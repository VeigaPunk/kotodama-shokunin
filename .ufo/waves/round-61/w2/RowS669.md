# RowS669 — one-row one-clause support review (round 61 WAVE 2: FALSIFY)

- Seat: KotodamaR61.RowS669 (leaf; no delegation, no background jobs).
- Page: https://www.nippon.com/en/guide-to-japan/gu020004/ ("The “Genkan”: Japan’s Traditional Entryway and Footwear Etiquette", nippon.com, published 2024-08-20, series "A Basic Guide to Japanese Etiquette").
- Measured by ordinary means only: `read` (reader mode) + `curl` raw HTML. No headless browser; no challenge encountered.
- Installs: none.

## (1) QUOTE — LOCATED

Live fetch: HTTP 200, 20,538 bytes (curl, final URL unchanged). Archive capture works: Wayback snapshot chain returns HTTP 200; the archive.org availability API itself returned 429 (host rate limit) and was not needed.

Raw HTML, first `<p>` of the article body (tag-stripped text is exactly the quoted passage):

> Many people in other countries are by now well-acquainted with the Japanese custom of removing footwear before entering a home. The same applies to <em><a href="https://www.nippon.com/en/features/jg00092/">ryokan inns</a></em>, temples, and even restaurants with tatami-floored rooms.

- Row passage: "Japanese custom of removing footwear before entering a home. The same applies to ryokan inns, temples, and even restaurants with tatami-floored rooms".
- Match: verbatim consecutive body text. The quote starts mid-sentence (omits the lead-in "Many people in other countries are by now well-acquainted with the") and ends before the sentence-final period after "rooms" — truncation at the edges only; every quoted character matches, including "even". "ryokan inns" is italicized/linked in the source; the words themselves are unaltered.
- It is the opening paragraph of the article body (under H2 "Climate-Adapted Architecture"), not navigation, not a caption, not the meta description.

## (2) CLAUSE — SUPPORTED

Clause: "Japan's footwear-removal custom for entering a home extends to ryokan inns, temples, and restaurants with tatami-floored rooms."

Carrying page text (15+ consecutive words of body text):

> …well-acquainted with the Japanese custom of removing footwear before entering a home. The same applies to ryokan inns, temples, and even restaurants with tatami-floored rooms.

- "Japan's footwear-removal custom for entering a home" = "the Japanese custom of removing footwear before entering a home" — same referent, nothing added.
- "extends to" = "The same applies to".
- All three extensions present: ryokan inns / temples / restaurants with tatami-floored rooms.
- Nothing added: no date, place, cause, comparison, or universal quantifier introduced. The page's "Many people in other countries are by now well-acquainted…" (international familiarity) and the page's causal follow-up ("Since in traditional homes people sat on the floor…") are simply not asserted by the clause.
- The clause drops the intensifier "even" before "restaurants". "Even" marks these restaurants as an unexpected extension; removing it removes emphasis, not factual content — the set of covered venues is unchanged, so the clause is not stronger than the page.

No defect found on this row.

## Residual risk / verification gaps

- Wayback availability API was rate-limited (429) from this host; archive reachability is attested via a direct snapshot request (HTTP 200) rather than the CDX/availability metadata.
- Verbatim check is against today's live rendering and raw HTML; the page shows article:modified 2026-01-17, so an older capture quoted in the row could differ in wording — not checkable without the row's original capture date, which is not recorded here.

QUOTE S669 LOCATED
CLAUSE S669 SUPPORTED
