# FAQ

## Is this a miner-control tool?

No. It is intentionally read-only diagnostic decision support.

## Does it connect directly to my mine?

No. The public project analyzes evidence you provide to the AI session. It does not ship a hosted collection service or remote-management backend.

## What files can I use?

Common examples include miner logs, CSV/JSON/XLSX fleet exports, screenshots, repair history, network output, power/thermal evidence, and incident notes.

## Why does the response include “Do not claim yet”?

Because operational evidence is frequently incomplete. The project is designed to separate what is observed from what is inferred and to make uncertainty visible.

## Why keep Unknown separate from zero?

A missing measurement and a measured zero describe different states. Treating missing data as zero can create false restart, failure, temperature, fan, or hashrate patterns.

## Is the demo data real?

No. The five public scenarios are intentionally synthetic and sanitized. They are large enough to test fleet-level reasoning without publishing a real operator's network or worker data.

## Can I sponsor development?

Yes. See [Funding and sponsorship](FUNDING.md). The project remains free; sponsorship supports continued public development and validation.

## Can a company fund a specific compatibility or evaluation effort?

Yes, subject to the project's safety and independence boundaries. Company sponsorship does not buy a preferred diagnostic conclusion or equipment-control capability.
