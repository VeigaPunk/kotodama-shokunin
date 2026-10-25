#!/usr/bin/env python3
r"""Round-73 coverage acceptance counter — claim C (conlang-scholarship assimilation).

Grades the frozen claim-C predicate (reports/round-73/claims.json) at an
explicit lands revision.  The worktree is never graded (QUALITY 19): the
counter materializes `git archive <lands>` into a temporary tree and every
leg reads bytes from that tree (the base revision is materialized the same
way).  Read-only git against the lane repository supplies only commit
metadata (ancestry, per-path history, diffs) and never a graded byte.

Receipt header (printed before the leg table, QUALITY 17/19):

  # counter sha256 (self): ...      the counter's own bytes
  # stamped revision: ...           the revision the receipt claims
  # evaluated revision: ...         the revision whose bytes were read
  # measured revision (lane main):  the lane worktree HEAD (disclosure only)
  # tree: ...                       git rev-parse <lands>^{tree}
  # base revision: ...              the frozen claim base
  # access date: 2026-10-25         the round's access date

Legs (10):

  ENTRIES       both admitted entries exist at <lands> with the full
                provenance header (source / verified-at / recheck / ground /
                topic / gap-filled / sources / couples / scope);
  ROWS          the registry diff base..<lands> adds exactly the adopted row
                set, contiguous from S876 upward, one per source the entries
                cite, all status mined, each used-by naming exactly the
                admitted entries that cite it, union covering both entries,
                no other row added or removed, and no added row is the staged
                text appended as-is (escaped pipe, un-normalized recheck cell,
                used-by naming non-admitted paths);
  REPOINTED     every `source:` line and every inline S-id in the admitted
                entries names a lane id >= S876 whose registry row exists and
                whose URL matches the cited document; campaign ids that name
                unrelated lane documents (S728 / S769 / S806) appear nowhere;
  GATE          corpus/lessons/round-73.md ## Gate carries, per adopted row,
                a table row with the row URL, access date 2026-10-25, a
                <=25-word quoted span and a non-empty locator cell; and >=1
                admit and >=1 reject row, every reject row recording the URL
                it rejected (QUALITY 21) with reason and flip columns;
  REJECTS       the lesson refuses, with reason and flip, every staged entry
                of the conlang theme that cites a quarantine-REFUSED or
                unreachable row (staged S869 / S894 / S910 by default) and
                names the remaining naming-systems / calendar / era /
                verification staged families as not adopted this round;
  GROUND        the gap-sweep receipt names the base registry's row count and
                a 0 for each tentative URL fragment, and the base tree is
                re-derived directly (0 owners, 0 conlang-scholarship files);
  CITEDLINES    tools/check-cited-lines.py, run from the materialized tree,
                reads both entries and prints 0 findings;
  CENSUS        scripts/sources-census.sh validate --root <fleet-root>
                kotodama exits 0 against the registry bytes of <lands>, the
                fleet root being a temporary root whose kotodama lane is the
                materialized tree;
  SCRATCHMIRROR .ufo/waves/round-73/assimilation/validate-receipt.txt shows
                census validate --file exit 0 on the mirrored corpus carrying
                the adopted rows, committed strictly before the registry
                append commit;
  COLLCHECK     the collision receipt (0-3-space-indent guard, proved on a
                planted indented collision first) carries zero id tokens for
                the adopted ids; the regenerated renumber map records old->new
                for every adopted id and supersedes the round-71 map, whose
                bytes are untouched base..<lands>.

Leg parameters come from a `row_set` / `entries` (and optionally `rejects` /
`ground`) object in reports/round-73/claims.json when present — read from the
lands tree first, then the lane worktree — and otherwise default to the five
tentative rows S876..S880 and the two entry paths below.  The receipt header
names which source supplied the configuration.

Exit: 0 all legs pass; 1 any leg fails; 2 input error.

Read-only outside the temporary materializations; stdlib only.
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
BASE = "8841ad3b896a0227674fa0725b818c999118046f"
ACCESS_DATE = "2026-10-25"
REGISTRY = "corpus/SOURCES.md"
LESSON = "corpus/lessons/round-73.md"
CLAIMS = "reports/round-73/claims.json"
ASSIM = ".ufo/waves/round-73/assimilation"
RECEIPT = ASSIM + "/validate-receipt.txt"
GROUND_RECEIPT = "reports/round-73/telemetry/gap-sweep.txt"
RENUMBER_MAP = ASSIM + "/id-renumber-map.json"
RENUMBER_MAP_DRAFT = ASSIM + "/id-renumber-map-draft.json"
STALE_MAP = ".ufo/waves/round-71/assimilation/id-renumber-map.json"
GUARD_DIR = ASSIM + "/guard-proof"
LEDGER_ROWS_BASE = 799
EVIDENCE_DIR = "reports/round-73/evidence"

DEFAULT_ENTRIES = (
    "corpus/knowledge/linguistics/conlang-scholarship.md",
    "corpus/knowledge/linguistics/conlang-scholarship.amend-2026-10-23.md",
)
DEFAULT_ROWS = ("S876", "S877", "S878", "S879", "S880")
DEFAULT_FORBIDDEN = ("S728", "S769", "S806")
DEFAULT_REFUSED_STAGED = ("S869", "S894", "S910")
DEFAULT_REFUSED_FILES = (
    "conlang-methodology.md",
    "conlang-scholarship.amend-2026-10-23.md",
    "conlang-scholarship.amend-2026-10-23b.md",
)
DEFAULT_FAMILIES = ("naming-systems", "calendar", "era", "verification")
DEFAULT_GROUND_FRAGMENTS = (
    "ojs.unito.it",
    "philol.msu.ru",
    "journals.rudn.ru",
    "cyberleninka.ru/article/n/klassifikatsii",
    "sanders.phonologist.org",
)
HEADER_FIELDS = ("source", "verified-at", "recheck", "ground", "topic",
                 "gap-filled", "sources", "couples", "scope")

ROW_RE = re.compile(r"^\s{0,3}\|\s*(S\d{3,})\s*\|")
INDENTED_ROW_RE = re.compile(r"^ {1,3}\|\s*(S\d{3,})\s*\|", re.M)
TOKEN_RE = re.compile(r"\bS\d{3,}\b")
URL_RE = re.compile(r"https?://[^\s|<>]+")
QUOTE_RE = re.compile(r'"(?:\\.|[^"\\\n])*"|“[^“”\n]*”|«[^«»\n]*»|「[^「」\n]*」')
H2_RE = re.compile(r"^##\s")
GATE_RE = re.compile(r"^##\s+Gate\b")
RECHECK_RE = re.compile(r"^(?:\d+d|\d{4}-\d{2}-\d{2}|[a-z][a-z-]*)$")
NOT_ADOPTED_RE = re.compile(r"(?i)\bnot\s+adopted\b|\bno\s+adoption\b|\bnot\s+admitted\b")


class Missing(Exception):
    """A materialized path cannot be read at the requested revision."""


# ---------------------------------------------------------------- helpers ---

def norm_label(s):
    return re.sub(r"[^A-Za-z0-9]", "", s).lower()


def norm_url(u):
    u = u.rstrip(".,;:!?)]}。，；：！？）】》»")
    p = urlparse(u)
    path = p.path.rstrip("/") or "/"
    return (p.netloc.lower(), path)


def git(root, *args):
    return subprocess.run(["git", "-C", root, *args],
                          capture_output=True, text=True)


def read_tree(tree, path):
    full = os.path.join(tree, path)
    try:
        with open(full, encoding="utf-8") as fh:
            return fh.read()
    except OSError:
        raise Missing(path)


def counter_sha256():
    with open(os.path.abspath(__file__), "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


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


def tree_files(tree, prefix):
    base = os.path.join(tree, prefix)
    out = []
    for dirpath, _dirnames, filenames in os.walk(base):
        for fn in filenames:
            full = os.path.join(dirpath, fn)
            out.append(os.path.relpath(full, tree))
    return out


def parse_rows(text):
    rows = {}
    for line in text.splitlines():
        m = ROW_RE.match(line)
        if m:
            rows[m.group(1)] = line
    return rows


def row_cells(row):
    return [c.strip() for c in row.split("|")]


def row_usedby(cells):
    if len(cells) < 12:
        return set()
    return set(p.strip() for p in cells[11].split(",")
               if p.strip() and p.strip() not in ("—", "-"))


def leg(name, passed, detail=""):
    print("LEG %s %s" % ("PASS" if passed else "FAIL", name))
    if detail:
        print("     %s" % detail)
    return bool(passed)


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
    lines = text.splitlines()
    out, started = [], False
    for line in lines:
        if GATE_RE.match(line):
            started = True
            continue
        if started and H2_RE.match(line):
            break
        if started:
            out.append(line)
    return out


def quoted_spans(line):
    return [m.group(0)[1:-1] for m in QUOTE_RE.finditer(line)]


def table_rows(lines):
    rows = []
    for line in lines:
        if line.lstrip().startswith("|"):
            rows.append(line.strip())
        elif line.startswith(" ") and rows:
            rows[-1] += " " + line.strip()
    return rows


def verdict_of(row):
    cells = [c.strip() for c in row.split("|")]
    nonempty = [c for c in cells if c]
    return nonempty[-1].lower() if nonempty else ""


def is_admit_row(row):
    return "admitted" in verdict_of(row)


def is_reject_row(row):
    v = verdict_of(row)
    return "rejected" in v or "refused" in v


def dedupe(seq):
    seen, out = set(), []
    for x in seq:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out


# ------------------------------------------------------------ config load ---

DEFAULTS = {
    "entries": DEFAULT_ENTRIES,
    "rows": DEFAULT_ROWS,
    "row_staged": {},
    "forbidden_ids": DEFAULT_FORBIDDEN,
    "refused_staged": DEFAULT_REFUSED_STAGED,
    "refused_files": DEFAULT_REFUSED_FILES,
    "families": DEFAULT_FAMILIES,
    "ground_fragments": DEFAULT_GROUND_FRAGMENTS,
    "config_source": "defaults (no row_set/entries object in claims.json)",
}


def _ids_from(value):
    if isinstance(value, str):
        return [m.upper() for m in TOKEN_RE.findall(value)]
    out = []
    if isinstance(value, list):
        for item in value:
            if isinstance(item, str):
                out.extend(m.upper() for m in TOKEN_RE.findall(item))
            elif isinstance(item, dict):
                for key in ("id", "lane", "new"):
                    v = item.get(key)
                    if isinstance(v, str) and TOKEN_RE.fullmatch(v.strip()):
                        out.append(v.strip().upper())
                        break
    return out


def _rows_from_spec(spec):
    """(ids tuple, {lane id: staged id}) from a row_set spec."""
    ids, staged = [], {}
    def take(item):
        if isinstance(item, str):
            ids.extend(m.upper() for m in TOKEN_RE.findall(item))
            return
        if not isinstance(item, dict):
            return
        rid = None
        for key in ("id", "lane", "new"):
            v = item.get(key)
            if isinstance(v, str) and TOKEN_RE.fullmatch(v.strip()):
                rid = v.strip().upper()
                break
        if rid is None:
            return
        ids.append(rid)
        for key in ("staged", "staged_id", "old"):
            v = item.get(key)
            if isinstance(v, str) and TOKEN_RE.fullmatch(v.strip()):
                staged[rid] = v.strip().upper()
                break
    if isinstance(spec, list):
        for item in spec:
            take(item)
    elif isinstance(spec, dict):
        listed = spec.get("ids")
        if isinstance(listed, list):
            for item in listed:
                take(item)
        for key, val in spec.items():
            if TOKEN_RE.fullmatch(str(key).strip()):
                rid = str(key).strip().upper()
                ids.append(rid)
                if isinstance(val, str) and TOKEN_RE.fullmatch(val.strip()):
                    staged[rid] = val.strip().upper()
                elif isinstance(val, dict):
                    for k2 in ("staged", "staged_id", "old"):
                        v2 = val.get(k2)
                        if isinstance(v2, str) and TOKEN_RE.fullmatch(v2.strip()):
                            staged[rid] = v2.strip().upper()
                            break
    else:
        ids.extend(_ids_from(spec))
    uniq = tuple(sorted(set(ids), key=lambda s: int(s[1:])))
    return uniq, staged


def _entries_from_spec(spec):
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
    return tuple(dict.fromkeys(out))


def load_config(mat, root):
    cfg = dict(DEFAULTS)
    cfg["row_staged"] = dict(DEFAULTS["row_staged"])
    text, src = None, DEFAULTS["config_source"]
    for cand, label in ((os.path.join(mat, CLAIMS), "lands tree"),
                        (os.path.join(root, CLAIMS), "lane worktree")):
        try:
            with open(cand, encoding="utf-8") as fh:
                text = fh.read()
            src = label
            break
        except OSError:
            continue
    if text is None:
        return cfg
    try:
        doc = json.loads(text)
    except ValueError:
        cfg["config_source"] = "%s (claims.json unparsable; defaults)" % src
        return cfg
    if not isinstance(doc, dict):
        return cfg
    claim = None
    for c in doc.get("claims") or []:
        if isinstance(c, dict) and str(c.get("id", "")).upper() == "C":
            claim = c
            break
    containers = [x for x in (claim, doc) if isinstance(x, dict)]

    def first_key(names):
        for container in containers:
            for name in names:
                if name in container:
                    return container[name]
        return None

    applied = []
    spec = first_key(("row_set",))
    if spec is not None:
        ids, staged = _rows_from_spec(spec)
        if ids:
            cfg["rows"] = ids
            cfg["row_staged"].update(staged)
            applied.append("row_set")
    spec = first_key(("entries",))
    if spec is not None:
        paths = _entries_from_spec(spec)
        if paths:
            cfg["entries"] = paths
            applied.append("entries")
    spec = first_key(("rejects",))
    if isinstance(spec, dict):
        ids = []
        for key in ("refused_staged", "unreachable_staged", "refused"):
            ids.extend(_ids_from(spec.get(key)))
        if ids:
            cfg["refused_staged"] = tuple(sorted(set(ids), key=lambda s: int(s[1:])))
            applied.append("rejects.refused_staged")
        files = spec.get("refused_files")
        if isinstance(files, str):
            cfg["refused_files"] = (files,)
            applied.append("rejects.refused_files")
        elif isinstance(files, list) and files:
            cfg["refused_files"] = tuple(str(f) for f in files)
            applied.append("rejects.refused_files")
        fams = spec.get("families")
        if isinstance(fams, list) and fams:
            cfg["families"] = tuple(str(f) for f in fams)
            applied.append("rejects.families")
        forb = _ids_from(spec.get("forbidden_ids"))
        if forb:
            cfg["forbidden_ids"] = tuple(sorted(set(forb), key=lambda s: int(s[1:])))
            applied.append("rejects.forbidden_ids")
    spec = first_key(("ground",))
    if isinstance(spec, dict):
        frags = spec.get("fragments")
        if isinstance(frags, list) and frags:
            cfg["ground_fragments"] = tuple(str(f) for f in frags)
            applied.append("ground.fragments")
    forb = _ids_from(first_key(("forbidden_ids",)))
    if forb:
        cfg["forbidden_ids"] = tuple(sorted(set(forb), key=lambda s: int(s[1:])))
        applied.append("forbidden_ids")
    cfg["config_source"] = "%s: %s" % (src, ", ".join(applied) if applied else
                                       "no row_set/entries object (defaults)")
    return cfg


# ------------------------------------------------------------------ legs ---

def leg_entries(mat, mat_base, root, lands, base, cfg):
    """Leg ENTRIES: both files exist at lands with the full header."""
    bad = []
    for e in cfg["entries"]:
        try:
            text = read_tree(mat, e)
        except Missing:
            bad.append("%s missing" % e)
            continue
        if not text.strip():
            bad.append("%s empty" % e)
        missing = [f for f in HEADER_FIELDS
                   if norm_label(f) not in header_field_names(text)]
        if missing:
            bad.append("%s header missing: %s" % (e, ",".join(missing)))
        for line in header_block(text):
            m = re.match(r"^[-*\s]*([A-Za-z][A-Za-z0-9 -]*):\s*(.*)$", line)
            if m and norm_label(m.group(1)) in [norm_label(f) for f in HEADER_FIELDS]:
                val = m.group(2).strip().strip("—-").strip().lower()
                if val in ("", "todo", "tbd", "n/a", "na", "none", "placeholder"):
                    bad.append("%s header field %r carries a placeholder value"
                               % (e, m.group(1)))
        body = text[sum(len(x) + 1 for x in header_block(text)):]
        words = len(body.split())
        floor = _min_entry_words(mat_base)
        if words < floor:
            bad.append("%s body has %d words (floor %d = the smallest knowledge entry at base)"
                       % (e, words, floor))
    return leg("ENTRIES", not bad, "; ".join(bad))


def _min_entry_words(mat_base):
    best = None
    for rel in tree_files(mat_base, "corpus/knowledge"):
        if not rel.endswith(".md"):
            continue
        try:
            t = read_tree(mat_base, rel)
        except Missing:
            continue
        n = len(t.split())
        best = n if best is None else min(best, n)
    return best or 0


def _evidence(mat, rid):
    """Parse reports/round-73/evidence/<id>.txt at lands into a dict."""
    try:
        text = read_tree(mat, EVIDENCE_DIR + "/" + rid + ".txt")
    except Missing:
        return None
    out = {}
    for line in text.splitlines():
        m = re.match(r"^([a-z0-9-]+):\s*(.*)$", line)
        if m and m.group(1) not in out:
            out[m.group(1)] = m.group(2)
    out["_text"] = text
    return out


def _wsnorm(s):
    return re.sub(r"\s+", " ", s).strip()


def leg_rows(mat, mat_base, root, lands, base, cfg):
    """Leg ROWS: exactly the adopted rows added, contiguous from S876,
    mined, used-by exactly the citing entries, no staged row appended as-is."""
    try:
        base_rows = parse_rows(read_tree(mat_base, REGISTRY))
        lands_rows = parse_rows(read_tree(mat, REGISTRY))
    except Missing as e:
        return leg("ROWS", False, "registry unreadable: %s" % e)
    added = set(lands_rows) - set(base_rows)
    removed = set(base_rows) - set(lands_rows)
    want = list(cfg["rows"])
    bad = []
    if added != set(want):
        bad.append("added=%s (want %s)" % (sorted(added), want))
    if removed:
        bad.append("removed=%s (want none)" % sorted(removed))
    nums = sorted(int(x[1:]) for x in added)
    if any(n < 876 for n in nums):
        bad.append("added ids below S876: %s" % nums)
    if nums and nums != list(range(876, 876 + len(nums))):
        bad.append("added ids %s do not continue contiguously from S876" % nums)

    cited = {}
    for e in cfg["entries"]:
        try:
            text = read_tree(mat, e)
        except Missing:
            bad.append("%s missing (cannot derive used-by)" % e)
            continue
        for sline in source_lines(text):
            for sid in TOKEN_RE.findall(sline):
                cited.setdefault(sid, set()).add(e)
    stray = set(cited) - set(want)
    if stray:
        bad.append("entries cite ids outside the adopted row set: %s" % sorted(stray))

    union = set()
    for sid in want:
        row = lands_rows.get(sid)
        if row is None:
            bad.append("%s row missing" % sid)
            continue
        cells = row_cells(row)
        if len(cells) < 12:
            bad.append("%s row has %d cells (want 12)" % (sid, len(cells)))
            continue
        status, recheck = cells[8], cells[10]
        if cells[9] != ACCESS_DATE:
            bad.append("%s opened=%r (want %s: a staged opened date is an as-is tell)"
                       % (sid, cells[9], ACCESS_DATE))
        ev = _evidence(mat, sid)
        if ev is not None and ev.get("quote"):
            if _wsnorm(ev["quote"]) not in _wsnorm(cells[6]):
                bad.append("%s anchor cell does not contain its evidence quote" % sid)
        mapurl = _map_url(mat, sid)
        if mapurl is None:
            bad.append("%s has no committed renumber-map entry" % sid)
        elif norm_url(mapurl) not in neutral_url_keys(urls_in(cells[2])):
            bad.append("%s source cell lacks the map URL %s" % (sid, mapurl))
        if status != "mined":
            bad.append("%s status=%r (want mined)" % (sid, status))
        if "\\|" in row:
            bad.append("%s row carries an escaped pipe (staged text appended as-is)"
                       % sid)
        if not RECHECK_RE.match(recheck):
            bad.append("%s recheck=%r not a normalized cadence" % (sid, recheck))
        used = row_usedby(cells)
        want_used = cited.get(sid, set())
        if used != want_used:
            bad.append("%s used-by=%s (want exactly %s)"
                       % (sid, sorted(used), sorted(want_used)))
        union |= used
    if union != set(cfg["entries"]):
        bad.append("used-by union %s (want both admitted entries)" % sorted(union))
    for e in cfg["entries"]:
        if not any(e in v for v in cited.values()):
            bad.append("%s cites no adopted row" % e)
    return leg("ROWS", not bad, "; ".join(dedupe(bad)))


def _map_url(mat, sid):
    try:
        data = json.loads(read_tree(mat, RENUMBER_MAP))
    except (Missing, ValueError):
        return None
    for v in data.values():
        if isinstance(v, list):
            for d in v:
                if isinstance(d, dict) and d.get("new_target") == sid:
                    return d.get("url")
    return None


def leg_repointed(mat, mat_base, root, lands, base, cfg):
    """Leg REPOINTED: every source line and inline id names an adopted row
    whose URL matches; campaign ids appear nowhere."""
    try:
        lands_rows = parse_rows(read_tree(mat, REGISTRY))
    except Missing as e:
        return leg("REPOINTED", False, "registry unreadable: %s" % e)
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
            if int(sid[1:]) < 876:
                bad.append("%s cites %s < S876" % (e, sid))
            if sid not in lands_rows:
                bad.append("%s cites %s with no registry row" % (e, sid))
                continue
            cited = urls_in(sline)
            if not cited:
                bad.append("%s source line has no URL" % e)
                continue
            row_keys = neutral_url_keys(urls_in(row_cells(lands_rows[sid])[2]))
            for u in cited:
                if norm_url(u) not in row_keys:
                    bad.append("%s cites URL not registered on %s: %s"
                               % (e, sid, u))
        for lineno, line in enumerate(text.splitlines(), 1):
            for sid in TOKEN_RE.findall(line):
                if int(sid[1:]) < 876:
                    bad.append("%s:%d inline id %s < S876" % (e, lineno, sid))
                elif sid not in lands_rows:
                    bad.append("%s:%d inline id %s has no registry row"
                               % (e, lineno, sid))
        for fid in cfg["forbidden_ids"]:
            if re.search(r"\b%s\b" % re.escape(fid), text):
                bad.append("%s cites campaign id %s (names an unrelated lane document)"
                           % (e, fid))
    return leg("REPOINTED", not bad, "; ".join(dedupe(bad)))


def leg_gate(mat, mat_base, root, lands, base, cfg):
    """Leg GATE: lesson Gate per-row URL + 2026-10-25 + <=25-word quote +
    locator, >=1 admit and >=1 reject, every reject recording its URL."""
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
    for sid in cfg["rows"]:
        row_line = None
        for r in admits:
            if re.search(r"\b%s\b" % sid, r):
                row_line = r
                break
        if row_line is None:
            bad.append("%s has no admit row in Gate" % sid)
            continue
        if ACCESS_DATE not in row_line:
            bad.append("%s row access date missing %s" % (sid, ACCESS_DATE))
        spans = quoted_spans(row_line)
        if not spans:
            bad.append("%s row has no quoted locator" % sid)
        elif any(len(s.split()) > 25 for s in spans):
            bad.append("%s row quote exceeds 25 words" % sid)
        cells = [c for c in row_cells(row_line) if c]
        if len(cells) < 5:
            bad.append("%s row lacks a locator cell" % sid)
        row_urls = []
        if sid in lands_rows:
            row_urls = urls_in(row_cells(lands_rows[sid])[2])
            if not any(u in row_line for u in row_urls):
                bad.append("%s row URL not recorded in Gate" % sid)
        elif not urls_in(row_line):
            bad.append("%s row has no URL and no registry row" % sid)
    if not admits:
        bad.append("no admit row (want >=1)")
    if not rejects:
        bad.append("no reject row (want >=1)")
    for r in rejects:
        if not urls_in(r):
            bad.append("reject row records no probed URL: %s" % r[:90])
        if not TOKEN_RE.search(r) and ".md" not in r:
            bad.append("reject row names no staged entry or row: %s" % r[:90])
    low = "\n".join(section).lower()
    if "reason" not in low or "flip" not in low:
        bad.append("reject reason+flip columns not recorded in Gate")
    return leg("GATE", not bad, "; ".join(dedupe(bad)))


def leg_evidence(mat, mat_base, root, lands, base, cfg):
    """Leg EVIDENCE: a committed capture per adopted row — fetch line (UA, status 200,
    sha256), verbatim quote <=25 words found in its context window, equal to the
    quote the Gate row and the registry anchor carry."""
    try:
        gate = table_rows(gate_section(read_tree(mat, LESSON)))
    except Missing as e:
        return leg("EVIDENCE", False, "%s" % e)
    bad = []
    for sid in cfg["rows"]:
        ev = _evidence(mat, sid)
        if ev is None:
            bad.append("%s evidence file missing" % sid)
            continue
        if ev.get("access-date") != ACCESS_DATE:
            bad.append("%s access-date %r" % (sid, ev.get("access-date")))
        if ev.get("http-status") != "200":
            bad.append("%s http-status %r (want 200)" % (sid, ev.get("http-status")))
        if not re.match(r"^[0-9a-f]{64}$", ev.get("sha256", "")):
            bad.append("%s sha256 line not a 64-hex digest" % sid)
        if not ev.get("user-agent", "").startswith("Mozilla/5.0"):
            bad.append("%s user-agent not recorded as a browser-shaped UA" % sid)
        if ev.get("quote-found-verbatim") != "yes":
            bad.append("%s quote-found-verbatim=%r" % (sid, ev.get("quote-found-verbatim")))
        q = ev.get("quote", "")
        if not q or len(q.split()) > 25:
            bad.append("%s quote empty or >25 words" % sid)
        window = ev["_text"].split("--- context window", 1)[-1]
        if _wsnorm(q) not in _wsnorm(window):
            bad.append("%s quote absent from its own context window" % sid)
        grow = [r for r in gate if re.search(r"\b%s\b" % sid, r) and is_admit_row(r)]
        if grow and _wsnorm(q) not in _wsnorm(grow[0]):
            bad.append("%s Gate row does not carry the evidence quote" % sid)
    return leg("EVIDENCE", not bad, "; ".join(dedupe(bad)))


def leg_rejects(mat, mat_base, root, lands, base, cfg):
    """Leg REJECTS: the lesson refuses the refused staged entries and names
    the remaining staged families as not adopted this round."""
    try:
        text = read_tree(mat, LESSON)
    except Missing as e:
        return leg("REJECTS", False, "%s" % e)
    bad = []
    for sid in cfg["refused_staged"]:
        if not re.search(r"\b%s\b" % re.escape(sid), text):
            bad.append("refused staged %s not named" % sid)
    for fname in cfg["refused_files"]:
        if fname not in text:
            bad.append("%s not named" % fname)
    lines = text.splitlines()
    for fam in cfg["families"]:
        pat = r"\b%s\b" % re.escape(fam).replace(r"\-", "[- ]")
        if not any(re.search(pat, line, re.I) and NOT_ADOPTED_RE.search(line)
                   for line in lines):
            bad.append("family %r not named as not adopted this round" % fam)
    low = text.lower()
    if not re.search(r"\b(refused|rejected|quarantine)\b", low):
        bad.append("no refusal/quarantine marker")
    if "reason" not in low or "flip" not in low:
        bad.append("reason+flip not recorded in the lesson")
    return leg("REJECTS", not bad, "; ".join(dedupe(bad)))


def leg_ground(mat, mat_base, root, lands, base, cfg):
    """Leg GROUND: the gap sweep at the base registry returns 0 owners,
    re-derived from the base tree; the receipt records it."""
    bad = []
    try:
        receipt = read_tree(mat, GROUND_RECEIPT)
    except Missing:
        receipt = ""
    try:
        base_rows = parse_rows(read_tree(mat_base, REGISTRY))
        base_reg = read_tree(mat_base, REGISTRY)
    except Missing as e:
        return leg("GROUND", False, "base registry unreadable: %s" % e)
    if not receipt:
        bad.append("receipt missing: %s" % GROUND_RECEIPT)
    else:
        m = re.search(r"(\d+)[- ]row", receipt)
        if not m:
            bad.append("receipt names no N-row registry")
        else:
            n = int(m.group(1))
            if n != len(base_rows):
                bad.append("receipt names a %d-row registry; base holds %d"
                           % (n, len(base_rows)))
            if base == BASE and n != LEDGER_ROWS_BASE:
                bad.append("receipt names %d rows; the claim base holds %d"
                           % (n, LEDGER_ROWS_BASE))
        lines = receipt.splitlines()
        for frag in cfg["ground_fragments"]:
            idxs = [i for i, line in enumerate(lines) if frag in line]
            if not idxs:
                bad.append("receipt does not name %s" % frag)
                continue
            zero = False
            for i in idxs:
                window = "\n".join(lines[i:i + 3])
                if re.search(r"\b0\b", lines[i]) or re.search(r"\b0\b", window):
                    zero = True
                    break
            if not zero:
                bad.append("receipt shows no 0 for %s" % frag)
    for frag in cfg["ground_fragments"]:
        hits = [sid for sid, row in base_rows.items()
                if frag.lower() in row_cells(row)[2].lower()]
        if hits:
            bad.append("base registry names %s in %s" % (frag, sorted(hits)))
    strays = [p for p in tree_files(mat_base, "corpus/knowledge")
              if "conlang-scholarship" in os.path.basename(p).lower()]
    if strays:
        bad.append("base tree already holds conlang-scholarship files: %s" % strays)
    return leg("GROUND", not bad, "; ".join(dedupe(bad)))


def leg_citedlines(mat, mat_base, root, lands, base, cfg):
    """Leg CITEDLINES: check-cited-lines.py over both entries, 0 findings."""
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


def leg_census(mat, mat_base, root, lands, base, cfg, fleet_root, census_sh):
    """Leg CENSUS: census validate over the registry bytes of <lands>."""
    script = census_sh or os.environ.get("KOTODAMA_CENSUS_SH") or \
        os.path.join(fleet_root, "scripts/sources-census.sh")
    if not os.path.isfile(script):
        return leg("CENSUS", False, "census script not found: %s" % script)
    bad = []
    with tempfile.TemporaryDirectory(prefix="r73-fleet-") as fleet:
        link = os.path.join(fleet, "kotodama-shokunin")
        os.symlink(os.path.abspath(mat), link)
        with open(os.path.join(fleet, "shokunin.conf"), "w", encoding="utf-8") as fh:
            fh.write('LANES="\n'
                     'kotodama|kotodama-shokunin|round-73 materialized lands tree\n'
                     '"\n')
        r = subprocess.run([script, "validate", "--root", fleet,
                            "--today", ACCESS_DATE, "kotodama"],
                           capture_output=True, text=True)
    if r.returncode != 0:
        bad.append("census exit=%d" % r.returncode)
    errs = re.findall(r"^kotodama\t(E\d\d)\t.*$", r.stdout, re.M)
    if errs:
        bad.append("census findings: %s" % ",".join(sorted(set(errs))))
    if not re.search(r"^kotodama\tok\t", r.stdout, re.M):
        bad.append("census did not report the lane ok")
    detail = "exit=%d" % r.returncode
    tail = r.stdout.strip().splitlines()[-1] if r.stdout.strip() else ""
    if tail:
        detail += " last-line=%s" % tail
    if bad:
        detail = "; ".join(bad) + " (" + detail + ")"
    return leg("CENSUS", not bad, detail)


def leg_scratch_mirror(mat, mat_base, root, lands, base, cfg):
    """Leg SCRATCHMIRROR: receipt exit 0 on the mirrored corpus carrying the
    adopted rows, committed strictly before the registry append."""
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
    first = cfg["rows"][0] if cfg["rows"] else "S876"
    app = git(root, "log", lands, "-S", first, "--format=%H", "--", REGISTRY)
    app_lines = [l for l in app.stdout.splitlines() if l.strip()]
    intro = git(root, "log", lands, "--diff-filter=A", "--format=%H", "--", RECEIPT)
    intro_lines = [l for l in intro.stdout.splitlines() if l.strip()]
    if not app_lines:
        bad.append("no registry-append commit reachable from lands for %s" % first)
    elif not intro_lines:
        bad.append("receipt has no introductory commit")
    else:
        appc, introc = app_lines[-1], intro_lines[-1]
        if introc == appc:
            bad.append("receipt committed in the append commit (not before)")
        else:
            anc = git(root, "merge-base", "--is-ancestor", introc, appc)
            if anc.returncode != 0:
                bad.append("receipt commit %s not before append commit %s"
                           % (introc[:12], appc[:12]))
    return leg("SCRATCHMIRROR", not bad, "; ".join(dedupe(bad)))


def _first_existing(tree, paths):
    for p in paths:
        if os.path.isfile(os.path.join(tree, p)):
            return p
    return None


def leg_collcheck(mat, mat_base, root, lands, base, cfg):
    """Leg COLLCHECK: indent-guarded collisions carry no adopted id; the
    regenerated renumber map supersedes the round-71 map, whose bytes are
    untouched base..lands."""
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
        return leg("COLLCHECK", False, "collision id files missing under %s" % ASSIM)
    d, v = found
    reg_ids = set(TOKEN_RE.findall(read_tree(mat, d + "/" + v[0])))
    staged_ids = set(TOKEN_RE.findall(read_tree(mat, d + "/" + v[1])))
    collide_ids = set(TOKEN_RE.findall(read_tree(mat, d + "/" + v[2])))
    adopted = set(cfg["rows"])
    bad = []
    if not staged_ids:
        bad.append("staged-ids is empty")
    for sid in sorted(adopted, key=lambda s: int(s[1:])):
        if sid in reg_ids:
            bad.append("%s present in reg-ids (id not free)" % sid)
        if sid in collide_ids:
            bad.append("%s listed in collisions" % sid)
    for lane_id, staged_id in sorted(cfg["row_staged"].items()):
        if staged_id not in staged_ids:
            bad.append("staged id %s (-> %s) absent from staged-ids"
                       % (staged_id, lane_id))

    # 0-3-space-indent guard: a planted indented collision was detected.
    guard = None
    if os.path.isdir(os.path.join(mat, GUARD_DIR)):
        for rel in tree_files(mat, GUARD_DIR):
            try:
                text = read_tree(mat, rel)
            except Missing:
                continue
            planted = INDENTED_ROW_RE.findall(text)
            if planted and re.search(r"(?i)collision", text) and \
                    re.search(r"(?i)exit\s*[=:]?\s*1|\bfail|\bdetected|non-?empty|SURVIVED|killed", text):
                guard = (rel, planted)
                break
    if guard is None:
        bad.append("no indent-guard proof under %s (planted 1-3-space collision "
                   "with a detection marker)" % GUARD_DIR)
    else:
        rel, planted = guard
        for pid in planted:
            if pid in adopted:
                bad.append("guard proof %s plants an adopted id %s" % (rel, pid))

    # regenerated renumber map, old->new, supersedes round-71.
    map_path = _first_existing(mat, (RENUMBER_MAP, RENUMBER_MAP_DRAFT))
    if map_path is None:
        bad.append("no regenerated renumber map (%s or %s)" % (RENUMBER_MAP,
                                                               RENUMBER_MAP_DRAFT))
    else:
        try:
            doc = json.loads(read_tree(mat, map_path))
        except ValueError:
            doc = None
        if not isinstance(doc, dict):
            bad.append("%s is not a JSON object" % map_path)
        else:
            mapping = doc.get("map")
            if not isinstance(mapping, dict):
                bad.append("%s has no map object" % map_path)
                mapping = {}
            targets = {}
            for old, new in mapping.items():
                if isinstance(new, dict):
                    new = new.get("target") or new.get("lane")
                if not isinstance(old, str) or not isinstance(new, str):
                    continue
                old, new = old.strip().upper(), new.strip().upper()
                if not TOKEN_RE.fullmatch(old) or not TOKEN_RE.fullmatch(new):
                    continue
                if old == new:
                    bad.append("map keeps id %s (arithmetic, not a re-point)" % old)
                if old not in staged_ids:
                    bad.append("map old id %s absent from staged-ids" % old)
                targets.setdefault(new, []).append(old)
            for sid in sorted(adopted, key=lambda s: int(s[1:])):
                if sid not in targets:
                    bad.append("map records no old->new for %s" % sid)
            sup = str(doc.get("supersedes") or "")
            if "round-71" not in sup or "id-renumber-map.json" not in sup:
                bad.append("%s supersedes does not name the round-71 map" % map_path)

    # stale round-71 map bytes untouched base..lands.
    at_base = git(root, "cat-file", "-e", "%s:%s" % (base, STALE_MAP))
    if at_base.returncode == 0:
        diff = git(root, "diff", "--quiet", base, lands, "--", STALE_MAP)
        if diff.returncode != 0:
            bad.append("stale round-71 map changed base..lands (%s)" % STALE_MAP)
    return leg("COLLCHECK", not bad, "; ".join(dedupe(bad)))


def run_legs(mat, mat_base, root, lands, base, cfg, fleet_root, census_sh):
    checks = (
        ("ENTRIES", leg_entries),
        ("ROWS", leg_rows),
        ("REPOINTED", leg_repointed),
        ("GATE", leg_gate),
        ("EVIDENCE", leg_evidence),
        ("REJECTS", leg_rejects),
        ("GROUND", leg_ground),
        ("CITEDLINES", leg_citedlines),
        ("CENSUS", lambda m, mb, r, l, b, c: leg_census(m, mb, r, l, b, c,
                                                        fleet_root, census_sh)),
        ("SCRATCHMIRROR", leg_scratch_mirror),
        ("COLLCHECK", leg_collcheck),
    )
    results = []
    for name, fn in checks:
        try:
            ok = fn(mat, mat_base, root, lands, base, cfg)
        except Missing as e:
            ok = leg(name, False, "missing at lands: %s" % e)
        except (OSError, RuntimeError, subprocess.SubprocessError) as e:
            ok = leg(name, False, "%s: %s" % (type(e).__name__, e))
        results.append((name, bool(ok)))
    passed = sum(1 for _n, ok in results if ok)
    return passed, len(results), results


def print_receipt(root, lands, base, mat, cfg):
    tree = git(root, "rev-parse", "%s^{tree}" % lands).stdout.strip()
    head = git(root, "rev-parse", "HEAD").stdout.strip()
    print("# round-73 acceptance counter — claim C (conlang-scholarship assimilation)")
    print("# counter sha256 (self): %s" % counter_sha256())
    print("# stamped revision: %s" % lands)
    print("# evaluated revision: %s" % lands)
    print("# measured revision (lane main): %s" % head)
    print("# tree: %s" % tree)
    print("# base revision: %s" % base)
    print("# materialized: git archive of the stamped revision at %s" % mat)
    print("# worktree graded: no (leg bytes read only from the materialized tree)")
    print("# access date: %s" % ACCESS_DATE)
    print("# config source: %s" % cfg["config_source"])
    print("# adopted rows: %s" % " ".join(cfg["rows"]))
    print("# entries: %s" % " ; ".join(cfg["entries"]))
    print()


def main(argv=None):
    ap = argparse.ArgumentParser(
        description="round-73 coverage counter (claim C)")
    ap.add_argument("--root", default=".", help="lane repository root")
    ap.add_argument("--lands", default=None,
                    help="required lands revision (40-hex commit)")
    ap.add_argument("--base", default=BASE,
                    help="frozen base revision (default: claim base)")
    ap.add_argument("--fleet-root", default=None,
                    help="fleet root (default: lane parent)")
    ap.add_argument("--census-sh", default=None,
                    help="census script path (override)")
    ap.add_argument("--selftest", action="store_true", help="run in-process cases")
    args = ap.parse_args(argv)

    if args.selftest:
        return run_selftest()

    if not args.lands or not re.fullmatch(r"[0-9a-fA-F]{40}", args.lands.strip()):
        print("ERROR: --lands must be a 40-hex commit "
              "(the worktree is never graded, QUALITY 19)", file=sys.stderr)
        return 2
    lands = args.lands.strip().lower()
    base = args.base.strip().lower()
    root = args.root if os.path.isabs(args.root) else os.path.join(LANE, args.root)
    if not os.path.isdir(os.path.join(root, ".git")):
        print("ERROR: not a git repository: %s" % root, file=sys.stderr)
        return 2
    if git(root, "cat-file", "-e", "%s^{commit}" % lands).returncode != 0:
        print("ERROR: --lands revision not found: %s" % lands, file=sys.stderr)
        return 2
    if git(root, "cat-file", "-e", "%s^{commit}" % base).returncode != 0:
        print("ERROR: --base revision not found: %s" % base, file=sys.stderr)
        return 2
    fleet_root = args.fleet_root or os.path.dirname(os.path.abspath(root))

    with tempfile.TemporaryDirectory(prefix="r73-lands-") as tmp:
        mat = os.path.join(tmp, "lands")
        mat_base = os.path.join(tmp, "base")
        os.makedirs(mat)
        os.makedirs(mat_base)
        try:
            materialize(root, lands, mat)
            materialize(root, base, mat_base)
        except RuntimeError as e:
            print("ERROR: %s" % e, file=sys.stderr)
            return 2
        cfg = load_config(mat, root)
        print_receipt(root, lands, base, mat, cfg)
        passed, total, _results = run_legs(mat, mat_base, root, lands, base, cfg,
                                           fleet_root, args.census_sh)
    ok = passed == total
    print("ACCEPT-C-73: %s legs=%d/%d" % ("PASS" if ok else "FAIL", passed, total))
    return 0 if ok else 1


# --------------------------------------------------------------------------
# selftest — every fixture repo is a fresh mktemp dir, every git call names it
# --------------------------------------------------------------------------

def gitq(lane, *args):
    return subprocess.run(["git", "-C", lane, *args],
                          capture_output=True, text=True)


def git_write(lane, rel, content):
    p = os.path.join(lane, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
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


BASE_REGISTRY = """\
# SOURCES — selftest registry

## Registry

| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
| S001 | Selftest one — https://example.com/one | docs | A | s | a | teaches one | mined | 2026-10-19 | 90d | — |
| S874 | Selftest two — https://example.com/two | docs | B | s | a | teaches two | mined | 2026-10-25 | 180d | — |
| S875 | Selftest three — https://example.com/three | docs | B | s | a | teaches three | mined | 2026-10-25 | 180d | — |
"""

ENTRY_ONE = "corpus/knowledge/linguistics/conlang-scholarship.md"
ENTRY_TWO = ("corpus/knowledge/linguistics/"
             "conlang-scholarship.amend-2026-10-23.md")

ENTRY_ONE_TEXT = """\
# Conlang scholarship — fixture entry

source: S876 — https://fixture.example/a — §1 abstract — fetched 2026-10-25
source: S877 — https://fixture.example/b — аннотация — fetched 2026-10-25
source: S880 — https://fixture.example/e — §4 — fetched 2026-10-25
verified-at: 2026-10-25
recheck: 180d — re-run the row recheck commands (ran 2026-10-25)
ground: the wave brief's scoped domain, which the lane served from no research venue.
- topic: fixture topic one.
- gap filled: `grep` over the registry returns 0.
- sources: the three rows above.
- couples: `linguistics/conlang-methodology.md`.
- scope: a fixture reference method; it decides no world's language.

## Body

1. A fixture claim carried by S876.
"""

ENTRY_TWO_TEXT = """\
# Amendment — fixture entry

source: S878 — https://fixture.example/c — Abstract, p. 455 — fetched 2026-10-25
source: S879 — https://fixture.example/d — §2 — fetched 2026-10-25
source: S880 — https://fixture.example/e — §4 — fetched 2026-10-25
verified-at: 2026-10-25
recheck: 180d — re-run the row recheck commands (ran 2026-10-25)
ground: the fixture entry cited an abstract only.
- topic: fixture topic two.
- gap filled: the method detail the abstract could not supply.
- sources: the three rows above.
- couples: `linguistics/conlang-scholarship.md`.
- scope: a fixture amendment; it decides no world's language.

## Body (dated addition)

- A fixture amendment claim carried by S878.
"""

ROWS_APPEND = """\
| S876 | Fixture A — https://fixture.example/a | paper | B | s | §1 "fixture quote a" | teaches A | mined | 2026-10-25 | 180d | corpus/knowledge/linguistics/conlang-scholarship.md |
| S877 | Fixture B — https://fixture.example/b | book | B | s | §2 "fixture quote b" | teaches B | mined | 2026-10-25 | 180d | corpus/knowledge/linguistics/conlang-scholarship.md |
| S878 | Fixture C — https://fixture.example/c | paper | B | s | §3 "fixture quote c" | teaches C | mined | 2026-10-25 | 180d | corpus/knowledge/linguistics/conlang-scholarship.amend-2026-10-23.md |
| S879 | Fixture D — https://fixture.example/d | paper | B | s | §4 "fixture quote d" | teaches D | mined | 2026-10-25 | 180d | corpus/knowledge/linguistics/conlang-scholarship.amend-2026-10-23.md |
| S880 | Fixture E — https://fixture.example/e | paper | B | s | §5 "fixture quote e" | teaches E | mined | 2026-10-25 | 180d | corpus/knowledge/linguistics/conlang-scholarship.md, corpus/knowledge/linguistics/conlang-scholarship.amend-2026-10-23.md |
"""

LESSON_GATE = """\
# Round 73 — selftest lesson

## Gate

Admitted this round (opened by this lane 2026-10-25):

| source | access date | quote (≤25 words) | grounds | verdict |
|---|---|---|---|---|
| S876 — https://fixture.example/a | 2026-10-25 | "fixture quote a" | §1 abstract | admitted |
| S877 — https://fixture.example/b | 2026-10-25 | "fixture quote b" | аннотация | admitted |
| S878 — https://fixture.example/c | 2026-10-25 | "fixture quote c" | p. 455 | admitted |
| S879 — https://fixture.example/d | 2026-10-25 | "fixture quote d" | §2 | admitted |
| S880 — https://fixture.example/e | 2026-10-25 | "fixture quote e" | §4 | admitted |

Rejected from the assimilation set (reason + flip; every reject records the
URL it rejected):

| staged entry | staged rows | reason | flip | verdict |
|---|---|---|---|---|
| conlang-methodology.md | S869 | payload unreachable: https://fixture.example/refused-a | reopen the URL when it serves | rejected |
| conlang-scholarship.amend-2026-10-23.md | S894 | quarantine-REFUSED: https://fixture.example/refused-b | a re-opened source carrying the span | rejected |
| conlang-scholarship.amend-2026-10-23b.md | S910 | quarantine-REFUSED: https://fixture.example/refused-c | a re-opened source carrying the span | rejected |

Not adopted this round: the naming-systems, calendar, era and verification
staged families.

## Mistakes

| class | evidence | captured-by | fix | state |
|---|---|---|---|---|
| fixture | selftest only | n/a | n/a | new |
"""

GROUND_RECEIPT_TEXT = """\
# round-73 gap sweep (selftest fixture)
# stamp: 2026-10-25 10:00:00 UTC
$ find corpus/knowledge -iname '*conlang-scholarship*' | wc -l
0
ojs.unito.it rows: 0
philol.msu.ru rows: 0
journals.rudn.ru rows: 0
cyberleninka.ru/article/n/klassifikatsii rows: 0
sanders.phonologist.org rows: 0
gap-sweep at the 3-row registry: owners 0
"""

RECEIPT_TEXT = """\
# round-73 scratch-mirror validation receipt (selftest fixture)
# stamp: 2026-10-25 10:00:00 UTC
census validate --file /tmp/r73-mirror/corpus/SOURCES.md
exit 0
rows present in mirror: S876 S877 S878 S879 S880
"""

GUARD_TEXT = """\
# 0-3-space-indent guard proof (selftest fixture)

Planted row (three leading spaces, one past the two-space form):

   | S999 | planted indented row — https://fixture.example/planted | docs | B | s | §1 | planted | mined | 2026-10-25 | 90d | — |

parser output: collision detected: S999 present in reg-ids
exit 1
"""

RENUMBER_TEXT = """\
{
 "drafted": "2026-10-25",
 "registry_count_at_draft": 3,
 "registry_last_id": "S875",
 "next_free": "S876",
 "supersedes": ".ufo/waves/round-71/assimilation/id-renumber-map.json",
 "map": {
  "S881": "S876",
  "S882": "S877",
  "S892": "S878",
  "S893": "S879",
  "S901": "S880"
 },
 "assignments": [
  {"staged_id": "S881", "new_target": "S876", "url": "https://fixture.example/a"},
  {"staged_id": "S882", "new_target": "S877", "url": "https://fixture.example/b"},
  {"staged_id": "S892", "new_target": "S878", "url": "https://fixture.example/c"},
  {"staged_id": "S893", "new_target": "S879", "url": "https://fixture.example/d"},
  {"staged_id": "S901", "new_target": "S880", "url": "https://fixture.example/e"}
 ]
}
"""

STAGED_IDS_TEXT = "\n".join(
    ["S859", "S869", "S881", "S882", "S892", "S893", "S894", "S901", "S910"]) + "\n"
REG_IDS_TEXT = "\n".join(["S001", "S874", "S875"]) + "\n"
COLLISIONS_TEXT = "S859\nS860\n"

CENSUS_STUB_OK = "#!/bin/sh\nprintf 'kotodama\\tok\\tstub\\n'\nexit 0\n"
CENSUS_STUB_FAIL = "#!/bin/sh\nprintf 'kotodama\\tE06\\tS876 tier=Z\\n'\nexit 1\n"

CLAIMS_FIXTURE = {
    "round": 73,
    "claims": [
        {
            "id": "C",
            "axis": "coverage",
            "row_set": [
                {"id": "S876", "staged": "S881"},
                {"id": "S877", "staged": "S882"},
                {"id": "S878", "staged": "S892"},
                {"id": "S879", "staged": "S893"},
                {"id": "S880", "staged": "S901"},
            ],
            "entries": {"paths": [ENTRY_ONE, ENTRY_TWO]},
            "rejects": {
                "refused_staged": ["S869", "S894", "S910"],
                "refused_files": ["conlang-methodology.md",
                                  "conlang-scholarship.amend-2026-10-23.md",
                                  "conlang-scholarship.amend-2026-10-23b.md"],
                "families": ["naming-systems", "calendar", "era",
                             "verification"],
            },
            "ground": {"fragments": list(DEFAULT_GROUND_FRAGMENTS)},
        }
    ],
}


MUTANTS = {
    "drop_entry": {"drop_entry": True},
    "staged_as_is": {"staged_as_is": True},
    "usedby_empty": {"usedby_empty": True},
    "row_gap": {"row_gap": True},
    "repoint_url": {"repoint_url": True},
    "campaign_id": {"campaign_id": True},
    "gate_quote": {"gate_quote": True},
    "gate_reject_no_url": {"gate_reject_no_url": True},
    "gate_no_admit": {"gate_no_admit": True},
    "no_rejects": {"no_rejects": True},
    "family_missing": {"family_missing": True},
    "ground_zero": {"ground_zero": True},
    "receipt_no_exit": {"receipt_no_exit": True},
    "receipt_in_append": {"receipt_in_append": True},
    "collisions": {"collisions": True},
    "guard_missing": {"guard_missing": True},
    "map_missing": {"map_missing": True},
    "multi_id_line": {"multi_id_line": True},
    "census_fail": {"census_fail": True},
    "junk_rows": {"junk_rows": True},
    "evidence_missing": {"evidence_missing": True},
    "evidence_notfound": {"evidence_notfound": True},
    "anchor_no_quote": {"anchor_no_quote": True},
    "placeholder_header": {"placeholder_header": True},
}

EXPECTED_FAIL = {
    "drop_entry": "ENTRIES",
    "staged_as_is": "ROWS",
    "usedby_empty": "ROWS",
    "row_gap": "ROWS",
    "repoint_url": "REPOINTED",
    "campaign_id": "REPOINTED",
    "gate_quote": "GATE",
    "gate_reject_no_url": "GATE",
    "gate_no_admit": "GATE",
    "no_rejects": "REJECTS",
    "family_missing": "REJECTS",
    "ground_zero": "GROUND",
    "receipt_no_exit": "SCRATCHMIRROR",
    "receipt_in_append": "SCRATCHMIRROR",
    "collisions": "COLLCHECK",
    "guard_missing": "COLLCHECK",
    "map_missing": "COLLCHECK",
    "multi_id_line": "CITEDLINES",
    "census_fail": "CENSUS",
    "junk_rows": "ENTRIES",
    "evidence_missing": "EVIDENCE",
    "evidence_notfound": "EVIDENCE",
    "anchor_no_quote": "ROWS",
    "placeholder_header": "ENTRIES",
}


def build_fixture(prefix, mut=None):
    mut = mut or {}
    lane = tempfile.mkdtemp(prefix=prefix + "-", suffix="-lane")
    stub = os.path.join(lane, "census-stub.sh")
    with open(stub, "w", encoding="utf-8") as fh:
        fh.write(CENSUS_STUB_FAIL if mut.get("census_fail") else CENSUS_STUB_OK)
    os.chmod(stub, 0o755)
    if gitq(lane, "init", "-q").returncode != 0:
        raise RuntimeError("git init failed")
    git_write(lane, "corpus/SOURCES.md", BASE_REGISTRY)
    git_write(lane, STALE_MAP, '{\n "map": {"S859": "S874"},\n "supersedes": "none"\n}\n')
    tool_src = os.path.join(LANE, "tools/check-cited-lines.py")
    with open(tool_src, encoding="utf-8") as fh:
        git_write(lane, "tools/check-cited-lines.py", fh.read())
    base = git_commit(lane, "base")

    if not mut.get("junk_rows"):
        receipt = RECEIPT_TEXT
        if mut.get("receipt_no_exit"):
            receipt = receipt.replace("exit 0", "exit 1")
        if not mut.get("receipt_in_append"):
            git_write(lane, RECEIPT, receipt)
        git_write(lane, ASSIM + "/reg-ids", REG_IDS_TEXT)
        git_write(lane, ASSIM + "/staged-ids", STAGED_IDS_TEXT)
        collisions = COLLISIONS_TEXT
        if mut.get("collisions"):
            collisions += "S876\n"
        git_write(lane, ASSIM + "/collisions", collisions)
        if not mut.get("guard_missing"):
            git_write(lane, GUARD_DIR + "/planted-indented-collision.txt", GUARD_TEXT)
        if not mut.get("map_missing"):
            git_write(lane, RENUMBER_MAP, RENUMBER_TEXT)
        if mut.get("claims") or mut.get("claims_narrow"):
            doc = json.loads(json.dumps(CLAIMS_FIXTURE))
            if mut.get("claims_narrow"):
                doc["claims"][0]["row_set"] = [
                    r for r in doc["claims"][0]["row_set"] if r["id"] != "S880"]
            git_write(lane, CLAIMS, json.dumps(doc, indent=1, ensure_ascii=False) + "\n")
        if not mut.get("evidence_missing"):
            for letter, rid in zip("abcde", ["S876", "S877", "S878", "S879", "S880"]):
                body = ("# evidence %s\nfetch: GET https://fixture.example/%s\n"
                        "user-agent: Mozilla/5.0 (X11; Linux x86_64)\naccess-date: 2026-10-25\n"
                        "http-status: 200\nbytes: 10\nsha256: %s\nextract: fixture\n"
                        "locator: s\nquote-words: 3\nquote-found-verbatim: %s\n"
                        "quote: fixture quote %s\n--- context window (x) ---\n"
                        "before fixture quote %s after\n"
                        % (rid, letter, "ab" * 32,
                           "NO" if mut.get("evidence_notfound") else "yes", letter, letter))
                git_write(lane, EVIDENCE_DIR + "/" + rid + ".txt", body)
        git_commit(lane, "mirror receipt + id lists + guard proof + map")
        if mut.get("receipt_in_append"):
            git_write(lane, RECEIPT, receipt)

    registry = BASE_REGISTRY + "\n" + ROWS_APPEND
    if mut.get("staged_as_is"):
        registry = registry.replace(
            "| S876 | Fixture A — https://fixture.example/a | paper | B | s | §1 \"fixture quote a\" | teaches A | mined | 2026-10-25 | 180d |",
            "| S876 | Fixture A — https://fixture.example/a | paper | B | s | §1 \"fixture quote a\" | teaches A | mined | 2026-10-23 | 180d — `curl ... \\| grep -c x` -> 2 (ran 2026-10-23) |")
    if mut.get("anchor_no_quote"):
        registry = registry.replace('§1 "fixture quote a"', "§1")
    if mut.get("usedby_empty"):
        registry = registry.replace(
            "| 180d | corpus/knowledge/linguistics/conlang-scholarship.amend-2026-10-23.md |\n| S879",
            "| 180d | — |\n| S879")
    if mut.get("row_gap"):
        registry = "\n".join(line for line in registry.splitlines()
                             if not line.startswith("| S879 |")) + "\n"
    if mut.get("repoint_url"):
        registry = registry.replace("Fixture A — https://fixture.example/a",
                                    "Fixture A — https://other.example/x")
    if mut.get("junk_rows"):
        git_write(lane, "corpus/SOURCES.md", registry)
        git_commit(lane, "lands: junk rows only")
        lands = gitq(lane, "rev-parse", "HEAD").stdout.strip()
        return lane, base, lands, stub

    git_write(lane, "corpus/SOURCES.md", registry)
    git_write(lane, ENTRY_ONE, ENTRY_ONE_TEXT)
    if not mut.get("drop_entry"):
        git_write(lane, ENTRY_TWO, ENTRY_TWO_TEXT)
    if mut.get("placeholder_header"):
        git_write(lane, ENTRY_TWO, re.sub(r"(?m)^- topic:.*$", "- topic: TODO", ENTRY_TWO_TEXT, count=1))
    if mut.get("multi_id_line"):
        git_write(lane, ENTRY_ONE, ENTRY_ONE_TEXT.replace(
            "1. A fixture claim carried by S876.",
            "1. A fixture claim carried by S876 (S877)."))
    if mut.get("campaign_id"):
        git_write(lane, ENTRY_ONE, ENTRY_ONE_TEXT.replace(
            "1. A fixture claim carried by S876.",
            "1. A fixture claim carried by S876.\n2. An earlier campaign id S728 stands here."))

    lesson = LESSON_GATE
    if mut.get("gate_quote"):
        lesson = lesson.replace(
            '"fixture quote a"',
            '"a b c d e f g h i j k l m n o p q r s t u v w x y z aa"')
    if mut.get("gate_reject_no_url"):
        lesson = lesson.replace("https://fixture.example/refused-a", "the URL")
        lesson = lesson.replace("https://fixture.example/refused-b", "the URL")
        lesson = lesson.replace("https://fixture.example/refused-c", "the URL")
    if mut.get("gate_no_admit"):
        lesson = lesson.replace("| admitted |", "| seen |")
    if mut.get("no_rejects"):
        lesson = lesson.split("Rejected from the assimilation set")[0] + \
            "Not adopted this round: the naming-systems, calendar, era and " \
            "verification staged families.\n\n## Mistakes\n"
    if mut.get("family_missing"):
        lesson = lesson.replace(
            "Not adopted this round: the naming-systems, calendar, era and "
            "verification\nstaged families.",
            "Not adopted this round: other staged families.")
    git_write(lane, LESSON, lesson)

    ground = GROUND_RECEIPT_TEXT
    if mut.get("ground_zero"):
        ground = ground.replace("philol.msu.ru rows: 0\n", "")
    git_write(lane, GROUND_RECEIPT, ground)

    git_commit(lane, "lands: entries, rows, lesson")
    lands = gitq(lane, "rev-parse", "HEAD").stdout.strip()
    return lane, base, lands, stub


def run_selftest():
    failures = []
    fixtures = []
    lane, base, lands, stub = build_fixture("r73st-clean")
    fixtures.append(lane)
    r = subprocess.run([sys.executable, "-B", os.path.abspath(__file__),
                        "--root", lane, "--lands", lands, "--base", base,
                        "--census-sh", stub],
                       capture_output=True, text=True)
    if "ACCEPT-C-73: PASS legs=11/11" not in r.stdout:
        failures.append("clean fixture: expected PASS 11/11, got exit=%d\n%s\n%s"
                        % (r.returncode, r.stdout, r.stderr))
    if "# evaluated revision: %s" % lands not in r.stdout:
        failures.append("clean fixture: receipt header does not stamp lands\n%s"
                        % r.stdout)

    # do-nothing control: lands == base must FAIL.
    r = subprocess.run([sys.executable, "-B", os.path.abspath(__file__),
                        "--root", lane, "--lands", base, "--base", base,
                        "--census-sh", stub],
                       capture_output=True, text=True)
    if "ACCEPT-C-73: FAIL" not in r.stdout:
        failures.append("base-lands control: expected FAIL, got exit=%d\n%s"
                        % (r.returncode, r.stdout))

    # required --lands: no worktree grading.
    r = subprocess.run([sys.executable, "-B", os.path.abspath(__file__),
                        "--root", lane, "--base", base, "--census-sh", stub],
                       capture_output=True, text=True)
    if r.returncode != 2 or "--lands" not in r.stderr:
        failures.append("missing-lands: expected exit 2 naming --lands, got %d\n%s"
                        % (r.returncode, r.stderr))

    # row_set / entries read from claims.json at lands (config path).
    lane, base, lands, stub = build_fixture("r73st-claims", {"claims": True})
    fixtures.append(lane)
    r = subprocess.run([sys.executable, "-B", os.path.abspath(__file__),
                        "--root", lane, "--lands", lands, "--base", base,
                        "--census-sh", stub],
                       capture_output=True, text=True)
    if "ACCEPT-C-73: PASS legs=11/11" not in r.stdout:
        failures.append("claims config: expected PASS 11/11, got exit=%d\n%s\n%s"
                        % (r.returncode, r.stdout, r.stderr))
    elif "# config source: lands tree: row_set, entries" not in r.stdout:
        failures.append("claims config: receipt does not disclose the claims source\n%s"
                        % r.stdout)

    # a narrowed row_set must drive ROWS: config is not decorative.
    lane, base, lands, stub = build_fixture("r73st-claims-narrow",
                                             {"claims_narrow": True})
    fixtures.append(lane)
    r = subprocess.run([sys.executable, "-B", os.path.abspath(__file__),
                        "--root", lane, "--lands", lands, "--base", base,
                        "--census-sh", stub],
                       capture_output=True, text=True)
    if "LEG FAIL ROWS" not in r.stdout or "ACCEPT-C-73: FAIL" not in r.stdout:
        failures.append("claims narrow row_set: expected FAIL ROWS\n%s" % r.stdout)

    for name, mut in MUTANTS.items():
        lane, base, lands, stub = build_fixture("r73st-" + name, mut)
        fixtures.append(lane)
        r = subprocess.run([sys.executable, "-B", os.path.abspath(__file__),
                            "--root", lane, "--lands", lands, "--base", base,
                            "--census-sh", stub],
                           capture_output=True, text=True)
        out = r.stdout
        wanted = EXPECTED_FAIL[name]
        if "ACCEPT-C-73: FAIL" not in out:
            failures.append("%s: expected final FAIL, got exit=%d\n%s\n%s"
                            % (name, r.returncode, out, r.stderr))
        elif "LEG FAIL %s" % wanted not in out:
            failures.append("%s: expected leg FAIL %s\n%s" % (name, wanted, out))

    total = 5 + len(MUTANTS)
    passed = total - len(failures)
    print("SELFTEST: %d/%d" % (passed, total))
    for f in failures:
        print("---", f)
    for lane in fixtures:
        shutil.rmtree(lane, ignore_errors=True)
    return 0 if passed == total else 1


if __name__ == "__main__":
    sys.exit(main())
