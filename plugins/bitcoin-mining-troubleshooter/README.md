# Bitcoin Mining Troubleshooter for Claude Code

Read-only diagnostic plugin for user-provided Bitcoin ASIC mining evidence.

## Local test

From the parent directory:

```bash
claude --plugin-dir ./bitcoin-mining-troubleshooter
```

Claude can invoke the skill automatically when the task matches its description. You can also invoke the skill manually with `/bitcoin-mining-troubleshooter:diagnose`.

The plugin contains no MCP server, hooks, background monitor, miner-control tool, firmware action, pool-changing action, or backend.
