#!/usr/bin/env python3
r"""Round-81 counter for claim O (operability): the W2 generator + the
replace-ref fixture builder. Grades committed bytes at --lands against
constants read at --freeze (QUALITY 25/26 shape). Never grades a worktree.

Legs (frozen in reports/round-81/claims.json claim O .legs):
  FROZENCFG  lands claims.json bytes == freeze claims.json bytes
  GEN        the W2 generator exists at lands with the pinned sha/size/markers
  MUTRUN     a fresh run of the generator at lands: exit 0, PASS 5/5, clean
             green first (the clean-first line and the hardened env control)
  FIXRUN     a fresh run of the replace-ref builder at lands: exit 0,
             REPLACEREFS-FIXTURE: PASS with old PASS pairs=1 and hardened
             REFUSED refs/replace verdict lines
  SELFTEST   this counter's refusal spine (run with --selftest; the leg passes
             when the committed selftest receipt exists and names this
             counter's sha with PASS)
  SEPARABLE  base..lands touches only allowed_o_paths + sibling_paths

Refusals (exit 2, `FAIL legs=0/<n> (refused: ...)`, never a PASS): a revision
that is not 40-hex; a freeze that is not an ancestor of lands; lands equal to
the frozen base (the do-nothing control); unreadable frozen claims.json; a leg
list that disagrees with this counter's leg table (LEGCOUNT); a --work that is
not an existing directory.
"""
import argparse
import hashlib
import json
import os
import re
import subprocess
import sys

LABEL = "ACCEPT-O-81"
LEGS = ["FROZENCFG", "GEN", "MUTRUN", "FIXRUN", "SELFTEST", "SEPARABLE"]
SELFTEST_RECEIPT = "reports/round-81/telemetry/selftest-o81.txt"
TOOL_PATH = "tools/ledger-token-guard.py"


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
        if cl.get("id") == "O":
            claim = cl
    if claim is None:
        raise Refuse("frozen claims.json carries no claim O")
    legs = claim.get("guard81", {}).get("legs", [])
    if list(legs) != LEGS:
        raise Refuse("LEGCOUNT: frozen legs %r != counter legs %r" % (legs, LEGS))
    return doc, claim["guard81"], b


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
    lines = [
        "# stamped revision: %s" % args.lands,
        "# evaluated revision: %s" % args.lands,
        "# measured revision (lane main): %s" % main_tip,
        "# tree: %s" % tree,
        "# counter sha256 (self): %s" % self_sha,
        "# config source: git show %s:reports/round-81/claims.json (never the graded tree)" % args.freeze,
        "# config sha256 (frozen claims.json): %s" % freeze_sha,
    ]
    return lines


def leg_frozencfg(repo, args, frozen_claims):
    b = show(repo, args.lands, "reports/round-81/claims.json")
    if b is None:
        return "FAIL", "claims.json absent at lands"
    if sha_bytes(b) != sha_bytes(frozen_claims):
        return "FAIL", "claims.json at lands differs from the frozen bytes"
    return "PASS", "lands bytes == freeze bytes"


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
    except Refuse as exc:
        print("%s: FAIL legs=0/%d (refused: %s)" % (LABEL, len(LEGS), exc))
        return 2
    except RuntimeError as exc:
        print("%s: FAIL legs=0/%d (refused: %s)" % (LABEL, len(LEGS), exc))
        return 2

    freeze_sha = sha_bytes(frozen_claims)
    for key in ("generator_path", "generator_sha256", "generator_min_bytes",
                "generator_max_bytes", "generator_markers", "builder_path",
                "builder_min_bytes", "builder_max_bytes", "old_rev",
                "allowed_o_paths"):
        if key not in cfg:
            print("%s: FAIL legs=0/%d (refused: frozen config incomplete: %s)"
                  % (LABEL, len(LEGS), key))
            return 2
    print("# frozen legs: %d (%s)" % (len(LEGS), ", ".join(LEGS)))
    for ln in receipt_headers(repo, args, freeze_sha):
        print(ln)

    results = []
    py = sys.executable

    # FROZENCFG
    verdict, why = leg_frozencfg(repo, args, frozen_claims)
    results.append(("FROZENCFG", verdict, why))

    # GEN
    gb = show(repo, args.lands, cfg["generator_path"])
    ok, why = True, []
    if gb is None:
        ok, why = False, ["generator absent at lands"]
    else:
        if sha_bytes(gb) != cfg["generator_sha256"]:
            ok = False; why.append("generator sha mismatch")
        n = len(gb)
        if not (cfg["generator_min_bytes"] <= n <= cfg["generator_max_bytes"]):
            ok = False; why.append("generator size %d outside [%d, %d]" % (n, cfg["generator_min_bytes"], cfg["generator_max_bytes"]))
        text = gb.decode("utf-8", "replace")
        for m in cfg["generator_markers"]:
            if m not in text:
                ok = False; why.append("marker missing: %r" % m)
    results.append(("GEN", "PASS" if ok else "FAIL", "; ".join(why) or "sha/size/markers ok"))

    # MUTRUN (fresh run of the generator at the lands bytes; the generator is
    # extracted from the lands commit because the lane tree carries
    # NTFS-uncheckoutable committed paths - lesson R79-M3 - so no worktree is
    # materialized; the generator reads the guard via git plumbing only)
    grun_ok = False
    mut_line = "<not run>"
    if ok:
        wd = os.path.join(args.work, "mutrun")
        os.makedirs(wd, exist_ok=True)
        gp_blob = show(repo, args.lands, cfg["generator_path"])
        if gp_blob is None:
            mut_line = "generator absent at lands"
        else:
            gp_path = os.path.join(wd, "w2-mutants.py")
            with open(gp_path, "wb") as fh:
                fh.write(gp_blob)
            r2 = subprocess.run([py, "-B", gp_path, "--repo", repo,
                                 "--rev", args.lands, "--work", wd],
                                capture_output=True)
            mut_text = (r2.stdout or b"").decode("utf-8", "replace") + (r2.stderr or b"").decode("utf-8", "replace")
            vl = [ln for ln in mut_text.splitlines() if ln.startswith("W2-RERUN:")] or ["<no verdict>"]
            mut_line = vl[0]
            grun_ok = (r2.returncode == 0 and "PASS 5/5" in mut_line
                       and "clean    selftest exit=0" in mut_text
                       and "control  hardened env-probe injected_leaked=0" in mut_text)
    results.append(("MUTRUN", "PASS" if grun_ok else "FAIL", mut_line))

    # FIXRUN (fresh run of the builder at the lands bytes)
    frun_ok = False
    fix_line = "<not run>"
    if ok:
        wd = os.path.join(args.work, "fixrun")
        os.makedirs(wd, exist_ok=True)
        fb = show(repo, args.lands, cfg["builder_path"])
        if fb is None:
            fix_line = "builder absent at lands"
        else:
            fb_path = os.path.join(wd, "build-fixture.py")
            with open(fb_path, "wb") as fh:
                fh.write(fb)
            r3 = subprocess.run([py, "-B", fb_path, "--repo", repo,
                                 "--old-rev", cfg["old_rev"],
                                 "--hard-rev", args.lands,
                                 "--work", wd], capture_output=True)
            fix_text = (r3.stdout or b"").decode("utf-8", "replace") + (r3.stderr or b"").decode("utf-8", "replace")
            fix_line = [ln for ln in fix_text.splitlines() if ln.startswith("REPLACEREFS-FIXTURE:")] or ["<no verdict>"]
            fix_line = fix_line[0]
            frun_ok = (r3.returncode == 0 and "REPLACEREFS-FIXTURE: PASS" in fix_line
                       and "PASS pairs=1" in fix_text
                       and "REFUSED --repo carries refs/replace entries" in fix_text)
    results.append(("FIXRUN", "PASS" if frun_ok else "FAIL", fix_line))

    # SELFTEST: the committed selftest receipt names this counter's sha and PASS
    rb = show(repo, args.lands, SELFTEST_RECEIPT)
    self_ok = False
    self_line = "receipt absent at lands"
    if rb is not None:
        rt = rb.decode("utf-8", "replace")
        self_sha = sha_bytes(open(os.path.abspath(__file__), "rb").read())
        self_ok = ("SELFTEST-O81: PASS" in rt) and (self_sha in rt)
        self_line = "SELFTEST-O81: PASS" if self_ok else "receipt lacks PASS or this counter's sha"
    results.append(("SELFTEST", "PASS" if self_ok else "FAIL", self_line))

    # SEPARABLE
    allowed = set(cfg.get("allowed_o_paths", [])) | set(cfg.get("sibling_paths", []))
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
    """Build a tiny fixture repo and prove the refusal spine + leg framing."""
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

    def sh(*a, **kw):
        return subprocess.run(["git", "-C", fx] + list(a), capture_output=True, env=env, **kw)

    os.makedirs(fx, exist_ok=True)
    subprocess.run(["git", "init", "-q", fx], capture_output=True, env=env)
    with open(os.path.join(fx, "seed.txt"), "w", newline="") as fh:
        fh.write("seed\n")
    sh("add", "seed.txt"); sh("commit", "-q", "-m", "base")
    base = sh("rev-parse", "HEAD").stdout.decode().strip()
    os.makedirs(os.path.join(fx, "reports", "round-81"), exist_ok=True)
    claims = json.dumps({"round": 81, "base": base, "claims": [
        {"id": "O", "axis": "operability", "guard81": {
            "legs": LEGS, "base": base,
            "generator_path": "reports/round-81/mutants/absent.py",
            "generator_sha256": "0" * 64, "generator_min_bytes": 1,
            "generator_max_bytes": 9, "generator_markers": [],
            "builder_path": "reports/round-81/fixtures/absent.py",
            "builder_min_bytes": 1, "builder_max_bytes": 9,
            "old_rev": base, "allowed_o_paths": ["reports/round-81/"],
            "sibling_paths": []}}]},
        indent=1) + "\n"
    with open(os.path.join(fx, "reports", "round-81", "claims.json"), "w", newline="") as fh:
        fh.write(claims)
    sh("add", "reports/round-81/claims.json"); sh("commit", "-q", "-m", "freeze")
    freeze = sh("rev-parse", "HEAD").stdout.decode().strip()

    me = os.path.abspath(__file__)
    wd = os.path.join(work, "wd")
    os.makedirs(wd, exist_ok=True)

    def counter(lands, freeze_, extra=None):
        argv = [sys.executable, "-B", me, "--root", fx, "--lands", lands,
                "--freeze", freeze_, "--work", wd]
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
              % (name, r.returncode, (got.group(0) if got else text.strip()[:60])[:60],
                 "True" if good else "False"))
        if good:
            ok += 1

    # 1. do-nothing control: lands == base
    r = counter(base, freeze)
    scenario("lands==base refused", r, r"refused: lands equals the frozen base", 2)
    # 2. non-40hex lands
    r = counter("not-a-rev", freeze)
    scenario("non-40hex lands refused", r, r"refused: --lands .* not a 40-hex", 2)
    # 3. freeze==lands is GRADED, never passed: with no generator at lands the
    #    graded run must FAIL on GEN with leg lines (not a refusal, not a PASS)
    r = counter(freeze, freeze)
    scenario("lands==freeze graded not passed", r, r"LEG FAIL GEN", 1)
    # 4. a graded-tree claims.json tamper fails FROZENCFG (frozen bytes intact)
    with open(os.path.join(fx, "reports", "round-81", "claims.json"), "w", newline="") as fh:
        fh.write(claims.replace('"legs"', '"legs2"'))
    sh("add", "reports/round-81/claims.json"); sh("commit", "-q", "-m", "tamper")
    tam = sh("rev-parse", "HEAD").stdout.decode().strip()
    r = counter(tam, freeze)
    scenario("tampered lands claims fails FROZENCFG", r, r"LEG FAIL FROZENCFG", 1)
    # 5. LEGCOUNT: a freeze whose claims.json legs differ from the leg table
    badf = os.path.join(fx, "reports", "round-81", "claims.json")
    bad_claims = json.dumps({"round": 81, "base": base, "claims": [
        {"id": "O", "axis": "operability", "guard81": {"legs": ["BOGUS"], "base": base}}]},
        indent=1) + "\n"
    with open(badf, "w", newline="") as fh:
        fh.write(bad_claims)
    sh("add", "reports/round-81/claims.json"); sh("commit", "-q", "-m", "badlegs")
    badfreeze = sh("rev-parse", "HEAD").stdout.decode().strip()
    sh("commit", "-q", "--allow-empty", "-m", "lands-after-badlegs")
    badlands = sh("rev-parse", "HEAD").stdout.decode().strip()
    r = counter(badlands, badfreeze)
    scenario("frozen legs disagree refused", r, r"refused: LEGCOUNT", 2)
    # 6. missing --work dir
    total += 1
    r = subprocess.run([sys.executable, "-B", me, "--root", fx, "--lands", freeze,
                        "--freeze", freeze, "--work", os.path.join(work, "nope")],
                       capture_output=True)
    good = r.returncode == 2 and b"existing scratch directory" in (r.stdout or b"")
    print("selftest: missing --work refused -> exit=%d as-expected=%s"
          % (r.returncode, "True" if good else "False"))
    if good:
        ok += 1
    print("SELFTEST-O81: %s (%d checks; counter sha256 %s)"
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
