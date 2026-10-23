#!/usr/bin/env python3
r"""Round-63 claim C acceptance, revision 0 (before any data).

Claim C (coverage, sourced): a new culture-material knowledge entry
corpus/knowledge/culture-material/headgear-head-covering-codes.md - headgear as
rank, ritual and identity code (crowns, wreaths, helmets, veils, wraps, caps,
hoods) feeding the era-costume matrix - supported by exactly 24 new registry rows
S694-S717 opened this round.  Run from the lane root:

  python3 -B reports/round-63/accept-c.py [--root DIR]

Legs, each printed PASS or FAIL:
  FILE    the entry exists under --root; <= 250 lines; exactly one H1; no H3;
          at most 16 H2; it carries a `- topic:` line
  ROWS    corpus/SOURCES.md holds rows S694-S717 and no other new row; each has
          >= 11 cells; tier A or B; status `mined`; opened `2026-10-23`; recheck
          `180d`; used-by names the entry path; the anchor cell's first
          double-quoted span normalises to 8-25 words; the source cell carries a
          live http(s) URL and then ` ; capture <web.archive.org/web/<ts>id_/<original>>`
          whose embedded <original> equals the live URL
  ONEID   every entry line carrying an S-id carries exactly one; the entry is
          clean under tools/check-cited-lines.py (0 findings)
  RESTATE for every entry line citing one of the new ids: the clause before the
          (S###) mark has >= 5 content words (>= 4 letters, not a stopword), at
          least 3 of those content words appear in the row's anchor quote in the
          quote's order (subsequence), and no run of more than 12 consecutive
          clause words is copied verbatim from the quote
  LINK    each new row's live URL appears in exactly one registry line (its own)
          and nowhere in the entry
  APPEND  every `| S` line of the base registry (round base 65b393e) is present
          verbatim in the measured registry; the measured registry has exactly
          24 more `| S` rows than the base (619 -> 643)
  NOHARM  `git diff --name-only <base> <measured> -- corpus/knowledge` lists
          exactly the new entry
  SWEEP   `python3 -B reports/round-28/readme/sweep.py` exits 0 (rows == files,
          topic_mismatch 0) and the README row for the entry carries the entry's
          `- topic:` text byte-equal
  LIVE    the frozen enumerable subset - the rows S### of the S694-S717 block with
          (n-693) % 4 == 1, i.e. S694, S698, S702, S706, S710, S714 - each
          prints `LOCATED <url>` and exit 0 under the base locator
          `python3 -B reports/round-61/reopen-quote.py --row S###` (its own frozen
          budget: three attempts per URL over live then capture, one pass); any
          NOT_LOCATED after that budget fails the leg
Frozen predicate (the same sentence in reports/round-63/claims.json and in every
receipt): ACCEPT-C-63: every leg of reports/round-63/accept-c.py prints PASS.
Exit 0 only when every leg passes; 1 when any leg fails; 2 on unreadable input.
Review-only (never legs): blind per-row SUPPORT judgment by the RevRowS### wave
seats; topic fit against the partial owners; whether line wording beyond the
shared words is carried by its page.
"""
import argparse
import os
import re
import subprocess
import sys
import unicodedata

BASE = "65b393ef3a4d82bd693cc21b7f96a1231417d522"
ENTRY = "corpus/knowledge/culture-material/headgear-head-covering-codes.md"
REGISTRY = "corpus/SOURCES.md"
LOCATOR = "reports/round-61/reopen-quote.py"
SWEEP = "reports/round-28/readme/sweep.py"
CITED = "tools/check-cited-lines.py"
NEW_IDS = [f"S{n}" for n in range(694, 718)]
LIVE_IDS = [f"S{n}" for n in range(694, 718) if (n - 693) % 4 == 1]
ROW_RE = re.compile(r"^\|\s*(S\d+)\s*\|")
URL_RE = re.compile(r"https?://[^\s<>\"|`]+")
QUOTE_RE = re.compile(r'"([^"]+)"|“([^“”]+)”')
CAPTURE_RE = re.compile(r"web\.archive\.org/web/(\d+|[a-z]+)id_/(.+?)\s*(?:;|\||$)", re.IGNORECASE)
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
        if len(cs) < 11:
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
        elif urls and cap.group(2).rstrip(".;,')") != urls[0].rstrip(".;,')"):
            row_bad.append(f"{sid}:capture_original_mismatch")
    extra_new = sorted(set(reg_by_id) - set(ROW_RE.match(l).group(1) for l in base_lines) - set(NEW_IDS))
    if extra_new:
        row_bad.append(f"extra_new_rows={extra_new[:6]}")
    leg("ROWS", not row_bad, f"bad={row_bad[:8]} checked={len(NEW_IDS)}")

    # ---------- ONEID ----------
    oneid_bad = []
    cited = []
    for i, line in enumerate(lines, 1):
        ids = re.findall(r"\bS\d{3,}\b", line)
        if ids and len(ids) != 1:
            oneid_bad.append(f"line{i}:ids={ids}")
        if ids and len(ids) == 1 and ids[0] in NEW_IDS:
            cited.append((i, line, ids[0]))
    cl = subprocess.run([sys.executable, "-B", CITED, ENTRY], cwd=root,
                        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    cl_out = cl.stdout.decode("utf-8", "replace")
    clean = cl.returncode == 0 and "0 finding" in cl_out
    leg("ONEID", not oneid_bad and clean,
        f"bad={oneid_bad[:6]} cited_lines={len(cited)} cited_lines_tool=exit{cl.returncode} clean={clean}")

    # ---------- RESTATE ----------
    restate_bad = []
    for i, line, sid in cited:
        m = re.match(r"^\s*-\s+(.*?)\s*\(%s\)\s*$" % sid, line)
        if not m:
            restate_bad.append(f"line{i}:shape")
            continue
        clause = m.group(1)
        cw = content_words(clause)
        row = reg_by_id.get(sid, [None])[0]
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
    count_ok = len(reg_lines) == len(base_lines) + 24
    leg("APPEND", not missing and count_ok,
        f"missing_base_lines={len(missing)} base={len(base_lines)} measured={len(reg_lines)} +24={count_ok}")

    # ---------- NOHARM ----------
    proc = subprocess.run(["git", "-C", root, "diff", "--name-only", BASE, "main", "--", "corpus/knowledge"],
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    diff = proc.stdout.decode().split()
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
        row_line = next((l for l in readme.splitlines() if "headgear-head-covering-codes.md" in l), "")
        topic_ok = topic_text != "" and topic_text in row_line
    except OSError:
        topic_ok = False
    leg("SWEEP", sweep_ok and topic_ok, f"{sweep_detail} topic_row={topic_ok}")

    # ---------- LIVE ----------
    live_bad = []
    for sid in LIVE_IDS:
        if sid not in reg_by_id:
            live_bad.append(f"{sid}:no_row")
            continue
        try:
            loc = subprocess.run([sys.executable, "-B", LOCATOR, "--row", sid], cwd=root,
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=1500)
            out = loc.stdout.decode("utf-8", "replace")
            first = out.splitlines()[0] if out.splitlines() else ""
            if loc.returncode != 0 or not first.startswith("LOCATED"):
                live_bad.append(f"{sid}:{first[:60] or 'no_output'}")
        except subprocess.TimeoutExpired:
            live_bad.append(f"{sid}:leg_timeout")
    leg("LIVE", not live_bad, f"subset={LIVE_IDS} bad={live_bad}")

    verdict = all(legs)
    print(f"ACCEPT-C-63: {'PASS' if verdict else 'FAIL'}")
    return 0 if verdict else 1


if __name__ == "__main__":
    sys.exit(main())
