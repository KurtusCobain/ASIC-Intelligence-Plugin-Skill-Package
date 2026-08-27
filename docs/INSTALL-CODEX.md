# Install for Codex / ChatGPT

The v1.1.0 Codex package is a skills-only plugin. It contains diagnostic instructions and references; it does not require an external app, account connection, or mining-control service.

## Package

Download:

`distributions/codex/bitcoin-mining-troubleshooter-codex-v1.1.0.zip`

## ChatGPT Skills route

OpenAI Skills follow the Agent Skills standard. In ChatGPT, eligible users can open **Plugins → Skills → Create → Upload from your computer** and upload a compatible skill package. If you prefer this route, use the portable Agent Skill package in `distributions/agent-skill/`.

## Plugin route

For a managed workspace or Codex surface that supports plugins, install or import the Codex plugin package according to the plugin controls available to your account/workspace. Skills-only plugins do not require an underlying connected app.

Workspace installation can depend on plan, role, workspace settings, and supported surface. If the plugin is not available to install, ask the workspace administrator to review plugin installation permissions.

## Test prompt

Attach `demos/01-fleet-restart-recovery.csv` and ask:

> Analyze this BTC Tools-style fleet scan. What is the dominant operational pattern, what does the evidence actually prove, and what should I check next?

Then ask:

> Are all of the zero-hash miners broken? Show me the strongest grouped comparison and tell me what you still cannot prove.

## Expected behavior

The skill should preserve explicit units and Unknown values, separate observed facts from derived metrics and hypotheses, avoid treating scanner response as proof of healthy mining, and finish with a read-only diagnostic check.
