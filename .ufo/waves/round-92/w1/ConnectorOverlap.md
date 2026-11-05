# Overlap scan — planned `corpus/knowledge/linguistics/ideophones-mimetics.md` (round 92, seat ConnectorOverlap)

Read-only seat. Paths are relative to /home/vgpnk/Projects/shokunin/kotodama-shokunin unless marked as a fleet-root path. Read-only Grep and Read calls ran 2026-11-05. Nothing was written outside the stage dir and the Report trailer.

## Summary

- **Contested scope: YES, one real overlap.** `linguistics/sound-symbolism.md` §6 (lines 99–111) already holds the ideophone word-class definition, the grammar profile, reduplication, the Japanese giongo/gitaigo system, a five-step ideophone register design procedure, and a diachrony note. The corpus index row (`corpus/README.md:372`) and the entry's header (`sound-symbolism.md:3`) advertise the same content. A new entry with a typological definition and a design procedure would be a second home for one claim, the failure mode `sound-symbolism.md` D1 (:142) names.
- **Ground the new entry can own without overlap:** Cushitic and Ethiosemitic ideophone grammar (S958 Kambaata, S959 Amharic), the word-class question (S957), and whatever S960 (Benítez-Burraco 2026) covers. A Grep over `corpus/` for `amharic|kambaata|ethiosemitic|cushitic|marsault|benítez|benitez` returned no ideophone claim. The hits were Geʿez/Ethiosemitic civilization material (`civilizations/aksum-ethiopia.md:33–51`, `:118–122`), a Cushitic lexicon mention (`linguistics/language-contact.md:114`), and a Cushitic family mention (`linguistics/morphological-typology.md:59`).
- **Sibling boundaries:** no sibling lane owns ideophones or mimetics. chousa owns research method, lore owns canon, kotoba owns prompt and skill craft, and kasegi is unrelated. The entry is a non-canon design-and-method reference and must say so.

## 1. Lane-internal: nearest owners of ideophone / mimetic / onomatopoeia material

| rank | file | section / line | what it holds | what the new entry must NOT absorb |
|---|---|---|---|---|
| 1 | `corpus/knowledge/linguistics/sound-symbolism.md` | §6 "Ideophones — the depictive class" :99–111. :101 class definition (Dingemanse 2012). :102 grammar profile (Dingemanse & Akita 2017, to-verify). :103 reduplication (Dingemanse 2015). :104 Japanese giongo/gitaigo (Hamano 1998; Kita 1997). :105–110 five-step ideophone register design procedure. :111 diachrony (Dingemanse 2018). | the ideophone class, its grammar, and its design procedure | All of §6. Also §1 three-way map :21–41, §5 phonesthemes :88–98, §8 calibration shelf :126–139 (C1–C9), §9 decisions D1–D7 :140–148. Sound-symbolic token effects (bouba/kiki, frequency code, Blasi signals) stay there. |
| 2 | `corpus/knowledge/synthesis/myth-to-language-derivation.md` | §2 table row :32 "Ideophone / sound imitation"; row :31 productive morpheme; §6 worked derivation B :84–100 (phonestheme sets with controls) | the rule that an ideophone is not automatically a sacred word, phonestheme, or divine name | The myth-to-ideophone derivation chain (§1 :16–24), and any sacred-ideophone claim. The new entry may cite :32 and must not restate it. |
| 3 | `corpus/knowledge/linguistics/phonetics-phonology.md` | §8 "Sound symbolism" :246–256 (compressed parent). §9 pitfall 7 :266. §10 handoff :273–280 (names `sound-symbolism.md` as a sibling). Couples :72–77. | phonetic-level symbolism summary and the "dictionary-itis" pitfall | Phonetic inventory mechanics (D1 keeps them there). |

Partial and noise owners, named so the new entry does not treat them as owners:

- `culture-material/music-instrument-lexicon.md:59` has a "sound / onomatopoeia" naming row for instrument names (*pipa*, *didgeridoo*). Instrument naming stays there.
- `linguistics/register-lexicon-ceilings.md:303,305,314–315` and §12 :291–317 treat the phrase `which semantic fields` as a pre-existing ideophone-sense hit (`sound-symbolism.md:106`). **Hazard:** if the new entry's fields step reuses "which semantic fields", its future absence and presence sweeps collide with the round-28 X63-F2 record. Use different wording.
- `myth-symbol/ritual-liminality.md:53,130` uses "mimetic" for Girard's mimetic mechanism. That is a different sense; do not cite it as an ideophone owner.
- `linguistics/speech-surrogates-whistled-drummed.md:37,71` and `sound-symbolism.md:121` are hook rows to music and drums with no ideophone claim.
- `SOURCES.md:818` (S863, Chhau dance) cites "daily-chore mimetics" as dance-vocabulary evidence. It is a source row, not an owner, and the new entry may cite it only for dance movement.

Corpus index: `corpus/README.md:371–373` lists `sociolinguistics-registers.md`, `sound-symbolism.md`, and `speech-surrogates-whistled-drummed.md` in filename order. The new row goes by filename order among the linguistics rows. The row for `sound-symbolism.md` (:372) already claims "ideophones as a depictive word class … an ideophone-register design procedure". The new row must not repeat that claim for the same content.

## 2. Sibling lanes: boundaries the entry must respect

Fleet-root paths, all read-only.

- **chousa-shokunin (research method), `chousa-shokunin/PROVINCE.md`.** Owns question framing, source hierarchy (primary / secondary / aggregator / unsourced), citation chaining, claim-vs-source verification, and search-strategy taxonomy (:5–8). Refuses bounty scope, model evaluation, orchestration, and external live-target research (:10–15). Out-of-province items go to report, not absorption (:17).
  - Boundary: the entry may cite sources and carry located quotes under its own gate. It must not restate chousa's source hierarchy, claim-vs-source method, or search taxonomy as its own method. Its tier labels follow kotodama's registry (`corpus/SOURCES.md`), not chousa's hierarchy.
- **lore-shokunin (canon), `lore-shokunin/PROVINCE.md`.** Owns fictional-world records and consistency verification (:3). Refuses claiming canon without an in-world citation (:9). Its adjacency names kotodama for generated-content handoff packets and says chousa is research method, not lore canon (:27–28).
  - Boundary: the entry is a non-canon design-and-method reference. It must not carry an in-world ideophone inventory for a named culture or a handoff-packet framing. Kotodama's own contract agrees: `corpus/knowledge/synthesis/worldbible-integration-contract.md:12` ("method/reference contract, not a world-bible entry, canon ruling"), `:17` (kotodama owns generative craft; lore owns canon), and `:209` (division of labour).
- **kotoba-shokunin (prompt and skill craft), `kotoba-shokunin/PROVINCE.md`.** Domain is prompt and skill craft (:3). Its kotodama row (:69) says kotodama "refuses prompt/skill craft by name" and kotoba owns that craft.
  - Boundary: no LLM-prompt use of ideophones as a generation technique, and no SKILL or AGENTS wording. The fictional depictive-register procedure is linguistic craft and belongs to kotodama. A prompt that elicits ideophones belongs to kotoba.
- **kasegi-shokunin (bounty and security research), `kasegi-shokunin/PROVINCE.md:3`.** No overlap. Refuses anything outside bounty and security scope (:25). Verdict: none.

Kotodama's own refusals (`PROVINCE.md:16–20`) match these: canon goes to lore, general source-research method to chousa, and prompt/skill craft to kotoba.

## 3. Contested scope and evidence pointers

1. **Ideophone class, grammar, and design procedure already live in `sound-symbolism.md` §6.** Evidence: `sound-symbolism.md:99–111`, `corpus/README.md:372`, `sound-symbolism.md:3`. The L1 must choose: (a) the new entry owns the word-class debate, the Cushitic and Ethiosemitic grammar, and acquisition and processing, and §6 becomes a pointer; or (b) the new entry keeps only what §6 lacks and points to §6 for the rest. Option (b) matches the D7 recheck note, "deduplicate by pointer, not by deletion" (`sound-symbolism.md:148`). Either option edits `sound-symbolism.md`, which is outside this seat's scope.
2. **Japanese mimetics.** Already at `sound-symbolism.md:104`, with page-level details marked to-verify at :15 and :17. The new entry must not add Japanese forms beyond that. Its own sources are S957–S960 in `reports/round-92/evidence/manifest.json`. The manifest quote for S957 is "whether or not ideophones make up a clear-cut word class in different languages", and for S958 it is "do they constitute a word class on their own, or should they be subsumed under another word class".
3. **Sound-symbolic token effects.** Stay in `sound-symbolism.md` §§2–4 (Blasi, bouba/kiki, Ohala). The shelf rules C7 and C9 (:136–137) apply to any reuse.
4. **Phonestheme and sacred-ideophone separation.** Stays in `myth-to-language-derivation.md:32`. The new entry may cite it.
5. **Acquisition and processing (in the claimed topic).** `sound-symbolism.md:14` cites Imai & Kita 2014 as the acquisition wedge and the §7 hook row at :113–124 marks it to-verify. No ideophone-acquisition claim was found elsewhere in `corpus/knowledge/`. The new entry can own this ground; it must mark Imai & Kita to-verify unless it captures a located quote.
6. **Index-phrase hazard.** `which semantic fields` (`sound-symbolism.md:106`; `register-lexicon-ceilings.md:303,305,314–315`). Do not reuse it in the new entry.

No sibling-lane contest beyond the boundaries in §2.

## Commands run (read-only) and results

- Grep `(?i)ideophon|mimet|onomatop|sound.?symbol` over `kotodama-shokunin/corpus/knowledge` — hits in `linguistics/sound-symbolism.md`, `linguistics/phonetics-phonology.md`, `linguistics/register-lexicon-ceilings.md`, `linguistics/speech-surrogates-whistled-drummed.md`, `culture-material/music-instrument-lexicon.md`, `synthesis/myth-to-language-derivation.md`, and `myth-symbol/ritual-liminality.md`.
- Grep `(?i)ideophon|mimetic|onomatop|sound.?symbol|linguist|conlang` over the four sibling `PROVINCE.md` and `SKILL.md` files — the only hits were `linguist`/`linguistic` wording (kotodama's own naming in `lore-shokunin/PROVINCE.md:28`, kotodama's row in `kotoba-shokunin/PROVINCE.md:69`). No ideophone, mimetic, or onomatopoeia term appears in any sibling province or skill file.
- Grep `(?i)amharic|kambaata|ethiosemitic|cushitic|marsault|benítez|benitez|S95[7-9]|S960|depictive` over `corpus` and `reports/round-92/evidence/manifest.json` — manifest rows S957–S960 are present; no ideophone claim is attributed to Kambaata or Amharic in the corpus prose.
- Grep `^## ` over `sound-symbolism.md`, `register-lexicon-ceilings.md`, `phonetics-phonology.md`, and `myth-to-language-derivation.md` — section lines cited above.
- Province reads: `chousa-shokunin/PROVINCE.md`, `lore-shokunin/PROVINCE.md`, `kotoba-shokunin/PROVINCE.md`, `kasegi-shokunin/PROVINCE.md`, `kotodama-shokunin/PROVINCE.md` (:10–25), and `kotodama-shokunin/SKILL.md:3`.

## Could not measure

- S957–S960 bodies were not read. Their topic overlap with §6 is inferred from manifest quotes and titles only.
- `corpus/SOURCES.md` was not checked for rows that cite Dingemanse or Kita beyond the `sound-symbolism.md` source block.
- The `lore*` glob matched one directory, `lore-shokunin`. No separate `lore/` lane directory exists in the fleet listing.
- Working tree was read, not the freeze pin `066b9728`. The `lore` directory listing was not checked against git history.
