# CriticIndependence — round 50 falsify, claim Ca "independent prediction"

Item attacked: `reports/round-50/separability/r49-expected-independent.txt` as an independent
prediction, and the normalized 6/6 match computed by `reports/round-50/run-validation.py`
(`_norm_finding` lines 387-394, `r49_matches` lines 397-404; receipt key
`r49_matches_independent_prediction`, EXPECT line 133).
All landed bytes were read at `1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0`, either with `git show` or in a
private `--shared` clone under /tmp with `GIT_CEILING_DIRECTORIES=/tmp`. The clone has been deleted. No installs.

## Verdict: PARTIAL

The six findings are reproducible and correct under the contract the round shipped. The
checker prints exactly those six lines, rc 1. A third matcher I wrote from the checker's
docstring reproduces every pair, every first-hit location, and every `xN` count and matched-id list.
Two parts of the claim do not hold:

- **"Independent" overstates it.** The prediction comes from the same contract and refinement
  stream as the checker, from the seat that designed the fixture, and it was compared by a matcher
  written afterwards.
- **The normalization is lossy.** It cannot see whole classes of mismatch.

## 1. Provenance: what the prediction actually is

- The prediction file is byte-identical to the `expected_findings` array in the fixture seat's
  patch (`.ufo/waves/round-50/patches/ExecSepFixture-4.patch`). The landed `r49-fixture.json` equals
  that patch minus `expected_findings`: the checker refuses unknown top-level keys, so the array was
  moved into a .txt file at integration. Command: parse both, compare; both comparisons returned `True`.
- The same seat chose the lands partition, the trees and the export regex
  (ExecSepFixture.md:33-51), and then predicted the findings (ExecSepFixture.md:53-62). The
  predicted set is a deterministic function of choices that seat made. For example, the
  `OVERLAP C/Ca README` line follows from listing `corpus/README.md` under both units, with no matching involved.
- Both seats worked from the same written contract (`gen-build-spec.py:17`, "Shared contract
  (Ca)") plus the same eight L1 IRC refinements (ExecSepFixture.md:6-9; ExecSepTool.md:1,10,14-19).
  The refinements are added-lines-only scanning, muting paths that exist at base, export
  novelty, and overlap. These refinements decide the result:

  | contract variant (my matcher) | dependency findings | difference from the landed six |
  |---|---|---|
  | as landed (added lines, base paths muted) | 5 + 1 overlap | none |
  | written contract only ("name any Y land path") | 7 + 1 overlap | adds `S->C` and `S->Ca` via `corpus/README.md` |

  So the match shows that two implementations agree on a spec they both received. It does not
  independently confirm what the spec says.
- **The "reference matcher" was not preserved.** ExecSepFixture.md:61-62 says the six were
  "computed by an independent reference matcher". No such script is in the landed commit or in the
  seat's work clone (`.ufo/waves/round-50/work/ExecSepFixture-4/reports/round-50/separability/` holds
  only the two JSON files). The prediction's derivation cannot be re-run.
- **There is some exposure to the in-flight checker.** ExecSepFixture.md:82-87 records that the seat
  "saw" a transient `S048` token in in-flight checker/QUALITY bytes during its matcher runs, and it
  gives advice about the checker's implementation (finditer/group(0)). The prediction's wording
  (`xN`, `matched S031,…`) differs from the checker's (`named at PATH:LINE`), so it was not copied
  from checker output. Neither seat ran the checker on the r49 fixture: ExecSepFixture.md:89-91 and
  ExecSepTool.md:56,60 both say so. The temporal-priority claim is therefore credible
  [INFERENCE: it rests on two self-reports].
- **The comparator was written after the fact.** `_norm_finding` and `r49_matches_independent_prediction`
  are not in `.ufo/waves/round-50/patches/ExecRunner.patch` (`grep` finds only `r49_fixture_rc` and
  `r49_detects_C_to_S`). They were added at integration, when both texts already existed. The
  docstring at line 388 says so: "the independent prediction and the tool word findings
  differently". The regex strips exactly the suffixes that differ (` matched …`, ` x\d…`,
  ` named at …`).
- **The headline finding was known in advance.** `C->S` is written into `claims.json`
  (`claims/2/after_required`: "exits 1 naming the C->S dependency") and both seat prompts.

## 2. Strongest counterexample: both sides agree on false dependents

Two of the five predicted dependencies are artifacts that the prediction and the checker share:

- **`C->Ca via land path tools/check-readme-revisions.py`** fires on `corpus/README.md:18` at
  `8c78e6b`: "`` `python3 tools/check-readme-revisions.py` (exit 1). Routed residual, not ``".
  That is Ca's control-reference text. It is charged to C only because both C and Ca land
  `corpus/README.md`. This is the file-granularity problem the build critic flagged
  (CriticCalibration.md:89, F12).
- **`S->Ca via land path tools/check-readme-revisions.py x9`** comes from `corpus/lessons/round-49.md:12`,
  which narrates that the tool "landed". The build critic measured this exact hit and called it "a ledger mention, so
  still a false dependent" (CriticCalibration.md:109).

An independent predictor working from r49's adjudication would not expect these two findings.
This predictor did expect them, because it implemented the same contract. Agreement here
confirms that the implementation follows the contract. It cannot catch a contract-level false
positive, and that is the property a calibration claim needs.

## 3. Normalization loss: mutation results

I imported the landed runner by path and ran `r49_matches` with the real checker output, then with
mutations. Only the copy of the expected file inside the private clone was mutated, and it was restored.

| mutation | `r49_matches` |
|---|---|
| baseline (real checker output) | True |
| prediction counts wrong (x12→x1, x9→x99, x1→x7) | **True** |
| prediction id list wrong (`matched S031` only, or `S099,S100`) | **True** |
| tool emits an extra `SEPARABILITY_DEPENDENCY C->S via acceptance …` finding | **True** |
| tool emits an extra `Ca-><base> via acceptance …` finding | **True** |
| tool emits an unknown kind (`SEPARABILITY_CYCLE …`) or `SEPARABILITY_UNEVALUATED` | **True** |
| tool emits a duplicate finding at another location | **True** |
| tool reports the wrong location (`README.md:99`) | **True** |
| `OVERLAP` line with trailing junk (`… and SKILL.md`) | **True** |
| tool drops the C->S export line | False |
| tool reverses S->Ca to Ca->S | False |
| prediction typo `via exports` | False |
| a path containing ` x1` or ` matched ` | truncated target (`docs/a x1.md` → `docs/a`) |

The causes, all in `run-validation.py`:

- **Uncompared fields.** Line 390 discards everything after the target, so the prediction's
  `xN` counts and matched-id lists never reach the comparison. They are decoration. The checker
  emits neither field, so the "6/6" covers only (pair, kind, target).
- **Lines dropped silently.** Line 403 (`if l.startswith("SEPARABILITY_") and _norm_finding(l)`)
  throws away any finding line the regex cannot parse. Acceptance-leg findings are the important
  case: the fixture has acceptance on all three units (`acceptance_runs=3`), the checker's own
  grammar defines `via acceptance` lines (checker docstring lines 40-41), and `_norm_finding` only
  recognizes `export|land path`. A regression in the dynamic leg would leave rc at 1,
  `r49_detects_C_to_S` true and the "match" true.
- **Sets collapse duplicates.** Lines 401-402 compare sets, and the `SEPARABILITY: <n> findings`
  summary line is never checked.

My own recount shows that on the landed data nothing is actually hidden. The predicted counts
and ids match the real bytes: C->S export 12 ids over 27 lines, SOURCES.md ×2, README ×1,
used-by ×12, lesson ×9. So the defect is in the instrument, not a mismatch being masked today.

## Impacted axes

- **Calibration**, the judged axis. The "independent prediction" label and the 6/6 figure claim
  more than the evidence carries.

There is a further point outside my item. The receipt `reports/round-50/validation.json`
(working tree, 13:32, not in the landed commit) was produced by a `run-validation.py` that differs
from the landed one. The diff touches only the C `TOPIC_OWNER_RE` word boundary (R50-M2). Ca code
is identical, so this report's conclusions are unaffected.

## Smallest safe correction

1. **Make `r49_matches` fail closed.** Return False when any line starting with `SEPARABILITY_`
   (other than the summary) normalizes to None. Compare with `collections.Counter` instead of
   sets. Check that the `SEPARABILITY: <n> findings` summary equals `len(want)`. About 4 lines;
   no fixture change.
2. **Fix the prediction's uncompared fields.** Either drop the `xN` counts and id lists from the
   prediction, or have the checker emit counts and compare them. Uncompared fields should not
   look like evidence.
3. **Re-word the claim.** Call it a "same-contract second implementation (fixture seat), compared
   post hoc on (pair, kind, target)", not an "independent prediction". Record in the lesson or
   QUALITY that `C->Ca` (README overlap) and `S->Ca` (lesson narration) are contract-level false
   dependents that both implementations share, not detections.

Author-lane advice, not admission.
