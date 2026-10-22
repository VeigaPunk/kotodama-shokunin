# ScoutBattisonRoute — is there an ordinary-access copy of Battison 1974 / 1978?

Round 52, attempt 1. Claim D (depth, repair-first). Read-only scout; no lane file was edited.

## Assigned item

Find a copy of Battison 1974, "Phonological Deletion in American Sign Language",
*Sign Language Studies* 5:1–19, or Battison 1978, *Lexical Borrowing in American Sign
Language* (Linstok Press), reachable by ordinary means (plain request, public copy,
Wayback/archive.org, open repository). A copy that opens would let the Dominance
Condition wording, the passive-hand set and the minimal pairs be cited to the work
itself; no copy that opens leaves those details unverified.

## Result — plainly

**No copy of either work opened by ordinary means.** Every route below either served an
access challenge, a login/purchase page, a lending restriction, or a record without full
text. The Dominance Condition details therefore stay **unverified at the work itself**
(tier A open copy). What can be said with evidence is narrower: open secondary rows
already present at base (S096, S097/S133) carry the seven-shape passive set and four ASL
minimal pairs, and a new open corroborator was found (Kwansei Gakuin 2025) that reproduces
the condition verbatim. Confidence high on the negative; the negative is a result, not a
gap in the search.

## Routes tried

| # | URL | HTTP | What was readable |
|---|---|---|---|
| 1 | `https://ida.gallaudet.edu/cgi/viewcontent.cgi?article=1004&context=sls` (Gallaudet issue scan) | 403 | Cloudflare challenge page. Not bypassed, per assignment and QUALITY 10 |
| 2 | `https://ida.gallaudet.edu/sls/5/` (volume index) | 200 | Volume 5, 1974 index; lists the article with a "Download" link that is route 1 |
| 3 | Wayback `web.archive.org/web/20250719091210id_/https://ida.gallaudet.edu/sls/5/` | 200 | Same index page, archived. No body text |
| 4 | CDX for the PDF: `.../cgi/viewcontent.cgi?article=1004&context=sls` | 200 (CDX) | **Zero captures.** The only capture of the bepress path `context/sls/article/1004/viewcontent/V5_1974.pdf` is a **302 challenge redirect**, not the PDF |
| 5 | `https://doi.org/10.1353/sls.1974.0005` → `muse.jhu.edu/article/507140` | 200 | Redirects to `muse.jhu.edu/verify?...` — "Project MUSE -- Verification required!" with a captcha. Not bypassed |
| 6 | Wayback `web.archive.org/web/20240529200719id_/https://muse.jhu.edu/article/507140` | 200 | **Real MUSE article page**: author, *Sign Language Studies* vol. 5, October 1974, pp. 1–19, DOI, and the abstract only. No body, no first page |
| 7 | Wayback captures of `muse.jhu.edu/article/507140/pdf` (2017, 2022) | 200 | `text/html`, ~7–8 KB: login/purchase shell, not the PDF |
| 8 | `https://www.academia.edu/118766331/Phonological_Deletion_in_American_Sign_Language` | 403 | `<title>Just a moment...` — Cloudflare. Not bypassed |
| 9 | `https://www.jstor.org/stable/26203099` | 200 | `<title>Client Challenge` — bot wall. Not bypassed |
| 10 | `https://catalog.hathitrust.org/Search/Home?lookfor=Battison+lexical+borrowing` and `babel.hathitrust.org/cgi/ls?...` | 403 | "Just a moment..." Cloudflare. Not bypassed |
| 11 | `https://catalog.hathitrust.org/api/volumes/brief/oclc/4517501.json` (OCLC from Open Library) | 200 | `{"records": {}, "items": []}` — no HathiTrust holding for the 1978 book |
| 12 | `https://archive.org/details/lexicalborrowing0000robb` (1978 book scan) | 200 | Metadata only: 262 images, `access-restricted-item: true`, collections `inlibrary`/`printdisabled`. Lending item |
| 13 | `.../fulltext/inside.php?item_id=lexicalborrowing0000robb...&q=dominance` | 403 | "Item not available" — search-inside disabled for this restricted item |
| 14 | `https://archive.org/download/lexicalborrowing0000robb/lexicalborrowing0000robb_djvu.txt` | 401 | Authorization required (lending). Not bypassed |
| 15 | `https://openlibrary.org/search/inside?q=%22one+hand+must+be+passive%22` | 200 | `<title>Human Verification` — challenge. Not bypassed |
| 16 | `https://books.google.com/books?id=7-O7AAAAIAAJ` (1978 volume, found via the public Books feed) | 200 | Volume page loads, no preview offered; "not available" |
| 17 | `books.google.com/books?id=7-O7AAAAIAAJ&jscmd=SearchWithinVolume&q=dominance` (also `passive`) | 200 | `{"number_of_results":0,...}` for both terms — no searchable text |
| 18 | `https://www.googleapis.com/books/v1/volumes?q=...` | 429 | Project-wide daily quota exhausted; no result |
| 19 | `https://api.unpaywall.org/v2/10.1353/sls.1974.0005` | 200 | `is_oa: false`, `oa_status: closed`, no OA locations |
| 20 | `https://api.semanticscholar.org/graph/v1/paper/DOI:10.1353/sls.1974.0005` | 200 | Record found; `openAccessPdf.status: CLOSED`, empty URL. Search endpoint returns 429 |
| 21 | `https://api.openalex.org/works?search=...` and title filter for the book | 200 | Both works found; `open_access.oa_url: null`, no repository copy |
| 22 | `https://api.core.ac.uk/v3/search/works/?q=...` | 301→500 | Redirect then server error; no result |
| 23 | `https://api.openaire.eu/search/publications?title=...` | 200 | One record (DOI, abstract); no full-text instance |
| 24 | `https://api.ies.ed.gov/eric/?search=author:"Battison, Robbin"` | 200 | `ED163785` for the 1978 book, `e_fulltextauth: 0` — record only, no ERIC full text |
| 25 | `https://api.fatcat.wiki/v0/release/lookup?doi=...` | timeout | Connection timed out after 60 s; no data |
| 26 | `https://scholar.archive.org/search?q=...` | 200 | `<title>Verify - IA Scholar` — challenge. Not bypassed |
| 27 | `https://escholarship.org/content/qt4zw7p9qg/qt4zw7p9qg.pdf` | 200 | 8.3 MB PDF opens (landing page is AWS WAF-challenged, the PDF URL is not). **But** it is Lynn A. Friedman's 1976 Berkeley dissertation "Phonology of a Soundless Language", not Battison's — same title family, different author. Not usable |

Route 27 is the one near-miss worth recording: the title looks like the work the OpenAlex
search surfaced, and the PDF does open, but the author is Friedman (OpenAlex
`W1513805112` also credits Friedman). It must not be filed as a Battison text.

## What did open, and exactly what it carries

**A. CSLDS (Asia-Pacific Consortium) Module 7 — S097, superseded on anchor by S133.**
`http://www.cslds.org/apsl-consortium/sign-linguistics/module-7-sign-phonetics-and-phonology-symmetry-and-dominance-condition/`,
HTTP 200, plain GET, no challenge. The page's only headings are the title, Type 1, Type 2,
Type 3 and References; the condition text sits in an unheaded paragraph after the Type
list. Quote (25 words), same paragraph:

> "the passive hand can only be one of the following handshapes: A, S, B, 5, G (i.e., 1), C and O, with very few exceptions"

and, three sentences later: "Out of the 45 possible handshapes in ASL, only 7 can appear
as the passive hand of a Type-3 two-handed sign." Tier B (teaching module reporting
Battison 1978, pp. 206–207). This is the base row the landed repair leans on, and its
passive set is the **seven**-shape list.

**B. Hara 2025, Kwansei Gakuin University — new, open.**
`https://www.kwansei.ac.jp/c_shuwa/assets/3.pdf`, HTTP 200, `application/pdf`, 8.0 MB,
plain GET. 原大介 (Hara, Daisuke), "A Proposal of a Location Constraint on Type III
Syllables in Japanese Sign Language as a Supplement to the Dominance Condition",
*Journal of Sign and Spoken Languages* / 手話・音声言語研究 3 (2025), Kwansei Gakuin
University Sign Language Research Center, ISSN 2759-355X. Section "(3a) The dominance
condition", **printed page 3** (PDF page 7), reproduces (23 words):

> "the specification of the passive handshape is restricted to be one of a small set : A, S, B, 5, G, C, O"

Its reference list carries "Battison, R. (1978) Lexical Borrowing in American Sign
Language. Linstok Press." It also reports, as its own contribution, that Japanese Sign
Language Type-III passive hands are limited to B, S, C, 1 rather than the seven (Hara &
Miwa 2023a/b, 2025). Tier B for the wording of Battison's condition; the JSL claim is
that paper's own, not Battison's.

**C. CSLDS Module 6 — S096.** `.../6-phonetics-and-phonology-minimal-pairs/`, HTTP 200.
Lists, verbatim, the ASL examples by parameter: handshape "CAR – ASL (Battison, 1978)"
and "WHICH – ASL (Battison 1978)"; location "ONION – ASL" and "APPLE – ASL"; movement
"NAME – ASL (Battison, 1978)" and "SHORT – ASL (Battison 1978)"; orientation "the examples
given by him were CHAIR and NAME". It contains **no** `OFFER`, `MAYBE` or `TRAIN` gloss
(re-checked on the extracted page text, case-sensitive; the only movement pair is
NAME/SHORT. An earlier case-insensitive hit was the word "training"). Tier B.

**D. Project MUSE abstract, via Wayback (route 6)**, 20 words: "The American Sign Language
of the deaf (ASL) has a level of structure which is analogous to phonology." Location:
article page abstract. Tier B (publisher abstract for claims about the work); it says
nothing about the conditions.

## What this means for claim D (attack, not redraft)

1. **Counter holds.** `awk '/S094/{n++} END{print n+0}' corpus/knowledge/linguistics/sign-languages-manual-modality.md`
   → `0` at `dea5ece`; `grep -rn 'S094' corpus/knowledge | wc -l` → `0`. No S134+ id, no C
   entry and no `lessons/round-52.md` citation appears in the entry.
2. **The two re-cited details are carried by the cited base rows.** Entry `:87` (45
   handshapes, 7 passive) and `:92` (seven shapes A, S, B, 5, G, C, O) match route A
   sentence for sentence; entry `:93`'s pairs match route C. Nothing rests on Battison
   1974 any more.
3. **Dropping OFFER/MAYBE and SHORT/TRAIN was correct.** Neither pair exists in S096, and
   the article stayed shut, so those two pairs had no open support left. S096 pairs SHORT
   with NAME instead. The entry's honest hedge for the 1974 set (`an earlier, smaller 1974
   set is not checked here (to-verify)`) is the right disposition while the article is
   unopened.
4. **Defect to route: the entry cites S097, not its correcting row S133.** Entry `:87` and
   `:92` cite S097. S097's anchor cell (`corpus/SOURCES.md:126`) names "sections Type
   1/Type 3, Symmetry Condition, Dominance Condition"; the page has no such sections
   (verified above, and it is round-51 routed defect 3). `corpus/SOURCES.md:162` (S133)
   exists precisely to supersede that anchor, with the anchor the page does have. As
   landed, a verifier following the citation lands on a locator the lane has already
   ruled wrong. Suggested repair for the L1: replace `S097` with `S133` at entry `:87` and
   `:92`, then move the registry cells — `corpus/SOURCES.md:126` (S097) is `mined` with
   `used-by` naming this entry, and `:162` (S133) is `queued` with `used-by` `—`, so the
   two used-by cells and S133's status swap, logged old→new in the round lesson as the
   registry contract requires. S133 is below S134, so the claim's `must_not_cite` is
   unaffected. Severity: taste/anchor, not a falsifier hit.

## Frontier step — a row opened this round (draft, 11 columns)

Offered only as an independent open corroborator of the condition wording. **D must not
cite it** (it would be S134+); no consumer is named, so status is `queued`, as S133 is.

| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
| NEW-BattisonRoute-1 | Hara, Daisuke, "A Proposal of a Location Constraint on Type III Syllables in Japanese Sign Language as a Supplement to the Dominance Condition", *Journal of Sign and Spoken Languages* / 手話・音声言語研究 3 (2025), Kwansei Gakuin University — https://www.kwansei.ac.jp/c_shuwa/assets/3.pdf | paper | B | the wording of Battison's (1978) symmetry and dominance conditions, and a JSL-specific restriction on the passive hand | section "(3a) The dominance condition", printed p. 3 (PDF p. 7); references list "Battison, R. (1978) Lexical Borrowing in American Sign Language. Linstok Press." | reproduces the dominance condition clause by clause, "(c) the specification of the passive handshape is restricted to be one of a small set : A, S, B, 5, G, C, O"; reports JSL Type-III passive hands limited to B, S, C, 1 (Hara & Miwa 2023a/b, 2025), with O and 5 as allophones — the paper's own claim, not Battison's; useful as a second open witness that the 1978 set is seven, not six | queued | 2026-10-22 | 365d | — |

## Mined mistake

**S094 was sourced through an access challenge.** `corpus/SOURCES.md:123` records the
Gallaudet PDF as "open issue scan; Cloudflare-gated, opened via headless browser"; the
round-51 closure ruled that counts as unopened (S132, `:161`), and this round's
`tools/check-source-access.py` enforces exactly that (`BYPASS` regex matches "headless").
The mistake to keep: a scan that yields text is not thereby an opened source, and the
correct response to a challenge is to record the failure and fall back to a secondary
row or `(to-verify)` — which is what the landed repair did. A second, smaller lesson from
this scout: an open PDF with the right title is not the right work (route 27).

## Routed defect 2 of round 51 (`corpus/lessons/round-51-verifier-spotcheck.md:121-129`)

Defect 2 asked for a Battison re-open through the publisher, Project MUSE or a library
copy, "then file a new row. Otherwise re-cite those details, or mark them `(to-verify)`".
Outcome this round: publisher/Gallaudet, MUSE, JSTOR, HathiTrust, academia.edu, Internet
Archive lending, Open Library search-inside and Google Books were all challenged or
restricted; no new Battison row is fileable. The lane took the "re-cite" branch, and the
re-citation is supported by routes A and C. Defect 2 can be closed on that branch; the
article itself remains an open flip for a future round with an ordinary route
(institutional access to MUSE, or a library scan).

## Checks not run by me (for the main agent)

- `python3 -B tools/check-source-access.py` — I did not run it; the S094 sweep above is a
  plain grep, not the checker's verdict.
- `python3 -B reports/round-52/dry-run.py` and the claim counters — not run; not my seat.
- No build, lint, test or formatter run. No file other than this report was written. No
  tool was installed or upgraded; nothing required pacman.

## Remaining unknowns

- Whether Battison 1974 itself prints six shape symbols, seven, or lists `5` in one
  passage and `S` in another (a discrepancy a web summary asserted but I could not verify
  against any opened copy). Only the article can settle it.
- Whether OFFER/MAYBE and SHORT/TRAIN appear in the 1974 article at all; S096 does not
  carry them.
- Whether a MUSE-institutional or library scan of *Sign Language Studies* 5 exists in any
  ordinary-access archive; none was found in Wayback, HathiTrust, IA or ERIC.
