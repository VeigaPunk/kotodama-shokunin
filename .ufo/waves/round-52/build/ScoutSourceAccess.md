# ScoutSourceAccess — claim C: which candidate sources open by ordinary means

Seat: KotodamaR52.ScoutSourceAccess (leaf). Round 52, attempt 1, 2026-10-22. Access date on every
row below: **2026-10-22**. Worktree `/home/vgpnk/Projects/shokunin/kotodama-shokunin`. No subagent,
no background job, no install or upgrade. Read-only HTTP only: `curl`/`read` plus public metadata
APIs (Crossref, NCBI eutils, Unpaywall, HAL search, archive.org). No browser, no challenge solved.

## 1. Assigned item

Pre-check access for the ten candidate sources of claim C: for each, try ordinary access, fall back
to a Wayback capture or an open repository copy, and report URL, working route, status code, page
title, and whether full text or only an abstract is readable. Opened-by-me facts only.

## 2. Result in one line

**Six of the ten candidates open in full or at their readable surface** (Seifart via PMC; Meyer 2008
via the author's own site; the Springer book via a Wayback capture; both UNESCO pages live; the
dùndún paper on Frontiers). **One opens only as an abstract** (Güntürkün). **Three do not open at
all** (Stern 1957, Sicoli 2016, Carrington 1949) — for Carrington the nearest open trace is his 1971
*Scientific American* piece, which gives a standfirst and no body. Four further open sources I found
along the way cover C's instrument typology, social control and ambiguity sections better than three
of the listed candidates would.

## 3. The ten assigned candidates

| # | candidate | URL tried | route that worked | status | page title as served | readable |
|---|---|---|---|---|---|---|
| 1 | Seifart et al. 2018, rsos.170354 | `https://royalsocietypublishing.org/doi/10.1098/rsos.170354` | **PMC** `https://pmc.ncbi.nlm.nih.gov/articles/PMC5936885/` (PMCID resolved by NCBI idconv for the DOI) | 403 at the publisher; **200** at PMC | "Reducing language to rhythm: Amazonian Bora drummed language exploits speech rhythm for long-distance communication - PMC" | **full text** (81.5k chars incl. references) |
| 2 | Meyer 2008 JIPA | `https://doi.org/10.1017/S0025100308003277`, Cambridge article slug, Cambridge AOP `content/view/S0025100308003277` | **author's association site**: `http://www.lemondesiffle.free.fr/projet/science/JIPA38.1-Meyer.pdf` | 429 (twice; body "429 Too many automated requests from this network."); Wayback none; **200** PDF 1,632,284 B | "Typology and acoustic strategies of whistled languages: Phonetic comparison and perceptual cues of whistled vowels" | **full text** (26 pp., journal header "Journal of the International Phonetic Association (2008) 38/1", DOI and IPA copyright line on p. 1) |
| 3 | Meyer 2015, Springer "Whistled Languages" | `https://link.springer.com/book/10.1007/978-3-662-45837-2` | **Wayback capture 20260103171227** `https://web.archive.org/web/2025/https://link.springer.com/book/10.1007/978-3-662-45837-2` | live page 200 but 3,036 B "Client Challenge"; capture **200**, 268,706 B | "Whistled Languages: A Worldwide Inquiry on Human Whistled Speech \| Springer Nature Link (formerly SpringerLink)" | **landing page only**: title, author (Julien Meyer), © 2015, "About this book" description and keywords; body text paywalled |
| 4 | Güntürkün et al. 2015, Curr Biol | `http://www.cell.com/article/S0960982215007940/pdf` (Unpaywall's OA link), `https://pubmed.ncbi.nlm.nih.gov/26294179/` | **NCBI eutils efetch**: `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=26294179&retmode=text&rettype=abstract` | cell.com **403**; pubmed HTML page 200 but a 5.5 kB JS shell; **efetch 200** | "Whistled Turkish alters language asymmetries." (Curr Biol 2015 Aug 17;25(16):R706-8) | **abstract only**; PMID 26294179, DOI confirmed, no PMC copy (idconv: "Identifier not found in PMC") |
| 5 | UNESCO ICH, Silbo Gomero | `https://ich.unesco.org/en/RL/whistled-language-of-the-island-of-la-gomera-canary-islands-the-silbo-gomero-00172` | **direct** (no challenge; contrast `corpus/SOURCES.md:91`, S062, whose live page showed a CAPTCHA) | **200**, 155,586 B | "Whistled language of the island of La Gomera (Canary Islands), the Silbo Gomero - UNESCO Intangible Cultural Heritage" | **full description** plus nomination/decision metadata (RL 00172, 4.COM 2009) |
| 6 | UNESCO ICH, whistled language (Türkiye) | `https://ich.unesco.org/en/USL/whistled-language-00658` | **direct** | **200**, 156,003 B | same template, element 00658 | **full description** (USL 00658, 12.COM 2017) incl. the decline paragraph |
| 7 | Stern 1957 | `https://doi.org/10.1525/aa.1957.59.3.02a00030`, then the correct DOI `10.1525/aa.1957.59.3.02a00070` via doi.org, anthrosource, onlinelibrary | none | **403** at doi.org and at both Wiley hosts; Wayback 404 for both slugs; Unpaywall `is_oa: false` | — | **not opened.** See §5: the DOI in the brief is a different article |
| 8 | Sicoli 2016, Language 92(2) | `https://muse.jhu.edu/article/622770`, Cambridge abs page, Cambridge PDF `…/S0097850716002472a.pdf/repair_organization_in_chinantec_whistled_speech.pdf`, `https://doi.org/10.1353/lan.2016.0032` | none | MUSE **200 but a challenge page** ("Project MUSE -- Verification required! … please complete this challenge"); Cambridge **429**; Wayback 404; Unpaywall not OA | "Project MUSE -- Verification required!" | **not opened.** The DOI in the brief is wrong too (see §5) |
| 9 | Carrington 1949 on archive.org | `https://archive.org/details/talkingdrumsofaf00carr`, `https://archive.org/download/…/talkingdrumsofaf00carr_djvu.txt` | partial: item metadata opens; the text does not | metadata **200**; djvu.txt **401** (`access-restricted-item: true`, collections `inlibrary`, `printdisabled`) | "Talking drums of Africa" (1969 print of the 1949 book) | **not readable** (lending/print-disabled). Nearest open Carrington trace: his 1971 *Scientific American* piece, deck only (row 10) |
| 10 | Frontiers in Communication 6:652690 (dùndún) | `https://www.frontiersin.org/articles/10.3389/fcomm.2021.652690/full` | **direct** | **200**, 995,240 B | "Frontiers \| When Music Speaks: An Acoustic Study of the Speech Surrogacy of the Nigerian Dùndún Talking Drum" | **full text** (Abstract, Introduction, Methods, Results, Discussion). Durojaye, Knowles, Patten, Garcia, McBeath; 27 Jul 2021 |

## 4. Additional open sources I opened (these fill C's sections better than 3 of the candidates)

| # | source | URL | status | title | readable |
|---|---|---|---|---|---|
| B1 | James 2021, *Front. Commun.* 6:653268 | `https://www.frontiersin.org/journals/communication/articles/10.3389/fcomm.2021.653268/full` | **200**, 967,901 B | "Systems of Communication: Aspects of Culture and Structure in Speech Surrogates" (Lucas James, Dartmouth; 9 Aug 2021) | **full text**; sections *Defining Speech Surrogacy · Previous Work · Challenges · Compensation Strategies · Constructing a Discourse · Frames, Formulas, and Enphrasing · Discussion*. Covers slit-log drums, ivory/bamboo trumpets, wooden flutes, jaw harps, gongs, Sambla balafon/xylophone, whistled systems, the Morse/alarm-bell exclusion test, and who is forbidden to practise |
| B2 | Meyer, Díaz Reyes, Batchelder-Schwab & Gautheron, "Whistled Languages and Whistled Speech", *International Encyclopedia of Language and Linguistics* (Elsevier) | `http://www.lemondesiffle.free.fr/media/WhistledLanguages_and_Whistled_Speech_Encyclopedy.pdf`; DOI per Crossref `10.1016/B978-0-323-95504-1.00545-7` | **200**, 1,439,365 B | "Whistled Languages and Whistled Speech" (© 2025 Elsevier; Crossref record dated 2026) | **full text**, author-hosted copy; sections incl. *Signal Characteristics and Audibility*, *Diversity of Whistled Languages*, *Phonetics and Phonology*, *Intelligibility*, *Endangered Linguistic Diversity*, *Revitalization* |
| B3 | Meyer & Moore 2021, *Front. Psychol.* 12:674289 | `https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2021.674289/full` | **200** | "A Flute, Musical Bows and Bamboo Clarinets that “Speak” in the Amazon Rainforest; Speech and Music in the Gavião Language of Rondônia" | **full text**; primary study of three Gavião "speaking" instruments (kotiráp flute, iridináp mouth bows, totoráp bamboo clarinets) |
| B4 | Meyer & Gautheron 2006, ELL entry | `http://www.lemondesiffle.free.fr/projet/science/ELL34.pdf` | **200**, 378,454 B | "Whistled Speech and Whistled Languages", *Encyclopedia of Language & Linguistics* 2nd ed., vol. 13, 573–576 | **full text** — but the Elsevier cover page forbids open posting; treat as reading, not as a preferred citation |
| B5 | Jewett 1977, MA thesis, Oregon State | `https://ir.library.oregonstate.edu/downloads/nz8063843` | **200**, 1,613,368 B | "Drum Languages and Their Messages" | **full text**; student work — lead only |
| B6 | Carrington 1971, *Scientific American* 225:90–94 | `https://www.scientificamerican.com/article/the-talking-drums-of-africa/` | **200**, ~3.8 kB of text | "The Talking Drums of Africa \| Scientific American" (Dec 1971) | **teaser only** ("1 min read"); standfirst plus one paragraph |

I also probed Carrington's de Gruyter chapter `10.1515/9783110804423-001` (`https://www.degruyter.com/document/doi/10.1515/9783110804423-001/html`): **HTTP 202, 0 bytes** — a bot wall, not opened.

## 5. Two DOI corrections for the brief

Both are checkable against Crossref, which I queried this session:

- **Stern 1957.** `10.1525/aa.1957.59.3.02a00030` is **White, "A Comparison of Theories on Southern
  Athapaskan Kinship Systems", American Anthropologist 59(3):434–448**. Stern's article is
  **"Drum and Whistle 'Languages': An Analysis of Speech Surrogates", American Anthropologist
  59(3):487–506, DOI `10.1525/aa.1957.59.3.02a00070`**. Searching the brief's DOI for access tests
  tests the wrong paper.
- **Sicoli 2016.** `10.1353/lan.2016.0032` 429s; the article's DOI is **`10.1353/lan.2016.0028`**,
  *Language* 92(2):411–432, "Repair organization in Chinantec whistled speech". It is not open
  (Unpaywall `is_oa: false`) and I found no repository copy.
- Carrington 1949 has no article DOI in Crossref; the archive.org item is the 1969 reprint of the
  book. `10.1093/oxfordjournals.afraf.a093745` is a two-page 1949 *African Affairs* notice under
  author **Jones**, not Carrington — do not cite it as Carrington.

## 6. Quotes ready for row drafting (verbatim, ≤25 words, with location)

| source | verbatim quote | location | supports |
|---|---|---|---|
| Seifart et al. 2018 | "Many drum communication systems around the world transmit information by emulating tonal and rhythmic patterns of spoken languages in sequences of drumbeats." | Abstract, sentence 1 | §5 drummed speech: the register's mechanism |
| Meyer 2008 | "Whistled speech is a complementary natural style of speech to be found in more than thirty languages of the world." | Abstract, sentence 1 | §4 whistled speech: register property and spread |
| Meyer et al. (encyclopedia) | "Whistled languages are secondary speech codes based on whistles anchored to, and derived from, a spoken language" | Abstract, sentence 1 | §1 secondary-code property |
| Meyer et al. (encyclopedia) | "These secondary speech codes are very different from “lexical ideographs” that lack phonetic resemblance to spoken language" | Introduction, ¶2 | §3 signal-code boundary, with Stern 1957 named there as the source of the distinction |
| Meyer 2015 (Springer) | "Whistled speech is adapted to the structure of each language, to specific traditional rural activities such as hunting or shepherding, and to specific ecological milieux." | "About this book", ¶4 | §7 ecology and function |
| Güntürkün et al. 2015 | "Whistled Turkish uses the full lexical and syntactic information of vocal Turkish, and transforms this into whistles" | Abstract, sentence 5 | §9 perception; §4 full-language capacity |
| UNESCO Silbo 00172 | "The whistled language replaces each vowel or consonant with a whistling sound: two distinct whistles replace the five Spanish vowels" | Description, ¶1 | §4/§6 encoding by reduction |
| UNESCO Silbo 00172 | "Taught in schools since 1999, the Silbo Gomero is understood by almost all islanders" | Description, ¶1 (later sentence) | §9 transmission and revival |
| UNESCO Türkiye 00658 | "Whistled language is a method of communication that uses whistling to simulate and articulate words." | Description, ¶1 | §1 register property |
| UNESCO Türkiye 00658 | "One of the key threats to the practice is the use of mobile phones." | Description, ¶2 | §9 decline |
| Durojaye et al. 2021 | "This feature enables the drum to be employed as both a musical instrument and a speech surrogate." | Abstract, sentence 2 | §5 drummed speech; §6 pitch-contour encoding |
| James 2021 | "The practice of speech surrogacy is used for communication across many cultures." | Abstract, sentence 1 | §1 register property |
| James 2021 | "some of the most common being slit-log drums, trumpets of ivory or bamboo, and wooden flutes" | Challenges for Speech Surrogate Communication | §3 all-channel typology |
| James 2021 | "Morse code does not count, as it violates 2) by referring to an alphabet rather than to speech itself" | Defining Speech Surrogacy, ¶2 | §3 signal-code boundary test |
| James 2021 | "There are no attested examples of communities for which surrogate speech is the primary means of verbal communication." | Compensation Strategies…, ¶ opening that sentence | §1 not a primary mode |
| James 2021 | "Participants such as women or children in areas are unwilling or forbidden to practice the system themselves" | Compensation Strategies…, next sentence | §8 who may speak |
| Meyer & Moore 2021 | "The Gavião, a native Amazonian group in Rondônia, Brazil, use three different traditional musical instruments that they identify as “speaking” ones" | Abstract, sentence 1 | §3 instrument-borne speech |
| Carrington 1971 | "In spite of an abundance of tall tales, drum talk is a reality." | standfirst under the title | §5 drummed speech — teaser only, cannot carry a claim |

## 7. Tier and scope recommendations (for the register scribe, not decided here)

- **A**: Seifart et al. (primary research, published version at PMC); Meyer 2008 (published version,
  author-hosted — the same file carries the journal header, DOI and IPA copyright line);
  Durojaye et al. and Meyer & Moore (open-access primary research articles); both UNESCO rows
  (documents, the precedent is `corpus/SOURCES.md:92`, S063, "UNESCO's own inscribed description").
- **B**: Güntürkün et al. — only the abstract opened, and criterion 6 makes abstracts tier B for
  claims about a work (`corpus/QUALITY.md:29`); James 2021 (survey-style argument, opens with a
  definitional review of Sebeok and Stern).
- **B or C — the L1 must rule**: Meyer et al.'s encyclopedia article. Tier B fits the "expert
  write-up … survey" definition (`corpus/SOURCES.md:17-18`), but the usual rule that an encyclopedia
  page is a lead (tier C) would demote it. If it is demoted, §1 and §3's boundary must rest on
  Seifart, James and Stern-speaking-second-hand, and the "(to-verify)" route is cheaper.
- **C only, or drop**: Carrington 1971 (teaser), Jewett 1977 (student thesis), Meyer & Gautheron
  2006 (the Elsevier copy explicitly forbids open posting — a Recheck risk, not an access risk).
- Recheck cadence: 90d for the Frontiers articles and UNESCO entries (living pages, liable to
  revision), 365d for the two published papers, on-release for the encyclopedia article.

## 8. Blocked, with the exact evidence

- **Project MUSE** served a challenge page, not the article: "Verification required! In order to
  better serve you and keep this site secure, please complete this challenge." I did not complete it.
  Sicoli 2016 stays unopened unless a library copy or an author copy surfaces.
- **Cambridge Core** refused the whole host from this network: "429 Too many automated requests from
  this network." Retried twice, 20 s apart, with a normal desktop UA string; unchanged. That blocks
  Meyer 2008, Sicoli 2016 and the Stern-adjacent Cambridge pages alike — hence the author-site route
  for Meyer 2008.
- **HAL** HTML pages and `/document` endpoints return an Anubis proof-of-work page ("Making sure
  you're not a bot!", 12,527 B), which is an access control. I did not solve it and took **no full
  text from HAL**. I did query the documented public HAL search API for metadata (titles, dates, file
  URLs) while looking for a Meyer 2008 copy. Nothing in this report depends on that metadata: the
  Meyer 2008 file came from the author's association site. If the L1 reads even API use as
  circumvention, discard §3 row 2's HAL footnote and the statement stands unchanged.
- **Wiley/AnthroSource** 403 on both Stern slugs, **no Wayback capture** at either
  (`/web/2018/…` and `/web/2025/…` both 404), Unpaywall not OA: Stern 1957 cannot support a claim
  this round. It can appear as an author-year mention with `(to-verify)`, and James 2021 quotes its
  "lexical ideograph" versus "abridgment" distinction second-hand (attributed there to Stern 1957,
  p. 172) if C needs the concept.
- **archive.org** lending items are print-disabled: `talkingdrumsofaf00carr_djvu.txt` returns 401,
  and the Sebeok & Umiker-Sebeok 1976 volumes (`speechsurrogates0000unse_pt.1`, `_pt.2`) are also
  `access-restricted-item: true`.
- **Archive.org's Wayback availability API** rate-limited me (429) after a burst; direct
  `/web/2025/<url>` requests still worked, and that is how the Springer capture was read.

## 9. Unrun checks

- No access check was made from a second network, so the 429s above are one observation, not a
  permanent verdict on Cambridge or MUSE.
- I did not attempt the `tools/check-source-access.py` instrument on these URLs (that is the
  mutation seat's subject); the status codes here are raw `curl` output.
- Nothing installed, nothing upgraded, so no tool entry to record.
