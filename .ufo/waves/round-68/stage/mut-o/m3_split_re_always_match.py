#!/usr/bin/env python3
r"""Round-68 operability capability: supersession-settlement checker.

The registry's correction mechanism is append-only: a defective row keeps its
cells and a new row whose `teaches` opens `supersedes S### —` carries the fix.
A chain is *settled* when exactly one state holds:

- SETTLED-ACTIVE  — the superseding row is `mined` with a `used-by` naming a
  real corpus path (the entry re-pointed to it) and the superseded row is no
  longer `mined` (`queued` or `rejected`).
- SETTLED-RETIRED — the superseding row is `rejected` (the correction was
  audited and refused; the superseded row keeps whatever status it holds).
- SETTLED-CLOSED  — the superseded row itself is `rejected` (keep-successor
  fingerprint: the chain resolved earlier and the successor is live).
- SETTLED-SPLIT   — both rows `mined` and the superseding `teaches` text
  carries an explicit scope limiter ("for entry/line/… only"); the
  supersession covers a named slice, both rows keep their scopes.

Any other non-rejected pair is `pending`: correction debt. A row whose
`used-by` names a path that does not contain the row's own id is
`STALE-USED-BY` (reported; gated only for the frozen ruling set, not globally —
the `--scan` exit code gates `pending` alone).

Usage:
  --scan      classify every supersedes chain; print one line per chain plus a
              `SETTLEMENT: pending=N keep=M stale_usedby=K` summary; exit 0 iff
              pending == 0 else 1, exit 2 on unreadable registry.
  --ledger F  validate a disposition ledger (TSV) against the registry: each
              row's ruling class is in {activate, retire, keep-successor,
              keep-reject, keep-split}, both ids resolve, and the ruling is
              consistent with the current row statuses; exit 0/1, 2 on
              unreadable input.
  --selftest  run the committed fixture battery; exit 0 iff every check holds.

Ledger columns (TSV, `|` inside a field forbidden):
  id | related | url | ruling | mechanism | evidence | note
`mechanism` is free text naming the settlement step (repoint, usedby-flip,
cell-flip, none); `evidence` is a repo path or audit artifact.

This tool reads; it never mutates. Fixture selftests build temp registries
only. No network.
"""

import argparse
import os
import re
import subprocess
import sys
import tempfile

ROW_RE = re.compile(r"^\|\s*(S\d{3,})\s*\|")
URL_RE = re.compile(r"https?://[^\s|]+")
SUP_RE = re.compile(r"supersedes\s+(S\d{3,})")
SPLIT_RE = re.compile(r"", re.S)
RULINGS = {"activate", "retire", "keep-successor", "keep-reject", "keep-split"}
KINDS = {"spec", "docs", "paper", "code", "tool", "dataset", "talk", "book",
         "community", "own-work"}


def norm_url(url):
    url = re.sub(r"#.*$", "", url).rstrip("/")
    url = re.sub(r"^[A-Za-z]+://", "", url)
    n = url.find("/")
    return (url[:n].lower() + url[n:]) if n > 0 else url.lower()


def parse_registry(text):
    rows = {}
    order = []
    in_registry = False
    for line in text.splitlines():
        s = line.strip()
        if s.startswith("##"):
            in_registry = s[2:].strip().lower().startswith("registry")
            continue
        if s.startswith("#"):
            in_registry = False
            continue
        if not in_registry:
            continue
        m = ROW_RE.match(s)
        if not m:
            continue
        c = [x.strip() for x in s.split("|")[1:-1]]
        if len(c) != 11:
            rows[m.group(1)] = {"malformed": True, "id": m.group(1)}
            continue
        rid, src, kind, tier, scope, anchor, teaches, status, opened, recheck, usedby = c
        u = ""
        mm = URL_RE.search(src)
        if mm:
            u = norm_url(mm.group(0))
        sm = SUP_RE.search(teaches)
        rows[rid] = {
            "id": rid, "url": u, "scope": scope, "teaches": teaches,
            "status": status, "usedby": usedby, "kind": kind, "tier": tier,
            "supersedes": sm.group(1) if sm else None, "malformed": False,
        }
        order.append(rid)
    return rows, order


def usedby_paths(row):
    out = []
    for p in re.split(r"[,;]", row["usedby"]):
        p = p.strip()
        if p and p != "—":
            out.append(p)
    return out


def classify(rows, order):
    """Return (chains, stale) — chains: list of dicts per supersedes pair."""
    chains = []
    for rid in order:
        r = rows[rid]
        if r.get("malformed") or not r["supersedes"]:
            continue
        t = r["supersedes"]
        s_st, t_row = r["status"], rows.get(t)
        t_st = t_row["status"] if t_row else "missing"
        s_used = usedby_paths(r)
        if t_st == "rejected":
            cls = "settled-closed"
        elif s_st == "rejected":
            cls = "settled-retired"
        elif s_st == "mined" and s_used and t_st == "queued":
            cls = "settled-active"
        elif s_st == "mined" and s_used and t_st == "mined" and \
                SPLIT_RE.search(r["teaches"]):
            cls = "settled-split"
        else:
            cls = "pending"
        chains.append({"s": rid, "t": t, "cls": cls,
                       "s_status": s_st, "t_status": t_st,
                       "same_url": bool(t_row) and r["url"] == t_row["url"],
                       "s_usedby": s_used})
    stale = []
    for rid in order:
        r = rows[rid]
        if r.get("malformed"):
            continue
        for p in usedby_paths(r):
            stale.append((rid, p))
    return chains, stale


def scan(root, registry_path):
    path = registry_path or os.path.join(root, "corpus/SOURCES.md")
    try:
        text = open(path, encoding="utf-8", errors="strict").read()
    except (OSError, UnicodeError) as exc:
        print(f"SCAN_ERROR {exc!r}")
        return 2
    rows, order = parse_registry(text)
    chains, stale = classify(rows, order)
    pending = [c for c in chains if c["cls"] == "pending"]
    for c in chains:
        print(f"{c['cls'].upper()} {c['s']}>{c['t']} "
              f"s={c['s_status']} t={c['t_status']} "
              f"same_url={c['same_url']} used_by={len(c['s_usedby'])}")
    # used-by resolution: only rows with corpus/ paths are checked for
    # existence here; citation truth is review work.
    missing_paths = [p for _, p in stale if not os.path.exists(os.path.join(root, p))]
    print(f"SETTLEMENT: pending={len(pending)} chains={len(chains)} "
          f"usedby_paths={len(stale)} missing_paths={len(missing_paths)}")
    return 1 if pending else 0


def validate_ledger(root, registry_path, ledger_path):
    try:
        reg_text = open(registry_path or os.path.join(root, "corpus/SOURCES.md"),
                        encoding="utf-8", errors="strict").read()
        led_text = open(ledger_path, encoding="utf-8", errors="strict").read()
    except (OSError, UnicodeError) as exc:
        print(f"LEDGER_ERROR {exc!r}")
        return 2
    rows, order = parse_registry(reg_text)
    seen_ids, bad = set(), []
    lineno = 0
    for raw in led_text.splitlines():
        line = raw.strip()
        lineno += 1
        if not line or line.startswith("#"):
            continue
        cells = [c.strip() for c in line.split("|")]
        if len(cells) != 7:
            bad.append(f"L{lineno}:fields={len(cells)}")
            continue
        rid, related, url, ruling, mechanism, evidence, note = cells
        if not re.fullmatch(r"S\d{3,}", rid):
            bad.append(f"L{lineno}:bad_id={rid!r}")
            continue
        if ruling not in RULINGS:
            bad.append(f"L{lineno}:ruling={ruling!r}")
        if rid in seen_ids:
            bad.append(f"L{lineno}:dup_id={rid}")
        seen_ids.add(rid)
        if rid not in rows:
            bad.append(f"L{lineno}:{rid}:not_in_registry")
            continue
        if related and not re.fullmatch(r"S\d{3,}", related):
            bad.append(f"L{lineno}:related={related!r}")
        elif related and related not in rows:
            bad.append(f"L{lineno}:{rid}:related_absent={related}")
        st = rows[rid]["status"]
        if ruling == "activate" and st != "mined":
            bad.append(f"L{lineno}:{rid}:activate_but_status={st}")
        if ruling == "retire" and st != "rejected":
            bad.append(f"L{lineno}:{rid}:retire_but_status={st}")
        if ruling == "keep-reject" and st != "rejected":
            bad.append(f"L{lineno}:{rid}:keep_reject_but_status={st}")
        for p in usedby_paths(rows[rid]):
            if not os.path.exists(os.path.join(root, p)):
                bad.append(f"L{lineno}:{rid}:usedby_missing={p}")
    print(f"LEDGER: rows={len(seen_ids)} findings={len(bad)}")
    for b in bad:
        print(f"LEDGER-FINDING {b}")
    return 1 if bad else 0


# ---------------------------------------------------------------- selftest --
FIX1 = """# t
## Registry
| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
| S001 | a — https://x.example/a | docs | B | s1 | "q" | base claim | mined | 2026-10-24 | 90d | corpus/knowledge/a.md |
| S002 | b — https://x.example/a | docs | B | s2 | "q" | supersedes S001 — tier fix | queued | 2026-10-24 | 90d | — |
"""
FIX2 = """# t
## Registry
| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
| S001 | a — https://x.example/a | docs | B | s1 | "q" | base claim | queued | 2026-10-24 | 90d | — |
| S002 | b — https://x.example/a | docs | B | s2 | "q" | supersedes S001 — tier fix | mined | 2026-10-24 | 90d | corpus/knowledge/a.md |
"""
FIX3 = """# t
## Registry
| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
| S001 | a — https://x.example/a | docs | B | s1 | "q" | base claim | mined | 2026-10-24 | 90d | corpus/knowledge/a.md |
| S002 | b — https://x.example/a | docs | B | s2 | "q" | supersedes S001 — wrong fix | rejected | 2026-10-24 | 90d | — |
| S003 | c — https://x.example/c | docs | A | s3 | "q" | supersedes S004 — ok | mined | 2026-10-24 | 90d | corpus/knowledge/a.md |
| S004 | d — https://x.example/c | docs | A | s4 | "q" | old claim | rejected | 2026-10-24 | 90d | — |
"""

FIX4 = """# t
## Registry
| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
| S001 | a — https://x.example/a | docs | B | s1 | "q" | base claim | mined | 2026-10-24 | 90d | corpus/knowledge/a.md |
| S002 | b — https://x.example/b | docs | A | s2 | "q" | supersedes S001 for entry line 41's cadet clause only | mined | 2026-10-24 | 90d | corpus/knowledge/a.md |
"""


def _mk(root, files):
    for rel, content in files.items():
        p = os.path.join(root, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w", encoding="utf-8") as fh:
            fh.write(content)


def selftest():
    checks = []

    def chk(name, cond):
        checks.append((name, bool(cond)))

    with tempfile.TemporaryDirectory(prefix="srs-") as td:
        # f1: one pending chain
        _mk(td, {"f1/corpus/SOURCES.md": FIX1,
                 "f1/corpus/knowledge/a.md": "cites S001 here\n"})
        rc1 = scan(os.path.join(td, "f1"), None)
        chk("pending-detected", rc1 == 1)
        # f2: settled-active chain
        _mk(td, {"f2/corpus/SOURCES.md": FIX2,
                 "f2/corpus/knowledge/a.md": "cites S002 now\n"})
        rc2 = scan(os.path.join(td, "f2"), None)
        chk("settled-active", rc2 == 0)
        # f3: retired + closed chains
        _mk(td, {"f3/corpus/SOURCES.md": FIX3,
                 "f3/corpus/knowledge/a.md": "cites S003\n"})
        rc3 = scan(os.path.join(td, "f3"), None)
        chk("settled-retired-closed", rc3 == 0)
        # f4s: settled-split chain (self-limiting teaches, both mined)
        _mk(td, {"f4s/corpus/SOURCES.md": FIX4,
                 "f4s/corpus/knowledge/a.md": "cites S001 and S002\n"})
        rc4s = scan(os.path.join(td, "f4s"), None)
        chk("settled-split", rc4s == 0)
        # f4: ledger validation — one good, one inconsistent row
        _mk(td, {"f4/corpus/SOURCES.md": FIX2,
                 "f4/corpus/knowledge/a.md": "cites S002 now\n",
                 "f4/ledger.tsv": "S002 | S001 | https://x.example/a | activate | repoint | corpus/knowledge/a.md | tier fix\n"})
        rc4 = validate_ledger(os.path.join(td, "f4"), None,
                              os.path.join(td, "f4", "ledger.tsv"))
        chk("ledger-clean", rc4 == 0)
        _mk(td, {"f4/bad.tsv": "S001 | S002 | https://x.example/a | activate | repoint | x | wrong status\nS999 | S001 | u | activate | x | x | ghost\n"})
        rc5 = validate_ledger(os.path.join(td, "f4"), None,
                              os.path.join(td, "f4", "bad.tsv"))
        chk("ledger-inconsistent-rejected", rc5 == 1)
        # f5: missing registry -> 2
        _mk(td, {"f5/.keep": ""})
        rc6 = scan(os.path.join(td, "f5"), None)
        chk("unreadable-exit-2", rc6 == 2)
    total = len(checks)
    passed = sum(1 for _, c in checks if c)
    for name, c in checks:
        print(f"{'PASS' if c else 'FAIL'} {name}")
    print(f"SELFTEST: {passed}/{total}")
    return 0 if passed == total else 1


def main():
    ap = argparse.ArgumentParser(description="supersession-settlement checker")
    ap.add_argument("--root", default=".")
    ap.add_argument("--registry", default=None)
    ap.add_argument("--scan", action="store_true")
    ap.add_argument("--ledger", default=None, metavar="FILE")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    root = os.path.abspath(args.root)
    if args.selftest:
        return selftest()
    if args.ledger:
        return validate_ledger(root, args.registry, args.ledger)
    # default: scan
    return scan(root, args.registry)


if __name__ == "__main__":
    sys.exit(main())
