# Round 61 — ScribeSrc04 source intake

Axes: coverage, provenance, quote locatability, and balance across the two assigned topics.

## Outcome

Four locatable sources are drafted, two for Venetian chopines and two for Louis XIV-era red heels. Every retained anchor includes a footwear-lexicon word, and each proposed entry line is limited to its anchor. IDs remain `S6??` per L1's integration decision; L1 assigns final IDs.

## Draft SOURCES rows

```text
| S6?? | Victoria and Albert Museum, “Pair of Chopines,” maker unknown, made in Venice ca. 1600; record created 14 February 2003 — https://collections.vam.ac.uk/item/O74447/pair-of-chopines-unknown/ | docs | A | Venetian chopines in the V&A record: concealment, dress-cloth demand and status | 2015–2016 Shoes: Pleasure and Pain gallery label, “On a Pedestal”: "Chopines were completely hidden under skirts. The higher the footwear the more cloth was required for the dress, another indication of status." | Chopines were hidden beneath skirts; higher footwear required more dress cloth and indicated status. | mined | 2026-10-23 | 180d | corpus/knowledge/culture-material/footwear-codes-terminology.md |
| S6?? | Harold Koda, “The Chopine,” Heilbrunn Timeline of Art History, The Metropolitan Museum of Art, 1 October 2002 — https://www.metmuseum.org/essays/the-chopine ; capture https://web.archive.org/web/20260417000000id_/https://www.metmuseum.org/essays/the-chopine | docs | A | the Met's expert account of chopines' popularity and functions among Venetian women | Opening paragraph: "Developed in the early sixteenth century and especially popular among Venetian women, the high-platformed shoe called the chopine had both a practical and symbolic function." | The Met describes the high-platformed chopine as popular among Venetian women and as having practical and symbolic functions. | mined | 2026-10-23 | 180d | corpus/knowledge/culture-material/footwear-codes-terminology.md |
| S6?? | The Museum at FIT, “The Museum at FIT,” HUE, 28 October 2025 — https://hue.fitnyc.edu/fit-museum/ | docs | B | FIT's museum feature associates a latchet shoe's red heels and soles with Louis XIV and his court | “Oldest item in the collection” caption: "The red heels and soles of these latchet shoes are associated with Louis XIV and his court." | The FIT page associates the red heels and soles of latchet shoes with Louis XIV and his court. | mined | 2026-10-23 | 180d | corpus/knowledge/culture-material/footwear-codes-terminology.md |
| S6?? | Signe Groot Terkelsen and Vivi Lena Andersen, “Red Heels: The Symbol of a Power Shift in 17th-Century Copenhagen?”, Archaeological Textiles Review 58 (2016): 3–9, DOI 10.7146/atr.58.167035 — https://tidsskrift.dk/atr/article/download/167035/208065 | paper | B | the article's French context for red heels and noble regulation, contrasted with excavated Copenhagen footwear | Introduction, opening historical-context paragraph: "King Louis XIV of France often wore shoes with red heels and soles, and by regulation made them the preserve of the nobility," | The paper says Louis XIV wore red-heeled shoes and by regulation made them the nobility's preserve. | mined | 2026-10-23 | 180d | corpus/knowledge/culture-material/footwear-codes-terminology.md |
```

## Draft entry bullets

- Higher chopines hidden under skirts required more dress cloth and signaled status. (S6??)
- The high-platformed chopine had practical and symbolic functions and was especially popular among Venetian women. (S6??)
- The red heels and soles of latchet shoes were associated with Louis XIV and his court. (S6??)
- Louis XIV made red-heeled shoes the preserve of the nobility by regulation. (S6??)

## Gate lines

- S6?? | https://collections.vam.ac.uk/item/O74447/pair-of-chopines-unknown/ | 2026-10-23 | "Chopines were completely hidden under skirts. The higher the footwear the more cloth was required for the dress, another indication of status."
- S6?? | https://www.metmuseum.org/essays/the-chopine | 2026-10-23 | "Developed in the early sixteenth century and especially popular among Venetian women, the high-platformed shoe called the chopine had both a practical and symbolic function."
- S6?? | https://hue.fitnyc.edu/fit-museum/ | 2026-10-23 | "The red heels and soles of these latchet shoes are associated with Louis XIV and his court."
- S6?? | https://tidsskrift.dk/atr/article/download/167035/208065 | 2026-10-23 | "King Louis XIV of France often wore shoes with red heels and soles, and by regulation made them the preserve of the nobility,"

## Evidence and provenance

Successful locator commands and exact stdout:

```text
timeout 300 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-61/reopen-quote.py 'https://collections.vam.ac.uk/item/O74447/pair-of-chopines-unknown/' 'Chopines were completely hidden under skirts. The higher the footwear the more cloth was required for the dress, another indication of status.'
LOCATED https://collections.vam.ac.uk/item/O74447/pair-of-chopines-unknown/

timeout 300 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-61/reopen-quote.py 'https://www.metmuseum.org/essays/the-chopine' 'Developed in the early sixteenth century and especially popular among Venetian women, the high-platformed shoe called the chopine had both a practical and symbolic function.'
LOCATED https://www.metmuseum.org/essays/the-chopine

timeout 300 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-61/reopen-quote.py 'https://hue.fitnyc.edu/fit-museum/' 'The red heels and soles of these latchet shoes are associated with Louis XIV and his court.'
LOCATED https://hue.fitnyc.edu/fit-museum/

timeout 300 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-61/reopen-quote.py 'https://tidsskrift.dk/atr/article/download/167035/208065' 'King Louis XIV of France often wore shoes with red heels and soles'
LOCATED https://tidsskrift.dk/atr/article/download/167035/208065

timeout 300 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-61/reopen-quote.py 'https://tidsskrift.dk/atr/article/download/167035/208065' 'King Louis XIV of France often wore shoes with red heels and soles, and by regulation made them the preserve of the nobility,'
LOCATED https://tidsskrift.dk/atr/article/download/167035/208065
```

Successful `LOCATED` runs correspond to the locator's documented exit status 0; the tool output did not print a separate exit line. Its declared PDF extraction path is `uv run --no-project --quiet --with pypdf==5.4.0`; no tool was installed or updated in this work.

For the Met essay, `functions.read` on the live page returned HTTP 429. The ordinary Wayback availability request was:

```text
timeout 300 curl -s 'https://archive.org/wayback/available?url=https%3A%2F%2Fwww.metmuseum.org%2Fessays%2Fthe-chopine'
{"url": "https://www.metmuseum.org/essays/the-chopine", "archived_snapshots": {"closest": {"status": "200", "available": true, "url": "http://web.archive.org/web/20260417000000/https://www.metmuseum.org/essays/the-chopine", "timestamp": "20260417000000"}}}
```

The corresponding `https://web.archive.org/web/20260417000000id_/https://www.metmuseum.org/essays/the-chopine` capture opened by ordinary `read`, but the required locator call against that capture returned `NOT_LOCATED https://web.archive.org/web/20260417000000id_/https://www.metmuseum.org/essays/the-chopine HTTPError` (exit 1). The live locator call above did locate the exact quote, so the row retains the live URL first and records the available capture second. No bot challenge, CAPTCHA, login, or paywall was met or bypassed.

### SOURCES.md URL checks

Each check used `functions.grep` against `/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md`; the exact result for each retained live host/path was `No matches found`:

- `collections\.vam\.ac\.uk/item/O74447` — `No matches found`
- `metmuseum\.org/essays/the-chopine` — `No matches found`
- `hue\.fitnyc\.edu/fit-museum` — `No matches found`
- `tidsskrift\.dk/atr/article/(download|view)/167035` — `No matches found`

## Non-kept probes and limits

- The Museum of Fine Arts, Boston chopine record returned HTTP 403 through `read`; Wayback availability reported capture timestamp `20250331054215`. It was not kept and no quote was submitted to the locator.
- The OpenEdition chapter on Monsieur's red heels opened, but the candidate locator returned `NOT_LOCATED https://books.openedition.org/pufr/29797 quote-absent`; its French `souliers` wording also does not match the frozen English footwear lexicon.
- The Bata Shoe Museum's Google Arts & Culture story opened, but its candidate locator returned `NOT_LOCATED https://artsandculture.google.com/story/standing-tall-the-curious-history-of-men-in-heels/AgVRZR_j5AhtLA denied-host`; it was excluded. The FIT museum page and peer-reviewed article were used instead.
- Met's archived “Court shoes” record was readable, but its archived locator attempt returned `NOT_LOCATED ... HTTPError`; it was not kept.
- The ATR paper studies Copenhagen finds; its Louis XIV statement is used only for the quoted French context, not as evidence about Copenhagen's excavated footwear. The FIT source is an official institutional feature, not a primary seventeenth-century record.

## Touched surfaces and scope

The sole write is this report: `.ufo/waves/round-61/w1/ScribeSrc04.md`. I read the round-61 claims, the source-registry schema and candidate URLs, the frozen footwear lexicon, the locator instructions, and the four retained source pages. I did not edit `SOURCES.md`, the footwear entry, product code, or any counter; I did not run acceptance counters, builds, tests, or other verification. Completing the 20-row claim predicate and integrating these drafts remain outside this source-seat report.
