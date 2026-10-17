# Round 12 O17–O18 — findings routed to round 14

- **Axis:** O / operability.
- **Prepared:** 2026-10-17, from the R12 round-8 through round-11 defect sweeps and available bounded-fix receipts.
- **Scope:** This file is the routing record only. No round-8–11 artifact was edited. Every owner below is a round-14 role; the round-14 dispatcher must name the seat before work starts.
- **Queue snapshot:** `date -u +%Y-%m-%dT%H:%M:%SZ; ls reports/round-12/defects` ran at `2026-10-17T23:07:07Z`. It showed `fix-09.md`, `fix-10.md`, `regression.md`, and `sweep-r8.md` through `sweep-r11.md`; no other O09–O16 fix receipt was present in that snapshot. Findings without an explicit later bounded-fix disposition remain routed below.

## Open items — round 14

### R8-SWEEP-01 / R11-X02 Finding A — filed validation outputs changed by live rechecks

**Status:** resolved-by-fix (fix-11 append-only correction; round-14 confirms application). The round-8 receipt showed acceptance true at the round-8 work commit and a later-tree false result; the R8 sweep attributes the only post-close change to the round-11 commit. The R11 adjacency receipt records that live rechecks invoked validators which write their own `OUTPUT_REL`, changing filed round-5–9 validation receipts. A receipt can therefore report stable command output while the filed artifact changes.

**Round-14 owner:** acceptance-runner/recheck protocol owner, with the round-14 integrator responsible for receipt preservation. Use a full-tree mirror or redirect every writer's output to disposable storage; compare filed-path hashes before/after the run. Keep historical reports immutable and place any interpretation or correction in a new round-14 record.

**Evidence:** `reports/round-12/defects/sweep-r8.md` §“Finding” compares the round-8 work-commit JSON to HEAD; its dated commands are the Python `json.loads(git show …)` comparison and `git log`/`git diff --quiet` checks (2026-10-17). `reports/round-11/adjacency.md` §§1.3–1.4 records the live-root recheck mechanism, row-147 timestamp/hash control, and the six earlier-round validation paths plus a separate filed-fragment append (observations dated 2026-10-17); `reports/round-11/recheck/row-131.json` identifies `python3 reports/round-8/run-validation.py` as writing its filed output. Do not restore or regenerate those earlier-round paths as part of this routing task.

### R9-X03 §4.2 — worker output landed in the parent tree

**Status:** Historical out-of-lane write confirmed; no procedural prevention control is evidenced. R9's adjacency report records a Kotodama-attributed V09 fragment written under the fleet parent rather than the lane. R10's later scope check found no outside-lane path in its own window; that does not erase the R9 breach or demonstrate a dispatch-time guard. The unrelated PDF noted in R9 §4.3 is explicitly unattributed and is not included as a Kotodama finding.

**Round-14 owner:** operator/dispatch owner. Add a preflight that binds each worker's working directory and permitted output root to the lane, and fail closed on an out-of-root destination. Verify the control with an isolated planted out-of-root path; do not move, delete, or otherwise modify the historical parent-tree artifact under this assignment.

**Evidence:** `reports/round-9/adjacency.md` §4.2 records `stat` of the parent-tree file at 17:59:41 and the in-lane `ls`/`grep` absence check at 17:59 on 2026-10-17; §4.4 records the dated parent-tree sweep. See also the same report's verdict row and the R10 adjacency scope check. Attribution and limitations are preserved there.

### R9-SWEEP-01 — baseline locations do not conform to the declared standard

**Status:** resolved-by-fix (fix-09 append-only correction; round-14 applies it). The two baselines in `reports/round-9/baselines/` are not under the round-phase path specified by `gate-frozen-run-standard.md`; the default battery leaves those gates uncovered, while adding that reports directory as a custom root passes. The filed round-9 runner reports, rather than fails, this gap, and the admitted O wording does not carry the qualification.

**Round-14 owner:** gate-battery/integration owner. Decide and document whether the layout is an authorized exception or the baseline/runner/claim needs a new conforming design. Keep old receipts and baselines unchanged; require the default-root check and the declared claim wording to agree before asserting standard-complete coverage.

**Evidence:** `reports/round-12/defects/sweep-r9.md` Finding O-R9-01 ran `python3 tools/check-gate-battery.py` and then the same battery with `--baselines-root tools/gates/frozen`, `tools/gates/expected`, and `reports/round-9/baselines` (2026-10-17); the default-root run exited 2 and the custom-root run exited 0. The sweep also cites `reports/round-9/validation.json` and `reports/round-9/baselines/registry.md` for the filed readings.

### R10-SWEEP F-01 (RESOLVED by fix-11; round-14 confirms) — LOG baseline label disagrees with the declared baseline

**Status:** Resolved by fix-11 (bounded append-only correction distinguishing the declared baseline from the declaration commit; control evidence in fix-11). Round-14 confirms application.

**Round-14 owner:** report/LOG integrator. Add a correction as a new round-14 record and ensure future closeout metadata distinguishes the baseline revision from the declaration revision. Do not rewrite the filed LOG entry.

**Evidence:** `reports/round-12/defects/sweep-r10.md` F-01 (RESOLVED by fix-11; round-14 confirms) compares `claims.json` to `git show -s --format='%H %s'` for both cited commits (2026-10-17); the round-10 report draft has the corresponding distinction.

### R10-SWEEP F-02 — coverage runner counts an index updater as an author

**Status:** Open runner-classification defect; no correction receipt is present in the queue snapshot. The current round-10 runner excludes only the exact `index-update.md` name, so the separately assigned `index-update-22.md` is counted in the author total.

**Round-14 owner:** acceptance-runner maintainer. Correct the classification in a new runner or successor harness and add a controlled regression proving index-updater fragments cannot inflate author counts. Leave the filed round-10 runner and validation receipt untouched.

**Evidence:** `reports/round-12/defects/sweep-r10.md` F-02 reproduces the discrepancy by listing `coverage/C[0-9][0-9].md` and `coverage/index-update*.md`, then reading `claims.C.measurement.fragments` from the receipt (2026-10-17); it also cites `reports/round-10/run-validation.py:495-499` and the C22 note in `coverage/index-update-22.md`.

### R10-SWEEP F-03 — stale-fixed ledger status conflicts with the reverted runner

**Status:** Open ledger-consistency defect. The round-10 drift ledger retains stale-fixed dispositions for the round-8 runner despite the integrator's reversion; a related row says stale-documented while its note still describes a repair. The final live runner does not contain the claimed fix, and the validator does not re-execute those commands to resolve the inconsistency.

**Round-14 owner:** drift-ledger integrator. Reconcile the conflicting entries against the retained runner bytes; if no retained fix exists, record documented-stale consistently in a new correction record. Preserve the filed round-10 ledger, receipt, and runner.

**Evidence:** `reports/round-12/defects/sweep-r10.md` F-03 compares `sha256sum reports/round-8/run-validation.py` with `git show 94ca098…:reports/round-8/run-validation.py | sha256sum` and checks for `gate_blob_for_pin` (2026-10-17); it cites the ledger rows and `LOG.md` reversion entry.

### R10-SWEEP F-04 (RESOLVED by fix-09 append-only correction; round-14 applies it) — tracker omits an existing verifier pointer

**Status:** Resolved by fix-09 (bounded append-only correction adding the missing verifier pointer; control evidence in fix-09 with normalized comparison + unchanged tracker hash). Round-14 applies it.

**Round-14 owner:** findings-tracker/report integrator. Carry the payload in the next permitted summary or a new correction record; do not back-patch `reports/round-10/findings-tracker.json`.

**Evidence:** `fix-09.md` records the normalized before-control command at 2026-10-17T19:57:12-03:00 and the after-control command at 2026-10-17T20:00:55-03:00. The latter checks that the correction covers the live file set while the filed tracker hash is unchanged.

### R10-SWEEP F-05 — no finalized in-lane report; SHONEN evidence/count remains provisional

**Status:** Open / external filing to verify. The in-lane candidate labels itself a draft and an orchestrator responsibility; the round-10 sweep did not inspect the named `.ufo` destination because it is outside the lane-only audit scope. The draft's SHONEN entry-count statement conflicts with its own coverage section and the validation receipt.

**Round-14 owner:** report scribe/integrator. Verify the final filing through the authorized owner, or produce a permitted new integration record; reconcile the entry-count statement against its receipt and attach the required SHONEN evidence. Preserve the draft and do not claim the external filing is absent without checking it through an authorized route.

**Evidence:** `reports/round-12/defects/sweep-r10.md` F-05 records a dated read-only check of the in-lane heading/markers and receipt field (2026-10-17) and explicitly limits the external-path conclusion. The cited sources are `reports/round-10/report-draft.md`, `reports/round-10/validation.json`, and `SHONEN.md`.

### R11-SWEEP-01 — rejected round has no finalized report/SHONEN section in the lane

**Status:** Open documentation integration item. The round-11 report artifact remains an explicitly labeled draft with a SHONEN skeleton, while LOG/SCORECARD and the validation receipt consistently record **REJECTED**. Finalization must keep that rejection and the supporting evidence; it must not convert the draft into an admission.

**Round-14 owner:** report scribe/integrator. Produce or point to the authorized final report, preserve the rejected verdict, and retain the named evidence and marker/verifier rules. Do not rewrite the filed round-11 draft.

**Evidence:** `reports/round-12/defects/sweep-r11.md` R11-SWEEP-01 checks the lane-local report inventory and compares `report-draft.md`, `SHONEN.md`, LOG, SCORECARD, and validation receipt (2026-10-17).

### R11-SWEEP-02 — draft F census is an in-flight snapshot, not the settled result

**Status:** Open report-reconciliation item; the rejection itself is valid. The draft's stamped census disagrees with the settled `recheck/summary.json` and validation measurement. The old draft value must remain identifiable as a historical snapshot; the final report should use the settled receipt and retain the below-threshold rejection.

**Round-14 owner:** freshness/report integrator. Add the corrected settled reading in a new integration record and identify the exact denominator/measurement channel. Never silently edit the filed draft or receipt.

**Evidence:** `reports/round-12/defects/sweep-r11.md` R11-SWEEP-02 gives the independent recount command `python3 -c 'import json,pathlib; ps=list(pathlib.Path("reports/round-11/recheck").glob("row-*.json")); rs=[json.loads(p.read_text()) for p in ps]; print(len(rs), sum(r.get("stable") is True for r in rs), sum(r.get("stable") is False for r in rs), sum(r.get("new_hash") is None for r in rs))'` (2026-10-17), and compares its output with `reports/round-11/recheck/summary.json` and `reports/round-11/validation.json`.

### R11-X02 Finding B — a filed round-10 fragment was appended after filing

**Status:** Pending current-state verification; the last round-11 adjacency record marked the post-filing append open. The fragment is an earlier-round filed artifact, so any useful addendum must live in a new record. No R12 fix receipt for this item appeared in the pre-write queue snapshot.

**Round-14 owner:** artifact-integrity/integration owner. Read-only compare the current path with the filed commit; record the disposition in a new round-14 note and add a prevention control for post-filing writes. Do not edit `reports/round-10/coverage/index-update-22.md` under this task.

**Evidence:** `reports/round-11/adjacency.md` §1.4 records the dated `git diff` and live-vs-HEAD hashes for `coverage/index-update-22.md` (2026-10-17); the round-11 report draft also lists it among the post-filing mutations.

### R11 availability trace — dispatch evidence absent from the round-11 report snapshot

**Status:** Open evidence gap, not an inference about worker quality. The round-11 report draft explicitly says no round-11 availability-attempt record existed at its refresh. Round-10's failed launch attempts are recorded in their own files, but that does not provide a round-11 dispatch trace.

**Round-14 owner:** dispatcher/operator. For each round-14 launch, retain a contemporaneous attempt record that binds requested model/worker count to actual route, launch/completion state, failure response, and authorized fallback. If a round has no attempt, state that explicitly in its report. Do not infer execution from the requested model alone.

**Evidence:** `reports/round-11/report-draft.md` lines 20–25 records the absence and points to `reports/round-10/availability-attempt-{1,2,3}.json`; both the report draft and attempt files are dated 2026-10-17.

## Findings not routed as open

- **R10-SWEEP F-06 — closed with control.** R12-O10's `reports/round-12/defects/fix-10.md` explicitly dispositions the current runner-digest pointer as `fixed-with-control` using an append-only correction; its before/after commands compare the current runner digest to the filed receipt and search retained runner blobs (2026-10-17T20:05:15-03:00 and 20:05:59-03:00). Round 14 should use that full current digest when finalizing, but no separate defect route is needed.
- **R11-SWEEP-03 — no current digest-binding defect.** The R11 sweep's dated read-only input-pin check found the current bindings resolve; its timestamped old prefixes are explicitly draft snapshots, not current pins.
- **R11 transient round-10 validation edit — not open at the later check.** `sweep-r11.md` records that a later scoped `git status --short -- reports/round-8 reports/round-9 reports/round-10 reports/round-11` on 2026-10-17 returned no entries for the earlier transient round-10 receipt change. Its cause remains unknown; route only if a future check finds a live mutation.
- **R9 unattributed PDF — excluded.** `reports/round-9/adjacency.md` §4.3 found no Kotodama attribution; it is not a lane defect.
- **R10 historical input-hash differences — excluded as defects.** `sweep-r10.md` attributes them to later legitimate changes and says the filed round-10 receipt is a historical snapshot; no receipt rewrite is authorized here.

**Routing result:** the open items above are handed to round-14 owners; no unresolved issue is represented as fixed by this router. The round-8–11 source files and filed receipts remain untouched by this worker.