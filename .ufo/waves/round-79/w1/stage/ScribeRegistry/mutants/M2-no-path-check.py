#!/usr/bin/env python3
"""Draft SKILL.md gate/probe registry-row schema checker (round-79 W1, ScribeRegistry).

Read-only. Parses every markdown table whose header is exactly the registry header
`| name | kind | entry command | verdict map | self-test | pinned values | write scope | owner |`
and grades each body row against the required fields below.

Usage:
  skill-row-check.py --skill <file> [--root <repo> [--rev <40hex>]] [--rows NAME[,NAME...]]
  skill-row-check.py --selftest <fixtures-dir>

  --skill  markdown file to read (for committed bytes: write `git show <rev>:SKILL.md` to a scratch file first)
  --root   repository used to check that a command's script path exists
  --rev    with --root: existence is `git -C <root> cat-file -e <rev>:<path>` (committed bytes);
           without --rev: existence is a working-tree file test under --root (selftest fixtures)
  --rows   grade only the named rows (default: every row)

Exit: 0 every graded row passes; 1 at least one finding; 2 unusable input.
Last line: `REGISTRY-ROWS: PASS rows=<n>` or `REGISTRY-ROWS: FAIL rows=<n> findings=<m>`.

Required fields (non-empty; for gate/probe rows a bare dash counts as empty):
  name           unique within the file
  kind           starts with gate | probe | note (note rows exempt from the tool fields)
  entry command  gate/probe: a `python3 [-B] <path>` or `sh` command whose script path exists
  verdict map    contains the exit codes 0, 1 and 2 as standalone numbers
  self-test      gate/probe: a `--selftest` command, or a parenthesised reason that no selftest exists
  pinned values  gate/probe: non-empty, not a bare dash
  write scope    names how the row writes (read-only, scratch, regenerates, ...)
  owner          non-empty

Finding codes: SHAPE NAME-EMPTY NAME-DUP KIND CMD-EMPTY CMD-NOT-PYTHON CMD-PATH-ABSENT
VERDICT-NOCODES SELFTEST-BARE PINNED-BARE WRITE-EMPTY WRITE-NOSCOPE OWNER-EMPTY
Limits: checks shape and presence only. It does not run the commands, does not confirm that the
verdict map matches the script's real exit codes, and does not check pinned values for correctness.
"""
import argparse
import json
import os
import re
import subprocess
import sys

HEADER = ["name", "kind", "entry command", "verdict map", "self-test",
          "pinned values", "write scope", "owner"]
DASH = {"—", "-", "–", ""}
WRITE_WORDS = re.compile(
    r"read-only|scratch|writes?\b|regenerat|tempfile|temp|clone|disposable|"
    r"materiali[sz]ed|auto-cleaned|default mode|in place", re.I)
PY_CMD = re.compile(r"(?:python3?|sh)\s+(?:-[A-Za-z]+\s+)*(?:-c\s+)?(\S+)")
CODE_SPAN = re.compile(r"`([^`]*)`")
EXIT_CODE = {d: re.compile(r"(?<![\w.])%s(?![\w.])" % d) for d in "012"}


def split_row(line):
    """GFM split: an unescaped pipe always separates cells, even inside a code span."""
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|") and not s.endswith("\\|"):
        s = s[:-1]
    return [c.replace("\\|", "|").strip() for c in re.split(r"(?<!\\)\|", s)]


def is_sep(line):
    return bool(re.match(r"^\|?\s*:?-{3,}:?(\s*\|\s*:?-{3,}:?)*\s*\|?\s*$", line.strip()))


def parse_tables(text):
    """Return a list of ("T", table_no, header_line) and ("R", table_no, line_no, cells)."""
    lines = text.splitlines()
    out = []
    table_no = 0
    i = 0
    while i < len(lines):
        if lines[i].strip().startswith("|") and split_row(lines[i]) == HEADER:
            table_no += 1
            out.append(("T", table_no, i + 1))
            j = i + 1
            if j < len(lines) and is_sep(lines[j]):
                j += 1
            while j < len(lines) and lines[j].strip().startswith("|"):
                out.append(("R", table_no, j + 1, split_row(lines[j])))
                j += 1
            i = j
            continue
        i += 1
    return out


def path_exists(args, path):
    if args.rev:
        r = subprocess.run(["git", "-C", args.root, "cat-file", "-e", f"{args.rev}:{path}"],
                           capture_output=True, text=True)
        return r.returncode == 0
    return os.path.isfile(os.path.join(args.root, path))


def grade(args, cells, names_seen):
    if len(cells) != 8:
        return [f"SHAPE({len(cells)})"]
    name, kind, cmd, verdict, selftest, pinned, write, owner = cells
    findings = []
    if not name:
        findings.append("NAME-EMPTY")
    elif name in names_seen:
        findings.append("NAME-DUP")
    names_seen.add(name)
    kind_ok = bool(re.match(r"(gate|probe|note)\b", kind))
    if not kind_ok:
        findings.append("KIND")
    is_tool = not kind.startswith("note")
    if is_tool:
        if cmd in DASH:
            findings.append("CMD-EMPTY")
        else:
            spans = CODE_SPAN.findall(cmd) or [cmd]
            m = None
            for s in spans:
                m = PY_CMD.search(s)
                if m:
                    break
            if not m:
                findings.append("CMD-NOT-PYTHON")
            elif False:
                findings.append(f"CMD-PATH-ABSENT({m.group(1)})")
    if is_tool and not all(EXIT_CODE[d].search(verdict) for d in "012"):
        findings.append("VERDICT-NOCODES")
    if is_tool and selftest in DASH:
        findings.append("SELFTEST-BARE")
    if is_tool and pinned in DASH:
        findings.append("PINNED-BARE")
    if is_tool and write in DASH:
        findings.append("WRITE-EMPTY")
    elif is_tool and not WRITE_WORDS.search(write):
        findings.append("WRITE-NOSCOPE")
    if owner in DASH:
        findings.append("OWNER-EMPTY")
    return findings


def run(args):
    try:
        with open(args.skill, encoding="utf-8") as fh:
            text = fh.read()
    except OSError as exc:
        print(f"ERROR: cannot read {args.skill}: {exc}", file=sys.stderr)
        return 2
    if args.rev and not re.fullmatch(r"[0-9a-f]{40}", args.rev):
        print("ERROR: --rev must be a 40-hex commit", file=sys.stderr)
        return 2
    if args.rev and not args.root:
        print("ERROR: --rev requires --root", file=sys.stderr)
        return 2
    items = parse_tables(text)
    if not any(it[0] == "T" for it in items):
        print("ERROR: no registry table with the required header found", file=sys.stderr)
        return 2
    wanted = set(args.rows.split(",")) if args.rows else None
    names_seen = set()
    graded = 0
    total = 0
    codes = {}
    for it in items:
        if it[0] == "T":
            print(f"TABLE {it[1]} header_line={it[2]}")
            continue
        _, table_no, line_no, cells = it
        name = cells[0] if cells else ""
        if wanted is not None and name not in wanted:
            names_seen.add(name)
            continue
        graded += 1
        f = grade(args, cells, names_seen)
        total += len(f)
        for c in f:
            key = re.sub(r"\(.*", "", c)
            codes[key] = codes.get(key, 0) + 1
        status = "OK" if not f else "FINDING"
        print(f"ROW {status} table={table_no} line={line_no} name={name!r} "
              f"cells={len(cells)} findings={','.join(f) if f else '-'}")
    print("CODES " + (",".join(f"{k}={v}" for k, v in sorted(codes.items())) or "-"))
    if graded == 0:
        print("ERROR: no rows graded", file=sys.stderr)
        return 2
    if total == 0:
        print(f"REGISTRY-ROWS: PASS rows={graded}")
        return 0
    print(f"REGISTRY-ROWS: FAIL rows={graded} findings={total}")
    return 1


def selftest(fixtures):
    """Run each fixture and compare exit, verdict and finding codes with expected.json."""
    spec_path = os.path.join(fixtures, "expected.json")
    try:
        with open(spec_path, encoding="utf-8") as fh:
            spec = json.load(fh)
    except (OSError, ValueError) as exc:
        print(f"ERROR: cannot read {spec_path}: {exc}", file=sys.stderr)
        return 2
    passed = 0
    for case in spec["cases"]:
        cmd = [sys.executable, os.path.abspath(__file__),
               "--skill", os.path.join(fixtures, case["skill"])]
        if case.get("root"):
            cmd += ["--root", os.path.join(fixtures, "tree")]
        proc = subprocess.run(cmd, capture_output=True, text=True)
        out = proc.stdout
        verdict_line = next((ln for ln in out.splitlines() if ln.startswith("REGISTRY-ROWS:")), "")
        got_verdict = verdict_line.split()[1].rstrip(":") if verdict_line else "NONE"
        got_codes = set()
        for ln in (x for x in out.splitlines() if x.startswith("ROW ")):
            m = re.search(r" findings=(\S+)$", ln)
            if m and m.group(1) != "-":
                got_codes |= {re.sub(r"\(.*", "", c) for c in m.group(1).split(",")}
        ok = (proc.returncode == case["exit"] and got_verdict == case["verdict"]
              and sorted(got_codes) == sorted(case["codes"]))
        passed += ok
        print(f"CASE {case['id']}: {'PASS' if ok else 'FAIL'} exit={proc.returncode} "
              f"verdict={got_verdict} codes={','.join(sorted(got_codes)) or '-'} "
              f"expected=exit {case['exit']} {case['verdict']} "
              f"{','.join(sorted(case['codes'])) or '-'}")
    n = len(spec["cases"])
    print(f"SELFTEST: {passed}/{n}")
    return 0 if passed == n else 1


def main(argv=None):
    ap = argparse.ArgumentParser(description="SKILL registry row schema checker (draft).")
    ap.add_argument("--skill")
    ap.add_argument("--root")
    ap.add_argument("--rev")
    ap.add_argument("--rows")
    ap.add_argument("--selftest", metavar="FIXTURES_DIR")
    args = ap.parse_args(argv)
    if args.selftest:
        return selftest(args.selftest)
    if not args.skill:
        ap.error("--skill is required")
    return run(args)


if __name__ == "__main__":
    sys.exit(main())
