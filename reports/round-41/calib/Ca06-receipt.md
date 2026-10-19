- Seat: Ca06 | executor | claim Ca | date 2026-10-19 | baseline 456674d

# Ca06 — calibration receipt draft: N3 argot-digest supersession

**Status: DRAFT; claim Ca is not yet admitted.** This receipt records the measured baseline, checks the available deltas and verifier fragments, and distinguishes named-surface results from out-of-scope historical pins. It does not apply any SKILL.md or SCORECARD.md changes.

## Findings

- Claim Ca requires the pre-r38 argot digest rows to be refreshed as dated supersessions carrying the current digest, preserves filed rounds, and requires a pin-supersession record plus two independent verifiers (`reports/round-41/claims.json:19-27`). The N3 queue row remains `carried-with-owner` pending a SKILL/pin-cascade pass (`reports/round-40/op/defect-queue-v2.json:352-358`).
- The current `tools/gates/argot-derivation-gate.py` SHA-256 is `10c884337fbb2b8f5cc64bedb70e2ddbc34b84c17aaa29fb9be15d049b324a75` (command output: `sha256sum tools/gates/argot-derivation-gate.py`). This matches the full digest and transition note in the filed r38 receipt (`reports/round-38/validation.json:17-18`).
- In the four named live surfaces, the only stale-prefix hit is `SKILL.md:383`, `b5406bcd…`, attached to a measurement dated 2026-10-18 on the pre-integration packet (`SKILL.md:382-388`). `SCORECARD.md` has no stale-prefix hit and already cites `10c88433…` at line 755; `corpus/README.md` and `AGENTS.md` have no stale-prefix hits (Grep results, corroborated by `reports/round-41/scout/K02-pin-scout.md:5-10,18-23`).
- The proposed SKILL delta preserves the measured digest/value, labels it historical, and adds a separate 2026-10-19 supersession with the full current digest (`reports/round-41/calib/Ca02-skill-delta.md:27-55`). The SCORECARD delta correctly proposes no change (`reports/round-41/calib/Ca03-scorecard-delta.md:3-10`). Ca04 verified the exact anchors and delta classifications; Ca05 independently re-grepped after those drafts appeared, with no disagreement (`reports/round-41/calib/Ca04-verify.md:5-8`; `reports/round-41/calib/Ca05-verify.md:7`). These are draft/verifier results; the live source files remain unchanged (command output: `git status --short -- SKILL.md SCORECARD.md corpus/README.md AGENTS.md tools/gates/argot-derivation-gate.py` was empty).
- The `8c7dd098…` text in `reports/round-40/run-validation.py:11` is a filed runner constant and cannot be edited under the round-41 byte-preservation rule (`reports/round-41/targets.json:6-8`). The old prefixes in `reports/round-41/claims.json:20,23` and `targets.json:23` describe the declared task/scope, not live gate measurements.
- Scope caveat: a broader `8c7dd098|b5406bcd` search found 7 occurrences across two `corpus/knowledge/` files. They are date-bound historical measurement passages: `register-lexicon-ceilings.md:18-20,135-140` and `register-strata-attestation.md:345-369,421-423`. These are outside the four named surfaces; if “every LIVE-file row” is intended to include them, the repository-wide sweep is not clear, and the round's no-corpus-changes rule prevents editing them (`reports/round-41/claims.json:26-27`; `targets.json:8`).
- No `reports/round-41/calib/Ca01-supersession.md`, `calib/pin-supersession.json`, `run-validation.py`, or `validation.json` was present at this receipt's final check (Glob results: no matches). Therefore the required inventory is not yet checkable, the in-round validation cross-reference cannot yet be audited, and acceptance remains to-verify. The in-tree round runner will not be executed, per `reports/round-41/targets.json:8`.

## Owed

- `reports/round-41/calib/Ca01-supersession.md` and `reports/round-41/calib/pin-supersession.json` — Ca01/integrator: land the supersession inventory, name the retained filed/historical readings, and resolve whether the additional corpus/knowledge passages are excluded by the claim's scoped census or remain future work. No corpus edit is authorized this round.
- `reports/round-41/run-validation.py` and `reports/round-41/validation.json` — integrator: not present at this check; when the validation receipt lands, inspect its live cross-references only. Do not execute the in-tree runner.
- Full acceptance remains to-verify until the supersession record is present and all claim thresholds are reconciled against the authorized scope.

## Citations

- `reports/round-41/claims.json:19-27` — claim Ca, required after-state, commands, thresholds, and non-goals.
- `reports/round-41/targets.json:6-8,160-164` — shared boundaries and this seat's assignment.
- `reports/round-38/validation.json:17-18` — full r38 current gate digest and supersession note.
- `reports/round-40/op/defect-queue-v2.json:352-358` — N3 remains carried-with-owner.
- `SKILL.md:382-398`; `SCORECARD.md:755`; `corpus/README.md`; `AGENTS.md:1-40` — named live-surface anchors and scan set.
- `reports/round-41/calib/Ca02-skill-delta.md:27-55`; `Ca03-scorecard-delta.md:3-10`; `Ca04-verify.md:5-8`; `Ca05-verify.md:7` — drafts and independent verification results.
- `reports/round-40/run-validation.py:11` — filed old `ARGOT_SHA_UNUSED` value.
- `corpus/knowledge/linguistics/register-lexicon-ceilings.md:18-20,135-140`; `corpus/knowledge/linguistics/register-strata-attestation.md:345-369,421-423` — additional historical digest references outside the named surface list.
- Command outputs: `sha256sum tools/gates/argot-derivation-gate.py` → `10c884337fbb2b8f5cc64bedb70e2ddbc34b84c17aaa29fb9be15d049b324a75`; `git rev-parse HEAD` → `456674dec01b8c433d7635a0edb49448f7714e12`; empty `git status --short` for the named live sources; `Grep` over the four named live surfaces → only `SKILL.md:383`; `Grep` over `corpus/knowledge` for `8c7dd098|b5406bcd` → 7 matches in two files; `Glob` → no Ca01 draft, supersession JSON, round-41 runner, or validation receipt.
