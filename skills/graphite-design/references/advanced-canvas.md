# Advanced Graphite canvas features

Read `read_skill({path:"scripts-and-shaders.md"})` before authoring shaders or script nodes. The live guide defines source headers, typed inputs, uniforms, array bindings, generated children and capture behavior. Do not substitute a historical Pencil example for those formats.

Graphite supports native GLSL paints and ordered shader effects, object/background/SDF textures, numeric and sampler arrays, mesh gradients and script-derived artwork. Some encodings are Graphite extensions; exact upstream pixel parity remains unverified. Derived script children are read-only through the agent API until converted using supported operations.

Ellipse arcs/rings use `innerRadius`, `startAngle` and `sweepAngle`. Paths use SVG geometry, optional viewBox and fillRule. Refer to `pen-schema.md` for supported paint/effect fields. Browser nodes use isolated Chromium pages and can be operated with the `browser` tool; read `browser-devices.md` for preset values.

Inspect `get_app_state().generation.available` and read `generate.md` before requesting image or vector generation. A missing provider is an availability issue, not permission to invent completed assets or silently switch services. Use an available agent image tool when the task warrants it and the user has authorized that workflow.

Check native captures and exports after advanced changes, keep warnings visible, and distinguish canvas rendering from implementation intent. A motion or interaction specification alone does not create a running application.
