# kotodama-shokunin — SCORECARD

Axes per fleet `AXES.md` (depth, coverage, operability, freshness,
calibration, adjacency). Every score is a claim: it carries the counting
command and the commit it was measured against.

## Axes

| axis | score | evidence | counting command | measured against |
|---|---|---|---|---|
| depth | 6→7 | round 3: D2 culture built end-to-end from corpus; 15/15 components, gates graded, frozen outputs | `ls examples/culture-d2/components/*.yml \| wc -l` = 15; `test -f tools/gates/frozen/round-3/MANIFEST.tsv` | round-3 commit 2026-10-17 |
| coverage | 6 | 6 partitions; civilizations/ covers 92 bases | `ls corpus/knowledge/civilizations \| wc -l` = 92 | mint commit 49ac1a5 |
| operability | 3→5→6 | rounds 1+3: 6 gates + deterministic merger + sha256-pinned frozen-run manifests | `ls tools/gates/*.py \| wc -l` = 6; `for g in tools/gates/*.py; do python3 $g --selftest; done` all exit 0 | round-1 commit 2026-10-17 |
| freshness | 1→4 | rounds 1–3: 1258 → 612 raw sum (policy mentions inflate; 9 direct-resolved round 3); 5 civ files carried to round 5 | `grep -rc 'to-verify' corpus/knowledge --include='*.md' \| awk -F: '{s+=$2} END {print s}'` = 612 (raw) | round-3 commit 2026-10-17 |
| calibration | 6 | every entry carries a calibration section; 983 basis-carrying triage decisions (503/416/64) | `grep -h 'CONFIRM\|DOWNGRADE\|EXCISE' corpus/lessons/round-1-triage/*.md \| wc -l` = 983 | round-1 commit 2026-10-17 |
| adjacency | 4→5 | round 2: executable handoff path — sample packet passes the contract gate 16/16; L0 filed | `python3 tools/gates/handoff-packet-check.py examples/handoff-packet.sample.md` exit 0 | round-2 commit 2026-10-17 |

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
| culture packet assembly | deterministically merge culture components into a gate-readable packet | tools/assemble-d2.py --check exit 0; frozen/round-3/MANIFEST.tsv | round 3 |
| end-to-end culture build | design a full miniature culture from corpus tables and grade it with the gate battery | examples/culture-d2/ASSEMBLY.md; 7 frozen runs | round 3 |
| to-verify triage | resolve provenance flags with CONFIRM/DOWNGRADE/EXCISE ledgers | corpus/lessons/round-1-triage/ (42 fragments, 983 decisions) | round 1 |
| handoff packet verdict | grade a world-bible handoff packet against the integration contract (envelope, canon hygiene, glossary etymologies) | tools/gates/handoff-packet-check.py --selftest green; exit 0 over examples/handoff-packet.sample.md | round 2 |

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
