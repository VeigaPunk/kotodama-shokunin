# R9-F01c — freshness residual R8-F01, alternate-angle hunt

- **Round:** 9 (loop 1 of 3, build round 2 of 4) · **Date:** 2026-10-17 · **Shard:** FRESHNESS R9-F01c
- **Residual:** R8-F01 (prior row R6-02-A), reconciled disposition `unresolved` (round-6 reconciliation, carried in `reports/round-8/freshness/reconciliation.json`); round-8 author receipt says `resolved-passage-level`
- **Entry:** `corpus/knowledge/civilizations/mesopotamia-sumer-akkad.md` — sha256 `bf6c92f9…a4b478` at recheck
- **Question:** Check the entry's evidence for Sumerian/Akkadian language contact and the separation of scribal language survival from spoken-language replacement; which dated text or scholarly passage supports the institutional coupling?

## The alternate angle: re-derive, then hunt

The residual's own rejection basis names the missing evidence: a *dated text or directly inspected scholarly passage* for the coupling. The entry supplies the criterion for "coupling" in its own words (line 14):

> "The strongest coupling evidence joins a dated text to its institution and material context."

So a settling witness needs three things at once: **a fixed date, an identified institution, and a find context**. A royal bilingual (the round-8 `to-verify` item, Louvre AO 5477) has only the first, and only for the *contact* leg — this angle therefore **demoted** it and hunted the document class that can carry all three: the excavation-publication-and-catalogue chain for a school house.

Named targets, all public:

| Target | Document | What it can settle |
|---|---|---|
| ST-1 | Robson 2001, "The Tablet House", *RA* 95, 39–66 | institution + operation window + material context |
| ST-2 | McCown & Haines 1967, *Nippur I* (OIP 78) | primary publication: date formulas ↔ house loci ↔ museum allocations |
| ST-3 | *Back to School in Babylonia*, ISACMP 1 (2023) | per-object findspot + museum number + internal date |

The prediction was falsifiable: either the chain yields a peer-reviewed passage stating the house's dates and school status **and** at least one numbered tablet with an internal date formula found inside that house, or the receipt records which sub-target stayed unretrieved. Both were found.

## What was retrieved (all read this round, not cited from blurbs)

### ST-1 — Robson 2001, full text (fetched 2026-10-17T20:48Z)

URL: https://shs.cairn.info/revue-d-assyriologie-2001-1-page-39?lang=en — full article text served to the fetcher (53,774 B / 350 lines extracted; sha256 `3beadb35…f8d5` of the extraction at the session tool-results path). Direct `curl` of the same URL returns **HTTP 403** (bot wall) — route difference documented, not worked around silently.

- **¶2:** > "'House F' was in operation in Nippur during the 1740s BCE (the early reign of king Samsu-iluna). It was excavated by the joint Chicago-Philadelphia expedition in 1951–52, yielding nearly one and a half thousand fragments of tablets."
- **¶3:** > "The house consisted of a small courtyard, locus 192, with three small rooms (191, 189, and 184) ranged to its northwest and a larger back room or courtyard, 205, to its northeast."
- **¶5:** > "House F produced 1, 425 fragments, over 85% of the entire number found in TA that season (Fig. 5; McCown and Haines 1967: pl. 160 D) … in House F only 2% of the tablets are clearly archival in character. Over 50% contain Sumerian literature, 42% are other school documents…"
- **¶30:** > "the Old Babylonian scribal schools were deliberately traditionalist, continuing to promulgate Sumerian while most administrative, business, and legal documents were already written in Akkadian" — and > "Some thirty or so household documents written after Hammurabi's conquest of Nippur in 1762 survive from House F and its neighbours in Area TA. Over two thirds of them were written in Sumerian (Fig. 15), and continued to be written in Sumerian until the area was abandoned after 1721."

### ST-2 — OIP 78, primary excavation publication (downloaded 2026-10-17T20:52Z)

Live OI path is **404**; retrieved via Wayback: `https://web.archive.org/web/2020id_/https://oi.uchicago.edu/…/oip78.pdf` — 51,527,953 B, **466 pages**, sha256 `881b6123…0a6b92`, closes with `%%EOF` after a `-C -` resume; text via `pdftotext -layout` (18,933 lines, sha256 `20cb4648…`).

- **p. 74 (PDF p. 96):** > "Perhaps the most remarkable fact concerning the dated, stratified tablets is how "unstratified" they are. … At best, cuneiform tablets can provide only a reasonable approximation of the date of the level in which they are found."
- **p. 75 (PDF p. 97):** > "The following dated tablets were found in TA." — heading of the Area TA dated-tablet table, continuing on p. 76.
- **p. 76 (PDF p. 98), TA table, left column (the House F locus sequence: 174 / 203 / 184 / 185 / 178), block "Level X 1":** > `3NT 87            184       Ilumailu` — with neighbouring rows `3NT 88 184 Rimsin year 54`, `3NT 86 185 Samsuiluna year 18`, `3NT 89 184 Samsuiluna year 27`.
- **p. 180 (PDF p. 204), Index of Catalogue Numbers:** > `3NT 87       p. 76                P      55-21-239` — tablet 3NT 87 allocated to the University Museum (P) as **55-21-239**, published at p. 76.
- **p. xii (PDF p. 12), TOC:** "Contents of Representative Houses … TA House F (Level XI 2) … 116 / TA House F (Level XI 1) … 116".
- Locus convention for objects from the same room (PDF pp. 362, 410): `TA 184 X 1` — Area TA, room 184, Level X, phase 1, matching ST-3's wording below.

### ST-3 — *Back to School in Babylonia*, ISACMP 1 (2023), open access (downloaded 2026-10-17T20:50Z)

Live ISAC PDF path now 301→HTML landing page; retrieved via Wayback `…/2024id_/https://isac.uchicago.edu/…/ISACMP/isacmp1.pdf` — 37,393,473 B, **482 pages**, sha256 `c8fd81d2…4dca7`; text 18,491 lines, sha256 `67c50ac9…`.

- **p. 3 (PDF p. 26), ch. 1 Paulus:** > "the tablets excavated by the Joint Expedition are special because they were discovered in the context of House F, widely believed to have been a scribal school."
- **p. 14 (PDF p. 37):** > "when House F's Edubbaʾa was in operation, Sumerian was no longer spoken and only rarely written in documents of daily life—there, Akkadian or Babylonian dominated."
- **p. 9 (PDF p. 32):** > "Rarely are school documents dated so as to allow putting them into a secure chronological sequence. A rare exception of unprovenienced tablets, now in the Yale University Babylonian Collection, indicates that a student named Qišti-Ea studied literary compositions between Samsu-iluna's regnal years one and eleven…"
- **p. 34 (PDF p. 57), ch. 3 McMahon:** > "Approximately 1,425 tablets or tablet fragments with a rich variety of text genres were recovered from House F in Level XI, making it one of the most important known scribal schools."
- **p. 103 (PDF p. 126), ch. 11 Siegmund:** > "Sumerian had lain dead for centuries as a mother tongue but been kept alive in the academy as a written language of great cultural import."
- **p. 226 (PDF p. 249), catalog no. 9:** > "Nippur, Area TA, House F, Room 184, Level X Floor 1 … ISACM A30143 (3NT-97) … Dated to the forty-eighth year and fourth month of the reign of King Rim-Sin of Larsa (ca. 1775 bce). Literature: McCown and Haines 1967, 76, 180".
- **p. 227 (PDF p. 250), catalog no. 10:** > "Nippur, Area TA, House F, Room 184, Level X Floor 1 … University of Pennsylvania Museum … UM 55-21-239 (3NT-87) … Dated to the first year, seventh month, and sixteenth day of the reign of King Iluma-ilum of the Sealand Dynasty (ca. 1721 bce). Literature: McCown and Haines 1967, 76, 180".

*Extraction note (all ST-3 quotes):* the volume is read from a `pdftotext -layout` extraction. Pages 3 and 9 are two-column pages whose left column carries figure captions; the extraction interleaves it mid-sentence, so those two passages are quoted as contiguous column runs with the caption lines removed (exact fragment splits are recorded per passage in `R9-F01c-receipt.json`). Catalog entry 10's date line breaks after "seven"; the quote joins it with a space. Every quote above was machine-checked verbatim against the extracted text on 2026-10-17.

## The chain, assembled

**3NT 87 = Penn UM 55-21-239** → found in **Area TA, House F, room 184** (Robson 2001 ¶3 lists 184 as one of House F's rooms; ISACMP 1 pp. 226–227) → dated by its **own internal formula**, Iluma-ilum year 1, vii-16 (≈ 1721 BCE) → published and allocated in the **primary publication** (OIP 78 pp. 76, 180, in the House F locus column under Level X 1). A second document, 3NT-97 = ISACM A30143, dated Rim-Sin year 48 (≈ 1775 BCE), carries the same findspot. This is exactly the "dated text + institution + material context" the residual said had not been retrieved.

## What remains unanswerable, precisely

1. **No text inside House F names it as a school.** The identification is assemblage-statistical (Robson ¶5: 2% archival vs >50% Sumerian literature, against the neighbouring houses' mixed profile), and the 2023 catalogue hedges it ("widely believed", p. 3). Any request for a *dated text naming the institution* is unanswerable from public sources — the institution is inferred from the finds, not from an inscription.
2. **Internal dates and secure find contexts trade off, by the sources' own statements.** School documents are "rarely" internally dated (p. 9); the primary publication warns dated house tablets are "unstratified" and level dates are approximations (p. 74). A maximally strong version of the question is unanswerable by construction: what exists is dated *house* documents with recorded findspots (both are sale/exchange documents, and both sit in the house's Level X phase), plus school exercises dated only by context.
3. **Phase assignment is not fully pinned** — the school assemblage is "Level XI" (p. 34), the two dated documents are "Level X Floor 1" (pp. 226–227), and OIP 78 names "TA House F (Level XI 1/2)" as the representative phases while placing 3NT 87 under a "Level X 1" block. `to-verify`.
4. **The tablets themselves were not inspected** — no museum/object record was retrievable (see failures).

## Access failures (attempted commands and statuses)

| Attempt | Status | Consequence |
|---|---|---|
| `curl -A 'Mozilla/5.0…' 'https://shs.cairn.info/revue-d-assyriologie-2001-1-page-39?lang=en'` | HTTP 403 (770 B) | article obtained via the host fetcher instead; extraction hash recorded |
| `curl -I` OI & ISAC PDF paths | 302→404 (OI); 301→200 text/html (ISAC) | both PDFs obtained via Wayback `id_` snapshots |
| CDLI permalinks/`.json` (`cdli.mpiwg-berlin.mpg.de`, `cdli.earth`) | 301→`cdli.earth/artifacts/…`→404; `.json` 404 | CDLI unusable as a server-rendered object record (consistent with round 8) |
| CDLI search `?q="UM 55-21-239"` | HTTP 200, 1,634,206 B, client-rendered | no server-side row |
| Penn Museum object page / search / api | HTTP 403 (curl and fetcher) | object attributes remain second-hand |
| ORACC DCCLT (curl and fetcher) | TLS issuer failure / fetch network error | DCCLT unused; ORACC OBMC essay retrieved OK and corroborates *é-dub-ba-a* = Akkadian *bīt ṭuppi* |
| `http://bdtns.filol.csic.es/` | TLS subject mismatch → redirects to `bdtns.cesga.es` (HTTP 200) | live route noted, not exercised |
| Local scratch | `/tmp` full (0 free inodes) | artifacts written under `/var/tmp/r9f01c` (outside the lane repo) |

## Disposition

`unresolved` → **partial-support-or-better**, at passage level *and* object-record level, for the bounded entry row (line 39) and for the residual's request as framed. Nothing contradicts the entry; the entry asserts no fixed vernacular-loss date, and none was obtained. Raw round-6 labels are untouched — this receipt reports only the reconciled disposition. Sibling angle receipts (R9-F01a/b) and the verifier (R9-F01d) had not landed when this shard started (`ls reports/round-9/freshness/` empty at 2026-10-17T20:47Z); this receipt deliberately asserts no disposition on their behalf.

**Counting basis:** all counts, hashes and page mappings are in `R9-F01c-receipt.json → counting_commands` (run 2026-10-17; `date -u` → 2026-10-17T20:54:38Z).
