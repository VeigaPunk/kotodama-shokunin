#!/usr/bin/env python3
r"""Round-64 claim C acceptance, revision 3 (pre-data).

Claim C (coverage, sourced): a new linguistics knowledge entry
corpus/knowledge/linguistics/language-socialization-and-acquisition.md -
how children learn language through culturally organized participation,
caregiver interaction, correction and multilingual socialization - supported
by exactly 26 new registry rows S718-S743 opened this round. Six further rows
S744-S749 preserve rejected candidates with reason and flip (round-63 closure
routed defect 7); the r63 S687 mined-but-unused status is corrected to queued
and its old->new change is logged in the lesson.  Run from the lane root:

  python3 -B reports/round-64/accept-c.py [--root DIR]

Legs, each printed PASS or FAIL:
  FILE    the entry exists under --root; <= 250 lines; exactly one H1; no H3;
          at most 16 H2; it carries a `- topic:` line
  ROWS    corpus/SOURCES.md holds rows S718-S743 and no other new row except
          the six listed rejection rows S744-S749; each new row has >= 11
          cells; tier A or B; status `mined`; opened `2026-10-23`; recheck
          `180d`; used-by names the entry path; anchor quote normalises to
          8-25 words; source cell has live URL followed by a same-page
          web.archive.org capture
  REJECTS six disposition rows S744-S749 (round-63 closure defect 7) carry
          status `rejected` or, where the retest contradicted the rejection
          ground, `queued`; teach cell `REJECTED: <reason>; flip: <what would
          change the verdict>` or `QUEUED-CANDIDATE: <reason>; flip: ...`, and
          a live URL, with ordinary re-open/status evidence recorded in the
          round-64 lesson Gate (revision 1, pre-data)
  ONEID   every entry line carrying an S-id carries exactly one; the entry is
          clean under tools/check-cited-lines.py (0 findings)
  RESTATE every entry line citing one of S718-S743 has >= 5 content words,
          >= 3 in-order content words from its row quote, no > 12-word copied
          run, and at least one novel content word
  HOSTS   no placeholder hosts
  LINK    each new row's live URL appears in exactly one registry line (its
          own) and nowhere in the entry
  APPEND  all base registry lines are preserved except S687, whose only
          allowed change is used-by/status mined→queued; exactly 32 rows are
          appended (26 mined + 6 rejected), so 643 → 675
  NOHARM  `git diff --name-only <base> <measured> -- corpus/knowledge` lists
          exactly the new entry
  SWEEP   `python3 -B reports/round-28/readme/sweep.py` exits 0 (rows == files,
          topic_mismatch 0) and README row carries the entry's topic verbatim
  LIVE    frozen subset S718,S723,S728,S733,S738,S743 each prints LOCATED
          using `python3 -B reports/round-61/reopen-quote.py --row S###`; the
          locator is pinned to base bytes, retry budget is three reopens 20s
          apart, and archived same-page captures remain inside each row.

Revision history (pre-data):
- revision 2: RESTATE rejects an entry clause copied verbatim from its row's
  teaches cell; forcing control: `.ufo/waves/round-64/w1/CriticClaims.md`.
- revision 3: ONEID rejects zero, missing, or duplicated citations among
  S718-S743; forcing control: `.ufo/waves/round-64/w1/ReviewerCounterC.md`
  (D1).
Frozen predicate (the same sentence in reports/round-64/claims.json and in
every receipt): ACCEPT-C-64: every leg of reports/round-64/accept-c.py prints
PASS.
Exit 0 only when every leg passes; 1 when any leg fails; 2 on unreadable input.
Review-only: blind per-row support judgment, topic fit, sentence support.
"""

import argparse
import os
import re
import subprocess
import sys
import time
import unicodedata
import urllib.parse
import hashlib

BASE = "ff30a205c8d23b35f1ac533740121a955a9fda96"
ENTRY = "corpus/knowledge/linguistics/language-socialization-and-acquisition.md"
REGISTRY = "corpus/SOURCES.md"
LOCATOR = "reports/round-61/reopen-quote.py"
SWEEP = "reports/round-28/readme/sweep.py"
CITED = "tools/check-cited-lines.py"
NEW_IDS = [f"S{n}" for n in range(718, 744)]
REJ_IDS = [f"S{n}" for n in range(744, 750)]
LIVE_IDS = [f"S{n}" for n in range(718, 744) if (n - 717) % 5 == 1]
# frozen pin of reports/round-61/reopen-quote.py at round base 65b393e
# (revision 3, RevCounterC H2: the LIVE leg must execute pinned bytes, never a mutable locator)
LOCATOR_SHA256 = None  # filled below from the base revision
ROW_RE = re.compile(r"^\|\s*(S\d+)\s*\|")
URL_RE = re.compile(r"https?://[^\s<>\"|`]+")
QUOTE_RE = re.compile(r'"([^"]+)"|“([^“”]+)”')
CAPTURE_RE = re.compile(r"web\.archive\.org/web/(\d{14})id_/(\S+?)\s*[.;]?\s*$", re.IGNORECASE)
NONWORD = re.compile(r"[\W_]+", re.UNICODE)
STOPWORDS = set("""
a an and are as at be been but by for from has have he her his i if in into is it its
of on or she so that the their them they this to was we were with you your not no nor
""".split())


def norm_words(text):
    folded = unicodedata.normalize("NFKC", text).casefold()
    return [w for w in NONWORD.sub(" ", folded).split() if w]


def content_words(text):
    return [w for w in norm_words(text) if len(w) >= 4 and w not in STOPWORDS and w.isalpha()]


def anchor_quote(cell):
    m = QUOTE_RE.search(cell)
    return m.group(1) or m.group(2) if m else None


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
    dropped, query and fragment ignored, path trailing slash stripped."""
    try:
        parts = urllib.parse.urlsplit(url.strip().rstrip(".,;'"))
    except ValueError:
        return url.strip().lower()
    scheme = parts.scheme.lower()
    host = (parts.hostname or "").lower()
    if host.startswith("www."):
        host = host[4:]
    port = parts.port
    if port and not (scheme == "http" and port == 80) and not (scheme == "https" and port == 443):
        host = f"{host}:{port}"
    path = parts.path or "/"
    if path != "/" and path.endswith("/"):
        path = path[:-1]
    return f"{scheme}://{host}{path}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    root = os.path.abspath(ap.parse_args().root)
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
    row_bad = []
    live_urls = {}
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
        if opened != "2026-10-23":
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
        if not cap:
            row_bad.append(f"{sid}:no_capture")
        elif urls and norm_url(cap.group(2)) != norm_url(urls[0]):
            row_bad.append(f"{sid}:capture_original_mismatch")
    extra_new = sorted(set(reg_by_id) - set(ROW_RE.match(l).group(1) for l in base_lines) - set(NEW_IDS) - set(REJ_IDS))
    if extra_new:
        row_bad.append(f"extra_new_rows={extra_new[:6]}")
    leg("ROWS", not row_bad, f"bad={row_bad[:8]} checked={len(NEW_IDS)}")
    # ---------- REJECTS ----------
    # revision 1 (pre-data): routed defect 7 asks for the round-63 rejected
    # candidates to be curated as rows.  Three retests still hold (S744 403
    # redirect, S745 403, S747 403); two seats re-opened their candidate and
    # found the ground contradicted (S748 LacusCurtius Corona 200 + LOCATED,
    # S749 Wikipedia headgear 200 + LOCATED), so a curated row must be able to
    # carry an honest queued-candidate disposition instead of a false rejection.
    # The leg therefore checks a disposition row: status rejected or queued,
    # a `REJECTED:` / `QUEUED-CANDIDATE:` reason and a `; flip:` clause.
    rej_bad = []
    for sid in REJ_IDS:
        rows = reg_by_id.get(sid, [])
        if len(rows) != 1:
            rej_bad.append(f"{sid}:rows={len(rows)}")
            continue
        cs = cells(rows[0])
        if len(cs) != 11 or cs[7] not in ("rejected", "queued"):
            rej_bad.append(f"{sid}:shape_or_status")
            continue
        teaches = cs[6]
        if not teaches.startswith(("REJECTED:", "QUEUED-CANDIDATE:")) or "; flip:" not in teaches:
            rej_bad.append(f"{sid}:teaches={teaches[:40]}")
    leg("REJECTS", not rej_bad, f"bad={rej_bad[:8]} checked={len(REJ_IDS)}")


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
    # revision 3 (pre-data; forcing control:
    # .ufo/waves/round-64/w1/ReviewerCounterC.md, D1): require each new ID
    # exactly once in the entry.
    leg("ONEID", not oneid_bad and not mark_bad and clean and citation_exact,
        f"bad={oneid_bad[:6]} marks={mark_bad[:6]} cited_lines={len(cited)} "
        f"cited_lines_tool=exit{cl.returncode} clean={clean} "
        f"citations_exactly_once={citation_exact} missing={missing_citations} "
        f"duplicates={duplicate_citations}")

    # ---------- RESTATE ----------
    restate_bad = []
    for i, line, sid in cited:
        m = re.match(r"^\s*-\s+(.*?)\s*\(%s\)\s*$" % sid, line)
        if not m:
            restate_bad.append(f"line{i}:shape")
            continue
        clause = m.group(1)
        row = reg_by_id.get(sid, [None])[0]
        # revision 2 (pre-data; forcing control:
        # .ufo/waves/round-64/w1/CriticClaims.md): a clause copied verbatim
        # from this source row's teaches cell is not a novel restatement.
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
        it = iter(range(len(qset_seq)))
        order_hits = 0
        pos = 0
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
        # anti-dump: the clause must add at least one content word beyond the quote's words
        if not set(cw) - set(qset_seq):
            restate_bad.append(f"line{i}:{sid}:no_novel_content_word")
        # longest run of consecutive clause words copied verbatim from the quote
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
    leg("RESTATE", not restate_bad, f"bad={restate_bad[:8]} lines={len(cited)}")

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
    # routed exception: S687's status cell flips mined -> queued (round-62 item
    # 7 / round-63 defect; logged old->new).  The base S687 line may miss the
    # multiset by exactly one and must be the only tolerated absence.
    tolerated = [l for l in missing if l.startswith("| S687 ")]
    missing_hard = [l for l in missing if not l.startswith("| S687 ")]
    s687_ok = len(tolerated) <= 1 and any(
        r.startswith("| S687 ") and cells(r)[7] == "queued" for r in reg_lines)
    count_ok = len(reg_lines) == len(base_lines) + 32
    leg("APPEND", not missing_hard and count_ok and s687_ok,
        f"missing_base_lines={len(missing_hard)} s687_queued={s687_ok} "
        f"base={len(base_lines)} measured={len(reg_lines)} +32={count_ok}")

    # ---------- NOHARM ----------
    proc = subprocess.run(["git", "-C", root, "diff", "--name-only", BASE, "main", "--", "corpus/knowledge"],
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    diff = sorted(proc.stdout.decode().split())
    noharm_ok = proc.returncode == 0 and diff == [ENTRY]
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
                         if l.startswith("- `language-socialization-and-acquisition.md`")), "")
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
    pin = LOCATOR_SHA256
    if pin is None:
        # resolve the pin from the base revision once, then hard-code it (rev 3)
        base_blob = subprocess.run(["git", "-C", root, "show", f"{BASE}:{LOCATOR}"],
                                   stdout=subprocess.PIPE).stdout
        pin = hashlib.sha256(base_blob).hexdigest() if base_blob else "unresolvable"
    if digest != pin:
        live_bad.append(f"locator_sha={digest}!={pin}")
    for sid in LIVE_IDS:
        if sid not in reg_by_id:
            live_bad.append(f"{sid}:no_row")
            continue
        # revision 4 (pre-data, receipt: telemetry/row-verify.txt S706 flakiness):
        # the leg re-invokes the locator up to 3 times, 20 s apart, because the
        # frozen subset's hosts rate-limit in windows (NMA observed 2/3 flapping)
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
    print(f"ACCEPT-C-64: {'PASS' if verdict else 'FAIL'}")
    return 0 if verdict else 1


if __name__ == "__main__":
    sys.exit(main())
