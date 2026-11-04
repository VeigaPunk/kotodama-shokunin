# SentinelGrammar adversarial probe — Kotodama r82 (hyaku run 15), milestone r82-v1

Hypothesis H (falsifiable): every `recheck` cell in corpus/SOURCES.md at lane base
revision c285b2afb19d4b64320e18df1f55e426bf2d0b0c is machine-parseable under the
declared grammar (on-release | NNd | ISO date), and every `opened` cell is an ISO
date. Tested with an independent parser written for this probe (below), NOT the
round's tool (tools/check-sources-recheck.py does not exist at the base rev).

## Input receipt

- bytes=991457 sha256=2f60171c8879f99e690f15403985c240a0b80def31b003e4862272b92f108263 lines=960
- fetch: git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin show c285b2afb19d4b64320e18df1f55e426bf2d0b0c:corpus/SOURCES.md
- base commit subject: c285b2afb19d4b64320e18df1f55e426bf2d0b0c 2026-11-01 17:44:19 +0000 "round-81 verifier spot-check (integrator, hyaku): non-author admit/reject"
- runtime: Python 3.14.8 (python3 --version)
- no tools were installed for this seat.

## Commands

```
TMPDIR=/fast/scratch/hyaku/kotodama-r82/SentinelGrammar/tmp python3 /fast/scratch/hyaku/kotodama-r82/SentinelGrammar/probe_parser.py --registry /fast/scratch/hyaku/kotodama-r82/SentinelGrammar/SOURCES.base.md --as-of 2026-11-04 --window 90
TMPDIR=/fast/scratch/hyaku/kotodama-r82/SentinelGrammar/tmp python3 /fast/scratch/hyaku/kotodama-r82/SentinelGrammar/probe_parser.py --registry /fast/scratch/hyaku/kotodama-r82/SentinelGrammar/SOURCES.base.md --as-of 2027-11-01 --window 90
```

## Findings (summary; full raw output below)

1. H HOLDS at the base rev: parse-failure list EMPTY over 827 data rows (raw
   output: == PARSE FAILURES (0) ==). Every recheck cell parses (forms: Nd 659,
   ISO 154, on-release 14; distinct values exactly {90d: 18, 180d: 249, 365d: 392,
   on-release: 14, 2027-10-22: 42, 2027-10-23: 112}); every opened cell is a valid
   ISO date (10 distinct, 2026-10-19 .. 2026-11-01). Cross-checked by independent
   grep counts (below), which agree exactly.
2. OPERABILITY TRAP (independent of H, found by this probe): the registry table is
   NOT contiguous. Three blank lines (inside line spans 704/706, 786/788, 852/854)
   split it into 4 blocks (30-704, 706-786, 788-852, 854-859). A row-walk that
   stops at the first non-pipe line silently sees 675 of 827 rows — this probe's
   first (buggy) run did exactly that and printed rows=675 / upcoming=15 before
   being fixed to scan the whole file. tools/check-sources-recheck.py MUST scan
   all pipe-starting lines of the file (or tolerate blank lines inside the table).
3. Queue at as-of 2026-11-04 window 90 (expected tool line):
   RECHECK-QUEUE: 0 due / 18 upcoming / 14 on-release / 827 rows  (horizon 2027-02-02)
4. Queue at as-of 2027-11-01 window 90 (expected tool line):
   RECHECK-QUEUE: 813 due / 0 upcoming / 14 on-release / 827 rows  (horizon 2028-01-30)
   (827 - 14 on-release = 813; every Nd/ISO due date maxes at 2027-10-24, so all
   are due; the tool will print 813 DUE lines — volume is per contract.)
5. Degenerate cases: NONE exist in real data (0d: 0 rows; N>=3650d: 0 rows — Nd
   cadences are exactly {90, 180, 365}; ISO recheck earlier than opened: 0 of 154).
   Honest answers, no invented rule: the contract text already determines all
   three deterministically (0d -> due = opened -> due at any as-of >= opened;
   3650d -> due far outside window, counts only as a row; ISO < opened -> due from
   the start). They are simply untested by real data; fixtures are optional.
6. Leading spaces: all 829 pipe-starting lines have exactly 0 leading spaces
   (histogram {0: 829}); zero rows with 1-3, zero with >3, zero with leading TAB.
   The census-grammar branch that tolerates 1-3 leading spaces is UNTESTED by real
   data. Fixture recommendation: --selftest should include a registry whose row is
   indented by 2 spaces and must parse identically to a flush-left row (and,
   recommended, a 4-space-indented row which CommonMark would make a code block
   and the tool must NOT parse).
7. rows semantics: rows = 827 counts ALL data rows, including the 37 status
   rejected rows — the contract says rows = rows parsed and does not exclude
   rejected rows; this count includes them. (status histogram: mined 732,
   queued 58, rejected 37.)
8. Consistency observation (not a parse defect): rows opened 2026-10-22/23 carry
   the same one-year intent in two spellings — 154 rows use absolute ISO
   (2027-10-22 x42, 2027-10-23 x112) while 365d rows from the same cohorts spell
   it as a cadence. Grammar handles both; no action required from the tool.
9. IDs: 827 distinct ids, all matching ^S[0-9]{3}$, no duplicates.

## Independent grep cross-checks (mechanism different from the parser)

```
on-release: 14     — grep -c "| on-release |" SOURCES.base.md
90d: 18            — grep -c "| 90d |" SOURCES.base.md
180d: 249          — grep -c "| 180d |" SOURCES.base.md
365d: 392          — grep -c "| 365d |" SOURCES.base.md
ISO recheck: 154   — grep -cE "\| 2027-10-2[23] \|" SOURCES.base.md
opened 2026-10-19: 47 — grep -cE "\| 2026-10-19 \| (on-release|[0-9]+d|2027-)" SOURCES.base.md
opened 2026-11-01: 3  — grep -cE "\| 2026-11-01 \| (on-release|[0-9]+d|2027-)" SOURCES.base.md
pipe-starting lines: 829 — grep -c "^|" SOURCES.base.md
```
Case-variant sweep (On-Release / ON-RELEASE / on_release) is covered by the parser
itself: the exact-value recheck histogram has exactly 6 distinct values and
parse failures are 0, so no other spelling exists.

## Parser (inline, verbatim; sha256 15c52faff7b0a26f6ae34158613715437c7113f1edb3f3b03d42ad238810d93e)

```python
#!/usr/bin/env python3
"""SentinelGrammar adversarial probe — Kotodama round 82, hyaku run 15.

Hypothesis H (falsifiable): every `recheck` cell in corpus/SOURCES.md at lane
base revision c285b2afb19d4b64320e18df1f55e426bf2d0b0c is machine-parseable
under the declared grammar (on-release | NNd | ISO-8601 calendar date), and
every `opened` cell is an ISO date.

This is an INDEPENDENT parser written for the probe; it is not the round's
tool. Input is the materialized blob (sha256 recorded at fetch time).

Exit status: 0 iff zero parse failures; 2 iff any parse failure.
"""
import argparse
import datetime as dt
import hashlib
import re
import sys
from collections import Counter

ISO_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
NND_RE = re.compile(r"^\d+d$")
SEP_RE = re.compile(r"^:?-{3,}:?$")
ID_RE = re.compile(r"^S\d{3}$")


def parse_iso(s):
    """Return dt.date iff s is a valid ISO YYYY-MM-DD calendar date."""
    if not ISO_RE.match(s):
        return None
    try:
        return dt.date.fromisoformat(s)
    except ValueError:
        return None


def split_row(raw):
    """Split a table line. Returns (leading_spaces, cells, note)."""
    stripped_trailing = raw.rstrip("\n")
    stripped = stripped_trailing.rstrip(" ").rstrip("\t")
    lead = len(stripped) - len(stripped.lstrip(" \t"))
    body = stripped.strip(" \t")
    if not body.startswith("|") or not body.endswith("|"):
        return lead, None, "line does not both start and end with '|'"
    if "\\|" in body:
        return lead, None, "contains escaped pipe \\| (not handled by naive split)"
    parts = body.split("|")
    inner = parts[1:-1]
    cells = [c.strip() for c in inner]
    return lead, cells, None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--registry", required=True)
    ap.add_argument("--as-of", default=None)
    ap.add_argument("--window", type=int, default=90)
    args = ap.parse_args()

    blob = open(args.registry, "rb").read()
    lines = blob.decode("utf-8").splitlines()

    print("== RECEIPT ==")
    print("file=%s" % args.registry)
    print("bytes=%d sha256=%s lines=%d" % (len(blob), hashlib.sha256(blob).hexdigest(), len(lines)))

    # ---- locate the registry header row ----
    header_idx = None
    header_cells = None
    for i, l in enumerate(lines, start=1):
        lead, cells, note = split_row(l)
        if cells and cells and cells[0] == "id" and "recheck" in cells and "opened" in cells:
            header_idx, header_cells = i, cells
            break
    if header_idx is None:
        print("FATAL: no header row containing id/opened/recheck found")
        return 2
    print("header line=%d cells=%s" % (header_idx, header_cells))
    col = {name: header_cells.index(name) for name in
           ("id", "source", "kind", "tier", "scope", "anchor", "teaches",
            "status", "opened", "recheck", "used-by")}
    ncols = len(header_cells)
    print("declared cell count=%d" % ncols)

    # ---- scan ALL pipe lines in the file (blank lines may split the table) ----
    sep_rows = 0
    header_rows = []
    data = []          # (lineno, lead, cells)
    malformed = []     # (lineno, lead, reason)
    table_leads = Counter()
    for i, l in enumerate(lines, start=1):
        if not l.lstrip(" \t").startswith("|"):
            continue
        lead, cells, note = split_row(l)
        table_leads[lead] += 1
        if note:
            malformed.append((i, lead, note))
            continue
        if cells[0] == "id":
            header_rows.append((i, cells))
            continue
        if len(cells) == ncols and all(SEP_RE.match(c) for c in cells):
            sep_rows += 1
            continue
        data.append((i, lead, cells))

    print("\n== TABLE SCAN ==")
    print("pipe-starting lines total=%d (grep -c '^|' cross-check)" % (len(header_rows) + sep_rows + len(data) + len(malformed)))
    print("header rows=%d at %s" % (len(header_rows), [i for i, _ in header_rows]))
    print("separator rows=%d" % sep_rows)
    print("data rows=%d — lines %d..%d" % (len(data), data[0][0] if data else -1, data[-1][0] if data else -1))
    blocks = []
    for (i, _, _) in data:
        if blocks and i == blocks[-1][1] + 1:
            blocks[-1][1] = i
        else:
            blocks.append([i, i])
    print("contiguous table blocks: %s" % ["%d-%d" % (a, b) for a, b in blocks])
    gaps = [(blocks[k][1], blocks[k + 1][0]) for k in range(len(blocks) - 1)]
    print("block gaps (end line, next start line): %s" % gaps)
    print("malformed pipe lines=%d" % len(malformed))
    for i, lead, note in malformed:
        print("  line %d lead=%d: %s" % (i, lead, note))
    print("leading-space histogram over ALL table lines (header excluded): %s" % dict(sorted(table_leads.items())))
    tab_lead = [i for (i, lead, _) in data if "\t" in lines[i - 1][: lead + 1]]
    lead_gt3 = [(i, lead) for (i, lead, _) in data if lead > 3]
    lead_1_3 = [(i, lead) for (i, lead, _) in data if 1 <= lead <= 3]
    lead_0 = [(i, lead) for (i, lead, _) in data if lead == 0]
    print("data rows with 0 leading spaces=%d" % len(lead_0))
    print("data rows with 1-3 leading spaces=%d%s" % (len(lead_1_3), (" " + str(lead_1_3[:10])) if lead_1_3 else ""))
    print("data rows with >3 leading spaces=%d%s" % (len(lead_gt3), (" " + str(lead_gt3[:10])) if lead_gt3 else ""))
    print("data rows with leading TAB=%d" % len(tab_lead))

    cellcount = Counter(len(c) for _, _, c in data)
    print("cell-count histogram: %s" % dict(sorted(cellcount.items())))

    # ---- parse rows ----
    failures = []
    recheck_vals = Counter()
    recheck_form = Counter()
    recheck_N = Counter()
    recheck_iso = Counter()
    opened_vals = Counter()
    ids = Counter()
    status_vals = Counter()
    rows = []  # dicts
    for lineno, lead, cells in data:
        why = []
        if len(cells) != ncols:
            why.append("cell count %d != %d" % (len(cells), ncols))
        rid = cells[col["id"]] if len(cells) > col["id"] else "<missing>"
        op_s = cells[col["opened"]] if len(cells) > col["opened"] else "<missing>"
        rc_s = cells[col["recheck"]] if len(cells) > col["recheck"] else "<missing>"
        st_s = cells[col["status"]] if len(cells) > col["status"] else "<missing>"
        ids[rid] += 1
        status_vals[st_s] += 1
        opened = parse_iso(op_s)
        if opened is None:
            why.append("opened %r is not a valid ISO YYYY-MM-DD date" % op_s)
        if rc_s == "on-release":
            form = "on-release"
            due = None
        elif NND_RE.match(rc_s):
            form = "Nd"
            n = int(rc_s[:-1])
            recheck_N[n] += 1
            due = opened + dt.timedelta(days=n) if opened else None
        else:
            d = parse_iso(rc_s)
            if d is not None:
                form = "ISO"
                recheck_iso[rc_s] += 1
                due = d
            else:
                form = "UNPARSEABLE"
                why.append("recheck %r matches neither on-release, NNd nor ISO date" % rc_s)
        recheck_form[form] += 1
        recheck_vals[rc_s] += 1
        if why:
            failures.append((lineno, rid, why))
            continue
        opened_vals[op_s] += 1
        rows.append({"line": lineno, "id": rid, "opened": opened,
                     "recheck_raw": rc_s, "form": form, "due": due,
                     "status": st_s})

    print("\n== PARSE FAILURES (%d) ==" % len(failures))
    for lineno, rid, why in failures:
        print("line %d id=%s: %s" % (lineno, rid, "; ".join(why)))
    if not failures:
        print("(none)")

    print("\n== VALUE HISTOGRAM: recheck ==")
    print("forms: %s" % dict(sorted(recheck_form.items())))
    print("on-release rows=%d" % recheck_form.get("on-release", 0))
    print("distinct recheck values=%d" % len(recheck_vals))
    for v, n in sorted(recheck_vals.items()):
        print("  %-12s %d" % (repr(v), n))
    if recheck_N:
        ns = sorted(recheck_N)
        print("Nd cadences: N values %s; min=%d max=%d" % (ns, ns[0], ns[-1]))
    if recheck_iso:
        print("ISO recheck values: %s" % dict(sorted(recheck_iso.items())))

    print("\n== VALUE HISTOGRAM: opened ==")
    print("distinct opened values=%d" % len(opened_vals))
    for v, n in sorted(opened_vals.items()):
        print("  %s %d" % (v, n))
    if opened_vals:
        ds = sorted(dt.date.fromisoformat(v) for v in opened_vals)
        print("min opened=%s max opened=%s" % (ds[0], ds[-1]))
        byyear = Counter(d.year for d in ds for _ in range(opened_vals[d.isoformat()]))
        print("opened by year: %s" % dict(sorted(byyear.items())))

    print("\n== HISTOGRAM: status (context only) ==")
    print("%s" % dict(sorted(status_vals.items())))

    dup = {k: v for k, v in ids.items() if v > 1}
    bad = [k for k in ids if not ID_RE.match(k)]
    print("\n== ID SANITY ==")
    print("distinct ids=%d duplicates=%s non-conforming=%s" % (len(ids), dup or "none", bad or "none"))

    print("\n== DEGENERATE SCAN ==")
    z = [r for r in rows if r["form"] == "Nd" and int(r["recheck_raw"][:-1]) == 0]
    print("0d-cadence rows: %d%s" % (len(z), "".join(" [line %d %s opened=%s]" % (r["line"], r["id"], r["opened"]) for r in z)))
    big = [r for r in rows if r["form"] == "Nd" and int(r["recheck_raw"][:-1]) >= 3650]
    print("N>=3650d rows: %d%s" % (len(big), "".join(" [line %d %s %s opened=%s]" % (r["line"], r["id"], r["recheck_raw"], r["opened"]) for r in big)))
    inv = [r for r in rows if r["form"] == "ISO" and r["due"] < r["opened"]]
    print("ISO-recheck rows with recheck date BEFORE opened: %d%s" % (len(inv), "".join(" [line %d %s recheck=%s opened=%s]" % (r["line"], r["id"], r["recheck_raw"], r["opened"]) for r in inv)))

    if args.as_of:
        as_of = dt.date.fromisoformat(args.as_of)
        horizon = as_of + dt.timedelta(days=args.window)
        print("\n== QUEUE as-of %s window %d (horizon %s) ==" % (as_of, args.window, horizon))
        due_rows = sorted((r for r in rows if r["due"] is not None and r["due"] <= as_of),
                          key=lambda r: (r["due"], r["id"]))
        up_rows = sorted((r for r in rows if r["due"] is not None and as_of < r["due"] <= horizon),
                         key=lambda r: (r["due"], r["id"]))
        exempt = sum(1 for r in rows if r["form"] == "on-release")
        print("RECHECK-QUEUE: %d due / %d upcoming / %d on-release / %d rows" %
              (len(due_rows), len(up_rows), exempt, len(rows)))
        for r in due_rows:
            print("DUE %s %s" % (r["id"], r["due"].isoformat()))
        for r in up_rows:
            print("UPCOMING %s %s (recheck=%s)" % (r["id"], r["due"].isoformat(), r["recheck_raw"]))
        print("due+upcoming+exempt=%d, rows=%d, unclassified=%d" %
              (len(due_rows) + len(up_rows) + exempt, len(rows),
               len(rows) - len(due_rows) - len(up_rows) - exempt))

    return 2 if failures else 0


if __name__ == "__main__":
    sys.exit(main())

```

## Raw output — as-of 2026-11-04 window 90 (exit 0)

```
== RECEIPT ==
file=/fast/scratch/hyaku/kotodama-r82/SentinelGrammar/SOURCES.base.md
bytes=991457 sha256=2f60171c8879f99e690f15403985c240a0b80def31b003e4862272b92f108263 lines=960
header line=28 cells=['id', 'source', 'kind', 'tier', 'scope', 'anchor', 'teaches', 'status', 'opened', 'recheck', 'used-by']
declared cell count=11

== TABLE SCAN ==
pipe-starting lines total=829 (grep -c '^|' cross-check)
header rows=1 at [28]
separator rows=1
data rows=827 — lines 30..859
contiguous table blocks: ['30-704', '706-786', '788-852', '854-859']
block gaps (end line, next start line): [(704, 706), (786, 788), (852, 854)]
malformed pipe lines=0
leading-space histogram over ALL table lines (header excluded): {0: 829}
data rows with 0 leading spaces=827
data rows with 1-3 leading spaces=0
data rows with >3 leading spaces=0
data rows with leading TAB=0
cell-count histogram: {11: 827}

== PARSE FAILURES (0) ==
(none)

== VALUE HISTOGRAM: recheck ==
forms: {'ISO': 154, 'Nd': 659, 'on-release': 14}
on-release rows=14
distinct recheck values=6
  '180d'       249
  '2027-10-22' 42
  '2027-10-23' 112
  '365d'       392
  '90d'        18
  'on-release' 14
Nd cadences: N values [90, 180, 365]; min=90 max=365
ISO recheck values: {'2027-10-22': 42, '2027-10-23': 112}

== VALUE HISTOGRAM: opened ==
distinct opened values=10
  2026-10-19 47
  2026-10-21 23
  2026-10-22 395
  2026-10-23 210
  2026-10-24 108
  2026-10-25 25
  2026-10-27 12
  2026-10-30 1
  2026-10-31 3
  2026-11-01 3
min opened=2026-10-19 max opened=2026-11-01
opened by year: {2026: 827}

== HISTOGRAM: status (context only) ==
{'mined': 732, 'queued': 58, 'rejected': 37}

== ID SANITY ==
distinct ids=827 duplicates=none non-conforming=none

== DEGENERATE SCAN ==
0d-cadence rows: 0
N>=3650d rows: 0
ISO-recheck rows with recheck date BEFORE opened: 0

== QUEUE as-of 2026-11-04 window 90 (horizon 2027-02-02) ==
RECHECK-QUEUE: 0 due / 18 upcoming / 14 on-release / 827 rows
UPCOMING S009 2027-01-17 (recheck=90d)
UPCOMING S012 2027-01-17 (recheck=90d)
UPCOMING S020 2027-01-17 (recheck=90d)
UPCOMING S021 2027-01-17 (recheck=90d)
UPCOMING S031 2027-01-17 (recheck=90d)
UPCOMING S032 2027-01-17 (recheck=90d)
UPCOMING S033 2027-01-17 (recheck=90d)
UPCOMING S084 2027-01-20 (recheck=90d)
UPCOMING S104 2027-01-20 (recheck=90d)
UPCOMING S105 2027-01-20 (recheck=90d)
UPCOMING S106 2027-01-20 (recheck=90d)
UPCOMING S107 2027-01-20 (recheck=90d)
UPCOMING S142 2027-01-20 (recheck=90d)
UPCOMING S157 2027-01-20 (recheck=90d)
UPCOMING S163 2027-01-20 (recheck=90d)
UPCOMING S859 2027-01-22 (recheck=90d)
UPCOMING S860 2027-01-23 (recheck=90d)
UPCOMING S875 2027-01-23 (recheck=90d)
due+upcoming+exempt=32, rows=827, unclassified=795
```

## Raw output — as-of 2027-11-01 window 90 (exit 0; 813 DUE lines below)

```
== RECEIPT ==
file=/fast/scratch/hyaku/kotodama-r82/SentinelGrammar/SOURCES.base.md
bytes=991457 sha256=2f60171c8879f99e690f15403985c240a0b80def31b003e4862272b92f108263 lines=960
header line=28 cells=['id', 'source', 'kind', 'tier', 'scope', 'anchor', 'teaches', 'status', 'opened', 'recheck', 'used-by']
declared cell count=11

== TABLE SCAN ==
pipe-starting lines total=829 (grep -c '^|' cross-check)
header rows=1 at [28]
separator rows=1
data rows=827 — lines 30..859
contiguous table blocks: ['30-704', '706-786', '788-852', '854-859']
block gaps (end line, next start line): [(704, 706), (786, 788), (852, 854)]
malformed pipe lines=0
leading-space histogram over ALL table lines (header excluded): {0: 829}
data rows with 0 leading spaces=827
data rows with 1-3 leading spaces=0
data rows with >3 leading spaces=0
data rows with leading TAB=0
cell-count histogram: {11: 827}

== PARSE FAILURES (0) ==
(none)

== VALUE HISTOGRAM: recheck ==
forms: {'ISO': 154, 'Nd': 659, 'on-release': 14}
on-release rows=14
distinct recheck values=6
  '180d'       249
  '2027-10-22' 42
  '2027-10-23' 112
  '365d'       392
  '90d'        18
  'on-release' 14
Nd cadences: N values [90, 180, 365]; min=90 max=365
ISO recheck values: {'2027-10-22': 42, '2027-10-23': 112}

== VALUE HISTOGRAM: opened ==
distinct opened values=10
  2026-10-19 47
  2026-10-21 23
  2026-10-22 395
  2026-10-23 210
  2026-10-24 108
  2026-10-25 25
  2026-10-27 12
  2026-10-30 1
  2026-10-31 3
  2026-11-01 3
min opened=2026-10-19 max opened=2026-11-01
opened by year: {2026: 827}

== HISTOGRAM: status (context only) ==
{'mined': 732, 'queued': 58, 'rejected': 37}

== ID SANITY ==
distinct ids=827 duplicates=none non-conforming=none

== DEGENERATE SCAN ==
0d-cadence rows: 0
N>=3650d rows: 0
ISO-recheck rows with recheck date BEFORE opened: 0

== QUEUE as-of 2027-11-01 window 90 (horizon 2028-01-30) ==
RECHECK-QUEUE: 813 due / 0 upcoming / 14 on-release / 827 rows
DUE S009 2027-01-17
DUE S012 2027-01-17
DUE S020 2027-01-17
DUE S021 2027-01-17
DUE S031 2027-01-17
DUE S032 2027-01-17
DUE S033 2027-01-17
DUE S084 2027-01-20
DUE S104 2027-01-20
DUE S105 2027-01-20
DUE S106 2027-01-20
DUE S107 2027-01-20
DUE S142 2027-01-20
DUE S157 2027-01-20
DUE S163 2027-01-20
DUE S859 2027-01-22
DUE S860 2027-01-23
DUE S875 2027-01-23
DUE S005 2027-04-17
DUE S006 2027-04-17
DUE S017 2027-04-17
DUE S019 2027-04-17
DUE S025 2027-04-17
DUE S027 2027-04-17
DUE S035 2027-04-17
DUE S205 2027-04-20
DUE S652 2027-04-21
DUE S653 2027-04-21
DUE S654 2027-04-21
DUE S655 2027-04-21
DUE S656 2027-04-21
DUE S657 2027-04-21
DUE S658 2027-04-21
DUE S659 2027-04-21
DUE S660 2027-04-21
DUE S661 2027-04-21
DUE S662 2027-04-21
DUE S663 2027-04-21
DUE S664 2027-04-21
DUE S665 2027-04-21
DUE S666 2027-04-21
DUE S667 2027-04-21
DUE S668 2027-04-21
DUE S669 2027-04-21
DUE S670 2027-04-21
DUE S671 2027-04-21
DUE S672 2027-04-21
DUE S673 2027-04-21
DUE S674 2027-04-21
DUE S675 2027-04-21
DUE S676 2027-04-21
DUE S677 2027-04-21
DUE S678 2027-04-21
DUE S679 2027-04-21
DUE S680 2027-04-21
DUE S681 2027-04-21
DUE S682 2027-04-21
DUE S683 2027-04-21
DUE S684 2027-04-21
DUE S685 2027-04-21
DUE S686 2027-04-21
DUE S687 2027-04-21
DUE S688 2027-04-21
DUE S689 2027-04-21
DUE S690 2027-04-21
DUE S691 2027-04-21
DUE S692 2027-04-21
DUE S693 2027-04-21
DUE S694 2027-04-21
DUE S695 2027-04-21
DUE S696 2027-04-21
DUE S697 2027-04-21
DUE S698 2027-04-21
DUE S699 2027-04-21
DUE S700 2027-04-21
DUE S701 2027-04-21
DUE S702 2027-04-21
DUE S703 2027-04-21
DUE S704 2027-04-21
DUE S705 2027-04-21
DUE S706 2027-04-21
DUE S707 2027-04-21
DUE S708 2027-04-21
DUE S709 2027-04-21
DUE S710 2027-04-21
DUE S711 2027-04-21
DUE S712 2027-04-21
DUE S713 2027-04-21
DUE S714 2027-04-21
DUE S715 2027-04-21
DUE S716 2027-04-21
DUE S717 2027-04-21
DUE S718 2027-04-21
DUE S719 2027-04-21
DUE S720 2027-04-21
DUE S721 2027-04-21
DUE S722 2027-04-21
DUE S723 2027-04-21
DUE S724 2027-04-21
DUE S725 2027-04-21
DUE S726 2027-04-21
DUE S727 2027-04-21
DUE S728 2027-04-21
DUE S729 2027-04-21
DUE S730 2027-04-21
DUE S731 2027-04-21
DUE S732 2027-04-21
DUE S733 2027-04-21
DUE S734 2027-04-21
DUE S735 2027-04-21
DUE S736 2027-04-21
DUE S737 2027-04-21
DUE S738 2027-04-21
DUE S739 2027-04-21
DUE S740 2027-04-21
DUE S741 2027-04-21
DUE S742 2027-04-21
DUE S743 2027-04-21
DUE S744 2027-04-21
DUE S745 2027-04-21
DUE S746 2027-04-21
DUE S747 2027-04-21
DUE S748 2027-04-21
DUE S749 2027-04-21
DUE S750 2027-04-22
DUE S751 2027-04-22
DUE S752 2027-04-22
DUE S753 2027-04-22
DUE S754 2027-04-22
DUE S755 2027-04-22
DUE S756 2027-04-22
DUE S757 2027-04-22
DUE S758 2027-04-22
DUE S759 2027-04-22
DUE S760 2027-04-22
DUE S761 2027-04-22
DUE S762 2027-04-22
DUE S763 2027-04-22
DUE S764 2027-04-22
DUE S765 2027-04-22
DUE S766 2027-04-22
DUE S767 2027-04-22
DUE S768 2027-04-22
DUE S769 2027-04-22
DUE S770 2027-04-22
DUE S771 2027-04-22
DUE S772 2027-04-22
DUE S773 2027-04-22
DUE S774 2027-04-22
DUE S775 2027-04-22
DUE S776 2027-04-22
DUE S779 2027-04-22
DUE S780 2027-04-22
DUE S781 2027-04-22
DUE S782 2027-04-22
DUE S783 2027-04-22
DUE S784 2027-04-22
DUE S785 2027-04-22
DUE S786 2027-04-22
DUE S787 2027-04-22
DUE S788 2027-04-22
DUE S789 2027-04-22
DUE S790 2027-04-22
DUE S791 2027-04-22
DUE S792 2027-04-22
DUE S793 2027-04-22
DUE S794 2027-04-22
DUE S795 2027-04-22
DUE S796 2027-04-22
DUE S797 2027-04-22
DUE S798 2027-04-22
DUE S799 2027-04-22
DUE S800 2027-04-22
DUE S801 2027-04-22
DUE S802 2027-04-22
DUE S803 2027-04-22
DUE S804 2027-04-22
DUE S805 2027-04-22
DUE S806 2027-04-22
DUE S807 2027-04-22
DUE S808 2027-04-22
DUE S809 2027-04-22
DUE S810 2027-04-22
DUE S811 2027-04-22
DUE S812 2027-04-22
DUE S813 2027-04-22
DUE S814 2027-04-22
DUE S815 2027-04-22
DUE S816 2027-04-22
DUE S817 2027-04-22
DUE S818 2027-04-22
DUE S819 2027-04-22
DUE S820 2027-04-22
DUE S821 2027-04-22
DUE S822 2027-04-22
DUE S823 2027-04-22
DUE S824 2027-04-22
DUE S825 2027-04-22
DUE S826 2027-04-22
DUE S827 2027-04-22
DUE S828 2027-04-22
DUE S833 2027-04-22
DUE S834 2027-04-22
DUE S835 2027-04-22
DUE S836 2027-04-22
DUE S837 2027-04-22
DUE S838 2027-04-22
DUE S839 2027-04-22
DUE S840 2027-04-22
DUE S841 2027-04-22
DUE S842 2027-04-22
DUE S843 2027-04-22
DUE S844 2027-04-22
DUE S845 2027-04-22
DUE S846 2027-04-22
DUE S847 2027-04-22
DUE S848 2027-04-22
DUE S849 2027-04-22
DUE S850 2027-04-22
DUE S851 2027-04-22
DUE S852 2027-04-22
DUE S853 2027-04-22
DUE S854 2027-04-22
DUE S855 2027-04-22
DUE S856 2027-04-22
DUE S861 2027-04-23
DUE S862 2027-04-23
DUE S863 2027-04-23
DUE S864 2027-04-23
DUE S865 2027-04-23
DUE S866 2027-04-23
DUE S867 2027-04-23
DUE S868 2027-04-23
DUE S869 2027-04-23
DUE S870 2027-04-23
DUE S871 2027-04-23
DUE S872 2027-04-23
DUE S873 2027-04-23
DUE S874 2027-04-23
DUE S876 2027-04-23
DUE S877 2027-04-23
DUE S878 2027-04-23
DUE S879 2027-04-23
DUE S880 2027-04-23
DUE S881 2027-04-23
DUE S882 2027-04-23
DUE S883 2027-04-23
DUE S884 2027-04-23
DUE S885 2027-04-25
DUE S886 2027-04-25
DUE S887 2027-04-25
DUE S888 2027-04-25
DUE S889 2027-04-25
DUE S890 2027-04-25
DUE S891 2027-04-25
DUE S892 2027-04-25
DUE S893 2027-04-25
DUE S894 2027-04-25
DUE S895 2027-04-25
DUE S896 2027-04-25
DUE S897 2027-04-28
DUE S898 2027-04-29
DUE S899 2027-04-29
DUE S900 2027-04-29
DUE S901 2027-04-30
DUE S902 2027-04-30
DUE S903 2027-04-30
DUE S008 2027-10-19
DUE S011 2027-10-19
DUE S013 2027-10-19
DUE S014 2027-10-19
DUE S015 2027-10-19
DUE S018 2027-10-19
DUE S022 2027-10-19
DUE S024 2027-10-19
DUE S026 2027-10-19
DUE S028 2027-10-19
DUE S029 2027-10-19
DUE S030 2027-10-19
DUE S034 2027-10-19
DUE S036 2027-10-19
DUE S037 2027-10-19
DUE S038 2027-10-19
DUE S039 2027-10-19
DUE S040 2027-10-19
DUE S041 2027-10-19
DUE S043 2027-10-19
DUE S044 2027-10-19
DUE S045 2027-10-19
DUE S046 2027-10-19
DUE S047 2027-10-19
DUE S048 2027-10-21
DUE S049 2027-10-21
DUE S050 2027-10-21
DUE S051 2027-10-21
DUE S052 2027-10-21
DUE S053 2027-10-21
DUE S054 2027-10-21
DUE S055 2027-10-21
DUE S056 2027-10-21
DUE S057 2027-10-21
DUE S058 2027-10-21
DUE S059 2027-10-21
DUE S060 2027-10-21
DUE S061 2027-10-21
DUE S062 2027-10-21
DUE S063 2027-10-21
DUE S064 2027-10-21
DUE S065 2027-10-21
DUE S066 2027-10-21
DUE S067 2027-10-21
DUE S068 2027-10-21
DUE S069 2027-10-21
DUE S070 2027-10-21
DUE S071 2027-10-22
DUE S072 2027-10-22
DUE S074 2027-10-22
DUE S075 2027-10-22
DUE S076 2027-10-22
DUE S078 2027-10-22
DUE S079 2027-10-22
DUE S080 2027-10-22
DUE S081 2027-10-22
DUE S082 2027-10-22
DUE S083 2027-10-22
DUE S085 2027-10-22
DUE S086 2027-10-22
DUE S087 2027-10-22
DUE S089 2027-10-22
DUE S090 2027-10-22
DUE S091 2027-10-22
DUE S092 2027-10-22
DUE S093 2027-10-22
DUE S094 2027-10-22
DUE S095 2027-10-22
DUE S096 2027-10-22
DUE S097 2027-10-22
DUE S098 2027-10-22
DUE S099 2027-10-22
DUE S100 2027-10-22
DUE S101 2027-10-22
DUE S102 2027-10-22
DUE S103 2027-10-22
DUE S108 2027-10-22
DUE S109 2027-10-22
DUE S110 2027-10-22
DUE S111 2027-10-22
DUE S112 2027-10-22
DUE S113 2027-10-22
DUE S114 2027-10-22
DUE S115 2027-10-22
DUE S116 2027-10-22
DUE S117 2027-10-22
DUE S118 2027-10-22
DUE S119 2027-10-22
DUE S121 2027-10-22
DUE S122 2027-10-22
DUE S123 2027-10-22
DUE S124 2027-10-22
DUE S125 2027-10-22
DUE S127 2027-10-22
DUE S128 2027-10-22
DUE S129 2027-10-22
DUE S130 2027-10-22
DUE S131 2027-10-22
DUE S132 2027-10-22
DUE S133 2027-10-22
DUE S134 2027-10-22
DUE S135 2027-10-22
DUE S136 2027-10-22
DUE S137 2027-10-22
DUE S138 2027-10-22
DUE S139 2027-10-22
DUE S140 2027-10-22
DUE S141 2027-10-22
DUE S143 2027-10-22
DUE S144 2027-10-22
DUE S145 2027-10-22
DUE S146 2027-10-22
DUE S147 2027-10-22
DUE S148 2027-10-22
DUE S149 2027-10-22
DUE S150 2027-10-22
DUE S151 2027-10-22
DUE S152 2027-10-22
DUE S153 2027-10-22
DUE S154 2027-10-22
DUE S155 2027-10-22
DUE S156 2027-10-22
DUE S158 2027-10-22
DUE S159 2027-10-22
DUE S160 2027-10-22
DUE S161 2027-10-22
DUE S162 2027-10-22
DUE S164 2027-10-22
DUE S165 2027-10-22
DUE S166 2027-10-22
DUE S167 2027-10-22
DUE S168 2027-10-22
DUE S169 2027-10-22
DUE S170 2027-10-22
DUE S171 2027-10-22
DUE S172 2027-10-22
DUE S173 2027-10-22
DUE S174 2027-10-22
DUE S175 2027-10-22
DUE S176 2027-10-22
DUE S177 2027-10-22
DUE S178 2027-10-22
DUE S179 2027-10-22
DUE S180 2027-10-22
DUE S181 2027-10-22
DUE S182 2027-10-22
DUE S183 2027-10-22
DUE S184 2027-10-22
DUE S185 2027-10-22
DUE S186 2027-10-22
DUE S187 2027-10-22
DUE S188 2027-10-22
DUE S189 2027-10-22
DUE S190 2027-10-22
DUE S191 2027-10-22
DUE S192 2027-10-22
DUE S193 2027-10-22
DUE S194 2027-10-22
DUE S195 2027-10-22
DUE S196 2027-10-22
DUE S197 2027-10-22
DUE S198 2027-10-22
DUE S199 2027-10-22
DUE S200 2027-10-22
DUE S201 2027-10-22
DUE S202 2027-10-22
DUE S203 2027-10-22
DUE S204 2027-10-22
DUE S206 2027-10-22
DUE S207 2027-10-22
DUE S208 2027-10-22
DUE S209 2027-10-22
DUE S210 2027-10-22
DUE S211 2027-10-22
DUE S212 2027-10-22
DUE S213 2027-10-22
DUE S214 2027-10-22
DUE S215 2027-10-22
DUE S216 2027-10-22
DUE S217 2027-10-22
DUE S218 2027-10-22
DUE S219 2027-10-22
DUE S220 2027-10-22
DUE S221 2027-10-22
DUE S222 2027-10-22
DUE S223 2027-10-22
DUE S224 2027-10-22
DUE S225 2027-10-22
DUE S226 2027-10-22
DUE S227 2027-10-22
DUE S228 2027-10-22
DUE S229 2027-10-22
DUE S230 2027-10-22
DUE S231 2027-10-22
DUE S232 2027-10-22
DUE S233 2027-10-22
DUE S234 2027-10-22
DUE S235 2027-10-22
DUE S236 2027-10-22
DUE S237 2027-10-22
DUE S238 2027-10-22
DUE S239 2027-10-22
DUE S240 2027-10-22
DUE S241 2027-10-22
DUE S242 2027-10-22
DUE S243 2027-10-22
DUE S244 2027-10-22
DUE S245 2027-10-22
DUE S246 2027-10-22
DUE S247 2027-10-22
DUE S248 2027-10-22
DUE S249 2027-10-22
DUE S250 2027-10-22
DUE S251 2027-10-22
DUE S252 2027-10-22
DUE S253 2027-10-22
DUE S254 2027-10-22
DUE S255 2027-10-22
DUE S256 2027-10-22
DUE S257 2027-10-22
DUE S258 2027-10-22
DUE S259 2027-10-22
DUE S260 2027-10-22
DUE S261 2027-10-22
DUE S262 2027-10-22
DUE S263 2027-10-22
DUE S264 2027-10-22
DUE S265 2027-10-22
DUE S266 2027-10-22
DUE S267 2027-10-22
DUE S268 2027-10-22
DUE S269 2027-10-22
DUE S270 2027-10-22
DUE S271 2027-10-22
DUE S272 2027-10-22
DUE S273 2027-10-22
DUE S274 2027-10-22
DUE S275 2027-10-22
DUE S276 2027-10-22
DUE S277 2027-10-22
DUE S278 2027-10-22
DUE S279 2027-10-22
DUE S280 2027-10-22
DUE S281 2027-10-22
DUE S282 2027-10-22
DUE S283 2027-10-22
DUE S284 2027-10-22
DUE S285 2027-10-22
DUE S286 2027-10-22
DUE S287 2027-10-22
DUE S288 2027-10-22
DUE S289 2027-10-22
DUE S290 2027-10-22
DUE S291 2027-10-22
DUE S292 2027-10-22
DUE S293 2027-10-22
DUE S294 2027-10-22
DUE S295 2027-10-22
DUE S296 2027-10-22
DUE S297 2027-10-22
DUE S298 2027-10-22
DUE S299 2027-10-22
DUE S300 2027-10-22
DUE S301 2027-10-22
DUE S302 2027-10-22
DUE S303 2027-10-22
DUE S304 2027-10-22
DUE S305 2027-10-22
DUE S306 2027-10-22
DUE S307 2027-10-22
DUE S308 2027-10-22
DUE S309 2027-10-22
DUE S310 2027-10-22
DUE S311 2027-10-22
DUE S312 2027-10-22
DUE S313 2027-10-22
DUE S314 2027-10-22
DUE S315 2027-10-22
DUE S316 2027-10-22
DUE S317 2027-10-22
DUE S318 2027-10-22
DUE S319 2027-10-22
DUE S320 2027-10-22
DUE S321 2027-10-22
DUE S322 2027-10-22
DUE S323 2027-10-22
DUE S324 2027-10-22
DUE S325 2027-10-22
DUE S326 2027-10-22
DUE S327 2027-10-22
DUE S328 2027-10-22
DUE S329 2027-10-22
DUE S330 2027-10-22
DUE S331 2027-10-22
DUE S332 2027-10-22
DUE S333 2027-10-22
DUE S334 2027-10-22
DUE S335 2027-10-22
DUE S336 2027-10-22
DUE S337 2027-10-22
DUE S338 2027-10-22
DUE S339 2027-10-22
DUE S340 2027-10-22
DUE S341 2027-10-22
DUE S342 2027-10-22
DUE S343 2027-10-22
DUE S344 2027-10-22
DUE S345 2027-10-22
DUE S346 2027-10-22
DUE S347 2027-10-22
DUE S348 2027-10-22
DUE S349 2027-10-22
DUE S350 2027-10-22
DUE S351 2027-10-22
DUE S352 2027-10-22
DUE S353 2027-10-22
DUE S354 2027-10-22
DUE S355 2027-10-22
DUE S356 2027-10-22
DUE S357 2027-10-22
DUE S358 2027-10-22
DUE S359 2027-10-22
DUE S360 2027-10-22
DUE S361 2027-10-22
DUE S362 2027-10-22
DUE S363 2027-10-22
DUE S364 2027-10-22
DUE S365 2027-10-22
DUE S366 2027-10-22
DUE S367 2027-10-22
DUE S368 2027-10-22
DUE S369 2027-10-22
DUE S370 2027-10-22
DUE S371 2027-10-22
DUE S372 2027-10-22
DUE S373 2027-10-22
DUE S374 2027-10-22
DUE S375 2027-10-22
DUE S376 2027-10-22
DUE S377 2027-10-22
DUE S378 2027-10-22
DUE S379 2027-10-22
DUE S380 2027-10-22
DUE S381 2027-10-22
DUE S382 2027-10-22
DUE S383 2027-10-22
DUE S384 2027-10-22
DUE S385 2027-10-22
DUE S386 2027-10-22
DUE S387 2027-10-22
DUE S388 2027-10-22
DUE S389 2027-10-22
DUE S390 2027-10-22
DUE S391 2027-10-22
DUE S392 2027-10-22
DUE S393 2027-10-22
DUE S394 2027-10-22
DUE S395 2027-10-22
DUE S396 2027-10-22
DUE S397 2027-10-22
DUE S398 2027-10-22
DUE S399 2027-10-22
DUE S400 2027-10-22
DUE S401 2027-10-22
DUE S402 2027-10-22
DUE S403 2027-10-22
DUE S404 2027-10-22
DUE S405 2027-10-22
DUE S406 2027-10-22
DUE S407 2027-10-22
DUE S408 2027-10-22
DUE S409 2027-10-22
DUE S410 2027-10-22
DUE S411 2027-10-22
DUE S412 2027-10-22
DUE S413 2027-10-22
DUE S414 2027-10-22
DUE S415 2027-10-22
DUE S416 2027-10-22
DUE S417 2027-10-22
DUE S418 2027-10-22
DUE S419 2027-10-22
DUE S420 2027-10-22
DUE S421 2027-10-22
DUE S422 2027-10-22
DUE S423 2027-10-22
DUE S424 2027-10-22
DUE S425 2027-10-22
DUE S426 2027-10-22
DUE S427 2027-10-22
DUE S428 2027-10-22
DUE S429 2027-10-22
DUE S430 2027-10-22
DUE S431 2027-10-22
DUE S432 2027-10-22
DUE S433 2027-10-22
DUE S434 2027-10-22
DUE S435 2027-10-22
DUE S436 2027-10-22
DUE S437 2027-10-22
DUE S438 2027-10-22
DUE S439 2027-10-22
DUE S440 2027-10-22
DUE S441 2027-10-22
DUE S442 2027-10-22
DUE S443 2027-10-22
DUE S444 2027-10-22
DUE S445 2027-10-22
DUE S446 2027-10-22
DUE S447 2027-10-22
DUE S448 2027-10-22
DUE S449 2027-10-22
DUE S450 2027-10-22
DUE S451 2027-10-22
DUE S452 2027-10-22
DUE S453 2027-10-22
DUE S454 2027-10-22
DUE S481 2027-10-22
DUE S482 2027-10-22
DUE S483 2027-10-22
DUE S484 2027-10-22
DUE S485 2027-10-22
DUE S486 2027-10-22
DUE S487 2027-10-22
DUE S488 2027-10-22
DUE S489 2027-10-22
DUE S490 2027-10-22
DUE S491 2027-10-22
DUE S500 2027-10-23
DUE S501 2027-10-23
DUE S502 2027-10-23
DUE S503 2027-10-23
DUE S504 2027-10-23
DUE S505 2027-10-23
DUE S506 2027-10-23
DUE S507 2027-10-23
DUE S508 2027-10-23
DUE S509 2027-10-23
DUE S510 2027-10-23
DUE S511 2027-10-23
DUE S512 2027-10-23
DUE S513 2027-10-23
DUE S514 2027-10-23
DUE S515 2027-10-23
DUE S516 2027-10-23
DUE S517 2027-10-23
DUE S518 2027-10-23
DUE S519 2027-10-23
DUE S520 2027-10-23
DUE S521 2027-10-23
DUE S522 2027-10-23
DUE S523 2027-10-23
DUE S524 2027-10-23
DUE S525 2027-10-23
DUE S526 2027-10-23
DUE S527 2027-10-23
DUE S528 2027-10-23
DUE S529 2027-10-23
DUE S530 2027-10-23
DUE S531 2027-10-23
DUE S532 2027-10-23
DUE S533 2027-10-23
DUE S534 2027-10-23
DUE S535 2027-10-23
DUE S536 2027-10-23
DUE S537 2027-10-23
DUE S538 2027-10-23
DUE S539 2027-10-23
DUE S540 2027-10-23
DUE S541 2027-10-23
DUE S542 2027-10-23
DUE S543 2027-10-23
DUE S560 2027-10-23
DUE S561 2027-10-23
DUE S562 2027-10-23
DUE S564 2027-10-23
DUE S565 2027-10-23
DUE S566 2027-10-23
DUE S567 2027-10-23
DUE S568 2027-10-23
DUE S569 2027-10-23
DUE S570 2027-10-23
DUE S571 2027-10-23
DUE S572 2027-10-23
DUE S573 2027-10-23
DUE S574 2027-10-23
DUE S575 2027-10-23
DUE S576 2027-10-23
DUE S600 2027-10-23
DUE S601 2027-10-23
DUE S602 2027-10-23
DUE S603 2027-10-23
DUE S604 2027-10-23
DUE S605 2027-10-23
DUE S606 2027-10-23
DUE S607 2027-10-23
DUE S608 2027-10-23
DUE S609 2027-10-23
DUE S610 2027-10-23
DUE S611 2027-10-23
DUE S612 2027-10-23
DUE S613 2027-10-23
DUE S614 2027-10-23
DUE S615 2027-10-23
DUE S616 2027-10-23
DUE S617 2027-10-23
DUE S618 2027-10-23
DUE S619 2027-10-23
DUE S620 2027-10-23
DUE S621 2027-10-23
DUE S622 2027-10-23
DUE S623 2027-10-23
DUE S624 2027-10-23
DUE S625 2027-10-23
DUE S626 2027-10-23
DUE S627 2027-10-23
DUE S628 2027-10-23
DUE S629 2027-10-23
DUE S630 2027-10-23
DUE S631 2027-10-23
DUE S632 2027-10-23
DUE S633 2027-10-23
DUE S634 2027-10-23
DUE S635 2027-10-23
DUE S636 2027-10-23
DUE S637 2027-10-23
DUE S638 2027-10-23
DUE S639 2027-10-23
DUE S640 2027-10-23
DUE S641 2027-10-23
DUE S642 2027-10-23
DUE S643 2027-10-23
DUE S644 2027-10-23
DUE S645 2027-10-23
DUE S646 2027-10-23
DUE S647 2027-10-23
DUE S648 2027-10-23
DUE S649 2027-10-23
DUE S650 2027-10-23
DUE S651 2027-10-23
DUE S829 2027-10-24
DUE S830 2027-10-24
DUE S831 2027-10-24
DUE S832 2027-10-24
DUE S857 2027-10-24
DUE S858 2027-10-24
due+upcoming+exempt=827, rows=827, unclassified=0
```
