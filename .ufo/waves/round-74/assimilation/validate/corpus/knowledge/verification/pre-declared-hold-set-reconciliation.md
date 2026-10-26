# Pre-declared hold-set reconciliation — naming the expected findings before the artifact exists

- topic: The verification procedure for **pre-declared expected finding sets**: a designer names, before implementation, the exact finding set a gate or projector is expected to emit (ids, severities, where-keys); the run emits its set; the two are reconciled row by row and every delta is dispositioned. Covers the declaration record, the three-way reconciliation (design union / delivered declaration / emitted set), delta classes, and the rule that a reconciled set is debt, never a clearance. Method and lane policy only; canon belongs to lore-shokunin.
- gap filled: the partition carries frozen-run verification (`gate-frozen-run-standard.md`) and the re-pin record (`verification-independence-anti-circularity.md`), but no entry covers **pre-declaring the expected finding set before the artifact exists** and reconciling the emitted set against it with each delta dispositioned. Absence sweep 2026-10-18: `grep -rln "hold set\|hold_set_declaration\|pre-declared" corpus/knowledge/verification/` → 0 files; the concept lives only in the D4 drill (`examples/culture-d4/components/01-brief.yml`) and `reports/round-18/d4/holds.md`.
- sources:
  - KTD-HS-S-0001 — `examples/culture-d4/components/01-brief.yml` `contract.hold_set_declaration` (read in `examples/culture-d4/brief.md` §"Named hold set (pre-implementation)"): the declaration made **before the packet existed** — 6 holds / 0 notes / 0 fails, `D4L-FORM-UNRESOLVED` at `GAR-01`…`GAR-06`. NON-CANON drill artifact.
  - KTD-HS-S-0002 — `examples/culture-d4/expected-holds.json` (sha256 `09490a2756d123ebbc2023be89fc01c95ec2f8cc7e6df42ecc5b8cd438058e98`, schema `kotodama-typed-pipeline-holds-v1`): the committed hold set pinned to delivered bytes — `counts {hold 15, note 1, fail 0}`, with `packet_sha256` `e7ecd204…` and `projection_sha256` `a59990bb…`.
  - KTD-HS-S-0003 — `reports/round-18/d4/holds.md` §0–§6: the extraction of the emitted set from `tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml --json` and the reconciliation against **three** pre-declared sets — the round-17 design-doc union (17 holds + 1 note), the delivered tree's own `01-brief.yml` declaration (6/0/0), and the emitted set (15 holds + 1 note). Deltas: 6 union rows keyed to records the delivered tree does not carry; 11 union rows with no delivered trigger and no engine path; +9 hold / +1 note against the delivered declaration.
  - KTD-HS-S-0004 — measured this round, 2026-10-18, lane root, `export TMPDIR=$PWD/.scratch`: `python3 tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml --json` → exit 1, `stats {"fail": 0, "hold": 15, "labels": 74, "note": 1}`; the committed file read back → `{'hold': 15, 'note': 1, 'fail': 0}`. The emitted set and the committed set agree on the counts.
  - KTD-HS-S-0005 — `corpus/knowledge/verification/verification-method-overview.md` §3 (minimal claim card: “test and expected result … a failing case fixed before review”) and §6 (fail-closed verdicts); `corpus/knowledge/verification/gate-frozen-run-standard.md` §2–§3 (a committed expected verdict and a digest pin make a later hand-edit contradict the run). These give the record shape; this entry supplies the pre-declaration step they assume.
  - KTD-HS-S-0006 — `corpus/knowledge/verification/verification-independence-anti-circularity.md` §3 (`claim ≠ anchor`: an artifact's self-description is not a measurement taken outside it). The reason the declaration is written *before* the artifact: a set written after the run can only bless it.
  - KTD-HS-S-0007 — Reproducible Builds project documentation, [reproducible-builds.org/docs/](https://reproducible-builds.org/docs/) (accessed 2026-10-18). A declared, deterministic expectation is what lets a stranger reproduce a verdict; cited for the expectation-first discipline, not as a claim about content.
  - KTD-HS-S-0008 — Edsger W. Dijkstra (1972), “The Humble Programmer,” *Communications of the ACM* 15(10): 859–866, doi:10.1145/355604.361591. A green run shows the presence, never the absence, of defects — why a matched set is bounded evidence, not clearance.
- calibration: the reconciliation procedure is this lane's house policy, not a published standard; the cited works (Dijkstra; Reproducible Builds) are engineering references used as design rules, never as historical evidence; the D4 declaration and hold counts are NON-CANON drill records.
- couples: verification — `verification-method-overview.md`, `gate-frozen-run-standard.md`, `verification-independence-anti-circularity.md`, `provenance-audit-ledger-format.md`, `to-verify-triage-protocol.md`; synthesis — `../synthesis/hold-set-contract-in-brief.md`, `../synthesis/finding-disposition-workflow.md`, `../synthesis/generated-artifact-lifecycle.md`; tooling — `tools/d2-typed-labels.py`, `tools/gates/d4-typed-labels-check-gate.py`, `tools/gates/typed-pipeline-gate.py`, `examples/culture-d4/expected-holds.json`; siblings — lore-shokunin owns canon; chousa-shokunin owns general research method.
- source: the D4 pre-declaration record, the round-18 reconciliation receipt, and this round's re-measurement of the emitted and committed sets; the reconciliation procedure is this lane's house method, not a finding attributed to the cited works.
- verified-at: 2026-10-18 — re-measured at HEAD `169c616`, lane root, `export TMPDIR=$PWD/.scratch`: projector run exit 1 with `stats {fail 0, hold 15, labels 74, note 1}`; `examples/culture-d4/expected-holds.json` read → `counts {hold 15, note 1, fail 0}`. Header fields and cross-reference targets checked for resolution; all cited repo paths exist. The round-18 reconciliation receipt was read by path, not re-executed; the declared-set text was read from the committed brief.
- recheck: whenever the declaration, the projector, the packet, or `expected-holds.json` changes; before quoting any hold count into a handoff; and before carrying a “matched set” line as though it were a clearance (corrections are new entries, never rewrites).

## 1. What this entry licenses

- A **reconciliation procedure**, not a pass/fail oracle: it tells a reviewer how to compare a declared expectation with an emitted set and how to dispose of each difference. It does not decide whether the findings themselves are acceptable.
- Pre-declaration is a **failure-source separation**: a set declared after the run cannot distinguish “the engine works” from “the engine's output was written down”. The declaration's only value is that it existed before the artifact.
- A reconciled set is **debt, not clearance**: the measured D4 set is 15 holds + 1 note + 0 fails, and every hold is open design debt (`examples/culture-d4/brief.md`).

## 2. The declaration record

A hold-set declaration is admissible when it carries, before implementation:

| field | required contents | why |
|---|---|---|
| set id + digest basis | the ids and severities expected, plus the artifact contract they are declared against (packet fields, projection schema) | a set declared against nothing is a wish |
| where-keys | the record keys the findings are expected to land on (`GAR-01`…`GAR-06`) | lets the reconciliation match on `(id, severity, where)`, not on prose |
| counts | expected `fail` / `hold` / `note` totals | the first reconciliation row; a count-only match is not a set match |
| reason per expected row | why this finding is expected rather than a defect | separates “known debt” from “tolerated bug” |
| pre-implementation stamp | date and the revision at which the declaration was written | the declaration's whole evidentiary value is its timestamp |
| non-clearance clause | an explicit statement that the expected set is debt, never a pass | prevents the declaration from becoming a target to hit |

## 3. The three-way reconciliation

A single declared set is not enough when more than one pre-declaration exists.
The measured D4 case reconciles three, and a two-way comparison would have hidden
the interesting deltas.

| comparison | declared | emitted | delta class | disposition |
|---|---|---|---|---|
| delivered declaration vs emitted | 6 holds / 0 notes / 0 fails | 15 holds / 1 note / 0 fails | **+9 hold, +1 note** | engine path emits findings the delivered brief did not enumerate; each delta row is listed and its trigger named (`reports/round-18/d4/holds.md`) |
| design-doc union vs emitted | 17 holds + 1 note | 15 holds + 1 note | 6 rows keyed to records the delivered tree does not carry; 11 rows with no delivered trigger and no engine path | union rows are **not** silently dropped; each is marked “no delivered trigger” |
| committed `expected-holds.json` vs live projector | 15/1/0 | 15/1/0 | none | the committed set is the projector's own deterministic build, re-checked by `--check` |

Delta classes, named:

- **D-EMITTED-EXTRA** — the run emits a row the declaration does not name. Disposition: either the declaration was incomplete (fix the declaration as a *new* file) or the run over-fires (a finding against the engine). Never absorbed silently.
- **D-EMITTED-MISSING** — the declaration names a row the run does not emit. Disposition: the trigger did not fire (a packet defect) or the engine has no path to it (a coverage gap). This is the class that reads “green” while the declared debt is unmeasured.
- **D-SEVERITY-DRIFT** — same `(id, where)`, different severity. Disposition: name the rule that changed severity; a severity that drifts without a rule change is a silent regression.
- **D-UNION-UNTRIGGERED** — a row from a wider pre-declaration with no delivered trigger. Disposition: recorded as untriggered, not deleted; the union is evidence of what was once expected.

## 4. Controls — what makes reconciliation a check

| control | planted condition | required result |
|---|---|---|
| count-only match | change one row's `where` while keeping totals | reconciliation **fails** — matching on counts alone is not a match |
| silent extra | add an emitted row not in the declaration | a `D-EMITTED-EXTRA` row appears; the run is not read clean |
| silent missing | suppress a declared row from the run | a `D-EMITTED-MISSING` row appears; the declared debt is shown unmeasured |
| severity flip | flip a hold to a note | `D-SEVERITY-DRIFT`; no silent downgrade |
| late declaration | write the set after the run | inadmissible — the declaration is rejected on its timestamp, not its content |

## 5. What reconciliation never proves

- **A matched set is not a good set.** It says the run did what was declared; the declared set may itself be wrong, thin, or incomplete (§3, D-EMITTED-EXTRA).
- **A declared set is not a target.** If the declaration is treated as the thing to hit, an over-firing engine becomes invisible; the declaration is a prior, not a quota.
- **A hold is not a pass.** Every hold in the measured set is carried as debt; a hold read as “expected, therefore fine” is the exact laundering this procedure exists to prevent.
- **Reconciliation is not canon.** Even a fully dispositioned set says nothing about whether the culture, forms, or systems are sound.

## 6. Decision record — the reconciliation rules this entry adopts

1. **Adopted:** the expected finding set is declared before implementation, with where-keys and per-row reasons, and stamped (§2). Consequence: a set written after the run is inadmissible regardless of how well it matches.
2. **Adopted:** reconciliation matches on `(id, severity, where)`, never on counts alone (§4). Consequence: a count-preserving row move fails.
3. **Adopted:** when multiple pre-declarations exist, all are reconciled, and untriggered union rows are recorded, not deleted (§3). Consequence: the D4 case reports three sets and three delta classes rather than one flattering comparison.
4. **Adopted:** every delta row is dispositioned as engine-defect or declaration-defect, and a corrected declaration is a **new file** (§3). Consequence: the declaration history is append-only, consistent with `provenance-audit-ledger-format.md` §8.
5. **Rejected:** treating a matched set as clearance. Reason: it asserts agreement with a prior, not soundness (Dijkstra; §5).
6. **Open (to-verify):** whether the 11 union rows with “no delivered trigger and no engine path” are a coverage gap in the engine or a legitimate narrowing of the drill's scope. Owner: this lane's D-axis; the round-18 receipt leaves it open and this entry does not close it.
