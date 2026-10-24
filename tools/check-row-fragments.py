#!/usr/bin/env python3
r"""Pre-integration fragment checker for sourced coverage rows (round 65).

Closes the round-64 routed residual on the seat-local check-rows.py: two
gaps are repaired durably here -

  teaches-length   a row's `teaches` cell is bounded (<= TEACHES_MAX chars);
                   an over-long cell is a finding (`teaches-length`)
  url-normalization  duplicate detection between the live URL and the
                   Wayback capture original, and across rows, is query- and
                   fragment-aware: scheme+host casefolded, `www.` stripped,
                   default port dropped, query and fragment ignored, path
                   trailing slash stripped (same identity as the lane
                   counters' norm_url). Two rows whose URLs differ only in
                   query/fragment are one duplicate (`dup-url`); a capture
                   whose original does not normalize-equal the live URL is
                   a finding (`capture-url-mismatch`)

Usage (lane root):

  python3 -B tools/check-row-fragments.py [--rows DIR] [--quiet]
  python3 -B tools/check-row-fragments.py --selftest

Scan mode prints one `FRAG: <file>:<label>: <finding>` line per finding and a
summary `FRAG: k finding(s) in m file(s)`; exit 0 when k == 0, 1 otherwise,
2 on unreadable input. --selftest runs the fixture battery and exits 0 only
when every check kills its mutant and passes its neutral control.
"""
import argparse
import os
import re
import subprocess
import sys
import tempfile
import unicodedata
import urllib.parse

TEACHES_MAX = 240
EXPECTED_OPENED = "2026-10-24"
ENTRY = "corpus/knowledge/culture-material/games-play-sport-contests.md"
ROW_RE = re.compile(r"^\|\s*(S\d+)\s*\|")
URL_RE = re.compile(r"https?://[^\s<>\"|`]+")
CAPTURE_RE = re.compile(r"web\.archive\.org/web/(\d{14})id_/(\S+?)\s*[.;]?\s*$", re.IGNORECASE)
LABEL_RE = re.compile(r"^(ROW|BULLET|VERIFY|CAPTURE|ACCESS)[:=](.*)$")
NONWORD = re.compile(r"[\W_]+", re.UNICODE)


def norm_url(url):
    """Query-aware identity: query and fragment ignored (the round-64
    check-rows.py gap), host casefolded, www. stripped, default port
    dropped, path trailing slash stripped."""
    try:
        parts = urllib.parse.urlsplit(url.strip().rstrip(".,;'"))
    except ValueError:
        return url.strip().lower()
    scheme = parts.scheme.lower()
    host = (parts.hostname or "").lower()
    if host.startswith("www."):
        host = host[4:]
    try:
        port = parts.port
    except ValueError:
        port = None
    if port and not (scheme == "http" and port == 80) and not (scheme == "https" and port == 443):
        host = f"{host}:{port}"
    path = parts.path or "/"
    if path != "/" and path.endswith("/"):
        path = path[:-1]
    return f"{scheme}://{host}{path}"


def norm_words(text):
    folded = unicodedata.normalize("NFKC", text).casefold()
    return [w for w in NONWORD.sub(" ", folded).split() if w]


def cells(line):
    return [c.strip() for c in line.split("|")[1:-1]] if line.startswith("|") else []


def parse_fragment(text):
    """Return {label: value} for labelled lines; ROW may repeat (two rows
    per fragment file are not expected, but a repeated label is reported)."""
    out = {}
    repeats = []
    for line in text.splitlines():
        m = LABEL_RE.match(line.strip())
        if m:
            label, value = m.group(1), m.group(2).strip()
            if label in out:
                repeats.append(label)
            out[label] = value
    return out, repeats


def check_rows(rows_dir, entry=ENTRY):
    findings = []
    frag_files = []
    if not os.path.isdir(rows_dir):
        return [[rows_dir, "rows-dir", "missing"]], frag_files
    seen_urls = {}
    for dirpath, _dirnames, filenames in os.walk(rows_dir):
        for fn in sorted(filenames):
            # scan only row fragments; seat rejects/notes stay out of the scan
            if not (fn.startswith("row-") and fn.endswith(".txt")):
                continue
            path = os.path.join(dirpath, fn)
            rel = os.path.relpath(path, rows_dir)
            frag_files.append(rel)
            try:
                text = open(path, encoding="utf-8").read()
            except (OSError, UnicodeDecodeError) as error:
                findings.append([rel, "unreadable", str(error)])
                continue
            labels, repeats = parse_fragment(text)
            for label in repeats:
                findings.append([rel, "label-repeat", label])
            row = labels.get("ROW", "")
            if not row:
                findings.append([rel, "no-ROW", ""])
                continue
            cs = cells(row)
            sid = None
            m = ROW_RE.match(row)
            if m:
                sid = m.group(1)
            if len(cs) != 11:
                findings.append([rel, "cells", f"{sid or '?'}:{len(cs)}"])
                continue
            source, _kind, tier, _scope, anchor = cs[1], cs[2], cs[3], cs[4], cs[5]
            teaches, status, opened, _recheck, usedby = cs[6], cs[7], cs[8], cs[9], cs[10]
            if len(teaches) > TEACHES_MAX:
                findings.append([rel, "teaches-length", f"{sid}:{len(teaches)}>{TEACHES_MAX}"])
            if status != "mined":
                findings.append([rel, "status", f"{sid}:{status}"])
            if opened != EXPECTED_OPENED:
                findings.append([rel, "opened", f"{sid}:{opened}"])
            if entry not in usedby:
                findings.append([rel, "used-by", f"{sid}:{usedby[:60]}"])
            if tier not in ("A", "B"):
                findings.append([rel, "tier", f"{sid}:{tier}"])
            urls = URL_RE.findall(source)
            cap = CAPTURE_RE.search(source)
            if not urls:
                findings.append([rel, "no-live-url", sid or "?"])
            else:
                live_norm = norm_url(urls[0])
                if live_norm in seen_urls:
                    findings.append([rel, "dup-url", f"{sid}:{live_norm} also {seen_urls[live_norm]}"])
                else:
                    seen_urls[live_norm] = sid or rel
            if not cap:
                findings.append([rel, "no-capture", sid or "?"])
            elif urls and norm_url(cap.group(2)) != norm_url(urls[0]):
                findings.append([rel, "capture-url-mismatch",
                                 f"{sid}:{norm_url(cap.group(2))} != {norm_url(urls[0])}"])
            qm = re.search(r'"([^"]+)"|“([^“”]+)”', anchor)
            quote = (qm.group(1) or qm.group(2)) if qm else None
            qw = norm_words(quote) if quote else []
            if not (8 <= len(qw) <= 25):
                findings.append([rel, "quote-words", f"{sid}:{len(qw)}"])
            bullet = labels.get("BULLET", "")
            bw = [w for w in norm_words(bullet) if len(w) >= 4]
            if bullet and len(bw) < 6:
                findings.append([rel, "bullet-words", f"{sid}:{len(bw)}"])
    return findings, frag_files


SELFTEST_DIR_NOTE = "selftest fixtures are built in a temporary directory"


def selftest():
    checks = []

    def build(rows):
        tmp = tempfile.mkdtemp(prefix="frag-selftest-")
        for name, text in rows.items():
            path = os.path.join(tmp, name)
            os.makedirs(os.path.dirname(path), exist_ok=True)
            open(path, "w", encoding="utf-8").write(text)
        return tmp

    def frag(sid, url, teaches, status="mined", opened=EXPECTED_OPENED,
             usedby=ENTRY, anchor='"word one two three four five six seven eight"',
             capture_path=None):
        cap_path = capture_path if capture_path is not None else urllib.parse.urlsplit(url).path
        return (f"ROW=| {sid} | Example Source — {url} ; "
                f"web.archive.org/web/20260101000000id_/{urllib.parse.urlsplit(url).scheme}://"
                f"{urllib.parse.urlsplit(url).netloc}{cap_path} . | docs | A | scope | "
                f"{anchor} | {teaches} | {status} | {opened} | 180d | {usedby} |\n"
                f"BULLET=independent clause words restated in present context here\n"
                f"VERIFY=ok\nCAPTURE=ok\nACCESS=ok\n")

    # 1. neutral: two clean rows pass
    tmp = build({
        "SeatA/row-main.txt": frag("S750", "https://Example.ORG/path/", "a short teaches cell"),
        "SeatB/row-main.txt": frag("S751", "https://other.net/x?p=1", "another short teaches cell",
                              capture_path="/x"),
    })
    f, files = check_rows(tmp)
    checks.append(("neutral-clean", not f, f))
    # 2. teaches-length mutant killed
    tmp = build({"SeatA/row-main.txt": frag("S750", "https://a.example/x", "x" * (TEACHES_MAX + 1))})
    f, _ = check_rows(tmp)
    checks.append(("teaches-length-kill", any(x[1] == "teaches-length" for x in f), f))
    # 3. query-only duplicate killed (query-aware normalization)
    tmp = build({
        "SeatA/row-main.txt": frag("S750", "https://a.example/x?q=1", "short one"),
        "SeatB/row-main.txt": frag("S751", "https://a.example/x?q=2", "short two"),
    })
    f, _ = check_rows(tmp)
    checks.append(("query-dup-kill", any(x[1] == "dup-url" for x in f), f))
    # 4. fragment-only twin is also a duplicate (fragment ignored by identity)
    tmp = build({
        "SeatA/row-main.txt": frag("S750", "https://a.example/x", "short one"),
        "SeatB/row-main.txt": frag("S751", "https://a.example/x#frag", "short two"),
    })
    f, _ = check_rows(tmp)
    checks.append(("fragment-twin-dup-kill", any(x[1] == "dup-url" for x in f), f))
    # 4b. genuinely distinct paths: no duplicate, no false positive
    tmp = build({
        "SeatA/row-main.txt": frag("S750", "https://a.example/x", "short one"),
        "SeatB/row-main.txt": frag("S751", "https://a.example/y", "short two"),
    })
    f, _ = check_rows(tmp)
    checks.append(("distinct-path-no-fp", not any(x[1] == "dup-url" for x in f), f))
    # 5. capture-original mismatch killed (capture path differs)
    tmp = build({"SeatA/row-main.txt": frag("S750", "https://a.example/x", "short one",
                                       capture_path="/y")})
    f, _ = check_rows(tmp)
    checks.append(("capture-mismatch-kill", any(x[1] == "capture-url-mismatch" for x in f), f))
    # 6. www/trailing-slash/case normalization: same host, no false dup
    tmp = build({
        "SeatA/row-main.txt": frag("S750", "https://www.a.example/x/", "short one"),
        "SeatB/row-main.txt": frag("S751", "https://A.example/x", "short two"),
    })
    f, _ = check_rows(tmp)
    checks.append(("host-norm-no-fp", any(x[1] == "dup-url" for x in f), f))
    # 7. status/opened/used-by mutants killed
    tmp = build({"SeatA/row-main.txt": frag("S750", "https://a.example/x", "short one",
                                       status="queued", opened="2026-10-23", usedby="—")})
    kinds = {x[1] for x in check_rows(tmp)[0]}
    checks.append(("cell-mutants-kill", {"status", "opened", "used-by"} <= kinds, kinds))
    # 8. short quote killed
    tmp = build({"SeatA/row-main.txt": frag("S750", "https://a.example/x", "short one",
                                       anchor='"tiny quote"')})
    f, _ = check_rows(tmp)
    checks.append(("quote-kill", any(x[1] == "quote-words" for x in f), f))
    # 9. bad cell count killed
    tmp = build({"SeatA/row-main.txt": "ROW=| S750 | only | few |\nBULLET=x\n"})
    f, _ = check_rows(tmp)
    checks.append(("cells-kill", any(x[1] == "cells" for x in f), f))

    bad = []
    for name, ok, detail in checks:
        print(f"SELFTEST {name}: {'PASS' if ok else 'FAIL'} {detail if not ok else ''}")
        if not ok:
            bad.append(name)
    print(f"SELFTEST: {'PASS' if not bad else 'FAIL'} {len(checks) - len(bad)}/{len(checks)}")
    return 0 if not bad else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--rows", default=".ufo/waves/round-65/rows")
    ap.add_argument("--quiet", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.selftest:
        return selftest()
    try:
        findings, files = check_rows(os.path.abspath(args.rows))
    except OSError as error:
        print(f"FRAG_ERROR {error}", file=sys.stderr)
        return 2
    for rel, kind, detail in findings:
        print(f"FRAG: {rel}:{kind}: {detail}")
    if not args.quiet:
        print(f"FRAG: {len(findings)} finding(s) in {len(files)} file(s)")
    return 0 if not findings else 1


if __name__ == "__main__":
    sys.exit(main())
