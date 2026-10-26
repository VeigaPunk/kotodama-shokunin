#!/usr/bin/env python3
r"""Junk-landing fixture generator for the kotodama round-75 counters.

Purpose
-------
Make the round-75 closure's acceptance surface *falsifiable*.  Each fixture
materializes, in a private mktemp directory under the round-75 scratch root,
a git tree that differs from a reference tree by exactly ONE named defect, and
grades that tree with the round-75 counter that owns the defect.  A correct
counter must REFUSE the junk landing; the fixture's `expected leg` names the
leg that must go red, and the receipt prints the whole leg table so a reviewer
can see (a) the verdict, (b) which legs are red, and (c) which legs the
mutation *newly* reddens relative to the unmutated reference tree.

Reference tree
--------------
The generator is *landing-relative*: it clones the lane, checks out a
reference revision (`--lands`, defaulting to the freeze commit), applies the
mutation, commits it in the clone only, and grades the commit.  Nothing is
ever written into the lane repository, its index, or its git/jj state; the
clone's `git rev-parse --show-toplevel` is asserted to be the clone before
any commit.

This matters for round 75: the freeze commit freezes claims.json, ledger.json,
the id-renumber map, both counters and the controls, but the *landing* (the
claim-C rows, entries, lesson, README rows, SCORECARD corrections and the
REPAIR edits) lands later.  A junk fixture is only attributable when the
reference tree is otherwise green, so the intended use is

    python3 -B .ufo/waves/round-75/counters/junk-fixtures.py --run \
        --freeze <freeze> --lands <landing-commit> --out-dir <dir>

When `--lands` is omitted the reference tree is the freeze commit itself; the
fixtures then still exercise the config / protected-file / ledger classes
(whose legs read frozen bytes), but the data legs are red for the trivial
reason that no landing exists, and the receipt's `newly-red` column is empty
for those legs.  The receipt always prints the baseline leg table next to the
mutant's so that distinction is never hidden.

FIXTURES (a correct counter REFUSES every one of them)

  J1   C   two header-only stub entries at the frozen entry paths, with the
           matching registry rows' used-by naming the stubs (ENTRIES)
  J2   C   the Gate admit quote is absent from every stored evidence window
           while the window sha256 still recomputes (EVIDENCE)
  J3   C   the graded tree's claims.json shrinks claim C to two rows and one
           entry (FROZENCFG)
  J4   Ca  every observe_cmd constant-prints expected_after — literal
           `python3 -c print(...)` / `echo`, in the GRADED TREE's ledger
           (FROZENCFG: the tree's ledger differs from the freeze)
  J4b  Ca  the same, evasive: `python3 -c "import os;assert os.sep;print(str(...))"`
           — passes a naive argv guard, reads no clone byte
  J4c  Ca  observe_cmd given as one shell string with metacharacters
           (`sh -c`-style / piped), not an argv
  J4m  Ca  the ledger carries fewer pairs than the frozen minimum, so the
           minimum-pairs clause of LEDGER cannot be met
  J4f  Ca  the FROZEN ledger itself constant-prints expected_after: the
           fixture's own commit is the freeze, so the counter's LEDGER leg
           READS the defective argv and must refuse it (LEDGER).  J4/J4b/J4c/J4m
           mutate the graded tree's ledger, which the counter never reads as
           its contract — only J4f reaches the LEDGER clause itself.
  J5   Ca  a `## Corrections — round 75` row names only its id (ANNOTATE/NOSTUB)
  J6   Ca  a frozen receipt outside every protected set is edited in place
           (APPENDONLY)
  J7   Ca  a non-rule-2 cell edit (teaches) on a pre-existing SOURCES row
           smuggled beside a rule-2 used-by edit on the same row — the
           exemption must NOT cover the teaches cell (APPENDONLY)
  J8   Ca  a byte in the Ca read set (a Corrections — round 75 row) cites the
           claim-C lane id S885 (SEPARABLE)
  J9   Ca  a receipt typed by hand: the stdout was never produced by a run and
           the stamps do not agree (RECEIPTS/STAMP)
  J10  Ca  a line is *removed* from a protected file (APPENDONLY)

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
    fx = jf.build("J3", freeze=jf.FREEZE, lands=jf.FREEZE, workroot=jf.SCRATCH)
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
SCRATCH = "/fast/scratch/hyaku/kotodama-r75/ExecJunkFixtures"

R75_CLAIMS = "reports/round-75/claims.json"
R75_LEDGER = "reports/round-75/ledger.json"
REGISTRY = "corpus/SOURCES.md"
SCORECARD = "SCORECARD.md"
LESSON = "corpus/lessons/round-75.md"
EVIDENCE_DIR = "reports/round-75/evidence"
TELEMETRY = "reports/round-75/telemetry"

# The counter bytes the L1 installs at the freeze commit; the wave copy is the
# fallback (a counter may live at either path).
C_COUNTER_CANDIDATES = ("reports/round-75/accept-c.py",
                        ".ufo/waves/round-75/counters/accept-c.py")
CA_COUNTER_CANDIDATES = ("reports/round-75/accept-ca.py",
                         ".ufo/waves/round-75/counters/accept-ca.py")

# The frozen Ca APPENDONLY leg names this protected set.  J6/J10 use it to
# pick a file that is *not* protected.
PROTECTED = (
    "LOG.md",
    "SCORECARD.md",
    "corpus/lessons/round-74.md",
    "corpus/lessons/round-73.md",
    "corpus/QUALITY.md",
    "SHONEN.md",
    "reports/round-73/claims.json",
    "reports/round-73/ledger.json",
)

# Frozen receipts that exist in the tree and are outside the protected set;
# J6 edits the first one that is present.
J6_CANDIDATES = (
    "reports/round-74/telemetry/accept-ca-73-at-lands.txt",
    "reports/round-74/telemetry/measures-ca.txt",
    "reports/round-73/telemetry/measures-ca72-rerun.txt",
    "reports/round-73/telemetry/selftest-r3.txt",
)

CORR_HEADING_RE = re.compile(r"^##\s+Corrections\s*[—–-]\s*round\s+(\d+)\b",
                             re.I | re.M)
ROW_RE = re.compile(r"^\s{0,3}\|\s*(S\d{3,})\s*\|")
ACCEPT_RE = re.compile(r"^ACCEPT-(C|CA)-\d+: (PASS|FAIL) legs=(\d+)/(\d+)",
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
                     "freeze lands base cell")


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


def clone_lane(workroot, label):
    """A private clone of the lane repo under a fresh mktemp directory.

    Returns (dir, repo).  The clone keeps the lane's history but its own refs
    and index; `git rev-parse --show-toplevel` is verified to be the clone
    before any commit, so no fixture commit can land anywhere else.
    """
    if workroot:
        os.makedirs(workroot, exist_ok=True)
        d = tempfile.mkdtemp(prefix="jf-%s-" % label, dir=workroot)
    else:
        d = tempfile.mkdtemp(prefix="jf-%s-" % label)
    repo = os.path.join(d, "repo")
    r = _run(["git", "clone", "-q", "--mirror", LANE, os.path.join(d, "mirror.git")])
    if r.returncode != 0:
        raise FixtureError("mirror clone of lane failed: %s" % r.stderr.strip())
    r = _run(["git", "clone", "-q", "--no-checkout",
              os.path.join(d, "mirror.git"), repo])
    if r.returncode != 0:
        raise FixtureError("clone of lane mirror failed: %s" % r.stderr.strip())
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
    return int(claims_doc.get("round") or 75)


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
    """Two header-only stub entries at the frozen entry paths, with the
    matching registry rows' used-by naming the stubs (ENTRIES)."""
    claims = ctx["claims"]
    entries = _entry_paths(claims)
    if len(entries) < 2:
        raise FixtureError("claim C names fewer than two entries")
    ids = _adopted_ids(claims)
    if len(ids) < 2:
        raise FixtureError("claim C names fewer than two adopted rows")
    urls = {}
    for row in _claims(claims, "C").get("row_set") or []:
        if isinstance(row, dict) and row.get("id"):
            urls[row["id"]] = row.get("document") or ""
    pairs = list(zip(entries[:2], ids[:2]))
    for path, rid in pairs:
        _stub_entry(repo, path, rid,
                    urls.get(rid) or "https://example.invalid/%s" % rid)
    # The matching registry rows must point their used-by at the stub paths.
    cols = registry_columns(repo)
    text = read(repo, REGISTRY)
    out = []
    touched = 0
    for line in text.splitlines(keepends=True):
        m = ROW_RE.match(line)
        if m and m.group(1) in {rid for _p, rid in pairs}:
            path = dict((rid, p) for p, rid in pairs)[m.group(1)]
            line = set_cell(line.rstrip("\n"), cols["used-by"],
                            sanitize_cell(path))
            line += "\n"
            touched += 1
        out.append(line)
    if touched == 0:
        raise FixtureError("no registry row for %s in the tree"
                           % ", ".join(rid for _p, rid in pairs))
    write(repo, REGISTRY, "".join(out))
    ctx["detail"] = ("stub entries %s (header only, no body); used-by of %s "
                     "rewritten to the stub path"
                     % (", ".join(p for p, _r in pairs),
                        ", ".join(r for _p, r in pairs)))


def _evidence_files(repo, ids):
    out = []
    for rid in ids:
        rel = "%s/%s.txt" % (EVIDENCE_DIR, rid)
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
        lesson = read(repo, LESSON)
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
    """The graded tree's claims.json shrinks claim C to two rows and one
    entry (FROZENCFG)."""
    doc = read_json(repo, R75_CLAIMS)
    claim = _claims(doc, "C")
    rows = [r for r in (claim.get("row_set") or []) if isinstance(r, dict)]
    if len(rows) < 2:
        raise FixtureError("claim C carries fewer than two rows")
    claim["row_set"] = rows[:2]
    claim["entries"] = (claim.get("entries") or [])[:1]
    write_json(repo, R75_CLAIMS, doc)
    ctx["detail"] = ("graded-tree claims.json narrowed to rows %s and %d entr%s"
                     % (", ".join(r.get("id", "?") for r in rows[:2]),
                        len(claim["entries"]),
                        "y" if len(claim["entries"]) == 1 else "ies"))


def junk_J4(repo, ctx):
    """Every observe_cmd constant-prints expected_after (literal)."""
    doc = read_json(repo, R75_LEDGER)
    write_json(repo, R75_LEDGER, rewrite_ledger_observe(doc, "literal"))
    ctx["detail"] = "every observe_cmd replaced by a literal constant printer"


def junk_J4b(repo, ctx):
    """The evasive constant printer: reads no clone byte, looks alive."""
    doc = read_json(repo, R75_LEDGER)
    write_json(repo, R75_LEDGER, rewrite_ledger_observe(doc, "evasive"))
    ctx["detail"] = ("every observe_cmd replaced by the evasive constant "
                     "printer (import os;assert os.sep;print(str(...)))")


def junk_J4c(repo, ctx):
    """observe_cmd given as one shell string with metacharacters."""
    doc = read_json(repo, R75_LEDGER)
    write_json(repo, R75_LEDGER, rewrite_ledger_observe(doc, "shell"))
    ctx["detail"] = ("every observe_cmd replaced by a single shell string "
                     "carrying metacharacters")


def junk_J4m(repo, ctx):
    """The ledger carries fewer pairs than the frozen minimum."""
    doc = read_json(repo, R75_LEDGER)
    pairs = doc.get("pairs") or []
    keep = pairs[:2]
    if len(pairs) < 3:
        raise FixtureError("ledger carries fewer than three pairs")
    doc["pairs"] = keep
    write_json(repo, R75_LEDGER, doc)
    ctx["detail"] = ("ledger trimmed to %d pairs (the frozen LEDGER leg "
                     "requires at least ten)" % len(keep))


def junk_J4f(repo, ctx):
    """The FROZEN ledger itself constant-prints expected_after.

    J4/J4b/J4c mutate the ledger in the GRADED TREE.  The counter reads its
    ledger from the freeze (`git show <freeze>:reports/round-75/ledger.json`),
    so a tree-level edit can only be caught as a FROZENCFG byte difference —
    it never reaches the LEDGER leg's own allowlist clause.  J4f therefore
    rewrites the ledger in the tree the counter FREEZE-PINS: the fixture's
    own freeze commit carries the constant printers, so the LEDGER leg reads
    them and must refuse the allowlist-violating argv.
    """
    doc = read_json(repo, R75_LEDGER)
    write_json(repo, R75_LEDGER, rewrite_ledger_observe(doc, "literal"))
    ctx["detail"] = ("the FROZEN ledger's every observe_cmd constant-prints "
                     "expected_after (literal print/echo); the counter's "
                     "LEDGER leg reads the freeze and must refuse the argv")
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
    """A `## Corrections — round 75` row names only its id."""
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
                     "`| %s |`" % (round_no, pid, pid))


def junk_J6(repo, ctx):
    """A frozen receipt outside every protected set is edited in place."""
    stated = {p.get("stated_at") for p in (ctx["ledger"].get("pairs") or [])}
    rel = None
    for cand in J6_CANDIDATES:
        if cand in PROTECTED or cand in stated:
            continue
        if os.path.isfile(os.path.join(repo, cand)):
            rel = cand
            break
    if rel is None:
        raise FixtureError("no unprotected frozen receipt found in the tree")
    text = read(repo, rel)
    m = re.search(r"legs=(\d+)/(\d+)", text)
    if not m:
        raise FixtureError("%s carries no legs=n/m verdict line" % rel)
    old = m.group(0)
    new = "legs=%s/%s" % (m.group(1), int(m.group(2)) + 1)
    write(repo, rel, replace_text(text, old, new, rel))
    ctx["detail"] = ("in-place edit of %s (%s -> %s); the file is outside the "
                     "protected set" % (rel, old, new))


def junk_J7(repo, ctx):
    """A non-rule-2 cell edit (teaches) smuggled beside a rule-2 used-by edit
    on the same pre-existing SOURCES row (APPENDONLY must still fail)."""
    cols = registry_columns(repo)
    rid = _rule2_row_id(repo, ctx)
    line = registry_row(repo, rid)
    used_by = split_cells(line)[cols["used-by"]].strip()
    teaches = split_cells(line)[cols["teaches"]].strip()
    new_teaches = sanitize_cell(teaches + " [junk fixture: non-rule-2 edit]")
    new_used_by = sanitize_cell(used_by + ("," if used_by else "")
                                + "corpus/knowledge/myth-symbol/comparative-frameworks.md")
    edited = set_cell(set_cell(line, cols["used-by"], new_used_by),
                      cols["teaches"], new_teaches)
    text = read(repo, REGISTRY)
    write(repo, REGISTRY,
          text.replace(line + "\n", edited + "\n", 1))
    ctx["detail"] = ("row %s: used-by cell extended (rule-2) AND teaches cell "
                     "edited (non-rule-2) on the same row" % rid)


def _rule2_row_id(repo, ctx):
    """A pre-existing registry row (not adopted this round)."""
    adopted = set(_adopted_ids(ctx["claims"]))
    ids = sorted(row_ids(read(repo, REGISTRY)))
    for rid in ids:
        if rid not in adopted:
            return rid
    raise FixtureError("no pre-existing registry row to edit")


def junk_J8(repo, ctx):
    """A byte in the Ca read set cites the claim-C lane id S885."""
    adopted = _adopted_ids(ctx["claims"])
    if not adopted:
        raise FixtureError("claim C carries no row_set")
    lane_id = adopted[0]
    pairs = _annotate_pairs(ctx)
    if not pairs:
        raise FixtureError("the frozen ledger carries no ANNOTATE pair")
    pid = pairs[0].get("id")
    row = ("| %s | %s | %s | %s | the round-75 registry row %s is claim C's |"
           % (pid,
              sanitize_cell(str(pairs[0].get("stated_text") or "")),
              sanitize_cell(str(pairs[0].get("expected_after") or "")),
              sanitize_cell(str(pairs[0].get("rederive") or "")),
              lane_id))
    text = read(repo, SCORECARD)
    write(repo, SCORECARD, append_correction_row(text, _round_of(ctx["claims"]),
                                                 row))
    ctx["detail"] = ("a Corrections — round %d row naming %s now cites the "
                     "claim-C lane id %s" % (_round_of(ctx["claims"]), pid,
                                            lane_id))


def junk_J9(repo, ctx):
    """A receipt typed by hand: the stdout was never produced by a run and the
    stamps do not agree (RECEIPTS/STAMP)."""
    rel = "%s/accept-ca-74-at-lands.txt" % TELEMETRY
    existed = os.path.isfile(os.path.join(repo, rel))
    tree = git(repo, "rev-parse", "%s^{tree}" % ctx["lands"]).strip()
    body = (
        "# typed by hand — this receipt was NOT produced by a counter run\n"
        "# counter sha256 (self): 0000000000000000000000000000000000000000"
        "000000000000000000000000\n"
        "# stamped revision: %s\n"
        "# evaluated revision: %s\n"
        "# measured revision (lane main): %s\n"
        "# tree: %s\n"
        "# claim: Ca  round: 75\n"
        "# counter: reports/round-74/accept-ca.py\n"
        "ACCEPT-CA-74: PASS legs=11/11\n"
        % (ctx["lands"], ctx["freeze"], ctx["base"], tree))
    write(repo, rel, body)
    ctx["detail"] = ("typed receipt %s (%s): hand-written PASS line, zeroed "
                     "counter sha256, and stamped/evaluated/measured set to "
                     "three different revisions"
                     % (rel, "replaced the landed receipt" if existed
                        else "added a receipt that no run produced"))


def junk_J10(repo, ctx):
    """A line is removed from a protected file (APPENDONLY)."""
    rel = "corpus/lessons/round-73.md"
    text = read(repo, rel)
    lines = text.splitlines(keepends=True)
    if len(lines) < 5:
        raise FixtureError("%s is too short to remove a line from" % rel)
    victim = lines[len(lines) // 2]
    if not victim.strip():
        victim = lines[len(lines) // 2 + 1]
    keep = lines[:len(lines) // 2] + lines[len(lines) // 2 + 1:]
    write(repo, rel, "".join(keep))
    ctx["detail"] = ("one line removed from the protected file %s: %r"
                     % (rel, victim.strip()[:60]))


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
           "FAIL: two header-only stub entries at the frozen entry paths, with "
           "the matching rows' used-by naming the stubs (ENTRIES)"),
    "J2": ("C", junk_J2, ("EVIDENCE",),
           "FAIL: the Gate admit quote is absent from every stored evidence "
           "window while the window sha256 still recomputes (EVIDENCE)"),
    "J3": ("C", junk_J3, ("FROZENCFG",),
           "FAIL: the graded tree's claims.json shrinks the claim to two rows "
           "and one entry (FROZENCFG)"),
    "J4": ("Ca", junk_J4, ("LEDGER", "FROZENCFG"),
           "FAIL: every observe_cmd constant-prints expected_after — literal "
           "print/echo (the graded tree's ledger differs from the freeze, so "
           "FROZENCFG is red and LEDGER's allowlist must reject the argv)"),
    "J4b": ("Ca", junk_J4b, ("LEDGER", "FROZENCFG"),
            "FAIL: the evasive constant printer reads no clone byte"),
    "J4c": ("Ca", junk_J4c, ("LEDGER", "FROZENCFG"),
            "FAIL: observe_cmd is a shell string with metacharacters, not an "
            "argv"),
    "J4m": ("Ca", junk_J4m, ("LEDGER", "FROZENCFG"),
            "FAIL: the ledger carries fewer pairs than the frozen minimum"),
    "J4f": ("Ca", junk_J4f, ("LEDGER",),
            "FAIL: the FROZEN ledger itself constant-prints expected_after — "
            "the counter's own LEDGER leg must read the freeze and refuse the "
            "allowlist-violating argv (this is the only fixture that reaches "
            "the LEDGER clause itself)"),
    "J5": ("Ca", junk_J5, ("ANNOTATE", "NOSTUB"),
           "FAIL: a Corrections — round 75 row names only its id "
           "(ANNOTATE/NOSTUB)"),
    "J6": ("Ca", junk_J6, ("APPENDONLY",),
           "FAIL: a frozen receipt outside every protected set is edited in "
           "place (APPENDONLY)"),
    "J7": ("Ca", junk_J7, ("APPENDONLY",),
           "FAIL: a non-rule-2 (teaches) cell edit smuggled beside a rule-2 "
           "used-by edit on one pre-existing row (APPENDONLY must still fail)"),
    "J8": ("Ca", junk_J8, ("SEPARABLE",),
           "FAIL: a byte in the Ca read set cites the claim-C lane id (SEPARABLE)"),
    "J9": ("Ca", junk_J9, ("RECEIPTS", "STAMP"),
           "FAIL: a receipt typed by hand — the stdout was never produced by a "
           "run and the stamps disagree (RECEIPTS/STAMP)"),
    "J10": ("Ca", junk_J10, ("APPENDONLY",),
            "FAIL: a line is removed from a protected file (APPENDONLY)"),
}

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

ORDER = ("J1", "J2", "J3", "J4", "J4b", "J4c", "J4m", "J4f", "J5", "J6",
         "J7", "J8", "J9", "J10")
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


def run_counter(repo, counter, rev, freeze, fleet_root=FLEET_ROOT,
                claim=None, extra=()):
    """Run one counter over `rev` and parse its verdict.

    Returns a dict: {exit, verdict, legs, total, red, green, tail, out,
    refused, cmd}.  `green` is the set of legs the counter reported as PASS.
    """
    cmd = [sys.executable, "-B", counter, "--root", repo, "--lands", rev,
           "--freeze", freeze, "--fleet-root", fleet_root] + list(extra)
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
    return {"exit": r.returncode, "verdict": m.group(2),
            "legs": int(m.group(3)), "total": int(m.group(4)),
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

def _seed_frozen_config(repo):
    """Put reports/round-75/{claims,ledger}.json into the fixture tree when
    the reference tree does not carry them.

    The convention is that the freeze commit carries both, and every fixture
    then mutates real frozen bytes.  Before the L1 has committed the freeze
    the files exist only in the lane's working tree; seeding them there keeps
    the fixtures materializable against a candidate freeze, and the fixture's
    detail line says so, so a receipt never claims to have graded committed
    bytes it did not.
    """
    seeded = []
    for rel in (R75_CLAIMS, R75_LEDGER):
        if os.path.isfile(os.path.join(repo, rel)):
            continue
        src = os.path.join(LANE, rel)
        if not os.path.isfile(src):
            continue
        with open(src, encoding="utf-8") as fh:
            write(repo, rel, fh.read())
        seeded.append(rel)
    return seeded


def _load_ctx(repo, freeze, lands, base):
    """The frozen claims/ledger — the same bytes the counter reads.

    The freeze commit carries reports/round-75/claims.json and ledger.json;
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
    claims = _doc(R75_CLAIMS)
    ledger = _doc(R75_LEDGER)
    return {"repo": repo, "freeze": freeze, "lands": lands, "base": base,
            "claims": claims, "ledger": ledger, "detail": ""}


def build(name, freeze, lands=None, base=None, workroot=None, baseline=False):
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
        reference = lands or freeze
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
        seeded = _seed_frozen_config(repo)
        if not baseline:
            ctx = _load_ctx(repo, freeze, reference, base)
            junk(repo, ctx)
            detail = ctx["detail"]
            cell = ctx.get("cell")
            own_freeze = bool(ctx.get("own_freeze"))
            if seeded:
                detail += (" [the reference tree carried no %s, so the lane's "
                           "working-tree copy was seeded into the fixture]"
                           % ", ".join(seeded))
        else:
            detail = "baseline: the reference tree, no mutation"
        if own_freeze:
            # The mutation belongs to the FREEZE the counter pins, so the
            # fixture's own commit is the freeze: the counter reads its
            # ledger from it and the LANDING is that same commit.
            rev = commit_all(repo, "junk fixture %s (%s): the freeze itself "
                                  "carries the defect" % (name, claim))
            changed = tuple(git(repo, "diff", "--name-only", reference,
                                rev).split())
            freeze = rev
            reference = rev
        else:
            rev = commit_all(repo, "junk fixture %s (%s) atop %s"
                             % (name, claim, reference[:12]))
            changed = tuple(git(repo, "diff", "--name-only", reference,
                                rev).split())
        if not baseline and not changed:
            raise FixtureError("%s committed no byte change" % name)
        legs = (FIXTURES[name][2] if name in FIXTURES else ("APPENDONLY",))
        return Fixture(name, claim, repo, rev, desc, legs, changed, detail,
                       freeze, reference, base, cell)
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
        fh.write("# r1exempt-%s.txt — round-75 R1EXEMPT fixture %s\n"
                 % (expected.lower(), name))
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
        out_dir=None, keep=False, baseline=True, out=sys.stdout):
    """Build and grade every fixture; return the names the counter ACCEPTED."""
    own_root = None
    if workroot is None:
        own_root = tempfile.mkdtemp(prefix="junk-r75-")
        workroot = own_root
    try:
        return _run_fixtures(freeze, lands, base, only, workroot, out_dir,
                             keep, baseline, out)
    finally:
        if own_root and not keep:
            shutil.rmtree(own_root, ignore_errors=True)


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
                       reference, base, None)
    except Exception:
        shutil.rmtree(d, ignore_errors=True)
        raise


def _run_fixtures(freeze, lands, base, only, workroot, out_dir, keep, baseline,
                  out):
    lands = lands or freeze
    names = [n for n in ORDER + tuple(R1_PAIR) if not only or n in only]
    print(file=out)
    print("# ==================== round-75 junk landings ====================",
          file=out)
    print("# freeze: %s" % freeze, file=out)
    print("# base: %s" % (base or "(not given)"), file=out)
    print("# reference lands: %s" % lands, file=out)
    print("# lane: %s" % LANE, file=out)
    print("# fleet-root: %s" % FLEET_ROOT, file=out)
    print("# counters: %s ; %s" % (C_COUNTER_CANDIDATES[0],
                                  CA_COUNTER_CANDIDATES[0]), file=out)
    print(file=out)

    accepted = []
    # Two reference trees: the landing tree carries the J* fixtures, the
    # freeze tree carries the R1EXEMPT pair.
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

    def _grade_baseline(label, claim):
        fx = baselines.get(label)
        if fx is None:
            return None
        key = (label, claim)
        if key in baseline_res:
            return baseline_res[key]
        try:
            counter = _counter_path(fx.repo,
                                    C_COUNTER_CANDIDATES if claim == "C"
                                    else CA_COUNTER_CANDIDATES)
            # The counter is pinned to the FIXTURE's freeze: for the
            # own-freeze fixtures (J4f) that is the fixture's own commit, so
            # the counter reads the defective ledger.
            res = run_counter(fx.repo, counter, fx.rev, fx.freeze, claim=claim)
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
                fx = build(name, freeze, lands, base, workroot)
                counter = _counter_path(fx.repo,
                                        C_COUNTER_CANDIDATES if claim == "C"
                                        else CA_COUNTER_CANDIDATES)
                res = run_counter(fx.repo, counter, fx.rev, freeze,
                                  claim=claim)
            except (FixtureError, OSError, subprocess.SubprocessError) as exc:
                print("fixture: %s" % name, file=out)
                print("error: %s: %s" % (type(exc).__name__, exc), file=out)
                print("accepted: no (no verdict was produced)", file=out)
                print(file=out)
                continue
            brec = _grade_baseline(label, claim) if baseline else None
            if res["verdict"] == "PASS":
                accepted.append("%s(%s)" % (name, section))
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
            print("expected-legs: %s" % ", ".join(fx.expected_legs), file=out)
            print("accepted: %s" % ("YES" if res["verdict"] == "PASS" else
                                    "no"), file=out)
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
    if accepted:
        print("# ACCEPTED JUNK LANDINGS: %s" % " ".join(accepted), file=out)
    else:
        print("# ACCEPTED JUNK LANDINGS: none", file=out)
    return accepted


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
    text = ("## Corrections — round 75\n\n"
            "| id | old | new | cmd |\n|---|---|---|---|\n"
            "| L75-01 | 412 | 808 | git grep -c x |\n")
    stubbed = stub_correction_row(text, "L75-01")
    check("stub row", "| L75-01 |" in stubbed and "808" not in stubbed,
          repr(stubbed))
    appended = append_correction_row(text, 75, "| L75-02 | a | b | c | S885 |")
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

    for name in failures:
        print("FAIL %s" % name)
    if failures:
        print("SELFTEST: FAIL (%d)" % len(failures))
        return 1
    print("SELFTEST: PASS")
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(
        description="junk-landing fixture generator (round-75)")
    ap.add_argument("--run", action="store_true",
                    help="build and grade every fixture")
    ap.add_argument("--freeze", default=None, help="frozen-contract commit")
    ap.add_argument("--base", default=None,
                    help="the lane base revision the counter diffs against "
                         "(recorded in the r1exempt receipts)")
    ap.add_argument("--lands", default=None,
                    help="reference tree the mutation is applied to "
                         "(default: the freeze commit)")
    ap.add_argument("--only", default=None,
                    help="comma-separated fixture names (default: all)")
    ap.add_argument("--out-dir", default=None,
                    help="directory for the r1exempt receipts")
    ap.add_argument("--out", default=None, help="run table output file")
    ap.add_argument("--workroot", default=None,
                    help="parent dir for the mktemp fixture dirs")
    ap.add_argument("--keep", action="store_true",
                    help="keep the materialized repositories")
    ap.add_argument("--no-baseline", action="store_true",
                    help="skip the unmutated reference run")
    ap.add_argument("--selftest", action="store_true",
                    help="run the helper self-test (no counter needed)")
    ap.add_argument("--list", action="store_true", help="list the fixtures")
    args = ap.parse_args(argv)

    if args.list:
        for name in ORDER:
            claim, _junk, expected, desc = FIXTURES[name]
            print("%-4s %-3s %-28s %s" % (name, claim, ",".join(expected), desc))
        for name in ("G", "R"):
            claim, _junk, desc = R1_PAIR[name]
            print("%-4s %-3s %-28s %s" % (name, claim, "APPENDONLY", desc))
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
    base = args.base.strip().lower() if args.base else None
    if base and not re.fullmatch(r"[0-9a-f]{40}", base):
        print("ERROR: --base must be 40-hex", file=sys.stderr)
        return 2
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
        accepted = run(freeze, lands, base, only=only,
                       workroot=args.workroot, out_dir=args.out_dir,
                       keep=args.keep, baseline=not args.no_baseline, out=fh)
    finally:
        if fh is not sys.stdout:
            fh.close()
    if args.out:
        print("wrote %s" % args.out)
    return 2 if accepted else 0


if __name__ == "__main__":
    sys.exit(main())
