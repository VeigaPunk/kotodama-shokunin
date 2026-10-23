# Round 63 — ScribeRowS716

## Result
I researched and drafted one S716 source row, entry bullet, and Gate line. The live quote locator returned `LOCATED`, but the selected Wayback capture locator returned `NOT_LOCATED ... quote-absent` (exit 1). Therefore this is a **partial, not acceptance-ready** S716 draft: the required live-and-capture locator condition is not met. Do not count this as a verified row or infer `ACCEPT-C-63` status from this seat. The direct read of the archived page showed the quote, but the frozen locator result is the gate evidence and is negative.

## Draft artifacts

Registry row (11 columns; use only after the archive locator issue is resolved):

```text
| S716 | James Wharton, “The bearskin: Everything you need to know about the iconic ceremonial headwear,” Forces News, 16 September 2024 - https://www.forcesnews.com/technology/uniform/bearskin-everything-you-need-know ; capture https://web.archive.org/web/20260812000554id_/https://www.forcesnews.com/technology/uniform/bearskin-everything-you-need-know | docs | B | British foot-guard regiments’ bearskin cap as full-dress ceremonial headwear; secondary reporting only | “Origins of bearskins” section, full-dress sentence: “The bearskin is only worn as part of full dress.” | the article reports the bearskin as full-dress headwear for British foot guards; secondary evidence for ceremonial use, not a primary uniform regulation | mined | 2026-10-23 | 180d | corpus/knowledge/culture-material/headgear-head-covering-codes.md |
```

Entry bullet:

```text
- British foot guards wear the bearskin only as part of full dress (S716)
```

Gate line:

```text
- S716 | https://www.forcesnews.com/technology/uniform/bearskin-everything-you-need-know | 2026-10-23 | "The bearskin is only worn as part of full dress."
```

The quote is 10 normalised words and appears in body text under “Origins of bearskins,” not in a caption, alt/title attribute, or search snippet. The entry clause has at least five qualifying content words; `bearskin`, `part`, `full`, `dress` occur in quote order, and its longest exact consecutive run (“as part of full dress”) is 5 words (within the 12-word limit). It carries one S-id. The page also says the headwear is worn by British foot guard regiments. Tier B is appropriate as secondary journalism, not a primary uniform regulation.

## Provenance and gate evidence

Source: [Forces News, James Wharton, “The bearskin: Everything you need to know about the iconic ceremonial headwear”](https://www.forcesnews.com/technology/uniform/bearskin-everything-you-need-know), dated 16 September 2024 on the page. The quote is a full body-text sentence. Wayback timemap returned seven status-200 captures; the selected timestamp `20260812000554` lists the original as exactly the live URL. A direct read of `https://web.archive.org/web/20260812000554id_/https://www.forcesnews.com/technology/uniform/bearskin-everything-you-need-know` also displayed the sentence in body text.

Final live locator command and full stdout:

```text
timeout 300 python3 -B reports/round-61/reopen-quote.py 'https://www.forcesnews.com/technology/uniform/bearskin-everything-you-need-know' 'The bearskin is only worn as part of full dress.'
LOCATED https://www.forcesnews.com/technology/uniform/bearskin-everything-you-need-know
```

The tool output did not state a numeric exit code; its locator docstring says `LOCATED` exits 0.

Final selected-capture locator command and full stdout:

```text
timeout 300 python3 -B reports/round-61/reopen-quote.py 'https://web.archive.org/web/20260812000554id_/https://www.forcesnews.com/technology/uniform/bearskin-everything-you-need-know' 'The bearskin is only worn as part of full dress.'
NOT_LOCATED https://web.archive.org/web/20260812000554id_/https://www.forcesnews.com/technology/uniform/bearskin-everything-you-need-know quote-absent
```

This command exited 1. That is the unresolved gate. I did not replace the failure with the direct-read result.

Other same-page archive locator attempts, all for the final quote, also failed:

- `timeout 300 python3 -B reports/round-61/reopen-quote.py 'https://web.archive.org/web/20240917133140id_/https://www.forcesnews.com/technology/uniform/bearskin-everything-you-need-know' 'The bearskin is only worn as part of full dress.'` → `NOT_LOCATED https://web.archive.org/web/20240917133140id_/https://www.forcesnews.com/technology/uniform/bearskin-everything-you-need-know HTTPError` (exit 1).
- `timeout 300 python3 -B reports/round-61/reopen-quote.py 'https://web.archive.org/web/20260811010952id_/https://www.forcesnews.com/technology/uniform/bearskin-everything-you-need-know' 'The bearskin is only worn as part of full dress.'` → `NOT_LOCATED https://web.archive.org/web/20260811010952id_/https://www.forcesnews.com/technology/uniform/bearskin-everything-you-need-know HTTPError` (exit 1).
- `timeout 300 python3 -B reports/round-61/reopen-quote.py 'https://web.archive.org/web/20250123130327id_/https://www.forcesnews.com/technology/uniform/bearskin-everything-you-need-know' 'The bearskin is only worn as part of full dress.'` → `NOT_LOCATED https://web.archive.org/web/20250123130327id_/https://www.forcesnews.com/technology/uniform/bearskin-everything-you-need-know HTTPError` (exit 1).

A direct `urllib` diagnostic using the locator's Firefox User-Agent to the older archive URL received `HTTP Error 429: Too Many Requests`. A `curl --compressed` diagnostic with the same User-Agent to that older capture returned `HTTP 200; bytes=18955`; this is not the required locator and is not used as a pass. No challenge, captcha, paywall, or login was routed around.

## Rejected candidates and URL check

- `https://www.britannica.com/topic/bearskin` and `https://www.britannica.com/topic/bearskin-military-headgear` each returned HTTP 404 on direct read.
- The Age of Revolution “Bearskin Headdress” page (`https://ageofrevolution.waterlooassociation.org.uk/200-object/modern-bearskin/`) and its live locator worked for its body quote, but its Wayback timemap returned `[]`, `/web/0id_/` returned HTTP 404, and its CDX/availability requests returned HTTP 429. It therefore lacked a same-page archive capture. The live locator output was `LOCATED https://ageofrevolution.waterlooassociation.org.uk/200-object/modern-bearskin/` for “The infantry wore bearskin headdresses, as a status symbol and to make themselves look taller and more fearsome in battle.”
- A broader registry search found S656’s bearskin shoe-sole source, not this page. The exact selected Forces News URL had no match in the current `corpus/SOURCES.md`. This checks existing registry bytes only; I did not establish URL uniqueness against all peer drafts.

## Touched surfaces, scope, and limits

- Lane write: this report only, at `.ufo/waves/round-63/w1/ScribeRowS716.md` (the single lane-repository write for this seat). No product code, `corpus/SOURCES.md`, or knowledge entry was changed; L1 remains the sole integration owner.
- Read-only local context: `reports/round-63/claims.json`, the docstrings in `reports/round-63/accept-o.py` and `accept-c.py`, section 5 of `corpus/lessons/round-62-verifier-spotcheck.md`, `corpus/SOURCES.md` (including S693), and the base `reports/round-61/reopen-quote.py` locator contract.
- Scratch artifacts: `/fast/scratch/hyaku/kotodama-r63/ScribeRowS716/S716-row.txt`, `S716-entry-bullet.txt`, `S716-gate-line.txt`, `S716-quote.txt`, `S716-source-notes.txt`, and `S716-locator-output.txt`.
- No counter, build, tests, or `tools/reopen-row.py` run; no tools installed. This was one coverage row only. The C receipt, all-row URL uniqueness, other scribes’ URL uniqueness, and final integration remain out of scope for this seat.
- Discovery used one web-search query (`bearskin cap guards military museum British Guards bear skin cap history`) only to find candidate pages; no search snippet was used as source evidence or as the quote. The source page and capture were then read directly, and the quote was checked with the specified locator.
