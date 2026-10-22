#!/usr/bin/env python3
"""Gate quote-cap check for corpus lessons (round 54, routed defect repair).

Round 53's `## Gate` section carried five rows whose quoted material ran to
26-36 words per line because a quote fragment was joined to another quoted
fragment on the same line (the round-53 verifier spot-check, routed defect 3:
"five round-53 `## Gate` lines joined quote fragments so the quoted words per
line reached 26-36, and no check caught it"). No tool in `tools/` looked at
the length of a Gate quotation, so the defect survived the round-53 gate.

This tool reads the `## Gate` section of a lesson and reports every row
whose quoted material breaks the lane's 25-word quotation cap.

What it reads
  * Only the `## Gate` section of each file: from the `## Gate` heading up to
    (not including) the next `## ` heading. `### ` sub-headings stay inside the
    section; nothing outside it is read.
  * Only the `- S### ` rows inside that section. A row is a line that starts
    with `- ` followed by a registry id (`S` + digits).

How a quotation is found
  * Quoted spans are straight `"..."` and curly `“...”` pairs. The spans are
    taken left to right and never overlap: a straight pair is preferred when
    one starts there, so a straight span that contains curly quotes is read
    whole rather than cut in two.
  * Spans on one row are grouped into *runs*. A run is a maximal group of
    consecutive spans with nothing but punctuation and whitespace between
    them (no letter, digit or underscore). A run is what a reader receives as
    one continuous quotation; two spans separated by prose ("... .
    Geography paragraph, line 82: ...") are two quotations, not one.

Word count rule
  * A run's word count is the sum over its spans of
    `len(span_text.split())`: the text between the quotation marks is split on
    whitespace and every non-empty token counts as one word. Punctuation-only
    tokens count ("(39%)" is one word) and an ellipsis token counts as one
    word. No stemming, no de-duplication, no punctuation stripping.

What it reports
  * `over-cap`   the run has more than 25 words.
  * `ellipsis-joined` the run carries an ellipsis that joins two fragments
    inside one pair of quotes (text on both sides of the ellipsis). Such a
    row is a joined quotation even when it is short, so it is reported. A
    leading or trailing ellipsis is an ordinary omission marker and is not
    reported.
  * A row is reported once per offending run; if a row has two offending runs
    the larger word count is the one printed.

Usage:
  python3 -B check-gate-quotes.py <lesson.md>...
  python3 -B check-gate-quotes.py --selftest

Output: one line per finding on stdout, then a summary line.
  <path>:<line> <S-id> words=<n>
  GATE_QUOTES: <n> findings
Exit codes: 0 no findings; 1 findings; 2 could not evaluate (a path is
missing or unreadable, a file has no `## Gate` section, or no path was
given; the reason goes to stderr as `GATE_QUOTES_ERROR:`). Read-only, Python
3 standard library only, no network.
"""

import argparse
import re
import sys

# The lane's quotation cap for a Gate quote.
MAX_WORDS = 25
# `## Gate` opens the section; the next `## ` heading closes it.
GATE_HEADING = re.compile(r"^##\s+Gate\b")
NEXT_H2 = re.compile(r"^##\s")
# A Gate row: `- S187 — https://...`.
ROW = re.compile(r"^-\s+(S\d+)\b")
# A quoted span: straight "..." first, then curly “...”.
QUOTE = re.compile(r'"[^"\n]*"|“[^“”\n]*”')
# Any letter, digit or underscore: prose between two spans breaks a run.
WORDISH = re.compile(r"[\w]", re.UNICODE)
# An ellipsis: the single character or three dots.
ELLIPSIS = re.compile(r"…|\.\.\.")


def gate_section(text):
    """The `## Gate` section as [(line_number, line)], or None if absent."""
    lines = text.splitlines()
    start = None
    for index, line in enumerate(lines):
        if GATE_HEADING.match(line):
            start = index + 1
            break
    if start is None:
        return None
    body = []
    for index in range(start, len(lines)):
        if NEXT_H2.match(lines[index]):
            break
        body.append((index + 1, lines[index]))
    return body


def quoted_spans(line):
    """Non-overlapping quoted spans of one line as (start, end, inner text)."""
    return [(m.start(), m.end(), m.group(0)[1:-1]) for m in QUOTE.finditer(line)]


def quote_runs(line):
    """Quoted spans of one line grouped into runs of one continuous quotation."""
    runs = []
    current = []
    previous_end = None
    for start, end, text in quoted_spans(line):
        if previous_end is not None:
            gap = line[previous_end:start]
            if WORDISH.search(gap):
                runs.append(current)
                current = []
        current.append(text)
        previous_end = end
    if current:
        runs.append(current)
    return runs


def run_words(run):
    """Word count of a run: whitespace split of each span's inner text."""
    return sum(len(text.split()) for text in run)


def ellipsis_joins(text):
    """True when an ellipsis inside one span joins two fragments."""
    for match in ELLIPSIS.finditer(text):
        if text[:match.start()].strip() and text[match.end():].strip():
            return True
    return False


def scan_line(line, number):
    """Findings on one line as (line_number, s_id, words, reason) tuples."""
    row = ROW.match(line)
    if not row:
        return []
    findings = []
    for run in quote_runs(line):
        words = run_words(run)
        if words > MAX_WORDS:
            findings.append((number, row.group(1), words, "over-cap"))
        elif any(ellipsis_joins(text) for text in run):
            findings.append((number, row.group(1), words, "ellipsis-joined"))
    return findings


def scan_text(text):
    """Findings in a whole document as (line_number, s_id, words, reason)."""
    section = gate_section(text)
    if section is None:
        return None
    findings = []
    for number, line in section:
        findings.extend(scan_line(line, number))
    return findings


def check(paths):
    """Findings per path as (path, findings); a path that cannot be read is
    reported with findings None."""
    results = []
    for path in paths:
        try:
            with open(path, "r", encoding="utf-8") as handle:
                text = handle.read()
        except OSError as exc:
            results.append((path, None, "unreadable: %s" % exc.strerror))
            continue
        findings = scan_text(text)
        if findings is None:
            results.append((path, None, "no `## Gate` section"))
            continue
        results.append((path, findings, None))
    return results


def run(paths):
    """Print the findings and return the exit code."""
    if not paths:
        print("GATE_QUOTES_ERROR: no lesson file given", file=sys.stderr)
        return 2
    results = check(paths)
    errors = 0
    total = 0
    reasons = {"over-cap": 0, "ellipsis-joined": 0}
    for path, findings, error in results:
        if findings is None:
            errors += 1
            print("GATE_QUOTES_ERROR: %s: %s" % (path, error), file=sys.stderr)
            continue
        for number, s_id, words, reason in findings:
            print("%s:%d %s words=%d" % (path, number, s_id, words))
            reasons[reason] = reasons.get(reason, 0) + 1
        total += len(findings)
    print("GATE_QUOTES: %d findings" % total)
    if errors:
        return 2
    return 1 if total else 0


def lesson(rows):
    """A whole lesson document whose `## Gate` section carries `rows`."""
    return "# Round 60 — lesson (kotodama)\n\n## Gate\n\n%s\n\n## Status\n" % rows


def selftest():
    """Cases that exercise the span, run, word-count and ellipsis rules."""
    long_quotes = " ".join(["w%d" % n for n in range(26)])
    cases = [
        ("short-quote", lesson('- S900 — p. 1: "one two three".\n'), 0),
        ("exactly-25", lesson('- S900 — p. 1: "%s".\n'
                              % " ".join(["w%d" % n for n in range(25)])), 0),
        ("26-words", lesson('- S900 — p. 1: "%s".\n' % long_quotes), 1),
        ("curly-26-words", lesson('- S900 — p. 1: “%s”.\n' % long_quotes), 1),
        ("anchor-join-27", lesson('- S900 — Table 2 "Counts of pointing forms used": '
                                  '"%s".\n'
                                  % " ".join(["w%d" % n for n in range(22)])), 1),
        ("two-separate-quotes", lesson('- S900 — p. 1: "%s". Next paragraph: "%s".\n'
                                       % (" ".join(["a%d" % n for n in range(13)]),
                                          " ".join(["b%d" % n for n in range(13)]))), 0),
        ("ellipsis-joined", lesson('- S900 — Abstract: "The first two '
                                   '… have recognition as emblems".\n'), 1),
        ("leading-ellipsis", lesson('- S900 — Abstract: "…the steep mountains '
                                    'and rugged topography of the region".\n'), 0),
        ("not-a-row", lesson('The gate says "%s".\n'
                             % " ".join(["w%d" % n for n in range(40)])), 0),
        ("outside-the-gate-section",
         "## Gate\n\n- S900 — p. 1: \"short\".\n\n## Later\n\n- S901 — p. 1: \"%s\".\n"
         % " ".join(["w%d" % n for n in range(40)]), 0),
        ("row-in-another-section",
         "## Intro\n\n- S901 — p. 1: \"%s\".\n\n## Gate\n\n- S900 — p. 1: \"short\".\n"
         % " ".join(["w%d" % n for n in range(40)]), 0),
        ("no-gate-section", "# Round 60 — lesson (kotodama)\n\n## Status\n", None),
    ]
    failures = 0
    for name, body, want in cases:
        findings = scan_text(body)
        got = None if findings is None else len(findings)
        ok = got == want
        failures += not ok
        print("%s %s want=%s got=%s" % ("PASS" if ok else "FAIL", name, want, got))
    total = len(cases)
    print("SELFTEST: %d/%d pass" % (total - failures, total))
    return 1 if failures else 0


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--selftest", action="store_true")
    parser.add_argument("paths", nargs="*")
    args = parser.parse_args()
    if args.selftest:
        return selftest()
    return run(args.paths)


if __name__ == "__main__":
    sys.exit(main())
