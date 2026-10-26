# ExecLegRejects — claim-C REJECTS leg (round 75, wave 2, pre-freeze)

Seat: leaf executor. Task: build `leg_rejects` for the round-75 claim-C counter, test it on a mock
landing, attack it with mutants of that mock, and report. No claim/ledger byte edited; no lane, fleet or
sibling-lane byte edited; read-only git only; pacman not run; nothing installed.

The leg text was re-cut by the L1 mid-build (`claims.json` 2026-10-27, sha256
`e8007fc2d457d2e9408cd18565e51264a6a09b8623419e3b6895ad3f3f37692b`): the counts are now
**`3 adopted / 6 path-present / 31 refused`** with a new `rejects.counts` object
(`{adopted 3, path_present 6, refused 31, total_staged_files 40}`). This report describes the re-cut leg;
the earlier `adopted + refused == total` reading is superseded.

## Files written (only these)

| path | sha256 | notes |
|---|---|---|
| `.ufo/waves/round-75/w2/parts/leg-rejects.py` | `f6701774420c3e57ccbd6a60d8f1284fbd55f5c823a8d9a6cc60456e87cf35df` | 16 785 bytes, 363 lines, 10 module-level `FunctionDef` nodes only (no top-level code, no imports), assembled PART A(1-510) + this part compiles, `py_compile` clean |
| `.ufo/waves/round-75/w2/ExecLegRejects.md` | this report | — |

No `part-cfg.py` existed while I built and tested, so the cfg was hand-built to the CFG-CONTRACT shape,
with `counts` read verbatim from `claims.json` `rejects.counts` (the note key dropped) — the pass-through
shape ExecCtrCfgMain confirmed. The leg needs no key outside CFG-CONTRACT.

## Leg text as I read it (re-cut)

Frozen text (`reports/round-75/claims.json`, claim C `legs`):

> REJECTS: the lesson states the triage counts of the 40 staged knowledge files as `3 adopted / 6
> path-present / 31 refused` (the three numbers sum to 40 and equal rejects.counts at the freeze), names
> each refused staged row and file with reason and flip, names staged S870's disposition with its re-quote
> or its refusal, and carries a `## Quarantine` section recording the standing register verdicts.

Checks the part implements, in order (`leg_rejects`):

1. **Counts (one paragraph, one identity).** One blank-line block must state all four numbers — adopted,
   path-present, refused and the staged-file total — and the leg requires `adopted + path_present +
   refused == total`, then each number equal to `cfg["counts"]` (`3 / 6 / 31 / 40`) and `adopted ==
   len(cfg["entries"])`. There is **no other arithmetic**: `refused` is not derived as `total - adopted`.
   Parsed shapes: `N staged … files` (or `of the N staged`), or the identity line `3 + 6 + 31 = 40`, for
   the total; `N adopted`, `N path-present`, `N refused` for the three published numbers.
2. **Refused file families.** For every frozen `rejects.refused_files_pending_triage` string, a markdown
   table row with a reason-ish column (`why`/`reason`) and a flip-ish column (`flip`/`revers`/`clearing`)
   must name the family, and that row's reason **and** flip cells must each be substantive (not a dash, not
   a PLACEHOLDER, ≥ 4 words or ≥ 40 chars) — per item; global "reason"/"flip" prose does not satisfy
   (CritCCounterVacuity repair 6).
3. **Bucket split.** File-bucket rows (`| family | files | why | flip |`) must carry the two frozen
   numbers split the way the freeze splits them: rows whose **first cell** names a refused family sum to
   `counts.refused` (31); rows that name no refused family — the path-present bucket — sum to
   `counts.path_present` (6) (RevClaimsFidelity F11's reconciliation, re-cut to the new counts). Rows keyed
   by a staged id in their first cell are excluded (a reject row is not a file bucket). Count shapes
   accepted: a digits-only cell (`| 11 |`), a digit sum (`| 3 + 1 |`), or `(N)` / `xN` in the row.
4. **S870's disposition.** A unit (table row or paragraph) naming a `cfg["refused_staged"]` id must carry a
   refusal (`REFUSAL_RE`) and be tied to the re-quote side: the lane id the frozen `row_staged` map binds
   (`S870 → S893`) or a re-quote/re-open marker; a reason+flip table row naming it must have both cells
   substantive.
5. **`## Quarantine`.** The section must exist and record the standing register verdicts: the per-class
   counts re-derived from `reports/round-71/telemetry/quarantine-verdicts.md` **at `<lands>`**
   (PRESENT 10 / REFUSED 7 / UNVERIFIABLE 4 = 21), the 21-row total, and every REFUSED id named with its
   REFUSED verdict (an upgrade to PRESENT is red). Nothing about those numbers is hard-coded.

## Ambiguities and how I resolved them

1. **"the three numbers sum to 40 and equal rejects.counts at the freeze"** — read literally: four numbers
   parsed, the identity enforced, and each of the three published numbers compared with the freeze's
   `counts`; `refused` is *not* recomputed from the total (the L1's explicit cut). When `cfg["counts"]` is
   empty (an unfrozen copy) the identity and `adopted == len(entries)` still bind, and the bucket split
   falls back to the lesson's own numbers; this is tested.
2. **What the counts are (derived, not assumed).** `shokuknow/merge/kotodama/knowledge` holds **40** staged
   `.md` files (myth-symbol 5, linguistics 17, culture-material 9, verification 9). Of those: **3 adopted**
   (the three frozen `entries`), **6 path-present** (heritage ×2, worldbuilding ×2, `conlang-scholarship.md`,
   `conlang-scholarship.amend-2026-10-23.md`), **31 refused** (naming-systems 11 + verification 9 +
   calendar 3 + era 2 + conlang-scholarship amendments 3 + conlang-methodology 1 + narrative c/24 2). The 4
   parent entries under `merge/kotodama/amendments` are outside the 40 — `find knowledge amendments | wc -l`
   returns 44, so a 40 read off both roots would be wrong.
3. **"names each refused staged row and file"** — the freeze names refused *families* (`naming-systems
   x11`, …), not paths, so the leg binds family-level naming; the bucket split (3) is what makes the family
   counts add up to the frozen 31 and keeps the six path-present files as their own declared bucket.
4. **"with reason and flip"** — per item, not global; a dash/`n/a`/placeholder cell fails.
5. **"with its re-quote or its refusal"** — read as *the disposition named*: the frozen `after` ("the
   staged quote itself remains rejected", "the document is re-opened as lane row S893") and the kill rule
   require both sides, so the leg requires a refusal marker **and** the mapped lane id (or a re-quote
   marker when the freeze maps no target). A bare "S870 refused" with no re-opened row fails, and so does
   an "S870 admitted".
6. **"recording the standing register verdicts"** — re-derived from the committed verdicts file at
   `<lands>`, not from a prose template; if that file is unreadable the leg is red (the standing record
   must survive).
7. **Reads.** Lesson and quarantine verdicts from `mat` only; no network, no lane worktree, no shokuknow at
   grade time, no scratch.

## Test setup

Scratch `/fast/scratch/hyaku/kotodama-r75/ExecLegRejects4/` (final matrix; an earlier set under
`…/ExecLegRejects2` was destroyed mid-run at 16:53 by ExecTmpSweep's `rm -rf
/fast/scratch/hyaku/kotodama-r75`, and was rebuilt): `git archive f556d104…` of the lane into `mat`, then
the lesson under test copied to `mat/corpus/lessons/round-75.md` and the leg called with `exec()` of PART A
(lines 1-510 of `.ufo/waves/round-75/counters/accept-c.py`) + `parts/leg-rejects.py` in one namespace,
`counts` taken from the freeze (and a `counts={}` variant). The quarantine file is the committed base blob.
Both cfg variants were run for every fixture.

The positive fixture is the draft lesson's shape with the re-cut counts: "40 staged `.md` files …; **3
adopted / 6 path-present / 31 refused** of the 40 (3 + 6 + 31 = 40)", a 7-row reason+flip triage table with
refused families 2+11+3+2+9+4 = 31 and a path-present row of 6, the Gate reject table
(`reason | flip | probed URL | verdict`) with the S870 row, the "S870's disposition, stated once" paragraph
(stays REFUSED; document re-opened as S893), and a `## Quarantine` section with 10/7/4/21 and all 7 REFUSED
ids.

## Positive / mutant table (exact counter output)

| fixture | output |
|---|---|
| positive, freeze counts | `LEG PASS REJECTS` (exit 0) |
| positive, `cfg["counts"] = {}` | `LEG PASS REJECTS` (exit 0) |
| variant: header `| family | files | reason | flip |`, counts written "adopted 3 files / path-present 6 files / refused 31 files of the 40", a Gate reason carrying "(2026-10-27 re-test)" | `LEG PASS REJECTS` (exit 0), both cfg variants |
| **the w2 staged lesson as it stands now** (`stage/corpus/lessons/round-75.md`) | `LEG FAIL REJECTS` — `lesson states no single triage-counts paragraph (adopted + path-present + refused + staged total together)` (it still says "3 adopted / 37 refused"; see F1) |
| the stale `drafts/lesson.md` | `LEG FAIL REJECTS` — `lesson states 2 adopted; the freeze holds 3; lesson states 32 refused; the freeze holds 31; refused-family buckets sum to 32 files; the freeze holds 31 refused; no path-present bucket row declares a file count; the freeze holds 6 path-present` |
| lesson missing at `<lands>` | `LEG FAIL REJECTS` — `lesson unreadable at <lands>: corpus/lessons/round-75.md` |

Mutants of the positive mock — every one violates the re-cut wording; all red under freeze counts **and**
under `counts={}`:

| mutant | what it violates | counter line |
|---|---|---|
| M1-counts-adopted `2 adopted / 6 path-present / 32 refused` | adopted ≠ freeze, refused ≠ freeze | `lesson states 2 adopted; the freeze holds 3; lesson states 32 refused; the freeze holds 31` |
| M15-refused-37 `3 adopted / 0 path-present / 37 refused` (sum still 40) | the L1's old arithmetic re-smuggled in | `lesson states 0 path-present; the freeze holds 6; lesson states 37 refused; the freeze holds 31` |
| M9-total-mismatch `3 / 6 / 31` but total 39 everywhere | identity broken | `triage counts do not sum: 3 adopted + 6 path-present + 31 refused = 40, not the 39 stated; lesson states 39 staged total; the freeze holds 40` |
| M7-partition-gap: path-present row dropped | path-present bucket missing | `no path-present bucket row declares a file count; the freeze holds 6 path-present` |
| M16-no-path-bucket: path row declares 9 | bucket count wrong | `path-present buckets sum to 9 files; the freeze holds 6` |
| M5-family-missing: naming-systems row deleted | family unnamed + counts short | `refused file family 'naming-systems' is not named in a table row carrying a reason column and a flip column; refused-family buckets sum to 20 files; the freeze holds 31 refused` |
| M6-global-reason-flip: table replaced by a family list + one global "reason and flip are the same" sentence | the CritCCounterVacuity junk path exactly | `refused file family 'naming-systems' is not named in a table row …; 'calendar-festival-systems' …; 'era-periodization-models' …` |
| M2-flip-dash: naming row's flip cell `—` | per-item flip | `'naming-systems': flip cell is empty, a dash or a placeholder` |
| M10-reason-placeholder: naming row's reason cell `n/a` | per-item reason | `'naming-systems': reason cell is empty, a dash or a placeholder` |
| M14-s870-reason-dash: S870 row's reason cell `—` (id kept) | per-item reason on the refused staged row | `refused staged S870: no row states both a reason and a flip` |
| M3-s870-no-requote: S870 row kept, flip "a later round", S893 sentence deleted | disposition lacks the re-quote side | `staged S870 is not tied to its re-opened lane row S893` |
| M12-s870-absent: Gate row + disposition paragraph removed | staged row not named | `refused staged S870 is not named in the lesson` |
| M4-no-quarantine: section deleted | `## Quarantine` | ``no `## Quarantine` section in the lesson`` |
| M11-quarantine-bare: section kept, one bare sentence | standing verdicts not recorded | ``does not record PRESENT 10; … REFUSED 7; … UNVERIFIABLE 4; … the 21-row total; REFUSED register row S779 is not named …`` |
| M8-quarantine-count: `REFUSED 9` on both lines, S814 dropped | counts + ids | ``does not record REFUSED 7; REFUSED register row S814 is not named in `## Quarantine` `` |
| M13-quarantine-upgrade: S816 moved into the PRESENT bullet | verdict upgraded | ``does not record PRESENT 10; does not record REFUSED 7`` |

## Findings for the L1 / scribe (pre-freeze, actionable)

- **F1 (blocking until the lesson is re-cut). The w2 staged lesson fails the re-cut leg.** It still carries
  the pre-cut wording "**3 adopted / 37 refused** (3 + 37 = 40)" plus "Refused (37) = 31 by family + 6
  path-present", so no single paragraph states `3 adopted / 6 path-present / 31 refused` and the total.
  The leg reds it with `lesson states no single triage-counts paragraph …`. The fix is textual and small:
  state the four numbers in one paragraph, e.g. "40 staged `.md` files …; **3 adopted / 6 path-present / 31
  refused** of the 40 (3 + 6 + 31 = 40)", and keep the refused-family rows summing to 31 with a
  path-present row of 6 (the current table already splits the rows that way).
- **F2 (resolved). `rejects.counts` is in the freeze now**, so `cfg["counts"]` is live and the identity is
  pinned to `3 / 6 / 31 / 40`. part-cfg passes it through verbatim (ExecCtrCfgMain confirmed; a non-integer
  value is dropped, not invented).
- **F3. The freeze names 31 refused files by family** (naming 11, verification 9, calendar 3, era 2,
  conlang-scholarship 3, conlang-methodology 1, narrative 2) and the 6 path-present files only by count; the
  leg binds the family names and the two bucket totals, not the six paths.
- **F4. `## Quarantine` is graded against `reports/round-71/telemetry/quarantine-verdicts.md` at `<lands>`**
  (committed at base: 21 rows, PRESENT 10 / REFUSED 7 / UNVERIFIABLE 4 with ids S776,S778,S795,S796,S804,
  S820,S823,S824,S825,S827 · S779,S786,S787,S792,S814,S816,S817 · S791,S807,S812,S835). A landing that
  removes or rewrites that file turns REJECTS red — intended.
- **F5. `find knowledge amendments | wc -l` = 44, not 40.** The 40 is the `knowledge/` tree; the 4 parent
  entries under `amendments/` are outside it (recorded so a later seat does not "fix" a correct 40 into 44).

## Limits of this leg (honest survivors)

- The truth of a reason/flip *text* is not checked (impossible from the lesson alone); only that it is
  substantive and per item. Gate/re-open legs own page truth.
- The 6 path-present files are bound by their bucket count (6), not by name.
- A lesson that names the refused staged row's id only in prose (no reason+flip table row) is graded by the
  prose refusal/re-quote path; M14 marks that boundary.
- The total is read from the lesson and checked against the freeze; it is not re-derived from the staged
  tree at grade time (the counter never sees that tree).

## Environment

No tool installed, no upgrade, no pacman (host-wide pause honoured). Scratch
`/fast/scratch/hyaku/kotodama-r75/ExecLegRejects{2,4}/` deleted before yield; every cited value is
reproduced in this report. Lane tree untouched (`git status --porcelain` shows only the pre-existing
uncommitted edits `SHONEN.md`, `SKILL.md`, `reports/round-28/readme/sweep.py` and the untracked round-75
directories — none written by this seat).
