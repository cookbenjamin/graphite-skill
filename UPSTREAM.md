# Upstream and Graphite adaptation

- Upstream: https://github.com/Nisus74/pencil-skill
- Base commit: 28ec61cefe3000a59bdac6b98b83168dbacca9c8
- Fork: https://github.com/cookbenjamin/graphite-skill
- Adaptation version: 0.9.0
- Adapted on: 2026-10-25

The fork preserves the upstream MIT license and design references. It replaces the large Pencil entrypoint with scoped Graphite guidance; rewrites the tool cookbook, execute semantics, schema routing, components, advanced canvas and CLI guidance; and ports all 15 worked examples to the five-tool API. Examples distinguish original library IDs from generated instance IDs and static design from implemented product behavior.

Outdated standalone-tool calls and automatic theme-registration assumptions are removed. Implicit broad renaming, required extra modes, fixed screenshot quotas and unsupported configuration fallbacks are not part of the workflow. The server's live read_skill documentation remains authoritative for rendering and operation support.

Platform manifests point to this fork and the same graphite-design skill folder. A copy of LICENSE travels with the installable skill. Original Pencil design assets are external user libraries, not repository content.

For future updates, fetch upstream, compare changed design references and port relevant improvements deliberately. Do not merge its old API recipes over the verified Graphite adapters.
