#!/usr/bin/env python3
r"""Round-63 claim O acceptance, revision 0 (before any data).

Claim O (operability, capability repair under the round-62 safety hold): the lane tool
tools/reopen-row.py is repaired so that the round-62 closure's routed defects are closed:
  1. (HIGH, gating) redirect targets are re-validated against the private-host refusal
     before they are requested.  Rule: when a response is a redirect, its Location is
     resolved (relative Locations against the current URL); if the target authority
     (lowercased host, effective port) differs from the current URL's authority, or when
     --allow-private is not set at all, the target must pass the same private-host
     refusal as a listed URL; a refused redirect ends that URL for the pass (with the
     requests already made counted as attempts).  At most 5 requests are made in one
     URL's redirect chain - the initial request plus follows - and a redirect received
     on the 5th response ends the URL for the pass as a fatal result.  A row whose every URL was pre-refused or died on a refused
     redirect, with no 2xx ever answered, prints REFUSED (attempts counts the requests
     that were actually made).
  2. a registry row whose URL is malformed - an unparseable port, an unbalanced
     bracketed IPv6 literal, or an empty host - prints `ROW <ID> MALFORMED attempts=0
     url=-`: no request is attempted for that URL, no traceback is shown, and the run's
     exit status is 1 (the registry is data, not invocation).  MALFORMED ranks below
     REFUSED.
  3. a response carrying Content-Encoding: gzip is decompressed before decoding and
     matching (so a gzipped body or caption is matched like a plain one).
  4. a body read that reaches the 4 MiB cap without EOF is not matched silently: when
     the quote is absent from the bytes actually read the verdict is TRUNCATED (ranked
     equal to ABSENT), when the quote is inside the read bytes the verdict is still
     LOCATED (or CAPTION_ONLY).  TRUNCATED prints `ROW <ID> TRUNCATED attempts=<n>
     url=-`.
  5. --timeout SECONDS (default 30, number > 0) is a per-request wall budget covering
     connect, headers and body: a body that stalls or drips cannot outlive the budget;
     expiry is a transient result (retried per the schedule).
  6. the round-62 behaviour is otherwise unchanged: verdict set (plus MALFORMED and
     TRUNCATED), retry/pass schedule, caption/body split, ordering, exit codes.

Run from the lane root:

  python3 -B reports/round-63/accept-o.py [--root DIR]

Legs, each printed PASS or FAIL:
  TOOL     tools/reopen-row.py exists at --root (the round-62 version does at 65b393e)
  INDEP    the tool's text names none of `reports/`, `accept-o`, `round-63`, `Fixture`;
           every run below uses a copy of the tool in a fresh temporary directory
  GEN      the round-62 class battery (BODY..NOROW, 2 of each) plus one fixture of each
           new class - REDIRECT_OK (one same-authority hop: LOCATED, attempts=2, the
           final URL reported), REDIRECT_MULTI (three hops: LOCATED, attempts=4),
           REDIRECT_LOOP (two hosts bouncing: UNREACHABLE, attempts=5, <=5 hops),
           MALFORMED_PORT (port 99999: MALFORMED, attempts=0, no request),
           MALFORMED_IPV6 (unbalanced bracket: MALFORMED, attempts=0),
           GZIP_BODY (gzip-encoded body: LOCATED, attempts=1),
           TRUNC_FAR (quote past the 4 MiB cap: TRUNCATED, attempts=1),
           TRUNC_NEAR (quote inside a body that overruns the cap: LOCATED) - run on a
           random local fixture (random ids, words, paths and quotes) with `--passes 3
           --gap 0 --allow-private`: every ROW line's verdict, attempts= and url= equal
           the class expectation, the server sees exactly the expected per-path hits,
           and the summary reads `REOPEN: <k>/<m> located`
  ORDER    ROW lines appear exactly once per argument, in argument order (repeated
           arguments print repeated lines)
  BOUND    the server's per-path request counts equal the class expectation; no request
           to an unlisted path
  EXIT     the GEN run exits 1; a four-BODY-row run exits 0 with `REOPEN: 4/4 located`;
           the same passes with no --registry (rows at corpus/SOURCES.md under the tool
           working directory)
  PRIV     without --allow-private three BODY rows on the local server print REFUSED
           attempts=0, the server sees 0 requests, exit 1
  DEFAULT  one DEAD row with no --passes/--gap prints UNREACHABLE attempts=9 within
           100-600 s of wall time (three passes, two 60 s gaps; bursts of three)
  ERR      no ID, a missing registry, an invalid UTF-8 registry, `--passes 0`, `--gap x`,
           `--timeout 0`, a non-numeric --timeout: each exit 2, a line starting
           REOPEN_ERROR, no Traceback on either stream
  REDIRECT with --allow-private, a row whose single URL answers 302 to a DIFFERENT
           loopback authority (other port) prints REFUSED attempts=1 url=-, the target
           server sees 0 requests, exit 1; without --allow-private the same row prints
           REFUSED attempts=0 and the source server sees 0 requests
  MALFORMED three rows (bad port, bad IPv6, empty host) print MALFORMED attempts=0 url=-,
           no Traceback on either stream, exit 1
  GZIP     a row whose body is gzip-encoded with the quote in the body prints LOCATED
           attempts=1; a row whose body is gzip-encoded with the quote only in a
           figcaption prints CAPTION_ONLY attempts=1
  TRUNC    a row whose quote sits past the 4 MiB cap prints TRUNCATED attempts=1 url=-;
           a row whose quote sits inside a body that overruns the cap prints LOCATED
  TIMEOUT  with `--timeout 4 --passes 1 --gap 0`, a row whose endpoint answers headers
           then stalls the body prints UNREACHABLE attempts=3 with no Traceback, and the
           wall time is < 45 s
  REVIEW   the independent review gate: .ufo/waves/round-63/w1/RevToolA.md, RevToolB.md
           and RevToolC.md each exist and contain the fixed token
           `VERDICT: NO-OPEN-HIGH-MED`, and reports/round-63/telemetry/rev-hold-lift.md
           (the residual review of the LANDED bytes) contains it too; a review that
           records an open finding, or a missing/dead review, fails this leg
Frozen predicate (the same sentence in reports/round-63/claims.json and in every
receipt): ACCEPT-O-63: every leg of reports/round-63/accept-o.py prints PASS.
Exit 0 only when every leg passes; 1 when any leg fails; 2 on unreadable input.
Review-only: the tool's live behaviour on registry rows (e.g. S665 caption, S671
Wayback, real archive gzip) is the closure's after admission, never a leg here.
"""
import argparse
import gzip
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

# class -> (expected verdict, expected attempts, {path role: expected hits})
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
    "DEAD_THEN_BODY2": ("LOCATED", 4, {"live": 3, "arch": 1}),
    "BODY_THEN_ARCHIVE": ("LOCATED", 1, {"live": 1, "arch": 0}),
    "DEAD": ("UNREACHABLE", 9, {"live": 9}),
    "GONE": ("UNREACHABLE", 1, {"live": 1}),
    "NOQUOTE": ("NO_QUOTE", 0, {"live": 0}),
    "SHORT": ("NO_QUOTE", 0, {"live": 0}),
    "NOROW": ("NO_ROW", 0, {}),
    # ---- round-63 routed-defect classes ----
    "REDIRECT_OK": ("LOCATED", 2, {"live": 1, "rtarget": 1}),
    "REDIRECT_MULTI": ("LOCATED", 4, {"c1": 1, "c2": 1, "c3": 1, "mtarget": 1}),
    "REDIRECT_LOOP": ("UNREACHABLE", 5, {"l1": 3, "l2": 2}),
    "MALFORMED_PORT": ("MALFORMED", 0, {}),
    "MALFORMED_IPV6": ("MALFORMED", 0, {}),
    "GZIP_BODY": ("LOCATED", 1, {"live": 1}),
    "TRUNC_FAR": ("TRUNCATED", 1, {"live": 1}),
    "TRUNC_NEAR": ("LOCATED", 1, {"live": 1}),
}

MATCH_ROLE = {cls: "live" for cls in (
    "BODY", "BODY_SPLIT", "PLAIN", "TRANSIENT2", "TRANSIENT_PASS",
    "GZIP_BODY", "TRUNC_NEAR")}
MATCH_ROLE.update({cls: "live" for cls in (
    "CAP_FIG", "CAP_ATTR", "CAP_ATTR_TITLE", "CAP_ATTR_DATA", "CAP_ATTR_ARIA",
    "CAP_ATTR_META", "CAP_CLASS", "CAP_CLASS_THUMB", "CAP_CLASS_GALLERY", "CAP_ID")})
MATCH_ROLE.update({"DEAD_ARCHIVE": "arch", "ARCHIVE_CAPTION": "arch",
                   "DEAD_THEN_BODY2": "arch", "BODY_THEN_ARCHIVE": "live"})

MAX_BODY_BYTES = 4 * 1024 * 1024


class Fixture:
    def __init__(self, rng):
        self.rng = rng
        self.routes = {}  # path -> (statuses list, body bytes, ctype, headers dict)
        self.hits = {}
        self.times = {}
        self.lock = threading.Lock()
        fixture = self

        class Handler(http.server.BaseHTTPRequestHandler):
            protocol_version = "HTTP/1.1"

            def do_GET(self):
                with fixture.lock:
                    n = fixture.hits.get(self.path, 0)
                    fixture.hits[self.path] = n + 1
                    fixture.times.setdefault(self.path, []).append(time.monotonic())
                    route = fixture.routes.get(self.path)
                if route is None:
                    self.send_response(404)
                    self.send_header("Content-Length", "0")
                    self.end_headers()
                    return
                statuses, body, ctype, headers = route
                status = statuses[min(n, len(statuses) - 1)]
                self.send_response(status)
                self.send_header("Content-Type", ctype)
                payload = body if status == 200 else b"<html><body><p>error page</p></body></html>"
                for name, value in headers.items():
                    self.send_header(name, value)
                self.send_header("Content-Length", str(len(payload)))
                self.end_headers()
                try:
                    self.wfile.write(payload)
                except (BrokenPipeError, ConnectionResetError):
                    pass

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
    """A port bound but never listening, held until the counter exits."""
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    RESERVED.append(s)
    return s.getsockname()[1]


def route(fx, path, statuses, body, ctype="text/html; charset=utf-8", headers=None):
    fx.routes[path] = (statuses, body, ctype, headers or {})


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
        route(fx, live, [200], ok_html)
    elif cls == "BODY_SPLIT":
        cut = len(qwords) // 2
        mixed = " ".join(qwords[:cut]).upper() + ", " + " \u2014 ".join(f"<b>{w}</b>" for w in qwords[cut:]) + "!"
        route(fx, live, [200], html(f"<p>{filler}</p><div><span>{mixed}</span></div>"), "text/html")
    elif cls == "PLAIN":
        route(fx, live, [200], f"{filler}\n{shown}\n{filler}\n".encode(), "text/plain; charset=utf-8")
    elif cls == "CAP_FIG":
        route(fx, live, [200], html(f"<p>{filler}</p><figure><img src='x.png'><figcaption>{shown}</figcaption></figure>"))
    elif cls.startswith("CAP_ATTR"):
        attr = {"CAP_ATTR": "alt", "CAP_ATTR_TITLE": "title", "CAP_ATTR_DATA": "data-img-description",
                "CAP_ATTR_ARIA": "aria-label"}.get(cls)
        if cls == "CAP_ATTR_META":
            body = ("<!doctype html><html><head><meta name=\"description\" content=\"" + shown + "\"></head><body><p>"
                    + filler + "</p></body></html>").encode()
        else:
            body = html(f"<p>{filler}</p><img src='x.png' {attr}=\"{shown}\">")
        route(fx, live, [200], body)
    elif cls.startswith("CAP_CLASS") or cls == "CAP_ID":
        attr = {"CAP_CLASS": 'class="wp-caption-text"', "CAP_CLASS_THUMB": 'class="thumbnail-description"',
                "CAP_CLASS_GALLERY": 'class="Gallery-item"', "CAP_ID": 'id="figCaption1"'}[cls]
        route(fx, live, [200], html(f"<p>{filler}</p><div {attr}><span>{shown}</span></div>"))
    elif cls == "SCRIPT":
        route(fx, live, [200], html(f"<p>{filler}</p><script>var t = \"{shown}\";</script>"))
    elif cls == "ABSENT":
        route(fx, live, [200], html(f"<p>{filler}</p><p>{' '.join(qwords[:-3])} {fx.word()}.</p>"))
    elif cls == "TRANSIENT2":
        route(fx, live, [503, 503, 200], ok_html)
    elif cls == "TRANSIENT_PASS":
        route(fx, live, [503, 502, 429, 200], ok_html)
    elif cls in ("DEAD_ARCHIVE", "ARCHIVE_CAPTION", "DEAD_THEN_BODY2", "BODY_THEN_ARCHIVE"):
        arch = f"/web/2025{rng.randint(10**9, 10**10 - 1)}id_/https://{fx.word()}.org{live}"
        paths["arch"] = arch
        if cls == "DEAD_ARCHIVE":
            route(fx, live, [403], ok_html)
            route(fx, arch, [200], ok_html)
        elif cls == "BODY_THEN_ARCHIVE":
            route(fx, live, [200], ok_html)
            route(fx, arch, [200], ok_html)
        elif cls == "ARCHIVE_CAPTION":
            route(fx, live, [410], ok_html)
            route(fx, arch, [200], html(f"<p>{filler}</p><figure><figcaption>{shown}</figcaption></figure>"))
        else:
            route(fx, live, [500], ok_html)
            route(fx, arch, [200], ok_html)
    elif cls == "DEAD":
        route(fx, live, [503], ok_html)
    elif cls == "GONE":
        route(fx, live, [404], ok_html)
    elif cls == "REDIRECT_OK":
        target = fx.path()
        paths["rtarget"] = target
        route(fx, live, [302], b"", headers={"Location": target})
        route(fx, target, [200], ok_html)
    elif cls == "REDIRECT_MULTI":
        c2, c3, target = fx.path(), fx.path(), fx.path()
        paths.update({"c1": live, "c2": c2, "c3": c3, "mtarget": target})
        route(fx, live, [301], b"", headers={"Location": c2})
        route(fx, c2, [302], b"", headers={"Location": c3})
        route(fx, c3, [307], b"", headers={"Location": target})
        route(fx, target, [200], ok_html)
    elif cls == "REDIRECT_LOOP":
        other = fx.path()
        paths.update({"l1": live, "l2": other})
        route(fx, live, [302], b"", headers={"Location": other})
        route(fx, other, [303], b"", headers={"Location": live})
    elif cls == "GZIP_BODY":
        route(fx, live, [200], gzip.compress(ok_html), headers={"Content-Encoding": "gzip"})
    elif cls == "TRUNC_FAR":
        pad = (" ".join(fx.words(12)) + ". ") * 70000
        body = html(f"<p>{pad}</p><p>{shown}</p>")
        route(fx, live, [200], body)
    elif cls == "TRUNC_NEAR":
        pad = (" ".join(fx.words(12)) + ". ") * 70000
        body = html(f"<p>{shown}</p><p>{pad}</p>")
        route(fx, live, [200], body)
    elif cls in ("NOQUOTE", "SHORT"):
        route(fx, live, [200], ok_html)
    urls = fx.url(live) + (f" ; capture {fx.url(arch)}" if arch else "")
    anchor = f"section {fx.word()}: \"{shown}\""
    if cls == "NOQUOTE":
        anchor = f"section {fx.word()}, no quoted span"
    elif cls == "SHORT":
        anchor = f"section {fx.word()}: \"{' '.join(qwords[:5])}\""
    row = (f"| {sid} | {fx.word().title()} page, Fixture Press, 2025 \u2014 {urls}. | docs | B | scope {fx.word()} | "
           f"{anchor} | teaches {fx.word()} | mined | 2026-10-23 | 180d | corpus/knowledge/x.md |")
    if cls == "MALFORMED_PORT":
        row = (f"| {sid} | Bad port page \u2014 http://127.0.0.1:99999{fx.path()} | docs | B | s | "
               f"{anchor} | t | mined | 2026-10-23 | 180d | x |")
    elif cls == "MALFORMED_IPV6":
        row = (f"| {sid} | Bad IPv6 page \u2014 http://[2001:db8::1{fx.path()} | docs | B | s | "
               f"{anchor} | t | mined | 2026-10-23 | 180d | x |")
    return row, paths


def run_tool(tool, cwd, args, timeout=900):
    """Runs the tool copy in its own process group; on timeout the whole group is killed."""
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


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    root = os.path.abspath(ap.parse_args().root)
    lane = root
    legs = []

    def leg(name, ok, detail):
        legs.append(ok)
        print(f"{name} {'PASS' if ok else 'FAIL'} {detail}")

    src = os.path.join(root, TOOL)
    have = os.path.isfile(src)
    leg("TOOL", have, f"path={TOOL} exists={have}")
    if not have:
        for name in ("INDEP", "GEN", "ORDER", "BOUND", "EXIT", "PRIV", "DEFAULT", "ERR",
                     "REDIRECT", "MALFORMED", "GZIP", "TRUNC", "TIMEOUT", "REVIEW"):
            leg(name, False, "no tool")
        print("ACCEPT-O-63: FAIL")
        return 1
    try:
        text = open(src, encoding="utf-8").read()
    except (OSError, UnicodeDecodeError) as error:
        print(f"ACCEPT_O_INPUT_ERROR {error}", file=sys.stderr)
        return 2
    named = [s for s in ("reports/", "accept-o", "round-63", "Fixture", "REOPEN_HOSTS") if s in text]
    leg("INDEP", not named, f"named={named}")

    rng = random.SystemRandom()
    work = tempfile.mkdtemp(prefix="accept-o-63-")
    tool = os.path.join(work, "reopen-row.py")
    shutil.copyfile(src, tool)
    fx = Fixture(rng)
    try:
        used = set()

        def fresh_id():
            while True:
                sid = f"S{rng.randint(2000, 2999)}"
                if sid not in used:
                    used.add(sid)
                    return sid

        plan = [c for c in CLASSES for _ in range(2 if c not in (
            "REDIRECT_OK", "REDIRECT_MULTI", "REDIRECT_LOOP", "MALFORMED_PORT", "MALFORMED_IPV6",
            "GZIP_BODY", "TRUNC_FAR", "TRUNC_NEAR") else 1)]
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
        for row in got:
            by.setdefault(row[0], []).append(tuple(row[1:3]))
        wrong = []
        located = 0
        for sid, cls in expect:
            want_v, want_n = ("UNREACHABLE", 9) if cls == "DEAD_PORT" else CLASSES[cls][:2]
            located += want_v == "LOCATED"
            seen = by.get(sid, [])
            if len(seen) != 1 or seen[0] != (want_v, want_n):
                wrong.append(f"{cls}:{sid}:want={want_v}/{want_n}:got={seen}")
            want_u = fx.url(roles[sid][MATCH_ROLE[cls]]) if cls in MATCH_ROLE else "-"
            if cls == "REDIRECT_OK":
                want_u = fx.url(roles[sid]["rtarget"])
            elif cls == "REDIRECT_MULTI":
                want_u = fx.url(roles[sid]["mtarget"])
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
            "missing": ["--registry", os.path.join(work, "nope.md"), "S2000"],
            "badutf8": ["--registry", bad_utf, "S1234"],
            "passes0": ["--registry", reg, "--passes", "0", ids[0]],
            "gapx": ["--registry", reg, "--gap", "x", ids[0]],
            "timeout0": ["--registry", reg, "--timeout", "0", ids[0]],
            "timeoutx": ["--registry", reg, "--timeout", "x", ids[0]],
        }
        err_bad = []
        for name, args in cases.items():
            c, o, e, _ = run_tool(tool, work, args, timeout=120)
            if c != 2 or not any(l.startswith("REOPEN_ERROR") for l in (o + "\n" + e).splitlines()) \
                    or "Traceback" in (o + e):
                err_bad.append(f"{name}:exit={c}")
        leg("ERR", not err_bad, f"bad={err_bad}")

        # ---- REDIRECT: cross-authority redirect refused even under --allow-private ----
        fx2 = Fixture(rng)
        try:
            secret_words = fx2.words(12)
            secret_quote = " ".join(secret_words)
            secret_shown = secret_quote[0].upper() + secret_quote[1:] + "."
            secret_path = "/secret-" + fx2.word()
            route(fx2, secret_path, [200], html(f"<p>{' '.join(fx2.words(20))}.</p><p>{secret_shown}</p>"))
            hop_path = "/hop-" + fx.word()
            route(fx, hop_path, [302], b"", headers={"Location": fx2.url(secret_path)})
            rsid = fresh_id()
            reg_r = os.path.join(work, "REDIRECT.md")
            open(reg_r, "w", encoding="utf-8").write(
                "| id | source |\n"
                f"| {rsid} | Hop page \u2014 {fx.url(hop_path)} | docs | B | s | "
                f"anchor: \"{secret_shown}\" | t | mined | 2026-10-23 | 180d | x |\n")
            rc, rout, rerr, _ = run_tool(tool, work, ["--registry", reg_r, "--passes", "1", "--gap", "0", "--allow-private", rsid])
            rgot = parse(rout)
            red_ok = (rc == 1 and rgot == [(rsid, "REFUSED", 1)]
                      and fx2.hits.get(secret_path, 0) == 0 and fx.hits.get(hop_path, 0) == 1
                      and "Traceback" not in (rout + rerr))
            rc2, rout2, _, _ = run_tool(tool, work, ["--registry", reg_r, "--passes", "1", "--gap", "0", rsid])
            rgot2 = parse(rout2)
            red_ok = red_ok and (rc2 == 1 and rgot2 == [(rsid, "REFUSED", 0)] and fx.hits.get(hop_path, 0) == 1)
            leg("REDIRECT", red_ok,
                f"allow_private={rgot} hits_src={fx.hits.get(hop_path, 0)} hits_target={fx2.hits.get(secret_path, 0)} "
                f"no_flag={rgot2} exits={rc},{rc2}")
        finally:
            fx2.close()

        # ---- MALFORMED ----
        mids = []
        mrows = ["| id | source |"]
        for label, url in (("badport", "http://127.0.0.1:99999/x"), ("badipv6", "http://[2001:db8::1/x"),
                           ("emptyhost", "http://:80/x")):
            sid = fresh_id()
            mids.append(sid)
            mrows.append(f"| {sid} | {label} \u2014 {url} | docs | B | s | anchor: \"{' '.join(fx.words(10))}\" | "
                         "t | mined | 2026-10-23 | 180d | x |")
        reg_m = os.path.join(work, "MALFORMED.md")
        open(reg_m, "w", encoding="utf-8").write("\n".join(mrows) + "\n")
        mc, mout, merr, _ = run_tool(tool, work, ["--registry", reg_m, "--allow-private"] + mids)
        mgot = parse(mout)
        leg("MALFORMED", mc == 1 and [(s, v, n) for s, v, n in mgot] == [(s, "MALFORMED", 0) for s in mids]
            and not any(fx.hits.get(p, 0) for p in ("/x",)) and "Traceback" not in (mout + merr),
            f"exit={mc} rows={mgot} traceback={'Traceback' in (mout + merr)}")

        # ---- GZIP ----
        gz_ids, gz_paths = [], {}
        gz_lines = ["| id | source |"]
        for caption in (False, True):
            sid = fresh_id()
            gz_ids.append(sid)
            p = "/gz-" + fx.word()
            gz_paths[sid] = p
            q = " ".join(fx.words(12))
            shown = q[0].upper() + q[1:] + "."
            if caption:
                body = html(f"<p>{' '.join(fx.words(20))}.</p><figure><figcaption>{shown}</figcaption></figure>")
            else:
                body = html(f"<p>{' '.join(fx.words(20))}.</p><p>{shown}</p>")
            route(fx, p, [200], gzip.compress(body), headers={"Content-Encoding": "gzip"})
            gz_lines.append(f"| {sid} | gz page \u2014 {fx.url(p)} | docs | B | s | anchor: \"{shown}\" | "
                            "t | mined | 2026-10-23 | 180d | x |")
        reg_gz = os.path.join(work, "GZIP.md")
        open(reg_gz, "w", encoding="utf-8").write("\n".join(gz_lines) + "\n")
        gc, gout, gerr, _ = run_tool(tool, work, ["--registry", reg_gz, "--passes", "1", "--gap", "0", "--allow-private"] + gz_ids)
        ggot = parse(gout)
        leg("GZIP", gc == 1 and [(s, v, n) for s, v, n in ggot] == [
                (gz_ids[0], "LOCATED", 1), (gz_ids[1], "CAPTION_ONLY", 1)] and "Traceback" not in (gout + gerr),
            f"exit={gc} rows={ggot}")

        # ---- TRUNC ----
        t_ids = []
        t_lines = ["| id | source |"]
        t_expect = []
        for far in (True, False):
            sid = fresh_id()
            t_ids.append(sid)
            p = "/trunc-" + fx.word()
            q = " ".join(fx.words(12))
            shown = q[0].upper() + q[1:] + "."
            pad = (" ".join(fx.words(10)) + ". ") * 80000
            body = (html(f"<p>{pad}</p><p>{shown}</p>") if far else html(f"<p>{shown}</p><p>{pad}</p>"))
            route(fx, p, [200], body)
            t_lines.append(f"| {sid} | trunc page \u2014 {fx.url(p)} | docs | B | s | anchor: \"{shown}\" | "
                           "t | mined | 2026-10-23 | 180d | x |")
            t_expect.append((sid, "TRUNCATED" if far else "LOCATED", 1))
        reg_t = os.path.join(work, "TRUNC.md")
        open(reg_t, "w", encoding="utf-8").write("\n".join(t_lines) + "\n")
        tc, tout, terr, _ = run_tool(tool, work, ["--registry", reg_t, "--passes", "1", "--gap", "0", "--allow-private"] + t_ids)
        tgot = parse(tout)
        leg("TRUNC", tc == 1 and [(s, v, n) for s, v, n in tgot] == t_expect and "Traceback" not in (tout + terr),
            f"exit={tc} rows={tgot} want={t_expect}")

        # ---- TIMEOUT ----
        stall_sid = fresh_id()
        stall_path = "/x"
        sq = " ".join(fx.words(12))
        # headers answered, body promised, then nothing for 120 s

        class StallHandler(http.server.BaseHTTPRequestHandler):
            def do_GET(self):
                self.send_response(200)
                self.send_header("Content-Type", "text/html")
                self.send_header("Content-Length", str(1024 * 1024))
                self.end_headers()
                try:
                    self.wfile.write(b"x" * 100)
                    self.wfile.flush()
                    time.sleep(120)
                except (BrokenPipeError, ConnectionResetError):
                    pass

            def log_message(self, *args):
                pass

        stall_server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), StallHandler)
        threading.Thread(target=stall_server.serve_forever, daemon=True).start()
        try:
            reg_st = os.path.join(work, "STALL.md")
            open(reg_st, "w", encoding="utf-8").write(
                "| id | source |\n"
                f"| {stall_sid} | stall page \u2014 http://127.0.0.1:{stall_server.server_address[1]}{stall_path} | docs | B | s | "
                f"anchor: \"{sq}\" | t | mined | 2026-10-23 | 180d | x |\n")
            stc, stout, sterr, wall = run_tool(tool, work,
                                               ["--registry", reg_st, "--passes", "1", "--gap", "0",
                                                "--timeout", "4", "--allow-private", stall_sid],
                                               timeout=120)
            stgot = parse(stout)
            leg("TIMEOUT", stc == 1 and stgot == [(stall_sid, "UNREACHABLE", 3)] and wall < 45
                and "Traceback" not in (stout + sterr),
                f"exit={stc} rows={stgot} wall={wall:.1f}s")
        finally:
            stall_server.shutdown()
            stall_server.server_close()

        # ---- REVIEW (independent review gate) ----
        reviews = [os.path.join(lane, ".ufo", "waves", "round-63", "w1", f"RevTool{n}.md") for n in "ABC"]
        reviews.append(os.path.join(lane, "reports", "round-63", "telemetry", "rev-hold-lift.md"))
        missing, verdicts = [], []
        for path in reviews:
            try:
                body = open(path, encoding="utf-8").read()
            except OSError:
                missing.append(os.path.basename(path))
                continue
            verdicts.append("VERDICT: NO-OPEN-HIGH-MED" in body)
        leg("REVIEW", not missing and all(verdicts),
            f"reports={len(reviews)} missing={missing} clean={sum(verdicts)}")
    finally:
        try:
            fx.close()
        finally:
            for sock in RESERVED:
                sock.close()
            shutil.rmtree(work, ignore_errors=True)
    verdict = all(legs)
    print(f"ACCEPT-O-63: {'PASS' if verdict else 'FAIL'}")
    return 0 if verdict else 1


if __name__ == "__main__":
    sys.exit(main())
