# ScribeSec01Register — Claim C, section `## 1. The register property: gesture is part of the utterance`

Seat: `KotodamaR53.ScribeSec01Register` (scribe, leaf; no delegation, no background jobs).
Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, branch `main`, jj-colocated. Read-only everywhere: no file in the lane was edited except this report.
Round 53, attempt 1, hyaku phase 3, 2026-10-22. Claim **C** (coverage): the new entry `corpus/knowledge/linguistics/gesture-co-speech-pointing.md`.
Base read this session: `find corpus/knowledge -name '*.md' | wc -l` → **228**; `find corpus/knowledge -iname '*gestur*' -o -iname '*pointing*' -o -iname '*kinesic*'` → **0** (gap still fresh at base).

## 0. Axes named, and the moves kept

| axis | state at base | move this seat made |
|---|---|---|
| coverage | no filename owner, no topic owner; four partial owners hold pieces of the ground (§2 of the entry) | opened the three named sources (plus two better primaries), so §1 rests on rows the L1 can register as S187 upward |
| operability | the entry's §1 must separate co-speech gesture from four neighbouring registers without restating them | every table cell carries either a `NEW-<SeatName>-<n>` id or an in-corpus `path:line`; no bare `-N` fragment anywhere in the drafted text (the round-52 defect class) |
| calibration | a designer's map is not a finding | the three-pole map is labelled **H** (heuristic) with each pole tied to an opened row; McNeill 1992's exact continuum wording is left `(to-verify)` because the book text was not opened |

Moves kept: every source was opened by ordinary means (plain request, no browser, no challenge bypass); the Cambridge page was read from a Wayback capture after a plain request returned HTTP 429 (rate limit, not a challenge), and the route is recorded in the row.

## 1. Drafted text — ready to paste into the C entry

Line count: **13 of the 14 lines allowed** (H2 line and blank lines counted).

```markdown
## 1. The register property: gesture is part of the utterance

**Master claim.** Co-speech gesture is produced with speech as one system, not decoration: gesture is "visible bodily action that is seen as intimately involved in the activity of speaking" (NEW-ScribeSec01Register-5), gestures and speech come out of "a single, unitary, project of action" (NEW-ScribeSec01Register-3), speech and gesture are "part and parcel of the same system" (NEW-ScribeSec01Register-2), and the two channels together make composite utterances whose gesture half adds semantic, syntactic, discursive and pragmatic information (NEW-ScribeSec01Register-1); McNeill's answer is to "examine language and gesture together" (NEW-ScribeSec01Register-4), so for a designer the hands belong on the same spec sheet as the words.

| Test | Pass when | Fails as (owner) |
|---|---|---|
| **Produced with the utterance** | the hand, body and face move in visible actions "intentionally used to communicate" and "expressed together with the verbal utterance" (NEW-ScribeSec01Register-1) | a sign language: a full language with its own grammar and community, not speech's accessory (`sign-languages-manual-modality.md:64`, `:161`) |
| **Carries meaning, not decoration** | the gesture adds what the words do not say, or settles which reading the words get (NEW-ScribeSec01Register-1) | body-language wallpaper: a gesture "not perceived as mere incidental accompaniments to the speech channel" (NEW-ScribeSec01Register-1) |
| **Conventionalization is a gradient** | forms turn conventional where pointing, interaction regulation and pragmatic work are done, and a fully conventionalized gesture can stand in for a word (NEW-ScribeSec01Register-3) | an emblem with a dictionary gloss and a fixed etiquette (`adornment-body-codes.md:79`) |
| **Not posture** | the movement is part of what is being said and is timed to the utterance (NEW-ScribeSec01Register-1, NEW-ScribeSec01Register-3) | a posture or bow gradient keyed to rank and seniority (`adornment-body-codes.md:80`) |
| **Not a counting system** | the hand shapes what is being said, as a Neapolitan speaker holds up four fingers while saying "per quattro persone" (NEW-ScribeSec01Register-3) | finger counting as a patterned counting technology, with its own digits and direction (`numerals-and-measures.md:107`) |

Designer's map (**H** — a heuristic, not a law): one conventionalization line, from co-speech gesture at the speech end, through emblems whose gloss a word can replace (the Neapolitan "piccole" gesture is one) (NEW-ScribeSec01Register-3), to sign languages at the far end (NEW-ScribeSec01Register-1; `sign-languages-manual-modality.md:64`); decide per form how conventional it is, whether a word replaces it, and who may use it, because the typical failure is a world whose gesture is either body-language wallpaper or a second full language, with nothing in between.
```

Notes for the integrator:

- `NEW-ScribeSec01Register-1` … `-5` are draft ids only. They must be replaced by the S-ids the L1 assigns (S187 upward) before landing; `reports/round-53/accept-c.py` reads the entry's S-ids, and a leftover `NEW-` string leaves the entry with no S-id at all (SIDS leg: "no S-id cited"). No bare `, -N` fragment appears in the drafted text.
- The closing line is the only place where the designer's map is stated, and it is labelled **H** per `corpus/knowledge/verification/calibration-registry.md:35-39`; the three poles each carry an opened row.
- The `(to-verify)` the L1 may want: the wording of a named "Kendon's continuum" (gesticulation, emblems, sign languages) in McNeill 1992 chapter 2, "Conventions, Gestures, and Signs" (the chapter title is confirmed on the opened publisher page, `press.uchicago.edu` table of contents). The book's text was not opened, so the drafted line does not attribute that phrase to Kendon or McNeill; it is presented as the lane's own map with the poles sourced. If the L1 wants the continuum named, it needs a page that states it.
- Nothing here restates a partial owner. `adornment-body-codes.md:79` (emblem taxonomy), `:80` (posture and bow gradients), `sign-languages-manual-modality.md:64` and `:161`, `numerals-and-measures.md:107` are cited one way only, as owners. `direction-symbolism.md:6` and `:36` (Guugu Yimithirr pointing) are not needed in §1; they belong to the pointing section.

## 2. In-corpus anchors, re-read at the lane worktree on 2026-10-22

| anchor | what it says |
|---|---|
| `corpus/knowledge/culture-material/adornment-body-codes.md:77` | `## 7. Gesture and posture — engineered gradients and their failure modes` |
| `corpus/knowledge/culture-material/adornment-body-codes.md:79` | `**The toolkit**: Ekman & Friesen (1969) classify nonverbal behavior into *emblems* (culture-specific gestures with dictionary meanings — the conlang-adjacent category), illustrators, affect displays, regulators, adaptors; Morris et al. (1979) mapped emblem…` |
| `corpus/knowledge/culture-material/adornment-body-codes.md:80` | `**Engineered honorific gradients**: Japanese bow degrees … Thai *wai* and Khmer *sampeah* with hand-height levels keyed to relative seniority; the Chinese *kowtow* …` |
| `corpus/knowledge/linguistics/sign-languages-manual-modality.md:64` | `| co-speech gesture (boundary) | speakers, alongside speech (S079) | picked up with the spoken language (design frame, **H**) | every speaker; no community boundary (design frame, **H**) | conveys information but is not conventionalized and systematic the way…` |
| `corpus/knowledge/linguistics/sign-languages-manual-modality.md:161` | `Sign is not gesture-code: emblems and proxemics stay at `adornment-body-codes.md:79`; homesign and emerging signs feed syntax-typology debates (`syntax-typology.md:99`) …` |
| `corpus/knowledge/linguistics/numerals-and-measures.md:107` | `- **Finger counting** is culturally patterned, not universal: direction (left-to-right, right-to-left), start finger, whether the thumb is a counter or a folder …` |
| `corpus/knowledge/verification/calibration-registry.md:35-39` | the R / C / B / H / T status codes used for the **H** label |
| `corpus/knowledge/myth-symbol/direction-symbolism.md:6`, `:36` | Guugu Yimithirr absolute directions and Haviland 1993 on pointing gestures (owner of the pointing evidence; not used in §1) |

## 3. Registry row drafts (for `corpus/SOURCES.md`)

Column order as `corpus/SOURCES.md`: `| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |`. The `id` cells below are the seat's draft ids; the L1 assigns S187 upward at integration, in the order the entry first cites them (1 → S187, 2 → S188, 3 → S189, 4 → S190, 5 → S191 if it keeps this order). `used-by` is repo-relative and must contain the entry path for `accept-c.py`'s SIDS leg.

```markdown
| NEW-ScribeSec01Register-1 | Özyürek, Aslı 2014, "Hearing and seeing meaning in speech and gesture: insights from brain and behaviour", Phil. Trans. R. Soc. B 369(1651):20130296, doi 10.1098/rstb.2013.0296 — https://pmc.ncbi.nlm.nih.gov/articles/PMC4123675/ | paper | A | how co-speech gesture and speech are processed as one semantic system, and the definition of gesture Kendon gives there | §1 Introduction, the paragraph beginning "Since the 1960s and 1970s", the sentence that attributes a definition to Kendon: "defines gestures as visible actions of the hand, body and face that are intentionally used to communicate and are expressed together with the verbal utterance"; the next paragraph, on what gesture adds: "co-speech gestures contribute semantic, syntactic, discursive and pragmatic information to the verbal part of an utterance, forming composite utterances with semiotic diversity"; §5 Summary, first sentences of the closing paragraph: "not perceived as mere incidental accompaniments to the speech channel" | gesture and speech are one message with two channels; iconic gesture carries meaning as a whole, not as separate segments; gesture and speech form composite utterances whose halves are integrated, not adjacent | mined | 2026-10-22 | 365d | corpus/knowledge/linguistics/gesture-co-speech-pointing.md |
| NEW-ScribeSec01Register-2 | Vigliocco, Gabriella, Pamela Perniss and David Vinson 2014, "Language as a multimodal phenomenon: implications for language learning, processing and evolution", Phil. Trans. R. Soc. B 369(1651):20130292, doi 10.1098/rstb.2013.0292 — https://pmc.ncbi.nlm.nih.gov/articles/PMC4123671/ | paper | A | the theme-issue case that speech and gesture are one integrated system, and that gesture form follows the typology of the speech it accompanies | §1(a) "Narrow-lens view of language 1: language as speech/text", the paragraph beginning "Regarding processing": "there is evidence from both production and comprehension that co-speech gestures are tightly integrated with speech, such that the form of gestures is influenced by the typological structure of the accompanying speech"; and the next sentence: "speech and gesture are part and parcel of the same system and together constitute a tightly integrated processing unit" | a designed language's gesture must be specified against its speech typology: the gesture's form follows the language's structure, not a generic human habit | mined | 2026-10-22 | 365d | corpus/knowledge/linguistics/gesture-co-speech-pointing.md |
| NEW-ScribeSec01Register-3 | Kendon, Adam 2009, "Kinesic Components of Multimodal Utterances", Berkeley Linguistics Society 35(2), doi 10.3765/bls.v35i2.3510 — https://journals.linguisticsociety.org/proceedings/index.php/BLS/article/download/3510/3295/4385 | paper | A | how manual actions enter utterance construction, which jobs they do, and where gesture forms become conventional | §3 "The Lessons of the Three Examples", first paragraph: "Gestures and speech are produced together as products of a single, unitary, project of action."; §1, the paragraph on convention and the four uses of gesture (it ends "This division into four uses of gesture is not, I should emphasize, intended as a typology of gesture."): "Especially when gestures are used for pointing, interaction regulation and pragmatic purposes, we find there a tendency for forms to be conventionalized."; §1, the sentence on emblem vocabularies: "an analysis of what they are reputed to mean shows a preponderance of interaction regulation and pragmatic functions"; §2.1, on the Neapolitan "piccole" gesture: "Sometimes these kinesic schematic actions can be fully conventionalized and semantically equivalent to spoken words."; §2.3, on the numeral: "holding his hand up displaying four fingers as he does so" | gesture and speech are produced together as one action; gesture does several distinct jobs (description, diagram, pragmatic act, pointing, interaction regulation) and Kendon declines to make them a typology; convention grows where pointing, interaction regulation and pragmatic work are done; a fully conventionalized gesture can be equivalent to a spoken word | mined | 2026-10-22 | 365d | corpus/knowledge/linguistics/gesture-co-speech-pointing.md |
| NEW-ScribeSec01Register-4 | McNeill, David 1992, "Hand and Mind: What Gestures Reveal about Thought", University of Chicago Press — https://press.uchicago.edu/ucp/books/book/chicago/H/bo3641188.html | docs | B | the book's own case for examining language and gesture together, and the chapter that works out the conventional categories; only the publisher's description and table of contents were opened, not the 1992 text | Book description: "gestures do not simply form a part of what is said and meant but have an impact on thought itself"; and "we must examine language and gesture together to unveil the operations of the mind"; Table of Contents, Part 1 item 2: "Conventions, Gestures, and Signs"; page facts: "423 pages" and "© 1995" | the founding statement of the speech–gesture unity thesis, and the pointer to the chapter where the conventional categories are set out; tier B because the page is a publisher description, not the book | mined | 2026-10-22 | 365d | corpus/knowledge/linguistics/gesture-co-speech-pointing.md |
| NEW-ScribeSec01Register-5 | Kendon, Adam 2004, "Gesture: Visible Action as Utterance", Cambridge University Press, DOI 10.1017/CBO9780511807572, "412 Pages" — https://www.cambridge.org/core/books/gesture/8D13E32E474A10800DAAC09DE6CF320D (read via Wayback capture 20261001143908; a plain request on 2026-10-22 returned HTTP 429) | docs | B | the publisher's own summary of the 2004 study: gesture as visible action intimately involved in speaking, its role in utterance construction, the gesture–sign-language relation, and variation by culture and language | Book description: "Gesture, or visible bodily action that is seen as intimately involved in the activity of speaking"; and "drawing on the analysis of everyday conversations to demonstrate its varied role in the construction of utterances"; and "exploring the relationship between gesture and sign language, and how the use of gesture varies according to cultural and language differences" | the reference frame the 2004 book set — gesture is part of speaking, varies by culture and language, and stands in a relation with sign language; tier B because only the publisher's description and contents were opened | mined | 2026-10-22 | 365d | corpus/knowledge/linguistics/gesture-co-speech-pointing.md |
```

Tier notes: rows 1, 2 and 3 are primary, full-text, open copies of the papers themselves (tier A for their scope). Rows 4 and 5 are publisher descriptions of books whose text was not opened (tier B under QUALITY criterion 6, which makes a publisher description B for claims about the work).

## 4. Gate lines (for `corpus/lessons/round-53.md`, `## Gate`)

Format copied from `corpus/lessons/round-52.md:25` onward: `- <id> — <URL> — accessed 2026-10-22 — <locator>: "<quote>". Grounds: <one line>. Seat: ScribeSec01Register.`

```markdown
- NEW-ScribeSec01Register-1 — https://pmc.ncbi.nlm.nih.gov/articles/PMC4123675/ — accessed 2026-10-22 — §1 Introduction, the paragraph on Kendon's definition: "visible actions of the hand, body and face that are intentionally used to communicate and are expressed together with the verbal utterance". Grounds: the master claim — gesture is produced with the utterance, not beside it. Seat: ScribeSec01Register.
- NEW-ScribeSec01Register-1 — https://pmc.ncbi.nlm.nih.gov/articles/PMC4123675/ — accessed 2026-10-22 — §1 Introduction, the paragraph beginning "Thus, there has been mounting evidence": "co-speech gestures contribute semantic, syntactic, discursive and pragmatic information to the verbal part of an utterance, forming composite utterances with semiotic diversity". Grounds: the row "Carries meaning, not decoration" — what the gesture half adds. Seat: ScribeSec01Register.
- NEW-ScribeSec01Register-1 — https://pmc.ncbi.nlm.nih.gov/articles/PMC4123675/ — accessed 2026-10-22 — §5 Summary and conclusion, the paragraph on iconic gestures: "not perceived as mere incidental accompaniments to the speech channel". Grounds: the fails-as cell of the "Carries meaning, not decoration" row. Seat: ScribeSec01Register.
- NEW-ScribeSec01Register-2 — https://pmc.ncbi.nlm.nih.gov/articles/PMC4123671/ — accessed 2026-10-22 — §1(a), the paragraph beginning "Regarding processing": "speech and gesture are part and parcel of the same system and together constitute a tightly integrated processing unit". Grounds: the master claim — one system, not two channels. Seat: ScribeSec01Register.
- NEW-ScribeSec01Register-3 — https://journals.linguisticsociety.org/proceedings/index.php/BLS/article/download/3510/3295/4385 — accessed 2026-10-22 — §3 "The Lessons of the Three Examples", first paragraph: "Gestures and speech are produced together as products of a single, unitary, project of action". Grounds: the master claim and the "Not posture" row. Seat: ScribeSec01Register.
- NEW-ScribeSec01Register-3 — https://journals.linguisticsociety.org/proceedings/index.php/BLS/article/download/3510/3295/4385 — accessed 2026-10-22 — §1, the paragraph on convention and the four uses of gesture (it ends "This division into four uses of gesture is not, I should emphasize, intended as a typology of gesture."): "Especially when gestures are used for pointing, interaction regulation and pragmatic purposes, we find there a tendency for forms to be conventionalized". Grounds: the "Conventionalization is a gradient" row and the designer's map. Seat: ScribeSec01Register.
- NEW-ScribeSec01Register-3 — https://journals.linguisticsociety.org/proceedings/index.php/BLS/article/download/3510/3295/4385 — accessed 2026-10-22 — §2.3, Example 3, the numeral: "holding his hand up displaying four fingers as he does so". Grounds: the "Not a counting system" row and the pointing hand-shape case. Seat: ScribeSec01Register.
- NEW-ScribeSec01Register-4 — https://press.uchicago.edu/ucp/books/book/chicago/H/bo3641188.html — accessed 2026-10-22 — Book description: "we must examine language and gesture together to unveil the operations of the mind". Grounds: the master claim's design reading. Seat: ScribeSec01Register.
- NEW-ScribeSec01Register-5 — https://www.cambridge.org/core/books/gesture/8D13E32E474A10800DAAC09DE6CF320D — accessed 2026-10-22 (content read via Wayback capture 20261001143908; the plain request returned HTTP 429) — Book description: "Gesture, or visible bodily action that is seen as intimately involved in the activity of speaking". Grounds: the master claim's opening clause. Seat: ScribeSec01Register.
```

## 5. What was opened, and how (ordinary means only)

| source | route | access date | result |
|---|---|---|---|
| Özyürek 2014, Phil. Trans. R. Soc. B 369(1651):20130296 | direct, `https://pmc.ncbi.nlm.nih.gov/articles/PMC4123675/` | 2026-10-22 | opened, full text |
| Vigliocco, Perniss & Vinson 2014, same issue | direct, `https://pmc.ncbi.nlm.nih.gov/articles/PMC4123671/` | 2026-10-22 | opened, full text |
| Kendon 2009, BLS 35(2) | direct, `https://journals.linguisticsociety.org/proceedings/index.php/BLS/article/download/3510/3295/4385` (LSA proceedings PDF) | 2026-10-22 | opened, full text |
| McNeill 1992, University of Chicago Press | direct, `https://press.uchicago.edu/ucp/books/book/chicago/H/bo3641188.html` | 2026-10-22 | opened: book description, table of contents, page facts (not the book text) |
| Kendon 2004, Cambridge University Press | plain request to `https://www.cambridge.org/core/books/gesture/8D13E32E474A10800DAAC09DE6CF320D` returned **HTTP 429**; content read from the Wayback capture **20261001143908** | 2026-10-22 | opened via capture; the route is recorded in the row |

No captcha, paywall, login or other access control was met and no tool was used to get past one. The Cambridge 429 is a rate limit, not a challenge. The McNeill 1992 book text and the Kendon 2004 book text were not opened, and no claim rests on them beyond what the opened pages state.

## 6. Result

- Section `## 1.` drafted at 13 of 14 lines, pipe table, master claim in bold, every factual cell carrying a `NEW-` id or an in-corpus `path:line`.
- Five registry rows and nine Gate lines drafted in the lane's formats, with URL, access date, verbatim quote (each ≤ 25 words) and location, and with the route recorded for the one capture.
- All four required separations are present: emblems (`adornment-body-codes.md:79`), sign language (`sign-languages-manual-modality.md:64`, `:161`), posture and bow gradients (`adornment-body-codes.md:80`), finger counting (`numerals-and-measures.md:107`).
- Every draft id is a well-formed `NEW-ScribeSec01Register-<n>`; no bare `-N` or `, -N` fragment exists in the drafted text.

## 7. Unrun checks and limits

- Nothing was landed, staged, committed or written outside this report. `reports/round-53/accept-c.py` was not run (it needs the integrated entry and the S-ids); `reports/round-28/readme/sweep.py` was not run.
- The drafted §1 was not run through the round-50 entry-contract checker (no entry file exists to check).
- The McNeill 1992 continuum wording and the Cambridge chapter list beyond the book description were not verified against the books themselves; the section states only what the opened pages state.
- Row ids are seat drafts; the S-187-upward assignment, the `used-by` cell and the `mined` status are the L1's to write at integration.
- No file in `corpus/`, `reports/`, `tools/` or the fleet repo was edited by this seat.

## 8. Tooling record

No installs or updates. Everything used the system `python3`, `curl` and the lane's own read-only tools already present.
