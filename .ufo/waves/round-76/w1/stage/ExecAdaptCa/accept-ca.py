#!/usr/bin/env python3
r"""Round-76 calibration acceptance counter — claim Ca (freeze-pinned, ledger-driven).

Claim Ca (reports/round-76/claims.json, FROZEN at <freeze>) grades the round's
self-assessment-versus-repo-state ledger: statements filed by round 75 whose
stated token differs from the token the committed bytes carry at base
98c486bdb4650ba5b8e651d332910e8ee60ad121.  The counter is data-driven: the
ledger, every constant and every allowlist it needs are read from the FREEZE
commit (`git show <freeze>:<path>`), observations are recomputed in throwaway
clones, and the graded tree's copies of the config are only COMPARED (leg
FROZENCFG), never read.  Parent: reports/round-75/accept-ca.py (round 75).

CLI (graded form — the claim text prints this command in full)

  python3 -B reports/round-76/accept-ca.py --root . --lands <Ca-lands> \
      --freeze <freeze> --fleet-root /home/vgpnk/Projects/shokunin \
      --combined <C-lands> --work /fast/scratch/hyaku/kotodama-r76/<seat>
  python3 -B reports/round-76/accept-ca.py --selftest

  Run it inside a scratch clone of the lane whose local `main` is pinned to
  <Ca-lands> (equivalent: pass `--main <Ca-lands>`): STAMP requires
  stamped == evaluated == measured == <lands>, and `--main` (default "main")
  supplies `measured`.  `--combined <C-lands>` is REQUIRED — claim C lands
  after claim Ca in round 76 and the COMBINED leg grades the tree carrying both
  landings; a missing flag is a REFUSAL (exit 2), never a leg FAIL that would
  read as a red claim.

EXIT: 0 all twelve legs pass; 1 any leg fails; 2 input error or REFUSAL.
Refusals (exit 2, verdict line `ACCEPT-CA-76: FAIL legs=0/12 (refused: ...)`):
no scratch root at all (none of `--work`, `$HYAKU_SCRATCH`, `$TMPDIR` is set —
the counter never invents the system temp dir); `--combined` is missing; the
frozen leg table is not exactly the twelve implemented legs (LEGCOUNT);
`--lands` equals the frozen claims base; `freeze == lands` while every leg is
green (a do-nothing shape may not pass).

LEG SET (12 — the frozen claim Ca leg set; the table length is checked at freeze)

  LEDGER       committed at <freeze>; declares the frozen round / claim Ca /
               base; at least the frozen pair floor (>= 10) unique pairs; each
               pair structurally valid: argv observe_cmd whose executable is in
               the read-only allowlist {git, grep, wc, sha256sum, ls, cat, head,
               tail, cut} (interpreters and echo/printf/true-class constant
               printers are refused, shell metacharacters are refused, path
               operands must exist in the clone and 40-hex operands must be
               objects of it); compiling parse with a capture group;
               stated_text found at stated_at in the BASE tree (on that line,
               or on the fleet line at the fleet pin); stated token anchored in
               stated_text; and NO absence-observation pair (a `git grep -c|-l`
               count that reads 0 at base whose expected_after is a positive
               count).
  BASEMISMATCH at the base revision, in a clone materialized at base, every
               pair is red (stated token != observed token), none is
               unobservable, none is a parse-miss, count >= the frozen floor.
  REPAIR       every REPAIR pair: the truth observed in the clone at <lands> is
               observable; the statement re-read at <lands> (LAST regex match
               over statement_after.path) equals it; it differs from the base
               statement; the base stated_text is absent from that file at
               <lands>; the frozen after-state equals the re-read statement;
               the statement_after path is one of the frozen MUTABLE files;
               and stated_at is never a line claim C appends to (a README
               totals/footer line).  A frozen fixed_surfaces entry carrying
               `required` text must be present at <lands>, and one carrying a
               sha256 is pinned to it.
  ANNOTATE     every ANNOTATE pair has a row under SCORECARD.md
               "## Corrections — round <frozen round>" whose FIRST CELL is the
               pair id and which carries the base stated token and the observed
               token, boundary-matched; the pair's re-derivation command is
               RE-RUN inside the counter (at <lands>) and must return the
               observed token; a count pair (numeric expected_after) must pin
               the frozen base revision in its observe_cmd; and the pair's
               stated_at path is one of the frozen APPEND-ONLY files (an
               annotation on a mutable file would skip the repair it owes).
  APPENDONLY   base..<lands> has zero removed lines in the frozen protected
               set; when the ledger pins a fleet report, it is byte-identical to
               the blob its sha256 names and unchanged at fleet HEAD, with no
               uncommitted bytes under the fleet root;
               every changed line elsewhere is a REPAIR pair's stated_at line
               or an appended line; AND — the R1 EXEMPTION — in
               corpus/SOURCES.md a changed line on a PRE-EXISTING row is
               exempt ONLY when the change lies inside that row's status,
               recheck or used-by cell (the SOURCES contract's rule 2); every
               other changed line on a pre-existing row fails the leg.
  R1EXEMPT     the exemption is proved both ways: a tree whose only
               corpus/SOURCES.md delta versus base is a rule-2 cell edit on one
               pre-existing row grades APPENDONLY green, and a tree whose only
               delta is a teaches-cell (non-rule-2) edit on one pre-existing row
               grades APPENDONLY red; the committed receipts
               r1exempt-green.txt / r1exempt-red.txt carry the runs.
  NOSTUB       every correction row carries id + old token + new token + the
               re-derivation command (executable under the allowlist) and no
               placeholder token ({TODO, TBD, FIXME, XXX, n/a, ?} or <...>).
  SEPARABLE    read set exactly: the ledger at <freeze>, every corrections row
               that LEADS with a pair id, the telemetry receipts and controls
               named in this file's Ca section, and the stated_at line of every
               pair.  No byte in that set cites a lane S-id that is IN the
               frozen claim-C row set (read from claim C's row_set at
               <freeze>) or names the frozen claim-C path family; no stated_at
               path is in the frozen forbidden set; every observation is the
               token the pair's observe_cmd returns in the clone at the
               revision the ledger names.
  RECEIPTS     materializes a clone of the frozen round-75 claim-Ca lands
               012e8d3c8b92f47c734f735d58d118d574fe6a14, pins that clone's local
               main to it, re-runs accept-ca-75 inside it (with
               --freeze <round-75 freeze>, --combined <round-75 combined>,
               --fleet-root and a --work inside our own scratch root),
               requires exit 0 and the exact line
               `ACCEPT-CA-75: PASS legs=12/12`, and requires the committed
               accept-ca-75-at-lands.txt to carry that stdout verbatim
               (volatile clone roots of BOTH instruments normalized) with
               stamped==evaluated==measured==that revision and the round-75
               counter's sha256.
  COMBINED     at the REQUIRED `--combined <C-lands>` tree carrying BOTH
               landings (claim C's and claim Ca's), materialized: the frozen
               claim-C rows and entries are present, the claim-Ca corrections
               are present, and the R1-exempt APPENDONLY holds at that tree —
               the round-74 APPENDONLY conflict class is closed.  The receipt
               measures-ca-head.txt carries the run.
  FROZENCFG    every constant comes from `git show <freeze>:...`; <freeze> is
               a strict ancestor of <lands> on the first-parent chain (a
               `lands == freeze` run is graded, NOTE'd, and can never PASS); the
               frozen base is an ancestor of <freeze>; the graded tree's claims
               and ledger are byte-identical to the freeze blobs.
  STAMP        stamped/evaluated/measured/tree/counter-sha256 headers (QUALITY
               17/19 grammar of tools/check-receipt-seq.py), stamped == evaluated
               == measured == <lands>, tree == `git rev-parse <lands>^{tree}`,
               counter sha256 == this file, every observation inside the clone.

PREDICATE READING, STATED (the frozen text does not decide these)

  * "red at base" = stated token != observed token, so an ANNOTATE pair stays red
    at <lands> and is closed by its correction row, not by a repo change.
  * "the statement re-read at <lands> (last occurrence)" = the LAST regex match
    over statement_after.path.  The frozen REPAIR sentence names
    `statement_after` for every REPAIR pair, so a REPAIR pair without a
    statement_after object (path + compiling capture parse) fails LEDGER; there
    is no fallback to stated_at, because a fallback would grade a weaker pair
    than the frozen text.
  * a fixed-surface `required` string is a REQUIREMENT, not always a verbatim
    byte string: each ';'-separated clause passes when its whitespace-normalized
    text occurs in the file, or when every word of four or more characters in
    the clause occurs there.  The landing's prose is authored separately from
    the claim's description, but the clause's content words are still checked,
    so a missing addendum fails.
  * "shell metacharacters" (LEDGER) are refused in every argv element EXCEPT the
    grep / git-grep PATTERN operand: the counter executes an argv and never a
    shell, so a `|` or a backtick inside a pattern is regex data — the ledger's
    own README index-row and registry-status patterns require both — while a
    separator or redirection in every other element, and in every path or
    revision operand, stays refused.
  * the re-derivation command is executed as an argv (shlex.split, never a
    shell), so a backtick inside a quoted grep pattern is a literal pattern
    character and is admitted there; command separators and redirections stay
    refused.
  * the APPENDONLY exception set is the frozen fixed_surfaces list: an entry
    with an integer `line` exempts that line only (the REPAIR stated_at rule), an
    entry with a frozen sha256 is pinned to that digest, and an entry with
    neither is a whole-file exemption.  Round 76 declares no tool repair, so the
    REPAIR leg checks only the frozen `required` / `line` / `sha256` surfaces
    and keeps no re-run of an external instrument.
  * all scratch lives under --work, else $HYAKU_SCRATCH, else $TMPDIR; with none
    of the three set the counter REFUSES (exit 2) instead of inventing the
    system temp dir, and no scratch path of its own is hardcoded.  The
    round-75 counter re-run (RECEIPTS) receives --work and TMPDIR inside our own
    root, so its clones land there too; the round-75 instrument's internal
    receipt comparison is its own business.
  * "differs from the base statement" = the re-read token != the base token AND
    no line the statement_after parse matches still carries the base
    stated_text (shadow-append closed).  A dated prose mention elsewhere in the
    file is not a statement site and does not shadow it — corpus/README.md:805
    quotes the stale `## culture-material/ (36)` heading on purpose, and
    APPENDONLY forbids editing that record, so the whole-file reading would make
    the claim unsatisfiable.
  * correction rows are matched by LEADING id, never by a mention in prose.
  * "no absence-observation pair" is implemented on the count shape only.
  * "count pairs measure at the pinned base revision" = an ANNOTATE pair whose
    expected_after is numeric must carry the frozen base revision as an operand.
  * a REPAIR pair's observation MAY pin a revision (the frozen REPAIR text says
    "the observation re-run in a clone", which does not forbid a pin; the round
    76 ledger pins the base on purpose, so that claim C's new registry rows
    cannot move the observed figure).  The observation is still executed inside
    the clone materialized at <lands>.
  * the disposition is decided by the frozen file classes: a REPAIR pair's
    `statement_after` path must be in the frozen mutable-file list and an
    ANNOTATE pair's `stated_at` path must be in the frozen append-only list,
    both parsed from the frozen REPAIR / ANNOTATE leg text.  An annotation on a
    mutable file would otherwise be a way to skip the repair it owes, and a
    repair of a byte that APPENDONLY freezes would be unsatisfiable.
  * claim C's path family is a SET in round 76 (claim C admits calendar and era
    entries): SEPARABLE forbids every `<token>*` the frozen leg text names, and
    every printed line is redacted against that set and against the frozen
    claim-C lane row ids.
  * the APPENDONLY protected set is parsed from the frozen leg text.  Each
    entry carries a scope: "whole" (zero removed lines anywhere in the file) or
    "mark lines" (SHONEN.md's promotion-mark lines only: the `- [~]` / `- [x]`
    checklist items and the "Marks:" legend).  corpus/QUALITY.md is read as
    "whole": its existing criteria are append-only, so a removal anywhere in
    the file fails the leg while an insertion (a new criterion, or an addendum
    under an existing one) is an added line and passes.
  * corpus/SOURCES.md is compared SEMANTICALLY, row by row, by row id: a row
    present at base and at <lands> whose differing cells all lie in the
    status / recheck / used-by cells (located by the table's own header) is
    exempt; a row present at base and absent at <lands>, a row whose other
    cells differ, a row that does not parse to the header's cell count at
    either revision (an inserted delimiter, a changed indentation) and any
    changed non-row line of the file all fail.
  * "carrying BOTH landings" (COMBINED) = every frozen claim-C row id is
    present in corpus/SOURCES.md at that tree, every frozen claim-C entry path
    exists at that tree, the claim-Ca corrections section is present there with
    a row leading with every ANNOTATE pair id, and every REPAIR pair's
    re-read statement equals its observed truth there.
  * a `fleet:` stated_at (and an absolute path under the fleet root) is
    resolved in the fleet repository at its stated pin; the fleet repository is
    read with `git -C <fleet-root>`, which is the only `-C` the H2 guard
    admits, and the fleet root is the one given on the command line.
  * RECEIPTS compares the re-executed stdout with the committed receipt after
    normalizing volatile clone roots: our own work root, the round-75 counter's
    r75-ca- temp roots and any system-temp path either instrument prints.  The
    comparison is exact otherwise, so a re-run that prints a different verdict
    or a different stamped revision fails.
  * the fleet-report clause of APPENDONLY applies when the ledger pins one (a
    `fleet_pin` / `fleet_report`); a ledger that pins none carries the clause
    vacuously and the run says so in the leg detail.
  * token containment is boundary-matched, so `0` is never found inside a hash.

USAGE (graded)

  python3 -B reports/round-76/accept-ca.py --root . --lands <Ca-lands> \
      --freeze <freeze> --fleet-root /home/vgpnk/Projects/shokunin \
      --combined <C-lands> --work /fast/scratch/hyaku/kotodama-r76/<seat>
"""
import argparse
import glob as globmod
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

CLAIM = "Ca"
CLAIMS_REL = "reports/round-76/claims.json"
LEDGER_REL = "reports/round-76/ledger.json"
SCORECARD_REL = "SCORECARD.md"
TELEMETRY_DIR = "reports/round-76/telemetry"
FLEET_REPORT_DEFAULT = ""
MIN_PAIRS_FLOOR = 10
OBSERVE_ALLOW = ("git", "grep", "wc", "sha256sum", "ls", "cat", "head", "tail",
                 "cut")
GIT_READONLY = ("show", "ls-tree", "cat-file", "rev-parse", "log", "grep",
                "diff", "ls-files", "rev-list", "merge-base", "for-each-ref",
                "describe", "show-ref", "name-rev")
INTERPRETERS = ("python", "python2", "python3", "pypy", "pypy3", "sh", "bash",
                "zsh", "dash", "ksh", "fish", "csh", "tcsh", "perl", "node",
                "nodejs", "ruby", "php", "awk", "gawk", "mawk", "sed", "env",
                "xargs", "eval", "exec", "nice", "nohup", "time", "busybox")
SHELL_META = ("|", "&", ";", "<", ">", "`", "$(", "\n", "\r")
# the re-derivation command runs as an argv (shlex.split, never a shell), so a
# backtick inside a quoted grep pattern is literal there; separators and
# redirections stay refused.
REDERIVE_META = tuple(m for m in SHELL_META if m != "`")
STUB_TOKENS = {"todo", "tbd", "fixme", "xxx", "n/a", "?"}
STUB_ANGLE_RE = re.compile(r"<[^>]*>")
ABSENCE_EXPECT_RE = re.compile(r"^[1-9][0-9]*$")
PASS_LINES = {"accept-ca-75": "ACCEPT-CA-75: PASS legs=12/12"}
R75_COUNTERS = {"accept-ca-75": "reports/round-75/accept-ca.py"}
RECEIPT_TMP_RE = re.compile(r"/(?:var/)?tmp/[^\s:,\"']+")
RECEIPT_NESTED_RE = re.compile(r"(?<![\w./-])/(?:[^\s\"']*/)?r7[0-9]-ca-[^\s\"']*")
DISPOSITIONS = ("REPAIR", "ANNOTATE")
REQUIRED_LEGS = ("LEDGER", "BASEMISMATCH", "REPAIR", "ANNOTATE", "APPENDONLY",
                 "R1EXEMPT", "NOSTUB", "SEPARABLE", "RECEIPTS", "COMBINED",
                 "FROZENCFG", "STAMP")
SEPARABLE_SCAN_KEYS = ("observe_cmd", "expected_after", "parse", "rederive",
                       "stated_token", "stated_parse")
SID_RE = re.compile(r"(?<![A-Za-z0-9_])S(\d{3,})(?![0-9])")
STAMPED_RE = re.compile(r"^# stamped revision: ([0-9a-f]{40})\s*$", re.M)
EVAL_RE = re.compile(r"^# evaluated revision: ([0-9a-f]{40})\s*$", re.M)
MEASURED_RE = re.compile(r"^# measured revision \(lane main\): ([0-9a-f]{40})\s*$",
                         re.M)
TREE_RE = re.compile(r"^# tree: ([0-9a-f]{40})\s*$", re.M)
SHA_RE = re.compile(r"^# counter sha256 \(self\): ([0-9a-f]{64})\s*$", re.M)
OBSERVE_TIMEOUT = 120
GREP_ARG_OPTS = ("-e", "-f", "-m", "-A", "-B", "-C")

RUN_STATE = {"outside_clone": False, "work": None}

# rule 2 of the SOURCES contract: the only cells that may change in place.
RULE2_CELLS = ("status", "recheck", "used-by")
# the fleet root the H2 guard may name with `git -C` (set by the driver); `cfg`
# is the frozen configuration every printed detail is redacted against.
CTX = {"fleet_root": None, "root": None, "cfg": None}


class ScratchRefused(Exception):
    """No scratch root is available; the counter never invents one."""


# --------------------------------------------------------------------------
# primitives
# --------------------------------------------------------------------------
def scratch_dir(explicit=None):
    """The one scratch root: --work, else $HYAKU_SCRATCH, else $TMPDIR.

    With none of the three set the counter REFUSES (ScratchRefused) instead of
    falling back to the system temp dir: no run of this instrument may write
    scratch bytes nobody named."""
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


def _require_work():
    work = RUN_STATE.get("work")
    if not work:
        raise ScratchRefused("observation requested before a scratch root was set")
    return work


def git(root, *args, timeout=300):
    return subprocess.run(["git", "-C", str(root), *args],
                          capture_output=True, text=True, timeout=timeout)


def git_bytes(root, *args):
    return subprocess.run(["git", "-C", str(root), *args],
                          capture_output=True)


def show(root, rev, path):
    r = git(root, "show", "%s:%s" % (rev, path))
    if r.returncode != 0:
        return None
    return r.stdout


def norm(text):
    return " ".join((text or "").split())


def sensitive_literals(cfg):
    """The lane S-ids and the claim-C path-family names, from the frozen claims."""
    ids = ["S%d" % i for i in sorted(cfg.get("lane_row_ids") or [])]
    fams = list(cfg.get("c_families") or [])
    return [x for x in ids + fams if x]


def scrub(value, cfg):
    """No printed line may echo a lane S-id or the claim-C family literal."""
    out = str(value)
    for lit in sensitive_literals(cfg or {}):
        if lit in out:
            out = out.replace(lit, "<redacted>")
    return out


def sha256_bytes(data):
    if not isinstance(data, bytes):
        data = data.encode()
    return hashlib.sha256(data).hexdigest()


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
        # every printed line is redacted: this counter's own stdout is inside
        # the SEPARABLE read set once it is committed as a telemetry receipt.
        print("     %s" % scrub(detail, CTX.get("cfg") or {}))
    return bool(passed)


def note(text):
    print("     NOTE %s" % scrub(text, CTX.get("cfg") or {}))


def token_in(text, token):
    """Boundary-matched containment: `0` is not found inside a 40-hex hash."""
    if not token:
        return False
    return re.search(r"(?<![0-9A-Za-z_])%s(?![0-9A-Za-z_])"
                     % re.escape(token), text or "") is not None


def section_of(text, heading_re):
    lines = (text or "").splitlines()
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


def corr_heading_re(round_no):
    return re.compile(r"^##\s+Corrections\s*[\u2014\u2013-]\s*round\s+%d\b"
                      % int(round_no), re.I)


def correction_rows(scor, round_no):
    body = section_of(scor, corr_heading_re(round_no))
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


def row_starts_with_id(row, pid):
    """A row is evidence for a pair only when the pair id LEADS it (first table
    cell, or the list lead), never when it is merely mentioned."""
    s = (row or "").strip()
    if not s:
        return False
    if s.startswith("|"):
        cells = s.split("|")
        first = cells[1].strip() if len(cells) > 1 else ""
        first = first.strip("*`_ ").strip()
        return first == pid
    s2 = re.sub(r"^[-*+]\s+", "", s)
    s2 = s2.lstrip("*`_ ").strip()
    return re.match(r"%s(?![A-Za-z0-9_-])" % re.escape(pid), s2) is not None


def row_names_id(row, pid):
    return re.search(r"(?<![A-Za-z0-9_-])%s(?![A-Za-z0-9_-])" % re.escape(pid),
                     row or "") is not None


def changed_files(root, base, lands):
    """[(status, path)] for paths whose base..lands diff has ARITY != 0 removal
    via --numstat; status letters from --name-status."""
    r = git(root, "diff", "--name-status", "--no-renames", "%s..%s" % (base, lands))
    out = []
    for line in r.stdout.splitlines():
        parts = line.split("\t")
        if len(parts) >= 2:
            out.append((parts[0], parts[-1]))
    return out


def numstat_removed(root, rev_a, rev_b, paths):
    r = git(root, "diff", "--numstat", "--no-renames", "%s..%s" % (rev_a, rev_b),
            "--", *paths)
    total = 0
    for line in r.stdout.splitlines():
        parts = line.split()
        if len(parts) >= 2 and parts[1].isdigit():
            total += int(parts[1])
    return total, r.stdout


def materialize(root, rev, tmpdir, label):
    dest = os.path.join(tmpdir, label)
    r = git(root, "clone", "--quiet", "--no-checkout", os.path.abspath(root), dest)
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


# --------------------------------------------------------------------------
# corpus/SOURCES.md — the R1 exemption is decided on cells, not on lines
# --------------------------------------------------------------------------
CELL_SPLIT_RE = re.compile(r"(?<!\\)\|")
SOURCES_ROW_RE = re.compile(r"^\|\s*(S\d{3,})\s*\|")


def sources_cells(line):
    """The cells of one registry row (an escaped pipe stays inside its cell)."""
    parts = CELL_SPLIT_RE.split(line)
    if parts and not parts[0].strip():
        parts = parts[1:]
    if parts and not parts[-1].strip():
        parts = parts[:-1]
    return [p.strip().replace("\\|", "|") for p in parts]


def sources_header(text):
    """[(cell name, index)] from the registry's own header row."""
    for line in (text or "").splitlines():
        if re.match(r"^\|\s*id\s*\|", line):
            names = sources_cells(line)
            return [(n.lower(), i) for i, n in enumerate(names)]
    return []


def sources_rows(text):
    """{row id: (line number, cells)} for the registry rows of a file."""
    out = {}
    for n, line in enumerate((text or "").splitlines(), 1):
        m = SOURCES_ROW_RE.match(line)
        if not m:
            continue
        out[m.group(1)] = (n, sources_cells(line))
    return out


def sources_diff(root, base, lands):
    """The semantic delta of corpus/SOURCES.md between two revisions.

    Returns (rule2_edits, violations): rule2_edits lists the row ids whose
    only differing cells are the contract's rule-2 cells (status, recheck,
    used-by); violations lists human-readable problems (removed rows, rows
    whose other cells changed, changed non-row lines).
    """
    problems = []
    base_text = show(root, base, "corpus/SOURCES.md")
    lands_text = show(root, lands, "corpus/SOURCES.md")
    if base_text is None:
        return [], ["corpus/SOURCES.md is absent at base"]
    if lands_text is None:
        return [], ["corpus/SOURCES.md is absent at lands"]
    header = sources_header(base_text)
    rule2_idx = [i for name, i in header if name in RULE2_CELLS]
    if not rule2_idx:
        return [], ["corpus/SOURCES.md header names no %s cell"
                   % "/".join(RULE2_CELLS)]
    base_rows = sources_rows(base_text)
    lands_rows = sources_rows(lands_text)
    rule2_edits = []
    for rid, (_bln, bcells) in sorted(base_rows.items()):
        if rid not in lands_rows:
            problems.append("row %s present at base is absent at lands" % rid)
            continue
        _lln, lcells = lands_rows[rid]
        if len(bcells) != len(header) or len(lcells) != len(header):
            problems.append("row %s does not parse to the header's %d cells "
                            "(%d at base, %d at lands)"
                            % (rid, len(header), len(bcells), len(lcells)))
            continue
        n = max(len(bcells), len(lcells))
        differing = [i for i in range(n)
                     if (bcells[i] if i < len(bcells) else None) !=
                        (lcells[i] if i < len(lcells) else None)]
        outside = [i for i in differing if i not in rule2_idx]
        if not differing:
            continue
        if outside:
            names = [header[i][0] if i < len(header) else "cell%d" % i
                     for i in outside]
            problems.append("row %s changed outside the rule-2 cells (%s)"
                            % (rid, ", ".join(names)))
        else:
            rule2_edits.append(rid)
    # changed non-row lines (the header block, the legend) fail the leg
    base_lines = base_text.splitlines()
    lands_lines = lands_text.splitlines()
    lands_set = set(lands_lines)
    d = git(root, "diff", "-U0", "--no-color", "%s..%s" % (base, lands),
            "--", "corpus/SOURCES.md")
    removed = []
    for line in d.stdout.splitlines():
        m = re.match(r"^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@", line)
        if m:
            old_start = int(m.group(1))
            old_count = int(m.group(2) or 1)
            for i in range(old_start, old_start + old_count):
                if i - 1 < len(base_lines) and base_lines[i - 1] not in lands_set:
                    removed.append((i, base_lines[i - 1]))
    for n, text in removed:
        if SOURCES_ROW_RE.match(text):
            continue          # a removed row is reported by the row comparison
        problems.append("non-row line %d changed: %s" % (n, norm(text)[:60]))
    return rule2_edits, problems


# --------------------------------------------------------------------------
# frozen configuration (H1)
# --------------------------------------------------------------------------
def _leg_text(legs, name):
    for item in legs:
        if isinstance(item, str) and item.split(":", 1)[0].strip() == name:
            return item
    return ""


def leg_name_of(item):
    if not isinstance(item, str):
        return ""
    return item.split(":", 1)[0].strip()


def _protected_scopes(leg_text):
    """[(path, scope)] parsed from the frozen APPENDONLY protected set.

    scope "whole"     — zero removed lines anywhere in the file.
    scope "mark lines" — only the file's promotion-mark lines are protected.
    """
    if not leg_text:
        return []
    m = re.search(r"zero removed lines in (.*?)(?:;|\.$|$)", leg_text, re.S)
    if not m:
        return []
    clause = m.group(1)
    items = [x.strip() for x in re.split(r",| and ", clause) if x.strip()]
    out = []
    for item in items:
        pm = re.search(r"([A-Za-z0-9_./-]+\.(?:md|json))", item)
        if not pm:
            continue
        path = pm.group(1)
        if "mark line" in item.lower():
            scope = "mark lines"
        else:
            scope = "whole"
        if path not in [p for p, _ in out]:
            out.append((path, scope))
    return out


def _clause_paths(clause):
    """A ', '/` and `-separated path list from a frozen leg clause."""
    out = []
    for item in re.split(r",| and ", clause or ""):
        item = item.strip().strip("`")
        if item and item not in out:
            out.append(item)
    return out


def _shonen_mark_lines(text):
    """The promotion-mark lines of SHONEN.md (checklist items + Marks legend)."""
    lines = (text or "").splitlines()
    marks = set()
    in_legend = False
    for n, line in enumerate(lines, 1):
        if re.match(r"^\s*[-*+]\s*\[[ ~xX]\]", line):
            marks.add(n)
        if re.match(r"^\s*Marks:", line):
            in_legend = True
            marks.add(n)
            continue
        if in_legend:
            if not line.strip():
                in_legend = False
                continue
            marks.add(n)
    return marks


def load_frozen(root, freeze, claims_rel, ledger_rel):
    """(cfg, error).  Everything comes from `git show <freeze>:<path>`."""
    problems = []
    claims_raw = show(root, freeze, claims_rel)
    if claims_raw is None:
        return None, "claims file %s is not committed at --freeze %s" % (
            claims_rel, freeze)
    try:
        claims = json.loads(claims_raw)
    except ValueError as exc:
        return None, "claims JSON at --freeze: %s" % exc
    if not isinstance(claims, dict):
        return None, "claims file at --freeze is not an object"

    cfg = {"claims_rel": claims_rel, "ledger_rel": ledger_rel,
           "claims_raw": claims_raw, "problems": problems}
    cfg["round"] = claims.get("round")
    if not isinstance(cfg["round"], int):
        problems.append("claims round=%r is not an integer" % (cfg["round"],))
        cfg["round"] = 76
    base = claims.get("base")
    if not isinstance(base, str) or not re.fullmatch(r"[0-9a-f]{40}", base or ""):
        problems.append("claims base=%r is not 40-hex" % (base,))
        base = None
    cfg["base"] = base

    claim = None
    for item in claims.get("claims", []) or []:
        if isinstance(item, dict) and item.get("id") == CLAIM:
            claim = item
            break
    if claim is None:
        problems.append("claims file carries no claim %s" % CLAIM)
        claim = {}
    cfg["fixed_surfaces"] = [
        x for x in claim.get("fixed_surfaces", [])
        if isinstance(x, dict) and isinstance(x.get("path"), str)
    ]
    legs = claim.get("legs") if isinstance(claim.get("legs"), list) else []
    cfg["legs"] = legs
    names = [leg_name_of(x) for x in legs if leg_name_of(x)]
    cfg["leg_names"] = names
    if sorted(names) != sorted(REQUIRED_LEGS):
        problems.append("frozen leg set %s != the twelve implemented legs %s"
                        % (sorted(names), sorted(REQUIRED_LEGS)))
    ledger_rel_frozen = claim.get("ledger")
    if isinstance(ledger_rel_frozen, str) and ledger_rel_frozen.strip():
        cfg["ledger_rel"] = ledger_rel_frozen.strip()

    lt_ledger = _leg_text(legs, "LEDGER")
    m = re.search(r">=\s*(\d+)", lt_ledger)
    if not m:
        problems.append("LEDGER leg text carries no '>= N' pair floor")
        cfg["min_pairs"] = MIN_PAIRS_FLOOR
    else:
        cfg["min_pairs"] = max(MIN_PAIRS_FLOOR, int(m.group(1)))
    if cfg["min_pairs"] < MIN_PAIRS_FLOOR:
        problems.append("frozen pair floor %d below the hard floor %d"
                        % (cfg["min_pairs"], MIN_PAIRS_FLOOR))

    lt_sep = _leg_text(legs, "SEPARABLE")
    families = []
    for m in re.finditer(r"([a-z0-9][a-z0-9-]{5,})\*", lt_sep):
        if m.group(1) not in families:
            families.append(m.group(1))
    cfg["c_families"] = families
    if not families:
        problems.append("SEPARABLE leg text names no claim-C path family '<tok>*'")

    lt_app = _leg_text(legs, "APPENDONLY")
    cfg["protected_scopes"] = _protected_scopes(lt_app)
    cfg["protected"] = [p for p, _ in cfg["protected_scopes"]]
    if not cfg["protected"]:
        problems.append("APPENDONLY leg text names no protected file list")

    m = re.search(r"no stated_at path is (.*?)(?:;|$)", lt_sep, re.S)
    forbidden = []
    if m:
        for item in re.split(r",| or ", m.group(1)):
            item = item.strip().strip("`")
            if item:
                forbidden.append(item)
    cfg["separable_forbidden"] = forbidden
    if not forbidden:
        problems.append("SEPARABLE leg text names no forbidden stated_at paths")

    m = re.search(r"mutable files \(([^)]*)\)", _leg_text(legs, "REPAIR"))
    cfg["repair_mutable"] = _clause_paths(m.group(1)) if m else []
    if not cfg["repair_mutable"]:
        problems.append("REPAIR leg text names no frozen mutable-file list")
    m = re.search(r"append-only files \(([^)]*)\)",
                  _leg_text(legs, "ANNOTATE"))
    cfg["annotate_append"] = _clause_paths(m.group(1)) if m else []
    if not cfg["annotate_append"]:
        problems.append("ANNOTATE leg text names no frozen append-only-file list")

    lane_ids = set()
    claim_c = None
    for item in claims.get("claims", []) or []:
        if isinstance(item, dict) and item.get("id") == "C":
            claim_c = item
            break
    if claim_c:
        for row in claim_c.get("row_set") or []:
            rid = row.get("id") if isinstance(row, dict) else row
            m = re.fullmatch(r"S(\d{3,})", str(rid or ""))
            if m:
                lane_ids.add(int(m.group(1)))
    if not lane_ids:
        for m in re.finditer(r"S(\d{3,})", lt_sep):
            lane_ids.add(int(m.group(1)))
    cfg["lane_row_ids"] = sorted(lane_ids)
    if not lane_ids:
        problems.append("the frozen claim-C lane row set is not derivable "
                        "(claim C row_set and the SEPARABLE leg text are empty)")
    cfg["claim_c_entries"] = [p for p in (claim_c or {}).get("entries") or []
                              if isinstance(p, str)]
    cfg["claim_c_owned_inplace"] = [
        x for x in (claim_c or {}).get("owned_inplace") or []
        if isinstance(x, dict)
    ]

    ca_named = set()
    claim_text = json.dumps(claim, ensure_ascii=False)
    for item in re.findall(r"reports/round-[0-9]+/telemetry/[A-Za-z0-9_./-]+",
                           claim_text):
        ca_named.add(item.rstrip(".,;`)"))
    for item in re.findall(r"(?<![A-Za-z0-9_./-])([A-Za-z0-9_.-]+\.txt)\b",
                           claim_text):
        ca_named.add(TELEMETRY_DIR + "/" + item)
    cfg["ca_named_paths"] = sorted(ca_named)

    lt_rec = _leg_text(legs, "RECEIPTS")
    receipt_paths = {}
    for m in re.finditer(
            r"((?:[A-Za-z0-9_./-]*/)?accept-ca-75-at-[A-Za-z0-9_.-]+\.txt)",
            lt_rec):
        path = m.group(1)
        if "/" not in path:
            path = TELEMETRY_DIR + "/" + path
        receipt_paths["accept-ca-75"] = path
    cfg["receipt_paths"] = receipt_paths
    if set(receipt_paths) != set(PASS_LINES):
        problems.append("RECEIPTS leg text names %s, want the round-75 receipt"
                        % sorted(receipt_paths))
    m = re.search(r"round-75 claim-Ca lands\s+([0-9a-f]{40})", lt_rec) \
        or re.search(r"claim-Ca lands\s+([0-9a-f]{40})", lt_rec)
    cfg["receipts_rev"] = m.group(1) if m else None
    if not cfg["receipts_rev"]:
        problems.append("RECEIPTS leg text names no round-75 lands revision")
    m = re.search(r"--freeze\s+([0-9a-f]{40})", lt_rec)
    cfg["receipts_freeze"] = m.group(1) if m else None
    if not cfg["receipts_freeze"]:
        problems.append("RECEIPTS leg text names no round-75 freeze revision")
    m = re.search(r"--combined\s+([0-9a-f]{40})", lt_rec)
    cfg["receipts_combined"] = m.group(1) if m else None
    if not cfg["receipts_combined"]:
        problems.append("RECEIPTS leg text names no round-75 --combined revision")
    m = re.search(r"-B\s+([A-Za-z0-9_./-]+\.py)", lt_rec)
    cfg["receipts_counter"] = m.group(1) if m else R75_COUNTERS["accept-ca-75"]
    m = re.search(r"ACCEPT-CA-\d+: PASS legs=\d+/\d+", lt_rec)
    cfg["receipts_pass_line"] = m.group(0) if m else PASS_LINES["accept-ca-75"]
    if cfg["receipts_pass_line"] != PASS_LINES["accept-ca-75"]:
        problems.append("RECEIPTS leg text names the pass line %r, the counter "
                        "requires %r" % (cfg["receipts_pass_line"],
                                         PASS_LINES["accept-ca-75"]))

    lt_r1 = _leg_text(legs, "R1EXEMPT")
    r1_paths = {}
    for item in re.findall(r"([A-Za-z0-9_.-]*r1exempt-(?:green|red)\.txt)", lt_r1):
        key = "green" if "green" in item else "red"
        path = item if "/" in item else TELEMETRY_DIR + "/" + item
        r1_paths[key] = path
    cfg["r1_receipt_paths"] = r1_paths
    if set(r1_paths) != {"green", "red"}:
        problems.append("R1EXEMPT leg text names %s, want green and red receipts"
                        % sorted(r1_paths))

    lt_comb = _leg_text(legs, "COMBINED")
    m = re.search(r"([A-Za-z0-9_.-]*measures-ca-(?:head|combined)\.txt)", lt_comb)
    if m:
        path = m.group(1)
        cfg["combined_receipt_path"] = path if "/" in path \
            else TELEMETRY_DIR + "/" + path
    else:
        cfg["combined_receipt_path"] = TELEMETRY_DIR + "/measures-ca-combined.txt"
        problems.append("COMBINED leg text names no measures-ca-combined.txt receipt")

    ledger_raw = show(root, freeze, cfg["ledger_rel"])
    cfg["ledger_raw"] = ledger_raw
    ledger = None
    if ledger_raw is None:
        cfg["ledger"] = None
        cfg["ledger_meta"] = {}
    else:
        try:
            ledger = json.loads(ledger_raw)
        except ValueError as exc:
            cfg["ledger"] = None
            cfg["ledger_meta"] = {}
            problems.append("ledger JSON at --freeze: %s" % exc)
        if isinstance(ledger, list):
            cfg["ledger_meta"] = {"pairs": [p for p in ledger if isinstance(p, dict)]}
            ledger = cfg["ledger_meta"]
        elif isinstance(ledger, dict):
            cfg["ledger_meta"] = dict(ledger)
            cfg["ledger_meta"]["pairs"] = [p for p in ledger.get("pairs", [])
                                           if isinstance(p, dict)]
        else:
            cfg["ledger_meta"] = {}
            if ledger_raw is not None:
                problems.append("ledger at --freeze is neither object nor list")
        cfg["ledger"] = ledger
    return cfg, None


# --------------------------------------------------------------------------
# H2 observe guard
# --------------------------------------------------------------------------
def _inside_clone(clone, rel):
    if not clone or os.path.isabs(rel):
        return False
    root = os.path.normpath(clone)
    p = os.path.normpath(os.path.join(root, rel))
    return p == root or p.startswith(root + os.sep)


def _exists_in(clone, rel):
    if not _inside_clone(clone, rel):
        return False
    if any(c in rel for c in "*?["):
        return bool(globmod.glob(os.path.join(clone, rel)))
    return os.path.exists(os.path.join(clone, rel))


def _exists_in_repo(repo, rel, rev=None):
    """A path exists in `repo` (at `rev` when given)."""
    if rev:
        return git(repo, "cat-file", "-e", "%s:%s" % (rev, rel)).returncode == 0
    return os.path.exists(os.path.join(repo, rel))


def _resolve_in(clone, spec):
    """`<rev>:<path>` must resolve to an object of the clone."""
    return git(clone, "cat-file", "-e", spec).returncode == 0


def _bin(argv):
    return os.path.basename(argv[0]) if argv else ""


EMPTY_TREE = "4b825dc642cb6eb9a060e54bf8d69288fbee4904"
PATH_EXTS = (".md", ".txt", ".json", ".py", ".sh", ".yml", ".yaml", ".tsv")
GIT_GLOBAL_OPTS = ("-c", "--git-dir", "--work-tree", "--namespace",
                   "--exec-path", "--config-env")
REV_NAMES = ("HEAD", "HEAD^", "HEAD~1", "@")


def _git_rev_problem(clone, token):
    if re.fullmatch(r"[0-9a-f]{40}", token):
        if token == EMPTY_TREE:
            return None
        if git(clone, "cat-file", "-e", token).returncode != 0:
            return "git operand %s is not an object of the clone (dead pin)" % token
        return None
    if token in REV_NAMES:
        return None
    return None


def _mutable_ref(token):
    """A branch/tag-shaped operand where a revision is expected (ledger R3)."""
    if re.fullmatch(r"[0-9a-f]{40}", token) or token in REV_NAMES:
        return False
    if "/" in token or token.endswith(PATH_EXTS) or token.startswith(":"):
        return False
    return re.fullmatch(r"[A-Za-z][A-Za-z0-9_.-]*", token) is not None


def _pathspec_ok(token):
    if token in ("--", ".", ":/"):
        return True
    if token.startswith(":"):
        return True
    return any(ch in token for ch in "*?[")


def _fleet_root_ok(path):
    fleet = CTX.get("fleet_root")
    if not fleet or not path:
        return False
    try:
        return os.path.realpath(path) == os.path.realpath(fleet)
    except OSError:
        return False


def _split_fleet_c(args):
    """`git -C <fleet-root> ...` — the only `-C` the guard admits."""
    if len(args) >= 2 and args[0] == "-C":
        return args[2:], args[1]
    return args, None


def _git_problem(clone, args):
    if not args:
        return "git with no subcommand"
    args, fleet_dir = _split_fleet_c(args)
    repo = clone
    if fleet_dir is not None:
        if not _fleet_root_ok(fleet_dir):
            return ("git -C %r is refused (the counter fixes repo and cwd; only "
                    "the --fleet-root may be named)" % fleet_dir)
        repo = CTX["fleet_root"]
    idx = 0
    while idx < len(args) and args[idx].startswith("-"):
        if args[idx] in GIT_GLOBAL_OPTS:
            return "git option %r is refused (the counter fixes repo and cwd)" % args[idx]
        idx += 1
    if idx >= len(args):
        return "git with no subcommand"
    sub, rest = args[idx], args[idx + 1:]
    if sub not in GIT_READONLY:
        return "git subcommand %r not in the read-only allowlist %s" % (
            sub, sorted(GIT_READONLY))
    if sub == "grep":
        return _git_grep_problem(repo, rest)
    if sub == "diff":
        return _git_diff_problem(repo, rest)
    for a in rest:
        if a.startswith("-") or a == "--":
            continue
        if re.fullmatch(r"[0-9a-f]{40}", a) or a in REV_NAMES:
            why = _git_rev_problem(repo, a)
            if why:
                return why
            continue
        if _pathspec_ok(a):
            continue
        if ":" in a and not os.path.isabs(a):
            if not _resolve_in(repo, a):
                return "git operand %r does not resolve in the clone" % a
            continue
        if "/" in a or a.endswith(PATH_EXTS):
            if not _exists_in_repo(repo, a):
                return "git operand %r does not exist in the clone" % a
    return None


def _git_grep_problem(clone, args):
    """`git grep [opts] [-e] PATTERN [rev...] [--] paths...` role parsing."""
    pats, revs, i, have_e = [], [], 0, False
    while i < len(args):
        a = args[i]
        if a == "--":
            i += 1
            break
        if a.startswith("-") and len(a) > 1:
            if a in ("-e", "-f"):
                if i + 1 >= len(args):
                    return "git grep %s without an argument" % a
                if a == "-e":
                    pats.append(args[i + 1])
                    have_e = True
                i += 2
                continue
            i += 1
            continue
        if not pats and not have_e and not revs:
            pats.append(a)
            i += 1
            continue
        if re.fullmatch(r"[0-9a-f]{40}", a) or a in REV_NAMES:
            revs.append(a)
            i += 1
            continue
        if _mutable_ref(a):
            return "git grep revision operand %r is a mutable ref (pin a 40-hex or HEAD)" % a
        break
    if not pats:
        return "git grep has no pattern"
    for r in revs:
        why = _git_rev_problem(clone, r)
        if why:
            return why
    paths = [x for x in args[i:] if x != "--"]
    if not paths:
        return "git grep has no path operand (the counter never greps the whole tree)"
    for x in paths:
        if _pathspec_ok(x):
            continue
        if not _exists_in_repo(clone, x, revs[0] if revs else None):
            return "git grep path operand %r does not exist in the clone" % x
    return None


def _git_diff_problem(clone, args):
    revs, i = [], 0
    while i < len(args):
        a = args[i]
        if a == "--":
            i += 1
            break
        if a.startswith("-"):
            i += 1
            continue
        if re.fullmatch(r"[0-9a-f]{40}", a) or a in REV_NAMES:
            revs.append(a)
            i += 1
            continue
        if _mutable_ref(a):
            return "git diff revision operand %r is a mutable ref (pin a 40-hex or HEAD)" % a
        break
    for r in revs:
        why = _git_rev_problem(clone, r)
        if why:
            return why
    for x in args[i:]:
        if _pathspec_ok(x):
            continue
        if not _exists_in_repo(clone, x, revs[0] if revs else None):
            return "git diff path operand %r does not exist in the clone" % x
    return None


def _grep_problem(clone, args):
    pats, files, have_e, i = [], [], False, 0
    while i < len(args):
        a = args[i]
        if a == "--":
            files.extend(args[i + 1:])
            break
        if a.startswith("-") and len(a) > 1:
            if a in GREP_ARG_OPTS:
                if a == "-e":
                    if i + 1 >= len(args):
                        return "grep -e without a pattern"
                    pats.append(args[i + 1])
                    have_e = True
                i += 2
                continue
            i += 1
            continue
        if not pats and not files and not have_e:
            pats.append(a)
        else:
            files.append(a)
        i += 1
    if not pats:
        return "grep has no pattern"
    if not files:
        return "grep has no file operand (stdin is not available)"
    for f in files:
        if f == "-":
            return "grep operand '-' (stdin) is refused"
        if not _exists_in(clone, f):
            return "grep file operand %r does not exist in the clone" % f
    return None


def _paths_problem(clone, args, need_one=True):
    paths = [a for a in args if not a.startswith("-")]
    if need_one and not paths:
        return "no path operand"
    for a in paths:
        if a == "-":
            return "stdin operand '-' is refused"
        if not _exists_in(clone, a):
            return "path operand %r does not exist in the clone" % a
    return None


def _grep_pattern_indices(binary, args):
    """The argv indices that carry grep PATTERN data (never code).

    `grep`/`git grep` receive a pattern as the argument of -e/--regexp or as the
    first bare operand; a metacharacter there is regex data because the counter
    executes an argv and never a shell."""
    out = set()
    i = 0
    if binary == "git":
        if not args or args[0] != "grep":
            return out
        i = 1
    elif binary != "grep":
        return out
    have_pattern = False
    while i < len(args):
        a = args[i]
        if a == "--":
            break
        if a.startswith("-") and len(a) > 1:
            if a in ("-e", "--regexp"):
                if i + 1 < len(args):
                    out.add(i + 1)
                    have_pattern = True
                i += 2
                continue
            if a in ("-f", "--file"):
                i += 2
                continue
            i += 1
            continue
        if not have_pattern:
            out.add(i)
            have_pattern = True
        i += 1
    return out


def observe_problem(argv, clone, rederive=False):
    """Static + dynamic H2 guard.  Static shape is clone-independent; the dynamic
    half resolves operands inside `clone` (the base clone for the LEDGER leg).

    `rederive=True` grades a re-derivation command, which the counter executes
    as an argv and never through a shell: a backtick is then a literal pattern
    character (the ledger's own README index-row pattern needs one)."""
    if isinstance(argv, str):
        return "observe_cmd is a shell string, not an argv list"
    if not isinstance(argv, list) or not argv:
        return "observe_cmd is not a non-empty argv list"
    for a in argv:
        if not isinstance(a, str) or not a:
            return "observe_cmd element is not a non-empty string"
    binary = _bin(argv)
    patterns = _grep_pattern_indices(binary, argv[1:])
    meta = REDERIVE_META if rederive else SHELL_META
    for idx, a in enumerate(argv):
        if idx and (idx - 1) in patterns:
            continue
        for bad in meta:
            if bad in a:
                return "shell construct %r in argv element %r" % (bad, a[:60])
    if binary in INTERPRETERS:
        return "interpreter/constant-printer binary %r is refused (H2)" % argv[0]
    if binary not in OBSERVE_ALLOW:
        return ("argv[0] %r not in the observe allowlist %s (the echo/printf/"
                "interpreter channels are closed)" % (argv[0], list(OBSERVE_ALLOW)))
    return _observe_operands_problem(binary, argv[1:], clone)


def _observe_operands_problem(binary, args, clone):
    if clone is None:
        return None
    if binary == "git":
        return _git_problem(clone, args)
    if binary == "grep":
        return _grep_problem(clone, args)
    if binary == "ls":
        return _paths_problem(clone, args, need_one=False)
    return _paths_problem(clone, args, need_one=True)


def observe_shape_problem(argv):
    """Clone-independent half of the guard (used when no clone exists yet)."""
    return observe_problem(argv, None)


def _child_env(tmpdir):
    """The closed environment of an observation or a child instrument.

    TMPDIR is the caller's scratch root: a child never inherits an ambient one,
    and nothing here names a system temp dir of its own."""
    return {
        "PATH": os.environ.get("PATH", "/usr/local/bin:/usr/bin:/bin"),
        "HOME": os.environ.get("HOME") or tmpdir,
        "TMPDIR": tmpdir,
        "LC_ALL": "C.UTF-8",
        "LANG": "C.UTF-8",
        "TZ": "UTC",
        "GIT_CONFIG_NOSYSTEM": "1",
        "GIT_TERMINAL_PROMPT": "0",
        "GIT_NO_REPLACE_OBJECTS": "1",
    }


def run_observe(clone_path, argv, cwd_is_clone=True):
    if not cwd_is_clone:
        RUN_STATE["outside_clone"] = True
    env = _child_env(_require_work())
    try:
        p = subprocess.run(argv, cwd=clone_path, capture_output=True, text=True,
                           timeout=OBSERVE_TIMEOUT, env=env)
    except FileNotFoundError:
        return None, "missing-binary:%s" % argv[0]
    except subprocess.TimeoutExpired:
        return None, "timeout:%ss" % OBSERVE_TIMEOUT
    except OSError as exc:
        return None, "os-error:%s" % exc
    if p.stdout.strip() == "" and p.returncode != 0:
        if _absence_observation(argv) and p.returncode == 1:
            return "0", "exit=1 (zero matches)"
        return None, "empty-stdout-exit=%d" % p.returncode
    return p.stdout, "exit=%d" % p.returncode


def _absence_observation(argv):
    """True for `git grep -c|-l ...` argv shapes (ledger grammar R1)."""
    if not isinstance(argv, list) or len(argv) < 3:
        return False
    if os.path.basename(argv[0]) != "git":
        return False
    args = argv[1:]
    if args and args[0] == "-C":
        args = args[2:]
    if len(args) < 2 or args[0] != "grep":
        return False
    return any(a in ("-c", "-l", "--count", "--files-with-matches")
               for a in args[1:])


def observed_raw(pair, clone_path):
    """The raw normalized stdout, parse ignored (absence-pair detection)."""
    why = observe_problem(pair.get("observe_cmd"), clone_path)
    if why:
        return None
    out, why = run_observe(clone_path, pair["observe_cmd"])
    return norm(out) if out is not None else None


def parse_observed(pair, out):
    """Parse one observe result to its typed token."""
    parse = pair.get("parse")
    if parse == "count-presence":
        m = re.search(r":([0-9]+)$", out.strip())
        if not m:
            return None, False, "count-presence parse-miss"
        return ("present" if int(m.group(1)) else "absent"), True, ""
    if parse:
        try:
            rx = re.compile(parse, re.M | re.S)
        except re.error as exc:
            return None, False, "parse:%s" % exc
        m = rx.search(out)
        if m:
            tok = norm(m.group(1) if m.groups() else m.group(0))
            if not tok:
                return None, False, "empty-token"
            return tok, True, ""
        return None, False, "parse-miss"
    tok = norm(out)[:200]
    if not tok:
        return None, False, "empty-token"
    return tok, True, ""


def observed_token(pair, clone_path):
    """(token, parsed, why). An empty token is unobservable: fail closed."""
    why = observe_problem(pair.get("observe_cmd"), clone_path)
    if why:
        return None, False, "invalid-observe_cmd:%s" % why
    out, why = run_observe(clone_path, pair["observe_cmd"])
    if out is None:
        return None, False, why
    token, parsed, parse_why = parse_observed(pair, out)
    return token, parsed, parse_why or why


def stated_token(pair):
    if pair.get("stated_parse"):
        try:
            m = re.search(pair["stated_parse"], pair.get("stated_text") or "", re.M)
        except re.error as exc:
            return None, False, "stated_parse:%s" % exc
        if m:
            tok = norm(m.group(1) if m.groups() else m.group(0))
            return (tok, True) if tok else (None, False)
        return None, False
    if pair.get("stated_token"):
        return norm(pair["stated_token"]), True
    tok = norm(pair.get("stated_text") or "")
    return (tok, True) if tok else (None, False)


def rederive_text(pair):
    if pair.get("rederive"):
        return norm(pair["rederive"])
    return norm(shlex.join(pair["observe_cmd"]))


def rederive_argv(pair):
    raw = pair.get("rederive") or shlex.join(pair["observe_cmd"])
    try:
        return shlex.split(raw), None
    except ValueError as exc:
        return None, "shlex:%s" % exc


def statement_after(pair, clone_path):
    """Read the declared statement_after file and return its last parsed token."""
    spec = pair.get("statement_after")
    if not isinstance(spec, dict):
        return None, False, "statement_after object required"
    path = spec.get("path")
    parse = spec.get("parse")
    if not isinstance(path, str) or not path:
        return None, False, "statement_after.path missing"
    if not isinstance(parse, str) or not parse:
        return None, False, "statement_after.parse missing"
    try:
        with open(os.path.join(clone_path, path), encoding="utf-8") as fh:
            text = fh.read()
    except OSError:
        return None, False, "statement_after path %s unreadable at lands" % path
    try:
        rx = re.compile(parse, re.M)
    except re.error as exc:
        return None, False, "statement_after.parse: %s" % exc
    matches = list(rx.finditer(text))
    if not matches:
        return None, False, "statement_after no-match in %s" % path
    m = matches[-1]
    tok = norm(m.group(1) if m.groups() else m.group(0))
    if not tok:
        return None, False, "statement_after empty token"
    return tok, True, ""


def evaluate_pairs(pairs, base_clone, lands_clone):
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


# --------------------------------------------------------------------------
# legs
# --------------------------------------------------------------------------
def leg_ledger(out, cfg, pairs, base_clone, ev):
    """Frozen sentence: committed at freeze, the frozen round / claim Ca / base,
    >= 10 unique pairs, structurally valid (argv over the read-only allowlist, no
    interpreters or constant printers, no shell metacharacters, compiling
    capture regex, stated_text found at stated_at in the BASE tree, stated
    token anchored), and NO absence-observation pair."""
    problems = []
    min_pairs = cfg["min_pairs"]
    meta = cfg.get("ledger_meta") or {}
    if cfg.get("ledger_raw") is None:
        return leg(out, "LEDGER", False,
                   "ledger %s is not committed at the --freeze commit; a worktree "
                   "copy is never read" % cfg["ledger_rel"])
    if meta.get("round") != cfg["round"]:
        problems.append("round=%r != frozen round %r"
                        % (meta.get("round"), cfg["round"]))
    if meta.get("claim") != CLAIM:
        problems.append("claim=%r" % (meta.get("claim"),))
    if meta.get("base") != cfg.get("base"):
        problems.append("ledger base=%r != frozen base %r"
                        % (meta.get("base"), cfg.get("base")))
    if len(pairs) < min_pairs:
        problems.append("pairs=%d < min-pairs=%d" % (len(pairs), min_pairs))
    seen = set()
    for idx, pair in enumerate(pairs):
        tag = pair.get("id") if isinstance(pair.get("id"), str) else "#%d" % idx
        pid = pair.get("id")
        if not isinstance(pid, str) or not pid.strip():
            problems.append("%s: empty id" % tag)
        elif pid in seen:
            problems.append("%s: duplicate id" % pid)
        else:
            seen.add(pid)
        if pair.get("disposition") not in DISPOSITIONS:
            problems.append("%s: disposition=%r" % (tag, pair.get("disposition")))
        why = observe_problem(pair.get("observe_cmd"), base_clone["path"])
        if why:
            problems.append("%s: %s" % (tag, why))
        if pair.get("parse") is None:
            problems.append("%s: parse missing (a compiling regex with a capture group, or count-presence, is required)" % tag)
        if "parse" in pair and pair["parse"] is not None:
            if not isinstance(pair["parse"], str):
                problems.append("%s: parse is not a string" % tag)
            elif pair["parse"] == "count-presence":
                pass
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
        class_site = classify_stated_at(cfg, pair)
        if pair.get("disposition") == "REPAIR":
            spec = pair.get("statement_after")
            spath = spec.get("path") if isinstance(spec, dict) else None
            mutable = cfg.get("repair_mutable") or []
            if mutable and isinstance(spath, str) and spath \
                    and spath not in mutable:
                problems.append("%s: REPAIR statement_after path %s is not one of "
                                "the frozen mutable files %s"
                                % (tag, spath, mutable))
        elif pair.get("disposition") == "ANNOTATE":
            append_only = cfg.get("annotate_append") or []
            spath = class_site[1] if class_site else None
            if append_only and spath and spath not in append_only:
                problems.append("%s: ANNOTATE stated_at path %s is not one of the "
                                "frozen append-only files %s"
                                % (tag, spath, append_only))
        if pair.get("disposition") == "REPAIR":
            spec = pair.get("statement_after")
            if not isinstance(spec, dict):
                problems.append("%s: REPAIR without a statement_after object "
                                "(the frozen REPAIR sentence names it)" % tag)
            else:
                path = spec.get("path")
                parse = spec.get("parse")
                if not isinstance(path, str) or not path:
                    problems.append("%s: statement_after.path missing" % tag)
                elif not _exists_in(base_clone["path"], path):
                    problems.append("%s: statement_after path %s absent at base"
                                    % (tag, path))
                if not isinstance(parse, str) or not parse:
                    problems.append("%s: statement_after.parse missing" % tag)
                else:
                    try:
                        rx = re.compile(parse)
                    except re.error as exc:
                        problems.append("%s: statement_after.parse: %s"
                                        % (tag, exc))
                    else:
                        if not rx.groups:
                            problems.append("%s: statement_after.parse has no "
                                            "capture group" % tag)
        # the statement site: lane path:line, or a fleet site
        site = classify_stated_at(cfg, pair)
        if site is None:
            problems.append("%s: stated_at=%r is neither path:line nor a fleet "
                            "site" % (tag, pair.get("stated_at")))
        else:
            fleet, path, line_no = site
            if fleet:
                pin = fleet_pin_for(cfg, pair)
                body = show(cfg["fleet_root"], pin, path)
                if body is None:
                    problems.append("%s: fleet statement path %s absent at pin %s"
                                    % (tag, path, pin[:12]))
                else:
                    lines = body.splitlines()
                    if line_no < 1 or line_no > len(lines):
                        problems.append("%s: fleet stated_at line %r out of range"
                                        % (tag, line_no))
                    else:
                        st = norm(pair.get("stated_text") or "")
                        if not st:
                            problems.append("%s: empty stated_text" % tag)
                        elif st not in norm(body):
                            problems.append("%s: stated_text not found in %s at "
                                            "the fleet pin" % (tag, path))
                        elif st not in norm(lines[line_no - 1]):
                            problems.append("%s: stated_text is in %s but NOT on "
                                            "line %d" % (tag, path, line_no))
            else:
                body = show(base_clone["path"], "HEAD", path)
                if body is None:
                    problems.append("%s: stated_at path %s absent at base"
                                    % (tag, path))
                else:
                    lines = body.splitlines()
                    if line_no < 1 or line_no > len(lines):
                        problems.append("%s: stated_at %s:%d beyond EOF (%d lines)"
                                        % (tag, path, line_no, len(lines)))
                    else:
                        st = norm(pair.get("stated_text") or "")
                        if not st:
                            problems.append("%s: empty stated_text" % tag)
                        elif st not in norm(body):
                            problems.append("%s: stated_text not found in %s at base"
                                            % (tag, path))
                        elif st not in norm(lines[line_no - 1]):
                            problems.append("%s: stated_text is in %s but NOT on "
                                            "line %d" % (tag, path, line_no))
        tok, ok = stated_token(pair)
        if not ok:
            problems.append("%s: stated token cannot be derived from stated_text"
                            % tag)
        elif tok is not None and norm(pair.get("stated_text") or ""):
            if tok not in norm(pair.get("stated_text") or ""):
                problems.append("%s: stated token %r not anchored in "
                                "stated_text" % (tag, scrub(tok[:40], cfg)))
        rec = pair.get("observed_at_base")
        if rec is not None and not isinstance(rec, str):
            problems.append("%s: observed_at_base is not a string" % tag)
        exp = norm(pair.get("expected_after") or "")
        argv = pair.get("observe_cmd")
        if ABSENCE_EXPECT_RE.match(exp) and isinstance(argv, list) \
                and _absence_observation(argv):
            raw = observed_raw(pair, base_clone["path"])
            if raw is not None and raw == "0":
                problems.append("%s: absence-observation pair (base count 0, "
                                "expected_after %r)" % (tag, exp))
    detail = "pairs=%d min=%d source=freeze" % (len(pairs), min_pairs)
    if problems:
        detail += " problems=%d %s" % (len(problems), problems[:8])
    return leg(out, "LEDGER", not problems, detail)


def classify_stated_at(cfg, pair):
    """(fleet?, path, line) for a pair's statement site.

    Lane sites are "path:line".  Fleet sites are "fleet:path:line", an
    absolute path under the fleet root, or a `stated_fleet` object."""
    stated_at = pair.get("stated_at") or ""
    spec = pair.get("stated_fleet")
    fleet_root = cfg.get("fleet_root")
    if isinstance(spec, dict):
        path = spec.get("path")
        line = spec.get("line")
        if isinstance(path, str) and path and isinstance(line, int):
            return True, path.lstrip("/"), line
        return None
    m = re.match(r"^fleet:(.+):(\d+)$", stated_at)
    if m:
        return True, m.group(1).lstrip("/"), int(m.group(2))
    if os.path.isabs(stated_at.split(":")[0]) and fleet_root:
        m = re.match(r"^(.+):(\d+)$", stated_at)
        if m:
            ap = os.path.realpath(m.group(1))
            if ap.startswith(os.path.realpath(fleet_root) + os.sep):
                rel = os.path.relpath(ap, os.path.realpath(fleet_root))
                return True, rel, int(m.group(2))
    m = re.match(r"^(.+):(\d+)$", stated_at)
    if m:
        return False, m.group(1), int(m.group(2))
    return None


def fleet_pin_for(cfg, pair):
    spec = pair.get("stated_fleet")
    if isinstance(spec, dict) and isinstance(spec.get("pin"), str) \
            and re.fullmatch(r"[0-9a-f]{40}", spec["pin"]):
        return spec["pin"]
    pin = (cfg.get("ledger_meta") or {}).get("fleet_pin")
    if isinstance(pin, str) and re.fullmatch(r"[0-9a-f]{40}", pin):
        return pin
    return "HEAD"


def leg_basemismatch(out, cfg, pairs, ev):
    min_pairs = cfg["min_pairs"]
    red, green, unobservable, misses = [], [], [], []
    for idx, pair in enumerate(pairs):
        pid = pair.get("id")
        tok = ev[idx]["stated"]
        obs, parsed, why = ev[idx]["base"]
        if obs is None:
            unobservable.append("%s:%s" % (pid, why))
            continue
        if not parsed:
            misses.append("%s:%s" % (pid, why))
        if not ev[idx]["stated_ok"] or tok is None:
            unobservable.append("%s:no-stated-token" % pid)
            continue
        if norm(tok) != norm(obs):
            red.append(pid)
        else:
            green.append(pid)
        rec = pair.get("observed_at_base")
        if isinstance(rec, str):
            lead = (rec.split() or [""])[0]
            if norm(lead) != norm(obs):
                misses.append("%s:recorded-observed-at-base=%r!=%r"
                              % (pid, scrub(rec[:40], cfg),
                                 scrub(obs[:40], cfg)))
    passed = (not unobservable) and (not green) and (not misses) \
        and len(red) >= min_pairs
    detail = "red=%d min=%d ids=%s" % (len(red), min_pairs, red)
    if green:
        detail += " green-at-base=%s" % green
    if misses:
        detail += " unobserved/miss=%s" % misses
    if unobservable:
        detail += " unobservable=%s" % unobservable
    return leg(out, "BASEMISMATCH", passed, detail)


def _c_appended_line(cfg, pair, base_text):
    """A REPAIR pair may never read a line claim C appends to: the index rows
    and the counts footer of a README (the assignment's gloss of the frozen
    sentence)."""
    m = re.match(r"^(.+):(\d+)$", pair.get("stated_at") or "")
    if not m:
        return False
    path, line_no = m.group(1), int(m.group(2))
    if os.path.basename(path) != "README.md":
        return False
    if base_text is None:
        return True
    anchors = [i for i, l in enumerate(base_text.splitlines(), 1)
               if l.startswith("Total knowledge entries:")
               or re.match(r"^##\s", l)]
    if not anchors:
        return False
    return line_no >= max(anchors)


def leg_repair(out, cfg, pairs, ev):
    red, unobservable, green = [], [], []
    for idx, pair in enumerate(pairs):
        if pair.get("disposition") != "REPAIR":
            continue
        pid = pair.get("id")
        m = re.match(r"^(.+):(\d+)$", pair.get("stated_at") or "")
        base_text = show(cfg["root"], cfg["base"], m.group(1)) if m else None
        if _c_appended_line(cfg, pair, base_text):
            red.append("%s(stated_at line is a claim-C appended line)" % pid)
            continue
        obs, parsed, why = ev[idx]["lands"]
        if obs is None:
            unobservable.append("%s:%s" % (pid, why))
            continue
        tok, found, swhy = ev[idx]["stmt_after"]
        if not found:
            red.append("%s(%s)" % (pid, swhy))
            continue
        stated = ev[idx]["stated"] or ""
        if norm(tok) != norm(obs):
            red.append("%s(statement=%r truth=%r)"
                       % (pid, scrub(tok[:40], cfg), scrub(obs[:40], cfg)))
            continue
        if norm(tok) == norm(stated):
            red.append("%s(statement unchanged from base %r)"
                       % (pid, scrub(stated[:40], cfg)))
            continue
        spec = pair.get("statement_after")
        path = spec.get("path") if isinstance(spec, dict) else None
        if not path:
            mm = re.match(r"^(.+):(\d+)$", pair.get("stated_at") or "")
            path = mm.group(1) if mm else ""
        lands_text = show(cfg["root"], cfg["lands"], path)
        if lands_text is None:
            red.append("%s(statement path %s unreadable at lands)" % (pid, path))
            continue
        stext = norm(pair.get("stated_text") or "")
        if stext:
            parse = spec.get("parse") if isinstance(spec, dict) else None
            try:
                rx = re.compile(parse) if isinstance(parse, str) else None
            except re.error:
                rx = None
            if rx is None:
                if stext in norm(lands_text):
                    red.append("%s(base stated_text still present in %s)"
                               % (pid, path))
                    continue
            else:
                hits = [norm(m.group(0)) for m in rx.finditer(lands_text)]
                if any(stext in h for h in hits):
                    red.append("%s(base stated_text still on a statement line "
                               "in %s)" % (pid, path))
                    continue
        if norm(pair.get("expected_after")) != norm(tok):
            red.append("%s(expected_after=%r != statement=%r)"
                       % (pid, scrub(pair.get("expected_after")[:40], cfg),
                          scrub(tok[:40], cfg)))
            continue
        green.append(pid)
    for item in cfg.get("fixed_surfaces") or []:
        path = item.get("path")
        required = item.get("required")
        if isinstance(path, str) and isinstance(required, str):
            text = show(cfg["root"], cfg["lands"], path)
            line_no = item.get("line")
            if line_no:
                lines = text.splitlines() if text is not None else []
                text = lines[line_no - 1] if 1 <= line_no <= len(lines) else None
            if not _required_ok(required, text):
                red.append("fixed-surface %s missing the required text %r"
                           % (path, required[:60]))
    detail = "green=%s red=%s" % (green, red)
    if unobservable:
        detail += " unobservable=%s" % unobservable
    return leg(out, "REPAIR", not red and not unobservable, detail)


def _annotate_rows(cfg, scor):
    rows = correction_rows(scor, cfg["round"])
    return rows


def leg_annotate(out, cfg, pairs, ev, scor, lands_clone):
    annotate = [(i, p) for i, p in enumerate(pairs)
                if p.get("disposition") == "ANNOTATE"]
    if not annotate:
        return leg(out, "ANNOTATE", True, "annotate-pairs=0 (vacuous)")
    if scor is None:
        return leg(out, "ANNOTATE", False, "SCORECARD.md unreadable at lands")
    rows = _annotate_rows(cfg, scor)
    if rows is None:
        return leg(out, "ANNOTATE", False,
                   "no '## Corrections — round %d' section; annotate-pairs=%d"
                   % (cfg["round"], len(annotate)))
    unannotated = []
    for idx, pair in annotate:
        pid = pair.get("id")
        tok = ev[idx]["stated"]
        obs, parsed, why = ev[idx]["lands"]
        if obs is None or tok is None:
            unannotated.append("%s(unobservable:%s)" % (pid, why))
            continue
        if re.fullmatch(r"\d+", norm(pair.get("expected_after") or "")):
            argv = pair.get("observe_cmd") or []
            if cfg.get("base") not in [a for a in argv if isinstance(a, str)]:
                unannotated.append("%s(count pair does not pin the base revision)"
                                   % pid)
                continue
        mine = [r for r in rows if row_starts_with_id(r, pid)]
        hit = [r for r in mine
               if token_in(norm(r), norm(tok)) and token_in(norm(r), norm(obs))]
        if not hit:
            unannotated.append("%s(row-leading-%s stated=%r observed=%r)"
                               % (pid, pid, scrub(norm(tok)[:40], cfg),
                                  scrub(norm(obs)[:40], cfg)))
            continue
        argv, why_argv = rederive_argv(pair)
        if argv is None:
            unannotated.append("%s(rederive %s)" % (pid, why_argv))
            continue
        why = observe_problem(argv, lands_clone["path"], rederive=True)
        if why:
            unannotated.append("%s(rederive not executable: %s)" % (pid, why))
            continue
        out_text, why = run_observe(lands_clone["path"], argv)
        if out_text is None:
            unannotated.append("%s(rederive %s)" % (pid, why))
            continue
        replay, replayed, replay_why = parse_observed(pair, out_text)
        if not replayed or norm(replay) != norm(obs):
            unannotated.append("%s(rederive token %r != observed %r; %s)"
                               % (pid, scrub(norm(replay or "")[:30], cfg),
                                  scrub(norm(obs)[:30], cfg), replay_why))
    return leg(out, "ANNOTATE", not unannotated,
               "rows=%d annotate-pairs=%d unannotated=%d %s"
               % (len(rows), len(annotate), len(unannotated), unannotated))


def _hunk_ranges(root, base, lands, path):
    """[(old_start, old_count, new_start, new_count)] for -U0 hunks."""
    d = git(root, "diff", "-U0", "--no-color", "%s..%s" % (base, lands),
            "--", path)
    out = []
    for line in d.stdout.splitlines():
        m = re.match(r"^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@", line)
        if m:
            out.append((int(m.group(1)), int(m.group(2) or 1),
                        int(m.group(3)), int(m.group(4) or 1)))
    return out


def _removed_base_lines(root, base, lands, path):
    """The base line numbers that base..lands removes or replaces in `path`."""
    out = []
    for old_start, old_count, _ns, _nc in _hunk_ranges(root, base, lands, path):
        for line_no in range(old_start, old_start + old_count):
            out.append(line_no)
    return out


def _protected_removals(root, cfg, path, scope):
    """The removed base lines of `path` that fall inside its protected scope."""
    base, lands = cfg["base"], cfg["lands"]
    removed = _removed_base_lines(root, base, lands, path)
    if scope == "whole":
        return removed
    if scope == "mark lines":
        base_text = show(root, base, path)
        marks = _shonen_mark_lines(base_text)
        return [n for n in removed if n in marks]
    return removed


def leg_appendonly(out, root, cfg, pairs, fleet_root):
    """Frozen sentence: zero removed lines in the frozen protected set; when
    the ledger pins a fleet report, that report at its fleet_pin is
    byte-identical to the blob its sha256 names and this lane writes no byte
    under the fleet root; every changed line elsewhere is a REPAIR pair's
    stated_at line or an appended line; and in corpus/SOURCES.md a changed line
    on a pre-existing row is exempt ONLY when the change lies inside that row's
    status / recheck / used-by cell (the R1 exemption)."""
    base, lands = cfg["base"], cfg["lands"]
    problems = []
    scopes = cfg.get("protected_scopes") or []
    if not scopes:
        problems.append("no protected file list derived from the frozen leg")
    protected_paths = [p for p, _ in scopes]
    for path, scope in scopes:
        removed = _protected_removals(root, cfg, path, scope)
        if removed:
            problems.append("%s: removed line(s) inside the %s scope %s"
                            % (path, scope, sorted(removed)[:6]))
    repair_lines = {}
    for pair in pairs:
        if pair.get("disposition") != "REPAIR":
            continue
        m = re.match(r"^(.+):(\d+)$", pair.get("stated_at") or "")
        if m:
            repair_lines.setdefault(m.group(1), set()).add(int(m.group(2)))
    for item in cfg.get("fixed_surfaces") or []:
        path = item.get("path")
        line_no = item.get("line")
        if isinstance(path, str) and isinstance(line_no, int):
            repair_lines.setdefault(path, set()).add(line_no)
    fixed_by_path = {
        item.get("path"): item for item in (cfg.get("fixed_surfaces") or [])
        if isinstance(item.get("path"), str)
    }
    c_exempt_lines = {}
    if cfg.get("combined_exemptions"):
        for item in cfg.get("claim_c_owned_inplace") or []:
            path = item.get("path")
            line_no = item.get("base_line")
            before = item.get("base_text")
            after = item.get("after_text")
            base_text = show(root, base, path) if isinstance(path, str) else None
            lands_text = show(root, lands, path) if isinstance(path, str) else None
            base_lines = base_text.splitlines() if base_text is not None else []
            lands_lines = lands_text.splitlines() if lands_text is not None else []
            if not isinstance(line_no, int) or line_no < 1 \
                    or line_no > len(base_lines) or line_no > len(lands_lines):
                problems.append("claim-C owned-inplace line has invalid line number: %r" % item)
                continue
            if base_lines[line_no - 1] != before \
                    or lands_lines[line_no - 1] != after:
                problems.append("%s:%d is not the exact frozen claim-C edit"
                                % (path, line_no))
                continue
            c_exempt_lines.setdefault(path, set()).add(line_no)
    inplace = []
    for status, path in changed_files(root, base, lands):
        if path in protected_paths:
            continue
        if path == "corpus/SOURCES.md":
            continue          # the SOURCES delta is graded semantically below
        if status.startswith("A"):
            continue          # a new file is an appended file
        if path in fixed_by_path and not isinstance(
                fixed_by_path[path].get("line"), int):
            # the frozen APPENDONLY exceptions: a whole-file fixed surface is
            # the declared repair.  A frozen sha256 pins its bytes; without one
            # REPAIR binds it by re-running the tool (base red / lands green)
            # and by its receipts.
            spec = fixed_by_path[path]
            digest = spec.get("sha256")
            if digest is not None:
                if not isinstance(digest, str) \
                        or not re.fullmatch(r"[0-9a-f]{64}", digest):
                    problems.append("%s: fixed surface sha256 is malformed" % path)
                else:
                    blob = show(root, lands, path)
                    if blob is None or sha256_bytes(blob) != digest:
                        problems.append("%s: fixed surface sha256 differs from "
                                        "the frozen repair" % path)
            continue
        allowed = set(repair_lines.get(path, set())) | set(c_exempt_lines.get(path, set()))
        bad = []
        for line_no in _removed_base_lines(root, base, lands, path):
            if line_no not in allowed:
                bad.append(line_no)
        if bad:
            problems.append("%s: changed lines outside REPAIR stated_at lines %s"
                            % (path, sorted(bad)[:6]))
        elif allowed:
            inplace.append(path)
    # the R1 exemption, decided on the SOURCES rows themselves
    rule2_edits, sources_problems = sources_diff(root, base, lands)
    problems.extend("corpus/SOURCES.md: %s" % p for p in sources_problems)
    meta = cfg.get("ledger_meta") or {}
    pin = meta.get("fleet_pin")
    spec = meta.get("fleet_report")
    recorded = None
    blob = None
    if isinstance(spec, dict):
        report = spec.get("path")
        pin = spec.get("pin") or pin
        recorded = spec.get("sha256")
        blob = spec.get("blob")
    else:
        report = spec if isinstance(spec, str) else None
        recorded = meta.get("fleet_sha256")
    if not isinstance(report, str) or not report:
        report = FLEET_REPORT_DEFAULT
    if not isinstance(pin, str) and not report:
        # a ledger that pins no fleet report carries the clause vacuously
        fleet_detail = "fleet-pin=none report=none (clause vacuous)"
        detail = ("protected=%s %s repair-stated_at=%s rule2-edits=%d"
                  % (protected_paths, fleet_detail,
                     {k: sorted(v) for k, v in repair_lines.items()},
                     len(rule2_edits)))
        if problems:
            detail += " problems=%s" % problems
        return leg(out, "APPENDONLY", not problems, detail)
    fleet_detail = "fleet-pin=%s report=%s" % (
        pin[:12] if isinstance(pin, str) else pin, report)
    if not isinstance(report, str) or not report:
        problems.append("the ledger pins a fleet commit but names no fleet report")
    elif not isinstance(pin, str) or not re.fullmatch(r"[0-9a-f]{40}", pin or ""):
        problems.append("no fleet_pin in the ledger (40hex fleet commit)")
    else:
        blob_pin = show(fleet_root, pin, report)
        blob_now = show(fleet_root, "HEAD", report)
        if blob_pin is None:
            problems.append("fleet report absent at fleet_pin")
        elif blob_now is None:
            problems.append("fleet report absent at fleet HEAD")
        else:
            got = sha256_bytes(blob_pin)
            if isinstance(recorded, str) and re.fullmatch(r"[0-9a-f]{64}", recorded):
                if got != recorded:
                    problems.append("fleet report at fleet_pin has sha256 %s != "
                                    "the recorded %s" % (got[:12], recorded[:12]))
            elif recorded is not None:
                problems.append("ledger fleet sha256 is not 64-hex")
            if blob is not None and isinstance(blob, str) \
                    and re.fullmatch(r"[0-9a-f]{40}", blob):
                actual = git(fleet_root, "rev-parse", "%s:%s" % (pin, report))
                if actual.stdout.strip() != blob:
                    problems.append("fleet report blob id at fleet_pin differs "
                                    "from the recorded blob")
            if sha256_bytes(blob_now) != got:
                problems.append("fleet report bytes differ since fleet_pin")
            if git_bytes(fleet_root, "diff", "--numstat", pin, "HEAD", "--",
                         report).stdout.strip():
                problems.append("fleet report changed between fleet_pin and HEAD")
            dirty = git(fleet_root, "status", "--porcelain", "--", report)
            if dirty.stdout.strip():
                problems.append("uncommitted bytes exist under the fleet root "
                                "for %s" % report)
            fleet_detail += " blob-sha256=%s" % got[:12]
    detail = ("protected=%s %s repair-stated_at=%s rule2-edits=%d"
              % (protected_paths, fleet_detail,
                 {k: sorted(v) for k, v in repair_lines.items()},
                 len(rule2_edits)))
    if problems:
        detail += " problems=%s" % problems
    return leg(out, "APPENDONLY", not problems, detail)


def _placeholder(token):
    low = norm(token or "").casefold()
    if low in STUB_TOKENS:
        return True
    return bool(STUB_ANGLE_RE.search(token or ""))


def _required_ok(required, text):
    """A fixed-surface `required` string is a requirement, not always a
    verbatim byte string: each ';'-separated clause passes when its normalized
    text occurs in the file, or when every word of four or more characters in
    the clause occurs there.  The landing's prose is authored separately from
    the claim's description; a missing addendum still fails."""
    body = norm(text or "").casefold()
    if not body:
        return False
    clauses = [c for c in re.split(r";", required or "") if norm(c)]
    if not clauses:
        return False
    for clause in clauses:
        nc = norm(clause)
        if nc.casefold() in body:
            continue
        words = [w for w in re.findall(r"[A-Za-z0-9][A-Za-z0-9_./-]*", nc)
                 if len(w) >= 4]
        if words and all(w.casefold() in body for w in words):
            continue
        return False
    return True


def leg_nostub(out, cfg, pairs, ev, scor):
    annotate = [(i, p) for i, p in enumerate(pairs)
                if p.get("disposition") == "ANNOTATE"]
    if not annotate:
        return leg(out, "NOSTUB", True, "annotate-pairs=0 (vacuous)")
    rows = _annotate_rows(cfg, scor or "") or []
    stubs = []
    for idx, pair in annotate:
        pid = pair.get("id")
        tok = ev[idx]["stated"]
        obs, parsed, why = ev[idx]["lands"]
        cmd = rederive_text(pair)
        argv, why_argv = rederive_argv(pair)
        problems = []
        if argv is None:
            problems.append("rederive %s" % why_argv)
        elif observe_problem(argv, None, rederive=True):
            problems.append("rederive %s" % observe_problem(argv, None,
                                                            rederive=True))
        mine = [r for r in rows if row_starts_with_id(r, pid)]
        if not mine:
            stubs.append("%s:no-leading-row" % pid)
            continue
        good = False
        reasons = []
        for row in mine:
            nr = norm(row)
            lacks = []
            if tok is None or not token_in(nr, norm(tok)):
                lacks.append("old-token")
            if obs is None or not token_in(nr, norm(obs)):
                lacks.append("new-token")
            if cmd not in nr:
                lacks.append("rederive-cmd")
            if lacks:
                reasons.append(",".join(lacks))
            else:
                good = True
                break
        if not good:
            stubs.append("%s:%s" % (pid, reasons[0] if reasons else "?"))
        stubs.extend("%s:%s" % (pid, p) for p in problems)
        for tokval in (tok, obs):
            if tokval is not None and _placeholder(tokval):
                stubs.append("%s:placeholder-token(%r)"
                             % (pid, scrub(tokval, cfg)))
    return leg(out, "NOSTUB", not stubs,
               "minimum-shape=leading-id+old-token+new-token+rederive "
               "stubs=%s" % stubs)


def _path_matches_forbidden(path, forbidden):
    for item in forbidden:
        base = item.rstrip("*")
        if item.endswith("**"):
            if path == base or path.startswith(base):
                return item
        elif path == item:
            return item
    return None


def leg_separable(out, cfg, pairs, ev, scor, lands_clone):
    """Frozen sentence, read set enumerated: the ledger at <freeze>, every
    SCORECARD line under the corrections heading that names a pair id, the
    telemetry receipts and controls named in the Ca section, and the stated_at
    line of every pair.

    Redaction: this counter's own receipts are inside that read set, so NO line
    it prints may carry a lane S-id or the claim-C path-family literal.
    """
    problems = []
    scan = []
    families = list(cfg.get("c_families") or [])
    forbidden = cfg.get("separable_forbidden") or []
    lane_ids = set(cfg.get("lane_row_ids") or [])
    if not families or not lane_ids:
        return leg(out, "SEPARABLE", False,
                   "frozen SEPARABLE constants not derivable "
                   "(row-set size=%d family-sha256:%s)"
                   % (len(lane_ids),
                      sha256_bytes(",".join(sorted(families)) or "")[:8]))
    if cfg.get("ledger_raw"):
        scan.append(("ledger", cfg["ledger_raw"], None))
    ids = [p.get("id") for p in pairs if isinstance(p.get("id"), str)]
    rows = correction_rows(scor or "", cfg["round"]) or []
    ca_rows = [r for r in rows if any(row_names_id(r, i) for i in ids)]
    if ca_rows:
        scan.append(("corrections-rows", "\n".join(ca_rows), None))
    for path in cfg.get("ca_named_paths") or []:
        body = show(lands_clone["path"], "HEAD", path)
        if body is not None:
            scan.append((path, body, None))
    for pair in pairs:
        site = classify_stated_at(cfg, pair)
        if site is None:
            continue
        fleet, path, line = site
        if fleet:
            pin = fleet_pin_for(cfg, pair)
            body = show(cfg["fleet_root"], pin, path)
            label = "fleet:" + path
        else:
            body = show(cfg["root"], cfg["base"], path)
            label = path
        hit = _path_matches_forbidden(path, forbidden)
        if hit:
            problems.append("%s: stated_at path %s is a forbidden read (%s)"
                            % (pair.get("id"), path, hit))
        if body is not None and isinstance(line, int):
            lines = body.splitlines()
            if 1 <= line <= len(lines):
                scan.append(("stated:%s:%d" % (label, line), lines[line - 1],
                             pair.get("id")))
    for label, body, pid in scan:
        where = label + (" (pair %s)" % pid if pid else "")
        for m in SID_RE.finditer(body):
            if int(m.group(1)) in lane_ids:
                problems.append("cites <redacted lane id> in %s" % where)
        for family in families:
            if family in body:
                problems.append("names the frozen claim-C path family in %s"
                                % where)
    uniq = sorted(set(problems))
    ids_digest = sha256_bytes(",".join(str(i) for i in sorted(lane_ids)))[:8]
    fam_digest = sha256_bytes(",".join(sorted(families)))[:8]
    return leg(out, "SEPARABLE", not uniq,
               "lane-ids=%d ids-sha256:%s families=%d family-sha256:%s "
               "forbidden=%d scanned=%s problems=%s"
               % (len(lane_ids), ids_digest, len(families), fam_digest,
                  len(forbidden), [entry[0] for entry in scan], uniq[:8]))


# --------------------------------------------------------------------------
# RECEIPTS (H6), R1EXEMPT, COMBINED
# --------------------------------------------------------------------------
def parse_receipt_header(text):
    def first(rx):
        m = rx.search(text or "")
        return m.group(1) if m else None
    return {"stamped": first(STAMPED_RE), "evaluated": first(EVAL_RE),
            "measured": first(MEASURED_RE), "tree": first(TREE_RE),
            "sha": first(SHA_RE)}


def _pin_main_plain(clone_path, rev):
    """Pin the clone's local main to rev (throwaway clone only)."""
    r = git(clone_path, "checkout", "-q", "-B", "main", rev)
    ok = r.returncode == 0 and \
        git(clone_path, "rev-parse", "main").stdout.strip() == rev
    return ok, (r.stderr.strip() or "main != rev")


def normalize_receipt(text, work=None):
    """Volatile per-run tokens only: materialized clone roots.

    Both instruments print absolute clone roots: our own work root, the
    round-75 counter's own r75-ca- temp roots (it is re-run with --work and
    TMPDIR inside our root) and, when a nested instrument falls back to a
    system temp dir, that path too.  Everything else is compared exactly."""
    out = RECEIPT_TMP_RE.sub("<TMP>", text or "")
    out = RECEIPT_NESTED_RE.sub("<TMP>", out)
    if work:
        for form in {os.path.abspath(work), os.path.realpath(work)}:
            if form and form != os.sep:
                out = out.replace(form, "<WORK>")
    return out


def _run_r75_counter(clone_path, argv, work):
    """Run the frozen round-75 counter as a child, its scratch inside `work`."""
    try:
        p = subprocess.run(argv, cwd=clone_path, capture_output=True, text=True,
                           timeout=1800, env=_child_env(work))
    except (OSError, subprocess.TimeoutExpired) as exc:
        return None, str(exc)
    return p, ""


def leg_receipts(out, root, cfg, work, fleet_root):
    """Frozen sentence: materialize a clone of the frozen round-75 claim-Ca
    lands, pin its local main to it, re-run accept-ca-75 inside it (with the
    frozen round-75 freeze, its --combined tree and --fleet-root), require exit
    0 and the exact PASS line, and require the committed receipt to carry that
    stdout verbatim with stamped==evaluated==measured==that revision."""
    problems = []
    rev = cfg.get("receipts_rev")
    r75_freeze = cfg.get("receipts_freeze")
    r75_combined = cfg.get("receipts_combined")
    counter_rel = cfg.get("receipts_counter") or R75_COUNTERS["accept-ca-75"]
    pass_line = cfg.get("receipts_pass_line") or PASS_LINES["accept-ca-75"]
    if not rev:
        return leg(out, "RECEIPTS", False,
                   "frozen RECEIPTS leg names no round-75 lands revision")
    if not r75_freeze:
        return leg(out, "RECEIPTS", False,
                   "frozen RECEIPTS leg names no round-75 freeze revision")
    if not r75_combined:
        return leg(out, "RECEIPTS", False,
                   "frozen RECEIPTS leg names no round-75 --combined revision")
    if not cfg.get("receipt_paths"):
        return leg(out, "RECEIPTS", False,
                   "frozen RECEIPTS leg names no receipt paths")
    for label, value in (("lands", rev), ("freeze", r75_freeze),
                         ("combined", r75_combined)):
        if git(root, "cat-file", "-e", "%s^{commit}" % value).returncode != 0:
            return leg(out, "RECEIPTS", False,
                       "round-75 %s %s is not a commit in the lane"
                       % (label, value[:12]))
    if git(root, "cat-file", "-e", "%s:%s" % (rev, counter_rel)).returncode != 0:
        return leg(out, "RECEIPTS", False,
                   "%s is unreadable at %s" % (counter_rel, rev[:12]))
    clone = materialize(root, rev, work, "r75lands")
    if clone is None:
        return leg(out, "RECEIPTS", False,
                   "could not materialize the round-75 lands %s" % rev[:12])
    ok_main, why = _pin_main_plain(clone["path"], rev)
    if not ok_main:
        problems.append("could not pin the clone's local main: %s" % why)
    child_work = os.path.join(work, "r75work")
    os.makedirs(child_work, exist_ok=True)
    argv = [sys.executable, "-B", counter_rel, "--root", ".",
            "--lands", rev, "--freeze", r75_freeze,
            "--fleet-root", fleet_root, "--combined", r75_combined,
            "--main", "main", "--work", child_work]
    proc, err = _run_r75_counter(clone["path"], argv, work)
    rerun = None
    if proc is None:
        problems.append("accept-ca-75 re-run failed to execute: %s" % err)
    else:
        rerun = proc.stdout
        if proc.returncode != 0:
            problems.append("accept-ca-75 re-run exit=%d (want 0)"
                            % proc.returncode)
        if pass_line not in proc.stdout.splitlines():
            problems.append("accept-ca-75 re-run did not print %r" % pass_line)
    receipt_detail = []
    for key, path in (cfg.get("receipt_paths") or {}).items():
        body = show(cfg["root"], cfg["lands"], path)
        if body is None:
            problems.append("receipt %s is not committed at lands" % path)
            continue
        hdr = parse_receipt_header(body)
        for hkey in ("stamped", "evaluated", "measured", "tree", "sha"):
            if not hdr.get(hkey):
                problems.append("%s: missing %s header" % (path, hkey))
        if hdr.get("stamped") != rev:
            problems.append("%s: stamped %s != %s"
                            % (path, hdr.get("stamped"), rev[:12]))
        if hdr.get("evaluated") != rev:
            problems.append("%s: evaluated != %s" % (path, rev[:12]))
        if hdr.get("measured") != rev:
            problems.append("%s: measured != %s" % (path, rev[:12]))
        want_tree = git(root, "rev-parse", "%s^{tree}" % rev).stdout.strip()
        if want_tree and hdr.get("tree") != want_tree:
            problems.append("%s: tree %s != %s"
                            % (path, hdr.get("tree"), want_tree[:12]))
        blob = git_bytes(root, "show", "%s:%s" % (rev, counter_rel))
        if blob.returncode != 0:
            problems.append("%s: %s is unreadable at %s"
                            % (path, counter_rel, rev[:12]))
        else:
            want_sha = sha256_bytes(blob.stdout)
            if hdr.get("sha") != want_sha:
                problems.append("%s: counter sha256 %s != the round-75 counter %s"
                                % (path, hdr.get("sha"), want_sha[:12]))
        if pass_line not in body.splitlines():
            problems.append("%s: does not carry %r" % (path, pass_line))
        if rerun is not None:
            got_receipt = normalize_receipt(body, work)
            got_rerun = normalize_receipt(rerun, work)
            if got_receipt != got_rerun:
                problems.append("%s: committed stdout differs from the re-run "
                                "(%s vs %s)"
                                % (path, sha256_bytes(got_receipt)[:12],
                                   sha256_bytes(got_rerun)[:12]))
            receipt_detail.append("%s=%s" % (key, sha256_bytes(body)[:12]))
    detail = "rev=%s combined=%s receipts=%s problems=%s" % (
        rev[:12], r75_combined[:12], receipt_detail, problems)
    return leg(out, "RECEIPTS", not problems, detail)


R1_FIXTURE_DIRS = (os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "fixtures"),
                   os.path.join(".ufo", "waves", "round-76", "counters",
                                "fixtures"))


def _r1_fixture_path(name):
    """The fixtures land beside the counter; a copy of the counter that lives
    elsewhere still finds the committed originals in the wave directory."""
    for base in R1_FIXTURE_DIRS:
        path = os.path.join(base, name)
        if os.path.exists(path):
            return path
    return None


def load_r1_fixtures():
    """{key: spec} for the R1EXEMPT fixtures committed with the counter.

    The fixtures live in counters/fixtures/ so the exemption is proved against
    readable bytes rather than a generator hidden in the leg: each names the
    registry cells it edits, the marker it appends and the verdict it must
    produce."""
    out = {}
    for key in ("green", "red", "mixed"):
        path = _r1_fixture_path("r1exempt-%s.json" % key)
        if path is None:
            continue
        try:
            with open(path, encoding="utf-8") as fh:
                spec = json.load(fh)
        except (OSError, ValueError):
            continue
        if not isinstance(spec, dict):
            continue
        cells = spec.get("cells")
        if not isinstance(cells, list) or not cells \
                or not all(isinstance(c, str) and c for c in cells):
            continue
        spec.setdefault("expect", "green" if key == "green" else "red")
        spec.setdefault("marker", "r1-exempt-marker")
        out[key] = spec
    return out


def _sources_edit_fixture(root, base, tmpdir, label, spec):
    """A tree whose only corpus/SOURCES.md delta versus base is the spec's cell
    edit on one pre-existing row (spec["row"] when the graded registry carries
    it, else the registry's first row id — the selftest's synthetic registry
    does not carry the real ids)."""
    clone = materialize(root, base, tmpdir, label)
    if clone is None:
        return None
    path = os.path.join(clone["path"], "corpus/SOURCES.md")
    try:
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
    except OSError:
        return None
    header = sources_header(text)
    idxs = []
    for cell in spec["cells"]:
        hit = [i for name, i in header if name == cell]
        if not hit:
            return None
        idxs.append(hit[0])
    rows = sources_rows(text)
    if not rows:
        return None
    rid = spec.get("row") if spec.get("row") in rows else sorted(rows)[0]
    lines = text.splitlines()
    lineno, cells = rows[rid]
    cells = list(cells)
    if len(cells) != len(header):
        return None
    for idx in idxs:
        cells[idx] = (cells[idx] + " " + spec["marker"]).strip()
    lines[lineno - 1] = "| " + " | ".join(
        c.replace("|", "\\|") for c in cells) + " |"
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")
    env = dict(os.environ)
    env.update(SELFTEST_ENV)
    subprocess.run(["git", "-C", clone["path"], "add", "-A"], env=env,
                   capture_output=True, text=True)
    subprocess.run(["git", "-C", clone["path"], "commit", "-q", "-m",
                    "r1 fixture: %s cell edit on %s"
                    % ("+".join(spec["cells"]), rid)],
                   env=env, capture_output=True, text=True)
    head = git(clone["path"], "rev-parse", "HEAD").stdout.strip()
    return {"path": clone["path"], "head": head, "row": rid,
            "cells": list(spec["cells"])}


def leg_r1exempt(out, root, cfg, freeze_tmp):
    """Frozen sentence: the exemption is proved both ways — a rule-2 cell edit
    on a pre-existing row grades APPENDONLY green, a teaches-cell edit grades
    it red — and the committed receipts carry the runs.  A third fixture (a
    simultaneous teaches + used-by edit) proves the exemption is decided on the
    changed cell SET, not on any changed span."""
    problems = []
    base = cfg["base"]
    specs = load_r1_fixtures()
    if set(specs) != {"green", "red", "mixed"}:
        problems.append("the R1 fixtures beside the counter are incomplete: %s"
                        % sorted(specs))
    verdicts = {}
    for key in ("green", "red", "mixed"):
        spec = specs.get(key)
        if not spec:
            continue
        fixture = _sources_edit_fixture(root, base, freeze_tmp, "r1-" + key,
                                        spec)
        if fixture is None:
            problems.append("could not build the %s fixture tree" % key)
            continue
        _edits, probs = sources_diff(fixture["path"], base, fixture["head"])
        verdicts[key] = not probs
        want_green = spec.get("expect") == "green"
        cells = "+".join(fixture["cells"])
        if want_green and probs:
            problems.append("%s fixture (row %s, cells %s) grades RED: %s"
                            % (key, fixture["row"], cells, probs[:3]))
        if not want_green and not probs:
            problems.append("%s fixture (row %s, cells %s) grades GREEN: the "
                            "exemption over-fires"
                            % (key, fixture["row"], cells))
    # the committed receipts must carry the two runs
    receipt_detail = []
    for key, path in (cfg.get("r1_receipt_paths") or {}).items():
        body = show(cfg["root"], cfg["lands"], path)
        if body is None:
            problems.append("receipt %s is not committed at lands" % path)
            continue
        want_pass = (key == "green")
        has_pass = re.search(r"LEG PASS APPENDONLY", body) is not None
        has_fail = re.search(r"LEG FAIL APPENDONLY", body) is not None
        if want_pass and not has_pass:
            problems.append("%s: does not carry 'LEG PASS APPENDONLY'" % path)
        if not want_pass and not has_fail:
            problems.append("%s: does not carry 'LEG FAIL APPENDONLY'" % path)
        if want_pass and not re.search(r"exit[ =:]?0", body):
            problems.append("%s: does not carry the exit code 0" % path)
        if (not want_pass) and not re.search(r"exit[ =:]?1", body):
            problems.append("%s: does not carry the exit code 1" % path)
        receipt_detail.append("%s=%s" % (key, sha256_bytes(body)[:12]))
    detail = "verdicts=%s receipts=%s problems=%s" % (verdicts, receipt_detail,
                                                      problems)
    return leg(out, "R1EXEMPT", not problems, detail)


def _carries_both_landings(root, cfg, rev):
    """(ok, problems) — does `rev` carry claim C's landing AND claim Ca's?"""
    problems = []
    for rid in ["S%d" % i for i in (cfg.get("lane_row_ids") or [])]:
        text = show(root, rev, "corpus/SOURCES.md")
        if text is None or rid not in sources_rows(text):
            problems.append("claim-C row %s absent at %s" % (rid, rev[:12]))
    for path in cfg.get("claim_c_entries") or []:
        if git(root, "rev-parse", "%s:%s" % (rev, path)).returncode != 0:
            problems.append("claim-C entry %s absent at %s" % (path, rev[:12]))
    scor = show(root, rev, SCORECARD_REL)
    rows = correction_rows(scor or "", cfg["round"])
    if rows is None:
        problems.append("no '## Corrections — round %d' section at %s"
                        % (cfg["round"], rev[:12]))
    else:
        pairs = (cfg.get("ledger_meta") or {}).get("pairs") or []
        for pair in pairs:
            if pair.get("disposition") != "ANNOTATE":
                continue
            pid = pair.get("id")
            if not any(row_starts_with_id(r, pid) for r in rows):
                problems.append("claim-Ca correction row for %s absent at %s"
                                % (pid, rev[:12]))
    return (not problems), problems


def leg_combined(out, root, cfg, tmpdir, combined_rev, lands_clone):
    """Re-evaluate APPENDONLY at the required `--combined` tree carrying both
    landings.

    The main Ca legs stay pinned to Ca's own landing for causal separability;
    COMBINED checks only that the actual combined diff stays inside the frozen
    rule-2 and claim-C exemptions.  A missing `--combined` never reaches this
    leg: main_check refuses the run (exit 2), so a red COMBINED here always
    means a real defect at the combined tree.
    """
    problems = []
    if not combined_rev:
        return leg(out, "COMBINED", False,
                   "internal: no combined revision reached the leg")
    rev = combined_rev
    if git(root, "cat-file", "-e", "%s^{commit}" % rev).returncode != 0:
        return leg(out, "COMBINED", False,
                   "combined revision %s is not a commit in the lane" % rev[:12])
    ok, probs = _carries_both_landings(root, cfg, rev)
    problems.extend(probs)
    clone = materialize(root, rev, tmpdir, "combined")
    if clone is None:
        problems.append("could not materialize the combined tree %s" % rev[:12])
    else:
        combined_cfg = dict(cfg)
        combined_cfg["lands"] = rev
        combined_cfg["combined_exemptions"] = True
        probe = []
        with redirect_stdout(io.StringIO()):
            leg_appendonly(probe, root, combined_cfg,
                           (cfg.get("ledger_meta") or {}).get("pairs") or [],
                           cfg.get("fleet_root"))
        if not probe or not probe[0][1]:
            detail = probe[0][2] if probe else "no APPENDONLY result"
            problems.append("combined APPENDONLY failed: %s" % detail)
    tree = git(root, "rev-parse", "%s^{tree}" % rev).stdout.strip()
    detail = ("ca-lands=%s combined=%s tree=%s problems=%s"
              % (cfg["lands"][:12], rev[:12], tree[:12], problems[:6]))
    return leg(out, "COMBINED", not problems, detail)


def _on_first_parent_chain(root, freeze, lands):
    revs = git(root, "rev-list", "--first-parent", lands).stdout.split()
    return freeze in revs


def leg_frozencfg(out, root, cfg, freeze, lands):
    problems = list(cfg.get("problems") or [])
    if freeze == lands:
        note("lands == freeze: do-nothing control shape; the strict-ancestor "
             "requirement is not applied to this run and a PASS is refused")
    else:
        anc = git(root, "merge-base", "--is-ancestor", freeze, lands)
        if anc.returncode != 0:
            problems.append("--freeze %s is not an ancestor of --lands %s"
                            % (freeze[:12], lands[:12]))
        elif not _on_first_parent_chain(root, freeze, lands):
            problems.append("--freeze %s is not on the lands first-parent chain"
                            % freeze[:12])
    base = cfg.get("base")
    if not base:
        problems.append("frozen claims base missing")
    else:
        anc = git(root, "merge-base", "--is-ancestor", base, freeze)
        if anc.returncode != 0:
            problems.append("frozen base %s is not an ancestor of --freeze"
                            % base[:12])
    for path in (cfg["claims_rel"], cfg["ledger_rel"]):
        blobs = []
        for rev in (freeze, lands):
            r = git(root, "rev-parse", "%s:%s" % (rev, path))
            blobs.append(r.stdout.strip() if r.returncode == 0 else None)
        if blobs[1] is None:
            problems.append("%s is absent from the graded tree (deleted after "
                            "freeze?)" % path)
        elif blobs[0] is None:
            problems.append("%s is absent at --freeze" % path)
        elif blobs[0] != blobs[1]:
            problems.append("%s was edited in the graded tree after freeze "
                            "(%s != %s)" % (path, blobs[0][:12], blobs[1][:12]))
    lane_ids = sorted(cfg.get("lane_row_ids") or [])
    detail = ("freeze=%s first-parent-of-lands; round=%r base=%s legs=%s "
              "min-pairs=%d lane-ids=%d ids-sha256:%s family-sha256:%s "
              "protected=%s receipts=%s"
              % (freeze[:12], cfg.get("round"),
                 (cfg.get("base") or "")[:12], cfg.get("leg_names"),
                 cfg.get("min_pairs"), len(lane_ids),
                 sha256_bytes(",".join(str(i) for i in lane_ids))[:8],
                 sha256_bytes(",".join(sorted(cfg.get("c_families") or [])))[:8],
                 cfg.get("protected"), (cfg.get("receipts_rev") or "")[:12]))
    if problems:
        detail += " problems=%d %s" % (len(problems), problems[:8])
    return leg(out, "FROZENCFG", not problems, detail)


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
        problems.append("an observation ran outside the clone")
    detail = ("stamped=evaluated=measured=%s tree=%s counter=%s clone=%s"
              % (lands[:12], (header.get("tree") or "")[:12],
                 (header.get("sha") or "")[:12], clone["path"]))
    if problems:
        detail += " problems=%s" % problems
    return leg(out, "STAMP", not problems, detail)


# --------------------------------------------------------------------------
# driver
# --------------------------------------------------------------------------
def _refuse(message):
    print("ACCEPT-CA-76: FAIL legs=0/12 (refused: %s)" % message)
    return 2


def main_check(root, lands, freeze, fleet_root, main_branch="main",
               claims_rel=CLAIMS_REL, ledger_rel=LEDGER_REL, combined_rev=None,
               work=None):
    root = os.path.abspath(root)
    fleet_root = os.path.abspath(fleet_root)
    try:
        work = scratch_dir(work)
    except ScratchRefused as exc:
        return _refuse(str(exc))
    CTX["fleet_root"] = fleet_root
    CTX["root"] = root
    RUN_STATE["outside_clone"] = False
    RUN_STATE["work"] = work
    out = []
    total_legs = len(REQUIRED_LEGS)

    # `--combined` is an input requirement, not a graded leg: claim C lands
    # after claim Ca in round 76, and a missing flag must REFUSE rather than
    # print a red COMBINED leg that reads as a failed claim.
    if not combined_rev:
        return _refuse("--combined <C-lands> is required: the COMBINED leg "
                       "grades the tree carrying both landings")
    if git(root, "cat-file", "-e", "%s^{commit}" % lands).returncode != 0:
        print("ERROR: --lands %s is not a commit in %s" % (lands, root),
              file=sys.stderr)
        return 2
    if git(root, "cat-file", "-e", "%s^{commit}" % freeze).returncode != 0:
        print("ERROR: --freeze %s is not a commit in %s" % (freeze, root),
              file=sys.stderr)
        return 2
    if git(root, "cat-file", "-e",
           "%s^{commit}" % combined_rev).returncode != 0:
        print("ERROR: --combined %s is not a commit in %s"
              % (combined_rev, root), file=sys.stderr)
        return 2

    cfg, err = load_frozen(root, freeze, claims_rel, ledger_rel)
    if err:
        print("ERROR: %s" % err, file=sys.stderr)
        return 2
    # LEGCOUNT: the implemented leg table must be exactly the frozen leg table,
    # in the frozen order
    frozen_names = list(cfg.get("leg_names") or [])
    if frozen_names != list(REQUIRED_LEGS):
        return _refuse("leg table %r != the frozen %d legs %r (order included)"
                       % (frozen_names, total_legs, list(REQUIRED_LEGS)))
    cfg.update({"root": root, "lands": lands, "freeze": freeze,
                "fleet_root": fleet_root})
    CTX["cfg"] = cfg
    base = cfg.get("base")
    if not base or git(root, "cat-file", "-e", "%s^{commit}" % base).returncode != 0:
        print("ERROR: the frozen claims base %r is not a commit in %s"
              % (base, root), file=sys.stderr)
        return 2
    if lands == base:
        return _refuse("--lands equals the frozen base %s" % base[:12])

    tmpdir = tempfile.mkdtemp(prefix="r76-ca-", dir=work)
    try:
        clone = materialize(root, lands, tmpdir, "lands")
        if clone is None:
            return 2
        base_clone = clone if base == lands \
            else materialize(root, base, tmpdir, "base")
        if base_clone is None:
            return 2

        meta = cfg.get("ledger_meta") or {}
        pairs = meta.get("pairs") or []

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
        print("# claim: %s  round: %r  base: %s%s"
              % (CLAIM, cfg.get("round"), base, measured_note))
        print("# freeze: %s (config read at this commit only)" % freeze)
        print("# min-pairs: %d" % cfg["min_pairs"])
        print("# frozen legs: %d (%s)" % (len(frozen_names),
                                          ", ".join(frozen_names)))
        if combined_rev:
            print("# combined revision: %s" % combined_rev)
        print("# counter: %s" % os.path.relpath(os.path.abspath(__file__),
                                                os.getcwd()))
        print("# clone: %s head=%s" % (clone["path"], clone["head"]))
        print("# base-clone: %s head=%s"
              % ("reused" if base_clone is clone else base_clone["path"],
                 base_clone["head"]))
        print("# ledger: %s source=freeze sha256=%s"
              % (cfg["ledger_rel"],
                 sha256_bytes(cfg["ledger_raw"]) if cfg.get("ledger_raw") else "none"))

        scor = show(clone["path"], "HEAD", SCORECARD_REL)

        ev = evaluate_pairs(pairs, base_clone, clone) if pairs else []
        for idx, pair in enumerate(pairs):
            tok = ev[idx]["stated"]
            ob, parsed, why = ev[idx]["base"]
            ol, parsed_l, why_l = ev[idx]["lands"]
            print("PAIR %s disposition=%s stated_at=%s stated=%r "
                  "observed_base=%r observed_lands=%r expected_after=%r"
                  % (pair.get("id"), pair.get("disposition"),
                     scrub(pair.get("stated_at"), cfg),
                     scrub((tok or "")[:60], cfg),
                     scrub((ob if ob is not None else "<%s>" % why)[:60], cfg),
                     scrub((ol if ol is not None else "<%s>" % why_l)[:60], cfg),
                     scrub(str(pair.get("expected_after", ""))[:40], cfg)))

        leg_ledger(out, cfg, pairs, base_clone, ev)
        if not pairs:
            for name in ("BASEMISMATCH", "REPAIR", "ANNOTATE", "NOSTUB"):
                leg(out, name, False, "no pairs in the frozen ledger")
        else:
            leg_basemismatch(out, cfg, pairs, ev)
            leg_repair(out, cfg, pairs, ev)
            leg_annotate(out, cfg, pairs, ev, scor, clone)
            leg_nostub(out, cfg, pairs, ev, scor)
        leg_appendonly(out, root, cfg, pairs, fleet_root)
        leg_r1exempt(out, root, cfg, tmpdir)
        leg_separable(out, cfg, pairs, ev, scor, clone)
        leg_receipts(out, root, cfg, tmpdir, fleet_root)
        leg_combined(out, root, cfg, tmpdir, combined_rev, clone)
        leg_frozencfg(out, root, cfg, freeze, lands)
        leg_stamp(out, header, root, lands, clone)
    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)

    passed = sum(1 for _, ok, _ in out if ok)
    total = len(out)
    ok = passed == total and total == total_legs
    if ok and freeze == lands:
        return _refuse("freeze == lands and every leg green: the do-nothing "
                       "shape cannot pass")
    print("ACCEPT-CA-76: %s legs=%d/%d"
          % ("PASS" if ok else "FAIL", passed, total))
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

STUB_R75_CA = '''#!/usr/bin/env python3
import argparse, hashlib, subprocess
ap = argparse.ArgumentParser()
ap.add_argument("--root", default=".")
ap.add_argument("--lands")
ap.add_argument("--freeze")
ap.add_argument("--fleet-root")
ap.add_argument("--main", default="main")
ap.add_argument("--combined")
ap.add_argument("--work")
args, _ = ap.parse_known_args()
sha = hashlib.sha256(open(__file__, "rb").read()).hexdigest()
tree = subprocess.run(["git", "-C", args.root, "rev-parse", args.lands + "^{tree}"],
                      capture_output=True, text=True).stdout.strip()
print("# counter sha256 (self): %s" % sha)
print("# stamped revision: %s" % args.lands)
print("# evaluated revision: %s" % args.lands)
print("# measured revision (lane main): %s" % args.lands)
print("# tree: %s" % tree)
print("ACCEPT-CA-75: PASS legs=12/12")
'''

FIXTURE_FILES = {
    "LOG.md": "# LOG\n\n- round-72 entry\n",
    "SCORECARD.md": ("# SCORECARD\n\n| axis | verdict |\n|---|---|\n"
                     "| calibration | ACCEPT-CA-72 PASS legs=12/12 |\n"),
    "corpus/lessons/round-74.md": "# Round 74\n\n- lesson\n",
    "corpus/lessons/round-73.md": "# Round 73\n\n- lesson\n",
    "corpus/lessons/round-75.md": ("# Round 75\n\n## Routed to round 76\n\n"
                                   "- a routed item\n"),
    "NOTES.md": "# notes\n\n- keep me in place\n",
    "REPORT.md": "# report\n\nmode: old-doc\n",
    "LIVE.md": "mode: legacy\n",
    "IDS.md": "entries: 0 (S900)\nentries: 0 (S909)\n",
    "SHONEN.md": ("# checklist\n\n- [~] item one\n  asserted: old\n"
                  "- [ ] item two\n  asserted: old\n\n"
                  "Marks: `[~]` asserted by the lane itself.\n"),
    "corpus/QUALITY.md": ("# corpus/QUALITY.md — the admission bar\n\n"
                          "1. **Provenance** — every claim carries a source\n"
                          "2. **Calibration** — every entry names its status\n"),
    "corpus/README.md": ("# corpus\n\n## linguistics/ (30)\n\n"
                         "Total knowledge entries: 243.\n"),
    "corpus/SOURCES.md": (
        "# SOURCES — where kotodama learns\n\n"
        "| id | source | kind | tier | scope | anchor | teaches | status | "
        "opened | recheck | used-by |\n"
        "|---|---|---|---|---|---|---|---|---|---|---|\n"
        "| S001 | Glottolog — https://glottolog.org/about.html | docs | A | "
        "identification | About | catalogue | mined | 2026-10-19 | on-release "
        "| corpus/knowledge/linguistics/naming-systems.md |\n"
        "| S002 | WALS — https://wals.info | dataset | A | syntax | README | "
        "syntax features | queued | 2026-10-19 | 180d | — |\n"),
    "corpus/knowledge/myth-symbol/other.md": "# other\n",
}
FIXTURE_KEYS = "".join("key%02d\n" % i for i in range(1, 11))
FIXTURE_STATEMENTS = "".join("row%02d entries: 0.\n" % i for i in range(1, 11))
FLEET_REPORT = ".ufo/reports/round-74/kotodama.md"
LANE_ROW_ID = "S894"
CLAIM_C_ENTRY = ("corpus/knowledge/culture-material/"
                 "calendar-festival-systems.amend-2026-10-24.md")
C_FAMILIES = ("calendar-festival-systems", "era-periodization-models")


def _g(root, *args):
    env = dict(os.environ)
    env.update(SELFTEST_ENV)
    return subprocess.run(["git", "-C", root, *args], capture_output=True,
                          text=True, env=env)


def _g_bytes(root, *args):
    env = dict(os.environ)
    env.update(SELFTEST_ENV)
    return subprocess.run(["git", "-C", root, *args], capture_output=True,
                          env=env)


def _write(root, rel, text):
    path = os.path.join(root, rel)
    os.makedirs(os.path.dirname(path) or root, exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)


def _commit(root, msg, only=None):
    _g(root, "add", "-A")
    if only:
        _g(root, "reset", "-q")
        _g(root, "add", "--", *only)
    r = _g(root, "commit", "-q", "-m", msg)
    if r.returncode != 0:
        raise RuntimeError("fixture commit failed: %s" % r.stderr)
    return _g(root, "rev-parse", "HEAD").stdout.strip()


def _branch(root, name, rev):
    _g(root, "checkout", "-q", "-B", name, rev)


def _at(root, rev):
    _g(root, "checkout", "-q", "--detach", rev)


def _set_branch(root, name, rev):
    _g(root, "branch", "-q", "-f", name, rev)


def _pairs(base):
    out = []
    for i in range(1, 11):
        cmd = ["git", "grep", "-c", "^key%02d$" % i, base, "--", "keys.txt"]
        out.append({
            "id": "A%02d" % i,
            "stated_at": "STATEMENTS.md:%d" % i,
            "stated_text": "row%02d entries: 0." % i,
            "stated_parse": r"entries: (\d+)",
            "observe_cmd": cmd,
            "parse": r":(\d+)$",
            "expected_after": "1",
            "disposition": "ANNOTATE",
            "rederive": shlex.join(cmd),
        })
    out.append({
        "id": "R01",
        "stated_at": "REPORT.md:3",
        "stated_text": "mode: old-doc",
        "stated_parse": r"mode: ([\w-]+)",
        "observe_cmd": ["grep", "-o", "^mode: .*", "LIVE.md"],
        "parse": r"mode: ([\w-]+)",
        "expected_after": "legacy",
        "disposition": "REPAIR",
        "statement_after": {"path": "REPORT.md", "parse": r"mode: ([\w-]+)"},
        "rederive": "grep -o '^mode: .*' LIVE.md",
    })
    return out


def _claims_legs(base, r75):
    return [
        "LEDGER: reports/round-76/ledger.json is committed in the freeze commit "
        "and declares round 76 / claim Ca / base, >= 10 unique pairs, each "
        "structurally valid (argv observe_cmd whose executable is in a "
        "read-only allowlist {git, grep, wc, sha256sum, ls, cat, head, tail, "
        "cut} that EXCLUDES interpreters and echo/printf/true-style constant "
        "printers and shell metacharacters; compiling parse with a capture "
        "group; stated_text found at stated_at in the BASE tree; stated token "
        "anchored in it; the disposition matches the frozen file class: a "
        "REPAIR pair's statement_after path is one of the frozen mutable files "
        "(REPORT.md); an ANNOTATE pair's stated_at path is one of the frozen "
        "append-only files (STATEMENTS.md, LOG.md, SCORECARD.md)); no "
        "absence-observation pair",
        "BASEMISMATCH: at the base revision every pair has stated token != "
        "observed token and none is unobservable; the number of such pairs >= 10",
        "REPAIR: every REPAIR pair's statement re-read at <lands> (last "
        "occurrence) equals the truth observed in a clone at <lands> and "
        "differs from the base statement; a REPAIR pair's statement_after path "
        "is one of the frozen mutable files (REPORT.md); a REPAIR pair's "
        "stated_at is never a line claim C appends to",
        "ANNOTATE: every ANNOTATE pair has a row under '## Corrections — "
        "round 76' in SCORECARD.md naming the pair id, the base stated token and "
        "the observed token, and the row's re-derivation command is re-run by "
        "the counter and returns the observed token; count pairs measure at "
        "the pinned base revision; an ANNOTATE pair's stated_at path is one of "
        "the frozen append-only files (STATEMENTS.md, LOG.md, SCORECARD.md)",
        "APPENDONLY: base..<lands> has zero removed lines in LOG.md, "
        "SCORECARD.md, corpus/lessons/round-74.md, corpus/lessons/round-73.md, "
        "corpus/lessons/round-75.md, corpus/QUALITY.md and SHONEN.md's mark "
        "lines; in corpus/SOURCES.md, changed lines on pre-existing rows are "
        "exempt ONLY when the change is inside the status, recheck or used-by "
        "cell of that row (SOURCES contract rule 2; the R1 exemption) — every "
        "other changed line on a pre-existing row fails the leg; changed lines "
        "elsewhere are a subset of the stated_at lines of REPAIR pairs plus "
        "appended lines; the fleet round-74 report at the ledger's fleet_pin is "
        "byte-identical to the blob its sha256 names and this lane writes no "
        "byte under the fleet root",
        "R1EXEMPT: fixtures committed with the freeze prove the exemption both "
        "ways: (a) a tree whose only SOURCES delta versus base is a rule-2 "
        "cell edit on one pre-existing row grades APPENDONLY green on every "
        "other leg unchanged; (b) a tree whose only SOURCES delta is a "
        "teaches-cell (non-rule-2) edit on one pre-existing row grades "
        "APPENDONLY red; receipts r1exempt-green.txt and r1exempt-red.txt "
        "carry the runs",
        "NOSTUB: every correction row carries id + old token + new token + the "
        "re-derivation command and no placeholder token in {TODO, TBD, FIXME, "
        "XXX, n/a, ?} or <...>",
        "SEPARABLE: the Ca read set is exactly {the ledger at <freeze>, every "
        "SCORECARD line under '## Corrections — round 76' that names a pair "
        "id, the telemetry receipts and controls named in this file's Ca "
        "section, and the stated_at line of every pair}; no byte in that set "
        "cites a lane id claim C adds (%s) or names %s* or %s*; no stated_at "
        "path is corpus/SOURCES.md, corpus/knowledge/**, "
        "reports/round-76/evidence/** or .ufo/waves/round-76/assimilation/**; "
        "every observation is the token the pair's observe_cmd returns in the "
        "clone at the revision the ledger names"
        % (LANE_ROW_ID, C_FAMILIES[0], C_FAMILIES[1]),
        "RECEIPTS: the counter materializes a clone of the round-75 claim-Ca "
        "lands %s and re-runs `python3 -B reports/round-75/accept-ca.py --root "
        ". --lands %s --freeze %s --fleet-root <fleet> --combined %s --main "
        "main` inside it (with --work under our own scratch root), requiring "
        "exit 0 and the exact line 'ACCEPT-CA-75: PASS legs=12/12', and "
        "requires the committed reports/round-76/telemetry/"
        "accept-ca-75-at-lands.txt to carry that stdout verbatim with "
        "stamped==evaluated==measured==that revision" % (r75, r75, base, r75),
        "COMBINED: at the required --combined tree carrying BOTH landings "
        "(materialized), accept-ca-76 prints ACCEPT-CA-76: PASS legs=12/12 — "
        "the round-74 APPENDONLY combined-tree conflict class is closed by the "
        "R1 exemption; receipt measures-ca-head.txt",
        "FROZENCFG: ledger, constants and allowlists are read from `git show "
        "<freeze>:...` (claims.json, ledger.json), never from the graded tree; "
        "<freeze> is an ancestor of <lands> on its first-parent chain (<lands> "
        "== <freeze> is graded as the do-nothing control); reports/round-76/"
        "claims.json and ledger.json at <lands> are byte-identical to the "
        "freeze blobs",
        "STAMP: the receipt carries the stamped/evaluated/measured revision, "
        "tree and counter-sha256 headers (QUALITY 17/19 grammar of "
        "tools/check-receipt-seq.py) with stamped == evaluated == measured == "
        "<lands>, produced inside a clone materialized at <lands>",
    ]


def _corrections(pairs):
    lines = ["", "## Corrections — round 76", "",
             "| id | old token | new token | re-derivation command | note |",
             "|---|---|---|---|---|"]
    for pair in pairs:
        if pair.get("disposition") != "ANNOTATE":
            continue
        lines.append("| %s | 0 | 1 | %s | fixture row |"
                     % (pair["id"], pair.get("rederive") or
                        shlex.join(pair["observe_cmd"])))
    lines.append("")
    return "\n".join(lines)


def _stub_receipt(lane, rev, rel, name, legs, extra=""):
    sha = hashlib.sha256(_g_bytes(lane, "show", "%s:%s" % (rev, rel)).stdout).hexdigest()
    tree = _g(lane, "rev-parse", "%s^{tree}" % rev).stdout.strip()
    return ("# counter sha256 (self): %s\n"
            "# stamped revision: %s\n"
            "# evaluated revision: %s\n"
            "# measured revision (lane main): %s\n"
            "# tree: %s\n"
            "%s: PASS legs=%s\n%s"
            % (sha, rev, rev, rev, tree, name, legs, extra))


def _build(td, tag, pairs=None, ledger_committed=True, claims_legs=None,
           mutate_ledger=None, claims_mutate=None, stub_counter=None):
    """(lane, fleet, base, r75, freeze, clean, head).  Fresh repo per tag."""
    lane = os.path.join(td, tag, "lane")
    fleet = os.path.join(td, tag, "fleet")
    os.makedirs(lane)
    os.makedirs(fleet)
    _g(fleet, "init", "-q")
    _write(fleet, FLEET_REPORT, "# round-74 fleet report\n")
    _write(fleet, "scripts/sources-census.sh", "#!/bin/sh\nexit 0\n")
    os.chmod(os.path.join(fleet, "scripts/sources-census.sh"), 0o755)
    _commit(fleet, "fleet r74 report")
    fleet_pin = _g(fleet, "rev-parse", "HEAD").stdout.strip()

    _g(lane, "init", "-q")
    top = _g(lane, "rev-parse", "--show-toplevel").stdout.strip()
    if os.path.realpath(top) != os.path.realpath(lane):
        raise RuntimeError("fixture toplevel %s != %s" % (top, lane))
    for rel, text in FIXTURE_FILES.items():
        _write(lane, rel, text)
    _write(lane, "keys.txt", FIXTURE_KEYS)
    _write(lane, "STATEMENTS.md", FIXTURE_STATEMENTS)
    base = _commit(lane, "fixture base")
    _set_branch(lane, "base", base)

    _write(lane, "reports/round-75/accept-ca.py", stub_counter or STUB_R75_CA)
    r75 = _commit(lane, "round-75 Ca lands (stub counter)")

    pairs = _pairs(base) if pairs is None else pairs
    if mutate_ledger:
        pairs = mutate_ledger(pairs, base)
    fleet_sha = hashlib.sha256(
        _g_bytes(fleet, "show", "HEAD:%s" % FLEET_REPORT).stdout).hexdigest()
    fleet_blob = _g(fleet, "rev-parse", "HEAD:%s" % FLEET_REPORT).stdout.strip()
    ledger = {"round": 76, "claim": "Ca", "base": base, "fleet_pin": fleet_pin,
              "fleet_report": {"path": FLEET_REPORT, "pin": fleet_pin,
                               "blob": fleet_blob, "sha256": fleet_sha},
              "must_track": [], "pairs": pairs}
    claims = {"round": 76, "base": base, "frozen": None,
              "claims": [{"id": "C", "axis": "coverage",
                          "row_set": [{"id": LANE_ROW_ID}],
                          "entries": [CLAIM_C_ENTRY]},
                         {"id": "Ca", "axis": "calibration",
                          "ledger": LEDGER_REL,
                          "legs": claims_legs or _claims_legs(base, r75)}]}
    if claims_mutate:
        claims_mutate(claims)
    _write(lane, CLAIMS_REL, json.dumps(claims, indent=1) + "\n")
    _write(lane, LEDGER_REL, json.dumps(ledger, indent=1) + "\n")
    # the R1EXEMPT receipts are pre-freeze runs of the fixture trees, committed
    # with the freeze (the claim's do-nothing control reads them there)
    _write(lane, "reports/round-76/telemetry/r1exempt-green.txt",
           "# r1exempt green\nLEG PASS APPENDONLY\nexit 0\n")
    _write(lane, "reports/round-76/telemetry/r1exempt-red.txt",
           "# r1exempt red\nLEG FAIL APPENDONLY\nexit 1\n")
    if ledger_committed:
        freeze = _commit(lane, "freeze (claims + ledger)")
    else:
        freeze = _commit(lane, "freeze (claims only)", only=[CLAIMS_REL])
    _set_branch(lane, "freeze", freeze)
    _set_branch(lane, "r75", r75)
    _set_branch(lane, "main", freeze)

    # the clean landing: corrections rows, the repair, claim C's landing
    _write(lane, "SCORECARD.md", FIXTURE_FILES["SCORECARD.md"]
           + _corrections(pairs))
    _write(lane, "REPORT.md", "# report\n\nmode: legacy\n")
    _write(lane, CLAIM_C_ENTRY,
           "# calendar and era instruments\n\nbody\n")
    _write(lane, "corpus/SOURCES.md",
           FIXTURE_FILES["corpus/SOURCES.md"].rstrip("\n")
           + "\n| %s | calendar and era instruments — https://example.org/n | "
             "standard | B | calendar | abstract | compilation | mined | "
             "2026-10-27 | 180d | %s |\n"
             % (LANE_ROW_ID, CLAIM_C_ENTRY))
    _write(lane, "reports/round-76/telemetry/accept-ca-75-at-lands.txt",
           _stub_receipt(lane, r75, "reports/round-75/accept-ca.py",
                         "ACCEPT-CA-75", "12/12"))
    _write(lane, "reports/round-76/telemetry/r1exempt-green.txt",
           "# r1exempt green\nLEG PASS APPENDONLY\nexit 0\n")
    _write(lane, "reports/round-76/telemetry/r1exempt-red.txt",
           "# r1exempt red\nLEG FAIL APPENDONLY\nexit 1\n")
    clean = _commit(lane, "clean landing")
    _set_branch(lane, "clean", clean)
    _set_branch(lane, "main", clean)
    _at(lane, clean)
    # the combined receipt (the head measurement) and its stamped revision
    _write(lane, "reports/round-76/telemetry/measures-ca-head.txt",
           _stub_receipt(lane, clean, "reports/round-75/accept-ca.py",
                         "ACCEPT-CA-76", "12/12"))
    head = _commit(lane, "combined measurement")
    _set_branch(lane, "head", head)
    _set_branch(lane, "main", head)
    _at(lane, head)
    return lane, fleet, base, r75, freeze, clean, head


def _run_check(lane, lands, freeze, fleet, main_branch, combined=None):
    buf = io.StringIO()
    with redirect_stdout(buf):
        code = main_check(lane, lands, freeze, fleet, main_branch=main_branch,
                          combined_rev=combined)
    text = buf.getvalue()
    states = {}
    for line in text.splitlines():
        m = re.match(r"^LEG (PASS|FAIL) (\S+)$", line)
        if m:
            states[m.group(2)] = m.group(1)
    return code, states, text


def _fork(lane, name, rev):
    _branch(lane, name, rev)
    return name


def _landing(lane, name, base_rev, rows=None, receipts=True):
    """Branch from base_rev and lay down the clean landing shapes."""
    _fork(lane, name, base_rev)
    with open(os.path.join(lane, "SCORECARD.md"), "a", encoding="utf-8") as fh:
        fh.write(rows if rows is not None else _corrections(_pairs(
            _g(lane, "rev-parse", "base").stdout.strip())))
    _write(lane, "REPORT.md", "# report\n\nmode: legacy\n")
    if receipts:
        r75 = _g(lane, "rev-parse", "r75").stdout.strip()
        _write(lane, "reports/round-76/telemetry/accept-ca-75-at-lands.txt",
               _stub_receipt(lane, r75, "reports/round-75/accept-ca.py",
                             "ACCEPT-CA-75", "12/12"))
        _write(lane, "reports/round-76/telemetry/r1exempt-green.txt",
               "# r1exempt green\nLEG PASS APPENDONLY\nexit 0\n")
        _write(lane, "reports/round-76/telemetry/r1exempt-red.txt",
               "# r1exempt red\nLEG FAIL APPENDONLY\nexit 1\n")
    return _commit(lane, "landing %s" % name)


def selftest():
    results = []
    scenarios = []

    def check(label, cond, detail=""):
        results.append((label, bool(cond), detail))
        if not cond:
            print("SELFTEST FAIL: %s %s" % (label, detail))

    def scenario(label, lane, lands, freeze, fleet, main_branch, want_exit,
                 want, text_must=(), combined=None):
        scenarios.append(label)
        code, states, text = _run_check(lane, lands, freeze, fleet, main_branch,
                                        combined=combined)
        print("selftest: %s -> exit=%d %s" % (label, code,
                                              " ".join("%s=%s" % (k, states.get(k, "-"))
                                                       for k in REQUIRED_LEGS)))
        check("%s exit" % label, code == want_exit,
              "got %d want %d" % (code, want_exit))
        for name, state in want.items():
            check("%s %s" % (label, name), states.get(name) == state,
                  "got %r want %r" % (states.get(name), state))
        for needle in text_must:
            check("%s text %r" % (label, needle), needle in text)
        return text

    td = tempfile.mkdtemp(prefix="r76-ca-selftest-", dir=scratch_dir())
    try:
        (lane, fleet, base, r75, freeze, clean, head) = _build(td, "main")
        legs = _claims_legs(base, r75)

        # 1. do-nothing control: lands == freeze, invoked WITH --combined so the
        # refusal rule and the COMBINED leg are not conflated (FROZENCFG green)
        do_nothing_text = scenario(
            "do-nothing", lane, freeze, freeze, fleet, "freeze", 1,
            {"LEDGER": "PASS", "BASEMISMATCH": "PASS", "REPAIR": "FAIL",
             "ANNOTATE": "FAIL", "APPENDONLY": "PASS", "R1EXEMPT": "PASS",
             "NOSTUB": "FAIL", "SEPARABLE": "PASS", "RECEIPTS": "FAIL",
             "COMBINED": "PASS", "FROZENCFG": "PASS", "STAMP": "PASS"},
            ("red=11 min=10",), combined=head)
        check("do-nothing output leaks no lane id/family",
              not _leaks(do_nothing_text), str(_leaks(do_nothing_text)))

        # 2. clean landing
        clean_text = scenario("clean", lane, clean, freeze, fleet, "clean", 0,
                              {name: "PASS" for name in REQUIRED_LEGS},
                              ("ACCEPT-CA-76: PASS legs=12/12",),
                              combined=head)
        check("clean output leaks no lane id/family", not _leaks(clean_text),
              str(_leaks(clean_text)))

        # 3. lands == frozen base is a refusal printing FAIL
        scenario("lands-eq-base", lane, base, freeze, fleet, "clean", 2,
                 {}, ("refused", "ACCEPT-CA-76: FAIL", "equals the frozen base"),
                 combined=head)

        # 3b. a missing --combined is a REFUSAL, never a red COMBINED leg
        missing_combined = scenario(
            "combined-required", lane, clean, freeze, fleet, "clean", 2, {},
            ("refused", "--combined", "ACCEPT-CA-76: FAIL"))
        check("combined-required says no leg ran",
              "LEG " not in missing_combined)

        # 3c. no scratch root is a REFUSAL, never a write under a temp dir
        env = {k: v for k, v in os.environ.items()
               if k not in ("HYAKU_SCRATCH", "TMPDIR")}
        argv = [sys.executable, "-B", os.path.abspath(__file__),
                "--root", lane, "--lands", clean, "--freeze", freeze,
                "--fleet-root", fleet, "--combined", head]
        proc = subprocess.run(argv, cwd=lane, capture_output=True, text=True,
                              env=env, timeout=120)
        scenarios.append("scratch-noroot")
        check("scratch-noroot exit", proc.returncode == 2,
              "got %d" % proc.returncode)
        check("scratch-noroot refusal", "no scratch root" in proc.stdout,
              proc.stdout[-200:])
        check("scratch-noroot runs no leg", "LEG " not in proc.stdout)

        # 4. LEGCOUNT: a frozen leg table of the wrong length is refused
        short_legs = legs[:-1]
        lane_lc, fleet_lc, base_lc, r75_lc, freeze_lc, clean_lc, head_lc = _build(
            td, "legcount", claims_legs=short_legs)
        text = scenario("legcount", lane_lc, clean_lc, freeze_lc, fleet_lc,
                        "clean", 2, {}, ("refused", "leg table"),
                        combined=head_lc)
        check("legcount names the frozen table", "LEDGER" in text)

        # 4b. LEGCOUNT: the same twelve names in another order are refused
        swapped = list(legs)
        swapped[0], swapped[1] = swapped[1], swapped[0]
        lane_ro, fleet_ro, _, _, freeze_ro, clean_ro, head_ro = _build(
            td, "legorder", claims_legs=swapped)
        scenario("legorder", lane_ro, clean_ro, freeze_ro, fleet_ro, "clean", 2,
                 {}, ("refused", "order included"), combined=head_ro)

        # 5. stub rows: id only
        stub = _landing(lane, "stub", freeze, rows="\n## Corrections — "
                        "round 76\n\n"
                        + "".join("- A%02d — corrected.\n" % i
                                  for i in range(1, 11))
                        + "- R01 — corrected.\n")
        scenario("stub-rows", lane, stub, freeze, fleet, "stub", 1,
                 {"ANNOTATE": "FAIL", "NOSTUB": "FAIL", "REPAIR": "PASS",
                  "APPENDONLY": "PASS", "FROZENCFG": "PASS", "STAMP": "PASS"},
                 combined=head)

        # 6. rows without the re-derivation command
        nocmd = _landing(lane, "nocmd", freeze, rows="\n## Corrections — "
                         "round 76\n\n"
                         + "".join("- A%02d — stated 0, observed 1.\n" % i
                                   for i in range(1, 11)))
        scenario("no-rederive", lane, nocmd, freeze, fleet, "nocmd", 1,
                 {"ANNOTATE": "PASS", "NOSTUB": "FAIL", "REPAIR": "PASS"},
                 combined=head)

        # 7. re-derivation command that prints another value
        def _fake_rederive(pairs, base=None):
            for pair in pairs:
                if pair["id"] == "A02":
                    pair["rederive"] = "grep -c zzz-no-such-key keys.txt"
            return pairs
        lane2, fleet2, base2, r742, freeze2, clean2, head2 = _build(
            td, "fakecmd", mutate_ledger=_fake_rederive)
        scenario("annotate-other-token", lane2, clean2, freeze2, fleet2, "clean",
                 1, {"ANNOTATE": "FAIL", "NOSTUB": "PASS", "SEPARABLE": "PASS"},
                 combined=head2)

        # 7b. a backtick inside a quoted re-derivation pattern is literal
        def _backtick(pairs, base=None):
            for pair in pairs:
                if pair["id"] == "A01":
                    pair["rederive"] = ("git grep -c -e key01 -e '`zz' %s -- "
                                        "keys.txt" % base)
            return pairs
        lane_bt, fleet_bt, _, _, freeze_bt, clean_bt, head_bt = _build(
            td, "backtick", mutate_ledger=_backtick)
        bt_text = scenario("rederive-backtick", lane_bt, clean_bt, freeze_bt,
                           fleet_bt, "clean", 0,
                           {"ANNOTATE": "PASS", "NOSTUB": "PASS"},
                           combined=head_bt)
        check("rederive-backtick not refused as a shell construct",
              "shell construct" not in bt_text)

        # 8-10. APPENDONLY
        logrem = _landing(lane, "logremoval", clean)
        _write(lane, "LOG.md", "# LOG\n")
        logrem = _commit(lane, "log line removed")
        scenario("append-only-removal", lane, logrem, freeze, fleet,
                 "logremoval", 1, {"APPENDONLY": "FAIL", "ANNOTATE": "PASS",
                                   "STAMP": "PASS"}, combined=head)
        scorrem = _landing(lane, "scorremoval", clean)
        _write(lane, "SCORECARD.md",
               FIXTURE_FILES["SCORECARD.md"].replace(
                   "| calibration | ACCEPT-CA-72 PASS legs=12/12 |\n", "")
               + _corrections(_pairs(base)))
        scorrem = _commit(lane, "scorecard row removed")
        scenario("protected-in-place", lane, scorrem, freeze, fleet,
                 "scorremoval", 1, {"APPENDONLY": "FAIL"}, combined=head)
        notesrem = _landing(lane, "notesremoval", clean)
        _write(lane, "NOTES.md", "# notes\n")
        notesrem = _commit(lane, "notes line removed")
        scenario("unnamed-in-place", lane, notesrem, freeze, fleet,
                 "notesremoval", 1, {"APPENDONLY": "FAIL"}, combined=head)

        # 11. R1: a rule-2 cell edit on a pre-existing SOURCES row is exempt
        r1green = _landing(lane, "r1green", clean)
        _write(lane, "corpus/SOURCES.md",
               FIXTURE_FILES["corpus/SOURCES.md"].replace(
                   "| mined | 2026-10-19 | on-release "
                   "| corpus/knowledge/linguistics/naming-systems.md |",
                   "| mined | 2026-10-19 | on-release "
                   "| corpus/knowledge/linguistics/naming-systems.md, "
                   + CLAIM_C_ENTRY + " |"))
        r1green = _commit(lane, "used-by cell edit (rule 2)")
        scenario("r1-rule2-exempt", lane, r1green, freeze, fleet, "r1green", 0,
                 {"APPENDONLY": "PASS", "R1EXEMPT": "PASS"},
                 ("ACCEPT-CA-76: PASS legs=12/12",), combined=head)

        # 12. R1: a teaches-cell edit on a pre-existing row is NOT exempt
        r1red = _landing(lane, "r1red", clean)
        _write(lane, "corpus/SOURCES.md",
               FIXTURE_FILES["corpus/SOURCES.md"].replace(
                   "About | catalogue |",
                   "About | catalogues and indexes |"))
        r1red = _commit(lane, "teaches cell edit (not rule 2)")
        scenario("r1-teaches-red", lane, r1red, freeze, fleet, "r1red", 1,
                 {"APPENDONLY": "FAIL"},
                 ("changed outside the rule-2 cells",), combined=head)

        # 12b. R1: a legitimate used-by edit must not buy a teaches edit
        r1mixed = _landing(lane, "r1mixed", clean)
        _write(lane, "corpus/SOURCES.md",
               FIXTURE_FILES["corpus/SOURCES.md"].replace(
                   "About | catalogue |",
                   "About | catalogues and indexes |").replace(
                   "corpus/knowledge/linguistics/naming-systems.md |",
                   "corpus/knowledge/linguistics/naming-systems.md, "
                   "corpus/knowledge/myth-symbol/other.md |"))
        r1mixed = _commit(lane, "teaches + used-by edit (mixed)")
        scenario("r1-mixed-red", lane, r1mixed, freeze, fleet, "r1mixed", 1,
                 {"APPENDONLY": "FAIL"},
                 ("changed outside the rule-2 cells",), combined=head)

        # 13-17. H2 guard: shell string, interpreter, constant printer,
        # out-of-clone, dead pin
        guard_cases = [
            ("shell-string", lambda ps, _b=None: _set_observe(
                ps, "A01", "git grep -c '^key01$' keys.txt"), "shell string"),
            ("interpreter", lambda ps, _b=None: _set_observe(
                ps, "A01", ["python3", "-c", "print(1)"]), "interpreter"),
            ("constant-printer", lambda ps, _b=None: _set_observe(
                ps, "A01", ["echo", "1"]), "not in the observe allowlist"),
            ("out-of-clone", lambda ps, _b=None: _set_observe(
                ps, "A01", ["wc", "-l", "/dev/null"]), "does not exist in the clone"),
            ("dead-pin", lambda ps, _b=None: _set_observe(
                ps, "A01", ["git", "show", "%s:keys.txt" % ("0" * 40)]),
             "does not resolve in the clone"),
        ]
        for label, mutate, needle in guard_cases:
            blame, afleet, _, _, afreeze, aclean, ahead = _build(
                td, "guard-" + label, mutate_ledger=mutate)
            code, states, text = _run_check(blame, aclean, afreeze, afleet,
                                            "clean", combined=ahead)
            scenarios.append(label)
            print("selftest: %s -> exit=%d LEDGER=%s"
                  % (label, code, states.get("LEDGER")))
            check("%s exit" % label, code == 1, "got %d" % code)
            check("%s LEDGER" % label, states.get("LEDGER") == "FAIL")
            check("%s guard text" % label, needle in text,
                  "want %r in output" % needle)

        # 18. absence pair: base token 0, after-state 1
        def _absence(pairs, base=None):
            _set_observe(pairs, "A01",
                         ["git", "grep", "-c", "^zzz-absent$", base, "--",
                          "keys.txt"])
            for pair in pairs:
                if pair["id"] == "A01":
                    pair["rederive"] = "git grep -c ^zzz-absent$ %s -- keys.txt" % base
            return pairs
        lane_ab, fleet_ab, _, _, freeze_ab, clean_ab, head_ab = _build(
            td, "absence", mutate_ledger=_absence)
        scenario("absence-pair", lane_ab, clean_ab, freeze_ab, fleet_ab, "clean",
                 1, {"LEDGER": "FAIL"}, ("absence-observation pair",),
                 combined=head_ab)

        # 19. pair floor
        short = _pairs(base)[:9]
        lane3, fleet3, _, _, freeze3, _, head3 = _build(td, "short", pairs=short)
        code, states, _ = _run_check(lane3, freeze3, freeze3, fleet3, "freeze",
                                     combined=head3)
        scenarios.append("min-pairs")
        check("min-pairs exit", code == 1)
        check("min-pairs LEDGER", states.get("LEDGER") == "FAIL")
        check("min-pairs BASEMISMATCH", states.get("BASEMISMATCH") == "FAIL")

        # 20-21. config edited in the graded tree
        ledgeredit = _landing(lane, "ledgeredit", clean)
        with open(os.path.join(lane, LEDGER_REL), "a", encoding="utf-8") as fh:
            fh.write("\n")
        ledgeredit = _commit(lane, "ledger edited after freeze")
        scenario("config-edit-ledger", lane, ledgeredit, freeze, fleet,
                 "ledgeredit", 1,
                 {"FROZENCFG": "FAIL", "LEDGER": "PASS", "REPAIR": "PASS",
                  "ANNOTATE": "PASS", "STAMP": "PASS"}, combined=head)
        claimsedit = _landing(lane, "claimsedit", clean)
        with open(os.path.join(lane, CLAIMS_REL), "a", encoding="utf-8") as fh:
            fh.write("\n")
        claimsedit = _commit(lane, "claims edited after freeze")
        scenario("config-edit-claims", lane, claimsedit, freeze, fleet,
                 "claimsedit", 1,
                 {"FROZENCFG": "FAIL", "REPAIR": "PASS", "LEDGER": "PASS"},
                 combined=head)

        # 22. freeze that is an ancestor but not on the first-parent chain
        _branch(lane, "sidebranch", base)
        _write(lane, "SIDE.md", "side\n")
        side = _commit(lane, "side commit")
        _g(lane, "merge", "-q", "--no-ff", "-m", "merge freeze into side",
           freeze)
        ofp = _g(lane, "rev-parse", "HEAD").stdout.strip()
        _set_branch(lane, "offp", ofp)
        scenario("freeze-off-first-parent", lane, ofp, freeze, fleet, "offp", 1,
                 {"FROZENCFG": "FAIL"}, ("first-parent chain",), combined=head)

        # 23. REPAIR without statement_after
        def _no_statement(pairs, base=None):
            for pair in pairs:
                pair.pop("statement_after", None)
            return pairs
        lane4, fleet4, _, _, freeze4, clean4, head4 = _build(
            td, "nostatement", mutate_ledger=_no_statement)
        scenario("repair-no-statement", lane4, clean4, freeze4, fleet4, "clean",
                 1, {"LEDGER": "FAIL", "REPAIR": "FAIL"}, combined=head4)

        # 23b. a REPAIR pair on a file the frozen text does not call mutable
        def _not_mutable(pairs, base=None):
            for pair in pairs:
                if pair["id"] == "R01":
                    pair["statement_after"]["path"] = "NOTES.md"
            return pairs
        lane_nm, fleet_nm, _, _, freeze_nm, clean_nm, head_nm = _build(
            td, "notmutable", mutate_ledger=_not_mutable)
        scenario("repair-not-mutable", lane_nm, clean_nm, freeze_nm, fleet_nm,
                 "clean", 1, {"LEDGER": "FAIL"},
                 ("frozen mutable files",), combined=head_nm)

        # 23c. an ANNOTATE pair filed on a mutable file skips its repair
        def _annotate_mutable(pairs, base=None):
            for pair in pairs:
                if pair["id"] == "A01":
                    pair["stated_at"] = "REPORT.md:1"
            return pairs
        lane_am, fleet_am, _, _, freeze_am, clean_am, head_am = _build(
            td, "annotmutable", mutate_ledger=_annotate_mutable)
        scenario("annotate-on-mutable", lane_am, clean_am, freeze_am, fleet_am,
                 "clean", 1, {"LEDGER": "FAIL"},
                 ("frozen append-only files",), combined=head_am)

        # 24. shadow repair: base line restored, new value appended
        shadow = _landing(lane, "shadow", clean)
        _write(lane, "REPORT.md", "# report\n\nmode: old-doc\nmode: legacy\n")
        shadow = _commit(lane, "shadow append")
        scenario("shadow-repair", lane, shadow, freeze, fleet, "shadow", 1,
                 {"REPAIR": "FAIL", "ANNOTATE": "PASS"}, combined=head)

        # 25-26. SEPARABLE: a lane row id and the claim-C path families
        sepsid = _landing(lane, "sepsid", clean)
        with open(os.path.join(lane, "SCORECARD.md"), "a", encoding="utf-8") as fh:
            fh.write("| A01 | 0 | 1 | git grep -c ^key01$ %s -- keys.txt | "
                     "see %s |\n" % (base, LANE_ROW_ID))
        sepsid = _commit(lane, "row cites the lane row id")
        scenario("separable-lane-row", lane, sepsid, freeze, fleet, "sepsid", 1,
                 {"SEPARABLE": "FAIL", "ANNOTATE": "PASS", "NOSTUB": "PASS"},
                 combined=head)

        def _family(pairs, base=None):
            for pair in pairs:
                if pair["id"] == "A02":
                    pair["expected_after"] = "%s*" % C_FAMILIES[1]
            return pairs
        lane5, fleet5, _, _, freeze5, clean5, head5 = _build(
            td, "family", mutate_ledger=_family)
        family_text = scenario(
            "separable-family", lane5, clean5, freeze5, fleet5, "clean", 1,
            {"SEPARABLE": "FAIL", "ANNOTATE": "PASS"},
            ("names the frozen claim-C path family in ledger",), combined=head5)
        check("separable-family leaks no lane id/family",
              not _leaks(family_text), str(_leaks(family_text)))

        # 27. fabricated observed_at_base
        def _fake_base(pairs, base=None):
            pairs[0]["observed_at_base"] = "0"
            return pairs
        lane6, fleet6, _, _, freeze6, clean6, head6 = _build(td, "fakebase",
                                                             mutate_ledger=_fake_base)
        scenario("fabricated-base-observation", lane6, clean6, freeze6, fleet6,
                 "clean", 1, {"BASEMISMATCH": "FAIL", "LEDGER": "PASS"},
                 combined=head6)

        # 28. a pair that is green at base
        def _green(pairs, base=None):
            _set_observe(pairs, "A01",
                         ["git", "grep", "-c", "^zzz-none$", base, "--", "keys.txt"])
            return pairs
        lane7, fleet7, _, _, freeze7, clean7, head7 = _build(
            td, "green", mutate_ledger=_green)
        scenario("green-pair", lane7, clean7, freeze7, fleet7, "clean", 1,
                 {"BASEMISMATCH": "FAIL"}, combined=head7)

        # 29. stated_text present but not on the stated line
        def _offline(pairs, base=None):
            pairs[0]["stated_at"] = "STATEMENTS.md:10"
            return pairs
        lane8, fleet8, _, _, freeze8, clean8, head8 = _build(
            td, "offline", mutate_ledger=_offline)
        scenario("stated-line-mismatch", lane8, clean8, freeze8, fleet8,
                 "clean", 1, {"LEDGER": "FAIL"}, combined=head8)

        # 30. correction rows that merely MENTION the pair id
        prose = _landing(lane, "proserow", freeze, rows="\n## Corrections — "
                         "round 76\n\n"
                         + "".join("- same drift as A%02d (old 0, new 1): "
                                   "git grep -c ^key%02d$ %s -- keys.txt\n"
                                   % (i, i, base) for i in range(1, 11)))
        scenario("prose-row", lane, prose, freeze, fleet, "proserow", 1,
                 {"ANNOTATE": "FAIL", "NOSTUB": "FAIL", "REPAIR": "PASS"},
                 combined=head)

        # 31. expected_after disagrees with the re-read statement
        def _bad_expected(pairs, base=None):
            for pair in pairs:
                if pair["id"] == "R01":
                    pair["expected_after"] = "999"
            return pairs
        lane11, fleet11, _, _, freeze11, clean11, head11 = _build(
            td, "badexpected", mutate_ledger=_bad_expected)
        scenario("expected-after-mismatch", lane11, clean11, freeze11, fleet11,
                 "clean", 1, {"REPAIR": "FAIL", "LEDGER": "PASS"},
                 combined=head11)

        # 32. worktree-only ledger (never read)
        lane10, fleet10, _, _, freeze10, clean10, head10 = _build(
            td, "wtonly", ledger_committed=False)
        scenario("worktree-only-ledger", lane10, clean10, freeze10, fleet10,
                 "clean", 1, {"LEDGER": "FAIL"}, combined=head10)

        # 33. STAMP: measured revision differs from lands
        scenario("stamp-measured", lane, clean, freeze, fleet, "base", 1,
                 {"STAMP": "FAIL", "LEDGER": "PASS", "REPAIR": "PASS"},
                 ("measured",), combined=head)

        # 34. RECEIPTS: the round-75 counter stub fails its own legs, so the
        # re-run can never print the frozen PASS line
        lane_f, fleet_f, _, _, freeze_f, clean_f, head_f = _build(
            td, "r75fail",
            stub_counter=STUB_R75_CA.replace("ACCEPT-CA-75: PASS legs=12/12",
                                             "ACCEPT-CA-75: FAIL legs=11/12"))
        scenario("receipts-r75-fail", lane_f, clean_f, freeze_f, fleet_f,
                 "clean", 1, {"RECEIPTS": "FAIL"},
                 ("accept-ca-75 re-run",), combined=head_f)

        # 35. COMBINED: the combined tree does not carry claim C's landing
        lane_c, fleet_c, _, _, freeze_c, clean_c, head_c = _build(td, "nocomb")
        _g(lane_c, "rm", "-q", CLAIM_C_ENTRY)
        nocomb = _commit(lane_c, "claim C entry removed")
        scenario("combined-missing-entry", lane_c, nocomb, freeze_c, fleet_c,
                 "nocomb", 1, {"COMBINED": "FAIL"}, combined=nocomb)

        # 36. CLI input errors
        scenarios.append("cli-errors")
        check("cli bad lands", main(["--root", lane, "--lands", "nothex",
                                     "--freeze", freeze, "--fleet-root", fleet,
                                     "--combined", head]) == 2)
        check("cli missing freeze", main(["--root", lane, "--lands", clean,
                                          "--fleet-root", fleet]) == 2)
        check("cli nonexistent freeze",
              main(["--root", lane, "--lands", clean, "--freeze", "0" * 40,
                    "--fleet-root", fleet, "--combined", head]) == 2)

        # every implemented leg has a named failing mutant
        covered = {
            "LEDGER": ("guard-shell-string", "guard-interpreter",
                       "guard-constant-printer", "guard-out-of-clone",
                       "guard-dead-pin", "absence-pair", "min-pairs",
                       "stated-line-mismatch", "worktree-only-ledger",
                       "repair-no-statement", "repair-not-mutable",
                       "annotate-on-mutable"),
            "BASEMISMATCH": ("fabricated-base-observation", "green-pair",
                             "min-pairs"),
            "REPAIR": ("shadow-repair", "expected-after-mismatch",
                       "repair-no-statement"),
            "ANNOTATE": ("stub-rows", "annotate-other-token", "prose-row"),
            "APPENDONLY": ("append-only-removal", "protected-in-place",
                           "unnamed-in-place", "r1-teaches-red"),
            "R1EXEMPT": ("do-nothing", "r1-teaches-red", "r1-mixed-red"),
            "NOSTUB": ("stub-rows", "no-rederive", "prose-row"),
            "SEPARABLE": ("separable-lane-row", "separable-family"),
            "RECEIPTS": ("receipts-r75-fail", "do-nothing"),
            "COMBINED": ("combined-missing-entry", "do-nothing"),
            "FROZENCFG": ("config-edit-ledger", "config-edit-claims",
                          "freeze-off-first-parent"),
            "STAMP": ("stamp-measured",),
        }
        failing = {label for label, ok, _ in results if not ok}
        for leg_name, mutants in covered.items():
            if not any(m in scenarios for m in mutants):
                check("mutant coverage %s" % leg_name, False,
                      "no scenario named among %s" % (mutants,))
    finally:
        shutil.rmtree(td, ignore_errors=True)

    failures = [r for r in results if not r[1]]
    if failures:
        for label, _, detail in failures:
            print("SELFTEST FAIL: %s %s" % (label, detail))
        return 1
    print("SELFTEST OK: %d checks across %d scenarios reported-fail=0: %s"
          % (len(results), len(scenarios), ", ".join(scenarios)))
    print("SELFTEST: %d/%d" % (len(results), len(results)))
    return 0


LEAK_LITERALS = (LANE_ROW_ID, "S895", "S896", "S898") + C_FAMILIES


def _leaks(text):
    """Any lane id or claim-C family literal in printed output (must be empty)."""
    return [lit for lit in LEAK_LITERALS if lit in (text or "")]


def _set_observe(pairs, pid, cmd):
    for pair in pairs:
        if pair["id"] == pid:
            pair["observe_cmd"] = cmd
    return pairs


def main(argv=None):
    ap = argparse.ArgumentParser(
        description="round-76 calibration counter (claim Ca, freeze-pinned ledger)")
    ap.add_argument("--root", default=".")
    ap.add_argument("--lands")
    ap.add_argument("--freeze")
    ap.add_argument("--fleet-root")
    ap.add_argument("--main", default="main")
    ap.add_argument("--combined",
                    help="REQUIRED: the tree carrying BOTH landings (claim C's "
                         "and claim Ca's), graded by the COMBINED leg; a "
                         "missing value refuses the run")
    ap.add_argument("--work",
                    help="scratch root for clones and fixtures: --work, else "
                         "$HYAKU_SCRATCH, else $TMPDIR; with none set the "
                         "counter refuses instead of inventing the system temp "
                         "dir")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args(argv)
    if args.selftest:
        try:
            return selftest()
        except ScratchRefused as exc:
            print("SELFTEST: refused (%s)" % exc, file=sys.stderr)
            return 2
    if not args.lands or not args.freeze or not args.fleet_root:
        print("ERROR: --lands <40hex>, --freeze <40hex> and --fleet-root are "
              "required", file=sys.stderr)
        return 2
    lands = args.lands.lower()
    freeze = args.freeze.lower()
    combined = args.combined.lower() if args.combined else None
    for label, value in (("--lands", lands), ("freeze", freeze)):
        if not re.fullmatch(r"[0-9a-f]{40}", value):
            print("ERROR: %s must be 40 hex" % label, file=sys.stderr)
            return 2
    if combined and not re.fullmatch(r"[0-9a-f]{40}", combined):
        print("ERROR: --combined must be 40 hex", file=sys.stderr)
        return 2
    if not os.path.isdir(args.fleet_root):
        print("ERROR: --fleet-root %s is not a directory" % args.fleet_root,
              file=sys.stderr)
        return 2
    return main_check(args.root, lands, freeze, args.fleet_root,
                      main_branch=args.main, combined_rev=combined,
                      work=args.work)


if __name__ == "__main__":
    sys.exit(main())
