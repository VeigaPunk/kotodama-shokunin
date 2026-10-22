#!/usr/bin/env python3
"""Draft-id fragment check for corpus entries (round 53, mined mistake repair).

A corpus entry must cite sources by their registered `corpus/SOURCES.md` id
(`S001`, `S002`, ...). Round 52's integration left unresolved draft-id
fragments in the speech-surrogates entry: the seat draft ids were never mapped
to registry rows, so the text kept bare `-N` fragments such as `(S159, -6)`.
The fragments read like citations but name no source, so the entry cites
nothing on that claim and every gate that counts cited rows is blind to it.

This tool reports every unresolved draft id it can see in Markdown text:

  F1  a `NEW-<SeatName>-<n>` token anywhere in the file;
  F2  a `, -N` (or `; -N`) fragment inside a *citation parenthesis* — a
      parenthesis whose text contains at least one registry id `S###`;
  F3  a `-N` fragment written directly after a registry id inside a
      parenthesis, with no separator (`(S157-2)`).

F2 and F3 are disjoint by construction: a fragment preceded by a comma or
semicolon is F2, a fragment glued to the registry id is F3.

Two predicates keep the tool from firing on text that only looks like a
fragment:

  * A registry id is one that stands alone. `S0718-68942020000100013` is a
    SciELO article pid and `S0271-5309` a DOI stem, so an id glued to a URL
    (`=`, `/`, `.`) or a DOI stem (`-`) is not a registry id and is not a
    citation parenthesis. F3 therefore also requires a short fragment (at
    most three digits), which a DOI stem never has.
  * A fragment must be a list element of the citation: after it comes `,`,
    `;`, `)` or the end of the line. `-40 °C` inside a citation parenthesis
    is a temperature, not a draft id.

A bare `, -N` that follows a non-registry id (`(KTD-AR-S-0005, -0006,
-0007)`) or that is not parenthesised at all (`DR-FUR-01, -02, -06 and -08`)
is a different numbering convention, not a draft-id fragment, and is not
reported.

Usage:
  python3 -B tools/check-draft-ids.py [--root LANE_ROOT] [PATH ...]
  python3 -B tools/check-draft-ids.py --selftest

With no PATH the tool scans every `*.md` file under `<root>/corpus/knowledge/`.
A PATH may be a Markdown file or a directory (scanned recursively). A
relative PATH is resolved against `--root`, not against the process working
directory.

Output: one line per finding, then `DRAFT_IDS: <n> findings`.
  DRAFT_ID <path>:<line> '<token>'
The token is the matched text as it appears in the file: `, -6` for an F2
fragment, `-2` for an F3 fragment, `NEW-Seat-1` for an F1 token.
Exit codes: 0 no findings; 1 findings; 2 could not evaluate (stderr
DRAFT_ID_INPUT_ERROR). Read-only, stdlib only.
"""
import argparse
import os
import re
import sys
import tempfile

# A registry id that stands alone: not glued to a URL, a DOI stem or a word.
SID = re.compile(r"(?<![\w/=.&#?%:-])S\d{3,}(?![\w-])")
# A draft token: NEW-<SeatName>-<n>.
NEW_ID = re.compile(r"\bNEW-[A-Za-z0-9_]+(?:-[A-Za-z0-9_]+)*-\d+\b")
# A separated fragment: `, -N` or `; -N`.
SEP_FRAG = re.compile(r"[,;][ \t]*-\d+\b")
# A glued fragment: `S###-N` with no separator.
ADJ_FRAG = re.compile(r"(?<![\w/=.&#?%:-])S\d{3,}[ \t]*(-\d{1,3})(?![\w-])")
# What may follow a fragment for it to be a list element of the citation.
TAIL = re.compile(r"[ \t]*(?:[,;)\]}]|$)")


def paren_groups(line):
    """Balanced parenthesis spans of one line as {start, end, parent} dicts.

    `start` is the index of the opening bracket, `end` the index just past the
    closing bracket, `parent` the start index of the enclosing group (or
    None). Groups are returned in closing order; use `find_group` to pick the
    innermost group containing a position.
    """
    stack = []
    groups = []
    for index, char in enumerate(line):
        if char == "(":
            stack.append((index, stack[-1][0] if stack else None))
        elif char == ")" and stack:
            start, parent = stack.pop()
            groups.append({"start": start, "end": index + 1, "parent": parent})
    return groups


def find_group(groups, position):
    """Innermost parenthesis group containing `position`, or None."""
    best = None
    for group in groups:
        if group["start"] < position < group["end"] - 1:
            if best is None or group["start"] > best["start"]:
                best = group
    return best


def group_chain(groups, group):
    """The group and its ancestors, innermost first."""
    chain = []
    by_start = {g["start"]: g for g in groups}
    current = group
    while current is not None:
        chain.append(current)
        current = by_start.get(current["parent"])
    return chain


def is_list_element(line, end):
    """True when a fragment ending at `end` closes a citation list element."""
    return TAIL.match(line, end) is not None


def scan_line(line, number):
    """Findings on one line as (line_number, column, token) tuples."""
    findings = []
    masked = list(line)
    for match in NEW_ID.finditer(line):
        findings.append((number, match.start(), match.group(0)))
        for index in range(match.start(), match.end()):
            masked[index] = " "
    masked = "".join(masked)
    groups = paren_groups(masked)
    citation = {}
    for group in groups:
        inner = masked[group["start"] + 1:group["end"] - 1]
        citation[group["start"]] = bool(SID.search(inner))
    for match in SEP_FRAG.finditer(masked):
        if not is_list_element(masked, match.end()):
            continue
        group = find_group(groups, match.start())
        if group is None:
            continue
        if not any(citation[g["start"]] for g in group_chain(groups, group)):
            continue
        findings.append((number, match.start(), match.group(0)))
    for match in ADJ_FRAG.finditer(masked):
        token = match.group(1)
        column = match.start(1)
        if not is_list_element(masked, match.end()):
            continue
        group = find_group(groups, column)
        if group is None:
            continue
        findings.append((number, column, token))
    findings.sort(key=lambda item: (item[1], item[2]))
    return findings


def scan_text(text):
    """Findings in a whole document as (line_number, column, token) tuples."""
    findings = []
    for number, line in enumerate(text.splitlines(), 1):
        findings.extend(scan_line(line, number))
    return findings


def resolve(root, target):
    """Resolve a CLI path against `--root`, so a relative path is root-relative."""
    return target if os.path.isabs(target) else os.path.join(root, target)


def markdown_files(root, paths):
    """Resolve CLI paths to a sorted list of Markdown files."""
    targets = list(paths) if paths else ["corpus/knowledge"]
    files = []
    for target in targets:
        target = resolve(root, target)
        if os.path.isdir(target):
            for folder, _dirs, names in os.walk(target):
                for name in sorted(names):
                    if name.endswith(".md"):
                        files.append(os.path.join(folder, name))
        elif os.path.isfile(target):
            files.append(target)
        else:
            raise ValueError(f"no such file or directory: {target}")
    return sorted(set(files))


def display_path(path, root):
    """Path as printed in a finding: root-relative when it lies under the root."""
    try:
        relative = os.path.relpath(path, root)
    except ValueError:
        return path
    return relative if not relative.startswith("..") else path


def check(root, paths):
    files = markdown_files(root, paths)
    findings = []
    for path in files:
        with open(path, encoding="utf-8") as handle:
            text = handle.read()
        for number, _column, token in scan_text(text):
            findings.append(f"DRAFT_ID {display_path(path, root)}:{number} '{token}'")
    return files, findings


def run(root, paths):
    try:
        files, findings = check(root, paths)
    except (OSError, ValueError, UnicodeDecodeError) as error:
        print(f"DRAFT_ID_INPUT_ERROR {error}", file=sys.stderr)
        return 2
    for line in findings:
        print(line)
    print(f"DRAFT_IDS: {len(findings)} findings")
    return 1 if findings else 0


def selftest():
    cases = [
        # name, text, expected findings
        ("clean", "the entry cites (S159) and S160 in prose.\n", 0),
        ("F1-new-token", "the row is NEW-ExecDraftIdChecker-1 in this draft.\n", 1),
        ("F1-new-token-in-paren", "cited (NEW-ScribeSec08-12) in passing.\n", 1),
        ("F1-hyphenated-seat-name", "the row is NEW-KotodamaR53-Scribe-3 here.\n", 1),
        ("F2-comma-fragment", "the drums reach people \"working their farms\" (S159, -6).\n", 1),
        ("F2-semicolon-fragment", "the range is \"up to five kilometres\" (S157; -2).\n", 1),
        ("F2-three-fragments", "the drum is a lossless code (S179, -5, -6, -7).\n", 3),
        ("F3-adjacent-fragment", "the quote sits in (S157-2) of the nomination.\n", 1),
        ("spec-example-S157", "the range is quoted in (S157, -2) of the form.\n", 1),
        ("spec-example-S179", "the drum is documented in (S179, -5, -6) here.\n", 2),
        ("neg-page-range", "the report prints (S145, pp. 2131-2134) for the row.\n", 0),
        ("neg-id-range", "the rows S134–S183 were opened this round.\n", 0),
        ("neg-id-range-ascii", "the rows S134-S183 were opened this round.\n", 0),
        ("neg-negative-number", "the sensor fails below -40 °C in winter.\n", 0),
        ("neg-negative-number-in-citation", "the row gives (S001, -40 °C) for the drum.\n", 0),
        ("neg-line-range", "the anchor is `phonetics-phonology.md:197-199`.\n", 0),
        ("neg-table-separator", "| channel | what it carries |\n|---|---|\n", 0),
        ("neg-hyphenated-word", "the co-speech channel and a well-known pair.\n", 0),
        ("neg-non-registry-paren", "preserved as the dated record it was (KTD-AR-S-0005, -0006, -0007).\n", 0),
        ("neg-non-registry-prose", "every consequence above was derived from DR-FUR-01, -02, -06 and -08.\n", 0),
        ("neg-to-verify", "the distance figure is (to-verify) for this instrument.\n", 0),
        ("neg-scielo-pid", "full text (https://www.scielo.cl/scielo.php?script=sci_arttext&pid=S0718-68942020000100013).\n", 0),
        ("neg-doi-stem", "the DOI (10.1016/S0271-5309(03)00012-0) ends the entry.\n", 0),
        ("neg-doi-in-parens", "the article (https://doi.org/10.4067/S0717-73562014000300003) is open.\n", 0),
        ("mixed", "(S159, -6) is a fragment; (S145, pp. 2131-2134) and -40 °C are not.\n", 1),
    ]
    failures = 0
    for name, body, want in cases:
        found = scan_text(body)
        ok = len(found) == want
        failures += not ok
        detail = ", ".join(f"{number}:{token}" for number, _column, token in found)
        print(f"{'PASS' if ok else 'FAIL'} {name} want={want} got={len(found)} [{detail}]")
    total = len(cases)
    print(f"SELFTEST: {total - failures}/{total} pass")
    failures += filesystem_controls()
    print("SELFTEST: filesystem controls", "PASS" if failures == 0 else "FAIL")
    return 1 if failures else 0


def filesystem_controls():
    """Controls that exercise the path resolution and the exit codes."""
    failures = 0
    with tempfile.TemporaryDirectory() as tmp:
        knowledge = os.path.join(tmp, "corpus", "knowledge", "p")
        os.makedirs(knowledge)
        with open(os.path.join(knowledge, "e.md"), "w", encoding="utf-8") as handle:
            handle.write("the quote sits in (S159, -6) here.\n")
        # A relative path is resolved against --root, not the process CWD.
        _files, findings = check(tmp, ["corpus/knowledge"])
        ok = len(findings) == 1 and findings[0].startswith(
            "DRAFT_ID corpus/knowledge/p/e.md:1 ")
        failures += not ok
        print(f"{'PASS' if ok else 'FAIL'} root-relative-path findings={len(findings)}")
        # An absolute path is accepted too.
        _files, findings = check(tmp, [knowledge])
        ok = len(findings) == 1
        failures += not ok
        print(f"{'PASS' if ok else 'FAIL'} absolute-path findings={len(findings)}")
        # A missing path is an input error, exit 2.
        got = run(tmp, ["no/such/dir"])
        ok = got == 2
        failures += not ok
        print(f"{'PASS' if ok else 'FAIL'} missing-path exit={got}")
        # A clean tree exits 0.
        with open(os.path.join(knowledge, "e.md"), "w", encoding="utf-8") as handle:
            handle.write("the quote sits in (S159) here.\n")
        got = run(tmp, ["corpus/knowledge"])
        ok = got == 0
        failures += not ok
        print(f"{'PASS' if ok else 'FAIL'} clean-tree exit={got}")
        # A tree with a fragment exits 1.
        with open(os.path.join(knowledge, "e.md"), "w", encoding="utf-8") as handle:
            handle.write("the quote sits in (S159, -6) here.\n")
        got = run(tmp, ["corpus/knowledge"])
        ok = got == 1
        failures += not ok
        print(f"{'PASS' if ok else 'FAIL'} defect-tree exit={got}")
    return failures


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--root", default=".")
    parser.add_argument("--selftest", action="store_true")
    parser.add_argument("paths", nargs="*")
    args = parser.parse_args()
    if args.selftest:
        return selftest()
    return run(args.root, args.paths)


if __name__ == "__main__":
    sys.exit(main())
