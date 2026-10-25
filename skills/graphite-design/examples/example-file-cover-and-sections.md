# Place a new frame without overlaps

Use native placement instead of assuming the document is empty.

Read the startup guides in SKILL.md first. Replace the absolute document placeholder with the intended path. This example creates its own named frame and does not alter existing tokens.

```json
{
  "tool": "execute",
  "arguments": {
    "filePath": "/absolute/path/design.pen",
    "description": "Place a new frame without overlaps",
    "input": "const where=FindEmptySpace({width:480,height:300,padding:64});screen=Insert(where.parentId||document,{type:'frame',name:'Project overview',...where,width:480,height:300,padding:32,layout:'vertical',gap:12,fill:'#fafafa',children:[{type:'text',name:'Project title',content:'Workspace design',fontFamily:'Inter',fontSize:28,fontWeight:'600',fill:'#171717'},{type:'text',name:'Scope',content:'The current product direction and key screens.',fontFamily:'Inter',fontSize:14,fill:'#737373'}]});Print(Get(screen,(n,c)=>{c.skipChildren();return c.bounds;}));TakeScreenshot([screen]);"
  }
}
```
