#!/usr/bin/env python3
"""DRAFT — SentinelExec, round-79 W1 (NOT frozen, NOT integrated, NOT a verified implementation).

Proposed read-only observation grammar for the O ledger-token guard (CLAIMS-DRAFT.md, claim O).
The round-73 committed guard (accept-ca.py, argv_problem/run_observe) admits any argv whose
argv[0] basename is in {git, grep, find, wc, ls, cat, sha256sum, stat, python3}; that
admission is what W1 probes C01-C18 (see stage/SentinelExec/probe-raw-v2.txt) show to be
unsafe. This draft replaces it with:

  1. a CLOSED set of git plumbing forms (no shells, no other binaries, no python, no
     find/cat/ls/grep on the worktree);
  2. every revision a full 40-hex commit (no HEAD, branch, tag, 7-hex, index `:path`);
  3. a whitelist of flags per form; any git global option (-c, -C, --git-dir, --work-tree,
     --exec-path, --paginate, --namespace, --config-env) is refused because argv[1] must be
     a subcommand from the table;
  4. paths relative, no '..', no leading '-', no ':' (the ':' is the rev:path separator);
  5. run() with a SCRUBBED environment: GIT_CONFIG_GLOBAL=/dev/null and GIT_CONFIG_NOSYSTEM=1
     remove the operator's ~/.config/git/config (pager, diff.external, diff.<driver>.textconv,
     core.hooksPath, core.fsmonitor ...) from every observation and materialization; HOME and
     XDG_CONFIG_HOME are pointed at an empty scratch dir; GIT_PAGER/PAGER=cat; GIT_DIR and
     GIT_WORK_TREE are not inherited (the env dict is replaced, not extended).

Stdlib only. Requires git >= 2.32 (GIT_CONFIG_GLOBAL); the caller must fail closed otherwise.
"""
import os
import re
import subprocess

SHA40 = re.compile(r"^[0-9a-f]{40}$")
PATH_BAD = re.compile(r"(^/)|(^-)|(\.\.)|(:)|([\x00-\x1f\x7f])")

# subcommand -> (allowed flags, form name). Flags listed are the ONLY flags accepted.
SUBCOMMANDS = {
    "cat-file": {"flags": {"-p", "-s", "-t"}, "form": "cat-file"},
    "ls-tree": {"flags": {"-r", "--name-only"}, "form": "ls-tree"},
    "grep": {"flags": {"-n", "-c", "-l", "-o", "-h", "-H", "-E", "-F", "-i", "-w", "-x"},
             "form": "grep"},
    "rev-parse": {"flags": {"--verify", "--quiet"}, "form": "rev-parse"},
    "rev-list": {"flags": {"--count"}, "form": "rev-list"},
}
MAX_STDOUT = 1 << 20  # 1 MiB; larger output is refused, not truncated


def _refuse(reason):
    return False, reason


def check_argv(argv):
    """(ok, reason). ok=True only for a closed-grammar form; everything else is refused."""
    if not isinstance(argv, list) or len(argv) < 2 or not all(isinstance(a, str) and a for a in argv):
        return _refuse("not a non-empty argv list of non-empty strings")
    if argv[0] != "git":
        return _refuse("argv[0] %r is not git (python/sh/find/cat/ls/grep/echo refused)" % argv[0])
    sub = argv[1]
    if sub not in SUBCOMMANDS:
        return _refuse("subcommand %r not in grammar (git global options -c/-C/--git-dir/--work-tree/--exec-path/--paginate refused here)" % sub)
    rest = argv[2:]
    allowed = SUBCOMMANDS[sub]["flags"]
    flags = [a for a in rest if a.startswith("-") and a != "--"]
    for f in flags:
        if f not in allowed:
            return _refuse("flag %r not allowed for %s (ext-diff/textconv/pager/output/-O refused)" % (f, sub))
    if len(set(flags)) != len(flags):
        return _refuse("repeated flag")
    form = SUBCOMMANDS[sub]["form"]
    if form == "cat-file":
        return _check_cat_file(rest)
    if form == "ls-tree":
        return _check_ls_tree(rest)
    if form == "grep":
        return _check_grep(rest)
    if form == "rev-parse":
        return _check_rev_parse(rest)
    if form == "rev-list":
        return _check_rev_list(rest)
    return _refuse("unreachable form")


def _rev_obj_ok(obj):
    if ":" in obj:
        rev, path = obj.split(":", 1)
        if not SHA40.match(rev):
            return _refuse("revision %r is not a full 40-hex commit (mutable/short revision refused)" % rev)
        if PATH_BAD.search(path) or not path:
            return _refuse("unsafe path %r" % path)
        return True, "ok"
    if not SHA40.match(obj):
        return _refuse("object %r is not a full 40-hex id" % obj)
    return True, "ok"


def _check_cat_file(rest):
    # forms: cat-file -p|-s|-t OBJ  |  cat-file blob OBJ
    if rest and rest[0] == "blob":
        if len(rest) != 2:
            return _refuse("cat-file blob takes exactly one object")
        return _rev_obj_ok(rest[1])
    if len(rest) != 2 or rest[0] not in ("-p", "-s", "-t"):
        return _refuse("cat-file form must be `-p|-s|-t OBJ` or `blob OBJ`")
    return _rev_obj_ok(rest[1])


def _check_ls_tree(rest):
    # ls-tree -r --name-only REV -- PATH
    # rest = ["-r", "--name-only", REV, "--", PATH]
    if rest[:2] != ["-r", "--name-only"] or len(rest) != 5 or rest[3] != "--":
        return _refuse("ls-tree form must be `-r --name-only REV -- PATH`")
    if not SHA40.match(rest[2]):
        return _refuse("revision %r is not a full 40-hex commit" % rest[2])
    if PATH_BAD.search(rest[4]) or not rest[4]:
        return _refuse("unsafe path %r" % rest[4])
    return True, "ok"


def _check_grep(rest):
    # grep [flags] PATTERN REV -- PATH   (flags already whitelisted by check_argv)
    flags = [a for a in rest if a.startswith("-")]
    pos = [a for a in rest if not a.startswith("-")]
    if rest.count("--") != 1 or rest[-2] != "--" or len(pos) != 3:
        # pos = [PATTERN, REV, PATH] after removing flags; `--` is a flag-looking token
        return _refuse("grep form must be `grep [flags] PATTERN REV -- PATH`")
    pattern, rev, path = pos[0], pos[1], pos[2]
    if pattern.startswith("-"):
        return _refuse("pattern may not start with '-'")
    if not SHA40.match(rev):
        return _refuse("revision %r is not a full 40-hex commit" % rev)
    if PATH_BAD.search(path) or not path:
        return _refuse("unsafe path %r" % path)
    return True, "ok"


def _check_rev_parse(rest):
    # rev-parse --verify --quiet 40HEX^{tree|commit}
    if len(rest) != 3 or set(rest[:2]) != {"--verify", "--quiet"}:
        return _refuse("rev-parse form must be `--verify --quiet <40hex>^{tree|commit}`")
    m = re.match(r"^([0-9a-f]{40})\^\{(tree|commit)\}$", rest[2])
    if not m:
        return _refuse("rev-parse target must be <40hex>^{tree} or <40hex>^{commit}")
    return True, "ok"


def _check_rev_list(rest):
    if len(rest) != 2 or not SHA40.match(rest[1]):
        return _refuse("rev-list form must be `--count <40hex>`")
    return True, "ok"


# ---- scrubbed execution -------------------------------------------------------
def scrubbed_env(home):
    """The ONLY environment observation or materialization runs under. Config, pager,
    external diff, textconv and hooks come from the operator's global config only, so
    setting GIT_CONFIG_GLOBAL=/dev/null removes all of them; HOME is pointed at an empty dir."""
    return {
        "PATH": os.environ.get("PATH", "/usr/bin:/bin"),
        "HOME": home,
        "XDG_CONFIG_HOME": os.path.join(home, ".config-empty"),
        "GIT_CONFIG_GLOBAL": "/dev/null",
        "GIT_CONFIG_NOSYSTEM": "1",
        "GIT_PAGER": "cat",
        "PAGER": "cat",
        "GIT_TERMINAL_PROMPT": "0",
        "GIT_OPTIONAL_LOCKS": "0",
        "LC_ALL": "C.UTF-8",
        "LANG": "C.UTF-8",
        "TZ": "UTC",
    }


def run(clone, argv, expect_head, home, timeout=120):
    """(stdout, why). Refuses before running; checks HEAD == expect_head before running.
    Fails closed: nonzero exit, timeout, oversize stdout or a HEAD mismatch -> (None, why)."""
    ok, why = check_argv(argv)
    if not ok:
        return None, "refused:" + why
    head = subprocess.run(["git", "rev-parse", "HEAD"], cwd=clone, env=scrubbed_env(home),
                          capture_output=True, text=True, timeout=timeout)
    if head.returncode != 0 or head.stdout.strip() != expect_head:
        return None, "head-mismatch:%s" % head.stdout.strip()[:12]
    try:
        p = subprocess.run(argv, cwd=clone, env=scrubbed_env(home), capture_output=True,
                           text=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        return None, "timeout:%ss" % timeout
    if p.returncode != 0:
        return None, "exit=%d" % p.returncode
    if len(p.stdout) > MAX_STDOUT:
        return None, "stdout-over-cap"
    return p.stdout, "exit=0"


def materialize(lane, rev, dest, home, timeout=300):
    """Clone the lane and detach at rev under the scrubbed env (so no operator hook runs)."""
    env = scrubbed_env(home)
    c = subprocess.run(["git", "clone", "--quiet", "--no-checkout", os.path.abspath(lane), dest],
                       env=env, capture_output=True, text=True, timeout=timeout)
    if c.returncode != 0:
        return None, "clone-failed:%s" % c.stderr.strip()[:200]
    k = subprocess.run(["git", "-C", dest, "checkout", "--quiet", "--detach", rev],
                       env=env, capture_output=True, text=True, timeout=timeout)
    if k.returncode != 0:
        return None, "checkout-failed:%s" % k.stderr.strip()[:200]
    return dest, "ok"
