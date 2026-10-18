# R28-C55 — reviewer of `C45.md` (decision record and calibration)

- **seat:** R28-C55 (C-ceiling, reviewer 5 of 6). **lane:**
  `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
- **date:** 2026-10-18. **lane HEAD** `69cecbc`.
- **canon:** NON-CANON engineering review. Author-side evidence; admits nothing,
  certifies no round, is not independent promotion verification.
- **writes:** this file only. No corpus byte touched. Scratch `.scratch/`,
  `TMPDIR=$PWD/.scratch`.
- **reviews:** `reports/round-28/ceiling/C45.md` against the entry's §8 decision
  record and §9 calibration shelf.

## 0. Verdict

**PASS. No defect. The seven rows are present, three of them rest on this round's
measurement as the fragment claims, and the two calibration labels the fragment
says it checked hardest are correctly labelled in the entry.**

| check | verdict |
|---|---|
| the record has seven rows, `RLC-1..7` | pass |
| three rows rest on this round's measurement | pass (`RLC-1`, `RLC-2`, `RLC-4`) |
| `RLC-4` is the entry's own correction | pass |
| the verlan label separates data from account | pass |
| the Aronoff/ceiling separation is stated | pass |
| the record makes no canon claim | pass |

## 1. The record, re-derived

```sh
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
grep -c 'RLC-' corpus/knowledge/linguistics/register-lexicon-ceilings.md   # 12
grep -n 'RLC-[1-7]' corpus/knowledge/linguistics/register-lexicon-ceilings.md
```

Seven distinct IDs, each a table row with evidence, consequence and recheck
columns — the shape the lane's entries use and which the round-28 runner's
`DECISION_RECORD_RE` recognises. `C45.md` §1's claim that **three of seven** rows
rest on this round's measurement is accurate: `RLC-1` cites `19/8` and `4 of 5`,
`RLC-2` cites the `27/27` biconditional, and `RLC-4` cites the filed-vs-delivered
divergence. The other four rest on cited framework (`RLC-3`, `RLC-7`) or on the
design's recorded decision (`RLC-5`, `RLC-6`).

## 2. `RLC-4`, the entry's own receipt, checked

`C45.md` §2 argues that `RLC-4` is the only row whose evidence is the entry's own
correction, and that the round-27 citation it supersedes is still stable. Both
halves verified:

```sh
grep -n 'RSA-4' reports/round-27/entry/C45.md
# 27:| `RSA-4` | ... | **measured** (`0 legal / 5 illegal` over institutional abstractions) |
python3 -B reports/round-28/ceiling/measure-ceiling.py | grep -E 'delivered|filed'
# delivered gate (b5406bcd)  legal=19 illegal=8
# filed round 27:      legal=18 illegal=9  (pre-fix reader)
```

So the round-27 file still reads `0 legal / 5 illegal` (stable, because the
amendment is append-only) while the delivered count is `1 legal / 4 illegal` and
`19/8` (stale, because the reader moved). `RLC-4` is the row that makes the
distinction a rule, and the fragment states it correctly.

## 3. The two calibration labels the fragment says it checked hardest

**Verlan — data vs account.** The entry's sources block labels the *analysis*
(LOOP+MIRROR) as one OT account among several and names the competitors (Plénat
1995; Weinberger & Lefkowitz 1992), while the *attested orders* are presented as
data. `C45.md` §3 claims this separation is made. Verified by reading the entry's
Gotowski bullet: it says "the analysis is one account of the constraint
(competing prosodic-template and CV-skeleton accounts exist …)" and "the paper
itself says written records of an informal game are not exhaustive". **Correct.**

**Aronoff — blocking vs the ceiling.** The entry's §2 table separates an
**operation ceiling** from **blocking** (Aronoff 1976) from a **lexical accident**
(Bauer 1983), and `RLC-3` makes the separation a rule. `C45.md` §3 says
conflating them would produce the wrong remedy. Verified: the entry's §2 states
"the remedies are incompatible" and `RLC-3`'s consequence column reads "coining
words to fix a phonological ceiling, or editing the gate until they pass".
**Correct.**

## 4. One thing this review checked that the fragment did not claim

The entry's §9 says the four-of-five ratio is "this drill's ratio", not a typical
one. Checked that the entry does not elsewhere imply generality:

```sh
grep -n 'four of five\|4 of 5\|typical\|generally' \
  corpus/knowledge/linguistics/register-lexicon-ceilings.md
```

Every hit is either the drill-specific measurement or an explicit disclaimer
("no claim that four-of-five is a typical ratio — it is this drill's ratio"). The
entry does not overreach. **No defect.**

## 5. What this review did not do

Did not edit the entry; did not re-derive the calibration status of every source
(Dixon/Halliday were checked in `review-C42.md` §4); did not certify claim C.

## 6. Replay

```sh
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
grep -n 'RLC-[1-7]' corpus/knowledge/linguistics/register-lexicon-ceilings.md
grep -n 'RSA-4' reports/round-27/entry/C45.md
python3 -B reports/round-28/ceiling/measure-ceiling.py | grep -E 'delivered|filed'
```
