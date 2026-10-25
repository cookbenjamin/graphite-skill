# Create connected button variants

A local reusable origin and two connected instances demonstrate inheritance without a new theme axis.

Read the startup guides in SKILL.md first. Replace the absolute document placeholder with the intended path. This example creates its own named frame and does not alter existing tokens.

```json
{
  "tool": "execute",
  "arguments": {
    "filePath": "/absolute/path/design.pen",
    "description": "Create connected button variants",
    "input": "origin=Insert(document,{\"type\": \"frame\", \"name\": \"Primary action\", \"layout\": \"vertical\", \"width\": 160, \"height\": 40, \"padding\": [0, 16], \"gap\": 16, \"fill\": \"#171717\", \"children\": [{\"type\": \"text\", \"name\": \"Continue\", \"content\": \"Continue\", \"fontFamily\": \"Inter\", \"fontSize\": 14, \"fill\": \"#fafafa\", \"fontWeight\": \"500\"}], \"alignItems\": \"center\", \"justifyContent\": \"center\", \"cornerRadius\": 6, \"reusable\": true});secondary=Copy(origin,document,{name:'Secondary action',x:200,fill:'#525252'});disabled=Copy(origin,document,{name:'Disabled action',x:400,opacity:0.5,context:'Disabled visual state; implementation prevents activation.'});TakeScreenshot([origin,secondary,disabled]);"
  }
}
```
