# RevRowS698 — blind support review (round 63, w1)

Sub-agent: kotodama-r63-w1-RevRowS698 (reviewer leaf; UFO-FSD review contract).
Item: claim C row S698 (frozen LIVE subset; subtopic: crown as regalia — encircling headpiece of sovereignty and its materials).
Scratch: /fast/scratch/hyaku/kotodama-r63/RevRowS698/

## Blind-support start condition
The designated scratch dir `/fast/scratch/hyaku/kotodama-r63/ScribeRowS698/` did not exist at my start (checked; empty), so per the assignment I proceeded to an independent search for a page on the same subtopic, and additionally requested the scribe's draft. The scribe (kotodama-r63-w1-ScribeRowS698) supplied their final draft rows live (see below), which I re-verified independently by ordinary means. This report reviews THAT drafted row (the object under review), with the independent verification documented.

## Drafted row under review (scribe's final artifacts, relayed 2026-10-23)
- Row: `| S698 | Collins English Dictionary — Complete & Unabridged, HarperCollins Publishers, 2012 Digital Edition (served by Dictionary.com; British noun sense 1) — https://www.dictionary.com/browse/crown ; capture https://web.archive.org/web/20260412094355id_/https://www.dictionary.com/browse/crown | docs | A | lexical definition of crown as sovereign headgear and materials (British noun sense) | British noun sense 1: "an ornamental headdress denoting sovereignty, usually made of gold embedded with precious stones" | Collins defines a crown as sovereign ornamental headwear and describes gold and precious-stone materials | mined | 2026-10-23 | 180d | corpus/knowledge/culture-material/headgear-head-covering-codes.md |`
- Entry bullet: `- A crown symbolizes sovereignty in gold and precious stones. (S698)`
- Gate line: `- S698 | https://www.dictionary.com/browse/crown | 2026-10-23 | "an ornamental headdress denoting sovereignty, usually made of gold embedded with precious stones"`

## Verdict
**SUPPORTED** (as drafted; with one transport-limitation caveat on the capture leg, detailed below — the quote IS verified in the capture body by ordinary means; the canonical locator's capture pass was blocked by archive.org 429 rate-limiting, not by absence).

## Evidence

### 1. Live URL — quote located (canonical locator)
Plain ordinary-method runs (canonical locator `reports/round-61/reopen-quote.py` from the lane repo; NOT the held `tools/reopen-row.py`):

- `python3 -B reports/round-61/reopen-quote.py 'https://www.dictionary.com/browse/crown' 'an ornamental headdress denoting sovereignty, usually made of gold embedded with precious stones.'` → `LOCATED https://www.dictionary.com/browse/crown`, exit 0. (Collins British noun sense 1 quote.)
- Same command with the American sense quote `any of various types of headgear worn by a monarch as a symbol of sovereignty, often made of precious metal and ornamented with valuable gems.` → `LOCATED`, exit 0 (double-check; the scribe's earlier draft).

Live page fetched independently by me (156,742 bytes, HTTP 200, ordinary curl). Quote present verbatim in visible body — `<div class="def">` (American sense) and `<p class="txt-variant-label-short">` under the British entry card (Collins sense). Both normalise-equal to the drafted quotes. The same string also appears in the `<meta name="description">` and `<title>` (page metadata), but the body definition spans are the substantive occurrences and are genuine definition text, not captions/alt/title/meta.

### 2. Capture URL — same page carries the quote (ordinary means)
CDX query (statuscode:200, limit -5): five captures; the newest, `20260412094355`, matches the row's capture `id_` URL and its embedded original URL equals the live URL (same-identity; verified via the `id_` fetch, final URL = `https://web.archive.org/web/20260412094355id_/https://www.dictionary.com/browse/crown`).

Capture fetched by me (81,772 bytes via ordinary curl). The Collins quote occurs exactly once in the body: `<p class="txt-variant-label-short">an ornamental headdress denoting sovereignty, usually made of gold embedded with precious stones</p>`, inside the "crown 1 British" entry card (`<em class="txt-entry-group-type british">British &nbsp;</em>`, IPA `/ kraʊn /`, `<h2>noun</h2>`, `<ol class="list-definition">` with 6 items, quote at item 0). The `<cite class="ftr-british-group">"Collins English Dictionary — Complete & Unabridged" 2012 Digital Edition …</cite>` ends the same British entry — consistent with the row's title/publisher attribution. Normalised capture-span == normalised quote (13 words): `an ornamental headdress denoting sovereignty usually made of gold embedded with precious stones`.

**Transport caveat (limitation, not absence):** the canonical locator against the capture returned `NOT_LOCATED … HTTPError` (HTTPError 429 Too Many Requests) repeatedly, including after backoffs (>45s) — web.archive.org rate-limits python-urllib carrying the locator's desktop-Firefox UA today; the same UA gets 429 even with `Accept-Encoding: identity` and `Connection: close`, while plain `curl` (default UA) succeeds and one urllib probe with UA `curl/8.5.0` succeeded (status 200, 13,803 bytes). So the capture leg's locator pass was not obtainable in this window; this is transport 429, not quote-absent, and the capture body is directly verified above. Scribe's report should record this as met-not-passed for the locator-on-capture step. The frozen LIVE leg (claim C) runs the locator on the **live** URL for S698, which passes; the risk is the row-level "locator confirms quote on the capture too" rule if the 429 persists at gate time (attach this report's capture digest: 81,772 bytes, quote once in the body, normalise-equal).

### 3. Quote shape
13 normalised words (8–25 ✓). Verbatim body definition, not caption/alt/title/meta (the body spans are the actual definitions; the identical meta description string is incidental).

### 4. Entry-line restatement
Draft: `- A crown symbolizes sovereignty in gold and precious stones. (S698)`

- Exactly one S-id ✓
- Content words (≥4 letters, non-stopword): crown, symbolizes, sovereignty, gold, precious, stones — 6 ≥ 5 ✓
- ≥3 content words in quote in quote order: sovereignty(4), gold(8), precious(11), stones(12) — 4, in order ✓
- At most 12 consecutive words copied verbatim: longest in-quote streak in the entry = 2 ("precious stones") ≤ 12 ✓
- No invented claims: "crown" = page headword; "symbolizes" = paraphrase of "denoting"; "sovereignty / gold / precious stones" all made the quote's own words ✓

### 5. URL reuse / collisions
`https://www.dictionary.com/browse/crown` — grep over corpus/SOURCES.md: no match (not previously in the registry). No other scribe's URL known to equal it (the scribe's own report confirms it is their choice for S698; no peer has claimed dictionary.com/browse/crown in any artifact I saw). Capture's embedded original URL == live URL (same-identity rerouting: N/A — no rerouting; identical).

## Residual risk / verification gaps
1. Locator-on-capture blocked by archive.org 429 (above). If it persists at gate time, the row may fail the capture-confirmation rule despite the quote being genuinely in the capture; recommend closure/L1 use the attached digest or re-run when the rate limit clears (frozen three-attempt budget per URL covers 429/5xx/timeout/connection-error retries, so a later successful run within budget is legitimate).
2. I did not obtain the scribe's final write of the registry/entry (the scribe provides the row; L1 assembles). My verdict applies to the exact drafted artifacts quoted above; if the L1 alters the quote or entry wording, re-verify.
3. Topic fit: crown as regalia/materials — the Collins British sense ("ornamental headdress denoting sovereignty, usually made of gold embedded with precious stones") directly covers sovereignty + materials; matches S698 subtopic.

## Checks not run (why)
- `tools/reopen-row.py` — under safety hold; never run (per instructions).
- No edits made to the lane repo or the fleet repo; only this report and my scratch files were written.
