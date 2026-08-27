# ASIC Intelligence Plugin/Skill Package

**Bitcoin Mining Troubleshooter**  
**Powered by ASIC Intelligence**

> Turn mining evidence into the next diagnostic step.

ASIC Intelligence Plugin/Skill Package is the public, free, **Read-only** diagnostic package from ASIC Intelligence. It packages the Bitcoin Mining Troubleshooter for **Codex**, **Claude Code**, and compatible **Agent Skill** systems. Give it miner logs, BTC Tools-style fleet exports, spreadsheets, repair history, screenshots, network output, power/thermal evidence, or an incident description. It separates what the evidence says from what can be inferred, makes uncertainty visible, and recommends the safest next diagnostic observation.

It does **not** reboot miners, change pools, flash firmware, alter tuning, switch power equipment, rewrite network settings, or execute equipment-control actions.

## Install

### Install for Codex

Download [`bitcoin-mining-troubleshooter-codex-v1.1.0.zip`](distributions/codex/bitcoin-mining-troubleshooter-codex-v1.1.0.zip) and read [Codex installation](docs/INSTALL-CODEX.md).

### Install for Claude

Download [`bitcoin-mining-troubleshooter-claude-v1.1.0.zip`](distributions/claude/bitcoin-mining-troubleshooter-claude-v1.1.0.zip) and read [Claude Code installation](docs/INSTALL-CLAUDE.md).

### Portable Agent Skill

Download [`bitcoin-mining-troubleshooter-agent-skill-v1.1.0.zip`](distributions/agent-skill/bitcoin-mining-troubleshooter-agent-skill-v1.1.0.zip) and read [Agent Skill installation](docs/INSTALL-AGENT-SKILL.md).

## Diagnostic trust contract

A strong diagnosis should distinguish:

1. **Observed evidence** — what a supplied source actually says.
2. **Derived findings** — calculations/correlations produced from that evidence.
3. **General mining knowledge** — domain context used to interpret the evidence.
4. **Assumptions** — stated explicitly rather than hidden inside a conclusion.
5. **Conflicting evidence** — sources that disagree.
6. **Missing evidence** — what is unavailable and how that limits the answer.
7. **Freshness** — current, recent, historical, or unknown-age evidence.
8. **Likely causes** — ranked without overstating certainty.
9. **Confidence** — High, Medium, Low, or **Insufficient Evidence**.
10. **Next safe read-only check** — the observation that removes the most uncertainty with the least work.
11. **What would change the conclusion** — evidence that would support a competing explanation.

“Insufficient Evidence” is a valid successful result. Missing values remain **Unknown** instead of silently becoming zero. Explicit units stay attached to measurements. Scanner response is not treated as proof of healthy mining or pool authorization. Shared rack, network, power, cooling, firmware, and timing patterns are considered before isolated component failure is assumed.

## Fleet-scale demo suite

The repository includes **5 fleet-scale synthetic scenarios** spanning more than **20,000 miner/evidence records** across CSV, XLSX, JSONL, and NDJSON. The public demos contain no real customer credentials, wallets, production network configuration, or operator-identifying data.

| Demo | Scale | Evidence |
| --- | ---: | --- |
| Fleet restart / recovery | 5,250 miners | CSV scanner export |
| Network segment incident | 4,800 miners | Multi-sheet XLSX |
| Power / thermal operations | 4,920 miners | Multi-sheet XLSX |
| Repair history | 3,500 miners / 12,050 events | JSONL |
| Miner log corpus | 3,000 miners | NDJSON |

Start with [`demos/README.md`](demos/README.md) and [`demos/DEMO-SCRIPT.md`](demos/DEMO-SCRIPT.md).

## About ASIC Intelligence

ASIC Intelligence is being developed as a broader mining-intelligence product for operators who need more than one-shot evidence analysis. This public package demonstrates the evidence-first diagnostic philosophy while keeping the commercial platform's proprietary implementation separate.

The public repository does **not** contain the proprietary ASIC Intelligence commercial runtime, private implementation architecture, customer integrations, private evaluator answers, or development recovery bundle.

## Use it. Integrate it. Fund it.

**Use it** — install the free package and test it against your mining evidence.  
**Integrate it** — vendors and tool builders can help validate public evidence formats and compatibility.  
**Fund it** — sponsors and mining-industry design partners can support continued public work or separate ASIC Intelligence development.

Read [Funding](docs/FUNDING.md) and [Partners](docs/PARTNERS.md). For private partnership discussions: **[austin@wnclogiclab.com](mailto:austin@wnclogiclab.com)**.

## Safety and privacy

The package is diagnostic decision support, not equipment control. Operational evidence can contain wallet addresses, pool credentials, tokens, public IPs, employee names, serial numbers, internal DNS names, and facility identifiers. Avoid posting unsanitized operational evidence to public issues.

See [Safety and scope](docs/SAFETY.md), [Security](SECURITY.md), [FAQ](docs/FAQ.md), and verify downloads with [SHA256SUMS](SHA256SUMS).

## Website

The GitHub Pages website is served from [`docs/`](docs/) after public launch.

## Version

Current release: **v1.1.0**

## License

This repository is **source-available under the PolyForm Shield License 1.0.0**. The license permits use, modification, and redistribution for permitted purposes, but does not permit using the software to provide a product that competes with this software or other products the licensor or its affiliates provide using it. See [`LICENSE`](LICENSE) and [`NOTICE`](NOTICE) for the controlling terms. Separately developed private ASIC Intelligence products, systems, customer data, and trademarks are not licensed by this repository. For commercial licensing or partnership questions, contact **[austin@wnclogiclab.com](mailto:austin@wnclogiclab.com)**.
