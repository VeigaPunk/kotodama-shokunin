# R12-O12 disposition — R8 filed-receipt rewrite

- Audit date: 2026-10-17.
- Sweep source: `reports/round-12/defects/sweep-r8.md`, receipt-integrity finding.

## Disposition

**Not fixed; route to round-14 integration.** The finding is that the filed round-8 validation receipt no longer preserves its close-time snapshot after a later validator run. Restoring or regenerating that file would rewrite filed history, not make a bounded typo/pointer correction. The round-8 sweep independently compared the work-commit and current JSON and identified the later write path; its commands and date are recorded in the sweep.

No before/after patch control applies because no change was made. The round-12 router should include this finding in `reports/round-12/defects/routed.md`, with the round-14 integrator as owner and a read-only correction record as the permissible remedy.
