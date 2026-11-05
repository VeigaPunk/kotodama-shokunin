# Round-91 O/C freeze review — ReviewerFreeze

Scope: static review of the frozen round-91 predicate at 691aebf2 (base d39434b3) — claim-clause ↔ counter-leg mapping, refusal-name grep, citation path checks, mutation-receipt header defect, stub control. Read-only; all probes ran against scratch copies only. Full report: `.ufo/waves/round-91/w1/stage/ReviewerFreeze/freeze-review.md` (23.8 KB, 33 numbered evidence rows, commands inline).

## Findings

**D1 (defect)** — claims.json O.before cites `reports/round-91/controls/before-v1-entry.txt` "measured by" receipt; that file exists neither at base, nor at freeze, nor in the working tree (`ls reports/round-91/controls/` → only stub + at-freeze-* + before-v1-selftest.txt; `git ls-tree -r 691aebf2 | grep before-v1` → only `before-v1-selftest.txt`). The "entry mode graded the round-90 fixtures as PASS at base" half of O.before is unreproducible from the frozen artifacts. The corroborating partial is `before-v1-selftest.txt` (committed at freeze, 67 `ok` lines, 0 of the nine refusal names) — it backs the "0/9 named refusals" half but not the fixture-PASS half.

**D4 (defect)** — mutant loop's `head` reuse in reports/round-91/mutants.py:113 (clean) → :134 (last mutant) → :146 (receipt write): the receipt header `# clean selftest rc=0 ['SELFTEST FAIL 76/77']` in reports/round-91/mutation-score.txt:2 is the **last mutant's** first stdout line, not the clean run's tally, despite `clean_rc: 0` in the JSON sidecar. Killed/total/survived/broken counters are unaffected (`head` is display-only), and measure91.py's MUTATION leg greps only the `MUTATION-SCORE:` line, so no counter leg flips — but the receipt header is unreliable as a binding artifact. Probed by feeding a cloned v2 tool with the tally string forced to FAIL through the full 53-pair pass: same header, `53/53 killed`, rc=1 from mutants.py.

**D5 (defect, counter contract)** — measure91.py never verifies the mutation receipt artifact that O.after_target names as part of the deliverable ("a mutation receipt over every v2 sub-check"); `grep -n receipt measure91.py` → only `--receipt` plumbing for the leg output, no existence or content check against the frozen tool's rows. The killed/total leg runs the frozen mutants.py copy itself, which is why the run still binds to the freeze bytes — but the O-17 clause "a mutation receipt over every v2 sub-check" is checked by nothing.

**W1 (weakness)** — claims.json C.surface "Topic lines name the register in **13** linguistics entries": no command named in the claim; I could not reproduce 13 under any natural reading of the linguistics partition at base (`topic:`-line greps → 3 and 12; whole-text synonym greps → 11 and 16). The other five surface numbers reproduced exactly (0 filename owners, 35 linguistics files, 875 registry rows, last id S951, and the entry path correctly absent at both revs).

**W2 (weakness, on record)** — mutants.py:113-115 clean gate is rc-only: a selftest exiting 0 while printing `SELFTEST FAIL …` passes the green gate (probe above). Not exploitable round-91; measure91's SELFTEST/OKCOUNT/TOOL legs plus the frozen sha pin absorb it. Should be named in the round report as a composition precondition, not as a solo guarantee.

**W3 (weakness)** — measure91.py grade_c APPENDONLY arm indexes `cells[3]/[7]/[8]/[10]` without verifying a new row's cell count against the 11-column header first; a malformed short row raises IndexError inside grade_c, which is neither a leg FAIL nor a Refused rc=2, so the counter aborts with an uncaught traceback instead of emitting a scored verdict.

**N1 (nit)** — claims.json carries a top-level `legs` block (O: 7 names, C: 4 names) plus a second `C.legs` (8 sub-legs); the counter's ENTRY leg consumes the 8-leg list, and the top-level 4-name C list is used by nothing. Harmless but a reader trap.

**N2 (nit)** — reports/round-91/mutants.py docstring "(43 pairs, kept verbatim) plus nine pairs over the v2 entry-mode sub-checks" = 52, but `MUTANTS` holds **53** triples (10 v2 pairs, not 9); O.mutation_min=52 still holds as a floor. The 43/9/52/53 numbers never reconcile in one place.

## Clause coverage summary

- O: 17 clauses enumerated; 16 map mechanically to a counter leg (TOOL, SELFTEST, OKCOUNT, REFUSALS, MUTATION, STUB, MATERIALIZE) + 9 v2-tool `chk()` anchors; 1 clause (O-17 receipt) checked by nothing → D5.
- C: 15 clauses enumerated; 14 map to ENTRY/INDEX/APPENDONLY arms plus named mutants/chk names; 1 clause (C-15 surface numbers) review-only with no base-reproduction leg → W1 for the unverifiable "13".
- Refusal names: 9/9 present verbatim as `chk('<name>'` in the frozen working tree grader (lines 1013, 1017, 1019, 1021, 1028, 1034, 1041, 1045, 1049), selftest counts exactly 77 `chk` calls.
- Stub control: 22 printer CASES → 22 `  ok ` lines ≠ 77 (OKCOUNT refused), zero of the 53 mutant target strings in its bytes → 0 killed (BROKEN-PATTERN on all, probed `0/53 killed, 0 survived, 1 broken-pattern` rc=1). Both STUB arms hold.

## Verification gaps

- Static review + scratch-probe level; measure91.py itself was not executed end-to-end (its MUTATION leg re-runs the frozen mutants.py, which I already ran twice on scratch copies and once through the 1-pair probe for branch coverage).
- The "13" W1 count stays open unless the L1 supplies the original command.
- Scratch dir `/fast/scratch/hyaku/kotodama-r91/ReviewerFreeze/` deleted (rc 0 confirmed); nothing installed, no pacman/uv-tool/sysctl touched; nothing written outside the stage dir and this report.
