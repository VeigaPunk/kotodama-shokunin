# CritQuarantineDesign — quarantine-verdict table gaming analysis (round 71, wave 1)

Seat: `L1Kotodama71.CritQuarantineDesign` (critic, leaf, read-only).
Target: the 21-row quarantine verdict table required by claim Ca
(`reports/round-71/telemetry/quarantine-verdicts.md` + lesson).

## 1. What is actually scored (the gate)

Claim Ca's `counting_command` for the table (frozen in `reports/round-71/claims.json`):

```
awk -F'|' 'NR>1 {print $1}' reports/round-71/telemetry/quarantine-verdicts.md | wc -l
```

Target / kill rule: **21 rows with nonempty verdict labels**. That is the entire scored
surface. No verdict vocabulary, no evidence columns, no join to fetch receipts, no
re-derivation of the slice.

The controlled input is the shokuknow absent-defect register
(`/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md`,
read-only). Its own class semantics define what a *legitimate* verdict distribution looks
like:

- **18 payload-absent rows** (S776 S778 S779 S786 S787 S791 S792 S795 S796 S804 S814 S816
  S817 S820 S823 S824 S825 S827) — by the register's definition: *every relevant source
  fetched cleanly and the quote is in none of them*. The quote was already checked by the
  campaign census; the fabrication class says "verify by hand, then correct the quote or
  refuse the row". A payload-absent row resolved on a clean fetch must land as PRESENT or
  REFUSED. Labeling it UNVERIFIABLE with no new reason is a category error.
- **3 unreachable rows** (S807, S812, S835) — register prose: "the cited source could not be
  fetched, so no quote was checked"; no locator recorded. These are legitimately
  UNVERIFIABLE (nothing to hand-check).

The verdict set is therefore not a free 21-slot distribution: the 3 unreachable rows are
UNVERIFIABLE by construction, and the 18 payload-absent rows may only be UNVERIFIABLE if
the table records a concrete new fetch failure (exact error + what was tried) that reopens
them. Nothing in the count-only gate enforces any of this.

## 2. The counterexample (gaming the table)

**All-UNVERIFIABLE no-fetch dodge.** Write 21 rows, first column `UNVERIFIABLE`, second
column any nonempty text (e.g. `no fetch attempted this round`). The gate prints 21, exits
0, claim Ca's verdict leg passes. No fetch, no quote search, no fabrication exposure, no
risk of a wrong PRESENT/REFUSED. The table is then content-free: it cannot be used by a
later adoption round and it fails the register's own purpose (payload-absent rows are
*fabrication candidates* that must be declared either found or refused).

Variants that also pass the gate:
- PRESENT rows with a plausible-looking span that was never located in any served bytes
  (no `found` evidence) — e.g. copy the register's "quote(s)" cell into the table and
  stamp `HTTP 200`.
- 21 "rows" fabricated by padding, duplicates, or mismapped ids (see §4 fake 3): any 21
  pipe-lines whose first cell is nonempty satisfy `wc -l` regardless of whether the ids are
  the slice ids, whether they are distinct, or whether they are even S-ids.

## 3. Minimum evidence each verdict must carry

Evidence must be committed, machine-readable, and mechanically joinable to the row
(round-68 precedent: `.ufo/waves/round-68/assimilation/quarantine-handcheck.json` per-row
`status/err/found/ctx/sha256/bytes`; `quarantine-pdf-pass.json` per-PDF byte/text counts
and found spans). A verdict column that is prose-only is not evidence.

| Verdict | Required minimum evidence |
|---|---|
| **PRESENT** | The **quote bytes found** (the exact matched span) **+ anchor**: for HTML, URL + HTTP status + a locator in the served bytes (element context / line:col; round-68 stores `ctx`); for PDFs, URL + page + pdftotext hit (round-68 `quarantine-pdf-pass.json`). Plus capture identity: source URL, capture URL (live or `web.archive.org/web/<ts>id_/`), captured-byte sha256, fetch date. "HTTP 200" alone is not PRESENT — the span must be found in the served bytes (`found != null`). |
| **REFUSED** | **Fetched page evidence**: resolved URL, HTTP status (+ content-type, byte size, fetch date), and the capture/artifact identifier. **The exact quoted span searched**. **Absence note**: what was searched (span normalization / folds) and confirmation the span is absent from the served bytes — plus, where useful, what *was* found instead (round-68 S779: "nao.ac.jp serves no Chinese 国家级名录 text — quote appears to belong to a different source"; S825: portal landing, not the table page). REFUSED is the fabrication class; the note must stay visible. |
| **UNVERIFIABLE** | **The exact error** (HTTP code, TLS/DNS failure, timeout, truncated locator, no locator) **+ what was tried** (which URLs/locators, when, and why the check could not proceed). Distinguish `broken locator` (S791: register URL cell truncated mid-percent-sequence → HTTP 400) from `never checked / no locator` (S807/S812/S835). A clean HTTP 200 fetch is never UNVERIFIABLE — absence determination then belongs to PRESENT/REFUSED. |

Every row must also carry its slice identity (the register's package S-id, NOT the lane's
registry id — namespace collision already recorded in the round-68 lesson) so a later
adoption round can bind the anchor to the right row.

## 4. Three ways the table can be faked, and the guard for each

**Fake 1 — All-UNVERIFIABLE / no-fetch dodge** (the counterexample above; also
"PRESENT without locating the quote" by stamping a seen span).
*Guard:* a verdict **schema gate run at count time** (new or existing `tools/check-*.py`
style tool, exit 0/1/2, selftest) that enforces:
 (a) verdict label ∈ {PRESENT, REFUSED, UNVERIFIABLE};
 (b) per-label required columns present (the §3 minimums — nonempty, non-placeholder);
 (c) class admissibility: the row's register class is derived live from the register by the
     same awk re-derivation; a payload-absent row carries UNVERIFIABLE **only** if its
     error column records a concrete fetch failure; the 3 unreachable rows must be
     UNVERIFIABLE (or carry a recorded new fix).
The gate is not a formality check on the table's own strings: it re-derives the class from
the register, so an all-UNVERIFIABLE table fails (c) for the 18 payload-absent rows.

**Fake 2 — PRESENT without locating the quote** (evidence-free or stale PRESENT rows:
claiming an anchor that was never matched in any captured bytes, or reusing round-68
verdicts verbatim without re-fetching — round-69 explicitly declined to re-fetch and
claimed *no new verdicts*; a round-71 re-derivation must either re-fetch or point to
committed receipts).
*Guard:* PRESENT rows must **join mechanically to committed capture evidence** — the span
in the row's `found` column must exist in the corresponding capture artifact (handcheck
JSON / PDF-pass JSON / committed raw bytes with sha256), and the anchor must resolve in it.
The join is part of the schema gate; unjoinable PRESENT = finding. Additionally, an
**independent non-author spot-check** (reviewer/verifier seat re-fetches a sample of
PRESENT rows and re-locates the span) — the same independence that routed V70-1..V70-6.

**Fake 3 — Row-set cosmetics to reach 21** (padding, duplicates, non-slice ids, or
mismapping package ids to lane registry ids, so `wc -l` passes without 21 genuine verdicted
rows; the current gate counts *any* 21 nonempty first cells).
*Guard:* a **bijection check**: the table's S-id set must equal the awk-re-derived 21-id
slice exactly — no duplicates, no extras, no omissions — and the table header must pin the
register input's revision (sha256 of the register bytes or of the committed slice file) so
a stale or re-rowed table fails. Ids are parsed from the register with the lesson's recipe,
not trusted from the table. This guard also makes Fake 1/Fake 2 rows fail if their ids are
wrong, not just their labels.

## 5. Impacted axes

- **Calibration (claim Ca)** — the verdict-table leg as frozen is vacuous: count-only.
  The defect does not falsify the claim as written (21 rows with labels will pass), but it
  makes the leg's *meaning* unverifiable and lets a fake table clear the kill rule.
- **Coverage (claim C)** — the round-71 entry cites new SOURCES rows; the round-68
  verdict anchors ("adoptable in a later round with this round's anchor") were the
  mechanism that let later rounds trust the package. A faked table silently breaks the
  future adoption contract.
- **Depth (claim D)** — not touched directly; the same count-only-tool pattern is what
  claim D's no-git guard exists to prevent elsewhere (a counter that passes on cheap
  content). Consistent with the campaign's drift-sentinel lessons (kake r35, tsukuroi
  r31: counters that cheap/false content also meet).

## 6. Smallest safe corrections

1. Freeze the schema gate (verdict vocabulary + per-label evidence columns + class
   admissibility) as part of claim Ca's acceptance for the table file, with a selftest
   and a pre-data do-nothing control (base tree: no table → gate non-zero).
2. Require the table's rows to join to committed capture evidence (present → found span;
   refused → fetch status + absence note; unverifiable → error + tried), pinned to the
   register revision; keep the 18/3 class split re-derivable.
3. Add the bijection check (id set == slice set, no dupes, revision-pinned), and extend
   the frozen counting command to invoke the gate — `awk … | wc -l` alone stays in the
   receipt only as a row-count sanity line.

No new evidence beyond the register and the round-68 receipts was needed; everything above
is re-derivable from the frozen inputs.
