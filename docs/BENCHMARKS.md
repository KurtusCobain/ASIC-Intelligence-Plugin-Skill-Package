# Benchmark Methodology

The public demo suite is designed for **blind diagnostic evaluation**, not for showing an assistant the answer and asking it to paraphrase it.

## Five evidence domains

1. Fleet restart/recovery telemetry
2. Shared network reachability incident
3. Power and thermal operations evidence
4. Longitudinal repair history
5. Miner-log triage corpus

Together they represent more than 20,000 miner/evidence records across CSV, XLSX, JSONL, and NDJSON.

## What a good run is evaluated for

- factual extraction accuracy
- correct handling of Unknown/missing values
- preservation of source units
- useful derived metrics with transparent denominators
- separation of unreachable from reachable zero-hash states
- recognition of shared versus miner-specific patterns
- appropriate confidence and uncertainty
- resistance to premature component diagnosis
- one discriminating read-only next check

## Blind use

Use the prompts in `demos/DEMO-SCRIPT.md`. Do not tell the assistant which pattern was intentionally planted. A public tester should judge whether the reasoning is supported by the evidence in the supplied file.

The public repository intentionally does not include hidden scoring answers or planted-case answer keys.
