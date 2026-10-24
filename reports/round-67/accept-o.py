#!/usr/bin/env python3
r"""Round-67 claim O acceptance, revision 0 (pre-data).

Operability claim (capability acquisition): the receipt-sequencing discipline
that produced the r65/r66 Ca rejections becomes a runnable tool,
tools/check-receipt-seq.py — receipt header equality (stamped/evaluated/
measured + tree + counter sha256), committed-bytes evaluation at --lands, and
post-records carrier-parentage (--topo). The round-66 closure's recommended
fix (`corpus/lessons/round-66-verifier-spotcheck.md` §5 item R66-D3).

Legs (each prints `NAME PASS|FAIL detail`):
  STAMP    `git rev-parse main` == --lands (evaluated == stamped)
  SELFTEST the tool's own --selftest exits 0 and prints `14/14`
  DIFF     the tool file is new versus BASE (`git diff BASE -- <tool>`
           non-empty on the added-file side)
  OPTIONS  --help lists --lands, --topo, --selftest
  LANDS    a materialized fixture repo whose main moved past lands still
           evaluates the receipt at --lands (committed bytes), FAILs on the
           absent receipt, and reports moved_past=True
  TOPO     the healthy fixture (receipts carried by B, stamped A) exits 0;
           the wrong-parent fixture exits 1 with parent= named
  HEADERS  a receipt missing stamped/evaluated/tree exits 1 naming
           missing_headers; stamped != evaluated exits 1 naming equal=False
  MUT      every byte-mutant under .ufo/waves/round-67/stage/mut-o/ kills its
           pinned selftest check (each mutant's expected check list is
           committed in this counter)
  R66      re-derivation: the r66 receipts at tip (final-measures-{c,o,ca})
           have carrier 4589ebdd whose parent equals each receipt's stamped
           `measured revision` 65fe8572 — the exact predicate the frozen
           D2 leg could not evaluate at lands time now runs green

Output ends `ACCEPT-O-67: PASS|FAIL`; exit 0/1, or 2 on unusable input.
"""

import argparse
import hashlib
import os
import re
import subprocess
import sys
import tempfile
import time

BASE = "ad5b52b0ab5691358cd38718ab75649dc9916f9a"
TOOL = "tools/check-receipt-seq.py"
MUT_DIR = ".ufo/waves/round-67/stage/mut-o"
R66_RECEIPTS = [
    "reports/round-66/telemetry/final-measures-c.txt",
    "reports/round-66/telemetry/final-measures-o.txt",
    "reports/round-66/telemetry/final-measures-ca.txt",
]
R66_STAMP = "65fe8572822ef83f1750593af77daddf34a1e337"
R66_CARRIER = "4589ebdd36659060a978d0bb5b41b8c4e275a549"

# mutant -> selftest check names that MUST print FAIL (and the run exits 1).
# Each mutant kills exactly the pinned behavior; nothing else may fail.
MUT_EXPECT = {
    "mut1_equality_always_true.py": ["moved-receipt-fail"],
    "mut2_parent_always_true.py": ["topo-wrong-parent-fail"],
    "mut3_missing_headers_ok.py": ["missing-headers-fail"],
    "mut4_no_carrier_pass.py": ["topo-no-carrier-fail"],
    "mut5_tree_unchecked.py": ["tree-mismatch-fail"],
}


def git(root, *args, check=True):
    env = dict(os.environ)
    env.update({
        "GIT_CONFIG_GLOBAL": os.devnull, "GIT_CONFIG_NOSYSTEM": "1",
        "GIT_AUTHOR_NAME": "fixture", "GIT_AUTHOR_EMAIL": "fixture@invalid",
        "GIT_COMMITTER_NAME": "fixture", "GIT_COMMITTER_EMAIL": "fixture@invalid",
    })
    proc = subprocess.run(["git", "-C", root, *args], env=env,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if check and proc.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)}: {proc.stderr.strip()}")
    return proc


def w(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(content)


def run_tool(tool_abs, root, argv):
    proc = subprocess.run([sys.executable, "-B", tool_abs, "--root", root]
                          + argv, stdout=subprocess.PIPE,
                          stderr=subprocess.STDOUT, text=True)
    return proc.returncode, proc.stdout


def fixture_healthy(root):
    """Lands A (counter) then records B (receipt stamped/evaluated A)."""
    os.makedirs(root, exist_ok=True)
    git(root, "init", "-q", "-b", "main")
    git(root, "config", "user.name", "f")
    git(root, "config", "user.email", "f@i")
    w(os.path.join(root, "tools/x.py"), "print('x')\n")
    git(root, "add", "-A")
    git(root, "commit", "-q", "-m", "lands")
    lands = git(root, "rev-parse", "HEAD").stdout.strip()
    tree = git(root, "rev-parse", "HEAD^{tree}").stdout.strip()
    sha = hashlib.sha256(open(os.path.join(root, "tools/x.py"), "rb").read()).hexdigest()
    w(os.path.join(root, "telemetry/r.txt"),
      "# counter sha256 (self): " + sha + "\n"
      "# stamped revision: " + lands + "\n"
      "# evaluated revision: " + lands + "\n"
      "# measured revision (lane main): " + lands + "\n"
      "# tree: " + tree + "\nok\n")
    git(root, "add", "-A")
    git(root, "commit", "-q", "-m", "records")
    return lands


def _run():
    t_start = time.monotonic()
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
        print("ACCEPT-O-67: FAIL")
        return 2
    mv = subprocess.run(["git", "-C", root, "rev-parse", "main"], stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE)
    mv_rev = mv.stdout.decode().strip()
    tree_p = subprocess.run(["git", "-C", root, "rev-parse", f"{lands}^{{tree}}"],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    tree_rev = tree_p.stdout.decode().strip()
    dirty = subprocess.run(["git", "-C", root, "status", "--porcelain",
                            "--untracked-files=no"],
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    dirty_flag = bool(dirty.stdout.decode().strip())
    print(f"# counter sha256 (self): {self_sha}")
    print(f"# stamped revision: {lands}")
    print(f"# evaluated revision: {mv_rev or 'unresolvable'}")
    print(f"# measured revision (lane main): {mv_rev or 'unresolvable'}")
    print(f"# tree: {tree_rev or 'unresolvable'}")
    print(f"# worktree dirty (tracked): {dirty_flag}")
    legs = []

    def leg(name, ok, detail):
        legs.append(bool(ok))
        print(f"{name} {'PASS' if ok else 'FAIL'} {detail}")

    stamp_ok = bool(re.fullmatch(r"[0-9a-f]{40}", mv_rev)) \
        and mv_rev == lands and bool(re.fullmatch(r"[0-9a-f]{40}", tree_rev))
    leg("STAMP", stamp_ok,
        f"stamped={lands[:8]} evaluated={mv_rev[:8]} "
        f"equal={mv_rev == lands} tree={tree_rev[:8]} "
        f"dirty_tracked={dirty_flag}")
    if not stamp_ok:
        print("ACCEPT-O-67: FAIL")
        return 1

    tool_abs = os.path.join(root, TOOL)

    # ---------- SELFTEST ----------
    st = run_tool(tool_abs, root, ["--selftest"])
    leg("SELFTEST", st[0] == 0 and "14/14" in st[1],
        f"exit={st[0]} count={'14/14' in st[1]}")

    # ---------- DIFF ----------
    d = subprocess.run(["git", "-C", root, "diff", "--name-status", BASE,
                        "--", TOOL], stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE, text=True)
    leg("DIFF", d.returncode == 0 and bool(d.stdout.strip()),
        f"diff_lines={len(d.stdout.strip().splitlines())} "
        f"status={d.stdout.split(chr(9))[0] if d.stdout.strip() else 'none'}")

    # ---------- OPTIONS ----------
    h = subprocess.run([sys.executable, "-B", tool_abs, "--help"], cwd=root,
                       stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                       text=True)
    missing = [o for o in ("--lands", "--topo", "--selftest")
               if o not in h.stdout]
    leg("OPTIONS", h.returncode == 0 and not missing, f"missing={missing}")

    # ---------- fixture lanes ----------
    fixtures_built = 0
    with tempfile.TemporaryDirectory(prefix="r67-o-") as td:
        f1 = os.path.join(td, "healthy")
        f1_lands = fixture_healthy(f1)
        fixtures_built += 1
        # ---------- LANDS ----------
        # evaluate the healthy lane at its lands revision: receipt absent at
        # lands -> FAIL unreadable; moved_past must be reported True.
        rc, out = run_tool(tool_abs, f1, ["--lands", f1_lands,
                                          "telemetry/r.txt"])
        lands_ok = (rc == 1 and "unreadable" in out
                    and "moved_past=True" in out)
        leg("LANDS", lands_ok, f"exit={rc} moved_flag={'moved_past=True' in out}")
        # ---------- TOPO ----------
        rc1, out1 = run_tool(tool_abs, f1, ["--topo", "telemetry/r.txt",
                                            "tools/x.py"])
        # wrong-parent fixture: stamp to the base-side ancestor
        base_anc = git(f1, "rev-parse", "HEAD^").stdout.strip()
        tree_a = git(f1, "rev-parse", "HEAD^{tree}").stdout.strip()
        sha_a = hashlib.sha256(open(os.path.join(f1, "tools/x.py"), "rb").read()).hexdigest()
        w(os.path.join(f1, "telemetry/wrong.txt"),
          "# counter sha256 (self): " + sha_a + "\n"
          "# stamped revision: " + base_anc + "\n"
          "# evaluated revision: " + base_anc + "\n"
          "# measured revision (lane main): " + base_anc + "\n"
          "# tree: " + tree_a + "\n")
        git(f1, "add", "telemetry/wrong.txt")
        git(f1, "commit", "-q", "-m", "wrong parent receipt")
        fixtures_built += 1
        rc2, out2 = run_tool(tool_abs, f1, ["--topo", "telemetry/wrong.txt"])
        topo_ok = (rc1 == 0 and "RECEIPT-SEQ: PASS" in out1
                   and rc2 == 1 and "TOPO-telemetry/wrong.txt FAIL" in out2
                   and "parent=" in out2)
        leg("TOPO", topo_ok,
            f"healthy={rc1} wrong={rc2}")
        # ---------- HEADERS ----------
        w(os.path.join(f1, "telemetry/bare.txt"), "no headers\n")
        rc3, out3 = run_tool(tool_abs, f1, ["telemetry/bare.txt"])
        moved_txt = ("# counter sha256 (self): " + sha_a + "\n"
                     "# stamped revision: " + base_anc + "\n"
                     "# evaluated revision: "
                     + git(f1, "rev-parse", "HEAD").stdout.strip() + "\n"
                     "# measured revision (lane main): " + base_anc + "\n"
                     "# tree: " + tree_a + "\n")
        w(os.path.join(f1, "telemetry/moved.txt"), moved_txt)
        rc4, out4 = run_tool(tool_abs, f1, ["telemetry/moved.txt"])
        headers_ok = (rc3 == 1 and "missing_headers" in out3
                      and rc4 == 1 and "equal=False" in out4)
        leg("HEADERS", headers_ok, f"bare={rc3} moved={rc4}")

    # ---------- MUT ----------
    mut_dir = os.path.join(root, MUT_DIR)
    mut_bad, mut_count = [], 0
    if os.path.isdir(mut_dir):
        for fname in sorted(os.listdir(mut_dir)):
            if not fname.endswith(".py"):
                continue
            mut_count += 1
            expected = MUT_EXPECT.get(fname)
            if expected is None:
                mut_bad.append(f"{fname}:unregistered")
                continue
            mp = os.path.join(mut_dir, fname)
            rc, out = run_tool(mp, root, ["--selftest"])
            missing_fail = [c for c in expected
                            if not re.search(rf"FAIL\s+{re.escape(c)}\b", out)]
            extra_fail = re.findall(r"^FAIL\s+(\S+)", out, re.M)
            extra_fail = [c for c in extra_fail if c not in expected]
            if not (rc == 1 and not missing_fail and not extra_fail):
                mut_bad.append(
                    f"{fname}:rc={rc} missing={missing_fail} extra={extra_fail}")
        leg("MUT", mut_count == len(MUT_EXPECT) and not mut_bad,
            f"mutants={mut_count} bad={mut_bad[:6]}")
    else:
        leg("MUT", False, f"mutant dir absent: {mut_dir}")

    # ---------- R66 ----------
    # The predicate the r66 frozen D2 leg could not evaluate at lands time:
    # for each r66 receipt, carrier-parentage against its stamped revision.
    r66_bad = []
    for rpath in R66_RECEIPTS:
        show = subprocess.run(["git", "-C", root, "show", f"main:{rpath}"],
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                              text=True)
        if show.returncode != 0:
            r66_bad.append(f"{rpath}:absent")
            continue
        text = show.stdout
        m = re.search(r"measured revision \(lane main\): ([0-9a-f]{40})", text)
        if not m or m.group(1) != R66_STAMP:
            r66_bad.append(f"{rpath}:stamp={(m.group(1)[:8] if m else 'none')}")
            continue
        carrier = git(root, "log", "-1", "--format=%H", "main", "--", rpath,
                      check=False)
        carrier = carrier.stdout.strip()
        if carrier != R66_CARRIER:
            r66_bad.append(f"{rpath}:carrier={carrier[:8]}")
            continue
        parent = git(root, "rev-parse", f"{carrier}^").stdout.strip()
        if parent != R66_STAMP:
            r66_bad.append(f"{rpath}:parent={parent[:8]}")
    leg("R66", not r66_bad, f"bad={r66_bad[:6]} "
        f"carrier={R66_CARRIER[:8]} parent_of={R66_STAMP[:8]}")

    leg("FIXTURES", fixtures_built >= 2 and (time.monotonic() - t_start) < 240,
        f"lanes={fixtures_built} wall={time.monotonic() - t_start:.1f}s")

    verdict = all(legs)
    print(f"ACCEPT-O-67: {'PASS' if verdict else 'FAIL'}")
    return 0 if verdict else 1


def main():
    try:
        return _run()
    except (RuntimeError, OSError, subprocess.SubprocessError, ValueError,
            KeyError) as exc:
        print(f"COUNTER_FAULT infrastructure unusable: {exc!r}")
        print("ACCEPT-O-67: FAIL")
        return 2


if __name__ == "__main__":
    sys.exit(main())
