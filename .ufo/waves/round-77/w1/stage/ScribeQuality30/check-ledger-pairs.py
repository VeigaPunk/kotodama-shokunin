#!/usr/bin/env python3
"""QUALITY 30 red-before check — a Ca ledger pair executes as an argv over committed bytes.

Reads the ledger blob at a revision (`git -C <repo> show <rev>:<ledger>`), never a
worktree copy, and grades each pair on four limbs:

  (a) argv, not shell text — `observe_cmd` is a non-empty argv list, and `rederive`
      (when present) is one too; the executable is in the read-only allowlist;
      a shell metacharacter outside a named grep pattern operand is refused.
  (b) `git -C <repo>` FIRST, revision in rev position — a git command begins
      `git -C <repo> <subcommand>`; every 40-hex operand sits before the `--`
      separator (never after it, never inside a path or pattern) and resolves in
      the repository; the command names at least one revision.
  (c) pattern operands named — a grep / git-grep pattern is the argument of -e /
      --regexp or the single first bare operand, so a pattern that carries a space
      cannot leak into a path or revision operand.
  (d) the statement is where the ledger says — `stated_at` is `path:line` inside a
      frozen allowlist for the disposition, and `stated_text` sits on that line of
      the base tree.

`--execute` adds the run limb: each pair's own argv is executed with cwd = the
scratch root and `parse` must return `expected_after`.

Exit: 0 every pair green; 1 at least one RED; 2 input error (an unreadable ledger,
a non-hex revision, or a missing allowlist — a check that cannot fail must refuse,
never print PASS).
"""
import argparse
import json
import os
import re
import subprocess
import sys

ALLOW = ("git", "grep", "wc", "sha256sum", "ls", "cat", "head", "tail", "cut")
INTERP = ("python", "python2", "python3", "pypy", "pypy3", "sh", "bash", "zsh",
          "dash", "ksh", "fish", "csh", "tcsh", "perl", "node", "nodejs", "ruby",
          "php", "awk", "gawk", "mawk", "sed", "env", "xargs", "eval", "exec",
          "nice", "nohup", "time", "busybox")
SHELL_META = ("|", "&", ";", "<", ">", "`", "$(", "\n", "\r")
HEX40 = re.compile(r"^[0-9a-f]{40}$")
REV_NAME = re.compile(r"^(HEAD|HEAD\^|HEAD~\d+|@)$")


def git(repo, *args):
    p = subprocess.run(["git", "-C", repo] + list(args),
                       capture_output=True, text=True)
    return p.returncode, p.stdout, p.stderr


def show(repo, rev, path):
    rc, out, _ = git(repo, "show", "%s:%s" % (rev, path))
    return out if rc == 0 else None


def exists_at(repo, rev, path):
    if not path:
        return False
    return git(repo, "cat-file", "-e", "%s:%s" % (rev, path))[0] == 0


def norm(text):
    return " ".join((text or "").split())


def pattern_positions(argv):
    """Global argv indices of grep pattern operands (the only elements that may
    carry a metacharacter).  Returns (set, why)."""
    binary = os.path.basename(argv[0])
    if binary == "git":
        # locate the subcommand whether or not `-C <repo>` is present: a missing
        # `-C` is the git limb's finding, and must not turn a pattern into a
        # spurious META hit here.
        i = 1
        while i < len(argv) and argv[i] == "-C" and i + 1 < len(argv):
            i += 2
        if i >= len(argv) or argv[i] != "grep":
            return set(), None
        start = i + 1
    elif binary == "grep":
        start = 1
    else:
        return set(), None
    out, have, i = set(), False, start
    while i < len(argv):
        a = argv[i]
        if a == "--":
            break
        if a.startswith("-") and len(a) > 1:
            if a in ("-e", "--regexp"):
                if i + 1 >= len(argv):
                    return set(), "grep %s without an argument" % a
                out.add(i + 1)
                have = True
                i += 2
                continue
            if a in ("-f", "--file"):
                return set(), "grep %s reads patterns from a file, not a named operand" % a
            i += 1
            continue
        if not have:
            out.add(i)
            have = True
        i += 1
    if not out:
        return set(), "grep with no pattern operand"
    return out, None


def argv_limb(pair, patterns):
    codes = []
    cmd = pair.get("observe_cmd")
    if isinstance(cmd, str):
        codes.append("SHELL-STRING: observe_cmd is a shell string, not an argv list")
    elif not isinstance(cmd, list) or not cmd:
        codes.append("SHELL-STRING: observe_cmd is not a non-empty argv list")
    else:
        for i, a in enumerate(cmd):
            if not isinstance(a, str) or not a:
                codes.append("SHELL-STRING: argv element %d is not a non-empty string" % i)
        base = os.path.basename(cmd[0]) if isinstance(cmd[0], str) else ""
        if base in INTERP:
            codes.append("EXEC-NOT-ALLOWED: interpreter/constant-printer %r" % cmd[0])
        elif base not in ALLOW:
            codes.append("EXEC-NOT-ALLOWED: argv[0] %r not in the allowlist %s"
                         % (cmd[0], list(ALLOW)))
        for i, a in enumerate(cmd):
            if not isinstance(a, str) or i in patterns:
                continue
            for bad in SHELL_META:
                if bad in a:
                    codes.append("META: shell construct %r in non-pattern argv "
                                 "element %r" % (bad, a[:48]))
                    break
    red = pair.get("rederive")
    if red is not None and not isinstance(red, list):
        codes.append("REDERIVE-STRING: rederive is %s, not an argv list (a shell "
                     "tokenizer would re-split it)" % type(red).__name__)
    return codes


def git_limb(pair, repo, base, patterns):
    codes = []
    cmd = pair.get("observe_cmd")
    if not isinstance(cmd, list) or not cmd:
        return codes
    if os.path.basename(cmd[0]) not in ALLOW:
        return codes            # a refused executable has no operands to resolve
    if os.path.basename(cmd[0]) != "git":
        # a non-git allowlisted binary: every non-option operand is a path
        for i, a in enumerate(cmd[1:], 1):
            if i in patterns or not isinstance(a, str) or a.startswith("-"):
                continue
            if not exists_at(repo, base, a):
                codes.append("UNRESOLVED: operand %r is not a path at base %s"
                             % (a, base[:7]))
        return codes
    args = cmd[1:]
    if len(args) < 2 or args[0] != "-C":
        codes.append("NO-C: git argv does not begin `git -C <repo>` "
                     "(it only runs from one working directory)")
        return codes
    if os.path.realpath(args[1]) != os.path.realpath(repo):
        codes.append("C-OTHER: `-C %s` is not the checked repository" % args[1])
        return codes
    if len(args) < 3:
        codes.append("NO-C: `git -C <repo>` with no subcommand")
        return codes
    sub, rest = args[2], args[3:]
    off = 4                     # global argv index of rest[0] when `-C <repo>` leads
    dash = rest.index("--") if "--" in rest else None
    revs, paths = [], []
    for i, a in enumerate(rest):
        if i + off in patterns or a == "--" or a.startswith("-"):
            continue
        if HEX40.match(a):
            if dash is not None and i > dash:
                codes.append("REV-POS: revision %s sits after `--`, in the path "
                             "position" % a)
            revs.append(a)
        elif ":" in a and not a.startswith(":"):
            head, _, tail = a.partition(":")
            if HEX40.match(head) or REV_NAME.match(head):
                revs.append(head)
                paths.append(tail)
            else:
                paths.append(a)
        elif REV_NAME.match(a):
            revs.append(a)
        else:
            paths.append(a)
    if not revs:
        codes.append("NO-REV: git %s names no revision operand" % sub)
    for r in revs:
        if HEX40.match(r) and git(repo, "cat-file", "-e", r)[0] != 0:
            codes.append("DEAD-PIN: revision %s is not an object of the repository" % r)
    for p in paths:
        if not exists_at(repo, base, p):
            codes.append("UNRESOLVED: operand %r is neither a revision nor a path "
                         "at base %s" % (p, base[:7]))
    return codes


def site_limb(pair, repo, base, annotate_allow, repair_allow):
    codes = []
    stated_at = pair.get("stated_at") or ""
    m = re.match(r"^(.+):(\d+)$", stated_at)
    if not m:
        return ["STATED-AT-SYNTAX: %r is not path:line" % stated_at]
    path, line = m.group(1), int(m.group(2))
    disp = pair.get("disposition")
    allow = annotate_allow if disp == "ANNOTATE" else repair_allow
    if path not in allow:
        codes.append("STATED-AT-SET: %s is outside the frozen %s allowlist %s"
                     % (path, disp, list(allow)))
    body = show(repo, base, path)
    if body is None:
        codes.append("STATED-AT-SYNTAX: %s is absent at base %s" % (path, base[:7]))
        return codes
    lines = body.splitlines()
    if line < 1 or line > len(lines):
        codes.append("STATED-AT-SYNTAX: line %d is out of range (%d lines)"
                     % (line, len(lines)))
        return codes
    text = norm(pair.get("stated_text"))
    if not text:
        codes.append("STATED-TEXT-ABSENT: stated_text is empty")
    elif text not in norm(lines[line - 1]):
        if text in norm(body):
            codes.append("STATED-TEXT-ABSENT: stated_text is in %s but not on "
                         "line %d" % (path, line))
        else:
            codes.append("STATED-TEXT-ABSENT: stated_text is not in %s at base"
                         % path)
    sp = pair.get("stated_parse")
    if sp and text:
        try:
            if not re.search(sp, pair.get("stated_text") or "", re.M):
                codes.append("PARSE-MISS: stated_parse does not match stated_text")
        except re.error as exc:
            codes.append("PARSE-MISS: stated_parse does not compile: %s" % exc)
    return codes


def execute_limb(pair, work):
    cmd = pair.get("observe_cmd")
    if not isinstance(cmd, list) or not cmd:
        return ["EXEC-FAIL: no argv to execute"]
    try:
        p = subprocess.run(cmd, cwd=work, capture_output=True, text=True,
                           timeout=120)
    except OSError as exc:
        return ["EXEC-FAIL: %s" % exc]
    if p.returncode != 0:
        first = (p.stderr or p.stdout).strip().splitlines()
        return ["EXEC-FAIL: exit=%d %s" % (p.returncode, first[0][:120] if first else "")]
    parse = pair.get("parse")
    want = norm(pair.get("expected_after"))
    if parse == "count-presence":
        n = len([l for l in p.stdout.splitlines() if l.strip()])
        got = "present" if n > 0 else "absent"
    elif isinstance(parse, str):
        try:
            m = re.search(parse, p.stdout, re.M)
        except re.error as exc:
            return ["EXEC-FAIL: parse does not compile: %s" % exc]
        if not m:
            return ["OBSERVE-MISMATCH: parse %r matched nothing" % parse]
        got = norm(m.group(1) if m.groups() else m.group(0))
    else:
        got = norm(p.stdout)
    if got != want:
        return ["OBSERVE-MISMATCH: observed %r != expected %r" % (got, want)]
    return []


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True)
    ap.add_argument("--rev", required=True, help="40-hex revision the ledger is read at")
    ap.add_argument("--ledger", required=True, help="repo-relative ledger path")
    ap.add_argument("--annotate-allow", default="")
    ap.add_argument("--repair-allow", default="")
    ap.add_argument("--execute", action="store_true")
    ap.add_argument("--work", default="")
    ap.add_argument("--quiet-ok", action="store_true")
    a = ap.parse_args()

    repo = os.path.abspath(a.repo)
    if not HEX40.match(a.rev):
        print("LEDGER-PAIRS: REFUSED (--rev %r is not a 40-hex commit)" % a.rev)
        return 2
    if not a.annotate_allow or not a.repair_allow:
        print("LEDGER-PAIRS: REFUSED (--annotate-allow and --repair-allow are "
              "required: an empty allowlist would pass every site)")
        return 2
    raw = show(repo, a.rev, a.ledger)
    if raw is None:
        print("LEDGER-PAIRS: REFUSED (no committed ledger at %s:%s)"
              % (a.rev[:7], a.ledger))
        return 2
    try:
        led = json.loads(raw)
    except ValueError as exc:
        print("LEDGER-PAIRS: REFUSED (ledger is not JSON: %s)" % exc)
        return 2
    base = led.get("base") or ""
    if not HEX40.match(str(base)):
        print("LEDGER-PAIRS: REFUSED (ledger base %r is not a 40-hex commit)" % base)
        return 2
    pairs = led.get("pairs") or []
    if not isinstance(pairs, list) or not pairs:
        print("LEDGER-PAIRS: REFUSED (ledger carries no pairs)")
        return 2
    annotate_allow = [p for p in a.annotate_allow.split(",") if p]
    repair_allow = [p for p in a.repair_allow.split(",") if p]

    if a.execute:
        work = a.work or os.environ.get("HYAKU_SCRATCH") or os.environ.get("TMPDIR")
        if not work:
            print("LEDGER-PAIRS: REFUSED (--execute needs --work, $HYAKU_SCRATCH "
                  "or $TMPDIR; no system temp dir is invented)")
            return 2
        work = os.path.abspath(work)
        os.makedirs(work, exist_ok=True)
    else:
        work = None

    reds, codes_all, total = 0, {}, len(pairs)
    for idx, pair in enumerate(pairs):
        pid = pair.get("id") if isinstance(pair.get("id"), str) else "#%d" % idx
        patterns, why = pattern_positions(pair.get("observe_cmd") or [])
        codes = []
        if why:
            codes.append("PATTERN-AMBIG: %s" % why)
        codes += argv_limb(pair, patterns)
        codes += git_limb(pair, repo, base, patterns)
        codes += site_limb(pair, repo, base, annotate_allow, repair_allow)
        if a.execute and not codes:
            codes += execute_limb(pair, work)
        if codes:
            reds += 1
            for c in codes:
                code = c.split(":", 1)[0]
                codes_all[code] = codes_all.get(code, 0) + 1
                print("RED %s %s" % (pid, c))
        elif not a.quiet_ok:
            print("PASS %s argv=ok git-c-first=ok rev-position=ok stated-at=in-set "
                  "stated-text=present" % pid)
    if reds:
        summary = ", ".join("%s=%d" % kv for kv in sorted(codes_all.items()))
        print("LEDGER-PAIRS: FAIL pairs=%d/%d red=%d (%s)"
              % (total - reds, total, reds, summary))
        return 1
    print("LEDGER-PAIRS: PASS pairs=%d/%d" % (total, total))
    return 0


if __name__ == "__main__":
    sys.exit(main())
