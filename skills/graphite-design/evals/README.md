# Behavioral evaluation

The scenarios in evals.json check tool choice, task scope, native visual review, original-library preservation and accurate provider reporting. They are prompts for a permitted agent evaluation, not claims that every scenario has been independently run.

`tools/validate-graphite.py` validates the packaged references and five-tool example calls. `tools/smoke-graphite.py` executes worked examples against a running isolated Graphite app when an MCP command is supplied. Its output distinguishes executed examples from an unavailable external-kit fixture.
