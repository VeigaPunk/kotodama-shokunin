- Seat: P02 | planner | claim O (+ A-claim audit checklist) | date 2026-10-19 | baseline 57c8409

# P02 — Defect-queue schema and adjacency audit checklist

Planning fragment only: this defines the O queue contract and A audit procedure; it is not a completed census, defect disposition, freeze adjudication, or acceptance verdict. Round 37 requires a dispositioned census across rounds 33–36, non-author evidence for every fixed row, and per-surface A verdicts including the r7 freeze question and eleven corpus entries (`reports/round-37/claims.json:19-30`). The round-36 D claim remains rejected as filed; round 37 must not rewrite or retroactively repair its evidence (`reports/round-36/validation.json:49-78`; `reports/round-37/targets.json:74`).

## 1. Defect-queue contract for O01/O02/O03/O05/O06/O09

Use K02's census as the starting set, then reconcile it against the round-33–36 SCORECARD rows, LOG entries, receipts, and referenced fragments. The queue must preserve every source pointer, merge repeated mentions only when they describe the same underlying defect, and retain an alias/cross-reference list so deduplication is auditable. A related recount row is a linked measurement, not a second defect row; give each underlying defect one canonical queue ID and point to the recount row where applicable. This addresses the explicit recount/defect overlap handoff (`reports/round-37/targets.json:16-17,68`).

Suggested root fields:

| Field | Requirement |
|---|---|
| `schema` | Fixed identifier, e.g. `kotodama-r37-defect-queue/1`. |
| `round`, `scope_rounds` | `37` and `[33,34,35,36]`. |
| `census_source` | `reports/round-37/scout/K02-defect-census.md`; cite its census date/cut. |
| `census_ids`, `queue_ids` | Stable sets used for explicit equality checking; report missing and extra IDs instead of smoothing them. |
| `items` | Exactly one row per canonical defect. |
| `routing` | Round-38-or-later destinations for carried items; no ownerless carry. |

Each `items[]` row should contain:

| Field | Requirement |
|---|---|
| `id`, `summary` | Stable census/finding ID and short, neutral description; do not mint a closure verdict. |
| `origin_refs[]` | At least one `{path, lines, record_kind, round}` citation to the originating record. |
| `also_reported_at[]` | All duplicate mentions in SCORECARD, LOG, receipts, and cross-references; do not drop conflicting readings. |
| `linked_records[]` | Related recount row / control / other ledger ID and relationship; identifies the single primary record owner. |
| `disposition` | Exactly `fixed-with-evidence` or `carried-with-owner+reason+next-touch`; no composite or third class. |
| `verification` | For `fixed-with-evidence`: fix/control pointers, exact re-verification command and observed result, verifier seat, and an explicit `non_author: true`. It is invalid without this round’s independent evidence. |
| `carry` | For carried rows: `owner`, `reason`, and `next_touch`, with the next-round route (round >= 38 or named external owner/trigger) repeated in the root routing table. |

Validation rules: IDs are unique; each row has source citations; the `census_ids` and `queue_ids` sets are equal; every fixed row has fresh non-author evidence; every carried row has all three required carry fields and a round-38+ route; no finding appears only as an unlinked recount overlap; and the queue has zero unowned rows. These gates implement O's stated 100% census, verification and routing thresholds (`reports/round-37/claims.json:19-24`).

Seed the census review with, but do not limit it to, the named candidates in the claim: F-C13-1, R34-N1, F1–F5 timekeeping, the 402 records, r36 residue, the conformance incident, and README prediction nuance (`reports/round-37/claims.json:20-22`). The source history confirms the F-C13-1 in-tree runner incidents and the prohibition/recovery record (`LOG.md:3548-3567`, `:3695-3698`), R34-N1's close and its round-35 hardening (`LOG.md:3616-3646`, `:3662-3667`), and the r36 D rejection plus C/ Ca records (`SCORECARD.md:651-667`; `reports/round-36/validation.json:49-78`). These are census leads, not preassigned dispositions: a row is fixed only if O02/O06 supplies the required independent proof; otherwise carry it. In particular, preserve the r36 D rejection and route its residue without changing the failed claim's historical evidence (`reports/round-37/targets.json:74`).

## 2. A-claim checklist

The audit covers round-33–37 artifacts and must file a verdict for every inventoried surface, with the freeze asymmetry adjudicated, the eleven r35/r36 entries checked for cross-domain language and couples resolution, no unfiled bleed, and contested scope still routed (`reports/round-37/claims.json:25-30`). Use a per-surface record with: `surface/path`, `origin round`, `inventory source`, checks and their evidence, verdict (`GREEN`, `FINDING:<id>`, or `to-verify`), and owner/route for every finding. A grep hit is a review pointer, not a verdict; read the context and cite the line. The r35 assembled audit's per-surface table and owner-backed findings are the useful precedent (`reports/round-35/adj/audit-assembled.md:34-64,192-225`).

1. **Establish the scope inventory.** Reconcile SCORECARD/LOG and round receipts/fragments with a diff-based list of round-33–37 created/edited surfaces. Include the in-scope records and any live files named by the claims; add each round-37 artifact as it lands. A surface may not disappear because it has no obvious textual bleed. Record command, revision/cut, and complete path list. Round-35's A claim and assembled audit show the prior diff-derived inventory method (`reports/round-35/claims.json:54-64`; `reports/round-35/adj/audit-assembled.md:34-41`).
2. **Adjudicate the r7 freeze/read-set asymmetry (A01; independent check A06).** In an isolated `git archive` copy under `.scratch`, inspect the r7 packet/freeze/expected/twin/claims-map bytes, current `D4_COMPONENTS`, `V3_READ_SET`, and verifier behavior. Re-render the current default pair in that copy, compare generated packet/twin and recorded input/output digests with the filed r7 bytes, and state whether they match. Separately establish whether `13-register-law.yml` is omitted intentionally and whether the omission is documented and safe: cite its manifest and direct read-set membership, plus the render/probe evidence for whether a change to that component is detected. The r36 review reports 58 frozen inputs, the 12-component tuple without `13-register-law.yml`, a green default chain, and a probe where changing that non-member changed the assembled packet and triggered E2E-DIGEST (`reports/round-36/review/R03-cross-review.md:17-44,68-75,344-349`); treat this as prior evidence to re-check, not this seat's adjudication. If the renderer/freeze pair diverges or no evidence supports a documented skip, file a named finding with owner and next touch; do not call the asymmetry harmless by inference. Preserve `reports/round-34/handoff/declared-in-r7/**`: no `--freeze`, no re-freeze, and no edits. Never execute any filed `reports/round-*/run-validation.py` in-tree; F-C13-1 is absolute (`reports/round-37/targets.json:3-8`).
3. **Re-scan the eleven r35/r36 corpus entries (A02).** Get the exact path roster from K04 and reconcile it to the ten r35 entries and one r36 timekeeping entry (`reports/round-35/claims.json:22-35`; `reports/round-36/claims.json:22-27`; `reports/round-37/targets.json:14,50`). For each entry, record the path and digest/cut; scan for language that crosses the lane's ownership boundary; hand-read each candidate and classify it as ordinary mention, negation, routed reference, or unsupported assertion. `PROVINCE.md:16-25` lists refused domains and says contested scope is routed, never absorbed; `corpus/QUALITY.md:13-20` requires explicit coupling and canon hygiene. Parse its `- couples:` references and resolve each target using the existing brace/path-resolution approach (`reports/round-19/audit/entry-audit.py:74-96`); file unresolved targets and inspect that each declared coupling is meaningful rather than silently claiming reciprocal links. Use heuristic scans only as discovery aids: the r35 entry runbook documents that language hits need human context review (`reports/round-35/cov/C12-audit-runbook.md:37-48`).
4. **Cross-round surface bleed and scope (A03).** For every inventory row, log the scan/check actually used, observed result, and a cited per-surface verdict. Check new/changed text for assertions of canon, clearance, rights rulings, promotion, or absorbed contested scope; distinguish quoted historical findings and explicit negations/routing from an assertion. Include both round-local artifacts and live files created/edited. Findings must be named and assigned; unsupported or unexamined surfaces stay `to-verify`, not GREEN. The r35 audit demonstrates named, owned findings rather than silently treating all surfaces as green (`reports/round-35/adj/audit-assembled.md:192-225`).
5. **Re-check contested items (A04).** Cross-read the existing bilateral read and contract-digest records and the round-33–36 findings that route matters to lore/operator/other owners. For each, state current evidence, owner, reason it remains unresolved, and next touch; confirm no round-37 prose absorbs a canon, clearance, promotion, or closure decision. Confirm the freshness pause remains in force and is not treated as an axis move (`reports/round-35/adj/audit-assembled.md:347-360`; `reports/round-37/claims.json:11,32-34`; `PROVINCE.md:22-25`).
6. **Coverage and independent verification.** Check every scope-inventory row has exactly one verdict and every finding has an owner plus route; reconcile the 11-entry roster and the freeze adjudication with A01–A04; A06 independently verifies those commands, while A08 provides the second adjacency pass (`reports/round-37/targets.json:49-56`). Do not promote the aggregate claim from a clean scan alone: the claim threshold is surface-level verdicts and zero *unfiled* bleed, with contested matters still routed (`reports/round-37/claims.json:25-30`).

## Owed

- `reports/round-37/scout/K02-defect-census.md` — required to instantiate the O set-equality comparison; this fragment specifies the schema but does not assert a complete defect list.
- `reports/round-37/scout/K03-freeze-drift.md` — freeze-source inventory and digest behavior needed before A01's independent adjudication; the r36 review is only a prior reading.
- `reports/round-37/scout/K04-entries-scout.md` — exact eleven-entry roster and entry-level surfaces needed before A02's re-scan.
- O02's independent fix-verification evidence (`reports/round-37/op/O02-fix-verify.md`) and O09's round-38+ routing (`reports/round-37/op/O09-routing.md`) remain owed. O06 has filed only `could-not-evaluate` because the O01/O02 inputs were absent; re-run its disposition-class check after those inputs land (`reports/round-37/op/O06-verify.md:3-7`). No row is classified fixed or carried here.
- Final per-surface verdicts and the queue census itself are downstream deliverables, not completed in this planner fragment.

## Citations

- `reports/round-37/claims.json:11,19-30,32-34` — freshness pause, O/A requirements and thresholds, example defects, and non-goals.
- `reports/round-37/targets.json:3-8,12-17,36-54,64-74` — shared safety rules, K02/K03/K04 missions, O/A roles, and rejected-r36 sentinel.
- `reports/round-36/validation.json:49-78` — D claim failed as declared and residue routed; `:91-105` — declared fallback and could-not-evaluate record.
- `reports/round-36/claims.json:22-33` — one timekeeping entry in r36 and its scope.
- `reports/round-35/claims.json:22-35,54-65` — ten r35 entries and prior adjacency criteria.
- `LOG.md:3548-3567,3616-3646,3648-3674,3676-3701` — F-C13-1 record, R34-N1 status, r35 findings, and r36 rejection/incident.
- `SCORECARD.md:593-601,620-626,645-667` — earlier findings and round-36 rejected status.
- `reports/round-36/review/R03-cross-review.md:17-44,68-75,221-258,280-288,344-349` — r7 read-set/re-render evidence and prior recount treatment.
- `reports/round-35/adj/audit-assembled.md:34-64,192-225,347-360` — per-surface verdict and finding/contested-scope precedent.
- `corpus/QUALITY.md:3-20`; `PROVINCE.md:16-25` — coupling, canon hygiene, refused scope, and contested-scope boundary.
- `reports/round-19/audit/entry-audit.py:74-96`; `reports/round-35/cov/C12-audit-runbook.md:37-48` — couples path resolution and human review of heuristic bleed hits.
