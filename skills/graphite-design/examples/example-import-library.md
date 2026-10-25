# Use the original Pencil shadcn library

Requires an unchanged original kit at `libraries/shadcn.lib.pen` beside the target design. The kit is external and is not included in this repository. Inspect the actual imported catalog before general library work.

Read the startup guides in SKILL.md first. Replace the absolute document placeholder with the intended path. This example creates its own named frame and does not alter existing tokens.

```json
{
  "tool": "execute",
  "arguments": {
    "filePath": "/absolute/path/design.pen",
    "description": "Use the original Pencil shadcn library",
    "input": "const current=Get(document);Update(document,{imports:{...(current.imports||{}),ui:'./libraries/shadcn.lib.pen'}});screen=Insert(document,{type:'frame',name:'Shadcn actions',layout:'vertical',width:360,height:200,padding:24,gap:16,fill:'$ui:--background',theme:{'ui:Mode':'Dark','ui:Base':'Zinc','ui:Accent':'Blue'}});action=Copy('ui:VSnC2',screen,{name:'Primary action'});input=Copy('ui:1415a',screen,{name:'Email field',width:'fill_container'});Print(Get(action,{resolveInstances:true,depth:2}));TakeScreenshot([screen]);"
  }
}
```

`VSnC2` and `1415a` are original IDs from Pencil extension 0.6.78. Alias-qualified variables and theme axes preserve the original kit. Other libraries have different IDs: inspect them, rather than treating these as universal names.
