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
  D2 (rev1) sources-census validate --file corpus/SOURCES.md exits 0; the
            census W04 URL multiset at lands equals the multiset measured
            at BASE (no new cross-scope duplicate URLs from round rows,
            none hidden by census-evasion indentation); ledger rows for
            the dedup ids + chain s-ids + every flagged id carry a ruling
            (activate/retire/keep-*). Rev 0's zero-W04 demand was false at
            every in-model state (round-58 pre-data revision precedent:
            telemetry/w04-impossibility.txt, w1/CriticAmendD2.md;
            claims.json revision_note).
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
# W04 ids the census empirically flags at BASE (measured 2026-10-24;
# claims.json W04_FLAGGED additionally names S200, which the census does
# not flag — frozen-set drift recorded in the round report). Rev-0 D2
# demanded zero W04 lines; that state is unreachable by any permitted
# registry transform (reports/round-68/telemetry/w04-impossibility.txt:
# W04 per URL group = distinct_scopes - 1, status/order independent, and
# pair S094/S132 is both-rejected + both-immutable). Rev 1 dispositions
# the frozen set instead.
W04_BASE = [
    "S127", "S128", "S129", "S130", "S131", "S132", "S133", "S185", "S186",
    "S358", "S482", "S483", "S485", "S490", "S561", "S564", "S565", "S566",
    "S569", "S570", "S571", "S572", "S573", "S648", "S649", "S650", "S651",
    "S830",
]
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

    # ---------- D2 (revision 1, pre-data — claims.json revision_note) ----------
    # Rev 0 demanded a W04-free census; false at every in-model state and
    # true only under an out-of-model census-evasion (4-space indentation —
    # see telemetry/w04-impossibility.txt and the CriticAmendD2 attack).
    # Rev 1: the census stays exit-0 at lands; the census's W04 URL multiset
    # at lands equals the multiset measured at BASE (no new cross-scope
    # duplicate URLs introduced by round rows, none hidden by evasion); and
    # every flagged id plus every DEDUP/chain id carries a ledger row with a
    # ruling in RULINGS. URLs, not printed ids, are compared: the printed id
    # depends on row order, a permitted transform, so an order change must
    # not fail a true claim.
    def _census_w04(url_or_path):
        c = subprocess.run([CENSUS, "validate", "--file", url_or_path],
                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                           text=True)
        urls = []
        for ln in c.stdout.splitlines():
            parts = ln.split("\t")
            if len(parts) > 3 and parts[1] == "W04":
                m = re.search(r"duplicate url (\S+) across scopes", parts[3])
                if m:
                    urls.append(m.group(1))
        return sorted(urls), c.returncode

    reg = read(root, REGISTRY)
    led = ledger_rows(read(root, LEDGER))
    d2_bad = []
    w04 = []
    if reg is None:
        d2_bad.append("registry_absent")
        leg("D2", False, f"bad={d2_bad}")
    else:
        reg_path = os.path.join(root, REGISTRY)
        w04, census_rc = _census_w04(reg_path)
        if census_rc != 0:
            d2_bad.append(f"census_exit={census_rc}")
        try:
            # --file mode resolves used-by paths against dirname(file)/..,
            # so the base copy must sit inside <root>/corpus (see the census
            # usedby_findings/resolve_targets); /tmp staging floods E11.
            base_path = os.path.join(root, "corpus",
                                     ".r68-base-sources.tmp")
            with open(base_path, "w", encoding="utf-8") as _bh:
                _bh.write(git_bytes(root, BASE, REGISTRY) or "")
            base_w04, base_rc = _census_w04(base_path)
            os.unlink(base_path)
        except OSError as exc:
            base_w04, base_rc = None, f"err:{exc!r}"
        if not isinstance(base_rc, int) or base_rc != 0:
            d2_bad.append(f"base_census_exit={base_rc}")
        elif w04 != base_w04:
            d2_bad.append(f"w04_urls_delta=+{sorted(set(w04) - set(base_w04))}"
                          f"-{sorted(set(base_w04) - set(w04))}")
        led_map = {r[0]: r for r in led}
        for sid in sorted(DEDUP_IDS | PENDING_S | set(W04_BASE)):
            row = led_map.get(sid)
            if row is None:
                d2_bad.append(f"{sid}:no_ledger_row")
            elif row[3] not in RULINGS:
                d2_bad.append(f"{sid}:ruling={row[3]!r}")
        leg("D2", not d2_bad,
            f"bad={d2_bad[:6]} w04={len(w04)} census_exit={census_rc}")

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
    # revision 1 (pre-data, CriticAmendD2): the row parse previously read
    # m.group(0) of a `| S### |`-only match (1 cell, 34/34 skipped). Match
    # the full row line so queued/ruling consistency is actually measured.
    r68_bad = []
    if reg is None:
        r68_bad.append("registry_absent")
    else:
        for sid in sorted(R68_ROWS):
            if len(re.findall(rf"(?m)^\|\s*{sid}\s*\|", reg)) != 1:
                r68_bad.append(f"{sid}:count")
        for sid in sorted(PENDING_S):
            m = re.search(rf"(?m)^\|\s*{sid}\s*\|[^\n]*", reg)
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
