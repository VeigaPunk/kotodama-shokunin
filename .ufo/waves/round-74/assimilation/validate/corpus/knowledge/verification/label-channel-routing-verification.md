# Label channel routing — verifying which channel a form-bearing record is graded on

- topic: The verification procedure for **label channel routing**: given one form-bearing record in a linguistic-cultural packet, decide which channel its string is graded on (the sound/identity channel, the recipient-adapted borrow channel, or no channel at all), prove the routing with negative controls, and refuse the two failure modes — grading a reader-facing gloss as a native form, and exempting a native form from checking because it was mislabeled. Reference method and lane policy only; canon decisions belong to lore-shokunin.
- gap filled: the verification partition carries the typed-label **kinds** (`SKILL.md` §"Label typing" decision table) and the executable that implements them (`tools/d2-typed-labels.py`), but no entry states the **routing decision procedure as a check** — which channel one record is graded on, what makes the routing wrong, and what control proves the router routes rather than blesses. Absence sweep 2026-10-18: `grep -rln "translated-label\|sound channel\|channel routing" corpus/knowledge/verification/` → 0 files.
- sources:
  - KTD-LR-S-0001 — `SKILL.md` §"Label typing — translated labels, native forms, borrowed strata": the three kinds, the checked channel per kind, the required companions, and the thresholds T1–T4; the design authority it cites is `reports/round-8/depth/design-spec.md` §1. Lane policy, not a published standard.
  - KTD-LR-S-0002 — `tools/d2-typed-labels.py` (projector, sha256 `0da0015f700345c938184cb45ca07178c33e98f798c3c09729007487fb89c802`, read from `examples/culture-d4/expected-holds.json` `projector_sha256` 2026-10-18): the `parse_typed_labels` parser (R8-D03 §4.2), the closed YAML subset loader (R8-D03 §4.1), and the `D2L-FORM-UNRESOLVED` / `D2L-DATA` / `D2L-BORROW` finding vocabulary. The executable authority for the routing table below.
  - KTD-LR-S-0003 — `examples/culture-d4/typed-labels.d4.yml` (generated projection, sha256 `a59990bbfe5a8992ffa6e67e9b3e43e7ff477df9fc754e5af92b6f40d23fe11d`, pinned in `tools/gates/frozen/round-18/MANIFEST.tsv`): the measured routing result — `typed_labels 74`, `labels_by_kind {native-form 56, translated-label 12, borrowed-strata 6}`, `label_findings_fail 0`, `label_findings_hold 12`. NON-CANON drill artifact.
  - KTD-LR-S-0004 — `examples/culture-d4/expected-holds.json` (sha256 `09490a2756d123ebbc2023be89fc01c95ec2f8cc7e6df42ecc5b8cd438058e98`): the 15-hold set the routing emits — six `D2L-FORM-UNRESOLVED` rows at `GAR-01`…`GAR-06` are the owed form slots the routing holds, never passes.
  - KTD-LR-S-0005 — `reports/round-18/d4/holds.md` §1–§6 and `reports/round-18/d4/gate-runs-1.md`: the emitted-set extraction and the gate-run receipt showing the same packet failing six `PHON-INVENTORY` rows on the *legacy* path — the artifact class the routing removes.
  - KTD-LR-S-0006 — `corpus/knowledge/verification/verification-method-overview.md` §2–§3 (epistemic type and the minimal claim card: a rule locator and a failing case fixed before review) and `corpus/knowledge/verification/verification-independence-anti-circularity.md` §1 (independence is a property of failure sources, not job titles). These supply the record shape; this entry supplies the routing rule they do not state.
  - KTD-LR-S-0007 — Yue Jia and Mark Harman (2011), “An Analysis and Survey of the Development of Mutation Testing,” *IEEE Transactions on Software Engineering* 37(5): 649–678, [doi:10.1109/TSE.2010.62](https://doi.org/10.1109/TSE.2010.62). A control's worth is whether a planted defect can make it fail — the discipline §4 applies to the routing controls. Calibration: a survey of a contested technique, cited as a design rule, not as a law.
- calibration: the routing rule is this lane's house policy read off `SKILL.md` and the projector, not a published standard; Jia–Harman (a survey of a contested technique) and Dijkstra are mainstream engineering references cited as design rules, never as linguistic-cultural evidence; no real language, script, or community is described.
- couples: verification — `verification-method-overview.md`, `verification-independence-anti-circularity.md`, `phonology-sanity-gate.md`, `lexicon-coverage-audit.md`, `naming-collision-gate.md`, `gate-frozen-run-standard.md`; synthesis — `../synthesis/glossary-registry-format.md`, `../synthesis/loanword-material-dating.md`, `../synthesis/typed-label-routing-workflow.md`; linguistics — `../linguistics/phonology-sanity.md`, `../linguistics/language-contact.md`, `../linguistics/writing-systems.md`; tooling — `tools/d2-typed-labels.py`, `tools/gates/d4-typed-labels-check-gate.py`, `examples/culture-d4/typed-labels.d4.yml`, `examples/culture-d4/expected-holds.json`; siblings — lore-shokunin owns canon and world-bible consistency; chousa-shokunin owns general source-research method; no sibling or world-bible writes.
- source: the `SKILL.md` routing table, the projector's own behaviour measured 2026-10-18, and the round-8/17/18 receipts named above; the routing rule and its controls are this lane's house method, not findings attributed to the cited works.
- verified-at: 2026-10-18 — re-measured at HEAD `169c616`, lane root, `export TMPDIR=$PWD/.scratch`: `python3 tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml --json` → exit 1, `stats {"fail": 0, "hold": 15, "labels": 74, "note": 1}`; `python3 tools/gates/d4-typed-labels-check-gate.py examples/culture-d4/typed-labels.d4.yml` → exit 0, `byte-identical deterministic projection`; `python3 tools/gates/d4-typed-labels-check-gate.py --selftest` → exit 0, `39/39 checks passed`. The projection's own `coverage` block was read for the kind split. Header fields and every cross-reference target checked for resolution; all cited repo paths exist. The cited round-18 receipts were read by path, not re-executed.
- recheck: whenever `tools/d2-typed-labels.py`, the `SKILL.md` routing table, or the D4 packet/projection changes; before quoting any kind count into a handoff; and whenever a peer entry's routing rule is revised (corrections are new entries, never rewrites of this one).

## 1. What this entry licenses

- A **check**, not a generator: given a record and its declared typing, this entry tells a reviewer which channel the record's string must be graded on and how to prove the routing is not inert. It does not type records for you (the projector does) and it does not decide canon.
- Routing is a **failure-source separation** (`verification-independence-anti-circularity.md` §1): a gloss routed onto the sound channel produces a representation artifact that looks like a linguistic defect; a native form routed off it produces a clean line with no evidence behind it. Both are routing failures, not language findings.
- The rule is **lane policy** derived from `SKILL.md` and the projector. It is not a claim about any real language, script, or community, and passing it is not canon.

## 2. The routing decision procedure

Apply in order; the first row that fires fixes the channel. `E` = the record's declared evidence status.

| # | Condition on the record | Kind | Graded channel | Companion the record must carry | Wrong routing produces |
|---|---|---|---|---|---|
| R1 | The string is a declared gloss field, uses whitespace/gloss punctuation, or carries a segment outside the declared inventory | `translated-label` | **none** — never the sound or identity channel | `label_id` + `owner`; the form slot stays **held** when the native form is owed | grading a gloss against native phonotactics manufactures an artifact — the six `PHON-INVENTORY` rows in `reports/round-18/d4/gate-runs-1.md` |
| R2 | A native form is supplied and passes the declared inventory **and** the declared syllable profile (T1) | `native-form`, `status: supplied` | sound + identity; **exactly one** checked form per record (T2) | script/representation/scheme, `era_ids`, evidence | a second supplied sound form on the same record is `D2L-DATA`, not a richer record |
| R3 | Sound kind declared but **no bytes supplied** | `native-form` or `borrowed-strata`, `status: absent`/`to-verify` | **none** — HOLD | owner + form slot + reason | silent pass is forbidden; the row is `D2L-FORM-UNRESOLVED` at severity `hold` |
| R4 | A supplied recipient form passes the recipient inventory **and** ≥2 of the five borrowed-strata discriminators (T3) | `borrowed-strata`, `status: supplied` | recipient-adapted form + borrow-ledger checks | layer ref, donor {immediate/ultimate/carrier}, donor form + substitutions, entry stage, referent availability, channel, register/domain | mistyping a loan as native erases the contact clock; mistyping a native word as a loan invents a contact history |
| R5 | Exactly **one** discriminator holds | kind **not asserted**, `status: to-verify` with the one discriminator named | none | the discriminator that holds | defaulting to either kind converts a coin-flip into a finding |
| R6 | No typing fields at all (legacy record) | no kind | the legacy form field is **still checked** | — | adding typing fields cannot exempt a string from checking |

T4 is the clock rule that makes R4 a two-clock check: typing `borrowed-strata`
opens a word-entry interval *and* a referent-arrival interval; intersecting them
to manufacture a date is `D2L-BORROW` (executable B4). T5 (calibration, not
hard): a declared loan-free lexicon needs a stated contact story.

## 3. Negative controls — what makes the routing a check

A router that types nothing and grades nothing is green for free. Each control
below must be able to fail; the measured controls are the projector's own
`--selftest` matrix (39/39, exit 0, 2026-10-18).

| control | planted condition | required result |
|---|---|---|
| gloss-on-sound | move a `translated-label`'s gloss into the sound channel | a finding appears (`PHON-INVENTORY`-class on the legacy path, `D2L-DATA`/routing finding on the typed path) — never a silent pass |
| owed-slot | declare a native form owed and leave the slot empty | `D2L-FORM-UNRESOLVED`, severity `hold`, form slot **held** |
| loan-as-native | supply a recipient form that fails the recipient inventory | `D2L-BORROW`, not a native pass |
| substitutions | supply substitutions that do not derive the declared form | `D2L-BORROW` (selftest case “spec B3”) |
| two-forms | supply two sound forms on one record | `D2L-DATA` (selftest case “spec L2”) |
| missing-field | omit a required field | `D2L-DATA` (selftest case “spec L1”) |

The measured projection is consistent with these controls: of 74 typed labels,
12 are `translated-label` and none is graded on the sound channel
(`label_findings_fail 0`), while the 12 owed slots appear as `label_findings_hold
12`.

## 4. What routing never proves

- **Inventory-legal is not native.** R2's inventory test routes strings *away*
  from the native channel; provenance decides nativeness, never the phonotactic
  test. A word that happens to be pronounceable is not thereby attested.
- **A label is not a gap-filler.** Removing a gloss from the sound channel
  removes an artifact; it does not clear the name. The aggregate stays red with
  the owed forms held (measured: 12 holds survive the routing).
- **A label is not history.** A translated or curatorial label never becomes an
  attested historical native word by repetition (`../synthesis/costume-language-coupling-table.md`).
- **A green routing run is bounded evidence.** It asserts this projector's
  typing over this packet at this revision; it says nothing about whether the
  declared inventory, the loan layers, or the culture are sound (Dijkstra: a
  test shows the presence, never the absence, of defects).

## 5. Reviewer checklist

1. For every form-bearing record, name its kind and the routing row (R1–R6) that fixed it.
2. Check the companion the row requires; a kind without its companion is an incomplete record, not a routed one.
3. Re-run one negative control from §3 and confirm it still fails.
4. Confirm every `hold` row is carried, not dropped, and that no `hold` was read as a pass.
5. Record the projector revision and packet digest the run was measured on; a routing verdict without a revision is unreproducible.

## 6. Decision record — the routing rules this entry adopts

1. **Adopted:** routing is a decision procedure over declared record fields (R1–R6), not a judgement about a string's *look*. Consequence: the same string can route differently across packets if the declared inventory differs, and that is correct — the declaration is the contract.
2. **Adopted:** a gloss is never graded on the sound or identity channel, and the owed form slot stays held (R1/R3). Consequence: a packet with glosses can never read fully clean; it reads clean-with-holds, and the holds are design debt.
3. **Adopted:** a native form and a loan are distinguished by the T3 discriminator count, never by resemblance (R4/R5). Consequence: exactly one discriminator yields `to-verify`, not a default kind.
4. **Adopted:** the two clocks opened by `borrowed-strata` are never intersected (T4). Consequence: the lane gives up a manufactured date rather than a false precision.
5. **Rejected:** treating a green projector run as a clearance. Reason: it asserts byte-level typing over one packet, not soundness, not attestation, and not canon (§4).
6. **Open (to-verify):** whether the same routing vocabulary should be shared with the D2/D3 pipelines' readers without per-family adapters — the round-17 typed-support fragments measured a culture-boundness (`examples/culture-d4/ASSEMBLY.md` §4 records `tools/d2-typed-labels.py` refusing the D4 packet on `packet.eras`). Owner: this lane's D-axis; not disposed here.
