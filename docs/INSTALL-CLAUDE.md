# Install for Claude Code

## Package

Download:

`distributions/claude/bitcoin-mining-troubleshooter-claude-v1.1.0.zip`

The archive contains a Claude Code plugin with `.claude-plugin/plugin.json` and a `skills/diagnose/SKILL.md` skill.

## Fast local test

Claude Code can load a plugin directory or ZIP directly for a session:

```bash
claude --plugin-dir ./bitcoin-mining-troubleshooter-claude-v1.1.0.zip
```

Inside Claude Code, invoke:

```text
/bitcoin-mining-troubleshooter:diagnose
```

You can also ask a mining troubleshooting question directly; Claude may select the skill from its description when appropriate.

## Validate before redistribution

If you are developing or repackaging the plugin, extract it and run:

```bash
claude plugin validate ./bitcoin-mining-troubleshooter
```

For stricter validation:

```bash
claude plugin validate --strict ./bitcoin-mining-troubleshooter
```

Validation status: the final v1.1.0 archive passes both `claude plugin validate` and `claude plugin validate --strict`. Claude Code plugin skills use the namespaced form `/bitcoin-mining-troubleshooter:diagnose`.

## Test prompt

Use one of the files in `demos/` and the blind prompts in `demos/DEMO-SCRIPT.md`.

The public plugin intentionally contains no MCP server, background monitor, miner-control command, remote credential flow, or automated equipment execution.
