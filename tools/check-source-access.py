#!/usr/bin/env python3
"""Ordinary-access check for corpus/SOURCES.md (QUALITY criterion 10, round 52).

A registry row whose source, anchor or teaches cell records that the source was
reached by getting past an access control (a headless browser, a solved captcha
or bot challenge, a bypassed paywall or login) counts as unopened. Such a row
supports nothing:

  * status leg: the row's status must be `rejected`;
  * cited leg: no corpus/knowledge entry may cite the row's S-id.

A row that met a challenge and was then read through an ordinary route (for
example a Wayback capture) does not carry a bypass marker and is not flagged.

Usage:
  python3 -B tools/check-source-access.py [--root LANE_ROOT] [--sources PATH]
  python3 -B tools/check-source-access.py --selftest

Output: one line per finding, then `ACCESS: <flagged> flagged rows, <n> findings`.
  ACCESS_FINDING status <S-id> <status>
  ACCESS_FINDING cited <S-id> <path>:<line>
Exit codes: 0 no findings; 1 findings; 2 could not evaluate (stderr
ACCESS_INPUT_ERROR). Read-only, stdlib only.
"""
import argparse
import os
import re
import sys
import tempfile

ROW = re.compile(r"^\|\s*(S\d{3,})\s*\|")
BYPASS = re.compile(
    r"\bheadless\b|\bbypass(?:ed|ing)?\b|\bsolved (?:a |the )?(?:bot )?(?:captcha|challenge)\b",
    re.IGNORECASE,
)


def parse_rows(text):
    rows = []
    for number, line in enumerate(text.splitlines(), 1):
        match = ROW.match(line)
        if not match:
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) != 11:
            raise ValueError(f"row {match.group(1)} at line {number} has {len(cells)} cells, not 11")
        rows.append({"id": cells[0], "source": cells[1], "anchor": cells[5],
                     "teaches": cells[6], "status": cells[7]})
    return rows


def flagged(rows):
    return [r for r in rows if BYPASS.search(" ".join((r["source"], r["anchor"], r["teaches"])))]


def check(root, sources):
    with open(sources, encoding="utf-8") as handle:
        rows = parse_rows(handle.read())
    if not rows:
        raise ValueError(f"no registry rows in {sources}")
    bad = flagged(rows)
    findings = []
    for row in bad:
        if row["status"] != "rejected":
            findings.append(f"ACCESS_FINDING status {row['id']} {row['status']}")
    ids = {row["id"] for row in bad}
    knowledge = os.path.join(root, "corpus", "knowledge")
    if not os.path.isdir(knowledge):
        raise ValueError(f"missing {knowledge}")
    if ids:
        cite = re.compile(r"\b(" + "|".join(sorted(ids)) + r")\b")
        for folder, _dirs, files in sorted(os.walk(knowledge)):
            for name in sorted(files):
                if not name.endswith(".md"):
                    continue
                path = os.path.join(folder, name)
                with open(path, encoding="utf-8") as handle:
                    for number, line in enumerate(handle, 1):
                        for sid in sorted(set(cite.findall(line))):
                            rel = os.path.relpath(path, root)
                            findings.append(f"ACCESS_FINDING cited {sid} {rel}:{number}")
    return len(bad), findings


def run(root, sources):
    try:
        count, findings = check(root, sources)
    except (OSError, ValueError, UnicodeDecodeError) as error:
        print(f"ACCESS_INPUT_ERROR {error}", file=sys.stderr)
        return 2
    for line in findings:
        print(line)
    print(f"ACCESS: {count} flagged rows, {len(findings)} findings")
    return 1 if findings else 0


HEAD = "| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |\n|---|---|---|---|---|---|---|---|---|---|---|\n"


def row(sid, source, teaches, status, anchor="p. 1"):
    return f"| {sid} | {source} | paper | A | s | {anchor} | {teaches} | {status} | 2026-10-22 | 365d | — |\n"


def selftest():
    cases = [
        # name, rows, knowledge text, expected exit, expected findings
        ("clean", row("S001", "A — https://a.example (opened by ordinary means)", "t", "mined"), "x (S001)\n", 0, 0),
        ("headless-mined", row("S001", "A — https://a.example (Cloudflare-gated, opened via headless browser)", "t", "mined"), "x\n", 1, 1),
        ("headless-rejected-uncited", row("S001", "A — https://a.example (opened via headless browser)", "t", "rejected"), "x\n", 0, 0),
        ("headless-rejected-cited", row("S001", "A — https://a.example (opened via headless browser)", "t", "rejected"), "x (S001)\ny S001\n", 1, 2),
        ("wayback-after-challenge", row("S001", "A — https://a.example (direct page served a JS challenge; read via Wayback capture)", "t", "mined"), "x (S001)\n", 0, 0),
        ("wayback-after-live-captcha", row("S001", "A — https://a.example (live page CAPTCHA; read via Wayback captures)", "t", "mined"), "x (S001)\n", 0, 0),
        ("captcha-in-teaches", row("S001", "A — https://a.example", "solved a captcha to read", "queued"), "x\n", 1, 1),
        ("bypass-in-anchor", row("S001", "A — https://a.example", "t", "mined", anchor="paywall bypassed, p. 3"), "x\n", 1, 1),
        ("prefix-id-not-cited", row("S001", "A — https://a.example (headless)", "t", "rejected"), "x S0011 and S00\n", 0, 0),
    ]
    failures = 0
    for name, body, knowledge, want_exit, want_n in cases:
        with tempfile.TemporaryDirectory() as tmp:
            os.makedirs(os.path.join(tmp, "corpus", "knowledge", "p"))
            with open(os.path.join(tmp, "corpus", "SOURCES.md"), "w", encoding="utf-8") as handle:
                handle.write(HEAD + body)
            with open(os.path.join(tmp, "corpus", "knowledge", "p", "e.md"), "w", encoding="utf-8") as handle:
                handle.write(knowledge)
            _count, findings = check(tmp, os.path.join(tmp, "corpus", "SOURCES.md"))
            got_exit = 1 if findings else 0
            ok = got_exit == want_exit and len(findings) == want_n
            failures += not ok
            print(f"{'PASS' if ok else 'FAIL'} {name} exit={got_exit} findings={len(findings)}")
    with tempfile.TemporaryDirectory() as tmp:
        os.makedirs(os.path.join(tmp, "corpus", "knowledge"))
        with open(os.path.join(tmp, "corpus", "SOURCES.md"), "w", encoding="utf-8") as handle:
            handle.write(HEAD + "| S001 | short | row |\n")
        got = run(tmp, os.path.join(tmp, "corpus", "SOURCES.md"))
        ok = got == 2
        failures += not ok
        print(f"{'PASS' if ok else 'FAIL'} malformed-row exit={got}")
    print(f"SELFTEST: {10 - failures}/10 pass")
    return 1 if failures else 0


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--root", default=".")
    parser.add_argument("--sources")
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    if args.selftest:
        return selftest()
    sources = args.sources or os.path.join(args.root, "corpus", "SOURCES.md")
    return run(args.root, sources)


if __name__ == "__main__":
    sys.exit(main())
