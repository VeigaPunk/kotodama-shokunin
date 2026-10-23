# SupS739 — blind support of the fixed S739 row

Axes named (godspeed): **coverage**, **operability**, **calibration**.

**Verdict: SUPPORTED.** The live row's scope and cells now match the quoted passage,
tier A is honest under the lane's scoped-tier rule, and the row is structurally and
RESTATE-compatible. The findings below are about stale stage artifacts and one
historical report file, not about the row's content. I did not edit the row, the
registry, the entry, or any git/jj state.

Row snapshot reviewed: `.ufo/waves/round-64/rows/ScribeRowS739/row.txt`,
sha256 `a9e6abc0a23a423be681a7d4708191f3154accce1981b1da54c076820db73530`,
mtime 2026-10-23 23:51:53 (-0300). The file was rewritten during the review window:
an earlier snapshot (~23:50) carried the Introduction/Aledo anchor; the current
snapshot is the one judged here and was hash-stable across repeated checks.

## Positive evidence

| Check | Result | Evidence |
|---|---|---|
| Cells / shape | 11 cells, no internal pipe; one ROW line | parsed with `check-rows.py` helpers; `CHECK-ROWS: 32/32 clean`, `S739 OK` |
| Anchor verbatim | 20 normalized words, present exactly | sentence extracted from `pdftotext live.pdf` reading-order text (raw.txt:322–324): "Based on the data obtained, urban parents in Sleman, Yogyakarta used various forms of address when interacting with their children." |
| Locator accuracy | section and paragraph both exist | raw.txt:293 "RESULTS AND DISCUSSION", :294 "Results"; the quoted paragraph begins at :322 immediately after "Diagram 1. Language Choice" |
| Scope ↔ quote | exact match | quote says urban parents in Sleman, Yogyakarta use various address forms with their children; scope cell = "parental use of address terms with children in urban Sleman, Indonesia". The wave-1 F3 mismatch (Aledo-2018 Introduction framing vs Sleman study) is gone with the Results anchor. |
| Tier honesty | A is correct | `corpus/SOURCES.md` preamble: tiers are scoped to the row's scope; A = primary/authoritative for that scope, explicitly including "original paper". The row's scope is this paper's own Sleman study, so A is not inflation. The F3 tier-inflation attack applied to the secondhand Aledo-anchored version, not to this anchor. |
| Teaches | 12 words (≤25), bounded to urban parents | "Helps worldbuilders model urban parents' use of varied address forms with children." |
| Bullet fidelity | faithful restatement, no added claim | clause 16 words (6–25); content words 13; in-order quote hits 7 (`urban, parents, sleman, address, when, interacting, children`); novel content words 5 (`study, results, show, using, varied`); longest copied run 5 (≤12); exactly one terminal `(S739)`. Adds only the attribution "Study results show". |
| Status cells | `mined | 2026-10-23 | 180d | corpus/knowledge/linguistics/language-socialization-and-acquisition.md` | as required for mined rows |
| Uniqueness | live URL, paper (Kurniawati), and quote occur only in S739 | `grep -rlF` across `.ufo/waves/round-64/rows/` and `corpus/SOURCES.md`; no same-work duplicate of the S718/S729 kind |
| Capture fidelity | archived bytes identical to live | live and Wayback fetch both HTTP 200, `application/pdf`, 303366 bytes, sha256 `c143fab87ebd61a5127d8da64b4f3678b92a6f7e26bbf352095557ad1effe235` for both; archived fetch at the exact stated timestamp 20240911000056 succeeded; CDX lists 20240911000056, same original URL, status 200, `application/pdf` |
| Source metadata | title/authors/volume/pages correct | title and three authors match the PDF; "LITERA, Volume 20, Nomor 2, Juli 2021"; first page 250, last page 268 |
| Lane locator | `LOCATED`, exit 0 | independent re-run of `python3 -B reports/round-61/reopen-quote.py '<live URL>' '<quote>'`; same result the seat reported |
| Row checker | `S739 OK`; `CHECK-ROWS: 32/32 clean` | read-only run after the rewrite; the seat's earlier `31/32` differed only by a concurrent S719 edit |

## Findings by severity

### MEDIUM (operability) — stale stage artifacts contradict the repaired row
- `.ufo/waves/round-64/stage/report.txt:39` still says `S739 PROBLEMS in_order=2`, and
  `.ufo/waves/round-64/stage/bullets.json` still carries the superseded bullet
  "Caregiver address teaches children to model culturally specific forms for addressing
  relatives in the community. (S739)". Both were computed against the old Aledo anchor;
  against the current anchor the same bullet yields in_order=2, while the current row
  bullet yields 7.
- The w2 assembler reads the row files, not this JSON: `.ufo/waves/round-64/integrate-w2.py`
  `parse_contribution` requires ROW/BULLET/VERIFY/CAPTURE/ACCESS from
  `rows/ScribeRowS739/row.txt` and maps S739 into §8. The stale files come from the
  wave-1 stager `.ufo/waves/round-64/integrate.py` (docstring line 8 names
  `stage/bullets.json` as an integration input; line 159 writes it).
- Risk: if the L1 consults `stage/report.txt` as a pre-check, or re-runs `integrate.py`,
  it will see a false RESTATE failure for S739. `integrate.py` reads
  `~/.cache/hyaku/kotodama-r64`, which no longer exists, so it cannot regenerate a
  correct stage. Recommended: assemble via `integrate-w2.py` and disregard
  `stage/report.txt` / `stage/bullets.json` for S739.

### LOW (calibration/evidence) — a historical report file must not be cited as current evidence
- `.ufo/waves/round-64/w2/B2FixS739.md` (mtime 20:04) presents the superseded
  Introduction/Aledo-anchored row as its "Corrected deliverable" and claims a re-anchor
  to a body sentence from the Introduction. The live row instead uses the Results anchor
  above. It is a historical artifact from an earlier attempt, not the seat's exclusive
  report; the seat confirmed it did not edit that file.
- The seat's actual report, `.ufo/waves/round-64/w2/FixRowS739.md` (mtime 23:52),
  correctly records the live row: scope and tier unchanged, anchor/teaches/bullet
  old→new exactly as observed here, locator `LOCATED`, and checker `S739 OK`. Cite that
  file, not `B2FixS739.md`, for S739's repair.
- Checker-snapshot note: the seat recorded `31/32 clean` with `S719 PROBLEMS
  bullet_shape` while a sibling seat was mid-edit on S719. My later run is `32/32
  clean`; `S739 OK` in both. The delta is the concurrent S719 repair, not an S739
  defect.

### LOW (provenance wording) — the ACCESS note's 429 is time-bound
- The ACCESS line says the archive availability API returned 429. That request now
  returns HTTP 200. The note was honest at observation time (the fix seat and this
  review both saw rate limiting earlier in the round); no row edit is needed unless the
  L1 wants current-state wording. Capture verification does not depend on that API: the
  capture fetch and CDX both confirm the timestamp and bytes.

### NOTE (verification technique) — layout extraction splits the quoted sentence
- `pdftotext -layout` breaks the sentence across the two columns ("...urban" /
  "parents in Sleman, Yogyakarta used" / "various forms..."), so a naive page-text grep
  misses it. The sentence is verbatim in reading-order extraction (`pdftotext` without
  `-layout`) and in the PDF text itself; the lane locator did locate it. Any independent
  verbatim recheck should normalize/reflow before calling it missing.

## Residual risk

- **Pre-integration state (expected, not a row defect).** `corpus/SOURCES.md` still ends
  at S717 (643 rows; the only pending diff is S687 mined→queued), and the `used-by`
  target `corpus/knowledge/linguistics/language-socialization-and-acquisition.md` does not
  exist. Until the L1 integrates, accept-c's ROWS/LINK/RESTATE legs cannot be exercised
  on S739 and the row is invisible to the counter. Static computation with accept-c.py's
  own functions gives content=13, in_order=7, novel=5, copy_run=5, clause=16,
  quote=20 — all inside the legs. LINK will require exactly one registry line containing
  the live URL and no occurrence of that URL in the entry; the URL is currently unique
  across staged rows and absent from the registry.
- **LIVE leg does not cover S739.** `LIVE_IDS` is every fifth id from S718
  (718, 723, 728, 733, 738, 743), so the counter will not re-fetch S739. The live URL was
  fetched here: HTTP 200, `application/pdf`, 303366 bytes.
- **Entry placement is static only.** `BULLET_MAP[8] = (S739, S740, S741)` places the
  row under §8 "Names, address and honorifics", which fits the claim; the entry does not
  exist yet, so the rendered citation is unobserved.
- **Same-file race.** A sibling seat was rewriting this row during the review; the
  judged hash is recorded above. If the row changes again, this verdict applies to the
  recorded snapshot only.

## Verification gaps

- No LSP server applies to a Markdown registry row; no `lsp` device is exposed in this
  session. Semantic checks used the frozen counter's own parsing functions plus direct
  PDF text, not grep-as-proof.
- No end-to-end `accept-c.py` run was made (the entry and registry rows are not yet
  landed, so it would fail for reasons outside this row). The 32/32 `check-rows.py`
  result was run read-only and passed.
- The quote was verified against the live and archived PDFs only; the journal landing
  page and HTML rendering were not used.

## Tooling

No installs or upgrades. Used system `curl`, `pdftotext`, `pdfinfo`, `python3`
(including accept-c.py and check-rows.py as read-only modules), `grep`, `stat`,
`sha256sum`. Scratch: `/home/vgpnk/.cache/hyaku/kotodama-r64-w2/SupS739/`
(`live.pdf`, `wb.pdf`, `live.txt`, `wb.txt`, `raw.txt`). The only lane write is this
report.

Report: .ufo/waves/round-64/w2/SupS739.md
