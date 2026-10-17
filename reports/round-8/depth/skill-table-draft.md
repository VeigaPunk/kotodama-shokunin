# R8-D14 — label-typing decision table (draft for SKILL.md)

- worker: DEPTH R8-D14 (round 8, shard of claim D); deliverable: this file only.
- lands: orchestrator copies the two LANDING-READY blocks into `SKILL.md`
  (suggested: the decision table into the "Decision table" region or beside
  the existing "Using the evidence" rows; the error rows into the existing
  "Error patterns" table). Nothing in `SKILL.md` is edited by this worker.
- date: 2026-10-17 (UTC; receipt times below).
- revision at read time: `git rev-parse HEAD` → `cf338a713060f274269cdacb18cdc0085bb06aeb`
  (claims.json baseline `e7ca0fa…`; sibling workers edit this tree concurrently —
  every locator below names its file and line, and §8 pins the sha256 of each
  cited file as read).
- dependency state: `reports/round-8/depth/design-spec.md` (R8-D01) landed
  2026-10-17T20:18:40Z; `reports/round-8/depth/shard-parser.md` (R8-D03)
  landed 20:16Z; `tools/d2-typed-labels.py` (R8-D02) landed 20:20Z, and §3–§6
  below are aligned to its **executed** schema — kinds `native-form` /
  `translated-label` / `borrowed-strata` plus `fictional-coordinate` /
  `descriptive-gloss`; typing by declaration (`kind_source` / per-field
  defaults), never guessed from the text's language. The tool failed its own
  selftest at 20:23Z (`NameError: by_id` at `:1062`) and was repaired by D02
  by 20:25Z — `--selftest` now exits 0 (`selftest: 32/32 checks passed`) with
  `TMPDIR` on the root filesystem; full receipts in §7. Field
  names from the older 22-report prototype (`form_kind`, `display_label`)
  appear below only as the marked legacy mapping.
- scope: how a culture-packet record's candidate form is **typed** —
  `translated-label` vs `native-form` vs `borrowed-strata` — and what each kind
  may and may not feed into the checked channels. "Unresolved" is a *status* of
  a declared kind, not a fourth kind. This is a representation-typing rule, not
  a canon ruling, not a general phonology standard, and not real-language
  clearance.

## 1. What this table decides

A record can carry up to three different kinds of string: an English gloss a
reader sees, a form in the culture's own language, and a form that entered
that language from a contact donor. The lane's gates check exactly one of
them: the native form. Two round-7 defects and one round-4 artifact class all
come from the same failure — a string's *kind* was never typed, so the gate
graded whatever string it found. The frozen round-4 naming output emits 10
`PHON-INVENTORY` findings and **10 of 10 name English `GAR-*` garment labels**
(receipts §2.1): the gate graded translations against native phonotactics.
This table fixes the typing so that the checked channel, the held channel,
and the layer-record channel are chosen deliberately.

## 2. Receipts (commands, outputs, date)

All commands run 2026-10-17 in `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.

### 2.1 The artifact class (counts)

```sh
sha256sum tools/gates/frozen/round-4/naming-collision-gate.out
# 4d70252bdf7745dea76af07b41a94560b5789ff278cdbb5af4bf6924688bb19e
grep -c "PHON-INVENTORY" tools/gates/frozen/round-4/naming-collision-gate.out
# 10
grep "PHON-INVENTORY" tools/gates/frozen/round-4/naming-collision-gate.out | grep -c "GAR-"
# 10
grep -c 'id: GAR-' examples/culture-d2/components/11-costumes.yml   # 10
grep -c 'form_slot:'  examples/culture-d2/components/11-costumes.yml # 10
grep -c 'native_form' examples/culture-d2/components/11-costumes.yml # 0 (grep exit 1)
```

Ten costume records, ten form slots, zero native forms — and ten of ten
sound-channel findings name the English label, not a native form. The D2
lexicon already declares its layers and counts: `grep -c "layer: loan"` → 2,
`grep -c "layer: native"` → 34 (`05-lexicon.yml:34` declares exactly
"native 34, loan 2").

### 2.2 Negative sweeps

```sh
grep -rln "form_slot\|native_form\|form_kind" tools/gates/*.py tools/assemble-d2.py
# (no output; exit 1) — no gate or assembler source reads a typing field
grep -n "form_kind\|borrowed-strata\|label-typing" SKILL.md
# (no output; exit 1) — SKILL.md carries no label-typing table
```

The only `form_slot` occurrences under `tools/gates/` are inside a frozen
round-3 *input packet copy*, not code. `SKILL.md:197` carries one D3 row
("An English label contains spaces or sounds outside the native inventory →
Keep it as `display_label`…") but no general typing rule.

### 2.3 Executable label controls already committed

- D3 guard: only `native_form`/`spoken_form`/`written_form`/`forms`/`expected`
  values are phonotactically tested — "display_label/gloss/proposition and
  every other translated English field are deliberately never tested here"
  (`tools/check-evidence-coupling.py:941-943`); finding id `D3-NATIVE`
  (`:36-37`).
- D3 positive control: changing a costume's `display_label` stays clean
  (`examples/culture-d3/controls.json:7`); a consistent non-profile glyph in a
  native form is a domain rejection (`:117`).
- D2 prototype controls (legacy mapping: the prototype's `form_kind` /
  `display_label` / `native_form` names are superseded by the landed schema's
  `kind` / `text` / `label_id`): label-only records leave the sound channel and
  are all held; a translation claim over a violating native form still FAILs
  (`reports/supplement-opencode-1/22-label-representation.md:139-145`).
- D2 typed-label design spec (R8-D01, landed 2026-10-17T20:18:40Z): routing
  rules R1–R6, borrow-ledger checks B1–B6, finding codes
  `D2L-FORM-UNRESOLVED` / `D2L-BORROW` / `D2L-ERA` / `D2L-DATA`
  (`reports/round-8/depth/design-spec.md:150-215`); parser shard (R8-D03)
  carries the same three kind names with `E-LABEL-*` diagnostics
  (`reports/round-8/depth/shard-parser.md` §2–§3).

## 3. Label-typing decision table — LANDING-READY

Grounding: `corpus/knowledge/synthesis/era-language-staging.md:108` — "type
every label" — with its label-type table `:110-121` (a later museum label "is
not automatically the wearer's garment term", `:121`) and `:124` (apply sound
laws to an inherited spoken label; track an unchanged written form, learned
rereading, translation, exonym, or official replacement separately). The
reject condition "A modern curatorial label becomes an attested historical
native word" is `corpus/knowledge/synthesis/costume-language-coupling-table.md:40`.

> Suggested SKILL.md intro line: "Type every form-bearing record before any
> gate reads it. The checked channel holds one form per record; a gloss is
> never that form, and a loan is never typed by its look."

| Condition on the record | Kind and status | Checked channel | Required companions | Wrong-typing consequence |
|---|---|---|---|---|
| Text is a reader-facing gloss (declared gloss field, whitespace/gloss syntax, or a segment outside the declared inventory) | `translated-label` | **never** — not on the sound or identity channel | `label_id` + `owner`; when the native form is still owed, the form slot stays held | grading a gloss against native phonotactics manufactures representation artifacts — 10/10 of the frozen round-4 `PHON-INVENTORY` class are this |
| A supplied native form exists | `native-form`, `status: supplied` | sound + identity; exactly one checked form per record | script/representation/scheme, `era_ids`, evidence | a translation claim cannot waive it: native bytes govern, still FAIL |
| Sound kind declared, no bytes supplied | `native-form` / `borrowed-strata`, `status: absent` or `to-verify` | nothing checked | owner + form slot + reason | silent pass forbidden — `D2L-FORM-UNRESOLVED` HOLD, never clean |
| Supplied form passes the declared inventory **and** ≥2 borrowed-strata discriminators (§4.3) hold | `borrowed-strata`, `status: supplied` | the recipient-adapted form against the recipient inventory, **plus** borrow-ledger checks: layer resolves, donor separated, substitutions reproduce the form, clocks ordered, domain/register declared | layer ref, donor {immediate / ultimate / carrier}, donor form + substitutions, entry stage, referent availability, channel, register/domain | mistyping a loan as native erases the contact clock; mistyping a native word as a loan invents a contact history |
| Exactly 1 discriminator holds | kind not asserted; `status: to-verify` with the one discriminator named | nothing | the discriminator that holds, stated | do not default to either kind |
| Untyped legacy record | no kind | unchanged channel — its legacy form field is still checked | — | adding typing fields cannot exempt a string from checking |

Three cautions that are part of the rule, not footnotes:

1. **Inventory-legal is not native.** A string that passes the declared
   inventory can still be an English gloss (any short lowercase word), so the
   inventory test routes strings *away* from the native channel; it never
   proves nativeness. Provenance (which record, which owner, which evidence)
   decides. The converse is safe: whitespace, gloss punctuation, or an
   out-of-inventory segment can never be a native form.
2. **A label is not a gap-filler.** Removing a gloss from the sound channel
   removes an artifact; it does not clear the name. The aggregate stays red
   with the missing forms held as `D2L-FORM-UNRESOLVED` (prototype controls
   C1/C1b, C4), and `compare_only` is not a licensed exemption channel for an
   unresolved typed label (design spec R3, `design-spec.md:155-158`).
3. **A label is not history.** A translated or curatorial label never becomes
   an attested historical native word by repetition
   (`costume-language-coupling-table.md:40`), and sound laws apply to an
   inherited spoken label — not to its translation, exonym, or official
   replacement (`era-language-staging.md:124`).

## 4. Thresholds

### 4.1 T1 — channel-eligibility thresholds (hard, deterministic)

- Native-eligibility: every segment is in the declared inventory **and** the
  form tokenizes under the declared syllable profile. D3's declared profile:
  `(C)V(C)`, coda subset `[n,l,r,s]`, `onset_clusters=false`, ASCII lowercase
  native spellings; "English translated labels are never phonotactically
  tested" (`reports/round-7/d3-contract.json:17`; guard implementation
  `tools/check-evidence-coupling.py:941-943`).
- Label signature (sufficient to route off the sound channel): whitespace,
  parentheses/semicolon gloss syntax, any out-of-inventory segment, or a
  record-declared gloss/translation provenance. All ten `GAR-*` labels carry
  parenthesised English prose (`11-costumes.yml:217-386`), which is why all
  ten fail the inventory as *labels*, not as names.

### 4.2 T2 — identity threshold (hard)

Exactly one checked form per record; `native_form` present ⇒ it is the
checked form (sound + identity); a contradiction between a translation claim
and native bytes ⇒ the native bytes govern; a declared native type with no
bytes ⇒ HOLD (`reports/supplement-opencode-1/22-label-representation.md:118-134`,
controls `:139-145`). Gate A uniqueness keys must be built from the native
form, not the display label (`:156`).

### 4.3 T3 — borrowed-strata discriminator threshold (house rule, ≥2 of 5)

The corpus supplies the discriminators; the count is this lane's house
threshold, stated as house design, not an external standard. The landed design
spec carries them as the borrow block's `alternative_checks` and makes D3/D5
concrete (layer resolves; donor separated; substitutions reproduce the form) —
`reports/round-8/depth/design-spec.md` §1.4.

| # | Discriminator | Holds when | Source |
|---|---|---|---|
| D1 | Recurring correspondences | the form participates in a recurring correspondence set with a **named donor stage** — not a lookalike ("resemblance alone cannot distinguish inheritance, chance, borrowing, or a shared earlier loan") | `loanword-material-dating.md:46`; `language-contact.md:78` |
| D2 | Donor-side chronology | the form preserves pre-change donor input or reflects a donor innovation | `loanword-material-dating.md:54`; `language-contact.md:135-136` |
| D3 | Channel separation | ultimate etymon, immediate donor, and carrier are recorded as separate facts | `loanword-material-dating.md:44` |
| D4 | Field/register clustering | the form sits in a semantic field consistent with a named contact event type (trade → food/cloth/measures; mission → religion/soul; conquest → war/law) | `language-contact.md:139`; `loanword-material-dating.md:57` |
| D5 | Witness + usage status | a dated witness is recorded and use is typed as quotation / code-switching / established use | `loanword-material-dating.md:43` |

**≥2 hold → `borrowed-strata`; exactly 1 → `to-verify`; 0 → native default.**
The native default is not a finding that the word is native — only that no
contact evidence was declared. Record which discriminators were checked and
which failed.

### 4.4 T4 — clock separation (hard, executable)

Typing `borrowed-strata` opens a **second clock**. The word-entry interval is
not the referent-arrival interval: a borrowed cloth word can later name a
local weave; "date the **sense–referent pairing**, not merely the word's
oldest ancestor" (`loanword-material-dating.md:60`; clocks table `:26`). Do
not intersect the loan interval with an object/deposition interval to
manufacture a date — the §10 toy exercise keeps "after 120, by 152" (word)
and 148–155 (burial) deliberately separate, and `:122` warns that a ruler, a
ruler-dated artifact, and an artifact-dated loan can be **one circular
argument**. Stratigraphy corollaries that make this clock usable:
`language-contact.md:133-139`.

Executable form (design spec B4): `entry_stage` earlier than
`referent_available_from` ⇒ `D2L-BORROW` FAIL
(`reports/round-8/depth/design-spec.md:206-212`, citing `05-lexicon.yml:185` —
"naming date and arrival date are different facts").

### 4.5 T5 — stratum-share calibration band (sample-based, not a rule)

WOLD's 1,460-meaning / 41-language sample: mean borrowing ≈24% of the list;
**no language in the sample is loan-free**; spread from Selice Romani ≈63%
and English ≈41% down to Mandarin ≈4%; nouns 31.2% > adjectives 15.2% >
verbs 14% (`language-contact.md:56-62`). Use as a sanity band when a packet
declares strata: a fully loan-free lexicon, or a core flooded far past the
sample's top, needs a stated contact story rather than silence. The
hierarchies are sample-based averages — prestige, religion, and literacy
override word class (`language-contact.md:52`), so the band never overrides a
packet's own declared history.

## 5. Error patterns — LANDING-READY

| Observation | Reading | Evidence |
|---|---|---|
| An English garment label fails the native inventory | representation-channel artifact, not a name violation; type the record or hold the owed form — never rename the garment to "fix" the gate | frozen round-4 output (10/10 `GAR-*`); `reports/supplement-opencode-1/22-label-representation.md` §1 |
| A label-only record passes silently | forbidden: label-only → off the sound channel **and** a hold, so the aggregate stays red | `22-label-representation.md:126-128`; controls C1/C1b; executable `TL-01` hold (`tools/d2-typed-labels.py:316-320`) |
| A translation claim made over a violating native form | cannot waive: native bytes govern, still FAIL | `22-label-representation.md:129-130`; control C2 |
| A sound kind declared with no bytes supplied | HOLD, not clean | `22-label-representation.md:131-132`; control C3; executable `TL-01` |
| An untyped legacy label | still checked; typing fields cannot exempt a string | `22-label-representation.md:133-134`; control C4 |
| A record with no declared kind at all | hold with a stable reason — the kind is never guessed from the text's language | `tools/d2-typed-labels.py:126-135`, `:386-390` (`TL-02`) |
| `compare_only` set while the typed label is unresolved | misuse, not a pass — the unresolved hold stands | design spec R3, `reports/round-8/depth/design-spec.md:155-158` |
| A borrowed form judged only against the native stratum | misfile: loans pass through the recipient's phonotactic filter and carry donor provenance; every stratum-1 loan "should look mouth-shaped for its borrowers" | `language-contact.md:78-79`, `:168` |
| A loan's oldest form used to date the referent's arrival | clock conflation; keep word-entry and object-arrival intervals separate | `loanword-material-dating.md:26`, `:60`; executable B4 |
| A loanword that switched referent in transit (Mandarin male gown → English female dress) | keep both coexisting names; date the sense–referent pairing | `garment-lexicon-crosslinguistic.md:26`; `loanword-material-dating.md:60` |
| Imported prestige terminology for locally made goods read as evidence of import | dictionary/selection bias; check local manufacture under imported labels | `loanword-material-dating.md:57` |
| A modern/curatorial label promoted to an attested historical native word | reject or split: the label is typed as a label; the term keeps its own record | `costume-language-coupling-table.md:40`; `era-language-staging.md:121` |
| A translation, exonym, or official replacement run through the inherited-form sound laws | track separately: sound laws apply to the inherited spoken label, not its translation or replacement | `era-language-staging.md:124` |
| Era tags or slot glosses graded on the name/sound channel (the 6 NAME-NEAR findings on E0–E3 tags) | type them: `fictional-coordinate` for era labels, `descriptive-gloss` for slot glosses; neither enters the sound channel | `22-label-representation.md` §3 (flagged class); tool `FIELD_DEFAULTS` (`tools/d2-typed-labels.py:126-135`) |
| Missing native forms counted as cleared names | a gap, not clearance | `SKILL.md:98` (existing row) |
| A transliteration collision read as native-script identity | compare per declared scheme; a collision in that output channel is not native identity | `naming-collision-gate.md:69-70` |
| A shared garment label across cultures read as identical cut or status | labels are neither cut nor status | `naming-collision-gate.md:52` |

## 6. Typed record shape per kind (schema alignment)

Executable authority is `tools/d2-typed-labels.py` (landed 2026-10-17T20:20Z;
repaired 20:25Z; sha256 `623b5b1f…` at read time); its design authority is
`reports/round-8/depth/design-spec.md` §1 (landed 20:18:40Z, sha256
`f1d57cda…`). The tool ships **five** kinds: the three the round claim names
(`native-form`, `translated-label`, `borrowed-strata`) plus
`fictional-coordinate` and `descriptive-gloss` (`tools/d2-typed-labels.py:84-103`).

| Kind | What it denotes | Checked channel | Tool rule (`d2-typed-labels.py`) |
|---|---|---|---|
| `translated-label` | analyst-language (English) descriptive label | **never** | "never quoted as in-world speech and never substituted for a native form" (`:90-92`) |
| `native-form` | in-world surface form coined in the culture's own language | sound + identity; one supplied sound form per record | must name stage/era scope and owning component; a `(to-verify)` placeholder "is unresolved and is never emitted as a native form" (`:86-88`) |
| `borrowed-strata` | form carried in the declared contact/loan layer | checked as a recipient string, plus layer checks | must name its layer (the stratum); "the loan layer is a declared stratum, not a style" (`:94-96`) |
| `fictional-coordinate` | position on the culture's own timeline (era tag, named era) | never a sound form | "not a CE/BCE date and not a claim about any real period" (`:97-99`) |
| `descriptive-gloss` | the analyst's gloss of a required term or slot | **never** | "carries no form claim; a gloss is not a label and cannot fill a form slot" (`:100-102`) |

Typing is **by declaration, never guessed from the text's language**
(`tools/d2-typed-labels.py:10-11`, `:126-135`): every record carries a
`kind_source` of `inline-annotation`, `declared-default` (per-field defaults —
`costumes.garment → translated-label`, `costumes.form_slot → native-form`,
`lexicon.term → from the record's own layer`), or `unannotated` → `TL-02`
hold. Executable holds: `TL-01` = a form slot with no native form; `TL-02` =
no declared kind (`:316-320`, `:386-390`). Legacy mapping: the 22-report
prototype's `form_kind` / `display_label` / `native_form` names
(`22-label-representation.md:118-121`) and the D3 contract's `display_label` /
`native_form` (`d3-contract.json:13`, `:17`, `:20`, `:33`, `:71`) name the same
split; map by semantics, not spelling. The design spec's status vocabulary
(`supplied` / `to-verify` / `absent`) maps to the tool's `declared` /
`unresolved`.

## 7. Limits — what this table does not establish

- Typing is representation discipline, not clearance: separate representation
  "is not real-language clearance" (`SKILL.md:197`), a native form is not
  thereby "real", and a loan's declared donor is not thereby historical.
- T3's count (≥2) and T5's band are house design; the discriminators and
  numbers are cited, the thresholds are this lane's policy and may be revised
  with evidence. The executable tool enforces the declaration, hold and
  borrow-ledger rules — not T3/T5.
- Tool selftest receipts, 2026-10-17. `python3 tools/d2-typed-labels.py
  --selftest` first exited 1 for an environmental reason — `/tmp` is at
  **100% inode use** (`df -i /tmp` → `tmpfs 1048576 1048576 0 100% /tmp`;
  `echo x > /tmp/d14-test.txt` → "No space left on device" despite 8.5G free
  space), so any scratch-writing selftest fails before its logic runs. With
  `TMPDIR` on the root filesystem, the then-current revision (sha256
  `13e82857…`) failed on a genuine defect — `NameError: name 'by_id' is not
  defined` at `:1062` in `build_artifact` (`selftest: 0/2 checks passed`).
  D02 repaired it (`by_id` now defined at `:1011`); on the current revision
  (sha256 `623b5b1f…`) the same command exits **0** with `selftest: 32/32
  checks passed — … no file outside the temporary directory touched`
  (receipt run 2026-10-17T20:25Z, `TMPDIR=$PWD/.d14-scratch2`, scratch
  removed after the run). Caveat for any future run: without a `TMPDIR`
  redirect, the `/tmp` inode exhaustion still fails the run environmentally.
- The D2 example's ten labels remain on the legacy gate's checked channel
  until the gate's own reader is changed by its owner
  (`22-label-representation.md:300-303`); this draft changes no packet, gate,
  or count.
- No web retrievals were made for this shard; every citation is a repo file
  with a line locator and the sha256 pin in §8.

## 8. Sources and locators

Repo-relative; sha256 as read 2026-10-17 (working tree at `cf338a7`; the
round-8 sibling artifacts landed mid-shard and their hashes are as read at
20:19–20:25Z).

| Path | sha256 | Used for |
|---|---|---|
| `reports/supplement-opencode-1/22-label-representation.md` | `5493b3f7a4c8e1b056ca0cdc7112c84e9ce43b6cb89ef47926bc88bdeacb3364` | typed contract, rules, controls, the ten-label evidence |
| `corpus/knowledge/linguistics/language-contact.md` | `3d4d77749bd894b063ceb6f03427f7d1052af0d7ee667a975912765747509507` | adaptation, stratigraphy, WOLD band, contact scale |
| `corpus/knowledge/synthesis/loanword-material-dating.md` | `bb08d4585033d856aaccb6b3548cfb8ce598ad226db4648d878109b9188e6fd8` | strata rules, discriminators, clocks, circularity |
| `corpus/knowledge/culture-material/garment-lexicon-crosslinguistic.md` | `10fba861fb2919f496fb3032450373d8bd7ccf3e84e75b465d27924725e024bf` | referent-switch case, doublet slot division, HJ trove |
| `corpus/knowledge/verification/naming-collision-gate.md` | `60491baec7b1aa916432cf1e27cebac0d3ac3a093d57c6cbec997ecfc48b2b1d` | name-use fields, transliteration/shared-label cautions |
| `corpus/knowledge/synthesis/cultural-translation-protocol.md` | `cf21c777d5db4c591eb07e35e1bc0f4829aed3b01a0d6abd3b37351e96127593` | rendering convention (`:33`) |
| `corpus/knowledge/synthesis/glossary-registry-format.md` | `043a4e3b9f525f4a9a7ed51e982c515e5ba3e861d4ffc0605987f1ad37caeee3` | translation-vs-record separation (`:21`, `:38`, `:53`) |
| `corpus/knowledge/synthesis/era-language-staging.md` | `621b7a33c06ff15f5d179059e8ce856b7d22b51f5601787831956f4bf4a91da8` | "type every label" (`:108`), label-type table (`:110-121`), separate tracking (`:124`, `:139`) |
| `corpus/knowledge/synthesis/costume-language-coupling-table.md` | `e856d40882ef4e9cc5727f27057a1773b7ddbe9c7a405379613155838fe7e0bc` | curatorial-label reject condition (`:40`) |
| `SKILL.md` | `ca940f4d872952607baa5421f90c019b63f1e2dc29d2b0108cff30490a95b35b` | existing rows (`:98`, `:186`, `:197`) |
| `examples/culture-d2/components/11-costumes.yml` | `b6e2c5c29cc5d68900d6cde5a8487e64f27d85ecb3d2bd7f3f5beb1113483f22` | ten labels, ten slots, zero native forms, layer sentence (`:418`) |
| `examples/culture-d2/components/05-lexicon.yml` | `9bdcb8d895be0592047260361c4c12493569e7d38318b3508a5bde314d87abdf` | layer record shape, loan adaptation note |
| `examples/culture-d2/components/01-brief.yml` | `ea0d67d0179aba4b118016f32f6cbf0d5e0dde92b1e8468ee6535e5026f2ea19` | CP-08 contact discipline (`:114`) |
| `examples/culture-d3/controls.json` | `f00ccf7aac931fb23719e4c3715f0e987c924fc79d7f9881236567d260d2ae70` | label-positive and native-negative controls |
| `tools/check-evidence-coupling.py` | `849494b0c4113885223f6d865110cd34ed6bb3aeec8b449d020f7b571eb2197e` | D3-NATIVE docstring and tested-field list |
| `reports/round-7/d3-contract.json` | `8969b1c89945720b0e53314759aa78f358d12bd339e0f6f35dd6ada56e261093` | D3 typed-label semantics |
| `tools/gates/frozen/round-4/naming-collision-gate.out` | `4d70252bdf7745dea76af07b41a94560b5789ff278cdbb5af4bf6924688bb19e` | the 10/10 artifact count |
| `reports/round-8/depth/design-spec.md` | `f1d57cda02457dac4c2151ac4ad08f97a445ddb1d41db50b281917b6199b58a7` | typed-label design authority (§1 kinds; routing R1–R6; borrow B1–B6) |
| `reports/round-8/depth/shard-parser.md` | `6d40b43f68ae9f97dea4ebf9d04eb92564c57b204dd13d4faeac388a1885460a` | parser shard: same three kind names, `E-LABEL-*` diagnostics |
| `tools/d2-typed-labels.py` | `623b5b1f2f9f50b3e306975b4107b5f70122e86e7d7b41aeca21bcb5a7979b03` (repaired 20:25Z; pre-repair revision `13e82857…`) | executed schema: five kinds, `kind_source`, `FIELD_DEFAULTS`, `TL-01`/`TL-02`; passing selftest receipt |

## 9. Landing instructions for the orchestrator

1. Paste §3 as a new subsection in `SKILL.md` (proposed heading: "Label
   typing — translated labels, native forms, borrowed strata") with the §4
   thresholds condensed to the T1–T4 bullets; keep §4.5 as a one-line
   calibration note.
2. Append the §5 rows to the existing "Error patterns" table.
3. Field names in §6 are already aligned to the landed tool
   (`tools/d2-typed-labels.py`, sha256 `623b5b1f…`); if the tool changes its
   names again, edit names in the landed copy only and record the alignment
   in the round log.
4. Before citing the D2 typing capability as working, re-run
   `python3 tools/d2-typed-labels.py --selftest` with `TMPDIR` on a
   non-inode-exhausted filesystem (the passing 32/32 receipt in §7 was taken
   that way); `/tmp` is at 100% inode use in this environment, which fails
   such runs environmentally regardless of tool state.
