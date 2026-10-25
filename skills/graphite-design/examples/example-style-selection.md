# Apply a style without overwriting existing tokens

Choose local reference values, add only missing variables, and preserve the document's current themes.

Read the startup guides in SKILL.md first. Replace the absolute document placeholder with the intended path. This example creates its own named frame and does not alter existing tokens.

```json
{
  "tool": "execute",
  "arguments": {
    "filePath": "/absolute/path/design.pen",
    "description": "Apply a style without overwriting existing tokens",
    "input": "const existing=GetVariables();const defaults={demoSurface:{type:'color',value:'#fafafa'},demoInk:{type:'color',value:'#171717'},demoFont:{type:'string',value:'Inter'}};SetVariables(Object.fromEntries(Object.entries(defaults).filter(([key])=>!Object.hasOwn(existing,key))));screen=Insert(document,{type:'frame',name:'Style sample',layout:'vertical',width:360,height:180,padding:24,fill:'$demoSurface',children:[{type:'text',name:'Title',content:'A clear starting point',fontFamily:'$demoFont',fontSize:24,fill:'$demoInk'}]});TakeScreenshot([screen]);"
  }
}
```
