# MutateAccessChecker — round 52, attempt 1

**Seat:** `KotodamaR52.MutateAccessChecker` (leaf, no subagents dispatched)
**Target:** `tools/check-source-access.py` (QUALITY criterion 10 checker, added at base `147cfde85eb13256438c1ed04d92e8d2ad09b76e`)
**Date:** 2026-10-22
**Scope:** mutation-test the access checker in a sandbox copy; attack claim D's landed bytes (`dea5ece`) without changing the lane.

## Assigned item

The assignment was to mutate `tools/check-source-access.py` in a sandbox copy at `/fast/scratch/hyaku/kotodama-r52/MutateAccessChecker`, make at least 10 single-point mutants, and run `--selftest` plus the live check against the copied corpus at base for each. This report gives the mutants, the detector, the observed outputs, the verdicts, the restoration evidence, and the controls that would kill the survivors.

The lane was never edited. The sandbox copy was built from the base commit blob; `git status --porcelain -- tools/` in the lane is empty.

## Sandbox setup (read-only w.r.t. the lane)

```
LANE=/home/vgpnk/Projects/shokunin/kotodama-shokunin
SB=/fast/scratch/hyaku/kotodama-r52/MutateAccessChecker
git -C $LANE archive 147cfde85eb13256438c1ed04d92e8d2ad09b76e corpus | tar -x -C $SB
git -C $LANE show 147cfde85eb13256438c1ed04d92e8d2ad09b76e:tools/check-source-access.py > $SB/tools/check-source-access.py
cp $SB/tools/check-source-access.py $SB/pristine.py
```

- Pristine sha256 (target file and `pristine.py`): `e6ff0c445a1c326641d156aa954f8e11193c6e36f81f541b8f000d0649b2fedf`
- `diff` of `pristine.py` against the base blob: identical.
- Copied corpus: `corpus/SOURCES.md` (rows S001–S133) and 227 `.md` files under `corpus/knowledge` (`find corpus/knowledge -name '*.md' | wc -l` = 227 at base), 0 non-`.md` files.
- Base `S094` status cell: `rejected` (`corpus/SOURCES.md:123`); base `S094` knowledge cites: 5, all in `corpus/knowledge/linguistics/sign-languages-manual-modality.md` (lines 83, 87, 90, 92, 93).

Harnesses written in the sandbox only: `harness.py` (mutants), `control_harness.py` (controls), `results.txt` (raw run log).

## Baseline (pristine bytes, both detectors)

Live check (`python3 -B tools/check-source-access.py --root $SB`), exit 1:

```
ACCESS_FINDING cited S094 corpus/knowledge/linguistics/sign-languages-manual-modality.md:83
ACCESS_FINDING cited S094 corpus/knowledge/linguistics/sign-languages-manual-modality.md:87
ACCESS_FINDING cited S094 corpus/knowledge/linguistics/sign-languages-manual-modality.md:90
ACCESS_FINDING cited S094 corpus/knowledge/linguistics/sign-languages-manual-modality.md:92
ACCESS_FINDING cited S094 corpus/knowledge/linguistics/sign-languages-manual-modality.md:93
ACCESS: 2 flagged rows, 5 findings
```

This matches the expected base value (5 cited findings). Two rows are flagged by the bypass regex: S094 (`corpus/SOURCES.md:123`, whose source cell says "Cloudflare-gated, opened via headless browser") and S132 (`corpus/SOURCES.md:161`, whose teaches cell describes the S094 bypass). S132 is `rejected` and cited nowhere in `corpus/knowledge`, so it contributes no finding.

Selftest (`--selftest`), exit 0: `SELFTEST: 10/10 pass` (9 named cases plus the malformed-row case; the malformed case prints `ACCESS_INPUT_ERROR row S001 at line 3 has 3 cells, not 11` on stderr, which is expected output of the case, not a failure).

Baseline is green on both channels, so every mutant result below is attributable to the mutation.

### Detector definition

- **D1 (selftest):** `--selftest` must exit 0, print `10/10 pass`, and print no `FAIL` line.
- **D2 (live):** the live check must exit 1 and print byte-identical stdout to the baseline above (5 cited findings, `2 flagged rows, 5 findings`).

A mutant is **killed** if D1 or D2 fails. **Survived** means both still pass.

## Mutants (17, all single-point)

Each mutant replaces exactly one occurrence of one string in the pristine file (harness asserts `count == 1`; 0 apply errors).

| id | single-point edit | verdict | killed by | live output (tail) |
|---|---|---|---|---|
| M01 | drop the status leg (the `row["status"] != "rejected"` finding block) | KILLED | D1 | baseline (5 findings) |
| M02 | drop the cited leg (`if ids:` → `if False:`) | KILLED | D1, D2 | `ACCESS: 2 flagged rows, 0 findings` |
| M03 | weaken BYPASS alternative 1 (`\bheadless\b` removed) | KILLED | D1, D2 | `ACCESS: 0 flagged rows, 0 findings` |
| M04 | weaken BYPASS alternative 2 (`\bbypass(?:ed|ing)?\b` removed) | KILLED | D1 | baseline (5 findings) |
| M05 | weaken BYPASS alternative 3 (`\bsolved (?:a \|the )?(?:bot )?(?:captcha\|challenge)\b` removed) | KILLED | D1 | baseline (5 findings) |
| M06 | flip the rejected comparison (`!= "rejected"` → `== "rejected"`) | KILLED | D1, D2 | `ACCESS_FINDING status S094 rejected` + `status S132 rejected` + 5 cited → 7 findings |
| M07 | break the cite regex trailing word boundary (`\b")` → `")`) | KILLED | D1 | baseline (5 findings) |
| M08 | remove the `.md` extension filter (scan every file) | **SURVIVED** | — | baseline (5 findings) |
| M09 | invert the `.md` extension filter (`not name.endswith(".md")` → `name.endswith(".md")`) | KILLED | D1, D2 | `ACCESS: 2 flagged rows, 0 findings` |
| M10 | return 0 on findings (`return 1 if findings else 0` → `return 0` in `run`) | KILLED | D2 | baseline text, but exit code 0 |
| M11 | narrow bypass scope to the source cell only (drop `anchor` and `teaches`) | KILLED | D1, D2 | `ACCESS: 1 flagged rows, 5 findings` (S132 no longer flagged) |
| M12 | take the cite id set from all rows, not only flagged rows | KILLED | D1, D2 | hundreds of spurious `ACCESS_FINDING cited S031…` |
| M13 | non-recursive knowledge walk (top level only) | KILLED | D1, D2 | `ACCESS: 2 flagged rows, 0 findings` |
| M14 | only the first sid per line is reported | **SURVIVED** | — | baseline (5 findings) |
| M15 | drop the empty-registry guard (`if not rows: raise ValueError`) | **SURVIVED** | — | baseline (5 findings) |
| M16 | break the cite regex leading word boundary (`r"\b("` → `r"("`) | **SURVIVED** | — | baseline (5 findings) |
| M17 | bypass regex loses `re.IGNORECASE` | **SURVIVED** | — | baseline (5 findings) |

Result: **12 killed, 5 survived, 0 apply errors.**

### Notable kill detail

- M04 and M05 are killed only by the selftest, not by the live check. The live corpus has no `bypass`-worded or `solved a captcha`-worded row, so removing those two alternatives leaves the live output unchanged; the selftest cases `bypass-in-anchor` and `captcha-in-teaches` are what hold them. This is the argument for keeping both detector channels rather than relying on the live run alone.
- M10 (`return 0 on findings`) is killed only by D2. The selftest computes its own exit expectation from the findings list and never calls `run()`, so the exit-code contract of the live tool is covered only by the live run. The selftest's `malformed-row` case is the only case that exercises `run()`.
- M06 shows the status leg is live on this corpus: flipping the comparison turns both flagged rows into status findings, giving 7 findings instead of 5.

## Restoration evidence

The harness writes the mutant to `tools/check-source-access.py`, runs both detectors, then copies `pristine.py` back over the target and re-hashes.

- After every one of the 17 mutants, `restore_ok = True`; the restored sha256 equals the pristine sha256 `e6ff0c4…b2fedf`.
- Final state of `tools/check-source-access.py` in the sandbox: sha256 `e6ff0c445a1c326641d156aa954f8e11193c6e36f81f541b8f000d0649b2fedf` = pristine.
- The lane copy was never written: `git -C $LANE status --porcelain -- tools/` is empty; the only lane worktree changes are the claim-D entry edit and the round-52 scratch files produced by other seats, none of them mine.

Per-mutant sha256 values (mutant file → restored file) are in `results.txt` in the sandbox; every restored value is `e6ff0c4…b2fedf`.

## Controls that would kill the survivors

Five extra selftest controls were injected into a controlled copy (`controlled.py`) and each survivor was re-applied on top of it. The controlled pristine passes all 14 cases plus the malformed-row case; each survivor is killed by exactly one control.

| survivor | proposed control | observed |
|---|---|---|
| M08 (no `.md` filter) | `control-non-md-ignored`: a `.txt` file in `corpus/knowledge/p/` carrying `(S001)` where S001 is a flagged rejected row; expect 0 findings | `FAIL control-non-md-ignored findings=1 want=0` → killed |
| M14 (first sid per line only) | `control-two-ids-one-line`: two flagged rejected rows S001 and S002, knowledge line `x (S001) (S002)`; expect 2 findings | `FAIL control-two-ids-one-line findings=1 want=2` → killed |
| M15 (no empty-registry guard) | `control-empty-registry-raises`: a `SOURCES.md` with only the header; expect `ValueError` (exit 2 `ACCESS_INPUT_ERROR`) | `FAIL control-empty-registry-raises raised=False` → killed |
| M16 (no leading `\b` in cite regex) | `control-glued-id-not-an-id`: knowledge line `xS001`; expect 0 findings (a glued id is not an id) | `FAIL control-glued-id-not-an-id findings=1 want=0` → killed |
| M17 (bypass regex case-sensitive) | `control-capitalised-bypass`: source cell `(Headless browser)`; expect 1 finding | `FAIL control-capitalised-bypass findings=0 want=1` → killed |

All five controls are ordinary additions to the existing `selftest()` case list; each writes a temporary registry and knowledge file, in the same style as the current cases. The control harness's own restore path was verified the same way as the mutants.

These are coverage findings about the current control set, not licence to change the tool's contract. The five survivors show the shipped `--selftest` does not yet hold: non-`.md` files, two flagged ids on one line, an empty registry, a glued id, and a capitalised bypass marker.

## Claim D bytes (attack)

The landed claim D commit `dea5ece` ("sign-language entry re-cited off S094 (S096, S097 re-opened by ordinary means); S094 lines 5 -> 0") was checked in a second sandbox (`.../MutateAccessChecker/D-landed`, corpus from `git archive dea5ece`):

```
$ python3 -B tools/check-source-access.py --root $SB2
ACCESS: 2 flagged rows, 0 findings
exit=0
$ python3 -B tools/check-source-access.py --selftest | tail -1
SELFTEST: 10/10 pass
```

The live check at the landed D bytes is clean: exit 0, zero findings, while both bypass-marked rows (S094, S132) remain flagged and rejected. The five S094 citations are gone from `corpus/knowledge/linguistics/sign-languages-manual-modality.md` (base lines 83, 87, 90, 92, 93 → 0), so the cited leg no longer fires. The same clean result holds on the current lane working copy (`git status` shows the entry still modified by other seats in flight). No live violation was found in D's landed bytes; the claim-D critique on this axis is not supported by the checker.

## One real weakness found (false positive, not a mutation)

The bypass regex searches `source + anchor + teaches`. A row that merely *describes* an earlier row's bypass in its `teaches` cell is flagged as a bypass row itself. Probe: a registry row whose teaches reads "supersedes S094 — REJECTED: S094 was opened by getting past a bot challenge with a headless browser" and whose status is `mined` produces `ACCESS_FINDING status S900 mined`, exit 1 — although that row was opened by ordinary means and merely narrates a prior row's history.

This shape already exists in the registry at `corpus/SOURCES.md:161` (S132 narrates S094's bypass). It is harmless today only because S132's own status is `rejected` and it is cited nowhere. A future row of the same shape that is legitimately `mined`, or that a knowledge entry cites, would be reported as a violation. That is a coverage gap in the bypass matcher, not a claim-D defect: it is authored-lane advice for the next round, and it is not the job of this seat to change the tool's contract.

## Unrun checks

- The checker was not run against the round-52 claim C bytes, because no C entry exists yet at the time of this probe (base corpus: 227 knowledge `.md` files). When C lands, the same live check should be re-run against the corpus with the new entry, and the new S134+ rows should be read to confirm none of them narrates a bypass marker in a `teaches` cell in the S132 shape.
- No check was run against the corpus of a future round or against other tools in `tools/`; the assignment scoped this seat to `tools/check-source-access.py`.
- The mutation harness was run under Python 3.14.8 (stdlib only). No other interpreter version was tried.

## Tooling

No packages installed, no versions changed, no host services touched. The seat used `git archive` / `git show` (read-only) from the lane's colocated git, `python3 -B` (system 3.14.8), and `coreutils`. Nothing was installed, so there is no install record to report.

## Files written

- Sandbox only: `/fast/scratch/hyaku/kotodama-r52/MutateAccessChecker/{pristine.py,controlled.py,harness.py,control_harness.py,results.txt}` and the copied `corpus/` and `tools/check-source-access.py`; plus the second sandbox `D-landed/`.
- This report: `.ufo/waves/round-52/build/MutateAccessChecker.md`.
