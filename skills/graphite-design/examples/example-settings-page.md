# Compose a settings form

Use grouped fields and one clear save action.

Read the startup guides in SKILL.md first. Replace the absolute document placeholder with the intended path. This example creates its own named frame and does not alter existing tokens.

```json
{
  "tool": "execute",
  "arguments": {
    "filePath": "/absolute/path/design.pen",
    "description": "Compose a settings form",
    "input": "screen=Insert(document,{\"type\":\"frame\",\"name\":\"Profile settings\",\"layout\":\"vertical\",\"width\":420,\"height\":\"fit_content\",\"padding\":24,\"gap\":16,\"fill\":\"#fafafa\",\"children\":[{\"type\":\"text\",\"name\":\"Profile\",\"content\":\"Profile\",\"fontFamily\":\"Inter\",\"fontSize\":24,\"fill\":\"#171717\",\"fontWeight\":\"600\"},{\"type\":\"text\",\"name\":\"Manage how your team sees you.\",\"content\":\"Manage how your team sees you.\",\"fontFamily\":\"Inter\",\"fontSize\":14,\"fill\":\"#737373\"},{\"type\":\"frame\",\"name\":\"Display name\",\"layout\":\"vertical\",\"width\":\"fill_container\",\"height\":\"fit_content\",\"padding\":0,\"gap\":8,\"fill\":\"#fafafa\",\"children\":[{\"type\":\"text\",\"name\":\"Display name\",\"content\":\"Display name\",\"fontFamily\":\"Inter\",\"fontSize\":12,\"fill\":\"#171717\"},{\"type\":\"frame\",\"name\":\"Display name input\",\"layout\":\"vertical\",\"width\":\"fill_container\",\"height\":40,\"padding\":[0,12],\"gap\":16,\"fill\":\"#fafafa\",\"children\":[{\"type\":\"text\",\"name\":\"Enter display name\",\"content\":\"Enter display name\",\"fontFamily\":\"Inter\",\"fontSize\":14,\"fill\":\"#737373\"}],\"justifyContent\":\"center\",\"stroke\":\"#d4d4d4\",\"strokeWidth\":1,\"cornerRadius\":6}]},{\"type\":\"frame\",\"name\":\"Email\",\"layout\":\"vertical\",\"width\":\"fill_container\",\"height\":\"fit_content\",\"padding\":0,\"gap\":8,\"fill\":\"#fafafa\",\"children\":[{\"type\":\"text\",\"name\":\"Email\",\"content\":\"Email\",\"fontFamily\":\"Inter\",\"fontSize\":12,\"fill\":\"#171717\"},{\"type\":\"frame\",\"name\":\"Email input\",\"layout\":\"vertical\",\"width\":\"fill_container\",\"height\":40,\"padding\":[0,12],\"gap\":16,\"fill\":\"#fafafa\",\"children\":[{\"type\":\"text\",\"name\":\"Enter email\",\"content\":\"Enter email\",\"fontFamily\":\"Inter\",\"fontSize\":14,\"fill\":\"#737373\"}],\"justifyContent\":\"center\",\"stroke\":\"#d4d4d4\",\"strokeWidth\":1,\"cornerRadius\":6}]},{\"type\":\"frame\",\"name\":\"Save profile\",\"layout\":\"vertical\",\"width\":\"fill_container\",\"height\":40,\"padding\":[0,16],\"gap\":16,\"fill\":\"#171717\",\"children\":[{\"type\":\"text\",\"name\":\"Save profile\",\"content\":\"Save profile\",\"fontFamily\":\"Inter\",\"fontSize\":14,\"fill\":\"#fafafa\",\"fontWeight\":\"500\"}],\"alignItems\":\"center\",\"justifyContent\":\"center\",\"cornerRadius\":6}]});TakeScreenshot([screen]);"
  }
}
```
