# Sibling-overlap scan — lullaby and child-directed song formulae (round-94, claim C)

Seat: ConnectorLullaby94 (read-only scan). Base: e7fa8eafb7c5d9edd706f860cfc023e6c99b1ab2. Date: 2026-11-05.

## Method and counts (every count with its scan)

Paths below are relative to the lane repo root `/home/vgpnk/Projects/shokunin/kotodama-shokunin/`. Scans run with the grep tool (Rust regex, PCRE2), case-insensitive unless marked cs.

1. `grep -i "lullab|cradle"` over the 10 candidate owner files (linguistics/{orality-formulaic-language,language-socialization-and-acquisition,sociolinguistics-registers,register-strata-attestation,sacred-registers-liturgical-language,phonetics-phonology,sound-symbolism,naming-systems}.md, culture-material/dance-performance-movement-codes.md, myth-symbol/death-afterlife-eschatology.md) → **0 matches** (also 0 case-sensitive).
2. `grep -i "nonsense|nonword|pseudo-word|pseudoword"` over the same 10 → **0 matches**.
3. `grep -i "refrain|infant|age-grad|caretaker|motherese|baby talk"` over the same 10 → **13 matching lines**: language-socialization-and-acquisition.md ×6 (16,17,19,24,25,34), sociolinguistics-registers.md ×4 (3,110,112,114), sacred-registers-liturgical-language.md ×1 (95), naming-systems.md ×2 (7,105 — 105 is the verb "refrains from", false positive).
4. `grep -i "lullab|cradle song"` over all of `corpus/knowledge` → **1 match**: myth-symbol/motif-index-usage.md:108. No linguistics or culture-material file anywhere in the corpus contains "lullab*" or "cradle song".
5. `grep -i "song|sing|chant|lament|cradle"` over linguistics/orality-formulaic-language.md → 15+ lines, all adult/performance-oriented (epic song, lament type-scene, ballad technique, singer's speech); **no child-directed or sleep-directed material**.
6. `grep -i "lullab|cradle|nonsense syllable"` over `corpus/SOURCES.md` → **1 match**: line 721, S765, the metaphor "cradle of chess" (false positive). **No lullaby, cradle-song, or nonsense-syllable source rows exist in the registry**, consistent with claim C requiring fresh rows S965+.

## Overlap table

| owner file (corpus/knowledge-relative) | line(s) | what it already owns | overlap with new entry |
|---|---|---|---|
| linguistics/language-socialization-and-acquisition.md | 16,17,19,24,25,34 | caregiver/infant-directed speech: IDS variability (S718), infants' attention to IDS prosody (S719), "questions, imperatives, and singing were more frequent in infant-directed than adult-directed speech" (S729), infant canonical babble (S720), infant turn-taking (S721), "Register specification marks child-directed verbs as a distinct pattern" (S743) | **partial** — closest overlap in the lane. Owns the interactional/prosodic side of talking to children, including the fact that singing is frequent in IDS. Owns no lullaby text, no nonsense refrain, no archaic retention, no register-shift analysis, no design procedure. |
| linguistics/orality-formulaic-language.md | 3, 66, 68, 99, 113, 136 | oral-formulaic composition of extended adult verbal art; lament as type-scene; "Ballad technique: incremental repetition"; singer's-speech register; "applause-able formula returns"; post-literate fossilization and archaism (H/L split) | **partial** — owns the formula/repetition/archaism machinery for adult performance. Nothing child-directed. New entry borrows vocabulary (formula, refrain, archaism) but must not restate the Parry–Lord engine. |
| linguistics/sociolinguistics-registers.md | 3, 110, 112, 114 | register stratification; "## 7. Age-grading and slang"; "Era anchor: age-graded registers (formal elder speech at rites of passage)" | none (lite) — age-grading indexes the *speaker's* age, not addressee-directed caretaker song; only generic register vocabulary is borrowed. |
| linguistics/register-strata-attestation.md | 3 | attestation register and register law | none |
| linguistics/sacred-registers-liturgical-language.md | 95 | hymn participation via "memorized refrain (partial 2)" | none — word collision only; the liturgical refrain is a different device owned there. |
| linguistics/phonetics-phonology.md | — (0 hits) | IPA, phonotactics, prosody machinery | none — couple as the toolkit the nonsense syllables must fit. |
| linguistics/sound-symbolism.md | — (0 hits) | iconicity, bouba/kiki, engineered sound-meaning coupling | none on the six terms; adjacent to nonsense-syllable sound play — couple, do not absorb. |
| linguistics/naming-systems.md | 7, 105 | teknonymy source (Geertz & Geertz 1964); name slots, name taboo; "praised as what Yamato refrains from" is a verb, false positive | none — child-name inventory stays here; address forms *as sung* stay with the new entry. |
| culture-material/dance-performance-movement-codes.md | 20, 22 | "dance-song-voice coupling"; couples `culture-material/music-instrument-lexicon.md` (dance-music coupling) | none on the six terms; adjacency only: lullaby-as-music belongs here / music-instrument-lexicon, not the new entry. |
| myth-symbol/death-afterlife-eschatology.md | — (0 hits) | death doctrine, funerary rite grammar | none; mourning songs route to orality's lament + this file's rite ownership. |
| (outside candidate list) myth-symbol/motif-index-usage.md | 108 | motif families; "one motif fossilized in jokes or lullabies" | none — one passing clause; the only other in-corpus "lullab*" occurrence. No owner exists. |
| corpus/SOURCES.md | 721 | S765 "cradle of chess" (metaphor) | none — no lullaby source rows; S965+ rows are unclaimed. |

## Duplicate verdict

No candidate file comes close to full overlap; **the new entry duplicates nothing**. The only file with real shared ground is `linguistics/language-socialization-and-acquisition.md` (partial). Nothing in the existing files needs narrowing — none of them mentions lullaby at all; all narrowing happens on the new entry's side:

- Narrow away: any IDS-prosody or general caregiving-register section (S718/S719/S743 ground — cite, don't restate).
- Narrow away: melody, rhythm-as-music, rocking/accompaniment (music-instrument-lexicon + dance-performance ground).
- Narrow away: Parry–Lord composition machinery, epic/ballad/lament (orality ground).
- Keep: the song's verbal text — sleep-inducing formulae, nonsense-syllable refrains, archaic retention in lullaby text, address to the child, register shift between song and ordinary speech, and the design procedure for a fictional lullaby register.

## Proposed owner boundary sentence (for the new entry's scope section)

> This entry owns the verbal text of songs directed at a child — the sleep-inducing formulae, the nonsense-syllable refrains, the archaic retention preserved in lullaby text, the forms of address to the child, the register shift between the song and ordinary speech, and a design procedure for a fictional lullaby register — and it owns no melody or accompaniment (`culture-material/music-instrument-lexicon.md`, `culture-material/dance-performance-movement-codes.md`), no infant-directed prosody or caregiving interaction beyond the song text itself (`linguistics/language-socialization-and-acquisition.md`), no oral-epic or ballad composition machinery beyond borrowed vocabulary (`linguistics/orality-formulaic-language.md`), no liturgical refrain (`linguistics/sacred-registers-liturgical-language.md`), and no mourning song or funerary rite (`linguistics/orality-formulaic-language.md`, `myth-symbol/death-afterlife-eschatology.md`).

## Proposed `- couples:` line (paths relative to corpus/knowledge/, one clause per owner)

```
- couples: `linguistics/language-socialization-and-acquisition.md` (infant-directed speech, prosody, and caregiving interaction; this entry takes only the song text), `linguistics/orality-formulaic-language.md` (formulaic composition, incremental repetition, and archaism-fossilization machinery for adult verbal art; borrowed, not restated), `linguistics/sociolinguistics-registers.md` (register and age-grading machinery), `linguistics/phonetics-phonology.md` (phonotactics and prosody tools the nonsense syllables must fit), `linguistics/sound-symbolism.md` (meaningless-syllable sound play versus engineered iconicity), `linguistics/sacred-registers-liturgical-language.md` (refrain as liturgical participation mode, distinct from the lullaby refrain), `linguistics/naming-systems.md` (child-name inventory and teknonymy behind the address forms), `culture-material/music-instrument-lexicon.md` (melody, rhythm, accompaniment; this entry owns no music), `culture-material/dance-performance-movement-codes.md` (dance-song-voice coupling and performance framing), `myth-symbol/motif-index-usage.md` (lullabies noted as a motif-fossilization site)
```

## Adjacency duty — contested scopes and their owners

1. **Lullaby as music** (melody, rocking rhythm, accompaniment) → `culture-material/music-instrument-lexicon.md`, with `culture-material/dance-performance-movement-codes.md` for dance-song-voice coupling. Do not absorb.
2. **IDS prosody and caregiving interaction** (S718, S719; the S729 singing-frequency fact) → `linguistics/language-socialization-and-acquisition.md`. S729 is the hinge between the two entries: it stays there; the lullaby entry cites it as motivation only.
3. **Refrain as liturgical participation device** → `linguistics/sacred-registers-liturgical-language.md:95`. Hymn refrain stays there; the nonsense-syllable lullaby refrain is the new entry's.
4. **Archaic retention as a general sung-tradition phenomenon** (fossilization, H/L split, epic-diction archaism) → `linguistics/orality-formulaic-language.md` (§9 fossilization; couples historical-linguistics). The new entry presents only the lullaby-text case and couples back.
5. **Mourning songs / songs for dead children** → lament type-scene in `linguistics/orality-formulaic-language.md:66` + rite ownership in `myth-symbol/death-afterlife-eschatology.md`. The new entry covers songs for the living child at sleep.
6. **Child vocatives, endearments, name taboo inventory** → `linguistics/naming-systems.md`. Address forms as they occur inside song text stay with the new entry.
7. **Nonsense syllables as engineered sound-meaning play** → `linguistics/sound-symbolism.md`. The refrain-formula convention (semantically empty syllables, repeated) stays with the new entry.
8. **Motif fossilization in lullabies** → already named in passing at `myth-symbol/motif-index-usage.md:108`; no absorption needed, couples clause suffices.

## Limits

- Scan covered only the 10 candidate files plus corpus-wide term sweeps and SOURCES.md; it did not audit every entry in linguistics/ (topic lines of all 10 candidates read via `grep "^- topic:"`; the corpus-wide `lullab|cradle song` sweep returning a single passing clause is the duplicate guard).
- All quotes above are exact substrings of the grep output at the cited path:line in the working tree at base e7fa8ea.
- Tooling installed: none. pacman: not invoked. Sysctls: untouched. Scratch `/fast/scratch/hyaku/kotodama-r94/ConnectorLullaby94/` deleted before yield (was never used — no writes needed).
