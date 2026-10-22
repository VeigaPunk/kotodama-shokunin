# ExecGateQuoteCheck — a mechanical check for joined Gate quotations (round-54 routed defect 3)

Scope: write `check-gate-quotes.py` and the fixtures, show the tool able to fail, and report what
it finds in the lane's lessons. Lane read-only: the only file I wrote outside my scratch dir is
this report. Code and fixtures live in `/fast/scratch/hyaku/kotodama-r54-a2/ExecGateQuoteCheck/`.

The routed defect (round-53 closure, `corpus/lessons/round-53-verifier-spotcheck.md:149` and `:175`):
five round-53 `## Gate` lines joined quote fragments so the quoted words per line reached 26–36,
and no check caught it. The fix asked for is "split joined fragments into separate quotes, each
≤25 words: S200, S205, S214, S224, S236".

## The rule the tool enforces (documented, mechanical)

Read only the `## Gate` section of a lesson — from the `## Gate` heading to the next `## `
heading; `### ` sub-headings stay inside, nothing outside is read. Inside that section, only the
`- S### ` rows are scanned.

A **quoted span** is a straight `"..."` pair or a curly `“...”` pair. Spans are taken left to
right and never overlap, so a straight span that contains curly quotes is read whole.

Spans on one row are grouped into a **run**: a maximal group of consecutive spans with nothing
but punctuation and whitespace between them (no letter, digit or underscore). A run is what a
reader receives as one continuous quotation. Two spans separated by prose (`". Geography
paragraph, line 82: "`) are two quotations, not one.

**Word count**: the text between the quotation marks is split on whitespace and every non-empty
token counts as one word, summed over the run's spans. Punctuation-only tokens count (`(39%)` is
one word); an ellipsis token counts as one word. No stemming, no de-duplication, no stripping.

A row is reported when either holds:

- **over-cap** — the run has more than 25 words;
- **ellipsis-joined** — the run carries an ellipsis with words on both sides of it inside one
  pair of quotes, i.e. two fragments presented as one quotation. This fires even when the run
  is short, because the join is the defect. A *leading* or *trailing* ellipsis is an ordinary
  omission marker and is not reported.

Output is one line per finding, `path:line S### words=N`, then `GATE_QUOTES: <n> findings`.
Exit codes: 0 no findings, 1 findings, 2 could not evaluate (missing or unreadable path, a file
with no `## Gate` section, or no path given; the reason goes to stderr as `GATE_QUOTES_ERROR:`).

## Final script source

`/fast/scratch/hyaku/kotodama-r54-a2/ExecGateQuoteCheck/check-gate-quotes.py`
(sha256 `81bbef86b3bc4a7424f34cd1560f84c31e8be2aa90c503daa88d668d31bff2bf`, 259 lines,
Python 3.14.8 standard library only, read-only, no network).

```python
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
```

## Every run (command, output, exit code)

Transcript file: `/fast/scratch/hyaku/kotodama-r54-a2/ExecGateQuoteCheck/runs.txt`.

### Built-in selftest and the fixtures

```
$ python3 -B check-gate-quotes.py --selftest
PASS short-quote want=0 got=0
PASS exactly-25 want=0 got=0
PASS 26-words want=1 got=1
PASS curly-26-words want=1 got=1
PASS anchor-join-27 want=1 got=1
PASS two-separate-quotes want=0 got=0
PASS ellipsis-joined want=1 got=1
PASS leading-ellipsis want=0 got=0
PASS not-a-row want=0 got=0
PASS outside-the-gate-section want=0 got=0
PASS row-in-another-section want=0 got=0
PASS no-gate-section want=None got=None
SELFTEST: 12/12 pass
exit=0

$ python3 -B check-gate-quotes.py fixtures/green.md
GATE_QUOTES: 0 findings
exit=0

$ python3 -B check-gate-quotes.py fixtures/red-26-words.md
fixtures/red-26-words.md:9 S900 words=26
GATE_QUOTES: 1 findings
exit=1

$ python3 -B check-gate-quotes.py fixtures/red-curly-26.md
fixtures/red-curly-26.md:9 S900 words=26
GATE_QUOTES: 1 findings
exit=1

$ python3 -B check-gate-quotes.py fixtures/red-ellipsis.md
fixtures/red-ellipsis.md:10 S900 words=11
GATE_QUOTES: 1 findings
exit=1

$ python3 -B check-gate-quotes.py fixtures/red-joined-anchor.md
fixtures/red-joined-anchor.md:10 S900 words=27
GATE_QUOTES: 1 findings
exit=1

$ python3 -B check-gate-quotes.py fixtures/outside-gate-section.md
GATE_QUOTES: 0 findings
exit=0

$ python3 -B check-gate-quotes.py fixtures/no-gate.md
GATE_QUOTES_ERROR: fixtures/no-gate.md: no `## Gate` section
GATE_QUOTES: 0 findings
exit=2

$ python3 -B check-gate-quotes.py fixtures/no-such-file.md
GATE_QUOTES_ERROR: fixtures/no-such-file.md: unreadable: No such file or directory
GATE_QUOTES: 0 findings
exit=2

$ python3 -B check-gate-quotes.py
GATE_QUOTES_ERROR: no lesson file given
exit=2
```

Fixture files (all under `fixtures/`): `green.md` (short quotes, exit 0), `red-26-words.md` (one
straight span of 26 words), `red-curly-26.md` (one curly span of 26 words), `red-ellipsis.md`
(one pair of quotes carrying two fragments joined by an ellipsis, 11 words), `red-joined-anchor.md`
(the round-53 S200 shape: quoted anchor + quoted passage, 5 + 22 = 27),
`outside-gate-section.md` (a 26-word quote in a row *after* the `## Gate` section — not read),
`no-gate.md` (exit 2).

### The lane's lessons

Run from the lane root `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, HEAD `5757c45118771d8baac238b52aa5e95fc18cbd54`,
working tree clean for `corpus/lessons/`. `corpus/lessons/round-53.md` was last changed by
`0ef3a4acffae480458b2278d7b56eebf07a2c6c6`, so the file read is the lane tip's bytes.

```
$ python3 -B /fast/scratch/hyaku/kotodama-r54-a2/ExecGateQuoteCheck/check-gate-quotes.py corpus/lessons/round-53.md
corpus/lessons/round-53.md:42 S187 words=28
corpus/lessons/round-53.md:49 S189 words=28
corpus/lessons/round-53.md:58 S192 words=40
corpus/lessons/round-53.md:62 S194 words=28
corpus/lessons/round-53.md:84 S200 words=27
corpus/lessons/round-53.md:109 S205 words=36
corpus/lessons/round-53.md:110 S205 words=30
corpus/lessons/round-53.md:111 S205 words=26
corpus/lessons/round-53.md:128 S214 words=27
corpus/lessons/round-53.md:133 S217 words=11
corpus/lessons/round-53.md:160 S224 words=28
corpus/lessons/round-53.md:181 S236 words=29
GATE_QUOTES: 12 findings
exit=1

$ python3 -B /fast/scratch/hyaku/kotodama-r54-a2/ExecGateQuoteCheck/check-gate-quotes.py corpus/lessons/round-52.md
corpus/lessons/round-52.md:34 S096 words=23
corpus/lessons/round-52.md:59 S139 words=26
corpus/lessons/round-52.md:66 S140 words=27
corpus/lessons/round-52.md:68 S142 words=34
corpus/lessons/round-52.md:87 S155 words=31
corpus/lessons/round-52.md:94 S159 words=30
corpus/lessons/round-52.md:99 S164 words=29
GATE_QUOTES: 7 findings
exit=1

$ python3 -B /fast/scratch/hyaku/kotodama-r54-a2/ExecGateQuoteCheck/check-gate-quotes.py corpus/lessons/round-51.md
corpus/lessons/round-51.md:33 S076 words=34
corpus/lessons/round-51.md:78 S121 words=30
GATE_QUOTES: 2 findings
exit=1
```

## What round-53.md yields, line by line

The five S-ids the routed item names are **all** named: S200 (`:84`), S205 (`:109`, `:110`,
`:111`), S214 (`:128`), S224 (`:160`), S236 (`:181`). Five further rows are named, and the
numbers are the joined quotations, not a guess: each row is `anchor span (words) + quote span
(words)`, with the separator between them given.

| line | S-id | joined words | the two spans | separator |
|---|---|---|---|---|
| 42 | S187 | 28 | `"It's Not Polite to Point"` (5) + `"pointing gestures can have interactional significance …"` (23) | `": "` |
| 49 | S189 | 28 | `"Variation in gesture across languages and cultures"` (7) + `"there is, unfortunately, no entrenched typological tradition …"` (21) | `": "` |
| 58 | S192 | 40 | `"This division into four uses of gesture is not, I should emphasize, intended as a typology of gesture."` (18) + `"Especially when gestures are used for pointing, interaction regulation and pragmatic purposes, …"` (22) | `"): "` |
| 62 | S194 | 28 | `"Thus, there has been mounting evidence"` (6) + `"co-speech gestures contribute semantic, syntactic, discursive and pragmatic information …"` (22) | `": "` |
| 84 | S200 | 27 | `"Counts of pointing forms used"` (5) + `"Yupno 234 (39%) 8 (1%) 252 (42%) 104 (17%) 598 / United States 450 (91%) 35 (7%) 0 (0%) 11 (2%) 496"` (22) | `": "` |
| 109 | S205 | 36 | `"In Ghana, many peolple consider pointing by the left hand to be a taboo"` (14) + `"there is a politeness convention to place the left hand on the lower back, …"` (22) | `"; "` |
| 110 | S205 | 30 | `"right-handed pointing may involve an anatomically staining position …"` (16) + `"pointing is sometimes performed with both hands together, which does not violate the taboo"` (14) | `"; "` |
| 111 | S205 | 26 | `"Left-handed pointing gestures occur in association with the verbalization of the concept LEFT"` (13) + `"Ghanaians do not consider them as pointing for the purpose of the taboo"` (13) | `"; "` |
| 128 | S214 | 27 | `"Motion + Path"` (3) + `"In the second typological pattern for the expression of Motion, …"` (24) | `": "` |
| 133 | S217 | 11 | `"The first two … have recognition as 'quotable gestures' or 'emblems'"` — one pair of quotes, two fragments joined by an ellipsis | — |
| 160 | S224 | 28 | `"That probably explains many cultures' fear"` (6) + `"In places as widely separated as Hungary, China, Mexico, and Gabon, …"` (22) | `": "` |
| 181 | S236 | 29 | `"Total Liking = 7% Verbal Liking + 38% Vocal Liking + 55% Facial Liking"` (14) + `"Unless a communicator is talking about their feelings or attitudes, …"` (15) | `": "` |

### The surprises, and what they mean

1. **Five rows beyond the routed five.** S187, S189, S192 and S194 are the *same shape* as the
   routed five: a quoted anchor (a section heading, or a sentence quoted to fix the locator)
   followed by the quoted passage, separated by punctuation alone. Their separators are the same
   `": "` (S187, S189, S194) or `"): "` (S192) that separate the routed S200, S214, S224 and S236
   rows. S187, S189 and S194 count 28 joined words, which is inside the 26–36 band the spot-check
   reported at `:149`; S192 counts 40, above it. The spot-check's list of seven is therefore
   narrower than the defect class it describes ("an anchor or a second fragment joined to a
   quote"). Splitting only the five routed lines will leave the tool red on `round-53.md`.
2. **S217 (`:133`) is the ellipsis shape.** `"The first two … have recognition as 'quotable
   gestures' or 'emblems'"` is one pair of quotes holding two fragments; it is 11 words, so the
   length rule alone never sees it. This is the one finding the spot-check could not have had
   from a length scan. The sibling seat ScoutS225Recheck reports the same shape in the
   round-53 spot-check text at `:112` ("the spotcheck quoted these two sentences joined with an
   ellipsis into one fragment"), so the shape is live in the lane's own records.
3. **The class is older than round 53.** `round-52.md` has 7 rows and `round-51.md` has 2 in the
   same shape (`:34` S096 is an ellipsis join; `:59` S139, `:66` S140, `:68` S142, `:87` S155,
   `:94` S159, `:99` S164 and `:33` S076, `:78` S121 are over-cap joins). A sweep of all 41
   files in `corpus/lessons/` shows only these three lessons red: every other round lesson exits
   0, and the triage notes and spot-check reports exit 2 because they have no `## Gate` section
   (they never had one; `round-5-availability.md` does, and is green).

### The sweep of `corpus/lessons/` (read-only, one line per file)

```
corpus/lessons/round-1-gates-and-triage.md     exit=2 findings=0   (no `## Gate` section)
corpus/lessons/round-10.md                     exit=0 findings=0
corpus/lessons/round-11.md                     exit=0 findings=0
corpus/lessons/round-12.md                     exit=0 findings=0
corpus/lessons/round-14.md                     exit=0 findings=0
corpus/lessons/round-15.md                     exit=0 findings=0
corpus/lessons/round-16.md                     exit=2 findings=0   (no `## Gate` section)
corpus/lessons/round-17.md                     exit=0 findings=0
corpus/lessons/round-18.md                     exit=0 findings=0
corpus/lessons/round-19.md                     exit=0 findings=0
corpus/lessons/round-2-adjacency.md            exit=2 findings=0   (no `## Gate` section)
corpus/lessons/round-20.md                     exit=0 findings=0
corpus/lessons/round-21.md                     exit=0 findings=0
corpus/lessons/round-22.md                     exit=0 findings=0
corpus/lessons/round-23.md                     exit=0 findings=0
corpus/lessons/round-25.md                     exit=0 findings=0
corpus/lessons/round-26.md                     exit=0 findings=0
corpus/lessons/round-27.md                     exit=0 findings=0
corpus/lessons/round-28.md                     exit=0 findings=0
corpus/lessons/round-29.md                     exit=0 findings=0
corpus/lessons/round-3-d2-build.md             exit=2 findings=0   (no `## Gate` section)
corpus/lessons/round-30.md                     exit=0 findings=0
corpus/lessons/round-31.md                     exit=0 findings=0
corpus/lessons/round-32.md                     exit=0 findings=0
corpus/lessons/round-4-sol-fixes-and-audits.md exit=2 findings=0   (no `## Gate` section)
corpus/lessons/round-49-verifier-spotcheck.md  exit=2 findings=0   (no `## Gate` section)
corpus/lessons/round-49.md                     exit=0 findings=0
corpus/lessons/round-5-availability.md         exit=0 findings=0
corpus/lessons/round-5.md                      exit=0 findings=0
corpus/lessons/round-50-verifier-spotcheck.md  exit=2 findings=0   (no `## Gate` section)
corpus/lessons/round-50.md                     exit=0 findings=0
corpus/lessons/round-51-verifier-spotcheck.md  exit=2 findings=0   (no `## Gate` section)
corpus/lessons/round-51.md                     exit=1 findings=2
corpus/lessons/round-52-verifier-spotcheck.md  exit=2 findings=0   (no `## Gate` section)
corpus/lessons/round-52.md                     exit=1 findings=7
corpus/lessons/round-53-verifier-spotcheck.md  exit=2 findings=0   (no `## Gate` section)
corpus/lessons/round-53.md                     exit=1 findings=12
corpus/lessons/round-6.md                      exit=0 findings=0
corpus/lessons/round-7.md                      exit=0 findings=0
corpus/lessons/round-8.md                      exit=0 findings=0
corpus/lessons/round-9.md                      exit=0 findings=0
```

## Calibration: what the rule does and does not see

- **The scope limit costs nothing on the current corpus.** The tool scans straight and curly
  double quotes; it does not scan single quotes (`'`, `‘…’`), because `'` is also an
  apostrophe inside words. I measured the difference by re-running the same rule with
  `‘…’` added as a delimiter over all 285 Gate rows of the three lessons: 27 rows in
  `round-53.md` carry a curly-single quote, 0 in the other two, and the wider rule flags **no
  row the shipped rule does not**. So no finding is lost to this limit today.
- **What is *not* counted is a separate quotation.** Two spans separated by prose are two
  quotations, so `round-53.md`'s S184 row (three quotes of 17, 6 and 9 words, separated by
  "Geography paragraph, line 82:") is green. The rule fires on the joined reading, not on the
  number of quotations a row happens to carry.
- **A leading ellipsis is not a join.** `round-52.md:98` (S163) opens its quote with `“…the
  steep mountains …`, which is an ordinary omission marker; the tool does not report it. The
  `ellipsis-joined` rule requires words on both sides of the ellipsis.
- **Only `- S### ` rows are read.** A continuation row that does not start with `- S###` is not
  scanned, so a fix that moves a second quote onto its own unprefixed line would escape the
  check. The fix has to keep each row's joined quotation within the cap, or give the second
  quote its own `- S###` row.
- **One row, two runs.** `round-53.md:58` (S192) and `:62` (S194) carry a second, short run
  (4 words each); only the offending run is reported, and the row is printed once with the
  larger count.
- **The tool is a record, not a verdict.** It says nothing about whether a quote is faithful to
  its source; it only says how many words a reader receives inside one pair of quotation marks.

## What the L1 has to decide

1. **The filed lesson bytes.** The lane does not rewrite filed lesson bytes — round-53's own
   lesson keeps "Errata to the round-52 lesson's Gate (filed bytes not rewritten)". A command
   that must exit 0 over `corpus/lessons/round-53.md` will therefore stay red unless the
   lesson bytes are rewritten. Either (a) rewrite the 12 rows in `round-53.md`, the 7 in
   `round-52.md` and the 2 in `round-51.md` so each row's joined quotation is within the cap,
   or (b) run the tool as a record at the round where the defect is routed, with the errata in
   the new round's lesson, and not as an acceptance command over filed lessons. Wiring it into
   an acceptance command without one of those two is the risk I would name first.
2. **The rule's width.** If the L1 prefers the spot-check's narrower list (five S-ids), the
   rule has to change to count only the quoted passage and not the quoted anchor — but then the
   S200 and S214 shapes would no longer be caught either, and the routed defect returns. My
   recommendation is the rule as written, plus the L1's decision on point 1.
3. **Copy path.** `tools/check-gate-quotes.py` in the lane; the fixtures can go beside it
   (the lane's `tools/check-draft-ids.py` carries a `--selftest` instead of fixture files, and
   this tool keeps that convention).

## Files written

- `/fast/scratch/hyaku/kotodama-r54-a2/ExecGateQuoteCheck/check-gate-quotes.py` (the tool)
- `/fast/scratch/hyaku/kotodama-r54-a2/ExecGateQuoteCheck/fixtures/` (7 fixture files)
- `/fast/scratch/hyaku/kotodama-r54-a2/ExecGateQuoteCheck/runs.txt` (the transcript above)
- this report, `.ufo/waves/round-54/build-a2/ExecGateQuoteCheck.md`

No lane file was created, edited or deleted; no git or jj command was run that writes; no
network request was made.

## Tools

No install, upgrade or downgrade was made: the tool needs only the Python 3 standard library
(Python 3.14.8, already present). No `pacman`, `uv`, `cargo` or `npm` transaction was run.

## unrun / not attempted

- No build, lint or test gate was run (the parent owns the post-integration gate).
- I did not re-open any of the quoted sources; the tool checks the shape and length of the
  filed quotation, not its fidelity. The quotation texts in the table above are copied from the
  lesson bytes.
- I did not modify any lesson; no errata text for the twelve rows is proposed here beyond what
  the tool's own table names.
