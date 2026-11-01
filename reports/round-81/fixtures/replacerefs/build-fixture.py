#!/usr/bin/env python3
r"""Round-81 replace-ref fixture builder — completes the round-80
`reports/round-80/fixtures/junk-ledgers/junk-replacerefs.json` template into a
real, graded fixture (the round-80 verifier spot-check's routed note 5: the
committed bytes are a template with `<40-hex ...>` placeholders and no
`observe.line`; "The committed receipts' runs used a completed copy").

Why the completed fixture must set its stated values to the SHADOWED content:
the replace-ref bypass is that a ledger's observations are read through
`refs/replace` — so a ledger whose stated text matches the shadowed view of the
base commit is blessed by the unhardened guard even though it states a lie
about the true committed bytes. The builder stages exactly that:

  good commit   probe.txt: "count 5"
  evil commit   probe.txt: "count 999"
  git replace   <good> -> <evil>   (refs/replace/heads fills with the mapping)
  ledger        observe {op: line, rev: <good>, path: probe.txt, line: 1,
                         pattern: ^(.+)$}; stated "count 999"

Then it grades the completed ledger twice, from committed bytes only:
  old bytes  (git show <old-rev>:tools/ledger-token-guard.py, the round-79
             unhardened guard)  -> exit 0, `PASS pairs=1`  (the lie blessed —
             the red-before re-derived)
  hardened bytes (<hard-rev>)    -> exit 2, `REFUSED --repo carries
             refs/replace entries ...`  (the refusal re-derived)

Prints a receipt with both verdict lines. Exits 0 when both behave as
recorded; 1 on any behavioral miss; 2 on input errors with the stable
`REPLACEREFS-ERROR` label, no traceback. Everything under --work is the
caller's scratch; nothing in the lane repo is touched. Fixture writes pin
newline semantics (lesson R80-M1) and the fixture repo's git env carries both
identities (lesson R80-M2).
"""
import argparse
import hashlib
import os
import re
import shutil
import subprocess
import sys

LABEL = "REPLACEREFS-ERROR"
OLD_SHA = "504c51c6fa73c0b5418c1b1ad734be926f43ed355832d5796a298af040dd7964"  # r79 bytes


def run(argv, env=None, inp=None, cwd=None):
    return subprocess.run(argv, capture_output=True, env=env, input=inp, cwd=cwd)


def out(r):
    return (r.stdout or b"").decode("utf-8", "replace") + \
           (r.stderr or b"").decode("utf-8", "replace")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True, help="lane repo (tool source + template)")
    ap.add_argument("--old-rev", required=True, help="rev holding the r79 guard bytes")
    ap.add_argument("--hard-rev", required=True, help="rev holding the hardened guard bytes")
    ap.add_argument("--template", default="reports/round-80/fixtures/junk-ledgers/junk-replacerefs.json")
    ap.add_argument("--work", required=True)
    args = ap.parse_args()
    for rev in (args.old_rev, args.hard_rev):
        if not re.fullmatch(r"[0-9a-f]{40}", rev):
            sys.stderr.write("%s: %r is not 40-hex\n" % (LABEL, rev))
            return 2
    r = run(["git", "-C", args.repo, "show", "%s:%s" % (args.old_rev, "tools/ledger-token-guard.py")])
    if r.returncode != 0:
        sys.stderr.write("%s: cannot read old guard at %s: %s\n" % (LABEL, args.old_rev, out(r).strip()))
        return 2
    old_bytes = r.stdout
    if hashlib.sha256(old_bytes).hexdigest() != OLD_SHA:
        sys.stderr.write("%s: old guard at %s is not the r79 bytes (%s...)\n"
                         % (LABEL, args.old_rev, OLD_SHA[:12]))
        return 2
    tmpl_path = os.path.join(args.repo, args.template)
    r = run(["git", "-C", args.repo, "show", "%s:%s" % (args.hard_rev, args.template)])
    if r.returncode != 0:
        sys.stderr.write("%s: cannot read template at %s: %s\n" % (LABEL, args.hard_rev, out(r).strip()))
        return 2
    template = r.stdout.decode("utf-8")

    work = os.path.abspath(args.work)
    fxrepo = os.path.join(work, "fixture-repo")
    if os.path.exists(fxrepo):
        shutil.rmtree(fxrepo, ignore_errors=True)
    env = dict(os.environ)
    env.update({"GIT_AUTHOR_NAME": "fx", "GIT_AUTHOR_EMAIL": "fx@invalid",
                "GIT_COMMITTER_NAME": "fx", "GIT_COMMITTER_EMAIL": "fx@invalid",
                "GIT_CONFIG_GLOBAL": os.devnull, "GIT_CONFIG_NOSYSTEM": "1"})

    def git(*a, check=True):
        r = run(["git", "-C", fxrepo] + list(a), env=env)
        if check and r.returncode != 0:
            sys.stderr.write("%s: git %s failed: %s\n" % (LABEL, a[0], out(r).strip()))
            sys.exit(2)
        return r

    os.makedirs(fxrepo, exist_ok=True)
    git("init", "-q")
    revs = {}
    for name, text in (("good", "count 5"), ("evil", "count 999")):
        with open(os.path.join(fxrepo, "probe.txt"), "w", encoding="utf-8", newline="") as fh:
            fh.write(text + "\n")
        git("add", "probe.txt")
        git("commit", "-q", "-m", name)
        revs[name] = git("rev-parse", "HEAD").stdout.decode().strip()
    good, evil = revs["good"], revs["evil"]
    if good == evil:
        sys.stderr.write("%s: fixture commits collapsed\n" % LABEL)
        return 2
    git("reset", "-q", "--hard", good)
    git("replace", "-f", good, evil)
    reps = git("for-each-ref", "refs/replace/").stdout.decode().strip()
    if good not in reps:
        sys.stderr.write("%s: replace ref not installed\n" % LABEL)
        return 2

    # complete the template: fill both placeholders, add observe.line, and set
    # the stated values to the SHADOWED view (the bypass shape the receipts graded)
    completed = (template
                 .replace("<40-hex head of a fixture repo carrying refs/replace entries>", good)
                 .replace("<same 40-hex>", good))
    import json
    try:
        doc = json.loads(completed)
    except ValueError as exc:
        sys.stderr.write("%s: completed template does not parse: %s\n" % (LABEL, exc))
        return 2
    pair = doc["pairs"][0]
    pair["observe"]["line"] = 1
    pair["stated_text"] = "count 999"
    pair["stated_parse"] = "count (\\d+)"
    pair["observed_at_base"] = "count 999"
    ledger_path = os.path.join(work, "junk-replacerefs.completed.json")
    with open(ledger_path, "w", encoding="utf-8", newline="") as fh:
        fh.write(json.dumps(doc, indent=1, ensure_ascii=False) + "\n")

    old_tool = os.path.join(work, "guard-r79.py")
    with open(old_tool, "wb") as fh:
        fh.write(old_bytes)  # binary copy, byte-pinned (lesson R80-M1)
    hard_tool = os.path.join(args.repo, "tools", "ledger-token-guard.py")

    gd = os.path.join(work, "grade-old")
    os.makedirs(gd, exist_ok=True)
    r = run([sys.executable, "-B", old_tool, "--ledger", ledger_path,
             "--repo", fxrepo, "--base", good, "--work", gd], env=env)
    old_text = out(r)
    old_pass = (r.returncode == 0 and "PASS pairs=1" in old_text)
    print("old bytes  (r79, %s...) -> exit=%d %s"
          % (OLD_SHA[:12], r.returncode,
             [ln for ln in old_text.splitlines() if ln.startswith("LEDGER-TOKEN-GUARD")]
             or ["<no verdict>"]))
    print("  command: python -B <guard-r79.py> --ledger junk-replacerefs.completed.json --repo <fixture-repo> --base %s --work <scratch>" % good[:12])

    gd2 = os.path.join(work, "grade-hard")
    os.makedirs(gd2, exist_ok=True)
    r = run([sys.executable, "-B", hard_tool, "--ledger", ledger_path,
             "--repo", fxrepo, "--base", good, "--work", gd2], env=env)
    hard_text = out(r)
    hard_refused = (r.returncode == 2 and "refs/replace" in hard_text)
    print("hard bytes (%s...) -> exit=%d %s"
          % (hashlib.sha256(open(hard_tool, "rb").read()).hexdigest()[:12], r.returncode,
             [ln for ln in hard_text.splitlines() if ln.startswith("LEDGER-TOKEN-GUARD")]
             or ["<no verdict>"]))
    print("  command: python -B tools/ledger-token-guard.py --ledger junk-replacerefs.completed.json --repo <fixture-repo> --base %s --work <scratch>" % good[:12])
    print("REPLACEREFS-FIXTURE: %s"
          % ("PASS (old PASS pairs=1 / hardened REFUSED refs/replace)"
             if old_pass and hard_refused else "FAIL"))
    return 0 if (old_pass and hard_refused) else 1


if __name__ == "__main__":
    sys.exit(main())
