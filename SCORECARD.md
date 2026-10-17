# kotodama-shokunin — SCORECARD

Axes per fleet `AXES.md` (depth, coverage, operability, freshness,
calibration, adjacency). Every score is a claim: it carries the counting
command and the commit it was measured against.

## Axes

| axis | score | evidence | counting command | measured against |
|---|---|---|---|---|
| depth | 6 | 176 entries with cited sources, decision tables, worked derivations | `find corpus/knowledge -name '*.md' \| wc -l` = 176 | mint commit 49ac1a5 |
| coverage | 6 | 6 partitions; civilizations/ covers 92 bases | `ls corpus/knowledge/civilizations \| wc -l` = 92 | mint commit 49ac1a5 |
| operability | 3→5 | round 1: 6 gates implemented (target ≥4), selftests green | `ls tools/gates/*.py \| wc -l` = 6; `for g in tools/gates/*.py; do python3 $g --selftest; done` all exit 0 | round-1 commit 2026-10-17 |
| freshness | 1→4 | round 1: to-verify flags 1258 → 795 (463 net; target 300) | `grep -rc 'to-verify' corpus/knowledge --include='*.md' \| awk -F: '{s+=$2} END {print s}'` | round-1 commit 2026-10-17 |
| calibration | 6 | every entry carries a calibration section; 983 basis-carrying triage decisions (503/416/64) | `grep -h 'CONFIRM\|DOWNGRADE\|EXCISE' corpus/lessons/round-1-triage/*.md \| wc -l` = 983 | round-1 commit 2026-10-17 |
| adjacency | 4 | synthesis/worldbible-integration-contract.md landed; handoff format defined | `test -f corpus/knowledge/synthesis/worldbible-integration-contract.md` | mint commit 49ac1a5 |

## Capabilities

| name | what it can now do | evidence | first-working round |
|---|---|---|---|
| corpus indexing | generate corpus/README.md from per-entry topic lines | corpus/README.md (176 entries indexed) | mint (operator dispatch) |
| provenance screening | enforce cited-source + to-verify + calibration discipline across batch authorship | 1258 flags + QUALITY.md bar | mint (operator dispatch) |
| phonology sanity verdict | grade a culture packet's sound system vs typology tables | tools/gates/phonology-sanity-gate.py --selftest green | round 1 |
| lexicon coverage verdict | grade semantic-field coverage + derivation discipline | tools/gates/lexicon-coverage-audit.py --selftest green | round 1 |
| myth consistency verdict | grade pantheon/motif/symbol coherence | tools/gates/myth-consistency-gate.py --selftest green | round 1 |
| costume-era consistency verdict | grade material/rank/era costume coherence | tools/gates/costume-era-consistency-gate.py --selftest green | round 1 |
| naming collision verdict | grade name uniqueness/pronounceability/derivation | tools/gates/naming-collision-gate.py --selftest green | round 1 |
| corpus provenance verdict | grade entry headers/sources/calibration + flag counts | tools/gates/provenance-audit.py --selftest green | round 1 |
| to-verify triage | resolve provenance flags with CONFIRM/DOWNGRADE/EXCISE ledgers | corpus/lessons/round-1-triage/ (42 fragments, 983 decisions) | round 1 |

## Planned (next rounds)

2. Freshness: triage the remaining ~795 flags incl. the 15 carried-over
   batches (token-plan key 3 first; chunk-read instruction from the first
   message).
3. Operability/depth: first end-to-end domain task executed by the lane
   itself — a miniature culture packet built and passed through all six
   gates (SHONEN box 2); frozen two-evidence runs per the gate standard.
4. Depth: SKILL.md decision tables deepened from synthesis/ + gap closure
   per corpus/README.md frontier.

## Saturation

Saturation line: score 8 on any axis. Stagnation window: 3 rounds without
a capability row.

## Retired

None.
