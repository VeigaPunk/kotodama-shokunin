#!/usr/bin/env python3
r"""Round-75 coverage acceptance counter — claim C.

Claim C (reports/round-75/claims.json, id "C", axis coverage): the shokuknow
assimilation of the narrative-structure-frameworks theme — eight adopted rows
(S885..S892), two entries under corpus/knowledge/myth-symbol/, the lesson's
`## Gate` record, the per-row evidence captures, the gap-sweep receipt, the
scratch mirror, the collision guard and the by-document renumber map.

Grading model (QUALITY 19).  Nothing in the graded tree is trusted to be the
tree that was graded: the counter clones the lane into a fresh scratch
directory, runs `git -C <clone> checkout --detach <lands>` there, and every
graded byte is read from that checkout.  The claim base is materialized from
the same clone with `git archive <base>`.  Read-only git against the lane
supplies commit metadata (ancestry, per-path history, blobs at a revision)
and never a graded byte.

Receipt header (QUALITY 17/19 grammar of tools/check-receipt-seq.py):

  # counter sha256 (self): ...        the counter's own bytes
  # stamped revision: <lands>         the revision the receipt claims
  # evaluated revision: <lands>       the revision the clone was checked out at
  # measured revision (lane main): <lands>   the revision whose bytes were read
  # tree: <lands>^{tree}              the tree of that revision
  # base revision: <frozen claim base>
  # freeze revision: <freeze>         the commit the constants are read from
  # lane worktree HEAD (disclosure only): ...   never graded

Legs (13): ENTRIES, ROWS, REPOINTED, GATE, EVIDENCE, REJECTS, GROUND,
CITEDLINES, CENSUS, SCRATCHMIRROR, COLLCHECK, FROZENCFG, INDEX.

The frozen claims.json `legs[]` is authoritative for the leg set: the counter
refuses (exit 2) when its own leg table length or ordered names differ from
the frozen list (LEGCOUNT), and every leg's detail is printed before the
`ACCEPT-C-75: ... legs=<n>/<n>` summary line.

Hardenings carried from round 74 (named here, as required):

  H1 FROZENCFG  Every constant the counter uses — row_set (lane id + staged
     ids), reused_rows, entry paths, ground.fragments, ground.terms, the
     rejects lists and counts, the access date, the by-document map path and
     its sha256, the claim base — is read with
     `git show <freeze>:reports/round-75/claims.json` and never from the
     graded tree.  The leg fails when the graded tree's claims.json differs
     from the frozen bytes, when <freeze> is not on <lands>' first-parent
     chain, when the frozen claim base is not a STRICT ancestor of <lands>
     (<lands> == <base> is refused outright), or when
     `git show <freeze>:<map.path>` does not hash to the frozen
     `map.sha256`.  A frozen claims.json that cannot be read at all is a
     refusal (exit 2).  `lands == the frozen base` is also a refusal that
     still prints FAIL (the do-nothing control).
  H2 EVIDENCE   The Gate quote must occur INSIDE the committed evidence
     window text (substring after NFKC + whitespace folding), the stored
     window's scope header is re-derived from the stored bytes
     (`excerpt` => window >= 4096 characters; `whole-document` => the stored
     window is shorter than 4096 characters and its length equals the
     recorded `visible-chars:`), and `window-sha256` / `window-bytes` are
     recomputed from the stored window line.  The self-attested
     `quote-found` / `quote-found-verbatim` lines are never read.
  H3 FROZENCFG  reports/round-75/claims.json at <lands> must be byte-identical
     to the freeze blob: a counter config edited in the graded tree is a junk
     landing and fails the leg (the same bytes are also the source of every
     constant, so a graded-tree edit would otherwise be self-consistent).
  H4 INDEX      The INDEX leg grades ONLY the myth-symbol index rows claim C
     appends and the new live footer.  corpus/README.md heading lines whose
     only change is the partition-count parenthetical (e.g.
     `## linguistics/ (30)` -> `## linguistics/ (32)`) belong to claim Ca's
     pairs L75-02 / L75-03 and are EXEMPT from the README diff scope; any
     other changed or removed README line outside the base's last footer
     block fails the leg, and a row-shaped added line carrying an S-id fails
     it too (the README never asserts registry rows).

Artifact shapes the legs read (all at <lands>; a shape miss is a leg FAIL,
never a skip):

  registry row     `| S885 | source | kind | tier | scope | anchor | teaches |
                   mined | <access date> | <cadence> | used-by |` — exactly 11
                   cells, no `|` inside any cell, anchor carrying the located
                   quote, source carrying the document URL, used-by exactly
                   the citing entry paths;
  Gate admit table a header row carrying a `quote`, an access-date and a
                   locator column; one admit row per adopted row carrying its
                   URL, the access date and a <=25-token / <=80-character
                   quoted span; the re-quoted staged ids (if the frozen
                   claims name any) also state `re-quote` and why the staged
                   quote was replaced;
  Gate reject table a header row carrying `reason` and `flip`; every reject
                   row carrying its probed URL, a non-dash reason and a
                   non-dash flip;
  evidence file    the grammar written by the round-7x capture tool:
                   `url:`/`fetch:`, `user-agent:` (Mozilla/5.0 ...),
                   `http-status: 200`, `bytes:`, 64-hex `sha256:`, `access-date:`,
                   a `--- window ---` line, its `window-sha256:`/`window-bytes:`,
                   a `window-scope:`/`visible-chars:` pair and a `--- quote ---`
                   block; the Gate quote must occur inside the window;
  README index     `corpus/README.md`: one row per adopted entry inside the
                   entry's own partition section, shaped
                   ``- `name.md` — <the entry's own `- topic:` text>``, the
                   last `Counts checked` footer carrying the file total and
                   the six-partition vector, and every older footer preserved
                   byte-identically from base;
  renumber map     `assignments[]` with staged_id/new_target/url and/or a
                   `map` object; the staged ids must be the row_set staged
                   ids and the url must name the row's document;
  guard proof      one file with a 1-3-space-indented planted row (an id that
                   is no real row) and a positive detection marker, and one
                   file with a 4-space planted row and a not-found marker;
  mirror receipt   `.ufo/waves/round-75/assimilation/validate-receipt.txt`
                   showing `validate --file`, exit 0, the adopted ids and
                   both entry basenames, committed before the registry-append
                   commit.

Configuration schema read at <freeze> (the draft claims.json schema; the
counter is deliberately tolerant about how the rejects are spelled, because
the frozen file is the contract and not this file):

  claims[id=C].row_set[]        {"id": "S885", "staged": "S876/S885/S917/S921",
                                 "document": "<url> (<title>)"}
                                 — `staged` may be one id, a "/"-separated
                                 list or a JSON list; `document` is optional
  claims[id=C].reused_rows[]    same shape (empty at the round-75 draft)
  claims[id=C].entries[]        entry paths
  claims[id=C].ground.fragments[] / .terms[] (also accepted: .cjk_terms[])
  claims[id=C].rejects.refused_staged_not_appended[] / .refused_staged[] /
                  .forced_new_quotes[] / .folded_dropped[]  (free text: S-ids
                  are extracted from the prose)
  claims[id=C].rejects.refused_files_pending_triage[] / .refused_files[] /
                  .families[]  (free text family/file specs)
  claims[id=C].rejects.counts   optional {adopted, refused,
                  total_staged_files, path_present}
  claims[id=C].map.path         the by-document renumber map path
  claims[id=C].map.sha256       the sha256 of that map blob at <freeze>
  claims[id=C].legs[]           the frozen leg list (LEGCOUNT)
  claims[id=C].access_date      OPTIONAL; otherwise the access date is
                  derived from the frozen legs/after text; if neither yields
                  one, the frozen configuration is unusable and the counter
                  refuses (exit 2)
  base                          top-level claim base (40-hex)

Usage:
  python3 -B accept-c.py --root <lane> --lands <40hex> --freeze <40hex>
                        [--fleet-root <fleet>] [--selftest]

Exit: 0 all legs pass; 1 any leg fails; 2 input error or refusal (missing
argument, unknown revision, unreadable/unusable claims.json at <freeze>,
`lands` equal to the frozen claim base, or the frozen `legs[]` list not
matching this counter's leg table).  A refusal also prints
`ACCEPT-C-75: FAIL legs=0/13 (refused: ...)` — no leg ran, so the verdict is
a FAIL and never a PASS; the exit code marks it as an input error.

--selftest builds every fixture repo in its own scratch directory (git init +
three commits: base, freeze, lands), runs the counter as a subprocess against
it, and asserts one named leg per mutant.  The scratch root is taken from
$SHOKUNIN_SCRATCH (default: the system temporary directory) so a run never
writes outside the operator's scratch tree.
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
import unicodedata
from collections import Counter
from urllib.parse import urlparse


def _lane_root():
    d = os.path.dirname(os.path.abspath(__file__))
    while True:
        if os.path.isdir(os.path.join(d, ".git")):
            return d
        nd = os.path.dirname(d)
        if nd == d:
            break
        d = nd
    return os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


LANE = _lane_root()
ROUND = 75
CLAIMS = "reports/round-75/claims.json"
REGISTRY = "corpus/SOURCES.md"
LESSON = "corpus/lessons/round-75.md"
EVIDENCE_DIR = "reports/round-75/evidence"
README = "corpus/README.md"
KNOWLEDGE = "corpus/knowledge"
ASSIM = ".ufo/waves/round-75/assimilation"
RECEIPT = ASSIM + "/validate-receipt.txt"
GROUND_RECEIPT = "reports/round-75/telemetry/gap-sweep.txt"
GUARD_DIR = ASSIM + "/guard-proof"
BASE_LESSON = "corpus/lessons/round-74.md"
CLAIM_KEYS = ("row_set", "entries", "ground", "rejects")
HEADER_FIELDS = ("source", "verified-at", "recheck", "ground", "topic",
                 "gap-filled", "sources", "couples", "scope")
# the frozen claim: no header value in this set, and none matching <[^>]+>
PLACEHOLDERS = ("", "todo", "tbd", "fixme", "xxx", "n/a", "?", "—")
MIN_WINDOW_CHARS = 4096
MAX_QUOTE_TOKENS = 25
MAX_QUOTE_CHARS = 80

# registry geometry (SOURCES-CONTRACT-v1: 11 columns, census NF==13)
ID, SOURCE, KIND, TIER, SCOPE, ANCHOR, TEACHES, STATUS, OPENED, RECHECK, USEDBY = range(11)
NCELLS = 11

ROW_RE = re.compile(r"^ {0,3}\|\s*(S\d{3,})\s*\|")
INDENTED_ROW_RE = re.compile(r"^ {1,3}\|\s*(S\d{3,})\s*\|", re.M)
FOURSPACE_ROW_RE = re.compile(r"^ {4,}\|\s*(S\d{3,})\s*\|", re.M)
TOKEN_RE = re.compile(r"\bS\d{3,}\b")
URL_RE = re.compile(r"https?://[^\s|<>()（）「」『』]+")
QUOTE_RE = re.compile(r'"(?:\\.|[^"\\\n])*"|“[^“”\n]*”|«[^«»\n]*»'
                      r'|「[^「」\n]*」|『[^『』\n]*』')
H2_RE = re.compile(r"^##\s")
GATE_RE = re.compile(r"^##\s+Gate\b")
# a cadence-only recheck cell: `180d`, `90d`, `on-release`, `quarterly` —
# never an ISO date, never a composite cell with prose in it
RECHECK_RE = re.compile(r"^(?:\d+d|[a-z][a-z0-9]*(?:[ -][a-z0-9]+)*)$")
NOT_ADOPTED_RE = re.compile(r"(?i)\bnot\s+adopted\b|\bno\s+adoption\b|\bnot\s+admitted\b"
                            r"|\bnot\s+appended\b")
REQUOTE_RE = re.compile(r"(?i)re-?\s?quote")
REFUSAL_RE = re.compile(r"(?i)\brefus|\breject|\bnot\s+adopted\b|\bnot\s+appended\b"
                        r"|\bstays?\s+refused\b|\bremain(s)?\s+refused\b")
MISPAIR_RE = re.compile(r"(?i)\babsent\b|\brefus|\bmis-?\s?pair")
DASHES = ("—", "-", "–", "n/a", "na", "")
ANGLE_RE = re.compile(r"<[^>]+>")
README_SECTION_RE = re.compile(r"^## ([a-z-]+)/ \((\d+)\)\s*$", re.M)
README_ROW_RE = re.compile(r"^- `([^`]+\.md)` — (.*)$")
README_FOOTER_RE = re.compile(r"\(total (\d+) files; directory totals ([\d/]+)\)")
README_HEADING_RE = re.compile(r"^## ([a-z-]+)/ \((\d+)\)\s*$")
ROW_SHAPED_LINE_RE = re.compile(r"^\s*\|\s*S\d{3,}\s*\|")


class Missing(Exception):
    """A materialized path cannot be read at the requested revision."""


class ConfigError(Exception):
    """The frozen configuration is unusable: the counter refuses to grade."""


# ---------------------------------------------------------------- helpers ---

def norm_label(s):
    return re.sub(r"[^A-Za-z0-9]", "", s).lower()


def norm_url(u):
    u = u.rstrip(".,;:!?)]}。，；：！？）】》»\"'")
    p = urlparse(u)
    path = p.path.rstrip("/") or "/"
    return (p.netloc.lower(), path)


def nfkc_ws(s):
    """NFKC, then every whitespace run folded to one space, ends stripped."""
    s = unicodedata.normalize("NFKC", s)
    return re.sub(r"\s+", " ", s).strip()


def git(root, *args):
    return subprocess.run(["git", "-C", root, *args],
                          capture_output=True, text=True)


def git_bytes(root, *args):
    return subprocess.run(["git", "-C", root, *args], capture_output=True)


def sha256_text(text):
    return hashlib.sha256(text.encode("utf-8", "surrogateescape")).hexdigest()


def counter_sha256():
    with open(os.path.abspath(__file__), "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def read_tree(tree, path):
    full = os.path.join(tree, path)
    try:
        with open(full, encoding="utf-8") as fh:
            return fh.read()
    except OSError:
        raise Missing(path)


def tree_files(tree, prefix):
    base = os.path.join(tree, prefix)
    out = []
    for dirpath, _dirnames, filenames in os.walk(base):
        for fn in filenames:
            out.append(os.path.relpath(os.path.join(dirpath, fn), tree))
    return sorted(out)


def is_ancestor(root, older, newer):
    """Strict ancestry: older must be a proper ancestor of newer."""
    if older == newer:
        return False
    return git(root, "merge-base", "--is-ancestor", older, newer).returncode == 0


def clone_at(root, lands, dest):
    """Materialize <lands> as a real checkout inside `dest` (a scratch dir)."""
    r = subprocess.run(["git", "clone", "--quiet", "--no-checkout",
                        os.path.abspath(root), dest],
                       capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError("git clone failed: %s" % r.stderr.strip())
    r = git(dest, "checkout", "--detach", lands)
    if r.returncode != 0:
        raise RuntimeError("checkout --detach %s failed: %s"
                           % (lands[:12], r.stderr.strip()))
    head = git(dest, "rev-parse", "HEAD").stdout.strip()
    if head != lands:
        raise RuntimeError("clone HEAD %s != lands %s" % (head[:12], lands[:12]))


def materialize(root, rev, dest):
    """Extract the committed tree of `rev` into `dest` (no git dir, exact bytes)."""
    proc = subprocess.Popen(["git", "-C", root, "archive", "--format=tar", rev],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    tar = subprocess.run(["tar", "-x", "-C", dest], stdin=proc.stdout,
                         capture_output=True, text=True)
    proc.stdout.close()
    err = proc.stderr.read().decode("utf-8", "replace")
    rc = proc.wait()
    if rc != 0 or tar.returncode != 0:
        raise RuntimeError("materialize %s failed (git rc=%d, tar rc=%d): %s"
                           % (rev[:12], rc, tar.returncode, err.strip()))


def parse_rows(text):
    rows = {}
    for line in text.splitlines():
        m = ROW_RE.match(line)
        if m:
            rows[m.group(1)] = line
    return rows


def row_cells(row):
    s = row.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|"):
        s = s[:-1]
    return [c.strip() for c in s.split("|")]


def row_usedby(cells):
    if len(cells) <= USEDBY:
        return set()
    out = set()
    for part in cells[USEDBY].split(","):
        part = part.strip()
        if part and part not in DASHES:
            out.add(part)
    return out


def leg(name, passed, detail=""):
    print("LEG %s %s" % ("PASS" if passed else "FAIL", name))
    if detail:
        print("     %s" % detail)
    return bool(passed)


def dedupe(seq):
    seen, out = set(), []
    for x in seq:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out


def header_block(text):
    out = []
    for line in text.splitlines():
        if H2_RE.match(line):
            break
        out.append(line)
    return out


def header_field_names(text):
    labels = set()
    for line in header_block(text):
        m = re.match(r"^[-*\s]*([A-Za-z][A-Za-z0-9 -]*):\s*", line)
        if m:
            labels.add(norm_label(m.group(1)))
    return labels


def source_lines(text):
    out = []
    for line in header_block(text):
        m = re.match(r"^[-*\s]*source:\s*(.*)$", line)
        if m:
            out.append(m.group(1))
    return out


def urls_in(s):
    return URL_RE.findall(s)


def neutral_url_keys(urls):
    return set(norm_url(u) for u in urls)


def _norm_path(u):
    """(host, path) with %20 folded to a space and the scheme dropped."""
    host, path = norm_url(u)
    return (host, path.replace("%20", " "))


def urls_compatible(a, b):
    """True when two URL strings name the same document.

    Exact (host, path) equality, or one document path contained in the other
    (a web.archive.org wrapper carries the original URL inside its path).
    """
    ka, kb = _norm_path(a), _norm_path(b)
    if ka == kb:
        return True
    pa, pb = ka[1], kb[1]
    if not pa or not pb:
        return False
    return pa.endswith(pb) or pb.endswith(pa) or pa in pb or pb in pa


def gate_section(text):
    return section_block(text, r"^##\s+Gate\b").splitlines()


def section_block(text, heading_re):
    """The body of the first H2 section whose heading matches heading_re."""
    lines = text.splitlines()
    out, started = [], False
    rx = re.compile(heading_re)
    for line in lines:
        if rx.match(line):
            started = True
            continue
        if started and H2_RE.match(line):
            break
        if started:
            out.append(line)
    return "\n".join(out)


def quoted_spans(line):
    return [m.group(0)[1:-1] for m in QUOTE_RE.finditer(line)]


def quote_ok(span):
    """The frozen Gate cap: <= 25 whitespace tokens AND <= 80 characters."""
    words = span.split()
    return bool(words) and len(words) <= MAX_QUOTE_TOKENS and \
        len(span) <= MAX_QUOTE_CHARS


def table_rows(lines):
    rows = []
    open_row = False
    for line in lines:
        if line.lstrip().startswith("|"):
            rows.append(line.strip())
            open_row = True
        elif not line.strip():
            open_row = False  # a blank line ends the table: later indented prose is not a continuation
        elif line.startswith(" ") and rows and open_row:
            rows[-1] += " " + line.strip()
    return rows


def verdict_of(row):
    cells = [c.strip() for c in row_cells(row)]
    nonempty = [c for c in cells if c]
    return nonempty[-1].lower() if nonempty else ""


def is_admit_row(row):
    return "admitted" in verdict_of(row)


def is_reject_row(row):
    v = verdict_of(row)
    return "rejected" in v or "refused" in v


def col_index(cells, names):
    for i, c in enumerate(cells):
        low = c.lower()
        if any(n in low for n in names):
            return i
    return None


def table_header(rows, needles):
    for r in rows:
        cells = row_cells(r)
        low = [c.lower() for c in cells]
        if all(any(n in c for c in low) for n in needles):
            return cells
    return None


# --- PART B ---
