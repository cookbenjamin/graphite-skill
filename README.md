# Graphite design skill

A Graphite adaptation of [Nisus74/pencil-skill](https://github.com/Nisus74/pencil-skill). It retains the upstream design references and provides a concise entrypoint, current five-tool recipes and 15 executable worked examples for the independent Graphite Electron canvas.

The MCP API is `read_skill`, `get_app_state`, `execute`, `browser`, `get_style`. Reads, edits, layout inspection, screenshots and exports run through execute functions. The connected server's own guide determines available operations and renderer limits. This skill does not install Graphite or an MCP server.

## Install

Copy `skills/graphite-design` into `~/.codex/skills/graphite-design` for Codex or `~/.claude/skills/graphite-design` for Claude Code. Preserve an existing different skill instead of overwriting it. It can coexist with Graphite's small built-in connection skill named `graphite`.

For a reproducible installation with Codex's skill-installer helper, use this repository and a reviewed commit ref with path `skills/graphite-design`. The same folder is used by both clients. The skill will be available after the client's skill catalogue refreshes.

The repository also contains Claude Code and Codex plugin manifests. For a Claude Code marketplace install, add `cookbenjamin/graphite-skill`, then install `graphite-design@graphite-design`. Folder installation is sufficient for ordinary skill discovery and avoids a duplicate plugin/skill installation.

## Use

Ask for an interface design or edit in Graphite, or invoke `$graphite-design`. The skill loads the connected server's current guide, inspects the intended document and uses existing components and tokens. It supports local `.lib.pen` imports, including an unchanged original Pencil shadcn kit supplied separately. Third-party kit assets are not bundled here.

Design references are loaded as needed. Examples cover forms, dashboards, marketing, mobile, states, charts, reusable variants, native placement and original-kit imports. Product behavior described in design notes is distinct from a working app implementation.

## Validation

```sh
python3 tools/skill-lint.py
python3 tools/test_skill_lint.py
python3 tools/validate-graphite.py
python3 tools/smoke-graphite.py --command /absolute/path/graphite-mcp
```

The smoke command needs a running Graphite app. Set `GRAPHITE_SOCKET` to an isolated app socket for testing and optionally supply `--library /path/to/shadcn.lib.pen` for the original-kit example. It creates temporary documents and leaves source libraries unchanged. The static checks do not by themselves establish visual quality or upstream rendering parity.

## Attribution

Forked from Nisus74/pencil-skill at commit `28ec61cefe3000a59bdac6b98b83168dbacca9c8`. The original MIT license and Travis Polland copyright are preserved. See [UPSTREAM.md](UPSTREAM.md) for adaptation scope. This community skill is independent of Pencil and does not refer to the `gt` stacked-PR product.
