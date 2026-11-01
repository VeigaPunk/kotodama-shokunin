#!/usr/bin/env python3
r"""Round-80 junk-landing battery (QUALITY 26b shape, applied post-landing).

Builds six junk landings on top of the claim-D lands commit and grades each
with the frozen round-80 counters. Every junk landing must FAIL on its named
leg:

  JO1  tools/ledger-token-guard.py replaced by the r79 (unhardened) bytes -> TOOL
  JO2  hardened tool with the replace-ref refusal removed (m1 mutant)      -> TOOL+REPLACE
  JO3  claims.json edited in the graded tree (leg list truncated)          -> FROZENCFG
  JD1  the maritime entry deleted at lands                                 -> ENTRY
  JD2  mutant entry carrying an S-id inside a table row                    -> LINT (TABLE-ID)
  JD3  SOURCES S899 status cell flipped mined -> queued                    -> ROWS

The fixture repo is a checkout-free plumbing clone (bare init + fetch +
alternates wrapper + index edits + commit-tree): the lane tree carries
committed paths that are uncheckoutable on Windows NTFS (lesson R79-M3),
and the counters read committed bytes via git plumbing only, so no worktree
is ever materialized. Writes its receipts to stdout. Everything under --work
is the caller's scratch; nothing in the lane repo is touched.
"""

import argparse
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
    ap.add_argument("--lands", required=True, help="claim-D lands commit (D junk builds on it)")
    ap.add_argument("--lands-o", required=True, help="claim-O lands commit (O junk builds on it)")
    ap.add_argument("--freeze", required=True)
    ap.add_argument("--base", required=True)
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
    # a bare clone materializes no worktree, so the NTFS-uncheckoutable
    # committed paths (lesson R79-M3) never block the battery
    r = sh("git", "-C", bare, "fetch", "--quiet", lane, "main", env=env)
    assert r.returncode == 0, out(r)
    # wrapper repo shares the bare store through alternates and is never
    # checked out; the counters only need plumbing reads plus an index
    r = sh("git", "init", "-q", wrapper, env=env)
    assert r.returncode == 0, out(r)
    # the wrapper never checks out, and its index must be allowed to carry
    # the lane's NTFS-uncheckoutable committed paths (lesson R79-M3)
    r = sh("git", "-C", wrapper, "config", "core.protectNTFS", "false", env=env)
    assert r.returncode == 0, out(r)
    with open(os.path.join(wrapper, ".git", "objects", "info", "alternates"),
              "w", newline="") as fh:
        fh.write(os.path.join(bare, "objects") + "\n")
    r = sh("git", "-C", wrapper, "update-ref", "refs/heads/main", args.lands,
           env=env)
    assert r.returncode == 0, out(r)

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

    def grade(counter, section, name, wantlegs, parent=None):
        rev = jcommit(name, parent or args.lands)
        print("# ---- %s / %s ----" % (section, name))
        print("commit: %s" % rev)
        wd = os.path.join(work, "grade-" + name.replace(" ", "-")[:24])
        os.makedirs(wd, exist_ok=True)
        p = sh(sys.executable, "-B", os.path.join(lane, counter),
               "--root", wrapper, "--lands", rev, "--freeze", args.freeze,
               "--work", wd)
        text = out(p)
        faillines = [ln for ln in text.splitlines()
                     if ln.startswith("LEG FAIL")]
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

    old_tool = git("show", "%s:tools/ledger-token-guard.py" % args.base).stdout
    cur_tool = git("show", "%s:tools/ledger-token-guard.py"
                   % args.lands).stdout
    needle = ('    _require(not _has_replace_refs(repo),\n'
              '             "--repo carries refs/replace entries: replace objects would "\n'
              '             "shadow the committed bytes this guard reads")\n')
    m1 = cur_tool.decode("utf-8").replace(needle, "")
    assert m1 != cur_tool.decode("utf-8")
    import json as _json
    claims = git("show", "%s:reports/round-80/claims.json"
                 % args.freeze).stdout.decode("utf-8")
    doc = _json.loads(claims)
    for cl in doc["claims"]:
        if cl.get("id") == "O":
            cl["guard80"]["legs"] = ["FROZENCFG", "TOOL"]
    shrunk = _json.dumps(doc, indent=1, ensure_ascii=False) + chr(10)
    assert shrunk != claims

    print("JUNK-RECEIPT round-80 claim O (accept-o.py; each junk landing "
          "must FAIL)")
    reset_index(args.lands)
    put_file("tools/ledger-token-guard.py", old_tool)
    grade("reports/round-80/accept-o.py", "junk-o", "JO1 old r79 tool at lands",
          ["TOOL"], parent=args.lands_o)
    reset_index(args.lands)
    put_file("tools/ledger-token-guard.py", m1.encode("utf-8"))
    grade("reports/round-80/accept-o.py", "junk-o",
          "JO2 replace refusal stubbed", ["TOOL", "REPLACE"],
          parent=args.lands_o)
    reset_index(args.lands)
    put_file("reports/round-80/claims.json", shrunk.encode("utf-8"))
    grade("reports/round-80/accept-o.py", "junk-o",
          "JO3 claims.json shrunk in graded tree", ["FROZENCFG"],
          parent=args.lands_o)

    entry_rel = "corpus/knowledge/culture-material/maritime-seafaring-lexicon.md"
    entry = git("show", "%s:%s" % (args.lands, entry_rel)).stdout.decode("utf-8")
    mut = entry.replace("| water regime |",
                        "| water regime (S899) |")
    assert mut != entry
    reg = git("show", "%s:corpus/SOURCES.md" % args.lands).stdout.decode("utf-8")
    rows = reg.splitlines()
    hit = False
    for i, ln in enumerate(rows):
        if ln.startswith("| S899 |") and "| mined | 2026-10-31 |" in ln:
            rows[i] = ln.replace("| mined | 2026-10-31 |",
                                 "| queued | 2026-10-31 |")
            hit = True
            break
    assert hit, "S899 status cell not found"
    flipped = "\n".join(rows) + "\n"

    print("JUNK-RECEIPT round-80 claim D (accept-d.py; each junk landing "
          "must FAIL)")
    reset_index(args.lands)
    remove_file(entry_rel)
    grade("reports/round-80/accept-d.py", "junk-d", "JD1 entry deleted at lands",
          ["ENTRY"])
    reset_index(args.lands)
    put_file(entry_rel, mut.encode("utf-8"))
    grade("reports/round-80/accept-d.py", "junk-d",
          "JD2 table-row S-id mutant", ["LINT"])
    reset_index(args.lands)
    put_file("corpus/SOURCES.md", flipped.encode("utf-8"))
    grade("reports/round-80/accept-d.py", "junk-d", "JD3 S899 status flipped",
          ["ROWS"])
    return 0

if __name__ == "__main__":
    sys.exit(main())
