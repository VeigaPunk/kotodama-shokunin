# RevSourceRows — round 76 W2 falsification (S894–S896)

Scope: registry rows S894/S895/S896 (`corpus/SOURCES.md:849-851`) reviewed against their opened pages
(`reports/round-76/evidence/S894.txt`, `S895.txt`, `S896.txt`), access dates, quote anchors,
status/recheck/used-by, and the registry contract (`corpus/SOURCES.md:5-12,19-21`). Revisions inspected
read-only via jj at base `98c486b`, frozen config `df0f030`, Ca landing `a43ed807`, C landing `722e69ff`.

## Findings

### F1 — MEDIUM — frozen S938→S895 map cell does not join the S895 row's named URLs

- Map cell: `.ufo/waves/round-76/assimilation/id-renumber-map.json:603-620` (identical bytes at
  `df0f030`, `722e69ff`, `a43ed807`). `S938.document_normalized` (`:607`) and
  `staged_url_cell_urls` (`:609`) carry
  `openstd.samr.gov.cn/bzgk/std/showGb?type=online&hcno=E107EA4DE9725EDF819F33C60A44B296`; `:618-620`
  say "append lane row S895 … alias only, no second row".
- Row cell: `corpus/SOURCES.md:850`, column 2 (source) names exactly two URLs — live
  `https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=E107EA4DE9725EDF819F33C60A44B296` and capture
  `https://web.archive.org/web/20260424031027id_/https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=…`.
  The alias appears only as prose ("showGb?type=online redirects here by HTTP 302") with no full URL.
- Inconsistency: the map's document identity for S938 is a URL string that occurs in no URL cell of the
  row it maps to. By the round's own one-document rule (302 alias of the same record — proven in
  `.ufo/waves/round-76/w1/RevQualityFit.md:94-102` and ExecCaptureEvidence R1, and asserted by the row's
  own prose), the map cell should normalize S938 to the `newGbInfo` document, as its sibling S932 entry
  correctly does (`id-renumber-map.json:582-601`, `document_normalized` `:586`). This is exactly the
  COLLCHECK red the round declared (`corpus/lessons/round-76.md:89`).
- Where the fault sits: the map cell, not the row. The row is faithful to what was opened
  (`reports/round-76/evidence/S895.txt:2,31-37`). The lesson's wording "the appended S895 source cell
  only names its `newGbInfo` target" (`corpus/lessons/round-76.md:89`) is imprecise — the cell also
  names the alias by route — but it never carries the alias URL, so the map/row join still fails.
- Repair route (recommendation): a map-normalization erratum (fold `showGb`→`newGbInfo` for document
  identity), not any edit to the immutable row.

### F2 — MEDIUM-HIGH — at the Ca landing the three rows are `mined` with a dangling used-by path

- Cells: `corpus/SOURCES.md:849-851` at `a43ed807` (byte-identical to C; `jj diff` C..Ca on
  `corpus/SOURCES.md` is empty): status cell = `mined`, used-by cell (column 11) =
  `corpus/knowledge/culture-material/calendar-festival-systems.amend-2026-10-24.md` in all three rows.
- Tree at `a43ed807`: that path does not exist. `jj file list -r a43ed807` shows only
  `corpus/knowledge/culture-material/calendar-festival-systems.md` under `corpus/`; the amendment exists
  solely as w1 drafts (`.ufo/waves/round-76/w1/drafts/corpus/knowledge/culture-material/…`). Knowledge
  file count Ca 675 vs C 676; the missing file is the used-by target.
- Contract: `corpus/SOURCES.md:19-21` defines `mined` as "cited by the paths in `used-by`". At the Ca
  landing revision the citation target is absent, so the rows' status is not derivable from that tree.
  The Ca branch landed the rows itself (SOURCES.md last touched in Ca ancestry by `cab52475b6dd`
  "round-76: correct base ground and mirror receipts") without the citing entry.
- Contrast: at the C landing the target exists and cites all three rows with matching URLs and byte
  hashes (`722e69ff`, `calendar-festival-systems.amend-2026-10-24.md:3-5`), and the census receipt
  closes `kotodama ok … exit=0` (`reports/round-76/telemetry/census-end.txt`).
- Not covered by declared counter reds: the Ca LEDGER failures (`corpus/lessons/round-76.md:89`) are
  L76-13 (stated-at path outside the append-only allowlist) and L76-19 (stated text not found) —
  neither grades the dangling used-by. This defect is additional.

## Verified clean (no row defect)

- Opened pages and anchors: for each row the committed evidence window's sha256 re-verified, and the
  row anchor locates verbatim (and folded) inside the stored window — S894
  「元号名称 開始西暦年 令和 2019」 (`S894.txt:33-37`), S895 「标准号：GB/T 33661-2017」
  (`S895.txt:31-37`), S896 「首次明确了农历的编排规则、计算模型和精度等」 (`S896.txt:31-37`).
  Locators agree with the Gate table (`corpus/lessons/round-76.md:11-13`).
- Access dates: row `opened` cells, Gate table, and evidence `access-date:` all 2026-10-27; fetch
  timestamps 2026-10-27T21:35:53–56Z.
- Capture pairing (QUALITY c18 shape): S894 capture is of the same URL (memento
  `link rel="original"` exact, `.ufo/waves/round-76/w1/ScoutDocS894.md:34`); S895 capture is of the same
  `newGbInfo` URL; S896 capture original is scheme-only http→https of the live URL
  (`.ufo/waves/round-76/w1/ScoutCDXPositive.md:12`).
- Tier/kind spread at census: base 817 rows A491/B310/C16 → end 820 A493/B311/C16 = exactly +2 A
  (S894, S895) +1 B (S896), matching the rows' tier cells; census-start/census-end receipts committed.
- Append-only discipline base→C: `jj diff` on `corpus/SOURCES.md` is additions only (3 rows + Paths/
  search-log lines); no pre-existing row's `status`/`recheck`/`used-by` changed. S894–S896 were free ids
  at base (registry ended S893; `.ufo/waves/round-76/w1/ScribeLesson.md:109` F7).
- Recheck cells: uniform `180d` across the three rows; Gate flip conditions (re-open, else unverifiable)
  match the lesson.
- used-by closure at C: the amendment cites S896/S895/S894 with the same URLs and sha256 values the
  rows record (S894 live `204b7188…` / capture `c015e1dc…`, S895 `f04feb47…`, S896 `670850ea…`).
- C vs Ca on the three rows: byte-identical cells; the F2 defect is tree-relative, not a row edit.

## Method and compliance

Read-only inspection of committed trees at the four cited revisions (jj/git plumbing only); sha256 and
folded-substring checks over the three committed evidence files; no builds, tests, linters, or
formatters; no tools installed; no source, lane, claim, counter, or report file modified except this
seat report; no scratch directory created (nothing to remove).
