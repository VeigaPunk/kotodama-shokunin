# R19-D09 — SCORECARD.md integration draft (paste-ready, must be re-measured before pasting)

- round: 19 (operator: loop 2 of 3, build round 3 of 4; `reports/round-19/claims.json`,
  provider `hyper/deepseek-v4.1-flash` per the operator substitution). Lane:
  `kotodama-shokunin`.
- seat **R19-D09** (integration drafts). Date 2026-10-18 (stamps UTC). Baseline
  revision `e5718945a1ab0a0c3db955338d2cae77d68fd348`; declare `169c616`.
- canon: **NON-CANON integration draft.** Draft text for `SCORECARD.md`; it edits no
  byte of `SCORECARD.md`, `LOG.md`, `corpus/**`, `tools/**` or any filed round-8..18
  artifact. The parent owns placement, wording and admission.
- writes: this file, plus gitignored scratch under `.scratch/`. No commit, no push.
- Every number is a read-time pin of a live wave (2026-10-18T11:32–11:37Z, worktree
  dirty); re-measure on the settled tree. The thresholds quoted are the declared
  ones from `reports/round-19/claims.json`; no scalar rubric or relaxed threshold is
  introduced. The freshness axis-move pause stands, and the two round-11 ratios
  (147/189 comparable; 147/192 all-row) remain separate and un-reopened — never
  write "147/192 = 0.778".

## Draft SCORECARD.md block

```markdown
## Axes — round 19 (2026-10-18)

Declared thresholds: `reports/round-19/claims.json` (claims D/C/O); counting command
`python3 reports/round-19/run-validation.py` (assigned runner owner only). Baseline
`e5718945a1ab0a0c3db955338d2cae77d68fd348` (round-18 admit); declare `169c616`.
Delivered-tree commands, exact tested code hashes and results are persisted in
`reports/round-19/validation.json`.

| axis | verdict | before → after / observation | re-run command | measured evidence |
|---|---|---|---|---|
| depth | <verdict> (claim D) | D4 craft uncodified → the D4 lesson entry lands (routing shape, round-trip corruption class, derivation-replay discipline, register-class debt) and SKILL.md gains the D4-derived decision tables; every row cited to D4 artifacts or corpus paths | `python3 reports/round-19/run-validation.py`; `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | `reports/round-19/integration/d4-lessons-entry.md`; `reports/round-19/knowledge/skill-draft-{a,b}.md`; gate 19/19 over `packet.d4.yml` at `04ad4bb4…`; **SKILL.md still 0 D4 mentions at 11:37Z** |
| coverage | <verdict> (claim C) | verification 15 / synthesis 24 → >=8 new sourced entries (>=3 each), gap-named and frontmatter-complete; `corpus/README.md` reconciled | `python3 reports/round-19/run-validation.py`; `ls corpus/knowledge/verification \| wc -l` | verification 15 → **20**, synthesis 24 → **28** (11:37Z); `reports/round-19/gaps.md`; `reports/round-19/entries/R19-C11..C15.md`; README still `revision: 1.3` @ `9df4b7c5…` |
| operability | <verdict> (claim O) | battery baseline duty already **9/9** (the D4 baselines landed in-round); duty-1 selftests still the seven structural gates; no D4 gate ships a self-test; the D4 adapter selftest is red | `TMPDIR=/var/tmp/... python3 tools/check-gate-battery.py`; `python3 tools/check-gate-battery.py --selftest` | battery exit 0 `{pass: 7, fail: 0, unevaluable: 0}`, baseline `coverage 9/9`, `pinned 17` (11:37Z); **`python3 tools/assemble-d4-typed.py --selftest` exit 1 at `08784671…`** |
| freshness / adjacency | unchanged | Pause in force; scope clean | — | `reports/round-19/scope.md`, `reports/round-19/scope-a20.md` |
```

## Notes the parent needs before filling the verdicts

- **depth (claim D).** The craft entry is preserved at
  `reports/round-19/integration/d4-lessons-entry.md` because peer seat X21 also held
  the assigned `corpus/lessons/round-19.md` path and landed its gate-keeper survey
  there first; the D claim's "corpus/lessons gains the D4 lesson entry" is therefore
  **not satisfied at a settled path** until the parent picks one. `SKILL.md` read
  **0** D4 mentions at 11:37Z (digest `e8d238a6…`), so the decision tables were not
  placed at this seat's read.
- **coverage (claim C).** Counters were still moving at the last stamp
  (verification 15 → 20, synthesis 24 → 28); do not paste a counter measured before
  the wave settled, and do not arithmetic-guess the README total (the round-10
  receipt must not be silently rewritten — append a new dated block).
- **operability (claim O).** Two duties must be read separately. **Duty 2
  (baselines): already 9/9, 17 pinned** — the D4 `expected.json` baselines landed
  inside the census window, so the claim's `before`-text is superseded by the
  round's own artifacts. **Duty 1 (selftests): not met** — the battery runs the
  seven structural selftests only, neither D4 gate ships a self-test, and
  `tools/assemble-d4-typed.py --selftest` is red. A verdict filled from "9/9"
  alone would credit a leg that does not exist.
- **Two open D4 reds to disposition** (detail in
  `reports/round-19/integration/log-fragment.md` §3): the adapter selftest, and the
  gate over `packet.d4.typed.yml` reading 14/16 (`L3-routing-consistency`). The
  second bears on the proposed "record the round-18 pending frozen row" deliverable:
  that row's input is the typed packet, so freezing it now pins a red.
- **Admission line (draft, parent fills):** "Admission: <measurable claims verify /
  do not verify> and no tested axis is harmed. This does not prove arbitrary
  malformed-schema safety, cultural authenticity or untested behavior. Full
  protocol conformance and promotion remain open."
- **Historical checkpoint state.** Keep the existing SCORECARD preamble rules: the
  old 0–10 estimates have no reproducible mapping and stay historical in Git; a raw
  file or marker count is not a quality score; freshness is historically the lowest
  non-retired axis, not a newly computed scalar.
