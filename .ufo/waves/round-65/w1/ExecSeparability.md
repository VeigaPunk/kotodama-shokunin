# Round 65 separability manifest

## Changed files

- `.ufo/waves/round-65/stage/separability-manifest.json` — checker-v1 manifest with the three claim units C/O/Ca and the separate `REC` record unit. The checker schema has no `reads` field: each claim's reads are represented by its `acceptance` argv, per `tools/check-claim-separability.py`'s manifest schema. All three claim acceptances use `needs_git: true` and `tree: WORKTREE`; the base is frozen at `17c32302c6845c8f164b985a8cb312d3181c8788`.

## Partition and expected class

- C uses the frozen claim lands (entry, `corpus/SOURCES.md`, README), exports S750-S775, and runs `reports/round-65/accept-c.py`. Its other helpers (`tools/check-cited-lines.py`, the README sweep and round-61 locator) are base reads.
- O uses `tools/check-row-fragments.py` as its claim land and runs `reports/round-65/accept-o.py`. `REC` owns the three round-65 counters and exactness-sweep receipt; the O acceptance also reads base `tools/reopen-row.py` and the 26 row-fragment inputs listed individually in `REC`.
- Ca uses the eight frozen Ca lands and runs `reports/round-65/accept-ca.py`. `REC` also owns the three correction records that this acceptance reads (`LOG.md`, `SCORECARD.md`, `.ufo/waves/round-64/w2/LessonFinal.md`); the remaining Ca inputs, including the round-65 lesson, are Ca lands. `tools/check-gate-quotes.py` is a base read.
- **Expected, not measured:** only acceptance dependencies to `REC` (C->REC, O->REC, Ca->REC); no claim-to-claim or `<base>` dependency. This follows the frozen separability note that counters are record lands and each claim uses its own counter. The L1's post-integration run is required to establish the actual result.

The O land partition intentionally treats the acceptance counters and exactness-sweep telemetry named in `claims.json`'s O land list as records, retaining the fragment-checker implementation as O's claim land. This follows the frozen separability block's explicit “counters are record lands” rule. The manifest therefore does not repeat O's five `claims.json` land paths verbatim; reconcile this interpretation if the L1 requires a one-to-one copy of that list.

## Retained evidence and dependencies

- `tools/check-claim-separability.py` docstring lines 7-15 defines `role`, `lands`, `exports`, `acceptance`, and `needs_git`; lines 30-35 describe the counterfactual acceptance/dependency test. Parser lines 371-420 reject unknown unit fields, disallow acceptance on records, and require `needs_git` only with acceptance. Static/dynamic evaluation lines 616-669 skips records as dependers and reports a claim-to-record acceptance repair as `SEPARABILITY_DEPENDENCY`.
- `reports/round-63/separability-manifest.json` declares `REC` as `role: record` with the two acceptance scripts in its lands. The requested precedent `reports/round-63/telemetry/rev-separability.txt` records `C->REC` via acceptance, while `O-><base>` occurred because no declared lands supplied its absent acceptance script. This is why the round-65 counters and the O acceptance's other counterfactual inputs are explicitly assigned to REC.
- `reports/round-65/claims.json` separability block (lines 84-86) says each claim verifies by its own counter, counters are round records, and states the specific C/O/Ca read boundaries. The acceptance source confirms the extra enumerated reads: `accept-o.py` lines 1219-1245 requires 26 scanned row files; `accept-ca.py` lines 113-118 reads LOG, SCORECARD and LessonFinal.
- **Integration dependency:** at authoring time `.ufo/waves/round-65/rows/` was empty (`read` returned “empty directory”); `stage/gate-spec.md` lines 15-18 records the same absence and lines 43-68 name the 26 expected fragment paths. The O acceptance requires exactly 26 (`accept-o.py` lines 1232-1241). `reports/round-65/telemetry/exactness-sweep-o65.txt`, also listed as an O land and needed by MUTEX, was absent from the observed round-65 telemetry listing. These paths are included in REC but must exist in the integrated worktree before the checker can load/run the manifest.

## Verification / blockers

No checker or acceptance command was run; the L1 owns post-integration verification. The missing row fragments and exactness-sweep receipt are integration dependencies, not findings from a checker run. No tools were installed or updated.
