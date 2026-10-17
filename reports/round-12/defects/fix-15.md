# R12-O15 disposition — R10 stale-fixed ledger conflict

- Audit date: 2026-10-17.
- Sweep source: `reports/round-12/defects/sweep-r10.md`, finding F-03.

## Disposition

**Not fixed; route to round-14 integration.** The filed drift ledger retains `stale-fixed` claims for a round-8 runner that is reverted in the current tree, while another row and the LOG describe the final state differently. Resolving this requires reconciling historical row dispositions against retained evidence; rewriting the filed ledger or runner is prohibited, and this is larger than a bounded pointer correction.

The sweep's current-hash, retained-runner, and ledger cross-checks are the evidence; commands and date are recorded there. No before/after patch control applies because no change was made. Route ledger reconciliation to the round-14 integrator.
