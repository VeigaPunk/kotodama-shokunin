# ReviewDryRun — declaration receipts review (QUALITY 8/9/11), round 61 wave 1

Seat: KotodamaR61.ReviewDryRun (leaf; no dispatch, no installs, no lane writes besides this report).
Scope: `/home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-61/telemetry/declaration-dry-run.txt` vs `reports/round-61/claims.json` and `reports/round-61/separability-manifest.json`; `reports/round-61/telemetry/census-start.txt`.
Method: read-only git + file reads; no counters were run.

## Verdict
The declaration receipt is honest, complete against the declared counting/acceptance commands, correctly names expected pre-landing results, and names a measured revision that is an ancestor of `main`. **One QA-9 gap:** the receipt's third command (separability checker) has no round-local textual declaration.

## Checks that pass (evidence)
1. **Declared counting commands appear verbatim in the receipt.**
   - C: `claims.json` `counting_command` = `python3 -B reports/round-61/accept-c.py`; receipt line 3 `$ python3 -B reports/round-61/accept-c.py` — verbatim.
   - O: `claims.json` `counting_command` = `python3 -B reports/round-61/accept-o.py`; receipt line 15 `$ python3 -B reports/round-61/accept-o.py` — verbatim.
   - Manifest acceptance argv match: C `["python3","-B","reports/round-61/accept-c.py"]` and O `["python3","-B","reports/round-61/accept-o.py"]` (separability-manifest.json C/O `acceptance`) agree with the same receipt lines.
2. **Expected pre-landing results are named and match actuals.**
   - Receipt line 2 names C FAIL legs (SET, SWEEP, FLOOR, LINES, TOPIC, LINK, COPY, LOCATE) — actual failing legs are exactly those (lines 4–6, 13, 16–18); RANGE/STATUS/OPENED/USEDBY/ACCESS/FRESH PASS as expected vacuously/absent.
   - O expected legs TOOL, INDEP, GEN, CLEAN, ERR, REAL — actual failing legs exactly those (lines 16–27).
   - Separability expected `C-><base>`/`O-><base>`; actual is `SEPARABILITY_INPUT_ERROR` exit=2 naming C's absent land (`footwear-codes-terminology.md`), with the receipt's note (line 32) stating later units/legs are unevaluated pre-landing — consistent with QUALITY criterion 9 ("A checker that stops at its first absent land leaves its later legs unevaluated, and the receipt says so").
   - Predicate labels present: `ACCEPT-C-61: FAIL` (line 14), `ACCEPT-O-61: FAIL` (line 28); exits 1/1/2.
3. **Measured revision named and ancestor of `main`.** Receipt line 1 names `106df397655bca3b9fde9d6e798dd93bab2060d9`; `git merge-base --is-ancestor 106df397655bca3b9fde9d6e798dd93bab2060d9 main` → exit 0. Manifest `base` = same revision. `main` tip is `78ad4b1` (commit "round-61: separability manifest and declaration dry-run receipt (revision 0)"), whose parent `106df39` is the instruments-revision-0 commit (message matches the receipt's "(instruments revision 0)").
4. **Census start receipt: exit 0.** Last line `exit=0`; header names `lane main 942abdf4` which equals `claims.json` `round_base` (`942abdf4f94f82a8372c5b550adb8241aa79c467`); run stamp 08:24:34Z precedes the declaration receipt stamp 08:25:55Z.
5. **Committed bytes equal worktree.** `git show 78ad4b1:<path>` sha256 equals working-tree sha256 for `declaration-dry-run.txt` (`efbd6bac…`), `separability-manifest.json` (`d4616db4…`), `claims.json` (`ce98068d…`); `git show 106df39` equals worktree for `census-start.txt` (`f91ebf16…`) and the instruments `accept-c.py` (`0a6e55ca…` = the frozen counter sha in the wave spec), `accept-o.py` (`1ac83e18…`), `reopen-quote.py`, `base-knowledge-files.txt`.

## Finding (severity: low-medium, calibration)
- **F1 — receipt command without a round-local declaration (QA 9 "every receipt command must match a declaration verbatim").**
  - `reports/round-61/telemetry/declaration-dry-run.txt:29` runs `python3 -B tools/check-claim-separability.py reports/round-61/separability-manifest.json`.
  - `reports/round-61/claims.json` contains **no** `separability_command` / `separability_manifest` field (grep for `separab|manifest` in the file: no matches). `reports/round-61/separability-manifest.json` carries per-claim `acceptance` arrays but no checker invocation; `SKILL.md` has no "separability" text (grep: no matches).
  - Precedent: rounds 51–59 declared this command explicitly in `claims.json` (`separability_command`), e.g. `reports/round-51/claims.json:10` (`["python3","-B","tools/check-claim-separability.py","reports/round-51/separability-manifest.json"]`).
  - Impact: the command itself is the canonical form and behaves as expected (exit 2 naming the absent land), so this is a *declaration completeness* gap, not a receipt-fabrication one. It is the sole two-way-check violation I found.

## Residual risk
- The receipt is hand-formed (no `dry-run.py` generator exists in `reports/round-61/`, unlike rounds 52–59); F1 is exactly the class of drift that generator check code prevented. Suggest the L1 either add `separability_command` to round-61 `claims.json` (match prior rounds) or record the w1-spec/manifest as the declaration source.

## Verification gaps
- I did not execute any counter or the checker; all claims above are textual/git verification. The separator exit-code semantics (exit 2) are taken from the receipt only.
- Not reviewed: claim-by-claim clause-to-leg mapping (criterion 11's list check is another seat; the receipt demonstrates fail-ability for every leg of both claims, which satisfies the mechanical "shown able to fail" requirement).
