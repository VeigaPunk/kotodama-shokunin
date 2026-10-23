# RowS674 — one-row, one-clause review (WAVE 2: FALSIFY)

- URL: https://www.nwttimeline.ca/stories/2500-year-old-kamik-boot/ ("Kamik (Boot)", NWT Timeline, PWNHC)
- Quoted passage on the row: "Made over 2,500 years ago, this child’s boot or kamik is one of the oldest examples of footwear found in the Canadian Arctic."
- Clause under test: "A child's kamik made over 2,500 years ago is among the oldest footwear found in the Canadian Arctic."
- Method: plain curl/HTTP + text reader only (no headless browser, no challenge bypass). Measured revision lane bound respected; no writes in lane repo except this report.

## Findings (by severity)

### Severity: none (defects) — one informational byte-level nuance
- INFO — verbatim is exact at rendered-text level, with two U+00A0 non-breaking spaces in the raw HTML: the story-body `<p>` reads `Made over 2,500 years ago, this child’s boot or\u00a0kamik\u00a0is one of the oldest examples of footwear found in the Canadian Arctic.` (apostrophe is U+2019, matching the row quote). After NBSP→space normalization the full sentence matches the row's quote byte-for-word, 1 occurrence live and 1 in the checked archive capture. A strict raw-bytes comparator that does not normalize NBSP would miss the match; any rendering (browser, reader, copy-paste) yields the row's string exactly.

## (1) QUOTE — LOCATED
- Live fetch: HTTP 200, `text/html; charset=UTF-8`, 49,560 bytes compressed (curl, no redirect: final URL = requested URL).
- The sentence is verbatim body text of the story section, inside a `<p>` immediately following the paragraph on Pre-Dorset migration ("...Dorset sites in the NWT are rare.</p> <p>Made over 2,500 years ago, ..."). It is not navigation, not a caption, not a meta/JSON fragment (the og:description is different text — the "Four thousand years ago..." overview).
- Archive capture works: web.archive.org has ≥10 status-200 captures of this exact URL (2023-06-06 through 2025-08-04). Capture 20250804145602 fetched: HTTP 200, and contains the same sentence verbatim (after NBSP normalization) in the story body.

## (2) CLAUSE — SUPPORTED
Every part of the clause is carried by the page; nothing added, no hedge removed:
- "A child's kamik": page says "this child’s boot or kamik" and later "The small size is thought to reflect a child’s use." → supported.
- "made over 2,500 years ago": verbatim "Made over 2,500 years ago" → supported.
- "is among the oldest footwear found in the Canadian Arctic": page says "is one of the oldest examples of footwear found in the Canadian Arctic". "among the oldest" is a faithful rendering of "one of the oldest examples of" — no universal introduced, no hedge removed → supported.

Carrier text (≥10 consecutive words, 24 words), from the live page story body:
"Made over 2,500 years ago, this child’s boot or kamik is one of the oldest examples of footwear found in the Canadian Arctic."

## Residual risk
- One archive capture verified (2025-08-04); nine other 200 captures unchecked — low risk, the sentence is present in both the live page and the checked capture, and the page's modified_time is 2023-05-10, predating all captures.
- Raw-bytes-only matchers will report a mismatch due to the two U+00A0 characters; this is an encoding nuance, not a content difference.

## Verification gaps
- None material for this row. No installs performed; no processes left running.

QUOTE S674 LOCATED
CLAUSE S674 SUPPORTED
