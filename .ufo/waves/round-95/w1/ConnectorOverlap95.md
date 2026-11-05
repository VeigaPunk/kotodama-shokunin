# ConnectorOverlap95 — Report (Round 95, w1, Milestone r95-v1)

- Seat: `ConnectorOverlap95` (connector role, leaf member)
- Base revision: `19aa4dd03dfd37b435d0b8ea5b313635d9d51592`
- Freeze revision: `d41eb594d27fa71869c0c28d9c2dc051fda40079`
- Target entry: `corpus/knowledge/linguistics/funerary-lament-dirge-formulae.md` (Claim C)
- Detail file: `.ufo/waves/round-95/w1/stage/ConnectorOverlap95/overlap.md` (sha256 `f41f215f8ece409fbc58bd8b1896017123bd627657728160bec4435ab1c6a5a0`)

---

## 1. Province Check

Read `/home/vgpnk/Projects/shokunin/kotodama-shokunin/PROVINCE.md`:
- **Domain:** Linguistic-cultural worldbuilding (言霊, *kotodama* — coupling of word and world-spirit): conlang design, mythic/symbolic systems, era/period models, material-culture terminology, naming systems, and formulaic verbal art for fictional worlds feeding the world bible.
- **Owned partitions:** `corpus/knowledge/{linguistics,myth-symbol,culture-material,synthesis,verification,civilizations}`.
- **Refused:** Claiming or recording canon (owned by `lore-shokunin`); real-world rights/attribution rulings; game mechanics (`game-dev-2d/3d`); general source-research method (`chousa`); web publishing (`kake`); prompt/skill craft (`kotoba`).
- **Adjacent contract (load-bearing):** `lore-shokunin` owns the world bible and its consistency verification. The handoff format is governed by `corpus/knowledge/synthesis/worldbible-integration-contract.md`. Contested scope is reported to the integrator, never absorbed.
- **Claim surface evaluation:**
  - **Claim C (coverage):** Adds `corpus/knowledge/linguistics/funerary-lament-dirge-formulae.md` to the `linguistics` partition. The subject ("funerary laments and dirges: the sung speech of mourning — professional keeners and lament genres, antiphonal and refrain structures, formulaic grief content, gendered mourning rules, the lament between speech and song, and the design procedure for a fictional mourning register") resides strictly within linguistic-cultural worldbuilding. It remains strictly NON-CANON, providing generative design procedures and registers rather than in-world canon facts.
  - **Claim O (operability):** Touches only `tools/check-advance-evidence.py` (lane-local grader tool, v5 -> v6) and wave stage files.
  - **Sibling surface isolation:** Confirmed. The claim set touches zero sibling lane repositories (`audio`, `chousa`, `game-dev-2d`, `game-dev-3d`, `kake`, `kama`, `kengaku`, `kotoba`, `kumitate`, `lore`, `mado`, `mori`, `revenger`, `shokuknow`, `souji`, `tabi`, `tsukuroi`). Sibling repositories remain completely read-only.

---

## 2. Census & Sweep Evidence

Commands run from `/home/vgpnk/Projects/shokunin` (all rc 0):
1. `grep -rniE --include="*.md" "\b(funerary-lament|dirge|keener|keening)\b" /home/vgpnk/Projects/shokunin/*-shokunin/corpus | grep -v "kotodama-shokunin" | wc -l` -> **0 lines**. No sibling lane owns any part of funerary laments or dirges.
2. `find /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/knowledge -iname "*lament*" -o -iname "*dirge*" -o -iname "*keener*"` -> **0 files**. Independent corroboration of `claims.json` C.surface ("0 filename owners at base").
3. `grep -rniE --include="*.md" "\b(funerary-lament|dirge(s)?|keener(s)?|keening)\b" /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/knowledge | wc -l` -> **5 lines** in 2 files (`calendar-festival-systems.md:92`, `funerary-material-culture.md:4, 37, 39, 139`).
4. `grep -rniE --include="*.md" "\blament\b" /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/knowledge | wc -l` -> **7 lines** in 7 files (`india-tamil-sangam.md:55`, `israel-ancient-hebrew.md:93`, `funerary-material-culture.md:37`, `music-instrument-lexicon.md:111`, `orality-formulaic-language.md:66`, `myth-ritual-theories.md:34`, `ritual-liminality.md:14`).
5. `grep -rniE --include="*.md" "\b(praefica|praeficae)\b" /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/knowledge | wc -l` -> **3 lines** in 1 file (`funerary-material-culture.md:19, 36, 129`).
6. `grep -rniE "\b(lament|dirge|keener|keening)\b" /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md` -> **0 lines** (rc 1). Base registry has zero sources on this topic; rows S970+ are completely unowned and unclaimed.

---

## 3. Sibling Overlap & Boundary Rules

### Primary Sibling 1: `culture-material/funerary-material-culture.md`
- **Owner holds:** The death assemblage as four coupled machines: DISPOSAL (cremation, inhumation, exposure, secondary burial), ASSEMBLAGE (grave goods, deposition grammar, Parker Pearson's grave-résumé critique), MONUMENT (tombs, stelae, necropolises), and WORD (avoidance terms, rite terms, office terms, monument terms); mortuary trade offices (*libitinarius*, *pollinctor*, *vespillo*, *praefica*, *chevra kadisha*, *rogyapa*) and funeral sumptuary laws.
- **Boundary rule:** `lament = sung speech register / performance rules vs funerary-material = objects + physical rites`.
- **Must NOT restate:** Physical disposal technologies (cremation, mummification, exposure); grave-goods deposition grammar; physical mortuary trade offices and commercial guild fees (undertakers, corpse washers); monument architecture and container etymologies (*sarcophagus*, *coffin*, *mausoleum*, *cenotaph*, *epitaph*).
- **Keener boundary:** *Praeficae* / keeners are treated strictly as *verbal and vocal specialists* performing the sung speech of mourning (antiphony, formulaic improvisation, lament refrains, weeping-speech continuum), NOT as corpse handlers or commercial undertakers.

### Primary Sibling 2: `myth-symbol/death-afterlife-eschatology.md`
- **Owner holds:** The doctrine of the dead person — four questions: Q1 (what survives: shadow, dual-soul split, rebirth, resurrection, ancestor office, dissolution), Q2 (destination geography as institutions: gates, ferrymen, clerks, courts, halls), Q3 (judgment machines: weighing, ledgers, interrogation, ordeal-journey, kin-recall), Q4 (what the living owe: counter-flow ledger, offerings, unquiet ghosts); cosmic eschatology.
- **Boundary rule:** `lament = sung speech register / performance rules vs eschatology = belief / doctrine of the dead person and the afterlife`.
- **Must NOT restate:** Soul-splitting metaphysics (*ka*/*ba*, *hun*/*po*); underworld destination geography (Styx, Chinvat, Naihe, Mictlan); bureaucratic judgment courts (weighing against Maat, Ten Kings' ledgers); ghost pacification rituals or long-term posthumous feeding calendars (Obon, Ghost Festival, *kispu*); cosmic end-of-the-world event grammar.

### Primary Sibling 3: `linguistics/lullaby-child-song-formulae.md`
- **Owner holds:** Verbal text of child-directed songs — sleep-inducing formulae, nonsense-syllable refrains, infant address, archaic retention in song text, register shift between song and ordinary speech, and fictional lullaby register design.
- **Boundary rule:** `lullaby vs lament = opposite speech acts on the same vocal channel`.
  - *Lullaby:* Soothing/sleep-inducing speech act; life-threshold (newborn/infant); asymmetric address to non-speaking child; descending/soothing melodic contour; domestic/intimate setting; protective archaism.
  - *Lament:* Mourning/grief speech act; death-threshold (deceased relative/hero); address to non-responsive dead (or death personified) with praise/blame/consolation; tear/sob/cry continuum; public/communal performance; antiphonal structure with professional keeners and gendered rules.
- **Must NOT restate:** Must NOT treat lament refrains as sleep modulators or nursery echo-refrains; must NOT treat lament address as intimate nursery talk or generic caregiving vocatives; must NOT replicate the lullaby's four-face register shift table without grounding it in the *crying/weeping-speech-song continuum*; must NOT copy the 12-row lullaby decision table (supply a dedicated fictional mourning register procedure).

### Other Adjacent Files
- `linguistics/orality-formulaic-language.md:66`: Owns oral-formulaic composition (Lord/Parry), incremental repetition, and epic type-scenes. Lament entry borrows formulaic composition concepts but owns the specific mourning genre and register design; epic narrative storytelling machinery remains in `orality-formulaic-language.md`.
- `culture-material/ritual-garments.md` & `costume-semiotics.md`: Own mourning dress, fabrics, color codes (*wǔfú*, crape, sackcloth, *deuil blanc*). Lament entry leaves mourning dress to garment files; owns only sung and spoken mourning registers.
- `culture-material/music-instrument-lexicon.md:111`: Owns musical instruments and accompaniment (aulos, mourning pipes). Lament entry leaves instrumental accompaniment and melodic theory to music files; owns verbal text, vocables, and the weeping-speech-song continuum.
- `linguistics/sacred-registers-liturgical-language.md:95`: Owns liturgical refrains and sacred high-variety registers. Folk and professional keening/lament is distinct from formalized liturgical prayers (Mass for the Dead, Requiem, Kaddish).

---

## 4. Boundary Table

| Adjacent File / Owner | Ground It Holds | Overlap with `funerary-lament-dirge-formulae.md` | Boundary Rule (What the New Entry Must NOT Restate) |
|---|---|---|---|
| `culture-material/funerary-material-culture.md:4,19,36,37,129` | Four mortuary machines: physical disposal tech, grave goods/assemblage, monuments, undertaker trade offices (*libitinarius*, *pollinctor*, *vespillo*, *praefica*), sumptuary laws | **Contested / Neighbor** — both treat mortuary settings and mention *praeficae* (hired mourners) | **Lament = sung speech register vs funerary-material = objects + physical rites.** Entry owns *praeficae* strictly as vocal/verbal specialists (sung genres, antiphony, formulaic grief). Must NOT restate physical corpse disposal, grave goods, monuments, or commercial undertaker trade. |
| `myth-symbol/death-afterlife-eschatology.md:4,24,37,51,67,81` | Doctrine of the dead person: survival types, destination geography, judgment machines, ghost pacification, cosmic eschatology | **Neighbor** — both touch the death transition and bereavement | **Lament = sung speech register vs eschatology = belief/doctrine.** Entry owns address to the dead, praise/blame, and mourning performance. Must NOT restate soul metaphysics (*ka*/*ba*, *hun*/*po*), underworld maps, judgment courts, ghost pacification rites, or world-end eschatology. |
| `linguistics/lullaby-child-song-formulae.md:3,16,28,52,141,237` | Child-directed song formulae: sleep-inducing speech acts, nonsense refrains, infant address, speech-song shift, lullaby register design | **Structural Sibling** — opposite ends of human lifecycle on the same vocal channel | **Lullaby vs lament = opposite speech acts on the same vocal channel.** Lullaby soothes infant to sleep; lament mourns dead at threshold. Entry must NOT treat lament refrains as sleep modulators, must NOT replicate nursery address, and must NOT copy lullaby's 12-row table. |
| `linguistics/orality-formulaic-language.md:66` | Oral-formulaic composition (Lord/Parry), incremental repetition, epic type-scenes (lament as one epic card) | **Structural Predecessor** — currently holds the only corpus mention of lament genre | **Oral-formulaic epic art vs lyric mourning register.** Entry borrows formulaic composition concepts but owns the specific mourning speech act, keening genres, and fictional mourning register design. |
| `culture-material/ritual-garments.md` & `costume-semiotics.md:40` | Mourning dress, *wǔfú* grades, crape, sackcloth, *deuil blanc*, sumptuary dress enforcement | **Neighbor** — visual vs verbal signs of mourning | **Dress vs voice.** Entry owns only verbal and sung expressions of mourning; leaves all fabric, cut, and dress rules to garment files. |
| `culture-material/music-instrument-lexicon.md:111` | Musical instruments, tuning, melodic accompaniment (e.g. aulos, mourning pipes) | **Neighbor** — instrumental vs vocal carrier | **Accompaniment vs verbal text.** Entry leaves instrumental construction and melodic theory to music files; owns verbal lyrics, vocables, and the weeping-speech-song continuum. |
| `linguistics/sacred-registers-liturgical-language.md:95` | Liturgical registers, sacred hymns, clerical recitation, ecclesiastical refrains | **Neighbor** — ritual speech registers | **Clerical liturgy vs communal/professional keening.** Entry owns folk and professional lament genres; leaves institutional sacred liturgy to sacred-registers. |
| `myth-symbol/ritual-liminality.md:14,24,32` | Rite-of-passage grammar (separation, liminality, incorporation), Hertz's double funeral, life-crisis transitions | **Neighbor** — anthropological rite framework | **Ritual grammar vs linguistic register.** Entry cross-cites liminal separation as the context for keening, but owns the verbal formulae, not the general rite grammar. |
| `synthesis/worldbible-integration-contract.md` | Protocol for handing off linguistic/cultural worldbuilding models to `lore-shokunin` | **Governance / Contract** | Entry remains strictly NON-CANON, providing generative procedures and options rather than canon facts. |

---

## 5. Contested-Scope List & Risks Found

1. **Keener / *Praeficae* Role Confusion (Owner: `culture-material/funerary-material-culture.md`):** `funerary-material-culture.md:19, 36, 129` lists *praefica* among the Roman mortuary trade. Scope is strictly partitioned: `funerary-material-culture.md` retains commercial undertaker trade and sumptuary laws; `funerary-lament-dirge-formulae.md` owns keeners exclusively as *verbal/vocal specialists* performing the sung speech of mourning. Nothing is absorbed.
2. **Underworld Travel & Judgment Overlap (Owner: `myth-symbol/death-afterlife-eschatology.md`):** Mourning laments addressing the journey of the dead must NOT detail underworld topography or post-mortem trials. `death-afterlife-eschatology.md` retains destination geography and judgment machines; the lament entry restricts journey references to the mourner's verbal parting formula. Nothing is absorbed.
3. **Refrain & Register-Shift Structural Drift (Owner: `linguistics/lullaby-child-song-formulae.md`):** Lament refrains are grief markers and antiphonal cues (not sleep modulators); lament address is eulogy, reproach, or apostrophe (not nursery diminutives); the shift is across the crying-speech-song continuum (not domestic soothing); and the decision table specifies fictional mourning registers. Nothing is absorbed.
4. **Collapsing Lament into Epic Narrative Type-Scenes (Owner: `linguistics/orality-formulaic-language.md`):** The new entry establishes the dedicated home for funerary laments and dirges. `orality-formulaic-language.md` retains only epic narrative type-scenes (Homer, Beowulf). Nothing is absorbed.

---

## 6. Open L0 Carryovers (Report Lines, No Answers)

1. **Kotodama round-92 ideophones overlap:**
   `/home/vgpnk/Projects/shokunin/.ufo/l0-questions.md` line 356:
   `kotodama | round-92 | Contested scope: corpus/knowledge/linguistics/ideophones-mimetics.md (landed 1473606b, claim C) re-states part of corpus/knowledge/linguistics/sound-symbolism.md §6 (lines 99–111: ideophone word-class definition, grammar profile, reduplication, giongo/gitaigo, a five-step ideophone register procedure). Decision needed: (a) keep both, with §6 trimmed to a pointer to the new entry in a later round; (b) keep §6 and make the new entry cover only the cross-linguistic and acquisition ground; or (c) retire the new entry's overlapping sections. The round counted the new entry as expansion on the dedicated-entry surface (0 filename owners at base) and qualified the verdict. Routed around; nothing edited in sound-symbolism.md.`
   - Status: Open. Carries NO L0 ANSWER.
2. **Freshness pause:**
   `/home/vgpnk/Projects/shokunin/.ufo/l0-questions.md` lines 47 and 303:
   - Line 47: `kotodama | round-11 | drift-recheck threshold calibration: the declared >=95%% 24h hash-stability threshold failed at 0.778 purely because build rounds 10/11 legitimately changed the tree (all 45 drifts dispositioned). Should the freshness recheck threshold be recalibrated (e.g. stability measured against a pinned baseline commit, or legitimate-change drift excluded), or should inter-build drift budget into the claim? Freshness axis-move claims are paused until ruled.`
   - Line 303: `kotodama | round-89 | Does live source re-verification (re-opening SOURCES rows at their URLs, committed captures, recheck cell advanced old→new) fall inside the round-11 pause "Freshness axis-move claims are paused until ruled"? Round 89 claim F did exactly this (16/16 rows, independent re-fetch agreement 16/16; kotodama-shokunin/reports/round-89/final/lands-F.txt) without using the round-11 drift-hash threshold. Please rule whether F is admissible as a freshness move, or whether freshness stays paused until the round-11 threshold question is answered.`
   - Status: Both lines open. Carry NO L0 ANSWER. Standing operator pause holds; the lowest-axis obligation is neither met nor waived this round.

---

## 7. Round-94 Closure Routed Items Relevant to Adjacency

Inspection of `corpus/lessons/round-94-verifier-spotcheck.md` §6 and closure ruling:
- **R95-1 (operability):** Grader v5 selftest does not pin the >=2-token heading rule (`head-qualify-off` mutant survives). Routed to Claim O.
- **R95-2 (operability):** `mutants94.py` `dispo-fallback` pattern is stale against v5 bytes. Routed to Claim O.
- **R95-3 (operability):** CriticO94's seven surviving counterfeit classes. Routed to Claim O.
- **R95-4 (bookkeeping, operator-visible):** The SCORECARD capabilities row "grader v5 counterfeit refusals" landed marked "author-side pending closure". Closure rejected round 94 and did not admit it; row must be re-demonstrated inside an admitted round or marked unadmitted by the lane L1.
- **Adjacency confirmation:** R95-4 is strictly an in-lane SCORECARD bookkeeping duty for the L1. Confirmed: nothing else in the round-94 closure ruling or verifier spot-check requires any cross-domain act, sibling file modification, or cross-lane interaction.

---

## 8. UFO-FSD Connector Move (Bounded Proposal)

### Evidence
1. `funerary-material-culture.md:39` currently routes dirges to `linguistics/orality-formulaic-language.md` ("the eulogy and the dirge are formulaic genres, and the formula survives the language").
2. `lullaby-child-song-formulae.md:16` currently routes mourning songs to `linguistics/orality-formulaic-language.md` ("no mourning song (linguistics/orality-formulaic-language.md)").
3. `ritual-liminality.md:14` routes lament as an epic type-scene to `orality-formulaic-language.md`.
4. In `orality-formulaic-language.md:66`, "lament" is only an epic narrative type-scene card, leaving the sung speech of mourning, keeners, and fictional mourning register design unowned.
5. The landing of `corpus/knowledge/linguistics/funerary-lament-dirge-formulae.md` (Claim C) fills this exact dedicated surface.

### Affected Axes
- `adjacency`: Improves corpus boundary precision by defining clean bidirectional coupling between the new lament entry and its material, eschatological, and oral-formulaic neighbors, eliminating transitional routing debt.
- `coverage`: Protects Claim C by ensuring the new entry satisfies all structural floor requirements without scope creep.
- `operability`: Zero harm; no tool, test, or mutant driver is touched.
- `calibration`: Zero harm; strictly respects non-canon boundaries and lane province.

### Proposed Move
A two-stage bounded synthesis:
1. **In-Wave Author Step (for ScribeEntry95):** The new entry `corpus/knowledge/linguistics/funerary-lament-dirge-formulae.md` explicitly adopts the proposed `- couples:` header and §1 boundary text below, formally anchoring its boundaries against `funerary-material-culture.md`, `death-afterlife-eschatology.md`, `lullaby-child-song-formulae.md`, and `orality-formulaic-language.md`.
2. **Post-Landing Maintenance Step (for L1 in a future round):** In a later maintenance pass (post-Round 95), the L1 can update the couples lines in `funerary-material-culture.md:39` and `lullaby-child-song-formulae.md:16` to point directly to `funerary-lament-dirge-formulae.md`, resolving the historical stopgap routing to `orality-formulaic-language.md`.

#### Proposed Header `- couples:` for `funerary-lament-dirge-formulae.md`:
```markdown
- couples: `culture-material/funerary-material-culture.md` (the death assemblage, disposal technologies, grave goods, monuments, and undertaker offices; this entry takes only the sung speech register and performance rules of mourning), `myth-symbol/death-afterlife-eschatology.md` (the doctrine of the dead person, survival types, destination geography, judgment machines, and ghost management; this entry takes only the verbal address to the dead, praise/blame/consolation, and mourning register), `linguistics/lullaby-child-song-formulae.md` (sleep-inducing child-directed song formulae; opposite life-boundary speech act on the same vocal channel, cited as structural contrast), `linguistics/orality-formulaic-language.md` (oral-formulaic composition, incremental repetition, and epic lament type-scene; borrowed, not restated), `culture-material/ritual-garments.md` (mourning dress and color codes; this entry takes vocal register only), `culture-material/music-instrument-lexicon.md` (mourning accompaniment instruments; this entry takes verbal text and vocal continuum only), `linguistics/sacred-registers-liturgical-language.md` (liturgical chanting and ecclesiastical refrains, distinct from folk/professional keening), `synthesis/worldbible-integration-contract.md` (non-canon handoff protocol)
```

#### Proposed §1 Boundary Paragraph for `funerary-lament-dirge-formulae.md`:
```markdown
This entry owns the sung speech of mourning — professional keeners and lament genres, antiphonal and refrain structures, formulaic grief content (praise of the dead, address to the dead, blame and consolation), gendered mourning rules, the lament between speech and song, and the design procedure for a fictional mourning register — and it owns no physical corpse disposal technologies, grave goods, or mortuary trade offices (`culture-material/funerary-material-culture.md`), no destination geography, judgment bureaucracy, or survival metaphysics (`myth-symbol/death-afterlife-eschatology.md`), no sleep-inducing child-directed song formulae (`linguistics/lullaby-child-song-formulae.md`), no epic narrative type-scenes beyond borrowed oral-formulaic vocabulary (`linguistics/orality-formulaic-language.md`), no mourning dress or sumptuary garment law (`culture-material/ritual-garments.md`, `culture-material/costume-semiotics.md`), no musical instruments or melodic theory (`culture-material/music-instrument-lexicon.md`), and no clerical liturgy (`linguistics/sacred-registers-liturgical-language.md`).
```

### Risks & Mitigations
- *Risk 1 (Causal separability):* Direct edits to existing corpus files during wave 1 would violate Claim C's touch list in `claims.json` and breach seat bounds.
  *Mitigation:* Confine all wave-1 output to stage; candidate repoints are filed for the L1's future maintenance ledger.
- *Risk 2 (Scope creep):* Author might be tempted to include keener pay scales, burial customs, or ghost beliefs in the lament entry.
  *Mitigation:* The boundary rule explicitly restricts keeners to *vocal/verbal specialists*, rejecting commercial undertaker and corpse-handling roles.

### Verification
- Check that every path in the proposed `- couples:` header resolves to an existing file on disk (`ls -l` passes).
- Check that `tools/check-corpus-index.py` exits 0 with 0 findings.
- Check that `python3 -B reports/round-95/predispatch.py` retains full causal separability between Claim O and Claim C.

---

## 9. Housekeeping & State

- Stage files written:
  - `stage/ConnectorOverlap95/overlap.md` (27872 bytes, sha256 `f41f215f8ece409fbc58bd8b1896017123bd627657728160bec4435ab1c6a5a0`)
  - `stage/ConnectorOverlap95/DONE` (65 bytes, containing the exact sha256 of `overlap.md`)
- Trailer file written:
  - `.ufo/waves/round-95/w1/ConnectorOverlap95.md`
- Tooling installed: None. pacman: Not invoked (host-wide pause respected). Host sysctls: Untouched.
- Scratch: `/fast/scratch/hyaku/kotodama-r95/ConnectorOverlap95/` cleaned up and deleted.
- Blockers: None.
