# ScribeQualityCriterion — QUALITY.md criterion 8 draft

Seat: KotodamaR51a3.ScribeQualityCriterion (leaf). Assigned item: draft QUALITY.md criterion 8 (declared inputs run once before dispatch) in the style of criteria 6 and 7, grounded in the round-50 verifier spot-check (Decision and Pins) and the round-50 contract's argument note at line 117, including how a closure checks compliance from committed bytes (the dry-run receipt).

## Drafted text, ready to paste (append after criterion 7 in `corpus/QUALITY.md`)

> 8. **Declared inputs run once before dispatch** — every declared acceptance or counting command is run once on its exact declared input before the round dispatches, and the receipt is committed. An input-shape error (missing manifest keys, an unreadable manifest, unrecognized arguments) fails the declaration, not the round: the declared command or input is corrected and re-run before dispatch, never substituted with a different input afterward; a land-not-yet-present error (the claimed paths do not exist on the declaration tree) is expected before landing and does not fail the run. A closure checks compliance from committed bytes by reading the dry-run receipt (`reports/round-51/telemetry/declaration-dry-run.txt`): each argv in it must match the declared command verbatim and each exit must be 0 or carry the absent-land message — never an input-shape error, and never a substituted input. Grounded in the round-50 Decision and Pins at `corpus/lessons/round-50-verifier-spotcheck.md#decision` (Ca's frozen self-application required exit 0 on the original `reports/round-50/claims.json`; the committed receipt recorded exit 2 with `SEPARABILITY_INPUT_ERROR manifest is missing base, schema`; a substitute manifest cannot satisfy the unchanged condition) and in the round-50 contract note at `.ufo/waves/round-50/build/ReviewEntryContract.md:117` (the declared `after_required` sweep string with trailing `rows 226 files 226 topic_mismatch 0` exits 2 on `unrecognized arguments`; only the bare command reads the render lines).

## Grounding evidence (file:line)

- `corpus/QUALITY.md:29` (criterion 6) and `:31` (criterion 7): one-paragraph style, bold lead-in, em-dash rule, `-`-grounded pointer with lesson anchor — the template followed.
- `corpus/lessons/round-50-verifier-spotcheck.md:7-11` (`#decision`): "Its frozen self-application requires exit 0 on `reports/round-50/claims.json`; the committed receipt records exit 2. A substitute manifest cannot satisfy that unchanged condition." — the input-shape failure adjudicated as claim-not-met, not rescued by substitution.
- `corpus/lessons/round-50-verifier-spotcheck.md:19-23` (`#pins-and-conformance`): original claims.json lacks `base` and `schema`; `tools/check-claim-separability.py` requires `schema`, `base`, `claims`; `reports/round-50/telemetry/final-conformance.json` records the exact declared argv, exit 2 and `SEPARABILITY_INPUT_ERROR manifest is missing base, schema`; "Main inspected both without execution" — the committed-receipt inspection pattern.
- `.ufo/waves/round-50/build/ReviewEntryContract.md:117`: the claims' `after_required` string `python3 -B reports/round-28/readme/sweep.py rows 226 files 226 topic_mismatch 0` exits 2 (`unrecognized arguments`; base ✓); "Use the bare command and read the render lines." — the unrecognized-arguments instance.
- `reports/round-51/claims.json:54` (`dry_run_rule`): "Every declared counting command and the separability command run once on the declaration tree before wave 1; each must exit without an input error (receipt reports/round-51/telemetry/declaration-dry-run.txt)." — round 51's own implementation of the criterion.
- `reports/round-51/telemetry/declaration-dry-run.txt:1-21,23-43`: the committed receipt; argv lines match the declared commands verbatim; entry 16-18 records exit 2 with "absent from the worktree" (land-not-yet-present, expected pre-landing); entry 19-21 is the flagged historical control showing the input-shape error (missing base, schema) — distinguishing the two error classes.
- `tools/check-claim-separability.py:49-51,1221-1226`: exit 0/1/2 semantics; input errors print `SEPARABILITY_INPUT_ERROR` on stderr.

## Compliance check from committed bytes (closure procedure)

1. Open `reports/round-51/telemetry/declaration-dry-run.txt` from the commit (no re-execution; cf. round-50 "Main inspected both without execution").
2. For every counting/acceptance/separability command declared in `reports/round-51/claims.json` (and the separability manifest), verify a receipt entry whose argv matches verbatim.
3. Verify each such exit is 0 or carries the absent-land message; if any entry shows an input-shape error (missing keys, unreadable manifest, unrecognized arguments), the declaration failed — the round's own checks cannot be read as passes (round-50 precedent: substitute input cannot satisfy the frozen condition).
4. Verify no substituted input appears (argv mismatch with the declaration).

## Result

Criterion 8 drafted, one paragraph, matching the criterion 6/7 style, grounded in the two named sources plus the round-51 dry-run receipt. The closure check is spelled out inside the criterion and here.

## Unrun checks

- I did not run any declared counting command (leaf seat; the dry-run receipt is evidence, not something to re-run).
- I did not edit `corpus/QUALITY.md`; the drafted text is for the closure/L1 to land (QUALITY.md is a record in `reports/round-51/claims.json` `records_not_claims`).

## Tooling

No installs performed or needed (read-only inspection only).
