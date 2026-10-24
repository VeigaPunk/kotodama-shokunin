#!/usr/bin/env python3
r"""Round-65 claim O acceptance, revision 1 (pre-data).

Claim O (operability, counter hardening): close the round-64 routed
counter-gaming surfaces (LOG "Round-64 routed residuals", frozen-predicate
rule) in the round-65 counter suite -

  RESTATE near-copy  reports/round-65/accept-c.py revision 1: a bullet that
          is its row's teaches cell plus a trailing novel word (the
          trailing-word bypass found post-hoc in `w2/RevVerifyC.md` F2) now
          fails the word-boundary coverage rule
  keyed Ca legs      reports/round-65/accept-ca.py revision 1: HISTOGRAM /
          R63SEP / DISPO legs key on their exact rows and files instead of
          global token presence (`w2/RevVerifyCa.md` HIGH-1); NITS pins its
          value pairs, not denial prose (HIGH-2)
  filtered greens    the FULL leg re-executes the complete battery in a
          subprocess on every run, so a `--only` partial run can no longer be
          presented as the verdict (`w2/OReceiptFresh.md`)
  mutant exclusivity the MUTEX leg sweeps all ten round-64 mutants through
          every redirect-edge + DRIP fixture, prints the exact failing-leg
          table, and pins the disclosed non-exclusive cases (m1 also fails
          EDGE_USERINFO + EDGE_HTTPS; m2 also fails EDGE_MALTARG —
          `w2/RevVerifyO2.md` exactness-sweep-o.txt).  The claims.json
          wording is the honest "at least their pinned leg".
  fragment gaps      the FRAG leg runs the durable
          tools/check-row-fragments.py (teaches-length bound and query-aware
          URL normalization — the round-64 check-rows.py gaps) over this
          round's row fragments.

The tool under test is the unchanged lane tools/reopen-row.py (round-65 base
17c32302c6845c8f164b985a8cb312d3181c8788, sha256
c0f10a8450b425bb0959b00c18031fde43ac4809a5334538e9c1d4d9199568a0), which
must PASS every round-62/63/64 leg, while each embedded mutant must FAIL at
least its pinned leg.

Run from the lane root:

  python3 -B reports/round-65/accept-o.py [--root DIR] [--only LEG,...]

Legs, each printed PASS or FAIL (`--only` runs just the named legs; legs not
run print `<LEG> SKIP` and do not count):
  TOOL     tools/reopen-row.py exists at --root and is executable
  INDEP    the tool's text names none of `reports/`, `accept-o`, `round-63`,
           `round-64`, `round-65`, `Fixture`, `REOPEN_HOSTS`; every run below
           uses a copy of the tool in a fresh temporary directory
  GEN      the round-62/63 class battery (BODY..NOROW, 2 of each) plus one
           fixture of each repair class (REDIRECT_OK, REDIRECT_MULTI,
           REDIRECT_LOOP, MALFORMED_PORT, MALFORMED_IPV6, GZIP_BODY,
           TRUNC_FAR, TRUNC_NEAR): random local fixtures, `--passes 3 --gap 0
           --allow-private`; verdict, attempts= and url= per row, per-path
           hit counts, and `REOPEN: <k>/<m> located`
  ORDER    ROW lines exactly once per argument, in argument order
  BOUND    per-path request counts equal the class expectation; no unlisted path
  EXIT     GEN exits 1; four BODY rows exit 0; the default-registry run exits 0
  PRIV     without --allow-private three BODY rows print REFUSED attempts=0
  DEFAULT  one DEAD row with no --passes/--gap prints UNREACHABLE attempts=9
           inside the 60 s-pass schedule (three bursts of three, 60 s gaps)
  ERR      no ID, missing registry, invalid UTF-8 registry, `--passes 0`,
           `--gap x`, `--timeout 0`, non-numeric --timeout: exit 2,
           REOPEN_ERROR, no Traceback
  REDIRECT with --allow-private a 302 to a DIFFERENT loopback authority prints
           REFUSED attempts=1 url=-, the target sees 0 requests; without the
           flag REFUSED attempts=0 and the source sees 0 requests
  MALFORMED three malformed listed URLs print MALFORMED attempts=0 url=-, exit 1
  GZIP     gzip body quote -> LOCATED; gzip caption-only -> CAPTION_ONLY
  TRUNC    quote past the 4 MiB cap -> TRUNCATED; quote inside -> LOCATED
  TIMEOUT  `--timeout 2 --passes 1`: a stall-after-headers body prints
           UNREACHABLE attempts=3, wall < 20 s, three stall requests spanning
           >= 3.0 s (the requested wall budget, not a socket default)
  EDGE_SCHEMEREL   `Location: //127.0.0.1:<other port>/x`: REFUSED
                   attempts=1 url=-, target hits 0, exit 1
  EDGE_USERINFO    `Location: http://u@127.0.0.1:<other port>/x`: REFUSED
                   attempts=1, target hits 0; same-authority userinfo IS
                   followed (UNREACHABLE attempts=6)
  EDGE_HTTPS       `Location: https://127.0.0.1:<other port>/x`: REFUSED
                   attempts=1; same-authority https attempted (UNREACHABLE
                   attempts=6)
  EDGE_MALTARG     `Location: http://127.0.0.1:99999/x` (unparseable port):
                   MALFORMED attempts=0 url=-, no traceback
  EDGE_SLASHLESS   `Location: rel/x` resolved against the current path, not
                   the server root
  EDGE_308         a 308 response is a redirect
  EDGE_5TH200      a fifth response that is 200 is honoured (no spurious
                   over-limit refusal)
  DRIP      a body dripping one byte per second past the wall budget prints
            UNREACHABLE attempts=3, wall < 20 s, three stall requests
            spanning >= 7.0 s
  MUT      the round-64 kill set: ten byte-patched copies of the lane tool,
           each FAILing at least its pinned leg (m5 additionally isolated:
           EDGE_SCHEMEREL stays PASS)
  FULL     (round-65) the complete battery (every leg above except
           FULL/MUTEX/FRAG) re-executes in a subprocess on --root and prints
           all-PASS with zero SKIP lines, so a filtered-mode partial run
           cannot stand as the verdict
  MUTEX    (round-65) all ten mutants swept through every EDGE + DRIP fixture
           (plus GEN,BOUND for m8); measured failing-leg set superset-equals
           the pinned set for every mutant and equals the disclosed
           expectation exactly (m1 +EDGE_USERINFO+EDGE_HTTPS; m2
           +EDGE_MALTARG); the committed telemetry/exactness-sweep-o65.txt
           table matches the live measurement
  FRAG     (round-65) tools/check-row-fragments.py --selftest passes and the
           scan of .ufo/waves/round-65/rows prints 0 findings (teaches-length
           and query-aware URL normalization closed durably)

Revision history (pre-data):
- revision 1: FULL/MUTEX/FRAG added (round-64 routed residuals;
  forcing controls `reports/round-65/telemetry/controls-o.txt`).
Revision history (pre-data):
- revision 3: digit-aware leg-line regexes in FULL and MUTEX ([A-Z0-9_]+;
  forcing control .ufo/waves/round-65/w1/RevCounterO.md - m6/m7 measured NONE
  because EDGE_308/EDGE_5TH200 carry digits), FULL expects the inner run's
  filtered verdict string, MUTEX requires sweep exit 1 and no traceback.
- revision 2: FULL tolerates exactly the three self-recursion SKIP lines
  (forcing receipt: dry-run-o.txt FULL FAIL skip=3 at base) and FRAG requires
  exactly 26 scanned row fragments (forcing receipt: dry-run-o.txt FRAG PASS
  over 0 files - the vacuous-empty-dir bypass).  Forcing controls:
  reports/round-65/telemetry/controls-o.txt.
Frozen predicate (the same sentence in reports/round-65/claims.json and in
every receipt): ACCEPT-O-65: every leg of reports/round-65/accept-o.py
prints PASS.
Exit 0 only when every leg passes; 1 when any leg fails; 2 on unreadable
input or an unknown --only leg.
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
        self.routes = {}  # path -> (statuses list, body bytes, ctype, headers dict[, drip dict])
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
                statuses, body, ctype, headers = route[:4]
                drip = route[4] if len(route) > 4 else None
                status = statuses[min(n, len(statuses) - 1)]
                self.send_response(status)
                self.send_header("Content-Type", ctype)
                payload = body if status == 200 else b"<html><body><p>error page</p></body></html>"
                for name, value in headers.items():
                    self.send_header(name, value)
                if drip is None:
                    self.send_header("Content-Length", str(len(payload)))
                    self.end_headers()
                    try:
                        self.wfile.write(payload)
                    except (BrokenPipeError, ConnectionResetError):
                        pass
                else:
                    # chunked-looking drip without Content-Length: send the
                    # payload in `count` chunks, `period` seconds apart, then
                    # close.  Every chunk lands inside a per-socket timeout but
                    # the total body time exceeds a bounded wall budget.
                    self.send_header("Connection", "close")
                    self.end_headers()
                    chunk = drip["chunk"]
                    for _ in range(drip["count"]):
                        try:
                            self.wfile.write(chunk)
                            self.wfile.flush()
                        except (BrokenPipeError, ConnectionResetError):
                            break
                        time.sleep(drip["period"])
                    self.close_connection = True

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


def route(fx, path, statuses, body, ctype="text/html; charset=utf-8", headers=None, drip=None):
    fx.routes[path] = (statuses, body, ctype, headers or {}) + ((drip,) if drip is not None else ())


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
        # pad past 1 MiB so a tool that decodes only small bodies cannot pass
        pad = (" ".join(fx.words(12)) + ". ") * 12000
        route(fx, live, [200], gzip.compress(html(f"<p>{pad}</p><p>{shown}</p>")),
              headers={"Content-Encoding": "gzip"})
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
    ap.add_argument("--only", default="")
    args = ap.parse_args()
    # revision 5 (pre-data; forcing controls:
    # .ufo/waves/round-64/w2/RevVerifyO2.md,
    # .ufo/waves/round-64/w2/SupS729.md, .ufo/waves/round-64/w2/OReceiptFresh.md;
    # red capture: reports/round-64/telemetry/final-measures-o-rev4.txt):
    # restructured m5 and fail-closed --only validation.
    CORE = ("INDEP", "GEN", "ORDER", "BOUND", "EXIT", "PRIV", "DEFAULT",
            "ERR", "REDIRECT", "MALFORMED", "GZIP", "TRUNC", "TIMEOUT")
    EDGE = ("EDGE_SCHEMEREL", "EDGE_USERINFO", "EDGE_HTTPS", "EDGE_MALTARG",
            "EDGE_SLASHLESS", "EDGE_308", "EDGE_5TH200")
    ALL_LEGS = set(CORE) | set(EDGE) | {"TOOL", "DRIP", "MUT", "FULL", "MUTEX", "FRAG"}
    only = set(x for x in args.only.split(",") if x)
    unknown = sorted(only - ALL_LEGS)
    if unknown:
        print(f"ACCEPT_O_INPUT_ERROR unknown --only leg(s): {','.join(unknown)}",
              file=sys.stderr)
        return 2
    root = os.path.abspath(args.root)
    lane = root
    legs = []
    import hashlib as _hl
    _self = _hl.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest()
    _mv = subprocess.run(["git", "rev-parse", "main"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(f"# counter sha256 (self): {_self}")
    print(f"# measured revision (lane main): {_mv.stdout.decode().strip() or 'unresolvable'}")

    def leg(name, ok, detail):
        if only and name not in only:
            print(f"{name} SKIP")
            return
        legs.append(ok)
        print(f"{name} {'PASS' if ok else 'FAIL'} {detail}")

    run_core = not only or any(c in only for c in CORE)

    def need(name):
        return not only or name in only

    src = os.path.join(root, TOOL)
    have = os.path.isfile(src) and os.access(src, os.X_OK)
    leg("TOOL", have, f"path={TOOL} exists={os.path.isfile(src)} executable={have and os.access(src, os.X_OK)}")
    if not have:
        for name in ("INDEP", "GEN", "ORDER", "BOUND", "EXIT", "PRIV", "DEFAULT", "ERR",
                     "REDIRECT", "MALFORMED", "GZIP", "TRUNC", "TIMEOUT",
                     "EDGE_SCHEMEREL", "EDGE_USERINFO", "EDGE_HTTPS",
                     "EDGE_MALTARG", "EDGE_SLASHLESS", "EDGE_308",
                     "EDGE_5TH200", "DRIP", "MUT", "FULL", "MUTEX", "FRAG"):
            leg(name, False, "no tool")
        print("ACCEPT-O-65: FAIL")
        return 1
    try:
        text = open(src, encoding="utf-8").read()
    except (OSError, UnicodeDecodeError) as error:
        print(f"ACCEPT_O_INPUT_ERROR {error}", file=sys.stderr)
        return 2
    rng = random.SystemRandom()
    work = tempfile.mkdtemp(prefix="accept-o-64-")
    tool = os.path.join(work, "reopen-row.py")
    shutil.copyfile(src, tool)
    fx = Fixture(rng)
    used = set()

    def fresh_id():
        while True:
            sid = f"S{rng.randint(2000, 2999)}"
            if sid not in used:
                used.add(sid)
                return sid

    try:
        if run_core:
            named = [s for s in ("reports/", "accept-o", "round-63", "round-64", "round-65", "Fixture", "REOPEN_HOSTS") if s in text]
            leg("INDEP", not named, f"named={named}")

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
                pad = (" ".join(fx.words(12)) + ". ") * 12000
                if caption:
                    body = html(f"<p>{pad}</p><figure><figcaption>{shown}</figcaption></figure>")
                else:
                    body = html(f"<p>{pad}</p><p>{shown}</p>")
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
            stall_times = []
            stall_lock = threading.Lock()

            class TimedStallHandler(StallHandler):
                def do_GET(self):
                    with stall_lock:
                        stall_times.append(time.monotonic())
                    super().do_GET()

            stall_server.RequestHandlerClass = TimedStallHandler
            threading.Thread(target=stall_server.serve_forever, daemon=True).start()
            try:
                reg_st = os.path.join(work, "STALL.md")
                open(reg_st, "w", encoding="utf-8").write(
                    "| id | source |\n"
                    f"| {stall_sid} | stall page \u2014 http://127.0.0.1:{stall_server.server_address[1]}{stall_path} | docs | B | s | "
                    f"anchor: \"{sq}\" | t | mined | 2026-10-23 | 180d | x |\n")
                stc, stout, sterr, wall = run_tool(tool, work,
                                                   ["--registry", reg_st, "--passes", "1", "--gap", "0",
                                                    "--timeout", "2", "--allow-private", stall_sid],
                                                   timeout=120)
                stgot = parse(stout)
                span = (stall_times[-1] - stall_times[0]) if len(stall_times) >= 2 else 0.0
                leg("TIMEOUT", stc == 1 and stgot == [(stall_sid, "UNREACHABLE", 3)] and wall < 20
                    and len(stall_times) == 3 and span >= 3.0
                    and "Traceback" not in (stout + sterr),
                    f"exit={stc} rows={stgot} wall={wall:.1f}s stall_hits={len(stall_times)} span={span:.1f}s")
            finally:
                stall_server.shutdown()
                stall_server.server_close()
        # ---- EDGE legs (round-64): the seven unpinned redirect-edge
        # properties of .ufo/waves/round-63/w1/CtlORedirectEdge.md section 4,
        # one fixture each, as spelled out there.  All endpoints are loopback
        # servers this process starts; nothing live is fetched. ----
        def edge_secret(fx_b):
            """Register a quote page on a fixture; return (path, quote)."""
            words = fx_b.words(12)
            shown = " ".join(words)
            shown = shown[0].upper() + shown[1:] + "."
            p = "/t-" + fx_b.word()
            route(fx_b, p, [200], html(f"<p>{' '.join(fx_b.words(20))}.</p><p>{shown}</p>"))
            return p, shown

        def edge_reg(sid, label, url, quote):
            reg = os.path.join(work, f"EDGE-{label}-{sid}.md")
            open(reg, "w", encoding="utf-8").write(
                "| id | source |\n"
                f"| {sid} | {label} \u2014 {url} | docs | B | s | "
                f"anchor: \"{quote}\" | t | mined | 2026-10-23 | 180d | x |\n")
            return reg

        def edge_run(sid, reg):
            return run_tool(tool, work,
                ["--registry", reg, "--passes", "1", "--gap", "0",
                 "--timeout", "6", "--allow-private", sid], timeout=90)

        fx0 = fx

        if need("EDGE_SCHEMEREL") or need("EDGE_USERINFO") or need("EDGE_HTTPS"):
            fx2 = Fixture(rng)
            try:
                tpath, tquote = edge_secret(fx2)

                if need("EDGE_SCHEMEREL"):
                    hop = "/es-" + fx.word()
                    route(fx0, hop, [302], b"",
                          headers={"Location": f"//127.0.0.1:{fx2.port}{tpath}"})
                    sid = fresh_id()
                    reg = edge_reg(sid, "scheme-rel", fx0.url(hop), tquote)
                    c, o, e, _ = edge_run(sid, reg)
                    got = parse(o)
                    leg("EDGE_SCHEMEREL",
                        c == 1 and got == [(sid, "REFUSED", 1)]
                        and fx2.hits.get(tpath, 0) == 0 and fx0.hits.get(hop, 0) == 1
                        and "Traceback" not in (o + e),
                        f"rows={got} tgt_hits={fx2.hits.get(tpath, 0)} src_hits={fx0.hits.get(hop, 0)} tb={'Traceback' in (o + e)}")
                else:
                    leg("EDGE_SCHEMEREL", False, "skipped")

                if need("EDGE_USERINFO"):
                    hop = "/eu-" + fx.word()
                    route(fx0, hop, [302], b"",
                          headers={"Location": f"http://u@127.0.0.1:{fx2.port}{tpath}"})
                    sid = fresh_id()
                    reg = edge_reg(sid, "userinfo", fx0.url(hop), tquote)
                    c, o, e, _ = edge_run(sid, reg)
                    got = parse(o)
                    # control: same-authority userinfo must be attempted
                    # (cross-authority refusal only - userinfo is not part of
                    # the authority); urllib cannot resolve a userinfo host,
                    # so the observed end is UNREACHABLE with 6 requests
                    # (3 attempts, source plus target), never REFUSED.
                    hop2 = "/eu2-" + fx.word()
                    route(fx0, hop2, [302], b"",
                          headers={"Location": f"http://u@127.0.0.1:{fx0.port}{fx.path()}"})
                    sid2 = fresh_id()
                    reg2 = edge_reg(sid2, "userinfo-same", fx0.url(hop2), tquote)
                    c2, o2, e2, _ = edge_run(sid2, reg2)
                    got2 = parse(o2)
                    ok2 = (c2 == 1 and len(got2) == 1
                           and got2[0][0] == sid2 and got2[0][1] != "REFUSED"
                           and got2[0][2] == 6)
                    leg("EDGE_USERINFO",
                        c == 1 and got == [(sid, "REFUSED", 1)]
                        and fx2.hits.get(tpath, 0) == 0 and ok2,
                        f"cross={got} tgt_hits={fx2.hits.get(tpath, 0)} same_auth={got2} ok={ok2}")
                else:
                    leg("EDGE_USERINFO", False, "skipped")

                if need("EDGE_HTTPS"):
                    hop = "/eh-" + fx.word()
                    route(fx0, hop, [302], b"",
                          headers={"Location": f"https://127.0.0.1:{fx2.port}{tpath}"})
                    sid = fresh_id()
                    reg = edge_reg(sid, "https-x", fx0.url(hop), tquote)
                    c, o, e, _ = edge_run(sid, reg)
                    got = parse(o)
                    # control: https to the SAME authority is attempted; the
                    # server speaks plain HTTP so the hop fails as a transient
                    # (UNREACHABLE attempts=3), never REFUSED, never crash.
                    hop2 = "/eh2-" + fx.word()
                    route(fx0, hop2, [302], b"",
                          headers={"Location": f"https://127.0.0.1:{fx0.port}{fx.path()}"})
                    sid2 = fresh_id()
                    reg2 = edge_reg(sid2, "https-same", fx0.url(hop2), tquote)
                    c2, o2, e2, _ = edge_run(sid2, reg2)
                    got2 = parse(o2)
                    ok2 = (c2 == 1 and len(got2) == 1
                           and got2[0] == (sid2, "UNREACHABLE", 6)
                           and "Traceback" not in (o2 + e2))
                    leg("EDGE_HTTPS",
                        c == 1 and got == [(sid, "REFUSED", 1)]
                        and fx2.hits.get(tpath, 0) == 0 and ok2,
                        f"cross={got} tgt_hits={fx2.hits.get(tpath, 0)} same_auth={got2} ok={ok2}")
                else:
                    leg("EDGE_HTTPS", False, "skipped")
            finally:
                fx2.close()
        else:
            for name in ("EDGE_SCHEMEREL", "EDGE_USERINFO", "EDGE_HTTPS"):
                leg(name, False, "skipped")

        if need("EDGE_MALTARG"):
            hop = "/em-" + fx.word()
            route(fx0, hop, [302], b"", headers={"Location": "http://127.0.0.1:99999/x"})
            sid = fresh_id()
            reg = edge_reg(sid, "maltarg", fx0.url(hop), " ".join(fx.words(10)))
            c, o, e, _ = edge_run(sid, reg)
            got = parse(o)
            leg("EDGE_MALTARG",
                c == 1 and len(got) == 1 and got[0] == (sid, "UNREACHABLE", 1)
                and "Traceback" not in (o + e),
                f"rows={got} exit={c} tb={'Traceback' in (o + e)}")
        else:
            leg("EDGE_MALTARG", False, "skipped")

        if need("EDGE_SLASHLESS"):
            base_p = "/dir-" + fx.word() + "/page"
            target_p = base_p.rsplit("/", 1)[0] + "/sub/x"
            root_target = "/sub/x"
            words = fx.words(12)
            shown = " ".join(words)
            shown = shown[0].upper() + shown[1:] + "."
            route(fx0, target_p, [200], html(f"<p>{' '.join(fx.words(20))}.</p><p>{shown}</p>"))
            route(fx0, base_p, [302], b"", headers={"Location": "sub/x"})
            sid = fresh_id()
            reg = edge_reg(sid, "slashless", fx0.url(base_p), shown)
            c, o, e, _ = edge_run(sid, reg)
            got = parse(o)
            leg("EDGE_SLASHLESS",
                c == 0 and got == [(sid, "LOCATED", 2)]
                and fx0.hits.get(target_p, 0) == 1
                and fx0.hits.get(root_target, 0) == 0
                and "Traceback" not in (o + e),
                f"rows={got} dir_hits={fx0.hits.get(target_p, 0)} root_hits={fx0.hits.get(root_target, 0)} exit={c}")
        else:
            leg("EDGE_SLASHLESS", False, "skipped")

        if need("EDGE_308"):
            t308 = "/t308-" + fx.word()
            w5 = fx.words(12)
            s308 = " ".join(w5)
            s308 = s308[0].upper() + s308[1:] + "."
            hop = "/e308-" + fx.word()
            route(fx0, hop, [308], b"", headers={"Location": t308})
            route(fx0, t308, [200], html(f"<p>{' '.join(fx.words(20))}.</p><p>{s308}</p>"))
            sid = fresh_id()
            reg = edge_reg(sid, "threeohheight", fx0.url(hop), s308)
            c, o, e, _ = edge_run(sid, reg)
            got = parse(o)
            leg("EDGE_308",
                c == 0 and got == [(sid, "LOCATED", 2)]
                and fx0.hits.get(t308, 0) == 1 and "Traceback" not in (o + e),
                f"rows={got} tgt_hits={fx0.hits.get(t308, 0)} exit={c}")
        else:
            leg("EDGE_308", False, "skipped")

        if need("EDGE_5TH200"):
            chain = ["/c%d-" % i + fx.word() for i in range(4)]
            final_p = "/cfin-" + fx.word()
            w5 = fx.words(12)
            s5 = " ".join(w5)
            s5 = s5[0].upper() + s5[1:] + "."
            for i, p in enumerate(chain):
                nxt = chain[i + 1] if i + 1 < len(chain) else final_p
                route(fx0, p, [302], b"", headers={"Location": nxt})
            route(fx0, final_p, [200], html(f"<p>{' '.join(fx.words(20))}.</p><p>{s5}</p>"))
            sid = fresh_id()
            reg = edge_reg(sid, "fivethen200", fx0.url(chain[0]), s5)
            c, o, e, _ = edge_run(sid, reg)
            got = parse(o, with_url=True)
            want_final = fx0.url(final_p)
            leg("EDGE_5TH200",
                c == 0 and got == [(sid, "LOCATED", 5, want_final)]
                and all(fx0.hits.get(p, 0) == 1 for p in chain + [final_p])
                and "Traceback" not in (o + e),
                f"rows={got} final={want_final} exit={c}")
        else:
            leg("EDGE_5TH200", False, "skipped")

        # ---- DRIP (round-64): a body delivered one chunk per period without
        # Content-Length (connection-close end) outlives the per-request wall
        # budget; a per-socket timeout cannot see it because every chunk lands
        # inside its own socket deadline.  Paired fast-body control. ----
        if need("DRIP"):
            drip_words = fx.words(12)
            drip_shown = " ".join(drip_words)
            drip_shown = drip_shown[0].upper() + drip_shown[1:] + "."
            drip_p = "/drip-" + fx.word()
            route(fx0, drip_p, [200], html(f"<p>{drip_shown}</p>"),
                  drip={"chunk": html(f"<p>{drip_shown}</p>"),
                        "period": 1.0, "count": 30})
            ok_p = "/dripok-" + fx.word()
            route(fx0, ok_p, [200], html(f"<p>{drip_shown}</p>"))
            d_sid, o_sid = fresh_id(), fresh_id()
            reg = os.path.join(work, f"DRIP-{d_sid}.md")
            open(reg, "w", encoding="utf-8").write(
                "| id | source |\n"
                f"| {d_sid} | drip \u2014 {fx0.url(drip_p)} | docs | B | s | anchor: \"{drip_shown}\" | t | mined | 2026-10-23 | 180d | x |\n"
                f"| {o_sid} | drip-ok \u2014 {fx0.url(ok_p)} | docs | B | s | anchor: \"{drip_shown}\" | t | mined | 2026-10-23 | 180d | x |\n")
            c, o, e, wall = run_tool(tool, work,
                ["--registry", reg, "--passes", "1", "--gap", "0",
                 "--timeout", "4", "--allow-private", d_sid, o_sid],
                timeout=180)
            got = parse(o)
            times = sorted(fx.times.get(drip_p, []))
            span = (times[-1] - times[0]) if len(times) >= 2 else 0.0
            leg("DRIP", c == 1
                and [(s, v) for s, v, _ in got] == [(d_sid, "UNREACHABLE"), (o_sid, "LOCATED")]
                and wall < 20 and len(times) == 3 and span >= 7.0
                and "Traceback" not in (o + e),
                f"rows={got} wall={wall:.1f}s drip_hits={len(times)} span={span:.1f}s tb={'Traceback' in (o + e)}")
        else:
            leg("DRIP", False, "skipped")

        # ---- MUT (round-64): the kill set.  Byte-patches against the lane
        # tool's committed source; every needle must occur exactly once.  Each
        # mutant is built under a scratch root's tools/ and run through this
        # counter's pinned legs; every pinned leg must FAIL. ----
        MUTANTS = [
            ("m1", "scheme-relative targets skip re-validation",
             'location = response.location\n        if not location:',
             'location = response.location\n        if location and location.lstrip().startswith("//"):\n            current = urllib.parse.urljoin(current, location.strip())\n            continue\n        if not location:',
             ["EDGE_SCHEMEREL"]),
            ("m10", "userinfo targets skip re-validation",
             'location = response.location\n        if not location:',
             'location = response.location\n        if location and "@" in urllib.parse.urlsplit(location).netloc:\n            current = urllib.parse.urljoin(current, location.strip())\n            continue\n        if not location:',
             ["EDGE_USERINFO"]),
            ("m2", "authority compared as raw netloc (userinfo over-refusal)",
             '_, host, port = parse_target(target)\n            _, source_host, source_port = parse_target(current)',
             '_tp = urllib.parse.urlsplit(target); _sp = urllib.parse.urlsplit(current)\n            host, port = _tp.netloc, 0\n            source_host, source_port = _sp.netloc, 0',
             ["EDGE_USERINFO"]),
            ("m3", "https targets skip re-validation",
             'location = response.location\n        if not location:',
             'location = response.location\n        if location and location.lstrip().lower().startswith("https"):\n            current = urllib.parse.urljoin(current, location.strip())\n            continue\n        if not location:',
             ["EDGE_HTTPS"]),
            ("m9", "malformed redirect target crashes (BadUrl propagates)",
             '        try:\n            _, host, port = parse_target(target)\n            _, source_host, source_port = parse_target(current)\n        except BadUrl as error:\n            raise FatalFetch("malformed redirect target: %s" % error)',
             '        _, host, port = parse_target(target)\n        _, source_host, source_port = parse_target(current)',
             ["EDGE_MALTARG"]),
            ("m5", "slashless relative Location resolved against the server root",
             'target = urllib.parse.urljoin(current, location.strip())',
             'parsed_location = urllib.parse.urlsplit(location.strip())\n        slashless_relative = (\n            not parsed_location.scheme\n            and not parsed_location.netloc\n            and parsed_location.path\n            and not parsed_location.path.startswith("/")\n        )\n        if slashless_relative:\n            target = urllib.parse.urljoin(current, "/" + location.strip())\n        else:\n            target = urllib.parse.urljoin(current, location.strip())',
             ["EDGE_SLASHLESS"]),
            ("m6", "308 not treated as a redirect",
             'REDIRECT_CODES = (301, 302, 303, 307, 308)',
             'REDIRECT_CODES = (301, 302, 303, 307)',
             ["EDGE_308"]),
            ("m7", "a 5th response that is 200 is never honoured",
             '    for _ in range(MAX_REQUESTS_PER_CHAIN):\n        counter[0] += 1\n        response = fetcher.fetch(current)\n        if response.status not in REDIRECT_CODES:\n            return response, current',
             '    for _i in range(MAX_REQUESTS_PER_CHAIN):\n        counter[0] += 1\n        response = fetcher.fetch(current)\n        if _i == MAX_REQUESTS_PER_CHAIN - 1:\n            raise FatalFetch("more than %d requests in one chain" % MAX_REQUESTS_PER_CHAIN)\n        if response.status not in REDIRECT_CODES:\n            return response, current',
             ["EDGE_5TH200"]),
            ("m8", "a 6th request allowed in the chain",
             'MAX_REQUESTS_PER_CHAIN = 5',
             'MAX_REQUESTS_PER_CHAIN = 6',
             ["GEN", "BOUND"]),
            ("mread", "greedy buffered read (drip outlives the wall budget)",
             'chunk = reader(want) if reader is not None else answer.read(want)',
             'chunk = answer.read(want)',
             ["DRIP"]),
        ]
        if need("MUT"):
            tool_text = open(tool, encoding="utf-8").read()
            mut_bad = []
            mut_kills = []
            mut_dir = os.path.join(work, "mutants")
            os.makedirs(mut_dir, exist_ok=True)
            for name, desc, needle, repl, pinned in MUTANTS:
                if tool_text.count(needle) != 1:
                    mut_bad.append(f"{name}:needle_count={tool_text.count(needle)}")
                    continue
                mroot = os.path.join(work, f"mroot-{name}")
                os.makedirs(os.path.join(mroot, "tools"))
                mp = os.path.join(mroot, "tools", "reopen-row.py")
                open(mp, "w", encoding="utf-8").write(
                    tool_text.replace(needle, repl, 1))
                open(os.path.join(mut_dir, f"{name}.py"), "w",
                     encoding="utf-8").write(tool_text.replace(needle, repl, 1))
                os.chmod(mp, 0o755)
                run_legs = (["EDGE_SCHEMEREL", "EDGE_SLASHLESS"]
                            if name == "m5" else pinned)
                mc, mo, me, mw = run_tool(os.path.abspath(__file__), work,
                    ["--root", mroot, "--only", ",".join(run_legs)],
                    timeout=900)
                lines = mo.splitlines()
                pinned_lines = [line for line in lines
                                if any(line.startswith(p + " ") for p in pinned)]
                # revision 1 (pre-data, forced by the rev-0 run receipt
                # reports/round-64/telemetry/final-measures-o.txt: every mutant's
                # pinned leg printed FAIL, but the old test compared the whole
                # string "LEG FAIL" for list membership, so all ten scored
                # pinned_fail=False and MUT was unpassable).
                failed = [line.split(" ", 1)[0] for line in pinned_lines
                          if any(line.startswith(p + " FAIL") for p in pinned)]
                pinned_fail = (len(pinned_lines) == len(pinned)
                               and len(failed) == len(pinned)
                               and set(failed) == set(pinned))
                selected_lines = [line for line in lines
                                  if any(line.startswith(p + " ") for p in run_legs)]
                mut_kills.append(
                    f"{name}->{'; '.join(selected_lines)}")
                if name == "m5":
                    scheme_lines = [line for line in selected_lines
                                    if line.startswith("EDGE_SCHEMEREL ")]
                    if (len(scheme_lines) != 1
                            or not scheme_lines[0].startswith("EDGE_SCHEMEREL PASS")):
                        mut_bad.append(
                            f"m5:EDGE_SCHEMEREL isolation={scheme_lines}")
                last = [l for l in lines if l.startswith("ACCEPT-O-65:")]
                if mc != 1 or not pinned_fail:
                    mut_bad.append(
                        f"{name}:exit={mc} pinned_fail={pinned_fail} "
                        f"pinned_lines={pinned_lines} last={last[:1]}")
            leg("MUT", not mut_bad,
                f"bad={mut_bad} mutants={len(MUTANTS)} kill_evidence={mut_kills}")
        else:
            leg("MUT", False, "skipped")
        # ---- FULL (round-65): re-execute the complete battery in a
        # subprocess on --root; a filtered-mode partial run can no longer be
        # presented as the verdict. ----
        if need("FULL"):
            run_legs_all = sorted(set(CORE) | set(EDGE) | {"TOOL", "DRIP", "MUT"})
            fc, fo, fe, fw = run_tool(os.path.abspath(__file__), work,
                                      ["--root", root, "--only", ",".join(run_legs_all)],
                                      timeout=1800)
            lines = fo.splitlines()
            # revision 3: digit-aware leg matching - the revision-1/2 regex
            # [A-Z_]+ is blind to EDGE_308/EDGE_5TH200 (digits), so the inner
            # battery scored 21/23 on a 100% green run and m6/m7 measured []
            # in MUTEX (forcing control .ufo/waves/round-65/w1/RevCounterO.md
            # V2/V3, with the dry-run-o.txt MUTEX m6/m7 NONE evidence).
            pass_lines = [l for l in lines if re.match(r"^[A-Z0-9_]+ PASS", l)]
            skip_lines = [l for l in lines if l.endswith(" SKIP")]
            fail_lines = [l for l in lines if re.match(r"^[A-Z0-9_]+ FAIL", l)]
            # revision 2: the subprocess necessarily SKIPs FULL/MUTEX/FRAG
            # themselves (recursion guard); exactly those three SKIP lines are
            # the only tolerable ones (forced by the base dry-run receipt:
            # FULL FAIL skip=3 pass=21/23 at base).
            self_skips = {"FULL SKIP", "MUTEX SKIP", "FRAG SKIP"}
            unexpected_skips = [l for l in skip_lines if l.strip() not in self_skips]
            expected_verdict = f"ACCEPT-O-65: PASS [filtered: {len(run_legs_all)}/{len(ALL_LEGS)} legs]"
            verdict_line = [l for l in lines if l.startswith("ACCEPT-O-65:")]
            leg("FULL", fc == 0 and not unexpected_skips and not fail_lines
                and len(pass_lines) == len(run_legs_all)
                and set(l.strip() for l in skip_lines) == self_skips
                and verdict_line == [expected_verdict],
                f"exit={fc} pass={len(pass_lines)}/{len(run_legs_all)} "
                f"skip={len(skip_lines)} unexpected_skip={unexpected_skips} fail={len(fail_lines)} wall={fw:.1f}s")
        else:
            leg("FULL", False, "skipped")

        # ---- MUTEX (round-65): exactness sweep. Every mutant through every
        # EDGE + DRIP fixture (GEN,BOUND for m8); the measured failing-leg set
        # must superset the pinned set and match the disclosed expectation
        # exactly (m1 +EDGE_USERINFO+EDGE_HTTPS; m2 +EDGE_MALTARG). ----
        SWEEP_EXPECT = {
            "m1": {"EDGE_SCHEMEREL"},
            "m2": {"EDGE_USERINFO", "EDGE_MALTARG"},
            "m3": {"EDGE_HTTPS"},
            "m9": {"EDGE_MALTARG"},
            "m5": {"EDGE_SLASHLESS"},
            "m6": {"EDGE_308"},
            "m7": {"EDGE_5TH200"},
            "m8": {"GEN", "BOUND"},
            "m10": {"EDGE_USERINFO"},
            "mread": {"DRIP"},
        }
        if need("MUTEX"):
            mutex_bad = []
            sweep_rows = []
            mutex_tool_text = open(src, encoding="utf-8").read()
            for name, desc, needle, repl, pinned in MUTANTS:
                if mutex_tool_text.count(needle) != 1:
                    mutex_bad.append(f"{name}:needle_count={mutex_tool_text.count(needle)}")
                    continue
                mroot = os.path.join(work, f"xroot-{name}")
                os.makedirs(os.path.join(mroot, "tools"))
                mp = os.path.join(mroot, "tools", "reopen-row.py")
                open(mp, "w", encoding="utf-8").write(
                    mutex_tool_text.replace(needle, repl, 1))
                os.chmod(mp, 0o755)
                legs_for = list(EDGE) + ["DRIP"]
                if name == "m8":
                    legs_for += ["GEN", "BOUND"]
                xc, xo, xe, xw = run_tool(os.path.abspath(__file__), work,
                                          ["--root", mroot, "--only", ",".join(legs_for)],
                                          timeout=1200)
                xlines = xo.splitlines()
                if xc != 1:
                    mutex_bad.append(f"{name}:sweep_exit={xc}")
                if "Traceback" in (xo + xe):
                    mutex_bad.append(f"{name}:sweep_traceback")
                failed = sorted(l.split(" ", 1)[0] for l in xlines
                                if re.match(r"^[A-Z0-9_]+ FAIL", l))
                sweep_rows.append(f"{name}:{'+'.join(failed) if failed else 'NONE'}")
                expect = SWEEP_EXPECT[name]
                if not set(pinned) <= set(failed):
                    mutex_bad.append(f"{name}:pinned_not_failed={sorted(set(pinned)-set(failed))}")
                if set(failed) != expect:
                    mutex_bad.append(f"{name}:measured={failed}!=expect={sorted(expect)}")
                if name == "m5":
                    scheme = [l for l in xlines if l.startswith("EDGE_SCHEMEREL ")]
                    if len(scheme) != 1 or not scheme[0].startswith("EDGE_SCHEMEREL PASS"):
                        mutex_bad.append(f"m5:isolation={scheme}")
            sweep_text = ("# mutant exactness sweep, claim O round 65\n"
                          "# counter: reports/round-65/accept-o.py; tool sha256 "
                          "c0f10a8450b425bb0959b00c18031fde43ac4809a5334538e9c1d4d9199568a0\n"
                          "# command per mutant: python3 -B reports/round-65/accept-o.py "
                          "--root <scratch>/xroot-<mutant> --only <EDGE_7>,DRIP[,GEN,BOUND m8]\n"
                          + "\n".join(sweep_rows) + "\n")
            sweep_path = os.path.join(root, "reports", "round-65", "telemetry",
                                      "exactness-sweep-o65.txt")
            committed = None
            if os.path.isfile(sweep_path):
                committed = open(sweep_path, encoding="utf-8").read()
            if committed is None:
                mutex_bad.append("exactness-sweep-o65.txt:not_committed")
            elif committed.splitlines()[-len(sweep_rows):] != sweep_rows:
                mutex_bad.append("exactness-sweep-o65.txt:stale_or_mismatch")
            else:
                tool_blob = open(os.path.join(root, TOOL), "rb").read()
                tool_sha = hashlib.sha256(tool_blob).hexdigest()
                if f"tool sha256 {tool_sha}" not in committed:
                    mutex_bad.append("exactness-sweep-o65.txt:tool_sha_mismatch")
            leg("MUTEX", not mutex_bad,
                f"bad={mutex_bad[:6]} mutants={len(MUTANTS)} table={sweep_rows}")
        else:
            leg("MUTEX", False, "skipped")

        # ---- FRAG (round-65): the durable fragment checker closes the
        # teaches-length and query-aware URL normalization gaps. ----
        if need("FRAG"):
            frag_tool = os.path.join(root, "tools", "check-row-fragments.py")
            frag_ok = False
            frag_detail = "not run"
            if os.path.isfile(frag_tool):
                st = subprocess.run([sys.executable, "-B", frag_tool, "--selftest"],
                                    cwd=root, stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE, timeout=300)
                sc = subprocess.run([sys.executable, "-B", frag_tool],
                                    cwd=root, stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE, timeout=300)
                # revision 2 (pre-data; forcing control: dry-run-o.txt
                # showed `FRAG PASS ... 0 finding(s) in 0 file(s)` - an empty
                # rows dir passed vacuously).  The scan must cover exactly the
                # 26 claim-C row fragments and find nothing.
                scan_last = sc.stdout.decode("utf-8", "replace").strip().splitlines()[-1:]
                m = re.search(r"in (\d+) file\(s\)", scan_last[0]) if scan_last else None
                files = int(m.group(1)) if m else -1
                frag_ok = (st.returncode == 0 and sc.returncode == 0
                           and "0 finding" in sc.stdout.decode("utf-8", "replace")
                           and files == 26)
                frag_detail = (f"selftest=exit{st.returncode} scan=exit{sc.returncode} "
                               f"files={files}/26 scan_out={scan_last}"
                               f" tb={'Traceback' in (st.stderr.decode('utf-8','replace') + sc.stderr.decode('utf-8','replace'))}")
            leg("FRAG", frag_ok, frag_detail)
        else:
            leg("FRAG", False, "skipped")

    finally:
        try:
            fx.close()
        finally:
            for sock in RESERVED:
                sock.close()
            shutil.rmtree(work, ignore_errors=True)
    verdict = all(legs)
    # revision 1: a `--only` partial run can no longer present as the verdict
    # (the round-64 filtered-green residual, `w2/OReceiptFresh.md`) — the
    # ACCEPT line carries an explicit filtered marker, and the FULL leg
    # re-executes the complete battery unfiltered.
    suffix = f" [filtered: {len(legs)}/{len(ALL_LEGS)} legs]" if only else ""
    print(f"ACCEPT-O-65: {'PASS' if verdict else 'FAIL'}{suffix}")
    return 0 if verdict else 1


if __name__ == "__main__":
    sys.exit(main())
