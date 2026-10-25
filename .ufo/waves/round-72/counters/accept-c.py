#!/usr/bin/env python3
r"""Round-72 coverage acceptance counter — claim C (shokuknow assimilation).

Checks the frozen claim-C predicate (reports/round-72/claims.json) at the
measured lands revision:

  ENTRIES       both heritage-taxonomy entries exist at --lands with the full
                header (source / verified-at / recheck / ground / topic /
                gap filled / sources / couples / scope);
  ROWS          exactly two new registry rows S874 and S875 exist at --lands,
                both status mined, both used-by the two admitted entries,
                no other registry row added or removed;
  REPOINTED     every `source:` citation in the entries names a lane id
                >= S874 whose row's URL matches the cited document;
  GATE          corpus/lessons/round-72.md ## Gate records per new row URL +
                access date 2026-10-25 + <=25-word located quote, and records
                >=1 admit and >=1 reject with reason+flip;
  REJECTS       the lesson names the two refused staged entries
                (narrative-structure-frameworks.md -> S870; worldbuilding-
                setting-practice.amend-2026-10-23.md -> S899/S900);
  GROUND        the round-72 receipt shows the gap sweep returns 0 at the
                pre-append (797-row) registry; independently re-verified
                against the frozen base registry;
  CITEDLINES    tools/check-cited-lines.py over the two entries at --lands
                prints 0 findings;
  CENSUS        scripts/sources-census.sh validate --root <fleet-root>
                kotodama exits 0 at --lands (HEAD == lands);
  SCRATCHMIRROR the scratch-mirror validation receipt
                (.ufo/waves/round-72/assimilation/validate-receipt.txt)
                shows census validate --file exit 0 on the mirrored corpus
                BEFORE the registry append, with the two rows in it;
  COLLCHECK     the id-collision check at .ufo/waves/round-72/assimilation/
                shows reg/staged id lists and an empty collisions file for
                the adopted rows' new ids (S874/S875 not in reg-ids).

Every lane file is read as committed bytes via `git show`.  CENSUS is the
one leg the claim itself defines as running the census command against the
worktree; CITEDLINES materializes the two committed entries into a temporary
directory before running the tool on them.

Exit: 0 all legs pass; 1 any leg fails; 2 input error.
"""

import argparse
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
BASE = "b60c7b140c5350caa7d1073711f14092541533f0"
REGISTRY = "corpus/SOURCES.md"
LESSON = "corpus/lessons/round-72.md"
ASSIM = ".ufo/waves/round-72/assimilation"
RECEIPT = ASSIM + "/validate-receipt.txt"
GROUND_RECEIPT = "reports/round-72/telemetry/gap-sweep.txt"
ENTRIES = (
    "corpus/knowledge/culture-material/heritage-taxonomy-models.md",
    "corpus/knowledge/culture-material/heritage-taxonomy-models.amend-2026-10-24-r13.md",
)
NEW_IDS = ("S874", "S875")
MIRROR_ID_FILES = ("reg-ids", "staged-ids", "collisions")
HEADER_FIELDS = ("source", "verified-at", "recheck", "ground", "topic",
                 "gap-filled", "sources", "couples", "scope")

ROW_RE = re.compile(r"^\s{0,3}\|\s*(S\d{3,})\s*\|")
TOKEN_RE = re.compile(r"\bS\d{3,}\b")
URL_RE = re.compile(r"https?://[^\s]+")
QUOTE_RE = re.compile(r'"(?:\\.|[^"\\\n])*"|“[^“”\n]*”|«[^«»\n]*»')
H2_RE = re.compile(r"^##\s")
GATE_RE = re.compile(r"^##\s+Gate\b")


class Missing(Exception):
    """A committed path cannot be read at the requested revision."""


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


def show(root, rev, path):
    r = git(root, "show", "%s:%s" % (rev, path))
    if r.returncode != 0:
        raise Missing(path)
    return r.stdout


def parse_rows(text):
    rows = {}
    for line in text.splitlines():
        m = ROW_RE.match(line)
        if m:
            rows[m.group(1)] = line
    return rows


def row_cells(row):
    return [c.strip() for c in row.split("|")]


def leg(name, passed, detail=""):
    print("LEG %s %s" % ("PASS" if passed else "FAIL", name))
    if detail:
        print("     %s" % detail)
    return bool(passed)


def header_block(text):
    """Lines before the first H2 heading (the entry header block)."""
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
    """`source:` bullet lines in the header block, with the dash optional."""
    out = []
    for line in header_block(text):
        m = re.match(r"^[-*\s]*source:\s*(.*)$", line)
        if m:
            out.append(m.group(1))
    return out


def urls_in(s):
    return [u for u in URL_RE.findall(s)]


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
    """Pipe-table rows; indented continuation lines join the previous row."""
    rows = []
    for line in lines:
        if line.lstrip().startswith("|"):
            rows.append(line.strip())
        elif line.startswith(" ") and rows:
            rows[-1] += " " + line.strip()
    return rows


def registry_sweep(text):
    return (len(re.findall(r"(?i)ihchina", text)),
            len(re.findall(r"(?i)bunka\.go\.jp", text)))


def leg_entries(root, lands, base):
    """Leg ENTRIES: both files exist at lands with the full header."""
    bad = []
    for e in ENTRIES:
        try:
            text = show(root, lands, e)
        except Missing:
            bad.append("%s missing" % e)
            continue
        if not text.strip():
            bad.append("%s empty" % e)
        missing_fields = [f for f in HEADER_FIELDS
                          if norm_label(f) not in header_field_names(text)]
        if missing_fields:
            bad.append("%s header missing: %s" % (e, ",".join(missing_fields)))
    return leg("ENTRIES", not bad, "; ".join(bad))


def leg_rows(root, lands, base):
    """Leg ROWS: exactly S874/S875 added, mined, used-by the two entries."""
    try:
        base_rows = parse_rows(show(root, base, REGISTRY))
        lands_rows = parse_rows(show(root, lands, REGISTRY))
    except Missing as e:
        return leg("ROWS", False, "registry unreadable: %s" % e)
    added = set(lands_rows) - set(base_rows)
    removed = set(base_rows) - set(lands_rows)
    bad = []
    if added != set(NEW_IDS):
        bad.append("added=%s (want S874/S875)" % sorted(added))
    if removed:
        bad.append("removed=%s (want none)" % sorted(removed))
    union_usedby = set()
    for sid in NEW_IDS:
        if sid not in lands_rows:
            bad.append("%s row missing" % sid)
            continue
        cells = row_cells(lands_rows[sid])
        status = cells[8] if len(cells) > 8 else ""
        usedby = cells[11] if len(cells) > 11 else ""
        if status != "mined":
            bad.append("%s status=%r (want mined)" % (sid, status))
        used = set(p for p in (x.strip() for x in usedby.split(",")) if p)
        if not used:
            bad.append("%s used-by empty" % sid)
        if not used <= set(ENTRIES):
            bad.append("%s used-by out of scope: %s" % (sid, sorted(used)))
        union_usedby |= used
    if union_usedby != set(ENTRIES):
        bad.append("used-by union %s (want both entries)" % sorted(union_usedby))
    return leg("ROWS", not bad, "; ".join(bad))


def leg_repointed(root, lands, base):
    """Leg REPOINTED: every source: citation is id >= S874 whose row URL matches."""
    try:
        lands_rows = parse_rows(show(root, lands, REGISTRY))
    except Missing as e:
        return leg("REPOINTED", False, "registry unreadable: %s" % e)
    bad = []
    for e in ENTRIES:
        try:
            text = show(root, lands, e)
        except Missing:
            bad.append("%s missing" % e)
            continue
        for sline in source_lines(text):
            ids = TOKEN_RE.findall(sline)
            if len(ids) != 1:
                bad.append("%s source line ids=%s (want exactly one)" % (e, ids))
                continue
            sid = ids[0]
            try:
                num = int(sid[1:])
            except ValueError:
                num = 0
            if num < 874:
                bad.append("%s cites %s < S874" % (e, sid))
            if sid not in lands_rows:
                bad.append("%s cites %s with no registry row" % (e, sid))
                continue
            cited = urls_in(sline)
            if not cited:
                bad.append("%s source line has no URL" % e)
            row_urls = urls_in(row_cells(lands_rows[sid])[2])
            row_keys = neutral_url_keys(row_urls)
            for u in cited:
                if norm_url(u) not in row_keys:
                    bad.append("%s cites URL not registered on %s: %s" % (e, sid, u))
    return leg("REPOINTED", not bad, "; ".join(bad))


def leg_gate(root, lands, base):
    """Leg GATE: lesson Gate per-row URL + 2026-10-25 + <=25-word quote,
    plus >=1 admit and >=1 reject with reason+flip."""
    try:
        text = show(root, lands, LESSON)
        lands_rows = parse_rows(show(root, lands, REGISTRY))
    except Missing as e:
        return leg("GATE", False, "%s" % e)
    section = gate_section(text)
    if not section:
        return leg("GATE", False, "no ## Gate section in %s" % LESSON)
    body = "\n".join(section)
    rows = table_rows(section)
    bad = []
    for sid in NEW_IDS:
        if re.search(r"\b%s\b" % sid, body) is None:
            bad.append("%s not named in Gate" % sid)
        row_line = None
        for r in rows:
            if re.search(r"\b%s\b" % sid, r):
                row_line = r
                break
        if row_line is None:
            bad.append("%s has no Gate table row" % sid)
            continue
        if "2026-10-25" not in row_line:
            bad.append("%s row access date missing 2026-10-25" % sid)
        spans = quoted_spans(row_line)
        if not spans:
            bad.append("%s row has no quoted locator" % sid)
        elif any(len(s.split()) > 25 for s in spans):
            bad.append("%s row quote exceeds 25 words" % sid)
        if sid in lands_rows:
            row_urls = urls_in(row_cells(lands_rows[sid])[2])
            if not any(u in body for u in row_urls):
                bad.append("%s row URL not recorded in Gate" % sid)
    admits = rejects = 0
    for r in rows:
        cells = [c.strip() for c in r.split("|")]
        nonempty = [c for c in cells if c]
        verdict = nonempty[-1].lower() if nonempty else ""
        if "admitted" in verdict:
            admits += 1
        if "rejected" in verdict:
            rejects += 1
    if admits < 1:
        bad.append("no admit row (want >=1)")
    if rejects < 1:
        bad.append("no reject row (want >=1)")
    low = body.lower()
    if "reason" not in low or "flip" not in low:
        bad.append("reject reason+flip not recorded in Gate")
    return leg("GATE", not bad, "; ".join(bad))


def leg_rejects(root, lands, base):
    """Leg REJECTS: lesson names the two refused staged entries and rows."""
    try:
        text = show(root, lands, LESSON)
    except Missing as e:
        return leg("REJECTS", False, "%s" % e)
    bad = []
    if "narrative-structure-frameworks.md" not in text:
        bad.append("narrative-structure-frameworks.md not named")
    if re.search(r"\bS870\b", text) is None:
        bad.append("refused staged S870 not named")
    if "worldbuilding-setting-practice.amend-2026-10-23.md" not in text:
        bad.append("worldbuilding-setting-practice.amend-2026-10-23.md not named")
    if re.search(r"\bS899\b", text) is None or re.search(r"\bS900\b", text) is None:
        bad.append("refused staged S899/S900 not named")
    low = text.lower()
    if not any(t in low for t in ("refused", "rejected", "quarantine")):
        bad.append("no refusal/quarantine marker")
    return leg("REJECTS", not bad, "; ".join(bad))


def leg_ground(root, lands, base):
    """Leg GROUND: receipt shows the gap sweep returns 0 at the pre-append
    797-row registry; the frozen base registry is re-verified directly."""
    bad = []
    try:
        receipt = show(root, lands, GROUND_RECEIPT)
    except Missing:
        receipt = ""
    if not receipt:
        bad.append("receipt missing: %s" % GROUND_RECEIPT)
    else:
        if re.search(r"\b797\b", receipt) is None:
            bad.append("receipt does not name the 797-row registry")
        for token in ("ihchina", "bunka"):
            if not re.search(r"(?i)(%s[^\n]*\b0\b|\b0\b[^\n]*%s)" % (token, token), receipt):
                bad.append("receipt does not show %s sweep 0" % token)
    try:
        base_reg = show(root, base, REGISTRY)
    except Missing as e:
        bad.append("base registry unreadable: %s" % e)
    else:
        ih, bk = registry_sweep(base_reg)
        if ih != 0 or bk != 0:
            bad.append("base registry sweep ihchina=%d bunka=%d (want 0/0)" % (ih, bk))
    return leg("GROUND", not bad, "; ".join(bad))


def leg_citedlines(root, lands, base):
    """Leg CITEDLINES: check-cited-lines.py over the two entries, 0 findings."""
    bad = []
    with tempfile.TemporaryDirectory(prefix="r72-cited-") as tmp:
        paths = []
        for e in ENTRIES:
            try:
                text = show(root, lands, e)
            except Missing as ex:
                bad.append("%s" % ex)
                continue
            p = os.path.join(tmp, os.path.basename(e))
            with open(p, "w", encoding="utf-8") as fh:
                fh.write(text)
            paths.append(p)
        if not paths:
            return leg("CITEDLINES", False, "; ".join(bad))
        tool = os.path.join(root, "tools/check-cited-lines.py")
        r = subprocess.run([sys.executable, "-B", tool] + paths,
                           capture_output=True, text=True)
        out = r.stdout
        if r.returncode != 0:
            bad.append("tool exit=%d" % r.returncode)
        if "0 finding(s)" not in out:
            bad.append("findings not zero: %s" % out.strip())
    return leg("CITEDLINES", not bad, "; ".join(bad))


def leg_census(root, lands, base, fleet_root, census_script):
    """Leg CENSUS: census validate --root <fleet-root> kotodama exits 0 at lands."""
    script = census_script or os.environ.get("KOTODAMA_CENSUS_SH") or \
        os.path.join(fleet_root, "scripts/sources-census.sh")
    args = [script, "validate", "--root", fleet_root, "kotodama"]
    r = subprocess.run(args, cwd=root, capture_output=True, text=True)
    head = git(root, "rev-parse", "HEAD").stdout.strip()
    ok = r.returncode == 0 and head == lands
    detail = "exit=%d head=%s" % (r.returncode, head[:12])
    if r.stdout.strip():
        detail += " last-line=%s" % r.stdout.strip().splitlines()[-1]
    return leg("CENSUS", ok, detail)


def leg_scratch_mirror(root, lands, base):
    """Leg SCRATCHMIRROR: receipt exists, exit 0, timestamped before append."""
    bad = []
    try:
        receipt = show(root, lands, RECEIPT)
    except Missing:
        return leg("SCRATCHMIRROR", False, "receipt missing: %s" % RECEIPT)
    if "--file" not in receipt:
        bad.append("receipt does not show census validate --file")
    if re.search(r"(?i)(?:exit|rc)\s*[=:]?\s*0", receipt) is None:
        bad.append("receipt does not show exit 0")
    if "S874" not in receipt or "S875" not in receipt:
        bad.append("receipt does not carry the two rows")
    lc = git(root, "rev-parse", lands + "^{commit}").stdout.strip()
    app = git(root, "log", "-S", "S874", "--format=%H", "-1", "--", REGISTRY)
    app_lines = [l for l in app.stdout.splitlines() if l.strip()]
    intro = git(root, "log", "--diff-filter=A", "--format=%H", "--", RECEIPT)
    intro_lines = [l for l in intro.stdout.splitlines() if l.strip()]
    if not app_lines:
        bad.append("no registry-append commit found for S874")
    elif not intro_lines:
        bad.append("receipt has no introductory commit")
    else:
        appc, introc = app_lines[0], intro_lines[-1]
        if introc == appc:
            bad.append("receipt committed in the append commit (not before)")
        else:
            anc = git(root, "merge-base", "--is-ancestor", introc, appc)
            if anc.returncode != 0:
                bad.append("receipt commit %s not before append commit %s"
                           % (introc[:12], appc[:12]))
    return leg("SCRATCHMIRROR", not bad, "; ".join(bad))


def leg_collcheck(root, lands, base):
    """Leg COLLCHECK: reg/staged id lists and an empty collisions file."""
    variants = [("reg-ids", "staged-ids", "collisions"),
                ("collcheck-reg-ids.txt", "collcheck-staged-ids.txt",
                 "collcheck-collisions.txt")]
    dirs = (ASSIM, ASSIM + "/validate", ASSIM + "/mutations")
    files = None
    for d in dirs:
        for v in variants:
            try:
                files = {f: show(root, lands, d + "/" + f) for f in v}
                break
            except Missing:
                continue
        if files:
            break
    if files is None:
        return leg("COLLCHECK", False, "mirror id files missing under %s" % ASSIM)
    reg_ids = set(TOKEN_RE.findall(files[v[0]] if False else list(files.values())[0]))
    vals = list(files.values())
    reg_ids = set(TOKEN_RE.findall(vals[0]))
    staged_ids = set(TOKEN_RE.findall(vals[1]))
    collide_ids = set(TOKEN_RE.findall(vals[2]))
    bad = []
    if not set(NEW_IDS) <= staged_ids:
        bad.append("staged-ids lacks %s" % ", ".join(set(NEW_IDS) - staged_ids))
    for sid in NEW_IDS:
        if sid in reg_ids:
            bad.append("%s present in reg-ids" % sid)
    if collide_ids:
        bad.append("collisions not empty: %s" % sorted(collide_ids))
    return leg("COLLCHECK", not bad, "; ".join(bad))


def run_legs(root, lands, base, fleet_root, census_script):
    ok = True
    ok &= leg_entries(root, lands, base)
    ok &= leg_rows(root, lands, base)
    ok &= leg_repointed(root, lands, base)
    ok &= leg_gate(root, lands, base)
    ok &= leg_rejects(root, lands, base)
    ok &= leg_ground(root, lands, base)
    ok &= leg_citedlines(root, lands, base)
    ok &= leg_census(root, lands, base, fleet_root, census_script)
    ok &= leg_scratch_mirror(root, lands, base)
    ok &= leg_collcheck(root, lands, base)
    return ok


def main(argv=None):
    ap = argparse.ArgumentParser(description="round-72 coverage counter (claim C)")
    ap.add_argument("--root", default=".", help="lane repository root")
    ap.add_argument("--lands", default=None, help="lands revision (40 hex)")
    ap.add_argument("--base", default=BASE, help="frozen base revision (default claim base)")
    ap.add_argument("--fleet-root", default=None, help="fleet root (default: lane parent)")
    ap.add_argument("--census-sh", default=None, help="census script path (override)")
    ap.add_argument("--selftest", action="store_true", help="run in-process cases")
    args = ap.parse_args(argv)

    if args.selftest:
        return run_selftest()

    if not args.lands or not re.fullmatch(r"[0-9a-f]{40}", args.lands.lower()):
        print("ERROR: --lands must be a 40-hex commit", file=sys.stderr)
        return 2
    lands = args.lands.lower()
    base = args.base.lower()
    root = args.root if os.path.isabs(args.root) else os.path.join(LANE, args.root)
    if not os.path.isdir(os.path.join(root, ".git")):
        print("ERROR: not a git repository: %s" % root, file=sys.stderr)
        return 2
    fleet_root = args.fleet_root or os.path.dirname(os.path.abspath(root))

    ok = run_legs(root, lands, base, fleet_root, args.census_sh)
    print("ACCEPT-C-72: %s legs=10/10" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


# --------------------------------------------------------------------------
# selftest
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
| S001 | Selftest one — https://example.com/one | docs | A | s | a | teaches one | mined | 2026-10-19 | 90d | corpus/knowledge/culture-material/some.md |
| S873 | Selftest two — https://example.com/two | docs | B | s | a | teaches two | queued | 2026-10-25 | 180d | — |
"""

ROWS_APPEND = """\
| S874 | 中国非物质文化遗产网 · 中国非物质文化遗产数字博物馆（文化和旅游部主管）,「国家级非物质文化遗产代表性项目名录」清单页 — https://www.ihchina.cn/project.html ; https://web.archive.org/web/20200216023423id_/http://www.ihchina.cn/project.html | dataset | A | Tier A for the PRC state's ten-category taxonomy | 清单页「国家级名录将非物质文化遗产分为十大门类…」段 | A state-grade material-culture category model | mined | 2026-10-25 | 180d | corpus/knowledge/culture-material/heritage-taxonomy-models.md, corpus/knowledge/culture-material/heritage-taxonomy-models.amend-2026-10-24-r13.md |
| S875 | 文化遺産データベース（文化庁）, 文化財検索 — https://online.bunka.go.jp/db/heritages/search | dataset | A | Tier A for the Japanese state's official cultural-property classification | 詳細検索フォーム「時代」選択肢 + 「分野」選択肢 | An official period vocabulary | mined | 2026-10-25 | 90d | corpus/knowledge/culture-material/heritage-taxonomy-models.md |
"""

ENTRY_CANONICAL = """\
# Heritage taxonomies — how states classify their own intangible and material culture

- source: S874 — https://www.ihchina.cn/project.html — 清单页「国家级名录将非物质文化遗产分为十大门类…」段 — fetched 2026-10-25
- source: S875 — https://online.bunka.go.jp/db/heritages/search — 詳細検索フォーム「時代」選択肢 + 「分野」選択肢 — fetched 2026-10-25
- verified-at: 2026-10-25
- recheck: 180d — re-run the two row recheck commands (ran 2026-10-25)
- ground: the wave brief's scoped domain, which the lane served from no state-published classification of its own; and the header-conformance gap.
- topic: the two states' official category models for material and intangible culture, read as design systems.
- gap filled: `grep -inE 'ihchina|非物质|非物質|文化遺産|heritage online|bunka'` over the 797-row registry returns 0 — the lane holds no state heritage taxonomy at all.
- sources: the two rows above; both are official state catalogues, opened this round, each with a located quote.
- couples: `culture-material/material-culture-inference-method.md`; `culture-material/era-periodization-models.md`.
- scope: a reference method for the culture-material partition. It describes real classification schemes so a worldbuilder can build an invented culture's craft and ritual taxonomy; it decides no world's canon.

## Proposed body

1. A state-grade category model: the PRC's ten 门类 and the Roman-numeral category code (S874).
2. A state-grade domain taxonomy: Japan's 分野 tree with its 時代 period ladder (S875).
3. The useful distinction: the category system is a stable object, while the inventory grows by dated batches.
"""

ENTRY_AMEND = """\
# Amendment — a state heritage taxonomy that is versioned

- source: S874 — https://web.archive.org/web/20200216023423id_/http://www.ihchina.cn/project.html — the Internet Archive's capture of the register's 清单页 — fetched 2026-10-25
- verified-at: 2026-10-25
- recheck: 180d — re-run the capture recheck command (ran 2026-10-25)
- ground: the register page was held to be unreachable, and its Archive coverage was believed to be nil.
- topic: what a state's own heritage-category list does over time, and how it should be cited.
- gap filled: the register was opened only once; this round opens the 2020 capture and compares it with the live page.
- sources: the row above — the Archive's 2020 capture of the ministry's own 清单页.
- couples: `culture-material/heritage-taxonomy-models.md`.
- scope: an amendment to the heritage-taxonomy entry. It adds the register's dated states and the capture as a reachable stand-in.

## Proposed body (dated addition)

- From the 2020 capture (S874): the register's category rule is word-for-word the same as on the live page; only the batch count has grown.
"""

LESSON_GATE = """\
# Round 72 — selftest lesson

## Gate

| source | access date | quote (≤25 words) | grounds | verdict |
|---|---|---|---|---|
| S874 — ihchina register 清单页 — https://www.ihchina.cn/project.html | 2026-10-25 | "国家级名录将非物质文化遗产分为十大门类" | capture 2020-02-16; live page | admitted |
| S875 — bunka 文化財検索 — https://online.bunka.go.jp/db/heritages/search | 2026-10-25 | "時代 選択肢（旧石器…令和）" | page as served 2026-10-25 | admitted |

Assimilation rejects:

| staged entry | staged rows | reason | flip | verdict |
|---|---|---|---|---|
| narrative-structure-frameworks.md | S870 | quoted span absent; cites quarantine-REFUSED staged S870 | reopen the register page | rejected |
| worldbuilding-setting-practice.amend-2026-10-23.md | S899/S900 | cites quarantine-REFUSED staged S899/S900 (registers S816/S817) | reopen both registers | rejected |

## Mistakes

| class | evidence | captured-by | fix | state |
|---|---|---|---|---|
| fixture | selftest only | n/a | n/a | new |
"""

RECEIPT_TEXT = """\
# round-72 scratch-mirror validation receipt (selftest fixture)
# stamp: 2026-10-25 10:00:00 UTC
gap-sweep re-run at the 797-row registry: ihchina-rows: 0 ; bunka-rows: 0
census validate --file /tmp/r72-mirror/corpus/SOURCES.md
exit 0
rows present in mirror: S874 S875
"""

MUTANTS = {
    "drop_entry": {"drop_entry": True},
    "repoint": {"repoint": True},
    "rows": {"rows": True},
    "gate_quote": {"gate_quote": True},
    "no_rejects": {"no_rejects": True},
    "ground_zeros": {"ground_zeros": True},
    "receipt_no_exit": {"receipt_no_exit": True},
    "collisions": {"collisions": True},
    "multi_id_line": {"multi_id_line": True},
    "head_ahead": {"head_ahead": True},
}

EXPECTED_FAIL = {
    "drop_entry": "ENTRIES",
    "repoint": "REPOINTED",
    "rows": "ROWS",
    "gate_quote": "GATE",
    "no_rejects": "GATE",
    "ground_zeros": "GROUND",
    "receipt_no_exit": "SCRATCHMIRROR",
    "collisions": "COLLCHECK",
    "multi_id_line": "CITEDLINES",
    "head_ahead": "CENSUS",
}


def build_fixture(prefix, mut=None):
    mut = mut or {}
    lane = tempfile.mkdtemp(prefix=prefix + "-", suffix="-lane")
    fleet = os.path.dirname(lane)
    r = gitq(lane, "init", "-q")
    if r.returncode != 0:
        raise RuntimeError("git init failed")
    git_write(lane, "corpus/SOURCES.md", BASE_REGISTRY)
    git_commit(lane, "base")
    base = gitq(lane, "rev-parse", "HEAD").stdout.strip()

    receipt = RECEIPT_TEXT
    if mut.get("receipt_no_exit"):
        receipt = receipt.replace("exit 0", "exit 1")
    if mut.get("ground_zeros"):
        receipt = receipt.replace(
            "gap-sweep re-run at the 797-row registry: ihchina-rows: 0 ; bunka-rows: 0\n",
            "")
    git_write(lane, RECEIPT, receipt)
    git_write(lane, ASSIM + "/reg-ids", "S001\nS873\n")
    git_write(lane, ASSIM + "/staged-ids", "S873\nS874\nS875\nS976\n")
    collisions = "" if not mut.get("collisions") else "S874\n"
    git_write(lane, ASSIM + "/collisions", collisions)
    git_commit(lane, "mirror receipt + id lists")

    registry = BASE_REGISTRY + "\n" + ROWS_APPEND
    if mut.get("repoint"):
        registry = registry.replace("https://www.ihchina.cn/project.html ; ",
                                    "https://other.example/x ; ")
    if mut.get("rows"):
        registry = registry.replace(
            "mined | 2026-10-25 | 90d | corpus/knowledge/culture-material/heritage-taxonomy-models.md |",
            "mined | 2026-10-25 | 90d | — |")
    git_write(lane, "corpus/SOURCES.md", registry)

    canonical = ENTRY_CANONICAL
    if mut.get("multi_id_line"):
        canonical = canonical.replace(
            "1. A state-grade category model: the PRC's ten 门类 and the Roman-numeral category code (S874).",
            "1. A state-grade category model: the PRC's ten 门类 and the Roman-numeral category code (S874) (S875).")
    git_write(lane, ENTRIES[0], canonical)
    if not mut.get("drop_entry"):
        git_write(lane, ENTRIES[1], ENTRY_AMEND)

    lesson = LESSON_GATE
    if mut.get("gate_quote"):
        lesson = lesson.replace(
            '"国家级名录将非物质文化遗产分为十大门类"',
            '"a b c d e f g h i j k l m n o p q r s t u v w x y z aa bb cc"')
    if mut.get("no_rejects"):
        lesson = lesson.split("Assimilation rejects:")[0] + "## Mistakes\n"
    git_write(lane, LESSON, lesson)

    git_commit(lane, "lands: entries, rows, lesson")
    lands = gitq(lane, "rev-parse", "HEAD").stdout.strip()
    if mut.get("head_ahead"):
        git_write(lane, "corpus/QUALITY.md", "# extra\n")
        git_commit(lane, "post-lands noise")
    else:
        gitq(lane, "checkout", "-q", "--detach", lands)
    tools_dir = os.path.join(lane, "tools")
    os.makedirs(tools_dir, exist_ok=True)
    shutil.copy(os.path.join(LANE, "tools/check-cited-lines.py"),
                os.path.join(tools_dir, "check-cited-lines.py"))
    stub = os.path.join(fleet, "sources-census-stub.sh")
    with open(stub, "w", encoding="utf-8") as fh:
        fh.write("#!/bin/sh\nprintf 'kotodama\\tok\\tstub\\n'\nexit 0\n")
    os.chmod(stub, 0o755)
    return lane, base, lands, stub


def run_selftest():
    failures = []
    # Clean fixture must pass 10/10.
    lane, base, lands, stub = build_fixture("r72st-clean")
    r = subprocess.run([sys.executable, "-B", os.path.abspath(__file__),
                        "--root", lane, "--lands", lands, "--base", base,
                        "--census-sh", stub],
                       capture_output=True, text=True)
    out = r.stdout
    if "ACCEPT-C-72: PASS legs=10/10" not in out:
        failures.append("clean fixture: expected PASS 10/10, got exit=%d\n%s\n%s"
                        % (r.returncode, out, r.stderr))
    # Each mutant must FAIL and specifically fail its mapped leg.
    for name, mut in MUTANTS.items():
        lane, base, lands, stub = build_fixture("r72st-" + name, mut)
        r = subprocess.run([sys.executable, "-B", os.path.abspath(__file__),
                            "--root", lane, "--lands", lands, "--base", base,
                            "--census-sh", stub],
                           capture_output=True, text=True)
        out = r.stdout
        wanted = EXPECTED_FAIL[name]
        if "ACCEPT-C-72: FAIL" not in out:
            failures.append("%s: expected final FAIL, got exit=%d\n%s" % (name, r.returncode, out))
        elif "LEG FAIL %s" % wanted not in out:
            failures.append("%s: expected leg FAIL %s\n%s" % (name, wanted, out))
    total = 1 + len(MUTANTS)
    passed = total - len(failures)
    print("SELFTEST: %d/%d" % (passed, total))
    for f in failures:
        print("---", f)
    return 0 if passed == total else 1


if __name__ == "__main__":
    sys.exit(main())
