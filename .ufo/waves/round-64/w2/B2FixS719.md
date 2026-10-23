# S719 row repair

## Behavior
Repaired the inherited S719 row in the scoped scratch artifact, retaining Cristia (2013) and its live URL. Removed the earlier section-heading locator and used a complete body sentence from Section 4's first paragraph (PDF p. 6). The title is no longer enclosed in quotation marks, so the row's first quoted text is the anchor sentence. Reworded the bullet to restate infant attention to IDS-like prosody.

## Corrected lines
```text
ROW: | S719 | Alejandrina Cristia, 2013. Input to Language: The Phonetics and Perception of Infant-Directed Speech. Language and Linguistics Compass 7(3):157–170 - https://pure.mpg.de/rest/items/item_1094677/component/file_1703379/content ; capture https://web.archive.org/web/20240415004434id_/https://pure.mpg.de/rest/items/item_1094677/component/file_1703379/content | paper | B | Infant-directed speech prosody (pitch and contour), vowel-space patterns, and links to infant attention and speech learning | Section 4, first paragraph: "The evidence summarized in Section 3 revealed that infants attend preferentially to IDS, and in particular to IDS-like prosody (with the aforementioned caveats)." | Helps worldbuilders portray IDS-like prosody as attention-grabbing without assuming that vowels are always clearer. | mined | 2026-10-23 | 180d | corpus/knowledge/linguistics/language-socialization-and-acquisition.md |
BULLET: - Infants attend preferentially to IDS-like prosody, helping caregivers attract a baby's attention. (S719)
VERIFY: LOCATED https://pure.mpg.de/rest/items/item_1094677/component/file_1703379/content
```

## Gates and evidence
- Required locator command, run from the lane root: `python3 -B reports/round-61/reopen-quote.py 'https://pure.mpg.de/rest/items/item_1094677/component/file_1703379/content' 'The evidence summarized in Section 3 revealed that infants attend preferentially to IDS, and in particular to IDS-like prosody (with the aforementioned caveats).'`
- Locator output (first line): `LOCATED https://pure.mpg.de/rest/items/item_1094677/component/file_1703379/content`.
- Re-opened the live PDF with a plain GET and read the extracted PDF text; the quoted sentence appears in Section 4's first body paragraph. Quote is 24 normalized tokens (the hyphenated `IDS-like` splits into `IDS` and `like`). The corrected row has 11 cells; the bullet has more than five content words, shares ordered content words with the quote, adds novel content, and has no copied run over 12 words.
- `accept-c.py` was not run; this seat's execution gate was the required locator, not full claim-C acceptance.

## Commands and outcomes
- `mkdir -p /home/vgpnk/.cache/hyaku/kotodama-r64/w2/FixS719` — succeeded.
- `curl -fLsS 'https://pure.mpg.de/rest/items/item_1094677/component/file_1703379/content' -o /home/vgpnk/.cache/hyaku/kotodama-r64/w2/FixS719/cristia-2013.pdf && file /home/vgpnk/.cache/hyaku/kotodama-r64/w2/FixS719/cristia-2013.pdf` — succeeded; `PDF document, version 1.3, 14 page(s)`.
- `printf '%s\n' 'The evidence summarized in Section 3 revealed that infants attend preferentially to IDS, and in particular to IDS-like prosody (with the aforementioned caveats).' | wc -w` — returned `23` whitespace-delimited words; the acceptance normalizer counts 24 because `IDS-like` splits at the hyphen.
- `curl -fsS 'https://archive.org/wayback/available?url=https://pure.mpg.de/rest/items/item_1094677/component/file_1703379/content'` — HTTP 429, exit 22.
- `curl -sS -L -o /dev/null -w 'HTTP %{http_code}\n' 'https://web.archive.org/web/20240415004434id_/https://pure.mpg.de/rest/items/item_1094677/component/file_1703379/content'` — could not connect to web.archive.org; HTTP 000, exit 7.
- `mkdir -p /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-64/w2` — succeeded.

## Provenance, limits, touched surfaces
The live source PDF was independently fetched and its body text re-opened. The same-page capture locator was inherited from the draft and its embedded original URL normalizes to the live URL, but the archive-availability API returned 429 and a direct GET to that capture could not connect; capture availability/content could not be independently confirmed. No tools were installed. No registry, corpus, judge, or other product files were edited; the lane-side write is this explicitly requested scoped report only.

Artifacts:
- `/home/vgpnk/.cache/hyaku/kotodama-r64/w2/FixS719/row.txt` — corrected labelled row artifact.
- `/home/vgpnk/.cache/hyaku/kotodama-r64/w2/FixS719/cristia-2013.pdf` — plain-GET source copy used to re-open the source.
- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-64/w2/B2FixS719.md` — this scoped findings report.
