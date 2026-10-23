# Round 62 W1 — ScribeHedgeOpen

## Scope and axis

**Axis:** depth (claim D), limited to footwear entry lines 63 (S692) and 75 (S666). The round-61 spot-check §7 routes both defects: the S692 wording closed the source's open list, and the S666 wording dropped “we have.” The frozen D counter requires the open-list and hedge clauses plus LINK/COPY checks; this report drafts those two lines only.

## Re-opened source evidence

Read `corpus/SOURCES.md` rows S666 and S692 and ran the specified base locator against each live URL and verbatim anchor quote. Both locator calls returned `LOCATED` and exit 0:

```text
timeout 300 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-61/reopen-quote.py 'https://www.dictionary.com/browse/sabot' 'a shoe made of a single block of wood hollowed out, worn especially by farmers and workers in the Netherlands, France, Belgium, etc.'; rc=$?; printf 'exit=%s\n' "$rc"; test "$rc" -eq 0
LOCATED https://www.dictionary.com/browse/sabot
exit=0

timeout 300 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-61/reopen-quote.py 'https://www.bbc.co.uk/programmes/articles/qsXBljJrnRm60Gdt2PR362/six-surprising-facts-about-the-history-of-high-heeled-shoes' 'The earliest evidence we have of someone wearing heels is from a 10th-century Persian bowl.'; rc=$?; printf 'exit=%s\n' "$rc"; test "$rc" -eq 0
LOCATED https://www.bbc.co.uk/programmes/articles/qsXBljJrnRm60Gdt2PR362/six-surprising-facts-about-the-history-of-high-heeled-shoes
exit=0
```

The locator quote for S692 is the Dictionary.com sense 1 anchor; it ends “Netherlands, France, Belgium, etc.” The S666 anchor is the BBC article's section 2 quote and contains the hedge “we have.”

## Drafts and LINK/COPY arithmetic

These are proposed lines, not edits to the entry. Arithmetic follows `accept-d.py`'s normalization and content-word definition (4+ characters, excluding its STOP words and digit-only tokens); LCS requirement is `max(4, ceil(0.4 × content count))`.

**Line 63 / S692**

```text
- A shoe made from one block of wood, hollowed out and worn especially by farmers and workers in the Netherlands, France, Belgium, etc. (S692)
```

- Content words (11): `shoe, block, wood, hollowed, worn, especially, farmers, workers, netherlands, france, belgium`.
- Shared content words (11): `shoe, block, wood, hollowed, worn, especially, farmers, workers, netherlands, france, belgium`.
- LCS: 11; LCS share 11/11 (100%); required minimum 5.
- Longest consecutive quote-word run: 12 (`worn especially by farmers and workers in the Netherlands, France, Belgium, etc.`).
- Keeps the quote's open country list with `Belgium, etc.`.

**Line 75 / S666**

```text
- The earliest evidence we have for someone wearing heels is from a 10th-century Persian bowl. (S666)
```

- Content words (9): `earliest, evidence, someone, wearing, heels, 10th, century, persian, bowl`.
- Shared content words (9): `earliest, evidence, someone, wearing, heels, 10th, century, persian, bowl`.
- LCS: 9; LCS share 9/9 (100%); required minimum 4.
- Longest consecutive quote-word run: 10 (`someone wearing heels is from a 10th-century Persian bowl`).
- Retains the source hedge `we have`; the draft changes “evidence … of someone” to “evidence … for someone” and keeps the cited claim's meaning.

Both drafts meet the counter's stated LINK thresholds and the 12-word COPY ceiling by this arithmetic. This is not an ACCEPT-D run or a full claim verdict.

## Gates, touched surfaces, and limits

- **Gate exercised:** base locator for S692 and S666 quotes only; each `LOCATED`, exit 0 as recorded above.
- **Not exercised:** `accept-d.py`, its other legs, source-access/lint gates, or the full claim predicate. No D receipt or claim pass is asserted.
- **Read surfaces:** `reports/round-62/claims.json`; `corpus/lessons/round-61-verifier-spotcheck.md` §7; S666/S692 in `corpus/SOURCES.md`; footwear entry lines 63 and 75; relevant D-counter requirements and locator implementation.
- **Product changes:** none by this seat; the entry was not edited. No tools installed. Lines 74 and 93, talaria sourcing, registry changes, ACCEPT-O, controls, and other D work are out of scope here.
- **Artifact:** `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-62/w1/ScribeHedgeOpen.md`.
