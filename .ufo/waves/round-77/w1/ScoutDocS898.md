# ScoutDocS898 — D2 open + attack (row S898 = staged S903)

Verdict: OPENED by ordinary means, locatable, ADMISSIBLE. Tier A for the row scope CONFIRMED.
Evidence: `.ufo/waves/round-77/w1/stage/ScoutDocS898/evidence.txt`.

## Open (UA→HTTP/bytes/wall receipts)

| request | UA | HTTP | bytes | wall | sha256 |
|---|---|---|---|---|---|
| live `GET https://onomastica.ijppan.pl/index.php/ONOM/article/download/574/763/` | curl/8.23.0 | 200 | 417093 | 2.612460s | 5d1bfa5a…29bc |
| capture `…/web/20260901045105id_/…` | curl/8.23.0 | 200 | 417093 | 1.799570s | 5d1bfa5a…29bc (BYTE-IDENTICAL to live) |
| capture `…/web/20251231111748id_/…` | curl/8.23.0 | 200 | 546440 | 3.638146s | 1b4c60f2…2ff9 (same document, older OJS regeneration) |

Commands verbatim: `fetch-command`/`capture-command` fields in evidence.txt. No challenge
(no login, no paywall, no bot gate; CC BY-ND 4.0). `pdfinfo`: Title "Onomastica 69_07",
Author "Irena Kałużyńska", Pages 13 (journal pp. 112–124), DOI 10.17651/ONOMAST.69.7.

Same-page verification: capture 20260901045105 is byte-for-byte identical to the live fetch —
use it as the QUALITY-18 pair. Capture 20251231111748 predates an OJS PDF regeneration
(live `content-disposition: …filename="574-Article Text-3204-3-10-20260417.pdf"`); its text
extract differs only in quote-mark glyph (U+201B→U+2018) and line rewrap; every located quote
below is verbatim in BOTH extracts.

## Located quote (≤25 words, in §2–§4)

Primary anchor — §3 ¶1, journal p. 114 (PDF p. 4), verbatim, 17 words / 111 chars:

> According to Kałużyńska (2008, pp. 223, 232), there were altogether 88 terms denoting plants, flowers and trees

Companion anchors, verbatim in both extracts:
- §4 heading, journal p. 116 (PDF p. 6), 16 words: `LIST OF THE 17 MOST COMMON
  LEXEMES/CHARACTERS DENOTING PLANTS, FLOWERS AND TREES OCCURRING IN FEMALE NAMES`.
- §3 ¶1 continuation, journal p. 115 (PDF p. 5): `2,500 characters occurred in the names of 85,567 females
  and 2,745 characters occurred in the names of 89,333 males` (19 words).
- §2 ¶3 classification survey, journal pp. 113–114: the paper names the literature's own
  schemes — huāniăo zì 花鸟字 / huācăo zì 花草字 / huāhuì zì 花卉字, method wù míng fă 物名法,
  jiè wù qĭmíng 借物起名 (He 2001; Jin 2002; Li 2004; Liu 1999, 2003; Wanyan 1994; Yuan 2001).

The chosen quote retains the paper's attribution to Kałużyńska (2008, pp. 223, 232); the §4
heading supplies the separate 17-most-common-lexemes classification anchor.

## Tier recommendation for scope 'the onomastics literature's own classification of Chinese given names'

CONFIRM tier A (SOURCES.md rule: A = primary or authoritative for the scope). This is an
original peer-reviewed journal article (Onomastica LXIX, 2025, Institute of Polish Language,
Polish Academy of Sciences) that itself names, cites and extends the literature's
classification schemes and supplies counted inventories (88 plant/flower/tree terms in the
author's corpus material; the 17 top-150 lexemes/characters with per-sex occurrence counts
from the 1982-census "Xingshi" statistics). It is the literature, not a write-up about it.

## Negative sweep (negative claim with its sweep)

`git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin grep -l -E 'onomastica|Kałużyńska|Kaluz'
211f9526800906e0c585d878d265c37e5e090c15 -- corpus/knowledge` → prints nothing (no duplicate
document in the knowledge corpus). Widening to `corpus/SOURCES.md` hits only S543
(Reszegi 2023, onomasticafelecan.ro — a different document); D2 is not a SOURCES duplicate.

## Defects / attack surface (none refusing)

1. PDF regeneration byte-drift — the 20251231 capture is NOT byte-identical to live. Mitigation:
   pair live with the byte-identical 20260901045105 capture (done above); treat text-extract
   sha256 / located quotes as the canonical identity, per `bytes-rule`.
2. Scope narrowness — the document covers plant/flower/tree lexemes in FEMALE names only, and
   reports the literature's schemes rather than defining one universal taxonomy; it supports
   "a finite lexeme classification of Chinese given names" as the claim phrases it, but a Gate
   wording promising a COMPLETE classification of all given names would overshoot the document.
3. Layout hyphenation — `pdftotext -layout` wraps mid-word ("flow- ers"); quotes must be chosen
   on non-hyphenated spans (all three candidates above verified verbatim in both extracts).
4. Secondary-source dependence — the 88/17 counts rest on Kałużyńska 2008 and the 1991 "Xingshi"
   census statistics; the article is still tier A for "the literature's own classification",
   but a claim about the 1982 census numbers themselves would need "Xingshi" primary.

Tooling: none installed (pdftotext 26.08.0, curl 8.23.0 already present).
Scratch: `/fast/scratch/hyaku/kotodama-r77/ScoutDocS898/` (PDFs + extracts; deleted on exit).
