#!/usr/bin/env python3
r"""Round-81 counter for claim C (calibration, capability acquisition): the
orphaned-evidence sweep. Grades committed bytes at --lands against constants
read at --freeze. Never grades a worktree.

Legs (frozen in reports/round-81/claims.json claim C .legs):
  FROZENCFG  lands claims.json bytes == freeze claims.json bytes
  TOOL       the checker exists at lands with the pinned sha/size/markers
  REDRUN     a fresh run of the checker (extracted from lands) exits 1 and
             names EXACTLY the frozen red orphan set (no more, no less)
  RECEIPT    the committed red receipt exists at lands, names every frozen
             orphan, and carries the frozen summary line
  DISPOSED   the dispositions record exists at lands and names every frozen
             orphan plus the checker path
  SEPARABLE  base..lands touches only allowed_c_paths + sibling_paths

Refusals (exit 2, `FAIL legs=0/<n> (refused: ...)`, never a PASS): a revision
that is not 40-hex; a freeze that is not an ancestor of lands; lands equal to
the frozen base (the do-nothing control); unreadable frozen claims.json or an
incomplete frozen config; a leg list that disagrees with this counter's leg
table (LEGCOUNT); a --work that is not an existing directory.
"""
import argparse
import hashlib
import json
import os
import re
import subprocess
import sys

LABEL = "ACCEPT-C-81"
LEGS = ["FROZENCFG", "TOOL", "REDRUN", "RECEIPT", "DISPOSED", "SEPARABLE"]
TOOL_PATH = "tools/check-orphan-evidence.py"


def run(repo, *a, **kw):
    return subprocess.run(["git", "-C", repo] + list(a), capture_output=True, **kw)


def gout(repo, *a):
    r = run(repo, *a)
    if r.returncode != 0:
        raise RuntimeError("git %s: %s" % (a[0], (r.stderr or b"").decode("utf-8", "replace").strip()))
    return r.stdout.decode("utf-8", "replace")


def sha_bytes(b):
    return hashlib.sha256(b).hexdigest()


class Refuse(Exception):
    pass


def show(repo, rev, path):
    r = run(repo, "show", "%s:%s" % (rev, path))
    if r.returncode != 0:
        return None
    return r.stdout


def build_args():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", required=True)
    ap.add_argument("--fleet", required=True, help="fleet repo root (closed reports)")
    ap.add_argument("--lands", required=True)
    ap.add_argument("--freeze", required=True)
    ap.add_argument("--work", required=True)
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if not re.fullmatch(r"[0-9a-f]{40}", args.lands):
        raise Refuse("--lands %r is not a 40-hex commit" % args.lands)
    if not re.fullmatch(r"[0-9a-f]{40}", args.freeze):
        raise Refuse("--freeze %r is not a 40-hex commit" % args.freeze)
    if not os.path.isdir(args.work):
        raise Refuse("--work must name an existing scratch directory")
    return args


def read_frozen(repo, freeze):
    b = show(repo, freeze, "reports/round-81/claims.json")
    if b is None:
        raise Refuse("frozen claims.json unreadable at %s" % freeze)
    try:
        doc = json.loads(b.decode("utf-8"))
    except ValueError as exc:
        raise Refuse("frozen claims.json does not parse: %s" % exc)
    claim = None
    for cl in doc.get("claims", []):
        if cl.get("id") == "C":
            claim = cl
    if claim is None:
        raise Refuse("frozen claims.json carries no claim C")
    legs = claim.get("sweep81", {}).get("legs", [])
    if list(legs) != LEGS:
        raise Refuse("LEGCOUNT: frozen legs %r != counter legs %r" % (legs, LEGS))
    return doc, claim["sweep81"], b


def check_ancestry(repo, lands, freeze, base):
    r = run(repo, "cat-file", "-t", lands)
    if r.returncode != 0 or r.stdout.decode().strip() != "commit":
        raise Refuse("lands %s is not a commit" % lands)
    if lands == base:
        raise Refuse("lands equals the frozen base %s (do-nothing control)" % base)
    r = run(repo, "merge-base", "--is-ancestor", freeze, lands)
    if r.returncode != 0:
        raise Refuse("freeze %s is not an ancestor of lands %s" % (freeze, lands))


def receipt_headers(repo, args, freeze_sha):
    tree = gout(repo, "rev-parse", "%s^{tree}" % args.lands).strip()
    r = run(repo, "rev-parse", "main")
    main_tip = r.stdout.decode().strip() if r.returncode == 0 else "<no main>"
    self_sha = sha_bytes(open(os.path.abspath(__file__), "rb").read())
    return [
        "# stamped revision: %s" % args.lands,
        "# evaluated revision: %s" % args.lands,
        "# measured revision (lane main): %s" % main_tip,
        "# tree: %s" % tree,
        "# counter sha256 (self): %s" % self_sha,
        "# config source: git show %s:reports/round-81/claims.json (never the graded tree)" % args.freeze,
        "# config sha256 (frozen claims.json): %s" % freeze_sha,
    ]


def main():
    try:
        args = build_args()
    except Refuse as exc:
        print("%s: FAIL legs=0/%d (refused: %s)" % (LABEL, len(LEGS), exc))
        return 2
    repo = os.path.abspath(args.root)
    try:
        doc, cfg, frozen_claims = read_frozen(repo, args.freeze)
        base = cfg.get("base") or doc.get("base")
        check_ancestry(repo, args.lands, args.freeze, base)
    except (Refuse, RuntimeError) as exc:
        print("%s: FAIL legs=0/%d (refused: %s)" % (LABEL, len(LEGS), exc))
        return 2
    for key in ("tool_path", "tool_sha256", "tool_min_bytes", "tool_max_bytes",
                "tool_markers", "selftest_expected", "red_receipt_path",
                "red_orphans", "red_summary", "dispositions_path",
                "allowed_c_paths"):
        if key not in cfg:
            print("%s: FAIL legs=0/%d (refused: frozen config incomplete: %s)"
                  % (LABEL, len(LEGS), key))
            return 2

    freeze_sha = sha_bytes(frozen_claims)
    print("# frozen legs: %d (%s)" % (len(LEGS), ", ".join(LEGS)))
    for ln in receipt_headers(repo, args, freeze_sha):
        print(ln)

    results = []
    py = sys.executable

    # FROZENCFG
    b = show(repo, args.lands, "reports/round-81/claims.json")
    if b is None:
        results.append(("FROZENCFG", "FAIL", "claims.json absent at lands"))
    elif sha_bytes(b) != sha_bytes(frozen_claims):
        results.append(("FROZENCFG", "FAIL", "claims.json at lands differs from the frozen bytes"))
    else:
        results.append(("FROZENCFG", "PASS", "lands bytes == freeze bytes"))

    # TOOL
    tb = show(repo, args.lands, cfg["tool_path"])
    ok = True
    why = []
    if tb is None:
        ok, why = False, ["checker absent at lands"]
    else:
        if sha_bytes(tb) != cfg["tool_sha256"]:
            ok = False; why.append("checker sha mismatch")
        n = len(tb)
        if not (cfg["tool_min_bytes"] <= n <= cfg["tool_max_bytes"]):
            ok = False; why.append("checker size %d outside [%d, %d]" % (n, cfg["tool_min_bytes"], cfg["tool_max_bytes"]))
        text = tb.decode("utf-8", "replace")
        for m in cfg["tool_markers"]:
            if m not in text:
                ok = False; why.append("marker missing: %r" % m)
    results.append(("TOOL", "PASS" if ok else "FAIL", "; ".join(why) or "sha/size/markers ok"))

    # REDRUN: fresh run of the lands checker over the fleet reports
    fresh = {}
    if ok:
        wd = os.path.join(args.work, "redrun")
        os.makedirs(wd, exist_ok=True)
        tp = os.path.join(wd, "check-orphan-evidence.py")
        with open(tp, "wb") as fh:
            fh.write(tb)
        r = subprocess.run([py, "-B", tp, "--fleet", args.fleet,
                            "--lane", repo, "--extra-dir",
                            os.path.join(repo, "corpus", "lessons")],
                           capture_output=True)
        text = (r.stdout or b"").decode("utf-8", "replace")
        for ln in text.splitlines():
            if ln.startswith("ORPHAN-ABSENT ") or ln.startswith("ORPHAN-ONDISK "):
                fresh[ln.split()[1]] = ln.split()[0]
        summary = [ln for ln in text.splitlines() if ln.startswith("ORPHAN-EVIDENCE:")]
        want = set(cfg["red_orphans"])
        got = set(fresh)
        line = summary[0] if summary else "<no summary>"
        redrun_ok = (r.returncode == 1 and got == want
                     and all(v == "ORPHAN-ABSENT" for v in fresh.values())
                     and line == "ORPHAN-EVIDENCE: " + cfg["red_summary"])
        results.append(("REDRUN", "PASS" if redrun_ok else "FAIL",
                        line if redrun_ok else "orphans %r != frozen set (exit %d)" % (sorted(got), r.returncode)))
    else:
        results.append(("REDRUN", "FAIL", "checker not usable at lands"))

    # RECEIPT
    rb = show(repo, args.lands, cfg["red_receipt_path"])
    rec_ok = False
    why = "receipt absent at lands"
    if rb is not None:
        rt = rb.decode("utf-8", "replace")
        missing = [p for p in cfg["red_orphans"] if p not in rt]
        has_summary = ("ORPHAN-EVIDENCE: " + cfg["red_summary"]) in rt
        rec_ok = not missing and has_summary
        why = "all orphans + summary named" if rec_ok else "missing %r summary=%s" % (missing, has_summary)
    results.append(("RECEIPT", "PASS" if rec_ok else "FAIL", why))

    # DISPOSED
    db = show(repo, args.lands, cfg["dispositions_path"])
    disp_ok = False
    why = "dispositions record absent at lands"
    if db is not None:
        dt = db.decode("utf-8", "replace")
        missing = [p for p in cfg["red_orphans"] if p not in dt]
        tool_ok = cfg["tool_path"] in dt
        disp_ok = not missing and tool_ok
        why = "all orphans + checker named" if disp_ok else "missing %r tool=%s" % (missing, tool_ok)
    results.append(("DISPOSED", "PASS" if disp_ok else "FAIL", why))

    # SEPARABLE
    allowed = set(cfg.get("allowed_c_paths", [])) | set(cfg.get("sibling_paths", []))
    changed = [ln for ln in gout(repo, "diff-tree", "-r", "--name-only",
                                 "%s..%s" % (base, args.lands)).splitlines() if ln]
    bad = [p for p in changed if not any(p == a or p.startswith(a) for a in allowed)]
    results.append(("SEPARABLE", "PASS" if not bad else "FAIL",
                    "0 foreign paths" if not bad else "foreign: %s" % bad[:4]))

    npass = 0
    for name, verdict, why in results:
        print("LEG %s %s (%s)" % (verdict, name, why))
        npass += verdict == "PASS"
    print("%s: %s legs=%d/%d" % (LABEL, "PASS" if npass == len(LEGS) else "FAIL",
                                 npass, len(LEGS)))
    return 0 if npass == len(LEGS) else 1


def selftest(work):
    """Prove the refusal spine and the REDRUN/RECEIPT/DISPOSED leg logic on a
    synthetic fixture (a stub checker whose output is faked by a stub
    fleet-repo reports tree)."""
    import shutil
    ok = 0
    total = 0
    fx = os.path.join(work, "fx")
    if os.path.exists(fx):
        shutil.rmtree(fx, ignore_errors=True)
    env = dict(os.environ)
    env.update({"GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@invalid",
                "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@invalid",
                "GIT_CONFIG_GLOBAL": os.devnull, "GIT_CONFIG_NOSYSTEM": "1"})

    def sh(*a):
        return subprocess.run(["git", "-C", fx] + list(a), capture_output=True, env=env)

    os.makedirs(fx, exist_ok=True)
    subprocess.run(["git", "init", "-q", fx], capture_output=True, env=env)
    with open(os.path.join(fx, "seed.txt"), "w", newline="") as fh:
        fh.write("seed\n")
    sh("add", "seed.txt"); sh("commit", "-q", "-m", "base")
    base = sh("rev-parse", "HEAD").stdout.decode().strip()
    os.makedirs(os.path.join(fx, "tools"), exist_ok=True)
    with open(os.path.join(fx, "tools", "check-orphan-evidence.py"), "w", newline="") as fh:
        fh.write("# stub " + "x" * 100 + "\n")
    os.makedirs(os.path.join(fx, "reports", "round-81"), exist_ok=True)
    cfg_stub = {
        "legs": LEGS, "base": base,
        "tool_path": "tools/check-orphan-evidence.py",
        "tool_sha256": hashlib.sha256(("# stub " + "x" * 100 + "\n").encode()).hexdigest(),
        "tool_min_bytes": 10, "tool_max_bytes": 900,
        "tool_markers": ["stub"], "selftest_expected": 11,
        "red_receipt_path": "reports/round-81/telemetry/red.txt",
        "red_orphans": ["reports/rx.txt"],
        "red_summary": "1 orphan(s) over 1 cited path(s) in 1 report(s)",
        "dispositions_path": "reports/round-81/annotations/disp.md",
        "allowed_c_paths": ["reports/round-81/", "tools/"], "sibling_paths": [],
    }
    claims = json.dumps({"round": 81, "base": base, "claims": [
        {"id": "C", "axis": "calibration", "sweep81": cfg_stub}]}, indent=1) + "\n"
    with open(os.path.join(fx, "reports", "round-81", "claims.json"), "w", newline="") as fh:
        fh.write(claims)
    sh("add", "-A"); sh("commit", "-q", "-m", "freeze")
    freeze = sh("rev-parse", "HEAD").stdout.decode().strip()

    # a stub fleet repo whose single kotodama report cites the one orphan
    fleet = os.path.join(work, "fleet")
    os.makedirs(os.path.join(fleet, ".ufo", "reports", "round-9"), exist_ok=True)
    with open(os.path.join(fleet, ".ufo", "reports", "round-9", "stublane.md"), "w", newline="") as fh:
        fh.write("cites `reports/rx.txt` here\n")

    me = os.path.abspath(__file__)
    wd = os.path.join(work, "wd")
    os.makedirs(wd, exist_ok=True)

    def counter(lands, freeze_, extra=None):
        argv = [sys.executable, "-B", me, "--root", fx, "--fleet", fleet,
                "--lands", lands, "--freeze", freeze_, "--work", wd]
        if extra:
            argv += extra
        return subprocess.run(argv, capture_output=True)

    def scenario(name, r, want_re, want_exit):
        nonlocal ok, total
        total += 1
        text = (r.stdout or b"").decode("utf-8", "replace")
        got = re.search(want_re, text)
        good = (r.returncode == want_exit) and bool(got)
        print("selftest: %s -> exit=%d %s as-expected=%s"
              % (name, r.returncode, (got.group(0) if got else text.strip()[:70])[:70],
                 "True" if good else "False"))
        if good:
            ok += 1

    # the stub checker must behave like the real one for REDRUN: build a stub
    # that scans nothing and prints the frozen summary + orphan line, then
    # freeze FIRST and land the receipt/dispositions after (freeze < lands)
    stub_body = (
        "# stub checker (selftest fixture)\n"
        "import sys\n"
        "print('ORPHAN-ABSENT reports/rx.txt cited=round-9')\n"
        "print('ORPHAN-EVIDENCE: 1 orphan(s) over 1 cited path(s) in 1 report(s)')\n"
        "sys.exit(1)\n")
    cfg_stub["tool_sha256"] = hashlib.sha256(stub_body.encode()).hexdigest()
    with open(os.path.join(fx, "tools", "check-orphan-evidence.py"), "w", newline="") as fh:
        fh.write(stub_body)
    claims2 = json.dumps({"round": 81, "base": base, "claims": [
        {"id": "C", "axis": "calibration", "sweep81": cfg_stub}]}, indent=1) + "\n"
    with open(os.path.join(fx, "reports", "round-81", "claims.json"), "w", newline="") as fh:
        fh.write(claims2)
    sh("add", "-A"); sh("commit", "-q", "-m", "freeze2")
    freeze2 = sh("rev-parse", "HEAD").stdout.decode().strip()

    r = counter(base, freeze2)
    scenario("lands==base refused", r, r"refused: lands equals the frozen base", 2)
    r = counter("zz", freeze2)
    scenario("non-40hex refused", r, r"refused: --lands .* not a 40-hex", 2)
    # a lands WITHOUT receipt/dispositions files: REDRUN passes, RECEIPT fails
    sh("commit", "-q", "--allow-empty", "-m", "lands-bare")
    lands = sh("rev-parse", "HEAD").stdout.decode().strip()
    r = counter(lands, freeze2)
    scenario("REDRUN pass on stub", r, r"LEG PASS REDRUN", 1)
    scenario("RECEIPT fails without receipt", r, r"LEG FAIL RECEIPT", 1)
    # now land the receipt + dispositions, expect a full PASS
    os.makedirs(os.path.join(fx, "reports", "round-81", "telemetry"), exist_ok=True)
    os.makedirs(os.path.join(fx, "reports", "round-81", "annotations"), exist_ok=True)
    with open(os.path.join(fx, "reports", "round-81", "telemetry", "red.txt"), "w", newline="") as fh:
        fh.write("# red\nORPHAN-ABSENT reports/rx.txt cited=round-9\n"
                 "ORPHAN-EVIDENCE: 1 orphan(s) over 1 cited path(s) in 1 report(s)\n")
    with open(os.path.join(fx, "reports", "round-81", "annotations", "disp.md"), "w", newline="") as fh:
        fh.write("dispositions for tools/check-orphan-evidence.py: reports/rx.txt -> none\n")
    sh("add", "-A"); sh("commit", "-q", "-m", "receipts")
    lands2 = sh("rev-parse", "HEAD").stdout.decode().strip()
    r = counter(lands2, freeze2)
    scenario("full pass on complete lands", r, r"ACCEPT-C-81: PASS legs=6/6", 0)
    # tamper: swap the stub checker so REDRUN's fresh output gains a second orphan
    with open(os.path.join(fx, "tools", "check-orphan-evidence.py"), "w", newline="") as fh:
        fh.write(stub_body.replace("1 cited path", "2 cited path").replace(
            "ORPHAN-EVIDENCE: 1", "ORPHAN-EVIDENCE: 2"))
    sh("add", "-A"); sh("commit", "-q", "-m", "tamper-tool")
    lands3 = sh("rev-parse", "HEAD").stdout.decode().strip()
    r = counter(lands3, freeze2)
    scenario("tampered checker fails TOOL", r, r"LEG FAIL TOOL", 1)
    print("SELFTEST-C81: %s (%d checks; counter sha256 %s)"
          % ("PASS" if ok == total else "FAIL", total,
             sha_bytes(open(me, "rb").read())))
    return 0 if ok == total else 1


if __name__ == "__main__":
    ap = argparse.ArgumentParser(add_help=False)
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--work", default="")
    known, _ = ap.parse_known_args()
    if known.selftest and known.work:
        sys.exit(selftest(known.work))
    sys.exit(main())
