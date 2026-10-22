# ScribeSec10Build — Claim C, section `## 10. Decision table and build order`

- Seat: KotodamaR53.ScribeSec10Build (leaf; no delegation, no background jobs, no swarms).
- Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, branch `main`, jj-colocated.
- Claim base `a9cf95fe47a82b516f6c2487cb76b89c3a71c493`; prerequisite `9ae5af92f9777cc5268c82372d22df56ad959765`; declaration `60f1d2a3d832b926e37f82b11c67496d131a1431`.
- Axis: coverage. Milestone: round 53, claim C (new entry `corpus/knowledge/linguistics/gesture-co-speech-pointing.md`).
- Nothing was written outside this report file. No entry file, no README edit, no SOURCES row, no git or jj command.

## 1. Result

Section 10 is drafted inside the 24-line budget, with the three required parts: a
`| If your culture… | then its gesture system needs… | and check |` table (6 rows), a numbered
build order of 5 steps, every step ending in `*Artifact: …*`, and a decision record table
`| ID | Decision | Trigger | Failure if skipped |` with `DR-GES-01` … `DR-GES-05`.

Every factual claim in the section carries a source id (`NEW-ScribeSec10Build-1` … `-3`, to be
mapped to S-ids at integration) or an in-corpus `path:line`; the design prescriptions are
marked as the lane's design heuristic (**H**) with the registry anchor.

`DR-GES` is unused in the lane: `grep -rn "DR-GES" corpus reports` → **0** hits (only the
round-53 wave-spec files under `.ufo/waves/round-53/` name the prefix). Existing decision-record
prefixes in `corpus/knowledge` are `DR-AG-…`, `DR-BB-…`, `DR-BS-…`, `DR-SRG-…` and others, so
`DR-GES` is free.

## 2. Drafted section text (paste-ready)

The block below is 24 lines as written, counting the H2 line and every blank line.
Paths are written the way the entry must write them: the C entry sits in
`corpus/knowledge/linguistics/`, so cross-partition anchors carry `../` and same-partition
anchors are bare.

```markdown
## 10. Decision table and build order

| If your culture… | then its gesture system needs… | and check |
|---|---|---|
| frames space absolutely or by landmark — uphill, sunward, riverward | a pointing default that lands in that frame rather than in the speaker's body | §4, §5; `../myth-symbol/direction-symbolism.md:44` (frame table, one-way); the prescriptions in this table are the lane's design heuristic (**H**, `../verification/calibration-registry.md:38`) |
| packages motion in its words | hands that follow that packaging: decide what the language already says in words before deciding what the hands add | §6; NEW-ScribeSec10Build-1 (Turkish, Japanese and English speakers gesture the same cartoon differently) |
| keeps a closed set of ritual or taboo gestures | a quotable repertoire with a taboo list and the institution that backs each taboo | §7, §8; `politeness-taboo-euphemism.md:75`, `:76`; pointing taboos are reported at NEW-ScribeSec10Build-2 |
| ranks people by age, office or standing | posture, distance and gesture size scaled by rank, and a rule for who may gesture to whom | §8; `../culture-material/adornment-body-codes.md:82` (gradient table, one-way) |
| has a manual language of its own | a hard boundary: co-speech gesture and a manual system must not be merged into one register | §3; `sign-languages-manual-modality.md:64` (the boundary row, one-way) |
| marks time on a line or in a spoken convention | a gesture time line set by the same convention the language uses | §5 |

1. Fix the language's frame of reference and its event framing first; the hands follow them. *Artifact: gesture-brief sheet (frame, framing pattern, pointing default).*
2. Choose the pointing form and the gaze rules: the index finger is not the default everywhere (NEW-ScribeSec10Build-3), so write who may point at whom and at what. *Artifact: pointing-and-gaze sheet with the taboo list.*
3. Build the quotable repertoire: every gesture glossed, the domain it covers, and the sanction behind each taboo. *Artifact: quotable-gesture table with glosses.*
4. Set the posture and distance gradients by rank and setting, reusing the emblem toolkit one-way (`../culture-material/adornment-body-codes.md:79`). *Artifact: posture-and-distance gradient table.*
5. Write the learning path and the misread table: infants point before they speak in every culture tested (NEW-ScribeSec10Build-2), so a child, a newcomer and a translator each fail differently. *Artifact: acquisition-and-error table plus one scripted scene.*

| ID | Decision | Trigger | Failure if skipped |
|---|---|---|---|
| DR-GES-01 | Decide what gesture is in this culture: part of the utterance, or a separate manual system | a signed system, a silence rule, or a rite with fixed hand forms | a "universal body language" paste with no boundary — the §3 error |
| DR-GES-02 | Set the frame of reference before choosing a pointing default | the language has uphill, sunward or riverward terms | hands that contradict the culture's own words for place |
| DR-GES-03 | Decide what the language already says in words before the hands repeat it | the conlang has a fixed way of packaging motion | a gesture that repeats the sentence, or contradicts it |
| DR-GES-04 | Fix the audience and the taboo list before the quotable repertoire | the culture forbids pointing at people, at the dead, or with one hand (NEW-ScribeSec10Build-2); a stated taboo means the gesture exists (NEW-ScribeSec10Build-2) | an emblem a reader will read as an insult |
| DR-GES-05 | Write the acquisition path before the repertoire is taught | children and outsiders share the same scenes; infants under a year are said to be exempt from pointing rules, untested (to-verify) | a gesture system only adults can read, and a newcomer who never learns it |
```

Line accounting: 1 H2 + 1 blank + 2 table head/separator + 6 rows + 1 blank + 5 build steps +
1 blank + 2 table head/separator + 5 decision rows = **24**.

Fallback if the integrator counts the blank line that separates §10 from §11 as part of this
section: delete the sixth decision-table row (the time-line row) and move its content into §5;
the block then is 23 lines plus the separator = 24. The 6-row table is inside the required 5–7
band either way; the 5 decision records are inside the required 4–6 band; no `§N` reference
exceeds 14.

## 3. In-corpus anchors, re-read at the lane worktree on 2026-10-22

| Anchor | What the line carries | How §10 uses it |
|---|---|---|
| `corpus/knowledge/myth-symbol/direction-symbolism.md:44` | the frame decision table: `| Frame chosen | What must be true of the world | What breaks if ignored |`, headed by "Decision table (frame → consequences)" at `:42`; the absolute/landmark/relative/mixed frames are described at `:34-40` | pointed to one-way in the first decision row; the frame side of the design stays there |
| `corpus/knowledge/myth-symbol/direction-symbolism.md:36` | "gestures are anchored to the world, not the body (Haviland 1993, 1998; Levinson 1997)" in the absolute-frame bullet | not restated; the row cites the frame table instead |
| `corpus/knowledge/culture-material/adornment-body-codes.md:79` | the toolkit bullet: Ekman and Friesen's emblem category, Morris et al. (1979) on emblem geography, Hall (1966) on proxemic distance bands | pointed to one-way in build step 4 (the emblem toolkit) |
| `corpus/knowledge/culture-material/adornment-body-codes.md:82` | "- **Gradient table**:" followed by the bow/wai/sampeah/kowtow/adoratio/homage gradient rows | pointed to one-way in the rank-and-posture row |
| `corpus/knowledge/linguistics/sign-languages-manual-modality.md:64` | the co-speech gesture (boundary) row: "conveys information but is not conventionalized and systematic the way sign is" | pointed to one-way in the manual-language row; the boundary test stays there |
| `corpus/knowledge/linguistics/politeness-taboo-euphemism.md:75` | the taboo domain inventory (seed 5–8) | pointed to in the taboo row |
| `corpus/knowledge/linguistics/politeness-taboo-euphemism.md:76` | the sanction gradient (supernatural dread → kin/elder ridicule → reputation → legal censor) | pointed to in the taboo row |
| `corpus/knowledge/verification/calibration-registry.md:38` | the `H` code: "Heuristic or interpretive framework, not an established causal law … label the designer's choices instead of presenting a discovery" | the status of the table's prescriptions |

Partial owners named in the wave context and **not** restated: `adornment-body-codes.md:77-93`,
`sign-languages-manual-modality.md:64` and `:161`, `numerals-and-measures.md:107`,
`direction-symbolism.md:6` and `:36`. The `numerals-and-measures.md:107` finger-counting anchor is
not used in this section; it belongs to the §2 one-owner boundary and to §7.

## 4. Sources opened this round by ordinary means

No headless browser, no challenge-solving, no paywall or login bypass. Route for all three:
direct plain request, then `pdftotext` on the downloaded PDF.

| Draft id | Source | Route | Verbatim quote and location |
|---|---|---|---|
| NEW-ScribeSec10Build-1 | Kita, Sotaro; Özyürek, Asli 2003, "What does cross-linguistic variation in semantic coordination of speech and gesture reveal?", *Journal of Memory and Language* 48(1): 16–32 | MPI PuRe copy, https://pure.mpg.de/rest/items/item_60538_2/component/file_60539/content (HTTP 200, 386 738 bytes, 17 pages) | Abstract, printed p. 16: "gestures used to express the same motion events were influenced simultaneously by (1) how features of motion events were expressed in each language". Results, printed p. 22: "the linguistic package for the same information is tighter in English than in Turkish or Japanese due to the difference in the lexicalization pattern". Results, printed p. 22: "English typically encodes Manner in a verb and Trajectory in a preposition or a verb particle". Results, printed p. 23: "Turkish and Japanese speakers were more likely to have Manner Only and Trajectory Only gestures". |
| NEW-ScribeSec10Build-2 | Liszkowski, Ulf; Brown, Penny; Callaghan, Tara; Takada, Akira; de Vos, Conny 2012, "A prelinguistic gestural universal of human communication", *Cognitive Science* 36(4): 698–713 | MPI PuRe copy, https://pure.mpg.de/rest/items/item_762562_18/component/file_1466200/content (HTTP 200, 254 913 bytes, 16 pages) | Abstract, printed p. 698: "by 10–14 months of age, infants and their caregivers pointed in all cultures in the same basic situation with similar frequencies". Discussion, printed p. 708: "Other cultures have been reported to refrain from index-finger pointing (Hewes, 1996), often with regard to specific situations". Discussion, printed p. 708: "all of these taboos are explicitly represented in folk theories of conduct and politeness" — Liszkowski's own inference, not Hewes's finding. Discussion, printed p. 708: "infants under 1 year of age are generally exempted from pointing rules and taboos, although this has not been tested". |
| NEW-ScribeSec10Build-3 | Cooperrider, Kensy; Slotta, James; Núñez, Rafael 2018, "The Preference for Pointing With the Hand Is Not Universal", *Cognitive Science* 42(4): 1375–1390 | author-hosted copy of the published article, https://kensycooperrider.squarespace.com/s/Cooperrider-Slotta-Nunez-2018-The-Preference-for-Pointing-With-the-Hand-Is-Not-Universal.pdf (HTTP 200, 404 723 bytes, 16 pages) | Abstract, printed p. 1: "The Yupno participants used non-manual pointing (nose- and head-pointing) numerically more often than manual pointing". §2.1 Participants, printed p. 4: "The Yupno portion of the study was conducted in the upper Yupno valley of Papua New Guinea, in the village of Gua". |

Field sites behind the seven cultures in NEW-ScribeSec10Build-2 (Table 1, printed pp. 702–703):
Papua New Guinea, Rossel Island (monolingual Yélî Dnye); Indonesia, Bali (multilingual, including
an indigenous sign language); Japan, Kyoto (monolingual Japanese); Peru, Montaro Valley, Central
Highlands (monolingual Spanish); Mexico, Tzeltal Mayans (monolingual Tzeltal); Mexico, Yucatec
Mayans (monolingual Yucatec); Canada, Nova Scotia (monolingual English).

**Attempted and not obtained.** Wilkins 2003, "Why pointing with the index finger is not a
universal", chapter 8 of *Pointing* (Kita ed.) — three ordinary routes, none of which serves the
text: the publisher's Taylor & Francis chapter page answers HTTP 200 but is a thin JavaScript
shell whose only abstract text is a 22-word truncated `meta description` ("This chapter examines
cultural variation in pointing gestures and discusses what this reveals about cross-cultural
differences in the semiotics of pointing. In"); the third-party full-volume PDF at manuals.plus
answers HTTP 403; the Wayback capture of that publisher page,
`https://web.archive.org/web/20210407061407/https://www.taylorfrancis.com/chapters/edit/10.4324/9781410607744-12/pointing-index-finger-universal-sociocultural-semiotic-terms-david-wilkins`,
answers HTTP 200 with no abstract body at all. No access control was solved or bypassed on any of them — these pages simply do not serve
the text — so the chapter is recorded as **unopened** and supports no claim here. An
author-voiced substitute for the same ground exists (Wilkins, Kita and Enfield 2007, *Field
Manual* 10: 89–95, HTTP 200), which ScoutSourceAccess records as a bibliographic-only lead; it
is a lead and not support for a substantive claim, and this section cites neither. The Wiley PDF
for Cooperrider et al. 2018 returned HTTP 403 (challenge met, not passed); the author-hosted copy
above was used instead and is the published text.

## 5. Registry row drafts (ids S187 upward are assigned by the L1 at integration)

Column order per `corpus/SOURCES.md` registry header: `| id | source | kind | tier | scope | anchor |
teaches | status | opened | recheck | used-by |`.

```
| S1xx (L1 assigns; seat draft NEW-ScribeSec10Build-1) | Kita, Sotaro; Özyürek, Asli 2003, "What does cross-linguistic variation in semantic coordination of speech and gesture reveal?", Journal of Memory and Language 48(1): 16–32 — MPI PuRe copy — https://pure.mpg.de/rest/items/item_60538_2/component/file_60539/content | paper | A | how a language's own packaging of motion shapes the gestures of its speakers (English, Japanese, Turkish) | Abstract, printed p. 16; linguistic package and lexicalization, printed p. 22; Rolling Event coding and results, printed p. 23 | the same motion event is gestured differently by speakers of different languages, so a conlang's gesture repertoire follows its speech packaging | mined | 2026-10-22 | 365d | corpus/knowledge/linguistics/gesture-co-speech-pointing.md |
| S1xx (L1 assigns; seat draft NEW-ScribeSec10Build-2) | Liszkowski, Ulf; Brown, Penny; Callaghan, Tara; Takada, Akira; de Vos, Conny 2012, "A prelinguistic gestural universal of human communication", Cognitive Science 36(4): 698–713 — MPI PuRe copy — https://pure.mpg.de/rest/items/item_762562_18/component/file_1466200/content | paper | A | preverbal pointing in infants and caregivers across seven field sites, and the reported exceptions and taboos in adult index-finger pointing | Abstract, printed p. 698; Table 1 field sites, printed pp. 702–703; Discussion on pointing taboos, printed p. 708 | infants and caregivers point by 10–14 months in all seven cultures tested; index-finger pointing has reported exceptions and is subject to taboos such as not pointing at people; Liszkowski infers that a stated taboo presupposes the behaviour exists; infants under one year are said to be exempt from pointing rules (untested) | mined | 2026-10-22 | 365d | corpus/knowledge/linguistics/gesture-co-speech-pointing.md |
| S1xx (L1 assigns; seat draft NEW-ScribeSec10Build-3) | Cooperrider, Kensy; Slotta, James; Núñez, Rafael 2018, "The Preference for Pointing With the Hand Is Not Universal", Cognitive Science 42(4): 1375–1390 — author-hosted copy of the published article — https://kensycooperrider.squarespace.com/s/Cooperrider-Slotta-Nunez-2018-The-Preference-for-Pointing-With-the-Hand-Is-Not-Universal.pdf | paper | A | pointing-form preference in the Yupno of the upper Yupno valley (village of Gua, Papua New Guinea) compared with U.S. undergraduates | Abstract, printed p. 1; §2.1 Participants, printed p. 4 | pointing form is a community preference, not a fixed universal: Yupno participants used nose- and head-pointing more often than manual pointing, U.S. participants used index-finger pointing | mined | 2026-10-22 | 365d | corpus/knowledge/linguistics/gesture-co-speech-pointing.md |
```

Duplicate-URL note for the L1: NEW-ScribeSec10Build-1 (Kita and Özyürek) and
NEW-ScribeSec10Build-2 (Liszkowski et al.) are also named in the briefs of the §6 and §9 seats.
If those seats open the same URLs, keep one row each and merge both seats' quotes, as the
round-52 lesson did for shared URLs. NEW-ScribeSec10Build-3 (Cooperrider et al.) is named in the
§4 seat's brief as well. ScoutSourceAccess reached the same Liszkowski file through the
`item_762562_16` variant of the same `file_1466200` component: one file, one row — the URL in my
row draft is `item_762562_18`, and the two are the same PDF (both HTTP 200, 254 913 bytes).

## 6. Gate line drafts (round-53 lesson `## Gate`)

Format follows `corpus/lessons/round-52.md:37-48`.

```
- S1xx — https://pure.mpg.de/rest/items/item_60538_2/component/file_60539/content — accessed 2026-10-22 — Abstract, printed p. 16: "gestures used to express the same motion events were influenced simultaneously by (1) how features of motion events were expressed in each language". Grounds: the decision-table row on speech packaging — the hands follow the language's own words. Seat: ScribeSec10Build.
- S1xx — https://pure.mpg.de/rest/items/item_60538_2/component/file_60539/content — accessed 2026-10-22 — Results, printed p. 22: "the linguistic package for the same information is tighter in English than in Turkish or Japanese due to the difference in the lexicalization pattern". Grounds: the decision-table row on speech packaging — the language's lexicalization decides the package, and the hands follow it.
- S1xx — https://pure.mpg.de/rest/items/item_60538_2/component/file_60539/content — accessed 2026-10-22 — Results, printed p. 22: "English typically encodes Manner in a verb and Trajectory in a preposition or a verb particle". Grounds: the concrete case behind that row.
- S1xx — https://pure.mpg.de/rest/items/item_60538_2/component/file_60539/content — accessed 2026-10-22 — Results, printed p. 23: "Turkish and Japanese speakers were more likely to have Manner Only and Trajectory Only gestures". Grounds: that the gesture repertoire differs with the language, not only the words.
- S1xx — https://pure.mpg.de/rest/items/item_762562_18/component/file_1466200/content — accessed 2026-10-22 — Abstract, printed p. 698: "by 10–14 months of age, infants and their caregivers pointed in all cultures in the same basic situation with similar frequencies". Grounds: build step 5 and DR-GES-05 — the acquisition path starts with pointing.
- S1xx — https://pure.mpg.de/rest/items/item_762562_18/component/file_1466200/content — accessed 2026-10-22 — Discussion, printed p. 708: "Other cultures have been reported to refrain from index-finger pointing (Hewes, 1996), often with regard to specific situations". Grounds: DR-GES-04 — the taboo list comes before the quotable repertoire.
- S1xx — https://pure.mpg.de/rest/items/item_762562_18/component/file_1466200/content — accessed 2026-10-22 — Discussion, printed p. 708: "all of these taboos are explicitly represented in folk theories of conduct and politeness". Grounds: DR-GES-04 — the inference that a stated taboo presupposes the behaviour exists is Liszkowski's own, so it is carried as his argument, not as Hewes's finding; the design rule it supports is marked **H**.
- S1xx — https://pure.mpg.de/rest/items/item_762562_18/component/file_1466200/content — accessed 2026-10-22 — Discussion, printed p. 708: "infants under 1 year of age are generally exempted from pointing rules and taboos, although this has not been tested". Grounds: DR-GES-05 — the acquisition trigger carries `(to-verify)` because Liszkowski states the exemption is untested.
- S1xx — https://kensycooperrider.squarespace.com/s/Cooperrider-Slotta-Nunez-2018-The-Preference-for-Pointing-With-the-Hand-Is-Not-Universal.pdf — accessed 2026-10-22 — Abstract, printed p. 1: "The Yupno participants used non-manual pointing (nose- and head-pointing) numerically more often than manual pointing". Grounds: build step 2 — the index finger is not the default everywhere.
- S1xx — https://kensycooperrider.squarespace.com/s/Cooperrider-Slotta-Nunez-2018-The-Preference-for-Pointing-With-the-Hand-Is-Not-Universal.pdf — accessed 2026-10-22 — §2.1 Participants, printed p. 4: "The Yupno portion of the study was conducted in the upper Yupno valley of Papua New Guinea, in the village of Gua". Grounds: naming the community and place precisely in the entry.
```

## 7. Out of scope for this seat

Sections 1–9 and 11–14 of the C entry, the eight-field head, the README index row, the SOURCES
rows themselves and the round-53 lesson belong to other seats and to the L1. This seat drafted
only §10, checked the `DR-GES` prefix, and opened three sources for it.

## 8. Unrun checks and limits

- No entry file was created, so none of the lane gates were run against this text:
  `tools/gates/provenance-audit.py`, `reports/round-28/readme/sweep.py`,
  `tools/harness/basename-couples-resolver.py` and `tools/harness/claims-freshness.py` were not
  executed for the C entry. The L1 must run them once the entry exists.
- The 24-line count was checked by script against the pasted block (line count, 6 decision rows,
  5 build steps each ending in `*Artifact: …*`, 5 decision records); the fallback in §2 covers
  the counting disagreement about the separator blank line.
- The quotes were taken from the downloaded PDFs with `pdftotext -layout`; ligatures and
  line-break hyphenation were normalised ("Tra-jectory" → "Trajectory"), and every quoted string
  was checked back against the extracted text line by line.
- Printed pages were re-checked page by page against the PDF (`pdftotext -f N -l N`), because the
  two-column layout misleads a whole-file line count: PDF page 7 is printed p. 22, PDF page 8 is
  printed p. 23. That check moved the packaging quotes from pp. 23–24 to pp. 22–23 and put the
  "linguistic package … lexicalization pattern" sentence on printed p. 22, correcting the
  attribution this seat had first recorded; ScoutSourceAccess flagged the same page and the
  correction was verified independently before it was applied. Method note for the next seat who
  extracts from this file: read the folio from the running head ("22 S. Kita, A. Özyürek / Journal
  of Memory and Language"), and where an even page omits the folio, take it from the neighbouring
  pages — PDF p. 7 = printed 22 and PDF p. 9 = printed 24, so PDF p. 8 is printed 23. The Fig. 5
  Manner–Trajectory Conflating discussion is a separate passage on printed p. 24 and is not
  quoted here.
- The Wilkins 2003 chapter is unopened: the publisher page answers 200 with a 22-word truncated
  metadata abstract, the third-party volume PDF answers 403, and the Wayback capture answers 200
  without the abstract body. No challenge was met or bypassed at the publisher, and no claim in
  §10 depends on the chapter. The Liszkowski paper itself reports the Barai report as
  unevidenced, and that sentence was deliberately not used as a claim.
- The pointing taboos in DR-GES-04 (not pointing at people, not pointing with one hand) rest on
  the Liszkowski et al. 2012 passage I opened, printed p. 708. No Ghana finding is made in this
  section: the abstract-only row for Kita and Essegbey 2001 (*Gesture* 1(1): 73–95, tier B)
  reported by ScoutSourceAccess is not relied on here, and no claim about Ghana appears in §10.
  Access note corrected after the scout's own re-probe and checked here: the Benjamins page is
  not host-dependent — a full desktop user agent with `Accept-Language` gets HTTP 200 on both
  `benjamins.com` and `www.benjamins.com`, while a bare `Mozilla/5.0` gets 403 on both, so a
  reviewer who re-opens that row with a bare user agent will see 403 and must not log it as a
  challenge met.
- No heritage, clinical or legal question is ruled on anywhere in the section; no real community
  is exoticized, and the named communities (Yupno, English-speaking, Japanese, Turkish, Balinese,
  Rossel Island, Tzeltal, Yucatec) appear only as evidence for what a designer must decide.

## 9. Tooling record

No installs and no updates: every tool used was already present — system `python3` (3.x),
`curl`, `pdftotext` and `pdfinfo` (poppler), `grep`, `sed`. All downloads went to `/tmp/ges`
outside the lane and outside the fleet repo; nothing was written in the lane except this report
file.
