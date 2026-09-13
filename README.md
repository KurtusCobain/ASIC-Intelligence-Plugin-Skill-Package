# Bitcoin Mining Troubleshooter

**Powered by ASIC Intelligence**  
**Read-only Bitcoin ASIC diagnostics from the evidence you already have.**

[Use in ChatGPT](https://chatgpt.com/plugins/plugins_6a90d9a9a63c81919cf452b0c4dcb665) · [Watch the demo](https://youtube.com/shorts/905z066Pj1M?si=rXnNoSENwMMUHKf1) · [Website](https://kurtuscobain.github.io/ASIC-Intelligence-Plugin-Skill-Package/)

Bitcoin Mining Troubleshooter analyzes user-provided miner logs, fleet exports, spreadsheets, screenshots, telemetry, repair history, network output, power/thermal evidence, and incident notes. It separates what the evidence says from what can reasonably be inferred, keeps uncertainty visible, and recommends the safest next diagnostic observation.

It does **not** reboot miners, change pools, flash firmware, alter tuning, switch power equipment, rewrite network settings, or execute equipment-control actions.

> **Product boundary:** Bitcoin Mining Troubleshooter is a standalone product. **ASIC Intelligence Desktop is a separate product** in development and is not required to use the Troubleshooter.

## Availability

- **ChatGPT — live:** [Use Bitcoin Mining Troubleshooter in ChatGPT](https://chatgpt.com/plugins/plugins_6a90d9a9a63c81919cf452b0c4dcb665)
- **Claude — marketplace approval pending:** the current v1.1.0 package remains available for manual Claude Code use.
- **Codex — available:** downloadable v1.1.0 skills package.
- **Portable Agent Skill — available:** platform-neutral v1.1.0 package.

## Install

The current public package release is **v1.1.0**.

### Install for Codex

Download [`bitcoin-mining-troubleshooter-codex-v1.1.0.zip`](https://github.com/KurtusCobain/ASIC-Intelligence-Plugin-Skill-Package/releases/download/v1.1.0/bitcoin-mining-troubleshooter-codex-v1.1.0.zip) and read [Codex installation](docs/INSTALL-CODEX.md).

### Install for Claude

Download [`bitcoin-mining-troubleshooter-claude-v1.1.0.zip`](https://github.com/KurtusCobain/ASIC-Intelligence-Plugin-Skill-Package/releases/download/v1.1.0/bitcoin-mining-troubleshooter-claude-v1.1.0.zip) and read [Claude Code installation](docs/INSTALL-CLAUDE.md). Marketplace approval is pending; this download is the manual v1.1.0 package.

### Portable Agent Skill

Download [`bitcoin-mining-troubleshooter-agent-skill-v1.1.0.zip`](https://github.com/KurtusCobain/ASIC-Intelligence-Plugin-Skill-Package/releases/download/v1.1.0/bitcoin-mining-troubleshooter-agent-skill-v1.1.0.zip) and read [Agent Skill installation](docs/INSTALL-AGENT-SKILL.md).

## Diagnostic trust contract

A strong diagnosis should distinguish:

1. **Observed evidence** — what a supplied source actually says.
2. **Derived findings** — calculations or correlations produced from that evidence.
3. **General mining knowledge** — domain context used to interpret the evidence.
4. **Assumptions** — stated explicitly rather than hidden inside a conclusion.
5. **Conflicting evidence** — sources that disagree.
6. **Missing evidence** — what remains unknown.
7. **Freshness** — current, recent, historical, or unknown-age evidence.
8. **Confidence** — High, Medium, Low, or Insufficient Evidence.
9. **Shared-cause reasoning** — common rack, network, power, cooling, firmware, or timing patterns before mass independent hardware failure.
10. **Next safe read-only check** — the observation that removes the most uncertainty with the least work.
11. **What would change the conclusion** — evidence that would support a competing explanation.

“Insufficient Evidence” is a valid result. Missing values remain **Unknown** instead of silently becoming zero. Explicit units stay attached to measurements. Scanner response is not treated as proof of healthy mining or pool authorization. Shared rack, network, power, cooling, firmware, and timing patterns are considered before isolated component failure is assumed.

## Fleet-scale demo suite

The repository includes **5 fleet-scale synthetic scenarios** representing **21,470 primary miner/case records**, plus longitudinal repair events, across CSV, XLSX, JSONL, and NDJSON. The public demos contain no real customer credentials, wallets, production network configuration, or operator-identifying data.

| Demo | Scale | Evidence |
| --- | ---: | --- |
| Fleet restart / recovery | 5,250 miners | CSV |
| Network segment incident | 4,800 miners | XLSX |
| Power / thermal operations | 4,920 miners | XLSX |
| Repair history | 3,500 miners / 12,050 events | JSONL |
| Miner log corpus | 3,000 cases | NDJSON |

Start with [`demos/README.md`](demos/README.md) and [`demos/DEMO-SCRIPT.md`](demos/DEMO-SCRIPT.md).

## ASIC Intelligence Desktop is separate

Bitcoin Mining Troubleshooter and ASIC Intelligence Desktop are different products.

The Troubleshooter is the standalone public diagnostic tool in this repository. It analyzes evidence intentionally supplied to the active AI session and does not require a persistent mining-site backend.

ASIC Intelligence Desktop is a separate mining-operations intelligence product in development. Its proprietary runtime, private implementation architecture, customer integrations, and development material are not included in or licensed by this repository.

## Repository name

The GitHub repository retains the historical name **ASIC Intelligence Plugin/Skill Package** for continuity with the v1.1.0 release and existing links. The user-facing product name is **Bitcoin Mining Troubleshooter**, powered by ASIC Intelligence.

## Use it. Integrate it. Fund it.

**Use it** — open the ChatGPT plugin or install the free package and test it against sanitized mining evidence.  
**Integrate it** — vendors and tool builders can help validate public evidence formats and compatibility.  
**Fund it** — sponsors and mining-industry design partners can support continued public work or separately scoped ASIC Intelligence development.

Read [Funding](docs/FUNDING.md) and [Partners](docs/PARTNERS.md). For private partnership discussions: **[austin@wnclogiclab.com](mailto:austin@wnclogiclab.com)**.

## Safety and security

See [Safety and scope](docs/SAFETY.md), [Security](SECURITY.md), [FAQ](docs/FAQ.md), and [Contributing](CONTRIBUTING.md).

For sensitive security reports, **do not post secrets or private operational evidence in a public issue**. Use the private reporting route documented in [SECURITY.md](SECURITY.md).

## Website

The GitHub Pages website is served from [`docs/`](docs/).

## Version

Current public release: **v1.1.0**

A newer candidate may exist in private/review workflows, but it is not a public release until its release gates are complete.

## License

This repository is **source-available** under the **PolyForm Shield License 1.0.0**. See [LICENSE](LICENSE) and [NOTICE](NOTICE) for the controlling terms and required notice.
