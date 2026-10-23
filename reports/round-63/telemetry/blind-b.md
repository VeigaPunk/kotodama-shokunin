# Round 63 blind-support verification — blind-b (RevBlindB)

- Date: 2026-10-23
- Scope: rows S707, S708, S710, S711 (new rows landed in `corpus/SOURCES.md` under the headgear batch).
- Method: re-opened each row's live URL by ordinary fetch (read tool native/content-negotiation transport; curl used for byte-level fixed-string confirmation). Each row's archive capture URL re-opened with the read tool (sanctioned for archive.org under intermittent egress) and cross-checked with `curl --compressed` + `grep -F` byte verification of the exact anchor span.
- Verbatim rule: anchor span counted VERBATIM when the exact character sequence from the row appears in fetched body text (HTML entity encodings such as `&#8212;` counted as encoding of the same character).

## Verdicts

| Row | Verdict |
|---|---|
| S707 | SUPPORTED |
| S708 | SUPPORTED |
| S710 | SUPPORTED |
| S711 | SUPPORTED |

---

## S707 — Kenna Libes, "Chaperon," Fashion History Timeline, FIT

- Live: https://fashionhistory.fitnyc.edu/chaperon/ — fetched OK (read tool, native HTML; curl 200).
- Capture: https://web.archive.org/web/20260908133544id_/https://fashionhistory.fitnyc.edu/chaperon/ — fetched OK (read tool native replay; curl 200 decompressed).
- Identity: capture canonical = live canonical `https://fashionhistory.fitnyc.edu/chaperon/`; same title, same byline "Posted by Kenna Libes … Last updated Jan 2, 2026 | Published on Jan 19, 2020" on both ends.
- Anchor (row): details paragraph: "The liripipe, the long hanging portion of what was originally the hood"
- Live span (verbatim, under "## The Details"):
  > The liripipe, the long hanging portion of what was originally the hood, can be seen at the right side of figure 1, hanging over the man's left shoulder.
- Capture span (verbatim, identical paragraph):
  > The liripipe, the long hanging portion of what was originally the hood, can be seen at the right side of figure 1, hanging over the man's left shoulder.
- Byte check: `grep -c -F` of exact anchor string → live 1, capture 1.
- **Verdict: SUPPORTED.**

## S708 — Susan Brown, "Yoruba Complete," Cooper Hewitt

- Live: https://www.cooperhewitt.org/2015/06/25/yoruba-complete/ — fetched OK (read tool, native HTML; curl 200).
- Capture: https://web.archive.org/web/20260605232422id_/https://www.cooperhewitt.org/2015/06/25/yoruba-complete/ — fetched OK (read tool native replay; curl 200 decompressed).
- Identity: capture canonical = live canonical; same title "Yoruba Complete | Cooper Hewitt, Smithsonian Design Museum"; same meta-author "Susan Brown"; article body identical on both ends.
- Anchor (row): article body: "create appropriate wraps for different social occasions, and express her personal aesthetic."
- Live span (verbatim):
  > Re-tying the wrap each time allows a woman to keep up with fashion, create appropriate wraps for different social occasions, and express her personal aesthetic.
- Capture span (verbatim, identical sentence):
  > Re-tying the wrap each time allows a woman to keep up with fashion, create appropriate wraps for different social occasions, and express her personal aesthetic.
- Byte check: `grep -c -F` of exact anchor string → live 1, capture 1.
- Context supports the row gloss: Susan Brown signs as "Associate Curator in the Textiles Department" and the sentence names the *gèlè* head wrap; "retying lets women create occasion-appropriate gèlè wraps and express personal aesthetic" is a fair paraphrase.
- **Verdict: SUPPORTED.**

## S710 — Collins English Dictionary (2012 Digital Edition) via Dictionary.com, "tiara", British noun sense 1

- Live: https://www.dictionary.com/browse/tiara — fetched OK (read tool, native HTML; curl 200).
- Capture: https://web.archive.org/web/20240418022016id_/https://www.dictionary.com/browse/tiara — fetched OK (read tool native replay; curl 200 decompressed).
- Identity: capture canonical = live canonical `https://www.dictionary.com/browse/tiara`; both show a "tiara / British / noun" block with the same sense list (1. semicircular jewelled headdress; 2. Persian headdress; 3. RC Church sub-senses).
- Anchor (row): British noun sense 1: "a woman's semicircular jewelled headdress for formal occasions"
- Live span (verbatim, British noun sense 1):
  > a woman's semicircular jewelled headdress for formal occasions
- Capture span (verbatim, same British noun sense 1):
  > a woman's semicircular jewelled headdress for formal occasions
- Byte check: `grep -c -F` (ASCII and U+2019 apostrophe variants pooled) → live 1, capture 2 (capture carries the sense in both rendered HTML and embedded JSON).
- Attribution on live page (immediately following the British block; entity-encoded in HTML, hence invisible to the first fixed-string grep):
  > "Collins English Dictionary — Complete & Unabridged" / 2012 Digital Edition / © William Collins Sons & Co. Ltd. 1979, 1986 / © HarperCollins Publishers 1998, 2000, 2003, 2005, 2006, 2007, 2009, 2012
- Attribution nuance: the 2024-04-18 capture does not render the Collins 2012 footer block (page version predates it); it does embed a `CollinsEntry` JSON node for the British block, naming the same source. The anchor quote itself is present at both ends; the row's attribution is verified against the live page.
- **Verdict: SUPPORTED** (with the attribution nuance above recorded).

## S711 — "Academic dress," University of Oxford

- Live: https://www.ox.ac.uk/students/academic/dress — fetched OK via read tool (content negotiation returned text/markdown, full page). **Transport failure met-not-passed: direct curl of the live URL returned HTTP 403 twice (plain UA and full browser headers); ox.ac.uk WAF blocks curl.** Live verification therefore rests on the read-tool fetch, which returned the page with the anchor sentence verbatim.
- Capture: https://web.archive.org/web/20260925000816id_/https://www.ox.ac.uk/students/academic/dress — fetched OK (read tool native replay; curl 200 decompressed, byte-confirmed).
- Identity: capture canonical = live canonical; same title "Academic dress"; same page structure ("Your sub fusc", "Additional notes", "Academic gowns for students", …).
- Anchor (row): additional notes: "The mortar board may be worn outdoors but must be removed as you enter buildings and carried whilst indoors."
- Live span (verbatim, under "Additional notes"):
  > The mortar board may be worn outdoors but must be removed as you enter buildings and carried whilst indoors. Soft caps may be kept on indoors.
- Capture span (verbatim, identical bullet):
  > The mortar board may be worn outdoors but must be removed as you enter buildings and carried whilst indoors. Soft caps may be kept on indoors.
- Byte check: `grep -c -F` of exact anchor sentence → capture 1 (live not byte-greppable due to the curl 403 above; read-tool text carries the sentence character-for-character).
- Corroboration: both ends also carry the degree-ceremonies restatement "Mortar boards may be worn outside, but removed when inside and carried." — consistent with the row gloss.
- **Verdict: SUPPORTED.**

---

## Transport log

- archive.org egress: no failures encountered this run; all four `id_` captures fetched on first attempt via read tool and via curl.
- Pipeline artifact (self-caught, not an archive failure): `id_` capture bodies are gzip-encoded; the first curl round grepped compressed bytes and reported false 0-matches for S707-cap and S711-cap. Re-run with `curl --compressed` → 1 match each.
- Live ox.ac.uk: curl 403 (×2, with and without browser headers) — met-not-passed for that transport; read-tool fetch succeeded and carries the verbatim sentence. Recorded above under S711.
- No installs performed (no new tooling needed); pacman untouched.
