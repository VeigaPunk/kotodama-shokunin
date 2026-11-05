# Round 91 · MutationTesterV2 · O (operability) new-mutant pass

Seat: MutationTesterV2 (read-only attack seat; mutated copies in scratch only).
Milestone: r91-v1. Judged on: operability.

## Result

MUTATION-SCORE: 9/16 killed, 7 survived, 0 broken-pattern.
Measured 2026-11-05 with `python3 -B runner.py` (rc 0; log copied to stage as `run.log`).
The frozen 53-pair pass is untouched; its 53 pairs are not reused here
(checked: every new old-string is absent from `reports/round-91/mutants.py` bytes).

## What was measured

- Lane tool `tools/check-advance-evidence.py` sha256 `88597a66c7912861d0a593f984b9eb224a3c46cba3b35d06209b529bc6031093`, equal to the freeze pin. Measured before and after the run; unchanged.
- Clean baseline: `--selftest --work <dir>` → `SELFTEST PASS 77/77`, rc 0. The baseline is green, so every kill is attributable to the mutation.
- Each mutant is one textual replacement applied to a copy under scratch; the old string occurs exactly once in the tool (`src.count(old) == 1`), and the replacement changed the bytes (mutant sha differs from clean).
- Detector: the tool's own selftest, same as the frozen pass. KILLED = rc != 0; SURVIVED = rc == 0.
- Restoration: pristine copy re-run → `SELFTEST PASS 77/77` rc 0.

## Killed (9)

| mutant | selftest rc | first line |
|---|---|---|
| phrase-floor-parse-off | 1 | SELFTEST FAIL 75/77 |
| entry-header-keys-weaken | 1 | SELFTEST FAIL 76/77 |
| appendonly-lands-disp-off | 1 | SELFTEST FAIL 75/77 |
| shape-worst-zero-off | 1 | SELFTEST FAIL 75/77 |
| topic-shared-floor-off | 1 | SELFTEST FAIL 76/77 |
| topic-stem-alwayshit-off | 1 | SELFTEST FAIL 76/77 |
| newids-cited-regex-off | 1 | SELFTEST FAIL 65/77 |
| capture-dispatch-entry-off | 1 | SELFTEST FAIL 75/77 |
| graded-isfile-off | 1 | SELFTEST FAIL 76/77 |

## Survived (7)

1. `newids-status-off` — NEWIDS `status != mined` arm has no fixture (only the uncited reject row S013 carries a non-mined status).
2. `newids-cited-closure-off` — **equivalent mutant**: `scoped` ⊆ `cited` by construction, so the arm is unreachable. Not a coverage gap; dead hardening.
3. `gate-missing-line-entry-off` — GATE arm "no lesson line with id and quote" never exercised in entry mode.
4. `capture-fetched-date-off` — CAPTURE `fetched_at date != as_of` arm: every fixture uses 2026-11-04.
5. `capture-traversal-off` — CAPTURE "not relative and confined" arm (absolute or `..` paths) never fixture-tested.
6. `topic-anchor-table-off` — TOPIC phrase-anchor table-cell text source is redundant on every fixture.
7. `graded-sources-autoinclude-off` — graded set auto-includes lesson/lands/entry bytes; the byte-copy fixture survives via `--graded corpus/lessons/round-90.md`, so the arm is never isolated.

Fixture ideas for each are in `survivors.md`; none was added to the tool.

## Limits

- The count of 16 is the number of new pairs written, not an exhaustive enumeration of v2 behaviour. Pairs were chosen to cover arms that the 77 selftest checks do not isolate; I did not enumerate every arm.
- "Survived" means the tool's own selftest did not notice. It does not establish that the removed arm is behaviourally wrong in the claim's terms.
- `newids-cited-closure-off` is counted as a survivor by the rule (rc 0) but is equivalent; the effective survivor count of real gaps is 6.

## Artifacts (stage: `.ufo/waves/round-91/w1/stage/MutationTesterV2/`)

- `new-mutants.py` — 16 `(name, old, new)` tuples, format matching `mutants.py` (sha256 `0e1ccce8af63a2a9ab63a304c51ec1b80851930e03b80fe76cc1e6fdabf3e429`).
- `new-mutation-score.txt` — MUTATION-SCORE line and one row per mutant with rc, first line, occurrence count and mutant sha256 (sha256 `c5b8d3b68a4dbe756b96ad0b0d1866a475b78731465a3a820ec026527961d280`).
- `survivors.md` — each survivor, check weakened, one-line kill-fixture idea (sha256 `f0a9e7c7877dcea3881bcfd7eb7585558230be2e2dfa20a20921178f87d865fd`).
- `runner.py` (sha256 `d8e7ce3ffae8890ca89bc3b78e74430927346b151bf7c187d94c6a4f3c158faf`) and `run.log` — the re-runnable command: `python3 -B runner.py` from any scratch dir; it writes only to its scratch constant and the stage dir.

## Hosting and tools

No tools installed or upgraded. Python 3 stdlib only. Scratch `/fast/scratch/hyaku/kotodama-r91/MutationTesterV2/` removed before yield. No writes outside the stage dir and this report; no git mutation; no sysctl change.

## Checks for the main agent

- Re-run `python3 -B runner.py` against the same tool sha to confirm 9/16 and 7 survivors.
- Consider whether the six fixture gaps should be closed in a later round; this round's frozen O predicate (52 pairs, 0 survived) is not affected by these new pairs and should not be amended to include them.
