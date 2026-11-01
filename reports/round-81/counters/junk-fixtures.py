#!/usr/bin/env python3
r"""Round-81 junk-landing battery (QUALITY 26b shape, applied post-landing).

Builds seven junk landings - each on its claim's OWN lands commit (lesson
R80-M4) - and grades each with the frozen round-81 counters. Every junk
landing must FAIL on its named leg:

  JO1  reports/round-81/mutants/w2-mutants.py deleted at lands      -> GEN   (O)
  JO2  claims.json edited in the graded tree (leg list truncated)   -> FROZENCFG (O)
  JC1  tools/check-orphan-evidence.py deleted at lands              -> TOOL  (C)
  JC2  the committed red sweep receipt deleted at lands             -> RECEIPT (C)
  JD1  the ordeal entry deleted at lands                            -> ENTRY (D)
  JD2  mutant entry carrying an S-id inside a decision-table row    -> LINT  (D)
  JD3  SOURCES S902 status cell flipped mined -> queued             -> ROWS  (D)

The fixture repo is a checkout-free plumbing clone (bare init + fetch +
alternates wrapper + index edits + commit-tree): the lane tree carries
committed paths that are uncheckoutable on Windows NTFS (lesson R79-M3), and
the counters read committed bytes via git plumbing + scratch extraction only,
so no worktree is ever materialized. Writes its receipts to stdout. Everything
under --work is the caller's scratch; nothing in the lane repo is touched.
"""
import argparse
import json
import os
import shutil
import subprocess
import sys


def sh(*a, **kw):
    kw.setdefault("capture_output", True)
    return subprocess.run(list(a), **kw)


def out(r):
    return (r.stdout or b"").decode("utf-8", "replace") + \
           (r.stderr or b"").decode("utf-8", "replace")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lane", required=True)
    ap.add_argument("--lands-o", required=True, help="claim-O lands commit")
    ap.add_argument("--lands-c", required=True, help="claim-C lands commit")
    ap.add_argument("--lands", required=True, help="claim-D lands commit")
    ap.add_argument("--freeze", required=True)
    ap.add_argument("--base", required=True)
    ap.add_argument("--fleet", required=True, help="fleet repo root (claim-C counter input)")
    ap.add_argument("--work", required=True)
    args = ap.parse_args()
    lane = os.path.abspath(args.lane)
    work = os.path.abspath(args.work)
    os.makedirs(work, exist_ok=True)
    env = dict(os.environ)
    env.update({"GIT_AUTHOR_NAME": "junk", "GIT_AUTHOR_EMAIL": "junk@invalid",
                "GIT_COMMITTER_NAME": "junk", "GIT_COMMITTER_EMAIL": "junk@invalid",
                "GIT_CONFIG_GLOBAL": os.devnull, "GIT_CONFIG_NOSYSTEM": "1"})
    bare = os.path.join(work, "junk-bare")
    wrapper = os.path.join(work, "junk-repo")
    for d in (bare, wrapper):
        if os.path.exists(d):
            shutil.rmtree(d, ignore_errors=True)
    r = sh("git", "init", "-q", "--bare", bare, env=env)
    assert r.returncode == 0, out(r)
    r = sh("git", "-C", bare, "fetch", "--quiet", lane, "main", env=env)
    assert r.returncode == 0, out(r)
    r = sh("git", "init", "-q", wrapper, env=env)
    assert r.returncode == 0, out(r)
    r = sh("git", "-C", wrapper, "config", "core.protectNTFS", "false", env=env)
    assert r.returncode == 0, out(r)
    with open(os.path.join(wrapper, ".git", "objects", "info", "alternates"),
              "w", newline="") as fh:
        fh.write(os.path.join(bare, "objects") + "\n")

    def git(*a, check=True, inp=None):
        r = sh("git", "-C", wrapper, *a, env=env, input=inp)
        if check:
            assert r.returncode == 0, out(r)
        return r

    def reset_index(rev):
        git("read-tree", rev)

    def put_file(path, data):
        r = sh("git", "-C", wrapper, "hash-object", "-w", "--stdin",
               env=env, input=data)
        assert r.returncode == 0, out(r)
        blob = r.stdout.decode().strip()
        git("update-index", "--cacheinfo", "100644,%s,%s" % (blob, path))

    def remove_file(path):
        git("rm", "--cached", "--quiet", path)

    def jcommit(msg, parent):
        tree = git("write-tree").stdout.decode().strip()
        r = sh("git", "-C", wrapper, "commit-tree", tree, "-p", parent,
               env=env, input=msg.encode())
        assert r.returncode == 0, out(r)
        c = r.stdout.decode().strip()
        git("update-ref", "refs/heads/fx", c)
        return c

    def grade(counter, section, name, wantlegs, parent=None, extra=None):
        rev = jcommit(name, parent or args.lands)
        print("# ---- %s / %s ----" % (section, name))
        print("commit: %s" % rev)
        wd = os.path.join(work, "grade-" + name.replace(" ", "-")[:24])
        os.makedirs(wd, exist_ok=True)
        argv = [sys.executable, "-B", os.path.join(lane, counter),
                "--root", wrapper, "--lands", rev, "--freeze", args.freeze,
                "--work", wd]
        if extra:
            argv += extra
        p = sh(*argv)
        text = out(p)
        faillines = [ln for ln in text.splitlines() if ln.startswith("LEG FAIL")]
        verdict = [ln for ln in text.splitlines() if ln.startswith("ACCEPT-")]
        print("command: python -B %s --root <fixture-repo> --lands %s "
              "--freeze %s --work <scratch>"
              % (counter, rev[:12], args.freeze[:12]))
        for ln in faillines:
            print(ln)
        print("verdict: %s exit=%d" % (verdict[0] if verdict else "<none>",
                                       p.returncode))
        hit = [w for w in wantlegs if any(w in fl for fl in faillines)]
        print("named-legs-failed: %s (wanted %s) -> %s"
              % (hit, wantlegs, "OK" if hit and p.returncode == 1 else "MISS"))
        print("")

    gen_rel = "reports/round-81/mutants/w2-mutants.py"
    chk_rel = "tools/check-orphan-evidence.py"
    red_rel = "reports/round-81/telemetry/orphan-sweep-red.txt"
    entry_rel = "corpus/knowledge/myth-symbol/ordeal-judicial-proof-rituals.md"

    claims = git("show", "%s:reports/round-81/claims.json" % args.freeze).stdout.decode("utf-8")
    doc = json.loads(claims)
    for cl in doc["claims"]:
        for key in ("guard81", "sweep81", "entry81"):
            if key in cl:
                cl[key]["legs"] = ["FROZENCFG"]
    shrunk = json.dumps(doc, indent=1, ensure_ascii=False) + chr(10)
    assert shrunk != claims

    entry = git("show", "%s:%s" % (args.lands, entry_rel)).stdout.decode("utf-8")
    mut = entry.replace("| reach |", "| reach (S901) |")
    assert mut != entry
    reg = git("show", "%s:corpus/SOURCES.md" % args.lands).stdout.decode("utf-8")
    rows = reg.splitlines()
    hit = False
    for i, ln in enumerate(rows):
        if ln.startswith("| S902 |") and "| mined | 2026-11-01 |" in ln:
            rows[i] = ln.replace("| mined | 2026-11-01 |", "| queued | 2026-11-01 |")
            hit = True
            break
    assert hit, "S902 status cell not found"
    flipped = "\n".join(rows) + "\n"

    print("JUNK-RECEIPT round-81 claim O (accept-o81.py; each junk landing "
          "must FAIL)")
    reset_index(args.lands_o)
    remove_file(gen_rel)
    grade("reports/round-81/accept-o81.py", "junk-o", "JO1 w2 generator deleted",
          ["GEN"], parent=args.lands_o)
    reset_index(args.lands_o)
    put_file("reports/round-81/claims.json", shrunk.encode("utf-8"))
    grade("reports/round-81/accept-o81.py", "junk-o",
          "JO2 claims.json shrunk in graded tree", ["FROZENCFG"],
          parent=args.lands_o)

    print("JUNK-RECEIPT round-81 claim C (accept-c81.py; each junk landing "
          "must FAIL)")
    reset_index(args.lands_c)
    remove_file(chk_rel)
    grade("reports/round-81/accept-c81.py", "junk-c", "JC1 orphan checker deleted",
          ["TOOL"], parent=args.lands_c, extra=["--fleet", args.fleet])
    reset_index(args.lands_c)
    remove_file(red_rel)
    grade("reports/round-81/accept-c81.py", "junk-c",
          "JC2 red sweep receipt deleted", ["RECEIPT"],
          parent=args.lands_c, extra=["--fleet", args.fleet])

    print("JUNK-RECEIPT round-81 claim D (accept-d81.py; each junk landing "
          "must FAIL)")
    reset_index(args.lands)
    remove_file(entry_rel)
    grade("reports/round-81/accept-d81.py", "junk-d", "JD1 entry deleted at lands",
          ["ENTRY"])
    reset_index(args.lands)
    put_file(entry_rel, mut.encode("utf-8"))
    grade("reports/round-81/accept-d81.py", "junk-d",
          "JD2 table-row S-id mutant", ["LINT"])
    reset_index(args.lands)
    put_file("corpus/SOURCES.md", flipped.encode("utf-8"))
    grade("reports/round-81/accept-d81.py", "junk-d", "JD3 S902 status flipped",
          ["ROWS"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
