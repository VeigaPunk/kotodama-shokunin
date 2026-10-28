#!/usr/bin/env python3
"""Round-77 `capture-evidence.py` dry run on a local public fixture page.

Serves `fixture-page.html` on loopback twice:

  * `/fixture-page.html`                                  the LIVE page (200)
  * `/web/<ts>id_/http://127.0.0.1:<port>/fixture-page.html`  its same-page
    replay (200, `Memento-Datetime`) -- the archive-shaped URL the tool parses
    to prove the capture is this page's capture.

Then it runs the tool twice on those two fetches: once with
`--window-from live` and once with `--window-from wayback`, and writes each
run's verbatim stdout/stderr plus the evidence file into `dryrun/`.

The page is a fixture, not a source: nothing here is cited as evidence for a
registry row.  The claims document is `capture-block-rehearsal.json` (an
uncommitted rehearsal, so the receipts record `claims-frozen: no`); at the
round-77 freeze the same tool reads `reports/round-77/claims.json` through
`git show <freeze>:...` instead.

Scratch: `--work` is forwarded to the tool (which removes its own temporary
directory); this driver writes only under its own directory.
"""

import argparse
import hashlib
import os
import subprocess
import sys
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

HERE = os.path.dirname(os.path.abspath(__file__))
TOOL = os.path.join(HERE, "capture-evidence.py")
PAGE = os.path.join(HERE, "fixture-page.html")
CLAIMS = os.path.join(HERE, "capture-block-rehearsal.json")
OUTDIR = os.path.join(HERE, "dryrun")
TS = "20260101000000"
MEMENTO = "Thu, 01 Jan 2026 00:00:00 GMT"
QUOTE = ("The capture tool binds each User-Agent to the response that request "
         "received.")
ANCHOR = ("Same-page binding is read out of the replay path, never asserted by "
          "the caller.")


class Handler(BaseHTTPRequestHandler):
    """Two routes: the live page and its archive-shaped replay, plus 404."""

    live_path = "/fixture-page.html"
    replay_path = None
    body = b""
    seen = []

    def do_GET(self):                      # noqa: N802 - http.server API
        Handler.seen.append((self.path, self.headers.get("User-Agent")))
        if self.path == Handler.live_path:
            self._send(200, {})
        elif self.replay_path is not None and self.path == Handler.replay_path:
            self._send(200, {"Memento-Datetime": MEMENTO})
        else:
            self._send(404, {}, b"no such route\n", "text/plain; charset=utf-8")

    def _send(self, status, extra, body=None, ctype="text/html; charset=utf-8"):
        body = Handler.body if body is None else body
        self.send_response(status)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        for name, value in extra.items():
            self.send_header(name, value)
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args):
        pass


def main(argv):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--work", default=None,
                    help="scratch root forwarded to the tool (default: the "
                         "tool's own resolution order)")
    args = ap.parse_args(argv)

    server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    base = "http://127.0.0.1:%d" % server.server_address[1]
    Handler.live_path = "/fixture-page.html"
    Handler.replay_path = "/web/%sid_/%s%s" % (TS, base, Handler.live_path)
    with open(PAGE, "rb") as fh:
        Handler.body = fh.read()
    server_thread = threading.Thread(target=server.serve_forever, daemon=True)
    server_thread.start()
    os.makedirs(OUTDIR, exist_ok=True)

    runs = (("dry-fixture-live", ["--window-from", "live"]),
            ("dry-fixture-wayback", ["--window-from", "wayback"]))
    failures = 0
    try:
        for name, extra in runs:
            out = os.path.join(OUTDIR, name.upper() + ".txt")
            command = [sys.executable, "-B", TOOL, "--claims-file", CLAIMS,
                       "--id", name.upper(),
                       "--url", base + Handler.live_path,
                       "--wayback-url", base + Handler.replay_path,
                       "--quote", QUOTE, "--anchor-quote", ANCHOR,
                       "--locator", "fixture page, target section",
                       "--out", out] + extra
            if args.work:
                command += ["--work", args.work]
            proc = subprocess.run(command, capture_output=True, text=True)
            shown = " ".join(("'%s'" % part if " " in part else part)
                             for part in command)
            receipt = ["$ %s" % shown, proc.stdout.rstrip("\n"), proc.stderr.rstrip("\n"),
                       "exit=%d" % proc.returncode]
            if os.path.exists(out):
                with open(out, "rb") as fh:
                    raw = fh.read()
                receipt.append("evidence: %s bytes=%d sha256=%s"
                               % (os.path.relpath(out, HERE), len(raw),
                                  hashlib.sha256(raw).hexdigest()))
            receipt = "\n".join(line for line in receipt if line) + "\n"
            with open(os.path.join(OUTDIR, name + ".log"), "w", encoding="utf-8") as fh:
                fh.write(receipt)
            print(receipt, end="")
            if proc.returncode != 0:
                failures += 1
    finally:
        server.shutdown()
        server.server_close()

    print("DRY RUN %s: %d/%d runs exit 0"
          % ("OK" if failures == 0 else "FAILED", len(runs) - failures, len(runs)))
    return 0 if failures == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
