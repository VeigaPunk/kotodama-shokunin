#!/usr/bin/env python3
"""SentinelExec W1 probe v2: runs the COMMITTED round-73 accept-ca.py observe guard
(argv_problem / run_observe / materialize; bytes copied unmodified from base
44f76d4 into scratch) against isolated fixture repos under scratch only.
Each case runs exactly once through run_observe (the committed function). Hostile
HOME config points at marker-writing script files, so a fired driver is visible as
a line in MARK. The only lane-external git mutation is C15 (update-ref -d) against
fixture 'other', whose root is asserted before use."""
import importlib.util, json, os, pathlib, shutil, subprocess

SCR = pathlib.Path("/fast/scratch/hyaku/kotodama-r79/SentinelExec").resolve()
RUN = SCR / "probe"
COUNTER = SCR / "accept-ca-r73.py"
assert str(RUN).startswith(str(SCR) + os.sep), RUN
if RUN.exists():
    shutil.rmtree(RUN)
RUN.mkdir(parents=True)

CLEAN = dict(os.environ, GIT_CONFIG_GLOBAL="/dev/null", GIT_CONFIG_NOSYSTEM="1",
             GIT_AUTHOR_NAME="p", GIT_AUTHOR_EMAIL="p@example.invalid",
             GIT_COMMITTER_NAME="p", GIT_COMMITTER_EMAIL="p@example.invalid")


def g(cwd, *a):
    r = subprocess.run(["git", "-C", str(cwd), *a], capture_output=True, text=True, env=CLEAN)
    assert r.returncode == 0, (a, r.stderr)
    return r.stdout.strip()


def fixture(name):
    p = RUN / name
    p.mkdir()
    subprocess.run(["git", "init", "-q", "-b", "main", str(p)], check=True, env=CLEAN)
    top = g(p, "rev-parse", "--show-toplevel")
    assert pathlib.Path(top).resolve() == p.resolve(), (top, p)  # verified root
    return p


other = fixture("other")
(other / "secret.txt").write_text("OUTSIDE-SECRET-LINE\n")
g(other, "add", "-A"); g(other, "commit", "-q", "-m", "other")
OTHER_REV = g(other, "rev-parse", "HEAD")
g(other, "branch", "victim")

lane = fixture("lane")
(lane / ".gitattributes").write_text("a.txt diff=evil\n")
(lane / "a.txt").write_text("needle one\n")
g(lane, "add", "-A"); g(lane, "commit", "-q", "-m", "r1")
REV1 = g(lane, "rev-parse", "HEAD")
(lane / "a.txt").write_text("needle two\n")
g(lane, "add", "-A"); g(lane, "commit", "-q", "-m", "r2")
REV2 = g(lane, "rev-parse", "HEAD")

# hostile HOME config: each driver is a script that appends its name to MARK
HOME = RUN / "home"; HOME.mkdir()
HOOKS = RUN / "hooks"; HOOKS.mkdir()
MARK = RUN / "MARK"
DRIVERS = {
    "pager": ("pager.sh", "echo PAGER-core >> %s\nexit 0\n"),
    "ext": ("ext.sh", "echo EXT-diff >> %s\nexit 0\n"),
    "textconv": ("textconv.sh", "echo TEXTCONV-evil >> %s\ncat \"$1\"\n"),
    "hook": ("hooks/post-checkout", "echo HOOK-post-checkout >> %s\n"),
}
for key, (name, body) in DRIVERS.items():
    p = RUN / name
    p.parent.mkdir(exist_ok=True)
    p.write_text("#!/bin/sh\n" + body % MARK)
    os.chmod(p, 0o755)
(HOME / ".gitconfig").write_text(
    "[core]\n\tpager = %s\n\thooksPath = %s\n"
    "[diff]\n\texternal = %s\n"
    "[diff \"evil\"]\n\ttextconv = %s\n"
    % (RUN / "pager.sh", RUN / "hooks", RUN / "ext.sh", RUN / "textconv.sh"))

os.environ["HOME"] = str(HOME)
os.environ.pop("GIT_CONFIG_GLOBAL", None)
os.environ["XDG_CONFIG_HOME"] = str(RUN / "xdg-empty")
spec = importlib.util.spec_from_file_location("ca73", str(COUNTER))
ca = importlib.util.module_from_spec(spec); spec.loader.exec_module(ca)

MAT = RUN / "mat"; MAT.mkdir()
if MARK.exists(): MARK.unlink()
clone = ca.materialize(str(lane), REV2, str(MAT), "obs")
assert clone and clone["head"] == REV2, clone
results = []


def marks():
    return MARK.read_text().split() if MARK.exists() else []


def case(cid, desc, argv, extra=None):
    if MARK.exists(): MARK.unlink()
    prob = ca.argv_problem(argv)
    if prob:
        out, why = None, "not-run:argv_problem"
    else:
        out, why = ca.run_observe(clone["path"], argv)  # committed function, one execution
    rec = {"id": cid, "desc": desc, "argv": argv, "argv_problem": prob,
           "run_observe": why, "stdout": (out or "")[:240], "markers": marks()}
    if extra:
        rec.update(extra())
    results.append(rec)
    print(json.dumps(rec, ensure_ascii=False))
    return rec


hook_marks = marks()
results.append({"id": "C00", "desc": "materialize (clone + checkout) under HOME core.hooksPath",
                "head_ok": clone["head"] == REV2, "markers": hook_marks})
print(json.dumps(results[-1], ensure_ascii=False))
if MARK.exists(): MARK.unlink()

case("C01", "mutable HEAD revision in cat-file", ["git", "cat-file", "-p", "HEAD:a.txt"])
case("C02", "git show REV:path with attr diff=evil (textconv driver in HOME config)",
     ["git", "show", REV2 + ":a.txt"])
case("C03", "control: plumbing cat-file blob at pinned revision", ["git", "cat-file", "blob", REV2 + ":a.txt"])
case("C04", "git grep -O with no revision (worktree) under HOME core.pager",
     ["git", "grep", "-O", "needle", "--", "a.txt"])
case("C04r", "git grep -O with a pinned revision (control: refused by git)",
     ["git", "grep", "-O", "needle", REV2, "--", "a.txt"])
case("C05", "argv -c core.pager override + worktree grep -O",
     ["git", "-c", "core.pager=%s" % (RUN / "pager.sh"), "grep", "-O", "needle", "--", "a.txt"])
case("C06", "git diff with diff.external in HOME config (ext-diff default on)",
     ["git", "diff", REV1 + ".." + REV2, "--", "a.txt"])
case("C06b", "git diff --no-ext-diff: textconv still in play under HOME attr driver",
     ["git", "diff", "--no-ext-diff", REV1 + ".." + REV2, "--", "a.txt"])
case("C07", "git diff --no-ext-diff --no-textconv --no-color -U0 (candidate spelling)",
     ["git", "diff", "--no-ext-diff", "--no-textconv", "--no-color", "-U0",
      REV1 + ".." + REV2, "--", "a.txt"])
case("C08", "git -C <other> reads a repo outside the clone",
     ["git", "-C", str(other), "cat-file", "-p", OTHER_REV + ":secret.txt"])
case("C09", "git --git-dir override reads outside the clone",
     ["git", "--git-dir", str(other / ".git"), "cat-file", "-p", OTHER_REV + ":secret.txt"])
FPRINT = RUN / "FPRINT"
case("C10", "find -fprint writes a file outside the clone",
     ["find", ".", "-maxdepth", "0", "-fprint", str(FPRINT)],
     extra=lambda: {"written_outside_clone": FPRINT.exists()})
case("C11", "cat of an absolute path outside the clone", ["cat", str(other / "secret.txt")])
case("C12", "python3 -c constant printer, no decoy token", ["python3", "-c", "print(245)"])
case("C12b", "python3 -c constant printer carrying the decoy token 'pathlib'",
     ["python3", "-c", "import pathlib;print(245)"])
case("C13", "python3 -c subprocess escape to sh (sh named only inside python)",
     ["python3", "-c", "import subprocess;subprocess.run(['sh','-c','echo PY-escape >> %s']);print(1)" % MARK])
case("C14", "7-hex abbreviated revision accepted", ["git", "cat-file", "-p", REV2[:7] + ":a.txt"])
case("C15", "git -C <other> update-ref -d: mutation of an outside repo (fixture other)",
     ["git", "-C", str(other), "update-ref", "-d", "refs/heads/victim"],
     extra=lambda: {"victim_present_after": "victim" in g(other, "branch", "--list", "victim")})
open(os.path.join(clone["path"], "untracked.md"), "w").write("worktree-only\n")
case("C16", "ls-files --others sees a worktree-only file in the clone",
     ["git", "ls-files", "--others", "--exclude-standard"])
case("C18", "pinned control: ls-tree at REV2 path filter",
     ["git", "ls-tree", "-r", "--name-only", REV2, "--", "a.txt"])

raw = RUN / "probe-results.jsonl"
raw.write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in results) + "\n")
print("FIXTURE other=%s lane=%s REV1=%s REV2=%s OTHER_REV=%s" % (other, lane, REV1, REV2, OTHER_REV))
print("RESULTS %s" % raw)
