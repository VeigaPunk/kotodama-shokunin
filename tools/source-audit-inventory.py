#!/usr/bin/env python3
"""source-audit-inventory — read-only uncertainty inventory over the knowledge corpus.

Counts the lane's unresolved-claim marker (`to-verify`, corpus/QUALITY.md item 1)
across `corpus/knowledge/**/*.md` recursively and emits a deterministic JSON or
text inventory: per-file sha256, exact line and occurrence counts for the raw
string, the parenthesized marker `(to-verify)`, its detailed variant
`(to-verify: ...)`, and case variants; plus one record per occurrence carrying
a bounded context excerpt and a heuristic policy-versus-substantive class.

What this tool does NOT do, by construction:

  * It never treats the absence of a marker as verified scholarship. Every file
    record carries `resolved_scholarship: "not-assessed"`; a clean file is
    reported as zero marks, not as confirmed content.
  * It never clears, rewrites, or moves a marker. It opens corpus files
    read-only and has no code path that writes inside a scan root.
  * It never claims its policy/substantive split is a verdict. Every occurrence
    record is `heuristic: true` and `review_required: true`; the class is a
    sort key for human triage, not an adjudication of the underlying claim.

Metric definitions (the exact numbers, so they can be re-derived):

  raw_lines                lines containing the case-sensitive string
                           `to-verify` — the sum the SCORECARD command
                           `grep -rc 'to-verify' corpus/knowledge --include='*.md'`
                           produces
  raw_occurrences          case-sensitive occurrences (grep -o count)
  ci_occurrences           occurrences, case-insensitive
  case_variant_occurrences occurrences whose text is not exactly `to-verify`
  marker_occurrences       occurrences matching `\\(to-verify[^)]*\\)`, counted
                           case-insensitively (`(TO-VERIFY)` counts)
  bare_marker_occurrences  parenthesized marks whose content is the token
                           alone: `\\(to-verify\\)`, case-insensitive
  detailed_marker_occurrences  parenthesized marks carrying anything beyond
                           the token (`(to-verify: ...)`, `(to-verify locally)`)
                           — a named research target rather than a naked mark;
                           bare + detailed = markers by construction
  marker_lines             lines carrying at least one parenthesized mark
  unparenthesized_occurrences  ci_occurrences - marker_occurrences, i.e. the
                           case-insensitive complement of the marks: policy
                           prose, handoff instructions, file references. Both
                           terms of this subtraction are case-insensitive so
                           the result cannot go negative on a case variant.

Usage:
  source-audit-inventory.py                     # text summary, corpus/knowledge
  source-audit-inventory.py --json              # full inventory JSON on stdout
  source-audit-inventory.py --json --summary    # JSON without occurrence lists
  source-audit-inventory.py --root DIR          # scan another root (read-only)
  source-audit-inventory.py --baseline REV      # echo a revision into the JSON
  source-audit-inventory.py --selftest

Paths in the JSON are relative to the scan root and never absolute; symlinks
resolving outside the root are skipped and reported. The default root is
resolved from this file's location, so the tool runs correctly from any
directory; an explicit `--root` is used as given. Exit codes: 0 inventory
produced; 2 could-not-evaluate (root missing or not a directory, or a file that
is unreadable, not UTF-8 text, or not a regular file); 2 for argparse usage
errors. `--selftest` exits 0 when every planted control behaves as asserted and
1 otherwise. Stdlib only. Deterministic: no clock, no environment, no network
value enters the output.
"""

import argparse
import hashlib
import json
import re
import sys
import tempfile
from pathlib import Path

SCHEMA = "kotodama-source-audit-inventory/1"
REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_ROOT = str(REPO_ROOT / "corpus" / "knowledge")

MARK_RE = re.compile(r"to-verify", re.IGNORECASE)
MARK_LOWER = "to-verify"
MARKER_RE = re.compile(r"\(to-verify[^)]*\)", re.IGNORECASE)
BARE_MARKER_RE = re.compile(r"\(to-verify\)", re.IGNORECASE)
CONTEXT_LIMIT = 200
CLASSES = ("substantive-flag-candidate", "policy-use-mention", "needs-review")

# Policy/use-mention shapes: the line talks about the lane's mark discipline
# rather than attaching a mark to a reference claim. Heuristic patterns only —
# a hit is a triage hint, never a resolution.
POLICY_PATTERNS = (
    ("policy-instruction",
     re.compile(r"\b(flag|flags|flagged|mark|marks|marked|retain|retains|keep|keeps|carry|carried|leave)\b[^.]{0,80}?to-verify", re.IGNORECASE)),
    ("policy-instruction",
     re.compile(r"to-verify\b[^.]{0,60}?\b(items?|marks?|marker|flags?|before)\b", re.IGNORECASE)),
    ("code-span", re.compile(r"`\s*to-verify\s*`", re.IGNORECASE)),
    ("lane-file-reference",
     re.compile(r"(\.\./)+[A-Za-z/]*to-verify[A-Za-z-]*\.md|to-verify-(triage|protocol)[A-Za-z-]*", re.IGNORECASE)),
    ("vocabulary-definition",
     re.compile(r"(metadata_status|queue_state|outcome|support_status)\b[^\n]{0,80}?to-verify", re.IGNORECASE)),
    ("mark-legend", re.compile(r"^\s*\|[^|]*to-verify", re.IGNORECASE)),
)


def sha256_bytes(data):
    return hashlib.sha256(data).hexdigest()


def rel_posix(path, root):
    return path.relative_to(root).as_posix()


def iter_markdown(root):
    """Return (sorted regular-file paths, skipped observations). Read-only."""
    entries, skipped = [], []
    for path in sorted(root.rglob("*")):
        if path.is_dir():
            continue
        rel = path.relative_to(root).as_posix()
        if path.is_symlink():
            try:
                resolved = path.resolve()
                inside = resolved.is_relative_to(root.resolve())
            except OSError:
                inside = False
            if not inside:
                skipped.append({"path": rel, "reason": "symlink-outside-root"})
                continue
        if path.suffix != ".md":
            skipped.append({"path": rel, "reason": "not-markdown"})
            continue
        if not path.is_file():
            skipped.append({"path": rel, "reason": "not-regular-file"})
            continue
        entries.append(path)
    return entries, skipped


def governing_policy_hits(line, start, end):
    """Policy pattern names whose match span actually covers this occurrence.

    A pattern that fires elsewhere on the line (say a handoff instruction in
    the same sentence as an unrelated mark) does not govern this occurrence,
    so it must not drag a parenthesized mark out of the substantive class.
    """
    hits = []
    for name, pattern in POLICY_PATTERNS:
        for match in pattern.finditer(line):
            span_start, span_end = match.span()
            if span_start <= max(0, start - 1) and span_end >= end:
                hits.append(name)
                break
    return hits


def classify(line, start, end, matched_text, marker_match):
    """Heuristic policy-vs-substantive label. Never a verdict."""
    hits = governing_policy_hits(line, start, end)
    is_marker = marker_match is not None
    if is_marker and hits:
        return "needs-review", "policy shape covers a parenthesized mark: " + ",".join(hits)
    if is_marker:
        return "substantive-flag-candidate", "parenthesized mark with no governing policy pattern"
    if hits:
        return "policy-use-mention", "policy pattern(s): " + ",".join(hits)
    if matched_text != MARK_LOWER:
        return "needs-review", "case-variant mention outside parentheses"
    return "needs-review", "bare mention; no pattern fired"


def scan_text(text):
    lines = text.splitlines()
    occurrences = []
    counts = {key: 0 for key in (
        "raw_lines", "raw_occurrences", "ci_occurrences",
        "case_variant_occurrences", "marker_occurrences",
        "bare_marker_occurrences", "detailed_marker_occurrences", "marker_lines")}
    for number, line in enumerate(lines, start=1):
        marks = list(MARK_RE.finditer(line))
        if not marks:
            continue
        if any(match.group(0) == MARK_LOWER for match in marks):
            counts["raw_lines"] += 1
        line_marker = False
        for match in marks:
            start = match.start()
            end = match.end()
            marker_match = (MARKER_RE.match(line, start - 1)
                            if start and line[start - 1] == "(" else None)
            is_marker = marker_match is not None
            is_bare = is_marker and BARE_MARKER_RE.match(line, start - 1) is not None
            is_detailed = is_marker and not is_bare
            if match.group(0) == MARK_LOWER:
                counts["raw_occurrences"] += 1
            else:
                counts["case_variant_occurrences"] += 1
            counts["ci_occurrences"] += 1
            if is_marker:
                counts["marker_occurrences"] += 1
                line_marker = True
                if is_bare:
                    counts["bare_marker_occurrences"] += 1
                else:
                    counts["detailed_marker_occurrences"] += 1
            cls, basis = classify(line, start, end, match.group(0), marker_match)
            snippet = line.strip()
            truncated = len(snippet) > CONTEXT_LIMIT
            occurrences.append({
                "line": number,
                "column": start + 1,
                "matched_text": match.group(0),
                "form": "parenthesized" if is_marker else "bare",
                "variant": "lower" if match.group(0) == MARK_LOWER else "case-variant",
                "class": cls,
                "class_basis": basis,
                "heuristic": True,
                "review_required": True,
                "context": snippet[:CONTEXT_LIMIT] + ("\u2026" if truncated else ""),
                "context_truncated": truncated,
            })
        if line_marker:
            counts["marker_lines"] += 1
    counts["unparenthesized_occurrences"] = (counts["ci_occurrences"]
                                             - counts["marker_occurrences"])
    counts["resolved_scholarship"] = "not-assessed"
    counts["occurrences"] = occurrences
    counts["lines"] = len(lines)
    return counts


def inventory(root, baseline=None, include_occurrences=True):
    root = Path(root)
    if not root.is_dir():
        raise FileNotFoundError(f"{root}: not a directory")
    paths, skipped = iter_markdown(root)
    files = []
    totals = {key: 0 for key in (
        "files", "files_with_any_mark", "files_with_marker", "lines",
        "raw_lines", "raw_occurrences", "ci_occurrences",
        "case_variant_occurrences", "marker_occurrences",
        "bare_marker_occurrences", "detailed_marker_occurrences",
        "marker_lines", "unparenthesized_occurrences",
    )}
    class_totals = {name: 0 for name in CLASSES}
    for path in paths:
        data = path.read_bytes()
        try:
            text = data.decode("utf-8")
        except UnicodeDecodeError as exc:
            raise ValueError(f"{rel_posix(path, root)}: not UTF-8 text ({exc})") from exc
        counts = scan_text(text)
        occurrences = counts.pop("occurrences")
        for occurrence in occurrences:
            class_totals[occurrence["class"]] += 1
        record = {
            "path": rel_posix(path, root),
            "sha256": sha256_bytes(data),
            "size_bytes": len(data),
            **counts,
        }
        if include_occurrences:
            record["occurrences"] = occurrences
        files.append(record)
        totals["files"] += 1
        totals["lines"] += counts["lines"]
        for key in ("raw_lines", "raw_occurrences", "ci_occurrences",
                    "case_variant_occurrences", "marker_occurrences",
                    "bare_marker_occurrences", "detailed_marker_occurrences",
                    "marker_lines", "unparenthesized_occurrences"):
            totals[key] += counts[key]
        if counts["raw_occurrences"]:
            totals["files_with_any_mark"] += 1
        if counts["marker_occurrences"]:
            totals["files_with_marker"] += 1
    return {
        "schema": SCHEMA,
        "baseline_revision": baseline,
        "root": Path(root).as_posix(),
        "read_only": True,
        "deterministic": True,
        "caveats": {
            "marker_absence_is_not_verification": True,
            "markers_never_auto_cleared": True,
            "classification_is_heuristic_needs_review": True,
            "line_count_is_not_a_quality_score": True,
            "note": (
                "Zero marks mean only 'no marker found in this file'; the "
                "inventory does not read, validate, or clear referenced "
                "sources. Every class is a triage hint and every occurrence "
                "is flagged review_required. Multi-occurrence lines are "
                "counted once in *_lines and once per match in *_occurrences."
            ),
        },
        "totals": totals,
        "class_totals": class_totals,
        "skipped": skipped,
        "files": files,
    }


def render_text(inv):
    out = []
    totals = inv["totals"]
    out.append(
        f"source-audit-inventory: root={inv['root']} files={totals['files']} "
        f"raw_lines={totals['raw_lines']} raw_occurrences={totals['raw_occurrences']} "
        f"markers={totals['marker_occurrences']} (bare={totals['bare_marker_occurrences']} "
        f"detailed={totals['detailed_marker_occurrences']}) on {totals['marker_lines']} line(s)")
    out.append(
        "INFO behaviour: read-only, no marker cleared; all classes heuristic "
        "and review_required; marker absence is not verification")
    by_dir = {}
    for record in inv["files"]:
        top = record["path"].split("/", 1)[0] if "/" in record["path"] else "."
        bucket = by_dir.setdefault(top, {"files": 0, "raw_lines": 0, "markers": 0})
        bucket["files"] += 1
        bucket["raw_lines"] += record["raw_lines"]
        bucket["markers"] += record["marker_occurrences"]
    for top in sorted(by_dir):
        bucket = by_dir[top]
        out.append(
            f"INFO directory {top}: files={bucket['files']} "
            f"raw_lines={bucket['raw_lines']} markers={bucket['markers']}")
    for name in CLASSES:
        out.append(f"INFO class-heuristic {name}: occurrences={inv['class_totals'][name]}")
    for record in inv["files"]:
        if record["raw_occurrences"]:
            out.append(
                f"Marks {record['path']}: raw_lines={record['raw_lines']} "
                f"occurrences={record['raw_occurrences']} "
                f"markers={record['marker_occurrences']} "
                f"bare={record['bare_marker_occurrences']} "
                f"detailed={record['detailed_marker_occurrences']}")
        else:
            out.append(f"No-marks {record['path']}: no marker found; scholarship not assessed")
    for entry in inv["skipped"]:
        out.append(f"INFO skipped {entry['path']}: {entry['reason']}")
    out.append(
        f"INFO scan: files={totals['files']} with_marks={totals['files_with_any_mark']} "
        f"raw_lines={totals['raw_lines']} occurrences={totals['raw_occurrences']} "
        f"markers={totals['marker_occurrences']} "
        f"case_variants={totals['case_variant_occurrences']} skipped={len(inv['skipped'])}")
    return "\n".join(out) + "\n"


def digest_tree(root):
    root = Path(root)
    digests = {}
    for path in sorted(root.rglob("*")):
        if path.is_file():
            digests[path.relative_to(root).as_posix()] = sha256_bytes(path.read_bytes())
    return digests


POSITIVE = """# Fixture entry \u2014 marks present

- topic: Planted uncertainty marks for the inventory selftest; the claims below are fixtures and cite nothing real.
- sources: Fixture-only citation slot (to-verify).
- couples: verification \u2014 `./to-verify-triage-protocol.md`; no sibling writes in this fixture.

## Claims
- A fixture claim with a naked mark (to-verify).
- A fixture claim with two marks on one line (to-verify) and its sibling detail (to-verify: dated fixture locator).
- A fixture claim in caps (TO-VERIFY) and a title-case one (To-verify).
- Handoff rule: flag every to-verify item before it approaches the bible.
- Field vocabulary: `metadata_status` may be `checked` / `partial` / `to-verify`.
"""

NEGATIVE_CLEAN = """# Fixture entry \u2014 no marks at all

- topic: A planted negative control: this file contains no marker string, and the inventory must report zero marks without treating that as verified content.
- sources: Fixture Author (2001), *A Citation-Shaped String*, Example Press.
- couples: verification \u2014 `./provenance-audit-ledger-format.md`; no sibling writes in this fixture.

## Claims
- This sentence asserts a fixture fact and carries no marker, which is exactly the state the inventory must not upgrade.
"""

NEGATIVE_POLICY_ONLY = """# Fixture entry \u2014 policy mentions only

- topic: A planted control whose only mentions of the marker are instructions about the marker itself, never marks attached to a claim.
- sources: Fixture Author (2002), *Another Citation-Shaped String*, Example Press.
- couples: verification \u2014 `./to-verify-triage-protocol.md`; no sibling writes in this fixture.

## Handoff
- Every generated claim carries a marker; mark the field `to-verify` and hand the list over before reuse, and keep the to-verify items intact when the packet moves on.
"""

EXPECTED = {
    "positive/markers.md": {
        "raw_lines": 6, "raw_occurrences": 7, "ci_occurrences": 9,
        "marker_occurrences": 6,
        "bare_marker_occurrences": 5, "detailed_marker_occurrences": 1,
        "case_variant_occurrences": 2, "marker_lines": 4,
        "unparenthesized_occurrences": 3,
    },
    "negative/clean.md": {
        "raw_lines": 0, "raw_occurrences": 0, "ci_occurrences": 0,
        "marker_occurrences": 0,
        "bare_marker_occurrences": 0, "detailed_marker_occurrences": 0,
        "case_variant_occurrences": 0, "marker_lines": 0,
        "unparenthesized_occurrences": 0,
    },
    "negative/policy-only.md": {
        "raw_lines": 2, "raw_occurrences": 3, "ci_occurrences": 3,
        "marker_occurrences": 0,
        "bare_marker_occurrences": 0, "detailed_marker_occurrences": 0,
        "case_variant_occurrences": 0, "marker_lines": 0,
        "unparenthesized_occurrences": 3,
    },
}

MARKDOWN_SET = ["negative/clean.md", "negative/policy-only.md", "positive/markers.md"]


def selftest():
    failures = []

    def check(condition, label):
        if not condition:
            failures.append(label)

    with tempfile.TemporaryDirectory(prefix="source-audit-inventory-") as tmp:
        root = Path(tmp) / "scratch"
        (root / "positive").mkdir(parents=True)
        (root / "negative").mkdir()
        (root / "positive" / "markers.md").write_text(POSITIVE, encoding="utf-8")
        (root / "negative" / "clean.md").write_text(NEGATIVE_CLEAN, encoding="utf-8")
        (root / "negative" / "policy-only.md").write_text(NEGATIVE_POLICY_ONLY, encoding="utf-8")
        (root / "notes.txt").write_text("to-verify\n", encoding="utf-8")
        before = digest_tree(root)

        try:
            inv = inventory(root, baseline="selftest")
        except Exception as exc:  # pragma: no cover - surfaced as a failure
            return 1, [f"inventory raised on the control tree: {exc!r}"]
        check(before == digest_tree(root), "scan wrote to the scanned tree (digests changed)")

        first = json.dumps(inv, sort_keys=True, ensure_ascii=False)
        second = json.dumps(inventory(root, baseline="selftest"), sort_keys=True, ensure_ascii=False)
        check(first == second, "two scans of the same tree produced different JSON")

        paths = [record["path"] for record in inv["files"]]
        check(paths == MARKDOWN_SET, f"expected markdown set only, got {paths}")
        check(all(not Path(record["path"]).is_absolute() for record in inv["files"]),
              "an absolute path leaked into the inventory")
        check(any(item["path"] == "notes.txt" for item in inv["skipped"]),
              "non-markdown file was not reported as skipped")

        by_path = {record["path"]: record for record in inv["files"]}
        for path, expected in EXPECTED.items():
            record = by_path[path]
            for key, want in expected.items():
                check(record[key] == want,
                      f"{path}: {key} expected {want}, got {record[key]}")
            check(record["resolved_scholarship"] == "not-assessed",
                  f"{path}: resolved_scholarship is not 'not-assessed'")
            check(bool(re.fullmatch(r"[0-9a-f]{64}", record["sha256"])),
                  f"{path}: sha256 is not a 64-char hex digest")

        clean = by_path["negative/clean.md"]
        check(clean["raw_occurrences"] == 0 and clean["marker_occurrences"] == 0,
              "negative control reported marks")
        check(clean["occurrences"] == [], "negative control reported occurrence records")
        policy = by_path["negative/policy-only.md"]
        check(policy["marker_occurrences"] == 0,
              "policy-only control was counted as a parenthesized marker")
        check(all(occurrence["class"] != "substantive-flag-candidate"
                  for occurrence in policy["occurrences"]),
              "policy-only control produced a substantive-flag-candidate")
        positive = by_path["positive/markers.md"]
        classes = {occurrence["class"] for occurrence in positive["occurrences"]}
        check("substantive-flag-candidate" in classes,
              "positive control produced no substantive-flag-candidate")
        check("policy-use-mention" in classes,
              "positive control produced no policy-use-mention")
        check(all(occurrence["review_required"] and occurrence["heuristic"]
                  for record in inv["files"] for occurrence in record["occurrences"]),
              "an occurrence record is not marked heuristic/review_required")
        columns = [(occurrence["line"], occurrence["column"])
                   for occurrence in positive["occurrences"]]
        check(len(columns) == len(set(columns)), "duplicate occurrence positions reported")
        check(all(occurrence["context"].strip() for occurrence in positive["occurrences"]),
              "an occurrence lost its context excerpt")

        totals = inv["totals"]
        check(totals["raw_lines"] == sum(item["raw_lines"] for item in EXPECTED.values()),
              f"totals.raw_lines wrong: {totals['raw_lines']}")
        check(totals["raw_occurrences"] == sum(item["raw_occurrences"] for item in EXPECTED.values()),
              f"totals.raw_occurrences wrong: {totals['raw_occurrences']}")
        check(totals["ci_occurrences"] == sum(item["ci_occurrences"] for item in EXPECTED.values()),
              f"totals.ci_occurrences wrong: {totals['ci_occurrences']}")
        check(totals["marker_lines"] == EXPECTED["positive/markers.md"]["marker_lines"],
              f"totals.marker_lines wrong: {totals['marker_lines']}")
        check(totals["unparenthesized_occurrences"]
              == totals["ci_occurrences"] - totals["marker_occurrences"],
              "unparenthesized_occurrences is not ci_occurrences minus markers")
        check(totals["bare_marker_occurrences"] + totals["detailed_marker_occurrences"]
              == totals["marker_occurrences"],
              "bare + detailed does not equal marker_occurrences")
        for path, record in by_path.items():
            check(record["bare_marker_occurrences"] + record["detailed_marker_occurrences"]
                  == record["marker_occurrences"],
                  f"{path}: bare + detailed does not equal marker_occurrences")
            check(record["unparenthesized_occurrences"] >= 0,
                  f"{path}: unparenthesized_occurrences went negative")
        check(totals["files_with_marker"] == 1 and totals["files_with_any_mark"] == 2,
              f"files_with_marker/any_mark wrong: {totals['files_with_marker']}/"
              f"{totals['files_with_any_mark']}")
        caveats = inv["caveats"]
        check(caveats["marker_absence_is_not_verification"] is True, "absence caveat missing")
        check(caveats["markers_never_auto_cleared"] is True, "no-auto-clear caveat missing")
        check(caveats["classification_is_heuristic_needs_review"] is True,
              "heuristic-class caveat missing")
        check(inv["read_only"] is True and inv["deterministic"] is True,
              "read_only/deterministic flags missing")
        check(json.loads(json.dumps(inv))["schema"] == SCHEMA, "schema round-trip failed")

        # Control: the scan root itself is never modified, checked again at the
        # directory level, and an unwritable-root scan still succeeds.
        check(digest_tree(root) == before, "control tree changed during the whole selftest")

    # CLI-level controls on real exit codes (subprocess-free: main() is called).
    with tempfile.TemporaryDirectory(prefix="source-audit-inventory-cli-") as tmp:
        missing = str(Path(tmp) / "does-not-exist")
        check(main(["--root", missing]) == 2, "missing root did not exit 2")
        check(main(["--root", missing, "--json"]) == 2, "missing root --json did not exit 2")
        bad = Path(tmp) / "bad"
        bad.mkdir()
        (bad / "invalid.md").write_bytes(b"# entry\n\xff\xfe not utf-8 \n")
        check(main(["--root", str(bad)]) == 2, "non-UTF-8 file did not exit 2")
        empty = Path(tmp) / "empty"
        empty.mkdir()
        check(main(["--root", str(empty)]) == 0, "empty root did not exit 0")
        scan = Path(tmp) / "scan"
        scan.mkdir()
        (scan / "one.md").write_text("A claim (to-verify).\n", encoding="utf-8")
        check(main(["--root", str(scan)]) == 0, "normal scan did not exit 0")
        check(digest_tree(scan) == {"one.md": sha256_bytes(b"A claim (to-verify).\n")},
              "CLI scan modified its root")

    return (0 if not failures else 1), failures


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="source-audit-inventory.py",
        description="Read-only, deterministic to-verify inventory over corpus/knowledge/**/*.md.")
    parser.add_argument("--root", default=DEFAULT_ROOT,
                        help=f"scan root (default: {DEFAULT_ROOT}); opened read-only")
    parser.add_argument("--json", action="store_true", help="emit the full inventory JSON")
    parser.add_argument("--summary", action="store_true",
                        help="with --json, omit per-occurrence records")
    parser.add_argument("--baseline", default=None,
                        help="revision label echoed into the JSON (no effect on the scan)")
    parser.add_argument("--selftest", action="store_true",
                        help="run planted positive/negative controls and exit")
    args = parser.parse_args(argv)

    if args.selftest:
        code, failures = selftest()
        if code:
            for failure in failures:
                print(f"SELFTEST FAIL: {failure}", file=sys.stderr)
            print(f"INFO selftest: failed={len(failures)}")
        else:
            print("SELFTEST PASS: 3 planted entries, exact counts, policy/substantive "
                  "split, no-write and determinism checks, missing-root, empty-root and "
                  "non-UTF-8 exit-code controls")
        return code

    output = sys.stdout
    if args.json:
        output = open(sys.stdout.fileno(), "w", encoding="utf-8", closefd=False)
    try:
        inv = inventory(args.root, baseline=args.baseline,
                        include_occurrences=not args.summary)
    except FileNotFoundError as exc:
        print(f"CANNOT-EVALUATE: {exc}", file=sys.stderr)
        return 2
    except ValueError as exc:
        print(f"CANNOT-EVALUATE: {exc}", file=sys.stderr)
        return 2
    except OSError as exc:
        print(f"CANNOT-EVALUATE: {exc}", file=sys.stderr)
        return 2

    if args.json:
        json.dump(inv, output, indent=2, ensure_ascii=False, sort_keys=False)
        output.write("\n")
    else:
        output.write(render_text(inv))
    return 0


if __name__ == "__main__":
    sys.exit(main())
