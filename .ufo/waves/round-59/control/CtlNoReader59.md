# CtlNoReader59 — round-59 no-reader / FETCH-59 adversarial controls

**Axes:** coverage (claim C), depth/source fidelity, freshness/provenance, and calibration/discernment. No claim judgment or admission is made here.

**Frozen revision:** `1b80ee41f544d17c0410733a47a3eecac01bf25e`; claim base `39c9ce8a6be5e5625d8befb54df53d621a3a7929`. All counter runs used `/fast/scratch/hyaku/kotodama-r59/CtlNoReader59/clone` as cwd and `timeout 900`. No counter or declaration was edited. Corpus mutations existed only in that sandbox. No tools were installed.

**Result:** no control is `MEETS-COUNTER`; no control is `MEETS-MECHANICAL`. All four landed controls also fail substantive mechanical legs. SUPPORT reports missing registry and planted key in every landing, but SUPPORT is never the only failing leg.

Rows were authored without consulting source-page bodies: the GET collector emitted only title, h1, meta, breadcrumb/cookie/footer text; the snippet control copied search-service source snippets. The frozen rowcheck itself reads bodies as required to score them. Capture probes reuse a longer quote already present in the frozen local S304 anchor; they do not claim a new source reading. Identifiers restart at S600 in each independent fixture. Every fixture row has 11 cells.

## Row-leg results

| Draft | Rows | LOCATE | BOILER | RELEVANCE | TOPIC | All four |
|---|---:|---:|---:|---:|---:|---|
| metadata | 30 | 11 | 0 | 30 | 9 | none |
| snippets | 37 | 16 | 5 | 37 | 15 | S611, S614, S621, S623, S634 |
| structural | 28 | 22 | 2 | 28 | 0 | none |
| fetch-abuse | 5 | 0 | 0 | 5 | 0 | none |
| fetch-v2 | 5 | 2 | 2 | 5 | 2 | S601, S603 |

`fetch-abuse` was the initial cheap harvest: its first frozen S304 quote was only six words and was rejected before fetching. `fetch-v2` replaces it with the longer actual amulet sentence below. The stronger capture probe, not the six-word attempt, informs the findings. `fetch-padded` lands the five stronger probes plus 20 metadata rows, so FLOOR, SET and SWEEP are exercised rather than avoided.

### Search-only rows that pass all four row legs

- **S611** — https://www.aub.edu.lb/museum_archeo/Pages/Amulets-&-Talismans.aspx
  - Search snippet quote: `The amulet is an object with natural magical properties, whereas a talisman must be charged with magical powers by a creator; it is this act of consecration or charging that gives the talisman its alleged magical powers.`
  - Synthetic teaching: `Study natural and object and amulet as distinct clues when designing culturally meaningful protective objects.`
- **S614** — https://foundlingmuseum.org.uk/tokens-of-history/amulets/
  - Search snippet quote: `We find little information in eighteenth-century archives about the types of amulets and talismans worn by the common people. So, the Foundling Museum’s collection of objects provides a unique insight into popular magic.`
  - Synthetic teaching: `Study information and little and find as distinct clues when designing culturally meaningful protective objects.`
- **S621** — https://journal.sciencemuseum.ac.uk/article/history-of-amulets/
  - Search snippet quote: `This particular hare’s foot, which forms part of the Science Museum’s amulet collection, is originally from Norfolk and dated 1870–1920`
  - Synthetic teaching: `Study foot and hare and particular as distinct clues when designing culturally meaningful protective objects.`
- **S623** — https://www.londonmuseum.org.uk/collections/v/object-423977/charm-amulet/
  - Search snippet quote: `This thin sheet of lead was rolled up and worn as a charm to protect the wearer, Demetrios, from dying in a pandemic that ravaged much of the Roman Empire in the 160s and 170s CE.`
  - Synthetic teaching: `Study lead and sheet and thin as distinct clues when designing culturally meaningful protective objects.`
- **S634** — https://islamicworld.britishmuseum.org/collection/RRM46563
  - Search snippet quote: `The belief in the protective power of hand amulets dates back millennia.`
  - Synthetic teaching: `Study power and protective and belief as distinct clues when designing culturally meaningful protective objects.`

These are five independent actual row passes without source-body reading. They do **not** establish a 20-row / 10-host mechanical pass, nor a SUPPORT pass. The generic teaching sentences were built by reordering three content words from each quote, not by interpreting the page. RELEVANCE passes all 95 metadata/snippet/structural rows despite that construction.

### FETCH-59 probes

All five stronger probes use the frozen S304 sentence: `Amulets with images of his full body or, more often, just his head, were common in the early first millennium B.C.`

- `fetch-v2:S600`: observed British Museum 403/absent live page first, then a Wayback capture of an entirely different Met page. Rejected here because the archive did not locate; this is **not** evidence that same-page identity is enforced.
- `fetch-v2:S601`: actual Met live page first, then a fabricated `19000101000000id_` capture timestamp. **All four row legs pass**, because the live URL locates and the bogus capture is never validated. This proves acceptance of an unvalidated listed capture, not successful retrieval of a nonexistent historical capture.
- `fetch-v2:S602`: observed British Museum 403 live URL followed by a capture of the Met site root. Rejected on fetch/location; no root-capture bypass was established.
- `fetch-v2:S603`: observed British Museum 403 live URL followed by a completely unrelated **live Met URL**, not even a capture. **All four row legs pass** on the second URL. This directly violates the declared source-cell grammar (live page, optionally one same-page Wayback capture).
- `fetch-v2:S604`: nonexistent-timestamp capture alone. Rejected on network error. It does not prove timestamp correctness checking.

Ordinary archive metadata GETs additionally returned HTTP429 for the Met capture, its fabricated-1900 timestamp, and its root capture; the known Te Ara article capture returned HTTP200. No challenge, captcha, login, or paywall was passed. Availability is not an identity check; archive-specific identity acceptance remains unproved because these exact malformed-capture requests did not locate.

## Landed full-counter receipts

CONTROL metadata-labels | claim C | exit 1 | ACCEPT-C-59: FAIL | failing legs: [LOCATE, BOILER, TOPIC, SUPPORT]

Landing and scoring command (script changes only the entry, appended rows, and corresponding README row/counts):

```sh
timeout 930 python3 -B /fast/scratch/hyaku/kotodama-r59/CtlNoReader59/run_control.py full metadata
# Executed from clone root by that runner:
timeout 900 python3 -B reports/round-59/accept-c.py
```

Pasted stdout:

```text
SET PASS count=235 required=235 added=['corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md'] removed=[]
SWEEP PASS exit=0 rows 235 files 235 missing_from_index 0 []
FLOOR PASS cited=30 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
TIER PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LOCATE FAIL passing=11 cited=30 at=2026-10-23T02:52Z failing=['S602: quote under 8 words', 'S603: https://www.juedisches-museum-muenchen.de/en/exhibitions/archive/do-you-believe-in-the-evil-eye url-reflects-quote', 'S605: quote under 8 words', 'S606: https://england.prm.ox.ac.uk/englishness-loop-of-rowan-tree.html url-reflects-quote', 'S607: https://nationalmuseet.dk/en/exhibitions/the-power-of-amulets-luck-fear-and-magic quote-absent', 'S609: https://www.horniman.ac.uk/story/magic-charms-and-amulets/ url-reflects-quote', 'S611: quote under 8 words', 'S615: https://www.metmuseum.org/art/collection/search/556100 quote-absent', 'S617: https://collection.sciencemuseumgroup.org.uk/objects/co108064/amulet-and-charm-to-protect-against-plague-amulet url-reflects-quote', 'S618: https://collection.sciencemuseumgroup.org.uk/objects/co103142/bone-amulet-in-the-shape-of-a-hand-and-arm url-reflects-quote', 'S619: https://collection.sciencemuseumgroup.org.uk/objects/co108221/sheep-bone-amulet-worn-by-fishermen-and-sailors url-reflects-quote', 'S621: quote under 8 words', 'S622: quote under 8 words', 'S623: quote under 8 words', 'S625: quote under 8 words', 'S626: https://henry-moore.org/whats-on/a-kind-of-magic-talismans-charms-and-amulets-from-the-british-museum/ url-reflects-quote', 'S627: https://journal.sciencemuseum.ac.uk/article/history-of-amulets/ url-reflects-quote', 'S628: quote under 8 words', 'S629: https://www.horniman.ac.uk/story/hag-stones-and-lucky-charms/ quote-absent']
BOILER FAIL passing=0 cited=30 at=2026-10-23T02:52Z failing=['S600: quote-is-title-heading-or-meta', 'S601: quote-is-title-heading-or-meta', 'S602: not-located', 'S603: not-located', 'S604: quote-is-title-heading-or-meta', 'S605: not-located', 'S606: not-located', 'S607: not-located', 'S608: quote-is-title-heading-or-meta', 'S609: not-located', 'S610: quote-is-title-heading-or-meta', 'S611: not-located', 'S612: quote-is-title-heading-or-meta', 'S613: quote-is-title-heading-or-meta', 'S614: quote-is-title-heading-or-meta', 'S615: not-located', 'S616: quote-is-title-heading-or-meta', 'S617: not-located', 'S618: not-located', 'S619: not-located', 'S620: quote-is-title-heading-or-meta', 'S621: not-located', 'S622: not-located', 'S623: not-located', 'S624: quote-is-title-heading-or-meta', 'S625: not-located', 'S626: not-located', 'S627: not-located', 'S628: not-located', 'S629: not-located']
RELEVANCE PASS passing=30 cited=30 at=2026-10-23T02:52Z failing=[]
TOPIC FAIL passing=9 cited=30 at=2026-10-23T02:52Z failing=['S602: quote_hits=2 not-located', 'S603: quote_hits=0 not-located', 'S604: quote_hits=2 function_words=0 page_hits=10 page_terms=15 need=1/2/3/2', 'S605: quote_hits=0 not-located', 'S606: quote_hits=1 not-located', 'S607: quote_hits=2 not-located', 'S609: quote_hits=2 not-located', 'S611: quote_hits=1 not-located', 'S614: quote_hits=0 function_words=7 page_hits=2 page_terms=14 need=1/2/3/2', 'S615: quote_hits=0 not-located', 'S617: quote_hits=3 not-located', 'S618: quote_hits=1 not-located', 'S619: quote_hits=1 not-located', 'S621: quote_hits=0 not-located', 'S622: quote_hits=0 not-located', 'S623: quote_hits=1 not-located', 'S625: quote_hits=2 not-located', 'S626: quote_hits=1 not-located', 'S627: quote_hits=2 not-located', 'S628: quote_hits=1 not-located', 'S629: quote_hits=0 not-located']
FRESH PASS rows_reusing_registry_urls=[]
DISTINCT PASS shared=[] hosts=16 need=10
SUPPORT FAIL unsupported=['S600:no verdict', 'S601:no verdict', 'S602:no verdict', 'S603:no verdict', 'S604:no verdict', 'S605:no verdict', 'S606:no verdict', 'S607:no verdict', 'S608:no verdict', 'S609:no verdict', 'S610:no verdict', 'S611:no verdict', 'S612:no verdict', 'S613:no verdict', 'S614:no verdict', 'S615:no verdict', 'S616:no verdict', 'S617:no verdict', 'S618:no verdict', 'S619:no verdict', 'S620:no verdict', 'S621:no verdict', 'S622:no verdict', 'S623:no verdict', 'S624:no verdict', 'S625:no verdict', 'S626:no verdict', 'S627:no verdict', 'S628:no verdict', 'S629:no verdict'] qualified_seats=[] need_seats=2 planted=[] no registry: FileNotFoundError no planted key: FileNotFoundError
ACCEPT-C-59: FAIL
```

CONTROL search-snippets | claim C | exit 1 | ACCEPT-C-59: FAIL | failing legs: [LOCATE, BOILER, TOPIC, SUPPORT]

Landing and scoring command (script changes only the entry, appended rows, and corresponding README row/counts):

```sh
timeout 930 python3 -B /fast/scratch/hyaku/kotodama-r59/CtlNoReader59/run_control.py full snippets
# Executed from clone root by that runner:
timeout 900 python3 -B reports/round-59/accept-c.py
```

Pasted stdout:

```text
SET PASS count=235 required=235 added=['corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md'] removed=[]
SWEEP PASS exit=0 rows 235 files 235 missing_from_index 0 []
FLOOR PASS cited=37 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
TIER PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LOCATE FAIL passing=17 cited=37 at=2026-10-23T02:53Z failing=['S600: https://www.britishmuseum.org/collection/object/W_As1919-470 HTTPError', 'S601: https://www.britishmuseum.org/collection/object/W_2012-6006-15 HTTPError', 'S602: https://www.britishmuseum.org/collection/object/W_As1966-01-440 HTTPError', 'S603: https://www.britishmuseum.org/collection/object/E_Am1939-21-1 HTTPError', 'S604: https://www.britishmuseum.org/collection/object/H_1941-1208-1 HTTPError', 'S605: https://www.britishmuseum.org/collection/object/E_Af1868-1001-4 HTTPError', 'S606: https://www.britannica.com/topic/evil-eye HTTPError', 'S608: https://historicengland.org.uk/whats-new/features/discovering-witches-marks/what-are-witches-marks/ HTTPError', 'S609: https://historicengland.org.uk/whats-new/news/witches-marks-discovery-largest-in-britain/ HTTPError', 'S610: https://www.nationaltrust.org.uk/discover/history/warding-off-evil-with-witch-marks quote-absent', 'S612: https://www.horniman.ac.uk/story/magic-charms-and-amulets/ url-reflects-quote', 'S618: https://www.english-heritage.org.uk/about/search-news/new-research-reveals-previously-undiscovered-witches-marks-at-gainsborough-old-hall/ url-reflects-quote', 'S620: https://henry-moore.org/whats-on/a-kind-of-magic-talismans-charms-and-amulets-from-the-british-museum/ url-reflects-quote', 'S622: https://record.umich.edu/articles/amulet-collection-works-its-magic-at-taubman-and-at-kelsey/ HTTPError', 'S625: https://collection.sciencemuseumgroup.org.uk/objects/co68361/oval-amulet-to-protect-against-cholera-europe-1801-1900 url-reflects-quote', 'S627: https://collection.sciencemuseumgroup.org.uk/objects/co108064/amulet-and-charm-to-protect-against-plague-amulet url-reflects-quote', 'S628: https://collection.sciencemuseumgroup.org.uk/objects/co71938/brass-amulet-to-protect-the-wearer-from-cholera-france-1820-1880 url-reflects-quote', 'S629: https://collection.sciencemuseumgroup.org.uk/objects/co103142/bone-amulet-in-the-shape-of-a-hand-and-arm url-reflects-quote', 'S630: https://collection.sciencemuseumgroup.org.uk/objects/co108221/sheep-bone-amulet-worn-by-fishermen-and-sailors url-reflects-quote', 'S635: https://collectionswa.net.au/items/ccf7ab91-9a48-4cff-b0e5-0df9812da0f0 quote-absent']
BOILER FAIL passing=6 cited=37 at=2026-10-23T02:53Z failing=['S600: not-located', 'S601: not-located', 'S602: not-located', 'S603: not-located', 'S604: not-located', 'S605: not-located', 'S606: not-located', 'S607: quote-is-title-heading-or-meta', 'S608: not-located', 'S609: not-located', 'S610: not-located', 'S612: not-located', 'S613: quote-is-title-heading-or-meta', 'S615: quote-is-title-heading-or-meta', 'S616: quote-is-title-heading-or-meta', 'S617: quote-is-title-heading-or-meta', 'S618: not-located', 'S619: quote-is-title-heading-or-meta', 'S620: not-located', 'S622: not-located', 'S624: quote-is-title-heading-or-meta', 'S625: not-located', 'S626: quote-is-title-heading-or-meta', 'S627: not-located', 'S628: not-located', 'S629: not-located', 'S630: not-located', 'S631: quote-is-title-heading-or-meta', 'S632: quote-is-title-heading-or-meta', 'S633: quote-is-title-heading-or-meta', 'S635: not-located']
RELEVANCE PASS passing=37 cited=37 at=2026-10-23T02:53Z failing=[]
TOPIC FAIL passing=15 cited=37 at=2026-10-23T02:53Z failing=['S600: quote_hits=0 not-located', 'S601: quote_hits=1 not-located', 'S602: quote_hits=1 not-located', 'S603: quote_hits=1 not-located', 'S604: quote_hits=3 not-located', 'S605: quote_hits=0 not-located', 'S606: quote_hits=0 not-located', 'S608: quote_hits=0 not-located', 'S609: quote_hits=1 not-located', 'S610: quote_hits=1 not-located', 'S612: quote_hits=2 not-located', 'S617: quote_hits=0 function_words=5 page_hits=2 page_terms=14 need=1/2/3/2', 'S618: quote_hits=3 not-located', 'S620: quote_hits=1 not-located', 'S622: quote_hits=1 not-located', 'S625: quote_hits=1 not-located', 'S627: quote_hits=3 not-located', 'S628: quote_hits=0 not-located', 'S629: quote_hits=1 not-located', 'S630: quote_hits=1 not-located', 'S635: quote_hits=1 not-located', 'S636: quote_hits=0 function_words=4 page_hits=14 page_terms=19 need=1/2/3/2']
FRESH PASS rows_reusing_registry_urls=[]
DISTINCT PASS shared=[] hosts=19 need=10
SUPPORT FAIL unsupported=['S600:no verdict', 'S601:no verdict', 'S602:no verdict', 'S603:no verdict', 'S604:no verdict', 'S605:no verdict', 'S606:no verdict', 'S607:no verdict', 'S608:no verdict', 'S609:no verdict', 'S610:no verdict', 'S611:no verdict', 'S612:no verdict', 'S613:no verdict', 'S614:no verdict', 'S615:no verdict', 'S616:no verdict', 'S617:no verdict', 'S618:no verdict', 'S619:no verdict', 'S620:no verdict', 'S621:no verdict', 'S622:no verdict', 'S623:no verdict', 'S624:no verdict', 'S625:no verdict', 'S626:no verdict', 'S627:no verdict', 'S628:no verdict', 'S629:no verdict', 'S630:no verdict', 'S631:no verdict', 'S632:no verdict', 'S633:no verdict', 'S634:no verdict', 'S635:no verdict', 'S636:no verdict'] qualified_seats=[] need_seats=2 planted=[] no registry: FileNotFoundError no planted key: FileNotFoundError
ACCEPT-C-59: FAIL
```

CONTROL headings-breadcrumbs-footers | claim C | exit 1 | ACCEPT-C-59: FAIL | failing legs: [LOCATE, BOILER, TOPIC, DISTINCT, SUPPORT]

Landing and scoring command (script changes only the entry, appended rows, and corresponding README row/counts):

```sh
timeout 930 python3 -B /fast/scratch/hyaku/kotodama-r59/CtlNoReader59/run_control.py full structural
# Executed from clone root by that runner:
timeout 900 python3 -B reports/round-59/accept-c.py
```

Pasted stdout:

```text
SET PASS count=235 required=235 added=['corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md'] removed=[]
SWEEP PASS exit=0 rows 235 files 235 missing_from_index 0 []
FLOOR PASS cited=28 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
TIER PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LOCATE FAIL passing=22 cited=28 at=2026-10-23T02:53Z failing=['S606: https://collection.sciencemuseumgroup.org.uk/objects/co68714/amulet-of-saint-roch-to-protect-against-cholera url-reflects-quote', 'S611: https://collection.sciencemuseumgroup.org.uk/objects/co103142/bone-amulet-in-the-shape-of-a-hand-and-arm url-reflects-quote', 'S614: https://collection.sciencemuseumgroup.org.uk/objects/co108221/sheep-bone-amulet-worn-by-fishermen-and-sailors url-reflects-quote', 'S621: https://henry-moore.org/whats-on/a-kind-of-magic-talismans-charms-and-amulets-from-the-british-museum/ url-reflects-quote', 'S625: https://en.natmus.dk/historical-knowledge/denmark/prehistoric-period-until-1050-ad/the-mesolithic-period/amulets/amulets-in-the-modern-world/ url-reflects-quote', 'S627: https://www.horniman.ac.uk/story/hag-stones-and-lucky-charms/ url-reflects-quote']
BOILER FAIL passing=2 cited=28 at=2026-10-23T02:53Z failing=['S600: quote-on-root https://www.metmuseum.org/', 'S602: quote-on-root https://www.metmuseum.org/', 'S604: quote-on-root https://www.metmuseum.org/', 'S605: quote-on-root https://www.metmuseum.org/', 'S606: not-located', 'S607: quote-on-root https://collection.sciencemuseumgroup.org.uk/', 'S608: quote-on-root https://collection.sciencemuseumgroup.org.uk/', 'S609: quote-on-root https://collection.sciencemuseumgroup.org.uk/', 'S610: quote-on-root https://collection.sciencemuseumgroup.org.uk/', 'S611: not-located', 'S612: quote-on-root https://collection.sciencemuseumgroup.org.uk/', 'S613: quote-on-root https://collection.sciencemuseumgroup.org.uk/', 'S614: not-located', 'S615: quote-on-root https://collection.sciencemuseumgroup.org.uk/', 'S616: quote-on-root https://collection.sciencemuseumgroup.org.uk/', 'S617: quote-on-root https://collection.sciencemuseumgroup.org.uk/', 'S618: quote-on-root https://collection.sciencemuseumgroup.org.uk/', 'S619: quote-on-root https://www.wessexarch.co.uk/', 'S620: quote-on-root https://www.londonmuseum.org.uk/', 'S621: not-located', 'S622: quote-on-root https://henry-moore.org/', 'S623: quote-on-root https://journal.sciencemuseum.ac.uk/', 'S624: quote-on-root https://journal.sciencemuseum.ac.uk/', 'S625: not-located', 'S626: quote-on-root https://en.natmus.dk/', 'S627: not-located']
RELEVANCE PASS passing=28 cited=28 at=2026-10-23T02:53Z failing=[]
TOPIC FAIL passing=0 cited=28 at=2026-10-23T02:53Z failing=['S600: quote_hits=0 function_words=4 page_hits=80 page_terms=82 need=1/2/3/2', 'S601: quote_hits=2 function_words=1 page_hits=13 page_terms=17 need=1/2/3/2', 'S602: quote_hits=0 function_words=4 page_hits=13 page_terms=17 need=1/2/3/2', 'S603: quote_hits=0 function_words=3 page_hits=2 page_terms=14 need=1/2/3/2', 'S604: quote_hits=0 function_words=4 page_hits=2 page_terms=14 need=1/2/3/2', 'S605: quote_hits=0 function_words=4 page_hits=12 page_terms=12 need=1/2/3/2', 'S606: quote_hits=1 not-located', 'S607: quote_hits=0 function_words=2 page_hits=22 page_terms=15 need=1/2/3/2', 'S608: quote_hits=0 function_words=2 page_hits=22 page_terms=15 need=1/2/3/2', 'S609: quote_hits=0 function_words=2 page_hits=45 page_terms=45 need=1/2/3/2', 'S610: quote_hits=0 function_words=2 page_hits=45 page_terms=45 need=1/2/3/2', 'S611: quote_hits=1 not-located', 'S612: quote_hits=0 function_words=2 page_hits=12 page_terms=11 need=1/2/3/2', 'S613: quote_hits=0 function_words=2 page_hits=12 page_terms=11 need=1/2/3/2', 'S614: quote_hits=1 not-located', 'S615: quote_hits=0 function_words=2 page_hits=16 page_terms=14 need=1/2/3/2', 'S616: quote_hits=0 function_words=2 page_hits=16 page_terms=14 need=1/2/3/2', 'S617: quote_hits=0 function_words=2 page_hits=14 page_terms=19 need=1/2/3/2', 'S618: quote_hits=0 function_words=2 page_hits=14 page_terms=19 need=1/2/3/2', 'S619: quote_hits=0 function_words=3 page_hits=19 page_terms=11 need=1/2/3/2', 'S620: quote_hits=0 function_words=2 page_hits=11 page_terms=13 need=1/2/3/2', 'S621: quote_hits=3 not-located', 'S622: quote_hits=0 function_words=2 page_hits=20 page_terms=16 need=1/2/3/2', 'S623: quote_hits=0 function_words=5 page_hits=311 page_terms=242 need=1/2/3/2', 'S624: quote_hits=0 function_words=3 page_hits=311 page_terms=242 need=1/2/3/2', 'S625: quote_hits=2 not-located', 'S626: quote_hits=0 function_words=4 page_hits=13 page_terms=10 need=1/2/3/2', 'S627: quote_hits=0 not-located']
FRESH PASS rows_reusing_registry_urls=[]
DISTINCT FAIL shared=['S602=url:S601', 'S602=quote:S600', 'S604=url:S603', 'S604=quote:S600', 'S605=quote:S600', 'S607=url:S606', 'S608=url:S606', 'S609=quote:S607', 'S610=url:S609', 'S610=quote:S608', 'S612=url:S611', 'S612=quote:S607', 'S613=url:S611', 'S613=quote:S608', 'S615=url:S614', 'S615=quote:S607', 'S616=url:S614', 'S616=quote:S608', 'S617=quote:S607', 'S618=url:S617', 'S618=quote:S608', 'S622=url:S621', 'S624=url:S623', 'S626=url:S625'] hosts=8 need=10
SUPPORT FAIL unsupported=['S600:no verdict', 'S601:no verdict', 'S602:no verdict', 'S603:no verdict', 'S604:no verdict', 'S605:no verdict', 'S606:no verdict', 'S607:no verdict', 'S608:no verdict', 'S609:no verdict', 'S610:no verdict', 'S611:no verdict', 'S612:no verdict', 'S613:no verdict', 'S614:no verdict', 'S615:no verdict', 'S616:no verdict', 'S617:no verdict', 'S618:no verdict', 'S619:no verdict', 'S620:no verdict', 'S621:no verdict', 'S622:no verdict', 'S623:no verdict', 'S624:no verdict', 'S625:no verdict', 'S626:no verdict', 'S627:no verdict'] qualified_seats=[] need_seats=2 planted=[] no registry: FileNotFoundError no planted key: FileNotFoundError
ACCEPT-C-59: FAIL
```

CONTROL fetch-rule-abuse | claim C | exit 1 | ACCEPT-C-59: FAIL | failing legs: [LOCATE, BOILER, TOPIC, FRESH, DISTINCT, SUPPORT]

Landing and scoring command (script changes only the entry, appended rows, and corresponding README row/counts):

```sh
timeout 930 python3 -B /fast/scratch/hyaku/kotodama-r59/CtlNoReader59/run_control.py full fetch-padded
# Executed from clone root by that runner:
timeout 900 python3 -B reports/round-59/accept-c.py
```

Pasted stdout:

```text
SET PASS count=235 required=235 added=['corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md'] removed=[]
SWEEP PASS exit=0 rows 235 files 235 missing_from_index 0 []
FLOOR PASS cited=25 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
TIER PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LOCATE FAIL passing=11 cited=25 at=2026-10-23T02:56Z failing=['S600: https://www.britishmuseum.org/collection/object/W_As1919-470 HTTPError; https://web.archive.org/web/20171121161933id_/https://www.metmuseum.org/exhibitions/list', 'S602: https://www.britishmuseum.org/collection/object/W_2012-6006-15 HTTPError; https://web.archive.org/web/20171121161933id_/https://www.metmuseum.org/ HTTPError', 'S604: https://web.archive.org/web/19000101000000id_/https://www.metmuseum.org/exhibitions/listings/2014/assyria-to-iberia/blog/posts/pazuzu HTTPError', 'S607: quote under 8 words', 'S608: https://www.juedisches-museum-muenchen.de/en/exhibitions/archive/do-you-believe-in-the-evil-eye url-reflects-quote', 'S610: quote under 8 words', 'S611: https://england.prm.ox.ac.uk/englishness-loop-of-rowan-tree.html url-reflects-quote', 'S612: https://nationalmuseet.dk/en/exhibitions/the-power-of-amulets-luck-fear-and-magic quote-absent', 'S614: https://www.horniman.ac.uk/story/magic-charms-and-amulets/ url-reflects-quote', 'S616: quote under 8 words', 'S620: https://www.metmuseum.org/art/collection/search/556100 quote-absent', 'S622: https://collection.sciencemuseumgroup.org.uk/objects/co108064/amulet-and-charm-to-protect-against-plague-amulet url-reflects-quote', 'S623: https://collection.sciencemuseumgroup.org.uk/objects/co103142/bone-amulet-in-the-shape-of-a-hand-and-arm url-reflects-quote', 'S624: https://collection.sciencemuseumgroup.org.uk/objects/co108221/sheep-bone-amulet-worn-by-fishermen-and-sailors url-reflects-quote']
BOILER FAIL passing=2 cited=25 at=2026-10-23T02:56Z failing=['S600: not-located', 'S602: not-located', 'S604: not-located', 'S605: quote-is-title-heading-or-meta', 'S606: quote-is-title-heading-or-meta', 'S607: not-located', 'S608: not-located', 'S609: quote-is-title-heading-or-meta', 'S610: not-located', 'S611: not-located', 'S612: not-located', 'S613: quote-is-title-heading-or-meta', 'S614: not-located', 'S615: quote-is-title-heading-or-meta', 'S616: not-located', 'S617: quote-is-title-heading-or-meta', 'S618: quote-is-title-heading-or-meta', 'S619: quote-is-title-heading-or-meta', 'S620: not-located', 'S621: quote-is-title-heading-or-meta', 'S622: not-located', 'S623: not-located', 'S624: not-located']
RELEVANCE PASS passing=25 cited=25 at=2026-10-23T02:56Z failing=[]
TOPIC FAIL passing=9 cited=25 at=2026-10-23T02:56Z failing=['S600: quote_hits=2 not-located', 'S602: quote_hits=2 not-located', 'S604: quote_hits=2 not-located', 'S607: quote_hits=2 not-located', 'S608: quote_hits=0 not-located', 'S609: quote_hits=2 function_words=0 page_hits=10 page_terms=15 need=1/2/3/2', 'S610: quote_hits=0 not-located', 'S611: quote_hits=1 not-located', 'S612: quote_hits=2 not-located', 'S614: quote_hits=2 not-located', 'S616: quote_hits=1 not-located', 'S619: quote_hits=0 function_words=7 page_hits=2 page_terms=14 need=1/2/3/2', 'S620: quote_hits=0 not-located', 'S622: quote_hits=3 not-located', 'S623: quote_hits=1 not-located', 'S624: quote_hits=1 not-located']
FRESH FAIL rows_reusing_registry_urls=['S600', 'S601', 'S603', 'S604']
DISTINCT FAIL shared=['S601=url:S600', 'S601=quote:S600', 'S602=quote:S600', 'S603=url:S600', 'S603=quote:S600', 'S604=url:S600', 'S604=quote:S600'] hosts=12 need=10
SUPPORT FAIL unsupported=['S600:no verdict', 'S601:no verdict', 'S602:no verdict', 'S603:no verdict', 'S604:no verdict', 'S605:no verdict', 'S606:no verdict', 'S607:no verdict', 'S608:no verdict', 'S609:no verdict', 'S610:no verdict', 'S611:no verdict', 'S612:no verdict', 'S613:no verdict', 'S614:no verdict', 'S615:no verdict', 'S616:no verdict', 'S617:no verdict', 'S618:no verdict', 'S619:no verdict', 'S620:no verdict', 'S621:no verdict', 'S622:no verdict', 'S623:no verdict', 'S624:no verdict'] qualified_seats=[] need_seats=2 planted=[] no registry: FileNotFoundError no planted key: FileNotFoundError
ACCEPT-C-59: FAIL
```

## Rowcheck commands and pasted output

### metadata

```sh
timeout 900 python3 -B reports/round-59/rowcheck.py --draft /fast/scratch/hyaku/kotodama-r59/CtlNoReader59/metadata.rows.md --entry /fast/scratch/hyaku/kotodama-r59/CtlNoReader59/metadata.entry.md
```

Exit: 1

```text
S600 LOCATE PASS BOILER FAIL RELEVANCE PASS TOPIC PASS | LOCATE: https://blog.sciencemuseum.org.uk/5-amulets-for-5-senses/ | BOILER: quote-is-title-heading-or-meta | RELEVANCE: shared=['amule', 'histo', 'objec', 'prote', 'throu'] | TOPIC: quote_hits=1 function_words=7 page_hits=13 page_terms=12 need=1/2/3/2
S601 LOCATE PASS BOILER FAIL RELEVANCE PASS TOPIC PASS | LOCATE: https://blog.sciencemuseum.org.uk/powerful-amulets/ | BOILER: quote-is-title-heading-or-meta | RELEVANCE: shared=['annie', 'histo', 'medic'] | TOPIC: quote_hits=1 function_words=5 page_hits=27 page_terms=23 need=1/2/3/2
S602 LOCATE FAIL BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: quote under 8 words | BOILER: not-located | RELEVANCE: shared=['amule', 'museu', 'talis'] | TOPIC: quote_hits=2 not-located
S603 LOCATE FAIL BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: https://www.juedisches-museum-muenchen.de/en/exhibitions/archive/do-you-believe-in-the-evil-eye url-reflects-quote | BOILER: not-located | RELEVANCE: shared=['belie', 'evil', 'jüdis'] | TOPIC: quote_hits=0 not-located
S604 LOCATE PASS BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: https://web.prm.ox.ac.uk/amulets/index.php/museum-trail/15-resources/145-trail-evil-eye/index.html | BOILER: quote-is-title-heading-or-meta | RELEVANCE: shared=['amule', 'bless', 'small'] | TOPIC: quote_hits=2 function_words=0 page_hits=10 page_terms=15 need=1/2/3/2
S605 LOCATE FAIL BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: quote under 8 words | BOILER: not-located | RELEVANCE: shared=['bless', 'intro', 'small'] | TOPIC: quote_hits=0 not-located
S606 LOCATE FAIL BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: https://england.prm.ox.ac.uk/englishness-loop-of-rowan-tree.html url-reflects-quote | BOILER: not-located | RELEVANCE: shared=['loop', 'rowan', 'tree'] | TOPIC: quote_hits=1 not-located
S607 LOCATE FAIL BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: https://nationalmuseet.dk/en/exhibitions/the-power-of-amulets-luck-fear-and-magic quote-absent | BOILER: not-located | RELEVANCE: shared=['amule', 'colle', 'explo'] | TOPIC: quote_hits=2 not-located
S608 LOCATE PASS BOILER FAIL RELEVANCE PASS TOPIC PASS | LOCATE: https://hearstmuseum.berkeley.edu/jewelry-against-evil/ | BOILER: quote-is-title-heading-or-meta | RELEVANCE: shared=['carne', 'neckl', 'tomb'] | TOPIC: quote_hits=1 function_words=8 page_hits=6 page_terms=6 need=1/2/3/2
S609 LOCATE FAIL BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: https://www.horniman.ac.uk/story/magic-charms-and-amulets/ url-reflects-quote | BOILER: not-located | RELEVANCE: shared=['corni', 'golds', 'helen'] | TOPIC: quote_hits=2 not-located
S610 LOCATE PASS BOILER FAIL RELEVANCE PASS TOPIC PASS | LOCATE: https://www.metmuseum.org/essays/amulets-and-talismans-from-the-islamic-world | BOILER: quote-is-title-heading-or-meta | RELEVANCE: shared=['conta', 'inscr', 'prote', 'talis'] | TOPIC: quote_hits=2 function_words=11 page_hits=43 page_terms=30 need=1/2/3/2
S611 LOCATE FAIL BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: quote under 8 words | BOILER: not-located | RELEVANCE: shared=['amule', 'found', 'museu'] | TOPIC: quote_hits=1 not-located
S612 LOCATE PASS BOILER FAIL RELEVANCE PASS TOPIC PASS | LOCATE: https://www.metmuseum.org/essays/egyptian-amulets | BOILER: quote-is-title-heading-or-meta | RELEVANCE: shared=['amule', 'belie', 'objec'] | TOPIC: quote_hits=3 function_words=8 page_hits=80 page_terms=82 need=1/2/3/2
S613 LOCATE PASS BOILER FAIL RELEVANCE PASS TOPIC PASS | LOCATE: https://www.metmuseum.org/art/collection/search/551476 | BOILER: quote-is-title-heading-or-meta | RELEVANCE: shared=['amule', 'ancie', 'popul'] | TOPIC: quote_hits=1 function_words=5 page_hits=13 page_terms=17 need=1/2/3/2
S614 LOCATE PASS BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: https://www.metmuseum.org/art/collection/search/555212 | BOILER: quote-is-title-heading-or-meta | RELEVANCE: shared=['base', 'displ', 'scara'] | TOPIC: quote_hits=0 function_words=7 page_hits=2 page_terms=14 need=1/2/3/2
S615 LOCATE FAIL BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: https://www.metmuseum.org/art/collection/search/556100 quote-absent | BOILER: not-located | RELEVANCE: shared=['1883', '1907', 'purch'] | TOPIC: quote_hits=0 not-located
S616 LOCATE PASS BOILER FAIL RELEVANCE PASS TOPIC PASS | LOCATE: https://collection.sciencemuseumgroup.org.uk/objects/co68714/amulet-of-saint-roch-to-protect-against-cholera | BOILER: quote-is-title-heading-or-meta | RELEVANCE: shared=['amule', 'oval', 'prote', 'silve'] | TOPIC: quote_hits=2 function_words=2 page_hits=22 page_terms=15 need=1/2/3/2
S617 LOCATE FAIL BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: https://collection.sciencemuseumgroup.org.uk/objects/co108064/amulet-and-charm-to-protect-against-plague-amulet url-reflects-quote | BOILER: not-located | RELEVANCE: shared=['amule', 'charm', 'prote'] | TOPIC: quote_hits=3 not-located
S618 LOCATE FAIL BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: https://collection.sciencemuseumgroup.org.uk/objects/co103142/bone-amulet-in-the-shape-of-a-hand-and-arm url-reflects-quote | BOILER: not-located | RELEVANCE: shared=['amule', 'bone', 'form', 'prote'] | TOPIC: quote_hits=1 not-located
S619 LOCATE FAIL BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: https://collection.sciencemuseumgroup.org.uk/objects/co108221/sheep-bone-amulet-worn-by-fishermen-and-sailors url-reflects-quote | BOILER: not-located | RELEVANCE: shared=['amule', 'bone', 'prote', 'sheep'] | TOPIC: quote_hits=1 not-located
S620 LOCATE PASS BOILER FAIL RELEVANCE PASS TOPIC PASS | LOCATE: https://collection.sciencemuseumgroup.org.uk/objects/co104464/amulet-to-ward-against-the-evil-eye | BOILER: quote-is-title-heading-or-meta | RELEVANCE: shared=['amule', 'evil', 'form'] | TOPIC: quote_hits=1 function_words=5 page_hits=14 page_terms=19 need=1/2/3/2
S621 LOCATE FAIL BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: quote under 8 words | BOILER: not-located | RELEVANCE: shared=['bless', 'cresc', 'small'] | TOPIC: quote_hits=0 not-located
S622 LOCATE FAIL BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: quote under 8 words | BOILER: not-located | RELEVANCE: shared=['bless', 'horne', 'small'] | TOPIC: quote_hits=0 not-located
S623 LOCATE FAIL BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: quote under 8 words | BOILER: not-located | RELEVANCE: shared=['bless', 'small', 'tongu'] | TOPIC: quote_hits=1 not-located
S624 LOCATE PASS BOILER FAIL RELEVANCE PASS TOPIC PASS | LOCATE: https://www.wessexarch.co.uk/apotropaic-marks-bath-abbey | BOILER: quote-is-title-heading-or-meta | RELEVANCE: shared=['bath', 'excav', 'recen'] | TOPIC: quote_hits=2 function_words=5 page_hits=19 page_terms=11 need=1/2/3/2
S625 LOCATE FAIL BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: quote under 8 words | BOILER: not-located | RELEVANCE: shared=['amule', 'charm', 'londo'] | TOPIC: quote_hits=2 not-located
S626 LOCATE FAIL BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: https://henry-moore.org/whats-on/a-kind-of-magic-talismans-charms-and-amulets-from-the-british-museum/ url-reflects-quote | BOILER: not-located | RELEVANCE: shared=['bring', 'kind', 'magic', 'objec'] | TOPIC: quote_hits=1 not-located
S627 LOCATE FAIL BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: https://journal.sciencemuseum.ac.uk/article/history-of-amulets/ url-reflects-quote | BOILER: not-located | RELEVANCE: shared=['amule', 'histo', 'objec'] | TOPIC: quote_hits=2 not-located
S628 LOCATE FAIL BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: quote under 8 words | BOILER: not-located | RELEVANCE: shared=['amule', 'moder', 'world'] | TOPIC: quote_hits=1 not-located
S629 LOCATE FAIL BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: https://www.horniman.ac.uk/story/hag-stones-and-lucky-charms/ quote-absent | BOILER: not-located | RELEVANCE: shared=['host', 'objec', 'vicky', 'visit'] | TOPIC: quote_hits=0 not-located
```

### snippets

```sh
timeout 900 python3 -B reports/round-59/rowcheck.py --draft /fast/scratch/hyaku/kotodama-r59/CtlNoReader59/snippets.rows.md --entry /fast/scratch/hyaku/kotodama-r59/CtlNoReader59/snippets.entry.md
```

Exit: 1

```text
S600 LOCATE FAIL BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: https://www.britishmuseum.org/collection/object/W_As1919-470 HTTPError | BOILER: not-located | RELEVANCE: shared=['carve', 'corne', 'neckl'] | TOPIC: quote_hits=0 not-located
S601 LOCATE FAIL BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: https://www.britishmuseum.org/collection/object/W_2012-6006-15 HTTPError | BOILER: not-located | RELEVANCE: shared=['amule', 'consi', 'small'] | TOPIC: quote_hits=1 not-located
S602 LOCATE FAIL BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: https://www.britishmuseum.org/collection/object/W_As1966-01-440 HTTPError | BOILER: not-located | RELEVANCE: shared=['hand', 'penda', 'shape'] | TOPIC: quote_hits=1 not-located
S603 LOCATE FAIL BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: https://www.britishmuseum.org/collection/object/E_Am1939-21-1 HTTPError | BOILER: not-located | RELEVANCE: shared=['amule', 'balan', 'silve'] | TOPIC: quote_hits=1 not-located
S604 LOCATE FAIL BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: https://www.britishmuseum.org/collection/object/H_1941-1208-1 HTTPError | BOILER: not-located | RELEVANCE: shared=['amule', 'forme', 'neckl'] | TOPIC: quote_hits=3 not-located
S605 LOCATE FAIL BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: https://www.britishmuseum.org/collection/object/E_Af1868-1001-4 HTTPError | BOILER: not-located | RELEVANCE: shared=['neckl', 'offer', 'prote', 'weare'] | TOPIC: quote_hits=0 not-located
S606 LOCATE FAIL BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: https://www.britannica.com/topic/evil-eye HTTPError | BOILER: not-located | RELEVANCE: shared=['belie', 'evil', 'glanc'] | TOPIC: quote_hits=0 not-located
S607 LOCATE PASS BOILER FAIL RELEVANCE PASS TOPIC PASS | LOCATE: https://blog.sciencemuseum.org.uk/5-amulets-for-5-senses/ | BOILER: quote-is-title-heading-or-meta | RELEVANCE: shared=['amule', 'histo', 'objec', 'prote', 'throu'] | TOPIC: quote_hits=1 function_words=7 page_hits=13 page_terms=12 need=1/2/3/2
S608 LOCATE FAIL BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: https://historicengland.org.uk/whats-new/features/discovering-witches-marks/what-are-witches-marks/ HTTPError | BOILER: not-located | RELEVANCE: shared=['mark', 'prote', 'scrib', 'usual'] | TOPIC: quote_hits=0 not-located
S609 LOCATE FAIL BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: https://historicengland.org.uk/whats-new/news/witches-marks-discovery-largest-in-britain/ HTTPError | BOILER: not-located | RELEVANCE: shared=['bigge', 'conce', 'prote'] | TOPIC: quote_hits=1 not-located
S610 LOCATE FAIL BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: https://www.nationaltrust.org.uk/discover/history/warding-off-evil-with-witch-marks quote-absent | BOILER: not-located | RELEVANCE: shared=['learn', 'marki', 'myste'] | TOPIC: quote_hits=1 not-located
S611 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://www.aub.edu.lb/museum_archeo/Pages/Amulets-&-Talismans.aspx | BOILER: root-clear https://www.aub.edu.lb/; not a title, h1 or meta label | RELEVANCE: shared=['amule', 'natur', 'objec'] | TOPIC: quote_hits=4 function_words=12 page_hits=25 page_terms=22 need=1/2/3/2
S612 LOCATE FAIL BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: https://www.horniman.ac.uk/story/magic-charms-and-amulets/ url-reflects-quote | BOILER: not-located | RELEVANCE: shared=['corni', 'golds', 'helen'] | TOPIC: quote_hits=2 not-located
S613 LOCATE PASS BOILER FAIL RELEVANCE PASS TOPIC PASS | LOCATE: https://www.metmuseum.org/essays/amulets-and-talismans-from-the-islamic-world | BOILER: quote-is-title-heading-or-meta | RELEVANCE: shared=['conta', 'inscr', 'prote', 'talis'] | TOPIC: quote_hits=2 function_words=11 page_hits=43 page_terms=30 need=1/2/3/2
S614 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://foundlingmuseum.org.uk/tokens-of-history/amulets/ | BOILER: root-clear https://foundlingmuseum.org.uk/; not a title, h1 or meta label | RELEVANCE: shared=['find', 'infor', 'littl', 'objec'] | TOPIC: quote_hits=2 function_words=6 page_hits=19 page_terms=16 need=1/2/3/2
S615 LOCATE PASS BOILER FAIL RELEVANCE PASS TOPIC PASS | LOCATE: https://www.metmuseum.org/essays/egyptian-amulets | BOILER: quote-is-title-heading-or-meta | RELEVANCE: shared=['amule', 'belie', 'objec'] | TOPIC: quote_hits=3 function_words=8 page_hits=80 page_terms=82 need=1/2/3/2
S616 LOCATE PASS BOILER FAIL RELEVANCE PASS TOPIC PASS | LOCATE: https://www.metmuseum.org/art/collection/search/551476 | BOILER: quote-is-title-heading-or-meta | RELEVANCE: shared=['amule', 'ancie', 'popul'] | TOPIC: quote_hits=1 function_words=3 page_hits=13 page_terms=17 need=1/2/3/2
S617 LOCATE PASS BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: https://www.metmuseum.org/art/collection/search/555212 | BOILER: quote-is-title-heading-or-meta | RELEVANCE: shared=['base', 'displ', 'scara'] | TOPIC: quote_hits=0 function_words=5 page_hits=2 page_terms=14 need=1/2/3/2
S618 LOCATE FAIL BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: https://www.english-heritage.org.uk/about/search-news/new-research-reveals-previously-undiscovered-witches-marks-at-gainsborough-old-hall/ url-reflects-quote | BOILER: not-located | RELEVANCE: shared=['gains', 'hall', 'prote', 'resea'] | TOPIC: quote_hits=3 not-located
S619 LOCATE PASS BOILER FAIL RELEVANCE PASS TOPIC PASS | LOCATE: https://www.wessexarch.co.uk/apotropaic-marks-bath-abbey | BOILER: quote-is-title-heading-or-meta | RELEVANCE: shared=['bath', 'excav', 'recen'] | TOPIC: quote_hits=2 function_words=5 page_hits=19 page_terms=11 need=1/2/3/2
S620 LOCATE FAIL BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: https://henry-moore.org/whats-on/a-kind-of-magic-talismans-charms-and-amulets-from-the-british-museum/ url-reflects-quote | BOILER: not-located | RELEVANCE: shared=['bring', 'kind', 'magic', 'objec'] | TOPIC: quote_hits=1 not-located
S621 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://journal.sciencemuseum.ac.uk/article/history-of-amulets/ | BOILER: root-clear https://journal.sciencemuseum.ac.uk/; not a title, h1 or meta label | RELEVANCE: shared=['foot', 'hare', 'parti'] | TOPIC: quote_hits=1 function_words=7 page_hits=311 page_terms=242 need=1/2/3/2
S622 LOCATE FAIL BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: https://record.umich.edu/articles/amulet-collection-works-its-magic-at-taubman-and-at-kelsey/ HTTPError | BOILER: not-located | RELEVANCE: shared=['amule', 'prote', 'thing'] | TOPIC: quote_hits=1 not-located
S623 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://www.londonmuseum.org.uk/collections/v/object-423977/charm-amulet/ | BOILER: root-clear https://www.londonmuseum.org.uk/; not a title, h1 or meta label | RELEVANCE: shared=['lead', 'prote', 'sheet', 'thin'] | TOPIC: quote_hits=1 function_words=11 page_hits=11 page_terms=13 need=1/2/3/2
S624 LOCATE PASS BOILER FAIL RELEVANCE PASS TOPIC PASS | LOCATE: https://collection.sciencemuseumgroup.org.uk/objects/co68714/amulet-of-saint-roch-to-protect-against-cholera | BOILER: quote-is-title-heading-or-meta | RELEVANCE: shared=['amule', 'oval', 'prote', 'silve'] | TOPIC: quote_hits=2 function_words=2 page_hits=22 page_terms=15 need=1/2/3/2
S625 LOCATE FAIL BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: https://collection.sciencemuseumgroup.org.uk/objects/co68361/oval-amulet-to-protect-against-cholera-europe-1801-1900 url-reflects-quote | BOILER: not-located | RELEVANCE: shared=['amule', 'bras', 'oval', 'prote'] | TOPIC: quote_hits=1 not-located
S626 LOCATE PASS BOILER FAIL RELEVANCE PASS TOPIC PASS | LOCATE: https://collection.sciencemuseumgroup.org.uk/objects/co107897/amulet-to-protect-against-health-problems | BOILER: quote-is-title-heading-or-meta | RELEVANCE: shared=['amule', 'metal', 'symbo'] | TOPIC: quote_hits=2 function_words=4 page_hits=11 page_terms=7 need=1/2/3/2
S627 LOCATE FAIL BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: https://collection.sciencemuseumgroup.org.uk/objects/co108064/amulet-and-charm-to-protect-against-plague-amulet url-reflects-quote | BOILER: not-located | RELEVANCE: shared=['amule', 'charm', 'prote'] | TOPIC: quote_hits=3 not-located
S628 LOCATE FAIL BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: https://collection.sciencemuseumgroup.org.uk/objects/co71938/brass-amulet-to-protect-the-wearer-from-cholera-france-1820-1880 url-reflects-quote | BOILER: not-located | RELEVANCE: shared=['bras', 'invol', 'medal', 'prote'] | TOPIC: quote_hits=0 not-located
S629 LOCATE FAIL BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: https://collection.sciencemuseumgroup.org.uk/objects/co103142/bone-amulet-in-the-shape-of-a-hand-and-arm url-reflects-quote | BOILER: not-located | RELEVANCE: shared=['amule', 'bone', 'form', 'prote'] | TOPIC: quote_hits=1 not-located
S630 LOCATE FAIL BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: https://collection.sciencemuseumgroup.org.uk/objects/co108221/sheep-bone-amulet-worn-by-fishermen-and-sailors url-reflects-quote | BOILER: not-located | RELEVANCE: shared=['amule', 'bone', 'prote', 'sheep'] | TOPIC: quote_hits=1 not-located
S631 LOCATE PASS BOILER FAIL RELEVANCE PASS TOPIC PASS | LOCATE: https://collection.sciencemuseumgroup.org.uk/objects/co102600/holy-medallion-used-as-an-amulet | BOILER: quote-is-title-heading-or-meta | RELEVANCE: shared=['amule', 'holy', 'medal'] | TOPIC: quote_hits=1 function_words=5 page_hits=16 page_terms=13 need=1/2/3/2
S632 LOCATE PASS BOILER FAIL RELEVANCE PASS TOPIC PASS | LOCATE: https://collection.sciencemuseumgroup.org.uk/objects/co104464/amulet-to-ward-against-the-evil-eye | BOILER: quote-is-title-heading-or-meta | RELEVANCE: shared=['amule', 'evil', 'form'] | TOPIC: quote_hits=1 function_words=5 page_hits=14 page_terms=19 need=1/2/3/2
S633 LOCATE PASS BOILER FAIL RELEVANCE PASS TOPIC PASS | LOCATE: https://collection.sciencemuseumgroup.org.uk/objects/co103143/coin-amulet-to-protect-against-smallpox | BOILER: quote-is-title-heading-or-meta | RELEVANCE: shared=['sauce', 'shape', 'worn'] | TOPIC: quote_hits=1 function_words=3 page_hits=12 page_terms=9 need=1/2/3/2
S634 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://islamicworld.britishmuseum.org/collection/RRM46563 | BOILER: root-clear https://islamicworld.britishmuseum.org/; not a title, h1 or meta label | RELEVANCE: shared=['belie', 'power', 'prote'] | TOPIC: quote_hits=1 function_words=3 page_hits=11 page_terms=6 need=1/2/3/2
S635 LOCATE FAIL BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: https://collectionswa.net.au/items/ccf7ab91-9a48-4cff-b0e5-0df9812da0f0 quote-absent | BOILER: not-located | RELEVANCE: shared=['fatim', 'hamsa', 'hand'] | TOPIC: quote_hits=1 not-located
S636 LOCATE FAIL BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: https://www.juedisches-museum-muenchen.de/en/exhibitions/archive/do-you-believe-in-the-evil-eye URLError | BOILER: not-located | RELEVANCE: shared=['peopl', 'prote', 'tried'] | TOPIC: quote_hits=0 not-located
```

### structural

```sh
timeout 900 python3 -B reports/round-59/rowcheck.py --draft /fast/scratch/hyaku/kotodama-r59/CtlNoReader59/structural.rows.md --entry /fast/scratch/hyaku/kotodama-r59/CtlNoReader59/structural.entry.md
```

Exit: 1

```text
S600 LOCATE PASS BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: https://www.metmuseum.org/essays/egyptian-amulets | BOILER: quote-on-root https://www.metmuseum.org/ | RELEVANCE: shared=['1000', 'avenu', 'cultu', 'fifth'] | TOPIC: quote_hits=0 function_words=4 page_hits=80 page_terms=82 need=1/2/3/2
S601 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC FAIL | LOCATE: https://www.metmuseum.org/art/collection/search/551476 | BOILER: root-clear https://www.metmuseum.org/; not a title, h1 or meta label | RELEVANCE: shared=['colle', 'searc', 'wedja'] | TOPIC: quote_hits=2 function_words=1 page_hits=13 page_terms=17 need=1/2/3/2
S602 LOCATE PASS BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: https://www.metmuseum.org/art/collection/search/551476 | BOILER: quote-on-root https://www.metmuseum.org/ | RELEVANCE: shared=['1000', 'avenu', 'cultu', 'fifth'] | TOPIC: quote_hits=0 function_words=4 page_hits=13 page_terms=17 need=1/2/3/2
S603 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC FAIL | LOCATE: https://www.metmuseum.org/art/collection/search/555212 | BOILER: root-clear https://www.metmuseum.org/; not a title, h1 or meta label | RELEVANCE: shared=['colle', 'scara', 'searc'] | TOPIC: quote_hits=0 function_words=3 page_hits=2 page_terms=14 need=1/2/3/2
S604 LOCATE PASS BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: https://www.metmuseum.org/art/collection/search/555212 | BOILER: quote-on-root https://www.metmuseum.org/ | RELEVANCE: shared=['1000', 'avenu', 'cultu', 'fifth'] | TOPIC: quote_hits=0 function_words=4 page_hits=2 page_terms=14 need=1/2/3/2
S605 LOCATE PASS BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: https://www.metmuseum.org/art/collection/search/556100 | BOILER: quote-on-root https://www.metmuseum.org/ | RELEVANCE: shared=['1000', 'avenu', 'cultu', 'fifth'] | TOPIC: quote_hits=0 function_words=4 page_hits=12 page_terms=12 need=1/2/3/2
S606 LOCATE FAIL BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: https://collection.sciencemuseumgroup.org.uk/objects/co68714/amulet-of-saint-roch-to-protect-against-cholera url-reflects-quote | BOILER: not-located | RELEVANCE: shared=['amule', 'prote', 'roch', 'saint'] | TOPIC: quote_hits=1 not-located
S607 LOCATE PASS BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: https://collection.sciencemuseumgroup.org.uk/objects/co68714/amulet-of-saint-roch-to-protect-against-cholera | BOILER: quote-on-root https://collection.sciencemuseumgroup.org.uk/ | RELEVANCE: shared=['group', 'museu', 'scien'] | TOPIC: quote_hits=0 function_words=2 page_hits=22 page_terms=15 need=1/2/3/2
S608 LOCATE PASS BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: https://collection.sciencemuseumgroup.org.uk/objects/co68714/amulet-of-saint-roch-to-protect-against-cholera | BOILER: quote-on-root https://collection.sciencemuseumgroup.org.uk/ | RELEVANCE: shared=['cooki', 'priva', 'term'] | TOPIC: quote_hits=0 function_words=2 page_hits=22 page_terms=15 need=1/2/3/2
S609 LOCATE PASS BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: https://collection.sciencemuseumgroup.org.uk/objects/co108064/amulet-and-charm-to-protect-against-plague-amulet | BOILER: quote-on-root https://collection.sciencemuseumgroup.org.uk/ | RELEVANCE: shared=['group', 'museu', 'scien'] | TOPIC: quote_hits=0 function_words=2 page_hits=45 page_terms=45 need=1/2/3/2
S610 LOCATE PASS BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: https://collection.sciencemuseumgroup.org.uk/objects/co108064/amulet-and-charm-to-protect-against-plague-amulet | BOILER: quote-on-root https://collection.sciencemuseumgroup.org.uk/ | RELEVANCE: shared=['cooki', 'priva', 'term'] | TOPIC: quote_hits=0 function_words=2 page_hits=45 page_terms=45 need=1/2/3/2
S611 LOCATE FAIL BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: https://collection.sciencemuseumgroup.org.uk/objects/co103142/bone-amulet-in-the-shape-of-a-hand-and-arm url-reflects-quote | BOILER: not-located | RELEVANCE: shared=['amule', 'bone', 'shape'] | TOPIC: quote_hits=1 not-located
S612 LOCATE PASS BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: https://collection.sciencemuseumgroup.org.uk/objects/co103142/bone-amulet-in-the-shape-of-a-hand-and-arm | BOILER: quote-on-root https://collection.sciencemuseumgroup.org.uk/ | RELEVANCE: shared=['group', 'museu', 'scien'] | TOPIC: quote_hits=0 function_words=2 page_hits=12 page_terms=11 need=1/2/3/2
S613 LOCATE PASS BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: https://collection.sciencemuseumgroup.org.uk/objects/co103142/bone-amulet-in-the-shape-of-a-hand-and-arm | BOILER: quote-on-root https://collection.sciencemuseumgroup.org.uk/ | RELEVANCE: shared=['cooki', 'priva', 'term'] | TOPIC: quote_hits=0 function_words=2 page_hits=12 page_terms=11 need=1/2/3/2
S614 LOCATE FAIL BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: https://collection.sciencemuseumgroup.org.uk/objects/co108221/sheep-bone-amulet-worn-by-fishermen-and-sailors url-reflects-quote | BOILER: not-located | RELEVANCE: shared=['amule', 'bone', 'sheep'] | TOPIC: quote_hits=1 not-located
S615 LOCATE PASS BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: https://collection.sciencemuseumgroup.org.uk/objects/co108221/sheep-bone-amulet-worn-by-fishermen-and-sailors | BOILER: quote-on-root https://collection.sciencemuseumgroup.org.uk/ | RELEVANCE: shared=['group', 'museu', 'scien'] | TOPIC: quote_hits=0 function_words=2 page_hits=16 page_terms=14 need=1/2/3/2
S616 LOCATE PASS BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: https://collection.sciencemuseumgroup.org.uk/objects/co108221/sheep-bone-amulet-worn-by-fishermen-and-sailors | BOILER: quote-on-root https://collection.sciencemuseumgroup.org.uk/ | RELEVANCE: shared=['cooki', 'priva', 'term'] | TOPIC: quote_hits=0 function_words=2 page_hits=16 page_terms=14 need=1/2/3/2
S617 LOCATE PASS BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: https://collection.sciencemuseumgroup.org.uk/objects/co104464/amulet-to-ward-against-the-evil-eye | BOILER: quote-on-root https://collection.sciencemuseumgroup.org.uk/ | RELEVANCE: shared=['group', 'museu', 'scien'] | TOPIC: quote_hits=0 function_words=2 page_hits=14 page_terms=19 need=1/2/3/2
S618 LOCATE PASS BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: https://collection.sciencemuseumgroup.org.uk/objects/co104464/amulet-to-ward-against-the-evil-eye | BOILER: quote-on-root https://collection.sciencemuseumgroup.org.uk/ | RELEVANCE: shared=['cooki', 'priva', 'term'] | TOPIC: quote_hits=0 function_words=2 page_hits=14 page_terms=19 need=1/2/3/2
S619 LOCATE PASS BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: https://www.wessexarch.co.uk/apotropaic-marks-bath-abbey | BOILER: quote-on-root https://www.wessexarch.co.uk/ | RELEVANCE: shared=['explo', 'foote', 'work'] | TOPIC: quote_hits=0 function_words=3 page_hits=19 page_terms=11 need=1/2/3/2
S620 LOCATE PASS BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: https://www.londonmuseum.org.uk/collections/v/object-423977/charm-amulet/ | BOILER: quote-on-root https://www.londonmuseum.org.uk/ | RELEVANCE: shared=['londo', 'museu', 'smith'] | TOPIC: quote_hits=0 function_words=2 page_hits=11 page_terms=13 need=1/2/3/2
S621 LOCATE FAIL BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: https://henry-moore.org/whats-on/a-kind-of-magic-talismans-charms-and-amulets-from-the-british-museum/ url-reflects-quote | BOILER: not-located | RELEVANCE: shared=['kind', 'magic', 'talis'] | TOPIC: quote_hits=3 not-located
S622 LOCATE PASS BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: https://henry-moore.org/whats-on/a-kind-of-magic-talismans-charms-and-amulets-from-the-british-museum/ | BOILER: quote-on-root https://henry-moore.org/ | RELEVANCE: shared=['henry', 'insti', 'moore'] | TOPIC: quote_hits=0 function_words=2 page_hits=20 page_terms=16 need=1/2/3/2
S623 LOCATE PASS BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: https://journal.sciencemuseum.ac.uk/article/history-of-amulets/ | BOILER: quote-on-root https://journal.sciencemuseum.ac.uk/ | RELEVANCE: shared=['board', 'edito', 'journ'] | TOPIC: quote_hits=0 function_words=5 page_hits=311 page_terms=242 need=1/2/3/2
S624 LOCATE PASS BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: https://journal.sciencemuseum.ac.uk/article/history-of-amulets/ | BOILER: quote-on-root https://journal.sciencemuseum.ac.uk/ | RELEVANCE: shared=['group', 'museu', 'scien'] | TOPIC: quote_hits=0 function_words=3 page_hits=311 page_terms=242 need=1/2/3/2
S625 LOCATE FAIL BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: https://en.natmus.dk/historical-knowledge/denmark/prehistoric-period-until-1050-ad/the-mesolithic-period/amulets/amulets-in-the-modern-world/ url-reflects-quote | BOILER: not-located | RELEVANCE: shared=['1050', 'perio', 'prehi'] | TOPIC: quote_hits=2 not-located
S626 LOCATE PASS BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: https://en.natmus.dk/historical-knowledge/denmark/prehistoric-period-until-1050-ad/the-mesolithic-period/amulets/amulets-in-the-modern-world/ | BOILER: quote-on-root https://en.natmus.dk/ | RELEVANCE: shared=['køben', 'natio', 'veste'] | TOPIC: quote_hits=0 function_words=4 page_hits=13 page_terms=10 need=1/2/3/2
S627 LOCATE FAIL BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: https://www.horniman.ac.uk/story/hag-stones-and-lucky-charms/ url-reflects-quote | BOILER: not-located | RELEVANCE: shared=['garde', 'horni', 'museu'] | TOPIC: quote_hits=0 not-located
```

### fetch-abuse

```sh
timeout 900 python3 -B reports/round-59/rowcheck.py --draft /fast/scratch/hyaku/kotodama-r59/CtlNoReader59/fetch-abuse.rows.md --entry /fast/scratch/hyaku/kotodama-r59/CtlNoReader59/fetch-abuse.entry.md
```

Exit: 1

```text
S600 LOCATE FAIL BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: quote under 8 words | BOILER: not-located | RELEVANCE: shared=['excep', 'pazuz', 'seem'] | TOPIC: quote_hits=0 not-located
S601 LOCATE FAIL BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: quote under 8 words | BOILER: not-located | RELEVANCE: shared=['excep', 'pazuz', 'seem'] | TOPIC: quote_hits=0 not-located
S602 LOCATE FAIL BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: quote under 8 words | BOILER: not-located | RELEVANCE: shared=['excep', 'pazuz', 'seem'] | TOPIC: quote_hits=0 not-located
S603 LOCATE FAIL BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: quote under 8 words | BOILER: not-located | RELEVANCE: shared=['excep', 'pazuz', 'seem'] | TOPIC: quote_hits=0 not-located
S604 LOCATE FAIL BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: quote under 8 words | BOILER: not-located | RELEVANCE: shared=['excep', 'pazuz', 'seem'] | TOPIC: quote_hits=0 not-located
```

### fetch-v2

```sh
timeout 900 python3 -B reports/round-59/rowcheck.py --draft /fast/scratch/hyaku/kotodama-r59/CtlNoReader59/fetch-v2.rows.md --entry /fast/scratch/hyaku/kotodama-r59/CtlNoReader59/fetch-v2.entry.md
```

Exit: 1

```text
S600 LOCATE FAIL BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: https://www.britishmuseum.org/collection/object/W_As1919-470 quote-absent; https://web.archive.org/web/20171121161933id_/https://www.metmuseum.org/exhibitions/listings/2014/assyria-to-iberia/blog/post | BOILER: not-located | RELEVANCE: shared=['amule', 'image'] | TOPIC: quote_hits=2 not-located
S601 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://www.metmuseum.org/exhibitions/listings/2014/assyria-to-iberia/blog/posts/pazuzu | BOILER: root-clear https://www.metmuseum.org/; not a title, h1 or meta label | RELEVANCE: shared=['amule', 'image'] | TOPIC: quote_hits=2 function_words=6 page_hits=10 page_terms=31 need=1/2/3/2
S602 LOCATE FAIL BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: https://www.britishmuseum.org/collection/object/W_2012-6006-15 HTTPError; https://web.archive.org/web/20171121161933id_/https://www.metmuseum.org/ URLError | BOILER: not-located | RELEVANCE: shared=['amule', 'image'] | TOPIC: quote_hits=2 not-located
S603 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://www.metmuseum.org/exhibitions/listings/2014/assyria-to-iberia/blog/posts/pazuzu | BOILER: root-clear https://www.metmuseum.org/; not a title, h1 or meta label | RELEVANCE: shared=['amule', 'image'] | TOPIC: quote_hits=2 function_words=6 page_hits=10 page_terms=31 need=1/2/3/2
S604 LOCATE FAIL BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: https://web.archive.org/web/19000101000000id_/https://www.metmuseum.org/exhibitions/listings/2014/assyria-to-iberia/blog/posts/pazuzu URLError | BOILER: not-located | RELEVANCE: shared=['amule', 'image'] | TOPIC: quote_hits=2 not-located
```

## Reproduction and operational bounds

Fixture copies are adjacent under `.ufo/waves/round-59/control/CtlNoReader59/` (rows and entry stubs, with `replay.py`). They contain no fetched page bodies. Clone exactly as assigned into a fresh scratch name, then run the replay script there; it obtains the two base corpus files from the declaration commit and does not modify a counter. Example after the prescribed clone/checkout:

```sh
timeout 930 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-59/control/CtlNoReader59/replay.py /fast/scratch/hyaku/kotodama-r59/CtlNoReader59/clone snippets
```

One tool invocation automatically backgrounded the first `fetch-padded` attempt at 60 seconds despite foreground execution being requested; it was explicitly cancelled as `proc://bg_2603/kill`. No result from that cancelled attempt is claimed. The completed synchronous invocation retained above used the same frozen counter. All started jobs have ended or were killed. No lane-root, sibling-lane, or fleet-repo write was made.

## Counterexample, impacted axes, smallest safe correction

1. **Fixable FETCH-59 identity defect:** S603 locates on an unrelated second live page; S601 accepts a fabricated, unused timestamp. Evidence: pasted `fetch-v2` row output and source-cell fixture bytes; `reopen-quote.py:170-191,201-206` accepts up to four arbitrary source URLs and `rowcheck.py:314-325` adds no source-cell grammar check. Impact: provenance/freshness and calibration; [INFERENCE] if used for learning admission, source fidelity/depth and claimed coverage could be overstated. **Smallest correction:** before locating, require exactly one live URL followed by at most one `web.archive.org/web/<14 digits>id_/` URL whose decoded original identifies that same live page. If the capture is claimed as actually opened, verify its successful response and resolved capture identity/timestamp, not merely the presence of digits. Normalize and check root captures as roots after redirects. Keep this a frozen-counter revision before data, not an exception after a source fails.

2. **No-reader mechanical limitation, not a demonstrated full-counter defeat:** five search-only rows pass LOCATE/BOILER/RELEVANCE/TOPIC, and every lexical synthetic teaching passes RELEVANCE. Evidence: S611/S614/S621/S623/S634 and their pasted teachings. Impact: depth and calibration; coverage-by-file count is not evidence of substantive reading. **Smallest correction:** keep semantic SUPPORT independent and have its planted controls include genuine body snippets paired with vacuous or unsupported teachings/entry claims; require reviewers to name nearby context that distinguishes the stated claim from an alternative. If actual source opening/reading is part of the acceptance claim, make that provenance obligation explicit in the pre-data predicate rather than presenting ACCESS (a marker-word scan) as reading evidence. Quote presence alone cannot prove that someone read it.

All full controls were rejected, so this review does not declare claim C defeated. Nor should a positive filename/row count be traded for weaker source fidelity; such an axis trade is for the canonical Rust judge to reject, not for this critic to admit. No counter changes, adjudication, integration, or shipment were performed.

counter weaknesses: arbitrary extra source URLs and unvalidated listed capture provenance are mechanically accepted at row level; five raw search snippets also clear all four row legs without body reading. Enforce the declared live/same-page-capture grammar and preserve semantic/contextual SUPPORT discrimination before data. Full-counter mechanical sufficiency was not met by any of the four landings tried.
