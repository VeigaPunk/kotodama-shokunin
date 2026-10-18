# R22-D07–D08 — D4 re-pin and verification

Date: 2026-10-18. Status: core post-fix checks pass; final source-pin synchronization pending. Assigned writer: D R22-D07..D08. At 14:50:15–14:50:19Z, isolated attempt 01 passed D4 19/19, adapter 12/12, projector 163/163, and the independent family/poison controls. Handoff v3 and its selftest correctly refused because the projector changed after the source owner's ready stamp: D4 expected-holds pinned `c3eb2261e539…`, while the copied source was `6ace1f7c8aea…` (live source moved again to `2819f68769df…` at 14:50:31Z). This is an integration dependency, not a waived pass; no new frozen id has been published against these moving bytes.

## Write ownership

This seat owns the new D4 projection baseline at `tools/gates/expected/d4-typed-labels-check-gate/r22-post/`, new D4 replay rows under `tools/gates/frozen/round-22/d4-repin/`, the D4 row's live resolution re-pin in `tools/gates/typed-pipelines.json`, and this seat's `repin.json`, `verification.json`, `skill-rule-draft.md`, and evidence transcripts under `reports/round-22/bleed/`. The source/adapter owner retains the projector, adapter, derived D4 projection/typed packet/expected holds; this seat does not race those outputs. Handoff renderer and its new v3 baseline belong to their fix owner; this seat verifies their final named pair.

No filed round-8–21 artifact, shared bookkeeping, source-fix file, or `SKILL.md` is changed by this seat. The skill deliverable is a draft for the orchestrator.

## Captured controls before the repair

An isolated Git clone at `.scratch/r22-d07/before` preserves the pre-fix tree. Commands ran on 2026-10-18 at 14:40Z, with `TMPDIR` under this lane's `.scratch` and no round validator executed:

- `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml`: exit 0, 19/19 legs, while the projection still holds the D2 fixture.
- `python3 tools/assemble-d4-typed.py --selftest`: exit 0, 12/12 controls.
- `python3 tools/exercise-handoff-e2e.py --profile v3`: exit 0, 105/105 links, 27 claims, census 16/7/4, v2 subset equal.
- JSON inventory of `examples/culture-d4/typed-labels.d4.yml`: rank component coverage 21; three D2 rank holds plus one rank note. D2 projection control digest `a3aa452cd5ae77c351d9532a707fb1f1ababf77c3fad8b9d28089e6958364a43`.

One exploratory gate call incorrectly named the already typed D4 packet as the canonical input. It returned exit 1, 14/16, due to its fallback/routing interpretation. The corrected canonical invocation above is the claim's command; the rejected invocation is preserved in the final evidence rather than reported as a regression.

## Pending post-fix work

Follow `design.md`: four local rank rules, 74 unchanged labels, 12 legitimate form holds, no inherited D2 rank findings, unchanged D2 projection. After source/adapter/expected outputs are mutually consistent, re-pin the D4 resolution row, snapshot the final working bytes into an isolated clone, run paired controls and the canonical gates, and create new frozen rows. The generic replay pins do not bind live peers by themselves; `repin.json` will name the full read-set pin check and its limits.

## Additional handoff content dependency — not repaired by hashes

At **2026-10-18T14:52:49Z**, structural source/claim review of the new `reports/round-22/handoff/declared-in/packet.md` still found the immutable round-20 D4 claim wording copied into the new packet:

- D4-CL05 at line 148 says 16 findings / 15 hold-or-fail; the corrected projection contains 12 form holds and no other findings.
- D4-CL06 at line 149 says 15 holds / 1 note, including D2 rank passengers; the corrected committed expectation is 12 holds / 0 notes.
- D4-CL07 at line 150 still says four conflicts and three quarantine handles; the corrected D4 rank view has zero of either.
- D4-CL09 at line 152 and OQ-V3-05 at line 307 still describe the removed inherited D2 residuals as present in D4.

Recheck command: `python3 -c 'import json; p=json.load(open("examples/culture-d4/typed-labels.d4.yml")); print(p["coverage"]); print(json.load(open("examples/culture-d4/expected-holds.json"))["counts"]); t=json.load(open("reports/round-22/handoff/declared-in/twin.json")); print([r for r in t["claim_ledger"] if r["claim_id"] in ("D4-CL05","D4-CL06","D4-CL07","D4-CL09")])'` (review date above; the data-side values were independently measured in attempt 01).

The handoff renderer/claim-map owner must issue a new superseding claim map and packet/baseline before claiming semantic integration. Do not edit the filed round-20 claim map, and do not present a later 105/105 structural-link pass as proof that this old wording became true. This re-pin seat reports the defect rather than racing the renderer's sole writer.
