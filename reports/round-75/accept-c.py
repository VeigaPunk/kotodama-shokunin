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

# ------------------------------------------------------------ part-cfg.py ---
# owner: ExecCtrCfgMain.  Function definitions only (no top-level code, no new
# imports); spliced by the L1 immediately after PART A and before the leg
# parts.  Round-74 provenance: `.ufo/waves/round-74/counters/accept-c.py`
# lines 473-745 (`_frozen_claim _paths_from_spec _id_list _row_pairs
# load_frozen_config _row_url_keys _gate_admit_row _min_entry_words _evidence
# _window _entry_citations`), names and signatures kept.
#
# Round-75 deltas carried here, each traceable to a w1 finding:
#
#  D1 multi-id staged rows.  `row_set[i].staged` may be one id, a
#     "/"-separated string or a JSON list; `cfg["row_staged"]` maps a lane id
#     to a LIST of staged ids (S885 <- S876/S885/S917/S921).  One registry row
#     per DOCUMENT, not per staged occurrence (SimplifierRows §4, ExecRenumber
#     §2/§3).  `_row_pairs` also rejects a staged id claimed by two lane rows:
#     a by-document map with an ambiguous staged side is not a map.
#  D2 by-document map.  cfg carries `map_path`/`map_sha256` (read from the
#     freeze blob; a null/absent sha256 makes the frozen config unusable) and
#     `row_doc` (the claim's `document` string per lane id).  Nothing here does
#     id arithmetic; identity is the document URL (ExecRenumber §1).
#  D3 page-level Persée URLs, and the two carrier/view folds.  A per-page
#     transcription `/doc/page/<slug>/<page>` is a VIEW of `/doc/<slug>`; a
#     `web.archive.org/web/<ts>/…` wrapper is a CARRIER of the embedded
#     original; `%20` and a raw space name the same document (S892).  These are
#     folded by `_doc_url_key`, and `_row_url_keys`/`_gate_admit_row` compare
#     with `_url_keys` (raw key UNION folded key) so a page-level citation and
#     a document-level source cell still join.  Legs that compare a cited or
#     fetched URL against a row MUST use `_url_keys(urls_in(...))` against
#     `_row_url_keys(...)` (raw-key-only intersection misses a page view).
#  D4 evidence window scope.  `window-scope: excerpt` needs >= 4096 characters,
#     `whole-document` needs a window shorter than 4096 whose length equals
#     `visible-chars:`; `_evidence`/`_window` only parse — the scope rule is
#     graded by the EVIDENCE leg (leg-evidence.py, `_evidence_core`).
#  D5 `terms` (the r74 `cjk_terms` slot, renamed by the round-75 claim text;
#     `ground.cjk_terms` is still accepted as the source key).
#  D6 `owned_inplace`.  The claim's in-place README heading edit
#     (`## myth-symbol/ (29)` -> `## myth-symbol/ (32)`) is carried so the
#     INDEX leg can exempt exactly those heading lines from the README diff
#     scope (H4) instead of failing on Ca's partition-count lines.
#  D7 `refused_staged` holds STAGED ids only (extracted ids - lane ids), so
#     S885 (staged AND a lane id) and S893 (the lane id the refusal prose also
#     names) are never reported as a refused staged row.  The raw prose is kept
#     in `refused_staged_text` for the REJECTS leg.  r75 freezes no
#     `forced_new_quotes` list: a re-quoted row is derived as
#     `row_staged[sid] & set(refused_staged)`.
#
# Ambiguities in the frozen text and their readings (also in the seat report):
#  A1 GATE "per adopted row URL + access date 2026-10-27" — the access date is
#     not a literal key of claims.json at the round-75 draft, so it is derived
#     from the frozen `after`/`legs` text (most frequent YYYY-MM-DD) and the
#     configuration refuses when no candidate exists (PART A docstring).
#  A2 REPOINTED "no campaign-namespace id is cited as a lane row except the
#     staged->lane substitutions in the frozen map" — read as: the forbidden set
#     is (staged ids NOT adopted as lane ids), so S885 is never forbidden
#     (CritCCounterVacuity repair 4, SimplifierRows §8(c)).
#  A3 INDEX "the myth-symbol heading equals the live partition count (32)" —
#     that line belongs to claim Ca's pairs L75-02/L75-03; this part only
#     exposes `owned_inplace` so the INDEX leg can exempt it (H4).


def _frozen_claim(doc):
    """The claim object with id C (case-insensitive) inside a claims document."""
    for c in doc.get("claims") or []:
        if isinstance(c, dict) and str(c.get("id", "")).upper() == "C":
            return c
    return None


def _cfg_pct_decode(s):
    """Percent-decode `%XX` runs without importing urllib (PART A imports are
    fixed; `%20` is the only form that occurs, the general form is free)."""
    def take(m):
        try:
            return chr(int(m.group(1), 16))
        except ValueError:
            return m.group(0)
    return re.sub(r"%([0-9A-Fa-f]{2})", take, s)


def _doc_url_key(u):
    """The DOCUMENT a URL names: (host without `www.`, document path).

    Folds the two carriers/views claim C's row set depends on:
      * `web.archive.org/web/<ts><mod>/<original>` -> key of <original>
        (a capture is a carrier of the document, not a second document);
      * `persee.fr/doc/page/<slug>/<page>` and `/docAsPDF/<slug>.pdf` ->
        `/doc/<slug>` (a per-page transcription is a view of the document).
    `%20` and a raw space are the same character after decoding, so the S892
    claim string and its row cell name one document.  Never numeric, never
    arithmetic.
    """
    u = (u or "").strip()
    host, path = norm_url(u)
    if host.startswith("www."):
        host = host[4:]
    path = _cfg_pct_decode(path)
    if host == "web.archive.org":
        m = re.match(r"^/web/\d{8,14}[a-z_]*/(.+)$", path)
        if m:
            return _doc_url_key(m.group(1))
    m = re.match(r"^/doc/page/([^/]+)/", path)
    if m:
        path = "/doc/" + m.group(1)
    else:
        m = re.match(r"^/docAsPDF/([^/]+?)(?:\.pdf)?$", path)
        if m:
            path = "/doc/" + m.group(1)
    return (host, path)


def _url_keys(urls):
    """Both keys of every URL: the raw norm_url key and its document key.

    A set, so a comparison is order-insensitive; the union lets a page-level
    citation (raw page key) meet a source cell that carries the page URL, and
    lets a document-level citation meet a row that carries a page URL.
    """
    out = set()
    for u in urls:
        try:
            out.add(norm_url(u))
        except ValueError:
            continue
        out.add(_doc_url_key(u))
    return out


def _paths_from_spec(spec):
    """Repo-relative paths from a claim `entries`-like value (string, list or
    object with a named path key), `./` stripped, order preserved."""
    out = []

    def take(value):
        if isinstance(value, str):
            v = value.strip()
            if v:
                out.append(v[2:] if v.startswith("./") else v)
        elif isinstance(value, list):
            for item in value:
                take(item)
        elif isinstance(value, dict):
            for key in ("path", "paths", "entries", "amendments", "canonical",
                        "admitted"):
                if key in value:
                    take(value[key])

    if isinstance(spec, dict):
        for key in ("paths", "entries", "amendments", "canonical", "admitted"):
            if key in spec:
                take(spec[key])
    else:
        take(spec)
    return list(dict.fromkeys(out))


def _id_list(value, what):
    """A list of S-ids from a list/string claim value (order preserved)."""
    if isinstance(value, str):
        value = [value]
    out = []
    if not isinstance(value, list):
        raise ConfigError("%s is not a list" % what)
    for item in value:
        v = str(item).strip().upper()
        if not TOKEN_RE.fullmatch(v):
            raise ConfigError("%s carries a non-S-id item: %r" % (what, item))
        out.append(v)
    return list(dict.fromkeys(out))


def _staged_ids(value, what):
    """D1: the staged side of one row_set item, always a LIST.

    Accepts one id (`"S902"`), a "/"-separated string (`"S876/S885/S917/S921"`)
    or a JSON list (of either form).  Order is the claim's, duplicates dropped.
    """
    if isinstance(value, str):
        parts = re.split(r"[/,;\s]+", value.strip())
    elif isinstance(value, list):
        parts = []
        for item in value:
            if isinstance(item, str):
                parts.extend(re.split(r"[/,;\s]+", item.strip()))
            else:
                raise ConfigError("%s carries a non-string staged item: %r"
                                  % (what, item))
    else:
        raise ConfigError("%s carries no staged ids: %r" % (what, value))
    out = []
    for part in parts:
        v = part.strip().upper()
        if not v:
            continue
        if not TOKEN_RE.fullmatch(v):
            raise ConfigError("%s carries a non-S-id staged item: %r"
                              % (what, part))
        if v not in out:
            out.append(v)
    if not out:
        raise ConfigError("%s carries no staged ids" % what)
    return out


def _row_pairs(spec, what):
    """[(lane id, [staged ids])] from a row_set/reused_rows list (D1).

    A lane id is the row the registry will hold; the staged ids are the
    campaign ids it absorbs by document.  A staged id claimed by two lane rows
    is an ambiguous by-document map and is refused here, not graded later.
    """
    if not isinstance(spec, list):
        raise ConfigError("%s is not a list" % what)
    pairs, seen, owners = [], set(), {}
    for item in spec:
        if not isinstance(item, dict):
            raise ConfigError("%s carries a non-object item: %r" % (what, item))
        rid = str(item.get("id", "")).strip().upper()
        if not TOKEN_RE.fullmatch(rid):
            raise ConfigError("%s item needs an S-id lane id: %r" % (what, item))
        staged = _staged_ids(item.get("staged", ""), what)
        if rid in seen:
            raise ConfigError("%s repeats lane id %s" % (what, rid))
        seen.add(rid)
        for sid in staged:
            other = owners.get(sid)
            if other is not None and other != rid:
                raise ConfigError("%s maps staged %s to both %s and %s"
                                  % (what, sid, other, rid))
            owners[sid] = rid
        pairs.append((rid, staged))
    return pairs


def _cfg_refusal_text(rejects):
    """D7: the raw refused-staged strings, from whichever key carries them.

    The frozen file is the contract, so the accepted spellings are the PART A
    docstring's set: prose (`refused_staged_not_appended`, `refused_staged`) and
    id lists (`forced_new_quotes`, `folded_dropped`).
    """
    out = []
    for key in ("refused_staged_not_appended", "refused_staged",
                "forced_new_quotes", "folded_dropped"):
        value = rejects.get(key)
        if value is None:
            continue
        items = value if isinstance(value, list) else [value]
        for item in items:
            text = str(item).strip()
            if text:
                out.append(text)
    return out


def _cfg_access_date(claim, doc):
    """A1: the claim's access date, or the date the frozen text repeats.

    Every date-shaped token of the frozen `after` clause and `legs` list is a
    candidate; the most frequent one wins (ties: the earliest, so the choice is
    deterministic).  No candidate, or an explicit non-YYYY-MM-DD value, makes
    the frozen configuration unusable (PART A docstring).
    """
    explicit = str(claim.get("access_date") or doc.get("access_date") or "").strip()
    if explicit:
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", explicit):
            raise ConfigError("access date at freeze is not YYYY-MM-DD: %r"
                              % explicit)
        return explicit
    text = " ".join([str(claim.get("after") or ""),
                     str(claim.get("before") or ""),
                     " ".join(str(x) for x in (claim.get("legs") or []))])
    dates = re.findall(r"\b(20\d\d-\d\d-\d\d)\b", text)
    if not dates:
        raise ConfigError("the frozen claim carries no access date (no "
                          "access_date key and no YYYY-MM-DD in its after/legs "
                          "text)")
    best = sorted(Counter(dates).items(), key=lambda kv: (-kv[1], kv[0]))[0][0]
    return best


def load_frozen_config(root, freeze):
    """H1: every constant comes from `git show <freeze>:claims.json`.

    Returns exactly the CFG-CONTRACT keys: freeze, frozen_sha256, base,
    access_date, rows, row_staged, row_doc, reused, reused_staged, entries,
    fragments, terms, refused_staged, refused_staged_text, refused_files,
    counts, map_path, map_sha256, frozen_legs, allowed_ids, forbidden_ids,
    owned_inplace, claim_keys.
    """
    r = git_bytes(root, "show", "%s:%s" % (freeze, CLAIMS))
    if r.returncode != 0:
        raise ConfigError("cannot read %s at freeze %s: %s"
                          % (CLAIMS, freeze[:12],
                             r.stderr.decode("utf-8", "replace").strip()))
    raw = r.stdout
    try:
        doc = json.loads(raw.decode("utf-8"))
    except (ValueError, UnicodeDecodeError) as e:
        raise ConfigError("%s at freeze %s is not JSON: %s"
                          % (CLAIMS, freeze[:12], e))
    if not isinstance(doc, dict):
        raise ConfigError("%s at freeze is not a JSON object" % CLAIMS)
    claim = _frozen_claim(doc)
    if claim is None:
        raise ConfigError("%s at freeze carries no claim with id C" % CLAIMS)
    missing = [k for k in CLAIM_KEYS if k not in claim]
    if missing:
        raise ConfigError("claim C at freeze lacks %s" % ", ".join(missing))
    base = str(doc.get("base") or claim.get("base") or "").strip().lower()
    if not re.fullmatch(r"[0-9a-f]{40}", base):
        raise ConfigError("claim base at freeze is not a 40-hex revision: %r" % base)

    # D1: one lane row per document, staged side a list.
    row_pairs = _row_pairs(claim["row_set"], "row_set")
    if not row_pairs:
        raise ConfigError("row_set at freeze is empty")
    reused_pairs = _row_pairs(claim.get("reused_rows") or [], "reused_rows")

    entries = _paths_from_spec(claim["entries"])
    if not entries:
        raise ConfigError("entries at freeze is empty")
    for e in entries:
        if e.startswith("/") or ".." in e.split("/"):
            raise ConfigError("entry path at freeze is not repo-relative: %r" % e)

    ground = claim["ground"]
    if not isinstance(ground, dict):
        raise ConfigError("ground at freeze is not an object")
    fragments = [str(x) for x in (ground.get("fragments") or [])]
    terms = [str(x) for x in (ground.get("terms")
                              or ground.get("cjk_terms") or [])]
    if not fragments:
        raise ConfigError("ground.fragments at freeze is empty")
    if not terms:
        raise ConfigError("ground.terms at freeze is empty")

    rejects = claim["rejects"]
    if not isinstance(rejects, dict):
        raise ConfigError("rejects at freeze is not an object")
    refused_staged_text = _cfg_refusal_text(rejects)
    refused_files = []
    for key in ("refused_files_pending_triage", "refused_files", "families"):
        value = rejects.get(key)
        if value is None:
            continue
        items = value if isinstance(value, list) else [value]
        refused_files.extend(str(x) for x in items if str(x).strip())
    counts = rejects.get("counts") or {}
    if not isinstance(counts, dict):
        raise ConfigError("rejects.counts at freeze is not an object")
    parsed_counts = {}
    for key, value in counts.items():
        try:
            parsed_counts[str(key)] = int(value)
        except (TypeError, ValueError):
            continue

    # D2: the by-document map is named by path and digest at the freeze.
    map_spec = claim.get("map")
    if not isinstance(map_spec, dict):
        raise ConfigError("claim C at freeze carries no map object")
    map_path = str(map_spec.get("path") or "").strip()
    map_sha = str(map_spec.get("sha256") or "").strip().lower()
    if not map_path or map_path.startswith("/") or ".." in map_path.split("/"):
        raise ConfigError("claim map.path at freeze is not a relative repo "
                          "path: %r" % map_path)
    if not re.fullmatch(r"[0-9a-f]{64}", map_sha):
        raise ConfigError("claim map.sha256 at freeze is not a 64-hex digest "
                          "(the by-document map cannot be pinned): %r"
                          % (map_spec.get("sha256")))

    frozen_legs = []
    for item in claim.get("legs") or []:
        name = str(item).split(":", 1)[0].strip().upper()
        if name:
            frozen_legs.append(name)

    access_date = _cfg_access_date(claim, doc)

    # D6: the claim's in-place edit (README partition heading), normalised to
    # objects carrying at least `path`.
    owned_inplace = []
    for item in claim.get("owned_inplace") or []:
        if isinstance(item, dict) and str(item.get("path") or "").strip():
            owned_inplace.append(dict(item))
        elif isinstance(item, str) and item.strip():
            owned_inplace.append({"path": item.strip()})

    rows = [p[0] for p in row_pairs]
    row_staged = dict(row_pairs)
    row_doc = {}
    for item in claim["row_set"]:
        if isinstance(item, dict):
            rid = str(item.get("id", "")).strip().upper()
            row_doc[rid] = str(item.get("document") or "").strip()
    reused = [p[0] for p in reused_pairs]
    reused_staged = dict(reused_pairs)
    lane_ids = set(rows) | set(reused)
    staged_ids = set()
    for staged in row_staged.values():
        staged_ids |= set(staged)
    for staged in reused_staged.values():
        staged_ids |= set(staged)
    # D7: a staged id that is also a lane id is not a refused staged row.
    refused_staged = []
    for text in refused_staged_text:
        for sid in TOKEN_RE.findall(text.upper()):
            if sid in staged_ids and sid not in lane_ids \
                    and sid not in refused_staged:
                refused_staged.append(sid)

    cfg = {
        "freeze": freeze,
        "frozen_sha256": hashlib.sha256(raw).hexdigest(),
        "base": base,
        "access_date": access_date,
        "rows": rows,
        "row_staged": row_staged,
        "row_doc": row_doc,
        "reused": reused,
        "reused_staged": reused_staged,
        "entries": entries,
        "fragments": fragments,
        "terms": terms,
        "refused_staged": sorted(refused_staged),
        "refused_staged_text": refused_staged_text,
        "refused_files": refused_files,
        "counts": parsed_counts,
        "map_path": map_path,
        "map_sha256": map_sha,
        "frozen_legs": frozen_legs,
        "allowed_ids": lane_ids,
        "forbidden_ids": sorted(staged_ids - lane_ids),
        "owned_inplace": owned_inplace,
        "claim_keys": sorted(claim.keys()),
    }
    return cfg


def _row_url_keys(lands_rows, sid):
    """The URL keys a registry row names: raw key UNION document key (D3).

    A page-level Persée transcription in the source cell therefore also carries
    its document's key, and the row's document key meets a page-level citation
    through `_url_keys`.
    """
    row = lands_rows.get(sid)
    if row is None:
        return set()
    cells = row_cells(row)
    if len(cells) <= SOURCE:
        return set()
    return _url_keys(urls_in(cells[SOURCE]))


def _row_has_url(lands_rows, sid, url):
    """True when `url` names a document/URL the row's source cell carries."""
    return bool(_url_keys([url]) & _row_url_keys(lands_rows, sid))


def _gate_admit_row(gate_rows, sid, lands_rows):
    """The Gate admit row for `sid`: joined by document URL first, by id token
    second.  With D3 the first join also reaches a page-level Gate URL that the
    row names only at document level (and a Wayback carrier)."""
    admits = [r for r in gate_rows if is_admit_row(r)]
    keys = _row_url_keys(lands_rows, sid)
    if keys:
        for r in admits:
            if keys & _url_keys(urls_in(r)):
                return r
    for r in admits:
        if re.search(r"\b%s\b" % re.escape(sid), r):
            return r
    return None


def _min_entry_words(mat_base):
    """The smallest corpus/knowledge entry at the claim base, in words (0 when
    the base tree carries none — the ENTRIES leg then has no floor)."""
    best = None
    for rel in tree_files(mat_base, KNOWLEDGE):
        if not rel.endswith(".md"):
            continue
        try:
            text = read_tree(mat_base, rel)
        except Missing:
            continue
        n = len(text.split())
        best = n if best is None else min(best, n)
    return best or 0


def _archive_original(u):
    """The original URL a `web.archive.org/web/<ts>/…` carrier embeds, else None.

    Returned in the carrier's own encoding (`%20` kept): the value is re-parsed
    by `urls_in`, which stops at a raw space, and the registry cell carries the
    percent-encoded form — decoding here would truncate the document path.
    """
    host, path = norm_url(u)
    bare = host[4:] if host.startswith("www.") else host
    if bare != "web.archive.org":
        return None
    m = re.match(r"^/web/\d{8,14}[a-z_]*/(.+)$", path)
    return m.group(1) if m else None


def _evidence(mat, rid):
    """Parse reports/round-75/evidence/<id>.txt at lands (capture-evidence.py
    grammar): the first occurrence of each `name: value` header line wins, the
    stored window comes from `_window`, and the raw lines are kept under `_all`
    so a QUALITY 22 two-request record is still reachable.

    Carrier disclosure (D3): when a fetch/url/final-url line names a
    `web.archive.org` capture, the document the capture carries is appended to
    the parsed value — `fetch: GET <wrapper> (original <url>)` — so a leg that
    intersects `neutral_url_keys(urls_in(ev["fetch"]))` with the row's keys
    still joins the ROW's document (S892: the live URL is challenge-walled and
    only the same-page capture is open).  The stored bytes are untouched; the
    verbatim line stays in `_text`/`_all`.
    """
    try:
        text = read_tree(mat, EVIDENCE_DIR + "/" + rid + ".txt")
    except Missing:
        return None
    out, pairs = {}, []
    for line in text.splitlines():
        m = re.match(r"^([A-Za-z][A-Za-z0-9_-]*):\s*(.*)$", line)
        if m:
            key = m.group(1).lower()
            pairs.append((key, m.group(2)))
            if key not in out:
                out[key] = m.group(2)
    originals = []
    for key in ("fetch", "url", "final-url"):
        value = out.get(key)
        if not value:
            continue
        found = [o for o in (_archive_original(u) for u in urls_in(value)) if o]
        if found:
            found = list(dict.fromkeys(found))
            originals.extend(found)
            out[key] = value + " (original %s)" % " ; ".join(found)
    out["_all"] = pairs
    out["_text"] = text
    out["_original"] = list(dict.fromkeys(originals))
    out["_window"] = _window(text)
    return out


def _window(text):
    """The stored window exactly as capture-evidence.py stores it: the lines
    between the `--- window ---` marker and `--- quote ---`, trailing empty
    lines dropped, joined by newlines (the producer writes ONE line)."""
    lines = text.splitlines()
    start = None
    for i, line in enumerate(lines):
        if line.strip() == "--- window ---":
            start = i + 1
            break
    if start is None:
        return None
    body = []
    for line in lines[start:]:
        if line.strip() == "--- quote ---":
            while body and body[-1] == "":
                body.pop()
            return "\n".join(body)
        body.append(line)
    return None


def _entry_citations(mat, entries, bad):
    """{S-id: {entry paths}} from the `source:` lines of the frozen entries."""
    cited = {}
    for e in entries:
        try:
            text = read_tree(mat, e)
        except Missing:
            bad.append("%s missing (cannot derive used-by)" % e)
            continue
        for sline in source_lines(text):
            for sid in TOKEN_RE.findall(sline):
                cited.setdefault(sid, set()).add(e)
    return cited

# part: leg-entries.py — ENTRIES leg (owner ExecLegEntries)
#
# Frozen leg text (reports/round-75/claims.json, claim C, legs[0]):
#   "ENTRIES: the frozen entries exist at <lands>, absent at base, provenance
#    header (source/verified-at/recheck/ground/topic/gap-filled/sources/
#    couples/scope) first, no header field value in {TODO, TBD, FIXME, XXX,
#    n/a, ?, —}, none matching <[^>]+>, at least one `## ` section, and a body
#    of at least 478 words (the smallest corpus/knowledge entry at base);
#    ENTRIES is a length-and-shape gate only"
#
# Readings of the ambiguous wording (each also stated in the seat report):
#  R1 "provenance header ... first": the nine fields are read only from the
#     header block, i.e. the lines before the first `## ` section (PART A
#     header_block/header_field_names). A provenance header written below the
#     body is therefore invisible and the leg fails; field ORDER inside the
#     block is not graded, because the frozen text enumerates the fields and
#     does not order them.
#  R2 "no header field value in {TODO, TBD, FIXME, XXX, n/a, ?, —}": a value
#     is a placeholder when, after casefolding and stripping the surrounding
#     dash/space, it equals a PART A PLACEHOLDERS member — or when its leading
#     whitespace token does, so "TBD — pending" is a placeholder value with an
#     excuse rather than a value. The empty value is a placeholder (PLACEHOLDERS
#     carries "").
#  R3 "none matching <[^>]+>": graded on header FIELD VALUES only — the frozen
#     clause binds the angle-marker test to the header fields, not to the H1
#     title or the body.
#  R4 "a body of at least 478 words": the body is every line from the first
#     `## ` section to EOF with heading lines removed, so heading text cannot
#     be spent as filler; the gate is the frozen constant 478 and the shared
#     _min_entry_words(mat_base) is used only to CONFIRM that constant's
#     parenthetical provenance (a mismatch is reported in the detail, never
#     graded), because the frozen text says this leg is a length-and-shape gate.
#  R5 "absent at base": the path does not exist as a file in the base tree
#     materialized from the frozen claim base.
# Deliberately NOT graded (the frozen text is shape-only, and w1
# CritCCounterVacuity's source-linked minimum was proposed, not frozen): prose
# quality, filler repetition inside an already >=478-word body, and whether a
# cited id resolves — REPOINTED/ROWS own the id resolution.
#
# Private helpers are prefixed _entries_ (the contract's `_<legfile>_` stem,
# with the file's dash written as an underscore). Shared helpers
# (_min_entry_words and the PART A functions) are CALLED, never redefined.

_ENTRIES_WORD_FLOOR = 478
_ENTRIES_HEADING_RE = re.compile(r"^#{1,6}\s")
_ENTRIES_FIELD_RE = re.compile(r"^[-*\s]*([A-Za-z][A-Za-z0-9 -]*):\s*(.*)$")


def _entries_placeholder(value):
    """R2: PLACEHOLDERS membership of the value or of its leading token."""
    v = value.strip()
    for cand in (v, v.strip("—-–").strip()):
        c = cand.casefold()
        if c in PLACEHOLDERS:
            return True
        toks = c.split()
        if toks and toks[0].rstrip(",;:.") in PLACEHOLDERS:
            return True
    return False


def _entries_body_words(lines):
    """R4: words after the first `## ` section with heading lines removed."""
    body = "\n".join(line for line in lines
                     if not _ENTRIES_HEADING_RE.match(line))
    return len(body.split())


def _entries_floor(mat_base):
    """(gate, derived): the frozen 478 is the gate; the shared helper confirms."""
    if not mat_base:
        return _ENTRIES_WORD_FLOOR, None
    try:
        derived = _min_entry_words(mat_base)
    except Exception:
        return _ENTRIES_WORD_FLOOR, None
    return _ENTRIES_WORD_FLOOR, (derived or None)


def leg_entries(ctx):
    """ENTRIES (length-and-shape gate): the frozen entries exist at <lands> and
    are absent at base; each carries the nine-field provenance header before
    its first section, no placeholder and no <...> field value, at least one
    `## ` section, and a body of at least 478 words (headings excluded)."""
    mat, mat_base, cfg = ctx["mat"], ctx.get("mat_base"), ctx["cfg"]
    bad, notes = [], []
    entries = list(cfg.get("entries") or [])
    if not entries:
        bad.append("frozen entry list is empty")
    floor, derived = _entries_floor(mat_base)
    if derived is not None and derived != floor:
        notes.append("frozen floor %d words; base derives %d" % (floor, derived))
    if not mat_base or not os.path.isdir(mat_base):
        notes.append("base tree unreadable: absent-at-base unconfirmed")
    wanted = set(norm_label(f) for f in HEADER_FIELDS)
    for e in entries:
        try:
            text = read_tree(mat, e)
        except Missing:
            bad.append("%s missing at lands" % e)
            continue
        except UnicodeDecodeError:
            # R6: an entry that is not UTF-8 text cannot carry the header or a
            # countable body; it is a shape failure, not a counter crash.
            bad.append("%s is not UTF-8 text" % e)
            continue
        if mat_base and os.path.isfile(os.path.join(mat_base, e)):
            bad.append("%s present at base (not uncovered ground)" % e)
        if not text.strip():
            bad.append("%s empty (no body)" % e)
            continue
        labels = header_field_names(text)
        missing = [f for f in HEADER_FIELDS if norm_label(f) not in labels]
        if missing:
            bad.append("%s provenance header before the first `## ` missing: %s"
                       % (e, ",".join(missing)))
        for line in header_block(text):
            m = _ENTRIES_FIELD_RE.match(line)
            if not m or norm_label(m.group(1)) not in wanted:
                continue
            value = m.group(2)
            if _entries_placeholder(value):
                bad.append("%s header field %r carries a placeholder value %r"
                           % (e, m.group(1), value.strip()[:40]))
            if ANGLE_RE.search(value):
                bad.append("%s header field %r carries a <...> template token"
                           % (e, m.group(1)))
        lines = text.splitlines()
        body_start = None
        for i, line in enumerate(lines):
            if H2_RE.match(line):
                body_start = i
                break
        if body_start is None:
            bad.append("%s has no `## ` section (header-only stub)" % e)
            continue
        words = _entries_body_words(lines[body_start:])
        if words < floor:
            bad.append("%s body has %d words (floor %d = the smallest "
                       "knowledge entry at base)" % (e, words, floor))
    # PART A prints one line per leg (`"     %s" % detail`) and the contract caps
    # that line at 300 characters; a three-entry landing can stack failures, so
    # the composed detail is cut at 295 (5 indent + 295 = 300), never reflowed.
    detail = "; ".join(dedupe(bad) + notes)
    if len(detail) > 295:
        detail = detail[:292] + "..."
    return leg("ENTRIES", not bad, detail)

def _rows_quote_core(value):
    """The stored `quote:` value with one wrapping quotation pair removed.

    The evidence producer may write the located span bare (`quote: Innombrables
    sont les récits du monde.`) or wrapped in the document's own marks
    (`quote: «Innombrables sont les récits du monde.»`).  The anchor cell wraps
    the span in its own `«…»`/`「…」`, so grading only the wrapped form would
    fail a landing whose only difference is the wrapper.  Both forms are tried;
    what has to be inside the anchor cell is the *text* of the quote.
    """
    v = value.strip()
    m = QUOTE_RE.fullmatch(v)
    if m:
        return m.group(0)[1:-1].strip()
    return v.strip('"\'“”‘’')


def _rows_cadence_ok(cell):
    """True for a cadence-ONLY recheck cell.

    PART A's RECHECK_RE documents the rule ("a cadence-only recheck cell:
    `180d`, `90d`, `on-release`, `quarterly` — never an ISO date, never a
    composite cell with prose in it"), but its body is a lowercase-phrase
    pattern that also accepts a campaign recheck sentence such as
    `re-open on 2026-10-23 and re-count the span in the served transcription`.
    The leg wording is "a cadence-only recheck cell", so the documented intent
    is enforced here too: a `NNd` cadence, or at most three lower-case/hyphen
    words carrying no digits (the lane's own vocabulary is `365d 180d 90d
    on-release`).
    """
    cell = cell.strip()
    # `re.fullmatch` on a string pattern is cached by the stdlib, so this
    # compiles once without a module-level constant.
    return bool(RECHECK_RE.match(cell)) and re.fullmatch(
        r"\d+d|[a-z][a-z-]{0,23}(?: [a-z][a-z-]{0,23}){0,2}", cell) is not None


def leg_rows(ctx):
    """ROWS: the registry diff base..<lands> adds exactly the frozen row_set.

    Frozen wording (reports/round-75/claims.json, claim C, legs[1]): "the
    registry diff base..<lands> adds exactly the frozen row_set (contiguous
    ids), none removed; each row status mined, opened 2026-10-27, a cadence-only
    recheck cell, 11 cells, no pipe in any cell, the evidence quote inside the
    anchor cell, used-by exactly the admitted entries whose source: lines cite
    it; every pre-existing row is byte-identical".

    Readings taken here (each also stated in the seat report):

    R1 "adds exactly the frozen row_set" / "none removed" is graded on the
       line multiset of both revisions, so a duplicated line cannot hide behind
       its twin.  A blank line adds no row and hides no row and is tolerated on
       either side; every other non-row line added, and every non-blank line
       removed, fails.
    R2 "contiguous ids" is a run check on the ids actually added (a gap such as
       S885..S890 + S892..S893 fails whatever the frozen set says).
    R3 "no pipe in any cell": `row_cells` splits on every `|`, so an escaped
       `\\|` from a staged cell splits one cell into two; the row is failed for
       the escaped pipe first (the as-is tell) and for the cell count second.
    R4 "the evidence quote inside the anchor cell" is the evidence file's own
       `quote:` field against the anchor cell after NFKC + whitespace folding
       (H2/R74 discipline); the self-attested `quote-found:` flags are never
       read.  A row with no committed evidence file has no quote to sit inside
       its anchor cell and fails here (the EVIDENCE leg fails it too).
    R5 "used-by exactly the admitted entries whose source: lines cite it" is
       graded BOTH ways per row: the cell names no entry that does not cite the
       row, names every entry that does, AND the citing set is non-empty.  An
       orphan row whose `used-by` is a dash because no configured entry cites it
       is not "exactly the citing entries" in the claim's sense: the after-state
       adopts each row through an entry, and an empty `used-by` cell is a
       staged row appended as-is (the kill rule's own limb).  The citing set is
       derived from `_entry_citations`, i.e. only `source:` header lines bind.
    R6 the frozen claim declares `reused_rows: []`, and the wording grants no
       in-place exception ("every pre-existing row is byte-identical"), so any
       changed pre-existing row fails.
    """
    mat, mat_base, cfg = ctx["mat"], ctx["mat_base"], ctx["cfg"]
    try:
        base_text = read_tree(mat_base, REGISTRY)
        lands_text = read_tree(mat, REGISTRY)
    except Missing as e:
        return leg("ROWS", False, "registry unreadable: %s" % e)
    base_rows = parse_rows(base_text)
    lands_rows = parse_rows(lands_text)
    want = list(cfg["rows"])
    bad = []

    # R1/R6: the line multiset diff.  Order-insensitive; a blank line is
    # tolerated, any other added line and every removed non-blank line fails.
    base_lines = [l.rstrip() for l in base_text.splitlines()]
    lands_lines = [l.rstrip() for l in lands_text.splitlines()]
    added_lines = list((Counter(lands_lines) - Counter(base_lines)).elements())
    removed_lines = list((Counter(base_lines) - Counter(lands_lines)).elements())
    inserted = []
    for line in removed_lines:
        if not line.strip():
            continue
        m = ROW_RE.match(line)
        bad.append("pre-existing %s line removed (every pre-existing row must "
                   "stay byte-identical): %r"
                   % (m.group(1) if m else "non-row", line[:60]))
    for line in added_lines:
        if not line.strip():
            continue
        m = ROW_RE.match(line)
        if not m:
            bad.append("registry line added outside the frozen row_set: %r"
                       % line[:60])
            continue
        inserted.append(m.group(1))
    if sorted(inserted) != sorted(want):
        bad.append("row lines added %s (want the frozen row_set %s)"
                   % (sorted(inserted), want))
    dup = sorted(i for i in set(inserted) if inserted.count(i) > 1)
    if dup:
        bad.append("a row line is added twice: %s" % dup)

    # the parsed-row view, for the failure a line-level diff alone words badly
    added = set(lands_rows) - set(base_rows)
    removed = set(base_rows) - set(lands_rows)
    if added != set(want):
        bad.append("rows present at lands but not at base: %s (want %s)"
                   % (sorted(added), want))
    if removed:
        bad.append("rows present at base but not at lands: %s" % sorted(removed))

    # R2: contiguous ids
    nums = sorted(int(x[1:]) for x in added)
    if nums and nums != list(range(nums[0], nums[0] + len(nums))):
        bad.append("added ids are not contiguous: %s" % nums)

    # R5: the citing entries, from the admitted entries' `source:` header lines
    cited = _entry_citations(mat, cfg["entries"], bad)

    missing = []
    for sid in want:
        row = lands_rows.get(sid)
        if row is None:
            missing.append(sid)
            continue
        if "\\|" in row:
            bad.append("%s row carries an escaped pipe (a staged cell appended "
                       "as-is): %r" % (sid, row[:60]))
            continue
        cells = row_cells(row)
        if len(cells) != NCELLS:
            bad.append("%s row has %d cells (want %d: no pipe inside any cell)"
                       % (sid, len(cells), NCELLS))
            continue
        if cells[STATUS] != "mined":
            bad.append("%s status=%r (want mined)" % (sid, cells[STATUS]))
        if cells[OPENED] != cfg["access_date"]:
            bad.append("%s opened=%r (want %s)"
                       % (sid, cells[OPENED], cfg["access_date"]))
        if not _rows_cadence_ok(cells[RECHECK]):
            bad.append("%s recheck=%r is not a cadence-only cell"
                       % (sid, cells[RECHECK]))
        want_used = set(cited.get(sid) or ())
        got_used = row_usedby(cells)
        if not want_used:
            bad.append("%s is cited by no admitted entry (orphan row; used-by=%r)"
                       % (sid, cells[USEDBY]))
        elif got_used != want_used:
            bad.append("%s used-by=%s (want exactly the admitting entries %s)"
                       % (sid, sorted(got_used), sorted(want_used)))

        # R4: the evidence quote lives inside the anchor cell
        ev = _evidence(mat, sid)
        if ev is None:
            bad.append("%s has no committed evidence file (%s/%s.txt)"
                       % (sid, EVIDENCE_DIR, sid))
            continue
        quote = (ev.get("quote") or "").strip()
        if not quote:
            bad.append("%s evidence file carries no quote: line" % sid)
            continue
        anchor = nfkc_ws(cells[ANCHOR])
        forms = dedupe([nfkc_ws(quote), nfkc_ws(_rows_quote_core(quote))])
        if not any(f and f in anchor for f in forms):
            bad.append("%s anchor cell does not contain its evidence quote (%r)"
                       % (sid, quote[:60]))
    if missing:
        bad.append("rows missing at lands: %s" % missing)
    return leg("ROWS", not bad, "; ".join(dedupe(bad)))

# ------------------------------------------------------------- REPOINTED ---
#
# Leg wording (reports/round-75/claims.json, claim C, legs[2]), as read here:
#
#   "REPOINTED: every `source:` line carries exactly one id whose row URL names
#    the cited document; every inline S-id in the entries resolves to a frozen
#    row; no campaign-namespace id is cited as a lane row except the
#    staged->lane substitutions in the frozen map; the staged S870 id is
#    replaced by lane S893; no unrelated staged id is preserved"
#
# Readings used by the implementation, each stated because the wording admits
# more than one:
#
#   R1 "source: line" is every line of the entry that carries the source field
#      (`[-*<space>]*source:`, the same line grammar PART A's header-only
#      source_lines() uses) -- not only the first provenance block: the frozen
#      entries keep one file per path with a SECOND provenance block for their
#      Part 2, and a header-only read would leave every citation below the first
#      `## ` ungraded (measured: a source line deleted from the registry and a
#      two-id source line in Part 2 both stayed green under the header-only
#      read).  The plural `sources:` field does not match that pattern and is not
#      a source line, so its ids are graded only by the inline rule.
#   R2 "row URL names the cited document" is a BY-DOCUMENT join, never
#      arithmetic: a source line's URLs and the row's source-cell URLs are
#      reduced to the frozen map's join key (host lowercased without `www.`,
#      default port dropped, path percent-decoded, persee.fr `/doc/page/<slug>/…`
#      collapsed to `/doc/<slug>`, a `web.archive.org/web/<ts>[flag]/…` wrapper
#      stripped to the embedded original) and the cited keys must be a SUBSET of
#      the row's keys -- the row may also carry page-level views the entry does
#      not quote.  A source line with no URL, or a row whose source cell carries
#      no URL, cannot be joined: both FAIL rather than pass silently.
#   R3 "inline S-id" is every S-id token anywhere in the entry (header and
#      body, source lines included); each must resolve to a frozen row
#      (cfg["allowed_ids"]).  This is what rejects the campaign-scope ids the
#      registry already reuses for unrelated documents (S744 -> the ushanka
#      page, S763 -> the tafl-games article).
#   R4 "campaign-namespace id" is an id the frozen by-document map names as
#      staged, the row_set/reused_rows `staged` values, or the frozen
#      forbidden/refused staged sets.  Such an id is legal ONLY when its map
#      target is itself (the identity substitution staged S885 -> lane S885);
#      a staged id whose map target differs (S864 -> S888) or that has no lane
#      row at all (S876, S902, S904, S905, S917, S919, S921, S870) FAILS.
#      Lane ids that are also staged ids in the campaign namespace but are not
#      in the frozen map (S886..S892, S893) cannot be distinguished from lane
#      citations by any frozen byte, so they are graded by R2's document join
#      and R3's row resolution -- the map is the only frozen authority for the
#      campaign namespace.
#   R5 "the staged S870 id is replaced by lane S893": S870 FAILS by R4, and the
#      replacement must be observable -- at least one entry cites the map's
#      lane target for S870 (S893), else the substitution did not happen.  The
#      target is read from the frozen map, never hard-coded.
#   R6 The map is read with `git show <freeze>:<cfg.map_path>` and its blob must
#      hash to cfg.map_sha256; an unpinned (empty) or mismatched map is a FAIL,
#      because the substitution table's authenticity is the clause's whole
#      content.  A map that is not ONE lookup table (one staged id with two
#      different targets) is a FAIL for the same reason.
#   R7 Absence of a `source:` line in an entry is NOT graded here: the frozen
#      ENTRIES leg owns the provenance-header field set.  This leg grades the
#      citations that exist plus R5's observable replacement.
#
# No new imports (PART A's re/hashlib/json/urlparse/... only); no network.



def _repointed_source_lines(text):
    """Every source-field line in the whole entry (R1), not only the first block.

    PART A's source_lines() stops at the first `## `; the frozen entries carry a
    second provenance block (their Part 2), whose `source:` lines are just as
    binding.  Same line grammar, whole document.
    """
    field = re.compile(r"^[-*\s]*source:\s*(.*)$")
    out = []
    for line in text.splitlines():
        m = field.match(line)
        if m:
            out.append(m.group(1))
    return out


def _repointed_unquote(s):
    """Percent-decode a URL path without importing urllib.parse.unquote."""
    if "%" not in s:
        return s
    out = bytearray()
    i, n = 0, len(s)
    while i < n:
        ch = s[i]
        if ch == "%" and i + 2 < n and re.fullmatch(r"[0-9A-Fa-f]{2}", s[i + 1:i + 3]):
            out.append(int(s[i + 1:i + 3], 16))
            i += 3
            continue
        out.extend(ch.encode("utf-8", "surrogateescape"))
        i += 1
    return bytes(out).decode("utf-8", "surrogateescape")


def _repointed_doc_key(url):
    """The frozen map's join key for one URL: (host, document path) or None.

    Strips a web.archive.org carrier wrapper (a capture is a carrier of the
    document, not a second document), lowercases the host, drops `www.` and a
    default port (:80 under http, :443 under https), percent-decodes the path
    and collapses a persee.fr per-page transcription
    (`/doc/page/<slug>/<transcription>`) onto the document `/doc/<slug>`.
    Scheme is not part of the key and no number is ever compared.
    """
    wrapper = re.compile(r"^/web/\d{8,14}[A-Za-z_]*/(.+)$")
    page = re.compile(r"^/doc/page/([^/]+)(?:/.*)?$")
    u = str(url or "").strip().rstrip(".,;:!?)]}\u3002\uff0c\uff1b\uff1a\uff01\uff1f"
                                  "\uff09\u3011\u300b\u00bb\"'")
    if not u:
        return None
    for _ in range(3):
        p = urlparse(u)
        host = (p.netloc or "").lower()
        path = p.path or ""
        if not host:
            return None
        if host == "web.archive.org" or host.endswith(".web.archive.org"):
            m = wrapper.match(path)
            if not m:
                return None
            inner = m.group(1)
            if not inner.lower().startswith(("http://", "https://")):
                inner = "https://" + inner.lstrip("/")
            u = inner
            continue
        break
    else:
        return None
    scheme = (p.scheme or "").lower()
    if "@" in host:
        host = host.rsplit("@", 1)[1]
    if host.endswith(":80") and scheme != "https":
        host = host[:-3]
    elif host.endswith(":443") and scheme == "https":
        host = host[:-4]
    if host.startswith("www."):
        host = host[4:]
    path = _repointed_unquote(path)
    if host == "persee.fr" or host.endswith(".persee.fr"):
        m = page.match(path)
        if m:
            path = "/doc/" + m.group(1)
    path = path.rstrip("/") or "/"
    return (host, path)


def _repointed_url_keys(urls):
    keys = set()
    for u in urls:
        k = _repointed_doc_key(u)
        if k is not None:
            keys.add(k)
    return keys


def _repointed_map_blob(ctx):
    """(doc, error): the by-document map read from the freeze commit, hash-pinned."""
    root, cfg = ctx["root"], ctx["cfg"]
    rel = str(cfg.get("map_path") or "").strip()
    if not rel:
        return None, "claim map.path is empty: no frozen by-document map to read"
    freeze = str(cfg.get("freeze") or "")
    r = git_bytes(root, "show", "%s:%s" % (freeze, rel))
    if r.returncode != 0:
        why = r.stderr.decode("utf-8", "replace").strip().splitlines()
        return None, ("cannot read the frozen map %s at %s: %s"
                      % (rel, freeze[:12], (why[0] if why else "git show failed")[:160]))
    raw = r.stdout
    want = str(cfg.get("map_sha256") or "").strip().lower()
    got = hashlib.sha256(raw).hexdigest()
    if not want:
        return None, ("claim map.sha256 is empty at freeze: the by-document map "
                      "%s is not hash-pinned" % rel)
    if want != got:
        return None, ("the frozen map %s hashes to %s, the claim pins %s"
                      % (rel, got, want))
    try:
        doc = json.loads(raw.decode("utf-8"))
    except (ValueError, UnicodeDecodeError) as e:
        return None, "the frozen map %s is not JSON: %s" % (rel, e)
    if not isinstance(doc, dict):
        return None, "the frozen map %s is not a JSON object" % rel
    return doc, None


def _repointed_ids(value):
    """Every S-id in a staged spec: one id, a "/"-separated list or a JSON list."""
    if isinstance(value, (list, tuple)):
        text = " ".join(str(x) for x in value)
    elif isinstance(value, str):
        text = value
    else:
        text = ""
    return [t.upper() for t in TOKEN_RE.findall(text)]


def _repointed_pairs(doc):
    """({(staged, lane): url}, error) from the frozen map, one lookup table only."""
    pairs = {}
    per_staged = {}

    def add(old, new, url):
        old = str(old or "").strip().upper()
        new = str(new or "").strip().upper()
        if not TOKEN_RE.fullmatch(old) or not TOKEN_RE.fullmatch(new):
            return
        key = (old, new)
        if key not in pairs:
            pairs[key] = str(url) if url else None
        elif url and not pairs[key]:
            pairs[key] = str(url)

    for a in doc.get("assignments") or []:
        if not isinstance(a, dict):
            continue
        add(a.get("staged_id") or a.get("old"),
            a.get("new_lane_id") or a.get("new_target") or a.get("new")
            or a.get("target") or a.get("lane"),
            a.get("url"))
    mapping = doc.get("map")
    if isinstance(mapping, dict):
        for old, val in mapping.items():
            if isinstance(val, dict):
                add(old, val.get("lane_id") or val.get("target") or val.get("lane"),
                    val.get("url"))
            else:
                add(old, val, None)
    conflict = []
    for (old, new) in pairs:
        if old in per_staged and per_staged[old] != new:
            conflict.append("%s -> %s and %s" % (old, per_staged[old], new))
        per_staged.setdefault(old, new)
    if conflict:
        return {}, ("the frozen map is not one lookup table: %s"
                    % "; ".join(dedupe(conflict)))
    return pairs, None


def _map_records(ctx):
    """{(staged_id, lane_id): url} from the frozen by-document map.

    Contract-named accessor: `git show <freeze>:<map.path>`, hash-pinned to
    cfg.map_sha256, never read from the graded tree.  Returns {} when the map
    cannot be read or does not pin (leg_repointed reports the reason).
    """
    doc, err = _repointed_map_blob(ctx)
    if err:
        return {}
    pairs, perr = _repointed_pairs(doc)
    if perr:
        return {}
    return pairs


def _repointed_staged_universe(cfg, lane_by_staged):
    """Every id the frozen config names as campaign-namespace (staged) side."""
    out = set(lane_by_staged)
    for key in ("row_staged", "reused_staged"):
        spec = cfg.get(key) or {}
        if isinstance(spec, dict):
            for val in spec.values():
                out.update(_repointed_ids(val))
        else:
            out.update(_repointed_ids(spec))
    for key in ("forbidden_ids", "refused_staged"):
        out.update(_repointed_ids(cfg.get(key) or []))
    return out


def _repointed_row_keys(row):
    """The document keys of one registry row's source cell."""
    cells = row_cells(row)
    if len(cells) <= SOURCE:
        return set()
    return _repointed_url_keys(urls_in(cells[SOURCE]))


def _repointed_problem(sid, allowed, staged, lane_by_staged, base_rows):
    """Why `sid` may not be cited as a lane row, or None when it resolves."""
    if sid in allowed:
        target = lane_by_staged.get(sid)
        if sid in staged and target not in (None, sid):
            return ("%s is a campaign-namespace id; the frozen map substitutes "
                    "it with lane %s" % (sid, target))
        return None
    if sid in staged:
        target = lane_by_staged.get(sid)
        if target:
            return ("%s is a campaign-namespace id cited as a lane row (frozen "
                    "map: %s -> %s)" % (sid, sid, target))
        return "%s is a campaign-namespace id cited as a lane row" % sid
    if sid in base_rows:
        return ("%s resolves to no frozen row; the lane registry reuses %s for "
                "an unrelated document" % (sid, sid))
    return "%s resolves to no frozen row" % sid


def leg_repointed(ctx):
    """REPOINTED: every source line names exactly one id whose registered row
    URL names the cited document (by-document join); every inline id resolves to
    a frozen row; campaign-namespace ids appear only as the frozen map's
    substitutions; the staged S870 id is replaced by its lane row."""
    mat, cfg = ctx["mat"], ctx["cfg"]
    try:
        lands_rows = parse_rows(read_tree(mat, REGISTRY))
    except Missing as e:
        return leg("REPOINTED", False, "registry unreadable at lands: %s" % e)
    doc, err = _repointed_map_blob(ctx)
    if err:
        return leg("REPOINTED", False, err)
    pairs, perr = _repointed_pairs(doc)
    if perr:
        return leg("REPOINTED", False, perr)
    allowed = set(cfg.get("allowed_ids") or ())
    if not allowed:
        return leg("REPOINTED", False,
                   "the frozen config names no lane rows (cfg.allowed_ids empty)")
    entries = cfg.get("entries") or []
    if not entries:
        return leg("REPOINTED", False, "the frozen config names no entries")
    lane_by_staged = {}
    for (old, new) in pairs:
        lane_by_staged[old] = new
    staged = _repointed_staged_universe(cfg, lane_by_staged)
    mat_base = ctx.get("mat_base")
    try:
        base_rows = parse_rows(read_tree(mat_base, REGISTRY)) if mat_base else {}
    except Missing:
        base_rows = {}
    bad = []
    cited = set()
    for e in entries:
        try:
            text = read_tree(mat, e)
        except Missing:
            bad.append("%s missing at lands" % e)
            continue
        for sline in _repointed_source_lines(text):
            ids = TOKEN_RE.findall(sline)
            if len(ids) != 1:
                bad.append("%s source line carries %d ids %s (want exactly one)"
                           % (e, len(ids), ids or "[]"))
                continue
            sid = ids[0]
            cited.add(sid)
            problem = _repointed_problem(sid, allowed, staged, lane_by_staged,
                                         base_rows)
            if problem:
                bad.append("%s source line: %s" % (e, problem))
                continue
            if sid not in lands_rows:
                bad.append("%s source line names %s with no registry row at "
                           "lands" % (e, sid))
                continue
            row_keys = _repointed_row_keys(lands_rows[sid])
            if not row_keys:
                bad.append("%s carries no document URL in its source cell, so "
                           "the cited document cannot be named" % sid)
                continue
            line_urls = urls_in(sline)
            if not line_urls:
                bad.append("%s source line for %s carries no URL (the row URL "
                           "cannot be joined to a document)" % (e, sid))
                continue
            for u in line_urls:
                key = _repointed_doc_key(u)
                if key is None or key not in row_keys:
                    bad.append("%s source line for %s cites a URL outside the "
                               "row's document: %s" % (e, sid, u))
        for lineno, line in enumerate(text.splitlines(), 1):
            for sid in TOKEN_RE.findall(line):
                cited.add(sid)
                problem = _repointed_problem(sid, allowed, staged,
                                             lane_by_staged, base_rows)
                if problem:
                    bad.append("%s:%d %s" % (e, lineno, problem))
    target = lane_by_staged.get("S870") or "S893"
    if target in allowed and target not in cited:
        bad.append("no entry cites lane %s: the staged S870 id is not replaced "
                   "by its lane row" % target)
    detail = "; ".join(dedupe(bad))
    if len(detail) > 300:
        detail = detail[:297] + "..."
    return leg("REPOINTED", not bad, detail)

# ===================================================================== GATE ===
# Claim C, leg GATE (reports/round-75/claims.json, frozen text):
#
#   "corpus/lessons/round-75.md `## Gate` carries per adopted row URL + access
#    date 2026-10-27 + a located quote of at most 25 whitespace tokens and at
#    most 80 characters + locator, and >=1 admit and >=1 reject; every reject
#    row of a probed URL carries its probed URL, reason and flip"
#
# Readings taken here (each one is a decision, recorded in
# .ufo/waves/round-75/w2/ExecLegGate.md; nothing below is stronger or weaker
# than that sentence):
#
#   R1 "per adopted row" = every lane id in cfg["rows"] + cfg["reused"].  The
#      admit row is joined to the registry row by URL first and by id token
#      second, through the shared _gate_admit_row helper (never a second join
#      rule), and the joined row must itself carry one of that registry row's
#      URLs.  A page-level Persee URL counts as the row URL because
#      _row_url_keys carries every URL of the source cell: one document row
#      owns all of its pages.
#   R2 "a located quote" = a quoted span, never a declared count.  Whatever a
#      `quote-words:` field or an `(N chars, M tokens)` note says is ignored:
#      the tokens are recounted from the span by whitespace splitting and the
#      characters by len().  A CJK span is therefore one whitespace token and
#      as many characters as it prints, so a long CJK span fails the
#      80-character cap instead of passing on a fabricated word count.
#      (Whether the span occurs on the opened page is the EVIDENCE leg's window
#      check; GATE never reads a self-attested `quote-found` flag.)
#   R3 "quote == the row's anchor quote" = the Gate span equals, after NFKC and
#      whitespace folding, the span the registry row's anchor cell marks as
#      located: the quoted span(s) after its `quote located:` marker, or every
#      quoted span of the cell when the row carries no marker.  When the cell
#      writes the anchor span without delimiters (the CJK rows are drafted that
#      way), the folded anchor span occurring verbatim in the cell is accepted,
#      so the leg binds the quote's identity to the row and not to a
#      typographic bracket.  This is what keeps a staged, absent-on-page span
#      out of the admit table after a document is re-opened under a new id.
#   R4 "locator" = a place inside the document, not the document itself.  A
#      dash/placeholder cell is no locator and neither is the row URL repeated
#      in the cell: once its URLs are removed at least one alphanumeric
#      character must remain (so `p. 11`, `§3` and `PDF p. 1, abstract` count).
#   R5 ">=1 admit and >=1 reject" = rows of the Gate section's tables, never a
#      prose marker.  A verdict that says both admitted and rejected counts as
#      neither (one row cannot satisfy the two halves at once), reject rows are
#      table rows only, and a rejection written as prose with no probed URL
#      satisfies nothing.
#   R6 "every reject row of a probed URL carries its probed URL, reason and
#      flip" = every reject row lies in a table whose header names reason and
#      flip columns, and it carries its probed URL in that table's probed-URL
#      (or URL) column -- a URL appearing only in the flip cell (the archive
#      copy a refusal flips to) is not the probed URL -- with a non-dash cell
#      in both reason and flip.


def _leg_gate_rows(lines):
    """The Gate section's Markdown table rows: lines that start with `|`.

    PART A's table_rows() also slurps any indented line into the previous row,
    which is how a prose bullet's wrapped continuation line becomes the last
    cell of the table's last row and silently turns that row's verdict into
    prose (the Gate-notes block sits right under the reject table in the
    drafted lesson).  A Markdown table row is one line, so GATE reads one line
    per row and never lets a wrapped note answer for a row.
    """
    return [line.strip() for line in lines if line.lstrip().startswith("|")]


def _leg_gate_sep(row):
    """True for a Markdown table separator row (`|---|---|`, `|:--|--:|`)."""
    cells = [c for c in row_cells(row) if c]
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", c) for c in cells)


def _leg_gate_tables(rows):
    """Split the Gate section's table rows into [{"header":..,"rows":[..]}].

    A table starts at the row directly above its separator row; the header is
    therefore always a real header and a data row that happens to contain the
    word "quote" can never be mistaken for one.  A table written without a
    separator keeps its first row as the header (tolerance, not strength).
    """
    tables = []
    for i, row in enumerate(rows):
        if _leg_gate_sep(row):
            if i == 0:
                continue
            hdr = rows[i - 1]
            if tables and tables[-1]["rows"] and tables[-1]["rows"][-1] == hdr:
                tables[-1]["rows"].pop()
            tables.append({"header": hdr, "rows": []})
            continue
        if tables:
            tables[-1]["rows"].append(row)
    if not tables and rows:
        tables = [{"header": rows[0], "rows": rows[1:]}]
    return tables


def _leg_gate_header(tables, needles):
    """The first table header whose cells satisfy every needle (needles are
    substrings of some cell, compared case-insensitively)."""
    for t in tables:
        cells = [c.lower() for c in row_cells(t["header"])]
        if all(any(n in c for c in cells) for n in needles):
            return row_cells(t["header"])
    return None


def _leg_gate_anchor_quotes(lands_rows, sid):
    """(spans, why) — the anchor quote(s) of the registry row `sid`.

    The located span(s) after the anchor cell's own `quote located:` marker
    when the marker carries any; every quoted span of the cell otherwise.  An
    empty list with a reason means the row cannot bind a quote at all.
    """
    row = lands_rows.get(sid)
    if row is None:
        return [], "no registry row at lands"
    cells = row_cells(row)
    if len(cells) <= ANCHOR:
        return [], "registry row has no anchor cell"
    cell = cells[ANCHOR]
    marker = None
    for marker in re.finditer(r"quote\s+located\s*[:：]", cell, re.I):
        pass
    if marker is not None:
        after = quoted_spans(cell[marker.end():])
        if after:
            return after, None
    spans = quoted_spans(cell)
    if not spans:
        return [], "registry anchor cell carries no quoted span"
    return spans, None


def _leg_gate_locator(cell):
    """R4: a locator is a place inside the document — not a dash, not the URL."""
    if cell is None:
        return False
    text = cell.strip()
    if text.lower() in DASHES:
        return False
    for url in urls_in(text):
        text = text.replace(url, "")
    return any(ch.isalnum() for ch in text)


def _leg_gate_quote(cell, anchor_spans):
    """R2+R3: (quote, None) when the cell carries the row's anchor quote within
    the caps, else (None, why).  Declared counts in the cell are never read."""
    spans = quoted_spans(cell)
    folded = nfkc_ws(cell)
    anchors = [(nfkc_ws(a), a) for a in anchor_spans if nfkc_ws(a)]
    seen = []
    for span in spans:
        fs = nfkc_ws(span)
        for fa, _anchor in anchors:
            if fs == fa:
                seen.append(span)
    for fa, anchor in anchors:
        if fa in folded:
            seen.append(anchor)
    if seen:
        for quote in seen:
            if quote_ok(quote):
                return quote, None
        return None, ("quote exceeds 25 whitespace tokens / 80 characters "
                      "(recounted from the span: tokens=%s chars=%s)"
                      % ([len(q.split()) for q in seen], [len(q) for q in seen]))
    if spans:
        return None, ("quoted span differs from the row's anchor quote "
                      "(recounted: tokens=%s chars=%s)"
                      % ([len(s.split()) for s in spans],
                         [len(s) for s in spans]))
    return None, ("no quoted span, and the row's anchor quote does not occur in "
                  "the quote cell (a declared word count is not a quote)")


def leg_gate(ctx):
    """GATE: the lesson's ## Gate carries, per adopted row, the row URL, the
    access date, the row's anchor quote within 25 whitespace tokens and 80
    characters, and a locator; >=1 admit and >=1 reject row; every reject row
    carries its probed URL, a reason and a flip."""
    mat, cfg = ctx["mat"], ctx["cfg"]
    try:
        text = read_tree(mat, LESSON)
        lands_rows = parse_rows(read_tree(mat, REGISTRY))
    except Missing as e:
        return leg("GATE", False, "%s" % e)
    section = gate_section(text)
    if not "".join(section).strip():
        return leg("GATE", False, "no ## Gate section in %s" % LESSON)
    tables = _leg_gate_tables(_leg_gate_rows(section))
    bad = []
    admits, rejects = [], []          # (header cells, row)
    for t in tables:
        hdr = row_cells(t["header"])
        for row in t["rows"]:
            admit, reject = is_admit_row(row), is_reject_row(row)
            if admit and reject:
                bad.append("Gate row verdict is both admitted and rejected: %s"
                           % row.strip()[:60])
            elif admit:
                admits.append((hdr, row))
            elif reject:
                rejects.append((hdr, row))

    ahdr = _leg_gate_header(tables, ("quote",))
    if ahdr is None:
        bad.append("admit table header lacks a quote column")
    else:
        if col_index(ahdr, ("date",)) is None:
            bad.append("admit table header lacks an access-date column")
        if col_index(ahdr, ("locator", "grounds", "anchor", "location")) is None:
            bad.append("admit table header lacks a locator column")
    rhdr = _leg_gate_header(tables, ("reason", "flip"))
    if rhdr is None:
        bad.append("reject table header lacks reason+flip columns")

    admit_rows = [r for _h, r in admits]
    for sid in cfg["rows"] + cfg["reused"]:
        row = _gate_admit_row(admit_rows, sid, lands_rows)
        if row is None:
            bad.append("%s has no admit row in Gate" % sid)
            continue
        hdr = ahdr
        for h, r in admits:
            if r == row:
                hdr = h
                break
        cells = row_cells(row)
        quote_i = col_index(hdr, ("quote",)) if hdr is not None else None
        date_i = col_index(hdr, ("date",)) if hdr is not None else None
        loc_i = (col_index(hdr, ("locator", "grounds", "anchor", "location"))
                 if hdr is not None else None)
        if not any(_row_has_url(lands_rows, sid, u) for u in urls_in(row)):
            bad.append("%s admit row does not carry the row URL" % sid)
        if date_i is not None:
            got = cells[date_i] if date_i < len(cells) else None
            if got != cfg["access_date"]:
                bad.append("%s admit row access date %r (want %s)"
                           % (sid, got, cfg["access_date"]))
        if loc_i is not None:
            if loc_i >= len(cells) or not _leg_gate_locator(cells[loc_i]):
                bad.append("%s admit row carries no locator cell" % sid)
        if quote_i is not None:
            if quote_i >= len(cells):
                bad.append("%s admit row has no quote cell" % sid)
            else:
                anchors, why = _leg_gate_anchor_quotes(lands_rows, sid)
                if why:
                    bad.append("%s admit row quote cannot be bound: %s"
                               % (sid, why))
                else:
                    _quote, why = _leg_gate_quote(cells[quote_i], anchors)
                    if why:
                        bad.append("%s admit row %s" % (sid, why))

    if not admits:
        bad.append("no admit row (want >=1)")
    if not rejects:
        bad.append("no reject row (want >=1)")
    for hdr, row in rejects:
        cells = row_cells(row)
        reason_i = col_index(hdr, ("reason",))
        flip_i = col_index(hdr, ("flip",))
        probed_i = col_index(hdr, ("probed", "url", "source"))
        if reason_i is None or flip_i is None:
            bad.append("reject row sits in a table without reason+flip "
                       "columns: %s" % row.strip()[:60])
            continue
        if reason_i >= len(cells) or cells[reason_i].strip().lower() in DASHES:
            bad.append("reject row carries no reason cell: %s"
                       % row.strip()[:60])
        if flip_i >= len(cells) or cells[flip_i].strip().lower() in DASHES:
            bad.append("reject row carries no flip cell: %s" % row.strip()[:60])
        if probed_i is None:
            bad.append("reject table has no probed-URL column: %s"
                       % row.strip()[:60])
        elif probed_i >= len(cells) or not urls_in(cells[probed_i]):
            bad.append("reject row carries no probed URL: %s"
                       % row.strip()[:60])
    return leg("GATE", not bad, "; ".join(dedupe(bad)))

# part: leg-evidence.py — EVIDENCE leg (owner ExecLegEvidence)
#
# Frozen leg text (reports/round-75/claims.json, claim C, legs[4]):
#   "EVIDENCE: reports/round-75/evidence/<id>.txt for every adopted row at
#    <lands>, each with fetch line, the UA used, HTTP status, bytes, the sha256
#    of the fetched body, the stored `--- window ---` text and its own
#    `window-sha256:` which the counter recomputes, with a `window-scope:`
#    header: `excerpt` (window >= 4096 characters around the quote) or
#    `whole-document` (allowed only when the whole extracted visible text is
#    shorter than 4096 characters and equal to the recorded `visible-chars:`);
#    the Gate quote occurs in the stored window after NFKC and whitespace
#    folding"
#
# Readings of the ambiguous wording (each is also stated in the seat report,
# .ufo/waves/round-75/w2/ExecLegEvidence.md):
#
#  R1 "<id>" is the ADOPTED LANE id (cfg["rows"] + cfg["reused"]), one file per
#     adopted row, never a staged id: every other leg keys the row set on the
#     lane ids, and the by-document map is what turns staged ids into them. A
#     staged-only id has no file requirement (and no file is read for it).
#  R2 "fetch line" names the row's document. The file is evidence FOR that row,
#     so its `fetch:`/`url:` URL must name a URL the row's SOURCE cell carries.
#     The join is the shared part-cfg predicate _row_has_url (raw norm_url key
#     union _doc_url_key: host without `www.`, percent-decoded, /doc/page/… and
#     /docAsPDF/… folded to /doc/<slug>, web.archive.org/web/<ts>/<original>
#     folded to <original>). That is what lets one row carry the document URL
#     plus page-level Persee URLs, and what joins S892's committed
#     web.archive.org capture to the iris.unipa.it URL its source cell names.
#     No local URL-matching rule is defined here: `_row_url_keys`' key space is
#     part-cfg's, and an intersection with PART A neutral_url_keys is a
#     DIFFERENT key space (netloc keeps `www.`, no document folding) that would
#     never meet it.
#  R3 "the Gate quote" is read from the Gate admit row's QUOTE COLUMN, not from
#     any quoted text in that row: a source cell carries the document title in
#     `«»` and authenticating the title would not authenticate the quote. When
#     the admit table has no identifiable quote column the leg falls back to
#     every quoted span of the admit row (the round-74 grammar). Candidates are
#     the column's delimited spans UNION the registry row's anchor-cell spans
#     that the column carries after NFKC + whitespace folding, because the GATE
#     leg (leg-gate.py R2/R3) binds an undelimited CJK quote cell to the row's
#     anchor quote: without the second half the two legs would disagree about
#     which string "the Gate quote" is on the drafted S888/S893 cells. At least
#     one candidate of <=25 whitespace tokens and <=80 characters is required
#     (PART A quote_ok) and at least one candidate must occur in the stored
#     window; the GATE leg owns the quote's identity, its size and its locator.
#  R4 "bytes" and "the sha256 of the fetched body" are graded for SHAPE here: a
#     positive byte count and a 64-hex digest. A leg has no network, so it
#     cannot re-derive the body; the ordinary re-open routed in the claim is
#     what binds body truth, and the w1 vacuity finding is reported, not
#     papered over.
#  R5 "the UA used" is graded as browser-shaped: recorded, starting
#     "Mozilla/5.0", and carrying no client/robot token (curl/, Wget/,
#     python-requests, python-urllib, libwww, scrapy, java/, go-http-client,
#     bot, spider, crawler, headless, phantomjs).
#  R6 "no challenge" (claim kill rule; QUALITY 10): the capture must RECORD its
#     challenge state and it must be `none`. A missing `challenge:` line is not
#     proof of a clean response; a met challenge is an UNOPENED source.
#  R7 `quote-found:` / `quote-found-verbatim:` are NEVER read. The capture tool
#     records them for a human; the recomputed window digest and the NFKC +
#     whitespace fold are the grader. A file saying `quote-found: no` whose
#     window does contain the quote PASSES, and a file saying `quote-found: yes`
#     whose window does not PASS-FREE fails.
#  R8 an all-whitespace stored window is a FAIL, never a skip: round-74's
#     counter skipped its quote test on a blank window (`if window is None or
#     not window.strip(): continue`), which let a landing blank every window
#     and grade green (w1 ExecJunkFixtures F2). Here the fold of the window is
#     computed once and an empty fold is reported.
#  R9 `excerpt` has a floor and no ceiling, but a window cannot be longer than
#     the visible text it was cut from: when `visible-chars:` is present on an
#     excerpt it must be >= len(window). This is internal consistency, not a
#     new scope rule - no file the capture tool writes can violate it - and it
#     is the mirror of the tool's own "short window under a long visible-chars"
#     verification rule. `visible-chars:` is REQUIRED only for
#     `whole-document`, which is the only scope the frozen text couples it to.
#  R10 the window is the exact stored bytes: the single line between the
#     `--- window ---` and `--- quote ---` markers, hashed as UTF-8 with no
#     trailing newline (part-cfg _window). `window-bytes:`, when present, must
#     equal that byte length; `window-sha256:` must equal its sha256.
#
# Private helpers are prefixed _evidence_ (the contract's `_<legfile>_` stem).
# Shared helpers (_evidence, _window, _row_url_keys, _gate_admit_row and the
# PART A functions) are CALLED, never redefined.

_EVIDENCE_UA_ROBOT_RE = re.compile(
    r"(?i)(?:curl/|wget/|python-requests|python-urllib|libwww|scrapy"
    r"|java/|go-http-client|phantomjs|headless|bot\b|spider|crawler)")
_EVIDENCE_CLEAN_CHALLENGE = ("", "none")


def _evidence_count(value):
    """A recorded non-negative integer, or None (`12` yes, `1,024` no)."""
    s = (value or "").strip()
    return int(s) if s.isdigit() else None


def _evidence_fold(text):
    """The one fold in play: NFKC, whitespace runs to one space, ends stripped."""
    return nfkc_ws(text or "")


def _evidence_fetch_names_row(fetch, lands_rows, sid):
    """R2: the fetch line names the row's document (part-cfg _row_has_url)."""
    fetch_urls = urls_in(fetch or "")
    if not fetch_urls:
        return False
    return any(_row_has_url(lands_rows, sid, u) for u in fetch_urls)


def _evidence_gate_quote_text(gate_rows, grow):
    """R3: the admit row's quote column, falling back to the whole row."""
    header = table_header(gate_rows, ("quote",))
    if header is None:
        return grow
    qi = col_index(header, ("quote",))
    if qi is None:
        return grow
    cells = row_cells(grow)
    return cells[qi] if qi < len(cells) else grow


def _evidence_anchor_spans(lands_rows, sid):
    """The delimited spans of the registry row's ANCHOR cell (quote_ok only)."""
    row = lands_rows.get(sid)
    if row is None:
        return []
    cells = row_cells(row)
    if len(cells) <= ANCHOR:
        return []
    return [s for s in quoted_spans(cells[ANCHOR]) if quote_ok(s)]


def _evidence_gate_quote_candidates(gate_rows, grow, lands_rows, sid):
    """R3: the strings the Gate record may be carrying as its quote.

    Delimited spans of the quote column, plus the row's anchor spans that the
    column carries after the fold (the undelimited CJK cell GATE's R3 binds).
    Returned folded, empty strings dropped.
    """
    cell = _evidence_gate_quote_text(gate_rows, grow)
    cell_fold = _evidence_fold(cell)
    cands = [_evidence_fold(s) for s in quoted_spans(cell) if quote_ok(s)]
    for span in _evidence_anchor_spans(lands_rows, sid):
        folded = _evidence_fold(span)
        if folded and folded in cell_fold:
            cands.append(folded)
    return [c for c in cands if c]


def _evidence_core(ev, sid, access_date, lands_rows):
    """Header, digest, length and scope checks for one evidence file.

    Returns (bad, window). `window` is the exact stored window string (or None
    when the file stores no window block); the caller runs the quote test on it
    and NEVER skips that test for a short or blank window (R8).

    The scope rule is re-derived from the stored bytes: `excerpt` needs at
    least MIN_WINDOW_CHARS characters; `whole-document` is allowed only when the
    stored window is shorter than MIN_WINDOW_CHARS and its length equals the
    recorded `visible-chars:`. No flag in the file decides either.
    """
    bad = []
    status = (ev.get("http-status") or ev.get("http") or "").strip()
    if status != "200":
        bad.append("%s http-status %r (want 200)" % (sid, status))
    if ev.get("access-date") != access_date:
        bad.append("%s access-date %r (want %s)"
                   % (sid, ev.get("access-date"), access_date))
    size = _evidence_count(ev.get("bytes"))
    if size is None or size <= 0:
        bad.append("%s bytes %r is not a positive byte count"
                   % (sid, (ev.get("bytes") or "")[:20]))
    if not re.fullmatch(r"[0-9a-f]{64}", (ev.get("sha256") or "").strip().lower()):
        bad.append("%s sha256 line is not a 64-hex digest of the fetched body" % sid)
    ua = (ev.get("user-agent") or ev.get("ua") or "").strip()
    if not ua:
        bad.append("%s records no user-agent" % sid)
    elif not ua.startswith("Mozilla/5.0"):
        bad.append("%s user-agent is not browser-shaped: %r" % (sid, ua[:40]))
    elif _EVIDENCE_UA_ROBOT_RE.search(ua):
        bad.append("%s user-agent carries a client/robot token: %r"
                   % (sid, ua[:60]))
    fetch = (ev.get("fetch") or ev.get("url") or "").strip()
    if not fetch:
        bad.append("%s carries no fetch line" % sid)
    elif not _evidence_fetch_names_row(fetch, lands_rows, sid):
        bad.append("%s fetch line does not name the row's document: %r"
                   % (sid, fetch[:70]))
    challenge = ev.get("challenge")
    if challenge is None:
        bad.append("%s records no challenge line (a clean response must say so)"
                   % sid)
    elif challenge.strip().lower() not in _EVIDENCE_CLEAN_CHALLENGE:
        bad.append("%s records a served challenge (%r): a challenge met is an "
                   "UNOPENED source" % (sid, challenge.strip()[:40]))
    window = ev["_window"]
    if window is None:
        bad.append("%s stores no --- window --- block" % sid)
        return bad, None
    payload = window.encode("utf-8")
    digest = hashlib.sha256(payload).hexdigest()
    declared = (ev.get("window-sha256") or "").strip().lower()
    if declared != digest:
        bad.append("%s window-sha256 %r != the recomputed digest of the stored "
                   "window (%s)" % (sid, declared[:16], digest[:16]))
    declared_bytes = (ev.get("window-bytes") or "").strip()
    if declared_bytes and declared_bytes != str(len(payload)):
        bad.append("%s window-bytes %r != the stored window's %d bytes"
                   % (sid, declared_bytes, len(payload)))
    scope = (ev.get("window-scope") or "").strip().lower()
    if scope not in ("excerpt", "whole-document"):
        bad.append("%s window-scope %r (want excerpt|whole-document)"
                   % (sid, (ev.get("window-scope") or "")[:30]))
    visible_raw = ev.get("visible-chars")
    visible = _evidence_count(visible_raw)
    if visible_raw is not None and visible is None:
        bad.append("%s visible-chars %r is not a character count"
                   % (sid, (visible_raw or "")[:20]))
    if scope == "excerpt":
        if len(window) < MIN_WINDOW_CHARS:
            bad.append("%s excerpt window is %d characters (want >= %d)"
                       % (sid, len(window), MIN_WINDOW_CHARS))
        elif visible is not None and visible < len(window):
            bad.append("%s excerpt window is %d characters but the recorded "
                       "visible text is %d (a window cannot exceed its document)"
                       % (sid, len(window), visible))
    elif scope == "whole-document":
        if visible is None:
            bad.append("%s whole-document window records no visible-chars" % sid)
        else:
            if len(window) >= MIN_WINDOW_CHARS:
                bad.append("%s whole-document window is %d characters (>= %d: "
                           "declare excerpt)" % (sid, len(window),
                                                 MIN_WINDOW_CHARS))
            if visible != len(window):
                bad.append("%s whole-document window is %d characters but "
                           "visible-chars is %d" % (sid, len(window), visible))
    return bad, window


def leg_evidence(ctx):
    """EVIDENCE (H2/R1-R10): a committed capture per adopted/reused row - fetch
    line naming the row's document, browser-shaped UA, HTTP 200, recorded bytes,
    64-hex body digest, a stored window whose scope rule holds, and the Gate
    quote INSIDE that window after NFKC + whitespace folding. No flag is read
    and a blank window fails rather than skipping the quote test."""
    mat, cfg = ctx["mat"], ctx["cfg"]
    try:
        gate_rows = table_rows(gate_section(read_tree(mat, LESSON)))
        lands_rows = parse_rows(read_tree(mat, REGISTRY))
    except Missing as e:
        return leg("EVIDENCE", False, "%s" % e)
    bad = []
    for sid in cfg["rows"] + cfg["reused"]:
        ev = _evidence(mat, sid)
        if ev is None:
            bad.append("%s evidence file missing (%s/%s.txt)"
                       % (sid, EVIDENCE_DIR, sid))
            continue
        row_bad, window = _evidence_core(ev, sid, cfg["access_date"], lands_rows)
        bad.extend(row_bad)
        if window is None:
            continue
        folded = _evidence_fold(window)
        if not folded:
            bad.append("%s stored window carries no visible text" % sid)
            continue
        grow = _gate_admit_row(gate_rows, sid, lands_rows)
        if grow is None:
            bad.append("%s has no Gate admit row to couple the window to" % sid)
            continue
        qspans = dedupe(_evidence_gate_quote_candidates(gate_rows, grow,
                                                        lands_rows, sid))
        if not qspans:
            bad.append("%s Gate admit row carries no <=25-token, <=80-char quote"
                       % sid)
            continue
        if not any(q in folded for q in qspans):
            bad.append("%s Gate quote is absent from the stored window "
                       "(substring after NFKC+whitespace folding)" % sid)
    return leg("EVIDENCE", not bad, "; ".join(dedupe(bad)))

# leg-rejects.py — REJECTS leg of the round-75 claim-C counter.
# Owner: ExecLegRejects.  Assembly: PART A + part-cfg.py + this part + part-main.py.
# Function definitions only: no top-level code, no imports.
#
# Frozen leg text (reports/round-75/claims.json, claim C, `legs`; re-cut by the
# L1 pre-data on 2026-10-27):
#   "REJECTS: the lesson states the triage counts of the 40 staged knowledge
#    files as `3 adopted / 6 path-present / 31 refused` (the three numbers sum
#    to 40 and equal rejects.counts at the freeze), names each refused staged
#    row and file with reason and flip, names staged S870's disposition with
#    its re-quote or its refusal, and carries a `## Quarantine` section
#    recording the standing register verdicts".
#
# Readings of the ambiguous clauses (each one restated in the seat report):
#
#  * "the triage counts" = ONE lesson paragraph that states all four numbers:
#    adopted, path-present, refused and the staged-file total, with
#    adopted + path_present + refused == total.  Every one of the three
#    published numbers is pinned by `cfg["counts"]` (the freeze's
#    `rejects.counts`: 3 / 6 / 31 / 40) and adopted is additionally pinned to
#    len(cfg["entries"]).  There is no other arithmetic: refused is NOT derived
#    as total - adopted (the L1 2026-10-27 cut).
#  * "names each refused staged row and file with reason and flip" is
#    per-item: the table row that names the item must carry a substantive
#    reason cell AND a substantive flip cell (CritCCounterVacuity repair 6).
#    Global occurrences of the words "reason"/"flip" do not satisfy the leg.
#  * the file buckets must carry the two frozen numbers, split the way the
#    freeze splits them: rows whose first cell names a refused family sum to
#    `counts.refused`; rows that name no refused family (the path-present
#    bucket) sum to `counts.path_present` (RevClaimsFidelity F11's
#    reconciliation, kept but re-cut to the new counts).
#  * "staged S870's disposition" = the staged quote's refusal AND the
#    re-quote / re-opened lane row, joined by the frozen row_staged map; the
#    claim's `after` and kill rule both say the quote stays refused while the
#    document re-opens as S893, so "or" is read as "the disposition named,
#    with the re-quote side present whenever the freeze maps a target".
#  * "the standing register verdicts" is re-derived from the committed
#    reports/round-71/telemetry/quarantine-verdicts.md at <lands>; the lesson's
#    `## Quarantine` section must record the same per-class counts, the total
#    and every REFUSED id.  Only the lesson is read for the triage counts.

def _rejects_paragraphs(text):
    """Blank-line separated blocks (a markdown table is one block)."""
    return [p for p in re.split(r"\n[ \t]*\n", text) if p.strip()]


def _rejects_tables(text):
    """[(header_cells, [row_cells, ...])] for every markdown table block."""
    out, header = [], None
    for line in text.splitlines():
        s = line.strip()
        if not s.startswith("|"):
            header = None
            continue
        cells = row_cells(s)
        if header is None:
            header = cells
            out.append([header, []])
            continue
        if cells and all(re.fullmatch(r":?-{2,}:?", c.replace(" ", ""))
                         for c in cells):
            continue
        out[-1][1].append(cells)
    return [(h, rows) for h, rows in out if rows]


def _rejects_units(text):
    """The lesson as per-item units: one unit per table row, else paragraph."""
    units = []
    for block in _rejects_paragraphs(text):
        rows = [l.strip() for l in block.splitlines() if l.strip().startswith("|")]
        if len(rows) >= 2:
            units.extend(rows)
        else:
            units.append(block)
    return units


def _rejects_stated_counts(text):
    """(adopted, path_present, refused, total) from the one paragraph stating all."""
    for para in _rejects_paragraphs(text):
        total = (re.search(r"(\d+)\s+staged\b[^\n]{0,24}?files?\b", para)
                 or re.search(r"\bof\s+(?:the\s+)?(\d+)\s+staged\b", para, re.I))
        if total is None:
            # the identity itself, e.g. `3 + 6 + 31 = 40`
            total = re.search(r"\d+(?:\s*\+\s*\d+)+\s*=\s*(\d+)", para)
        adopted = (re.search(r"(\d+)\s+adopted\b", para, re.I)
                   or re.search(r"\badopted\b[^\n]{0,40}?(\d+)", para, re.I))
        present = (re.search(r"(\d+)\s+path-?\s?present\b", para, re.I)
                   or re.search(r"\bpath-?\s?present\b[^\n]{0,40}?(\d+)", para, re.I))
        refused = (re.search(r"(\d+)\s+(?:staged\s+|files?\s+)?refused\b",
                             para, re.I)
                   or re.search(r"\brefused\b[^\n]{0,40}?(\d+)", para, re.I))
        if total and adopted and present and refused:
            return (int(adopted.group(1)), int(present.group(1)),
                    int(refused.group(1)), int(total.group(1)))
    return None


def _rejects_real(cell):
    """A substantive reason/flip cell: not a dash/placeholder, not a stub."""
    s = nfkc_ws(cell).strip("*`_ ")
    if s.lower() in DASHES or s.lower() in PLACEHOLDERS:
        return False
    words = [w for w in s.split()
             if re.search(r"[A-Za-z0-9\u00c0-\u024f\u3040-\u30ff\u4e00-\u9fff]", w)]
    return len(words) >= 4 or len(s) >= 40


def _rejects_families(cfg):
    """[(name tests, frozen count, raw spec)] per refused_files entry."""
    out = []
    for spec in cfg.get("refused_files") or []:
        s = nfkc_ws(str(spec))
        m = re.search(r"\sx(\d+)\b|\bx(\d+)\b", s)
        if m:
            n = int(m.group(1) or m.group(2))
        elif re.search(r"\band\b", s):
            # "amend-2026-10-23c and amend-2026-10-24 refused as separate paths"
            n = 2
        else:
            n = 1
        head = re.split(r"\s+x\d+\b", s)[0]
        head = re.split(r"\s+and\s+", head)[0]
        head = re.split(r"\b(?:refused|rejected|pending|not)\b", head,
                        flags=re.I)[0]
        toks = head.strip(" ;,.").split()
        tok = toks[0] if toks else head.strip()
        names = []
        if ".amend-" in tok:
            names.append(tok.split(".amend-")[0])
        if "/" in tok:
            first = tok.split("/")[0]
            names.append(first)
            if ".amend-" in first:
                names.append(first.split(".amend-")[0])
        names.append(tok)
        names = [x for x in dict.fromkeys(names) if len(x) >= 3]
        out.append((names, n, s))
    return out


def _rejects_refuse_rows(text):
    """[(cells, reason_index, flip_index)] for every reason+flip table row."""
    out = []
    for header, rows in _rejects_tables(text):
        ri = col_index(header, ("why", "reason"))
        fi = col_index(header, ("flip", "revers", "clearing"))
        if ri is None or fi is None:
            continue
        for cells in rows:
            out.append((cells, ri, fi))
    return out


def _rejects_cell(cells, idx):
    return cells[idx] if 0 <= idx < len(cells) else ""


def _rejects_row_count(cells):
    """(n, declared) — the refused-file count the row declares for itself.

    Accepted shapes: a cell that is only digits (`| 11 |`), a cell that is an
    addition of digits (`| 3 + 1 |`), or `(N)` / `xN` inside the row.  A row
    with none of these declares no count, so it cannot reconcile.
    """
    total, found = 0, False
    for c in cells:
        s = nfkc_ws(c)
        if re.fullmatch(r"\d+", s):
            total += int(s)
            found = True
        elif re.fullmatch(r"\d+(\s*\+\s*\d+)+", s):
            total += sum(int(x) for x in re.findall(r"\d+", s))
            found = True
    if found:
        return total, True
    blob = nfkc_ws(" ".join(cells))
    m = re.search(r"\((\d+)\)", blob) or re.search(r"\bx(\d+)\b", blob)
    if m:
        return int(m.group(1)), True
    return 0, False


def leg_rejects(ctx):
    """REJECTS: triage counts, per-item reason+flip, S870 disposition,
    `## Quarantine` with the standing register verdicts."""
    mat, cfg = ctx["mat"], ctx["cfg"]
    try:
        text = read_tree(mat, LESSON)
    except Missing as e:
        return leg("REJECTS", False, "lesson unreadable at <lands>: %s" % e)
    bad = []
    entries = list(cfg.get("entries") or [])
    fams = _rejects_families(cfg)
    counts = cfg.get("counts") or {}

    # --- 1. the triage counts, stated in one paragraph ---------------------
    # --- 1. the triage counts: 3 adopted / 6 path-present / 31 refused (40) --
    stated = _rejects_stated_counts(text)
    exp_adopted = counts.get("adopted", len(entries))
    exp_present = counts.get("path_present")
    exp_refused = counts.get("refused")
    exp_total = counts.get("total_staged_files", counts.get("total"))
    if exp_adopted != len(entries):
        bad.append("config inconsistency: counts.adopted %r vs the frozen entry "
                   "set (%d)" % (exp_adopted, len(entries)))
    if stated is None:
        bad.append("lesson states no single triage-counts paragraph "
                   "(adopted + path-present + refused + staged total together)")
    else:
        a, p, r, t = stated
        if a + p + r != t:
            bad.append("triage counts do not sum: %d adopted + %d path-present + "
                       "%d refused = %d, not the %d stated" % (a, p, r, a + p + r, t))
        for label, got, want in (("adopted", a, exp_adopted),
                                 ("path-present", p, exp_present),
                                 ("refused", r, exp_refused),
                                 ("staged total", t, exp_total)):
            if want is not None and got != want:
                bad.append("lesson states %d %s; the freeze holds %d"
                           % (got, label, want))

    # --- 2. refused file families: named, reason+flip, counts reconcile ---
    refuse = _rejects_refuse_rows(text)
    fam_names = [x for names, _n, _sp in fams for x in names]
    fam_total, fam_rows, odd_total, odd_rows = 0, 0, 0, 0
    for cells, _ri, _fi in refuse:
        first = nfkc_ws(cells[0]) if cells else ""
        if re.search(r"\bS\d{3}\b", first):
            continue  # a staged-row / reject row, not a refused-file bucket
        n, declared = _rejects_row_count(cells)
        if not declared:
            continue
        if any(x in first for x in fam_names):
            fam_total += n
            fam_rows += 1
        else:
            odd_total += n
            odd_rows += 1
    for names, n, spec in fams:
        label = names[0] if names else spec[:40]
        cands = [(c, ri, fi) for c, ri, fi in refuse
                 if any(x in nfkc_ws(" ".join(c)) for x in names)]
        if not cands:
            bad.append("refused file family %r is not named in a table row "
                       "carrying a reason column and a flip column" % label)
            continue
        why = "no candidate row"
        good = False
        for cells, ri, fi in cands:
            reason = _rejects_cell(cells, ri)
            flip = _rejects_cell(cells, fi)
            if not _rejects_real(reason):
                why = "%r: reason cell is empty, a dash or a placeholder" % label
                continue
            if not _rejects_real(flip):
                why = "%r: flip cell is empty, a dash or a placeholder" % label
                continue
            good = True
            break
        if not good:
            bad.append(why)
    want_refused = exp_refused if exp_refused is not None else (stated[2] if stated else None)
    want_present = exp_present if exp_present is not None else (stated[1] if stated else None)
    if want_refused is not None:
        if fam_rows == 0:
            bad.append("no refused-family bucket row declares a file count; the "
                       "triage counts cannot be reconciled to the refused files")
        elif fam_total != want_refused:
            bad.append("refused-family buckets sum to %d files; the freeze holds "
                       "%d refused" % (fam_total, want_refused))
    # L1 pre-freeze edit: the path-present count is bound by the one triage
    # paragraph's ternary identity (section 1) and cfg counts; a table-row bucket
    # for it is stronger than the claim wording ("states the triage counts"), so
    # it is not graded (odd_rows/odd_total stay informational).

    # --- 3. the refused staged row's disposition --------------------------
    units = _rejects_units(text)
    for sid in cfg.get("refused_staged") or []:
        hits = [u for u in units if re.search(r"\b%s\b" % re.escape(sid), u)]
        if not hits:
            bad.append("refused staged %s is not named in the lesson" % sid)
            continue
        rows = [t for t in refuse
                if re.search(r"\b%s\b" % re.escape(sid), nfkc_ws(" ".join(t[0])))]
        if rows and not any(_rejects_real(_rejects_cell(c, ri)) and
                            _rejects_real(_rejects_cell(c, fi))
                            for c, ri, fi in rows):
            bad.append("refused staged %s: no row states both a reason and a flip"
                       % sid)
        if not any(REFUSAL_RE.search(u) for u in hits):
            bad.append("refused staged %s carries no refusal in its own row, "
                       "paragraph or reject row" % sid)
        targets = sorted(rid for rid, staged in (cfg.get("row_staged") or {}).items()
                         if sid in (staged or []))
        requoted = any(REQUOTE_RE.search(u) or re.search(r"re-?\s?open", u, re.I)
                       for u in hits)
        tied = any(any(rid in u for rid in targets) for u in hits)
        if targets:
            if not (requoted or tied):
                bad.append("staged %s is not tied to its re-opened lane row %s"
                           % (sid, ",".join(targets)))
            elif not tied:
                bad.append("staged %s's re-quote does not name the lane row %s"
                           % (sid, ",".join(targets)))
        elif not requoted:
            bad.append("staged %s is named without a re-quote or a refusal" % sid)

    # --- 4. `## Quarantine` and the standing register verdicts ------------
    qsec = section_block(text, r"^##\s+Quarantine\b")
    if not qsec.strip():
        bad.append("no `## Quarantine` section in the lesson")
    else:
        verdicts = {"PRESENT": [], "REFUSED": [], "UNVERIFIABLE": []}
        try:
            reg = read_tree(mat,
                            "reports/round-71/telemetry/quarantine-verdicts.md")
        except Missing as e:
            bad.append("standing register verdicts unreadable at <lands>: %s" % e)
        else:
            for line in reg.splitlines():
                m = re.match(r"^\|\s*(S\d{3})\s*\|\s*(PRESENT|REFUSED|UNVERIFIABLE)\s*\|",
                             line)
                if m:
                    verdicts[m.group(2)].append(m.group(1))
        total = sum(len(v) for v in verdicts.values())
        if not total:
            if "register" not in nfkc_ws(qsec).lower():
                bad.append("`## Quarantine` does not record the register verdicts")
        else:
            if "register" not in nfkc_ws(qsec).lower():
                bad.append("`## Quarantine` does not name the register")
            paras = _rejects_paragraphs(qsec)
            for cls in ("PRESENT", "REFUSED", "UNVERIFIABLE"):
                ids = verdicts[cls]
                if not ids:
                    continue
                want = len(ids)
                ok = any(re.search(r"\b%s\b" % cls, p, re.I) and
                         re.search(r"(?<![\d])%d(?![\d])" % want, p)
                         for p in paras)
                if not ok:
                    bad.append("`## Quarantine` does not record %s %d" % (cls, want))
            if not re.search(r"(?<![\d])%d(?![\d])" % total, qsec):
                bad.append("`## Quarantine` does not record the %d-row total"
                           % total)
            for rid in verdicts["REFUSED"]:
                if not re.search(r"\b%s\b" % rid, qsec):
                    bad.append("REFUSED register row %s is not named in "
                               "`## Quarantine`" % rid)
                    continue
                naming = [p for p in paras if rid in p]
                if not any("refused" in nfkc_ws(p).lower() for p in naming):
                    bad.append("register row %s is named in `## Quarantine` "
                               "without its REFUSED verdict" % rid)
    detail = "; ".join(dedupe(bad))
    if len(detail) > 300:
        detail = detail[:297] + "..."
    return leg("REJECTS", not bad, detail)

def _ground_cited_census_has_zero(text):
    """A standalone 0 token: `0`, never `10`, `808`, `0x`, `-0.5`."""
    return re.search(r"(?:^|[^\d])0(?:[^\d]|$)", text) is not None


def _ground_cited_census_ecodes(out):
    """E-code findings in a sources-census.sh TSV stream.

    The frozen wording is "prints no `^E[0-9][0-9]` line".  The fleet script
    emits `<lane>\\t<E-code>\\t<value>` (e.g. `file\\tE01\\tS894`), so the literal
    anchored form can never match the script's own output; the field form
    below implements the wording's reading — no E-code finding line — and also
    accepts a bare `E01` line should the format ever change.  The exit status
    remains the load-bearing check: sources-census.sh exits 1 on any E finding.
    """
    return dedupe(re.findall(r"(?:^|\t)(E\d\d)(?=\t|$)", out, re.M))


def leg_ground(ctx):
    """GROUND: reports/round-75/telemetry/gap-sweep.txt names the 808-row
    registry and 0 matches per fragment at base; the counter independently
    re-derives 0 at base from mat_base.

    Reading of the frozen text: it names the registry count and the fragments
    only, so `cfg["terms"]` (part of the ground config) is NOT graded here —
    the leg may neither add nor drop a term check — and "absent at base" for
    the entry paths belongs to ENTRIES.  The receipt is graded from `mat`
    (committed bytes at <lands>); the re-derivation is read from `mat_base`,
    which the counter materialized itself, so the receipt cannot vouch for
    itself.
    """
    mat, mat_base, cfg = ctx["mat"], ctx["mat_base"], ctx["cfg"]
    frags = list(cfg.get("fragments") or [])
    if not frags:
        return leg("GROUND", False, "cfg carries no ground fragments")
    try:
        base_text = read_tree(mat_base, REGISTRY)
    except Missing as e:
        return leg("GROUND", False, "base registry unreadable: %s" % e)
    base_rows = parse_rows(base_text)
    bad = []
    try:
        receipt = read_tree(mat, GROUND_RECEIPT)
    except Missing:
        receipt = ""
    if not receipt.strip():
        bad.append("receipt missing: %s" % GROUND_RECEIPT)
    else:
        m = re.search(r"(\d+)[- ]row", receipt)
        if not m:
            bad.append("receipt names no N-row registry")
        elif int(m.group(1)) != len(base_rows):
            bad.append("receipt names a %d-row registry; the base holds %d"
                       % (int(m.group(1)), len(base_rows)))
        lines = receipt.splitlines()
        for frag in frags:
            idxs = [i for i, line in enumerate(lines) if frag in line]
            if not idxs:
                bad.append("receipt does not name fragment %r" % frag)
                continue
            found_zero = False
            for i in idxs:
                # the 0 must belong to this fragment's own entry: its line plus
                # any continuation lines, stopping at a blank line or at the
                # next fragment's line, so a zero printed for a different item
                # (or for a whole-list total) cannot vouch for this one
                window = [lines[i]]
                for nxt in lines[i + 1:i + 3]:
                    if not nxt.strip() or any(f in nxt for f in frags):
                        break
                    window.append(nxt)
                text = "\n".join(window)
                # the fragment's own digits are stripped before the zero is
                # looked for, so e.g. `_0588` can never supply one
                for other in frags:
                    text = text.replace(other, "")
                if _ground_cited_census_has_zero(text):
                    found_zero = True
                    break
            if not found_zero:
                bad.append("receipt shows no 0 for fragment %r" % frag)
    low_registry = base_text.lower()
    for frag in frags:
        if frag.lower() in low_registry:
            bad.append("base registry already names the fragment %r" % frag)
    return leg("GROUND", not bad, "; ".join(dedupe(bad))[:300])


def leg_citedlines(ctx):
    """CITEDLINES: tools/check-cited-lines.py over the entries from the
    materialized tree prints `CITED-LINES: 0 finding(s)`.

    Reading of the frozen text: the tool is the one read from `mat` (the
    materialized lands tree) — the frozen wording pins no blob, so this leg
    does not pin one either; the entries are exactly `cfg["entries"]`, and a
    missing entry is a FAIL rather than a silently shorter run.
    """
    mat, cfg = ctx["mat"], ctx["cfg"]
    entries = list(cfg.get("entries") or [])
    if not entries:
        return leg("CITEDLINES", False, "cfg carries no entries")
    tool = os.path.join(mat, "tools/check-cited-lines.py")
    if not os.path.isfile(tool):
        return leg("CITEDLINES", False, "tools/check-cited-lines.py missing at lands")
    bad, paths = [], []
    for e in entries:
        p = os.path.join(mat, e)
        if os.path.isfile(p):
            paths.append(p)
        else:
            bad.append("%s missing" % e)
    if not paths:
        return leg("CITEDLINES", False, "; ".join(dedupe(bad)))
    r = subprocess.run([sys.executable, "-B", tool] + paths,
                       capture_output=True, text=True)
    out = (r.stdout or "").strip()
    if r.returncode != 0:
        bad.append("tool exit=%d" % r.returncode)
    if "CITED-LINES: 0 finding(s)" not in (r.stdout or ""):
        last = out.splitlines()[-1] if out else "(no stdout)"
        bad.append("no zero-findings line over %d file(s): %s"
                   % (len(paths), last))
    detail = "files=%d" % len(paths)
    if out:
        detail += " last-line=%s" % out.splitlines()[-1]
    if bad:
        detail = "; ".join(dedupe(bad)) + " (" + detail + ")"
    return leg("CITEDLINES", not bad, detail[:300])


def leg_census(ctx):
    """CENSUS: sources-census.sh validate against the materialized registry
    exits 0 with no `^E[0-9][0-9]` line.

    Materialization: the registry is `<mat>/corpus/SOURCES.md` where `mat` is
    the git-archive tree of <lands> the counter built itself; `--file` makes
    the fleet script resolve every row's `used-by` path against the parent of
    `corpus/` — i.e. against the same graded tree — so no lane directory name
    and no fleet-root lane layout are needed (`--root` would have required
    symlinking <mat> under a lane name the fleet conf knows).  `--today` is the
    frozen access date, so the E08 open-date check is deterministic.
    """
    mat, cfg = ctx["mat"], ctx["cfg"]
    fleet_root = ctx["fleet_root"]
    script = os.path.join(fleet_root, "scripts/sources-census.sh")
    if not os.path.isfile(script):
        return leg("CENSUS", False, "census script not found: %s" % script)
    registry = os.path.join(mat, REGISTRY)
    if not os.path.isfile(registry):
        return leg("CENSUS", False, "registry missing at lands: %s" % REGISTRY)
    today = cfg.get("access_date")
    if not today:
        return leg("CENSUS", False,
                   "cfg carries no access_date; the census date is undeterminable")
    r = subprocess.run([script, "validate", "--file", registry, "--today", today],
                       capture_output=True, text=True)
    out = r.stdout or ""
    bad = []
    if r.returncode != 0:
        bad.append("census exit=%d" % r.returncode)
    ecodes = _ground_cited_census_ecodes(out)
    if ecodes:
        bad.append("census TSV carries E-code line(s): %s" % ",".join(ecodes))
    detail = "exit=%d" % r.returncode
    tail = out.strip().splitlines()[-1] if out.strip() else ""
    if tail:
        detail += " last-line=%s" % tail
    if bad:
        detail = "; ".join(dedupe(bad)) + " (" + detail + ")"
    return leg("CENSUS", not bad, detail[:300])

"""SCRATCHMIRROR and COLLCHECK — the two provenance legs of claim C.

Wording graded (reports/round-75/claims.json, claim C legs[], frozen text):

  SCRATCHMIRROR: `.ufo/waves/round-75/assimilation/validate-receipt.txt` shows
  `validate --file` exit 0 on a mirrored corpus carrying the frozen rows and
  entries, committed strictly before the registry-append commit.

  COLLCHECK: reg-ids/staged-ids/collisions files and guard-proof show a planted
  1-3-space-indented collision found and a 4-space one not found; no adopted lane
  id is in reg-ids; the map maps staged->lane by document for every adopted id.

Readings (ambiguities resolved here; see .ufo/waves/round-75/w2/
ExecLegMirrorColl.md for the full list and the positive/mutant table):

  R1  "committed strictly before the registry-append commit" is graded on the
      first-parent chain between the frozen claim base and <lands>: the append
      commit is the first chain commit whose REGISTRY blob holds the first
      frozen row id; the receipt commit is the chain commit that adds (or
      touches) the receipt.  A receipt added in the append commit, or touched
      after it, is not "before".  No per-path rev-list: a merge could carry a
      receipt commit that is not on the chain the L1 lands on.
  R2  "carrying the frozen rows and entries" is graded from the receipt's named
      ids/basenames — the receipt is a rehearsal record; the counter does not
      re-run census inside a leg (the CENSUS leg owns execution, and a leg that
      re-ran the mirror would grade an input, not the committed artefact).
  R3  The receipt must name EVERY frozen entry basename, the three-entry
      round-75 set included: a receipt regenerated from a two-entry mirror does
      not carry the frozen entries.
  R4  reg-ids is the PRE-APPEND registry id set (the claim's base registry):
      the leg re-derives it from the claim base with the 0-3-space row pattern
      and requires the landed file to equal that set.  "No adopted lane id is in
      reg-ids" is vacuous if reg-ids is any list at all, so the file's
      provenance is graded, not assumed.
  R5  collisions is re-derived as comm -12 of the two lists (set intersection):
      the file's only meaning is that intersection, and a stale or hand-edited
      collision list cannot support the guard claim.
  R6  A planted 1-3-space "collision" needs the planted id to be a STAGED id
      the registry does not hold (that is what makes it a collision) and the
      plant to be a real row in the committed proof bytes — so a proof that
      only asserts "found" in prose, or that plants an id outside the staged
      universe, does not pass.  Same for the 4-space control, both ways.
  R7  "maps staged->lane by document for every adopted id": for each adopted
      lane id the map must carry at least one staged record, must carry every
      staged id the frozen row_set names for that row, and every such record's
      url must name a document the landed row's source cell names (document
      identity via urls_compatible, which folds the persee page-level view onto
      its document and the %20 form onto the raw-space form).
"""


def _mirrorcoll_ids(value):
    """One row_set `staged` cell as a list of staged ids.

    Round 75 freezes a LIST per lane id (four staged rows collapse onto S885:
    "S876/S885/S917/S921"); a single-id row stays a bare string.
    """
    if isinstance(value, (list, tuple)):
        items = list(value)
    elif isinstance(value, str):
        items = re.split(r"[/,;\s]+", value)
    else:
        items = []
    out = []
    for item in items:
        v = str(item).strip().upper()
        if v and TOKEN_RE.fullmatch(v) and v not in out:
            out.append(v)
    return out


def _mirrorcoll_brief(ids, limit=6):
    """A bounded id list for a leg detail line (<= 300 chars, contract)."""
    ids = sorted(ids)
    head = ", ".join(ids[:limit])
    if len(ids) > limit:
        head += " (+%d more)" % (len(ids) - limit)
    return head or "-"


def _mirrorcoll_detail(bad, info):
    """The leg detail line: every reason that fits in 300 characters.

    The contract fixes the first detail line at <= 300 characters; a landing
    that breaks several clauses at once is summarised as the first three plus a
    count, never truncated mid-reason.
    """
    msgs = dedupe(bad)
    text = "; ".join(msgs[:3])
    if len(msgs) > 3:
        text += "; (+%d more)" % (len(msgs) - 3)
    room = 296 - len(info)
    if len(text) > room:
        text = text[:max(room - 4, 0)].rstrip() + "..."
    return ("%s; %s" % (text, info)) if text else info


def _mirrorcoll_text(root, rev, path):
    """`path` at `rev` as text, or None when the path is absent there."""
    r = git(root, "show", "%s:%s" % (rev, path))
    return r.stdout if r.returncode == 0 else None


def leg_scratch_mirror(ctx):
    """SCRATCHMIRROR: the `validate --file` receipt is committed on <lands>'
    first-parent chain strictly before the registry-append commit, shows exit 0,
    and carries the frozen adopted ids and entry basenames."""
    root, mat, cfg, lands = ctx["root"], ctx["mat"], ctx["cfg"], ctx["lands"]
    try:
        receipt = read_tree(mat, RECEIPT)
    except Missing:
        return leg("SCRATCHMIRROR", False, "receipt missing: %s" % RECEIPT)
    bad = []
    if re.search(r"(?s)validate.{0,200}--file|--file.{0,200}validate", receipt) is None:
        bad.append("receipt does not show `validate --file`")
    if re.search(r"(?i)\b(?:exit|rc)\s*[=:]?\s*0\b", receipt) is None:
        bad.append("receipt does not show exit 0")
    missing = [sid for sid in cfg["rows"]
               if not re.search(r"\b%s\b" % re.escape(sid), receipt)]
    if missing:
        bad.append("receipt does not carry %s" % _mirrorcoll_brief(missing))
    for e in cfg["entries"]:
        if os.path.basename(e) not in receipt:
            bad.append("receipt does not carry the entry %s" % os.path.basename(e))

    chain = git(root, "rev-list", "--first-parent", "--reverse",
                "%s..%s" % (cfg["base"], lands)).stdout.split()
    first = cfg["rows"][0] if cfg["rows"] else None
    receipt_revs, append_rev = [], None
    # seed from the claim base: only commits INSIDE base..<lands> can add the
    # receipt or the first row, so a pre-existing file is not misread as this
    # round's commit
    prev = _mirrorcoll_text(root, cfg["base"], RECEIPT)
    had_row = bool(first) and first in parse_rows(
        _mirrorcoll_text(root, cfg["base"], REGISTRY) or "")
    for i, rev in enumerate(chain):
        text = _mirrorcoll_text(root, rev, RECEIPT)
        if text is not None and text != prev:
            receipt_revs.append(i)
        prev = text
        if append_rev is None and first and not had_row:
            reg = _mirrorcoll_text(root, rev, REGISTRY)
            if reg is not None and first in parse_rows(reg):
                append_rev = i
    if had_row:
        bad.append("the %s row already exists at the claim base" % (first or "-"))
    elif append_rev is None:
        bad.append("no first-parent commit in base..<lands> adds the %s row"
                   % (first or "-"))
    if not receipt_revs:
        bad.append("receipt is not committed on the base..<lands> first-parent chain")
    elif append_rev is not None:
        if append_rev in receipt_revs:
            bad.append("receipt committed in the registry-append commit (not before)")
        elif max(receipt_revs) >= append_rev:
            bad.append("receipt touched after the registry-append commit")
    detail = "receipt@%s append@%s rows=%d entries=%d" % (
        ",".join(str(i) for i in receipt_revs) or "-",
        "-" if append_rev is None else str(append_rev),
        len(cfg["rows"]), len(cfg["entries"]))
    return leg("SCRATCHMIRROR", not bad, _mirrorcoll_detail(bad, detail))


def _guard_files(mat):
    """(rel, text) for every committed file under the guard-proof dir.

    The frozen wording names `guard-proof`; a landing that keeps the proof
    elsewhere under the assimilation tree is still graded, from committed bytes.
    """
    for base in (GUARD_DIR, ASSIM):
        if not os.path.isdir(os.path.join(mat, base)):
            continue
        out = []
        for rel in tree_files(mat, base):
            try:
                out.append((rel, read_tree(mat, rel)))
            except Missing:
                continue
        if out:
            return out
    return []


def _negated(line):
    return re.search(r"(?i)(\b(?:not|no|none|zero|missed|absent|never)\b|n't\b)", line)


def leg_collcheck(ctx):
    """COLLCHECK: the three id lists (re-derived where the wording allows),
    the indent guard proved both ways on committed fixture bytes, and the
    by-document map covering every adopted id."""
    mat, cfg = ctx["mat"], ctx["cfg"]
    bad = []
    variants = (("reg-ids", "staged-ids", "collisions"),
                ("collcheck-reg-ids.txt", "collcheck-staged-ids.txt",
                 "collcheck-collisions.txt"))
    dirs = (ASSIM, ASSIM + "/validate", ASSIM + "/mutations")
    found = None
    for d in dirs:
        for v in variants:
            if all(os.path.isfile(os.path.join(mat, d, f)) for f in v):
                found = (d, v)
                break
        if found:
            break
    if found is None:
        return leg("COLLCHECK", False,
                   "collision id files missing under %s" % ASSIM)
    d, v = found
    try:
        reg_ids = set(TOKEN_RE.findall(read_tree(mat, d + "/" + v[0])))
        staged_ids = set(TOKEN_RE.findall(read_tree(mat, d + "/" + v[1])))
        collide_ids = set(TOKEN_RE.findall(read_tree(mat, d + "/" + v[2])))
    except Missing as e:
        return leg("COLLCHECK", False, "collision id file unreadable: %s" % e)

    if not staged_ids:
        bad.append("staged-ids is empty")
    for sid in cfg["rows"]:
        if sid in reg_ids:
            bad.append("%s present in reg-ids (adopted id is not free)" % sid)
        if sid in collide_ids:
            bad.append("%s listed in collisions" % sid)
        for s in _mirrorcoll_ids(cfg["row_staged"].get(sid)):
            if s not in staged_ids:
                bad.append("staged id %s (-> %s) absent from staged-ids" % (s, sid))

    base_reg = None
    try:
        base_reg = read_tree(ctx["mat_base"], REGISTRY)
    except Missing:
        pass
    if base_reg is None:
        bad.append("claim-base registry unreadable (cannot re-derive reg-ids)")
        base_ids = set()
    else:
        base_ids = set(parse_rows(base_reg))
        if reg_ids != base_ids:
            bad.append("reg-ids is not the claim-base registry id set (file %d, "
                       "base %d; missing %s; extra %s)"
                       % (len(reg_ids), len(base_ids),
                          _mirrorcoll_brief(base_ids - reg_ids),
                          _mirrorcoll_brief(reg_ids - base_ids)))
    derived_coll = reg_ids & staged_ids
    if collide_ids != derived_coll:
        bad.append("collisions is not comm -12 of the id lists (file %d, derived "
                   "%d; missing %s; extra %s)"
                   % (len(collide_ids), len(derived_coll),
                      _mirrorcoll_brief(derived_coll - collide_ids),
                      _mirrorcoll_brief(collide_ids - derived_coll)))

    lands_rows = {}
    try:
        lands_rows = parse_rows(read_tree(mat, REGISTRY))
    except Missing:
        pass
    real_ids = (base_ids | set(lands_rows) | set(cfg["rows"]) | set(cfg["reused"]))
    guard_files = _guard_files(mat)
    positive = re.compile(r"(?i)collision|detect|present|found|fail|survived|killed"
                          r"|exit\s*[=:]?\s*1|sees[^\n]*\b1\b")
    negative = re.compile(r"(?i)(?:^|[^\d])0(?:[^\d]|$)|not\s+(?:found|seen|detected|"
                          r"matched)|no\s+collision|missed")
    indent_ok, four_ok = None, None
    for rel, text in guard_files:
        lines = [l for l in text.splitlines()
                 if not (ROW_RE.match(l) or INDENTED_ROW_RE.match(l)
                         or FOURSPACE_ROW_RE.match(l))]
        planted = [p for p in INDENTED_ROW_RE.findall(text)
                   if p not in real_ids and p in staged_ids]
        if planted and indent_ok is None:
            for pid in planted:
                hit = [l for l in lines
                       if pid in l and not _negated(l) and positive.search(l)]
                if hit:
                    indent_ok = (rel, pid, hit[0].strip()[:90])
                    break
        fours = [p for p in FOURSPACE_ROW_RE.findall(text)
                 if p not in real_ids and p in staged_ids]
        if four_ok is None:
            for pid in fours:
                hit = [l for l in lines
                       if (pid in l or re.search(r"(?i)4[- ]space|four[- ]space", l))
                       and _negated(l) and negative.search(l)]
                if hit:
                    four_ok = (rel, pid, hit[0].strip()[:90])
                    break
        if four_ok is None:
            # a control file may state the 4-space plant was not seen without
            # quoting the row itself
            hit = [l for l in lines
                   if re.search(r"(?i)4[- ]space|four[- ]space", l)
                   and _negated(l) and negative.search(l)]
            if hit:
                four_ok = (rel, None, hit[0].strip()[:90])
    if indent_ok is None:
        bad.append("no indent-guard proof under %s (a staged-id row planted at "
                   "1-3 spaces with a positive detection marker)" % GUARD_DIR)
    else:
        rel, pid, _line = indent_ok
        if re.search(r"^ {4,}\|\s*%s\s*\|" % pid, read_tree(mat, rel), re.M):
            bad.append("guard proof %s plants %s at 4+ spaces, not 1-3"
                       % (rel, pid))
    if four_ok is None:
        bad.append("no four-space control under %s (a staged-id row planted at "
                   "4 spaces with a not-found marker)" % GUARD_DIR)
    elif four_ok[1] is not None:
        rel, pid, _line = four_ok
        if pid in set(INDENTED_ROW_RE.findall(read_tree(mat, rel))):
            bad.append("four-space control %s plants %s inside the 1-3-space "
                       "grammar" % (rel, pid))

    recs = _map_records(ctx)
    if not recs:
        bad.append("no renumber-map records at the freeze (%s:%s)"
                   % (cfg["freeze"][:12], cfg["map_path"]))
    else:
        for sid in cfg["rows"]:
            olds = set(old for (old, new) in recs if new == sid)
            if not olds:
                bad.append("map records no staged->lane for %s" % sid)
                continue
            want = set(_mirrorcoll_ids(cfg["row_staged"].get(sid)))
            missing = want - olds
            if missing:
                bad.append("map does not map %s -> %s (the row_set stages those "
                           "ids on it)" % (_mirrorcoll_brief(missing), sid))
            row = lands_rows.get(sid)
            cells = row_cells(row) if row is not None else []
            row_urls = urls_in(cells[SOURCE]) if len(cells) > SOURCE else []
            for old in sorted(olds):
                url = recs[(old, sid)]
                if not url:
                    bad.append("map record %s -> %s carries no url" % (old, sid))
                elif row is None or not row_urls:
                    continue  # the ROWS leg owns a missing row / source cell
                elif not any(urls_compatible(url, u) for u in row_urls):
                    bad.append("map record %s -> %s names a document the row "
                               "does not: %s" % (old, sid, url[:60]))
    detail = "ids=%d staged=%d collisions=%d guard=%s/%s map=%d" % (
        len(reg_ids), len(staged_ids), len(collide_ids),
        "ok" if indent_ok else "missing", "ok" if four_ok else "missing",
        len(recs))
    return leg("COLLCHECK", not bad, _mirrorcoll_detail(bad, detail))

# leg-frozencfg.py — round-75 claim C, leg FROZENCFG (owner: ExecLegFrozenCfg).
# Part of the assembled reports/round-75/accept-c.py (CFG-CONTRACT.md order 3).
# Function definitions only; only PART A imports are used.
#
# Frozen leg text (reports/round-75/claims.json, claims[id=C].legs[11]) — the rule:
#   "FROZENCFG: row set, entry paths, fragments, reject counts and every constant
#    are read from `git show <freeze>:reports/round-75/claims.json`; the
#    by-document map is read from `git show <freeze>:<map.path>` whose sha256
#    equals map.sha256; never from the graded tree; <freeze> is an ancestor of
#    <lands> on its first-parent chain (<lands> == <freeze> is graded, not
#    refused); claims.json at <lands> is byte-identical to the freeze blob"
#
# Readings of the ambiguous parts (each marked at the check it governs):
#
# R1 "read from the freeze" is proved by re-derivation, not by assertion: every
#    constant in ctx["cfg"] is re-read from the frozen blob by this leg and
#    compared with the value the loader handed it.  Because the frozen bytes
#    also have to be the bytes at <lands> (below), a cfg built from the graded
#    tree cannot pass: an edited graded tree both breaks byte identity and
#    diverges from the frozen constants.
# R2 "<freeze> is an ancestor of <lands> on its first-parent chain" = membership
#    in `git rev-list --first-parent <lands>`.  A freeze reachable only through
#    a merge side branch FAILS with that reason (it is not merely "not an
#    ancestor").  <lands> == <freeze> is graded: the freeze is the first element
#    of its own first-parent chain, so the check passes and no special case is
#    needed.
# R3 "<lands> == <freeze> is graded, not refused" — this leg never raises for
#    that case; every byte comparison below degenerates to comparing the freeze
#    blob with itself, which is why the do-nothing control prints FROZENCFG
#    green while the data legs are red.
# R4 "claims.json at <lands> is byte-identical to the freeze blob" is a byte
#    comparison (not a hash comparison): two different byte strings that a
#    hash collision would map together are not "byte-identical".
# R5 "the counter's own sha256 equals sha256sum of the committed
#    reports/round-75/accept-c.py at <lands> when that path exists" (wave-2
#    dispatch, H1 self-pin): conditional on the path existing, so a landing
#    that never commits the counter is not failed by this limb; at
#    <lands> == <freeze> the limb reduces to "the bytes at the freeze are the
#    bytes of the counter that is grading", i.e. the freeze-pinned counter is
#    the one running.  The path is derived from PART A's ROUND, never
#    hardcoded.
# R6 ledger (claim Ca's pin, per the wave-2 dispatch): the ledger path is read
#    from the frozen config (the claim that declares a `ledger`), and its bytes
#    at <lands> must equal its bytes at <freeze>.  Claim Ca's own FROZENCFG leg
#    pins the same bytes, so this cannot fail a combined tree that grades green;
#    it is kept here because the ledger is part of the round's frozen constant
#    surface, and because a C grader run at a tree where the ledger was edited
#    must not report a frozen configuration.
# R7 "reject counts" — the frozen `counts` object is an INTEGER surface
#    (adopted, path_present, refused, total_staged_files).  Both sides are
#    reduced to their integer keys (key -> int), so int-vs-str rendering and a
#    prose sibling that lands inside the object are not tests, while a drifted
#    or dropped count is.  When the freeze declares no counts there is no
#    frozen referent, so no failure is raised (CFG-CONTRACT allows {}).
# R8 "row set ... every constant" — a frozen row set, entry list, fragment
#    list or term list that is EMPTY makes the data legs vacuous, so empty
#    frozen lists are a FROZENCFG failure (carried from the round-74 leg).
# R9 the map must be readable JSON as well as hash-pinned: an unparseable map
#    is not a by-document map that any leg could read (COLLCHECK owns its
#    records; this leg owns only that it is the frozen, readable blob).


def _frozencfg_ids(value):
    """Every S-id token carried by a frozen `staged`/prose value."""
    if value is None:
        return []
    if isinstance(value, (list, tuple)):
        text = " ".join(str(x) for x in value)
    elif isinstance(value, dict):
        text = " ".join(str(x) for x in value.values())
    else:
        text = str(value)
    return dedupe(TOKEN_RE.findall(text.upper()))


def _frozencfg_paths(value):
    """Repo-relative paths from a frozen `entries`-shaped value."""
    out = []

    def take(v):
        if isinstance(v, str):
            s = v.strip()
            if s:
                out.append(s[2:] if s.startswith("./") else s)
        elif isinstance(v, (list, tuple)):
            for item in v:
                take(item)
        elif isinstance(v, dict):
            for key in ("path", "paths", "entries", "amendments", "canonical",
                        "admitted"):
                if key in v:
                    take(v[key])

    take(value)
    return dedupe(out)


def _frozencfg_strings(value):
    """The frozen list of strings (paths, fragments, terms, file specs)."""
    if value is None:
        return []
    if isinstance(value, (list, tuple)):
        return [str(x).strip() for x in value]
    return [str(value).strip()]


def _frozencfg_counts(value):
    """A rejects.counts object as {key: int-string} (integer keys only).

    The frozen `counts` is an integer surface (adopted, path_present, refused,
    total_staged_files); a prose sibling that a later freeze puts *inside* the
    object (or a non-numeric value) is not a count the loader can carry, so it
    is dropped on both sides instead of being stringified into a false red.
    """
    if not isinstance(value, dict):
        return {}
    out = {}
    for k, v in value.items():
        try:
            out[str(k)] = str(int(v))
        except (TypeError, ValueError):
            continue
    return out


def _frozencfg_blob(root, rev, path):
    """The committed bytes of `path` at `rev`, or None when it is not there."""
    r = git_bytes(root, "show", "%s:%s" % (rev, path))
    if r.returncode != 0:
        return None
    return r.stdout


def _frozencfg_ledger_path(doc):
    """The ledger path the frozen round config pins (claim Ca declares it)."""
    for c in doc.get("claims") or []:
        if isinstance(c, dict):
            p = c.get("ledger")
            if isinstance(p, str) and p.strip():
                return p.strip()
    p = doc.get("ledger")
    return p.strip() if isinstance(p, str) and p.strip() else ""


def _frozencfg_rows(spec):
    """[(lane id, {staged ids})] from a frozen row_set/reused_rows list."""
    out = []
    for item in spec or []:
        if not isinstance(item, dict):
            continue
        rid = str(item.get("id", "")).strip().upper()
        out.append((rid, set(_frozencfg_ids(item.get("staged")))))
    return out


def _frozencfg_staged_map(value):
    """{lane id -> set(staged ids)} from the cfg row_staged/reused_staged dict."""
    out = {}
    if not isinstance(value, dict):
        return out
    for k, v in value.items():
        out[str(k).strip().upper()] = set(_frozencfg_ids(v))
    return out


def _frozencfg_compare(cfg, doc, claim, raw_text, bad):
    """R1: every cfg constant re-read from the frozen claims.json claims[C]."""
    note = bad.append

    # base: the top-level frozen base (a claim-local base is accepted as a
    # fallback exactly as the loader does).
    want_base = str(doc.get("base") or claim.get("base") or "").strip().lower()
    got_base = str(cfg.get("base") or "").strip().lower()
    if got_base != want_base:
        note("cfg base %s is not the frozen base %s"
             % (got_base[:12] or "-", want_base[:12] or "-"))

    # row set (order is part of the frozen constant) and the staged lists.
    rows = _frozencfg_rows(claim.get("row_set"))
    want_rows = [rid for rid, _staged in rows]
    got_rows = [str(x).strip().upper() for x in (cfg.get("rows") or [])]
    if got_rows != want_rows:
        note("cfg row set %s is not the frozen row set %s"
             % (" ".join(got_rows) or "-", " ".join(want_rows) or "-"))
    want_staged = {}
    for rid, staged in rows:
        want_staged.setdefault(rid, set()).update(staged)
    got_staged = _frozencfg_staged_map(cfg.get("row_staged"))
    if got_staged != want_staged:
        for rid in sorted(set(want_staged) | set(got_staged)):
            if got_staged.get(rid, set()) != want_staged.get(rid, set()):
                note("cfg staged ids for %s are %s, the frozen row declares %s"
                     % (rid, " ".join(sorted(got_staged.get(rid, set()))) or "-",
                        " ".join(sorted(want_staged.get(rid, set()))) or "-"))
    reused = _frozencfg_rows(claim.get("reused_rows"))
    want_reused = [rid for rid, _staged in reused]
    got_reused = [str(x).strip().upper() for x in (cfg.get("reused") or [])]
    if got_reused != want_reused:
        note("cfg reused rows %s are not the frozen reused_rows %s"
             % (" ".join(got_reused) or "-", " ".join(want_reused) or "-"))
    want_reused_staged = {}
    for rid, staged in reused:
        want_reused_staged.setdefault(rid, set()).update(staged)
    got_reused_staged = _frozencfg_staged_map(cfg.get("reused_staged"))
    if got_reused_staged != want_reused_staged:
        note("cfg reused_staged %s is not the frozen reused mapping %s"
             % (sorted(got_reused_staged) or "-", sorted(want_reused_staged) or "-"))

    # entry paths and the ground lists (sets: the freeze declares membership).
    want_entries = set(_frozencfg_paths(claim.get("entries")))
    got_entries = set(_frozencfg_paths(cfg.get("entries")))
    if got_entries != want_entries:
        note("cfg entry paths [%s] are not the frozen entry paths [%s]"
             % (", ".join(sorted(got_entries)) or "-",
                ", ".join(sorted(want_entries)) or "-"))
    ground = claim.get("ground") if isinstance(claim.get("ground"), dict) else {}
    want_frag = set(_frozencfg_strings(ground.get("fragments")))
    got_frag = set(_frozencfg_strings(cfg.get("fragments")))
    if got_frag != want_frag:
        note("cfg ground fragments [%s] are not the frozen fragments [%s]"
             % (", ".join(sorted(got_frag)) or "-",
                ", ".join(sorted(want_frag)) or "-"))
    terms_src = ground.get("terms")
    if terms_src is None:
        terms_src = ground.get("cjk_terms")
    want_terms = set(_frozencfg_strings(terms_src))
    got_terms = set(_frozencfg_strings(cfg.get("terms")))
    if got_terms != want_terms:
        note("cfg ground terms [%s] are not the frozen terms [%s]"
             % (", ".join(sorted(got_terms)) or "-",
                ", ".join(sorted(want_terms)) or "-"))

    # rejects: the refused staged ids, the refused file specs and (when the
    # freeze declares them, R7) the counts.
    rejects = claim.get("rejects") if isinstance(claim.get("rejects"), dict) else {}
    prose = rejects.get("refused_staged_not_appended")
    if prose is None:
        prose = rejects.get("refused_staged")
    prose_ids = set(_frozencfg_ids(prose))
    got_refused = set(_frozencfg_ids(cfg.get("refused_staged")))
    want_allowed = set(want_rows) | set(want_reused)
    if got_refused - prose_ids:
        note("cfg refused_staged %s names ids the frozen rejects prose does not"
             % " ".join(sorted(got_refused - prose_ids)))
    if prose_ids - got_refused - want_allowed:
        note("the frozen rejects prose refuses %s but cfg records %s"
             % (" ".join(sorted(prose_ids - got_refused - want_allowed)),
                " ".join(sorted(got_refused)) or "-"))
    files_src = rejects.get("refused_files_pending_triage")
    if files_src is None:
        files_src = rejects.get("refused_files")
    want_files = set(_frozencfg_strings(files_src))
    got_files = set(_frozencfg_strings(cfg.get("refused_files")))
    if got_files != want_files:
        note("cfg refused file specs [%s] are not the frozen [%s]"
             % ("; ".join(sorted(got_files)) or "-",
                "; ".join(sorted(want_files)) or "-"))
    if "counts" in rejects:
        want_counts = _frozencfg_counts(rejects.get("counts"))
        got_counts = _frozencfg_counts(cfg.get("counts"))
        if got_counts != want_counts:
            note("cfg reject counts %s are not the frozen counts %s"
                 % (sorted(got_counts.items()), sorted(want_counts.items())))

    # the by-document map path and its pin.
    map_spec = claim.get("map") if isinstance(claim.get("map"), dict) else {}
    want_map_path = str(map_spec.get("path") or "").strip()
    want_map_sha = str(map_spec.get("sha256") or "").strip().lower()
    got_map_path = str(cfg.get("map_path") or "").strip()
    got_map_sha = str(cfg.get("map_sha256") or "").strip().lower()
    if got_map_path != want_map_path:
        note("cfg map.path %r is not the frozen map.path %r"
             % (got_map_path, want_map_path))
    else:
        if not got_map_path or got_map_path.startswith("/") or \
                ".." in got_map_path.split("/"):
            note("the frozen map.path %r is not a relative repo path"
                 % got_map_path)
    if got_map_sha != want_map_sha:
        note("cfg map.sha256 %s is not the frozen map.sha256 %s"
             % (got_map_sha[:16] or "-", want_map_sha[:16] or "-"))
    elif not got_map_sha:
        note("the frozen map.sha256 is empty: the by-document map is "
             "uncheckable at this freeze")

    # the frozen leg list (its length and order are the leg-set contract).
    want_legs = [str(x).split(":", 1)[0].strip().upper()
                 for x in (claim.get("legs") or [])]
    got_legs = [str(x).strip().upper() for x in (cfg.get("frozen_legs") or [])]
    if got_legs != want_legs:
        note("cfg leg list %s is not the frozen leg list %s"
             % (" ".join(got_legs) or "-", " ".join(want_legs) or "-"))

    # the frozen claim's key set (claim_keys is a frozen constant surface) —
    # either the claim object's keys or the round document's keys, r74's
    # `sorted(claim.keys())` being the loader's declared shape.
    want_keys = sorted(str(k) for k in claim.keys())
    got_keys = [str(k) for k in (cfg.get("claim_keys") or [])]
    if got_keys != want_keys and got_keys != sorted(str(k) for k in doc.keys()):
        note("cfg claim_keys %s are not the frozen claim keys %s"
             % (" ".join(got_keys) or "-", " ".join(want_keys) or "-"))

    # row_doc / owned_inplace when the loader exposes them (CFG-CONTRACT cfg):
    # each document string must come from the frozen row_set document text, and
    # the owned_inplace list must be the frozen claim's list.
    row_doc = cfg.get("row_doc")
    if isinstance(row_doc, dict):
        for item in claim.get("row_set") or []:
            if not isinstance(item, dict):
                continue
            rid = str(item.get("id", "")).strip().upper()
            want_doc = str(item.get("document") or "")
            got_doc = str(row_doc.get(rid) or "").strip()
            if want_doc and (not got_doc or not want_doc.startswith(got_doc)):
                note("cfg row_doc[%s] %r is not the frozen document %r"
                     % (rid, got_doc[:60], want_doc[:60]))
    if "owned_inplace" in cfg:
        want_own = claim.get("owned_inplace") or []
        got_own = cfg.get("owned_inplace") or []
        if json.dumps(got_own, sort_keys=True) != json.dumps(want_own, sort_keys=True):
            note("cfg owned_inplace %r is not the frozen owned_inplace %r"
                 % (got_own, want_own))

    # the access date: declared at the freeze, or derived from frozen prose
    # (PART A docstring) — in which case it must occur in the frozen bytes.
    want_date = str(claim.get("access_date") or doc.get("access_date")
                    or "").strip()
    got_date = str(cfg.get("access_date") or "").strip()
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", got_date):
        note("cfg access_date %r is not a frozen YYYY-MM-DD date" % got_date)
    elif want_date and want_date != got_date:
        note("cfg access_date %s is not the frozen access_date %s"
             % (got_date, want_date))
    elif not want_date and got_date not in raw_text:
        note("cfg access_date %s does not occur in the frozen claims.json"
             % got_date)

    # the id namespace split derived from the frozen rows.
    allowed = set(str(x).strip().upper() for x in (cfg.get("allowed_ids") or []))
    if allowed != want_allowed:
        note("cfg allowed ids %s are not the frozen lane ids %s"
             % (" ".join(sorted(allowed)) or "-",
                " ".join(sorted(want_allowed)) or "-"))
    staged_all = set()
    for staged in want_staged.values():
        staged_all |= staged
    for staged in want_reused_staged.values():
        staged_all |= staged
    want_forbidden = sorted(staged_all - want_allowed)
    got_forbidden = sorted(str(x).strip().upper()
                           for x in (cfg.get("forbidden_ids") or []))
    if got_forbidden != want_forbidden:
        note("cfg forbidden ids %s are not the frozen staged ids %s"
             % (" ".join(got_forbidden) or "-",
                " ".join(want_forbidden) or "-"))

    # R8: empty frozen lists would make the data legs vacuous.
    if not want_rows:
        note("the frozen row set is empty")
    if not want_entries:
        note("the frozen entry list is empty")
    if not want_frag:
        note("the frozen ground fragments are empty")
    if not want_terms:
        note("the frozen ground terms are empty")


def _frozencfg_detail(bad, summary):
    """First detail line <= 300 characters; reasons first, then the summary."""
    if bad:
        head = str(bad[0])
        if len(head) > 300:
            head = head[:297] + "..."
        return "\n".join([head] + ["  - " + str(r) for r in bad[1:]] + summary)
    return "\n".join(summary)


def leg_frozencfg(ctx):
    """FROZENCFG: constants from the freeze blob only, map pinned by sha256,
    freeze on lands' first-parent chain, claims.json at lands frozen-identical."""
    root = ctx.get("root") or ""
    lands = str(ctx.get("lands") or "").strip().lower()
    cfg = ctx.get("cfg") or {}
    bad = []

    required = ("freeze", "frozen_sha256", "base", "access_date", "rows",
                "row_staged", "entries", "fragments", "terms",
                "refused_staged", "refused_files", "counts", "map_path",
                "map_sha256", "frozen_legs", "allowed_ids", "forbidden_ids",
                "claim_keys")
    for key in required:
        if key not in cfg:
            bad.append("cfg lacks the frozen constant %r (CFG-CONTRACT cfg)" % key)

    freeze = str(cfg.get("freeze") or "").strip().lower()
    hex40 = re.compile(r"[0-9a-f]{40}")
    if not hex40.fullmatch(freeze):
        bad.append("cfg freeze %r is not a 40-hex revision" % freeze)
    if not hex40.fullmatch(lands):
        bad.append("lands %r is not a 40-hex revision" % lands)
    valid = hex40.fullmatch(freeze) and hex40.fullmatch(lands)

    # R2: <freeze> on <lands>' first-parent chain.  R3: lands == freeze is
    # graded — the freeze heads its own first-parent chain, no special case.
    same_commit = bool(valid) and freeze == lands
    on_chain = False
    if valid:
        rev = git(root, "rev-list", "--first-parent", lands)
        if rev.returncode != 0:
            bad.append("cannot read lands' first-parent chain: %s"
                       % (rev.stderr or "").strip()[:120])
        else:
            chain = rev.stdout.split()
            on_chain = freeze in chain
            if not on_chain:
                if is_ancestor(root, freeze, lands):
                    bad.append("freeze %s is reachable from lands %s but not on "
                               "its first-parent chain (merge-side freeze)"
                               % (freeze[:12], lands[:12]))
                else:
                    bad.append("freeze %s is not an ancestor of lands %s"
                               % (freeze[:12], lands[:12]))

    # the frozen claims blob: the ONLY source of every constant.
    frozen_raw = None
    doc = None
    claims_state = "missing"
    if hex40.fullmatch(freeze):
        frozen_raw = _frozencfg_blob(root, freeze, CLAIMS)
        if frozen_raw is None:
            bad.append("cannot read %s at freeze %s" % (CLAIMS, freeze[:12]))
        else:
            sha = hashlib.sha256(frozen_raw).hexdigest()
            if sha != str(cfg.get("frozen_sha256") or "").strip().lower():
                bad.append("%s at freeze hashes to %s, cfg says %s"
                           % (CLAIMS, sha[:16],
                              str(cfg.get("frozen_sha256") or "-")[:16]))
            try:
                doc = json.loads(frozen_raw.decode("utf-8"))
            except (ValueError, UnicodeDecodeError) as exc:
                bad.append("%s at freeze is not readable JSON: %s"
                           % (CLAIMS, str(exc)[:120]))
            if not isinstance(doc, dict):
                bad.append("%s at freeze is not a JSON object" % CLAIMS)
                doc = None

    claim = None
    if doc is not None:
        for c in doc.get("claims") or []:
            if isinstance(c, dict) and str(c.get("id", "")).upper() == "C":
                claim = c
                break
        if claim is None:
            bad.append("%s at freeze carries no claim with id C" % CLAIMS)
        else:
            _frozencfg_compare(cfg, doc, claim, frozen_raw.decode("utf-8", "replace"),
                               bad)

    # R4: claims.json at <lands> is byte-identical to the freeze blob.
    if frozen_raw is not None and hex40.fullmatch(lands):
        lands_raw = _frozencfg_blob(root, lands, CLAIMS)
        if lands_raw is None:
            bad.append("%s is not committed at lands %s" % (CLAIMS, lands[:12]))
        elif lands_raw != frozen_raw:
            claims_state = "differs"
            bad.append("%s at lands %s differs from the freeze blob "
                       "(counter config edited in the graded tree)"
                       % (CLAIMS, lands[:12]))
        else:
            claims_state = "frozen-bytes"

    # the by-document map: pinned at the freeze, unchanged at lands (R9).
    map_path = str(cfg.get("map_path") or "").strip()
    map_sha = str(cfg.get("map_sha256") or "").strip().lower()
    map_state = "nocheck"
    frozen_map = None
    if hex40.fullmatch(freeze) and map_path:
        frozen_map = _frozencfg_blob(root, freeze, map_path)
        if frozen_map is None:
            map_state = "missing"
            bad.append("the by-document map %s is not committed at freeze %s"
                       % (map_path, freeze[:12]))
        else:
            sha = hashlib.sha256(frozen_map).hexdigest()
            map_state = "sha256-match"
            if map_sha:
                if sha != map_sha:
                    map_state = "sha256-drift"
                    bad.append("the map %s at freeze hashes to %s, the frozen "
                               "map.sha256 is %s"
                               % (map_path, sha[:16], map_sha[:16]))
            try:
                json.loads(frozen_map.decode("utf-8"))
            except (ValueError, UnicodeDecodeError) as exc:
                map_state += ",unparseable"
                bad.append("the map %s at freeze is not readable JSON: %s"
                           % (map_path, str(exc)[:120]))
            if hex40.fullmatch(lands):
                lands_map = _frozencfg_blob(root, lands, map_path)
                if lands_map is None:
                    map_state += ",lands-missing"
                    bad.append("the by-document map %s is not committed at "
                               "lands %s" % (map_path, lands[:12]))
                elif lands_map != frozen_map:
                    map_state += ",lands-differs"
                    bad.append("the map %s at lands %s differs from the freeze "
                               "blob" % (map_path, lands[:12]))

    # R6: the ledger pin (claim Ca's frozen path) — same bytes at lands.
    ledger_path = _frozencfg_ledger_path(doc) if isinstance(doc, dict) else ""
    ledger_state = "no-pin"
    if ledger_path and hex40.fullmatch(freeze) and hex40.fullmatch(lands):
        frozen_ledger = _frozencfg_blob(root, freeze, ledger_path)
        if frozen_ledger is None:
            ledger_state = "missing-at-freeze"
            bad.append("the frozen ledger %s is not committed at freeze %s"
                       % (ledger_path, freeze[:12]))
        else:
            lands_ledger = _frozencfg_blob(root, lands, ledger_path)
            if lands_ledger is None:
                ledger_state = "missing-at-lands"
                bad.append("the frozen ledger %s is not committed at lands %s"
                           % (ledger_path, lands[:12]))
            elif lands_ledger != frozen_ledger:
                ledger_state = "differs"
                bad.append("the ledger %s at lands %s differs from the freeze "
                           "blob" % (ledger_path, lands[:12]))
            else:
                ledger_state = "frozen-bytes"

    # R5: the counter's own sha256 against the committed counter at lands.
    counter_path = "reports/round-%d/accept-c.py" % ROUND
    counter_state = "absent"
    if hex40.fullmatch(lands):
        committed = _frozencfg_blob(root, lands, counter_path)
        if committed is not None:
            sha = hashlib.sha256(committed).hexdigest()
            mine = counter_sha256()
            if sha != mine:
                counter_state = "mismatch"
                bad.append("the counter's own sha256 %s is not %s's committed "
                           "%s (%s), so this run is not the frozen counter"
                           % (mine[:16], lands[:12], counter_path, sha[:16]))
            else:
                counter_state = "self-pinned"

    # the frozen claim base is a STRICT ancestor of lands (lands == base is the
    # counter's own refusal; an ancestor test that also accepted equality would
    # silently grade a tree that never landed anything).
    base = str(cfg.get("base") or "").strip().lower()
    if hex40.fullmatch(base) and hex40.fullmatch(lands):
        if not is_ancestor(root, base, lands):
            bad.append("the frozen claim base %s is not a strict ancestor of "
                       "lands %s" % (base[:12], lands[:12]))

    summary = [
        ("freeze %s: constants from git show %s:%s (sha256 %s); rows %s; "
         "entries %d; fragments %d; terms %d; refused %s; access %s"
         % (freeze[:12] or "-", freeze[:12] or "-", CLAIMS,
            str(cfg.get("frozen_sha256") or "-")[:16],
            " ".join(str(x) for x in (cfg.get("rows") or [])) or "-",
            len(cfg.get("entries") or []), len(cfg.get("fragments") or []),
            len(cfg.get("terms") or []),
            " ".join(str(x) for x in (cfg.get("refused_staged") or [])) or "-",
            cfg.get("access_date") or "-")),
        ("  lands %s: lands==freeze=%s first-parent-chain=%s claims@lands=%s "
         "map=%s(%s) ledger=%s counter=%s"
         % (lands[:12] or "-", "yes" if same_commit else "no",
            "yes" if on_chain else "no", claims_state,
            map_path or "-", map_state, ledger_state, counter_state)),
    ]
    return leg("FROZENCFG", not bad, _frozencfg_detail(bad, summary))

# ------------------------------------------------------------- leg: INDEX ---
# Claim C, leg 13 (INDEX), frozen text (reports/round-75/claims.json, claim C,
# legs[-1]; the SHONEN.md:6 clause was removed from this leg by the L1 before
# data, SHONEN.md being claim Ca's, so this leg never reads SHONEN.md):
#
#   corpus/README.md at <lands> has exactly one index row per adopted entry in
#   the myth-symbol section, each entry's own `- topic:` text verbatim under the
#   `- `name.md` — ` prefix, the myth-symbol heading equals the live partition
#   count (32), the last 'Counts checked' footer's total equals the live file
#   count with the per-directory vector 32/32/40/29/24/95; every base footer
#   block is preserved byte-identical and in order (the new footer is a new
#   appended block); README lines changed, removed or added outside {the three
#   adopted index rows, the myth-symbol heading, the appended footer block
#   (`Total knowledge entries: N.` and its `Counts checked` paragraph),
#   partition-heading lines whose only change is the count parenthetical
#   (claim Ca's), index rows naming a knowledge file that exists at base (claim
#   Ca's index-gap rows)} fail, and an added row-shaped `| S-id |` line fails.
#
# The SHONEN.md:6 clause was removed from this leg by the L1 before data
# (SHONEN.md is claim Ca's), so this leg never reads SHONEN.md.  Claim Ca lands
# BEFORE claim C, so the graded tree carries Ca's two partition-heading count
# repairs and its four index-gap rows; both are exempt, nothing else is.
#
# Readings where the wording is ambiguous (each stated in the w2 report):
#   R1 "live partition count" / "live file count" are counted from the graded
#      tree (mat), never from the README and never from the lane worktree.
#   R2 "exactly one index row per adopted entry in the myth-symbol section" is
#      read as the round-74 counter read the identical culture-material wording:
#      exactly one row for the basename anywhere in README, and that row inside
#      the myth-symbol section (r74 MutIndexLeg M8 killed a trailing-block
#      duplicate that way).
#   R3 "verbatim" compares the row body byte-for-byte against the entry's
#      `- topic:` value; the README-side body is not stripped, so a trailing
#      space on a row fails (r74 MutIndexLeg F2/M10 was the strip()-lenient
#      survivor).
#   R4 "older footers are byte-identical" = every base `Counts checked` block:
#      the base footer-block sequence must be a prefix of the lands one, which
#      also closes r74 MutIndexLeg F1 (the immediately-preceding live footer was
#      exempt under the old `[:-1]` loop).
#   R5 "the appended footer block" = the last `Counts checked` line of the
#      lands file, the paragraph that starts there (through its last non-blank
#      line), and the `Total knowledge entries: N.` line with the blank lines
#      that separate it from the previous paragraph.  A line appended outside
#      that block, an appended section heading or an extra prose paragraph,
#      fails.  (The base file's own footers are multi-line paragraphs that end
#      with prose, so the block's prose lines are part of it.)
#   R6 the per-directory vector is the six `## <part>/ (N)` partitions in README
#      section order; the last footer's vector must equal the frozen
#      (32, 32, 40, 29, 24, 95) AND the live per-partition .md counts, so the
#      footer states a true directory reading for the landed tree.
#   R7 the base README must embed, line by line and in order, into the lands
#      README: every base line survives verbatim (only partition-count heading
#      parentheticals may be replaced) and every lands line is either matched or
#      in the exemption set.  No diff algorithm is used, so repeated lines (the
#      footers repeat their closing lines; the file is full of blank lines)
#      cannot be matched against the wrong occurrence.


def _readme_sections(text):
    """[(partition, start, end)] char spans of the `## <part>/ (N)` sections."""
    marks = [(m.start(), m.group(1)) for m in README_SECTION_RE.finditer(text)]
    out = []
    for i, (pos, part) in enumerate(marks):
        end = marks[i + 1][0] if i + 1 < len(marks) else len(text)
        out.append((part, pos, end))
    return out


def _footer_blocks(text):
    """Paragraph blocks whose first line is a `Counts checked` footer."""
    blocks = []
    for block in re.split(r"\n[ \t]*\n", text):
        stripped = block.strip("\n")
        if stripped.startswith("Counts checked "):
            blocks.append(stripped)
    return blocks


def _entry_topic(mat, path):
    """The entry's own `- topic:` header value (first one, in the pre-body header)."""
    try:
        text = read_tree(mat, path)
    except Missing:
        return None
    for line in header_block(text):
        m = re.match(r"^[-*\s]*topic:\s*(.*)$", line)
        if m:
            value = m.group(1).strip()
            return value or None
    return None


def _md_count(mat, prefix):
    return len([p for p in tree_files(mat, prefix) if p.endswith(".md")])


def leg_index(ctx):
    """INDEX: one verbatim myth-symbol row per adopted entry, the heading equal
    to the live partition count, the last footer true to the landed tree with
    the frozen six-partition vector, every older footer byte-identical, and no
    README change outside the frozen exemption set."""
    mat, mat_base, cfg = ctx["mat"], ctx["mat_base"], ctx["cfg"]
    wanted_vec = (32, 32, 40, 29, 24, 95)      # frozen in the claim's leg text
    bad = []
    try:
        lands_text = read_tree(mat, README)
    except Missing:
        return leg("INDEX", False, "%s missing at lands" % README)
    try:
        base_text = read_tree(mat_base, README)
    except Missing:
        base_text = ""

    entries = list(cfg.get("entries") or [])
    names = [os.path.basename(e) for e in entries]
    lines = lands_text.splitlines()
    sections = _readme_sections(lands_text)
    parts = [p for p, _s, _e in sections]
    heading_counts = {}
    for h in README_SECTION_RE.finditer(lands_text):
        heading_counts[h.group(1)] = int(h.group(2))

    myth = [s for s in sections if s[0] == "myth-symbol"]
    if not myth:
        bad.append("%s has no `## myth-symbol/ (N)` section" % README)
        first = last = -1
    else:
        _p, myth_start, myth_end = myth[0]
        first = lands_text.count("\n", 0, myth_start)
        last = lands_text.count("\n", 0, myth_end)

    # R2/R3: one row per adopted entry, inside the myth-symbol section, body
    # equal to the entry's own `- topic:` value.
    for path, name in zip(entries, names):
        topic = _entry_topic(mat, path)
        if topic is None:
            bad.append("%s has no non-empty `- topic:` header line" % path)
        hits = []
        for k, line in enumerate(lines):
            m = README_ROW_RE.match(line)
            if m and m.group(1) == name:
                hits.append((k, m.group(2)))
        if len(hits) != 1:
            bad.append("%s has %d index rows in %s (want exactly one)"
                       % (name, len(hits), README))
            continue
        k, body = hits[0]
        if not 0 <= first <= k < last:
            bad.append("%s index row is not inside the myth-symbol section"
                       % name)
        if topic is not None and body != topic:
            bad.append("%s index row is not the entry's `- topic:` text verbatim"
                       % name)

    # R1: the myth-symbol heading equals the live count of that partition.
    live_parts = [_md_count(mat, KNOWLEDGE + "/" + part) for part in parts]
    if "myth-symbol" in heading_counts:
        live_myth = _md_count(mat, KNOWLEDGE + "/myth-symbol")
        if heading_counts["myth-symbol"] != live_myth:
            bad.append("myth-symbol heading (%d) != the %d live .md files in "
                       "corpus/knowledge/myth-symbol"
                       % (heading_counts["myth-symbol"], live_myth))

    # R1/R6: the last footer's total and six-partition vector.
    lands_blocks = _footer_blocks(lands_text)
    base_blocks = _footer_blocks(base_text)
    shown_total = shown_vec = "-"
    if not lands_blocks:
        bad.append("%s carries no `Counts checked` footer" % README)
    else:
        m = README_FOOTER_RE.search(lands_blocks[-1])
        if not m:
            bad.append("the last `Counts checked` footer carries no "
                       "(total N files; directory totals V) reading")
        else:
            total = int(m.group(1))
            vector = tuple(int(x) for x in m.group(2).split("/") if x)
            shown_total, shown_vec = str(total), m.group(2)
            live_total = _md_count(mat, KNOWLEDGE)
            if total != live_total:
                bad.append("last footer total %d != the %d .md files at lands"
                           % (total, live_total))
            if len(parts) != len(wanted_vec):
                bad.append("%s declares %d partition sections (want %d)"
                           % (README, len(parts), len(wanted_vec)))
            if vector != wanted_vec:
                bad.append("last footer vector %s != the frozen %s"
                           % ("/".join(str(v) for v in vector),
                              "/".join(str(v) for v in wanted_vec)))
            elif live_parts != list(wanted_vec):
                bad.append("the live partition counts %s differ from the frozen "
                           "vector %s"
                           % ("/".join(str(v) for v in live_parts),
                              "/".join(str(v) for v in wanted_vec)))

    # R4: every base footer (older than the new last one) byte-identical, in
    # order: the base block sequence is a prefix of the lands block sequence.
    for pos, blk in enumerate(base_blocks):
        if pos >= len(lands_blocks) or lands_blocks[pos] != blk:
            bad.append("an older `Counts checked` footer is not preserved "
                       "byte-identically: %r" % blk.splitlines()[0][:60])

    # R5 + the exemption set: base is embedded line by line, in order, into
    # lands.  Every base line must survive verbatim unless it is one of the
    # partition-count headings (whose parenthetical a landing may replace), and
    # every lands line must be matched unless it is in the exemption set.  The
    # walk is greedy and ordered, so a rewritten, moved or deleted line fails
    # and an inserted line outside the set fails.
    base_lines = base_text.splitlines()
    adopted = set(names)
    try:
        base_knowledge = set(os.path.basename(p)
                             for p in tree_files(mat_base, KNOWLEDGE))
    except OSError:
        base_knowledge = set()
    base_parts = set(m.group(1) for m in
                     (README_SECTION_RE.match(x) for x in base_lines) if m)
    lands_parts = set(m.group(1) for m in
                      (README_SECTION_RE.match(x) for x in lines) if m)
    exempt = set()
    if lands_blocks:
        cf = None
        for k, line in enumerate(lines):
            if line.startswith("Counts checked "):
                cf = k
        if cf is not None:
            hi = cf
            while hi + 1 < len(lines) and lines[hi + 1].strip():
                hi += 1
            lo = cf
            back = lo - 1
            if back >= 0 and not lines[back].strip():    # blank before Counts
                lo = back
                back -= 1
            if back >= 0 and lines[back].startswith("Total knowledge entries:"):
                lo = back
            if lo > 0 and not lines[lo - 1].strip():     # blank before the block
                lo -= 1
            exempt.update(range(lo, hi + 1))
    base_occ = Counter(base_lines)
    lands_occ = Counter(lines)
    for k, line in enumerate(lines):
        if lands_occ[line] <= base_occ.get(line, 0):
            continue                     # a line the base already carries
        if ROW_SHAPED_LINE_RE.match(line):
            bad.append("README line %d is a row-shaped registry line (this file "
                       "never asserts registry rows): %r" % (k + 1, line[:90]))
            continue
        rm = README_ROW_RE.match(line)
        if rm and rm.group(1) not in adopted and rm.group(1) not in base_knowledge:
            bad.append("README line %d adds an index row for %r, which is "
                       "neither a frozen adopted entry nor a knowledge file "
                       "existing at base" % (k + 1, rm.group(1)))
    for k, line in enumerate(lines):
        if lands_occ[line] <= base_occ.get(line, 0):
            continue                     # a line the base already carries
        m = README_SECTION_RE.match(line)
        if m and m.group(1) in base_parts:
            exempt.add(k)
            continue
        rm = README_ROW_RE.match(line)
        if rm and (rm.group(1) in adopted or rm.group(1) in base_knowledge):
            exempt.add(k)
    i = j = 0
    while i < len(base_lines) and j < len(lines):
        if base_lines[i] == lines[j]:
            i += 1
            j += 1
        elif j in exempt:
            j += 1
        else:
            m = README_SECTION_RE.match(base_lines[i])
            if m and m.group(1) in lands_parts:
                i += 1                   # count parenthetical replaced at lands
            else:
                bad.append("README line %d removed/edited outside the exemption "
                           "set: %r" % (i + 1, base_lines[i][:90]))
                i += 1
    while i < len(base_lines):
        m = README_SECTION_RE.match(base_lines[i])
        if not (m and m.group(1) in lands_parts):
            bad.append("README line %d removed/edited outside the exemption "
                       "set: %r" % (i + 1, base_lines[i][:90]))
        i += 1
    while j < len(lines):
        if j not in exempt:
            line = lines[j]
            rm = README_ROW_RE.match(line)
            if ROW_SHAPED_LINE_RE.match(line):
                bad.append("README line %d is a row-shaped registry line (this "
                           "file never asserts registry rows): %r"
                           % (j + 1, line[:90]))
            elif rm:
                bad.append("README line %d adds an index row for %r, which is "
                           "neither a frozen adopted entry nor a knowledge file "
                           "existing at base" % (j + 1, rm.group(1)))
            else:
                bad.append("README line %d added outside the exemption set: %r"
                           % (j + 1, line[:90]))
        j += 1

    detail = ("%s: %d section(s), myth-symbol=%s, last footer total=%s vector=%s, "
              "%d adopted row(s), %d base / %d lands line(s), %d exempt line(s)"
              % (README, len(parts), heading_counts.get("myth-symbol"),
                 shown_total, shown_vec, len(names), len(base_lines), len(lines),
                 len(exempt)))
    if bad:
        reasons = dedupe(bad)
        if len(reasons) > 4:
            reasons = reasons[:4] + ["(+%d more)" % (len(reasons) - 4)]
        detail = "; ".join(reasons) + " | " + detail
    return leg("INDEX", not bad, detail[:300])

# ---------------------------------------------- part-selftest-fixtures.py ---
# owner: ExecSelftestFixtures.  Function definitions only (the CFG-CONTRACT
# item 5 slot, concatenated before part-main.py's `__main__` guard): the
# fixture builder `build_fixture(prefix, mut=None)`, the named mutation table
# `MUTANTS`, the documented non-red survivors `SURVIVORS`, and `_sfx_`-prefixed
# private helpers.  `_selftest_scratch()` is also here: part-selftest-run.py
# calls it with no arguments to agree on one scratch root.  This part defines
# no `_run_counter` and no `run_selftest` (owner ExecSelftestMutants) and
# removes nothing: the runner owns every cleanup.
#
# WHAT IS BUILT
#   One throw-away git repository per call, three commits, in the
#   `$HYAKU_SCRATCH/kotodama-r75/<prefix>` scratch tree (never /tmp; the
#   operator default `/fast/scratch/hyaku/kotodama-r75` is used only when no
#   env var is set):
#     base    the 808-row fixture registry (S077..S884), the 249-file
#             knowledge tree (six partitions 32/29/40/29/24/95, every file
#             exactly 478 words so the frozen ENTRIES floor is the derived
#             floor too), corpus/README.md with two preserved footers,
#             tools/check-cited-lines.py (the lane's real linter), and the
#             standing quarantine verdicts;
#     freeze  reports/round-75/claims.json (claim C: 9 rows, 3 entries, the
#             40-file triage prose, 9 fragments + 2 terms, the map pin, the 13
#             frozen leg names), the hash-pinned by-document renumber map, the
#             scratch-mirror receipt, the three collision id files and the two
#             guard proofs;
#     lands   the nine registry rows S885..S893, the three myth-symbol entries,
#             the lesson (`## Gate` admit + reject tables, triage counts,
#             `## Quarantine`), nine evidence captures, the gap-sweep receipt,
#             the README index rows + myth-symbol heading + appended footer.
#   The positive lands satisfies all thirteen frozen legs at round-75 shape.
#   Every fixture is independent: distinct prefixes get distinct lane and fleet
#   directories, no ports, no module state, no fixed paths beyond the scratch
#   root.
#
# MUTANTS: `(name, expected_leg, spec)` 3-tuples; `spec` is a dict (or a
#   zero-arg callable returning one).  Each spec applies ONE named defect.
#   Some defects necessarily redden a second leg - a missing row takes its
#   evidence coupling with it - and the table names the PRIMARY leg (the leg
#   whose own clause the defect violates).  Two spec forms are special:
#   `{"no_data": True}` (a lands commit after the freeze with no claim-C
#   artefact) and `{"lands_is_freeze": True}` (the graded `lands == freeze`
#   control).
#
# SURVIVORS: junk landings the w1 vacuity critique (CritCCounterVacuity.md)
#   showed the FROZEN wording cannot refuse offline (fabricated page truth,
#   filler-only entry prose, a fabricated mirror receipt).  They are recorded,
#   not asserted red: a mutant whose expected leg could not go red would make
#   the selftest lie.  The structural half of each survivor IS a mutant.
#
# Round-74 provenance: `.ufo/waves/round-74/counters/accept-c.py` lines
# 1991-2835 (`_pad_to _evidence_text claims_fixture build_fixture` and the
# git helpers), reshaped for the round-75 leg set and the by-document map.
# No new imports (PART A's imports only); no network; stdlib only.

_SFX_ACCESS = "2026-10-27"
_SFX_UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
           "(KHTML, like Gecko) Chrome/130.0 Safari/537.36")
_SFX_CLAIMS = "reports/round-75/claims.json"
_SFX_REGISTRY = "corpus/SOURCES.md"
_SFX_LESSON = "corpus/lessons/round-75.md"
_SFX_EVIDENCE = "reports/round-75/evidence"
_SFX_README = "corpus/README.md"
_SFX_KNOWLEDGE = "corpus/knowledge"
_SFX_ASSIM = ".ufo/waves/round-75/assimilation"
_SFX_RECEIPT = _SFX_ASSIM + "/validate-receipt.txt"
_SFX_GROUND = "reports/round-75/telemetry/gap-sweep.txt"
_SFX_GUARD = _SFX_ASSIM + "/guard-proof"
_SFX_MAP = _SFX_ASSIM + "/id-renumber-map.json"
_SFX_CITED = "tools/check-cited-lines.py"
_SFX_VERDICTS = "reports/round-71/telemetry/quarantine-verdicts.md"

_SFX_BASE_FIRST = 77          # base rows S077..S884 = 808 rows, last id S884
_SFX_BASE_LAST = 884
_SFX_BASE_PARTITIONS = (("linguistics", 32), ("myth-symbol", 29),
                        ("culture-material", 40), ("synthesis", 29),
                        ("verification", 24), ("civilizations", 95))
_SFX_LANDS_MYTH = 32          # 29 base + the three adopted entries
_SFX_BASE_WORDS = 478         # the frozen ENTRIES floor, and the derived floor
_SFX_BODY_WORDS = 620         # every fixture entry body clears the floor

_SFX_U1113 = ("https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1113")
_SFX_U1120 = ("https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1120")
_SFX_U1114 = ("https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1114")
_SFX_UUCASS = "https://jw.ucass.edu.cn/kcdg/zyk/xwcb/xushixue.pdf"
_SFX_UJCSS = "https://www.jstage.jst.go.jp/article/jcss/25/2/25_200/_pdf"
_SFX_UJSIK = ("https://www.jstage.jst.go.jp/article/jsik/32/2/"
              "32_2022_017/_pdf")
_SFX_UUNIGE = ("https://www.unige.ch/lettres/framo/cernet/biblio/barth70.html")
_SFX_UUNIPA = ("https://iris.unipa.it/retrieve/e3ad891d-ad9f-da0e-"
               "e053-3705fe0a2b96/2014%20marrone%20age%20dor---2.pdf")
_SFX_UCW23 = ("https://www.chinawriter.com.cn/n1/2023/0922/"
              "c404024-40083104.html")

# (id, staged ids, document url, kind, tier, source-cell lead, scope,
#  located quote, teaches) - the round-75 row_set, one row per DOCUMENT.
_SFX_ROWS = (
    ("S885", ("S876", "S885", "S917", "S921"), _SFX_U1113, "paper", "A",
     "Roland Barthes, «Introduction à l'analyse structurale des récits», "
     "Communications 8 (1966), 1-27",
     "the article's own structural method, in the article's own words",
     "Innombrables sont les récits du monde.",
     "narrative described at several levels of description at once, and the "
     "hierarchy between those levels"),
    ("S886", ("S902",), _SFX_U1120, "paper", "A",
     "Tzvetan Todorov, «Les catégories du récit littéraire», Communications 8 "
     "(1966), 125-151",
     "a primary structuralist account of the categories of narrative",
     "Les catégories du récit littéraire",
     "temporal deformation as the feature that separates discourse from "
     "history"),
    ("S887", ("S904",), _SFX_U1114, "paper", "A",
     "A. J. Greimas, «Éléments pour une théorie de l'interprétation du récit "
     "mythique», Communications 8 (1966), 28-59",
     "the two isotopies of a mythic narrative",
     "Loin de se limiter à l'interprétation des énoncés, la théorie sémantique",
     "one message read twice, on the discursive plane and on the structural "
     "plane"),
    ("S888", ("S864",), _SFX_UUCASS, "docs", "B",
     "中国社会科学院大学 研究生院,《叙事学》课程大纲 (课程编号 102072020193)",
     "the Chinese-language narratology canon and course architecture",
     "故事是一种深层的抽象结构，必须通过话语呈现",
     "story as deep structure against discourse as its presentation"),
    ("S889", ("S865",), _SFX_UJCSS, "paper", "B",
     "小方 孝,「物語生成の物語論あるいはポストナラトロジー」, Cognitive Studies "
     "25(2), 200-217 (2018)",
     "a Japanese-language systematic theory of narrative generation",
     "a new research area called “narratology of narrative generation”",
     "narratives modelled as generated across layers and disciplines"),
    ("S890", ("S866",), _SFX_UJSIK, "paper", "B",
     "村井 源,「物語構造の階層的記述方式の提案」, 情報知識学会誌 32(2), 246-251 "
     "(2022)",
     "a machine-writable three-layer description format for narrative",
     "describe a story as a hierarchical structure consisting of three major "
     "layers",
     "ストーリー / クエスト / シーン as a writable three-layer spec"),
    ("S891", ("S905",), _SFX_UUNIGE, "paper", "B",
     "Roland Barthes, S/Z (Paris: Seuil, 1970), the five codes in the "
     "accessible excerpt",
     "the five codes of S/Z and their definitions",
     "les premières lexies suscitent l'établissement des cinq grands codes",
     "hermeneutic, semantic, symbolic, proairetic and gnomic codes as five "
     "simultaneous voices"),
    ("S892", ("S919",), _SFX_UUNIPA, "paper", "B",
     "Gianfranco Marrone, «L'âge d'or de la sémiotique littéraire», Signata 5 "
     "(2014), 57-72",
     "what the scholarly literature says about where the five codes come from",
     "Mais combien, et de quelle nature, sont ces codes ?",
     "the codes read as a received typology rather than a rule system"),
    ("S893", ("S870",), _SFX_UCW23, "community", "C",
     "三九音域「世界观是打开小说幻想屋的钥匙」, 中国作家网, 2023-09-22",
     "the native practitioner vocabulary of Chinese web-fiction world-building",
     "网络小说中的世界观，指的是故事设定中世间万物运转的方式，是故事发生的场景、规则",
     "世界观 as the rules by which a world's things operate (Tier C, "
     "lead-level only)"),
)

_SFX_LOCATORS = {
    "S885": "notice de l'article and the article's opening paragraph",
    "S886": "p. 125, the article's opening paragraph",
    "S887": "p. 29, the paragraph on the two isotopies",
    "S888": "课程教学计划「第二讲 故事：事件（一）」第 1 点",
    "S889": "PDF p. 1, the 解 説 abstract",
    "S890": "PDF p. 1, the 抄録 abstract",
    "S891": "the «S/Z» paragraph on the five great codes",
    "S892": "p. 58, the paragraph posing the question",
    "S893": "§世界观是打开小说幻想屋的钥匙, paragraph 1, sentence 2",
}

_SFX_ENTRY_A = (_SFX_KNOWLEDGE + "/myth-symbol/"
                "narrative-structure-frameworks.md")
_SFX_ENTRY_B = (_SFX_KNOWLEDGE + "/myth-symbol/"
                "narrative-structure-frameworks.amend-2026-10-23.md")
_SFX_ENTRY_C = (_SFX_KNOWLEDGE + "/myth-symbol/"
                "narrative-structure-frameworks.amend-2026-10-23b.md")
_SFX_ENTRIES = (_SFX_ENTRY_A, _SFX_ENTRY_B, _SFX_ENTRY_C)

_SFX_ENTRY_SPECS = (
    {"path": _SFX_ENTRY_A,
     "title": "Narrative structure frameworks — the Western anchor beside the "
              "Chinese and Japanese frames",
     "sources": ("S885", "S888", "S889", "S890", "S893"),
     "ground": "round 1's CANNOT-ANSWER — the narrative entry was sourced only "
               "from Chinese and Japanese theory, and the wave brief names the "
               "Western primary source as the question to close.",
     "topic": "narrative structure as a build order for an invented culture, "
              "from the Chinese, Japanese and Western structuralist sources "
              "side by side: the story/discourse split, the actantial model, "
              "the three time axes, the Japanese three-layer description "
              "format and the 1966 structuralist method of describing a "
              "narrative at several levels at once — a reference method for "
              "the myth-symbol partition, deciding no culture's story",
     "gap": "the lane held the four Western etic toolkits in "
            "`myth-symbol/comparative-frameworks.md` and held no file that "
            "governed narrative structure as such.",
     "couples": "`myth-symbol/comparative-frameworks.md` (the four mythic "
                "toolkits this entry does not repeat).",
     "scope": "a reference method for the myth-symbol partition; it decides no "
              "culture's story (lore-shokunin owns canon).",
     "heading": "The Western anchor beside the Chinese and Japanese frames",
     "beats": (
         "- **§1 The structuralist premise** — narrative as a formal object "
         "described at several levels at once rather than a genre surveyed "
         "(S885).",
         "- **§2 The Chinese frame** — 故事 as deep structure against 话语 as "
         "surface presentation, with the actantial model and the three time "
         "axes beside it (S888).",
         "- **§3 The Japanese frame** — a three-layer description format with "
         "its character sub-layer, and 起承転結 as a minimal completable unit "
         "rather than a four-beat plot (S890).",
         "- **§4 The generation side** — a systematic theory of how narratives "
         "are produced, not only how they are read (S889).",
         "- **§5 The practitioner register** — 世界观 as a rule-system, "
         "recorded as vocabulary and never as authority (S893).",
     )},
    {"path": _SFX_ENTRY_B,
     "title": "Amendment — a second and a mythic primary voice for narrative "
              "description",
     "sources": ("S885", "S886", "S887", "S891", "S892"),
     "ground": "round 3's CANNOT-ANSWER — the five codes could not be recovered "
               "from the transcription, so the Western anchor was one article "
               "read partly.",
     "topic": "the two 1966 Communications primary voices the notice-only "
              "anchor could not carry — Todorov on the categories of narrative "
              "and Greimas on the two isotopies of a mythic narrative — "
              "together with the five codes of S/Z and the scholarly statement "
              "of where those codes come from — an amendment correcting an "
              "attribution rather than re-teaching the codes",
     "gap": "the lane held Greimas's Sémantique structurale and the four etic "
            "toolkits, and held no primary source from the issue the Western "
            "structuralist canon was written in.",
     "couples": "`myth-symbol/hero-journey-variants.md` (Campbell's variants "
                "this amendment does not restate).",
     "scope": "an amendment to the narrative-structure entry; it adds primary "
              "sources and corrects an attribution.",
     "heading": "The dated addition",
     "beats": (
         "- **§N Narrative categories** — temporality as the decisive axis, "
         "with temporal deformation separating discourse from history (S886).",
         "- **§N+1 Two readings of a mythic narrative** — the message occupies "
         "two isotopies at once and the narrative is a single semantic "
         "structure to begin with (S887).",
         "- **§N+2 The levels of description** — the hierarchy of levels and "
         "the rule that no level produces sense alone (S885).",
         "- **§N+3 The five codes** — hermeneutic, semantic, symbolic, "
         "proairetic and gnomic as five simultaneous voices (S891).",
         "- **§N+4 Where the codes come from** — the scholarly statement of the "
         "typology's provenance, so the codes are not conflated with a rule "
         "system (S892).",
     )},
    {"path": _SFX_ENTRY_C,
     "title": "Amendment b — the mythic reading folded from the refused drafts",
     "sources": ("S885", "S887"),
     "ground": "round 4's CANNOT-ANSWER — the mythic reading was carried by two "
               "separate amendment drafts that were refused as separate paths.",
     "topic": "the mythic reading folded from the refused 23c and 24 amendment "
              "drafts into one admitted amendment path — Greimas's two "
              "isotopies beside Barthes's levels of description, with the "
              "folded material carried as prose here and never as a separate "
              "file path",
     "gap": "the refused drafts' material had no admitted path, so the mythic "
            "reading had no file of its own.",
     "couples": "`myth-symbol/narrative-structure-frameworks.amend-2026-10-23.md` "
                "(the amendment this one folds into).",
     "scope": "a folded amendment path; it adds no document the registry does "
              "not already hold.",
     "heading": "The folded reading",
     "beats": (
         "- **§F1 Why a fold** — two drafts were refused as separate paths, so "
         "their material lands here as prose and no separate file path is "
         "claimed (S887).",
         "- **§F2 The reading itself** — the mythic message read on the "
         "discursive plane and on the structural plane, set equivalent rather "
         "than ranked (S885).",
         "- **§F3 What the fold does not do** — it adds no new document, no new "
         "registry row and no new claim about mythic narrative.",
     )},
)

_SFX_PREFIX_HEAD = """\
# SOURCES — selftest fixture registry

| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
"""

_SFX_FILLER = ("fixture entry padding carries no claim about the lane and keeps "
               "the derived length floor stable").split()


# --------------------------------------------------------------- scratch ---

def _selftest_scratch():
    """The selftest scratch ROOT (`<HYAKU_SCRATCH>/kotodama-r75`).

    Honours $HYAKU_SCRATCH, then the older $SHOKUNIN_SCRATCH spelling, then
    the operator default `/fast/scratch/hyaku/kotodama-r75`, and only as a
    last resort the system temporary directory (never a hardcoded /tmp).
    """
    base = (os.environ.get("HYAKU_SCRATCH")
            or os.environ.get("SHOKUNIN_SCRATCH") or "").strip()
    if base:
        return os.path.join(os.path.abspath(base), "kotodama-r75")
    fast = "/fast/scratch/hyaku"
    if os.path.isdir(fast) and os.access(fast, os.W_OK):
        return os.path.join(fast, "kotodama-r75")
    return os.path.join(tempfile.gettempdir(), "kotodama-r75")


def _sfx_slug(text):
    return re.sub(r"[^A-Za-z0-9._-]+", "-", str(text)).strip("-") or "fixture"


# ----------------------------------------------------------- git helpers ---

def _sfx_git(lane, *args, **kw):
    env = dict(os.environ)
    when = kw.get("when")
    if when:
        env["GIT_AUTHOR_DATE"] = when
        env["GIT_COMMITTER_DATE"] = when
    return subprocess.run(["git", "-C", lane] + list(args),
                          capture_output=True, text=True, env=env)


def _sfx_write(root, rel, text):
    path = os.path.join(root, rel)
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)


def _sfx_read(root, rel):
    with open(os.path.join(root, rel), encoding="utf-8") as fh:
        return fh.read()


def _sfx_init(lane):
    r = _sfx_git(lane, "init", "-q")
    if r.returncode != 0:
        raise RuntimeError("git init failed in %s: %s" % (lane, r.stderr))
    top = _sfx_git(lane, "rev-parse", "--show-toplevel").stdout.strip()
    if os.path.realpath(top) != os.path.realpath(lane):
        raise RuntimeError("fixture toplevel %r is not %r" % (top, lane))


def _sfx_commit(lane, message, when):
    r = _sfx_git(lane, "add", "-A")
    if r.returncode != 0:
        raise RuntimeError("git add failed: %s" % r.stderr.strip())
    r = _sfx_git(lane, "-c", "user.name=selftest",
                 "-c", "user.email=selftest@fixture.invalid",
                 "commit", "-q", "-m", message, when=when)
    if r.returncode != 0:
        raise RuntimeError("git commit failed: %s" % r.stderr.strip())
    head = _sfx_git(lane, "rev-parse", "HEAD").stdout.strip()
    if not re.fullmatch(r"[0-9a-f]{40}", head):
        raise RuntimeError("fixture commit yielded no 40-hex revision")
    return head


# -------------------------------------------------------------- content ---

def _sfx_tokens(n, seed=0):
    out = []
    for i in range(n):
        out.append(_SFX_FILLER[(i + seed) % len(_SFX_FILLER)])
    return out


def _sfx_knowledge_text(name, words=_SFX_BASE_WORDS):
    """A base knowledge file of exactly `words` whitespace tokens.

    The header words count too, so the smallest base entry is exactly the
    frozen 478-word floor: the derived floor and the frozen floor agree and the
    ENTRIES leg prints no provenance note.
    """
    head = ["#", name]
    body = _sfx_tokens(max(0, words - len(head)))
    return " ".join(head + body) + "\n"


def _sfx_url_of(sid):
    for row in _SFX_ROWS:
        if row[0] == sid:
            return row[2]
    raise KeyError(sid)


def _sfx_usedby(sid, specs):
    return [spec["path"] for spec in specs if sid in spec["sources"]]


def _sfx_registry_row(row, specs, quotes, over=None):
    """One 11-cell registry row; `over` names the mutation's single defect."""
    over = over or {}
    sid, _staged, url, kind, tier, lead, scope, _quote, teaches = row
    quote = quotes.get(sid, row[7])
    anchor = "quote located: «%s»" % quote
    used = ", ".join(_sfx_usedby(sid, specs))
    opened = over.get("opened", _SFX_ACCESS)
    recheck = over.get("recheck", "180d")
    status = over.get("status", "mined")
    anchor = over.get("anchor", anchor)
    used = over.get("usedby", used)
    if over.get("drop_teaches"):
        return ("| %s | %s — %s | %s | %s | %s | %s | mined | %s | %s | %s |"
                % (sid, lead, url, kind, tier, scope, anchor, opened, recheck,
                   used))
    teaches = over.get("teaches", teaches)
    return ("| %s | %s — %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |"
            % (sid, lead, url, kind, tier, scope, anchor, teaches, status,
               opened, recheck, used))


def _sfx_base_registry(mut):
    lines = [_SFX_PREFIX_HEAD]
    for num in range(_SFX_BASE_FIRST, _SFX_BASE_LAST + 1):
        sid = "S%03d" % num
        url = "https://example.invalid/src/%03d" % num
        if mut.get("ground_fragment_at_base") and num == 500:
            url = _SFX_UUNIPA
        lines.append(
            "| %s | fixture source %03d — %s | docs | B | fixture scope %03d | "
            "fixture anchor %03d | fixture teaches %03d | queued | 2026-10-19 | "
            "180d | %s/linguistics/linguistics-fixture-01.md |\n"
            % (sid, num, url, num, num, num, _SFX_KNOWLEDGE))
    return "".join(lines)


def _sfx_base_knowledge(mut):
    out = {}
    for part, count in _SFX_BASE_PARTITIONS:
        for i in range(1, count + 1):
            name = "%s-fixture-%02d.md" % (part, i)
            out["%s/%s/%s" % (_SFX_KNOWLEDGE, part, name)] = \
                _sfx_knowledge_text(name)
    return out


def _sfx_readme_base():
    parts = []
    for part, count in _SFX_BASE_PARTITIONS:
        parts.append("## %s/ (%d)\n- `%s-fixture-01.md` — a fixture topic line\n"
                     % (part, count, part))
    return ("""\
# kotodama-shokunin corpus index

revision: 2.21 — fixture index for the round-75 selftest lane.

""" + "\n".join(parts) + """
Total knowledge entries: 246.

Counts checked 2026-10-25 from the repo root:
`find corpus/knowledge -type f -name '*.md' | wc -l`
(total 246 files; directory totals 32/29/40/29/24/92).

Total knowledge entries: 249.

Counts checked 2026-10-26 from the repo root:
`find corpus/knowledge -type f -name '*.md' | wc -l`
(total 249 files; directory totals 32/29/40/29/24/95).

""")


def _sfx_readme_lands(base_text, specs, mut):
    """The lands README: myth-symbol heading, three index rows, new footer.

    Every change is inside the frozen INDEX exemption set; `index_*` keys inject
    exactly one defect each.
    """
    myth_heading = "## myth-symbol/ (%d)" % (_SFX_LANDS_MYTH
                                             if not mut.get("index_heading_stale")
                                             else 29)
    rows = []
    for spec in specs:
        topic = spec["topic"]
        if mut.get("index_topic_mismatch") and spec["path"] == _SFX_ENTRY_B:
            topic = spec["topic"].replace("an amendment correcting", "a note "
                                          "on")
        rows.append("- `%s` — %s" % (os.path.basename(spec["path"]), topic))
    if mut.get("index_missing_row"):
        rows = rows[:-1]
    if mut.get("index_row_duplicated"):
        rows.append(rows[0])
    text = base_text.replace("## myth-symbol/ (29)", myth_heading, 1)
    block = "\n".join(rows) + "\n"
    if mut.get("index_row_outside_section"):
        # one row moves into the linguistics section: the only row that is
        # then not inside myth-symbol.
        moved = rows[-1]
        text = text.replace("## linguistics/ (32)\n",
                            "## linguistics/ (32)\n" + moved + "\n", 1)
        block = "\n".join(rows[:-1]) + "\n"
    text = text.replace(myth_heading + "\n", myth_heading + "\n" + block, 1)
    if mut.get("index_sid_row"):
        text = text.replace(myth_heading + "\n",
                            myth_heading + "\n| S885 | registry row |\n", 1)
    total = 251 if mut.get("index_footer_total") else 252
    vector = ("32/31/40/29/24/95" if mut.get("index_footer_vector")
              else "32/32/40/29/24/95")
    text += ("Total knowledge entries: %d.\n\n"
             "Counts checked %s from the repo root:\n"
             "`find corpus/knowledge -type f -name '*.md' | wc -l`\n"
             "(total %d files; directory totals %s).\n"
             % (total, _SFX_ACCESS, total, vector))
    if mut.get("index_older_footer_edited"):
        text = text.replace("(total 246 files; directory totals "
                            "32/29/40/29/24/92).",
                            "(total 246 files; directory totals "
                            "32/29/40/29/24/93).", 1)
    return text


def _sfx_entry_text(spec, mut):
    """One entry: nine-field provenance header, one `## ` section, long body."""
    path = spec["path"]
    lines = ["# " + spec["title"], ""]
    for sid in spec["sources"]:
        lines.append("source: %s — %s — %s — fetched %s"
                     % (sid, _sfx_url_of(sid), _SFX_LOCATORS[sid], _SFX_ACCESS))
    if mut.get("source_staged_id") and path == _SFX_ENTRY_A:
        lines = [line.replace("source: S893 — ", "source: S870 — ")
                 if line.startswith("source: S893 ") else line
                 for line in lines]
    if mut.get("source_url_mismatch") and path == _SFX_ENTRY_B:
        lines = [line.replace("source: S886 — %s" % _SFX_U1120,
                              "source: S886 — https://example.invalid/other")
                 if line.startswith("source: S886 ") else line
                 for line in lines]
    lines += [
        "verified-at: " + _SFX_ACCESS,
        "recheck: 180d — re-run each row's own recheck command; every row's "
        "cadence is 180d (ran %s)" % _SFX_ACCESS,
        "ground: " + spec["ground"],
        "- topic: " + spec["topic"],
        "- gap filled: " + spec["gap"],
        "- sources: the rows above, each opened this round with a located "
        "quote.",
        "- couples: " + spec["couples"],
        "- scope: " + spec["scope"],
        "",
        "## " + spec["heading"],
        "",
    ]
    beats = list(spec["beats"])
    if mut.get("inline_staged") and path == _SFX_ENTRY_C:
        beats.append("- **§F4 A stray staged id** — the refused campaign id "
                     "S864 stands here (a defect).")
    if mut.get("inline_base_row") and path == _SFX_ENTRY_A:
        beats.append("- **§6 A base row** — the unrelated lane row S500 stands "
                     "here (a defect).")
    if mut.get("citedlines_multi_id") and path == _SFX_ENTRY_A:
        beats.append("- **§7 Two ids on one line** — S885 and S888 both stand "
                     "here (a defect).")
    if mut.get("citedlines_table_id") and path == _SFX_ENTRY_A:
        beats.append("| S885 | a table row carrying an id (a defect) |")
    text = "\n".join(lines + beats)
    if mut.get("entry_stub") and path == _SFX_ENTRY_C:
        text = "\n".join(lines[:-1])
    if mut.get("entry_body_short") and path == _SFX_ENTRY_C:
        return _sfx_pad(text, 200)
    if mut.get("entry_header_placeholder") and path == _SFX_ENTRY_A:
        text = re.sub(r"(?m)^- scope:.*$", "- scope: TODO", text, count=1)
    if mut.get("entry_template_token") and path == _SFX_ENTRY_B:
        text = re.sub(r"(?m)^ground:.*$", "ground: <the gap>", text, count=1)
    return _sfx_pad_body(text, _SFX_BODY_WORDS)


def _sfx_pad(text, target):
    pad = ("The fixture body is padding only and exists to keep this entry "
           "comfortably above the length floor the counter reads from the "
           "frozen claim. ")
    while len(text.split()) < target:
        text += pad
    return text


def _sfx_pad_body(text, target):
    """Pad the SECTION BODY (everything from the first `## `) to `target` words.

    The ENTRIES leg counts only the body, so padding the whole file lets a long
    provenance header eat the body's length: pad where the gate looks.
    """
    idx = text.find("\n## ")
    if idx < 0:
        return text
    return text[:idx] + _sfx_pad(text[idx:], target)


def _sfx_window(quote, total, lead=560):
    head = " ".join(_sfx_tokens(4000, 5))[:lead]
    tail_len = max(0, total - len(head) - len(quote) - 2)
    tail = " ".join(_sfx_tokens(4200, 9))[:tail_len]
    return (head + " " + quote + " " + tail)[:total]


def _sfx_evidence_text(sid, url, quote, scope="excerpt", total=4200,
                       body_sha=None, window_sha=None, window_bytes=None,
                       status="200", ua=None, visible=None, access=None,
                       fetch_url=None, challenge="none", window=None):
    if window is None:
        window = _sfx_window(quote, total)
    payload = window.encode("utf-8")
    digest = window_sha or hashlib.sha256(payload).hexdigest()
    if visible is None:
        visible = len(window) + (900 if scope == "excerpt" else 0)
    ua = ua or _SFX_UA
    body_sha = body_sha or ("ab" * 32)
    if window_bytes is None:
        window_bytes = len(payload)
    return (
        "# evidence %s — claim C GATE (round 75 selftest fixture)\n"
        "url: %s\n"
        "ua: %s\n"
        "http: 200\n"
        "bytes: %d\n"
        "sha256: %s\n"
        "fetched: %sT10:00:00Z\n"
        "quote-found: yes\n"
        "quote-words: %d\n"
        "quote-chars: %d\n"
        "visible-chars: %s\n"
        "window-scope: %s\n"
        "window: chars=%d min=4096 pad=400 before=%d after=%d\n"
        "window-sha256: %s\n"
        "window-bytes: %d\n"
        "window-rule: sha256 of the single stored window line, UTF-8, no "
        "trailing newline\n"
        "quote-found-verbatim: yes\n"
        "challenge: %s\n"
        "challenge-detail: (none)\n"
        "content-type: text/html;charset=UTF-8\n"
        "final-url: %s\n"
        "extract: fixture text (synthetic; no network was used)\n"
        "fetch: GET %s\n"
        "user-agent: %s\n"
        "access-date: %s\n"
        "http-status: %s\n"
        "content-length: -\n"
        "transferred-bytes: %d\n"
        "fetch-attempts: 1\n"
        "locator: %s\n"
        "normalise: NFKC(per-character)+whitespace-fold; matched=verbatim\n"
        "quote: %s\n"
        "--- window ---\n"
        "%s\n"
        "--- quote ---\n"
        "%s\n"
        % (sid, url, ua, 12345, body_sha, _SFX_ACCESS, len(quote.split()),
           len(quote), visible, scope, len(window), 560, max(0, len(window) - 560),
           digest, window_bytes, challenge, url, fetch_url or url, ua,
           access or _SFX_ACCESS, status, 12345,
           _SFX_LOCATORS.get(sid, "fixture locator"), quote, window, quote))


def _sfx_evidence_files(specs, mut, quotes):
    """{path: text} for the nine adopted rows, one defect each when keyed."""
    out = {}
    for row in _SFX_ROWS:
        sid = row[0]
        if mut.get("evidence_missing") and sid == "S892":
            continue
        quote = quotes.get(sid, row[7])
        url = row[2]
        kwargs = {}
        scope = "excerpt"
        total = 4200
        if sid == "S885":
            # the one whole-document capture: 3720 visible chars < 4096.
            scope, total = "whole-document", 3720
        if mut.get("evidence_quote_absent") and sid == "S889":
            kwargs["window"] = _sfx_window("", total)
        if mut.get("window_sha_tamper") and sid == "S885":
            kwargs["window_sha"] = "0" * 64
        if mut.get("window_bytes_mismatch") and sid == "S890":
            kwargs["window_bytes"] = 17
        if mut.get("evidence_bad_ua") and sid == "S893":
            kwargs["ua"] = "curl/8.7.1"
        if mut.get("evidence_bad_status") and sid == "S891":
            kwargs["status"] = "403"
        if mut.get("evidence_bad_body_sha") and sid == "S886":
            kwargs["body_sha"] = "abc123"
        if mut.get("evidence_short_window") and sid == "S888":
            scope, total = "excerpt", 2000
        if mut.get("evidence_whole_4096") and sid == "S885":
            scope, total = "whole-document", 4200
            kwargs["visible"] = 4200
        if mut.get("evidence_visible_mismatch") and sid == "S886":
            scope, total = "whole-document", 3000
            kwargs["visible"] = 3005
        if mut.get("evidence_scope_unknown") and sid == "S892":
            scope = "full-page"
        if mut.get("evidence_fetch_other") and sid == "S892":
            kwargs["fetch_url"] = "https://example.invalid/other"
        text = _sfx_evidence_text(sid, url, quote, scope=scope, total=total,
                                  **kwargs)
        out["%s/%s.txt" % (_SFX_EVIDENCE, sid)] = text
    return out


def _sfx_lesson(specs, rows, mut, quotes):
    """The round-75 lesson: Gate admit + reject tables, triage, Quarantine."""
    admit = ["| source | access date | quote (<=25 words) | locator | evidence "
             "capture | verdict |",
             "|---|---|---|---|---|---|"]
    for row in rows:
        sid, _staged, url = row[0], row[1], row[2]
        quote = quotes.get(sid, row[7])
        date = _SFX_ACCESS
        cell_url = url
        locator = _SFX_LOCATORS[sid]
        if mut.get("gate_admit_date") and sid == "S890":
            date = "2026-10-26"
        if mut.get("gate_admit_locator") and sid == "S891":
            locator = "—"
        if mut.get("gate_admit_url") and sid == "S887":
            cell_url = "https://example.invalid/other"
        admit.append("| %s — %s | %s | \"%s\" | %s | %s/%s.txt (HTTP 200) | "
                     "admitted |"
                     % (sid, cell_url, date, quote, locator, _SFX_EVIDENCE, sid))
    reject = ["| item | reason | flip | probed URL | verdict |",
              "|---|---|---|---|---|",
              "| staged S870 quote | the staged quoted span is absent from the "
              "served page (a URL-quote mispairing) | re-open the document and "
              "quote afresh as lane S893 | %s | rejected |" % _SFX_UCW23]
    families = (
        ("naming-systems family (11)", "payload outside the declared "
         "narrative-structure theme", "a later round takes the naming-systems "
         "family", "probe/naming-systems"),
        ("calendar-festival-systems family (3)", "payload outside the declared "
         "theme", "a later round takes the calendar family",
         "probe/calendar-festival"),
        ("era-periodization-models family (2)", "payload outside the declared "
         "theme", "a later round takes the era family", "probe/era"),
        ("verification amendments (9)", "amendments with no admitted entry "
         "path", "a later round re-probes the amendments",
         "probe/verification"),
        ("conlang-scholarship amendments (3)", "the staged documents are "
         "already held by another leaf", "a later round re-probes them",
         "probe/conlang-scholarship"),
        ("conlang-methodology amendment (1)", "the staged document is already "
         "held by another leaf", "a later round re-probes it",
         "probe/conlang-methodology"),
        ("narrative-structure-frameworks amendment drafts (2)",
         "refused as separate paths; their material is folded into the "
         "admitted amendment", "no separate path is claimed again",
         "probe/narrative-amend"),
    )
    for label, why, flip, probe in families:
        line = ("| %s | %s | %s | https://example.invalid/%s | rejected |"
                % (label, why, flip, probe))
        if mut.get("rejects_family_renamed") and label.startswith("naming"):
            line = line.replace("naming-systems", "other-systems")
        reject.append(line)
    reject.append("| probe-only candidate | payload outside the declared "
                  "theme | a later round re-probes it | "
                  "https://example.invalid/probe/extra | rejected |")
    if mut.get("gate_reject_no_flip"):
        reject[-1] = reject[-1].replace("a later round re-probes it", "—")
    if mut.get("gate_reject_no_url"):
        reject[-1] = reject[-1].replace(
            "https://example.invalid/probe/extra", "the probed page")
    counts = ("Triage counts for the 40 staged knowledge files: 3 adopted / 6 "
              "path-present / 31 refused.")
    quarantine = """\
## Quarantine

The standing register verdicts (reports/round-71/telemetry/
quarantine-verdicts.md): 4 verdicts — PRESENT 1, REFUSED 2, UNVERIFIABLE 1.
The REFUSED register rows S816 and S817 stay refused; each document is
re-opened as new rows and no refused id is reused.

The narrative-structure staging refused no register row; the register records
are unchanged this round.
"""
    text = ("# Round 75 — narrative-structure-frameworks landing\n\n"
            "## Gate\n\n"
            "Admitted this round (every row opened %s by a plain request with "
            "the recorded browser-shaped UA):\n\n" % _SFX_ACCESS)
    text += "\n".join(admit) + "\n\n"
    text += ("Refused or not adopted from the assimilation set (reason + flip; "
             "every row names its probed URL):\n\n")
    text += "\n".join(reject) + "\n\n"
    if not mut.get("rejects_no_counts"):
        text += counts + "\n\n"
    if mut.get("rejects_no_s870"):
        text = text.replace("| staged S870 quote |", "| staged quote |")
    if mut.get("quarantine_missing"):
        quarantine = quarantine.replace("## Quarantine", "## Clearing notes")
    if mut.get("quarantine_no_refused"):
        quarantine = quarantine.replace(
            "The standing register verdicts (reports/round-71/telemetry/\n"
            "quarantine-verdicts.md): 4 verdicts — PRESENT 1, REFUSED 2, "
            "UNVERIFIABLE 1.\nThe REFUSED register rows S816 and S817 stay "
            "refused; each document is\nre-opened as new rows and no refused "
            "id is reused.\n\n", "")
    return text + quarantine


def _sfx_ground(mut):
    if mut.get("ground_missing"):
        return None
    lines = ["# round-75 gap sweep (selftest fixture)",
             "# stamp: %s 09:00:00 UTC" % _SFX_ACCESS,
             "gap-sweep at the %s-row registry (the claim base): 0 matches per "
             "fragment" % (817 if mut.get("ground_rows_wrong") else 808),
             "persee.fr/doc/comm_0588-8018_1966_num_8_1_1113: 0",
             "persee.fr/doc/comm_0588-8018_1966_num_8_1_1120: 0",
             "persee.fr/doc/comm_0588-8018_1966_num_8_1_1114: 0",
             "jw.ucass.edu.cn: 0",
             "jstage.jst.go.jp/article/jcss: 0",
             "jstage.jst.go.jp/article/jsik: 0",
             "unige.ch/lettres/framo: 0",
             "iris.unipa.it: 0",
             "chinawriter.com.cn/n1/2023/0922/c404024-40083104.html: 0",
             "narrative structure: 0",
             "narratology: 0"]
    if mut.get("ground_fragment_missing"):
        lines = [l for l in lines if not l.startswith("iris.unipa.it")]
    return "\n".join(lines) + "\n"


def _sfx_receipt(mut):
    if mut.get("receipt_missing"):
        return None
    flag = "validate" if mut.get("receipt_no_file_flag") else \
        "sources-census.sh validate --file"
    lines = ["# round-75 scratch-mirror validation receipt (selftest fixture)",
             "# stamp: %s 08:00:00 UTC" % _SFX_ACCESS,
             "$ %s <scratch>/mirror/corpus/SOURCES.md" % flag,
             "exit 1" if mut.get("receipt_no_exit") else "exit 0",
             "rows present in mirror: S885 S886 S887 S888 S889 S890 S891 S892 "
             "S893",
             "entries in mirror: %s" % ", ".join(_SFX_ENTRIES),
             "E-lines: 0"]
    if mut.get("receipt_missing_id"):
        lines = [l.replace("S888 ", "") if l.startswith("rows present") else l
                 for l in lines]
    return "\n".join(lines) + "\n"


def _sfx_guard_positive(mut):
    planted = "S884" if mut.get("coll_plant_real_id") else "S902"
    indent = "\t" if mut.get("coll_tab_plant") else "   "
    if mut.get("coll_lowercase_plant"):
        planted = "s902"
    return ("# 0-3-space-indent guard proof (selftest fixture)\n\n"
            "PLANTED at 1-3 spaces (staged id %s):\n"
            "%s| %s | planted indented row — https://example.invalid/planted | "
            "docs | B | s | §1 | planted | queued | %s | 90d | — |\n\n"
            "parser output: collision detected, the guard sees the plant: "
            "%s -> 1\nexit 1\n"
            % (planted, indent, planted, _SFX_ACCESS, planted))


def _sfx_guard_fourspace(mut):
    found = "4-space plant found: 1" if mut.get("coll_fourspace_found") else \
        "4-space plant: not found (0) — four or more spaces are indented code"
    return ("# four-space control (selftest fixture)\n\n"
            "4-space plant (staged id S904):\n"
            "    | S904 | four-space planted row | docs | B | s | §1 | planted "
            "| queued | %s | 90d | — |\n\n%s\n" % (_SFX_ACCESS, found))


def _sfx_map_text(mut):
    assignments = []
    for row in _SFX_ROWS:
        sid, staged, url = row[0], row[1], row[2]
        for old in staged:
            assignments.append({"staged_id": old, "new_lane_id": sid,
                                "url": url})
    mapping = {}
    for item in assignments:
        mapping[item["staged_id"]] = item["new_lane_id"]
    doc = {
        "round": 75,
        "status": "selftest fixture — the by-document renumber map",
        "join_key": "normalized document URL (host without www., path "
                    "percent-decoded, persee /doc/page/<slug>/… folded to "
                    "/doc/<slug>, web.archive.org wrapper stripped)",
        "assignments": assignments,
        "map": mapping,
    }
    return json.dumps(doc, indent=1, ensure_ascii=False, sort_keys=False) + "\n"


def _sfx_claims_text(base, map_sha, rows, specs, mut):
    staged_text = {}
    for row in rows:
        staged_text[row[0]] = "/".join(row[1])
    row_set = [{"id": row[0], "staged": staged_text[row[0]],
                "document": "%s (%s)" % (row[2], row[5])} for row in rows]
    rejects = {
        "refused_staged_not_appended": [
            "S870's staged quote (absent on page; source re-opened as S893 "
            "with a fresh quote)"],
        "refused_files_pending_triage": [
            "naming-systems x11",
            "calendar-festival-systems x3",
            "era-periodization-models x2",
            "verification amendments x9",
            "conlang-scholarship.amend-2026-10-23b/-23c/-2026-10-24 x3",
            "conlang-methodology.amend-2026-10-24",
            "narrative-structure-frameworks.amend-2026-10-23c and "
            "amend-2026-10-24 refused as separate paths; their Barthes "
            "material is folded into the admitted amend-2026-10-23b entry; no "
            "separate file path is claimed"],
        # the L1 ruling (claims.json edited pre-data): the lesson's triple and
        # the frozen counts must agree, and the three numbers sum to the total.
        "counts": {
            "adopted": 3,
            "path_present": 6,
            "refused": 31,
            "total_staged_files": 40,
        },
    }
    legs = ["%s: selftest fixture leg (access date %s)" % (name, _SFX_ACCESS)
            for name in ("ENTRIES", "ROWS", "REPOINTED", "GATE", "EVIDENCE",
                         "REJECTS", "GROUND", "CITEDLINES", "CENSUS",
                         "SCRATCHMIRROR", "COLLCHECK", "FROZENCFG", "INDEX")]
    claim = {
        "id": "C",
        "axis": "coverage",
        "kind": "assimilation-sourced",
        "title": "shokuknow assimilation: narrative-structure-frameworks "
                 "theme (selftest fixture)",
        "before": "the fixture base holds 808 rows (S077..S884) and 249 "
                  "knowledge files, and no narrative-named knowledge file.",
        "after": "the fixture lands adds rows S885..S893, three myth-symbol "
                 "entries, the lesson, the evidence captures and the receipts.",
        "row_set": row_set,
        "reused_rows": [],
        "entries": list(_SFX_ENTRIES),
        "rejects": rejects,
        "ground": {
            "fragments": [
                "persee.fr/doc/comm_0588-8018_1966_num_8_1_1113",
                "persee.fr/doc/comm_0588-8018_1966_num_8_1_1120",
                "persee.fr/doc/comm_0588-8018_1966_num_8_1_1114",
                "jw.ucass.edu.cn",
                "jstage.jst.go.jp/article/jcss",
                "jstage.jst.go.jp/article/jsik",
                "unige.ch/lettres/framo",
                "iris.unipa.it",
                "chinawriter.com.cn/n1/2023/0922/c404024-40083104.html"],
            "terms": ["narrative structure", "narratology"],
        },
        "map": {"path": _SFX_MAP,
                "sha256": "0" * 64 if mut.get("map_sha_mismatch") else map_sha},
        "legs": legs,
        "access_date": _SFX_ACCESS,
        "owned_inplace": [{"path": _SFX_README, "base_line": 1,
                           "base_text": "## myth-symbol/ (29)",
                           "after_text": "## myth-symbol/ (32)"}],
    }
    doc = {"round": 75,
           "status": "selftest fixture — NOT the frozen round-75 claims",
           "frozen": "selftest",
           "base": base,
           "claims": [claim]}
    return json.dumps(doc, indent=1, ensure_ascii=False) + "\n"


def _sfx_collision_files(mut):
    base_ids = ["S%03d" % n for n in range(_SFX_BASE_FIRST, _SFX_BASE_LAST + 1)]
    staged = []
    for row in _SFX_ROWS:
        for sid in row[1]:
            if sid not in staged:
                staged.append(sid)
    if mut.get("coll_staged_missing"):
        staged = [s for s in staged if s != "S921"]
    reg = list(base_ids)
    if mut.get("coll_adopted_in_regids"):
        reg.append("S885")
    collide = sorted(set(reg) & set(staged))
    if mut.get("coll_adopted_in_collisions"):
        collide.append("S890")
    return {"%s/reg-ids" % _SFX_ASSIM: "\n".join(reg) + "\n",
            "%s/staged-ids" % _SFX_ASSIM: "\n".join(staged) + "\n",
            "%s/collisions" % _SFX_ASSIM: "\n".join(collide) + "\n"}


_SFX_CENSUS_OK = ("#!/bin/sh\n"
                  "# selftest census stub (the counter only reads the TSV)\n"
                  "printf 'file\\tok\\tstub\\n'\n"
                  "exit 0\n")
_SFX_CENSUS_FAIL = ("#!/bin/sh\n"
                    "printf 'file\\tE06\\tS885 tier=Z\\n'\n"
                    "exit 1\n")


# ------------------------------------------------------------- builder ---

def build_fixture(prefix, mut=None):
    """A fresh three-commit fixture lane + its fleet root.

    Returns (lane, fleet, base, freeze, lands) as absolute paths/shas.  Every
    git call names the fixture (`git -C <lane>`), and the toplevel is asserted
    before the first commit.  The scratch directory `<root>/<prefix>` is this
    call's own and is recreated, never shared.
    """
    mut = dict(mut or {})
    root = os.path.join(_selftest_scratch(), _sfx_slug(prefix))
    shutil.rmtree(root, ignore_errors=True)
    lane = os.path.join(root, "lane")
    fleet = os.path.join(root, "fleet")
    os.makedirs(lane)
    os.makedirs(fleet)

    _sfx_write(fleet, "scripts/sources-census.sh",
               _SFX_CENSUS_FAIL if mut.get("census_fail") else _SFX_CENSUS_OK)
    os.chmod(os.path.join(fleet, "scripts/sources-census.sh"), 0o755)

    _sfx_init(lane)
    specs = [dict(s) for s in _SFX_ENTRY_SPECS]
    quotes = {}
    if mut.get("gate_quote_tokens"):
        # 26 single-letter whitespace tokens (51 characters): inside the
        # 80-character cap, over the 25-token cap.
        quotes["S890"] = " ".join("abcdefghijklmnopqrstuvwxyz"[i % 26]
                                  for i in range(26))
    if mut.get("gate_quote_chars"):
        # four 25-character tokens (103 characters): inside the token cap, over
        # the character cap.
        quotes["S886"] = " ".join(ch * 25 for ch in "ABCD")

    # ---- base ------------------------------------------------------------
    _sfx_write(lane, _SFX_REGISTRY, _sfx_base_registry(mut))
    for rel, text in _sfx_base_knowledge(mut).items():
        _sfx_write(lane, rel, text)
    _sfx_write(lane, _SFX_README, _sfx_readme_base())
    _sfx_write(lane, _SFX_VERDICTS,
               "# standing register verdicts (selftest fixture)\n\n"
               "| id | verdict |\n|---|---|\n"
               "| S816 | REFUSED |\n| S817 | REFUSED |\n"
               "| S820 | PRESENT |\n| S821 | UNVERIFIABLE |\n")
    _sfx_write(lane, _SFX_CITED, _sfx_citedlines_tool())
    if mut.get("entry_at_base"):
        _sfx_write(lane, _SFX_ENTRY_A,
                   _sfx_entry_text(specs[0], {}))
    base = _sfx_commit(lane, "base: fixture registry, knowledge tree, README",
                       "2026-10-27T09:00:00+00:00")

    # ---- freeze ----------------------------------------------------------
    map_text = _sfx_map_text(mut)
    map_sha = hashlib.sha256(map_text.encode("utf-8")).hexdigest()
    _sfx_write(lane, _SFX_MAP, map_text)
    _sfx_write(lane, _SFX_CLAIMS,
               _sfx_claims_text(base, map_sha, _SFX_ROWS, specs, mut))
    receipt = _sfx_receipt(mut)
    if receipt is not None and not mut.get("receipt_in_append"):
        _sfx_write(lane, _SFX_RECEIPT, receipt)
    for rel, text in _sfx_collision_files(mut).items():
        _sfx_write(lane, rel, text)
    _sfx_write(lane, _SFX_GUARD + "/guard-proof.txt", _sfx_guard_positive(mut))
    _sfx_write(lane, _SFX_GUARD + "/four-space-control.txt",
               _sfx_guard_fourspace(mut))
    freeze = _sfx_commit(
        lane, "freeze: claims.json, the by-document map, the mirror receipt, "
              "the collision files and the guard proofs",
        "2026-10-27T10:00:00+00:00")

    if mut.get("lands_is_freeze"):
        return lane, fleet, base, freeze, freeze

    # ---- lands -----------------------------------------------------------
    if mut.get("no_data"):
        _sfx_write(lane, _SFX_KNOWLEDGE + "/synthesis/scratch.md",
                   "# a scratch file that lands no claim-C artefact\n")
        lands = _sfx_commit(lane, "lands: no claim-C data (do-nothing control)",
                            "2026-10-27T11:00:00+00:00")
        return lane, fleet, base, freeze, lands

    registry = _sfx_base_registry(mut)
    extra = []
    for row in _SFX_ROWS:
        sid = row[0]
        if mut.get("row_missing_s890") and sid == "S890":
            continue
        over = {}
        if mut.get("row_staged_opened") and sid == "S886":
            over["opened"] = "2026-10-23"
        if mut.get("row_recheck_prose") and sid == "S887":
            over["recheck"] = "180d — re-read (ran %s)" % _SFX_ACCESS
        if mut.get("row_escaped_pipe") and sid == "S888":
            over["teaches"] = row[8] + " \\| planted"
        if mut.get("row_cell_count") and sid == "S893":
            over["drop_teaches"] = True
        if mut.get("row_status_queued") and sid == "S889":
            over["status"] = "queued"
        if mut.get("row_usedby_extra") and sid == "S892":
            over["usedby"] = ", ".join(_sfx_usedby(sid, specs) + [_SFX_ENTRY_A])
        if mut.get("row_usedby_missing") and sid == "S886":
            over["usedby"] = "—"
        if mut.get("row_anchor_no_quote") and sid == "S885":
            over["anchor"] = "page header"
        extra.append(_sfx_registry_row(row, specs, quotes, over))
    if mut.get("row_extra"):
        extra.append("| S894 | extra fixture row — https://example.invalid/extra "
                     "| docs | B | s | a | teaches extra | mined | %s | 180d | "
                     "%s |" % (_SFX_ACCESS, _SFX_ENTRY_A))
    registry = registry + "\n".join(extra) + "\n"
    if mut.get("row_removed_pre_existing"):
        registry = "\n".join(l for l in registry.splitlines()
                             if not l.startswith("| S500 |")) + "\n"
    if mut.get("row_pre_existing_edited"):
        registry = registry.replace("fixture teaches 500",
                                    "fixture teaches 500 (edited)", 1)
    _sfx_write(lane, _SFX_REGISTRY, registry)

    for spec in specs:
        if mut.get("entry_missing") and spec["path"] == _SFX_ENTRY_C:
            continue
        _sfx_write(lane, spec["path"], _sfx_entry_text(spec, mut))

    _sfx_write(lane, _SFX_LESSON, _sfx_lesson(specs, _SFX_ROWS, mut, quotes))
    ground = _sfx_ground(mut)
    if ground is not None:
        _sfx_write(lane, _SFX_GROUND, ground)
    for rel, text in _sfx_evidence_files(specs, mut, quotes).items():
        _sfx_write(lane, rel, text)
    _sfx_write(lane, _SFX_README, _sfx_readme_lands(
        _sfx_readme_base(), specs, mut))
    if mut.get("citedlines_tool_missing"):
        os.unlink(os.path.join(lane, _SFX_CITED))
    if mut.get("receipt_in_append") and receipt is not None:
        _sfx_write(lane, _SFX_RECEIPT, receipt)
    lands = _sfx_commit(
        lane, "lands: rows, entries, lesson, evidence, ground sweep, README",
        "2026-10-27T11:00:00+00:00")

    if mut.get("config_edited_at_lands"):
        text = _sfx_read(lane, _SFX_CLAIMS) + " "
        _sfx_write(lane, _SFX_CLAIMS, text)
        lands = _sfx_commit(lane, "lands: config edited after the freeze",
                            "2026-10-27T12:00:00+00:00")
    if mut.get("claims_missing_at_lands"):
        os.unlink(os.path.join(lane, _SFX_CLAIMS))
        lands = _sfx_commit(lane, "lands: claims.json removed",
                            "2026-10-27T12:00:00+00:00")
    return lane, fleet, base, freeze, lands


_SFX_CITED_TOOL = '''#!/usr/bin/env python3
"""Clause-scoping lint for cited lines (fixture copy).

A faithful reimplementation of the lane's tools/check-cited-lines.py contract
(round 61, claim O): per line, the distinct S-ids; MULTI-ID when a line carries
two or more, TABLE-ID when a line whose leading whitespace is stripped starts
with `|` and carries at least one.  The last stdout line is
`CITED-LINES: <k> finding(s) in <m> file(s)`; exit 1 when k > 0, 0 when k == 0.

Embedded in the fixture so the graded tool is the fixture's own bytes and does
not depend on where the assembled counter happens to live.
"""
import os
import re
import sys

SID = re.compile(r"\\bS\\d{3,}\\b")


def main(argv):
    paths = [a for a in argv if not a.startswith("-")]
    if not paths:
        sys.stderr.write("CITED_LINES_ERROR: no PATH given\\n")
        return 2
    findings = 0
    files = 0
    for path in paths:
        if os.path.isdir(path):
            todo = []
            for base, _dirs, names in os.walk(path):
                todo.extend(os.path.join(base, n) for n in sorted(names)
                            if n.endswith(".md"))
        elif os.path.isfile(path):
            todo = [path]
        else:
            sys.stderr.write("CITED_LINES_ERROR: cannot read %s\\n" % path)
            return 2
        for one in todo:
            try:
                with open(one, encoding="utf-8") as fh:
                    text = fh.read()
            except (OSError, UnicodeDecodeError) as exc:
                sys.stderr.write("CITED_LINES_ERROR: %s\\n" % exc)
                return 2
            files += 1
            for number, line in enumerate(text.splitlines(), 1):
                ids = sorted(set(SID.findall(line)), key=lambda t: int(t[1:]))
                if not ids:
                    continue
                kinds = []
                if len(ids) >= 2:
                    kinds.append("MULTI-ID")
                if line.lstrip().startswith("|"):
                    kinds.append("TABLE-ID")
                for kind in kinds:
                    findings += 1
                    print("%s %s:%d %s" % (kind, one, number, ",".join(ids)))
    print("CITED-LINES: %d finding(s) in %d file(s)" % (findings, files))
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
'''


def _sfx_citedlines_tool():
    """The fixture's clause-scoping linter (see `_SFX_CITED_TOOL`).

    The frozen CITEDLINES wording pins no tool blob, so the fixture ships its
    own faithful implementation rather than reaching for the lane's copy (an
    assembled counter in a scratch directory has no lane to read, and a stub
    would hide the multi-id mutants - the w1 vacuity finding).
    """
    return _SFX_CITED_TOOL


# --------------------------------------------------------------- table ---
#
# Coverage of the w1 junk paths (each mutant is the structural half of a named
# junk landing; the survivors that no offline counter can refuse are in
# SURVIVORS):
#
#   CritCCounterVacuity.md per-leg junk
#     ENTRIES    filler-only body         -> mutant `entry_stub`/`entry_body_short`
#                (the pure filler body is SURVIVOR `entry_filler_body`)
#     ROWS       normalized copied row    -> `row_staged_opened`,
#                                           `row_recheck_prose`, `row_usedby_*`
#     REPOINTED  id/URL-only compliance   -> `source_url_mismatch`,
#                                           `inline_base_row`
#     GATE       fabricated short quote   -> `gate_quote_tokens/_chars`;
#                (page truth is SURVIVOR `gate_fabricated_quote`)
#     EVIDENCE   fabricated window        -> `window_sha_tamper`,
#                (the window's truth is SURVIVOR `evidence_fabricated_window`)
#     REJECTS    global reason/flip words -> `rejects_family_renamed`,
#                                           `rejects_no_s870`
#     GROUND     fabricated sweep         -> `ground_fragment_missing`,
#                                           `ground_rows_wrong`,
#                                           `ground_fragment_at_base`
#     CITEDLINES stub tool printed zero   -> `citedlines_multi_id`,
#                                           `citedlines_table_id`
#     CENSUS     semantically false cells -> `census_fail` (E-code/exit)
#     SCRATCHMIRROR fabricated receipt    -> `receipt_missing`, `receipt_no_exit`,
#                (prose-only mirror is SURVIVOR `mirror_fabricated_receipt`)
#     COLLCHECK  fabricated marker        -> `coll_plant_real_id`,
#                                           `coll_fourspace_found`
#     FROZENCFG  graded-tree config edit  -> `config_edited_at_lands`
#     INDEX      ghost/wrong-topic row    -> `index_missing_row`,
#                                           `index_topic_mismatch`,
#                                           `index_row_duplicated`
#
#   MutRegistryCollision.md m1..m8 (8 cases)
#     m1  2-space plant found             POSITIVE control: the clean guard
#                                        proof is exactly this fixture
#     m2  3-space plant found             POSITIVE control (same proof)
#     m3  4-space NOT found               `coll_fourspace_found` (states found)
#     m4  column-zero plant               `coll_plant_real_id`-class: the plant
#                                        must be a staged id AND inside the
#                                        1-3-space grammar
#     m5  tab plant is silent             `coll_tab_plant`
#     m6  lowercase id missed by guard    `coll_lowercase_plant`
#     m7  4-digit id survives             SURVIVOR `guard_four_digit_id`
#     m8  adopted id in the collision set `coll_adopted_in_collisions`,
#                                        `coll_adopted_in_regids`
#
#   junk-fixtures.py claim-C cases
#     J1  header-only stub entry          `entry_stub`
#     J2  Gate quote absent from windows  `evidence_quote_absent`
#     J3  graded-tree claims.json shrink  `config_edited_at_lands`,
#                                        `claims_missing_at_lands`
#     J4x/J5-J10/G/R are claim Ca's and are not fixtures of this counter.

MUTANTS = (
    # ENTRIES
    ("entry_missing", "ENTRIES", {"entry_missing": True}),
    ("entry_stub", "ENTRIES", {"entry_stub": True}),
    ("entry_body_short", "ENTRIES", {"entry_body_short": True}),
    ("entry_header_placeholder", "ENTRIES",
     {"entry_header_placeholder": True}),
    ("entry_template_token", "ENTRIES", {"entry_template_token": True}),
    ("entry_at_base", "ENTRIES", {"entry_at_base": True}),
    # ROWS
    ("row_extra", "ROWS", {"row_extra": True}),
    ("row_removed_pre_existing", "ROWS", {"row_removed_pre_existing": True}),
    ("row_pre_existing_edited", "ROWS", {"row_pre_existing_edited": True}),
    ("row_staged_opened", "ROWS", {"row_staged_opened": True}),
    ("row_recheck_prose", "ROWS", {"row_recheck_prose": True}),
    ("row_escaped_pipe", "ROWS", {"row_escaped_pipe": True}),
    ("row_cell_count", "ROWS", {"row_cell_count": True}),
    ("row_status_queued", "ROWS", {"row_status_queued": True}),
    ("row_usedby_extra", "ROWS", {"row_usedby_extra": True}),
    ("row_usedby_missing", "ROWS", {"row_usedby_missing": True}),
    ("row_anchor_no_quote", "ROWS", {"row_anchor_no_quote": True}),
    ("row_missing_s890", "ROWS", {"row_missing_s890": True}),
    # REPOINTED
    ("source_url_mismatch", "REPOINTED", {"source_url_mismatch": True}),
    ("source_staged_id", "REPOINTED", {"source_staged_id": True}),
    ("inline_staged", "REPOINTED", {"inline_staged": True}),
    ("inline_base_row", "REPOINTED", {"inline_base_row": True}),
    # GATE
    ("gate_quote_tokens", "GATE", {"gate_quote_tokens": True}),
    ("gate_quote_chars", "GATE", {"gate_quote_chars": True}),
    ("gate_admit_date", "GATE", {"gate_admit_date": True}),
    ("gate_admit_locator", "GATE", {"gate_admit_locator": True}),
    ("gate_admit_url", "GATE", {"gate_admit_url": True}),
    ("gate_reject_no_flip", "GATE", {"gate_reject_no_flip": True}),
    ("gate_reject_no_url", "GATE", {"gate_reject_no_url": True}),
    # EVIDENCE
    ("evidence_missing", "EVIDENCE", {"evidence_missing": True}),
    ("evidence_quote_absent", "EVIDENCE", {"evidence_quote_absent": True}),
    ("window_sha_tamper", "EVIDENCE", {"window_sha_tamper": True}),
    ("window_bytes_mismatch", "EVIDENCE", {"window_bytes_mismatch": True}),
    ("evidence_bad_ua", "EVIDENCE", {"evidence_bad_ua": True}),
    ("evidence_bad_status", "EVIDENCE", {"evidence_bad_status": True}),
    ("evidence_bad_body_sha", "EVIDENCE", {"evidence_bad_body_sha": True}),
    ("evidence_short_window", "EVIDENCE", {"evidence_short_window": True}),
    ("evidence_whole_4096", "EVIDENCE", {"evidence_whole_4096": True}),
    ("evidence_visible_mismatch", "EVIDENCE",
     {"evidence_visible_mismatch": True}),
    ("evidence_scope_unknown", "EVIDENCE", {"evidence_scope_unknown": True}),
    ("evidence_fetch_other", "EVIDENCE", {"evidence_fetch_other": True}),
    # REJECTS
    ("rejects_no_s870", "REJECTS", {"rejects_no_s870": True}),
    ("rejects_no_counts", "REJECTS", {"rejects_no_counts": True}),
    ("rejects_family_renamed", "REJECTS", {"rejects_family_renamed": True}),
    ("quarantine_missing", "REJECTS", {"quarantine_missing": True}),
    ("quarantine_no_refused", "REJECTS", {"quarantine_no_refused": True}),
    # GROUND
    ("ground_missing", "GROUND", {"ground_missing": True}),
    ("ground_fragment_missing", "GROUND", {"ground_fragment_missing": True}),
    ("ground_rows_wrong", "GROUND", {"ground_rows_wrong": True}),
    ("ground_fragment_at_base", "GROUND", {"ground_fragment_at_base": True}),
    # CITEDLINES
    ("citedlines_multi_id", "CITEDLINES", {"citedlines_multi_id": True}),
    ("citedlines_table_id", "CITEDLINES", {"citedlines_table_id": True}),
    ("citedlines_tool_missing", "CITEDLINES", {"citedlines_tool_missing": True}),
    # CENSUS
    ("census_fail", "CENSUS", {"census_fail": True}),
    # SCRATCHMIRROR
    ("receipt_missing", "SCRATCHMIRROR", {"receipt_missing": True}),
    ("receipt_no_exit", "SCRATCHMIRROR", {"receipt_no_exit": True}),
    ("receipt_missing_id", "SCRATCHMIRROR", {"receipt_missing_id": True}),
    ("receipt_in_append", "SCRATCHMIRROR", {"receipt_in_append": True}),
    ("receipt_no_file_flag", "SCRATCHMIRROR", {"receipt_no_file_flag": True}),
    # COLLCHECK
    ("coll_adopted_in_regids", "COLLCHECK", {"coll_adopted_in_regids": True}),
    ("coll_adopted_in_collisions", "COLLCHECK",
     {"coll_adopted_in_collisions": True}),
    ("coll_fourspace_found", "COLLCHECK", {"coll_fourspace_found": True}),
    ("coll_plant_real_id", "COLLCHECK", {"coll_plant_real_id": True}),
    ("coll_tab_plant", "COLLCHECK", {"coll_tab_plant": True}),
    ("coll_lowercase_plant", "COLLCHECK", {"coll_lowercase_plant": True}),
    ("coll_staged_missing", "COLLCHECK", {"coll_staged_missing": True}),
    # FROZENCFG
    ("config_edited_at_lands", "FROZENCFG", {"config_edited_at_lands": True}),
    ("claims_missing_at_lands", "FROZENCFG", {"claims_missing_at_lands": True}),
    ("map_sha_mismatch", "FROZENCFG", {"map_sha_mismatch": True}),
    # INDEX
    ("index_missing_row", "INDEX", {"index_missing_row": True}),
    ("index_topic_mismatch", "INDEX", {"index_topic_mismatch": True}),
    ("index_heading_stale", "INDEX", {"index_heading_stale": True}),
    ("index_footer_total", "INDEX", {"index_footer_total": True}),
    ("index_footer_vector", "INDEX", {"index_footer_vector": True}),
    ("index_older_footer_edited", "INDEX", {"index_older_footer_edited": True}),
    ("index_row_outside_section", "INDEX", {"index_row_outside_section": True}),
    ("index_row_duplicated", "INDEX", {"index_row_duplicated": True}),
    ("index_sid_row", "INDEX", {"index_sid_row": True}),
)

# Junk landings the FROZEN wording cannot refuse offline (w1
# CritCCounterVacuity.md): recorded, never asserted red.  Each survivor's
# structural half is one of the MUTANTS above (`entry_stub` for F7's shape,
# `window_sha_tamper` for F4's digest, `receipt_no_exit` for F2's prose).
SURVIVORS = (
    ("entry_filler_body", "ENTRIES",
     "a >=478-word filler body with a valid header is explicitly a "
     "length-and-shape gate (CritCCounterVacuity F7)"),
    ("gate_fabricated_quote", "GATE",
     "a plausible quote on a page nobody re-opened cannot be falsified by a "
     "committed-bytes counter (F5/F14); the routed ordinary re-open owns it"),
    ("evidence_fabricated_window", "EVIDENCE",
     "a fabricated window with a correct digest authenticates stored bytes, "
     "not a fetch (F4); the body sha256 is shape-graded"),
    ("mirror_fabricated_receipt", "SCRATCHMIRROR",
     "a receipt naming a mirror that never ran is prose-only evidence (F2); "
     "CENSUS owns the executed census"),
    ("guard_fabricated_marker", "COLLCHECK",
     "the guard is pattern-matched, not executed (F3); the planted id must at "
     "least be a staged id"),
    ("guard_four_digit_id", "COLLCHECK",
     "a 4-digit id (S1005) planted at 1-3 spaces is seen by the guard and, "
     "with no staged counterpart, collides with nothing (MutRegistryCollision "
     "m7/F3); the fixture's plant is a staged 3-digit id instead"),
    ("citedlines_stub_tool", "CITEDLINES",
     "the frozen wording pins no tool blob, so a stub printing the line "
     "passes (F1); this fixture ships the real tool instead"),
    ("ground_fabricated_receipt", "GROUND",
     "a syntactically matching sweep receipt is not provable offline (F8); "
     "the independent base re-derivation is what bites"),
)

# --------------------------------------------------------------------------
# selftest -- runner half (owner: ExecSelftestMutants)
#
# Every case builds a fixture repo (part-selftest-fixtures.py), runs THIS
# counter as a subprocess against it, and asserts the exact verdict shape the
# claim needs: the positive tree PASSes 13/13, every mutant is caught on its
# named leg, `lands == base` is REFUSED with a FAIL line, `lands == freeze` is
# GRADED (FROZENCFG green, data legs red), and a missing --lands/--freeze is
# an input error (exit 2).
#
# Scratch (fixtures, the counter's own grading clone via TMPDIR, and this
# runner) lives under $HYAKU_SCRATCH/kotodama-r75 (never /tmp) and is removed
# on exit.  $SHOKUNIN_SCRATCH is honoured as the older spelling the PART A
# docstring still carries; /fast/scratch/hyaku is the operator default.
# --------------------------------------------------------------------------

_STR_LEG_ORDER = ("ENTRIES", "ROWS", "REPOINTED", "GATE", "EVIDENCE",
                  "REJECTS", "GROUND", "CITEDLINES", "CENSUS",
                  "SCRATCHMIRROR", "COLLCHECK", "FROZENCFG", "INDEX")
_STR_TIMEOUT = 600


def _str_scratch():
    """The selftest scratch root: the fixture builder's own root when it is
    present (so both halves agree on one tree), else the env/default chain."""
    helper = globals().get("_selftest_scratch")
    if callable(helper):
        try:
            root = helper()
        except Exception:
            root = None
        if root:
            return root
    base = (os.environ.get("HYAKU_SCRATCH")
            or os.environ.get("SHOKUNIN_SCRATCH")
            or "")
    if base:
        return os.path.join(base, "kotodama-r75")
    fast = "/fast/scratch/hyaku"
    if os.path.isdir(fast) and os.access(fast, os.W_OK):
        return os.path.join(fast, "kotodama-r75")
    return os.path.join(tempfile.gettempdir(), "kotodama-r75")


def _str_tmpdir():
    """This run's own temporary directory inside the scratch root (QUALITY 14:
    never /tmp).  Named by pid so two selftests can run side by side and the
    cleanup can never touch a seat directory or another run's files.  The
    caller creates it; the cleanup only ever removes this exact path."""
    return os.path.join(_str_scratch(), "selftest-tmp-%d" % os.getpid())


def _str_slug(text):
    return re.sub(r"[^A-Za-z0-9._-]+", "-", str(text)).strip("-") or "mutant"


def _str_mutants():
    """MUTANTS normalised to [(name, expected_leg, spec_or_callable), ...].

    The frozen shape is the fixture builder's list of 3-tuples; a mapping
    (r74 shape, with EXPECTED_FAIL beside it) is accepted as well so an
    assembly order mistake cannot silently skip every mutant.
    """
    table = globals().get("MUTANTS")
    if table is None:
        return []
    if isinstance(table, dict):
        expected = globals().get("EXPECTED_FAIL") or {}
        items = [(name, expected.get(name, ""), spec)
                 for name, spec in table.items()]
    else:
        items = list(table)
    rows = []
    for item in items:
        try:
            name, leg, spec = item
        except (TypeError, ValueError):
            rows.append((item, "", None))
            continue
        rows.append((name, leg, spec))
    return rows


def _run_counter(lane, fleet, lands, freeze=None, extra=None, omit_lands=False):
    """Run the assembled counter as a subprocess against one fixture.

    TMPDIR points into the selftest scratch so the counter's own grading clone
    and the fixtures' temp dirs never land in /tmp.  A hang is reported as
    exit 124 rather than killing the whole selftest.
    """
    cmd = [sys.executable, "-B", os.path.abspath(__file__),
           "--root", lane, "--fleet-root", fleet]
    if not omit_lands:
        cmd += ["--lands", lands]
    if freeze:
        cmd += ["--freeze", freeze]
    if extra:
        cmd += list(extra)
    tmp = _str_tmpdir()
    os.makedirs(tmp, exist_ok=True)
    env = dict(os.environ)
    env.setdefault("PYTHONHASHSEED", "0")
    env["TMPDIR"] = tmp
    env.pop("TMP", None)
    env.pop("TEMP", None)
    try:
        return subprocess.run(cmd, capture_output=True, text=True, env=env,
                              cwd=tmp, timeout=_STR_TIMEOUT)
    except subprocess.TimeoutExpired as e:
        out = e.stdout if isinstance(e.stdout, str) else (e.stdout or b"").decode(
            "utf-8", "replace")
        err = e.stderr if isinstance(e.stderr, str) else (e.stderr or b"").decode(
            "utf-8", "replace")
        return subprocess.CompletedProcess(
            cmd, 124, out, err + "\nTIMEOUT after %ds" % _STR_TIMEOUT)


def run_selftest():
    results = []
    dirs = []

    def emit(name, problems, note=""):
        ok = not problems
        detail = note if ok else " | ".join(p.strip() for p in problems if p.strip())
        detail = " ".join(str(detail).split())
        if len(detail) > 280:
            detail = detail[:277] + "..."
        results.append(ok)
        print("CASE %s: %s%s" % (name, "PASS" if ok else "FAIL",
                                 (" -- " + detail) if detail else ""),
              flush=True)
        return ok

    def verdict(r, want_code, want_line, green=(), red=(), stderr_has=None):
        problems = []
        if r.returncode != want_code:
            problems.append("exit %d, want %d" % (r.returncode, want_code))
        if want_line and want_line not in r.stdout:
            problems.append("stdout lacks %r (exit %d)"
                            % (want_line, r.returncode))
        for pl in green:
            if "LEG PASS %s" % pl not in r.stdout:
                problems.append("%s must be green" % pl)
        for nl in red:
            if "LEG FAIL %s" % nl not in r.stdout:
                problems.append("%s must be red" % nl)
        if stderr_has and stderr_has not in r.stderr:
            problems.append("stderr lacks %r" % stderr_has)
        return problems

    build = globals().get("build_fixture")
    if not callable(build):
        emit("fixtures", ["build_fixture is not defined: "
                          "part-selftest-fixtures.py is missing or assembled "
                          "after part-selftest-run.py"])
        print("SELFTEST: 0/1")
        return 1

    def fixture(prefix, mut=None):
        try:
            got = build(prefix, mut)
        except Exception as e:
            return None, "build_fixture(%s) raised %s: %s" % (
                prefix, type(e).__name__, " ".join(str(e).split())[:200])
        if not (isinstance(got, (tuple, list)) and len(got) == 5):
            return None, ("build_fixture(%s) returned %r, want "
                          "(lane, fleet, base, freeze, lands)" % (prefix, got))
        lane, fleet, base, freeze, lands = got
        for d in (lane, fleet):
            if isinstance(d, str) and d and d not in dirs:
                dirs.append(d)
        bad = [v for v in (base, freeze, lands)
               if not (isinstance(v, str) and re.fullmatch(r"[0-9a-f]{40}", v))]
        if bad:
            return None, "build_fixture(%s) returned a non-40-hex commit: %r" % (
                prefix, [base, freeze, lands])
        return (lane, fleet, base, freeze, lands), ""

    try:
        # 1. the mutant table itself: every one of the 13 legs must be
        #    exercised by at least one named mutant, and nobody may expect a
        #    leg that does not exist.
        rows = _str_mutants()
        problems = []
        if not rows:
            problems.append("MUTANTS is empty: no leg is exercised")
        seen = {}
        for name, leg, _spec in rows:
            if not isinstance(name, str) or not name:
                problems.append("a mutant has no name: %r" % (name,))
                continue
            if leg not in _STR_LEG_ORDER:
                problems.append("mutant %s expects unknown leg %r" % (name, leg))
                continue
            seen.setdefault(leg, []).append(name)
        missing = [n for n in _STR_LEG_ORDER if n not in seen]
        if missing:
            problems.append("no mutant exercises: %s" % " ".join(missing))
        emit("mutant-table", problems,
             note="%d mutants over %d/%d legs" % (len(rows), len(seen),
                                                 len(_STR_LEG_ORDER)))

        # 2. the positive fixture: PASS 13/13, every leg green, receipt
        #    stamped with the evaluated and frozen revisions.
        clean, err = fixture("r75st-clean")
        if clean is None:
            emit("clean", [err])
        else:
            lane, fleet, base, freeze, lands = clean
            r = _run_counter(lane, fleet, lands, freeze)
            problems = verdict(r, 0, "ACCEPT-C-75: PASS legs=13/13",
                               green=_STR_LEG_ORDER)
            if "# evaluated revision: %s" % lands not in r.stdout:
                problems.append("receipt does not stamp the evaluated "
                                "revision %s" % lands[:12])
            if "# freeze revision: %s" % freeze not in r.stdout:
                problems.append("receipt does not name the freeze %s"
                                % freeze[:12])
            emit("clean", problems, note="PASS 13/13 at %s" % lands[:12])

        if clean is None:
            # the dependent cases must still be accounted for: a case that
            # cannot run is a failure, never a silently smaller denominator.
            for name in ("lands-eq-base", "freeze-eq-lands", "missing-lands",
                         "missing-freeze"):
                emit(name, ["clean fixture unavailable: %s" % err])
        else:
            lane, fleet, base, freeze, lands = clean

            # 3. do-nothing control (2): lands == the frozen base is REFUSED
            #    (exit 2) and still prints a FAIL line -- never a PASS.
            r = _run_counter(lane, fleet, base, freeze)
            problems = []
            if r.returncode != 2:
                problems.append("exit %d, want 2 (refusal)" % r.returncode)
            if "ACCEPT-C-75: FAIL" not in (r.stdout + r.stderr):
                problems.append("refusal prints no ACCEPT-C-75: FAIL line")
            if "ACCEPT-C-75: PASS" in (r.stdout + r.stderr):
                problems.append("refusal prints a PASS line")
            emit("lands-eq-base", problems, note="refused, FAIL printed")

            # 4. do-nothing control (1): lands == freeze is GRADED -- the data
            #    legs are red, FROZENCFG stays green, exit 1 (not a refusal).
            r = _run_counter(lane, fleet, freeze, freeze)
            problems = verdict(r, 1, "ACCEPT-C-75: FAIL",
                               green=("FROZENCFG",),
                               red=("ENTRIES", "ROWS"))
            if "REFUSED" in r.stderr:
                problems.append("lands==freeze was refused, not graded")
            emit("freeze-eq-lands", problems, note="graded FAIL, FROZENCFG green")

            # 5. an input error, not a verdict: no --lands / no --freeze.
            r = _run_counter(lane, fleet, lands, freeze, omit_lands=True)
            emit("missing-lands", verdict(r, 2, None, stderr_has="--lands"),
                 note="exit 2 naming --lands")

            r = _run_counter(lane, fleet, lands, None)
            emit("missing-freeze", verdict(r, 2, None, stderr_has="--freeze"),
                 note="exit 2 naming --freeze")

        # 6. a lands commit after the freeze that lands no claim-C artefact
        #    must fail the data legs while the frozen config stays green.
        nodata, err = fixture("r75st-nodata", {"no_data": True})
        if nodata is None:
            emit("no-data", [err])
        else:
            lane, fleet, _b, freeze, lands = nodata
            r = _run_counter(lane, fleet, lands, freeze)
            problems = verdict(r, 1, "ACCEPT-C-75: FAIL",
                               green=("FROZENCFG",),
                               red=("ENTRIES", "ROWS"))
            emit("no-data", problems, note="data legs red, FROZENCFG green")

        # 7. one case per mutant: exit 1 with the expected leg red.
        for name, leg, spec in rows:
            label = "mutant:%s" % name
            if not isinstance(name, str) or not name:
                emit(label, ["unnamed mutant: %r" % (name,)])
                continue
            try:
                mut = spec() if callable(spec) else spec
            except Exception as e:
                emit(label, ["mutant spec raised %s: %s"
                             % (type(e).__name__, " ".join(str(e).split())[:150])])
                continue
            if mut is not None and not isinstance(mut, dict):
                emit(label, ["mutant spec is %s, want dict" % type(mut).__name__])
                continue
            tup, err = fixture("r75st-" + _str_slug(name), mut)
            if tup is None:
                emit(label, [err])
                continue
            lane, fleet, _b, freeze, lands = tup
            r = _run_counter(lane, fleet, lands, freeze)
            problems = verdict(r, 1, "ACCEPT-C-75: FAIL")
            if leg in _STR_LEG_ORDER and "LEG FAIL %s" % leg not in r.stdout:
                found = [n for n in _STR_LEG_ORDER
                         if "LEG FAIL %s" % n in r.stdout]
                problems.append("expected LEG FAIL %s, got [%s] (exit %d)"
                                % (leg, " ".join(found) or "none",
                                   r.returncode))
            emit(label, problems, note="LEG FAIL %s" % leg)
    finally:
        # Remove exactly what this run created: the fixtures the builder
        # returned, an emptied per-fixture parent, and this run's own TMPDIR.
        # Never a shared parent and never a seat directory by name.
        root = _str_scratch()
        for d in dirs:
            shutil.rmtree(d, ignore_errors=True)
        # A builder that keeps lane and fleet inside one per-fixture directory
        # leaves that directory behind (the fixture owns it, both paths point
        # into it); remove it only when it sits strictly below the scratch root
        # and every fixture path lives inside it.
        by_parent = {}
        for d in dirs:
            by_parent.setdefault(os.path.dirname(d), []).append(d)
        for p, kids in by_parent.items():
            if p == root or not p.startswith(root + os.sep):
                continue
            if all(d.startswith(p + os.sep) for d in kids):
                shutil.rmtree(p, ignore_errors=True)
        shutil.rmtree(_str_tmpdir(), ignore_errors=True)

    total = len(results)
    passed = sum(1 for ok in results if ok)
    print("SELFTEST: %d/%d" % (passed, total))
    return 0 if passed == total else 1

# ----------------------------------------------------------- part-main.py ---
# owner: ExecCtrCfgMain.  LEGS / run_legs / print_receipt / refuse / main and
# the `__main__` guard.  Round-74 provenance: `.ufo/waves/round-74/counters/
# accept-c.py` lines 1832-1990 (main) and its LEGS/run_legs/print_receipt.
#
# Round-75 deltas (each from a w1 finding or from the frozen claim text):
#  M1 `<lands> == <base>` is REFUSED (exit 2) and still prints
#     `ACCEPT-C-75: FAIL legs=0/13 (refused: ...)`: the do-nothing control at
#     the claim base is never a graded PASS.  A claim base that is not an
#     ancestor of <lands> at all is refused for the same reason (the graded
#     revision is not descended from the claim's before-state).
#  M2 `<lands> == <freeze>` is GRADED, not refused: the frozen claim text says
#     "`<lands> == <freeze>` is graded, not refused", so the data legs go red
#     and FROZENCFG stays green on the frozen tree (control (1) of the
#     do-nothing receipt).
#  M3 LEGCOUNT against the frozen `legs[]` list in claims.json order; a frozen
#     list that is absent, shorter, longer or differently spelled is a refusal
#     (exit 2), never a partial grade.
#  M4 every clone/materialization lives under the scratch root: `--work` or
#     `$HYAKU_SCRATCH/kotodama-r75/counter` or
#     `/fast/scratch/hyaku/kotodama-r75/counter`; a system temporary directory
#     is refused (QUALITY 14 / prompt §7.4) and the per-run directory is
#     removed on exit.
#  M5 the receipt header carries the round-75 fields (counter sha256 (self),
#     stamped/evaluated/measured, tree, base, freeze, config sha256, frozen
#     legs/map, materialized, lane worktree HEAD disclosure, access date,
#     adopted rows with their staged ids, entries).
#  M6 `--selftest` calls `run_selftest()`, which the selftest parts define;
#     when those parts are not assembled the counter says so instead of
#     raising NameError.
#
# ASSEMBLY: `part-selftest-fixtures.py` and `part-selftest-run.py` must be
# concatenated immediately BEFORE the `__main__` guard below, so `run_selftest`
# exists before the guard runs (CFG-CONTRACT item 5).  The guard is deliberately
# the last three lines of the assembled counter.

LEGS = (
    ("ENTRIES", leg_entries),
    ("ROWS", leg_rows),
    ("REPOINTED", leg_repointed),
    ("GATE", leg_gate),
    ("EVIDENCE", leg_evidence),
    ("REJECTS", leg_rejects),
    ("GROUND", leg_ground),
    ("CITEDLINES", leg_citedlines),
    ("CENSUS", leg_census),
    ("SCRATCHMIRROR", leg_scratch_mirror),
    ("COLLCHECK", leg_collcheck),
    ("FROZENCFG", leg_frozencfg),
    ("INDEX", leg_index),
)


def run_legs(ctx):
    """Run every leg in frozen order; one leg's failure never stops the rest.

    A leg that raises is a red leg with a one-line reason, never a traceback:
    `Missing` is the materialization telling the leg a path is absent, and the
    rest is any defect (a KeyError from a shape the leg expected included) that
    must be visible in the receipt rather than fatal to the run.
    """
    results = []
    for name, fn in LEGS:
        try:
            ok = fn(ctx)
        except Missing as e:
            ok = leg(name, False, "missing at lands: %s" % e)
        except (OSError, RuntimeError, ValueError, TypeError,
                KeyError, AttributeError, subprocess.SubprocessError) as e:
            ok = leg(name, False, "%s: %s" % (type(e).__name__, e))
        results.append((name, bool(ok)))
    passed = sum(1 for _n, ok in results if ok)
    return passed, len(results), results


def print_receipt(root, lands, mat, cfg, how):
    """The receipt header (PART A docstring; tools/check-receipt-seq.py
    grammar): stamped == evaluated == measured == <lands>, the tree of that
    revision, the claim base, the freeze the constants came from, the frozen
    legs and map, where the graded bytes were materialized, and the lane
    worktree HEAD as a disclosure only (never graded)."""
    tree = git(root, "rev-parse", "%s^{tree}" % lands).stdout.strip()
    head = git(root, "rev-parse", "HEAD").stdout.strip()
    print("# round-75 acceptance counter — claim C "
          "(shokuknow narrative-structure-frameworks assimilation)")
    print("# counter sha256 (self): %s" % counter_sha256())
    print("# stamped revision: %s" % lands)
    print("# evaluated revision: %s" % lands)
    print("# measured revision (lane main): %s" % lands)
    print("# tree: %s" % tree)
    print("# base revision: %s" % cfg["base"])
    print("# freeze revision: %s" % cfg["freeze"])
    print("# config sha256 (frozen claims.json): %s" % cfg["frozen_sha256"])
    print("# config source: git show %s:%s (never the graded tree)"
          % (cfg["freeze"], CLAIMS))
    print("# frozen legs: %d (%s)" % (len(cfg["frozen_legs"]),
                                      ",".join(cfg["frozen_legs"])))
    print("# frozen map: %s sha256=%s"
          % (cfg["map_path"], cfg["map_sha256"]))
    print("# materialized: %s at %s" % (how, mat))
    print("# worktree graded: no (leg bytes read only from the checkout and the "
          "git-archive base tree)")
    print("# lane worktree HEAD (disclosure only): %s" % head)
    print("# access date: %s" % cfg["access_date"])
    print("# adopted rows: %s (staged %s)"
          % (" ".join(cfg["rows"]),
             " ".join("/".join(cfg["row_staged"][r]) for r in cfg["rows"])))
    print("# reused rows: %s (staged %s)"
          % (" ".join(cfg["reused"]) or "-",
             " ".join("/".join(cfg["reused_staged"][r]) for r in cfg["reused"])
             or "-"))
    print("# entries: %s" % " ; ".join(cfg["entries"]))
    print()


def refuse(msg):
    """Refuse to grade (H1/M1/M3/M4).  The verdict line is a FAIL, never a
    PASS: no leg ran, and the exit code (2) marks the refusal as an input
    error, not a graded verdict."""
    print("REFUSED: %s" % msg, file=sys.stderr)
    print("ACCEPT-C-75: FAIL legs=0/%d (refused: %s)"
          % (len(LEGS), msg.splitlines()[0]))
    return 2


def _scratch_root(args):
    """M4: the scratch root for every clone, materialization and temp dir.

    `--work` wins; then `$HYAKU_SCRATCH/kotodama-r75/counter`; then the
    operator's scratch tree.  Never the system temporary directory.
    """
    work = (getattr(args, "work", None) or "").strip()
    if work:
        return os.path.abspath(work)
    env = (os.environ.get("HYAKU_SCRATCH") or "").strip()
    if env:
        return os.path.join(os.path.abspath(env), "kotodama-r75", "counter")
    return "/fast/scratch/hyaku/kotodama-r75/counter"


def _forbidden_scratch(path):
    """True when `path` is (inside) the system temporary directory."""
    p = os.path.abspath(path)
    banned = {os.path.abspath("/tmp"), os.path.abspath(tempfile.gettempdir())}
    for b in banned:
        if p == b or p.startswith(b + os.sep):
            return True
    return False


def main(argv=None):
    ap = argparse.ArgumentParser(
        description="round-75 coverage counter (claim C)")
    ap.add_argument("--root", default=".", help="lane repository root")
    ap.add_argument("--lands", default=None,
                    help="required lands revision (40-hex commit)")
    ap.add_argument("--freeze", default=None,
                    help="required freeze revision (40-hex commit; graded when "
                         "it equals --lands, refused only for the claim base)")
    ap.add_argument("--fleet-root", default=None,
                    help="fleet root (default: the lane's parent directory)")
    ap.add_argument("--work", default=None,
                    help="scratch root for the clone/materialization "
                         "(default: $HYAKU_SCRATCH/kotodama-r75/counter or "
                         "/fast/scratch/hyaku/kotodama-r75/counter)")
    ap.add_argument("--selftest", action="store_true", help="run in-process cases")
    args = ap.parse_args(argv)

    if args.selftest:
        runner = globals().get("run_selftest")
        if runner is None:
            return refuse("--selftest needs part-selftest-fixtures.py and "
                          "part-selftest-run.py assembled before the __main__ "
                          "guard (CFG-CONTRACT item 5)")
        return runner()

    if not args.lands or not re.fullmatch(r"[0-9a-fA-F]{40}", args.lands.strip()):
        print("ERROR: --lands must be a 40-hex commit "
              "(the worktree is never graded, QUALITY 19)", file=sys.stderr)
        return 2
    if not args.freeze or not re.fullmatch(r"[0-9a-fA-F]{40}",
                                           args.freeze.strip()):
        print("ERROR: --freeze must be a 40-hex commit "
              "(the claim constants are read from it, H1)", file=sys.stderr)
        return 2
    lands = args.lands.strip().lower()
    freeze = args.freeze.strip().lower()
    root = args.root if os.path.isabs(args.root) else os.path.join(LANE, args.root)
    if not os.path.isdir(os.path.join(root, ".git")):
        print("ERROR: not a git repository: %s" % root, file=sys.stderr)
        return 2
    for name, rev in (("--lands", lands), ("--freeze", freeze)):
        if git(root, "cat-file", "-e", "%s^{commit}" % rev).returncode != 0:
            print("ERROR: %s revision not found: %s" % (name, rev),
                  file=sys.stderr)
            return 2
    try:
        cfg = load_frozen_config(root, freeze)
    except ConfigError as e:
        return refuse("%s" % e)
    if lands == cfg["base"]:
        return refuse("lands %s is the frozen claim base %s (the do-nothing "
                      "control: no data landed)" % (lands[:12], cfg["base"][:12]))
    if not is_ancestor(root, cfg["base"], lands):
        return refuse("claim base %s is not an ancestor of lands %s (the graded "
                      "revision is not descended from the claim's before-state)"
                      % (cfg["base"][:12], lands[:12]))
    ours = [name for name, _fn in LEGS]
    frozen_legs = cfg["frozen_legs"]
    if not frozen_legs:
        return refuse("the frozen claims.json carries no legs list (LEGCOUNT)")
    if len(frozen_legs) != len(ours) or frozen_legs != ours:
        return refuse("LEGCOUNT: the frozen claims.json lists %d legs (%s); "
                      "this counter implements %d (%s)"
                      % (len(frozen_legs), ",".join(frozen_legs),
                         len(ours), ",".join(ours)))
    if git(root, "cat-file", "-e", "%s^{commit}" % cfg["base"]).returncode != 0:
        print("ERROR: frozen claim base not found: %s" % cfg["base"],
              file=sys.stderr)
        return 2
    fleet_root = args.fleet_root or os.path.dirname(os.path.abspath(root))

    scratch = _scratch_root(args)
    if _forbidden_scratch(scratch):
        return refuse("scratch root %s is the system temporary directory "
                      "(pass --work or set $HYAKU_SCRATCH; QUALITY 14)"
                      % scratch)
    try:
        os.makedirs(scratch, exist_ok=True)
    except OSError as e:
        return refuse("cannot create scratch root %s: %s" % (scratch, e))

    tmp_root = tempfile.mkdtemp(prefix="r75-lands-", dir=scratch)
    try:
        mat = os.path.join(tmp_root, "clone")
        mat_base = os.path.join(tmp_root, "base")
        os.makedirs(mat_base)
        try:
            clone_at(root, lands, mat)
            how = ("git clone of %s, checkout --detach %s"
                   % (os.path.abspath(root), lands[:12]))
        except RuntimeError:
            shutil.rmtree(mat, ignore_errors=True)
            os.makedirs(mat)
            materialize(root, lands, mat)
            how = ("git archive of %s (the clone refused the revision)"
                   % lands[:12])
        try:
            materialize(root, cfg["base"], mat_base)
        except RuntimeError as e:
            print("ERROR: %s" % e, file=sys.stderr)
            return 2
        ctx = {"root": root, "lands": lands, "mat": mat, "mat_base": mat_base,
               "cfg": cfg, "fleet_root": fleet_root, "scratch": scratch}
        print_receipt(root, lands, mat, cfg, how)
        passed, total, _results = run_legs(ctx)
    finally:
        shutil.rmtree(tmp_root, ignore_errors=True)
    ok = passed == total
    print("ACCEPT-C-75: %s legs=%d/%d" % ("PASS" if ok else "FAIL", passed, total))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
