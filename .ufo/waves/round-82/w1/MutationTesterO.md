# MutationTesterO — round-82 (hyaku 15) scoped findings

Seat `MutationTesterO` (leaf). Verdict up front: **counter mutation score 1/5 killed; the QUEUE leg does catch a tool-contract `NNd` predicate mutation against the real registry; four honest coverage gaps found.** No blockers. No installs (no tools added/upgraded this seat).

## What was probed

Target instrument: `reports/round-82/accept-o82.py` (claim O counter), sha256 `77b8c19d61cdcae5a9d10fc2e089d772455014bb210a90577b72b1c10d313030` — recorded before any run, re-verified after (`stage/MutationTesterO/hashes.txt`); the lane file was read-only for this seat throughout.

1) Five single-predicate mutants of the counter in scratch, each run under the counter's own bounded detector `--selftest` (pristine baseline: `SELFTEST-O82: PASS (12 checks)`, rc=0):

- M1 due-boundary `<=`→`<` (tally L125) — SURVIVED; verdict `SELFTEST-O82: PASS (12 checks)`, rc=0 — no check (`selftest-m1.log`).
- M2 window-boundary `<=`→`<` (tally L127) — SURVIVED; `SELFTEST-O82: PASS (12 checks)`, rc=0 (`selftest-m2.log`).
- M3 on-release counted as due (`exempt += 1`→`due += 1`, tally L124) — KILLED by 3 checks: `clean fixture PASS`, `QUEUE compares against the counter's own parse`, `MODULAR passes on a population-neutral append`; `SELFTEST-O82: FAIL (12 checks)`, rc=1; killing line `LEG FAIL QUEUE (2026-11-04: tool (0, 1, 1, 3) != counter (1, 1, 0, 3); ...)` (`selftest-m3.log`).
- M4 `SUMMARY` rows-field made optional (L43) — SURVIVED; `SELFTEST-O82: PASS (12 checks)`, rc=0 (`selftest-m4.log`).
- M5 MODULAR neutral-row expectation trivially true (`ok1 = True`, L333) — SURVIVED; `SELFTEST-O82: PASS (12 checks)`, rc=0 (`selftest-m5.log`).

2) Tool-contract mutation: contract-exact scratch stub with one predicate defect (`NNd` → `opened + N*30 days`), self-consistent `--selftest` (8 checks, `SELFTEST: PASS (8 checks)`), graded by the pristine counter in a scratch fixture holding the REAL registry blob from base `c285b2af` (991457 B — `git -C lane show c285b2afb19d4b64320e18df1f55e426bf2d0b0c:corpus/SOURCES.md | wc -c`) plus the real claims.json (fixture `base` re-pointed to the fixture's own commit). Result — mutated stub: `LEG FAIL QUEUE (2026-11-04: tool (0, 0, 14, 827) != counter (0, 18, 14, 827); 2027-11-01: tool (154, 0, 14, 827) != counter (813, 0, 14, 827))`, `ACCEPT-O-82: FAIL legs=5/7`, rc=1; control stub: `ACCEPT-O-82: PASS legs=7/7`, rc=0. Counter's own tally of the real blob: `(0, 18, 14, 827, 0)` / `(813, 0, 14, 827, 0)` — matches claims.json "after". The QUEUE leg's independent parse is the check that fires; MODULAR also failed but only collaterally via its frozen baseline (its `365d` neutral probe is invisible to an NNd-scaling defect).

## Honest gaps (predicates no selftest check covers)

1. `due_date <= as_of` vs `<` — no fixture row due exactly on a graded as-of (M1).
2. `due_date <= as_of + window` vs `<` — no fixture row at exactly `as_of + window` (M2).
3. MODULAR neutral-row expectation — no negative probe; trivialized `ok1` passes all 12 checks (M5).
4. `SUMMARY` strictness on the `/ N rows` contract field — no deviant-output probe; a rows-less summary would TypeError-crash the counter mid-grade rather than fail the leg cleanly (M4).

Closure is fixture-only (add boundary rows at both dates + `as_of+window`, one rows-less junk summary, one MODULAR-negative append); no leg logic needs to change.

Postscript (freeze-time delta, after my runs): the lane counter was upgraded by the L1 at 2026-11-04 08:40:10 (`77b8c19d…`/25355 B → `3b339c50…`/30105 B; diff captured in transcript vs `stage/MutationTesterO/m1.py`). The frozen counter adds `due_ids`, an exactly-one-summary + DUE-set equality check in QUEUE, an NNd boundary probe in MODULAR, and junk5/junk6 — closing gaps 1, 2 and 4 (M1/M2/M4 classes) and, by inference, catching the NNd×30 stub class in MODULAR too; gap 3 (M5, trivially-true neutral MODULAR expectation) remains open, and the rows-less-summary `int(None)` crash remains latent. These closures are [INFERENCE] from the diff — per the L1 wrap-up order no mutants were re-run against the frozen bytes. Measured score against the graded bytes: 1/5.

## Evidence & files (absolute paths)

All under `/home/vgpnk/Projects/shokunin/kotodama-shokunin/`:
- Report: `.ufo/waves/round-82/w1/MutationTesterO.md` (this file)
- `.ufo/waves/round-82/w1/stage/MutationTesterO/mutation.md` — full analysis with pasted verdicts
- `.../stage/MutationTesterO/m1.py` … `m5.py` — the five counter mutants (sha256 in `hashes.txt`)
- `.../stage/MutationTesterO/tool-stub-mutated.py`, `tool-stub-control.py` — contract stubs
- `.../stage/MutationTesterO/selftest-m1.log` … `selftest-m5.log` — detector runs with rc
- `.../stage/MutationTesterO/queue-probe.log` — fixture-driver transcript (both counter runs + tallies + stub summaries)
- `.../stage/MutationTesterO/mutant-diffs.txt` — one-line-diff proof per mutant
- `.../stage/MutationTesterO/hashes.txt` — lane file before/after hash, artifact hashes, verdict lines

Producing commands (all run with cwd/artifacts under `/fast/scratch/hyaku/kotodama-r82/MutationTesterO`, TMPDIR set there, removed after capture; fixture repos created with `mktemp -d -p .../fx` and `git -C <fx> rev-parse --show-toplevel` asserted pre-commit):

- Baseline/mutants: `python3 -B <file> --selftest --work <wd>` (one per mutant; logs above).
- QUEUE probe: `python3 -B fixture_driver.py` (transcript in `queue-probe.log`).

Negative-claim sweep: the four survivors were checked against EVERY one of the 12 selftest checks — all 12 print `SELFTEST ok` in each survivor's log (not a subset); the "no check covers it" claim carries its full sweep. Coordination: ExecEvidence's finding about a fixture bug inside an executor's draft tool selftest is out of this seat's scope (counter + contract only) and was routed back to the authoring executor.
