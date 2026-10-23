# B2ReviewRowS719 — falsification review of inherited draft S719

Draft under review: `/home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRowS719/row.txt` (wave-1 output, unverified).
Counter: `reports/round-64/accept-c.py` legs ROWS and RESTATE.
Access: plain `curl -sL` GET, no challenge, no login; 2026-10-23.

## HTTP results (verbatim)

- Live: `HTTP 200 https://pure.mpg.de/rest/items/item_1094677/component/file_1703379/content application/pdf; charset=UTF-8 327063` — PDF 1.3, 14 pages.
- Capture: `HTTP 200 https://web.archive.org/web/20240415004434id_/https://pure.mpg.de/rest/items/item_1094677/component/file_1703379/content application/pdf; charset=UTF-8 327063` — same byte count as live.

## Lane locator

`python3 -B reports/round-61/reopen-quote.py 'https://pure.mpg.de/rest/items/item_1094677/component/file_1703379/content' 'The evidence summarized in Section 3 revealed that infants attend preferentially to IDS, and in particular to IDS-like prosody'`
→ first line: `LOCATED https://pure.mpg.de/rest/items/item_1094677/component/file_1703379/content` (exit 0).

## Verdict table

| field | draft value | verified? | evidence (verbatim) | required fix |
|---|---|---|---|---|
| live URL | `https://pure.mpg.de/rest/items/item_1094677/component/file_1703379/content` | yes | `HTTP 200 … application/pdf … 327063`; pdftotext header `Language and Linguistics Compass 7/3 (2013): 157–170, 10.1111/lnc3.12015` | none |
| archive capture | `web.archive.org/web/20240415004434id_/…` | yes | `HTTP 200 … application/pdf … 327063` (same size as live); CAPTURE_RE matches at end of source cell, `norm_url(original)==norm_url(live)` | none |
| kind / tier | `paper` / `B` | yes | Peer-reviewed review article in *Language and Linguistics Compass* (Blackwell); a survey = "strong secondary" B for the named scope; A would require the primary experiments it cites | none |
| scope | IDS prosody (pitch/contour), vowel-space, links to infant attention & learning | yes | Abstract: "to outline the first comprehensive empirical picture of infant-directed speech and its effects on language acquisition"; §2.1 prosody, §2.2 segmental/vowel, §3 preference | none |
| anchor quote (human check) | "The evidence summarized in Section 3 revealed that infants attend preferentially to IDS, and in particular to IDS-like prosody" | yes in body text | pdftotext line 246ff: `4. Effects of IDS on Performance \| The evidence summarized in Section 3 revealed that infants attend preferentially to IDS, \| and in particular to IDS-like prosody (with the aforementioned caveats).` — first sentence of §4 body, contiguous, not heading/caption/nav; 20 normalised words | none for the quote itself |
| **anchor cell as counter sees it** | `Section 4, “Effects of IDS on Performance”: "…"` | **NO — FAIL** | Counter `QUOTE_RE.search` returns earliest match: curly-quoted `“Effects of IDS on Performance”` precedes the evidence quote. Simulated `anchor_quote(cell)` → `'Effects of IDS on Performance'` = **5 words** → ROWS `S719:quote_words=5` FAIL (needs 8–25). Same 5-word string becomes the RESTATE quote: bullet content words share 0 in-order words with `[effects,of,ids,on,performance]` → `in_order=0` FAIL | strip quotes from the locator or move it after the evidence quote, e.g. `Section 4 (Effects of IDS on Performance): "The evidence summarized…"` |
| citation | Alejandrina Cristia, 2013, "Input to Language: The Phonetics and Perception of Infant-Directed Speech", LLC 7(3):157–170 | yes | PDF header verbatim: `Language and Linguistics Compass 7/3 (2013): 157–170`, title and `Alejandrina Cristia` as sole author | none |
| opened / recheck / status / used-by | `2026-10-23` / `180d` / `mined` / entry path | yes | matches ROWS leg constants; 11 cells, no `|` inside cells | none |
| teaches cell vs quote | "IDS-like prosody as attention-grabbing without assuming vowels always clearer" | partial | First clause supported by quote. Vowel clause not in the anchor quote but consistent with §2.2 ("Evidence on segmental instantiation is less straightforward") — defensible gloss, no invented number | optional: could drop vowel clause; not a leg failure |
| BULLET vs quote (RESTATE) | "Infants attend preferentially to IDS-like prosody, letting worldbuilders give caregiver speech a distinct attention cue." | yes against intended quote | 12 content words ≥5; in-order hits 5 (`infants,attend,preferentially,like,prosody`) ≥3; longest verbatim copy-run 5 ≤12; 7 novel content words. Asserts only the preference the quote states — no overreach, no invented number | none once anchor cell is fixed; FAILS (`in_order=0`) while counter extracts the 5-word locator |

## Evidence quotes (verbatim from fetched PDF)

- Header: `Language and Linguistics Compass 7/3 (2013): 157–170, 10.1111/lnc3.12015` / `Input to Language: The Phonetics and Perception of Infant-Directed Speech` / `Alejandrina Cristia`.
- Anchor context (~200 chars either side, pdftotext): `…where the sound has been eliminated (Schachner and Hannon 2011) or replaced by music (Werker and McLeod 1989). | 4. Effects of IDS on Performance | The evidence summarized in Section 3 revealed that infants attend preferentially to IDS, and in particular to IDS-like prosody (with the aforementioned caveats). It then comes as no surprise…`

## Offending words

`Section 4, “Effects of IDS on Performance”:` — the curly quotes around the locator make the counter extract the locator, not the evidence quote. This is a formatting defect, not a sourcing defect: URL, capture, citation, tier, verbatim anchor, and bullet all verify.

VERDICT: FIX-REQUIRED anchor cell quotes the section locator with curly quotes, so the counter extracts "Effects of IDS on Performance" (5 words) → ROWS quote_words=5 FAIL and RESTATE in_order=0 FAIL; unquote the locator or put the evidence quote first.
