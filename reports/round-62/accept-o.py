#!/usr/bin/env python3
r"""Round-62 claim O acceptance, revision 1 (before any data: DEFAULT checks exit, summary and the
request schedule; GEN checks url=; EXIT adds the default registry path; CriticClaims finding 3.
ORDER repeats IDs (CtlOOrderErr). MutCounterO: the dead port stays reserved, BODY_SPLIT is balanced,
CAP_ATTR covers alt, title, data-*, aria-label and meta content, ERR anchors REOPEN_ERROR and reads
both streams, and tool runs own a process group).
Claim O (operability, capability acquisition): a lane tool
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
    and any element whose class or id contains `caption`, `thumbnail` or `gallery` (revision 1: S665's
    quote sits in a `<p class="thumbnail-description">` gallery overlay, ExecReopenTool live run),
    case-insensitive, with its descendants) and
    CAPTION text (text inside figcaption or a `caption`/`thumbnail`/`gallery` class/id element, plus the values of alt,
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
           VERDICT and attempts= equal the class expectation (CLASSES below), its url= is the URL
           that matched (live or capture, per class) for LOCATED/CAPTION_ONLY and `-` otherwise
           (revision 1), and the summary reads `REOPEN: <k>/<m> located` with the true k and m
  ORDER    the ROW lines appear exactly once per ID, in argument order; revision 1 (CtlOOrderErr met
           revision 0 with a de-duplicating tool): a run whose arguments repeat IDs (a b a c b) prints
           one ROW line per argument, in argument order
  BOUND    the server's per-path request counts equal the class expectation (a retry bound that is
           neither skipped nor exceeded); revision 1 (CtlOUnbounded met revision 0 by fetching every URL
           after a BODY match and by requesting an unlisted URL): class BODY_THEN_ARCHIVE expects 0
           requests to its listed capture, and the server must see no request to an unlisted path
           (requests to other hosts are not observable here: review-only)
  EXIT     the GEN run exits 1; a run on four BODY-class rows exits 0 with `REOPEN: 4/4 located`;
           (revision 1) the same four-row check passes with no --registry, the rows placed at
           corpus/SOURCES.md under the tool's working directory (the default registry path)
  PRIV     without --allow-private, three BODY-class rows on the local server print REFUSED
           attempts=0, the server sees 0 requests, exit 1
  DEFAULT  one DEAD row with no --passes/--gap prints UNREACHABLE attempts=9 within 100-600 s of wall
           time (three passes, two 60 s gaps); revision 1: exits 1, prints `REOPEN: 0/1 located`, and
           the server's nine request times form exactly three bursts of three (consecutive requests
           within a burst 4-10 s apart (revision 1: CtlONoRetry met revision 0 with no wait between attempts); the first request of each later burst >= 55 s after the last
           request of the burst before and <= 75 s after it; CtlODefault met the 55 s floor alone with a
           200 s default gap)
  ERR      no ID, a missing registry, an invalid UTF-8 registry, `--passes 0`, `--gap x`: each exit 2,
           a line starting REOPEN_ERROR (stdout or stderr), no `Traceback` on either stream (revision 1)
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
import signal
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
    "CAP_ATTR_TITLE": ("CAPTION_ONLY", 1, {"live": 1}),
    "CAP_ATTR_DATA": ("CAPTION_ONLY", 1, {"live": 1}),
    "CAP_ATTR_ARIA": ("CAPTION_ONLY", 1, {"live": 1}),
    "CAP_ATTR_META": ("CAPTION_ONLY", 1, {"live": 1}),
    "CAP_CLASS": ("CAPTION_ONLY", 1, {"live": 1}),
    "CAP_CLASS_THUMB": ("CAPTION_ONLY", 1, {"live": 1}),
    "CAP_CLASS_GALLERY": ("CAPTION_ONLY", 1, {"live": 1}),
    "CAP_ID": ("CAPTION_ONLY", 1, {"live": 1}),
    "SCRIPT": ("ABSENT", 1, {"live": 1}),
    "ABSENT": ("ABSENT", 1, {"live": 1}),
    "TRANSIENT2": ("LOCATED", 3, {"live": 3}),
    "TRANSIENT_PASS": ("LOCATED", 4, {"live": 4}),
    "DEAD_ARCHIVE": ("LOCATED", 2, {"live": 1, "arch": 1}),
    "ARCHIVE_CAPTION": ("CAPTION_ONLY", 2, {"live": 1, "arch": 1}),
    "DEAD": ("UNREACHABLE", 9, {"live": 9}),
    "GONE": ("UNREACHABLE", 1, {"live": 1}),
    "DEAD_THEN_BODY2": ("LOCATED", 4, {"live": 3, "arch": 1}),
    "BODY_THEN_ARCHIVE": ("LOCATED", 1, {"live": 1, "arch": 0}),
    "NOQUOTE": ("NO_QUOTE", 0, {"live": 0}),
    "SHORT": ("NO_QUOTE", 0, {"live": 0}),
    "NOROW": ("NO_ROW", 0, {}),
}


class Fixture:
    def __init__(self, rng):
        self.rng = rng
        self.routes = {}  # path -> (statuses list, body bytes, ctype)
        self.hits = {}
        self.times = {}
        self.lock = threading.Lock()
        fixture = self

        class Handler(http.server.BaseHTTPRequestHandler):
            def do_GET(self):
                with fixture.lock:
                    n = fixture.hits.get(self.path, 0)
                    fixture.hits[self.path] = n + 1
                    fixture.times.setdefault(self.path, []).append(time.monotonic())
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


RESERVED = []


def dead_port():
    """A port bound but never listening, held until the counter exits: connections are refused
    (revision 1, MutCounterO: a closed port could be re-bound by another process)."""
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    RESERVED.append(s)
    return s.getsockname()[1]


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
        mixed = " ".join(qwords[:cut]).upper() + ", " + " \u2014 ".join(f"<b>{w}</b>" for w in qwords[cut:]) + "!"
        fx.routes[live] = ([200], html(f"<p>{filler}</p><div><span>{mixed}</span></div>"), "text/html")
    elif cls == "PLAIN":
        fx.routes[live] = ([200], f"{filler}\n{shown}\n{filler}\n".encode(), "text/plain; charset=utf-8")
    elif cls == "CAP_FIG":
        fx.routes[live] = ([200], html(f"<p>{filler}</p><figure><img src='x.png'><figcaption>{shown}</figcaption></figure>"), "text/html")
    elif cls.startswith("CAP_ATTR"):
        attr = {"CAP_ATTR": "alt", "CAP_ATTR_TITLE": "title", "CAP_ATTR_DATA": "data-img-description",
                "CAP_ATTR_ARIA": "aria-label"}.get(cls)
        if cls == "CAP_ATTR_META":
            body = ("<!doctype html><html><head><meta name=\"description\" content=\"" + shown + "\"></head><body><p>"
                    + filler + "</p></body></html>").encode()
        else:
            body = html(f"<p>{filler}</p><img src='x.png' {attr}=\"{shown}\">")
        fx.routes[live] = ([200], body, "text/html")
    elif cls.startswith("CAP_CLASS") or cls == "CAP_ID":
        attr = {"CAP_CLASS": 'class="wp-caption-text"', "CAP_CLASS_THUMB": 'class="thumbnail-description"',
                "CAP_CLASS_GALLERY": 'class="Gallery-item"', "CAP_ID": 'id="figCaption1"'}[cls]
        fx.routes[live] = ([200], html(f"<p>{filler}</p><div {attr}><span>{shown}</span></div>"), "text/html")
    elif cls == "SCRIPT":
        fx.routes[live] = ([200], html(f"<p>{filler}</p><script>var t = \"{shown}\";</script>"), "text/html")
    elif cls == "ABSENT":
        fx.routes[live] = ([200], html(f"<p>{filler}</p><p>{' '.join(qwords[:-3])} {fx.word()}.</p>"), "text/html")
    elif cls == "TRANSIENT2":
        fx.routes[live] = ([503, 503, 200], ok_html, "text/html")
    elif cls == "TRANSIENT_PASS":
        fx.routes[live] = ([503, 502, 429, 200], ok_html, "text/html")
    elif cls in ("DEAD_ARCHIVE", "ARCHIVE_CAPTION", "DEAD_THEN_BODY2", "BODY_THEN_ARCHIVE"):
        arch = f"/web/2025{rng.randint(10**9, 10**10 - 1)}id_/https://{fx.word()}.org{live}"
        paths["arch"] = arch
        if cls == "DEAD_ARCHIVE":
            fx.routes[live] = ([403], ok_html, "text/html")
            fx.routes[arch] = ([200], ok_html, "text/html")
        elif cls == "BODY_THEN_ARCHIVE":
            fx.routes[live] = ([200], ok_html, "text/html")
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
    """Runs the tool copy in its own process group; on timeout the whole group is killed (revision 1)."""
    t0 = time.monotonic()
    proc = subprocess.Popen([sys.executable, "-B", tool] + args, cwd=cwd, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE, start_new_session=True)
    try:
        out, err = proc.communicate(timeout=timeout)
        return proc.returncode, out.decode("utf-8", "replace"), err.decode("utf-8", "replace"), time.monotonic() - t0
    except subprocess.TimeoutExpired:
        os.killpg(proc.pid, signal.SIGKILL)
        proc.communicate()
        return None, "", "TIMEOUT", time.monotonic() - t0


def parse(out, with_url=False):
    rows = []
    for line in out.splitlines():
        m = ROWLINE.match(line.strip())
        if m:
            rows.append((m.group(1), m.group(2), int(m.group(3))) + ((m.group(4),) if with_url else ()))
    return rows


MATCH_ROLE = {"BODY": "live", "BODY_SPLIT": "live", "PLAIN": "live", "CAP_FIG": "live", "CAP_ATTR": "live",
              "CAP_ATTR_TITLE": "live", "CAP_ATTR_DATA": "live", "CAP_ATTR_ARIA": "live", "CAP_ATTR_META": "live",
              "CAP_CLASS": "live", "CAP_CLASS_THUMB": "live", "CAP_CLASS_GALLERY": "live", "CAP_ID": "live", "TRANSIENT2": "live", "TRANSIENT_PASS": "live", "DEAD_ARCHIVE": "arch",
              "ARCHIVE_CAPTION": "arch", "DEAD_THEN_BODY2": "arch", "BODY_THEN_ARCHIVE": "live"}


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
        urls = {}
        for sid, _, _, u in parse(out, with_url=True):
            urls.setdefault(sid, []).append(u)
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
            want_u = fx.url(roles[sid][MATCH_ROLE[cls]]) if cls in MATCH_ROLE else "-"
            if urls.get(sid) != [want_u]:
                wrong.append(f"{cls}:{sid}:url_want={want_u}:got={urls.get(sid)}")
        summary = f"REOPEN: {located}/{len(expect)} located"
        leg("GEN", not wrong and summary in out.splitlines(),
            f"rows={len(expect)} wrong={len(wrong)} {wrong[:6]} summary_ok={summary in out.splitlines()} exit={code}")
        rep_ids, rep_lines = [], ["| id | source |"]
        for _ in range(3):
            sid = fresh_id()
            row, _ = build(fx, "BODY", sid)
            rep_lines.append(row)
            rep_ids.append(sid)
        reg_rep = os.path.join(work, "REPEAT.md")
        open(reg_rep, "w", encoding="utf-8").write("\n".join(rep_lines) + "\n")
        rep_args = [rep_ids[0], rep_ids[1], rep_ids[0], rep_ids[2], rep_ids[1]]
        _, out_rep, _, _ = run_tool(tool, work, ["--registry", reg_rep, "--passes", "3", "--gap", "0", "--allow-private"] + rep_args)
        rep_got = [s for s, _, _ in parse(out_rep)]
        leg("ORDER", [s for s, _, _ in got] == ids and rep_got == rep_args,
            f"printed={len(got)} expected={len(ids)} repeated_args={len(rep_args)} repeated_printed={len(rep_got)}")
        bound_bad = []
        for sid, cls in expect:
            if cls in ("NOROW", "DEAD_PORT"):
                continue
            for role, want in CLASSES[cls][2].items():
                hit = fx.hits.get(roles[sid][role], 0)
                if hit != want:
                    bound_bad.append(f"{cls}:{role}:want={want}:hits={hit}")
        listed = {p for paths in roles.values() for p in paths.values()}
        unlisted = sorted(p for p in fx.hits if p not in listed and p not in fx.routes)
        leg("BOUND", not bound_bad and not unlisted, f"bad={bound_bad[:8]} unlisted_requests={unlisted[:5]}")

        body_ids, body_lines = [], ["| id | source |"]
        for _ in range(4):
            sid = fresh_id()
            row, _ = build(fx, "BODY", sid)
            body_lines.append(row)
            body_ids.append(sid)
        reg2 = os.path.join(work, "BODY.md")
        open(reg2, "w", encoding="utf-8").write("\n".join(body_lines) + "\n")
        code2, out2, _, _ = run_tool(tool, work, ["--registry", reg2, "--passes", "3", "--gap", "0", "--allow-private"] + body_ids)
        home = os.path.join(work, "home")
        os.makedirs(os.path.join(home, "corpus"))
        dflt_ids, dflt_lines = [], ["| id | source |"]
        for _ in range(4):
            sid = fresh_id()
            row, _ = build(fx, "BODY", sid)
            dflt_lines.append(row)
            dflt_ids.append(sid)
        open(os.path.join(home, "corpus", "SOURCES.md"), "w", encoding="utf-8").write("\n".join(dflt_lines) + "\n")
        code5, out5, _, _ = run_tool(tool, home, ["--passes", "3", "--gap", "0", "--allow-private"] + dflt_ids)
        leg("EXIT", code == 1 and code2 == 0 and "REOPEN: 4/4 located" in out2.splitlines()
            and code5 == 0 and "REOPEN: 4/4 located" in out5.splitlines(),
            f"gen_exit={code} body_exit={code2} default_registry_exit={code5}")

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
        stamps = sorted(fx.times.get(dpaths["live"], []))
        bursts = []
        for i, t in enumerate(stamps):
            if i and t - stamps[i - 1] <= 10:
                bursts[-1].append(t)
            else:
                bursts.append([t])
        sched = len(bursts) == 3 and all(len(b) == 3 for b in bursts) and \
            all(4 <= b[j + 1] - b[j] <= 10 for b in bursts for j in range(len(b) - 1)) and \
            all(55 <= bursts[k + 1][0] - bursts[k][-1] <= 75 for k in range(len(bursts) - 1))
        shape = [len(b) for b in bursts]
        gaps = [round(bursts[k + 1][0] - bursts[k][-1]) for k in range(len(bursts) - 1)]
        leg("DEFAULT", dgot == [(dsid, "UNREACHABLE", 9)] and 100 <= wall <= 600 and fx.hits.get(dpaths["live"], 0) == 9
            and code4 == 1 and "REOPEN: 0/1 located" in out4.splitlines() and sched,
            f"rows={dgot} wall={wall:.0f}s hits={fx.hits.get(dpaths['live'], 0)} exit={code4} bursts={shape} gaps={gaps}")

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
            if c != 2 or not any(l.startswith("REOPEN_ERROR") for l in (o + "\n" + e).splitlines()) \
                    or "Traceback" in (o + e):
                err_bad.append(f"{name}:exit={c}")
        leg("ERR", not err_bad, f"bad={err_bad}")
    finally:
        try:
            fx.close()
        finally:
            for sock in RESERVED:
                sock.close()
            shutil.rmtree(work, ignore_errors=True)
    verdict = all(legs)
    print(f"ACCEPT-O-62: {'PASS' if verdict else 'FAIL'}")
    return 0 if verdict else 1


if __name__ == "__main__":
    sys.exit(main())
