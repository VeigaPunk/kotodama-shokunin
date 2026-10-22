#!/usr/bin/env python3
"""Round-56 claim O acceptance (operability, capability: HTML character references in Gate rows).
Run from the lane root:

  python3 -B reports/round-56/accept-o.py [--root DIR]

The checker under test is tools/check-gate-quotes.py. A finding line is
`<path>:<line> <S-id> <detail>`; the class this claim adds prints `html-entity` as its detail;
over-cap and ellipsis-joined findings keep their `words=<n>` detail and the round-55 classes print
`doubled-locator` and `truncated-grounds`. The last stdout line of a lesson run is
`GATE_QUOTES: <n> findings`. Every finding is compared as a (line, S-id, detail) triple.
Routed by the round-55 verifier spot-check (corpus/lessons/round-55-verifier-spotcheck.md §5 item 6):
Gate Grounds carry HTML entities the checker does not decode.
One leg per mechanical clause of claim O (reports/round-56/claims.json), each printed with PASS or
FAIL:
  ENTITY    on corpus/lessons/round-55.md the html-entity triples are exactly the 16 in ENTITY_WANT,
            each once (the Gate rows that carry an HTML character reference: lines 72 S288 ... 141
            S357); triples are compared as multisets, so a finding per reference rather than per row
            fails
  NOFALSE   on corpus/lessons/round-55.md no finding of any class other than html-entity (the
            html-entity triples themselves are ENTITY's)
  EXIT      the round-55 run and the entities-fixture run each exit 1 (findings), not 0 or 2
  DECODE    on reports/round-56/fixtures/lessons/entities.md (its registry is
            reports/round-56/fixtures/SOURCES.md) the triples are exactly FIX_WANT (multiset), and on a
            copy of it written at run time under another name with two blank lines inserted after its
            title (beside a copy of its registry) the run exits 1 and the triples are the same rows
            under the copy's path at line + 2. FIX_WANT: S951 html-entity
            and truncated-grounds (an entity-encoded Grounds that is a proper prefix of its teaches
            cell once decoded), S952 html-entity only (an entity-encoded whole Grounds), S954
            html-entity (numeric references inside a quote), S955 html-entity and words=26 (a
            26-word quotation whose marks are numeric references &#8220; &#8221;), S958 html-entity
            (hexadecimal references), S959 html-entity (another HTML5 named reference, &rsquo;), S960
            html-entity and words=5 (an &hellip; that joins two fragments inside one span: the
            ellipsis-joined rule on the decoded row); S953 (`AT&T;`, `R&D;`, a URL `&b=2`), S961 (a URL
            `&region=eu&copy=2&reg`: names without `;` are no reference) and S956 (clean) are
            unreported
  KEEP      on corpus/lessons/round-49.md ... round-54.md each run's stdout and exit status equal
            the base tool's, as pinned in reports/round-56/base-gate-keep.txt
  BADUTF8   on reports/round-56/fixtures/lessons/bad-utf8.md (a Gate row with invalid UTF-8 bytes)
            the run exits 2, its stderr's first line starts `GATE_QUOTES_ERROR: ` and names the
            path, and its stderr carries no `Traceback`
  FORMAT    the round-55, fixture and six KEEP runs each write nothing to stderr, every stdout line
            is a finding line or the summary, and the summary's <n> equals the finding lines
  SELFTEST  `python3 -B tools/check-gate-quotes.py --selftest` exits 0
Exit 0 only when every leg passes; 1 when any leg fails; 2 on unreadable input, including a pinned
input whose sha256 differs from PINS. Every tool's exit status is read directly (no pipe, no
shell).
Review-only (no leg): whether the html-entity rule is documented in the tool's docstring with its
false-positive boundary (a reference counts only when it is numeric or an HTML5 named reference);
whether the selftest carries a red and a green case for the new class and for decoded comparison;
whether decoding before the quote and Grounds rules generalises beyond the routed lines.
"""
import argparse
import hashlib
import os
import re
import shutil
import subprocess
import sys
import tempfile
from collections import Counter

TOOL = "tools/check-gate-quotes.py"
R55 = "corpus/lessons/round-55.md"
FIX = "reports/round-56/fixtures/lessons/entities.md"
FIXREG = "reports/round-56/fixtures/SOURCES.md"
BAD = "reports/round-56/fixtures/lessons/bad-utf8.md"
KEEPFILE = "reports/round-56/base-gate-keep.txt"
PINS = {FIX: "803fff4e8c064d42ebdd3cc57b5e195047ca51176b1b57f798e88a09dfd1c876",
        FIXREG: "0a82a6ab4a62d9dce960f3e1a983ab62c3544d81088c0be396038aa148680f8a",
        BAD: "230dbacd02064acff38850020d6022ac6af89c0a2d4139cd3bf65228e3611a58",
        KEEPFILE: "fa289d07750e97f3cb9bbe4fa4b7ca87a9abfd54fc892d7dfa750abdd76290a7",
        R55: "1bbf70814548295c6e6bd2d916ea15a4b27d43a91a4af40e19062fee65fbc8ff"}
ENTITY_WANT = Counter((R55, n, s, "html-entity") for n, s in (
    (72, "S288"), (82, "S298"), (88, "S304"), (89, "S305"), (93, "S309"), (96, "S312"),
    (110, "S326"), (113, "S329"), (125, "S341"), (127, "S343"), (131, "S347"), (132, "S348"),
    (134, "S350"), (138, "S354"), (140, "S356"), (141, "S357")))
FIX_ROWS = [(8, "S951", "html-entity"), (8, "S951", "truncated-grounds"), (9, "S952", "html-entity"),
            (11, "S954", "html-entity"), (12, "S955", "html-entity"), (12, "S955", "words=26"),
            (14, "S958", "html-entity"), (15, "S959", "html-entity"), (16, "S960", "html-entity"),
            (16, "S960", "words=5")]
FIX_WANT = Counter((FIX,) + r for r in FIX_ROWS)
SHIFT = 2
FINDING = re.compile(r"^(\S+):(\d+) (S\d+) (\S+)$")
SUMMARY = re.compile(r"^GATE_QUOTES: (\d+) findings$")
KEEPHEAD = re.compile(r"^## (\S+) exit (\d+)$")


def run(root, argv):
    try:
        return subprocess.run([sys.executable, "-B"] + argv, cwd=root, capture_output=True, text=True,
                              errors="replace", timeout=300)
    except (OSError, subprocess.TimeoutExpired) as error:
        print(f"ACCEPT_O_INPUT_ERROR {' '.join(argv)} {error}", file=sys.stderr)
        return None


def triples(result):
    return Counter((m.group(1), int(m.group(2)), m.group(3), m.group(4))
                   for m in map(FINDING.match, result.stdout.splitlines()) if m)


def moved_copy(root, tmp):
    """The fixture under another name with SHIFT blank lines inserted after its title, beside a
    copy of its registry, so no output keyed on the fixture's path or line numbers can pass."""
    os.makedirs(os.path.join(tmp, "lessons"))
    shutil.copyfile(os.path.join(root, FIXREG), os.path.join(tmp, "SOURCES.md"))
    lines = open(os.path.join(root, FIX), encoding="utf-8").read().split("\n")
    path = os.path.join(tmp, "lessons", "moved-copy.md")
    open(path, "w", encoding="utf-8").write("\n".join(lines[:1] + [""] * SHIFT + lines[1:]))
    return path


def well_formed(result):
    lines = result.stdout.splitlines()
    found = [l for l in lines if FINDING.match(l)]
    other = [l for l in lines if not FINDING.match(l)]
    summary = SUMMARY.match(other[-1]) if len(other) == 1 else None
    return (not result.stderr and summary is not None and lines and lines[-1] == other[0]
            and int(summary.group(1)) == len(found))


def load_keep(path):
    keep, current = {}, None
    for line in open(path, encoding="utf-8"):
        line = line.rstrip("\n")
        head = KEEPHEAD.match(line)
        if head:
            current = head.group(1)
            keep[current] = [int(head.group(2)), []]
        elif current is not None:
            keep[current][1].append(line)
    return keep


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    root = os.path.abspath(ap.parse_args().root)
    try:
        for path, digest in PINS.items():
            seen = hashlib.sha256(open(os.path.join(root, path), "rb").read()).hexdigest()
            if seen != digest:
                print(f"ACCEPT_O_INPUT_ERROR {path} sha256 {seen} != pinned {digest}", file=sys.stderr)
                return 2
        keep = load_keep(os.path.join(root, KEEPFILE))
    except (OSError, UnicodeDecodeError) as error:
        print(f"ACCEPT_O_INPUT_ERROR {error}", file=sys.stderr)
        return 2
    if sorted(keep) != [f"corpus/lessons/round-{n}.md" for n in range(49, 55)]:
        print(f"ACCEPT_O_INPUT_ERROR {KEEPFILE} names {sorted(keep)}", file=sys.stderr)
        return 2
    tmp = tempfile.mkdtemp(prefix="kotodama-r56-accept-o-")
    try:
        moved = moved_copy(root, tmp)
        mov = run(root, [TOOL, moved])
    finally:
        shutil.rmtree(tmp)
    r55, fix, bad, st = (run(root, [TOOL, R55]), run(root, [TOOL, FIX]), run(root, [TOOL, BAD]),
                         run(root, [TOOL, "--selftest"]))
    keeps = {path: run(root, [TOOL, path]) for path in sorted(keep)}
    if None in (r55, fix, bad, st, mov) or None in keeps.values():
        return 2
    t55 = triples(r55)
    ent = Counter({t: n for t, n in t55.items() if t[3] == "html-entity"})
    stray = sorted(t for t in t55 if t[3] != "html-entity")
    tfix = triples(fix)
    tmov = triples(mov)
    mov_want = Counter((moved, n + SHIFT, s, d) for n, s, d in FIX_ROWS)
    keep_bad = [p for p, r in keeps.items()
                if r.returncode != keep[p][0] or r.stdout.splitlines() != keep[p][1]]
    first = (bad.stderr.splitlines() or [""])[0]
    bad_format = [name for name, r in [("round55", r55), ("fixture", fix)] + sorted(keeps.items())
                  if not well_formed(r)]
    legs = [
        ("ENTITY", ent == ENTITY_WANT,
         f"count={sum(ent.values())} missing={sorted((ENTITY_WANT - ent).elements())} "
         f"extra={sorted((ent - ENTITY_WANT).elements())}"),
        ("NOFALSE", not stray, f"stray={stray}"),
        ("EXIT", r55.returncode == 1 and fix.returncode == 1, f"round55={r55.returncode} fixture={fix.returncode}"),
        ("DECODE", tfix == FIX_WANT and tmov == mov_want and mov.returncode == 1,
         f"missing={sorted((FIX_WANT - tfix).elements())} extra={sorted((tfix - FIX_WANT).elements())} "
         f"moved_exit={mov.returncode} moved_missing={len(list((mov_want - tmov).elements()))} "
         f"moved_extra={len(list((tmov - mov_want).elements()))}"),
        ("KEEP", not keep_bad, f"changed={keep_bad}"),
        ("BADUTF8", bad.returncode == 2 and first.startswith("GATE_QUOTES_ERROR: ") and BAD in first
         and "Traceback" not in bad.stderr, f"exit={bad.returncode} stderr_first={first[:120]!r} "
         f"traceback={'Traceback' in bad.stderr}"),
        ("FORMAT", not bad_format, f"malformed_runs={bad_format}"),
        ("SELFTEST", st.returncode == 0, f"exit={st.returncode} {(st.stdout.strip().splitlines() or ['?'])[-1]}"),
    ]
    for name, ok, detail in legs:
        print(f"{name} {'PASS' if ok else 'FAIL'} {detail}")
    return 0 if all(ok for _, ok, _ in legs) else 1


if __name__ == "__main__":
    sys.exit(main())
