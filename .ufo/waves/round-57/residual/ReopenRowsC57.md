# Residual re-open — SOURCES rows S441–S454 at 78d83b5e

Seat: ReopenRowsC57 (Kotodama round 57, claim C residual). Method: every row host
re-fetched live 2026-10-22 by ordinary means (plain `curl`, Firefox desktop UA, no
challenge bypass) into `/fast/scratch/hyaku/kotodama-r57/ReopenRowsC57/`; anchor
quotes extracted from the committed `78d83b5e:corpus/SOURCES.md` cells and matched
verbatim against served bytes (HTML entity-unescaped and tag-stripped, whitespace
collapsed; PDFs via `pdftotext` 26.08.0; `s451` served ISO-8859-1→cp1252).
Worktree `corpus/SOURCES.md` diffs from 78d83b5e only by appended rows S481–S491
(sibling work); rows S441–S454 are byte-identical to the commit. All 14 hosts
answered HTTP 200; nine served byte counts equal the recorded cell byte-for-byte.

## Findings

**F1 — MEDIUM — S453: citation carries "protocol rules" the served page lacks;
knowledge entry cites them at "served text" strength; two cells truncated.**
`/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md:483` and
`corpus/knowledge/myth-symbol/heraldry-emblems-identity-marks.md:113`.
The row serves `USCODE-2024-title4-chap1-sec1.htm` = §1 (design) plus an
Executive-Order note on agency flag sizes and the union jack. Measured on the
fetched page: `dip` ×0, `distress` ×0, `position of honor` ×0, `display` ×0
(`pdftotext`-equivalent stripped text; grep of `s453.htm`). Yet
- entry line 113 asserts "and its protocol: never dipped, union down only in
  distress (S453, served text)" — the protocol clauses are not on the page;
- scope cell is truncated mid-claim: "Statutory description of the national
  flag's design (stripes, union, stars); protocol rules for" — ends before any
  object;
- citation cell is truncated: "2024, United States — https://…" (the document is
  the U.S. Code, Title 4, Chapter 1, Section 1; the served head reads `§1. Flag;
  stripes and stars on`).

Exact fixes:
- `knowledge/.../heraldry-emblems-identity-marks.md:113`
  old: `a statute can fix a design ("thirteen horizontal stripes") and its
  protocol: never dipped, union down only in distress (S453, served text)`
  new: `a statute can fix a design ("thirteen horizontal stripes"), and its
  notes regulate sizes and the union jack for executive agencies (S453, served
  text)` — or cut the protocol clause entirely; no opened row carries
  dipping/distress rules.
- `SOURCES.md:483` scope cell
  old: `Statutory description of the national flag's design (stripes, union,
  stars); protocol rules for`
  new: `Statutory description of the national flag's design (stripes, union,
  stars); the served page's executive-order note regulates agency flag sizes
  and the union jack (not dipping or distress rules, which the page lacks).`
- `SOURCES.md:483` citation cell
  old: `Office of the Law Revision Counsel / U.S. Government Publishing Office,
  2024, United States —`
  new: `Office of the Law Revision Counsel / U.S. Government Publishing Office,
  2024, United States Code, Title 4 (Flag and Seal, Seat of Government, and the
  States), Chapter 1 (The Flag), Section 1 —`

**F2 — LOW — S452: anchor uses ASCII apostrophe; served page has `’` (U+2019);
citation title and scope cell truncated mid-phrase.**
`/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md:482`.
Served bytes (Wayback `20010723223146if_`, cp1252 `0x92`): "organization’s seal"
(curly). Row stores `organization's` (ASCII `'`). Prefix match 48/55 chars.
Fix quotes cell: old `"Never use writing of any kind or an organization's seal"`
→ new `"Never use writing of any kind or an organization’s seal"`.
Truncations, measured against the same booklet's cover capture
(`web.archive.org/web/2001id_/…/gfbf-1.htm`, HTTP 200, 3,545 bytes; served text
reads "GOOD FLAG, BAD FLAG — HOW TO DESIGNA GREAT FLAG", with the run-in exactly
as served) and page `gfbf-2.htm` (capture `20010722170313`, HTTP 200):
- citation cell old `"Good Flag, Bad Flag — How to — http://…` → new `"Good Flag,
  Bad Flag — How to Designa Great Flag" —` (as served; "DESIGNA" is the cover's
  own run-in — keep or note `[sic]`).
- scope cell old `…the historical link from flags to` → new `…the historical
  link from flags to heraldry: "Flags grew out of heraldry—the practice of
  designing coats of arms—and follow many of the same design principles."`
  (verbatim on the gfbf-2 capture the row itself names).
Advisory: entry line 113 cites S452 for "simple enough for a child to draw, two
or three basic colours"; both statements are on the cited gfbf-3 page ("a child
can draw it from memory", "Limit the number of colors on the flag to three") but
carry no anchor; strength is fine, coverage only.

**F3 — LOW — S445: anchor's terminal period fabricated; source continues with a
comma.** `/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md:474`.
Prefix match 127/128: served `…blått, svart, grønt eller purpur, eventuelt med
stiliserte pelsverk (hermelin eller gråverk).` vs row `…grønt eller purpur."`.
Fix quotes cell: old `…svart, grønt eller purpur."` → new `…svart, grønt eller
purpur, eventuelt med stiliserte pelsverk (hermelin eller gråverk)."`

**F4 — LOW — S451: access cell says "served as ISO-8859-1"; response header now
returns `charset=UTF-8`.** `/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md:481`.
Fetched `Content-Type: text/html; charset=UTF-8` (23,665 bytes, matching the
recorded count); the page meta still declares `charset=ISO-8859-1`. The anchor
"Rather than display his own crests on the pole, as was customary for a pole
standing before a lineage house" locates verbatim under either decoding.
Fix: old `(direct, HTTP 200, text/html (23,665 bytes, served as ISO-8859-1;
quotes verified against served bytes).)` → new `(direct, HTTP 200, text/html
(23,665 bytes; page declares ISO-8859-1, header now reports UTF-8; quotes
verified against served bytes).)`.

**F5 — INFO — S446 under the appended criterion-10 sentence.** The Internet
Archive item `in.ernet.dli.2015.178234` (`metadata` endpoint fetched live:
`collection=digitallibraryindia`, `scanner="Internet Archive Python library"`,
description names `dc.contributor.other: State Central Library, Hyderabad` and
the DLI handle `2015.178234`; `licenseurl`/`rights` are unset). The amended
sentence accepts "the digitising library's or archive's own scan" — this is the
Digital Library of India's own scan of a State Central Library copy; PASS. The
row cell records the provenance already; recommend adding "(item metadata names
State Central Library, Hyderabad as contributor; DLI's own scan)" to make the
criterion-10 basis legible. No host-name-only inference needed.

## Per-row verdicts

| Row | Anchors verbatim | Tier vs scope | Entry strength | Criterion-10 | Verdict |
|---|---|---|---|---|---|
| S441 TNA seals guide | 4/4 | docs·A ✓ | §9 line 106, §11 line 133, §12 line 149 ✓ | plain GET, byte count matches | agree |
| S442 V&A matrix O322757 | 4/4 | docs·A ✓ | §3 line 46, §9 line 106 ✓ | plain GET | agree |
| S443 AAS 61 (1969) | 4/4 (pp. 336, 339 text layer) | docs·A ✓ | §4 line 60 ("simple and clear" is the entry's translation of the Latin — acceptable), §7 line 90, §10 line 124, §13 line 154 ✓ | publisher's own scan | agree |
| S444 heraldica.org | 4/4 | community·B ✓ | §7 line 90, §10 line 124 ✓ | plain GET | agree |
| S445 heraldikk.no PDF | 3/4 (F3) | docs·A ✓ | §4 line 59 ✓ | society's own PDF | disagree → fix F3 |
| S446 Mayer 1933 (IA/DLI) | 4/4 | book·A ✓ | §3 line 44, §7 line 89 ("apparently had no right to it" ≈ served "apparently had no right to arms" ✓), §11 line 137 ✓ | digitising library's own scan (F5) | agree |
| S447 London Museum A295 | 3/3, `A295` on page | docs·A ✓ | §3 line 45, §7 line 92, §12 line 145 ✓ | plain GET | agree |
| S448 Fordham Notitia | 3/3 | docs·A ✓ | §3 line 44 ("never names the incumbent" = genre observation, supported), §7 line 88 ✓ | plain GET | agree |
| S449 lukeuedasarson.com | 4/4 | community·B ✓ | §7 line 88 hedge ("never labels" supported: "the document itself doesn't assert any particular patterns shown therein 'show the shield of X'"), §11 line 138 ("minority of units" supported verbatim) ✓ | plain GET | agree |
| S450 MOA UBC PDF | 4/4 | docs·A ✓ | §3 line 48, §9 line 111, §13 line 154 ✓ | museum's own PDF | agree |
| S451 Royal BC Museum | 1/1; "four … Kwakwaka'wakw nations" verbatim on page | docs·A ✓ | §9 line 111, §13 line 154 ✓ | plain GET (F4 header drift) | agree → cosmetic fix F4 |
| S452 NAVA (Wayback 2001) | 1/1 except `'`→`’` (F2); scope & title truncated (F2) | docs·A ✓ | §9 line 113, §12 line 149 ✓ (uncited-but-served child/colours claims) | archive capture | disagree → fix F2 |
| S453 govinfo 4 USC §1 | 1/1 | docs·A ✓ | §9 line 113 protocol clauses NOT on page (F1) | plain GET | disagree → fix F1 |
| S454 V&A rank badges O456793 | 3/3; JSON record corroborates | docs·A ✓ | §7 line 91 ✓ | plain GET | agree |

## Residual risk / verification gaps

- S452 scope completion above relies on the page-1 (`gfbf-2.htm`, capture
  `20010722170313`) and cover (`gfbf-1.htm`) captures; the row's parenthetical
  `20010722170222` is one second off the served wombat timestamp for page 1 —
  worth normalising if the fix is applied.
- S449's citation reads "(2015)"; served page states "created 27 April 2014,
  last modified 12 November 2015" — acceptable but could be made exact.
- No install performed; `pdftotext` 26.08.0 already present. Fetch artifacts
  remain in `/fast/scratch/hyaku/kotodama-r57/ReopenRowsC57/` for re-run.

Verdict: **disagree with what landed for S452 and S453 as written** (F1, F2 —
one unsupported knowledge citation and four truncated/drifted cells), plus the
S445 comma (F3) and S451 charset note (F4). All other rows verify clean: anchors
verbatim on the served page, tier fits scope, citing sentences carried at stated
strength, and criterion 10 (including the round-57 scan-provenance sentence)
passes on every host.
