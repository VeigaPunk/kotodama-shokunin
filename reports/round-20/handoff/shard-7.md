# shard-7 — selftest control matrices (R20-D05..D12)

- topic: the two control matrices that prove the v1 and v3 paths fail closed:
  v1's preserved 17 controls and v3's 28 controls (gate, preflight,
  uncertainty, links, alias guard, tamper).
- date: 2026-10-18.

## 1. Commands and observed lines

```sh
export TMPDIR=$PWD/.scratch
python3 tools/exercise-handoff-e2e.py --selftest
# -> selftest: OK — positive run (exit 0, fields=16/16, glossary-entries=20, findings=0) plus 17 controls

python3 tools/exercise-handoff-e2e.py --profile v3 --selftest
# -> selftest: OK — positive run (exit 0, fields=16/16, glossary-entries=20, findings=0,
#    links=105/105, claims=27, statuses=16/7/4, v2_subset=equal, alias_leg=landed) plus 28 controls
```

Every control runs against a fresh fixture copy under `TMPDIR`; the live tree
is never mutated (preservation control re-measures all read-set files before
and after a run).

## 2. v3 controls (each mutation → its stable code)

- gate family: dropped `request_ref` row → `HO-MISSING`; blank scope →
  `HO-EMPTY`; floating version → `HO-DEP-FLOAT`; canon marker removed →
  `HO-CANON-MARKER`; producer canon claim → `HO-CANON-CLAIM`; unlicensed
  etymology → `HO-GLOSS-ETYM`; hyphenated heading → `HO-MISSING`; renamed
  heading → `HO-MISSING`; no heading → exit 2 `HO-DATA`; canon-verb trap in a
  basis cell → `HO-CANON-CLAIM` (m10).
- uncertainty family: m1 dropped D4 row → `E2E-COUNT`; m2 `tentative` →
  `E2E-UNC`; m3 duplicated basis → `E2E-UNC`; m4 partial without
  `restriction:` → `E2E-UNC`; m5 unresolved without `owner:` → `E2E-UNC`;
  m11 supported D4-CL08 without the run witness → `E2E-UNC`; m2b the same
  off-vocabulary status in the twin → the harness's own `U-STATUS-VOCAB`.
- link family: m6 dangling selector in the twin → harness exit 1
  `L-TOKEN-MISSING`; m7 link outside the read set → `E2E-LINK`.
- scan family: m9 extra glossary row → `E2E-SCAN`.
- tamper family: m12a edited baseline → exit 2 `E2E-BASELINE` (integrity
  digest mismatch); m12b drifted D4 projection → exit 1 `E2E-DIGEST` naming
  the file; m8 re-typed v2 row → exit 1 `E2E-DIGEST`; re-signed scan
  expectation → exit 2 `E2E-BASELINE`; missing D4 artifact → exit 2
  `E2E-ARTIFACT`.
- hazard/preservation: no emitted heading carries a field-name token; the
  58 read-set files are byte-identical before and after a run.

## 3. v1 controls (preserved)

- The round-11 matrix is carried verbatim: positive, isolation, malformed-01
  … malformed-10, the dropped-glossary preflight control, the heading-hazard
  probe, preservation, and the four tamper controls — 17 controls, all
  green on a fresh fixture.
- The v1 matrix is deliberately unchanged; its live-tree drift is the O
  seat's round-20 input change (shard-8), not a control regression.
