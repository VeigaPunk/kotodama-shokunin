#!/usr/bin/env python3
"""provenance-audit — kotodama-shokunin corpus-scanner gate.

Scans corpus entry documents (not culture packets) against this lane's
admission bar for provenance apparatus, corpus/QUALITY.md items 1-3, and the
verdict/disposition vocabulary of
corpus/knowledge/verification/provenance-audit-ledger-format.md:

  * `- topic:` header line absent                        -> missing-topic
  * `- sources:` header line absent                      -> missing-sources
  * `- sources:` present but names no source             -> empty-sources
  * `- couples:` header line absent                      -> missing-couples
  * `- couples:` present but names nothing it connects   -> empty-couples
  * no calibration vocabulary anywhere in the entry      -> missing-calibration

The `empty-couples` check follows corpus/QUALITY.md item 3 ("An entry that
couples nothing is reference, not craft; it must say so"): a silently blank
coupling field is a defect, while an entry that names its lack of couplings
in prose still passes the header check. `missing-calibration` fires only when
the word `calibrat*` is absent entirely — the gate cannot judge whether the
named status is warranted, so an entry that names calibration only in running
prose passes with an `INFO calibration-prose-only` observation instead of a
finding. The gate is read-only: it never writes to the corpus.

A header field's content is the text after its colon plus any following
indented continuation lines (the house style wraps long fields and uses a
blank `- sources:` line followed by an indented source list), ending at the
next top-level line. A value that is only whitespace or a placeholder
(`none`, `n/a`, `tbd`, `todo`, `unknown`, `-`, `(to-verify)`) counts as empty.

`to-verify` marks are counted per entry and reported as inventory, never as
findings: the ledger format keeps unresolved marks legitimate (verdict
`unverified`, disposition `hold`, §5), so a mark is a backlog item for the
triage protocol, not a conformance defect. Counts are taken at run time and
are case-insensitive; a live corpus can change between runs.

Output — one line each on stdout:

  FINDING <id>: <path>: <message>
  INFO to-verify-count: <path>: <occurrences> mark(s) on <lines> line(s)
  INFO calibration-prose-only: <path>: <detail>
  CANNOT-EVALUATE: <path>: <reason>
  INFO scan: files=<n> marks=<n> mark-lines=<n> findings=<n> blocked=<n>

Exit codes: 0 clean; 1 findings; 2 could-not-evaluate for at least one path
(missing, unreadable, not UTF-8 text, or not an entry document — an empty file
or a text file with neither a Markdown heading nor a lane header line), and
also 2 for argparse usage errors. `--selftest` exits 0 when the fixture tree
passes and 1 when it fails.

Usage:
  provenance-audit.py <corpus-file> [more files ...]
  provenance-audit.py <directory> [more directories ...]   # *.md, sorted
  provenance-audit.py --selftest

`--selftest` regenerates tools/gates/fixtures/provenance/ (one clean entry
plus one entry per planted defect) and the committed expected-ID lists
tools/gates/fixtures/provenance.expected and
tools/gates/fixtures/provenance-audit.expected (one ID per line), then
asserts: exit 1 on the defect tree with exactly the planted IDs, exit 0 with
no findings on the clean entry, its mark count, and exit 2 on a missing path.

Spec: corpus/knowledge/verification/provenance-audit-ledger-format.md;
admission bar: corpus/QUALITY.md. Stdlib only.
"""

import argparse
import re
import sys
from pathlib import Path

FIELD_NAMES = ("topic", "sources", "couples")
FIELD_RE = re.compile(r"^- (topic|sources|couples):[ \t]*(.*)$")
INDENT_RE = re.compile(r"^[ \t]+\S")
HEADING_RE = re.compile(r"^#{1,6}[ \t]+\S")
MARK_RE = re.compile(r"to-verify", re.IGNORECASE)
COUNT_LINE_RE = re.compile(
    r"^INFO to-verify-count: (?P<path>.+): (?P<marks>\d+) mark\(s\) on "
    r"(?P<lines>\d+) line\(s\)$"
)
CALIB_WORD_RE = re.compile(r"calibrat", re.IGNORECASE)
PLACEHOLDERS = {
    "", "-", "--", "\u2014", "?", "??", "???", "n/a", "na", "none", "null",
    "tbd", "todo", "unknown", "to-verify", "(to-verify)", "((to-verify))",
}

# Calibration apparatus shapes (reported as INFO when a file names calibration
# only in running prose; a finding is raised only when the entry has no
# calibration vocabulary at all).
CALIB_HEADING_RE = re.compile(r"^#{1,6}[ \t]+.*calibrat", re.IGNORECASE)
CALIB_TABLE_RE = re.compile(r"^\s*\|.*calibrat", re.IGNORECASE)
CALIB_BOLD_RE = re.compile(r"\*\*[^*]*calibrat[^*]*\*\*", re.IGNORECASE)
CALIB_LABEL_RE = re.compile(r"^\s*[-*+][ \t]+[^:|]*calibrat[^:]*:", re.IGNORECASE)

FINDING_ORDER = (
    "missing-topic",
    "missing-sources",
    "empty-sources",
    "missing-couples",
    "empty-couples",
    "missing-calibration",
)

FIXTURE_SUBDIR = ("fixtures", "provenance")
EXPECTED_PATHS = ("fixtures/provenance.expected", "fixtures/provenance-audit.expected")

GOOD_ENTRY = """# Fixture entry \u2014 well formed

- topic: A well-formed fixture entry for the provenance-audit gate: header lines, a non-empty source block, a calibration section, and two deliberate unresolved marks for the counter selftest. Gate machinery only, never a citation.
- sources: Fixture Author (2001), *A Citation Block Shaped Like the House Style*, Example Press, ISBN 9780000000001; Fixture Author (2002), "Second Fixture Claim," *Journal of Gate Fixtures* 1(1): 1\u20132, doi:10.0000/gate.1. Fixture-only names; no real work is cited or implied.
- couples: language \u2014 `../linguistics/historical-linguistics.md`; verification \u2014 `./provenance-audit-ledger-format.md`; sibling boundary \u2014 gate fixtures change no sibling file and decide no canon.

## Scope and calibration
- Labels used here: **fixture** = test data for this gate; an unresolved proposition in a real entry stays visibly flagged rather than asserted.
- Calibration rule: a gate fixture is machinery, not reference knowledge, and must never be handed to lore-shokunin as a source.
- Two inventory marks stay deliberately unresolved below so the counter has something to report, and this section names the fixture's own status.

## Coupling map
| Channel | What it carries | Limit |
|---|---|---|
| Header block | topic, sources, couples | None of the three asserts a fact |
| Calibration line | scope and status labels | A label is not evidence |

- Body prose here is a placeholder shape; a real entry would carry cited claims and a source key (to-verify wording of one dating detail).
- Further unresolved detail planted for the counter (to-verify).
"""

DEFECT_MISSING_TOPIC = """# Fixture entry \u2014 topic line missing

- sources: Fixture Author (2001), *A Citation Block Shaped Like the House Style*, Example Press. Fixture-only name.
- couples: method \u2014 `./provenance-audit-ledger-format.md`; no sibling writes.

## Scope and calibration
- Planted defect: the header line that opens the topic field is absent; every other header check should pass.
- Calibration rule: fixture machinery only; the file asserts nothing about the real world.
"""

DEFECT_MISSING_SOURCES = """# Fixture entry \u2014 sources line missing

- topic: A fixture entry whose provenance field is absent while the topic, coupling, and calibration fields are present.
- couples: method \u2014 `./provenance-audit-ledger-format.md`; no sibling writes.

## Scope and calibration
- Planted defect: no line opens the provenance field, so the gate cannot see a source block at all.
- Calibration rule: fixture machinery only; the heading below holds no real reference.

## Source key
- (fixture placeholder; no real source is named in this file)
"""

DEFECT_EMPTY_SOURCES = """# Fixture entry \u2014 empty sources field

- topic: A fixture entry whose provenance field opens but names no source, not even on an indented continuation line.
- sources:
- couples: method \u2014 `./provenance-audit-ledger-format.md`; no sibling writes.

## Scope and calibration
- Planted defect: the provenance field closes empty; a placeholder is not a citation.
- Calibration rule: fixture machinery only; the file asserts nothing about the real world.
"""

DEFECT_MISSING_COUPLES = """# Fixture entry \u2014 couples line missing

- topic: A fixture entry whose coupling field is absent while the other header fields and the calibration section are present.
- sources: Fixture Author (2001), *A Citation Block Shaped Like the House Style*, Example Press. Fixture-only name.

## Scope and calibration
- Planted defect: no coupling line is present, so this entry never names the systems it connects.
- Calibration rule: fixture machinery only; the file asserts nothing about the real world.
"""

DEFECT_EMPTY_COUPLES = """# Fixture entry \u2014 empty couples field

- topic: A fixture entry whose coupling field opens and names nothing it connects.
- sources: Fixture Author (2001), *A Citation Block Shaped Like the House Style*, Example Press. Fixture-only name.
- couples:

## Scope and calibration
- Planted defect: the coupling field closes empty; corpus/QUALITY.md item 3 requires an entry that couples nothing to say so.
- Calibration rule: fixture machinery only; the file asserts nothing about the real world.
"""

DEFECT_MISSING_CALIBRATION = """# Fixture entry \u2014 status apparatus missing

- topic: A fixture entry with header fields and a source block whose body never names a status vocabulary, an uncertainty label, or a contested-framework flag.
- sources: Fixture Author (2001), *A Citation Block Shaped Like the House Style*, Example Press. Fixture-only name.
- couples: method \u2014 `./provenance-audit-ledger-format.md`; no sibling writes.

## Coupling map
| Channel | What it carries | Limit |
|---|---|---|
| Header block | topic, sources, couples | None of the three asserts a fact |

- Planted defect: no section, bold label, table column, or labelled clause names the entry's evidentiary status anywhere in this file.
"""

FIXTURES = (
    ("good-entry.md", GOOD_ENTRY),
    ("defect-missing-topic.md", DEFECT_MISSING_TOPIC),
    ("defect-missing-sources.md", DEFECT_MISSING_SOURCES),
    ("defect-empty-sources.md", DEFECT_EMPTY_SOURCES),
    ("defect-missing-couples.md", DEFECT_MISSING_COUPLES),
    ("defect-empty-couples.md", DEFECT_EMPTY_COUPLES),
    ("defect-missing-calibration.md", DEFECT_MISSING_CALIBRATION),
)

EXPECTED_IDS = (
    "missing-topic",
    "missing-sources",
    "empty-sources",
    "missing-couples",
    "empty-couples",
    "missing-calibration",
)

EXPECTED_BY_FILE = {
    "defect-missing-topic.md": ("missing-topic",),
    "defect-missing-sources.md": ("missing-sources",),
    "defect-empty-sources.md": ("empty-sources",),
    "defect-missing-couples.md": ("missing-couples",),
    "defect-empty-couples.md": ("empty-couples",),
    "defect-missing-calibration.md": ("missing-calibration",),
    "good-entry.md": (),
}

EXPECTED_MARKS = {
    "good-entry.md": 2,
    "defect-missing-topic.md": 0,
    "defect-missing-sources.md": 0,
    "defect-empty-sources.md": 0,
    "defect-missing-couples.md": 0,
    "defect-empty-couples.md": 0,
    "defect-missing-calibration.md": 0,
}


class CouldNotEvaluate(Exception):
    """Raised when a path cannot be read or is not an entry document."""


def field_block(lines, name):
    """Return (present, content) for a `- <name>:` header field."""
    for index, line in enumerate(lines):
        match = FIELD_RE.match(line)
        if match and match.group(1) == name:
            parts = [match.group(2).strip()]
            for following in lines[index + 1:]:
                if not following.strip():
                    continue
                if FIELD_RE.match(following):
                    break
                if INDENT_RE.match(following):
                    parts.append(following.strip())
                    continue
                break
            return True, " ".join(part for part in parts if part)
    return False, ""


def is_empty_value(content):
    """A header value is empty when it is blank or only a placeholder."""
    return content.strip().strip("`*_ ").lower() in PLACEHOLDERS


def calibration_apparatus(text):
    """Name the first calibration apparatus shape found, else None."""
    for line in text.splitlines():
        if CALIB_HEADING_RE.match(line):
            return "heading"
        if CALIB_TABLE_RE.match(line):
            return "table-column"
        if CALIB_BOLD_RE.search(line):
            return "bold-label"
        if CALIB_LABEL_RE.match(line):
            return "labelled-line"
    return None


def read_entry_text(display, path):
    """Read one entry document, or raise CouldNotEvaluate with a reason."""
    try:
        raw = path.read_bytes()
    except OSError as exc:
        raise CouldNotEvaluate(f"unreadable ({exc.strerror or exc})")
    try:
        text = raw.decode("utf-8-sig")
    except UnicodeDecodeError:
        raise CouldNotEvaluate("not UTF-8 text")
    if not text.strip():
        raise CouldNotEvaluate("empty file")
    if not HEADING_RE.search(text) and not FIELD_RE.search(text):
        raise CouldNotEvaluate(
            "not a corpus entry document (no Markdown heading, no header line)"
        )
    return text


def check_text(text):
    """Return (findings, mark occurrences, mark lines, calibration info)."""
    lines = text.splitlines()
    findings = {}

    present, content = field_block(lines, "topic")
    if not present:
        findings["missing-topic"] = "no '- topic:' header line"

    present, content = field_block(lines, "sources")
    if not present:
        findings["missing-sources"] = "no '- sources:' header line"
    elif is_empty_value(content):
        findings["empty-sources"] = (
            "'- sources:' names no source (blank or placeholder value only)"
        )

    present, content = field_block(lines, "couples")
    if not present:
        findings["missing-couples"] = "no '- couples:' header line"
    elif is_empty_value(content):
        findings["empty-couples"] = (
            "'- couples:' names nothing it connects (blank or placeholder value only)"
        )

    if not CALIB_WORD_RE.search(text):
        findings["missing-calibration"] = (
            "no calibration vocabulary anywhere (no status section, label, or mention)"
        )

    occurrences = len(MARK_RE.findall(text))
    mark_lines = sum(1 for line in lines if MARK_RE.search(line))
    apparatus = calibration_apparatus(text)
    return findings, occurrences, mark_lines, apparatus


def expand_paths(raw_paths):
    """Expand argv into (display, Path) pairs and block reasons."""
    targets = []
    blocked = []
    for raw in raw_paths:
        path = Path(raw)
        if path.is_dir():
            found = sorted(p for p in path.rglob("*.md") if p.is_file())
            if not found:
                blocked.append((raw, "directory contains no *.md entry files"))
                continue
            targets.extend((str(p), p) for p in found)
        else:
            targets.append((raw, path))
    return targets, blocked


def run_paths(raw_paths):
    """Evaluate paths; return (exit code, output lines)."""
    outputs = []
    code = 0
    targets, blocked = expand_paths(raw_paths)
    for display, reason in blocked:
        outputs.append(f"CANNOT-EVALUATE: {display}: {reason}")
        code = 2

    total_marks = 0
    total_mark_lines = 0
    total_findings = 0
    evaluated = 0
    for display, path in targets:
        if not path.exists() or not path.is_file():
            outputs.append(f"CANNOT-EVALUATE: {display}: not a readable file")
            code = 2
            continue
        try:
            text = read_entry_text(display, path)
        except CouldNotEvaluate as exc:
            outputs.append(f"CANNOT-EVALUATE: {display}: {exc}")
            code = 2
            continue

        evaluated += 1
        findings, occurrences, mark_lines, apparatus = check_text(text)
        for finding_id in FINDING_ORDER:
            if finding_id in findings:
                outputs.append(f"FINDING {finding_id}: {display}: {findings[finding_id]}")
                total_findings += 1
        outputs.append(
            f"INFO to-verify-count: {display}: {occurrences} mark(s) on {mark_lines} line(s)"
        )
        if CALIB_WORD_RE.search(text) and apparatus is None:
            outputs.append(
                f"INFO calibration-prose-only: {display}: calibration vocabulary "
                "appears only in running prose, not in a heading, table column, or labelled line"
            )
        total_marks += occurrences
        total_mark_lines += mark_lines

    if code == 0 and total_findings:
        code = 1
    outputs.append(
        "INFO scan: files={} marks={} mark-lines={} findings={} blocked={}".format(
            evaluated, total_marks, total_mark_lines, total_findings, len(blocked)
        )
    )
    return code, outputs


def write_fixtures(root):
    """Regenerate the fixture tree and both committed expected-ID lists."""
    fixture_dir = root.joinpath(*FIXTURE_SUBDIR)
    fixture_dir.mkdir(parents=True, exist_ok=True)
    for name, body in FIXTURES:
        (fixture_dir / name).write_text(body, encoding="utf-8")
    expected_body = "".join(f"{finding_id}\n" for finding_id in EXPECTED_IDS)
    for relative in EXPECTED_PATHS:
        target = root / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(expected_body, encoding="utf-8")
    return fixture_dir


def split_finding(line):
    """Return (finding_id, path) from a FINDING output line."""
    finding_id, rest = line[len("FINDING "):].split(":", 1)
    return finding_id.strip(), rest.strip().split(":")[0].strip()


def selftest(root):
    """Build the fixtures, run the gate on them, assert the planted outcome."""
    failures = []
    fixture_dir = write_fixtures(root)
    fixture_paths = [str(fixture_dir / name) for name, _ in FIXTURES]

    for relative in EXPECTED_PATHS:
        expected_file = root / relative
        body = expected_file.read_text(encoding="utf-8")
        if body != "".join(f"{finding_id}\n" for finding_id in EXPECTED_IDS):
            failures.append(f"{relative} does not match the embedded expected IDs")

    code, lines = run_paths([str(fixture_dir)])
    findings = [line for line in lines if line.startswith("FINDING ")]
    found_ids = [split_finding(line)[0] for line in findings]
    found_pairs = sorted((split_finding(line)[0], split_finding(line)[1]) for line in findings)
    expected_pairs = sorted(
        (finding_id, str(fixture_dir / name))
        for name, ids in EXPECTED_BY_FILE.items()
        for finding_id in ids
    )

    print("selftest: defect-tree run")
    for line in lines:
        print(f"  {line}")

    if code != 1:
        failures.append(f"defect tree exited {code}, expected 1")
    if sorted(found_ids) != sorted(EXPECTED_IDS):
        failures.append(
            f"defect tree findings {sorted(found_ids)} != planted {sorted(EXPECTED_IDS)}"
        )
    if found_pairs != expected_pairs:
        failures.append("defect tree finding attribution to fixture files is wrong")

    counts = {}
    for line in lines:
        match = COUNT_LINE_RE.match(line)
        if match:
            counts[match.group("path")] = int(match.group("marks"))
            if int(match.group("lines")) > int(match.group("marks")):
                failures.append(f"mark-line count exceeds mark count in: {line}")
    for name, expected in EXPECTED_MARKS.items():
        display = str(fixture_dir / name)
        if counts.get(display) != expected:
            failures.append(
                f"{name}: to-verify count {counts.get(display)} != expected {expected}"
            )

    good_path = str(fixture_dir / "good-entry.md")
    code_good, lines_good = run_paths([good_path])
    print("selftest: clean-entry run")
    for line in lines_good:
        print(f"  {line}")
    if code_good != 0:
        failures.append(f"clean entry exited {code_good}, expected 0")
    if any(line.startswith("FINDING ") for line in lines_good):
        failures.append("clean entry produced findings")

    missing_path = str(fixture_dir / "definitely-absent.md")
    code_missing, _ = run_paths([missing_path])
    if code_missing != 2:
        failures.append(f"missing path exited {code_missing}, expected 2")

    if failures:
        for failure in failures:
            print(f"SELFTEST FAIL: {failure}")
        return 1
    print(
        "SELFTEST OK: {} fixture file(s), planted IDs {}, exit 1 on the defect "
        "tree, exit 0 on the clean entry, exit 2 on a missing path".format(
            len(fixture_paths), ", ".join(EXPECTED_IDS)
        )
    )
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="provenance-audit.py",
        description="Scan kotodama-shokunin corpus entries for provenance apparatus.",
    )
    parser.add_argument("paths", nargs="*", help="corpus entry files or directories of *.md")
    parser.add_argument(
        "--selftest",
        action="store_true",
        help="regenerate tools/gates/fixtures/provenance/ and self-check",
    )
    args = parser.parse_args(argv)
    root = Path(__file__).resolve().parent

    if args.selftest:
        return selftest(root)
    if not args.paths:
        parser.error("give at least one corpus file or directory, or --selftest")

    code, lines = run_paths(args.paths)
    for line in lines:
        print(line)
    return code


if __name__ == "__main__":
    sys.exit(main())