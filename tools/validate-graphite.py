#!/usr/bin/env python3
"""Validate packaged Graphite references and worked MCP call arguments."""
from pathlib import Path
from urllib.parse import unquote
import json
import re

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / 'skills/graphite-design'
TOOLS = {
    'read_skill': ({'path'}, set()),
    'get_app_state': (set(), set()),
    'execute': ({'filePath', 'input', 'description', 'editId', 'edits'}, {'filePath'}),
    'browser': ({'filePath', 'action', 'url', 'nodeId', 'target', 'querySelector', 'method', 'params'}, {'filePath', 'action'}),
    'get_style': ({'name', 'params'}, set()),
}
LEGACY = re.compile(r'\b(?:batch_design|batch_get|get_editor_state|get_guidelines|snapshot_layout|get_screenshot|get_variables|export_nodes|export_html)\b')


def calls(path):
    for match in re.finditer(r'^```json\s*\n(.*?)^```', path.read_text(), re.M | re.S):
        data = json.loads(match[1])
        if isinstance(data, dict) and 'tool' in data:
            yield data


def main():
    errors = []
    count = 0
    for path in SKILL.rglob('*.md'):
        text = path.read_text()
        if LEGACY.search(text):
            errors.append(f'{path}: obsolete MCP tool name')
        for target in re.findall(r'\[[^\]]*\]\(([^\s)]+)(?:\s+"[^"]*")?\)', text):
            if target.startswith(('http:', 'https:', 'mailto:', '#')):
                continue
            target = unquote(target.strip('<>').split('#')[0])
            resolved = (path.parent / target).resolve()
            if not resolved.is_relative_to(SKILL) or not resolved.exists():
                errors.append(f'{path}: missing or unpackaged reference {target}')
        try:
            for call in calls(path):
                count += 1
                tool, args = call.get('tool'), call.get('arguments')
                if tool not in TOOLS or not isinstance(args, dict):
                    errors.append(f'{path}: invalid tool/arguments')
                    continue
                allowed, required = TOOLS[tool]
                if set(args) - allowed or required - set(args):
                    errors.append(f'{path}: invalid {tool} argument keys')
                if tool == 'execute':
                    if not isinstance(args.get('filePath'), str):
                        errors.append(f'{path}: execute needs a string filePath')
                    if 'input' not in args and not (args.get('editId') and args.get('edits')):
                        errors.append(f'{path}: execute needs input or repair arguments')
        except (json.JSONDecodeError, TypeError) as error:
            errors.append(f'{path}: {error}')
    examples = list((SKILL / 'examples').glob('*.md'))
    for path in examples:
        if len(list(calls(path))) != 1:
            errors.append(f'{path}: expected one standalone worked MCP call')
    if (SKILL / 'LICENSE').read_bytes() != (ROOT / 'LICENSE').read_bytes():
        errors.append('The original MIT license must travel with the installed skill.')
    skill_version = re.search(r'version: "([^"]+)"', (SKILL / 'SKILL.md').read_text())[1]
    for platform in ['.claude-plugin', '.cursor-plugin', '.codex-plugin']:
        manifest = json.loads((ROOT / platform / 'plugin.json').read_text())
        if manifest['name'] != 'graphite-design' or manifest['version'] != skill_version:
            errors.append(f'{platform}: inconsistent package metadata')
    marketplace = json.loads((ROOT / '.claude-plugin/marketplace.json').read_text())
    if marketplace['plugins'][0]['version'] != skill_version:
        errors.append('Marketplace version differs from the skill.')
    for error in errors:
        print(error)
    print(json.dumps({'examples': len(examples), 'mcpCalls': count, 'errors': len(errors)}))
    return bool(errors)


if __name__ == '__main__':
    raise SystemExit(main())
