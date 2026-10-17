# Round 6 — worker 14 review: linguistic/textual mediation (author-side)

- Reviewer: worker 14, kotodama-shokunin round 6; assignment: review actually completed source fragments 02–07 for direct passage vs metadata, script/language conflation, text versions/mediation, and partial-claim inflation.
- Date: 2026-10-17. Baseline revision: `030c3928de74ed514853bc1f7490e0f8bb4d451f`.
- Inputs read: `AGENTS.md`, `reports/round-6/claims.json`, `reports/round-6/targets.json`, `reports/round-6/baseline.json`, and the six entry files at their baseline bytes.
- Status: **author-side review only.** No admission, promotion, merge, or canon decision is made or implied here; parent owns integration and judgment.

## 1. Fragment availability at review time

One check, no polling (contract forbids waiting): `ls -la corpus/lessons/round-6-sources/` — the directory does not exist; `reports/round-6/` contains only `baseline.json`, `claims.json`, `dispatch-plan.json`, `prompt-template.txt`, `targets.json`.

| Fragment | Assignment / entry | Targets IDs | Status at 2026-10-17 |
|---|---|---|---|
| 02 | mesopotamia-sumer-akkad | R6-02-A, R6-02-B | **unreviewed — file absent** |
| 03 | egypt-ancient | R6-03-A, R6-03-B | **unreviewed — file absent** |
| 04 | aegean-minoan-mycenaean | R6-04-A, R6-04-B | **unreviewed — file absent** |
| 05 | anatolia-hittite | R6-05-A, R6-05-B | **unreviewed — file absent** |
| 06 | china-shang-zhou | R6-06-A, R6-06-B | **unreviewed — file absent** |
| 07 | levant-canaan-phoenician | R6-07-A, R6-07-B | **unreviewed — file absent** |

Per protocol, absence is recorded as **unreviewed**; this file predicts no fragment quality. Sections 2–4 supply the conformance checklist and bounded counterexamples for the parent's later review pass or a continuity re-review once fragments land. All entry anchors below are line numbers valid at the baseline bytes above; if an entry changes, anchors must be re-verified before reuse.

## 2. Schema-level mediation checks (apply to every audit row)

From `claims.json` → `source_schema`, with the linguistic-specific readings this lane exists to enforce:

1. `retrieved_passage=true` requires **actual source text** with locator plus a quotation ≤ 40 words. Search snippets, TOCs, bibliographic records, publisher blurbs, repository abstracts, catalogue/accession metadata, book jackets, and another worker's assertion are metadata, not passages.
2. `source_url`: exactly one HTTP(S) URL; anything else belongs in separately labelled optional fields. Identity metadata (accession number, CTH/KAI/tablet siglum, archive or pit ID) is a **locator** and can never serve as content confirmation.
3. Verdict/support discipline: verdicts limited to supported/contradicted/unresolved; `support_scope` must stay `partial` when only part of a compound claim is witnessed. Partial support never verifies the whole bounded claim.
4. `entry_claim` must be the entry's **actual bounded assertion with an entry locator**. If the entry does not assert the link the question presumes, the limit is recorded — not manufactured.
5. `retrieval_method`/`basis` must name the language, translation, edition, and mediator actually inspected. A translation of an unread primary licenses claims about the translation, not the primary's wording; a secondary quotation is not the unread primary.
6. Copy date vs composition date; archive siglum vs text; museum label vs object report — each audit should make its layer explicit (see per-entry anchors).

## 3. Per-assignment bounded counterexamples (grounded in baseline entry bytes)

Each item states the entry anchor (path:line at baseline) and what would constitute the named failure mode. These are falsifiable checks, not conclusions about the absent fragments.

### 02 — corpus/knowledge/civilizations/mesopotamia-sumer-akkad.md

Anchors: L36 (contact-ecology row: script survival ≠ speech-community survival), L44 (proto-cuneiform not securely Sumerian), L47 (transliteration / normalization / translation are distinct layers), L48 (Sumerian word-signs inside Akkadian writing), L61 (Ur III administrative language ≠ workers' mother tongue), L139 (carved texture: fleece/woven-pile/tufting/construction not uniquely established), L185–186 (entry's own verification boundary: Zawadzki repository record is metadata/abstract only; only bibliographic records and the two ETCSL translations were checked).

- **Terminology manufacture (targets R6-02-B):** the question's word "kaunakes" does not occur anywhere in this entry; the entry's tokens are "textured/flounced surfaces" and "tufting" (L139). If fragment 02-B records `entry_claim` = "the entry calls the garment kaunakes", that is a manufactured claim. The bounded entry claim is: carved texture does not uniquely establish fibre/construction; reconstruction is a proposal, object by object.
- **Metadata-as-passage:** a `retrieved_passage=true` row citing the Zawadzki ZORA repository page contradicts the entry's own boundary (L22, L186). The document-level route the entry itself names is Quillien (2019), open-access author copy (L23), which cites Sippar tablets such as BM 64798.
- **Script/language conflation (R6-02-A):** a passage about cuneiform sign lists, determinatives, or schools witnesses the **script/scribal layer**, not the institutional coupling of scribal-language survival against spoken replacement. The entry's checkable formulation is the L36 row plus the L61 guardrail; "precise end of spoken Sumerian" is explicitly contested (L191), so any audit verdict implying a settled replacement date is inflation.
- **Version conflation:** ETCSL translations are composites exposing manuscript variants (L24, L74); a quotation licenses claims about the composite translation, not any single tablet. A first-millennium copy preserves tradition without documenting earlier performance (L11).

### 03 — corpus/knowledge/civilizations/egypt-ancient.md

Anchors: L42 (rn/*ren* citation forms are not recovered recordings of speech), L60 (mdw-nṯr check locates R93 pp. 35–36), L13 (R93 printed pages, not PDF pages), L11 (A14's posted excerpt is Lesson 1, pp. 1–10), L17 (Hdt 2.37/2.81 via Macaulay at Lexundria; "a classical account, not evidence that the rules were universally observed"), L21+L147 (Louvre E 12026: linen plain weave, pleated sleeves/body, Assiut tomb 13, late Dyn. 11–early Dyn. 12; record itself warns it may not reflect latest scholarship), L110 (surviving Middle Kingdom pleated linen blocks "pleats invented in the New Kingdom"), L22 (verification boundary: K98 bibliographic records only; H06 metadata only).

- **Locator drift (R6-03-A):** the entry's mdw-ntr evidence is R93 pp. 35–36 (L60). A fragment quoting Ritner's chapter title, the SAOC landing page, or a PDF-page mismatched quotation fails direct passage.
- **Excerpt-scope inflation:** Allen 2014's posted excerpt covers Lesson 1 only (L11). Quoting it as support for name-efficacy (essays 6–8) or creation-word theology (essays 11–14) is partial-support inflation; the efficacy material lives in R93's named pages and A88's checked ranges.
- **Translation stacking:** Herodotus in Macaulay is a classical account inside a 19th-century translation (L17, L143). It supports "what Herodotus reports about priests' linen and wool restrictions", not the Egyptian rules themselves; using it to confirm practice is mediator inflation.
- **Pleating version (R6-03-B):** the dated-object anchor is Louvre E 12026 (L21, L147). A valid audit quotes the record's material description and bounds the inference at "pleating is already attested before the New Kingdom" (L110) — not a cutting/pleating reconstruction, which no cited passage supplies. Catalogue attribution ≠ reign chronology (L187-analog: entry L21 warning).

### 04 — corpus/knowledge/civilizations/aegean-minoan-mycenaean.md

Anchors: L52–56 (A is undeciphered; B-based transliterations are analytical notation; unsafe-inference row), L61 (transliteration hyphens divide signs, not spoken syllables/morphemes), L63 ("applying a Linear B value to a similar Linear A sign is not proof of its exact Minoan pronunciation, much less the word's meaning"), L11 (Salgarella 2022 OCD: undeciphered; unaffiliated; no bilingual), L103 (*da-ma-te* = Déméter is a contested etymological proposal, not a decipherment), L125–134 (fresco/figurine vs Linear B textile accounts vs surviving fragments are distinct evidence classes; L133: no secure one-to-one cloth-term-to-painted-outfit matching), L8 (depicted textiles are not surviving fabric samples).

- **Transliteration-as-reading (R6-04-A):** any passage that "reads" a Linear A sign group through B values as Minoan words or divine names fails L63. The safe content of an A document is structural (numbers, accounting, repeated commodity signs, L52–55). Sign similarity is explicitly not affiliation evidence (L56).
- **Abstract-as-passage:** Salgarella 2022's OCD entry is the correct witness for "undeciphered / no agreed family / no bilingual"; the audit must quote the encyclopedia's own assertion text, not its navigation or abstract metadata.
- **Textile version conflation (R6-04-B):** a Linear B textile/wool/personnel term supports archive categories only (L74, L133); painted costume and figurines are a separate class (L125–134). An audit claiming a tablet term identifies a fresco garment inverts the entry's evidence-class separation — exactly the leap targets R6-04-B names. No excavated octopus-patterned textile is claimed anywhere (L199).

### 05 — corpus/knowledge/civilizations/anatolia-hittite.md

Anchors: L11 (four separate categories: political Hatti / Hittite language / Hattic language / Anatolian family), L55 (Hattic: non-Indo-European; inherited cult names and liturgical passages within Hittite textual settings; no demonstrated Caucasian genealogy), L57 (a Sumerogram does not make the clause Sumerian), L45 (Old Hittite composition ≠ Old Script manuscript ≠ later copy), L61 (cuneiform/hieroglyphic Luwian name corpora through their scripts), L69 ("Hieroglyphic Hittite" label misleading about language), L84 (Tarḫunna-/Tarḫunt-/Teššub/Taru are distinct linguistic-cult traditions aligned in context), L111 (CTH numbers identify text groups, not single autographs), L132 vs L134 (divine pointed horned headgear vs royal rounded cap; exact textile/construction `(to-verify)`), L25 (Seeher's plates not inspected), L24 (Hawkins Iron Age corpus must not be backdated to the empire).

- **Label conflation (R6-05-A):** quoting a source for "Hieroglyphic Hittite" inscriptions as Hittite-language evidence repeats the mislabel (L69); the Iron Age hieroglyphic corpus is largely Luwian (L42, L46 row) and cannot be projected into the empire period (L24).
- **Catalogue metadata:** CTH numbers, corpus volume titles, or Yazılıkaya relief inventory entries are locators (L111, L126). Passage support must be translated tablet text (Hoffner 1998 route) or Hawkins/Beckman wording actually inspected.
- **Deity-assembly conflation:** one attested equation (e.g., storm-god translation across languages, L84) does not support a Hattic origin for the pointed cap or any universal icon; L132 leaves construction `(to-verify)` and L134 separates royal rounded cap from divine pointed horned headgear — merging them is partial-claim inflation against R6-05-B.
- **Copy-date inflation:** a ritual's late manuscript does not date the rite's institution (L45); festival-cult provenance (Hattic substrate names inside Hittite framing, L55) is linguistic transmission, not proof of Hattic speech community survival.

### 06 — corpus/knowledge/civilizations/china-shang-zhou.md

Anchors: L25 (oracle inscriptions "not a complete spoken-language sample or myth handbook"), L49 (earliest extensive securely readable corpus ≠ invention date), L50 (morphosyllabic/logographic with phonetic components; "pictures expressing universal ideas" misleading), L48 (pinyin is a modern finding aid), L94 (*tāotiè* is later naming practice), L99 (nine-ding/9-7-5 ladders not excavated law), L100 (later antiquarian vessel names ≠ what Shang makers called the form), L116 (*bi*/*cong* cosmic formulas come from transmitted *Zhouli*, a later prescriptive text), L12 (DB99 posted extracts are the oracle passages actually read), L20 (K78/Q00/BS14/S91 checked bibliographically, not re-read).

- **Bibliography-as-passage:** the entry's own boundary (L20) says Keightley, Qiu, Baxter–Sagart, and Shaughnessy were checked bibliographically only. A `retrieved_passage=true` row quoting their unread pages overclaims the demonstrated basis unless the worker genuinely retrieved the page; the entry's directly read oracle text is DB99's posted extracts (L12).
- **Transmitted-prescription back-projection (R6-06-B):** *Zhouli* bi/cong associations (L116), *tāotiè* (L94), antiquarian vessel names (L100), and numerical rank ladders (L99) are later normative/classificatory layers; using them to gloss Shang object terminology inverts the targets' separation of Shang object evidence, Zhou institutions, and later transmitted prescriptions.
- **Script=speech / genre census (R6-06-A):** the divination record's components (L59–65) are analytical categories over a selective royal archive (L25, L31); a charge's formulaic language witnesses the archive genre, not Shang speech at large or universal belief. A graph's pictorial motivation is not its meaning (L50).
- **Romanization as pronunciation:** pinyin *dǐng* vs *dīng* (L101) and all L48 forms are finding aids; a passage confirming a graph does not confirm Bronze Age sound values (L47; BS14 is a reconstruction model, L11).

### 07 — corpus/knowledge/civilizations/levant-canaan-phoenician.md

Anchors: L76 (mlqrt "king of the city"; civic semantics more productive than a fixed merchant-patron job), L78 (Herodotus 2.44 is "Greek inquiry and translation, not a Phoenician foundation chronicle"), L83 (Josephus citing Menander; translation route; rite reconstruction `(to-verify)`), L120–124 (Timna: wool fibres, chemical evidence; demonstrates consumption/connectivity, not Phoenician identity; production origins inference), L129 (Timna supports costly colored components, not necessarily a whole purple garment), L135 (no universal king-only statute established; do not back-project Roman/Byzantine restrictions), L171 (entry's directly inspected items: Timna paper, Louvre records, Herodotus' Tyrian passage, opening of Briquel-Chatonnet, publisher/bibliographic records — Bonnet, Krahmalkov, Gibson are reference leads, not inspected content), L175 (*phoinix*/*kinahhu* derivations are hypotheses).

- **Etymology metadata (R6-07-A):** an inscription naming *mlqrt* (e.g., Louvre AO 7676 bilingual, L80) attests name and cult, not the "king of the city" analysis. Support for the etymology needs a philological passage (grammar/lexicon/scholarship wording). Bonnet 1988 is a lead only per L171 — a fragment presenting direct Bonnet quotations as this wave's inspected basis overclaims unless it genuinely retrieved the text.
- **Translation chains:** Herodotus via Godley/Loeb (L16) supports Herodotus' report; Josephus/Whiston citing Menander is second-hand (L19, L83). Neither verifies Tyrian archives' content, and the priests' antiquity claim is their claim (L78).
- **Sumptuary inflation (R6-07-B):** Timna fragments support costly dyed components (L129) and inland consumption (L123); a "king-only purple law" is precisely the disallowed back-projection (L135). Greek *porphyra* and later Roman restrictions are external mediators, not native garment terms (L130, L138: derive garment lexicon from fibre/weave/finish/dye grade — do not pass modern labels off as attested Phoenician vocabulary).

## 4. Cross-cutting mediation requirements for every audit row

- Record which **language/edition/translation/mediator** was actually inspected (ETCSL English composite vs Sumerian; Macaulay vs Greek; Whiston vs Greek; Godley vs Greek; DB99 excerpt vs Keightley; museum label vs object report).
- Secondary quotation of an unread primary is not the primary; identity metadata is never content confirmation.
- Modern/analytic labels (Ennead, abjad, *tāotiè*, "lustral basin", kaunakes-style garment names) are conventional, not native terms — check the entry's own marked conventions before accepting an audit's `entry_claim`.
- If a fragment's `entry_claim` cannot be located in the entry at the cited locator, treat as manufactured until shown otherwise (re-check against baseline bytes, since line anchors above are baseline-bound).

## 5. Questions for parent (left here; not waiting on replies)

1. Will the parent re-dispatch a continuity review of 02–07 after fragments land, or apply §2–§3 directly during integration? §3's anchors are reusable as-is only against unchanged entry bytes.
2. Targets R6-02-B presumes "kaunakes" is entry vocabulary; it is not (checked at baseline bytes). Parent may wish to note this for worker 02's scribe so `entry_claim` is drawn from the entry's actual terms (L139), not the question's wording.
3. If any fragment lands with `source_kind=unavailable` after a real access failure, parent confirms intended handling (stays unresolved; identity metadata never converts it into content confirmation) — this matches claims.json but is worth an explicit instruction to scorers.

## 6. Limits of this review

- No fragment content was assessed; all six are named unreviewed per contract.
- No retrievals redone; no live gate selftests run; no corpus bytes, ledgers, or shared bookkeeping touched; only this assigned file written.
- Author-side review only; parent owns integration, judgment, and publication.

## 7. Actual-output review (appended after ledgers landed; §1–§6 retained as history)

Date: 2026-10-17 (same day, post-landing). Inputs: all six ledgers `corpus/lessons/round-6-sources/02.json`–`07.json`, re-checked against `targets.json`, `claims.json` `source_schema`, `baseline.json`, and the §3 anchors above. Reviewer retrievals redone: **exactly two** targeted re-fetches (FIT Timeline "Kaunakes"; UT Austin Hittite Online lesson 2), plus local greps of repo files and of the saved fetch outputs. No researcher retrieval was otherwise redone; no worker files edited; no commits.

### 7.1 Availability update (supersedes §1 statuses, which are retained as history)

| Fragment | Status at this append |
|---|---|
| 02, 03, 04, 05, 06, 07 | **present and reviewed** (all 12 audit rows, R6-02-A … R6-07-B) |

### 7.2 Conformance matrix (all twelve rows)

- Top-level fields (`round`, `baseline_revision`, `worker_scope`, `entry`, `entry_sha256_before`, `audits`) present in all six; every `entry_sha256_before` matches `baseline.json`.
- All 12 `question` strings match `targets.json` verbatim; IDs R6-02-A…R6-07-B complete (exactly two per assignment).
- Every row carries all 17 required `each_audit` fields; corroboration lives in separately labelled optional fields (`extra_corroboration`, `corroboration`, `corroboration_url`/`corroboration_note`), as the schema permits.
- `source_url`: one HTTP(S) URL per main source in every row. Excerpt word caps respected (02-B is exactly 40; others under).
- **No metadata-as-passage found**: every `retrieved_passage=true` row quotes actual retrieved page/PDF/record text. The two conservative demotions are correct: Jagersma's abstract (`02-A` corroboration) and Cleveland's texture-free object record (`02-B` corroboration) are `retrieved_passage=false`. Identity metadata (accessions, CTH/KAI sigla, tablet loci) never serves as content confirmation.
- Mediation is recorded in every `retrieval_method`/`basis`/`limits` (language, translation, edition, host). Translation-only status is disclosed wherever it applies (DB99 English; Zhouli transcription without translation; Wikipedia-embedded Herodotus/Josephus; French Louvre/Persée originals).
- Hygiene: bot-wall 403/429s and the pirated Killen scan refusal are recorded, not ground; raw files stay in workers' own ignored scratch subtrees; entry bytes reported unchanged against baseline hashes.

### 7.3 Per-row findings and exact row-ID scoped parent classification recommendations

Verdicts `supported` can in every case stand; the narrowings below are `support_scope` corrections only, for parent to apply row-ID scoped. "Confirmed" below means reviewer-verified against the named page or repo file.

- **R6-02-A — accept `supported`/`whole-bounded-claim` on the row as bounded (L36+L38), with a recorded tertiary-relay caveat.** Tertiary is honestly declared (`source_kind: tertiary`); the Wikipedia lead is real retrieved text. The question's "which dated text or scholarly passage" leg is **unresolved**: no scholarly passage was retrieved (Jagersma abstract is metadata, correctly `retrieved_passage=false`). If parent treats that leg as inside the claim, narrow to `partial`; otherwise record the caveat.
- **R6-02-B — accept; the pre-registered kaunakes trap is resolved correctly.** `entry_claim` explicitly records that "kaunakes" does not occur in the entry and bounds the claim to L139's non-uniqueness row. Reviewer re-fetch confirms the quoted Tortora sentence, the "Greek word kaunakes has been applied to both sheepskin and woven garments" sentence (same Tortora block — the ellipsis is a same-passage elision, not a cross-paragraph splice), and Kemper/Boucher wording verbatim. Both internal cross-references verify at cited lines: `corpus/knowledge/culture-material/dress-through-eras.md:30` and `corpus/lessons/round-1-triage/Z16.md:14`. Residual caveat for parent's classification note: the dated-object leg rests on tertiary mentions (Wikipedia kaunakes objects) not individually quoted, and no first-hand museum texture description was obtained (MET 429; Cleveland record texture-free — disclosed).
- **R6-03-A — accept; strongest row in the wave.** `secondary-scholarly`, printed-page locator (p. 35, header-verified), real Ritner passage; OCR transliteration garbling and the unread Harris Papyrus footnote disclosed. The "not every receipt is a spell" caution is spirit-supported, not passage-proven — worker disclosed it; keeping `whole` is defensible. Note for parent: the worker's open question about the A14 Lesson-1 excerpt slightly overreads — entry L60 already routes mdw-nṯr to R93, not to A14, so no entry defect is implied; any A14-locator clarifying edit is optional and parent-owned.
- **R6-03-B — accept `whole`.** Record descriptive fields (lin/toile/plissés/findspot/dating) are object-record content, not mere metadata; French mediation and the museum's own dating caveat disclosed; bibliography corroborations correctly labelled not-re-inspected.
- **R6-04-A — recommend parent narrow `support_scope`: `whole-bounded-claim` → `partial`.** Directly witnessed: undeciphered leg (Rutter 15, verbatim), readable-Greek leg (Rutter 26 divine-name lists; LiBER Ventris framing), no-image-to-name caution. Not directly witnessed by quoted text: "not securely assigned to any family" (Salgarella 2022 403; tested only indirectly — disclosed) and the da-ma-te-contested leg (Duhoux 1997 bibliographic-only — disclosed). Verdict `supported` stands as `partial`.
- **R6-04-B — accept `whole`.** Boloti's sentence plus the adjacent "hypothetical or dubious" sentence (quoted in `basis`) directly witness the no-one-to-one limit; cult-link corroborations carry their hedges. Note: the adjacent-sentence quotation sits in `basis` beyond the 40-word excerpt; optional parent spot-check of the Curis PDF.
- **R6-05-A — recommend parent narrow `support_scope`: `whole-bounded-claim` → `partial`; `source_kind` mislabel candidate.** Reviewer re-fetch confirms the UT quotes verbatim (Telipinu son of the Hattic Storm-god; "probably a copy of an even earlier version"; IṢ-BAT Akkadogram with "The Hittite reading is ēpta"), witnessing cult-provenance and copy-layer legs. But the **Hattic non-IE classification** and **no-demonstrated-Caucasian-genealogy** legs are quoted from no retrieved text, and a grep of the same fetched UT page finds no Hattic non-IE statement (its Indo-European material concerns Hittite itself). The Taru/Tarḫunt- name-forms are unconfirmed (worker discloses). Also: `repository-scholarship` is a mislabel candidate for an authored pedagogical teaching text — `secondary-scholarly` fits the entry's own framing; Wikipedia corroboration items are correctly `tertiary`. Minor internal drift: `basis` says "cuneiform adopted from Assyrian colonies" while the quoted intro sentence says the Hittites adopted cuneiform from the Hatti. Verdict `supported` stands as `partial`.
- **R6-05-B — accept `partial` (correctly self-narrowed).** Real retrieved text (Chamber A procession "horned hats"; Chamber B Sharruma/Tudḫaliya IV caption). Unwitnessed legs recorded: royal rounded-cap row (entry L134) is not covered by any retrieved text; Neo-Hittite and Hattic-era comparator legs unverified (disclosed); whether Sharruma's cap is horned unstated. `tertiary` declared.
- **R6-06-A — recommend parent narrow `support_scope`: `whole-bounded-claim` → `partial` (or re-bound the claim to the witnessed legs).** Directly witnessed: genre-limit leg (verbatim "highly selective record … relevant to the elite class"), paired/non-paired charge forms, ancestors/Di illness-harvest-settlement charges, verification-of-failure (childbearing 15B). Inference-carried legs: L49's "earliest extensive, securely readable" is only "consistent with" DB99's popularized "earliest written records" line, and "not a myth handbook" is absence-inference (worker discloses both). Mediation honest: English translation only, graphs/provenance unverified, BS14 language-family leg explicitly untested, Wu Ding dates not adopted. `primary-text` is an acceptable label for translated inscriptions given the disclosed mediator.
- **R6-06-B — accept `partial` (correctly self-scoped).** Verbatim match to entry L116's Zhouli quotation; prescriptive genre evidenced (six-jade rite, nine-grade ladder, graded garments); compilation-dating leg left open; non-projection caution labelled methodological; Wikisource's lack of critical apparatus and untranslated classical Chinese disclosed. Shanghai Museum corroboration correctly limited to provenience/attribution.
- **R6-07-A — accept `partial` (correctly self-set).** The Lipiński derivation arrives via tertiary relay (Wikipedia quoting Lipiński 2002 p. 235; original unopened — disclosed); Bonnet 1988 remains unread per the entry's own L171 boundary. The Persée corroboration is genuinely opened entry-cited scholarship (French original). Label note: the Herodotus/Josephus corroboration item is typed `secondary-scholarly` but is English translation embedded in a tertiary page — parent should count it as tertiary-mediated, not an independent classical witness.
- **R6-07-B — accept `whole` on the bounded lines 123–124 claim; the pre-registered Timna trap is avoided.** The "universal king-only wearing law" is handled exactly as required: "verified only as calibrated absence … not a proof that no restriction existed" (row `limits`), and the scope stays inside the Sukenik-backed sentences, each mapped to retrieved article text (HPLC identification, radiocarbon dating, Red-Sea/murex geography, "It is reasonable to suggest" hedging, biblical/Classical textual carriers of the elite register). Native-garment-term leg (entry L130) stays open as recorded.

### 7.4 Summary for parent

- Narrowings recommended (row-ID scoped): **R6-04-A, R6-05-A, R6-06-A** `whole-bounded-claim` → `partial`. All other rows: classifications stand as filed; caveat notes above are optional classification annotations, not corrections.
- Both known-trap checks positive: 02-B names the kaunakes absence and bounds the claim accordingly; 07-B keeps the no-law absence calibrated. The 05-A/06-A whole-claim inflation flagged by the parent is confirmed in the specific legs identified in §7.3.
- Threshold observation (author-side, not promotion verification): each ledger carries ≥2 distinct retrieved relevant non-bibliographic passages (main + corroboration), so the F shape (≥6 passages across ≥4 entries) is facially met with tertiary-relay qualifiers as noted; parent verifies keyed by URL+locator+excerpt independently.
- Reviewer verification footprint: two public re-fetches (FIT kaunakes page — quoted text verbatim-genuine; UT lesson 2 — quoted text verbatim-genuine, non-IE leg absent from page), local greps of `dress-through-eras.md:30`, `Z16.md:14`, and the saved UT fetch output. Not re-fetched by this reviewer (parent spot-checks own these): ISAC Ritner PDF, Curis Boloti PDF, PLOS Timna text, Louvre E 12026 / AO 7676 records, Shanghai Museum record, DB99 pages, Wikisource Zhouli, Wikipedia pages, Rutter/Dartmouth pages, BMCR, LiBER.
- No admission, promotion, merge, or canon decision is made here; worker ledgers are left untouched for parent reconciliation.
