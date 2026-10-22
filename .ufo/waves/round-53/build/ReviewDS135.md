# ReviewDS135: claim D, line-54 falsifier (with line 58)

- Seat: KotodamaR53.ReviewDS135 (reviewer, leaf, no delegation).
- Target: `corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md`, lines 54 and 58 (table rows "Whistled speech, tonal language" and "Reed-pipe and mouth-organ speech").
- Lane head: `60f1d2a3d832b926e37f82b11c67496d131a1431`. Every source was opened on 2026-10-22.
- Worktree state: the entry is modified by a sibling's in-progress repair (8 insertions, 8 deletions, all at lines 105-181: fragments and rows). Lines 54 and 58 are unchanged from HEAD. This report judges that text. Re-check after any edit.
- Recommendation only. I edited no file except this report. Downloads went to `/fast/scratch/hyaku/kotodama-r53/ReviewDS135/`.
- "Carried" below means the cited row's own text states the clause, in substance.

## 1. Result

- **Line 54 does not pass.** Four clauses are absent from S135: "force", "fixed", "Oaxaca" and the three countries. The round-52 over-reads "force fixed formulas" and "(Laos, Thailand, United States) (S135)" are still in the worktree. S135 also drops its own qualifiers ("two level tones"; "to a trained listener"; "high levels of intelligibility").
- **Line 58 does not pass as written.** "seven to eight" is not a qeej fact (S141 says seven). "so this is encoding, not abridging" is Catlin (1982)'s argument, relayed by S140, stated here as settled. "the repertoire is fixed and learned by rote" is S140's sentence about the funeral repertoire, widened to all of it. S135 is cited for a reed-pipe statement it does not contain.
- **Findings count:** 4 high, 5 medium, 6 low (section 6).

## 2. Sources re-opened

| Row | Route | Copy checked |
|---|---|---|
| S135, `http://www.lemondesiffle.free.fr/media/WhistledLanguages_and_Whistled_Speech_Encyclopedy.pdf` | Direct plain request (HTTP 200, application/pdf) | 10-page PDF (qpdf 12.4.2, pdfinfo). Running header matches the PDF page number. Locators below are PDF pages. |
| S141, `https://www.hmongstudiesjournal.org/uploads/4/5/8/7/4587788/hsj-v2n1_morrison.pdf` | Direct plain request (HTTP 200) | 17-page PDF. Locators below are the "Hmong Studies Journal Page N of 17" headers. Paragraph numbers [n] are the article's own. |
| S140, `https://www.lddjournal.org/article/id/2939/` | Direct (article HTML; the PDF galley link returned HTML) | Article text, no page numbers. Located by section (§). |
| S155, `https://api.crossref.org/works/10.1353/lan.2016.0028` | Direct (Crossref record) | 834-character abstract. Article body not opened. |

No bot challenge, paywall or captcha was met.

## 3. What S135 says about Suruí, Chinantec and Hmong

- **Suruí, Hmong and Chinantec (Intelligibility section, p. 7):** "this informational load is much higher in Hmong (seven to eight contour tones, depending on the dialect) than in Suruí (two level tones)."
- Same paragraph, p. 7: "whistled sentences are more formulaic and therefore more predictable"; "high levels of intelligibility can be reached in unpredictable sentences"; "such as Chinantec (for examples see Sicoli (2016))".
- Same paragraph, p. 7, first sentence: "In tonal languages, the possibility of transmitting complex sentences to a trained listener depends on the informational load carried by pitch prosody in the language."
- **Chinantec and Mexico (p. 3):** "speakers of tonal languages which had a whistled register, such as Mazatec or Chinantec", in the sentence that opens "In Mexico, there are records that whistled Spanish developed in populations speaking non tonal languages".
- **Tone and segmental cues (p. 5):** "the whistled pitch largely reproduces the fundamental frequency of the spoken register, including effects from lexical tone"; "basic segmental information is rendered by the amplitude envelope of whistled tonal languages".
- **Hmong and Thailand (p. 5, leaf or flute whistling):** "Hmong (Busnel et al., 1989), and of Akha in Thailand and Hani people in China (Meyer, 2015)". The only Thailand in S135 is Akha's.
- **Signal (p. 2):** "The pitches of whistles are concentrated in a narrow bandwidth" (a general statement about whistles).
- **Search of the full 10-page text:** no "Laos", no "Oaxaca", no Thailand for Hmong. "United States" appears once, in an author affiliation on p. 1: "Boston University, Boston, MA, United States".

S135 names no country for any Hmong whistling and no place for the Chinantec variety.

## 4. Clause audit, line 54

| # | Clause as written | Verdict | Evidence |
|---|---|---|---|
| 1 | Whistled speech, tonal language | carried | S135 p. 5 |
| 2 | Lexical tone carried by whistle pitch | carried | S135 p. 5 |
| 3 | segmental cues in the amplitude envelope | carried | S135 p. 5 |
| 4 | the tonal inventory is the budget | carried in substance | S135 p. 7 "informational load carried by pitch prosody"; "budget" is the entry's metaphor |
| 5 | Same whistle physics | inference | S135 p. 2 gives one signal account for all whistles; no tonal versus non-tonal physics is stated |
| 6 | a rich tone system (Chinantec) allows unpredictable sentences | partly; qualifiers dropped | S135 p. 7 "high levels of intelligibility can be reached", with "to a trained listener" in the sentence before. The example is deferred to Sicoli (2016). S155's abstract covers repair only. |
| 7 | two tones (Suruí) | partly; "level" dropped | S135 p. 7 "Suruí (two level tones)" |
| 8 | force fixed formulas | not carried | S135 p. 7 says "more formulaic and therefore more predictable". Neither "force" nor "fixed" appears. |
| 9 | Chinantec (cited S135) | carried | S135 pp. 3, 4, 7, 9 |
| 10 | (Oaxaca, Mexico): Oaxaca | not in S135; in S155 | S155 abstract: "in San Pedro Sochiapam Chinantec of Oaxaca, Mexico" (one variety only). S155 is not cited on line 54. |
| 11 | (Oaxaca, Mexico): Mexico | carried by context | S135 p. 3 (the sentence above); p. 2 "hotspots found in … Mexico" |
| 12 | Hmong (cited S135) | carried | S135 pp. 5, 7 |
| 13 | Laos (cited S135) | not carried | No match in S135 |
| 14 | Thailand (cited S135) | not carried | S135 p. 5 names Thailand only for Akha |
| 15 | United States (cited S135) | not carried | S135 p. 1, author affiliation only |
| 16 | the country list, cited to S135 | not carried; no row fills it | S141 places Laos, Thailand and the United States with the qeej (a reed pipe), not whistled Hmong. No row in `corpus/SOURCES.md` names a country next to Hmong (checked by search). |
| 17 | hook map at `sound-symbolism.md:121` | resolves | Line 121 is the "music" row (tone-language drum and whistle speech) |
| 18 | Decide how many tones…; detail in §4 | design advice | §4 "Whistled speech" is at entry line 69 |
| 19 | Placement | note | The intelligibility claim sits in the "Typical reach" column (header, line 51), which otherwise holds distances |

## 5. Clause audit, line 58

| # | Clause as written | Verdict | Evidence |
|---|---|---|---|
| 1 | Reed-pipe and mouth-organ speech | carried | S140 §3.5 "a free-reed mouth organ with six bamboo pipes"; S141 p. 1 "a free-reed multiple pipe musical instrument" |
| 2 | Hmong's seven to eight tones | "seven" carried; "to eight" not carried for the qeej | S141 p. 6 [15] "one of seven tones"; S141 p. 16 "The Blue/Green Hmong dialect (Moob Ntsuab) is used throughout." The eight is S135 p. 7, for whistled Hmong, "depending on the dialect". S140 never says "eight". |
| 3 | the vowels are reproducible | carried | S141 p. 6 [15] "Each of these tones can be replicated on the Hmong qeej along with all of the Hmong vowel sounds." |
| 4 | consonants are not | carried | S141 p. 6 [15] "Consonants, however, cannot be pronounced by the qeej." |
| 5 | polyphony blurs the tone-note map | carried, second-hand | S140 §3.5: the qeej "produces polyphonic music by combining a drone tone with other musical notes" and "this obscures direct tone-note correspondences", both as Catlin (1982)'s argument. S141 p. 5 [13]: "a blending of the multiple pipe tones". The same S140 paragraph gives Falk (2004)'s view that the obscured relation "may be beneficial" (omitted). |
| 6 | so this is encoding, not abridging | overread: attribution and scope | S140 §3.5: "Catlin (1982) argues that this obscures direct tone-note correspondences to the extent that the qeej should be considered an encoding rather than abridging phonemic system". S140 §2: "there is a spectrum of how closely a phonemic system emulates the sounds of speech. Thus, I group together both 'abridging' and 'encoding' systems under the heading of 'phonemic' speech surrogates." |
| 7 | the repertoire is fixed and learned by rote | narrowed by S140; S141 supports ritual formulae | S140 §3.5: "This funeral repertoire is fixed and learned by rote, unlike the more creative poetic language used on the ncas."; "However, it should be noted that the qeej is also a popular instrument outside of funeral contexts, such as at New Years festivities." S141 p. 8 [20]: "Young players are taught each song note by note, word by word."; S141 p. 9 [24]: "A player's reputation is based entirely on his ability to recall and play the ritual formulations." |
| 8 | Loud | carried | S140 §3.5 "The qeej is a considerably louder instrument"; S141 makes no loudness claim |
| 9 | public | inference | S140 §3.5 "with no expected verbal interaction from bystanders"; S141 p. 11 "the living community of relatives and friends" |
| 10 | unlike the jaw harp | carried | S140 §3.5 "The sound of the jaw harp is quiet and intimate" |
| 11 | distance (to-verify) | flagged as unverified; no claim | none |
| 12 | Hmong qeej | carried | S140 §3.5; S141 title |
| 13 | Hmong communities (Laos, Thailand, United States) | carried by S141 only | S141 p. 7 [19] "In current times, in Laos and Thailand, interested boys"; pp. 8-9 [22] "there are only two of them living in the United States" and "Hmong men continue to learn the qeej in the United States". S140 names no country. |
| 14 | The pipe speaks ritual text | carried | S141 p. 3 [3] "it is a bamboo voice that intones a highly stylized and ritualistic language"; p. 9 [24] "While the language of the qeej is ritualistic and ceremonial" |
| 15 | not conversation | carried | S140 §3.5 "performance-oriented, as in the Hmong qeej, with no expected verbal interaction from bystanders"; S141 p. 15 [41] "the qeej communicates with the spirit world but does not dialogue with it" |
| 16 | decide who may play it | advice; the facts are carried | S140 §3.5 "Traditionally, only men play the qeej."; S141 p. 5 [13] "the instrument is played now exclusively by men" (except the Hmong in China) |
| 17 | what it addresses | carried | S141 p. 9 [24] "essentially an instrument for communicating with the spirit realm" |
| 18 | (S140; S135; S141) | S135 misdirected | S135 has no qeej statement. Its Hmong content is the whistled tone count (p. 7) and a leaf or flute whistling mention (p. 5). |

## 6. Findings by severity

### High

- **H1 (line 54, countries).** "Hmong (Laos, Thailand, United States) (S135)" has no support in S135. Re-citing it to S141 would attach a reed-pipe fact to the whistle channel. Drop the countries, or cite a row that names a country for whistled Hmong (none found).
- **H2 (line 54, "force fixed formulas").** Still in the worktree. S135 p. 7 says only "more formulaic and therefore more predictable". The round-52 over-read is open at this line, and `reports/round-53/d-count.py` OVER1 and OVER2 will still fire.
- **H3 (line 54, "Oaxaca").** Not in S135. S155's abstract supports it for San Pedro Sochiapam Chinantec only. Either cite S155 on the line and name the variety, or drop "Oaxaca".
- **H4 (line 58, "seven to eight").** The qeej row cites S140, S135 and S141. S141 gives seven (Blue/Green dialect, pp. 6 and 16). The eight comes from S135's whistle-channel dialect range (p. 7). Keep "seven" with S141, or name the dialect range and its own source.

### Medium

- **M1 (line 58, "encoding, not abridging").** This is Catlin (1982)'s argument as relayed by S140 §3.5. S140 §2 treats encoding and abridging as one spectrum under one heading. Attribute the label to Catlin, or state it the way S140 does.
- **M2 (line 58, "the repertoire is fixed and learned by rote").** S140's sentence is about the funeral repertoire, and S140 says the qeej is also used outside funeral contexts. Write "the funeral repertoire" (S140 §3.5), or cite S141 pp. 8-9 for memorized ritual formulae.
- **M3 (line 58, S135 in the citation list).** S135 has no qeej statement. Remove it, or scope it to the whistled-Hmong count ("seven to eight contour tones, depending on the dialect").
- **M4 (line 54, "allows unpredictable sentences").** Drops "to a trained listener" and "high levels of intelligibility" (S135 p. 7). The Chinantec example is S135's deferral to Sicoli (2016), and S155's abstract does not cover sentences.
- **M5 (line 54, "two tones (Suruí)").** S135 says "two level tones" (p. 7). The level versus contour contrast is the point of that passage, so restore "level".

### Low

- **L1** "Same whistle physics" is an inference. Mark it or drop it.
- **L2** "the tonal inventory is the budget" is carried in substance. "Budget" is a metaphor, not a source word.
- **L3** "public" (line 58) is an inference. Mark it.
- **L4** Line 58 omits Falk (2004)'s view, given in the same S140 paragraph, that the obscured relation "may be beneficial". A fair entry would say so.
- **L5** Do not carry the qeej's seven-tone reproduction over to the jaw-harp line (59). Footnote 7 of S140, attached to the ncas paragraph in §2.1, says: "the seven contrastive tones of Hmong are neutralized to four musical notes, corresponding to H6–H9."
- **L6** Placement: line 54's intelligibility claim sits in the "Typical reach" column, which otherwise holds distances.

## 7. Drafted replacement cells (not applied; cite only S135, S140, S141, S155)

Line 54, "Typical reach":

> The whistle signal is the one described for all whistled speech (S135 p. 2). In a tonal language with a rich tone system, a trained listener can reach high intelligibility on unpredictable sentences (Chinantec, S135 p. 7). With few level tones, as in Suruí, sentences tend to be more formulaic and so more predictable (S135 p. 7).

Line 54, "Example language and community":

> Chinantec, San Pedro Sochiapam, Oaxaca, Mexico (variety and place from the S155 abstract; tone claim from S135 p. 7); Suruí, two level tones (S135 p. 7); Hmong, seven to eight contour tones by dialect (S135 p. 7). No country is stated for whistled Hmong in S135.

Line 58, "What is encoded":

> Hmong qeej: seven tones, each replicable, and all the vowels; consonants are not (S141 p. 6); Blue/Green dialect (S141 p. 16). The pipes blend into one voice (S141 p. 5). Catlin (1982), relayed by S140 §3.5, argues that the polyphony obscures direct tone-note correspondence and that the qeej is an encoding rather than abridging system; S140 §2 treats encoding and abridging as a spectrum. The funeral repertoire is fixed and learned by rote (S140 §3.5); young players learn note by note, word by word (S141 p. 8).

Line 58, "Typical reach":

> Considerably louder than the quiet jaw harp (S140 §3.5); played with no expected verbal reply from bystanders (S140 §3.5); offers guidance and solace to the living community at funerals (S141 p. 11); distance (to-verify).

Line 58, "Example language and community":

> Hmong qeej; Laos and Thailand, where boys learn it (S141 p. 7); two master players living in the United States (S141 p. 8); young Hmong men still learning it in the United States (S141 p. 9).

Line 58, "Design consequence" (keeps the advice, fixes the claim):

> The pipe speaks ritual text and does not dialogue with the spirits (S141 pp. 3, 15). Decide who may play it (traditionally only men, S140 §3.5; now exclusively men except the Hmong in China, S141 p. 5) and what it addresses (the spirit realm, S141 p. 9).

## 8. Registry defects (reported, not edited)

- **R1, S135 row** (`corpus/SOURCES.md:164`): locator "PDF pp. 1–2 of 17". The copy opened today has 10 pages. The claims cited to S135 on lines 53-58 sit on pp. 1-8. The "of 17" may come from `file(1)`, which reports 17 pages for this copy while qpdf and pdfinfo report 10 [INFERENCE].
- **R2, S141 row** (`corpus/SOURCES.md:170`): "p. 4 paragraph [13]". Paragraph [13] is on PDF p. 5 of 17, with the "blending" and "exclusively by men" sentences.
- **R3, S140 row** (`corpus/SOURCES.md:169`): the scope lists §2.1, §2.2, §2.3 and §3.5. The "encoding" label first appears in the §2 opening paragraph, with the spectrum caveat, and that is not listed.
- **R4, S155 row** (`corpus/SOURCES.md:184`): used-by names the entry, so SID_BAD would not fire. Its scope is repair only, so it can support the place name, not the sentence claim.

## 9. Residual risk

- S141 is one master player's account (p. 1: "This study is based on oral interviews with Hmong qeej players, focusing on one master qeej player"), 1998, Blue/Green dialect only. Line 58's general wording about "the repertoire" reaches beyond that.
- S140's qeej statements are second-hand from Catlin (1982) and Falk (2004). Neither was opened here.
- The Chinantec example in S135 rests on Sicoli (2016). Its body was not opened; S155 is abstract only.
- No registry row supports any country for whistled Hmong.

## 10. Verification gaps and unrun checks

- Not opened: Catlin (1982), Falk (2004), Busnel et al. (1989), the body of Sicoli (2016).
- Not evaluated: lines other than 54 and 58, including the sibling's in-progress diff at lines 105-181. Other seats cover those.
- Not run: `reports/round-53/d-count.py` and the acceptance scripts (main-agent verification). No build or lint was run.
- Search-based checks, not line-by-line reads: the full S135 text for country names and "Oaxaca"; the full S140 text for "eight", "Laos" and "Thailand" (none); `corpus/SOURCES.md` for Hmong with a country (none).

## 11. Tooling record

No install or update this run. Existing binaries used: curl 8.23.0; pdftotext and pdfinfo (poppler, pdftotext 26.08.0); qpdf 12.4.2. Reads went through the read and grep tools. Note: `file(1)` reported 17 pages for the S135 copy and 10 for the S141 copy, the reverse of qpdf and pdfinfo. I used qpdf and pdfinfo counts.
