#!/usr/bin/env python3
r"""Round-57 claim O acceptance (operability: the Gate checker's reference grammar and its selftest's
kill set). Run from the lane root:

  python3 -B reports/round-57/accept-o.py [--root DIR] [--tool PATH] [--seed N]

PATH defaults to tools/check-gate-quotes.py (relative to the root); the pre-dispatch control receipt
scores other checkers through --tool. The counting command runs WITHOUT --seed (seeds come from
os.urandom and appear in no path, argv or environment the checker sees); --seed exists only to replay
a printed run. Routed by the round-56 verifier spot-check
(corpus/lessons/round-56-verifier-spotcheck.md §5 items 1 and 2): the round-56 counter was met by a
checker that decodes nothing and only knows 23 S-ids, and three mutants survived. Revised before any
data after the pre-dispatch critic CriticClauseListO57 met the first draft with a seed-replay
checker, a `Seat: Gen.`-keyed checker and a function-identity selftest
(.ufo/waves/round-57/predispatch/CriticClauseListO57.md): random temporary directory names,
randomised constant text, filler words drawn from lesson prose, the REAL leg and the neutral patches.

Frozen predicate (the same sentence in reports/round-57/claims.json and in the receipts):
  ACCEPT-O-57: every leg below prints PASS on the checker under test.

Legs, each printed with PASS or FAIL:
  GEN       five lessons generated at run time (seeds printed after they are drawn; --seed N fixes the
            first and the others follow as N+1..N+4). Each lesson is written under a random temporary
            directory and draws, from its seed, fresh S-ids (S100-S999, distinct), a random file name,
            title, URL host, Seat label, accessed date, kind, tier and scope, a random number (1-6) of
            blank lines after its title, a random row order, and filler words drawn from the prose of
            lessons 49-56; it writes its own registry one directory up.
            Its rows come from twelve templates whose expected findings the generator computes
            itself (never by running a checker):
              clean                 plain quote                                   -> none
              named-1, named-2      a random HTML5 named reference ending in `;` whose value is
                                    one letter (571 of the table's names)         -> html-entity
              numeric-bare          a decimal reference to a letter WITHOUT `;`, followed by a space
                                    or a letter (`&#233 ` or `&#233w`)            -> html-entity
              hex-bare              a hexadecimal reference to a letter WITHOUT `;`, followed by a
                                    space or a letter outside a-f                 -> html-entity
              invalid-codepoint     `&#0;`, `&#xD800;` or `&#1114112;` (decodes to U+FFFD)
                                                                                  -> html-entity
              double-encoded        `&amp;hellip;`, `&amp;mldr;` or `&amp;#8230;` between two words:
                                    decoded once it is literal text, not an ellipsis -> html-entity
              truncated-encoded     Grounds `&quot;W w&quot; ...` that is a proper prefix of its
                                    teaches cell once decoded            -> html-entity, truncated-grounds
              overcap-numeric       26-30 words between `&#8220;` and `&#8221;`   -> html-entity, words=<n>
              bare-ampersand        `&XY;` with XY two random capitals that are no HTML5 name, a URL
                                    `?a=1&b=2`, `&#;`, `&#x;` and `&#xg`          -> none
              named-no-semicolon    `&copy` or `&reg` followed by a space (names bind only with `;`)
                                                                                  -> none
            PASS when, for all five lessons, the checker exits 1, its (line, S-id, detail) multiset
            equals the generator's and its stdout is well formed (see FORMAT).
  REAL      three copies of corpus/lessons/round-56.md (registry corpus/SOURCES.md copied beside
            each, under a random temporary directory and file name); in each, six random Gate rows
            that carry no `&` have one letter of their Grounds replaced by a numeric reference to
            that letter WITHOUT `;` (decimal, or hexadecimal when the next character is not a hex
            digit), so the decoded text is unchanged: the checker exits 1 and its multiset equals the
            pinned base findings of round-56.md plus one html-entity per injected row (real prose, so
            no generator text to key on)
  MULTI     for each GEN lesson, one run over [its invalid-UTF-8 sibling, the lesson] and one over
            the reverse order: each exits 2, its stderr's first line is `GATE_QUOTES_ERROR: <invalid
            path>: ...` with no Traceback, and its stdout carries exactly the findings of the
            checker's own single run on that lesson (at least one) and the summary line counting
            them (continuation past an unreadable file; the grammar itself is GEN's)
  MUTANTS   the checker's selftest, run in-process with the checker loaded as a module, exits
            non-zero under each of three run-time mutants patched into the loaded module (the file
            on disk is never changed): double-decode (decode_html_references applied twice),
            stop-at-first-bad-file (check stops after the first unreadable path), label-rename (run
            prints `html_entity` for `html-entity`); it exits 0 unmutated and exits 0 under each of
            three behaviour-preserving neutral patches of the same shape (neutral-decode,
            neutral-check, neutral-run), so a selftest that kills by detecting a patch rather than a
            behaviour fails. Patch helper names carry a random token per run. A patch that cannot be
            applied (the runner exits 97: a module that fails to load or lacks a name) fails the leg.
            The checker therefore keeps the module names decode_html_references(line), check(paths),
            run(paths) and selftest(), and its selftest reaches them through the module's globals
  KEEP      on corpus/lessons/round-49.md ... round-56.md each run's stdout and exit equal the base
            tool's, as pinned in reports/round-57/base-gate-keep.txt (base 86d08883)
  FORMAT    the KEEP runs write nothing to stderr, every stdout line is a finding line or the
            summary, and the summary's <n> equals the finding lines
  SELFTEST  the checker's `--selftest` exits 0 (unmutated)
Exit 0 only when every leg passes; 1 when any leg fails; 2 on unreadable input.
Every tool exit status is read directly (no pipe, no shell).
Review-only (no leg): whether the tool's docstring states the semicolon policy (numeric references
bind with or without `;`, named references only with `;`) and the U+FFFD handling of invalid code
points; whether the selftest's new cases are behavioural (a selftest that inspects its own file
is not a kill: the mutants never touch the file).
"""
import argparse
import hashlib
import html.entities
import os
import random
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata
from collections import Counter

DEFAULT_TOOL = "tools/check-gate-quotes.py"
KEEPFILE = "reports/round-57/base-gate-keep.txt"
PINS = {KEEPFILE: "817b000849fb7c8d7b16c836a8103ac3267ea22b07d76c4944a5b94dce7ad120"}
LESSONS = [f"corpus/lessons/round-{n}.md" for n in range(49, 57)]
FINDING = re.compile(r"^(\S+):(\d+) (S\d+) (\S+)$")
SUMMARY = re.compile(r"^GATE_QUOTES: (\d+) findings$")
KEEPHEAD = re.compile(r"^## (\S+) exit (\d+)$")
LETTER_NAMES = sorted(k for k, v in html.entities.html5.items()
                      if k.endswith(";") and len(v) == 1 and unicodedata.category(v).startswith("L"))
LETTER_CODES = [c for c in range(0xC0, 0x250) if unicodedata.category(chr(c)).startswith("L")]
REAL_HOST = "corpus/lessons/round-56.md"
GATE_ROW = re.compile(r"^- (S\d+) — ")
MUTANT_RUNNER = r'''
import importlib.util, sys
tool, kind, token = sys.argv[1], sys.argv[2], sys.argv[3]
spec = importlib.util.spec_from_file_location("gate_checker_under_test", tool)
module = importlib.util.module_from_spec(spec)
try:
    spec.loader.exec_module(module)
except BaseException as error:
    print("MUTANT_RUNNER_LOAD_ERROR", type(error).__name__, file=sys.stderr)
    sys.exit(97)
PATCHES = {
"double-decode": """
_orig_T = decode_html_references
def decode_html_references(line):
    once, found = _orig_T(line)
    twice, again = _orig_T(once)
    return twice, found or again
""",
"neutral-decode": """
_orig_T = decode_html_references
def decode_html_references(line):
    once, found = _orig_T(line)
    return once, found
""",
"stop-at-first-bad-file": """
_orig_T = check
def check(paths):
    results = []
    for path in paths:
        part = _orig_T([path])
        results.extend(part)
        if part and part[0][1] is None:
            break
    return results
""",
"neutral-check": """
_orig_T = check
def check(paths):
    results = []
    for path in paths:
        part = _orig_T([path])
        results.extend(part)
    return results
""",
"label-rename": """
import io as _io_T, re as _re_T, sys as _sys_T, contextlib as _contextlib_T
_orig_T = run
def run(paths):
    buffer = _io_T.StringIO()
    with _contextlib_T.redirect_stdout(buffer):
        code = _orig_T(paths)
    _sys_T.stdout.write(_re_T.sub(r" html-entity$", " html_entity", buffer.getvalue(), flags=_re_T.M))
    return code
""",
"neutral-run": """
import io as _io_T, re as _re_T, sys as _sys_T, contextlib as _contextlib_T
_orig_T = run
def run(paths):
    buffer = _io_T.StringIO()
    with _contextlib_T.redirect_stdout(buffer):
        code = _orig_T(paths)
    _sys_T.stdout.write(_re_T.sub(r" html-entity$", " html-entity", buffer.getvalue(), flags=_re_T.M))
    return code
""",
}
if kind != "none":
    try:
        source = PATCHES[kind].replace("_T", "_" + token)
        exec(compile(source, tool, "exec"), module.__dict__)
    except BaseException as error:
        print("MUTANT_RUNNER_PATCH_ERROR", kind, type(error).__name__, file=sys.stderr)
        sys.exit(97)
sys.exit(module.selftest())
'''


def run(root, argv, timeout=300):
    try:
        return subprocess.run([sys.executable, "-B"] + argv, cwd=root, capture_output=True, text=True,
                              errors="replace", timeout=timeout)
    except (OSError, subprocess.TimeoutExpired) as error:
        print(f"ACCEPT_O_INPUT_ERROR {' '.join(argv[:2])} {error}", file=sys.stderr)
        return None


def triples(stdout):
    return Counter((m.group(1), int(m.group(2)), m.group(3), m.group(4))
                   for m in map(FINDING.match, stdout.splitlines()) if m)


def well_formed(result, allow_stderr=False):
    lines = result.stdout.splitlines()
    found = [l for l in lines if FINDING.match(l)]
    other = [l for l in lines if not FINDING.match(l)]
    summary = SUMMARY.match(other[0]) if len(other) == 1 else None
    return ((allow_stderr or not result.stderr) and summary is not None and lines[-1] == other[0]
            and int(summary.group(1)) == len(found))


def vocabulary(root):
    """Lower-case alphabetic words of 3-12 letters from the prose of lessons 49-56 (filler for GEN)."""
    seen = set()
    for path in LESSONS:
        for word in re.findall(r"\b[a-z]{3,12}\b", open(os.path.join(root, path), encoding="utf-8").read()):
            seen.add(word)
    return sorted(w for w in seen if w not in ("amp", "quot", "copy", "reg", "hellip", "mldr"))


VOCAB = []


def words(rng, n):
    return " ".join(rng.choice(VOCAB) for _ in range(n))


def caps_not_named(rng):
    while True:
        name = rng.choice("BCHJKMNPRVWXZ") + rng.choice("BCHJKMNPRVWXZ")
        if name + ";" not in html.entities.html5 and name not in html.entities.html5:
            return name


def templates(rng):
    """(name, quote, grounds, teaches, expected details) per template; grounds == teaches unless named."""
    out = []

    def add(name, quote, expected, grounds=None, teaches=None):
        g = grounds or (words(rng, 1).capitalize() + " " + words(rng, rng.randint(3, 7)))
        out.append((name, quote, g, teaches or g, expected))

    add("clean", words(rng, rng.randint(3, 6)), [])
    for label in ("named-1", "named-2"):
        add(label, f"{words(rng, 2)} &{rng.choice(LETTER_NAMES)} {words(rng, 2)}", ["html-entity"])
    tail = rng.choice([" " + words(rng, 1), words(rng, 1)])
    add("numeric-bare", f"{words(rng, 2)} &#{rng.choice(LETTER_CODES)}{tail} {words(rng, 1)}", ["html-entity"])
    tail = rng.choice([" " + words(rng, 1), rng.choice("ghkmnprstvz") + words(rng, 1)])
    add("hex-bare", f"{words(rng, 2)} &#x{rng.choice(LETTER_CODES):X}{tail} {words(rng, 1)}", ["html-entity"])
    add("invalid-codepoint", f"{words(rng, 2)} {rng.choice(['&#0;', '&#xD800;', '&#1114112;'])} {words(rng, 1)}",
        ["html-entity"])
    add("double-encoded", f"{words(rng, 1)} {rng.choice(['&amp;hellip;', '&amp;mldr;', '&amp;#8230;'])} {words(rng, 1)}",
        ["html-entity"])
    head = words(rng, 2)
    rest = words(rng, rng.randint(2, 4))
    add("truncated-encoded", words(rng, 3), ["html-entity", "truncated-grounds"],
        grounds=f"&quot;{head}&quot; {rest}",
        teaches=f"\"{head}\" {rest}, {words(rng, rng.randint(2, 5))}")
    n = rng.randint(26, 30)
    out.append(("overcap-numeric", None, None, None, ["html-entity", f"words={n}"], n))
    add("bare-ampersand", f"{words(rng, 1)} &{caps_not_named(rng)}; {words(rng, 1)} &#; &#x; &#xg {words(rng, 1)}", [])
    add("named-no-semicolon", f"{words(rng, 1)} &{rng.choice(['copy', 'reg'])} {words(rng, 1)}", [])
    return out


def generate(directory, seed):
    """Write a lesson and its registry under directory; return (lesson path, expected Counter, bad path)."""
    rng = random.Random(seed)
    host = f"https://{words(rng, 1)}.{rng.choice(['org', 'net', 'edu', 'info', 'example'])}"
    seat = words(rng, 1).capitalize() + words(rng, 1).capitalize()
    date = f"2026-{rng.randint(1, 12):02d}-{rng.randint(1, 28):02d}"
    kind = rng.choice(["paper", "book", "web", "record", "docs"])
    ids = rng.sample(range(100, 1000), 13)
    rows, registry, expected = [], [], []
    for (index, item) in enumerate(templates(rng)):
        sid = f"S{ids[index]}"
        if item[0] == "overcap-numeric":
            n = item[5]
            grounds = words(rng, 1).capitalize() + " " + words(rng, rng.randint(3, 7))
            quote_part = f"&#8220;{words(rng, n)}&#8221;"
            details, teaches = item[4], grounds
        else:
            name, quote, grounds, teaches, details = item
            quote_part = f'"{quote}"'
        url = f"{host}/{words(rng, 1)}/{rng.randint(1000, 99999)}"
        if item[0] == "bare-ampersand":
            url += f"?{words(rng, 1)}=1&{words(rng, 1)}=2"
        rows.append((sid, f"- {sid} — {url} — accessed {date} — p. {rng.randint(1, 400)}: {quote_part}. "
                          f"Grounds: {grounds}. Seat: {seat}.", details))
        registry.append(f"| {sid} | {words(rng, 2).title()} — {url} | {kind} | {rng.choice('AB')} | "
                        f"{words(rng, 3)} | p. {rng.randint(1, 400)} | {teaches} | mined | "
                        f"{date} | 2027-{date[5:]} | — |")
    rng.shuffle(rows)
    os.makedirs(os.path.join(directory, "lessons"))
    with open(os.path.join(directory, "SOURCES.md"), "w", encoding="utf-8") as handle:
        handle.write(f"# {words(rng, 2).title()}\n\n| id | source | kind | tier | scope | anchor | teaches | status | "
                     "opened | recheck | used-by |\n|---|---|---|---|---|---|---|---|---|---|---|\n")
        handle.write("\n".join(registry) + "\n")
    name = f"{words(rng, 1)}-{rng.randint(10, 99)}.md"
    path = os.path.join(directory, "lessons", name)
    head = ["# " + words(rng, rng.randint(2, 6)).capitalize()] + [""] * rng.randint(1, 6) + ["## Gate", ""]
    body = [r[1] for r in rows]
    with open(path, "w", encoding="utf-8") as handle:
        handle.write("\n".join(head + body + ["", "## Status", "", "End."]) + "\n")
    first = len(head) + 1
    for offset, (sid, _, details) in enumerate(rows):
        for detail in details:
            expected.append((path, first + offset, sid, detail))
    bad = os.path.join(directory, "lessons", f"bad-{rng.randint(10, 99)}.md")
    with open(bad, "wb") as handle:
        handle.write(f"## Gate\n\n- S{ids[12]} — p. 1: \"".encode() + b"\xff\xfe" + b"\".\n")
    return path, Counter(expected), bad


def inject_real(root, directory, seed, base_lines):
    """A copy of REAL_HOST (with the lane registry beside it) in which six random Gate rows that carry
    no `&` get one letter of their Grounds replaced by a numeric reference without `;` (decimal, or
    hexadecimal when the next character is not a hex digit); the decoded text is unchanged, so the
    expected findings are the base findings of REAL_HOST plus one html-entity per injected row."""
    rng = random.Random(seed)
    os.makedirs(os.path.join(directory, "lessons"))
    shutil.copyfile(os.path.join(root, "corpus/SOURCES.md"), os.path.join(directory, "SOURCES.md"))
    lines = open(os.path.join(root, REAL_HOST), encoding="utf-8").read().split("\n")
    start = lines.index("## Gate")
    end = next(i for i in range(start + 1, len(lines)) if lines[i].startswith("## "))
    candidates = [i for i in range(start, end)
                  if GATE_ROW.match(lines[i]) and "Grounds: " in lines[i] and "&" not in lines[i]]
    path = os.path.join(directory, "lessons", f"{rng.choice(VOCAB)}-{rng.randint(10, 99)}.md")
    expected = []
    for i in rng.sample(candidates, 6):
        line = lines[i]
        g = line.index("Grounds: ") + len("Grounds: ")
        stop = line.find(". Seat:", g)
        stop = stop if stop > 0 else len(line)
        hexmode = rng.random() < 0.5
        spots = [g + m.start() + k for m in re.finditer(r"[A-Za-z]{3,}", line[g:stop])
                 for k in range(m.end() - m.start() - 1)]
        if hexmode:
            spots = [p for p in spots if line[p + 1] not in "0123456789abcdefABCDEF"]
        p = rng.choice(spots)
        ref = f"&#x{ord(line[p]):X}" if hexmode else f"&#{ord(line[p])}"
        lines[i] = line[:p] + ref + line[p + 1:]
        expected.append((path, i + 1, GATE_ROW.match(line).group(1), "html-entity"))
    for (_, n, s, d), count in triples("\n".join(base_lines)).items():
        expected += [(path, n, s, d)] * count
    with open(path, "w", encoding="utf-8") as handle:
        handle.write("\n".join(lines))
    return path, Counter(expected)


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
    ap.add_argument("--tool", default=DEFAULT_TOOL)
    ap.add_argument("--seed", type=int)
    args = ap.parse_args()
    root = os.path.abspath(args.root)
    tool = os.path.abspath(os.path.join(root, args.tool))
    try:
        for path, digest in PINS.items():
            seen = hashlib.sha256(open(os.path.join(root, path), "rb").read()).hexdigest()
            if seen != digest:
                print(f"ACCEPT_O_INPUT_ERROR {path} sha256 {seen} != pinned {digest}", file=sys.stderr)
                return 2
        keep = load_keep(os.path.join(root, KEEPFILE))
        open(tool, "rb").close()
    except (OSError, UnicodeDecodeError) as error:
        print(f"ACCEPT_O_INPUT_ERROR {error}", file=sys.stderr)
        return 2
    if sorted(keep) != sorted(LESSONS):
        print(f"ACCEPT_O_INPUT_ERROR {KEEPFILE} names {sorted(keep)}", file=sys.stderr)
        return 2
    VOCAB.extend(vocabulary(root))
    first = args.seed if args.seed is not None else int.from_bytes(os.urandom(4), "big")
    seeds = [first + i for i in range(5)]
    real_seeds = [first + 100 + i for i in range(3)]
    print(f"# tool {os.path.relpath(tool, root)} sha256 {hashlib.sha256(open(tool, 'rb').read()).hexdigest()}")
    print(f"# seeds {seeds} real-seeds {real_seeds}")
    tmp = tempfile.mkdtemp(prefix="gq-")
    gen_bad, multi_bad, real_bad = [], [], []
    try:
        for seed in real_seeds:
            lesson, want = inject_real(root, tempfile.mkdtemp(dir=tmp), seed, keep[REAL_HOST][1])
            result = run(root, [tool, lesson])
            if result is None:
                return 2
            got = triples(result.stdout)
            if not (result.returncode == 1 and got == want and well_formed(result)):
                real_bad.append(f"seed={seed} exit={result.returncode} missing={sorted((want - got).elements())} "
                                f"extra={sorted((got - want).elements())}")
        for seed in seeds:
            directory = tempfile.mkdtemp(dir=tmp)
            lesson, want, bad = generate(directory, seed)
            result = run(root, [tool, lesson])
            if result is None:
                return 2
            got = triples(result.stdout)
            if not (result.returncode == 1 and got == want and well_formed(result)):
                gen_bad.append(f"seed={seed} exit={result.returncode} missing={sorted((want - got).elements())} "
                               f"extra={sorted((got - want).elements())}")
            for order in ([bad, lesson], [lesson, bad]):
                multi = run(root, [tool] + order)
                if multi is None:
                    return 2
                first_err = (multi.stderr.splitlines() or [""])[0]
                if not (multi.returncode == 2 and first_err.startswith(f"GATE_QUOTES_ERROR: {bad}:")
                        and "Traceback" not in multi.stderr and got and triples(multi.stdout) == got
                        and well_formed(multi, allow_stderr=True)):
                    multi_bad.append(f"seed={seed} order={'bad-first' if order[0] == bad else 'bad-last'} "
                                     f"exit={multi.returncode} stderr_first={first_err[:100]!r}")
    finally:
        shutil.rmtree(tmp)
    mutants = {}
    for kind in ("none", "double-decode", "stop-at-first-bad-file", "label-rename",
                 "neutral-decode", "neutral-check", "neutral-run"):
        result = run(root, ["-c", MUTANT_RUNNER, tool, kind, "h" + os.urandom(5).hex()])
        if result is None:
            return 2
        mutants[kind] = result.returncode
    killing = ("double-decode", "stop-at-first-bad-file", "label-rename")
    survivors = [k for k in killing if mutants[k] == 0]
    neutral_fail = [k for k in mutants if k.startswith("neutral") and mutants[k] != 0]
    unpatched = [k for k, code in mutants.items() if code == 97]
    keeps = {path: run(root, [tool, path]) for path in LESSONS}
    if None in keeps.values():
        return 2
    keep_bad = [p for p, r in keeps.items()
                if r.returncode != keep[p][0] or r.stdout.splitlines() != keep[p][1]]
    bad_format = [p for p, r in keeps.items() if not well_formed(r)]
    st = run(root, [tool, "--selftest"])
    if st is None:
        return 2
    legs = [
        ("GEN", not gen_bad, f"lessons=5 failing={len(gen_bad)} {gen_bad[:2]}"),
        ("REAL", not real_bad, f"lessons=3 failing={len(real_bad)} {real_bad[:2]}"),
        ("MULTI", not multi_bad, f"runs=10 failing={multi_bad[:2]}"),
        ("MUTANTS", not survivors and not unpatched and not neutral_fail and mutants["none"] == 0,
         f"unmutated_selftest_exit={mutants['none']} survivors={survivors} neutral_failing={neutral_fail} "
         f"unpatched={unpatched} exits={mutants}"),
        ("KEEP", not keep_bad, f"changed={keep_bad}"),
        ("FORMAT", not bad_format, f"malformed_runs={bad_format}"),
        ("SELFTEST", st.returncode == 0, f"exit={st.returncode} {(st.stdout.strip().splitlines() or ['?'])[-1]}"),
    ]
    for name, ok, detail in legs:
        print(f"{name} {'PASS' if ok else 'FAIL'} {detail}")
    verdict = all(ok for _, ok, _ in legs)
    print(f"ACCEPT-O-57: {'PASS' if verdict else 'FAIL'}")
    return 0 if verdict else 1


if __name__ == "__main__":
    sys.exit(main())
