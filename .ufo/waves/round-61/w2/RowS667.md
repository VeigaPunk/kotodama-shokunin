# Row S667 — one-row one-clause review

- Page: https://jpsearch.go.jp/en/gallery/ndl-GZqzDNvVK0a ("Japanese Wooden Clogs - Japan Search")
- Fetch: HTTP 200 via curl (live page, 2026-10-23); reader-mode extraction also succeeded. No archive capture needed.
- Measured revision context: lane repo efbee29c; this seat is review-only.

## (1) QUOTE

Quoted passage: "Traditional Japanese footwear can be roughly divided into two groups: zori sandals and geta wooden clogs."

Raw HTML contains verbatim: `Traditional Japanese footwear can be roughly divided into two groups: ` immediately followed by `*zori* sandals and *geta* wooden clogs.` (the page italicizes *zori* and *geta*; stripping the emphasis markup yields the quoted text exactly). It sits in the second body paragraph of the article — running prose, not navigation, not a caption fragment.

Verdict: LOCATED.

## (2) CLAUSE

Clause: "Traditional Japanese footwear is roughly divided into zori sandals and geta wooden clogs."

Page text carrying the clause (>= 10 consecutive words):
"Traditional Japanese footwear can be roughly divided into two groups: zori sandals and geta wooden clogs."

Check per element:
- "Traditional Japanese footwear" — present verbatim.
- "roughly divided" — present ("can be roughly divided"); dropping "into two groups" adds nothing.
- "zori sandals and geta wooden clogs" — present verbatim as the two named groups.
- Nothing added: no date, place, cause, comparison, universal, or hedge introduced; no hedge removed (the clause preserves "roughly").

Verdict: SUPPORTED.

## Install/update record

None — no tools installed or updated for this review.

QUOTE S667 LOCATED
CLAUSE S667 SUPPORTED
