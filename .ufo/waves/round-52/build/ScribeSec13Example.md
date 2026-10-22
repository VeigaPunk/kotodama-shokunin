# ScribeSec13Example — Claim C, section `## 11. NON-CANON worked micro-example`

## Assigned item

Draft the section `## 11. NON-CANON worked micro-example` (budget 9 lines) for the C entry
`corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md`: one invented ravine
culture with a tonal language and a herding economy, walked through the §10 decision table
(sections 3-9) — channel, encoding, stock phrases, who may drum or whistle, one decline
driver — plus three invented example messages described by tone or pitch contour. Registry
row drafts and Gate lines for the sources I opened. No product file was edited: the C entry
does not exist yet at the lane worktree (`test ! -e corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md`
→ NO), so this seat returns paste-ready text only.

## Result

Paste-ready text below, 9 lines of section content (H2 line through the last table row).
Two sources were opened by ordinary means (direct request, no headless browser, no
challenge): Meyer 2004 (SciELO open PDF) and Seifart et al. 2018 (PMC full text). Row drafts
use the seat's draft ids `NEW-ScribeSec13Example-1` and `-2`; the L1 assigns the final
S-ids (S134 upward) at integration.

## Paste-ready section text

```markdown
## 11. NON-CANON worked micro-example

**NON-CANON.** The Coldwater ravine culture, its language (Coldwater, tonal, spoken by herding households that keep goats and sheep above the tree line), its places, its phrases and every number below are invented; nothing here describes a real people, and canon belongs to lore-shokunin. Walked through the §10 decision table: channel — two, a two-note whistle and a hide drum, because the ravine walls carry pitch further than they carry rhythm (§7; design frame, **H**); encoding — the whistle keeps the language's lexical tone and vowel length and reduces consonants to transitions, which a tonal language can afford because pitch level characterizes the syllable (NEW-ScribeSec13Example-1; §4), while the drum carries pause length and a closed set of stock phrases, because four rhythmic units ride the pauses and tone alone separates few words (NEW-ScribeSec13Example-2; §5, §6); stock phrases — 24 fixed herding formulas, one drum pattern each, drawn from the oral formula banks (`orality-formulaic-language.md:114`, `:124`); who may speak it — whistling is open to every adult of the herding households, drumming is licensed to the herd-criers and is the channel outsiders must not overhear (§8; performer licensing stays at `orality-formulaic-language.md:112`); decline driver — the new valley road brings a lorry line and a school that teaches the valley's trade language, so the whistle stops being learned and only the drum formulas survive as ritual (§9). The failure to design around is a drum that carries only a closed list of calls, which would be a signal code rather than a surrogate (§1, §3). The tone-and-drum couplings stay with `phonetics-phonology.md:197-199`, instrument naming with `../culture-material/music-instrument-lexicon.md:98-100`, and channel iconicity with `sound-symbolism.md:121`.

| Invented message (English gloss) | Channel and contour |
|---|---|
| "the goats are up at the north spring" | whistle: three notes, level, rising, level; the mid tone of the second word is the only cue that separates it from its neighbour |
| "the herd moves to the upper pasture tonight" | drum: six beats with a long pause before the fourth, the pause pattern that marks the stock phrase; no melody and no pitch |
| "how many sheep are left?" | whistle: rising, then falling, the last note held twice as long, the contour that asks for a count |
```

## Line count

| line | content |
|---|---|
| 1 | `## 11. NON-CANON worked micro-example` |
| 2 | blank |
| 3 | the `**NON-CANON.**` paragraph |
| 4 | blank |
| 5 | table header |
| 6 | table separator |
| 7 | message 1 |
| 8 | message 2 |
| 9 | message 3 |

Note for the L1: the section is 9 lines as budgeted. Every section of this entry is followed
by one blank line before the next `## ` heading, so the block as it lands in the file is 10
lines (line 10 = that separator blank, which also satisfies the entry contract's blank line
after a pipe table). If the budget is read as including that blank, move message 3 into the
paragraph: add the sentence `A third invented message, "how many sheep are left?", is a
whistle: rising, then falling, the last note held twice as long, the contour that asks for a
count.` and drop the third table row — that variant is exactly 9 lines including the
separator blank.

## Registry row drafts

Rows use the 11 columns of `corpus/SOURCES.md:28` (id, source, kind, tier, scope, anchor,
teaches, status, opened, recheck, used-by). The L1 renumbers `NEW-ScribeSec13Example-n` to
the final S-id and sets `used-by` if the entry lands under a different path.

```markdown
| NEW-ScribeSec13Example-1 | Meyer, Julien 2004, "Bioacoustics of human whistled languages: an alternative approach to the cognitive processes of language", Anais da Academia Brasileira de Ciencias 76(2):405-412 — https://www.scielo.br/j/aabc/a/C7c5W8SQmKmGxgdV4T5JbRJ/?lang=en&format=pdf | paper | B | the acoustic design space of whistled speech as surveyed by the author; a 2004 review, not a primary study of any one whistled language, and its counts are the author's own | §Linguistic considerations, tonal-languages paragraph (printed p. 408); Abstract | a whistle is a transposition of a local language into a repertoire of whistles; in a tonal language the pitch level characterizes the syllable, so a whistle can carry tone while consonants must be repaired by frequency modulation | mined | 2026-10-22 | 365d | corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md |
| NEW-ScribeSec13Example-2 | Seifart, Meyer, Grawunder & Dentel 2018, "Reducing language to rhythm: Amazonian Bora drummed language exploits speech rhythm for long-distance communication", Royal Society Open Science 5:170354, doi 10.1098/rsos.170354 — https://pmc.ncbi.nlm.nih.gov/articles/PMC5936885/ | paper | A | what drummed Bora encodes (rhythm, tone, conventional markers) as the authors' own measured result; one language, not a law for other drum systems | Abstract; §1.2 "Tone, rhythm and enphrasing in drummed speech" | drummed messages encode four rhythmic units in the length of pauses between beats; the two tones carry few lexical contrasts, so rhythm and conventional markers do the disambiguating | mined | 2026-10-22 | 365d | corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md |
```

Tier notes. Row 1 is tier B because it is the author's 2004 review (a survey), used only
for the acoustic design frame (pitch carries the syllable in a tonal language); it is not
used for any claim about a living community. Row 2 is tier A: it is the primary published
paper of a peer-reviewed study, opened as the PMC full text (open access), and it is used
only for the design points it measures — pause-length rhythm, tone's small lexical load,
conventional markers.

## Gate lines

Format copied from `corpus/lessons/round-51.md:28-36`.

```markdown
- NEW-ScribeSec13Example-1 — https://www.scielo.br/j/aabc/a/C7c5W8SQmKmGxgdV4T5JbRJ/?lang=en&format=pdf — accessed 2026-10-22 — §Linguistic considerations, tonal-languages paragraph (printed p. 408): "As far as the tonal languages are concerned, the pitch level characterizes the composition of the syllable and has a phonological signification." Grounds: in a tonal language a whistle can keep pitch, so a designer may drop consonants and keep tone on the whistle channel (§4 of the entry). Seat: ScribeSec13Example.
- NEW-ScribeSec13Example-1 — https://www.scielo.br/j/aabc/a/C7c5W8SQmKmGxgdV4T5JbRJ/?lang=en&format=pdf — accessed 2026-10-22 — Abstract: "Whistled languages can be regarded as a transposition of a given local language into a repertoire of whistles." Grounds: a whistle surrogate carries the local language itself, not a fixed call list (§1, §3 of the entry). Seat: ScribeSec13Example.
- NEW-ScribeSec13Example-2 — https://pmc.ncbi.nlm.nih.gov/articles/PMC5936885/ — accessed 2026-10-22 — Abstract: "We show that four rhythmic units are encoded in the length of pauses between beats." Grounds: a drum register can carry stock phrases by pause length and rhythm (§5, §6 of the entry). Seat: ScribeSec13Example.
- NEW-ScribeSec13Example-2 — https://pmc.ncbi.nlm.nih.gov/articles/PMC5936885/ — accessed 2026-10-22 — Abstract: "The two phonological tones represented in drummed speech encode only few lexical contrasts." Grounds: tone alone is a weak carrier, so a designer must add rhythm, markers and stock phrases (§6 of the entry). Seat: ScribeSec13Example.
```

All four quotes were checked verbatim against the fetched files (Meyer: `pdftotext` of the
SciELO PDF, reading order; Seifart: the PMC full-text HTML). No quote exceeds 25 words.

## In-corpus anchors cited in the section (re-read at the lane worktree, HEAD `dea5ece`)

| anchor | what it owns (pointed at, never restated) |
|---|---|
| `corpus/knowledge/linguistics/phonetics-phonology.md:197-199` | the whistled-speech and drum-language couplings under "Solid couplings" |
| `corpus/knowledge/culture-material/music-instrument-lexicon.md:98-100` | the "instruments that speak" row and the talking-drum coupling note |
| `corpus/knowledge/linguistics/orality-formulaic-language.md:114` | media extensions: tonal languages riding drums and whistled registers |
| `corpus/knowledge/linguistics/orality-formulaic-language.md:124` | the lexical-tone row of the meter decision table (drum/whistle speech) |
| `corpus/knowledge/linguistics/orality-formulaic-language.md:112` | performer licensing (hereditary guild, apprenticeship) |
| `corpus/knowledge/linguistics/sound-symbolism.md:121` | the music row: drum/whistle speech as phonological encoding on instruments |

Cross-partition paths are written `../culture-material/…` as in the model entry
`corpus/knowledge/linguistics/sign-languages-manual-modality.md`. The four partial owners
named in the wave context are cited one way only; no sentence of theirs is repeated here.

## What the example decides, and the failure it avoids

The worked example fixes, in the §10 order: two channels and why (ravine terrain, §7); what
each channel encodes (tone and vowel length on the whistle, pause length and a closed
formula set on the drum, §4-§6); how ambiguity is repaired (24 stock phrases, one drum
pattern each, from the oral formula banks); who may use each channel (whistle open to
adults of the herding households, drum licensed to the herd-criers and used where outsiders
must not overhear, §8); and one decline driver (the valley road with a lorry line and a
school that teaches the valley's trade language, so the whistle stops being learned, §9).
The typical failure named in the paragraph is a drum that carries only a closed list of
calls — that is a signal code, not a surrogate (§1, §3). Everything in the section is
invented and marked as such; no real community, language or number is described.

## Unrun checks and limits

- No file in the lane was created or edited except this report. The C entry was not written,
  so the section text was not pasted, and no head, heading, README, SOURCES or lesson check
  was run against a landed file.
- No `§N` reference in the draft exceeds the entry's highest H2 number (references are
  §1, §3, §4, §5, §6, §7, §8, §9, §10).
- The sibling sections were not available at drafting time; the section numbers used here
  (3 typology, 4 whistled, 5 drummed, 6 encoding, 7 ecology, 8 who may speak, 9
  transmission/decline, 10 decision table) match the planned numbering in the wave context
  and the sibling seat titles. If a sibling renumbers, the `§N` pointers in the paragraph
  need a matching edit.
- The Meyer PDF was read from the SciELO copy; the Annual Reviews typology review
  (`10.1146/annurev-linguistics-011619-030444`) answered HTTP 403 on a plain request, so it
  was not used, and no attempt was made to route around that refusal.
- The Wikipedia page on whistled speech was not opened and is not cited; a tier C lead is
  never sole support.
- The three messages are English glosses of invented Coldwater speech; they are not
  translations of any documented language and carry no numbers or distances.

## Tooling record

No installs and no updates: the work used the system `python3`, `curl`, `pdftotext`
(poppler, already present) and the `read` tool. Nothing was installed, upgraded or
downgraded; no host service was touched.

## Notes for the L1

1. Section text above is ready to paste; decide the 9-versus-10-line reading from the
   line-count note.
2. Two frontier rows, ids `NEW-ScribeSec13Example-1` and `-2`, with the four Gate lines
   above; both rows carry `status = mined`, `opened = 2026-10-22`, `recheck = 365d` and
   `used-by = corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md`.
3. Both rows were opened by ordinary means (plain request, public open-access copy). No
   headless browser, no challenge, no login: QUALITY criterion 10 holds for both.
4. The worked example uses no S-id below S134 and no `corpus/lessons/round-52.md` path.
