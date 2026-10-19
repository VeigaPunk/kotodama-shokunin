- Seat: C05 | executor | claim C (calibration) | date 2026-10-19 | baseline da68a6d

# C05 — calibration receipt draft: claim C before→after

**Assignment** (`reports/round-34/targets.json`, seat C05): "Calibration receipt draft:
before→after for claim C with the counting commands." Out path:
`reports/round-34/calib/C05-receipt.md`.

**Status.** DRAFT for the integrator. Every figure below is a live measurement taken by this
seat in the window below, or a cited filed reading. Nothing here is landed: the durable survey
artifact, the assembled reissue table and the round runner are named as other seats'
deliverables or as owed.

**Measurement window.** 2026-10-19 (in-session), lane root
`/home/vgpnk/Projects/shokunin/kotodama-shokunin`, env
`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`. `git rev-parse HEAD` →
`da68a6d705e41f369f21e8607bfaab5b54077f84`. `git status --porcelain` → `?? reports/round-34/`
only; no tracked byte was touched by this seat. No round runner was executed in-tree
(F-C13-1 prevention, `reports/round-34/claims.json:71`); the tools this seat ran —
`reports/round-30/craft/box1-survey.py`, `reports/round-25/audit/c31-lessons-index-audit.py`,
`reports/round-25/audit/x45-lessons-pointer-audit.py`,
`reports/round-27/audit/x57-lessons-audit.py --selftest` — are filed audit instruments, not
round runners.

## 1. The calibration move claim C buys

Claim C (`reports/round-34/claims.json:54-65`) converts a console-only green observation at a
superseded SKILL.md digest into a digest-pinned, dated, re-runnable receipt at the live digest,
and reissues the A09 R1–R8 anchor rows as new records with the old readings named *superseded*
rather than repaired in place. Claim fields: `:56` (claim), `:58` (before), `:60`
(after_required), `:61-64` (counting commands), `:65` (thresholds).

Honesty frame carried from the scorecard and the instrument itself: `SCORECARD.md:16` — "A raw
file or marker count is not a quality score"; `reports/round-30/run-validation.py:703` — "Box 1
is re-surveyed, not automatically promoted; remaining unnamed executables are reported, not
silently cleared." The 28/28 below is a path-resolution count.

## 2. Before — the filed readings claim C supersedes

| # | reading at HEAD `da68a6d` | value | source |
|---|---|---|---|
| B1 | durable box-1 receipt (filed, the only durable one) | `skill_sha256 83b0a78a…`, `date 2026-10-18`, `named_in_skill 28` / `resolvable 28` | `reports/round-30/craft/box1-landed-survey.json:2,4-6` |
| B2 | SKILL.md digest recorded at r31 admission | `79fe91d3…` | `reports/round-31/validation.json:1026` |
| B3 | SKILL.md digest recorded at r32 admission | `79fe91d3…` | `reports/round-32/validation.json:1000` |
| B4 | box-1 re-verification as prose + console only | "28/28 named executables resolve, re-verified this round: `python3 -B reports/round-30/craft/box1-survey.py` exit 0 at SKILL sha `79fe91d3…`" | `reports/round-32/final-dossier.md:46` (+ command block `:133`); `reports/round-32/dossier-d11-shonen-boxes.md:50,205`; `reports/round-32/dossier-d12-capability-inventory.md:97`; `reports/round-32/dossier-d13-operator-decisions.md:48`; `reports/round-32/scribe/fragment-ledger.md:178,235` |
| B5 | SKILL.md digest / line count at the round-33 entry (pre-edit) | `79fe91d3…`, 715 lines | `reports/round-33/op/K01-falsifier-scout.md:136` |
| B6 | A09's anchor readings (the R-rows' before-state) | `:522`, `:534-536`, `:660`, `:713-715` at 715 lines; live anchor `AGENTS.md:42` | `reports/round-33/adj/A09-pins.md:87,89`; R-table `:107-114` |
| B7 | round-33 admission already recorded the digest move + the AGENTS excision as supersessions | "SKILL.md digest `79fe91d3…` → `f9bd07c2…`; AGENTS.md drafting residue excised (42 → 40 lines)" | `SCORECARD.md:599` |

B1 pins a digest two moves behind live (`83b0a78a…` → `79fe91d3…` → `f9bd07c2…`); B2–B4 are
digest readings in filed receipts and prose that the round-33 SKILL edit already superseded.
Every B-row is a filed byte: none may be edited; the reissue is new rows only.

## 3. Live measurement — counting command 1

Command (claim C's first counting command, `reports/round-34/claims.json:62`):
`python3 -B reports/round-30/craft/box1-survey.py`. Verbatim output, exit 0:

```json
{
 "date": "2026-10-18",
 "named": 28,
 "resolvable": 28,
 "unnamed_in_skill": [],
 "skill_sha256": "f9bd07c2bd13462367be20e8d775cec1c5569eb2e575dc5d078519ecc72e5a9b"
}
```

Corroboration of the digest and line count: `sha256sum SKILL.md` →
`f9bd07c2bd13462367be20e8d775cec1c5569eb2e575dc5d078519ecc72e5a9b`; `wc -l SKILL.md` → 732.

The 28 named executables, each resolving on disk (existence check, all OK):
`tools/assemble-culture-d3.py`, `tools/assemble-culture-d4.py`, `tools/assemble-d2-typed.py`,
`tools/assemble-d2.py`, `tools/assemble-d4-typed.py`, `tools/check-craft-exercise.py`,
`tools/check-evidence-coupling.py`, `tools/check-gate-battery.py`, `tools/d2-typed-labels.py`,
`tools/exercise-handoff-e2e.py`, `tools/gates/argot-derivation-gate.py`,
`tools/gates/costume-era-consistency-gate.py`, `tools/gates/d4-assembly-check-gate.py`,
`tools/gates/d4-typed-labels-check-gate.py`, `tools/gates/handoff-packet-check.py`,
`tools/gates/lexicon-coverage-audit.py`, `tools/gates/myth-consistency-gate.py`,
`tools/gates/naming-collision-gate.py`, `tools/gates/phonology-sanity-gate.py`,
`tools/gates/provenance-audit.py`, `tools/gates/register-law-gate.py`,
`tools/gates/typed-pipeline-gate.py`, `tools/harness/packet_links.py`,
`tools/harness/packet_uncertainty.py`, `tools/harness/r8_checks.py`,
`tools/harness/receipt_guard.py`, `tools/replay-frozen.py`, `tools/source-audit-inventory.py`.

**Two instrument findings that the durable receipt must handle** (calibration-relevant: they
decide whether the landed artifact is a true reading or a copied defect):

- **C05-F1 — the counting instrument's `date` field is a hard-coded literal.**
  `reports/round-30/craft/box1-survey.py:8` builds `{"date": "2026-10-18", …}` as a constant;
  the script reads no clock. A verbatim capture at any later date therefore carries a false
  observation date. The durable receipt must stamp the true observation date out-of-band — the
  instrument cannot self-date — or the date cell reads as an instrument defect.
- **C05-F2 — the instrument's output shape differs from the filed receipt shape.** The script
  emits `named` / `resolvable` / `unnamed_in_skill` / `skill_sha256`
  (`reports/round-30/craft/box1-survey.py:8-10`); the filed round-30 receipt carries
  `named_in_skill` / `resolvable` / `unresolvable` / `mode` / `box1_note`
  (`reports/round-30/craft/box1-landed-survey.json:3-8`). A verbatim capture cannot match the
  filed shape; the integrator must state which shape the durable artifact adopts and how it was
  derived from the script output.

## 4. Anchor map — the SKILL.md side of the A09 R1–R8 reissue

A09 measured its rows at the 715-line / `79fe91d3…` tree (`reports/round-33/adj/A09-pins.md:87-94`).
The round-33 landing moved SKILL.md to 732 lines. The line map is derivable from the landing
diff, `git diff -U0 17e90b9 da68a6d -- SKILL.md` — hunk headers `@@ -128 +128 @@`,
`@@ -479/481/483/486/488/491/501 +… @@`, `@@ -584 +584,3 @@`, `@@ -694,4 +696,5 @@`,
`@@ -699,2 +702,4 @@`, `@@ -704 +709,12 @@`, `@@ -714,2 +730,3 @@` — giving cumulative offsets
0 (≤583), +2 (584–693), +3 (694–698), +5 (699–703), +16 (704–713), +17 (≥714). The arithmetic
checks: 715 + 17 = 732.

| A09 anchor at 715 lines | measured at 732 lines | check | verdict |
|---|---|---|---|
| `:47` — "adding typing fields cannot exempt a string" | `:47` | `awk`/`grep`, same content | unchanged |
| `:149` — self-cite `SKILL.md:47` | `:149` | `grep -n "SKILL\.md:" SKILL.md` | unchanged |
| `:183` — self-cite `SKILL.md:47` + `era-language-staging.md:111` | `:183` | same grep | unchanged |
| `:522` — `## Checklist (executable where a tool exists)` | `:522` | `grep -n` heading | unchanged |
| `:534` last checklist content line / `:535` blank / `:536` `## Corpus map` | `:534` / `:535` / `:536` | `awk` window | unchanged |
| `:660` — `## Source-bounded culture drill — D3 (round 7)` | `:662` | `grep -n` heading | **shifted +2** |
| `:713-715` — availability/dispatch closing-snapshot checklist item + audit one-liner | `:729` / `:731` / `:732` | `awk` window at both revisions | **shifted +16 / +17** |
| `AGENTS.md:42` — "append one item to '## Checklist …' (after :534)" | **absent** — AGENTS.md is 40 lines | `wc -l AGENTS.md` → 40; `grep -n "append one item" AGENTS.md` → no match (rc=1); `git diff --numstat 17e90b9 da68a6d -- AGENTS.md` → `0 2` | **row's target deleted at da68a6d** |

So A09 **R5**'s live-anchor leg reads *superseded-and-absent*, not merely shifted: the line the
row points at was removed by the round-33 AGENTS.md excision — the same excision
`SCORECARD.md:599` records as "42 → 40 lines". Three legs (self-cites, checklist head,
corpus-map boundary) are byte-position stable; two moved.

Scope note: the assembled old-anchor → new-anchor → owning-row table covering all eight A09 rows
is C03's deliverable. This section supplies the SKILL.md measurements that table needs and the
row-scope split in §5.

## 5. Which R-rows are still owed at HEAD, and which were closed by round 33

| A09 row (`reports/round-33/adj/A09-pins.md:107-114`) | state at `da68a6d` | in claim C's scope? |
|---|---|---|
| R1 README git-blob pin in the r26 runner | closed as a supersession at round 33 — live blob `73f3e1bd29d4569ddd2a5d9a2309f4451fa35ae5` (`git hash-object corpus/lessons/README.md` == `git rev-parse HEAD:corpus/lessons/README.md`), was `a3187055…` at A09 (`:36,57,61`); `SCORECARD.md:598-599` records the new row | no |
| R2 README sha256 receipts (6 sites) | live README digest `f752e1d79ae627a0d9728fe16fd1532e7cb9e587f6ac7025a880d8af46233868`, 448 lines, 33 rows (measured this window); the listed rows are superseded readings of the revision-3 landing | no |
| R3 SKILL.md sha256 receipts (8 sites) | **owed** — the reissue must name the `79fe91d3…` rows as superseded and `f9bd07c2…` as current at HEAD | **yes** |
| R4 box-1 re-survey | **owed** — `reports/round-34/craft/box1-resurvey-durable.json` per `claims.json:60` | **yes** |
| R5 SKILL.md line anchors | **owed** — §4 measurements; `AGENTS.md:42` leg is absence, not shift | **yes** |
| R6 README prose arithmetic + new rows' cells | closed by round 33's O claim: `python3 -B reports/round-25/audit/c31-lessons-index-audit.py` → exit 0, findings 0, 33 files == 33 rows, `formats {'gate-keeper': 21, 'fragment-index': 5, 'plain': 7}` (measured this window) | no |
| R7 x45 / x57 instruments | **carried as named findings, not fixed** — and redder than A09 recorded (§6) | no (must be named) |
| R8 README rows vs `round-33.md` landing order | closed by the round-33 O landing (`SCORECARD.md:589` attributes the 33/33 rows); c31's `C31_index_rows_eq_files` PASS at 33 == 33 is the live check | no |

The claim's threshold "the reissue table covers every A09 R1–R8 row" (`claims.json:65`) is
therefore satisfiable: five rows are closed-by-supersession or closed-by-round-33, three are
claim C's own (R3/R4/R5). The table still has to *name* all eight, which is C03's assembly.

## 6. R7 instruments — live readings vs A09's

| instrument | A09 at `139e3b6` (`A09-pins.md:100,125`) | measured at `da68a6d` (this window) |
|---|---|---|
| `reports/round-25/audit/x45-lessons-pointer-audit.py` | exit 1, `X45-P1 unresolved-pointer` naming the round-4 row's `reports/round-4*` glob | exit 1; `P1_pointers_resolve` FAIL, `P2`/`P3` PASS, findings 1; the single finding now names **4 tuples** — the round-4 glob row plus pointer rows for `corpus/lessons/round-26.md`, `round-27.md`, `round-29.md`. Counters: lessons 33, index rows 33, queue rows 78, carry rows 30 |
| `reports/round-27/audit/x57-lessons-audit.py --selftest` | 34/37 | **28/37, exit 1**; the 9 failing controls: `partition is 27 md files` (obs 33), `filed rows are 26` (obs 33), `revision pins drift on exactly one row (live control)` (obs `["README.md","round-26.md"]`), `filed orphan is exactly round-26.md (live control)` (obs `[]`), `revision has no orphan (live control)` (obs 6 files), `filed queue is 49 rows (live control)` (obs 78), `G2 silent when the revision pin matches the live bytes`, `I reads 49 queue ids and 49 disposition rows` (obs `[78,49]`), `I is green on the live revision` (obs 3 queue ids) |

A09's rule stands and is now stronger: neither instrument may be quoted as green at HEAD.
Both readings are revision-bound — A09 measured at `139e3b6`, this seat at `da68a6d`, and the
round-33 landing changed exactly the values those controls compare against (README revision-3:
346 → 448 lines, blob `a3187055…` → `73f3e1bd…`, queue 49 → 78, partition 26 → 33 rows).
**Attribution of the 34/37 → 28/37 and 1-tuple → 4-tuple deltas to the round-33 landing is
`to-verify` here** — the pre-revision-3 run was not performed by this seat. What is measured is
the delta itself and the revision at each end.

## 7. Counting command 2 — not yet runnable

`python3 reports/round-34/run-validation.py` (`claims.json:63`) does not exist at this read
(`ls reports/round-34/run-validation.py` → No such file or directory), which matches the
`targets.json` shared rule that "this round's own `reports/round-34/run-validation.py` does not
exist yet". This seat does not execute round runners in-tree under any circumstance
(`claims.json:71`); the runner must be exercised only from an isolated `git archive` copy.

## 8. After-state checklist this receipt asserts (each item falsifiable)

| # | after-state requirement (`claims.json:60,65`) | check | status at this seat's read |
|---|---|---|---|
| A1 | `reports/round-34/craft/box1-resurvey-durable.json` exists, digest-pinned to `f9bd07c2…`, dated, re-runnable | re-run the survey; artifact's digest literal == `sha256sum SKILL.md`; declared shape per C05-F2; true date per C05-F1 | **owed** (C02's deliverable) |
| A2 | 28/28 named executables resolve at the new digest | §3 | **measured green at this seat's read** |
| A3 | reissue table covers every A09 R1–R8 row: old anchor → new anchor → owning row, each grep-verified | assembled table (C03) using §4/§5 | **partially evidenced; table owed** |
| A4 | promotion-dossier box-1 evidence current at HEAD | a round-34 record naming `f9bd07c2…` as current, with the r32 rows (`final-dossier.md:46,133`; dossier-d11/d12/d13; fragment-ledger) read as superseded, filed bytes untouched | **owed** |
| A5 | zero filed-round edits | `git status --porcelain`; `git diff --stat -- reports/round-30/ reports/round-31/ reports/round-32/ reports/round-33/` | **clean at this seat's read** (`?? reports/round-34/` only) |
| A6 | counting command 2 exits 0 (`REGIMEN.md:41`) | isolated `git archive` copy of round 34 | **owed** (runner absent) |

**Verdict framing for the integrator, not asserted here.** Per `REGIMEN.md:37-43` a round is
admitted only when every claim verifies and no axis is harmed; this seat's evidence supports
"verifiable" for A2/A5 and leaves A1/A3/A4/A6 to the landed revision. A calibration
*improvement* is claimable only once A1/A3/A4 land. Until then the honest reading is: the
observation is green and re-measurable, the durable form is not yet on disk — and the
`unclaimed-observation` variant of a calibration row (`SCORECARD.md:34` and following) would
overstate it.

## 9. Cross-checks with sibling fragments (read after this draft was written)

The C-block siblings landed while this draft was being written. Where they touch this fragment:

- **Convergent, no erratum.** `C01-survey-run.md:18-36` (same verbatim JSON, same 732 lines,
  same digest at baseline and HEAD), `C02-receipt-json.md:11-14` (same digest, 28 named /
  28 resolvable / `unnamed_in_skill []`), `C07-verify-survey.md:9,32` (independent 28/28 at
  `f9bd07c2…`), `C06-scribe.md:36-57` and `C09-final-receipt.md:52-54` all reproduce §3's
  reading. C06 independently names the same two instrument defects this fragment's C05-F1/F2
  name (`C06-scribe.md:47,55-57`) and the same `AGENTS.md:42` absence (`C06-scribe.md:122`).
  C09's anchor table (`C09-final-receipt.md:194-210`) matches §4 row-for-row on the legs it
  covers: `:522`, `:534`, `:535`, `:536` unchanged; `:660` → `:662`; `:713-715` → `:729-732`;
  `AGENTS.md:42` "target is gone". C09's `:584` hunk is the +2 boundary §4 derives.
- **This fragment updates one sibling row.** `C09-final-receipt.md:264` carries R7 as
  "A09-F4 stands as filed … Nothing this seat ran contradicts it" — C09 did not re-run either
  instrument. §6 is the live re-run at `da68a6d`: x45's finding grew from 1 tuple to 4, and
  x57 `--selftest` reads 28/37 (A09-F4 filed 34/37 at `139e3b6`). The final fold should carry
  §6's numbers with their revisions, not A09-F4's alone.
- **C03 never landed.** `ls reports/round-34/calib/C03*` → absent at this read. Its table is
  nevertheless covered in substance by `C09-final-receipt.md`'s §6 fold, which this fragment's
  §4/§5 agree with; the integrator should treat C03's absence as satisfied-by-fold rather than
  as a hole, while §5's R-row *scope split* (which A09 rows are claim C's own) remains this
  fragment's framing.
- **A1's C05-F1 requirement is met by C02's draft bytes, not yet by a landed file.** C02's
  durable JSON sets `"date": "2026-10-19"` plus `"measured_at_utc"` and a `supersedes` field
  (`C02-receipt-json.md:28-34,45-49`); `reports/round-34/craft/` does not exist at this read, so
  A1 stays "owed" in the sense of *landing*, not of *drafting*.

## Owed

- `reports/round-34/calib/C01-survey-run.md`, `C02-receipt-json.md`, `C03-anchor-reissue.md`,
  `C04-byte-check.md` — this mission's named dependency fragments; `reports/round-34/calib/` was
  empty at this seat's first read (04:00Z). C01/C02/C04 landed during this seat's run and are
  cross-checked in §9; **C03 never landed** (`ls reports/round-34/calib/C03*` → absent) — its
  table is covered in substance by `C09-final-receipt.md` §6, which §4/§5 agree with.
- `reports/round-34/craft/box1-resurvey-durable.json` — claim C's after-state artifact
  (`claims.json:60`); must carry a true observation date (C05-F1) and declare which key shape it
  adopts (C05-F2). C02's draft bytes already do both (`C02-receipt-json.md:28-34,45-49`); the
  remaining owed step is the integrator's landing, since `reports/round-34/craft/` does not exist
  at this read. The r30 box-1 detector idiom (`reports/round-30/run-validation.py:674-685`,
  conditions at `:328-329` and `:44-45`) is **not** a binding constraint here: that runner scans
  `reports/round-30/` docs only, and filed round-30 is never re-run at round 34.
- `reports/round-34/run-validation.py` — claim C's second counting command; absent at this read.
- The assembled old-anchor → new-anchor → owning-row table for all eight A09 rows (C03); C09's
  §6 fold is the surviving assembly, so the integrator owes only the C03-absent note.
- Attribution of the x57 34/37 → 28/37 and x45 1-tuple → 4-tuple deltas to the round-33 landing
  (`to-verify`; a pre-revision-3 run of both instruments would settle it, and neither instrument
  may be quoted as green in the meantime).

## Citations

- `reports/round-34/claims.json:54-65` (claim C: `:56` claim, `:58` before, `:60` after, `:61-64`
  counting commands, `:65` thresholds), `:71` (no in-tree round-runner execution);
  `reports/round-34/targets.json` seat C05 + `shared_rules`; `REGIMEN.md:27,37-43`
  (`:41` admit-only rule)
- Filed readings: `reports/round-30/craft/box1-landed-survey.json:2,3-8`;
  `reports/round-30/run-validation.py:44-45,328-329,645-652,674-685,697-698,703,712`;
  `reports/round-30/craft/box1-survey.py:5,6,7,8,10`
- `reports/round-31/validation.json:1026`; `reports/round-32/validation.json:1000`;
  `reports/round-32/final-dossier.md:46,133`; `reports/round-32/dossier-d11-shonen-boxes.md:50,205`;
  `reports/round-32/dossier-d12-capability-inventory.md:97`;
  `reports/round-32/dossier-d13-operator-decisions.md:48`;
  `reports/round-32/scribe/fragment-ledger.md:178,235`
- `reports/round-33/op/K01-falsifier-scout.md:136`; `reports/round-33/adj/A09-pins.md:36,57,61,87,89,94,100,107-114,125`;
  `SCORECARD.md:16,34,589,598,599`
- `SKILL.md:47,149,183,522,534,535,536,662,729,731,732`; `AGENTS.md` (40 lines, no `append one item` line)
- Sibling fragments read post-write (§9): `reports/round-34/calib/C01-survey-run.md:18-36`;
  `C02-receipt-json.md:11-14,28-34,45-49`; `C06-scribe.md:36-57,122`; `C07-verify-survey.md:9,32`;
  `C09-final-receipt.md:52-54,194-210,264`; `ls reports/round-34/calib/C03*` → absent
- `corpus/lessons/README.md` (448 lines, sha256 `f752e1d7…`, git blob `73f3e1bd…`); `corpus/lessons/*.md` (33 files)
- Commands run (2026-10-19, lane root, `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`):
  `git rev-parse HEAD`; `git status --porcelain`; `sha256sum SKILL.md AGENTS.md corpus/lessons/README.md`;
  `wc -l SKILL.md AGENTS.md corpus/lessons/README.md`; `git hash-object corpus/lessons/README.md`;
  `git rev-parse HEAD:corpus/lessons/README.md`; `ls corpus/lessons/*.md | wc -l`;
  `python3 -B reports/round-30/craft/box1-survey.py` (exit 0, verbatim JSON in §3);
  python one-liner re-deriving the 28 `tools/**.py` names from `SKILL.md` with per-path existence
  checks (28/28); `python3 -B reports/round-25/audit/c31-lessons-index-audit.py` (exit 0, findings 0);
  `python3 -B reports/round-25/audit/x45-lessons-pointer-audit.py` (exit 1, P1 FAIL, 4 tuples);
  `python3 -B reports/round-27/audit/x57-lessons-audit.py --selftest` (exit 1, 28/37);
  `git diff -U0 17e90b9 da68a6d -- SKILL.md | grep '^@@'`; `git diff 17e90b9 da68a6d -- AGENTS.md`;
  `git diff --numstat 17e90b9 da68a6d -- SKILL.md AGENTS.md corpus/lessons/README.md` (`35 18`,
  `0 2`, `130 28`); `git log --oneline -- SKILL.md AGENTS.md`; `git show 17e90b9:AGENTS.md | wc -l` (42);
  `git show 17e90b9:SKILL.md | awk 'NR>=706 && NR<=715'`; `awk`/`grep -n` windows over `SKILL.md`
  at both revisions; `ls reports/round-34/run-validation.py` (absent)
