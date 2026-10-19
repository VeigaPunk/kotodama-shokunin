# Ca01 — MANIFEST rounds[] fidelity to lane receipts (claim Ca, calibration)

Read-only audit. Reconciles `/home/vgpnk/Projects/shokunin/MANIFEST.json`
`rounds[]` against each lane `reports/round-<N>/validation.json` verdict.

The ledger uses two schemas: canonical `closure` rows (rounds 33-42) carry
`lanes:{kotodama:"ok"}` + `lane_rounds` + an `admitted` flag; r43/r44 carry the
newer per-lane schema (`verdict`/`admitted`/`close_commit`).

| round | lane receipt verdict | fleet row | fleet admitted | reconciles? |
|---|---|---|---|---|
| 33 | True | closure ok | True | YES |
| 34 | True | closure ok | True | YES |
| 35 | True | closure ok | True | YES |
| 36 | False | closure ok | False | YES |
| 37 | True | closure ok | True | YES |
| 38 | True | closure ok | True | YES |
| 39 | True | closure ok | True | YES |
| 40 | True | closure ok | True | YES |
| 41 | True | closure ok | True | YES |
| 42 | False | closure ok | False | YES |
| 43 | rejected-honest-stop | per-lane | False | YES (verdict match) |
| 44 | rejected-honest-stop | per-lane | False | YES (verdict match) |

Admitted count reconciles: lane receipts show 8 True / 2 False / 2
rejected-honest-stop; the ledger's `admitted` flags agree row-for-row.

**Schema note (not a discrepancy):** rounds 33-42 are present as fleet-level
`closure` rows, not the per-lane schema used at 43-44. The `lane: "kotodama"`
field is absent on closure rows (the lane is named inside `lanes`/`lane_rounds`),
so a naive `lane=='kotodama'` filter undercounts — that is a schema-evolution
observation, not missing rows. No verdict disagreement found.

Verdict: claim Ca verified — all 12 loop-1 rows reconcile; zero unexplained
discrepancies; the two ledger schemas noted.
