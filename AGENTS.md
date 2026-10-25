# Graphite design skill: project context

This fork adapts Nisus74/pencil-skill for the independent Graphite Electron canvas. Read README.md and UPSTREAM.md for scope and attribution.

The core artifact is skills/graphite-design/SKILL.md. Keep its entrypoint concise and use references for design depth. Graphite's five top-level tools are read_skill, get_app_state, execute, browser and get_style. The connected server's read_skill guide determines supported operation semantics. Canvas reads/edits and verification use Graphite MCP; Markdown and source edits in this repository use ordinary file tools.

Preserve user scope, existing tokens, themes and third-party kit files. Do not add universal requirements to rename layers, backfill context, create dark modes, take a fixed number of screenshots or delegate work. Treat the design references as context-sensitive aids. Never present design notes as implemented interactive behavior.

Keep API recipes and all worked example calls consistent with the five-tool contract. Instance paths cross ref boundaries only. Imports qualify IDs, variable names and axes; preserve existing aliases and inspect actual component IDs. Supplied IDs are regenerated; assigned JSON bindings persist per document.

The skill directory and frontmatter name are graphite-design; plugin names match. Keep versions synchronized across SKILL metadata, platform manifests and the marketplace entry. Use supported frontmatter fields and manifest fields. Do not add a custom permissions frontmatter field: declarations in a Markdown file do not grant execution permissions.

Run tools/skill-lint.py, tools/test_skill_lint.py and tools/validate-graphite.py. Run tools/smoke-graphite.py with an isolated app when testing execute examples. Keep external kit assets and local app paths out of commits. Preserve the MIT license in the repository and the installable skill folder.
