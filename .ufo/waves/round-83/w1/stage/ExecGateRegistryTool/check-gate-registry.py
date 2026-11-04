#!/usr/bin/env python3
r"""check-gate-registry.py — gate-registry coverage auditor for kotodama-shokunin.

Round 83 (hyaku 15), claim O. Audits the `## Gates and probes` registry table
in SKILL.md against the committed counter fleet:

  instruments  sorted repo-relative reports/round-*/accept-*.py files under
               --root; an instrument is covered iff its path is a substring of
               some registry row's entry-command cell (visible cell index 2);
  dead rows    every (tools|reports)/[A-Za-z0-9_./-]+.py token in an
               entry-command cell must exist under --root.

Row rules (measured on the real table): the first pipe row after the heading
is the header; `---` separator rows are skipped; data rows normally carry
>= 8 cells, but a row of kind `note` (or any kind other than `gate`/`probe`)
may carry fewer, and a `gate`/`probe` row may carry more than 8 cells when a
literal `|` sits inside a later cell — the entry command is always visible
cell 3. Only a `gate`/`probe` data row with fewer than 8 cells is
could-not-evaluate.

Plain output: exactly one GATE-REGISTRY summary line, then one MISSING line
per uncovered instrument, one DEAD line per unresolvable token, then exactly
one GATE-REGISTRY-INFO line counting tools/*.py files no row names (the info
line never affects the exit code). Exit 0 iff nothing is missing and nothing
is dead; 1 otherwise; 2 with GATE-REGISTRY-ERROR on could-not-evaluate
(absent registry, absent heading, a short gate/probe row, unreadable input).
No traceback ever.

`--json` prints exactly one JSON object and nothing else (the grader parses
the whole stdout with json.loads). `--selftest` runs a fixture battery in a
tempfile.mkdtemp() directory (honouring TMPDIR; never a hardcoded /tmp).
Stdlib only; never imports counterlib.

Frozen contract: reports/round-83/claims.json (claim O tool83 block); graded
by reports/round-83/accept-o83.py.
"""

from __future__ import annotations

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
MIN_CELLS = 8            # gate/probe rows carry at least 8 pipe-separated cells
ENTRY_CELL = 2           # visible-cell index of the entry command
KIND_CELL = 1            # visible-cell index of the row kind
GATED_KINDS = ("gate", "probe")
ROW_PREFIX = re.compile(r"^ {0,3}\|")
H2 = "## "
TOKEN = re.compile(r"(?:tools|reports)/[A-Za-z0-9_./-]+\.py")
INSTRUMENT_GLOB = ("reports", "round-*", "accept-*.py")
TOOLS_GLOB = ("tools", "*.py")


class RegistryError(Exception):
    """Could-not-evaluate: reported as GATE-REGISTRY-ERROR, exit 2."""


def split_cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def is_separator(cells):
    return set("".join(cells)) <= set("-: ")


def registry_rows(text, label):
    """Data rows of the `## Gates and probes` table (header excluded)."""
    lines = text.splitlines()
    start = None
    for i, line in enumerate(lines):
        if line.strip() == HEADING:
            start = i
            break
    if start is None:
        raise RegistryError("no '%s' heading in %s" % (HEADING, label))
    rows = []
    header_seen = False
    for i in range(start + 1, len(lines)):
        stripped = lines[i].lstrip()
        if stripped.startswith(H2) and i > start + 1:
            break
        if not ROW_PREFIX.match(lines[i]):
            continue
        cells = split_cells(lines[i])
        if len(cells) < 2:
            continue
        if is_separator(cells):
            continue
        if not header_seen:
            header_seen = True
            continue
        if len(cells) < MIN_CELLS and cells[KIND_CELL] in GATED_KINDS:
            raise RegistryError(
                "row with %d cells (< %d) at line %d of %s"
                % (len(cells), MIN_CELLS, i + 1, label))
        rows.append({
            "name": cells[0],
            "kind": cells[KIND_CELL],
            "entry": cells[ENTRY_CELL] if len(cells) > ENTRY_CELL else "",
            "line": i + 1,
        })
    return rows


def glob_paths(root, parts):
    out = []
    for path in glob.glob(os.path.join(root, *parts)):
        if os.path.isfile(path):
            out.append(os.path.relpath(path, root).replace(os.sep, "/"))
    return sorted(out)


def evaluate(root, registry):
    if not os.path.isfile(registry):
        raise RegistryError("registry not found: %s" % registry)
    try:
        with open(registry, encoding="utf-8") as f:
            text = f.read()
    except (OSError, UnicodeError) as e:
        raise RegistryError("cannot read %s: %s" % (registry, e))
    rows = registry_rows(text, registry)
    instruments = glob_paths(root, INSTRUMENT_GLOB)
    tools = glob_paths(root, TOOLS_GLOB)
    entries = [r["entry"] for r in rows]

    def covered(path):
        return any(path in e for e in entries)

    missing = [p for p in instruments if not covered(p)]
    tools_without_rows = [p for p in tools if not covered(p)]
    dead = []
    for r in rows:
        for tok in TOKEN.findall(r["entry"]):
            if not os.path.isfile(os.path.join(root, tok)):
                dead.append({"row": r["name"], "path": tok})
    return {
        "instruments": instruments,
        "registered": [r["name"] for r in rows],
        "missing": missing,
        "dead": dead,
        "rows": len(rows),
        "tools_without_rows": tools_without_rows,
    }


SUMMARY = "GATE-REGISTRY: %d missing / %d registered / %d instruments / %d dead"


def report_lines(res):
    lines = [SUMMARY % (len(res["missing"]), res["rows"],
                        len(res["instruments"]), len(res["dead"]))]
    lines.extend("MISSING " + p for p in res["missing"])
    lines.extend("DEAD %s %s" % (d["row"], d["path"]) for d in res["dead"])
    lines.append("GATE-REGISTRY-INFO: %d tools without a row"
                 % len(res["tools_without_rows"]))
    return lines


class Parser(argparse.ArgumentParser):
    def error(self, message):
        print("GATE-REGISTRY-ERROR %s" % message)
        raise SystemExit(2)


def main(argv=None):
    p = Parser(prog="check-gate-registry.py",
               description="Gate-registry coverage auditor (round 83, claim O).")
    p.add_argument("--root", default=".",
                   help="tree root to audit (default: current directory)")
    p.add_argument("--registry", default=None,
                   help="registry file (default: <root>/SKILL.md)")
    p.add_argument("--json", action="store_true",
                   help="print one JSON object instead of the plain report")
    p.add_argument("--selftest", action="store_true",
                   help="run the fixture selftest battery")
    a = p.parse_args(argv)
    if a.selftest:
        try:
            return selftest()
        except Exception as e:  # could-not-evaluate, never a traceback
            print("GATE-REGISTRY-ERROR selftest could not run: %s" % e)
            return 2
    registry = a.registry if a.registry is not None else os.path.join(a.root, "SKILL.md")
    try:
        res = evaluate(a.root, registry)
    except RegistryError as e:
        print("GATE-REGISTRY-ERROR %s" % e)
        return 2
    except Exception as e:  # never a traceback
        print("GATE-REGISTRY-ERROR unexpected: %s" % e)
        return 2
    if a.json:
        print(json.dumps(res))
    else:
        for line in report_lines(res):
            print(line)
    return 0 if not res["missing"] and not res["dead"] else 1


TOOL = os.path.abspath(__file__)
TABLE_HEAD = ("| name | kind | entry command | verdict map | self-test | "
              "pinned values | write scope | owner |")
TABLE_SEP = "|---|---|---|---|---|---|---|---|"


def write_fixture(root, rel, content):
    path = os.path.join(root, rel)
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    mode = "wb" if isinstance(content, bytes) else "w"
    with open(path, mode) as f:
        f.write(content)


def registry_text(entries):
    lines = ["# fixture", "", HEADING, "", TABLE_HEAD, TABLE_SEP]
    for indent, row in entries:
        lines.append(" " * indent + row)
    return "\n".join(lines) + "\n"


def row(name, entry, kind="gate", verdict="0 pass / 1 fail"):
    return "| %s | %s | `%s` | %s | — | — | read-only | fixture |" % (
        name, kind, entry, verdict)


def run_tool(args, cwd):
    env = dict(os.environ)
    env.pop("PYTHONPATH", None)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    r = subprocess.run([sys.executable, "-B", TOOL] + list(args),
                       capture_output=True, cwd=cwd, env=env)
    return (r.returncode,
            r.stdout.decode("utf-8", "replace"),
            r.stderr.decode("utf-8", "replace"))


def selftest():
    checks = []

    def check(name, cond, detail=""):
        checks.append((name, bool(cond), detail))

    tmp = tempfile.mkdtemp(prefix="gate-registry-selftest-")
    try:
        # 1. clean registry: exact summary text, one summary line, exit 0
        d = os.path.join(tmp, "clean")
        write_fixture(d, "reports/round-1/accept-a.py", "")
        write_fixture(d, "SKILL.md", registry_text(
            [(0, row("accept-a-1", "python3 reports/round-1/accept-a.py"))]))
        rc, out, err = run_tool(["--root", d], d)
        lines = out.splitlines()
        summary_hits = [l for l in lines if l.startswith("GATE-REGISTRY: ")]
        check("clean-registry",
              rc == 0
              and lines[0] == "GATE-REGISTRY: 0 missing / 1 registered / 1 instruments / 0 dead"
              and len(summary_hits) == 1,
              "rc=%d first=%r" % (rc, lines[0] if lines else ""))

        # 2. one missing instrument: exit 1, MISSING line, summary counts
        d = os.path.join(tmp, "missing")
        write_fixture(d, "reports/round-2/accept-b.py", "")
        write_fixture(d, "SKILL.md", registry_text([]))
        rc, out, err = run_tool(["--root", d], d)
        check("one-missing",
              rc == 1
              and "MISSING reports/round-2/accept-b.py" in out.splitlines()
              and out.splitlines()[0]
              == "GATE-REGISTRY: 1 missing / 0 registered / 1 instruments / 0 dead",
              "rc=%d" % rc)

        # 3. dead token: exit 1, DEAD line names row and path
        d = os.path.join(tmp, "dead")
        write_fixture(d, "reports/round-1/accept-a.py", "")
        write_fixture(d, "SKILL.md", registry_text(
            [(0, row("gate-1", "python3 reports/round-1/accept-a.py tools/absent.py"))]))
        rc, out, err = run_tool(["--root", d], d)
        check("dead-token",
              rc == 1
              and "DEAD gate-1 tools/absent.py" in out.splitlines()
              and "/ 1 dead" in out.splitlines()[0],
              "rc=%d" % rc)

        # 4. short gate row: could-not-evaluate (exit 2), no traceback
        d = os.path.join(tmp, "shortrow")
        write_fixture(d, "reports/round-1/accept-a.py", "")
        write_fixture(d, "SKILL.md", registry_text(
            [(0, "| short | gate | `x` | y |")]))
        rc, out, err = run_tool(["--root", d], d)
        check("short-gate-row",
              rc == 2 and "GATE-REGISTRY-ERROR" in out
              and "Traceback" not in out + err,
              "rc=%d" % rc)

        # 5. absent registry file: exit 2 with GATE-REGISTRY-ERROR
        d = os.path.join(tmp, "noreg")
        write_fixture(d, "reports/round-1/accept-a.py", "")
        rc, out, err = run_tool(["--root", d], d)
        check("absent-registry",
              rc == 2 and "GATE-REGISTRY-ERROR" in out,
              "rc=%d" % rc)

        # 6. absent heading: exit 2, message names the heading
        d = os.path.join(tmp, "nohead")
        write_fixture(d, "reports/round-1/accept-a.py", "")
        write_fixture(d, "SKILL.md", "# fixture\n\n## Other\n\ntext\n")
        rc, out, err = run_tool(["--root", d], d)
        check("absent-heading",
              rc == 2 and "GATE-REGISTRY-ERROR" in out
              and "Gates and probes" in out,
              "rc=%d" % rc)

        # 7. rows indented 0-3 spaces are accepted
        d = os.path.join(tmp, "indents")
        entries = []
        for i, n in enumerate("abcd"):
            write_fixture(d, "reports/round-%d/accept-%s.py" % (i + 1, n), "")
            entries.append((i, row("accept-%s" % n,
                                   "python3 reports/round-%d/accept-%s.py" % (i + 1, n))))
        write_fixture(d, "SKILL.md", registry_text(entries))
        rc, out, err = run_tool(["--root", d], d)
        check("indented-rows-0-3",
              rc == 0 and " 0 missing /" in out.splitlines()[0],
              "rc=%d" % rc)

        # 8. a 4-space row is ignored (markdown code block)
        d = os.path.join(tmp, "fourspace")
        write_fixture(d, "reports/round-1/accept-a.py", "")
        write_fixture(d, "SKILL.md", registry_text(
            [(4, row("accept-a-1", "python3 reports/round-1/accept-a.py"))]))
        rc, out, err = run_tool(["--root", d], d)
        check("four-space-row-ignored",
              rc == 1 and "MISSING reports/round-1/accept-a.py" in out.splitlines()
              and "/ 0 registered /" in out.splitlines()[0],
              "rc=%d" % rc)

        # 9. --json: whole stdout is one JSON object with the frozen keys
        d = os.path.join(tmp, "jsonshape")
        write_fixture(d, "reports/round-1/accept-a.py", "")
        write_fixture(d, "SKILL.md", registry_text(
            [(0, row("accept-a-1", "python3 reports/round-1/accept-a.py"))]))
        rc, out, err = run_tool(["--root", d, "--json"], d)
        try:
            js = json.loads(out)
            shape = (rc == 0 and set(js) == {"instruments", "registered", "missing",
                                             "dead", "rows", "tools_without_rows"}
                     and js["instruments"] == ["reports/round-1/accept-a.py"]
                     and js["registered"] == ["accept-a-1"] and js["rows"] == 1
                     and js["missing"] == [] and js["dead"] == []
                     and js["tools_without_rows"] == [])
        except ValueError:
            shape = False
        check("json-shape", shape, "rc=%d" % rc)

        # 10. info line counts tools/*.py without a row; never affects exit
        d = os.path.join(tmp, "infoline")
        write_fixture(d, "reports/round-1/accept-a.py", "")
        write_fixture(d, "tools/loose.py", "")
        write_fixture(d, "SKILL.md", registry_text(
            [(0, row("accept-a-1", "python3 reports/round-1/accept-a.py"))]))
        rc, out, err = run_tool(["--root", d], d)
        check("info-line",
              rc == 0
              and "GATE-REGISTRY-INFO: 1 tools without a row" in out.splitlines(),
              "rc=%d" % rc)

        # 11. malformed registry bytes: exit 2, no traceback
        d = os.path.join(tmp, "garbage")
        write_fixture(d, "reports/round-1/accept-a.py", "")
        write_fixture(d, "SKILL.md",
                      b"# t\n\n" + HEADING.encode("ascii")
                      + b"\n\n| a |\n\xff\xfebinary\n")
        rc, out, err = run_tool(["--root", d], d)
        check("malformed-no-traceback",
              rc == 2 and "GATE-REGISTRY-ERROR" in out
              and "Traceback" not in out + err,
              "rc=%d" % rc)

        # 12. dead forces exit 1 even when nothing is missing
        d = os.path.join(tmp, "deadonly")
        write_fixture(d, "reports/round-1/accept-a.py", "")
        write_fixture(d, "SKILL.md", registry_text(
            [(0, row("accept-a-1", "python3 reports/round-1/accept-a.py tools/gone.py"))]))
        rc, out, err = run_tool(["--root", d], d)
        check("dead-exit1",
              rc == 1 and " 0 missing /" in out.splitlines()[0]
              and "/ 1 dead" in out.splitlines()[0],
              "rc=%d" % rc)

        # 13. header and separator are not counted as rows
        d = os.path.join(tmp, "headcount")
        write_fixture(d, "reports/round-1/accept-a.py", "")
        write_fixture(d, "SKILL.md", registry_text(
            [(0, row("accept-a-1", "python3 reports/round-1/accept-a.py"))]))
        rc, out, err = run_tool(["--root", d], d)
        check("header-not-counted",
              rc == 0 and "/ 1 registered /" in out.splitlines()[0],
              "rc=%d" % rc)

        # 14. the section ends at the next H2; short tables later are ignored
        d = os.path.join(tmp, "nextsection")
        write_fixture(d, "reports/round-1/accept-a.py", "")
        write_fixture(d, "SKILL.md", registry_text(
            [(0, row("accept-a-1", "python3 reports/round-1/accept-a.py"))])
            + "\n## Other\n\n| x | y | z |\n|---|---|---|\n| 1 | 2 | 3 |\n")
        rc, out, err = run_tool(["--root", d], d)
        check("section-ends-at-next-h2",
              rc == 0 and "/ 1 registered /" in out.splitlines()[0],
              "rc=%d" % rc)

        # 15. a short note-kind row is legal and counted (kind-gated cell floor)
        d = os.path.join(tmp, "noterow")
        write_fixture(d, "reports/round-1/accept-a.py", "")
        write_fixture(d, "SKILL.md", registry_text(
            [(0, row("accept-a-1", "python3 reports/round-1/accept-a.py")),
             (0, "| corrections | note | — | prose only |")]))
        rc, out, err = run_tool(["--root", d], d)
        check("note-row-short-legal",
              rc == 0 and "/ 2 registered /" in out.splitlines()[0],
              "rc=%d" % rc)

        # 16. a literal | inside a later cell does not move the entry command
        d = os.path.join(tmp, "straypipe")
        write_fixture(d, "reports/round-1/accept-a.py", "")
        write_fixture(d, "SKILL.md", registry_text(
            [(0, row("accept-a-1", "python3 reports/round-1/accept-a.py",
                     verdict="ends `PASS|FAIL`; exit 0/1"))]))
        rc, out, err = run_tool(["--root", d], d)
        check("stray-pipe-entry-cell-stable",
              rc == 0 and " 0 missing /" in out.splitlines()[0],
              "rc=%d" % rc)

        # 17. two dead tokens on one row: two DEAD lines, dead count 2
        d = os.path.join(tmp, "twodead")
        write_fixture(d, "reports/round-1/accept-a.py", "")
        write_fixture(d, "SKILL.md", registry_text(
            [(0, row("gate-x", "python3 tools/a.py tools/b.py"))]))
        rc, out, err = run_tool(["--root", d], d)
        check("multiple-dead-tokens",
              rc == 1 and "DEAD gate-x tools/a.py" in out.splitlines()
              and "DEAD gate-x tools/b.py" in out.splitlines()
              and "/ 2 dead" in out.splitlines()[0],
              "rc=%d" % rc)

        # 18. missing lines and the instrument list are sorted
        d = os.path.join(tmp, "sorted")
        write_fixture(d, "reports/round-2/accept-b.py", "")
        write_fixture(d, "reports/round-1/accept-a.py", "")
        write_fixture(d, "SKILL.md", registry_text([]))
        rc, out, err = run_tool(["--root", d], d)
        missing_lines = [l for l in out.splitlines() if l.startswith("MISSING ")]
        check("sorted-output",
              rc == 1 and missing_lines
              == ["MISSING reports/round-1/accept-a.py",
                  "MISSING reports/round-2/accept-b.py"],
              "rc=%d" % rc)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    total = len(checks)
    failed = [c for c in checks if not c[1]]
    for name, ok, detail in checks:
        print("CHECK %-28s %s%s" % (name, "PASS" if ok else "FAIL",
                                    "" if ok else " -- " + detail))
    if not failed:
        print("SELFTEST: PASS (%d checks)" % total)
        return 0
    print("SELFTEST: FAIL (%d of %d checks failed: %s)"
          % (len(failed), total, ", ".join(n for n, ok, _ in failed)))
    return 1


if __name__ == "__main__":
    sys.exit(main())
