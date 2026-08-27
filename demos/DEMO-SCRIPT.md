# 5-Demo Script — Bitcoin Mining Troubleshooter v1.1.0

## Demo 1 — Fleet restart / recovery
Attach `01-fleet-restart-recovery.csv`.

**Prompt:**
> Analyze this BTC Tools-style fleet scan. What is the dominant operational pattern, what does the evidence actually prove, and what should I check next?

**Follow-up:**
> Are all of the zero-hash miners broken? Show me the strongest grouped comparison and tell me what you still cannot prove.

## Demo 2 — Network segment incident
Attach `02-network-segment-incident.xlsx`.

**Prompt:**
> Diagnose this fleet workbook. Separate unreachable miners from reachable zero-hash miners and identify whether the evidence supports a shared network problem or widespread miner hardware failures.

**Follow-up:**
> Which shared grouping is most suspicious, and what single read-only observation would best test that hypothesis?

## Demo 3 — Power / thermal operations
Attach `03-power-thermal-operations.xlsx`.

**Prompt:**
> Analyze this operations workbook. Determine whether the dominant underperformance pattern is better supported by miner hardware, electrical loading, or environmental conditions. Keep physical capacity, measured power, and live hashing evidence separate.

**Follow-up:**
> What evidence argues against the strongest alternative explanation?

## Demo 4 — Repair history
Attach `04-repair-history.jsonl`.

**Prompt:**
> Review this repair history across the fleet. Find the strongest recurring pattern, distinguish technician labels from confirmed root cause, and tell me whether any historical diagnoses deserve re-evaluation.

**Follow-up:**
> What changed over time, and what can you infer from the before/after pattern without overclaiming causation?

## Demo 5 — Miner log corpus
Attach `05-miner-log-corpus.ndjson`.

**Prompt:**
> Triage this 3,000-miner log corpus. Rank the main fault domains, identify shared signatures, and avoid forcing one cause onto unrelated failures.

**Follow-up:**
> Which problems look shared versus miner-specific, and what is the single most useful read-only next check for the largest affected group?
