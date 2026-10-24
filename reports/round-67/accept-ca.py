#!/usr/bin/env python3
r"""Round-67 claim Ca acceptance, revision 0 (pre-data).

Calibration claim (records): the round-66 verifier spot-check's routed
defects R66-D1..D5 are dispositioned in this round's records
(corpus/lessons/round-66-verifier-spotcheck.md §5), and the receipt
sequencing protocol itself is hardened so a receipt can never again record
a lands-time FAIL where the predicate only became evaluable post-records.

Receipt discipline (QUALITY.md criterion 19): --lands <40hex> is REQUIRED;
the receipt records stamped (== --lands), evaluated (== `git rev-parse
main`) and measured revisions plus tree and counter sha256; STAMP fails
unless evaluated == stamped. Counters run inside a materialized clone at
the lands commit. Carrier-parentage is post-records evidence
(check-receipt-seq.py --topo -> reports/round-67/telemetry/post-records.txt),
never a lands-time leg.

Legs (each prints `NAME PASS|FAIL detail`):
  STAMP    `git rev-parse main` == --lands (evaluated == stamped)
  D1       R66-D1 wave evidence durable: the committed manifest
           reports/round-67/dispositions/r66-wave-evidence-manifest.txt
           parses; every listed path is TRACKED at the lands revision
           (`git cat-file -e <lands>:<path>`); >=8 seat reports named;
           excluded scratch trees are named with reasons
  D2       R66-D2 registry placement: sources-census.sh validate --file on
           the lands-tree corpus/SOURCES.md exits 0 (E12 x23, E11 x1 gone);
           S776/S779-S800 sit inside ## Registry; S753 used-by is '—'
  D3       R66-D4 ledger restored: LOG.md carries a 'Round 66' heading and
           'round-66' mentions; SCORECARD.md carries an 'Axes — round 66'
           table with coverage/operability/calibration rows
  D4       R66-D5 first-class rejects: registry rows S801-S804 exist exactly
           once each with status rejected and 'REJECTED:' teaches cells,
           plus >=2 rejected rows opened 2026-10-24 from the round-67 gate
  SEQ      the frozen counters' own discipline: every
           reports/round-67/accept-{c,o,ca}.py requires --lands, prints
           stamped/evaluated headers, and asserts equality before its
           verdict; tools/check-receipt-seq.py --selftest exits 0
  CRITERION corpus/QUALITY.md gains criterion 19 grounding receipt
           sequencing (stamped/evaluated equality, materialized lands
           evaluation, post-records carrier-parentage)
  QUOTES   tools/check-gate-quotes.py finds 0 findings on
           corpus/lessons/round-67.md and its Gate names >=20 of S805-S828

Output ends `ACCEPT-CA-67: PASS|FAIL`; exit 0/1, or 2 on unusable input.
"""

import argparse
import hashlib
import os
import re
import subprocess
import sys

CENSUS = "/home/vgpnk/Projects/shokunin/scripts/sources-census.sh"
MANIFEST = "reports/round-67/dispositions/r66-wave-evidence-manifest.txt"
REGISTRY = "corpus/SOURCES.md"
LOG = "LOG.md"
SCORECARD = "SCORECARD.md"
QUALITY = "corpus/QUALITY.md"
LESSON = "corpus/lessons/round-67.md"
QUOTE_TOOL = "tools/check-gate-quotes.py"
SEQ_TOOL = "tools/check-receipt-seq.py"
COUNTERS = ["reports/round-67/accept-c.py",
            "reports/round-67/accept-o.py",
            "reports/round-67/accept-ca.py"]
ROW_RE = re.compile(r"^\|\s*(S\d+)\s*\|")
R66_ROWS = ["S776"] + [f"S{n}" for n in range(779, 801)]
R66_REJECTS = [f"S{n}" for n in range(801, 805)]


def read(root, path):
    try:
        with open(os.path.join(root, path), encoding="utf-8") as fh:
            return fh.read()
    except (OSError, UnicodeDecodeError):
        return None


def git_out(root, args):
    proc = subprocess.run(["git", "-C", root] + args,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return proc.returncode, proc.stdout.decode("utf-8", "replace")


def _run():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--lands", required=True,
                    help="the lands revision this run claims to measure")
    args = ap.parse_args()
    root = os.path.abspath(args.root)
    lands = args.lands
    self_sha = hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest()
    if not re.fullmatch(r"[0-9a-f]{40}", lands or ""):
        print("STAMP FAIL --lands is not a full commit hash")
        print("ACCEPT-CA-67: FAIL")
        return 2
    code, mv_rev = git_out(root, ["rev-parse", "main"])
    mv_rev = mv_rev.strip()
    code, tree_rev = git_out(root, ["rev-parse", f"{lands}^{{tree}}"])
    tree_rev = tree_rev.strip()
    print(f"# counter sha256 (self): {self_sha}")
    print(f"# stamped revision: {lands}")
    print(f"# evaluated revision: {mv_rev or 'unresolvable'}")
    print(f"# measured revision (lane main): {mv_rev or 'unresolvable'}")
    print(f"# tree: {tree_rev or 'unresolvable'}")
    legs = []

    def leg(name, ok, detail):
        legs.append(bool(ok))
        print(f"{name} {'PASS' if ok else 'FAIL'} {detail}")

    stamp_ok = bool(re.fullmatch(r"[0-9a-f]{40}", mv_rev)) \
        and mv_rev == lands and bool(re.fullmatch(r"[0-9a-f]{40}", tree_rev))
    leg("STAMP", stamp_ok,
        f"stamped={lands[:8]} evaluated={mv_rev[:8]} "
        f"equal={mv_rev == lands} tree={tree_rev[:8]}")
    if not stamp_ok:
        print("ACCEPT-CA-67: FAIL")
        return 1

    # ---------- D1 ----------
    man = read(root, MANIFEST)
    d1_bad = []
    if man is None:
        d1_bad.append("manifest_absent")
        leg("D1", False, f"bad={d1_bad}")
    else:
        include, exclude = [], []
        for raw in man.splitlines():
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            m = re.match(r"^INCLUDE\s+(\S+)", line)
            if m:
                include.append(m.group(1))
            elif re.match(r"^EXCLUDE\s+", line):
                exclude.append(line)
        seat = [p for p in include if re.match(
            r"\.ufo/waves/round-66/w1/[^/]+\.md$", p)]
        untracked = []
        for p in include:
            c, _ = git_out(root, ["cat-file", "-e", f"{lands}:{p}"])
            if c != 0:
                untracked.append(p)
        if not include:
            d1_bad.append("no_includes")
        if len(seat) < 8:
            d1_bad.append(f"seat_reports={len(seat)}")
        if untracked:
            d1_bad.append(f"untracked={untracked[:4]}")
        if not exclude:
            d1_bad.append("no_exclusions_named")
        leg("D1", not d1_bad,
            f"bad={d1_bad} includes={len(include)} seats={len(seat)}")

    # ---------- D2 ----------
    reg_path = os.path.join(root, REGISTRY)
    reg = read(root, REGISTRY)
    d2_bad = []
    if reg is None:
        d2_bad.append("registry_absent")
        leg("D2", False, f"bad={d2_bad}")
    else:
        c = subprocess.run([CENSUS, "validate", "--file", reg_path],
                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                           text=True)
        e_lines = [l for l in c.stdout.splitlines() if "\tE" in l]
        if c.returncode != 0:
            d2_bad.append(f"census_exit={c.returncode} E={e_lines[:4]}")
        # placement: r66 rows under ## Registry, not ## Leads
        heads = [(m.group(0), m.start())
                 for m in re.finditer(r"(?m)^##\s+\S.*$", reg)]
        reg_pos = next((s for t, s in heads if "Registry" in t), -1)
        leads_pos = next((s for t, s in heads if "Leads" in t), len(reg))
        for sid in R66_ROWS:
            m = re.search(rf"(?m)^\|\s*{sid}\s*\|", reg)
            if not m:
                d2_bad.append(f"{sid}:absent")
            elif not (reg_pos <= m.start() < leads_pos):
                d2_bad.append(f"{sid}:outside_registry")
        m753 = re.search(r"(?m)^\|\s*S753\s*\|", reg)
        if m753:
            c753 = [x.strip() for x in m753.group(0).split("|")[1:-1]]
            if len(c753) == 11 and c753[10] != "—":
                d2_bad.append(f"S753:used-by={c753[10]!r}")
        else:
            d2_bad.append("S753:absent")
        leg("D2", not d2_bad,
            f"bad={d2_bad} census_exit={c.returncode} E_lines={len(e_lines)}")

    # ---------- D3 ----------
    log = read(root, LOG) or ""
    sc = read(root, SCORECARD) or ""
    d3_bad = []
    if not re.search(r"(?im)^#+.*round[ -]?66\b", log):
        d3_bad.append("log:no_round66_heading")
    if "round-66" not in log and "Round 66" not in log:
        d3_bad.append("log:no_round66_mentions")
    if not re.search(r"(?im)axes\s*—\s*round[ -]?66", sc):
        d3_bad.append("scorecard:no_axes66")
    for ax in ("coverage", "operability", "calibration"):
        if not re.search(rf"(?im){ax}.*round[ -]?66|round[ -]?66.*{ax}", sc):
            d3_bad.append(f"scorecard:no_{ax}")
    leg("D3", not d3_bad, f"bad={d3_bad}")

    # ---------- D4 ----------
    d4_bad = []
    if reg is None:
        d4_bad.append("registry_absent")
    else:
        rej_opened_today = 0
        for line in reg.splitlines():
            m = ROW_RE.match(line)
            if not m:
                continue
            c = [x.strip() for x in line.split("|")[1:-1]]
            if len(c) != 11:
                continue
            sid = m.group(1)
            if sid in R66_REJECTS:
                if c[7] != "rejected":
                    d4_bad.append(f"{sid}:status={c[7]}")
                if "REJECTED:" not in c[6] or "flip:" not in c[6]:
                    d4_bad.append(f"{sid}:teaches_no_rejected")
            if c[7] == "rejected" and c[8] == "2026-10-24":
                rej_opened_today += 1
        once = {s for s in R66_REJECTS
                if len(re.findall(rf"(?m)^\|\s*{s}\s*\|", reg)) != 1}
        if once:
            d4_bad.append(f"nonunique={sorted(once)}")
        new_rejects = rej_opened_today - len(
            [s for s in R66_REJECTS
             if re.search(rf"(?m)^\|\s*{s}\s*\|", reg)])
        if rej_opened_today < len(R66_REJECTS) + 2:
            d4_bad.append(f"rejected_opened_today={rej_opened_today}")
        leg("D4", not d4_bad,
            f"bad={d4_bad} r66_rejects={len(R66_REJECTS)} "
            f"opened_today={rej_opened_today}")

    # ---------- SEQ ----------
    seq_bad = []
    for cpath in COUNTERS:
        text = read(root, cpath) or ""
        if "--lands" not in text or "required=True" not in text:
            seq_bad.append(f"{cpath}:no_required_lands")
        if "stamped revision" not in text or "evaluated revision" not in text:
            seq_bad.append(f"{cpath}:no_headers")
        if "mv_rev == lands" not in text.replace("mv_rev==lands", "mv_rev == lands"):
            seq_bad.append(f"{cpath}:no_equality_assert")
    st = subprocess.run([sys.executable, "-B", SEQ_TOOL, "--selftest"],
                        cwd=root, stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT, text=True)
    if st.returncode != 0 or "14/14" not in st.stdout:
        seq_bad.append(f"tool_selftest={st.returncode}")
    leg("SEQ", not seq_bad, f"bad={seq_bad[:6]}")

    # ---------- CRITERION ----------
    qtext = read(root, QUALITY) or ""
    m = re.search(r"(?m)^\s*19\.\s", qtext)
    crit_ok = bool(m) and "receipt" in qtext[m.start():m.start() + 1200].lower() \
        and "stamped" in qtext[m.start():m.start() + 1200].lower() \
        and "lands" in qtext[m.start():m.start() + 1200].lower()
    leg("CRITERION", crit_ok,
        "QUALITY criterion 19 names receipt sequencing")

    # ---------- QUOTES ----------
    q = subprocess.run([sys.executable, "-B", QUOTE_TOOL, LESSON], cwd=root,
                       stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                       text=True)
    lesson_text = read(root, LESSON) or ""
    gate_ids = set(re.findall(r"\bS(8[0-2]\d)\b", lesson_text)) & {
        f"S{n}" for n in range(805, 829)}
    quotes_ok = (q.returncode == 0 and "0 finding" in q.stdout
                 and len(lesson_text.splitlines()) > 10
                 and len(gate_ids) >= 20)
    leg("QUOTES", quotes_ok,
        f"exit={q.returncode} gate_ids={len(gate_ids)} "
        f"clean={'0 finding' in q.stdout}")

    verdict = all(legs)
    print(f"ACCEPT-CA-67: {'PASS' if verdict else 'FAIL'}")
    return 0 if verdict else 1


def main():
    try:
        return _run()
    except (RuntimeError, OSError, subprocess.SubprocessError, ValueError,
            KeyError) as exc:
        print(f"COUNTER_FAULT infrastructure unusable: {exc!r}")
        print("ACCEPT-CA-67: FAIL")
        return 2


if __name__ == "__main__":
    sys.exit(main())
