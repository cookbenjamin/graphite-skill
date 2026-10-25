---
name: graphite-design
description: Design and refine interfaces in the Graphite .pen canvas using reusable components, linked libraries, layout inspection, screenshots and exports. Use for UI composition, design systems and visual iteration in Graphite. Excludes the Graphite stacked-PR CLI and general frontend coding without a .pen design.
metadata:
  version: "0.9.0"
---

# Graphite interface design

Use the MCP server named `graphite`. Its complete top-level API is `read_skill`, `get_app_state`, `execute`, `browser` and `get_style`. Discover deferred tools when needed. This skill adds design guidance to the installed server's documentation; the server's current `read_skill` guides determine supported operations and schema.

## Start with the current design

Call `read_skill()` and `get_app_state({})` before editing, then `read_skill({path:"execute.md"})` before the first execute. Confirm the intended absolute `.pen` path from the state or the user's request. An explicit new path in `execute` creates a blank document; `filePath:""` selects the active document. A disconnected MCP server is a connection issue: inspect the existing configuration and report the actual failure. Do not switch to Pencil, install another editor or change credentials as a fallback.

Inspect the relevant subtree, reusable components, imports, variables and themes. Reuse components that fit the requested design. Existing tokens, user references and project conventions guide the work. Ask only for information that materially affects the result and cannot be inferred. Keep small edits small: a label correction does not authorize renaming a file, reorganizing layers, creating new themes or retokenizing a design.

## Use the five tools correctly

| Tool | Purpose |
| --- | --- |
| `read_skill({path?})` | Current server guide; `execute.md`, `pen-schema.md`, `guide/components.md`, `scripts-and-shaders.md`, `generate.md`, `browser-devices.md` |
| `get_app_state({})` | Active path, root nodes, selection, reusable components, imported libraries, tokens, themes, warnings and generation availability |
| `execute({filePath,input,description?})` | Read, edit, inspect native bounds, capture and export with JavaScript functions |
| `browser({filePath,action,...})` | Inspect a real page or import editable layers; use for the requested page or browser node |
| `get_style({name?,params?})` | List/reference local palettes; does not apply tokens or import a component library |

Reads are `Get`, `Find` and `GetVariables` **inside execute**. Native layout is `Get(id,(node,ctx)=>...)` with `ctx.bounds` and `ctx.problems`. Images are `TakeScreenshot`; files are `Export`, also inside execute. Read [references/mcp-tools.md](references/mcp-tools.md) for complete call examples and [references/execute.md](references/execute.md) for node/transaction semantics. [references/codex-tools.md](references/codex-tools.md) explains client wrappers.

Use real JavaScript and capture IDs returned by `Insert`, `Copy` and `Replace`. Supplied IDs are regenerated. Assigned JSON bindings persist per document between calls; local `const` and `let` do not. Use `Get(...).id` when passing a retrieved node to an operation that expects a string. A slash crosses an instance boundary; ordinary nested frames do not add path segments. `Update` cannot change `type`, `ref`, `id` or `children`; use structural operations. A failed execute rolls back edits, globals and staged exports. Repair it with the returned `editId` and exact `edits`, or issue a corrected snippet.

## Compose, review and finish

Preserve the visual direction and use the requested responsive targets and modes. For a new screen, establish its primary task and information hierarchy before adding decoration. Choose typography and density deliberately; the reference catalogues below offer options, not mandatory themes. Use meaningful names and document behavior when it helps implementation. Add semantic tokens when useful, inspecting existing values before changing them. Literal colors are valid when the task or asset calls for them.

Prefer flex layout for content and fixed coordinates for artwork. `fill_container` depends on a bounded parent; text wraps only with `textGrowth:"fixed-width"` or `"fixed-width-height"`. Inter, Geist and Geist Mono are bundled. A reference's other font suggestions require an available font, and missing-font warnings need resolution. See [references/pen-schema.md](references/pen-schema.md).

Make focused changes. Use native bounds to investigate overflow and screenshots to judge visible changes, contrast, typography and rhythm. Inspect the actual image and refine material problems. Select a useful crop and cadence for the task; there is no fixed number of screenshots, operations, screens or iterations. Keep renderer warnings visible and distinguish verified output from unsupported or unverified behavior.

For interaction specifications, consider relevant loading, error, empty, focus and disabled states. These are design representations and implementation notes; adding a `context` string does not implement keyboard behavior, forms or ARIA. Add modes, state families and additional screens when the task requires them. Do not invent product behavior or silently broaden a cosmetic request into an accessibility or design-system overhaul.

Finish with what changed, what was visually checked and any material remaining limitation. Export in the requested format. Optional design-system templates are available under [design-system/](design-system/README.md); use them when the user wants project documentation, rather than copying a documentation tree for every task.

## Components and original Pencil libraries

Read `read_skill({path:"guide/components.md"})` and [references/component-anatomy.md](references/component-anatomy.md) before unfamiliar instance or slot edits. Imports use relative `.pen`/`.lib.pen` paths and qualified IDs, variables and theme axes. For alias `ui`, use `ui:componentId`, `$ui:token` and `ui:Mode`. `Update(document,{imports:{...}})` can attach a library in Graphite; preserve existing aliases. Inspect the imported catalog for actual IDs and descendant paths.

Imported definitions stay read-only from a consumer. Local overrides and authored slot content belong to instances; edit a source file explicitly when the user wants to change the shared definition. Preserve third-party kit files when the task is to use them unchanged. The original Pencil shadcn kit can be imported directly; a local installation may live at `~/.local/share/graphite/libraries/pencil/shadcn.lib.pen`. Keep the kit's license/provenance with project-local copies. [examples/example-import-library.md](examples/example-import-library.md) uses its real IDs without bundling the third-party asset.

## Load design depth as needed

These references are design aids. Apply recommendations to the user's scope and existing product conventions; do not treat every recommendation as a universal requirement. Code-oriented accessibility, responsive and motion advice describes implementation intent unless the Graphite server documents a rendering feature.

| Task | References |
| --- | --- |
| Hierarchy, density, visual critique | [visual-hierarchy](references/visual-hierarchy.md), [design-eye](references/design-eye.md), [iteration-patterns](references/iteration-patterns.md) |
| Screen composition | [layout-patterns](references/layout-patterns.md), [industry-patterns](references/industry-patterns.md), [file-architecture](references/file-architecture.md) |
| Typography and visual direction | [typography](references/typography.md), [font-pairings](references/font-pairings.md), [colour-palettes](references/colour-palettes.md), [style-catalogue](references/style-catalogue.md) |
| Forms, text and controls | [forms](references/forms.md), [microcopy](references/microcopy.md), [iconography](references/iconography.md) |
| Flows, states and interaction intent | [flows](references/flows.md), [states](references/states.md), [interactions](references/interactions.md), [accessibility](references/accessibility.md) |
| Mobile and implementation patterns | [mobile-patterns](references/mobile-patterns.md), [modern-patterns](references/modern-patterns.md), [performance-design](references/performance-design.md) |
| Charts and dashboards | [data-viz](references/data-viz.md), [chart-anatomy](references/chart-anatomy.md) |
| Reusable design systems | [composition-patterns](references/composition-patterns.md), [component-anatomy](references/component-anatomy.md), [extract](references/extract.md) |
| Shaders, scripts and browser capture | [advanced-canvas](references/advanced-canvas.md), then the corresponding live MCP guide |
| Shell launch and file exports | [graphite-cli](references/graphite-cli.md); use the already configured MCP connection for ordinary editing |

Worked MCP calls for common requests live under [examples/](examples/example-login-screen.md). Each example assumes the startup guide calls above and uses `/absolute/path/design.pen` as a placeholder for the actual target. Do not execute a placeholder path.

Adapted from [Nisus74/pencil-skill](https://github.com/Nisus74/pencil-skill), with its MIT license preserved in [LICENSE](LICENSE). Graphite is an independent local canvas, separate from Pencil and from the `gt` stacked-PR tool.
