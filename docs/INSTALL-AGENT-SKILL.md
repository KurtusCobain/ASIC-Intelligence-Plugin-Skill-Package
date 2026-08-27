# Portable Agent Skill

`distributions/agent-skill/bitcoin-mining-troubleshooter-agent-skill-v1.1.0.zip` contains the platform-neutral troubleshooting skill and its reference files without a Codex- or Claude-specific plugin wrapper.

Use this package with products that support the Agent Skills open standard or provide a compatible skill-import mechanism.

## What is included

- `SKILL.md` — evidence-grounded diagnostic workflow
- `references/evidence-guide.md` — evidence handling and provenance rules
- `references/symptom-guide.md` — mining symptom categories
- `references/safety.md` — read-only safety boundary

## What is not included

- mining-control APIs
- remote network scanning
- credentials or secrets
- hosted backend
- account system
- payment or checkout flow

The skill is designed to reason over evidence provided in the active session.
