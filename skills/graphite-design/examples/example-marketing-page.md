# Compose a marketing section

A restrained two-column hero. Use the product's actual copy and visual direction.

Read the startup guides in SKILL.md first. Replace the absolute document placeholder with the intended path. This example creates its own named frame and does not alter existing tokens.

```json
{
  "tool": "execute",
  "arguments": {
    "filePath": "/absolute/path/design.pen",
    "description": "Compose a marketing section",
    "input": "screen=Insert(document,{\"type\":\"frame\",\"name\":\"Product hero\",\"layout\":\"horizontal\",\"width\":980,\"height\":\"fit_content\",\"padding\":40,\"gap\":40,\"fill\":\"#fafafa\",\"children\":[{\"type\":\"frame\",\"name\":\"Hero copy\",\"layout\":\"vertical\",\"width\":470,\"height\":\"fit_content\",\"padding\":0,\"gap\":24,\"fill\":\"#fafafa\",\"children\":[{\"type\":\"text\",\"name\":\"A calmer way to work\",\"content\":\"A calmer way to work\",\"fontFamily\":\"Inter\",\"fontSize\":40,\"fill\":\"#171717\",\"fontWeight\":\"600\",\"textGrowth\":\"fixed-width\",\"width\":430},{\"type\":\"text\",\"name\":\"Bring your team\\u2019s projects into one clear workspace.\",\"content\":\"Bring your team\\u2019s projects into one clear workspace.\",\"fontFamily\":\"Inter\",\"fontSize\":14,\"fill\":\"#737373\",\"textGrowth\":\"fixed-width\",\"width\":420},{\"type\":\"frame\",\"name\":\"Create a workspace\",\"layout\":\"vertical\",\"width\":\"fill_container\",\"height\":40,\"padding\":[0,16],\"gap\":16,\"fill\":\"#171717\",\"children\":[{\"type\":\"text\",\"name\":\"Create a workspace\",\"content\":\"Create a workspace\",\"fontFamily\":\"Inter\",\"fontSize\":14,\"fill\":\"#fafafa\",\"fontWeight\":\"500\"}],\"alignItems\":\"center\",\"justifyContent\":\"center\",\"cornerRadius\":6}]},{\"type\":\"frame\",\"name\":\"Product preview\",\"layout\":\"vertical\",\"width\":400,\"height\":300,\"padding\":24,\"gap\":16,\"fill\":\"#f0f0f0\",\"children\":[{\"type\":\"text\",\"name\":\"Your workspace\",\"content\":\"Your workspace\",\"fontFamily\":\"Inter\",\"fontSize\":20,\"fill\":\"#171717\",\"fontWeight\":\"600\"},{\"type\":\"frame\",\"name\":\"Preview rows\",\"layout\":\"vertical\",\"width\":\"fill_container\",\"height\":\"fit_content\",\"padding\":24,\"gap\":16,\"fill\":\"#ffffff\",\"children\":[{\"type\":\"text\",\"name\":\"Product planning\",\"content\":\"Product planning\",\"fontFamily\":\"Inter\",\"fontSize\":14,\"fill\":\"#171717\"},{\"type\":\"text\",\"name\":\"Design review\",\"content\":\"Design review\",\"fontFamily\":\"Inter\",\"fontSize\":14,\"fill\":\"#171717\"},{\"type\":\"text\",\"name\":\"Next release\",\"content\":\"Next release\",\"fontFamily\":\"Inter\",\"fontSize\":14,\"fill\":\"#171717\"}]}],\"cornerRadius\":12}]});TakeScreenshot([screen]);"
  }
}
```
