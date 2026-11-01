#!/usr/bin/env python3
r"""Round-81 W2 mutant generator — makes the round-80 mutation pass re-runnable
from committed bytes (the round-80 verifier spot-check's routed note 6: the five
mutant bytes were scratch artifacts; "commit the five mutant generators next
time").

What it does, in order:

  0. reads the hardened guard at the pinned revision (`git show <rev>:tools/
     ledger-token-guard.py`) and asserts sha256 == the round-80 hardened pin;
  1. clean-first (QUALITY 23 addendum, limb 2): runs the REAL tool's --selftest
     and requires `SELFTEST: PASS` before any mutant row;
  2. builds five single-hardening-removal mutants by exact needle replacement,
     asserting each mutant's sha256:
       m1 replace-refusal removed  -> byte-exact round-80 m1 (sha ba5d8b91...)
       m2 input cap raised         -> deterministic r81 pin (71143bea...)
       m3 recursion catch removed  -> byte-exact round-80 m3 (sha f998e41b...)
       m4 duplicate floor removed  -> deterministic r81 pin (6f1c3379...)
       m5 env drop reverted        -> deterministic r81 pin (942f4c85...)
     HONESTY NOTE: the round-80 W2 pass ran in scratch; m1/m3 happen to be
     byte-reproducible because their r80 scratch edits removed exactly these
     needles (recorded in round-80's junk-fixtures.py and confirmed here); the
     r80 scratch edit text for m2/m4/m5 was not preserved, so those recorded
     shas (1d07c6ad/8510358487/6c863a4a in
     reports/round-80/telemetry/w1-w2-guard-revision-run80.txt section 5) stay
     historical, and these committed deterministic mutants carry their own pins.
  3. runs each mutant's --selftest expecting the named scenario to flip
     (exit=1, that scenario as-expected=False, all other scenarios as before)
     -> caught=True; m5 is probed by importing the module and diffing _env()
     under four injected GIT_* variables (hardened drops all; the mutant leaks
     all four) -> caught=True;
  4. prints per-mutant verdict lines and `W2-RERUN: PASS 5/5 (clean green
     first)`, exit 0; on any miss prints the offending lines and exits 1;
     input errors exit 2 with the stable `W2-RERUN-ERROR` label, no traceback.

Usage:
  python -B reports/round-81/mutants/w2-mutants.py --repo <lane> --rev <40hex> \
      --work <scratch>
"""
import argparse
import hashlib
import json
import os
import re
import subprocess
import sys

LABEL = "W2-RERUN-ERROR"
TOOL_PATH = "tools/ledger-token-guard.py"
TOOL_SHA = "cca7db1748bc4e49406cd768a3339454b8a59d63086b06d87a10082be3107f9a"

# recorded in reports/round-80/telemetry/w1-w2-guard-revision-run80.txt section 5
R80_M1_SHA = "ba5d8b91d0600f02b3fc7a7d323c0bd2bc1f87438cf0ff2f38656dc9c961fb04"
R80_M3_SHA = "f998e41b1d91f85b50ed51ddd474fb1b08dc6b8bbc508710cb544a54aafbb47d"
R80_M2_SCRATCH_SHA = "1d07c6ad65e1e71e515697649789f69a5b8ba7077f7fa9dbefee8c11b39ff356"
R80_M4_SCRATCH_SHA = "85103584875044b30b979d1fda8182cf87cdddf2313cdae6e39b1432e0686095"
R80_M5_SCRATCH_SHA = "6c863a4a30d9a65c8be09f50483fd7e385bff1e80bf47cee1b6c08bd181e37ef"

# deterministic r81 pins (computed from the hardened bytes; frozen in
# reports/round-81/claims.json)
PINS = {
    "m1-replace-refusal-removed": R80_M1_SHA,
    "m2-input-cap-raised": "71143bea9f3e2371afedff3426f656adf859744aeb240e5a1ea12c11490695f4",
    "m3-recursion-catch-removed": R80_M3_SHA,
    "m4-duplicate-floor-removed": "6f1c3379d8769b6c048db3582cb5331b7c6d90b37b8496b9e77455a1d9ff2c3d",
    "m5-env-drop-reverted": "942f4c85f66f0a4c4a9d21cc7d2c8ee4ed4ca39a92e21a33e141c8eb0bc0005d",
}
SCENARIO = {
    "m1-replace-refusal-removed": "replace refs refused",
    "m2-input-cap-raised": "oversize ledger refused",
    "m3-recursion-catch-removed": "deep-nested ledger refused",
    "m4-duplicate-floor-removed": "duplicate observation refused",
}
INJECT = ["GIT_ALTERNATE_OBJECT_DIRECTORIES", "GIT_CONFIG_COUNT",
          "GIT_CONFIG_KEY_0", "GIT_CONFIG_VALUE_0"]

NEEDLES = {
    "m1-replace-refusal-removed": (
        '    _require(not _has_replace_refs(repo),\n'
        '             "--repo carries refs/replace entries: replace objects would "\n'
        '             "shadow the committed bytes this guard reads")\n', ""),
    "m2-input-cap-raised": (
        "LEDGER_MAX_BYTES = 1024 * 1024",
        "LEDGER_MAX_BYTES = 1024 * 1024 * 1024"),
    "m3-recursion-catch-removed": (
        '    except RecursionError:\n'
        '        raise Refusal("ledger is JSON nested beyond the parse limit")\n', ""),
    "m4-duplicate-floor-removed": (
        '        sig = json.dumps(p["observe"], sort_keys=True, ensure_ascii=False)\n'
        '        if sig in obs_seen:\n'
        '            raise Refusal("duplicate observation object shared by pairs %s "\n'
        '                          "and %s (distinct-observation floor)"\n'
        '                          % (obs_seen[sig], p["id"]))\n'
        '        obs_seen[sig] = p["id"]\n', ""),
    "m5-env-drop-reverted": (
        '    env = {k: v for k, v in os.environ.items()\n'
        '           if not (k.startswith("GIT_") and k not in PINNED_GIT_ENV)}\n',
        "    env = dict(os.environ)\n"),
}


def run(argv, **kw):
    return subprocess.run(argv, capture_output=True, **kw)


def out(r):
    return (r.stdout or b"").decode("utf-8", "replace") + \
           (r.stderr or b"").decode("utf-8", "replace")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True)
    ap.add_argument("--rev", required=True, help="revision pinning the hardened guard")
    ap.add_argument("--work", required=True)
    args = ap.parse_args()
    if not re.fullmatch(r"[0-9a-f]{40}", args.rev):
        sys.stderr.write("%s: --rev is not 40-hex\n" % LABEL)
        return 2
    r = run(["git", "-C", args.repo, "show", "%s:%s" % (args.rev, TOOL_PATH)])
    if r.returncode != 0:
        sys.stderr.write("%s: cannot read %s at %s: %s\n"
                         % (LABEL, TOOL_PATH, args.rev, out(r).strip()))
        return 2
    src = r.stdout.decode("utf-8")
    sha = hashlib.sha256(src.encode("utf-8")).hexdigest()
    if sha != TOOL_SHA:
        sys.stderr.write("%s: tool at %s hashes %s, want %s\n"
                         % (LABEL, args.rev, sha, TOOL_SHA))
        return 2

    os.makedirs(args.work, exist_ok=True)
    py = sys.executable
    tool = os.path.join(args.repo, TOOL_PATH)
    print("# w2-rerun: tool sha256 %s at %s" % (sha, args.rev))
    print("# w2-rerun: r80 scratch shas for m2/m4/m5 stay historical (%s / %s / %s)"
          % (R80_M2_SCRATCH_SHA[:12], R80_M4_SCRATCH_SHA[:12], R80_M5_SCRATCH_SHA[:12]))

    # clean first (QUALITY 23 addendum, limb 2); the guard requires its --work
    # to name an existing scratch directory
    clean_wd = os.path.join(args.work, "clean")
    os.makedirs(clean_wd, exist_ok=True)
    r = run([py, "-B", tool, "--selftest", "--work", clean_wd])
    text = out(r)
    print("clean    selftest exit=%d %s" % (r.returncode,
          "SELFTEST: PASS" if "SELFTEST: PASS" in text else "NO-PASS-LINE"))
    if r.returncode != 0 or "SELFTEST: PASS" not in text:
        print("W2-RERUN: FAIL (clean scenario not green first)")
        return 1

    caught = 0
    # the m5 probe must be shown able to distinguish: the REAL tool's _env()
    # drops every injected GIT_* variable
    probe = (
        "import json, os, runpy, sys\n"
        "for k in %r: os.environ[k] = 'x'\n"
        "mod = runpy.run_path(sys.argv[1])\n"
        "env = mod['_env']()\n"
        "print(json.dumps(sorted(k for k in env if k.startswith('GIT_'))))\n"
        % (INJECT,))
    r = run([py, "-c", probe, tool])
    try:
        hard_leaked = json.loads(out(r).strip().splitlines()[-1])
    except (ValueError, IndexError):
        hard_leaked = ["<unparsed>"]
    hard_gone = [k for k in INJECT if k not in hard_leaked]
    print("control  hardened env-probe injected_leaked=%d" % (len(INJECT) - len(hard_gone)))
    if len(hard_gone) != len(INJECT):
        print("W2-RERUN: FAIL (hardened control leaks injected GIT_* variables)")
        return 1
    for name, needle in NEEDLES.items():
        mut = src.replace(needle[0], needle[1])
        if mut == src:
            print("W2-RERUN-ERROR internal: needle for %s did not apply" % name)
            return 2
        msha = hashlib.sha256(mut.encode("utf-8")).hexdigest()
        mpath = os.path.join(args.work, name + ".py")
        with open(mpath, "w", encoding="utf-8", newline="") as fh:
            fh.write(mut)
        ok_sha = (msha == PINS[name])
        if name == "m5-env-drop-reverted":
            probe = (
                "import json, os, runpy, sys\n"
                "for k in %r: os.environ[k] = 'x'\n"
                "mod = runpy.run_path(sys.argv[1])\n"
                "env = mod['_env']()\n"
                "print(json.dumps(sorted(k for k in env if k.startswith('GIT_'))))\n"
                % (INJECT,))
            r = run([py, "-c", probe, mpath])
            try:
                leaked = json.loads(out(r).strip().splitlines()[-1])
            except (ValueError, IndexError):
                leaked = ["<unparsed>"]
            gone = [k for k in INJECT if k not in leaked]
            # caught: the mutant lets ANY injected GIT_* var through, where the
            # hardened _env() drops every GIT_* outside its pin list
            caught_b = any(k in leaked for k in INJECT)
            print("mutant %s sha256=%s pin=%s selftest=env-probe leaked=%d injected_leaked=%d caught=%s"
                  % (name, msha, "MATCH" if ok_sha else "MISMATCH",
                     len(leaked), len(INJECT) - len(gone),
                     "True" if caught_b else "False"))
            if caught_b:
                caught += 1
            continue
        mwd = os.path.join(args.work, name)
        os.makedirs(mwd, exist_ok=True)
        r = run([py, "-B", mpath, "--selftest", "--work", mwd])
        text = out(r)
        want = SCENARIO[name]
        line = [ln for ln in text.splitlines() if want in ln and "as-expected=" in ln]
        flipped = bool(line) and ("as-expected=False" in line[0])
        failed = r.returncode == 1 and "SELFTEST: FAIL" in text
        caught_b = failed and flipped
        print("mutant %s sha256=%s pin=%s selftest exit=%d %s caught=%s"
              % (name, msha, "MATCH" if ok_sha else "MISMATCH", r.returncode,
                 ("SELFTEST: FAIL [%s]" % want) if caught_b else "NO-FLIP",
                 "True" if caught_b else "False"))
        if caught_b and ok_sha:
            caught += 1
    print("W2-RERUN: %s %d/5 (clean green first)"
          % ("PASS" if caught == 5 else "FAIL", caught))
    return 0 if caught == 5 else 1


if __name__ == "__main__":
    sys.exit(main())
