#!/usr/bin/env python3
r"""Round-77 coverage acceptance counter — claim C.

Claim C (reports/round-77/claims.json, id "C", axis coverage): the shokuknow
assimilation of the Chinese naming-system theme — the 姓/名 structure and the
onomastics literature's finite lexeme classification of Chinese given names —
staged as exactly ONE admitted amendment entry under
corpus/knowledge/linguistics/, citing a by-DOCUMENT row set.  The landing adds
one knowledge file (253 -> 254) and one mined, opened registry row per new
document (820 -> 822; S897, S898).

Grading model (QUALITY 19).  Nothing in the graded worktree is trusted: the
counter clones the lane into a fresh scratch directory, checks out <lands>
there, and every graded byte is read from that checkout.  The claim base is
materialized from the same clone with `git archive <base>`.  Read-only git
against the lane supplies commit metadata (ancestry, blobs at a revision) and
never a graded byte.

Receipt header (QUALITY 17/19 grammar of tools/check-receipt-seq.py):

  # counter sha256 (self): ...        the counter's own bytes
  # stamped revision: <lands>         the revision the receipt claims
  # evaluated revision: <lands>       the revision the clone was checked out at
  # measured revision (lane main): <lands>   the revision whose bytes were read
  # tree: <lands>^{tree}              the tree of that revision
  # base revision: <frozen claim base>
  # freeze revision: <freeze>         the commit the constants are read from
  # lane worktree HEAD (disclosure only): ...   never graded

Legs (13, the draft's lineage set, every name once — the frozen `legs[]` is
GENERATED from this table by `legs_generated()` / `--emit-legs`, never
hand-typed, and a frozen list that differs is refused):

  ENTRIES    the admitted entry exists at lands and not at base, carries the
             provenance header without placeholders, a section, a body at
             least the smallest base entry, cites mined rows, and the knowledge
             tree moves knowledge_before -> +n with the diff exactly the entries
  ROWS       ONLY `| S### |` row lines are counted: the ids added inside the
             frozen row_set (rows_before -> +k), each 11 cells / mined / opened
             / cadence / used-by exactly its citing entries / live URL +
             same-page capture / anchor quote; added NON-row lines are never
             counted here (r76 defect 1); a pre-existing row may change only
             its rule-2 cells (status, recheck, used-by)
  REPOINTED  every `source:` line of the admitted entry carries exactly one id
             whose row URL names that document; every inline S-id resolves to a
             frozen lane row or a base-held row; no removed legacy id and no
             campaign-namespace id is cited as a lane row
  GATE       corpus/lessons/round-77.md `## Gate`: one admit row per row with
             URL, access date, a <=25-token / <=80-character located quote and
             the evidence path
  EVIDENCE   a committed capture per row: fetch/UA/HTTP 200/digest/window whose
             scope rule re-derives from the bytes, stamped against <freeze>, and
             the Gate quote inside it
  REJECTS    >=1 admit and >=1 reject from the assimilation set: the frozen
             refused staged ids are in the Gate reject table with reason+flip
             and are never lane rows; declared triage counts sum
  GROUND     frozen sweeps absent at base UNCONDITIONALLY and present in the
             admitted entry; frozen document fragments absent at base and
             present in the landed rows/entry; the declared ground receipt is
             committed at lands with no nonzero exit line
  CITEDLINES tools/check-cited-lines.py over the entries prints
             `CITED-LINES: 0 finding(s)` (one id scopes one clause; no table
             row hides a citation)
  CENSUS     the fleet `sources-census.sh validate --file` exits 0 on the
             landed registry with no E-code line; a declared census-start
             receipt is committed at lands and records the declared row count
  SCRATCHMIRROR the staged-id universe and its collision guard are committed
             and re-derive from the BASE registry: reg-ids == the base id set,
             staged-ids covers every row_set staged id, collisions ==
             reg-ids ∩ staged-ids, no adopted lane id is already in reg-ids, and
             the 1-3-space / 4-space indent guard proves both ways on committed
             bytes (a declared mirror receipt is graded when present)
  COLLCHECK  DOCUMENT identity — the frozen document_url folded to
             (host, path) vs the row's source cell; never a raw URL string
             comparison (r76 defect 2); the frozen staged->lane map agrees
  FROZENCFG  the frozen claims.json is the config, byte-identical at <lands>,
             stamped round-77/frozen on the frozen base, and its by-document map
             blob (when declared) hashes to the frozen digest
  INDEX      README index row for the entry inside its partition, every
             heading vs the live count, last footer total+vector, older
             footers preserved; PLUS `required_sections[]` (Paths / Search-log)
             checked here and never as out-of-set ROWS

Readings of the ambiguous wording (each is also stated in
`.ufo/waves/round-77/w1/ExecAdaptC.md`):

  R1 ROWS counts additions BY ID: `set(lands ids) - set(base ids)` must equal
     the frozen row_set lane ids.  An added non-row line (the Paths / Search-log
     edits the r76 freeze failed to account for) is invisible to ROWS and, when
     required, graded by INDEX through `required_sections[]`.  A pre-existing
     row is compared cell by cell and may differ only in the rule-2 cells the
     registry contract lets a round change in place (status, recheck, used-by);
     any other cell change, a removal or a reordering fails.
  R2 COLLCHECK joins documents through `_doc_url_key` (host without `www.`,
     percent-decoded path, `web.archive.org/web/<ts><mod>/<original>` folded to
     the original).  A same-page capture of the same path is the SAME document;
     a different path on the same host is NOT — which is exactly the alias the
     round-76 COLLCHECK could not separate from prose.
  R3 LEGCOUNT is refused, not graded (the r76 shape): a frozen `legs[]` that is
     absent, shorter, longer, reordered or duplicated is an unusable contract
     (exit 2, `FAIL legs=0/13`), because the frozen list names the legs the
     claim is measured by.  The counter prints its generated list in the
     receipt and via `--emit-legs`.
  R4 The do-nothing control `<lands> == <freeze>` is graded: FROZENCFG,
     SCRATCHMIRROR, CENSUS and GROUND's before-half stay green (they grade the
     frozen state, which is intact), the data legs go red.  `<lands> == <base>`
     is REFUSED (exit 2) and still prints `ACCEPT-C-77: FAIL legs=0/13`.
  R5 `required_sections[]` records are {path?, pattern, min?, label?}; a record
     without `path` applies to every admitted entry.  The pattern is a Python
     regex matched per line; `min` defaults to 1.
  R6 `row_set[]` records are {lane_id, staged_id, document_url} (r77 schema);
     the r76 spellings {id, staged, document} are accepted as aliases so an
     older staged map still loads, but the receipt prints the lane/staged pairs
     it actually read.
  R7 A registry row's source cell must name BOTH the live URL and a same-page
     Wayback capture whose embedded original folds to the same document
     (QUALITY 18); the capture is a carrier, not a second document.
  R8 `removed_ids[]` (optional) is the frozen list of legacy ids the rewrite
     must not keep (the draft names S886/S888/S889/S890/S891/S896): each must be
     absent from the admitted entry, and REPOINTED fails when one is cited.

Usage:
  python3 -B accept-c.py --root <lane> --lands <40hex> --freeze <40hex>
                        [--fleet-root <fleet>] [--work <scratch>] [--selftest]
                        [--emit-legs]

Exit: 0 all legs pass; 1 any leg fails; 2 input error or refusal (missing
argument, unknown revision, unreadable/unusable claims.json at <freeze>,
`lands` equal to the frozen claim base, the frozen `legs[]` not matching this
counter's table, or the scratch root being the system temporary directory).

Scratch (operator 2026-10-25): `--work` -> `$HYAKU_SCRATCH/kotodama-r77/counter`
-> an operator-chosen `$TMPDIR/kotodama-r77/counter` -> the operator default
`/fast/scratch/hyaku/kotodama-r77/counter`.  The SYSTEM temporary directory is
refused, never written to; `--selftest` resolves `.../kotodama-r77/selftest`
the same way and removes its own run directory.
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
ROUND = 77
CLAIMS = "reports/round-77/claims.json"
REGISTRY = "corpus/SOURCES.md"
LESSON = "corpus/lessons/round-77.md"
EVIDENCE_DIR = "reports/round-77/evidence"
TELEMETRY = "reports/round-77/telemetry"
README = "corpus/README.md"
KNOWLEDGE = "corpus/knowledge"
ASSIM = ".ufo/waves/round-77/assimilation"
BASE_LESSON = "corpus/lessons/round-76.md"

# the r77 claim contract: the single-entry shape, the by-document row map and
# the non-row requirements named by the routed r76 defects.  `map` and
# `receipts` are OPTIONAL (the row_set itself is the document map; receipts fall
# back to ground.receipt), and CLAIM_KEYS omits both.
CLAIM_KEYS = ("entries", "rows_before", "knowledge_before", "row_set",
              "required_sections", "ground", "rejects", "legs")
HEADER_FIELDS = ("source", "verified-at", "recheck", "ground", "topic")
PLACEHOLDERS = ("", "todo", "tbd", "fixme", "xxx", "n/a", "?", "—")
MIN_WINDOW_CHARS = 4096
MAX_QUOTE_TOKENS = 25
MAX_QUOTE_CHARS = 80

# registry geometry (SOURCES-CONTRACT-v1: 11 columns, census NF==13)
ID, SOURCE, KIND, TIER, SCOPE, ANCHOR, TEACHES, STATUS, OPENED, RECHECK, USEDBY = range(11)
NCELLS = 11

ROW_RE = re.compile(r"^ {0,3}\|\s*(S\d{3,})\s*\|")
TOKEN_RE = re.compile(r"\bS\d{3,}\b")
URL_RE = re.compile(r"https?://[^\s|<>()（）「」『』]+")
QUOTE_RE = re.compile(r'"(?:\\.|[^"\\\n])*"|“[^“”\n]*”|«[^«»\n]*»'
                      r'|「[^「」\n]*」|『[^『』\n]*』')
H2_RE = re.compile(r"^##\s")
ANGLE_RE = re.compile(r"<[^>]+>")
README_SECTION_RE = re.compile(r"^## ([a-z-]+)/ \((\d+)\)\s*$", re.M)
README_ROW_RE = re.compile(r"^- `([^`]+\.md)` — (.*)$")
README_FOOTER_RE = re.compile(r"\(total (\d+) files; directory totals ([\d/]+)\)")
ROW_SHAPED_LINE_RE = re.compile(r"^\s*\|\s*S\d{3,}\s*\|")
DASHES = ("—", "-", "–", "n/a", "na", "")
CLEAN_CHALLENGE = ("none", "no", "clean", "not-served", "not served")


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


def gate_section(text):
    return section_block(text, r"^##\s+Gate\b").splitlines()


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
            open_row = False  # a blank line ends the table
        elif line.startswith(" ") and rows and open_row:
            rows[-1] += " " + line.strip()
    return rows


def urls_in(s):
    return URL_RE.findall(s)


def _cfg_pct_decode(s):
    def take(m):
        try:
            return chr(int(m.group(1), 16))
        except ValueError:
            return m.group(0)
    return re.sub(r"%([0-9A-Fa-f]{2})", take, s)


def _doc_url_key(u):
    """The DOCUMENT a URL names: (host without `www.`, decoded document path).

    Folds the only two carriers a claim C row depends on:
      * `web.archive.org/web/<ts><mod>/<original>` -> key of <original>
        (a same-page capture is a carrier, not a second document);
      * `%20` / a raw space are the same character after decoding.
    Query strings are not part of document identity (a query is a view
    parameter); a different PATH on the same host is a different document, which
    is what separates a real document from an alias route.
    """
    u = (u or "").strip()
    try:
        host, path = norm_url(u)
    except ValueError:
        return ("", "")
    if host.startswith("www."):
        host = host[4:]
    path = _cfg_pct_decode(path)
    if host == "web.archive.org":
        m = re.match(r"^/web/\d{8,14}[a-z_]*/(.+)$", path)
        if m:
            return _doc_url_key(m.group(1))
    return (host, path)


def _archive_original(u):
    """The original URL a `web.archive.org/web/<ts>/…` carrier embeds, else None."""
    host, path = norm_url(u)
    bare = host[4:] if host.startswith("www.") else host
    if bare != "web.archive.org":
        return None
    m = re.match(r"^/web/\d{8,14}[a-z_]*/(.+)$", path)
    return m.group(1) if m else None


def _doc_pair(cell):
    """(live URLs, capture originals) named by a registry source cell."""
    live, caps = [], []
    for u in urls_in(cell):
        orig = _archive_original(u)
        if orig is not None:
            caps.append(orig)
        else:
            live.append(u)
    return live, caps


def _paths_from_spec(spec):
    """Repo-relative paths from an `entries`-like value (string, list, object)."""
    out = []
    items = spec if isinstance(spec, (list, tuple)) else [spec]
    for item in items:
        if isinstance(item, dict):
            value = item.get("path") or item.get("file") or ""
        else:
            value = item
        value = str(value).strip()
        if value.startswith("./"):
            value = value[2:]
        if value:
            out.append(value)
    return list(dict.fromkeys(out))


def _frozen_claim(doc):
    """The claim object with id C (case-insensitive) inside a claims document."""
    for c in doc.get("claims") or []:
        if isinstance(c, dict) and str(c.get("id", "")).upper() == "C":
            return c
    return None


def _cfg_int(claim, key, floor=1):
    value = claim.get(key)
    if isinstance(value, bool) or not isinstance(value, int):
        raise ConfigError("claim C at freeze carries no integer %s: %r"
                          % (key, value))
    if value < floor:
        raise ConfigError("claim C at freeze declares %s = %d (floor %d)"
                          % (key, value, floor))
    return value


def _staged_ids(value):
    """One row's `staged_id` cell as a list of staged ids."""
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
    if not out:
        raise ConfigError("row_set record carries no staged S-id: %r" % (value,))
    return out


def _cfg_row_set(claim):
    """[{lane, staged[], document}] from the r77 row_set schema (R6)."""
    value = claim.get("row_set")
    if not isinstance(value, list) or not value:
        raise ConfigError("row_set at freeze is empty")
    out, seen = [], set()
    for item in value:
        if not isinstance(item, dict):
            raise ConfigError("row_set carries a non-object item: %r" % (item,))
        lane = str(item.get("lane_id") or item.get("id") or item.get("lane")
                   or "").strip().upper()
        if not TOKEN_RE.fullmatch(lane):
            raise ConfigError("row_set record carries no lane S-id: %r" % (item,))
        if lane in seen:
            raise ConfigError("row_set repeats the lane id %r" % lane)
        seen.add(lane)
        staged = _staged_ids(item.get("staged_id") if "staged_id" in item
                             else item.get("staged"))
        document = str(item.get("document_url") or item.get("document")
                       or item.get("url") or "").strip()
        if not document or not urls_in(document):
            raise ConfigError("row_set %s carries no document URL: %r"
                              % (lane, item.get("document_url")))
        out.append({"lane": lane, "staged": staged, "document": document})
    return out


def _cfg_required_sections(claim):
    """R5: [{path, pattern, min, label}] — the non-row requirements (r76 defect 1)."""
    value = claim.get("required_sections")
    if not isinstance(value, list) or not value:
        raise ConfigError("required_sections at freeze is empty (the required "
                          "non-row edits must be named, never counted as rows)")
    out = []
    for item in value:
        if isinstance(item, str):
            item = {"pattern": item}
        if not isinstance(item, dict):
            raise ConfigError("required_sections carries a non-object item: %r"
                              % (item,))
        pattern = str(item.get("pattern") or item.get("regex") or "").strip()
        if not pattern:
            raise ConfigError("a required_sections record carries no pattern")
        try:
            re.compile(pattern)
        except re.error as e:
            raise ConfigError("required_sections pattern %r does not compile: %s"
                              % (pattern, e))
        path = str(item.get("path") or item.get("file") or "").strip()
        if path.startswith("./"):
            path = path[2:]
        if path and (path.startswith("/") or ".." in path.split("/")):
            raise ConfigError("required_sections path is not repo-relative: %r"
                              % path)
        try:
            floor = int(item.get("min", 1))
        except (TypeError, ValueError):
            raise ConfigError("required_sections min is not an integer: %r"
                              % (item.get("min"),))
        label = str(item.get("label") or item.get("heading") or pattern).strip()
        out.append({"path": path, "pattern": pattern, "min": max(floor, 1),
                    "label": label})
    return out


def _cfg_sweeps(ground, entries):
    """[{pattern, candidate, scope}] from claim.ground.sweeps."""
    value = ground.get("sweeps")
    if not isinstance(value, list) or not value:
        raise ConfigError("ground.sweeps at freeze is empty (the before/after "
                          "ground probe is the claim's coverage evidence)")
    out = []
    for item in value:
        if not isinstance(item, dict):
            raise ConfigError("ground.sweeps carries a non-object item: %r"
                              % (item,))
        pattern = str(item.get("pattern") or "").strip()
        if not pattern:
            raise ConfigError("a ground sweep carries no pattern: %r" % (item,))
        try:
            re.compile(pattern)
        except re.error as e:
            raise ConfigError("ground sweep pattern %r does not compile: %s"
                              % (pattern, e))
        candidate = str(item.get("candidate") or "").strip()
        candidate = candidate[2:] if candidate.startswith("./") else candidate
        if candidate and candidate not in entries:
            raise ConfigError("ground sweep %r is gated by %r, which is not a "
                              "frozen entry" % (pattern, candidate))
        scope = str(item.get("scope") or KNOWLEDGE).strip().rstrip("/")
        if not scope or scope.startswith("/") or ".." in scope.split("/"):
            raise ConfigError("ground sweep %r carries a non-relative scope: %r"
                              % (pattern, scope))
        out.append({"pattern": pattern, "candidate": candidate, "scope": scope})
    return out


def _cfg_receipt_path(value, what):
    """One repo-relative receipt path (string or {path, contains[]})."""
    item = value if isinstance(value, dict) else {"path": value}
    path = str(item.get("path") or "").strip()
    if not path:
        raise ConfigError("%s carries no path" % what)
    if path.startswith("/") or ".." in path.split("/"):
        raise ConfigError("%s path is not repo-relative: %r" % (what, path))
    return {"path": path,
            "contains": [str(x) for x in (item.get("contains") or [])]}


def _cfg_ground_receipt(ground):
    """The declared ground receipt ({path, contains[]}) or None."""
    value = ground.get("receipt")
    if value is None or value == "":
        return None
    return _cfg_receipt_path(value, "ground.receipt")


def _cfg_census_start(claim):
    """The declared census-start receipt ({path, rows, contains[]}) or None."""
    value = claim.get("census_start")
    if value is None:
        return None
    rec = _cfg_receipt_path(value, "census_start")
    rows = value.get("rows") if isinstance(value, dict) else None
    if rows is not None:
        try:
            rec["rows"] = int(rows)
        except (TypeError, ValueError):
            raise ConfigError("census_start.rows is not an integer: %r" % (rows,))
    else:
        rec["rows"] = None
    return rec


def _cfg_removed_ids(claim):
    """R8: the frozen legacy ids the rewrite must not keep (may be empty)."""
    out = []
    for key in ("removed_ids", "removed_legacy_ids", "legacy_ids"):
        value = claim.get(key)
        if value is None:
            continue
        items = value if isinstance(value, list) else [value]
        for item in items:
            for sid in TOKEN_RE.findall(str(item).upper()):
                if sid not in out:
                    out.append(sid)
    return out


def _cfg_staged_ids_path(claim):
    """The assimilation staged-id universe path (default the r77 tree)."""
    value = claim.get("staged_ids")
    path = str(value or "").strip() if value is not None else ""
    if not path:
        return ASSIM + "/staged-ids"
    if path.startswith("/") or ".." in path.split("/"):
        raise ConfigError("claim staged_ids path is not repo-relative: %r"
                          % path)
    return path


def _cfg_scratch_mirror(claim):
    """{dir, receipt} for SCRATCHMIRROR (dir defaults to the r77 tree)."""
    value = claim.get("scratch_mirror")
    out = {"dir": ASSIM, "receipt": None}
    if value is None:
        return out
    if isinstance(value, str):
        value = {"dir": value}
    if not isinstance(value, dict):
        raise ConfigError("scratch_mirror at freeze is not an object: %r"
                          % (value,))
    directory = str(value.get("dir") or ASSIM).strip().rstrip("/")
    if not directory or directory.startswith("/") \
            or ".." in directory.split("/"):
        raise ConfigError("scratch_mirror.dir is not repo-relative: %r"
                          % directory)
    out["dir"] = directory
    if value.get("receipt"):
        out["receipt"] = _cfg_receipt_path(value["receipt"],
                                          "scratch_mirror.receipt")
    return out


def _cfg_legs(claim):
    """The frozen leg names (`NAME: wording` accepted), order preserved."""
    value = claim.get("legs")
    if not isinstance(value, list) or not value:
        raise ConfigError("the frozen claims.json carries no legs list (the "
                          "claim contract's leg set is absent)")
    out = []
    for item in value:
        name = str(item).split(":", 1)[0].strip().upper()
        if name:
            out.append(name)
    if not out:
        raise ConfigError("the frozen legs list carries no leg name")
    return out


def _cfg_refusal_text(rejects):
    out = []
    for key in ("refused_staged_not_appended", "refused_staged",
                "forced_new_quotes", "folded_dropped"):
        value = rejects.get(key)
        if value is None:
            continue
        items = value if isinstance(value, list) else [value]
        out.extend(str(x) for x in items if str(x).strip())
    return out


def _cfg_access_date(claim, doc):
    for holder in (claim, doc):
        value = str(holder.get("access_date") or "").strip()
        if re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
            return value
    raise ConfigError("claim C at freeze declares no YYYY-MM-DD access_date "
                      "(the Gate and evidence dates are undeterminable)")


def load_frozen_config(root, freeze):
    """H1: every constant comes from `git show <freeze>:claims.json`.

    Returns: freeze, frozen_sha256, doc_round, doc_status, doc_frozen, base,
    access_date, entries, min_entries, rows, row_staged, row_doc, rows_before,
    knowledge_before, knowledge_after, rows_after, required_sections, sweeps,
    ground_receipt, fragments, terms, refused_staged, refused_staged_text,
    refused_files, counts, map_path, map_sha256, receipts, frozen_legs,
    claim_keys.
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
        raise ConfigError("claim base at freeze is not a 40-hex revision: %r"
                          % base)

    entries = _paths_from_spec(claim["entries"])
    if not entries:
        raise ConfigError("claim C at freeze lists no entry path")
    for e in entries:
        if e.startswith("/") or ".." in e.split("/"):
            raise ConfigError("entry path at freeze is not repo-relative: %r" % e)
    min_entries = claim.get("min_entries", 1)
    if isinstance(min_entries, bool) or not isinstance(min_entries, int) \
            or min_entries < 1:
        raise ConfigError("claim C at freeze declares a bad min_entries: %r"
                          % (min_entries,))
    if len(entries) < min_entries:
        raise ConfigError("claim C at freeze lists %d entry path(s); "
                          "min_entries is %d" % (len(entries), min_entries))

    row_records = _cfg_row_set(claim)
    rows = [r["lane"] for r in row_records]
    row_staged = dict((r["lane"], r["staged"]) for r in row_records)
    row_doc = dict((r["lane"], r["document"]) for r in row_records)

    rows_before = _cfg_int(claim, "rows_before")
    knowledge_before = _cfg_int(claim, "knowledge_before")
    knowledge_after = claim.get("knowledge_after")
    if knowledge_after is not None:
        if isinstance(knowledge_after, bool) or not isinstance(knowledge_after, int):
            raise ConfigError("claim knowledge_after is not an integer: %r"
                              % (knowledge_after,))
    rows_after = claim.get("rows_after")
    if rows_after is not None:
        if isinstance(rows_after, bool) or not isinstance(rows_after, int):
            raise ConfigError("claim rows_after is not an integer: %r"
                              % (rows_after,))

    required_sections = _cfg_required_sections(claim)

    ground = claim["ground"]
    if not isinstance(ground, dict):
        raise ConfigError("ground at freeze is not an object")
    fragments = [str(x) for x in (ground.get("fragments") or [])]
    terms = [str(x) for x in (ground.get("terms")
                              or ground.get("cjk_terms") or [])]
    if not fragments:
        raise ConfigError("ground.fragments at freeze is empty")
    sweeps = _cfg_sweeps(ground, set(entries))
    ground_receipt = _cfg_ground_receipt(ground)

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

    # D2: the by-document map is OPTIONAL.  The r77 draft records the
    # document/staged/lane map inside `row_set` itself; a separately pinned map
    # blob (r76 shape) is graded when declared, and COLLCHECK then cross-checks
    # it.  An undeclared map is printed as "(none declared)", never assumed.
    map_spec = claim.get("map")
    map_path = map_sha = ""
    if map_spec is not None:
        if not isinstance(map_spec, dict):
            raise ConfigError("claim map at freeze is not an object: %r"
                              % (map_spec,))
        map_path = str(map_spec.get("path") or "").strip()
        map_sha = str(map_spec.get("sha256") or "").strip().lower()
        if not map_path or map_path.startswith("/") \
                or ".." in map_path.split("/"):
            raise ConfigError("claim map.path at freeze is not a relative repo "
                              "path: %r" % map_path)
        if not re.fullmatch(r"[0-9a-f]{64}", map_sha):
            raise ConfigError("claim map.sha256 at freeze is not a 64-hex "
                              "digest (the by-document map cannot be pinned): "
                              "%r" % (map_spec.get("sha256")))

    census_start = _cfg_census_start(claim)
    removed_ids = _cfg_removed_ids(claim)
    staged_ids_path = _cfg_staged_ids_path(claim)
    scratch_mirror = _cfg_scratch_mirror(claim)
    frozen_legs = _cfg_legs(claim)
    access_date = _cfg_access_date(claim, doc)

    staged_universe = set()
    r = git_bytes(root, "show", "%s:%s" % (freeze, staged_ids_path))
    if r.returncode == 0:
        for line in r.stdout.decode("utf-8", "replace").splitlines():
            sid = line.strip().upper()
            if TOKEN_RE.fullmatch(sid):
                staged_universe.add(sid)

    lane_ids = set(rows)
    staged_ids = set()
    for staged in row_staged.values():
        staged_ids |= set(staged)
    refused_staged = []
    for text in refused_staged_text:
        for sid in TOKEN_RE.findall(text.upper()):
            if sid in lane_ids or sid in staged_ids or sid in refused_staged:
                continue
            refused_staged.append(sid)

    return {
        "freeze": freeze,
        "frozen_sha256": hashlib.sha256(raw).hexdigest(),
        "doc_round": doc.get("round"),
        "doc_status": str(doc.get("status") or ""),
        "doc_frozen": doc.get("frozen"),
        "base": base,
        "access_date": access_date,
        "entries": entries,
        "min_entries": min_entries,
        "rows": rows,
        "row_staged": row_staged,
        "row_doc": row_doc,
        "rows_before": rows_before,
        "knowledge_before": knowledge_before,
        "knowledge_after": knowledge_after,
        "rows_after": rows_after,
        "required_sections": required_sections,
        "sweeps": sweeps,
        "ground_receipt": ground_receipt,
        "fragments": fragments,
        "terms": terms,
        "refused_staged": sorted(refused_staged),
        "refused_staged_text": refused_staged_text,
        "refused_files": refused_files,
        "counts": parsed_counts,
        "map_path": map_path,
        "map_sha256": map_sha,
        "census_start": census_start,
        "removed_ids": removed_ids,
        "staged_ids_path": staged_ids_path,
        "staged_universe": sorted(staged_universe),
        "scratch_mirror": scratch_mirror,
        "frozen_legs": frozen_legs,
        "allowed_ids": lane_ids,
        "forbidden_ids": sorted(staged_ids - lane_ids),
        "claim_keys": sorted(claim.keys()),
    }


# --------------------------------------------------------------- evidence ---

def _window(text):
    """The stored window: lines between `--- window ---` and `--- quote ---`."""
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


def _evidence(mat, rid):
    """Parse reports/round-77/evidence/<id>.txt (capture-tool grammar)."""
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
            originals.extend(found)
            out[key] = value + " (original %s)" % " ; ".join(found)
    out["_all"] = pairs
    out["_text"] = text
    out["_original"] = list(dict.fromkeys(originals))
    out["_window"] = _window(text)
    return out


def _evidence_count(value):
    m = re.search(r"\d+", str(value or ""))
    return int(m.group(0)) if m else None


def _evidence_fold(s):
    return nfkc_ws(s or "")


def _evidence_doc_keys(ev):
    keys = set()
    for token in (ev.get("fetch") or "", ev.get("url") or "",
                  ev.get("final-url") or ""):
        for u in urls_in(token):
            keys.add(_doc_url_key(u))
        if token.strip():
            keys.add(_doc_url_key(token.strip()))
    return keys


def _evidence_gate_quotes(gate_admit, sid):
    """Every <=25-token / <=80-char quoted span in the row's Gate admit record."""
    out = []
    for row in gate_admit.get(sid, []):
        for span in quoted_spans(row):
            if quote_ok(span):
                out.append(_evidence_fold(span))
    return dedupe(out)


# ------------------------------------------------------------ entries view ---

def _header_values(text):
    out = {}
    for line in header_block(text):
        m = re.match(r"^[-*\s]*([A-Za-z][A-Za-z0-9 -]*):\s*(.*)$", line)
        if m:
            out.setdefault(norm_label(m.group(1)), m.group(2).strip())
    return out


def _placeholder_value(value):
    stripped = value.strip().strip("-—– ").strip()
    if stripped.lower() in PLACEHOLDERS:
        return True
    first = stripped.split()[0].lower() if stripped.split() else ""
    return first in PLACEHOLDERS


def _entry_topic(text):
    for line in header_block(text):
        m = re.match(r"^[-*\s]*topic:\s*(.*)$", line)
        if m:
            return m.group(1).strip()
    return None


def source_field_lines(text):
    """Every `source:` line in the whole entry (header and body)."""
    return [m.group(1) for m in
            re.finditer(r"^[-*\s]*source:\s*(.*)$", text, re.M)]


def _body_words(text):
    lines = text.splitlines()
    started = False
    words = 0
    for line in lines:
        if not started:
            if H2_RE.match(line):
                started = True
            continue
        if re.match(r"^#{1,6}\s", line):
            continue
        words += len(line.split())
    return words


def _min_entry_words(mat_base):
    best = None
    try:
        files = [p for p in tree_files(mat_base, KNOWLEDGE) if p.endswith(".md")]
    except OSError:
        return 0
    for rel in files:
        try:
            text = read_tree(mat_base, rel)
        except Missing:
            continue
        n = len(text.split())
        best = n if best is None else min(best, n)
    return best or 0


def _entry_citations(mat, entries, bad):
    """{S-id: {entry paths}} from every `source:` line of the frozen entries."""
    cited = {}
    for e in entries:
        try:
            text = read_tree(mat, e)
        except Missing:
            bad.append("%s missing (cannot derive used-by)" % e)
            continue
        for sline in source_field_lines(text):
            for sid in TOKEN_RE.findall(sline):
                cited.setdefault(sid, set()).add(e)
    return cited


def _md_count(tree, rel):
    base = os.path.join(tree, rel)
    n = 0
    for _dirpath, _dirnames, filenames in os.walk(base):
        for fn in filenames:
            if fn.endswith(".md"):
                n += 1
    return n


def _readme_sections(text):
    ms = list(README_SECTION_RE.finditer(text))
    out = []
    for i, m in enumerate(ms):
        end = ms[i + 1].start() if i + 1 < len(ms) else len(text)
        out.append((m.group(1), m.start(), end))
    return out


def _footer_blocks(text):
    blocks, cur = [], []
    for line in text.splitlines():
        if not line.strip():
            if cur:
                blocks.append("\n".join(cur))
                cur = []
        else:
            cur.append(line)
    if cur:
        blocks.append("\n".join(cur))
    return [b for b in blocks if "Counts checked " in b]


def _grep_tree(tree, scope, pattern):
    rx = re.compile(pattern)
    hits = []
    base = os.path.join(tree, scope)
    for dirpath, _dirnames, filenames in os.walk(base):
        for fn in sorted(filenames):
            full = os.path.join(dirpath, fn)
            try:
                with open(full, encoding="utf-8", errors="replace") as fh:
                    txt = fh.read()
            except OSError:
                continue
            if rx.search(txt):
                hits.append(os.path.relpath(full, tree))
    return hits


def _gate_tables(lines):
    """(admit rows by sid, reject rows) from the Gate section's tables.

    A table's kind is read from its header row: a header carrying `quote`
    opens the admit table, one carrying `reason` opens the reject table.
    """
    rows = table_rows(lines)
    admit, reject = {}, []
    kind = None
    for row in rows:
        cells = [c.lower() for c in row_cells(row)]
        if cells and all(re.fullmatch(r":?-{2,}:?", c) for c in cells):
            continue                        # the table's separator row
        if any("quote" in c for c in cells) and any(
                "verdict" in c or "admit" in c for c in cells):
            kind = "admit"
            continue
        if any("reason" in c for c in cells) and any("flip" in c for c in cells):
            kind = "reject"
            continue
        if kind == "admit":
            ids = TOKEN_RE.findall(row)
            if ids:
                admit.setdefault(ids[0], []).append(row)
        elif kind == "reject":
            reject.append(row)
    return admit, reject


def _gate_access_date(lines):
    for line in lines:
        m = re.search(r"(?i)access[- ]date[:\s]+(\d{4}-\d{2}-\d{2})", line)
        if m:
            return m.group(1)
    return None


# ------------------------------------------------------------------- legs ---

def leg_frozencfg(ctx):
    """FROZENCFG: the frozen claims.json is the config, byte-identical at
    <lands>, stamped round-77/frozen on the frozen base, its by-document map blob
    (when declared) matches its digest, and the graded checkout IS <lands>."""
    root, mat, cfg = ctx["root"], ctx["mat"], ctx["cfg"]
    lands = ctx["lands"]
    bad = []
    try:
        lands_claims = git_bytes(root, "show", "%s:%s" % (lands, CLAIMS))
    except Exception:
        lands_claims = None
    if lands_claims is None or lands_claims.returncode != 0:
        bad.append("%s missing at lands" % CLAIMS)
    else:
        got = hashlib.sha256(lands_claims.stdout).hexdigest()
        if got != cfg["frozen_sha256"]:
            bad.append("graded-tree %s (sha256 %s) differs from the freeze blob "
                       "(%s): a counter config edited in the graded tree is a "
                       "junk landing" % (CLAIMS, got[:16],
                                         cfg["frozen_sha256"][:16]))
    if not is_ancestor(root, cfg["base"], lands):
        bad.append("claim base %s is not a strict ancestor of lands %s"
                   % (cfg["base"][:12], lands[:12]))
    doc_round = cfg.get("doc_round")
    if not (doc_round == ROUND or str(doc_round) == str(ROUND)):
        bad.append("frozen claims document round=%r (want %d)"
                   % (doc_round, ROUND))
    if cfg.get("doc_status").strip().lower() != "frozen":
        bad.append("frozen claims document status=%r (want frozen)"
                   % cfg.get("doc_status"))
    frozen = cfg.get("doc_frozen")
    if isinstance(frozen, bool):
        if not frozen:
            bad.append("frozen claims document carries frozen=false")
    elif isinstance(frozen, str) and re.fullmatch(r"[0-9a-f]{40}", frozen.lower()):
        if frozen.lower() != cfg["freeze"]:
            bad.append("frozen claims document is stamped %s, not the freeze %s"
                       % (frozen[:12], cfg["freeze"][:12]))
    elif frozen is not None:
        bad.append("frozen claims document carries an unreadable frozen stamp: %r"
                   % (frozen,))
    want_tree = git(root, "rev-parse", "%s^{tree}" % lands).stdout.strip()
    if os.path.isdir(os.path.join(mat, ".git")):
        head = git(mat, "rev-parse", "HEAD").stdout.strip()
        tree = git(mat, "rev-parse", "HEAD^{tree}").stdout.strip()
        if head != lands:
            bad.append("graded checkout HEAD %s != lands %s"
                       % (head[:12], lands[:12]))
        if tree != want_tree:
            bad.append("graded checkout tree %s != lands tree %s"
                       % (tree[:12], want_tree[:12]))
    else:
        listed = git(root, "ls-tree", "-r", "--name-only", lands).stdout.split()
        present = tree_files(mat, ".")
        if sorted(listed) != sorted(present):
            bad.append("archive materialization carries %d file(s); lands "
                       "carries %d" % (len(present), len(listed)))
    r = git_bytes(root, "show", "%s:%s" % (cfg["freeze"], cfg["map_path"])) \
        if cfg["map_path"] else None
    if r is not None and r.returncode != 0:
        bad.append("map %s unreadable at freeze %s"
                   % (cfg["map_path"], cfg["freeze"][:12]))
    elif r is not None:
        got = hashlib.sha256(r.stdout).hexdigest()
        if got != cfg["map_sha256"]:
            bad.append("map %s sha256 %s != the frozen %s"
                       % (cfg["map_path"], got[:16], cfg["map_sha256"][:16]))
    detail = ("frozen sha=%s base=%s lands=%s tree=%s map=%s"
              % (cfg["frozen_sha256"][:16], cfg["base"][:12],
                 lands[:12], want_tree[:12], cfg["map_path"] or "(none declared)"))
    if bad:
        detail = "; ".join(dedupe(bad)) + " | " + detail
    return leg("FROZENCFG", not bad, detail[:300])


def leg_repointed(ctx):
    """REPOINTED: every `source:` line of the admitted entry carries exactly one
    id whose row URL names that document; every inline S-id resolves to a frozen
    lane row or a base-held row; no removed legacy id and no campaign-namespace
    id is cited as a lane row (r77 draft: rewrite, do not copy)."""
    mat, mat_base, cfg = ctx["mat"], ctx["mat_base"], ctx["cfg"]
    try:
        base_rows = parse_rows(read_tree(mat_base, REGISTRY))
        lands_rows = parse_rows(read_tree(mat, REGISTRY))
    except Missing as e:
        return leg("REPOINTED", False, "registry unreadable: %s" % e)
    lane = set(cfg["rows"])
    staged = set(cfg.get("staged_universe") or ())
    legacy = set(cfg.get("removed_ids") or ())
    bad = []
    seen_source_lines = 0
    cited_on_source_lines = set()
    for path in cfg["entries"]:
        try:
            text = read_tree(mat, path)
        except Missing:
            bad.append("%s missing at lands" % path)
            continue
        for sline in source_field_lines(text):
            seen_source_lines += 1
            ids = TOKEN_RE.findall(sline)
            cited_on_source_lines |= set(ids)
            if len(ids) != 1:
                bad.append("%s `source:` line carries %d id(s) (want exactly "
                           "one): %r" % (path, len(ids), sline[:60]))
                continue
            sid = ids[0]
            if sid in legacy:
                bad.append("%s cites the removed legacy id %s" % (path, sid))
            if sid in lane:
                row = lands_rows.get(sid)
                doc_keys = set()
                if row is not None:
                    cells = row_cells(row)
                    if len(cells) > SOURCE:
                        doc_keys = set(_doc_url_key(u)
                                       for u in urls_in(cells[SOURCE]))
                line_keys = set(_doc_url_key(u) for u in urls_in(sline))
                if not line_keys:
                    bad.append("%s source line for %s names no URL"
                               % (path, sid))
                elif not (line_keys & doc_keys):
                    bad.append("%s source line for %s names a document its row "
                               "does not carry" % (path, sid))
            elif sid in base_rows:
                cells = row_cells(base_rows[sid])
                row_keys = set(_doc_url_key(u)
                               for u in urls_in(cells[SOURCE])) \
                    if len(cells) > SOURCE else set()
                line_keys = set(_doc_url_key(u) for u in urls_in(sline))
                if not line_keys:
                    bad.append("%s source line for the base-held %s names no URL"
                               % (path, sid))
                elif not (line_keys & row_keys):
                    bad.append("%s source line for the base-held %s names a "
                               "document that row does not carry" % (path, sid))
            else:
                bad.append("%s cites %s, which is neither a frozen lane row nor "
                           "a base-held row" % (path, sid))
        for sid in sorted(set(TOKEN_RE.findall(text))):
            if sid in legacy:
                if sid not in cited_on_source_lines:
                    bad.append("%s keeps the removed legacy id %s" % (path, sid))
            elif sid in lane or sid in base_rows:
                continue
            elif sid in staged:
                bad.append("%s cites the campaign-namespace id %s as a lane row"
                           % (path, sid))
            else:
                bad.append("%s carries the unresolved id %s" % (path, sid))
    if not seen_source_lines:
        bad.append("no admitted entry carries a `source:` line")
    detail = ("source lines=%d lane rows=%s removed=%s staged universe=%d"
              % (seen_source_lines, ",".join(cfg["rows"]),
                 ",".join(sorted(legacy)) or "-", len(staged)))
    if bad:
        detail = "; ".join(dedupe(bad)) + " | " + detail
    return leg("REPOINTED", not bad, detail[:300])


def leg_entries(ctx):
    """ENTRIES: the admitted entry, its provenance header, section, body floor
    and its citations of mined rows."""
    mat, mat_base, cfg = ctx["mat"], ctx["mat_base"], ctx["cfg"]
    bad = []
    floor = _min_entry_words(mat_base)
    cited_bad = []
    cited = _entry_citations(mat, cfg["entries"], cited_bad)
    bad.extend(cited_bad)
    try:
        lands_rows = parse_rows(read_tree(mat, REGISTRY))
    except Missing:
        lands_rows = {}
    for path in cfg["entries"]:
        if os.path.isdir(os.path.join(mat, path)):
            bad.append("%s is a directory at lands" % path)
            continue
        try:
            text = read_tree(mat, path)
        except Missing:
            bad.append("%s missing at lands" % path)
            continue
        if os.path.exists(os.path.join(mat_base, path)):
            bad.append("%s already exists at base (an entry must be new)" % path)
        values = _header_values(text)
        for field in HEADER_FIELDS:
            key = norm_label(field)
            if key not in values:
                bad.append("%s header carries no `%s:` field" % (path, field))
                continue
            value = values[key]
            if _placeholder_value(value):
                bad.append("%s header `%s:` is a placeholder (%r)"
                           % (path, field, value[:40]))
            elif ANGLE_RE.search(value):
                bad.append("%s header `%s:` carries an angle marker (%r)"
                           % (path, field, value[:40]))
        if not re.search(r"^##\s", text, re.M):
            bad.append("%s carries no `## ` section" % path)
        words = _body_words(text)
        if words < floor:
            bad.append("%s body holds %d word(s); the smallest base entry holds "
                       "%d" % (path, words, floor))
        ids = sorted(sid for sid, paths in cited.items() if path in paths)
        if not ids:
            bad.append("%s cites no registry row on its `source:` line(s)" % path)
        for sid in ids:
            if sid not in lands_rows:
                bad.append("%s cites %s, which no landed row carries"
                           % (path, sid))
            elif len(row_cells(lands_rows[sid])) > STATUS \
                    and row_cells(lands_rows[sid])[STATUS] != "mined":
                bad.append("%s cites %s, whose status is not mined"
                           % (path, sid))
    base_md = _md_count(mat_base, KNOWLEDGE)
    lands_md = _md_count(mat, KNOWLEDGE)
    want_md = cfg["knowledge_before"] + len(cfg["entries"])
    if base_md != cfg["knowledge_before"]:
        bad.append("base knowledge tree holds %d .md file(s); the freeze "
                   "declares %d" % (base_md, cfg["knowledge_before"]))
    if lands_md != want_md:
        bad.append("lands knowledge tree holds %d .md file(s); %d+n with n=%d "
                   "is %d" % (lands_md, cfg["knowledge_before"],
                              len(cfg["entries"]), want_md))
    if cfg.get("knowledge_after") is not None \
            and cfg["knowledge_after"] != want_md:
        bad.append("the freeze declares knowledge_after=%d but "
                   "knowledge_before+n is %d"
                   % (cfg["knowledge_after"], want_md))
    base_files = set(p for p in tree_files(mat_base, KNOWLEDGE)
                     if p.endswith(".md"))
    lands_files = set(p for p in tree_files(mat, KNOWLEDGE) if p.endswith(".md"))
    added = sorted(lands_files - base_files)
    removed = sorted(base_files - lands_files)
    if set(added) != set(cfg["entries"]):
        bad.append("knowledge .md files added %s (want the frozen entries %s)"
                   % (added, cfg["entries"]))
    if removed:
        bad.append("knowledge .md files removed %s" % removed)
    detail = "entries=%d min=%d floor=%d words=%s knowledge %d->%d added=%s" % (
        len(cfg["entries"]), cfg["min_entries"], floor,
        "/".join(str(_body_words(read_tree(mat, p)))
                 for p in cfg["entries"]
                 if os.path.isfile(os.path.join(mat, p))) or "-",
        base_md, lands_md, added or "-")
    if bad:
        detail = "; ".join(dedupe(bad)) + " | " + detail
    return leg("ENTRIES", not bad, detail[:300])


def _rows_cadence_ok(cell):
    value = (cell or "").strip().lower()
    if not value or value in DASHES or "|" in value:
        return False
    return bool(re.fullmatch(r"(?:\d+d|on-[a-z][a-z0-9-]*|on release|"
                             r"quarterly|annual|semi-?annual|monthly|weekly|"
                             r"yearly|per-edition)", value))


def leg_rows(ctx):
    """ROWS (r76 defect 1 fixed): ONLY `| S### |` row line additions are
    counted, and only the frozen row_set's ids may be added.  Added non-row
    lines are invisible here (INDEX grades the required sections)."""
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

    new_ids = [sid for sid in lands_rows if sid not in base_rows]
    if sorted(new_ids) != sorted(want):
        bad.append("row ids added %s (want the frozen row_set %s)"
                   % (sorted(new_ids), want))
    k = len(want)
    if len(base_rows) != cfg["rows_before"]:
        bad.append("base registry holds %d row(s); the freeze declares %d"
                   % (len(base_rows), cfg["rows_before"]))
    want_rows = cfg["rows_before"] + k
    if len(lands_rows) != want_rows:
        bad.append("lands registry holds %d row(s); %d+k with k=%d is %d"
                   % (len(lands_rows), cfg["rows_before"], k, want_rows))
    if cfg.get("rows_after") is not None and cfg["rows_after"] != want_rows:
        bad.append("the freeze declares rows_after=%d but rows_before+k is %d"
                   % (cfg["rows_after"], want_rows))
    # pre-existing rows: only the registry contract's rule-2 cells (status,
    # recheck, used-by) may change in place; no removal, no reordering.
    rule2 = (STATUS, RECHECK, USEDBY)
    order = list(base_rows)
    lands_order = [sid for sid in lands_rows if sid in base_rows]
    if lands_order != [sid for sid in order if sid in lands_rows]:
        bad.append("pre-existing rows are reordered at lands")
    for sid, brow in base_rows.items():
        if sid not in lands_rows:
            bad.append("pre-existing row %s is removed" % sid)
            continue
        bcell, lcell = row_cells(brow), row_cells(lands_rows[sid])
        if len(bcell) != NCELLS or len(lcell) != NCELLS:
            if brow != lands_rows[sid]:
                bad.append("pre-existing row %s is edited" % sid)
            continue
        changed = [i for i in range(NCELLS) if bcell[i] != lcell[i]]
        outside = [i for i in changed if i not in rule2]
        if outside:
            bad.append("pre-existing row %s changes cell(s) %s outside the "
                       "rule-2 set" % (sid, outside))
    line_counts = Counter(l for l in lands_text.splitlines() if ROW_RE.match(l))
    duplicates = sorted(sid for sid in want
                        if lands_rows.get(sid) is not None
                        and line_counts.get(lands_rows[sid], 0) > 1)
    if duplicates:
        bad.append("a frozen row line is present twice: %s" % duplicates)

    cited = _entry_citations(mat, cfg["entries"], bad)
    for sid in want:
        row = lands_rows.get(sid)
        if row is None:
            bad.append("%s missing at lands" % sid)
            continue
        if "\\|" in row:
            bad.append("%s row carries an escaped pipe (a staged cell appended "
                       "as-is)" % sid)
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
        live, caps = _doc_pair(cells[SOURCE])
        if not live:
            bad.append("%s source cell names no live URL" % sid)
        if not caps:
            bad.append("%s source cell names no same-page Wayback capture "
                       "(QUALITY 18)" % sid)
        if live and caps and not any(
                _doc_url_key(a) == _doc_url_key(b)
                for a in live for b in caps):
            bad.append("%s live URL and captured original are not the same "
                       "document" % sid)
        ev = _evidence(mat, sid)
        if ev is None:
            bad.append("%s has no committed evidence file (%s/%s.txt)"
                       % (sid, EVIDENCE_DIR, sid))
            continue
        quotes = [s for s in quoted_spans(row) if quote_ok(s)]
        if not quotes:
            bad.append("%s row anchor carries no <=25-token, <=80-char quote"
                       % sid)
            continue
        anchor = nfkc_ws(cells[ANCHOR])
        if not any(_evidence_fold(q) and _evidence_fold(q) in anchor
                   for q in quotes):
            bad.append("%s anchor cell does not contain its located quote" % sid)
    detail = "added ids=%s want=%s" % (sorted(new_ids), want)
    if bad:
        detail = "; ".join(dedupe(bad)) + " | " + detail
    return leg("ROWS", not bad, detail[:300])


def leg_citedlines(ctx):
    """CITEDLINES: tools/check-cited-lines.py over the admitted entries prints
    `CITED-LINES: 0 finding(s)` (one id scopes one clause; no table row hides a
    citation).  The tool is the one committed at <lands>."""
    mat, cfg = ctx["mat"], ctx["cfg"]
    entries = list(cfg["entries"])
    tool = os.path.join(mat, "tools/check-cited-lines.py")
    if not os.path.isfile(tool):
        return leg("CITEDLINES", False, "tools/check-cited-lines.py missing at lands")
    bad, paths = [], []
    for e in entries:
        full = os.path.join(mat, e)
        if os.path.isfile(full):
            paths.append(full)
        else:
            bad.append("%s missing" % e)
    if not paths:
        return leg("CITEDLINES", False, "; ".join(dedupe(bad)) or "no entry")
    try:
        r = subprocess.run([sys.executable, "-B", tool] + paths,
                           capture_output=True, text=True, timeout=300)
    except (OSError, subprocess.SubprocessError) as e:
        return leg("CITEDLINES", False, "tool run failed: %s" % e)
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


def _map_records(records):
    """Normalise one by-document map record to {staged, lane, doc}."""
    staged = records.get("staged_id") if "staged_id" in records \
        else records.get("staged") or records.get("from")
    lane = records.get("lane_id") if "lane_id" in records \
        else records.get("new_target") or records.get("lane") \
        or records.get("to") or records.get("target")
    doc = (records.get("document_url") or records.get("url")
           or records.get("document") or records.get("normalized_document_url")
           or "")
    staged_ids = [s.upper() for s in re.split(r"[/,;\s]+", str(staged or ""))
                  if TOKEN_RE.fullmatch(s.upper())]
    lane_id = str(lane or "").strip().upper()
    doc_urls = list(doc) if isinstance(doc, (list, tuple)) else [str(doc)]
    if not doc and isinstance(records.get("staged_url_cell_urls"), list):
        doc_urls = [str(u) for u in records["staged_url_cell_urls"]]
    return staged_ids, lane_id, [u for u in doc_urls if u]


def _map_pairs(ctx):
    """{staged id: [{lane, docs}]} from the pinned freeze map; None when absent."""
    root, cfg = ctx["root"], ctx["cfg"]
    r = git_bytes(root, "show", "%s:%s" % (cfg["freeze"], cfg["map_path"]))
    if r.returncode != 0:
        return None
    try:
        doc = json.loads(r.stdout.decode("utf-8"))
    except (ValueError, UnicodeDecodeError):
        return None
    records = []
    if isinstance(doc, dict):
        for key in ("assignments", "records", "rows", "map"):
            if isinstance(doc.get(key), list):
                records = doc[key]
                break
        if not records and isinstance(doc.get("map"), dict):
            records = [dict({"staged_id": k}, **v) if isinstance(v, dict)
                       else {"staged_id": k, "new_target": v}
                       for k, v in doc["map"].items()]
    if not isinstance(records, list):
        return None
    out = {}
    for rec in records:
        if not isinstance(rec, dict):
            continue
        staged_ids, lane_id, doc_urls = _map_records(rec)
        for sid in staged_ids:
            out.setdefault(sid, []).append({"lane": lane_id, "docs": doc_urls})
    return out


def leg_collcheck(ctx):
    """COLLCHECK (r76 defect 2 fixed): DOCUMENT identity of the frozen
    document_url against the row's source cell, plus the pinned staged->lane
    map agreeing with both sides.  Never a raw URL-string comparison."""
    mat, cfg = ctx["mat"], ctx["cfg"]
    try:
        lands_rows = parse_rows(read_tree(mat, REGISTRY))
    except Missing as e:
        return leg("COLLCHECK", False, "registry unreadable: %s" % e)
    bad = []
    pairs = _map_pairs(ctx) if cfg["map_path"] else None
    if cfg["map_path"] and pairs is None:
        bad.append("the pinned by-document map %s is absent or unreadable at "
                   "freeze %s" % (cfg["map_path"], cfg["freeze"][:12]))
    for sid in cfg["rows"]:
        frozen_doc = cfg["row_doc"][sid]
        frozen_key = _doc_url_key(frozen_doc)
        row = lands_rows.get(sid)
        if row is None:
            bad.append("%s row missing at lands (no source cell to compare)" % sid)
            continue
        cells = row_cells(row)
        if len(cells) <= SOURCE:
            bad.append("%s row carries no source cell" % sid)
            continue
        source = cells[SOURCE]
        source_urls = urls_in(source)
        if not source_urls:
            bad.append("%s source cell names no URL at all (the document is "
                       "only described in prose)" % sid)
            continue
        keys = set(_doc_url_key(u) for u in source_urls)
        if frozen_key not in keys:
            bad.append("%s source cell names a different document than the "
                       "frozen %s%s (document identity, not a raw string)"
                       % (sid, frozen_key[0], frozen_key[1]))
        if pairs is not None:
            for staged in cfg["row_staged"][sid]:
                recs = pairs.get(staged) or []
                if not recs:
                    bad.append("the map carries no record for staged %s"
                               % staged)
                    continue
                if not any(rec["lane"] == sid for rec in recs):
                    bad.append("the map's staged %s targets %s, not lane %s"
                               % (staged,
                                  ",".join(sorted(set(r["lane"] for r in recs))),
                                  sid))
                if not any(_doc_url_key(u) == frozen_key
                           for rec in recs for u in rec["docs"]):
                    bad.append("the map's staged %s names no document matching "
                               "the frozen %s%s"
                               % (staged, frozen_key[0], frozen_key[1]))
    detail = "rows=%s map=%s" % (",".join(cfg["rows"]), cfg["map_path"])
    if bad:
        detail = "; ".join(dedupe(bad)) + " | " + detail
    return leg("COLLCHECK", not bad, detail[:300])


def leg_index(ctx):
    """INDEX: the README index row for the admitted entry in its partition,
    every heading against the live count, the last footer true to the tree,
    older footers preserved; plus the `required_sections[]` non-row edits."""
    mat, mat_base, cfg = ctx["mat"], ctx["mat_base"], ctx["cfg"]
    bad = []
    try:
        lands_text = read_tree(mat, README)
    except Missing:
        return leg("INDEX", False, "%s missing at lands" % README)
    try:
        base_text = read_tree(mat_base, README)
    except Missing:
        base_text = ""

    entries = list(cfg["entries"])
    names = [os.path.basename(e) for e in entries]
    lines = lands_text.splitlines()
    sections = _readme_sections(lands_text)
    parts = [p for p, _s, _e in sections]
    heading_counts = {}
    for h in README_SECTION_RE.finditer(lands_text):
        heading_counts[h.group(1)] = int(h.group(2))

    entry_parts = set()
    for e in entries:
        m = re.match(r"^%s/([^/]+)/[^/]+\.md$" % re.escape(KNOWLEDGE), e)
        if not m:
            bad.append("%s is not an entry path inside a knowledge partition" % e)
            continue
        entry_parts.add(m.group(1))
    if len(entry_parts) > 1:
        bad.append("the admitted entries sit in %d partitions (%s); the index "
                   "rows are graded in one"
                   % (len(entry_parts), ",".join(sorted(entry_parts))))
    part = sorted(entry_parts)[0] if len(entry_parts) == 1 else None
    target = [s for s in sections if s[0] == part] if part else []
    if part and not target:
        bad.append("%s has no `## %s/ (N)` section" % (README, part))
    if target:
        _p, part_start, part_end = target[0]
        first = lands_text.count("\n", 0, part_start)
        last = lands_text.count("\n", 0, part_end)
    else:
        first = last = -1

    for path, name in zip(entries, names):
        try:
            text = read_tree(mat, path)
        except Missing:
            bad.append("%s missing at lands" % path)
            continue
        topic = _entry_topic(text)
        if not topic:
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
            bad.append("%s index row is not inside the %s section"
                       % (name, part or "entry-partition"))
        if topic and body != topic:
            bad.append("%s index row is not the entry's `- topic:` text verbatim"
                       % name)

    live_parts = [_md_count(mat, KNOWLEDGE + "/" + p) for p in parts]
    for heading, count in sorted(heading_counts.items()):
        live = _md_count(mat, KNOWLEDGE + "/" + heading)
        if count != live:
            bad.append("%s heading (%d) != the %d live .md files in "
                       "corpus/knowledge/%s" % (heading, count, live, heading))

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
            if len(vector) != len(parts):
                bad.append("%s declares %d partition sections but the footer "
                           "vector %s holds %d value(s)"
                           % (README, len(parts),
                              "/".join(str(v) for v in vector), len(vector)))
            if vector != tuple(live_parts):
                bad.append("last footer vector %s != the live partition counts "
                           "%s" % ("/".join(str(v) for v in vector),
                                   "/".join(str(v) for v in live_parts)))
    pos = 0
    for blk in base_blocks:
        while pos < len(lands_blocks) and lands_blocks[pos] != blk:
            pos += 1
        if pos >= len(lands_blocks):
            bad.append("an older `Counts checked` footer is not preserved "
                       "byte-identically: %r" % blk.splitlines()[0][:60])
            break
        pos += 1

    # the exemption set: the last footer block, partition-count headings, and
    # the admitted entries' own index rows.  Everything else that changed fails.
    exempt = set()
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
        if back >= 0 and not lines[back].strip():
            back -= 1
        if back >= 0 and lines[back].startswith("Total knowledge entries:"):
            lo = back
            back -= 1
        if back >= 0 and not lines[back].strip():
            lo = back
        exempt.update(range(lo, hi + 1))
    base_occ = Counter(base_text.splitlines())
    lands_occ = Counter(lines)
    adopted = set(names)
    try:
        base_knowledge = set(os.path.basename(p)
                             for p in tree_files(mat_base, KNOWLEDGE))
    except OSError:
        base_knowledge = set()
    for k, line in enumerate(lines):
        if lands_occ[line] <= base_occ.get(line, 0):
            continue
        if k in exempt:
            continue
        m = README_SECTION_RE.match(line)
        if m and m.group(1) in parts:
            exempt.add(k)
            continue
        rm = README_ROW_RE.match(line)
        if rm and (rm.group(1) in adopted or rm.group(1) in base_knowledge):
            exempt.add(k)
            continue
        if not line.strip():
            exempt.add(k)
            continue
        bad.append("README line %d added outside the exemption set: %r"
                   % (k + 1, line[:70]))
    for line, count in base_occ.items():
        if not line.strip() or lands_occ.get(line, 0) >= count:
            continue
        m = README_SECTION_RE.match(line)
        if m:
            continue                       # count parenthetical may be replaced
        bad.append("README line removed/edited outside the exemption set: %r"
                   % line[:70])

    # R5 + r76 defect 1: the required non-row edits are checked HERE, and are
    # never counted as out-of-set rows.
    for spec in cfg["required_sections"]:
        targets = [spec["path"]] if spec["path"] else list(entries)
        for target in targets:
            try:
                text = read_tree(mat, target)
            except Missing:
                bad.append("required_sections target %s missing at lands" % target)
                continue
            hits = sum(1 for line in text.splitlines()
                       if re.search(spec["pattern"], line))
            if hits < spec["min"]:
                bad.append("required section %r missing from %s (%d < %d)"
                           % (spec["label"], target, hits, spec["min"]))
    detail = ("%s: %d section(s), %s=%s, last footer total=%s vector=%s, "
              "%d adopted row(s), %d required section(s)"
              % (README, len(parts), part or "-",
                 heading_counts.get(part) if part else "-",
                 shown_total, shown_vec, len(names),
                 len(cfg["required_sections"])))
    if bad:
        reasons = dedupe(bad)
        if len(reasons) > 4:
            reasons = reasons[:4] + ["(+%d more)" % (len(reasons) - 4)]
        detail = "; ".join(reasons) + " | " + detail
    return leg("INDEX", not bad, detail[:300])


def leg_evidence(ctx):
    """EVIDENCE: a committed capture per row whose stored bytes re-derive its
    own scope/digest and hold the Gate quote (no self-attested flag is read)."""
    mat, cfg = ctx["mat"], ctx["cfg"]
    try:
        gate_lines = gate_section(read_tree(mat, LESSON))
    except Missing as e:
        return leg("EVIDENCE", False, "%s" % e)
    admit, _rejects = _gate_tables(gate_lines)
    bad = []
    for sid in cfg["rows"]:
        ev = _evidence(mat, sid)
        if ev is None:
            bad.append("%s evidence file missing (%s/%s.txt)"
                       % (sid, EVIDENCE_DIR, sid))
            continue
        status = (ev.get("http-status") or ev.get("http") or "").strip()
        if status != "200":
            bad.append("%s http-status %r (want 200)" % (sid, status))
        if ev.get("access-date") != cfg["access_date"]:
            bad.append("%s access-date %r (want %s)"
                       % (sid, ev.get("access-date"), cfg["access_date"]))
        size = _evidence_count(ev.get("bytes"))
        if size is None or size <= 0:
            bad.append("%s bytes %r is not a positive byte count"
                       % (sid, (ev.get("bytes") or "")[:20]))
        digest = (ev.get("sha256") or "").strip().lower()
        if not re.fullmatch(r"[0-9a-f]{64}", digest):
            bad.append("%s sha256 line is not a 64-hex body digest" % sid)
        ua = (ev.get("user-agent") or ev.get("ua") or "").strip()
        if not ua:
            bad.append("%s records no user-agent (QUALITY 22)" % sid)
        fetch = (ev.get("fetch") or ev.get("url") or "").strip()
        if not fetch:
            bad.append("%s carries no fetch line" % sid)
        else:
            frozen_key = _doc_url_key(cfg["row_doc"][sid])
            if frozen_key not in _evidence_doc_keys(ev):
                bad.append("%s fetch line does not name the frozen document "
                           "(%s%s)" % (sid, frozen_key[0], frozen_key[1]))
        challenge = ev.get("challenge")
        if challenge is not None \
                and challenge.strip().lower() not in CLEAN_CHALLENGE:
            bad.append("%s records a served challenge (%r): a challenge met is "
                       "an UNOPENED source" % (sid, challenge.strip()[:40]))
        src = (ev.get("claims-source") or "").strip()
        if not src:
            bad.append("%s evidence carries no claims-source stamp" % sid)
        elif cfg["freeze"] not in src and cfg["freeze"][:12] not in src:
            bad.append("%s evidence claims-source does not name the freeze (%s)"
                       % (sid, src[:60]))
        if (ev.get("claims-frozen") or "").strip().lower() != "yes":
            bad.append("%s evidence does not declare claims-frozen: yes" % sid)
        window = ev["_window"]
        if window is None:
            bad.append("%s stores no --- window --- block" % sid)
            continue
        payload = window.encode("utf-8")
        declared = (ev.get("window-sha256") or "").strip().lower()
        if declared != hashlib.sha256(payload).hexdigest():
            bad.append("%s window-sha256 does not re-derive from the stored "
                       "window" % sid)
        declared_bytes = (ev.get("window-bytes") or "").strip()
        if declared_bytes and declared_bytes != str(len(payload)):
            bad.append("%s window-bytes %r != the stored window's %d bytes"
                       % (sid, declared_bytes, len(payload)))
        scope = (ev.get("window-scope") or "").strip().lower()
        visible = _evidence_count(ev.get("visible-chars"))
        if scope not in ("excerpt", "whole-document"):
            bad.append("%s window-scope %r (want excerpt|whole-document)"
                       % (sid, (ev.get("window-scope") or "")[:30]))
        elif scope == "excerpt":
            if len(window) < MIN_WINDOW_CHARS:
                bad.append("%s excerpt window is %d characters (want >= %d)"
                           % (sid, len(window), MIN_WINDOW_CHARS))
        else:
            if visible is None:
                bad.append("%s whole-document window records no visible-chars"
                           % sid)
            elif visible != len(window):
                bad.append("%s whole-document window is %d characters but "
                           "visible-chars is %d" % (sid, len(window), visible))
        folded = _evidence_fold(window)
        if not folded:
            bad.append("%s stored window carries no visible text" % sid)
            continue
        quotes = _evidence_gate_quotes(admit, sid)
        if not quotes:
            bad.append("%s has no Gate admit row carrying a <=25-token, <=80-char "
                       "quote" % sid)
            continue
        if not any(q in folded for q in quotes):
            bad.append("%s Gate quote is absent from the stored window" % sid)
    detail = "rows=%s windows=%s" % (
        ",".join(cfg["rows"]),
        ",".join(str(len(_evidence(mat, sid)["_window"] or ""))
                 for sid in cfg["rows"] if _evidence(mat, sid)))
    if bad:
        detail = "; ".join(dedupe(bad)) + " | " + detail
    return leg("EVIDENCE", not bad, detail[:300])


def leg_gate(ctx):
    """GATE: `## Gate` names each new row with URL, access date, a located
    <=25-token / <=80-character quote and its evidence path."""
    mat, cfg = ctx["mat"], ctx["cfg"]
    try:
        text = read_tree(mat, LESSON)
    except Missing as e:
        return leg("GATE", False, "%s" % e)
    lines = gate_section(text)
    bad = []
    if not lines:
        return leg("GATE", False, "%s carries no `## Gate` section" % LESSON)
    date = _gate_access_date(lines)
    if date != cfg["access_date"]:
        bad.append("the Gate section declares access date %r (want %s)"
                   % (date, cfg["access_date"]))
    admit, _rejects = _gate_tables(lines)
    for sid in cfg["rows"]:
        rows = admit.get(sid) or []
        if not rows:
            bad.append("%s has no Gate admit row" % sid)
            continue
        shown = False
        for row in rows:
            spans = [s for s in quoted_spans(row) if quote_ok(s)]
            if not spans:
                bad.append("%s Gate admit row carries no <=25-token, <=80-char "
                           "quote" % sid)
                continue
            if cfg["access_date"] not in row:
                bad.append("%s Gate admit row carries no access date" % sid)
                continue
            frozen_key = _doc_url_key(cfg["row_doc"][sid])
            if frozen_key not in set(_doc_url_key(u) for u in urls_in(row)):
                bad.append("%s Gate admit row names no URL of the frozen "
                           "document" % sid)
                continue
            ev_path = "%s/%s.txt" % (EVIDENCE_DIR, sid)
            if ev_path not in row:
                bad.append("%s Gate admit row names no evidence path (%s)"
                           % (sid, ev_path))
                continue
            shown = True
            break
        if not shown and not bad:
            bad.append("%s Gate admit row could not be verified" % sid)
    detail = "gate rows=%s admit=%d" % (",".join(cfg["rows"]), len(admit))
    if bad:
        detail = "; ".join(dedupe(bad)) + " | " + detail
    return leg("GATE", not bad, detail[:300])


def leg_rejects(ctx):
    """REJECTS: >=1 admit and >=1 reject from the assimilation set; the frozen
    refused staged ids are in the Gate reject table with reason+flip and are
    never lane rows; declared triage counts sum."""
    mat, cfg = ctx["mat"], ctx["cfg"]
    try:
        text = read_tree(mat, LESSON)
        lands_rows = parse_rows(read_tree(mat, REGISTRY))
    except Missing as e:
        return leg("REJECTS", False, "%s" % e)
    lines = gate_section(text)
    bad = []
    if not lines:
        return leg("REJECTS", False, "%s carries no `## Gate` section" % LESSON)
    _admit, reject_rows = _gate_tables(lines)
    if not reject_rows:
        bad.append("the Gate carries no reject row")
    reject_text = "\n".join(reject_rows)
    for row in reject_rows:
        cells = row_cells(row)
        if not urls_in(row):
            bad.append("a Gate reject row carries no probed URL: %r" % row[:70])
        tail = [c for c in cells if c][-3:]
        if len(tail) < 3:
            bad.append("a Gate reject row carries no reason+flip pair: %r"
                       % row[:70])
        else:
            reason, flip = tail[0], tail[1]
            if reason.strip().lower() in DASHES:
                bad.append("a Gate reject row carries a dash reason: %r"
                           % row[:70])
            if flip.strip().lower() in DASHES:
                bad.append("a Gate reject row carries a dash flip: %r"
                           % row[:70])
    if not cfg["refused_staged"]:
        bad.append("the freeze declares no refused staged id (an assimilation "
                   "set with no reject cannot show taste)")
    for sid in cfg["refused_staged"]:
        if sid not in reject_text:
            bad.append("refused staged %s is not recorded in the Gate reject "
                       "table" % sid)
        if sid in lands_rows:
            bad.append("refused staged %s was appended as a lane row" % sid)
    adopted = len(cfg["entries"])
    counts = cfg["counts"]
    if counts:
        if counts.get("adopted") is not None and counts["adopted"] != adopted:
            bad.append("rejects.counts.adopted=%d != the %d admitted entry(ies)"
                       % (counts["adopted"], adopted))
        refused = counts.get("refused")
        if refused is not None and refused < 1:
            bad.append("rejects.counts.refused=%d (want >= 1)" % refused)
        total = counts.get("total_staged_files")
        if refused is not None and total is not None:
            parts_sum = adopted + refused
            path_present = counts.get("path_present")
            if path_present is not None:
                parts_sum += path_present
            if parts_sum != total:
                bad.append("triage counts do not sum: %d != %d"
                           % (parts_sum, total))
    detail = ("admitted=%d refused_staged=%s reject rows=%d counts=%s"
              % (adopted, ",".join(cfg["refused_staged"]) or "-",
                 len(reject_rows),
                 ",".join("%s=%s" % (k, counts[k]) for k in sorted(counts)) or "-"))
    if bad:
        detail = "; ".join(dedupe(bad)) + " | " + detail
    return leg("REJECTS", not bad, detail[:300])


def leg_census(ctx):
    """CENSUS: `sources-census.sh validate --file <landed registry>` exits 0
    with no E-code line, dated with the frozen access date."""
    mat, cfg = ctx["mat"], ctx["cfg"]
    fleet_root = ctx["fleet_root"]
    script = os.path.join(fleet_root, "scripts/sources-census.sh")
    if not os.path.isfile(script):
        return leg("CENSUS", False, "census script not found: %s" % script)
    registry = os.path.join(mat, REGISTRY)
    if not os.path.isfile(registry):
        return leg("CENSUS", False, "registry missing at lands: %s" % REGISTRY)
    try:
        r = subprocess.run([script, "validate", "--file", registry,
                            "--today", cfg["access_date"]],
                           capture_output=True, text=True, timeout=900)
    except (OSError, subprocess.SubprocessError) as e:
        return leg("CENSUS", False, "census run failed: %s" % e)
    out = r.stdout or ""
    bad = []
    if r.returncode != 0:
        bad.append("census exit=%d" % r.returncode)
    ecodes = sorted(set(re.findall(r"(?m)^E\d\d\b", out)))
    if ecodes:
        bad.append("census TSV carries E-code line(s): %s" % ",".join(ecodes))
    tail = out.strip().splitlines()[-1] if out.strip() else ""
    detail = "exit=%d%s" % (r.returncode, (" last-line=%s" % tail) if tail else "")
    start = cfg.get("census_start")
    if start:
        try:
            text = read_tree(mat, start["path"])
        except Missing:
            bad.append("declared census-start receipt %s missing at lands"
                       % start["path"])
            text = None
        if text is not None:
            if start.get("rows") is not None \
                    and str(start["rows"]) not in text:
                bad.append("census-start receipt does not record %d row(s)"
                           % start["rows"])
            for m in re.finditer(r"(?im)^\s*exit\s*[:=]?\s*(\d+)\s*$", text):
                if m.group(1) != "0":
                    bad.append("census-start receipt records exit %s"
                               % m.group(1))
            for needle in start["contains"]:
                if needle not in text:
                    bad.append("census-start receipt does not carry %r" % needle)
        detail += "; start=%s" % start["path"]
    if bad:
        detail = "; ".join(dedupe(bad)) + " (" + detail + ")"
    return leg("CENSUS", not bad, detail[:300])


def leg_ground(ctx):
    """GROUND: each frozen sweep is absent at base (unconditionally) and
    present in the admitted entry; each fragment is absent from the base
    registry and present at lands."""
    mat, mat_base, cfg = ctx["mat"], ctx["mat_base"], ctx["cfg"]
    bad = []
    for sweep in cfg["sweeps"]:
        before = _grep_tree(mat_base, sweep["scope"], sweep["pattern"])
        if before:
            bad.append("sweep %r is already present at base in %s"
                       % (sweep["pattern"], ",".join(before[:3])))
        after = []
        for e in cfg["entries"]:
            try:
                txt = read_tree(mat, e)
            except Missing:
                continue
            if re.search(sweep["pattern"], txt):
                after.append(e)
        if not after:
            bad.append("sweep %r is absent from the admitted entry(ies)"
                       % sweep["pattern"])
    try:
        base_registry = read_tree(mat_base, REGISTRY)
        lands_registry = read_tree(mat, REGISTRY)
    except Missing as e:
        return leg("GROUND", False, "registry unreadable: %s" % e)
    lands_rows = parse_rows(lands_registry)
    row_sources = "\n".join(lands_rows[sid] for sid in cfg["rows"]
                            if sid in lands_rows)
    entry_text = "\n".join(read_tree(mat, e) for e in cfg["entries"]
                           if os.path.isfile(os.path.join(mat, e)))
    for frag in cfg["fragments"]:
        if frag in base_registry:
            bad.append("document fragment %r is already in the base registry"
                       % frag)
        if frag not in row_sources and frag not in entry_text:
            bad.append("document fragment %r is absent from the landed rows "
                       "and entries" % frag)
    receipt = cfg.get("ground_receipt")
    if receipt:
        try:
            text = read_tree(mat, receipt["path"])
        except Missing:
            bad.append("declared ground receipt %s missing at lands"
                       % receipt["path"])
            text = None
        if text is not None:
            for m in re.finditer(r"(?im)^\s*exit\s*[:=]?\s*(\d+)\s*$", text):
                if m.group(1) != "0":
                    bad.append("ground receipt records exit %s" % m.group(1))
            for needle in receipt["contains"]:
                if needle not in text:
                    bad.append("ground receipt does not carry %r" % needle)
    detail = "sweeps=%d fragments=%d receipt=%s" % (
        len(cfg["sweeps"]), len(cfg["fragments"]),
        (receipt or {}).get("path") or "-")
    if bad:
        detail = "; ".join(dedupe(bad)) + " | " + detail
    return leg("GROUND", not bad, detail[:300])


def _smirror_ids(mat, rel, bad):
    """An assimilation id list as a set (one S-id per line), or None."""
    try:
        text = read_tree(mat, rel)
    except Missing:
        bad.append("%s missing at lands" % rel)
        return None
    out = []
    for line in text.splitlines():
        value = line.strip().upper()
        if not value:
            continue
        if not TOKEN_RE.fullmatch(value):
            bad.append("%s carries a non-id line %r" % (rel, line[:40]))
            continue
        out.append(value)
    return set(out)


def leg_scratchmirror(ctx):
    """SCRATCHMIRROR: the staged-id universe and its collision guard are
    committed and re-derive from the BASE registry; the 1-3-space / 4-space
    indent guard proves both ways on committed bytes (r76's mirror leg, cut to
    the r77 assimilation artifacts)."""
    mat, mat_base, cfg = ctx["mat"], ctx["mat_base"], ctx["cfg"]
    assim = cfg["scratch_mirror"]["dir"]
    try:
        base_ids = set(parse_rows(read_tree(mat_base, REGISTRY)))
    except Missing as e:
        return leg("SCRATCHMIRROR", False, "base registry unreadable: %s" % e)
    bad = []
    reg = _smirror_ids(mat, assim + "/reg-ids", bad)
    staged = _smirror_ids(mat, assim + "/staged-ids", bad)
    coll = _smirror_ids(mat, assim + "/collisions", bad)
    if reg is not None:
        if reg != base_ids:
            bad.append("reg-ids (%d id(s)) != the base registry id set (%d)"
                       % (len(reg), len(base_ids)))
    if staged is not None:
        want_staged = set()
        for sids in cfg["row_staged"].values():
            want_staged |= set(sids)
        missing = sorted(want_staged - staged)
        if missing:
            bad.append("staged-ids omits the row_set staged id(s) %s"
                       % ",".join(missing))
    if reg is not None and staged is not None:
        collisions = sorted(reg & staged)
        if coll is None:
            pass
        elif sorted(coll) != collisions:
            bad.append("collisions %s != reg-ids ∩ staged-ids %s"
                       % (sorted(coll)[:6] or "-", collisions[:6] or "-"))
        adopted = sorted(set(cfg["rows"]) & reg)
        if adopted:
            bad.append("adopted lane id(s) %s already sit in reg-ids"
                       % ",".join(adopted))
    guard = assim + "/guard-proof"
    try:
        indented = read_tree(mat, guard + "/indented.md")
    except Missing:
        indented = None
        bad.append("%s/indented.md missing at lands" % guard)
    try:
        fourspace = read_tree(mat, guard + "/fourspace.md")
    except Missing:
        fourspace = None
        bad.append("%s/fourspace.md missing at lands" % guard)

    def detected(text):
        out = set()
        for line in text.splitlines():
            m = ROW_RE.match(line)          # 0-3 leading spaces only
            if m:
                out.add(m.group(1))
        return out

    planted = None
    if indented is not None:
        det = detected(indented)
        extra = sorted(det - base_ids)
        if len(extra) != 1:
            bad.append("the 1-3-space proof detects %d planted row(s) (%s); "
                       "want exactly one" % (len(extra), ",".join(extra) or "-"))
        else:
            planted = extra[0]
        listed = _smirror_ids(mat, guard + "/reg-ids-indented", bad)
        if listed is not None and listed != det:
            bad.append("reg-ids-indented != the rows the 0-3-space pattern "
                       "detects in the proof (%d vs %d)"
                       % (len(listed), len(det)))
    if fourspace is not None:
        det4 = detected(fourspace)
        if det4:
            bad.append("the 4-space proof's planted row is detected (%s); the "
                       "0-3-space pattern must find nothing there"
                       % ",".join(sorted(det4)[:4]))
        listed = _smirror_ids(mat, guard + "/reg-ids-four", bad)
        if listed is not None and listed != det4:
            bad.append("reg-ids-four != the rows the 0-3-space pattern detects "
                       "in the four-space proof")
    receipt = cfg["scratch_mirror"].get("receipt")
    if receipt:
        try:
            text = read_tree(mat, receipt["path"])
        except Missing:
            text = None
            bad.append("declared mirror receipt %s missing at lands"
                       % receipt["path"])
        if text is not None:
            for m in re.finditer(r"(?im)^\s*exit\s*[:=]?\s*(\d+)\s*$", text):
                if m.group(1) != "0":
                    bad.append("mirror receipt records exit %s" % m.group(1))
            for sid in cfg["rows"]:
                if sid not in text:
                    bad.append("mirror receipt does not name row %s" % sid)
            for e in cfg["entries"]:
                if os.path.basename(e) not in text:
                    bad.append("mirror receipt does not name %s"
                               % os.path.basename(e))
            for needle in receipt["contains"]:
                if needle not in text:
                    bad.append("mirror receipt does not carry %r" % needle)
    detail = ("reg-ids=%s staged=%s collisions=%s planted=%s"
              % ("-" if reg is None else len(reg),
                 "-" if staged is None else len(staged),
                 "-" if coll is None else len(coll), planted or "-"))
    if bad:
        detail = "; ".join(dedupe(bad)) + " | " + detail
    return leg("SCRATCHMIRROR", not bad, detail[:300])


# --------------------------------------------------------------- the table ---

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
    ("SCRATCHMIRROR", leg_scratchmirror),
    ("COLLCHECK", leg_collcheck),
    ("FROZENCFG", leg_frozencfg),
    ("INDEX", leg_index),
)


def legs_generated():
    """The frozen `legs[]`, generated from the table (r76 defect 4)."""
    return [name for name, _fn in LEGS]


def run_legs(ctx):
    """Run every leg in table order; one leg's failure never stops the rest."""
    results = []
    for name, fn in LEGS:
        try:
            ok = fn(ctx)
        except Missing as e:
            ok = leg(name, False, "missing at lands: %s" % e)
        except (OSError, RuntimeError, ValueError, TypeError,
                KeyError, AttributeError, IndexError,
                subprocess.SubprocessError) as e:
            ok = leg(name, False, "%s: %s" % (type(e).__name__, e))
        results.append((name, bool(ok)))
    passed = sum(1 for _n, ok in results if ok)
    return passed, len(results), results


def print_receipt(root, lands, mat, cfg, how):
    tree = git(root, "rev-parse", "%s^{tree}" % lands).stdout.strip()
    head = git(root, "rev-parse", "HEAD").stdout.strip()
    generated = legs_generated()
    print("# round-77 acceptance counter — claim C "
          "(shokuknow Chinese naming-system assimilation)")
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
    print("# generated legs: %d (%s)" % (len(generated), ",".join(generated)))
    print("# frozen legs: %d (%s)" % (len(cfg["frozen_legs"]),
                                      ",".join(cfg["frozen_legs"])))
    print("# frozen map: %s sha256=%s"
          % (cfg["map_path"] or "(none declared)", cfg["map_sha256"] or "-"))
    print("# materialized: %s at %s" % (how, mat))
    print("# worktree graded: no (leg bytes read only from the checkout and the "
          "git-archive base tree)")
    print("# lane worktree HEAD (disclosure only): %s" % head)
    print("# access date: %s" % cfg["access_date"])
    print("# entries (min %s): %s"
          % (cfg["min_entries"], " ; ".join(cfg["entries"])))
    print("# frozen counts: rows %s -> %s (k=%d); knowledge %s -> %s (n=%d)"
          % (cfg["rows_before"], cfg["rows_before"] + len(cfg["rows"]),
             len(cfg["rows"]), cfg["knowledge_before"],
             cfg["knowledge_before"] + len(cfg["entries"]),
             len(cfg["entries"])))
    print("# adopted rows: %s"
          % " ".join("%s<-%s" % (sid, "/".join(cfg["row_staged"][sid]))
                     for sid in cfg["rows"]))
    print("# required sections: %d (%s)"
          % (len(cfg["required_sections"]),
             " ; ".join(s["label"] for s in cfg["required_sections"])))
    print("# removed legacy ids: %s" % (",".join(cfg["removed_ids"]) or "-"))
    print("# staged universe: %s (from %s)"
          % (len(cfg["staged_universe"]), cfg["staged_ids_path"]))
    print("# scratch mirror: %s%s"
          % (cfg["scratch_mirror"]["dir"],
             (" receipt=%s" % cfg["scratch_mirror"]["receipt"]["path"])
             if cfg["scratch_mirror"].get("receipt") else ""))
    print("# ground receipt: %s"
          % ((cfg["ground_receipt"] or {}).get("path") or "-"))
    print("# census start: %s"
          % ((cfg["census_start"] or {}).get("path") or "-"))
    print()


def refuse(msg):
    """Refuse to grade: no leg ran, so the verdict is FAIL, never PASS."""
    print("REFUSED: %s" % msg, file=sys.stderr)
    print("ACCEPT-C-77: FAIL legs=0/%d (refused: %s)"
          % (len(LEGS), msg.splitlines()[0]))
    return 2


def _scratch_root(args):
    """The scratch root for every clone, materialization and temp dir.

    `--work`; then `$HYAKU_SCRATCH/kotodama-r77/counter`; then an
    operator-chosen `$TMPDIR/kotodama-r77/counter`; then the operator default
    `/fast/scratch/hyaku/kotodama-r77/counter`.  The system temporary directory
    is never used.
    """
    work = (getattr(args, "work", None) or "").strip()
    if work:
        return os.path.abspath(work)
    env = (os.environ.get("HYAKU_SCRATCH") or "").strip()
    if env:
        return os.path.join(os.path.abspath(env), "kotodama-r77", "counter")
    tmp = (os.environ.get("TMPDIR") or "").strip()
    if tmp and not _forbidden_scratch(tmp):
        return os.path.join(os.path.abspath(tmp), "kotodama-r77", "counter")
    return os.path.join(os.sep, "fast", "scratch", "hyaku", "kotodama-r77",
                        "counter")


def _forbidden_scratch(path):
    """True when `path` is (inside) the system temporary directory."""
    p = os.path.abspath(path)
    banned = os.path.abspath(os.sep + "tmp")
    return p == banned or p.startswith(banned + os.sep)


# ---------------------------------------------------------------- selftest ---
# Every fixture repo is git-init'd inside the scratch root, its
# `rev-parse --show-toplevel` asserted, and committed with a per-commit
# identity (`-c user.name/-c user.email`): no identity is written anywhere.

_FX_ACCESS = "2026-10-27"
_FX_ENTRY = "corpus/knowledge/linguistics/naming-systems.amend-2026-10-23.md"
_FX_ROWS = [("S004", "S901", "https://example.org/docs/alpha", "單名與雙名"),
            ("S005", "S902", "https://example.org/docs/beta",
             "Flowers, Plants, and Trees in Female Naming in China")]
_FX_TOPIC = ("Chinese personal naming as a structure — 姓/名 order and the "
             "contact-era acquisition — plus the onomastic classification of "
             "given names")
_FX_BASE_ENTRY = "# Naming systems\n\n## 1. The frame\n\n" + " ".join(
    ["name"] * 60) + "\n"
_FX_BASE_SAMPLE = "# Sample symbol\n\n## 1. Ground\n\n" + " ".join(
    ["symbol"] * 40) + "\n"


def _st_git(d, *args, check=True):
    r = subprocess.run(["git", "-C", d, *args], capture_output=True, text=True)
    if check and r.returncode != 0:
        raise RuntimeError("git %s failed: %s" % (" ".join(args), r.stderr.strip()))
    return r


def _st_write(root, rel, text, mode=None):
    full = os.path.join(root, rel)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as fh:
        fh.write(text)
    if mode is not None:
        os.chmod(full, mode)


def _st_commit(d, msg):
    _st_git(d, "add", "-A")
    _st_git(d, "-c", "user.name=AcceptFixture", "-c",
            "user.email=accept@example.invalid", "commit", "-q", "-m", msg)
    return _st_git(d, "rev-parse", "HEAD").stdout.strip()


def _st_registry_rows(rows):
    out = ["| id | source | kind | tier | scope | anchor | teaches | status | "
           "opened | recheck | used-by |",
           "|---|---|---|---|---|---|---|---|---|---|---|"]
    for rid, source, kind, tier, scope, anchor, teaches, status, opened, recheck, used in rows:
        out.append("| %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |"
                   % (rid, source, kind, tier, scope, anchor, teaches, status,
                      opened, recheck, used))
    return "\n".join(out) + "\n"


def _st_base_registry():
    return ("# SOURCES — fixture registry\n\nFixture shape: 11 cells per row.\n\n"
            "## Registry\n\n" + _st_registry_rows([
                ("S001", "Example base alpha — https://example.org/base/alpha",
                 "docs", "A", "fixture alpha", "heading — quote located: "
                 "「alpha base」", "teaches base alpha", "mined", "2026-10-20",
                 "on-change", "corpus/knowledge/linguistics/naming-systems.md"),
                ("S002", "Example base beta — https://example.org/base/beta",
                 "docs", "B", "fixture beta", "heading — quote located: "
                 "「beta base」", "teaches base beta", "mined", "2026-10-20",
                 "on-change", "corpus/knowledge/linguistics/naming-systems.md"),
                ("S003", "Example base gamma — https://example.org/base/gamma",
                 "docs", "B", "fixture gamma", "heading — quote located: "
                 "「gamma base」", "teaches base gamma", "mined", "2026-10-20",
                 "on-change", "corpus/knowledge/myth-symbol/sample.md"),
            ]) + "\n## Paths\n\n(base paths recorded by earlier rounds)\n\n"
                  "## Search log\n\n(base searches recorded by earlier rounds)\n")


def _st_readme(total, vec):
    return "\n".join([
        "# kotodama fixture corpus index", "",
        "revision: 0.1 — fixture base.", "",
        "## linguistics/ (%d)" % vec[0], "",
        "- `naming-systems.md` — Fixture naming systems entry.", "",
        "## myth-symbol/ (%d)" % vec[1], "",
        "- `sample.md` — Fixture sample symbol entry.", "",
        "Total knowledge entries: %d." % total, "",
        "Counts checked 2026-10-27 from the repo root: "
        "`find corpus/knowledge -type f -name '*.md' | wc -l` "
        "(total %d files; directory totals %s)."
        % (total, "/".join(str(v) for v in vec)), "",
    ])


def _st_footer(total, vec):
    return ("Total knowledge entries: %d.\n\n"
            "Counts checked 2026-10-27 from the repo root: "
            "`find corpus/knowledge -type f -name '*.md' | wc -l` "
            "(total %d files; directory totals %s).\n"
            % (total, total, "/".join(str(v) for v in vec)))


def _st_evidence_doc(sid, quote, freeze_sha, claims_source=None):
    if sid == "S004":
        body = ("單名與雙名 fixture document. The 姓/名 structure: 名 predates 姓; "
                "姓 + 名 is a contact-era acquisition in the southern Han–Jin "
                "material. " + " ".join(["alpha"] * 30))
        url = "https://example.org/docs/alpha"
    else:
        body = ("Flowers, Plants, and Trees in Female Naming in China — fixture "
                "onomastica document. " + " ".join(["beta"] * 30))
        url = "https://example.org/docs/beta"
    window = body if quote in body else body + " " + quote
    src = claims_source if claims_source is not None else \
        "git show %s:reports/round-77/claims.json" % freeze_sha
    return "\n".join([
        "# evidence %s — claim C GATE (round 77)" % sid,
        "url: %s" % url,
        "fetch: GET %s" % url,
        "user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/130.0 Safari/537.36",
        "http-status: 200",
        "bytes: %d" % len(body.encode("utf-8")),
        "sha256: %s" % hashlib.sha256(body.encode("utf-8")).hexdigest(),
        "access-date: %s" % _FX_ACCESS,
        "claims-source: %s" % src,
        "claims-frozen: yes",
        "challenge: none",
        "window-scope: whole-document",
        "visible-chars: %d" % len(window),
        "window-sha256: %s" % hashlib.sha256(window.encode("utf-8")).hexdigest(),
        "window-bytes: %d" % len(window.encode("utf-8")),
        "quote-words: %d" % len(quote.split()),
        "quote-chars: %d" % len(quote),
        "",
        "--- window ---",
        window,
        "--- quote ---",
        "「%s」" % quote,
        "",
    ])


def _st_lesson(rows, rejects, quote_ok_flag=True):
    lines = ["# Round 77 — fixture lesson", "", "## Gate", "",
             "Access date: %s. Evidence windows are committed as "
             "`reports/round-77/evidence/S004.txt` and "
             "`reports/round-77/evidence/S005.txt`." % _FX_ACCESS, "",
             "| source | access date | quote | locator | evidence | verdict |",
             "|---|---|---|---|---|---|"]
    for sid, _staged, url, quote in rows:
        shown = "「%s」" % quote if quote_ok_flag else "(quote absent)"
        lines.append("| %s — fixture document, live %s ; same-page capture "
                     "%s | %s | %s | section 1 | `%s/%s.txt` | admitted (tier A) |"
                     % (sid, url, _archive_for(url), _FX_ACCESS, shown,
                        EVIDENCE_DIR, sid))
    lines += ["", "| item | probed URL | reason | flip | verdict |",
              "|---|---|---|---|---|"]
    for sid, url, reason in rejects:
        lines.append("| %s staged record | %s | %s | reopen only if the page is "
                     "re-served | refused |" % (sid, url, reason))
    lines += ["", "## Mistakes", "", "(none)", ""]
    return "\n".join(lines)


def _archive_for(url):
    return "https://web.archive.org/web/20261027000000id_/%s" % url


def _st_claims(base, map_sha, mut):
    rows = []
    for sid, staged, url, _q in _FX_ROWS:
        doc = url
        if mut.get("collcheck_alias") and sid == "S005":
            doc = "https://example.org/docs/beta-alias"
        if mut.get("archive_doc") and sid == "S005":
            doc = _archive_for(url)
        rows.append({"lane_id": sid, "staged_id": staged, "document_url": doc})
    legs = legs_generated()
    if mut.get("leglist_dup"):
        legs = legs + ["INDEX"]
    claim = {
        "id": "C",
        "axis": "coverage",
        "title": "fixture: Chinese naming-system assimilation",
        "entries": [_FX_ENTRY],
        "min_entries": 1,
        "rows_before": 3,
        "knowledge_before": 2,
        "row_set": rows,
        "required_sections": [
            {"path": REGISTRY,
             "pattern": r"^- naming-system design .*S897.*S898", "min": 1,
             "label": "Paths entry naming S897 and S898"},
            {"path": REGISTRY,
             "pattern": r"(?i)^\*\*Chinese naming-system assimilation "
                        r"\(round 77\)\.\*\*", "min": 1,
             "label": "Search-log entry for round 77"},
        ],
        "ground": {
            "sweeps": [
                {"pattern": r"單名與雙名", "candidate": _FX_ENTRY,
                 "scope": "corpus/knowledge"},
                {"pattern": r"Flowers, Plants, and Trees", "candidate": _FX_ENTRY,
                 "scope": "corpus/knowledge"},
            ],
            "fragments": ["example.org/docs/alpha", "example.org/docs/beta"],
            "terms": ["單名", "雙名"],
            "receipt": TELEMETRY + "/gap-sweep.txt",
        },
        "rejects": {
            "refused_staged_not_appended": ["S933", "S934"],
            "refused_files": ["naming-systems.amend-2026-10-24.md"],
            "counts": {"adopted": 1, "refused": 2, "total_staged_files": 3},
        },
        "map": ({"path": ASSIM + "/id-renumber-map.json",
                 "sha256": "0" * 64 if mut.get("map_sha_bad") else map_sha}
                if not mut.get("rowset_only") else None),
        "census_start": {"path": TELEMETRY + "/census-start.txt", "rows": 3},
        "removed_ids": ["S886", "S896"],
        "staged_ids": ASSIM + "/staged-ids",
        "scratch_mirror": {"dir": ASSIM},
        "legs": legs,
        "access_date": _FX_ACCESS,
        "owned_inplace": ["corpus/README.md"],
    }
    return {"round": ROUND, "status": "frozen", "frozen": True, "base": base,
            "claims": [claim]}


def _st_map_text(mut=None):
    mut = mut or {}
    beta = "https://example.org/docs/beta"
    if mut.get("map_doc_alias"):
        beta = "https://example.org/docs/beta-alias"
    return json.dumps({"round": ROUND, "assignments": [
        {"staged_id": "S901", "new_target": "S004",
         "document_url": "https://example.org/docs/alpha"},
        {"staged_id": "S902", "new_target": "S005",
         "document_url": beta},
    ]}, indent=2) + "\n"


def _st_entry_text(mut):
    topic = "TBD" if mut.get("stub_entry") else _FX_TOPIC
    body = " ".join(["naming"] * 40) if mut.get("stub_entry") else " ".join(
        ["naming system structure and lexeme inventory"] * 8)
    paths = "" if mut.get("drop_required_section") else (
        "## Paths\n\n- 姓/名 structure: 名 predates 姓.\n- Lexeme inventory: "
        "finite classification.\n\n")
    term = "" if mut.get("ground_after") else "單名與雙名 and "
    legacy = "The earlier note S886 is superseded.\n\n" if mut.get(
        "legacy_cited") else ""
    two_ids = ("The structure and the inventory are covered together "
               "(S004, S005).\n\n") if mut.get("citedlines_multi") else ""
    source_beta = ("source: Kałużyńska 2025 — fixture onomastica document "
                   "named without its address; column S005\n"
                   if mut.get("source_no_url")
                   else "source: Kałużyńska 2025 — https://example.org/docs/beta "
                        "; lane row S005\n")
    return ("# Naming systems — amendment\n\n"
            "source: 魏斌 — https://example.org/docs/alpha ; lane row S004\n"
            "%s"
            "verified-at: %s\nrecheck: on-change\n"
            "ground: at base the corpus holds no system-level account of the "
            "姓/名 structure\n"
            "topic: %s\n\n%s## 1. Structure\n\n%s\n\n%s%sThe amendment records "
            "%s the finite lexical inventory; Flowers, Plants, and Trees in "
            "Female Naming in China is one classification row.\n\n"
            "## Search log\n\nSearch log: the base sweep prints nothing; the two "
            "documents above are the only ones opened this round.\n"
            % (source_beta, _FX_ACCESS, topic, paths, body, legacy, two_ids,
               term))


def _st_cited_tool():
    """A stand-in for tools/check-cited-lines.py with the same contract."""
    return '''#!/usr/bin/env python3
"""Fixture stand-in for tools/check-cited-lines.py (same output contract)."""
import re
import sys

ID = re.compile(r"\\bS\\d{3,}\\b")


def main(paths):
    findings = 0
    files = 0
    for path in paths:
        files += 1
        try:
            with open(path, encoding="utf-8") as fh:
                lines = fh.read().splitlines()
        except OSError:
            print("CITED_LINES_ERROR", file=sys.stderr)
            return 2
        for lineno, line in enumerate(lines, 1):
            ids = sorted(set(ID.findall(line)))
            if len(ids) >= 2:
                findings += 1
                print("MULTI-ID %s:%d %s" % (path, lineno, ",".join(ids)))
            if line.lstrip().startswith("|") and ids:
                findings += 1
                print("TABLE-ID %s:%d %s" % (path, lineno, ",".join(ids)))
    print("CITED-LINES: %d finding(s) in %d file(s)" % (findings, files))
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
'''


def _st_assim_files(d, mut):
    """The assimilation artifacts SCRATCHMIRROR re-derives."""
    base_text = _st_base_registry()
    base_ids = list(parse_rows(base_text))
    reg = list(base_ids)
    if mut.get("scratch_regids"):
        reg = reg[:-1]
    staged = ["S901", "S902", "S905"]
    if mut.get("scratch_collision") or mut.get("scratch_collision_stale"):
        staged = staged + [base_ids[1]]
    collisions = sorted(set(reg) & set(staged))
    if mut.get("scratch_collision_stale"):
        collisions = []
    planted = "S004"
    header = ("# SOURCES — fixture guard proof\n\nA planted row, not a real "
              "registry.\n\n## Registry\n\n")
    indented = (header + _st_registry_rows([
        ("S001", "planted-proof S001", "docs", "A", "x", "y", "z", "queued",
         "2026-10-27", "90d", "—"),
        ("S002", "planted-proof S002", "docs", "A", "x", "y", "z", "queued",
         "2026-10-27", "90d", "—"),
        ("S003", "planted-proof S003", "docs", "A", "x", "y", "z", "queued",
         "2026-10-27", "90d", "—"),
    ]) + "   | %s | planted 3space row | paper | A | x | y | z | queued | "
         "2026-10-27 | 90d | — |\n" % planted)
    indent_lead = "   " if mut.get("scratch_guard") else "    "
    fourspace = (header + "%s| %s | planted row | paper | A | x | y | z | "
                 "queued | 2026-10-27 | 90d | — |\n" % (indent_lead, planted))
    _st_write(d, ASSIM + "/reg-ids", "\n".join(reg) + "\n")
    _st_write(d, ASSIM + "/staged-ids", "\n".join(staged) + "\n")
    _st_write(d, ASSIM + "/collisions",
              ("\n".join(collisions) + "\n") if collisions else "")
    _st_write(d, ASSIM + "/guard-proof/indented.md", indented)
    _st_write(d, ASSIM + "/guard-proof/fourspace.md", fourspace)
    _st_write(d, ASSIM + "/guard-proof/reg-ids-indented",
              "\n".join(reg + [planted]) + "\n")
    _st_write(d, ASSIM + "/guard-proof/reg-ids-four",
              ("\n".join([planted]) + "\n") if mut.get("scratch_guard") else "")


def _st_landing_files(d, freeze, mut):
    rows = []
    for sid, _staged, url, quote in _FX_ROWS:
        source = ("%s fixture document — live %s ; same page captured %s at %s"
                  % (sid, url, _FX_ACCESS, _archive_for(url)))
        if mut.get("collcheck_prose") and sid == "S005":
            source = "Kałużyńska 2025 fixture document (see the Gate for its address)"
        if mut.get("row_usedby_extra") and sid == "S004":
            used = _FX_ENTRY + ", corpus/knowledge/myth-symbol/sample.md"
        else:
            used = _FX_ENTRY
        rows.append("| %s | %s | docs | A | fixture scope | section 1 — quote "
                    "located: 「%s」 | teaches %s | mined | %s | on-change | %s |"
                    % (sid, source, quote, sid, _FX_ACCESS, used))
    registry = _st_base_registry()
    if mut.get("appendonly_edit"):
        registry = registry.replace("| S002 | Example base beta",
                                    "| S002 | Example base beta (edited)")
    extra = ""
    if mut.get("row_extra"):
        extra = ("| S006 | Example extra — live https://example.org/docs/gamma "
                 "| docs | B | fixture extra | section 1 | teaches extra | mined "
                 "| %s | on-change | %s |\n" % (_FX_ACCESS, _FX_ENTRY))
    if mut.get("pre_row_edit"):
        registry = registry.replace("Example base beta — https://example.org"
                                    "/base/beta",
                                    "Example base beta — https://example.org"
                                    "/base/beta2")
    if mut.get("pre_row_rule2"):
        registry = registry.replace("on-change | corpus/knowledge/myth-symbol"
                                    "/sample.md",
                                    "on-change | corpus/knowledge/myth-symbol"
                                    "/sample.md, corpus/knowledge/linguistics"
                                    "/naming-systems.md")
    head, _sections = registry.split("\n## Paths", 1)
    paths_line = "" if mut.get("drop_required_section") else (
        "- naming-system design — S897 → S898: read the 姓/名 structure account, "
        "then the onomastic inventory classification; neither supports the "
        "other's clauses.\n")
    search_line = "" if mut.get("drop_required_section") else (
        "**Chinese naming-system assimilation (round 77).** Question: does one "
        "staged naming-system amendment add a source-grounded structure the "
        "corpus did not hold? Where searched: the two opened documents.\n")
    text = head + extra + "\n".join(rows) + "\n"
    text += "\n## Paths\n\n(base paths recorded by earlier rounds)\n" + paths_line
    text += ("\n## Search log\n\n(base searches recorded by earlier rounds)\n"
             + search_line)
    _st_write(d, REGISTRY, text)

    if not mut.get("entry_missing"):
        _st_write(d, _FX_ENTRY, _st_entry_text(mut))
    if mut.get("extra_knowledge"):
        _st_write(d, "corpus/knowledge/myth-symbol/extra.md",
                  "# Extra\n\n## 1. Ground\n\n" + " ".join(["extra"] * 30) + "\n")

    # the README: change the linguistics count parenthetical, insert the entry's
    # index row, and APPEND a new footer block (older footers stay untouched).
    live_vec = [1 + (0 if mut.get("entry_missing") else 1),
                1 + (1 if mut.get("extra_knowledge") else 0)]
    total = sum(live_vec)
    text = _st_readme(2, [1, 1])
    text = text.replace("## linguistics/ (1)",
                        "## linguistics/ (%d)" % live_vec[0], 1)
    if not mut.get("entry_missing"):
        entry_row = "- `%s` — %s" % (
            os.path.basename(_FX_ENTRY),
            "TBD" if mut.get("stub_entry") else _FX_TOPIC)
        text = text.replace(
            "- `naming-systems.md` — Fixture naming systems entry.",
            entry_row + "\n- `naming-systems.md` — Fixture naming systems entry.",
            1)
    shown_vec = [live_vec[0], live_vec[1] + (1 if mut.get("index_footer_bad")
                                             else 0)]
    text = text.rstrip("\n") + "\n\n" + _st_footer(total, shown_vec)
    _st_write(d, README, text)

    rejects = [] if mut.get("rejects_empty") else [
        ("S933", "https://example.org/docs/gamma",
         "the staged page no longer carries the text"),
        ("S934", "https://example.org/docs/delta",
         "same document as S005 (document-level duplicate)"),
    ]
    _st_write(d, LESSON, _st_lesson(_FX_ROWS, rejects,
                                    quote_ok_flag=not mut.get("gate_quote_absent")))

    for sid, _staged, _url, quote in _FX_ROWS:
        src = None
        if mut.get("stamp_wrong"):
            src = "git show %s:reports/round-77/claims.json" % ("0" * 40)
        text = _st_evidence_doc(sid, quote, freeze, src)
        if mut.get("evidence_window_sha"):
            text = text.replace("window-sha256: ", "window-sha256: 0")
        _st_write(d, "%s/%s.txt" % (EVIDENCE_DIR, sid), text)

    if mut.get("ground_receipt_missing"):
        try:
            os.remove(os.path.join(d, TELEMETRY + "/gap-sweep.txt"))
        except OSError:
            pass
    if mut.get("shrink_claims"):
        path = os.path.join(d, CLAIMS)
        with open(path, encoding="utf-8") as fh:
            doc = json.load(fh)
        doc["claims"][0]["row_set"] = doc["claims"][0]["row_set"][:1]
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(doc, fh, indent=2)
            fh.write("\n")


def _st_census_stub(fleet, red):
    script = os.path.join(fleet, "scripts", "sources-census.sh")
    os.makedirs(os.path.dirname(script), exist_ok=True)
    body = "#!/bin/sh\necho \"fixture\\trows\\t3\"\nexit %d\n" % (1 if red else 0)
    with open(script, "w", encoding="utf-8") as fh:
        fh.write(body)
    os.chmod(script, 0o755)
    return fleet


def _st_build(case_dir, mut=None):
    mut = dict(mut or {})
    d = os.path.join(case_dir, "lane")
    os.makedirs(d)
    _st_git(d, "init", "-q")
    top = _st_git(d, "rev-parse", "--show-toplevel").stdout.strip()
    if os.path.realpath(top) != os.path.realpath(d):
        raise RuntimeError("fixture toplevel %r != %r" % (top, d))
    _st_write(d, REGISTRY, _st_base_registry())
    _st_write(d, README, _st_readme(2, [1, 1]))
    _st_write(d, "corpus/knowledge/linguistics/naming-systems.md", _FX_BASE_ENTRY)
    _st_write(d, "corpus/knowledge/myth-symbol/sample.md",
              _FX_BASE_SAMPLE + ("\n單名與雙名\n" if mut.get("ground_before") else ""))
    _st_write(d, "tools/check-cited-lines.py", _st_cited_tool(), mode=0o755)
    _st_write(d, BASE_LESSON, "# Round 76 — fixture lesson\n\n## Gate\n\n(none)\n")
    base = _st_commit(d, "base")

    map_text = _st_map_text(mut)
    map_sha = hashlib.sha256(map_text.encode("utf-8")).hexdigest()
    if not mut.get("rowset_only"):
        _st_write(d, ASSIM + "/id-renumber-map.json", map_text)
    claims = _st_claims(base, map_sha, mut)
    _st_write(d, CLAIMS, json.dumps(claims, indent=2) + "\n")
    _st_assim_files(d, mut)
    _st_write(d, TELEMETRY + "/census-start.txt",
              "sources-census.sh validate --root . kotodama\nrows 3\nexit 0\n")
    _st_write(d, TELEMETRY + "/gap-sweep.txt",
              "gap sweep %s: 單名與雙名 and Flowers, Plants, and Trees absent at "
              "base\nexit 0\n" % _FX_ACCESS)
    freeze = _st_commit(d, "freeze")

    fleet = _st_census_stub(os.path.join(case_dir, "fleet"),
                            red=bool(mut.get("census_red")))
    if mut.get("lands_eq_base"):
        return {"root": d, "base": base, "freeze": freeze, "lands": base,
                "fleet": fleet}
    if mut.get("lands_eq_freeze"):
        return {"root": d, "base": base, "freeze": freeze, "lands": freeze,
                "fleet": fleet}
    _st_landing_files(d, freeze, mut)
    lands = _st_commit(d, "lands")
    return {"root": d, "base": base, "freeze": freeze, "lands": lands,
            "fleet": fleet}


def _st_run(paths, scratch):
    cmd = [sys.executable, "-B", os.path.abspath(__file__),
           "--root", paths["root"], "--lands", paths["lands"],
           "--freeze", paths["freeze"], "--fleet-root", paths["fleet"],
           "--work", scratch]
    r = subprocess.run(cmd, capture_output=True, text=True)
    legs = {}
    for line in (r.stdout or "").splitlines():
        m = re.match(r"^LEG (PASS|FAIL) (\S+)$", line)
        if m:
            legs[m.group(2)] = m.group(1)
    verdict = None
    for line in (r.stdout or "").splitlines():
        if line.startswith("ACCEPT-C-77:"):
            verdict = line
    return r.returncode, legs, verdict, r.stdout or "", r.stderr or ""


_ST_CASES = [
    # (name, mutation, want exit, want EXACT failing-leg set, mode)
    ("clean", {}, 0, (), "all-pass"),
    ("lands-eq-freeze", {"lands_eq_freeze": True}, 1,
     ("CITEDLINES", "COLLCHECK", "ENTRIES", "EVIDENCE", "GATE", "GROUND",
      "INDEX", "REJECTS", "REPOINTED", "ROWS"), "graded"),
    ("lands-eq-base", {"lands_eq_base": True}, 2, (), "refused"),
    ("J1-stub-entry", {"stub_entry": True}, 1, ("ENTRIES",), "graded"),
    ("J2-gate-quote-absent", {"gate_quote_absent": True}, 1,
     ("EVIDENCE", "GATE"), "graded"),
    ("J3-shrunk-claims", {"shrink_claims": True}, 1, ("FROZENCFG",), "graded"),
    ("row-extra", {"row_extra": True}, 1, ("ROWS",), "graded"),
    ("row-usedby-extra", {"row_usedby_extra": True}, 1, ("ROWS",), "graded"),
    ("pre-row-edit", {"pre_row_edit": True}, 1, ("ROWS",), "graded"),
    ("pre-row-rule2-cell", {"pre_row_rule2": True}, 0, (), "all-pass"),
    ("collcheck-alias", {"collcheck_alias": True}, 1,
     ("COLLCHECK", "EVIDENCE", "GATE"), "graded"),
    ("collcheck-prose-only", {"collcheck_prose": True}, 1,
     ("COLLCHECK", "REPOINTED", "ROWS"), "graded"),
    ("collcheck-map-alias", {"map_doc_alias": True}, 1,
     ("COLLCHECK",), "graded"),
    ("collcheck-archive-identity", {"archive_doc": True}, 0, (), "all-pass"),
    ("rowset-only-map-absent", {"rowset_only": True}, 0, (), "all-pass"),
    ("map-sha-mismatch", {"map_sha_bad": True}, 1, ("FROZENCFG",), "graded"),
    ("index-footer", {"index_footer_bad": True}, 1, ("INDEX",), "graded"),
    ("index-required-section", {"drop_required_section": True}, 1,
     ("INDEX",), "graded"),
    ("evidence-window-sha", {"evidence_window_sha": True}, 1,
     ("EVIDENCE",), "graded"),
    ("evidence-stamp-wrong", {"stamp_wrong": True}, 1, ("EVIDENCE",), "graded"),
    ("rejects-empty", {"rejects_empty": True}, 1, ("REJECTS",), "graded"),
    ("ground-before-present", {"ground_before": True}, 1, ("GROUND",), "graded"),
    ("ground-after-missing", {"ground_after": True}, 1, ("GROUND",), "graded"),
    ("ground-receipt-missing", {"ground_receipt_missing": True}, 1,
     ("GROUND",), "graded"),
    ("census-red", {"census_red": True}, 1, ("CENSUS",), "graded"),
    ("counts-extra-knowledge", {"extra_knowledge": True}, 1,
     ("ENTRIES", "INDEX"), "graded"),
    ("entry-missing", {"entry_missing": True}, 1,
     ("CITEDLINES", "ENTRIES", "GROUND", "INDEX", "REPOINTED", "ROWS"),
     "graded"),
    ("repointed-legacy-id", {"legacy_cited": True}, 1, ("REPOINTED",), "graded"),
    ("repointed-source-no-url", {"source_no_url": True}, 1,
     ("REPOINTED",), "graded"),
    ("citedlines-multi", {"citedlines_multi": True}, 1,
     ("CITEDLINES",), "graded"),
    ("scratchmirror-regids", {"scratch_regids": True}, 1,
     ("SCRATCHMIRROR",), "graded"),
    ("scratchmirror-collision-recorded", {"scratch_collision": True}, 0, (),
     "all-pass"),
    ("scratchmirror-collisions-stale", {"scratch_collision_stale": True}, 1,
     ("SCRATCHMIRROR",), "graded"),
    ("scratchmirror-indent-guard", {"scratch_guard": True}, 1,
     ("SCRATCHMIRROR",), "graded"),
    ("legcount-duplicate", {"leglist_dup": True}, 2, (), "refused"),
]


def _st_scratch(work=None):
    work = (work or "").strip()
    if work:
        return os.path.abspath(work)
    env = (os.environ.get("HYAKU_SCRATCH") or "").strip()
    if env:
        return os.path.join(os.path.abspath(env), "kotodama-r77", "selftest")
    tmp = (os.environ.get("TMPDIR") or "").strip()
    if tmp and not _forbidden_scratch(tmp):
        return os.path.join(os.path.abspath(tmp), "kotodama-r77", "selftest")
    return os.path.join(os.sep, "fast", "scratch", "hyaku", "kotodama-r77",
                        "selftest")


def run_selftest():
    scratch = _st_scratch()
    if _forbidden_scratch(scratch):
        print("SELFTEST: 0/1 (scratch root %s is the system temporary "
              "directory)" % scratch)
        return 1
    os.makedirs(scratch, exist_ok=True)
    run_dir = tempfile.mkdtemp(prefix="accept-c77-", dir=scratch)
    results = []
    try:
        # the leg table is the frozen list's only source
        gen = legs_generated()
        ok = len(gen) == len(set(gen)) and len(gen) == len(LEGS)
        results.append((ok, "CASE emit-legs: %s -- %d name(s), no duplicate"
                        % ("PASS" if ok else "FAIL", len(gen))))
        r = subprocess.run([sys.executable, "-B", os.path.abspath(__file__),
                            "--emit-legs"], capture_output=True, text=True)
        try:
            emitted = json.loads(r.stdout)
        except ValueError:
            emitted = None
        ok = r.returncode == 0 and emitted == gen
        results.append((ok, "CASE emit-legs-json: %s -- --emit-legs prints the "
                            "generated list" % ("PASS" if ok else "FAIL")))
        work = os.path.join(run_dir, "scratch")
        for name, mut, want_exit, want_fails, mode in _ST_CASES:
            case_dir = os.path.join(run_dir, name)
            os.makedirs(case_dir)
            try:
                paths = _st_build(case_dir, mut)
            except Exception as e:              # a fixture that cannot build
                results.append((False, "CASE %s: FAIL -- fixture build: %s"
                                % (name, e)))
                continue
            code, legs, verdict, out, err = _st_run(paths, work)
            problems = []
            got = tuple(sorted(n for n, v in legs.items() if v == "FAIL"))
            if code != want_exit:
                problems.append("exit %d (want %d)" % (code, want_exit))
            if mode == "refused":
                if "REFUSED" not in err:
                    problems.append("no refusal on stderr")
                if not (verdict or "").startswith("ACCEPT-C-77: FAIL"):
                    problems.append("no FAIL verdict line")
                if got:
                    problems.append("legs ran: %s" % ",".join(got))
            else:
                if got != want_fails:
                    problems.append("failed legs %s (want %s)"
                                    % (",".join(got) or "-",
                                       ",".join(want_fails) or "-"))
                if mode == "all-pass" and "FAIL" in (verdict or ""):
                    problems.append("verdict %r" % verdict)
            ok = not problems
            results.append((ok, "CASE %s: %s -- %s"
                            % (name, "PASS" if ok else "FAIL",
                               "; ".join(problems) if problems else
                               (verdict or "")[:160])))
    finally:
        shutil.rmtree(run_dir, ignore_errors=True)
    total, passed = len(results), sum(1 for ok, _m in results if ok)
    for ok, msg in results:
        print(msg)
    print("SELFTEST: %d/%d" % (passed, total))
    return 0 if passed == total else 1


# ------------------------------------------------------------------- main ---

def main(argv=None):
    ap = argparse.ArgumentParser(
        description="round-77 coverage counter (claim C)")
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
                         "(default: $HYAKU_SCRATCH/kotodama-r77/counter, else "
                         "$TMPDIR/kotodama-r77/counter, else "
                         "/fast/scratch/hyaku/kotodama-r77/counter; never the "
                         "system temporary directory)")
    ap.add_argument("--selftest", action="store_true", help="run in-process cases")
    ap.add_argument("--emit-legs", action="store_true",
                    help="print the generated frozen legs[] as JSON and exit")
    args = ap.parse_args(argv)

    if args.emit_legs:
        print(json.dumps(legs_generated()))
        return 0

    if args.selftest:
        runner = globals().get("run_selftest")
        if runner is None:
            return refuse("--selftest needs the fixture part assembled")
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
    if git(root, "cat-file", "-e", "%s^{commit}" % cfg["base"]).returncode != 0:
        print("ERROR: frozen claim base not found: %s" % cfg["base"],
              file=sys.stderr)
        return 2
    ours = legs_generated()
    theirs = list(cfg["frozen_legs"])
    duplicates = sorted(n for n in set(theirs) if theirs.count(n) > 1)
    if duplicates:
        return refuse("LEGCOUNT: the frozen claims.json repeats the leg name(s) "
                      "%s; this counter implements 13 unique names (%s)"
                      % (",".join(duplicates), ",".join(ours)))
    if theirs != ours:
        return refuse("LEGCOUNT: the frozen claims.json lists %d legs (%s); "
                      "this counter implements %d (%s) — regenerate legs[] "
                      "from --emit-legs"
                      % (len(theirs), ",".join(theirs), len(ours),
                         ",".join(ours)))
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

    tmp_root = tempfile.mkdtemp(prefix="r77-lands-", dir=scratch)
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
    print("ACCEPT-C-77: %s legs=%d/%d" % ("PASS" if ok else "FAIL", passed, total))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
