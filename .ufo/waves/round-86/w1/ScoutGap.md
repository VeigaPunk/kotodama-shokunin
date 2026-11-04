# ScoutGap — round 86 / w1

Axes: **depth + operability**. Read-only source reconnaissance, not admission or validator adjudication. Freshness pause unchanged; no planner-role exception claimed.

## Observed base and authority

- Declared base: `1e6b10a02b93a981b012987c51399d278fe37fa9`; freeze: `16c267832746e1cb98fb42a56180f8d1d12dc18b`.
- Observed HEAD during reconnaissance: `079fbf5969e4ac152a360f45cd8ed76a0191e14a`, the predispatch-control commit after freeze, NOT the base. Read-only log showed HEAD → freeze → base. `git -C ... diff --name-only BASE HEAD -- corpus` produced no paths. Earlier status showed no corpus modifications; other owners' dirty files were left alone.
- `corpus/knowledge/linguistics/orality-formulaic-language.md` has identical base, HEAD and worktree SHA-256: `f827bbee6f305466a17a8b6e911539c38820e6865eb7755881e779ad143a6a95`.
- Read claims directly from `git -C LANE show FREEZE:reports/round-86/claims.json`, and read `reports/round-86/measure86.py`, including `evaluate`, `selftest`, and CLI. No counter or tests executed. Its selftest creates/commits Git fixtures and therefore was not permissible for this seat.
- Base `git cat-file -e BASE:corpus/knowledge/linguistics/proverbs-riddles-attestation-solutions.md` returned 128, explicitly naming the absent path. Base registry's last numeric rows were S921/S922/S923. Filename sweep over base `corpus/` for proverb/riddle/paremi/saying produced no matching paths.

## Inherited knowledge — genres are NOT absent

Nearest and primary owner: `corpus/knowledge/linguistics/orality-formulaic-language.md`.

| Locator | Already inherited |
|---|---|
| Title/topic, lines 1–3; bibliography line 19 | Both genres named explicitly; Taylor 1931/1951, Permyakov 1979 and Uther 2004 already cited. |
| §5, lines 75–80 | Kenning/riddle compression, proverb parallelism, conventional kenning versus occasional competitive riddle. |
| §6, lines 82–89 | Paremiology and situation classes; Yoruba meta-proverb; reproach/counsel; legal, agricultural and historical uses; wisdom-literature relationship; design budget of 100–300 proverbs and situation/ethos/allusion tags. These are inherited assertions, not independently revalidated facts in this seat. |
| §7, lines 91–97 | Riddle definition, Exeter Book approximately 90 riddles, writing/bookmoth examples; Vedic/Norse/African performance frames; taxonomy, trial and sovereignty; proverb/kenning/riddle distinction. |
| §8 and §11 | Register-design checklist, riddle breaks and proverb inventory examples; reference/method only, with canon owned by lore-shokunin. |

**Important prior-source overlap:** `corpus/lessons/supplement-opencode-1/sources/orality.json:34–43`, ORALITY-03, already records retrieval of the EXACT proposed S926 Tupper URL. It records edition-dependent counts 89/95; Tupper Bookmoth No.48 versus modern No.47; and no modern critical edition/manuscript facsimile opened. Located inherited quote: “by drawing four riddles into two, gives us eighty-nine in all” (13 words). This is a quotation from an opened local historical receipt, NOT a fresh external-source reopening. The new dossier cannot claim first discovery/opening of Tupper or first awareness of numbering uncertainty.

## Complete bounded filename/topic-owner inventory

Literal case-insensitive `proverb|riddle` sweep over `corpus/`, paged at file offsets 0/20/40, returned **43 matching files**: 35 knowledge files, README, SOURCES, and six lesson/evidence files. This is a literal inventory, not semantic proof. `xd://lsp` returned “No such tool”; no language-server navigation was available.

All knowledge paths below are relative to `corpus/knowledge/`:

- **Primary genre owner:** `linguistics/orality-formulaic-language.md`.
- **Civilization-specific substantive/contextual owners:** `civilizations/akan.md` (adinkra/kente/proverb networks), `aksum-ethiopia.md` (qene boundary), `fon-dahomey.md` (asen and royal emblems), `germanic-norse.md` (poetic diction), `malagasy-madagascar.md` (kabary), `mali-songhai.md` (bogolan), `persia-sasanian.md` (andarz), `swahili-coast.md` (kanga/taarab), `yoruba.md` (àlọ́ àpamọ̀ riddles versus folktales).
- **Material context/boundary:** `culture-material/dress-through-eras.md`, `games-play-sport-contests.md`, `transport-mobility-lexicon.md`. `games-play-sport-contests.md:117` explicitly assigns riddle-debate/oral-formula/wager traditions to orality. `culture-material/cuisine-food-lexicon.md` is a bibliographic title hit, not a riddle-genre owner.
- **Linguistic coupling/context:** `linguistics/kinship-terminology.md`, `linguistic-anthropology.md`, `politeness-taboo-euphemism.md`, `register-strata-attestation.md`, `sociolinguistics-registers.md`, `syntax-typology.md`.
- **Myth/symbol coupling, exemplars or genre/index context:** `myth-symbol/animal-symbolism.md`, `binding-speech-complex.md`, `color-symbolism.md`, `comparative-frameworks.md`, `creation-myths-taxonomy.md`, `divination-omen-systems.md`, `guest-right-hospitality-law.md`, `marriage-alliance-bridewealth.md`, `motif-index-usage.md`, `myth-folktale-genres.md`, `myth-ritual-theories.md`, `pantheon-archetypes.md`, `plant-symbolism.md`, `symbolism-synthesis-method.md`, `trickster.md`. Some are incidental title/proverb/reference hits; a keyword hit does not confer whole-topic ownership.
- **Remaining evidence/index hits:** `corpus/README.md`, `corpus/SOURCES.md`, `corpus/lessons/round-1-triage/{Z01,Z15,Z23}.md`, `corpus/lessons/round-65.md`, `corpus/lessons/round-2-triage/V01.md`, `corpus/lessons/supplement-opencode-1/sources/orality.json`.

## What D can newly deepen

**Observed frozen scope:** dedicated `proverbs-riddles-attestation-solutions.md`; S924–S926; ≥6000 UTF-8 bytes; ≥6 H2 sections; six decisions; ≥12 single-ID anchors; mined/opened rows; cited-line shape check. Frozen counter `evaluate:67–85` checks these structural/registry legs, not historical truth or exact semantic support.

**Inference / actionable novelty boundary:** the gain is an edition-located attestation and solution dossier: distinguish first located witness from origin, editor selection from oral repertoire, and proposed/uncertain solution from uniquely determined answer. Tie each case to its particular edition and numbering. Repeating genre definitions, Exeter approximately-90, Bookmoth, or general performance frames is inherited recap, not the depth delta.

`reports/round-86/source-map.json` assigns S924 to the 1911 Britannica Proverb article, S925 to the historical English proverb dictionary transcription, and S926 to Tupper's Exeter transcription. These URLs were read from the local map only; this seat did not independently reopen them. Consequently no new mined/opened-source row or admission is claimed. Require the assigned source seat's actual opened-source receipt, located ≤25-word quote and access date for new rows.

O remains the **new containing-article paragraph ordinal verdict**, not first acquisition of a quote-span locator. This seat did not exercise its implementation.

## Assimilation: none recommended

Opened `/home/vgpnk/Projects/shokuknow/merge/kotodama/MERGE-REPORT.md` read-only. It proposes 132 rows and 56 entries, starting S859, and describes an old 782-row registry. Its listed themes are naming/conlang scholarship, calendars/periodization, narrative theory, heritage and citation/catalogue verification—not this attestation/solution dossier or article-paragraph locator.

Bounded package search `proverb|riddle|paragraph.locat|orality` found incidental narrative-structure prose/registry hits, no direct genre/locator package. **Recommend Assimilation:none**: no demonstrated direct fit; bulk adoption would introduce unrelated material and overlapping ID space into S924–S926 reservations. This is not a verdict that all package research is invalid; no external rows were reopened or admitted here. The initially attempted lane-local shokuknow path was absent; the correct external repository was then located and opened.

## considerthese absence — bounded, not a token-absence claim

- Filename globs `LANE/**/considerthese*` and `LANE/considerthese*`, hidden included and ignore rules disabled: no matches.
- Additional direct globs `LANE/corpus/considerthese*` and `/home/vgpnk/Projects/shokuknow/considerthese*`: no matches.
- Content sweep across this lane for `considerthese|consider_these|consider-these` found historical mentions (90 matching files reported), including prior absence receipts and references to OTHER lanes. Therefore the directory/package is absent within the searched bounds; the word is emphatically NOT absent from recorded prose. No inference about the rest of the host.

## Limits and handoff

High confidence: inherited genre coverage, base path absence, prior exact Tupper URL use, bounded directory absence, and no directly fitting merge-report target. Historical/source accuracy beyond the opened local records remains unadjudicated. Current D/O completion is outside this scout question; no green test, build, lint, freshness gain, external admission or planner-role exception claimed.

No production edits, Git/jj/index mutations, installations, delegated jobs or background processes. No scratch directory was created, so none remains to remove. Only the expressly requested report and this seat's stage receipt were written.
