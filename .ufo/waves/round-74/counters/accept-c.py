#!/usr/bin/env python3
r"""Round-74 coverage acceptance counter — claim C.

Claim C (reports/round-74/claims.json, id "C", axis coverage): the shokuknow
assimilation of the worldbuilding-setting-practice theme — four adopted rows
(S881..S884), one reused lane row (S877, used-by changed in place), two
entries, the Gate record, the per-row evidence captures, the gap-sweep
receipt, the scratch mirror and the collision guard.

Grading model (QUALITY 19).  Nothing in the graded tree is trusted to be the
tree that was graded: the counter clones the lane into a fresh mktemp
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
`ACCEPT-C-74: ... legs=<n>/<n>` summary line.

Hardenings closed (round-73 survivors, corpus/lessons/round-73-verifier-
spotcheck.md §6 and corpus/lessons/round-73.md `## Routed to round 74`):

  H1 FROZENCFG  Every constant the counter uses — row_set (lane id + staged
     id), reused_rows, entry paths, ground.fragments, ground.cjk_terms, the
     rejects lists and counts, the by-document map path and its sha256, the
     claim base and the access date — is read with
     `git show <freeze>:reports/round-74/claims.json` and never from the
     graded tree.  The leg fails when the graded tree's claims.json differs
     from the frozen bytes, when <freeze> is not on <lands>' first-parent
     chain, or when `git show <freeze>:<map.path>` does not hash to the frozen
     `map.sha256`.  A frozen claims.json that cannot be read at all is a
     refusal (exit 2).  `lands == the frozen base` is also a refusal that
     still prints FAIL (the do-nothing control).
  H2 EVIDENCE   The Gate quote must occur INSIDE the committed evidence
     window text (substring after NFKC + whitespace folding), the stored
     window is at least 4096 characters, and `window-sha256` / `window-bytes`
     are recomputed from the stored window line.  The self-attested
     `quote-found` / `quote-found-verbatim` lines are never read: a
     `quote-found: yes` over a window that lacks the quote fails.
  H3 GATE       The Gate quote's word and character counts are recomputed from
     the quoted span itself (<= 25 whitespace tokens AND <= 80 characters;
     CJK counts per whitespace token).  No `quote-words:` field is trusted.
  H4 ROWS       The registry diff base..<lands> is compared exactly, as a
     line multiset: the only lines that may be added are the adopted rows,
     the only lines that may be removed are a reused row's old line, and that
     pair may differ in the used-by cell alone.  Any other added, removed or
     replaced line (prose included) fails.  A blank line is tolerated: it
     adds no row and hides no row.
  H5            Junk-landing resistance: a header-only stub entry fails
     ENTRIES (body-word floor from the base knowledge tree); rows copied from
     the staged package with used-by pointing at stub paths fail ROWS
     (used-by must equal exactly the admitted entries whose `source:` lines
     cite the row); an entry citing an id whose registry row names a
     different document fails REPOINTED (URL join, never arithmetic); a
     counter config edited in the graded tree fails FROZENCFG.  These are the
     controls in the `do_nothing_control` of claim C and the mutants in
     --selftest.

Artifact shapes the legs read (all at <lands>; a shape miss is a leg FAIL,
never a skip):

  registry row     `| S881 | source | kind | tier | scope | anchor | teaches |
                   mined | <access date> | <cadence> | used-by |` — exactly 11
                   cells, no `\|`, anchor carrying the evidence quote,
                   source carrying the map URL verbatim, used-by exactly the
                   citing entry paths;
  Gate admit table a header row carrying a `quote`, an access-date and a
                   locator/grounds/anchor column; one admit row per adopted
                   row carrying its URL, a `<=25`-token quoted span and a
                   non-dash locator; the re-quoted rows (staged ids in
                   rejects.forced_new_quotes) also state `re-quote` and
                   absent/refused/mispairing;
  Gate reject table a header row carrying `reason` and `flip`; every reject
                   row carrying its probed URL, a non-dash reason and a
                   non-dash flip;
  evidence file    the grammar written by counters/capture-evidence.py:
                   `url:`/`fetch:`, `user-agent:` (Mozilla/5.0 ...),
                   `http-status: 200`, 64-hex `sha256:`, `access-date:`, a
                   `--- window ---` line of >= 4096 characters, its
                   `window-sha256:`/`window-bytes:` and a `--- quote ---`
                   block; the Gate quote must occur inside the window;
  README index     `corpus/README.md`: one row per adopted entry inside the
                   `## culture-material/` section, shaped
                   ``- `name.md` — <the entry's own `- topic:` text>``, the
                   last `Counts checked` footer carrying the file total and
                   the six-partition vector, and every older footer preserved
                   byte-identically from base;
  renumber map     `assignments[]` with staged_id/new_target/url and/or a
                   `map` object; the old id must be the row_set staged id and
                   the url must be the row's document;
  guard proof      one file with a 1-3-space-indented planted row (an id that
                   is no real row) and a positive detection marker, and one
                   file with a 4-space planted row and a not-found marker;
  mirror receipt   `.ufo/waves/round-74/assimilation/validate-receipt.txt`
                   showing `--file`, exit 0, the four ids and both entry
                   basenames, committed before the registry-append commit.

Configuration schema read at <freeze> (the draft claims.json schema, kept —
no schema change is required; `access_date` is the only optional addition):
  claims[id=C].row_set[]        {"id": "S881", "staged": "S883"}
  claims[id=C].reused_rows[]    {"id": "S877", "staged": "S882"}
  claims[id=C].entries[]        entry paths
  claims[id=C].ground.fragments[] / .cjk_terms[]
  claims[id=C].rejects.refused_staged_not_appended[] / .forced_new_quotes[] /
                  .folded_dropped[] / .refused_files[] /
                  .path_present_bytes_differ[] / .counts{}
  claims[id=C].map.path         the by-document renumber map path
  claims[id=C].map.sha256       the sha256 of that map blob at <freeze>
  claims[id=C].legs[]           the frozen leg list (LEGCOUNT)
  claims[id=C].access_date      OPTIONAL; default 2026-10-25
  base                          top-level claim base (40-hex)

Usage:
  python3 -B accept-c.py --root <lane> --lands <40hex> --freeze <40hex>
                         [--fleet-root <fleet>] [--selftest]

Exit: 0 all legs pass; 1 any leg fails; 2 input error or refusal (missing
argument, unknown revision, unreadable/unusable claims.json at <freeze>,
`lands` equal to the frozen claim base, or the frozen `legs[]` list not
matching this counter's leg table).  A refusal also prints
`ACCEPT-C-74: FAIL legs=0/<n> (refused: ...)` — no leg ran, so the verdict is
a FAIL and never a PASS; the exit code marks it as an input error.

--selftest builds every fixture repo in its own mktemp dir (git init + three
commits: base, freeze, lands), runs the counter as a subprocess against it,
and asserts one named leg per mutant.
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
ROUND = 74
ACCESS_DATE = "2026-10-25"
CLAIMS = "reports/round-74/claims.json"
REGISTRY = "corpus/SOURCES.md"
LESSON = "corpus/lessons/round-74.md"
EVIDENCE_DIR = "reports/round-74/evidence"
README = "corpus/README.md"
KNOWLEDGE = "corpus/knowledge"
ASSIM = ".ufo/waves/round-74/assimilation"
RECEIPT = ASSIM + "/validate-receipt.txt"
GROUND_RECEIPT = "reports/round-74/telemetry/gap-sweep.txt"
RENUMBER_MAP = ASSIM + "/id-renumber-map.json"
RENUMBER_MAP_DRAFT = ASSIM + "/id-renumber-map-draft.json"
GUARD_DIR = ASSIM + "/guard-proof"
CLAIM_KEYS = ("row_set", "reused_rows", "entries", "ground", "rejects")
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
RECHECK_RE = re.compile(r"^(?:\d+d|\d{4}-\d{2}-\d{2}|[a-z][a-z-]*)$")
NOT_ADOPTED_RE = re.compile(r"(?i)\bnot\s+adopted\b|\bno\s+adoption\b|\bnot\s+admitted\b"
                            r"|\bnot\s+appended\b")
REQUOTE_RE = re.compile(r"(?i)re-?\s?quote")
MISPAIR_RE = re.compile(r"(?i)\babsent\b|\brefus|\bmis-?\s?pair")
DASHES = ("—", "-", "–", "n/a", "na", "")
ANGLE_RE = re.compile(r"<[^>]+>")
README_SECTION_RE = re.compile(r"^## ([a-z-]+)/ \((\d+)\)\s*$", re.M)
README_ROW_RE = re.compile(r"^- `([^`]+\.md)` — (.*)$")
README_FOOTER_RE = re.compile(r"\(total (\d+) files; directory totals ([\d/]+)\)")


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
    if older == newer:
        return False
    return git(root, "merge-base", "--is-ancestor", older, newer).returncode == 0


def clone_at(root, lands, dest):
    """Materialize <lands> as a real checkout inside `dest` (a mktemp dir)."""
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
    for line in lines:
        if line.lstrip().startswith("|"):
            rows.append(line.strip())
        elif line.startswith(" ") and rows:
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


# ------------------------------------------------------------ config load ---

def _frozen_claim(doc):
    for c in doc.get("claims") or []:
        if isinstance(c, dict) and str(c.get("id", "")).upper() == "C":
            return c
    return None


def _paths_from_spec(spec):
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


def _row_pairs(spec, what):
    if not isinstance(spec, list):
        raise ConfigError("%s is not a list" % what)
    pairs, seen = [], set()
    for item in spec:
        if not isinstance(item, dict):
            raise ConfigError("%s carries a non-object item: %r" % (what, item))
        rid = str(item.get("id", "")).strip().upper()
        staged = str(item.get("staged", "")).strip().upper()
        if not TOKEN_RE.fullmatch(rid) or not TOKEN_RE.fullmatch(staged):
            raise ConfigError("%s item needs 40-hex-free S-ids: %r" % (what, item))
        if rid in seen:
            raise ConfigError("%s repeats lane id %s" % (what, rid))
        seen.add(rid)
        pairs.append((rid, staged))
    return pairs


def load_frozen_config(root, freeze):
    """H1: every constant comes from `git show <freeze>:claims.json`."""
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
    row_pairs = _row_pairs(claim["row_set"], "row_set")
    if not row_pairs:
        raise ConfigError("row_set at freeze is empty")
    reused_pairs = _row_pairs(claim.get("reused_rows") or [], "reused_rows")
    entries = _paths_from_spec(claim["entries"])
    if not entries:
        raise ConfigError("entries at freeze is empty")
    ground = claim["ground"]
    if not isinstance(ground, dict):
        raise ConfigError("ground at freeze is not an object")
    fragments = [str(x) for x in (ground.get("fragments") or [])]
    cjk_terms = [str(x) for x in (ground.get("cjk_terms") or [])]
    if not fragments:
        raise ConfigError("ground.fragments at freeze is empty")
    if not cjk_terms:
        raise ConfigError("ground.cjk_terms at freeze is empty")
    rejects = claim["rejects"]
    if not isinstance(rejects, dict):
        raise ConfigError("rejects at freeze is not an object")
    refused_staged = _id_list(rejects.get("refused_staged_not_appended") or [],
                              "rejects.refused_staged_not_appended")
    forced = _id_list(rejects.get("forced_new_quotes") or [],
                      "rejects.forced_new_quotes")
    folded = _id_list(rejects.get("folded_dropped") or [],
                      "rejects.folded_dropped")
    refused_files = [str(x) for x in (rejects.get("refused_files") or [])]
    path_present = [str(x) for x in
                    (rejects.get("path_present_bytes_differ") or [])]
    counts = rejects.get("counts")
    if not isinstance(counts, dict):
        raise ConfigError("rejects.counts at freeze is not an object")
    parsed_counts = {}
    for key in ("adopted", "path_present", "refused", "total_staged_files"):
        try:
            parsed_counts[key] = int(counts[key])
        except (KeyError, TypeError, ValueError):
            raise ConfigError("rejects.counts.%s at freeze is not an integer"
                              % key)
    map_spec = claim.get("map")
    if not isinstance(map_spec, dict):
        raise ConfigError("claim C at freeze carries no map object")
    map_path = str(map_spec.get("path") or "").strip()
    map_sha = str(map_spec.get("sha256") or "").strip().lower()
    if not map_path or map_path.startswith("/") or ".." in map_path.split("/"):
        raise ConfigError("claim map.path at freeze is not a relative repo "
                          "path: %r" % map_path)
    if not map_sha:
        raise ConfigError("claim map.sha256 at freeze is empty")
    frozen_legs = []
    for item in claim.get("legs") or []:
        name = str(item).split(":", 1)[0].strip().upper()
        if name:
            frozen_legs.append(name)
    access_date = str(claim.get("access_date") or doc.get("access_date")
                      or ACCESS_DATE).strip()
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", access_date):
        raise ConfigError("access date at freeze is not YYYY-MM-DD: %r" % access_date)
    rows = [p[0] for p in row_pairs]
    row_staged = dict(row_pairs)
    reused = [p[0] for p in reused_pairs]
    reused_staged = dict(reused_pairs)
    lane_ids = set(rows) | set(reused)
    staged_ids = set(row_staged.values()) | set(reused_staged.values())
    cfg = {
        "freeze": freeze,
        "frozen_sha256": hashlib.sha256(raw).hexdigest(),
        "base": base,
        "access_date": access_date,
        "rows": rows,
        "row_staged": row_staged,
        "reused": reused,
        "reused_staged": reused_staged,
        "entries": entries,
        "fragments": fragments,
        "cjk_terms": cjk_terms,
        "refused_staged": refused_staged,
        "forced_new_quotes": forced,
        "folded_dropped": folded,
        "refused_files": refused_files,
        "path_present": path_present,
        "counts": parsed_counts,
        "map_path": map_path,
        "map_sha256": map_sha,
        "frozen_legs": frozen_legs,
        "allowed_ids": lane_ids,
        "forbidden_ids": sorted(staged_ids - lane_ids),
        "claim_keys": sorted(claim.keys()),
    }
    return cfg


# ------------------------------------------------------------------ legs ---

def _row_url_keys(lands_rows, sid):
    row = lands_rows.get(sid)
    if row is None:
        return set()
    cells = row_cells(row)
    if len(cells) <= SOURCE:
        return set()
    return neutral_url_keys(urls_in(cells[SOURCE]))


def _gate_admit_row(gate_rows, sid, lands_rows):
    """The Gate admit row for `sid`: joined by URL first, by id token second."""
    admits = [r for r in gate_rows if is_admit_row(r)]
    keys = _row_url_keys(lands_rows, sid)
    for r in admits:
        if keys & neutral_url_keys(urls_in(r)):
            return r
    for r in admits:
        if re.search(r"\b%s\b" % sid, r):
            return r
    return None


def _min_entry_words(mat_base):
    best = None
    for rel in tree_files(mat_base, "corpus/knowledge"):
        if not rel.endswith(".md"):
            continue
        try:
            text = read_tree(mat_base, rel)
        except Missing:
            continue
        n = len(text.split())
        best = n if best is None else min(best, n)
    return best or 0


def _evidence(mat, rid):
    """Parse reports/round-74/evidence/<id>.txt at lands."""
    try:
        text = read_tree(mat, EVIDENCE_DIR + "/" + rid + ".txt")
    except Missing:
        return None
    out = {}
    for line in text.splitlines():
        m = re.match(r"^([A-Za-z][A-Za-z0-9_-]*):\s*(.*)$", line)
        if m and m.group(1).lower() not in out:
            out[m.group(1).lower()] = m.group(2)
    out["_text"] = text
    out["_window"] = _window(text)
    return out


def _window(text):
    """The stored window exactly as capture-evidence.py stores it: the lines
    between the `--- window ---` marker and `--- quote ---`, trailing empty
    lines dropped, joined by newlines (the producer writes one line)."""
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


def leg_entries(ctx):
    """ENTRIES: both entries exist at lands, absent at base, header first, no
    placeholder values, body at least the base tree's smallest entry in words."""
    mat, mat_base, cfg = ctx["mat"], ctx["mat_base"], ctx["cfg"]
    bad = []
    floor = _min_entry_words(mat_base)
    if floor <= 0:
        bad.append("base knowledge tree yields no word floor")
    for e in cfg["entries"]:
        try:
            text = read_tree(mat, e)
        except Missing:
            bad.append("%s missing at lands" % e)
            continue
        if os.path.exists(os.path.join(mat_base, e)):
            bad.append("%s present at base (not uncovered ground)" % e)
        if not text.strip():
            bad.append("%s empty" % e)
            continue
        labels = header_field_names(text)
        missing = [f for f in HEADER_FIELDS if norm_label(f) not in labels]
        if missing:
            bad.append("%s header missing: %s" % (e, ",".join(missing)))
        wanted = set(norm_label(f) for f in HEADER_FIELDS)
        for line in header_block(text):
            m = re.match(r"^[-*\s]*([A-Za-z][A-Za-z0-9 -]*):\s*(.*)$", line)
            if not m or norm_label(m.group(1)) not in wanted:
                continue
            val = m.group(2).strip().strip("—-–").strip().lower()
            if val in PLACEHOLDERS:
                bad.append("%s header field %r carries a placeholder value"
                           % (e, m.group(1)))
            if ANGLE_RE.search(m.group(2)):
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
        words = len("\n".join(lines[body_start:]).split())
        if words < floor:
            bad.append("%s body has %d words (floor %d = the smallest knowledge "
                       "entry at base)" % (e, words, floor))
    return leg("ENTRIES", not bad, "; ".join(dedupe(bad)))


def leg_rows(ctx):
    """ROWS (H4): the registry diff base..lands adds exactly the adopted rows,
    changes nothing else but the reused row's used-by cell, and each row is a
    normalized, mined, dated row whose used-by is exactly its citing entries."""
    mat, mat_base, cfg = ctx["mat"], ctx["mat_base"], ctx["cfg"]
    try:
        base_text = read_tree(mat_base, REGISTRY)
        lands_text = read_tree(mat, REGISTRY)
    except Missing as e:
        return leg("ROWS", False, "registry unreadable: %s" % e)
    base_rows = parse_rows(base_text)
    lands_rows = parse_rows(lands_text)
    want = list(cfg["rows"])
    reused = set(cfg["reused"])
    bad = []

    added = set(lands_rows) - set(base_rows)
    removed = set(base_rows) - set(lands_rows)
    if added != set(want):
        bad.append("added=%s (want %s)" % (sorted(added), want))
    if removed:
        bad.append("removed=%s (want none)" % sorted(removed))
    nums = sorted(int(x[1:]) for x in added)
    if nums and nums != list(range(nums[0], nums[0] + len(nums))):
        bad.append("added ids %s are not contiguous" % nums)
    base_max = max((int(i[1:]) for i in base_rows), default=0)
    if nums and nums[0] <= base_max:
        bad.append("added ids start at S%d, not above the base's last id S%d"
                   % (nums[0], base_max))

    # H4: line-level diff, exactly the adopted rows added + the one used-by
    # change on a reused row.  Multiset difference is order-insensitive and
    # keeps a duplicate line from hiding behind its twin; a blank line adds no
    # row and hides no row, so it is tolerated.
    base_lines = [l.rstrip() for l in base_text.splitlines()]
    lands_lines = [l.rstrip() for l in lands_text.splitlines()]
    added_lines = list((Counter(lands_lines) - Counter(base_lines)).elements())
    removed_lines = list((Counter(base_lines) - Counter(lands_lines)).elements())
    inserted, removed_row_ids = [], []
    for line in removed_lines:
        if not line.strip():
            continue
        m = ROW_RE.match(line)
        if not m:
            bad.append("registry line removed outside the reused row: %r"
                       % line[:70])
            continue
        removed_row_ids.append(m.group(1))
    for line in added_lines:
        if not line.strip():
            continue
        m = ROW_RE.match(line)
        if not m:
            bad.append("registry line added outside the adopted rows: %r"
                       % line[:70])
            continue
        if m.group(1) in removed_row_ids:
            continue  # a replacement line; the removed-row loop judges it
        inserted.append(m.group(1))
    if sorted(inserted) != sorted(want):
        bad.append("added rows %s (want %s)" % (sorted(inserted), sorted(want)))
    if len(set(inserted)) != len(inserted):
        bad.append("a row line is added twice: %s" % sorted(inserted))
    reused_old, reused_new = {}, {}
    for rid in removed_row_ids:
        if rid not in reused:
            bad.append("%s removed (only a reused row's used-by cell may change)"
                       % rid)
            continue
        old_line = next(l for l in removed_lines if ROW_RE.match(l)
                        and ROW_RE.match(l).group(1) == rid)
        new_cand = [l for l in added_lines if ROW_RE.match(l)
                    and ROW_RE.match(l).group(1) == rid]
        if not new_cand:
            bad.append("%s row removed with no replacement line" % rid)
            continue
        cb, cl = row_cells(old_line), row_cells(new_cand[0])
        if len(cb) != len(cl):
            bad.append("%s in-place change alters the cell count" % rid)
        else:
            diff = [k for k in range(len(cb)) if cb[k] != cl[k]]
            if diff != [USEDBY]:
                bad.append("%s in-place change outside the used-by cell (cells %s)"
                           % (rid, diff))
        reused_old[rid], reused_new[rid] = cb, cl

    cited = _entry_citations(mat, cfg["entries"], bad)
    stray = set(cited) - set(want) - reused
    if stray:
        bad.append("entries cite ids outside the adopted/reused set: %s"
                   % sorted(stray))

    map_recs = _map_records(ctx)
    union = set()
    for sid in want:
        row = lands_rows.get(sid)
        if row is None:
            bad.append("%s row missing" % sid)
            continue
        cells = row_cells(row)
        if "\\|" in row:
            bad.append("%s row carries an escaped pipe (staged text appended as-is)"
                       % sid)
            continue
        if len(cells) != NCELLS:
            bad.append("%s row has %d cells (want %d)" % (sid, len(cells), NCELLS))
            continue
        if cells[STATUS] != "mined":
            bad.append("%s status=%r (want mined)" % (sid, cells[STATUS]))
        if cells[OPENED] != cfg["access_date"]:
            bad.append("%s opened=%r (want %s: a staged opened date is an "
                       "as-is tell)" % (sid, cells[OPENED], cfg["access_date"]))
        if not RECHECK_RE.match(cells[RECHECK]):
            bad.append("%s recheck=%r is not a cadence-only cell"
                       % (sid, cells[RECHECK]))
        used = row_usedby(cells)
        want_used = cited.get(sid, set())
        if used != want_used:
            bad.append("%s used-by=%s (want exactly %s)"
                       % (sid, sorted(used), sorted(want_used)))
        union |= used
        ev = _evidence(mat, sid)
        if ev is not None and ev.get("quote"):
            if nfkc_ws(ev["quote"]) not in nfkc_ws(cells[ANCHOR]):
                bad.append("%s anchor cell does not contain its evidence quote" % sid)
        recs = [v for k, v in map_recs.items() if k[1] == sid]
        if not recs:
            bad.append("%s has no committed renumber-map entry" % sid)
        else:
            url = recs[0]
            if not url:
                bad.append("%s map entry carries no url" % sid)
            elif url not in cells[SOURCE]:
                bad.append("%s source cell lacks the map URL verbatim: %s"
                           % (sid, url))

    # the reused row: its used-by cell and nothing else, base value plus
    # exactly the base-entry path (parsed from both revisions).
    for sid in cfg["reused"]:
        row = lands_rows.get(sid)
        if row is None:
            bad.append("%s row missing" % sid)
            continue
        cells = row_cells(row)
        if len(cells) != NCELLS:
            bad.append("%s row has %d cells (want %d)" % (sid, len(cells), NCELLS))
            continue
        old = base_rows.get(sid)
        if old is None:
            bad.append("%s row is not present at base" % sid)
            continue
        ocells = row_cells(old)
        if len(ocells) != NCELLS:
            bad.append("%s base row has %d cells (want %d)"
                       % (sid, len(ocells), NCELLS))
            continue
        diff = [k for k in range(NCELLS) if cells[k] != ocells[k]]
        if diff != [USEDBY]:
            bad.append("%s differs from its base line outside the used-by cell "
                       "(cells %s)" % (sid, diff))
            continue
        expect = row_usedby(ocells) | {cfg["entries"][0]}
        got = row_usedby(cells)
        if got != expect:
            bad.append("%s used-by=%s (want its base value plus exactly %s)"
                       % (sid, sorted(got), cfg["entries"][0]))
    if union != set(cfg["entries"]):
        bad.append("used-by union %s (want both admitted entries)" % sorted(union))
    for e in cfg["entries"]:
        if not any(e in v for v in cited.values()):
            bad.append("%s cites no adopted row" % e)

    # the reused row's in-place used-by change must be logged old -> new.
    try:
        lesson = read_tree(mat, LESSON)
    except Missing:
        lesson = ""
    for rid, old in reused_old.items():
        new = reused_new[rid]
        old_s, new_s = old[USEDBY], new[USEDBY]
        if old_s == new_s:
            continue
        same_line = any(old_s in l and new_s in l for l in lesson.splitlines())
        both = (any(old_s in l for l in lesson.splitlines())
                and any(new_s in l for l in lesson.splitlines())
                and re.search(r"→|->|old", lesson))
        if not (same_line or both):
            bad.append("%s used-by change not logged old->new in %s" % (rid, LESSON))
    return leg("ROWS", not bad, "; ".join(dedupe(bad)))


def _map_records(ctx):
    """{(old_id, new_id): url} from the frozen by-document map.

    The map is read with `git show <freeze>:<map.path>` — the frozen claims
    name both the path and the sha256 — and never from the graded tree.
    """
    root, cfg = ctx["root"], ctx["cfg"]
    r = git_bytes(root, "show", "%s:%s" % (cfg["freeze"], cfg["map_path"]))
    if r.returncode != 0:
        return {}
    try:
        doc = json.loads(r.stdout.decode("utf-8"))
    except (ValueError, UnicodeDecodeError):
        return {}
    if not isinstance(doc, dict):
        return {}
    recs = {}
    for a in doc.get("assignments") or []:
        if not isinstance(a, dict):
            continue
        old = str(a.get("staged_id") or a.get("old") or "").strip().upper()
        new = str(a.get("new_lane_id") or a.get("new_target") or a.get("new")
                  or a.get("target") or a.get("lane") or "").strip().upper()
        if TOKEN_RE.fullmatch(old) and TOKEN_RE.fullmatch(new):
            url = a.get("url")
            recs[(old, new)] = str(url) if url else None
    mapping = doc.get("map")
    if isinstance(mapping, dict):
        for old, new in mapping.items():
            if isinstance(new, dict):
                new = new.get("target") or new.get("lane")
            old = str(old).strip().upper()
            new = str(new or "").strip().upper()
            if TOKEN_RE.fullmatch(old) and TOKEN_RE.fullmatch(new):
                recs.setdefault((old, new), None)
    return recs


def leg_repointed(ctx):
    """REPOINTED: every source line names exactly one id whose row URL equals
    the cited URL; every inline id resolves to one of those rows; no
    staged-namespace id is cited as if it were a lane row."""
    mat, cfg = ctx["mat"], ctx["cfg"]
    try:
        lands_rows = parse_rows(read_tree(mat, REGISTRY))
    except Missing as e:
        return leg("REPOINTED", False, "registry unreadable: %s" % e)
    allowed = cfg["allowed_ids"]
    bad = []
    for e in cfg["entries"]:
        try:
            text = read_tree(mat, e)
        except Missing:
            bad.append("%s missing" % e)
            continue
        for sline in source_lines(text):
            ids = TOKEN_RE.findall(sline)
            if len(ids) != 1:
                bad.append("%s source line ids=%s (want exactly one)" % (e, ids))
                continue
            sid = ids[0]
            if sid not in allowed:
                bad.append("%s cites %s outside the five adopted/reused rows"
                           % (e, sid))
                continue
            if sid not in lands_rows:
                bad.append("%s cites %s with no registry row" % (e, sid))
                continue
            cited_urls = urls_in(sline)
            if not cited_urls:
                bad.append("%s source line for %s carries no URL" % (e, sid))
                continue
            row_keys = _row_url_keys(lands_rows, sid)
            for u in cited_urls:
                if norm_url(u) not in row_keys:
                    bad.append("%s cites a URL not registered on %s: %s"
                               % (e, sid, u))
        for lineno, line in enumerate(text.splitlines(), 1):
            for sid in TOKEN_RE.findall(line):
                if sid not in allowed:
                    bad.append("%s:%d inline id %s resolves to no adopted/reused row"
                               % (e, lineno, sid))
        for fid in cfg["forbidden_ids"]:
            if re.search(r"\b%s\b" % re.escape(fid), text):
                bad.append("%s cites staged-namespace id %s as if it were a lane row"
                           % (e, fid))
    return leg("REPOINTED", not bad, "; ".join(dedupe(bad)))


def leg_gate(ctx):
    """GATE (H3): per adopted row the lesson's ## Gate carries URL + access
    date + a recomputed <=25-token located quote + a locator cell, >=1 admit
    and >=1 reject, every reject row carrying its probed URL, reason and flip;
    the re-quoted rows state the earlier refusal."""
    mat, cfg = ctx["mat"], ctx["cfg"]
    try:
        text = read_tree(mat, LESSON)
        lands_rows = parse_rows(read_tree(mat, REGISTRY))
    except Missing as e:
        return leg("GATE", False, "%s" % e)
    section = gate_section(text)
    if not section:
        return leg("GATE", False, "no ## Gate section in %s" % LESSON)
    rows = table_rows(section)
    admits = [r for r in rows if is_admit_row(r)]
    rejects = [r for r in rows if is_reject_row(r)]
    bad = []
    ahdr = table_header(rows, ("quote",))
    quote_i = date_i = loc_i = None
    if ahdr is None:
        bad.append("admit table header lacks a quote column")
    else:
        quote_i = col_index(ahdr, ("quote",))
        date_i = col_index(ahdr, ("date",))
        loc_i = col_index(ahdr, ("locator", "grounds", "anchor", "location"))
        if date_i is None:
            bad.append("admit table header lacks an access-date column")
        if loc_i is None:
            bad.append("admit table header lacks a locator column")
    rhdr = table_header(rows, ("reason", "flip"))
    if rhdr is None:
        bad.append("reject table header lacks reason+flip columns")
    reason_i = flip_i = None
    if rhdr is not None:
        reason_i = col_index(rhdr, ("reason",))
        flip_i = col_index(rhdr, ("flip",))

    for sid in cfg["rows"] + cfg["reused"]:
        row = _gate_admit_row(admits, sid, lands_rows)
        if row is None:
            bad.append("%s has no admit row in Gate" % sid)
            continue
        cells = row_cells(row)
        if date_i is not None:
            if date_i >= len(cells) or cells[date_i] != cfg["access_date"]:
                bad.append("%s admit row access date %r (want %s)"
                           % (sid, cells[date_i] if date_i < len(cells) else None,
                              cfg["access_date"]))
        if loc_i is not None:
            if loc_i >= len(cells) or cells[loc_i].strip().lower() in DASHES:
                bad.append("%s admit row carries no locator cell" % sid)
        if quote_i is not None:
            if quote_i >= len(cells):
                bad.append("%s admit row has no quote cell" % sid)
            else:
                spans = quoted_spans(cells[quote_i])
                if not spans:
                    bad.append("%s admit row carries no quoted span" % sid)
                elif not any(quote_ok(s) for s in spans):
                    bad.append("%s admit row quote exceeds 25 tokens or 80 "
                               "characters (recomputed: tokens=%s chars=%s)"
                               % (sid, [len(s.split()) for s in spans],
                                  [len(s) for s in spans]))
        if not (_row_url_keys(lands_rows, sid) & neutral_url_keys(urls_in(row))):
            bad.append("%s admit row does not carry the row URL" % sid)
        staged = cfg["row_staged"].get(sid)
        if staged and staged in cfg["forced_new_quotes"]:
            if not REQUOTE_RE.search(row):
                bad.append("%s admit row does not state the re-quote" % sid)
            elif not MISPAIR_RE.search(row):
                bad.append("%s admit row does not state why the staged quote was "
                           "replaced (absent/refused/mispairing)" % sid)
    if not admits:
        bad.append("no admit row (want >=1)")
    if not rejects:
        bad.append("no reject row (want >=1)")
    for row in rejects:
        cells = row_cells(row)
        if not urls_in(row):
            bad.append("reject row records no probed URL: %s" % row[:80])
        if reason_i is not None:
            if reason_i >= len(cells) or cells[reason_i].strip().lower() in DASHES:
                bad.append("reject row carries no reason cell: %s" % row[:80])
        if flip_i is not None:
            if flip_i >= len(cells) or cells[flip_i].strip().lower() in DASHES:
                bad.append("reject row carries no flip cell: %s" % row[:80])
    return leg("GATE", not bad, "; ".join(dedupe(bad)))


def _evidence_core(ev, sid, access_date, row_keys):
    """Header, scope, digest and length checks for one evidence file.

    Window scope (claim C, final): `excerpt` requires a window of at least 4096
    characters; `whole-document` is allowed only when the stored window is
    shorter than 4096 characters and its length equals the recorded
    `visible-chars:`.  The stored window's sha256 is recomputed from the bytes
    the file stores; no flag in the file is read.
    """
    bad = []
    status = ev.get("http-status") or ev.get("http")
    if status != "200":
        bad.append("%s http-status %r (want 200)" % (sid, status))
    if ev.get("access-date") != access_date:
        bad.append("%s access-date %r (want %s)"
                   % (sid, ev.get("access-date"), access_date))
    if not re.fullmatch(r"[0-9a-f]{64}", ev.get("sha256", "")):
        bad.append("%s sha256 line is not a 64-hex digest" % sid)
    ua = ev.get("user-agent") or ev.get("ua") or ""
    if not ua.startswith("Mozilla/5.0"):
        bad.append("%s user-agent not recorded as a browser-shaped UA: %r"
                   % (sid, ua[:40]))
    fetch = ev.get("fetch") or ev.get("url") or ""
    if not fetch:
        bad.append("%s carries no fetch line" % sid)
    elif not (row_keys & neutral_url_keys(urls_in(fetch))):
        bad.append("%s fetch line does not name the row URL" % sid)
    window = ev["_window"]
    if window is None:
        bad.append("%s stores no --- window --- block" % sid)
        return bad, None
    payload = window.encode("utf-8")
    digest = hashlib.sha256(payload).hexdigest()
    declared = (ev.get("window-sha256") or "").strip().lower()
    if declared != digest:
        bad.append("%s window-sha256 %r != the recomputed digest of the "
                   "stored window (%s)" % (sid, declared[:16], digest[:16]))
    declared_bytes = (ev.get("window-bytes") or "").strip()
    if declared_bytes and declared_bytes != str(len(payload)):
        bad.append("%s window-bytes %r != the stored window's %d bytes"
                   % (sid, declared_bytes, len(payload)))
    scope = (ev.get("window-scope") or "").strip().lower()
    visible = (ev.get("visible-chars") or "").strip()
    if scope not in ("excerpt", "whole-document"):
        bad.append("%s window-scope %r (want excerpt|whole-document)"
                   % (sid, scope))
    if not visible.isdigit():
        bad.append("%s visible-chars %r is not a character count"
                   % (sid, visible))
    if scope == "excerpt":
        if len(window) < MIN_WINDOW_CHARS:
            bad.append("%s excerpt window is %d characters (want >= %d)"
                       % (sid, len(window), MIN_WINDOW_CHARS))
    elif scope == "whole-document":
        if len(window) >= MIN_WINDOW_CHARS:
            bad.append("%s whole-document window is %d characters (>= %d: "
                       "declare excerpt)" % (sid, len(window), MIN_WINDOW_CHARS))
        if visible.isdigit() and int(visible) != len(window):
            bad.append("%s whole-document window is %d characters but "
                       "visible-chars is %s" % (sid, len(window), visible))
    return bad, window


def leg_evidence(ctx):
    """EVIDENCE (H2): a committed capture per adopted/reused row — fetch line,
    browser-shaped UA, HTTP 200, 64-hex sha256, a stored window whose scope
    rule holds, and the window CONTAINS the Gate quote after NFKC + whitespace
    folding.  No flag is read."""
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
        row_bad, window = _evidence_core(ev, sid, cfg["access_date"],
                                         _row_url_keys(lands_rows, sid))
        bad.extend(row_bad)
        if window is None or not window.strip():
            continue
        grow = _gate_admit_row(gate_rows, sid, lands_rows)
        if grow is None:
            bad.append("%s has no Gate admit row to couple the window to" % sid)
            continue
        spans = [s for s in quoted_spans(grow) if quote_ok(s)]
        if not spans:
            bad.append("%s Gate admit row carries no <=25-token, <=80-char quote"
                       % sid)
            continue
        if not any(nfkc_ws(s) in nfkc_ws(window) for s in spans):
            bad.append("%s Gate quote is absent from the stored window "
                       "(substring after NFKC+whitespace folding)" % sid)
    return leg("EVIDENCE", not bad, "; ".join(dedupe(bad)))


def _refused_names(spec):
    """Name tests for one refused_files entry: the leading name and its stem."""
    first = spec.strip().split()[0] if spec.strip() else ""
    names = [first]
    if "(" in spec:
        names.append(spec.split("(")[0].strip())
    if "/" in first:
        names.append(first.split("/")[0])
    return [n for n in dict.fromkeys(names) if len(n) >= 3]


def leg_rejects(ctx):
    """REJECTS: the lesson names the refused staged row, the earlier-refused
    quotes and the re-quote, and every not-adopted file/family, with reason
    and flip."""
    mat, cfg = ctx["mat"], ctx["cfg"]
    try:
        text = read_tree(mat, LESSON)
    except Missing as e:
        return leg("REJECTS", False, "%s" % e)
    lines = text.splitlines()
    bad = []
    for sid in cfg["refused_staged"]:
        hits = [l for l in lines if re.search(r"\b%s\b" % re.escape(sid), l)]
        if not hits:
            bad.append("refused staged %s not named in the lesson" % sid)
            continue
        reused_ids = [rid for rid, st in cfg["reused_staged"].items() if st == sid]
        if reused_ids:
            if not any(any(rid in l for rid in reused_ids) or
                       re.search(r"(?i)\balready\b|\bexisting\b", l) for l in hits):
                bad.append("refused staged %s not tied to its existing lane row %s"
                           % (sid, ",".join(reused_ids)))
        elif not any(NOT_ADOPTED_RE.search(l) or re.search(r"(?i)\brefus", l)
                     for l in hits):
            bad.append("refused staged %s carries no refusal marker" % sid)
    for sid in cfg["forced_new_quotes"]:
        hits = [l for l in lines if re.search(r"\b%s\b" % re.escape(sid), l)]
        if not hits:
            bad.append("earlier-refused staged %s not named in the lesson" % sid)
        elif not any(REQUOTE_RE.search(l) or MISPAIR_RE.search(l) for l in hits):
            bad.append("staged %s is not recorded with its refusal and re-quote"
                       % sid)
    for sid in cfg["folded_dropped"]:
        hits = [l for l in lines if re.search(r"\b%s\b" % re.escape(sid), l)]
        if not hits:
            bad.append("folded-dropped staged %s not named in the lesson" % sid)
        elif not any(re.search(r"(?i)\bfold|dropped|refus|rejected", l)
                     for l in hits):
            bad.append("staged %s is not recorded as folded/dropped" % sid)
    for spec in cfg["refused_files"]:
        if not any(name in text for name in _refused_names(spec)):
            bad.append("not-adopted staged file/family not named: %r" % spec[:60])
    counts = cfg["counts"]
    order = [counts["adopted"], counts["path_present"], counts["refused"],
             counts["total_staged_files"]]
    pat = re.compile(r"\b%d\b[\s\S]{0,300}?\b%d\b[\s\S]{0,300}?\b%d\b"
                     r"[\s\S]{0,300}?\b%d\b" % tuple(order))
    paragraphs = re.split(r"\n[ \t]*\n", text)
    if not any(pat.search(p) for p in paragraphs):
        bad.append("lesson does not state the counts %d adopted / %d "
                   "path-present / %d refused of %d" % tuple(order))
    if len(cfg["path_present"]) != counts["path_present"]:
        bad.append("frozen rejects.path_present_bytes_differ holds %d paths, "
                   "counts.path_present says %d"
                   % (len(cfg["path_present"]), counts["path_present"]))
    qsec = section_block(text, r"^##\s+Quarantine\b")
    if not qsec.strip():
        bad.append("no `## Quarantine` section in the lesson")
    else:
        qlow = nfkc_ws(qsec).lower()
        for sid in ("S816", "S817"):
            if not re.search(r"\b%s\b" % sid, qsec):
                bad.append("`## Quarantine` does not name register row %s" % sid)
        if "refused" not in qlow:
            bad.append("`## Quarantine` does not record S816/S817 as REFUSED")
        if "stay refused" not in qlow:
            bad.append("`## Quarantine` does not state that refused rows stay "
                       "refused")
        if not re.search(r"re-?\s?opened\s+as\s+new\s+rows", qlow):
            bad.append("`## Quarantine` does not state that the document is "
                       "re-opened as new rows")
    low = text.lower()
    if not re.search(r"\b(refused|rejected|quarantine)\b", low):
        bad.append("no refusal/quarantine marker in the lesson")
    if "reason" not in low or "flip" not in low:
        bad.append("reason+flip not recorded in the lesson")
    return leg("REJECTS", not bad, "; ".join(dedupe(bad)))


def leg_ground(ctx):
    """GROUND: the gap-sweep receipt names the base registry's row count and a
    0 per fragment and per CJK term; the base tree is re-derived independently."""
    mat, mat_base, cfg = ctx["mat"], ctx["mat_base"], ctx["cfg"]
    try:
        base_text = read_tree(mat_base, REGISTRY)
        base_rows = parse_rows(base_text)
    except Missing as e:
        return leg("GROUND", False, "base registry unreadable: %s" % e)
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
        for label, terms in (("fragment", cfg["fragments"]),
                             ("CJK term", cfg["cjk_terms"])):
            for term in terms:
                idxs = [i for i, l in enumerate(lines) if term in l]
                if not idxs:
                    bad.append("receipt does not name %s %r" % (label, term))
                    continue
                if not any(re.search(r"(?:^|[^\d])0(?:[^\d]|$)",
                                     "\n".join(lines[i:i + 3]))
                           for i in idxs):
                    bad.append("receipt shows no 0 for %s %r" % (label, term))
    # independent re-derivation at base
    low_registry = base_text.lower()
    for frag in cfg["fragments"]:
        if frag.lower() in low_registry:
            bad.append("base registry already names the fragment %r" % frag)
    stems = set()
    for e in cfg["entries"]:
        stems.add(re.split(r"\.amend-", os.path.basename(e))[0].lower())
    for rel in tree_files(mat_base, "corpus/knowledge"):
        base = os.path.basename(rel).lower()
        for stem in stems:
            if stem and stem in base:
                bad.append("base knowledge tree already holds %s" % rel)
    for rel in tree_files(mat_base, "corpus/knowledge"):
        if not rel.endswith(".md"):
            continue
        try:
            body = read_tree(mat_base, rel)
        except Missing:
            continue
        for term in cfg["cjk_terms"]:
            if term in body:
                bad.append("base knowledge file %s already carries %r" % (rel, term))
    return leg("GROUND", not bad, "; ".join(dedupe(bad)))


def leg_citedlines(ctx):
    """CITEDLINES: tools/check-cited-lines.py over both entries, 0 findings."""
    mat, cfg = ctx["mat"], ctx["cfg"]
    bad = []
    tool = os.path.join(mat, "tools/check-cited-lines.py")
    if not os.path.isfile(tool):
        return leg("CITEDLINES", False, "tools/check-cited-lines.py missing at lands")
    paths = []
    for e in cfg["entries"]:
        if os.path.isfile(os.path.join(mat, e)):
            paths.append(os.path.join(mat, e))
        else:
            bad.append("%s missing" % e)
    if not paths:
        return leg("CITEDLINES", False, "; ".join(bad))
    r = subprocess.run([sys.executable, "-B", tool] + paths,
                       capture_output=True, text=True)
    out = r.stdout
    if r.returncode != 0:
        bad.append("tool exit=%d" % r.returncode)
    if "CITED-LINES: 0 finding(s) in %d file(s)" % len(paths) not in out:
        bad.append("findings not zero over %d files: %s" % (len(paths), out.strip()))
    return leg("CITEDLINES", not bad, "; ".join(dedupe(bad)))


def leg_census(ctx):
    """CENSUS: sources-census.sh validate exits 0 over the registry of <lands>."""
    mat, cfg = ctx["mat"], ctx["cfg"]
    fleet_root = ctx["fleet_root"]
    script = os.path.join(fleet_root, "scripts/sources-census.sh")
    if not os.path.isfile(script):
        return leg("CENSUS", False, "census script not found: %s" % script)
    bad = []
    with tempfile.TemporaryDirectory(prefix="r74-fleet-") as fleet:
        os.symlink(os.path.abspath(mat), os.path.join(fleet, "kotodama-shokunin"))
        with open(os.path.join(fleet, "shokunin.conf"), "w", encoding="utf-8") as fh:
            fh.write('LANES="\n'
                     'kotodama|kotodama-shokunin|round-74 materialized lands tree\n'
                     '"\n')
        r = subprocess.run([script, "validate", "--root", fleet,
                            "--today", cfg["access_date"], "kotodama"],
                           capture_output=True, text=True)
    if r.returncode != 0:
        bad.append("census exit=%d" % r.returncode)
    errs = re.findall(r"^E[0-9][0-9]", r.stdout, re.M)
    if errs:
        bad.append("census TSV carries E-code line(s): %s"
                   % ",".join(sorted(set(errs))))
    detail = "exit=%d" % r.returncode
    tail = r.stdout.strip().splitlines()[-1] if r.stdout.strip() else ""
    if tail:
        detail += " last-line=%s" % tail
    if bad:
        detail = "; ".join(bad) + " (" + detail + ")"
    return leg("CENSUS", not bad, detail)


def leg_scratch_mirror(ctx):
    """SCRATCHMIRROR: the validate --file receipt carries exit 0 on the
    mirrored corpus with the four rows and both entries, in a commit strictly
    before the registry-append commit."""
    root, mat, cfg = ctx["root"], ctx["mat"], ctx["cfg"]
    try:
        receipt = read_tree(mat, RECEIPT)
    except Missing:
        return leg("SCRATCHMIRROR", False, "receipt missing: %s" % RECEIPT)
    bad = []
    if "--file" not in receipt:
        bad.append("receipt does not show census validate --file")
    if re.search(r"(?i)(?:exit|rc)\s*[=:]?\s*0", receipt) is None:
        bad.append("receipt does not show exit 0")
    missing = [sid for sid in cfg["rows"] if sid not in receipt]
    if missing:
        bad.append("receipt does not carry %s" % ", ".join(missing))
    for e in cfg["entries"]:
        if os.path.basename(e) not in receipt:
            bad.append("receipt does not carry the entry %s" % os.path.basename(e))
    first = cfg["rows"][0] if cfg["rows"] else None
    append_commit = None
    if first:
        for rev in git(root, "rev-list", "--reverse",
                       "%s..%s" % (cfg["base"], ctx["lands"]),
                       "--", REGISTRY).stdout.split():
            text = git(root, "show", "%s:%s" % (rev, REGISTRY)).stdout
            if first in parse_rows(text):
                append_commit = rev
                break
    if append_commit is None:
        bad.append("no registry-append commit for %s in base..lands" % first)
    revs = git(root, "rev-list", "--reverse", "%s..%s" % (cfg["base"], ctx["lands"]),
               "--", RECEIPT).stdout.split()
    if not revs:
        bad.append("receipt is not committed in base..lands")
    elif append_commit is not None:
        if revs[0] == append_commit:
            bad.append("receipt committed in the registry-append commit (not before)")
        elif not is_ancestor(root, revs[0], append_commit):
            bad.append("receipt commit %s is not before the append commit %s"
                       % (revs[0][:12], append_commit[:12]))
    return leg("SCRATCHMIRROR", not bad, "; ".join(dedupe(bad)))


def _guard_files(mat):
    """Every file under the assimilation tree (the guard dir lives inside it)."""
    out = []
    if not os.path.isdir(os.path.join(mat, ASSIM)):
        return out
    for rel in tree_files(mat, ASSIM):
        try:
            out.append((rel, read_tree(mat, rel)))
        except Missing:
            continue
    return out


def _negated(line):
    return re.search(r"(?i)\b(not|no|none|zero|missed|absent|never)\b", line)


def leg_collcheck(ctx):
    """COLLCHECK: no adopted id in reg-ids or collisions; the indent guard
    proves a 1-3-space collision IS found and a 4-space one is NOT; the
    regenerated map records old->new for every adopted id."""
    mat, cfg = ctx["mat"], ctx["cfg"]
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
    reg_ids = set(TOKEN_RE.findall(read_tree(mat, d + "/" + v[0])))
    staged_ids = set(TOKEN_RE.findall(read_tree(mat, d + "/" + v[1])))
    collide_ids = set(TOKEN_RE.findall(read_tree(mat, d + "/" + v[2])))
    bad = []
    if not staged_ids:
        bad.append("staged-ids is empty")
    for sid in cfg["rows"]:
        if sid in reg_ids:
            bad.append("%s present in reg-ids (id not free)" % sid)
        if sid in collide_ids:
            bad.append("%s listed in collisions" % sid)
    for sid, staged in cfg["row_staged"].items():
        if staged not in staged_ids:
            bad.append("staged id %s (-> %s) absent from staged-ids" % (staged, sid))

    base_rows = set()
    try:
        base_rows = set(parse_rows(read_tree(ctx["mat_base"], REGISTRY)))
    except Missing:
        pass
    lands_rows = set()
    try:
        lands_rows = set(parse_rows(read_tree(mat, REGISTRY)))
    except Missing:
        pass
    real_ids = base_rows | lands_rows | set(cfg["rows"]) | set(cfg["reused"])

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
        planted = [p for p in INDENTED_ROW_RE.findall(text) if p not in real_ids]
        if planted and indent_ok is None:
            for pid in planted:
                hit = [l for l in lines
                       if pid in l and not _negated(l) and positive.search(l)]
                if hit:
                    indent_ok = (rel, pid, hit[0].strip()[:90])
                    break
        fours = [p for p in FOURSPACE_ROW_RE.findall(text) if p not in real_ids]
        if four_ok is None:
            for pid in fours:
                hit = [l for l in lines
                       if (pid in l or re.search(r"(?i)4[- ]space|four[- ]space", l))
                       and _negated(l) and negative.search(l)]
                if hit:
                    four_ok = (rel, pid, hit[0].strip()[:90])
                    break
        if four_ok is None:
            # the round-73 shape: a control file that states the 4-space plant
            # was not seen, without printing the row itself.
            hit = [l for l in lines
                   if re.search(r"(?i)4[- ]space|four[- ]space", l)
                   and _negated(l) and negative.search(l)]
            if hit:
                four_ok = (rel, None, hit[0].strip()[:90])
    if indent_ok is None:
        bad.append("no indent-guard proof under %s (a planted 1-3-space row with a "
                   "positive detection marker)" % GUARD_DIR)
    else:
        rel, pid, line = indent_ok
        text = read_tree(mat, rel)
        if re.search(r"^ {4,}\|\s*%s\s*\|" % pid, text, re.M):
            bad.append("guard proof %s plants %s at 4+ spaces, not 1-3"
                       % (rel, pid))
    if four_ok is None:
        bad.append("no four-space control under %s (a planted 4-space row with a "
                   "not-found marker)" % GUARD_DIR)
    elif four_ok[1] is not None:
        rel, pid, line = four_ok
        text = read_tree(mat, rel)
        if pid in set(INDENTED_ROW_RE.findall(text)):
            bad.append("four-space control %s plants %s inside the 1-3-space "
                       "grammar" % (rel, pid))

    recs = _map_records(ctx)
    if not recs:
        bad.append("no renumber map records at the freeze (%s:%s)"
                   % (ctx["cfg"]["freeze"], ctx["cfg"]["map_path"]))
    else:
        try:
            lands_rows_text = parse_rows(read_tree(mat, REGISTRY))
        except Missing:
            lands_rows_text = {}
        for sid in cfg["rows"]:
            cands = [(old, new, url) for (old, new), url in recs.items()
                     if new == sid]
            if not cands:
                bad.append("map records no old->new for %s" % sid)
                continue
            old, new, url = cands[0]
            want_old = cfg["row_staged"].get(sid)
            if want_old and old != want_old:
                bad.append("map maps %s -> %s (row_set says staged %s)"
                           % (old, sid, want_old))
            if url:
                keys = _row_url_keys(lands_rows_text, sid)
                if keys and norm_url(url) not in keys:
                    bad.append("map record %s -> %s carries a URL the row does not "
                               "name: %s" % (old, sid, url))
    return leg("COLLCHECK", not bad, "; ".join(dedupe(bad)))


def leg_frozencfg(ctx):
    """FROZENCFG (H1): every constant came from `git show <freeze>:claims.json`;
    <freeze> is a strict ancestor of <lands>; the graded tree's claims.json is
    the frozen one (a config edited after the freeze is a junk landing)."""
    root, lands, cfg = ctx["root"], ctx["lands"], ctx["cfg"]
    freeze = cfg["freeze"]
    bad = []
    chain = git(root, "rev-list", "--first-parent", lands).stdout.split()
    if freeze not in chain:
        bad.append("freeze %s is not on lands' first-parent chain"
                   % freeze[:12])
    if not is_ancestor(root, cfg["base"], lands):
        bad.append("claim base %s is not an ancestor of lands" % cfg["base"][:12])
    map_r = git_bytes(root, "show", "%s:%s" % (freeze, cfg["map_path"]))
    if map_r.returncode != 0:
        bad.append("map %s is not committed at freeze %s"
                   % (cfg["map_path"], freeze[:12]))
        map_sha = "-"
    else:
        map_sha = hashlib.sha256(map_r.stdout).hexdigest()
        if map_sha != cfg["map_sha256"]:
            bad.append("map %s at freeze hashes to %s, the frozen map.sha256 "
                       "is %s" % (cfg["map_path"], map_sha[:16],
                                  cfg["map_sha256"][:16]))
    r = git_bytes(root, "show", "%s:%s" % (lands, CLAIMS))
    if r.returncode != 0:
        bad.append("%s is not committed at lands" % CLAIMS)
    elif hashlib.sha256(r.stdout).hexdigest() != cfg["frozen_sha256"]:
        bad.append("%s at lands differs from the frozen bytes (counter config "
                   "edited in the graded tree)" % CLAIMS)
    nums = sorted(int(s[1:]) for s in cfg["rows"])
    if nums != list(range(nums[0], nums[0] + len(nums))):
        bad.append("frozen row_set %s is not contiguous" % cfg["rows"])
    if not cfg["entries"]:
        bad.append("frozen entries list is empty")
    if not cfg["fragments"] or not cfg["cjk_terms"]:
        bad.append("frozen ground lists are empty")
    detail = ("constants from git show %s:%s (sha256 %s): rows=%s reused=%s "
              "entries=%d fragments=%d cjk_terms=%d refused=%s forced=%s "
              "access_date=%s"
              % (freeze[:12], CLAIMS, cfg["frozen_sha256"][:16],
                 " ".join(cfg["rows"]), " ".join(cfg["reused"]),
                 len(cfg["entries"]), len(cfg["fragments"]),
                 len(cfg["cjk_terms"]), ",".join(cfg["refused_staged"]) or "-",
                 ",".join(cfg["forced_new_quotes"]) or "-", cfg["access_date"]))
    if bad:
        detail = "; ".join(bad) + " | " + detail
    return leg("FROZENCFG", not bad, detail)


def _readme_sections(text):
    """[(partition, start, end)] for the `## <part>/ (N)` sections, in order."""
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
    """The entry's own `- topic:` header value (first one, beyond the header)."""
    try:
        text = read_tree(mat, path)
    except Missing:
        return None
    for line in header_block(text):
        m = re.match(r"^[-*\s]*topic:\s*(.*)$", line)
        if m:
            return m.group(1).strip()
    return None


def _md_count(mat, prefix):
    return len([p for p in tree_files(mat, prefix) if p.endswith(".md")])


def leg_index(ctx):
    """INDEX: corpus/README.md carries one culture-material row per adopted
    entry with the entry's own `- topic:` text verbatim, and the live footer's
    total and six-partition vector equal the landed tree; older footers are
    preserved byte-identically from base."""
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
    sections = _readme_sections(lands_text)
    parts = [p for p, _s, _e in sections]
    cm = [s for s in sections if s[0] == "culture-material"]
    if not cm:
        bad.append("%s has no `## culture-material/ (N)` section" % README)
    cm_text = lands_text[cm[0][1]:cm[0][2]] if cm else ""
    for e in cfg["entries"]:
        base = os.path.basename(e)
        topic = _entry_topic(mat, e)
        if topic is None:
            bad.append("%s has no `- topic:` header line" % e)
        hits = []
        for line in lands_text.splitlines():
            rm = README_ROW_RE.match(line)
            if rm and rm.group(1) == base:
                hits.append(rm.group(2).strip())
        if len(hits) != 1:
            bad.append("%s has %d index rows (want exactly one)"
                       % (base, len(hits)))
            continue
        in_section = False
        for line in cm_text.splitlines():
            rm = README_ROW_RE.match(line)
            if rm and rm.group(1) == base:
                in_section = True
                break
        if not in_section:
            bad.append("%s index row is not inside the culture-material section"
                       % base)
        if topic is not None and hits[0] != topic:
            bad.append("%s index row is not the entry's `- topic:` text verbatim"
                       % base)
    blocks = _footer_blocks(lands_text)
    if not blocks:
        bad.append("%s carries no `Counts checked` footer" % README)
    else:
        m = README_FOOTER_RE.search(blocks[-1])
        if not m:
            bad.append("the last `Counts checked` footer carries no "
                       "(total N files; directory totals V) reading")
        else:
            total = int(m.group(1))
            vector = [int(x) for x in m.group(2).split("/") if x]
            actual_total = _md_count(mat, KNOWLEDGE)
            actual_vec = [_md_count(mat, KNOWLEDGE + "/" + part)
                          for part in parts]
            if total != actual_total:
                bad.append("last footer total %d != the %d .md files at lands"
                           % (total, actual_total))
            if len(parts) != 6:
                bad.append("README declares %d partition sections (want six)"
                           % len(parts))
            if vector != actual_vec:
                bad.append("last footer vector %s != the landed partition "
                           "counts %s" % (vector, actual_vec))
    for blk in _footer_blocks(base_text)[:-1]:
        if blk not in blocks:
            bad.append("an older `Counts checked` footer is not preserved "
                       "byte-identically: %r" % blk.splitlines()[0][:60])
    return leg("INDEX", not bad, "; ".join(dedupe(bad)))


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
    results = []
    for name, fn in LEGS:
        try:
            ok = fn(ctx)
        except Missing as e:
            ok = leg(name, False, "missing at lands: %s" % e)
        except (OSError, RuntimeError, subprocess.SubprocessError) as e:
            ok = leg(name, False, "%s: %s" % (type(e).__name__, e))
        results.append((name, bool(ok)))
    passed = sum(1 for _n, ok in results if ok)
    return passed, len(results), results


def print_receipt(root, lands, mat, cfg, how):
    tree = git(root, "rev-parse", "%s^{tree}" % lands).stdout.strip()
    head = git(root, "rev-parse", "HEAD").stdout.strip()
    print("# round-74 acceptance counter — claim C "
          "(shokuknow worldbuilding-setting-practice assimilation)")
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
             " ".join(cfg["row_staged"][r] for r in cfg["rows"])))
    print("# reused rows: %s (staged %s)"
          % (" ".join(cfg["reused"]) or "-",
             " ".join(cfg["reused_staged"][r] for r in cfg["reused"]) or "-"))
    print("# entries: %s" % " ; ".join(cfg["entries"]))
    print()


def refuse(msg):
    """Refuse to grade (H1).  The verdict line is a FAIL, never a PASS: no leg
    ran, and the exit code (2) marks the refusal as an input error, not a
    graded verdict."""
    print("REFUSED: %s" % msg, file=sys.stderr)
    print("ACCEPT-C-74: FAIL legs=0/%d (refused: %s)"
          % (len(LEGS), msg.splitlines()[0]))
    return 2


def main(argv=None):
    ap = argparse.ArgumentParser(
        description="round-74 coverage counter (claim C)")
    ap.add_argument("--root", default=".", help="lane repository root")
    ap.add_argument("--lands", default=None,
                    help="required lands revision (40-hex commit)")
    ap.add_argument("--freeze", default=None,
                    help="required freeze revision (40-hex commit; a strict "
                         "ancestor of --lands)")
    ap.add_argument("--fleet-root", default=None,
                    help="fleet root (default: the lane's parent directory)")
    ap.add_argument("--selftest", action="store_true", help="run in-process cases")
    args = ap.parse_args(argv)

    if args.selftest:
        return run_selftest()

    if not args.lands or not re.fullmatch(r"[0-9a-fA-F]{40}", args.lands.strip()):
        print("ERROR: --lands must be a 40-hex commit "
              "(the worktree is never graded, QUALITY 19)", file=sys.stderr)
        return 2
    if not args.freeze or not re.fullmatch(r"[0-9a-fA-F]{40}", args.freeze.strip()):
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
            print("ERROR: %s revision not found: %s" % (name, rev), file=sys.stderr)
            return 2
    try:
        cfg = load_frozen_config(root, freeze)
    except ConfigError as e:
        return refuse("%s" % e)
    if lands == cfg["base"]:
        return refuse("lands %s is the frozen claim base %s (the do-nothing "
                      "control: no data landed)" % (lands[:12], cfg["base"][:12]))
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

    with tempfile.TemporaryDirectory(prefix="r74-lands-") as tmp:
        mat = os.path.join(tmp, "clone")
        mat_base = os.path.join(tmp, "base")
        os.makedirs(mat_base)
        try:
            clone_at(root, lands, mat)
            how = ("git clone of %s, checkout --detach %s"
                   % (os.path.abspath(root), lands[:12]))
        except RuntimeError:
            shutil.rmtree(mat, ignore_errors=True)
            os.makedirs(mat)
            materialize(root, lands, mat)
            how = "git archive of %s (the clone refused the revision)" % lands[:12]
        try:
            materialize(root, cfg["base"], mat_base)
        except RuntimeError as e:
            print("ERROR: %s" % e, file=sys.stderr)
            return 2
        ctx = {"root": root, "lands": lands, "mat": mat, "mat_base": mat_base,
               "cfg": cfg, "fleet_root": fleet_root}
        print_receipt(root, lands, mat, cfg, how)
        passed, total, _results = run_legs(ctx)
    ok = passed == total
    print("ACCEPT-C-74: %s legs=%d/%d" % ("PASS" if ok else "FAIL", passed, total))
    return 0 if ok else 1


# --------------------------------------------------------------------------
# selftest — every fixture repo is a fresh mktemp dir, every git call names it
# --------------------------------------------------------------------------

def gitq(lane, *args):
    return subprocess.run(["git", "-C", lane, *args],
                          capture_output=True, text=True)


def git_write(lane, rel, content):
    p = os.path.join(lane, rel)
    d = os.path.dirname(p)
    if d:
        os.makedirs(d, exist_ok=True)
    with open(p, "w", encoding="utf-8") as fh:
        fh.write(content)


def git_commit(lane, message):
    r = gitq(lane, "add", "-A")
    if r.returncode != 0:
        raise RuntimeError("git add failed: %s" % r.stderr)
    r = gitq(lane, "-c", "user.name=selftest", "-c", "user.email=selftest@local",
              "commit", "-q", "-m", message)
    if r.returncode != 0:
        raise RuntimeError("git commit failed: %s" % r.stderr)
    return gitq(lane, "rev-parse", "HEAD").stdout.strip()


ENTRY_ONE = "corpus/knowledge/culture-material/worldbuilding-setting-practice.md"
ENTRY_TWO = ("corpus/knowledge/culture-material/"
             "worldbuilding-setting-practice.amend-2026-10-23.md")
OLD_ENTRY = "corpus/knowledge/culture-material/old-entry.md"
LONG_ENTRY = "corpus/knowledge/linguistics/long-entry.md"

U_LITMEMO = "https://litmemo.com/ja/blog/novel-worldbuilding-guide"
U_TUDUKU = "https://tuduku.space/column/novel-worldbuilding"
U_CW25 = "https://www.chinawriter.com.cn/n1/2025/0605/c404024-40494534.html"
U_CW22 = "https://www.chinawriter.com.cn/n1/2022/1207/c404024-32582252.html"
U_SIDOROVA = "http://www.philol.msu.ru/~sidorova/files/conlangs.pdf"

Q877 = "Глава 1: вымышленные языки"
Q881 = "設定ノートを一冊つくる"
Q882 = "世界観設定の5要素"
Q883 = "我先设定世界观，再考虑怎么升级"
Q884 = "二十章以内に世界観を出す"

UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/130.0 Safari/537.36")

FIXTURE_FILLER = (
    "This fixture sentence exists only to carry a body past the word floor "
    "the counter derives from the base knowledge tree. ")


def _pad_to(text, target):
    while len(text.split()) < target:
        text += FIXTURE_FILLER
    return text


BASE_REGISTRY = """\
# SOURCES — selftest registry

## Registry

| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
| S001 | Fixture one — https://example.com/one | docs | A | s | a | teaches one | mined | 2026-10-19 | 90d | %s |
| S875 | Fixture two — https://example.com/two | docs | B | s | a | teaches two | mined | 2026-10-19 | 180d | — |
| S877 | Fixture sidorova — %s | book | B | s | Глава 1 | teaches sidorova | mined | 2026-10-19 | 180d | %s |
| S880 | Fixture four — https://example.com/four | docs | B | s | a | teaches four | mined | 2026-10-19 | 180d | — |
""" % (OLD_ENTRY, U_SIDOROVA, OLD_ENTRY)

OLD_ENTRY_TEXT = _pad_to("""\
# Old fixture entry

source: S001 — https://example.com/one — §1 — fetched 2026-10-19
verified-at: 2026-10-19
recheck: 90d — re-run the row recheck commands (ran 2026-10-19)
ground: the fixture's scoped domain.
- topic: a fixture topic.
- gap filled: none needed for the fixture.
- sources: the row above.
- couples: nothing.
- scope: a fixture only.

## Body

A fixture body long enough to give the floor a value. It repeats a sentence so
that the word floor is a number the fixture entries can clear without effort.
""", 470)

LONG_ENTRY_TEXT = _pad_to("""\
# Long fixture entry

source: S001 — https://example.com/one — §2 — fetched 2026-10-19
verified-at: 2026-10-19
recheck: 90d — re-run the row recheck commands (ran 2026-10-19)
ground: the fixture's second base entry.
- topic: a long base entry topic.
- gap filled: none needed for the fixture.
- sources: the row above.
- couples: nothing.
- scope: a fixture only.

## Body

""", 470)

BASE_README = """\
# corpus index fixture

## linguistics/ (1)

- `long-entry.md` — a long base entry topic

## myth-symbol/ (0)

## culture-material/ (1)

- `old-entry.md` — a fixture topic

## synthesis/ (0)

## verification/ (0)

## civilizations/ (0)

Counts checked 2026-10-24 from the repo root:
`find corpus/knowledge -type f -name '*.md' | wc -l`
(total 1 files; directory totals 1/0/1/0/0/0).

Counts checked 2026-10-25 from the repo root:
`find corpus/knowledge -type f -name '*.md' | wc -l`
(total 2 files; directory totals 1/0/1/0/0/0).
"""

ENTRY_ONE_TEXT = _pad_to("""\
# Worldbuilding setting practice — fixture entry

source: S881 — %s — §2 設定ノート — fetched 2026-10-25
source: S877 — %s — Глава 1, printed p. 10 — fetched 2026-10-25
verified-at: 2026-10-25
recheck: 180d — re-run the row recheck commands (ran 2026-10-25)
ground: the wave brief's scoped domain, which the lane served from no craft guide.
- topic: how a practitioner records and scopes a fictional setting.
- gap filled: the registry held no worldbuilding-setting source at base.
- sources: the two rows above.
- couples: the amendment entry.
- scope: a craft method for authoring settings; it decides no world's facts.

## Build order

1. The five-step build order is carried by S881.
2. The layered world-view block is carried by S877.
3. A third sentence pads the body so the word floor is cleared.
4. A fourth sentence pads the body so the word floor is cleared.
5. A fifth sentence pads the body so the word floor is cleared.

## Practice

The settings-note document is the single source of truth for the setting, and
the layered world-view is written before the plot. This paragraph exists so the
fixture body is comfortably longer than the base tree's smallest entry, which
is the floor the counter derives rather than trusts.
""" % (U_LITMEMO, U_SIDOROVA), 700)

ENTRY_TWO_TEXT = _pad_to("""\
# Worldbuilding setting practice — fixture amendment

source: S882 — %s — §3 世界観設定の5要素 — fetched 2026-10-25
source: S883 — %s — 第2节 — fetched 2026-10-25
source: S884 — %s — 第5段 — fetched 2026-10-25
source: S877 — %s — Глава 1, printed p. 10 — fetched 2026-10-25
verified-at: 2026-10-25
recheck: 180d — re-run the row recheck commands (ran 2026-10-25)
ground: the base entry cited one craft guide only.
- topic: the five-element block and the delivery schedule.
- gap filled: the CJK practitioner detail the base entry could not supply.
- sources: the four rows above.
- couples: the base entry.
- scope: a craft method for authoring settings; it decides no world's facts.

## Five elements

1. The five-element block is carried by S882.
2. The interview's build order is carried by S883.
3. The delivery schedule is carried by S884.
4. The scholarly frame is carried by S877.
5. A fifth sentence pads the body so the word floor is cleared.

## Delivery

World-view information is released gradually and early, within roughly the
first twenty chapters, only where the opening stays interesting. This paragraph
exists so the fixture body is comfortably longer than the base tree's smallest
entry, which is the floor the counter derives rather than trusts.
""" % (U_TUDUKU, U_CW25, U_CW22, U_SIDOROVA), 700)

ROWS_APPEND = """\
| S881 | LitMemo 創作ノート — %s | blog | B | s | §2 「%s」 | teaches the five-step build order | mined | 2026-10-25 | 180d | %s |
| S882 | tuduku コラム — %s | blog | B | s | §3 「%s」 | teaches the five-element block | mined | 2026-10-25 | 180d | %s |
| S883 | 中国作家网 interview (2025) — %s | paper | B | s | 第2节 「%s」 | teaches the build order in the author's words | mined | 2026-10-25 | 180d | %s |
| S884 | 中国作家网 interview (2022) — %s | paper | B | s | 第5段 「%s」 | teaches the delivery schedule | mined | 2026-10-25 | 180d | %s |
""" % (U_LITMEMO, Q881, ENTRY_ONE,
       U_TUDUKU, Q882, ENTRY_TWO,
       U_CW25, Q883, ENTRY_TWO,
       U_CW22, Q884, ENTRY_TWO)

LESSON_TEXT = """\
# Round 74 — selftest lesson

## Gate

Admitted this round (every row opened 2026-10-25 by a plain request with a
recorded browser-shaped UA; staged ids re-pointed by document, never by
arithmetic):

| source | access date | quote (<=25 words) | locator | evidence capture | verdict |
|---|---|---|---|---|---|
| S877 — %s | 2026-10-25 | «%s» | Глава 1, printed p. 10 | reports/round-74/evidence/S877.txt (HTTP 200) | admitted |
| S881 — %s | 2026-10-25 | 「%s」 | §2 見出し | reports/round-74/evidence/S881.txt (HTTP 200) | admitted |
| S882 — %s | 2026-10-25 | 「%s」 | §3 見出し | reports/round-74/evidence/S882.txt (HTTP 200) | admitted |
| S883 — %s | 2026-10-25 | 「%s」 | 第2节 | re-quote: the staged span was absent (R68 refusal, URL-quote mispairing); reports/round-74/evidence/S883.txt | admitted |
| S884 — %s | 2026-10-25 | 「%s」 | 第5段 | re-quote: the staged span was absent (R71 refusal, URL-quote mispairing); reports/round-74/evidence/S884.txt | admitted |

Refused or not adopted from the assimilation set (reason + flip; every row
names the probed URL):

| staged entry | staged rows | reason | flip | probed URLs | verdict |
|---|---|---|---|---|---|
| worldbuilding base entry (staged S882) | S882 | the document already holds lane row S877; not appended | cite S877 in place | %s | rejected |
| worldbuilding folded passage (staged S895) | S895 | the folded passage was dropped from the staged set | a later round re-opens it | https://example.com/refused-c | rejected |
| naming-systems family | S886 | payload outside the declared set | a later round takes it | https://example.com/refused-a | rejected |
| calendar-festival-systems family | S887 | payload outside the declared set | a later round takes it | https://example.com/refused-b | rejected |

Counts: 2 adopted / 4 path-present with differing staged bytes / 34 refused of
the 40 staged knowledge files.

Earlier-refused quotes: staged S899 and staged S900 were refused in rounds 68
and 71 because the staged quoted spans were absent from the pages (a
URL-quote mispairing, not a dead payload); both are re-quoted from the page
this round.

Not adopted this round: the calendar-festival-systems and naming-systems
staged families.

## Registry in-place change

S877 used-by: %s -> %s, %s

## Quarantine

Register rows S816 and S817 are REFUSED-as-staged (their spans are absent,
re-confirmed this round). The four clearing conditions: refused rows stay
refused; each document is re-opened as new rows; quotes located this round;
admitted bytes are a round-74 entry.

## Mistakes

| class | evidence | captured-by | fix | state |
|---|---|---|---|---|
| fixture | selftest only | n/a | n/a | new |
""" % (U_SIDOROVA, Q877, U_LITMEMO, Q881, U_TUDUKU, Q882, U_CW25, Q883,
       U_CW22, Q884, U_SIDOROVA, OLD_ENTRY, OLD_ENTRY, ENTRY_ONE)

GROUND_TEXT = """\
# round-74 gap sweep (selftest fixture)
# stamp: 2026-10-25 10:00:00 UTC
$ find corpus/knowledge -iname '*worldbuilding-setting*' | wc -l
0
litmemo.com: 0
tuduku.space: 0
chinawriter.com.cn: 0
設定ノート: 0
世界観: 0
世界观: 0
gap-sweep at the 4-row registry: owners 0
"""

RECEIPT_TEXT = """\
# round-74 scratch-mirror validation receipt (selftest fixture)
# stamp: 2026-10-25 10:00:00 UTC
census validate --file /tmp/r74-mirror/corpus/SOURCES.md
exit 0
rows present in mirror: S881 S882 S883 S884
entries in mirror: %s, %s
""" % (ENTRY_ONE, ENTRY_TWO)

GUARD_TEXT = """\
# 0-3-space-indent guard proof (selftest fixture)

PLANTED (2 leading spaces): S990
   | S990 | planted indented row — https://fixture.example/planted | docs | B | s | §1 | planted | mined | 2026-10-25 | 90d | — |

parser output: collision detected: S990 present in reg-ids (guard) -> 1
exit 1
"""

FOURSPACE_R73_TEXT = """\
# four-space control (round-74 fixture, round-73 shape): a 4-space-indented
# planted row is code per the census parser and is NOT found by the 0-3-space
# guard; the 2-space plant in guard-proof.txt IS found (collision)
reg-ids with 4-space plant (guard): 4 (the fixture registry holds 4 rows;
4 = the 4-space plant is NOT seen)
collision detected for S990: 0 (0 = not found, as required for 4 spaces)
"""

FOURSPACE_TEXT = """\
# four-space control (selftest fixture)

4-space plant: S991
    | S991 | four-space planted row | docs | B | s | §1 | planted | mined | 2026-10-25 | 90d | — |

4-space plant found: 0 (0 = not found, as required for 4 spaces)
"""

MAP_TEXT = """\
{
 "round": 74,
 "supersedes": ".ufo/waves/round-73/assimilation/id-renumber-map.json",
 "assignments": [
  {"staged_id": "S883", "new_target": "S881", "url": "%s"},
  {"staged_id": "S884", "new_target": "S882", "url": "%s"},
  {"staged_id": "S899", "new_target": "S883", "url": "%s"},
  {"staged_id": "S900", "new_target": "S884", "url": "%s"}
 ],
 "map": {"S883": "S881", "S884": "S882", "S899": "S883", "S900": "S884"}
}
""" % (U_LITMEMO, U_TUDUKU, U_CW25, U_CW22)

STAGED_IDS_TEXT = "S882\nS883\nS884\nS899\nS900\n"
REG_IDS_TEXT = "S001\nS875\nS877\nS880\n"
COLLISIONS_TEXT = "S001\nS002\n"

CENSUS_STUB_OK = "#!/bin/sh\nprintf 'kotodama\\tok\\tstub\\n'\nexit 0\n"
CENSUS_STUB_FAIL = "#!/bin/sh\nprintf 'kotodama\\tE06\\tS881 tier=Z\\n'\nexit 1\n"

CENSUS_SH_REAL = """\
#!/bin/sh
# selftest census stub (delegates nothing; the counter only reads the TSV)
printf 'kotodama\\tok\\tstub\\n'
exit 0
"""


def _evidence_text(sid, url, quote, window=None, ua=UA, sha=None, status="200",
                   scope=None, visible=None, window_sha=None):
    body = window if window is not None else (
        ("filler " * 700) + quote + (" tail" * 20))
    scope = scope or "excerpt"
    if visible is None:
        visible = len(body)
    payload = body.encode("utf-8")
    digest = window_sha or hashlib.sha256(payload).hexdigest()
    return ("# evidence %s — claim C GATE (round 74)\n"
            "url: %s\n"
            "http: %s\n"
            "bytes: 1234\n"
            "sha256: %s\n"
            "fetched: 2026-10-25T10:00:00Z\n"
            "ua: %s\n"
            "content-type: text/html\n"
            "final-url: %s\n"
            "extract: html tags stripped\n"
            "quote-found: yes\n"
            "quote-words: %d\n"
            "quote-chars: %d\n"
            "quote-found-verbatim: yes\n"
            "window: chars=%d pad=400 before=10 after=10\n"
            "window-scope: %s\n"
            "visible-chars: %s\n"
            "window-sha256: %s\n"
            "window-bytes: %d\n"
            "window-rule: sha256 of the single stored window line, UTF-8\n"
            "fetch: GET %s\n"
            "user-agent: %s\n"
            "access-date: 2026-10-25\n"
            "http-status: %s\n"
            "content-length: 1234\n"
            "fetch-command: curl -sS -A '<UA>'\n"
            "locator: fixture locator\n"
            "normalise: NFKC(per-character)+whitespace-fold; matched=verbatim\n"
            "quote: %s\n"
            "--- window ---\n"
            "%s\n"
            "--- quote ---\n"
            "%s\n"
            % (sid, url, status, sha or ("ab" * 32), ua, url,
               len(quote.split()), len(quote), len(body), scope, visible,
               digest, len(payload), url, ua, status, quote, body, quote))


QUOTES = {"S877": Q877, "S881": Q881, "S882": Q882, "S883": Q883, "S884": Q884}
URLS = {"S877": U_SIDOROVA, "S881": U_LITMEMO, "S882": U_TUDUKU,
        "S883": U_CW25, "S884": U_CW22}

LEG_NAMES = ["ENTRIES", "ROWS", "REPOINTED", "GATE", "EVIDENCE", "REJECTS",
             "GROUND", "CITEDLINES", "CENSUS", "SCRATCHMIRROR", "COLLCHECK",
             "FROZENCFG", "INDEX"]


def claims_fixture(base, narrow=False, legcount=13):
    rows = [{"id": "S881", "staged": "S883"},
            {"id": "S882", "staged": "S884"},
            {"id": "S883", "staged": "S899"},
            {"id": "S884", "staged": "S900"}]
    if narrow:
        rows = rows[:3]
    legs = ["%s: selftest fixture leg" % n for n in LEG_NAMES]
    if legcount and legcount < len(legs):
        legs = legs[:legcount]
    return {
        "round": 74,
        "status": "selftest fixture",
        "frozen": "selftest",
        "base": base,
        "claims": [{
            "id": "C",
            "axis": "coverage",
            "row_set": rows,
            "reused_rows": [{"id": "S877", "staged": "S882",
                             "note": "in-place used-by change only"}],
            "entries": [ENTRY_ONE, ENTRY_TWO],
            "rejects": {
                "refused_staged_not_appended": ["S882"],
                "forced_new_quotes": ["S899", "S900"],
                "folded_dropped": ["S895"],
                "refused_files": ["naming-systems x11",
                                  "calendar-festival-systems x3"],
                "path_present_bytes_differ": [
                    "culture-material/heritage-taxonomy-models.md",
                    "culture-material/"
                    "heritage-taxonomy-models.amend-2026-10-24-r13.md",
                    "linguistics/conlang-scholarship.md",
                    "linguistics/conlang-scholarship.amend-2026-10-23.md"],
                "counts": {"adopted": 2, "path_present": 4, "refused": 34,
                           "total_staged_files": 40},
            },
            "ground": {"fragments": ["litmemo.com", "tuduku.space",
                                     "chinawriter.com.cn"],
                       "cjk_terms": ["設定ノート", "世界観", "世界观"]},
            "map": {"path": RENUMBER_MAP,
                    "sha256": hashlib.sha256(
                        MAP_TEXT.encode("utf-8")).hexdigest()},
            "legs": legs,
            "access_date": "2026-10-25",
        }],
    }


def _topic_of(text):
    for line in header_block(text):
        m = re.match(r"^[-*\s]*topic:\s*(.*)$", line)
        if m:
            return m.group(1).strip()
    return ""


def _readme_lands(mut):
    """The lands `corpus/README.md`: two culture-material rows + a live footer."""
    rows = [
        "- `%s` — %s" % (os.path.basename(ENTRY_TWO), _topic_of(ENTRY_TWO_TEXT)),
        "- `%s` — %s" % (os.path.basename(ENTRY_ONE), _topic_of(ENTRY_ONE_TEXT)),
    ]
    if mut.get("index_missing_row"):
        rows = rows[:1]
    if mut.get("index_topic_mismatch"):
        rows[1] = rows[1].replace("scopes", "frames")
    text = BASE_README.replace(
        "- `old-entry.md` — a fixture topic\n",
        "- `old-entry.md` — a fixture topic\n" + "\n".join(rows) + "\n")
    vector = "1/0/2/0/0/0" if mut.get("index_footer_vector") else "1/0/3/0/0/0"
    total = "5" if mut.get("index_footer_total") else "4"
    text = text.rstrip("\n") + (
        "\n\nCounts checked 2026-10-25 from the repo root:\n"
        "`find corpus/knowledge -type f -name '*.md' | wc -l`\n"
        "(total %s files; directory totals %s).\n" % (total, vector))
    if mut.get("index_older_footer_edited"):
        text = text.replace("(total 1 files; directory totals 1/0/1/0/0/0).",
                            "(total 9 files; directory totals 9/0/0/0/0/0).")
    return text


def build_fixture(prefix, mut=None):
    """A fresh fixture lane + fleet root.  Returns (lane, fleet, base, freeze,
    lands).  Every git call names the fixture."""
    mut = mut or {}
    lane = tempfile.mkdtemp(prefix=prefix + "-", suffix="-lane")
    fleet = tempfile.mkdtemp(prefix=prefix + "-", suffix="-fleet")
    git_write(fleet, "scripts/sources-census.sh",
              CENSUS_STUB_FAIL if mut.get("census_fail") else CENSUS_STUB_OK)
    os.chmod(os.path.join(fleet, "scripts/sources-census.sh"), 0o755)
    if gitq(lane, "init", "-q").returncode != 0:
        raise RuntimeError("git init failed")
    if gitq(lane, "rev-parse", "--show-toplevel").stdout.strip() != lane:
        raise RuntimeError("fixture toplevel mismatch")

    git_write(lane, REGISTRY, BASE_REGISTRY)
    git_write(lane, OLD_ENTRY, OLD_ENTRY_TEXT)
    git_write(lane, LONG_ENTRY, LONG_ENTRY_TEXT)
    git_write(lane, README, BASE_README)
    with open(os.path.join(LANE, "tools/check-cited-lines.py"),
              encoding="utf-8") as fh:
        git_write(lane, "tools/check-cited-lines.py", fh.read())
    if mut.get("entry_at_base"):
        git_write(lane, ENTRY_ONE, ENTRY_ONE_TEXT)
    base = git_commit(lane, "base")

    doc = claims_fixture(base, narrow=mut.get("claims_narrow"),
                         legcount=12 if mut.get("legcount_mismatch") else 13)
    if mut.get("claims_extra_rows"):
        doc["claims"][0]["row_set"].append({"id": "S885", "staged": "S901"})
    if mut.get("map_sha_mismatch"):
        doc["claims"][0]["map"]["sha256"] = "0" * 64
    git_write(lane, CLAIMS, json.dumps(doc, indent=1, ensure_ascii=False) + "\n")
    if mut.get("config_edited_in_lands"):
        pass  # rewritten at the lands commit, after the freeze
    if not mut.get("receipt_in_append"):
        receipt = RECEIPT_TEXT
        if mut.get("receipt_no_exit"):
            receipt = receipt.replace("exit 0", "exit 1")
        if mut.get("receipt_missing_ids"):
            receipt = receipt.replace("S884", "")
        git_write(lane, RECEIPT, receipt)
    git_write(lane, ASSIM + "/reg-ids", REG_IDS_TEXT)
    git_write(lane, ASSIM + "/staged-ids", STAGED_IDS_TEXT)
    collisions = COLLISIONS_TEXT
    if mut.get("collisions_adopted"):
        collisions += "S881\n"
    git_write(lane, ASSIM + "/collisions", collisions)
    if not mut.get("guard_missing"):
        git_write(lane, GUARD_DIR + "/guard-proof.txt", GUARD_TEXT)
    if not mut.get("guard_fourspace_missing"):
        git_write(lane, GUARD_DIR + "/four-space-control.txt",
                  FOURSPACE_R73_TEXT if mut.get("guard_r73shape") else FOURSPACE_TEXT)
    if not mut.get("map_missing"):
        git_write(lane, RENUMBER_MAP, MAP_TEXT)
    freeze = git_commit(lane, "freeze: claims.json + controls + mirror receipt")

    # ---- lands -----------------------------------------------------------
    if mut.get("no_data"):
        # the do-nothing control: lands is a commit after the freeze that lands
        # no claim-C artefact at all (tree == freeze's tree plus one scratch file).
        git_write(lane, "corpus/knowledge/synthesis/scratch.md",
                  "no claim-C data here\n")
        lands = git_commit(lane, "lands: no claim-C data (do-nothing control)")
        return lane, fleet, base, freeze, lands
    registry = BASE_REGISTRY + ROWS_APPEND
    if mut.get("staged_as_is"):
        registry = registry.replace(
            "| mined | 2026-10-25 | 180d | " + ENTRY_ONE + " |",
            "| mined | 2026-10-23 | 180d — `curl ... \\| grep -c x` -> 2 (ran 2026-10-23) | "
            + ENTRY_ONE + " |")
    if mut.get("usedby_stub"):
        registry = registry.replace("180d | " + ENTRY_TWO + " |",
                                    "180d | corpus/knowledge/stub.md |", 1)
    if mut.get("row_gap"):
        registry = "\n".join(l for l in registry.splitlines()
                             if not l.startswith("| S883 |")) + "\n"
    if mut.get("extra_row"):
        registry += ("| S885 | Extra — https://example.com/extra | docs | B | s | a | "
                     "teaches extra | mined | 2026-10-25 | 180d | — |\n")
    if mut.get("remove_row"):
        registry = "\n".join(l for l in registry.splitlines()
                             if not l.startswith("| S875 |")) + "\n"
    if mut.get("inplace_other"):
        registry = registry.replace(
            "| S880 | Fixture four — https://example.com/four | docs | B |",
            "| S880 | Fixture four — https://example.com/four | docs | C |")
    if mut.get("registry_prose"):
        registry = registry.replace("# SOURCES — selftest registry",
                                    "# SOURCES — selftest registry (amended)")
    if mut.get("anchor_no_quote"):
        registry = registry.replace("§2 「%s」" % Q881, "§2")
    if mut.get("map_url_absent"):
        registry = registry.replace("tuduku コラム — " + U_TUDUKU,
                                    "tuduku コラム — https://other.example/tuduku")
    added = ENTRY_TWO if mut.get("reused_usedby_wrong") else ENTRY_ONE
    registry = registry.replace(
        "| S877 | Fixture sidorova — %s | book | B | s | Глава 1 | teaches "
        "sidorova | mined | 2026-10-19 | 180d | %s |"
        % (U_SIDOROVA, OLD_ENTRY),
        "| S877 | Fixture sidorova — %s | book | B | s | Глава 1 | teaches "
        "sidorova | mined | 2026-10-19 | 180d | %s, %s |"
        % (U_SIDOROVA, OLD_ENTRY, added))
    if mut.get("reused_unlogged"):
        pass  # the lesson below simply omits the old->new line
    git_write(lane, REGISTRY, registry)

    if not mut.get("drop_entry_two"):
        if mut.get("stub_entry"):
            git_write(lane, ENTRY_TWO,
                      ENTRY_TWO_TEXT.split("## Five elements")[0])
        elif mut.get("stub_entry_400"):
            git_write(lane, ENTRY_TWO,
                      ENTRY_TWO_TEXT.split("## Five elements")[0]
                      + _pad_to("## Stub\n\n", 400))
        else:
            git_write(lane, ENTRY_TWO, ENTRY_TWO_TEXT)
    entry_one = ENTRY_ONE_TEXT
    if mut.get("placeholder_header"):
        entry_one = re.sub(r"(?m)^- topic:.*$", "- topic: TODO", entry_one, count=1)
    if mut.get("repoint_url"):
        entry_one = entry_one.replace("S881 — " + U_LITMEMO,
                                      "S881 — https://other.example/x")
    if mut.get("campaign_id"):
        entry_one = entry_one.replace(
            "5. A fifth sentence pads the body so the word floor is cleared.",
            "5. An earlier campaign id S899 stands here.")
    if mut.get("inline_unrelated"):
        entry_one = entry_one.replace(
            "5. A fifth sentence pads the body so the word floor is cleared.",
            "5. An unrelated lane row S875 stands here.")
    if mut.get("multi_id_line"):
        entry_one = entry_one.replace(
            "1. The five-step build order is carried by S881.",
            "1. The five-step build order is carried by S881 (S877).")
    git_write(lane, ENTRY_ONE, entry_one)

    lesson = LESSON_TEXT
    if mut.get("gate_quote_words"):
        lesson = lesson.replace("「%s」" % Q881,
                                '"' + " ".join("w%d" % i for i in range(30)) + '"')
    if mut.get("gate_quote_chars"):
        lesson = lesson.replace(
            "「%s」" % Q881,
            '"%s"' % " ".join(chr(0x41 + i) * 25 for i in range(4)))
    if mut.get("gate_reject_no_url"):
        lesson = lesson.replace("https://example.com/refused-a", "the probed URL")
        lesson = lesson.replace("https://example.com/refused-b", "the probed URL")
    if mut.get("gate_no_admit"):
        lesson = lesson.replace("| admitted |", "| seen |")
    if mut.get("gate_reject_no_flip"):
        lesson = lesson.replace("| cite S877 in place |", "| — |")
    if mut.get("gate_no_requote"):
        lesson = lesson.replace(
            "re-quote: the staged span was absent (R68 refusal, URL-quote mispairing); ",
            "")
        lesson = lesson.replace(
            "re-quote: the staged span was absent (R71 refusal, URL-quote mispairing); ",
            "")
    if mut.get("no_refused_staged"):
        lesson = lesson.replace("| worldbuilding base entry (staged S882) | S882 |",
                                "| worldbuilding base entry | staged row |")
    if mut.get("refused_file_missing"):
        lesson = lesson.replace("naming-systems", "other-family")
    if mut.get("rejects_counts_missing"):
        lesson = lesson.replace(
            "Counts: 2 adopted / 4 path-present with differing staged bytes / "
            "34 refused of\nthe 40 staged knowledge files.\n", "")
    if mut.get("quarantine_missing"):
        lesson = lesson.replace("## Quarantine", "## Clearing notes")
    if mut.get("reused_unlogged"):
        lesson = lesson.replace(
            "S877 used-by: %s -> %s, %s" % (OLD_ENTRY, OLD_ENTRY, ENTRY_ONE),
            "S877 used-by changed in place.")
    git_write(lane, LESSON, lesson)

    ground = GROUND_TEXT
    if mut.get("ground_zero_missing"):
        ground = ground.replace("tuduku.space: 0\n", "")
    if mut.get("ground_cjk_missing"):
        ground = ground.replace("世界観: 0\n", "")
    if mut.get("ground_rows_wrong"):
        ground = ground.replace("4-row registry", "9-row registry")
    git_write(lane, GROUND_RECEIPT, ground)

    for sid, quote in QUOTES.items():
        if mut.get("evidence_missing") and sid == "S882":
            continue
        window = None
        ua = UA
        sha = None
        scope = None
        visible = None
        window_sha = None
        if mut.get("evidence_quote_absent") and sid == "S881":
            window = "filler " * 700
        if mut.get("evidence_bad_ua") and sid == "S883":
            ua = "curl/8.7.1"
        if mut.get("evidence_bad_sha") and sid == "S884":
            sha = "abc123"
        if mut.get("window_sha_tamper") and sid == "S881":
            window_sha = "0" * 64
        if mut.get("window_short") and sid == "S881":
            window = "short window carrying %s" % quote
        if mut.get("window_scope_whole_4096") and sid == "S881":
            scope = "whole-document"
        if mut.get("window_scope_visible_mismatch") and sid == "S881":
            scope = "whole-document"
            window = "short whole document carrying %s" % quote
            visible = len(window) + 5
        if mut.get("window_scope_unknown") and sid == "S881":
            scope = "full-page"
        git_write(lane, EVIDENCE_DIR + "/" + sid + ".txt",
                  _evidence_text(sid, URLS[sid], quote, window=window, ua=ua,
                                 sha=sha, scope=scope, visible=visible,
                                 window_sha=window_sha))
    git_write(lane, README, _readme_lands(mut))
    if mut.get("receipt_in_append"):
        receipt = RECEIPT_TEXT
        git_write(lane, RECEIPT, receipt)
    if mut.get("config_edited_in_lands"):
        doc2 = claims_fixture(base, narrow=True)
        git_write(lane, CLAIMS, json.dumps(doc2, indent=1, ensure_ascii=False) + "\n")
    lands = git_commit(lane, "lands: entries, rows, lesson, evidence, receipt")
    return lane, fleet, base, freeze, lands


MUTANTS = {
    # ENTRIES
    "drop_entry": {"drop_entry_two": True},
    "stub_entry": {"stub_entry": True},
    "stub_entry_400": {"stub_entry_400": True},
    "placeholder_header": {"placeholder_header": True},
    "entry_at_base": {"entry_at_base": True},
    # ROWS
    "staged_as_is": {"staged_as_is": True},
    "usedby_stub": {"usedby_stub": True},
    "row_gap": {"row_gap": True},
    "extra_row": {"extra_row": True},
    "remove_row": {"remove_row": True},
    "inplace_other": {"inplace_other": True},
    "registry_prose": {"registry_prose": True},
    "anchor_no_quote": {"anchor_no_quote": True},
    "map_url_absent": {"map_url_absent": True},
    "reused_unlogged": {"reused_unlogged": True},
    "reused_usedby_wrong": {"reused_usedby_wrong": True},
    # REPOINTED
    "repoint_url": {"repoint_url": True},
    "campaign_id": {"campaign_id": True},
    "inline_unrelated": {"inline_unrelated": True},
    # GATE
    "gate_quote_words": {"gate_quote_words": True},
    "gate_quote_chars": {"gate_quote_chars": True},
    "gate_reject_no_url": {"gate_reject_no_url": True},
    "gate_no_admit": {"gate_no_admit": True},
    "gate_reject_no_flip": {"gate_reject_no_flip": True},
    "gate_no_requote": {"gate_no_requote": True},
    # EVIDENCE
    "evidence_missing": {"evidence_missing": True},
    "evidence_quote_absent": {"evidence_quote_absent": True},
    "evidence_bad_ua": {"evidence_bad_ua": True},
    "evidence_bad_sha": {"evidence_bad_sha": True},
    "window_sha_tamper": {"window_sha_tamper": True},
    "window_short": {"window_short": True},
    "window_scope_whole_4096": {"window_scope_whole_4096": True},
    "window_scope_visible_mismatch": {"window_scope_visible_mismatch": True},
    "window_scope_unknown": {"window_scope_unknown": True},
    # REJECTS
    "no_refused_staged": {"no_refused_staged": True},
    "refused_file_missing": {"refused_file_missing": True},
    "rejects_counts_missing": {"rejects_counts_missing": True},
    "quarantine_missing": {"quarantine_missing": True},
    # GROUND
    "ground_zero_missing": {"ground_zero_missing": True},
    "ground_cjk_missing": {"ground_cjk_missing": True},
    "ground_rows_wrong": {"ground_rows_wrong": True},
    # CITEDLINES
    "multi_id_line": {"multi_id_line": True},
    # CENSUS
    "census_fail": {"census_fail": True},
    # SCRATCHMIRROR
    "receipt_no_exit": {"receipt_no_exit": True},
    "receipt_in_append": {"receipt_in_append": True},
    "receipt_missing_ids": {"receipt_missing_ids": True},
    # COLLCHECK
    "collisions_adopted": {"collisions_adopted": True},
    "guard_missing": {"guard_missing": True},
    "guard_fourspace_missing": {"guard_fourspace_missing": True},
    # FROZENCFG
    "map_missing": {"map_missing": True},
    "map_sha_mismatch": {"map_sha_mismatch": True},
    "config_edited_in_lands": {"config_edited_in_lands": True},
    # INDEX
    "index_missing_row": {"index_missing_row": True},
    "index_topic_mismatch": {"index_topic_mismatch": True},
    "index_footer_total": {"index_footer_total": True},
    "index_footer_vector": {"index_footer_vector": True},
    "index_older_footer_edited": {"index_older_footer_edited": True},
}

EXPECTED_FAIL = {
    "drop_entry": "ENTRIES",
    "stub_entry": "ENTRIES",
    "stub_entry_400": "ENTRIES",
    "placeholder_header": "ENTRIES",
    "entry_at_base": "ENTRIES",
    "staged_as_is": "ROWS",
    "usedby_stub": "ROWS",
    "row_gap": "ROWS",
    "extra_row": "ROWS",
    "remove_row": "ROWS",
    "inplace_other": "ROWS",
    "registry_prose": "ROWS",
    "anchor_no_quote": "ROWS",
    "map_url_absent": "ROWS",
    "reused_unlogged": "ROWS",
    "reused_usedby_wrong": "ROWS",
    "repoint_url": "REPOINTED",
    "campaign_id": "REPOINTED",
    "inline_unrelated": "REPOINTED",
    "gate_quote_words": "GATE",
    "gate_quote_chars": "GATE",
    "gate_reject_no_url": "GATE",
    "gate_no_admit": "GATE",
    "gate_reject_no_flip": "GATE",
    "gate_no_requote": "GATE",
    "evidence_missing": "EVIDENCE",
    "evidence_quote_absent": "EVIDENCE",
    "evidence_bad_ua": "EVIDENCE",
    "evidence_bad_sha": "EVIDENCE",
    "window_sha_tamper": "EVIDENCE",
    "window_short": "EVIDENCE",
    "window_scope_whole_4096": "EVIDENCE",
    "window_scope_visible_mismatch": "EVIDENCE",
    "window_scope_unknown": "EVIDENCE",
    "no_refused_staged": "REJECTS",
    "refused_file_missing": "REJECTS",
    "rejects_counts_missing": "REJECTS",
    "quarantine_missing": "REJECTS",
    "ground_zero_missing": "GROUND",
    "ground_cjk_missing": "GROUND",
    "ground_rows_wrong": "GROUND",
    "multi_id_line": "CITEDLINES",
    "census_fail": "CENSUS",
    "receipt_no_exit": "SCRATCHMIRROR",
    "receipt_in_append": "SCRATCHMIRROR",
    "receipt_missing_ids": "SCRATCHMIRROR",
    "collisions_adopted": "COLLCHECK",
    "guard_missing": "COLLCHECK",
    "guard_fourspace_missing": "COLLCHECK",
    "map_missing": "FROZENCFG",
    "map_sha_mismatch": "FROZENCFG",
    "config_edited_in_lands": "FROZENCFG",
    "index_missing_row": "INDEX",
    "index_topic_mismatch": "INDEX",
    "index_footer_total": "INDEX",
    "index_footer_vector": "INDEX",
    "index_older_footer_edited": "INDEX",
}


def _run_counter(lane, fleet, lands, freeze=None, extra=None, omit_lands=False):
    cmd = [sys.executable, "-B", os.path.abspath(__file__),
           "--root", lane, "--fleet-root", fleet]
    if not omit_lands:
        cmd += ["--lands", lands]
    if freeze:
        cmd += ["--freeze", freeze]
    if extra:
        cmd += list(extra)
    return subprocess.run(cmd, capture_output=True, text=True)


def run_selftest():
    failures, fixtures, scenarios = [], [], []

    def scenario(name):
        scenarios.append(name)

    def drop(lane, fleet):
        fixtures.append((lane, fleet))

    # 1. clean fixture: PASS 13/13 with a stamped, frozen-config receipt.
    lane, fleet, base, freeze, lands = build_fixture("r74st-clean")
    drop(lane, fleet)
    scenario("clean")
    r = _run_counter(lane, fleet, lands, freeze)
    if "ACCEPT-C-74: PASS legs=13/13" not in r.stdout:
        failures.append("clean fixture: expected PASS 13/13, got exit=%d\n%s\n%s"
                        % (r.returncode, r.stdout, r.stderr))
    if "# evaluated revision: %s" % lands not in r.stdout:
        failures.append("clean fixture: receipt header does not stamp lands\n%s"
                        % r.stdout)
    if "# freeze revision: %s" % freeze not in r.stdout:
        failures.append("clean fixture: receipt header does not name the freeze\n%s"
                        % r.stdout)
    if "# config source: git show %s:%s" % (freeze, CLAIMS) not in r.stdout:
        failures.append("clean fixture: receipt does not disclose the frozen "
                        "config source\n%s" % r.stdout)
    if "# frozen legs: 13 (" not in r.stdout:
        failures.append("clean fixture: receipt does not name the frozen leg "
                        "list\n%s" % r.stdout)

    # 2. lands == the frozen base is refused and still prints FAIL.
    scenario("lands-eq-base")
    r = _run_counter(lane, fleet, base, freeze)
    if r.returncode != 2 or "ACCEPT-C-74: FAIL" not in r.stdout:
        failures.append("base-lands control: expected refusal exit 2 with a FAIL "
                        "line, got %d\n%s\n%s"
                        % (r.returncode, r.stdout, r.stderr))

    # 3. required --lands.
    scenario("missing-lands")
    r = _run_counter(lane, fleet, lands, freeze, omit_lands=True)
    if r.returncode != 2 or "--lands" not in r.stderr:
        failures.append("missing-lands: expected exit 2 naming --lands, got %d\n%s"
                        % (r.returncode, r.stderr))

    # 4. required --freeze.
    scenario("missing-freeze")
    r = _run_counter(lane, fleet, lands, None)
    if r.returncode != 2 or "--freeze" not in r.stderr:
        failures.append("missing-freeze: expected exit 2 naming --freeze, got %d\n%s"
                        % (r.returncode, r.stderr))

    # 5. lands == the freeze commit is NOT a refusal: the data legs fail,
    #    FROZENCFG passes (the do-nothing control's first shape).
    scenario("freeze-eq-lands")
    r = _run_counter(lane, fleet, freeze, freeze)
    out = r.stdout
    if r.returncode != 1 or "ACCEPT-C-74: FAIL" not in out:
        failures.append("lands==freeze: expected graded FAIL exit 1, got %d\n%s"
                        % (r.returncode, out))
    else:
        for leg_name in ("ENTRIES", "ROWS", "GATE", "EVIDENCE", "REJECTS",
                         "INDEX"):
            if "LEG FAIL %s" % leg_name not in out:
                failures.append("lands==freeze: expected %s red\n%s"
                                % (leg_name, out))
        if "LEG PASS FROZENCFG" not in out:
            failures.append("lands==freeze: FROZENCFG must stay green\n%s" % out)

    # 6. a freeze that is a descendant of lands fails FROZENCFG.
    scenario("freeze-descendant")
    r = _run_counter(lane, fleet, freeze, lands)
    if "LEG FAIL FROZENCFG" not in r.stdout or "ACCEPT-C-74: FAIL" not in r.stdout:
        failures.append("freeze=descendant: expected FAIL FROZENCFG\n%s" % r.stdout)

    # 6b. LEGCOUNT: a frozen leg list of 12 is refused.
    lane6b, fleet6b, base6b, freeze6b, lands6b = build_fixture(
        "r74st-legcount", {"legcount_mismatch": True})
    drop(lane6b, fleet6b)
    scenario("legcount-mismatch")
    r = _run_counter(lane6b, fleet6b, lands6b, freeze6b)
    if r.returncode != 2 or "LEGCOUNT" not in r.stderr:
        failures.append("legcount mismatch: expected refusal exit 2 naming "
                        "LEGCOUNT, got %d\n%s" % (r.returncode, r.stderr))

    # 7. a freeze commit without claims.json is refused.
    lane2, fleet2, base2, _f2, _l2 = build_fixture("r74st-noclaims")
    drop(lane2, fleet2)
    scenario("freeze-no-claims")
    r = _run_counter(lane2, fleet2, _l2, base2)
    if r.returncode != 2 or "REFUSED" not in r.stderr:
        failures.append("freeze without claims.json: expected refusal exit 2, "
                        "got %d\n%s" % (r.returncode, r.stderr))

    # 8. the frozen row_set drives ROWS: a narrowed set must FAIL ROWS.
    lane3, fleet3, base3, freeze3, lands3 = build_fixture(
        "r74st-narrow", {"claims_narrow": True})
    drop(lane3, fleet3)
    scenario("config-narrow-drives-rows")
    r = _run_counter(lane3, fleet3, lands3, freeze3)
    if "LEG FAIL ROWS" not in r.stdout or "ACCEPT-C-74: FAIL" not in r.stdout:
        failures.append("narrow frozen row_set: expected FAIL ROWS\n%s" % r.stdout)
    elif "# adopted rows: S881 S882 S883 " not in r.stdout:
        failures.append("narrow frozen row_set: receipt does not follow the "
                        "frozen config\n%s" % r.stdout)

    # 9. a frozen row_set naming a row the lands tree never appends FAILS ROWS
    #    (the config is not decorative in the other direction either).
    lane4, fleet4, base4, freeze4, lands4 = build_fixture(
        "r74st-extra", {"claims_extra_rows": True})
    drop(lane4, fleet4)
    scenario("config-extra-row")
    r = _run_counter(lane4, fleet4, lands4, freeze4)
    if "LEG FAIL ROWS" not in r.stdout:
        failures.append("extra frozen row: expected FAIL ROWS\n%s" % r.stdout)

    # 10. the round-73-shaped four-space control (a description, not a literal
    #     planted row) still satisfies COLLCHECK: the leg is not over-fitted.
    lane5, fleet5, base5, freeze5, lands5 = build_fixture(
        "r74st-guardshape", {"guard_r73shape": True})
    drop(lane5, fleet5)
    scenario("guard-r73-shape")
    r = _run_counter(lane5, fleet5, lands5, freeze5)
    if "ACCEPT-C-74: PASS legs=13/13" not in r.stdout:
        failures.append("r73-shaped four-space control: expected PASS 13/13, "
                        "got exit=%d\n%s" % (r.returncode, r.stdout))

    # 11. the do-nothing control proper: a lands commit after the freeze that
    #     lands no claim-C artefact must FAIL the data legs.
    lane6, fleet6, base6, freeze6, lands6 = build_fixture(
        "r74st-nodata", {"no_data": True})
    drop(lane6, fleet6)
    scenario("do-nothing-no-data")
    r = _run_counter(lane6, fleet6, lands6, freeze6)
    if "ACCEPT-C-74: FAIL" not in r.stdout:
        failures.append("no-data lands: expected FAIL, got exit=%d\n%s"
                        % (r.returncode, r.stdout))
    elif "LEG FAIL ENTRIES" not in r.stdout or "LEG FAIL ROWS" not in r.stdout:
        failures.append("no-data lands: expected ENTRIES and ROWS to fail\n%s"
                        % r.stdout)
    elif "LEG PASS FROZENCFG" not in r.stdout:
        failures.append("no-data lands: FROZENCFG should still pass (the config is "
                        "frozen and unedited)\n%s" % r.stdout)

    for name, mut in MUTANTS.items():
        scenario("mutant-" + name)
        lane, fleet, base, freeze, lands = build_fixture("r74st-" + name, mut)
        drop(lane, fleet)
        r = _run_counter(lane, fleet, lands, freeze)
        out = r.stdout
        wanted = EXPECTED_FAIL[name]
        if "ACCEPT-C-74: FAIL" not in out:
            failures.append("%s: expected final FAIL, got exit=%d\n%s\n%s"
                            % (name, r.returncode, out, r.stderr))
        elif "LEG FAIL %s" % wanted not in out:
            failures.append("%s: expected leg FAIL %s\n%s" % (name, wanted, out))

    total = len(scenarios)
    passed = total - len(failures)
    print("SELFTEST: %d/%d scenarios" % (passed, total))
    for f in failures:
        print("---", f)
    for lane, fleet in fixtures:
        shutil.rmtree(lane, ignore_errors=True)
        shutil.rmtree(fleet, ignore_errors=True)
    return 0 if passed == total else 1


if __name__ == "__main__":
    sys.exit(main())
