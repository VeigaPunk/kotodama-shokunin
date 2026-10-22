# ScoutSourceAccess — C source access pre-check (round 53)

Assigned item: probe the twelve candidate gesture/pointing sources for the C entry by ordinary
means, and report per source the URL that worked, HTTP status, route, full text versus abstract,
and the tier consequence under QUALITY criterion 6. Access date for every row: **2026-10-22**.
No browser, no challenge solving, no login. Nothing in the lane was edited; this file is my only write.

Method: `curl`/`urllib` with a plain desktop user agent, then MPI PuRe REST components, Wayback
captures, author pages and repositories where the publisher refused. OpenAlex and Unpaywall were
queried to find candidate copies only; no claim rests on their metadata.

## 1. Answer table

| # | Work | URL that worked | HTTP | Route | Depth | Tier consequence |
|---|---|---|---|---|---|---|
| 1 | Wilkins 2003, "Why Pointing With the Index Finger Is Not a Universal (in Sociocultural and Semiotic Terms)", in Kita (ed.), *Pointing* | https://www.taylorfrancis.com/chapters/edit/10.4324/9781410607744-12/pointing-index-finger-universal-sociocultural-semiotic-terms-david-wilkins | 200 | direct landing page (Angular shell): the one-sentence abstract exists **only on the live page**, in `meta name="description"`; the Wayback capture 20210407061407 answers 200 with an **empty** description tag and carries the bibliographic block only (imprint Psychology Press, "Pages 46", eBook ISBN 9781410607744) | **metadata plus a one-sentence abstract on the live page; metadata only in the capture** | **tier B, scope = bibliographic identity and the chapter's stated topic only.** Cannot support any content claim. Use the Wilkins, Kita & Enfield 2007 field guide in §4 for the author's own open statement of the thesis |
| 2 | Enfield 2001, "'Lip-pointing': A discussion of form and function with reference to data from Laos", *Gesture* 1(2):185–212 | https://pure.mpg.de/rest/items/item_94885_2/component/file_94884/content | 200 | MPI PuRe REST component (the `pubman/item/.../component/...pdf` form of the same file answers **403**) | **full text**, 27 pp., journal running header present | **tier A** for pages read |
| 3 | Kita & Essegbey 2001, "Pointing left in Ghana", *Gesture* **1(1):73–95** (not 1:2) | https://www.benjamins.com/catalog/gest.1.1.06kit | 200 | direct; **the user agent decides the status, not the host prefix**: a full desktop UA with `Accept-Language` answers 200 three times in a row, a bare `Mozilla/5.0` answers 403 on both `benjamins.com` and `www.benjamins.com`. The abstract is in `og:description` | **abstract only** (full abstract, no body text) | **tier B** per criterion 6. No open full text found: the academia.edu copy answers 403, the Bristol record is metadata only, and the Wayback availability API had no snapshot for the two Benjamins pages I queried early with a bare UA — `gest.1.2.03enf` and `gest.1.2.05kit`, which were guessed DOI variants I never confirmed exist, so their 403 says nothing about the real page. The publisher abstract contains its own typos — "peolple" for people, "anatomically staining position" — so reproduce them verbatim and never silently correct |
| 4 | Cooperrider, Slotta & Núñez 2018, "The Preference for Pointing With the Hand Is Not Universal", *Cognitive Science* 42(4) — the Yupno pointing comparison | https://kensycooperrider.squarespace.com/s/Cooperrider-Slotta-Nunez-2018-The-Preference-for-Pointing-With-the-Hand-Is-Not-Universal.pdf | 200 | author's own site (PDF link listed on kensycooperrider.com) | **full text**, 16 pp., early-view pagination 1–16 | **tier A** for pages read |
| 5 | Núñez & Sweetser 2006, "With the Future Behind Them", *Cognitive Science* 30:401–450 (Aymara) | https://linguistics.berkeley.edu/~sweetser/NunezSweetser2006.pdf | 200 | co-author's university page | **full text**, 50 pp., published pagination | **tier A** |
| 6 | Núñez, Cooperrider, Doan & Wassmann 2012, "Contours of time", *Cognition* 124(1):25–35 (Yupno time) | https://pages.ucsd.edu/~rnunez/COGS155_Readings/YupnoTime.pdf | 200 | first author's UCSD page | **full text**, 11 pp., published pagination | **tier A** |
| 7 | Kita & Özyürek 2003, *JML* 48(1):16–32 | https://pure.mpg.de/rest/items/item_60538_2/component/file_60539/content | 200 | MPI PuRe REST component — the **published** Elsevier PDF (17 pp., printed pp. 16–32 in the running heads) | **full text**, printed pagination | **tier A**; quotes may carry printed pages. Fallback if the PuRe item moves: the Warwick WRAP accepted manuscript, `wrap.warwick.ac.uk/66232/...pdf` (200, 56 pp.), which must then be anchored by manuscript page |
| 8 | Kita 2009, "Cross-cultural variation of speech-accompanying gesture: A review", *LCP* 24(2):145–167 | http://wrap.warwick.ac.uk/66214/2/WRAP_Kita_culture_and_gestue_LCP_v13-distr%20%281%29.pdf | 200 | WRAP | **full text**, 41 pp., **accepted manuscript** | **tier A** for content, same version caveat |
| 9 | Liszkowski, Brown, Callaghan, Takada & de Vos 2012, *Cognitive Science* 36(4):698–713 | https://pure.mpg.de/rest/items/item_762562_16/component/file_1466200/content | 200 | MPI PuRe REST component | **full text**, 16 pp., published pagination | **tier A** |
| 10 | Özyürek 2014, "Hearing and seeing meaning in speech and gesture", *Phil. Trans. R. Soc. B* 369(1651):20130296 | https://pmc.ncbi.nlm.nih.gov/articles/PMC4123675/ | 200 | PubMed Central; the Royal Society PDF and `rstb` landing page both answer **403** | **full text** (abstract, sections, references) | **tier A** |
| 11 | Brookes 2004, "A Repertoire of South African Quotable Gestures", *JLA* 14(2):186–224 | https://linguisticanthropology.org/journal/web-enhanced-articles/web-enhanced-article-a-repertoire-of-south-african-quotable-gestures/ | 200 | Society for Linguistic Anthropology web-enhanced article page | **abstract plus part of the paper's own gesture dictionary**: the served page carries the abstract and the dictionary's A–B entries (the A–Z index is present; entries stop at "burn") | **tier A scoped to the dictionary entries actually printed** (journal-published companion to the article); **tier B** for the article's argument, via its abstract. No OA full text: Unpaywall `is_oa=false`, Wiley PDF 403, no Wayback snapshot of the Wiley PDF |
| 12 | Levinson 1997, "Language and Cognition: The Cognitive Consequences of Spatial Description in Guugu Yimithirr", *JLA* 7(1):98–131 | https://pure.mpg.de/rest/items/item_66622_3/component/file_66623/content | 200 | MPI PuRe REST component; the publisher **published** article, 34 pp., printed folios 98–131 in the running heads | **full text**, printed pagination | **tier A**; quotes carry printed pages (pdf p. 2 = p. 99, pdf p. 28 = p. 125, pdf p. 34 = p. 131). An earlier revision of this table called it a folio-less typescript — that was my misread of the opening page, which carries the MPI header line instead of a folio |

Net: **nine of the twelve have an open full text (tier A for the pages read)**. Brookes 2004 is tier A
only for the dictionary entries the journal page prints and tier B for the article's argument;
Kita & Essegbey 2001 is tier B (publisher abstract); Wilkins 2003 is bibliographic only. Nothing was
reached through an access control, so no row needs the criterion-10 note.

## 2. Verified quotes, verbatim, with the location I actually saw

These are copy-checked against the fetched bytes; each is at most 25 words. Use them as the anchor
cell content, and do not extend a quote past the words below without re-opening the file.

| # | Location | Quote |
|---|---|---|
| 2 | Enfield 2001, p. 185 (abstract, PDF p. 1) | "‘Lip-pointing’ is a widespread but little-documented form of deictic gesture, which may involve not just protruding one or both lips" |
| 2 | Enfield 2001, p. 185 (abstract, PDF p. 1) | "the ‘vector’ of lip-pointing is in fact defined by gaze" |
| 3 | Kita & Essegbey 2001, publisher abstract (`og:description`) | "First, there is a politeness convention to place the left hand on the lower back, as if to hide it from the interlocutor." |
| 4 | Cooperrider, Slotta & Núñez 2018, p. 1 (abstract) | "The Yupno participants used non-manual pointing (nose- and head-pointing) numerically more often than manual pointing" |
| 5 | Núñez & Sweetser 2006, p. 401 (abstract) | "The Aymara language instead has a major static model of time wherein FUTURE IS BEHIND EGO and PAST IS IN FRONT OF EGO" |
| 6 | Núñez et al. 2012, p. 25 (abstract) | "the past is construed as downhill, the present as co-located with the speaker, and the future as uphill" |
| 7 | Kita & Özyürek 2003, p. 16 (abstract) | "Gestures that spontaneously accompany speech convey information coordinated with the concurrent speech." |
| 7 | Kita & Özyürek 2003, p. 16 (abstract) | "Narratives in Turkish, Japanese, and English were elicited using an animated cartoon as the stimulus." |
| 7 | Kita & Özyürek 2003, p. 22 (Rolling Scene) | "the linguistic package for the same information is tighter in English than in Turkish or Japanese" |
| 8 | Kita 2009, accepted ms p. 3 (abstract) | "This article reviews the literature on cross-cultural variation of gestures. Four factors governing the variation were identified." |
| 9 | Liszkowski et al. 2012, p. 698 (abstract) | "The current study provides evidence for the universality of a prelinguistic gestural basis for human communication." |
| 9 | Liszkowski et al. 2012, p. 698 (abstract) | "caregivers pointed in all cultures in the same basic situation with similar frequencies and the same proto-typical morphology of the extended index finger" |
| 10 | Özyürek 2014, Abstract ¶1 | "we use not only the arbitrary form–meaning mappings of the speech channel but also motivated form–meaning correspondences, i.e. iconic gestures" |
| 11 | Brookes 2004, journal abstract (SLA page) | "Quotable gestures fall within three main gestural types: lexical, holophrastic, and concept, with lexical gestures constituting the highest proportion." |
| 11 | Brookes 2004, Gesture Dictionary entry headed "arrest" | "arrest phakata (Is = Iscamtho) Undersides of both wrists are tapped together. Hands are made into fists." |
| 12 | Levinson 1997, p. 98 (PDF p. 1) | "examining the case of \"absolute\" (cardinal direction) spatial description in the Australian aboriginal language Guugu Yimithirr" |
| 1 | Wilkins 2003, T&F `meta name="description"` (truncated there, at "In") | "This chapter examines cultural variation in pointing gestures and discusses what this reveals about cross-cultural differences in the semiotics of pointing." |

Liszkowski et al. 2012, p. 3, also carries a usable secondary account of the closed chapter:
"According to Wilkins, in several cultures around the world people predominantly point with pursed
lips or with the chin instead of using the canonical index-finger point". That is tier A for
Liszkowski's statement, not for Wilkins' page.

## 3. Row ingredients for `corpus/SOURCES.md`

Take the source string, URL and HTTP note from §1; take the remaining cells here. Ids are the L1's
(S187 upward); `opened` is **2026-10-22** for every row.

| # | kind | scope (claim-scoped, per criterion 6) | recheck |
|---|---|---|---|
| 1 | chapter | bibliographic identity of the chapter and its stated topic only — publisher description, so tier B | 365d |
| 2 | paper | form and function of lip-pointing in Lao video data; the vector defined by gaze, the action as a gaze-switch (published version) | 365d |
| 3 | paper | effect of the left-hand taboo on Ghanaian pointing practice — read from the publisher abstract, so tier B | 365d |
| 4 | paper | preference for non-manual pointing among the Yupno against U.S. index-finger pointing | 365d |
| 5 | paper | the Aymara static model with the future behind the ego, and its gestural evidence | 365d |
| 6 | paper | Yupno deictic time as allocentric topography: past downhill, future uphill, non-linear | 365d |
| 7 | paper | cross-linguistic packaging of the same motion event in speech and gesture (published version) | 365d |
| 8 | paper | four factors governing cross-cultural variation of co-speech gesture (accepted manuscript) | 365d |
| 9 | paper | index-finger pointing in infants and caregivers across seven cultures by 10–14 months | 365d |
| 10 | paper | comprehension of iconic co-speech gesture: N400 modulation and the left fronto-temporal network | 365d |
| 11 | paper | the South African quotable-gesture repertoire and its three gestural types; only the printed dictionary entries are tier A | 365d |
| 12 | paper | absolute (cardinal) spatial description in Guugu Yimithirr and its non-verbal memory consequences | 365d |
| 13 | docs | pointing elicitation protocol and the "grammar of pointing" framing, co-authored by Wilkins | 365d |

## 4. Open sources found while probing that are not on the list

Both answer 200 as PDFs and I read their first pages, so a row for either is defensible.

| Found | URL | Status | What it carries |
|---|---|---|---|
| Wilkins, Kita & Enfield 2007, "'Ethnography of pointing' — field worker's guide", *Field Manual* 10:89–95, doi 10.17617/2.492922 | https://pure.mpg.de/rest/items/item_492922_8/component/file_2555838/content | 200, 8 pp. | the open, author-written statement of the Wilkins 2003 thesis: "such gestures have a place within a system of pointing gesture possibilities ... a kind of 'grammar of pointing'" (PDF p. 3). This is the practical substitute for row 1 |
| Cooperrider, Slotta & Núñez 2017, "Uphill and Downhill in a Flat World", *Cognitive Science* 41(3):768–799 | http://kensycooperrider.com/s/Cooperrider-Slotta-Nunez-2017-Uphill-and-Downhill-in-a-Flat-World-The-Conceptual-Topography-of-the-Y.pdf | 200, 32 pp. | the Yupno house topography; supports §5 (frames of reference) without leaning on the closed *Cognition* paper |

## 5. Route notes worth keeping (these cost probe attempts)

| Host / shape | Behaviour | Working form |
|---|---|---|
| `benjamins.com/catalog/...` | 403 with a bare `Mozilla/5.0` user agent; 403 under parallel probing; 200 with a full desktop UA plus `Accept-Language`, serially (three consecutive 200s) | the host prefix is irrelevant — send a real UA string and one request at a time, then read the abstract from `og:description`. `jbe-platform.com` answers 403 with or without `?crawler=true` |
| `pure.mpg.de/pubman/item/<id>/component/<file>/...pdf` | 403 | `https://pure.mpg.de/rest/items/<item>/component/<file>/content` answers 200 `application/pdf` |
| `hdl.handle.net/11858/...` | 403; the handle API answers 200 but exposes no URL value | skip the handle and go straight to the PuRe REST component |
| `onlinelibrary.wiley.com/doi/pdfdirect/...` and `/doi/pdf/...` | 403 (all four tried) | author or repository copy |
| `royalsocietypublishing.org/doi/pdf/...` | 403 | PMC `PMC4123675` |
| `escholarship.org/uc/item/...` | 403 | Wayback capture (e.g. 20240505141604 for `6sd477h8`) |
| `pure.mpg.de/rest/items?q=<words>` | returns alphabetical matches, **not** keyword hits | locate PuRe items by author-page or web search, then fetch the component |
| `archive.org/wayback/available` | fine, but the capture fetch 429s under repeated calls | space calls out; the CDX API confirms a capture exists before retrying |
| `rest/items/item_66562_3/.../file_66563/content` vs `rest/items/item_66622_3/.../file_66623/content` | two item ids, **one file**: both serve sha256 `465c83b4…`, 2,571,374 bytes (Levinson 1997) | register one row, from either URL |
| `rest/items/item_762562_16/...` vs `rest/items/item_762562_18/...` | both name `file_1466200`, so one file at two item versions (Liszkowski 2012) | register one row |
| two-column journal PDFs (e.g. the published Kita & Özyürek file) | whole-file `pdftotext` interleaves the columns, so a sentence's folio can come out one page off | extract with `pdftotext -f N -l N` per page and read the running head as that page's folio; even pages sometimes omit it (pdf p. 7 = "22 S. Kita…", p. 9 = "24", so p. 8 = 23) |

One row per work, whichever seat opens it. Two works sit in both my table and ScribeSec05SpaceTime's
draft rows — Levinson 1997, and (from other tables) Núñez et al. 2012 and Núñez & Sweetser 2006 — so
each of those must collapse to a single S-id at integration. Haviland 1993 and 1996, Fuhrman &
Boroditsky 2010, McNeill, Cienki 2022, Cooperrider/Abner/Goldin-Meadow 2018 and Williamson et al. 2026
were opened by other seats, not by me, and I make no claim about them here.

## 6. What I did not do

- I did not verify that any of these pages supports a specific sentence of the drafted entry; that is
  the section scribes' and the falsify wave's check.
- I did not write rows into `corpus/SOURCES.md`, assign S-ids, or touch the entry, `corpus/README.md`
  or `corpus/lessons/`. The L1 assigns ids from S187 upward.
- I did not run `reports/round-53/accept-c.py` or `d-count.py`; neither is exercised by this item.
- No tool was installed or upgraded for this probe.

## 7. Handoff caution for whoever writes the rows

The round-52 mined mistake was eleven bare `, -N` draft-id fragments left in `used-by` cells at
integration. Write seat draft ids only in the `NEW-<SeatName>-<n>` form, and replace every one with
its assigned S-id before the round closes. A `used-by` cell must name
`corpus/knowledge/linguistics/gesture-co-speech-pointing.md` exactly.
