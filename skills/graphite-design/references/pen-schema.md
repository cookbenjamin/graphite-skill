# Graphite .pen schema

Read `read_skill({path:"pen-schema.md"})` for the renderer's supported format. The published Pencil format supplies interchange context, while the installed guide identifies Graphite extensions and gaps. Do not assume that all browser CSS, runtime interactions or future Pencil properties are canvas features.

Documents have a string `version` and `children`, with optional `imports`, `variables` and `themes`. New documents currently use version `2.21`. Existing older libraries can load unchanged; do not rewrite an original kit merely to change its version.

Useful node types include frame/group, text, rectangle, ellipse, polygon, path, line, icon, ref, browser and script. Use `content` for text. Set a text fill explicitly when authoring. Text defaults to unwrapped automatic growth: choose `textGrowth:"fixed-width"` or `"fixed-width-height"` for wrapping.

Flex layout uses `layout:"horizontal"|"vertical"`, `gap`, `padding`, `alignItems:"start"|"center"|"end"` and `justifyContent:"start"|"center"|"end"|"space_between"|"space_around"`. Padding is a number, two values or four values. Sizes are numbers, `fill_container` or `fit_content`, optionally with numeric fallbacks. The fallback syntax is not a CSS max-width or breakpoint expression.

Fills can be color strings, fill objects or ordered arrays. New strokes use `stroke` plus `strokeWidth`; legacy stroke objects remain supported for interoperability. Icons use `type:"icon",library:"lucide",icon:"plus"`; legacy icon_font nodes in original kits can remain unchanged. Inter, Geist and Geist Mono are bundled. Other fonts need to be available on the host; review missing-font and missing-icon warnings.

Variables are `{type:"color"|"number"|"string"|"boolean",value:...}` and referenced as `$name`. A themed value is an array of `{value,theme}` entries on a variable. Declare axes through `SetThemes`, preserving existing axes. A consumer's imported names and axes are qualified (`$ui:--primary`, `ui:Mode`).

Slots, shader annotations, scripts, effect ordering, exact paint formats and browser device options need their corresponding live guide. `context` documents behavior for implementation; it does not make a static drawing interactive or accessible by itself.
