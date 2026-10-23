VERDICT KotodamaR62.ResidLine93S693: HOLDS

Seat: KotodamaR62.ResidLine93S693 (read-only, no delegation, no installs made).
Measured revision: a2c5caa59b2d67ce35e53d6ce0217030a66cdd48 (branch main).
Freeze: 9143fc44. FIN: claim D (depth), line 93 ↔ S693. All evidence collected by ordinary means (curl/python), no browser automation.

---

## 1. S693 row content (corpus/SOURCES.md, line 648)

Row S693 (verbatim):
`| S693 | talaria, Dictionary.com (American entry; page date not shown) — https://www.dictionary.com/browse/talaria ; capture https://web.archive.org/web/20240529024530id_/https://www.dictionary.com/browse/talaria | docs | B | Dictionary.com's American sense of talaria in Classical Mythology: what the word denotes and whose attribute it is | American entry, plural noun, Classical Mythology sense: "the wings or winged sandals on the feet of Hermes, or Mercury." | Dictionary.com defines talaria as the wings or winged sandals on the feet of Hermes (Mercury). | mined | 2026-10-23 | 180d | corpus/knowledge/culture-material/footwear-codes-terminology.md |`

Line 93 of corpus/knowledge/culture-material/footwear-codes-terminology.md (raw):
`- Talaria are the wings or winged sandals worn on the feet of Hermes, or Mercury. (S693)`

## 2. Both URLs re-opened (ordinary means) — HOLDS

Command (live):
`curl -sS -L --max-time 90 -A "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0" -o live-talaria.html -w "HTTP %{http_code} final=%{url_effective} bytes=%{size_download}\n" "https://www.dictionary.com/browse/talaria"`
Output: `HTTP 200 final=https://www.dictionary.com/browse/talaria bytes=70599`

Command (capture):
`curl -sS -L --max-time 120 -A "Mozilla/5.0 ..." -o wayback-talaria.html -w "HTTP %{http_code} final=%{url_effective} bytes=%{size_download}\n" "https://web.archive.org/web/20240529024530id_/https://www.dictionary.com/browse/talaria"`
Output: `HTTP 200 final=https://web.archive.org/web/20240529024530id_/https://www.dictionary.com/browse/talaria bytes=246054`

## 3. Quote: body text, verbatim, 8–25 words — HOLDS

Quote: `the wings or winged sandals on the feet of Hermes, or Mercury.`
Word count (alphabetic tokens): **12** → within 8–25. ✓

LIVE (dictionary.com/browse/talaria), one body occurrence, byte-exact, inside the visible definition list:
`<ol class="list-definition hide-ordinal"> ... <li class="item-definition"> <p class="txt-variant-label-short"> the wings or winged sandals on the feet of Hermes, or Mercury. </p>`
preceded by `<div class="box-posb-label"><em>Classical Mythology.</em></div>`. Not a caption, not JSON-LD, not `<meta>` (the identical sentence also appears in `<meta name="description">`, but the body occurrence independently exists).

WAYBACK (id_ capture), one body occurrence, byte-exact:
`<section ... data-type="part-of-speech-module"><h2>plural noun</h2><div>, <i>Classical Mythology.</i></div><ol data-type="definition-content-list"><li><span><div><div> <!-- -->the wings or winged sandals on the feet of Hermes, or Mercury.</div>`

Anchor fields check: "American entry" (page prints `talaria American [t uh - lair -ee- uh ] … plural noun Classical Mythology.`), "plural noun" (h2), "Classical Mythology sense" (em label) — all present on both payloads. ✓

## 4. Capture is of the same page and past-dated — HOLDS

- Wayback canonical link inside capture: `<link data-react-helmet="true" href="https://www.dictionary.com/browse/talaria" rel="canonical"/>` — identical to live page canonical. Same `<title>` ("TALARIA Definition & Meaning | Dictionary.com"), same definition sentence byte-for-byte. Same page. ✓
- `curl -sSI` headers on the capture:
  - `memento-datetime: Wed, 29 May 2024 02:45:30 GMT` (matches URL timestamp 20240529024530)
  - `x-archive-orig-date: Wed, 29 May 2024 02:45:30 GMT`
  - `link: <https://www.dictionary.com/browse/talaria>; rel="original", ...`
  - Past-dated vs 2026-10-23. ✓

## 5. Tier B judgment — HOLDS

Claim scope: "Dictionary.com's American sense of talaria in Classical Mythology: what the word denotes and whose attribute it is." For that scope Dictionary.com (an aggregating lexical site; the American entries derive from the Random House Unabridged Dictionary — page footer: "Definitions and idiom definitions from Dictionary.com Unabridged, based on the Random House Unabridged Dictionary, © Random House, Inc. 2023") is a strong secondary reference, not primary/authoritative. QUALITY.md criterion 6: tier A reserved for sources primary or authoritative for the exact scope; publisher/secondary descriptions are B. Lane precedent: S692 (same publisher, Random House Unabridged ©2023, same dictionary definition genre) is filed B; S688 (Yates 1875, primary text on talaria in art) is also B. B is correct for S693. ✓

Kind: `docs` describes the web page. LOW/consistency note (not a predicate violation): S692 files the same Random House-derived dictionary entry as `book`; S693's source cell does not name Random House, so `docs` is defensible, but the two sibling rows are stylistically inconsistent. Smallest fix: name "Random House Unabridged Dictionary" in S693's source cell and file kind `book` to match S692, or add a kind legend to SOURCES.

## 6. Line 93 restates ONLY what the quote says — HOLDS

Quote: "the wings or winged sandals on the feet of Hermes, or Mercury."
Line 93: "Talaria are the wings or winged sandals worn on the feet of Hermes, or Mercury."
- "Talaria are …" — definitional framing of the same quoted gloss (the quote is the dictionary definition of talaria).
- "worn" — added; entailed by "on the feet" for wings/sandals. No additional fact (no origin, no material, no exclusivity) beyond the quote. Restates only the quote's content. ✓
(If a stricter reading were wanted, smallest fix: drop "worn" — not required.)

## 7. S687 row differs from d42ffb89 only in its used-by cell — HOLDS

Command (sandbox clone, GIT_DIR/GIT_WORK_TREE/GIT_INDEX_FILE unset):
`git -C /fast/scratch/hyaku/kotodama-r62/resid/KotodamaR62.ResidLine93S693/clone diff d42ffb89 a2c5caa59b2d67ce35e53d6ce0217030a66cdd48 -- corpus/SOURCES.md`

Full hunk for S687 (only line changed in that row):
```
-| S687 | Hermes Estate & Attributes, Theoi Greek Mythology (author and date not shown) — https://www.theoi.com/Olympios/HermesTreasures.html | docs | C | Theoi's summary of Hermes' winged boots and Greek/Latin terminology |  WINGED BOOTS & CAP OF HERMES section, first sentence: "Hermes wore winged, short leather boots called by the Greeks pteroeis pedila and by the Romans talaria." | Theoi says Hermes wore winged short leather boots, called pteroeis pedila by Greeks and talaria by Romans. | mined | 2026-10-23 | 180d | corpus/knowledge/culture-material/footwear-codes-terminology.md |
+| S687 | ... [identical cells] ... | mined | 2026-10-23 | 180d | — |
```
Every other cell byte-identical; only the trailing used-by cell changed `corpus/knowledge/culture-material/footwear-codes-terminology.md` → `—`. The diff's only other hunk is the S693 row addition. ✓

## 8. Supporting observations (claim D context)

- S693: status `mined`, opened 2026-10-23, used-by the footwear entry, lists the live URL and the capture. ✓
- In the entry, line 93 is the sole citation of S693 (grep of corpus/knowledge for `S693` matches only line 93) → one S-id per line (QUALITY criterion 15 clause-scoping). ✓
- No rows S694–S699 exist; the claim's "one new tier A/B row S693-S699" is satisfied by S693 alone. ✓
- The live page still carries the same definition today (2026-10-23), so the capture and the live URL agree.

## Severity findings

- None high/medium. Two LOW/consistency notes: (a) kind `docs` vs S692's `book` for the same Random House-derived dictionary genre (fix above); (b) "worn" on line 93 is an entailment-level addition (fix: omit, optional).

## Residual risk / verification gaps

- I did not re-run the claim's acceptance counter (final-measures.txt is the sole authoritative record; my runs were reproductions/attacks only).
- I did not independently evaluate round 61's footwear TOPIC rule (out of this seat's assigned items); the S693 quote satisfies the cited literal requirements (names talaria and Hermes).
- Dictionary.com is a live site; the frozen verification anchor is the 2024-05-29 capture, which I verified byte-exact against the live body text today.
