# Compose a mobile project list

A bounded mobile frame with a simple navigation region.

Read the startup guides in SKILL.md first. Replace the absolute document placeholder with the intended path. This example creates its own named frame and does not alter existing tokens.

```json
{
  "tool": "execute",
  "arguments": {
    "filePath": "/absolute/path/design.pen",
    "description": "Compose a mobile project list",
    "input": "screen=Insert(document,{\"type\":\"frame\",\"name\":\"Projects mobile\",\"layout\":\"vertical\",\"width\":390,\"height\":844,\"padding\":24,\"gap\":16,\"fill\":\"#fafafa\",\"children\":[{\"type\":\"text\",\"name\":\"Projects\",\"content\":\"Projects\",\"fontFamily\":\"Inter\",\"fontSize\":28,\"fill\":\"#171717\",\"fontWeight\":\"600\"},{\"type\":\"frame\",\"name\":\"Project list\",\"layout\":\"vertical\",\"width\":\"fill_container\",\"height\":\"fill_container\",\"padding\":0,\"gap\":16,\"fill\":\"#fafafa\",\"children\":[{\"type\":\"frame\",\"name\":\"Product planning\",\"layout\":\"vertical\",\"width\":\"fill_container\",\"height\":\"fit_content\",\"padding\":24,\"gap\":16,\"fill\":\"#ffffff\",\"children\":[{\"type\":\"text\",\"name\":\"Product planning\",\"content\":\"Product planning\",\"fontFamily\":\"Inter\",\"fontSize\":14,\"fill\":\"#171717\",\"fontWeight\":\"500\"},{\"type\":\"text\",\"name\":\"Updated today\",\"content\":\"Updated today\",\"fontFamily\":\"Inter\",\"fontSize\":12,\"fill\":\"#737373\"}],\"cornerRadius\":8},{\"type\":\"frame\",\"name\":\"Design review\",\"layout\":\"vertical\",\"width\":\"fill_container\",\"height\":\"fit_content\",\"padding\":24,\"gap\":16,\"fill\":\"#ffffff\",\"children\":[{\"type\":\"text\",\"name\":\"Design review\",\"content\":\"Design review\",\"fontFamily\":\"Inter\",\"fontSize\":14,\"fill\":\"#171717\",\"fontWeight\":\"500\"},{\"type\":\"text\",\"name\":\"Updated today\",\"content\":\"Updated today\",\"fontFamily\":\"Inter\",\"fontSize\":12,\"fill\":\"#737373\"}],\"cornerRadius\":8},{\"type\":\"frame\",\"name\":\"Next release\",\"layout\":\"vertical\",\"width\":\"fill_container\",\"height\":\"fit_content\",\"padding\":24,\"gap\":16,\"fill\":\"#ffffff\",\"children\":[{\"type\":\"text\",\"name\":\"Next release\",\"content\":\"Next release\",\"fontFamily\":\"Inter\",\"fontSize\":14,\"fill\":\"#171717\",\"fontWeight\":\"500\"},{\"type\":\"text\",\"name\":\"Updated today\",\"content\":\"Updated today\",\"fontFamily\":\"Inter\",\"fontSize\":12,\"fill\":\"#737373\"}],\"cornerRadius\":8}]},{\"type\":\"frame\",\"name\":\"Bottom navigation\",\"layout\":\"horizontal\",\"width\":\"fill_container\",\"height\":\"fit_content\",\"padding\":16,\"gap\":16,\"fill\":\"#ffffff\",\"children\":[{\"type\":\"text\",\"name\":\"Projects\",\"content\":\"Projects\",\"fontFamily\":\"Inter\",\"fontSize\":14,\"fill\":\"#171717\",\"fontWeight\":\"600\"},{\"type\":\"text\",\"name\":\"Activity\",\"content\":\"Activity\",\"fontFamily\":\"Inter\",\"fontSize\":14,\"fill\":\"#737373\"},{\"type\":\"text\",\"name\":\"Profile\",\"content\":\"Profile\",\"fontFamily\":\"Inter\",\"fontSize\":14,\"fill\":\"#737373\"}],\"justifyContent\":\"space_between\"}]});TakeScreenshot([screen]);"
  }
}
```
