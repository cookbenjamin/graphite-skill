# Graphite shell commands

Use the configured Graphite MCP server for ordinary agent editing. These commands operate the same local app and are useful when the user requests shell launch, connection setup or exports:

```sh
graphite open /absolute/path/design.pen
graphite serve /absolute/path/design.pen
graphite state
graphite execute --file /absolute/path/design.pen --input operations.js
graphite screenshot ./out.png --file /absolute/path/design.pen --node actual-id
graphite export ./out.pdf --file /absolute/path/design.pen --node actual-id --format pdf
```

`serve` starts without a visible window. It still uses Electron and the native renderer. It is not a standalone cloud generator and does not imply a configured image provider. Relative output paths are resolved by the CLI before export; use explicit paths for handoff. Graphite can open and create documents through its File menu or an explicit execute path.

`graphite mcp` starts stdio MCP. `graphite config codex` and `graphite config claude` print client configuration; `graphite connect codex` or `graphite connect claude` registers the server when the user asks for that setup. Inspect existing settings before modifying them. This skill does not authorize changing MCP configuration or installing applications merely because a connection failed.

Only use commands that the local CLI actually supports. Avoid unrelated `gt` commands: Graphite's stacked-PR tool is a different product.
