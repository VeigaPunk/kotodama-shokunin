# R23-D02 — paired controls (draft pass)

- Seat: D R23-D02 (rule drafter 2 of 3). Date: 2026-10-18.
- Axes: depth (data isolation vs dependency isolation), operability
  (fail-closed controls), calibration (no clearance from equality).
- Scope: draft contribution only; no source, gate, SKILL.md, or filed-round
  writes. Consolidated output: `reports/round-23/rule/skill-draft.md` §1
  (control table + T2/T3).

## Contribution: design control → landed control mapping

All seven controls required by `reports/round-22/bleed/design.md`
§Required paired controls (`:32-42`) have landed embedded counterparts in
`_selftest_family` (`tools/d2-typed-labels.py:2980`), inside the 163/163
selftest recorded at `reports/round-22/bleed/impl.md:54,70`. Control labels
verified by `grep -n 'check("boundary\|check("family'`, 2026-10-18:

| Design control (design.md §) | Landed control label (line) |
|---|---|
| D2 compatibility (`:36`) | `boundary compatibility: D2 projection keeps its exact baseline digest` (`:3114`); `boundary D2 control: D2 rank projection remains enabled and responds to D2 mutation` (`:3119`) |
| D4 independence (`:37`) | `boundary: packet-only D4 mirror is byte-identical without a foreign tree` (`:3045`); `boundary poison control: D4 never calls embedded D2 fixture machinery` (`:3053-3054`); pre-fix artifact refused `P-FAMILY-SOURCE … GAR-01.owner: foreign owner '11-costumes'` (`reports/round-22/bleed/impl.md:64`) |
| Not empty-by-default (`:38`) | `boundary local control: RK-01 authority/property/rank follow the local packet only` (`:3063`); `boundary coverage control: … local row counted exactly once` (`:3073`); `boundary malformed local rank set … fails closed` (`:3099`) |
| Owner-qualified citations (`:39`) | `boundary control: deterministic D2-owned label metadata is rejected` (`:3011`); `boundary control: foreign label … rejected` (`:3024`); `boundary: D4 WR writing ids and shared engine references are not substring-banned` (`:3032`) |
| No ID-based reinterpretation (`:40`) | `boundary explicit same-id foreign label: emit refuses and preserves … output` (`:3109`) |
| Honest borrowed language (`:41`) | `boundary: label texts, kinds, owed slots and all six borrow ledgers unchanged` (`:2989`); normative rows `D2B-01..04` at `examples/culture-d4/components/01-brief.yml:111-121` |
| Propagation/tamper (`:42`) | `carry_findings` consumer coupling (`tools/assemble-d4-typed.py:276-288`); frozen generation `tools/gates/frozen/round-22/d4-repin/MANIFEST.tsv` (3 rows, exit 0) with deployed replay 33 peer pairs, `--require-live`, 2026-10-18T14:56:01Z (`reports/round-22/bleed/evidence/deployed-replay.json`); profile row + `repin_history[2]` in `tools/gates/typed-pipelines.json`; stale-pin refusal exit 2 `L1-profile` (`reports/round-22/bleed/impl.md:60`) |

## Review findings

- **F1 (no design-only controls remain).** Every control the design required
  exists as an executed embedded control; the draft's table cites landed
  lines, not prospective work. This is what lets the SKILL subsection state
  the controls in present tense.
- **F2 (the asymmetry is the point).** The mirror control (`:3045`) alone
  proves dependency isolation only — the C3 sentinel probe
  (`reports/round-22/bleed/analysis.md:103-110`) showed the foreign ledger is
  embedded and reachable with every disk reader disabled. Data isolation needs
  the poison half (`:3053-3054`) **and** the local-mutation half (`:3063`):
  poison proves the family never calls the fixture machinery; the RK-01
  mutation proves local declarations actually drive the projection. A fix that
  passes either half alone can still be cosmetic (empty-by-default) or
  globally disabled — T3 of the draft encodes this.
- **F3 (anti-global-disable teeth).** The pair `:3114` + `:3119` is what
  defeats "compatibility by disabling rank projection everywhere": D2 keeps
  its exact baseline digest **and** still responds to a D2-side rank mutation.
  Both directions are needed; cite them together.
- **F4 (tamper leg is frozen, not asserted).** The propagation control's
  evidence is the landed frozen generation and the deployed replay (33 peer
  pairs, live peers checked), plus the measured stale-pin refusal. The draft
  cites receipts with dates rather than restating counts as its own claims.
- **F5 (labels, not APIs).** The "Landed control" citations are matched
  substring labels at current line numbers; a selftest refactor moves them.
  Update such citations as a new rule revision — never weaken the
  paired-control wording to keep stale lines green.

## Verification record (all 2026-10-18, read-only)

- `grep -n 'check("boundary\|check("family' tools/d2-typed-labels.py` — the
  control labels/lines above; `grep -c "P-FAMILY-SOURCE\|P-FAMILY-RANK"` → 25
  refusal sites.
- `head -4 tools/gates/frozen/round-22/d4-repin/MANIFEST.tsv` — header + 3
  rows, exit 0.
- `python3 -c` JSON reads: `typed-pipelines.json` profile/repin digests;
  `deployed-replay.json` (33 pairs, 14:56:01Z); `expected-holds.json` counts.

Status: draft pass complete; no gate run by this seat.
