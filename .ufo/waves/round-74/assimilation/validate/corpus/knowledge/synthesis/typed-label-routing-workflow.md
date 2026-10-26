# Typed-label routing workflow — routing every form-bearing record before a gate reads it

- topic: The design-side workflow for **routing form-bearing records onto the correct channel before any gate reads them**: enumerate the records a culture packet carries, type each string as a native form, a translated label, or a borrowed-strata form, attach the companions each kind owes, hold every owed form slot open rather than filling it with a gloss, and hand the packet to the gates only after the routing is complete. Covers the routing pass, the register/era scoping of slots, the owed-slot backlog, and the handoff statement that a routed packet is clean-with-holds, never clean. Reference method and design workflow only; canon belongs to lore-shokunin.
- gap filled: the synthesis partition carries `glossary-registry-format.md` (glossary entry shape) and `loanword-material-dating.md` (borrow clocks), but no entry states the **design-side routing workflow** — the order of operations by which every form-bearing record is typed and given its companions before a gate reads it. Absence sweep 2026-10-18: `grep -rln "translated-label\|route.*channel\|typed label" corpus/knowledge/synthesis/` → 0 files.
- sources:
  - KTD-TW-S-0001 — `SKILL.md` §"Label typing — translated labels, native forms, borrowed strata": the three kinds, the checked channel per kind, the required companions, and thresholds T1–T5. The design authority it cites is `reports/round-8/depth/design-spec.md` §1. Lane policy, not a published standard.
  - KTD-TW-S-0002 — `tools/d2-typed-labels.py` (projector; sha256 `0da0015f700345c938184cb45ca07178c33e98f798c3c09729007487fb89c802` from `examples/culture-d4/expected-holds.json`): `parse_typed_labels` (R8-D03 §4.2), the closed YAML subset loader (R8-D03 §4.1), `reconcile_scoped` (R8-D05 §4), the rank-rule adapter (R8-D04 §4), and the `D2L-*` finding vocabulary. The executable that reads a routed packet.
  - KTD-TW-S-0003 — `examples/culture-d4/typed-labels.d4.yml` (generated projection, sha256 `a59990bb…`, pinned in `tools/gates/frozen/round-18/MANIFEST.tsv`): the measured routing of a whole packet — `typed_labels 74`, `labels_by_kind {native-form 56, translated-label 12, borrowed-strata 6}`, `label_findings_fail 0`, `label_findings_hold 12`. NON-CANON drill artifact.
  - KTD-TW-S-0004 — `examples/culture-d4/brief.md` §"Named hold set (pre-implementation)" and `examples/culture-d4/components/01-brief.yml` `contract.hold_set_declaration`: the declaration that six garment glosses (`GAR-01`…`GAR-06`) are translated labels whose native forms are owed — the design intent the routing implements.
  - KTD-TW-S-0005 — `corpus/knowledge/synthesis/glossary-registry-format.md` §1–§4 (glossary-entry profile: identity, required fields, evidential etymologies, register) and `corpus/knowledge/synthesis/loanword-material-dating.md` §"layer/register" (the borrow ledger the routing must carry). These fix the record shapes; this entry fixes the order of operations and the owed-slot discipline.
  - KTD-TW-S-0006 — `corpus/knowledge/linguistics/language-contact.md` §5–§6 (borrowing scales, strata) and `corpus/knowledge/linguistics/color-terminology.md` (a semantic field whose terms often arrive as loans): the linguistic grounding for why a form's kind is a design decision with consequences, not a formatting choice.
  - KTD-TW-S-0007 — `corpus/knowledge/verification/label-channel-routing-verification.md` (this lane, round 19): the verification-side routing procedure this workflow hands to. The workflow and the check are one pair; a design that skips the routing cannot be checked.
  - KTD-TW-S-0008 — `corpus/knowledge/verification/verification-method-overview.md` §2–§3 (epistemic type; the minimal claim card: a failing case fixed before review). Supplies the record discipline the routing pass must satisfy.
  - KTD-TW-S-0009 — Yue Jia and Mark Harman (2011), “An Analysis and Survey of the Development of Mutation Testing,” *IEEE Transactions on Software Engineering* 37(5): 649–678, [doi:10.1109/TSE.2010.62](https://doi.org/10.1109/TSE.2010.62). A design control is worth what it can catch; cited as a design rule for the routing pass's controls, not as a law.
- calibration: the routing workflow is this lane's house policy read off `SKILL.md` and the projector, not a published standard; Jia–Harman is cited as a design rule for controls; the D4 routing counts are a NON-CANON drill measurement, not a claim about any real language.
- couples: synthesis — `glossary-registry-format.md`, `loanword-material-dating.md`, `conlang-blueprint-template.md`, `worldbible-integration-contract.md`, `costume-language-coupling-table.md`, `generated-artifact-lifecycle.md`, `hold-set-contract-in-brief.md`; verification — `../verification/label-channel-routing-verification.md`, `../verification/lexicon-coverage-audit.md`, `../verification/phonology-sanity-gate.md`, `../verification/naming-collision-gate.md`; linguistics — `../linguistics/language-contact.md`, `../linguistics/phonology-sanity.md`; tooling — `tools/d2-typed-labels.py`, `examples/culture-d4/typed-labels.d4.yml`; siblings — lore-shokunin owns canon; chousa-shokunin owns general research method.
- source: the `SKILL.md` routing table, the D4 routing projection, and the corpus record-format entries named above; the workflow is this lane's house method, not findings attributed to the cited works.
- verified-at: 2026-10-18 — the D4 routing projection was read at HEAD `169c616` for its `coverage` block; `python3 tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml --json` → exit 1, `stats {"fail": 0, "hold": 15, "labels": 74, "note": 1}` (lane root, `export TMPDIR=$PWD/.scratch`). Header fields and cross-reference targets checked for resolution; all cited repo paths exist. The round-17/18 receipts behind the counts were read by path, not re-executed.
- recheck: whenever the `SKILL.md` routing table, `tools/d2-typed-labels.py`, the glossary or loan formats, or a packet's record set changes; before quoting a routing count into a handoff; and whenever the verification-side routing procedure is revised (corrections are new entries, never rewrites).

## 1. What this workflow licenses

- A **design order of operations**, not a generator and not a gate. It tells a designer in what order to touch a packet so the routing is complete before verification reads it.
- Routing is **work the design owes**, not bookkeeping: a record whose kind is undeclared is an unfinished record, and a form slot filled with a gloss is a record that lies about what it carries.
- A routed packet is **clean-with-holds**, never clean: the measured D4 routing leaves 12 holds (six `GAR` glosses × the `where` and `LEX` keys) that are design debt, not clearance.

## 2. The routing pass — order of operations

| step | action | output | if skipped |
|---|---|---|---|
| P1 enumerate | list every form-bearing record the packet carries: lexicon entries, names, garment terms, loan layers, symbol words | a record census | a record the census misses is never typed and may be graded on the wrong channel |
| P2 declare the inventory | fix the phoneme inventory and syllable profile the packet declares (T1) | the sound-channel admission test | routing has no test to route against |
| P3 type each string | for each record, apply the routing table (`../verification/label-channel-routing-verification.md` §2) and record the kind | `native-form` / `translated-label` / `borrowed-strata` / untyped-legacy | an undeclared kind is graded by look |
| P4 attach companions | give each kind the companions it owes: `label_id` + `owner` (gloss); script/scheme + `era_ids` + evidence (native); layer ref + donor set + substitutions + entry stage + referent availability + channel + register (loan) | a complete record | a kind without its companion is an incomplete record, not a routed one |
| P5 hold owed slots | where the native form is owed, leave the slot **held** and record why | the owed-slot backlog | filling the slot with the gloss manufactures a representation artifact |
| P6 scope to register/era | bind each form to its register/domain and era tags; a form that is right in one register is not thereby right in another | scoped forms | a register-limited form is graded against the whole inventory |
| P7 hand to verification | run the routing check and the lexicon/phonology/naming gates over the routed packet | a clean-with-holds reading | verification grades an unrouted packet and reports artifacts as defects |

## 3. Register and era scoping of slots

- A **slot** is a position in a record (`LEX-GAR-01`), not a string. The slot can
  be filled (native form supplied), held (owed), or filled by a loan; the slot's
  state is the design's statement about that record.
- **Register scoping**: a form is admitted in the register it is declared for
  (ritual, ordinary, technical, argot). A form legal in a ritual register is not
  thereby legal in ordinary speech; the routing carries the register, and the
  gate reads the scoped form.
- **Era scoping**: a form belongs to era tags (`era_ids`); a form attested for
  E0 is not automatically E3. The projection's era reconciliation resolves era
  labels through declared rows, never by number (`../verification/label-channel-routing-verification.md` §2 T4).
- **Loan scoping**: a `borrowed-strata` record opens a second clock — the
  word-entry interval and the referent-arrival interval. The workflow requires
  both to be declared; the gate refuses to intersect them.
- Consequence for the designer: a packet's routing is not one pass over strings
  but a pass over **scoped slots**, and the same surface string can legitimately
  carry different kinds in different scopes.

## 4. The owed-slot backlog

| slot state | record carries | handoff statement |
|---|---|---|
| filled native | the form, script/scheme, era tags, evidence | the form is checkable on the sound and identity channels |
| filled loan | the recipient form + the borrow ledger | the form is checkable on the recipient channel plus the ledger |
| held (owed) | owner, the slot id, the reason | the form is **owed**; the reading is a hold, never a pass |
| held (to-verify) | the one discriminator that holds (T3) | the kind is not asserted; the record is a queue item |
| legacy untyped | the legacy form field | the legacy form is still checked; typing fields cannot exempt it |

- The backlog is a **design artifact**: it is the list of forms the culture still
  owes, and it is handed to lore-shokunin as open work, never closed by a gloss.
- Removing a gloss from the sound channel **removes an artifact**; it does not
  clear the name. The aggregate stays red with the owed forms held.

## 5. What the workflow never licenses

- **A gloss is not a form.** A reader-facing rendering never enters the sound or identity channel, no matter how pronounceable it looks.
- **A loan is not a native word.** Typing by resemblance invents or erases a contact history; the kind comes from the discriminator count, not the look.
- **A routed packet is not a cleared packet.** Clean-with-holds means the artifacts are gone and the debt is visible; it is not approval.
- **A routing pass is not canon.** It says how the packet's forms are carried; whether the culture is sound is a separate judgement owned by lore-shokunin.

## 6. Decision record — the routing rules this workflow adopts

1. **Adopted:** the routing pass runs **before** verification, in the order P1–P7 (§2). Consequence: a gate reading of an unrouted packet is reported as an artifact, and the fix is the routing, not the gate.
2. **Adopted:** every form-bearing record gets a kind and the companions that kind owes; a kind without its companion is an incomplete record (§2 P4). Consequence: the census (P1) is load-bearing — a missed record is an untyped record.
3. **Adopted:** owed native forms leave the slot **held**, and the backlog is handed off as open work (§4). Consequence: a packet can never read fully clean while forms are owed; the honest reading is clean-with-holds.
4. **Adopted:** forms are scoped to register and era, and loans carry two clocks that are never intersected (§3). Consequence: the routing operates on scoped slots, not on bare strings.
5. **Rejected:** filling an owed slot with its gloss to make the packet read clean. Reason: it removes the artifact and the evidence together, leaving a false clean (§4; the D4 declaration exists to prevent exactly this).
6. **Open (to-verify):** whether the owed-slot backlog should be a first-class handoff artifact with its own id space, or remain a view of the projection's hold set. Owner: this lane's D/C boundary; not disposed here.
