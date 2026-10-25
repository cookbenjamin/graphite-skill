# Create a compact sign-in form

A new form composition. Reuse a project Input or Button component instead when one already fits.

Read the startup guides in SKILL.md first. Replace the absolute document placeholder with the intended path. This example creates its own named frame and does not alter existing tokens.

```json
{
  "tool": "execute",
  "arguments": {
    "filePath": "/absolute/path/design.pen",
    "description": "Create a compact sign-in form",
    "input": "screen=Insert(document,{\"type\":\"frame\",\"name\":\"Sign in\",\"layout\":\"vertical\",\"width\":360,\"height\":\"fit_content\",\"padding\":24,\"gap\":16,\"fill\":\"#fafafa\",\"children\":[{\"type\":\"text\",\"name\":\"Welcome back\",\"content\":\"Welcome back\",\"fontFamily\":\"Inter\",\"fontSize\":24,\"fill\":\"#171717\",\"fontWeight\":\"600\"},{\"type\":\"text\",\"name\":\"Use your work email to continue.\",\"content\":\"Use your work email to continue.\",\"fontFamily\":\"Inter\",\"fontSize\":14,\"fill\":\"#737373\"},{\"type\":\"frame\",\"name\":\"Email\",\"layout\":\"vertical\",\"width\":\"fill_container\",\"height\":\"fit_content\",\"padding\":0,\"gap\":8,\"fill\":\"#fafafa\",\"children\":[{\"type\":\"text\",\"name\":\"Email\",\"content\":\"Email\",\"fontFamily\":\"Inter\",\"fontSize\":12,\"fill\":\"#171717\"},{\"type\":\"frame\",\"name\":\"Email input\",\"layout\":\"vertical\",\"width\":\"fill_container\",\"height\":40,\"padding\":[0,12],\"gap\":16,\"fill\":\"#fafafa\",\"children\":[{\"type\":\"text\",\"name\":\"Enter email\",\"content\":\"Enter email\",\"fontFamily\":\"Inter\",\"fontSize\":14,\"fill\":\"#737373\"}],\"justifyContent\":\"center\",\"stroke\":\"#d4d4d4\",\"strokeWidth\":1,\"cornerRadius\":6}]},{\"type\":\"frame\",\"name\":\"Password\",\"layout\":\"vertical\",\"width\":\"fill_container\",\"height\":\"fit_content\",\"padding\":0,\"gap\":8,\"fill\":\"#fafafa\",\"children\":[{\"type\":\"text\",\"name\":\"Password\",\"content\":\"Password\",\"fontFamily\":\"Inter\",\"fontSize\":12,\"fill\":\"#171717\"},{\"type\":\"frame\",\"name\":\"Password input\",\"layout\":\"vertical\",\"width\":\"fill_container\",\"height\":40,\"padding\":[0,12],\"gap\":16,\"fill\":\"#fafafa\",\"children\":[{\"type\":\"text\",\"name\":\"Enter password\",\"content\":\"Enter password\",\"fontFamily\":\"Inter\",\"fontSize\":14,\"fill\":\"#737373\"}],\"justifyContent\":\"center\",\"stroke\":\"#d4d4d4\",\"strokeWidth\":1,\"cornerRadius\":6}]},{\"type\":\"frame\",\"name\":\"Sign in\",\"layout\":\"vertical\",\"width\":\"fill_container\",\"height\":40,\"padding\":[0,16],\"gap\":16,\"fill\":\"#171717\",\"children\":[{\"type\":\"text\",\"name\":\"Sign in\",\"content\":\"Sign in\",\"fontFamily\":\"Inter\",\"fontSize\":14,\"fill\":\"#fafafa\",\"fontWeight\":\"500\"}],\"alignItems\":\"center\",\"justifyContent\":\"center\",\"cornerRadius\":6}],\"cornerRadius\":12});TakeScreenshot([screen]);"
  }
}
```

Labels and controls are drawings. Document validation and keyboard intent when requested; this does not implement a live form.
