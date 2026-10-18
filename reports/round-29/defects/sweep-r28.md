# Round-28 conformance defect sweep — R29-O07..O08

- **Audit date:** 2026-10-18.
- **Scope:** the acceptance runner's replay coverage and `replay-frozen.py` behavior for pinned D4 manifests.
- **Mode:** read-only review of `reports/round-28/audit/o39-o40-law-replay-and-sweep-adversarial.md`, `run-validation.py`, and the saved validation receipt. No round validator was run for this sweep; command results below are the audit's dated observations.
- **Round state:** the late `reports/round-28/validation.json` receipt records `acceptance_checks_passed: true` at **2026-10-18T20:50:17Z**. That receipt does not by itself demonstrate that a frozen manifest was replayed.

## Findings

### O07 — The “all replays green” acceptance clause does not invoke frozen-manifest replay

The final runner's replay measurement at `reports/round-28/run-validation.py:1338-1344` reads only `replay-selftest`, `handoff-v2`, `handoff-v3-selftest`, and `handoff-v3`; no frozen-manifest replay label is in that set. The **2026-10-18** `python3 reports/round-28/run-validation.py --check` snapshot therefore reports only those handoff/selftest exits for the clause. The independently invoked manifest result is recorded separately under O08 (`reports/round-28/audit/o39-o40-law-replay-and-sweep-adversarial.md`, §2.4). The finding is a **runner coverage defect**: its “all replays” wording is broader than the set it grades. The positive acceptance receipt at 20:50:17Z is not a frozen-manifest replay result.

This is independent of whether the replay implementation itself works: an acceptance clause that never invokes a manifest replay cannot observe either a green or red result from that surface.

### O08 — A frozen replay launches the gate against the live tree, not the pinned snapshot

At **2026-10-18 20:26Z**, the archived command `TMPDIR=/var/tmp/r28o39 python3 tools/replay-frozen.py tools/gates/frozen/round-26/post-register/MANIFEST.tsv` produced two D4-row mismatches (gate exit 2 versus recorded exit 0), and the diagnostic cited the live assembly digest rather than the pinned input (`reports/round-28/audit/o39-o40-law-replay-and-sweep-adversarial.md`, §§2.1-2.2). Source inspection explains the result: `replay-frozen.py:175-196` launches the gate by its repository path, while `typed-pipeline-gate.py:78` derives `ROOT` from `__file__`; the gate consequently resolves peers and packet bytes from the live lane, not the mirror snapshot. The replay tool then classifies the gate's input-class refusal as `mismatch` instead of `could-not-evaluate` (§2.3).

This is a confirmed **replay implementation / result-classification defect** in the dated reading. It is separate from O07: O07 is the runner not asking for manifest replay; O08 is what happens when the manifest replay is explicitly invoked. The measurement is snapshot-dependent and does not imply every manifest is red.

## Preservation boundary

Do not merge the runner-coverage and wrong-root findings into one failure mode. The audit's result is non-canon engineering evidence, not an acceptance decision. No round-8–28 file was edited by this sweep.

FILES: reports/round-29/defects/sweep-r28.md | SUMMARY: the acceptance clause omits manifest replay, and an invoked frozen replay reads live D4 dependencies instead of its pinned snapshot.
