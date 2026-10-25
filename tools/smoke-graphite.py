#!/usr/bin/env python3
"""Run the packaged worked calls against an existing isolated Graphite app."""
from pathlib import Path
import argparse
import base64
import hashlib
import json
import selectors
import shutil
import struct
import subprocess
import tempfile
import time
import importlib.util

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / 'skills/graphite-design'
spec = importlib.util.spec_from_file_location('graphite_validation', ROOT / 'tools/validate-graphite.py')
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


class Client:
    def __init__(self, command):
        self.process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
        self.serial = 0

    def call(self, method, params):
        self.serial += 1
        self.process.stdin.write(json.dumps({'jsonrpc': '2.0', 'id': self.serial, 'method': method, 'params': params}) + '\n')
        self.process.stdin.flush()
        selector = selectors.DefaultSelector()
        selector.register(self.process.stdout, selectors.EVENT_READ)
        try:
            deadline = time.monotonic() + 60
            while time.monotonic() < deadline:
                if not selector.select(max(0, deadline - time.monotonic())):
                    break
                line = self.process.stdout.readline()
                if not line:
                    raise RuntimeError('MCP process exited before replying')
                response = json.loads(line)
                if response.get('id') != self.serial:
                    continue
                if 'error' in response:
                    raise RuntimeError(response['error'])
                return response['result']
            raise TimeoutError('MCP request timed out: ' + method)
        finally:
            selector.close()

    def tool(self, name, args, allow_error=False):
        response = self.call('tools/call', {'name': name, 'arguments': args})
        if response.get('isError') and not allow_error:
            raise RuntimeError(json.dumps(response))
        return response

    def notify(self, method):
        self.process.stdin.write(json.dumps({'jsonrpc': '2.0', 'method': method}) + '\n')
        self.process.stdin.flush()

    def close(self):
        self.process.stdin.close()
        try:
            self.process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            self.process.terminate()
            self.process.wait(timeout=5)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--command', nargs='+', required=True, help='Existing stdio MCP launcher and optional arguments')
    parser.add_argument('--library', type=Path, help='Original Pencil shadcn .lib.pen for the import example')
    parser.add_argument('--output', type=Path, help='Write verification JSON and PNGs outside the installed skill')
    args = parser.parse_args()
    client = Client(args.command)
    source_hash = digest(args.library) if args.library else None
    report = {'tools': [], 'examples': [], 'skipped': [], 'screenshots': 0}
    try:
        client.call('initialize', {'protocolVersion': '2025-06-18', 'capabilities': {}, 'clientInfo': {'name': 'graphite-skill-smoke', 'version': '0.9.0'}})
        client.notify('notifications/initialized')
        listed = client.call('tools/list', {})['tools']
        assert sorted(tool['name'] for tool in listed) == sorted(validator.TOOLS)
        client.tool('read_skill', {})
        client.tool('get_app_state', {})
        client.tool('read_skill', {'path': 'execute.md'})
        client.tool('get_style', {})
        client.tool('get_style', {'name': 'graphite'})
        report['tools'] = sorted(validator.TOOLS)
        if args.output:
            args.output.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(prefix='graphite-skill-smoke-') as directory:
            directory = Path(directory)
            if args.library:
                (directory / 'libraries').mkdir()
                shutil.copyfile(args.library, directory / 'libraries/shadcn.lib.pen')
            reference = directory / 'reference.html'
            reference.write_text('<!doctype html><title>Graphite skill test</title><p>Local reference</p>')
            for example in sorted((SKILL / 'examples').glob('*.md')):
                if example.stem == 'example-import-library' and not args.library:
                    report['skipped'].append({'name': example.stem, 'reason': 'Original kit fixture not supplied'})
                    continue
                file = directory / (example.stem + '.pen')
                file.write_text(json.dumps({'version': '2.21', 'children': []}))
                call = next(validator.calls(example))
                call['arguments']['filePath'] = str(file)
                response = client.tool(call['tool'], call['arguments'])
                images = [item for item in response.get('content', []) if item['type'] == 'image']
                assert images, 'Example must actually render: ' + example.stem
                for i, image in enumerate(images):
                    png = base64.b64decode(image['data'])
                    assert png[:8] == b'\x89PNG\r\n\x1a\n'
                    width, height = struct.unpack('>II', png[16:24])
                    assert 0 < width <= 16384 and 0 < height <= 16384
                    if args.output:
                        (args.output / f'{example.stem}-{i}.png').write_bytes(png)
                assert not any('Renderer warnings' in item.get('text', '') for item in response.get('content', []))
                assert json.loads(file.read_text())['children'], 'Example did not persist a drawing'
                report['screenshots'] += len(images)
                report['examples'].append({'name': example.stem, 'images': len(images)})
                print('Passed ' + example.stem, flush=True)
            # Exercise the fifth tool against an owned local file, with no remote navigation.
            client.tool('browser', {'filePath': str(file), 'action': 'load-page', 'url': reference.as_uri()})
            # Validate persistence and rollback/repair through the actual server.
            before = file.read_bytes()
            bad = 'scratch=Insert(document,{type:"rectangle",name:"Repair fixture",width:20,height:20,fill:"#f00"});throw new Error("smoke fixture");'
            failed = client.tool('execute', {'filePath': str(file), 'input': bad}, allow_error=True)
            assert failed.get('isError')
            assert file.read_bytes() == before
            text = '\n'.join(item.get('text', '') for item in failed.get('content', []))
            import re
            edit_id = failed.get('editId')
            if not edit_id:
                # Graphite returns retry metadata as JSON text alongside its diagnostic.
                for item in failed.get('content', []):
                    try:
                        data = json.loads(item.get('text', ''))
                        edit_id = data.get('editId') or edit_id
                    except (json.JSONDecodeError, AttributeError):
                        continue
            if not edit_id:
                match = re.search(r'^editId:\s*(\S+)', text, re.M)
                edit_id = match[1] if match else None
            assert edit_id, text
            repaired = client.tool('execute', {'filePath': str(file), 'editId': edit_id, 'edits': [{'find': 'throw new Error("smoke fixture");', 'replace': 'TakeScreenshot([scratch]);'}]})
            assert any(item['type'] == 'image' for item in repaired['content'])
            client.tool('execute', {'filePath': str(file), 'input': 'Print(Get(scratch).name);'})
            report['rollbackAndRepair'] = True
            report['bindingsPersist'] = True
            if args.library:
                assert digest(args.library) == source_hash
                assert digest(directory / 'libraries/shadcn.lib.pen') == source_hash
                report['libraryUnchanged'] = True
        if args.output:
            (args.output / 'validation.json').write_text(json.dumps(report, indent=2) + '\n')
        print(json.dumps(report, indent=2))
    finally:
        client.close()


if __name__ == '__main__':
    main()
