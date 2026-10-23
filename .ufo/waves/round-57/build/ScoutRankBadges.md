# ScoutRankBadges — round 57, claim C (Chinese rank badges: buzui, birds for civil / animals for military)

Two holding-museum object records opened this session by ordinary GET: the V&A direct (HTTP 200), the Metropolitan Museum of Art via a Wayback capture after the live host answered a bot challenge. No installs. Freshness: `grep -c 'O456793'`, `grep -c '69082'` and `grep -c '60512'` on corpus/SOURCES.md print 0, so none of the offered URLs is named by an existing row (FRESH-leg compatible). Every quote below was run through the round locator (`reports/round-57/reopen-quote.py`) and its one-line output is pasted; quotes deliberately contain no quotation marks (the locator's QUOTE regex would otherwise extract only the first quoted span).

### NEW-ScoutRankBadges-1
citation: Victoria and Albert Museum, London, object record "Pair of rank badges" (pair of uncut square mandarin rank badges), museum number T.49&A-1968 (parts T.49-1968 and T.49A-1968), made in China, late 19th century, embroidered with coloured silks in satin, split, long and short stem stitches and laid and couched work, with laid and couched gold thread and some sequins; record system number O456793, no author or publication date on the record.
url: https://collections.vam.ac.uk/item/O456793/pair-of-rank-unknown/
route: direct, HTTP 200 (text/html, 48,355 bytes via plain curl with a desktop user-agent; the museum's own object record page; corroborated by the museum's JSON record at https://api.vam.ac.uk/v2/museumobject/O456793, which returns accession T.49&A-1968, objectType "Pair of rank badges", made late 19th century)
kind: record
tier: A — the holding museum's own object record states the object class name, the civil rank a charge denotes, and the badge's field vocabulary, exactly the claim's territory.
scope: the class name ("mandarin rank badges") that the record attaches to the garment part; the civil-rank rule (golden pheasant = insignia of a civil official of the second rank); the badge's background vocabulary (water, waves, rocks, clouds, miscellaneous symbols); materials and matched-pair, uncut-square fabrication.
quotes:
- object description: "On each badge is embroidered a golden pheasant, the insignia of a civil official of the second rank"
`LOCATED https://collections.vam.ac.uk/item/O456793/pair-of-rank-unknown/`
- object description: "with a background of water, waves, rocks, clouds and miscellaneous symbols"
`LOCATED https://collections.vam.ac.uk/item/O456793/pair-of-rank-unknown/`
- object description: "Pair of uncut square mandarin rank badges embroidered with coloured silks in satin"
`LOCATED https://collections.vam.ac.uk/item/O456793/pair-of-rank-unknown/`
teaches: Mandarin squares are embroidered robe badges where the creature names the grade: a golden pheasant insignia marks a second-rank civil official.
draft sentences:
- Give the garment part its bureaucracy's own name: the record opens "Pair of uncut square mandarin rank badges embroidered with coloured silks in satin" — the badge is a fitted, embroidered textile part of official dress, not a free-floating sign. (NEW-ScoutRankBadges-1, object description)
- One creature reads as one grade: "On each badge is embroidered a golden pheasant, the insignia of a civil official of the second rank" — the charge doubles as a legible rank-plate, so a worldbuilder can grade any official by species alone. (NEW-ScoutRankBadges-1, object description)
- Set the charge in a stated field vocabulary: the record continues the very sentence "with a background of water, waves, rocks, clouds and miscellaneous symbols" — a fixed backdrop convention an embroiderer inherits, rocks, waves and clouds around the central beast. (NEW-ScoutRankBadges-1, object description)
- Make the mark a workshop product, not a painting: the pair is worked in satin, split and long-and-short stem stitches with laid and couched gold thread and some sequins — matched pieces made to the textile-technique conventions of their maker. (NEW-ScoutRankBadges-1, object description)

### NEW-ScoutRankBadges-2
citation: The Metropolitan Museum of Art, New York, object record "Rank badge with tiger" (Qing dynasty 1644–1911, 18th century, China, silk and metallic thread, 9 1/2 × 9 3/4 in.), titled in Chinese 清 虎紋刺繡朝服補子, accession 36.65.11, Fletcher Fund 1936, Department of Asian Art; no author or publication date on the record.
url: https://web.archive.org/web/20251012230219id_/https://www.metmuseum.org/art/collection/search/69082
route: Wayback capture 20251012230219 of the live object URL (HTTP 200 via plain GET); the live URL https://www.metmuseum.org/art/collection/search/69082 answered HTTP 429 with a Vercel Security Checkpoint interstitial to a plain request — challenge met, not passed.
kind: record
tier: A — the holding museum's own record states the Ming–Qing two-ladder scheme, the badge's placement on the robe, and a charge's changed rank between dynasties, the claim's core.
scope: placement (square badges sewn on the front of government officials' robes in the Ming and Qing); the scheme (badges embroidered with birds for civil officials and animals for military officers, each creature corresponding to a specific rank); the tiger as a symbol of authority and bravery; the same charge carrying different ranks in Ming vs Qing (tiger = senior commander, rank 3, in the Ming; regimental vice commander, rank 4, in the Qing).
quotes:
- description: "Government officials of the Ming and Qing dynasties wore square badges sewn on the front of their robes"
`LOCATED https://web.archive.org/web/20251012230219id_/https://www.metmuseum.org/art/collection/search/69082`
- description: "These badges were embroidered with birds for civil officials and animals for military officers"
`LOCATED https://web.archive.org/web/20251012230219id_/https://www.metmuseum.org/art/collection/search/69082`
- description: "A symbol of authority and bravery, the tiger adorned the badge of a senior commander (Rank 3) in the Ming"
`LOCATED https://web.archive.org/web/20251012230219id_/https://www.metmuseum.org/art/collection/search/69082`
- description: "and that of a regimental vice commander (Rank 4) in the Qing"
`LOCATED https://web.archive.org/web/20251012230219id_/https://www.metmuseum.org/art/collection/search/69082`
teaches: Ming and Qing officials wore square badges sewn on their robes: birds for civil, animals for military officers, each creature a specific rank that shifted between dynasties.
draft sentences:
- Put the emblem where the office is visible: "Government officials of the Ming and Qing dynasties wore square badges sewn on the front of their robes" — the mark of appointment is a garment-mounted square, sewn to the chest. (NEW-ScoutRankBadges-2, description)
- The system runs on two parallel ladders: "These badges were embroidered with birds for civil officials and animals for military officers" — one species per grade on each side, a single glance tells service and grade apart. (NEW-ScoutRankBadges-2, description)
- Copy the rule, not the table: the same tiger "adorned the badge of a senior commander (Rank 3) in the Ming and that of a regimental vice commander (Rank 4) in the Qing" — grade charts were re-tuned between dynasties, so a worldbuilder who reuses one dynasty's chart for another's badges mis-reads them. (NEW-ScoutRankBadges-2, description)
- Let the beast carry its own meaning: the museum leads the description with "A symbol of authority and bravery, the tiger adorned" — the chosen creature both ranks the wearer and characterizes him. (NEW-ScoutRankBadges-2, description)

### Rejected
- https://www.metmuseum.org/art/collection/search/69082 (live) — plain GET answered HTTP 429 with a Vercel Security Checkpoint interstitial (challenge met, not passed); the record was read from the Wayback capture offered above.
- https://web.archive.org/web/20260329041010id_/https://www.metmuseum.org/art/collection/search/69082 — the capture holds the same description (verified by decompressed curl) but replays gzip-encoded; the locator's plain urllib fetch cannot decompress it and printed NOT_LOCATED (quote-absent). Not offered.
- https://www.metmuseum.org/art/collection/search/60512 ("Rank Badge with Wild Goose", 18th century, accession 30.75.874) — opened via Wayback capture 20240726053705id_ (serves identity; the description "The wild goose on this badge corresponds to the fourth rank of civil officials" was verified this session). Not filed: the scout limit is two sources and the civil-bird leg is already carried by the V&A row; recorded here as an identity-encoded, UTF-verified fallback if the L1 wants a second civil-grade record.
- https://searchcollection.asianart.org/objects/2121/rank-badge-of-goose-fourth-rank (Asian Art Museum of San Francisco, "Rank badge of goose, fourth rank") — plain GET answered HTTP 202 with a JavaScript "verify that you're not a robot" interstitial (challenge met, not passed); not opened further.
- Minneapolis Institute of Art — https://collections.artsmia.org/items/16573 (and sibling items) serves a JavaScript single-page shell with no server-side record text; the public search API (https://search.artsmia.org/) returns the records (verified 16573, 24228, 27272, 27674, 27915) but with empty descriptive text for the Chinese rank badges, so nothing quotable beyond titles; not offered.
- https://collections.vam.ac.uk/item/O457654/rank-badge-unknown/ (V&A) — surfaced in search with an internal bird-name inconsistency ("silver egret" vs "Silver Pheasant" in the same record); not opened; excluded.
