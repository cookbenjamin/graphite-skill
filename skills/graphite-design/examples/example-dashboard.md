# Compose a dashboard summary

Use hierarchy and a simple native chart to establish a data overview.

Read the startup guides in SKILL.md first. Replace the absolute document placeholder with the intended path. This example creates its own named frame and does not alter existing tokens.

```json
{
  "tool": "execute",
  "arguments": {
    "filePath": "/absolute/path/design.pen",
    "description": "Compose a dashboard summary",
    "input": "screen=Insert(document,{\"type\":\"frame\",\"name\":\"Dashboard\",\"layout\":\"vertical\",\"width\":640,\"height\":\"fit_content\",\"padding\":24,\"gap\":16,\"fill\":\"#fafafa\",\"children\":[{\"type\":\"text\",\"name\":\"Workspace overview\",\"content\":\"Workspace overview\",\"fontFamily\":\"Inter\",\"fontSize\":24,\"fill\":\"#171717\",\"fontWeight\":\"600\"},{\"type\":\"frame\",\"name\":\"Metrics\",\"layout\":\"horizontal\",\"width\":\"fill_container\",\"height\":\"fit_content\",\"padding\":0,\"gap\":16,\"fill\":\"#fafafa\",\"children\":[{\"type\":\"frame\",\"name\":\"Revenue\",\"layout\":\"vertical\",\"width\":220,\"height\":\"fit_content\",\"padding\":24,\"gap\":16,\"fill\":\"#fafafa\",\"children\":[{\"type\":\"text\",\"name\":\"Revenue\",\"content\":\"Revenue\",\"fontFamily\":\"Inter\",\"fontSize\":14,\"fill\":\"#737373\"},{\"type\":\"text\",\"name\":\"$24,580\",\"content\":\"$24,580\",\"fontFamily\":\"Inter\",\"fontSize\":28,\"fill\":\"#171717\",\"fontWeight\":\"600\"}]},{\"type\":\"frame\",\"name\":\"Customers\",\"layout\":\"vertical\",\"width\":220,\"height\":\"fit_content\",\"padding\":24,\"gap\":16,\"fill\":\"#fafafa\",\"children\":[{\"type\":\"text\",\"name\":\"Customers\",\"content\":\"Customers\",\"fontFamily\":\"Inter\",\"fontSize\":14,\"fill\":\"#737373\"},{\"type\":\"text\",\"name\":\"1,280\",\"content\":\"1,280\",\"fontFamily\":\"Inter\",\"fontSize\":28,\"fill\":\"#171717\",\"fontWeight\":\"600\"}]}]},{\"type\":\"frame\",\"name\":\"Activity chart\",\"layout\":\"horizontal\",\"width\":\"fill_container\",\"height\":140,\"padding\":16,\"gap\":12,\"fill\":\"#f5f5f5\",\"children\":[{\"type\":\"rectangle\",\"name\":\"Day 1\",\"width\":24,\"height\":44,\"fill\":\"#2563eb\"},{\"type\":\"rectangle\",\"name\":\"Day 2\",\"width\":24,\"height\":60,\"fill\":\"#2563eb\"},{\"type\":\"rectangle\",\"name\":\"Day 3\",\"width\":24,\"height\":48,\"fill\":\"#2563eb\"},{\"type\":\"rectangle\",\"name\":\"Day 4\",\"width\":24,\"height\":84,\"fill\":\"#2563eb\"},{\"type\":\"rectangle\",\"name\":\"Day 5\",\"width\":24,\"height\":72,\"fill\":\"#2563eb\"},{\"type\":\"rectangle\",\"name\":\"Day 6\",\"width\":24,\"height\":108,\"fill\":\"#2563eb\"},{\"type\":\"rectangle\",\"name\":\"Day 7\",\"width\":24,\"height\":96,\"fill\":\"#2563eb\"}],\"alignItems\":\"end\"}]});TakeScreenshot([screen]);"
  }
}
```
