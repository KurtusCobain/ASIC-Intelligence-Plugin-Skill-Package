# Fleet-Scale Synthetic Demo Suite

These five scenarios are synthetic and intentionally omit their planted answer keys. Use them for blind evaluation of evidence extraction, uncertainty handling, common-cause reasoning, and safe next-check selection.

1. **Fleet restart / recovery** — 5,250-miner BTC Tools-style CSV.
2. **Network segment incident** — 4,800-miner multi-sheet XLSX.
3. **Power / thermal operations** — 4,920-miner multi-sheet XLSX.
4. **Repair history** — 3,500 miners with 12,050 longitudinal events in JSONL.
5. **Miner log corpus** — 3,000 synthetic miner cases in NDJSON.

The public repository does not include evaluator ground truth, expected findings, or scoring keys.

See [`DEMO-SCRIPT.md`](DEMO-SCRIPT.md) for blind prompts.
