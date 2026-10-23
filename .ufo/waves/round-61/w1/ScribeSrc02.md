# Round 61 W1 — ScribeSrc02 source findings

## Behavior and axis

**Coverage.** Two candidate source rows and two one-clause entry lines are drafted for Ötzi’s shoes. No locatable source was found for the ancient Egyptian sandals subtopic after ordinary requests to the British Museum, Brooklyn Museum, and UCL/Petrie endpoints; that gap is reported without invented quotes or rows. IDs remain `S6??` for the L1 integration owner: concurrent source reports already contain overlapping proposed ID ranges. These are drafts, not registry or corpus changes.

## Draft source rows and entry lines

### Ötzi’s shoes

**SOURCES row (draft):**

```text
| S6?? | South Tyrol Museum of Archaeology (date not shown), “New reconstruction of the Iceman’s shoes and coat” — https://www.iceman.it/en/news/new-reconstruction-of-the-iceman-s-shoes-and-coat_440; capture https://web.archive.org/web/20250915132459id_/https://www.iceman.it/en/news/new-reconstruction-of-the-iceman-s-shoes-and-coat_440 | news | A | museum account of the Iceman shoe replica, including hay stuffing | Article text: “To keep his feet warm in the snow the Iceman also stuffed his shoes with hay.” | The museum’s account says hay was stuffed in the Iceman’s shoes to keep his feet warm in snow. | mined | 2026-10-23 | 180d | corpus/knowledge/culture-material/footwear-codes-terminology.md |
```

**Entry line (draft):**

```text
- Hay in the Iceman’s shoes kept his feet warm in snow. (S6??)
```

**Gate line (draft):**

```text
- S6?? | https://www.iceman.it/en/news/new-reconstruction-of-the-iceman-s-shoes-and-coat_440 | 2026-10-23 | “To keep his feet warm in the snow the Iceman also stuffed his shoes with hay.”
```

**SOURCES row (draft):**

```text
| S6?? | Eva IJsveld, “Reconstructing Ötzi’s shoes,” EXARC Journal Issue 2023/2, 2023-06-17 — https://exarc.net/issue-2023-2/at/reconstructing-otzis-shoes; capture https://web.archive.org/web/20230616010106id_/https://exarc.net/issue-2023-2/at/reconstructing-otzis-shoes | paper | B | reviewed reconstruction article describing shoe materials and attachment | Description of the shoes: “The shoes consist of a bearskin sole, deerskin upper leather attached to the sole with a thin cow hide strap.” | The article describes a bearskin sole, deerskin upper leather, and a thin cowhide strap attaching the upper to the sole. | mined | 2026-10-23 | 180d | corpus/knowledge/culture-material/footwear-codes-terminology.md |
```

**Entry line (draft):**

```text
- Ötzi’s shoes joined a bearskin sole to deerskin upper leather with a thin cowhide strap. (S6??)
```

**Gate line (draft):**

```text
- S6?? | https://exarc.net/issue-2023-2/at/reconstructing-otzis-shoes | 2026-10-23 | “The shoes consist of a bearskin sole, deerskin upper leather attached to the sole with a thin cow hide strap.”
```

## Locator and registry evidence

The locator commands were run from the lane root, each with the 300-second cap. Both live URL quotes were located (exit 0):

```text
timeout 300 python3 -B reports/round-61/reopen-quote.py 'https://www.iceman.it/en/news/new-reconstruction-of-the-iceman-s-shoes-and-coat_440' 'To keep his feet warm in the snow the Iceman also stuffed his shoes with hay.'; status=$?; echo exit=$?
LOCATED https://www.iceman.it/en/news/new-reconstruction-of-the-iceman-s-shoes-and-coat_440
exit=0

timeout 300 python3 -B reports/round-61/reopen-quote.py 'https://exarc.net/issue-2023-2/at/reconstructing-otzis-shoes' 'The shoes consist of a bearskin sole, deerskin upper leather attached to the sole with a thin cow hide strap.'; status=$?; echo exit=$?
LOCATED https://exarc.net/issue-2023-2/at/reconstructing-otzis-shoes
exit=0
```

`functions.grep` checks against `/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md`, case-insensitive, returned `No matches found.` for each full URL pattern:

- `https://www\.iceman\.it/en/news/new-reconstruction-of-the-iceman-s-shoes-and-coat_440`
- `https://exarc\.net/issue-2023-2/at/reconstructing-otzis-shoes`

The `archive.org/wayback/available` requests for these two live URLs returned HTTP 429. Ordinary `web.archive.org/cdx/search/cdx` requests then reported existing successful snapshots: Iceman `20250915132459` and EXARC `20230616010106`. These `id_` captures are included in the draft source cells. LOCATE was run on the live URLs, not on the captures; the live quotes located.

## Egyptian sandals search — no retained source

No qualifying quote, source row, entry clause, or Gate line is drafted for this subtopic. Attempts and outcomes:

- British Museum collection search pages for `sandal` and `Egyptian sandals` yielded only the generic Collections Search page text, not an individual record or quote. Ordinary GETs to `https://www.britishmuseum.org/api/search?term=sandal`, `...?term=sandals`, and `...?term=Egyptian%20sandals` returned JSON with `hits.total: 0`.
- Brooklyn Museum Open Collection search URLs (singular and plural sandal queries) and its API documentation URL returned HTTP 429. A separate ordinary `urllib` GET of the plural search URL also returned HTTP 429. `archive.org/wayback/available` returned `archived_snapshots: {}` for the search URL; `web.archive.org/cdx/search/cdx` returned `[]`. **Rate-limit access block met, not passed; no bypass attempted.**
- The Digital Egypt root at UCL was readable but supplied no footwear quote. `garments/shoes.html`, `garments/sandals.html`, and `garments/index.html` returned HTTP 404; `alphabet.html`, `Welcome.html`, and `sitemap.xml` returned HTTP 403. The Petrie catalogue root and `search.aspx?search=sandal` returned HTTP 500. Wayback availability for the catalogue query returned no snapshots; CDX for the old Digital Egypt shoes URL returned `[]`. **403 access block met, not passed; no bypass attempted.**
- A Met collection API lead returned HTTP 410 and was not retained. Ordinary Google/Bing discovery requests yielded no relevant result. No browser, login, paywall or challenge workaround was used.

## Touched surfaces, gates, and limits

- **Touched:** only this requested report artifact. No product file, `corpus/SOURCES.md`, knowledge entry, README, tool, counter, judge, or build surface was changed. No tool was installed and no scratch file was written.
- **Gates exercised:** live quote locator for two Ötzi sources; full host/path registry reuse grep for both. No `ACCEPT-C-61`, `ACCEPT-O-61`, build, or test was run. This is not a pass claim for C or O.
- **Limits:** the two Ötzi drafts do not satisfy the full 20-row coverage floor; the Egyptian subtopic remains unfilled by this seat. The task-provided revision is `78ad4b176695e9fcd490ab607cb8218e2ce62738`; it was not independently verified. The two quoted archive captures were identified by CDX, but only the live pages were locator-tested. ID placeholders are left for L1 to resolve against concurrent drafts.

## Artifact path

`/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-61/w1/ScribeSrc02.md`
