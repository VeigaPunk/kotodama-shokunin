#!/usr/bin/env python3
"""MutRevision (round-79 W1) mutable-revision and option-injection mutant driver.

Probes the round-77 ledger-check detector (ConnClaimsCounter accept-ca.py,
sha256 ac2bc93d02932464f9ee43222ffe1d06dd5bf1a0e68fd38bd94e10a991489b2e)
with single-pair mutants of the pristine round-77 probe ledger
(probe-real-ledger.pristine.json, sha256 b7509d2b...). Each run mutates
pair D07 only. Every run uses the lane read-only (git clone --no-checkout
by the detector) and writes only under SCRATCH and STAGE.

Usage: python3 -B driver.py
Writes: STAGE/raw/<id>.txt, STAGE/summary.tsv, STAGE/lane-state.txt
Fixture repos are created here with a verified toplevel; no lane write.
"""
import copy
import hashlib
import json
import os
import shlex
import shutil
import subprocess
import sys

SCRATCH = "/fast/scratch/hyaku/kotodama-r79/MutRevision"
LANE = "/home/vgpnk/Projects/shokunin/kotodama-shokunin"
STAGE = LANE + "/.ufo/waves/round-79/w1/stage/MutRevision"
BASE = "211f9526800906e0c585d878d265c37e5e090c15"
DETECTOR_SRC = LANE + "/.ufo/waves/round-77/w2/stage/ConnClaimsCounter/accept-ca.py"
DETECTOR_SHA = "ac2bc93d02932464f9ee43222ffe1d06dd5bf1a0e68fd38bd94e10a991489b2e"
PROBE_SRC = LANE + "/.ufo/waves/round-77/w2/stage/MutCaLedger/probe-real-ledger.pristine.json"
PROBE_SHA = "b7509d2b0980f8c5824c417a8359c8f7107d3de6236cf486ac058947915d0704"
GIT = shutil.which("git") or "/usr/bin/git"
PAIR = "D07"

FIX = os.path.join(SCRATCH, "fixtures")
WORK = os.path.join(SCRATCH, "work")
LEDG = os.path.join(SCRATCH, "ledgers")
MARK_WRAP = os.path.join(SCRATCH, "WRAPPER-MARK.txt")
MARK_DIFF = os.path.join(SCRATCH, "PAGER-MARK.txt")
GIT_ENV = {
    "PATH": os.environ.get("PATH", "/usr/bin:/bin"),
    "HOME": SCRATCH,
    "TMPDIR": SCRATCH,
    "GIT_AUTHOR_NAME": "mutrev", "GIT_AUTHOR_EMAIL": "mutrev@example.invalid",
    "GIT_COMMITTER_NAME": "mutrev", "GIT_COMMITTER_EMAIL": "mutrev@example.invalid",
    "GIT_CONFIG_GLOBAL": "/dev/null", "GIT_CONFIG_NOSYSTEM": "1",
}


def sha256(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def run(argv, **kw):
    kw.setdefault("capture_output", True)
    kw.setdefault("text", True)
    kw.setdefault("timeout", 600)
    return subprocess.run(argv, **kw)


def fixture_repo(name, versions):
    """Commit each LOG.md version in order on main; assert the root."""
    d = os.path.join(FIX, name)
    shutil.rmtree(d, ignore_errors=True)
    os.makedirs(d)
    run([GIT, "init", "-q", "-b", "main", d], check=True, env=GIT_ENV)
    top = run([GIT, "-C", d, "rev-parse", "--show-toplevel"], env=GIT_ENV).stdout.strip()
    assert top == d, "fixture root mismatch: %r != %r" % (top, d)
    for i, body in enumerate(versions):
        with open(os.path.join(d, "LOG.md"), "w") as fh:
            fh.write(body)
        run([GIT, "-C", d, "add", "LOG.md"], check=True, env=GIT_ENV)
        run([GIT, "-C", d, "commit", "-q", "-m", "v%d" % i], check=True, env=GIT_ENV)
    head = run([GIT, "-C", d, "rev-parse", "HEAD"], env=GIT_ENV).stdout.strip()
    return d, head


def make_fixtures():
    os.makedirs(FIX, exist_ok=True)
    g1, h1 = fixture_repo("optrepo1", ["# Round one entry\nbody text\n",
                                       "# Different heading\nother bytes\n"])
    g2, h2 = fixture_repo("optrepo2", ["# Heading A\n# Heading B\nbody\n"])
    # wrapper named `git` whose basename passes the observe allowlist
    wd = os.path.join(FIX, "bin")
    os.makedirs(wd, exist_ok=True)
    wrap = os.path.join(wd, "git")
    with open(wrap, "w") as fh:
        fh.write("#!/bin/sh\necho \"WRAPPER RAN argv=$*\" >> %s\nexec %s \"$@\"\n"
                 % (MARK_WRAP, GIT))
    os.chmod(wrap, 0o755)
    # marker-writing program for diff.external (separated -c control)
    dm = os.path.join(FIX, "pager-marker.sh")
    with open(dm, "w") as fh:
        fh.write("#!/bin/sh\necho \"EXTDIFF RAN argv=$*\" >> %s\n" % MARK_DIFF)
    os.chmod(dm, 0o755)
    return {"optrepo1": (g1, h1), "optrepo2": (g2, h2), "wrapper": wrap, "extdiff": dm}


def mutants(fx):
    g1 = fx["optrepo1"][0]
    g2 = fx["optrepo2"][0]
    gd1 = os.path.join(g1, ".git")
    gd2 = os.path.join(g2, ".git")
    obs = ["git", "-C", ".", "grep", "-c", "-E", "^#", BASE, "--", "LOG.md"]

    def same(o):
        return {"observe_cmd": o, "rederive": shlex.join(o)}

    out = []
    # Group A: rederive-only rev-token swaps (the round-77 single-field method)
    for mid, tok, note in [
        ("A01", "HEAD", "round-77 D07 survivor, reproduce"),
        ("A02", "HEAD~0", "HEAD-family tilde form, not in REV_NAMES"),
        ("A03", "HEAD^^", "HEAD-family caret form, not in REV_NAMES"),
        ("A04", "HEAD@{0}", "reflog form of HEAD"),
        ("A05", "HEAD:LOG.md", "tree-ish:path object spec before --"),
        ("A06", "main~0", "branch with tilde"),
        ("A07", "origin/main", "remote-tracking branch with slash"),
        ("A08", "FETCH_HEAD", "control: mutable name without slash"),
        ("A09", "main", "control: plain branch name (round-77 D06 form)"),
        ("A10", "211f952", "7-hex short sha, digit-first"),
        ("A11", "@{u}", "upstream reflog form"),
        ("A12", "HEAD~1", "REV_NAMES member (inventory)"),
        ("A13", "@~0", "@-family tilde form"),
    ]:
        out.append(dict(id=mid, group="A", field="rederive", note=note,
                        mutate={"rederive": "git -C . grep -c -E '^#' %s -- LOG.md" % tok}))
    # Group B: observe_cmd + rederive (observation provenance and option forms)
    out += [
        dict(id="B01", group="B", field="observe_cmd+rederive", note="HEAD in observe position",
             mutate=same(["git", "-C", ".", "grep", "-c", "-E", "^#", "HEAD", "--", "LOG.md"])),
        dict(id="B02", group="B", field="observe_cmd+rederive",
             note="attached --git-dir= to optrepo2 (HEAD count 2): observed mismatch expected",
             mutate=same(["git", "-C", ".", "--git-dir=" + gd2, "grep", "-c", "-E", "^#", "HEAD", "--", "LOG.md"])),
        dict(id="B03", group="B", field="observe_cmd+rederive",
             note="attached --git-dir= to optrepo1 (HEAD count 1, other bytes): count equal",
             mutate=same(["git", "-C", ".", "--git-dir=" + gd1, "grep", "-c", "-E", "^#", "HEAD", "--", "LOG.md"])),
        dict(id="B04", group="B", field="observe_cmd+rederive",
             note="control: separated --git-dir <path> (exact global match)",
             mutate=same(["git", "-C", ".", "--git-dir", gd1, "grep", "-c", "-E", "^#", "HEAD", "--", "LOG.md"])),
        dict(id="B05", group="B", field="observe_cmd+rederive",
             note="control: separated -c diff.external=<marker> before grep",
             mutate=same(["git", "-C", ".", "-c", "diff.external=" + fx["extdiff"],
                          "grep", "-c", "-E", "^#", BASE, "--", "LOG.md"])),
        dict(id="B06", group="B", field="observe_cmd+rederive",
             note="attached -ccore.quotepath=off before grep (exact -c match misses it)",
             mutate=same(["git", "-C", ".", "-ccore.quotepath=off", "grep", "-c", "-E", "^#", BASE, "--", "LOG.md"])),
        dict(id="B07", group="B", field="observe_cmd+rederive",
             note="attached --namespace=x before grep (exact match misses it)",
             mutate=same(["git", "-C", ".", "--namespace=x", "grep", "-c", "-E", "^#", BASE, "--", "LOG.md"])),
    ]
    # Group C: grep option blanket skip (observe_cmd + rederive)
    out += [
        dict(id="C01", group="C", field="observe_cmd+rederive",
             note="valid no-op grep option --textconv after grep",
             mutate=same(["git", "-C", ".", "grep", "--textconv", "-c", "-E", "^#", BASE, "--", "LOG.md"])),
        dict(id="C02", group="C", field="observe_cmd+rederive",
             note="--open-files-in-pager (no value) after grep; git 2.56 rejects",
             mutate=same(["git", "-C", ".", "grep", "--open-files-in-pager", "-c", "-E", "^#", BASE, "--", "LOG.md"])),
    ]
    # Group D: argv[0] basename check (observe_cmd + rederive)
    out += [
        dict(id="D01", group="D", field="observe_cmd+rederive",
             note="argv[0] = absolute path to a wrapper whose basename is git",
             mutate=same([fx["wrapper"], "-C", ".", "grep", "-c", "-E", "^#", BASE, "--", "LOG.md"])),
        dict(id="D02", group="D", field="observe_cmd+rederive",
             note="control: argv[0] = absolute real git (basename git)",
             mutate=same([GIT, "-C", ".", "grep", "-c", "-E", "^#", BASE, "--", "LOG.md"])),
        dict(id="D03", group="D", field="observe_cmd+rederive",
             note="control: argv[0] = absolute python3 (basename refused)",
             mutate=same(["/usr/bin/python3", "-c", "print(1)"])),
    ]
    # Group E: recorded observed_at_base with NO injection (isolates the compare)
    out += [
        dict(id="E01", group="E", field="observed_at_base",
             note="fabricated observed_at_base '2' (fresh base count is 149), no other change",
             mutate={"observed_at_base": "2"}),
        dict(id="E02", group="E", field="observed_at_base",
             note="control: true fresh base observation '149' (git grep -c at base = 149)",
             mutate={"observed_at_base": "149"}),
    ]
    return out


def build_ledger(mut, fx):
    with open(PROBE_SRC) as fh:
        led = json.load(fh)
    pair = next(p for p in led["pairs"] if p["id"] == PAIR)
    before = copy.deepcopy(pair)
    pair.update(mut["mutate"])
    changed = sorted(k for k in set(before) | set(pair) if before.get(k) != pair.get(k))
    path = os.path.join(LEDG, mut["id"] + ".json")
    os.makedirs(LEDG, exist_ok=True)
    with open(path, "w") as fh:
        json.dump(led, fh, indent=1, ensure_ascii=False)
    return path, changed


def lane_state():
    head = run([GIT, "-C", LANE, "rev-parse", "HEAD"]).stdout.strip()
    st = run([GIT, "-C", LANE, "status", "--porcelain"]).stdout
    return "HEAD=%s status-lines=%d detector-sha=%s probe-sha=%s" % (
        head, len([x for x in st.splitlines() if x.strip()]),
        sha256(DETECTOR_SRC), sha256(PROBE_SRC))


def classify(exit_code, out):
    if exit_code == 0 and "PASS" in out:
        return "ACCEPTED"
    if exit_code == 1 and "FAIL" in out:
        return "REFUSED"
    return "INPUT-ERR(exit=%d)" % exit_code


def main():
    assert sha256(DETECTOR_SRC) == DETECTOR_SHA, "detector sha drift"
    assert sha256(PROBE_SRC) == PROBE_SHA, "probe sha drift"
    os.makedirs(STAGE, exist_ok=True)
    raw_dir = os.path.join(STAGE, "raw")
    os.makedirs(raw_dir, exist_ok=True)
    detector = os.path.join(SCRATCH, "accept-ca.py")
    shutil.copy(DETECTOR_SRC, detector)
    assert sha256(detector) == DETECTOR_SHA
    before = lane_state()
    fx = make_fixtures()
    rows = []
    for mut in mutants(fx):
        ledger, changed = build_ledger(mut, fx)
        work = os.path.join(WORK, mut["id"])
        shutil.rmtree(work, ignore_errors=True)
        os.makedirs(work)
        for m in (MARK_WRAP, MARK_DIFF):
            if os.path.exists(m):
                os.remove(m)
        argv = [sys.executable, "-B", detector, "--ledger-check", ledger,
                "--root", LANE, "--base", BASE, "--work", work]
        p = run(argv, cwd=SCRATCH)
        out = (p.stdout or "") + (p.stderr or "")
        marks = []
        for m in (MARK_WRAP, MARK_DIFF):
            if os.path.exists(m):
                marks.append("%s: %s" % (os.path.basename(m), open(m).read().strip()))
        verdict = classify(p.returncode, out)
        with open(os.path.join(raw_dir, mut["id"] + ".txt"), "w") as fh:
            fh.write("# mutant %s group=%s field=%s changed=%s\n# note: %s\n"
                     % (mut["id"], mut["group"], mut["field"], changed, mut["note"]))
            fh.write("# argv: %s\n" % shlex.join(argv))
            fh.write("# verdict: %s exit=%d\n" % (verdict, p.returncode))
            fh.write("# marks: %s\n" % ("; ".join(marks) if marks else "(none)"))
            fh.write(out)
        problems = [ln for ln in out.splitlines() if ln.startswith(PAIR + ":") or ln.startswith("LEDGER-CHECK")]
        rows.append((mut["id"], mut["group"], ";".join(changed), p.returncode, verdict,
                     "; ".join(marks) if marks else "-", " | ".join(problems[:3])))
        print(mut["id"], verdict, "exit=%d" % p.returncode, " | ".join(problems[:2]))
    with open(os.path.join(STAGE, "summary.tsv"), "w") as fh:
        fh.write("id\tgroup\tchanged\texit\tverdict\tmarks\tproblems\n")
        for r in rows:
            fh.write("\t".join(str(x) for x in r) + "\n")
    after = lane_state()
    with open(os.path.join(STAGE, "lane-state.txt"), "w") as fh:
        fh.write("before: %s\nafter:  %s\nunchanged: %s\n" % (before, after, before == after))
    print("lane unchanged:", before == after)


if __name__ == "__main__":
    main()
