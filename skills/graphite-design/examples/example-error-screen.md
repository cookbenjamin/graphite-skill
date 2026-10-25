# Compose an offline state

Explain the failure and give one useful recovery action.

Read the startup guides in SKILL.md first. Replace the absolute document placeholder with the intended path. This example creates its own named frame and does not alter existing tokens.

```json
{
  "tool": "execute",
  "arguments": {
    "filePath": "/absolute/path/design.pen",
    "description": "Compose an offline state",
    "input": "screen=Insert(document,{\"type\":\"frame\",\"name\":\"Offline state\",\"layout\":\"vertical\",\"width\":390,\"height\":\"fit_content\",\"padding\":32,\"gap\":16,\"fill\":\"#fafafa\",\"children\":[{\"type\":\"text\",\"name\":\"You\\u2019re offline\",\"content\":\"You\\u2019re offline\",\"fontFamily\":\"Inter\",\"fontSize\":28,\"fill\":\"#171717\",\"fontWeight\":\"600\"},{\"type\":\"text\",\"name\":\"Reconnect to load your workspace. Your saved changes are still here.\",\"content\":\"Reconnect to load your workspace. Your saved changes are still here.\",\"fontFamily\":\"Inter\",\"fontSize\":14,\"fill\":\"#737373\",\"textGrowth\":\"fixed-width\",\"width\":320},{\"type\":\"frame\",\"name\":\"Try again\",\"layout\":\"vertical\",\"width\":\"fill_container\",\"height\":40,\"padding\":[0,16],\"gap\":16,\"fill\":\"#171717\",\"children\":[{\"type\":\"text\",\"name\":\"Try again\",\"content\":\"Try again\",\"fontFamily\":\"Inter\",\"fontSize\":14,\"fill\":\"#fafafa\",\"fontWeight\":\"500\"}],\"alignItems\":\"center\",\"justifyContent\":\"center\",\"cornerRadius\":6}]});TakeScreenshot([screen]);"
  }
}
```
