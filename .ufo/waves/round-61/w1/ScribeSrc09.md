# ScribeSrc09 — Round 61, wave 1 source findings

## Behavior and scope

Prepared six draft source rows and six one-source bullet clauses for the assigned footwear sub-topics: Russian/Slavic bast shoes, medieval pattens/overshoes, and Hermes/Mercury winged footwear. Each selected source was opened by ordinary static reading, its quoted anchor was LOCATED by the round-61 locator on the live URL, and a host+path search of the current `corpus/SOURCES.md` returned no match. These are source drafts only; no SOURCES row, entry, Gate section, index, or product file was integrated by this seat.

Axes tracked: coverage, source provenance/tier, quote location, and registry freshness.

## Gates and verification

- Six kept-source quote locators: all `LOCATED`, exit 0 (commands and full output lines below).
- Six kept source URLs: each host+path search against `/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md` returned `No matches found.` (patterns/output below).
- `ACCEPT-C-61`, `ACCEPT-O-61`, build, lint, and tests: **not run**. This seat did not integrate the entry or lint tool, and its scope was source research/drafting; therefore no full claim predicate is reported as passing.
- No tool installed or updated. No git/jj commands, no source-registry edits, and no external browser/challenge-solving used. The supplied lane revision `78ad4b176695e9fcd490ab607cb8218e2ce62738` was not independently checked with git/jj.

## Draft source rows, entry clauses, and Gate lines

Rows use the exact requested 11-data-cell form (13 fields after `split('|')` including edge empties), with `180d` as requested. Locator words identify the anchor within the opened page.

### 1. Russian/Slavic bast shoes (lapti)

Source registry search: pattern `polotsk-local.museum.by/en/node/45054` → `No matches found.`

```text
| S668 | Bast shoes, Museum of Local Studies (published 2018-11-01) — https://polotsk-local.museum.by/en/node/45054 | docs | A | peasant bast-shoe materials and weaving in the Belarusian museum's scope | opening body paragraph on bast shoes: "Traditional type of peasant shoes were bast shoes. They are woven from vine or linden bast (soft bark)." | Bast shoes were woven from vine or linden bast, described as soft bark. | mined | 2026-10-23 | 180d | corpus/knowledge/culture-material/footwear-codes-terminology.md |
```

- Peasant bast shoes were woven from vine or linden bast. (S668)
- S668 | https://polotsk-local.museum.by/en/node/45054 | 2026-10-23 | "Traditional type of peasant shoes were bast shoes. They are woven from vine or linden bast (soft bark)."

Source registry search: pattern `collections.readingmuseum.org.uk/index.asp` → `No matches found.`

```text
| S669 | Birch bark, Reading Museum, object REDMG : 2007.1228.1 (date not shown) — https://collections.readingmuseum.org.uk/index.asp?page=record&mwsquery=%7Btotopic%7D=%7BWorld%20Collection:%20Ornamentation%7D&filename=REDMG&hitsStart=156 | docs | A | museum record for a Finnish birch-bark shoe and the page's comparison with Russian lapti | Birch bark section, explanatory paragraph: "Shoes made from woven birch bark are found throughout Scandinavia, Siberia, and the Baltics. In Russia they are known as 'lapti' shoes." | The museum says woven birch-bark shoes occur in Scandinavia, Siberia and the Baltics, and are known as lapti shoes in Russia. | mined | 2026-10-23 | 180d | corpus/knowledge/culture-material/footwear-codes-terminology.md |
```

- In Russia, woven birch-bark shoes are known as lapti. (S669)
- S669 | https://collections.readingmuseum.org.uk/index.asp?page=record&mwsquery=%7Btotopic%7D=%7BWorld%20Collection:%20Ornamentation%7D&filename=REDMG&hitsStart=156 | 2026-10-23 | "Shoes made from woven birch bark are found throughout Scandinavia, Siberia, and the Baltics. In Russia they are known as 'lapti' shoes."

The Reading Museum page identifies the pictured/catalogued shoe as from Finland; S669 uses only its separate explicit statement about the Russian name and does not present that Finnish object as Russian.

### 2. Medieval pattens and overshoes

Source registry search: pattern `londonmuseum.org.uk/collections/v/object-731922/wood-worked-wood-patten` → `No matches found.`

```text
| S670 | Wood, worked wood, patten, London Museum (production date: Medieval; late Medieval; 15th century) — https://www.londonmuseum.org.uk/collections/v/object-731922/wood-worked-wood-patten/ | docs | A | London Museum patten description and wet-weather use; object dated to the 15th century | Description, opening sentences: "Wooden patten. This was a type of overshoe worn to raise the foot above ground during wet weather." | The museum describes a wooden patten as an overshoe worn to raise the foot above ground in wet weather. | mined | 2026-10-23 | 180d | corpus/knowledge/culture-material/footwear-codes-terminology.md |
```

- A wooden patten was an overshoe worn to raise the foot above ground in wet weather. (S670)
- S670 | https://www.londonmuseum.org.uk/collections/v/object-731922/wood-worked-wood-patten/ | 2026-10-23 | "Wooden patten. This was a type of overshoe worn to raise the foot above ground during wet weather."

Source registry search: pattern `museum.ie/collections/collection/antiquity-68544` → `No matches found.`

```text
| S671 | Wooden patten with leather shoe, National Museum of Ireland Collections Online (production period: Late Medieval; page date not shown) — https://www.museum.ie/collections/collection/antiquity-68544/ | docs | A | late-medieval patten identity and wear over ordinary shoes | Description paragraph, opening sentences: "This piece of footwear is a patten. It is one of a pair (1945:61.2). These were worn over a pair of normal shoes." | The museum identifies a patten in a pair, worn over normal shoes. | mined | 2026-10-23 | 180d | corpus/knowledge/culture-material/footwear-codes-terminology.md |
```

- A patten was worn over a pair of normal shoes. (S671)
- S671 | https://www.museum.ie/collections/collection/antiquity-68544/ | 2026-10-23 | "This piece of footwear is a patten. It is one of a pair (1945:61.2). These were worn over a pair of normal shoes."

### 3. Hermes/Mercury winged footwear (talaria)

Source registry search: pattern `theoi.com/Olympios/HermesTreasures.html` → `No matches found.`

```text
| S672 | Hermes Estate & Attributes, Theoi Greek Mythology (author and date not shown) — https://www.theoi.com/Olympios/HermesTreasures.html | docs | C | Theoi's summary of Hermes' winged boots and Greek/Latin terminology | WINGED BOOTS & CAP OF HERMES section, first sentence: "Hermes wore winged, short leather boots called by the Greeks pteroeis pedila and by the Romans talaria." | Theoi says Hermes wore winged short leather boots, called pteroeis pedila by Greeks and talaria by Romans. | mined | 2026-10-23 | 180d | corpus/knowledge/culture-material/footwear-codes-terminology.md |
```

- Hermes' talaria were winged leather boots. (S672)
- S672 | https://www.theoi.com/Olympios/HermesTreasures.html | 2026-10-23 | "Hermes wore winged, short leather boots called by the Greeks pteroeis pedila and by the Romans talaria."

Source registry search: pattern `penelope.uchicago.edu/Thayer/E/Roman/Texts/secondary/SMIGRA` → `No matches found.`

```text
| S673 | “Talaria,” James Yates in William Smith, Dictionary of Greek and Roman Antiquities, John Murray, London (1875), hosted by LacusCurtius — https://penelope.uchicago.edu/Thayer/E/Roman/Texts/secondary/SMIGRA*/Talaria.html | book | B | Yates's 19th-century account of Mercury's winged sandals in ancient art | p.1094, first paragraph on artistic representations: "commonly done by representing him with sandals, which have wings fastened to them on each side over the ancles." | Yates describes sandals in ancient art with wings fastened on each side over the ankles. | mined | 2026-10-23 | 180d | corpus/knowledge/culture-material/footwear-codes-terminology.md |
```

- Sandals had wings fastened on each side above the ankles. (S673)
- S673 | https://penelope.uchicago.edu/Thayer/E/Roman/Texts/secondary/SMIGRA*/Talaria.html | 2026-10-23 | "commonly done by representing him with sandals, which have wings fastened to them on each side over the ancles."

## Exact live locator commands and stdout

Each command was run with a 300-second process timeout; the line below is its full stdout followed by the observed shell exit code.

1. `timeout 300 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-61/reopen-quote.py 'https://polotsk-local.museum.by/en/node/45054' 'Traditional type of peasant shoes were bast shoes. They are woven from vine or linden bast (soft bark).'; echo exit=$?`
   ```text
   LOCATED https://polotsk-local.museum.by/en/node/45054
   exit=0
   ```
2. `timeout 300 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-61/reopen-quote.py 'https://collections.readingmuseum.org.uk/index.asp?page=record&mwsquery=%7Btotopic%7D=%7BWorld%20Collection:%20Ornamentation%7D&filename=REDMG&hitsStart=156' "Shoes made from woven birch bark are found throughout Scandinavia, Siberia, and the Baltics. In Russia they are known as 'lapti' shoes."; echo exit=$?`
   ```text
   LOCATED https://collections.readingmuseum.org.uk/index.asp?page=record&mwsquery=%7Btotopic%7D=%7BWorld%20Collection:%20Ornamentation%7D&filename=REDMG&hitsStart=156
   exit=0
   ```
3. `timeout 300 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-61/reopen-quote.py 'https://www.londonmuseum.org.uk/collections/v/object-731922/wood-worked-wood-patten/' 'Wooden patten. This was a type of overshoe worn to raise the foot above ground during wet weather.'; echo exit=$?`
   ```text
   LOCATED https://www.londonmuseum.org.uk/collections/v/object-731922/wood-worked-wood-patten/
   exit=0
   ```
4. `timeout 300 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-61/reopen-quote.py 'https://www.museum.ie/collections/collection/antiquity-68544/' 'This piece of footwear is a patten. It is one of a pair (1945:61.2). These were worn over a pair of normal shoes.'; echo exit=$?`
   ```text
   LOCATED https://www.museum.ie/collections/collection/antiquity-68544/
   exit=0
   ```
5. `timeout 300 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-61/reopen-quote.py 'https://www.theoi.com/Olympios/HermesTreasures.html' 'Hermes wore winged, short leather boots called by the Greeks pteroeis pedila and by the Romans talaria.'; echo exit=$?`
   ```text
   LOCATED https://www.theoi.com/Olympios/HermesTreasures.html
   exit=0
   ```
6. `timeout 300 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-61/reopen-quote.py 'https://penelope.uchicago.edu/Thayer/E/Roman/Texts/secondary/SMIGRA*/Talaria.html' 'commonly done by representing him with sandals, which have wings fastened to them on each side over the ancles.'; echo exit=$?`
   ```text
   LOCATED https://penelope.uchicago.edu/Thayer/E/Roman/Texts/secondary/SMIGRA*/Talaria.html
   exit=0
   ```

## Non-retained research and limits

- Artefact/Culture Russia page `https://ar.culture.ru/en/subject/lapti-41`: ordinary live read returned HTTP 403. `timeout 300 curl -s 'https://archive.org/wayback/available?url=https%3A%2F%2Far.culture.ru%2Fen%2Fsubject%2Flapti-41'` returned an available 2024-11-10 snapshot. Static reading of `https://web.archive.org/web/20241110113016id_/https://ar.culture.ru/en/subject/lapti-41` exposed the English article, but the required locator attempt returned `NOT_LOCATED https://web.archive.org/web/20241110113016id_/https://ar.culture.ru/en/subject/lapti-41 HTTPError`, exit 1. Consequently no Artefact row was kept. The corresponding availability query for `lapti-35` returned `{"url": "https://ar.culture.ru/en/subject/lapti-35", "archived_snapshots": {}}`. The English female-lapti and Bugulma URLs also had empty availability results. This access challenge was met (403) but not passed; no challenge was solved.
- The selected alternatives for the Russian/Slavic slot are the two opened museum pages S668–S669. A Traditional Shoes Museum page (`http://traditionalshoes.com/en/archives/17`) did LOCATE the search-result quote `Lapti are the traditional bast shoes of the Russian peasants.` (exit 0), but was not retained because the selected museum records provide stronger institutional provenance. Its static-reader attempt resolved to an alternate comments feed; an HTTPS read failed with `ERR_TLS_CERT_ALTNAME_INVALID`.
- PAS exploration surfaced post-medieval patten records, including record 660966 dated to the 18th–19th century, not a securely medieval find. Direct reading of `https://finds.org.uk/database/artefacts/record/id/660966` returned HTTP 403 and its locator returned `NOT_LOCATED https://finds.org.uk/database/artefacts/record/id/660966 HTTPError`, exit 1. No PAS quote was retained or represented as medieval. London Museum and National Museum of Ireland provide the two located patten sources.
- British Museum record `https://www.britishmuseum.org/collection/object/G_1864-1021-1` was returned as HTTP 403 by static reading; its locator returned `NOT_LOCATED https://www.britishmuseum.org/collection/object/G_1864-1021-1 HTTPError`, exit 1. The archive-availability request returned HTTP 429, so no capture was used. The located Yates/Smith historical reference (S673) was used instead of claiming an unlocated museum record.
- Other unretained discovery attempts: the Russian History Museum article returned HTTP 429 on read and `Too many requests. Please retry in one minute.` by ordinary curl; the Fitzwilliam Mercury/Hermes page returned HTTP 503 on both tried host forms; the Met object page returned HTTP 429. No quote from these candidates was used.

## Touched surfaces, out of scope, and artifacts

- Touched: only this report file. No product, counter, registry, corpus entry, or documentation source file was edited. The scratch directory `/fast/scratch/hyaku/kotodama-r61/KotodamaR61.ScribeSrc09/` was created; no files were written there.
- Out of scope: integrating S668–S673 into `corpus/SOURCES.md`, drafting the complete knowledge entry/Gate section, the remaining C coverage and the ≥20-source floor, `corpus/README.md`, ACCEPT-C/ACCEPT-O controls, the O lint tool, and any build/test/lint run.
- Known limits: source-draft evidence is verified, but it is not evidence that the full C predicate passes. The 15th-century London patten is a dated object record; the Irish record is identified as late medieval. The PAS records actually found in the attempted results were later/post-medieval. The Theoi row is tier C (lead only); S673 is a historical secondary reference, not an ancient primary text.
- Artifact path: `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-61/w1/ScribeSrc09.md`.
