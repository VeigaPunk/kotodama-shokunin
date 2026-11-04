import pathlib
R=pathlib.Path('raw')
def raw(n):
    return R.joinpath(n).read_text(encoding='utf-8').rstrip('\n')
def block(n, lang='text'):
    return "```%s\n%s\n```" % (lang, raw(n))

doc = f"""# Registry grammar census — kotodama base c285b2a (round 82, w1)

Seat: **ScoutRegistry**. Date: 2026-11-04. Scope: the grammar that claim O's
`tools/check-sources-recheck.py` must parse at the round base. Read-only; nothing under the
lane or the fleet root was written.

## 0. Provenance

The census runs on the base blob, extracted once to scratch and never edited:

{block('01_base_blob.txt')}

{block('02_blob_sha.txt')}

{block('03_head.txt')}

The lane's working tree is byte-identical to the base blob (so a round-start run against
`corpus/SOURCES.md` and a run against the base blob are the same input):

{block('04_worktree_sha.txt')}

Extraction command used for every later probe:

```text
$ git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin show c285b2afb19d4b64320e18df1f55e426bf2d0b0c:corpus/SOURCES.md > SOURCES.base.md
$ sha256sum SOURCES.base.md
2f60171c8879f99e690f15403985c240a0b80def31b003e4862272b92f108263  SOURCES.base.md
```

## 1. Row census

Rows matching the contract pattern `^\\s{{0,3}}\\|\\s*S\\d{{3,}}\\s*\\|` ({block('05_rows.txt').splitlines()[1]} rows), all of them at column 0:

{block('05_rows.txt')}

{block('06_rows_col0.txt')}

{block('07_rows_indented.txt')}

**Reading.** 827 rows match at 0–3 leading spaces; 827 match at column 0 exactly; **0 rows
carry any leading whitespace**. The indentation tolerance the contract requires (0–3 spaces)
is therefore *unexercised by real lane data* — see §7. `grep -c` exiting 1 on the zero-match
indented sweep is expected (no match, not an error).

Row band: lines 30–859 of the 960-line file, i.e. the `## Registry` section (heading line 26,
header row line 28, separator line 29):

{block('08_sections.txt')}

Only lines 28 and 29 outside the row band begin with `|`, so the fleet checker's E12
(row-shaped source outside `## Registry`) cannot fire on this file:

```text
$ grep -nE '^ {{0,3}}\\|' SOURCES.base.md | grep -vE '\\|[[:space:]]*S[0-9]{{3,}}[[:space:]]*\\|' | head -10
28:| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
29:|---|---|---|---|---|---|---|---|---|---|---|
```

File hygiene (a parser need not handle tabs or CRLF here):

{block('09_hygiene.txt')}

## 2. Column census

One-off parser (`census.py`, reproduced in this stage directory): split the row body on `|`,
strip each cell, count.

{block('10_cell_census.txt')}

**Cell count.** Distribution is `{{11: 827}}` — every single row has exactly 11 cells, none
has 12, none has 10. No row is malformed at base, so claim O's *error path* (exit 2,
`RECHECK-ERROR <detail>`, no traceback) is never triggered by real lane data: it can only be
proven by `--selftest` or by a synthetic registry.

**`opened` column.** 10 distinct values, every one a real ISO date (each parsed by
`datetime.date.fromisoformat`, which rejects impossible days like 2026-02-30):

| opened | rows |
|---|---|
| 2026-10-19 | 47 |
| 2026-10-21 | 23 |
| 2026-10-22 | 395 |
| 2026-10-23 | 210 |
| 2026-10-24 | 108 |
| 2026-10-25 | 25 |
| 2026-10-27 | 12 |
| 2026-10-30 | 1 |
| 2026-10-31 | 3 |
| 2026-11-01 | 3 |

**`recheck` column.** 6 distinct values, all inside the contract's three forms
(`NNd` → opened+N days, ISO date → itself, `on-release` → exempt):

| recheck | form | rows |
|---|---|---|
| 90d | opened+90 | 18 |
| 180d | opened+180 | 249 |
| 365d | opened+365 | 392 |
| 2027-10-22 | ISO | 42 |
| 2027-10-23 | ISO | 112 |
| on-release | exempt | 14 |

`NNd` (659) + ISO (154) + `on-release` (14) = 827. Rows whose `opened` is not ISO: **none**.
Rows whose `recheck` is not `NNd`/ISO/`on-release`: **none**.

Status histogram (irrelevant to the queue but useful when reading a diff): mined 732,
queued 58, rejected 37.

## 3. Duplicate-id and duplicate-URL traps

**Duplicate ids: none.** 827 rows carry 827 distinct ids. Ids span S001–S903, and 76 numbers
in that span are unused (S455–S474 among others) — the registry has holes, so an
implementation that assumes contiguous ids or derives `rows` from `max(id) - min(id) + 1`
reports 903 instead of 827. `rows` must be the parsed-row count.

{block('12_dups.txt')}

**URL duplicates are 43 groups, and only 28 of them are W04.** The fleet census flags a
duplicate only when the row's `scope` also differs; the other 15 groups are the lane's
deliberate `supersedes` / correction pairs (same URL, same scope, e.g. S029→S047, S034→S044,
S038→S045, S039→S046). 15 + 28 = 43, which reconciles exactly with the census count below.
For claim O this matters only as a non-goal: the recheck auditor must not dedupe or collapse
rows by URL, or it would drop 15 rows from `rows` and from the cadence computation.

## 4. Round-start fleet census (as instructed)

{block('13_census_validate.txt')}

Exit status and the code histogram of that output:

{block('14_validate_codes.txt')}

Tail (last three lines of the same run):

```text
kotodama	W01	S884 tierC mined used-by=corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-23.md
kotodama	W01	S893 tierC mined used-by=corpus/knowledge/myth-symbol/narrative-structure-frameworks.md
kotodama	ok	/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md
```

**Answer to the question asked: 28 W04 duplicate-URL warnings for this lane, exit 0, final
line `ok`.** The 4 W01 lines are pre-existing tier-C-mined notes, not this round's business.

## 5. Date boundaries

{block('11_dates.txt')}

{block('17_boundary.txt')}

**Earliest / latest `opened`:** 2026-10-19 / 2026-11-01.

**Rows due exactly on the two probe dates: 0 and 0.** No row lands on 2026-11-04 and none on
2027-11-01, so neither date can distinguish `<=` from `<` at the *as-of* edge by itself. The
date that does exercise `due_date <= as-of` in real data is **2027-01-17**: 7 rows fall due
exactly there, and an as-of 2027-01-17 run must count them as **due=7** (a `<` implementation
prints due=0 — see the strict-`<` line in the probe above).

**Window edge is not exercised either.** At as-of 2026-11-04 the window closes on 2027-02-02;
the latest in-window due date is 2027-01-23, **10 days inside the edge**. As-of 2027-02-02 and
2027-02-03 both print `18 / 249`, identical, because no row falls due on either date. So the
inclusive upper bound (`due_date <= as-of + window`) cannot be proven from lane data; it must
be built synthetically in `--selftest`.

## 6. Target output for the new tool at this base

With the contract's own semantics (`due = due_date <= as-of`; `upcoming = as-of < due_date <=
as-of + window`; `on-release` exempt; `rows = rows parsed`), the base registry must produce,
verbatim:

```text
$ python3 tools/check-sources-recheck.py --as-of 2026-11-04
RECHECK-QUEUE: 0 due / 18 upcoming / 14 on-release / 827 rows
```

— one line, no `DUE` lines (there are zero due rows), and

```text
$ python3 tools/check-sources-recheck.py --as-of 2027-11-01
RECHECK-QUEUE: 813 due / 0 upcoming / 14 on-release / 827 rows
DUE S009 2027-01-17
DUE S012 2027-01-17
... (813 DUE lines total)
```

The 18 upcoming rows at 2026-11-04, for a spot check:

```text
DUE-DATE 2027-01-17: S009 S012 S020 S021 S031 S032 S033   (7)
DUE-DATE 2027-01-20: S084 S104 S105 S106 S107 S142 S157 S163  (8)
DUE-DATE 2027-01-22: S859                               (1)
DUE-DATE 2027-01-23: S860 S875                           (2)
```

**The three buckets do not sum to `rows` at 2026-11-04** (0 + 18 + 14 = 32, not 827): the
remaining 795 rows are past the window and belong to no bucket. That is the contract as
written — `rows` is the parsed-row count, not the sum. An implementer who "fixes" the
arithmetic by adding a fourth "later" bucket, or by making `upcoming` mean "everything not
due", breaks the contract. The selftest should pin one case where
`due + upcoming + on-release < rows` so the distinction survives refactors.

## 7. What real data does NOT exercise (mandatory selftest coverage)

Derived from the numbers above; every item is a check the `--selftest` (≥ 8 checks, printing
`SELFTEST: PASS (<n> checks)`) must build synthetically, because the 827 real rows cannot
distinguish a correct implementation from a wrong one:

1. **Indented rows.** Zero rows carry leading whitespace. Must test 0, 1, 2, 3 spaces parse
   and (per the fleet parser's documented rule, "4 or more spaces are indented code and
   ignored") that 4 spaces does not. The contract text only promises 0–3; the 4-space case is
   a decision the tool must make and the report should record.
2. **Malformed row → exit 2.** No real row has ≠ 11 cells. Must test one 10-cell and one
   12-cell row, asserting exit 2, stdout `RECHECK-ERROR <detail>`, and *no traceback* (empty
   stderr, or at minimum no `Traceback (most recent call last)`).
3. **Unparseable cadence → exit 2.** Every real value is valid. Must test e.g. `90 days`,
   `90D`, `2027-13-01`, `never`, `""`.
4. **`due_date == as-of` counts as due.** Real data can test it only at as-of 2027-01-17
   (7 rows); the selftest should assert it on a 1-row fixture so the boundary is explicit.
5. **`due_date == as-of + window` counts as upcoming (inclusive).** No real row is within 10
   days of the edge.
6. **`on-release` never enters due/upcoming**, even when `opened` is far in the past (the 14
   real rows are all recent; a 2020-opened `on-release` row would be the sharp case).
7. **ISO recheck in the past** (e.g. `2020-01-01` with `opened 2019-01-01`) is due at once —
   no real row has an ISO recheck earlier than its opened date plus cadence; all 154 ISO rows
   are future-dated 2027-10-22/23.
8. **Month/leap-year arithmetic.** `opened + NNd` must be calendar arithmetic on real dates,
   not 30-day months: 2026-10-19 + 90 = 2027-01-17 (crosses the year boundary and the short
   months); a leap case (e.g. 2027-12-01 + 90 = 2028-02-29) is unobtainable from lane data.
9. **Empty registry / no rows**: real file always has 827; the tool must decide and pin
   whether `0 due / 0 upcoming / 0 on-release / 0 rows` exits 0 or 2.
10. **`--window 0`**: nothing is upcoming by definition; pin it.

## 8. Post-round delta the L1 can use at the freeze

If claim D appends S904–S906 (and S907 as a `rejected` row, matching how S028/S043/S047 are
kept), the registry becomes 831 rows. All four are opened 2026-11-04, so with a 90d/180d/365d
cadence their due dates are 2027-02-02 / 2027-05-03 / 2027-11-04 — every one of them strictly
after the 2026-11-04 window edge (2027-02-02 is the edge itself only for a 90d cadence, and
`due_date == as-of + window` is upcoming, not due). Therefore the post-round run at as-of
2026-11-04 must still print:

```text
RECHECK-QUEUE: 0 due / <18 or 18+N> upcoming / <14 or 14+M> on-release / 831 rows
```

where N is the number of new rows given a cadence ≤ 90d (a 90d row lands exactly on the window
edge and is *upcoming*, so N counts it) and M the number of new rows marked `on-release`. Any
other shape — especially `due > 0`, or `rows` ≠ 831 — means the parser dropped, duplicated or
mis-dated a row. This is the cheapest end-to-end check available at the freeze.

## 9. Reproduction

Scripts used (copied into this stage directory, dependency-free Python 3, no network):
`census.py` (§2), `dates.py` (§5), `boundary.py` (§5), `duprec.py` (§3). Raw transcripts in
`raw/` (`01`–`17`). Scratch dir `/fast/scratch/hyaku/kotodama-r82/ScoutRegistry/` is removed
after the stage copy; the base blob is recoverable at any time with the `git show` in §0.
"""
out = pathlib.Path('/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/stage/ScoutRegistry/registry-census.md')
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(doc, encoding='utf-8')
print(out, out.stat().st_size, "bytes")
