- Seat: P01 | planner | cross | date 2026-10-19 | baseline 456674d

## Axes and scope

This plan covers the declared operability move O and calibration move Ca only; freshness remains paused, and no canon, promotion, closure, or filed-byte repair is in scope (`reports/round-41/claims.json:9-27`; `REGIMEN.md:27-43`). P01's assignment is planning both claims, not implementing their source files (`reports/round-41/targets.json:27-31`). Workers write only assigned round-41 fragments; the integrator applies source changes and records them after the wave (`reports/round-41/targets.json:4-9`; `AGENTS.md:5-9`).

## O — operability plan

1. Treat `reports/round-40/run-validation.py` as the reference and the filed r34-r39 runners as immutable census subjects. The static evidence establishes the defect shape: r39 has an absolute ROOT and `os.chdir` (`reports/round-39/run-validation.py:5-13`); r40 uses `Path(__file__).resolve().parents[2]`, does not chdir, calls `guard_receipt()` before writing its receipt, and records its runner hash plus named findings/limits (`reports/round-40/run-validation.py:5,197-209,227-247`). SCORECARD records r40 as the N7 cure and r39 root-regression fix (`SCORECARD.md:781-797`).
2. O01 drafts the complete template for later copying into `reports/round-<N>/run-validation.py`: use the relative ROOT expression; anchor file/subprocess paths to ROOT without changing process cwd; keep the guard on every publish path before receipt writes; compute a non-null own-file SHA-256; and require round-specific `named_findings` and `limits`, not copied historical text. Keep measurement/check/selftest modes read-only with respect to receipts. The template contract is the five points in O's claim (`reports/round-41/claims.json:13-18`).
3. O02 drafts a static AST/text conformance checker rather than importing or executing the runners. It should emit one deterministic row per r34-r40 runner, naming each applicable defect class across the five contract points; `--selftest` should exercise conformant and adversarial fake runners (including guard-after-write, absent/null digest, chdir, absolute-root, and stale/shared findings). O03 independently predicts the seven rows; O04/O05 extract and test the checker and compare JSON row-for-row; O09 verifies r40 as the reference. No runner file is executed by these checks (`reports/round-41/claims.json:14-18`; `reports/round-41/targets.json:40-73,96-101`).
4. O06 drafts queue-v2 dispositions only after the checker and census evidence land. Preserve the distinction between historical defective runners (which stay filed and should be flagged) and the r40/future-template cure. The current N7 row says four null receipts and describes r40 as its cure (`reports/round-40/op/defect-queue-v2.json:370-376`); the separate r39-root row expects r40's relative-root shape (`:312-319`). Update both rows to fixed-with-evidence only if the accepted evidence actually demonstrates the relevant cure and future conformance check; do not claim r34-r39 are repaired.

## Ca — calibration plan

1. Use K02's occurrence inventory as the authority for the live-file read set and its historical-vs-current classification. Ca's deliverable is a supersession map plus exact SKILL/SCORECARD delta drafts, not in-place edits (`reports/round-41/targets.json:21-24,125-157`; `reports/round-41/claims.json:19-24`).
2. Pin the replacement digest from the current argot gate at integration time: the observed command output is `sha256sum tools/gates/argot-derivation-gate.py` → `10c884337fbb2b8f5cc64bedb70e2ddbc34b84c17aaa29fb9be15d049b324a75`; this agrees with the r38 receipt and r40 assembly audit (`reports/round-38/validation.json:17-18`; `reports/round-40/adj/A03-verify-assembly.md:45`). Each supersession entry should identify the file/row, old reading, exact replacement row, and whether the old text remains as a marked historical reading. The SKILL's worked-ceiling measurement explicitly dates its b5406bcd reading (`SKILL.md:382-389`); preserve that measurement as historical and append/attach a clear supersession, rather than silently rewriting the old evidence.
3. Ca01 drafts the complete JSON map from K02's census; Ca02 and Ca03 supply exact before/after blocks for SKILL.md and SCORECARD.md. Ca04 checks each anchor and historical classification; Ca05 independently repeats the scoped stale-digest search after draft application. Acceptance is zero unmarked stale argot digest references on the scoped live surfaces (or only explicitly marked historical quotes), with every changed row represented in the map (`reports/round-41/claims.json:20-24`; `reports/round-41/targets.json:125-157`).
4. Avoid a repository-wide blind replacement. Broad read-only search also finds historical round/lesson evidence (for example, `corpus/lessons/round-27.md:78` records the b5406bcd digest as a dated reading), and the live `15f8b232…` references belong to the separate register-law gate baseline, not the argot gate; leave those and all filed round bytes untouched unless the owner establishes a separate authorized scope (`tools/gates/expected/register-law-gate/r30-post/expected.json:10,20`; `reports/round-41/targets.json:6-8`). In particular, do not re-freeze `declared-in-r7` or edit corpus files (`reports/round-41/claims.json:26-27`).

## Integration and stop conditions

Integrate O and Ca independently, then run the claim-declared conformance/checksum searches against the delivered tree and require independent review before adjudicating either axis. Never execute any `reports/round-*/run-validation.py` in-tree; the round-41 validator leg is owed to the integrator for a permitted isolated-tree procedure, or must remain explicitly `could-not-evaluate` if safe isolation is unavailable (`reports/round-41/targets.json:8`; `REGIMEN.md:37-50`). No O/Ca acceptance should be inferred from a template, a digest match, or a checker selftest alone.

## Owed

Final implementation, census, independent verification, source application, and round-41 validation are owned by their assigned seats/integrator. P01 did not run checker modes or any round runner; in-tree round-validation execution remains prohibited.

## Citations

- `reports/round-41/claims.json:9-27` — axis set, claim contracts, thresholds, and non-goals.
- `reports/round-41/targets.json:4-9,21-31,40-73,96-101,125-157` — shared constraints and assigned seats.
- `REGIMEN.md:27-50` — per-round verification, admission, and record requirements.
- `SCORECARD.md:746-797` — r38 digest and r40 N7/root-regression status.
- `reports/round-39/run-validation.py:5-13`; `reports/round-40/run-validation.py:5,197-209,227-247` — contrasting runner shapes.
- `reports/round-40/op/defect-queue-v2.json:312-319,370-376` — N7 and r39-root queue rows.
- `reports/round-40/adj/A03-verify-assembly.md:45` and command output `sha256sum tools/gates/argot-derivation-gate.py` — current argot digest.
- `SKILL.md:382-389` and `tools/gates/expected/register-law-gate/r30-post/expected.json:10,20` — historical argot measurement and distinct law-gate digest.
