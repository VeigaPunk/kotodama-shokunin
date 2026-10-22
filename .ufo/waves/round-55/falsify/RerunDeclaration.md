# RerunDeclaration — criterion-9 / criterion-11 receipt check (round 55 falsify)

Verdict: CARRIED. The declaration's criterion-9 and criterion-11 receipts are honest and complete at the claim base; the claims commit message transposes the control counters (minor, record-level only, no contract effect).

Verified in a sandbox clone at `8eda9543e940bdc4938fad90182ee6a6fe271d0f`
(`/fast/scratch/hyaku/kotodama-r55-falsify/RerunDeclaration/lane`), exact `git clone` of the lane, `git checkout 8eda9543`. No tools installed (no installs recorded).

## Checked items

- `reports/round-55/dry-run.py check reports/round-55/telemetry/declaration-dry-run.txt` — CARRIED. Exit 0; `MISSING_FROM_RECEIPT []`, `UNDECLARED_IN_RECEIPT []`. Every `$` command in the receipt (accept-c.py x2, accept-o.py x2, check-claim-separability.py, claims-agree.py) matches the declared commands verbatim (claims.json counting_command/agreement_command/separability_command, and each manifest acceptance argv).
- `reports/round-55/claims-agree.py` — CARRIED. Exit 0; `AGREE claims=['C', 'O']`.
- Receipt matches a fresh run — CARRIED. Re-ran `dry-run.py run` at 8eda9543: byte-identical to the stored receipt except the header timestamp line (stored 2026-10-22T20:06:28Z, fresh 20:33:11Z) and the working-tree path in the separability error line (stored `.../kotodama-shokunin`, fresh `.../lane`). No output line, exit code, or expected-pre-landing line differs.
- claims.json `before` vs receipt — CARRIED. C before "exit 1: SET FAIL (count=230), SWEEP FAIL (rows 230 files 230), FLOOR FAIL (cited=0); RANGE, STATUS and USEDBY PASS vacuously; ACCESS PASS" matches receipt lines 3-10; O before matches receipt lines 23-31 (DOUBLED count=0 / TRUNC count=0 / EXIT round54=0 adversarial=0 / ESCAPE 4 missing / NOFALSE, KEEP53, FORMAT, SELFTEST PASS). Both `expected_pre_landing_counting` comments match the receipt's `# role:` lines.
- Sha256 pins of `criterion11-controls.txt` (C) — CARRIED. All five lines match `git show f4015e70h<path> | sha256sum` byte-for-byte: accept-c.py `8e3ea41…`, base-knowledge-files.txt `56f1cb48…`, sweep.py `9b2ccac0…`, check-source-access.py `fb915386…`, criterion11-controls.py `4daf6c04…`.
- Sha256 pins of `criterion11-controls-o.txt` (O) — CARRIED. All five lines match: accept-o.py `a71daef3…`, check-gate-quotes.py `81bbef86…`, fixtures/adversarial.md `e31e602f…`, base-gate-r53.txt `77fd00f4…`, criterion11-controls-o.py `8503070b…`.
- Receipt-vs-declaration alignment at the base — CARRIED. The receipts at 8eda9543 are the revised-instrument receipts (tree f4015e70; C 14/14 with RED-SWEEP-EXIT; O 16/16 with FORMAT leg and the two-way reds), matching the revised claims.json (after_required "all eight legs PASS") and the base-note. The pre-revision receipts at f4015e70 (C 13/13, O 8/8) are superseded by the revision, as claimed.

## Findings by severity

- DEFECT (minor, record text only) — `8eda9543` commit message (git log topic): "controls C 16/16, O 14/14" transposes the receipts' counters; the receipts read C 14/14 (14 `AS EXPECTED` blocks, "CONTROLS 14/14") and O 16/16 (16 blocks, "CONTROLS 16/16"). The number pair is swapped. Fix: message should read "controls C 14/14, O 16/16". No claim contract or receipt data is affected (the receipts themselves are internally consistent and carry the hub counters).
- OVER-READ (cosmetic; no fix required) — `criterion11-controls.txt:1` / `criterion11-controls-o.txt:1` label `tree f4015e70b829523ed81e14ce4279bfab0e0233e4`, where f4015e70 is a commit object, not a git tree object (the commit's tree is `85a6a6e…`). The label is understandable as "at commit f4015e70" and the pin target is unambiguous; the literal object type is mislabeled. Fix if touched: `commit f4015e70…`. No correctness impact.

## Unrun checks

- Did not re-run the control builders (`criterion11-controls.py` / `criterion11-controls-o.py`) in the samebox to reproduce the 14/14 and 16/16 receipts; the receipts' content was cross-checked against the declared `red_control` lists (all 14 C reds and 16 O reds present and labeled AS EXPECTED) rather than re-derived from mutants.
- Did not re-run the landed acceptance instruments (accept-c.py/accept-o.py at the landed tip) — outside this seat's receipt scope; the claims' post-landing legs are verified by other seats.

## Residual risk / verification gaps

- The dry-run receipt records the pre-landing (base) runs; its truth at the base was confirmed by the fresh identical re-run at 8eda9543. Path-dependent text differs only in the two documented, expected lines.
- The commit-message transposition is unfixable (read-only jj/git), so it stands as a record-level finding rather than an actionable edit.
