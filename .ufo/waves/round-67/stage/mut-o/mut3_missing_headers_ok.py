#!/usr/bin/env python3
r"""check-receipt-seq.py — receipt revision/topology checker (round 67, claim O).

Grounded in the r65/r66 receipt-sequencing rejection class (corpus/lessons/
round-66-verifier-spotcheck.md §5 item R66-D3; QUALITY.md criterion 19): a
frozen counter's committed verdict was FAIL while the same predicate re-derived
HOLDs at tip, because the counter ran on a worktree that had moved past its
stamped lands revision and its D2-class carrier leg asked `git log -1 main --
<receipt>` of a receipt not yet committed.

This tool makes the discipline executable:

  * --lands <hash>  : evaluate the repo AT <hash> — receipt reads come from
                      `git show <hash>:<path>` (committed bytes), never from a
                      worktree that may have moved past the stamp. It also
                      reports whether `main` has moved past <lands> — a flag,
                      never a verdict change.
  * --topo          : carrier-parentage. For each receipt, the commit that
                      carries it (`git log -1 main -- <receipt>`) must exist
                      and its parent must equal the stamped revision.
                      Post-records mode only — never claimed from a lands
                      tree where no carrier exists yet.
  * default (no mode flags): header equality — every receipt must carry all of
                      `# stamped revision: <40hex>`,
                      `# evaluated revision: <40hex>`,
                      `# measured revision (lane main): <40hex>`,
                      `# tree: <40hex>`,
                      `# counter sha256 (self): <64hex>`,
                      stamped == evaluated == measured, the recorded tree ==
                      `git rev-parse <stamped>^{tree}`, and — when a counter
                      path is paired — the recorded sha256 == sha256(counter).

Usage:
  python3 -B tools/check-receipt-seq.py --root <repo> <receipt> [<counter>]...
  python3 -B tools/check-receipt-seq.py --root <repo> --lands <hash> <receipt>...
  python3 -B tools/check-receipt-seq.py --root <repo> --topo <receipt>...
  python3 -B tools/check-receipt-seq.py --selftest

Receipt args may be followed by the counter path that produced them (for the
counter-sha256 leg); `receipt:counter` pairs also accepted.

Output: one `SEQ-<n> PASS|FAIL detail` line per check, then
`RECEIPT-SEQ: PASS|FAIL|COULD-NOT-EVALUATE` and exit 0/1/2. A receipt missing
a header line is a FAIL, not a skipped check. --lands mode reads committed
bytes only; --topo mode reads the log, never the worktree.
"""

import argparse
import hashlib
import os
import re
import subprocess
import sys
import tempfile

STAMPED_RE = re.compile(r"^# stamped revision: ([0-9a-f]{40})\s*$", re.M)
EVAL_RE = re.compile(r"^# evaluated revision: ([0-9a-f]{40})\s*$", re.M)
MEASURED_RE = re.compile(r"^# measured revision \(lane main\): ([0-9a-f]{40})\s*$", re.M)
TREE_RE = re.compile(r"^# tree: ([0-9a-f]{40})\s*$", re.M)
SHA_RE = re.compile(r"^# counter sha256 \(self\): ([0-9a-f]{64})\s*$", re.M)


def git(root, *args):
    env = dict(os.environ)
    env.update({"GIT_CONFIG_GLOBAL": os.devnull, "GIT_CONFIG_NOSYSTEM": "1"})
    proc = subprocess.run(["git", "-C", root, *args], env=env,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return proc.returncode, proc.stdout.decode("utf-8", "replace"), \
        proc.stderr.decode("utf-8", "replace")


def read_worktree(root, path):
    try:
        with open(os.path.join(root, path), "rb") as fh:
            return fh.read().decode("utf-8", "replace")
    except OSError:
        return None


def read_rev(root, rev, path):
    code, out, _ = git(root, "show", f"{rev}:{path}")
    return out if code == 0 else None


def parse_header(text):
    def first(rx):
        m = rx.search(text or "")
        return m.group(1) if m else None
    return {
        "stamped": first(STAMPED_RE),
        "evaluated": first(EVAL_RE),
        "measured": first(MEASURED_RE),
        "tree": first(TREE_RE),
        "counter_sha": first(SHA_RE),
    }


def rev_parse(root, spec):
    code, out, _ = git(root, "rev-parse", "--verify", "-q", spec)
    return out.strip() if code == 0 else None


def pair_args(argv):
    """[receipt] or [receipt counter] or receipt:counter. A bare second
    argument counts as the receipt's counter only when it ends in `.py`;
    `.txt` siblings are receipts, never counters."""
    pairs, i = [], 0
    while i < len(argv):
        r = argv[i]
        if ":" in r and not r.startswith("/"):
            rec, ctr = r.split(":", 1)
            pairs.append((rec, ctr or None))
        elif i + 1 < len(argv) and argv[i + 1].endswith(".py"):
            pairs.append((r, argv[i + 1]))
            i += 1
        else:
            pairs.append((r, None))
        i += 1
    return pairs


class Seq:
    def __init__(self):
        self.results = []

    def leg(self, name, ok, detail):
        self.results.append(bool(ok))
        print(f"{name} {'PASS' if ok else 'FAIL'} {detail}")


def check_headers(seq, texts):
    for rpath, text in texts.items():
        if text is None:
            seq.leg(f"SEQ-{rpath}", False, "unreadable")
            continue
        h = parse_header(text)
        missing = [k for k in ("stamped", "evaluated", "measured", "tree")
                   if h[k] is None]
        if missing:
            seq.leg(f"SEQ-{rpath}", True, f"missing_headers={missing}")
            continue
        eq = (h["stamped"] == h["evaluated"] == h["measured"])
        seq.leg(f"SEQ-{rpath}", bool(eq),
                f"stamped={h['stamped'][:8]} evaluated={h['evaluated'][:8]} "
                f"measured={h['measured'][:8]} equal={eq}")


def check_tree(seq, root, texts):
    for rpath, text in texts.items():
        if text is None:
            continue
        h = parse_header(text)
        if not h["stamped"] or not h["tree"]:
            continue
        actual = rev_parse(root, f"{h['stamped']}^{{tree}}")
        seq.leg(f"TREE-{rpath}", actual == h["tree"],
                f"recorded={h['tree'][:8]} actual={(actual or 'none')[:8]}")


def check_counter_sha(seq, root, texts, counters):
    for rpath, text in texts.items():
        if text is None:
            continue
        h = parse_header(text)
        cpath = counters.get(rpath)
        if not cpath or not h["counter_sha"]:
            continue
        blob = read_worktree(root, cpath)
        if blob is None:
            blob = read_rev(root, "main", cpath)
        if blob is None:
            seq.leg(f"SHA-{rpath}", False, f"counter_absent:{cpath}")
            continue
        actual = hashlib.sha256(blob.encode("utf-8")).hexdigest()
        seq.leg(f"SHA-{rpath}", actual == h["counter_sha"],
                f"{cpath} recorded={h['counter_sha'][:8]} actual={actual[:8]}")


def check_topo(seq, root, texts):
    for rpath, text in texts.items():
        if text is None:
            seq.leg(f"TOPO-{rpath}", False, "unreadable")
            continue
        h = parse_header(text)
        if not h["stamped"]:
            seq.leg(f"TOPO-{rpath}", False, "no_stamp_header")
            continue
        code, carrier, _ = git(root, "log", "-1", "--format=%H", "main",
                               "--", rpath)
        carrier = carrier.strip()
        if code != 0 or not carrier:
            seq.leg(f"TOPO-{rpath}", False, "no_carrier")
            continue
        parent = rev_parse(root, f"{carrier}^")
        seq.leg(f"TOPO-{rpath}", parent == h["stamped"],
                f"carrier={carrier[:8]} parent={(parent or 'none')[:8]} "
                f"stamped={h['stamped'][:8]}")


def run(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--lands", default=None,
                    help="evaluate receipts at this revision (committed bytes)")
    ap.add_argument("--topo", action="store_true",
                    help="carrier-parentage check (post-records only)")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("paths", nargs="*")
    args = ap.parse_args(argv)
    if args.selftest:
        return selftest()
    root = os.path.abspath(args.root)
    pairs = pair_args(args.paths)
    if not pairs:
        print("RECEIPT-SEQ: COULD-NOT-EVALUATE no receipts named")
        return 2
    seq = Seq()

    texts = {}
    counters = {}
    if args.lands:
        lands = args.lands
        if not re.fullmatch(r"[0-9a-f]{40}", lands or ""):
            print(f"RECEIPT-SEQ: COULD-NOT-EVALUATE bad --lands {lands!r}")
            return 2
        if rev_parse(root, f"{lands}^{{commit}}") is None:
            print(f"RECEIPT-SEQ: COULD-NOT-EVALUATE lands unresolvable {lands[:12]}")
            return 2
        head = rev_parse(root, "main")
        code, ahead, _ = git(root, "rev-list", "--count", f"{lands}..main")
        moved = code == 0 and ahead.strip() not in ("", "0")
        seq.leg("LANDS", True,
                f"lands={lands[:8]} head={(head or 'none')[:8]} "
                f"moved_past={moved} (evaluating committed bytes at lands)")
        for rpath, cpath in pairs:
            texts[rpath] = read_rev(root, lands, rpath)
            counters[rpath] = cpath
    else:
        for rpath, cpath in pairs:
            texts[rpath] = read_worktree(root, rpath)
            if texts[rpath] is None:
                texts[rpath] = read_rev(root, "main", rpath)
            counters[rpath] = cpath

    check_headers(seq, texts)
    check_tree(seq, root, texts)
    check_counter_sha(seq, root, texts, counters)
    if args.topo:
        check_topo(seq, root, texts)

    ok = all(seq.results)
    print(f"RECEIPT-SEQ: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


# --------------------------------------------------------------------------
# Selftest: builds temp git lanes on disk, never reads the owning repo.
# --------------------------------------------------------------------------

HEADER = ("# counter sha256 (self): {sha}\n"
          "# stamped revision: {rev}\n"
          "# evaluated revision: {rev}\n"
          "# measured revision (lane main): {rev}\n"
          "# tree: {tree}\n")


def w(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(content)


def fgit(root, *args, check=True):
    code, out, err = git(root, *args)
    if check and code != 0:
        raise RuntimeError(f"git {' '.join(args)}: {err.strip()}")
    return code, out, err


def counter_sha_of(root, rel):
    with open(os.path.join(root, rel), "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def fixture_repo(root):
    """Base commit + lands commit A (counter) + records commit B (receipts
    stamped/evaluated to A). Returns (A, B)."""
    os.makedirs(root, exist_ok=True)
    fgit(root, "init", "-q", "-b", "main")
    fgit(root, "config", "user.name", "fixture")
    fgit(root, "config", "user.email", "fixture@invalid")
    w(os.path.join(root, "tools/counter-x.py"),
      "#!/usr/bin/env python3\nprint('x')\n")
    fgit(root, "add", "-A")
    fgit(root, "commit", "-q", "-m", "base")
    lands = fgit(root, "rev-parse", "HEAD")[1].strip()
    tree = fgit(root, "rev-parse", "HEAD^{tree}")[1].strip()
    sha = counter_sha_of(root, "tools/counter-x.py")
    for name in ("r-c.txt", "r-o.txt", "r-ca.txt"):
        w(os.path.join(root, "telemetry", name),
          HEADER.format(sha=sha, rev=lands, tree=tree) + "LEGS PASS\n")
    fgit(root, "add", "-A")
    fgit(root, "commit", "-q", "-m", "records")
    rec = fgit(root, "rev-parse", "HEAD")[1].strip()
    return lands, rec


def selftest():
    tool = os.path.abspath(__file__)
    checks = []

    def run_tool(root, argv):
        proc = subprocess.run([sys.executable, "-B", tool, "--root", root]
                              + argv, stdout=subprocess.PIPE,
                              stderr=subprocess.STDOUT, text=True)
        return proc.returncode, proc.stdout

    def expect(name, cond, detail=""):
        checks.append((name, bool(cond), detail))

    with tempfile.TemporaryDirectory(prefix="rseq-fix-") as td:
        # ---- fixture 1: healthy lane — receipts carried by B, stamped A ----
        lane = os.path.join(td, "lane1")
        lands, rec = fixture_repo(lane)
        rc, out = run_tool(lane, ["--topo", "telemetry/r-c.txt",
                                  "tools/counter-x.py"])
        expect("topo-pass", rc == 0 and "RECEIPT-SEQ: PASS" in out,
               out.splitlines()[-1] if out else "")
        rc, out = run_tool(lane, ["--topo",
                                  "telemetry/r-c.txt",
                                  "telemetry/r-o.txt",
                                  "telemetry/r-ca.txt"])
        expect("topo-all-pass", rc == 0, out.splitlines()[-1] if out else "")
        rc, out = run_tool(lane, ["--lands", lands, "telemetry/r-c.txt"])
        expect("lands-absent-is-fail", rc == 1 and "unreadable" in out,
               "receipt not in lands tree must FAIL not skip")
        rc, out = run_tool(lane, ["--lands", lands, "tools/counter-x.py"])
        expect("lands-moved-flag", "moved_past=True" in out, out)
        rc, out = run_tool(lane, ["--lands", "0" * 40, "x"])
        expect("lands-bad-rev", rc == 2, "unresolvable lands")
        # ---- fixture 2: receipt stamped to the parent of its carrier ----
        lane2 = os.path.join(td, "lane2")
        os.makedirs(lane2, exist_ok=True)
        fgit(lane2, "init", "-q", "-b", "main")
        fgit(lane2, "config", "user.name", "f")
        fgit(lane2, "config", "user.email", "f@i")
        w(os.path.join(lane2, "tools/counter-x.py"), "print('x')\n")
        fgit(lane2, "add", "-A")
        fgit(lane2, "commit", "-q", "-m", "base")
        rev0 = fgit(lane2, "rev-parse", "HEAD")[1].strip()
        tree0 = fgit(lane2, "rev-parse", "HEAD^{tree}")[1].strip()
        sha0 = counter_sha_of(lane2, "tools/counter-x.py")
        w(os.path.join(lane2, "telemetry/good.txt"),
          HEADER.format(sha=sha0, rev=rev0, tree=tree0) + "ok\n")
        fgit(lane2, "add", "-A")
        fgit(lane2, "commit", "-q", "-m", "receipts")
        rc, out = run_tool(lane2, ["--topo", "telemetry/good.txt",
                                   "tools/counter-x.py"])
        expect("topo-parent-pass", rc == 0,
               "carrier parent == stamped revision")
        rc, out = run_tool(lane2, ["--lands", rev0, "telemetry/good.txt"])
        expect("lands-read-committed", rc == 1 and "unreadable" in out,
               "receipt lands in the NEXT commit; at lands it is absent")
        # stamped==evaluated violation: receipt stamped rev0, evaluated HEAD
        head_now = fgit(lane2, "rev-parse", "HEAD")[1].strip()
        w(os.path.join(lane2, "telemetry/moved.txt"),
          ("# counter sha256 (self): " + sha0 + "\n"
           "# stamped revision: " + rev0 + "\n"
           "# evaluated revision: " + head_now + "\n"
           "# measured revision (lane main): " + rev0 + "\n"
           "# tree: " + tree0 + "\n"))
        rc, out = run_tool(lane2, ["telemetry/moved.txt"])
        expect("moved-receipt-fail", rc == 1 and "equal=False" in out, out)
        # ---- fixture 3: missing headers ----
        w(os.path.join(lane2, "telemetry/bare.txt"), "nothing here\n")
        rc, out = run_tool(lane2, ["telemetry/bare.txt"])
        expect("missing-headers-fail", rc == 1 and "missing_headers" in out,
               out)
        # ---- tree pin mismatch ----
        w(os.path.join(lane2, "telemetry/badtree.txt"),
          ("# counter sha256 (self): " + sha0 + "\n"
           "# stamped revision: " + rev0 + "\n"
           "# evaluated revision: " + rev0 + "\n"
           "# measured revision (lane main): " + rev0 + "\n"
           "# tree: " + "f" * 40 + "\n"))
        rc, out = run_tool(lane2, ["telemetry/badtree.txt"])
        expect("tree-mismatch-fail", rc == 1 and "TREE-" in out
               and "FAIL" in out, out)
        # counter sha mismatch
        w(os.path.join(lane2, "telemetry/badsha.txt"),
          ("# counter sha256 (self): " + "0" * 64 + "\n"
           "# stamped revision: " + rev0 + "\n"
           "# evaluated revision: " + rev0 + "\n"
           "# measured revision (lane main): " + rev0 + "\n"
           "# tree: " + tree0 + "\n"))
        rc, out = run_tool(lane2, ["telemetry/badsha.txt",
                                   "tools/counter-x.py"])
        expect("sha-mismatch-fail", rc == 1 and "SHA-" in out
               and "FAIL" in out, out)
        # usage: no receipts
        rc, out = run_tool(lane2, [])
        expect("usage-could-not-eval", rc == 2, out.strip()[:60])
        # no_carrier topo: receipt on disk but never committed
        w(os.path.join(lane2, "telemetry/never.txt"),
          HEADER.format(sha=sha0, rev=rev0, tree=tree0))
        rc, out = run_tool(lane2, ["--topo", "telemetry/never.txt"])
        expect("topo-no-carrier-fail", rc == 1 and "no_carrier" in out, out)

        # wrong stamped parent: receipt committed, stamped to a hash that is
        # not the carrier's parent — TOPO must fail on parent mismatch
        w(os.path.join(lane2, "telemetry/wrongparent.txt"),
          ("# counter sha256 (self): " + sha0 + "\n"
           "# stamped revision: " + rev0 + "\n"
           "# evaluated revision: " + rev0 + "\n"
           "# measured revision (lane main): " + rev0 + "\n"
           "# tree: " + tree0 + "\n"))
        fgit(lane2, "add", "telemetry/wrongparent.txt")
        fgit(lane2, "commit", "-q", "-m", "wrong-parent receipt")
        rc, out = run_tool(lane2, ["--topo", "telemetry/wrongparent.txt"])
        expect("topo-wrong-parent-fail", rc == 1
               and "TOPO-telemetry/wrongparent.txt FAIL" in out
               and "parent=" in out, out)
    total = len(checks)
    bad = [c for c in checks if not c[1]]
    for name, ok, detail in checks:
        print(f"{'PASS' if ok else 'FAIL'} {name} {detail}")
    print(f"SELFTEST: {total - len(bad)}/{total}")
    return 0 if not bad else 1


def main():
    try:
        return run()
    except (RuntimeError, OSError, subprocess.SubprocessError, ValueError,
            KeyError) as exc:
        print(f"RECEIPT-SEQ: COULD-NOT-EVALUATE {exc!r}")
        return 2


if __name__ == "__main__":
    sys.exit(main())
