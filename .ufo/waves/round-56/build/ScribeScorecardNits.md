# Round 56 — SCORECARD round-55 record nits (routed defect 2)

Seat: ScribeScorecardNits. Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`. Read-only over the
lane; measured against the round-55 tip `2935c47011049527842b6d3f08691d9629c3b983` (lane `main` is now at
round-56 `456f5ad`, so every revision below is named). No lane file was edited; this report is the only
write, plus scratch under `/fast/scratch/hyaku/kotodama-r56/ScribeScorecardNits/`.

Result: both defects in routed defect 2 are confirmed. Correction rows are drafted at the end in the
SCORECARD axes-row shape, for append only. Calibration census: 12 SCORECARD cells name a number or a commit
(10 in the round-55 axes table, 2 in the capability row), plus 12 tokens in the section preamble; 3 cells
mismatch the repository, 9 cells and all 12 prose tokens match.

## Finding (a) — mistake count

- `SCORECARD.md:1070` (round-55 calibration row) reads: `mistakes R55-M1 to R55-M4`.
- `corpus/lessons/round-55.md:227-232` carries six rows, `R55-M1` through `R55-M6`. M5 is the separability
  export declared as S285-S999, which made the selftest fixture S900 read as a dependency; M6 is record text
  whose commit messages transpose the C and O control counts and name a fix that landed in `81178c8`.
- Re-run command and output (from the lane root, read-only):

```
$ grep -c '^| R55-M' corpus/lessons/round-55.md
6
$ grep -o '^| R55-M[0-9]' corpus/lessons/round-55.md | tr '\n' ' '
| R55-M1 | R55-M2 | R55-M3 | R55-M4 | R55-M5 | R55-M6
```

## Finding (b) — selftest count and its revision

- `SCORECARD.md:55` (capability row `gate-line shape checker`) reads `--selftest (24/24)` and names no
  revision for that count. `SCORECARD.md:1069` (round-55 operability row) also reads `selftest 24/24`; its
  evidence cell names `454a2dc` for the tool, but not for this number, and the row presents the eight-leg
  PASS set as the landed result.
- Measured lineage of the checker: 12/12 at `f4015e7` (claim base), 24/24 at `454a2dc` (O lands), 27/27 at
  `173cab6` (the only later commit that touches the checker) and 27/27 at the round-55 tip `2935c47`.
  `git rev-parse 173cab6:tools/check-gate-quotes.py 2935c47:tools/check-gate-quotes.py` returns the same blob
  `a3bca98d52e94b585bda6394f63215ebff142862` for both.
- So 24/24 is true only at `454a2dc`; a reader of the tip takes a stale number. Re-run commands and output:

```
$ git show 454a2dc:tools/check-gate-quotes.py > /tmp/t-454a2dc.py && python3 -B /tmp/t-454a2dc.py --selftest | tail -1; echo exit=$?
SELFTEST: 24/24 pass
exit=0
$ git show 2935c47:tools/check-gate-quotes.py > /tmp/t-2935c47.py && python3 -B /tmp/t-2935c47.py --selftest | tail -1; echo exit=$?
SELFTEST: 27/27 pass
exit=0
$ git show f4015e7:tools/check-gate-quotes.py > /tmp/t-f4015e7.py && python3 -B /tmp/t-f4015e7.py --selftest | tail -1; echo exit=$?
SELFTEST: 12/12 pass
exit=0
$ git show 173cab6:tools/check-gate-quotes.py > /tmp/t-173cab6.py && python3 -B /tmp/t-173cab6.py --selftest | tail -1; echo exit=$?
SELFTEST: 27/27 pass
exit=0
```

- The exit pair in both rows re-runs as filed. Ran from extracted trees (`git archive <rev>` into scratch,
  then `python3 -B reports/round-55/accept-o.py`): exit 1 at `f4015e7`, exit 0 at `454a2dc`, exit 0 at
  `2935c47`. The tip run reports `DOUBLED PASS count=13`, `TRUNC PASS count=17`, `SELFTEST: 27/27 pass`.

## Drafted correction rows (append only; do not edit lines 55, 1069 or 1070)

Placement: append after the round-55 axes table ends (after `SCORECARD.md:1071`) and before the Frontier
step paragraph, or in a clearly labelled corrections block below the round-55 section.

| axis | verdict | before → after / observation | re-run command | measured evidence |
|---|---|---|---|---|
| calibration (correction, appended round 56) | recorded | the round-55 calibration row says `mistakes R55-M1 to R55-M4`; the lesson carries six, `R55-M5` (C's separability export declared as S285-S999, so the selftest fixture S900 read as a dependency) and `R55-M6` (declaration and routed-fix commit messages transpose the C/O control counts and name a fix that landed in `81178c8`). The round-55 row stands as filed | `grep -c '^| R55-M' corpus/lessons/round-55.md` | 6; ids `R55-M1` to `R55-M6` at `corpus/lessons/round-55.md:227-232` |
| operability (correction, appended round 56) | recorded | the capability row and the round-55 operability row cite `--selftest` 24/24 without naming the revision that measures it; 24/24 is the count at `454a2dc`, while the later checker commit `173cab6` and the round-55 tip `2935c47` measure 27/27. The exit pair re-runs as filed: accept-o exit 1 at `f4015e7`, exit 0 at `454a2dc` | `git show 454a2dc:tools/check-gate-quotes.py > /tmp/t.py && python3 -B /tmp/t.py --selftest`; the same with `2935c47` | `SELFTEST: 24/24 pass` (exit 0) at `454a2dc`; `SELFTEST: 27/27 pass` (exit 0) at `2935c47`; accept-o exit 1 at `f4015e7`, exit 0 at `454a2dc` |

## Calibration census — one command

Script (scratch, read-only over the lane):
`/fast/scratch/hyaku/kotodama-r56/ScribeScorecardNits/scorecard-r55-census.py`
Run: `python3 -B scorecard-r55-census.py`
Full output: `/fast/scratch/hyaku/kotodama-r56/ScribeScorecardNits/census-out.txt`

```
CENSUS cells-naming-number-or-commit=12 (round-55 axes table 10, capability row 2); preamble prose tokens=12
...
TOTAL checks=30 pass=30 fail=0
CALIBRATION cells=12 matched=9 mismatched=3 (prose tokens=12, all matched)
MISMATCH SCORECARD.md:1070 col2 says 'mistakes R55-M1 to R55-M4'; lesson has R55-M1..R55-M6
MISMATCH SCORECARD.md:1069 col2 says 'selftest 24/24'; round-55 tip measures 27/27 and 24/24 is 454a2dc's count
MISMATCH SCORECARD.md:55 col2 says '--selftest (24/24)' with no revision; round-55 tip measures 27/27
```

What the 30 checks establish (all pass; values measured at `2935c47` unless a revision is named):

- All ten commits named in the round-55 section exist and are ancestors of `2935c47`: `d44309a`, `f4015e7`,
  `8eda954`, `b9c44a2`, `81178c8`, `d52c9df`, `454a2dc`, `eb0a331`, `173cab6`, `2935c47`.
- `454a2dc` touches only `tools/check-gate-quotes.py`; `eb0a331` adds the entry, 73 SOURCES rows and the
  README row; `2935c47` changes only `SCORECARD.md` and `SHONEN.md`.
- knowledge files 230 → 231 and myth-symbol 26 → 27 at the named revisions; SOURCES rows 284 → 358;
  status totals 240/34/10 → 313/34/10 → 313/35/10.
- The entry cites 73 unique S-ids, lowest S285, each with exactly one registry row, `mined`, with the entry
  in `used-by`; entry length 186 lines at `eb0a331`, 188 at the tip.
- Checker selftest 12/12 at `f4015e7`, 24/24 at `454a2dc`, 27/27 at `173cab6` and `2935c47`; accept-o exit 1
  at `f4015e7` and exit 0 at `454a2dc` and at the tip.
- accept-o at the tip: eight legs PASS, DOUBLED count 13, TRUNC count 17, SELFTEST 27/27, exit 0.
- accept-c at the tip: seven legs PASS (SET 231, SWEEP 231/231, FLOOR cited 73, RANGE, STATUS, USEDBY,
  ACCESS), exit 0.
- Build wave 51 seats and falsify wave 33 seats, matching `.ufo/waves/round-55/{build,falsify}-dispatch.json`.
- `S358` is tier B and its `teaches` opens `supersedes S256`; `S256` remains tier A and `mined`.
- The three routed line fixes land at the stated lines: `b9c44a2` hunk at line 68, `81178c8` at line 79,
  `d52c9df` at line 72.
- The round-11 L0 question named in the freshness cell exists as a ledger row: `kotodama | round-11 |`
  in `/home/vgpnk/Projects/shokunin/.ufo/l0-questions.md`.
- Control receipts read at the tip: `criterion11-controls.txt` ends `CONTROLS 14/14 as expected`;
  `criterion11-controls-o.txt` ends `CONTROLS 16/16 as expected`.

## Touched surfaces

None in the lane. No SCORECARD, lesson, tool, corpus or registry edit; no git or jj write; no commit, push,
add, stash, checkout or ref update. Scratch only: the census script, per-revision checker copies `t-<rev>.py`,
extracted trees `tree-{f4015e7,454a2dc,2935c47}`, accept-o logs, and `census-out.txt`, all under
`/fast/scratch/hyaku/kotodama-r56/ScribeScorecardNits/`. No tool installs.

## Unrun checks and limits

- The criterion-11 control builders were not re-executed; their receipt tails were read at the tip, so
  14/14 and 16/16 are receipt-verified, not re-derived here.
- The pre-landing DOUBLED/TRUNC zero sets were not re-derived; the pre-landing result I reproduced is the
  accept-o exit code (1 at `f4015e7`, 0 at `454a2dc`).
- The coverage row's `0 filename owners at base` gap was not re-measured at the base revision; the tip
  accept-c SET leg was re-run instead.
- The round-11 L0 row was verified to exist, not read for a ruling.
- The 24/24 numbers are true at `454a2dc`; the finding is that neither row pins that revision, so at the
  round-55 tip they read stale. The correction rows say this at that strength.
