#!/usr/bin/env python3
r"""Round-68 claim Ca acceptance, revision 0 (pre-data).

Calibration claim: the r67 sequencing discipline is re-demonstrated and the
two r67-routed defects land — R67-D1 (26 uncommitted .ufo/waves/ leftovers,
incl. the 172+ MiB fabric-c clone, swept or dispositioned) and R67-D2 (census
W04 duplicate-URL rows, dispositioned per source-tier rules). The claim holds
iff every leg passes: stamped==evaluated on the run's own receipt, the three
counter files carry the required --lands/stamped/evaluated machinery, the
frozen r67-D1 path list is gone from the worktree, the census validates with
zero W04 findings, the ledger's W04 rows are all dispositioned, the round's
records files carry the round-68 headings, and the lesson Gate holds >=20
located quotes for the new row band.

Receipt discipline (QUALITY.md criterion 19): --lands <40hex> REQUIRED;
stamped from --lands, evaluated from `git rev-parse main`; STAMP fails unless
equal. Evaluate against a `git clone --no-local` at the lands commit.

Legs (each prints `NAME PASS|FAIL detail`):
  STAMP     evaluated == stamped
  D1        every path in reports/round-68/dispositions/r67-d1-paths.txt is
            absent from the worktree at lands; the path list has >=20 entries
  D2        sources-census validate --file corpus/SOURCES.md exits 0 with no
            `W04` lines; ledger rows for the 33 dedup ids carry a ruling
            (activate/retire/keep-*) consistent with registry statuses
  D3        LOG.md and SCORECARD.md carry round-68 sections
  D4        the R68 rejection rows (S857, S858) are rejected with
            REJECTED:/flip: teaches; >=2 rejected rows opened 2026-10-24
  SEQ       the three counters require --lands and print stamped/evaluated;
            check-receipt-seq.py --selftest still passes 14/14
  R68       each r68 claim id S833-S856 is a unique registry row; the two
            reject rows unique; no row in the frozen settlement set retains
            status `queued` while its chain target stays `mined` unless a
            ledger row rules it keep-split
  CRITERION QUALITY.md criterion 19 names receipt sequencing (stamped/lands)
  QUOTES    check-gate-quotes on lessons/round-68.md exits 0 with
            `0 finding`, and >=20 gate ids in S833-S860
  FIXTURES  control runs: every counter exits nonzero when run with --lands
            pointing at BASE (stale evaluation), proving the stamp guard
"""

import argparse
import hashlib
import os
import re
import subprocess
import sys

BASE = "99fae3085ec858446df00c2b294748f635cb6c45"
CENSUS = "/home/vgpnk/Projects/shokunin/scripts/sources-census.sh"
D1_PATHS = "reports/round-68/dispositions/r67-d1-paths.txt"
LEDGER = "reports/round-68/dispositions/dedup-ledger.tsv"
REGISTRY = "corpus/SOURCES.md"
LOG = "LOG.md"
SCORECARD = "SCORECARD.md"
QUALITY = "corpus/QUALITY.md"
LESSON = "corpus/lessons/round-68.md"
QUOTE_TOOL = "tools/check-gate-quotes.py"
SEQ_TOOL = "tools/check-receipt-seq.py"
COUNTERS = ["reports/round-68/accept-c.py",
            "reports/round-68/accept-o.py",
            "reports/round-68/accept-ca.py"]
ROW_RE = re.compile(r"^\|\s*(S\d{3,})\s*\|")
R68_ROWS = {f"S{n}" for n in range(833, 857)}
R68_REJECTS = {"S857", "S858"}
DEDUP_IDS = {
    "S034", "S038", "S039", "S060", "S095", "S079", "S086", "S097", "S105",
    "S117", "S119", "S122", "S157", "S256", "S359", "S367", "S383", "S385",
    "S392", "S395", "S396", "S399", "S407", "S410", "S413", "S417", "S421",
    "S433", "S438", "S440", "S445", "S452", "S453",
}
PENDING_S = {
    "S044", "S045", "S046", "S070", "S125", "S126", "S127", "S128", "S129",
    "S130", "S131", "S133", "S186", "S358", "S481", "S482", "S483", "S484",
    "S485", "S486", "S487", "S488", "S489", "S490", "S491", "S560", "S561",
    "S562", "S564", "S565", "S566", "S567", "S568", "S569",
}
RULINGS = {"activate", "retire", "keep-successor", "keep-reject", "keep-split"}


def git_out(root, args):
    proc = subprocess.run(["git", "-C", root] + args,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return proc.returncode, proc.stdout.decode("utf-8", "replace").strip()


def read(root, rel):
    try:
        with open(os.path.join(root, rel), encoding="utf-8") as fh:
            return fh.read()
    except (OSError, UnicodeDecodeError):
        return None


def ledger_rows(text):
    rows = []
    for raw in (text or "").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        cells = [c.strip() for c in line.split("|")]
        if len(cells) == 7:
            rows.append(cells)
    return rows


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
        print("ACCEPT-CA-68: FAIL")
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
        print("ACCEPT-CA-68: FAIL")
        return 1

    # ---------- D1 ----------
    d1_text = read(root, D1_PATHS)
    d1_bad = []
    if d1_text is None:
        d1_bad.append("path_list_absent")
        paths = []
    else:
        paths = [l.strip() for l in d1_text.splitlines()
                 if l.strip() and not l.startswith("#")]
        if len(paths) < 20:
            d1_bad.append(f"paths={len(paths)}")
        present = [p for p in paths
                   if os.path.exists(os.path.join(root, p.rstrip("/")))]
        if present:
            d1_bad.append(f"present={present[:4]}")
    leg("D1", not d1_bad, f"bad={d1_bad} paths={len(paths)}")

    # ---------- D2 ----------
    reg = read(root, REGISTRY)
    led = ledger_rows(read(root, LEDGER))
    d2_bad = []
    if reg is None:
        d2_bad.append("registry_absent")
        leg("D2", False, f"bad={d2_bad}")
    else:
        reg_path = os.path.join(root, REGISTRY)
        c = subprocess.run([CENSUS, "validate", "--file", reg_path],
                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                           text=True)
        w04 = [l for l in c.stdout.splitlines() if "W04" in l]
        if c.returncode != 0:
            d2_bad.append(f"census_exit={c.returncode}")
        if w04:
            d2_bad.append(f"w04={len(w04)}")
        led_map = {r[0]: r for r in led}
        for sid in sorted(DEDUP_IDS | PENDING_S):
            row = led_map.get(sid)
            if row is None:
                d2_bad.append(f"{sid}:no_ledger_row")
            elif row[3] not in RULINGS:
                d2_bad.append(f"{sid}:ruling={row[3]!r}")
        leg("D2", not d2_bad,
            f"bad={d2_bad[:6]} w04={len(w04)} census_exit={c.returncode}")

    # ---------- D3 ----------
    log = read(root, LOG) or ""
    sc = read(root, SCORECARD) or ""
    d3_bad = []
    if not re.search(r"(?im)^#+.*round[ -]?68\b", log):
        d3_bad.append("log:no_round68_heading")
    if not re.search(r"(?im)axes\s*—\s*round[ -]?68", sc):
        d3_bad.append("scorecard:no_axes68")
    for ax in ("coverage", "operability", "calibration"):
        if not re.search(rf"(?im){ax}.*round[ -]?68|round[ -]?68.*{ax}", sc):
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
            if sid in R68_REJECTS:
                if c[7] != "rejected":
                    d4_bad.append(f"{sid}:status={c[7]}")
                if "REJECTED:" not in c[6] or "flip:" not in c[6]:
                    d4_bad.append(f"{sid}:teaches_no_rejected")
            # r66/r67 ran the same calendar day; count only the r68 band
            if c[7] == "rejected" and c[8] == "2026-10-24" \
                    and int(sid[1:]) >= 857:
                rej_opened_today += 1
        once = {s for s in R68_REJECTS
                if len(re.findall(rf"(?m)^\|\s*{s}\s*\|", reg)) != 1}
        if once:
            d4_bad.append(f"nonunique={sorted(once)}")
        if rej_opened_today < 2:
            d4_bad.append(f"r68_rejects={rej_opened_today}")
    leg("D4", not d4_bad, f"bad={d4_bad} r68_band={rej_opened_today}")

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

    # ---------- R68 ----------
    r68_bad = []
    if reg is None:
        r68_bad.append("registry_absent")
    else:
        for sid in sorted(R68_ROWS):
            if len(re.findall(rf"(?m)^\|\s*{sid}\s*\|", reg)) != 1:
                r68_bad.append(f"{sid}:count")
        for sid in sorted(PENDING_S):
            m = re.search(rf"(?m)^\|\s*{sid}\s*\|", reg)
            if not m:
                continue
            c = [x.strip() for x in m.group(0).split("|")[1:-1]]
            if len(c) != 11:
                continue
            row = next((r for r in led if r[0] == sid), None)
            ruling = row[3] if row else None
            if c[7] == "queued" and ruling != "keep-split":
                r68_bad.append(f"{sid}:still_queued")
            if ruling == "activate" and c[7] != "mined":
                r68_bad.append(f"{sid}:activate_not_mined")
            if ruling == "retire" and c[7] != "rejected":
                r68_bad.append(f"{sid}:retire_not_rejected")
    leg("R68", not r68_bad, f"bad={r68_bad[:6]}")

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
    gate_ids = set(re.findall(r"\b(S8[0-9]\d)\b", lesson_text)) & (
        {f"S{n}" for n in range(833, 861)})
    quotes_ok = (q.returncode == 0 and "0 finding" in q.stdout
                 and len(lesson_text.splitlines()) > 10
                 and len(gate_ids) >= 20)
    leg("QUOTES", quotes_ok,
        f"exit={q.returncode} gate_ids={len(gate_ids)} "
        f"clean={'0 finding' in q.stdout}")

    # ---------- FIXTURES ----------
    # base-stamp controls: accept-c and accept-o must exit nonzero run with
    # --lands pointing at BASE (stale evaluation). accept-ca itself is the
    # runner — including it would recurse into FIXTURES again.
    fx_bad = []
    for cpath in COUNTERS[:2]:
        rc = subprocess.run([sys.executable, "-B", cpath,
                             "--root", root, "--lands", BASE],
                            cwd=root, stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT, text=True)
        if rc.returncode == 0:
            fx_bad.append(f"{cpath}:base_stamp_passed")
    leg("FIXTURES", not fx_bad, f"bad={fx_bad}")

    verdict = all(legs)
    print(f"ACCEPT-CA-68: {'PASS' if verdict else 'FAIL'}")
    return 0 if verdict else 1


def main():
    try:
        return _run()
    except (RuntimeError, OSError, subprocess.SubprocessError, ValueError,
            KeyError) as exc:
        print(f"COUNTER_FAULT infrastructure unusable: {exc!r}")
        print("ACCEPT-CA-68: FAIL")
        return 2


if __name__ == "__main__":
    sys.exit(main())
