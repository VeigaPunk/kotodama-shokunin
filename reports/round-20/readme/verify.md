# R20-C verify — independent re-measurement of the `corpus/README.md` reconciliation

- **seat:** R20-C04 (verify leg of R20-C01..C04). **lane:**
  `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
- **date:** 2026-10-18, local clock UTC−03:00; stamps **13:02:57Z** (first
  pass), **13:05:13Z** (close pass, after the `reconcile.md` §8 addendum), and
  **13:07:53Z** (final pass, after the revision block named its counting
  command — the binding one). **HEAD:** `122086b` plus the live round-20 working
  tree. **README sha256:** `fa1671218cb790f1ed22e0fa3a106004677a7b7bda559740f0e482a32b8db4fb`
  at 13:02:57Z, `a20b6b263f089364dbfa236afdca58f160954d03d2ef9822c9540ef8ef584f7b`
  at 13:05:13Z, `1a359d55387eef1aebd79316a7bf19d53a2ac6f0bcacb1cd109bdeff1294e7ce`
  at 13:07:53Z. V1–V7 below were re-run at the final stamp and read the same
  (sweep exit 0, 199/199, 0 mismatches; selftest 10/10; V3 10/10 + 10/0), and V8
  records the round runner's own C verdict.
- **canon:** NON-CANON engineering evidence; admits nothing, certifies no round.
- **what this file is:** the reconciliation's measurements re-run from a fresh
  process, plus before/after and negative controls. It is **same-seat**
  verification — a re-measurement with controls, not independent-seat review —
  and that limit is restated in §5 rather than hidden.

## V1 — the sweep re-run (fresh process)

```sh
export TMPDIR=$PWD/.scratch
python3 .scratch/r20-c-readme-sweep.py            # exit 0
# parts {'linguistics': 19, 'myth-symbol': 19, 'culture-material': 18,
#        'synthesis': 29, 'verification': 20, 'civilizations': 94} rows 199 files 199
# missing_from_index 0 []   topic_mismatch 0 []   orphan_rows 0 []   header_drift {}
python3 .scratch/r20-c-readme-sweep.py --json     # same result as JSON
python3 .scratch/r20-c-readme-sweep.py --selftest # exit 0, 10/10
```

## V2 — counts re-derived by a second, independent method

```sh
python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge
# totals.files 199; per-dir 94/18/19/19/29/20
for d in linguistics myth-symbol culture-material synthesis verification civilizations; do
  find corpus/knowledge/$d -maxdepth 1 -name '*.md' -type f | wc -l; done
# 19 19 18 29 20 94
```

Both agree with the numbers the README revision-1.5 line carries, and both
contradict the round-20 claim's declared `linguistics 20` (declared sum 200 vs
199 files) — the discrepancy the README records.

## V3 — before/after re-derivation of the ten repaired rows

The repair's own claim is falsifiable and was tested by reconstruction, not by
re-reading the receipt:

```sh
python3 .scratch/r20-c-verify.py   # exit 0
# V3a repaired rows byte-equal to topic: 10/10 equal, 0 defects
# V3b reconstructed-before mismatch count: 10
#     matches the ten recorded rows: True
# V3b current-tree mismatch count: 0
```

V3a checks each repaired row against the entry's live `- topic:` line
(byte-equal, exactly one occurrence). V3b rebuilds the pre-repair README text
from the recorded old rows (`.scratch/r20-c-rows.json`, captured before the
repair) and re-runs the sweep over it: exactly the ten recorded rows flag, and
the current text flags none. The repair therefore changed exactly what it
claims — no more, no fewer rows.

## V4 — controls (the sweep can fail)

`--selftest` plants, in memory only, one defect per leg and requires detection:
planted paraphrase → 1 mismatch; **truncated rewrite** (the round-19 defect
class) → 1 mismatch; ghost row → 1 orphan; deleted row → 1 missing file; wrong
header count → 1 drift; plus five live legs. **10/10, exit 0.** The first run of
this selftest returned 8/9 because the paraphrase control's expectation omitted
the `partition/` prefix the sweep reports — the control was wrong, the sweep was
right; fixed, and the truncated-rewrite control was added (see `reconcile.md`
§2).

## V5 — header counts and file counts agree, partition by partition

Six `## <partition>/ (N)` headers were parsed and compared with live counts:
`linguistics 19/19`, `myth-symbol 19/19`, `culture-material 18/18`,
`synthesis 29/29`, `verification 20/20`, `civilizations 94/94` — 0 drift.

## V6 — the known-gaps closures re-measured

| README statement | command | result |
|---|---|---|
| `tools/d2-typed-labels.py --selftest` 39/39 | `python3 tools/d2-typed-labels.py --selftest` | `39/39 checks passed`, exit 0 (13:02:57Z, after the O seat's concurrent edit to the file) |
| seventeen committed `expected.json` baselines | `find tools/gates/expected tools/gates/frozen reports/round-9/baselines -name expected.json \| wc -l` | 17 |
| battery registers nine gates, `pass 7 / fail 0 / unevaluable 0` | `python3 tools/check-gate-battery.py` | exit 0; `baselines_found 17`, `coverage 9/9`, `gates_uncovered []`, `pinned 17`, `unevaluable 0` |
| `d4-assembly-check-gate.py` ships no `--selftest` | `python3 tools/gates/d4-assembly-check-gate.py --selftest` | `assembly error: … '--selftest'`, exit 2 |
| round-7 acceptance recorded false | `reports/round-7/validation.json` | `acceptance_checks_passed: false` (F wrong rejection, preservation failure, chained round-6 acceptance) |

## V7 — blast radius

```sh
git status --short
#  M corpus/README.md        ← this seat
#  M reports/round-5/validation.json   M reports/round-7/validation.json
#  M reports/round-9/validation.json   M tools/d2-typed-labels.py   ← other seats
# ?? corpus/lessons/round-20.md  ?? reports/round-20/**             ← other seats
git diff --stat corpus/README.md
#  1 file changed, 85 insertions(+), 14 deletions(-)  (at the 13:07:53Z final stamp)
```

No `corpus/knowledge/` byte, no round-8..19 filed artifact, no gate and no
ledger was touched by this seat. The other modified paths are the concurrent
round-20 seats (§4 of `reconcile.md`).

## V8 — the round's own runner, C leg

The round's counting command landed from another seat ~13:06Z and was re-run in
its no-write mode:

```sh
python3 reports/round-20/run-validation.py --check     # prints, writes no receipt
# claim C: PASS; failures: []
# revision checks: commanded True, dated True, numbers_present True, placeholder False
# counts: civilizations 94, culture-material 18, linguistics 19, myth-symbol 19,
#         synthesis 29, verification 20
# declared linguistics 20 vs live 19 — documented_in_readme true
```

The same run reports D and O failing on their own in-flight artifacts (missing
v3 baselines, stale D4 pins, the foreign-tree mirror) — their seats' legs, not
C's. V8 is quoted as the round runner's verdict on C; it does not replace
V1–V7, which are this seat's own commands.

## Falsifiers (what would have shown this wrong)

- A remaining mismatch → sweep exit 1; observed pre-repair (`topic_mismatch 10`),
  and reproducible by V3b's reconstruction.
- A repair that over-reached (rows changed beyond the ten) → V3b would flag
  fewer than ten on the reconstructed text, or V1 would flag rows outside the
  ten.
- A green sweep that cannot fail → V4's planted defects would go undetected.
- Counts that do not survive a second method → V2 would disagree.

## Limits

- **Same-seat, same convention.** The verbatim-`- topic:` convention is the
  lane's round-10 convention; this file re-runs it rather than re-justifying it.
  An independent-seat reviewer that chooses a different convention would get a
  different (and defensible) reading; that reading is not in this file.
- **Correspondence only.** Nothing here certifies an entry's quality, sources,
  accuracy, or canon status; "verbatim" means the row equals the entry's own
  topic line.
- **Point-in-time.** Stamped 13:02:57Z on a tree that other seats were actively
  writing. Any later write to `corpus/knowledge/` or `corpus/README.md`
  invalidates V1–V5 until the sweep is re-run; the README sha256 above is the
  binding pin for this reading.
- The round's shared counting command `python3 reports/round-20/run-validation.py`
  did not exist at this stamp (measured 13:02:30Z); no verdict in this file is
  a round-runner verdict.
