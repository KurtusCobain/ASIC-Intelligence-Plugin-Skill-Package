# Evidence guide

Treat evidence according to its source.

1. Direct measurement: external meter/PDU/network measurement supplied by the user.
2. Miner-reported telemetry: API or status-page values supplied by the user.
3. Management-platform telemetry: values from scanner/fleet-management exports supplied by the user.
4. Vendor specification: exact model/variant figures from an authoritative source.
5. Derived values: calculations from known inputs.

Keep these categories distinct. Do not overwrite a measured value with a nameplate specification or present a derived estimate as a direct measurement.

Useful evidence can include hashrate, average hashrate, expected rate, board/chip counts, fan RPM, temperatures, power, uptime, accepted/rejected/stale shares, pool state, timestamps, and shared network/power topology.

## Data-quality rules

- Preserve explicit units from the source. Do not strip `GH/s`, `TH/s`, watts, RPM, temperature units, or time units and then guess them later.
- Missing/blank/null/unparseable fields stay **Unknown** and must not be converted to numeric zero.
- Keep explicit zero distinct from Unknown.
- For derived fleet rates or grouped counts, disclose the denominator and relevant excluded/Unknown rows.
- A scanner success/response flag proves only that a response was returned; it does not prove healthy hashing, Stratum connectivity, authorization, or accepted shares.
- Treat obvious sentinel-looking telemetry (for example repeated `255` values) as invalid/Unknown unless vendor/schema evidence establishes a physical meaning.
