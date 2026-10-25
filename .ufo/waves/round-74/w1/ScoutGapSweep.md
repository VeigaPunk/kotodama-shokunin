# ScoutGapSweep — claim C GROUND gap sweep (round 74 wave 1)

Base f7104cbce186bc2e1522abf0cfd619cc834628bb (lane HEAD == base at sweep time; git status showed only the inherited round-73 w2 files plus untracked `.ufo/waves/round-74/` and `reports/round-74/`). At-base figures were re-derived from the git tree (`git ls-tree`, `git grep`, `git show`), not only from the worktree. Read-only; no network; no installs.

Receipt text (ready to commit as `reports/round-74/telemetry/gap-sweep.txt`): `.ufo/waves/round-74/w1/gap-sweep-draft.txt` (written by this seat). Command + output are inside it, section by section.

## Verdict
**`worldbuilding-setting-practice` is uncovered ground at base**, and all three `before` clauses of claim C reproduce:

| Claim C `before` clause | Observed at base |
|---|---|
| (a) `find corpus/knowledge -iname '*worldbuilding*' -o -iname '*setting*'` | no output → 0 files (`git ls-tree` agrees; `architecture-settlement-lexicon.md` is "settlement", not "setting", and does not match) |
| (b) 804 rows, last id S880; litmemo.com / tuduku.space / chinawriter.com.cn | `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'` = **804**; last id **S880**; litmemo.com 0, tuduku.space 0, chinawriter.com.cn 0, 中国作家网 0 |
| (c) CJK terms in knowledge | `grep -rlE '設定ノート\|世界観\|世界观\|設定資料集' corpus/knowledge` → no output, exit 1 → **0 files** (`git grep` at base: 0). Wider net also 0: 設定\|设定; ライトノベル\|小説\|小说\|創作\|创作\|作家; 世界設定\|世界设定\|世界構築; settei\|sekaikan |

Extra: `設定|设定|小説|小说|創作|创作` over SOURCES.md = 0.

## Caution for the claim text (observed, not a defect in the three clauses)
- Claim `before (a)` says "README names worldbuilding only as a method label on other entries". Observed: that is true of README (lines 96, 106, 118 "conlang and worldbuilding method"; index lines 348-524), but the word is also a pervasive **use-label inside entries**: case-insensitive `worldbuilding|setting note|world-view|world view` hits **75 files / 121 lines** under corpus/knowledge (`worldbuilding` alone 72 files; loose `world-building|world building|worldbuild` 196 files / 321 lines). By partition: civilizations 27/95, culture-material 14/38, linguistics 18/32, myth-symbol 13/29, verification 3/24, synthesis 0/29. Any counter or entry text that asserts "0 worldbuilding hits" would be false; only the filename probe, the CJK terms and the three host fragments are 0. The claim's `ground` block (fragments + cjk_terms) is correctly scoped to the 0-valued items. Top counts: myth-ritual-theories 7, semantic-fields-lexicon-building 7, sign-languages-manual-modality 5, numerals-and-measures 4, celestial-symbolism-calendars 4, gesture-co-speech-pointing 4.
- `World View` hits are partly citation titles (Hallowell 1960 in animal-symbolism, calibration-registry, algonquian; Joralemon 1996 in olmec) — not method.
- Registry: `grep -inE 'worldbuilding|setting note|world-view|world view' corpus/SOURCES.md` = 2 lines: row **S322** (bl.uk bestiary, "Christian world view" — incidental) and line 881 (a prose paragraph about sign-language rows, **not a row**). Case-insensitive loose `world-building|world building|worldbuild` over data rows: 19 rows (S330 S413 S452 S568 S718–S724 S728 S733 S736 S739–S742 S760), all word hits inside annotation of conlang/lexicon sources; row bodies not read in full, so "none is a setting-practice source" is by title/host (no litmemo/tuduku/chinawriter host), moderate confidence.

## Sibling scan (read-only, all 20 sibling lanes; requested seven examined individually)
- lore (26 knowledge files), kotoba (60), chousa (72), kengaku (42), kumitate (59), tameshi (55), kake (52) — and the other 13 lanes: **0** knowledge files containing `world-?building`, **0** with 設定ノート/世界観/世界观/設定資料集, **0** SOURCES hits for litmemo/tuduku/chinawriter.
- PROVINCE.md: only `kotoba-shokunin/PROVINCE.md:61` mentions worldbuilding (an adjacency row describing kotodama as "worldbuilding and naming" and refusing prompt craft). lore's PROVINCE "Owns: fictional-world records — entities, relations, timeline events — with consistency verification and sourced inspiration" (the records, not authoring practice); kotodama's own PROVINCE.md:3-9 owns "linguistic-cultural worldbuilding" generative craft and hands systems to lore (`synthesis/worldbible-integration-contract.md`).
- **No sibling owns a worldbuilding-setting-method**, so there is no cross-lane ownership conflict to route.

## Nearest existing entries and what each does NOT do
| Entry | Owns | Does NOT do |
|---|---|---|
| `synthesis/coupling-model.md` (4395 w) | master method: interderive language/myth/symbol/era/costume, constraint propagation, handoff to lore; worked invented culture (Savari estuary) | no practitioner setting-recording practice (what an author writes down, in what order, for whom); no CJK 設定ノート/世界観 craft tradition; derives systems, not the author's notes |
| `myth-symbol/comparative-frameworks.md` (3540 w) | four etic mythology toolkits (monomyth, Eliade, Lévi-Strauss, Propp/Dundes) as generators with calibration | generators of *myths*, not of settings; no setting-note/world-view documentation craft, no practitioner literature |
| `synthesis/worldbible-integration-contract.md` | handoff envelope kotodama→lore, ownership table, retcon safety, claim kind vs canon status | contract between lanes, not authoring method; says nothing about how a creator builds/organizes/discloses a setting |
| `synthesis/cultural-translation-protocol.md` | presenting a constructed culture through action not exposition dumps; term staging; name-first reading; footnote discipline (Appiah/Genette/Venuti) | reader-facing delivery of terms only; not setting construction, scoping, note-keeping or "how much to write" practice; no CJK practitioner sources |
| `synthesis/worked-example-mini-culture.md` (5045 w) | one end-to-end invented culture (Retied Houses) as teaching fixture | a fixture, not a method for choosing/ordering setting content; no practice sources |
| `synthesis/consistency-verification-checklist.md` | cross-system preflight, findings to lore | audit of coupled systems, not setting-creation practice |
| `verification/real-world-inspiration-boundaries.md` | screens borrowing/extraction/sacred-material for worldbuilding references | boundary policy; not the craft of building a setting |
| `myth-symbol/hero-journey-variants.md`, `pantheon-archetypes.md` ("Worldbuilding-craft reference for divine-role systems") | narrative / divine-role archetypes | one sub-system each; no whole-setting practice |
| `linguistics/conlang-scholarship.md` (cites lane row S877, philol.msu.ru conlangs.pdf — the only entry citing S877) | conlang scholarship incl. the Russian monograph | the document is already in the registry as S877, which is why staged S882 is correctly not appended |

Coverage conclusion: the corpus covers *what to derive* (coupled systems), *how to hand off* (lore contract) and *how to present terms* (translation protocol); it has **no entry on the practitioner craft of the setting itself** — recording a 設定 / 世界观 (setting notes, scope, what to leave unwritten), from CJK practitioner sources. That is exactly the object of the two entries claim C proposes.

## Notes for the draft claim (no edits made)
1. Clauses (a)–(c) hold. Suggest the final `ground` prose not repeat "README names worldbuilding only as a method label" as if the corpus never uses the word — the 75-file figure above would contradict a naive reader's check.
2. `ground.cjk_terms` lacks 設定資料集 (my sweep included it; also 0) — optional hardening, not required.
3. Both proposed entry names (`worldbuilding-setting-practice.md`, `.amend-2026-10-23.md`) are free at base (0 name hits); partition `culture-material` has 38 files and no narrative/setting entry. (The claim's refused family "narrative-structure-frameworks" is a staged file; no such file exists in the lane at base — confirmed absent from `ls` of culture-material and myth-symbol.)

## Not exercised
No live fetch; no check of the staged package (not in my scope); the 19 loose-registry rows' bodies were not individually read.
