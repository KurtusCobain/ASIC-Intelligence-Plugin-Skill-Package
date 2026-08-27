# Safety and Scope

Bitcoin Mining Troubleshooter provides **read-only diagnostic decision support**.

## In scope

- miner logs
- BTC Tools-style scanner exports
- fleet CSV/JSON/XLSX evidence
- screenshots
- repair history
- pool symptoms and connection evidence
- network command output supplied by the user
- power and thermal evidence supplied by the user
- incident descriptions

## Out of scope

The public project does not execute state-changing equipment actions. It must not instruct itself to perform or automatically perform:

- miner reboot or factory reset
- pool or wallet changes
- firmware flashing
- overclocking, tuning, or voltage changes
- static-IP or network reconfiguration
- PDU/breaker switching
- curtailment actions
- arbitrary shell commands that change operational state

If a possible remediation is state-changing, the troubleshooting response should instead recommend the read-only observation that would justify or reject that remediation.

## Evidence rules

- Missing, blank, and unparseable measurements remain **Unknown** rather than becoming zero.
- Explicit source units are preserved.
- Derived rates state their denominator and disclose excluded Unknown records when material.
- Scanner success means a response was returned; it does not by itself prove healthy hashing, pool authorization, accepted shares, or electrical health.
- Sentinel-looking telemetry is treated cautiously unless its meaning is established by the source schema or vendor documentation.
- Correlation by model, firmware, subnet, container, rack, or uptime is not automatically causation.
- Shared infrastructure hypotheses should be considered before hundreds of simultaneous observations are turned into hundreds of independent hardware diagnoses.

## Operational use

Use the output as decision support, not as a substitute for site procedures, electrical safety requirements, manufacturer guidance, or qualified personnel. Preserve original evidence before destructive troubleshooting such as resets or firmware changes.
