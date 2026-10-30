#!/usr/bin/env python3
r"""reference ledger-token guard — fixture implementation of the contract.

Not the production tools/ledger-token-guard.py.  Exists so the acceptance
counter can be built and self-tested before the production guard lands; the
counter grades whatever bytes sit at <lands>:tools/ledger-token-guard.py.
"""
import argparse
import json
import os
import re
import subprocess
import sys

READONLY_SUB = {"show", "grep", "cat-file", "ls-tree", "rev-parse", "log",
                "diff", "ls-files", "rev-list", "merge-base"}
PRINTERS = {"echo", "printf", "true", "false", "yes"}
INTERPRETERS = {"python", "python2", "python3", "pypy", "pypy3", "sh", "bash",
                "zsh", "dash", "ksh", "fish", "csh", "tcsh", "perl", "node",
                "nodejs", "ruby", "php", "awk", "gawk", "mawk", "sed", "env",
                "xargs", "eval", "exec", "nice", "nohup", "time", "busybox"}
SHELL_META = ("|", "&", ";", "<", ">", "`", "$(", "\n", "\r")
MUTABLE = ("HEAD", "main", "master", "@{", "refs/")
OBS_TIMEOUT = 30
OUT_CAP = 1000000


def _subcommand(argv):
    args = argv[1:]
    i = 0
    while i < len(args):
        a = args[i]
        if a == "-C":
            i += 2
            continue
        if a.startswith("-"):
            i += 1
            continue
        return a
    return None


def grammar_problem(argv, base):
    if not isinstance(argv, list) or not argv:
        return "empty observe_cmd"
    exe = os.path.basename(str(argv[0]))
    if exe in INTERPRETERS:
        return "interpreter %r is refused" % exe
    if exe in PRINTERS:
        return "constant-printer %r is refused" % exe
    if exe != "git":
        return "executable %r is outside the read-only git grammar" % exe
    for el in argv[1:]:
        el = str(el)
        if any(m in el for m in SHELL_META):
            return "shell metacharacter in observe argv element %r" % el
        if any(el == mv or el.startswith(mv) for mv in MUTABLE):
            return "mutable revision %r is refused" % el
    sub = _subcommand(argv)
    if sub not in READONLY_SUB:
        return "git subcommand %r is not in the read-only set" % sub
    pinned = any(str(el) == base or str(el).startswith(base + ":")
                 for el in argv[1:])
    if not pinned:
        return "observation is not pinned at --base %s" % base[:12]
    return None


def run_observe(argv, base, repo):
    cmd = [str(a).replace("{base}", base) for a in argv]
    try:
        r = subprocess.run(cmd, cwd=repo, capture_output=True, text=True,
                           timeout=OBS_TIMEOUT)
    except subprocess.TimeoutExpired:
        return None, "observe timed out after %ds" % OBS_TIMEOUT
    if len(r.stdout) > OUT_CAP:
        return None, "observe output exceeds the %d-byte cap" % OUT_CAP
    if r.returncode != 0:
        return None, "observe exited %d" % r.returncode
    return r.stdout, None


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--ledger")
    ap.add_argument("--repo")
    ap.add_argument("--base")
    ap.add_argument("--work")
    ap.add_argument("--emit")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args(argv)
    if args.selftest:
        return selftest(args.work)
    missing = [name for name in ("ledger", "repo", "base", "work")
               if not getattr(args, name)]
    if missing:
        print("LEDGER-GUARD-79: FAIL (refused: missing %s)"
              % ", ".join("--" + m for m in missing))
        return 2
    if not re.fullmatch(r"[0-9a-f]{40}", args.base):
        print("LEDGER-GUARD-79: FAIL (refused: --base must be 40 hex)")
        return 2
    if not os.path.isdir(args.repo):
        print("LEDGER-GUARD-79: FAIL (refused: --repo %s is not a directory)"
              % args.repo)
        return 2
    work = os.path.abspath(args.work)
    os.makedirs(work, exist_ok=True)
    try:
        ledger = json.load(open(args.ledger, encoding="utf-8"))
    except (OSError, ValueError) as exc:
        print("LEDGER-GUARD-79: FAIL (refused: ledger unreadable: %s)" % exc)
        return 2
    pairs = ledger.get("pairs")
    if not isinstance(pairs, list) or not pairs:
        print("LEDGER-GUARD-79: FAIL (refused: ledger carries no pairs)")
        return 2

    grammar = []
    for pair in pairs:
        if not isinstance(pair, dict) or not isinstance(
                pair.get("observe_cmd"), list):
            grammar.append("PAIR %s: malformed pair (no observe_cmd)"
                           % (pair.get("id") if isinstance(pair, dict)
                              else "?"))
            continue
        subbed = [str(a).replace("{base}", args.base)
                  for a in pair["observe_cmd"]]
        why = grammar_problem(subbed, args.base)
        if why:
            grammar.append("PAIR %s: %s" % (pair.get("id"), why))
    if grammar:
        print("LEDGER-GUARD-79: FAIL (refused: %d grammar problem(s)) "
              "%s" % (len(grammar), grammar[:4]))
        return 2

    results = []
    problems = 0
    for pair in pairs:
        pid = pair.get("id")
        stated = None
        m = re.search(pair.get("stated_parse", ""), pair.get("stated_text", ""))
        if m:
            stated = m.group(1)
        out, why = run_observe(pair["observe_cmd"], args.base, args.repo)
        if out is None:
            results.append({"id": pid, "observed": None, "stated": stated,
                            "status": "unobservable: %s" % why})
            problems += 1
            continue
        m = re.search(pair.get("parse", ""), out)
        if not m:
            results.append({"id": pid, "observed": None, "stated": stated,
                            "status": "unparseable observation"})
            problems += 1
            continue
        observed = m.group(1)
        recorded = str(pair.get("observed_at_base"))
        if recorded != observed:
            results.append({"id": pid, "observed": observed, "stated": stated,
                            "status": "obs-mismatch"})
            problems += 1
            continue
        if stated is not None and stated == observed:
            results.append({"id": pid, "observed": observed, "stated": stated,
                            "status": "not-red"})
            problems += 1
            continue
        results.append({"id": pid, "observed": observed, "stated": stated,
                        "status": "ok"})
    if args.emit:
        with open(args.emit, "w", encoding="utf-8") as fh:
            json.dump({"verdict": "FAIL" if problems else "PASS",
                       "pairs": results}, fh, indent=1)
            fh.write("\n")
    if problems:
        print("LEDGER-GUARD-79: FAIL pairs=%d problems=%d"
              % (len(pairs), problems))
        for pair, res in zip(pairs, results):
            if res["status"] == "obs-mismatch":
                print("PAIR %s: OBS_MISMATCH recorded=%r actual=%r"
                      % (res["id"], str(pair.get("observed_at_base")),
                         res["observed"]))
            elif res["status"] == "not-red":
                print("PAIR %s: NOT_RED token=%r" % (res["id"], res["stated"]))
            else:
                print("PAIR %s: %s" % (res["id"], res["status"]))
        return 1
    print("LEDGER-GUARD-79: PASS pairs=%d" % len(pairs))
    return 0


def selftest(work):
    repo = os.path.join(work, "guard-selftest-repo")
    os.makedirs(repo, exist_ok=True)
    subprocess.run(["git", "-C", repo, "init", "-q"], check=True)
    for rel, text in {"KEYS.txt": "k1\nk2\n",
                      "LOG.md": "# a\n# b\ntotal: 2\n"}.items():
        with open(os.path.join(repo, rel), "w", encoding="utf-8") as fh:
            fh.write(text)
    subprocess.run(["git", "-C", repo, "add", "-A"], check=True)
    subprocess.run(["git", "-C", repo, "-c", "user.name=fixture",
                    "-c", "user.email=fixture@example.invalid",
                    "commit", "-q", "-m", "selftest"], check=True)
    base = subprocess.run(["git", "-C", repo, "rev-parse", "HEAD"],
                          capture_output=True, text=True,
                          check=True).stdout.strip()
    ledger = {"round": 79, "claim": "O", "base": base, "pairs": [{
        "id": "G1", "disposition": "ANNOTATE",
        "stated_at": "LOG.md:1", "stated_text": "# a",
        "stated_parse": r"^# (.+)$",
        "observe_cmd": ["git", "-C", ".", "grep", "-c", "-E", "^k",
                        "{base}", "--", "KEYS.txt"],
        "parse": r":([0-9]+)$", "expected_after": "1",
        "observed_at_base": "2"}]}
    lp = os.path.join(work, "guard-selftest-ledger.json")
    with open(lp, "w", encoding="utf-8") as fh:
        json.dump(ledger, fh)
    ok = True
    c = main(["--ledger", lp, "--repo", repo, "--base", base, "--work", work])
    print("case green exit=%d" % c)
    ok = ok and c == 0
    ledger["pairs"][0]["observed_at_base"] = "3"
    with open(lp, "w", encoding="utf-8") as fh:
        json.dump(ledger, fh)
    c = main(["--ledger", lp, "--repo", repo, "--base", base, "--work", work])
    print("case obs-mismatch exit=%d" % c)
    ok = ok and c == 1
    ledger["pairs"][0]["observed_at_base"] = "2"
    ledger["pairs"][0]["stated_parse"] = r"total: (\d+)"
    ledger["pairs"][0]["stated_text"] = "total: 2"
    ledger["pairs"][0]["observe_cmd"] = ["git", "-C", ".", "grep", "-c",
                                         "-E", "^#", "{base}", "--",
                                         "LOG.md"]
    ledger["pairs"][0]["parse"] = r":([0-9]+)$"
    with open(lp, "w", encoding="utf-8") as fh:
        json.dump(ledger, fh)
    c = main(["--ledger", lp, "--repo", repo, "--base", base, "--work", work])
    print("case not-red exit=%d" % c)
    ok = ok and c == 1
    ledger["pairs"][0]["observe_cmd"] = ["echo", "2"]
    with open(lp, "w", encoding="utf-8") as fh:
        json.dump(ledger, fh)
    c = main(["--ledger", lp, "--repo", repo, "--base", base, "--work", work])
    print("case grammar exit=%d" % c)
    ok = ok and c == 2
    print("SELFTEST: %s green+obs-mismatch+not-red+grammar"
          % ("4/4" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
