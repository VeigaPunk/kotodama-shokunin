#!/usr/bin/env python3
r"""Round-67 claim C acceptance, revision 0 (pre-data).

Coverage claim: the medicine / healing / physician / remedy register is
unowned in corpus/knowledge (0 filename owners under the word-bounded census;
topic-line sweep finds only partial-scope mentions, not whole-register
owners) -> one new culture-material entry
corpus/knowledge/culture-material/medicine-healing-codes.md supported by
exactly 24 registry rows S805-S828 opened this round (2026-10-24), each tier
A or B, mined, used-by the entry, cited exactly once by it; the registry
grows append-only (plus the declared r66 disposition additions S801-S804 and
the S753 used-by cell repair), the corpus index stays consistent, and nothing
outside the declared land set changes under corpus/knowledge.

Receipt discipline (QUALITY.md criterion 19, the r66 sequencing fix):
--lands <40hex> is REQUIRED and names the lands revision the run claims to
measure. The counter reads the stamped revision from --lands and the
evaluated revision from `git rev-parse main` of --root; the receipt records
BOTH, and leg STAMP fails unless they are equal. The evaluation protocol is:
materialize the lands tree (`git clone --no-local` of the lane at the lands
commit) and run `--root <clone> --lands <lands>` — a clone whose main moved
past lands, or a stale clone, makes evaluated != stamped and STAMP fails.
Carrier-parentage is a post-records check (check-receipt-seq.py --topo),
never a lands-time leg.

Legs (each prints `NAME PASS|FAIL detail`):
  STAMP    `git rev-parse main` == --lands (evaluated == stamped)
  FILE     entry exists; 1 H1, <=16 H2, 0 H3, <=250 lines, carries '- topic:'
  SET      ids S805-S828 each occur exactly once as registry rows
  ROWS     every new row: 11 cells, kind in enum, tier A|B, status mined,
           opened 2026-10-24, used-by names the entry path
  ONEID    each new id is cited exactly once in the entry body ( `(S###)` )
  RESTATE  each cited bullet carries >=3 in-order content words from that row's
           anchor quote, <80% in-order coverage of the teaches cell, and >=1
           content word absent from the teaches cell
  HOSTS    new rows span >=10 distinct normalized hosts
  LINK     no new row's normalized live URL equals any base row's or another
           new row's normalized live URL (query-aware)
  APPEND   every registry row line present at base is unchanged at the tip
           except the declared S753 used-by cell flip; the added set is
           bounded to NEW_IDS + the declared disposition ids S801-S804
  NOHARM   `git diff --name-status BASE -- corpus/knowledge` is a subset of
           {ENTRY} (the r66 games re-point landed in the base revision)
  SWEEP    reports/round-28/readme/sweep.py exits 0 and prints totals_ok True
  CAPTURE  every new row names a web.archive.org capture of its live URL or an
           explicit 'no-capture' reason token in the source cell
  TOPIC    the entry's `- topic:` line text occurs verbatim in the entry's
           corpus/README.md index row

Output ends `ACCEPT-C-67: PASS|FAIL`; exit 0/1, or 2 on unusable input.
"""

import argparse
import hashlib
import os
import re
import subprocess
import sys
import unicodedata
import urllib.parse

BASE = "ad5b52b0ab5691358cd38718ab75649dc9916f9a"
ENTRY = "corpus/knowledge/culture-material/medicine-healing-codes.md"
REGISTRY = "corpus/SOURCES.md"
SWEEP = "reports/round-28/readme/sweep.py"
README = "corpus/README.md"
NEW_IDS = [f"S{n}" for n in range(805, 829)]
# Declared extra additions this round (r66 dispositions): rejected rows
# carrying the r66 frontier ids S801-S804.
EXTRA_IDS = {"S801", "S802", "S803", "S804"}
# Declared in-place cell flip (r66 dispositions): S753 used-by '-' -> '—'.
ALLOWED_FLIP = {"S753"}
ROW_RE = re.compile(r"^\|\s*(S\d+)\s*\|")
URL_RE = re.compile(r"https?://[^\s<>\"|`;]+")
CAPTURE_RE = re.compile(r"web\.archive\.org/web/\d{14}(?:id_|if_|im_)?/\S+",
                        re.IGNORECASE)
KINDS = {"spec", "docs", "paper", "code", "tool", "dataset", "talk", "book",
         "community", "own-work"}
NONWORD = re.compile(r"[\W_]+", re.UNICODE)
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


def norm_url_q(url):
    """Same-page identity including query: host + path + percent-decoded
    query. Scheme is dropped; percent-encoding variants are one page."""
    try:
        parsed = urllib.parse.urlparse(url)
    except ValueError:
        return url
    host = parsed.netloc.lower()
    if host.startswith("www."):
        host = host[4:]
    path = parsed.path or "/"
    if path != "/" and path.endswith("/"):
        path = path[:-1]
    query = urllib.parse.unquote(parsed.query)
    return f"{host}{path}?{query}" if query else f"{host}{path}"


def ordered_hits(needle_words, haystack_words):
    hits, j = 0, 0
    for w in needle_words:
        k = j
        while k < len(haystack_words) and haystack_words[k] != w:
            k += 1
        if k < len(haystack_words):
            hits += 1
            j = k + 1
    return hits


def row_urls(cell):
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


def _run():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--lands", required=True,
                    help="the lands revision this run claims to measure")
    args = ap.parse_args()
    root = os.path.abspath(args.root)
    lands = args.lands
    self_sha = hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest()
    if not re.fullmatch(r"[0-9a-f]{40}", lands or ""):
        print("STAMP FAIL --lands is not a full commit hash")
        print("ACCEPT-C-67: FAIL")
        return 2
    mv = subprocess.run(["git", "-C", root, "rev-parse", "main"], stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE)
    mv_rev = mv.stdout.decode().strip()
    tree_p = subprocess.run(["git", "-C", root, "rev-parse", f"{lands}^{{tree}}"],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    tree_rev = tree_p.stdout.decode().strip()
    dirty = subprocess.run(["git", "-C", root, "status", "--porcelain",
                            "--untracked-files=no"],
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    dirty_flag = bool(dirty.stdout.decode().strip())
    print(f"# counter sha256 (self): {self_sha}")
    print(f"# stamped revision: {lands}")
    print(f"# evaluated revision: {mv_rev or 'unresolvable'}")
    print(f"# measured revision (lane main): {mv_rev or 'unresolvable'}")
    print(f"# tree: {tree_rev or 'unresolvable'}")
    print(f"# worktree dirty (tracked): {dirty_flag}")
    legs = []

    def leg(name, ok, detail):
        legs.append(bool(ok))
        print(f"{name} {'PASS' if ok else 'FAIL'} {detail}")

    # ---------- STAMP ----------
    # evaluated == stamped: a stale clone or a worktree moved past lands fails
    # here; nothing downstream can rescue a moved evaluation.
    stamp_ok = bool(re.fullmatch(r"[0-9a-f]{40}", mv_rev)) \
        and mv_rev == lands and bool(re.fullmatch(r"[0-9a-f]{40}", tree_rev))
    leg("STAMP", stamp_ok,
        f"stamped={lands[:8]} evaluated={mv_rev[:8]} "
        f"equal={mv_rev == lands} tree={tree_rev[:8]} "
        f"dirty_tracked={dirty_flag}")
    if not stamp_ok:
        print("ACCEPT-C-67: FAIL")
        return 1

    # ---------- FILE ----------
    path = os.path.join(root, ENTRY)
    try:
        text = open(path, encoding="utf-8").read()
        lines = text.splitlines()
        h1 = sum(1 for l in lines if l.startswith("# "))
        h2 = sum(1 for l in lines if l.startswith("## "))
        h3 = sum(1 for l in lines if l.startswith("### "))
        tline0 = next((l for l in lines if l.startswith("- topic:")), "")
        topic = bool(tline0) and bool(tline0[len("- topic:"):].strip())
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
    base_urls_q = set()
    for l in base_lines:
        c = cells(l)
        if len(c) >= 2:
            u = row_urls(c[1])
            if u:
                base_urls_q.add(norm_url_q(u))
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
            if c[3] not in ("A", "B", "C"):
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
            else:
                row_bad.append(f"{sid}:no_live_url")
    leg("ROWS", not row_bad, f"bad={row_bad[:6]} n={len(row_bad)}")

    # ---------- ONEID ----------
    oneid_bad = []
    cited = re.findall(r"\((S\d{3,})\)", text)
    for sid in NEW_IDS:
        count = cited.count(sid)
        if count != 1:
            oneid_bad.append(f"{sid}:citations={count}")
    foreign = sorted({s for s in cited if s not in NEW_IDS})
    for sid in foreign:
        oneid_bad.append(f"{sid}:out_of_claim_set")
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
        inq = ordered_hits(qw, bw)
        cov = in_order_coverage(tw, bw)
        novel = [w for w in bw if w not in tw]
        if inq < 3 or cov >= 0.8 or not novel:
            restate_bad.append(f"{sid}:quote_words={inq} teaches_cov={cov:.2f} novel={len(novel)}")
        if len(tw) < 4:
            restate_bad.append(f"{sid}:teaches_thin")
        else:
            q_cov = in_order_coverage(qw, tw)
            if q_cov >= 0.8:
                restate_bad.append(f"{sid}:teaches_echoes_quote={q_cov:.2f}")
    leg("RESTATE", not restate_bad, f"bad={restate_bad[:4]}")

    # ---------- HOSTS ----------
    hosts = set()
    for sid, u in live_urls.items():
        try:
            host = urllib.parse.urlparse(u).netloc.lower()
            if host.startswith("www."):
                host = host[4:]
            if host:
                hosts.add(host)
        except ValueError:
            pass
    leg("HOSTS", len(hosts) >= 10, f"hosts={len(hosts)}")

    # ---------- LINK ----------
    seen = {}
    link_bad = []
    for sid, u in sorted(live_urls.items()):
        n = norm_url_q(u)
        if n in base_urls_q:
            link_bad.append(f"{sid}:dup-base")
        if n in seen:
            link_bad.append(f"{sid}:dup-{seen[n]}")
        seen[n] = sid
    leg("LINK", not link_bad, f"bad={link_bad[:6]}")

    # ---------- APPEND ----------
    # Status/recheck/used-by cells are mutable in place; every other base row
    # byte must survive, the added set is bounded to NEW_IDS + EXTRA_IDS, and
    # the only allowed in-place flip is S753's used-by cell.
    base_set = {ROW_RE.match(l).group(1): l.rstrip() for l in base_lines}
    tip_set = {ROW_RE.match(l).group(1): l.rstrip() for l in reg_lines}
    missing_old = [sid for sid in base_set if sid not in tip_set]
    appended_ids = sorted(sid for sid in tip_set if sid not in base_set)
    allowed_new = set(NEW_IDS) | EXTRA_IDS
    extra_ids = [sid for sid in appended_ids if sid not in allowed_new]
    mutable_bad = []
    for sid, old_line in base_set.items():
        new_line = tip_set.get(sid)
        if new_line is None or new_line == old_line:
            continue
        oc, nc = cells(old_line), cells(new_line)
        if sid in ALLOWED_FLIP and len(oc) == 11 and len(nc) == 11 \
                and oc[:10] == nc[:10] and oc[10] != nc[10]:
            continue  # declared S753 used-by cell flip only
        if len(oc) == 11 and len(nc) == 11 \
                and oc[:7] == nc[:7] and oc[8] == nc[8]:
            continue  # status/recheck/used-by cell flips allowed
        mutable_bad.append(sid)
    append_ok = not missing_old and not extra_ids and not mutable_bad
    leg("APPEND", append_ok,
        f"missing_old={missing_old} appended={len(appended_ids)} "
        f"extra={extra_ids[:6]} immutable_violations={mutable_bad[:6]}")

    # ---------- NOHARM ----------
    proc = subprocess.run(["git", "-C", root, "diff", "--name-status", BASE,
                           "--", "corpus/knowledge"],
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    diff = sorted(set(p.split("\t")[-1] for p in proc.stdout.splitlines() if p))
    allowed = sorted([ENTRY])
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
        live = live_urls.get(sid)
        if not live:
            cap_bad.append(f"{sid}:no_live_url")
            continue
        cap_m = CAPTURE_RE.search(src)
        if not cap_m:
            cap_bad.append(f"{sid}:no_capture")
            continue
        cap_orig = re.sub(r"^web\.archive\.org/web/\d{14}(?:id_|if_|im_)?/",
                          "", cap_m.group(0))
        if norm_url_q(cap_orig) != norm_url_q(live):
            cap_bad.append(f"{sid}:capture_target_mismatch")
    leg("CAPTURE", not cap_bad, f"bad={cap_bad[:8]}")

    # ---------- TOPIC ----------
    topic_ok = False
    tline = next((l for l in lines if l.startswith("- topic:")), "")
    rpath = os.path.join(root, README)
    try:
        rtext = open(rpath, encoding="utf-8").read()
        fname = ENTRY.split("/")[-1]
        row = next((l for l in rtext.splitlines()
                    if l.startswith("- ") and fname in l), "")
        topic_ok = bool(tline) and tline[len("- topic:"):].strip() in row
    except OSError:
        pass
    leg("TOPIC", topic_ok, "entry topic text appears verbatim in the README row")

    verdict = all(legs)
    print(f"ACCEPT-C-67: {'PASS' if verdict else 'FAIL'}")
    return 0 if verdict else 1


def main():
    try:
        return _run()
    except (RuntimeError, OSError, subprocess.SubprocessError, ValueError,
            KeyError) as exc:
        print(f"COUNTER_FAULT infrastructure unusable: {exc!r}")
        print("ACCEPT-C-67: FAIL")
        return 2


if __name__ == "__main__":
    sys.exit(main())
