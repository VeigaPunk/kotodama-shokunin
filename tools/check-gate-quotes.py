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
  * Only `- S### ` rows inside that section, including `- * S### ` rows.
    Indented continuation lines are joined to the row before its quotes are checked.

How a quotation is found
  * Quoted spans are straight `"..."`, curly `“...”`, or guillemet `«...»`
    pairs. The spans are taken left to right and never overlap: a straight pair
    is preferred when one starts there, so a straight span that contains curly
    quotes is read whole rather than cut in two.
  * Spans on one row are grouped into *runs*. A run is a maximal group of
    consecutive spans with nothing but punctuation and whitespace between
    them (no letter, digit or underscore). A run is what a reader receives as
    one continuous quotation; two spans separated by prose ("... .
    Geography paragraph, line 82: ...") are two quotations, not one.

Word count rule
  * A run's word count is the sum over its spans of
    `len(span_text.split())`: the text between quotation marks is split on
    whitespace and every non-empty token counts as one word. Thus `mother-in-law`
    is one token, not three. Punctuation-only tokens count ("(39%)" is one word)
    and an ellipsis token counts as one word. No stemming, de-duplication, or
    punctuation stripping.

  * `over-cap` reports a run with more than 25 words.
  * `ellipsis-joined` reports an ellipsis joining fragments inside a span or
    between spans of one run; a leading or trailing omission marker is not
    reported.
  * `doubled-locator` reports a first cited span whose text also appears in the
    locator after the `accessed <date> — ` field, when another quoted span
    follows. This catches repeated single- or double-quoted locator text without
    mistaking escaped quotes inside one span for a repeated locator.
  * `truncated-grounds` reports Grounds text that is a proper prefix (shorter,
    not equal) of the same S-id's registry `teaches` cell, ignoring quote
    delimiters and trailing full stops or whitespace. Missing registry files or
    rows are skipped. A complete Grounds sentence, including one ending in a
    single full stop, is not reported.
  * A row is reported once per offending run and once per new shape; if a run
    has two quote findings, the over-cap count takes precedence.

Usage:
  python3 -B check-gate-quotes.py <lesson.md>...
  python3 -B check-gate-quotes.py --selftest

Output: one line per finding on stdout, then a summary line. Existing quote
findings retain their original detail; shape findings use their class name.
  <path>:<line> <S-id> words=<n> | doubled-locator | truncated-grounds
Exit codes: 0 no findings; 1 findings; 2 could not evaluate (a path is
missing or unreadable, a file has no `## Gate` section, or no path was
given; the reason goes to stderr as `GATE_QUOTES_ERROR:`). Read-only, Python
3 standard library only, no network.
"""

import argparse
import os
import re
import sys

# The lane's quotation cap for a Gate quote.
MAX_WORDS = 25
# `## Gate` opens the section; the next `## ` heading closes it.
GATE_HEADING = re.compile(r"^##\s+Gate\b")
NEXT_H2 = re.compile(r"^##\s")
# A Gate row: `- S187 — https://...`.
ROW = re.compile(r"^-\s+(?:\*\s+)?(S\d+)\b")
# A quoted span: straight, curly, or guillemet quote pairs.
QUOTE = re.compile(r'"(?:\\.|[^"\\\n])*"|“[^“”\n]*”|«[^«»\n]*»')
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
    """Non-overlapping quoted spans as (start, end, inner text)."""
    return [(m.start(), m.end(), m.group(0)[1:-1]) for m in QUOTE.finditer(line)]


def quote_run_details(line):
    """Quoted spans grouped by punctuation-only gaps, with gap ellipses noted."""
    runs = []
    current = []
    previous_end = None
    joined_ellipsis = False
    for start, end, text in quoted_spans(line):
        if previous_end is not None:
            gap = line[previous_end:start]
            if WORDISH.search(gap):
                runs.append((current, joined_ellipsis))
                current = []
                joined_ellipsis = False
            elif ELLIPSIS.search(gap):
                joined_ellipsis = True
        current.append(text)
        previous_end = end
    if current:
        runs.append((current, joined_ellipsis))
    return runs


def quote_runs(line):
    """Quoted spans of one line grouped into runs of one continuous quotation."""
    return [run for run, _ in quote_run_details(line)]


def run_words(run):
    """Word count of a run: whitespace split of each span's inner text."""
    return sum(len(text.split()) for text in run)


def ellipsis_joins(text):
    """True when an ellipsis inside one span joins two fragments."""
    for match in ELLIPSIS.finditer(text):
        if text[:match.start()].strip() and text[match.end():].strip():
            return True
    return False


def registry_teaches(path):
    """Read source teaches cells from the SOURCES.md beside a lesson corpus."""
    source_path = os.path.normpath(
        os.path.join(os.path.dirname(os.path.abspath(path)), "..", "SOURCES.md"))
    try:
        with open(source_path, "r", encoding="utf-8") as handle:
            lines = handle.readlines()
    except (OSError, UnicodeError):
        return {}
    teaches = {}
    for line in lines:
        if not line.startswith("| S"):
            continue
        cells = line.rstrip("\r\n").split("|")
        if len(cells) != 13:
            continue
        s_id = cells[1].strip()
        if re.fullmatch(r"S\d+", s_id):
            teaches[s_id] = cells[7].strip()
    return teaches


def doubled_locator(line):
    """True when the first cited span repeats text from its accessed locator."""
    accessed = re.search(r" — accessed \d{4}-\d{2}-\d{2} — ", line)
    if accessed is None:
        return False
    spans = [span for span in quoted_spans(line) if span[0] >= accessed.end()]
    quote_index = None
    locator = ""
    for index, span in enumerate(spans):
        before = line[accessed.end():span[0]]
        if re.search(r":\s+$", before):
            quote_index = index
            locator = before.rsplit(":", 1)[0]
            break
    if quote_index is None or quote_index + 1 >= len(spans):
        return False
    quoted_title = spans[quote_index][2].strip()
    return bool(quoted_title) and quoted_title in locator


def comparable_teaches(text):
    """Drop quote delimiters and trailing full stops/whitespace for comparison."""
    return re.sub(r'["“”«»]', "", text).rstrip().rstrip(".").rstrip()


def truncated_grounds(line, s_id, teaches):
    """True when Grounds is an incomplete prefix of its registry teaches cell."""
    source_teaches = teaches.get(s_id)
    if not source_teaches:
        return False
    match = re.search(r"\bGrounds:\s*(.*?)\. Seat:", line)
    if match is None:
        return False
    grounds = comparable_teaches(match.group(1))
    source_teaches = comparable_teaches(source_teaches)
    return bool(grounds and len(grounds) < len(source_teaches)
                and source_teaches.startswith(grounds))


def scan_line(line, number, teaches=None):
    """Findings on a logical row as (line_number, s_id, words, reason) tuples."""
    row = ROW.match(line)
    if not row:
        return []
    s_id = row.group(1)
    teaches = teaches or {}
    findings = []
    for run, gap_ellipsis in quote_run_details(line):
        words = run_words(run)
        if words > MAX_WORDS:
            findings.append((number, s_id, words, "over-cap"))
        elif gap_ellipsis or any(ellipsis_joins(text) for text in run):
            findings.append((number, s_id, words, "ellipsis-joined"))
    if doubled_locator(line):
        findings.append((number, s_id, 0, "doubled-locator"))
    if truncated_grounds(line, s_id, teaches):
        findings.append((number, s_id, 0, "truncated-grounds"))
    return findings


def gate_rows(section):
    """Gate rows with their indented physical continuation lines joined."""
    rows = []
    number = None
    logical_line = None
    for line_number, line in section:
        if ROW.match(line):
            if logical_line is not None:
                rows.append((number, logical_line))
            number = line_number
            logical_line = line
        elif logical_line is not None and line[:1].isspace() and line.strip():
            logical_line += " " + line.strip()
        elif logical_line is not None:
            rows.append((number, logical_line))
            number = None
            logical_line = None
    if logical_line is not None:
        rows.append((number, logical_line))
    return rows


def scan_text(text, teaches=None):
    """Findings in a whole document as (line_number, s_id, words, reason)."""
    section = gate_section(text)
    if section is None:
        return None
    findings = []
    for number, line in gate_rows(section):
        findings.extend(scan_line(line, number, teaches))
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
        findings = scan_text(text, registry_teaches(path))
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
            detail = reason if reason in ("doubled-locator", "truncated-grounds") else "words=%d" % words
            print("%s:%d %s %s" % (path, number, s_id, detail))
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
    """Cases exercising spans, row shapes, word counts, and ellipsis rules."""
    long_quotes = " ".join(["w%d" % n for n in range(26)])
    hard_wrapped = " ".join(["w%d" % n for n in range(26)])
    hyphenated = " ".join(["w%02d" % n for n in range(1, 24)] + ["mother-in-law", "twenty-six"])
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
        ("hard-wrapped-26", lesson('- S900 — p. 1: "%s\n  %s".\n'
                                   % (" ".join(hard_wrapped.split()[:13]),
                                      " ".join(hard_wrapped.split()[13:]))), 1),
        ("guillemets-26", lesson('- S900 — p. 1: «%s».\n' % long_quotes), 1),
        ("ellipsis-between-spans",
         lesson('- S900 — p. 1: "alpha bravo charlie delta echo foxtrot golf hotel" '
                '… "india juliet kilo lima mike november oscar papa quebec romeo sierra tango '
                'uniform victor".\n'), 1),
        ("star-bullet-26", lesson('- * S900 — p. 1: "%s".\n' % long_quotes), 1),
        ("hyphenated-whitespace-25", lesson('- S900 — p. 1: "%s".\n' % hyphenated), 0),
    ]
    failures = 0
    for name, body, want in cases:
        findings = scan_text(body)
        got = None if findings is None else len(findings)
        ok = got == want
        failures += not ok
        print("%s %s want=%s got=%s" % ("PASS" if ok else "FAIL", name, want, got))

    class_cases = [
        ("doubled-locator-single-quoted-red",
         lesson("- S900 — URL — accessed 2026-10-22 — Section 'X': \"X\": \"real quote\".\n"),
         None, "doubled-locator"),
        ("doubled-locator-double-quoted-red",
         lesson('- S900 — URL — accessed 2026-10-22 — "Section", ¶1: "Section", ¶1: "real".\n'),
         None, "doubled-locator"),
        ("doubled-locator-green",
         lesson("- S900 — URL — accessed 2026-10-22 — Section 'X': \"other\": \"real quote\".\n"),
         None, None),
        ("doubled-locator-s273-escaped-green",
         lesson('- S273 — URL — accessed 2026-10-22 — Title (EN): "Gold death-mask of a man, known by the conventional name \\"mask of Agamemnon\\"".\n'),
         None, None),
        ("truncated-grounds-red",
         lesson("- S900 — p. 1: \"short\". Grounds: the keeper was a. Seat: Scout.\n"),
         {"S900": "the keeper was a guardian."}, "truncated-grounds"),
        ("truncated-grounds-whole-single-stop-green",
         lesson("- S900 — p. 1: \"short\". Grounds: the keeper was owed. Seat: Scout.\n"),
         {"S900": "the keeper was owed."}, None),
        ("truncated-grounds-double-stop-green",
         lesson("- S900 — p. 1: \"short\". Grounds: the keeper was owed.. Seat: Scout.\n"),
         {"S900": "the keeper was owed."}, None),
    ]
    for name, body, source_teaches, want in class_cases:
        findings = scan_text(body, source_teaches)
        got = [] if findings is None else [reason for _, _, _, reason in findings]
        expected = [] if want is None else [want]
        ok = got == expected
        failures += not ok
        print("%s %s want=%s got=%s" %
              ("PASS" if ok else "FAIL", name, want or "none", ",".join(got) or "none"))
    total = len(cases) + len(class_cases)
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
