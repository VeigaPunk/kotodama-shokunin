#!/usr/bin/env python3
"""CriticClaims-22 falsification battery for the frozen round-83 counters.

Builds a throwaway --shared fixture clone of the lane, commits the cheapest
stub landings that try to pass claims O and D, grades them with the frozen
counters (run from the freeze bytes staged beside this script), and runs the
refusal battery against the real lane root. Read-only w.r.t. the lane.
"""
import os
import shutil
import subprocess
import sys

LANE = "/home/vgpnk/Projects/shokunin/kotodama-shokunin"
BASE = "3088bd7fe2a55a123214abba7008dcddf12b301c"
FREEZE = "21277b089e3c64c247bb4e0fcb033abfdfa1e668"
STAGE = os.path.dirname(os.path.abspath(__file__))
SCRATCH = "/fast/scratch/hyaku/kotodama-r83/CriticClaims-22"
ENTRY = "corpus/knowledge/myth-symbol/marriage-alliance-bridewealth.md"

MISSING11 = [
    "reports/round-76/accept-c.py",
    "reports/round-76/accept-ca.py",
    "reports/round-79/accept-ca.py",
    "reports/round-79/accept-o.py",
    "reports/round-80/accept-d.py",
    "reports/round-80/accept-o.py",
    "reports/round-81/accept-c81.py",
    "reports/round-81/accept-d81.py",
    "reports/round-81/accept-o81.py",
    "reports/round-82/accept-d82.py",
    "reports/round-82/accept-o82.py",
]
NEW83 = [
    "reports/round-83/accept-o83.py",
    "reports/round-83/accept-d83.py",
    "reports/round-83/accept-c83.py",
]


def git(dest, *a, check=True):
    r = subprocess.run(["git", "-C", dest] + list(a), capture_output=True)
    if check and r.returncode != 0:
        raise RuntimeError("git %s: %s" % (a[0], r.stderr.decode("utf-8", "replace")[:300]))
    return r


def out(dest, *a):
    return git(dest, *a).stdout.decode("utf-8", "replace")


def commit(dest, relpath, content, msg):
    p = os.path.join(dest, relpath)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    mode = "wb" if isinstance(content, bytes) else "w"
    with open(p, mode) as f:
        f.write(content)
    git(dest, "add", "--", relpath)
    git(dest, "commit", "-q", "-m", msg)
    return out(dest, "rev-parse", "HEAD").strip()


STUB_TOOL = r'''#!/usr/bin/env python3
r"""Minimal gate-registry coverage stub -- CriticClaims-22 falsification control.

This file exists ONLY inside a throwaway fixture clone. It is the cheapest
artifact that carries every frozen shape marker of claim O (GATE-REGISTRY:,
--json, def main(), 4000 bytes) while doing none of the curation work. Its
--selftest executes zero checks and prints the pass line anyway, which is the
point: the frozen counter cannot tell a self-asserted check count from a real
one. Its dead-instrument semantics are deliberately lenient (only instrument
tokens are resolved) to show that the counter must rely on its own parse.
"""
import argparse
import json
import os
import re
import sys

SUMMARY = "GATE-REGISTRY: %d missing / %d registered / %d instruments / %d dead"
TOKEN = re.compile(r"((?:tools|reports)/[A-Za-z0-9_./-]+\.py)")
INSTR = re.compile(r"^reports/[^/]+/accept-[^/]+\.py$")


def instruments(root):
    """Every reports/round-*/accept-*.py under --root, sorted."""
    found = []
    for dirpath, _dirs, files in os.walk(os.path.join(root, "reports")):
        for name in files:
            rel = os.path.relpath(os.path.join(dirpath, name), root)
            if INSTR.match(rel):
                found.append(rel)
    return sorted(found)


def rows(root):
    """Cells of the ## Gates and probes table (header included)."""
    with open(os.path.join(root, "SKILL.md"), encoding="utf-8") as handle:
        lines = handle.read().splitlines()
    try:
        start = next(i for i, l in enumerate(lines) if l.strip() == "## Gates and probes")
    except StopIteration:
        return []
    kept = []
    for i in range(start + 1, len(lines)):
        stripped = lines[i].lstrip()
        if stripped.startswith("## ") and i > start + 1:
            break
        if not stripped.startswith("|"):
            continue
        cells = [c.strip() for c in stripped.strip().strip("|").split("|")]
        if len(cells) < 2 or set("".join(cells)) <= set("-: "):
            continue
        kept.append(cells)
    return kept


def audit(root):
    inst = instruments(root)
    table = rows(root)
    missing = [p for p in inst if not any(p in c[2] for c in table if len(c) > 2)]
    dead = []
    for cells in table:
        if len(cells) < 3:
            continue
        for tok in TOKEN.findall(cells[2]):
            if INSTR.match(tok) and not os.path.isfile(os.path.join(root, tok)):
                dead.append(tok)
    registered = len(table) - 1
    return missing, registered, inst, sorted(set(dead))


def selftest():
    # CONTROL: no check runs; the count is a bare claim. The frozen counter
    # grades only rc and the printed number, so 12 >= 12 passes vacuously.
    print("SELFTEST: PASS (12 checks)")
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.selftest:
        return selftest()
    missing, registered, inst, dead = audit(args.root)
    if args.json:
        print(json.dumps({"missing": missing, "registered": registered,
                          "instruments": inst, "dead": dead}))
        return 0
    print(SUMMARY % (len(missing), registered, len(inst), len(dead)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
'''


def build_skill_rows():
    rows = []
    for p in MISSING11 + NEW83:
        name = p.rsplit("/", 1)[1][:-3]
        rows.append("| %s | counter | python3 %s |" % (name, p))
    return rows


def patch_skill(skill_text):
    lines = skill_text.splitlines(keepends=True)
    start = next(i for i, l in enumerate(lines) if l.strip() == "## Gates and probes")
    end = len(lines)
    for i in range(start + 1, len(lines)):
        if lines[i].startswith("## "):
            end = i
            break
    block = "".join(r + "\n" for r in build_skill_rows())
    return "".join(lines[:end]) + block + "".join(lines[end:])


def build_entry():
    head = "\n".join([
        "- topic: marriage as an alliance-and-transfer institution (STUB CONTROL)",
        "- gap filled: none -- this is a padded shape stub, not scholarship",
        "- sources: S909; S910; S911; S912",
        "- couples: stub",
        "- source: none",
        "- verified-at: 2026-11-04",
        "- recheck: 2027-05-04",
        "- scope: falsification control only",
        "",
        "Prose padding paragraph. The institution is described in generic terms;",
        "no claim here is evidence-bearing. Repeated below to cross the byte floor.",
    ])
    dec = "\n".join([
        "## 2. Six design decisions",
        "",
        "| D1 | payment direction | bridewealth moves value to the bride's group |",
        "| D2 | prohibited degrees | cousin marriage allowed or barred by rule |",
        "| D3 | rite sequence | betrothal, transfer, residence, consummation |",
        "| D4 | name and dress | the taker or giver of a new name and dress |",
        "| D5 | dissolution | who may end the bond and at what cost |",
        "| D6 | lexicon | the words the institution forces into the language |",
        "",
    ])
    anchors = ["## 3. Attested anchors", ""]
    ids = ["S909", "S910", "S911", "S912"]
    for i in range(22):
        anchors.append("- %s stub anchor %02d: a padded bullet with exactly one registry id." % (ids[i % 4], i))
    others = "\n".join([
        "## 1. The question", "", "stub prose", "",
        dec,
        "\n".join(anchors), "",
        "## 4. Lexicon", "", "stub prose", "",
        "## 5. Dissolution", "", "stub prose", "",
        "## 6. Open problems", "", "stub prose", "",
        "## 7. Receipts", "", "stub prose", "",
    ])
    body = head + "\n\n" + others
    # pad to >= 12000 bytes with id-free prose
    filler = ("\nFiller sentence for the control body; it asserts nothing and cites nothing.\n" * 60)
    return body + filler


def sourcerow(rid):
    return ("| %s | https://example.org/r83-stub-%s | secondary | T2 | stub control row; "
            "no real source | ch. I | stub: control row, not scholarship | mined | 2026-11-04 | "
            "2027-05-04 | %s |" % (rid, rid.lower(), ENTRY))


def append_sources(dest):
    p = os.path.join(dest, "corpus/SOURCES.md")
    with open(p, encoding="utf-8") as f:
        text = f.read()
    if not text.endswith("\n"):
        text += "\n"
    text += "".join(sourcerow(r) + "\n" for r in ("S909", "S910", "S911", "S912"))
    with open(p, "w", encoding="utf-8") as f:
        f.write(text)


def grade(counter, dest, rev, work):
    git(dest, "update-ref", "refs/heads/main", rev)
    os.makedirs(work, exist_ok=True)
    r = subprocess.run(
        [sys.executable, "-B", os.path.join(STAGE, counter),
         "--root", dest, "--lands", rev, "--freeze", FREEZE, "--work", work],
        capture_output=True, text=True)
    return r.returncode, (r.stdout + r.stderr).strip()


def main():
    if os.path.exists(SCRATCH):
        shutil.rmtree(SCRATCH)
    os.makedirs(SCRATCH)
    D = os.path.join(SCRATCH, "fixture")
    subprocess.run(["git", "clone", "--shared", "--no-hardlinks", "-q", LANE, D], check=True)
    git(D, "config", "user.email", "fixture@round83.invalid")
    git(D, "config", "user.name", "round83-fixture")
    git(D, "checkout", "-q", FREEZE)
    top = out(D, "rev-parse", "--show-toplevel").strip()
    assert top == D, "toplevel mismatch: %r != %r" % (top, D)
    print("FIXTURE-OK toplevel==%s at freeze" % top)
    print()

    # --- claim O stub landing (tool + 14 SKILL.md rows, nothing else)
    skill_path = os.path.join(D, "SKILL.md")
    with open(skill_path, encoding="utf-8") as f:
        skill = f.read()
    with open(skill_path, "w", encoding="utf-8") as f:
        f.write(patch_skill(skill))
    commit(D, "tools/check-gate-registry.py", STUB_TOOL, "control: stub gate-registry tool")
    O1 = commit(D, "SKILL.md", patch_skill(skill), "control: 14 minimal registry rows")
    print("O-STUB lands:", O1)
    rc, txt = grade("accept-o83.py", D, O1, os.path.join(SCRATCH, "work-o"))
    print("exit", rc)
    print(txt)
    print()

    # --- claim D stub landing (entry + 4 SOURCES rows, nothing else)
    git(D, "checkout", "-q", "-B", "dstub", FREEZE)
    D1 = commit(D, ENTRY, build_entry(), "control: padded knowledge stub")
    append_sources(D)
    D1 = commit(D, "corpus/SOURCES.md",
                open(os.path.join(D, "corpus/SOURCES.md"), encoding="utf-8").read(),
                "control: four stub registry rows")
    print("D-STUB lands:", D1)
    rc, txt = grade("accept-d83.py", D, D1, os.path.join(SCRATCH, "work-d"))
    print("exit", rc)
    print(txt)
    print()

    # --- combined stub (O files + D files in one landing): separability check
    git(D, "checkout", "-q", "-B", "both", O1)
    C1 = commit(D, ENTRY, build_entry(), "control: combined stub, entry")
    append_sources(D)
    C1 = commit(D, "corpus/SOURCES.md",
                open(os.path.join(D, "corpus/SOURCES.md"), encoding="utf-8").read(),
                "control: combined stub, sources")
    print("COMBINED lands:", C1)
    for counter in ("accept-o83.py", "accept-d83.py"):
        rc, txt = grade(counter, D, C1, os.path.join(SCRATCH, "work-" + counter[7:9]))
        print("-- %s exit %d" % (counter, rc))
        for line in txt.splitlines():
            if line.startswith(("LEG SEPARABLE", "ACCEPT-")):
                print("   " + line)
    print()

    # --- refusal battery against the REAL lane root (read-only git only)
    CTL = os.path.join(SCRATCH, "ctl")
    os.makedirs(CTL, exist_ok=True)
    for counter in ("accept-o83.py", "accept-d83.py", "accept-c83.py"):
        for label, lands in (("do-nothing(base)", BASE), ("non-40hex", "not-a-revision"),
                             ("lands==freeze", FREEZE)):
            r = subprocess.run(
                [sys.executable, "-B", os.path.join(STAGE, counter),
                 "--root", LANE, "--lands", lands, "--freeze", FREEZE, "--work", CTL],
                capture_output=True, text=True)
            first = [l for l in (r.stdout + r.stderr).splitlines() if l.strip()]
            print("REFUSE %-14s %-9s exit=%d :: %s" % (counter[7:-3], label, r.returncode,
                                                       first[0] if first else "<silent>"))
        r = subprocess.run(
            [sys.executable, "-B", os.path.join(STAGE, counter),
             "--root", LANE, "--lands", BASE, "--freeze", FREEZE,
             "--work", os.path.join(SCRATCH, "no-such-work")],
            capture_output=True, text=True)
        first = [l for l in (r.stdout + r.stderr).splitlines() if l.strip()]
        print("REFUSE %-14s %-9s exit=%d :: %s" % (counter[7:-3], "bad --work", r.returncode,
                                                   first[0] if first else "<silent>"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
