# Adjacent-Owner Overlap Scan — Oath, Blessing, and Curse Formulae Surface

**Seat:** ConnectorOverlap96  
**Milestone:** r96-v1 (round 96, wave 1, attempt 1)  
**Lane:** kotodama-shokunin (linguistic-cultural worldbuilding)  
**Surface:** `corpus/knowledge/linguistics/oath-blessing-curse-formulae.md` (Claim C)  
**Date:** 2026-11-05  

---

## 1. Sibling PROVINCE.md Scan

Command: `ls -d /home/vgpnk/Projects/shokunin/*-shokunin/PROVINCE.md` (rc=0, 21 paths: 20 siblings + 1 current lane).  
Each sibling file was inspected for its `Domain:`, `Owns:`, and `Refuses:` declarations.

| Sibling Lane | Domain Summary | Owns Scope | Refuses Scope |
|---|---|---|---|
| **audio-shokunin** | Game audio production | SFX (UI, impacts, movement, ambience) and music assets | Perceptual-quality claims without a measurable proxy; publishing |
| **chousa-shokunin** | Deep-research method (調査) | Question framing; source hierarchy; citation chaining; claim-vs-source verification; search-strategy taxonomy | Bounty scope; model quality; orchestration; unapproved live targets; secrets |
| **game-dev-2d-shokunin** | 2D game production | 2D game loop, input, physics, scenes, camera, UI, levels, juice | Engine source mutation; store submission; asset rights; narrative canon (lore) |
| **game-dev-3d-shokunin** | 3D game production | 3D game loop, physics, lighting, cameras, headless fixtures | Engine source mutation; publishing; store submission |
| **kagi-shokunin** | Secrets & vault operations | Secret management, the-janitor credential flows, vault hygiene | Scope outside secrets/vaults |
| **kaidoku-shokunin** | Reverse engineering of shipped artifacts | Shipped artifact analysis with REA on Linux, observation/inference ledgers | Live-target execution outside declared target; non-REA domains |
| **kake-shokunin** | Web properties & publishing | ds4cc.com, kimi.page/pro mirrors, Cloudflare Pages deploys | Scope outside web properties/publishing |
| **kama-shokunin** | Local model serving & endpoint health | Local LLM endpoints, baseURL discovery, llama.cpp/vLLM server health | Model quality/eval (kengaku); credentials (kagi) |
| **kasegi-shokunin** | Bounty & security research | Program rules, scope boundaries, vulnerability claim packages | Scope outside bounty programs |
| **kengaku-shokunin** | LLM/model research & evaluation | LLM benchmark evaluation, prompt route telemetry, llm-wiki | Scope outside model research/eval |
| **kotoba-shokunin** | Prompt & skill craft | SKILL.md/AGENTS.md quality, trigger fidelity, prompt construction | Scope outside prompt/skill craft |
| **kumitate-shokunin** | Orchestration & tooling | OMP task/hub, ufo-fsd runtime scripts, wave orchestration | Scope outside orchestration/tooling |
| **lore-shokunin** | Fictional-world records | Fictional-world entities, relations, timeline events, consistency verification | Claiming canon without in-world citation; silently resolving contradictions; game mechanics (game-dev) |
| **mado-shokunin** | Desktop & compositor craft | Hyprland, waybar, walker configuration, terminal themes | Secrets in configs (kagi); model endpoints (kama) |
| **mori-shokunin** | Fleet & host observability (森) | Watchdog liveness, resource monitors, wave settlement states | Dispatch mechanism (kumitate); OS packages (tsukuroi) |
| **revenger-shokunin** | Reverse engineering of shipped artifacts | Shipped binary/package reverse engineering with evidence ledger | Live targets beyond declared lifecycle |
| **souji-shokunin** | Fleet repository & workspace hygiene | Git workspace cleanup, drift audit, receipt-gated hygiene | Scope outside repo hygiene |
| **tabi-shokunin** | Browser & web-interaction craft | Web interaction via kimi-webbridge, CDP browser automation | Reverse engineering as forensics (revenger/kaidoku) |
| **tameshi-shokunin** | Verification-fixture craft | Reusable verification method, gate mutation-testing | Product domains — every lane keeps its own gate |
| **tsukuroi-shokunin** | Host operability & system repair | OS packages (pacman), systemd units, drivers, boot repair | Model serving (kama); secrets (kagi) |

---

## 2. Sibling PROVINCE.md and SKILL.md Term Grep

Command: Grep over all 20 sibling `PROVINCE.md` and 18 sibling `SKILL.md` files for regex `\b(oath|curse|blessing|malediction|imprecation|vow|sanction|ordeal|witness|performative)\b` (case-insensitive).

### Findings by Sibling

1. **audio-shokunin**: 0 hits in PROVINCE.md; 0 hits in SKILL.md.
2. **chousa-shokunin**: 0 hits in PROVINCE.md. 12 hits in `SKILL.md` (lines 97, 98, 102, 103, 116, 682, 696, 697, 709, 727, 734, 735). All hits are for `witness` (e.g. `argv-witness`, `mechanism-witness`, `WITNESS_SEPARATED`).
   - *Nature of claim:* **Research method verification craft** (execution tracing of research-gate matchers and query engines). None claim linguistic or cultural oaths/curses.
3. **game-dev-2d-shokunin**: 0 hits in PROVINCE.md; 0 hits in SKILL.md.
4. **game-dev-3d-shokunin**: 0 hits in PROVINCE.md. 2 hits in `SKILL.md` (lines 49, 189) for `witness` ("F7 witness", row-probe witness).
   - *Nature of claim:* **Reference craft** (verification non-author audit witness).
5. **kagi-shokunin**: 0 hits in PROVINCE.md. 2 hits in `SKILL.md` (lines 825, 826) for `witness` ("M39-6 red witness").
   - *Nature of claim:* **Reference craft** (mutation-testing red witness fixture).
6. **kaidoku-shokunin**: 6 hits in `PROVINCE.md` (lines 544, 546, 552, 556, 560, 571) and 13 hits in `SKILL.md` (lines 1152, 1196, 1579, 1581, 1585, 1602, 1945, 1993, 1996, 2003, 2105, 2107, 2115). All hits are for `witness` ("raw-witness capsule audit", "kernel-side environment witness", "execution witness").
   - *Nature of claim:* **Reference craft** (software reverse-engineering observation probe and receipt verification).
7. **kake-shokunin**: 0 hits in PROVINCE.md. 2 hits in `SKILL.md` (lines 948, 1155) for `witness` ("checkout commit witness", "30-witness counter").
   - *Nature of claim:* **Reference craft** (git commit inspection witness).
8. **kama-shokunin**: 0 hits in PROVINCE.md. 22 hits in `SKILL.md` (e.g. lines 702, 829, 1044, 1530, 1536, 1539) for `witness` ("replay execution witness", "red-green-witness.py", "witness hold").
   - *Nature of claim:* **Reference craft** (LLM endpoint replay verification).
9. **kasegi-shokunin**: 0 hits in PROVINCE.md. 1 hit in `SKILL.md` (line 1100) for `witness` (probe witness).
   - *Nature of claim:* **Reference craft** (bounty claim probe witness).
10. **kengaku-shokunin**: 0 hits in PROVINCE.md. 9 hits in `SKILL.md` (lines 604, 620, 622, etc.) for `witness` (counter witness).
    - *Nature of claim:* **Reference craft** (model evaluation counter witness).
11. **kotoba-shokunin**: 0 hits in PROVINCE.md. 1 hit in `SKILL.md` (line 275) for `witness` ("derivation, not a re-run").
    - *Nature of claim:* **Reference craft** (prompt derivation witness).
12. **kumitate-shokunin**: 0 hits in PROVINCE.md. 1 hit in `SKILL.md` (line 369) for `witness` ("20-witness preflight").
    - *Nature of claim:* **Reference craft** (orchestrator execution preflight).
13. **lore-shokunin**: 0 hits in PROVINCE.md; 0 hits in SKILL.md.
14. **mado-shokunin**: 4 hits in `PROVINCE.md` (lines 367, 370, 390, 396) and 7 hits in `SKILL.md` (lines 310, 828, 829, etc.) for `witness` (`c1-r74-witness-rule.py`, `replay-witness`, `harness-witness`).
    - *Nature of claim:* **Reference craft** (compositor fixture witness).
15. **mori-shokunin**: 0 hits in PROVINCE.md. 5 hits in `SKILL.md` (lines 183, 190, 1037, 1078, 1365) for `witness` (ledger counter witness).
    - *Nature of claim:* **Reference craft** (observability ledger witness).
16. **revenger-shokunin**: 0 hits in PROVINCE.md; 0 hits in SKILL.md.
17. **souji-shokunin**: 0 hits in PROVINCE.md. 4 hits in `SKILL.md` (lines 245, 262, 265, 282) for `witness` ("baseline witness", "child-env witness").
    - *Nature of claim:* **Reference craft** (repo hygiene test witness).
18. **tabi-shokunin**: 5 hits in `PROVINCE.md` (lines 77, 100, 109, 116, 137) and 48 hits in `SKILL.md` for `witness` (CDP wire capture, keystroke witness, DOM state witness); 1 hit in `SKILL.md` (line 1678) for `blessing` ("no runtime self-blessing" — a gate that does not validate itself).
    - *Nature of claim:* **Reference craft** (browser automation fixture test verification).
19. **tameshi-shokunin**: 0 hits in PROVINCE.md. 12 hits in `SKILL.md` (lines 1546, 1549, 1580, 1595, etc.) for `witness` ("bash declared-witness study", "witness metadata companion").
    - *Nature of claim:* **Reference / verification craft** (tameshi's explicit craft of verification fixtures).
20. **tsukuroi-shokunin**: 0 hits in PROVINCE.md. 15 hits in `SKILL.md` (lines 3184, 3190, 4554, etc.) for `witness` ("Executed witness", "Witness on this host").
    - *Nature of claim:* **Reference craft** (system operability observation witness).

### Synthesis of Sibling Grep
**Zero** sibling lanes claim oath, curse, blessing, malediction, imprecation, vow, sanction, ordeal, or performative as owned surface. All occurrences of `witness` in siblings belong exclusively to technical software verification terminology (observation probes, execution records, test pass receipts). No sibling owns linguistic formula grammar or speech acts.

---

## 3. Lane Internal Grep (kotodama-shokunin)

### Topic Lines in `corpus/knowledge/**/*.md` (267 files total)
Scanning `grep -nE '^- topic:.*\b(oath|curse|blessing|malediction|imprecation|vow|sanction|ordeal|witness|performative)\b' corpus/knowledge/**/*.md` yielded 14 files:

1. `corpus/knowledge/civilizations/scythian-saka.md:2` [oath] — *Owner: civilizations partition*
2. `corpus/knowledge/culture-material/ritual-garments.md:3` [performative] — *Owner: culture-material partition*
3. `corpus/knowledge/linguistics/petitionary-and-votive-formulae.md:3` [vow] — *Owner: linguistics partition*
4. `corpus/knowledge/myth-symbol/animal-symbolism.md:3` [performative] — *Owner: myth-symbol partition*
5. `corpus/knowledge/myth-symbol/binding-speech-complex.md:4` [oath] — *Owner: myth-symbol partition*
6. `corpus/knowledge/myth-symbol/death-afterlife-eschatology.md:4` [ordeal] — *Owner: myth-symbol partition*
7. `corpus/knowledge/myth-symbol/guest-right-hospitality-law.md:3` [oath] — *Owner: myth-symbol partition*
8. `corpus/knowledge/myth-symbol/mineral-stone-symbolism.md:5` [witness] — *Owner: myth-symbol partition*
9. `corpus/knowledge/myth-symbol/ordeal-judicial-proof-rituals.md:3` [oath] — *Owner: myth-symbol partition*
10. `corpus/knowledge/myth-symbol/purity-pollution-boundary-systems.md:4` [ordeal] — *Owner: myth-symbol partition*
11. `corpus/knowledge/myth-symbol/ritual-liminality.md:3` [performative] — *Owner: myth-symbol partition*
12. `corpus/knowledge/myth-symbol/sacred-kingship-mythic-charter.md:3` [oath] — *Owner: myth-symbol partition*
13. `corpus/knowledge/myth-symbol/witchcraft-sorcery-accusation-institution.md:3` [oath] — *Owner: myth-symbol partition*
14. `corpus/knowledge/verification/verification-independence-anti-circularity.md:3` [blessing] — *Owner: verification partition*

### Teaches Cells in `corpus/SOURCES.md` (898 rows total)
Scanning the `teaches` column across all rows for the terms yielded 9 qualifying rows:
1. **S797** [witness] (`used-by: corpus/knowledge/culture-material/scent-perfume-aromatics-codes.md`): Pliny's unguent survey as a primary-witness map.
2. **S811** [witness] (`used-by: corpus/knowledge/culture-material/medicine-healing-codes.md`): Ebers papyrus as oldest witness to Egyptian healing practice.
3. **S839** [vow] (`used-by: corpus/knowledge/culture-material/hair-grooming-codes.md`): Numbers 6:5 Nazirite vow regarding hair growth.
4. **S840** [vow] (`used-by: corpus/knowledge/culture-material/hair-grooming-codes.md`): Rastafari locks justified by the Nazarite vow.
5. **S901** [oath] (`used-by: corpus/knowledge/myth-symbol/ordeal-judicial-proof-rituals.md`, `.../witchcraft-sorcery-accusation-institution.md`): Coupling oath (who may swear), body (which element decides), and exit.
6. **S905** [sanction] (`used-by: corpus/knowledge/myth-symbol/guest-right-hospitality-law.md`, `.../marriage-alliance-bridewealth.md`, `.../witchcraft-sorcery-accusation-institution.md`): Hospitality as an institution with a religious sanction.
7. **S929** [witness] (`used-by: corpus/lessons/round-87.md`): Fictional exercise audit separating witness, origin, collection, and design clocks.
8. **S945** [vow] (`used-by: corpus/knowledge/linguistics/petitionary-and-votive-formulae.md`): Vocative address vs prayer/vow/supplication registers.
9. **S950** [curse] (`used-by: corpus/lessons/round-90.md`): Compelling gods, spirits or the dead classified as a curse register distinct from petition/vow.

---

### Topic Lines and Single-Sentence Boundary Statements

1. **`corpus/knowledge/linguistics/sacred-registers-liturgical-language.md`**  
   *Topic line:* The linguistics of a register system whose high variety is reserved for the sacred: the sacred specialization of diglossia (H allocated to ritual events, learned without native acquisition, kept by institutions rather than speakers); the six-competence model of sacred-language skill (hearing recognition, recitation accuracy, liturgical literacy, comprehension, composition, authorization) and how ritual events map to the competences they require; the mechanics of liturgical fossilization, per layer, with the maintenance institutions each freeze needs; event-typed language rules (recitation, sermon, petition, hymn, naming, authorized translation differ in what competence they demand and what counts as a violation); recitation norms and chant as phonological preservation engines; and the design procedure for a fictional sacred register whose fossil depth matches its culture's history.  
   *Boundary statement:* While `sacred-registers-liturgical-language.md` governs institutional diglossia, speaker competence hierarchies, and liturgical fossilization mechanisms of high sacred varieties, `oath-blessing-curse-formulae.md` governs the micro-syntactic formula grammar (invoked witness, conditional sanction, self-imprecation, performative verb) across sacred, legal, and everyday registers.

2. **`corpus/knowledge/linguistics/politeness-taboo-euphemism.md`**  
   *Topic line:* How cultures regulate saying — politeness theory (Brown & Levinson and its critics), honorific systems as grammar (Japanese, Korean, Javanese, Thai/Vietnamese), taboo vocabulary and its sanctions, euphemism cycles and the euphemism treadmill, and the fossil strata taboo leaves in lexicon, calendar, and law — with construction procedures for fictional cultures.  
   *Boundary statement:* While `politeness-taboo-euphemism.md` governs conversational face-management, honorific morphology, and the social avoidance of forbidden words, `oath-blessing-curse-formulae.md` governs overt, assertive performative speech acts that deliberately invoke legal or supernatural sanctions.

3. **`corpus/knowledge/linguistics/taboo-strata-lifecycle.md`**  
   *Topic line:* the lexical-diachronic lifecycle of a forbidden word as a **form-history**: the inventory of form-building operations a taboo substitution can be minted with (mincing, compound circumlocution and its univerbation, semantic shift, borrowing, graphic substitution, reading substitution, understatement, clipping/initialism); the word-level lifecycle states (plain → charged → substituted → fossil or live rung → replaced or reanalyzed) as a branching state graph, never a universal ladder; and the **read-off** — the procedure for ordering the strata a taboo deposits in a lexicon against each other and against the language's other dated strata, using four bracketing tests (sound-law bracketing, loan bracketing, legal/orthographic bracketing, semantic-field coherence).  
   *Boundary statement:* While `taboo-strata-lifecycle.md` traces the historical phonological and morphological replacement stages of individual suppressed lexemes, `oath-blessing-curse-formulae.md` specifies the multi-clause syntactic templates and pragmatic force that make an oath, blessing, or curse binding upon its parties.

4. **`corpus/knowledge/synthesis/taboo-euphemism-lifecycle.md`**  
   *Topic line:* In-world taboo drift across eras: competing euphemisms, minced forms, fossilized replacements, and the limits of using their distribution to date fictional documents, rituals, names, symbols, and dress.  
   *Boundary statement:* While `synthesis/taboo-euphemism-lifecycle.md` provides chronological diagnostic methods for dating fictional artifacts via euphemistic decay, `oath-blessing-curse-formulae.md` provides generative construction rules for the verbal formulae that establish covenants, invocations, and conditional punishments.

5. **`corpus/knowledge/synthesis/deity-name-derivation-pipeline.md`**  
   *Topic line:* Derive era-specific divine naming systems by coupling linguistic history, cult address, myth, symbols, and material display; distinguish transparent and opaque names, epithet accumulation, interpretatio, and name avoidance without deciding fictional canon.  
   *Boundary statement:* While `deity-name-derivation-pipeline.md` generates the morphology, onomastics, and cultic epithets of divine figures, `oath-blessing-curse-formulae.md` treats the deity strictly as an abstract functional argument (the invoked witness/executor) within an operational formula slot without generating divine names or settling pantheon canon.

6. **`corpus/knowledge/linguistics/semantics-pragmatics.md`**  
   *Topic line:* how languages package meaning (semantic fields, polysemy, classifiers) and act through it (evidentials, implicature, speech acts, deixis) — named frameworks, comparative data, and design levers for a fictional culture's "meaning economy".  
   *Boundary statement:* While `semantics-pragmatics.md` surveys broad theoretical frameworks of linguistic pragmatics and Austinian illocutionary force, `oath-blessing-curse-formulae.md` develops the specialized worldbuilding engineering procedure for the sub-grammar of binding oaths, blessings, and curses.

7. **`corpus/knowledge/myth-symbol/binding-speech-complex.md`**  
   *Topic line:* the binding-speech complex as a designed system for a fictional culture — the four channels (oath, curse, blessing, name-power) treated as one machinery with four directions of binding, the binding triangle (speaker → word → executor) and the maxim that a word holds only where an executor exists; the master channel table (genre, binder, bound party, executor, sanction shape, release, failure mode, visibility); the oath in depth (formula anatomy: invocation / assertion / self-imprecation / uptake; the four enforcement models with attested exemplars; oath institutions — compurgation, the oath ring, the covenant archive, the oath-scroll; the oath-witness slot in a pantheon); the curse in depth (seven curse genres, curse physics: retention, transfer, decay, counter-curse; material carriers: lead tablet, bone, threshold, knot; the curse-breaker typology); the blessing in depth (the four blessing genres, blessing economics: scarcity, transferability, blessing-theft, the deathbed blessing; physical tokens: laying-on of hands, spit, breath, garment fringe); name-power in brief; and the failure modes that make binding speech cheap.  
   *Boundary statement:* While `myth-symbol/binding-speech-complex.md` governs the macro-institutional systems, executor enforcement models, material carriers, and metaphysical physics of binding speech, `linguistics/oath-blessing-curse-formulae.md` governs the micro-linguistic syntax, clause sequencing, performative verb choices, and register-specific grammar of the spoken utterances themselves.

8. **`corpus/knowledge/linguistics/petitionary-and-votive-formulae.md`**  
   *Topic line:* petitionary address and votive formulae: vocative address to deities, petition mood (imperative, optative, precative), the conditional vow, votive inscription grammar, prayer-register archaism and parallelism, design procedure and failure modes.  
   *Boundary statement:* While `petitionary-and-votive-formulae.md` governs supplicatory requests and conditional vows offered upward to deities for favors, `oath-blessing-curse-formulae.md` governs performative speech acts that bind mortal actors under penalty of sanction or project harm and favor outward through conditional curses and blessings.

9. **`corpus/knowledge/myth-symbol/ordeal-judicial-proof-rituals.md`**  
   *Topic line:* judicial proof as a ritual system for fictional cultures — the proof ladder (vindicatory oath → compurgation → ordeal → judicial battle), the boundary where an oath stops being enough and a body must be put at risk (the Frisian pleader's "deny my oath and fight me"), the ordeal menu (boiling water, red-hot iron carried a fixed number of steps, fire-walking, cold water, the morsel), the inspection grammar (hands examined for burn-traces and bound in leaves, the fixed step-count that makes the element falsifiable), the administrator's economy (a church that blesses the iron, fasts the parties, and whose records record the miracles that reverse outcomes), the official acquittal trickery that survives its own disbelief (mountebank fire-ordeal recipes, priest-assisted hot-water swaps, the host morsel that chokes only the guilty), and the decay ladder (how an ordeal system is dismantled from within: papal bans, royal inquests, jury trial).  
   *Boundary statement:* While `ordeal-judicial-proof-rituals.md` governs the somatic escalation and physical proof procedures when verbal oaths fail or are challenged, `oath-blessing-curse-formulae.md` governs the internal syntactic structure and verbal performance of the oath before somatic trial occurs.

---

## 4. Verdict per Adjacent Owner

| Owner Lane | Verdict | Justification & Boundary Enforcement |
|---|---|---|
| **lore-shokunin** | **Boundary to respect** | `lore-shokunin` owns fictional canon, entities, relations, and the world bible. Kotodama's PROVINCE.md explicitly refuses claiming or recording canon. The new entry must provide generative grammatical rules, clause slots, and non-canonical exemplars only, deferring any landed in-world history or specific covenants to `lore-shokunin`. Handoff occurs via `worldbible-integration-contract.md`. |
| **chousa-shokunin** | **Boundary to respect** | `chousa-shokunin` owns deep-research method, question framing, source hierarchy, and citation chaining. The new entry must cite primary and authoritative secondary sources under `SOURCES-CONTRACT-v1` as reference craft without establishing independent research-method standards or general claim-verification frameworks. |
| **game-dev-2d-shokunin** | **No overlap** | Mechanics verification refused by kotodama; 2D game loops and gameplay mechanics do not cover linguistic formula design. |
| **game-dev-3d-shokunin** | **No overlap** | 3D rendering, animation, and physics engines do not cover linguistic formula grammar. |
| **kagi-shokunin** | **No overlap** | Secret operations and credential hygiene do not overlap with linguistic formula design. |
| **kaidoku-shokunin** | **No overlap** | Reverse engineering of Linux binaries does not overlap with linguistic formula grammar. Sibling uses of "witness" are kernel environment and receipt probes. |
| **kake-shokunin** | **No overlap** | Web property hosting and publishing do not overlap with linguistic formula design. |
| **kama-shokunin** | **No overlap** | Local model serving health does not overlap with linguistic formula grammar. |
| **kasegi-shokunin** | **No overlap** | Bug bounty program rules do not overlap with linguistic formula design. |
| **kengaku-shokunin** | **No overlap** | LLM benchmark evaluations do not overlap with linguistic formula grammar. |
| **kotoba-shokunin** | **No overlap** | Prompt and skill craft do not overlap with linguistic worldbuilding grammar. |
| **kumitate-shokunin** | **No overlap** | Multi-agent orchestration and ufo-fsd tooling do not overlap with linguistic formula design. |
| **mado-shokunin** | **No overlap** | Desktop/compositor configuration craft does not overlap with linguistic formula design. |
| **mori-shokunin** | **No overlap** | Fleet observability and watchdog liveness do not overlap with linguistic formula design. |
| **revenger-shokunin** | **No overlap** | Reverse engineering of shipped packages does not overlap with linguistic formula design. |
| **souji-shokunin** | **No overlap** | Git hygiene and repository workspace sweeping do not overlap with linguistic formula design. |
| **tabi-shokunin** | **No overlap** | Browser automation and CDP navigation do not overlap with linguistic formula design. |
| **tameshi-shokunin** | **No overlap** | Reusable test fixtures and mutation-testing craft do not overlap with linguistic formula design. |
| **tsukuroi-shokunin** | **No overlap** | Linux system operability, package management, and systemd maintenance do not overlap with linguistic formula design. |
| **audio-shokunin** | **No overlap** | Audio asset synthesis (SFX, dialogue acoustics) does not overlap with linguistic syntactic grammar. |

---

## 5. Unreadable Sibling Files

**None.**  
Every candidate sibling file inspected (all 20 sibling `PROVINCE.md` files and 18 sibling `SKILL.md` files) was readable locally on the filesystem with exit code 0. No file was locked, absent, permission-denied, or corrupted.

---

## 6. Contested-Scope Items for L1 to Route to L0

The following three boundary seams are identified for the L1 to route to the L0 channel to ensure cross-lane consistency:

1. **Canon Pledge Text vs Generative Linguistic Formula (`lore-shokunin` vs `kotodama-shokunin`):**  
   When a fictional culture has a core institutional vow (e.g. coronation oath, night guard pledge, temple covenant), does the verbatim text constitute immutable world-bible canon (owned by lore) or a linguistic formula specimen (owned by kotodama)?  
   *Recommended L0 Resolution:* Kotodama owns the abstract formula grammar, slot syntax, and generative procedure using unbound tokens (`[Deity]`, `[Witness]`, `[Sanction]`); once an oath is fixed with specific historical characters, factions, and dates, the instantiated pledge belongs exclusively to lore-shokunin's canon bible.

2. **Epigraphic Formula Corpus Authority vs Research Sourcing Hierarchy (`chousa-shokunin` vs `kotodama-shokunin`):**  
   When kotodama mines epigraphic curse tablets (Greek/Roman *defixiones*) and ancient Near Eastern vassal treaties (e.g., Esarhaddon, Sefire) to calibrate formula clauses, does assessing the critical edition quality and transliteration authority infringe upon chousa's deep-research source hierarchy?  
   *Recommended L0 Resolution:* Chousa owns general source evaluation methodology; kotodama acts within reference craft by citing peer-reviewed critical editions (Tier A) under `SOURCES-CONTRACT-v1` without establishing independent research-method standards.

3. **Macro-Metaphysical Binding Systems vs Micro-Syntactic Utterance Grammar (Internal Partition: `myth-symbol` vs `linguistics`):**  
   `myth-symbol/binding-speech-complex.md` owns the four channels (oath, curse, blessing, name-power), the executor triangle, and curse physics. If `linguistics/oath-blessing-curse-formulae.md` begins specifying the cosmological consequences of oath-breaking or metaphysical transfer of curses, it duplicates `binding-speech-complex.md`.  
   *Recommended L0 Resolution:* Maintain a hard partition boundary: `linguistics` owns the clause syntax, performative verbs, register markers (sacred/legal/everyday), and phonetic delivery; `myth-symbol` owns the cosmological executor models, pantheon witness roles, and material curse carriers. The linguistics entry must cite `binding-speech-complex.md` for macro-enforcement rather than re-theorizing it.

---

## 7. Connector Synthesis Proposal

### Evidence
- In `kotodama-shokunin/reports/round-96/claims.json`, Claim C demands a new entry `corpus/knowledge/linguistics/oath-blessing-curse-formulae.md` containing >= 6 H2 headings, a table >= 5 data rows x >= 3 columns, >= 4 of the six frozen phrases (`"oath formula"`, `"blessing formula"`, `"curse formula"`, `"self-imprecation"`, `"witness invocation"`, `"sanction clause"`), byte-exact topic line, and >= 3 new mined registry rows S975+.
- In `lore-shokunin/PROVINCE.md:28-30`, lore declares `worldbible-integration-contract.md` unacknowledged (coverage row CM-g: "kotodama packet intake stay uncovered").
- In `kotodama-shokunin/corpus/knowledge/myth-symbol/binding-speech-complex.md`, the macro-enforcement triangle and channel table already exist.

### Affected Axes
- **Coverage (Claim C):** Directly satisfies all 7 legs (C1–C7) of Claim C.
- **Adjacency (Province Conformance):** Eliminates potential friction with `lore-shokunin` and prevents internal partition redundancy with `myth-symbol`.
- **Operability (Verification Safety):** Ensures predispatch C1 passes mechanically without risk of prose-level scope creep.

### Proposed Move
**The Four-Slot Syntax Blueprint with Unbound Entity Variables:**  
In `corpus/knowledge/linguistics/oath-blessing-curse-formulae.md`, organize the design procedure and master table around a rigorous four-slot grammatical structure:  
$$\text{Formula} = [\text{Witness Invocation}] + [\text{Performative Verb}] + [\text{Stipulation/Condition}] + [\text{Sanction Clause / Self-Imprecation}]$$  
- Parameterize all exemplars with bracketed unbound entity tokens (`{DEITY_INVOKED}`, `{COVENANT_STIPULATION}`, `{SANCTION_TARGET}`) rather than fictional historical entities, guaranteeing strict compliance with `PROVINCE.md:16` (refusal of canon).
- Map the four slots directly across the three required registers (**Sacred**, **Legal**, **Everyday**), highlighting differences in mood (optative vs imperative vs jussive), archaic morphology, and particle clitics.
- Pre-structure the output format of the design procedure to match the payload schema of `corpus/knowledge/synthesis/worldbible-integration-contract.md`, establishing an immediately ingestible packet for lore-shokunin's future CM-g integration.

### Risks
- *Risk 1 (Under-specification):* Making the formula slots too abstract could lead to vague entries that fail QUALITY criteria.  
  *Mitigation:* Ground every slot in attested historical comparative linguistics (e.g. Old Babylonian treaty clauses, Homeric swearing formulas, Latin devotio, Old Norse *eiðr*).
- *Risk 2 (Partition Blur):* Slipping into descriptions of how curses physically manifest or how gods punish violators.  
  *Mitigation:* Explicitly delegate sanction execution to `myth-symbol/binding-speech-complex.md` via one-way link.

### Verification
- `predispatch.py` leg C1: checks size >= 12,000 B, >= 6 H2 headings, table >= 5 rows x >= 3 cols, exact topic line, and frozen phrases.
- Absence of named world-bible entities (zero canon bleed).
- Grep sweep confirms clean one-way linkage to `binding-speech-complex.md`.
