#!/usr/bin/env python3
"""ConnClaimsCounter: Ca observe/rederive argv grammar probes (scratch only).

Calls the staged ACCEPT-CA-77 validator directly on argv lists against a fixture
clone under /fast/scratch/hyaku/kotodama-r77/ConnClaimsCounter/probe/ca-fixture.
observe_problem() returns None when the argv is ACCEPTED, else the refusal text.
"""
import importlib.util
import os
import subprocess

SCR = "/fast/scratch/hyaku/kotodama-r77/ConnClaimsCounter/probe"
COUNTER = "/fast/scratch/hyaku/kotodama-r77/ConnClaimsCounter/ca/accept-ca.py"
REPO = os.path.join(SCR, "ca-fixture", "lane")

spec = importlib.util.spec_from_file_location("acc_ca", COUNTER)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def g(*args):
    return subprocess.run(["git", "-C", REPO, *args], capture_output=True, text=True)


def setup():
    os.makedirs(REPO, exist_ok=True)
    top = g("rev-parse", "--show-toplevel").stdout.strip() if os.path.isdir(
        os.path.join(REPO, ".git")) else ""
    if not top:
        subprocess.run(["git", "-C", REPO, "init", "-q"], check=True)
        top = g("rev-parse", "--show-toplevel").stdout.strip()
    assert os.path.realpath(top) == os.path.realpath(REPO), (top, REPO)
    with open(os.path.join(REPO, "LOG.md"), "w", encoding="utf-8") as fh:
        fh.write("# log\n\nrow A01 entries: 0.\n")
    g("add", "-A")
    g("-c", "user.name=P", "-c", "user.email=p@example.invalid", "commit", "-q",
      "-m", "fixture")
    return g("rev-parse", "HEAD").stdout.strip()


def probe(label, argv):
    res = m.observe_problem(argv, REPO)
    verdict = "ACCEPTED" if res is None else "REFUSED: %s" % res
    print("%-44s %s" % (label, verdict))
    print("    argv=%r" % (argv,))


def main():
    sha = setup()
    print("fixture HEAD (40-hex) =", sha)
    print("fixture mutable branch =", g("rev-parse", "--abbrev-ref", "HEAD").stdout.strip())
    print()
    # control: the grammar the LEDGER text promises
    probe("control: -C, 40-hex rev, -- , path",
          ["git", "-C", REPO, "log", "-1", sha, "--", "LOG.md"])
    # promised `--` before repo-relative paths: omitted
    probe("no `--` before repo-relative path",
          ["git", "-C", REPO, "log", "-1", sha, "LOG.md"])
    # promised immutable 40-hex in revision position: branch name in rev slot
    probe("mutable branch name in rev slot (log)",
          ["git", "-C", REPO, "log", "-1", "master", "--", "LOG.md"])
    probe("mutable branch name in rev slot (show)",
          ["git", "-C", REPO, "show", "master:LOG.md"])
    probe("HEAD~0 relative rev in rev slot (show)",
          ["git", "-C", REPO, "show", "HEAD~0:LOG.md"])
    # no `-C` first: refused (control for the -C rule)
    probe("no -C (control)", ["git", "log", "-1", sha, "--", "LOG.md"])


if __name__ == "__main__":
    main()
