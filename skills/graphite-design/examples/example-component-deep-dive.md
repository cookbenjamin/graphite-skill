# Inspect and override a component

Discover a generated label ID before writing an instance override.

Read the startup guides in SKILL.md first. Replace the absolute document placeholder with the intended path. This example creates its own named frame and does not alter existing tokens.

```json
{
  "tool": "execute",
  "arguments": {
    "filePath": "/absolute/path/design.pen",
    "description": "Inspect and override a component",
    "input": "origin=Insert(document,{\"type\": \"frame\", \"name\": \"Reusable action\", \"layout\": \"vertical\", \"width\": 160, \"height\": 40, \"padding\": [0, 16], \"gap\": 16, \"fill\": \"#171717\", \"children\": [{\"type\": \"text\", \"name\": \"Continue\", \"content\": \"Continue\", \"fontFamily\": \"Inter\", \"fontSize\": 14, \"fill\": \"#fafafa\", \"fontWeight\": \"500\"}], \"alignItems\": \"center\", \"justifyContent\": \"center\", \"cornerRadius\": 6, \"reusable\": true});const tree=Get(origin,{depth:2});labelId=tree.children[0].id;instance=Copy(origin,document,{name:'Save action',x:200,descendants:{[labelId]:{content:'Save changes'}}});Print(Get(instance,{resolveInstances:true,depth:2}));TakeScreenshot([instance]);"
  }
}
```
