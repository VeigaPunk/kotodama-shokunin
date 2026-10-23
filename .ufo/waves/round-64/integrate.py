#!/usr/bin/env python3
"""Round-64 claim C integration helper (L1-owned).

Reads the wave-1 scribe artifacts under ~/.cache/hyaku/kotodama-r64/, validates
each row against the accept-c ROWS rules, checks each bullet against the
RESTATE rules, and stages:
  .ufo/waves/round-64/stage/rows.txt    (11-cell rows, ascending id)
  .ufo/waves/round-64/stage/bullets.json (id -> bullet line)
  .ufo/waves/round-64/stage/report.txt  (per-id verdicts)

Never writes corpus/.  Run: python3 -B .ufo/waves/round-64/integrate.py
"""
import glob
import json
import os
import re
import sys
import unicodedata

ROOT = "/home/vgpnk/Projects/shokunin/kotodama-shokunin"
CACHE = os.path.expanduser("~/.cache/hyaku/kotodama-r64")
ENTRY = "corpus/knowledge/linguistics/language-socialization-and-acquisition.md"
NEW_IDS = [f"S{n}" for n in range(718, 744)]
REJ_IDS = [f"S{n}" for n in range(744, 750)]
NONWORD = re.compile(r"[\W_]+", re.UNICODE)
STOPWORDS = set("""
a an and are as at be been but by for from has have he her his i if in into is it its
of on or she so that the their them they this to was we were with you your not no nor
""".split())
QUOTE_RE = re.compile(r'"([^"]+)"|“([^“”]+)”')
CAPTURE_RE = re.compile(r"web\.archive\.org/web/(\d{14})id_/(\S+?)\s*[.;]?\s*$", re.IGNORECASE)
URL_RE = re.compile(r"https?://[^\s<>\"|`]+")


def norm_words(text):
    folded = unicodedata.normalize("NFKC", text).casefold()
    return [w for w in NONWORD.sub(" ", folded).split() if w]


def content_words(text):
    return [w for w in norm_words(text) if len(w) >= 4 and w not in STOPWORDS and w.isalpha()]


def anchor_quote(cell):
    m = QUOTE_RE.search(cell)
    return (m.group(1) or m.group(2)) if m else None


def norm_url(url):
    import urllib.parse
    parts = urllib.parse.urlsplit(url.strip().rstrip(".,;'"))
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


def parse_row(path):
    text = open(path, encoding="utf-8", errors="replace").read()
    line = next((l for l in text.splitlines() if l.startswith("ROW:")), None)
    bullet = next((l for l in text.splitlines() if l.startswith("BULLET:")), None)
    verify = next((l for l in text.splitlines() if l.startswith("VERIFY:")), None)
    return line, bullet, verify


def main():
    stage = os.path.join(ROOT, ".ufo/waves/round-64/stage")
    os.makedirs(stage, exist_ok=True)
    rows, bullets, report = {}, {}, []
    for sid in NEW_IDS + REJ_IDS:
        path = os.path.join(CACHE, f"ScribeRow{sid}", "row.txt")
        if not os.path.exists(path):
            path = os.path.join(CACHE, f"ScribeRej{sid}", "row.txt")
        if not os.path.exists(path) or os.path.getsize(path) == 0:
            report.append(f"{sid} MISSING")
            continue
        line, bullet, verify = parse_row(path)
        if not line:
            report.append(f"{sid} NO-ROW-LINE")
            continue
        row = line[4:].strip()
        cs = [c.strip() for c in row.split("|")[1:-1]] if row.startswith("|") else []
        problems = []
        if len(cs) != 11:
            problems.append(f"cells={len(cs)}")
            report.append(f"{sid} BAD {' '.join(problems)}")
            continue
        if sid in NEW_IDS:
            if cs[3] not in ("A", "B"):
                problems.append(f"tier={cs[3]}")
            if cs[7] != "mined":
                problems.append(f"status={cs[7]}")
            if cs[8] != "2026-10-23":
                problems.append(f"opened={cs[8]}")
            if cs[9] != "180d":
                problems.append(f"recheck={cs[9]}")
            if ENTRY not in cs[10]:
                problems.append("usedby")
            quote = anchor_quote(cs[5])
            qw = norm_words(quote) if quote else []
            if not (8 <= len(qw) <= 25):
                problems.append(f"quote_words={len(qw)}")
            urls = URL_RE.findall(cs[1])
            cap = CAPTURE_RE.search(cs[1])
            if not urls:
                problems.append("no_live_url")
            if not cap:
                problems.append("no_capture")
            elif urls and norm_url(cap.group(2)) != norm_url(urls[0]):
                problems.append("capture_mismatch")
        else:
            if cs[7] not in ("rejected", "queued"):
                problems.append(f"status={cs[7]}")
            if not cs[6].startswith(("REJECTED:", "QUEUED-CANDIDATE:")) or "; flip:" not in cs[6]:
                problems.append("teaches")
        rows[sid] = row
        if bullet:
            bullets[sid] = bullet[len("BULLET:"):].strip()
        else:
            problems.append("no_bullet")
        # RESTATE preview for mined rows
        if sid in NEW_IDS and bullet:
            b = bullets[sid]
            m = re.match(r"^\s*-\s+(.*?)\s*\(%s\)\s*$" % sid, b)
            if not m:
                problems.append("bullet_shape")
            else:
                clause = m.group(1)
                cw = content_words(clause)
                quote = anchor_quote(cs[5])
                qw = norm_words(quote) if quote else []
                pos, hits = 0, 0
                for w in cw:
                    for j in range(pos, len(qw)):
                        if qw[j] == w:
                            pos = j + 1
                            hits += 1
                            break
                if len(cw) < 5:
                    problems.append(f"content={len(cw)}")
                if hits < 3:
                    problems.append(f"in_order={hits}")
                if not set(cw) - set(qw):
                    problems.append("no_novel")
        report.append(f"{sid} {'OK' if not problems else 'PROBLEMS'} {' '.join(problems)}")
        if verify:
            report.append(f"    {verify.strip()[:150]}")
    with open(os.path.join(stage, "rows.txt"), "w", encoding="utf-8") as fh:
        for sid in NEW_IDS + REJ_IDS:
            if sid in rows:
                fh.write(rows[sid] + "\n")
    with open(os.path.join(stage, "bullets.json"), "w", encoding="utf-8") as fh:
        json.dump(bullets, fh, indent=1, ensure_ascii=False)
    with open(os.path.join(stage, "report.txt"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(report) + "\n")
    print("\n".join(report))
    print(f"rows={len(rows)} bullets={len(bullets)}")


if __name__ == "__main__":
    sys.exit(main())
