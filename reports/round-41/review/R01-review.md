- Seat: R01 | reviewer | cross | date 2026-10-19 | baseline 456674d

## Review

### O — checker false-green hunt

- **No checker verdict is available.** At review time, `reports/round-41/op/O02-checker.md`, `tools/harness/round_runner_conformance.py`, and O03’s predicted census were absent. O05 independently records the same missing checker and correctly makes no classification claim (`reports/round-41/op/O05-traps.md:5-11`). Treat all checker behaviors and census output as `to-verify`; do not admit O on this evidence.
- **Template-side false-green risk:** O01’s `make_receipt()` checks that `named_findings` and `limits` are lists of nonblank strings, but `any(...)` is false for an empty list, so `[]` passes; neither it nor the checker is yet shown to enforce the documented “round-specific” content (`reports/round-41/op/O01-template.md:31-39,42-52,98-100`). The checker’s selftest should include empty fields and the known r39 stale/duplicated findings as negatives, not merely check for field names/types (`reports/round-39/run-validation.py:195-200`; `reports/round-38/run-validation.py:195-200`).
- **Cohort/count contradiction:** claims line 14 declares seven runners r34–r40; line 18’s `reports/round-3[3-9]/run-validation.py` plus round-40 selects eight (r33–r40). Resolve this before reporting 100% coverage or comparing rows (`reports/round-41/claims.json:14-18`). My read-only AST scan of the seven named runners found r34–r39 with absolute `ROOT` and `chdir`, and r40 with file-relative `ROOT` and no `chdir`; it did not execute a runner. K01 likewise distinguishes r33 prior art from the seven-runner cohort (`reports/round-41/scout/K01-runner-scout.md:5-18`).
- A generic checker must demonstrate dominance, not token presence: reject a runner with no guard on the publish path, while accepting r40’s guard-before-write shape (`reports/round-40/run-validation.py:227-244`). O02 is absent, so positive/negative controls and its unknown-input behavior remain unverified.

### Ca — pin census completeness

- K02’s four-surface scan is reproducible: `SKILL.md:383` has the sole old-prefix hit in those four files, within a dated pre-integration measurement (`SKILL.md:382-388`); SCORECARD already cites `10c88433…` (`SCORECARD.md:755`); corpus README and AGENTS have no matching digest. Ca02’s proposed after-block explicitly labels the old reader as historical and appends a dated current-pin supersession; Ca03’s no-change disposition is supported by the existing SCORECARD pin (`reports/round-41/calib/Ca02-skill-delta.md:30-55`; `reports/round-41/calib/Ca03-scorecard-delta.md:5-10`).
- **The broader “every LIVE-file row” census is not complete yet.** A separate read-only scan found historical `b5406bcd…` readings in `corpus/knowledge/linguistics/register-lexicon-ceilings.md:18-19,137-140` and `corpus/knowledge/linguistics/register-strata-attestation.md:345-368,421-423`. These are dated evidence, not current gate pins, and the round forbids corpus edits; nevertheless the supersession inventory should explicitly classify/list them or narrow its claim scope. K02’s enumerated scan does not cover these files (`reports/round-41/scout/K02-pin-scout.md:5-10,18-23`).
- The round-41 contract itself contains the old prefixes as task wording/search patterns, not as measurements (`reports/round-41/claims.json:20-23`; `reports/round-41/targets.json:23`); classify these as contract references, not refresh targets. `tools/gates/expected/register-law-gate/r30-post/expected.json:10,20` pins the law gate, and `sha256sum` confirms it is still `15f8b232…`; it is not an argot-gate stale pin. The argot gate independently hashes to the claimed `10c884337fbb2b8f5cc64bedb70e2ddbc34b84c17aaa29fb9be15d049b324a75` (command output).
- The supersession inventory and validation cross-reference census cannot yet be checked: Ca01 and Ca04 were absent, and no round-41 `validation.json` exists (`reports/round-41/calib/Ca05-verify.md:7-11`). Ca05’s existing check is useful but is not evidence for those missing artifacts.

## Owed

- `reports/round-41/op/O02-checker.md` and `tools/harness/round_runner_conformance.py`: review actual predicates/selftests and classify the adversarial fixtures; verify guard dominance, SHA non-nullness, findings/limits checks, and unreadable/unparseable inputs.
- `reports/round-41/op/O03-predicted.md`: resolve the seven-versus-eight roster, then compare checker rows with the predicted census.
- `reports/round-41/calib/Ca01-supersession.md` and `reports/round-41/calib/Ca04-verify.md`: check that the inventory accounts for the two historical corpus-knowledge occurrences without editing corpus bytes.
- `reports/round-41/validation.json`: if filed, inspect its claims/validation digest cross-references only; do not execute the in-tree runner.

## Citations

- `reports/round-41/claims.json:14-24` — both claim contracts, required cohort and counting commands.
- `reports/round-41/targets.json:195-200` — R01 review mission and assigned output.
- `reports/round-41/op/O01-template.md:31-52,90-102`; `reports/round-41/op/O05-traps.md:5-11` — template contract and missing-checker evidence.
- `reports/round-41/scout/K01-runner-scout.md:5-18`; `reports/round-40/run-validation.py:5,197,227-244` — runner census and r40 reference.
- `reports/round-41/scout/K02-pin-scout.md:5-10,18-23`; `reports/round-41/calib/Ca02-skill-delta.md:30-55`; `reports/round-41/calib/Ca03-scorecard-delta.md:5-10` — four-surface pin findings and drafts.
- `corpus/knowledge/linguistics/register-lexicon-ceilings.md:18-19,137-140`; `corpus/knowledge/linguistics/register-strata-attestation.md:345-368,421-423` — additional dated historical readings outside K02’s scan.
- `tools/gates/expected/register-law-gate/r30-post/expected.json:10,20` — law-gate pin; command output: `sha256sum tools/gates/argot-derivation-gate.py tools/gates/register-law-gate.py` returned current hashes `10c884337fbb…` and `15f8b232…`.
- `reports/round-41/calib/Ca05-verify.md:7-11` — missing supersession/verifier/validation dependencies.
