#!/usr/bin/env python3
r"""Round-74 calibration acceptance counter — claim Ca (freeze-pinned, ledger-driven).

Claim Ca (reports/round-74/claims.json, FINAL) grades the round's
self-assessment-versus-repo-state ledger.  The counter is data-driven: the ledger,
every constant and every allowlist it needs are read from the FREEZE commit
(`git show <freeze>:<path>`), observations are recomputed in throwaway clones, and
the graded tree's copies of the config are only COMPARED (leg FROZENCFG), never
read.  Parent: reports/round-73/accept-ca.py r3.

CLI (graded form)

  python3 -B reports/round-74/accept-ca.py --root . --lands <40hex>       --freeze <40hex> --fleet-root /home/vgpnk/Projects/shokunin
  python3 -B reports/round-74/accept-ca.py --selftest

EXIT: 0 all eleven legs pass; 1 any leg fails; 2 input error or REFUSAL.
Refusals (exit 2, printing `ACCEPT-CA-74: FAIL ... (REFUSED: ...)`): the frozen leg
table is not exactly the eleven implemented legs (LEGCOUNT); `--lands` equals the
frozen claims base; `freeze == lands` while every leg is green (a do-nothing shape
may not pass).  `--main` (default "main") is the ref STAMP's `measured` header is
read from; the graded invocation passes nothing.

LEDGER SCHEMA (reports/round-74/ledger.json at <freeze>)

  {round: 74, claim: "Ca", base: <40hex>,
   fleet_pin: <40hex>,                      APPENDONLY (fleet report)
   fleet_report: {path, pin, sha256, blob}  or a path string + fleet_sha256
   must_track: [<path> | {path, sha256}]    TRACKED; sha256 may also come from
                                            must_track_sha256 or content_pins'
                                            sha256_expected_after
   pairs: [{id, stated_at "path:line" | "fleet:<path>:<line>" + stated_fleet,
            stated_text, stated_parse|stated_token, observe_cmd (argv),
            parse, expected_after, disposition REPAIR|ANNOTATE,
            statement_after {path, parse} (REPAIR), rederive,
            observed_at_base (optional cross-check)}]}

  Every observation is an argv list executed with cwd inside a clone at the
  revision named by the pair (a 40-hex operand pins; `HEAD`/a path reads the graded
  clone), under the read-only allowlist.  No worktree byte is ever read.

LEGS (11 — the frozen claim Ca leg set; the table length is checked at freeze)

  LEDGER       committed at <freeze>; declares round 74 / claim Ca / base; at least
               the frozen pair floor (>= 10) unique pairs; each pair structurally
               valid: argv observe_cmd whose executable is in {git, grep, wc,
               sha256sum, ls, cat, head, tail, cut} (interpreters and echo/printf/
               true-class constant printers are refused, shell metacharacters are
               refused, path operands must exist in the clone and 40-hex operands
               must be objects of it); compiling parse with a capture group;
               stated_text found at stated_at in the BASE tree (on that line, or on
               the fleet line at the fleet pin); stated token anchored in
               stated_text; and NO absence-observation pair (a `git grep -c|-l`
               count that reads 0 at base whose expected_after is a positive
               count).
  BASEMISMATCH at the base revision, in a clone materialized at base, every pair is
               red (stated token != observed token), none is unobservable, none is
               a parse-miss, count >= the frozen floor, and a declared
               observed_at_base — compared by its LEADING whitespace-delimited
               token only, the rest being prose — equals the counter's own
               observation.
  REPAIR       every REPAIR pair: the truth observed in the clone at <lands> is
               observable; the statement re-read at <lands> (LAST regex match over
               statement_after.path) equals it; it differs from the base statement;
               the base stated_text is absent from that file at <lands>; the frozen
               after-state equals the re-read statement; and stated_at is never a
               line claim C appends to (a README totals/footer line).
  ANNOTATE     every ANNOTATE pair has a row under SCORECARD.md
               "## Corrections — round <frozen round>" whose FIRST CELL is the pair
               id and which carries the base stated token and the observed token,
               boundary-matched; the pair's re-derivation command is RE-RUN inside
               the counter (at <lands>) and must return the observed token; a count
               pair (numeric expected_after) must pin the frozen base revision in
               its observe_cmd.
  APPENDONLY   base..<lands> has zero removed lines in the frozen protected list
               (LOG.md, SCORECARD.md, the round-72/73/74 lessons,
               reports/round-73/claims.json, reports/round-73/ledger.json); the
               fleet round-73 report at the ledger's fleet_pin is byte-identical to
               the blob its sha256 names, unchanged at fleet HEAD, with no
               uncommitted bytes under the fleet root; every changed line elsewhere
               is a REPAIR pair's stated_at line or an appended line, EXCEPT the six
               must_track paths (pinned by TRACKED, not by the line rule).
  NOSTUB       every correction row carries id + old token + new token + the
               re-derivation command (executable under the allowlist) and no
               placeholder token ({TODO, TBD, FIXME, XXX, n/a, ?} or <...>).
  SEPARABLE    read set exactly: the ledger at <freeze>, every corrections row that
               LEADS with a pair id, the telemetry receipts/controls named in the
               claims Ca section, and the stated_at line of every pair.  No byte in
               that set cites a lane S-id that is IN the frozen claim-C row set
               (S881..S884, read from claim C's row_set at <freeze>; campaign-
               namespace ids such as S894/S909/S910 are not lane rows) or names the
               frozen claim-C path family; no stated_at path is in the frozen
               forbidden set; every observation is the token the pair's observe_cmd
               returns in the clone at the revision the ledger names.
  TRACKED      every must_track path is tracked at <freeze> and at <lands> with
               identical blob ids, non-empty, sha256 equal to the recorded value.
  RECEIPTS     materializes a clone of the frozen round-73 lands, pins its local
               main to it, re-runs accept-c-73 (--census-sh) and accept-ca-73
               (--main, --fleet-root) there, requires exit 0 and the exact lines
               `ACCEPT-C-73: PASS legs=11/11` / `ACCEPT-CA-73: PASS legs=9/9`, and
               requires the two committed receipts at <lands> to carry that stdout
               (volatile /tmp clone paths normalized) with
               stamped==evaluated==measured==that revision, the revision's tree and
               the round-73 counter sha256 values.
  FROZENCFG    every constant comes from `git show <freeze>:...`; <freeze> is a
               strict ancestor of <lands> on the first-parent chain (a
               `lands == freeze` run is graded, NOTE'd, and can never PASS); the
               frozen base is an ancestor of <freeze>; the graded tree's claims and
               ledger are byte-identical to the freeze blobs.
  STAMP        stamped/evaluated/measured/tree/counter-sha256 headers (QUALITY
               17/19 grammar of tools/check-receipt-seq.py), stamped == evaluated ==
               measured == <lands>, tree == `git rev-parse <lands>^{tree}`, counter
               sha256 == this file, every observation inside the clone.

PREDICATE READING, STATED (the frozen text does not decide these)

  * "red at base" = stated token != observed token, so an ANNOTATE pair stays red
    at <lands> and is closed by its correction row, not by a repo change.
  * "the statement re-read at <lands> (last occurrence)" = the LAST regex match over
    statement_after.path; a REPAIR pair without statement_after fails LEDGER.
  * "differs from the base statement" = the re-read token != the base token AND the
    base stated_text is absent from that file at <lands> (shadow-append closed).
  * correction rows are matched by LEADING id, never by a mention in prose.
  * "no absence-observation pair" is implemented on the count shape only: a
    `git grep -c|-l` argv reading 0 at base whose expected_after is a positive
    integer (ledger grammar R1 also supplies the zero-match token "0" so such a
    pair is diagnosable instead of "unobservable").
  * "count pairs measure at the pinned base revision" = an ANNOTATE pair whose
    expected_after is numeric must carry the frozen base revision as an operand.
  * `lands == freeze` keeps FROZENCFG green (the do-nothing control's required
    shape) but the driver refuses a PASS for that shape.
  * a `fleet:` stated_at (ledger grammar R5) is resolved at its stated_fleet pin;
    the pinned bytes must equal the fleet HEAD bytes and the recorded sha256.
  * RECEIPTS compares the re-executed stdout with the committed receipt after
    normalizing only /tmp materialization paths (the round-73 counters print their
    throwaway clone roots; both runs of each counter are byte-identical after that
    normalization — verified 2026-10-25 at 2d1cd91).
  * token containment is boundary-matched, so `0` is never found inside a hash.

USAGE (graded)

  python3 -B reports/round-74/accept-ca.py --root . --lands <lands> \
      --freeze <freeze> --fleet-root /home/vgpnk/Projects/shokunin
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
CLAIMS_REL = "reports/round-74/claims.json"
LEDGER_REL = "reports/round-74/ledger.json"
SCORECARD_REL = "SCORECARD.md"
TELEMETRY_DIR = "reports/round-74/telemetry"
FLEET_REPORT_DEFAULT = ".ufo/reports/round-73/kotodama.md"
REQUIRED_RECEIPTS = ("ACCEPT-C-73", "ACCEPT-CA-73")
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
STUB_TOKENS = {"todo", "tbd", "fixme", "xxx", "n/a", "?"}
STUB_ANGLE_RE = re.compile(r"<[^>]*>")
ABSENCE_EXPECT_RE = re.compile(r"^[1-9][0-9]*$")
PASS_LINES = {"accept-c-73": "ACCEPT-C-73: PASS legs=11/11",
              "accept-ca-73": "ACCEPT-CA-73: PASS legs=9/9"}
R73_COUNTERS = {"accept-c-73": "reports/round-73/accept-c.py",
                "accept-ca-73": "reports/round-73/accept-ca.py"}
RECEIPT_TMP_RE = re.compile(r"/(?:var/)?tmp/[^\s:,\"']+")
DISPOSITIONS = ("REPAIR", "ANNOTATE")
REQUIRED_LEGS = ("LEDGER", "BASEMISMATCH", "REPAIR", "ANNOTATE", "APPENDONLY",
                 "NOSTUB", "SEPARABLE", "TRACKED", "RECEIPTS", "FROZENCFG",
                 "STAMP")
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

RUN_STATE = {"outside_clone": False}


# --------------------------------------------------------------------------
# primitives
# --------------------------------------------------------------------------
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
        print("     %s" % detail)
    return bool(passed)


def note(text):
    print("     NOTE %s" % text)


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
    """MutLandedCa M01/M02: a row is evidence for a pair only when the pair id
    LEADS it (first table cell, or the list lead), never when it is mentioned."""
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


def hunks_with_removals(root, base, lands, path):
    d = git(root, "diff", "-U0", "--no-color", "%s..%s" % (base, lands),
            "--", path)
    n = 0
    for line in d.stdout.splitlines():
        m = re.match(r"^@@ -\d+(?:,(\d+))? \+\d+(?:,(\d+))? @@", line)
        if m and int(m.group(1) or 1) > 0:
            n += 1
    return n


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
        cfg["round"] = 74
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
    legs = claim.get("legs") if isinstance(claim.get("legs"), list) else []
    cfg["legs"] = legs
    names = [leg_name_of(x) for x in legs if leg_name_of(x)]
    cfg["leg_names"] = names
    if sorted(names) != sorted(REQUIRED_LEGS):
        problems.append("frozen leg set %s != the eleven implemented legs %s"
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
    m = re.search(r"S(\d{3,})", lt_sep)
    if not m:
        problems.append("SEPARABLE leg text names no S-id floor")
        cfg["separable_min_id"] = None
    else:
        cfg["separable_min_id"] = int(m.group(1))
    m = re.search(r"([a-z0-9][a-z0-9-]{5,})\*", lt_sep)
    if not m:
        problems.append("SEPARABLE leg text names no claim-C path family '<token>*'")
        cfg["c_family"] = None
    else:
        cfg["c_family"] = m.group(1)

    lt_app = _leg_text(legs, "APPENDONLY")
    m = re.search(r"zero removed lines in (.*?)(?:\(|;|$)", lt_app, re.S)
    protected = []
    if m:
        protected = re.findall(r"[A-Za-z0-9_./-]+\.(?:md|json)", m.group(1))
    seen = []
    for p in protected:
        if p not in seen:
            seen.append(p)
    cfg["protected"] = seen
    if not seen:
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

    ca_named = set()
    claim_text = json.dumps(claim, ensure_ascii=False)
    for item in re.findall(r"reports/round-[0-9]+/telemetry/[A-Za-z0-9_./-]+",
                           claim_text):
        ca_named.add(item.rstrip(".,;`)"))
    cfg["ca_named_paths"] = sorted(ca_named)

    lt_rec = _leg_text(legs, "RECEIPTS")
    receipt_paths = {}
    for m in re.finditer(
            r"((?:[A-Za-z0-9_./-]*/)?accept-c(a)?-73-at-[A-Za-z0-9_.-]+\.txt)",
            lt_rec):
        path = m.group(1)
        if "/" not in path:
            path = TELEMETRY_DIR + "/" + path
        receipt_paths["accept-ca-73" if m.group(2) else "accept-c-73"] = path
    cfg["receipt_paths"] = receipt_paths
    if set(receipt_paths) != set(PASS_LINES):
        problems.append("RECEIPTS leg text names %s, want both receipts"
                        % sorted(receipt_paths))

    m = re.search(r"([0-9a-f]{40})", lt_rec)
    if not m:
        problems.append("RECEIPTS leg text names no round-73 lands revision")
        cfg["receipts_rev"] = None
    else:
        cfg["receipts_rev"] = m.group(1)

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


def _resolve_in(clone, spec):
    """`<rev>:<path>` must resolve to an object of the clone."""
    return git(clone, "cat-file", "-e", spec).returncode == 0


def _bin(argv):
    return os.path.basename(argv[0]) if argv else ""


EMPTY_TREE = "4b825dc642cb6eb9a060e54bf8d69288fbee4904"
PATH_EXTS = (".md", ".txt", ".json", ".py", ".sh", ".yml", ".yaml", ".tsv")
GIT_GLOBAL_OPTS = ("-C", "-c", "--git-dir", "--work-tree", "--namespace",
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
        return True                      # git pathspec magic, e.g. :(exclude)*.md
    return any(ch in token for ch in "*?[")


def _git_problem(clone, args):
    if not args:
        return "git with no subcommand"
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
        return _git_grep_problem(clone, rest)
    if sub == "diff":
        return _git_diff_problem(clone, rest)
    for a in rest:
        if a.startswith("-") or a == "--":
            continue
        if re.fullmatch(r"[0-9a-f]{40}", a) or a in REV_NAMES:
            why = _git_rev_problem(clone, a)
            if why:
                return why
            continue
        if _pathspec_ok(a):
            continue
        if ":" in a and not os.path.isabs(a):
            if not _resolve_in(clone, a):
                return "git operand %r does not resolve in the clone" % a
            continue
        if "/" in a or a.endswith(PATH_EXTS):
            if not _exists_in(clone, a):
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
        if not _exists_in(clone, x):
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
        if not _exists_in(clone, x):
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


def observe_problem(argv, clone):
    """Static + dynamic H2 guard.  Static shape is clone-independent; the dynamic
    half resolves operands inside `clone` (the base clone for the LEDGER leg)."""
    if isinstance(argv, str):
        return "observe_cmd is a shell string, not an argv list"
    if not isinstance(argv, list) or not argv:
        return "observe_cmd is not a non-empty argv list"
    for a in argv:
        if not isinstance(a, str) or not a:
            return "observe_cmd element is not a non-empty string"
    for a in argv:
        for bad in SHELL_META:
            if bad in a:
                return "shell construct %r in argv element %r" % (bad, a[:60])
    binary = _bin(argv)
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


def run_observe(clone_path, argv, cwd_is_clone=True):
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
        p = subprocess.run(argv, cwd=clone_path, capture_output=True, text=True,
                           timeout=OBSERVE_TIMEOUT, env=env)
    except FileNotFoundError:
        return None, "missing-binary:%s" % argv[0]
    except subprocess.TimeoutExpired:
        return None, "timeout:%ss" % OBSERVE_TIMEOUT
    except OSError as exc:
        return None, "os-error:%s" % exc
    if p.stdout.strip() == "" and p.returncode != 0:
        # ledger grammar R1: `git grep -c|-l` with no match prints nothing and
        # exits 1 -- that is a ZERO observation, not an unobservable one.
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
    if len(argv) < 2 or argv[1] != "grep":
        return False
    return any(a in ("-c", "-l", "--count", "--files-with-matches")
               for a in argv[2:])


def observed_raw(pair, clone_path):
    """The raw normalized stdout, parse ignored (absence-pair detection)."""
    why = observe_problem(pair.get("observe_cmd"), clone_path)
    if why:
        return None
    out, why = run_observe(clone_path, pair["observe_cmd"])
    return norm(out) if out is not None else None


def observed_token(pair, clone_path):
    """(token, parsed, why).  An empty token is unobservable: fail closed."""
    why = observe_problem(pair.get("observe_cmd"), clone_path)
    if why:
        return None, False, "invalid-observe_cmd:%s" % why
    out, why = run_observe(clone_path, pair["observe_cmd"])
    if out is None:
        return None, False, why
    parse = pair.get("parse")
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
            return tok, True, why
        return None, False, "parse-miss(%s)" % why
    tok = norm(out)[:200]
    if not tok:
        return None, False, "empty-token"
    return tok, True, why


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
    """(token, found, why) — the LAST match over statement_after.path (frozen:
    "the statement re-read at <lands> (last occurrence)")."""
    spec = pair.get("statement_after")
    if not isinstance(spec, dict):
        return None, False, "no statement_after"
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
        rx = re.compile(parse)
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
    """Frozen sentence: committed at freeze, round 74 / claim Ca / base, >= 10
    unique pairs, structurally valid (argv over the read-only allowlist, no
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
        if pair.get("disposition") == "REPAIR":
            spec = pair.get("statement_after")
            if not isinstance(spec, dict):
                problems.append("%s: REPAIR without statement_after (the frozen "
                                "leg requires the statement re-read at lands)" % tag)
            else:
                path = spec.get("path")
                if not isinstance(path, str) or not path:
                    problems.append("%s: statement_after.path missing" % tag)
                elif not _exists_in(base_clone["path"], path):
                    problems.append("%s: statement_after path %s absent at base"
                                    % (tag, path))
                parse = spec.get("parse")
                if not isinstance(parse, str) or not parse:
                    problems.append("%s: statement_after.parse missing" % tag)
                else:
                    try:
                        rx = re.compile(parse)
                    except re.error as exc:
                        problems.append("%s: statement_after.parse: %s" % (tag, exc))
                    else:
                        if not rx.groups:
                            problems.append("%s: statement_after.parse has no "
                                            "capture group" % tag)
        stated_at = pair.get("stated_at")
        fleet_spec = pair.get("stated_fleet")
        if isinstance(fleet_spec, dict):
            # ledger grammar R5: a fleet statement site resolved with
            # `git -C <fleet> show <pin>:<path>`, never from the lane tree.
            fpath = fleet_spec.get("path")
            fpin = fleet_spec.get("pin")
            fline = fleet_spec.get("line")
            fsha = fleet_spec.get("sha256")
            body = None
            if not isinstance(fpath, str) or not fpath:
                problems.append("%s: stated_fleet.path missing" % tag)
            if not isinstance(fpin, str) or not re.fullmatch(r"[0-9a-f]{40}", fpin or ""):
                problems.append("%s: stated_fleet.pin is not 40-hex" % tag)
            elif not isinstance(fpath, str) or not fpath:
                pass
            else:
                body = show(cfg["fleet_root"], fpin, fpath)
                if body is None:
                    problems.append("%s: stated_fleet path %s absent at pin %s"
                                    % (tag, fpath, fpin[:12]))
                else:
                    if isinstance(fsha, str) and re.fullmatch(r"[0-9a-f]{64}", fsha):
                        if sha256_bytes(body) != fsha:
                            problems.append("%s: stated_fleet sha256 does not match "
                                            "the pinned bytes" % tag)
                    elif fsha is not None:
                        problems.append("%s: stated_fleet.sha256 is not 64-hex" % tag)
                    head_body = show(cfg["fleet_root"], "HEAD", fpath)
                    if head_body is None or sha256_bytes(head_body) != sha256_bytes(body):
                        problems.append("%s: fleet report bytes at fleet HEAD differ "
                                        "from the pinned bytes" % tag)
            if body is not None:
                lines = body.splitlines()
                if not isinstance(fline, int) or fline < 1 or fline > len(lines):
                    problems.append("%s: stated_fleet line %r out of range"
                                    % (tag, fline))
                elif norm(pair.get("stated_text") or "") not in norm(lines[fline - 1]):
                    problems.append("%s: stated_text not on fleet line %s:%s"
                                    % (tag, fpath, fline))
        else:
            m = re.match(r"^(.+):(\d+)$", stated_at or "")
            if not m:
                problems.append("%s: stated_at=%r is not path:line"
                                % (tag, stated_at))
            else:
                path, line_no = m.group(1), int(m.group(2))
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
                problems.append("%s: stated token %r not anchored in stated_text"
                                % (tag, tok[:40]))
        rec = pair.get("observed_at_base")
        if rec is not None and not isinstance(rec, str):
            problems.append("%s: observed_at_base is not a string" % tag)
        # no absence-observation pair: a zero count whose after-state is a
        # positive count can only turn green by this round appending the token
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
                              % (pid, rec[:40], obs[:40]))
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
    """A REPAIR pair may never read a line claim C appends to: the totals and
    footer lines of a README (the assignment's gloss of the frozen sentence)."""
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
        pins = [a for a in (pair.get("observe_cmd") or [])
                if isinstance(a, str) and re.search(
                    r"(?<![0-9a-f])[0-9a-f]{40}(?![0-9a-f])", a)]
        if pins:
            red.append("%s(observation pinned to %s; a REPAIR truth must be "
                       "observed in the clone at <lands>)" % (pid, pins[0][:12]))
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
            red.append("%s(statement=%r truth=%r)" % (pid, tok[:40], obs[:40]))
            continue
        if norm(tok) == norm(stated):
            red.append("%s(statement unchanged from base %r)" % (pid, stated[:40]))
            continue
        spec = pair.get("statement_after") or {}
        path = spec.get("path") or ""
        lands_text = show(cfg["root"], cfg["lands"], path)
        if lands_text is None:
            red.append("%s(statement path %s unreadable at lands)" % (pid, path))
            continue
        stext = norm(pair.get("stated_text") or "")
        if stext and stext in norm(lands_text):
            red.append("%s(base stated_text still present in %s)" % (pid, path))
            continue
        if norm(pair.get("expected_after")) != norm(tok):
            red.append("%s(expected_after=%r != statement=%r)"
                       % (pid, pair.get("expected_after")[:40], tok[:40]))
            continue
        green.append(pid)
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
                   "no '## Corrections \u2014 round %d' section; annotate-pairs=%d"
                   % (cfg["round"], len(annotate)))
    unannotated = []
    for idx, pair in annotate:
        pid = pair.get("id")
        tok = ev[idx]["stated"]
        obs, parsed, why = ev[idx]["lands"]
        if obs is None or tok is None:
            unannotated.append("%s(unobservable:%s)" % (pid, why))
            continue
        # count pairs measure at the pinned base revision: the frozen base must
        # be an operand of the observation (ledger grammar R3, frozen sentence
        # "count pairs measure at the pinned base revision").
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
                               % (pid, pid, norm(tok)[:40], norm(obs)[:40]))
            continue
        argv, why_argv = rederive_argv(pair)
        if argv is None:
            unannotated.append("%s(rederive %s)" % (pid, why_argv))
            continue
        why = observe_problem(argv, lands_clone["path"])
        if why:
            unannotated.append("%s(rederive not executable: %s)" % (pid, why))
            continue
        out_text, why = run_observe(lands_clone["path"], argv)
        if out_text is None:
            unannotated.append("%s(rederive %s)" % (pid, why))
            continue
        if not token_in(out_text, norm(obs)):
            unannotated.append("%s(rederive does not return %r; printed %r)"
                               % (pid, norm(obs)[:30], norm(out_text)[:40]))
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


def leg_appendonly(out, root, cfg, pairs, fleet_root):
    """Frozen sentence: zero removed lines in the seven protected files; the
    fleet round-73 report at the ledger's fleet_pin is byte-identical to the
    blob its sha256 names and this lane writes no byte under the fleet root;
    changed lines elsewhere are a subset of REPAIR stated_at lines plus
    appended lines."""
    base, lands = cfg["base"], cfg["lands"]
    problems = []
    protected = cfg.get("protected") or []
    if not protected:
        problems.append("no protected file list derived from the frozen leg")
    removed, ns = numstat_removed(root, base, lands, protected)
    if removed:
        problems.append("protected-removed=%d %s" % (removed, ns.strip()[:160]))
    repair_lines = {}
    for pair in pairs:
        if pair.get("disposition") != "REPAIR":
            continue
        m = re.match(r"^(.+):(\d+)$", pair.get("stated_at") or "")
        if m:
            repair_lines.setdefault(m.group(1), set()).add(int(m.group(2)))
    exempt = {path for path, _sha in _must_track(cfg.get("ledger_meta") or {})[0]}
    inplace = []
    for status, path in changed_files(root, base, lands):
        if path in protected:
            continue
        if path in exempt:
            continue  # the six must_track paths are pinned by TRACKED instead
        if status.startswith("A"):
            continue  # a new file is an appended file
        allowed = repair_lines.get(path, set())
        bad = []
        for old_start, old_count, new_start, new_count in _hunk_ranges(
                root, base, lands, path):
            if old_count == 0:
                continue  # pure append
            for line_no in range(old_start, old_start + old_count):
                if line_no not in allowed:
                    bad.append(line_no)
        if bad:
            problems.append("%s: changed lines outside REPAIR stated_at lines %s"
                            % (path, sorted(bad)[:6]))
        elif allowed:
            inplace.append(path)
    meta = cfg.get("ledger_meta") or {}
    pin = meta.get("fleet_pin")
    spec = meta.get("fleet_report")
    if isinstance(spec, dict):
        report = spec.get("path")
        pin = spec.get("pin") or pin
        recorded = spec.get("sha256")
        blob = spec.get("blob")
    else:
        report = spec if isinstance(spec, str) else None
        recorded = meta.get("fleet_sha256")
        blob = None
    if not isinstance(report, str) or not report:
        report = FLEET_REPORT_DEFAULT
    fleet_detail = "fleet-pin=%s report=%s" % (
        pin[:12] if isinstance(pin, str) else pin, report)
    if not isinstance(pin, str) or not re.fullmatch(r"[0-9a-f]{40}", pin or ""):
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
    detail = ("protected=%s protected-removed=%d %s repair-stated_at=%s "
              "must_track-exempt=%d" % (
                  protected, removed, fleet_detail,
                  {k: sorted(v) for k, v in repair_lines.items()}, len(exempt)))
    if problems:
        detail += " problems=%s" % problems
    return leg(out, "APPENDONLY", not problems, detail)


def _placeholder(token):
    low = norm(token or "").casefold()
    if low in STUB_TOKENS:
        return True
    return bool(STUB_ANGLE_RE.search(token or ""))


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
        elif observe_problem(argv, None):
            problems.append("rederive %s" % observe_problem(argv, None))
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
                stubs.append("%s:placeholder-token(%r)" % (pid, tokval))
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
    line of every pair."""
    problems = []
    scan = []
    min_id = cfg.get("separable_min_id")
    family = cfg.get("c_family")
    forbidden = cfg.get("separable_forbidden") or []
    if min_id is None or family is None:
        return leg(out, "SEPARABLE", False,
                   "frozen SEPARABLE constants not derivable "
                   "(id=%r family=%r)" % (min_id, family))
    if cfg.get("ledger_raw"):
        scan.append(("ledger", cfg["ledger_raw"]))
    ids = [p.get("id") for p in pairs if isinstance(p.get("id"), str)]
    rows = correction_rows(scor or "", cfg["round"]) or []
    ca_rows = [r for r in rows if any(row_starts_with_id(r, i) for i in ids)]
    if ca_rows:
        scan.append(("corrections-rows", "\n".join(ca_rows)))
    for path in cfg.get("ca_named_paths") or []:
        body = show(lands_clone["path"], "HEAD", path)
        if body is not None:
            scan.append((path, body))
    for pair in pairs:
        m = re.match(r"^(.+):(\d+)$", pair.get("stated_at") or "")
        spec = pair.get("stated_fleet")
        if isinstance(spec, dict):
            body = show(cfg["fleet_root"], spec.get("pin"), spec.get("path") or "")
            line = spec.get("line")
            path = "fleet:" + str(spec.get("path"))
        elif m:
            path, line = m.group(1), int(m.group(2))
            body = show(cfg["root"], cfg["base"], path)
        else:
            continue
        hit = _path_matches_forbidden(path, forbidden)
        if hit:
            problems.append("%s: stated_at path %s is a forbidden read (%s)"
                            % (pair.get("id"), path, hit))
        if body is not None and isinstance(line, int):
            lines = body.splitlines()
            if 1 <= line <= len(lines):
                scan.append(("stated:%s:%d" % (path, line), lines[line - 1]))
    lane_ids = set(cfg.get("lane_row_ids") or [])
    if not lane_ids:
        return leg(out, "SEPARABLE", False,
                   "the frozen claim-C row set is not derivable")
    for label, body in scan:
        for m in SID_RE.finditer(body):
            if int(m.group(1)) in lane_ids:
                problems.append("%s cites S%s (a claim-C lane row)"
                                % (label, m.group(1)))
        if family in body:
            problems.append("%s names the claim-C path family %s"
                            % (label, family))
    uniq = sorted(set(problems))
    return leg(out, "SEPARABLE", not uniq,
               "lane-ids=%s family=%s forbidden=%s scanned=%s problems=%s"
               % (sorted("S%d" % i for i in lane_ids), family, forbidden,
                  [s[0] for s in scan], uniq[:8]))



def _must_track(meta):
    raw = meta.get("must_track")
    shas = meta.get("must_track_sha256")
    if not isinstance(shas, dict):
        shas = {}
    out, problems = [], []
    if not isinstance(raw, list) or not raw:
        return [], ["ledger declares no must_track list"]
    for item in raw:
        if isinstance(item, dict):
            path = item.get("path")
            sha = item.get("sha256")
        elif isinstance(item, str):
            path = item
            sha = shas.get(item)
        else:
            problems.append("must_track entry %r is neither path nor object" % (item,))
            continue
        if not isinstance(path, str) or not path:
            problems.append("must_track entry without a path")
            continue
        if not isinstance(sha, str) or not re.fullmatch(r"[0-9a-f]{64}", sha):
            problems.append("%s: no 64-hex sha256 recorded in the ledger" % path)
            continue
        out.append((path, sha))
    return out, problems


def _must_track(meta):
    """[(path, sha256)] from must_track (strings or objects) + must_track_sha256
    + content_pins sha256_expected_after."""
    raw = meta.get("must_track")
    shas = meta.get("must_track_sha256")
    if not isinstance(shas, dict):
        shas = {}
    pins = {}
    for item in meta.get("content_pins") or []:
        if isinstance(item, dict) and isinstance(item.get("path"), str):
            sha = item.get("sha256_expected_after") or item.get("sha256")
            if isinstance(sha, str):
                pins[item["path"]] = sha
    out, problems = [], []
    if not isinstance(raw, list) or not raw:
        return [], ["ledger declares no must_track list"]
    for item in raw:
        if isinstance(item, dict):
            path = item.get("path")
            sha = item.get("sha256")
        elif isinstance(item, str):
            path = item
            sha = shas.get(item) or pins.get(item)
        else:
            problems.append("must_track entry %r is neither path nor object"
                            % (item,))
            continue
        if not isinstance(path, str) or not path:
            problems.append("must_track entry without a path")
            continue
        if not isinstance(sha, str) or not re.fullmatch(r"[0-9a-f]{64}", sha):
            problems.append("%s: no 64-hex sha256 recorded in the ledger" % path)
            continue
        out.append((path, sha))
    return out, problems


def leg_tracked(out, root, cfg, meta):
    """Frozen sentence: tracked at <freeze> and at <lands> with identical blob
    ids, non-empty, sha256 equal to the ledger's must_track values."""
    paths, problems = _must_track(meta)
    if not paths and problems:
        return leg(out, "TRACKED", False, problems[0])
    bad = list(problems)
    for path, sha in paths:
        ids = {}
        for label, rev in (("freeze", cfg["freeze"]), ("lands", cfg["lands"])):
            r = git(root, "rev-parse", "%s:%s" % (rev, path))
            if r.returncode != 0 or not r.stdout.strip():
                bad.append("%s not tracked at %s" % (path, label))
                continue
            ids[label] = r.stdout.strip()
            size = git(root, "cat-file", "-s", ids[label])
            if size.returncode != 0 or not size.stdout.strip().isdigit() \
                    or int(size.stdout.strip()) == 0:
                bad.append("%s empty at %s" % (path, label))
        if len(ids) != 2:
            continue
        if ids["freeze"] != ids["lands"]:
            bad.append("%s blob id differs between freeze (%s) and lands (%s)"
                       % (path, ids["freeze"][:12], ids["lands"][:12]))
            continue
        blob = git_bytes(root, "cat-file", "blob", ids["lands"])
        if blob.returncode != 0:
            bad.append("%s unreadable at lands" % path)
            continue
        if sha256_bytes(blob.stdout) != sha:
            bad.append("%s bytes != the recorded must_track sha256" % path)
    return leg(out, "TRACKED", not bad,
               "paths=%d problems=%s" % (len(paths), bad))


# --------------------------------------------------------------------------
# RECEIPTS (H6) and STAMP
# --------------------------------------------------------------------------
def parse_receipt_header(text):
    def first(rx):
        m = rx.search(text or "")
        return m.group(1) if m else None
    return {"stamped": first(STAMPED_RE), "evaluated": first(EVAL_RE),
            "measured": first(MEASURED_RE), "tree": first(TREE_RE),
            "sha": first(SHA_RE)}


def _pin_main_plain(clone_path, rev):
    """Pin the clone's local `main` to rev (throwaway clone only)."""
    r = git(clone_path, "checkout", "-q", "-B", "main", rev)
    ok = r.returncode == 0 and \
        git(clone_path, "rev-parse", "main").stdout.strip() == rev
    return ok, (r.stderr.strip() or "main != rev")


def normalize_receipt(text):
    """Volatile per-run tokens only: materialized clone roots under /tmp."""
    return RECEIPT_TMP_RE.sub("<TMP>", text or "")


def _run_r73_counter(clone_path, argv):
    env = {
        "PATH": os.environ.get("PATH", "/usr/local/bin:/usr/bin:/bin"),
        "HOME": os.environ.get("HOME", "/tmp"),
        "TMPDIR": os.environ.get("TMPDIR", "/tmp"),
        "LC_ALL": "C.UTF-8",
        "LANG": "C.UTF-8",
        "TZ": "UTC",
        "GIT_CONFIG_NOSYSTEM": "1",
        "GIT_TERMINAL_PROMPT": "0",
        "GIT_NO_REPLACE_OBJECTS": "1",
    }
    try:
        p = subprocess.run(argv, cwd=clone_path, capture_output=True, text=True,
                           timeout=1800, env=env)
    except (OSError, subprocess.TimeoutExpired) as exc:
        return None, str(exc)
    return p, ""


def leg_receipts(out, root, cfg, freeze_tmp, fleet_root):
    """Frozen sentence: materialize a clone of the round-73 lands, pin its local
    main to it, re-run accept-c-73 (--census-sh) and accept-ca-73 (--main,
    --fleet-root) there, require exit 0 and the exact PASS lines, and require
    the committed receipts at <lands> to carry that stdout with
    stamped==evaluated==measured==that revision and the round-73 counter sha256
    values."""
    problems = []
    rev = cfg.get("receipts_rev")
    if not rev:
        return leg(out, "RECEIPTS", False,
                   "frozen RECEIPTS leg names no round-73 lands revision")
    if not cfg.get("receipt_paths"):
        return leg(out, "RECEIPTS", False,
                   "frozen RECEIPTS leg names no receipt paths")
    census = os.path.join(fleet_root, "scripts", "sources-census.sh")
    if not os.path.isfile(census):
        problems.append("census script not found: %s" % census)
    commands = {
        "accept-c-73": [sys.executable, "-B", R73_COUNTERS["accept-c-73"],
                        "--root", ".", "--lands", rev, "--census-sh", census],
        "accept-ca-73": [sys.executable, "-B", R73_COUNTERS["accept-ca-73"],
                         "--root", ".", "--lands", rev, "--main", rev,
                         "--fleet-root", fleet_root],
    }
    clone = materialize(root, rev, freeze_tmp, "r73lands")
    if clone is None:
        return leg(out, "RECEIPTS", False,
                   "could not materialize the round-73 lands %s" % rev[:12])
    ok_main, why = _pin_main_plain(clone["path"], rev)
    if not ok_main:
        problems.append("could not pin the clone's local main: %s" % why)
    rerun = {}
    for key, argv in commands.items():
        proc, err = _run_r73_counter(clone["path"], argv)
        if proc is None:
            problems.append("%s re-run failed to execute: %s" % (key, err))
            continue
        if proc.returncode != 0:
            problems.append("%s re-run exit=%d (want 0)" % (key, proc.returncode))
        if PASS_LINES[key] not in proc.stdout.splitlines():
            problems.append("%s re-run did not print %r"
                            % (key, PASS_LINES[key]))
        rerun[key] = proc.stdout
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
            problems.append("%s: measured %s != %s"
                            % (path, hdr.get("measured"), rev[:12]))
        want_tree = git(root, "rev-parse", "%s^{tree}" % rev).stdout.strip()
        if want_tree and hdr.get("tree") != want_tree:
            problems.append("%s: tree %s != %s"
                            % (path, hdr.get("tree"), want_tree[:12]))
        blob = git_bytes(root, "show", "%s:%s" % (rev, R73_COUNTERS[key]))
        if blob.returncode != 0:
            problems.append("%s: %s is unreadable at %s"
                            % (path, R73_COUNTERS[key], rev[:12]))
        else:
            want_sha = sha256_bytes(blob.stdout)
            if hdr.get("sha") != want_sha:
                problems.append("%s: counter sha256 %s != the round-73 counter %s"
                                % (path, hdr.get("sha"), want_sha[:12]))
        if PASS_LINES[key] not in body.splitlines():
            problems.append("%s: does not carry %r" % (path, PASS_LINES[key]))
        if key in rerun:
            if normalize_receipt(body) != normalize_receipt(rerun[key]):
                problems.append("%s: committed stdout differs from the re-run "
                                "(%s vs %s)"
                                % (path,
                                   sha256_bytes(normalize_receipt(body))[:12],
                                   sha256_bytes(normalize_receipt(rerun[key]))[:12]))
            receipt_detail.append("%s=%s" % (key, sha256_bytes(body)[:12]))
    return leg(out, "RECEIPTS", not problems,
               "rev=%s receipts=%s problems=%s"
               % (rev[:12], receipt_detail, problems))


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
    detail = ("freeze=%s first-parent-of-lands; round=%r base=%s legs=%s "
              "min-pairs=%d separable>=S%s family=%s protected=%s receipts=%s"
              % (freeze[:12], cfg.get("round"),
                 (cfg.get("base") or "")[:12], cfg.get("leg_names"),
                 cfg.get("min_pairs"), cfg.get("separable_min_id"),
                 cfg.get("c_family"), cfg.get("protected"),
                 (cfg.get("receipts_rev") or "")[:12]))
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
    print("ACCEPT-CA-74: FAIL legs=0/11 (REFUSED: %s)" % message)
    return 2


def main_check(root, lands, freeze, fleet_root, main_branch="main",
               claims_rel=CLAIMS_REL, ledger_rel=LEDGER_REL):
    root = os.path.abspath(root)
    fleet_root = os.path.abspath(fleet_root)
    RUN_STATE["outside_clone"] = False
    out = []
    total_legs = len(REQUIRED_LEGS)

    if git(root, "cat-file", "-e", "%s^{commit}" % lands).returncode != 0:
        print("ERROR: --lands %s is not a commit in %s" % (lands, root),
              file=sys.stderr)
        return 2
    if git(root, "cat-file", "-e", "%s^{commit}" % freeze).returncode != 0:
        print("ERROR: --freeze %s is not a commit in %s" % (freeze, root),
              file=sys.stderr)
        return 2

    cfg, err = load_frozen(root, freeze, claims_rel, ledger_rel)
    if err:
        print("ERROR: %s" % err, file=sys.stderr)
        return 2
    # LEGCOUNT: the implemented leg table must be exactly the frozen leg table
    frozen_names = list(cfg.get("leg_names") or [])
    if len(frozen_names) != total_legs or sorted(frozen_names) != sorted(REQUIRED_LEGS):
        return _refuse("leg table %r != the frozen %d legs %r"
                       % (frozen_names, total_legs, list(REQUIRED_LEGS)))
    cfg.update({"root": root, "lands": lands, "freeze": freeze,
                "fleet_root": fleet_root})
    base = cfg.get("base")
    if not base or git(root, "cat-file", "-e", "%s^{commit}" % base).returncode != 0:
        print("ERROR: the frozen claims base %r is not a commit in %s"
              % (base, root), file=sys.stderr)
        return 2
    if lands == base:
        return _refuse("--lands equals the frozen base %s" % base[:12])

    tmpdir = tempfile.mkdtemp(prefix="r74-ca-")
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
                     pair.get("stated_at"), (tok or "")[:60],
                     (ob if ob is not None else "<%s>" % why)[:60],
                     (ol if ol is not None else "<%s>" % why_l)[:60],
                     str(pair.get("expected_after", ""))[:40]))

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
        leg_separable(out, cfg, pairs, ev, scor, clone)
        leg_tracked(out, root, cfg, meta)
        leg_receipts(out, root, cfg, tmpdir, fleet_root)
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
    print("ACCEPT-CA-74: %s legs=%d/%d"
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

STUB_C = '''#!/usr/bin/env python3
import argparse, hashlib, subprocess
ap = argparse.ArgumentParser()
ap.add_argument("--root", default=".")
ap.add_argument("--lands")
ap.add_argument("--census-sh")
ap.add_argument("--fleet-root")
ap.add_argument("--main", default="main")
ap.add_argument("--base")
args, _ = ap.parse_known_args()
sha = hashlib.sha256(open(__file__, "rb").read()).hexdigest()
tree = subprocess.run(["git", "-C", args.root, "rev-parse", args.lands + "^{tree}"],
                      capture_output=True, text=True).stdout.strip()
print("# counter sha256 (self): %s" % sha)
print("# stamped revision: %s" % args.lands)
print("# evaluated revision: %s" % args.lands)
print("# measured revision (lane main): %s" % args.lands)
print("# tree: %s" % tree)
print("ACCEPT-C-73: PASS legs=11/11")
'''
STUB_CA = STUB_C.replace("ACCEPT-C-73: PASS legs=11/11",
                         "ACCEPT-CA-73: PASS legs=9/9")

FIXTURE_FILES = {
    "LOG.md": "# LOG\n\n- round-72 entry\n",
    "SCORECARD.md": ("# SCORECARD\n\n| axis | verdict |\n|---|---|\n"
                     "| calibration | ACCEPT-CA-72 PASS legs=12/12 |\n"),
    "corpus/lessons/round-73.md": "# Round 73\n\n- lesson\n",
    "corpus/lessons/round-72.md": "# Round 72\n\n- lesson\n",
    "NOTES.md": "# notes\n\n- keep me in place\n",
    "REPORT.md": "# report\n\nmode: old-doc\n",
    "LIVE.md": "mode: legacy\n",
    ".ufo/waves/round-73/w2/Seat.md": "# Seat\n\n- inherited evidence\n",
    "IDS.md": "entries: 0 (S883)\nentries: 0 (S909)\n",
}
FIXTURE_KEYS = "".join("key%02d\n" % i for i in range(1, 11))
FIXTURE_STATEMENTS = "".join("row%02d entries: 0.\n" % i for i in range(1, 11))
FLEET_REPORT = ".ufo/reports/round-73/kotodama.md"
RECEIPTS = {"accept-c-73": "reports/round-74/telemetry/accept-c-73-at-lands.txt",
            "accept-ca-73": "reports/round-74/telemetry/accept-ca-73-at-lands.txt"}


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


def _claims_legs(base, r73):
    return [
        "LEDGER: reports/round-74/ledger.json is committed in the freeze commit "
        "and declares round 74 / claim Ca / base, >= 10 unique pairs, each "
        "structurally valid (argv observe_cmd over the read-only allowlist, no "
        "interpreters or constant printers, no shell metacharacters, compiling "
        "parse with a capture group, stated_text found at stated_at in the BASE "
        "tree, stated token anchored); no absence-observation pair",
        "BASEMISMATCH: at the base revision every pair has stated token != "
        "observed token and none is unobservable; >= 10 such pairs",
        "REPAIR: every REPAIR pair's statement re-read at <lands> (last "
        "occurrence) equals the truth observed in a clone at <lands> and differs "
        "from the base statement; never a line claim C appends to",
        "ANNOTATE: every ANNOTATE pair has a row under '## Corrections \u2014 "
        "round 74' naming the pair id, the base stated token and the observed "
        "token, and the row's re-derivation command is re-run and returns the "
        "observed token; count pairs measure at the pinned base revision",
        "APPENDONLY: base..<lands> has zero removed lines in LOG.md, SCORECARD.md, "
        "corpus/lessons/round-73.md, reports/round-73/claims.json; the fleet "
        "round-73 report at the ledger's fleet_pin is byte-identical to the blob "
        "its sha256 names and this lane writes no byte under the fleet root; "
        "changed lines elsewhere are a subset of the stated_at lines of REPAIR "
        "pairs plus appended lines",
        "NOSTUB: every correction row carries id + old token + new token + the "
        "re-derivation command and no placeholder token in {TODO, TBD, FIXME, "
        "XXX, n/a, ?} or <...>",
        "SEPARABLE: no byte in the read set cites S881, S882, S883 or S884 (the "
        "lane ids claim C adds) or names worldbuilding-setting-practice*; no "
        "stated_at path is corpus/SOURCES.md, corpus/knowledge/**, "
        "corpus/lessons/round-74.md",
        "TRACKED: the six inherited files are tracked at <freeze> and at <lands> "
        "with identical blob ids, non-empty, sha256 equal to must_track",
        "RECEIPTS: materializes a clone of the round-73 lands %s, pins local main "
        "to it, re-runs accept-c-73 (with --census-sh) and accept-ca-73 (with "
        "--main), requires exit 0 and `ACCEPT-C-73: PASS legs=11/11` / "
        "`ACCEPT-CA-73: PASS legs=9/9`, and requires "
        "reports/round-74/telemetry/accept-c-73-at-lands.txt and "
        "reports/round-74/telemetry/accept-ca-73-at-lands.txt to carry that "
        "stdout verbatim with stamped==evaluated==measured==%s" % (r73, r73),
        "FROZENCFG: ledger, constants and allowlists are read from `git show "
        "<freeze>:...`; <freeze> is a strict ancestor of <lands> on the "
        "first-parent chain; reports/round-74/claims.json and ledger.json at "
        "<lands> are byte-identical to the freeze blobs",
        "STAMP: the receipt carries the stamped/evaluated/measured revision, tree "
        "and counter-sha256 headers with stamped == evaluated == measured == "
        "<lands>, produced inside a clone materialized at <lands>",
    ]


def _corrections(pairs):
    lines = ["", "## Corrections \u2014 round 74", "",
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


def _stub_receipt(lane, rev, rel, name, legs):
    sha = hashlib.sha256(_g_bytes(lane, "show", "%s:%s" % (rev, rel)).stdout).hexdigest()
    tree = _g(lane, "rev-parse", "%s^{tree}" % rev).stdout.strip()
    return ("# counter sha256 (self): %s\n"
            "# stamped revision: %s\n"
            "# evaluated revision: %s\n"
            "# measured revision (lane main): %s\n"
            "# tree: %s\n"
            "%s: PASS legs=%s\n" % (sha, rev, rev, rev, tree, name, legs))


def _build(td, tag, pairs=None, ledger_committed=True, claims_legs=None,
           must_track_sha=True, mutate_ledger=None, nest_extra=None):
    """(lane, fleet, base, r73, freeze, clean).  Fresh repo per tag."""
    lane = os.path.join(td, tag, "lane")
    fleet = os.path.join(td, tag, "fleet")
    os.makedirs(lane)
    os.makedirs(fleet)
    _g(fleet, "init", "-q")
    _write(fleet, FLEET_REPORT, "# round-73 fleet report\n")
    _write(fleet, "scripts/sources-census.sh", "#!/bin/sh\nexit 0\n")
    os.chmod(os.path.join(fleet, "scripts/sources-census.sh"), 0o755)
    _commit(fleet, "fleet r73 report")
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

    _write(lane, "reports/round-73/accept-c.py", STUB_C)
    _write(lane, "reports/round-73/accept-ca.py", STUB_CA)
    r73 = _commit(lane, "round-73 lands (stub counters)")

    pairs = _pairs(base) if pairs is None else pairs
    if mutate_ledger:
        pairs = mutate_ledger(pairs, base)
    seat_sha = sha256_file(os.path.join(lane, ".ufo/waves/round-73/w2/Seat.md"))
    fleet_sha = hashlib.sha256(
        _g_bytes(fleet, "show", "HEAD:%s" % FLEET_REPORT).stdout).hexdigest()
    fleet_blob = _g(fleet, "rev-parse", "HEAD:%s" % FLEET_REPORT).stdout.strip()
    ledger = {"round": 74, "claim": "Ca", "base": base, "fleet_pin": fleet_pin,
              "fleet_report": {"path": FLEET_REPORT, "pin": fleet_pin,
                               "blob": fleet_blob, "sha256": fleet_sha},
              "must_track": ([{"path": ".ufo/waves/round-73/w2/Seat.md",
                               "sha256": seat_sha}] if must_track_sha else
                             [".ufo/waves/round-73/w2/Seat.md"]),
              "pairs": pairs}
    claims = {"round": 74, "base": base, "frozen": None,
              "claims": [{"id": "Ca", "axis": "calibration",
                          "ledger": LEDGER_REL,
                          "legs": claims_legs or _claims_legs(base, r73)}]}
    if nest_extra:
        nest_extra(claims)
    _write(lane, CLAIMS_REL, json.dumps(claims, indent=1) + "\n")
    _write(lane, LEDGER_REL, json.dumps(ledger, indent=1) + "\n")
    if ledger_committed:
        freeze = _commit(lane, "freeze (claims + ledger)")
    else:
        freeze = _commit(lane, "freeze (claims only)", only=[CLAIMS_REL])
    _set_branch(lane, "freeze", freeze)
    _set_branch(lane, "r73", r73)
    _set_branch(lane, "main", freeze)

    _write(lane, "SCORECARD.md", FIXTURE_FILES["SCORECARD.md"]
           + _corrections(pairs))
    _write(lane, "REPORT.md", "# report\n\nmode: legacy\n")
    _write(lane, RECEIPTS["accept-c-73"],
           _stub_receipt(lane, r73, "reports/round-73/accept-c.py",
                         "ACCEPT-C-73", "11/11"))
    _write(lane, RECEIPTS["accept-ca-73"],
           _stub_receipt(lane, r73, "reports/round-73/accept-ca.py",
                         "ACCEPT-CA-73", "9/9"))
    clean = _commit(lane, "clean landing")
    _set_branch(lane, "clean", clean)
    _set_branch(lane, "main", clean)
    _at(lane, clean)
    return lane, fleet, base, r73, freeze, clean


def _run_check(lane, lands, freeze, fleet, main_branch):
    buf = io.StringIO()
    with redirect_stdout(buf):
        code = main_check(lane, lands, freeze, fleet, main_branch=main_branch)
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


def _landing(lane, name, base_rev, repair=True, rows=None, receipts=True):
    """Branch from base_rev and lay down the clean landing shapes."""
    _fork(lane, name, base_rev)
    with open(os.path.join(lane, "SCORECARD.md"), "a", encoding="utf-8") as fh:
        fh.write(rows if rows is not None else _corrections(_pairs(
            _g(lane, "rev-parse", "base").stdout.strip())))
    if repair:
        _write(lane, "REPORT.md", "# report\n\nmode: legacy\n")
    if receipts:
        r73 = _g(lane, "rev-parse", "r73").stdout.strip() if _g(
            lane, "rev-parse", "--verify", "--quiet", "r73").returncode == 0 \
            else _g(lane, "rev-parse", "freeze").stdout.strip()
        for key, rel, name in (("accept-c-73", "reports/round-73/accept-c.py",
                                "ACCEPT-C-73"),
                               ("accept-ca-73", "reports/round-73/accept-ca.py",
                                "ACCEPT-CA-73")):
            _write(lane, RECEIPTS[key],
                   _stub_receipt(lane, r73, rel, name,
                                 "11/11" if key == "accept-c-73" else "9/9"))
    return _commit(lane, "landing %s" % name)


def selftest():
    results = []
    scenarios = []

    def check(label, cond, detail=""):
        results.append((label, bool(cond), detail))
        if not cond:
            print("SELFTEST FAIL: %s %s" % (label, detail))

    def scenario(label, lane, lands, freeze, fleet, main_branch, want_exit,
                 want, text_must=()):
        scenarios.append(label)
        code, states, text = _run_check(lane, lands, freeze, fleet, main_branch)
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

    td = tempfile.mkdtemp(prefix="r74-ca-selftest-")
    try:
        lane, fleet, base, r73, freeze, clean = _build(td, "main")
        legs = _claims_legs(base, r73)

        # 1. do-nothing control: lands == freeze (FROZENCFG stays green)
        scenario("do-nothing", lane, freeze, freeze, fleet, "freeze", 1,
                 {"LEDGER": "PASS", "BASEMISMATCH": "PASS", "REPAIR": "FAIL",
                  "ANNOTATE": "FAIL", "APPENDONLY": "PASS", "NOSTUB": "FAIL",
                  "SEPARABLE": "PASS", "TRACKED": "PASS", "RECEIPTS": "FAIL",
                  "FROZENCFG": "PASS", "STAMP": "PASS"},
                 ("red=11 min=10",))

        # 2. clean landing
        scenario("clean", lane, clean, freeze, fleet, "clean", 0,
                 {name: "PASS" for name in REQUIRED_LEGS},
                 ("ACCEPT-CA-74: PASS legs=11/11",))

        # 3. lands == frozen base is a refusal printing FAIL
        scenario("lands-eq-base", lane, base, freeze, fleet, "clean", 2,
                 {}, ("REFUSED", "ACCEPT-CA-74: FAIL"))

        # 4. LEGCOUNT: a frozen leg table of the wrong length is refused
        short_legs = legs[:-1]
        lane_lc, fleet_lc, base_lc, r73_lc, freeze_lc, clean_lc = _build(
            td, "legcount", claims_legs=short_legs)
        text = scenario("legcount", lane_lc, clean_lc, freeze_lc, fleet_lc,
                        "clean", 2, {}, ("REFUSED", "leg table"))
        check("legcount names the frozen table", "LEDGER" in text)

        # 5. stub rows: id only
        stub = _landing(lane, "stub", freeze, rows="\n## Corrections \u2014 "
                        "round 74\n\n"
                        + "".join("- A%02d \u2014 corrected.\n" % i
                                  for i in range(1, 11))
                        + "- R01 \u2014 corrected.\n")
        scenario("stub-rows", lane, stub, freeze, fleet, "stub", 1,
                 {"ANNOTATE": "FAIL", "NOSTUB": "FAIL", "REPAIR": "PASS",
                  "APPENDONLY": "PASS", "FROZENCFG": "PASS", "STAMP": "PASS"})

        # 6. rows without the re-derivation command
        nocmd = _landing(lane, "nocmd", freeze, rows="\n## Corrections \u2014 "
                         "round 74\n\n"
                         + "".join("- A%02d \u2014 stated 0, observed 1.\n" % i
                                   for i in range(1, 11)))
        scenario("no-rederive", lane, nocmd, freeze, fleet, "nocmd", 1,
                 {"ANNOTATE": "PASS", "NOSTUB": "FAIL", "REPAIR": "PASS"})

        # 7. re-derivation command that prints another value
        def _fake_rederive(pairs, base=None):
            for pair in pairs:
                if pair["id"] == "A02":
                    pair["rederive"] = "grep -c zzz-no-such-key keys.txt"
            return pairs
        lane2, fleet2, base2, r732, freeze2, clean2 = _build(
            td, "fakecmd", mutate_ledger=_fake_rederive)
        scenario("annotate-other-token", lane2, clean2, freeze2, fleet2, "clean",
                 1, {"ANNOTATE": "FAIL", "NOSTUB": "PASS", "SEPARABLE": "PASS"})

        # 8-10. APPENDONLY
        logrem = _landing(lane, "logremoval", clean)
        _write(lane, "LOG.md", "# LOG\n")
        logrem = _commit(lane, "log line removed")
        scenario("append-only-removal", lane, logrem, freeze, fleet,
                 "logremoval", 1, {"APPENDONLY": "FAIL", "ANNOTATE": "PASS",
                                   "STAMP": "PASS"})
        scorrem = _landing(lane, "scorremoval", clean)
        _write(lane, "SCORECARD.md",
               FIXTURE_FILES["SCORECARD.md"].replace(
                   "| calibration | ACCEPT-CA-72 PASS legs=12/12 |\n", "")
               + _corrections(_pairs(base)))
        scorrem = _commit(lane, "scorecard row removed")
        scenario("protected-in-place", lane, scorrem, freeze, fleet,
                 "scorremoval", 1, {"APPENDONLY": "FAIL"})
        notesrem = _landing(lane, "notesremoval", clean)
        _write(lane, "NOTES.md", "# notes\n")
        notesrem = _commit(lane, "notes line removed")
        scenario("unnamed-in-place", lane, notesrem, freeze, fleet,
                 "notesremoval", 1, {"APPENDONLY": "FAIL"})

        # 11-15. H2 guard: shell string, interpreter, constant printer,
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
            blame, afleet, _, _, afreeze, aclean = _build(td, "guard-" + label,
                                                          mutate_ledger=mutate)
            code, states, text = _run_check(blame, aclean, afreeze, afleet, "clean")
            scenarios.append(label)
            print("selftest: %s -> exit=%d LEDGER=%s"
                  % (label, code, states.get("LEDGER")))
            check("%s exit" % label, code == 1, "got %d" % code)
            check("%s LEDGER" % label, states.get("LEDGER") == "FAIL")
            check("%s guard text" % label, needle in text,
                  "want %r in output" % needle)

        # 16. absence pair: base token 0, after-state 1
        def _absence(pairs, base=None):
            _set_observe(pairs, "A01",
                         ["git", "grep", "-c", "^zzz-absent$", base, "--",
                          "keys.txt"])
            for pair in pairs:
                if pair["id"] == "A01":
                    pair["rederive"] = "git grep -c ^zzz-absent$ %s -- keys.txt" % base
            return pairs
        lane_ab, fleet_ab, _, _, freeze_ab, clean_ab = _build(
            td, "absence", mutate_ledger=_absence)
        scenario("absence-pair", lane_ab, clean_ab, freeze_ab, fleet_ab, "clean",
                 1, {"LEDGER": "FAIL"}, ("absence-observation pair",))

        # 17. pair floor
        short = _pairs(base)[:9]
        lane3, fleet3, base3, r733, freeze3, _ = _build(td, "short", pairs=short)
        code, states, _ = _run_check(lane3, freeze3, freeze3, fleet3, "freeze")
        scenarios.append("min-pairs")
        check("min-pairs exit", code == 1)
        check("min-pairs LEDGER", states.get("LEDGER") == "FAIL")
        check("min-pairs BASEMISMATCH", states.get("BASEMISMATCH") == "FAIL")

        # 18-19. config edited in the graded tree
        ledgeredit = _landing(lane, "ledgeredit", clean)
        with open(os.path.join(lane, LEDGER_REL), "a", encoding="utf-8") as fh:
            fh.write("\n")
        ledgeredit = _commit(lane, "ledger edited after freeze")
        scenario("config-edit-ledger", lane, ledgeredit, freeze, fleet,
                 "ledgeredit", 1,
                 {"FROZENCFG": "FAIL", "LEDGER": "PASS", "REPAIR": "PASS",
                  "ANNOTATE": "PASS", "STAMP": "PASS"})
        claimsedit = _landing(lane, "claimsedit", clean)
        with open(os.path.join(lane, CLAIMS_REL), "a", encoding="utf-8") as fh:
            fh.write("\n")
        claimsedit = _commit(lane, "claims edited after freeze")
        scenario("config-edit-claims", lane, claimsedit, freeze, fleet,
                 "claimsedit", 1,
                 {"FROZENCFG": "FAIL", "REPAIR": "PASS", "LEDGER": "PASS"})

        # 20. freeze that is an ancestor but not on the first-parent chain
        _branch(lane, "sidebranch", base)
        _write(lane, "SIDE.md", "side\n")
        side = _commit(lane, "side commit")
        _g(lane, "merge", "-q", "--no-ff", "-m", "merge freeze into side",
           freeze)
        ofp = _g(lane, "rev-parse", "HEAD").stdout.strip()
        _set_branch(lane, "offp", ofp)
        scenario("freeze-off-first-parent", lane, ofp, freeze, fleet, "offp", 1,
                 {"FROZENCFG": "FAIL"}, ("first-parent chain",))

        # 21. REPAIR without statement_after
        def _no_statement(pairs, base=None):
            for pair in pairs:
                pair.pop("statement_after", None)
            return pairs
        lane4, fleet4, _, _, freeze4, clean4 = _build(
            td, "nostatement", mutate_ledger=_no_statement)
        scenario("repair-no-statement", lane4, clean4, freeze4, fleet4, "clean",
                 1, {"LEDGER": "FAIL", "REPAIR": "FAIL"})

        # 22. shadow repair: base line restored, new value appended
        shadow = _landing(lane, "shadow", clean)
        _write(lane, "REPORT.md", "# report\n\nmode: old-doc\nmode: legacy\n")
        shadow = _commit(lane, "shadow append")
        scenario("shadow-repair", lane, shadow, freeze, fleet, "shadow", 1,
                 {"REPAIR": "FAIL", "ANNOTATE": "PASS"})

        # 23-24. TRACKED: missing / blob-id mismatch
        tmiss = _landing(lane, "trackedmissing", clean)
        _g(lane, "rm", "-q", ".ufo/waves/round-73/w2/Seat.md")
        tmiss = _commit(lane, "seat removed")
        scenario("tracked-missing", lane, tmiss, freeze, fleet, "trackedmissing",
                 1, {"TRACKED": "FAIL"})
        tblob = _landing(lane, "trackedblob", clean)
        _write(lane, ".ufo/waves/round-73/w2/Seat.md",
               "# Seat\n\n- inherited evidence\n- rewritten\n")
        tblob = _commit(lane, "seat blob changed")
        scenario("tracked-blob-mismatch", lane, tblob, freeze, fleet,
                 "trackedblob", 1, {"TRACKED": "FAIL", "APPENDONLY": "PASS"},
                 ("must_track-exempt=",))

        # 25-27. RECEIPTS
        typed = _landing(lane, "typedreceipt", clean)
        body = open(os.path.join(lane, RECEIPTS["accept-c-73"]),
                    encoding="utf-8").read()
        _write(lane, RECEIPTS["accept-c-73"],
               body.replace("ACCEPT-C-73: PASS legs=11/11",
                            "ACCEPT-C-73: PASS legs=11/11\nLEG PASS EXTRA"))
        typed = _commit(lane, "typed receipt")
        scenario("typed-receipt", lane, typed, freeze, fleet, "typedreceipt", 1,
                 {"RECEIPTS": "FAIL", "ANNOTATE": "PASS"})
        rrev = _landing(lane, "receiptrev", clean)
        _write(lane, RECEIPTS["accept-ca-73"],
               _stub_receipt(lane, freeze, "reports/round-73/accept-ca.py",
                             "ACCEPT-CA-73", "9/9"))
        rrev = _commit(lane, "receipt wrong revision")
        scenario("receipt-wrong-rev", lane, rrev, freeze, fleet, "receiptrev", 1,
                 {"RECEIPTS": "FAIL"})
        rmiss = _landing(lane, "receiptmissing", clean)
        _g(lane, "rm", "-q", RECEIPTS["accept-ca-73"])
        rmiss = _commit(lane, "receipt removed")
        scenario("receipt-missing", lane, rmiss, freeze, fleet, "receiptmissing",
                 1, {"RECEIPTS": "FAIL"})

        # 27b. SEPARABLE id test: the frozen claim-C row set, not ">= S881"
        def _stated_s883(pairs, base=None):
            for pair in pairs:
                if pair["id"] == "A02":
                    pair["stated_at"] = "IDS.md:1"
                    pair["stated_text"] = "entries: 0 (S883)"
                    pair["stated_parse"] = r"entries: (\d+)"
            return pairs
        lane_s1, fleet_s1, _, _, freeze_s1, clean_s1 = _build(
            td, "stated-s883", mutate_ledger=_stated_s883)
        scenario("separable-lane-row", lane_s1, clean_s1, freeze_s1, fleet_s1,
                 "clean", 1, {"SEPARABLE": "FAIL", "LEDGER": "PASS",
                              "ANNOTATE": "PASS", "REPAIR": "PASS"},
                 ("cites S883 (a claim-C lane row)",))

        def _stated_s909(pairs, base=None):
            for pair in pairs:
                if pair["id"] == "A02":
                    pair["stated_at"] = "IDS.md:2"
                    pair["stated_text"] = "entries: 0 (S909)"
                    pair["stated_parse"] = r"entries: (\d+)"
            return pairs
        lane_s2, fleet_s2, _, _, freeze_s2, clean_s2 = _build(
            td, "stated-s909", mutate_ledger=_stated_s909)
        scenario("separable-non-lane-id", lane_s2, clean_s2, freeze_s2, fleet_s2,
                 "clean", 0, {name: "PASS" for name in REQUIRED_LEGS},
                 ("stated:IDS.md:2",))

        # 27c. observed_at_base cross-check uses the leading token only
        def _prose_base(pairs, base=None):
            for pair in pairs:
                if pair["id"] == "A02":
                    pair["observed_at_base"] = "1 (key02 present in keys.txt)"
            return pairs
        lane_s3, fleet_s3, _, _, freeze_s3, clean_s3 = _build(
            td, "prose-base", mutate_ledger=_prose_base)
        scenario("basemismatch-leading-token", lane_s3, clean_s3, freeze_s3,
                 fleet_s3, "clean", 0,
                 {name: "PASS" for name in REQUIRED_LEGS})

        # 28-29. SEPARABLE
        sepsid = _landing(lane, "sepsid", clean)
        with open(os.path.join(lane, "SCORECARD.md"), "a", encoding="utf-8") as fh:
            fh.write("| A01 | 0 | 1 | git grep -c ^key01$ %s -- keys.txt | "
                     "see S881 |\n" % base)
        sepsid = _commit(lane, "row cites S881")
        scenario("separable-sid", lane, sepsid, freeze, fleet, "sepsid", 1,
                 {"SEPARABLE": "FAIL", "ANNOTATE": "PASS", "NOSTUB": "PASS"})

        def _family(pairs, base=None):
            for pair in pairs:
                if pair["id"] == "A02":
                    pair["expected_after"] = "worldbuilding-setting-practice*"
            return pairs
        lane5, fleet5, _, _, freeze5, clean5 = _build(td, "family",
                                                      mutate_ledger=_family)
        scenario("separable-family", lane5, clean5, freeze5, fleet5, "clean", 1,
                 {"SEPARABLE": "FAIL", "ANNOTATE": "PASS"})

        # 30. fabricated observed_at_base
        def _fake_base(pairs, base=None):
            pairs[0]["observed_at_base"] = "0"
            return pairs
        lane6, fleet6, _, _, freeze6, clean6 = _build(td, "fakebase",
                                                      mutate_ledger=_fake_base)
        scenario("fabricated-base-observation", lane6, clean6, freeze6, fleet6,
                 "clean", 1, {"BASEMISMATCH": "FAIL", "LEDGER": "PASS"})

        # 31. a pair that is green at base
        def _green(pairs, base=None):
            _set_observe(pairs, "A01",
                         ["git", "grep", "-c", "^zzz-none$", base, "--", "keys.txt"])
            return pairs
        lane7, fleet7, _, _, freeze7, clean7 = _build(td, "green",
                                                      mutate_ledger=_green)
        scenario("green-pair", lane7, clean7, freeze7, fleet7, "clean", 1,
                 {"BASEMISMATCH": "FAIL"})

        # 32. stated_text present but not on the stated line
        def _offline(pairs, base=None):
            pairs[0]["stated_at"] = "STATEMENTS.md:10"
            return pairs
        lane8, fleet8, _, _, freeze8, clean8 = _build(td, "offline",
                                                      mutate_ledger=_offline)
        scenario("stated-line-mismatch", lane8, clean8, freeze8, fleet8, "clean",
                 1, {"LEDGER": "FAIL"})

        # 33. correction rows that merely MENTION the pair id
        prose = _landing(lane, "proserow", freeze, rows="\n## Corrections \u2014 "
                         "round 74\n\n"
                         + "".join("- same drift as A%02d (old 0, new 1): "
                                   "git grep -c ^key%02d$ %s -- keys.txt\n"
                                   % (i, i, base) for i in range(1, 11)))
        scenario("prose-row", lane, prose, freeze, fleet, "proserow", 1,
                 {"ANNOTATE": "FAIL", "NOSTUB": "FAIL", "REPAIR": "PASS"})

        # 34. expected_after disagrees with the re-read statement
        def _bad_expected(pairs, base=None):
            for pair in pairs:
                if pair["id"] == "R01":
                    pair["expected_after"] = "999"
            return pairs
        lane11, fleet11, _, _, freeze11, clean11 = _build(
            td, "badexpected", mutate_ledger=_bad_expected)
        scenario("expected-after-mismatch", lane11, clean11, freeze11, fleet11,
                 "clean", 1, {"REPAIR": "FAIL", "LEDGER": "PASS"})

        # 34b. REPAIR whose observation is pinned to an older revision
        def _pinned_repair(pairs, base=None):
            for pair in pairs:
                if pair["id"] == "R01":
                    pair["observe_cmd"] = ["git", "show",
                                           "%s:LIVE.md" % base]
            return pairs
        lane12, fleet12, _, _, freeze12, clean12 = _build(
            td, "pinnedrepair", mutate_ledger=_pinned_repair)
        scenario("repair-pinned-observation", lane12, clean12, freeze12, fleet12,
                 "clean", 1, {"REPAIR": "FAIL"},
                 ("must be observed in the clone at <lands>",))

        # 35. worktree-only ledger (never read)
        lane10, fleet10, _, _, freeze10, clean10 = _build(
            td, "wtonly", ledger_committed=False)
        scenario("worktree-only-ledger", lane10, clean10, freeze10, fleet10,
                 "clean", 1, {"LEDGER": "FAIL"})

        # 36. STAMP: measured revision differs from lands
        scenario("stamp-measured", lane, clean, freeze, fleet, "base", 1,
                 {"STAMP": "FAIL", "LEDGER": "PASS", "REPAIR": "PASS"},
                 ("measured",))

        # 37. CLI input errors
        scenarios.append("cli-errors")
        check("cli bad lands", main(["--root", lane, "--lands", "nothex",
                                     "--freeze", freeze, "--fleet-root", fleet]) == 2)
        check("cli missing freeze", main(["--root", lane, "--lands", clean,
                                          "--fleet-root", fleet]) == 2)
        check("cli nonexistent freeze",
              main(["--root", lane, "--lands", clean, "--freeze", "0" * 40,
                    "--fleet-root", fleet]) == 2)

        # every implemented leg has a named failing mutant
        covered = {
            "LEDGER": ("guard-shell-string", "guard-interpreter",
                       "guard-constant-printer", "guard-out-of-clone",
                       "guard-dead-pin", "absence-pair", "min-pairs",
                       "stated-line-mismatch", "worktree-only-ledger"),
            "BASEMISMATCH": ("fabricated-base-observation", "green-pair",
                             "min-pairs", "basemismatch-leading-token"),
            "REPAIR": ("shadow-repair", "expected-after-mismatch",
                       "repair-no-statement", "repair-pinned-observation"),
            "ANNOTATE": ("stub-rows", "annotate-other-token", "prose-row"),
            "APPENDONLY": ("append-only-removal", "protected-in-place",
                           "unnamed-in-place", "tracked-blob-mismatch"),
            "NOSTUB": ("stub-rows", "no-rederive", "prose-row"),
            "SEPARABLE": ("separable-sid", "separable-family",
                          "separable-lane-row", "separable-non-lane-id"),
            "TRACKED": ("tracked-missing", "tracked-blob-mismatch"),
            "RECEIPTS": ("typed-receipt", "receipt-wrong-rev", "receipt-missing"),
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
    return 0


def _set_observe(pairs, pid, cmd):
    for pair in pairs:
        if pair["id"] == pid:
            pair["observe_cmd"] = cmd
    return pairs


def main(argv=None):
    ap = argparse.ArgumentParser(
        description="round-74 calibration counter (claim Ca, freeze-pinned ledger)")
    ap.add_argument("--root", default=".")
    ap.add_argument("--lands")
    ap.add_argument("--freeze")
    ap.add_argument("--fleet-root")
    ap.add_argument("--main", default="main")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args(argv)
    if args.selftest:
        return selftest()
    if not args.lands or not args.freeze or not args.fleet_root:
        print("ERROR: --lands <40hex>, --freeze <40hex> and --fleet-root are "
              "required", file=sys.stderr)
        return 2
    lands = args.lands.lower()
    freeze = args.freeze.lower()
    for label, value in (("--lands", lands), ("--freeze", freeze)):
        if not re.fullmatch(r"[0-9a-f]{40}", value):
            print("ERROR: %s must be 40 hex" % label, file=sys.stderr)
            return 2
    if not os.path.isdir(args.fleet_root):
        print("ERROR: --fleet-root %s is not a directory" % args.fleet_root,
              file=sys.stderr)
        return 2
    return main_check(args.root, lands, freeze, args.fleet_root,
                      main_branch=args.main)


if __name__ == "__main__":
    sys.exit(main())
