#!/usr/bin/env python3
"""noop-killer.py — round-79 O-seat fixture that kills the cheapest no-work /
stub-print attacks on tools/ledger-token-guard.py.

Attack class under test (QUALITY 25 J4/J4b, QUALITY 28):
  A1 canned --selftest : guard prints the expected receipt lines and exits 0
                         without building any fixture or running any scenario.
  A2 echo/lookup guard : guard never observes committed bytes; it echoes the
                         ledger's stated_token (or a verdict looked up from a
                         table of committed fixture hashes).

Kill principle (run-time salted driver-side oracle):
  The driver generates a FRESH nonce token per run, writes it into an isolated
  fixture repository it commits itself, and re-derives the actual observation
  independently (its own `git show <base>:probe.txt` + parse). The guard's
  output must echo the observed token per pair; the driver asserts equality
  with its own oracle. A printer/echo/lookup stub cannot know a nonce that
  did not exist when it was written.

Contract required of the real guard (flag names reconciled at integration via
--guard-cmd templates; behaviour is what is graded):

  BATCH   <guard> --ledger L --base B --work W --repo R
            exit 0 = all pairs green; exit 1 = observed mismatch/rejection;
            exit 2 = refused (mutable revision / interpreter grammar / bad input)
            stdout: one line per pair  "pair <id> observed <token>"
                     plus verdict line  "GUARD: PASS ..." / "GUARD: FAIL ..."

  SELFTEST <guard> --selftest --work W
            exit 0, and under W it MUST leave behind:
              - the fixture repository/repositories it built (with commits), and
              - selftest-manifest.json: [{"scenario","fixture_commit","repo_dir",
                "ledger_path","pair_id","observed_token","expect_exit"}]
            The killer re-derives every observed_token from the left-behind
            committed bytes with its own oracle. No fixtures + no manifest =
            canned receipt = killed, whatever was printed.

Usage:
  python3 -B noop-killer.py --guard-cmd '<guard> --ledger {ledger} --base {base} --work {work}' \
      [--selftest-cmd '<guard> --selftest --work {work}'] [--keep-scratch]
  python3 -B noop-killer.py --demo     # run the two simulated cheapest attacks
"""
import argparse
import hashlib
import json
import os
import re
import secrets
import shutil
import subprocess
import sys
import tempfile

PROBE_PATH = "probe.txt"
TOKEN_RE = re.compile(r"^token: (.+)$", re.M)
EXPECTED_GREEN_EXIT = 0


def sh(args, cwd=None, env=None):
    e = dict(os.environ)
    e.update({"GIT_AUTHOR_NAME": "noop-killer", "GIT_AUTHOR_EMAIL": "nk@example.invalid",
              "GIT_COMMITTER_NAME": "noop-killer", "GIT_COMMITTER_EMAIL": "nk@example.invalid",
              "GIT_CONFIG_NOSYSTEM": "1", "HOME": tempfile.gettempdir()})
    if env:
        e.update(env)
    return subprocess.run(args, cwd=cwd, env=e, capture_output=True, text=True,
                          timeout=60)


class FixtureRepo:
    """Isolated fixture repository with a verified root (host-guard rule)."""

    def __init__(self, root):
        self.root = root
        os.makedirs(root, exist_ok=True)
        r = sh(["git", "init", "-q", "-b", "main", root])
        assert r.returncode == 0, r.stderr
        top = subprocess.run(["git", "rev-parse", "--show-toplevel"],
                             capture_output=True, text=True, cwd=root)
        assert top.returncode == 0 and os.path.realpath(top.stdout.strip()) == \
            os.path.realpath(root), "fixture root mismatch: %r" % top.stdout

    def commit_probe(self, token):
        with open(os.path.join(self.root, PROBE_PATH), "w") as f:
            f.write("calibration probe\ntoken: %s\n" % token)
        sh(["git", "add", PROBE_PATH], cwd=self.root)
        r = sh(["git", "commit", "-q", "-m", "probe"], cwd=self.root)
        assert r.returncode == 0, r.stderr
        return sh(["git", "rev-parse", "HEAD"], cwd=self.root).stdout.strip()


def oracle_observed(repo_root, base):
    """Driver-side independent re-derivation: read committed bytes only."""
    r = sh(["git", "show", "%s:%s" % (base, PROBE_PATH)], cwd=repo_root)
    assert r.returncode == 0, r.stderr
    m = TOKEN_RE.search(r.stdout)
    assert m, "oracle could not parse token"
    return m.group(1)


def write_ledger(path, base, pairs):
    doc = {"round": 79, "claim": "O", "base": base, "pairs": pairs}
    with open(path, "w") as f:
        json.dump(doc, f, indent=1)


def pair(pid, stated, observed_at_base, observe):
    return {"id": pid, "stated_token": stated, "observed_at_base": observed_at_base,
            "observe": observe}


def run_batch(guard_cmd, ledger, base, work, repo):
    cmd = guard_cmd.format(ledger=ledger, base=base, work=work, repo=repo)
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=60)
    observed = {}
    for line in r.stdout.splitlines():
        m = re.match(r"pair\s+(\S+)\s+observed\s+(\S+)", line.strip())
        if m:
            observed[m.group(1)] = m.group(2)
    return r.returncode, observed, r.stdout + r.stderr


def verdict(label, ok, detail=""):
    print("%s %-46s %s" % ("GUARD-OK " if ok else "CAUGHT   ", label, detail))
    return ok


def kill_run(guard_cmd, selftest_cmd, scratch):
    """Run the kill battery. Returns (all_ok, rows)."""
    rows = []

    def rec(label, ok, detail=""):
        rows.append((label, ok, detail))
        return verdict(label, ok, detail)

    actual = "n-" + secrets.token_hex(8)          # fresh nonce: unknowable pre-run
    stated = "S884-stated-decoy"                   # honest record: stated != actual

    # -- green + four mutants, each a separate ledger over the same base ------
    fx = FixtureRepo(os.path.join(scratch, "fixture-repo"))
    base = fx.commit_probe(actual)

    ledgers = os.path.join(scratch, "ledgers")
    os.makedirs(ledgers, exist_ok=True)

    observe_ok = ["git", "show", "%s:%s" % (base, PROBE_PATH), "|parse", TOKEN_RE.pattern]
    cases = []
    g = os.path.join(ledgers, "green.json")
    write_ledger(g, base, [pair("G", stated, actual, observe_ok)])
    cases.append(("green", g, EXPECTED_GREEN_EXIT, actual, True))
    m1 = os.path.join(ledgers, "m1-stated-eq-actual.json")
    write_ledger(m1, base, [pair("M1", actual, actual, observe_ok)])   # stated==actual
    cases.append(("m1-stated-eq-actual", m1, 1, actual, False))
    m2 = os.path.join(ledgers, "m2-observed-tampered.json")
    write_ledger(m2, base, [pair("M2", stated, "tampered-not-" + actual, observe_ok)])
    cases.append(("m2-observed-tampered", m2, 1, actual, False))
    m3 = os.path.join(ledgers, "m3-constant-printer.json")
    write_ledger(m3, base, [pair("M3", stated, actual,
                                ["python3", "-c", "import os;print(str('x'));assert os.sep"])])
    cases.append(("m3-constant-printer", m3, 2, None, False))
    m4 = os.path.join(ledgers, "m4-mutable-revision.json")
    write_ledger(m4, base, [pair("M4", stated, actual,
                                ["git", "show", "main:%s" % PROBE_PATH, "|parse",
                                 TOKEN_RE.pattern])])                # branch, not 40-hex
    cases.append(("m4-mutable-revision", m4, 2, None, False))

    ok_all = True
    for name, ledger, want_exit, want_token, want_green in cases:
        work = os.path.join(scratch, "work-" + name)
        code, observed, raw = run_batch(guard_cmd, ledger, base, work, fx.root)
        detail = "exit=%d want=%d" % (code, want_exit)
        ok = code == want_exit
        if want_green:
            got = observed.get("G")
            oracle = oracle_observed(fx.root, base)
            ok = ok and got == oracle == want_token
            detail += " observed=%r oracle=%r" % (got, oracle)
        rec("batch:%s" % name, ok, detail)
        ok_all = ok_all and ok
        with open(os.path.join(scratch, "raw-batch-%s.txt" % name), "w") as f:
            f.write("$ %s\n%s" % (guard_cmd.format(ledger=ledger, base=base, work=work, repo=fx.root), raw))

    # -- worktree-mutation cross-check: a guard reading the worktree, not the -
    # -- commit, must disagree with the committed-bytes oracle ----------------
    with open(os.path.join(fx.root, PROBE_PATH), "a") as f:
        f.write("token: worktree-poison-%s\n" % secrets.token_hex(4))
    g2 = os.path.join(ledgers, "green-after-poison.json")
    write_ledger(g2, base, [pair("G", stated, actual, observe_ok)])
    work = os.path.join(scratch, "work-poison")
    code, observed, raw = run_batch(guard_cmd, g2, base, work, fx.root)
    oracle = oracle_observed(fx.root, base)
    got = observed.get("G")
    rec("batch:worktree-poison(oracle=committed bytes)", got == oracle == actual,
        "exit=%d observed=%r oracle=%r (poisoned worktree must not leak)" % (code, got, oracle))
    ok_all = ok_all and (got == oracle == actual)
    sh(["git", "checkout", "-q", "--", PROBE_PATH], cwd=fx.root)

    # -- selftest: fixtures + manifest must be left behind; tokens re-derived -
    if selftest_cmd:
        work = os.path.join(scratch, "work-selftest")
        os.makedirs(work, exist_ok=True)
        cmd = selftest_cmd.format(work=work)
        r = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=120)
        manifest_path = os.path.join(work, "selftest-manifest.json")
        if not os.path.exists(manifest_path):
            rec("selftest:manifest-left-behind", False,
                "no selftest-manifest.json under --work; canned receipt cannot be re-derived")
            ok_all = False
        else:
            manifest = json.load(open(manifest_path))
            okm = True
            for row in manifest:
                rd = os.path.join(work, row["repo_dir"])
                try:
                    oracle = oracle_observed(rd, row["fixture_commit"])
                except Exception as exc:  # noqa: BLE001
                    okm = False
                    rec("selftest:rederive:%s" % row.get("scenario", "?"), False,
                        "oracle error %s" % exc)
                    continue
                good = oracle == row["observed_token"]
                okm = okm and good
            rec("selftest:every-observed-token-rederived", okm,
                "%d scenarios, exit=%d" % (len(manifest), r.returncode))
            ok_all = ok_all and okm and r.returncode == 0
            with open(os.path.join(scratch, "raw-selftest.txt"), "w") as f:
                f.write("$ %s\n%s%s" % (cmd, r.stdout, r.stderr))
    else:
        print("note: no --selftest-cmd given; selftest legs skipped")
    return ok_all, rows


def demo(scratch):
    """Run the two simulated cheapest attacks; both must be killed."""
    stage = os.path.dirname(os.path.abspath(__file__))
    stub = os.path.join(stage, "stub-guards.py")
    results = {}
    for name in ("canned-selftest", "echo-lookup"):
        sub = os.path.join(scratch, "demo-" + name)
        os.makedirs(sub, exist_ok=True)
        guard_cmd = "python3 -B %s %s --ledger {ledger} --base {base} --work {work}" % (stub, name)
        selftest_cmd = "python3 -B %s %s --selftest --work {work}" % (stub, name)
        print("=== simulated attack: %s ===" % name)
        ok, _ = kill_run(guard_cmd, selftest_cmd, sub)
        results[name] = ok
    return results


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--guard-cmd")
    ap.add_argument("--selftest-cmd")
    ap.add_argument("--work", default=os.environ.get("TMPDIR", "/tmp"))
    ap.add_argument("--keep-scratch", action="store_true")
    ap.add_argument("--demo", action="store_true")
    args = ap.parse_args()

    scratch = tempfile.mkdtemp(prefix="noop-killer-", dir=args.work)
    print("# scratch: %s" % scratch)
    try:
        if args.demo:
            results = demo(scratch)  # values: True == stub survived every leg
            survived = [k for k, v in results.items() if v]
            print("DEMO VERDICT: %s" % ("ALL SIMULATED ATTACKS CAUGHT ON EVERY LEG"
                                        if not survived
                                        else "FIXTURE BROKEN, attack survived: %s" % survived))
            return 0 if not survived else 1
        if not args.guard_cmd:
            ap.error("--guard-cmd required (or --demo)")
        ok, _ = kill_run(args.guard_cmd, args.selftest_cmd, scratch)
        print("KILL VERDICT: %s" % ("GUARD SURVIVES BATTERY" if ok else "GUARD KILLED (or incomplete)"))
        return 0 if ok else 1
    finally:
        if not args.keep_scratch:
            shutil.rmtree(scratch, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main())
