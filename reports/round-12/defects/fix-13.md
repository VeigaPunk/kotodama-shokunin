# R12-O13 disposition — R9 baseline layout gap

- Audit date: 2026-10-17.
- Sweep source: `reports/round-12/defects/sweep-r9.md`, finding O-R9-01.

## Disposition

**Not fixed; route to round-14 integration.** Two round-9 baselines are outside the frozen-run standard's declared path, and the default battery therefore does not cover all gates; a custom-root run does. Relocating filed baselines or changing the standard/claim interpretation is an integration decision, not a typo/pointer correction. The sweep's read-only default-root and custom-root controls, outputs, and date are recorded in the source fragment.

No before/after patch control applies because no change was made. The round-12 router should route the standard-path exception to the round-14 integrator and preserve the filed round-9 baseline bytes.
