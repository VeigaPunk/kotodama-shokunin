# CriticControlCa — do-nothing control

## Evidence

At the lane root, `python3 -B reports/round-65/accept-ca.py --root .` exited 1. All nine legs failed, byte-similar to `reports/round-65/telemetry/dry-run-ca.txt`: R1 reports `restamp=False` and tree `0ec0e50ea828ca6d8e20298f72af49414692e9e4`; R2 `original_intact=True named=False`; R3/R4 fail; R5 `in_control=True in_log=False`; R6 fails; R7 still has the stale skeleton/await-L1 line; CRITERION fails; QUOTES reports exit 2 with `GATE_QUOTES: 0 findings`.

No lane files were changed for the forgery test. I first overlaid `Correction (round 65, R1) 8bab271c` on `LOG.md` in memory; then tested the stronger global-marker case by appending it to every `accept-ca.py` record read except `final-measures-ca.txt` (so the receipt was not re-stamped). All nine legs still failed:

| Leg | Result under global-marker overlay | What rejects it / remaining failure |
|---|---|---|
| R1 | FAIL (`restamp=False`; `repeats_log_score_lessonfinal=True`) | The correction marker in records cannot substitute for the required receipt stamp/tree/original-stamp checks. |
| R2 | FAIL (`original_intact=True`, `named=False`) | Requires the R2 correction marker, not an R1 marker. |
| R3 | FAIL | Requires both actual/wrong reviewer paths in LOG and an R3 correction in SCORECARD. |
| R4 | FAIL | Requires the statement correction, honest mutant wording, and unchanged predicate. |
| R5 | FAIL (`in_control=True`, `in_log=False`) | Requires the Control-O binding record. |
| R6 | FAIL | Requires the R6 correction tied to R64-M12. |
| R7 | FAIL | The verified-at line remains stale. |
| CRITERION | FAIL | No criterion-17/tree-hash text is supplied by the R1 marker. |
| QUOTES | FAIL (exit 2) | The round-65 lesson input is absent; zero findings on stdout is not a successful run. |

**Conclusion on the assigned fake:** it does not make ACCEPT-CA-65 green. R1 is the direct guard against replacing the receipt restamp with global marker text; other legs continue to reject their own unresolved predicates.

## Findings

1. **R1 does not establish that the claimed original receipt bytes were preserved.** `accept-ca.py` checks for `re-stamped`, a `tree:` line matching the tree of the hard-coded true revision, and the old measured-revision string somewhere after `original receipt bytes`. It does not compare that suffix with the original receipt bytes (or their hash). A fabricated suffix containing only that old revision string can satisfy this part of R1 while omitting the original receipt. **Axis:** calibration / Ca provenance. **Smallest safe correction:** compare the entire post-marker bytes (or a hash of them) to the original receipt captured from the frozen base, and fail on mismatch.

2. **The “committed bytes” basis is not enforced by the counter.** `read()` opens worktree paths directly; aside from the static `git rev-parse 8bab…^{tree}` and R2's base lookup, the legs do not compare the bytes read with committed blobs or reject dirty inputs. Thus an uncommitted records edit can be counted as evidence for a claim that says each leg is over committed bytes. **Axis:** calibration / Ca evidence provenance. **Smallest safe correction:** before scoring, reject dirty/untracked acceptance inputs or require each consumed path's bytes to equal its `HEAD` blob (including the round-65 lesson passed to the quote checker).

3. **Required pre-data artifacts are missing at this snapshot.** `reports/round-65/telemetry/controls-ca.txt` and `corpus/lessons/round-65.md` were not found. The latter explains why QUOTES exits 2 despite printing zero findings; it is an unreadable-input failure, not a quote-clean PASS. **Axis:** calibration / Ca control readiness. **Smallest safe correction:** record the Ca control at the frozen path and provide the round-65 lesson before treating the QUOTES leg as exercised; do not relabel its exit 2 as success.

Report: .ufo/waves/round-65/w1/CriticControlCa.md
