# kotodama-shokunin — SCORECARD

Axes per fleet `AXES.md` (depth, coverage, operability, freshness,
calibration, adjacency). Every score is a claim: it carries the counting
command and the commit it was measured against.

## Axes

| axis | score | evidence | counting command | measured against |
|---|---|---|---|---|
| depth | 0→pending | seed SKILL.md carries decision table but corpus cites are unlanded | `grep -c '^| ' SKILL.md` (6 rows) | seed commit |
| coverage | 1 | corpus skeleton exists, 4 partition dirs | `find corpus/knowledge -mindepth 1 -maxdepth 1 -type d \| wc -l` | seed commit |
| operability | 1 | checklists exist but not yet executed end-to-end | `grep -c '^- \[ \]' SKILL.md` (4 items) | seed commit |
| freshness | 0→pending | no re-verification cycle yet (mint day) | — | — |
| calibration | 1 | calibration section seeded via synthesis/source-discipline-calibration.md (planned) | — | — |
| adjacency | 2 | lore handoff contract declared in PROVINCE.md + synthesis plan | `grep -c 'lore' PROVINCE.md` (3) | seed commit |

## Capabilities

| name | what it can now do | evidence | first-working round |
|---|---|---|---|
| — none yet; corpus seeding in flight (mint directive) — | | | |

## Planned (next rounds)

1. Corpus seeding lands (64 swarm entries): coverage claim, counting
   command `find corpus/knowledge -name '*.md' \| wc -l` (target 64 + index).
2. corpus/README.md index + knowledge-entry spot audit: operability.
3. First end-to-end domain task: a miniature culture built end-to-end and
   logged (SHONEN box 2).

## Saturation

Saturation line: score 8 on any axis. Stagnation window: 3 rounds without
a capability row.

## Retired

None.
