# R22-O04..O06 — deterministic candidate selection

Date: 2026-10-18. Axes: operability/determinism, calibration of the 102-vs-105 discrepancy, preservation of filed evidence. NON-CANON engineering evidence; not a lore receipt.

## Source change and immutable boundary

`reports/round-22/fixes/tie-break.py` is the round-22 successor selector and regression runner. No round-8..21 file was edited. The frozen round-20 runner remains historical evidence, including its original defect.

The old sites are `reports/round-20/run-validation.py:797-809` (packet ranking) and `:852-881` (audit ranking). The round-22 adapter loads the frozen module **only in an isolated clone**, verifies its SHA-256 (`2b7a252b5449415dddac2e667ed2e192df800a80173849989fa72423961646da`), and replaces exactly the two rank functions and two candidate-discovery assignments in `measure_d` in memory. It never rewrites the historical source or receipt. A changed source digest or unexpected assignment/function count refuses adaptation.

The round-22 integration entry points are `candidate_rank(root, relative)`, `candidate_paths(root, paths, role, baseline=...)`, `select_candidate(root, paths, role, baseline=...)`, and `install_round20_selectors(load_round20(clone))`. The integrator must use this successor for the current selection claim; invoking the unadapted historical runner does **not** acquire the fix.

## R22-O04 — rank by content, never metadata

Within the eligible role, the winner is the maximum tuple:

1. Parsed numeric build (`build16`, `build 16`, `build-16`, `build_16`, or a keyed filename's terminal `-16`/`_16`); absent build is `-1`. Version, round and date digits do not independently become build numbers.
2. SHA-256 of the entire file, descending lexicographically; no truncated text or filesystem timestamp participates.
3. Repository-relative path, only when the build and full content digest are equal. This makes identical-content duplicates independent of discovery order without changing which bytes are judged.

Control: the selftest compiles the **actual frozen** `audit_rank` definition into a tiny fixture. Reversing timestamps changes that old winner from `audit-b.md` to `audit-a.md`; the new same-build winner remains `audit-a.md` in both orders. Numeric-build controls select 10 over 9 and select a newer failing audit over an older passing audit: there is no preference for a green verdict.

## R22-O05 — separate roles and bind the measured packet

A hash-only substitution is insufficient: the archive packet's SHA-256 sorts above the real audit's at build 16. The old broad content discovery admits the packet because its prose mentions the contract audit. The successor requires a contract-audit/recheck **document title**, not merely a body mention, before audit ranking. An empty audit set is not a pass, and the existing semantic verdict parser still rejects `Verdict: FAIL`.

Packet candidates are first bound to the selected v3 baseline's `packet_sha256`. No match, malformed pin, unreadable candidate or escaped path fails closed rather than falling back to an unrelated archive. The eligible packet is then ranked using the same numeric-build/SHA-256 rule. Controls cover both timestamp/input orders, identical-byte duplicates, a packet masquerading as an audit through prose, missing/invalid pins and missing/outside files.

On the isolated snapshot used below, the selected pair is:

- Packet: `reports/round-20/handoff/packet.md`, SHA-256 `e92f5e6775b657c24fa6260e340e4e7a04cf6c3777188cba80678bed079ae43b` (the v3 baseline pin), **not** the build-16 archive.
- Audit: `reports/round-20/handoff/audit-v3.md`, numeric build 16, SHA-256 `10f09b9b16829f5db0dd43b5b71a62286f504b06f985c06e773473fd43e72c98`; the unchanged verdict parser reads `pass-with-named-gaps`.

## R22-O06 — 102-vs-105 replay/control

The live v3 exercise has no mtime-based candidate selector to replace. `tools/exercise-handoff-e2e.py` reads an explicit profile baseline (`v3_load_baseline`, `v3_exercise`) and checks baseline integrity, input digests, packet/twin digests and the link census. No edit of that shared tool was needed for this assignment. The timestamp-dependent discovery belonged to its surrounding round-20 validator.

The new regression reverses timestamps of the actual archive packet, baseline-bound packet and audit **inside the clone**, runs the real v3 CLI in each arrangement, and restores their original timestamps. Both arrangements select the same packet/audit and emit byte-identical summaries:

`handoff-v3: exit=0 fields=16/16 glossary=20/20 findings=0 links=105/105 claims=27 statuses=16/7/4 v2_subset=equal alias_leg=landed packet_sha256=e92f5e6775b657c24fa6260e340e4e7a04cf6c3777188cba80678bed079ae43b`

This prevents an archive's 102-link statement from being silently substituted for the baseline-bound live 105-link measurement. It does **not** retrospectively reproduce or correct the historical 102 count, prove how that count was generated, or equate it with the audit's separate markdown count. The filed figures remain untouched (`reports/round-21/recount/r20-2.md`, `reports/round-21/recount/dispositions.md:18-25`).

## Commands, dates and results

Every command below was run on **2026-10-18**, with `export TMPDIR=$PWD/.scratch` before scratch-writing commands. The isolated clones were created with `git clone --shared --quiet . <clone>` from `cd9c8e4cb62896a8b5d0d642cd04966d41dd4d13`; concurrent uncommitted work from other seats was not copied into these baseline controls. No historical validator was executed against the live worktree.

- `python3 reports/round-22/fixes/tie-break.py --root .scratch/round-22-tie-break/clone --selftest` → **exit 0, 23/23 controls**, including two real v3 invocations. The receipt reports **zero changed files under rounds 8–21**. Raw output: `.scratch/round-22-tie-break/selftest.json`.
- In the separate `.scratch/round-22-tie-break/historical-control` clone, `python3 tools/exercise-handoff-e2e.py --profile v3 --selftest` → **exit 0**, positive run plus **28 controls**, links **105/105**, fields **16/16**, glossary **20/20**, findings **0**. Raw output: `.scratch/round-22-tie-break/v3-selftest.txt`.
- In that separate clone, `python3 reports/round-20/run-validation.py --check` → **exit 1**, exactly the known audit-selection failure: it chooses `packet-v3-16.md`, which has no audit verdict. Raw output: `.scratch/round-22-tie-break/historical-check.json`.
- `python3 reports/round-22/fixes/tie-break.py --root .scratch/round-22-tie-break/clone --check` → **exit 1**, now selects the correct packet and audit and removes the audit-selection failure. It exposes a **different** historical check failure: the old `PLACEHOLDER_RE` matches the legitimate word `unchanged` in D4-CL08's `unchanged-foreign-path control` basis. No selector failure remains; rounds 8–21 have **zero byte changes**. Raw output: `.scratch/round-22-tie-break/successor-check.json`.
- `git diff --check` and `git diff --exit-code -- reports/round-{8..21}` → **exit 0**. AST syntax validation of the new script and importing/installing the adapter from inside a clone also passed.

## Integration status / remaining issue

The assigned selector/control implementation is filed; its regression suite and the standard v3 selftest are green. The **full historical successor acceptance is not green**, and is not claimed as such: the newly exposed placeholder false positive needs an explicit round-22 disposition if the integrator requires that historical full check to pass. This seat did not weaken that unrelated check, alter D4-CL08, overwrite old receipts, or change any re-pin row. Current-round gates after the other seats' source fixes and new re-pins belong to the integrator's settled-tree verification.
