# ReviewerEntryDraft — round 82 w1 report (claim-D review seat)

Verdict: ACCEPT — claim-D entry clears QUALITY 1-5 and 15 on the installed bytes
(`corpus/knowledge/myth-symbol/guest-right-hospitality-law.md`, 29,020 B; lint
`CITED-LINES: 0 finding(s) in 1 file(s)`, exit 0). One routed defect in the round's
records (Gate draft tier typo), two craft weaknesses with minimal edits, S907 refute
discipline compliant.

## Reviewed object and motion

Reviewed the w1 draft
`.ufo/waves/round-82/w1/drafts/corpus/knowledge/myth-symbol/guest-right-hospitality-law.md`
(29,046 B at read; the draft appeared mid-flight at 08:2x), then re-measured the installed
file after the L1's ACCEPT-D-82 (29,020 B). Sole diff: line 91's S907 etymology quote
trimmed from 「cognate with Lat. hostis, originally a stranger, hence enemy」 to
「originally a stranger, hence enemy」 (receipts/diff-draft-vs-installed.txt). All findings
below were re-checked against the installed line numbers and hold.

## QUALITY 1-5 (deciding lines on the installed file)

1. Provenance — PASS. Line 7 (`- source:`): "no source outside that list is used for a
   factual claim". 22 §3 bullets (lines 70-91), one S-id each; quotes bound to ids in
   `stage/ScribeEntry/quote-check.txt` (22/22 OK, quote_exit=0) with located passages in
   `fetch-records.md`. Gap-fill counts re-derived at base `c285b2af…`: 255 md, 0 filename
   hits, 27 vocab lines / 15 files, 0 institutional core, 4-hit `ritual` control — all as
   the entry claims (receipts/corpus-refs-and-gap-counts.txt).
2. Calibration — PASS. Line 7 ("Anything the rows do not settle is labelled craft,
   method, or `(to-verify)`") and line 10 (`- scope:` "reference method and lane policy").
   Frazerian hazard kept out by the Gate's S908 reject; no pop-mythography in the entry.
3. Coupling — PASS. Line 6 (`- couples:`, 9 files) + §1 lines 14-23 (10 owners). All 15
   cited corpus line refs read at base and each matches the entry's claim; the two
   handoff/coupled files exist (ordeal-judicial-proof-rituals.md,
   synthesis/worldbible-integration-contract.md).
4. Usability — PASS. Decision table (25-36), lexicon tables + derivation (38-60),
   12-item checklist (93-106), worked example (108-124).
5. Canon hygiene — PASS. Line 126 ("decides nothing about what is true in any world"),
   line 124 ("Decides nothing about any world; demonstrates the checklist"), PROVINCE
   sentence at line 10.

## QUALITY 15

`python3 -B tools/check-cited-lines.py <installed>` → `CITED-LINES: 0 finding(s) in 1
file(s)`, exit 0 (receipts/citedlines-installed.txt). Independent sweep: 22 cited lines,
exactly one distinct id each; 0 lines with ≥2 distinct ids; 22 table rows, 0 with an S-id.
No MULTI-ID line or TABLE-ID row exists to name.

## Craft attack (two weakest sections)

W1 — §2.1 worked derivation (50-64): the entry's own example sentences use -m (dative),
-eth (eldership) and the loan šen, none in the stated three-suffix morphology, so a
worldbuilder cannot parse/extend the examples; and §5's guest-class compounds (dawan-oph
etc.) are never given a derivational rule in §2.1, so the degree ladder §2 row 1 requires
cannot be lexicalized from §2.1 as written. Smallest edit: two sentences (declare -m/-eth/
šen as non-derivational register/case morphology; state that guest-classes compound on the
guest-term).
W2 — violation-consequence row (line 33) and violation-term row (line 47): the five
consequences read as a pick-one menu while the checklist (line 100) and worked example
(line 121) treat them as a stacked, priced ladder — a table-only reader builds a one-rung
culture; and line 47's "which of those can be redeemed?" is never answered anywhere
(grep: "redeem" occurs only at line 47). Smallest edit: prepend "rungs, not alternatives —
stack and price (§5)" to the line-33 consequence cell; one sentence on redemption/Vethari
in the line-47 row.

## S907 QUALITY 27 discipline — compliant; one routed defect

The Gate draft names `reports/round-82/evidence/S907.txt`, the span 「one who receives
hospitality in the house of another」, and a presence finding ("present once after
whitespace folding in body and capture"; live-body grep line 518 inside
`div.prp-pages-output`; capture raw-count-0/ folded-count-1 nuance recorded). UA binding
per QUALITY 22: `UA "curl/8.23.0" -> HTTP 200, 60273 B, wall absent` and the browser-shaped
UA -> HTTP 200, 60273 B, byte-identical (sha256 f6db75f3…); capture 29020 B (sha256
37a3eb42…); same-namespace positive control (Ordeal, 87131 B, 3374 words) per QUALITY
21+24; automation: none.
ROUTED DEFECT: the Gate draft's supersede bullet says "Disposition: mined, tier B" while
the rows draft's S907 row carries tier C (`drafts/rows/S904-S907.md:raw:4`) and the same
paragraph then says "the tier is C on that ground". One-word fix ("tier B"→"tier C") in
the Gate draft before install, else the lesson contradicts the SOURCES row.
Observations (non-blocking): Gate draft's "28992 B" entry measure is stale (installed
29,020 B — re-measure or drop byte counts of a moving draft); carried heraldry reject
lacks the literal present/absent word (add "present" at install for shape cleanliness).

## Unrun / out of scope

Live re-fetch of the four URLs (scribe's scratch bytes deleted at yield; I verified
records, not live pages). Claim-O tool is ExecEvidence's object; its selftest-fixture
finding is with the tool owner. No tools installed this seat (nothing new needed).

## Files written

- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/stage/ReviewerEntryDraft/review.md` (full review)
- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/stage/ReviewerEntryDraft/receipts/citedlines-installed.txt`
- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/stage/ReviewerEntryDraft/receipts/corpus-refs-and-gap-counts.txt`
- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/stage/ReviewerEntryDraft/receipts/diff-draft-vs-installed.txt`
- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/stage/ReviewerEntryDraft/receipts/corpus-refs-first-pass-garbled.txt`
- This report: `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/ReviewerEntryDraft.md`
Scratch `/fast/scratch/hyaku/kotodama-r82/ReviewerEntryDraft` removed at yield.
