# 06 — Uncertainty inventory (`to-verify`) and coupling source recheck

- Wave: `supplement-opencode-1` (not a numbered GLM round; OpenCode Go DeepSeek
  v4.1 Flash lane). Baseline revision: `fe34faaafbe0add59ff68827a0df6c5782a72404`.
- Owned artifacts written by this lane, and nothing else:
  `tools/source-audit-inventory.py`, this report, and
  `corpus/lessons/supplement-opencode-1/sources/06-coupling-table.json`.
- No corpus byte was modified in this pass (§5, §7). LOG/SCORECARD/SKILL and the
  frozen round-3/4 artifacts were not touched; the correction in §3 is handed to
  the parent as suggested wording, not written.

## 1. Commands executed and observed results

| Command | Observed |
|---|---|
| `python3 tools/source-audit-inventory.py --selftest` | `SELFTEST PASS: 3 planted entries, exact counts, policy/substantive split, no-write and determinism checks, missing-root, empty-root and non-UTF-8 exit-code controls`; exit 0 |
| `python3 tools/source-audit-inventory.py --json --summary --baseline fe34faa…` (root = frozen baseline extraction, §2) | exit 0, valid JSON, totals in §2 |
| `python3 tools/source-audit-inventory.py --root … --json …` twice, `cmp` | byte-identical output (determinism) |
| `find <frozen root> … sha256sum \| sha256sum` before/after both scans | `831c3ace…` before and after — the scan wrote nothing |
| `grep -rc 'to-verify' <frozen root> --include='*.md' \| awk -F: '{s+=$2} END {print s}'` | 590 (tool `totals.raw_lines` = 590) |
| per-file `grep -c` vs tool `raw_lines`, all 179 files | 0 mismatches (both sum 590) |
| `grep -rEo '\(to-verify[^)]*\)' <frozen root> \| wc -l` | 566 (tool `marker_occurrences` = 566) |
| `grep -ro '(to-verify)'` / `grep -rio 'to-verify'` | 537 bare markers / 597 case-insensitive occurrences (tool: bare 537, ci 597) |
| `git archive fe34faa corpus/knowledge \| tar -x -C <tmp>` | frozen baseline extraction, 179 files, tree digest `831c3ace8a19c1117c58ee4a8ea3f32b8484bb6e30e269da6150ea1a076f4e19` |

The corpus is live during this wave: peers appended dated errata to
`africa-primary-sources.md`, `ottoman.md`, `slavs-early.md`,
`color-terminology.md`, `kinship-terminology.md`, `phonetics-phonology.md` and
`semantic-fields-lexicon-building.md` while this lane ran. Every "baseline"
number below is therefore computed from the frozen `fe34faa` extraction, not
from the working tree; live values are reported separately and dated.

## 2. Actual baseline totals (`fe34faa`, 179 files, 32,350 lines)

| Metric | Baseline `fe34faa` | Live tree 2026-10-17T15:47Z (digest `1416bb5e…`) |
|---|---|---|
| files / lines | 179 / 32,350 | 179 / 32,447 |
| `raw_lines` (case-sensitive, = SCORECARD's command) | **590** | 591 |
| `raw_occurrences` (case-sensitive, `grep -o`) | 595 | 597 |
| `ci_occurrences` (case-insensitive) | 597 | 599 |
| `case_variant_occurrences` | 2 (`TO-VERIFY`, `To-verify`) | 2 |
| `marker_occurrences` `\(to-verify[^)]*\)` | **566** | 567 |
| — `bare_marker_occurrences` `(to-verify)` | 537 | 538 |
| — `detailed_marker_occurrences` `(to-verify: …)` etc. | 29 | 29 |
| `marker_lines` | 563 | 564 |
| `unparenthesized_occurrences` (policy prose, handoff rules, file names) | 31 | 32 |
| files with ≥1 mark / ≥1 parenthesized marker | 123 / 109 | 123 / 109 |

Baseline by directory (files / raw_lines / markers): civilizations 94 / 404 /
401 · culture-material 16 / 4 / 3 · linguistics 16 / 16 / 4 · myth-symbol
16 / 9 / 0 · synthesis 24 / 86 / 89 · verification 13 / 71 / 69. Markers can
exceed raw_lines because a line may carry several marks.

## 3. Reconciliation of the claimed 612 / 1258 totals

Independent per-commit counts (`git grep`, case-sensitive, `corpus/knowledge`):

| Revision | Files | `raw_lines` | `raw_occurrences` | markers | ci lines |
|---|---|---|---|---|---|
| `49ac1a5` mint | 176 | **1258** | 1286 | 1165 | 1260 |
| `291c714` round 1 | 176 | 795 | 807 | 760 | 797 |
| `1688790` round 2 | 176 | 587 | 592 | 560 | 589 |
| `c610e0a` round 3 | 178 | **612** | 623 | 593 | 614 |
| `fe34faa` round 4 / baseline | 179 | 590 | 595 | 566 | 592 |

Both endpoints named in `SCORECARD.md:14` ("rounds 1–3: 1258 → 612 raw sum")
reproduce exactly with the scorecard's own command. What does not reproduce is
the implied progress curve: round 2 was already **587** and round 4 is **590**,
so 612 was a local high, not the low end of a triage series.

Round 3's +25 is fully accounted per file: `mesoamerica-primary-sources.md`
0→32 and `gate-frozen-run-standard.md` 0→1 against `politeness-taboo-euphemism.md`
8→3 and `deity-name-derivation-pipeline.md` 4→1. That is 33 marker lines added
(a rewritten entry) and 8 removed — new marks in new text, not uncertainty
found in old text.

Why the raw line metric cannot carry a freshness claim:

- It counts **lines containing the string**, so second and later marks on a line
  are invisible (595 occurrences on 590 lines at baseline).
- It counts **~31 non-mark uses** — handoff instructions ("flag every
  to-verify item"), lane file names (`to-verify-triage-protocol.md`), and the
  vocabulary rows that define the mark (`metadata_status`).
- It moves with authoring as easily as with resolution: round 3 proves this.
- Its absence proves nothing about scholarship. A zero-count file is reported by
  the tool as "no marker found; scholarship not assessed", never as verified.

`reports/supplement-opencode-1/claims.json` carries `raw_to_verify_lines: 590`,
which matches the baseline exactly; the defect is confined to the scorecard's
paired endpoints and to `LOG.md:45` / `LOG.md:390`, where 1258 is likewise a
line count rather than a resolved-claim count.

Suggested correction wording for the parent to integrate (parent owns LOG and
SCORECARD): "raw `to-verify` line sum: mint 1258 → r1 795 → r2 587 → r3 612 →
r4 590; non-monotone, inflated by policy prose and multi-mark lines, and not a
resolved-claim measure; parenthesized markers at baseline 566 on 563 lines, of
which 537 are bare and 29 name a target."

## 4. What the inventory measures, and how honest its classification is

Definition of every counter is in the tool docstring and echoed in the JSON
(`schema: kotodama-source-audit-inventory/1`). Each occurrence record carries
file, line, column, matched text, form (parenthesized/bare), variant, a bounded
context excerpt (≤200 chars, `context_truncated` flagged), a class, the class
basis, and `heuristic: true` / `review_required: true`. Files carry sha256,
size, and `resolved_scholarship: "not-assessed"`. Top-level caveats assert
`marker_absence_is_not_verification`, `markers_never_auto_cleared`,
`classification_is_heuristic_needs_review`, `line_count_is_not_a_quality_score`.

Measured classifier quality on the frozen baseline — reported because a
heuristic nobody checked is a liability:

- 487 occurrences were classed `substantive-flag-candidate`. A random sample of
  25 (`random.seed(20261017)`) hand-checked against the full lines gave 13
  attached to a specific claim and 12 to use-mention, definition, or handoff
  prose (~52%; small-sample interval is wide, roughly 31–72%).
- All 18 `policy-use-mention` rows inspected were genuinely policy prose.
- Of 79 rows classed "policy shape covers a parenthesized mark", 12 sampled:
  ~10 were policy instructions that also carry a mark, ~2 were claim-attached.
- Of 11 rows left as bare "needs-review", ~4 were claim-attached flagged
  details and ~7 were policy/handoff prose.

So the split separates *some* policy prose from the marker population but must
not be read as resolved-vs-unresolved. Known improvement backlog, not applied
here: a definiendum pattern (`` `(to-verify)` marks … ``), table-cell vocabulary
rows, and the `- sources:` placeholder form.

## 5. Gate and mechanism evidence

- **Selftest (positive and negative controls):** three planted entries — a
  marker-dense positive file (9 case-insensitive occurrences, 6 marks, 5 bare,
  1 detailed, 1 line with two marks, 2 case variants, both classes produced), a
  genuinely clean negative file (all counters 0, `occurrences: []`), and a
  policy-only negative file (3 mentions, 0 markers, no substantive class). It
  additionally asserts: the scanned tree's digests are unchanged by the scan,
  two scans produce byte-identical JSON, paths are relative and sorted,
  non-markdown files are reported as skipped, `bare + detailed == markers`,
  `unparenthesized == ci_occurrences - markers` and never negative, and the CLI
  exits 0 on a normal and an empty root and 2 on a missing root and a
  non-UTF-8 file. Exit 0 observed.
- **No writes:** the tool opens files read-only and has no write path; the
  selftest proves it mechanically, and the frozen scan tree's digest
  (`831c3ace…`) is identical before and after both scan modes.
- **Cross-implementation parity:** `grep -rc` per file matches the tool on all
  179 files, and total markers (566) match an independent `git grep -oE` count.
- `--selftest`, `--json`, `--summary`, `--root`, `--baseline` are the whole CLI;
  output is deterministic (no clock, environment, or network value).
- Two of my own metrics were wrong at first write and were caught by the
  selftest before any number reached this report: `unparenthesized_occurrences`
  mixed a case-sensitive count with a case-insensitive one, and `raw_lines`
  counted case-insensitively (592) instead of the documented case-sensitive
  definition (590). The "detailed mark" regex also missed space-suffixed forms
  like `(to-verify locally)`; it is now "parenthesized but not bare", which makes
  bare + detailed = markers exact. A third defect surfaced only after the
  `raw_lines` fix: the positive fixture's expected line count had itself been
  calibrated to the buggy case-insensitive behaviour, and the selftest failed
  (expected 7, got 6) until the expectation was corrected — the control caught a
  stale expectation rather than a code error, which is what it is for.

## 6. Source recheck (freshness axis)

Assigned entry: `corpus/knowledge/synthesis/costume-language-coupling-table.md`
(sha256 `caaca840b9cefc1081a28c6424628467e657a6f34a64296e2c3d96d789a7ebde`,
unchanged from baseline to handoff; 18 parenthesized marks on 15 lines).
Full structured rows with excerpts, locators, verdicts and access limits:
`corpus/lessons/supplement-opencode-1/sources/06-coupling-table.json`.

| ID | Claim rechecked (entry locator) | Source retrieved | Verdict |
|---|---|---|---|
| KTD-06-01 | R4: latus clavus = broad purple band woven down the centre of the tunica, senatorial (line 82) | Rich, "Clavus Latus", Smith's Dictionary 1875, pp. 293–294 (Thayer full text) | supported |
| KTD-06-02 | R4: Augustus lets senators' sons assume the stripe after the gown of manhood (SA 38.2) | Suetonius, *Augustus* 38.2 (Rolfe trans., Thayer full text) | supported |
| KTD-06-03 | R3: PS75 records pura/libera and cites Fasti III.771 for libera (line 81) | Smith, "Toga", 1875, p. 1137 (Thayer full text) | supported |
| KTD-06-04 | Q1: 補子 bǔzi is the museum citation form for Ming–Qing badges (line 83) | Cleveland Museum of Art open-access records (1985.32, 1948.69, …) | supported |
| KTD-06-05 | Q1: crane–first-rank pairing reported from the 1391 Ming regulation (line 83) | Cleveland descriptions (1391 sentence); Met page text not retrievable | **unresolved** |
| KTD-06-06 | M1 Kangxi 1662–1722 kesi; M2 late 17th–early 18th c. embroidery on satin (lines 69–70, 83) | The Met Collection API objects 60511 and 62893 | supported |

Three rows test coupling rather than an isolated bibliography fact: dress
feature ↔ rank language ↔ Augustan era (KTD-06-01/02), rite and life-stage ↔
lexicon ↔ era (KTD-06-03), and badge design ↔ rank ↔ Ming 1391 regulation ↔ Qing
object (KTD-06-05). KTD-06-05 stays open on purpose: Cleveland's own crane
badges are described as "fourth or higher ranks" and one portrait's crane as the
"third ranked officer", so the first-rank reading is a curatorial statement the
entry already hedges and cannot be generalized; the Met's interpretive text was
rate-limited and its archived snapshot exposes metadata only.

No erratum was appended to the entry: no factual correction was demonstrably
supported, so under the append-only rule there was nothing to correct. Two of
the entry's six flagged rows came back supported and are recorded as evidence,
not as marker removal — the markers stay.

## 7. Unresolved, limits, and what the parent owns

1. **`LOG.md` / `SCORECARD.md` correction** (§3 wording) is proposed, not
   written — parent-owned files, per lane boundaries.
2. **Baseline vs live drift:** peers wrote to seven knowledge files during this
   run; the live tree (digest `1416bb5e…`, 15:47Z) already differs from
   `fe34faa` (591/597/567 on the live count). Any number in this report that
   must be reproducible should be re-derived from the frozen extraction or from
   a fresh `git archive` of the revision being reported.
3. **Classifier precision** is ~52% for the substantive bucket on a 25-row
   sample (§4). The tool says so in its caveats; do not quote class totals as
   resolution statistics.
4. **KTD-06-05 remains open** (crane = first civil rank), with the divergence
   recorded in the JSON.
5. **Kyoto National Museum and the Ovid Loeb/Kline texts** were not re-fetched in
   this pass; the entry's own checks of them are not independently confirmed
   here, and KTD-06-03/04 record that limit.
6. This report is author-side evidence only: no rank promotion, no SHONEN
   checkbox, no shared-bookkeeping write. No permission or restricted ritual
   detail is asserted anywhere in it.
