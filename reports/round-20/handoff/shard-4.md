# shard-4 — the twelve D4 rows, census and the alias evidence state (R20-D05..D12)

- topic: the twelve D4 claim rows enter the v3 ledger from
  `reports/round-20/handoff/claims-map.md` (the packet seat's copy surface),
  with the design's census and the D4-CL08 evidence-keyed status.
- date: 2026-10-18.

## 1. Mechanism

- `v3_parse_claims_map` extracts the twelve `### D4-CLnn — kind —
  evidence_status — \`status\`` sections: statement, `u.basis` (clause
  grammar), and the backticked link specs — all carried into the ledger
  unchanged.
- The parser fails closed on shape drift: not twelve rows, or a row without
  statement/basis/links, is `E2E-ARTIFACT`.
- The `D4-CL08` guard (design §4 rule 2 / control **m11**): if the row is
  typed `supported`, its basis must carry the run witness
  (`era_reconciliation` + `12/12`); a missing witness is `E2E-UNC`.

## 2. Measured

```sh
export TMPDIR=$PWD/.scratch
python3 tools/exercise-handoff-e2e.py --profile v3 --quiet
# -> … claims=27 statuses=16/7/4 v2_subset=equal alias_leg=landed …
```

- Census: **27 claims — 16 supported / 7 partial / 4 unresolved** (v2's
  8/5/2 + D4's 8/2/2). The landed branch is measured, not assumed: the D4
  legs are re-run every time (shard-2 §3) and the alias state is frozen in
  the baseline (`alias_state: "landed"`).
- Unresolved rows and their routing: `D2-CL02` (OQ-V2-03),
  `CL13` (OQ-V2-01), `D4-CL09` (OQ-V3-05), `D4-CL12` (OQ-V3-06) —
  `packet_uncertainty.py --require-oq` exits 0 with zero findings.
- D4 status histogram: supported `D4-CL01/02/03/05/06/07/08/11`, partial
  `D4-CL04/10`, unresolved `D4-CL09/12`.

## 3. Controls (selftest, all measured)

- m1 dropped D4 row → `E2E-COUNT`; m2 status `tentative` → `E2E-UNC`;
  m3 duplicated basis → `E2E-UNC`; m4 partial without `restriction:` →
  `E2E-UNC`; m5 unresolved without `owner:` → `E2E-UNC`; m11 supported
  D4-CL08 without the run witness → `E2E-UNC`; m2b the same off-vocabulary
  status in the twin → `U-STATUS-VOCAB` from the harness itself.

## 4. If the O bytes are reverted

- The flip is symmetric by construction: the witness legs go red, the
  assembly refuses to emit the `supported` form (`E2E-UNC`, naming the red
  legs), and the baseline's `alias_state` mismatch forces a re-freeze as a
  **new row** with the reason recorded — never a silent edit. The pre-flip
  row text is retained in `claims-map.md`'s flip record.
