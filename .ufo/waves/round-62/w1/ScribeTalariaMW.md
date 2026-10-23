# ScribeTalariaMW — Merriam-Webster talaria source

## Behavior / finding

Opened Merriam-Webster's `talaria` dictionary page by ordinary read, and opened the same page's Wayback capture. The page's body definition supplies this exact 21-word quote:

> winged shoes fastened to the ankles and chiefly used as an attribute of the god Hermes or Mercury of classical mythology

It names Hermes (and Mercury) and supports the requested lexical definition. The quote is visible in the live page read and verbatim in the archive capture. The archive capture is a same-page match: the CDX result has the same original URL, status 200, timestamp `20251008014307`; the capture's canonical URL is the Merriam-Webster entry.

The source URL was not already in `corpus/SOURCES.md` (registry search returned `No matches found`). The final visible registry entry is S692, so S693 is the next row id. Proposed tier A is scoped narrowly to Merriam-Webster's authoritative English lexical definition, not historical practice or depictions in art.

## Drafts for the lane owner

**SOURCES row (11 columns):**

```text
| S693 | “TALARIA Definition & Meaning,” Merriam-Webster.com Dictionary, Merriam-Webster (undated; accessed 2026-10-23) — https://www.merriam-webster.com/dictionary/talaria ; capture https://web.archive.org/web/20251008014307id_/https://www.merriam-webster.com/dictionary/talaria | book | A | English lexical definition of talaria and its mythological attribution; not historical practice or artistic depictions | entry talaria, definition: "winged shoes fastened to the ankles and chiefly used as an attribute of the god Hermes or Mercury of classical mythology" | Merriam-Webster defines talaria as winged shoes fastened at the ankles, chiefly an attribute of Hermes or Mercury in classical mythology. | mined | 2026-10-23 | 180d | corpus/knowledge/culture-material/footwear-codes-terminology.md |
```

**Proposed replacement for footwear entry line 93:**

```text
- Talaria are winged shoes fastened at the ankles, chiefly an attribute of Hermes or Mercury in classical mythology. (S693)
```

This has 11 content words; 10 occur in the quote in order (LCS 10; required minimum 5). The longest consecutive copied run is three words, below the 12-word limit. It has one S-id and no defect mark.

**Draft Gate line:**

```text
- Merriam-Webster, https://www.merriam-webster.com/dictionary/talaria (accessed 2026-10-23): “winged shoes fastened to the ankles and chiefly used as an attribute of the god Hermes or Mercury of classical mythology.”
```

## Gates and exact re-test receipts

CDX query used:

```text
https://web.archive.org/cdx/search/cdx?url=https%3A%2F%2Fwww.merriam-webster.com%2Fdictionary%2Ftalaria&output=json&limit=-5&filter=statuscode%3A200
```

It returned 5 captures. The selected last result was original `https://www.merriam-webster.com/dictionary/talaria`, timestamp `20251008014307`, status `200`, digest `ZUGP4XXXZD3XXOP6UN4TZBWYZO5VPBA4`, length `100270`.

Base locator live-URL run (rejecting the live URL as a sole locator):

```text
timeout 300 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-61/reopen-quote.py 'https://www.merriam-webster.com/dictionary/talaria' 'winged shoes fastened to the ankles and chiefly used as an attribute of the god Hermes or Mercury of classical mythology'; echo exit=$?
NOT_LOCATED https://www.merriam-webster.com/dictionary/talaria HTTPError
exit=1
```

Base locator archived-copy run (accepted fallback):

```text
timeout 300 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-61/reopen-quote.py 'https://web.archive.org/web/20251008014307id_/https://www.merriam-webster.com/dictionary/talaria' 'winged shoes fastened to the ankles and chiefly used as an attribute of the god Hermes or Mercury of classical mythology'; echo exit=$?
LOCATED https://web.archive.org/web/20251008014307id_/https://www.merriam-webster.com/dictionary/talaria
exit=0
```

The live locator output does not expose an HTTP status code. I did not attempt to bypass an access control; the ordinary page reader had returned the live body, and the ordinary Wayback capture read and locator both contained the quote. The live endpoint alone therefore fails this locator observation, but the live URL plus listed archive copy is supported as the row's source pair.

## Scope, gates, and provenance

- **Affected surfaces:** This report only. The row and entry line above are drafts; I did not edit product files or `corpus/SOURCES.md`.
- **Not performed / out of scope:** No ACCEPT-D counter, source-access checker, lint, build, or other acceptance gate was run; no claim verdict is issued. Collins/Oxford mirrors and Wiktionary were not tested because this tier A source and its capture supplied the quote. No alternate dictionary is rejected on untested evidence.
- **Revision provenance:** Assignment context names target revision `f0173481047a93c46798f90b68d71d4f169d2642`; I did not run git/jj commands or independently verify HEAD.
- **Inputs read:** round-62 `claims.json`, round-61 spotcheck §7, round-62 `accept-d.py` contract, `corpus/SOURCES.md`, `corpus/QUALITY.md`, footwear entry context, and round-61 `reopen-quote.py` contract. No tools were installed.
- **Artifacts:** Merriam-Webster live URL above; CDX result above; same-page Wayback capture above; this report at `.ufo/waves/round-62/w1/ScribeTalariaMW.md`.
