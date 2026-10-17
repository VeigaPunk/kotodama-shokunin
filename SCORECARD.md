# kotodama-shokunin — SCORECARD

Axes per fleet `AXES.md` (depth, coverage, operability, freshness,
calibration, adjacency). Every score is a claim: it carries the counting
command and the commit it was measured against.

## Axes

| axis | score | evidence | counting command | measured against |
|---|---|---|---|---|
| depth | 6 | 176 entries with cited sources, decision tables, worked derivations | `find corpus/knowledge -name '*.md' \| wc -l` = 176 | worktree, mint-corpus commit 2026-10-17 (commands re-runnable) |
| coverage | 6 | 6 partitions; civilizations/ covers 92 bases across all macro-areas | `ls corpus/knowledge \| wc -l` = 6; `ls corpus/knowledge/civilizations \| wc -l` = 92 | same |
| operability | 3 | index + QUALITY bar + executable checklists; verification gates are specs, not scripts (named gap in corpus/README.md) | `test -f corpus/README.md && test -f corpus/QUALITY.md` | same |
| freshness | 1 | mint day; no re-verification cycle yet — first re-verify is a planned claim | — | — |
| calibration | 6 | every entry carries a calibration section; master registries at verification/calibration-registry.md + source-discipline; 1258 to-verify flags | `grep -rc 'to-verify' corpus/knowledge --include='*.md' \| awk -F: '{s+=$2} END {print s}'` = 1258 | same |
| adjacency | 4 | synthesis/worldbible-integration-contract.md landed; handoff format defined; README fleet index row live | `test -f corpus/knowledge/synthesis/worldbible-integration-contract.md` | same |

## Capabilities

| name | what it can now do | evidence | first-working round |
|---|---|---|---|
| corpus indexing | generate corpus/README.md from per-entry topic lines | corpus/README.md (176 entries indexed) | mint (operator dispatch) |
| provenance screening | enforce cited-source + to-verify + calibration discipline across batch authorship | 1258 flags + QUALITY.md bar | mint (operator dispatch) |

## Planned (next rounds)

1. Implement the first executable verification gate
   (verification/phonology-sanity-gate.md) — operability claim.
2. to-verify triage pass over the 1258 flags per
   verification/to-verify-triage-protocol.md — freshness claim.
3. First end-to-end domain task executed and logged by the lane itself:
   a miniature culture built from the corpus tooling (SHONEN box 2) —
   note worked-example-mini-culture.md is corpus reference, not the
   executed task.

## Saturation

Saturation line: score 8 on any axis. Stagnation window: 3 rounds without
a capability row.

## Retired

None.
