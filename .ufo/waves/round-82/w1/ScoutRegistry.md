# ScoutRegistry — registry grammar census for claim O (round 82, w1)

**Verdict:** the base registry is grammatically clean and the parser's job is small, but *the
base data alone cannot falsify a wrong implementation*. 827 rows, all 11 cells, all cadences
valid, zero indented rows, zero malformed rows, zero duplicate ids — so the error path, the
indentation tolerance and both date boundaries are unreachable from lane data. Their proof
must be synthetic, in `--selftest`. The two counts that are reachable are pinned below and
agree with the fleet's own `overdue` mode row for row.

All facts are read at base `c285b2afb19d4b64320e18df1f55e426bf2d0b0c`; the lane working tree
is byte-identical to it (`sha256sum corpus/SOURCES.md` = `2f60171c…108263` = `git show
<base>:corpus/SOURCES.md | sha256sum`).

## 1. Row census

- **827 rows** match `^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|` — `grep -cE` on the base blob.
- **827 rows** match the same pattern at column 0 — `grep -cE '^\|…'`; therefore **0 rows**
  carry any leading whitespace — `grep -cE '^[[:space:]]+\|…'` (exit 1, no match).
- Rows occupy lines 30–859 of 960; `## Registry` heading at line 26, header row 28, separator
  29. Only lines 28–29 outside the row band start with `|`, so fleet E12 cannot fire.
- File has 0 tabs, 0 CRLF lines, 0 trailing-space lines — `grep -cP '\t'`, `grep -c $'\r'`,
  `grep -cE ' +$'`.

## 2. Column census

- Cell-count distribution `{11: 827}`; **0 rows** with ≠ 11 cells, so the contract's
  malformed-row → exit 2 path is never exercised by real data.
- `opened`: 10 distinct values, all real ISO dates (each parsed by
  `datetime.date.fromisoformat`), range **2026-10-19 … 2026-11-01**; histogram 47 / 23 / 395 /
  210 / 108 / 25 / 12 / 1 / 3 / 3 for 10-19, 10-21, 10-22, 10-23, 10-24, 10-25, 10-27, 10-30,
  10-31, 11-01.
- `recheck`: 6 distinct values, all legal — `90d` 18, `180d` 249, `365d` 392, `2027-10-22` 42,
  `2027-10-23` 112, `on-release` 14. Sum 827. **0 rows** whose `opened` is not ISO and **0**
  whose `recheck` is not `NNd`/ISO/`on-release`.
- Consequence for the tool: `NNd` 659 + ISO 154 + `on-release` 14.

## 3. Duplicate traps

- **No duplicate ids**: 827 rows, 827 distinct ids — `python3 duprec.py`.
- Ids span S001–S903 with **76 holes** inside the span (S455–S474 among them). An
  implementation that derives `rows` from `max(id) − min(id) + 1` prints 903 — wrong. `rows`
  must be the parsed-row count.
- URL duplicates: **43** normalized groups, of which **28** are cross-scope (= the W04
  warnings) and **15** are same-scope supersede/correction pairs (S029→S047, S034→S044,
  S038→S045, S039→S046, …). 15 + 28 = 43 exactly. Round-start fleet census:
  `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root
  /home/vgpnk/Projects/shokunin kotodama` → exit **0**, **28** `W04` lines, **4** `W01`
  lines, final line `kotodama\tok\t/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md`
  (`awk -F'\t' '{print $2}' | sort | uniq -c` → `1 ok`, `4 W01`, `28 W04`).
- The auditor must **not** dedupe by URL or filter by status: 37 rejected and 58 queued rows
  carry cadences too, and 25 of the rejects are `365d`.

## 4. Date boundaries (the numbers the tool must reproduce)

| as-of (window 90) | due | upcoming | on-release | rows |
|---|---|---|---|---|
| 2026-10-19 | 0 | 7 | 14 | 827 |
| **2026-11-04** | **0** | **18** | **14** | **827** |
| 2027-01-16 | 0 | 18 | 14 | 827 |
| 2027-01-17 | 7 | 18 | 14 | 827 |
| 2027-02-02 | 18 | 249 | 14 | 827 |
| 2027-02-03 | 18 | 249 | 14 | 827 |
| 2027-10-24 | 813 | 0 | 14 | 827 |
| **2027-11-01** | **813** | **0** | **14** | **827** |

Computed by `boundary.py` on the base blob. **Rows due exactly on 2026-11-04: 0. Rows due
exactly on 2027-11-01: 0.** So:

```text
$ python3 tools/check-sources-recheck.py --as-of 2026-11-04
RECHECK-QUEUE: 0 due / 18 upcoming / 14 on-release / 827 rows
```

(one line, zero `DUE` lines), and at 2027-11-01 `RECHECK-QUEUE: 813 due / 0 upcoming / 14
on-release / 827 rows` plus 813 `DUE` lines.

**Independent confirmation:** `sources-census.sh overdue --root … kotodama --today 2027-11-01`
reports the same 813 rows as overdue (exit 1); its id set is 154 ISO-dated + 659 `NNd` past
due, and the only ids it never judges are the 14 `on-release` rows — `comm -23/-13/-12` on the
sorted id lists give 154 / 14 / 659. At `--today 2026-11-04` it reports 0 overdue (exit 0).
Two implementations, same numbers.

## 5. What the base data cannot falsify (and therefore what `--selftest` must build)

1. Indented rows: 0 exist. Test 0/1/2/3 spaces parse; decide and pin the 4-space case.
2. Malformed row (exit 2, `RECHECK-ERROR <detail>`, no traceback): 0 exist.
3. Unparseable cadence (exit 2): 0 exist.
4. `due_date == as-of` counts as due: only reachable at as-of 2027-01-17 (7 rows); a strict
   `<` prints due=0 there — verified.
5. `due_date == as-of + window` counts as upcoming: unreachable — nearest in-window due date
   is 10 days inside the edge (2027-01-23 vs edge 2027-02-02); as-of 2027-02-02 and
   2027-02-03 print identical `18 / 249`.
6. `on-release` exemption for a long-past `opened`: the 14 real `on-release` rows are all
   recent.
7. Past-dated ISO cadence: all 154 ISO rows are future-dated 2027-10-22/23.
8. Calendar arithmetic / leap years: 2026-10-19 + 90 = 2027-01-17 is the only real
   year-crossing case; no leap case is reachable.
9. Empty registry and `--window 0`: not representable by lane data.

**Sum warning:** at 2026-11-04, `0 + 18 + 14 = 32 ≠ 827`. That is correct per contract
(`rows` is the parsed-row count, not the sum of the buckets). A "fix" that adds a fourth
bucket or redefines `upcoming` as "not due" breaks the contract; pin one such case in
`--selftest`.

**Open decisions the contract does not settle** (the implementer must pick and document):
line order (contract sentence implies summary first, then `DUE` lines); `DUE` line order
(file order is the deterministic default); `--as-of` default (UTC today — the fleet census's
own selftest asserts `UTC-date-in-Sao-Paulo`); `--registry` relative to cwd, which breaks if
run from `tools/`; and exit code for a clean-but-overdue run (must be 0 — only malformed
input is 2, unlike the fleet census's exit 1).

## 6. Post-round delta for the freeze

S904–S907 opened 2026-11-04 land due 2027-02-02 / 2027-05-03 / 2027-11-04 at 90d/180d/365d.
A 90d row lands on the window edge, which is *upcoming*, so **no new row can raise `due`**.
The post-round run at as-of 2026-11-04 must read `RECHECK-QUEUE: 0 due / <18 or 18+N>
upcoming / <14 or 14+M> on-release / 831 rows` (N = new rows with cadence ≤ 90d, M = new
`on-release` rows). `rows ≠ 831` or `due > 0` means the parser dropped, duplicated or
mis-dated a row — the cheapest end-to-end gate available at the freeze.

## 7. Files written

- `.ufo/waves/round-82/w1/ScoutRegistry.md` (this report) —
  `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/ScoutRegistry.md`
- `.ufo/waves/round-82/w1/stage/ScoutRegistry/registry-census.md` — full census with every
  command and its raw output, sections 0–9 (plus 5.1, 6.1) —
  `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/stage/ScoutRegistry/registry-census.md`
- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/stage/ScoutRegistry/`
  also holds `census.py`, `dates.py`, `boundary.py`, `duprec.py`, `compose.py`, the blob
  digest `SOURCES.base.sha256.txt`, and `raw/01`–`raw/18` transcripts.

## 8. Not run / limits

- No network fetch: this seat reads only the lane's base blob and the fleet census script.
- No write under the lane's tracked paths, no git/jj mutation; `git show`, `git rev-parse`,
  `git status` only. Fleet repo untouched.
- I did not run `sources-census.sh selftest`, `census`, `shared`, or the fleet-wide sweep: out
  of scope, and the fleet census is read-only by contract.
- No tool was installed; nothing to record.
