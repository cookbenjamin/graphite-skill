# Read and use components

Read the imported/reusable catalog from `get_app_state`. Inspect an unfamiliar definition with `execute({filePath,input:"Print(Get('ui:actualId',{resolveInstances:true,depth:4}));"})`, using actual IDs. A source's name is a label, not necessarily its ID. Libraries qualify node IDs, variable names and theme axes with the import alias.

`Copy('ui:buttonId',parent,overrides)` creates a connected instance. `Insert(parent,{type:'ref',ref:'ui:buttonId'})` also creates an instance. Override a label through its instance path or descendants map. A slash crosses a reference boundary only:

```js
button=Copy('ui:buttonId',document,{descendants:{'ui:labelId':{content:'Save'}}});
Update(button+'/ui:labelId',{content:'Continue'});
```

For an ordinary frame containing a label, the label's globally unique ID is its address; do not construct `frameId/labelId`. Across a nested component instance, use `outerId/ui:nestedRefId/ui:labelId`. Unique descendant names may be used in override maps; ambiguous names need explicit paths.

Identify slots in the read tree before filling them. `Insert(instanceId+'/ui:slotId',node)` appends authored slot content. `Replace` returns a new binding for a replacement. Inherited children cannot be freely moved or deleted; use `enabled:false` for an instance override when appropriate. `Update` cannot change children/type/ref; choose the relevant structural operation.

Inspect actual theme axes and values before setting an instance state. Preserve casing: the original Pencil shadcn kit uses `ui:Mode:'Dark'`, not `mode:'dark'`. A library can express variants with separate reusable refs, theme axes, or both. Do not invent a state axis for an existing component.

Imported definitions and variables are read-only from a consumer. Change the shared library only when that is the requested scope, targeting its own source file and unqualified IDs. Consumer overrides remain local when the library refreshes. Keep original third-party kits unchanged for an exact-kit import.

For a concrete original-kit call, see [example-import-library.md](../examples/example-import-library.md). Read `read_skill({path:'guide/components.md'})` for the complete current instance rules.
