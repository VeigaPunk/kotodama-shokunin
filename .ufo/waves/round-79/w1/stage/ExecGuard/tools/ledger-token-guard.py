#!/usr/bin/env python3
"""ledger-token-guard.py — bounded ledger-token guard for kotodama round 79.

Round 79 claim O (operability) build artifact, graded by the independent
acceptance counter accept-o.py.  The guard re-runs the approved read-only
observations of a calibration ledger against IMMUTABLE COMMITTED BYTES of one
base revision and validates the recorded tokens:

  * the ledger's observation is an argv ARRAY (never a shell string); the
    literal substring "{base}" in any element is replaced with the --base
    value before grammar checks and execution;
  * after substitution the observation must be PINNED at --base: at least one
    element equals --base or starts with "<base>:" — HEAD, a branch, another
    commit or a worktree target is a refusal;
  * argv[0] must be "git" with a read-only subcommand (show grep cat-file
    ls-tree rev-parse log diff ls-files rev-list merge-base); interpreters
    (python*, sh, bash, perl, node, ruby, …) and constant printers (echo,
    printf, true, yes, …) are refused because the only legal argv[0] is git;
    any shell metacharacter (| & ; < > ` $( CR LF) in any element is a
    refusal; an optional leading "-C <dir>" is allowed only when <dir>
    resolves inside --repo;
  * stated_text must equal the base blob's line stated_at names, and
    stated_parse must extract the stated token from stated_text;
  * the recorded observed_at_base must equal the re-run observation EXACTLY
    (no normalization), and the stated token must DIFFER from the observed
    token (a green-at-base pair is a failure, not a mismatch);
  * per-observe wall timeout 60 s and 1 MiB stdout cap; ledger file <= 1 MiB,
    <= 500 pairs; child environment scrubbed (HOME/TMPDIR pinned to --work).

Exit codes and stable labels:
  0  LEDGER-GUARD-79: PASS pairs=N
  1  LEDGER-GUARD-79: FAIL pairs=N problems=M
       per-pair lines:
       PAIR <id>: OBS_MISMATCH recorded='<r>' actual='<a>'
       PAIR <id>: NOT_RED token='<t>'
       PAIR <id>: STATED_MISMATCH ledger='<l>' blob='<b>'
       PAIR <id>: UNOBSERVABLE <why>
       PAIR <id>: UNPARSEABLE pattern='<p>'
  2  LEDGER-GUARD-79: FAIL (refused: <why>)
       usage errors, unreadable/malformed ledgers, strict-schema violations,
       grammar violations (interpreter/constant-printer/shell meta/mutable
       or unpinned revision) and an absent/unwritable --work.  A refusal is
       never a pair verdict.

A refusal (exit 2) is decided from the ledger file and CLI alone; anything
that requires touching the repository is a pair verdict (exit 1).

--emit PATH writes strict JSON the counter compares against its own
independent re-derivation:
  {"verdict": "PASS"|"FAIL",
   "pairs": [{"id": "A01", "observed": "2", "stated": "fixture …",
              "status": "ok|obs-mismatch|not-red|stated-mismatch|"
                        "unobservable|unparseable"}]}
(observed/stated are null when that side did not produce a token; the file is
written on refusals too, as {"verdict": "FAIL", "pairs": []}.)

Scope honesty: this guard validates base-observation tokens only.  It does
not grade REPAIR post-states, ANNOTATE rows, expected_after values, receipt
presence or any round acceptance leg — those belong to the round counter.
`disposition`, `expected_after` and `rederive` are carried as documentation
and are not executed or graded.  It does not certify historical truth; it
certifies that the ledger's recorded base observations reproduce from
committed bytes and that every pair is a true stated-vs-observed mismatch.

CLI:
  python3 -B ledger-token-guard.py --ledger PATH --repo PATH --base HEX40 \
      --work DIR [--emit PATH] [--selftest]
  --selftest builds its own tiny fixtures under --work (pinned commit dates)
  and ignores the other grading flags; it must exit 0 and prints one
  deterministic line starting with "SELFTEST:".
"""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys

TOOL = "ledger-token-guard"
PASS_LABEL = "LEDGER-GUARD-79: PASS"
FAIL_LABEL = "LEDGER-GUARD-79: FAIL"
REFUSED_LABEL = "LEDGER-GUARD-79: FAIL (refused: "

MAX_LEDGER_BYTES = 1 * 1024 * 1024
MAX_PAIRS = 500
MAX_STDOUT_BYTES = 1 * 1024 * 1024
MAX_STATED_BLOB_BYTES = 4 * 1024 * 1024
OBSERVE_TIMEOUT = 60
MAX_ID = 32
MAX_CLAIM = 32
MAX_PATH = 256
MAX_ELEMENT = 512
MAX_ARGV = 32
MAX_STATED_TEXT = 4096
MAX_PARSE = 512
MAX_RECORDED = 256
MAX_EXPECTED = 256
MAX_REDERIVE = 512
MAX_SHOWN = 80

HEX40_RE = re.compile(r"^[0-9a-f]{40}$")
ID_RE = re.compile(r"^[A-Za-z0-9_-]{1,32}$")
PATH_RE = re.compile(r"^[A-Za-z0-9_][A-Za-z0-9_./-]{0,255}$")
STATED_AT_RE = re.compile(r"^([A-Za-z0-9_][A-Za-z0-9_./-]{0,255}):([0-9]+)$")

TOP_KEYS = {"round", "claim", "base", "pairs"}
PAIR_KEYS = {"id", "disposition", "stated_at", "stated_text", "stated_parse",
             "observe_cmd", "parse", "expected_after", "observed_at_base",
             "rederive"}
GIT_SUBCOMMANDS = ("show", "grep", "cat-file", "ls-tree", "rev-parse", "log",
                   "diff", "ls-files", "rev-list", "merge-base")
SHELL_META = ("|", "&", ";", "<", ">", "`", "$(", "\r", "\n")

EXIT_PASS, EXIT_FAIL, EXIT_REFUSED = 0, 1, 2


class Refused(Exception):
    """exit-2 refusal: usage, malformed ledger, grammar violation."""


def _scrub(value):
    s = str(value)
    return s if len(s) <= MAX_SHOWN else s[:MAX_SHOWN] + "…(%d)" % len(s)


def _check_str(value, where, lo, hi):
    if not isinstance(value, str) or len(value) < lo or len(value) > hi:
        raise Refused("%s: not a string of length %d..%d"
                      % (where, lo, hi))


def _one_group(pattern, where):
    try:
        rx = re.compile(pattern)
    except re.error as exc:
        raise Refused("%s: regex does not compile: %s" % (where, exc))
    if rx.groups != 1:
        raise Refused("%s: regex must have exactly one capture group, has %d"
                      % (where, rx.groups))
    return rx


def _path_problem(path):
    if not isinstance(path, str) or not path:
        return "path is not a non-empty string"
    if len(path) > MAX_PATH:
        return "path longer than %d" % MAX_PATH
    if not PATH_RE.match(path):
        return "path %r fails the repo-relative shape" % _scrub(path)
    parts = path.split("/")
    if any(p in ("", ".", "..") for p in parts):
        return "path %r has an empty, '.' or '..' component" % _scrub(path)
    if "\\" in path:
        return "path %r contains a backslash" % _scrub(path)
    return None


def substitute_base(value, base, where):
    if not isinstance(value, str):
        raise Refused("%s: argv element is not a string" % where)
    return value.replace("{base}", base)


def check_observe_argv(raw_argv, base, repo, where):
    """Validate one observe_cmd after {base} substitution.

    Returns the substituted argv.  Raises Refused on any grammar violation."""
    if not isinstance(raw_argv, list) or not raw_argv:
        raise Refused("%s: observe_cmd is not a non-empty argv array" % where)
    if len(raw_argv) > MAX_ARGV:
        raise Refused("%s: observe_cmd longer than %d elements"
                      % (where, MAX_ARGV))
    argv = []
    for i, element in enumerate(raw_argv):
        element = substitute_base(element, base, "%s.observe_cmd[%d]"
                                  % (where, i))
        if len(element) > MAX_ELEMENT:
            raise Refused("%s.observe_cmd[%d]: element longer than %d"
                          % (where, i, MAX_ELEMENT))
        for bad in SHELL_META:
            if bad in element:
                raise Refused(
                    "%s.observe_cmd[%d]: shell metacharacter %r in element %r"
                    % (where, i, bad, _scrub(element)))
        argv.append(element)
    if argv[0] != "git":
        raise Refused(
            "%s.observe_cmd[0] %r: argv[0] must be 'git' — interpreters "
            "and constant printers are refused"
            % (where, _scrub(argv[0])))
    rest = argv[1:]
    if rest and rest[0] == "-C":
        if len(rest) < 2:
            raise Refused("%s.observe_cmd: '-C' without an operand" % where)
        target = rest[1]
        resolved = os.path.realpath(os.path.join(repo, target))
        root = os.path.realpath(repo)
        if resolved != root and not resolved.startswith(root + os.sep):
            raise Refused(
                "%s.observe_cmd: '-C %s' resolves outside the guarded repo"
                % (where, _scrub(target)))
        rest = rest[2:]
    if not rest:
        raise Refused("%s.observe_cmd: no git subcommand" % where)
    if rest[0] not in GIT_SUBCOMMANDS:
        raise Refused(
            "%s.observe_cmd: subcommand %r is not one of the read-only set "
            "%s" % (where, rest[0], list(GIT_SUBCOMMANDS)))
    pinned = any(a == base or a.startswith(base + ":") for a in argv)
    if not pinned:
        raise Refused(
            "%s.observe_cmd: not pinned at --base %s (no element equals it "
            "or starts with '<base>:'); mutable or foreign revisions are "
            "refused" % (where, base))
    return argv


def load_ledger(path, base, repo):
    """Read, substitute and strict-validate the ledger.

    Returns (pairs).  Raises Refused on any shape/grammar violation —
    everything here is decidable from the ledger file and CLI alone."""
    try:
        with open(path, "rb") as fh:
            raw = fh.read(MAX_LEDGER_BYTES + 1)
    except OSError as exc:
        raise Refused("ledger unreadable: %s" % exc)
    if len(raw) > MAX_LEDGER_BYTES:
        raise Refused("ledger larger than %d bytes" % MAX_LEDGER_BYTES)
    try:
        doc = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, ValueError) as exc:
        raise Refused("ledger is not valid UTF-8 JSON: %s" % exc)
    if not isinstance(doc, dict):
        raise Refused("ledger top level is not a JSON object")
    unknown = set(doc) - TOP_KEYS
    if unknown:
        raise Refused("unknown top-level key(s) %s (strict schema)"
                      % sorted(unknown))
    missing = TOP_KEYS - set(doc)
    if missing:
        raise Refused("missing top-level key(s) %s" % sorted(missing))
    round_no = doc["round"]
    if not isinstance(round_no, int) or isinstance(round_no, bool) \
            or round_no < 0:
        raise Refused("round: not an integer >= 0")
    _check_str(doc["claim"], "claim", 1, MAX_CLAIM)
    ledger_base = doc["base"]
    if not isinstance(ledger_base, str):
        raise Refused("base: not a string")
    ledger_base = ledger_base.replace("{base}", base)
    if not HEX40_RE.match(ledger_base):
        raise Refused("base %r is not 40 lowercase hex" % _scrub(ledger_base))
    if ledger_base != base:
        raise Refused("ledger base %s differs from --base %s"
                      % (ledger_base, base))
    pairs = doc["pairs"]
    if not isinstance(pairs, list) or not (1 <= len(pairs) <= MAX_PAIRS):
        raise Refused("pairs is not a list of length 1..%d" % MAX_PAIRS)
    seen = set()
    for i, pair in enumerate(pairs):
        where = "pairs[%d]" % i
        if not isinstance(pair, dict):
            raise Refused("%s is not an object" % where)
        unknown = set(pair) - PAIR_KEYS
        if unknown:
            raise Refused("%s unknown key(s) %s (strict schema)"
                          % (where, sorted(unknown)))
        missing = PAIR_KEYS - set(pair)
        if missing:
            raise Refused("%s missing key(s) %s" % (where, sorted(missing)))
        pid = pair["id"]
        if not isinstance(pid, str) or not ID_RE.match(pid):
            raise Refused("%s.id %r fails %s" % (where, _scrub(pid),
                                                 ID_RE.pattern))
        if pid in seen:
            raise Refused("duplicate pair id %r" % pid)
        seen.add(pid)
        _check_str(pair["disposition"], where + ".disposition", 1, 32)
        m = STATED_AT_RE.match(pair["stated_at"]
                               if isinstance(pair["stated_at"], str) else "")
        if not m:
            raise Refused("%s.stated_at %r is not <path>:<line>"
                          % (where, _scrub(pair["stated_at"])))
        stated_path, stated_line = m.group(1), int(m.group(2))
        if stated_line < 1:
            raise Refused("%s.stated_at line must be >= 1" % where)
        prob = _path_problem(stated_path)
        if prob:
            raise Refused("%s.stated_at: %s" % (where, prob))
        _check_str(pair["stated_text"], where + ".stated_text", 1,
                   MAX_STATED_TEXT)
        stated_rx = _one_group(pair["stated_parse"], where + ".stated_parse")
        if not stated_rx.search(pair["stated_text"]):
            raise Refused("%s.stated_parse does not match stated_text "
                          "(the ledger is self-inconsistent)" % where)
        pair["observe_argv"] = check_observe_argv(pair["observe_cmd"], base,
                                                  repo, where)
        _one_group(pair["parse"], where + ".parse")
        _check_str(pair["expected_after"], where + ".expected_after", 1,
                   MAX_EXPECTED)
        _check_str(pair["observed_at_base"], where + ".observed_at_base", 1,
                   MAX_RECORDED)
        _check_str(pair["rederive"], where + ".rederive", 1, MAX_REDERIVE)
        pair["stated_path"] = stated_path
        pair["stated_line"] = stated_line
    return pairs


# --------------------------------------------------------------------------
# repository observation: the ONLY subprocess channel
# --------------------------------------------------------------------------

def _child_env(work):
    return {
        "PATH": os.environ.get("PATH", "/usr/local/bin:/usr/bin:/bin"),
        "HOME": work,
        "TMPDIR": work,
        "LC_ALL": "C.UTF-8",
        "LANG": "C.UTF-8",
        "TZ": "UTC",
        "GIT_CONFIG_NOSYSTEM": "1",
        "GIT_TERMINAL_PROMPT": "0",
        "GIT_NO_REPLACE_OBJECTS": "1",
    }


def _git(repo, work, args, timeout=OBSERVE_TIMEOUT):
    try:
        proc = subprocess.run(
            ["git", "-C", repo] + args, cwd=work, capture_output=True,
            timeout=timeout, env=_child_env(work))
    except FileNotFoundError:
        raise Refused("git binary not found on PATH")
    except subprocess.TimeoutExpired:
        raise TimeoutError("git %s timed out after %ss"
                           % (" ".join(args), timeout))
    except OSError as exc:
        raise RuntimeError("git %s os-error: %s" % (" ".join(args), exc))
    return proc


def check_base_commit(repo, base, work):
    try:
        proc = _git(repo, work, ["cat-file", "-e", base + "^{commit}"])
    except TimeoutError as exc:
        raise Refused(str(exc))
    if proc.returncode != 0:
        raise Refused("base %s is not a commit object in %s (refusing a "
                      "mutable or foreign revision)" % (base, repo))


def check_work(work):
    try:
        os.makedirs(work, exist_ok=True)
        probe = os.path.join(work, ".guard-probe")
        with open(probe, "w") as fh:
            fh.write("ok")
        os.remove(probe)
    except OSError as exc:
        raise Refused("--work %s is not usable scratch: %s" % (work, exc))


def _stated_blob_lines(repo, work, base, path):
    try:
        proc = _git(repo, work, ["show", "%s:%s" % (base, path)])
    except TimeoutError as exc:
        return None, str(exc)
    if proc.returncode != 0:
        return None, "git show exit=%d: %s" % (
            proc.returncode,
            proc.stderr.decode("utf-8", "replace").strip()[:MAX_SHOWN])
    if len(proc.stdout) > MAX_STATED_BLOB_BYTES:
        return None, "stated blob larger than %d bytes" % \
            MAX_STATED_BLOB_BYTES
    return proc.stdout.decode("utf-8", "replace").splitlines(), None


def run_observe(repo, work, argv):
    """Execute one validated observation argv.  Returns (stdout, why|None).

    The argv runs with cwd=repo: a "-C ." operand is relative to the guarded
    repository (already validated to stay inside it); HOME/TMPDIR stay work."""
    try:
        proc = subprocess.run(argv, cwd=repo, capture_output=True,
                              timeout=OBSERVE_TIMEOUT,
                              env=_child_env(work))
    except FileNotFoundError:
        return None, "missing-binary:%s" % argv[0]
    except subprocess.TimeoutExpired:
        return None, "timeout:%ss" % OBSERVE_TIMEOUT
    except OSError as exc:
        return None, "os-error:%s" % exc
    if len(proc.stdout) > MAX_STDOUT_BYTES:
        return None, "stdout larger than %d bytes" % MAX_STDOUT_BYTES
    out = proc.stdout.decode("utf-8", "replace")
    if proc.returncode != 0:
        return None, "exit=%d: %s" % (
            proc.returncode, proc.stderr.decode("utf-8", "replace")
            .strip()[:MAX_SHOWN])
    return out, None


def evaluate_pairs(repo, work, base, pairs):
    """Second pass: stated-side binding + observation + token validation.

    Returns a list of per-pair dicts: {id, stated, observed, status, line}
    where line is the printed problem line or None."""
    results = []
    for pair in pairs:
        pid = pair["id"]
        stated_rx = re.compile(pair["stated_parse"], re.M)
        stated_token = stated_rx.search(pair["stated_text"]).group(1)

        # stated-side binding to committed bytes
        lines, why = _stated_blob_lines(repo, work, base, pair["stated_path"])
        if lines is None:
            results.append({"id": pid, "stated": stated_token,
                            "observed": None, "status": "stated-mismatch",
                            "line": "PAIR %s: STATED_MISMATCH blob='%s'"
                                    % (pid, _scrub(why))})
            continue
        if pair["stated_line"] > len(lines):
            results.append({
                "id": pid, "stated": stated_token, "observed": None,
                "status": "stated-mismatch",
                "line": "PAIR %s: STATED_MISMATCH stated_at='%s:%d' beyond "
                        "EOF (%d lines)" % (pid, pair["stated_path"],
                                            pair["stated_line"], len(lines))})
            continue
        blob_line = lines[pair["stated_line"] - 1]
        if blob_line != pair["stated_text"]:
            results.append({
                "id": pid, "stated": stated_token, "observed": None,
                "status": "stated-mismatch",
                "line": "PAIR %s: STATED_MISMATCH ledger='%s' blob='%s'"
                        % (pid, _scrub(pair["stated_text"]),
                           _scrub(blob_line))})
            continue

        # observation (argv already grammar-checked and substituted)
        out, why = run_observe(repo, work, pair["observe_argv"])
        if out is None:
            results.append({"id": pid, "stated": stated_token,
                            "observed": None, "status": "unobservable",
                            "line": "PAIR %s: UNOBSERVABLE %s"
                                    % (pid, _scrub(why))})
            continue
        parse_rx = re.compile(pair["parse"], re.M | re.S)
        m = parse_rx.search(out)
        if not m:
            results.append({"id": pid, "stated": stated_token,
                            "observed": None, "status": "unparseable",
                            "line": "PAIR %s: UNPARSEABLE pattern='%s'"
                                    % (pid, _scrub(pair["parse"]))})
            continue
        observed_token = m.group(1)

        if pair["observed_at_base"] != observed_token:
            results.append({
                "id": pid, "stated": stated_token, "observed": observed_token,
                "status": "obs-mismatch",
                "line": "PAIR %s: OBS_MISMATCH recorded='%s' actual='%s'"
                        % (pid, _scrub(pair["observed_at_base"]),
                           _scrub(observed_token))})
            continue
        if stated_token == observed_token:
            results.append({
                "id": pid, "stated": stated_token, "observed": observed_token,
                "status": "not-red",
                "line": "PAIR %s: NOT_RED token='%s'"
                        % (pid, _scrub(stated_token))})
            continue
        results.append({"id": pid, "stated": stated_token,
                        "observed": observed_token, "status": "ok",
                        "line": None})
    return results


def write_emit(path, verdict, results):
    doc = {"verdict": verdict,
           "pairs": [{"id": r["id"], "observed": r["observed"],
                      "stated": r["stated"], "status": r["status"]}
                     for r in results]}
    with open(path, "w") as fh:
        json.dump(doc, fh, indent=1, sort_keys=True)
        fh.write("\n")


def run_guard(ledger_path, repo, base, work, emit_path=None):
    """Grade one ledger.  Returns (exit_code, lines[])."""
    if not isinstance(base, str) or not HEX40_RE.match(base):
        raise Refused("--base %r is not 40 lowercase hex" % _scrub(base))
    if not os.path.isdir(repo):
        raise Refused("repo %s is not a directory" % repo)
    check_work(work)
    pairs = load_ledger(ledger_path, base, repo)
    check_base_commit(repo, base, work)

    results = evaluate_pairs(repo, work, base, pairs)
    problems = [r for r in results if r["status"] != "ok"]
    if problems:
        lines = ["%s pairs=%d problems=%d" % (FAIL_LABEL, len(pairs),
                                              len(problems))]
        lines += [r["line"] for r in problems]
        if emit_path:
            write_emit(emit_path, "FAIL", results)
        return EXIT_FAIL, lines
    lines = ["%s pairs=%d" % (PASS_LABEL, len(pairs))]
    if emit_path:
        write_emit(emit_path, "PASS", results)
    return EXIT_PASS, lines


# --------------------------------------------------------------------------
# selftest: hermetic fixture repositories under --work, red+green
# --------------------------------------------------------------------------

_FIXTURE_LOG = "\n".join([
    "# ledger fixture log",
    "## round 3 mint",
    "body line one",
    "## round 7 census",
    "body line two",
    "## round 9 close",
    "body line three",
    "",
])
_FIXTURE_README = "Total knowledge entries: 243.\n"
_PIN_ENV = dict(os.environ, GIT_AUTHOR_DATE="1980-01-01T00:00:00Z",
                GIT_COMMITTER_DATE="1980-01-01T00:00:00Z",
                GIT_AUTHOR_NAME="guard", GIT_AUTHOR_EMAIL="g@x.invalid",
                GIT_COMMITTER_NAME="guard",
                GIT_COMMITTER_EMAIL="g@x.invalid")


def _git_fixture(work, name):
    """Materialize one isolated fixture repo; return (dir, commit)."""
    root = os.path.abspath(os.path.join(work, "fixtures", name))
    os.makedirs(root)
    proc = subprocess.run(["git", "init", "-q", root], capture_output=True)
    if proc.returncode != 0:
        raise RuntimeError("git init failed: %s" % proc.stderr)
    top = subprocess.run(["git", "-C", root, "rev-parse", "--show-toplevel"],
                         capture_output=True, text=True)
    if top.returncode != 0 or top.stdout.strip() != root:
        raise RuntimeError("fixture root check failed: %r != %r"
                           % (top.stdout.strip(), root))
    with open(os.path.join(root, "LOG.md"), "w") as fh:
        fh.write(_FIXTURE_LOG)
    with open(os.path.join(root, "README.md"), "w") as fh:
        fh.write(_FIXTURE_README)
    subprocess.run(["git", "-C", root, "add", "LOG.md", "README.md"],
                   check=True, env=_PIN_ENV)
    subprocess.run(["git", "-C", root, "commit", "-q", "-m", "fixture"],
                   check=True, env=_PIN_ENV)
    commit = subprocess.run(["git", "-C", root, "rev-parse", "HEAD"],
                            capture_output=True, text=True, check=True,
                            env=_PIN_ENV).stdout.strip()
    return root, commit


def _clean_ledger(base, placeholder_base=False):
    b = "{base}" if placeholder_base else base
    return {
        "round": 79,
        "claim": "O",
        "base": b,
        "pairs": [
            {
                "id": "A01",
                "disposition": "ANNOTATE",
                "stated_at": "LOG.md:2",
                "stated_text": "## round 3 mint",
                "stated_parse": r"^## round ([0-9]+)",
                "observe_cmd": ["git", "-C", ".", "grep", "-c", "-E", "^#",
                                "{base}", "--", "LOG.md"],
                "parse": r":([0-9]+)$",
                "expected_after": "5",
                "observed_at_base": "4",
                "rederive": "git -C . grep -c -E '^#' {base} -- LOG.md",
            },
            {
                "id": "A02",
                "disposition": "ANNOTATE",
                "stated_at": "README.md:1",
                "stated_text": "Total knowledge entries: 243.",
                "stated_parse": r"Total knowledge entries: ([0-9]+)\.",
                "observe_cmd": ["git", "-C", ".", "grep", "-c", "-E", "Total",
                                "{base}", "--", "README.md"],
                "parse": r":([0-9]+)$",
                "expected_after": "244",
                "observed_at_base": "1",
                "rederive": "git -C . grep -c -E 'Total' {base} -- README.md",
            },
        ],
    }


def _write_json(path, doc):
    with open(path, "w") as fh:
        json.dump(doc, fh, indent=1)


def _deepcopy(doc):
    return json.loads(json.dumps(doc))


def selftest(work):
    """Run the red+green selftest; returns (exit_code, lines[])."""
    os.makedirs(work, exist_ok=True)
    lines = ["SELFTEST ledger-token-guard"]
    scenarios = []  # (name, exit_code, expect_code, expect_sub, hit)

    repo, base = _git_fixture(work, "clean")
    led_dir = os.path.join(work, "ledgers")
    os.makedirs(led_dir, exist_ok=True)

    def run_doc(name, doc, emit=None):
        path = os.path.join(led_dir, name + ".json")
        _write_json(path, doc)
        emit_path = os.path.join(led_dir, name + ".emit.json") if emit else None
        try:
            code, out = run_guard(path, repo, base,
                                  os.path.join(work, "run", name), emit_path)
        except Refused as exc:
            code, out = EXIT_REFUSED, ["%s%s)" % (REFUSED_LABEL, exc)]
            if emit_path:
                write_emit(emit_path, "FAIL", [])
        return code, out, emit_path

    def mutant(name, mutate, expect_code, expect_sub):
        doc = _deepcopy(_clean_ledger(base))
        mutate(doc)
        code, out, _e = run_doc(name, doc)
        hit = any(expect_sub in line for line in out)
        scenarios.append((name, code, expect_code, expect_sub, hit))

    # green baseline FIRST: every mutant below is judged against this green.
    code, out, emit_path = run_doc("clean", _clean_ledger(base), emit=True)
    clean_green = code == EXIT_PASS and out[0].startswith(PASS_LABEL)
    lines.append("scenario clean -> exit=%d %s" % (code, out[0]))
    scenarios.append(("clean", code, EXIT_PASS, PASS_LABEL, clean_green))
    # the emit of the clean run must agree with an in-process re-derivation
    # (mirrors what the acceptance counter does independently).
    emit_doc = json.load(open(emit_path))
    rederive_ok = (
        emit_doc["verdict"] == "PASS"
        and [p["id"] for p in emit_doc["pairs"]] == ["A01", "A02"]
        and emit_doc["pairs"][0]["observed"] == "4"
        and emit_doc["pairs"][0]["stated"] == "3"
        and emit_doc["pairs"][0]["status"] == "ok"
        and emit_doc["pairs"][1]["observed"] == "1"
        and emit_doc["pairs"][1]["stated"] == "243"
        and emit_doc["pairs"][1]["status"] == "ok")
    scenarios.append(("emit-agrees", EXIT_PASS if rederive_ok else EXIT_FAIL,
                      EXIT_PASS, "emit", rederive_ok))

    # {base} substitution end-to-end (top-level base and argv elements)
    code, out, _e = run_doc("substitute-base",
                            _clean_ledger(base, placeholder_base=True))
    scenarios.append(("substitute-base", code, EXIT_PASS, PASS_LABEL,
                      any(PASS_LABEL in line for line in out)))

    def m_obs_mismatch(d):
        d["pairs"][0]["observed_at_base"] = "3"
    mutant("obs-mismatch", m_obs_mismatch, EXIT_FAIL, "OBS_MISMATCH")

    def m_not_red(d):
        # stated "3"; counting lines matching "round" also yields 3 -> green.
        d["pairs"][0]["stated_parse"] = r"([0-9]+)"
        d["pairs"][0]["observe_cmd"] = ["git", "-C", ".", "grep", "-c", "-E",
                                        "round", "{base}", "--", "LOG.md"]
        d["pairs"][0]["observed_at_base"] = "3"
    mutant("not-red", m_not_red, EXIT_FAIL, "NOT_RED")

    def m_unobservable(d):
        d["pairs"][0]["observe_cmd"][-1] = "NOPE.md"
    mutant("unobservable", m_unobservable, EXIT_FAIL, "UNOBSERVABLE")

    def m_unparseable(d):
        d["pairs"][0]["parse"] = r"zzz([0-9]+)"
    mutant("unparseable", m_unparseable, EXIT_FAIL, "UNPARSEABLE")

    def m_stated_mismatch(d):
        d["pairs"][0]["stated_text"] = "## round 3 mint "
    mutant("stated-mismatch", m_stated_mismatch, EXIT_FAIL, "STATED_MISMATCH")

    def m_interpreter(d):
        d["pairs"][0]["observe_cmd"] = ["python3", "-c",
                                        "print('4')"]
    mutant("refuse-interpreter", m_interpreter, EXIT_REFUSED, "argv[0]")

    def m_printer(d):
        d["pairs"][0]["observe_cmd"] = ["echo", "4"]
    mutant("refuse-constant-printer", m_printer, EXIT_REFUSED, "argv[0]")

    def m_shell_meta(d):
        d["pairs"][0]["observe_cmd"].insert(1, ";")
    mutant("refuse-shell-meta", m_shell_meta, EXIT_REFUSED,
           "shell metacharacter")

    def m_unpinned_head(d):
        d["pairs"][0]["observe_cmd"] = ["git", "-C", ".", "grep", "-c", "-E",
                                        "^#", "HEAD", "--", "LOG.md"]
    mutant("refuse-unpinned-head", m_unpinned_head, EXIT_REFUSED,
           "not pinned at --base")

    def m_other_commit(d):
        d["pairs"][0]["observe_cmd"] = ["git", "show", "%s:LOG.md"
                                        % ("0" * 40)]
    mutant("refuse-other-commit", m_other_commit, EXIT_REFUSED,
           "not pinned at --base")

    def m_mut_sub(d):
        d["pairs"][0]["observe_cmd"] = ["git", "reset", "--hard", base]
    mutant("refuse-mutable-subcommand", m_mut_sub, EXIT_REFUSED,
           "read-only set")

    def m_traversal(d):
        d["pairs"][0]["observe_cmd"][1] = "-C"
        d["pairs"][0]["observe_cmd"][2] = ".."
    mutant("refuse-c-traversal", m_traversal, EXIT_REFUSED, "outside")

    def m_no_group(d):
        d["pairs"][0]["parse"] = r"[0-9]+"
    mutant("refuse-parse-no-group", m_no_group, EXIT_REFUSED, "capture group")

    def m_unknown_key(d):
        d["pairs"][0]["surprise"] = 1
    mutant("refuse-unknown-key", m_unknown_key, EXIT_REFUSED, "unknown key")

    def m_ledger_base_differs(d):
        d["base"] = "f" * 40
    mutant("refuse-ledger-base-differs", m_ledger_base_differs, EXIT_REFUSED,
           "differs from --base")

    # refusal: emit written on refusal too
    doc = _deepcopy(_clean_ledger(base))
    doc["pairs"][0]["observe_cmd"] = ["echo", "4"]
    code, out, emit_path = run_doc("refuse-emit-written", doc, emit=True)
    try:
        ed = json.load(open(emit_path))
        emit_refusal_ok = ed["verdict"] == "FAIL" and ed["pairs"] == []
    except (OSError, ValueError):
        emit_refusal_ok = False
    scenarios.append(("refuse-emit-written", code, EXIT_REFUSED, "argv[0]",
                      any("argv[0]" in l for l in out) and emit_refusal_ok))

    # repo-level refusals
    path = os.path.join(led_dir, "clean2.json")
    _write_json(path, _clean_ledger(base))
    try:
        run_guard(path, repo, "z" * 40, os.path.join(work, "run", "badhex"))
        code, out = EXIT_PASS, ["unexpected pass"]
    except Refused as exc:
        code, out = EXIT_REFUSED, ["%s%s)" % (REFUSED_LABEL, exc)]
    scenarios.append(("refuse-base-not-hex", code, EXIT_REFUSED,
                      "not 40 lowercase hex",
                      any("not 40 lowercase hex" in l for l in out)))
    try:
        run_guard(path, os.path.join(work, "no-such-repo"), base,
                  os.path.join(work, "run", "badrepo"))
        code, out = EXIT_PASS, ["unexpected pass"]
    except Refused as exc:
        code, out = EXIT_REFUSED, ["%s%s)" % (REFUSED_LABEL, exc)]
    scenarios.append(("refuse-repo-missing", code, EXIT_REFUSED,
                      "not a directory",
                      any("not a directory" in l for l in out)))
    doc_badbase = _clean_ledger("f" * 40)
    path_badbase = os.path.join(led_dir, "badbase.json")
    _write_json(path_badbase, doc_badbase)
    try:
        run_guard(path_badbase, repo, "f" * 40,
                  os.path.join(work, "run", "noobj"))
        code, out = EXIT_PASS, ["unexpected pass"]
    except Refused as exc:
        code, out = EXIT_REFUSED, ["%s%s)" % (REFUSED_LABEL, exc)]
    scenarios.append(("refuse-base-not-commit", code, EXIT_REFUSED,
                      "not a commit object",
                      any("not a commit object" in l for l in out)))
    # unwritable --work
    ro_dir = os.path.join(work, "readonly")
    os.makedirs(ro_dir, exist_ok=True)
    os.chmod(ro_dir, 0o500)
    try:
        run_guard(path, repo, base, os.path.join(ro_dir, "sub"))
        code, out = EXIT_PASS, ["unexpected pass"]
    except Refused as exc:
        code, out = EXIT_REFUSED, ["%s%s)" % (REFUSED_LABEL, exc)]
    finally:
        os.chmod(ro_dir, 0o700)
    scenarios.append(("refuse-unwritable-work", code, EXIT_REFUSED,
                      "not usable scratch",
                      any("not usable scratch" in l for l in out)))

    # usage error prints the stable refused label and exits 2
    import contextlib
    import io
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        ucode, _ulines = main(["ledger-token-guard", "--ledger", "x.json"])
    uout = buf.getvalue()
    scenarios.append(("refuse-usage-label", ucode, EXIT_REFUSED,
                      REFUSED_LABEL,
                      ucode == EXIT_REFUSED and REFUSED_LABEL in uout))

    # verdict accounting
    total = len(scenarios)
    good = sum(1 for s in scenarios if s[1] == s[2] and s[4])
    for name, code, expect_code, _sub, hit in scenarios:
        lines.append("scenario %s -> exit=%d (expect %d) %s"
                      % (name, code, expect_code,
                         "as-expected" if (code == expect_code and hit)
                         else "UNEXPECTED"))
    lines.append("SELFTEST: %d/%d scenarios green (clean green-first: %s)"
                 % (good, total, "yes" if clean_green else "NO"))
    code = EXIT_PASS if (good == total and clean_green) else EXIT_FAIL
    return code, lines


# --------------------------------------------------------------------------

def _usage_refused(msg):
    return EXIT_REFUSED, ["%s%s)" % (REFUSED_LABEL, msg),
                          "usage: %s --ledger PATH --repo PATH --base HEX40 "
                          "--work DIR [--emit PATH] [--selftest]" % TOOL]


def main(argv):
    args = list(argv[1:])
    if "--help" in args or "-h" in args:
        print(__doc__)
        return EXIT_PASS, []
    if "--selftest" in args:
        rest = [a for a in args if a != "--selftest"]
        work = None
        err = None
        i = 0
        while i < len(rest):
            if rest[i] == "--work" and i + 1 < len(rest):
                work = rest[i + 1]
                i += 2
            else:
                err = "unknown --selftest argument %r" % rest[i]
                break
        if err is None and work is None:
            work = os.environ.get("HYAKU_SCRATCH") or os.environ.get("TMPDIR")
            if not work:
                err = ("--selftest needs --work, HYAKU_SCRATCH or TMPDIR "
                       "(no ambient temp fallback)")
        if err is not None:
            code, lines = _usage_refused(err)
            for line in lines:
                print(line)
            return code, lines
        code, lines = selftest(os.path.abspath(work))
        for line in lines:
            print(line)
        return code, lines

    vals = {}
    i = 0
    err = None
    while i < len(args):
        a = args[i]
        if a in ("--ledger", "--repo", "--base", "--work", "--emit") \
                and i + 1 < len(args):
            vals[a[2:]] = args[i + 1]
            i += 2
        else:
            err = "unknown or dangling argument %r" % a
            break
    if err is None:
        for req in ("ledger", "repo", "base", "work"):
            if req not in vals:
                err = "missing --%s" % req
                break
    if err is not None:
        code, lines = _usage_refused(err)
        for line in lines:
            print(line)
        return code, lines
    try:
        code, lines = run_guard(os.path.abspath(vals["ledger"]),
                                os.path.abspath(vals["repo"]),
                                vals["base"],
                                os.path.abspath(vals["work"]),
                                os.path.abspath(vals["emit"])
                                if "emit" in vals else None)
    except Refused as exc:
        code, lines = EXIT_REFUSED, ["%s%s)" % (REFUSED_LABEL, exc)]
    for line in lines:
        print(line)
    return code, lines


if __name__ == "__main__":
    sys.exit(main(sys.argv)[0])
