# Round 7 — 01 PLANNER + CONNECTOR plan review

Date: 2026-10-17. Scope: this file only. No contract, component, tool, or
bookkeeping file was changed; all work below is read-only verification plus
this report. Baseline revision confirmed at HEAD `30caac66a2a382f1c46ba31f0c3c93da62d0762c`.

Inputs read: MISSION.md, AXES.md, AGENTS.md, PROVINCE.md,
reports/round-7/{claims.json,d3-contract.json,targets.json,baseline.json,dispatch-plan.json},
reports/round-6/parent-reconciliation.json, corpus/lessons/round-6-sources/{05,03,13,09}.json,
tools/assemble-d2.py, tools/gates/{costume-era-consistency,naming-collision}-gate.py,
examples/handoff-packet.sample.md, corpus/knowledge/synthesis/worldbible-integration-contract.md,
landed components 04/05/07.

## Verdict summary

- No contract-level blocker found. Two real findings: one cross-surface gap
  (legacy projection key mapping — G1) and one blocker-class process gap
  (unowned counting command — G2). One guard-implementation landmine (G3) and
  one compatible simplification (S1). Everything else verified conformant.
- Component 06, both tools, packet, controls, expected.json, handoff and README
  are absent at review time (mid-swarm). They are **unreviewed, not predicted
  green**; parent can resume owners per dispatch-plan.

## G1 — Cross-surface gap: legacy key mapping can silently kill the expected red

d3-contract.json `legacy_projection` says "materials gate_name and routes".
The costume gate does **not** read a `gate_name` key:

- Base keys: `name, eras, costumes[{garment, material, wearer_rank, rite, era}]`
  — tools/gates/costume-era-consistency-gate.py:47.
- Material identity resolves from `entry.get("material") or entry.get("name")`
  — costume-era-consistency-gate.py:435; costume→material linkage reads the
  costume's `material` value — costume-era-consistency-gate.py:675.
- D2 canonical shape: costumes `material: wool`, materials `name: wool` —
  tools/assemble-d2.py:257–272.

If the assembler emits D3-native keys (`gate_name`, `material_id`) into
packet.gates.yml, C03 stops matching RR1's `property.value` ("plant-cloth"):
R-01 (the expected note/exit-1 red) and the era/route checks fire differently
or not at all — a silent loss of the expected red, i.e. a false green.

Minimal fix (no contract change needed; it is a reading of d3-contract.json
line 71): owner 03 must map the **value** `gate_name` into legacy keys —
`materials[].name` = gate_name, `costumes[].material` = the material's
gate_name — and keep `garment` = native_form, never a display label.
Reviewer 15 should assert the C03 legacy row is exactly
`{garment: mila, material: plant-cloth, wearer_rank: visitor, rite: assembly,
era: E1}` (+place if the row carries it) so R-01/EAR-01 stay load-bearing.

## G2 — Blocker-class process gap: counting command has no owner

claims.json gives `python3 reports/round-7/run-validation.py` as the
counting command for **both** claims F and O (claims.json:12). No dispatch
item 01–16 owns that file. Precedent: reports/round-6/run-validation.py exists
as a parent-integration surface (alongside validation.json/checkpoint.json).

Minimal fix: parent declares and writes reports/round-7/run-validation.py at
integration (mirroring the round-6 runner: freeze inputs, count the five F
ledgers/passage criteria/parent refetch receipts, run the O command battery).
Workers must not create it — it would collide with parent integration. Until
it exists, neither claim is measurable even after all artifacts land.

## G3 — Guard landmine: D3-SCOPE must compare against *effective* labels, not raw ledgers

The raw round-6 records differ from the effective reconciliation rows:

- R6-05-A raw `source_kind` = "repository-scholarship"
  (corpus/lessons/round-6-sources/05.json:17) vs effective
  "secondary-scholarly" (reports/round-6/parent-reconciliation.json:26).
- R6-13-A raw url ≠ effective pinned-archive `effective_source_url`
  (parent-reconciliation.json:42); R6-09-A carries an
  `effective_source_locator` override (parent-reconciliation.json:34).

Owner 07 handled this correctly (S01–S05 verified below). But if guard owner
02 implements D3-SCOPE by comparing references to the **raw** ledger fields,
the committed positive packet false-fails on S01's kind and S03's URL. The
closed expected table must be: raw ledger values overridden by the
reconciliation row's `effective_*` fields. Also note `audit_id` in
source_bindings matches `audits[].id` inside each ledger
(round-6-sources/05.json:9), not a top-level field.

## S1 — Compatible simplification: reuse the D2 concat-rule dialect

For the six synthesized legacy replay rules, reuse the existing UP-COMPOUND
shape rather than inventing a new one: `{id, kind: compound, pattern:
'^(?P<B1><escaped E1 base 1>)[+](?P<B2><escaped E1 base 2>)$', output:
'{B1}{B2}'}` (tools/assemble-d2.py:193–196) with each legacy name carrying
`formation: {stem: "<b1>+<b2>", rule: <id>}`. The naming gate's replay path
(tools/gates/naming-collision-gate.py:1170–1266) then replays all six rules
with zero new dialect and no DERIV-HOLD/DERIV-AFFIX noise, keeping CROSS-HOLD
(HOLD → exit 1, naming-collision-gate.py:49,1543) as the sole expected
naming red, exactly as the contract requires. `yaml_lines(value, indent=0)`
(assemble-d2.py:72) is confirmed reusable read-only.

## Verification performed (all pass)

Commands: `sha256sum` over the six pinned files; a read-only python3
cross-check recomputing SC1/concat and validating components 04/05/07 against
the contract, baseline.json, actual ledger bytes and the reconciliation rows.

- All six reference hashes byte-match baseline.json (`reference_sha256`).
- Component 04: exactly 20 lexemes L01–L20; 4 initial-p (L01,L04,L05,L06),
  16 unchanged; SC1 recompute mismatches: 0; syllabification violations
  (corrected checker, (C)V(C) coda∈{n,l,r,s}) across lexicon E0/E1, all six
  names, all utterance forms: 0; E0 anchors exactly pina/suma/talu +
  nara/salu/mila/kuru; six names concat-recompute exactly, mutually distinct,
  distinct from all lexeme forms; U01 fina/pina, U02 suma/pina (AV1
  substitution of L02's E0 form), U03/U04 talu — utterance law exact.
- Component 05: AV1 byte-exact per contract; NR1 allowed_offsets [2,8,20],
  chosen 8, status constructed-not-historical; B01/B02 attributed, disagreeing,
  truth_status unresolved; SY01/SY02 have audience and era E1.
- Component 07: S01–S05 ledger_path/audit_id/support_scope match the closed
  bindings; `file_sha256` equals actual ledger bytes; `source_kind` equals the
  **effective** reconciliation kind for all five; `source_url` equals the
  effective URL for all five (S03 correctly carries the pinned archive
  override, not the raw url); canon NON-CANON, handoff prepared-not-accepted,
  screening unresolved with sweep=false; BR01–BR05 target existing D3 ids with
  design-only relations; component top-level key sets exactly per contract.
- Expected-red legacy checks: R-01 note finding exists
  (costume-era-consistency-gate.py:104,943,1490) and any finding ⇒ exit 1
  (EXIT_FINDINGS=1, :135–136,1081) — "C03 R-01 note/exit1" is real;
  CROSS-HOLD HOLD → exit 1 (naming-collision-gate.py:49,1543); RR1 matches
  the gate's documented rank_rules schema (:65–67). Handoff envelope: the
  contract §4 table is exactly 16 fields
  (worldbible-integration-contract.md:46–63) and the sample carries all of
  them; controls count ">=12 (prefer 14 domain ids) + 4 malformed + >=2
  positive" is consistent across contract, claims and dispatch item 13.
  Lexicon list is ordered L01..L20 (L17 at index 16), so owner 13's
  JSON-pointer patch paths are stable.
- Native-vs-display: display labels are separate fields throughout component
  04; the historical failure class is on record — round-4 frozen red
  PHON-INVENTORY fired because a display label was sent to phonology
  (tools/gates/frozen/round-4/naming-collision-gate.out:8) — the contract's
  "names native_form only" + "no English display labels as garment names"
  rules directly prevent recurrence; G1 is the remaining way to lose that
  guarantee.

## Named checklist areas

- native-vs-display: verified clean (see above; watch G1 on the legacy side).
- source-support-vs-invention: verified clean end-to-end (hashes, effective
  labels/kinds/URLs, unresolved screening, design-only bridges); guard must
  implement the effective table (G3).
- ritual surface / worn item: contract-consistent (O01 ground-surface
  worn=false vs O04 worn attachment; D3-OBJECT covers exactly this); component
  06 absent at review time, so the actual worn/object data is **unreviewed**.
- ordinary change/avoidance: verified clean (SC1 ordinary-only recompute; E0
  retained in ritual/written layer; AV1 exactly one substitution; U03/U04 no
  trigger).
- expected-red legacy checks: expectation confirmed real (R-01 note/exit1,
  CROSS-HOLD exit1); G1 is the one implementation risk that could silence
  them.

## Harms

None. Only this file was written; no shared bookkeeping, contract, tool, or
component was touched. Open items for parent: G1 (brief owner 03 / reviewer
15), G2 (parent owns run-validation.py), G3 (brief owner 02). No live source
research was redone; the five F re-fetches remain with scouts 08–12.
