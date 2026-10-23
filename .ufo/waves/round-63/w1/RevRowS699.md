# RevRowS699 — blind support review of drafted row S699 (round 63)

**Verdict: NOT-SUPPORTED** (as a mergeable, rule-complete row). The page content itself is genuinely supported; two defects block the row: (1) the canonical locator cannot confirm the capture this round — persistent HTTP 429 on web.archive.org against the locator's fixed Firefox UA (an ordinary-means rate-limit, not absent content), and (2) the drafted entry bullet carries one gloss the quote does not.

Draft reviewed: scribe scratch `/fast/scratch/hyaku/kotodama-r63/kotodama-r63-w1-ScribeRowS699/` (registry row, entry bullet, gate line, transcript) and report `.ufo/waves/round-63/w1/ScribeRowS699.md`. The scribe self-assessed "blocked; do not merge" — this review confirms and sharpens that.

## What was independently re-verified (all ordinary means; the held tool was not run)

- **Live URL**: `https://www.newadvent.org/cathen/10404a.htm` (Braun, "Mitre", Catholic Encyclopedia 1911). Canonical locator, my own run:
  `timeout 300 python3 -B reports/round-61/reopen-quote.py 'https://www.newadvent.org/cathen/10404a.htm' '<quote>'` → `LOCATED`, exit 0 (matches the scribe's run).
- **Quote is verbatim body text, not caption/alt/title**: in tag-stripped body text of the live page the quote sits inside a running paragraph — pasted located span (normalised, live.html offset 1680):
  > "…they wear a plain linen mitre, while the cardinals on occasions wear a simple mitre of silk damask. **the right to wear the mitre belongs by law only to the pope, the cardinals, and the bishops.** others require for its use a special papal privilege. this privilege is possessed, for example, by numerous abbots…"
  18 normalised words (within 8–25). No `[IMGALT]` adjacency; not a heading, caption, or attribute.
- **Capture content**: plain curl of the drafted capture `https://web.archive.org/web/20260831220821id_/https://www.newadvent.org/cathen/10404a.htm` returned HTTP 200, 23,830 bytes; its tag-stripped body is **identical to the live page** (same normalised length 13,013 chars, quote at the same offset 1680). Same page, same quote — content-level YES.
- **Capture via canonical locator: FAIL, 4 attempts across 2 timestamps.** Scribe: `NOT_LOCATED … URLError` (ConnectionRefusedError 111) on 20260831220821id_, 20260812203755id_, and the display URL. My retries ~1 h later: `NOT_LOCATED … HTTPError` exit 1 on 20260831220821id_ (after sleep 45) and 20260812203755id_ (after sleep 40).
- **Root cause pinned by differential probe**: the locator hardcodes `UA = "Mozilla/5.0 (X11; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0"` (reports/round-61/reopen-quote.py). Fetching the capture with python's default UA → **HTTP 200**; with that Firefox UA → **HTTP 429 Too Many Requests** from web.archive.org (nginx, 2026-10-23T19:16Z). The same UA succeeded against the live page (locator PASS). So the capture refusal is a UA-targeted rate limit/challenge at the archive, met-not-passed by content-identical ordinary fetch — but the round rule makes the locator the judge, and it does not pass.
- **URL uniqueness**: `10404a` occurs nowhere in `corpus/SOURCES.md` (only other newadvent row is S353 `/fathers/120116.htm`) and no sibling wave report or scratch drafts the same URL.
- **Row shape**: 11 columns mirroring S693 ✓; kind encyclopedia, tier B (1911 tertiary — plausible B) ✓; mined | 2026-10-23 | 180d ✓; used-by path `corpus/knowledge/culture-material/headgear-head-covering-codes.md` ✓; capture is an `id_` URL of the same page from the CDX 200 list ✓.

## Defect 2 — entry bullet over-reaches the quote

Drafted: `- The right to wear the mitre rests with the pope, cardinals, and bishops under church law (S699)`

- Formal bullet constraints PASS: one S-id; 8 content words ≥4 letters (right, wear, mitre, rests, pope, cardinals, bishops, church); 6 quote words in the quote's order (right→wear→mitre→pope→cardinals→bishops); longest verbatim run 6 words ("The right to wear the mitre") ≤ 12.
- **"under church law" is not carried by the quote** ("by law"), and the page never says "church law" or "canon" anywhere in its body; the only other "law" sentence on the page concerns *secular* princes (Duke Wratislaw of Bohemia; Peter of Aragon). It also drops the quote's exclusivity ("only"). Under the strict restatement test this is an invented qualifier.
- Minimal quote-carried fix: `- By law only the pope, the cardinals, and the bishops may wear the mitre (S699)` — content words pope, cardinals, bishops, wear, mitre (=5), order preserved, longest verbatim run 7 words ("the pope, the cardinals, and the bishops").

## Receipts

- `RECEIPT kotodama-r63-w1-RevRowS699/S699-live-locator counter-sha256=<n/a: round-61 locator, not a counter> rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=n/a exit=0 stopped-by=-` (LOCATED)
- `RECEIPT kotodama-r63-w1-RevRowS699/S699-capture-locator-20260831220821id_` … exit=1 stopped-by=HTTPError (429 on locator UA; retry after 45 s), and `.../S699-capture-locator-20260812203755id_` exit=1 stopped-by=HTTPError (retry after 40 s). Scribe's original attempts: URLError ConnectionRefused. No accept-o.py/accept-c.py run (out of this seat's scope; counters untouched).

## Residual risk and gaps

- The capture requirement may flip to PASS later in the round: the 429 is rate-based (default-UA fetch of the identical capture succeeds), so a later locator retry — ideally after the wave's archive.org pressure subsides — could confirm 20260831220821id_ without changing anything else. I did not retry further within the time box.
- I verified body-paragraph placement by tag-stripped text extraction, not the counter's own row-walk (S699 is not yet in SOURCES.md, so `--row S699` cannot run).
- Tier assignment (B) was not re-derived from QUALITY criteria; judged plausible only.

## Path to SUPPORTED (no new source needed)

1. Entry bullet → the quote-carried rewrite above (or any variant staying inside the quote's words).
2. One canonical-locator pass on the capture URL (id_) once the 429 lifts; any of the five CDX 200 captures qualifies if it locates.
Both hold → row S699 is fully supported as drafted in every other respect.
