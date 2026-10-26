# Round 4 lessons (2026-10-17) — sol-max round: fixes, audits, and target discipline

## What moved

D2 v1.1: myth MC-S00 (symbol mediums) and costume G-ERA (era retag with
declared map) eliminated entirely; phonology findings reanalyzed honestly
(gate still flags its 3 REVIEWs — expected); naming 20 → 18. Gate battery
re-run unchanged: selftests green, fixture bytes untouched — no gate was
weakened to buy findings (verified `git status` over tools/gates/).
Corpus: africa-primary-sources landed (179 entries); corpus/README.md
regenerated (revision 1.1); 17 audit reports under round-4-audit/
(header/calibration/flag-basis apparatus checks across all 148 seeded
entries + gap entries). Triage: gap-entry flags 33 → 11 with a 60-row
ledger.

## The target-setting fallacy (calibration — orchestrator-owned)

Rounds 2 and 4 were both rejected with claims falsified *as declared*
while every axis improved in fact. The error is mine: I set targets by
aspiration (≤10 findings, ≥25 flags) instead of by measured rate (one
finding-class per round ≈ 2 classes; flag resolution ≈ 20–25/agent-hour).
Rule going forward: a round's target must cite the measurement it is
extrapolated from, and 'improved in fact but below target' is recorded as
a falsified claim, never silently re-based.

## Named residual work (round-5+ queue)

- PHON-INVENTORY ×10 in naming-collision: suspect class — either real
  coda/segment violations in 05/13 or an encoding mismatch (accent marks /
  long-vowel digraphs read as unknown segments). Diagnose before fixing.
- DERIV-REPLAY ×8: component 03 now carries explicit regex rules that the
  naming gate cannot replay — the gate needs a derivation adapter (or the
  assembler needs to materialize derived forms into the packet).
- CROSS-HOLD ×1: real-language sweep stays a declared pre-publication gap.
- 11 retained gap flags + 5 civ files (39 flags) → round 5 (zai lane).
