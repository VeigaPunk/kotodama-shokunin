"""Draft bounded-limits helpers for the round-79 ledger-token guard.

Seat: SentinelLimits (W1, pre-data). DRAFT ONLY, stage-local. ExecGuard owns the
production file tools/ledger-token-guard.py; L1 integrates. This module has no
dependency on the round-76 counter and never reads a worktree path: callers pass
committed bytes (from `git cat-file blob <rev>:<path>`) and an explicit scratch dir.

Stdlib only. Run `python3 -B ledger_limits_draft.py --selftest --work <dir>
--fixture-repo <git repo with big.txt, bad.txt at rev>` for the probe.

Exit labels (guard-facing, stable): refusals print `REFUSED <LABEL>: <detail>`
and the caller exits 2; a non-clean finding is the caller's exit 1; clean is 0.
"""
import json
import os
import re
import selectors
import signal
import subprocess
import sys
import time

# ---- limits (each number is justified in report SentinelLimits.md) -------------
LEDGER_MAX_BYTES = 1 << 20        # largest base ledger-shaped blob is 75,791 B
OBS_TIMEOUT_S = 20.0              # wall clock per observation; measured git grep ~0.6 s
RUN_BUDGET_S = 600.0              # wall clock for the whole guard run
OBS_STDOUT_MAX = 64 << 10         # 64 KiB; historical observations emit one count line
OBS_STDERR_MAX = 8 << 10
TOKEN_MAX_CHARS = 200             # refuse, never truncate (truncation fakes equality)
JSON_MAX_DEPTH = 32
JSON_MAX_NODES = 100_000
JSON_MAX_STR_CHARS = 64 << 10
JSON_MAX_INT_DIGITS = 18
ARGV_MAX_ITEMS = 32
ARGV_MAX_ITEM_CHARS = 1024
PAIRS_MAX = 256
READ_CHUNK = 65536

PARSE_CLOSED = ("count-presence", "exact")   # regex parse modes refused (see report)
ASCII_WS_RE = re.compile(r"[ \t\r\n\f\v]+")


class Refusal(Exception):
    def __init__(self, label, detail=""):
        super().__init__("%s: %s" % (label, detail))
        self.label = label
        self.detail = detail

    def line(self):
        return "REFUSED %s: %s" % (self.label, self.detail)


# ---- bounded subprocess ----------------------------------------------------------
def run_bounded(argv, cwd, env, timeout_s=OBS_TIMEOUT_S,
                stdout_max=OBS_STDOUT_MAX, stderr_max=OBS_STDERR_MAX):
    """Run argv in its own session with a wall deadline and per-stream byte caps.

    Returns (returncode, stdout_bytes, stderr_bytes). Raises Refusal:
      SPAWN         missing binary / OS error at exec
      TIMEOUT       deadline passed, or a pipe stayed open after the leader exited
      OUTPUT-CAP    a stream exceeded its cap (reading stops at cap + one chunk)
    The whole process group is SIGKILLed on every exit path, so a grandchild that
    inherited the pipes cannot outlive the observation.
    """
    if timeout_s <= 0:
        raise Refusal("TIMEOUT", "no budget left before spawn")
    try:
        p = subprocess.Popen(argv, cwd=cwd, env=env, stdin=subprocess.DEVNULL,
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                             start_new_session=True, close_fds=True)
    except OSError as exc:
        raise Refusal("SPAWN", "%s: %s" % (argv[0], exc))
    out_fd, err_fd = p.stdout.fileno(), p.stderr.fileno()
    caps = {out_fd: (stdout_max, "stdout"),
            err_fd: (stderr_max, "stderr")}
    bufs = {fd: bytearray() for fd in caps}
    sel = selectors.DefaultSelector()
    for fd in caps:
        sel.register(fd, selectors.EVENT_READ)
    deadline = time.monotonic() + timeout_s
    failure = None
    try:
        while sel.get_map() and failure is None:
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                failure = Refusal("TIMEOUT", "%s: %.1fs wall budget" % (argv[0], timeout_s))
                break
            for key, _ in sel.select(timeout=min(remaining, 0.25)):
                fd = key.fd
                chunk = os.read(fd, READ_CHUNK)
                if not chunk:
                    sel.unregister(fd)
                    continue
                bufs[fd] += chunk
                cap, name = caps[fd]
                if len(bufs[fd]) > cap:
                    failure = Refusal("OUTPUT-CAP", "%s over %d bytes" % (name, cap))
                    break
    finally:
        sel.close()
        try:
            os.killpg(p.pid, signal.SIGKILL)
        except (ProcessLookupError, PermissionError):
            pass
        rc = p.wait()
        p.stdout.close()
        p.stderr.close()
    if failure is not None:
        raise failure
    return rc, bytes(bufs[out_fd]), bytes(bufs[err_fd])


def argv_problem(argv):
    if not isinstance(argv, list) or not (1 <= len(argv) <= ARGV_MAX_ITEMS):
        return "argv must be a list of 1..%d items" % ARGV_MAX_ITEMS
    for item in argv:
        if not isinstance(item, str) or not item:
            return "argv item is not a non-empty string"
        if len(item) > ARGV_MAX_ITEM_CHARS:
            return "argv item of %d chars exceeds %d" % (len(item), ARGV_MAX_ITEM_CHARS)
        if "\x00" in item:
            return "argv item contains NUL"
    return None


# ---- strict text ------------------------------------------------------------------
def decode_strict(raw, what):
    """UTF-8 strict. Invalid bytes, encoded surrogates, NUL and a leading BOM refuse.

    Round-76 run_observe uses text=True, which raises UnicodeDecodeError out of
    subprocess.run where no handler exists; this turns that into a labelled refusal.
    """
    if b"\x00" in raw:
        raise Refusal("NUL-BYTE", what)
    try:
        text = raw.decode("utf-8", errors="strict")
    except UnicodeDecodeError as exc:
        raise Refusal("ENCODING", "%s: %s" % (what, str(exc)[:90]))
    if text.startswith("\ufeff"):
        raise Refusal("BOM", what)
    return text


def norm_token(text, what="token"):
    """Collapse ASCII whitespace only; refuse over-long tokens instead of truncating.

    The round-76 norm() uses str.split(), which also folds U+00A0 and U+3000 into
    spaces, so a stated `a\\u00a0b` would equal an observed `a b`. Here only
    [ \\t\\r\\n\\f\\v] is folded; any other code point stays distinct.
    """
    tok = ASCII_WS_RE.sub(" ", text).strip(" ")
    if len(tok) > TOKEN_MAX_CHARS:
        raise Refusal("TOKEN-TOO-LONG", "%s is %d chars" % (what, len(tok)))
    return tok


def parse_closed(mode, text):
    """Closed parse grammar: no regex, so no backtracking on hostile input."""
    if mode not in PARSE_CLOSED:
        raise Refusal("UNSUPPORTED-PARSE", "parse mode %r is not in %s" % (mode, PARSE_CLOSED))
    if mode == "exact":
        lines = text.rstrip("\n").split("\n")
        if len(lines) != 1:
            raise Refusal("PARSE", "exact mode needs one line, got %d" % len(lines))
        return norm_token(lines[0], "observed")
    line = text.strip()
    if "\n" in line:
        raise Refusal("PARSE", "count-presence needs one line")
    head, sep, count = line.rpartition(":")
    if not sep or not count.isdigit() or not head:
        raise Refusal("PARSE", "count-presence needs <path>:<digits>")
    return "present" if int(count) > 0 else "absent"


# ---- strict JSON ------------------------------------------------------------------
def _no_duplicate_keys(pairs):
    out = {}
    for key, value in pairs:
        if key in out:
            raise Refusal("DUP-KEY", repr(key[:60]))
        out[key] = value
    return out


def _refuse_constant(name):
    raise Refusal("NONSTD-CONST", name)


def _bounded_int(text):
    if len(text.lstrip("-")) > JSON_MAX_INT_DIGITS:
        raise Refusal("BIG-INT", "%d digits" % len(text.lstrip("-")))
    return int(text)


def _refuse_float(text):
    raise Refusal("FLOAT", text[:40])


def _check_tree(root, what):
    """Iterative walk: depth, node count, string length, lone surrogates, NUL."""
    stack = [(root, 1)]
    nodes = 0
    while stack:
        node, depth = stack.pop()
        nodes += 1
        if nodes > JSON_MAX_NODES:
            raise Refusal("NODES", "%s has more than %d nodes" % (what, JSON_MAX_NODES))
        if depth > JSON_MAX_DEPTH:
            raise Refusal("DEPTH", "%s deeper than %d" % (what, JSON_MAX_DEPTH))
        if isinstance(node, dict):
            for key, value in node.items():
                stack.append((key, depth + 1))
                stack.append((value, depth + 1))
        elif isinstance(node, list):
            stack.extend((item, depth + 1) for item in node)
        elif isinstance(node, str):
            if len(node) > JSON_MAX_STR_CHARS:
                raise Refusal("STR-TOO-LONG", "%s string of %d chars" % (what, len(node)))
            if "\x00" in node:
                raise Refusal("NUL-IN-STRING", what)
            try:
                node.encode("utf-8", errors="strict")
            except UnicodeEncodeError:
                raise Refusal("SURROGATE", "%s holds a lone surrogate" % what)


def load_json_strict(raw, what, max_bytes=LEDGER_MAX_BYTES):
    """Committed-bytes JSON load with every hostile-field path refused by label."""
    if len(raw) > max_bytes:
        raise Refusal("LIMIT-BYTES", "%s is %d bytes, cap %d" % (what, len(raw), max_bytes))
    text = decode_strict(raw, what)
    try:
        obj = json.loads(text, object_pairs_hook=_no_duplicate_keys,
                         parse_constant=_refuse_constant, parse_int=_bounded_int,
                         parse_float=_refuse_float)
    except RecursionError:
        raise Refusal("DEPTH", "%s overflowed the parser stack" % what)
    except json.JSONDecodeError as exc:
        raise Refusal("JSON", "%s: %s" % (what, str(exc)[:90]))
    _check_tree(obj, what)
    return obj


class Budget:
    def __init__(self, seconds=RUN_BUDGET_S):
        self.deadline = time.monotonic() + seconds

    def left(self):
        remaining = self.deadline - time.monotonic()
        if remaining <= 0:
            raise Refusal("BUDGET", "run wall budget exhausted")
        return remaining


def observe(argv, cwd, env, budget, timeout_s=OBS_TIMEOUT_S):
    """One bounded observation: argv check, bounded run, strict decode, closed parse input."""
    problem = argv_problem(argv)
    if problem:
        raise Refusal("ARGV", problem)
    rc, out, err = run_bounded(argv, cwd, env, timeout_s=min(timeout_s, budget.left()))
    return rc, decode_strict(out, "stdout of %s" % argv[0]), err
