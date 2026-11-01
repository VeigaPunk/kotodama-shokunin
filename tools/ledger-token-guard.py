#!/usr/bin/env python3
r"""ledger-token-guard - re-run a claim ledger's recorded observations.

BOUNDED PURPOSE. A claim ledger records, for each pair, a stated token
(taken from a corpus or lane artifact at a named line) and an
`observed_at_base` token (what an approved observation at a pinned commit
reported). This guard re-runs every observation against the immutable
committed bytes named by the pair's `observe` object and refuses to let two
documented defect classes pass silently:

  * recorded-observation drift (round-77 R78-M1): the recorded
    `observed_at_base` differs from what the same observation yields on the
    same committed bytes today;
  * vacuity: the stated token equals the observed token, so the pair cannot
    distinguish a correct observation from an echo.

STRICT LEDGER SCHEMA. The only accepted ledger is a JSON object with a
`pairs` array; every element is an object carrying:

  id               non-empty string, unique across the ledger
  stated_at        "<path>:<line>" locating the stated evidence
  stated_text      the recorded text the stated token was extracted from
  stated_parse     a regular expression; the stated token is capture
                   group 1 if present, else the whole match
  observe          object: op, rev, path, pattern, and per-op fields below
  observed_at_base the recorded observation token to re-check

observe.op is one of:

  count  count lines matching `pattern` in `<rev>:<path>`; the observed
         token is that count rendered in decimal.
  line   read line `line` (1-based) of `<rev>:<path>`; the observed token
         is capture group 1 (else the whole match) of `pattern` on it.

observe.rev MUST be a 40-hex commit resolvable in --repo; mutable names
(HEAD, branch names, tags, `~`/`^` expressions, short hashes) are refused
before any lookup. observe.path must be a clean relative path inside the
repository (no leading `/`, no `..` components, no NUL); the blob is read
with `git cat-file`, never through the worktree. There is deliberately no
`observe_cmd` field and no command channel of any kind: this guard never
executes a command from a ledger, and a ledger naming one is refused as
unknown op. Historical argv-ledger shapes (top-level array, missing
`observe`, `argv`/`command`/`run` keys) are refused up front with the same
stable label, not parsed halfway.

HARDENED READ CHANNEL (round-80 revision of the round-79 tool; findings
MutPath F6, SentinelLimits F1/F3/F9 and MutVacuous F7, round-79 W1). Four
rules pin "immutable committed bytes" against the measured bypasses:

  * replace objects: `--repo` carrying any `refs/replace/` entry is
    refused outright (replace objects shadow the bytes `cat-file` returns),
    and every git child runs with `GIT_NO_REPLACE_OBJECTS=1` so no
    inherited environment can re-enable shadowing;
  * environment: every `GIT_*` variable is dropped from the inherited
    environment except the guard's own pinned set (GIT_CONFIG_GLOBAL,
    GIT_CONFIG_NOSYSTEM, GIT_TERMINAL_PROMPT, GIT_NO_REPLACE_OBJECTS,
    GIT_OPTIONAL_LOCKS), closing the GIT_DIR-adjacent and
    GIT_CONFIG_COUNT/KEY_n/VALUE_n injection channels;
  * input cap: a ledger larger than LEDGER_MAX_BYTES (1 MiB) is refused
    before decode, and JSON nested beyond the parser's recursion limit is
    refused with the stable label instead of escaping as a traceback;
  * distinct-observation floor: two pairs may not carry the identical
    `observe` object (same op/rev/path/pattern/line) - a ledger restating
    one observation N times cannot inflate its pair count.

OUTPUT CONTRACT (greppable, diffable):

  pair <id>: ok observed=<token>             - pair verified
  pair <id>: fail MISMATCH recorded=<r> actual=<a>
  pair <id>: fail VACUOUS token=<t>          - stated == observed
  LEDGER-TOKEN-GUARD: PASS pairs=<n>
  LEDGER-TOKEN-GUARD: FAIL pairs=<n> failed=<m> mismatched=<k> vacuous=<v>
  LEDGER-TOKEN-GUARD: REFUSED <reason>       - exit 2, nothing graded

Exit: 0 every pair ok; 1 at least one pair failed; 2 refusal
(unreadable/invalid/oversize input, mutable rev, unknown op, unsafe path,
missing blob, replace refs, duplicate observations, ledger/base argument
mismatch). Refusals always carry the LEDGER-TOKEN-GUARD label and never
print pair verdicts.

SELF-CONTAINED SELFTEST: `--selftest --work <dir>` builds fresh fixture
git repositories under <dir> (never reusing an existing path), commits a
probe file, runs every schema check, both defect-class detectors and the
four hardened-channel scenarios against them, and prints one
`as-expected` line per scenario plus `SELFTEST: PASS`. Every scenario must
land on its expected exit class or the selftest fails; the fixture
repositories are left under the work dir for inspection unless run with
`--clean`.

LIMITS, STATED: this guard re-checks recorded observations; it does not
certify that the original observation was approved, that the stated token
is the right thing to measure, or that the pair's prose is honest. Those
remain reviewer obligations. It grades committed bytes only: a ledger
pointing at the worktree, or at bytes outside --repo, cannot be checked
here by design. The distinct-observation floor refuses only exact
duplicate `observe` objects - two pairs observing the same path with
different patterns remain legal and are graded independently.
"""

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys

LABEL = "LEDGER-TOKEN-GUARD"
HEX40 = re.compile(r"^[0-9a-f]{40}$")
LEDGER_MAX_BYTES = 1024 * 1024  # 1 MiB ledger input cap (SentinelLimits F1)
PINNED_GIT_ENV = ("GIT_CONFIG_GLOBAL", "GIT_CONFIG_NOSYSTEM",
                  "GIT_TERMINAL_PROMPT", "GIT_NO_REPLACE_OBJECTS",
                  "GIT_OPTIONAL_LOCKS")
OPS = ("count", "line")
FORBIDDEN_TOP = ("argv", "command", "run", "cmd", "observe_cmd", "shell",
                 "exec")


class Refusal(Exception):
    """Input problem: refuse, exit 2, stable label, nothing graded."""


def _env(extra=None):
    env = {k: v for k, v in os.environ.items()
           if not (k.startswith("GIT_") and k not in PINNED_GIT_ENV)}
    env.update(GIT_CONFIG_GLOBAL=os.devnull, GIT_CONFIG_NOSYSTEM="1",
               GIT_TERMINAL_PROMPT="0", GIT_NO_REPLACE_OBJECTS="1",
               GIT_OPTIONAL_LOCKS="0", LC_ALL="C")
    if extra:
        env.update(extra)
    return env


def git(repo, *args):
    proc = subprocess.run(["git", "-C", repo, *args], capture_output=True,
                          env=_env())
    if proc.returncode != 0:
        return None
    return proc.stdout


def _require(cond, reason):
    if not cond:
        raise Refusal(reason)


def _check_rev(repo, rev):
    """observe.rev: immutable 40-hex commit only."""
    _require(isinstance(rev, str) and HEX40.match(rev),
             "observe.rev %r is not an immutable 40-hex commit" % (rev,))
    out = git(repo, "cat-file", "-t", rev)
    _require(out is not None and out.decode().strip() == "commit",
             "observe.rev %s is not a commit in repo" % rev)


def _check_path(path):
    _require(isinstance(path, str) and path and not path.startswith("/"),
             "observe.path %r is not a relative path" % (path,))
    _require("\x00" not in path and "\\" not in path,
             "observe.path %r contains a banned byte" % (path,))
    parts = path.split("/")
    _require(all(p not in ("", ".", "..") for p in parts),
             "observe.path %r is not a clean in-repo path" % (path,))


def _has_replace_refs(repo):
    out = git(repo, "for-each-ref", "refs/replace/")
    return bool(out and out.strip())


def _blob(repo, rev, path):
    """Read the committed blob; raise Refusal on anything unusual."""
    spec = "%s:%s" % (rev, path)
    kind = git(repo, "cat-file", "-t", spec)
    _require(kind is not None, "blob %s not found" % spec)
    _require(kind.decode().strip() == "blob",
             "%s is not a regular blob" % spec)
    data = git(repo, "cat-file", "blob", spec)
    _require(data is not None, "blob %s unreadable" % spec)
    return data.decode("utf-8", "replace")


def _stated_token(pair):
    pat = pair["stated_parse"]
    _require(isinstance(pat, str) and pat, "pair %s stated_parse empty"
             % (pair.get("id"),))
    try:
        rx = re.compile(pat)
    except re.error as exc:
        raise Refusal("pair %s stated_parse does not compile: %s"
                      % (pair.get("id"), exc))
    m = rx.search(pair["stated_text"])
    _require(m is not None, "pair %s stated_parse does not match "
             "stated_text" % (pair.get("id"),))
    return m.group(1) if m.groups() else m.group(0)


def _observe(repo, obs):
    """Run one observation on committed bytes; return the observed token."""
    _require(isinstance(obs, dict), "observe is not an object")
    op = obs.get("op")
    _require(op in OPS, "observe.op %r not in %s" % (op, "/".join(OPS)))
    _check_rev(repo, obs.get("rev"))
    _check_path(obs.get("path"))
    pat = obs.get("pattern")
    _require(isinstance(pat, str) and pat, "observe.pattern empty")
    try:
        rx = re.compile(pat)
    except re.error as exc:
        raise Refusal("observe.pattern does not compile: %s" % exc)
    text = _blob(repo, obs["rev"], obs["path"])
    if op == "count":
        return str(sum(1 for ln in text.splitlines() if rx.search(ln)))
    # op == "line"
    line = obs.get("line")
    _require(isinstance(line, int) and line >= 1,
             "observe.line %r is not a 1-based line number" % (line,))
    lines = text.splitlines()
    _require(line <= len(lines),
             "observe.line %d past end of %s (%d lines)"
             % (line, obs["path"], len(lines)))
    m = rx.search(lines[line - 1])
    _require(m is not None, "observe.pattern did not match %s:%d"
             % (obs["path"], line))
    return m.group(1) if m.groups() else m.group(0)


def _load_ledger(path):
    try:
        with open(path, "rb") as fh:
            raw = fh.read()
    except OSError as exc:
        raise Refusal("ledger unreadable: %s" % exc)
    _require(len(raw) <= LEDGER_MAX_BYTES,
             "ledger is %d bytes, over the %d byte input cap"
             % (len(raw), LEDGER_MAX_BYTES))
    try:
        doc = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, ValueError) as exc:
        raise Refusal("ledger is not a JSON object: %s" % exc)
    except RecursionError:
        raise Refusal("ledger is JSON nested beyond the parse limit")
    _require(isinstance(doc, dict), "ledger top level is not an object")
    bad = [k for k in doc if k in FORBIDDEN_TOP]
    _require(not bad, "ledger carries command-channel keys: %s"
             % ",".join(sorted(bad)))
    pairs = doc.get("pairs")
    _require(isinstance(pairs, list) and pairs,
             "ledger has no non-empty pairs array")
    seen = set()
    obs_seen = {}
    for i, p in enumerate(pairs):
        _require(isinstance(p, dict), "pair %d is not an object" % i)
        _require(isinstance(p.get("id"), str) and p["id"],
                 "pair %d has no id" % i)
        _require(p["id"] not in seen, "duplicate pair id %s" % p["id"])
        seen.add(p["id"])
        for key in ("stated_at", "stated_text", "stated_parse",
                    "observed_at_base", "observe"):
            _require(key in p, "pair %s missing key %s" % (p["id"], key))
        _require(isinstance(p["stated_text"], str),
                 "pair %s stated_text is not a string" % p["id"])
        _require(isinstance(p["observed_at_base"], str),
                 "pair %s observed_at_base is not a string" % p["id"])
        _require(isinstance(p.get("observe"), dict),
                 "pair %s observe is not an object" % p["id"])
        sig = json.dumps(p["observe"], sort_keys=True, ensure_ascii=False)
        if sig in obs_seen:
            raise Refusal("duplicate observation object shared by pairs %s "
                          "and %s (distinct-observation floor)"
                          % (obs_seen[sig], p["id"]))
        obs_seen[sig] = p["id"]
    return doc


def guard(ledger_path, repo, base):
    doc = _load_ledger(ledger_path)
    declared = doc.get("base")
    _require(declared is None or declared == base,
             "ledger base %r differs from --base %r" % (declared, base))
    _check_rev(repo, base)
    _require(os.path.isdir(repo), "--repo %s is not a directory" % repo)
    _require(git(repo, "rev-parse", "--git-dir") is not None,
             "--repo %s is not a git repository" % repo)
    _require(not _has_replace_refs(repo),
             "--repo carries refs/replace entries: replace objects would "
             "shadow the committed bytes this guard reads")
    failed = mismatched = vacuous = 0
    lines = []
    for p in doc["pairs"]:
        actual = _observe(repo, p["observe"])
        stated = _stated_token(p)
        recorded = p["observed_at_base"]
        pid = p["id"]
        if actual != recorded:
            failed += 1
            mismatched += 1
            lines.append("pair %s: fail MISMATCH recorded=%s actual=%s"
                         % (pid, recorded, actual))
        elif stated == actual:
            failed += 1
            vacuous += 1
            lines.append("pair %s: fail VACUOUS token=%s" % (pid, actual))
        else:
            lines.append("pair %s: ok observed=%s" % (pid, actual))
    return lines, len(doc["pairs"]), failed, mismatched, vacuous


def run(argv=None):
    ap = argparse.ArgumentParser(
        description="Re-run a claim ledger's recorded observations against "
                    "immutable committed bytes.")
    ap.add_argument("--ledger", help="claim ledger JSON file")
    ap.add_argument("--repo", help="git repository the pairs observe")
    ap.add_argument("--base", help="40-hex commit the ledger binds")
    ap.add_argument("--work", help="existing scratch directory "
                                   "(required; no TMPDIR fallback)")
    ap.add_argument("--selftest", action="store_true",
                    help="run the built-in scenario battery and exit")
    ap.add_argument("--clean", action="store_true",
                    help="with --selftest: remove fixture directories")
    args = ap.parse_args(argv)
    try:
        if args.selftest:
            return selftest(args.work, args.clean)
        for flag in ("--ledger", "--repo", "--base", "--work"):
            if getattr(args, flag[2:]) is None:
                raise Refusal("missing %s" % flag)
        if not os.path.isdir(args.work):
            raise Refusal("--work %s is not an existing directory "
                          "(explicit scratch; no TMPDIR fallback)"
                          % args.work)
        lines, total, failed, mismatched, vacuous = guard(
            args.ledger, args.repo, args.base)
        for ln in lines:
            print(ln)
        if failed:
            print("%s: FAIL pairs=%d failed=%d mismatched=%d vacuous=%d"
                  % (LABEL, total, failed, mismatched, vacuous))
            return 1
        print("%s: PASS pairs=%d" % (LABEL, total))
        return 0
    except Refusal as exc:
        print("%s: REFUSED %s" % (LABEL, exc))
        return 2


# --------------------------------------------------------------- selftest

def _mkrepo(root, name):
    repo = os.path.join(root, name)
    os.mkdir(repo)
    env = _env({"GIT_AUTHOR_NAME": "guard-selftest",
                "GIT_AUTHOR_EMAIL": "selftest@invalid",
                "GIT_COMMITTER_NAME": "guard-selftest",
                "GIT_COMMITTER_EMAIL": "selftest@invalid"})
    subprocess.run(["git", "-C", repo, "init", "-q", "-b", "main"],
                   env=env, check=True)
    with open(os.path.join(repo, "probe.txt"), "w") as fh:
        fh.write("alpha\nbeta\ngamma\nentries: 42\n")
    subprocess.run(["git", "-C", repo, "add", "probe.txt"], env=env,
                   check=True)
    subprocess.run(["git", "-C", repo, "-c", "commit.gpgsign=false",
                    "commit", "-q", "-m", "fixture"], env=env, check=True)
    rev = subprocess.run(["git", "-C", repo, "rev-parse", "HEAD"], env=env,
                         capture_output=True,
                         check=True).stdout.decode().strip()
    return repo, rev


def _ledger(path, base, pairs):
    doc = {"round": 0, "claim": "selftest", "base": base, "pairs": pairs}
    with open(path, "w") as fh:
        json.dump(doc, fh)


def _pair(pid, obs, recorded, stated_text="count 5", stated_parse=r"count (5)"):
    return {"id": pid, "stated_at": "x:1", "stated_text": stated_text,
            "stated_parse": stated_parse, "observe": obs,
            "observed_at_base": recorded}


def _run_cli(ledger, repo, base, work):
    proc = subprocess.run(
        [sys.executable, "-B", os.path.abspath(__file__), "--ledger", ledger,
         "--repo", repo, "--base", base, "--work", work],
        capture_output=True)
    return proc.returncode, (proc.stdout.decode("utf-8", "replace")
                             + proc.stderr.decode("utf-8", "replace"))


def _replace_fixture(st):
    """Second fixture repo carrying a refs/replace entry (MutPath F6)."""
    repo, rev = _mkrepo(st, "fixture-repo-replace")
    env = _env({"GIT_AUTHOR_NAME": "guard-selftest",
                "GIT_AUTHOR_EMAIL": "selftest@invalid"})
    v2 = os.path.join(st, "probe-v2.txt")
    with open(v2, "w") as fh:
        fh.write("alpha\nREPLACED-CONTENT\n")
    new_blob = subprocess.run(
        ["git", "-C", repo, "hash-object", "-w", v2], env=env,
        capture_output=True, check=True).stdout.decode().strip()
    old_blob = subprocess.run(
        ["git", "-C", repo, "rev-parse", "%s:probe.txt" % rev], env=env,
        capture_output=True, check=True).stdout.decode().strip()
    subprocess.run(["git", "-C", repo, "replace", old_blob, new_blob],
                   env=env, check=True)
    return repo, rev


def selftest(work, clean):
    _require(work and os.path.isdir(work),
             "--work must name an existing scratch directory")
    st = os.path.join(work, "ledger-token-guard-selftest")
    _require(not os.path.exists(st),
             "selftest fixture root %s already exists" % st)
    os.makedirs(st)
    repo, rev = _mkrepo(st, "fixture-repo")
    rerepo, rerev = _replace_fixture(st)
    bad = []
    runw = os.path.join(st, "run")
    os.mkdir(runw)

    obs_ok = {"op": "count", "rev": rev, "path": "probe.txt",
              "pattern": "a$"}
    obs_line = {"op": "line", "rev": rev, "path": "probe.txt",
                "pattern": r"entries: ([0-9]+)", "line": 4}
    obs_line1 = {"op": "line", "rev": rerev, "path": "probe.txt",
                 "pattern": r"^(.+)$", "line": 1}
    cases = []

    led = os.path.join(st, "green.json")
    _ledger(led, rev, [_pair("G1", obs_ok, "3"),
                       _pair("G2", obs_line, "42",
                             stated_text="entries: 9",
                             stated_parse=r"entries: ([0-9]+)")])
    cases.append(("green all pairs", repo, led, rev, 0, "PASS pairs=2"))

    led = os.path.join(st, "mismatch.json")
    _ledger(led, rev, [_pair("M1", obs_ok, "1")])
    cases.append(("recorded!=observed", repo, led, rev, 1, "MISMATCH"))

    led = os.path.join(st, "vacuous.json")
    _ledger(led, rev, [_pair("V1", obs_ok, "3", stated_text="count 3",
                             stated_parse=r"count (3)")])
    cases.append(("stated==observed", repo, led, rev, 1, "VACUOUS"))

    led = os.path.join(st, "mutablerev.json")
    _ledger(led, rev, [_pair("R1",
                             dict(obs_ok, rev="HEAD"), "3")])
    cases.append(("mutable observe.rev", repo, led, rev, 2, "REFUSED"))

    led = os.path.join(st, "badbase.json")
    _ledger(led, rev, [_pair("B1", obs_ok, "3")])
    with open(led) as fh:
        d = json.load(fh)
    d["base"] = "0" * 40
    with open(led, "w") as fh:
        json.dump(d, fh)
    cases.append(("ledger/base mismatch", repo, led, rev, 2, "REFUSED"))

    led = os.path.join(st, "badop.json")
    _ledger(led, rev, [_pair("O1",
                             {"op": "exec", "rev": rev, "path": "probe.txt",
                              "pattern": "x"}, "0")])
    cases.append(("unknown op", repo, led, rev, 2, "REFUSED"))

    led = os.path.join(st, "badpath.json")
    _ledger(led, rev, [_pair("P1",
                             {"op": "count", "rev": rev,
                              "path": "../escape", "pattern": "x"}, "0")])
    cases.append(("unsafe path", repo, led, rev, 2, "REFUSED"))

    led = os.path.join(st, "argvshape.json")
    with open(led, "w") as fh:
        json.dump({"argv": ["git", "log"], "pairs": [
            _pair("A1", obs_ok, "3")]}, fh)
    cases.append(("argv-ledger shape", repo, led, rev, 2, "REFUSED"))

    led = os.path.join(st, "missingpath.json")
    _ledger(led, rev, [_pair("N1",
                             {"op": "count", "rev": rev,
                              "path": "absent.txt", "pattern": "x"}, "0")])
    cases.append(("missing blob", repo, led, rev, 2, "REFUSED"))

    # -- round-80 hardened-channel scenarios (W1 findings) --
    led = os.path.join(st, "replacerefs.json")
    _ledger(led, rerev, [_pair("RP1", obs_line1, "alpha",
                               stated_text="count 5",
                               stated_parse=r"count (5)")])
    cases.append(("replace refs refused", rerepo, led, rerev, 2, "replace"))

    led = os.path.join(st, "oversize.json")
    _ledger(led, rev, [_pair("Z1", obs_ok, "3",
                             stated_text="count 5 " + "x" * (1024 * 1024),
                             stated_parse=r"count (5)")])
    cases.append(("oversize ledger refused", repo, led, rev, 2, "input cap"))

    led = os.path.join(st, "deepnest.json")
    with open(led, "w") as fh:
        fh.write("[" * 100000 + "]" * 100000)
    cases.append(("deep-nested ledger refused", repo, led, rev, 2, "nested"))

    led = os.path.join(st, "dupobs.json")
    _ledger(led, rev, [_pair("D1", obs_ok, "3"),
                       _pair("D2", dict(obs_ok), "3")])
    cases.append(("duplicate observation refused", repo, led, rev, 2,
                  "duplicate"))

    for name, crepo, led, base, want, needle in cases:
        code, out = _run_cli(led, crepo, base, runw)
        ok = code == want and needle in out
        print("selftest: %s -> exit=%d want=%d %s as-expected=%s"
              % (name, code, want, needle, ok))
        if not ok:
            bad.append(name)
    print("SELFTEST: %s" % ("PASS" if not bad else "FAIL %s" % bad))
    if clean:
        shutil.rmtree(st, ignore_errors=True)
    return 0 if not bad else 1


if __name__ == "__main__":
    sys.exit(run())
