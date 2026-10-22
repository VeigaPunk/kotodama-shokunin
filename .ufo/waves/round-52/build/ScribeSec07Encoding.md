# ScribeSec07Encoding — Claim C, section `## 6. Encoding and ambiguity`

## Assigned item

Draft the section `## 6. Encoding and ambiguity` (budget 15 lines) for the C entry
`corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md`: a decision table for
what the designer must choose — which features ride the channel (tone, length, rhythm, vowel
quality, consonant transitions), what is lost, how the loss is repaired (stock phrases and long
epithets, context restriction to a few topics, repetition, call-and-answer repair) — and the
information-rate cost. Registry row drafts and Gate lines for the sources opened. Read-only
seat: no product file was created or edited; the C entry does not exist yet at the lane
worktree, so this seat returns paste-ready text only.

## Result

Paste-ready text below: the fenced block is 15 lines — H2 line, blank, framing paragraph, blank,
table, five rows, blank, two closing paragraphs, and the blank line that separates §6 from §7.
Seven
external sources were opened by ordinary means (plain `curl` or
the `read` tool; no headless browser, no challenge, no login). Row drafts use the seat's draft
ids `NEW-ScribeSec07Encoding-1` … `-7`; the L1 assigns the real S-ids (S134 upward) at
integration and must replace every `NEW-ScribeSec07Encoding-n` token in the entry text with
the final S-id.

## Paste-ready section text

```markdown
## 6. Encoding and ambiguity

A surrogate channel is a lossy channel, so the first decision is which features of the spoken language ride it and which are dropped; status codes: **B** for the attested measurements below, **H** for the design frame (`../verification/calibration-registry.md:35-39`).

| Feature the designer assigns | What rides the channel | What is lost | Repair, and the typical failure |
|---|---|---|---|
| **Tone** | one instrument pitch per tonal level: in the Bora *manguaré* system of the northwest Amazon the talking mode uses two pitches, one on each drum (NEW-ScribeSec07Encoding-1) | finer tonal structure — two notes cannot render downstep, as the Akan atumpan pair shows (`../civilizations/akan.md:58`), and for tonal bases the surrogate strips away segmental features to keep the tonal ones (NEW-ScribeSec07Encoding-6) | stock phrases: a short word that would come out a drum homophone is replaced by a longer conventional expression (NEW-ScribeSec07Encoding-1), as with the Kele people of the Stanleyville area of the Congo, whose 'manioc' is always drummed as 'the manioc which remains in the fallow ground' (NEW-ScribeSec07Encoding-5); the failure is one melodic shape per event, which leaves no way to tell which message was meant (`../civilizations/yoruba.md:46-47`) |
| **Length** | pause length between beats; four rhythmic units match vowel-to-vowel intervals with different consonant counts and vowel lengths (NEW-ScribeSec07Encoding-1) | the syllable as the unit — aligning beats with syllables, mora or vowel length alone gives inconsistent results (NEW-ScribeSec07Encoding-1) | longer stereotyped phrases, whose extra length is what makes them identifiable (NEW-ScribeSec07Encoding-5); the failure is a fixed beat-per-letter cipher, which no source documents and the lane forbids inventing (`../civilizations/fon-dahomey.md:46`) |
| **Rhythm** | the beat sequence and its timing, plus the conventional rhythmically distinct markers that separate words (NEW-ScribeSec07Encoding-1) | segmental detail, dropped as the signal simplifies (NEW-ScribeSec07Encoding-6) | framing and markers: messages conventionally carry an opening signal and a closing signal (NEW-ScribeSec07Encoding-6); the failure is free composition, so no two drummers read the same sequence alike (**H**) |
| **Vowel quality** | in whistled speech the whistle's frequency stands in for the vowel's second formant, and vowels sit at different frequency levels with consonants as modulations around them (NEW-ScribeSec07Encoding-3, NEW-ScribeSec07Encoding-7) | the voice's complex spectrum: a whistle carries its high power in one band, 800 to 4000 Hz (NEW-ScribeSec07Encoding-7) | a small fixed set of vowel-bearing forms whose contour carries the word (**H**); the failure is designing more vowel contrasts than the channel can hold (**H**) |
| **Consonant transitions** | in whistled speech, as frequency and amplitude modulations of the steadier vowel frequencies (NEW-ScribeSec07Encoding-7); on the drum, only as a count of consonants inside a vowel-to-vowel interval (NEW-ScribeSec07Encoding-1) | consonant place and manner, so drum homophones multiply (NEW-ScribeSec07Encoding-1) | long epithets and conventional elaborations — enphrasing, the strategy that operates on roteness and elaborateness at once (NEW-ScribeSec07Encoding-6); the failure is expecting the listener to recover the intended consonant from the melody alone (**H**) |

Four repairs, in the order a designer should apply them: stock phrases and long epithets, since the elaborateness of the Kele drum names is what differentiates the tonal patterns without ambiguity (NEW-ScribeSec07Encoding-5, NEW-ScribeSec07Encoding-6); repetition, because the drum form is much longer "because of the repetition necessary to make the meaning clear" (NEW-ScribeSec07Encoding-5); restriction to a few topics, since context is "an important tool for combatting the problem of ambiguity, since it allows listeners to use context to their advantage" (NEW-ScribeSec07Encoding-6); and call-and-answer repair: in the whistled register of San Pedro Sochiapam Chinantec, Oaxaca, the open repair format is favoured over the restricted one, which Sicoli attributes to a reduced semiotic carrying capacity of the whistled channel (NEW-ScribeSec07Encoding-2), and the attested failures were repaired with a limited set of standard questions and interjections (NEW-ScribeSec07Encoding-6). The couplings that place a surrogate in its world stay with `phonetics-phonology.md:197-199` and `../culture-material/music-instrument-lexicon.md:98-100`; the formula broadcast layer with `orality-formulaic-language.md:114` and `orality-formulaic-language.md:124`; the music row with `sound-symbolism.md:121`. Test the result the lane's own way: compare phrases that share a tonal pattern, add conventional expansions or contextual cues, and see whether trained listeners recover the intended message (`../civilizations/fon-dahomey.md:45`).
Rate cost: the channel carries less than the voice — whistled languages "encode less information from which to identify the intended speech sounds than voiced speech" (NEW-ScribeSec07Encoding-3) — and no surrogate channel in these sources is measured in bits per second, so the yardstick is the spoken one, 39.15 bits/s on average across 17 languages (NEW-ScribeSec07Encoding-4); the designer buys the loss back with redundancy and with a trained listener, since in Busnel's whistled Turkish experiments isolated words were recognized at about 70% against 80–90% for common whistled sentences (NEW-ScribeSec07Encoding-7).

```

## Line count

| line | content |
|---|---|
| 1 | `## 6. Encoding and ambiguity` |
| 2 | blank |
| 3 | the framing paragraph (status codes, calibration path) |
| 4 | blank |
| 5 | table header |
| 6 | table separator |
| 7 | row: tone |
| 8 | row: length |
| 9 | row: rhythm |
| 10 | row: vowel quality |
| 11 | row: consonant transitions |
| 12 | blank (the contract's blank line after a pipe table) |
| 13 | the four-repairs paragraph, ending with the one-way owner pointers and the prototype step |
| 14 | the rate-cost paragraph |
| 15 | blank (separator to §7) |

The block is 15 lines as pasted, the trailing blank included, so it drops in unchanged and
leaves §6 with its blank separator before the next `## ` heading. If the L1 counts the trailing
blank as belonging to §7, the section is 14 lines; either way the budget of 15 holds. If a
14-line reading is preferred, delete the last line of the fenced block.

**Trim rule, agreed with the sibling §4 seat so the two sections are not cut differently.** The
blank after the pipe table (line 12 here) and the blank before the next `## ` heading (line 15
here) both stay; they are what the entry contract and the model entry
`corpus/knowledge/linguistics/sign-languages-manual-modality.md` require. If a section has to
shrink, shrink a paragraph — in §6 that would mean folding the rate-cost paragraph into the
four-repairs paragraph, never deleting either blank. The sibling §4 seat's block is 16 lines
against a 16-line budget and lands on 16 as pasted, so it needs no L1 edit.

## Registry row drafts

Columns are the 11 columns of `corpus/SOURCES.md:28` (id, source, kind, tier, scope, anchor,
teaches, status, opened, recheck, used-by). The L1 renumbers `NEW-ScribeSec07Encoding-n` to
the final S-id (S134 upward) and keeps `used-by` = the entry path. No cell contains a pipe
character, so the `used-by` column index stays at 11 (`ExecCAcceptanceControls` §"used-by
column index").

```markdown
| NEW-ScribeSec07Encoding-1 | Seifart, Meyer, Grawunder & Dentel 2018, "Reducing language to rhythm: Amazonian Bora drummed language exploits speech rhythm for long-distance communication", Royal Society Open Science 5(4):170354, doi 10.1098/rsos.170354, opened as the PMC full text at https://pmc.ncbi.nlm.nih.gov/articles/PMC5936885/ | paper | A | what the Bora manguaré system of the northwest Amazon encodes (rhythm, tone, conventional markers) as the authors' own measured result; one language and one instrument, not a law for other drum systems | Abstract; §1.2 "Tone, rhythm and enphrasing in drummed speech"; §1.4 | drummed messages encode four rhythmic units in the length of pauses between beats, matching vowel-to-vowel intervals; the two tones carry few lexical contrasts; rhythmically distinct markers separate words | mined | 2026-10-22 | 365d | corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md |
| NEW-ScribeSec07Encoding-2 | Sicoli 2016, "Repair organization in Chinantec whistled speech", Language 92(2):411-432, doi 10.1353/lan.2016.0028, abstract read from the Crossref deposit at https://api.crossref.org/works/10.1353/lan.2016.0028 | paper | B | the publisher's abstract only; the article body was not opened, so the row is used for the abstract's own claims about repair organisation in the whistled register of San Pedro Sochiapam Chinantec, Oaxaca, and never as sole support | abstract field of the Crossref record | repair in whistled speech keeps the sequential organisation of spoken repair but shows fewer repair-initiation types, no preference for self-initiated repair, and an inversion favouring open over restricted repairs, attributed to the channel's reduced carrying capacity | mined | 2026-10-22 | 365d | corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md |
| NEW-ScribeSec07Encoding-3 | Belyk, Schultz, Correia, Beal & Kotz 2019, "Whistling shares a common tongue with speech: bioacoustics from real-time MRI of the human vocal tract", Proceedings of the Royal Society B 286(1911):20191116, doi 10.1098/rspb.2019.1116, opened as the PMC full text at https://pmc.ncbi.nlm.nih.gov/articles/PMC6784732/ | paper | A | what the whistle channel can and cannot carry, as the authors' own real-time MRI and bioacoustic result | Introduction, paragraph on robustness; §4(a) | whistled languages encode less information for identifying the intended speech sounds than voiced speech while remaining more robust over distance; the whistled frequency stands in for the vowel's second formant | mined | 2026-10-22 | 365d | corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md |
| NEW-ScribeSec07Encoding-4 | Coupé, Oh, Dediu & Pellegrino 2019, "Different languages, similar encoding efficiency: Comparable information rates across the human communicative niche", Science Advances 5(9):eaaw2594, doi 10.1126/sciadv.aaw2594, opened as the PMC full text at https://pmc.ncbi.nlm.nih.gov/articles/PMC6984970/ | paper | A | the spoken-language information rate used as the yardstick a lossy channel is measured against; not a measurement of any surrogate system, and not a claim about any one language | Abstract; Results, paragraph on IR and SR | cross-linguistic speech sits near 39 bits per second (mean 39.15, SD 5.10) across 17 languages, so a surrogate's loss should be stated against this baseline rather than as an absolute bit figure | mined | 2026-10-22 | 365d | corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md |
| NEW-ScribeSec07Encoding-5 | Finnegan 2012, "Drum Language and Literature", ch. 17 of Oral Literature in Africa, Cambridge: Open Book Publishers (CC-BY) — read as the Internet Archive open-access deposit of that edition, https://archive.org/details/oapen-20.500.12657-31251 (full-text file 633751_djvu.txt); the Open Book Publishers copy of the same chapter returned an interstitial page to a plain request | book | B | the Kele (Lokele) drum-language material as a scholarly survey reports it from Carrington 1949; Carrington's own 1949 book was not opened, so the row carries Finnegan's wording and citations, not Carrington's page images | ch. 17 §I ¶¶5-9 (the principles of drum language, the Kele examples, the extension to horns, flutes and gongs) and the section on drum names | drum homophones are avoided by stereotyped phrases whose extra length raises identifiability; 'manioc' is drummed as 'the manioc which remains in the fallow ground'; drum names are elaborated to differentiate tonal patterns; the same principle serves 'spoken' communication through other instruments | mined | 2026-10-22 | 365d | corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md |
| NEW-ScribeSec07Encoding-6 | James 2021, "Systems of Communication: Aspects of Culture and Structure in Speech Surrogates", Frontiers in Communication 6:653268, doi 10.3389/fcomm.2021.653268, opened as the open-access full text at https://www.frontiersin.org/journals/communication/articles/10.3389/fcomm.2021.653268/full | paper | B | the compensation strategies of speech surrogates as a review article collects them; its readings of other people's corpora are second-hand, so it supports framing, formulas, enphrasing and topic limitation rather than any claim about a community's own practice | "Compensation Strategies in Speech Surrogate Communication"; "Frames, Formulas, and Enphrasing"; "Enphrasing"; "Challenges for Speech Surrogate Communication" | enphrasing replaces a lexical unit with a phrase; frames open and close a message; formulas fix whole messages; repeated topics and shared context let listeners resolve ambiguity; a surrogate message carries less linguistic content than the speech it replaces | mined | 2026-10-22 | 365d | corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md |
| NEW-ScribeSec07Encoding-7 | Meyer, Magnasco & Reiss 2021, "The Relevance of Human Whistled Languages for the Analysis and Decoding of Dolphin Communication", Frontiers in Psychology 12:689501, doi 10.3389/fpsyg.2021.689501, opened as the open-access full text at https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2021.689501/full | paper | B | the acoustic and perceptual design of whistled speech as this article reviews and compares it; the recognisability percentages are Busnel's whistled Turkish experiments as reported here, not measurements made by the authors | "Human Whistled Speech Acoustic Structure: Encoding and Perception"; Figure 2 caption; "Socio-Environmental Parallels" | vowels sit at different frequency levels and consonants as modulations around them; the whistle works in a band of 800 to 4000 Hz; isolated whistled words were recognized at about 70% against 80-90% for common whistled sentences | mined | 2026-10-22 | 365d | corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md |
```

Tier notes. Row 1 and row 3 are tier A: each is the primary published paper of a peer-reviewed
study, opened as its PMC full text (open access), and each is used only for what it measures —
pause-length rhythm, tone's small lexical load and conventional markers (row 1); the
whistle's frequency-to-formant mapping and the information a whistle carries (row 3). Row 4
is tier A as the primary paper of a peer-reviewed study, used only for the spoken-language
information rate, which is a yardstick and not a claim about surrogates. Row 2 is tier B and
is the weakest row: it is the publisher's abstract, taken from the Crossref deposit, because
the article body is not openly reachable; it is therefore never the sole support for a claim —
the Chinantec repair finding is paired with row 6's field description. Rows 5, 6 and 7 are
tier B: a scholarly survey reporting Carrington rather than Carrington himself; a review
article whose readings of other people's corpora are second-hand; and an article that reviews
and compares whistled-speech studies and reports Busnel's percentages rather than measuring
them. No row in this seat's set is tier C.

## Gate lines

Format copied from `corpus/lessons/round-51.md:28-36` (ids are the seat's draft ids; the L1
substitutes the assigned S-ids).

```markdown
- NEW-ScribeSec07Encoding-1 — https://pmc.ncbi.nlm.nih.gov/articles/PMC5936885/ — accessed 2026-10-22 — Abstract: "We show that four rhythmic units are encoded in the length of pauses between beats." Grounds: pause length, not beat count, is the drum's rhythmic carrier, so the designer chooses interval classes (§6).
- NEW-ScribeSec07Encoding-1 — https://pmc.ncbi.nlm.nih.gov/articles/PMC5936885/ — accessed 2026-10-22 — Abstract: "The two phonological tones represented in drummed speech encode only few lexical contrasts." Grounds: tone alone separates few words, so the designer must add rhythm, markers and stock phrases (§6).
- NEW-ScribeSec07Encoding-2 — https://api.crossref.org/works/10.1353/lan.2016.0028 — accessed 2026-10-22 — publisher abstract deposited with Crossref: "an inversion of the frequency relation of OPEN and RESTRICTED repairs to favor open formats". Grounds: the Chinantec whistled register prefers open repairs, which is the call-and-answer repair a designer must plan (§6).
- NEW-ScribeSec07Encoding-2 — https://api.crossref.org/works/10.1353/lan.2016.0028 — accessed 2026-10-22 — publisher abstract deposited with Crossref, first sentence, closing clause: "whistled speech in San Pedro Sochiapam Chinantec of Oaxaca, Mexico". Grounds: the community and place the repair finding belongs to (§6).
- NEW-ScribeSec07Encoding-3 — https://pmc.ncbi.nlm.nih.gov/articles/PMC6784732/ — accessed 2026-10-22 — Introduction, paragraph on the whistle as a robust channel: "Whistled languages encode less information from which to identify the intended speech sounds than voiced speech, but are more robust to long-distance communication." Grounds: the information-rate cost of the whistle channel (§6).
- NEW-ScribeSec07Encoding-4 — https://pmc.ncbi.nlm.nih.gov/articles/PMC6984970/ — accessed 2026-10-22 — Results, paragraph on IR and SR: "We found that IR is centered on a mean of 39.15 bits/s with an SD of 5.10 bits/s". Grounds: the spoken-language rate baseline against which a surrogate's loss is stated (§6).
- NEW-ScribeSec07Encoding-5 — https://archive.org/download/oapen-20.500.12657-31251/633751_djvu.txt — accessed 2026-10-22 — ch. 17 §I, paragraph on stereotyped phrases: "the very extra length of the drum stereotypes or holophrases leads to greater identifiability in rhythmic and tonal patterning". Grounds: stock phrases buy identifiability, the classic repair for drum homophones (§6). Route: the same chapter is published by Open Book Publishers at https://books.openedition.org/obp/1206 and was read once through the plain reader tool, but a later plain request to that URL returned an interstitial page; the copy registered here is the Internet Archive open-access deposit of the same CC-BY edition, which a plain request reaches directly. No access control was involved at any point.
- NEW-ScribeSec07Encoding-6 — https://www.frontiersin.org/journals/communication/articles/10.3389/fcomm.2021.653268/full — accessed 2026-10-22 — "Enphrasing", first paragraph, James quoting Stern 1957 p. 127: "the lexical unit is replaced by a phrase". Grounds: the designer-facing name for the long-epithet repair (§6); Stern's own text was not opened.
- NEW-ScribeSec07Encoding-7 — https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2021.689501/full — accessed 2026-10-22 — "Human Whistled Speech Acoustic Structure: Encoding and Perception", paragraph on intelligibility: "isolate words are recognized at a rate of approximately 70%". Grounds: a trained listener's accuracy on isolated words, the price of a thin channel (§6).
```

Every quote was checked verbatim against the fetched file (PMC full-text HTML for rows 1, 3
and 4; the Internet Archive full-text file for row 5; the Frontiers full-text HTML for rows 6
and 7; the Crossref JSON record for row 2). No quote exceeds 25 words. The row-7 percentage is
quoted as a bare figure because the sentence's subject (Busnel's whistled Turkish experiments)
is named in the entry text next to it.

Fresh-route check, run on all seven row URLs on 2026-10-22 from a plain `curl` with a
browser user-agent: every URL returned HTTP 200, and no challenge marker
(`challenge-platform`, `Just a moment`, `captcha`, `Enable JavaScript and cookies`) appears in
the rendered text of any of them. Note for a reviewer who greps the raw HTML instead of the
rendered text: the two Frontiers pages carry the string "captcha" inside their
`window.__NUXT__` site-configuration script, which is not a challenge; both pages rendered
108,052 and 133,486 characters of article text respectively.

**Keep the PMC, Internet Archive, Crossref and Frontiers URLs in the registry rows.** The
`doi.org` redirects of two of these works do not survive a plain request on 2026-10-22:
`https://doi.org/10.1098/rsos.170354` answered HTTP 403 with a "Just a moment" interstitial,
and `https://doi.org/10.1353/lan.2016.0028` answered HTTP 429. The rows therefore name the
copy that was actually opened — the PMC full text for rows 1, 3 and 4, the Internet Archive
open-access file for row 5, the Crossref deposit for row 2 — with the DOI kept as a bare
identifier in the source cell rather than as the URL.

## In-corpus anchors cited in the section (re-read at the lane worktree, HEAD `5b7ecfb`)

| anchor | what it owns (pointed at, never restated) |
|---|---|
| `corpus/knowledge/linguistics/phonetics-phonology.md:197-199` | the whistled-speech and drum-language couplings under "Solid couplings" |
| `corpus/knowledge/culture-material/music-instrument-lexicon.md:98-100` | the "instruments that speak" row and the talking-drum coupling note |
| `corpus/knowledge/linguistics/orality-formulaic-language.md:114` | media extensions: tonal languages riding drums and whistled registers |
| `corpus/knowledge/linguistics/orality-formulaic-language.md:124` | the lexical-tone row of the meter decision table |
| `corpus/knowledge/linguistics/sound-symbolism.md:121` | the music row: drum and whistle speech as phonological encoding on instruments |
| `corpus/knowledge/civilizations/fon-dahomey.md:45` | the prototype rule: compare phrases sharing a tonal pattern, add conventional expansions, test trained listeners |
| `corpus/knowledge/civilizations/fon-dahomey.md:46` | the neighbouring ban on inventing a beat-to-letter cipher, a fixed transmission distance or a precise ceremonial rank |
| `corpus/knowledge/civilizations/yoruba.md:46-47` | the culture-specific dùndún case: many verbal strings share a tonal melody, and the melody maps one-to-many onto possible utterances |
| `corpus/knowledge/civilizations/akan.md:58` | the culture-specific atumpan case: the pair encodes only H and L, downstepped H is played as plain H |
| `corpus/knowledge/verification/calibration-registry.md:35-39` | the R/C/B/H/T status codes used in the section's first paragraph |

The four declared partial owners are cited one way only, in a single closing sentence of the
section, with no sentence of theirs repeated. The three `civilizations/` files are cited for
their own culture-specific cases, as the round-52 scout and reviewer asked; the design
conclusions in this section come from this seat's own rows. Cross-partition paths are written
`../culture-material/…`, `../civilizations/…`, `../verification/…`, as in the model entry
`corpus/knowledge/linguistics/sign-languages-manual-modality.md`.

## What the section decides, and the failure it avoids

The section fixes the channel before the lexicon: which of tone, length, rhythm, vowel quality
and consonant transitions the designer puts on the instrument, what the channel cannot carry,
and which repair pays for the loss. It names four repairs in the order they should be
applied — stock phrases and long epithets, repetition, restriction to a few topics, and
call-and-answer repair — and it states the price of the whole arrangement as redundancy and
training rather than as a bit figure no source measures. The typical failure named in each row
is the one the lane already records elsewhere: a signal code with one melodic shape per event
(`yoruba.md:46-47`), an invented cipher (`fon-dahomey.md:46`), free composition, more vowel
contrasts than the channel can hold, and a melody expected to yield its consonants on its own.
No community is exoticised: Bora of the northwest Amazon, the Kele of the Stanleyville area,
and San Pedro Sochiapam Chinantec in Oaxaca are named with their own channel systems, and
nothing is claimed about any living practice beyond what the sources state.

## Findings for the L1

1. **The Sicoli row is abstract-only.** The Cambridge Core article page answered HTTP 429 on a
   plain request and the JSTOR PDF served an interstitial page that this seat did not route
   around; the abstract was read from the Crossref deposit. The row is filed tier B with its
   scope saying so, and the Chinantec repair claim in the entry is carried by that row plus
   row 6's field description, never by one alone. If the L1 prefers to drop the row, the
   repair claim must move to row 6 alone and lose the abstract's exact wording.
2. **Row 5 may be mergeable with a Finnegan row filed elsewhere.** This seat read the 2012
   Open Book Publishers edition of *Oral Literature in Africa* from the Internet Archive
   open-access deposit, because a plain request to the OpenEdition copy of the same chapter
   returned an interstitial page. The corpus already cites "Finnegan (1970)" in
   `music-instrument-lexicon.md:4`; the 2012 OBP book is the reissue of that work, so one row
   can carry both citations if the L1 prefers one row per work.
3. **No surrogate channel is measured in bits per second in this seat's set.** The entry
   therefore states the spoken-language rate as a yardstick and the whistle's loss in
   information terms, with no surrogate rate asserted. If another seat holds a measured
   surrogate rate, §6 line 14 can take it; if not, the entry must keep the present wording.
4. **Duplicate-check with the head scribe.** The head scribe's list and this seat's list do not
   overlap; the two caveats about Finnegan and about the abstract-only Sicoli row were sent to
   `ScribeHeadScope` before this report was written.
5. **Gate locators, against routed defect 3** (`corpus/lessons/round-51-verifier-spotcheck.md:125`):
   every locator in this seat's eight Gate lines names a heading or a paragraph that exists in
   the fetched copy — "Abstract", "Results, paragraph on IR and SR", "Introduction, paragraph
   on the whistle as a robust channel", "Enphrasing", "Human Whistled Speech Acoustic
   Structure: Encoding and Perception", "ch. 17 §I". The one indirect locator is the row-2
   abstract, which names the Crossref record's `abstract` field because the article body was
   not opened.
6. **Sicoli 2016: one row per work, and the two seats agree on which to keep.** This seat and
   `ScribeSec04Whistled` independently took the same route: JSTOR served a "Client Challenge"
   gate that neither seat routed around, and both then opened the same article's
   publisher-deposited abstract through the public Crossref record
   (https://api.crossref.org/works/10.1353/lan.2016.0028, HTTP 200). The sibling seat has
   updated its report accordingly and its draft row `NEW-ScribeSec04Whistled-11` is the same
   work by the same route; keep this seat's `NEW-ScribeSec07Encoding-2` and fold the other in
   rather than filing both. The row is tier B, scoped as the publisher's abstract only, and the
   lane already has precedent for Crossref abstracts (S040's anchor is "abstract (Crossref
   record)"). My section leans on the row for one clause — that in San Pedro Sochiapam Chinantec
   the open repair format is favoured over the restricted one, which Sicoli attributes to a
   reduced semiotic carrying capacity of the whistled channel — paired with James 2021 (row 6)
   for the field description; if the L1 drops the row, that clause must be re-sourced rather
   than kept. Finnegan is the same situation: the 2012 Open Book Publishers reissue of the work
   cited in-corpus as "Finnegan (1970)", and the sibling seat holds no competing row for it.
7. **Carrington's own 1949 book was not opened, and could not be.** The two Internet Archive
   copies of *Talking Drums of Africa* (`talkingdrumsofaf00carr`, 1969, and
   `talkingdrumsofaf0000pric`, 1973) both report `access-restricted-item: true` with the PDF
   and full-text files marked private, so reaching them needs an account or a loan — an access
   control, which QUALITY criterion 10 forbids. The Kele stock-phrase evidence in §6 therefore
   comes from Finnegan's open-access chapter (row 5), which quotes Carrington 1949a with page
   references, and the enphrasing rule itself comes from the modern primary article (row 1).
   Carrington's own wording is not cited anywhere in the section.

## Unrun checks and limits

- No file in the lane was created or edited except this report. The C entry was not written, so
  the section text was not pasted, and no head, heading, README, SOURCES, lesson or access
  check was run against a landed file.
- The section cites no S-id below S134 (only this seat's `NEW-ScribeSec07Encoding-n` draft ids,
  which the L1 replaces) and no `corpus/lessons/round-52.md` path. It does not cite
  `corpus/knowledge/linguistics/sign-languages-manual-modality.md` at all, so no line changed
  by claim D is touched.
- No `§N` cross-reference is used in the section, so the entry's heading-number rule cannot be
  broken by it.
- The sibling sections were not available at drafting time. The section number 6 and the
  numbering assumed for the neighbours (3 typology, 4 whistled speech, 5 drummed speech, 7
  ecology and function, 10 decision table) follow the wave context and the sibling seat titles;
  if a sibling renumbers, this section needs no edit, since it makes no `§N` reference.
- The four in-corpus `civilizations/` anchors (four lines in three files) were re-read at the
  lane worktree at HEAD `5b7ecfb` on 2026-10-22; none of them is quoted verbatim in the
  section, only paraphrased and pointed at.
- The Finnegan chapter's printed page numbers are not recoverable from the archive's
  full-text file, so the row anchors to chapter, section and paragraph rather than to a page.
- Wikipedia was not opened and is not cited; no tier C row supports any claim here.
- The worked stock phrases in the entry are the Kele examples as Finnegan prints them, with
  their community named; no invented Kele phrase is presented as attested.

## Touched surfaces and out-of-scope items

- **Written:** `.ufo/waves/round-52/build/ScribeSec07Encoding.md` (this report) — the only file
  this seat created. Lane HEAD at drafting time was `5b7ecfb`; `git status` shows the corpus
  tree untouched by this seat.
- **Not written, by design:** the C entry `corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md`
  (does not exist yet), `corpus/SOURCES.md` (the L1 appends the rows and assigns the S-ids),
  `corpus/README.md`, `corpus/lessons/round-52.md` and the sign-language entry. No product,
  registry, index or lesson file was edited, staged or committed.
- **Out of scope for this seat:** the entry's eight-field head, §13 Recheck, §14 Scope (owned by
  `ScribeHeadScope`), the boundary table (§2), the typology (§3), the per-channel sections
  (§4, §5), the ecology and social sections (§7–§9), the decision table and build order (§10),
  the worked example (§11) and the calibration bank (§12). The frontier step — the one mined
  mistake and the routed defects at `corpus/lessons/round-51-verifier-spotcheck.md:121-129` —
  belongs to the L1; this seat contributes to it only through its Gate lines and through
  finding 5 above, which answers routed defect 3 for its own rows.

## Tooling record

No installs and no updates. The work used the system `python3` (standard library only), the
`read` tool, `curl` and the already-present `pdftotext` from poppler. Nothing was installed,
upgraded or downgraded; no host service was restarted; no pacman transaction was run.

## Notes for the L1

1. Section text above is ready to paste; the line-count note gives both readings of the
   15-line budget.
2. Seven frontier rows, ids `NEW-ScribeSec07Encoding-1` … `-7`, with the nine Gate lines
   above; all seven carry `status = mined`, `opened = 2026-10-22`, `recheck = 365d` and
   `used-by = corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md`. Row 2 is the
   same work and route as `NEW-ScribeSec04Whistled-11` in the sibling §4 report: keep one row
   for Sicoli 2016 and renumber the other seat's draft id out.
3. All seven rows were opened by ordinary means: PMC full text (rows 1, 3, 4), the Internet
   Archive open-access deposit of the CC-BY book (row 5), the Crossref deposit (row 2), and
   the Frontiers full text (rows 6, 7). No headless browser, no challenge, no login: QUALITY
   criterion 10 holds for all seven.
4. The `NEW-ScribeSec07Encoding-n` tokens in the section text must be replaced with the
   assigned S-ids before landing, since the C acceptance checks every `S###` token in the
   entry against `corpus/SOURCES.md`.
