# RevScorecardCorrections — round 75, wave 3

**Verdict: HOLDS.** The four appended correction rows match the frozen ledger and their stated re-derivations return the declared new tokens from a clone at base. The old tokens/text are present at the specified BASE `stated_at` lines. No removed SCORECARD.md or LOG.md lines occur from base to dispatch `main`.

## Four correction rows

Ran each command from the root of a scratch clone checked out at `f556d1049fe651d3d63975600b13acd9fb686f15`; each command and pathspec are the row's re-derivation command.

| Pair | Filed old → new | Re-derived result | BASE `stated_at` evidence |
|---|---|---|---|
| L75-04 | `249` → `247` | `git grep -c -E '^- `[^`]+\.md` —' ... -- corpus/README.md` returned `247` (exit 0). | `corpus/README.md:813`: `Total knowledge entries: 249.` |
| L75-08 | `absent` → `present` | `git grep -c '非凡特性来自最初造物主' ... -- reports/round-74/evidence/S883.txt` returned `1` (exit 0; presence). | `corpus/lessons/round-74.md:37` contains “was absent from the page it was bound to”. |
| L75-09 | `absent` → `present` | `git grep -c '这个我肯定考虑过' ... -- reports/round-74/evidence/S884.txt` returned `1` (exit 0; presence). | `corpus/lessons/round-74.md:38` contains “absent from this page”. |
| L75-10 | `43` → `44` | `git diff --shortstat 4b825dc642cb6eb9a060e54bf8d69288fbee4904 f556d1049fe651d3d63975600b13acd9fb686f15 -- ':(glob).ufo/waves/round-74/w2/*.md'` returned `44 files changed, 13810 insertions(+)` (exit 0). | `LOG.md:4318` states `43 of 44 report files present at filing`. |

The row commands match the corresponding frozen ledger `rederive` strings. L75-08/09's count-presence parser maps the one-match result to `present`.

## README sweep

Read the script's usage docstring first. Each run was from a scratch clone checked out at the named revision.

- BASE `f556d1049fe651d3d63975600b13acd9fb686f15`: exit **1**. Findings include 247 rows vs 249 files, four missing index rows, two orphan rows, header drift (culture-material 36 vs 40; linguistics 30 vs 32), and the stale first footer (243 vs live 249; directory vector also stale). This is the expected red baseline.
- Claim-Ca landing `012e8d3c8b92f47c734f735d58d118d574fe6a14`: exit **0**; 249 rows/files, no missing/orphan/mismatch/header drift, live footer 249 and no footer findings.
- Claim-C landing `4f5e3b2535c2c06c51627dc2736c40183847cae1`: exit **0**; 252 rows/files, no missing/orphan/mismatch/header drift, live footer 252 and no footer findings.
- `--selftest` on the repaired Ca-landing script: **14/14 checks passed**, exit **0**. For comparison, BASE's pre-repair script selftest exited **1** (`continuation lines space-joined` failed); the repaired script passes that case and the added appendix/last-footer cases.

## Axes / append-only checks

The end-of-file axes section at the inspected Ca commit is the round-74 section; no `## Axes — round 75` section exists at the current dispatch `main` (`82ced5cc205a116516e40895c4241415d54dae52`). Thus there is no round-75 axes row there to validate yet. The round-74 unchanged-axes row's cited freshness pause is supported by the open `kotodama | round-11` L0 item at fleet `.ufo/l0-questions.md:47`; the SCORECARD head at lines 13–15 explicitly disclaims new numeric scores. I did not re-run the round-74 acceptance counters; the round-74 calibration/coverage rows remain author-side historical assertions outside this seat's assigned four-row/sweep checks.

The required removal check, `git diff f556d1049fe651d3d63975600b13acd9fb686f15 main -- SCORECARD.md LOG.md | grep '^-[^-]'`, produced no matching lines (empty result): filed lines remain untouched.
