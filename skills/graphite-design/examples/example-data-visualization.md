# Compose a bar comparison

Native rectangles with bounded widths preserve an easy-to-read comparison.

Read the startup guides in SKILL.md first. Replace the absolute document placeholder with the intended path. This example creates its own named frame and does not alter existing tokens.

```json
{
  "tool": "execute",
  "arguments": {
    "filePath": "/absolute/path/design.pen",
    "description": "Compose a bar comparison",
    "input": "screen=Insert(document,{\"type\":\"frame\",\"name\":\"Weekly activity\",\"layout\":\"vertical\",\"width\":420,\"height\":\"fit_content\",\"padding\":24,\"gap\":16,\"fill\":\"#fafafa\",\"children\":[{\"type\":\"text\",\"name\":\"Weekly activity\",\"content\":\"Weekly activity\",\"fontFamily\":\"Inter\",\"fontSize\":24,\"fill\":\"#171717\",\"fontWeight\":\"600\"},{\"type\":\"frame\",\"name\":\"Bars\",\"layout\":\"horizontal\",\"width\":\"fill_container\",\"height\":\"fit_content\",\"padding\":0,\"gap\":16,\"fill\":\"#fafafa\",\"children\":[{\"type\":\"frame\",\"name\":\"Mon\",\"layout\":\"vertical\",\"width\":50,\"height\":200,\"padding\":0,\"gap\":8,\"fill\":\"#fafafa\",\"children\":[{\"type\":\"rectangle\",\"name\":\"Mon bar\",\"width\":34,\"height\":80,\"fill\":\"#2563eb\"},{\"type\":\"text\",\"name\":\"Mon\",\"content\":\"Mon\",\"fontFamily\":\"Inter\",\"fontSize\":12,\"fill\":\"#737373\"}],\"justifyContent\":\"end\",\"alignItems\":\"center\"},{\"type\":\"frame\",\"name\":\"Tue\",\"layout\":\"vertical\",\"width\":50,\"height\":200,\"padding\":0,\"gap\":8,\"fill\":\"#fafafa\",\"children\":[{\"type\":\"rectangle\",\"name\":\"Tue bar\",\"width\":34,\"height\":110,\"fill\":\"#2563eb\"},{\"type\":\"text\",\"name\":\"Tue\",\"content\":\"Tue\",\"fontFamily\":\"Inter\",\"fontSize\":12,\"fill\":\"#737373\"}],\"justifyContent\":\"end\",\"alignItems\":\"center\"},{\"type\":\"frame\",\"name\":\"Wed\",\"layout\":\"vertical\",\"width\":50,\"height\":200,\"padding\":0,\"gap\":8,\"fill\":\"#fafafa\",\"children\":[{\"type\":\"rectangle\",\"name\":\"Wed bar\",\"width\":34,\"height\":96,\"fill\":\"#2563eb\"},{\"type\":\"text\",\"name\":\"Wed\",\"content\":\"Wed\",\"fontFamily\":\"Inter\",\"fontSize\":12,\"fill\":\"#737373\"}],\"justifyContent\":\"end\",\"alignItems\":\"center\"},{\"type\":\"frame\",\"name\":\"Thu\",\"layout\":\"vertical\",\"width\":50,\"height\":200,\"padding\":0,\"gap\":8,\"fill\":\"#fafafa\",\"children\":[{\"type\":\"rectangle\",\"name\":\"Thu bar\",\"width\":34,\"height\":144,\"fill\":\"#2563eb\"},{\"type\":\"text\",\"name\":\"Thu\",\"content\":\"Thu\",\"fontFamily\":\"Inter\",\"fontSize\":12,\"fill\":\"#737373\"}],\"justifyContent\":\"end\",\"alignItems\":\"center\"},{\"type\":\"frame\",\"name\":\"Fri\",\"layout\":\"vertical\",\"width\":50,\"height\":200,\"padding\":0,\"gap\":8,\"fill\":\"#fafafa\",\"children\":[{\"type\":\"rectangle\",\"name\":\"Fri bar\",\"width\":34,\"height\":120,\"fill\":\"#2563eb\"},{\"type\":\"text\",\"name\":\"Fri\",\"content\":\"Fri\",\"fontFamily\":\"Inter\",\"fontSize\":12,\"fill\":\"#737373\"}],\"justifyContent\":\"end\",\"alignItems\":\"center\"}],\"alignItems\":\"end\"}]});TakeScreenshot([screen]);"
  }
}
```
