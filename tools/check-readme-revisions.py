#!/usr/bin/env python3
"""Revision-label control for corpus/README.md (round 49, claim Ca).

The round-28 index sweep (`reports/round-28/readme/sweep.py`) checks rows,
section counts, the totals line and the counts footer; the round-48 sibling
(`tools/check-readme-heading.py`) checks ATX headings. Neither has a
revision-label leg: a truncated duplicate `revision: 2.0` stub (a bare label
line followed immediately by a blank line, then the real 2.0 block) sat in
the live README at line 55 while every check stayed green.

This control is their sibling. It reads one Markdown file, collects
`^revision: <label>` lines outside fenced code blocks, and asserts:

  * every revision label is unique (duplicates report all their lines)
  * no revision line is a truncated stub: a label line immediately followed
    by a blank line (or end of file) has no changelog body
  * labels appear in non-increasing order top-to-bottom (newest first);
    enabled because the current README is strictly decreasing

Findings drive the exit code. Two advisory warning classes are also emitted:
REVISION-ORPHAN (a whole paragraph inside the revisions span that is not
headed by `revision:` — a changelog body detached from its header, like the
pre-existing round-35 rev-1.9 orphan at lines 69-80) and REVISION-GAP (a
skipped minor within one major, e.g. 2.3 -> 2.1). Warnings report debt a
round may legitimately carry; they never turn a clean verdict red.

Stdlib only. Read-only: no network, no writes, no eval/exec.

Usage:
  python3 tools/check-readme-revisions.py
  python3 tools/check-readme-revisions.py --readme <path> [--json]
  python3 tools/check-readme-revisions.py --selftest

Exit codes: 0 = clean, 1 = finding present, 2 = could-not-evaluate (missing or
unreadable input, usage error). Unexpected internal failures print a JSON
object with `ok: null` and exit 2; no traceback is printed.
"""
import argparse
import contextlib
import hashlib
import io
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.abspath(os.path.join(HERE, ".."))
DEFAULT_README = os.path.join(LANE, "corpus", "README.md")

REVISION_RE = re.compile(r"^revision:[ \t]+(\S+)")
FENCE_RE = re.compile(r"^[ ]{0,3}(`{3,}|~{3,})")
NUM_RE = re.compile(r"\d+")

# Stable diagnostic ids.
REVISION_DUP = "REVISION-DUP"
REVISION_STUB = "REVISION-STUB"
REVISION_ORDER = "REVISION-ORDER"
# Advisory classes: reported as warnings, never counted in `ok`.
REVISION_ORPHAN = "REVISION-ORPHAN"
REVISION_GAP = "REVISION-GAP"

# The pre-fix commit whose README carried the real round-49 defect: a
# truncated duplicate `revision: 2.0` stub at line 55. Selftest uses it as a
# committed fixture (SKIP, not FAIL, when the object is unreachable).
BASE_COMMIT = "c42d675be96b6b3957e6e5c00ab192080cb70083"


def revisions(text):
    """`^revision: <label>` lines outside fenced blocks: [(line_no, label)]."""
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
        r = REVISION_RE.match(line)
        if r:
            out.append((i, r.group(1)))
    return out


def label_key(label):
    """Numeric sort key for a label like '2.5'; None when it has no digits."""
    nums = NUM_RE.findall(label)
    return tuple(int(n) for n in nums) if nums else None


def evaluate_text(text):
    """Measure one README string. Pure: no IO."""
    revs = revisions(text)
    findings = []

    # (a) unique labels
    by_label = {}
    for n, label in revs:
        by_label.setdefault(label, []).append(n)
    for label in sorted(by_label):
        ns = by_label[label]
        if len(ns) > 1:
            findings.append(
                {
                    "class": REVISION_DUP,
                    "detail": "revision label %r repeated" % label,
                    "lines": ns,
                }
            )

    # (b) no truncated stubs: label line immediately followed by blank/EOF
    lines = text.splitlines()
    for n, label in revs:
        nxt = lines[n].strip() if n < len(lines) else ""
        if nxt == "":
            findings.append(
                {
                    "class": REVISION_STUB,
                    "detail": "revision %r at line %d has no changelog body" % (label, n),
                    "lines": [n],
                }
            )

    # (c) non-increasing order top-to-bottom over numeric labels
    keyed = [(n, label, label_key(label)) for n, label in revs]
    keyed = [(n, label, k) for n, label, k in keyed if k is not None]
    for (n1, l1, k1), (n2, l2, k2) in zip(keyed, keyed[1:]):
        if k2 > k1:
            findings.append(
                {
                    "class": REVISION_ORDER,
                    "detail": "revision %r (line %d) follows %r (line %d): "
                    "labels must be non-increasing" % (l2, n2, l1, n1),
                    "lines": [n1, n2],
                }
            )
            break

    warnings = []

    # (w1) orphan paragraphs: a whole paragraph inside the revisions span
    # (first..last revision line) that is not headed by `revision:` is a
    # changelog body detached from its header — e.g. the round-35 rev-1.9
    # body stranded between the 2.0 and 1.8 blocks.
    if revs:
        fenced = set()
        fence = None
        for i, raw in enumerate(lines):
            m = FENCE_RE.match(raw.rstrip("\r"))
            if m:
                marker = m.group(1)[0]
                if fence is None:
                    fence = marker
                elif fence == marker:
                    fence = None
                continue
            if fence is not None:
                fenced.add(i + 1)
        in_span = lambda n: revs[0][0] <= n <= revs[-1][0]
        para_start = None
        for n in range(revs[0][0], revs[-1][0] + 1):
            if n in fenced or lines[n - 1].strip() == "":
                if para_start is not None:
                    if not REVISION_RE.match(lines[para_start - 1]):
                        warnings.append(
                            {
                                "class": REVISION_ORPHAN,
                                "detail": "unheaded paragraph inside revisions "
                                "span (starts %r)" % lines[para_start - 1][:60],
                                "lines": [para_start, n - 1],
                            }
                        )
                    para_start = None
                continue
            if para_start is None:
                para_start = n
        if para_start is not None and not REVISION_RE.match(lines[para_start - 1]):
            warnings.append(
                {
                    "class": REVISION_ORPHAN,
                    "detail": "unheaded paragraph inside revisions span "
                    "(starts %r)" % lines[para_start - 1][:60],
                    "lines": [para_start, revs[-1][0]],
                }
            )

    # (w2) minor gaps within one major (2.3 -> 2.1 skips 2.2). Cross-major
    # transitions are not checked: the lower major's max minor is unknown.
    for (n1, l1, k1), (n2, l2, k2) in zip(keyed, keyed[1:]):
        if len(k1) >= 2 and len(k2) >= 2 and k1[0] == k2[0] and k1[1] - k2[1] > 1:
            warnings.append(
                {
                    "class": REVISION_GAP,
                    "detail": "label sequence %r (line %d) -> %r (line %d) "
                    "skips a minor" % (l1, n1, l2, n2),
                    "lines": [n1, n2],
                }
            )

    return {
        "ok": not findings,
        "findings": findings,
        "warnings": warnings,
        "revision_count": len(revs),
        "revision_lines": [n for n, _ in revs],
        "labels": [label for _, label in revs],
    }

def receipt(path, text, result):
    result = dict(result)
    result["readme"] = path
    result["sha256"] = hashlib.sha256(text.encode("utf-8")).hexdigest()
    return result


def selftest():
    ok = True
    skips = []

    def check(name, cond, detail=""):
        nonlocal ok
        if not cond:
            ok = False
        print(("PASS " if cond else "FAIL ") + name + (" " + detail if detail else ""))

    def skip(name, detail=""):
        skips.append(name)
        print("SKIP " + name + (" " + detail if detail else ""))

    # 1. newest-first unique labels, each with a body -> clean
    r = evaluate_text(
        "# title\n\nrevision: 2.1 — second\nbody text\n\n"
        "revision: 2.0 — first\nbody text\n"
    )
    check("control: clean revision list passes", r["ok"] is True, json.dumps(r["findings"]))

    # 2. duplicated label -> flagged with both lines
    r = evaluate_text(
        "revision: 2.0 — dup\nbody\n\nrevision: 2.0 — dup\nbody\n"
    )
    f = [x for x in r["findings"] if x["class"] == REVISION_DUP]
    check(
        "control: duplicate label flagged at [1, 4]",
        len(f) == 1 and f[0]["lines"] == [1, 4],
        json.dumps(r["findings"]),
    )

    # 3. truncated stub (label line then blank) -> flagged
    r = evaluate_text("revision: 2.1 — real\nbody\n\nrevision: 2.0 — stub\n\nrevision: 2.0 — real\nbody\n")
    classes = [x["class"] for x in r["findings"]]
    check(
        "control: truncated stub flagged",
        REVISION_STUB in classes and REVISION_DUP in classes,
        json.dumps(r["findings"]),
    )

    # 4. revision line as last line of file -> stub
    r = evaluate_text("body\n\nrevision: 9.9 — dangling\n")
    check(
        "control: EOF stub flagged",
        any(x["class"] == REVISION_STUB for x in r["findings"]),
        json.dumps(r["findings"]),
    )

    # 5. increasing order -> flagged
    r = evaluate_text("revision: 1.4 — old\nbody\n\nrevision: 2.5 — new\nbody\n")
    check(
        "control: increasing order flagged",
        any(x["class"] == REVISION_ORDER for x in r["findings"]),
        json.dumps(r["findings"]),
    )

    # 6. 'revision:' inside a fenced block is not counted
    r = evaluate_text("```\nrevision: 0.0 — example\n```\n\nrevision: 1.0 — only\nbody\n")
    check(
        "control: fenced 'revision:' ignored",
        r["ok"] is True and r["revision_count"] == 1,
        json.dumps(r),
    )

    # 7. no revision lines at all -> nothing to check, clean
    r = evaluate_text("# title\n\nbody\n")
    check(
        "control: absent revision lines passes",
        r["ok"] is True and r["revision_count"] == 0,
        json.dumps(r),
    )

    # 8. missing file -> exit 2 (could-not-evaluate)
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        code = main(["--readme", os.path.join(HERE, "no-such-readme.md")])
    check("control: missing file exits 2", code == 2, buf.getvalue().strip())

    # 9. the real r49 defect: base commit's README -> REVISION-DUP + REVISION-STUB
    name = "control: base %s README flagged (r49 defect)" % BASE_COMMIT[:7]
    try:
        proc = subprocess.run(
            ["git", "-C", LANE, "show", "%s:corpus/README.md" % BASE_COMMIT],
            capture_output=True,
            timeout=30,
        )
        if proc.returncode != 0:
            skip(name, "(base object unreachable)")
        else:
            r = evaluate_text(proc.stdout.decode("utf-8"))
            classes = {x["class"] for x in r["findings"]}
            check(
                name,
                REVISION_DUP in classes and REVISION_STUB in classes,
                json.dumps(r["findings"]),
            )
    except (OSError, subprocess.SubprocessError) as exc:
        skip(name, "(%r)" % exc)

    # 10. detached body (lost header) -> REVISION-ORPHAN warning, still ok
    r = evaluate_text(
        "revision: 2.0 — real\nbody\n\n"
        "round-28 C entry landed (orphan body)\nand its totals line\n\n"
        "revision: 1.8 — older\nbody\n"
    )
    w = [x for x in r["warnings"] if x["class"] == REVISION_ORPHAN]
    check(
        "control: orphan paragraph warned at [4, 5], verdict clean",
        r["ok"] is True and len(w) == 1 and w[0]["lines"] == [4, 5],
        json.dumps(r["warnings"]),
    )

    # 11. skipped minor within one major -> REVISION-GAP warning
    r = evaluate_text("revision: 2.3 — a\nbody\n\nrevision: 2.1 — b\nbody\n")
    check(
        "control: minor gap warned",
        any(x["class"] == REVISION_GAP for x in r["warnings"]),
        json.dumps(r["warnings"]),
    )

    print("selftest skips: %d" % len(skips))
    return ok


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--readme", default=DEFAULT_README)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args(argv)

    if args.selftest:
        passed = selftest()
        print("selftest: %s" % ("all checks passed" if passed else "FAILED"))
        return 0 if passed else 1

    try:
        with open(args.readme, encoding="utf-8") as fh:
            text = fh.read()
        result = receipt(args.readme, text, evaluate_text(text))
    except (OSError, UnicodeDecodeError) as exc:
        print(json.dumps({"ok": None, "error": repr(exc), "readme": args.readme}))
        return 2
    except Exception as exc:  # defensive: internal failure is not a finding
        print(json.dumps({"ok": None, "error": repr(exc), "readme": args.readme}))
        return 2

    if args.json:
        print(json.dumps(result, indent=1, sort_keys=True))
    else:
        print("readme %s" % result["readme"])
        print("sha256 %s" % result["sha256"])
        print("revision_lines %s" % result["revision_lines"])
        print("labels %s" % json.dumps(result["labels"]))
        print("findings %d" % len(result["findings"]))
        for f in result["findings"]:
            print("  %s lines=%s %s" % (f["class"], f["lines"], f["detail"]))
        print("warnings %d" % len(result["warnings"]))
        for w in result["warnings"]:
            print("  %s lines=%s %s" % (w["class"], w["lines"], w["detail"]))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
