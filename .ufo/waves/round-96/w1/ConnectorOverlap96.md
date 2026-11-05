# ConnectorOverlap96 — Report (round 96, w1, attempt 1, milestone r96-v1)

**Seat:** ConnectorOverlap96  
**Judged axis:** Adjacency  
**Surface:** `corpus/knowledge/linguistics/oath-blessing-curse-formulae.md` (Claim C)  
**Main stage output:** `.ufo/waves/round-96/w1/stage/ConnectorOverlap96/overlap.md` (sha256: `c930692ef19c0104cb293691babf2573bd12340cf19aa7a94750c97073e32321`)  
**Frozen files:** Untouched (`claims.json`, `predispatch.py`, `predispatch-base.txt`, `reports/round-95/`).  
**Tooling record:** None installed or updated.  

---

## 1. Work Performed

1. **Sibling Province Scan:** Scanned all 20 sibling `PROVINCE.md` files via `ls -d /home/vgpnk/Projects/shokunin/*-shokunin/PROVINCE.md` (rc=0, 21 paths). Read Domain, Owns, and Refuses sections without reading sibling corpora beyond grep.
2. **Term Grep on Sibling Boundaries:** Grepped all 20 sibling `PROVINCE.md` and 18 sibling `SKILL.md` files for `oath|curse|blessing|malediction|imprecation|vow|sanction|ordeal|witness|performative`. Categorized every occurrence as reference craft or research-method verification; verified that zero sibling lanes claim the linguistic, cultural, or religious formula surface as owned.
3. **Lane Internal Grep:** Grepped `corpus/knowledge/**/*.md` (267 files) for topic lines containing the terms (14 matching files) and `corpus/SOURCES.md` (898 rows) for `teaches` cells (9 matching rows: S797, S811, S839, S840, S901, S905, S929, S945, S950). Formulated single-sentence boundaries for `sacred-registers-liturgical-language.md`, `politeness-taboo-euphemism.md`, `taboo-strata-lifecycle.md`, `synthesis/taboo-euphemism-lifecycle.md`, `synthesis/deity-name-derivation-pipeline.md`, `semantics-pragmatics.md`, `myth-symbol/binding-speech-complex.md`, `petitionary-and-votive-formulae.md`, and `ordeal-judicial-proof-rituals.md`.
4. **Owner Verdicts:** Evaluated all 20 adjacent owners against `PROVINCE.md`. Assigned `Boundary to respect` to `lore-shokunin` (canon refusal; handoff via `worldbible-integration-contract.md`) and `chousa-shokunin` (research method vs reference craft). Assigned `No overlap` to the remaining 18 siblings.
5. **Unreadable Files:** Checked filesystem readability across all inspected sibling files: 0 files unreadable (all returned rc=0).
6. **Contested Scope:** Identified at most three boundary seams for L1 routing to the L0 channel.
7. **Connector Proposal:** Synthesized the Four-Slot Syntax Blueprint (`[Witness Invocation] + [Performative Verb] + [Stipulation] + [Sanction Clause / Self-Imprecation]`) with unbound entity variables to satisfy Claim C while strictly preventing canon bleed and partition redundancy.

---

## 2. Table of Owners with Verdicts

| Adjacent Owner | Verdict | Boundary / Justification |
|---|---|---|
| `lore-shokunin` | **Boundary to respect** | Lore owns world-bible canon, entities, and landed events. Kotodama PROVINCE.md explicitly refuses claiming or recording canon. The new entry must supply generative grammatical rules, clause slots, and non-canon exemplars only. Specific historical covenants or vows belong to lore. Handoff defined in `worldbible-integration-contract.md`. |
| `chousa-shokunin` | **Boundary to respect** | Chousa owns deep-research methodology, question framing, and source hierarchy. Kotodama PROVINCE.md refuses general research method. Kotodama cites epigraphic and historical texts under `SOURCES-CONTRACT-v1` as reference craft without establishing independent research-method standards. |
| `audio-shokunin` | **No overlap** | Game audio SFX/music production does not cover linguistic formula grammar. |
| `game-dev-2d-shokunin` | **No overlap** | 2D game loops, physics, and gameplay mechanics do not cover linguistic formula grammar. |
| `game-dev-3d-shokunin` | **No overlap** | 3D rendering and physics do not cover linguistic formula grammar. Sibling SKILL hits for "witness" are non-author verification probes. |
| `kagi-shokunin` | **No overlap** | Secret operations and credential hygiene do not overlap. SKILL hits for "witness" are mutation test fixtures. |
| `kaidoku-shokunin` | **No overlap** | Shipped binary reverse engineering does not overlap. PROVINCE/SKILL hits for "witness" are raw environment and capsule audit probes. |
| `kake-shokunin` | **No overlap** | Web property hosting and publishing do not overlap with linguistic formula design. |
| `kama-shokunin` | **No overlap** | Local model serving endpoint health does not overlap. SKILL hits for "witness" are server replay execution probes. |
| `kasegi-shokunin` | **No overlap** | Bounty programs and vulnerability packages do not overlap with linguistic formula design. |
| `kengaku-shokunin` | **No overlap** | LLM benchmark evaluations do not overlap with linguistic formula grammar. |
| `kotoba-shokunin` | **No overlap** | Prompt and skill craft do not overlap with linguistic worldbuilding grammar. |
| `kumitate-shokunin` | **No overlap** | Orchestration and ufo-fsd tooling do not overlap with linguistic formula design. |
| `mado-shokunin` | **No overlap** | Desktop/compositor configuration craft does not overlap. Hits for "witness" are compositor test harness rules. |
| `mori-shokunin` | **No overlap** | Fleet observability does not overlap. Hits for "witness" are ledger counters. |
| `revenger-shokunin` | **No overlap** | Binary and APK reverse engineering do not overlap with linguistic formula design. |
| `souji-shokunin` | **No overlap** | Git repo hygiene and workspace sweep do not overlap. Hits for "witness" are test fixtures. |
| `tabi-shokunin` | **No overlap** | Browser automation does not overlap. Hits for "witness" are CDP DOM/keystroke states; hit for "self-blessing" is a test runner rule. |
| `tameshi-shokunin` | **No overlap** | Verification-fixture craft does not overlap. Hits for "witness" are declared-witness studies. |
| `tsukuroi-shokunin` | **No overlap** | Host operability and package repair do not overlap. Hits for "witness" are pacman hook execution probes. |

---

## 3. Measured Commands and Return Codes

| Measurement / Step | Command Executed | Return Code | Observed Value |
|---|---|---|---|
| Sibling PROVINCE.md count | `ls -d /home/vgpnk/Projects/shokunin/*-shokunin/PROVINCE.md \| wc -l` | rc=0 | 21 paths (20 siblings, 1 lane) |
| Sibling SKILL.md count | `ls -d /home/vgpnk/Projects/shokunin/*-shokunin/SKILL.md \| wc -l` | rc=0 | 19 paths (18 siblings, 1 lane) |
| Kotodama HEAD rev | `git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin rev-parse HEAD` | rc=0 | `063f70c9ab9aed5297741773292ded6d713d537a` |
| Kotodama knowledge files | `python3 -c "import glob; print(len(glob.glob('corpus/knowledge/**/*.md', recursive=True)))"` | rc=0 | 267 files |
| Sibling PROVINCE term matches | Python regex search over 20 sibling PROVINCE.md | rc=0 | 3 lanes with hits (`kaidoku`, `mado`, `tabi`), all 15 hits for `witness` (reference craft) |
| Sibling SKILL term matches | Python regex search over 18 sibling SKILL.md | rc=0 | 16 lanes with hits, all for `witness` (reference craft / gate tracing) plus 1 metaphorical `self-blessing` in `tabi` |
| Lane topic-line hits | `grep -nE '^- topic:.*\b(oath\|curse\|...)\b' corpus/knowledge/**/*.md` | rc=0 | 14 files |
| Lane SOURCES.md rows | `grep -cE '^\| *S[0-9]{3,}' corpus/SOURCES.md` | rc=0 | 898 rows |
| Lane SOURCES teaches hits | Python regex search over `corpus/SOURCES.md` teaches column | rc=0 | 9 qualifying rows (S797, S811, S839, S840, S901, S905, S929, S945, S950) |
| Unreadable files count | Python filesystem accessibility sweep | rc=0 | 0 unreadable files |
| Main output sha256 | `sha256sum stage/ConnectorOverlap96/overlap.md` | rc=0 | `c930692ef19c0104cb293691babf2573bd12340cf19aa7a94750c97073e32321` |

---

## 4. Contested-Scope Items for L1 Routing to L0

1. **Canon Pledge Text vs Generative Linguistic Formula (`lore-shokunin` vs `kotodama-shokunin`):**  
   *Seam:* When a worldbuilding system includes core oaths (e.g. night watch vow, coronation oath), does the text belong to lore-shokunin as world-bible canon or kotodama as linguistic formula design?  
   *Resolution:* Kotodama owns the abstract grammatical formula with unbound tokens (`[Witness]`, `[Sanction]`); once instantiated with specific historical characters, factions, and dates in a world bible, the pledge belongs strictly to lore-shokunin.

2. **Epigraphic Corpus Sourcing Authority vs Research Hierarchy (`chousa-shokunin` vs `kotodama-shokunin`):**  
   *Seam:* When mining epigraphic tablets (*defixiones*) or ancient Near Eastern treaties for linguistic formula anatomy, does evaluating critical editions and translations infringe upon chousa's deep-research source hierarchy?  
   *Resolution:* Chousa owns source hierarchy and verification methodology; kotodama acts within reference craft by citing peer-reviewed critical editions (Tier A) under `SOURCES-CONTRACT-v1` without establishing independent research-method rules.

3. **Macro-Metaphysical Binding Systems vs Micro-Syntactic Utterance Grammar (Internal Partition: `myth-symbol` vs `linguistics`):**  
   *Seam:* `myth-symbol/binding-speech-complex.md` owns the four channels (oath, curse, blessing, name-power), the executor triangle, and curse physics. If `linguistics/oath-blessing-curse-formulae.md` defines cosmological consequences or metaphysical transmission, it duplicates `binding-speech-complex.md`.  
   *Resolution:* Maintain a strict partition boundary: `linguistics` owns formula syntax, performative verbs, register morphology, and phonetic delivery; `myth-symbol` owns cosmological executor models, pantheon witness roles, and material curse carriers. The linguistics entry must cite `binding-speech-complex.md` for macro-enforcement rather than re-theorizing it.

---

## 5. Connector Proposal: Four-Slot Syntax Blueprint

- **Evidence:** Claim C requires `corpus/knowledge/linguistics/oath-blessing-curse-formulae.md` with >= 6 H2 headings, a table >= 5 rows x >= 3 cols, >= 4 frozen phrases, exact topic line, and >= 3 new mined registry rows. `lore-shokunin` PROVINCE.md refuses canon and marks kotodama packet intake as uncovered (CM-g). `binding-speech-complex.md` already covers macro-enforcement.
- **Affected axes:** Coverage (Claim C legs C1–C7), Adjacency (Province compliance, lore boundary), Operability (predispatch pass).
- **Proposed move:** Structure `oath-blessing-curse-formulae.md` around a standardized Four-Slot Syntax Blueprint:
  $$\text{Formula} = [\text{Witness Invocation}] + [\text{Performative Verb}] + [\text{Stipulation}] + [\text{Sanction Clause / Self-Imprecation}]$$
  Parameterize all exemplars with unbound tokens (`{DEITY_INVOKED}`, `{SANCTION_TARGET}`), map them across Sacred, Legal, and Everyday registers, and pre-format the output to match `worldbible-integration-contract.md` for seamless lore intake.
- **Risks & Mitigation:** Risk of canon bleed eliminated by using unbound variables. Risk of partition overlap eliminated by one-way link to `binding-speech-complex.md` for macro-physics.
- **Verification:** Verified by `predispatch.py` leg C1, zero named world-bible entities, and clean census validation.
