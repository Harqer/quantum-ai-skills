# Security

## Threat model

The plugin is static instruction content. The primary risk is supply-chain or instruction tampering in future repository changes.

## Controls

- No MCP server.
- No hooks or executable scripts.
- No credentials or OAuth configuration.
- No network endpoints.
- No provider-specific account access.
- Pin installs to reviewed tags/commits when possible.
- Protect `main` and require review for changes to `plugin.json`, marketplace metadata, `SKILL.md`, or `references/`.

Report unexpected instruction changes or malicious content through GitHub issues/security reporting once enabled.
