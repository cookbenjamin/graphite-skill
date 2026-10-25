# Client tool wrappers

The logical Graphite MCP names are `read_skill`, `get_app_state`, `execute`, `browser` and `get_style` in Claude Code and Codex. Discover/load deferred tools before calling them. A client may expose wrapper names such as `mcp__graphite__execute`; inspect the available tools instead of inventing a namespace.

Use native file-reading tools to read this skill's on-demand Markdown references. Canvas edits and verification go through Graphite. The five argument schemas stay the same across clients. No extra standalone token, layout, screenshot, import or export tool is needed: those functions run in execute.

The installed server's guide is authoritative for its operations. This skill supplies design workflow and examples. An existing `graphite` skill may provide the same connection guide; both can coexist. Neither skill selects the unrelated `gt` CLI or a failed Pencil server for a Graphite canvas task.
