#!/usr/bin/env python3
"""L1 pre-integration checker for round-64 claim C (mirrors accept-c.py legs).

Reads a rows-dir of ScribeRow*/ and ScribeRej*/ contributions and prints, per
id, the same problems accept-c.py would report after integration (ROWS,
REJECTS, RESTATE).  Read-only: writes nothing.

  python3 -B .ufo/waves/round-64/check-rows.py --rows-dir <dir>
"""
import argparse
import os
import re
import sys
import unicodedata
from pathlib import Path

ENTRY = "corpus/knowledge/linguistics/language-socialization-and-acquisition.md"
NEW_IDS = [f"S{n}" for n in range(718, 744)]
REJ_IDS = [f"S{n}" for n in range(744, 750)]
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
    return (m.group(1) or m.group(2)) if m else None


def cells(line):
    return [c.strip() for c in line.split("|")[1:-1]] if line.startswith("|") else []


def norm_url(url):
    import urllib.parse
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


def parse(path):
    text = open(path, encoding="utf-8", errors="replace").read()
    fields = {}
    for line in text.splitlines():
        m = re.match(r"^(ROW|BULLET|VERIFY|CAPTURE|ACCESS|TEST|TEST2):[ \t]?(.*)$", line)
        if m:
            fields[m.group(1)] = m.group(2)
    return fields


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--rows-dir", required=True)
    args = ap.parse_args()
    root = Path(args.rows_dir)
    problems = {sid: [] for sid in NEW_IDS + REJ_IDS}
    seen_urls = {}
    for sid in NEW_IDS + REJ_IDS:
        cls = "ScribeRow" if sid in NEW_IDS else "ScribeRej"
        path = root / f"{cls}{sid}" / "row.txt"
        if not path.is_file():
            problems[sid].append("MISSING")
            continue
        f = parse(path)
        row = f.get("ROW", "")
        cs = cells(row)
        if len(cs) != 11:
            problems[sid].append(f"cells={len(cs)}")
            continue
        if sid in NEW_IDS:
            if cs[3] not in ("A", "B"):
                problems[sid].append(f"tier={cs[3]}")
            if cs[7] != "mined":
                problems[sid].append(f"status={cs[7]}")
            if cs[8] != "2026-10-23":
                problems[sid].append(f"opened={cs[8]}")
            if cs[9] != "180d":
                problems[sid].append(f"recheck={cs[9]}")
            if ENTRY not in cs[10]:
                problems[sid].append("usedby")
            quote = anchor_quote(cs[5])
            qw = norm_words(quote) if quote else []
            if not (8 <= len(qw) <= 25):
                problems[sid].append(f"quote_words={len(qw)}")
            urls = URL_RE.findall(cs[1])
            cap = CAPTURE_RE.search(cs[1])
            if not urls:
                problems[sid].append("no_live_url")
            else:
                seen_urls.setdefault(urls[0], []).append(sid)
            if not cap:
                problems[sid].append("no_capture")
            elif urls and norm_url(cap.group(2)) != norm_url(urls[0]):
                problems[sid].append("capture_mismatch")
            bullet = f.get("BULLET", "")
            m = re.match(r"^\s*-\s+(.*?)\s*\(%s\)\s*$" % sid, bullet)
            if not m:
                problems[sid].append("bullet_shape")
            else:
                clause = m.group(1)
                cw = content_words(clause)
                if len(cw) < 5:
                    problems[sid].append(f"content={len(cw)}")
                pos, hits = 0, 0
                for w in cw:
                    for j in range(pos, len(qw)):
                        if qw[j] == w:
                            pos = j + 1
                            hits += 1
                            break
                if hits < 3:
                    problems[sid].append(f"in_order={hits}")
                if not set(cw) - set(qw):
                    problems[sid].append("no_novel")
                clause_words = norm_words(clause)
                best = 0
                for start in range(len(clause_words)):
                    for length in range(best + 1, len(clause_words) - start + 1):
                        window = " ".join(clause_words[start:start + length])
                        if " " + window + " " in " " + " ".join(qw) + " ":
                            best = length
                        else:
                            break
                if best > 12:
                    problems[sid].append(f"copy_run={best}")
            if len(f) and not f.get("VERIFY", "").startswith("LOCATED"):
                problems[sid].append("verify_not_located")
        else:
            if cs[7] not in ("rejected", "queued"):
                problems[sid].append(f"status={cs[7]}")
            if not cs[6].startswith(("REJECTED:", "QUEUED-CANDIDATE:")) or "; flip:" not in cs[6]:
                problems[sid].append("teaches")
    for url, sids in seen_urls.items():
        if len(sids) > 1:
            for sid in sids:
                problems[sid].append(f"dup_live_url={sids}")
    bad = 0
    for sid in NEW_IDS + REJ_IDS:
        state = "OK" if not problems[sid] else "PROBLEMS " + " ".join(problems[sid])
        if problems[sid]:
            bad += 1
        print(f"{sid} {state}")
    print(f"CHECK-ROWS: {len(NEW_IDS) + len(REJ_IDS) - bad}/{len(NEW_IDS) + len(REJ_IDS)} clean")
    return 0 if bad == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
