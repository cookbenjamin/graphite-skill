# Compose a first-use state

Lead with a useful first action rather than adding an entire tutorial by default.

Read the startup guides in SKILL.md first. Replace the absolute document placeholder with the intended path. This example creates its own named frame and does not alter existing tokens.

```json
{
  "tool": "execute",
  "arguments": {
    "filePath": "/absolute/path/design.pen",
    "description": "Compose a first-use state",
    "input": "screen=Insert(document,{\"type\":\"frame\",\"name\":\"First project\",\"layout\":\"vertical\",\"width\":360,\"height\":\"fit_content\",\"padding\":24,\"gap\":16,\"fill\":\"#fafafa\",\"children\":[{\"type\":\"text\",\"name\":\"Make room for your next idea\",\"content\":\"Make room for your next idea\",\"fontFamily\":\"Inter\",\"fontSize\":28,\"fill\":\"#171717\",\"fontWeight\":\"600\",\"textGrowth\":\"fixed-width\",\"width\":312},{\"type\":\"text\",\"name\":\"Create a project to keep its plans, files and decisions together.\",\"content\":\"Create a project to keep its plans, files and decisions together.\",\"fontFamily\":\"Inter\",\"fontSize\":14,\"fill\":\"#737373\",\"textGrowth\":\"fixed-width\",\"width\":312},{\"type\":\"frame\",\"name\":\"Create a project\",\"layout\":\"vertical\",\"width\":\"fill_container\",\"height\":40,\"padding\":[0,16],\"gap\":16,\"fill\":\"#171717\",\"children\":[{\"type\":\"text\",\"name\":\"Create a project\",\"content\":\"Create a project\",\"fontFamily\":\"Inter\",\"fontSize\":14,\"fill\":\"#fafafa\",\"fontWeight\":\"500\"}],\"alignItems\":\"center\",\"justifyContent\":\"center\",\"cornerRadius\":6}]});TakeScreenshot([screen]);"
  }
}
```
