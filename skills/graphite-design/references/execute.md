# Execute semantics

Load `read_skill({path:"execute.md"})` for the installed server's current function reference. This skill uses those functions inside the `input` string of `execute({filePath,input})`.

| Function | Result / detail |
| --- | --- |
| `Insert(parent,properties)` | Generated ID; nested child trees are supported by Graphite |
| `Copy(id,parent?,overrides?)` | Connected instance for reusable sources; ordinary nodes receive new subtree IDs |
| `Replace(id,properties)` | New ID; use for a replacement or a type change |
| `Update(id,properties)` | Merge properties; cannot replace children or change type/ref/id |
| `Move(id,parent?,index?)`, `Delete(id)` | Structural edits; inherited instance nodes have restrictions |
| `Get(id?,visitor?,options?)`, `Find(query)` | Schema reads/search; use a visitor for native bounds |
| `GetVariables()`, `SetVariables(values,replace?)` | Read tokens before merging changes; merge still overwrites supplied keys |
| `SetThemes(themes)` | Declare axes explicitly, preserving existing axes |
| `FindEmptySpace(options)` | Native collision-aware placement, including optional parentId |
| `TakeScreenshot(ids,options?)` | Inline rendered images |
| `Export(ids,format,outputPath,options?)` | PNG/JPEG/WebP/PDF/HTML output |
| `Select(ids)`, `Focus(ids)`, `Print(...values)` | Selection, viewport and text output |
| `Generate(...)` | Provider-dependent; read `generate.md` and inspect availability first |

Assigned JSON bindings persist for each document. `const`/`let` bindings are local to a call. Supplied node IDs are regenerated; retain returned IDs. `Get` returns node objects, while edit operations take ID strings. A slash crosses an instance boundary, not each nested frame.

Imports can be attached with `Update(document,{imports:{...}})` and used in the same execution. Preserve existing aliases. Imported source nodes and variables are read-only from consumers. See [component-anatomy.md](component-anatomy.md).

Ordinary JavaScript loops and comments are supported. A thrown error rolls back the complete call, persistent bindings and staged outputs. Do not catch an operation error merely to report success. Retry only after resolving its actual cause.

Use meaningful batches for the task; there is no fixed eight-operation limit. Worker and rendering budgets are documented by the installed MCP guide. Split large work when it would exceed those budgets or become hard to review.
