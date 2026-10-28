# MutCentryIDs — wave-2 falsifier, round 77 (REPOINTED entry-source-ID probe)

Seat: `MutCentryIDs` (leaf, attack-only). Date: 2026-10-27. Lane:
`/home/vgpnk/Projects/shokunin/kotodama-shokunin`. Base:
`211f9526800906e0c585d878d265c37e5e090c15` (untouched; no lane file other than
this report and `w2/stage/MutCentryIDs/**` was written).

## Named W1 item attacked

W1 `w1/ExecAdaptC.md`, finding 3: *"REPOINTED carries the rewrite clause: one id
per `source:` line, the line's URL must be that row's document, every inline id
must resolve, and the draft's legacy ids (config `removed_ids`) must be gone.
This is the only guard against a landed entry that keeps
S886/S888/S889/S890/S891/S896."* The counter's own selftest proves this on
synthetic fixture bytes (`repointed-legacy-id`, `repointed-source-no-url`); this
probe re-runs the leg on the **real entry bytes**.

Invariant under test: the ACCEPT-C-77 REPOINTED leg fails an admitted entry that
retains staged `S903` and a legacy id, and passes the rewritten S897/S898
candidate.

## Detector (same bounded behavioral detector on every run)

`python3 -B .ufo/waves/round-77/w1/stage/ExecAdaptC/accept-c.py` (W1 build;
sha256 `5ac63e0d6630e8711aca7cceb159ee2b13c94b5a1bec4997afbdb3806826dca4`,
3,303 lines — byte-identical to the sha recorded in `w1/ExecAdaptC.md`), run as
a real subprocess against a purpose-built fixture git repo per case, exactly as
the counter's own selftest harness builds them (`_st_build` reused verbatim;
every fixture commit made with `git -C <fixture>`, toplevel asserted). Scratch:
`/fast/scratch/hyaku/kotodama-r77/MutCentryIDs` (deleted after the runs; raw
outputs preserved in `w2/stage/MutCentryIDs/`).

Real inputs used by every case: the W1 clean candidate entry bytes
(`w1/drafts/corpus/knowledge/linguistics/naming-systems.amend-2026-10-23.md`,
sha256 `4e513f4861137980f6f1aafb880f38782bce46fcf77eb708288c3afba01afb1e`,
git blob `5144cb1884bd8ed0762246c55f73b459bc1df954`), the real staged universe
(`.ufo/waves/round-77/assimilation/staged-ids`, 132 ids, contains S897 and
S903), the draft's six removed ids `S886,S888,S889,S890,S891,S896`, real
row_set documents (lishisuo.cssn.cn S897←S897; onomastica.ijppan.pl S898←S903),
real Gate quotes (`名的使用要早于姓`, `there were altogether 88 terms`). Fixture
scaffolding (same in all four runs): base registry rows S001–S003, evidence
window bodies, lesson shell, census stub, README topic string — none of it
reads or writes the lane. Frozen config identical across all four runs:
claims.json sha256 `50c9d3cbb038dc9fe5a7c0752d64570fdc379f7d357ea06851fb9ca236d754f6`,
map sha256 `da5d1ee1a7988c729fdc5cb2064abe026f1fb38d16e15736e13af2a2a74ce870`.

## Cases (exact mutations; driver: `w2/stage/MutCentryIDs/driver.py`)

- **pristine** — the W1 clean candidate verbatim. Expected: REPOINTED PASS.
- **mut1 (the assigned draft mutant)** — pristine bytes with exactly three
  counted substitutions: (a) `source:` line `- source: S898 — Kałużyńska` →
  `- source: S903 — Kałużyńska` (staged id retained, URL kept); (b) one legacy
  source line retained verbatim beneath it: `- source: S886 —
  https://kotobank.jp/word/苗字-392782 — 「世界大百科事典(旧版)」所収 苗字 項 —
  fetched 2026-10-23`; (c) one inline `(S898)` → `(S903)` in the 88-term
  sentence. sha256 `d5c3bf5e0e29469c2d30095bb8013addadc6127b2293f3fcaa975fbb6897e952`.
  Expected: REPOINTED FAIL.
- **mut2 (pre-rewrite draft, corroboration)** —
  `w1/stage/RevQualityFit-2/naming-systems.amend-2026-10-23.md` verbatim
  (S897+S903 source lines plus all six legacy ids). sha256
  `43b3551815e9916c41ef10623335c6e3183f4533a7eb79ae2cf5b649ee547b78`.
  Expected: REPOINTED FAIL.
- **restored** — mut1's fixture with the pristine bytes written back and
  re-committed. Expected: REPOINTED PASS, byte-identical entry.

## Actual outputs (full stdout per run in `w2/stage/MutCentryIDs/<case>.stdout.txt`)

Commands (all exit 1 — the counter exits 1 when any leg fails; per-leg verdicts
are the datapoints):

```
$ python3 -B …/w1/stage/ExecAdaptC/accept-c.py --root <scratch>/case-pristine/lane --lands 8124c70f919d97b2f88ad46dc6d0960a01cf699b --freeze fbcda5cfc90fa3d324638c8c713443f9d298ad6a --fleet-root <scratch>/case-pristine/fleet --work <scratch>/work
$ python3 -B …/accept-c.py --root <scratch>/case-mut1/lane --lands ae37cbcb69a2b61eb5909697b2c3d6782040a397 --freeze fbcda5cfc90fa3d324638c8c713443f9d298ad6a --fleet-root <scratch>/case-mut1/fleet --work <scratch>/work
$ python3 -B …/accept-c.py --root <scratch>/case-mut1/lane --lands d72b61ac49d8940a653053bfbb673ca4956be36b --freeze fbcda5cfc90fa3d324638c8c713443f9d298ad6a --fleet-root <scratch>/case-mut1/fleet --work <scratch>/work   # restored
$ python3 -B …/accept-c.py --root <scratch>/case-mut2/lane --lands aafbe1b422858be73d75692dbf380079f5e75073 --freeze fbcda5cfc90fa3d324638c8c713443f9d298ad6a --fleet-root <scratch>/case-mut2/fleet --work <scratch>/work
```

| case | verdict line | REPOINTED leg | failing set |
|---|---|---|---|
| pristine | `ACCEPT-C-77: FAIL legs=12/13` | `LEG PASS REPOINTED` | INDEX only |
| mut1 | `ACCEPT-C-77: FAIL legs=9/13` | `LEG FAIL REPOINTED` | ENTRIES, ROWS, REPOINTED, INDEX |
| restored | `ACCEPT-C-77: FAIL legs=12/13` | `LEG PASS REPOINTED` | INDEX only |
| mut2 | `ACCEPT-C-77: FAIL legs=7/13` | `LEG FAIL REPOINTED` | ENTRIES, ROWS, REPOINTED, GROUND, CITEDLINES, INDEX |

REPOINTED detail lines, verbatim (the counter truncates leg detail at 300
chars, `accept-c.py` line 1338 `detail[:300]`; the cut is in the printed line,
not my transcription):

- mut1: `corpus/knowledge/linguistics/naming-systems.amend-2026-10-23.md cites
  S903, which is neither a frozen lane row nor a base-held row;
  corpus/knowledge/linguistics/naming-systems.amend-2026-10-23.md cites the
  removed legacy id S886; corpus/knowledge/linguistics/naming-systems.
  amend-2026-10-23.md cites ` — the line ends mid-message at the 300-char cap;
  the remaining clause (the campaign-namespace arm for inline S903,
  accept-c.py:1259-1260, 1330-1331) is not visible in stdout.
- mut2: same first two clauses (S903 not-a-row; removed legacy id S886), also
  truncated at the cap.
- pristine/restored: `LEG PASS REPOINTED` with detail `source lines=2 lane
  rows=S897,S898 removed=S886,S888,S889,S890,S891,S896 staged universe=132`.

Corroborating leg details on the mutants: mut1 ENTRIES — `cites S886, which no
landed row carries; … cites S903, which no landed row carries`; mut1/mut2 ROWS
— `S898 is cited by no admitted entry (orphan row; used-by=
'corpus/knowledge/linguistics/naming-systems.amend-2026-10-23.md')`; mut2
CITEDLINES — `CITED-LINES: 3 finding(s) in 1 file(s)`; mut2 GROUND — both
sweeps absent (the pre-rewrite draft never carried the located quotes).

## Restoration evidence

- pristine entry blob `5144cb1884bd8ed0762246c55f73b459bc1df954`
- mut1 entry blob `3d2da3ac6e95757b9ced1e45c8493207dfa25afa`
- restored entry blob `5144cb1884bd8ed0762246c55f73b459bc1df954`
  (`git -C <fixture> rev-parse HEAD:<entry>`; equal to pristine: True)
- mut2 entry blob `d69ab75aba8c715bc8cdfb0470aa6066a6558c6e`
- The lane was never touched: all fixture repos lived under
  `/fast/scratch/hyaku/kotodama-r77/MutCentryIDs/case-*/lane`; scratch deleted
  after copying the raw outputs into `w2/stage/MutCentryIDs/`.

## Verdict and findings

1. **Assigned mutant KILLED.** REPOINTED fails the draft that retains S903 and
   one legacy id (S886) and passes the rewritten S897/S898 candidate; the
   restored bytes pass again. Baseline (pristine) is conclusive for this leg,
   so the kill is a real kill, not a baseline artifact.
2. **No surviving mutant** of the assigned class. The pre-rewrite draft (all
   six legacy ids) is also killed, and is additionally caught by ENTRIES, ROWS,
   GROUND and CITEDLINES — the entry-ID invariant is layered, with REPOINTED
   the only leg that names the legacy-id clause explicitly.
3. **Fixture artifact disclosure (constant, not a mutant effect):** INDEX fails
   in all four runs with `naming-systems.amend-2026-10-23.md index row is not
   the entry's `- topic:` text verbatim` — the fixture wrote a scaffold topic
   into corpus/README.md while the real entry's topic differs. It is
   independent of the entry-ID mutation (identical in pristine and restored
   runs) and says nothing about the lane. Consequently no run printed a full
   `PASS legs=13/13`; REPOINTED is the graded leg throughout, as assigned.
4. **Observation for the freeze (coverage, not contract change):** REPOINTED's
   printed detail truncates at 300 characters while mut1's message list is
   longer; an operator reading only the LEG line sees the S903 and S886
   clauses but not the inline campaign-namespace clause. The verdict bit is
   unaffected.

No installs (pacman paused; none needed). No fleet-repo, sibling-lane, lane-git,
LOG/SCORECARD/SKILL/SHONEN or corpus/reports production writes. Report trailer
paths are relative to the lane root.
