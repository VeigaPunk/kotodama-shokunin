# Round-65 lesson skeleton — `corpus/lessons/round-65.md` (+ lessons-index revision bump)

Seat **ScribeLessonR65**, round-65 v2 wave (build side), base revision
`17c32302c6845c8f164b985a8cb312d3181c8788`, 2026-10-24. This file is a draft
under `.ufo/`; the L1 integrates it. Nothing in it is a measurement of anything
that has not landed — every `<FILL …>` slot is filled at integration from landed
artifacts.

Grounding read for this skeleton: `corpus/lessons/round-64.md` (618 lines, model
for section order, row shape and note conventions), `corpus/lessons/README.md`
(556 lines, revision-13 head), `reports/round-65/claims.json`, the `QUOTES`
leg of `reports/round-65/accept-ca.py:229-236`, and `tools/check-gate-quotes.py`
(587 lines, docstring + `GATE_HEADING`/`ROW`/`QUOTE` regexes).

Two sibling drafts overlap this one and win where they are more specific:
`stage/gate-spec.md` (seat ScribeGateRecords — the `## Gate`/`## Mistakes`
shape, row line by row line) and `stage/lesson-gate.md` (seat ExecGateFill —
the assembled Gate, quote byte-equal to each fragment). At integration, if
`stage/lesson-gate.md` exists, **copy its rows verbatim** into the `## Gate`
section below rather than re-cutting quotes here: two independent cutters of the
same quote is how the round-64 near-copy class (R64-M4) re-enters.

Row fragments live at `.ufo/waves/round-65/rows/<SEAT>/row-<SID>.txt` (the
`--rows` default of `tools/check-row-fragments.py:265`, and the path the 13
ScoutRow seats are told to write). Each fragment carries one
`ROW=| <SID> | … | "<anchor quote 8-25 body words>" | …` line, so a Gate quote
lifted byte-equal from that span is inside the 25-word cap by construction. At
this seat's stamp `.ufo/waves/round-65/rows/` holds only `ScoutGapGames/` and
`ScoutRow02/` with no `row-<SID>.txt` — **no fragment exists yet**, which is why
every row below is a placeholder and not a quotation.

Measured base facts this skeleton binds to (all read-only, this seat, 2026-10-24):

| fact | measurement | command |
|---|---|---|
| lesson files | 65 | `ls corpus/lessons/*.md \| wc -l` |
| lessons-README §2 rows | 50 | `grep -c '^\| \`corpus/lessons/' corpus/lessons/README.md` |
| §2 rows naming a missing file | 0 | per-row `test -e` |
| pin drift on existing rows | 0 | bytes/lines/sha8 re-derived, no in-place cell differs |
| formats (live) | gate-keeper 35, fragment-index 5, plain 25 | `c31-lessons-index-audit.py` |
| lessons-README exit | 1, `findings: 3` | same tool, stdout `/tmp/audit65.txt` |
| `check-gate-quotes.py corpus/lessons/round-64.md` | `GATE_QUOTES: 0 findings`, exit 0 | shape control for the row form |
| `check-gate-quotes.py corpus/lessons/round-63.md` | `GATE_QUOTES: 0 findings`, exit 0 | second shape control |
| round-65 lesson on disk | absent at base (`ls` → no such file) | — |
| `corpus/lessons/README.md` in any claim's `lands` | **no** (C, O, Ca read in full) | claims.json |

---

## Part A — the lesson skeleton (copy from the next line into `corpus/lessons/round-65.md`)

# Round 65 — 2026-10-24 (hyaku run 5, L1 <FILL L1 name>)

source: `reports/round-65/claims.json` (the three frozen claims and predicates); the frozen counters
`reports/round-65/accept-c.py`, `reports/round-65/accept-o.py`, `reports/round-65/accept-ca.py` as
measured; `reports/round-65/telemetry/` (census, dry runs, final measures); the Gate rows' own
`row-<SID>.txt` artifacts under `.ufo/waves/round-65/rows/<SEAT>/`
verified-at: 2026-10-24 — <FILL: the measured landing revision and what was measured against it, e.g.
"lane worktree at `<rev>`, ACCEPT-C-65 / ACCEPT-O-65 / ACCEPT-CA-65 all PASS, receipt
`reports/round-65/telemetry/<file>`">. **R7 rule (round-64 spot-check §6): this line must not read
"skeleton", "prepared" or "await L1" once the content is in — the round-64 entry carried that stale
phrase for a whole round and it was routed as a defect.**
recheck: whenever a `corpus/SOURCES.md` row this round opened changes `status`, `recheck` or `used-by`,
and on each opened row's own `recheck` cadence (log old→new here, never edit the row in place outside
the registry append convention)
scope: the round-65 record — the three claims' lands, the 26 Gate rows S750-S775 with their located
or NOT LOCATED state, the round's counting instruments and receipts, the routed defects and their
dispositions. This lesson admits nothing and certifies no verdict; the verdicts are the three
receipts in `reports/round-65/telemetry/`.

## Round summary

<FILL at integration, modelled on `corpus/lessons/round-64.md:3-36`. It must state, with the measured
values only:>

- base revision `17c32302c6845c8f164b985a8cb312d3181c8788`, declared 2026-10-24, one v2 wave of
  64 seats (build+attack in the same wave).
- **C (coverage, sourced):** one new entry
  `corpus/knowledge/culture-material/games-play-sport-contests.md` supported by exactly 26 new
  registry rows S750-S775 (tier A/B, mined, opened 2026-10-24, used-by the entry, cited exactly once).
  Predicate `ACCEPT-C-65`: every leg of `reports/round-65/accept-c.py` prints PASS
  (legs FILE, ROWS, ONEID, RESTATE, HOSTS, LINK, APPEND, NOHARM, SWEEP, LIVE; LIVE frozen subset
  S750, S755, S760, S765, S770, S775). <FILL measured result + receipt path.>
- **O (operability, counter hardening):** the round-64 closure's six counter-gaming surfaces closed
  in the frozen counters — accept-c rev1 RESTATE word-boundary near-copy rule, accept-ca rev1 keyed
  legs and NITS value-pair pinning, accept-o FULL/MUTEX/FRAG, `tools/check-row-fragments.py`
  teaches-length and query-aware URL normalization; `reports/round-65/accept-o.py` declares 26 legs
  ending FULL, MUTEX, FRAG. Predicate `ACCEPT-O-65`. <FILL measured result + receipt path +
  counter sha256s (a revision label is not an identity — round-64 R64-M17).>
- **Ca (calibration, records):** the round-64 verifier spot-check's seven routed defects R1-R7 each
  dispositioned by one counting leg (R1..R7, CRITERION, QUOTES). Predicate `ACCEPT-CA-65`.
  <FILL measured result + receipt path.>
- Attempt history is part of the record (round-64 precedent): <FILL the wave's dead-seat
  re-dispatches, superseded drafts and red receipts, if any, with their paths.>

## Gate (rows opened this round; each quote is the anchor quote of that row's own
final `row-<SID>.txt` fragment; a row whose wording could not be located on the cited
URL is annotated NOT LOCATED in the round-64 D2 form rather than presented as a
located quotation)

<FILL: exactly 26 rows, S750 through S775 in id order, one row each, this shape
(a 2-space indent here only so this draft is not itself parsed as a Gate row;
the landed rows start at column 0):>

  - S750 | <URL> | 2026-10-24 | "<anchor sentence, one quoted run, <= 25 words, byte-equal to that row's own quote>"

Row rules, each backed by a counter leg or a filed round-64 defect class:

1. **One quoted run per row, <= 25 words.** `tools/check-gate-quotes.py` sums
   every span between two spans of prose into one run (round-64 R64-M4: a
   quoted section locator ahead of the body sentence became the "quote" and the
   counter read 3-5 words). Put the body sentence in plain double quotes first
   and leave the locator unquoted.
2. **No `Grounds:` that truncates the row's `teaches` cell** — checker class
   `truncated-grounds`; a Grounds equal to the whole cell (ending in a full
   stop) is not reported, an opening sentence copied out of a longer cell is.
3. **Do not repeat the locator's text as a quoted span** after an
   `accessed <date> — ` field — checker class `doubled-locator`. The round-64
   pipe form (`id | URL | date | "quote"`) carries no `accessed` field and is
   not read by that class; keep that form unless a seat has a reason not to.
4. **No HTML character references in a quote** — checker class `html-entity`;
   decode them in the row artifact instead (S749-class wording).
5. **NOT LOCATED is a state, not a quotation.** A row that could not locate its
   wording says so, names the failing fetch, and carries no quoted wording
   (round-64 S744/S745/S747 form). Never print tested wording as if located.
6. **Exact set.** The Gate holds the 26 opened ids and no other `- S###` row;
   the LIVE frozen subset (S750, S755, S760, S765, S770, S775) must be the same
   wording as its row artifact.
7. **The gate is machine-checked:**
   `python3 -B tools/check-gate-quotes.py corpus/lessons/round-65.md` must print
   `GATE_QUOTES: 0 findings` and exit 0. That run *is* the `QUOTES` leg of
   `reports/round-65/accept-ca.py` (which requires exit 0 and `0 finding` in the
   output); exit 2 means the file has no `## Gate` section at all.

Notes on the Gate, one `Note: S### —` line per deviation (not a row), in id
order — <FILL: e.g. a row re-sourced, a locator corrected, a quote re-cut to fit
the cap, a host refused live and its same-page capture cited. Round-64 notes to
model on: `corpus/lessons/round-64.md:107-135`.>

## Mistakes

- R65-M1 (class: receipt-attribution). <PLACEHOLDER — verify every clause against
  the landed bytes before integrating.> The round-64 `Ca` receipt asserted
  `measured revision: 95c9194ef938e1338b2af894086a46e8b8677ee2` while the bytes
  its read path actually equalled were the records commit
  `8bab271c691c6b1006da95316a24ae1958ec01e2`, 17 minutes later, over a dirty
  worktree — and no instrument compared the stamp with the bytes it read, so the
  receipt could not be bound to a revision at all. Evidence:
  `reports/round-64/telemetry/final-measures-ca.txt` (re-stamped this round, the
  original bytes preserved below a marker) and
  `corpus/lessons/round-64-verifier-spotcheck.md` §6 R1 (HIGH). Captured by:
  nothing at the time — the protocol had no tree-hash-of-read-inputs rule. Now
  captured by the `R1` leg of `reports/round-65/accept-ca.py` (receipt must name
  the measured revision *and* `tree: <sha>` of its read inputs) and by
  `corpus/QUALITY.md` criterion 17. Fix (standing): a receipt pins the measured
  revision plus a tree hash of the inputs it read; the counter sha256 alone binds
  the instrument, not the measurement, and a revision label is a name, not an
  identity.

<FILL: append this round's own rows as R65-M2, R65-M3, … from the wave's filed
findings, one class per row, each with evidence path(s), the seat or leg that
captured it, and a standing fix. Round-64's shape (`## Mistakes`, R64-M1..M19,
each with class / evidence / captured by / fix) is the model. Do not number rows
that no artifact supports, and keep the numbering the same one `LOG.md` and
`SCORECARD.md` cite — the round-61/62 mismatch (LOG said M1..M6, the lesson had
M1..M7) was itself routed as a defect.>

## Census and counts

<FILL from the receipts only: census start/wave/end (`kotodama ok`, exit 0),
registry `corpus/SOURCES.md` 675 -> 701 rows with tiers/statuses, corpus entries
238 -> 239 and culture-material 31 -> 32, the staged row set's tier histogram,
`corpus/lessons` file count (65 at base, 66 after this file lands), and the
measured counter sha256s with the receipt -> revision map. Every number carries
its receipt path; a number without a receipt is not written here.>

---

## Part B — `corpus/lessons/README.md`: the revision bump this round needs

### B.1 Exact current revision (measured, not inherited)

The index's last block is **Revision 13** — `corpus/lessons/README.md:554-556`,
whose own text is "Adds two §2 rows, for `round-55-verifier-spotcheck.md` … and
`round-56.md`, pinned from the live bytes at the round-56 records commit; rows
48, files 48 (the §2 count line above is left as filed)." No revision block
after 13 exists; there is no unstamped block to inherit from. The number in
force for the next landing is therefore **14**.

### B.2 Live state at base (what revision 14 lands on top of)

`python3 -B reports/round-25/audit/c31-lessons-index-audit.py` at
`17c32302…` (read-only, 2026-10-24) prints:

```
lesson files:  65
index rows:    50
queue rows:    78
formats:       {'gate-keeper': 35, 'fragment-index': 5, 'plain': 25}
  FAIL C31_index_rows_eq_files
  PASS C32_owners_resolve
  PASS C33_formats_documented
  PASS C34_pins_rederived
  FAIL C34c_shape_cells_rederived
  FAIL C34b_prose_arithmetic
findings:      3
exit 1
```

- `C31-1 unindexed-file` (15): `round-57-verifier-spotcheck.md`,
  `round-58-verifier-spotcheck.md`, `round-58.md`, `round-59-verifier-spotcheck.md`,
  `round-59.md`, `round-60-verifier-spotcheck.md`, `round-60.md`,
  `round-61-verifier-spotcheck.md`, `round-61.md`, `round-62-verifier-spotcheck.md`,
  `round-62.md`, `round-63-verifier-spotcheck.md`, `round-63.md`,
  `round-64-verifier-spotcheck.md`, `round-64.md`. These are **pre-existing**;
  `round-65.md` becomes the sixteenth unindexed file if this bump is not applied.
- `C34-3 shape-cell-drift`: the rows for `round-54.md`, `round-55.md`,
  `round-56.md`, `round-57.md` declare `contract` `4/4` while those files carry
  **0** column-0 contract lines (measured `0/4`). Pre-existing; the audit's own
  `C34c` re-derives the cell, so the declared values are false as filed.
- `C34-2 prose-arithmetic-drift`: the machine-read line `README.md:122`
  (`**Rows: 43. Files: 43.**`) against measured `[50, 65]`.
- Reader-visible drift the audit does **not** flag: `README.md:271` says "Of the
  42 index rows" (live 50), and §1's `ls corpus/lessons/*.md | wc -l # 37`
  annotation (live 65). Both are prose a reader will quote; neither is
  machine-read.

### B.3 The exact new §2 row

Append **one** row directly after `README.md:120` (the last table row, which is
`round-57.md`), before the blank line and `**Rows: 43. Files: 43.**`:

```
| `corpus/lessons/round-65.md` | gate-keeper | 4/4 | none (no Q ids) | `reports/round-65/claims.json` | bytes=<N> lines=<N> sha8=<8 hex> |
```

Cell rules — each is re-derived by the audit, so a wrong cell is a new finding:

- **format `gate-keeper`** — correct iff the landed file carries a `## Gate`
  section (`classify()` in `c31-lessons-index-audit.py:72`); Part A above does.
- **contract `4/4`** — correct **only if all four column-0 lines survive
  landing**: `source:`, `verified-at:`, `recheck:`, `scope:`. The model,
  `corpus/lessons/round-64.md`, carries none, so a lesson copied from it must be
  filed with `0/4` instead; do not copy the stale `4/4` that rows 114-120 carry
  over files that measure `0/4`. Part A carries all four deliberately, which
  makes `4/4` the honest cell and keeps `C34c` green for this row.
- **open-questions `none (no Q ids)`** — the round's open items, if any, are
  routed ids (R1-R7 class) and would become §4 rows; if a §4 row is added, this
  cell and the §4 tables change together (re-run `C32`).
- **disposition pointer `` `reports/round-65/claims.json` ``** — matches rows
  106-120's pattern (the round's declaration surface, not a verdict).
- **pin `bytes=<N> lines=<N> sha8=<8 hex>`** — measured **after** the file
  lands, never from this skeleton: `python3 -B
  reports/round-25/audit/c31-lessons-index-audit.py --json` emits the live
  cells; `sha8` is `sha256(bytes)[:8]`. `C34` re-derives all three, so a pin
  written from a draft is a finding.

### B.4 The machine-read count line

`README.md:122` is read by `C34b` (`re.finditer(r"\*\*Rows:\s*(\d+)\.\s*Files:\s*(\d+)\.\*\*")`,
`c31-lessons-index-audit.py:298-315`) and **cannot** be superseded by an appended
restatement. Revision 13 left it as filed; revision 14 must correct it in place
to the post-landing measurement — `**Rows: 51. Files: 66.**` if only the
round-65 row is added (50 + 1, 65 + 1). If the integrator also back-fills the 15
pre-existing unindexed files, the count moves to `66 / 66`; the stated pair must
equal the measured pair either way. With only the round-65 row, `C31-1` still
fails on the 15 older files and the audit stays at exit 1 — state that in the
revision block rather than implying green.

### B.5 The revision-14 block text (append at the foot, after `## Revision 13`)

```
## Revision 14 — round-65 lesson row (2026-10-24)

Adds one §2 row, for `round-65.md`, pinned from the live bytes with
`reports/round-25/audit/c31-lessons-index-audit.py --json` after the lesson
landed; the §2 count line is corrected in place to `**Rows: 51. Files: 66.**`.
The lesson carries the four contract lines at column 0, so its `contract` cell
is `4/4` (measured, not inherited from the rows above it).

This revision does not repair the pre-existing drift it lands on top of: fifteen
lesson files of rounds 57-64 remain unindexed (`C31-1`), the `round-54`-`round-57`
rows declare `contract` `4/4` against files that measure `0/4` (`C34-3`), and
`README.md:271` still reads "42 index rows" (measured 50). The audit therefore
exits 1 with those findings at this stamp. Back-filling them is a separate
revision with its own pins, or a named disposition; this block must not be read
as an index that is green.

Superseding edits land as a new revision block here, never as an in-place
rewrite of the per-round rows' provenance claims.
```

### B.6 Ownership and write-scope notes the L1 must resolve

- `corpus/lessons/README.md` is **not** in any of the three claims' `lands` in
  `reports/round-65/claims.json` (C: entry, `corpus/SOURCES.md`,
  `corpus/README.md`; O: three counters, `tools/check-row-fragments.py`, the
  exactness receipt; Ca: the eight paths printed by `claims.json`). The bump is
  a records edit that no claim delivers. Either the L1 lands it as a records
  edit with its own revision block and says so in the round-65 LOG entry, or it
  names the omission — silence leaves the index one row further behind.
- The file's own rule is binding: filed lesson bytes are read-only and a
  correction lands as a new file or a new dated block. Nothing in this bump
  edits any `corpus/lessons/round-*.md` byte; the only in-place edit is the
  machine-read count line at `:122`, which revision 13 itself shows cannot be
  superseded by an appendix.
- `corpus/README.md` (claim C's land: entries 238 -> 239, culture-material
  31 -> 32) is a **different file** from `corpus/lessons/README.md`. Do not let
  one edit stand for the other.
- Ca's statement requires corrections in `LOG.md` and `SCORECARD.md` (R1
  repeats, R3 citation, R5 binding) and its R1/R3/R5 legs read both files, but
  neither file is in Ca's `lands` list; the integrator should treat that as a
  declaration gap and record which edit landed where.
