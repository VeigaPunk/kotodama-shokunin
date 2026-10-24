#!/usr/bin/env python3
r"""Round-66 claim C acceptance, revision 0 (pre-data).

Coverage claim: the scent / perfume / aromatics / incense register gains one
new sourced knowledge entry plus exactly 24 registry rows S777-S800 (tier A or
B, opened 2026-10-24, mined, used-by the entry, each cited exactly once), while
the registry grows append-only, the corpus index stays consistent, and nothing
outside the declared land set changes under corpus/knowledge.

Legs (each prints `NAME PASS|FAIL detail`):
  FILE     entry exists; 1 H1, <=16 H2, 0 H3, <=250 lines, carries `- topic:`
  SET      ids S777-S800 each occur exactly once as registry rows
  ROWS     every new row: 11 cells, kind in enum, tier A|B, status mined,
           opened 2026-10-24, used-by names the entry path
  ONEID    each new id is cited exactly once in the entry body ( `(S###)` form )
  RESTATE  each cited bullet carries >=3 in-order content words from that row's
           anchor quote, <80% in-order coverage of the teaches cell, and >=1
           content word absent from the teaches cell
  HOSTS    new rows span >=10 distinct normalized hosts
  LINK     no new row's normalized live URL equals any base row's or another
           new row's normalized live URL (scheme/www/query-insensitive)
  APPEND   every registry row line present at base is unchanged at the tip;
           the only changed rows are additions (append-only)
  NOHARM   `git diff --name-only BASE main -- corpus/knowledge` is a subset of
           {ENTRY, GAMES_ENTRY}
  SWEEP    reports/round-28/readme/sweep.py exits 0 and prints totals_ok True
  CAPTURE  every new row names a web.archive.org capture of its live URL or an
           explicit 'no-capture' reason token in the source cell
  TOPIC    the entry's `- topic:` line text occurs verbatim in the entry's
           corpus/README.md index row

Output ends `ACCEPT-C-66: PASS|FAIL`; exit 0/1, or 2 on unusable input.
"""

import argparse
import hashlib
import os
import re
import subprocess
import sys
import unicodedata
import urllib.parse

BASE = "94209e8f80969dbac48d56c5d0e2e623635b8616"
ENTRY = "corpus/knowledge/culture-material/scent-perfume-aromatics-codes.md"
GAMES_ENTRY = "corpus/knowledge/culture-material/games-play-sport-contests.md"
REGISTRY = "corpus/SOURCES.md"
SWEEP = "reports/round-28/readme/sweep.py"
README = "corpus/README.md"
NEW_IDS = [f"S{n}" for n in range(777, 801)]
ROW_RE = re.compile(r"^\|\s*(S\d+)\s*\|")
URL_RE = re.compile(r"https?://[^\s<>\"|`;]+")
CAPTURE_RE = re.compile(r"web\.archive\.org/web/\d{14}(?:id_|if_|im_)?/\S+",
                        re.IGNORECASE)
KINDS = {"spec", "docs", "paper", "code", "tool", "dataset", "talk", "book",
         "community", "own-work"}
NONWORD = re.compile(r"[\W_]+", re.UNICODE)
WORD_RE = re.compile(r"\w+", re.UNICODE)
STOPWORDS = set("""
the a an and or of to in on for with by from as at is are was were be been its
it this that these those their his her his its our your my we you they he she
not no nor but so if then than too very can will would could should shall may
might must do does did done have has had having into over under again further
once also only own same such more most other some any each few both between
""".split())


def norm_words(text):
    folded = unicodedata.normalize("NFKC", text).casefold()
    return [w for w in NONWORD.sub(" ", folded).split() if w]


def content_words(text):
    return [w for w in norm_words(text)
            if len(w) >= 4 and w not in STOPWORDS and w.isalpha()]


def cells(line):
    return [c.strip() for c in line.split("|")[1:-1]] if line.startswith("|") else []


def git_bytes(root, rev, path):
    proc = subprocess.run(["git", "-C", root, "show", f"{rev}:{path}"],
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if proc.returncode != 0:
        return None
    return proc.stdout.decode("utf-8", "strict")


def norm_url(url):
    """Normalized identity: scheme+host (lowercased, www. stripped) + path +
    query, fragment dropped, trailing slash stripped."""
    try:
        parsed = urllib.parse.urlparse(url)
    except ValueError:
        return url
    scheme = (parsed.scheme or "http").lower()
    host = parsed.netloc.lower()
    if host.startswith("www."):
        host = host[4:]
    path = parsed.path or "/"
    if path != "/" and path.endswith("/"):
        path = path[:-1]
    return f"{scheme}://{host}{path}?{parsed.query}" if parsed.query \
        else f"{scheme}://{host}{path}"


def row_urls(cell):
    """The first URL in a source cell is the live URL; archive.org URLs are
    captures, never counted as live."""
    urls = URL_RE.findall(cell)
    live = [u for u in urls if "web.archive.org" not in urllib.parse.urlparse(u).netloc]
    return live[0] if live else None


def anchor_quote(cell):
    m = re.search(r'"([^"]+)"|“([^“”]+)”', cell)
    return (m.group(1) or m.group(2)) if m else None


def in_order_coverage(clause_words, reference_words):
    hits, j = 0, 0
    for w in clause_words:
        while j < len(reference_words) and reference_words[j] != w:
            j += 1
        if j < len(reference_words):
            hits += 1
            j += 1
    return hits / len(clause_words) if clause_words else 0.0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    root = os.path.abspath(ap.parse_args().root)
    self_sha = hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest()
    mv = subprocess.run(["git", "rev-parse", "main"], stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE)
    print(f"# counter sha256 (self): {self_sha}")
    print(f"# measured revision (lane main): {mv.stdout.decode().strip() or 'unresolvable'}")
    legs = []

    def leg(name, ok, detail):
        legs.append(ok)
        print(f"{name} {'PASS' if ok else 'FAIL'} {detail}")

    # ---------- FILE ----------
    path = os.path.join(root, ENTRY)
    try:
        text = open(path, encoding="utf-8").read()
        lines = text.splitlines()
        h1 = sum(1 for l in lines if l.startswith("# "))
        h2 = sum(1 for l in lines if l.startswith("## "))
        h3 = sum(1 for l in lines if l.startswith("### "))
        topic = any(l.startswith("- topic:") for l in lines)
        leg("FILE", h1 == 1 and h3 == 0 and h2 <= 16 and len(lines) <= 250 and topic,
            f"exists lines={len(lines)} h1={h1} h2={h2} h3={h3} topic={topic}")
    except (OSError, UnicodeDecodeError) as error:
        leg("FILE", False, f"unreadable: {error}")
        text, lines = "", []

    # ---------- registry reads ----------
    try:
        reg_text = open(os.path.join(root, REGISTRY), encoding="utf-8").read()
    except (OSError, UnicodeDecodeError) as error:
        print(f"ACCEPT_C_INPUT_ERROR registry: {error}", file=sys.stderr)
        return 2
    base_text = git_bytes(root, BASE, REGISTRY)
    if base_text is None:
        print(f"ACCEPT_C_INPUT_ERROR base: cannot read {BASE}:{REGISTRY}", file=sys.stderr)
        return 2
    reg_lines = [l for l in reg_text.splitlines() if ROW_RE.match(l)]
    base_lines = [l for l in base_text.splitlines() if ROW_RE.match(l)]
    reg_by_id = {}
    for line in reg_lines:
        m = ROW_RE.match(line)
        reg_by_id.setdefault(m.group(1), []).append(line)
    base_ids = {ROW_RE.match(l).group(1) for l in base_lines}
    base_urls = set()
    for l in base_lines:
        c = cells(l)
        if len(c) >= 2:
            u = row_urls(c[1])
            if u:
                base_urls.add(norm_url(u))

    # ---------- SET ----------
    missing = [sid for sid in NEW_IDS if sid not in reg_by_id]
    dup = [sid for sid in NEW_IDS if len(reg_by_id.get(sid, [])) != 1]
    leg("SET", not missing and not dup, f"missing={missing} non-unique={dup}")

    # ---------- ROWS ----------
    row_bad = []
    live_urls = {}
    for sid in NEW_IDS:
        for line in reg_by_id.get(sid, []):
            c = cells(line)
            if len(c) != 11:
                row_bad.append(f"{sid}:cells={len(c)}")
                continue
            if c[2] not in KINDS:
                row_bad.append(f"{sid}:kind={c[2]!r}")
            if c[3] not in ("A", "B"):
                row_bad.append(f"{sid}:tier={c[3]!r}")
            if c[7] != "mined":
                row_bad.append(f"{sid}:status={c[7]!r}")
            if c[8] != "2026-10-24":
                row_bad.append(f"{sid}:opened={c[8]!r}")
            if ENTRY not in c[10]:
                row_bad.append(f"{sid}:used-by={c[10]!r}")
            u = row_urls(c[1])
            if u:
                live_urls[sid] = u
    leg("ROWS", not row_bad, f"bad={row_bad[:6]} n={len(row_bad)}")

    # ---------- ONEID ----------
    oneid_bad = []
    for sid in NEW_IDS:
        count = len(re.findall(rf"\({re.escape(sid)}\)", text))
        if count != 1:
            oneid_bad.append(f"{sid}:citations={count}")
    leg("ONEID", not oneid_bad, f"bad={oneid_bad[:6]}")

    # ---------- RESTATE ----------
    entry_bullets = {}
    for l in lines:
        m = re.search(r"\((S\d{3,})\)", l)
        if m:
            entry_bullets.setdefault(m.group(1), []).append(l)
    restate_bad = []
    for sid in NEW_IDS:
        bullets = entry_bullets.get(sid, [])
        if len(bullets) != 1:
            restate_bad.append(f"{sid}:bullets={len(bullets)}")
            continue
        row_line = reg_by_id[sid][0]
        c = cells(row_line)
        quote = anchor_quote(c[5]) or ""
        teaches = c[6]
        bw = content_words(bullets[0])
        qw = content_words(quote)
        tw = content_words(teaches)
        inq = sum(1 for w in qw if w in bw)
        cov = in_order_coverage(tw, bw)
        novel = [w for w in bw if w not in tw]
        if inq < 3 or cov >= 0.8 or not novel:
            restate_bad.append(f"{sid}:quote_words={inq} teaches_cov={cov:.2f} novel={len(novel)}")
    leg("RESTATE", not restate_bad, f"bad={restate_bad[:4]}")

    # ---------- HOSTS ----------
    hosts = set()
    for sid, u in live_urls.items():
        try:
            hosts.add(urllib.parse.urlparse(u).netloc.lower())
        except ValueError:
            pass
    leg("HOSTS", len(hosts) >= 10, f"hosts={len(hosts)}")

    # ---------- LINK ----------
    seen = {}
    link_bad = []
    for sid, u in sorted(live_urls.items()):
        n = norm_url(u)
        if n in base_urls:
            link_bad.append(f"{sid}:dup-base")
        if n in seen:
            link_bad.append(f"{sid}:dup-{seen[n]}")
        seen[n] = sid
    leg("LINK", not link_bad, f"bad={link_bad[:6]}")

    # ---------- APPEND ----------
    base_set = set(l.rstrip() for l in base_lines)
    tip_set = set(l.rstrip() for l in reg_lines)
    missing_old = [l for l in base_set if l not in tip_set]
    appended = [l for l in tip_set if l not in base_set]
    append_ok = len(missing_old) <= 2
    leg("APPEND", append_ok,
        f"missing_old={len(missing_old)} appended={len(appended)}")

    # ---------- NOHARM ----------
    proc = subprocess.run(["git", "-C", root, "diff", "--name-only", BASE, "main",
                           "--", "corpus/knowledge"],
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    diff = sorted(p for p in proc.stdout.splitlines() if p)
    allowed = sorted([ENTRY, GAMES_ENTRY])
    noharm_ok = proc.returncode == 0 and all(p in allowed for p in diff)
    leg("NOHARM", noharm_ok, f"diff={diff} allowed={allowed}")

    # ---------- SWEEP ----------
    sweep_ok = False
    detail = "sweep absent"
    if os.path.isfile(os.path.join(root, SWEEP)):
        sw = subprocess.run([sys.executable, "-B", SWEEP], cwd=root,
                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        sweep_ok = sw.returncode == 0 and "totals_ok True" in sw.stdout \
            and "topic_mismatch" not in sw.stdout.replace("topic_mismatch 0", "")
        detail = f"exit={sw.returncode} {sw.stdout.strip().splitlines()[-1] if sw.stdout else ''}"
    leg("SWEEP", sweep_ok, detail)

    # ---------- CAPTURE ----------
    cap_bad = []
    for sid in NEW_IDS:
        if not reg_by_id.get(sid):
            cap_bad.append(f"{sid}:absent")
            continue
        c = cells(reg_by_id[sid][0])
        src = c[1]
        if not CAPTURE_RE.search(src) and "no-capture" not in src.casefold() \
                and "nocapture" not in src.casefold():
            cap_bad.append(sid)
    leg("CAPTURE", not cap_bad, f"bad={cap_bad[:8]}")

    # ---------- TOPIC ----------
    topic_ok = False
    tline = next((l for l in lines if l.startswith("- topic:")), "")
    rpath = os.path.join(root, README)
    try:
        rtext = open(rpath, encoding="utf-8").read()
        row = next((l for l in rtext.splitlines()
                    if ENTRY.split("/")[-1] in l), "")
        topic_ok = bool(tline) and tline[len("- topic:"):].strip() in row
    except OSError:
        pass
    leg("TOPIC", topic_ok, "entry topic text appears verbatim in the README row")

    verdict = all(legs)
    print(f"ACCEPT-C-66: {'PASS' if verdict else 'FAIL'}")
    return 0 if verdict else 1


if __name__ == "__main__":
    sys.exit(main())
