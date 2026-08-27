# Contributing

Contributions are welcome when they strengthen evidence-grounded, read-only Bitcoin mining troubleshooting.

## Good contributions

- sanitized miner-log patterns
- documentation for public miner/firmware behavior
- regression cases for missing values, units, timestamps, or ambiguous telemetry
- improvements to diagnostic uncertainty language
- synthetic fleet scenarios
- installation/documentation fixes
- platform packaging fixes

## Hard boundaries

Do not add equipment-control commands, pool changes, firmware flashing, reboot actions, tuning writes, PDU switching, credential automation, arbitrary shell execution, or other state-changing mining operations.

Do not submit real production evidence unless it is fully sanitized. Public fixtures must not contain customer names, private IP maps copied from production, MAC addresses copied from production, real pool workers, credentials, or secrets.

## Pull-request checklist

Before opening a pull request:

1. Run `python -m unittest -v tests.test_public_repo`.
2. Run `python tools/verify_public_repo.py .`.
3. Confirm new fixtures are synthetic or demonstrably sanitized.
4. Confirm documentation clearly distinguishes evidence, inference, and uncertainty.
5. Confirm no state-changing capability was introduced.
## Contribution licensing

By submitting a contribution, you represent that you have the right to submit it and agree that the contribution may be distributed as part of this project under the **PolyForm Shield License 1.0.0** and the repository's required notices. Do not submit material whose license is incompatible with those terms.

