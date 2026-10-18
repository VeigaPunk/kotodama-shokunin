# R28-C51 — reviewer of `C41.md` (the instrument and the counts)

- **seat:** R28-C51 (C-ceiling, reviewer 1 of 6). **lane:**
  `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
- **date:** 2026-10-18. **lane HEAD** `69cecbc`.
- **canon:** NON-CANON engineering review. Author-side evidence; admits nothing,
  certifies no round, is not independent promotion verification.
- **writes:** this file only. No corpus, tool, packet or pin byte touched.
  Scratch `.scratch/`, `TMPDIR=$PWD/.scratch`.
- **reviews:** `reports/round-28/ceiling/C41.md` and
  `reports/round-28/ceiling/measure-ceiling.py` (sha256 `ff1a7f24…`).

## 0. Verdict

**PASS, with one defect found and fixed in the fragment, and one reading I
confirmed rather than took on trust.**

| check | verdict |
|---|---|
| the instrument's counts re-derive from a fresh process | pass |
| the filed 18/9 is genuinely the pre-fix reader's reading | pass — reproduced |
| the delta is exactly one row (`L-45`) | pass |
| the mechanism biconditional holds 27/27 | pass |
| `C41.md` §3's claim about the filed class table | **defect D-1** (fixed by the author) |
| the pre-fix reader is labelled as a reconstruction | pass |

## 1. The counts, re-derived by this seat

```sh
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
python3 -B reports/round-28/ceiling/measure-ceiling.py --selftest
# selftest: 10/10 checks passed                                        exit 0
python3 -B reports/round-28/ceiling/measure-ceiling.py
# population: mark-axis plain words = 27
# delivered gate (b5406bcd)  legal=19 illegal=8
#   illegal: L-08, L-15, L-17, L-24, L-26, L-30, L-44, L-51
# filed round 27:      legal=18 illegal=9  (pre-fix reader)
# pre-fix gate (5b5abe78) legal=18 illegal=9
#   delta vs delivered: {'L-45'}
# mechanism: ... -> True (27/27)
sha256sum examples/culture-d4/packet.d4.yml tools/gates/argot-derivation-gate.py
# 543d68a8…  b5406bcd…
```

Every figure in `C41.md` §0/§1/§2 matches. The packet and gate digests the
fragment quotes are the live ones.

## 2. The pre-fix reader, tested independently

The fragment claims the pre-fix gate declares no legality predicate. Verified:

```sh
python3 -B - <<'PY'
import runpy
g = runpy.run_path('.scratch/r27-d13/oldg/tools/gates/argot-derivation-gate.py')
print('is_legal_syllable' in g)          # False
print(g['syllabify']('semkit'))          # ['se', 'mki', 't']
PY
# False
# ['se', 'mki', 't']
```

and with the delivered gate, `syllabify('semkit')` → `['sem', 'kit']`. So the
`L-45` delta is real and it is a **syllabification** difference, not a legality
difference — exactly as `C41.md` §2 states. (The pre-fix scan's own split is
`['se', 'mki', 't']`, which `C41.md` now quotes exactly.) **The fragment's
labelling of the 18/9 as a reconstruction is correct and necessary**: the 18/9
cannot be obtained by calling the pre-fix file,
so calling it "the pre-fix gate's reading" without the caveat would be an
overstatement. The fragment does not overstate it.

## 3. Defect D-1 — a wrong claim about the filed class table (fixed)

`C41.md` §3 (first version) asserted: *"The filed table's `material 8 legal / 2
illegal` is not reproducible under either reader as a class count."* That is
**false**, and this seat caught it before the fragment propagated.

Round 27's table used **three** classes (`material`, `abstract`, `other`); the
instrument uses **two**. Summed, round 27's non-abstract classes are
`8+10 = 18 legal` and `2+2 = 4 illegal` — which is **exactly** the instrument's
`material/other` row (18 legal, 4 illegal). Verified:

```sh
python3 -B - <<'PY'
filed = {'material': (8,2), 'abstract': (0,5), 'other': (10,2)}
print('material+other:', (filed['material'][0]+filed['other'][0],
                          filed['material'][1]+filed['other'][1]))   # (18, 4)
PY
# material+other: (18, 4)
```

**Disposition: fixed by the author** — `C41.md` §3 now states the reconciliation
as exact and confines the divergence to the abstract class and to `L-45`. The
corrected claim is stronger than the wrong one: it says the pre-fix reader was
wrong about **one compound** and right about the other 26 words.

## 4. What this review did not do

Did not edit the instrument or the entry deliverables beyond the one fix it asked
for; did not re-measure anything outside the ceiling's population; did not
adjudicate whether the ceiling should be repaired.

## 5. Replay

```sh
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
python3 -B reports/round-28/ceiling/measure-ceiling.py --selftest
python3 -B reports/round-28/ceiling/measure-ceiling.py
python3 -B - <<'PY'
import runpy
g = runpy.run_path('.scratch/r27-d13/oldg/tools/gates/argot-derivation-gate.py')
print('is_legal_syllable' in g, g['syllabify']('semkit'))
PY
```
