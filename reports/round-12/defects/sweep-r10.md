# Round-10 conformance defect sweep — R12-O05..O06

- Audit date: 2026-10-17.
- Scope: round-10 declaration, acceptance artifacts, findings queue, report draft, and the round-10 `SHONEN`/LOG claims. Review criteria are from `reports/round-10/targets.json` and `SHONEN.md`.
- Mode: read-only audit. No round-8..11 artifact was edited, and the round-10 validation runner was not executed because it rewrites its filed `reports/round-10/validation.json` output.

## Findings

### F-01 — LOG records the declaration commit as the baseline (medium)

`LOG.md:2989-2990` labels `eb348f3` as the round-10 baseline. The declared baseline in `reports/round-10/claims.json:5` is `9dc18ec1339bffd6f81e74f1a5742464ef578749`; `reports/round-10/report-draft.md:12-14` correctly distinguishes that baseline from declaration commit `eb348f3ed4dfa5258be3fba15be0618a1667b962`. Reproduce (2026-10-17): read `claims.json`'s `baseline_revision`, then run `git show -s --format='%H %s' 9dc18ec1339bffd6f81e74f1a5742464ef578749` and `git show -s --format='%H %s' eb348f3`.

**Disposition:** factual metadata mismatch; preserve the filed log and have the integrator record a correction as a new entry. Owner: round-14 integrator.

### F-02 — Coverage runner misclassifies the second index-updater report as authorship (low)

The target assigns both R10-C21 and R10-C22 to index updating (`reports/round-10/targets.json:15-17`), and the second report is `coverage/index-update-22.md`. The runner excludes only the exact filename `index-update.md` from authorship (`reports/round-10/run-validation.py:495-499`), so it counts the mandated backup updater as an author. Reproduce (2026-10-17): list `coverage/C[0-9][0-9].md` and `coverage/index-update*.md`, then read `claims.C.measurement.fragments` from `reports/round-10/validation.json`. The command output was 10 author files (`C01.md`–`C10.md`), two index-updater files, but the receipt reports `authorship: 11` and `index_update: true`.

This is a measurement/classification defect, not a failed threshold: the ten actual author fragments meet the declared minimum without counting `index-update-22.md`. C22 independently documented the same issue at `reports/round-10/coverage/index-update-22.md:224-244`.

**Disposition:** route a bounded runner-classification correction and an isolated recheck to round 14. Do not alter the filed runner in this sweep.

### F-03 — Round-8 runner is reverted, but round-10 ledger still calls it stale-fixed (medium)

The round-10 ledger has two `stale-fixed` rows for `python3 reports/round-8/run-validation.py`, with `fix-20.md` as evidence (`reports/round-10/drift/ledger.json:1027-1034` and `:1190-1197`); another row for the same command says `stale-documented` while its note still says the runner was repaired (`:1569-1575`). `LOG.md:3003-3006` says the integrator reverted the runner change and documented staleness instead.

Current-state check (2026-10-17): `sha256sum reports/round-8/run-validation.py` and `git show 94ca098b8ab03be52ec80f6925538e5e2c0ed327:reports/round-8/run-validation.py | sha256sum` both returned `7eaa36789b4d71ce94ffadc93d2f5e10d6e0ca353df1c233d0ba94f29bff8369`; `python3 -c 'from pathlib import Path; print("gate_blob_for_pin" in Path("reports/round-8/run-validation.py").read_text())'` returned `False`. `fix-20.md:47-49` instead records the patched runner digest as `d78da29f…` after the fix.

The round-10 validator's own limits say cited commands are checked for ledger presence, not re-executed (`reports/round-10/validation.json` limits; `run-validation.py` F coverage logic). Therefore the stored F pass does not resolve the conflict between the stale-fixed entries and the final reverted file.

**Disposition:** reconcile the duplicate ledger entries and preserve the final status as documented-stale unless a later permitted artifact proves a retained fix. Keep the receipt and runner bytes unchanged. Owner: round-14 integrator.

### F-04 — Tracker final-state verifier list omits an existing verdict (low)

`reports/round-10/findings-tracker.json:381-385` lists `findings-verify-1.md`, `findings-verify-2.md`, and `findings-verify-4.md`, omitting `findings-verify-3.md`. The omitted report exists; the scribe says all four verifier files are present (`findings-scribe.md:17-21,59-68`), and the validation receipt's O measurement also lists verifier 3 (`validation.json:698-703`). Reproduce (2026-10-17): `python3` loading `tracker['final_state']['verify_files']` and globbing `reports/round-10/findings-verify-*.md` returns three listed names versus four files.

**Disposition:** summary-field transcription defect; correct only through a new correction record, not by rewriting the filed tracker. Owner: round-14 integrator.

### F-05 — In-lane report remains an unfinalized SHONEN draft; its count is inconsistent (medium / needs confirmation)

The only in-lane report candidate is explicitly headed “DRAFT BODY — orchestrator finalizes” and says it is not an admission (`reports/round-10/report-draft.md:1-9`). It names `.ufo/reports/round-10/kotodama.md` as the final destination, but that path is absent inside this lane repository; I did not inspect outside the assigned repo. Its `## SHONEN skeleton` is present, but all four markers are `[~]` and none is `[x]`; under `SHONEN.md:10-11`, asserted markers need evidence pointers and verified markers need a named non-author verifier. Reproduce (2026-10-17): a read-only Python check of the heading and checkbox lines returns `shonen_heading_present=True`, `markers_total=4`, `asserted=4`, `verified=0`, and `local_ufo_final_report_present=False`.

The draft's SHONEN bullet says “8 new entries” (`report-draft.md:240-241`), while the same draft's coverage section says 10 (`:34-42`) and the stored final receipt says `claims.C.measurement.new_entries = 10`. Reproduce the receipt value (2026-10-17) by reading that JSON field; it is also consistent with `python3 reports/round-10/run-validation.py` as cited in the final admission record. The report's `[~]` section and open-items list are explicitly an earlier floor snapshot, but no finalized in-lane report resolves the conflicting count or records the final marker evidence.

**Disposition:** to-verify whether the named external final report was filed; within the allowed scope, the in-lane record remains provisional. Require the integrator to attach/point to the final SHONEN evidence and reconcile the 8-vs-10 statement in a new record. No external path was accessed.

### F-06 — Draft runner hash is not resolvable to a retained runner version (low)

The draft cites runner hash prefix `4529ac3d…` at `report-draft.md:102,127-130`. The current runner is `23d6dc09002fe18c46778ac57d2c34246ab970a9371e7382950ca737d4019b0e` (2026-10-17, `sha256sum reports/round-10/run-validation.py`), which is the `runner_sha256` in the final `validation.json`. The report contains only the truncated earlier prefix, and no version with that prefix appears in the committed history for this path. Reproduce (2026-10-17): scan `git log --all -- reports/round-10/run-validation.py`, hash each `git show <commit>:reports/round-10/run-validation.py` blob, and compare the prefix; the scan returned no match.

**Disposition:** this appears to be a transient pre-finalization runner snapshot, not evidence that the final runner hash is wrong. Preserve the historical observation but bind the finalized report to a retained full digest or mark the old digest `to-verify`. Owner: round-14 integrator.

## Hash-mismatch disposition (not a defect)

The stored round-10 receipt reports acceptance and claims C/F/O passing. On 2026-10-17, a read-only audit of its `input_sha256` map against current files found 74 of 76 paths matching and two mismatches. These are later legitimate changes, not silent corrections: the recorded `SCORECARD.md` digest `cc032db8…` resolves at baseline commit `9dc18ec`; its current digest `f735edf4…` resolves at round-11 commit `a3f6fcef`. The recorded `coverage/index-update-22.md` digest `1b30ea92…` resolves at round-10 admission commit `94ca098`; its current digest `2c33853f…` resolves at round-11 commit `a3f6fcef`. Reproduce (2026-10-17): hash all `validation.json.input_sha256` paths, then scan `git log --all` blobs for each recorded digest. Cause: subsequent round-11 edits/addendum. The round-10 receipt remains a historical input snapshot; do not rewrite it.

## Overall disposition

The current stored validation receipt is acceptance-true, with C/F/O all passing (read-only JSON extraction, 2026-10-17). That does not clear the transcription, misclassification, ledger-state, and report-finalization findings above. No round-10 runner was executed and no round-8..11 artifact was changed in this sweep.
