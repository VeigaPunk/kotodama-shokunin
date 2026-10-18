# Round-24 cold-run consolidation (claim O)

Consolidated from the seat fragments by the integrator; fragments remain the
primary evidence. Breaks were found and dispositioned — this is NOT a no-breaks run.

seat: A
seat: B
seat: four
seat: fixer

## Executed commands (extracted from the seat fragments)

- `python3 tools/check-gate-battery.py`
- `python3 tools/d2-typed-labels.py --selftest`
- `python3 tools/assemble-d2.py --check`
- `python3 tools/assemble-culture-d3.py --check`
- `python3 tools/assemble-culture-d4.py --check`
- `python3 tools/assemble-d4-typed.py --selftest`
- `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml`
- `python3 tools/gates/typed-pipeline-gate.py`
- `python3 tools/exercise-handoff-e2e.py --profile v3`
- `python3 tools/exercise-handoff-e2e.py --profile v2`
- `python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv`

## Findings (all dispositioned in the fragments)

- F1 (break, major): SKILL.md:501 battery row inverted — fixed by F3 with controls (reports/round-24/audit-fixes.md, dated 2026-10-18).
- F2 (break): d4-repin replay needs TMPDIR outside the repo — precondition documented by fixer fix 5.
- F3 (break): round-5/6/7 run-validation.py exit 1 undocumented — named condition N-class.
- F4 (hazard): those scripts overwrite filed receipts in place — condition (receipt-guard class).
- F5 (break): D4 gate input unnamed (typed packet input = false red) — condition N2, fix drafted.
- F6 (ambiguity): prose checklist 1-of-4 executable — declared in-tree by fixer.
- F7 (break): stray code fences — fixed F8 by the audit fixer.

## Result
All documented steady states reproduce; seven box-3 conditions named in
cold-run-conditions.md; seven wording-level SKILL.md fixes landed with controls.
