#!/usr/bin/env python3
r"""accept-o.py — round-79 claim O acceptance counter (ledger-token guard).

Claim O (operability): the lane acquires a bounded ledger-token guard
(tools/ledger-token-guard.py) for its calibration records.  The guard re-runs
approved read-only observations against immutable committed bytes, refuses
mutable revisions and constant printers, rejects a recorded observed_at_base
that differs from the actual observation, and rejects a stated_token equal to
the actual observation (a vacuous pair).  Grounded in the round-77 probe
evidence (`.ufo/waves/round-77/w2/ScoutLogPairs.md`): the real-base probe
ledger recorded observed_at_base "1" where the observation actually parsed
"149" (ten fabricated recorded observations), and pair D11 was green at base
(stated == observed) — both classes passed the round-77 structural checker.

The counter grades the claim at <lands> with every constant read from
`git show <freeze>:...`.  It never reads the graded tree as a worktree.

Legs (the frozen claims.json legs[] must equal this table, order included —
LEGCOUNT refusal otherwise):

  FROZENCFG  <freeze> is on the <lands> first-parent chain (<lands> ==
             <freeze> is graded, never passed, as the do-nothing control);
             the frozen base is an ancestor of <freeze>; the guard, the
             fixture files and claims.json are byte-identical between
             <freeze> and <lands>.
  GREEN      the committed green fixture is truthful (the counter re-derives
             every stated and observed token from committed fixture bytes via
             git blob operations, never from guard output) and the guard
             extracted from <lands> bytes grades it PASS with exit 0, a
             per-pair --emit agreeing with the counter's re-derivation.
  REDOBS     the committed mut-observed fixture really falsifies a recorded
             observation (counter re-derived) and the guard rejects it
             exit 1 with an OBS_MISMATCH label naming the pair.
  REDSTATED  the committed mut-stated fixture really has stated == observed
             (counter re-derived) and the guard rejects it exit 1 with a
             NOT_RED label naming the pair.
  REDGRAM    the committed grammar fixtures really carry a constant printer
             or a mutable revision (counter-verified from committed bytes)
             and the guard refuses them exit 2.
  SELFTEST   the committed guard-selftest receipt at <lands> names the
             <lands> guard blob sha256 and the guard's live --selftest re-run
             (from <lands> bytes, in explicit scratch) exits 0 and reproduces
             the receipt's SELFTEST line.
  RECEIPTS   the junk and control receipts shipped at <freeze> are committed
             unchanged at <lands> and carry the expected per-fixture verdict
             lines (failures named, never prose-trusted); the counter's own
             committed selftest receipt names a green clean scenario; LOG.md
             carries the round-79 claim-O lands row.
  STAMP      this run's receipt headers carry stamped == evaluated ==
             measured == <lands>, the lands tree and this counter's sha256.

Review-only clauses (QUALITY 11, named not graded): the guard's documented
output/timeout caps are not exercised by a fixture; the guard's schema
documentation is read by reviewers; "no arbitrary argv execution" is covered
only insofar as the grammar fixtures reach the guard's refusal path.

Usage:
  python3 -B reports/round-79/accept-o.py --root <lane> --lands <40hex> \
      --freeze <40hex> --work <scratch>
  python3 -B reports/round-79/accept-o.py --selftest          # isolated
"""

import argparse
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import tempfile
from contextlib import redirect_stdout

CLAIM = "O"
ROUND = 79
VERDICT = "ACCEPT-O-79"
CLAIMS_REL = "reports/round-79/claims.json"
COUNTER_REL = "reports/round-79/accept-o.py"
GUARD_REL_DEFAULT = "tools/ledger-token-guard.py"
FIXTURES_REL_DEFAULT = "reports/round-79/fixtures/o"
TELEMETRY_REL_DEFAULT = "reports/round-79/telemetry"
GUARD_SELFTEST_RECEIPT_DEFAULT = "reports/round-79/telemetry/selftest-guard.txt"
JUNK_RECEIPT_DEFAULT = "reports/round-79/telemetry/junk-o.txt"
CONTROLS_RECEIPT_DEFAULT = "reports/round-79/telemetry/controls-o.txt"
COUNTER_SELFTEST_RECEIPT_DEFAULT = "reports/round-79/telemetry/selftest-o.txt"

REQUIRED_LEGS = ("FROZENCFG", "GREEN", "REDOBS", "REDSTATED", "REDGRAM",
                 "SELFTEST", "RECEIPTS", "STAMP")

OBS_TIMEOUT = 60
OUT_CAP = 1_000_000
HEX40 = re.compile(r"[0-9a-f]{40}")
STAMPED_RE = re.compile(r"^# stamped revision: ([0-9a-f]{40})\s*$", re.M)
EVAL_RE = re.compile(r"^# evaluated revision: ([0-9a-f]{40})\s*$", re.M)
MEASURED_RE = re.compile(r"^# measured revision \(lane main\): ([0-9a-f]{40})\s*$", re.M)
TREE_RE = re.compile(r"^# tree: ([0-9a-f]{40})\s*$", re.M)
SHA_RE = re.compile(r"^# counter sha256 \(self\): ([0-9a-f]{64})\s*$", re.M)
GUARD_SHA_RE = re.compile(r"^# guard sha256: ([0-9a-f]{64})\s*$", re.M)
SELFTEST_LINE_RE = re.compile(r"^SELFTEST:.*$", re.M)
LEG_LINE_RE = re.compile(r"^LEG (PASS|FAIL) (\S+)$", re.M)

# ---------------------------------------------------------------------------
# fixture material (also landed under reports/round-79/fixtures/o/ at lands;
# the selftest dumps byte-identical copies for the integrator)
# ---------------------------------------------------------------------------

FIXTURE_REPO_FILES = {
    "KEYS.txt": "key01\nkey02\nkey03\nkey04\nkey05\n",
    "LOG.md": ("# fixture ledger-token guard observations\n"
               "## 2026-10-30 — round 79 fixture mint\n"
               "total keys: 5\n"),
}

_GREEN_PAIRS = [
    {
        "id": "A01",
        "disposition": "ANNOTATE",
        "stated_at": "LOG.md:1",
        "stated_text": "# fixture ledger-token guard observations",
        "stated_parse": r"^# (.+)$",
        "observe_cmd": ["git", "-C", ".", "grep", "-c", "-E", "^#",
                        "{base}", "--", "LOG.md"],
        "parse": r":([0-9]+)$",
        "expected_after": "1",
        "observed_at_base": "2",
        "rederive": "git -C . grep -c -E '^#' {base} -- LOG.md",
    },
    {
        "id": "A02",
        "disposition": "ANNOTATE",
        "stated_at": "LOG.md:2",
        "stated_text": "## 2026-10-30 — round 79 fixture mint",
        "stated_parse": r"## (\d{4}-\d{2}-\d{2})",
        "observe_cmd": ["git", "-C", ".", "grep", "-c", "-E", "^##",
                        "{base}", "--", "LOG.md"],
        "parse": r":([0-9]+)$",
        "expected_after": "1",
        "observed_at_base": "1",
        "rederive": "git -C . grep -c -E '^##' {base} -- LOG.md",
    },
    {
        "id": "A03",
        "disposition": "ANNOTATE",
        "stated_at": "LOG.md:3",
        "stated_text": "total keys: 5",
        "stated_parse": r"^(total keys: \d+)$",
        "observe_cmd": ["git", "-C", ".", "grep", "-c", "-E", "^key",
                        "{base}", "--", "KEYS.txt"],
        "parse": r":([0-9]+)$",
        "expected_after": "1",
        "observed_at_base": "5",
        "rederive": "git -C . grep -c -E '^key' {base} -- KEYS.txt",
    },
    {
        "id": "A04",
        "disposition": "ANNOTATE",
        "stated_at": "KEYS.txt:1",
        "stated_text": "key01",
        "stated_parse": r"key(\d+)",
        "observe_cmd": ["git", "-C", ".", "cat-file", "-s",
                        "{base}:KEYS.txt"],
        "parse": r"^([0-9]+)$",
        "expected_after": "1",
        "observed_at_base": "30",
        "rederive": "git -C . cat-file -s {base}:KEYS.txt",
    },
]


def _green_ledger():
    return {"round": ROUND, "claim": "O", "base": "{base}",
            "pairs": [dict(p) for p in _GREEN_PAIRS]}


def _mut_observed_ledger():
    ledger = _green_ledger()
    for pair in ledger["pairs"]:
        if pair["id"] == "A02":
            pair["observed_at_base"] = "2"          # actual is 1
    return ledger


def _mut_stated_ledger():
    stated = dict(_GREEN_PAIRS[2])
    stated.update({
        "id": "B01",
        "disposition": "ANNOTATE",
        "stated_at": "LOG.md:3",
        "stated_text": "total keys: 5",
        "stated_parse": r"total keys: (\d+)",
        "observed_at_base": "5",
    })
    return {"round": ROUND, "claim": "O", "base": "{base}",
            "pairs": [stated]}


def _mut_grammar_ledgers():
    echo = _green_ledger()
    for pair in echo["pairs"]:
        pair["observe_cmd"] = ["echo", "1"]
        pair["parse"] = r"^([0-9]+)$"
        pair["observed_at_base"] = "1"
    py = _green_ledger()
    for pair in py["pairs"]:
        pair["observe_cmd"] = ["python3", "-c", "print(1)"]
        pair["parse"] = r"^([0-9]+)$"
        pair["observed_at_base"] = "1"
    head = _green_ledger()
    for pair in head["pairs"]:
        pair["observe_cmd"] = ["git", "-C", ".", "grep", "-c", "-E", "^#",
                               "HEAD", "--", "LOG.md"]
    return echo, py, head


FIXTURE_LEDGER_FILES = {
    "green.json": _green_ledger,
    "mut-observed.json": _mut_observed_ledger,
    "mut-stated.json": _mut_stated_ledger,
}
_GRAMMAR = _mut_grammar_ledgers()
FIXTURE_LEDGER_FILES["mut-grammar-echo.json"] = lambda: _GRAMMAR[0]
FIXTURE_LEDGER_FILES["mut-grammar-python.json"] = lambda: _GRAMMAR[1]
FIXTURE_LEDGER_FILES["mut-grammar-head.json"] = lambda: _GRAMMAR[2]

FIXTURE_MANIFEST = ["repo/KEYS.txt", "repo/LOG.md"] + sorted(
    FIXTURE_LEDGER_FILES)

# The reference guard implements the behavioural contract the counter grades.
# It is a FIXTURE for the counter's isolated selftest only — the production
# guard (ExecGuard seat) is graded at <lands> bytes, never this source.
REFERENCE_GUARD = r'''#!/usr/bin/env python3
r"""reference ledger-token guard — fixture implementation of the contract.

Not the production tools/ledger-token-guard.py.  Exists so the acceptance
counter can be built and self-tested before the production guard lands; the
counter grades whatever bytes sit at <lands>:tools/ledger-token-guard.py.
"""
import argparse
import json
import os
import re
import subprocess
import sys

READONLY_SUB = {"show", "grep", "cat-file", "ls-tree", "rev-parse", "log",
                "diff", "ls-files", "rev-list", "merge-base"}
PRINTERS = {"echo", "printf", "true", "false", "yes"}
INTERPRETERS = {"python", "python2", "python3", "pypy", "pypy3", "sh", "bash",
                "zsh", "dash", "ksh", "fish", "csh", "tcsh", "perl", "node",
                "nodejs", "ruby", "php", "awk", "gawk", "mawk", "sed", "env",
                "xargs", "eval", "exec", "nice", "nohup", "time", "busybox"}
SHELL_META = ("|", "&", ";", "<", ">", "`", "$(", "\n", "\r")
MUTABLE = ("HEAD", "main", "master", "@{", "refs/")
OBS_TIMEOUT = 30
OUT_CAP = 1000000


def _subcommand(argv):
    args = argv[1:]
    i = 0
    while i < len(args):
        a = args[i]
        if a == "-C":
            i += 2
            continue
        if a.startswith("-"):
            i += 1
            continue
        return a
    return None


def grammar_problem(argv, base):
    if not isinstance(argv, list) or not argv:
        return "empty observe_cmd"
    exe = os.path.basename(str(argv[0]))
    if exe in INTERPRETERS:
        return "interpreter %r is refused" % exe
    if exe in PRINTERS:
        return "constant-printer %r is refused" % exe
    if exe != "git":
        return "executable %r is outside the read-only git grammar" % exe
    for el in argv[1:]:
        el = str(el)
        if any(m in el for m in SHELL_META):
            return "shell metacharacter in observe argv element %r" % el
        if any(el == mv or el.startswith(mv) for mv in MUTABLE):
            return "mutable revision %r is refused" % el
    sub = _subcommand(argv)
    if sub not in READONLY_SUB:
        return "git subcommand %r is not in the read-only set" % sub
    pinned = any(str(el) == base or str(el).startswith(base + ":")
                 for el in argv[1:])
    if not pinned:
        return "observation is not pinned at --base %s" % base[:12]
    return None


def run_observe(argv, base, repo):
    cmd = [str(a).replace("{base}", base) for a in argv]
    try:
        r = subprocess.run(cmd, cwd=repo, capture_output=True, text=True,
                           timeout=OBS_TIMEOUT)
    except subprocess.TimeoutExpired:
        return None, "observe timed out after %ds" % OBS_TIMEOUT
    if len(r.stdout) > OUT_CAP:
        return None, "observe output exceeds the %d-byte cap" % OUT_CAP
    if r.returncode != 0:
        return None, "observe exited %d" % r.returncode
    return r.stdout, None


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--ledger")
    ap.add_argument("--repo")
    ap.add_argument("--base")
    ap.add_argument("--work")
    ap.add_argument("--emit")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args(argv)
    if args.selftest:
        return selftest(args.work)
    missing = [name for name in ("ledger", "repo", "base", "work")
               if not getattr(args, name)]
    if missing:
        print("LEDGER-GUARD-79: FAIL (refused: missing %s)"
              % ", ".join("--" + m for m in missing))
        return 2
    if not re.fullmatch(r"[0-9a-f]{40}", args.base):
        print("LEDGER-GUARD-79: FAIL (refused: --base must be 40 hex)")
        return 2
    if not os.path.isdir(args.repo):
        print("LEDGER-GUARD-79: FAIL (refused: --repo %s is not a directory)"
              % args.repo)
        return 2
    work = os.path.abspath(args.work)
    os.makedirs(work, exist_ok=True)
    try:
        ledger = json.load(open(args.ledger, encoding="utf-8"))
    except (OSError, ValueError) as exc:
        print("LEDGER-GUARD-79: FAIL (refused: ledger unreadable: %s)" % exc)
        return 2
    pairs = ledger.get("pairs")
    if not isinstance(pairs, list) or not pairs:
        print("LEDGER-GUARD-79: FAIL (refused: ledger carries no pairs)")
        return 2

    grammar = []
    for pair in pairs:
        if not isinstance(pair, dict) or not isinstance(
                pair.get("observe_cmd"), list):
            grammar.append("PAIR %s: malformed pair (no observe_cmd)"
                           % (pair.get("id") if isinstance(pair, dict)
                              else "?"))
            continue
        subbed = [str(a).replace("{base}", args.base)
                  for a in pair["observe_cmd"]]
        why = grammar_problem(subbed, args.base)
        if why:
            grammar.append("PAIR %s: %s" % (pair.get("id"), why))
    if grammar:
        print("LEDGER-GUARD-79: FAIL (refused: %d grammar problem(s)) "
              "%s" % (len(grammar), grammar[:4]))
        return 2

    results = []
    problems = 0
    for pair in pairs:
        pid = pair.get("id")
        stated = None
        m = re.search(pair.get("stated_parse", ""), pair.get("stated_text", ""))
        if m:
            stated = m.group(1)
        out, why = run_observe(pair["observe_cmd"], args.base, args.repo)
        if out is None:
            results.append({"id": pid, "observed": None, "stated": stated,
                            "status": "unobservable: %s" % why})
            problems += 1
            continue
        m = re.search(pair.get("parse", ""), out)
        if not m:
            results.append({"id": pid, "observed": None, "stated": stated,
                            "status": "unparseable observation"})
            problems += 1
            continue
        observed = m.group(1)
        recorded = str(pair.get("observed_at_base"))
        if recorded != observed:
            results.append({"id": pid, "observed": observed, "stated": stated,
                            "status": "obs-mismatch"})
            problems += 1
            continue
        if stated is not None and stated == observed:
            results.append({"id": pid, "observed": observed, "stated": stated,
                            "status": "not-red"})
            problems += 1
            continue
        results.append({"id": pid, "observed": observed, "stated": stated,
                        "status": "ok"})
    if args.emit:
        with open(args.emit, "w", encoding="utf-8") as fh:
            json.dump({"verdict": "FAIL" if problems else "PASS",
                       "pairs": results}, fh, indent=1)
            fh.write("\n")
    if problems:
        print("LEDGER-GUARD-79: FAIL pairs=%d problems=%d"
              % (len(pairs), problems))
        for pair, res in zip(pairs, results):
            if res["status"] == "obs-mismatch":
                print("PAIR %s: OBS_MISMATCH recorded=%r actual=%r"
                      % (res["id"], str(pair.get("observed_at_base")),
                         res["observed"]))
            elif res["status"] == "not-red":
                print("PAIR %s: NOT_RED token=%r" % (res["id"], res["stated"]))
            else:
                print("PAIR %s: %s" % (res["id"], res["status"]))
        return 1
    print("LEDGER-GUARD-79: PASS pairs=%d" % len(pairs))
    return 0


def selftest(work):
    repo = os.path.join(work, "guard-selftest-repo")
    os.makedirs(repo, exist_ok=True)
    subprocess.run(["git", "-C", repo, "init", "-q"], check=True)
    for rel, text in {"KEYS.txt": "k1\nk2\n",
                      "LOG.md": "# a\n# b\ntotal: 2\n"}.items():
        with open(os.path.join(repo, rel), "w", encoding="utf-8") as fh:
            fh.write(text)
    subprocess.run(["git", "-C", repo, "add", "-A"], check=True)
    subprocess.run(["git", "-C", repo, "-c", "user.name=fixture",
                    "-c", "user.email=fixture@example.invalid",
                    "commit", "-q", "-m", "selftest"], check=True)
    base = subprocess.run(["git", "-C", repo, "rev-parse", "HEAD"],
                          capture_output=True, text=True,
                          check=True).stdout.strip()
    ledger = {"round": 79, "claim": "O", "base": base, "pairs": [{
        "id": "G1", "disposition": "ANNOTATE",
        "stated_at": "LOG.md:1", "stated_text": "# a",
        "stated_parse": r"^# (.+)$",
        "observe_cmd": ["git", "-C", ".", "grep", "-c", "-E", "^k",
                        "{base}", "--", "KEYS.txt"],
        "parse": r":([0-9]+)$", "expected_after": "1",
        "observed_at_base": "2"}]}
    lp = os.path.join(work, "guard-selftest-ledger.json")
    with open(lp, "w", encoding="utf-8") as fh:
        json.dump(ledger, fh)
    ok = True
    c = main(["--ledger", lp, "--repo", repo, "--base", base, "--work", work])
    print("case green exit=%d" % c)
    ok = ok and c == 0
    ledger["pairs"][0]["observed_at_base"] = "3"
    with open(lp, "w", encoding="utf-8") as fh:
        json.dump(ledger, fh)
    c = main(["--ledger", lp, "--repo", repo, "--base", base, "--work", work])
    print("case obs-mismatch exit=%d" % c)
    ok = ok and c == 1
    ledger["pairs"][0]["observed_at_base"] = "2"
    ledger["pairs"][0]["stated_parse"] = r"total: (\d+)"
    ledger["pairs"][0]["stated_text"] = "total: 2"
    ledger["pairs"][0]["observe_cmd"] = ["git", "-C", ".", "grep", "-c",
                                         "-E", "^#", "{base}", "--",
                                         "LOG.md"]
    ledger["pairs"][0]["parse"] = r":([0-9]+)$"
    with open(lp, "w", encoding="utf-8") as fh:
        json.dump(ledger, fh)
    c = main(["--ledger", lp, "--repo", repo, "--base", base, "--work", work])
    print("case not-red exit=%d" % c)
    ok = ok and c == 1
    ledger["pairs"][0]["observe_cmd"] = ["echo", "2"]
    with open(lp, "w", encoding="utf-8") as fh:
        json.dump(ledger, fh)
    c = main(["--ledger", lp, "--repo", repo, "--base", base, "--work", work])
    print("case grammar exit=%d" % c)
    ok = ok and c == 2
    print("SELFTEST: %s green+obs-mismatch+not-red+grammar"
          % ("4/4" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
'''


class ScratchRefused(Exception):
    """No scratch root is available; the counter never invents one."""


# ---------------------------------------------------------------------------
# primitives
# ---------------------------------------------------------------------------

def scratch_dir(explicit=None):
    for label, value in (("--work", explicit),
                         ("$HYAKU_SCRATCH", os.environ.get("HYAKU_SCRATCH")),
                         ("$TMPDIR", os.environ.get("TMPDIR"))):
        if isinstance(value, str) and value.strip():
            root = os.path.abspath(os.path.expanduser(value.strip()))
            os.makedirs(root, exist_ok=True)
            return root
    raise ScratchRefused(
        "no scratch root: pass --work, or set $HYAKU_SCRATCH (preferred) or "
        "$TMPDIR; this counter never invents the system temp dir")


def git(root, *args, timeout=300):
    return subprocess.run(["git", "-C", str(root), *args],
                          capture_output=True, text=True, timeout=timeout)


def show(root, rev, path):
    r = git(root, "show", "%s:%s" % (rev, path))
    if r.returncode != 0:
        return None
    return r.stdout


def sha256_bytes(data):
    return hashlib.sha256(data.encode("utf-8")).hexdigest()


def sha256_file(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def leg(out, name, passed, detail=""):
    out.append((name, bool(passed)))
    print("LEG %s %s" % ("PASS" if passed else "FAIL", name))
    if detail:
        print("     %s" % detail[:600])
    return passed


def note(text):
    print("# %s" % text)


def _refuse(message):
    print("%s: FAIL legs=0/%d (refused: %s)" % (VERDICT, len(REQUIRED_LEGS),
                                                message))
    return 2


def _on_first_parent_chain(root, freeze, lands):
    revs = git(root, "rev-list", "--first-parent", lands).stdout.split()
    return freeze in revs


def leg_name_of(item):
    if not isinstance(item, str):
        return None
    m = re.match(r"^([A-Z][A-Z0-9]*):", item)
    return m.group(1) if m else None


# ---------------------------------------------------------------------------
# frozen configuration
# ---------------------------------------------------------------------------

def load_frozen(root, freeze):
    """(cfg, error).  Everything comes from `git show <freeze>:<path>`."""
    raw = show(root, freeze, CLAIMS_REL)
    if raw is None:
        return None, "claims file %s is not committed at --freeze %s" % (
            CLAIMS_REL, freeze)
    try:
        claims = json.loads(raw)
    except ValueError as exc:
        return None, "claims JSON at --freeze: %s" % exc
    if not isinstance(claims, dict):
        return None, "claims file at --freeze is not an object"
    base = claims.get("base")
    if not isinstance(base, str) or not HEX40.fullmatch(base or ""):
        return None, "claims base %r is not 40-hex" % (base,)
    claim = None
    for item in claims.get("claims", []) or []:
        if isinstance(item, dict) and item.get("id") == CLAIM:
            claim = item
            break
    if claim is None:
        return None, "claims file carries no claim %s" % CLAIM
    legs = claim.get("legs") if isinstance(claim.get("legs"), list) else []
    names = [leg_name_of(x) for x in legs if leg_name_of(x)]
    if names != list(REQUIRED_LEGS):
        return None, ("leg table %r != the frozen %d legs %r (order included)"
                      % (names, len(REQUIRED_LEGS), list(REQUIRED_LEGS)))
    cfg = {"raw": raw, "base": base, "round": claims.get("round"),
           "legs": legs, "leg_names": names}
    cfg["guard_rel"] = claim.get("guard") or GUARD_REL_DEFAULT
    cfg["fixtures_rel"] = claim.get("fixtures") or FIXTURES_REL_DEFAULT
    cfg["telemetry_rel"] = claim.get("telemetry") or TELEMETRY_REL_DEFAULT
    receipts = claim.get("receipts") if isinstance(claim.get("receipts"),
                                                   dict) else {}
    cfg["guard_selftest_receipt"] = receipts.get(
        "guard_selftest") or GUARD_SELFTEST_RECEIPT_DEFAULT
    cfg["junk_receipt"] = receipts.get("junk") or JUNK_RECEIPT_DEFAULT
    cfg["controls_receipt"] = receipts.get("controls") or CONTROLS_RECEIPT_DEFAULT
    cfg["counter_selftest_receipt"] = receipts.get(
        "counter_selftest") or COUNTER_SELFTEST_RECEIPT_DEFAULT
    cfg["counter_rel"] = claim.get("counter") or COUNTER_REL
    manifest = claim.get("fixture_manifest")
    if not isinstance(manifest, list) or not all(
            isinstance(x, str) for x in manifest):
        return None, "frozen claim O carries no fixture_manifest of rel paths"
    cfg["fixture_manifest"] = manifest
    junk = claim.get("junk_expect") if isinstance(claim.get("junk_expect"),
                                                  dict) else {}
    cfg["junk_expect"] = junk
    controls = claim.get("controls_expect") if isinstance(
        claim.get("controls_expect"), dict) else {}
    cfg["controls_expect"] = controls
    if not junk or not controls:
        return None, "frozen claim O carries no junk_expect/controls_expect"
    log_row = claim.get("log_row_lands12")
    cfg["log_row_lands12"] = bool(log_row)
    return cfg, None


# ---------------------------------------------------------------------------
# fixture machinery — the counter re-derives every observation itself from
# committed bytes via git blob operations (never from guard output)
# ---------------------------------------------------------------------------

def _write(root, rel, text):
    path = os.path.join(root, rel)
    os.makedirs(os.path.dirname(path) or root, exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)


def _fixture_commit(root, msg):
    subprocess.run(["git", "-C", root, "add", "-A"], check=True,
                   capture_output=True)
    r = subprocess.run(
        ["git", "-C", root, "-c", "user.name=fixture",
         "-c", "user.email=fixture@example.invalid", "commit", "-q", "-m", msg],
        capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError("fixture commit failed: %s" % r.stderr)
    return git(root, "rev-parse", "HEAD").stdout.strip()


def build_observation_repo(work, tag, files):
    """Materialize the guarded-object fixture repo in explicit scratch.

    (path, head).  The toplevel assertion is the fixture-repo equivalent of
    the lane rule: never run a fixture driver that writes relative paths
    anywhere but inside its own verified root."""
    path = os.path.join(work, "obsrepo-%s" % tag)
    os.makedirs(path)
    subprocess.run(["git", "-C", path, "init", "-q"], check=True,
                   capture_output=True)
    top = git(path, "rev-parse", "--show-toplevel").stdout.strip()
    if os.path.realpath(top) != os.path.realpath(path):
        raise RuntimeError("fixture toplevel %s != %s" % (top, path))
    for rel, text in files.items():
        _write(path, rel, text)
    head = _fixture_commit(path, "observation fixture (%s)" % tag)
    return path, head


def counter_independent(ledger, repo, head):
    """Re-derive stated/observed tokens per pair from committed bytes.

    Returns {id: {stated, observed, on_line, error}}.  Observations run the
    pair's own declared argv with {base} -> <head> against the scratch repo;
    stated_text is verified against the named blob line with git show."""
    out = {}
    for pair in ledger.get("pairs", []):
        pid = pair.get("id")
        entry = {"stated": None, "observed": None, "on_line": None,
                 "error": None}
        try:
            m = re.search(pair.get("stated_parse", ""),
                          pair.get("stated_text", ""))
            entry["stated"] = m.group(1) if m else None
        except re.error as exc:
            entry["error"] = "stated_parse %s" % exc
            out[pid] = entry
            continue
        stated_at = str(pair.get("stated_at", ""))
        if ":" in stated_at:
            rel, _, line = stated_at.rpartition(":")
            blob = show(repo, head, rel)
            if blob is None:
                entry["error"] = "stated_at path %s absent at %s" % (rel,
                                                                     head[:12])
            else:
                lines = blob.splitlines()
                try:
                    idx = int(line) - 1
                    entry["on_line"] = (0 <= idx < len(lines)
                                        and lines[idx] == pair.get("stated_text"))
                except ValueError:
                    entry["error"] = "stated_at line %r not an integer" % line
        argv = pair.get("observe_cmd")
        if not isinstance(argv, list) or not argv:
            entry["error"] = entry["error"] or "no observe_cmd"
            out[pid] = entry
            continue
        cmd = [str(a).replace("{base}", head) for a in argv]
        try:
            r = subprocess.run(cmd, cwd=repo, capture_output=True, text=True,
                               timeout=OBS_TIMEOUT)
        except subprocess.TimeoutExpired:
            entry["error"] = entry["error"] or "observe timed out"
            out[pid] = entry
            continue
        if len(r.stdout) > OUT_CAP:
            entry["error"] = entry["error"] or "observe output over cap"
            out[pid] = entry
            continue
        if r.returncode != 0:
            entry["error"] = entry["error"] or "observe exit %d" % r.returncode
            out[pid] = entry
            continue
        m = re.search(pair.get("parse", ""), r.stdout)
        if not m:
            entry["error"] = entry["error"] or "observation unparseable"
        else:
            entry["observed"] = m.group(1)
        out[pid] = entry
    return out


def extract_guard(work, guard_src, tag):
    path = os.path.join(work, "guard-%s.py" % tag)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(guard_src)
    return path


def run_guard(guard_path, ledger_path, repo, base, work, tag):
    emit = os.path.join(work, "emit-%s.json" % tag)
    env = dict(os.environ)
    env["HYAKU_SCRATCH"] = work
    env["TMPDIR"] = work
    r = subprocess.run(
        [sys.executable, "-B", guard_path, "--ledger", ledger_path,
         "--repo", repo, "--base", base, "--work",
         os.path.join(work, "guardwork-%s" % tag), "--emit", emit],
        capture_output=True, text=True, timeout=600, env=env)
    parsed = None
    if os.path.exists(emit):
        try:
            parsed = json.load(open(emit, encoding="utf-8"))
        except ValueError:
            parsed = None
    return r.returncode, r.stdout, r.stderr, parsed


def run_guard_selftest(guard_path, work, tag):
    env = dict(os.environ)
    env["HYAKU_SCRATCH"] = work
    env["TMPDIR"] = work
    r = subprocess.run(
        [sys.executable, "-B", guard_path, "--selftest", "--work",
         os.path.join(work, "guardselfwork-%s" % tag)],
        capture_output=True, text=True, timeout=600, env=env)
    return r.returncode, r.stdout, r.stderr


def _load_ledger(text, name, problems):
    try:
        ledger = json.loads(text)
    except ValueError as exc:
        problems.append("%s is not JSON: %s" % (name, exc))
        return None
    if not isinstance(ledger, dict) or not isinstance(
            ledger.get("pairs"), list) or not ledger["pairs"]:
        problems.append("%s carries no pairs" % name)
        return None
    return ledger


# ---------------------------------------------------------------------------
# legs
# ---------------------------------------------------------------------------

def leg_frozencfg(out, root, cfg, freeze, lands):
    problems = []
    if freeze == lands:
        note("lands == freeze: do-nothing control shape; the strict-ancestor "
             "requirement is not applied and a PASS is refused")
    elif not _on_first_parent_chain(root, freeze, lands):
        problems.append("--freeze %s is not on the lands first-parent chain"
                        % freeze[:12])
    base = cfg.get("base")
    if git(root, "merge-base", "--is-ancestor", base, freeze).returncode != 0:
        problems.append("frozen base %s is not an ancestor of --freeze"
                        % base[:12])
    manifest = [CLAIMS_REL, cfg["guard_rel"], cfg["counter_rel"],
                cfg["junk_receipt"], cfg["controls_receipt"]]
    manifest += [cfg["fixtures_rel"] + "/" + rel
                 for rel in cfg["fixture_manifest"]]
    for path in manifest:
        blobs = []
        for rev in (freeze, lands):
            r = git(root, "rev-parse", "%s:%s" % (rev, path))
            blobs.append(r.stdout.strip() if r.returncode == 0 else None)
        if blobs[1] is None:
            problems.append("%s is absent from the graded tree" % path)
        elif blobs[0] is None:
            problems.append("%s is absent at --freeze" % path)
        elif blobs[0] != blobs[1]:
            problems.append("%s was edited in the graded tree after freeze"
                            % path)
    detail = ("freeze=%s%s base=%s manifest=%d legs=%s"
              % (freeze[:12],
                 " (do-nothing)" if freeze == lands else "",
                 (base or "")[:12], len(manifest),
                 ",".join(cfg["leg_names"])))
    if problems:
        detail += " problems=%d %s" % (len(problems), problems[:6])
    return leg(out, "FROZENCFG", not problems, detail)


def leg_green(out, root, cfg, lands, work, repo, head):
    problems = []
    rel = cfg["fixtures_rel"] + "/green.json"
    text = show(root, lands, rel)
    if text is None:
        return leg(out, "GREEN", False, "%s absent from the graded tree" % rel)
    ledger = _load_ledger(text, "green.json", problems)
    if ledger is None:
        return leg(out, "GREEN", False, "; ".join(problems))
    indep = counter_independent(ledger, repo, head)
    for pair in ledger.get("pairs", []):
        pid = pair.get("id")
        e = indep.get(pid, {})
        if e.get("error"):
            problems.append("%s: counter re-derivation failed: %s"
                            % (pid, e["error"]))
            continue
        if not e.get("on_line"):
            problems.append("%s: stated_text not on its stated_at line at %s"
                            % (pid, head[:12]))
        if str(pair.get("observed_at_base")) != e.get("observed"):
            problems.append("%s: green fixture lies: recorded observed_at_base "
                            "%r != actual %r" % (pid, pair.get("observed_at_base"),
                                                 e.get("observed")))
    guard_path = extract_guard(work, GUARD_SRC[0], "green")
    lp = os.path.join(work, "ledger-green.json")
    with open(lp, "w", encoding="utf-8") as fh:
        fh.write(text)
    code, stdout, _s, emit = run_guard(guard_path, lp, repo, head, work,
                                       "green")
    if code != 0:
        problems.append("guard exit %d on the green fixture: %s"
                        % (code, stdout.strip().splitlines()[0][:120]
                           if stdout.strip() else "<no output>"))
    elif "LEDGER-GUARD-79: PASS pairs=%d" % len(ledger["pairs"]) not in stdout:
        problems.append("guard green verdict line missing/wrong: %r"
                        % (stdout.strip()[:120],))
    if isinstance(emit, dict):
        emap = {p.get("id"): p for p in emit.get("pairs", [])}
        for pair in ledger.get("pairs", []):
            pid = pair.get("id")
            e = indep.get(pid, {})
            em = emap.get(pid)
            if em is None:
                problems.append("%s: guard emit omits the pair" % pid)
                continue
            if str(em.get("observed")) != str(e.get("observed")):
                problems.append("%s: guard observed %r != counter re-derived %r"
                                % (pid, em.get("observed"), e.get("observed")))
            if str(em.get("stated")) != str(e.get("stated")):
                problems.append("%s: guard stated %r != counter re-derived %r"
                                % (pid, em.get("stated"), e.get("stated")))
            if em.get("status") != "ok":
                problems.append("%s: guard status %r on the green fixture"
                                % (pid, em.get("status")))
    else:
        problems.append("guard emitted no machine-readable --emit JSON")
    detail = ("pairs=%d guard_exit=%d emit_pairs=%s"
              % (len(ledger.get("pairs", [])), code,
                 len(emit.get("pairs", [])) if isinstance(emit, dict) else "-"))
    if problems:
        detail += " problems=%d %s" % (len(problems), problems[:6])
    return leg(out, "GREEN", not problems, detail)


def _reject_leg(out, name, root, cfg, lands, work, repo, head, fixture,
                label, bad_kind):
    rel = cfg["fixtures_rel"] + "/" + fixture
    text = show(root, lands, rel)
    problems = []
    if text is None:
        return leg(out, name, False, "%s absent from the graded tree" % rel)
    ledger = _load_ledger(text, fixture, problems)
    if ledger is None:
        return leg(out, name, False, "; ".join(problems))
    indep = counter_independent(ledger, repo, head)
    bad = []
    for pair in ledger.get("pairs", []):
        pid = pair.get("id")
        e = indep.get(pid, {})
        if bad_kind == "obs":
            if not e.get("error") and str(pair.get("observed_at_base")) != \
                    e.get("observed"):
                bad.append(pid)
        elif bad_kind == "stated":
            if not e.get("error") and e.get("stated") is not None and \
                    e.get("stated") == e.get("observed"):
                bad.append(pid)
    if not bad:
        problems.append("fixture carries no counter-verified %s pair"
                        % bad_kind)
    guard_path = extract_guard(work, GUARD_SRC[0], name.lower())
    lp = os.path.join(work, "ledger-%s" % fixture)
    with open(lp, "w", encoding="utf-8") as fh:
        fh.write(text)
    code, stdout, _s, emit = run_guard(guard_path, lp, repo, head, work,
                                       name.lower())
    if code != 1:
        problems.append("guard exit %d, want 1 (stdout %r)"
                        % (code, stdout.strip()[:120]))
    for pid in bad:
        if ("PAIR %s:" % pid) not in stdout or label not in stdout:
            problems.append("guard output names no %s for pair %s"
                            % (label, pid))
    if isinstance(emit, dict):
        emap = {p.get("id"): p for p in emit.get("pairs", [])}
        for pid in bad:
            em = emap.get(pid, {})
            e = indep.get(pid, {})
            want = "obs-mismatch" if bad_kind == "obs" else "not-red"
            if em.get("status") != want:
                problems.append("guard emit status %r for %s, want %r"
                                % (em.get("status"), pid, want))
            if str(em.get("observed")) != str(e.get("observed")):
                problems.append("guard observed %r != counter %r for %s"
                                % (em.get("observed"), e.get("observed"), pid))
    else:
        problems.append("guard emitted no machine-readable --emit JSON")
    detail = ("bad=%s guard_exit=%d" % (bad, code))
    if problems:
        detail += " problems=%d %s" % (len(problems), problems[:6])
    return leg(out, name, not problems, detail)


def leg_redobs(out, root, cfg, lands, work, repo, head):
    return _reject_leg(out, "REDOBS", root, cfg, lands, work, repo, head,
                       "mut-observed.json", "OBS_MISMATCH", "obs")


def leg_redstated(out, root, cfg, lands, work, repo, head):
    return _reject_leg(out, "REDSTATED", root, cfg, lands, work, repo, head,
                       "mut-stated.json", "NOT_RED", "stated")


def leg_redgram(out, root, cfg, lands, work, repo, head):
    fixtures = {"mut-grammar-echo.json": ("echo", "constant-printer"),
                "mut-grammar-python.json": ("python3", "constant-printer"),
                "mut-grammar-head.json": ("HEAD", "mutable-revision")}
    problems = []
    exits = {}
    for fixture in sorted(fixtures):
        token, kind = fixtures[fixture]
        rel = cfg["fixtures_rel"] + "/" + fixture
        text = show(root, lands, rel)
        if text is None:
            problems.append("%s absent from the graded tree" % rel)
            continue
        if token not in text:
            problems.append("%s does not carry the %s token %r"
                            % (fixture, kind, token))
        ledger = _load_ledger(text, fixture, problems)
        if ledger is None:
            continue
        guard_path = extract_guard(work, GUARD_SRC[0],
                                   fixture.replace(".", "-"))
        lp = os.path.join(work, "ledger-%s" % fixture)
        with open(lp, "w", encoding="utf-8") as fh:
            fh.write(text)
        code, stdout, _s, _e = run_guard(guard_path, lp, repo, head, work,
                                         fixture.replace(".", "-"))
        exits[fixture] = code
        if code != 2:
            problems.append("guard exit %d on %s (%s), want refusal 2"
                            % (code, fixture, kind))
        elif "refused" not in stdout:
            problems.append("guard stdout names no refusal on %s: %r"
                            % (fixture, stdout.strip()[:100]))
    detail = "exits=%s" % exits
    if problems:
        detail += " problems=%d %s" % (len(problems), problems[:6])
    return leg(out, "REDGRAM", not problems, detail)


def leg_selftest(out, root, cfg, lands, work):
    problems = []
    receipt_rel = cfg["guard_selftest_receipt"]
    receipt = show(root, lands, receipt_rel)
    if receipt is None:
        return leg(out, "SELFTEST", False,
                   "%s absent from the graded tree" % receipt_rel)
    guard_src = GUARD_SRC[0]
    m = GUARD_SHA_RE.search(receipt)
    if not m:
        problems.append("receipt carries no '# guard sha256:' header")
    elif m.group(1) != sha256_bytes(guard_src):
        problems.append("receipt guard sha256 %s != the lands guard blob %s"
                        % (m.group(1)[:12], sha256_bytes(guard_src)[:12]))
    st = SELFTEST_LINE_RE.search(receipt)
    if not st:
        problems.append("receipt carries no SELFTEST: line")
    guard_path = extract_guard(work, guard_src, "selftest")
    code, stdout, _s = run_guard_selftest(guard_path, work, "selftest")
    if code != 0:
        problems.append("live guard --selftest exit %d" % code)
    if st and st.group(0) not in stdout:
        problems.append("live guard --selftest does not reproduce the "
                        "committed SELFTEST line %r" % st.group(0))
    detail = ("receipt=%s live_exit=%d" % (receipt_rel, code))
    if problems:
        detail += " problems=%d %s" % (len(problems), problems[:6])
    return leg(out, "SELFTEST", not problems, detail)


def leg_receipts(out, root, cfg, lands, freeze):
    problems = []
    for rel in (cfg["junk_receipt"], cfg["controls_receipt"]):
        for rev in (freeze, lands):
            if show(root, rev, rel) is None:
                problems.append("%s absent at %s" % (rel, rev[:12]))
        a = show(root, freeze, rel)
        b = show(root, lands, rel)
        if a is not None and b is not None and a != b:
            problems.append("%s changed after freeze" % rel)
    junk = show(root, lands, cfg["junk_receipt"]) or ""
    for fixture, expect in sorted(cfg["junk_expect"].items()):
        leg_name = expect.get("leg") if isinstance(expect, dict) else None
        code = expect.get("exit") if isinstance(expect, dict) else None
        line = next((l for l in junk.splitlines()
                     if fixture in l), None)
        if line is None:
            problems.append("junk receipt names no %s" % fixture)
            continue
        if "exit=%s" % code not in line:
            problems.append("junk receipt %s exit mismatch: %r" % (fixture, line))
        if leg_name and ("LEG FAIL %s" % leg_name) not in line:
            problems.append("junk receipt %s names no LEG FAIL %s: %r"
                            % (fixture, leg_name, line[:120]))
    controls = show(root, lands, cfg["controls_receipt"]) or ""
    for control, code in sorted(cfg["controls_expect"].items()):
        line = next((l for l in controls.splitlines()
                     if control in l), None)
        if line is None:
            problems.append("controls receipt names no %s" % control)
        elif "exit=%s" % code not in line:
            problems.append("controls receipt %s exit mismatch: %r"
                            % (control, line))
    counter_st = show(root, lands, cfg["counter_selftest_receipt"])
    if counter_st is None:
        problems.append("counter selftest receipt %s absent from the graded "
                        "tree" % cfg["counter_selftest_receipt"])
    else:
        lines = counter_st.splitlines()
        if not any("clean -> exit=0" in l for l in lines[:3]):
            problems.append("counter selftest receipt names no green clean "
                            "scenario in its first lines")
        if not SELFTEST_LINE_RE.search(counter_st):
            problems.append("counter selftest receipt carries no SELFTEST: "
                            "summary line")
    log = show(root, lands, "LOG.md")
    if log is None:
        problems.append("LOG.md absent from the graded tree")
    elif not any("claim O" in l and "round-79" in l
                 for l in log.splitlines()):
        problems.append("LOG.md carries no round-79 claim-O lands row")
    detail = ("junk=%s controls=%s counter_selftest=%s"
              % (cfg["junk_receipt"], cfg["controls_receipt"],
                 cfg["counter_selftest_receipt"]))
    if problems:
        detail += " problems=%d %s" % (len(problems), problems[:8])
    return leg(out, "RECEIPTS", not problems, detail)


def leg_stamp(out, header, root, lands):
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
    counter_blob = show(root, lands, COUNTER_REL)
    if counter_blob is None:
        problems.append("%s absent from the graded tree" % COUNTER_REL)
    elif sha256_bytes(counter_blob) != header.get("sha"):
        problems.append("counter blob at lands != this counter's sha256")
    detail = ("stamped=evaluated=measured=%s tree=%s counter=%s"
              % (lands[:12], (header.get("tree") or "")[:12],
                 (header.get("sha") or "")[:12]))
    if problems:
        detail += " problems=%s" % problems
    return leg(out, "STAMP", not problems, detail)


# ---------------------------------------------------------------------------
# driver
# ---------------------------------------------------------------------------

GUARD_SRC = [None]          # filled by main_check (extracted from lands)


def main_check(root, lands, freeze, work=None, main_branch="main"):
    root = os.path.abspath(root)
    try:
        work = scratch_dir(work)
    except ScratchRefused as exc:
        return _refuse(str(exc))
    if not HEX40.fullmatch(lands):
        return _refuse("--lands must be 40 hex")
    if not HEX40.fullmatch(freeze):
        return _refuse("--freeze must be 40 hex")
    for label, rev in (("--lands", lands), ("--freeze", freeze)):
        if git(root, "cat-file", "-e", "%s^{commit}" % rev).returncode != 0:
            print("ERROR: %s %s is not a commit in %s" % (label, rev, root),
                  file=sys.stderr)
            return 2
    cfg, err = load_frozen(root, freeze)
    if err:
        return _refuse(err)
    base = cfg["base"]
    if lands == base:
        return _refuse("--lands equals the frozen base %s" % base[:12])
    if lands != freeze and not _on_first_parent_chain(root, freeze, lands):
        return _refuse("--freeze %s is not on the lands first-parent chain"
                       % freeze[:12])
    if git(root, "merge-base", "--is-ancestor", base, freeze).returncode != 0:
        return _refuse("frozen base %s is not an ancestor of --freeze"
                       % base[:12])

    guard_src = show(root, lands, cfg["guard_rel"])
    GUARD_SRC[0] = guard_src if guard_src is not None else ""
    if guard_src is None:
        note("guard %s is absent from the graded tree" % cfg["guard_rel"])

    measured = git(root, "rev-parse", "--verify", "--quiet",
                   "%s^{commit}" % main_branch).stdout.strip()
    measured_note = ""
    if not measured:
        measured = git(root, "rev-parse", "HEAD").stdout.strip()
        measured_note = " (fallback HEAD: %s unresolved)" % main_branch
    tree = git(root, "rev-parse", "%s^{tree}" % lands).stdout.strip()
    header = {"stamped": lands, "evaluated": lands, "measured": measured,
              "tree": tree, "sha": sha256_file(__file__)}
    print("# counter sha256 (self): %s" % header["sha"])
    print("# stamped revision: %s" % header["stamped"])
    print("# evaluated revision: %s" % header["evaluated"])
    print("# measured revision (lane main): %s%s" % (header["measured"],
                                                     measured_note))
    print("# tree: %s" % header["tree"])
    print("# claim: %s  round: %r  base: %s" % (CLAIM, cfg.get("round"),
                                                base))
    print("# freeze: %s (config read at this commit only)" % freeze)
    print("# frozen legs: %d (%s)" % (len(cfg["leg_names"]),
                                      ", ".join(cfg["leg_names"])))
    print("# guard: %s source=lands sha256=%s" % (cfg["guard_rel"],
                                                  sha256_bytes(GUARD_SRC[0])
                                                  if guard_src else "absent"))
    print("# fixtures: %s (%d files)" % (cfg["fixtures_rel"],
                                         len(cfg["fixture_manifest"])))

    out = []
    tmpdir = tempfile.mkdtemp(prefix="r79-o-", dir=work)
    # the guarded-object fixture repo is materialized from committed fixture
    # bytes in explicit scratch — never from a moving worktree
    repo_files = {}
    missing = []
    for rel in cfg["fixture_manifest"]:
        if not rel.startswith("repo/"):
            continue
        blob = show(root, lands, cfg["fixtures_rel"] + "/" + rel)
        if blob is None:
            missing.append(rel)
        else:
            repo_files[rel[len("repo/"):]] = blob
    obs_repo = obs_head = None
    if missing:
        note("fixture repo files absent at lands: %s" % missing)
    elif repo_files:
        obs_repo, obs_head = build_observation_repo(tmpdir, "main", repo_files)
        note("observation repo: %s head=%s" % (obs_repo, obs_head))

    leg_frozencfg(out, root, cfg, freeze, lands)
    if obs_repo and guard_src:
        leg_green(out, root, cfg, lands, tmpdir, obs_repo, obs_head)
        leg_redobs(out, root, cfg, lands, tmpdir, obs_repo, obs_head)
        leg_redstated(out, root, cfg, lands, tmpdir, obs_repo, obs_head)
        leg_redgram(out, root, cfg, lands, tmpdir, obs_repo, obs_head)
    else:
        for name in ("GREEN", "REDOBS", "REDSTATED", "REDGRAM"):
            leg(out, name, False,
                "guard or fixture repo absent — behaviour legs unevaluated")
    if guard_src:
        leg_selftest(out, root, cfg, lands, tmpdir)
    else:
        leg(out, "SELFTEST", False, "guard absent from the graded tree")
    leg_receipts(out, root, cfg, lands, freeze)
    leg_stamp(out, header, root, lands)

    passed = sum(1 for _n, ok in out if ok)
    total = len(out)
    print("%s: %s legs=%d/%d" % (VERDICT,
                                 "PASS" if passed == total else "FAIL",
                                 passed, total))
    return 0 if passed == total else 1


# ---------------------------------------------------------------------------
# selftest — every fixture repo is initialized here, under explicit scratch;
# the toplevel assertion runs before any fixture driver writes a relative path
# ---------------------------------------------------------------------------

def _git_init(path):
    r = subprocess.run(["git", "-C", path, "init", "-q"],
                       capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError("git init failed: %s" % r.stderr)
    top = git(path, "rev-parse", "--show-toplevel").stdout.strip()
    if os.path.realpath(top) != os.path.realpath(path):
        raise RuntimeError("fixture toplevel %s != %s" % (top, path))


def _claims_doc(base, junk_expect, controls_expect):
    legs = [
        "FROZENCFG: <freeze> is on the <lands> first-parent chain (<lands> == "
        "<freeze> is graded, never passed, as the do-nothing control); the "
        "frozen base is an ancestor of <freeze>; the guard, the fixture files "
        "and claims.json are byte-identical between <freeze> and <lands>",
        "GREEN: the committed green fixture is truthful (the counter "
        "re-derives every stated and observed token from committed fixture "
        "bytes via git blob operations, never from guard output) and the "
        "guard extracted from <lands> bytes grades it PASS with exit 0 and a "
        "per-pair --emit agreeing with the counter's re-derivation",
        "REDOBS: the committed mut-observed fixture really falsifies a "
        "recorded observation (counter re-derived) and the guard rejects it "
        "exit 1 with an OBS_MISMATCH label naming the pair",
        "REDSTATED: the committed mut-stated fixture really has stated == "
        "observed (counter re-derived) and the guard rejects it exit 1 with "
        "a NOT_RED label naming the pair",
        "REDGRAM: the committed grammar fixtures really carry a constant "
        "printer or a mutable revision (counter-verified from committed "
        "bytes) and the guard refuses them exit 2",
        "SELFTEST: the committed guard-selftest receipt at <lands> names the "
        "<lands> guard blob sha256 and the guard's live --selftest re-run "
        "(from <lands> bytes, in explicit scratch) exits 0 and reproduces "
        "the receipt's SELFTEST line",
        "RECEIPTS: the junk and control receipts shipped at <freeze> are "
        "committed unchanged at <lands> and carry the expected per-fixture "
        "verdict lines; the counter's own committed selftest receipt names a "
        "green clean scenario; LOG.md carries the round-79 claim-O lands row",
        "STAMP: this run's receipt headers carry stamped == evaluated == "
        "measured == <lands>, the lands tree and this counter's sha256",
    ]
    return {
        "round": ROUND,
        "base": base,
        "claims": [{
            "id": "O",
            "axis": "operability",
            "guard": GUARD_REL_DEFAULT,
            "fixtures": FIXTURES_REL_DEFAULT,
            "telemetry": TELEMETRY_REL_DEFAULT,
            "counter": COUNTER_REL,
            "receipts": {
                "guard_selftest": GUARD_SELFTEST_RECEIPT_DEFAULT,
                "junk": JUNK_RECEIPT_DEFAULT,
                "controls": CONTROLS_RECEIPT_DEFAULT,
                "counter_selftest": COUNTER_SELFTEST_RECEIPT_DEFAULT,
            },
            "fixture_manifest": FIXTURE_MANIFEST,
            "junk_expect": junk_expect,
            "controls_expect": controls_expect,
            "log_row_lands12": True,
            "legs": legs,
        }],
    }


def _build_fixture_lane(td, tag, claims_mutate=None, guard=None,
                        junk_expect=None, controls_expect=None):
    """(lane, base, apparatus, freeze, olands).

    apparatus = the tree carrying claims+counter+guard+fixtures (the freeze's
    parent once the receipts are written); freeze = apparatus + the
    junk/controls receipts; olands = freeze + selftest-guard.txt + LOG row.
    Junk/control receipt runs happen against trees branched from apparatus —
    the receipt lines name apparatus as --freeze (receipts cannot name their
    own carrying commit)."""
    lane = os.path.join(td, tag, "lane")
    os.makedirs(lane)
    _git_init(lane)
    _write(lane, "LOG.md", "# fixture lane log\n")
    _write(lane, "README.md", "# fixture lane for accept-o selftest\n")
    base = _fixture_commit(lane, "fixture base")

    with open(__file__, "rb") as fh:
        counter_bytes = fh.read()
    claims = _claims_doc(base, junk_expect or {}, controls_expect or {})
    if claims_mutate:
        claims = claims_mutate(claims)
    _write(lane, COUNTER_REL, counter_bytes.decode("utf-8"))
    _write(lane, CLAIMS_REL, json.dumps(claims, indent=1) + "\n")
    _write(lane, GUARD_REL_DEFAULT, guard if guard is not None
           else REFERENCE_GUARD)
    for rel, text in FIXTURE_REPO_FILES.items():
        _write(lane, FIXTURES_REL_DEFAULT + "/repo/" + rel, text)
    for name, maker in FIXTURE_LEDGER_FILES.items():
        _write(lane, FIXTURES_REL_DEFAULT + "/" + name,
               json.dumps(maker(), indent=1) + "\n")
    apparatus = _fixture_commit(lane, "claim O apparatus (claims + guard + "
                                     "fixtures)")
    return lane, base, apparatus, claims


def _branch(root, name, rev):
    git(root, "checkout", "-q", "-B", name, rev)


def _run(lane, lands, freeze, work, main_branch="main"):
    buf = io.StringIO()
    with redirect_stdout(buf):
        code = main_check(lane, lands, freeze, work=work,
                          main_branch=main_branch)
    text = buf.getvalue()
    states = {}
    for m in LEG_LINE_RE.finditer(text):
        states[m.group(2)] = m.group(1)
    return code, states, text


def _run_subprocess(lane, lands, freeze, work, scratch_env=True):
    argv = [sys.executable, "-B", os.path.abspath(__file__),
            "--root", lane, "--lands", lands, "--freeze", freeze]
    env = dict(os.environ)
    if scratch_env:
        env["HYAKU_SCRATCH"] = work
        env["TMPDIR"] = work
    else:
        env.pop("HYAKU_SCRATCH", None)
        env.pop("TMPDIR", None)
    return subprocess.run(argv, cwd=lane, capture_output=True, text=True,
                          env=env, timeout=600)


def _junk_line(fixture, commit, freeze, exit_code, leg_name):
    return ("%s commit=%s freeze=%s cmd=\"python3 -B %s --root <lane> "
            "--lands %s --freeze %s --work $HYAKU_SCRATCH\" -> exit=%d "
            "LEG FAIL %s" % (fixture, commit, freeze[:12], COUNTER_REL,
                             commit, freeze[:12], exit_code, leg_name))


def selftest():
    results = []

    def check(label, cond, detail=""):
        results.append((label, bool(cond)))
        if not cond:
            print("SELFTEST FAIL: %s %s" % (label, detail))

    scenarios = []

    def scenario(label, lane, lands, freeze, want_exit, want, work,
                 text_must=()):
        code, states, text = _run(lane, lands, freeze, work)
        print("selftest: %s -> exit=%d %s" % (label, code, " ".join(
            "%s=%s" % (k, states.get(k, "-")) for k in REQUIRED_LEGS)))
        if code != want_exit:
            print(text)
        scenarios.append(label)
        check("%s exit" % label, code == want_exit,
              "got %d want %d" % (code, want_exit))
        for name, state in want.items():
            check("%s %s" % (label, name), states.get(name) == state,
                  "got %r want %r" % (states.get(name), state))
        for needle in text_must:
            check("%s text %r" % (label, needle), needle in text)
        return code, states, text

    td = tempfile.mkdtemp(prefix="r79-o-selftest-", dir=scratch_dir())
    dump = os.environ.get("DUMP_FIXTURES")
    if dump:
        os.makedirs(dump, exist_ok=True)

    # expectation tables (the frozen claims carry the same tables)
    junk_expect = {
        "J-01": {"leg": "FROZENCFG", "exit": 1},
        "J-02": {"leg": "GREEN", "exit": 1},
        "J-03": {"leg": "FROZENCFG", "exit": 1},
        "J-04": {"leg": "SELFTEST", "exit": 1},
    }
    controls_expect = {
        "C-01": 1, "C-02": 2, "C-03": 2, "C-04": 2, "C-05": 2, "C-06": 2,
    }

    lane, base, apparatus, claims = _build_fixture_lane(
        td, "main", junk_expect=junk_expect, controls_expect=controls_expect)
    work = os.path.join(td, "main", "work")

    # junk trees branched from the apparatus commit, receipt runs recorded
    junk_lines = []
    _branch(lane, "j01", apparatus)
    _write(lane, GUARD_REL_DEFAULT,
           "#!/usr/bin/env python3\n"
           "print('LEDGER-GUARD-79: PASS pairs=4')\n")
    j01 = _fixture_commit(lane, "J-01 stub guard printing the verdict")
    code, states, _ = _run(lane, j01, apparatus, work)
    junk_lines.append(_junk_line("J-01 stub-guard", j01, apparatus, code,
                                 "FROZENCFG"))
    check("J-01 ran red on FROZENCFG",
          states.get("FROZENCFG") == "FAIL" and code == 1,
          str(states))

    _branch(lane, "j02", apparatus)
    lie = _mut_observed_ledger()
    _write(lane, FIXTURES_REL_DEFAULT + "/green.json",
           json.dumps(lie, indent=1) + "\n")
    j02 = _fixture_commit(lane, "J-02 lying green fixture")
    code, states, _ = _run(lane, j02, apparatus, work)
    junk_lines.append(_junk_line("J-02 green-lie", j02, apparatus, code,
                                 "GREEN"))
    check("J-02 ran red on GREEN",
          states.get("GREEN") == "FAIL" and code == 1, str(states))

    _branch(lane, "j03", apparatus)
    tamper = _mut_observed_ledger()
    for pair in tamper["pairs"]:
        if pair["id"] == "A02":
            pair["observed_at_base"] = "3"
    _write(lane, FIXTURES_REL_DEFAULT + "/mut-observed.json",
           json.dumps(tamper, indent=1) + "\n")
    j03 = _fixture_commit(lane, "J-03 fixture tampered after freeze")
    code, states, _ = _run(lane, j03, apparatus, work)
    junk_lines.append(_junk_line("J-03 tamper-fixture", j03, apparatus, code,
                                 "FROZENCFG"))
    check("J-03 ran red on FROZENCFG",
          states.get("FROZENCFG") == "FAIL" and code == 1, str(states))

    _branch(lane, "j04", apparatus)
    _write(lane, GUARD_SELFTEST_RECEIPT_DEFAULT,
           "# guard sha256: %s\nSELFTEST: forged receipt\n" % ("0" * 64))
    j04 = _fixture_commit(lane, "J-04 forged guard selftest receipt")
    code, states, _ = _run(lane, j04, apparatus, work)
    junk_lines.append(_junk_line("J-04 receipt-mismatch", j04, apparatus,
                                 code, "SELFTEST"))
    check("J-04 ran red on SELFTEST",
          states.get("SELFTEST") == "FAIL" and code == 1, str(states))

    # control receipts, all against the apparatus tree
    code, states, _ = _run(lane, apparatus, apparatus, work)
    controls_lines = ["C-01 do-nothing(lands=freeze=apparatus) exit=%d "
                      "legs=%s" % (code, ",".join(
                          k for k, v in states.items() if v == "FAIL"))]
    check("C-01 do-nothing red", code == 1 and states.get("SELFTEST") == "FAIL"
          and states.get("RECEIPTS") == "FAIL", str(states))
    proc = _run_subprocess(lane, apparatus, apparatus, work, scratch_env=False)
    controls_lines.append("C-02 no-scratch exit=%d (refused)" % proc.returncode)
    check("C-02 no-scratch refused", proc.returncode == 2
          and "no scratch root" in proc.stdout, proc.stdout[-160:])
    def _short_legs(c):
        c["claims"][0]["legs"] = c["claims"][0]["legs"][:-1]
        return c

    def _swap_legs(c):
        legs = c["claims"][0]["legs"]
        c["claims"][0]["legs"] = [legs[1], legs[0]] + legs[2:]
        return c

    lane_lc, _b, apparatus_lc, _c = _build_fixture_lane(
        td, "legcount", claims_mutate=_short_legs,
        junk_expect=junk_expect, controls_expect=controls_expect)
    code, _s, text_lc = _run(lane_lc, apparatus_lc, apparatus_lc,
                             os.path.join(td, "legcount", "work"))
    controls_lines.append("C-03 legcount exit=%d (refused)" % code)
    check("C-03 legcount refused", code == 2 and "leg table" in text_lc,
          text_lc[-160:])
    lane_lo, _b2, apparatus_lo, _c2 = _build_fixture_lane(
        td, "legorder", claims_mutate=_swap_legs,
        junk_expect=junk_expect, controls_expect=controls_expect)
    code, _s, text_lo = _run(lane_lo, apparatus_lo, apparatus_lo,
                             os.path.join(td, "legorder", "work"))
    controls_lines.append("C-04 legorder exit=%d (refused)" % code)
    check("C-04 legorder refused", code == 2 and "leg table" in text_lo,
          text_lo[-160:])
    code, _s, text_base = _run(lane, base, apparatus, work)
    controls_lines.append("C-05 lands-eq-base exit=%d (refused)" % code)
    check("C-05 lands-eq-base refused", code == 2
          and "frozen base" in text_base, text_base[-160:])
    _branch(lane, "offp", base)
    _write(lane, "side.md", "side\n")
    side = _fixture_commit(lane, "side branch")
    code, _s, text_ofp = _run(lane, side, apparatus, work)
    controls_lines.append("C-06 freeze-off-first-parent exit=%d (refused)"
                          % code)
    check("C-06 freeze-off-first-parent refused",
          code == 2 and "first-parent" in text_ofp, text_ofp[-160:])
    _branch(lane, "main", apparatus)

    # the freeze: apparatus + the junk/controls receipts + the counter's
    # committed selftest receipt (the real W1 receipt lands with the
    # production O-lands; this fixture copy carries the same shape)
    _write(lane, JUNK_RECEIPT_DEFAULT, "\n".join(junk_lines) + "\n")
    _write(lane, CONTROLS_RECEIPT_DEFAULT, "\n".join(controls_lines) + "\n")
    _write(lane, COUNTER_SELFTEST_RECEIPT_DEFAULT,
           "selftest: do-nothing -> exit=1 FROZENCFG=PASS GREEN=PASS "
           "REDOBS=PASS REDSTATED=PASS REDGRAM=PASS SELFTEST=FAIL "
           "RECEIPTS=FAIL STAMP=PASS\n"
           "selftest: clean -> exit=0 FROZENCFG=PASS GREEN=PASS REDOBS=PASS "
           "REDSTATED=PASS REDGRAM=PASS SELFTEST=PASS RECEIPTS=PASS "
           "STAMP=PASS\n"
           "SELFTEST: receipt (fixture copy; the production receipt is the "
           "counter's own --selftest output)\n")
    freeze = _fixture_commit(lane, "freeze (claims + counter + guard + "
                                   "fixtures + receipts)")
    _branch(lane, "freeze", freeze)
    _branch(lane, "main", freeze)

    # the O-lands: freeze + the live guard selftest receipt + the LOG row
    guard_path = extract_guard(work, REFERENCE_GUARD, "receipt")
    gcode, gout, _gerr = run_guard_selftest(guard_path, work, "receipt")
    check("reference guard selftest green", gcode == 0, gout[-200:])
    receipt = "# guard sha256: %s\n%s" % (sha256_bytes(REFERENCE_GUARD), gout)
    _branch(lane, "lands", freeze)
    _write(lane, GUARD_SELFTEST_RECEIPT_DEFAULT, receipt)
    with open(os.path.join(lane, "LOG.md"), "a", encoding="utf-8") as fh:
        fh.write("## round-79 — claim O (operability) lands row\n")
    olands = _fixture_commit(lane, "claim O lands (guard selftest receipt + "
                                   "LOG row)")
    _branch(lane, "lands", olands)
    _branch(lane, "main", olands)

    if dump:
        for rel in ([CLAIMS_REL, COUNTER_REL, GUARD_REL_DEFAULT,
                     JUNK_RECEIPT_DEFAULT, CONTROLS_RECEIPT_DEFAULT,
                     GUARD_SELFTEST_RECEIPT_DEFAULT,
                     COUNTER_SELFTEST_RECEIPT_DEFAULT]
                    + [FIXTURES_REL_DEFAULT + "/" + r
                       for r in FIXTURE_LEDGER_FILES]
                    + [FIXTURES_REL_DEFAULT + "/repo/" + r
                       for r in FIXTURE_REPO_FILES]):
            src = os.path.join(lane, rel)
            if os.path.exists(src):
                dst = os.path.join(dump, rel)
                os.makedirs(os.path.dirname(dst), exist_ok=True)
                with open(src, "rb") as a, open(dst, "wb") as b:
                    b.write(a.read())

    # 1. do-nothing control: lands == freeze is graded, never PASS
    _branch(lane, "main", freeze)
    scenario("do-nothing", lane, freeze, freeze, 1,
             {"SELFTEST": "FAIL", "RECEIPTS": "FAIL",
              "GREEN": "PASS", "FROZENCFG": "PASS", "STAMP": "PASS"}, work)

    # 2. clean landing: every leg passes
    _branch(lane, "main", olands)
    scenario("clean", lane, olands, freeze, 0,
             {n: "PASS" for n in REQUIRED_LEGS}, work,
             ("%s: PASS legs=%d/%d" % (VERDICT, len(REQUIRED_LEGS),
                                       len(REQUIRED_LEGS))),)

    # 3. graded junk landings — regeneration-equivalent to the receipt-named
    #    apparatus trees, but branched from the freeze so the ancestry rule
    #    grades them instead of refusing them
    _branch(lane, "gj01", freeze)
    _write(lane, GUARD_REL_DEFAULT,
           "#!/usr/bin/env python3\n"
           "print('LEDGER-GUARD-79: PASS pairs=4')\n")
    gj01 = _fixture_commit(lane, "graded J-01 stub guard")
    scenario("junk-J01", lane, gj01, freeze, 1, {"FROZENCFG": "FAIL"}, work)

    _branch(lane, "gj02", freeze)
    _write(lane, FIXTURES_REL_DEFAULT + "/green.json",
           json.dumps(_mut_observed_ledger(), indent=1) + "\n")
    gj02 = _fixture_commit(lane, "graded J-02 lying green fixture")
    scenario("junk-J02", lane, gj02, freeze, 1, {"GREEN": "FAIL"}, work)

    _branch(lane, "gj03", freeze)
    tamper_g = _mut_observed_ledger()
    for pair in tamper_g["pairs"]:
        if pair["id"] == "A02":
            pair["observed_at_base"] = "3"
    _write(lane, FIXTURES_REL_DEFAULT + "/mut-observed.json",
           json.dumps(tamper_g, indent=1) + "\n")
    gj03 = _fixture_commit(lane, "graded J-03 fixture tampered after freeze")
    scenario("junk-J03", lane, gj03, freeze, 1, {"FROZENCFG": "FAIL"}, work)

    _branch(lane, "gj04", freeze)
    _write(lane, GUARD_SELFTEST_RECEIPT_DEFAULT,
           "# guard sha256: %s\nSELFTEST: forged receipt\n" % ("0" * 64))
    gj04 = _fixture_commit(lane, "graded J-04 forged guard selftest receipt")
    scenario("junk-J04", lane, gj04, freeze, 1, {"SELFTEST": "FAIL"}, work)
    _branch(lane, "main", olands)

    # 4. a junk receipt typed without the run: expectation lines flipped
    _branch(lane, "junkreceipt", olands)
    forged = "\n".join(l.replace("exit=1", "exit=0")
                       .replace("LEG FAIL", "LEG PASS")
                       for l in junk_lines) + "\n"
    _write(lane, JUNK_RECEIPT_DEFAULT, forged)
    jrep = _fixture_commit(lane, "junk receipt forged to green")
    scenario("junk-receipt-forged", lane, jrep, freeze, 1,
             {"RECEIPTS": "FAIL"}, work)

    # 5. guard replaced by a stub at the graded tree (QUALITY 28 class)
    _branch(lane, "stub", olands)
    _write(lane, GUARD_REL_DEFAULT,
           "#!/usr/bin/env python3\nprint('LEDGER-GUARD-79: PASS pairs=4')\n")
    stub = _fixture_commit(lane, "guard swapped for a verdict-printing stub")
    code, states, _ = scenario("stub-guard", lane, stub, freeze, 1,
                               {"FROZENCFG": "FAIL"}, work)
    check("stub-guard ran red before any PASS",
          states.get("FROZENCFG") == "FAIL", str(states))

    ok = sum(1 for _l, good in results if good)
    print("SELFTEST: %d/%d scenarios ok" % (ok, len(results)))
    return 0 if ok == len(results) else 1


def main(argv=None):
    ap = argparse.ArgumentParser(
        description="round-79 claim O counter (ledger-token guard acceptance)")
    ap.add_argument("--root", default=".")
    ap.add_argument("--lands")
    ap.add_argument("--freeze")
    ap.add_argument("--main", default="main")
    ap.add_argument("--work",
                    help="scratch root: --work, else $HYAKU_SCRATCH, else "
                         "$TMPDIR; with none set the counter refuses instead "
                         "of inventing the system temp dir")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args(argv)
    if args.selftest:
        try:
            return selftest()
        except ScratchRefused as exc:
            print("SELFTEST: refused (%s)" % exc, file=sys.stderr)
            return 2
    if not args.lands or not args.freeze:
        print("ERROR: --lands <40hex> and --freeze <40hex> are required",
              file=sys.stderr)
        return 2
    return main_check(args.root, args.lands.lower(), args.freeze.lower(),
                      work=args.work, main_branch=args.main)


if __name__ == "__main__":
    sys.exit(main())
