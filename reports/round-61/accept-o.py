#!/usr/bin/env python3
r"""Round-61 claim O acceptance: the clause-scoping lint tools/check-cited-lines.py (R60-M6 fix). Run
from the lane root:

  python3 -B reports/round-61/accept-o.py [--root DIR]

Tool contract (claims.json `O.contract`): `python3 -B tools/check-cited-lines.py PATH...` reads each
PATH (a file, or a directory walked recursively for files whose name ends in `.md`). An S-id is a
match of \bS\d{3,}\b. For each line of each file, in line order, it prints
  MULTI-ID <path>:<lineno> <ids>   when the line carries two or more distinct S-ids
  TABLE-ID <path>:<lineno> <ids>   when the line, leading whitespace removed, starts with `|` and
                                   carries at least one S-id
(<ids> the distinct ids sorted by number, comma-joined; a line may give both findings), then a last
line `CITED-LINES: <k> finding(s) in <m> file(s)`. Exit 1 when k > 0, 0 when k = 0, 2 (with a
`CITED_LINES_ERROR` line on stderr) when no PATH is given, a PATH does not exist, or a file is
unreadable or not valid UTF-8. `--selftest` runs its own cases and ends with `selftest N/N`.

Legs, each printed with PASS or FAIL:
  TOOL   tools/check-cited-lines.py exists; `--selftest` exits 0 and its last line is
         `selftest N/N` with N >= 10
  INDEP  the tool's source names neither `reports/` nor `accept-o` (it does not load this counter)
  GEN    on a fixture tree generated now in a fresh temporary directory from os.urandom (random ids,
         random filler words, random separators, random file and directory names; every run differs),
         the tool, given the tree's root directory, prints exactly the reference finding set (kind,
         path, line, ids), exits 1, and its summary counts the findings and the `.md` files
  CLEAN  on a generated file whose lines carry at most one distinct S-id and no table row, the tool
         prints no finding, exits 0 and summarises `0 finding(s) in 1 file(s)`
  ERR    a missing path and a file that is not valid UTF-8 each give exit 2 and a
         `CITED_LINES_ERROR` line on stderr
  REAL   on corpus/knowledge exported from the round base 942abdf4 by `git archive`, the tool prints
         exactly the reference finding set, which is not empty (the R60-M6 line of the amulets entry
         carrying S612 and S613 is in it)
Frozen predicate (the same sentence in reports/round-61/claims.json and in every receipt):
  ACCEPT-O-61: every leg above prints PASS.
Exit 0 only when every leg passes; 1 when any leg fails; 2 on an input error of this counter.
"""
import argparse
import os
import random
import re
import subprocess
import sys
import tempfile

TOOL = "tools/check-cited-lines.py"
BASE = "942abdf4f94f82a8372c5b550adb8241aa79c467"
SID = re.compile(r"\bS\d{3,}\b")
FINDING = re.compile(r"^(MULTI-ID|TABLE-ID) (.+):(\d+) (S\d{3,}(?:,S\d{3,})*)$")
SUMMARY = re.compile(r"^CITED-LINES: (\d+) finding\(s\) in (\d+) file\(s\)$")


def reference(root_arg, cwd):
    """The finding set and file count the contract requires for root_arg (a dir) under cwd."""
    found, files = set(), 0
    top = os.path.join(cwd, root_arg)
    for d, dirs, fs in os.walk(top):
        for f in fs:
            if not f.endswith(".md"):
                continue
            files += 1
            rel = os.path.normpath(os.path.join(root_arg, os.path.relpath(os.path.join(d, f), top)))
            with open(os.path.join(d, f), encoding="utf-8") as h:
                for n, line in enumerate(h.read().splitlines(), 1):
                    ids = sorted(set(SID.findall(line)), key=lambda s: int(s[1:]))
                    if len(ids) >= 2:
                        found.add(("MULTI-ID", rel, n, ",".join(ids)))
                    if ids and line.lstrip().startswith("|"):
                        found.add(("TABLE-ID", rel, n, ",".join(ids)))
    return found, files


def run_tool(root, args, cwd):
    try:
        return subprocess.run([sys.executable, "-B", os.path.join(root, TOOL)] + args, cwd=cwd,
                              capture_output=True, text=True, timeout=300)
    except (OSError, subprocess.TimeoutExpired) as error:
        return subprocess.CompletedProcess(args, 99, "", f"counter: {error}")


def parse(out):
    lines = out.stdout.splitlines()
    found, bad = set(), []
    for l in lines[:-1]:
        m = FINDING.match(l)
        if m:
            found.add((m.group(1), os.path.normpath(m.group(2)), int(m.group(3)), m.group(4)))
        else:
            bad.append(l)
    summary = SUMMARY.match(lines[-1]) if lines else None
    return found, bad, summary


def word(rng):
    return "".join(rng.choice("abcdefghijklmnoprstuvwyz") for _ in range(rng.randint(3, 9)))


def sid(rng):
    return f"S{rng.randint(100, 9999)}"


def gen_line(rng, kind):
    filler = " ".join(word(rng) for _ in range(rng.randint(2, 8)))
    if kind == "plain":
        return rng.choice(["", "# ", "- ", "  "]) + filler
    if kind == "single":
        return f"{rng.choice(['- ', '  - ', '', '## '])}{filler} ({sid(rng)}) {word(rng)}"
    if kind == "repeat":
        s = sid(rng)
        return f"- {filler} {s}; {word(rng)} [{s}] {word(rng)}"
    if kind == "lookalike":
        s = sid(rng)
        return f"- {filler} X{s} {s}x S{rng.randint(1, 99)} {s}_ {s.lower()}"
    if kind == "multi":
        ids = rng.sample(range(100, 9999), rng.randint(2, 4))
        sep = rng.choice([", ", "; ", " and ", "/", "–", "-", ")(", " "])
        return f"- {filler} (" + sep.join(f"S{i}" for i in ids) + f") {word(rng)}"
    if kind == "table1":
        return f"{rng.choice(['', '  '])}| {word(rng)} | {filler} {sid(rng)} | {word(rng)} |"
    if kind == "tablen":
        a, b = rng.sample(range(100, 9999), 2)
        return f"| S{a} | {filler} | S{b} |"
    if kind == "tableplain":
        return f"| {word(rng)} | {filler} |"
    raise ValueError(kind)


def write_tree(rng, top):
    kinds = ["plain", "single", "repeat", "lookalike", "multi", "table1", "tablen", "tableplain"]
    paths = []
    for i in range(4):
        sub = os.path.join(top, *[word(rng) for _ in range(rng.randint(0, 2))])
        os.makedirs(sub, exist_ok=True)
        paths.append(os.path.join(sub, f"{word(rng)}.md"))
    for p in paths:
        body = [gen_line(rng, k) for k in kinds * 3] + [gen_line(rng, rng.choice(kinds)) for _ in range(rng.randint(10, 30))]
        rng.shuffle(body)
        with open(p, "w", encoding="utf-8") as h:
            h.write("\n".join(body) + "\n")
    with open(os.path.join(top, f"{word(rng)}.txt"), "w", encoding="utf-8") as h:
        h.write(gen_line(rng, "multi") + "\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    root = os.path.abspath(ap.parse_args().root)
    rng = random.Random(os.urandom(16))
    legs = []
    tool_path = os.path.join(root, TOOL)
    exists = os.path.isfile(tool_path)
    st = run_tool(root, ["--selftest"], root) if exists else None
    last = (st.stdout.strip().splitlines() or [""])[-1] if st else ""
    m = re.match(r"^selftest (\d+)/(\d+)$", last)
    legs.append(("TOOL", bool(exists and st.returncode == 0 and m and m.group(1) == m.group(2)
                              and int(m.group(1)) >= 10),
                 f"exists={exists} exit={st.returncode if st else None} last={last!r}"))
    src = open(tool_path, encoding="utf-8", errors="replace").read() if exists else ""
    legs.append(("INDEP", exists and "reports/" not in src and "accept-o" not in src,
                 f"exists={exists}"))
    with tempfile.TemporaryDirectory() as tmp:
        fx = word(rng)
        write_tree(rng, os.path.join(tmp, fx))
        want, nfiles = reference(fx, tmp)
        out = run_tool(root, [fx], tmp)
        got, bad, summary = parse(out)
        ok = (exists and out.returncode == 1 and not bad and got == want and summary is not None
              and int(summary.group(1)) == len(want) and int(summary.group(2)) == nfiles)
        legs.append(("GEN", ok, f"exit={out.returncode} want={len(want)} got={len(got)} missing={len(want - got)} "
                     f"extra={len(got - want)} unparsed={len(bad)} files={nfiles} summary={summary.group(0) if summary else None}"))
        clean = os.path.join(tmp, f"{word(rng)}.md")
        with open(clean, "w", encoding="utf-8") as h:
            h.write("\n".join(gen_line(rng, rng.choice(["plain", "single", "repeat", "lookalike", "tableplain"]))
                              for _ in range(60)) + "\n")
        out = run_tool(root, [os.path.basename(clean)], tmp)
        got, bad, summary = parse(out)
        legs.append(("CLEAN", exists and out.returncode == 0 and not got and not bad and summary is not None
                     and summary.group(0) == "CITED-LINES: 0 finding(s) in 1 file(s)",
                     f"exit={out.returncode} findings={len(got)} summary={summary.group(0) if summary else None}"))
        badutf = os.path.join(tmp, f"{word(rng)}.md")
        with open(badutf, "wb") as h:
            h.write(b"- ok S123\n- \xff\xfe broken S456 S789\n")
        e1 = run_tool(root, [os.path.join(tmp, word(rng) + "-missing.md")], tmp)
        e2 = run_tool(root, [badutf], tmp)
        legs.append(("ERR", exists and all(e.returncode == 2 and "CITED_LINES_ERROR" in e.stderr for e in (e1, e2)),
                     f"missing_exit={e1.returncode} badutf8_exit={e2.returncode}"))
        real = os.path.join(tmp, "base")
        os.makedirs(real)
        arch = subprocess.run(f"git -C '{root}' archive {BASE} corpus/knowledge | tar -x -C '{real}'",
                              shell=True, capture_output=True, text=True)
        if arch.returncode != 0:
            print(f"ACCEPT_O_INPUT_ERROR git archive {arch.stderr.strip()}", file=sys.stderr)
            return 2
        want, nfiles = reference("corpus/knowledge", real)
        out = run_tool(root, ["corpus/knowledge"], real)
        got, bad, summary = parse(out)
        r60 = any(k == "MULTI-ID" and p.endswith("amulets-talismans-apotropaic-marks.md")
                  and "S612" in ids.split(",") and "S613" in ids.split(",") for k, p, _, ids in want)
        legs.append(("REAL", exists and bool(want) and r60 and got == want and not bad and out.returncode == 1,
                     f"exit={out.returncode} want={len(want)} got={len(got)} missing={sorted(want - got)[:3]} "
                     f"extra={sorted(got - want)[:3]} r60_line_in_reference={r60}"))
    for name, ok, detail in legs:
        print(f"{name} {'PASS' if ok else 'FAIL'} {detail}")
    verdict = all(ok for _, ok, _ in legs)
    print(f"ACCEPT-O-61: {'PASS' if verdict else 'FAIL'}")
    return 0 if verdict else 1


if __name__ == "__main__":
    sys.exit(main())
