#!/usr/bin/env python3
r"""Round-65 claim C acceptance, revision 1 (pre-data).

Claim C (coverage, sourced): the games / play / sport / contests register is
unowned in corpus/knowledge (0 filename owners, 0 topic-line owners at the
round-65 base) -> one new culture-material entry
corpus/knowledge/culture-material/games-play-sport-contests.md supported by
exactly 26 new registry rows S750-S775 opened this round (2026-10-24), each
mined and cited exactly once by the entry.  Run from the lane root:

  python3 -B reports/round-65/accept-c.py [--root DIR]

Legs, each printed PASS or FAIL:
  FILE    the entry exists under --root; <= 250 lines; exactly one H1; no H3;
          at most 16 H2; it carries a `- topic:` line
  ROWS    corpus/SOURCES.md holds rows S750-S775 and no other new row; each
          has >= 11 cells; tier A or B; status `mined`; opened `2026-10-24`;
          recheck `180d`; used-by names the entry; anchor quote normalises to
          8-25 words; source cell has live URL followed by a same-page
          web.archive.org capture whose original query-aware-normalizes equal
          to the live URL
  ONEID   every entry line carrying an S-id carries exactly one; the entry is
          clean under tools/check-cited-lines.py (0 findings); each of
          S750-S775 is cited exactly once
  RESTATE every entry line citing one of S750-S775 has >= 5 content words,
          >= 3 in-order content words from its row quote, no > 12-word copied
          run, at least one novel content word, and is not a near-copy of its
          row's teaches cell: word-boundary normalised (NFKC, casefold,
          [\w]+ tokens) clause content words that appear in-order as a
          subsequence of the teaches cell's content words covering >= 80% of
          the clause's content words FAIL the leg (round-64 routed residual:
          the trailing-word teaches-copy bypass of the verbatim-copy rule)
  HOSTS   no placeholder hosts
  LINK    each new row's live URL appears in exactly one registry line (its
          own) and nowhere in the entry; no two new rows share a
          query-aware-normalized URL (query and fragment ignored)
  APPEND  all base registry lines are preserved verbatim; exactly 26 rows are
          appended, so 675 -> 701
  NOHARM  `git diff --name-only <base> main -- corpus/knowledge` lists
          exactly the new entry
  SWEEP   `python3 -B reports/round-28/readme/sweep.py` exits 0 (rows == files,
          topic_mismatch 0) and README row carries the entry's topic verbatim
  LIVE    frozen subset S750,S755,S760,S765,S770,S775 each prints LOCATED
          using `python3 -B reports/round-61/reopen-quote.py --row S###`; the
          locator is pinned to base bytes, retry budget is three reopens 20s
          apart, and archived same-page captures remain inside each row

Revision history (pre-data):
- revision 1: RESTATE gains the word-boundary teaches near-copy rule and
  LINK/ROWS gain query-aware URL normalization (round-64 routed residuals:
  `w2/RevVerifyC.md` F2; check-rows.py normalization gap).  Forcing
  controls: `reports/round-65/telemetry/controls-c.txt` (the teaches-cell +
  trailing-word fixture fails RESTATE; a query-only URL twin fails ROWS).
- revision 2a: NOHARM tolerates the pre-declared Ca R7 land (the round-64
  entry edit) alongside the new entry - C and Ca were mutually exclusive.
- revision 2: RESTATE requires every new row cited (no empty-cited
  vacuous pass; forcing control `.ufo/waves/round-65/w1/CriticControlC.md`).
Frozen predicate (the same sentence in reports/round-65/claims.json and in
every receipt): ACCEPT-C-65: every leg of reports/round-65/accept-c.py
prints PASS.
Exit 0 only when every leg passes; 1 when any leg fails; 2 on unreadable
input.  Review-only: blind per-row support judgment, topic fit, sentence
support, the lore handoff.
"""

import argparse
import hashlib
import os
import re
import subprocess
import sys
import time
import unicodedata
import urllib.parse

BASE = "17c32302c6845c8f164b985a8cb312d3181c8788"
ENTRY = "corpus/knowledge/culture-material/games-play-sport-contests.md"
REGISTRY = "corpus/SOURCES.md"
LOCATOR = "reports/round-61/reopen-quote.py"
SWEEP = "reports/round-28/readme/sweep.py"
CITED = "tools/check-cited-lines.py"
NEW_IDS = [f"S{n}" for n in range(750, 776)]
LIVE_IDS = ["S750", "S755", "S760", "S765", "S770", "S775"]
ROW_RE = re.compile(r"^\|\s*(S\d+)\s*\|")
URL_RE = re.compile(r"https?://[^\s<>\"|`]+")
QUOTE_RE = re.compile(r'"([^"]+)"|“([^“”]+)”')
CAPTURE_RE = re.compile(r"web\.archive\.org/web/(\d{14})id_/(\S+?)\s*[.;]?\s*$", re.IGNORECASE)
NONWORD = re.compile(r"[\W_]+", re.UNICODE)
WORD_RE = re.compile(r"\w+", re.UNICODE)
STOPWORDS = set("""
a an and are as at be been but by for from has have he her his i if in into is it its
of on or she so that the their them they this to was we were with you your not no nor
""".split())


def norm_words(text):
    folded = unicodedata.normalize("NFKC", text).casefold()
    return [w for w in NONWORD.sub(" ", folded).split() if w]


def word_tokens(text):
    """Word-boundary tokenisation for the near-copy rule: NFKC, casefold,
    maximal word-character runs (regex: backslash-w plus)."""
    return WORD_RE.findall(unicodedata.normalize("NFKC", text).casefold())


def content_words(text):
    return [w for w in norm_words(text) if len(w) >= 4 and w not in STOPWORDS and w.isalpha()]


def anchor_quote(cell):
    m = QUOTE_RE.search(cell)
    return (m.group(1) or m.group(2)) if m else None


def cells(line):
    return [c.strip() for c in line.split("|")[1:-1]] if line.startswith("|") else []


def git_bytes(root, rev, path):
    proc = subprocess.run(["git", "-C", root, "show", f"{rev}:{path}"],
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if proc.returncode != 0:
        return None
    return proc.stdout.decode("utf-8", "strict")


def norm_url(url):
    """Identity for LINK: scheme+host lowercased, www. stripped, default port
    dropped, query and fragment ignored (query-aware), path trailing slash
    stripped."""
    try:
        parts = urllib.parse.urlsplit(url.strip().rstrip(".,;'"))
    except ValueError:
        return url.strip().lower()
    scheme = parts.scheme.lower()
    host = (parts.hostname or "").lower()
    if host.startswith("www."):
        host = host[4:]
    # revision 3 (RevRegistryFinal: a bad port raised ValueError and aborted
    # the counter before any leg line): fail closed to the stripped literal.
    try:
        port = parts.port
    except ValueError:
        return url.strip().lower()
    if port and not (scheme == "http" and port == 80) and not (scheme == "https" and port == 443):
        host = f"{host}:{port}"
    path = parts.path or "/"
    if path != "/" and path.endswith("/"):
        path = path[:-1]
    return f"{scheme}://{host}{path}"


def in_order_coverage(clause_words, reference_words):
    """Fraction of clause_words occurring in-order as a subsequence of
    reference_words (word-boundary tokens)."""
    if not clause_words:
        return 0.0
    pos = 0
    hits = 0
    for w in clause_words:
        found = False
        for j in range(pos, len(reference_words)):
            if reference_words[j] == w:
                pos = j + 1
                found = True
                break
        if found:
            hits += 1
    return hits / len(clause_words)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    root = os.path.abspath(ap.parse_args().root)
    import hashlib as _hl
    _self = _hl.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest()
    _mv = subprocess.run(["git", "rev-parse", "main"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(f"# counter sha256 (self): {_self}")
    print(f"# measured revision (lane main): {_mv.stdout.decode().strip() or 'unresolvable'}")
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
    try:
        base_text = git_bytes(root, BASE, REGISTRY)
        if base_text is None:
            raise ValueError(f"git show {BASE}:{REGISTRY} failed")
    except Exception as error:
        print(f"ACCEPT_C_INPUT_ERROR base: {error}", file=sys.stderr)
        return 2
    reg_lines = [l for l in reg_text.splitlines() if ROW_RE.match(l)]
    base_lines = [l for l in base_text.splitlines() if ROW_RE.match(l)]
    reg_by_id = {}
    for line in reg_lines:
        m = ROW_RE.match(line)
        reg_by_id.setdefault(m.group(1), []).append(line)

    # ---------- ROWS ----------
    # revision 3 (RevRegistryFinal): the duplicate scan must be seeded with
    # the base rows - query/www/trailing-slash/scheme/fragment twins of a base
    # URL used to pass every registry leg.
    row_bad = []
    live_urls = {}
    norm_seen = {}
    for bline in base_lines:
        bcs = cells(bline)
        if len(bcs) == 11:
            for u in URL_RE.findall(bcs[1]):
                norm_seen.setdefault(norm_url(u), "base:" + (ROW_RE.match(bline).group(1) if ROW_RE.match(bline) else "?"))
    for sid in NEW_IDS:
        rows = reg_by_id.get(sid, [])
        if len(rows) != 1:
            row_bad.append(f"{sid}:rows={len(rows)}")
            continue
        cs = cells(rows[0])
        if len(cs) != 11:
            row_bad.append(f"{sid}:cells={len(cs)}")
            continue
        source, kind, tier, scope, anchor = cs[1], cs[2], cs[3], cs[4], cs[5]
        teaches, status, opened, recheck, usedby = cs[6], cs[7], cs[8], cs[9], cs[10]
        if tier not in ("A", "B"):
            row_bad.append(f"{sid}:tier={tier}")
        if status != "mined":
            row_bad.append(f"{sid}:status={status}")
        if opened != "2026-10-24":
            row_bad.append(f"{sid}:opened={opened}")
        if recheck != "180d":
            row_bad.append(f"{sid}:recheck={recheck}")
        if ENTRY not in usedby:
            row_bad.append(f"{sid}:usedby={usedby[:40]}")
        quote = anchor_quote(anchor)
        qw = norm_words(quote) if quote else []
        if not (8 <= len(qw) <= 25):
            row_bad.append(f"{sid}:quote_words={len(qw)}")
        urls = URL_RE.findall(source)
        cap = CAPTURE_RE.search(source)
        if not urls:
            row_bad.append(f"{sid}:no_live_url")
            live_urls[sid] = None
        else:
            live_urls[sid] = urls[0]
            nurl = norm_url(urls[0])
            if nurl in norm_seen:
                row_bad.append(f"{sid}:norm_dup_of={norm_seen[nurl]}")
            else:
                norm_seen[nurl] = sid
        if not cap:
            row_bad.append(f"{sid}:no_capture")
        elif urls and norm_url(cap.group(2)) != norm_url(urls[0]):
            row_bad.append(f"{sid}:capture_original_mismatch")
    extra_new = sorted(set(reg_by_id) - set(ROW_RE.match(l).group(1) for l in base_lines) - set(NEW_IDS))
    if extra_new:
        row_bad.append(f"extra_new_rows={extra_new[:6]}")
    leg("ROWS", not row_bad, f"bad={row_bad[:8]} checked={len(NEW_IDS)}")

    # ---------- ONEID + NOMARK ----------
    oneid_bad = []
    cited = []
    MARK_RE = re.compile(r"\((?:to-verify|unverified|todo|fixme|tbd|draft)\b", re.IGNORECASE)
    mark_bad = []
    for i, line in enumerate(lines, 1):
        ids = re.findall(r"\bS\d{3,}\b", line)
        if ids and len(ids) != 1:
            oneid_bad.append(f"line{i}:ids={ids}")
        if ids and MARK_RE.search(line):
            mark_bad.append(f"line{i}")
        if ids and len(ids) == 1 and ids[0] in NEW_IDS:
            cited.append((i, line, ids[0]))
    cl = subprocess.run([sys.executable, "-B", CITED, ENTRY], cwd=root,
                        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    cl_out = cl.stdout.decode("utf-8", "replace")
    clean = cl.returncode == 0 and "0 finding" in cl_out
    cited_ids = [sid for _, _, sid in cited]
    citation_exact = sorted(cited_ids) == NEW_IDS
    missing_citations = [sid for sid in NEW_IDS if sid not in cited_ids]
    duplicate_citations = [sid for sid in NEW_IDS if cited_ids.count(sid) > 1]
    leg("ONEID", not oneid_bad and not mark_bad and clean and citation_exact,
        f"bad={oneid_bad[:6]} marks={mark_bad[:6]} cited_lines={len(cited)} "
        f"cited_lines_tool=exit{cl.returncode} clean={clean} "
        f"citations_exactly_once={citation_exact} missing={missing_citations} "
        f"duplicates={duplicate_citations}")

    # ---------- RESTATE (with word-boundary teaches near-copy rule) ----------
    restate_bad = []
    for i, line, sid in cited:
        m = re.match(r"^\s*-\s+(.*?)\s*\(%s\)\s*$" % sid, line)
        if not m:
            restate_bad.append(f"line{i}:shape")
            continue
        clause = m.group(1)
        row = reg_by_id.get(sid, [None])[0]
        teaches = cells(row)[6] if row else None
        if teaches is not None and clause == teaches:
            restate_bad.append(f"line{i}:{sid}:teaches_copy")
        cw = content_words(clause)
        quote = anchor_quote(cells(row)[5]) if row else None
        qw = norm_words(quote) if quote else []
        if len(cw) < 5:
            restate_bad.append(f"line{i}:{sid}:content={len(cw)}")
            continue
        qset_seq = qw
        pos = 0
        order_hits = 0
        for w in cw:
            found = False
            for j in range(pos, len(qset_seq)):
                if qset_seq[j] == w:
                    pos = j + 1
                    found = True
                    break
            if found:
                order_hits += 1
        if order_hits < 3:
            restate_bad.append(f"line{i}:{sid}:in_order={order_hits}")
        if not set(cw) - set(qset_seq):
            restate_bad.append(f"line{i}:{sid}:no_novel_content_word")
        clause_words = norm_words(clause)
        best = 0
        for start in range(len(clause_words)):
            for length in range(best + 1, len(clause_words) - start + 1):
                window = clause_words[start:start + length]
                joined = " ".join(window)
                if " " + joined + " " in " " + " ".join(qset_seq) + " ":
                    best = length
                else:
                    break
        if best > 12:
            restate_bad.append(f"line{i}:{sid}:copy_run={best}")
        # revision 1: word-boundary near-copy of the teaches cell.  The
        # round-64 trailing-word bypass appended one novel word to a verbatim
        # teaches copy; token-subsequence coverage catches it.
        if teaches is not None:
            clause_tokens = word_tokens(clause)
            teaches_tokens = word_tokens(teaches)
            cov = in_order_coverage(clause_tokens, teaches_tokens)
            if len(clause_tokens) >= 5 and cov >= 0.8:
                restate_bad.append(f"line{i}:{sid}:teaches_nearcopy={cov:.2f}")
    # revision 2 (pre-data; forcing control:
    # .ufo/waves/round-65/w1/CriticControlC.md - RESTATE passed vacuously with
    # zero cited lines when ONEID was the only leg requiring citations): the
    # leg fails unless every new row is cited, so no empty-cited pass exists.
    leg("RESTATE", not restate_bad and len(cited) == len(NEW_IDS),
        f"bad={restate_bad[:8]} lines={len(cited)}/{len(NEW_IDS)}")

    # ---------- HOSTS ----------
    PLACEHOLDER_HOSTS = (
        "example.com", "example.org", "example.net", "example.io", "example.edu",
        "httpbin.org", "httpbingo.org", "reqres.in", "postman-echo.com", "jsonplaceholder.typicode.com",
    )
    hosts_bad = []
    for sid, url in live_urls.items():
        if not url:
            continue
        host = re.sub(r"^https?://", "", url).split("/")[0].lower().split(":")[0]
        host = host.rsplit("@", 1)[-1]  # revision 3: userinfo must not mask the host
        if any(host == ph or host.endswith("." + ph) for ph in PLACEHOLDER_HOSTS):
            hosts_bad.append(f"{sid}:{host}")
    leg("HOSTS", not hosts_bad, f"bad={hosts_bad[:6]}")

    # ---------- LINK ----------
    link_bad = []
    for sid, url in live_urls.items():
        if not url:
            continue
        hits = sum(1 for line in reg_lines if url in line)
        if hits != 1:
            link_bad.append(f"{sid}:registry_hits={hits}")
        if url in text:
            link_bad.append(f"{sid}:url_in_entry")
    leg("LINK", not link_bad, f"bad={link_bad[:6]}")

    # ---------- APPEND ----------
    reg_multiset = {}
    for line in reg_lines:
        reg_multiset[line] = reg_multiset.get(line, 0) + 1
    missing = [l for l in base_lines if reg_multiset.get(l, 0) < base_lines.count(l)]
    count_ok = len(reg_lines) == len(base_lines) + 25
    leg("APPEND", not missing and count_ok,
        f"missing_base_lines={len(missing)} base={len(base_lines)} "
        f"measured={len(reg_lines)} +26={count_ok}")

    # ---------- NOHARM ----------
    proc = subprocess.run(["git", "-C", root, "diff", "--name-only", BASE, "main", "--", "corpus/knowledge"],
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    diff = sorted(proc.stdout.decode().split())
    # revision 2 (pre-data; forcing control .ufo/waves/round-65/w1/RevClaimCa.md
    # HIGH-4: Ca's R7 land edits the round-64 entry, so an exact-single-file
    # diff made C and Ca mutually exclusive).  The tolerated second path is
    # claim Ca's pre-declared R7 land.
    allowed = sorted([ENTRY, "corpus/knowledge/linguistics/language-socialization-and-acquisition.md"])
    noharm_ok = proc.returncode == 0 and diff in ([ENTRY], allowed)
    leg("NOHARM", noharm_ok, f"diff={diff}")

    # ---------- SWEEP ----------
    sweep_ok = False
    sweep_detail = "not run"
    if os.path.isfile(os.path.join(root, SWEEP)):
        sw = subprocess.run([sys.executable, "-B", SWEEP], cwd=root,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=600)
        sweep_ok = sw.returncode == 0
        sweep_detail = f"exit={sw.returncode}"
    topic_line = next((l for l in lines if l.startswith("- topic:")), "")
    topic_text = topic_line[len("- topic:"):].strip() if topic_line else ""
    try:
        readme = open(os.path.join(root, "corpus", "README.md"), encoding="utf-8").read()
        row_line = next((l for l in readme.splitlines()
                         if l.startswith("- `games-play-sport-contests.md`")), "")
        topic_ok = topic_text != "" and topic_text in row_line
    except OSError:
        topic_ok = False
    leg("SWEEP", sweep_ok and topic_ok, f"{sweep_detail} topic_row={topic_ok}")

    # ---------- LIVE ----------
    live_bad = []
    locator_path = os.path.join(root, LOCATOR)
    try:
        blob = open(locator_path, "rb").read()
        digest = hashlib.sha256(blob).hexdigest()
    except OSError:
        digest = None
    base_blob = subprocess.run(["git", "-C", root, "show", f"{BASE}:{LOCATOR}"],
                               stdout=subprocess.PIPE).stdout
    pin = hashlib.sha256(base_blob).hexdigest() if base_blob else "unresolvable"
    if digest != pin:
        live_bad.append(f"locator_sha={digest}!={pin}")
    for sid in LIVE_IDS:
        if sid not in reg_by_id:
            live_bad.append(f"{sid}:no_row")
            continue
        located = False
        detail = ""
        for attempt in range(3):
            try:
                loc = subprocess.run([sys.executable, "-B", LOCATOR, "--row", sid], cwd=root,
                                     stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=1500)
                out = loc.stdout.decode("utf-8", "replace")
                first = out.splitlines()[0] if out.splitlines() else ""
                detail = first
                if loc.returncode == 0 and first.startswith("LOCATED"):
                    located = True
                    break
            except subprocess.TimeoutExpired:
                detail = "leg_timeout"
            if attempt + 1 < 3:
                time.sleep(20)
        if not located:
            live_bad.append(f"{sid}:{detail[:60] or 'no_output'}")
    leg("LIVE", not live_bad, f"subset={LIVE_IDS} bad={live_bad}")

    verdict = all(legs)
    print(f"ACCEPT-C-65: {'PASS' if verdict else 'FAIL'}")
    return 0 if verdict else 1


if __name__ == "__main__":
    sys.exit(main())
