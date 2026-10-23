#!/usr/bin/env python3
r"""Round-62 claim O acceptance (operability, capability acquisition): a lane tool
tools/reopen-row.py that re-opens SOURCES rows with a bounded retry, an archived-copy fallback and a
body-versus-caption verdict (QUALITY criterion 13's treatment made runnable; the S671 transient miss
and the S665 caption-only quote of round 61). Run from the lane root:

  python3 -B reports/round-62/accept-o.py [--root DIR]

Tool contract (what the legs check):
  python3 -B tools/reopen-row.py [--registry PATH] [--passes N] [--gap SECONDS] [--allow-private] ID...
  - A row is a `| S### |` line of the registry (default corpus/SOURCES.md, relative to the working
    directory); split on `|`, cell 2 is the source cell, cell 6 the anchor cell. The row's URLs are
    the http(s) URLs of the source cell in order (trailing `.,;:'` and an unbalanced `)` trimmed); its
    quote is the first double-quoted span ("..." or curly) of the anchor cell.
  - Text match: NFKC, casefold, every run of non-word characters or `_` to one space; the quote's
    normalised words must occur as a contiguous whole-word run in the normalised text.
  - HTML is split into BODY text (text nodes outside script, style, noscript, template, figcaption
    and any element whose class or id contains `caption`, case-insensitive, with its descendants) and
    CAPTION text (text inside figcaption or a `caption` class/id element, plus the values of alt,
    title, aria-label, content and every data-* attribute). Script/style text is neither. A non-HTML
    body (text/plain, JSON) is BODY text as a whole.
  - Fetch: GET, timeout 30 s. A transient result is HTTP 429, any 5xx, a timeout or a connection
    error; it is retried up to 3 attempts per URL per pass, waiting min(gap, 5) s between attempts.
    Any other HTTP error ends that URL for the pass after one attempt. Without --allow-private a URL
    whose host is or resolves to a loopback, private, link-local, reserved or unspecified address, or
    does not resolve, is refused without a request.
  - A pass tries the row's URLs in order and stops at the first BODY match. Pass verdict: LOCATED
    (a BODY match), else CAPTION_ONLY (a CAPTION match on a fetched page), else ABSENT (some URL
    answered 2xx), else REFUSED (every URL refused), else UNREACHABLE. Another pass runs, after gap
    seconds, only when the pass was not LOCATED and some URL in it ended on a transient result, up
    to --passes passes (default 3; --gap default 60). The row verdict is the best pass verdict in the
    order LOCATED > CAPTION_ONLY > ABSENT > UNREACHABLE > REFUSED.
  - NO_ROW: no registry row; NO_QUOTE: no quote, a quote under 8 normalised words, or no URL (no
    request is made for either).
  - Output: one line per ID in argument order, `ROW <ID> <VERDICT> attempts=<n> url=<url or ->` (n =
    HTTP requests and connection attempts made for that row over all passes; url = the URL that gave
    the verdict's match, else `-`), then `REOPEN: <k>/<m> located`. Exit 0 when every row is
    LOCATED, 1 otherwise, 2 on an input error (no ID, unreadable or invalid UTF-8 registry, a
    --passes that is not an integer >= 1, a --gap that is not a number >= 0) with a line starting
    `REOPEN_ERROR` and no traceback.

Legs, each printed PASS or FAIL:
  TOOL     tools/reopen-row.py exists at --root (it does not at the round base d42ffb89)
  INDEP    the tool's text names none of `reports/`, `accept-o`, `round-62`; every run below uses a
           copy of the tool in a fresh temporary directory (cwd there), never the lane path
  GEN      on a run-time random fixture (random S-ids, paths, vocabulary and quotes; 2 rows per class,
           shuffled; one local HTTP server; `--passes 3 --gap 0 --allow-private`) every ROW line's
           VERDICT and attempts= equal the class expectation (CLASSES below) and the summary reads
           `REOPEN: <k>/<m> located` with the true k and m
  ORDER    the ROW lines appear exactly once per ID, in argument order
  BOUND    the server's per-path request counts equal the class expectation (a retry bound that is
           neither skipped nor exceeded)
  EXIT     the GEN run exits 1; a run on four BODY-class rows exits 0 with `REOPEN: 4/4 located`
  PRIV     without --allow-private, three BODY-class rows on the local server print REFUSED
           attempts=0, the server sees 0 requests, exit 1
  DEFAULT  one DEAD row with no --passes/--gap prints UNREACHABLE attempts=9 within 100-600 s of wall
           time (three passes, two 60 s gaps)
  ERR      no ID, a missing registry, an invalid UTF-8 registry, `--passes 0`, `--gap x`: each exit 2,
           a REOPEN_ERROR line, no `Traceback` on stderr
Frozen predicate (the same sentence in reports/round-62/claims.json and in every receipt):
  ACCEPT-O-62: every leg above prints PASS.
Exit 0 only when every leg passes; 1 when any leg fails; 2 on unreadable input.
Review-only: the tool's behaviour on live pages (e.g. S665 caption, S671 Wayback) is a wave-2 review
item, never a leg (no live fetch decides this claim).
"""
import argparse
import http.server
import os
import random
import re
import shutil
import socket
import subprocess
import sys
import tempfile
import threading
import time

TOOL = "tools/reopen-row.py"
ROWLINE = re.compile(r"^ROW (S\d+) (\w+) attempts=(\d+) url=(\S+)$")

# class -> (expected verdict, expected attempts, expected hits per path role)
CLASSES = {
    "BODY": ("LOCATED", 1, {"live": 1}),
    "BODY_SPLIT": ("LOCATED", 1, {"live": 1}),
    "PLAIN": ("LOCATED", 1, {"live": 1}),
    "CAP_FIG": ("CAPTION_ONLY", 1, {"live": 1}),
    "CAP_ATTR": ("CAPTION_ONLY", 1, {"live": 1}),
    "CAP_CLASS": ("CAPTION_ONLY", 1, {"live": 1}),
    "SCRIPT": ("ABSENT", 1, {"live": 1}),
    "ABSENT": ("ABSENT", 1, {"live": 1}),
    "TRANSIENT2": ("LOCATED", 3, {"live": 3}),
    "TRANSIENT_PASS": ("LOCATED", 4, {"live": 4}),
    "DEAD_ARCHIVE": ("LOCATED", 2, {"live": 1, "arch": 1}),
    "ARCHIVE_CAPTION": ("CAPTION_ONLY", 2, {"live": 1, "arch": 1}),
    "DEAD": ("UNREACHABLE", 9, {"live": 9}),
    "GONE": ("UNREACHABLE", 1, {"live": 1}),
    "DEAD_THEN_BODY2": ("LOCATED", 4, {"live": 3, "arch": 1}),
    "NOQUOTE": ("NO_QUOTE", 0, {"live": 0}),
    "SHORT": ("NO_QUOTE", 0, {"live": 0}),
    "NOROW": ("NO_ROW", 0, {}),
}


class Fixture:
    def __init__(self, rng):
        self.rng = rng
        self.routes = {}  # path -> (statuses list, body bytes, ctype)
        self.hits = {}
        self.lock = threading.Lock()
        fixture = self

        class Handler(http.server.BaseHTTPRequestHandler):
            def do_GET(self):
                with fixture.lock:
                    n = fixture.hits.get(self.path, 0)
                    fixture.hits[self.path] = n + 1
                    route = fixture.routes.get(self.path)
                if route is None:
                    self.send_response(404)
                    self.end_headers()
                    return
                statuses, body, ctype = route
                status = statuses[min(n, len(statuses) - 1)]
                self.send_response(status)
                self.send_header("Content-Type", ctype)
                payload = body if status == 200 else b"<html><body><p>error page</p></body></html>"
                self.send_header("Content-Length", str(len(payload)))
                self.end_headers()
                self.wfile.write(payload)

            def log_message(self, *args):
                pass

        self.server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        self.port = self.server.server_address[1]
        threading.Thread(target=self.server.serve_forever, daemon=True).start()

    def word(self):
        return "".join(self.rng.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(self.rng.randint(4, 9)))

    def words(self, n):
        return [self.word() for _ in range(n)]

    def path(self):
        return "/" + "/".join(self.word() for _ in range(self.rng.randint(1, 3)))

    def url(self, path):
        return f"http://127.0.0.1:{self.port}{path}"

    def close(self):
        self.server.shutdown()
        self.server.server_close()


def html(*parts):
    return ("<!doctype html><html><head><title>t</title></head><body>" + "".join(parts) + "</body></html>").encode()


def dead_port():
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    port = s.getsockname()[1]
    s.close()
    return port


def build(fx, cls, sid):
    """Returns (registry row line, {role: path}) for one fixture row of class cls."""
    rng = fx.rng
    qwords = fx.words(rng.randint(10, 16))
    quote = " ".join(qwords)
    shown = quote[0].upper() + quote[1:] + "."
    filler = " ".join(fx.words(30)) + "."
    live, arch = fx.path(), None
    paths = {"live": live}
    ok_html = html(f"<p>{filler}</p><p>{shown}</p><p>{filler}</p>")
    if cls == "BODY":
        fx.routes[live] = ([200], ok_html, "text/html; charset=utf-8")
    elif cls == "BODY_SPLIT":
        cut = len(qwords) // 2
        mixed = " ".join(qwords[:cut]).upper() + ", <em>" + "</em> \u2014 <b>".join(qwords[cut:]) + "</b>!"
        fx.routes[live] = ([200], html(f"<p>{filler}</p><div><span>{mixed}</span></div>"), "text/html")
    elif cls == "PLAIN":
        fx.routes[live] = ([200], f"{filler}\n{shown}\n{filler}\n".encode(), "text/plain; charset=utf-8")
    elif cls == "CAP_FIG":
        fx.routes[live] = ([200], html(f"<p>{filler}</p><figure><img src='x.png'><figcaption>{shown}</figcaption></figure>"), "text/html")
    elif cls == "CAP_ATTR":
        attr = rng.choice(["alt", "title", "data-img-description", "aria-label"])
        fx.routes[live] = ([200], html(f"<p>{filler}</p><img src='x.png' {attr}=\"{shown}\">"), "text/html")
    elif cls == "CAP_CLASS":
        name = rng.choice(["thumbnail-caption", "wp-caption-text", "Caption"])
        fx.routes[live] = ([200], html(f"<p>{filler}</p><div class=\"{name}\"><span>{shown}</span></div>"), "text/html")
    elif cls == "SCRIPT":
        fx.routes[live] = ([200], html(f"<p>{filler}</p><script>var t = \"{shown}\";</script>"), "text/html")
    elif cls == "ABSENT":
        fx.routes[live] = ([200], html(f"<p>{filler}</p><p>{' '.join(qwords[:-3])} {fx.word()}.</p>"), "text/html")
    elif cls == "TRANSIENT2":
        fx.routes[live] = ([503, 503, 200], ok_html, "text/html")
    elif cls == "TRANSIENT_PASS":
        fx.routes[live] = ([503, 502, 429, 200], ok_html, "text/html")
    elif cls in ("DEAD_ARCHIVE", "ARCHIVE_CAPTION", "DEAD_THEN_BODY2"):
        arch = f"/web/2025{rng.randint(10**9, 10**10 - 1)}id_/https://{fx.word()}.org{live}"
        paths["arch"] = arch
        if cls == "DEAD_ARCHIVE":
            fx.routes[live] = ([403], ok_html, "text/html")
            fx.routes[arch] = ([200], ok_html, "text/html")
        elif cls == "ARCHIVE_CAPTION":
            fx.routes[live] = ([410], ok_html, "text/html")
            fx.routes[arch] = ([200], html(f"<p>{filler}</p><figure><figcaption>{shown}</figcaption></figure>"), "text/html")
        else:
            fx.routes[live] = ([500], ok_html, "text/html")
            fx.routes[arch] = ([200], ok_html, "text/html")
    elif cls == "DEAD":
        fx.routes[live] = ([503], ok_html, "text/html")
    elif cls == "GONE":
        fx.routes[live] = ([404], ok_html, "text/html")
    elif cls in ("NOQUOTE", "SHORT"):
        fx.routes[live] = ([200], ok_html, "text/html")
    urls = fx.url(live) + (f" ; capture {fx.url(arch)}" if arch else "")
    anchor = f"section {fx.word()}: \"{shown}\""
    if cls == "NOQUOTE":
        anchor = f"section {fx.word()}, no quoted span"
    elif cls == "SHORT":
        anchor = f"section {fx.word()}: \"{' '.join(qwords[:5])}\""
    row = (f"| {sid} | {fx.word().title()} page, Fixture Press, 2025 \u2014 {urls}. | docs | B | scope {fx.word()} | "
           f"{anchor} | teaches {fx.word()} | mined | 2026-10-23 | 180d | corpus/knowledge/x.md |")
    return row, paths


def run_tool(tool, cwd, args, timeout=900):
    t0 = time.monotonic()
    try:
        done = subprocess.run([sys.executable, "-B", tool] + args, cwd=cwd, capture_output=True, timeout=timeout)
        return done.returncode, done.stdout.decode("utf-8", "replace"), done.stderr.decode("utf-8", "replace"), time.monotonic() - t0
    except subprocess.TimeoutExpired:
        return None, "", "TIMEOUT", time.monotonic() - t0


def parse(out):
    rows = []
    for line in out.splitlines():
        m = ROWLINE.match(line.strip())
        if m:
            rows.append((m.group(1), m.group(2), int(m.group(3))))
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    root = os.path.abspath(ap.parse_args().root)
    legs = []

    def leg(name, ok, detail):
        legs.append(ok)
        print(f"{name} {'PASS' if ok else 'FAIL'} {detail}")

    src = os.path.join(root, TOOL)
    have = os.path.isfile(src)
    leg("TOOL", have, f"path={TOOL} exists={have}")
    if not have:
        for name in ("INDEP", "GEN", "ORDER", "BOUND", "EXIT", "PRIV", "DEFAULT", "ERR"):
            leg(name, False, "no tool")
        print("ACCEPT-O-62: FAIL")
        return 1
    try:
        text = open(src, encoding="utf-8").read()
    except (OSError, UnicodeDecodeError) as error:
        print(f"ACCEPT_O_INPUT_ERROR {error}", file=sys.stderr)
        return 2
    named = [s for s in ("reports/", "accept-o", "round-62") if s in text]
    leg("INDEP", not named, f"named={named}")

    rng = random.SystemRandom()
    work = tempfile.mkdtemp(prefix="accept-o-62-")
    tool = os.path.join(work, "reopen-row.py")
    shutil.copyfile(src, tool)
    fx = Fixture(rng)
    try:
        used = set()

        def fresh_id():
            while True:
                sid = f"S{rng.randint(1000, 9999)}"
                if sid not in used:
                    used.add(sid)
                    return sid

        plan = [c for c in CLASSES for _ in range(2)]
        rng.shuffle(plan)
        lines, expect, roles = ["# fixture registry", "", "| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |", "|---|---|---|---|---|---|---|---|---|---|---|"], [], {}
        for cls in plan:
            sid = fresh_id()
            if cls == "NOROW":
                expect.append((sid, cls))
                continue
            row, paths = build(fx, cls, sid)
            lines.append(row)
            expect.append((sid, cls))
            roles[sid] = paths
        # a DEAD row whose live URL is a closed port (connection errors are transient)
        port_sid = fresh_id()
        qwords = fx.words(12)
        lines.append(f"| {port_sid} | Closed port page \u2014 http://127.0.0.1:{dead_port()}{fx.path()} | docs | B | s | "
                     f"anchor: \"{' '.join(qwords)}\" | t | mined | 2026-10-23 | 180d | x |")
        expect.append((port_sid, "DEAD_PORT"))
        reg = os.path.join(work, "SOURCES.md")
        open(reg, "w", encoding="utf-8").write("\n".join(lines) + "\n")
        ids = [s for s, _ in expect]
        code, out, err, _ = run_tool(tool, work, ["--registry", reg, "--passes", "3", "--gap", "0", "--allow-private"] + ids)
        got = parse(out)
        by = {}
        for sid, verdict, n in got:
            by.setdefault(sid, []).append((verdict, n))
        wrong = []
        located = 0
        for sid, cls in expect:
            want_v, want_n = ("UNREACHABLE", 9) if cls == "DEAD_PORT" else CLASSES[cls][:2]
            located += want_v == "LOCATED"
            seen = by.get(sid, [])
            if len(seen) != 1 or seen[0] != (want_v, want_n):
                wrong.append(f"{cls}:{sid}:want={want_v}/{want_n}:got={seen}")
        summary = f"REOPEN: {located}/{len(expect)} located"
        leg("GEN", not wrong and summary in out.splitlines(),
            f"rows={len(expect)} wrong={len(wrong)} {wrong[:6]} summary_ok={summary in out.splitlines()} exit={code}")
        leg("ORDER", [s for s, _, _ in got] == ids, f"printed={len(got)} expected={len(ids)}")
        bound_bad = []
        for sid, cls in expect:
            if cls in ("NOROW", "DEAD_PORT"):
                continue
            for role, want in CLASSES[cls][2].items():
                hit = fx.hits.get(roles[sid][role], 0)
                if hit != want:
                    bound_bad.append(f"{cls}:{role}:want={want}:hits={hit}")
        leg("BOUND", not bound_bad, f"bad={bound_bad[:8]}")

        body_ids, body_lines = [], ["| id | source |"]
        for _ in range(4):
            sid = fresh_id()
            row, _ = build(fx, "BODY", sid)
            body_lines.append(row)
            body_ids.append(sid)
        reg2 = os.path.join(work, "BODY.md")
        open(reg2, "w", encoding="utf-8").write("\n".join(body_lines) + "\n")
        code2, out2, _, _ = run_tool(tool, work, ["--registry", reg2, "--passes", "3", "--gap", "0", "--allow-private"] + body_ids)
        leg("EXIT", code == 1 and code2 == 0 and "REOPEN: 4/4 located" in out2.splitlines(),
            f"gen_exit={code} body_exit={code2}")

        priv_ids, priv_lines, priv_paths = [], ["| id | source |"], []
        for _ in range(3):
            sid = fresh_id()
            row, paths = build(fx, "BODY", sid)
            priv_lines.append(row)
            priv_ids.append(sid)
            priv_paths.append(paths["live"])
        reg3 = os.path.join(work, "PRIV.md")
        open(reg3, "w", encoding="utf-8").write("\n".join(priv_lines) + "\n")
        code3, out3, _, _ = run_tool(tool, work, ["--registry", reg3, "--passes", "3", "--gap", "0"] + priv_ids)
        pgot = parse(out3)
        leg("PRIV", code3 == 1 and [(s, v, n) for s, v, n in pgot] == [(s, "REFUSED", 0) for s in priv_ids]
            and all(fx.hits.get(p, 0) == 0 for p in priv_paths), f"exit={code3} rows={pgot}")

        dsid = fresh_id()
        drow, dpaths = build(fx, "DEAD", dsid)
        reg4 = os.path.join(work, "DEAD.md")
        open(reg4, "w", encoding="utf-8").write("| id | source |\n" + drow + "\n")
        code4, out4, _, wall = run_tool(tool, work, ["--registry", reg4, "--allow-private", dsid], timeout=900)
        dgot = parse(out4)
        leg("DEFAULT", dgot == [(dsid, "UNREACHABLE", 9)] and 100 <= wall <= 600 and fx.hits.get(dpaths["live"], 0) == 9,
            f"rows={dgot} wall={wall:.0f}s hits={fx.hits.get(dpaths['live'], 0)} exit={code4}")

        bad_utf = os.path.join(work, "BAD.md")
        open(bad_utf, "wb").write(b"| S1234 | \xff\xfe bad |\n")
        cases = {
            "no-id": ["--registry", reg],
            "missing": ["--registry", os.path.join(work, "nope.md"), "S1000"],
            "badutf8": ["--registry", bad_utf, "S1234"],
            "passes0": ["--registry", reg, "--passes", "0", ids[0]],
            "gapx": ["--registry", reg, "--gap", "x", ids[0]],
        }
        err_bad = []
        for name, args in cases.items():
            c, o, e, _ = run_tool(tool, work, args, timeout=120)
            if c != 2 or "REOPEN_ERROR" not in (o + e) or "Traceback" in e:
                err_bad.append(f"{name}:exit={c}")
        leg("ERR", not err_bad, f"bad={err_bad}")
    finally:
        fx.close()
        shutil.rmtree(work, ignore_errors=True)
    verdict = all(legs)
    print(f"ACCEPT-O-62: {'PASS' if verdict else 'FAIL'}")
    return 0 if verdict else 1


if __name__ == "__main__":
    sys.exit(main())
