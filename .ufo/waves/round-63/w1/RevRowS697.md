# RevRowS697 — Blind SUPPORT verdict (claim C, row S697)

- Seat: kotodama-r63-w1-RevRowS697 (reviewer, leaf).
- Verdict: **SUPPORTED**.
- Object: row S697 draft (scribe kotodama-r63-w1-ScribeRowS697), subtopic Phrygian cap.
  - Live URL: `https://www.britannica.com/art/Phrygian-cap`
  - Capture: `https://web.archive.org/web/20260327023549id_/https://www.britannica.com/art/Phrygian-cap`
  - Draft quote: “soft felt or wool conical headdress fitting closely around the head and characterized by a pointed crown that curls forward” (20 normalised words; 8–25 OK)
  - Entry bullet: `- Phrygian caps use felt or wool and a pointed crown that curls forward, echoing their Anatolian origin and Greek artistic representation. (S697)`

## 1. Does the page carry the draft quote verbatim? YES
- Live page fetched by ordinary means (`read` tool, native GET, no browser): body opening paragraph reads
  `**Phrygian cap**, soft felt or wool conical headdress fitting closely around the head and characterized by a pointed crown that curls forward. It originated in the ancient country of Phrygia in Anatolia and is represented in ancient Greek art …`
- Located span (live, body text): `soft felt or wool conical headdress fitting closely around the head and characterized by a pointed crown that curls forward` — 20 normalised words; body prose, not caption/alt/title/meta.
- Base locator (frozen tool, not the held one): `python3 -B reports/round-61/reopen-quote.py "https://www.britannica.com/art/Phrygian-cap" "soft felt …"` → `LOCATED https://www.britannica.com/art/Phrygian-cap`, exit 0.
- Caveat (recorded): a direct `curl` to the live URL returned a Cloudflare “Just a moment…” challenge; the `read` tool fetch succeeded without a browser and the frozen locator reports LOCATED. Challenge met-not-passed for the raw-curl path; content verified by the ordinary read fetch.

## 2. Does the capture URL show the same page with the quote? YES
- Capture fetched via `read` on `https://web.archive.org/web/20260327023549id_/https://www.britannica.com/art/Phrygian-cap`:
  - Title: `Phrygian cap | Definition, History, & Facts | Britannica` (same page).
  - Body carries the identical opening paragraph including the quote verbatim
    (`… soft felt or wool conical headdress fitting closely around the head and characterized by a pointed crown that curls forward …`).
- CDX (`url=britannica.com/art/Phrygian-cap&filter=statuscode:200`) lists `20260327023549` with statuscode 200 and original `https://www.britannica.com/art/Phrygian-cap` — embedded original equals the live URL. Capture of the same page, same quote.
- NOTE: the frozen base locator against the capture URL prints `NOT_LOCATED … HTTPError` (URLError/HTTPError — transport failure on the archive replay, not absence of the quote). The quote's presence in the capture is verified directly by the ordinary read fetch; the locator's HTTP error is a transport limitation, not a content miss.

## 3. Does the entry line restate only what the quote carries? Mostly YES, one clause beyond the quoted span
- In-quote clause: `use felt or wool and a pointed crown that curls forward` — carried by the quote (felt/wool/pointed/crown/curls/forward as content-word subsequence in quote order; longest verbatim run 6 ≤ 12).
- Extra clause: `echoing their Anatolian origin and Greek artistic representation` — NOT inside the quoted span, but carried by the same page's body immediately after the quote (`It originated in the ancient country of Phrygia in Anatolia and is represented in ancient Greek art …`). Not invented; no dates/peoples/uses beyond the page.
- Normalised checks: bullet content words ≥ 5; ≥ 3 content words from the quote in quote order (felt, wool, pointed, crown, curls, forward); longest verbatim run 6 tokens (≤ 12). ROW cell is 11 columns, tier B, kind `docs`, status mined, opened 2026-10-23, recheck 180d, used-by entry path. Live page confirms `Last updated Sep. 7, 2026` (matches the row's “updated September 7, 2026”).

## Residual risks / verification gaps
- Capture timestamp (2026-03-27) predates the live article's last update (2026-09-07); the capture still carries the quote and describes the same page — no content mismatch observed, but the capture is not the freshest revision.
- Wayback replay intermittently refused connections/429s during this review; the capture was read successfully on completion.
- The frozen locator's capture-path HTTP error should be treated as a locator transport issue, not evidence against the row (quote visibly present in the capture's HTML body).
