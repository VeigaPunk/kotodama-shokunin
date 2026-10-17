# Round-11 defect sweep — R12-O07..O08

- Audit date: 2026-10-17.
- Scope: read-only conformance review of round-11 report/artifacts for the SHONEN section, digest citations, LOG entry, and verdict consistency. No round-8–11 file was edited. I did not invoke `reports/round-11/run-validation.py`, since its normal output path is the filed `reports/round-11/validation.json`.
- Round status: **REJECTED**, not admitted. `LOG.md:3010-3029` and `SCORECARD.md:184-205` record F below its declared threshold while D/O verify; the validation receipt also has `acceptance_checks_passed: false` and only claim F failing (`reports/round-11/validation.json:1-4,209-211,560-630,639-641`). This is a valid rejection, not a reason to omit the report's normal conformance evidence.

## Findings

### R11-SWEEP-01 — no finalized round report / SHONEN section remains a draft (open)

The only Markdown files found directly in `reports/round-11/` are `adjacency.md` and `report-draft.md`; no final `reports/round-11/kotodama.md` was found, and the lane-local `.ufo/reports/**/*.md` search found no finalized report. `report-draft.md:1-9` explicitly calls itself a draft, says the orchestrator must finalize it, and says “Nothing here is an admission.” Its section is `## SHONEN skeleton` (`report-draft.md:260-269`), not a settled report section. The checklist guidance in `SHONEN.md:1-11` requires evidence for assertions and a named non-author verifier for `[x]` marks.

The round's rejected verdict is already recorded consistently in LOG/SCORECARD, but the report artifact remains unfinished. A final report must preserve the **REJECTED** status, reconcile its stale snapshot values below, and retain the SHONEN checklist/evidence. This is documentation integration work; do not rewrite the filed draft or any other round-11 artifact in this sweep.

### R11-SWEEP-02 — draft F census is stale against the settled receipts (open)

`report-draft.md:135-155,194-207` says the complete receipt set was **149 stable / 43 unstable**. That is a stamped in-flight reading, but it does not match the final receipts/summary/validation now present. Read-only recount, run 2026-10-17:

```sh
python3 -c 'import json,pathlib; ps=list(pathlib.Path("reports/round-11/recheck").glob("row-*.json")); rs=[json.loads(p.read_text()) for p in ps]; print(len(rs), sum(r.get("stable") is True for r in rs), sum(r.get("stable") is False for r in rs), sum(r.get("new_hash") is None for r in rs))'
```

Observed output: `192 147 45 3` (row receipts, `stable: true`, `stable: false`, and null `new_hash`, respectively). The same-day `reports/round-11/recheck/summary.json` records 147 stable / 45 unstable and ratio 0.7656 over all 192 rows. The validation measurement reports 189 byte-comparable rows, 147 stable, and summary counts 192/147/45; its stability is 0.777777777778 (rounded in the receipt to 0.778), because the 3 no-hash rows are separately dispositioned as unreproducible (`validation.json:209-211,543-555,864-865`). All three readings remain below the declared 0.95 threshold. Cause of the draft mismatch: it is an earlier, explicitly stamped in-flight snapshot, not the final summary; do not silently replace historical values in the draft. The finalized report should identify the settled denominator and keep the rejection.

Read-only validation extraction, run 2026-10-17, confirmed `acceptance_checks_passed=false`, D=true, O=true, F=false, with F failure `stability 0.778 < required 0.95` (`validation.json:1,209-211,560-630,639-641`). This agrees with LOG/SCORECARD and the user's stated rejected-round status.

### R11-SWEEP-03 — current digest bindings resolve; draft-only hashes must stay snapshot-scoped

A read-only checker of `validation.json`'s `input_sha256` mapping, run 2026-10-17, found **212 listed inputs, 0 missing and 0 mismatches**. The runner's recorded `runner_sha256` also matches the current `reports/round-11/run-validation.py`. Current code/input checks give `tools/exercise-handoff-e2e.py` SHA-256 `a21934ade22b2cda338645ee389c7f848256348446d8a79f38a9c9ff827d2005`, matching its validation input pin; the current typed projection SHA-256 is `a3aa452cd5ae77c351d9532a707fb1f1ababf77c3fad8b9d28089e6958364a43`. The projection's embedded packet digest equals the live `examples/culture-d2/packet.d2.yml` digest `e0f21509e14ac03ed5747e6bbbb48183cbe56d6b61afff8c8475e4a50137b643`. The draft's full baseline/declaration commit citations (`94ca098b8ab03be52ec80f6925538e5e2c0ed327`, `e3ef1719c123ab4fb83ed94e033961dd61a2e8c7`) resolve with `git cat-file -e <hash>^{commit}` (run 2026-10-17).

The older exercise/runner prefixes in the draft (`38d1cba4…` at its 22:09 snapshot and `97958223cd64…` at its 19:09 receipt snapshot) are not the current code pins. They are time-labelled observations rather than unresolved current input hashes; the finalized report must not present them as settled-tree digests. Likewise, the draft's old typed-projection packet mismatch (`8da90b07…` vs `e0f21509…`, lines 42-46) is superseded: the current embedded pin now matches the packet, and final validation records the D claim passed. No current validation input digest mismatch was found.

## Cross-round scope observation (not attributed to round 11)

An initial `git status --short -- reports/round-8 reports/round-9 reports/round-10 reports/round-11` during this audit (2026-10-17) showed `M reports/round-10/validation.json`. The contemporaneous `git diff -- reports/round-10/validation.json` showed the filed receipt changing from acceptance true to false after adding two newly required drift command keys (ledger coverage 36/38; `python3 reports/round-10/run-validation.py` and `python3 reports/round-11/run-validation.py` absent) and an unrecorded `typed-pipeline-gate.py` registry match. A later repeat of the scoped status command on 2026-10-17 returned no entries. Attribution and the reason for restoration are unknown; this worker made no edits. Treat this as a transient write to a filed artifact, keep it out of any round-10 rewrite, and have the round-12 integrator decide whether a new-file note is needed.

## Verdict

Round 11's rejection marker is consistent across its machine receipt, SCORECARD and LOG. The material conformance defects are the missing finalized report/SHONEN section and the stale in-flight F census in the draft. Current validation hashes and the typed-projection packet pin reproduce. No filed round-8–11 artifact was modified by this audit.

FILES: reports/round-12/defects/sweep-r11.md
SUMMARY: Round 11 correctly remains REJECTED; its report is still a stale draft without a finalized SHONEN section, while current validation bindings reproduce.
