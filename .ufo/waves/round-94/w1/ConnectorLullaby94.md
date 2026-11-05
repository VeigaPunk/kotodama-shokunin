# ConnectorLullaby94 — Report (round-94, sibling-overlap scan, claim C)

Read-only scan at base e7fa8eafb7c5d9edd706f860cfc023e6c99b1ab2, 2026-11-05.
Full detail: `.ufo/waves/round-94/w1/stage/ConnectorLullaby94/overlap.md` (sha256 `d76c7a1220750ae78d0b3efd4f6186b3cb5c193ec117698769ea208abb654df6`).

## Counts (scan → result)

1. grep -i `lullab|cradle` over the 10 candidate owner files → **0**.
2. grep -i `nonsense|nonword|pseudo-word|pseudoword` over the same 10 → **0**.
3. grep -i `refrain|infant|age-grad|caretaker|motherese|baby talk` over the same 10 → **13 lines**: language-socialization-and-acquisition.md 16,17,19,24,25,34; sociolinguistics-registers.md 3,110,112,114; sacred-registers-liturgical-language.md 95; naming-systems.md 7,105 (105 = verb "refrains from", false positive).
4. grep -i `lullab|cradle song` over all corpus/knowledge → **1**: myth-symbol/motif-index-usage.md:108 ("one motif fossilized in jokes or lullabies") — passing clause, no owner.
5. grep -i `song|sing|chant|lament|cradle` over orality-formulaic-language.md → all adult-performance material; no child-directed content.
6. grep -i `lullab|cradle|nonsense syllable` over corpus/SOURCES.md → **1**: S765 "cradle of chess" metaphor (false positive); no lullaby source rows — S965+ rows are unclaimed.

## Overlap table summary

| owner | ground it holds | overlap |
|---|---|---|
| linguistics/language-socialization-and-acquisition.md (16,17,19,24,25,34) | IDS/caregiving: S718 IDS variability, S719 IDS prosody, S729 "questions, imperatives, and singing were more frequent in infant-directed than adult-directed speech", S720/721 babble/turn-taking, S743 child-directed verbs | **partial** — closest in lane; owns interactional/prosodic side, no lullaby text or design procedure |
| linguistics/orality-formulaic-language.md (3,66,68,99,113,136) | adult oral-formulaic art, lament type-scene, incremental repetition, singer's-speech register, archaism fossilization | **partial** — machinery borrowed, not restated |
| linguistics/sociolinguistics-registers.md (3,110–114) | age-grading (speaker-age indexed) | none (lite) |
| linguistics/register-strata-attestation.md | attestation register | none |
| linguistics/sacred-registers-liturgical-language.md (95) | "memorized refrain (partial 2)" hymn mode | none (word collision) |
| linguistics/phonetics-phonology.md / sound-symbolism.md | phonotactics/prosody; iconicity | none (couple only) |
| linguistics/naming-systems.md (7,105) | names, teknonymy | none |
| culture-material/dance-performance-movement-codes.md (20,22) | dance-song-voice coupling | none |
| myth-symbol/death-afterlife-eschatology.md | death doctrine, funerary rite | none |
| myth-symbol/motif-index-usage.md (108) | passing lullabies clause | none |

**Duplicate verdict: no full overlap anywhere; the new entry duplicates nothing.** All narrowing goes on the new entry's side: no IDS-prosody section, no melody/rhythm, no Parry–Lord machinery, no liturgical refrain, no mourning song.

## Boundary sentence (proposed)

> This entry owns the verbal text of songs directed at a child — the sleep-inducing formulae, the nonsense-syllable refrains, the archaic retention preserved in lullaby text, the forms of address to the child, the register shift between the song and ordinary speech, and a design procedure for a fictional lullaby register — and it owns no melody or accompaniment (`culture-material/music-instrument-lexicon.md`, `culture-material/dance-performance-movement-codes.md`), no infant-directed prosody or caregiving interaction beyond the song text itself (`linguistics/language-socialization-and-acquisition.md`), no oral-epic or ballad composition machinery beyond borrowed vocabulary (`linguistics/orality-formulaic-language.md`), no liturgical refrain (`linguistics/sacred-registers-liturgical-language.md`), and no mourning song or funerary rite (`linguistics/orality-formulaic-language.md`, `myth-symbol/death-afterlife-eschatology.md`).

## Couples line (proposed)

```
- couples: `linguistics/language-socialization-and-acquisition.md` (infant-directed speech, prosody, and caregiving interaction; this entry takes only the song text), `linguistics/orality-formulaic-language.md` (formulaic composition, incremental repetition, and archaism-fossilization machinery for adult verbal art; borrowed, not restated), `linguistics/sociolinguistics-registers.md` (register and age-grading machinery), `linguistics/phonetics-phonology.md` (phonotactics and prosody tools the nonsense syllables must fit), `linguistics/sound-symbolism.md` (meaningless-syllable sound play versus engineered iconicity), `linguistics/sacred-registers-liturgical-language.md` (refrain as liturgical participation mode, distinct from the lullaby refrain), `linguistics/naming-systems.md` (child-name inventory and teknonymy behind the address forms), `culture-material/music-instrument-lexicon.md` (melody, rhythm, accompaniment; this entry owns no music), `culture-material/dance-performance-movement-codes.md` (dance-song-voice coupling and performance framing), `myth-symbol/motif-index-usage.md` (lullabies noted as a motif-fossilization site)
```

## Adjacency duty (contested scopes → owner)

1. Lullaby as music → music-instrument-lexicon + dance-performance-movement-codes; not absorbed.
2. IDS prosody / caregiving interaction (S718, S719, S729 hinge) → language-socialization-and-acquisition.md.
3. Liturgical refrain → sacred-registers-liturgical-language.md:95; lullaby refrain is the new entry's.
4. General archaic-retention machinery (fossilization, H/L split) → orality-formulaic-language.md; new entry shows only the lullaby-text case.
5. Mourning songs / songs for dead children → orality lament + death-afterlife-eschatology rite.
6. Child vocatives/endearments/name inventory → naming-systems.md; sung address forms stay with the new entry.
7. Nonsense syllables as engineered iconicity → sound-symbolism.md; the refrain-formula convention stays with the new entry.
8. Motif fossilization in lullabies → already named at motif-index-usage.md:108; couples clause suffices.

## Housekeeping

- Files written: `stage/ConnectorLullaby94/overlap.md`, `stage/ConnectorLullaby94/DONE` (sha256 of overlap.md, rc 0), this trailer. No other files touched; no git/jj mutations; frozen files untouched.
- Tooling installed: none. pacman: not invoked (host-wide pause respected). Sysctls: untouched. Scratch `/fast/scratch/hyaku/kotodama-r94/ConnectorLullaby94/` deleted (never used; no writes needed).
- Blockers: none.
