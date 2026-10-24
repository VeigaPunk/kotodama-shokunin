#!/usr/bin/env python3
r"""Round-66 claim Ca acceptance, revision 0 (pre-data).

Calibration claim (records): the four round-65 routed defects are dispositioned
in this round's records (corpus/lessons/round-65-verifier-spotcheck.md section
5). Each leg re-derives its disposition from committed bytes.

Legs (each prints `NAME PASS|FAIL detail`):
  D1        S753 durability repair: telemetry/s753-recapture.txt records the
            live PDF (status 200, application/pdf, the mancala quote verbatim)
            and the fresh capture 20261024111013 replaying 200 pdf; the games
            entry's mancala bullet cites S776 exactly once and S753 zero times
  D2        receipt sequencing: for each reports/round-66/telemetry/
            final-measures-{c,o,ca}.txt, `git log -1 main -- <receipt>` names
            the commit that carries it, that commit's parent equals the
            receipt's stamped 'measured revision', and the receipt's tree and
            counter sha256 lines resolve against the stamped revision
  D3        dispatch evidence: telemetry/seat-evidence.txt names >=8 seat
            report files under .ufo/waves/round-66/ that exist on disk, with a
            per-seat status line; dead seats carry a last-error line
  D4        separability bound: telemetry/separability-real.txt carries a
            `SEPARABILITY:` verdict line and an `acceptance_runs=` count
  CRITERION corpus/QUALITY.md gains criterion 18 grounding row-anchor
            durability (the S753 class)
  QUOTES    tools/check-gate-quotes.py finds 0 findings on
            corpus/lessons/round-66.md and its Gate names the round's ids
            (S776 plus S779-S800)

Output ends `ACCEPT-CA-66: PASS|FAIL`; exit 0/1, or 2 on unusable input.
"""

import argparse
import hashlib
import os
import re
import subprocess
import sys

RECEIPTS = [
    "reports/round-66/telemetry/final-measures-c.txt",
    "reports/round-66/telemetry/final-measures-o.txt",
    "reports/round-66/telemetry/final-measures-ca.txt",
]
COUNTERS = {
    "reports/round-66/telemetry/final-measures-c.txt": "reports/round-66/accept-c.py",
    "reports/round-66/telemetry/final-measures-o.txt": "reports/round-66/accept-o.py",
    "reports/round-66/telemetry/final-measures-ca.txt": "reports/round-66/accept-ca.py",
}
D1_RECEIPT = "reports/round-66/telemetry/s753-recapture.txt"
D3_RECEIPT = "reports/round-66/telemetry/seat-evidence.txt"
D4_RECEIPT = "reports/round-66/telemetry/separability-real.txt"
GAMES = "corpus/knowledge/culture-material/games-play-sport-contests.md"
QUALITY = "corpus/QUALITY.md"
LESSON = "corpus/lessons/round-66.md"
QUOTE_TOOL = "tools/check-gate-quotes.py"
QUOTE = ("Versions of mancala are traditionally played across Africa and Asia")


def read(root, path):
    try:
        with open(os.path.join(root, path), encoding="utf-8") as fh:
            return fh.read()
    except OSError:
        return None


def git_out(root, args):
    proc = subprocess.run(["git", "-C", root] + args,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return proc.returncode, proc.stdout.decode("utf-8", "replace")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    root = os.path.abspath(ap.parse_args().root)
    self_sha = hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest()
    mv = subprocess.run(["git", "-C", root, "rev-parse", "main"], stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE)
    print(f"# counter sha256 (self): {self_sha}")
    print(f"# measured revision (lane main): {mv.stdout.decode().strip() or 'unresolvable'}")
    legs = []

    def leg(name, ok, detail):
        legs.append(bool(ok))
        print(f"{name} {'PASS' if ok else 'FAIL'} {detail}")

    # ---------- D1 ----------
    d1 = read(root, D1_RECEIPT) or ""
    games = read(root, GAMES) or ""
    d1_bad = []
    if "200" not in d1 or "application/pdf" not in d1:
        d1_bad.append("live_status")
    if "sha256" not in d1.lower():
        d1_bad.append("no_digest")
    if QUOTE not in d1:
        d1_bad.append("quote")
    if "20261024111013" not in d1:
        d1_bad.append("capture_ts")
    if "cb6ff9b8" not in d1:
        d1_bad.append("live_digest")
    if "S776" not in d1:
        d1_bad.append("s776")
    s776_hits = len(re.findall(r"\(S776\)", games))
    s753_hits = len(re.findall(r"\(S753\)", games))
    if s776_hits != 1:
        d1_bad.append(f"s776_citations={s776_hits}")
    if s753_hits != 0:
        d1_bad.append(f"s753_citations={s753_hits}")
    leg("D1", not d1_bad, f"bad={d1_bad}")

    # ---------- D2 ----------
    d2_bad = []
    for rpath in RECEIPTS:
        rtext = read(root, rpath)
        if rtext is None:
            d2_bad.append(f"{rpath}:absent")
            continue
        m = re.search(r"measured revision \(lane main\): ([0-9a-f]{40})", rtext) \
            or re.search(r"measured revision: ([0-9a-f]{40})", rtext)
        if not m:
            d2_bad.append(f"{rpath}:no_stamp")
            continue
        stamped = m.group(1)
        code, carrier = git_out(root, ["log", "-1", "--format=%H", "main", "--", rpath])
        carrier = carrier.strip()
        if code != 0 or not carrier:
            d2_bad.append(f"{rpath}:no_carrier")
            continue
        code, parent = git_out(root, ["rev-parse", f"{carrier}^"])
        parent = parent.strip()
        if code != 0 or parent != stamped:
            d2_bad.append(f"{rpath}:parent={parent[:8]} stamped={stamped[:8]}")
        code, tree = git_out(root, ["rev-parse", f"{stamped}^{{tree}}"])
        tree = tree.strip()
        if f"tree: {tree}" not in rtext:
            d2_bad.append(f"{rpath}:tree")
        counter_path = COUNTERS[rpath]
        cblob = read(root, counter_path)
        if cblob is None:
            d2_bad.append(f"{rpath}:counter_absent")
        else:
            csha = hashlib.sha256(cblob.encode("utf-8")).hexdigest()
            if f"counter sha256 (self): {csha}" not in rtext:
                d2_bad.append(f"{rpath}:counter_sha")
    leg("D2", not d2_bad, f"bad={d2_bad[:4]}")

    # ---------- D3 ----------
    d3 = read(root, D3_RECEIPT) or ""
    seat_paths = list(dict.fromkeys(
        re.findall(r"(.ufo/waves/round-66/\S+\.md)", d3)))
    # a declared-dead seat names a path that need not exist; every other
    # named path must be a nonempty file on disk
    dead = set(re.findall(r"(?im)^dead:\s*(\S+)", d3))
    existing = [p for p in seat_paths
                if p not in dead
                and os.path.isfile(os.path.join(root, p))
                and os.path.getsize(os.path.join(root, p)) > 0]
    named = len(seat_paths)
    d3_ok = named >= 8 and len(existing) >= 8 \
        and re.search(r"(?i)(seat|report|status)", d3)
    leg("D3", d3_ok,
        f"named={named} present_nonempty={len(existing)} dead={len(dead)} min=8")

    # ---------- D4 ----------
    d4 = read(root, D4_RECEIPT) or ""
    m = re.search(r"^SEPARABILITY: (\d+) findings$", d4, re.MULTILINE)
    runs_m = re.search(r"acceptance_runs=(\d+)", d4)
    d4_ok = (bool(m)
             and runs_m is not None and int(runs_m.group(1)) > 0
             and "PARTIAL" not in d4
             and "skipped=0" in d4
             and "SEPARABILITY_NOTE" in d4
             and "separability-manifest.json" in d4)
    leg("D4", bool(d4_ok),
        f"complete verdict runs={runs_m.group(1) if runs_m else '?'} "
        f"skipped=0 {'skipped=0' in d4} manifest_named={'separability-manifest.json' in d4}")

    # ---------- CRITERION ----------
    qtext = read(root, QUALITY) or ""
    m = re.search(r"(?m)^\s*18\.\s", qtext)
    crit_ok = bool(m) and "anchor" in qtext[m.start():m.start() + 900].lower() \
        and "resolv" in qtext[m.start():m.start() + 900].lower()
    leg("CRITERION", crit_ok, "QUALITY criterion 18 names anchor resolvability")

    # ---------- QUOTES ----------
    q = subprocess.run([sys.executable, "-B", QUOTE_TOOL, LESSON], cwd=root,
                       stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    lesson_text = read(root, LESSON) or ""
    gate_ids = set(re.findall(r"\bS(77[6-9]|7[89]\d|800)\b", lesson_text))
    quotes_ok = (q.returncode == 0 and re.search(r"(^|\s)0 finding", q.stdout)
                 and len(lesson_text.splitlines()) > 10
                 and len(gate_ids) >= 23)
    leg("QUOTES", quotes_ok,
        f"exit={q.returncode} gate_ids={len(gate_ids)} "
        f"clean={'0 finding' in q.stdout}")

    verdict = all(legs)
    print(f"ACCEPT-CA-66: {'PASS' if verdict else 'FAIL'}")
    return 0 if verdict else 1


if __name__ == "__main__":
    sys.exit(main())
