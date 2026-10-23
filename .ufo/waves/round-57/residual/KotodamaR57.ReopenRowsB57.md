# Residual falsify — KotodamaR57.ReopenRowsB57 — SOURCES rows S427–S440 @ 78d83b5e

Method: live plain GET of every row's source-cell URL(s) into
/fast/scratch/hyaku/kotodama-r57/KotodamaR57.ReopenRowsB57/ (all HTTP 200), PDFs via
pdftotext, every anchor-cell quoted span checked for verbatim presence with the
frozen locator's normalizer (NFKC, casefold, `\W→space`, reports/round-57/reopen-quote.py).
Tier judged against the SOURCES header rules; entry sentences re-read in
corpus/knowledge/myth-symbol/heraldry-emblems-identity-marks.md.

## Findings (severity-ordered)

### F1 — MEDIUM — S428: two of four anchor quotes are not verbatim on the served page (locator MISS)
`corpus/SOURCES.md:457`. Served bytes: archive.org `transactionsasi26japagoog_djvu.txt`
(1,212,356 B). The DjVu OCR splits both spans at line-break hyphens:

- quote 1: `"they took their origin from the patterns embroidered upon, or woven into, the state garments of the old court nobles at Kiy6to"` — served text (scratch s428.txt:17519-17521) is `the state gar-` / `ments of the old court nobles`. Under the frozen normalizer, "garments" ≠ "gar ments" → MISS. This is the row's FIRST quoted span, so a live locator rerun returns not-located for S428.
- quote 4: `"the only place where the distinfraishing mark could be borne was either on the helmet or on the breast plate"` — served text (scratch s428.txt:17483-84) is `distinfraish-` / `ing`. Same cause → MISS. ("breast plate" vs served "breast-plate" normalizes equal and is not a defect.)

Note: landing receipt already recorded "live-located 40/42" — S428 is evidently one of the
two non-locating rows; ACCEPT-C-57's ceil(0.8·42)=34 floor still passes, so this does not
flip the predicate, but the row's quoted spans are factually not verbatim-as-served.

Fix (SOURCES.md:457, verbatim transcription of the served hyphenation — normalizes
identically to what the page serves):
- old: `the state garments of the old court nobles at Kiy6to` → new: `the state gar-ments of the old court nobles at Kiy6to`
- old: `the only place where the distinfraishing mark could be borne was either on the helmet or on the breast plate` → new: `the only place where the distinfraish-ing mark could be borne was either on the helmet or on the breast plate`
- Cleaner alternative for quote 4 (contiguous on the page, same claim): `crests and badges are the only Heraldic insignia here known` (served at scratch s428.txt:17485-17486).

### F2 — LOW — S430: entry drops the source's own hedge
`corpus/knowledge/myth-symbol/heraldry-emblems-identity-marks.md:108` (§9 garment row):
"a masterless samurai still wears his former clan's mon (S430, served text)". The V&A
record hedges: "the same family mon (crest) probably the emblem of his former samurai
clan" (verified verbatim in served HTML). Fix:
- old: `a masterless samurai still wears his former clan's mon (S430, served text)` → new: `a masterless samurai's mon is probably the emblem of his former clan (S430, served text)`
Incidental: the row's quote reproduces V&A's own typo "Miyaki Prefecture" — verbatim, correct as-is.

### F3 — LOW — S434: calibration-bank gloss exceeds what the source states
`corpus/knowledge/myth-symbol/heraldry-emblems-identity-marks.md:136` (§11):
`"a tamga is a script" | R | signs of group identity, not an alphabet (S434)`. The source
states "signs of group identity" (verified verbatim); "not an alphabet" is the entry's
gloss, and the paper elsewhere notes tamgas "in the form of runic graphemes" (s434.txt:636),
which the flat gloss elides. The R verdict itself is defensible — the source defines tamgas
as identity marks — but the parenthetical reads as source content. Fix:
- old: `signs of group identity, not an alphabet (S434)` → new: `signs of group identity (S434); "not an alphabet" is this entry's gloss`

### F4 — LOW — S440: scope cell ends mid-sentence
`corpus/SOURCES.md:469`: scope ends "and the commemorative context of a merchant about."
— truncated text. The quotes verify (both exact on the served page) and the teaches cell is
coherent; only the scope sentence is broken. Fix:
- old: `the commemorative context of a merchant about.` → new: `the commemorative context of a merchant's tomb.` (consistent with teaches cell "on his tomb brass")

### Cosmetic notes (no fix required)
- S429 quotes 1 and 4 contain markdown asterisks (`*kamon*`, `*bushi*`) absent from the
  served page; normalization strips them so the locator passes, and the row's own scope
  uses the same italics convention. Words are identical on the page.
- S428 page labels ("page 4", "page 2") cannot be verified from the served bytes (the
  djvu.txt serves as a single un-paginated stream). Not a defect found, a gap noted.
- S439 tier B for an 1853 original monograph: "A — primary or authoritative for that
  scope" would arguably fit, but B is defensible as dated scholarship; `community is never A` and a period source needn't be A. No change demanded.

## Per-row verdicts

| row | anchor quotes verbatim | tier fits scope | entry sentences at stated strength | verdict |
|---|---|---|---|---|
| S427 | 4/4 locate (1 exact, 3 normalized) | B: community never A — fits | §10 oldest colour arms + 1149 seal; §11 C — carried | PASS |
| S428 | 2/4 MISS (OCR hyphen splits) | A: original 1876 paper — fits | all cited claims verified in OCR (assumed at will, conferred by chieftain, same-family different badges, Mito/Owari/Kii differencing) | FAIL (partial) — F1 |
| S429 | 4/4 locate (asterisk markup only) | B: popular explainer — fits | Edo permission + kikumon/aoimon exceptions, onnamon, godaimon all on page | PASS |
| S430 | 3/3 locate (1 exact) | A: museum record — fits | rōnin clause drops "probably" — F2 | PASS with fix |
| S431 | 3/3 locate, all exact | A: national museum — fits | hedged attribution honored as T in §7/§11 | PASS |
| S432 | 2/2 locate (quote 1 on URL 1, quote 2 on URL 2) | A: museum records — fits | licensed-use, 1615–1867 span, guard+signature verified (inscription block) | PASS |
| S433 | 2/2 locate (abstract record page) | A: original paper's record page — fits | Salbyk stripes sentence carried | PASS |
| S434 | 4/4 locate in PDF text | A: original paper, CC BY — fits | Karluk federation divisions verified; §11 gloss overstated — F3 | PASS with fix |
| S435 | 4/4 locate in PDF text | A: original paper — fits | zawołanie, clan boundaries, Bieniak factions, Piotr's two cries all verified | PASS |
| S436 | 4/4 locate, all exact | A: state agency — fits | all four inspection triggers, daylight rule, recorded brand on page | PASS |
| S437 | 3/3 locate, all exact | A: official form — fits | reading order, lazy/bow vocabulary, monogram verified | PASS |
| S438 | 4/4 locate | A: state agency — fits | ~30,000 brands, ~1865 territorial origin, 75-mile trigger, fee funding verified | PASS |
| S439 | 4/4 locate | B: 1853 monograph — defensible | hand-sign, Erfurt survival, Hauptmittel, v. Gagern arms = house mark (served: "nichts andres als dieselbe Marke"), ear-marks all verified | PASS |
| S440 | 2/2 locate, both exact | A: museum record — fits | shield + carding comb on tomb brass carried; scope cell truncated — F4 | PASS with fix |

## Verdict

Agree with what landed, with one genuine row defect and three small fixes. F1 is the only
verbatim violation in the 14 rows: S428's first quoted span does not locate live under the
frozen instrument (consistent with the landing's own 40/42 receipt; the LOCATE floor is
unaffected). 13 of 14 rows pass quote-verbatim outright; every tier fits its scope; every
entry sentence is carried at stated strength except the two hedge-drops at F2/F3 and the
truncated scope cell at F4.

Residual risk: unverified page-number labels on S428 quotes; no form-feed page structure in
the served OCR to falsify them cheaply. Verification gap: LOCATE floor margin is 41/42 vs
34 required — comfortable, no drift toward the floor observed today.
