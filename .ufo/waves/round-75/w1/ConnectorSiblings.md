# ConnectorSiblings — sibling-overlap scan: narrative-structure surface

Seat: ConnectorSiblings (connector, leaf). Lane: kotodama-shokunin. Base: f556d1049fe651d3d63975600b13acd9fb686f15.
Scope: does the narrative-structure surface (narratology as a worldbuilding design system: story/discourse split, actantial model, time axes, focalisation, three-layer story spec formats, narrative-generation models; Barthes/Todorov/Greimas and Chinese/Japanese scholarship) overlap a sibling province? Method: read every `*-shokunin/PROVINCE.md`; grep sibling `corpus/knowledge`, `corpus/README.md`, `corpus/SOURCES.md`, `SKILL.md`, and `.ufo/waves` for the narratology terms; read the lore boundary contract; read the shokuknow staging scopes that feed the claim-C entry (read-only).

## Verdict

**CONTESTED with `lore-shokunin`, narrow.** Secondary, weaker: `kengaku-shokunin` (only if LLM story-generation evaluation enters the entry), `chousa-shokunin` (source-acquisition method only; not a content overlap). No overlap with `kotoba`, `game-dev-2d`, `game-dev-3d`, `audio`, `revenger`, `kumitate`, `kake`, `mado`, `mori`, `souji`, `tsukuroi`, `kaidoku`, `kama`, `kagi`, `kasegi`, `tabi`, `tameshi`.

The narratology *vocabulary* is not contested. The contest is over one concept family: **discourse order / reveal order, focalisation (who knows what, when), and story time vs. discourse time.** That family is lore's own declared frontier (CM-f and the character-knowledge row), and it is also what a narratology design entry would most naturally specify.

## 1. Evidence: lore-shokunin (the contested sibling)

Lore's own province and coverage map name this exact ground as theirs to verify:

- `lore-shokunin/PROVINCE.md:19` — "CM-f reveal order vs chronology … stay `uncovered`."
- `lore-shokunin/PROVINCE.md:23` — Frontier: "reveal order vs chronology, in-world source reliability grading, character knowledge/memory state over time, continuity-error taxonomy crosswalk vs ConStory-Bench, kotodama packet intake."
- `lore-shokunin/corpus/README.md:72` — CM-f row, "reveal (narrative) order vs chronology … fabula/syuzhet … uncovered."
- `lore-shokunin/corpus/README.md:78` and `:90` — "the schema encodes integer ticks only … spoiler/discourse-order errors are uncheckable … define a non-tick reveal-order field or a per-cluster narrative-order map."
- `lore-shokunin/corpus/README.md:92` — character knowledge/memory state over time (Knowledge Contradictions).
- `lore-shokunin/corpus/README.md:93` — ConStory-Bench crosswalk.
- `lore-shokunin/corpus/SOURCES.md:18–20` — S010 (StoRM, reader-model story generation), S011 (FlawedFictions plot holes), S012 (ConStory-Bench, LLM long-story consistency taxonomy): all `queued`. These are the narrative-generation literature, held by lore.
- `lore-shokunin/corpus/SOURCES.md` S017/S015/S016 are rejected rows (per `corpus/lessons/round-103.md:52`), including ConStory-Checker as canon authority.

Lore's own pending work on the same ground, outside the lore repo:

- `.ufo/waves/kaika-w1/lore-art.md:18–19` — ART dossier re-reads ConStory, FlawedFictions, Qiu et al., StoRM as "useful failure modes"; `:45–49` proposes S018–S022 (StoRM, FlawedFictions, KG storytelling, Qiu, ConStory); `:57` proposes `continuity-error-taxonomy-crosswalk.md` as a Frontier item.
- shokuknow `.ufo/scopes/corpus-expansion-1/ScoutLore.md:19` assigns S033 (Fludernik, narratological glossary) to CM-f; `:38` proposes `corpus/knowledge/narrative-order-and-chronology.md` (S033, S034, S044); `:46–57` argues discourse order vs event chronology is distinct in Western, Japanese (物語 vs 筋, fabula/syuzhet) and Chinese (时序/时距/频率) literature; the knowledge-state entry (`character-knowledge-state.md`) cites S040, S041, S043 (黄灿, Chinese narratology, "what the character knows").

So lore is actively building the reveal-order and knowledge-state surface from the **same literatures** (Fludernik / 物語–筋 / Chinese narratology) that kotodama's claim C stages (S723 = Chinese narratology syllabus; S724/S725 = Japanese narratology of generation and three-layer story spec; S885–S892 = Barthes/Todorov/Greimas/S-Z/Marrone).

## 2. Evidence: kotodama's own narrative surface (what the overlap touches)

Shokuknow's staged narrative entry (read-only, `merge/kotodama/knowledge/corpus/knowledge/myth-symbol/narrative-structure-frameworks.md`) already bounds itself, and the bound is the right one:

- It "describes how narrative structure is theorised and specified so a worldbuilder can design one; it decides no culture's story (lore-shokunin owns canon)."
- §6 "A three-layer spec format — ストーリー / クエスト / シーン, with the キャラクター hierarchical sub-layer; the format a world bible can actually store."
- §9 "Coupling to the world bible — what to hand to lore-shokunin, and what not to."
- Barthes's levels of description and "what this lets a world bible do" are framed as checkable specification.

The risk is in §6 and §9: a "format a world bible can actually store" plus "checkable" language is a step into lore's reveal-order schema (CM-f) and knowledge-state gate. The entry should not specify either.

## 3. Evidence: in-lane overlap (not a sibling; relevant to claim C's own BEFORE text)

Claim C's BEFORE text (`reports/round-75/claims.json`, claim C `before` (a)) says the base tree has "no file governs narrative structure" and that `comparative-frameworks.md` and `hero-journey-variants.md` "neither names a structuralist narrative source." That is **false at base**. `git show f556d104…:corpus/knowledge/myth-symbol/comparative-frameworks.md` shows:

- line 15 — Propp (1928) and Greimas (1966), *Sémantique structurale*, "actantial model" in the sources block;
- line 78 — "Greimas (1966) generalizes Propp's roles into six **actants** — subject, object, sender, receiver, helper, opponent";
- §5 (line 73ff) — Propp/Dundes tale-grammar engine.

And `corpus/knowledge/culture-material/costume-semiotics.md:12,20` already cites Barthes (1967) *Système de la mode* and the 1957 Annales essay for fashion semiotics. The Barthes and Greimas surface is therefore partly in-lane already. Claim C adds Barthes 1966, Todorov 1966, Greimas 1966 on mythic narrative, S/Z, and the Chinese/Japanese scholarship; it does not create the first mention. The new entry must either cross-reference or de-duplicate `comparative-frameworks.md §5` (actantial/Propp) rather than re-teach it. This is an in-lane correctness fix to claim C's BEFORE text, not a sibling boundary.

## 4. Duplicate staging across shokuknow waves (same documents, different IDs)

Same underlying documents carry different campaign IDs; a row counter that dedupes by ID will not see the duplication.

- Chinese narratology syllabus (xushixue.pdf): `.ufo/scopes/corpus-expansion-1/ScoutKotodama.md:81` = S723; `lanes/kotodama/SOURCES-PROPOSED.md:62` = S864 (claim C row S888 cites it).
- Japanese narratology of generation (小方 孝, jcss/25/2/25_200): ScoutKotodama.md:82 = S724; SOURCES-PROPOSED.md:71 = S865 (claim C S889).
- Japanese three-layer spec (村井 源, jsik/32/2): ScoutKotodama.md:83 = S725; SOURCES-PROPOSED.md:80 = S866 (claim C S890).
- Barthes 1966 (Persée 1113): claim C stages it as S876/S885/S917/S921 (four IDs, one document; `claims.json` row S885 `staged` field).
- Todorov 1966 (Persée 1120) = S902; Greimas 1966 (Persée 1114) = S904 (SOURCES-PROPOSED.md:various).
- Chinese 世界观 essay 三九音域 (2023-09-22): S729 (round 1) = S761 = S787 = S870 (same URL and title).

Consequence for claim C: its row_set (S885–S892) is contiguous and does not include S864–S866, S902, S904 as-is, so no collision now, but the "staged" field lists a multi-ID mapping that the freeze must reconcile (ID-per-document, not ID-per-appearance), and S870 (chinawriter, refused round 72) is the same essay as S729. This is an integrator/ExecRenumber concern (cross-lane: the shokuknow pool is shared by lore and kotodama), flagged here, not decided.

## 5. Secondary siblings

- **kengaku-shokunin (LLM/model eval).** No narrative or story-generation content in `corpus/knowledge`, `SKILL.md`, or `PROVINCE.md` (grep: zero hits for narrative/story-generation terms). kengaku's cross-lane record is `kengaku-shokunin/.ufo/waves/round-32/falsify/FxConnector.md:56`, which notes lore rejected ConStory-Checker as authority because it is a model judge. Boundary: if the kotodama entry describes **computational / LLM story generation and its evaluation** (Japanese 物語生成 literature; StoRM; ConStory), the evaluation and judge-calibration claims route to kengaku (LLM eval craft). A design-side structural description (story/discourse, actants, three-layer spec) stays kotodama's. Current claim C does not assert an LLM evaluation result, so: **in-lane for the design side; route any generation-eval claim to kengaku.**
- **chousa-shokunin (research method).** No narrative content. Its J-STAGE and citation rows (`corpus/SOURCES.md:107,108,117`; `corpus/knowledge/japanese-search-record-r38.md:3`) are about how J-STAGE exposes citations, not narratology. Claim C's use of Persée per-page transcription and J-STAGE PDFs is source-acquisition practice: kotodama's QUALITY 10 governs admission, and chousa owns the research method and its external-target approval table (`chousa-shokunin/PROVINCE.md`). No province overlap; flag only that the Persée page-transcription service must not be used through any access control (already in claim C's kill rule).
- **game-dev-2d / game-dev-3d / audio / revenger.** Their PROVINCE files refuse "narrative canon (lore)" (`game-dev-2d-shokunin/PROVINCE.md:10`, `game-dev-3d-shokunin/PROVINCE.md:35`, `audio-shokunin/PROVINCE.md:15`, `revenger-shokunin/PROVINCE.md:29`). None claims narrative structure, quest/scene design, or story specs. The three-layer story/quest/scene format (S725) is quest-adjacent; no game lane holds quest-design method. **No overlap found; latent only** if a quest/scene schema is later written as game-mechanics spec (then game-dev-2d/3d).
- **kotoba (prompt/skill craft).** No narrative content in its PROVINCE or knowledge. Overlap only if the story spec format were framed as an LLM prompt/skill structure; the staged entry frames it as a world-bible storage format. **No overlap.**

## 6. Proposed boundary (for the integrator; not ruled here)

Split the surface by what is designed versus what is checked or canonized:

| Item | kotodama (design, generative craft) | lore (verification, canon) |
|---|---|---|
| Story/discourse split | Describe as a design option and the terms for it (fabula/syuzhet vocabulary, attributed to scholars) | Decide how discourse order enters the bible and whether any reader-facing order is canon |
| Reveal / discourse order | Generative alternatives (order variants, proposed narrative-order map per cluster) as coupling edges, with alternatives | Checks (CM-f): non-tick reveal-order field, warn vs fail, licensed vs unlicensed anachrony |
| Actantial model / Propp / Greimas | Role-generator for myth and tale families (already in `comparative-frameworks.md §5`); de-dupe, do not re-teach | Which in-world role-holders exist as entities |
| Focalisation / character knowledge over time | Design axis: who may know what (narrator's and character's epistemic positions) as proposal | Character knowledge state gate; canon knowledge state; contradictions ledger |
| Time axes (story vs discourse time) | Narratology as design vocabulary; calendars/eras stay with kotodama (`calendar-festival-systems.md`, `era-periodization-models.md`) | Story time vs discourse time as chronology checks; in-world dating (CM-c) |
| Three-layer spec (story/quest/scene) | Proposal of a storage shape and its derivation rules | Whether the bible stores it; schema and consistency gates |
| Narrative-generation models (non-LLM) | Design-side structural models | None (no canon claim) |
| LLM story-generation evaluation (StoRM, ConStory, FlawedFictions) | Not in scope | Lore for consistency taxonomy and canon authority; kengaku for judge/eval claims |

Required guard for claim C's entries: an explicit line that the entry supplies **no reveal-order schema, no knowledge-state gate, and no canon ruling**, pointing to lore-shokunin (CM-f, CM-g) and the contract `worldbible-integration-contract.md` §3 row "Contradiction" / §6. The contract's §3 table has no narrative-order row, so this is an unresolved scope gap rather than an explicit assignment; the integrator should decide whether to add one.

## 7. Recommendations

1. Keep claim C in-lane: `myth-symbol/narrative-structure-frameworks*.md` is kotodama's category, and lore's own frontier names the surface as uncovered, not as lore's content. Narrative structure is a design method here.
2. Fix claim C's BEFORE text: replace "neither names a structuralist narrative source" with the `comparative-frameworks.md:15,78` and `costume-semiotics.md:12,20` facts. Dedupe against `comparative-frameworks.md §5`.
3. Add a scope line to the entry (no schema, no gate, no canon) with a pointer to `lore-shokunin/corpus/README.md` CM-f and `PROVINCE.md:19,23`.
4. Raise to the integrator (contested, not absorbed): whether discourse order and focalisation belong to kotodama's design method or lore's frontier. Name lore-shokunin and the boundary above. Do not resolve by silence (contract §10).
5. Raise to the integrator: the cross-wave duplicate staging of S723–S725 = S864–S866, the Barthes four-ID row, and S729 = S761 = S787 = S870 (one essay). The freeze should key rows by document, not by appearance.
6. Route any LLM story-generation evaluation claim to kengaku-shokunin if it enters a later round.

## Evidence scope and limits

- Read: every lane `PROVINCE.md` (lore, kengaku, chousa, kotoba, game-dev-2d/3d, audio, revenger, kotodama in full); lore `corpus/README.md` coverage/frontier rows and `corpus/SOURCES.md` S010–S012; lore `.ufo/waves/kaika-w1/lore-art.md`; `kotodama-shokunin/corpus/knowledge/synthesis/worldbible-integration-contract.md` §§1–13; `claims.json` claim C and Ca axes; base `comparative-frameworks.md` (via `git show f556d104…`); shokuknow scopes `ScoutKotodama.md` and `ScoutLore.md` and `lanes/kotodama/SOURCES-PROPOSED.md` IDs (read-only, grep excerpts).
- Not done: no web fetches; no source content opened (the Persée, J-STAGE and ucass documents were not read by this seat); the shokuknow narrative entry was read through grep excerpts, not in full. Statements about the entry's contents are from excerpts, marked as such.
- No verification run (connector seat; checks belong to the main agent per the assignment).
- Install record: none. Scratch `/fast/scratch/hyaku/kotodama-r75/ConnectorSiblings/` created and removed. No writes to fleet root, siblings, shokuknow, or the lane's claims/ledger/counters.
