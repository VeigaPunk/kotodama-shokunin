#!/usr/bin/env python3
"""Heading-count control for corpus/README.md (round 48, claim Ca).

The round-28 index sweep (`reports/round-28/readme/sweep.py`) checks rows,
section counts, the totals line and the counts footer. It has no heading leg:
a duplicated H1 passes every existing check, which is why the live README
carried `# kotodama-shokunin corpus index` at both lines 1 and 3 while the
sweep stayed green.

The sweep is filed round-28 bytes and is not editable; this control is its
sibling. It reads one Markdown file, counts ATX headings outside fenced code
blocks, and asserts:

  * exactly one level-1 heading (`^# `); duplicates are reported with lines
  * that H1 is the first non-blank line of the file
  * no two headings of the same level share the same text

Stdlib only. Read-only: no network, no writes, no eval/exec.

Usage:
  python3 tools/check-readme-heading.py
  python3 tools/check-readme-heading.py --readme <path> [--json]
  python3 tools/check-readme-heading.py --selftest

Exit codes: 0 = clean, 1 = finding present, 2 = could-not-evaluate (missing or
unreadable input, usage error). Unexpected internal failures print a JSON
object with `ok: null` and exit 2; no traceback is printed.
"""
import argparse
import hashlib
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.abspath(os.path.join(HERE, ".."))
DEFAULT_README = os.path.join(LANE, "corpus", "README.md")

HEADING_RE = re.compile(r"^(#{1,6})[ \t]+(.*?)[ \t]*$")
FENCE_RE = re.compile(r"^[ ]{0,3}(`{3,}|~{3,})")

# Stable diagnostic ids.
H1_ABSENT = "H1-ABSENT"
H1_COUNT = "H1-COUNT"
H1_NOT_FIRST = "H1-NOT-FIRST"
HEADING_DUP = "HEADING-DUP"


def headings(text):
    """ATX headings outside fenced code blocks: [(line_no, level, text)]."""
    out = []
    fence = None
    for i, raw in enumerate(text.splitlines(), 1):
        line = raw.rstrip("\r")
        m = FENCE_RE.match(line)
        if m:
            marker = m.group(1)[0]
            if fence is None:
                fence = marker
            elif fence == marker:
                fence = None
            continue
        if fence is not None:
            continue
        h = HEADING_RE.match(line)
        if h:
            out.append((i, len(h.group(1)), h.group(2).strip()))
    return out


def evaluate_text(text):
    """Measure one README string. Pure: no IO."""
    hs = headings(text)
    h1 = [(n, t) for n, lvl, t in hs if lvl == 1]
    findings = []

    if not h1:
        findings.append({"class": H1_ABSENT, "detail": "no level-1 heading", "lines": []})
    elif len(h1) > 1:
        findings.append(
            {
                "class": H1_COUNT,
                "detail": "expected exactly 1 level-1 heading, found %d" % len(h1),
                "lines": [n for n, _ in h1],
                "texts": [t for _, t in h1],
            }
        )

    lines = text.splitlines()
    first = next((i for i, ln in enumerate(lines, 1) if ln.strip()), None)
    if h1 and first != h1[0][0]:
        findings.append(
            {
                "class": H1_NOT_FIRST,
                "detail": "first non-blank line is %s, first H1 is line %d"
                % (first, h1[0][0]),
                "lines": [first, h1[0][0]] if first is not None else [h1[0][0]],
            }
        )

    by_level = {}
    for n, lvl, t in hs:
        by_level.setdefault(lvl, {}).setdefault(t, []).append(n)
    for lvl, texts in sorted(by_level.items()):
        if lvl == 1:
            continue  # H1-COUNT already reports the whole level
        for t, ns in texts.items():
            if len(ns) > 1:
                findings.append(
                    {
                        "class": HEADING_DUP,
                        "detail": "level-%d heading %r repeated" % (lvl, t),
                        "lines": ns,
                    }
                )

    return {
        "ok": not findings,
        "findings": findings,
        "h1": h1,
        "h1_lines": [n for n, _ in h1],
        "heading_count": len(hs),
        "headings_by_level": {
            str(lvl): sum(1 for _, l, _ in hs if l == lvl) for lvl in sorted(by_level)
        },
    }


def receipt(path, text, result):
    result = dict(result)
    result["readme"] = path
    result["sha256"] = hashlib.sha256(text.encode("utf-8")).hexdigest()
    return result


def selftest():
    ok = True

    def check(name, cond, detail=""):
        nonlocal ok
        if not cond:
            ok = False
        print(("PASS " if cond else "FAIL ") + name + (" " + detail if detail else ""))

    # 1. one H1 first -> clean
    r = evaluate_text("# title\n\nbody\n")
    check("control: single leading H1 passes", r["ok"] is True, json.dumps(r["findings"]))

    # 2. the live defect shape -> flagged with both lines
    r = evaluate_text("# title\n\n# title\n\nrevision: 2.4\n")
    f = [x for x in r["findings"] if x["class"] == H1_COUNT]
    check(
        "control: duplicate H1 flagged at [1, 3]",
        len(f) == 1 and f[0]["lines"] == [1, 3],
        json.dumps(r["findings"]),
    )

    # 3. no H1 -> flagged
    r = evaluate_text("## section\n\nbody\n")
    check(
        "control: absent H1 flagged",
        [x["class"] for x in r["findings"]] == [H1_ABSENT],
        json.dumps(r["findings"]),
    )

    # 4. H1 after content -> flagged
    r = evaluate_text("preamble\n\n# title\n")
    check(
        "control: H1 after content flagged",
        any(x["class"] == H1_NOT_FIRST for x in r["findings"]),
        json.dumps(r["findings"]),
    )

    # 5. '#nospace' is not an ATX heading
    r = evaluate_text("# title\n\n#nospace\n")
    check(
        "control: '#nospace' not counted",
        r["ok"] is True and r["heading_count"] == 1,
        json.dumps(r),
    )

    # 6. a heading inside a fenced block is not counted
    r = evaluate_text("# title\n\n```\n# not a heading\n```\n")
    check(
        "control: fenced '# ' ignored",
        r["ok"] is True and r["heading_count"] == 1,
        json.dumps(r),
    )

    # 7. duplicate H2 -> flagged
    r = evaluate_text("# title\n\n## a\n\n## a\n")
    check(
        "control: duplicate H2 flagged",
        any(x["class"] == HEADING_DUP for x in r["findings"]),
        json.dumps(r["findings"]),
    )

    # 8. level counts are reported
    r = evaluate_text("# title\n\n## a\n\n### b\n")
    check(
        "control: level counts reported",
        r["headings_by_level"] == {"1": 1, "2": 1, "3": 1},
        json.dumps(r["headings_by_level"]),
    )

    return ok


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--readme", default=DEFAULT_README)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args(argv)

    if args.selftest:
        passed = selftest()
        print("selftest: %s" % ("8/8 checks passed" if passed else "FAILED"))
        return 0 if passed else 1

    try:
        with open(args.readme, encoding="utf-8") as fh:
            text = fh.read()
        result = receipt(args.readme, text, evaluate_text(text))
    except (OSError, UnicodeDecodeError) as exc:
        print(json.dumps({"ok": None, "error": repr(exc), "readme": args.readme}))
        return 2

    if args.json:
        print(json.dumps(result, indent=1, sort_keys=True))
    else:
        print("readme %s" % result["readme"])
        print("sha256 %s" % result["sha256"])
        print("h1_lines %s" % result["h1_lines"])
        print("headings %s" % json.dumps(result["headings_by_level"], sort_keys=True))
        print("findings %d" % len(result["findings"]))
        for f in result["findings"]:
            print("  %s lines=%s %s" % (f["class"], f["lines"], f["detail"]))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
