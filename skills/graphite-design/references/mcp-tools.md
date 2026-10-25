# Graphite MCP calls

The server exposes exactly five tools. Client wrappers vary: discover `graphite` tools, then call the logical names below. Their argument schemas do not change by client.

```json
{"tool":"read_skill","arguments":{}}
```
```json
{"tool":"get_app_state","arguments":{}}
```
```json
{"tool":"read_skill","arguments":{"path":"execute.md"}}
```

Use the confirmed absolute document path in execute. Here and in worked examples `/absolute/path/design.pen` is a placeholder, not a request to create that path.

```json
{"tool":"execute","arguments":{"filePath":"/absolute/path/design.pen","input":"Print(GetVariables()); Print(Get(document,{depth:2}));"}}
```

Use `Find({name:"Button"})` for a property search. Resolve instances or variables only when needed:

```js
Print(Get('actual-id',{resolveInstances:true,resolveVariables:true,depth:3}));
Print(Get('actual-id',(n,c)=>({id:n.id,bounds:c.bounds,problems:c.problems}),{depth:2,resolveInstances:true}));
```

These snippets are input strings to execute, not extra MCP tools. Narrow visitor scope to avoid expanding a large design unnecessarily. Native bounds are parent-relative border boxes. `FindEmptySpace` returns `{x,y,parentId?}`; use the returned parent when inserting among nested siblings.

```js
const where=FindEmptySpace({width:390,height:844,padding:64});
screen=Insert(where.parentId||document,{type:'frame',name:'Mobile screen',...where,width:390,height:844});
TakeScreenshot([screen]);
Export([screen],'png','./exports',{scale:2});
```

`TakeScreenshot` returns images. `Export` writes image/PDF files into an output directory, or HTML into a specified filename. Screenshots default to 1×; image exports default to 2×. Call `read_skill` for the current output limits. Keep source/library/image paths out of export destinations.

```json
{"tool":"get_style","arguments":{}}
```
```json
{"tool":"get_style","arguments":{"name":"graphite"}}
```

Styles return reference values. They do not attach libraries or change document variables. Preserve existing tokens when applying a chosen style.

For a requested web reference, browser actions are `load-page`, `import-to-canvas`, `screenshot-to-canvas`, `return-element`, `return-screenshot` and `cdp`. All require `filePath` and `action`. For an existing local reference file, replace both placeholder paths in this call:

```json
{"tool":"browser","arguments":{"filePath":"/absolute/path/design.pen","action":"load-page","url":"file:///absolute/path/reference.html"}}
```

An element query uses `target:"query"` and `querySelector`. For canvas browser nodes, pass `nodeId` to target that node rather than a separate page. Read the live browser guide before importing layers or sending CDP commands.

When execute fails, the returned `editId` supports an exact source patch:

```json
{"tool":"execute","arguments":{"filePath":"/absolute/path/design.pen","editId":"returned-edit-id","edits":[{"find":"fontSize: 720","replace":"fontSize: 72"}]}}
```

Omit input in this repair form. `all`, when used, is a boolean. Failed transactions do not publish partial edits or exports. A concurrent file/library change requires rereading and retrying against current state.
