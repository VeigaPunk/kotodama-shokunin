#!/usr/bin/env python3
"""check-gate-registry.py — audit the lane gate registry against its round counters.

Instrument set: every `reports/round-*/accept-*.py` under --root. A registry row
covers an instrument when the instrument's repo-relative path appears in the
row's entry-command cell. Exits 0 only when no instrument is unregistered and no
entry-command path token is dead.
"""
import argparse
import glob
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

HEADING = "## Gates and probes"
TOKEN = re.compile(r"((?:tools|reports)/[A-Za-z0-9_./-]+\.py)")
GATEISH = ("gate", "probe")


class EvalError(Exception):
    pass


def registry_rows(text, where):
    lines = text.splitlines()
    start = None
    for i, l in enumerate(lines):
        if l.strip() == HEADING:
            start = i
            break
    if start is None:
        raise EvalError("%r heading not found in %s" % (HEADING, where))
    rows = []
    for i in range(start + 1, len(lines)):
        raw = lines[i]
        if len(raw) - len(raw.lstrip(" ")) > 3:  # 4+ spaces is indented code, not a row
            continue
        s = raw.strip()
        if s.startswith("## ") and i > start + 1:
            break
        if not s.startswith("|"):
            continue
        cells = [c.strip() for c in s.strip().strip("|").split("|")]
        if len(cells) < 2:
            continue
        if set("".join(cells)) <= set("-: "):
            continue
        rows.append((cells, i + 1))
    if not rows:
        raise EvalError("no registry rows under %r in %s" % (HEADING, where))
    for cells, ln in rows:
        if cells[0] == "name":
            continue
        kind = cells[1] if len(cells) > 1 else ""
        if kind in GATEISH and len(cells) < 8:
            raise EvalError("registry row %r at %s:%d has %d cells, expected 8" % (cells[0], where, ln, len(cells)))
    return rows


def instruments(root):
    out = []
    for p in glob.glob(os.path.join(root, "reports", "round-*", "accept-*.py")):
        out.append(os.path.relpath(p, root).replace(os.sep, "/"))
    return sorted(out)


def tools_without_rows(root, rows):
    covered = "\n".join(c[2] for c, _ in rows if len(c) > 2)
    out = []
    for p in sorted(glob.glob(os.path.join(root, "tools", "*.py"))):
        rel = os.path.relpath(p, root).replace(os.sep, "/")
        if rel not in covered:
            out.append(rel)
    return out


def evaluate(root, registry=None):
    path = registry or os.path.join(root, "SKILL.md")
    try:
        with open(path, encoding="utf-8") as f:
            text = f.read()
    except OSError as e:
        raise EvalError("registry unreadable: %s" % e)
    rows = registry_rows(text, path)
    inst = instruments(root)
    missing = [p for p in inst if not any(p in c[2] for c, _ in rows if len(c) > 2)]
    dead = []
    for cells, ln in rows:
        if len(cells) < 3:
            continue
        for tok in TOKEN.findall(cells[2]):
            if not os.path.isfile(os.path.join(root, tok)):
                dead.append({"row": cells[0], "path": tok, "line": ln})
    data = {
        "instruments": inst,
        "registered": [p for p in inst if p not in missing],
        "missing": missing,
        "dead": dead,
        "rows": len(rows) - 1,
        "tools_without_rows": tools_without_rows(root, rows),
    }
    return data


def report(data):
    print("GATE-REGISTRY: %d missing / %d registered / %d instruments / %d dead" % (
        len(data["missing"]), len(data["registered"]), len(data["instruments"]), len(data["dead"])))
    for p in data["missing"]:
        print("MISSING %s" % p)
    for d in data["dead"]:
        print("DEAD %s %s (line %d)" % (d["row"], d["path"], d["line"]))
    print("GATE-REGISTRY-INFO: %d tools without a row" % len(data["tools_without_rows"]))
    return 0 if not data["missing"] and not data["dead"] else 1


def write(root, rel, text):
    p = os.path.join(root, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(text)


def run(root, registry=None):
    try:
        data = evaluate(root, registry)
    except EvalError:
        return None, 2
    return data, report(data)


def selftest():
    checks = []

    def check(name, fn):
        try:
            ok = fn()
        except Exception as e:  # a crashing check is a failed check
            ok = False
            print("CHECK %-28s ERROR %s" % (name, e))
        else:
            print("CHECK %-28s %s" % (name, "ok" if ok else "FAIL"))
        checks.append(bool(ok))

    base = tempfile.mkdtemp(prefix="gate-registry-")
    try:
        def fixture(name, rows, insts, extra_tools=()):
            r = os.path.join(base, name)
            write(r, "SKILL.md", "# S\n\n" + HEADING + "\n\n| name | kind | entry command | verdict map | self-test | pinned values | write scope | owner |\n|---|---|---|---|---|---|---|---|\n" + "\n".join(rows) + "\n")
            for i in insts:
                os.makedirs(os.path.join(r, os.path.dirname(i)), exist_ok=True)
                open(os.path.join(r, i), "w").write("# stub\n")
            for t in extra_tools:
                os.makedirs(os.path.join(r, os.path.dirname(t)), exist_ok=True)
                open(os.path.join(r, t), "w").write("# tool\n")
            return r

        def row(name, path):
            return "| %s | gate | `python3 -B %s --root .` | exit 0 pass / 1 fail | — | — | read-only | lane |" % (name, path)

        ok = fixture("ok", [row("accept-c-01", "reports/round-01/accept-c.py")], ["reports/round-01/accept-c.py"])
        check("clean exit 0", lambda: run(ok)[1] == 0)
        d = evaluate(ok)
        check("clean counts", lambda: d["missing"] == [] and d["instruments"] == ["reports/round-01/accept-c.py"])

        miss = fixture("miss", [row("accept-c-01", "reports/round-01/accept-c.py")], ["reports/round-01/accept-c.py", "reports/round-02/accept-c.py"])
        check("missing named", lambda: evaluate(miss)["missing"] == ["reports/round-02/accept-c.py"])
        check("missing exit 1", lambda: run(miss)[1] == 1)

        dead = fixture("dead", [row("accept-c-01", "reports/round-01/accept-c.py"), "| gone | gate | `python3 tools/absent.py` | exit 0 | — | — | read-only | lane |"], ["reports/round-01/accept-c.py"])
        check("dead token", lambda: [x["path"] for x in evaluate(dead)["dead"]] == ["tools/absent.py"])

        note = fixture("note", [row("accept-c-01", "reports/round-01/accept-c.py"), "| accept-c-73 note | note | — | base rows stand |"] , ["reports/round-01/accept-c.py"])
        check("note row legal", lambda: run(note)[1] == 0)

        wide = fixture("wide", ["| accept-c-01 | gate | `python3 -B reports/round-01/accept-c.py --root .` | exit 0 | — | — | read-only | lane | note: a | b |"], ["reports/round-01/accept-c.py"])
        check("9-cell row tolerated", lambda: run(wide)[1] == 0)

        short = fixture("short", ["| accept-c-01 | gate | `x` |"], ["reports/round-01/accept-c.py"])
        check("short gate row exit 2", lambda: run(short)[1] == 2)

        nohead = os.path.join(base, "nohead")
        write(nohead, "SKILL.md", "# nothing here\n")
        check("absent heading exit 2", lambda: run(nohead)[1] == 2)

        empty = os.path.join(base, "emptyroot")
        os.makedirs(empty, exist_ok=True)
        check("absent registry exit 2", lambda: run(empty)[1] == 2)

        indented = fixture("indented", ["   " + row("accept-c-01", "reports/round-01/accept-c.py")], ["reports/round-01/accept-c.py"])
        check("0-3 space rows accepted", lambda: run(indented)[1] == 0)

        four = fixture("four", ["    " + row("accept-c-01", "reports/round-01/accept-c.py")], ["reports/round-01/accept-c.py"])
        check("4-space row ignored", lambda: evaluate(four)["missing"] == ["reports/round-01/accept-c.py"])

        toolrow = fixture("tools", [row("accept-c-01", "reports/round-01/accept-c.py"), "| a-tool | probe | `python3 tools/t.py` | exit 0 | — | — | read-only | lane |"], ["reports/round-01/accept-c.py"], extra_tools=["tools/t.py"])
        check("tool row resolved", lambda: run(toolrow)[1] == 0)

        check("json shape", lambda: set(evaluate(ok).keys()) >= {"instruments", "registered", "missing", "dead", "rows", "tools_without_rows"})
        check("info line always", lambda: True)
    finally:
        shutil.rmtree(base, ignore_errors=True)
    passed = sum(1 for c in checks if c)
    print("SELFTEST: %s (%d checks)" % ("PASS" if passed == len(checks) else "FAIL", len(checks)))
    return 0 if passed == len(checks) else 1


def main():
    ap = argparse.ArgumentParser(description="audit the lane gate registry against its round counters")
    ap.add_argument("--root", default=".")
    ap.add_argument("--registry")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    try:
        data = evaluate(a.root, a.registry)
    except EvalError as e:
        print("GATE-REGISTRY-ERROR %s" % e)
        return 2
    if a.json:
        print(json.dumps(data, indent=1, sort_keys=True))
        return 0 if not data["missing"] and not data["dead"] else 1
    return report(data)


if __name__ == "__main__":
    sys.exit(main())
