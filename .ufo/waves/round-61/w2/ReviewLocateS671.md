# Round 61 W2 — ReviewLocateS671: diagnosis of C's single LOCATE miss

Scoped review, read-only, ~10:00–10:04 UTC (receipt measured at 09:58Z; the one-receipt rule holds — `accept-c.py` was never run by this seat, no counter was re-run).

## The row and its URLs

`corpus/SOURCES.md:626` — S671's `source` cell carries exactly two http(s) URLs, in this order (the locator `locate()` tries `urls[:4]` in order):

1. live — `https://americanindian.si.edu/collections-search/object/NMAI_26904`
2. capture — `https://web.archive.org/web/20250612214229id_/https://americanindian.si.edu/collections-search/object/NMAI_26904`

Anchor quote: `"Object Name Moccasins Media/Materials Elk hide/skin, hide thong/babiche, paint Techniques Sewn, painted"` (11 normalised words ≥ 8; legal quote).

## Status codes observed now (ordinary means)

| URL | curl `-w %{http_code}` | `timeout 300 python3 -B reports/round-61/reopen-quote.py URL QUOTE` |
|---|---|---|
| live | 403 (three draws, incl. locator's exact Firefox UA and urllib-style headers) | `LOCATED https://americanindian.si.edu/...` exit 0 at ~10:01Z — one urllib pass amid 403s |
| capture | 200 (51,017 bytes) | `LOCATED https://web.archive.org/web/20250612214229id_/...` exit 0 |
| CDX `url=...NMAI_26904` | — | `20250612214229 200` — the capture exists at the expected timestamp |

- The live 403 body (24,512 bytes, saved to `/fast/scratch/hyaku/kotodama-r61/w2/ReviewLocateS671/live-403-body.html`) is a **Cloudflare challenge page**: `<title>Smithsonian site temporarily unavailable</title>`, `/cdn-cgi/challenge-platform/scripts/precursor/main.js`. Site-wide for curl — `https://americanindian.si.edu/` root also 403s. A bare `urllib` GET at ~10:03Z also returned `HTTPError 403`.
- The capture body (saved to `/fast/scratch/hyaku/kotodama-r61/w2/ReviewLocateS671/capture-body.html`) contains the anchor verbatim: `Object Name`, `Elk hide/skin, hide thong/babiche, paint`, `Sewn, painted`.
- `archive.org/wayback/available` answered **429 Too Many Requests** at ~10:00Z — archive.org rate-limiting was active in this window.

## Transient vs structural

- **Live leg: structural.** A Cloudflare bot-challenge 403 stood at draft time (scribe recorded 403 on the object page and the `collections.si.edu` mirror), at measure time (receipt: `HTTPError`), and for curl/urllib now. My single intermittent `LOCATED` on the live URL shows the challenge is fingerprint/state-sensitive rather than a hard wall — a plain non-JS GET occasionally passes — but an ordinary GET cannot be relied on, and under the instrument's rule a fetch error is a non-location. For the claim's purposes the live leg is dead.
- **Capture leg: transient.** The capture exists (CDX `200`), serves the quote (LOCATED + verbatim strings at ~10:01Z), and the L1's own post-measure diagnostic `reopen-quote.py --row S671` run about two minutes after the receipt located the capture while the live URL still 403'd (`corpus/lessons/round-61.md` R61-M4). Archive.org was rate-limiting (429) in the same window, so the 09:58Z capture error is consistent with transient archive-side flakiness (429/5xx/timeout). **Exact error class is unrecoverable**: `accept-c.py:250` truncates each miss detail at 160 chars (`detail[:160]`), and the receipt's S671 entry is cut inside the capture URL itself — the error class never entered the receipt. [INFERENCE: transient; consistent with all in-window evidence.]

## Scribe report vs pre-landing record (`.ufo/waves/round-61/w1/ScribeSrc06.md`)

- **Located live fetch: NO.** The scribe recorded `read` on the live URL and the Smithsonian catalog mirror `collections.si.edu/search/detail/edanmdm:nmai_26904` — both `HTTP 403` ("the live 403 is recorded as an access failure, not as a verified challenge"). The live URL was never observed locating at draft time.
- **Located capture: YES.** The availability API confirmed the `20250612214229` capture; the HTTPS `id_` capture was read and `reopen-quote.py` returned `LOCATED <capture>` exit 0.
- The scribe's draft Gate line therefore named the **capture URL** as the vouching URL. The **landed** Gate line (`corpus/lessons/round-61.md:68`) instead lists the **live URL** for S671 — the URL that 403'd — not the capture that was demonstrated locating. Low-severity calibration wrinkle: LOCATE reads the row's `source` cell, not the Gate line, so verdict impact is nil, but the Gate record misstates which URL was verified (pre-landing state of any L1 row-probe is not in evidence).
- Row order is correct under `locate()` (live first, capture second); the row's only working leg was second — zero redundancy once live 403'd.

## Frozen kill rule

The receipt is final and nothing here amends it. At 09:58Z both listed URLs fetched errors, so the row was `NOT_LOCATED` and LOCATE (share 1.0, all 41 cited rows) failed. **The verdict stays FAIL** — ACCEPT-C-61 FAIL on LOCATE alone (13 of 14 legs PASS, 40/41 located). My post-hoc located results are diagnostic only, exactly as R61-M4 records.

## Net diagnosis

Claim C died on a double hit inside one ~1-minute measure window: a **structural** Cloudflare-403 live leg plus a **transient** archive.org error on the row's only backup URL. Either leg alone working would have passed the row. This is the second round (after R58, per R61-M4) where a transient archive error flips a claim with a no-slack live leg — a row whose sole non-live URL is one capture has zero redundancy under LOCATE share 1.0.

Instrumentation note (finding, low severity): `detail[:160]` truncation destroyed the capture's error class in the only artifact of the miss, making this diagnosis partly inferential; a longer or structured miss detail would have made transient-vs-structural decidable from the receipt alone.

No tools installed. No delegation, no background jobs, no git/jj writes, no `accept-c.py` run. Only lane write is this report; other files under `/fast/scratch/hyaku/kotodama-r61/w2/ReviewLocateS671/`.
