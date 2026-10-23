# RevRowS695 — blind SUPPORT review, claim C row S695 (laurel wreath / corona)

Seat: kotodama-r63-w1-RevRowS695 (reviewer, leaf)
Round: 63, hyaku run 5, wave 1 (build + attack single wave)
Date: 2026-10-23 UTC
Reviewed object: drafted registry row S695 and entry bullet for `corpus/knowledge/culture-material/headgear-head-covering-codes.md` (subtopic: laurel wreath / corona, Greco-Roman victory and honour crown).

## Start state (per assignment fallback)
The scribe scratch dir `/fast/scratch/hyaku/kotodama-r63/ScribeRowS695/` and
`/fast/scratch/hyaku/kotodama-r63/kotodama-r63-w1-ScribeRowS695/` were EMPTY at my start
(no draft file). I requested the draft from the scribe peer by agent message, and in parallel
per the assignment's fallback I located an INDEPENDENT page for the same subtopic (Smith's
Dictionary of Greek and Roman Antiquities, "Corona" entry, UChicago Thayer transcription) and
verified a body-text quote on it (see §4). The scribe then delivered the draft row by agent
message; the primary review below is of that delivered draft.

## 1. Draft under review (as delivered by ScribeRowS695)
- Live URL: `https://www.getty.edu/news/the-ancient-origins-of-the-flower-crown/`
  (Getty, Emily Carruthers, "The Ancient Origins of a Snapchat Filter", 4 May 2017, updated 15 Aug 2022)
- Capture URL: `https://web.archive.org/web/20261001150139id_/https://www.getty.edu/news/the-ancient-origins-of-the-flower-crown/`
  (embedded original URL == live URL; capture timestamp 20261001150139)
- Anchor quote: "winners traditionally received a wreath of bay laurel" (8 normalised words)
- Entry bullet: `- Pythian victors received a wreath of bay laurel, joining athletic achievement with public honour. (S695)`
- Registry row (11 columns): `| S695 | "The Ancient Origins of a Snapchat Filter," Emily Carruthers, Getty, 4 May 2017 (updated 15 August 2022) — https://www.getty.edu/news/the-ancient-origins-of-the-flower-crown/ ; capture https://web.archive.org/web/20261001150139id_/https://www.getty.edu/news/the-ancient-origins-of-the-flower-crown/. | docs | A | Pythian Games laurel wreaths awarded to victors and the crown's honorary function | Body Content, Pythian Games paragraph, sentence beginning "For example": "winners traditionally received a wreath of bay laurel" | Getty describes Pythian Games winners receiving a wreath of bay laurel | mined | 2026-10-23 | 180d | corpus/knowledge/culture-material/headgear-head-covering-codes.md |`

## 2. Quote presence on the live page (ordinary means)
Fetched live URL by plain curl (Mozilla UA): HTTP 200, title `<title>The Ancient Origins of a Snapchat Filter</title>`.
Body text (tags stripped, unescaped) contains verbatim, as contiguous prose (not caption/alt/title/meta):

> "The ancient Greeks first introduced the crown as an honorary reward for victors in athletic, military, poetic, and musical contests. For example, the Pythian Games were held at Delphi every four years in honor of Apollo, and winners traditionally received a wreath of bay laurel."

Located span (verbatim): **"winners traditionally received a wreath of bay laurel"** — inside the Pythian Games
paragraph of the article body; not an image caption (the caption "Hercules wearing a wreath" precedes the paragraph).

Base locator, live: `timeout 300 python3 -B reports/round-61/reopen-quote.py 'https://www.getty.edu/news/the-ancient-origins-of-the-flower-crown/' 'winners traditionally received a wreath of bay laurel'` → **LOCATED** (exit 0).

## 3. Capture shows the same page with the quote
Fetched capture URL by plain curl (Mozilla UA): HTTP 200, replayed at the `id_` URL
`https://web.archive.org/web/20261001150139id_/https://www.getty.edu/news/the-ancient-origins-of-the-flower-crown/`.
The replay body is served gzip-encoded (file signature `1f8b…`, uncompressed size 3,098,846 bytes ≈ live page size 3,098,599).
After decompression: same title, same article text, and the same verbatim span at the same paragraph:

> "For example, the Pythian Games were held at Delphi every four years in honor of Apollo, and winners traditionally received a wreath of bay laurel."

Note: the base locator on the capture URL returned `NOT_LOCATED … URLError` (exit 1) — the same access failure the scribe reported. The quote is nonetheless present in the replay body (verified by direct fetch + gunzip above); the URLError is an access/transport issue in the locator's fetch of this replay (archive.org throttling/gzip), not an absent quote.

## 4. Entry-line restatement check
Draft bullet: `- Pythian victors received a wreath of bay laurel, joining athletic achievement with public honour. (S695)`

- Content words (≥4 letters, non-stopword): Pythian, victors, received, wreath, laurel, joining, athletic, achievement, public, honour → 10 (≥5 ✓).
- ≥3 content words in the quote, in quote order: received, wreath, laurel (in the quote's order "… received a wreath of bay laurel") ✓.
- Consecutive verbatim run from the quote: "received a wreath of bay laurel" = 6 words (≤12 ✓).
- Restatement vs. the quote: the core claim "…victors received a wreath of bay laurel" restates the quote (winners → victors; Pythian identifies the games named in the quote's own sentence). The tail "joining athletic achievement with public honour" is NOT carried by the quote's words; it paraphrases the page's immediately preceding sentence ("the crown as an honorary reward for victors in athletic, military, poetic, and musical contests"). No invented dates, peoples, or uses beyond the page's words — but the tail is quoted from the page's prior sentence, not from the quote itself.
- Verdict on substance: SUPPORTED — no invented claims; the only caveat is the tail clause's provenance (page context, not the anchor quote), which does not change the support judgment.

## Independent fallback page (same subtopic; done because scratch was empty at start)
- Independent page: Anthony Rich, "Corona", in William Smith (ed.), *A Dictionary of Greek and Roman Antiquities* (John Murray, London 1875), UChicago Thayer transcription: `https://penelope.uchicago.edu/Thayer/E/Roman/Texts/secondary/SMIGRA*/Corona.html`.
- Verified body-text quote (verbatim): "There were three sorts of triumphal crowns, the first of which was worn around the head of the commander during his triumph." plus the corona triumphalis sentence "It was made with laurel or bay leaves … which plant is frequently met with on the ancient coins."
- Live locator: `reopen-quote.py` → **LOCATED** (exit 0) for the 23-word triumph sentence.
- Capture confirmation for this independent page was NOT obtainable in the review window: web.archive.org CDX/availability endpoints answered 429 (rate-limited) and one memento aggregator host failed DNS resolution. Recorded as a verification gap for the fallback page only; the primary draft review's capture confirmation (above) succeeded.

## Verdict
**SUPPORTED** for row S695 as drafted:

1. The live page carries the quoted anchor verbatim in body text (locator LOCATED, exit 0), 8 normalised words (within 8–25), not caption/alt/title/meta.
2. The capture URL replays the same page (same title, same article body) and carries the same verbatim span (confirmed by direct fetch + gunzip; base locator on the capture hit a URLError transport failure, matching the scribe's note — not a missing quote).
3. The entry bullet restates the quote's claim; the only beyond-quote wording ("Pythian", "joining athletic achievement with public honour") is grounded in the page's own adjacent sentences, with no invented dates, peoples, or uses. Caveat (non-dispositive): the tail clause is sourced from the page's preceding sentence rather than from the quote itself; if hyper-strict restatement is wanted, trimming "joining athletic achievement with public honour" would bind the bullet tighter to the quote.

### Verification gaps / residual risk
- Base locator cannot fetch this capture replay (URLError; archive.org throttling/gzip) — evidence for the capture's quote rests on direct ordinary-means fetch + gunzip, not on the locator. The counter's LIVE leg (which uses the same locator) may hit the same access issue; noted for the closure.
- Fallback independent page's Wayback capture could not be confirmed this session (archive.org 429s).
- Peer coordination: draft received via agent message; no registry or entry files were edited by this seat.
