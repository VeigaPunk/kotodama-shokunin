# Era and material scoped reconciliation — resolving labels by declared row, never by number

- topic: The design workflow for **scoped era and material reconciliation**: era labels in a packet resolve through declared scoped rows (`identity`, `mapped-confirmed`, `mapped-unconfirmed`, `unmapped`, `conflict`) and materials resolve by slot identity, never by label text or by an ordinal; a `(to-verify)` row holds rather than promotes, an unnamed label is `unmapped` rather than identity-by-number, and a declared two-to-one row is kept rather than collapsed. Covers the reconciliation ledger, the row vocabulary, the design obligations a designer owes the resolver, and the rule that a reconciliation is a resolution record, never a dating. Reference method and design workflow only; canon belongs to lore-shokunin.
- gap filled: `era-language-staging.md` stages a language across eras and `era-myth-language-costume-matrix.md` lays out an era-by-system worksheet, but no entry states the **scoped reconciliation rule** — how an era or material label resolves through a declared row, and why number-to-number identity is forbidden. Absence sweep 2026-10-18: `grep -rln "reconcile_scoped\|mapped-confirmed\|mapped-unconfirmed" corpus/knowledge/synthesis/` → 0 files.
- sources:
  - KTD-EM-S-0001 — `tools/d2-typed-labels.py` module docstring §2 and its `reconcile_scoped` implementation (R8-D05 §4): “era labels resolve through declared, scoped rows (`identity`, `mapped-confirmed`, `mapped-unconfirmed`, `unmapped`, `conflict`) and materials through slot identity, never by label; a `to-verify` row holds rather than promotes”. The executable authority.
  - KTD-EM-S-0002 — `tools/d2-typed-labels.py --selftest` measured this round, 2026-10-18, lane root, `export TMPDIR=$PWD/.scratch`: exit 0, `39/39 checks passed`, including the era rows — “era: a contract tag is identity”, “era: the declared legacy handle is mapped-confirmed”, “era: a (to-verify) ERX row is mapped-unconfirmed, never promoted”, “era: an unnamed label is unmapped, never identity-by-number”, “era: the declared two-to-one row is kept, not collapsed”, and “probe: a foreign era label holds rather than merging by number”.
  - KTD-EM-S-0003 — `examples/culture-d4/typed-labels.d4.yml` `era_material_reconciliation`: six records (`GAR-01`…`GAR-06`) each with an era block (`code: R-ERA-IN-SCOPE`, `tag` in `E0`/`E1`) and a material block (`code: R-MAT-RESOLVED`, `resolved: CMAT-0n`), `findings: []`. The measured resolution of a whole packet's era/material slots. NON-CANON drill artifact.
  - KTD-EM-S-0004 — `examples/culture-d4/typed-labels.d4.yml` `coverage`: `reconciliation_records 6`, `conflicts 4`, `rank_quarantine_handles 3`, `rank_rules_unresolved_items 13` — the reconciliation's own counts, including the conflicts it carried rather than collapsed.
  - KTD-EM-S-0005 — `corpus/knowledge/synthesis/era-language-staging.md` §"ordered sound changes, stratified registers, diglossic domain shifts" and `corpus/knowledge/synthesis/era-myth-language-costume-matrix.md` (separating political periodization from changes in cult, speech, writing, naming, dress, signs, timekeeping). These stage the eras; this entry fixes how a label attaches to one.
  - KTD-EM-S-0006 — `corpus/knowledge/verification/pre-declared-hold-set-reconciliation.md` (this lane, round 19) and `corpus/knowledge/verification/label-channel-routing-verification.md` §2 T4 (the two-clock rule for loans). The reconciliation is consumed by the hold-set procedure and shares the clock discipline.
  - KTD-EM-S-0007 — `corpus/knowledge/verification/to-verify-triage-protocol.md` §1–§2 (evidence states; a naked marker without a research question is not a usable queue item) and `corpus/knowledge/verification/calibration-registry.md` §1 (status vocabulary). The vocabulary a `(to-verify)` reconciliation row must satisfy.
  - KTD-EM-S-0008 — `corpus/knowledge/synthesis/loanword-material-dating.md` (entry interval ≠ referent-arrival interval; never intersect them to manufacture a date). The reason a reconciliation row is a resolution record and never a dating.
- calibration: the row vocabulary is this lane's house policy read off the projector and its measured selftest, not a published standard; the D4 era tags are fixture-relative (`E0`–`E3`), not BCE/CE dates, and this entry claims no chronology.
- couples: synthesis — `era-language-staging.md`, `era-myth-language-costume-matrix.md`, `loanword-material-dating.md`, `hold-set-contract-in-brief.md`, `generated-artifact-lifecycle.md`, `coupling-model.md`; verification — `../verification/label-channel-routing-verification.md`, `../verification/pre-declared-hold-set-reconciliation.md`, `../verification/to-verify-triage-protocol.md`, `../verification/calibration-registry.md`; culture-material — `../culture-material/era-periodization-models.md`, `../culture-material/material-culture-inference-method.md`; tooling — `tools/d2-typed-labels.py`, `examples/culture-d4/typed-labels.d4.yml`; siblings — lore-shokunin owns canon and chronology; chousa-shokunin owns general research method.
- source: the projector's `reconcile_scoped` behaviour and selftest, the D4 reconciliation ledger, and the era/material corpus entries named above; the row vocabulary and the resolution rules are this lane's house method, not findings attributed to the cited works.
- verified-at: 2026-10-18 — re-measured at HEAD `169c616`, lane root, `export TMPDIR=$PWD/.scratch`: `python3 tools/d2-typed-labels.py --selftest` → exit 0, `39/39 checks passed`; the D4 reconciliation block was read from `examples/culture-d4/typed-labels.d4.yml` for its record and coverage counts. Header fields and cross-reference targets checked for resolution; all cited repo paths exist. The round-8 design shard (R8-D05) behind the rule was cited via the tool, not re-inspected.
- recheck: whenever `tools/d2-typed-labels.py`, the era/material record shapes, or a packet's era tags change; before quoting a resolution count into a handoff; and whenever the row vocabulary is revised (corrections are new entries, never rewrites).

## 1. What this workflow licenses

- A **resolution procedure**, not a chronology: it tells a designer how an era or material label attaches to a declared row, and how an unresolved label is carried. It does not date anything.
- The rule exists because a packet's era tags are **design-local**: D4's `E0`–`E3` are fixture-relative, not BCE/CE (`examples/culture-d4/brief.md`). Treating two tags as equal because their numbers match is the failure the row vocabulary prevents.
- A reconciliation ledger is **evidence of resolution**: it says which label resolved to which declared row, and which did not.

## 2. The row vocabulary

| row | fires when | what it means | what it never means |
|---|---|---|---|
| `identity` | the label is a contract tag the packet declares directly | the label **is** the slot | that the tag names a calendar date |
| `mapped-confirmed` | the label matches a declared legacy handle with a confirmed mapping | the two labels denote the same declared row | that the mapping is dated, or attested outside this packet |
| `mapped-unconfirmed` | the label maps to a declared row but the row is `(to-verify)` | the resolution **holds** | that the row may be promoted |
| `unmapped` | no declared row matches | the label is carried unresolved | identity-by-number, or a silent merge |
| `conflict` | two declared rows claim the label, or two labels claim a row | the disagreement is carried | a collapsed one-to-one answer |

Materials use the same discipline but resolve by **slot identity**
(`R-MAT-RESOLVED` → `CMAT-0n`), never by label text: a material's name is not
its identity.

## 3. Design obligations the resolver needs

| obligation | what the designer supplies | why |
|---|---|---|
| declare the era rows | a scoped table of era tags with their declared handles | without declared rows, every label is `unmapped` and every mapping is guesswork |
| declare two-to-one rows explicitly | when two labels legitimately denote one row (or one label two rows), say so | the resolver keeps a declared two-to-one row rather than collapsing it |
| mark `(to-verify)` rows | the open question and its owner on the row | a `(to-verify)` row holds; an unmarked row invites promotion |
| separate the clocks | word-entry interval and referent-arrival interval declared apart | intersecting them manufactures a date (`loanword-material-dating.md`) |
| declare material slots | each material as a slot with its id, not as a name | resolution by slot identity is the only stable match |
| keep the ledger | the reconciliation record, per era/material slot | a resolution without a record is unreproducible |

## 4. What reconciliation never licenses

- **A resolution is not a date.** Resolving `E0` to a declared row says nothing about when `E0` was; the row is a design-local handle.
- **A mapping is not attestation.** `mapped-confirmed` confirms an *internal* mapping, not a historical correspondence.
- **A `(to-verify)` row is not promoted.** It holds; the promotion decision belongs elsewhere and is not the resolver's.
- **A conflict is not an error to erase.** A carried conflict is the honest output; collapsing it to a one-to-one answer destroys the disagreement the ledger exists to preserve.
- **A reconciliation is not canon.** It records how a packet's labels resolve; chronology and canon belong to lore-shokunin.

## 5. Reviewer checklist

1. Confirm every era label in the packet has a declared row, and every unresolved label is carried as `unmapped`.
2. Confirm `(to-verify)` rows hold and carry their open question and owner.
3. Confirm declared two-to-one rows are kept, not collapsed, and that conflicts are carried.
4. Confirm materials resolve by slot identity, not by label text.
5. Confirm the two clocks (entry interval, referent arrival) are declared apart and never intersected.
6. Record the projector revision and packet digest the ledger was produced from.

## 6. Decision record — the reconciliation rules this workflow adopts

1. **Adopted:** era labels resolve through declared scoped rows, and materials by slot identity; number-to-number identity is forbidden (§2). Consequence: two era tags with the same ordinal never merge by that fact alone.
2. **Adopted:** a `(to-verify)` row holds rather than promotes, and an unnamed label is `unmapped` rather than identity-by-number (§2). Consequence: the resolver never manufactures a resolution it was not given.
3. **Adopted:** declared two-to-one rows and conflicts are carried, not collapsed (§2–§3). Consequence: the reconciliation ledger can report `conflicts` and unresolved items without erasing them.
4. **Adopted:** the two clocks opened by borrowed-strata forms are declared apart and never intersected (§3). Consequence: the lane gives up a manufactured date rather than a false precision.
5. **Rejected:** resolving a label by its ordinal or its text. Reason: both are the look of a label, not its declared identity — the exact confusion the row vocabulary exists to prevent.
6. **Open (to-verify):** whether the reconciliation ledger's `conflicts` and `unresolved_items` counts should feed the hold-set declaration as expected rows, or stay a separate coverage block. Owner: this lane's D axis; the D4 packet carries both, and this entry does not merge them.
