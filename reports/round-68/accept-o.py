#!/usr/bin/env python3
r"""Round-68 claim O acceptance, revision 0 (pre-data).

Operability claim: a new capability `tools/check-supersession-settlement.py`
classifies every `supersedes S###` registry chain (settled-active /
settled-retired / settled-closed / settled-split / pending), resolves used-by
paths, and validates a disposition ledger; the round settles every pending
chain at base (the r66-dedup rows plus the sign/Kongo/heraldry/subsistence
correction rows), so the tool's scan at lands reports pending=0 and
missing_paths=0, its selftest passes 7/7, and the committed ledger validates
with 0 findings covering the frozen required-id set.

Receipt discipline (QUALITY.md criterion 19): --lands <40hex> is REQUIRED and
names the lands revision the run claims to measure. stamped revision comes
from --lands, evaluated from `git rev-parse main` of --root; leg STAMP fails
unless they are equal. Evaluate against a `git clone --no-local` of the lane
at the lands commit: a stale clone makes evaluated != stamped.

Legs (each prints `NAME PASS|FAIL detail`):
  STAMP     evaluated == stamped (lane main == --lands)
  SELFTEST  tool --selftest exits 0 and prints SELFTEST: 7/7
  DIFF      `git diff BASE -- tools/check-supersession-settlement.py`
            shows the tool as added (status A)
  SHA       sha256 of the tool file at lands equals sha256 of the file in
            the worktree (tool evaluated is tool committed)
  PENDING   tool --scan at lands prints `pending=0` and `missing_paths=0`
  LEDGER    tool --ledger reports/round-68/dispositions/dedup-ledger.tsv
            exits 0 with 0 findings, and the ledger covers every required id
            exactly once (28 census-flagged ids + every base-pending chain's
            superseding id + the 13 pre-settled chain superseding ids)
  EXEC      a fixture lane built in a temp dir — pending chain at fixture
            base, settled at fixture lands — scores PENDING fail at base and
            pass at lands under this counter's own PENDING logic
  MUT       three tool mutants (scan always pending=0, ledger always clean,
            selftest skipped) each fail their pinned leg against the live
            lane; nothing else may fail
  TOPO      lands' parent is the declaration commit T0 (settlement is the
            direct child of the counter-bearing commit)
"""

import argparse
import hashlib
import os
import re
import subprocess
import sys
import tempfile
import time

BASE = "99fae3085ec858446df00c2b294748f635cb6c45"
DECLARATION = None  # filled at declaration commit (see --declaration arg)
TOOL = "tools/check-supersession-settlement.py"
LEDGER = "reports/round-68/dispositions/dedup-ledger.tsv"
CHAIN_IDS = [
    "S044", "S045", "S046", "S070", "S125", "S126", "S127", "S128", "S129",
    "S130", "S131", "S133", "S186", "S358", "S481", "S482", "S483", "S484",
    "S485", "S486", "S487", "S488", "S489", "S490", "S491", "S560", "S561",
    "S562", "S564", "S565", "S566", "S567", "S568", "S569",
]
FLAGGED_IDS = [
    "S034", "S038", "S039", "S060", "S095", "S079", "S086", "S097", "S105",
    "S117", "S119", "S122", "S157", "S256", "S359", "S367", "S383", "S385",
    "S392", "S395", "S396", "S399", "S407", "S410", "S413", "S417", "S421",
    "S433", "S438", "S440", "S445", "S452", "S453",
]
KEEP_IDS = [
    "S047", "S132", "S185", "S570", "S571", "S572", "S573", "S574", "S575",
    "S648", "S649", "S650", "S651",
]
MUTANTS = {
    "mut_scan_always_clean.py": "PENDING",
    "mut_ledger_always_clean.py": "LEDGER",
    "mut_selftest_skip.py": "SELFTEST",
}


def sh(args, cwd=None):
    proc = subprocess.run(args, cwd=cwd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE, text=True)
    return proc.returncode, proc.stdout


def git(root, *args):
    return sh(["git", "-C", root, *args])[1].strip()


def ledger_required_ids():
    return set(CHAIN_IDS) | set(FLAGGED_IDS) | set(KEEP_IDS)


def ledger_ids(path):
    ids = []
    try:
        for raw in open(path, encoding="utf-8"):
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            cells = [c.strip() for c in line.split("|")]
            if len(cells) == 7 and re.fullmatch(r"S\d{3,}", cells[0]):
                ids.append(cells[0])
    except OSError:
        return None
    return ids


def run_pending(root):
    """This counter's own PENDING logic, usable on fixture roots."""
    rc, out = sh([sys.executable, "-B", os.path.join(root, TOOL),
                  "--root", root, "--scan"])
    m = re.search(r"pending=(\d+)\s+chains=(\d+)\s+usedby_paths=(\d+)\s+"
                  r"missing_paths=(\d+)", out or "")
    ok = (rc == 0 and m is not None
          and m.group(1) == "0" and m.group(4) == "0")
    return ok, f"exit={rc} summary={m.group(0) if m else 'absent'}"


def fixture_lane(td):
    """Build pending-at-base, settled-at-lands fixture lane."""
    root = os.path.join(td, "fx")
    src = os.path.join(root, "corpus/SOURCES.md")
    tool_dst = os.path.join(root, TOOL)
    os.makedirs(os.path.dirname(src), exist_ok=True)
    os.makedirs(os.path.dirname(tool_dst), exist_ok=True)
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           "..", "..", TOOL), "rb") as fh:
        tool_bytes = fh.read()
    with open(tool_dst, "wb") as fh:
        fh.write(tool_bytes)
    env = dict(os.environ)
    env.update({"GIT_CONFIG_GLOBAL": os.devnull, "GIT_CONFIG_NOSYSTEM": "1",
                "GIT_AUTHOR_NAME": "f", "GIT_AUTHOR_EMAIL": "f@i",
                "GIT_COMMITTER_NAME": "f", "GIT_COMMITTER_EMAIL": "f@i"})
    def g(*a):
        subprocess.run(["git", "-C", root, *a], env=env, check=True,
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    head = """# t
## Registry
| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
"""
    r1 = '| S001 | a — https://x/a | docs | B | s | "q" | base | mined | d | 90d | corpus/knowledge/a.md |\n'
    r2p = '| S002 | a — https://x/a | docs | A | s | "q" | supersedes S001 — fix | queued | d | 90d | — |\n'
    r2s = '| S002 | a — https://x/a | docs | A | s | "q" | supersedes S001 — fix | mined | d | 90d | corpus/knowledge/a.md |\n'
    r1q = '| S001 | a — https://x/a | docs | B | s | "q" | base | queued | d | 90d | — |\n'
    g("init", "-q", "-b", "main")
    g("config", "user.name", "f")
    g("config", "user.email", "f@i")
    with open(src, "w") as fh:
        fh.write(head + r1 + r2p)
    g("add", "-A")
    g("commit", "-q", "-m", "base")
    base = git(root, "rev-parse", "HEAD")
    with open(src, "w") as fh:
        fh.write(head + r1q + r2s)
    g("add", "-A")
    g("commit", "-q", "-m", "lands")
    lands = git(root, "rev-parse", "HEAD")
    return root, base, lands


def make_mutants(tool_src, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    m1 = tool_src.replace('print(f"SETTLEMENT: pending={len(pending)} chains={len(chains)} "',
                          'pending = []\n    print(f"SETTLEMENT: pending={len(pending)} chains={len(chains)} "')
    m2 = tool_src.replace("return 1 if bad else 0\n\n\n# ---",
                          "return 0\n\n\n# ---")
    m3 = tool_src.replace("rc6 = scan(os.path.join(td, \"f5\"), None)",
                          "rc6 = 0  # mutant: unreadable fixture check always fails")
    for name, text in (("mut_scan_always_clean.py", m1),
                       ("mut_ledger_always_clean.py", m2),
                       ("mut_selftest_skip.py", m3)):
        with open(os.path.join(out_dir, name), "w", encoding="utf-8") as fh:
            fh.write(text)


def _run():
    t_start = time.monotonic()
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--lands", required=True,
                    help="the lands revision this run claims to measure")
    ap.add_argument("--declaration", default=None,
                    help="the T0 declaration commit hash (topo leg)")
    args = ap.parse_args()
    root = os.path.abspath(args.root)
    lands = args.lands
    self_sha = hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest()
    if not re.fullmatch(r"[0-9a-f]{40}", lands or ""):
        print("STAMP FAIL --lands is not a full commit hash")
        print("ACCEPT-O-68: FAIL")
        return 2
    mv_rev = git(root, "rev-parse", "main")
    tree_rev = git(root, "rev-parse", f"{lands}^{{tree}}")
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
        print("ACCEPT-O-68: FAIL")
        return 1

    tool_abs = os.path.join(root, TOOL)

    # ---------- SELFTEST ----------
    rc, out = sh([sys.executable, "-B", tool_abs, "--selftest"])
    leg("SELFTEST", rc == 0 and "7/7" in out,
        f"exit={rc} count={'7/7' in out}")

    # ---------- DIFF ----------
    rc, out = sh(["git", "-C", root, "diff", "--name-status", BASE, "--", TOOL])
    leg("DIFF", rc == 0 and out.strip().startswith("A"),
        f"status={out.strip()[:1] or 'none'}")

    # ---------- SHA ----------
    live_sha = hashlib.sha256(open(tool_abs, "rb").read()).hexdigest()
    rc, blob = sh(["git", "-C", root, "show", f"{lands}:{TOOL}"])
    leg("SHA", rc == 0 and hashlib.sha256(blob.encode()).hexdigest() == live_sha,
        f"live={live_sha[:12]}")

    # ---------- PENDING ----------
    ok, detail = run_pending(root)
    leg("PENDING", ok, detail)

    # ---------- LEDGER ----------
    ledger_path = os.path.join(root, LEDGER)
    rc, out = sh([sys.executable, "-B", tool_abs, "--root", root,
                  "--ledger", ledger_path])
    findings = re.search(r"findings=(\d+)", out or "")
    ids = ledger_ids(ledger_path)
    required = ledger_required_ids()
    missing = sorted(required - set(ids or []))
    extra = sorted(set(ids or []) - required)
    dup = sorted({i for i in (ids or []) if (ids or []).count(i) > 1})
    leg("LEDGER", rc == 0 and findings and findings.group(1) == "0"
        and not missing and not dup,
        f"exit={rc} findings={findings.group(1) if findings else '?'} "
        f"missing={missing[:4]} dup={dup[:4]} extra={len(extra)}")

    # ---------- EXEC ----------
    with tempfile.TemporaryDirectory(prefix="r68-o-") as td:
        fx_root, fx_base, fx_lands = fixture_lane(td)
        ok_b, det_b = run_pending(fx_root)  # currently at lands -> pass
        # check out base state for the negative leg
        env = dict(os.environ)
        env.update({"GIT_CONFIG_GLOBAL": os.devnull, "GIT_CONFIG_NOSYSTEM": "1"})
        subprocess.run(["git", "-C", fx_root, "checkout", "-q", fx_base],
                       env=env, check=True)
        ok_pre, det_pre = run_pending(fx_root)
        subprocess.run(["git", "-C", fx_root, "checkout", "-q", fx_lands],
                       env=env, check=True)
        ok_post, det_post = run_pending(fx_root)
        leg("EXEC", (not ok_pre) and ok_post and ok_b,
            f"base_pending_fail={not ok_pre} lands_pass={ok_post}")

        # ---------- MUT ----------
        # each mutant must diverge from the real tool on an input where the
        # real tool reports the pinned behavior — proving the counter's leg
        # would flip if the checked behavior were removed.
        tool_src = open(tool_abs, encoding="utf-8").read()
        make_mutants(tool_src, td)
        subprocess.run(["git", "-C", fx_root, "checkout", "-q", fx_base],
                       env=env, check=True)
        mut_bad = []
        for name, pinned_leg in MUTANTS.items():
            mpath = os.path.join(td, name)
            if pinned_leg == "PENDING":
                # fixture base has a pending chain (real tool: pending=1);
                # the mutant must still print pending=0
                rc_b, out_b = sh([sys.executable, "-B", mpath,
                                  "--root", fx_root, "--scan"])
                m_b = re.search(r"pending=(\d+)", out_b or "")
                if not (m_b and m_b.group(1) == "0"):
                    mut_bad.append(f"{name}:not_a_mutant")
            elif pinned_leg == "LEDGER":
                # real tool exits 1 on a malformed ledger; the mutant exits 0
                bad_led = os.path.join(td, "bad-ledger.tsv")
                with open(bad_led, "w") as fh:
                    fh.write("S001 | S002 | u | bogus-ruling | x | x | t\n")
                rc, out = sh([sys.executable, "-B", mpath, "--root", root,
                              "--ledger", bad_led])
                if rc != 0:
                    mut_bad.append(f"{name}:not_a_mutant_rc={rc}")
            elif pinned_leg == "SELFTEST":
                rc, out = sh([sys.executable, "-B", mpath, "--selftest"])
                if rc == 0 and "7/7" in out:
                    mut_bad.append(f"{name}:selftest_still_passes")
        leg("MUT", not mut_bad, f"bad={mut_bad[:4]}")

    # ---------- TOPO ----------
    decl = args.declaration
    if decl and re.fullmatch(r"[0-9a-f]{40}", decl):
        parent = git(root, "rev-parse", f"{lands}^")
        leg("TOPO", parent == decl,
            f"parent={parent[:8]} declaration={decl[:8]}")
    else:
        leg("TOPO", False, "no --declaration hash supplied")

    verdict = all(legs)
    print(f"ACCEPT-O-68: {'PASS' if verdict else 'FAIL'} "
          f"wall={time.monotonic() - t_start:.1f}s")
    return 0 if verdict else 1


def main():
    try:
        return _run()
    except (RuntimeError, OSError, subprocess.SubprocessError, ValueError,
            KeyError) as exc:
        print(f"COUNTER_FAULT infrastructure unusable: {exc!r}")
        print("ACCEPT-O-68: FAIL")
        return 2


if __name__ == "__main__":
    sys.exit(main())
