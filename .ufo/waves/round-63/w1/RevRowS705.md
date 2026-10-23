# RevRowS705 — blind support, claim C row S705 (Corinthian helmet)

Verdict: **SUPPORTED** (content-level verification complete; one named tool-network gap, below).

## Mode

`/fast/scratch/hyaku/kotodama-r63/ScribeRowS705/` did not exist at start and `S705` was absent from
`corpus/SOURCES.md` — no scribe draft existed to re-open. Per the assignment fallback I searched an
**independent page for the same subtopic** and reviewed it as the drafted row. Subtopic source: the
wave task list (`.ufo/waves/round-63/w1-taskcall.json`, ScribeRowS705 entry): "Corinthian helmet
(Greek bronze hoplite helmet; evolution to Italic forms)", suggested British Museum / Britannica /
academic page, tier A or B.

## Candidate page (independent)

- Live URL: https://art.thewalters.org/object/54.2304/ — The Walters Art Museum, "Corinthian Helmet",
  Greek, 7th–6th century BCE (Archaic), bronze, accession 54.2304.
- Britannica `topic/Corinthian-helmet` answered HTTP 404; Met object 250922 answered HTTP 429 to the
  plain fetch; Walters served HTTP 200 via content negotiation (`text/markdown`), no challenge.
- URL uniqueness: `art.thewalters.org/object/54.2304/` has no match in `corpus/SOURCES.md`
  (`54\.2304` → no matches); other Walters rows are different objects (W.659, 51.354, 51.271).
  Subtopic-exclusive to S705.

## Quote check (verbatim body text, 8–25 normalised words)

Quote: `The nose-guard and cheekpieces of the undecorated, crestless Corinthian helmet left only the
eyes and mouth of its wearer exposed.`

- It is the object-description body text (second description paragraph), not a caption, alt/title
  attribute, or search snippet.
- Normalised word count by the frozen locator's own `normalise()`: **21** (within 8–25).
- **Live URL, frozen locator:** `cd kotodama-shokunin && timeout 300 python3 -B
  reports/round-61/reopen-quote.py 'https://art.thewalters.org/object/54.2304/' '<quote>'` →
  `LOCATED https://art.thewalters.org/object/54.2304/`, exit=0.

## Capture check (same page, quote present)

- CDX (`.../cdx?url=art.thewalters.org/object/54.2304/&output=json&limit=-5&filter=statuscode:200`):
  five HTTP-200 `text/html` captures — 20250218133708, 20250320174042, 20250718173057, 20251108222920,
  20260216150036.
- Chosen capture for the row: `https://web.archive.org/web/20260216150036id_/https://art.thewalters.org/object/54.2304/`
  — plain curl HTTP 200, 238,612 bytes; earliest checked capture 20250218133708id_ HTTP 200, 237,953
  bytes.
- Both saved capture pages carry the title "Corinthian Helmet" and accession 54.2304 → same page as
  live.
- **Canonical content check:** the frozen locator module's own `to_text` + `locate_in` run locally on
  the fetched capture bytes returned **True for both captures** (quote located in extracted body
  text).
- **Gap:** the locator run *as a network tool* against web.archive.org replay URLs failed all 8
  attempts this session with transport-level errors (`URLError` → `[Errno 111] Connection refused`,
  one `HTTPError`), while curl to the same URLs succeeded and one direct `urllib` call succeeded
  (HTTP 200, quote bytes present). This is host-level intermittent Wayback connectivity, not content
  absence. Recommend L1 re-run the locator once on the capture id_ URL at integration time; if the
  network path recovers it should print LOCATED.

## Entry line draft (RESTATE check)

Draft: `- The Walters' record describes the Corinthian helmet as crestless, its nose-guard and
cheekpieces leaving only the eyes and mouth of the wearer exposed (S705).`

- Ends in ` (S705)`; exactly one S-id. ✓
- ≥5 content words (≥4 letters, non-stop): Walters, record, describes, Corinthian, helmet, crestless,
  nose-guard, cheekpieces, leaving, eyes, mouth, wearer, exposed. ✓
- ≥3 shared with the quote in the quote's order: Corinthian(9) < helmet(10) < eyes(14) < mouth(16) <
  wearer(19) < exposed(20) — same relative order in the entry. ✓
- Longest verbatim consecutive run vs the quote: `only the eyes and mouth of` (6 words) ≤ 12. ✓
- Restates ONLY the quote: crestless, nose-guard, cheekpieces, eyes-and-mouth-only exposure — no
  dates, peoples, or uses beyond the quoted words; the only addition is attribution
  ("The Walters' record describes"). ✓

## Draft row (11 columns, for the scribe/L1; I filed nothing)

`| S705 | The Walters Art Museum, "Corinthian Helmet", Greek, 7th–6th century BCE (Archaic), bronze, accession 54.2304, Museum purchase with funds provided by the S. & A.P. Fund, 1946; collection record, no author or publication date on the record. — https://art.thewalters.org/object/54.2304/ ; capture https://web.archive.org/web/20260216150036id_/https://art.thewalters.org/object/54.2304/ | docs | A | one Greek bronze helmet of Corinthian type in the hoplite's equipment: crestless, nose-guard and cheekpieces leaving only the eyes and mouth exposed | object description, second paragraph: "The nose-guard and cheekpieces of the undecorated, crestless Corinthian helmet left only the eyes and mouth of its wearer exposed." | the Corinthian type's face coverage as the Walters states it on one crestless bronze; supports headgear as hoplite identity equipment | mined | 2026-10-23 | 180d | corpus/knowledge/culture-material/headgear-head-covering-codes.md |`

## Residual risk / verification gaps

1. Locator-vs-capture network gap (above): content verified with the frozen module's canonical
   functions on fetched bytes, but no in-tool LOCATED line for the capture this session.
2. Row not filed by me (out of my scope): L1 must integrate; re-check URL uniqueness against the
   other 23 rows' final URLs at integration (theoretically another scribe could pick the same object
   page; the subtopic list makes it unlikely).
3. Tier A assigned by precedent (museum's own record for its own object, cf. S394/S601); if the
   counter's tier rules differ, tier B also satisfies "tier A/B".

No tool installs performed. No repo files modified other than this report.
