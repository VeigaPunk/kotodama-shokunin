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

OUTPUT CONTRACT (greppable, diffable):

  pair <id>: ok observed=<token>             - pair verified
  pair <id>: fail MISMATCH recorded=<r> actual=<a>
  pair <id>: fail VACUOUS token=<t>          - stated == observed
  LEDGER-TOKEN-GUARD: PASS pairs=<n>
  LEDGER-TOKEN-GUARD: FAIL pairs=<n> failed=<m> mismatched=<k> vacuous=<v>
  LEDGER-TOKEN-GUARD: REFUSED <reason>       - exit 2, nothing graded

Exit: 0 every pair ok; 1 at least one pair failed; 2 refusal
(unreadable/invalid input, mutable rev, unknown op, unsafe path, missing
blob, ledger/base argument mismatch). Refusals always carry the
LEDGER-TOKEN-GUARD label and never print pair verdicts.

SELF-CONTAINED SELFTEST: `--selftest --work <dir>` builds a fresh fixture
git repository under <dir> (never reusing an existing path), commits a
probe file, runs every schema check and both defect-class detectors
against it, and prints one `as-expected` line per scenario plus
`SELFTEST: PASS`. Every scenario must land on its expected exit class or
the selftest fails; the fixture repositories are left under the work dir
for inspection unless run with `--clean`.

LIMITS, STATED: this guard re-checks recorded observations; it does not
certify that the original observation was approved, that the stated token
is the right thing to measure, or that the pair's prose is honest. Those
remain reviewer obligations. It grades committed bytes only: a ledger
pointing at the worktree, or at bytes outside --repo, cannot be checked
here by design.
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
GIT_ENV_DROP = ("GIT_DIR", "GIT_WORK_TREE", "GIT_INDEX_FILE", "GIT_NAMESPACE",
                "GIT_OBJECT_DIRECTORY")
FORBIDDEN_TOP = ("argv", "command", "run", "cmd", "observe_cmd", "shell",
                 "exec")
OPS = ("count", "line")


class Refusal(Exception):
    """Input problem: refuse, exit 2, stable label, nothing graded."""


def _env(extra=None):
    env = {k: v for k, v in os.environ.items() if k not in GIT_ENV_DROP}
    env.update(GIT_CONFIG_GLOBAL=os.devnull, GIT_CONFIG_NOSYSTEM="1",
               LC_ALL="C")
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
    try:
        doc = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, ValueError) as exc:
        raise Refusal("ledger is not a JSON object: %s" % exc)
    _require(isinstance(doc, dict), "ledger top level is not an object")
    bad = [k for k in doc if k in FORBIDDEN_TOP]
    _require(not bad, "ledger carries command-channel keys: %s"
             % ",".join(sorted(bad)))
    pairs = doc.get("pairs")
    _require(isinstance(pairs, list) and pairs,
             "ledger has no non-empty pairs array")
    seen = set()
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


def selftest(work, clean):
    _require(work and os.path.isdir(work),
             "--work must name an existing scratch directory")
    st = os.path.join(work, "ledger-token-guard-selftest")
    _require(not os.path.exists(st),
             "selftest fixture root %s already exists" % st)
    os.makedirs(st)
    repo, rev = _mkrepo(st, "fixture-repo")
    bad = []
    runw = os.path.join(st, "run")
    os.mkdir(runw)

    obs_ok = {"op": "count", "rev": rev, "path": "probe.txt",
              "pattern": "a$"}
    obs_line = {"op": "line", "rev": rev, "path": "probe.txt",
                "pattern": r"entries: ([0-9]+)", "line": 4}
    cases = []

    led = os.path.join(st, "green.json")
    _ledger(led, rev, [_pair("G1", obs_ok, "3"),
                       _pair("G2", obs_line, "42",
                             stated_text="entries: 9",
                             stated_parse=r"entries: ([0-9]+)")])
    cases.append(("green all pairs", led, rev, 0, "PASS pairs=2"))

    led = os.path.join(st, "mismatch.json")
    _ledger(led, rev, [_pair("M1", obs_ok, "1")])
    cases.append(("recorded!=observed", led, rev, 1, "MISMATCH"))

    led = os.path.join(st, "vacuous.json")
    _ledger(led, rev, [_pair("V1", obs_ok, "3", stated_text="count 3",
                             stated_parse=r"count (3)")])
    cases.append(("stated==observed", led, rev, 1, "VACUOUS"))

    led = os.path.join(st, "mutablerev.json")
    _ledger(led, rev, [_pair("R1",
                             dict(obs_ok, rev="HEAD"), "3")])
    cases.append(("mutable observe.rev", led, rev, 2, "REFUSED"))

    led = os.path.join(st, "badbase.json")
    _ledger(led, rev, [_pair("B1", obs_ok, "3")])
    with open(led) as fh:
        d = json.load(fh)
    d["base"] = "0" * 40
    with open(led, "w") as fh:
        json.dump(d, fh)
    cases.append(("ledger/base mismatch", led, rev, 2, "REFUSED"))

    led = os.path.join(st, "badop.json")
    _ledger(led, rev, [_pair("O1",
                             {"op": "exec", "rev": rev, "path": "probe.txt",
                              "pattern": "x"}, "0")])
    cases.append(("unknown op", led, rev, 2, "REFUSED"))

    led = os.path.join(st, "badpath.json")
    _ledger(led, rev, [_pair("P1",
                             {"op": "count", "rev": rev,
                              "path": "../escape", "pattern": "x"}, "0")])
    cases.append(("unsafe path", led, rev, 2, "REFUSED"))

    led = os.path.join(st, "argvshape.json")
    with open(led, "w") as fh:
        json.dump({"argv": ["git", "log"], "pairs": [
            _pair("A1", obs_ok, "3")]}, fh)
    cases.append(("argv-ledger shape", led, rev, 2, "REFUSED"))

    led = os.path.join(st, "missingpath.json")
    _ledger(led, rev, [_pair("N1",
                             {"op": "count", "rev": rev,
                              "path": "absent.txt", "pattern": "x"}, "0")])
    cases.append(("missing blob", led, rev, 2, "REFUSED"))

    for name, led, base, want, needle in cases:
        code, out = _run_cli(led, repo, base, runw)
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
