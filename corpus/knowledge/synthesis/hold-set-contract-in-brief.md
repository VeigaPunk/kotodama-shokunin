# Hold-set contract in the brief — declaring expected findings before implementation

- topic: The design workflow for writing a **hold-set declaration into a culture brief**: before any packet exists, the brief names the finding set the typed pipeline is expected to emit (ids, severities, where-keys, and a reason per row), fixes the artifact contract the set is declared against, and states that the expected set is design debt, never a clearance. Covers the declaration's place in the brief, the fields it owes, how it is used as a prior by verification, and the discipline that keeps a declaration from becoming a target. Reference method and design workflow only; canon belongs to lore-shokunin.
- gap filled: the synthesis partition carries the brief/blueprint template (`conlang-blueprint-template.md`) and the coupling model, but no entry states the **hold-set declaration as a design contract** — the expected finding set named in the brief before implementation. Absence sweep 2026-10-18: `grep -rln "hold_set_declaration\|hold set\|expected finding" corpus/knowledge/synthesis/` → 0 files; the concept lives only in the D4 brief and `reports/round-18/d4/holds.md`.
- sources:
  - KTD-HB-S-0001 — `examples/culture-d4/components/01-brief.yml` `contract.hold_set_declaration` (read in `examples/culture-d4/brief.md` §"Named hold set (pre-implementation)"): the declaration made **before the packet existed** — 6 holds / 0 notes / 0 fails, `D4L-FORM-UNRESOLVED` at `GAR-01`…`GAR-06`, one per owed form slot. NON-CANON drill artifact.
  - KTD-HB-S-0002 — `reports/round-18/d4/holds.md` §0–§6: the reconciliation of the declared set against the emitted set and two other pre-declarations, with every delta dispositioned (6 union rows keyed to absent records; 11 union rows with no delivered trigger; +9 hold / +1 note against the delivered declaration). The receipt that shows what a declaration buys.
  - KTD-HB-S-0003 — `examples/culture-d4/brief.md` §"Named hold set": the explicit statement that the holds are “open design debt, never a clearance”.
  - KTD-HB-S-0004 — measured this round, 2026-10-18, lane root, `export TMPDIR=$PWD/.scratch`: `python3 tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml --json` → exit 1, `stats {"fail": 0, "hold": 15, "labels": 74, "note": 1}`; `examples/culture-d4/expected-holds.json` → `counts {hold 15, note 1, fail 0}`. The emitted set is larger than the declared one, and the delta is the interesting evidence.
  - KTD-HB-S-0005 — `corpus/knowledge/synthesis/conlang-blueprint-template.md` §0 (brief, scope, and reference passport; the fill-in rows and gate G0) and `corpus/knowledge/synthesis/coupling-model.md` §1/§5 (interderive constraints; exercise the coupled output rather than describe it). These fix the brief's shape; this entry adds the declaration section it lacks.
  - KTD-HB-S-0006 — `corpus/knowledge/verification/pre-declared-hold-set-reconciliation.md` (this lane, round 19): the verification-side reconciliation procedure. The brief's declaration is the prior that procedure consumes; a design that does not declare cannot be reconciled.
  - KTD-HB-S-0007 — `corpus/knowledge/verification/verification-independence-anti-circularity.md` §3 (`claim ≠ anchor`: an artifact's self-description is not a measurement taken outside it) and `corpus/knowledge/verification/gate-frozen-run-standard.md` §2 (a committed expected verdict makes a later hand-edit contradict the run). The reason the declaration must predate the artifact.
  - KTD-HB-S-0008 — Reproducible Builds project documentation, [reproducible-builds.org/docs/](https://reproducible-builds.org/docs/) (accessed 2026-10-18). Expectation-first, deterministic checking; cited as the discipline, not as a claim about content.
- calibration: the declaration discipline is this lane's house policy, not a published standard; the Reproducible Builds documentation is cited for expectation-first deterministic checking; the D4 declared and emitted counts are NON-CANON drill records, not a universal expectation.
- couples: synthesis — `conlang-blueprint-template.md`, `coupling-model.md`, `generated-artifact-lifecycle.md`, `typed-label-routing-workflow.md`, `worldbible-integration-contract.md`, `finding-disposition-workflow.md`; verification — `../verification/pre-declared-hold-set-reconciliation.md`, `../verification/gate-frozen-run-standard.md`, `../verification/verification-independence-anti-circularity.md`; tooling — `tools/d2-typed-labels.py`, `examples/culture-d4/expected-holds.json`, `examples/culture-d4/components/01-brief.yml`; siblings — lore-shokunin owns canon; chousa-shokunin owns general research method.
- source: the D4 pre-declaration record, the round-18 reconciliation receipt, and this round's re-measurement of the emitted and committed sets; the declaration discipline is this lane's house method, not findings attributed to the cited works.
- verified-at: 2026-10-18 — re-measured at HEAD `169c616`, lane root, `export TMPDIR=$PWD/.scratch`: projector run exit 1 with `stats {fail 0, hold 15, labels 74, note 1}`; `expected-holds.json` read → `counts {hold 15, note 1, fail 0}`. Header fields and cross-reference targets checked for resolution; all cited repo paths exist. The declaration text was read from the committed brief; the round-18 receipt was read by path.
- recheck: whenever the brief template, the projector, the packet, or `expected-holds.json` changes; before treating a declared set as a target; and whenever a declaration is amended (corrections are new files, never in-place rewrites).

## 1. What this workflow licenses

- A **brief section and its discipline**, not a gate. It tells a designer what to declare before implementation and how the declaration is used downstream.
- The declaration's entire evidentiary value is its **timestamp**: a set written before the artifact can distinguish “the pipeline works” from “the output was written down”.
- A declared set is a **prior, not a quota**: the measured D4 case emitted 15 holds + 1 note against a 6-hold declaration, and the delta — not the match — is what the round learned.

## 2. Where the declaration lives, and what it owes

The declaration is a subsection of the brief's contract block
(`contract.hold_set_declaration`), written with the seed and the spine, before any
component is authored. It owes:

| field | required contents | why the brief must carry it |
|---|---|---|
| set id + contract basis | the ids and severities expected, plus the artifact contract they are declared against (packet fields, projection schema) | a set declared against nothing is a wish |
| where-keys | the record keys the findings are expected to land on (`GAR-01`…`GAR-06`) | the reconciliation matches on `(id, severity, where)`, not prose |
| counts | expected `fail` / `hold` / `note` totals | the first reconciliation row; a count-only match is not a set match |
| reason per row | why this finding is expected rather than a defect | separates known debt from a tolerated bug |
| pre-implementation stamp | date and revision the declaration was written at | the declaration's whole value is that it predates the artifact |
| non-clearance clause | an explicit “debt, never a clearance” statement | stops the declaration becoming a target |

## 3. The declaration as a prior for verification

- Verification consumes the declaration via
  `../verification/pre-declared-hold-set-reconciliation.md`: declared vs emitted,
  row by row, with deltas classified (emitted-extra, emitted-missing,
  severity-drift, union-untriggered).
- A declaration that names too little is visible as **D-EMITTED-EXTRA** (the D4
  case: +9 holds, +1 note). That is not a failure of the declaration; it is the
  declaration doing its job by making the excess visible.
- A declaration that names a row the pipeline cannot emit is visible as
  **D-EMITTED-MISSING** — the declared debt is shown unmeasured, which is the
  reading a green run would otherwise hide.
- Consequence for the designer: write the declaration **narrowly and honestly**.
  An inflated declaration turns into a self-fulfilling quota; an absent one
  turns every emitted finding into an unexplained surprise.

## 4. What the declaration never licenses

- **A declared set is not a target.** If it is treated as the thing to hit, an over-firing pipeline becomes invisible.
- **A match is not a pass.** A matched set says the run did what was declared; the declared set may itself be wrong or thin.
- **A hold is not approval.** Every declared hold is open design debt, handed off as such (`examples/culture-d4/brief.md`).
- **A declaration is not canon.** It says what the pipeline is expected to report about a design, not what is true in any world.

## 5. Reviewer checklist

1. Confirm the declaration exists in the brief's contract block and carries the six fields of §2.
2. Confirm its stamp predates the packet; a set written after the run is inadmissible.
3. Confirm the per-row reasons distinguish debt from tolerated bugs.
4. Confirm the non-clearance clause is present and is not contradicted elsewhere in the brief.
5. Hand the declaration to the reconciliation procedure and expect deltas; a perfect match on a first run is itself worth questioning.

## 6. Decision record — the declaration rules this workflow adopts

1. **Adopted:** the brief declares the expected finding set before implementation, with where-keys, per-row reasons, and a stamp (§2). Consequence: a set written after the run is inadmissible on its timestamp, not its content.
2. **Adopted:** the declaration is consumed as a **prior** by the reconciliation procedure, and its deltas are the evidence (§3). Consequence: an over-firing pipeline shows up as emitted-extra rather than as an unexplained finding.
3. **Adopted:** the declaration carries an explicit non-clearance clause and is handed off as open design debt (§4). Consequence: a hold is never read as approval.
4. **Adopted:** a corrected declaration is a **new** file with its own stamp (§2; consistent with `../verification/provenance-audit-ledger-format.md` §8). Consequence: the declaration history is append-only.
5. **Rejected:** writing the declaration after the artifact to make it match. Reason: it can only bless the run (§1; `claim ≠ anchor`).
6. **Open (to-verify):** whether a brief should declare a *band* (expected holds between N and M) rather than an exact set, given the measured +9/+1 delta on the first D4 run. Owner: this lane's D axis; not disposed here.
