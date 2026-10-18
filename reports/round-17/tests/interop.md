# R17-D28 — interop: d2/d3 `--check`, battery and craft stay green

- round: 17 (operator loop 2 of 3, build round 1 of 4) · shard: **D28** (tests ×4,
  claim D `culture-d4-assembly`) · owner: L2 worker, kotodama-shokunin lane
- assignment (verbatim): "D4 R17-D26..D29 (tests x4): determinism (two assemblies
  byte-identical); replay-frozen over D4 artifacts; interop (assemble-d2/d3
  --check + battery + craft green); gate findings == named hold set exactly.
  reports/round-17/tests/{determinism,replay,interop,holdset}.md."
- date: 2026-10-18. Baseline revision
  `f30b6f8188937632bbedd0e7b29aeefff6f8b07b`; working-tree HEAD `9b49a4a`.
- canon: NON-CANON engineering evidence. No clearance or canon claim is made.
- writes: **this file only** plus gitignored scratch under `.scratch/r17-tests/`.
  No tool, gate, example or earlier-round byte is edited. No commit, no push.
- **status: complete — all required legs green**, plus the D4 additions measured
  below.

## 1. Required legs (claim D: "d2/d3 paths untouched and green")

All commands run from the lane root, 2026-10-18, `TMPDIR=$PWD/.scratch`;
receipts captured under `.scratch/r17-tests/interop/`.

| command | exit | observed |
|---|---:|---|
| `python3 tools/assemble-d2.py --check` | 0 | `packet.d2.yml: byte-identical deterministic assembly` |
| `python3 tools/assemble-d2.py --selftest` | 0 | `selftest: 42/42 checks passed` |
| `python3 tools/assemble-culture-d3.py --check` | 0 | `packet.json: byte-identical…; packet.gates.yml: byte-identical deterministic assembly` |
| `python3 tools/assemble-culture-d3.py --selftest` | 0 | `selftest: 85/85 checks passed` (includes the real naming/costume gates run read-only over the fixture) |
| `python3 tools/assemble-d2-typed.py --check` | 0 | `examples/culture-d2/packet.d2.typed.yml: byte-identical deterministic typed packet` |
| `python3 tools/d2-typed-labels.py --check` | 0 | byte-identical deterministic projection (run in the same sweep; see §4 note) |
| `python3 tools/gates/typed-pipeline-gate.py` | 0 | `summary: 16/16 legs passed` (15 holds + 1 note, 0 fails) |
| `python3 tools/check-gate-battery.py` | 0 | `summary {pass: 7, fail: 0, unevaluable: 0, battery_exit: 0}`; `originals.preserved: true` (28 files hashed before/after, 0 modified/added/deleted) |
| `python3 tools/check-gate-battery.py --selftest` | 0 | `SELFTEST OK 29/29 controls behaved as expected` |
| `python3 tools/check-craft-exercise.py examples/supplement-opencode-1/sound-change-vs-taboo.json --counts` | 0 | `total 7`: `verdict_supported 5`, `verdict_unresolved 2`, `verdict_contradicted 0` |
| `python3 tools/check-craft-exercise.py --selftest …` | 0 | `SELFTEST OK 10/10 tamper cases detected` + `CLI-SELFTEST OK 18/18 cases passed` |

**Untouched, measured not assumed:** `git diff f30b6f8188937632bbedd0e7b29aeefff6f8b07b --
examples/culture-d2 examples/culture-d3 tools/assemble-d2.py tools/assemble-d2-typed.py
tools/d2-typed-labels.py tools/assemble-culture-d3.py tools/gates | wc -l` → **0
lines** (2026-10-18). The five legacy gates are byte-identical to the round-11
frozen pins (`reports/round-17/tests/replay.md` §3).

## 2. D4 additions measured in the same sweep

| command | exit | observed |
|---|---:|---|
| `python3 tools/assemble-culture-d4.py --check` | 0 | `packet.d4.yml: byte-identical deterministic assembly` |
| `python3 tools/assemble-culture-d4.py --selftest` | 0 | `selftest: 81/81 checks passed` |
| `python3 tools/gates/naming-collision-gate.py examples/culture-d4/packet.d4.yml` | 1 | 8 findings (6 `PHON-INVENTORY`, 1 `NAME-NEAR`, 1 `CROSS-HOLD`) |
| `python3 tools/gates/phonology-sanity-gate.py examples/culture-d4/packet.d4.yml` | 1 | 1 finding (`A-CLASS` REVIEW) |
| `python3 tools/gates/costume-era-consistency-gate.py examples/culture-d4/packet.d4.yml` | 0 | 0 findings |
| `python3 tools/gates/lexicon-coverage-audit.py examples/culture-d4/packet.d4.yml` | 0 | 0 findings |
| `python3 tools/gates/myth-consistency-gate.py examples/culture-d4/packet.d4.yml` | 0 | 0 findings |

Every D4 gate exit is in {0, 1}: no exit 2, no traceback — the interop leg the
round-17 counting contract measures (`reports/round-17/scope.md:111-113`).
This matches `examples/culture-d4/ASSEMBLY.md:32-38` row for row.

## 3. Interpretation

- The D2 typed pipeline (assembler → projector → adapter → gate) is green end to
  end on the frozen D2 example, and the D3 evidence-coupling example still
  regenerates byte-identically with its 85-check selftest green. The D4 build
  did not disturb either path, and the harness (battery, craft) is green with
  its own controls.
- A red gate row is not a defect to silence: the D4 naming gate's six
  `PHON-INVENTORY` lines are the legacy face of the six named holds
  (`reports/round-17/tests/holdset.md`), and its `CROSS-HOLD` line records that
  no real-language sweep was performed — never a clearance.

## 4. Limits (what this does not cover)

- **D4 typed interop is not evaluable.** The contract's typed-packet legs —
  strict-parse under the projector loader, `assembly` pin re-verification,
  `typed_channel` routing-row coverage — need a typed artifact, and none exists
  at this stamp (sweep 2026-10-18: `ls examples/culture-d4/` →
  `ASSEMBLY.md brief.md components packet.d4.yml README.md`; `ls tools/ | grep -i
  d4` → `assemble-culture-d4.py`). `reports/round-17/run-validation.py --check`
  (07:04 local, read-only) fails claim D on exactly those three artifacts.
  Blocking cause recorded in `reports/round-17/d4/typed-run.md` §0 and
  re-measured in `reports/round-17/tests/holdset.md` §4.
- `d2-typed-labels.py --check` is listed from the same sweep; its receipt is in
  `.scratch/r17-tests/interop/` alongside the others.
- Battery exit 0 means the seven gate selftests passed and the live tree was
  byte-preserved; it is not an endorsement of any gate's domain verdicts.

## 5. Reproduce

```sh
export TMPDIR=$PWD/.scratch
bash .scratch/r17-tests/interop-run.sh     # scratch harness used above; prints exit per leg
python3 reports/round-17/run-validation.py --check | python3 -c \
  "import json,sys; d=json.load(sys.stdin); print(d['claims']['D']['failures'])"
```
