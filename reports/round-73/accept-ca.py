#!/usr/bin/env python3
r"""Round-73 calibration acceptance counter — claim Ca (ledger-driven).

Claim Ca (reports/round-73/claims.json, DRAFT until the freeze commit) grades
the round's self-assessment-versus-repo-state ledger.  This counter is
data-driven: it reads the ledger and recomputes every observation from
committed bytes, so the frozen pair set is fixed at freeze without touching
this file.

LEDGER SCHEMA (reports/round-73/ledger.json, committed before data)

  {
    "round": 73,
    "claim": "Ca",
    "base":  "<40hex lane commit the ledger was measured from>",
    "fleet_pin": "<40hex fleet commit the round-72 fleet report is pinned at>",
    "pairs": [
      {
        "id":            "R1",                     unique, non-empty
        "stated_at":     "SCORECARD.md:1401",      path:line at --lands
        "stated_text":   "<verbatim line>",        normalized-substring of
                                                   that file at --lands
        "stated_token":  "<token quoted from stated_text>"   optional;
                                                   default = stated_text,
                                                   or the match of the
                                                   optional "stated_parse"
                                                   regex over stated_text
        "observe_cmd":   ["grep", "-ho", "..."],   argv list; NEVER a shell
                                                   string (see SHELL GUARD)
        "parse":         "ACCEPT-CA-72: (PASS)",   optional regex; capture
                                                   group 1 (else whole match)
                                                   is the observed token
        "expected_after":"PASS",                   the value at --lands
        "disposition":   "REPAIR" | "ANNOTATE",
        "rederive":      "<human re-derivation command>"     optional;
                                                   default = shlex.join of
                                                   observe_cmd
      }
    ]
  }

  A top-level bare list of pairs is also accepted (round/claim/base/fleet_pin
  then have no home and the LEDGER leg fails closed).  Extra keys are allowed.

LEGS (8, fixed at freeze)

  LEDGER        the ledger is readable at --lands (a worktree read is
                disclosed in the receipt header and is only allowed for an
                explicitly named --ledger, e.g. a fixture run); it declares
                round 73, claim Ca, base == the counter's base; it holds
                >= --min-pairs unique pairs; every pair is structurally
                valid: argv list, compilable capture regex, resolvable
                path:line, stated_text present in that file at lands, stated
                token anchored in stated_text, disposition in the frozen set.
  BASEMISMATCH  at the base revision the same ledger yields >= --min-pairs
                pairs whose stated token disagrees with the observed token
                (the do-nothing control).  A pair whose observe_cmd cannot
                run at base (missing binary, timeout, empty stdout with a
                nonzero exit) makes this leg FAIL closed.
  REPAIR        every REPAIR pair observes expected_after at --lands.
  ANNOTATE      every ANNOTATE pair has a row under SCORECARD.md
                "## Corrections — round 73" naming the pair id, the stated
                token and the observed token at --lands; the leg prints the
                unannotated count (the claim's after-state is 0).
  APPENDONLY    zero removed lines in LOG.md, SCORECARD.md,
                corpus/lessons/round-72.md, corpus/lessons/round-71.md
                (lane, base..lands) and in the fleet round-72 report
                (.ufo/reports/round-72/kotodama.md, pinned by the ledger's
                fleet_pin: identical blob, zero removed lines); in-place
                edits are authorized only inside SKILL.md
                "## Gates and probes" or a README footer, and only for a
                file a ledger pair names in stated_at.
  NOSTUB        every correction row also carries the pair's re-derivation
                command (rederive, default shlex.join(observe_cmd)) and
                carries no placeholder token (round-69 stub-row class: a row
                naming only the id).
  SEPARABLE     no byte the Ca legs READ (the ledger text, the round-73
                corrections rows that name a pair id, and Ca telemetry
                receipts under reports/round-73/telemetry/ whose basename
                contains "ca") cites a lane S-id >= 876 or a claim-C path;
                the ledger's observe_cmd / expected_after / parse strings
                name no claim-C path either.  The counter source is not in
                the scan set: it must name the C paths it tests for, so a
                self-scan would be incoherent.
  STAMP         the receipt names the stamped/evaluated/measured revision,
                the lands tree hash and the counter sha256 (QUALITY 17/19
                header lines, grammar of tools/check-receipt-seq.py), with
                stamped == evaluated == measured == --lands, tree ==
                `git rev-parse <lands>^{tree}`, and the evaluation ran
                inside a clone materialized at --lands (clone HEAD and tree
                re-derived, every observe_cmd cwd inside the clone).

PREDICATE AMBIGUITIES, STATED (the frozen text does not decide these)

  * "mismatch pair" at base is formalized as stated-token != observed-token
    (the self-assessment disagrees with the repo state).  A mismatch is
    therefore disposition-independent: an ANNOTATE pair is a mismatch at base
    and at lands, and is closed by its correction row, not by a repo change.
  * The frozen pair shape names no "stated token"; ANNOTATE/NOSTUB require
    one, so the counter derives it from stated_text (explicit stated_token or
    stated_parse), and requires it to be anchored in stated_text.  An
    omission-class defect (R3: rows missing) must therefore anchor its token
    on a stated line (e.g. the registry's last accept row), not on the
    absence itself.
  * The frozen APPENDONLY leg names no fleet revision; the counter requires
    the ledger-level fleet_pin and fails closed without it.
  * The frozen ledger leg names no "parse" field; the counter accepts it as
    an optional capture regex and falls back to the raw stdout token
    (flagged PARSE-MISS in the receipt) when the regex does not match.
  * --min-pairs exists only so a fixture ledger can exercise BASEMISMATCH
    before the real 8-pair ledger is frozen; its value is disclosed in the
    receipt header and the graded run uses the default 8.
  * A ledger with zero ANNOTATE pairs makes ANNOTATE and NOSTUB vacuous; the
    receipt prints "annotate-pairs=0 (vacuous)".

EXIT: 0 all legs pass; 1 any leg fails; 2 input error (bad --lands, missing
base, ledger unreadable, clone/materialization failure, --selftest failure).

USAGE

  python3 -B .ufo/waves/round-73/counters/accept-ca.py --root . \
      --lands <40hex> --fleet-root /home/vgpnk/Projects/shokunin
  python3 -B .ufo/waves/round-73/counters/accept-ca.py --selftest
"""
import argparse
import hashlib
import io
import json
import os
import re
import shlex
import shutil
import subprocess
import sys
import tempfile
from contextlib import redirect_stdout

BASE = "8841ad3b896a0227674fa0725b818c999118046f"
ROUND = 73
CLAIM = "Ca"
LEDGER_REL = "reports/round-73/ledger.json"
SCORECARD_REL = "SCORECARD.md"
CORR_HEADING_RE = re.compile(r"^##\s+Corrections\s*[—–-]\s*round\s+73\b", re.I)
REGISTRY_HEADING_RE = re.compile(r"^##\s+Gates and probes\s*$")
APPENDONLY_FILES = ("LOG.md", "SCORECARD.md",
                    "corpus/lessons/round-72.md", "corpus/lessons/round-71.md")
FLEET_R72_REPORT = ".ufo/reports/round-72/kotodama.md"
INPLACE_PATHS = ("SKILL.md", "corpus/README.md", "README.md")
CA_TELEMETRY_DIR = "reports/round-73/telemetry"
SEPARABLE_MIN_ID = 876
C_PATHS = ("corpus/knowledge/linguistics/conlang-scholarship", "corpus/lessons/round-73.md",
           "reports/round-73/accept-c.py", "reports/round-73/evidence", "corpus/SOURCES.md")
SID_RE = re.compile(r"(?<![A-Za-z0-9_])S(\d{3,})(?![0-9])")
OBSERVE_ALLOW = {"git", "grep", "find", "wc", "ls", "cat", "sha256sum", "stat", "python3"}
SHELLS = {"sh", "bash", "zsh", "dash", "ksh", "fish", "csh", "tcsh"}
STUB_TOKENS = {"", "?", "??", "???", "tbd", "n/a", "na", "none", "todo",
               "fixme", "<old>", "<new>", "old", "new", "...", "…", "-"}
MIN_PAIRS = 8
OBSERVE_TIMEOUT = 120
DISPOSITIONS = ("REPAIR", "ANNOTATE")

RUN_STATE = {"outside_clone": False}


# --------------------------------------------------------------------------
# primitives
# --------------------------------------------------------------------------
def git(root, *args, timeout=300):
    return subprocess.run(["git", "-C", str(root), *args],
                          capture_output=True, text=True, timeout=timeout)


def show(root, rev, path):
    r = git(root, "show", "%s:%s" % (rev, path))
    if r.returncode != 0:
        return None
    return r.stdout


def norm(text):
    return " ".join((text or "").split())


def sha256_bytes(data):
    return hashlib.sha256(data if isinstance(data, bytes) else data.encode()).hexdigest()


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def leg(out, name, passed, detail=""):
    out.append((name, bool(passed), detail))
    print("LEG %s %s" % ("PASS" if passed else "FAIL", name))
    if detail:
        print("     %s" % detail)
    return bool(passed)


def note(text):
    print("     NOTE %s" % text)


def section_of(text, heading_re):
    """Return the body of the first section whose heading matches."""
    lines = text.splitlines()
    out, started = [], False
    for line in lines:
        if not started:
            if heading_re.match(line):
                started = True
                out.append(line)
            continue
        if re.match(r"^##\s", line) and not heading_re.match(line):
            break
        out.append(line)
    return "\n".join(out) if started else ""


def section_range(text, heading_re):
    """1-based (start, end) of the first matching section, heading included."""
    lines = text.splitlines()
    start = None
    for i, line in enumerate(lines, 1):
        if heading_re.match(line):
            start = i
            continue
        if start is not None and re.match(r"^##\s", line):
            return (start, i - 1)
    if start is not None:
        return (start, len(lines))
    return None


def footer_range(text):
    """1-based (start, end) of a README footer: from the last totals line or
    the last level-2 heading, whichever is later, to EOF."""
    lines = text.splitlines()
    totals = [i for i, l in enumerate(lines, 1)
              if re.match(r"^Total knowledge entries:", l)]
    heads = [i for i, l in enumerate(lines, 1) if re.match(r"^##\s", l)]
    anchors = totals + heads
    if not anchors:
        return (1, len(lines))
    return (max(anchors), len(lines))


def in_span(line_no, span, appended=0):
    if span is None or not line_no:
        return False
    return span[0] <= line_no <= span[1] + appended


def changed_hunks(root, base, lands, path):
    """(old_start, old_count, new_start, new_count) per hunk, -U0."""
    d = git(root, "diff", "-U0", "--no-color", "%s..%s" % (base, lands),
            "--", path)
    hunks = []
    for line in d.stdout.splitlines():
        m = re.match(r"^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@", line)
        if m:
            hunks.append((int(m.group(1)), int(m.group(2) or 1),
                          int(m.group(3)), int(m.group(4) or 1)))
    return hunks


def numstat_removed(root, rev_a, rev_b, paths):
    r = git(root, "diff", "--numstat", "--no-renames", "%s..%s" % (rev_a, rev_b),
            "--", *paths)
    total = 0
    for line in r.stdout.splitlines():
        parts = line.split()
        if len(parts) >= 2 and parts[1].isdigit():
            total += int(parts[1])
    return total, r.stdout


def added_lines(root, base, lands, paths):
    d = git(root, "diff", "-U0", "--no-color", "%s..%s" % (base, lands),
            "--", *paths)
    return [l[1:] for l in d.stdout.splitlines()
            if l.startswith("+") and not l.startswith("+++")]


# --------------------------------------------------------------------------
# evaluation harness
# --------------------------------------------------------------------------
def materialize(root, rev, tmpdir, label):
    dest = os.path.join(tmpdir, label)
    r = git(root, "clone", "--quiet", "--no-checkout",
            os.path.abspath(root), dest)
    if r.returncode != 0:
        print("ERROR: clone of %s failed: %s" % (root, r.stderr.strip()),
              file=sys.stderr)
        return None
    c = git(dest, "checkout", "--quiet", "--detach", rev)
    if c.returncode != 0:
        print("ERROR: checkout %s failed: %s" % (rev, c.stderr.strip()),
              file=sys.stderr)
        return None
    head = git(dest, "rev-parse", "HEAD").stdout.strip()
    tree = git(dest, "rev-parse", "HEAD^{tree}").stdout.strip()
    if head != rev:
        print("ERROR: clone HEAD %s != %s" % (head, rev), file=sys.stderr)
        return None
    return {"path": dest, "head": head, "tree": tree}


def argv_problem(argv):
    """The observe_cmd must be an argv list, never a shell string."""
    if not isinstance(argv, list) or not argv:
        return "observe_cmd is not a non-empty argv list"
    for a in argv:
        if not isinstance(a, str) or not a:
            return "observe_cmd element is not a non-empty string"
    if os.path.basename(argv[0]) in SHELLS:
        return "shell interpreter as argv[0]: %s" % argv[0]
    if os.path.basename(argv[0]) not in OBSERVE_ALLOW:
        return "argv[0] %r not in the observe allowlist %s (echo/printf channels are closed)" % (
            argv[0], sorted(OBSERVE_ALLOW))
    if os.path.basename(argv[0]).startswith("python"):
        if len(argv) < 3 or argv[1] != "-c":
            return "python3 is allowed only as `python3 -c <code>`"
        code = argv[2]
        if not re.search(r"pathlib|open\(|subprocess|os\.", code):
            return "python3 -c code must read the clone (pathlib/open/subprocess/os)"
        if re.search(r"(?i)\bprint\(\s*(['\"])[^'\"]*\1\s*\)", code):
            return "python3 -c code prints a literal (echo channel)"
    for a in argv:
        for bad in ("|", "$(", "`", "&&"):
            if bad in a:
                return "shell construct %r in argv element %r" % (bad, a[:60])
    return None


def run_observe(clone_path, argv, cwd_is_clone=True):
    """Run argv with cwd inside the materialized clone; return (stdout, why)."""
    if not cwd_is_clone:
        RUN_STATE["outside_clone"] = True
    env = {
        "PATH": os.environ.get("PATH", "/usr/local/bin:/usr/bin:/bin"),
        "HOME": os.environ.get("HOME", "/tmp"),
        "TMPDIR": os.environ.get("TMPDIR", "/tmp"),
        "LC_ALL": "C.UTF-8",
        "LANG": "C.UTF-8",
        "TZ": "UTC",
        "GIT_CONFIG_NOSYSTEM": "1",
        "GIT_TERMINAL_PROMPT": "0",
    }
    try:
        p = subprocess.run(argv, cwd=clone_path, capture_output=True,
                           text=True, timeout=OBSERVE_TIMEOUT, env=env)
    except FileNotFoundError:
        return None, "missing-binary:%s" % argv[0]
    except subprocess.TimeoutExpired:
        return None, "timeout:%ss" % OBSERVE_TIMEOUT
    except OSError as exc:
        return None, "os-error:%s" % exc
    if p.stdout.strip() == "" and p.returncode != 0:
        return None, "empty-stdout-exit=%d" % p.returncode
    return p.stdout, "exit=%d" % p.returncode


def observed_token(pair, clone_path):
    """(token, parsed, why) for one pair inside one materialized clone."""
    why = argv_problem(pair.get("observe_cmd"))
    if why:
        return None, False, "invalid-observe_cmd:%s" % why
    out, why = run_observe(clone_path, pair["observe_cmd"])
    if out is None:
        return None, False, why
    parse = pair.get("parse")
    if parse:
        m = re.search(parse, out, re.M | re.S)
        if m:
            tok = m.group(1) if m.groups() else m.group(0)
            return norm(tok), True, why
        return norm(out)[:200], False, "parse-miss(%s)" % why
    return norm(out)[:200], True, why


def stated_token(pair):
    if pair.get("stated_parse"):
        m = re.search(pair["stated_parse"], pair["stated_text"], re.M)
        if m:
            return norm(m.group(1) if m.groups() else m.group(0)), True
        return None, False
    if pair.get("stated_token"):
        return norm(pair["stated_token"]), True
    return norm(pair["stated_text"]), True


def rederive_text(pair):
    if pair.get("rederive"):
        return norm(pair["rederive"])
    return norm(shlex.join(pair["observe_cmd"]))


def load_ledger(root, clone, lands, ledger_arg):
    """(obj, source, sha, raw, error). source: 'lands' | 'worktree-uncommitted'."""
    rel = ledger_arg
    if not os.path.isabs(rel):
        r = git(clone["path"] if isinstance(clone, dict) else clone,
                "show", "%s:%s" % (lands, rel))
        if r.returncode == 0:
            raw = r.stdout
            try:
                return json.loads(raw), "lands", sha256_bytes(raw), raw, None
            except ValueError as exc:
                return None, "lands", sha256_bytes(raw), raw, \
                    "ledger JSON: %s" % exc
    cand = rel if os.path.isabs(rel) else os.path.join(root, rel)
    if os.path.isfile(cand):
        with open(cand, encoding="utf-8") as fh:
            raw = fh.read()
        try:
            return (json.loads(raw), "worktree-uncommitted", sha256_bytes(raw),
                    raw, None)
        except ValueError as exc:
            return None, "worktree-uncommitted", sha256_bytes(raw), raw, \
                "ledger JSON: %s" % exc
    return None, "absent", None, "", \
        "ledger unreadable at %s and in the worktree" % rel


# --------------------------------------------------------------------------
# legs
# --------------------------------------------------------------------------
def leg_ledger(out, pairs, meta, base, min_pairs, texts):
    problems = []
    if meta.get("round") != ROUND:
        problems.append("round=%r" % meta.get("round"))
    if meta.get("claim") != CLAIM:
        problems.append("claim=%r" % meta.get("claim"))
    if meta.get("base") != base:
        problems.append("base=%r != %s" % (meta.get("base"), base))
    if len(pairs) < min_pairs:
        problems.append("pairs=%d < min-pairs=%d" % (len(pairs), min_pairs))
    seen = set()
    for idx, pair in enumerate(pairs):
        tag = pair.get("id") if isinstance(pair, dict) else "#%d" % idx
        if not isinstance(pair, dict):
            problems.append("%s: not an object" % tag)
            continue
        pid = pair.get("id")
        if not isinstance(pid, str) or not pid.strip():
            problems.append("%s: empty id" % tag)
        elif pid in seen:
            problems.append("%s: duplicate id" % pid)
        else:
            seen.add(pid)
        if pair.get("disposition") not in DISPOSITIONS:
            problems.append("%s: disposition=%r" % (tag, pair.get("disposition")))
        why = argv_problem(pair.get("observe_cmd"))
        if why:
            problems.append("%s: %s" % (tag, why))
        elif "--others" in pair["observe_cmd"]:
            note("%s observe_cmd uses ls-files --others: a clone carries no "
                 "untracked files, so that observation reads 0 at every "
                 "revision — encode the tracked-count predicate instead" % tag)
        if "parse" in pair and pair["parse"] is not None:
            if not isinstance(pair["parse"], str):
                problems.append("%s: parse is not a string" % tag)
            else:
                try:
                    rx = re.compile(pair["parse"])
                except re.error as exc:
                    problems.append("%s: parse does not compile: %s" % (tag, exc))
                else:
                    if not rx.groups:
                        problems.append("%s: parse has no capture group" % tag)
        if not isinstance(pair.get("expected_after"), str) \
                or not pair["expected_after"].strip():
            problems.append("%s: expected_after is not a non-empty string" % tag)
        stated_at = pair.get("stated_at")
        m = re.match(r"^(.+):(\d+)$", stated_at or "")
        if not m:
            problems.append("%s: stated_at=%r is not path:line" % (tag, stated_at))
        else:
            path, line_no = m.group(1), int(m.group(2))
            body = texts.get(path)
            if body is None:
                problems.append("%s: stated_at path %s absent at base" % (tag, path))
            elif line_no < 1 or line_no > len(body.splitlines()):
                problems.append("%s: stated_at %s:%d beyond EOF (%d lines)"
                                % (tag, path, line_no, len(body.splitlines())))
            else:
                st = norm(pair.get("stated_text") or "")
                if not st:
                    problems.append("%s: empty stated_text" % tag)
                elif st not in norm(body):
                    problems.append("%s: stated_text not found in %s at base"
                                    % (tag, path))
                else:
                    line = norm(body.splitlines()[line_no - 1])
                    if st not in line:
                        note("%s stated_text is in %s but not on line %d"
                             % (tag, path, line_no))
        tok, ok = stated_token(pair)
        if not ok:
            problems.append("%s: stated_parse does not match stated_text" % tag)
        elif tok is not None and norm(pair.get("stated_text") or "") != "":
            if tok not in norm(pair.get("stated_text") or ""):
                problems.append("%s: stated token %r not anchored in stated_text"
                                % (tag, tok[:40]))
    detail = ("pairs=%d min=%d" % (len(pairs), min_pairs))
    if problems:
        detail += " problems=%d %s" % (len(problems), problems[:6])
    return leg(out, "LEDGER", not problems, detail)


def statement_after(pair, clone_path):
    """Re-read the statement side at the clone: pair["statement_after"] =
    {"path": <lane path>, "parse": <regex, capture group 1, applied with DOTALL so
    `(?s).*PATTERN` captures the LAST occurrence>}.  None when the pair has none."""
    spec = pair.get("statement_after")
    if not isinstance(spec, dict):
        return None
    try:
        with open(os.path.join(clone_path, spec["path"]), encoding="utf-8") as fh:
            text = fh.read()
    except (OSError, KeyError):
        return ("", False)
    m = re.search(spec.get("parse", ""), text, re.S)
    if not m:
        return ("", False)
    return (norm(m.group(1) if m.groups() else m.group(0)), True)


def evaluate_pairs(pairs, base_clone, lands_clone):
    """One observation pass per pair per revision; legs consume this."""
    ev = []
    for pair in pairs:
        tok, ok = stated_token(pair)
        ev.append({
            "stated": tok,
            "stated_ok": ok,
            "base": observed_token(pair, base_clone["path"]),
            "lands": observed_token(pair, lands_clone["path"]),
            "stmt_after": statement_after(pair, lands_clone["path"]),
        })
    return ev


def leg_basemismatch(out, pairs, ev, min_pairs):
    mismatched, unobservable, misses = [], [], []
    for idx, pair in enumerate(pairs):
        tok = ev[idx]["stated"]
        obs, parsed, why = ev[idx]["base"]
        pid = pair.get("id")
        if obs is None:
            unobservable.append("%s:%s" % (pid, why))
            continue
        if not parsed:
            misses.append(pid)
        if tok is None or norm(tok) != norm(obs):
            mismatched.append(pid)
    passed = (not unobservable) and len(mismatched) >= min_pairs
    detail = "found=%d min=%d ids=%s" % (len(mismatched), min_pairs, mismatched)
    if misses:
        detail += " parse-miss=%s" % misses
    if unobservable:
        detail += " unobservable=%s" % unobservable
    return leg(out, "BASEMISMATCH", passed, detail)


def leg_repair(out, pairs, ev):
    red, unobservable, green = [], [], []
    for idx, pair in enumerate(pairs):
        if pair.get("disposition") != "REPAIR":
            continue
        obs, parsed, why = ev[idx]["lands"]
        pid = pair.get("id")
        if obs is None:
            unobservable.append("%s:%s" % (pid, why))
            continue
        sa = ev[idx].get("stmt_after")
        if sa is not None:
            tok, found = sa
            if found and tok == norm(obs) and tok != ev[idx]["stated"]:
                green.append(pid)
            else:
                red.append("%s(statement-after=%r truth=%r stated-at-base=%r)"
                           % (pid, tok[:40], obs[:40], (ev[idx]["stated"] or "")[:40]))
            continue
        if norm(obs) == norm(pair.get("expected_after")):
            green.append(pid)
        else:
            red.append("%s(observed=%r expected=%r)"
                       % (pid, obs[:40], pair["expected_after"][:40]))
    detail = "green=%s red=%s" % (green, red)
    if unobservable:
        detail += " unobservable=%s" % unobservable
    return leg(out, "REPAIR", not red and not unobservable, detail)


def correction_rows(scor):
    body = section_of(scor, CORR_HEADING_RE)
    if not body:
        return None
    rows = []
    for line in body.splitlines()[1:]:
        s = line.strip()
        if not s:
            continue
        if re.match(r"^\|[\s:|-]+\|$", s):
            continue
        rows.append(s)
    return rows


def row_names_id(row, pid):
    return re.search(r"(?<![A-Za-z0-9_-])%s(?![A-Za-z0-9_-])" % re.escape(pid),
                     row) is not None


def leg_annotate(out, pairs, ev, texts):
    annotate = [(i, p) for i, p in enumerate(pairs)
                if p.get("disposition") == "ANNOTATE"]
    if not annotate:
        return leg(out, "ANNOTATE", True, "annotate-pairs=0 (vacuous)")
    scor = texts.get(SCORECARD_REL)
    if scor is None:
        return leg(out, "ANNOTATE", False, "SCORECARD.md unreadable at lands")
    rows = correction_rows(scor)
    if rows is None:
        return leg(out, "ANNOTATE", False,
                   "no '## Corrections — round 73' section; annotate-pairs=%d"
                   % len(annotate))
    unannotated = []
    for idx, pair in annotate:
        tok = ev[idx]["stated"]
        obs, parsed, why = ev[idx]["lands"]
        if obs is None or tok is None:
            unannotated.append("%s(unobservable:%s)" % (pair.get("id"), why))
            continue
        want = (norm(tok), norm(obs))
        hit = [r for r in rows
               if row_names_id(r, pair.get("id"))
               and want[0] in norm(r) and want[1] in norm(r)]
        if not hit:
            unannotated.append("%s(stated=%r observed=%r)"
                               % (pair.get("id"), want[0][:40], want[1][:40]))
    return leg(out, "ANNOTATE", not unannotated,
               "rows=%d annotate-pairs=%d unannotated=%d %s"
               % (len(rows), len(annotate), len(unannotated), unannotated))


def leg_nostub(out, pairs, ev, texts):
    annotate = [(i, p) for i, p in enumerate(pairs)
                if p.get("disposition") == "ANNOTATE"]
    if not annotate:
        return leg(out, "NOSTUB", True, "annotate-pairs=0 (vacuous)")
    scor = texts.get(SCORECARD_REL) or ""
    rows = correction_rows(scor) or []
    stubs = []
    for idx, pair in annotate:
        tok = ev[idx]["stated"]
        obs, parsed, why = ev[idx]["lands"]
        cmd = rederive_text(pair)
        mine = [r for r in rows if row_names_id(r, pair.get("id"))]
        if not mine:
            stubs.append("%s:no-row" % pair.get("id"))
            continue
        good = False
        reasons = []
        for row in mine:
            nr = norm(row)
            lacks = []
            if tok is None or norm(tok) not in nr:
                lacks.append("stated-token")
            if obs is None or norm(obs) not in nr:
                lacks.append("observed-token")
            if cmd not in nr:
                lacks.append("rederive-cmd")
            if lacks:
                reasons.append(",".join(lacks))
            else:
                good = True
                break
        if not good:
            stubs.append("%s:%s" % (pair.get("id"),
                                    reasons[0] if reasons else "?"))
        for tokval in (tok, obs):
            if tokval is not None and norm(tokval).casefold() in STUB_TOKENS:
                stubs.append("%s:placeholder-token(%r)"
                             % (pair.get("id"), tokval))
    return leg(out, "NOSTUB", not stubs,
               "minimum-shape=id+stated+observed+rederive stubs=%s" % stubs)


def leg_appendonly(out, root, base, lands, fleet_root, meta):
    removed, ns = numstat_removed(root, base, lands, APPENDONLY_FILES)
    problems = []
    if removed:
        problems.append("lane-removed=%d %s" % (removed, ns.strip()[:160]))
    pin = meta.get("fleet_pin")
    fleet_detail = "fleet-pin=%s" % (pin[:12] if isinstance(pin, str) else pin)
    if not isinstance(pin, str) or not re.fullmatch(r"[0-9a-f]{40}", pin):
        problems.append("no fleet_pin in the ledger (40hex fleet commit)")
    else:
        blob_pin = show(fleet_root, pin, FLEET_R72_REPORT)
        blob_now = show(fleet_root, "HEAD", FLEET_R72_REPORT)
        if blob_pin is None:
            problems.append("fleet report absent at fleet_pin")
        elif blob_now is None:
            problems.append("fleet report absent at fleet HEAD")
        else:
            if sha256_bytes(blob_pin) != sha256_bytes(blob_now):
                problems.append("fleet report bytes differ since fleet_pin")
            f_removed, f_ns = numstat_removed(fleet_root, pin, "HEAD",
                                              (FLEET_R72_REPORT,))
            if f_removed:
                problems.append("fleet-removed=%d %s"
                                % (f_removed, f_ns.strip()[:120]))
            fleet_detail += " blob=%s" % sha256_bytes(blob_now)[:12]
    names = git(root, "diff", "--name-only", "%s..%s" % (base, lands),
                "--", *INPLACE_PATHS).stdout.split()
    listed = set()
    for pair in meta.get("pairs", []):
        m = re.match(r"^(.+):(\d+)$", pair.get("stated_at") or "")
        if m:
            listed.add(m.group(1))
    inplace_detail = []
    for path in names:
        base_text = show(root, base, path)
        lands_text = show(root, lands, path)
        if base_text is None or lands_text is None:
            problems.append("%s added/removed in place" % path)
            continue
        if path == "SKILL.md":
            span_base = section_range(base_text, REGISTRY_HEADING_RE)
            span_lands = section_range(lands_text, REGISTRY_HEADING_RE)
            where = "registry"
        else:
            span_base = footer_range(base_text)
            span_lands = footer_range(lands_text)
            where = "footer"
        hunks = changed_hunks(root, base, lands, path)
        bad = []
        for old_start, old_count, new_start, new_count in hunks:
            appended = 1 if new_count else 0
            if in_span(new_start, span_lands, appended) \
                    or in_span(old_start, span_base):
                continue
            bad.append("@@-%d,+%d" % (old_start, new_start))
        if bad:
            problems.append("%s hunk(s) outside %s: %s" % (path, where, bad))
        if path not in listed:
            problems.append("%s changed in place but no ledger pair names it"
                            % path)
        inplace_detail.append("%s(%s)" % (path, where))
    detail = "lane-removed=%d %s in-place=%s" % (removed, fleet_detail,
                                                 inplace_detail or "none")
    if problems:
        detail += " problems=%s" % problems
    return leg(out, "APPENDONLY", not problems, detail)


def leg_separable(out, root, base, lands, meta, texts, lands_clone, lraw):
    problems = []
    scan = []
    ledger_text = lraw if lraw else texts.get(LEDGER_REL)
    if ledger_text:
        scan.append(("ledger", ledger_text))
    for pair in meta.get("pairs", []):
        for key in ("observe_cmd", "expected_after", "parse", "rederive",
                    "stated_token", "stated_parse"):
            val = pair.get(key)
            pieces = val if isinstance(val, list) else [val]
            for piece in pieces:
                if isinstance(piece, str):
                    for cpath in C_PATHS:
                        if cpath in piece:
                            problems.append("%s: %s names %s"
                                            % (pair.get("id"), key, cpath))
    scor = texts.get(SCORECARD_REL) or ""
    rows = correction_rows(scor) or []
    ids = [p.get("id") for p in meta.get("pairs", []) if p.get("id")]
    ca_rows = [r for r in rows if any(row_names_id(r, i) for i in ids)]
    if ca_rows:
        scan.append(("corrections-rows", "\n".join(ca_rows)))
    tele = git(lands_clone["path"], "ls-files", CA_TELEMETRY_DIR).stdout.split()
    for path in tele:
        if "ca" not in os.path.basename(path):
            continue
        body = texts.get(path)
        if body is None:
            body = show(lands_clone["path"], lands, path) or ""
        scan.append((path, body))
    for label, body in scan:
        for m in SID_RE.finditer(body):
            if int(m.group(1)) >= SEPARABLE_MIN_ID:
                problems.append("%s cites S%s" % (label, m.group(1)))
        for cpath in C_PATHS:
            if cpath in body:
                problems.append("%s names %s" % (label, cpath))
    added = added_lines(root, base, lands, ("SKILL.md", "corpus/README.md",
                                            "README.md"))
    for line in added:
        for m in SID_RE.finditer(line):
            if int(m.group(1)) >= SEPARABLE_MIN_ID:
                problems.append("in-place added line cites S%s" % m.group(1))
    uniq = sorted(set(problems))
    return leg(out, "SEPARABLE", not uniq,
               "scanned=%s problems=%s" % ([s[0] for s in scan], uniq[:6]))


def leg_tracked(out, root, base, lands, meta):
    """TRACKED (defect R1): every path in the ledger's `must_track` list is absent
    from the base tree and present, non-empty, in the tree at <lands> — the landing
    defect class (seat reports written but never committed).  Reads git trees only."""
    paths = meta.get("must_track")
    if not isinstance(paths, list) or not paths:
        return leg(out, "TRACKED", False, "ledger declares no must_track list")
    bad = []
    for path in paths:
        if git(root, "cat-file", "-e", "%s:%s" % (base, path)).returncode == 0:
            bad.append("%s already tracked at base (not a landing defect)" % path)
        r = git(root, "cat-file", "-s", "%s:%s" % (lands, path))
        if r.returncode != 0 or not r.stdout.strip().isdigit() or int(r.stdout.strip()) == 0:
            bad.append("%s absent or empty at lands" % path)
    return leg(out, "TRACKED", not bad, "paths=%d problems=%s" % (len(paths), bad))


def leg_stamp(out, header, root, lands, clone):
    problems = []
    for key in ("stamped", "evaluated", "measured", "tree", "sha"):
        if not header.get(key):
            problems.append("missing %s" % key)
    if header.get("stamped") != lands:
        problems.append("stamped != lands")
    if header.get("evaluated") != lands:
        problems.append("evaluated != lands")
    if header.get("measured") != lands:
        problems.append("measured %s != lands %s"
                        % (header.get("measured"), lands))
    real_tree = git(root, "rev-parse", "%s^{tree}" % lands).stdout.strip()
    if header.get("tree") != real_tree:
        problems.append("tree %s != rev-parse lands^{tree} %s"
                        % (header.get("tree"), real_tree))
    if header.get("sha") != sha256_file(__file__):
        problems.append("counter sha256 does not match this file")
    if clone["head"] != lands:
        problems.append("clone HEAD %s != lands" % clone["head"])
    if clone["tree"] != real_tree:
        problems.append("clone tree %s != lands tree" % clone["tree"])
    if RUN_STATE["outside_clone"]:
        problems.append("an observe_cmd ran outside the clone")
    detail = ("stamped=evaluated=measured=%s tree=%s counter=%s clone=%s"
              % (lands[:12], (header.get("tree") or "")[:12],
                 (header.get("sha") or "")[:12], clone["path"]))
    if problems:
        detail += " problems=%s" % problems
    return leg(out, "STAMP", not problems, detail)


# --------------------------------------------------------------------------
# driver
# --------------------------------------------------------------------------
def main_check(root, lands, fleet_root, base=BASE, ledger_path=LEDGER_REL,
               min_pairs=MIN_PAIRS, main_branch="main"):
    root = os.path.abspath(root)
    fleet_root = os.path.abspath(fleet_root)
    RUN_STATE["outside_clone"] = False
    out = []

    if git(root, "cat-file", "-e", "%s^{commit}" % lands).returncode != 0:
        print("ERROR: --lands %s is not a commit in %s" % (lands, root),
              file=sys.stderr)
        return 2
    if base != lands and \
            git(root, "cat-file", "-e", "%s^{commit}" % base).returncode != 0:
        print("ERROR: base %s is not a commit in %s" % (base, root),
              file=sys.stderr)
        return 2

    tmpdir = tempfile.mkdtemp(prefix="r73-ca-")
    try:
        clone = materialize(root, lands, tmpdir, "lands")
        if clone is None:
            return 2
        base_clone = clone if base == lands \
            else materialize(root, base, tmpdir, "base")
        if base_clone is None:
            return 2

        tree = git(root, "rev-parse", "%s^{tree}" % lands).stdout.strip()
        measured = git(root, "rev-parse", "--verify", "--quiet",
                       "%s^{commit}" % main_branch).stdout.strip()
        measured_note = ""
        if not measured:
            measured = git(root, "rev-parse", "HEAD").stdout.strip()
            measured_note = " (fallback HEAD: %s unresolved)" % main_branch
        header = {"stamped": lands, "evaluated": clone["head"],
                  "measured": measured, "tree": tree,
                  "sha": sha256_file(__file__)}
        print("# counter sha256 (self): %s" % header["sha"])
        print("# stamped revision: %s" % header["stamped"])
        print("# evaluated revision: %s" % header["evaluated"])
        print("# measured revision (lane main): %s" % header["measured"])
        print("# tree: %s" % header["tree"])
        print("# claim: Ca  round: 73  base: %s%s" % (base, measured_note))
        print("# counter: %s" % os.path.relpath(os.path.abspath(__file__),
                                                os.getcwd()))
        print("# min-pairs: %d" % min_pairs)
        print("# clone: %s head=%s" % (clone["path"], clone["head"]))
        print("# base-clone: %s head=%s"
              % ("reused" if base_clone is clone else base_clone["path"],
                 base_clone["head"]))

        obj, source, lsha, lraw, err = load_ledger(root, clone, lands,
                                                   ledger_path)
        print("# ledger: %s source=%s sha256=%s"
              % (ledger_path, source, lsha or "none"))
        if source == "worktree-uncommitted":
            note("ledger read from the moving worktree (not committed at lands)")

        pairs, meta = [], {}
        if isinstance(obj, list):
            pairs = [p for p in obj if isinstance(p, dict)]
            meta = {"pairs": pairs}
        elif isinstance(obj, dict):
            pairs = [p for p in obj.get("pairs", []) if isinstance(p, dict)]
            meta = dict(obj)
            meta["pairs"] = pairs

        # cache the lands bytes the legs read
        texts = {}
        texts_base = {}
        for pair in pairs:
            m = re.match(r"^(.+):(\d+)$", pair.get("stated_at") or "")
            if m and m.group(1) not in texts:
                texts[m.group(1)] = show(root, lands, m.group(1))
            if m and m.group(1) not in texts_base:
                texts_base[m.group(1)] = show(root, base, m.group(1))
        for path in (SCORECARD_REL, LEDGER_REL):
            if path not in texts:
                texts[path] = show(root, lands, path)

        if err:
            leg(out, "LEDGER", False, err)
        else:
            leg_ledger(out, pairs, meta, base, min_pairs, texts_base)

        if not pairs:
            for name in ("BASEMISMATCH", "REPAIR", "ANNOTATE", "NOSTUB"):
                leg(out, name, False, "no pairs")
        else:
            ev = evaluate_pairs(pairs, base_clone, clone)
            for idx, pair in enumerate(pairs):
                tok = ev[idx]["stated"]
                ob, parsed, why = ev[idx]["base"]
                ol, parsed_l, why_l = ev[idx]["lands"]
                print("PAIR %s disposition=%s stated_at=%s stated=%r "
                      "observed_base=%r observed_lands=%r expected_after=%r"
                      % (pair.get("id"), pair.get("disposition"),
                         pair.get("stated_at"), (tok or "")[:60],
                         (ob if ob is not None else "<%s>" % why)[:60],
                         (ol if ol is not None else "<%s>" % why_l)[:60],
                         pair.get("expected_after", "")[:40]))
                if not parsed or not parsed_l:
                    note("%s parse-miss (raw stdout token used)" % pair.get("id"))
            leg_basemismatch(out, pairs, ev, min_pairs)
            leg_repair(out, pairs, ev)
            leg_annotate(out, pairs, ev, texts)
            leg_nostub(out, pairs, ev, texts)

        leg_appendonly(out, root, base, lands, fleet_root, meta)
        leg_separable(out, root, base, lands, meta, texts, clone, lraw)
        leg_tracked(out, root, base, lands, meta)
        leg_stamp(out, header, root, lands, clone)
    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)

    passed = sum(1 for _, ok, _ in out if ok)
    total = len(out)
    ok = passed == total and total == 9
    print("ACCEPT-CA-73: %s legs=%d/%d" % ("PASS" if ok else "FAIL", passed, total))
    return 0 if ok else 1


# --------------------------------------------------------------------------
# selftest
# --------------------------------------------------------------------------
SELFTEST_ENV = {
    "GIT_CONFIG_GLOBAL": "/dev/null",
    "GIT_CONFIG_NOSYSTEM": "1",
    "GIT_AUTHOR_NAME": "ca-selftest",
    "GIT_AUTHOR_EMAIL": "ca-selftest@example.invalid",
    "GIT_COMMITTER_NAME": "ca-selftest",
    "GIT_COMMITTER_EMAIL": "ca-selftest@example.invalid",
}


def _g(root, *args):
    env = dict(os.environ)
    env.update(SELFTEST_ENV)
    return subprocess.run(["git", "-C", root, *args], capture_output=True,
                          text=True, env=env)


def _write(root, rel, text):
    path = os.path.join(root, rel)
    os.makedirs(os.path.dirname(path) or root, exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)


def _commit(root, msg):
    _g(root, "add", "-A")
    r = _g(root, "commit", "-q", "-m", msg)
    if r.returncode != 0:
        raise RuntimeError("fixture commit failed: %s" % r.stderr)
    return _g(root, "rev-parse", "HEAD").stdout.strip()


SELFTEST_LEDGER_PAIRS = [
    {
        "id": "P1",
        "stated_at": "SCORECARD.md:5",
        "stated_text": "| calibration | ACCEPT-CA-72 PASS legs=12/12 |",
        "stated_token": "ACCEPT-CA-72 PASS legs=12/12",
        "observe_cmd": ["grep", "-ho", "ACCEPT-CA-72: [A-Z]*",
                        "reports/round-72/telemetry/measures-ca.txt",
                        "reports/round-73/telemetry/measures-ca.txt"],
        "parse": "ACCEPT-CA-72: (PASS)",
        "expected_after": "PASS",
        "disposition": "REPAIR",
        "rederive": "grep -ho 'ACCEPT-CA-72: [A-Z]*' reports/round-72/telemetry/measures-ca.txt reports/round-73/telemetry/measures-ca.txt",
    },
    {
        "id": "P2",
        "stated_at": "corpus/README.md:7",
        "stated_text": "Total knowledge entries: 1.",
        "stated_token": "entries: 1",
        "observe_cmd": ["python3", "-c",
                        "import pathlib;print(sum(1 for p in pathlib.Path('corpus/knowledge').rglob('*.md')))"],
        "parse": r"^(\d+)$",
        "expected_after": "2",
        "disposition": "ANNOTATE",
        "rederive": "find corpus/knowledge -type f -name '*.md' | wc -l",
    },
]

SELFTEST_CORRECTIONS = (
    "\n## Corrections — round 73\n\n"
    "- P2 — stated `entries: 1`, observed `2`; re-derive: "
    "`find corpus/knowledge -type f -name '*.md' | wc -l`\n"
)

SELFTEST_STUB = "\n## Corrections — round 73\n\n- P2 — corrected.\n"


def _selftest_repo(td):
    lane = os.path.join(td, "lane")
    fleet = os.path.join(td, "fleet")
    os.makedirs(lane)
    os.makedirs(fleet)
    _g(lane, "init", "-q")
    _g(fleet, "init", "-q")

    _write(lane, "SCORECARD.md",
           "# SCORECARD\n\n| axis | verdict |\n|---|---|\n"
           "| calibration | ACCEPT-CA-72 PASS legs=12/12 |\n"
           "| coverage | registry rows: accept-ca-70..72 = 0 |\n")
    _write(lane, "LOG.md", "# LOG\n\n## Round 72\n\n- round-72 entry\n")
    _write(lane, "corpus/lessons/round-72.md", "# Round 72\n\n- lesson\n")
    _write(lane, "corpus/lessons/round-71.md", "# Round 71\n\n- lesson\n")
    _write(lane, "corpus/README.md",
           "# corpus index\n\n## linguistics/ (2)\n\n## Known gaps\n\n"
           "Total knowledge entries: 1.\n")
    _write(lane, "corpus/knowledge/linguistics/a.md", "# a\n")
    _write(lane, "corpus/knowledge/linguistics/b.md", "# b\n")
    _write(lane, "SKILL.md",
           "# SKILL\n\n## Gates and probes\n\n| name |\n|---|\n| accept-c-69 |\n\n"
           "## Boundaries\n\n- hard\n")
    _write(lane, "reports/round-72/telemetry/measures-ca.txt",
           "# counter sha256 (self): 0\nLEG FAIL REPORTCORR\n"
           "ACCEPT-CA-72: FAIL legs=12/12\n")
    base = _commit(lane, "base")

    ledger = {"round": 73, "claim": "Ca", "base": base, "fleet_pin": None,
              "must_track": ["reports/round-73/telemetry/measures-ca.txt"],
              "pairs": SELFTEST_LEDGER_PAIRS}
    _write(lane, LEDGER_REL, json.dumps(ledger, indent=1) + "\n")
    ledger_commit = _commit(lane, "ledger")

    _write(fleet, FLEET_R72_REPORT, "# round-72 fleet report\n")
    fleet_pin = _commit(fleet, "fleet r72 report")
    ledger["fleet_pin"] = fleet_pin
    _write(lane, LEDGER_REL, json.dumps(ledger, indent=1) + "\n")
    ledger_commit = _commit(lane, "ledger with fleet pin")
    return lane, fleet, base, ledger_commit, fleet_pin


def _run_check(root, lands, fleet, base, ledger_path, min_pairs, main_branch):
    buf = io.StringIO()
    with redirect_stdout(buf):
        code = main_check(root, lands, fleet, base=base, ledger_path=ledger_path,
                          min_pairs=min_pairs, main_branch=main_branch)
    text = buf.getvalue()
    states = {}
    for line in text.splitlines():
        m = re.match(r"^LEG (PASS|FAIL) (\S+)$", line)
        if m:
            states[m.group(2)] = m.group(1)
    return code, states, text


def selftest():
    failures = []

    def expect(label, got, want):
        if got != want:
            failures.append("%s: got %r want %r" % (label, got, want))

    td = tempfile.mkdtemp(prefix="r73-ca-selftest-")
    try:
        lane, fleet, base, ledger_commit, fleet_pin = _selftest_repo(td)
        branch = _g(lane, "symbolic-ref", "--short", "HEAD").stdout.strip()

        # ---- 1. do-nothing control: the ledger commit, no data ----
        code, states, text = _run_check(lane, ledger_commit, fleet, base,
                                        LEDGER_REL, 2, branch)
        print("selftest: do-nothing control (lands=ledger commit)")
        for line in text.splitlines():
            print("  %s" % line)
        expect("do-nothing exit", code, 1)
        expect("do-nothing LEDGER", states.get("LEDGER"), "PASS")
        expect("do-nothing BASEMISMATCH", states.get("BASEMISMATCH"), "PASS")
        expect("do-nothing REPAIR", states.get("REPAIR"), "FAIL")
        expect("do-nothing ANNOTATE", states.get("ANNOTATE"), "FAIL")
        expect("do-nothing NOSTUB", states.get("NOSTUB"), "FAIL")
        expect("do-nothing APPENDONLY", states.get("APPENDONLY"), "PASS")
        expect("do-nothing SEPARABLE", states.get("SEPARABLE"), "PASS")
        expect("do-nothing STAMP", states.get("STAMP"), "PASS")
        if "found=2" not in text:
            failures.append("do-nothing BASEMISMATCH did not report found=2")

        # ---- 2. clean landing: receipt + correction row ----
        _write(lane, "reports/round-73/telemetry/measures-ca.txt",
               "ACCEPT-CA-72: PASS legs=12/12\n")
        with open(os.path.join(lane, "SCORECARD.md"), "a",
                  encoding="utf-8") as fh:
            fh.write(SELFTEST_CORRECTIONS)
        clean = _commit(lane, "clean landing")
        code, states, text = _run_check(lane, clean, fleet, base, LEDGER_REL,
                                        2, branch)
        print("selftest: clean landing")
        for line in text.splitlines():
            print("  %s" % line)
        expect("clean exit", code, 0)
        for name in ("LEDGER", "BASEMISMATCH", "REPAIR", "ANNOTATE",
                     "APPENDONLY", "NOSTUB", "SEPARABLE", "STAMP"):
            expect("clean %s" % name, states.get(name), "PASS")

        # ---- 3. stub-row control: correction row naming only the id ----
        _g(lane, "checkout", "-q", "-B", "stub", ledger_commit)
        _write(lane, "reports/round-73/telemetry/measures-ca.txt",
               "ACCEPT-CA-72: PASS legs=12/12\n")
        with open(os.path.join(lane, "SCORECARD.md"), "a",
                  encoding="utf-8") as fh:
            fh.write(SELFTEST_STUB)
        stub = _commit(lane, "stub row")
        code, states, text = _run_check(lane, stub, fleet, base, LEDGER_REL,
                                        2, "stub")
        print("selftest: stub-row control")
        for line in text.splitlines():
            print("  %s" % line)
        expect("stub exit", code, 1)
        expect("stub STAMP", states.get("STAMP"), "PASS")
        expect("stub REPAIR", states.get("REPAIR"), "PASS")
        expect("stub ANNOTATE", states.get("ANNOTATE"), "FAIL")
        expect("stub NOSTUB", states.get("NOSTUB"), "FAIL")

        # ---- 4. in-place removal in an append-only file ----
        _g(lane, "checkout", "-q", "-B", "inplace", ledger_commit)
        _write(lane, "reports/round-73/telemetry/measures-ca.txt",
               "ACCEPT-CA-72: PASS legs=12/12\n")
        with open(os.path.join(lane, "SCORECARD.md"), "a",
                  encoding="utf-8") as fh:
            fh.write(SELFTEST_CORRECTIONS)
        _write(lane, "LOG.md", "# LOG\n\n## Round 72\n")
        bad = _commit(lane, "log line removed")
        code, states, text = _run_check(lane, bad, fleet, base, LEDGER_REL,
                                        2, "inplace")
        print("selftest: append-only removal")
        for line in text.splitlines():
            print("  %s" % line)
        expect("removal exit", code, 1)
        expect("removal STAMP", states.get("STAMP"), "PASS")
        expect("removal APPENDONLY", states.get("APPENDONLY"), "FAIL")

        # ---- 5. in-place edit outside the registry/footer span ----
        _g(lane, "checkout", "-q", "-B", "outspan", ledger_commit)
        _write(lane, "reports/round-73/telemetry/measures-ca.txt",
               "ACCEPT-CA-72: PASS legs=12/12\n")
        with open(os.path.join(lane, "SCORECARD.md"), "a",
                  encoding="utf-8") as fh:
            fh.write(SELFTEST_CORRECTIONS)
        _write(lane, "corpus/README.md",
               "# corpus INDEX\n\n## linguistics/ (2)\n\n## Known gaps\n\n"
               "Total knowledge entries: 1.\n")
        outspan = _commit(lane, "readme head rewritten")
        code, states, text = _run_check(lane, outspan, fleet, base, LEDGER_REL,
                                        2, "outspan")
        print("selftest: in-place edit outside the footer")
        for line in text.splitlines():
            print("  %s" % line)
        expect("outspan exit", code, 1)
        expect("outspan STAMP", states.get("STAMP"), "PASS")
        expect("outspan APPENDONLY", states.get("APPENDONLY"), "FAIL")

        # ---- 6. shell-string observe_cmd is a LEDGER failure ----
        shell_ledger = {"round": 73, "claim": "Ca", "base": base,
                        "fleet_pin": fleet_pin,
                        "pairs": [dict(SELFTEST_LEDGER_PAIRS[0],
                                       observe_cmd="grep -h PASS receipt.txt"),
                                  SELFTEST_LEDGER_PAIRS[1]]}
        shell_path = os.path.join(lane, "shell-ledger.json")
        with open(shell_path, "w", encoding="utf-8") as fh:
            fh.write(json.dumps(shell_ledger, indent=1) + "\n")
        code, states, text = _run_check(lane, clean, fleet, base,
                                        shell_path, 2, branch)
        print("selftest: shell-string observe_cmd")
        for line in text.splitlines():
            print("  %s" % line)
        expect("shell exit", code, 1)
        expect("shell LEDGER", states.get("LEDGER"), "FAIL")
        os.unlink(shell_path)

        # ---- 7. min-pairs gate: the same clean landing under the default 8 ----
        code, states, text = _run_check(lane, clean, fleet, base, LEDGER_REL,
                                        8, branch)
        expect("min-pairs exit", code, 1)
        expect("min-pairs LEDGER", states.get("LEDGER"), "FAIL")
        expect("min-pairs BASEMISMATCH", states.get("BASEMISMATCH"), "FAIL")

        # ---- 9. authorized in-place registry append (positive control) ----
        _g(lane, "checkout", "-q", "-B", "registry", ledger_commit)
        _write(lane, "reports/round-73/telemetry/measures-ca.txt",
               "ACCEPT-CA-72: PASS legs=12/12\n")
        with open(os.path.join(lane, "SCORECARD.md"), "a",
                  encoding="utf-8") as fh:
            fh.write(SELFTEST_CORRECTIONS)
        with open(os.path.join(lane, "SKILL.md"), encoding="utf-8") as fh:
            skill = fh.read()
        skill = skill.replace(
            "| accept-c-69 |\n",
            "| accept-c-69 |\n| accept-ca-73 | gate | "
            "`python3 -B reports/round-73/accept-ca.py --root . --lands <lands>` | "
            "0 pass / 1 fail / 2 usage-env. | `--selftest` | - | read-only | "
            "kotodama-shokunin |\n")
        _write(lane, "SKILL.md", skill)
        registry = _commit(lane, "registry append")
        p3 = {
            "id": "P3",
            "stated_at": "SKILL.md:7",
            "stated_text": "| accept-c-69 |",
            "stated_token": "accept-c-69",
            "observe_cmd": ["grep", "-c", "accept-ca-7", "SKILL.md"],
            "parse": r"^(\d+)$",
            "expected_after": "1",
            "disposition": "REPAIR",
            "rederive": "grep -c accept-ca-7 SKILL.md",
        }
        reg_ledger = {"round": 73, "claim": "Ca", "base": base,
                      "fleet_pin": fleet_pin,
                      "must_track": ["reports/round-73/telemetry/measures-ca.txt"],
                      "pairs": SELFTEST_LEDGER_PAIRS + [p3]}
        reg_path = os.path.join(lane, "registry-ledger.json")
        with open(reg_path, "w", encoding="utf-8") as fh:
            fh.write(json.dumps(reg_ledger, indent=1) + "\n")
        code, states, text = _run_check(lane, registry, fleet, base, reg_path,
                                        3, "registry")
        print("selftest: authorized in-place registry append")
        for line in text.splitlines():
            print("  %s" % line)
        expect("registry exit", code, 0)
        for name in ("LEDGER", "BASEMISMATCH", "REPAIR", "ANNOTATE",
                     "APPENDONLY", "NOSTUB", "SEPARABLE", "TRACKED", "STAMP"):
            expect("registry %s" % name, states.get(name), "PASS")
        if "in-place=['SKILL.md(registry)']" not in text:
            failures.append("registry append not recognized as an authorized "
                            "in-place registry edit")
        os.unlink(reg_path)

        # ---- 8. CLI input errors ----
        expect("bad lands exit", main(["--root", lane, "--lands", "nothex",
                                       "--fleet-root", fleet]), 2)
        buf = io.StringIO()
        with redirect_stdout(buf):
            missing = main_check(lane, clean, fleet, base=base,
                                 ledger_path="reports/round-73/nope.json",
                                 min_pairs=2, main_branch=branch)
        expect("missing ledger exit", missing, 1)
        if "LEG FAIL LEDGER" not in buf.getvalue():
            failures.append("missing ledger did not fail the LEDGER leg")
        expect("frozen base absent exit",
               main(["--root", lane, "--lands", clean,
                     "--fleet-root", fleet]), 2)
    finally:
        shutil.rmtree(td, ignore_errors=True)

    if failures:
        for failure in failures:
            print("SELFTEST FAIL: %s" % failure)
        return 1
    print("SELFTEST OK: 9 scenarios — do-nothing control (BASEMISMATCH "
          "found=2, REPAIR/ANNOTATE/NOSTUB FAIL), clean landing 9/9, stub-row "
          "control (ANNOTATE+NOSTUB FAIL), append-only removal FAIL, "
          "in-place-outside-footer FAIL, shell-string argv FAIL, min-pairs "
          "gate FAIL, authorized SKILL.md registry append 9/9, CLI exit 2 on a bad --lands")
    return 0


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------
def main(argv=None):
    ap = argparse.ArgumentParser(
        description="round-73 calibration counter (claim Ca, ledger-driven)")
    ap.add_argument("--root", default=".")
    ap.add_argument("--lands")
    ap.add_argument("--fleet-root")
    ap.add_argument("--ledger", default=LEDGER_REL)
    ap.add_argument("--min-pairs", type=int, default=MIN_PAIRS)
    ap.add_argument("--main", default="main")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args(argv)
    if args.selftest:
        return selftest()
    if not args.lands or not args.fleet_root:
        print("ERROR: --lands <40hex> and --fleet-root are required",
              file=sys.stderr)
        return 2
    lands = args.lands.lower()
    if not re.fullmatch(r"[0-9a-f]{40}", lands):
        print("ERROR: --lands must be 40 hex", file=sys.stderr)
        return 2
    if args.min_pairs < 1:
        print("ERROR: --min-pairs must be >= 1", file=sys.stderr)
        return 2
    if not os.path.isdir(args.fleet_root):
        print("ERROR: --fleet-root %s is not a directory" % args.fleet_root,
              file=sys.stderr)
        return 2
    return main_check(args.root, lands, args.fleet_root, base=BASE,
                      ledger_path=args.ledger, min_pairs=args.min_pairs,
                      main_branch=args.main)


if __name__ == "__main__":
    sys.exit(main())
