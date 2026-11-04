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
