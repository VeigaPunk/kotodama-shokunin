# Tier / scope judgments for the three proposed registry rows (round 88, seat ScoutSources)

Tiers are scoped to the row's own scope cell, never global (SOURCES header contract).

## S931 - Chrisomalis 2018, "The writing of numbers"

| field | judgment |
|---|---|
| kind | `paper` |
| venue | *Terrain. Anthropologie & sciences humaines* 70 (peer-reviewed journal), published 2018/10/09, doi 10.4000/terrain.17506 |
| author | Chrisomalis, Stephen (`DC.creator` in the page head) |
| tier | **A** for the scope "the two-axis typology of numerical notations and the trade-offs among its five types" - the paper is the primary/original source for that typology and for the no-perfect-system finding it states |
| tier caveat | figure 1 is captioned "Typology of numerical notations (after Chrisomalis 2004, 2010)", so the typology itself is the author's earlier work restated here; the row's scope should read "the typology as presented in this 2018 paper", not "the origin of the typology" |
| live access | the live URL answered an Anubis bot-check challenge page on 2026-11-04 (HTTP 200, 5,281 bytes, `anubis_challenge` JSON in the body). The challenge was **met and not passed**; the body text was read from the Wayback capture of the same page |
| durable capture | `https://web.archive.org/web/20251211231049id_/https://journals.openedition.org/terrain/17506` (HTTP 200, 190,162 bytes) - the capture's embedded original normalizes equal to the live URL under the lane's own `tools/check-row-fragments.py:norm_url` (query ignored) |
| CDX gap (observed, report to the row owner) | CDX exact query for `journals.openedition.org/terrain/17506?lang=en` returns `[]`: **no capture exists under the `?lang=en` query form itself**. Captures exist for the query-less URL, whose body serves the same English article text (41 numbered paragraphs verified). The row should therefore name the capture of the query-less same page, or name the live URL without the query |
| other captures checked | 20190505043833 and 20210228041215 also carry the full 41-paragraph English body with identical para 7-10 and para 25 text; 20260223185515 is a bot-check page (4,474 bytes) and carries none of it |

## S932 - MacTutor, "Babylonian numerals"

| field | judgment |
|---|---|
| kind | `docs` (a university-hosted history-topics article, not a paper) |
| authorship / date | "Written by J J O'Connor and E F Robertson", "Last Update December 2000"; University of St Andrews, School of Mathematics and Statistics |
| tier | **B** for the scope "how a sexagesimal positional notation is built and where it fails without a zero" - strong secondary with reproducible detail, not primary scholarship |
| tier caveat | the page is 25 years old and its base-60 origin discussion is explicitly the authors' own speculation ("I [EFR] feel that all of these reasons are really not worth considering seriously"). A row scoped to *why* base 60 would exceed tier B and should not be written that way |
| scope it can carry | the two-sign construction of the 59 digits, the missing zero and the resulting 1 / 1,0 ambiguity, the sexagesimal point |
| scope it cannot carry | the two-axis typology. MacTutor never uses "cumulative-positional"; it says "positional base 60 system" and adds that the Sumerian and Akkadian systems "was a positional system" is false. Any typology classification of Babylon must be attributed to S931, not to S932 |
| durable capture | `https://web.archive.org/web/20200708131715id_/https://mathshistory.st-andrews.ac.uk/HistTopics/Babylonian_numerals/` (HTTP 200, 62,852 bytes); every S932 quote was re-located in that capture's body |

## S933 - MacTutor, "Egyptian numerals"

| field | judgment |
|---|---|
| kind | `docs` |
| authorship / date | "Written by J J O'Connor and E F Robertson", "Last Update December 2000"; University of St Andrews |
| tier | **B** for the scope "how Egyptian hieroglyphic and hieratic numerals are built and why the hieratic form is non-positional" |
| tier caveat | same 2000 vintage; the page's Karnak-stone attribution ("a stone carving from Karnak, dating from around 1500 BC, and now displayed in the Louvre") is the authors' statement, not an exhibition record, so it cannot carry a catalogue-grade claim |
| scope it can carry | the base-10 hierarchy of separate signs, the additive composition rule, the hieratic compactness figure, and the explicit non-positional statement ("the hieratic numerals did not form a positional system so the particular numerals could be written in any order") |
| scope it cannot carry | the typology. MacTutor uses no typological vocabulary; the classification of early Egyptian hieroglyphic numerals as cumulative-additive comes from S931 para 19, not from S933 |
| durable capture | `https://web.archive.org/web/20200724192341id_/https://mathshistory.st-andrews.ac.uk/HistTopics/Egyptian_numerals/` (HTTP 200, 20,186 bytes); every S933 quote was re-located in that capture's body |

## Verbatim-text cautions for the row owner

- S933's live text contains the typos "The Egyptians had a bases 10 system" and "they has separate symbols". A
  quote cell reproduces them verbatim; the entry prose must not, and the row's `teaches` cell must not.
- S932's "the 59 numbers, which go into one of the places of the system, were built from a 'unit' symbol and a
  'ten' symbol" is 23 words and inside the cap; quoting it together with the "two symbols" sentence would
  exceed 25 words, so they must be two separate quotes on separate lines.
- No `|` character may appear inside any registry cell: `reports/round-88/measure88.py:claim_d` splits the row
  on `|` to read tier and status, so a pipe inside a cell shifts the parsed columns and the `new-rows-mined`
  leg reads the wrong fields.

## Wording hazard for the S931 row (lane tool `tools/check-source-access.py`)

That tool flags a mined row whose source/anchor/teaches cell records getting *past* an access control.
Six candidate phrasings of the S931 access note were tested against the tool's own BYPASS regex; none
matched, e.g. "challenge met, not passed; content read from Wayback capture 20251211231049id_". Phrasings
such as "solved the challenge" or "read via headless browser" would match and must not be used.
