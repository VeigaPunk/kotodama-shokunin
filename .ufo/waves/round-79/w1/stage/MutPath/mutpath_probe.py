#!/usr/bin/env python3
# MutPath (kotodama round-79 W1) blob-path probe driver.
#
# Builds an isolated fixture repository under --work (which must be a fresh
# subdirectory of /fast/scratch/hyaku/kotodama-r79/MutPath/), runs git
# blob-path probes as argv lists (no shell), and writes the raw observations
# to --receipt. The only lane access is read-only: `git -C LANE` with
# cat-file / show / ls-tree / for-each-ref / rev-parse against LANE_BASE.
# Nothing is committed, pushed or written in the lane.
#
# Usage:
#   python3 -B mutpath_probe.py --work /fast/scratch/hyaku/kotodama-r79/MutPath/work \
#       --receipt <stage>/receipts/mutpath-probe-raw.txt
import argparse
import hashlib
import os
import re
import subprocess
import sys

LANE = "/home/vgpnk/Projects/shokunin/kotodama-shokunin"
LANE_BASE = "44f76d456c1b326a71ffdb381590af825cbf11be"
SCRATCH_ROOT = "/fast/scratch/hyaku/kotodama-r79/MutPath"

ap = argparse.ArgumentParser()
ap.add_argument("--work", required=True)
ap.add_argument("--receipt", required=True)
args = ap.parse_args()

WORK = os.path.realpath(args.work)
if not WORK.startswith(SCRATCH_ROOT + "/") or WORK.startswith(LANE):
    sys.exit("refused: --work must be a subdirectory of " + SCRATCH_ROOT)
if os.path.exists(WORK):
    sys.exit("refused: --work already exists (fresh directories only): " + WORK)
os.makedirs(WORK)
HOME = os.path.join(WORK, "home")
os.makedirs(HOME)
FIX = os.path.join(WORK, "fix")
TC = os.path.join(WORK, "clone-tc")
REP = os.path.join(WORK, "clone-rep")

ENV = {
    "PATH": os.environ.get("PATH", "/usr/bin:/bin"),
    "HOME": HOME,
    "LC_ALL": "C",
    "LANG": "C",
    "GIT_CONFIG_GLOBAL": os.devnull,
    "GIT_CONFIG_NOSYSTEM": "1",
    "GIT_PAGER": "cat",
    "PAGER": "cat",
    "GIT_TERMINAL_PROMPT": "0",
    "GIT_AUTHOR_NAME": "mutpath",
    "GIT_AUTHOR_EMAIL": "mutpath@example.invalid",
    "GIT_COMMITTER_NAME": "mutpath",
    "GIT_COMMITTER_EMAIL": "mutpath@example.invalid",
    "GIT_AUTHOR_DATE": "2026-10-30T00:00:00Z",
    "GIT_COMMITTER_DATE": "2026-10-30T00:00:00Z",
}

OUT = []


def emit(line=""):
    OUT.append(line)


def run(argv, cwd, stdin=None):
    p = subprocess.run(argv, cwd=cwd, env=ENV, input=stdin, capture_output=True, timeout=60)
    return p.returncode, p.stdout, p.stderr


def must(argv, cwd, stdin=None):
    rc, out, err = run(argv, cwd, stdin)
    if rc:
        sys.exit("setup failed rc=%d argv=%r stderr=%s" % (rc, argv, err.decode("utf-8", "replace")))
    return out.decode("utf-8", "replace").strip()


def toplevel_ok(path):
    top = os.path.realpath(must(["git", "rev-parse", "--show-toplevel"], path))
    if top != os.path.realpath(path):
        sys.exit("toplevel mismatch: %s != %s" % (top, path))
    return top


def write(rel, data):
    p = os.path.join(FIX, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "wb") as fh:
        fh.write(data)


# ---------------------------------------------------------------- fixture build
emit("# MutPath round-79 W1 blob-path probe receipt (raw, machine-generated)")
emit("# driver: stage/MutPath/mutpath_probe.py (python3 -B)")
emit("# python: " + sys.version.split()[0])
emit("# git: " + must(["git", "--version"], WORK))
emit("# lane (read-only): " + LANE + " base " + LANE_BASE)
emit("# scratch work root: " + WORK)
emit("# env (scrubbed, passed to every git call): " + ", ".join(
    sorted(k for k in ENV if not k.endswith("DATE"))) + "; dates pinned 2026-10-30T00:00:00Z")
emit()

os.makedirs(FIX)
must(["git", "init", "-q", "-b", "main"], FIX)
top_fix = toplevel_ok(FIX)
emit("fixture toplevel verified: " + top_fix)

write("corpus/SOURCES.md", b"| S001 | row one |\n| S002 | row two |\n")
write("corpus/a:b.md", b"colon-name S001\n")
write("corpus/-dash.md", b"dash S001\n")
write("corpus/knowledge/x/top.md", b"top S001\n")
write("corpus/knowledge/x/y/deep.md", b"deep S001\n")
write("corpus/sub/inner.md", b"inner S001\n")
write(".gitattributes", b"*.md diff=tc\n")
os.symlink("/etc/passwd", os.path.join(FIX, "corpus/link-abs"))
os.symlink("sub", os.path.join(FIX, "corpus/link-dir"))
must(["git", "add", "-A"], FIX)
must(["git", "update-index", "--add", "--cacheinfo", "160000," + "1" * 40 + ",corpus/subm"], FIX)
must(["git", "commit", "-q", "-m", "base corpus/SOURCES.md S001"], FIX)
C1 = must(["git", "rev-parse", "HEAD"], FIX)

write("corpus/SOURCES.md", b"| S001 | changed |\n")
must(["git", "add", "-A"], FIX)
must(["git", "commit", "-q", "-m", "second"], FIX)
C2 = must(["git", "rev-parse", "HEAD"], FIX)

# index differs from HEAD; worktree differs from index (mutable layers)
write("corpus/SOURCES.md", b"| S001 | staged |\n")
must(["git", "add", "-A"], FIX)
write("corpus/SOURCES.md", b"| S001 | worktree |\n")

# pager stub for `git grep --open-files-in-pager=` (fixture only; writes a marker in WORK)
PAGER = os.path.join(WORK, "pager.sh")
with open(PAGER, "w") as fh:
    fh.write("#!/bin/sh\nprintf 'ran %s\\n' \"$*\" >> '" + os.path.join(WORK, "marker.txt") + "'\n")
os.chmod(PAGER, 0o755)

must(["git", "clone", "-q", "--no-local", FIX, TC], WORK)
must(["git", "clone", "-q", "--no-local", FIX, REP], WORK)
toplevel_ok(TC)
toplevel_ok(REP)
must(["git", "config", "diff.tc.textconv", "tr a-z A-Z"], TC)  # clone-local, fixture only
ORIG_BLOB = must(["git", "rev-parse", C1 + ":corpus/SOURCES.md"], REP)
NEW_BLOB = must(["git", "hash-object", "-w", "--stdin"], REP, stdin=b"| S999 | replaced |\n")
must(["git", "replace", ORIG_BLOB, NEW_BLOB], REP)

emit("C1 (base, S001 row one)  = " + C1)
emit("C2 (second, changed)     = " + C2)
emit("index  : corpus/SOURCES.md staged as 'staged'; worktree 'worktree' (unstaged)")
emit("clone-tc: diff.tc.textconv = 'tr a-z A-Z' (clone-local config; .gitattributes *.md diff=tc)")
emit("clone-rep: git replace " + ORIG_BLOB[:12] + " -> " + NEW_BLOB[:12] + " (replacement blob 'S999')")
emit()

SUBS = {
    "@C1@": C1, "@C1U@": C1.upper(), "@C1S@": C1[:7], "@C2@": C2,
    "@FIX@": FIX, "@WORK@": WORK, "@TC@": TC, "@REP@": REP, "@LANE@": LANE,
    "@LANE_BASE@": LANE_BASE,
}


def sub(s):
    for k, v in SUBS.items():
        s = s.replace(k, v)
    return s


def rel(p):
    return "WORK/" + os.path.relpath(p, WORK) if p.startswith(WORK) else p


def fmt(b, limit=320):
    text = b[:limit].decode("utf-8", "replace")
    suffix = "" if len(b) <= limit else "...(+%d bytes)" % (len(b) - limit)
    return repr(text) + suffix


def sha(b):
    return hashlib.sha256(b).hexdigest()


def effect(path):
    if not os.path.exists(path):
        return "%s absent" % rel(path)
    with open(path, "rb") as fh:
        data = fh.read()
    return "%s exists size=%d sha256=%s" % (rel(path), len(data), sha(data))


# ------------------------------------------------------------------ probe list
PROBES = []


def p(pid, group, desc, argv, cwd="@FIX@", effects=()):
    PROBES.append((pid, group, desc, cwd, argv, effects))


# A. baseline: committed-blob reads that the counters rely on
p("A1", "baseline", "show committed blob at pinned commit", ["git", "show", "@C1@:corpus/SOURCES.md"])
p("A2", "baseline", "cat-file blob committed blob", ["git", "cat-file", "blob", "@C1@:corpus/SOURCES.md"])
p("A3", "baseline", "cat-file -t committed blob", ["git", "cat-file", "-t", "@C1@:corpus/SOURCES.md"])
p("A4", "baseline", "rev-parse --verify committed blob", ["git", "rev-parse", "--verify", "@C1@:corpus/SOURCES.md"])
p("A5", "baseline", "show HEAD:corpus/SOURCES.md (mutable symbolic rev, moves per commit)", ["git", "show", "HEAD:corpus/SOURCES.md"])

# B. traversal and relative-path semantics of <rev>:<path>
p("B1", "traversal", "show <rev>:../SOURCES.md (from repo root cwd)", ["git", "show", "@C1@:../SOURCES.md"])
p("B2", "traversal", "show <rev>:corpus/../corpus/SOURCES.md", ["git", "show", "@C1@:corpus/../corpus/SOURCES.md"])
p("B3", "traversal", "show <rev>:corpus/../../../../../../etc/passwd", ["git", "show", "@C1@:corpus/../../../../../../etc/passwd"])
p("B4", "traversal", "show <rev>:./corpus/SOURCES.md", ["git", "show", "@C1@:./corpus/SOURCES.md"])
p("B5", "traversal", "show <rev>:corpus//SOURCES.md (double slash)", ["git", "show", "@C1@:corpus//SOURCES.md"])
p("B6", "traversal", "show <rev>:corpus/SOURCES.md/ (trailing slash on file)", ["git", "show", "@C1@:corpus/SOURCES.md/"])
p("B7", "traversal", "cat-file -e <rev>:../../etc/passwd", ["git", "cat-file", "-e", "@C1@:../../etc/passwd"])
p("B8", "traversal", "git -C corpus show <rev>:SOURCES.md (-C changes prefix)", ["git", "-C", "corpus", "show", "@C1@:SOURCES.md"])
p("B9", "traversal", "git -C corpus show <rev>:../corpus/SOURCES.md", ["git", "-C", "corpus", "show", "@C1@:../corpus/SOURCES.md"])
p("B10", "traversal", "show <rev>:corpus/link-abs/passwd (symlink as dir component)", ["git", "show", "@C1@:corpus/link-abs/passwd"])
p("B11", "traversal", "show <rev>:corpus/link-abs (symlink blob, not followed)", ["git", "show", "@C1@:corpus/link-abs"])
p("B12", "traversal", "cat-file blob <rev>:corpus/link-abs", ["git", "cat-file", "blob", "@C1@:corpus/link-abs"])
p("B13", "traversal", "show <rev>:corpus/link-dir/inner.md (dir symlink component)", ["git", "show", "@C1@:corpus/link-dir/inner.md"])
p("B14", "traversal", "show <rev>:corpus/sub (tree, not blob)", ["git", "show", "@C1@:corpus/sub"])
p("B15", "traversal", "cat-file blob <rev>:corpus/sub (tree)", ["git", "cat-file", "blob", "@C1@:corpus/sub"])
p("B16", "traversal", "show <rev>:corpus/subm (gitlink)", ["git", "show", "@C1@:corpus/subm"])
p("B17", "traversal", "cat-file -t <rev>:corpus/subm (gitlink)", ["git", "cat-file", "-t", "@C1@:corpus/subm"])
p("B18", "traversal", "show <rev>: (root tree, empty path)", ["git", "show", "@C1@:"])
p("B19", "traversal", "show <rev>:corpus/nope.md (missing)", ["git", "show", "@C1@:corpus/nope.md"])
p("B20", "traversal", "cat-file -e <rev>:corpus/nope.md (missing)", ["git", "cat-file", "-e", "@C1@:corpus/nope.md"])
p("B21", "traversal", "cat-file -t <rev>:corpus/sub (tree type)", ["git", "cat-file", "-t", "@C1@:corpus/sub"])

# C. absolute paths and no-colon forms
p("C1", "absolute", "show <rev>:/etc/passwd", ["git", "show", "@C1@:/etc/passwd"])
p("C2", "absolute", "show <rev>:/corpus/SOURCES.md (leading slash)", ["git", "show", "@C1@:/corpus/SOURCES.md"])
p("C3", "absolute", "show <rev>:<abs fixture path>/corpus/SOURCES.md", ["git", "show", "@C1@:@FIX@/corpus/SOURCES.md"])
p("C4", "absolute", "show :/corpus/SOURCES.md (no rev: commit-message search)", ["git", "show", ":/corpus/SOURCES.md"])
p("C5", "absolute", "cat-file -t :/corpus/SOURCES.md (no rev: message search)", ["git", "cat-file", "-t", ":/corpus/SOURCES.md"])
p("C6", "absolute", "show /corpus/SOURCES.md (no colon, no --; worktree file exists)", ["git", "show", "/corpus/SOURCES.md"])
p("C7", "absolute", "cat-file -e corpus/SOURCES.md (no rev, no colon)", ["git", "cat-file", "-e", "corpus/SOURCES.md"])
p("C8", "absolute", "show corpus/SOURCES.md (no colon, no --; worktree file exists)", ["git", "show", "corpus/SOURCES.md"])

# D. colon and option ambiguity in <rev>:<path>
p("D1", "colon", "show <rev>:corpus/a:b.md (colon inside a legal filename)", ["git", "show", "@C1@:corpus/a:b.md"])
p("D2", "colon", "show <rev>:corpus/a:b.md:x (second colon becomes part of path)", ["git", "show", "@C1@:corpus/a:b.md:x"])
p("D3", "colon", "show :corpus/SOURCES.md (EMPTY rev = index, mutable)", ["git", "show", ":corpus/SOURCES.md"])
p("D4", "colon", "show :corpus/a:b.md (EMPTY rev = index)", ["git", "show", ":corpus/a:b.md"])
p("D5", "colon", "cat-file -e corpus/a:b.md (no rev; colon read as rev separator)", ["git", "cat-file", "-e", "corpus/a:b.md"])
p("D6", "colon", "show <rev>::corpus/SOURCES.md (path begins with colon)", ["git", "show", "@C1@::corpus/SOURCES.md"])
p("D7", "colon", "show <rev>:corpus/SOURCES.md: (path ends with colon)", ["git", "show", "@C1@:corpus/SOURCES.md:"])
p("D8", "colon", "show <rev> -- corpus/SOURCES.md (commit plus path limit, not content)", ["git", "show", "@C1@", "--", "corpus/SOURCES.md"])
p("D9", "colon", "show -- <rev>:corpus/SOURCES.md (-- makes it a path)", ["git", "show", "--", "@C1@:corpus/SOURCES.md"])
p("D10", "colon", "show <rev>:corpus/-dash.md (leading dash in filename)", ["git", "show", "@C1@:corpus/-dash.md"])
p("D11", "colon", "rev-parse --verify --quiet :corpus/SOURCES.md (index blob id)", ["git", "rev-parse", "--verify", "--quiet", ":corpus/SOURCES.md"])
p("D12", "colon", "rev-parse --verify <rev>^{tree}:corpus (tree id)", ["git", "rev-parse", "--verify", "@C1@^{tree}:corpus"])
p("D13", "colon", "cat-file blob :corpus/SOURCES.md (index blob, mutable)", ["git", "cat-file", "blob", ":corpus/SOURCES.md"])

# E. pathspec forms on git grep (observe_cmd grammar uses `git grep ... <rev> -- <path>`)
GREP = ["git", "grep", "-c", "S001"]
p("E1", "pathspec", "grep <rev> -- corpus/SOURCES.md", GREP + ["@C1@", "--", "corpus/SOURCES.md"])
p("E2", "pathspec", "grep <rev> -- :/corpus/SOURCES.md (top magic)", GREP + ["@C1@", "--", ":/corpus/SOURCES.md"])
p("E3", "pathspec", "grep <rev> -- :(top)corpus/SOURCES.md", GREP + ["@C1@", "--", ":(top)corpus/SOURCES.md"])
p("E4", "pathspec", "grep <rev> -- corpus/knowledge/*/*.md (no glob magic)", GREP + ["@C1@", "--", "corpus/knowledge/*/*.md"])
p("E5", "pathspec", "grep <rev> -- :(glob)corpus/knowledge/*/*.md", GREP + ["@C1@", "--", ":(glob)corpus/knowledge/*/*.md"])
p("E6", "pathspec", "grep <rev> -- corpus/*.md (wildcard crosses slash?)", GREP + ["@C1@", "--", "corpus/*.md"])
p("E7", "pathspec", "grep <rev> -- :(literal)corpus/*.md", GREP + ["@C1@", "--", ":(literal)corpus/*.md"])
p("E8", "pathspec", "grep <rev> -- corpus/nope.md (missing path)", GREP + ["@C1@", "--", "corpus/nope.md"])
p("E9", "pathspec", "grep <rev> -- corpus/a:b.md (colon mid-pathspec)", GREP + ["@C1@", "--", "corpus/a:b.md"])
p("E10", "pathspec", "grep <rev> -- :corpus/a:b.md (leading colon pathspec)", GREP + ["@C1@", "--", ":corpus/a:b.md"])
p("E11", "pathspec", "grep <rev> -- corpus :!corpus/SOURCES.md (exclude magic)", GREP + ["@C1@", "--", "corpus", ":!corpus/SOURCES.md"])
p("E12", "pathspec", "grep <rev> -- ../corpus/SOURCES.md (outside repo)", GREP + ["@C1@", "--", "../corpus/SOURCES.md"])
p("E13", "pathspec", "grep <rev> -- /etc/passwd (absolute pathspec)", GREP + ["@C1@", "--", "/etc/passwd"])
p("E14", "pathspec", "grep <rev> -- corpus/sub (directory pathspec)", GREP + ["@C1@", "--", "corpus/sub"])
p("E15", "pathspec", "grep (no rev) -- corpus/SOURCES.md (reads WORKTREE, mutable)", GREP + ["--", "corpus/SOURCES.md"])
p("E16", "pathspec", "grep <rev> -- corpus/link-abs (symlink blob)", GREP + ["@C1@", "--", "corpus/link-abs"])
p("E17", "pathspec", "grep two revs <rev> HEAD -- corpus/SOURCES.md (extra operand)", GREP + ["@C1@", "HEAD", "--", "corpus/SOURCES.md"])
p("E18", "pathspec", "grep EMPTY rev \"\" -- corpus/SOURCES.md (empty rev operand)", GREP + ["", "--", "corpus/SOURCES.md"])

# F. options, exec and write escapes; numeric and ref ambiguity
p("F1", "options", "show --output=<WORK>/out-F1.txt <rev>:path (write escape?)",
  ["git", "show", "--output=@WORK@/out-F1.txt", "@C1@:corpus/SOURCES.md"],
  effects=["@WORK@/out-F1.txt"])
p("F2", "options", "grep --open-files-in-pager=<WORK>/pager.sh (exec escape?)",
  ["git", "grep", "--open-files-in-pager=@WORK@/pager.sh", "-c", "S001", "@C1@", "--", "corpus/SOURCES.md"],
  effects=["@WORK@/marker.txt"])
p("F2b", "options", "grep --open-files-in-pager=<WORK>/pager.sh WITHOUT rev (worktree form; exec escape?)",
  ["git", "grep", "--open-files-in-pager=@WORK@/pager.sh", "-c", "S001", "--", "corpus/SOURCES.md"],
  effects=["@WORK@/marker.txt"])
p("F2c", "options", "grep -O<WORK>/pager.sh short form WITHOUT rev",
  ["git", "grep", "-O@WORK@/pager.sh", "-c", "S001", "--", "corpus/SOURCES.md"],
  effects=["@WORK@/marker.txt"])
p("F1b", "options", "show --output=<WORK>/out-F1b.txt on a COMMIT (no rev:path)",
  ["git", "show", "--output=@WORK@/out-F1b.txt", "@C1@"],
  effects=["@WORK@/out-F1b.txt"])
p("F3", "options", "cat-file -e -p^{commit} (option-looking rev)", ["git", "cat-file", "-e", "-p^{commit}"])
p("F4", "options", "rev-parse --verify -- -p^{commit}", ["git", "rev-parse", "--verify", "--", "-p^{commit}"])
p("F5", "options", "cat-file -e <rev with trailing newline>^{commit}", ["git", "cat-file", "-e", "@C1@\n^{commit}"])
p("F6", "options", "cat-file -e <UPPERCASE rev>^{commit}", ["git", "cat-file", "-e", "@C1U@^{commit}"])
p("F7", "options", "cat-file -e <7-char short rev>^{commit}", ["git", "cat-file", "-e", "@C1S@^{commit}"])
p("S1", "setup", "SETUP: create branch whose name is the 40-hex C1 pointing at C2",
  ["git", "branch", "@C1@", "@C2@"])
p("F8", "options", "rev-parse --verify <C1>^{commit} with branch named <C1> -> C2", ["git", "rev-parse", "--verify", "@C1@^{commit}"])
p("F9", "options", "show <C1>:corpus/SOURCES.md with branch named <C1> present", ["git", "show", "@C1@:corpus/SOURCES.md"])

# G. textconv: does `git show <rev>:path` return committed bytes or a textconv output?
p("G1", "textconv", "show <rev>:corpus/SOURCES.md (clone with textconv driver)",
  ["git", "show", "@C1@:corpus/SOURCES.md"], cwd="@TC@")
p("G2", "textconv", "cat-file blob <rev>:corpus/SOURCES.md (clone with textconv driver)",
  ["git", "cat-file", "blob", "@C1@:corpus/SOURCES.md"], cwd="@TC@")
p("G3", "textconv", "show --no-textconv <rev>:corpus/SOURCES.md (clone with textconv driver)",
  ["git", "show", "--no-textconv", "@C1@:corpus/SOURCES.md"], cwd="@TC@")

# H. replace refs: can a replacement alter 'committed bytes'?
p("H1", "replace", "show <rev>:corpus/SOURCES.md (clone with git replace on the blob)",
  ["git", "show", "@C1@:corpus/SOURCES.md"], cwd="@REP@")
p("H2", "replace", "cat-file blob <rev>:corpus/SOURCES.md (replace on blob)",
  ["git", "cat-file", "blob", "@C1@:corpus/SOURCES.md"], cwd="@REP@")
p("H3", "replace", "show --no-replace-objects <rev>:corpus/SOURCES.md",
  ["git", "--no-replace-objects", "show", "@C1@:corpus/SOURCES.md"], cwd="@REP@")
p("H4", "replace", "grep -c S001 <rev> -- corpus/SOURCES.md (replace on blob)",
  GREP + ["@C1@", "--", "corpus/SOURCES.md"], cwd="@REP@")
p("H5", "replace", "grep -c S999 <rev> -- corpus/SOURCES.md (replacement text visible?)",
  ["git", "grep", "-c", "S999", "@C1@", "--", "corpus/SOURCES.md"], cwd="@REP@")

# L. lane read-only observations at the frozen base (no writes; read-only plumbing only)
p("L1", "lane-ro", "cat-file -e <LANE_BASE>:corpus/SOURCES.md",
  ["git", "cat-file", "-e", "@LANE_BASE@:corpus/SOURCES.md"], cwd="@LANE@")
p("L2", "lane-ro", "show <LANE_BASE>:../../../etc/passwd",
  ["git", "show", "@LANE_BASE@:../../../etc/passwd"], cwd="@LANE@")
p("L3", "lane-ro", "show <LANE_BASE>:/corpus/SOURCES.md",
  ["git", "show", "@LANE_BASE@:/corpus/SOURCES.md"], cwd="@LANE@")
p("L4", "lane-ro", "for-each-ref refs/replace (lane has no replace refs?)",
  ["git", "for-each-ref", "--format=%(refname)", "refs/replace"], cwd="@LANE@")
p("L5", "lane-ro", "ls-tree -r --name-only <LANE_BASE> -- corpus/knowledge (depth census below)",
  ["git", "ls-tree", "-r", "--name-only", "@LANE_BASE@", "--", "corpus/knowledge"], cwd="@LANE@")
p("L6", "lane-ro", "cat-file -t <round-78 pin 4b255745>^{commit}",
  ["git", "cat-file", "-t", "4b255745dea45a45d88b17e3c3fea4cdb6700cf7^{commit}"], cwd="@LANE@")

# ------------------------------------------------------------------- execute
emit("== probe results (argv as given; @TOKENS@ substituted; cwd shown relative to WORK)")
emit()
RESULTS = []
for pid, group, desc, cwd, argv, effects in PROBES:
    cwd_s = sub(cwd)
    argv_s = [sub(a) for a in argv]
    if pid == "S1":
        rc, out, err = run(argv_s, cwd_s)
        emit("== [%s] %s %s" % (pid, group, desc))
        emit("argv: %r   cwd: %s" % (argv_s, rel(cwd_s)))
        emit("rc: %d   stdout: %s   stderr: %s" % (rc, fmt(out), fmt(err)))
        if rc != 0:
            rc2, out2, err2 = run(["git", "update-ref", "refs/heads/" + C1, C2], cwd_s)
            emit("fallback argv: ['git','update-ref','refs/heads/<C1>','<C2>'] rc=%d stderr=%s" % (rc2, fmt(err2)))
        emit()
        continue
    rc, out, err = run(argv_s, cwd_s)
    emit("== [%s] %s %s" % (pid, group, desc))
    emit("argv: %r   cwd: %s" % (argv_s, rel(cwd_s)))
    emit("rc: %d   stdout_bytes=%d stdout_sha256=%s" % (rc, len(out), sha(out)))
    emit("stdout: " + fmt(out))
    emit("stderr: " + fmt(err, 240))
    for e in effects:
        emit("effect: " + effect(sub(e)))
    emit()
    RESULTS.append((pid, rc))

# Lane depth census (derived from L5 output; read-only)
l5 = subprocess.run(["git", "ls-tree", "-r", "--name-only", LANE_BASE, "--", "corpus/knowledge"],
                    cwd=LANE, env=ENV, capture_output=True, timeout=60)
names = [n for n in l5.stdout.decode("utf-8", "replace").split("\n") if n]
md = [n for n in names if n.endswith(".md")]
deep = [n for n in md if n.count("/") >= 4]
emit("== DERIVED lane census at base (from L5 output)")
emit("corpus/knowledge .md files: %d; depth>=4 (nested below a partition dir): %d" % (len(md), len(deep)))
for n in deep[:12]:
    emit("  deep: " + n)
emit()

# PY-side validation shapes for --lands / --freeze style args (no git)
emit("== PY regex shapes for a 40-hex revision argument (no git involved)")
for label, value in (("C1 exact", C1), ("C1 + newline", C1 + "\n"), ("C1 uppercase", C1.upper()),
                     ("C1 short7", C1[:7]), ("'-p' + C1", "-p" + C1)):
    m_match = re.match(r"[0-9a-f]{40}$", value)
    m_full = re.fullmatch(r"[0-9a-f]{40}", value)
    emit("%-14s re.match(...$)=%-5s re.fullmatch=%s" % (label, bool(m_match), bool(m_full)))
emit()

# Summary of probe exit codes
emit("== exit code summary")
for pid, rc in RESULTS:
    emit("%s rc=%d" % (pid, rc))

os.makedirs(os.path.dirname(os.path.realpath(args.receipt)), exist_ok=True)
with open(args.receipt, "w") as fh:
    fh.write("\n".join(OUT) + "\n")
print("receipt written: %s (%d lines)" % (args.receipt, len(OUT) + 1))
