#!/usr/bin/env python3
r"""Junk-landing fixture generator for the kotodama round-77 counters.

Purpose
-------
Make the round's acceptance surface *falsifiable*.  Each fixture materializes,
in a private clone under this round's scratch root, a git tree that differs
from a reference tree by exactly ONE named defect, and grades that tree with
the counter that owns the defect.  A correct counter must REFUSE the junk
landing; the fixture's `expected leg` names the leg that must go red, and the
receipt prints the whole leg table so a reviewer can see (a) the verdict,
(b) which legs are red, and (c) which legs the mutation *newly* reddens
relative to the unmutated reference tree.

Round token
-----------
The round is a CONFIGURATION value, not a rewrite: `--round N` defaults to the
round this file ships for (76) and the frozen `reports/round-<N>/claims.json`
must declare the same `round`.  Every path the generator names — claims,
ledger, evidence, telemetry, the lesson — and the verdict prefix it parses
(`ACCEPT-C-<N>` / `ACCEPT-CA-<N>`) derive from it, and the claim base is read
from the frozen claims.json rather than written here (QUALITY 25/26/28: a
counter's constants come from the freeze commit).  `--c-counter` /
`--ca-counter` point the grader at explicit counter paths, so the generator
can be run against an earlier round's counters to measure the red-before.

Reference tree
--------------
The generator is *landing-relative*: it clones the lane with
`git clone --shared`, checks out a reference revision (`--lands`, defaulting to
the freeze commit), applies the mutation, commits it in the clone only, and
grades the commit.  Nothing is ever written into the lane repository, its
index, or its git/jj state; the clone's `git rev-parse --show-toplevel` is
asserted to be the clone before any commit.

This matters for round 77: the freeze commit freezes claims.json, ledger.json,
both counters and the controls, but the *landing* (the claim-C rows, entries,
lesson, SCORECARD corrections and the REPAIR edits) lands later.  A junk
fixture is only attributable when the reference tree is otherwise green, so the
intended use is

    python3 -B reports/round-77/junk-fixtures.py --run \
        --freeze <freeze> --lands <landing-commit> --out-dir <dir>

Round-77 leg names
-------------------
The expected legs name the frozen round-77 tables, not the round-76 ones:
claim C is FROZENCFG, STAMP, LEDGELIST, COUNTS, ENTRIES, ROWS, APPENDONLY,
COLLCHECK, INDEX, EVIDENCE, GATE, REJECTS, CENSUS, GROUND, RECEIPTS; claim Ca
is LEDGER, BASEMISMATCH, REPAIR, ANNOTATE, APPENDONLY, R1EXEMPT, SEPARABLE,
COMBINED, RECEIPTS, FROZENCFG, STAMP, LEDGELIST.  A fixture's `expected_legs`
is therefore checked against the round-77 counter's own leg table, and the
`--round` token keeps the verdict prefix (`ACCEPT-C-77` / `ACCEPT-CA-77`) in
step with the frozen claims.

Scratch
-------
Every clone and temporary directory lives under `--work` / `--workroot`, else
`$HYAKU_SCRATCH/kotodama-r77/junk-fixtures`, else
`$TMPDIR/kotodama-r77-junk-fixtures`, else the operator's
`/fast/scratch/hyaku/kotodama-r77/junk-fixtures`; a root inside the system
temporary directory is refused (the round-75 routed defect, QUALITY 25).

When `--lands` is omitted the reference tree is the freeze commit itself; the
fixtures then still exercise the config / protected-file / ledger classes
(whose legs read frozen bytes), but the data legs are red for the trivial
reason that no landing exists, and the receipt's `newly-red` column is empty
for those legs.  The receipt always prints the baseline leg table next to the
mutant's so that distinction is never hidden.

FIXTURES (a correct counter REFUSES every one of them)

  J1   C   header-only stub entries at the frozen entry paths, with the
           matching registry rows' used-by naming the stubs (ENTRIES)
  J2   C   the Gate admit quote is absent from every stored evidence window
           while the window sha256 still recomputes (EVIDENCE; the lesson's
           Gate row can no longer bind its quote, so GATE is expected red too)
  J3   C   the graded tree's claims.json shrinks claim C to two rows and one
           entry (FROZENCFG)
  J4   Ca  the FREEZE's every observe_cmd is a literal constant printer of
           expected_after (LEDGER) — the fixture's own commit is the freeze,
           because LEDGER reads the freeze and a lands-only ledger edit can
           only ever reach FROZENCFG (round-75's measured lesson)
  J4b  Ca  the same, evasive: `python3 -c "import os;assert os.sep;print(str(...))"`
           — reads no clone byte but looks alive (LEDGER)
  J5   Ca  a `## Corrections — round <N>` row names only its id (ANNOTATE)
  J6   Ca  a frozen receipt outside every protected set is edited in place
           (APPENDONLY)
  J7   Ca  a byte in the Ca read set (a Corrections — round <N> row) cites a
           claim-C lane id, so the two claims are no longer separable
           (SEPARABLE)
  J8   Ca  a FREEZE pair's `stated_at` names a file outside the frozen
           stated_at allowlist while its stated_text is still present there
           (LEDGER) — the r76-routed L76-13 class, guarded pre-freeze
  J9   Ca  a FREEZE pair's `stated_text` is absent at its `stated_at` in the
           base tree (LEDGER) — the r76-routed L76-19 class
  J10  Ca  a FREEZE pair's observe_cmd is a `grep -E` argv whose pattern
           operand carries an escaped pipe and no pattern-operand mark
           (LEDGER) — the r76-routed unexecutable-argv class
  J11  C   NEGATIVE control: the reference landing with its frozen
           `required_sections[]` lines (the Paths and Search-log lines)
           removed.  ROWS must stay GREEN (it counts only `| S### |` lines
           inside the frozen row_set) and INDEX must go RED (the lines are
           required there) — the r76-routed "required non-row line counted as
           out-of-set" class

R1EXEMPT pair (the SOURCES rule-2 exemption, proved both ways)

  G    only a rule-2 cell edit (used-by) on one pre-existing row — the
       APPENDONLY leg must stay GREEN and every other leg must be unchanged
  R    only a non-rule-2 cell edit (teaches) on the same pre-existing row —
       the APPENDONLY leg must go RED and every other leg must be unchanged

  Their receipts are `r1exempt-green.txt` and `r1exempt-red.txt`.

LIBRARY API (stdlib only; the file name carries a hyphen, so import by path)

    import importlib.util, os
    HERE = os.path.dirname(os.path.abspath(__file__))
    spec = importlib.util.spec_from_file_location(
        "junk_fixtures", os.path.join(HERE, "junk-fixtures.py"))
    jf = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(jf)
    fx = jf.build("J3", freeze=<40hex>, lands=<40hex>,
                  workroot=jf.resolve_workroot())
    try:
        ...                            # grade fx.repo at fx.rev
    finally:
        jf.cleanup(fx)

Read-only outside the mktemp fixture repositories; stdlib only; no network.
"""

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from collections import namedtuple

# ---------------------------------------------------------------- constants ---

LANE = "/home/vgpnk/Projects/shokunin/kotodama-shokunin"
FLEET_ROOT = "/home/vgpnk/Projects/shokunin"
SCRATCH_PARENT = "/fast/scratch/hyaku"   # operator scratch tree (never /tmp)
ROUND = 77                               # the round this file ships for
PREV_LEGS = 12                           # previous accept-ca's leg count

RoundCfg = namedtuple("RoundCfg",
                      "round claims ledger evidence telemetry lesson "
                      "prev_lesson prev_receipt prev_counter")


def round_config(round_no):
    """Every round-derived path and token (QUALITY 25/26/28).

    The round is read from the frozen claims.json, never assumed: the
    claims/ledger/evidence/telemetry/lesson paths, the `## Corrections —
    round <N>` heading the ANNOTATE fixtures edit, the typed receipt's
    previous-round name and counter, and the `ACCEPT-C-<N>` / `ACCEPT-CA-<N>`
    verdict prefix all follow from it.
    """
    r = int(round_no)
    return RoundCfg(round=r,
                    claims="reports/round-%d/claims.json" % r,
                    ledger="reports/round-%d/ledger.json" % r,
                    evidence="reports/round-%d/evidence" % r,
                    telemetry="reports/round-%d/telemetry" % r,
                    lesson="corpus/lessons/round-%d.md" % r,
                    prev_lesson="corpus/lessons/round-%d.md" % (r - 1),
                    prev_receipt="accept-ca-%d-at-lands.txt" % (r - 1),
                    prev_counter="reports/round-%d/accept-ca.py" % (r - 1))


CFG = round_config(ROUND)
REGISTRY = "corpus/SOURCES.md"
SCORECARD = "SCORECARD.md"

# The counter bytes the L1 installs at the freeze commit; the wave copy is the
# fallback (a counter may live at either path).  They follow the configured
# round, so a `--round 75` run looks for the round-75 counters.
def c_counter_candidates(round_no=None):
    r = int(round_no if round_no is not None else CFG.round)
    return ("reports/round-%d/accept-c.py" % r,
            ".ufo/waves/round-%d/counters/accept-c.py" % r)


def ca_counter_candidates(round_no=None):
    r = int(round_no if round_no is not None else CFG.round)
    return ("reports/round-%d/accept-ca.py" % r,
            ".ufo/waves/round-%d/counters/accept-ca.py" % r)


def protected_set(round_no=None):
    """The frozen Ca APPENDONLY protected set (append-only files).

    J6 picks a receipt *outside* it.  The set is derived from the round rather
    than hardcoded: the two previous rounds' lessons, the round's own
    log/scorecard/QUALITY/SHONEN records and the two previous rounds' frozen
    configs.
    """
    r = int(round_no if round_no is not None else CFG.round)
    return (
        "LOG.md",
        "SCORECARD.md",
        "corpus/lessons/round-%d.md" % (r - 1),
        "corpus/lessons/round-%d.md" % (r - 2),
        "corpus/QUALITY.md",
        "SHONEN.md",
        "reports/round-%d/claims.json" % (r - 1),
        "reports/round-%d/ledger.json" % (r - 1),
        "reports/round-%d/claims.json" % (r - 2),
        "reports/round-%d/ledger.json" % (r - 2),
    )


def stated_at_allowlist(round_no=None):
    """The frozen ANNOTATE `stated_at` allowlist (r77 routed defect r76 #3).

    Round 77 freezes the allowlist rather than deriving it per pair: the round's
    log, its scorecard, and the two previous rounds' lessons are append-only
    targets; `corpus/README.md` is REPAIR-only and therefore NOT in this set.
    J8 moves a pair's `stated_at` to a file outside it.
    """
    r = int(round_no if round_no is not None else CFG.round)
    return (
        "LOG.md",
        "SCORECARD.md",
        "corpus/lessons/round-%d.md" % (r - 2),
        "corpus/lessons/round-%d.md" % (r - 1),
    )


# The frozen observe-argv executable allowlist (round-77 claim Ca, "rederive
# strings must be argv-executable").  J10 reaches the clause that r76 lacked:
# a grep -E pattern *operand* carrying an escaped pipe or a backtick, which the
# r76 guard skipped wholesale.
OBSERVE_ALLOW = ("git", "grep", "wc", "sha256sum", "ls", "cat", "head", "tail",
                 "cut")
PATTERN_META = ("|", "\\|", "`")
PATTERN_MARK_KEYS = ("pattern_operand", "pattern-operand", "pattern_operand_ok")


def pattern_operand_marked(pair):
    """True when a pair marks its grep operand as a deliberate pattern."""
    return any(bool(pair.get(k)) for k in PATTERN_MARK_KEYS)


def grep_pattern_operands(argv):
    """The argv indices grep treats as its pattern operand."""
    out = set()
    if not isinstance(argv, list) or not argv or argv[0] != "grep":
        return out
    i, have = 1, False
    while i < len(argv):
        a = argv[i]
        if a == "--":
            break
        if a.startswith("-") and len(a) > 1:
            if a in ("-e", "--regexp"):
                if i + 1 < len(argv):
                    out.add(i + 1)
                    have = True
                i += 2
                continue
            if a in ("-f", "--file"):
                i += 2
                continue
            i += 1
            continue
        if not have:
            out.add(i)
            have = True
        i += 1
    return out


def pattern_operand_defect(argv, pair):
    """The r77 clause: an unmarked pattern operand holding `|`/`\\|`/backtick."""
    if pattern_operand_marked(pair):
        return None
    for idx in sorted(grep_pattern_operands(argv)):
        operand = argv[idx]
        for bad in PATTERN_META:
            if bad in operand:
                return ("grep pattern operand %r carries %r and the pair is "
                        "not marked pattern-operand" % (operand[:60], bad))
    return None


def required_sections(claims_doc):
    """The frozen `required_sections[]` of claim C (round 77)."""
    claim = _claims(claims_doc, "C")
    out = []
    for item in claim.get("required_sections") or []:
        if isinstance(item, dict) and item.get("path"):
            out.append(item)
        elif isinstance(item, str) and item.strip():
            out.append({"path": REGISTRY, "section": item.strip()})
    return out


def _section_span(lines, heading):
    """(start, end) line indexes of a `## <heading>` section, or (None, None)."""
    want = heading.lstrip("#").strip().lower()
    start = None
    for i, line in enumerate(lines):
        if start is None:
            m = re.match(r"^##\s+(.*\S)\s*$", line)
            if m and m.group(1).strip().lower() == want:
                start = i + 1
            continue
        if re.match(r"^##\s", line):
            return start, i
    return (start, len(lines)) if start is not None else (None, None)


def _required_line(repo, item):
    """Locate the line `item` enumerates: (path, line index, text)."""
    path = item["path"]
    text = read(repo, path)
    lines = text.splitlines(keepends=True)
    needle = item.get("match") or item.get("contains") or item.get("line")
    if needle:
        for i, line in enumerate(lines):
            if needle in line:
                return path, i, line
        raise FixtureError("%s carries no line matching %r"
                           % (path, needle))
    heading = item.get("section")
    if not heading:
        raise FixtureError("required_sections entry %r names neither a match "
                           "nor a section" % (item,))
    start, end = _section_span(lines, heading)
    if start is None:
        raise FixtureError("%s carries no `## %s` section" % (path, heading))
    for i in range(start, end):
        if lines[i].strip() and not ROW_RE.match(lines[i]):
            return path, i, lines[i]
    raise FixtureError("%s `## %s` holds no removable line" % (path, heading))


# Frozen receipts that exist in the tree and are outside the protected set;
# J6 edits the first one that is present, then falls back to the oldest
# telemetry receipt it can find in the tree.
J6_CANDIDATES = (
    "reports/round-75/telemetry/measures-ca.txt",
    "reports/round-75/telemetry/measures-c.txt",
    "reports/round-75/telemetry/accept-ca-74-at-lands.txt",
    "reports/round-74/telemetry/measures-ca.txt",
)

CORR_HEADING_RE = re.compile(r"^##\s+Corrections\s*[—–-]\s*round\s+(\d+)\b",
                             re.I | re.M)
ROW_RE = re.compile(r"^\s{0,3}\|\s*(S\d{3,})\s*\|")
ACCEPT_RE = re.compile(r"^ACCEPT-(C|CA)-(\d+): (PASS|FAIL) legs=(\d+)/(\d+)",
                       re.M)
LEG_RE = re.compile(r"^LEG (PASS|FAIL) (\w+)", re.M)


def leg_table(text):
    """{leg name: passed?} from a counter's `LEG PASS|FAIL <name>` lines.

    The verdict word is compared against "PASS" — a substring test would read
    the string "FAIL" as truthy and call every leg green.
    """
    return {name: (verdict == "PASS") for verdict, name in LEG_RE.findall(text)}

COMMIT_ID = ("junk-fixtures", "junk@fixture.invalid")
CLONE_TIMEOUT = 600
COUNTER_TIMEOUT = 1800

# The filler J2 writes over a Gate quote inside a stored evidence window.
# It must not be whitespace: the counter's EVIDENCE leg skips the quote check
# on a window whose `.strip()` is empty, so a blank filler would make the
# junk landing pass for the wrong reason.
JUNK_FILLER = "\u2588"

Fixture = namedtuple("Fixture",
                     "name claim repo rev expected expected_legs paths detail "
                     "freeze lands base cell must_pass seeded")


class FixtureError(Exception):
    """A fixture could not be materialized."""


# ---------------------------------------------------------------- git plumbing ---

def _run(cmd, cwd=None, timeout=CLONE_TIMEOUT):
    return subprocess.run(cmd, cwd=cwd, capture_output=True, text=True,
                          timeout=timeout)


def git(repo, *args, timeout=CLONE_TIMEOUT):
    """git in `repo` only (every call names -C, the mktemp rule)."""
    r = _run(["git", "-C", repo, *args], timeout=timeout)
    if r.returncode != 0:
        raise FixtureError("git -C %s %s failed: %s"
                           % (repo, " ".join(args), r.stderr.strip()))
    return r.stdout


def commit_all(repo, msg, allow_empty=False):
    """Stage everything in `repo` and commit with the throwaway identity."""
    git(repo, "add", "-A")
    cmd = ["git", "-C", repo,
           "-c", "user.name=%s" % COMMIT_ID[0],
           "-c", "user.email=%s" % COMMIT_ID[1],
           "commit", "-q"]
    if allow_empty:
        cmd.append("--allow-empty")
    cmd += ["-m", msg]
    r = _run(cmd)
    if r.returncode != 0:
        raise FixtureError("fixture commit %r failed in %s: %s"
                           % (msg, repo, r.stderr.strip()))
    return git(repo, "rev-parse", "HEAD").strip()


def _forbidden_scratch(path):
    """True when `path` is (inside) the system temporary directory.

    The round-75 routed defect was a counter writing under a literal system
    temp root; this generator refuses such a root rather than verifying after
    the fact.  The banned root is whatever `tempfile.gettempdir()` resolves
    (which honours `$TMPDIR`), so no temp path is spelled here.
    """
    p = os.path.abspath(path)
    b = os.path.abspath(tempfile.gettempdir())
    return p == b or p.startswith(b + os.sep)


def resolve_workroot(explicit=None, round_no=None):
    """The scratch root every clone and temp dir lives under.

    `--work` / `--workroot` wins; then `$HYAKU_SCRATCH/kotodama-r<NN>/
    junk-fixtures`; then `$TMPDIR/kotodama-r<NN>-junk-fixtures`; then the
    operator's `/fast/scratch/hyaku/kotodama-r<NN>/junk-fixtures`.  A
    system-temporary root is refused (QUALITY 25 routed defect); there is no
    silent system-temp fallback.
    """
    r = int(round_no if round_no is not None else CFG.round)
    if explicit and str(explicit).strip():
        root = os.path.abspath(str(explicit).strip())
    else:
        env = (os.environ.get("HYAKU_SCRATCH") or "").strip()
        tmp = (os.environ.get("TMPDIR") or "").strip()
        if env:
            root = os.path.join(os.path.abspath(env),
                                "kotodama-r%d" % r, "junk-fixtures")
        elif tmp:
            root = os.path.join(os.path.abspath(tmp),
                                "kotodama-r%d-junk-fixtures" % r)
        elif os.path.isdir(SCRATCH_PARENT) and os.access(SCRATCH_PARENT, os.W_OK):
            root = os.path.join(SCRATCH_PARENT,
                                "kotodama-r%d" % r, "junk-fixtures")
        else:
            raise FixtureError(
                "no scratch root: pass --work <dir> or set $HYAKU_SCRATCH "
                "(refusing to fall back to the system temporary directory)")
    if _forbidden_scratch(root):
        raise FixtureError("scratch root %s is inside the system temporary "
                           "directory; pass --work under the operator scratch "
                           "tree instead" % root)
    return root


def clone_lane(workroot, label):
    """A private clone of the lane repo under a fresh mktemp directory.

    `git clone --shared` borrows the lane's objects through an alternates
    file (no mirror copy, no hardlinked object store), and `--no-checkout`
    leaves the worktree empty until the reference revision is materialized.
    Returns (dir, repo).  The clone keeps the lane's history but its own refs
    and index; `git rev-parse --show-toplevel` is verified to be the clone
    before any commit, so no fixture commit can land anywhere else.
    """
    workroot = resolve_workroot(workroot) if not workroot else workroot
    os.makedirs(workroot, exist_ok=True)
    d = tempfile.mkdtemp(prefix="jf-%s-" % label, dir=workroot)
    repo = os.path.join(d, "repo")
    r = _run(["git", "clone", "-q", "--shared", "--no-checkout", LANE, repo])
    if r.returncode != 0:
        shutil.rmtree(d, ignore_errors=True)
        raise FixtureError("shared clone of lane failed: %s" % r.stderr.strip())
    top = git(repo, "rev-parse", "--show-toplevel").strip()
    if os.path.realpath(top) != os.path.realpath(repo):
        raise FixtureError("clone toplevel %r != %r (refusing to commit)"
                           % (top, repo))
    return d, repo


def cleanup(fixture):
    """Remove the fixture's mktemp directory (the repo lives inside it)."""
    shutil.rmtree(os.path.dirname(fixture.repo), ignore_errors=True)


# ---------------------------------------------------------------- text edits ---

def read(repo, rel):
    with open(os.path.join(repo, rel), encoding="utf-8") as fh:
        return fh.read()


def write(repo, rel, text):
    path = os.path.join(repo, rel)
    os.makedirs(os.path.dirname(path) or repo, exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)


def read_json(repo, rel):
    return json.loads(read(repo, rel))


def write_json(repo, rel, doc):
    write(repo, rel, json.dumps(doc, ensure_ascii=False, indent=1) + "\n")


def git_show(repo, rev, rel):
    r = _run(["git", "-C", repo, "show", "%s:%s" % (rev, rel)])
    if r.returncode != 0:
        raise FixtureError("git show %s:%s failed: %s"
                           % (rev[:12], rel, r.stderr.strip()))
    return r.stdout


def replace_text(text, old, new, path="<text>"):
    n = text.count(old)
    if n != 1:
        raise FixtureError("%s: expected exactly one %r, found %d"
                           % (path, old, n))
    return text.replace(old, new)


def split_cells(line):
    """Split a registry row into cells, honouring escaped pipes (`\\|`)."""
    cells, cur, i = [], [], 0
    while i < len(line):
        ch = line[i]
        if ch == "\\" and i + 1 < len(line) and line[i + 1] == "|":
            cur.append("\\|")
            i += 2
            continue
        if ch == "|":
            cells.append("".join(cur))
            cur = []
            i += 1
            continue
        cur.append(ch)
        i += 1
    cells.append("".join(cur))
    return cells


def set_cell(line, index, value):
    """Return `line` with cell `index` (0 = the empty left margin) rewritten."""
    cells = split_cells(line)
    if index >= len(cells) - 1:
        raise FixtureError("row has %d cells, no index %d: %r"
                           % (len(cells) - 2, line[:90]))
    cells[index] = " %s " % value
    return "|".join(cells)


def registry_columns(repo, rel=REGISTRY):
    """{column name: cell index} from the registry table header."""
    for line in read(repo, rel).splitlines():
        if not line.lstrip().startswith("|"):
            continue
        cells = [c.strip() for c in split_cells(line)]
        if cells and cells[1] == "id":
            return {name: i for i, name in enumerate(cells) if name}
    raise FixtureError("%s carries no registry table header" % rel)


def registry_row(repo, rid, rel=REGISTRY):
    for line in read(repo, rel).splitlines():
        m = ROW_RE.match(line)
        if m and m.group(1) == rid:
            return line
    raise FixtureError("%s carries no row %s" % (rel, rid))


def row_ids(text):
    """{S-id: line} for registry rows."""
    out = {}
    for line in text.splitlines():
        m = ROW_RE.match(line)
        if m:
            out[m.group(1)] = line
    return out


def sanitize_cell(text):
    """A cell value with every pipe neutralised (no literal pipe in a cell)."""
    return re.sub(r"\s+", " ", text.replace("|", "/")).strip()


def rewrite_ledger_observe(doc, mode):
    """Replace every pair's observe_cmd with a constant printer of
    expected_after.

    mode "literal"  -> `python3 -c "print('X')"` on even pairs, `echo X` on odd
    mode "evasive"  -> `python3 -c "import os;assert os.sep;print(str('X'))"`,
                        which reads no clone byte but looks less obviously
                        constant
    mode "shell"    -> one argv string with shell metacharacters
    """
    if mode not in ("literal", "evasive", "shell"):
        raise FixtureError("unknown constant-printer mode %r" % mode)
    for i, pair in enumerate(doc.get("pairs") or []):
        exp = pair.get("expected_after")
        if not isinstance(exp, str):
            raise FixtureError("pair %r has no expected_after" % pair.get("id"))
        literal = json.dumps(exp)
        if mode == "evasive":
            pair["observe_cmd"] = ["python3", "-c",
                                   "import os;assert os.sep;print(str(%s))"
                                   % literal]
        elif mode == "shell":
            # One argv element that is a whole shell pipeline: the executable
            # is not on the read-only allowlist and the string carries shell
            # metacharacters, so a counter that splits argv and allowlists
            # argv[0] must refuse it.
            pair["observe_cmd"] = [
                "git grep -c -E '^. S[0-9]{3}' HEAD -- corpus/SOURCES.md "
                "| tail -1"]
        elif i % 2:
            pair["observe_cmd"] = ["echo", exp]
        else:
            pair["observe_cmd"] = ["python3", "-c", "print(%s)" % literal]
    return doc


def stub_correction_row(text, pid):
    """Replace the correction row whose first cell is `pid` with `| pid |`."""
    pattern = re.compile(r"^\|\s*%s\s*\|.*$" % re.escape(pid), re.M)
    matches = pattern.findall(text)
    if len(matches) != 1:
        raise FixtureError("expected one correction row for %s, found %d"
                           % (pid, len(matches)))
    return pattern.sub("| %s |" % pid, text)


def corrections_section_bounds(text, round_no):
    """(start, end) line indexes of the `## Corrections — round N` section."""
    lines = text.splitlines(keepends=True)
    start = None
    for i, line in enumerate(lines):
        if start is None:
            m = CORR_HEADING_RE.match(line)
            if m and int(m.group(1)) == round_no:
                start = i
            continue
        if re.match(r"^##\s", line):
            return start, i
    if start is None:
        return None, None
    return start, len(lines)


def append_correction_row(text, round_no, row):
    """Append `row` to the `## Corrections — round N` section (creating the
    section when it does not exist).  The section is append-only: the row is
    added after the last table row, never inside an existing row."""
    lines = text.splitlines(keepends=True)
    start, end = corrections_section_bounds(text, round_no)
    if start is None:
        block = ("\n## Corrections — round %d\n\n"
                 "| id | old token | new token | re-derivation command | note |\n"
                 "|---|---|---|---|---|\n" % round_no)
        return text.rstrip("\n") + "\n" + block + row.rstrip("\n") + "\n"
    last = end - 1
    while last > start and not lines[last].strip():
        last -= 1
    lines.insert(last + 1, row.rstrip("\n") + "\n")
    return "".join(lines)


def gate_quotes(text):
    """The quoted spans of the `## Gate` section's admitted rows."""
    lines = text.splitlines()
    start = None
    for i, line in enumerate(lines):
        if start is None:
            if re.match(r"^##\s+Gate\b", line):
                start = i + 1
            continue
        if re.match(r"^##\s", line):
            break
        low = line.lower()
        if "admitted" not in low and "admit" not in low:
            continue
        for m in re.finditer(r'"([^"\n]{4,})"|“([^“”\n]{4,})”|«([^»»\n]{4,})»',
                             line):
            span = next(g for g in m.groups() if g)
            if span.strip():
                yield span.strip()


def gate_section(text):
    """The `## Gate` section's table rows (each a list of cells).

    A text that carries no `## Gate` heading is read as a bare table, so the
    helper is usable on a section body as well as on a whole lesson.
    """
    lines = text.splitlines()
    start = None
    for i, line in enumerate(lines):
        if re.match(r"^##\s+Gate\b", line):
            start = i + 1
            break
    if start is None:
        start = 0
    else:
        for i in range(start, len(lines)):
            if re.match(r"^##\s", lines[i]):
                lines = lines[:i]
                break
    for line in lines[start:]:
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in line.split("|")]
        if len(cells) > 2 and cells[1].lower() not in ("id", "---"):
            yield cells
    return


def row_quotes(text, rid):
    """The quoted spans of the Gate row that pairs with the registry row
    `rid` — the counter pairs a Gate admit row to a row by the id or the URL
    the row's source names, so the fixture pairs them the same way."""
    url = None
    for cells in gate_section(text):
        blob = " ".join(cells)
        if rid and re.search(r"(?<![0-9A-Za-z_])%s(?![0-9A-Za-z_])"
                             % re.escape(rid), blob):
            url = url or blob
            spans = [s for s in re.findall(
                r'"([^"\n]{4,})"|“([^“”\n]{4,})”|«([^»»\n]{4,})»', blob)
                for s in s if s]
            spans = [s.strip() for s in spans if s.strip()]
            if spans and "admit" in blob.lower():
                return spans
    return []


def nfkc_ws(text):
    """The counter's fold: NFKC per character, then whitespace folded away."""
    import unicodedata
    return "".join(unicodedata.normalize("NFKC", c) for c in (text or "")
                   if not c.isspace())


# ------------------------------------------------------------------ fixtures ---

def _claims(doc, cid):
    want = cid.strip().upper()
    for claim in doc.get("claims") or []:
        if isinstance(claim, dict) and \
                str(claim.get("id", "")).strip().upper() == want:
            return claim
    raise FixtureError("claims.json carries no claim %s" % cid)


def _round_of(claims_doc):
    """The round the frozen claims declare (the configured round is only the
    default for a claims file that omits it)."""
    return int(claims_doc.get("round") or CFG.round)


def _adopted_ids(claims_doc):
    claim = _claims(claims_doc, "C")
    ids = []
    for row in claim.get("row_set") or []:
        rid = row.get("id") if isinstance(row, dict) else row
        if rid:
            ids.append(rid)
    return ids


def _entry_paths(claims_doc):
    claim = _claims(claims_doc, "C")
    return [p for p in (claim.get("entries") or []) if p]


def _stub_entry(repo, path, rid, url):
    """A header-only stub entry: complete provenance header, no body.

    The header names exactly one adopted row, so the matching registry row's
    used-by cell can name this stub path and the pair still matches.
    """
    lines = ["# %s" % os.path.basename(path), ""]
    lines.append("- source: %s — %s" % (rid, url))
    lines += [
        "- verified-at: 2026-10-27",
        "- recheck: 180d — re-open the cited row and re-locate its quoted span",
        "- ground: junk fixture ground line; the entry body was never mined",
        "- gap filled: junk fixture gap line; no prose beyond this header exists",
        "- topic: junk fixture topic line standing in for a mined topic",
        "- sources: the row above, left unmined by this fixture",
        "- couples: `myth-symbol/comparative-frameworks.md`",
        "- scope: a fixture stub; it decides no world's story and adds no canon",
    ]
    write(repo, path, "\n".join(lines) + "\n")


def junk_J1(repo, ctx):
    """A header-only stub entry at the frozen entry path, with the matching
    registry row's used-by naming the stub (ENTRIES).

    Round 77 adopts ONE entry, so the round-76 shape (two stubs) is wrong here:
    the fixture stubs the single frozen entry and points its row's used-by at
    it, which is the strongest form of the defect the ENTRIES leg exists to
    refuse (a complete provenance header, no mined body).
    """
    claims = ctx["claims"]
    entries = _entry_paths(claims)
    if not entries:
        raise FixtureError("claim C names no entry path")
    ids = _adopted_ids(claims)
    if not ids:
        raise FixtureError("claim C names no adopted row")
    path, rid = entries[0], ids[0]
    urls = {}
    for row in _claims(claims, "C").get("row_set") or []:
        if isinstance(row, dict) and row.get("id"):
            urls[row["id"]] = row.get("document") or ""
    _stub_entry(repo, path, rid, urls.get(rid) or
                "https://example.invalid/%s" % rid)
    # The matching registry row must point its used-by at the stub path.
    cols = registry_columns(repo)
    text = read(repo, REGISTRY)
    out = []
    touched = 0
    for line in text.splitlines(keepends=True):
        m = ROW_RE.match(line)
        if m and m.group(1) == rid:
            line = set_cell(line.rstrip("\n"), cols["used-by"],
                            sanitize_cell(path)) + "\n"
            touched += 1
        out.append(line)
    if touched == 0:
        raise FixtureError("no registry row %s in the tree (the stub entry "
                           "cannot be paired with a row)" % rid)
    write(repo, REGISTRY, "".join(out))
    ctx["detail"] = ("stub entry %s (header only, no body); used-by of %s "
                     "rewritten to the stub path" % (path, rid))


def _evidence_files(repo, ids):
    out = []
    for rid in ids:
        rel = "%s/%s.txt" % (CFG.evidence, rid)
        if os.path.isfile(os.path.join(repo, rel)):
            out.append((rid, rel))
    return out


def _evidence_window(text):
    """(window_line, start_index, stop_index) of an evidence file's stored
    window, or None when the file carries no window block."""
    lines = text.splitlines()
    try:
        start = lines.index("--- window ---")
        stop = lines.index("--- quote ---")
    except ValueError:
        return None
    if stop <= start + 1:
        return None
    return lines[start + 1], start, stop


def junk_J2(repo, ctx):
    """The Gate admit quote is absent from every stored evidence window while
    the window's own scope, length and digest still hold (EVIDENCE).

    The mutation is surgical on purpose: the window keeps its exact character
    count (so the `excerpt` >= 4096 rule and the `whole-document` ==
    visible-chars rule both still hold) and its `window-sha256:` /
    `window-bytes:` are recomputed from the bytes the file stores, so the
    ONLY sub-check that can fail is the one this fixture names: the Gate
    quote is no longer in the window.
    """
    ids = _adopted_ids(ctx["claims"])
    files = _evidence_files(repo, ids)
    if not files:
        raise FixtureError("no evidence file for the adopted rows %s" % ids)
    try:
        lesson = read(repo, CFG.lesson)
    except OSError:
        lesson = ""
    touched = 0
    removed = []
    for rid, rel in files:
        text = read(repo, rel)
        found = _evidence_window(text)
        if found is None:
            raise FixtureError("%s carries no --- window --- block" % rel)
        window, start, stop = found
        quotes = row_quotes(lesson, rid)
        new_window = None
        for quote in quotes:
            if nfkc_ws(quote) not in nfkc_ws(window):
                continue
            # Replace the quote's own characters with neutral filler, keeping
            # the window's character count identical.  The filler is NOT
            # whitespace: a counter that guards `if not window.strip():
            # continue` SKIPS the quote check on a blank window, so a blank
            # filler would let the junk landing pass for the wrong reason.
            candidate = window.replace(quote, JUNK_FILLER * len(quote))
            if nfkc_ws(quote) not in nfkc_ws(candidate):
                new_window = candidate
                removed.append((rid, quote))
                break
        if new_window is None:
            # The quote is not in this window verbatim (it matches only after
            # folding), or no Gate quote is paired with it yet: blank the whole
            # window with same-length filler so the length rules still hold.
            new_window = (JUNK_FILLER * len(window))[:len(window)]
        lines = text.splitlines()
        lines[start + 1:stop] = [new_window]
        text = "\n".join(lines) + "\n"
        payload = new_window.encode("utf-8")
        text = re.sub(r"^window-sha256: .*$",
                      "window-sha256: %s"
                      % hashlib.sha256(payload).hexdigest(),
                      text, flags=re.M)
        text = re.sub(r"^window-bytes: .*$",
                      "window-bytes: %d" % len(payload), text, flags=re.M)
        write(repo, rel, text)
        touched += 1
    ctx["detail"] = ("the Gate quote removed from the stored window of %d "
                     "evidence file(s) (%s); each window keeps its character "
                     "count and its window-sha256/window-bytes are recomputed, "
                     "so the only failing sub-check is the quote's absence"
                     % (touched,
                        ", ".join("%s:%r" % (r, q[:24]) for r, q in removed)
                        or "no row was paired verbatim"))


def junk_J3(repo, ctx):
    """The graded tree's claims.json shrinks claim C (FROZENCFG).

    The shrink drops the LAST frozen row, and the last entry when the claim
    carries more than one.  Round 77 adopts exactly one entry and two rows, so
    a fixed "keep two rows and one entry" truncation would be a no-op on the
    real freeze — the mutation is stated as a delta, never as an absolute
    shape, and `build()` refuses a fixture whose only delta is the seeded
    config.
    """
    doc = read_json(repo, CFG.claims)
    claim = _claims(doc, "C")
    rows = [r for r in (claim.get("row_set") or []) if isinstance(r, dict)]
    if len(rows) < 2:
        raise FixtureError("claim C carries %d row(s); the shrink needs at "
                           "least two" % len(rows))
    claim["row_set"] = rows[:-1]
    entries = list(claim.get("entries") or [])
    if len(entries) > 1:
        claim["entries"] = entries[:-1]
    write_json(repo, CFG.claims, doc)
    ctx["detail"] = ("graded-tree claims.json shrinks claim C to %d row(s) "
                     "(%s) and %d entr%s"
                     % (len(claim["row_set"]),
                        ", ".join(r.get("id", "?") for r in claim["row_set"]),
                        len(claim.get("entries") or []),
                        "y" if len(claim.get("entries") or []) == 1 else "ies"))


def junk_J4(repo, ctx):
    """The FROZEN ledger's every observe_cmd constant-prints expected_after.

    The LEDGER leg reads its contract from the freeze (`git show
    <freeze>:reports/round-77/ledger.json`), so a lands-only ledger edit can
    only ever surface as a FROZENCFG byte difference and never reaches the
    argv clause.  The fixture therefore commits the defective ledger as its
    OWN freeze (round-75's measured J4f lesson, carried into round 77).
    """
    doc = read_json(repo, CFG.ledger)
    write_json(repo, CFG.ledger, rewrite_ledger_observe(doc, "literal"))
    ctx["detail"] = ("the frozen ledger's every observe_cmd is a literal "
                     "constant printer of expected_after (python3 -c print / "
                     "echo)")
    ctx["own_freeze"] = True


def junk_J4b(repo, ctx):
    """The evasive constant printer: reads no clone byte, looks alive."""
    doc = read_json(repo, CFG.ledger)
    write_json(repo, CFG.ledger, rewrite_ledger_observe(doc, "evasive"))
    ctx["detail"] = ("the frozen ledger's every observe_cmd is the evasive "
                     "constant printer (import os;assert os.sep;"
                     "print(str(...)))")
    ctx["own_freeze"] = True


def _annotate_pairs(ctx):
    """The frozen ledger's ANNOTATE pairs (the rows a correction must name)."""
    return [p for p in (ctx["ledger"].get("pairs") or [])
            if p.get("disposition") == "ANNOTATE"]


def _section_text(text, round_no):
    """The text of the `## Corrections — round N` section (heading included)."""
    lines = text.splitlines(keepends=True)
    start = None
    for i, line in enumerate(lines):
        m = CORR_HEADING_RE.match(line)
        if m and int(m.group(1)) == round_no:
            start = i
            break
    if start is None:
        return None
    end = len(lines)
    for i in range(start + 1, len(lines)):
        if re.match(r"^##\s", lines[i]):
            end = i
            break
    return "".join(lines[start:end])


def junk_J5(repo, ctx):
    """A `## Corrections — round <N>` row names only its id."""
    pairs = _annotate_pairs(ctx)
    if not pairs:
        raise FixtureError("the frozen ledger carries no ANNOTATE pair")
    pid = pairs[0].get("id")
    round_no = _round_of(ctx["claims"])
    text = read(repo, SCORECARD)
    section = _section_text(text, round_no)
    if section is None:
        raise FixtureError("SCORECARD carries no `## Corrections — round %d` "
                           "section" % round_no)
    if not re.search(r"^\|\s*%s\s*\|" % re.escape(pid), section, re.M):
        raise FixtureError("the round-%d corrections section carries no row "
                           "for the ANNOTATE pair %s" % (round_no, pid))
    write(repo, SCORECARD, stub_correction_row(text, pid))
    ctx["detail"] = ("the Corrections — round %d row for %s reduced to "
                     "`| %s |` (id only: no old token, no observed token, no "
                     "re-derivation command)" % (round_no, pid, pid))


def _j6_receipts(repo, stated):
    """Unprotected frozen receipts present in the tree, most preferred first.

    The static list names older rounds' receipts; the fallback scans the
    older rounds' telemetry directories so a tree that has moved on still
    yields a receipt outside the protected set (never one a pair states, and
    never one the round's own RECEIPTS leg grades).
    """
    protected = set(protected_set())
    pinned = {CFG.prev_receipt}
    out = []
    for cand in J6_CANDIDATES:
        if cand in protected or cand in stated:
            continue
        if os.path.isfile(os.path.join(repo, cand)):
            out.append(cand)
    for r in sorted({CFG.round - 2, CFG.round - 3}, reverse=True):
        d = "reports/round-%d/telemetry" % r
        full = os.path.join(repo, d)
        if not os.path.isdir(full):
            continue
        for name in sorted(os.listdir(full)):
            rel = "%s/%s" % (d, name)
            if not name.endswith(".txt") or os.path.basename(rel) in pinned:
                continue
            if rel in protected or rel in stated or rel in out:
                continue
            out.append(rel)
    return out


def junk_J6(repo, ctx):
    """A frozen receipt outside every protected set is edited in place."""
    stated = {p.get("stated_at") for p in (ctx["ledger"].get("pairs") or [])}
    rel = None
    for cand in _j6_receipts(repo, stated):
        text = read(repo, cand)
        if re.search(r"legs=(\d+)/(\d+)", text):
            rel = cand
            break
    if rel is None:
        raise FixtureError("no unprotected frozen receipt found in the tree")
    text = read(repo, rel)
    m = re.search(r"legs=(\d+)/(\d+)", text)
    old = m.group(0)
    new = "legs=%s/%s" % (m.group(1), int(m.group(2)) + 1)
    write(repo, rel, replace_text(text, old, new, rel))
    ctx["detail"] = ("in-place edit of the frozen receipt %s (%s -> %s); the "
                     "file is outside the protected set" % (rel, old, new))


def junk_J7(repo, ctx):
    """A byte in the Ca read set cites a claim-C lane id (SEPARABLE)."""
    adopted = _adopted_ids(ctx["claims"])
    if not adopted:
        raise FixtureError("claim C carries no row_set")
    lane_id = adopted[0]
    pairs = _annotate_pairs(ctx)
    if not pairs:
        raise FixtureError("the frozen ledger carries no ANNOTATE pair")
    pid = pairs[0].get("id")
    round_no = _round_of(ctx["claims"])
    row = ("| %s | %s | %s | %s | the round-%d registry row %s is claim C's |"
           % (pid,
              sanitize_cell(str(pairs[0].get("stated_text") or "")),
              sanitize_cell(str(pairs[0].get("expected_after") or "")),
              sanitize_cell(str(pairs[0].get("rederive") or "")),
              round_no, lane_id))
    text = read(repo, SCORECARD)
    write(repo, SCORECARD, append_correction_row(text, round_no, row))
    ctx["detail"] = ("a Corrections — round %d row naming %s now cites the "
                     "claim-C lane id %s, so the Ca read set names a C row and "
                     "the claims stop being separable" % (round_no, pid, lane_id))


def _rule2_row_id(repo, ctx):
    """A pre-existing registry row (not adopted this round)."""
    adopted = set(_adopted_ids(ctx["claims"]))
    ids = sorted(row_ids(read(repo, REGISTRY)))
    for rid in ids:
        if rid not in adopted:
            return rid
    raise FixtureError("no pre-existing registry row to edit")


# --------------------------------------------------- the round-77 J8..J10 ---
#
# The three ledger-shape classes the round-77 claim names as routed defects
# from round 76.  All three mutate the ledger the counter FREEZE-PINS, so the
# fixture's own commit is the freeze and the LEDGER leg reads the defective
# pair directly (a lands-only edit reaches FROZENCFG and nothing else).

def _stated_path(pair):
    return str(pair.get("stated_at") or "").rsplit(":", 1)[0]


def _first_pair(ctx, pred):
    for pair in ctx["ledger"].get("pairs") or []:
        if isinstance(pair, dict) and pred(pair):
            return pair
    raise FixtureError("the frozen ledger carries no pair matching the "
                       "fixture's precondition")


OUTSIDE_SITE = "corpus/lessons/round-%d.md"   # outside the frozen allowlist


def junk_J8(repo, ctx):
    """A FREEZE pair's stated_at names a file outside the allowlist.

    The pair's stated_text is written verbatim as a new line of
    `corpus/lessons/round-74.md` (outside the round-77 allowlist, outside the
    protected set) and `stated_at` is pointed at that line, so the presence
    clause still holds and the ONLY sub-check that can fail is the allowlist
    (round-76 routed defect #3, L76-13).
    """
    allow = set(stated_at_allowlist())
    site = OUTSIDE_SITE % (CFG.round - 3)
    pair = _first_pair(
        ctx, lambda p: p.get("disposition") == "ANNOTATE"
        and _stated_path(p) in allow
        and (p.get("stated_text") or "").strip()
        and not re.search(r"\bS\d{3,}\b", p.get("stated_text") or ""))
    text = read(repo, site) if os.path.isfile(os.path.join(repo, site)) else ""
    marker = "round-%d fixture: stated line carried from %s" % (
        CFG.round, pair.get("stated_at"))
    body = text.rstrip("\n") + "\n" + marker + " — %s\n" % pair["stated_text"]
    write(repo, site, body)
    line_no = len(body.splitlines())
    pair["stated_at"] = "%s:%d" % (site, line_no)
    write_json(repo, CFG.ledger, ctx["ledger"])
    ctx["detail"] = ("%s's stated_at moved to %s:%d, outside the frozen "
                     "allowlist %s; its stated_text is present on that line"
                     % (pair.get("id"), site, line_no, sorted(allow)))
    ctx["own_freeze"] = True


def junk_J9(repo, ctx):
    """A FREEZE pair's stated_text is absent at its stated_at in the base tree.

    The pair keeps its allowlisted stated_at, its stated_parse and its stated
    token; only a trailing marker is added to stated_text, so the text no
    longer occurs at the base (round-76 routed defect: L76-19).
    """
    allow = set(stated_at_allowlist())
    pair = _first_pair(
        ctx, lambda p: _stated_path(p) in allow
        and (p.get("stated_text") or "").strip())
    pair["stated_text"] = "%s (round-%d fixture marker)" % (
        pair["stated_text"], CFG.round)
    write_json(repo, CFG.ledger, ctx["ledger"])
    ctx["detail"] = ("%s's stated_text now ends with a round-%d fixture "
                     "marker, so the exact text is absent at %s in the base "
                     "tree while its stated_parse token still derives"
                     % (pair.get("id"), CFG.round, pair.get("stated_at")))
    ctx["own_freeze"] = True


def junk_J10(repo, ctx):
    """A FREEZE pair's observe_cmd is a grep -E argv with an escaped-pipe
    pattern operand and no pattern-operand mark (r77's own clause).

    The argv is a legal argv over the allowlist and its operand exists in the
    base clone, so an argv-shape guard alone passes it; only the clause "no
    grep -E pattern operand holds a backtick or escaped pipe unless marked
    pattern-operand" refuses it.
    """
    pair = _first_pair(ctx, lambda p: isinstance(p.get("observe_cmd"), list))
    for key in PATTERN_MARK_KEYS:
        pair.pop(key, None)
    pair["observe_cmd"] = ["grep", "-c", "-E", "zzz\\|zzz", "corpus/SOURCES.md"]
    pair["expected_after"] = "0"
    write_json(repo, CFG.ledger, ctx["ledger"])
    ctx["detail"] = ("%s's observe_cmd is grep -c -E 'zzz\\|zzz' "
                     "corpus/SOURCES.md: an escaped pipe in the -E pattern "
                     "operand, no pattern-operand mark, the operand present at "
                     "base and the pattern matching nothing (expected '0')"
                     % pair.get("id"))
    ctx["own_freeze"] = True


def junk_J11(repo, ctx):
    """The frozen `required_sections[]` lines are removed from the landing.

    NEGATIVE control: ROWS must stay GREEN because it counts only `| S### |`
    lines inside the frozen row_set; INDEX must go RED because the Paths and
    Search-log lines are required there.  This is the round-76 routed defect
    (ROWS failed the landing's two required non-row lines).
    """
    items = required_sections(ctx["claims"])
    if not items:
        raise FixtureError("claim C carries no required_sections[]; the "
                           "round-77 contract enumerates the required non-row "
                           "edits there and without it this fixture has no "
                           "subject")
    touched = []
    for item in items:
        path, idx, line = _required_line(repo, item)
        lines = read(repo, path).splitlines(keepends=True)
        del lines[idx]
        write(repo, path, "".join(lines))
        touched.append("%s: %r" % (path, line.strip()[:60]))
    ctx["detail"] = ("%d frozen required_sections[] line(s) removed (%s); the "
                     "row append is untouched" % (len(touched),
                                                  "; ".join(touched)))
    ctx["must_pass"] = ("ROWS",)


# The R1EXEMPT pair: G edits only a rule-2 cell, R only a non-rule-2 cell.
def junk_G(repo, ctx):
    """Only a rule-2 (used-by) cell edit on one pre-existing row."""
    cols = registry_columns(repo)
    rid = _rule2_row_id(repo, ctx)
    line = registry_row(repo, rid)
    used_by = split_cells(line)[cols["used-by"]].strip()
    new_used_by = sanitize_cell(
        used_by + ("," if used_by else "")
        + "corpus/knowledge/myth-symbol/comparative-frameworks.md")
    edited = set_cell(line, cols["used-by"], new_used_by)
    write(repo, REGISTRY,
          read(repo, REGISTRY).replace(line + "\n", edited + "\n", 1))
    ctx["cell"] = {"row": rid, "cell": "used-by", "index": cols["used-by"],
                   "old": used_by, "new": new_used_by, "rule2": True}
    ctx["detail"] = ("row %s: used-by cell edited only (a rule-2 cell); every "
                     "other byte of the tree is unchanged" % rid)


def junk_R(repo, ctx):
    """Only a non-rule-2 (teaches) cell edit on one pre-existing row."""
    cols = registry_columns(repo)
    rid = _rule2_row_id(repo, ctx)
    line = registry_row(repo, rid)
    teaches = split_cells(line)[cols["teaches"]].strip()
    new_teaches = sanitize_cell(
        teaches + " [junk fixture: non-rule-2 edit]")
    edited = set_cell(line, cols["teaches"], new_teaches)
    write(repo, REGISTRY,
          read(repo, REGISTRY).replace(line + "\n", edited + "\n", 1))
    ctx["cell"] = {"row": rid, "cell": "teaches", "index": cols["teaches"],
                   "old": teaches, "new": new_teaches, "rule2": False}
    ctx["detail"] = ("row %s: teaches cell edited only (not a rule-2 cell); "
                     "every other byte of the tree is unchanged" % rid)


FIXTURES = {
    "J1": ("C", junk_J1, ("ENTRIES",),
           "FAIL: a header-only stub entry at the frozen entry path, with its "
           "row's used-by naming the stub (ENTRIES)"),
    "J2": ("C", junk_J2, ("EVIDENCE", "GATE"),
           "FAIL: the Gate admit quote is absent from every stored evidence "
           "window while the window sha256 still recomputes (EVIDENCE; the "
           "lesson Gate row can no longer bind its quote either, so GATE is "
           "reported as an also-reached leg)"),
    "J3": ("C", junk_J3, ("FROZENCFG",),
           "FAIL: the graded tree's claims.json shrinks claim C by one row (and one "
           "entry when it carries more than one) (FROZENCFG)"),
    "J4": ("Ca", junk_J4, ("LEDGER",),
           "FAIL: the FREEZE's every observe_cmd is a literal constant printer "
           "of expected_after (LEDGER reads the freeze, so the fixture commits "
           "its own defective freeze)"),
    "J4b": ("Ca", junk_J4b, ("LEDGER",),
            "FAIL: the FREEZE's every observe_cmd is the evasive constant "
            "printer (import os;assert os.sep;print(str(...)))"),
    "J5": ("Ca", junk_J5, ("ANNOTATE",),
           "FAIL: a Corrections — round <N> row names only its id (ANNOTATE)"),
    "J6": ("Ca", junk_J6, ("APPENDONLY",),
           "FAIL: a frozen receipt outside every protected set is edited in "
           "place (APPENDONLY)"),
    "J7": ("Ca", junk_J7, ("SEPARABLE",),
           "FAIL: a byte in the Ca read set cites a claim-C lane id "
           "(SEPARABLE)"),
    "J8": ("Ca", junk_J8, ("LEDGER",),
           "FAIL: a FREEZE pair's stated_at names a file outside the frozen "
           "allowlist while its stated_text is present there (LEDGER; the "
           "round-76 routed L76-13 class)"),
    "J9": ("Ca", junk_J9, ("LEDGER",),
           "FAIL: a FREEZE pair's stated_text is absent at its stated_at in "
           "the base tree (LEDGER; the round-76 routed L76-19 class)"),
    "J10": ("Ca", junk_J10, ("LEDGER",),
            "FAIL: a FREEZE pair's observe_cmd is a grep -E argv whose pattern "
            "operand carries an escaped pipe and no pattern-operand mark "
            "(LEDGER; the round-76 routed unexecutable-argv class)"),
    "J11": ("C", junk_J11, ("INDEX",),
            "NEGATIVE CONTROL: the frozen required_sections[] Paths/Search-log "
            "lines are removed from the landing, so INDEX must go RED and ROWS "
            "must stay GREEN (it counts only `| S### |` lines inside the "
            "frozen row_set) — the round-76 routed out-of-set class"),
}

# Legs a fixture's defect must NOT reach.  J11 is the negative control: the
# whole point is that ROWS does not consume the required non-row edits.
MUST_PASS = {"J11": ("ROWS",)}

# Fixtures whose defect belongs to the contract the counter FREEZE-pins, so
# the fixture's own commit must be the freeze (a lands-only edit is only ever
# visible as a FROZENCFG byte difference).
OWN_FREEZE = ("J4", "J4b", "J8", "J9", "J10")

R1_PAIR = {
    "G": ("Ca", junk_G,
          "GREEN: only a rule-2 (used-by) cell edit on one pre-existing row; "
          "the APPENDONLY leg must stay green and every other leg must be "
          "unchanged"),
    "R": ("Ca", junk_R,
          "RED: only a non-rule-2 (teaches) cell edit on one pre-existing "
          "row; the APPENDONLY leg must go red and every other leg must be "
          "unchanged"),
}

ORDER = ("J1", "J2", "J3", "J4", "J4b", "J5", "J6", "J7", "J8", "J9", "J10",
         "J11")
# ------------------------------------------------------------------- grading ---

def _counter_path(repo, candidates, override=None):
    if override:
        if not os.path.isfile(override):
            raise FixtureError("counter %s does not exist" % override)
        return override
    for rel in candidates:
        if os.path.isfile(os.path.join(repo, rel)):
            return os.path.join(repo, rel)
    raise FixtureError("no counter found in the tree at %s"
                       % " or ".join(candidates))


def verdict_is_for(text, claim, round_no):
    """True when a verdict line names `claim` (optional) and `round_no`.

    A counter for another round, or the other claim, did not grade this
    fixture; its PASS may never be counted.
    """
    m = ACCEPT_RE.match((text or "").strip())
    if not m:
        return False
    if int(m.group(2)) != int(round_no):
        return False
    if claim and m.group(1).upper() != str(claim).strip().upper():
        return False
    return True


def run_counter(repo, counter, rev, freeze, fleet_root=FLEET_ROOT,
                claim=None, extra=(), round_no=None):
    """Run one counter over `rev` and parse its verdict.

    Returns a dict: {exit, verdict, legs, total, red, green, tail, out,
    refused, cmd}.  `green` is the set of legs the counter reported as PASS.
    A verdict line carrying another round's token (or the other claim's
    letter) is NO-VERDICT: a counter for a different round or claim did not
    grade this fixture, so its PASS may never count.
    """
    cmd = [sys.executable, "-B", counter, "--root", repo, "--lands", rev,
           "--freeze", freeze, "--fleet-root", fleet_root] + list(extra)
    expect = int(round_no if round_no is not None else CFG.round)
    try:
        r = _run(cmd, cwd=repo, timeout=COUNTER_TIMEOUT)
    except subprocess.TimeoutExpired:
        return {"exit": None, "verdict": "TIMEOUT", "legs": None,
                "total": None, "red": (), "green": (), "tail": "TIMEOUT",
                "out": "counter timed out after %ds" % COUNTER_TIMEOUT,
                "refused": False, "cmd": " ".join(cmd)}
    out = r.stdout + ("\n" + r.stderr if r.stderr.strip() else "")
    legs = leg_table(r.stdout)
    m = None
    for m in ACCEPT_RE.finditer(r.stdout):
        pass
    if m is None:
        return {"exit": r.returncode, "verdict": "NO-VERDICT", "legs": None,
                "total": None, "red": tuple(sorted(n for n, ok in legs.items()
                                                   if not ok)),
                "green": tuple(sorted(n for n, ok in legs.items() if ok)),
                "tail": (r.stdout.strip().splitlines() or
                         ["(no stdout)"])[-1],
                "out": out, "refused": "REFUSED" in out,
                "cmd": " ".join(cmd)}
    want_claim = (claim or "").strip().upper()
    if not verdict_is_for(m.group(0), want_claim, expect):
        note = ("# wrong verdict for this fixture: counter printed %r; the "
                "fixture expects ACCEPT-%s-%d"
                % (m.group(0), want_claim or "C|CA", expect))
        return {"exit": r.returncode, "verdict": "NO-VERDICT", "legs": None,
                "total": None, "red": tuple(sorted(n for n, ok in legs.items()
                                                   if not ok)),
                "green": tuple(sorted(n for n, ok in legs.items() if ok)),
                "tail": m.group(0), "out": out + "\n" + note,
                "refused": "REFUSED" in out, "cmd": " ".join(cmd)}
    return {"exit": r.returncode, "verdict": m.group(3),
            "legs": int(m.group(4)), "total": int(m.group(5)),
            "red": tuple(sorted(n for n, ok in legs.items() if not ok)),
            "green": tuple(sorted(n for n, ok in legs.items() if ok)),
            "tail": m.group(0), "out": out, "refused": "REFUSED" in out,
            "cmd": " ".join(cmd)}


def _leg_lines(res):
    out = []
    for line in res["out"].splitlines():
        if line.startswith("LEG "):
            out.append(line)
    return out


# ------------------------------------------------------------------- builder ---

SYNTHETIC_BASE = "211f9526800906e0c585d878d265c37e5e090c15"


def _synthetic_claims(round_no):
    """A round-77-SHAPED claim-C document for a dry run only.

    It mirrors the shape the round-77 DRAFT declares (one entry, two rows, an
    enumerated `required_sections[]`) so the C-side mutations can be exercised
    before the L1 commits the freeze.  It is NOT the contract: it carries no
    observations, its document URLs are placeholders, and no counter may grade
    a tree that carries it.
    """
    return {
        "round": round_no,
        "status": "SYNTHETIC — dry-run shape only; never the frozen contract",
        "base": SYNTHETIC_BASE,
        "claims": [
            {"id": "C", "axis": "coverage", "kind": "assimilation-sourced",
             "title": "synthetic dry-run claim C (round-%d)" % round_no,
             "min_admitted": 1,
             "entries": ["corpus/knowledge/linguistics/"
                         "naming-systems.amend-2026-10-23.md"],
             "row_set": [
                 {"id": "S897", "staged": "S897",
                  "document": "https://example.invalid/round-%d/d1" % round_no},
                 {"id": "S898", "staged": "S898",
                  "document": "https://example.invalid/round-%d/d2" % round_no}],
             "required_sections": [
                 {"path": REGISTRY, "section": "## Paths",
                  "match": "- naming-systems design — S897"},
                 {"path": REGISTRY, "section": "## Search log",
                  "match": "**Chinese personal naming (rows S897–S898).**"}],
             "rows_before": 820, "knowledge_before": 253},
            {"id": "Ca", "axis": "calibration",
             "title": "synthetic dry-run claim Ca (round-%d)" % round_no}],
        "frontier_step": {}, "attempt": {},
    }


def _synthetic_ledger(repo, round_no):
    """A round-77-SHAPED Ca ledger for a dry run only (SYNTHETIC).

    Ten ANNOTATE pairs whose `stated_at` sits inside the frozen allowlist and
    whose `stated_text` is a line of the previous round's lesson, so the J8/J9
    mutations have a clean pair to move.  Every observation field is a
    placeholder: this document is never graded.
    """

    picks_strict, picks_loose = [], []
    for rel in stated_at_allowlist(round_no):
        try:
            lines = read(repo, rel).splitlines()
        except OSError:
            continue
        for i, line in enumerate(lines):
            text = line.strip()
            if len(text) < 25 or text.startswith(("|", "#")):
                continue
            pick = (rel, i + 1, text)
            if re.search(r"S\d{3}", text):
                picks_loose.append(pick)
            else:
                picks_strict.append(pick)
    picks = (picks_strict + picks_loose)[:10]
    if len(picks) < 10:
        raise FixtureError("the base tree's %s carries %d quotable line(s); a "
                           "synthetic ledger needs ten"
                           % (", ".join(stated_at_allowlist(round_no)),
                              len(picks)))
    pairs = []
    for n, (rel, line_no, text) in enumerate(picks, 1):
        pairs.append({
            "id": "L77-%02d" % n,
            "disposition": "ANNOTATE",
            "stated_at": "%s:%d" % (rel, line_no),
            "stated_text": text[:80],
            "stated_parse": "([A-Za-z]{4,})",
            "observe_cmd": ["wc", "-l", "corpus/SOURCES.md"],
            "parse": "^\\s*(\\d+)",
            "expected_after": "900",
            "observed_at_base": "900",
            "red_at_base": True,
            "rederive": "wc -l corpus/SOURCES.md",
            "why": "SYNTHETIC dry-run pair: no observation was taken",
        })
    return {"round": round_no, "claim": "Ca", "axis": "calibration",
            "base": SYNTHETIC_BASE,
            "status": "SYNTHETIC — dry-run shape only; never the frozen "
                      "contract, never gradeable",
            "pairs": pairs}


def _seed_frozen_config(repo, synthetic=False):
    """Put reports/round-<N>/{claims,ledger}.json into the fixture tree when
    the reference tree does not carry them.

    The convention is that the freeze commit carries both, and every fixture
    then mutates real frozen bytes.  Before the L1 has committed the freeze
    the files exist only in the lane's working tree; seeding them there keeps
    the fixtures materializable against a candidate freeze, and the fixture's
    detail line says so, so a receipt never claims to have graded committed
    bytes it did not.

    With `synthetic=True` and neither the tree nor the lane carrying a file,
    a round-77-SHAPED document is written instead (see `_synthetic_claims` /
    `_synthetic_ledger`).  The caller is responsible for refusing to grade such
    a tree: a synthetic fixture proves the MUTATION applies, never that a
    counter refuses it.
    """
    seeded = []
    docs = {CFG.claims: lambda: _synthetic_claims(CFG.round),
            CFG.ledger: lambda: _synthetic_ledger(repo, CFG.round)}
    for rel in (CFG.claims, CFG.ledger):
        if os.path.isfile(os.path.join(repo, rel)):
            continue
        src = os.path.join(LANE, rel)
        if os.path.isfile(src):
            with open(src, encoding="utf-8") as fh:
                write(repo, rel, fh.read())
            seeded.append((rel, "lane-copy"))
        elif synthetic and rel in docs:
            write_json(repo, rel, docs[rel]())
            seeded.append((rel, "SYNTHETIC"))
        else:
            continue
    return seeded


def _load_ctx(repo, freeze, lands, base):
    """The frozen claims/ledger — the same bytes the counter reads.

    The freeze commit carries reports/round-<N>/claims.json and ledger.json;
    they are read from there first.  When the freeze does not carry them (a
    freeze taken before the L1 committed them), the lane's own working-tree
    copy is used, so the fixtures can still be materialized against a
    candidate freeze.
    """
    def _doc(rel):
        try:
            return json.loads(git_show(repo, freeze, rel))
        except FixtureError:
            pass
        try:
            return json.loads(read(repo, rel))
        except OSError:
            pass
        with open(os.path.join(LANE, rel), encoding="utf-8") as fh:
            return json.loads(fh.read())
    claims = _doc(CFG.claims)
    ledger = _doc(CFG.ledger)
    return {"repo": repo, "freeze": freeze, "lands": lands, "base": base,
            "claims": claims, "ledger": ledger, "detail": ""}


def build(name, freeze, lands=None, base=None, workroot=None, baseline=False,
          synthetic=False):
    """Materialize one fixture.

    `freeze` is the frozen-contract commit; `lands` is the reference tree the
    mutation is applied to (default: the freeze commit itself).  Returns a
    Fixture(repo, rev, expected, ...).  With `baseline=True` the reference
    tree is committed untouched (the T0 baseline of the leg table).

    The R1EXEMPT pair (G, R) is always built on the FREEZE tree, not on the
    landing tree: the frozen Ca R1EXEMPT leg asks for "a tree whose only
    SOURCES delta versus base is a rule-2 cell edit on one pre-existing row"
    (G) and "a tree whose only SOURCES delta is a teaches-cell edit on one
    pre-existing row" (R).  Building them on the landing would add the
    landing's registry appends to the SOURCES delta and destroy exactly the
    property the pair exists to measure.
    """
    if name in FIXTURES:
        claim, junk, expected, desc = FIXTURES[name]
        # The ledger-shape fixtures (OWN_FREEZE) mutate the contract the
        # counter pins, so they mount on the FREEZE tree: mounting them on the
        # landing would fold the landing's own deltas into the fixture's
        # freeze and blur what the fixture is attributable to.
        reference = freeze if name in OWN_FREEZE else (lands or freeze)
    elif name in R1_PAIR:
        claim, junk, desc = R1_PAIR[name]
        expected = ("APPENDONLY",)
        reference = freeze
    else:
        raise FixtureError("unknown fixture %r (have %s)"
                           % (name, ", ".join(ORDER + tuple(R1_PAIR))))
    d, repo = clone_lane(workroot, name)
    try:
        git(repo, "checkout", "-q", "-B", "main", reference)
        git(repo, "read-tree", "-u", "--reset", reference)
        git(repo, "checkout", "-q", "main")
        cell = None
        own_freeze = False
        seeded = _seed_frozen_config(repo, synthetic)
        pre = {}
        for rel, _kind in seeded:
            try:
                pre[rel] = read(repo, rel)
            except OSError:
                pre[rel] = None
        if not baseline:
            ctx = _load_ctx(repo, freeze, reference, base)
            junk(repo, ctx)
            detail = ctx["detail"]
            cell = ctx.get("cell")
            own_freeze = bool(ctx.get("own_freeze"))
            if seeded:
                detail += (" [the reference tree carried no frozen config, so "
                           "this was seeded into the fixture: %s]"
                           % ", ".join("%s (%s)" % (rel, kind)
                                       for rel, kind in seeded))
        else:
            detail = "baseline: the reference tree, no mutation"
        if own_freeze:
            # The mutation belongs to the FREEZE the counter pins, so the
            # fixture's own commit is the freeze.  The LANDING is an EMPTY
            # child of it: <freeze> must stay a strict ancestor of <lands>,
            # and a `lands == freeze` run is exactly the shape FROZENCFG
            # refuses to pass — that rule would mask the LEDGER clause this
            # fixture exists to reach (round 75's J4f measured FROZENCFG red
            # and LEDGER green for that reason).
            rev = commit_all(repo, "junk fixture %s (%s): the freeze itself "
                                  "carries the defect" % (name, claim))
            changed = tuple(git(repo, "diff", "--name-only", reference,
                                rev).split())
            freeze = rev
            reference = rev
            rev = commit_all(repo, "junk fixture %s (%s): empty landing atop "
                                   "the defective freeze" % (name, claim),
                             allow_empty=True)
        else:
            rev = commit_all(repo, "junk fixture %s (%s) atop %s"
                             % (name, claim, reference[:12]))
            changed = tuple(git(repo, "diff", "--name-only", reference,
                                rev).split())
        if not baseline:
            # The seeded config is not part of the defect: a fixture whose only
            # delta is the seed did not mutate anything and must not be
            # reported as attributable.
            seed_only = set()
            for rel, _kind in seeded:
                try:
                    post = read(repo, rel)
                except OSError:
                    continue
                if pre.get(rel) == post:
                    seed_only.add(rel)
            defect = [p for p in changed if p not in seed_only]
            if not defect:
                raise FixtureError("%s committed no byte change beyond the "
                                   "seeded config" % name)
        legs = (FIXTURES[name][2] if name in FIXTURES else ("APPENDONLY",))
        must_pass = (ctx.get("must_pass") if not baseline else None) \
            or MUST_PASS.get(name)
        return Fixture(name, claim, repo, rev, desc, legs, changed, detail,
                       freeze, reference, base, cell, must_pass,
                       tuple("%s (%s)" % (rel, kind) for rel, kind in seeded))
    except Exception:
        shutil.rmtree(d, ignore_errors=True)
        raise


# --------------------------------------------------------------- the receipts ---

def _legs_of(res):
    return leg_table(res["out"])


def _newly_red(res, baseline_res):
    if baseline_res is None:
        return []
    base = _legs_of(baseline_res)
    return sorted(n for n, ok in _legs_of(res).items()
                  if not ok and base.get(n, True))


def _sources_delta(repo, base, rev):
    """The SOURCES.md delta between `base` and `rev`: (changed-line count,
    the changed line numbers, the diffstat)."""
    if not base:
        return None, [], ""
    numstat = git(repo, "diff", "--numstat", "%s..%s" % (base, rev),
                  "--", REGISTRY).strip()
    diff = git(repo, "diff", "-U0", "--no-color", "%s..%s" % (base, rev),
               "--", REGISTRY)
    lines = []
    for line in diff.splitlines():
        m = re.match(r"^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@", line)
        if m:
            start, count = int(m.group(1)), int(m.group(2) or 1)
            lines.extend(range(start, start + count))
    return numstat, lines, numstat


def _r1_receipt(name, fx, res, baseline_res, path, counterpart=None):
    """The r1exempt-green.txt / r1exempt-red.txt receipt grammar.

    The receipt carries the runs (the counter command, its exit status and
    stdout's LEG lines), the properties the frozen Ca R1EXEMPT leg asks for
    — the SOURCES delta versus base is exactly one changed line on one
    pre-existing row, the APPENDONLY verdict itself, and every other leg
    unchanged — and the recipe the counter needs to RE-DERIVE the fixture:
    the base, the freeze, the row id, the cell index and the cell's old and
    new text.  `counterpart` is the other half of the pair, whose leg table
    is printed so the pair's one differing leg is visible in both receipts.
    """
    legs = _legs_of(res)
    appendonly = legs.get("APPENDONLY")
    expected = "GREEN" if name == "G" else "RED"
    others_same = True
    if baseline_res is not None:
        base = _legs_of(baseline_res)
        for leg, ok in legs.items():
            if leg == "APPENDONLY":
                continue
            if base.get(leg) != ok:
                others_same = False
    ok = (appendonly is True if name == "G" else appendonly is False)
    numstat, changed_lines, _ = _sources_delta(fx.repo, fx.base, fx.rev)
    one_line = (len(changed_lines) == 1)
    pair_diff = None
    if counterpart is not None:
        other_legs = _legs_of(counterpart["res"])
        pair_diff = sorted(set(legs) | set(other_legs))
        pair_diff = [leg for leg in pair_diff
                     if legs.get(leg) != other_legs.get(leg)]
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("# r1exempt-%s.txt — round-%d R1EXEMPT fixture %s\n"
                 % (expected.lower(), CFG.round, name))
        fh.write("# claim: Ca   leg under test: APPENDONLY   expectation: %s\n"
                 % expected)
        fh.write("# generated: %s\n" % time.strftime("%Y-%m-%dT%H:%M:%SZ",
                                                     time.gmtime()))
        fh.write("# fixture: %s — %s\n" % (name, fx.expected))
        fh.write("# mutation: %s\n" % fx.detail)
        fh.write("# freeze: %s\n" % fx.freeze)
        fh.write("# base: %s\n" % (fx.base or "(none given)"))
        fh.write("# reference-lands: %s\n" % fx.lands)
        fh.write("# fixture-lands: %s\n" % fx.rev)
        fh.write("# tree: %s\n" % git(fx.repo, "rev-parse",
                                      "%s^{tree}" % fx.rev).strip())
        fh.write("# counter: %s\n" % res["cmd"])
        fh.write("# changed-paths: %s\n" % (", ".join(fx.paths) or "(none)"))
        if fx.cell:
            fh.write("# edited-row: %s\n" % fx.cell["row"])
            fh.write("# edited-cell: %s (index %d, rule-2 cell: %s)\n"
                     % (fx.cell["cell"], fx.cell["index"],
                        "yes" if fx.cell["rule2"] else "no"))
            fh.write("# old-cell: %s\n" % fx.cell["old"])
            fh.write("# new-cell: %s\n" % fx.cell["new"])
        fh.write("# sources-delta-vs-base: %s\n" % (numstat or "(none)"))
        fh.write("# sources-changed-lines-vs-base: %s\n"
                 % (", ".join(str(n) for n in changed_lines) or "(none)"))
        fh.write("# sources-delta-is-one-changed-line: %s\n"
                 % ("yes" if one_line else "no"))
        fh.write("exit: %d\n" % res["exit"])
        fh.write("%s\n" % res["tail"])
        for line in _leg_lines(res):
            fh.write("%s\n" % line)
        if baseline_res is not None:
            fh.write("# baseline-legs: %s\n"
                     % ", ".join("%s=%s" % (n, "PASS" if ok else "FAIL")
                                 for n, ok in sorted(_legs_of(baseline_res).items())))
        if counterpart is not None:
            fh.write("# counterpart-fixture: %s\n" % counterpart["name"])
            fh.write("# counterpart-appendonly: %s\n"
                     % counterpart["appendonly"])
            fh.write("# legs-differing-from-counterpart: %s\n"
                     % (", ".join(pair_diff) if pair_diff is not None
                        else "(not compared)"))
        fh.write("appendonly: %s\n"
                 % ("PASS" if appendonly is True else
                    "FAIL" if appendonly is False else "NOT-REPORTED"))
        fh.write("other-legs-unchanged: %s\n" % ("yes" if others_same else "no"))
        fh.write("verdict: %s\n" % ("AS-EXPECTED" if ok else "UNEXPECTED"))
    return ok


# ------------------------------------------------------------------- runner ---

def run(freeze, lands=None, base=None, only=None, workroot=None,
        out_dir=None, keep=False, baseline=True, out=sys.stdout,
        counters=None, synthetic=False, grade_it=True, combined=None):
    """Build and grade every fixture; return (met, unmet) fixture names.

    `counters` maps "C"/"CA" to an explicit counter path (`--c-counter` /
    `--ca-counter`); without it the counter is taken from the graded tree at
    the round's committed path, then from the wave's `counters/` copy.

    With `grade_it=False` (`--no-grade`) the fixtures are only materialized:
    the table records each fixture's commit and mutation and claims no verdict.
    """
    workroot = resolve_workroot(workroot)
    return _run_fixtures(freeze, lands, base, only, workroot, out_dir,
                         keep, baseline, out, counters or {},
                         synthetic=synthetic, grade_it=grade_it,
                         combined=combined)


def grade(fx, counter, claim, workroot, combined=None):
    """Run the round-77 counter over one fixture with its own required argv.

    Round 77's Ca counter refuses to run without `--combined` and `--work`, and
    its C counter without `--work` (the do-nothing control shape).  The fixture
    tree carries both landings for the fixtures that grade Ca, so `--combined`
    defaults to the fixture's own revision.
    """
    return run_counter(fx.repo, counter, fx.rev, fx.freeze, claim=claim,
                       round_no=CFG.round,
                       extra=_counter_extra(claim, fx.rev, workroot,
                                            combined))


def _counter_extra(claim, rev, work, combined=None):
    """The counter's own required argv (draft: `--combined`/`--work`)."""
    extra = ["--work", work]
    if str(claim).strip().upper() == "CA":
        extra += ["--combined", combined or rev, "--main", rev]
    return tuple(extra)


def _expectation(fx, res):
    """(as-expected?, lines) for one graded fixture.

    `expected_legs[0]` is the leg the fixture exists to reach and MUST be red;
    any further names are legs the same defect may also reach (reported, not
    required — the frozen round-77 wording decides how far it spreads).
    `must_pass` legs must be green: that is the whole point of the J11
    negative control.
    """
    legs = _legs_of(res)
    named = list(fx.expected_legs or ())
    lines = []
    ok = True
    if not legs:
        return False, ["no LEG line was printed: the counter produced no leg "
                       "table, so nothing about this fixture is attributable"]
    for i, leg in enumerate(named):
        red = legs.get(leg) is False
        role = "required-leg" if i == 0 else "also-expected-leg"
        if i == 0:
            ok = ok and red
        lines.append("%s %s: %s" % (role, leg,
                                    "RED (counter refused)" if red
                                    else "NOT-RED (counter did not refuse)"))
    for leg in fx.must_pass or ():
        green = legs.get(leg) is True
        ok = ok and green
        lines.append("must-pass-leg %s: %s" % (leg, "GREEN" if green
                                               else "NOT-GREEN"))
    return ok, lines


def _baseline_for(freeze, reference, base, workroot):
    """The unmutated reference tree, committed (the T0 of the leg table)."""
    d, repo = clone_lane(workroot, "baseline")
    try:
        git(repo, "checkout", "-q", "-B", "main", reference)
        git(repo, "read-tree", "-u", "--reset", reference)
        git(repo, "checkout", "-q", "main")
        rev = commit_all(repo, "junk fixture baseline (unmutated reference "
                               "tree %s)" % reference[:12], allow_empty=True)
        return Fixture("BASELINE", "-", repo, rev, "", (), (), "", freeze,
                       reference, base, None, None, ())
    except Exception:
        shutil.rmtree(d, ignore_errors=True)
        raise


def _run_fixtures(freeze, lands, base, only, workroot, out_dir, keep, baseline,
                  out, counters, synthetic=False, grade_it=True,
                  combined=None):
    lands = lands or freeze
    names = [n for n in ORDER + tuple(R1_PAIR) if not only or n in only]
    print(file=out)
    print("# ==================== round-%d junk landings ===================="
          % CFG.round, file=out)
    print("# freeze: %s" % freeze, file=out)
    print("# base: %s" % (base or "(not given)"), file=out)
    print("# reference lands: %s" % lands, file=out)
    print("# lane: %s" % LANE, file=out)
    print("# fleet-root: %s" % FLEET_ROOT, file=out)
    print("# workroot: %s" % workroot, file=out)
    print("# counters: %s ; %s"
          % (counters.get("C") or c_counter_candidates()[0],
             counters.get("CA") or ca_counter_candidates()[0]), file=out)
    print(file=out)

    met, unmet = [], []
    baselines = {}
    r1_results = {}
    if baseline:
        for label, ref in (("landing", lands), ("freeze", freeze)):
            try:
                fx = _baseline_for(freeze, ref, base, workroot)
            except (FixtureError, OSError) as exc:
                print("# baseline (%s): not materialized (%s)" % (label, exc),
                      file=out)
                continue
            baselines[label] = fx
    baseline_res = {}

    def _grader(claim):
        """The counter for `claim`: the CLI override wins over the tree."""
        return counters.get(claim.upper()) or counters.get(claim)

    def _grade_baseline(label, claim):  # combined: the C-lands tree, if given
        fx = baselines.get(label)
        if fx is None:
            return None
        key = (label, claim)
        if key in baseline_res:
            return baseline_res[key]
        try:
            counter = _counter_path(
                fx.repo,
                c_counter_candidates() if claim == "C"
                else ca_counter_candidates(),
                override=_grader(claim))
            # The counter is pinned to the FIXTURE's freeze: for the
            # own-freeze fixtures (J4f) that is the fixture's own commit, so
            # the counter reads the defective ledger.
            res = run_counter(fx.repo, counter, fx.rev, fx.freeze,
                              claim=claim, round_no=CFG.round,
                              extra=_counter_extra(claim, fx.rev, workroot,
                                                   combined))
        except (FixtureError, OSError) as exc:
            print("# baseline (%s, %s): not graded (%s)" % (label, claim, exc),
                  file=out)
            return None
        baseline_res[key] = res
        return res

    for section in ("C", "Ca"):
        print("# ===== SECTION %s =====" % section, file=out)
        print(file=out)
        for name in names:
            claim = (FIXTURES[name][0] if name in FIXTURES
                     else R1_PAIR[name][0])
            if claim != section:
                continue
            label = "freeze" if name in R1_PAIR else "landing"
            try:
                fx = build(name, freeze, lands, base, workroot,
                           synthetic=synthetic)
                if not grade_it:
                    # --no-grade: the tree is materialized and its commit
                    # recorded, but no verdict is claimed.  A synthetic-config
                    # tree is never graded: it proves the mutation applies,
                    # never that a counter refuses it.
                    print("fixture: %s" % name, file=out)
                    print("claim: %s" % claim, file=out)
                    print("mutation: %s" % fx.detail, file=out)
                    print("lands: %s" % fx.rev, file=out)
                    print("freeze: %s" % fx.freeze, file=out)
                    print("changed-paths: %s"
                          % (", ".join(fx.paths) or "(none)"), file=out)
                    if fx.seeded:
                        print("seeded-config: %s" % ", ".join(fx.seeded),
                              file=out)
                    print("expected-legs: %s"
                          % (", ".join(fx.expected_legs) or "-"), file=out)
                    print("graded: no (dry run: no verdict is claimed)",
                          file=out)
                    print(file=out)
                    if not keep:
                        cleanup(fx)
                    continue
                counter = _counter_path(
                    fx.repo,
                    c_counter_candidates() if claim == "C"
                    else ca_counter_candidates(),
                    override=_grader(claim))
                res = grade(fx, counter, claim, workroot, combined)
            except (FixtureError, OSError, subprocess.SubprocessError) as exc:
                print("fixture: %s" % name, file=out)
                print("error: %s: %s" % (type(exc).__name__, exc), file=out)
                print("as-expected: no (the fixture was not materialized or "
                      "graded)", file=out)
                print(file=out)
                unmet.append(name)
                continue
            brec = _grade_baseline(label, claim) if baseline else None
            ok, checks = _expectation(fx, res)
            (met if ok else unmet).append(name)
            print("fixture: %s" % name, file=out)
            print("section: %s" % section, file=out)
            print("claim: %s" % claim, file=out)
            print("expected: %s" % fx.expected, file=out)
            print("mutation: %s" % fx.detail, file=out)
            print("reference-lands: %s" % fx.lands, file=out)
            print("lands: %s" % fx.rev, file=out)
            print("changed-paths: %s" % (", ".join(fx.paths) or "(none)"),
                  file=out)
            print("command: %s" % res["cmd"], file=out)
            print("exit: %d" % res["exit"], file=out)
            for line in _leg_lines(res):
                print(line, file=out)
            if brec is not None:
                print("baseline-legs: %s"
                      % ", ".join("%s=%s" % (n, "PASS" if ok else "FAIL")
                                  for n, ok in sorted(_legs_of(brec).items())),
                      file=out)
            print("verdict: %s" % res["tail"], file=out)
            print("red-legs: %s" % (", ".join(res["red"]) or "(none)"), file=out)
            print("newly-red: %s" % (", ".join(_newly_red(res, brec)) or
                                     "(none)"), file=out)
            print("expected-legs: %s" % (", ".join(fx.expected_legs) or "-"),
                  file=out)
            for line in checks:
                print(line, file=out)
            print("as-expected: %s" % ("YES" if ok else "no"), file=out)
            print(file=out)
            if name in R1_PAIR:
                # The pair's receipts are written after BOTH halves are
                # graded, so each can print the legs that differ from its
                # counterpart.  The fixture repo must survive until then:
                # the receipt reads the tree id from it.
                r1_results[name] = {"fx": fx, "res": res, "base": brec}
            elif not keep:
                cleanup(fx)
    if out_dir and r1_results:
        os.makedirs(out_dir, exist_ok=True)
        for name, entry in r1_results.items():
            other = r1_results.get("R" if name == "G" else "G")
            counterpart = None
            if other is not None:
                counterpart = {
                    "name": ("R" if name == "G" else "G"),
                    "appendonly": _legs_of(other["res"]).get("APPENDONLY"),
                    "res": other["res"],
                }
            target = os.path.join(out_dir, "r1exempt-%s.txt"
                                  % ("green" if name == "G" else "red"))
            _r1_receipt(name, entry["fx"], entry["res"], entry["base"],
                        target, counterpart)
            print("# wrote %s" % target, file=out)
    for entry in r1_results.values():
        if not keep:
            cleanup(entry["fx"])
    for fx in baselines.values():
        if not keep:
            cleanup(fx)
    if met:
        print("# EXPECTATIONS MET: %s" % " ".join(met), file=out)
    if unmet:
        print("# EXPECTATIONS NOT MET: %s" % " ".join(unmet), file=out)
    if not met and not unmet:
        print("# EXPECTATIONS MET: none", file=out)
    return met, unmet


# --------------------------------------------------------------------- CLI ---

def _selftest():
    """Exercise the mutation helpers without any counter (stdlib only)."""
    failures = []

    def check(name, cond, why=""):
        if not cond:
            failures.append("%s: %s" % (name, why))

    # cell splitting with an escaped pipe
    line = "| S001 | a \\| b | c |"
    cells = split_cells(line)
    check("split_cells", len(cells) == 5, "got %d cells" % len(cells))
    check("split_cells escaped", cells[2] == " a \\| b ", repr(cells[2]))

    # constant printers
    doc = {"pairs": [{"id": "L1", "expected_after": "808"},
                     {"id": "L2", "expected_after": "32"}]}
    lit = rewrite_ledger_observe(json.loads(json.dumps(doc)), "literal")
    check("literal even", lit["pairs"][0]["observe_cmd"][0] == "python3",
          repr(lit["pairs"][0]["observe_cmd"]))
    check("literal odd", lit["pairs"][1]["observe_cmd"][0] == "echo",
          repr(lit["pairs"][1]["observe_cmd"]))
    ev = rewrite_ledger_observe(json.loads(json.dumps(doc)), "evasive")
    check("evasive", "import os" in ev["pairs"][0]["observe_cmd"][2],
          repr(ev["pairs"][0]["observe_cmd"]))
    sh = rewrite_ledger_observe(json.loads(json.dumps(doc)), "shell")
    check("shell", "|" in sh["pairs"][0]["observe_cmd"][0],
          repr(sh["pairs"][0]["observe_cmd"]))

    # correction-row helpers
    text = ("## Corrections — round %d\n\n" % CFG.round
            + "| id | old | new | cmd |\n|---|---|---|---|\n"
            "| L75-01 | 412 | 808 | git grep -c x |\n")
    stubbed = stub_correction_row(text, "L75-01")
    check("stub row", "| L75-01 |" in stubbed and "808" not in stubbed,
          repr(stubbed))
    appended = append_correction_row(text, CFG.round,
                                     "| L75-02 | a | b | c | S885 |")
    check("append row", "S885" in appended, "citation missing")
    check("append row keeps old", "| L75-01 | 412 | 808 |" in appended,
          "existing row damaged")

    # gate quote extraction
    lesson = ("## Gate\n\n"
              "| url | date | quote | admitted |\n"
              "|---|---|---|---|\n"
              "| https://example.invalid/a | 2026-10-27 | \"une citation "
              "verifiable\" | admitted |\n"
              "| https://example.invalid/b | 2026-10-27 | \"une citation "
              "refusee\" | refused |\n")
    quotes = list(gate_quotes(lesson))
    check("gate quotes", quotes == ["une citation verifiable"], repr(quotes))

    # the evidence-window helpers
    ev = ("# evidence S885\n"
          "window-sha256: x\nwindow-bytes: 10\nwindow-scope: excerpt\n"
          "visible-chars: 4096\n"
          "--- window ---\n"
          "abc 自然環境が社会の仕組みを決め、社会の仕組みが文化を生む。\n"
          "--- quote ---\n"
          "自然環境が社会の仕組みを決め、社会の仕組みが文化を生む。\n")
    found = _evidence_window(ev)
    check("evidence window", found is not None, "no window block found")
    if found:
        window, start, stop = found
        check("window text", "自然環境" in window, repr(window[:40]))
    quotes = list(row_quotes(
        "| id | url | quote | verdict |\n"
        "|---|---|---|---|\n"
        "| S885 | https://example.invalid/a | \"une citation\" | admitted |\n"
        "| S886 | https://example.invalid/b | \"autre citation\" | refused |\n",
        "S885"))
    check("row quotes", quotes == ["une citation"], repr(quotes))
    check("row quotes refuse", list(row_quotes(
        "| S886 | u | \"autre citation\" | refused |\n", "S886")) == [],
        "a refused row yielded a quote")
    check("nfkc fold", nfkc_ws("a b") == "ab", nfkc_ws("a b"))

    # round configuration: every path and token follows the round number
    r75 = round_config(75)
    check("round paths",
          (r75.claims, r75.ledger, r75.evidence, r75.telemetry, r75.lesson)
          == ("reports/round-75/claims.json", "reports/round-75/ledger.json",
              "reports/round-75/evidence", "reports/round-75/telemetry",
              "corpus/lessons/round-75.md"), repr(r75))
    check("round previous",
          round_config(76).prev_receipt == "accept-ca-75-at-lands.txt"
          and round_config(76).prev_counter
          == "reports/round-75/accept-ca.py", repr(round_config(76)))
    check("round default", CFG.round == ROUND, repr(CFG.round))
    check("protected set", CFG.prev_lesson in protected_set(),
          repr(protected_set()))
    check("stated-at allowlist",
          stated_at_allowlist() == ("LOG.md", "SCORECARD.md",
                                    "corpus/lessons/round-75.md",
                                    "corpus/lessons/round-76.md"),
          repr(stated_at_allowlist()))
    check("allowlist excludes README",
          "corpus/README.md" not in stated_at_allowlist(),
          "corpus/README.md is REPAIR-only, never an ANNOTATE site")

    # the pattern-operand clause J10 reaches
    pair = {"id": "L77-01",
            "observe_cmd": ["grep", "-c", "-E", "zzz\\|zzz", "corpus/SOURCES.md"]}
    check("pattern operand refused",
          pattern_operand_defect(pair["observe_cmd"], pair) is not None,
          "an escaped pipe in an unmarked -E operand was accepted")
    marked = dict(pair, pattern_operand=True)
    check("pattern operand marked",
          pattern_operand_defect(pair["observe_cmd"], marked) is None,
          "a marked pattern operand was refused")
    plain = {"observe_cmd": ["grep", "-c", "-E", "^id", "corpus/SOURCES.md"]}
    check("plain pattern ok",
          pattern_operand_defect(plain["observe_cmd"], plain) is None,
          "a plain pattern operand was refused")
    check("pattern indices",
          grep_pattern_operands(["grep", "-c", "-E", "^x", "f"]) == {3},
          repr(grep_pattern_operands(["grep", "-c", "-E", "^x", "f"])))
    check("pattern indices -e",
          grep_pattern_operands(["grep", "-e", "^x", "f"]) == {2},
          repr(grep_pattern_operands(["grep", "-e", "^x", "f"])))

    # required_sections[]: dict and bare-string shapes
    claims_doc = {"claims": [{"id": "C", "required_sections": [
        {"path": REGISTRY, "section": "## Paths", "match": "x"},
        "## Search log"]}]}
    items = required_sections(claims_doc)
    check("required sections dict", items[0]["path"] == REGISTRY, repr(items))
    check("required sections string",
          items[1] == {"path": REGISTRY, "section": "## Search log"},
          repr(items))
    body = "## Paths\n- a\n\n## Search log\n**note**\n"
    start, end = _section_span(body.splitlines(), "## Search log")
    check("section span", (start, end) == (4, 5), repr((start, end)))

    # the fixture table: every r77 leg name is a frozen-table name
    r77_c = {"FROZENCFG", "STAMP", "LEDGELIST", "COUNTS", "ENTRIES", "ROWS",
             "APPENDONLY", "COLLCHECK", "INDEX", "EVIDENCE", "GATE",
             "REJECTS", "CENSUS", "GROUND", "RECEIPTS"}
    r77_ca = {"LEDGER", "BASEMISMATCH", "REPAIR", "ANNOTATE", "APPENDONLY",
              "R1EXEMPT", "SEPARABLE", "COMBINED", "RECEIPTS", "FROZENCFG",
              "STAMP", "LEDGELIST"}
    for name in ORDER:
        claim, _junk, expected, _desc = FIXTURES[name]
        table = r77_c if claim == "C" else r77_ca
        check("%s legs are r77 legs" % name, set(expected) <= table,
              "%s not in the round-77 %s table" % (set(expected) - table, claim))
    check("J11 must-pass", MUST_PASS.get("J11") == ("ROWS",),
          repr(MUST_PASS))
    check("own-freeze set", set(OWN_FREEZE) <= set(ORDER), repr(OWN_FREEZE))

    # the expectation evaluator: a required red leg, a must-pass green leg
    fx = Fixture("X", "C", "", "", "", (), (), "", "", "", None, None,
                 ("ROWS",), ())
    ok, lines = _expectation(fx, {"out": "LEG PASS ROWS\n"})
    check("expectation must-pass green", ok, repr(lines))
    ok, lines = _expectation(fx, {"out": "LEG FAIL ROWS\n"})
    check("expectation must-pass red", not ok, repr(lines))
    fx2 = fx._replace(expected_legs=("LEDGER",), must_pass=None)
    ok, _lines = _expectation(fx2, {"out": "LEG FAIL LEDGER\n"})
    check("expectation required red", ok, "a red required leg was refused")
    ok, _lines = _expectation(fx2, {"out": "LEG PASS LEDGER\n"})
    check("expectation required green", not ok,
          "a green required leg was accepted")
    ok, _lines = _expectation(fx2, {"out": "no leg lines\n"})
    check("expectation no legs", not ok, "an empty leg table was accepted")

    # the verdict guard: another round's or claim's PASS never counts
    check("verdict round",
          verdict_is_for("ACCEPT-C-75: PASS legs=1/1", "C", 75),
          "a round-75 verdict was rejected")
    check("verdict wrong round",
          not verdict_is_for("ACCEPT-C-75: PASS legs=1/1", "C", 76),
          "a round-75 verdict counted for round 76")
    check("verdict wrong claim",
          not verdict_is_for("ACCEPT-C-75: PASS legs=1/1", "CA", 75),
          "an accept-c verdict counted for claim Ca")
    check("verdict junk", not verdict_is_for("junk", "C", 75),
          "a non-verdict line was accepted")

    # scratch: a system-temporary root is refused, the env root is used
    check("scratch tmp refused",
          _forbidden_scratch(os.path.join(tempfile.gettempdir(), "r77")),
          "a system-temporary root was not refused")
    check("scratch explicit",
          resolve_workroot("/fast/scratch/hyaku/kotodama-r77/x")
          == "/fast/scratch/hyaku/kotodama-r77/x", "explicit root not used")
    _saved = os.environ.get("HYAKU_SCRATCH")
    os.environ["HYAKU_SCRATCH"] = "/scratch/base"
    try:
        check("scratch env",
              resolve_workroot() == "/scratch/base/kotodama-r77/junk-fixtures",
              repr(resolve_workroot()))
    finally:
        if _saved is None:
            del os.environ["HYAKU_SCRATCH"]
        else:
            os.environ["HYAKU_SCRATCH"] = _saved

    for name in failures:
        print("FAIL %s" % name)
    if failures:
        print("SELFTEST: FAIL (%d)" % len(failures))
        return 1
    print("SELFTEST: PASS")
    return 0


def main(argv=None):
    global CFG
    ap = argparse.ArgumentParser(
        description="junk-landing fixture generator (round-77; --round selects "
                    "the frozen round the counters belong to)")
    ap.add_argument("--run", action="store_true",
                    help="build and grade every fixture")
    ap.add_argument("--freeze", default=None, help="frozen-contract commit")
    ap.add_argument("--round", type=int, default=ROUND,
                    help="round token (default %d); the frozen claims.json "
                         "must declare it" % ROUND)
    ap.add_argument("--base", default=None,
                    help="the lane base revision the counter diffs against "
                         "(default: the frozen claims.json's own `base`)")
    ap.add_argument("--lands", default=None,
                    help="reference tree the mutation is applied to "
                         "(default: the freeze commit)")
    ap.add_argument("--combined", default=None,
                    help="the revision carrying BOTH landings, passed to the Ca "
                         "counter's required --combined (default: each "
                         "fixture's own landing commit)")
    ap.add_argument("--only", default=None,
                    help="comma-separated fixture names (default: all)")
    ap.add_argument("--out-dir", default=None,
                    help="directory for the r1exempt receipts")
    ap.add_argument("--out", default=None, help="run table output file")
    ap.add_argument("--workroot", "--work", dest="workroot", default=None,
                    help="parent dir for the fixture clones (default "
                         "$HYAKU_SCRATCH/kotodama-r<NN>/junk-fixtures, then "
                         "$TMPDIR, then /fast/scratch/hyaku)")
    ap.add_argument("--c-counter", default=None,
                    help="explicit reports/round-<N>/accept-c.py path (the "
                         "graded tree's copy is used when omitted)")
    ap.add_argument("--ca-counter", default=None,
                    help="explicit reports/round-<N>/accept-ca.py path")
    ap.add_argument("--keep", action="store_true",
                    help="keep the materialized repositories")
    ap.add_argument("--no-baseline", action="store_true",
                    help="skip the unmutated reference run")
    ap.add_argument("--no-grade", action="store_true",
                    help="materialize the fixtures and record their commits "
                         "without running a counter (no verdict is claimed)")
    ap.add_argument("--synthetic-config", action="store_true",
                    help="when neither the reference tree nor the lane carries "
                         "reports/round-<N>/{claims,ledger}.json, write a "
                         "round-<N>-SHAPED synthetic pair so the mutations can "
                         "be exercised before the freeze; such a tree is never "
                         "graded (implies --no-grade)")
    ap.add_argument("--selftest", action="store_true",
                    help="run the helper self-test (no counter needed)")
    ap.add_argument("--list", action="store_true", help="list the fixtures")
    args = ap.parse_args(argv)

    if args.round:
        CFG = round_config(args.round)

    if args.list:
        print("# round %d (claims %s)" % (CFG.round, CFG.claims))
        for name in ORDER:
            claim, _junk, expected, desc = FIXTURES[name]
            must = MUST_PASS.get(name)
            print("%-4s %-3s %-24s %s%s"
                  % (name, claim, ",".join(expected),
                     "must-pass: %s; " % ",".join(must) if must else "", desc))
        for name in ("G", "R"):
            claim, _junk, desc = R1_PAIR[name]
            print("%-4s %-3s %-24s %s" % (name, claim, "APPENDONLY", desc))
        return 0
    if args.selftest:
        return _selftest()
    if not args.run:
        ap.print_help()
        return 0
    if not args.freeze or not re.fullmatch(r"[0-9a-fA-F]{40}",
                                           args.freeze.strip()):
        print("ERROR: --run needs --freeze <40-hex>", file=sys.stderr)
        return 2
    freeze = args.freeze.strip().lower()
    lands = args.lands.strip().lower() if args.lands else freeze
    if not re.fullmatch(r"[0-9a-f]{40}", lands):
        print("ERROR: --lands must be 40-hex", file=sys.stderr)
        return 2
    combined = args.combined.strip().lower() if args.combined else None
    if combined and not re.fullmatch(r"[0-9a-f]{40}", combined):
        print("ERROR: --combined must be 40-hex", file=sys.stderr)
        return 2
    base = args.base.strip().lower() if args.base else None
    if base and not re.fullmatch(r"[0-9a-f]{40}", base):
        print("ERROR: --base must be 40-hex", file=sys.stderr)
        return 2
    # The frozen claims.json is the contract: it names the round and (unless
    # --base overrides it) the claim base the counter diffs against.
    frozen = None
    r = _run(["git", "-C", LANE, "show", "%s:%s" % (freeze, CFG.claims)])
    if r.returncode == 0:
        try:
            frozen = json.loads(r.stdout)
        except ValueError:
            frozen = None
    if frozen is None:
        if base is None:
            print("ERROR: cannot read %s at the freeze %s and no --base was "
                  "given" % (CFG.claims, freeze), file=sys.stderr)
            return 2
    else:
        declared = int(frozen.get("round") or 0)
        if declared and declared != CFG.round:
            print("ERROR: %s at %s declares round %d, not %d; pass --round %d"
                  % (CFG.claims, freeze[:12], declared, CFG.round, declared),
                  file=sys.stderr)
            return 2
        if base is None:
            base = str(frozen.get("base") or "").strip().lower() or None
            if base and not re.fullmatch(r"[0-9a-f]{40}", base):
                print("ERROR: the frozen claims.json names no usable base (%r)"
                      % base, file=sys.stderr)
                return 2
    counters = {}
    for claim, path, flag in (("C", args.c_counter, "--c-counter"),
                              ("CA", args.ca_counter, "--ca-counter")):
        if not path:
            continue
        path = os.path.abspath(path)
        if not os.path.isfile(path):
            print("ERROR: %s %s does not exist" % (flag, path), file=sys.stderr)
            return 2
        counters[claim] = path
    only = None
    if args.only:
        only = {x.strip() for x in args.only.split(",") if x.strip()}
        unknown = only - set(FIXTURES) - set(R1_PAIR)
        if unknown:
            print("ERROR: unknown fixture(s): %s" % ", ".join(sorted(unknown)),
                  file=sys.stderr)
            return 2
    if args.out:
        os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
        fh = open(args.out, "w", encoding="utf-8")
    else:
        fh = sys.stdout
    try:
        met, unmet = run(freeze, lands, base, only=only,
                         workroot=args.workroot, out_dir=args.out_dir,
                         keep=args.keep, baseline=not args.no_baseline,
                         out=fh, counters=counters,
                         synthetic=args.synthetic_config,
                         grade_it=not (args.no_grade or args.synthetic_config),
                         combined=combined)
    finally:
        if fh is not sys.stdout:
            fh.close()
    if args.out:
        print("wrote %s" % args.out)
    if args.no_grade or args.synthetic_config:
        return 0
    return 2 if unmet else 0


if __name__ == "__main__":
    sys.exit(main())
