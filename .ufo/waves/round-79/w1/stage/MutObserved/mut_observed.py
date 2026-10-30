#!/usr/bin/env python3
"""MutObserved probe (round-79 W1 draft): observed_at_base off-by-one mutation fixture.

Builds an isolated git fixture repository under --work (root verified before any
commit), derives truth independently (git show bytes + python, never the guard's
own observer), then runs one pristine draft guard and a set of mutants over fixed
truthful and false cases. Writes results.json and run.txt to --out.

Usage:
  python3 -B mut_observed.py --work <fresh scratch dir> --out <receipt dir>

Exit 0 only if: pristine has zero disagreements, every mutant is killed, both
controls behave, and the hand-written case expectations agree with the
truth-derived rule (self-check).

Semantics under test (the draft rule, stated once here):
  - observed_at_base must be PRESENT (a string);
  - it must STATE the observed token: normalized recorded text equals the token,
    or starts with it at a non-alphanumeric boundary (so "3 matches" states 3,
    "30" does not, "PASS" does not state "PASS legs=12/12");
  - a stated_token equal to the observed token is a green pair and fails;
  - observed is taken from committed bytes at a pinned rev; exactly one parse hit
    is required (ambiguous output is unobservable, never first-hit);
  - an empty/zero-match absence observation is "0" only via git grep exit 1.
"""
import argparse
import json
import os
import re
import subprocess
import sys

ENV_BASE = {
    "LC_ALL": "C.UTF-8",
    "LANG": "C.UTF-8",
    "GIT_CONFIG_NOSYSTEM": "1",
    "GIT_TERMINAL_PROMPT": "0",
    "GIT_AUTHOR_NAME": "fixture",
    "GIT_AUTHOR_EMAIL": "fixture@example.invalid",
    "GIT_COMMITTER_NAME": "fixture",
    "GIT_COMMITTER_EMAIL": "fixture@example.invalid",
    "GIT_AUTHOR_DATE": "2026-10-30T00:00:00Z",
    "GIT_COMMITTER_DATE": "2026-10-30T00:00:00Z",
}

PARSE_COUNT = r"^[0-9a-f]{40}:[^:]+:([0-9]+)$"          # <rev>:<path>:<count>
PARSE_STATUS = r"^[0-9a-f]{40}:status\.txt:(.+)$"        # multi-token capture


def norm(text):
    return " ".join((text or "").split())


def env_for(work):
    env = dict(ENV_BASE)
    env["PATH"] = os.environ.get("PATH", "/usr/bin:/bin")
    env["HOME"] = work
    env["TMPDIR"] = work
    return env


def git(env, repo, *args, check=True):
    p = subprocess.run(["git", "-C", repo, *args], capture_output=True,
                       text=True, env=env)
    if check and p.returncode != 0:
        raise SystemExit("git %r rc=%d stderr=%s" % (args, p.returncode, p.stderr))
    return p


def build_fixture(env, repo):
    """B1: keys.txt 3 key lines + note; other.txt 2 key lines; status.txt one
    multi-token line. B2: keys.txt 13 key lines + note. Worktree then gets one
    uncommitted key line (14 in worktree, 13 at B2). Every rev read is pinned."""
    if os.path.exists(repo):
        raise SystemExit("fixture path already exists: %s" % repo)
    os.makedirs(repo)
    git(env, repo, "init", "-q", "-b", "main")
    top = git(env, repo, "rev-parse", "--show-toplevel").stdout.strip()
    if os.path.realpath(top) != os.path.realpath(repo):
        raise SystemExit("ROOT MISMATCH top=%s repo=%s" % (top, repo))

    def write(name, lines):
        with open(os.path.join(repo, name), "w") as fh:
            fh.write("".join(lines))

    write("keys.txt", ["key01\n", "key02\n", "key03\n", "note\n"])
    write("other.txt", ["key-x\n", "key-y\n"])
    write("status.txt", ["PASS legs=12/12\n"])
    git(env, repo, "add", "keys.txt", "other.txt", "status.txt")
    git(env, repo, "commit", "-q", "-m", "B1")
    b1 = git(env, repo, "rev-parse", "HEAD").stdout.strip()

    write("keys.txt", ["key%02d\n" % i for i in range(1, 14)] + ["note\n"])
    git(env, repo, "add", "keys.txt")
    git(env, repo, "commit", "-q", "-m", "B2")
    b2 = git(env, repo, "rev-parse", "HEAD").stdout.strip()

    with open(os.path.join(repo, "keys.txt"), "a") as fh:
        fh.write("key14-worktree\n")  # uncommitted: worktree only
    return b1, b2


def truth_lines(env, repo, rev, path, prefix):
    """Independent truth from `git show <rev>:<path>` bytes (python, not git grep)."""
    p = git(env, repo, "show", "%s:%s" % (rev, path))
    return [line for line in p.stdout.splitlines() if line.startswith(prefix)]


# ----------------------------------------------------------------- observers
def run_argv(env, repo, argv):
    p = subprocess.run(argv, cwd=repo, capture_output=True, text=True, env=env)
    return p.returncode, p.stdout


def obs_pristine(env, repo, argv, parse):
    rc, out = run_argv(env, repo, argv)
    if out.strip() == "" and rc == 1:
        return "0", "exit=1 zero-matches", out
    if rc != 0 or out.strip() == "":
        return None, "rc=%d empty" % rc, out
    hits = re.findall(parse, out, re.M)
    if len(hits) != 1:
        return None, "parse-hits=%d" % len(hits), out
    return norm(hits[0]), "ok", out


def obs_group0(env, repo, argv, parse):
    """Mutant: token is the whole matched line, not the capture group."""
    rc, out = run_argv(env, repo, argv)
    if out.strip() == "" and rc == 1:
        return "0", "exit=1 zero-matches", out
    ms = [m.group(0) for m in re.finditer(parse, out, re.M)]
    if len(ms) != 1:
        return None, "parse-hits=%d" % len(ms), out
    return norm(ms[0]), "ok", out


def obs_first(env, repo, argv, parse):
    """Mutant: first regex hit only; ambiguity is not refused."""
    rc, out = run_argv(env, repo, argv)
    if out.strip() == "" and rc == 1:
        return "0", "exit=1 zero-matches", out
    m = re.search(parse, out, re.M)
    if not m:
        return None, "parse-miss", out
    return norm(m.group(1)), "ok", out


def obs_worktree(env, repo, argv, parse):
    """Mutant: drops the rev operand so the observer reads the moving worktree;
    the rev prefix in the parse becomes optional to match `git grep` output."""
    stripped = [a for a in argv if not re.fullmatch(r"[0-9a-f]{40}", a)]
    wt_parse = parse.replace("^[0-9a-f]{40}:", "^(?:[0-9a-f]{40}:)?", 1)
    rc, out = run_argv(env, repo, stripped)
    if out.strip() == "" and rc == 1:
        return "0", "exit=1 zero-matches", out
    hits = re.findall(wt_parse, out, re.M)
    if len(hits) != 1:
        return None, "parse-hits=%d" % len(hits), out
    return norm(hits[0]), "ok", out


# ------------------------------------------------------------------- guards
def _int(text):
    try:
        return int(text)
    except (TypeError, ValueError):
        return None


def covers(rec, obs):
    """Recorded text STATES the observed token: equal, or the token followed by a
    non-alphanumeric boundary (so '3 matches' states 3; '30' and 'PASS' do not
    state '3' or 'PASS legs=12/12')."""
    if not isinstance(rec, str) or obs is None:
        return False
    n = norm(rec)
    if n == obs:
        return True
    return n.startswith(obs) and len(n) > len(obs) and not n[len(obs)].isalnum()


def g_pristine(rec, stated, obs):
    if obs is None:
        return "UNOBSERVABLE"
    if not isinstance(rec, str):
        return "FAIL"
    if stated is not None and norm(stated) == obs:
        return "FAIL"  # green pair: must be dropped, never listed
    return "PASS" if covers(rec, obs) else "FAIL"


def g_committed_lead(rec, stated, obs):
    """Mirrors the committed round-76 BASEMISMATCH rule: first whitespace token only."""
    if obs is None:
        return "UNOBSERVABLE"
    if not isinstance(rec, str):
        return "FAIL"
    if stated is not None and norm(stated) == obs:
        return "FAIL"
    lead = (rec.split() or [""])[0]
    return "PASS" if lead == obs else "FAIL"


def g_tol_pm1(rec, stated, obs):
    v = g_pristine(rec, stated, obs)
    if v != "FAIL" or obs is None or not isinstance(rec, str):
        return v
    a, b = _int(norm(rec).split()[0] if norm(rec) else ""), _int(obs)
    return "PASS" if (a is not None and b is not None and abs(a - b) <= 1) else "FAIL"


def g_under1(rec, stated, obs):
    v = g_pristine(rec, stated, obs)
    if v != "FAIL" or obs is None or not isinstance(rec, str):
        return v
    a, b = _int(norm(rec).split()[0] if norm(rec) else ""), _int(obs)
    return "PASS" if (a is not None and b is not None and a == b - 1) else "FAIL"


def g_le(rec, stated, obs):
    if obs is None or not isinstance(rec, str):
        return g_pristine(rec, stated, obs)
    if stated is not None and norm(stated) == obs:
        return "FAIL"
    a, b = _int(norm(rec).split()[0] if norm(rec) else ""), _int(obs)
    if a is not None and b is not None:
        return "PASS" if a <= b else "FAIL"
    return g_pristine(rec, stated, obs)


def g_prefix_nobound(rec, stated, obs):
    """Mutant: prefix match without the alphanumeric boundary."""
    if obs is None or not isinstance(rec, str):
        return g_pristine(rec, stated, obs)
    if stated is not None and norm(stated) == obs:
        return "FAIL"
    n = norm(rec)
    return "PASS" if (n and n.startswith(obs)) else "FAIL"


def g_obs_prefix_of_rec(rec, stated, obs):
    """Mutant: the observed token is accepted as a prefix of the recorded one
    (reverse containment, i.e. recorded may be truncated)."""
    if obs is None or not isinstance(rec, str):
        return g_pristine(rec, stated, obs)
    if stated is not None and norm(stated) == obs:
        return "FAIL"
    n = norm(rec)
    return "PASS" if (n and obs.startswith(n)) else "FAIL"


def g_lex_ge(rec, stated, obs):
    if obs is None or not isinstance(rec, str):
        return g_pristine(rec, stated, obs)
    if stated is not None and norm(stated) == obs:
        return "FAIL"
    lead = (rec.split() or [""])[0]
    return "PASS" if (lead and lead >= obs) else "FAIL"


def g_stated_cmp(rec, stated, obs):
    if obs is None:
        return "UNOBSERVABLE"
    if stated is None:
        return "FAIL"
    return "PASS" if covers(norm(stated), obs) else "FAIL"


def g_nogreen(rec, stated, obs):
    if obs is None:
        return "UNOBSERVABLE"
    if not isinstance(rec, str):
        return "FAIL"
    return "PASS" if covers(rec, obs) else "FAIL"


def g_missing_skip(rec, stated, obs):
    if not isinstance(rec, str) and obs is not None:
        return "PASS"  # mirrors committed round-76 BASEMISMATCH: cross-check skipped
    return g_pristine(rec, stated, obs)


def g_accept_all(rec, stated, obs):
    return "UNOBSERVABLE" if obs is None else "PASS"


def g_reject_all(rec, stated, obs):
    return "UNOBSERVABLE" if obs is None else "FAIL"


GUARDS = {
    "M00_pristine": (g_pristine, obs_pristine),
    "M01_tolerance_pm1": (g_tol_pm1, obs_pristine),
    "M02_accepts_obs_minus1": (g_under1, obs_pristine),
    "M03_le_instead_of_eq": (g_le, obs_pristine),
    "M04_obs_prefix_of_rec": (g_obs_prefix_of_rec, obs_pristine),
    "M05_lexical_ge": (g_lex_ge, obs_pristine),
    "M06_stated_compared_not_observed": (g_stated_cmp, obs_pristine),
    "M07_no_green_check": (g_nogreen, obs_pristine),
    "M08_missing_field_skipped": (g_missing_skip, obs_pristine),
    "M09_token_is_group0": (g_pristine, obs_group0),
    "M10_first_hit_not_refused": (g_pristine, obs_first),
    "M11_reads_worktree_not_rev": (g_pristine, obs_worktree),
    "M12_committed_leading_token": (g_committed_lead, obs_pristine),
    "M13_prefix_without_boundary": (g_prefix_nobound, obs_pristine),
    "C01_control_accept_all": (g_accept_all, obs_pristine),
    "C02_control_reject_all": (g_reject_all, obs_pristine),
}
CONTROLS = {"C01_control_accept_all", "C02_control_reject_all"}


# -------------------------------------------------------------------- keys
def build_keys(b1, b2):
    """key -> (argv pinned to a rev or tree, parse regex)."""
    return {
        "B1": (["git", "grep", "-c", "^key", b1, "--", "keys.txt"], PARSE_COUNT),
        "B2": (["git", "grep", "-c", "^key", b2, "--", "keys.txt"], PARSE_COUNT),
        "B1Z": (["git", "grep", "-c", "^zzz", b1, "--", "keys.txt"], PARSE_COUNT),
        "B1MULTI": (["git", "grep", "-c", "^key", b1], PARSE_COUNT),
        "S": (["git", "grep", "^PASS", b1, "--", "status.txt"], PARSE_STATUS),
    }


# (id, observe key, recorded observed_at_base or None, stated token,
#  hand expectation PASS | FAIL | NOTPASS, why)
CASES = [
    ("C01", "B1", "3", "4", "PASS", "truthful exact count"),
    ("C02", "B1", "3 matches in keys.txt", "4", "PASS", "truthful, prose after token at boundary"),
    ("C03", "B1", "  3\n", "4", "PASS", "truthful, surrounding whitespace"),
    ("C04", "B1", "4", "2", "FAIL", "+1 off-by-one (recorded above observed)"),
    ("C05", "B1", "2", "4", "FAIL", "-1 off-by-one (recorded below observed)"),
    ("C06", "B2", "13", "12", "PASS", "truthful two-digit count"),
    ("C07", "B2", "12", "14", "FAIL", "-1 across tens boundary"),
    ("C08", "B2", "14", "14", "FAIL", "recorded = worktree count (uncommitted line)"),
    ("C09", "B2", "1", "2", "FAIL", "prefix of observed token (1 of 13)"),
    ("C10", "B1", "", "4", "FAIL", "empty recorded token"),
    ("C11", "B1", "3", "3", "FAIL", "stated equals observation: green pair must be dropped"),
    ("C12", "B1", None, "4", "FAIL", "observed_at_base absent (design decision: require it)"),
    ("C13", "B1", "4", "4", "FAIL", "recorded equals stated but not observed (3)"),
    ("C14", "B1Z", "0", "2", "PASS", "truthful zero-match absence"),
    ("C15", "B1Z", "1", "2", "FAIL", "+1 off-by-one at zero"),
    ("C16", "B1MULTI", "3", "4", "NOTPASS", "two-file hit set: ambiguous, must refuse not first-hit"),
    ("C17", "B2", "13", "13", "FAIL", "truthful value but stated equals observation (green)"),
    ("C18", "S", "PASS legs=12/12", "FAIL", "PASS", "truthful multi-token record (committed leading-token rule rejects it)"),
    ("C19", "S", "PASS legs=12/12 (round-72 receipt)", "FAIL", "PASS", "truthful multi-token record with prose after the token"),
    ("C20", "S", "PASS", "FAIL", "FAIL", "truncated multi-token record"),
    ("C21", "S", "PASS legs=12/1", "FAIL", "FAIL", "truncated inside the final token"),
    ("C22", "B1", "30", "4", "FAIL", "recorded starts with observed digits but continues (30 vs 3)"),
]


def derive_expectation(case, truths):
    cid, key, rec, stated, _, _ = case
    if key == "B1MULTI":
        return "NOTPASS"
    truth = truths[key]
    if rec is None or stated is None:
        return "FAIL"
    if norm(stated) == truth:
        return "FAIL"
    return "PASS" if covers(rec, truth) else "FAIL"


def normalize_verdict(v):
    return "NOTPASS" if v in ("FAIL", "UNOBSERVABLE") else v


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--work", required=True, help="fresh scratch dir (must not exist)")
    ap.add_argument("--out", required=True, help="receipt directory")
    args = ap.parse_args()

    work = os.path.abspath(args.work)
    out_dir = os.path.abspath(args.out)
    if os.path.exists(work):
        raise SystemExit("work dir must not exist: %s" % work)
    os.makedirs(work)
    os.makedirs(out_dir, exist_ok=True)
    env = env_for(work)
    repo = os.path.join(work, "fixture-repo")

    b1, b2 = build_fixture(env, repo)
    keys = build_keys(b1, b2)

    k_b1 = truth_lines(env, repo, b1, "keys.txt", "key")
    k_b2 = truth_lines(env, repo, b2, "keys.txt", "key")
    s_line = truth_lines(env, repo, b1, "status.txt", "PASS")
    truths = {
        "B1": str(len(k_b1)),
        "B2": str(len(k_b2)),
        "B1Z": "0",
        "S": norm(s_line[0]) if s_line else None,
    }

    self_check = []
    for case in CASES:
        derived = derive_expectation(case, truths)
        self_check.append({"case": case[0], "hand": case[4], "derived": derived,
                           "ok": derived == case[4]})
    self_check_ok = all(x["ok"] for x in self_check)

    raw_obs = {}
    for key, (argv, _) in keys.items():
        rc, out = run_argv(env, repo, argv)
        raw_obs[key] = {"argv": argv, "rc": rc, "stdout": out}
    wt_argv = [a for a in keys["B2"][0] if not re.fullmatch(r"[0-9a-f]{40}", a)]
    rc, out = run_argv(env, repo, wt_argv)
    raw_obs["B2-worktree-no-rev"] = {"argv": wt_argv, "rc": rc, "stdout": out}

    matrix = {}
    disagreements = {}
    for gname, (guard, observer) in GUARDS.items():
        rows = []
        dis = []
        for case in CASES:
            cid, key, rec, stated, hand, why = case
            argv, parse = keys[key]
            obs, ob_why, raw = observer(env, repo, argv, parse)
            v = normalize_verdict(guard(rec, stated, obs))
            want = "PASS" if hand == "PASS" else "NOTPASS"
            rows.append({"case": cid, "key": key, "recorded": rec, "stated": stated,
                         "observed": obs, "why_obs": ob_why,
                         "verdict": v, "expected": want, "why": why})
            if v != want:
                dis.append(cid)
        matrix[gname] = rows
        disagreements[gname] = dis

    pristine_clean = not disagreements["M00_pristine"]
    mutants = [g for g in GUARDS if g != "M00_pristine" and g not in CONTROLS]
    killed = {g: bool(disagreements[g]) for g in mutants}
    controls = {g: bool(disagreements[g]) for g in CONTROLS}
    all_killed = all(killed.values())
    controls_ok = all(controls.values())

    result = {
        "fixture": {"repo": repo, "b1": b1, "b2": b2, "truths": truths},
        "self_check": self_check,
        "self_check_ok": self_check_ok,
        "raw_observations": raw_obs,
        "pristine_disagreements": disagreements["M00_pristine"],
        "pristine_clean": pristine_clean,
        "mutant_killed": killed,
        "control_killed": controls,
        "all_mutants_killed": all_killed,
        "controls_behave": controls_ok,
        "disagreements": disagreements,
        "matrix": matrix,
    }
    with open(os.path.join(out_dir, "results.json"), "w") as fh:
        json.dump(result, fh, indent=1, sort_keys=True)

    lines = []
    lines.append("MutObserved probe — observed_at_base guard draft")
    lines.append("fixture root verified: %s" % repo)
    lines.append("B1=%s B2=%s" % (b1, b2))
    lines.append("truth: B1=%s B2=%s B1Z=0 S=%r (worktree adds 1 uncommitted key line)"
                 % (truths["B1"], truths["B2"], truths["S"]))
    lines.append("self-check hand vs truth-derived expectations: %s" % self_check_ok)
    for x in self_check:
        if not x["ok"]:
            lines.append("  SELF-CHECK MISMATCH %s hand=%s derived=%s"
                         % (x["case"], x["hand"], x["derived"]))
    lines.append("")
    lines.append("%-34s %-14s %s" % ("guard", "result", "disagreeing cases"))
    for g in GUARDS:
        if g == "M00_pristine":
            res = "CLEAN" if pristine_clean else "DIRTY"
        elif g in CONTROLS:
            res = "CONTROL-OK" if controls[g] else "CONTROL-SURVIVED"
        else:
            res = "KILLED" if killed[g] else "SURVIVED"
        lines.append("%-34s %-14s %s" % (g, res, ",".join(disagreements[g]) or "-"))
    lines.append("")
    lines.append("pristine clean: %s | all mutants killed: %s | controls behave: %s | self-check: %s"
                 % (pristine_clean, all_killed, controls_ok, self_check_ok))
    text = "\n".join(lines) + "\n"
    with open(os.path.join(out_dir, "run.txt"), "w") as fh:
        fh.write(text)
    sys.stdout.write(text)

    ok = pristine_clean and all_killed and controls_ok and self_check_ok
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
