# MutCaCounterProbe — Round 75, W2

## Mutation probe result

The pristine `accept-ca.py --selftest` was run against a snapshot copied to scratch. It exited 1, so the required detector baseline is inconclusive and mutation verdicts cannot be established. No mutants were applied.

Observed baseline failures:
- Clean fixture: exit 1; `RECEIPTS=FAIL`, expected PASS; stdout did not contain expected `ACCEPT-CA-75: PASS legs=12/12`.
- `annotate-other-token`: `NOSTUB=FAIL`, expected PASS.
- `r1-rule2-exempt`: exit 1; `RECEIPTS=FAIL`, expected PASS.
- `repair-no-statement`: `LEDGER=PASS`, expected FAIL.

Mutant table: not run (baseline inconclusive).

Snapshot counter SHA-256: `d167093537864fc9572fedec2ee8cd0f8e1f86c7c6daa380e81bfde893975bdb`.
Restore evidence: scratch snapshot was not mutated; original lane counter was not written. Scratch directory was removed on shell exit.

Report: .ufo/waves/round-75/w2/MutCaCounterProbe.md
