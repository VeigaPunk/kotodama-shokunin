#!/usr/bin/env python3
r"""Junk-landing fixture generator for the kotodama round-73 acceptance counters.

Purpose: make the round-73 closure's *survivor* claims reproducible.  Each
fixture materializes, in a fresh mktemp directory, a git repository whose
`main` tip is a junk LANDING for one of the two round-73 counters:

  claim C  -> reports/round-73/accept-c.py   (acceptance surface: entries +
              registry rows + Gate/evidence + config + census/mirror)
  claim Ca -> reports/round-73/accept-ca.py  (calibration surface: ledger +
              SCORECARD correction rows + append-only/in-place bytes + the
              Ca-byte separation scan)

A fixture is the *real* landed round-73 tree (tree 9b10fa06…) replayed as two
commits on top of the frozen base (8841ad3b…):

  A  the landing artefacts, with the registry kept at its base bytes
  B  the registry append, restoring the landed tree

This two-commit shape is required by the counters themselves, not by taste:
claim C's SCRATCHMIRROR leg reads `git log -S <row> -- corpus/SOURCES.md` and
`--diff-filter=A -- <receipt>` and requires the receipt to be introduced in a
commit strictly before the registry append.  A one-commit fixture would fail
that leg for the wrong reason and every other leg would be untested junk.

The junk is then applied as one additional commit C on top of B, so that every
leg not named by the fixture is exercised against real landed bytes and the
only difference from a legitimate landing is the named defect.  `build()`
returns a Fixture(repo, rev, expected, ...) where `rev` is C; grade it with:

  python3 -B <repo>/reports/round-73/accept-c.py --root <repo> --lands <rev> \
      --fleet-root /home/vgpnk/Projects/shokunin
  python3 -B <repo>/reports/round-73/accept-ca.py --root <repo> --lands <rev> \
      --fleet-root /home/vgpnk/Projects/shokunin

`--run-r73` builds each fixture, runs the round-73 counter of its claim
against it and prints one table row per fixture: PASS means the round-73
counter ACCEPTED the junk landing (a red-before survivor), FAIL means it
caught it.  A baseline (P0) replays the landing with no junk and must be
green on both counters before any fixture verdict is trusted; the claim-C
do-nothing control (P0b, --lands == base) must fail.

FIXTURES (expected verdict of a correct counter is FAIL in every case)

  J1  C   two header-only stub entries + four rows whose used-by names the
          stub paths (row_set narrowed to the four materialized rows)
  J2  C   every Gate admit row's quoted span replaced by one phrase that no
          evidence window carries (URL<->quote mispairing class)
  J3  C   claims.json edited INSIDE the graded tree to a two-row, one-entry
          set, with the registry shrunk to match (the counter must read its
          contract from the frozen commit, never the graded tree)
  J4  Ca  every ledger observe_cmd constant-prints expected_after (literal
          `python3 -c print("…")` on even pairs, `echo` on odd pairs)
  J4b Ca  companion: the evasive constant printer round 73 accepted
          (`python3 -c "import os;print(str(\"…\"))"` -- reads no clone byte)
  J5  Ca  one correction row gutted to `| L01 |` (stub-row class: an id and
          nothing else; the row's evidence is borrowed from a sibling row)
  J6  Ca  in-place edit of a frozen receipt outside both protected sets
          (reports/round-72/telemetry/measures-ca.txt ACCEPT-CA-72 FAIL->PASS)
  J7  Ca  a Ca-byte (round-73 corrections note) cites claim-C row ids
          incidentally: S876..S880 in a row that names no ledger pair, so the
          frozen SEPARABLE scan set never reads it

LIBRARY API (stdlib only; import from a round-74 counter's selftest)

  Fixture(name, claim, repo, rev, expected, paths)
  build(name, workroot=None)          -> Fixture   (J1..J7, J4b)
  J1() … J7(), J4b()                  -> Fixture   (one callable per fixture)
  cleanup(fixture)                    -> None      (rm -rf the fixture dir)
  run_counter(repo, counter_rel, rev, fleet_root=FLEET_ROOT) -> dict

  The file name carries a hyphen, so import it by path (never by module name):

    import importlib.util, os
    HERE = os.path.dirname(os.path.abspath(__file__))
    spec = importlib.util.spec_from_file_location(
        "junk_fixtures", os.path.join(HERE, "junk-fixtures.py"))
    jf = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(jf)
    fx = jf.build("J3")
    try:
        ...                              # grade fx.repo at fx.rev
    finally:
        jf.cleanup(fx)

  A round-74 landing has its own base/lands/config, so its selftest should
  reuse the primitives rather than the fixed J1..J7 trees: clone_lane() +
  landing_replay(repo, round74_base, round74_lands, "corpus/SOURCES.md"),
  then the junk transform for the control being exercised (e.g.
  shrink_claims(), rewrite_ledger_observe(), stub_correction_row(), or
  replace_text() on the round-74 frozen receipt) and commit_all().

  Reusable primitives (all pure text transforms unless stated):
    clone_lane(workroot, label)       -> (dir, repo)  lane clone, toplevel checked
    landing_replay(repo, base, lands, defer_path)     -> (rev, prior_rev)
        replays base..lands as two commits; the second restores `lands` with
        `defer_path` reverted to its base bytes (the append commit)
    commit_all(repo, msg)             -> rev
    drop_rows(text, ids)              -> registry text without those rows
    row_ids(text)                     -> {id: line}
    rewrite_cell(line, index, value)  -> table line with one 1-based pipe cell
    truncate_to_header(text)          -> text up to (not including) first `## `
    replace_gate_quotes(text, phrase) -> lesson text with Gate admit quotes swapped
    shrink_claims(doc, ids=None, entries=None) -> claims doc with claim-C set narrowed
    rewrite_ledger_observe(doc, mode) -> ledger doc; mode "literal" | "evasive"
    stub_correction_row(text, pid)    -> SCORECARD text with `| pid |` only row
    insert_note(text, heading_re, line)-> text with a line at the end of a section
    replace_text(text, old, new)      -> text (exactly-one-occurrence checked)

Read-only outside the mktemp fixture repositories; stdlib only; no network.
"""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from collections import namedtuple

# ---------------------------------------------------------------- constants ---

LANE = "/home/vgpnk/Projects/shokunin/kotodama-shokunin"
FLEET_ROOT = "/home/vgpnk/Projects/shokunin"

R73_BASE = "8841ad3b896a0227674fa0725b818c999118046f"
R73_LANDS = "0316b8883b4f8d44b8efd720140e7f52f734a102"
R73_LANDED_TREE = "9b10fa06a2d3756c8bacfc8fc7b2115921370d97"  # replay check

C_COUNTER = "reports/round-73/accept-c.py"
CA_COUNTER = "reports/round-73/accept-ca.py"
REGISTRY = "corpus/SOURCES.md"
CLAIMS = "reports/round-73/claims.json"
LEDGER = "reports/round-73/ledger.json"
SCORECARD = "SCORECARD.md"
LESSON = "corpus/lessons/round-73.md"
EVIDENCE_DIR = "reports/round-73/evidence"
R72_RECEIPT = "reports/round-72/telemetry/measures-ca.txt"

ENTRY_ONE = "corpus/knowledge/linguistics/conlang-scholarship.md"
ENTRY_TWO = ("corpus/knowledge/linguistics/"
             "conlang-scholarship.amend-2026-10-23.md")
ENTRIES = (ENTRY_ONE, ENTRY_TWO)
CORR_73_RE = re.compile(r"^##\s+Corrections\s*[—–-]\s*round\s+73\b", re.I)

ROW_RE = re.compile(r"^\s{0,3}\|\s*(S\d{3,})\s*\|")
H2_RE = re.compile(r"^##\s")
GATE_RE = re.compile(r"^##\s+Gate\b")
QUOTE_RE = re.compile(r'"(?:\\.|[^"\\\n])*"|“[^“”\n]*”|«[^«»\n]*»|「[^「」\n]*」')
ACCEPT_RE = re.compile(r"^ACCEPT-(C|CA)-73: (PASS|FAIL) legs=(\d+)/(\d+)$", re.M)
LEGFAIL_RE = re.compile(r"^LEG FAIL (\w+)", re.M)

JUNK_QUOTE = ("junk fixtures assert this sentence and no captured context "
              "window carries it")
JUNK_NOTE = ("- Round-73 close note: the conlang rows S876..S880 are claim "
             "C's registry rows; no calibration pair reads them.")

COMMIT_ID = ("junk-fixtures", "junk@fixture.invalid")
CLONE_TIMEOUT = 300
COUNTER_TIMEOUT = 600


class FixtureError(Exception):
    """A fixture could not be materialized."""


Fixture = namedtuple("Fixture", "name claim repo rev expected paths")


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


def commit_all(repo, msg):
    """Stage everything in `repo` and commit with the throwaway fixture identity."""
    git(repo, "add", "-A")
    r = _run(["git", "-C", repo,
              "-c", "user.name=%s" % COMMIT_ID[0],
              "-c", "user.email=%s" % COMMIT_ID[1],
              "commit", "-q", "-m", msg])
    if r.returncode != 0:
        raise FixtureError("fixture commit %r failed in %s (nothing changed?): %s"
                           % (msg, repo, r.stderr.strip()))
    return git(repo, "rev-parse", "HEAD").strip()


def clone_lane(workroot, label):
    """A private clone of the lane repo under a fresh mktemp dir.

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
    r = _run(["git", "clone", "-q", "--no-checkout", LANE, repo])
    if r.returncode != 0:
        raise FixtureError("clone of lane failed: %s" % r.stderr.strip())
    top = git(repo, "rev-parse", "--show-toplevel").strip()
    if os.path.realpath(top) != os.path.realpath(repo):
        raise FixtureError("clone toplevel %r != %r (refusing to commit)"
                           % (top, repo))
    return d, repo


def landing_replay(repo, base, lands, defer_path=REGISTRY):
    """Replay `lands` on top of `base` in two commits.

    Commit A carries the landed artefacts with `defer_path` at its base bytes;
    commit B restores the full landed tree.  Returns (landing_rev, prior_rev)
    and leaves `main` at the landing.  This ordering is what claim C's
    SCRATCHMIRROR leg measures.
    """
    git(repo, "checkout", "-q", "--detach", base)
    git(repo, "read-tree", "-u", "--reset", lands)
    if defer_path:
        git(repo, "checkout", base, "--", defer_path)
    prior = commit_all(repo, "fixture replay A: landed artefacts (pre-data)")
    git(repo, "read-tree", "-u", "--reset", lands)
    landing = commit_all(repo, "fixture replay B: deferred append")
    git(repo, "checkout", "-q", "-B", "main")
    return landing, prior


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


def replace_text(text, old, new, path="<text>"):
    n = text.count(old)
    if n != 1:
        raise FixtureError("%s: expected exactly one %r, found %d"
                           % (path, old, n))
    return text.replace(old, new)


def row_ids(text):
    """{S-id: line} for registry rows (the counter's ROW_RE)."""
    out = {}
    for line in text.splitlines():
        m = ROW_RE.match(line)
        if m:
            out[m.group(1)] = line
    return out


def drop_rows(text, ids):
    """Registry text without the rows whose ids are in `ids`."""
    drop = set(ids)
    kept = []
    for line in text.splitlines(keepends=True):
        m = ROW_RE.match(line)
        if m and m.group(1) in drop:
            continue
        kept.append(line)
    return "".join(kept)


def rewrite_cell(line, index, value):
    """Rewrite one pipe-delimited cell; `index` counts cells like
    `[c.strip() for c in line.split('|')]` (0 is the empty left margin)."""
    parts = line.split("|")
    if index >= len(parts) - 1:
        raise FixtureError("row has %d cells, no index %d: %r"
                           % (len(parts) - 2, index, line[:90]))
    parts[index] = " %s " % value
    return "|".join(parts)


def truncate_to_header(text):
    """The file up to (not including) its first level-2 heading: a header-only
    stub.  The round-73 ENTRIES leg measures the body word count after the
    header block, so this reduces the body to zero words."""
    lines = text.splitlines(keepends=True)
    for i, line in enumerate(lines):
        if H2_RE.match(line):
            return "".join(lines[:i])
    return "".join(lines)


def _gate_section_bounds(text):
    lines = text.splitlines(keepends=True)
    start = None
    for i, line in enumerate(lines):
        if start is None:
            if GATE_RE.match(line):
                start = i + 1
            continue
        if H2_RE.match(line):
            return start, i
    return (start, len(lines)) if start is not None else (None, None)


def replace_gate_quotes(text, phrase):
    """Replace the first quoted span of every Gate ADMIT row (verdict cell
    `admitted`) inside the `## Gate` section with `"<phrase>"`."""
    start, end = _gate_section_bounds(text)
    if start is None:
        raise FixtureError("no ## Gate section in %s" % LESSON)
    lines = text.splitlines(keepends=True)
    touched = 0
    for i in range(start, end):
        raw = lines[i]
        cells = [c.strip() for c in raw.split("|") if c.strip()]
        if not cells or cells[-1].lower() != "admitted":
            continue
        new = QUOTE_RE.sub(lambda m: '"%s"' % phrase, raw, count=1)
        if new != raw:
            lines[i] = new
            touched += 1
    if touched == 0:
        raise FixtureError("no Gate admit row carried a quoted span")
    return "".join(lines)


def shrink_claims(doc, ids=None, entries=None):
    """Narrow claim C's `row_set` (and optionally `entries`) in a claims doc."""
    for claim in doc.get("claims") or []:
        if isinstance(claim, dict) and str(claim.get("id", "")).upper() == "C":
            if ids is not None:
                rows = claim.get("row_set")
                if not isinstance(rows, list):
                    raise FixtureError("claim C carries no row_set list")
                keep = [r for r in rows
                        if isinstance(r, dict) and r.get("id") in set(ids)]
                if len(keep) != len(ids):
                    raise FixtureError("row_set does not carry %s" % sorted(ids))
                claim["row_set"] = keep
            if entries is not None:
                claim["entries"] = list(entries)
            return doc
    raise FixtureError("no claim C object in claims.json")


def rewrite_ledger_observe(doc, mode):
    """Replace every pair's observe_cmd with a constant printer of
    expected_after.  mode "literal" = `print("…")` / `echo`; mode "evasive" =
    `import os;print(str("…"))`, which passes the round-73 argv guard while
    still reading no clone byte."""
    if mode not in ("literal", "evasive"):
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


def insert_note(text, heading_re, line):
    """Insert `line` as the last line of the section whose heading matches."""
    lines = text.splitlines(keepends=True)
    start = None
    for i, raw in enumerate(lines):
        if start is None:
            if heading_re.match(raw):
                start = i
            continue
        if H2_RE.match(raw):
            return "".join(lines[:i] + ["%s\n" % line] + lines[i:])
    if start is None:
        raise FixtureError("section heading not found")
    tail = lines[-1]
    if not tail.endswith("\n"):
        lines[-1] = tail + "\n"
    return "".join(lines + ["%s\n" % line])


# ---------------------------------------------------------------- junk bodies ---

STUB_HEADER = """# {title}

- source: {id1} — {url1}
- source: {id2} — {url2}
- verified-at: 2026-10-25
- recheck: 180d — re-open both rows and re-locate each quoted span
- ground: stub fixture ground line; the entry body was never mined
- gap filled: stub fixture gap line; no prose beyond this header exists
- topic: stub fixture topic line standing in for a mined topic
- sources: the two rows above, both left unmined by this fixture
- couples: `linguistics/conlang-methodology.md`
- scope: a fixture stub; it decides no world's language and adds no canon
"""

STUB_DOCS = {
    ENTRY_ONE: ("Conlang scholarship — stub fixture", "S876",
                "https://ojs.unito.it/index.php/ricognizioni/article/view/7099",
                "S877",
                "http://www.philol.msu.ru/~sidorova/files/conlangs.pdf"),
    ENTRY_TWO: ("Amendment stub fixture", "S878",
                "https://journals.rudn.ru/semiotics-semantics/article/viewFile/"
                "31528/20955",
                "S879",
                "https://cyberleninka.ru/article/n/"
                "klassifikatsii-konlangov-v-sovremennoy-interlingvistike"),
}


def junk_J1(repo):
    """Two header-only stub entries + four rows whose used-by names the stubs."""
    doc = read_json(repo, CLAIMS)
    ids = ["S876", "S877", "S878", "S879"]
    shrink_claims(doc, ids=ids, entries=list(ENTRIES))
    write_json(repo, CLAIMS, doc)
    write(repo, REGISTRY, drop_rows(read(repo, REGISTRY), {"S880"}))
    for rel, (title, id1, url1, id2, url2) in STUB_DOCS.items():
        write(repo, rel, STUB_HEADER.format(title=title, id1=id1, url1=url1,
                                            id2=id2, url2=url2))


def junk_J2(repo):
    """Gate quotes that no evidence window carries."""
    write(repo, LESSON, replace_gate_quotes(read(repo, LESSON), JUNK_QUOTE))


def junk_J3(repo):
    """Config edited inside the graded tree to a two-row, one-entry set."""
    doc = read_json(repo, CLAIMS)
    shrink_claims(doc, ids=["S876", "S877"], entries=[ENTRY_ONE])
    write_json(repo, CLAIMS, doc)
    write(repo, REGISTRY, drop_rows(read(repo, REGISTRY),
                                    {"S878", "S879", "S880"}))


def junk_J4(repo):
    """Literal/echo constant printers in every ledger observe_cmd."""
    write_json(repo, LEDGER, rewrite_ledger_observe(read_json(repo, LEDGER),
                                                    "literal"))


def junk_J4b(repo):
    """The evasive constant printer round 73 accepted."""
    write_json(repo, LEDGER, rewrite_ledger_observe(read_json(repo, LEDGER),
                                                    "evasive"))


def junk_J5(repo):
    """One correction row naming only its id."""
    write(repo, SCORECARD, stub_correction_row(read(repo, SCORECARD), "L01"))


def junk_J6(repo):
    """In-place edit of an unguarded frozen receipt."""
    text = read(repo, R72_RECEIPT)
    write(repo, R72_RECEIPT,
          replace_text(text, "ACCEPT-CA-72: FAIL", "ACCEPT-CA-72: PASS",
                       R72_RECEIPT))


def junk_J7(repo):
    """A Ca note that cites claim-C row ids incidentally."""
    write(repo, SCORECARD, insert_note(read(repo, SCORECARD), CORR_73_RE,
                                       JUNK_NOTE))


FIXTURES = {
    "J1": ("C", junk_J1,
           "FAIL: two header-only stub entries stand in for the mined prose "
           "(body word floor) though their header is complete"),
    "J2": ("C", junk_J2,
           "FAIL: every Gate admit quote is absent from its evidence window "
           "(the quote/URL mispairing class)"),
    "J3": ("C", junk_J3,
           "FAIL: claims.json inside the graded tree shrinks the claim to two "
           "rows and one entry; the contract must come from the frozen commit"),
    "J4": ("Ca", junk_J4,
           "FAIL: every observe_cmd constant-prints expected_after "
           "(literal python3 -c print / echo) instead of reading clone bytes"),
    "J4b": ("Ca", junk_J4b,
            "FAIL: evasive constant printer (import os;print(str(...))) passes "
            "the argv guard but reads no clone byte"),
    "J5": ("Ca", junk_J5,
           "FAIL: a correction row names only its id; ANNOTATE/NOSTUB must "
           "require id + stated token + observed token + re-derivation"),
    "J6": ("Ca", junk_J6,
           "FAIL: a frozen receipt outside both protected sets is edited in "
           "place (ACCEPT-CA-72 FAIL->PASS)"),
    "J7": ("Ca", junk_J7,
           "FAIL: a Ca correction-section note cites claim-C rows S876..S880 "
           "incidentally; SEPARABLE must scan the whole Ca byte set"),
}

ORDER = ("J1", "J2", "J3", "J4", "J4b", "J5", "J6", "J7")


# ---------------------------------------------------------------- build API ---

def _landing(workroot, label):
    d, repo = clone_lane(workroot, label)
    rev, prior = landing_replay(repo, R73_BASE, R73_LANDS, REGISTRY)
    top = git(repo, "rev-parse", "%s^{tree}" % rev).strip()
    if top != R73_LANDED_TREE:
        raise FixtureError("%s replay tree %s != landed tree %s"
                           % (label, top, R73_LANDED_TREE))
    return d, repo, rev, prior


def baseline(workroot=None):
    """P0: the round-73 landing replayed with no junk (must grade PASS)."""
    d, repo, rev, _prior = _landing(workroot, "P0")
    return Fixture("P0", "C+Ca", repo, rev,
                   "PASS: unjunked replay of the round-73 landing", ())


def build(name, workroot=None):
    """Materialize fixture `name`; the caller owns `cleanup(fixture)`."""
    if name not in FIXTURES:
        raise FixtureError("unknown fixture %r (have %s)"
                           % (name, ", ".join(ORDER)))
    claim, junk, expected = FIXTURES[name]
    d, repo, pristine, _prior = _landing(workroot, name)
    junk(repo)
    rev = commit_all(repo, "junk fixture %s: %s" % (name, claim))
    changed = tuple(git(repo, "diff", "--name-only", pristine, rev).split())
    if not changed:
        raise FixtureError("fixture %s committed no byte change" % name)
    return Fixture(name, claim, repo, rev, expected, changed)


def cleanup(fixture):
    """Remove the fixture's mktemp directory (the repo lives inside it)."""
    shutil.rmtree(os.path.dirname(fixture.repo), ignore_errors=True)


# One callable per fixture: each returns a Fixture (repo path + expected verdict).
def J1(workroot=None):
    return build("J1", workroot)


def J2(workroot=None):
    return build("J2", workroot)


def J3(workroot=None):
    return build("J3", workroot)


def J4(workroot=None):
    return build("J4", workroot)


def J4b(workroot=None):
    return build("J4b", workroot)


def J5(workroot=None):
    return build("J5", workroot)


def J6(workroot=None):
    return build("J6", workroot)


def J7(workroot=None):
    return build("J7", workroot)


# ---------------------------------------------------------------- grading ---

def run_counter(repo, counter_rel, rev, fleet_root=FLEET_ROOT):
    """Run one round-73 counter at `rev` and parse its verdict.

    Returns {exit, verdict, legs, total, red, tail, out}.  `counter_rel` is
    resolved inside `repo`, so the graded counter bytes are the landing's own.
    """
    counter = os.path.join(repo, counter_rel)
    if not os.path.isfile(counter):
        raise FixtureError("counter missing at %s" % counter)
    cmd = [sys.executable, "-B", counter, "--root", repo, "--lands", rev,
           "--fleet-root", fleet_root]
    r = _run(cmd, cwd=repo, timeout=COUNTER_TIMEOUT)
    out = r.stdout + ("\n" + r.stderr if r.stderr.strip() else "")
    m = None
    for m in ACCEPT_RE.finditer(r.stdout):
        pass
    if m is None:
        return {"exit": r.returncode, "verdict": "NO-VERDICT", "legs": None,
                "total": None, "red": tuple(LEGFAIL_RE.findall(r.stdout)),
                "tail": (r.stdout.strip().splitlines() or [""])[-1], "out": out,
                "cmd": " ".join(cmd)}
    return {"exit": r.returncode, "verdict": m.group(2),
            "legs": int(m.group(3)), "total": int(m.group(4)),
            "red": tuple(LEGFAIL_RE.findall(r.stdout)),
            "tail": m.group(0), "out": out, "cmd": " ".join(cmd)}


def _signature(res):
    if res["verdict"] == "NO-VERDICT":
        return "NO-VERDICT exit=%d" % res["exit"]
    text = "%s legs=%s/%s exit=%d" % (res["verdict"], res["legs"],
                                      res["total"], res["exit"])
    if res["red"]:
        text += " red=%s" % ",".join(res["red"])
    return text


def run_r73(only=None, workroot=None, keep=False, out=sys.stdout):
    """Build, grade and tabulate the fixtures; return the accepted names."""
    own_root = None
    if workroot is None:
        own_root = tempfile.mkdtemp(prefix="junk-fixtures-")
        workroot = own_root
    try:
        return _run_r73(only, workroot, keep, out)
    finally:
        if own_root and not keep:
            shutil.rmtree(own_root, ignore_errors=True)


def _run_r73(only, workroot, keep, out):
    names = [n for n in ORDER if not only or n in only]
    print("# junk-landing fixtures — round-73 red-before", file=out)
    print("# lane: %s" % LANE, file=out)
    print("# base: %s  landed tree: %s" % (R73_BASE, R73_LANDED_TREE),
          file=out)
    print("# fleet-root: %s" % FLEET_ROOT, file=out)
    print("# counters: %s ; %s" % (C_COUNTER, CA_COUNTER), file=out)
    print(file=out)

    base_fx = baseline(workroot)
    res_c = run_counter(base_fx.repo, C_COUNTER, base_fx.rev)
    res_ca = run_counter(base_fx.repo, CA_COUNTER, base_fx.rev)
    print("P0  baseline landing (no junk)          C: %s | Ca: %s"
          % (_signature(res_c), _signature(res_ca)), file=out)
    if keep:
        print("# P0 repo=%s lands=%s" % (base_fx.repo, base_fx.rev), file=out)
    if not (res_c["verdict"] == "PASS" and res_c["total"] == 11
            and res_ca["verdict"] == "PASS" and res_ca["total"] == 9):
        print("HARNESS ERROR: the unjunked replay is not green on both "
              "counters; fixture verdicts would be meaningless.", file=out)
        if not keep:
            cleanup(base_fx)
        return None
    res_dn = run_counter(base_fx.repo, C_COUNTER, R73_BASE)
    print("P0b do-nothing control (C, --lands=base)   %s"
          % _signature(res_dn), file=out)
    if res_dn["verdict"] != "FAIL":
        print("HARNESS ERROR: the claim-C do-nothing control did not fail.",
              file=out)
        if not keep:
            cleanup(base_fx)
        return None
    print(file=out)

    rows, accepted = [], []
    for name in names:
        fx = build(name, workroot)
        counter = C_COUNTER if fx.claim == "C" else CA_COUNTER
        res = run_counter(fx.repo, counter, fx.rev)
        ok = res["verdict"] == "PASS"
        if ok:
            accepted.append(name)
        rows.append((fx, res, ok))
        if not keep:
            cleanup(fx)
    if not keep:
        cleanup(base_fx)

    head = ("fixture", "claim", "junk paths", "expected (correct counter)",
            "round-73 counter", "accepted?")
    print("| %s |" % " | ".join(head), file=out)
    print("|%s|" % "|".join("---" for _ in head), file=out)
    for fx, res, ok in rows:
        print("| %s | %s | %s | %s | %s | %s |"
              % (fx.name, fx.claim, ", ".join(fx.paths), fx.expected,
                 _signature(res), "YES (survivor)" if ok else "no"), file=out)
    print(file=out)
    if not keep:
        print("# fixture repositories were removed after grading "
              "(re-run with --keep to retain them)", file=out)
    for fx, res, ok in rows:
        print("# %s repo=%s lands=%s" % (fx.name, fx.repo, fx.rev), file=out)
        print("# %s cmd: %s" % (fx.name, res["cmd"]), file=out)
    print(file=out)
    if accepted:
        print("SURVIVORS (round-73 counter accepted the junk landing): %s"
              % " ".join(accepted), file=out)
    else:
        print("SURVIVORS: none", file=out)
    return accepted


# ---------------------------------------------------------------- CLI ---

def main(argv=None):
    ap = argparse.ArgumentParser(
        description="junk-landing fixture generator for the round-73 counters")
    ap.add_argument("--run-r73", action="store_true",
                    help="build every fixture and grade it with its round-73 counter")
    ap.add_argument("--only", default=None,
                    help="comma-separated fixture names (default: all)")
    ap.add_argument("--workroot", default=None,
                    help="parent dir for the mktemp fixture dirs")
    ap.add_argument("--keep", action="store_true",
                    help="keep the materialized repositories (paths printed)")
    ap.add_argument("--list", action="store_true", help="list the fixtures")
    args = ap.parse_args(argv)

    if args.list:
        for name in ORDER:
            claim, _junk, expected = FIXTURES[name]
            print("%-4s %-2s %s" % (name, claim, expected))
        return 0
    if not args.run_r73:
        ap.print_help()
        return 0
    only = None
    if args.only:
        only = {x.strip() for x in args.only.split(",") if x.strip()}
        unknown = only - set(FIXTURES)
        if unknown:
            print("ERROR: unknown fixture(s): %s" % ", ".join(sorted(unknown)),
                  file=sys.stderr)
            return 2
    accepted = run_r73(only=only, workroot=args.workroot, keep=args.keep)
    return 2 if accepted is None else 0


if __name__ == "__main__":
    sys.exit(main())
