# Security Policy

ASIC Intelligence Plugin/Skill Package — Bitcoin Mining Troubleshooter is a read-only instruction/skill package. It does not require mining credentials or a hosted service.

## Reporting a security concern

For a security issue that is safe to discuss publicly and contains no sensitive operational details, a GitHub issue is acceptable.

For a vulnerability or report involving credentials, private infrastructure, unsanitized logs, confidential customer information, or another sensitive detail, **do not open a public GitHub issue**. Email **austin@wnclogiclab.com** with a subject beginning **`[SECURITY]`** and include only the minimum information needed to establish the issue. Redact secrets before sending whenever possible.

If a public reproduction can be created safely, reduce the case to sanitized evidence before posting it publicly.

Never paste these into a public issue:

- wallet seed phrases or private keys
- pool passwords, tokens, cookies, or API credentials
- real customer identities
- private internal network maps
- remote-access credentials
- unsanitized miner configuration files
- secrets embedded in screenshots or logs

## Scope

Security issues include accidental secret disclosure in distributed files, unsafe instructions that contradict the read-only boundary, package-integrity problems, prompt or evidence handling that could override the intended diagnostic contract, and evidence handling that could cause a user to mistake an unsupported inference for a confirmed operational fact.
