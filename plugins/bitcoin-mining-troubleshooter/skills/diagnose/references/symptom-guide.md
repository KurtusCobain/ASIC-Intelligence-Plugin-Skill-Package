# Symptom interpretation guardrails

- Zero hash with a responsive management interface is different from a completely unreachable miner.
- Low hashrate alone does not identify the failed component.
- Missing chains/chips can indicate board, connector, power, control, initialization, or firmware-context problems; isolate before declaring hardware dead.
- Fan/thermal symptoms may be primary or protective responses to another condition.
- Pool failures must distinguish DNS, TCP reachability, Stratum connection, worker authorization, rejected shares, stale shares, and upstream pool status.
- Many miners failing together may indicate shared switch/network/PDU/breaker/feed/cooling problems instead of simultaneous miner hardware failures.
- A repair that worked once is not a universal fix. Preserve sample size and recurrence evidence.
