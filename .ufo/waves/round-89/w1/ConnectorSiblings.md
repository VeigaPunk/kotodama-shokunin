# ConnectorSiblings — round 89 w1 report (read-only sibling-overlap scan)

Paths written: .ufo/waves/round-89/w1/stage/ConnectorSiblings/overlap.md, this file. Scratch /fast/scratch/hyaku/kotodama-r89/ConnectorSiblings/ removed. No tools installed.

Commands (all rc 0): per-sibling `grep -rilE 'evidential|mirativ|epistemic modal|epistemic marking|WALS.{0,20}(77|78)|wals.info/chapter/7[78]'` (39 hits, all inspected); `grep -rilE 'wals\.info' */corpus/SOURCES.md`; PROVINCE.md term grep over lore/chousa/kotoba; recheck/freshness tool census (`ls */tools/*recheck*`, `grep -rlE recheck */tools`); `git show 42816d25:corpus/SOURCES.md` for population rows.

## Evidence
- (1) Evidentiality content: none in any sibling. All 39 hits use "evidential" as an English adjective about evidence, e.g. chousa SOURCES.md:100 S090 and claim-support-test-r37.md:22. No sibling cites WALS 77/78 or wals.info.
- (2) PROVINCE: no sibling claims the topic. Nearest boundary is lore CM-d, in-world source reliability grading (lore PROVINCE.md:19; corpus/README.md:70,77,91), classed adjacent: C must not map evidential markers to reliability or truth grades for a bible, and it hands that off to lore. Chousa (PROVINCE.md:3-8) is adjacent: no general research-method rules. Kotoba: none.
- (3) Recheck tooling: no duplicate. Two items are adjacent and reusable. One is chousa recheck-due-r26.md ("a due date schedules assessment, not truth") plus its archive caveat at japanese-prisma-item-wording-r40.md:25. The other is mori-source-drift.py / mori-drift-recheck.py, which separate churn from content drift. kama release-recheck.py is the route for the on-release rows F excludes.

## Affected axes
Coverage (C ground confirmed uncovered fleet-wide) and adjacency (lore CM-d hand-off, and the F×C cell-set interaction).

## Proposed move (one)
Write a single cross-claim guard into the integration plan. C may edit only `used-by`/`status` of non-population rows. C must not edit any of the 16 population rows or any recheck cell, because measure89.py:189-197 OTHERCELLS would kill F even though C's APPENDONLY allows those changes. C gate lines in round-89.md name only S936-S941, so DISPOSED/BACKED at measure89.py:171,185-186 cannot pick them up. This improves both claims' survival without touching the frozen predicate.

## Risks / unresolved defects
- F-1: url_ok (measure89.py:98-102) accepts a web.archive.org memento with any timestamp. The counter only checks fetched_at, so an old snapshot can back a "freshness" advance. Frozen, so not amended. The closure should check that every archive-backed row's memento year is ≥ 2026.
- F-2: kotodama's auditor computes NNd from opened and treats on-release as exempt. Chousa computes from verified-at and treats on-release as an event. This is method drift with no effect on the r89 population.
- The scan covered sibling working trees as found on disk, not pinned revisions.

## Verification
Re-run the grep in (1) and confirm there are zero linguistic-sense hits. In a dry lands fixture, add a used-by token to S009 and confirm that F's OTHERCELLS FAILs while C's APPENDONLY still PASSes.
