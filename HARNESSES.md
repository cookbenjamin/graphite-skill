# Client support

Claude Code and Codex use the same skills/graphite-design folder. Their local folder targets are ~/.claude/skills and ~/.codex/skills. Repository manifests provide optional plugin packaging; the installed skill does not require a plugin marketplace.

Both clients need a working Graphite MCP server. Discover client wrappers and deferred tools rather than hardcoding a host-specific wrapper. Logical tool names and JSON arguments are shared. This fork's API examples target Graphite's five tools and use its live read_skill documentation.

Optional upstream design-system templates and references remain platform-independent Markdown. Tools, authorization boundaries and actual renderer capabilities take precedence over descriptive design advice.
