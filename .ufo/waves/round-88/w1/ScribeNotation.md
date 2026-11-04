# ScribeNotation — round-88 w1 report

Axes: operability, depth. Milestone r88-v1. Lane `/home/vgpnk/Projects/shokunin/kotodama-shokunin`; frozen claims `O` and `D` at `4b76524c51e1c2f76c99eeb3b629cfac08a44a76`; base `4956282281dac1306cfbe59523e46dde99749d75`; pre-freeze controls `0c8c733088df8c4f06770c9e714360eed7f29272`.

## Behavior

Drafted one new knowledge section and one correction fragment for
`corpus/knowledge/linguistics/numerals-and-measures.md`. Nothing was written to the
production entry, to `corpus/SOURCES.md`, or to any other production file.

- **`stage/ScribeNotation/notation-section.md`** — the section text, carrying the frozen
  heading `## 4b. Numeral notation: two axes, five types, and their trade-offs` exactly
  once. It is a method-and-reference section (non-canon, hands off to lore) that adds the
  *written* side of numbering between the entry's word-typology sections (1–4) and its
  counting-technology section (5). Seven subsections: the four things that are easy to
  confuse (numeral words / numeral notation / tallying / counting devices), the two axes
  and why five types rather than six, a five-row cost sheet, two case studies (Egyptian
  and Babylonian), a NON-CANON worked example, the limits, and the source anchors. Two
  tables: 5×4 in 4b.1 and 6×6 in 4b.3. Twelve anchor lines, each carrying exactly one
  source id and one located quote.
- **`stage/ScribeNotation/section5-correction-fragment.md`** — a precise replacement
  proposal for **one** bullet of §5 (the "typological stages" bullet), staged, not
  applied. It quotes the current bullet verbatim, lists the four separable defects with
  the opened source behind each, and gives the replacement in the clause-scoped split form
  the QUALITY-15 lint requires. The entry's history — its round-10 authorship note, its
  bibliography, its `(to-verify)` list, its section order — is left untouched.

## Sources actually opened

All three were opened by plain HTTP request (curl User-Agent, no browser automation, no
challenge solving, no cookie handling), and each was re-fetched under the lane's own
re-opener User-Agent (`kotodama-reopen-row/1.0`) to confirm reproducibility. All three
were also pulled from a same-page Wayback capture. Every anchor quote was located in the
**body** text (script/style/noscript/template and figure captions excluded) of **both**
copies.

| id | URL | HTTP | bytes | sha256 (live) | Wayback capture | HTTP | bytes |
|---|---|---|---|---|---|---|---|
| S931 | `https://journals.openedition.org/terrain/17506?lang=en` | 200 | 189906 | `4f7108f2…c7b5c0` | `20190505043833id_` | 200 | 126580 |
| S932 | `https://mathshistory.st-andrews.ac.uk/HistTopics/Babylonian_numerals/` | 200 | 65959 | `ac4701fb…f9d5f` | `20200708131715id_` | 200 | 62852 |
| S933 | `https://mathshistory.st-andrews.ac.uk/HistTopics/Egyptian_numerals/` | 200 | 23397 | `5f6ef5ee…18d1b5` | `20200724192341id_` | 200 | 20186 |

Retained bodies and their hashes are in `stage/ScribeNotation/receipts/`; the full
manifest with byte counts, capture URLs, quote line numbers and per-quote presence flags
is `receipts/receipts.json`.

One access note recorded honestly: a first probe of the Terrain URL with a
**browser-shaped** User-Agent returned an Anubis interstitial (HTTP 200, 5283 bytes). That
response was discarded and was **not** used as the source. The retained body is the
plain-request answer, and the row wording contains no bypass, automation or
challenge-solving language.

## What the section asserts, and how it is held down

- **Five types, from the two axes.** The coefficient axis (inside one power) has
  cumulative, ciphered and multiplicative; the power axis (across powers) has additive
  and positional. The section names the source's own terms (intraexponential /
  interexponential) alongside the plainer "coefficient / power" gloss. The sixth grid
  cell is recorded as **excluded and absent**, never as a type; the section contains no
  multiplicative-plus-positional type row.
- **No perfect system, no ladder.** The section states that no type is later or better
  than another and quotes the source's own "there is no perfect system" and its refusal
  of the Ifrah/Dehaene teleological reading. "Stage" survives in the section only inside
  sentences that refuse the stage reading.
- **Numerals vs notation vs tally vs computation** are separated in 4b.1 with their own
  base/no-base row and cross-references to the entry's existing sections, so the new
  section deepens rather than duplicates.
- **Actionable, non-canon.** 4b.5 is a worked example (a fictional tag-and-board market
  town, *Kharsund*) that runs three named constraints against the cost sheet and lands
  two coherent packages with a stated loser. It is explicitly a template, not a world, and
  hands off to lore. The name is new to the corpus (`grep -ric` over `corpus/knowledge`
  returns 0 for it).
- **Scope boundaries held.** The section says it does not certify the historical truth of
  any notation system, does not supersede `writing-systems.md` (which owns scripts), and
  does not decide any world's canon. The MacTutor pages are labelled tertiary accounts
  with their own stated revision date (December 2000), and their competing explanations
  for base 60 are reported as competing, not adopted.

## Gates

- `python3 -B stage/ScribeNotation/receipts/verify-quotes.py` → `ANCHOR QUOTES: 24/24 located
  in both copies`, `PROSE QUOTES: 31/31 located in the retained bodies`, rc 0. Every
  quotation in the section — the 24 anchor quotes and the 31 further quoted spans in the
  prose — re-located in the retained live and Wayback bodies.
- `python3 -B stage/ScribeNotation/receipts/mined-leg-check.py --section
  stage/ScribeNotation/notation-section.md` → the frozen claim-D leg arithmetic replicated
  read-only against a candidate merged entry: `heading-absent-at-base` 0, `heading-present-at-lands` 1,
  `table-rows` pass (10 data rows counted), `table-columns` pass (6), `new-rows-cited` 3
  (S931, S932, S933), `growth-bytes` pass (23012 bytes). **`new-rows-mined` FAILS at this
  moment — expected, and it is not mine to close**: the three registry rows do not exist
  in `corpus/SOURCES.md` yet (0 hits for S931/S932/S933 at HEAD). That leg closes only
  when ScribeRowsLesson's rows land.
- `python3 -B tools/check-cited-lines.py` on the merged candidate entry → `CITED-LINES: 0
  finding(s) in 1 file(s)`, rc 0. No line carries two distinct S-ids; no table row carries
  any S-id.
- Frozen `reports/round-88/claims.json`, `measure88.py` and `cases.json`: **not modified,
  not executed against the lane by this seat.** The D-leg check above replicates the
  counter's arithmetic in a separate read-only script rather than running the frozen
  instrument, so the frozen counter is untouched by this seat.

## Stage files

Directory `.ufo/waves/round-88/w1/stage/ScribeNotation/`:

- `notation-section.md` — the section text to land (23 KB).
- `section5-correction-fragment.md` — the staged §5 bullet replacement with its
  reasoning and the integrator's checks (7 KB).
- `receipts/receipts.json` — fetch manifest, hashes, capture URLs, 24 quote locators,
  access note, D-leg shape check.
- `receipts/S931-terrain-17506-lang-en-2026-11-04.html`,
  `receipts/S931-terrain-17506-wayback-20190505043833.html`,
  `receipts/S932-mactutor-babylonian-numerals-2026-11-04.html`,
  `receipts/S932-mactutor-babylonian-wayback-20200708131715.html`,
  `receipts/S933-mactutor-egyptian-numerals-2026-11-04.html`,
  `receipts/S933-mactutor-egyptian-wayback-20200724192341.html` — the six retained bodies.
- `receipts/verify-quotes.py` — re-locates every anchor quote in both copies.
- `receipts/mined-leg-check.py` — replicates the frozen D-leg arithmetic read-only.

Scratch `/fast/scratch/hyaku/kotodama-r88/ScribeNotation/` was created for the work, its
receipts were copied into the stage directory, and it was removed. It was never under
`/tmp`.

## Out of scope

- Production `corpus/knowledge/linguistics/numerals-and-measures.md`,
  `corpus/SOURCES.md`, `corpus/QUALITY.md` and `corpus/lessons/` were not edited.
- The frozen `reports/round-88/claims.json`, `measure88.py` and `cases.json` were not
  opened for editing, not modified, and the counter was not run against the lane.
- No git or jj mutation, no commit, no push, no branch, no index change. `git status` in
  the lane is unchanged by this seat beyond the pre-existing `M LOG.md` /
  `M corpus/QUALITY.md` and the round-88 untracked files that were already there.
- No task calls, no delegation, no background jobs, no fleet or sibling writes. The
  sibling seats' stage directories were read only to confirm the D-leg dependency.
- No tools were installed. `/home/vgpnk/.omp/agent/RULES.md` was read before any tooling
  decision, and existing tools (`git`, `curl`, `python3` stdlib, and the lane's own
  read-only `tools/check-cited-lines.py`) were sufficient. All pacman transactions remain
  paused as instructed.

## Findings, and limits worth carrying to the integrator

1. **The `new-rows-mined` leg depends on another seat's artifact.** The section cites
   S931/S932/S933; the registry rows that make the frozen leg read `mined` are
   ScribeRowsLesson's. My check script prints `LEG FAIL new-rows-mined expected=3
   observed=0` until those rows land. The rows must carry tier A for S931 and tier B for
   S932/S933, status `mined`, and `used-by
   corpus/knowledge/linguistics/numerals-and-measures.md` — that used-by path exists, so
   the census `E11` check will pass once the rows are in.
2. **The frozen row arithmetic is loose, and the section satisfies it twice over.** The
   frozen `table-rows` leg counts *every* pipe row in the section, subtracts **one** for
   the header, and takes the maximum pipe count for columns — it does not know where one
   table ends and the next begins. The staged section carries two tables, so the frozen
   count is 11 raw rows → 10 after a single header subtraction, and 6 columns. If the
   integrator keeps only the 4b.3 table (6 rows, 6 columns), the frozen arithmetic still
   gives 5 data rows and 6 columns, and the leg still passes. Both arrangements clear the
   thresholds, so the landing is not fragile to that choice.
3. **The §5 replacement must be applied in the split form.** The single-line version I
   first drafted carries three distinct S-ids on one line and would trip the
   clause-scoping lint with a MULTI-ID finding. The fragment file gives the five-line
   split form, which passes the lint. Whoever applies it must use the split form.
4. **The `writing-systems.md` overlap is a live risk and is fenced, not solved.** That
   entry's §6 already lists "math notation" among semasiographic systems and its
   "missing plumbing" note names numerals. My section keeps to *numeric sign systems* and
   states in its scope block that it does not supersede that entry's ownership of scripts.
   ConnectorScope is the seat that can judge whether the two now overlap materially.
5. **Two of the three sources are tertiary.** MacTutor's pages carry their own
   "Last Update December 2000" and their own internal tensions (the Babylonian page
   argues against its own listed origin theories, in the author's own voice). The section
   reports what the pages state, dates them, and declines to adopt their origin theories.
   Tier B for both is the honest call and matches the sibling rows' plan.
6. **The base-60 origin question is left open on purpose.** The section lists the
   competing explanations the page itself lists and quotes the author's own doubt about
   anyone "ever chose a number base". Nothing in the section picks a winner.
7. **Three of my first-draft locators were wrong, and the corrected values are in the
   staged file.** My initial anchors put paragraph 3 and paragraph 1 of the Terrain
   article body in the section "The transcoding engine"; both are in the introduction,
   before the first section heading. A third put the "cross-culturally very rare" rarity
   claim at paragraph 24 when it is paragraph 25 (24 is the neighbouring sentence about
   devices). All twelve S931 anchor lines were re-derived with an ascending-marker scan
   of the retained body (the article's own printed paragraph markers, 1–43) and its own
   section headings; the corrected values are the ones in the staged section and in
   `receipts/receipts.json`. The two misquotes I had made in the prose (writing the
   Babylonian empty-position sentence as "empty place" and dropping "anyone" from the
   author's base-choice sentence) were caught by the same re-verification pass and
   corrected; both are now exact. The verifier now checks all 55 quotations in the
   section, not only the anchors, so a later edit that disturbs a prose quotation will
   fail loudly. The MacTutor pages carry no printed paragraph
   numbering, so their anchors are located by a named body paragraph rather than by a
   number — a reviewer should not expect a number there.
8. **The sibling scout's table agrees with mine on every overlapping quote**, at the
   same paragraph numbers (Terrain ¶7, ¶9, ¶10, ¶19, ¶25; MacTutor body ¶2, ¶3, ¶10,
   ¶22). Two independent fetches landing the same spans in the same bodies is the
   strongest evidence I have that the anchors are stable and not an artifact of my own
   capture.

## Checks for the main agent

- After integration, `python3 -B reports/round-88/measure88.py --root . --base
  4956282281dac1306cfbe59523e46dde99749d75 --lands <lands> --claim D` should report
  `new-rows-mined` 3 and `new-rows-cited` 3. Until the three registry rows land, that leg
  reads 0.
- `python3 -B tools/check-cited-lines.py corpus/knowledge/linguistics/numerals-and-measures.md`
  must exit 0 after the landing.
- `grep -c '## 4b. Numeral notation: two axes, five types, and their trade-offs'
  corpus/knowledge/linguistics/numerals-and-measures.md` must return exactly 1, and
  `grep -c 'typological stages' corpus/knowledge/linguistics/numerals-and-measures.md`
  must return 0 after the §5 fragment is applied.
- `python3 -B stage/ScribeNotation/receipts/verify-quotes.py` must still print
  `ANCHOR QUOTES: 24/24 located in both copies` and `PROSE QUOTES: 31/31 located in the
  retained bodies` against the retained bodies.
- If the section is landed, the entry's §13 open item (2) — "no entry yet exists for
  numeral *notation* as a writing subsystem (Chrisomalis-grade detail)" — is partly
  answered. It is not closed here: the section is a typology and cost sheet, not a
  full notation-as-writing-subsystem treatment, and that entry's handoff note belongs to
  the integrator.
