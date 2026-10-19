- Seat: Ca10 | scribe | Ca | date 2026-10-19 | baseline 456674d

## Post-review calibration fold

**Partial fold; not a closure/admission claim.** In the four named live surfaces, the baseline census has one old-prefix occurrence: `SKILL.md:383` preserves the `b5406bcd…` reader for a dated 2026-10-18 measurement over the pre-integration packet (`SKILL.md:382-388`). Ca02's proposed replacement labels that reading historical and appends a separate 2026-10-19 supersession carrying the full current argot-gate digest. Ca04 verified the before-block match, historical classification, and digest in the proposal. `SCORECARD.md:755` already cites current prefix `10c88433…`; Ca03 correctly proposes no change, also verified by Ca04. No old-prefix hits were found in `corpus/README.md` or root `AGENTS.md` (K02 and Ca04 scans).

The current `tools/gates/argot-derivation-gate.py` SHA-256 is `10c884337fbb2b8f5cc64bedb70e2ddbc34b84c17aaa29fb9be15d049b324a75` (sha256sum output). The `8c7dd098…` / `15f8b232…` strings in round-41 claims/targets are task-definition text, not measured live pins. No in-tree round validation was run; `reports/round-41/validation.json` was absent at the last inventory check, so its cross-references remain unaudited.

Ca04 and Ca05 independently reviewed the proposed SKILL/SCORECARD deltas. Ca04 verifies the exact before-block, historical classification, and current digest; Ca05 reports a post-draft exact-anchor check and re-grep with no disagreement. Ca06's calibration receipt is now present as a DRAFT and agrees on the digest, four-surface census, delta checks, verifier results, and corpus boundary; it does not admit claim Ca. The fold remains partial because Ca01's supersession-record draft and `pin-supersession.json` are absent, so the complete refreshed-row/filed-readings inventory remains to-verify. The round-41 runner and `validation.json` were absent at Ca06's final inventory; no in-tree validation was run, and the validation cross-references remain unaudited.

A broader `corpus/knowledge/` scan finds historical `b5406bcd…` measurement references in `register-lexicon-ceilings.md:18-19,137` and `register-strata-attestation.md:348-369,422`. These are outside the named live-surface census and corpus edits are prohibited this round; do not claim a repository-wide stale-prefix cleanup. If that broader scope is required, route a separately authorized, append-only supersession rather than editing corpus bytes here.

## Owed

- `reports/round-41/calib/Ca01-supersession.md` and `reports/round-41/calib/pin-supersession.json` — absent; complete inventory of refreshed surfaces and retained filed readings cannot be checked.
- `reports/round-41/run-validation.py` and `reports/round-41/validation.json` — absent at the latest referenced inventory; live validation cross-references remain unaudited. Do not execute the in-tree runner.
- If "live files" expands beyond the four named surfaces, owner/integrator to resolve the corpus historical hits under separately permitted scope; no corpus edits this round.

## Citations

- `reports/round-41/claims.json:20-27` — supersession threshold, old-prefix scope, and corpus-change prohibition.
- `reports/round-41/targets.json:188-193` — Ca10 assignment and output path; `targets.json:5-9` shared scope rules.
- `SKILL.md:382-398`; `SCORECARD.md:755` — source measurement and current round-38 digest reference.
- `reports/round-41/calib/Ca02-skill-delta.md:27-55`; `Ca03-scorecard-delta.md:3-10`; `Ca04-verify.md:3-12` — proposed deltas and first verifier result/owed Ca01.
- `reports/round-41/calib/Ca05-verify.md:7-11`; `reports/round-41/scout/K02-pin-scout.md:3-10` — second verifier's post-draft recheck and independent baseline census.
- `reports/round-41/calib/Ca06-receipt.md:3-21,25-33` — current calibration receipt draft and remaining acceptance blockers.
- `reports/round-41/calib/Ca07-gap-fill.md:3-11`; `Ca08-gap-fill.md:3-23`; `Ca09-scribe.md:5-14` — corpus boundary, task-text distinction, and prior incomplete-snapshot notes.
- `corpus/knowledge/linguistics/register-lexicon-ceilings.md:18-19,137`; `corpus/knowledge/linguistics/register-strata-attestation.md:348-369,422` — broader-scope historical digest mentions.
- Command output: `sha256sum tools/gates/argot-derivation-gate.py` → `10c884337fbb2b8f5cc64bedb70e2ddbc34b84c17aaa29fb9be15d049b324a75`.
- Grep output: `8c7dd098|b5406bcd|15f8b232|10c884337fbb` over `SKILL.md`, `SCORECARD.md`, `corpus/README.md`, `AGENTS.md` → sole hit `SKILL.md:383`; exact anchor grep → one source anchor at `SKILL.md:382`, and Ca02 draft contains the `Historical worked ceiling` and dated supersession headings.
- Grep output: old prefixes over `corpus/knowledge/` → the historical references listed above.
- Glob output at final inventory: no `reports/round-41/calib/Ca01-supersession.md`, `pin-supersession.json`, `reports/round-41/run-validation.py`, or `reports/round-41/validation.json`; `Ca06-receipt.md` was present and read.
- `reports/round-41/claims.json:20,23`; `targets.json:23` — task-scope mentions, not current artifact pins.
