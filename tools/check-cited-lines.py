#!/usr/bin/env python3
r"""Clause-scoping lint for cited lines (kotodama round 61, claim O; the R60-M6 routed fix).

A registered source id must scope the one clause it supports. A knowledge
bullet that carries two ids cites two sources for one sentence, and a table
row that carries any id hides its citation from every line-scoped check. This
tool reports both shapes so a packet can be repaired before it is scored.

Usage:
  python3 -B tools/check-cited-lines.py PATH [PATH ...]
  python3 -B tools/check-cited-lines.py --selftest

Each PATH is a file, or a directory walked recursively for files whose name
ends in `.md`. An S-id is a match of \bS\d{3,}\b. For each line of each file,
in line order, it prints

  MULTI-ID <path>:<lineno> <ids>   when the line carries two or more distinct S-ids
  TABLE-ID <path>:<lineno> <ids>   when the line, leading whitespace removed,
                                   starts with `|` and carries at least one S-id

`<ids>` is that line's distinct S-ids sorted by number and comma-joined with no
space; a line may give both findings, MULTI-ID first. The last stdout line is

  CITED-LINES: <k> finding(s) in <m> file(s)

where k counts findings, not lines (a table row carrying two ids is two), and
m counts the Markdown files read (a file argument counts as one).

Exit codes: 1 when k > 0; 0 when k = 0; 2, with a `CITED_LINES_ERROR` line on
stderr and nothing on stdout, when no PATH is given, a PATH does not exist, or
a file is unreadable or not valid UTF-8. `--selftest` runs the in-process cases
and ends with `selftest N/N`.

Read-only; stdlib only; the output depends only on the bytes read.
"""
import argparse
import contextlib
import io
import os
import re
import sys
import tempfile

SID = re.compile(r"\bS\d{3,}\b")
MULTI = "MULTI-ID"
TABLE = "TABLE-ID"


class InputError(Exception):
    """A path or file this tool cannot evaluate."""


def scan_line(line):
    """(kinds, ids) for one line: kinds in printing order, ids sorted by number."""
    ids = sorted(set(SID.findall(line)), key=lambda text: int(text[1:]))
    kinds = []
    if len(ids) >= 2:
        kinds.append(MULTI)
    if ids and line.lstrip().startswith("|"):
        kinds.append(TABLE)
    return kinds, ids


def scan_file(path, display):
    """Findings for one file as (kind, display, lineno, comma-joined ids)."""
    try:
        with open(path, "rb") as handle:
            raw = handle.read()
    except OSError as error:
        raise InputError(f"cannot read {display}: {error.strerror or error}") from None
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as error:
        raise InputError(f"{display} is not valid UTF-8: {error}") from None
    found = []
    for number, line in enumerate(text.splitlines(), 1):
        kinds, ids = scan_line(line)
        for kind in kinds:
            found.append((kind, display, number, ",".join(ids)))
    return found


def walk_markdown(top):
    """(file_path, display_path) for every `.md` file under `top`, deterministic."""
    for dirpath, dirnames, filenames in os.walk(top):
        dirnames.sort()
        for name in sorted(filenames):
            if not name.endswith(".md"):
                continue
            full = os.path.join(dirpath, name)
            yield full, os.path.normpath(os.path.join(top, os.path.relpath(full, top)))


def collect(paths):
    """(findings, Markdown file count) for the PATH arguments; raises InputError."""
    findings, files = [], 0
    for argument in paths:
        if not os.path.exists(argument):
            raise InputError(f"no such file or directory: {argument}")
        if os.path.isdir(argument):
            for full, display in walk_markdown(argument):
                files += 1
                findings.extend(scan_file(full, display))
        elif os.path.isfile(argument):
            files += 1
            findings.extend(scan_file(argument, os.path.normpath(argument)))
        else:
            raise InputError(f"not a regular file or directory: {argument}")
    return findings, files


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Report knowledge lines that carry several source ids, and table rows that carry one.",
        allow_abbrev=False,
    )
    parser.add_argument("--selftest", action="store_true", help="run the in-process cases")
    parser.add_argument("paths", nargs="*", metavar="PATH", help="file, or directory walked for *.md")
    args = parser.parse_args(argv)
    if args.selftest:
        if args.paths:
            print("CITED_LINES_ERROR --selftest takes no PATH", file=sys.stderr)
            return 2
        return run_selftest()
    if not args.paths:
        print("CITED_LINES_ERROR no PATH given", file=sys.stderr)
        return 2
    try:
        findings, files = collect(args.paths)
    except InputError as error:
        print(f"CITED_LINES_ERROR {error}", file=sys.stderr)
        return 2
    for kind, display, number, ids in findings:
        print(f"{kind} {display}:{number} {ids}")
    print(f"CITED-LINES: {len(findings)} finding(s) in {files} file(s)")
    return 1 if findings else 0


# --- selftest -----------------------------------------------------------------

LINE_CASES = [
    # name, line, expected [(kind, ids)] -- each expectation fails under a
    # plausible bug named beside it.
    ("multi-comma", "the row is cited (S612, S613) here.", [(MULTI, "S612,S613")]),
    ("multi-semicolon", "the row is cited S612; S613 here.", [(MULTI, "S612,S613")]),
    ("multi-slash", "the pair S612/S613 is cited.", [(MULTI, "S612,S613")]),
    ("multi-and", "the pair S612 and S613 is cited.", [(MULTI, "S612,S613")]),
    # A range is two ids at its ends, not one id and not its interior: fails a
    # tool that expands ranges or treats them as a single token.
    ("range-ascii", "the spread S612-S615 is cited.", [(MULTI, "S612,S615")]),
    ("range-endash", "the spread S612\u2013S615 is cited.", [(MULTI, "S612,S615")]),
    # Numeric sort: fails a lexical sort that would print S1000 before S652.
    ("sorted-numeric", "the pair S1000 and S652 is cited.", [(MULTI, "S652,S1000")]),
    ("sorted-numeric-four", "the set S700 S6120 S652 S613.", [(MULTI, "S613,S652,S700,S6120")]),
    # One distinct id repeated is not two citations: fails counting matches.
    ("repeated-one-id", "the row is cited S612 and again S612.", []),
    # Lookalikes and short ids: fails an unanchored or `\d+` regex.
    ("lookalikes", "tokens XS612, S612x, S612_, s612, S61 and S6 are not ids.", []),
    ("two-digit-only", "the pair S12 and S34 is not a citation.", []),
    ("table-leading-spaces", "   | S612 | sandal |", [(TABLE, "S612")]),
    ("table-leading-tab", "\t| S612 | sandal |", [(TABLE, "S612")]),
    # A table row with two ids gives both findings, MULTI-ID first.
    ("table-two-ids", "| S612 | S613 |", [(MULTI, "S612,S613"), (TABLE, "S612,S613")]),
    ("table-no-id", "| sandal | bare |", []),
    # A pipe after prose is not a table row: fails `"|" in line`.
    ("table-not-leading", "see | S612 | S613 |", [(MULTI, "S612,S613")]),
]


def _scan_line_view(line):
    kinds, ids = scan_line(line)
    return [(kind, ",".join(ids)) for kind in kinds]


def _cli(argv, cwd):
    """(exit, stdout, stderr) for main(argv) run with the process cwd at cwd."""
    out, err = io.StringIO(), io.StringIO()
    previous = os.getcwd()
    try:
        os.chdir(cwd)
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = main(argv)
    finally:
        os.chdir(previous)
    return code, out.getvalue(), err.getvalue()


def run_selftest():
    checks = []

    def check(name, expected, actual):
        ok = expected == actual
        checks.append(ok)
        print(f"{'PASS' if ok else 'FAIL'} {name}" + ("" if ok else f" want={expected!r} got={actual!r}"))

    for name, line, expected in LINE_CASES:
        check(name, expected, _scan_line_view(line))

    with tempfile.TemporaryDirectory(prefix="cited-lines-selftest-") as tmp:
        tree = os.path.join(tmp, "tree")
        os.makedirs(os.path.join(tree, "nest"))
        with open(os.path.join(tree, "one.md"), "w", encoding="utf-8") as handle:
            handle.write("- alpha cites S612\n- beta has no id\n")
        with open(os.path.join(tree, "two.md"), "w", encoding="utf-8") as handle:
            handle.write("intro line\n- beta cites (S612, S613)\n")
        with open(os.path.join(tree, "plain.txt"), "w", encoding="utf-8") as handle:
            handle.write("- gamma cites S612 S613 S614\n")
        with open(os.path.join(tree, "nest", "inner.md"), "w", encoding="utf-8") as handle:
            handle.write("| S612 | S613 |\n")
        # A clean file: at most one distinct id per line, no table row.
        with open(os.path.join(tmp, "clean.md"), "w", encoding="utf-8") as handle:
            handle.write("| bare | row |\n- one id S612\n- repeated S612 S612\n")
        broken = os.path.join(tmp, "broken")
        os.makedirs(broken)
        with open(os.path.join(broken, "bad.md"), "wb") as handle:
            handle.write(b"- ok S123\n- \xff\xfe broken S456 S789\n")
        crlf = os.path.join(tmp, "crlf.md")
        with open(crlf, "wb") as handle:
            handle.write(b"first line\r\nsecond line\r\n- cited S612 S613\r\n")

        check(
            "cli-single-file-clean",
            (0, "CITED-LINES: 0 finding(s) in 1 file(s)\n", ""),
            _cli(["clean.md"], tmp),
        )
        check(
            "cli-single-file-findings",
            (1, "MULTI-ID tree/two.md:2 S612,S613\nCITED-LINES: 1 finding(s) in 1 file(s)\n", ""),
            _cli(["tree/two.md"], tmp),
        )
        # Directory: `.txt` ignored, nested path joined, k counts findings (the
        # table row gives two) and m counts the three Markdown files.
        check(
            "cli-directory-md-only",
            (
                1,
                "MULTI-ID tree/two.md:2 S612,S613\n"
                "MULTI-ID tree/nest/inner.md:1 S612,S613\n"
                "TABLE-ID tree/nest/inner.md:1 S612,S613\n"
                "CITED-LINES: 3 finding(s) in 3 file(s)\n",
                "",
            ),
            _cli(["tree"], tmp),
        )
        # k is findings, not offending lines: fails a per-line counter.
        check(
            "cli-summary-counts-findings",
            (1, "MULTI-ID x.md:1 S612,S613\nTABLE-ID x.md:1 S612,S613\nCITED-LINES: 2 finding(s) in 1 file(s)\n", ""),
            (lambda: (_write(os.path.join(tmp, "x.md"), "| S612 | S613 |\n"), _cli(["x.md"], tmp))[1])(),
        )
        # CRLF keeps one line per line, numbered as the file reads.
        check(
            "cli-crlf-line-number",
            (1, "MULTI-ID crlf.md:3 S612,S613\nCITED-LINES: 1 finding(s) in 1 file(s)\n", ""),
            _cli(["crlf.md"], tmp),
        )
        for name, argv in (
            ("err-missing-path", ["no/such/file.md"]),
            ("err-no-path", []),
            ("err-invalid-utf8-file", ["broken/bad.md"]),
            ("err-invalid-utf8-in-directory", ["broken"]),
        ):
            code, out, err = _cli(argv, tmp)
            check(
                name,
                (2, "", True),
                (code, out, "CITED_LINES_ERROR" in err and err.startswith("CITED_LINES_ERROR ")),
            )
        check(
            "err-selftest-with-path",
            (2, "", True),
            (lambda got: (got[0], got[1], "CITED_LINES_ERROR" in got[2]))(_cli(["--selftest", "tree"], tmp)),
        )

    total = len(checks)
    passed = sum(checks)
    print(f"selftest {passed}/{total}")
    return 0 if passed == total else 1


def _write(path, text):
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    sys.exit(main())
