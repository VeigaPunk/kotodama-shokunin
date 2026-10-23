# ScoutConcealedObjects — concealed protective objects in buildings (S622–S623)

Subtopic: concealed shoes, witch bottles and related hidden deposits as building protection.
Seat scope: claim C source seat, 2 rows offered, ids S622–S623 only. No installs this session.

## Registry rows

| S622 | Museum Wales (Amgueddfa Cymru), "Witch-bottles and healing charms", blog post, 16 June 2011 — https://museum.wales/blog/1203/Witch-bottles-and-healing-charms/ (direct, HTTP 200, 88910 bytes) | docs | A | Welsh witch-bottle practice: what goes into the vessel and the reasoning behind it | Section Witch-bottles and pots, body sentence: "The bottle symbolised the witch's bladder, and so the sharp objects were believed to cause her much pain." | A witch bottle stood for the witch's bladder, so the sharp objects sealed inside it were meant to hurt her. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md |
| S623 | Shawcross, Rebecca. 2022. "Concealed Shoes Revealed", Footwear Research Network, 4 February 2022 — https://footwearresearchnetwork.org/articles/concealed-shoes-revealed (direct, HTTP 200, 248354 bytes) | docs | B | concealed shoes in English buildings read as apotropaic devices, with the evidence caveats | Section on why shoes were concealed, the accepted theory: "shoes are always highly worn, often patched and repaired they act as apotropaic devices to protect the house and its occupants from malicious evil forces" | Worn, patched shoes hidden in a house were read as apotropaic devices that shielded its occupants from malicious forces. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md |

## Gate

- S622 — https://museum.wales/blog/1203/Witch-bottles-and-healing-charms/ — accessed 2026-10-23 — Section Witch-bottles and pots, body sentence: “The bottle symbolised the witch's bladder, and so the sharp objects were believed to cause her much pain.” Grounds: A witch bottle stood for the witch's bladder, so the sharp objects sealed inside it were meant to hurt her. Seat: ScoutConcealedObjects.
- S623 — https://footwearresearchnetwork.org/articles/concealed-shoes-revealed — accessed 2026-10-23 — Section on why shoes were concealed, the accepted theory: “shoes are always highly worn, often patched and repaired they act as apotropaic devices to protect the house and its occupants from malicious evil forces”. Grounds: Worn, patched shoes hidden in a house were read as apotropaic devices that shielded its occupants from malicious forces. Seat: ScoutConcealedObjects.

## rowcheck output (verbatim, exit 0)

```
S622 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://museum.wales/blog/1203/Witch-bottles-and-healing-charms/ | BOILER: root-clear https://museum.wales/; not a title, h1 or meta label | RELEVANCE: shared=['bladd', 'bottl', 'objec', 'sharp', 'witch'] | TOPIC: quote_hits=1 function_words=4 page_hits=7 page_terms=9 need=1/2/3/2
S623 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://footwearresearchnetwork.org/articles/concealed-shoes-revealed | BOILER: root-clear https://footwearresearchnetwork.org/; not a title, h1 or meta label | RELEVANCE: shared=['apotr', 'devic', 'force', 'house', 'malic', 'occup'] | TOPIC: quote_hits=2 function_words=7 page_hits=5 page_terms=3 need=1/2/3/2
EXIT=0
```

Command run: `cd /fast/scratch/hyaku/kotodama-r59/ScoutConcealedObjects && timeout 900 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-59/rowcheck.py --draft .../rows.md --entry .../stub.md`

## draft sentences

In the Welsh witch-bottle practice the bottle was understood to stand for the witch's bladder, so the sharp objects inside it were meant to cause her pain (S622).
The charm works by correspondence: the vessel stands in for the witch, and what is enclosed in it is felt by her (S622).
Concealed shoes are usually heavily worn and patched, and the leading explanation reads them as apotropaic devices that protect a house and its occupants from malicious forces (S623).
The protection is aimed at the house and its occupants rather than at one person alone (S623).

## What the opened pages carry (for the entry, beyond the row quotes)

Observed on the Museum Wales page (same page as S622): the Buckley pot found buried at the foot of an old yew tree at Allt-y-Rhiw farmhouse near Llansilin, Powys, with a quarter of its volume filled with lead; the reasoning that sealing an object in a bottle or pot entrapped a troublesome spirit "and so was used as a protective charm"; the counter-ritual of putting thorns and pins into a bottle "usually filled with the victim's urine", sealed and boiled over the fire "or buried under the hearthstone"; written charms against witchcraft "rolled up and sealed inside a bottle"; wise men (dynion hysbys) selling charms. These are page-level facts: only the quoted sentence is under S622's blind-support obligation, so the entry should attribute placement/contents detail to the quote's row only if the sentence stays within the quote.

Observed on the Footwear Research Network page (same page as S623): find locations described as "points of weakness in a building ... down chimneys, though the roof, under floorboards and through windows and doors"; the caution that "the reason why people concealed shoes remains a mystery" and that no contemporaneous written evidence fixes a purpose; the alternative readings (good spirit of the wearer kept in the container-shaped shoe, evil spirits disliking the smell of leather, lucky charm); the earliest spirit-trap reference to John Schorn (rector of North Marston 1290–1314).

## rejected (opened this session, not offered)

- https://historicengland.org.uk/whats-new/features/discovering-witches-marks/what-are-witches-marks/ — fetch failed: `HTTPError HTTP Error 403: Forbidden` (same result with the locator's Firefox UA; no ordinary live copy, so no capture was saved).
- https://historicengland.org.uk/whats-new/features/discovering-witches-marks/types-of-marks/ — `HTTPError HTTP Error 403: Forbidden`.
- https://www.nationaltrustcollections.org.uk/object/420359 — HTTP 200 but an error shell, not the object record: 2263 bytes, `<title>Unknown Error</title>`, `<meta name="robots" content="noindex, nofollow">`, body heading `What a prickle…` / `We're sorry – it looks like something's gone wrong`. No curatorial text to quote.
- https://www.nationaltrust.org.uk/discover/history/warding-off-evil-with-witch-marks — HTTP 200, 2263 bytes, same `Unknown Error` shell (`windows 0 disc 0`); not the article.
- https://www.nms.ac.uk/discover-catalogue/footwear-lost-and-found — `HTTPError HTTP Error 403: Forbidden`.
- https://www.northamptonmuseums.com/collection/collections-home/shoe/ — HTTP 200, 654917 bytes, but the page text carries no protective-object vocabulary: scored `windows 0 disc 0`, so TOPIC cannot pass; its concealed-shoe text is an index description ("Concealed shoes are those that have been deliberately hidden in buildings"), not protection reasoning.
- https://www.northamptonmuseums.com/site/scripts/documents_info.php?switchstyle=museums2.css&categoryID=3&documentID=61 — `HTTPError HTTP Error 404: Not Found`.
- https://www.mola.org.uk/discoveries/research-projects/witch-bottles-concealed-and-revealed — HTTP 200, 75080 bytes, but the rendered text scores `windows 1 disc 0`: the page names witch bottles without using the field's protective vocabulary, so TOPIC would fail.
- https://www.mola.org.uk/discoveries/news/what-should-you-do-if-you-find-17th-century-witch-bottle — HTTP 200, 80646 bytes; scored `windows 2 disc 2` (`amulets`, `charms`), one window short of PAGE_HITS 3: TOPIC would fail. Kept as a spare only.
- Wayback availability/cdx queries for the two offered pages returned no snapshots (`{"archived_snapshots": {}}`, `cdx ... []`), so both rows list the live URL only.

## Confidence and unknowns

- S622: high confidence in the verbatim sentence and in the practice it describes; the page is a national museum blog dated 16 June 2011, and the passage continues into the hearthstone burial and paper-charm cases. Unknown: the post carries no personal byline, so the row attributes it to Museum Wales.
- S623: high confidence in the verbatim clause and author/date (Rebecca Shawcross, `datePublished 2022-02-04`, Northampton's senior shoe curator by trade); the article itself marks the purpose as unresolved, which the scope cell records. Unknown: whether any single 25-word window of the longer sentence carries the worn/patched detail to a blind reviewer — the offered clause was chosen to hold that detail at exactly 25 words.
- Neither row states a universal: both sources are England/Wales specific and both present protection as interpretation.
