# ScribeRowS695 — round 63, claim C

## Outcome
Prepared a sourced S695 draft for the laurel-wreath / corona subtopic. The live quote passes the prescribed base locator; the archived quote is visible in the capture opened by `read` and was independently confirmed by the peer reviewer using ordinary curl plus gunzip, but the prescribed base locator did **not** locate the archive response. Therefore I do not claim that the required locator-on-both-URLs condition passed. No product registry or entry file was edited.

## Draft artifacts

Registry row (11 columns):

`| S695 | “The Ancient Origins of a Snapchat Filter,” Emily Carruthers, Getty, 4 May 2017 (updated 15 August 2022) — https://www.getty.edu/news/the-ancient-origins-of-the-flower-crown/ ; capture https://web.archive.org/web/20261001150139id_/https://www.getty.edu/news/the-ancient-origins-of-the-flower-crown/. | docs | A | Pythian Games laurel wreaths awarded to victors and the crown's honorary function | Body Content, Pythian Games paragraph, sentence beginning “For example”: “winners traditionally received a wreath of bay laurel” | Getty describes Pythian Games winners receiving a wreath of bay laurel | mined | 2026-10-23 | 180d | corpus/knowledge/culture-material/headgear-head-covering-codes.md |`

Entry bullet:

`- Pythian winners received a wreath of bay laurel. (S695)`

Gate line:

`- S695 | https://www.getty.edu/news/the-ancient-origins-of-the-flower-crown/ | 2026-10-23 | "winners traditionally received a wreath of bay laurel"`

The anchor is 8 normalized words in the Getty article's `Body Content` Pythian Games paragraph, not a caption, alt text, title, or metadata. The entry clause has five content words (Pythian, winners, received, wreath, laurel); `winners`, `received`, `wreath`, `bay`, `laurel` occur in quote order; the longest verbatim run is six words (`received a wreath of bay laurel`). The Getty page describes the crown as an honorary reward in the preceding sentence and the bay laurel as a symbol of victory, achievement, and status in the following sentence.

## Provenance and checks

- Read `reports/round-63/claims.json`, the docstrings of both frozen acceptance counters, and §5 of `corpus/lessons/round-62-verifier-spotcheck.md` before source work. `sha256sum` output matched the specified hashes:
  - `accept-o.py`: `a751efecccf623fcd4d2f348994933e34da892cf08132fa55b77f28c5fd8a5de`
  - `accept-c.py`: `3a5310342c9e17567964e8b20ea24126d0f31b9316cadccc0d2c41a80fe499ca`
- Searched `corpus/SOURCES.md` for the exact Getty live URL; no matches.
- Read the live Getty article at `https://www.getty.edu/news/the-ancient-origins-of-the-flower-crown/`. Its body says: “For example, the Pythian Games were held at Delphi every four years in honor of Apollo, and winners traditionally received a wreath of bay laurel.”
- Exact CDX request: `http://web.archive.org/cdx/search/cdx?url=https://www.getty.edu/news/the-ancient-origins-of-the-flower-crown/&output=json&limit=-5&filter=statuscode%3A200`. The `read` result listed five HTTP 200 records for that exact original URL, including `20261001150139`, MIME `text/html`, digest `WWY7TM2P7ZCNHFNWGMYZ5TJ6PNP666BF`, length `1181759`. The selected capture URL embeds the same original live URL.
- Read the `20261001150139id_` capture. Its `Body Content` has the same Pythian paragraph and the exact anchor quote.
- Independent review: `kotodama-r63-w1-RevRowS695` reports live-body and capture-body confirmation and a `SUPPORTED` substance verdict. Its report records that plain curl returned a gzip-encoded replay which contained the quote after decompression; that reviewer evidence is at `.ufo/waves/round-63/w1/RevRowS695.md`. This is peer evidence, not a successful base-locator capture result from my seat.

## Required locator outputs

Live command, run from the lane root:

`cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && timeout 300 python3 -B reports/round-61/reopen-quote.py 'https://www.getty.edu/news/the-ancient-origins-of-the-flower-crown/' 'winners traditionally received a wreath of bay laurel'`

Full stdout: `LOCATED https://www.getty.edu/news/the-ancient-origins-of-the-flower-crown/` — exit `0`.

Capture command:

`cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && timeout 300 python3 -B reports/round-61/reopen-quote.py 'https://web.archive.org/web/20261001150139id_/https://www.getty.edu/news/the-ancient-origins-of-the-flower-crown/' 'winners traditionally received a wreath of bay laurel'`

Full stdout: `NOT_LOCATED https://web.archive.org/web/20261001150139id_/https://www.getty.edu/news/the-ancient-origins-of-the-flower-crown/ URLError` — exit `1`.

Further ordinary URL attempts on the archive also failed; these do not change the required result:

- `http://web.archive.org/web/20261001150139id_/https://www.getty.edu/news/the-ancient-origins-of-the-flower-crown/` with the anchor quote → `NOT_LOCATED ... quote-absent`, exit `1`.
- `http://web.archive.org/web/20261001150139/https://www.getty.edu/news/the-ancient-origins-of-the-flower-crown/` with the anchor quote → `NOT_LOCATED ... HTTPError`, exit `1`.
- Older CDX captures `20260518212752id_`, `20220410071258id_`, and `20220625001104id_` with the same quote → respectively `quote-absent`, `HTTPError`, `HTTPError`, each exit `1`.
- On the latest id_ URL, the alternate body quote `Since antiquity, the circular or horseshoe shape of the wreath has been a symbol of glory, power, and eternity` → `NOT_LOCATED ... HTTPError`, exit `1`.

## Rejected candidates

- Loeb Classical Library, Pliny, *Natural History*, Book XV, ch. XXXIX, `https://www.loebclassics.com/display/pliny_elder-natural_history/1938/pb_LCL370.375.xml`: the live anchor `this laurel is used to make wreaths for the winners at Delphi, as it is for generals going in triumph at Rome` returned `LOCATED` (exit 0), but the exact-URL CDX query returned `[]`; rejected because no Wayback capture was found.
- `https://www.britannica.com/art/laurel-wreath`: ordinary `read` returned `Failed to fetch URL (HTTP 404)` and the exact-URL CDX query returned `[]`; rejected. No quote was accepted from this page.

## Gates, touched surfaces, and limits

- S695 draft checks: the live URL was not present in the base registry; Getty body quote is 8 words; proposed row has the required date, tier A, `mined`, `180d`, used-by path, same-page Wayback id_ URL, and body-text location; the entry line has one S695 and meets the content-word, quote-order, and copy-run limits.
- Capture locator: **not passed** by this seat. Although `read` shows the same body quote and the peer reviewer independently reports curl + gunzip confirmation, the mandated base locator returned `NOT_LOCATED`; preserve that failure in any integration record.
- No `accept-c.py` counter or O counter was run; no tests/build/lint/formatter, held `tools/reopen-row.py`, live registry row re-opener, git, or jj command was run. No tools were installed.
- Only scratch artifacts and this designated report were written. `corpus/SOURCES.md`, the headgear entry, product code, counters, and judge were left unchanged. No O repair/review work was in this seat's scope.

Scratch artifacts:
- `/fast/scratch/hyaku/kotodama-r63/kotodama-r63-w1-ScribeRowS695/row-S695.md`
- `/fast/scratch/hyaku/kotodama-r63/kotodama-r63-w1-ScribeRowS695/entry-bullet-S695.md`
- `/fast/scratch/hyaku/kotodama-r63/kotodama-r63-w1-ScribeRowS695/gate-line-S695.md`
- `/fast/scratch/hyaku/kotodama-r63/kotodama-r63-w1-ScribeRowS695/locator-results-S695.md`
