#!/usr/bin/env python3
"""neg-11 — isolated negative control for R8-O11 (defect index 7 = review 26 §3 D7).

Defect: a non-UTF-8 packet file made `phonology-sanity-gate.py` and
`myth-consistency-gate.py` raise an uncaught `UnicodeDecodeError` (traceback,
exit 1 = "findings"), instead of the documented exit 2 "could-not-evaluate".
Repair (this shard): both CLI read boundaries catch `UnicodeDecodeError` and
print one `FINDING G-DATA` line, exit 2.

The control is isolated: payloads and pre-fix gate copies live in a temp
directory (honours TMPDIR; use --scratch when /tmp is saturated), gates run as
subprocesses, no live repository path is written. `--selftest` for the two
repaired gates runs against a copy of tools/gates so the committed fixtures
are not rewritten (review 29 §F1).

Exit codes: 0 all controls pass · 1 any control fails · 2 usage/environment.

Usage:
    python3 reports/round-8/operability/neg-controls/neg-11/neg-11-control.py
    ... --rev e7ca0fa --scratch /some/dir --receipts receipts.json
"""

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", "..", "..", ".."))

PHON = "phonology-sanity-gate.py"
MYTH = "myth-consistency-gate.py"
OTHERS = ["naming-collision-gate.py", "costume-era-consistency-gate.py",
          "lexicon-coverage-audit.py"]

# exact probe bytes used in the filed report; sha256 pinned below
PROBE = ("name: t\n"
         "phonology:\n"
         "  consonants: [p, t, k]\n"
         "  vowels: [a]\n"
         "  phonotactics: (C)V\n"
         "  tones: 0\n"
         "# caf\xe9-probe\n").encode("latin-1")
PROBE_SHA256 = "2d3722282732ba9846887bd5101ab7a7bbbfb385810f48c39629870f8b4175bf"

CLEAN = ("name: probe\n"
         "phonology:\n"
         "  consonants: [p, t, k, m, n, s, l]\n"
         "  vowels: [a, e, i, o, u]\n"
         "  phonotactics: (C)V(C)\n"
         "  tones: 0\n").encode("utf-8")
IPA = ("name: probe\n"
       "phonology:\n"
       "  consonants: [p, t, k, m, n, s, l, \u0272]\n"
       "  vowels: [a, e, i, o, u, \u0259]\n"
       "  phonotactics: (C)V(C)\n"
       "  tones: 0\n").encode("utf-8")

NEW_PHON_MSG = "not UTF-8 text"
NEW_MYTH_MSG = "cannot decode"


def sha256(path):
    with open(path, "rb") as handle:
        return hashlib.sha256(handle.read()).hexdigest()


def run(gate_path, packet_path, timeout=30):
    try:
        proc = subprocess.run([sys.executable, gate_path, packet_path],
                              capture_output=True, text=True, timeout=timeout)
        return {"rc": proc.returncode, "stdout": proc.stdout, "stderr": proc.stderr,
                "timeout": False}
    except subprocess.TimeoutExpired:
        return {"rc": None, "stdout": "", "stderr": "", "timeout": True}


def resolve_scratch(explicit):
    """First writable candidate wins: --scratch, TMPDIR, system temp, ~/.cache.

    The wave can saturate the system temp directory, and the acceptance
    harness runs this control with no arguments, so a full /tmp must not turn
    the control into a crash.
    """
    candidates = []
    if explicit:
        candidates.append(explicit)
    env = os.environ.get("TMPDIR")
    if env:
        candidates.append(env)
    candidates.append(tempfile.gettempdir())
    candidates.append(os.path.join(os.path.expanduser("~"), ".cache",
                                   "neg-11-scratch"))
    for candidate in candidates:
        try:
            os.makedirs(candidate, exist_ok=True)
            probe = os.path.join(candidate, ".neg-11-write-probe")
            with open(probe, "w", encoding="utf-8") as handle:
                handle.write("ok")
            os.unlink(probe)
            return candidate
        except OSError:
            continue
    return None


def main(argv=None):
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument("--rev", default="e7ca0fa",
                        help="git revision for the pre-fix gate bytes (default e7ca0fa)")
    parser.add_argument("--scratch", default=None,
                        help="scratch directory (default: system temp / TMPDIR)")
    parser.add_argument("--receipts", default=None,
                        help="write a JSON receipt to this path")
    args = parser.parse_args(argv)

    if not os.path.isdir(os.path.join(REPO, "tools", "gates")):
        sys.stderr.write("neg-11: repository root not found from %s\n" % HERE)
        return 2

    results = []
    receipt = {"control": "neg-11", "shard": "R8-O11", "defect": "review-26 D7",
               "repo": REPO, "pre_fix_rev": args.rev, "checks": results}

    def check(name, ok, detail):
        results.append({"check": name, "ok": bool(ok), "detail": detail})
        print("%-4s %-46s %s" % ("PASS" if ok else "FAIL", name, detail))

    scratch = resolve_scratch(args.scratch)
    if scratch is None:
        sys.stderr.write("neg-11: no writable scratch directory "
                         "(--scratch, TMPDIR, system temp, ~/.cache all failed)\n")
        return 2
    work = tempfile.mkdtemp(prefix="neg-11-", dir=scratch)
    try:
        probe = os.path.join(work, "probe.yml")
        with open(probe, "wb") as handle:
            handle.write(PROBE)
        clean = os.path.join(work, "clean.yml")
        with open(clean, "wb") as handle:
            handle.write(CLEAN)
        ipa = os.path.join(work, "ipa.yml")
        with open(ipa, "wb") as handle:
            handle.write(IPA)
        missing = os.path.join(work, "absent.yml")

        pre = os.path.join(work, "pre")
        os.makedirs(pre)
        for name in [PHON, MYTH] + OTHERS:
            blob = subprocess.run(["git", "-C", REPO, "show",
                                   "%s:tools/gates/%s" % (args.rev, name)],
                                  capture_output=True)
            if blob.returncode != 0:
                sys.stderr.write("neg-11: git show failed for %s: %s\n"
                                 % (name, blob.stderr.decode("utf-8", "replace").strip()))
                return 2
            with open(os.path.join(pre, name), "wb") as handle:
                handle.write(blob.stdout)
        receipt["pre_fix_sha256"] = {name: sha256(os.path.join(pre, name))
                                     for name in [PHON, MYTH] + OTHERS}
        receipt["worktree_sha256"] = {
            name: sha256(os.path.join(REPO, "tools", "gates", name))
            for name in [PHON, MYTH] + OTHERS}

        # C1 — probe identity
        check("C1-probe-sha256", sha256(probe) == PROBE_SHA256,
              "probe sha256 %s" % sha256(probe))

        # C2/C3 — fail before: pre-fix bytes crash on the same payload
        for label, gate in (("C2-fail-before-phonology", PHON),
                            ("C3-fail-before-myth", MYTH)):
            res = run(os.path.join(pre, gate), probe)
            ok = (res["rc"] == 1 and "UnicodeDecodeError" in res["stderr"]
                  and "FINDING" not in res["stdout"])
            check(label, ok, "rc=%s traceback=%s findings=%s"
                  % (res["rc"], "UnicodeDecodeError" in res["stderr"],
                     "FINDING" in res["stdout"]))

        # C4/C5 — pass after: worktree bytes report could-not-evaluate
        for label, gate, needle in (("C4-pass-after-phonology", PHON, NEW_PHON_MSG),
                                    ("C5-pass-after-myth", MYTH, NEW_MYTH_MSG)):
            res = run(os.path.join(REPO, "tools", "gates", gate), probe)
            ok = (res["rc"] == 2 and "FINDING G-DATA" in res["stdout"]
                  and needle in res["stdout"] and "Traceback" not in res["stderr"])
            check(label, ok, "rc=%s msg=%r" % (res["rc"], res["stdout"].strip()[:70]))

        # C6/C7 — no false positive: valid UTF-8 (ASCII and non-ASCII) still evaluates
        for label, packet in (("C6-utf8-ascii-still-evaluates", clean),
                              ("C7-utf8-nonascii-still-evaluates", ipa)):
            ok = True
            detail = []
            for gate, needle in ((PHON, NEW_PHON_MSG), (MYTH, NEW_MYTH_MSG)):
                res = run(os.path.join(REPO, "tools", "gates", gate), packet)
                good = res["rc"] in (0, 1) and needle not in res["stdout"]
                ok = ok and good
                detail.append("%s rc=%s" % (gate.split("-")[0], res["rc"]))
            check(label, ok, ", ".join(detail))

        # C8 — unchanged error path: missing file keeps its pre-existing message
        ok = True
        detail = []
        for gate, needle in ((PHON, "could not be read"), (MYTH, "cannot read")):
            res = run(os.path.join(REPO, "tools", "gates", gate), missing)
            good = (res["rc"] == 2 and needle in res["stdout"]
                    and NEW_PHON_MSG not in res["stdout"]
                    and NEW_MYTH_MSG not in res["stdout"])
            ok = ok and good
            detail.append("%s rc=%s" % (gate.split("-")[0], res["rc"]))
        check("C8-missing-file-path-unchanged", ok, ", ".join(detail))

        # C9 — cross-gate invariance: the three correct gates behave as before
        ok = True
        detail = []
        for gate in OTHERS:
            before = run(os.path.join(pre, gate), probe)
            after = run(os.path.join(REPO, "tools", "gates", gate), probe)
            good = before["rc"] == after["rc"] == 2
            ok = ok and good
            detail.append("%s %s->%s" % (gate.split("-")[0], before["rc"], after["rc"]))
        check("C9-cross-gate-invariance", ok, ", ".join(detail))

        # C10 — selftests of the repaired gates, in a mirror (no live fixture write)
        mirror = os.path.join(work, "mirror")
        os.makedirs(mirror)
        for name in [PHON, MYTH] + OTHERS:
            shutil.copy2(os.path.join(REPO, "tools", "gates", name),
                         os.path.join(mirror, name))
        ok = True
        detail = []
        for gate in (PHON, MYTH):
            res = run(os.path.join(mirror, gate), "--selftest")
            good = res["rc"] == 0
            ok = ok and good
            detail.append("%s rc=%s" % (gate.split("-")[0], res["rc"]))
        check("C10-selftest-mirror", ok, ", ".join(detail))

        # C11 — the working tree under test actually carries the repair
        differ = all(receipt["pre_fix_sha256"][g] != receipt["worktree_sha256"][g]
                     for g in (PHON, MYTH))
        check("C11-worktree-differs-from-pre-fix", differ,
              "%s: pre %s -> work %s" % (PHON, receipt["pre_fix_sha256"][PHON][:12],
                                         receipt["worktree_sha256"][PHON][:12]))

        # C12/C13 — the stdin path of the phonology gate (`-`) is the same boundary
        def run_stdin(gate_path):
            try:
                proc = subprocess.run([sys.executable, gate_path, "-"], input=PROBE,
                                      capture_output=True, timeout=30)
                return proc.returncode, proc.stdout.decode("utf-8", "replace"), \
                    proc.stderr.decode("utf-8", "replace")
            except subprocess.TimeoutExpired:
                return None, "", ""

        rc, out, err = run_stdin(os.path.join(pre, PHON))
        check("C12-fail-before-phonology-stdin",
              rc == 1 and "UnicodeDecodeError" in err and "FINDING" not in out,
              "rc=%s traceback=%s" % (rc, "UnicodeDecodeError" in err))

        rc, out, err = run_stdin(os.path.join(REPO, "tools", "gates", PHON))
        check("C13-pass-after-phonology-stdin",
              rc == 2 and "FINDING G-DATA" in out and NEW_PHON_MSG in out
              and "Traceback" not in err,
              "rc=%s msg=%r" % (rc, out.strip()[:60]))

        failed = [item for item in results if not item["ok"]]
        receipt["summary"] = {"pass": len(results) - len(failed),
                              "fail": len(failed),
                              "verdict": "pass" if not failed else "fail"}
        if args.receipts:
            with open(args.receipts, "w", encoding="utf-8") as handle:
                json.dump(receipt, handle, indent=1, sort_keys=True)
                handle.write("\n")
        print("neg-11: %d/%d controls pass" % (receipt["summary"]["pass"], len(results)))
        return 0 if not failed else 1
    finally:
        shutil.rmtree(work, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main())
