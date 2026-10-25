#!/usr/bin/env python3
r"""Round-74 claim-C evidence capture.

Fetches one URL, records what was actually served, and writes the evidence file
the claim-C EVIDENCE leg reads: `reports/round-74/evidence/<id>.txt`.

Why this exists.  The round-73 Gate files carried a self-attested
`quote-found-verbatim: yes` line and a hand-pasted "context window"; a forger
wrote either.  This tool derives every field of the file from one fetched body:
the fetch line (UA, HTTP status, bytes), the sha256 of those bytes, the
extracted visible text, and the window actually surrounding the located quote.
A seat can still hand-write an evidence file -- nothing here makes forgery
impossible -- but the honest path is one command, and the counter can re-run it.

Grammar written (keys required by round 74 first, then the round-73 keys kept
verbatim so an r73-shaped parser still reads the file):

  # evidence <id> — claim C GATE (round 74)
  url:            requested URL
  http:           HTTP status, or `file` for a local path
  bytes:          length of the stored body in bytes
  sha256:         64-hex digest of those bytes
  fetched:        UTC ISO-8601 second of the fetch
  ua:             exact User-Agent sent
  content-type:   response Content-Type (or a local-file guess)
  final-url:      url_effective after redirects
  extract:        the extraction performed and the text length
  quote-found:    yes | no   (after NFKC/NFKD + whitespace folding)
  quote-words:    whitespace tokens, `wc -w` reading
  quote-chars:    characters, `wc -m` reading
  quote-found-verbatim: yes | no  (exact substring of the extracted text)
  window:         chars=<n> min=<n> pad=<n> before=<n> after=<n>
  window-scope:   excerpt | whole-document (see the rule below)
  visible-chars:  characters of the whole extracted visible text, collapsed
  window-sha256:  sha256 of the stored window line (see the rule below)
  window-bytes:   byte length of that same string
  window-rule:    the hashing rule, restated inside the file
  fetch:          GET <url>                    (round-73 key)
  user-agent:     exact User-Agent             (round-73 key)
  access-date:    YYYY-MM-DD, local            (round-73 key)
  http-status:    HTTP status                  (round-73 key)
  content-length: response Content-Length or `-`
  transferred-bytes: curl %{size_download}; with --compressed this is the wire
                  size, so it is below `bytes:` on a gzipped response
  fetch-attempts: how many curl runs it took (transient resets are retried)
  fetch-command:  the literal curl argv, body/header paths elided
  locator:        the caller-supplied location of the quote
  normalise:      the folding that matched, and the tier
  quote:          the quote on one line (round-73 key)
  --- window ---
  <ONE line: >=4096 chars of extracted visible text around the quote,
   whitespace-collapsed, no leading or trailing whitespace>
  --- quote ---
  <the quote as supplied>

The window rule (claim C's final EVIDENCE leg, as amended).  The window is
stored as a single whitespace-collapsed line, so "the window text" is
unambiguous: it is the one line between the `--- window ---` marker line and the
`--- quote ---` marker line, with no trailing newline.

`window-scope: excerpt` is the ordinary case: at least `--min-window` (4096)
characters around the quote.  When the whole extracted visible text is shorter
than 4096 characters no excerpt can reach the minimum, so the tool stores the
whole text and declares `window-scope: whole-document`; the leg then requires the
stored text to be exactly that whole text, which is why the same run writes
`visible-chars:` (characters of the collapsed full text) and the verifier
requires `len(window) == visible-chars` *and* `visible-chars < 4096`.  A short
window under a long `visible-chars`, or a whole-document claim for a text that
could have been excerpted, is a verification failure.  `window-sha256:` is the sha256 of those
bytes as UTF-8, `window-bytes:` their length.  The counter recomputes both from
the stored line, and no flag in the file is read -- `quote-found` is recorded
for a human, not trusted by the grader.  After writing, the tool re-reads its
own file, extracts the window exactly as stored, recomputes the digest,
compares it with the header and checks the quote inside the window after
whole-string NFKC + whitespace folding (the same fold the counter uses); a
failure in any of those is exit 5, and the file is left on disk for inspection.
`--verify PATH` re-runs exactly that check later, on any evidence file.

`ua:`/`user-agent:` and `http:`/`http-status:` are deliberately duplicated: the
round-73 parser keys are `user-agent` and `http-status` and read the first
occurrence of each name, so both spellings must appear as their own lines.

Quote matching.  Tiers, strongest first: (1) exact substring of the extracted
text; (2) NFKC per character, every whitespace run collapsed to one space, ends
stripped; (3) the same with all whitespace removed -- a source line break inside
a Japanese or Chinese run must not stop a quote from matching; (4) and (5)
repeat (2) and (3) under NFKD, for bodies that use combining sequences.  Both
sides are folded identically and the fold carries an index map back to source
offsets, so the window is cut from the undecorated text.  Per-character NFKC
differs from whole-string NFKC only where composition crosses a character
boundary; that is why the NFKD retry exists.  `quote-found-verbatim: yes` is the
stronger claim and is what a Gate citation should carry; `normalise:` records
the tier that matched.

Bytes.  `bytes:`/`sha256:` always describe the decompressed body, so they equal
an uncompressed fetch of the same page (verified: the four candidate pages hash
to the same digests as the round-74 scouts' uncompressed captures).
`transferred-bytes:` is the wire size, below `bytes:` when the server negotiated
gzip; `content-length:` is `-` in that case because the response is chunked.

Fetching.  http(s) goes through curl with the browser-shaped User-Agent above,
`-L`, `--compressed`, a 20 s connect timeout and a 90 s total.  Transport
failures (curl exit 7/18/28/35/52/55/56) are retried with backoff -- one origin
in this round resets connections and aborts TLS handshakes intermittently --
and `fetch-attempts:` records how many runs it took.  HTTP-level failures are
never retried: a 404 is an answer.

Verification.  After writing, the tool re-reads its own file: it extracts the
window exactly as stored (the lines between the marker lines, joined by
newlines, no trailing newline), recomputes sha256 and the byte length, compares
them with `window-sha256:`/`window-bytes:`, checks the stored window is one
line of at least `--min-window` characters (default and floor 4096), and checks
the quote occurs in it after whole-string NFKC + whitespace folding -- the same
fold the claim's counter uses.  Any failure is exit 5 with the file left on disk.
`--verify PATH` repeats exactly that check on any evidence file later, which is
what a reviewer or a counter author can run without refetching.

Known limits.  The window is extracted visible text, not raw HTML, and `<head>`
is dropped, so a string that exists only in `<title>`/meta is not findable
unless the page repeats it in the body (all five pages do).  A body line
beginning with `--- ` inside a window would truncate a naive block parse; none
of the five pages' extracted text has one (checked 2026-10-25/26).  A quote that
matches only the whitespace-free tier -- a Japanese or Chinese sentence broken
by a source line break, written without that space -- is *found* and the file is
written, but verification fails (exit 5), because the counter's fold would not
confirm it: re-quote such a span rather than editing the evidence.

Dependencies: python3 stdlib, plus `curl` for http(s) and `pdftotext` for PDF
bodies.  No third-party Python.

Exit codes: 0 written and self-verified; 2 fetch/extract/usage error (no file);
3 written but the quote is not in the extracted text; 4 written but HTTP != 200;
5 written but self-verification failed (window digest, window length, status not
200, or the quote absent after NFKC+whitespace folding).  A file is written on
3, 4 and 5 on purpose: the failing capture is evidence too.

Usage:
  capture-evidence.py --id S881 --url https://example/x \
      --quote-file /tmp/ExecEvidence/q-S881.txt \
      --out reports/round-74/evidence/S881.txt --locator "h2 ..., para 3"
  capture-evidence.py --verify reports/round-74/evidence/S881.txt
  capture-evidence.py --selftest

`--allow-file` exists for the selftest only: it lets `--verify` accept
`http-status: file`, which a graded capture must never carry.
  capture-evidence.py --selftest
"""

import argparse
import hashlib
import html
import html.parser
import io
import os
import re
import shutil
import subprocess
import sys
import tempfile
import threading
import time
import unicodedata
import urllib.parse
from datetime import datetime, timezone
from contextlib import redirect_stderr, redirect_stdout
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

ROUND = "74"
UA_BROWSER = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
              "(KHTML, like Gecko) Chrome/130.0 Safari/537.36")
DEFAULT_PAD = 400
MIN_PAD = 400
MIN_WINDOW = 4096          # claim C: the stored window is >= 4096 characters
ACCESS_DATE = "2026-10-25"  # the round's access date; --verify enforces it

SKIP_TAGS = {"script", "style", "noscript", "template", "svg", "math", "head"}
BLOCK_TAGS = {
    "address", "article", "aside", "blockquote", "br", "dd", "details", "div",
    "dl", "dt", "fieldset", "figcaption", "figure", "footer", "form", "h1",
    "h2", "h3", "h4", "h5", "h6", "header", "hr", "li", "main", "nav", "ol",
    "p", "pre", "section", "table", "tbody", "td", "tfoot", "th", "thead",
    "tr", "ul", "caption", "summary",
}
ASCII_SPACE = re.compile(r"[ \t\r\f\v]+")


class CaptureError(Exception):
    """The capture could not be produced (fetch, decode or extraction)."""


# --------------------------------------------------------------------------
# fetch
# --------------------------------------------------------------------------

def _parse_headers(text):
    """Return the headers of the last response block in a curl -D dump."""
    blocks = [b for b in re.split(r"\r?\n\r?\n", text) if b.strip()]
    if not blocks:
        return {}
    out = {}
    for line in blocks[-1].splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            out.setdefault(k.strip().lower(), v.strip())
    return out


def _is_local(url):
    return url.startswith("file://") or (not re.match(r"^[a-z][a-z0-9+.-]*://", url)
                                         and os.path.exists(url))


def _local_path(url):
    if url.startswith("file://"):
        parts = urllib.parse.urlsplit(url)
        return urllib.parse.unquote(parts.path)
    return url


def _guess_type(path):
    low = path.lower()
    for suffix, ctype in ((".html", "text/html"), (".htm", "text/html"),
                          (".pdf", "application/pdf"), (".txt", "text/plain"),
                          (".md", "text/plain")):
        if low.endswith(suffix):
            return ctype
    return "text/plain"


def fetch(url, ua, tmpdir, retries=2):
    """Fetch `url`; return a dict with body bytes and the served metadata.

    Transport failures (curl exit 7/18/28/35/52/55/56) are retried `retries`
    times with a short backoff: the tuduku.space origin resets connections and
    aborts TLS handshakes intermittently (measured 2026-10-25), and a transient
    reset must not decide a Gate.  HTTP-level failures are never retried: a
    404 is an answer, not noise.
    """
    if _is_local(url):
        path = _local_path(url)
        try:
            with open(path, "rb") as fh:
                body = fh.read()
        except OSError as e:
            raise CaptureError("cannot read %s: %s" % (path, e))
        return {
            "http": "file",
            "final_url": url,
            "body": body,
            "headers": {},
            "content_type": _guess_type(path),
            "command": "(local file read, no fetch: %s)" % path,
            "ua_sent": "(none: local file)",
            "attempts": 1,
            "transferred": len(body),
        }

    body_path = os.path.join(tmpdir, "body.bin")
    header_path = os.path.join(tmpdir, "headers.txt")
    fmt = "%{http_code}\n%{url_effective}\n%{size_download}\n"
    argv = ["curl", "-sS", "-L", "--compressed",
            "--connect-timeout", "20", "--max-time", "90",
            "-A", ua, "-o", body_path, "-D", header_path,
            "-w", fmt, url]
    transient = {7, 18, 28, 35, 52, 55, 56}
    attempts = 0
    while True:
        attempts += 1
        try:
            proc = subprocess.run(argv, capture_output=True)
        except OSError as e:
            raise CaptureError("cannot run curl: %s" % e)
        if proc.returncode == 0:
            break
        detail = proc.stderr.decode("utf-8", "replace").strip()
        if proc.returncode not in transient or attempts > retries:
            raise CaptureError("curl exit %d after %d attempt(s): %s"
                               % (proc.returncode, attempts, detail))
        time.sleep(2 * attempts)
    fields = proc.stdout.decode("utf-8", "replace").splitlines()
    if len(fields) < 3:
        raise CaptureError("curl -w output not understood: %r" % proc.stdout)
    with open(body_path, "rb") as fh:
        body = fh.read()
    header_text = ""
    if os.path.exists(header_path):
        with open(header_path, "r", encoding="utf-8", errors="replace") as fh:
            header_text = fh.read()
    headers = _parse_headers(header_text)
    command = ("curl -sS -L --compressed --connect-timeout 20 --max-time 90 "
               "-A \"%s\" -o BODY -D HEADERS -w \"%s\" %s"
               % (ua, fmt.replace("\n", "\\n"), url))
    return {
        "http": fields[0].strip(),
        "final_url": fields[1].strip(),
        "body": body,
        "headers": headers,
        "content_type": headers.get("content-type", ""),
        "command": command,
        "ua_sent": ua,
        "attempts": attempts,
        "transferred": int(fields[2].strip() or 0),
    }


# --------------------------------------------------------------------------
# decode + extract
# --------------------------------------------------------------------------

def decode(body, content_type):
    """Decode bytes to text, honouring Content-Type, <meta charset=...> and BOM."""
    charset = None
    match = re.search(r"charset\s*=\s*\"?([A-Za-z0-9_.:-]+)", content_type or "", re.I)
    if match:
        charset = match.group(1)
    if charset is None:
        head = body[:8192].decode("latin-1", "replace")
        match = re.search(r"<meta[^>]+charset\s*=\s*[\"']?([A-Za-z0-9_.:-]+)", head, re.I)
        if match:
            charset = match.group(1)
    if charset is None:
        for bom, name in ((b"\xef\xbb\xbf", "utf-8-sig"),
                          (b"\xff\xfe", "utf-16"), (b"\xfe\xff", "utf-16")):
            if body.startswith(bom):
                charset = name
                break
    tried = []
    for candidate in [charset, "utf-8", "gb18030", "big5", "shift_jis",
                      "euc-jp", "cp1251", "cp1252"]:
        if not candidate:
            continue
        if candidate in tried:
            continue
        tried.append(candidate)
        try:
            return body.decode(candidate), candidate
        except (LookupError, UnicodeDecodeError):
            continue
    return body.decode("utf-8", "replace"), "utf-8/replace"


class _TextExtractor(html.parser.HTMLParser):
    """Visible text of an HTML body: tags dropped, block tags break lines."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []
        self.skip_depth = 0
        self.tags_in_skip = []

    def handle_starttag(self, tag, attrs):
        if self.skip_depth:
            if tag in SKIP_TAGS:
                self.tags_in_skip.append(tag)
                self.skip_depth += 1
            return
        if tag in SKIP_TAGS:
            self.tags_in_skip.append(tag)
            self.skip_depth = 1
            return
        if tag in BLOCK_TAGS:
            self.parts.append("\n")

    def handle_startendtag(self, tag, attrs):
        if not self.skip_depth and tag in BLOCK_TAGS:
            self.parts.append("\n")

    def handle_endtag(self, tag):
        if self.skip_depth:
            if self.tags_in_skip and tag == self.tags_in_skip[-1]:
                self.tags_in_skip.pop()
                self.skip_depth -= 1
            return
        if tag in BLOCK_TAGS:
            self.parts.append("\n")

    def handle_data(self, data):
        if not self.skip_depth:
            self.parts.append(data)


def html_to_text(markup):
    parser = _TextExtractor()
    parser.feed(markup)
    parser.close()
    raw = "".join(parser.parts)
    raw = html.unescape(raw)
    lines = []
    for line in raw.split("\n"):
        line = ASCII_SPACE.sub(" ", line).strip()
        if line:
            lines.append(line)
    return "\n".join(lines)


def extract_text(body, content_type, tmpdir):
    """Return (text, extract-line description)."""
    ctype = (content_type or "").lower()
    if ctype.startswith("application/pdf") or body[:5] == b"%PDF-":
        body_path = os.path.join(tmpdir, "body.pdf")
        with open(body_path, "wb") as fh:
            fh.write(body)
        if shutil.which("pdftotext") is None:
            raise CaptureError("PDF body but pdftotext is not installed")
        proc = subprocess.run(["pdftotext", "-enc", "UTF-8", body_path, "-"],
                              capture_output=True)
        if proc.returncode != 0:
            raise CaptureError("pdftotext exit %d: %s"
                               % (proc.returncode,
                                  proc.stderr.decode("utf-8", "replace").strip()[:400]))
        text = proc.stdout.decode("utf-8", "replace")
        text = "\n".join(line.rstrip() for line in text.splitlines())
        return text, ("pdftotext -enc UTF-8 BODY - (stdlib subprocess); %d chars"
                      % len(text))

    decoded, charset = decode(body, content_type)
    if ctype.startswith("text/html") or re.search(r"<(html|body|p|div|h1)\b",
                                                  decoded[:16384], re.I):
        text = html_to_text(decoded)
        return text, ("html->text via stdlib html.parser (comments and "
                      "script/style/noscript/template/svg/head dropped, block "
                      "tags -> newline, entities decoded, blank lines dropped, "
                      "intra-line ASCII spaces collapsed); charset=%s; %d chars"
                      % (charset, len(text)))
    text = "\n".join(line.rstrip() for line in decoded.splitlines())
    return text, "plain text decode; charset=%s; %d chars" % (charset, len(text))


# --------------------------------------------------------------------------
# normalise + locate
# --------------------------------------------------------------------------

def fold(text, form="NFKC", keep_space=True):
    """NFKC/NFKD per character + whitespace fold, with a map to source offsets.

    Returns (folded, index) where index[i] is the offset in `text` of the
    character that produced folded[i].  Leading and trailing whitespace is
    dropped; every internal whitespace run becomes one space, or is removed
    entirely when `keep_space` is False (the CJK tier: a source line break
    inside an unspaced run must not stop a quote from matching).
    """
    out = []
    index = []
    started = False
    pending = None
    for i, ch in enumerate(text):
        if ch.isspace():
            if started and keep_space and pending is None:
                pending = i
            continue
        expanded = unicodedata.normalize(form, ch)
        if not expanded:
            continue
        if pending is not None:
            out.append(" ")
            index.append(pending)
            pending = None
        for c in expanded:
            out.append(c)
            index.append(i)
        started = True
    return "".join(out), index


def locate(text, quote):
    """Find `quote` in `text`.

    Tiers, strongest first: exact substring; NFKC fold with spaces collapsed;
    NFKC fold with all whitespace removed; the same two under NFKD.  The tier
    that matched is reported so a reader can tell a verbatim hit from a
    normalised one from a whitespace-insensitive one.
    """
    verbatim = text.find(quote)
    if verbatim >= 0:
        return {"found": True, "verbatim": True, "form": "NFKC",
                "tier": "verbatim",
                "start": verbatim, "end": verbatim + len(quote)}
    tiers = (("folded", True), ("folded-no-space", False))
    for form in ("NFKC", "NFKD"):
        for tier, keep_space in tiers:
            haystack, index = fold(text, form, keep_space)
            needle = fold(quote, form, keep_space)[0]
            if not needle:
                continue
            pos = haystack.find(needle)
            if pos < 0:
                continue
            start = index[pos]
            end = index[pos + len(needle) - 1] + 1
            return {"found": True, "verbatim": False, "form": form,
                    "tier": tier, "start": start, "end": end}
    return {"found": False, "verbatim": False, "form": None, "tier": None,
            "start": None, "end": None}


def collapse(text):
    """Every whitespace run folded to one space, ends stripped."""
    return re.sub(r"\s+", " ", text).strip()


def nfkc_ws(text):
    """The counter's fold: whole-string NFKC, then whitespace collapsed."""
    return collapse(unicodedata.normalize("NFKC", text))


def make_window(text, hit, pad, min_window, quote):
    """Whitespace-collapsed window of >= min_window chars around the quote.

    Symmetric where the text allows it; near a document edge the window slides
    into the remaining text so the minimum is still met when the document is
    long enough.  A document shorter than the minimum yields its whole text and
    the caller fails the capture (exit 5) instead of storing a short window.
    """
    span = hit["end"] - hit["start"]
    want = max(pad, (min_window - span) // 2 + 4)
    start = max(0, hit["start"] - want)
    end = min(len(text), hit["end"] + want)
    for _ in range(8):
        chunk = collapse(text[start:end])
        if len(chunk) >= min_window or (start == 0 and end == len(text)):
            return chunk
        need = min_window - len(chunk) + 2
        if end < len(text):
            end = min(len(text), end + need)
        elif start > 0:
            start = max(0, start - need)
        else:
            return chunk
    return collapse(text[start:end])


# --------------------------------------------------------------------------
# render
# --------------------------------------------------------------------------

def render(ident, url, meta, body, text, extract_line, quote, hit, locator,
           pad, min_window, window_text, scope, visible_chars):
    """Build the evidence file text and the body and window digests."""
    digest = hashlib.sha256(body).hexdigest()
    now = datetime.now(timezone.utc)
    content_length = meta["headers"].get("content-length", "-") if meta["headers"] else "-"
    if hit["found"] and window_text:
        window_bytes = window_text.encode("utf-8")
        window_digest = hashlib.sha256(window_bytes).hexdigest()
        inner = locate(window_text, quote)
        before = inner["start"] if inner["found"] else -1
        after = len(window_text) - inner["end"] if inner["found"] else -1
        window_line = ("window: chars=%d min=%d pad=%d before=%d after=%d"
                       % (len(window_text), min_window, pad, before, after))
        normalise = ("normalise: %s(per-character)+whitespace-fold; matched=%s"
                     % (hit["form"], hit["tier"]))
    else:
        window_text = ""
        window_bytes = b""
        window_digest = hashlib.sha256(window_bytes).hexdigest()
        window_line = ("window: chars=0 min=%d pad=%d before=n/a after=n/a"
                       % (min_window, pad))
        normalise = "normalise: NFKC,NFKD(per-character)+whitespace-fold; matched=none"

    quote_line = collapse(quote)

    lines = [
        "# evidence %s — claim C GATE (round %s)" % (ident, ROUND),
        "url: %s" % url,
        "http: %s" % meta["http"],
        "bytes: %d" % len(body),
        "sha256: %s" % digest,
        "fetched: %s" % now.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "ua: %s" % meta["ua_sent"],
        "content-type: %s" % (meta["content_type"] or "unknown"),
        "final-url: %s" % meta["final_url"],
        "extract: %s" % extract_line,
        "quote-found: %s" % ("yes" if hit["found"] else "no"),
        "quote-words: %d" % len(quote.split()),
        "quote-chars: %d" % len(quote),
        "quote-found-verbatim: %s" % ("yes" if hit["verbatim"] else "no"),
        window_line,
        "window-scope: %s" % scope,
        "visible-chars: %d" % visible_chars,
        "window-sha256: %s" % window_digest,
        "window-bytes: %d" % len(window_bytes),
        "window-rule: sha256 of the single stored window line, UTF-8, no trailing newline",
        "fetch: GET %s" % url,
        "user-agent: %s" % meta["ua_sent"],
        "access-date: %s" % datetime.now().strftime("%Y-%m-%d"),
        "http-status: %s" % meta["http"],
        "content-length: %s" % content_length,
        "transferred-bytes: %d" % meta["transferred"],
        "fetch-attempts: %d" % meta["attempts"],
        "fetch-command: %s" % meta["command"],
        "locator: %s" % (locator or "(none supplied)"),
        normalise,
        "quote: %s" % quote_line,
        "--- window ---",
        window_text,
        "--- quote ---",
        quote,
    ]
    return "\n".join(lines) + "\n", digest, window_digest


# --------------------------------------------------------------------------
# read back + verify
# --------------------------------------------------------------------------

def parse_evidence(text):
    """Header keys of an evidence file; the first occurrence of each name wins."""
    out = {}
    for line in text.splitlines():
        match = re.match(r"^([A-Za-z][A-Za-z0-9_-]*):\s*(.*)$", line)
        if match and match.group(1).lower() not in out:
            out[match.group(1).lower()] = match.group(2)
    return out


def stored_window(text):
    """The window exactly as stored: the lines between the two markers, joined
    by newlines, no trailing newline.  A window is written as one line, so this
    is that line."""
    lines = text.splitlines()
    start = None
    for i, line in enumerate(lines):
        if line.strip() == "--- window ---":
            start = i + 1
            break
    if start is None:
        return None
    body = []
    for line in lines[start:]:
        if line.strip() == "--- quote ---":
            while body and body[-1] == "":
                body.pop()
            return "\n".join(body)
        body.append(line)
    return None


def stored_quote(text):
    """The quote block, verbatim; empty when the block is absent."""
    marker = "\n--- quote ---\n"
    if marker not in text:
        return ""
    return text.split(marker, 1)[1]


REQUIRED_KEYS = ("url", "fetch", "user-agent", "access-date", "http-status",
                 "bytes", "sha256", "locator", "quote-words", "quote-chars",
                 "window-sha256", "window-bytes", "window-scope", "visible-chars")


def verify_file(path, quote=None, min_window=MIN_WINDOW, allow_file=False):
    """Re-read an evidence file and check it the way the counter will.

    Returns (problems, header, window).  Checks: the required keys exist; the
    status is 200 and the access date is the round's; the stored window is one
    line of >= min_window characters; its sha256 and byte length match the
    header (`window-sha256` recomputed from the stored bytes); and the quote
    occurs in it after whole-string NFKC + whitespace folding.

    The amended leg: `window-scope: excerpt` needs >= min_window characters and
    cannot exceed the whole text; `window-scope: whole-document` is allowed only
    when the whole extracted visible text is shorter than min_window, and then
    the stored window must BE that whole text -- its length must equal
    `visible-chars:`, written by the same run from the same extraction.
    """
    try:
        with open(path, "r", encoding="utf-8") as fh:
            text = fh.read()
    except OSError as e:
        return ["cannot read %s: %s" % (path, e)], {}, ""
    head = parse_evidence(text)
    win = stored_window(text)
    problems = []
    for key in REQUIRED_KEYS:
        if not head.get(key):
            problems.append("missing header key %r" % key)
    status = head.get("http-status")
    if status != "200" and not (allow_file and status == "file"):
        problems.append("http-status %r (want 200)" % status)
    if head.get("access-date") != ACCESS_DATE:
        problems.append("access-date %r (want %s)" % (head.get("access-date"), ACCESS_DATE))
    if win is None:
        problems.append("no --- window --- block")
        return problems, head, ""
    payload = win.encode("utf-8")
    recomputed = hashlib.sha256(payload).hexdigest()
    if head.get("window-sha256") != recomputed:
        problems.append("window-sha256 mismatch: header %r recomputed %s"
                        % (head.get("window-sha256"), recomputed))
    if head.get("window-bytes") != str(len(payload)):
        problems.append("window-bytes %r (stored %d)" % (head.get("window-bytes"), len(payload)))
    if "\n" in win:
        problems.append("window is not stored as a single line")
    scope = head.get("window-scope")
    try:
        visible = int(head.get("visible-chars", ""))
    except ValueError:
        visible = None
    if scope == "excerpt":
        if len(win) < min_window:
            problems.append("window is %d characters (want >= %d for an excerpt)"
                            % (len(win), min_window))
        if visible is not None and len(win) > visible:
            problems.append("window is longer than the whole text (%d > %d)"
                            % (len(win), visible))
    elif scope == "whole-document":
        if visible is None:
            problems.append("visible-chars is not an integer (%r)"
                            % head.get("visible-chars"))
        else:
            if len(win) != visible:
                problems.append("whole-document window is %d characters but "
                                "visible-chars says %d" % (len(win), visible))
            if visible >= min_window:
                problems.append("whole-document claimed for a %d-character text "
                                "(>= %d): store an excerpt instead"
                                % (visible, min_window))
    else:
        problems.append("window-scope %r (want excerpt or whole-document)" % scope)
    wanted = quote if quote is not None else (stored_quote(text).strip() or head.get("quote", ""))
    if not wanted:
        problems.append("no quote to check")
    elif nfkc_ws(wanted) not in nfkc_ws(win):
        problems.append("quote absent from the stored window after NFKC+whitespace fold")
    return problems, head, win


def verify_command(args):
    quote = None
    if args.quote or args.quote_file:
        quote = read_quote(args)
    problems, head, win = verify_file(args.verify, quote, args.min_window,
                                      args.allow_file)
    for problem in problems:
        print("VERIFY %s: %s" % (args.verify, problem), file=sys.stderr)
    if problems:
        print("VERIFY FAIL: %s (%d problem(s))" % (args.verify, len(problems)))
        return 5
    print("VERIFY OK: %s window-sha256=%s window-bytes=%d window-chars=%d "
          "quote-in-window=yes access-date=%s http-status=%s"
          % (args.verify, head["window-sha256"], len(win.encode("utf-8")),
             len(win), head["access-date"], head["http-status"]))
    return 0


# --------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------

def parse_args(argv):
    ap = argparse.ArgumentParser(
        prog="capture-evidence.py",
        description="Capture one URL's bytes and quote into a round-74 evidence file.")
    ap.add_argument("--id", help="evidence id (default: the --out file stem)")
    ap.add_argument("--url", help="URL to fetch (http(s)://, file:// or a path)")
    group = ap.add_mutually_exclusive_group()
    group.add_argument("--quote", help="the quoted span, verbatim")
    group.add_argument("--quote-file", help="file holding the quoted span")
    ap.add_argument("--out", help="evidence file to write (reports/round-%s/evidence/<id>.txt)"
                    % ROUND)
    ap.add_argument("--locator", default="", help="where the quote sits in the page")
    ap.add_argument("--ua", default=UA_BROWSER, help="User-Agent to send (recorded verbatim)")
    ap.add_argument("--retries", type=int, default=2,
                    help="retries after a transient curl transport failure "
                         "(default 2; HTTP errors are never retried)")
    ap.add_argument("--pad", type=int, default=DEFAULT_PAD,
                    help="floor for the symmetric window pad (min %d)" % MIN_PAD)
    ap.add_argument("--min-window", type=int, default=MIN_WINDOW,
                    help="minimum stored window characters (min %d)" % MIN_WINDOW)
    ap.add_argument("--verify", metavar="PATH",
                    help="re-verify an existing evidence file and exit")
    ap.add_argument("--allow-file", action="store_true",
                    help="with --verify: accept `http-status: file` (local fixtures only; "
                         "a graded capture must be HTTP 200)")
    ap.add_argument("--selftest", action="store_true", help="run the fixture suite")
    args = ap.parse_args(argv)

    if args.selftest or args.verify:
        if args.min_window < MIN_WINDOW:
            ap.error("--min-window %d is below the grammar minimum of %d"
                     % (args.min_window, MIN_WINDOW))
        return args
    missing = [name for name in ("url", "out")
               if not getattr(args, name)]
    if not (args.quote or args.quote_file):
        missing.append("quote|quote-file")
    if missing:
        ap.error("missing required argument(s): %s" % ", ".join(missing))
    if args.pad < MIN_PAD:
        ap.error("--pad %d is below the grammar minimum of %d" % (args.pad, MIN_PAD))
    if args.min_window < MIN_WINDOW:
        ap.error("--min-window %d is below the grammar minimum of %d"
                 % (args.min_window, MIN_WINDOW))
    return args


def read_quote(args):
    if args.quote_file:
        try:
            with open(args.quote_file, "r", encoding="utf-8") as fh:
                quote = fh.read()
        except OSError as e:
            raise CaptureError("cannot read --quote-file: %s" % e)
    else:
        quote = args.quote
    quote = quote.strip()
    if not quote:
        raise CaptureError("quote is empty")
    return quote


def capture(args):
    quote = read_quote(args)
    ident = args.id or os.path.splitext(os.path.basename(args.out))[0]
    tmpdir = tempfile.mkdtemp(prefix="capture-evidence-")
    try:
        meta = fetch(args.url, args.ua, tmpdir, args.retries)
        text, extract_line = extract_text(meta["body"], meta["content_type"], tmpdir)
        hit = locate(text, quote)
        visible = collapse(text)
        if not hit["found"]:
            scope = "none"
            window_text = ""
        elif len(visible) < args.min_window:
            # the document is shorter than the window minimum: store all of it,
            # and say so -- an excerpt rule cannot be met by a smaller document
            scope = "whole-document"
            window_text = visible
        else:
            scope = "excerpt"
            window_text = make_window(text, hit, args.pad, args.min_window, quote)
        document, digest, window_digest = render(
            ident, args.url, meta, meta["body"], text, extract_line, quote, hit,
            args.locator, args.pad, args.min_window, window_text,
            scope, len(visible))
        out_dir = os.path.dirname(os.path.abspath(args.out))
        if out_dir:
            os.makedirs(out_dir, exist_ok=True)
        with open(args.out, "w", encoding="utf-8") as fh:
            fh.write(document)
        print("EVIDENCE %s: quote-found=%s verbatim=%s http=%s bytes=%d sha256=%s "
              "window-chars=%d window-scope=%s window-sha256=%s -> %s"
              % (ident, "yes" if hit["found"] else "no",
                 "yes" if hit["verbatim"] else "no", meta["http"],
                 len(meta["body"]), digest[:16], len(window_text), scope,
                 window_digest[:16], args.out))
        if meta["http"] not in ("200", "file"):
            print("EVIDENCE %s: HTTP %s is not 200 — the capture is not citable"
                  % (ident, meta["http"]), file=sys.stderr)
            return 4
        if not hit["found"]:
            print("EVIDENCE %s: quote not found in the extracted text — the "
                  "capture is not citable" % ident, file=sys.stderr)
            return 3
        problems, head, win = verify_file(args.out, quote, args.min_window,
                                          allow_file=(meta["http"] == "file"))
        for problem in problems:
            print("EVIDENCE %s: verify: %s" % (ident, problem), file=sys.stderr)
        if problems:
            print("VERIFY FAIL: %s (%d problem(s)); the file was left on disk"
                  % (args.out, len(problems)))
            return 5
        print("VERIFY OK: %s window-sha256=%s window-bytes=%d window-chars=%d "
              "quote-in-window=yes" % (args.out, head["window-sha256"],
                                       len(win.encode("utf-8")), len(win)))
        return 0
    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)


def main(argv):
    args = parse_args(argv)
    if args.selftest:
        return selftest()
    try:
        if args.verify:
            return verify_command(args)
        return capture(args)
    except CaptureError as e:
        print("ERROR: %s" % e, file=sys.stderr)
        return 2


# --------------------------------------------------------------------------
# selftest
# --------------------------------------------------------------------------

FILLER = "見出しの前後の本文です。" * 400       # 4400 chars, CJK
CJK_QUOTE = "世界観の作り方は、一つの場所に集めることです。"
SPACED_QUOTE = "設定ノートの構成例 です。"
LATIN_QUOTE = "The settings note holds five sections in one file."
EDGE_QUOTE = "冒頭の一文です。"
SHORT_QUOTE = "短い文書の一文です。"


def _fixture_html():
    return """<!doctype html>
<html lang="ja"><head><meta charset="utf-8"><title>fixture title</title>
<script>var SCRIPT_ONLY_TEXT = 1;</script>
<style>.STYLE_ONLY_TEXT { color: red; }</style></head>
<body>
<p>%s</p>
<p>%s</p>
<p>ＡＢＣ１２３ の全角ラテン</p>
<p>設定ノートの
   構成例 です。</p>
<p>The settings note holds  five sections
 in one file.</p>
<p>アンパサンド &amp; と山括弧 &lt;tag&gt;</p>
<p>%s</p>
<!-- COMMENT_ONLY_TEXT -->
</body></html>
""" % (FILLER, CJK_QUOTE, FILLER)


def _fixture_edge_html():
    return "<html><body><p>%s</p><p>%s</p></body></html>" % (EDGE_QUOTE, FILLER)


def _minimal_pdf(sentence, filler="Evidence window filler line for the PDF fixture."):
    """A one-page PDF of 96 Helvetica lines with the quote at line 48, xref
    offsets computed.  Leading 7pt from y=740 keeps every line inside the page
    box, so pdftotext extracts them all and a >=4096-character window exists."""
    body = ["BT /F1 6 Tf 7 TL 36 740 Td"]
    for number in range(96):
        text = sentence if number == 48 else "%s %03d" % (filler, number)
        body.append("(%s) Tj T*" % text)
    body.append("ET")
    content = "\n".join(body).encode("ascii")
    objects = [
        b"<</Type/Catalog/Pages 2 0 R>>",
        b"<</Type/Pages/Kids[3 0 R]/Count 1>>",
        b"<</Type/Page/Parent 2 0 R/MediaBox[0 0 612 792]"
        b"/Resources<</Font<</F1 4 0 R>>>>/Contents 5 0 R>>",
        b"<</Type/Font/Subtype/Type1/BaseFont/Helvetica>>",
        b"<</Length %d>>stream\n%s\nendstream" % (len(content), content),
    ]
    out = bytearray(b"%PDF-1.4\n")
    offsets = []
    for number, payload in enumerate(objects, start=1):
        offsets.append(len(out))
        out += b"%d 0 obj\n" % number + payload + b"\nendobj\n"
    xref_at = len(out)
    out += b"xref\n0 %d\n" % (len(objects) + 1)
    out += b"0000000000 65535 f \n"
    for offset in offsets:
        out += b"%010d 00000 n \n" % offset
    out += (b"trailer\n<</Size %d/Root 1 0 R>>\nstartxref\n%d\n%%%%EOF\n"
            % (len(objects) + 1, xref_at))
    return bytes(out)


class _FixtureHandler(BaseHTTPRequestHandler):
    """Serves /fixture.html (200), /missing.html (404) and /flaky.html (a body
    shorter than its Content-Length the first `flaky` times), recording the UA."""

    payload = b""
    seen = []
    flaky = {"left": 0}

    def do_GET(self):                      # noqa: N802 - http.server API
        _FixtureHandler.seen.append((self.path, self.headers.get("User-Agent")))
        if self.path == "/flaky.html" and _FixtureHandler.flaky["left"] > 0:
            _FixtureHandler.flaky["left"] -= 1
            body = _FixtureHandler.payload
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body) + 5000))
            self.end_headers()
            self.wfile.write(body)
            self.close_connection = True
            return
        if self.path == "/missing.html":
            body = b"<html><body><p>not here</p></body></html>"
            self.send_response(404)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        body = _FixtureHandler.payload
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args):          # silence the selftest's stderr
        pass


def _read(path):
    with open(path, "r", encoding="utf-8") as fh:
        return fh.read()


def _header_map(text):
    """First occurrence of each `key: value` line wins."""
    out = {}
    for line in text.splitlines():
        match = re.match(r"^([a-z0-9-]+):\s*(.*)$", line)
        if match and match.group(1) not in out:
            out[match.group(1)] = match.group(2)
    return out


def _block(text, name):
    """Body of a `--- name ---` block, up to the next `--- ` header."""
    marker = "--- %s ---" % name
    if marker not in text:
        return None
    rest = text.split(marker, 1)[1]
    if rest.startswith("\n"):
        rest = rest[1:]
    nxt = rest.find("\n--- ")
    return rest if nxt < 0 else rest[:nxt]


def _run(argv):
    """Run main() in-process, capturing stdout/stderr."""
    out, err = io.StringIO(), io.StringIO()
    with redirect_stdout(out), redirect_stderr(err):
        try:
            code = main(argv)
        except SystemExit as e:            # argparse usage errors
            code = e.code if isinstance(e.code, int) else 2
    return code, out.getvalue(), err.getvalue()


def selftest():
    tmp = tempfile.mkdtemp(prefix="capture-evidence-selftest-")
    results = []

    def check(name, ok, detail=""):
        results.append((name, bool(ok), detail))
        return bool(ok)

    html_path = os.path.join(tmp, "fixture.html")
    edge_path = os.path.join(tmp, "edge.html")
    short_path = os.path.join(tmp, "short.html")
    with open(html_path, "w", encoding="utf-8") as fh:
        fh.write(_fixture_html())
    with open(edge_path, "w", encoding="utf-8") as fh:
        fh.write(_fixture_edge_html())
    with open(short_path, "w", encoding="utf-8") as fh:
        fh.write("<html><body><p>%s</p><p>ほんの少しの本文です。</p></body></html>"
                 % SHORT_QUOTE)
    ev = os.path.join(tmp, "evidence")

    try:
        # 1. file:// + CJK: the full round-74 grammar, window >= 4096, digest
        out1 = os.path.join(ev, "F1.txt")
        code, outlog, err = _run(["--id", "F1", "--url", "file://" + html_path,
                                  "--quote", CJK_QUOTE, "--out", out1,
                                  "--locator", "fixture p2", "--allow-file"])
        text1 = _read(out1) if os.path.exists(out1) else ""
        head1 = _header_map(text1)
        window1 = _block(text1, "window") or ""
        quote1 = _block(text1, "quote") or ""
        geo = re.match(r"chars=(\d+) min=(\d+) pad=(\d+) before=(\d+) after=(\d+)",
                       head1.get("window", ""))
        required = ["url", "http", "bytes", "sha256", "fetched", "ua", "quote-found",
                    "quote-words", "quote-chars", "quote-found-verbatim", "window",
                    "window-sha256", "window-bytes", "window-rule"]
        legacy = ["fetch", "user-agent", "access-date", "http-status", "extract",
                  "locator", "quote", "quote-words", "sha256", "bytes"]
        digest_ok = (head1.get("window-sha256")
                     == hashlib.sha256(window1.encode("utf-8")).hexdigest())
        check("file-cjk-window",
              code == 0
              and head1.get("quote-found") == "yes"
              and head1.get("quote-found-verbatim") == "yes"
              and geo is not None
              and int(geo.group(1)) >= 4096 and int(geo.group(1)) == len(window1)
              and int(geo.group(4)) >= 400 and int(geo.group(5)) >= 400
              and "\n" not in window1
              and nfkc_ws(CJK_QUOTE) in nfkc_ws(window1)
              and digest_ok
              and head1.get("window-bytes") == str(len(window1.encode("utf-8")))
              and head1.get("window-scope") == "excerpt"
              and int(head1.get("visible-chars", "0")) >= len(window1)
              and quote1.strip() == CJK_QUOTE
              and all(k in head1 for k in required)
              and all(k in head1 for k in legacy)
              and head1.get("access-date") == ACCESS_DATE
              and head1.get("quote-chars") == str(len(CJK_QUOTE))
              and "VERIFY OK" in outlog
              and re.fullmatch(r"[0-9a-f]{64}", head1.get("sha256", "")) is not None,
              "exit=%d err=%r window=%r digest_ok=%s"
              % (code, err.strip(), head1.get("window"), digest_ok))

        # 2. NFKC: fullwidth body vs ASCII quote
        out2 = os.path.join(ev, "F2.txt")
        code, _, _ = _run(["--url", "file://" + html_path, "--quote", "ABC123",
                           "--out", out2, "--allow-file"])
        head2 = _header_map(_read(out2))
        check("nfkc-fold",
              code == 0 and head2.get("quote-found") == "yes"
              and head2.get("quote-found-verbatim") == "no",
              "exit=%d found=%r verbatim=%r"
              % (code, head2.get("quote-found"), head2.get("quote-found-verbatim")))

        # 3. whitespace collapsed: a line break and a doubled space inside a
        #    Latin sentence still match the single-spaced quote
        out3 = os.path.join(ev, "F3.txt")
        code, _, _ = _run(["--url", "file://" + html_path, "--quote", LATIN_QUOTE,
                           "--out", out3, "--allow-file"])
        head3 = _header_map(_read(out3))
        check("whitespace-collapse",
              code == 0 and head3.get("quote-found") == "yes"
              and head3.get("quote-found-verbatim") == "no"
              and "matched=folded" in head3.get("normalise", ""),
              "exit=%d found=%r normalise=%r"
              % (code, head3.get("quote-found"), head3.get("normalise")))

        # 3b. a CJK run broken by a source line break matches only the no-space
        #     tier, which the counter's fold cannot confirm: the file is written
        #     (the quote IS on the page) but the capture fails verification.
        out3b = os.path.join(ev, "F3b.txt")
        code, _, err3b = _run(["--url", "file://" + html_path, "--quote", SPACED_QUOTE,
                               "--out", out3b, "--allow-file"])
        head3b = _header_map(_read(out3b)) if os.path.exists(out3b) else {}
        check("cjk-linebreak-refused",
              code == 5 and head3b.get("quote-found") == "yes"
              and "matched=folded-no-space" in head3b.get("normalise", "")
              and "after NFKC+whitespace fold" in err3b,
              "exit=%d found=%r normalise=%r err=%r"
              % (code, head3b.get("quote-found"), head3b.get("normalise"),
                 err3b.strip()[:100]))

        # 4. absent quote: file written, window empty, exit 3
        out4 = os.path.join(ev, "F4.txt")
        code, _, err4 = _run(["--url", "file://" + html_path,
                              "--quote", "この文はページに存在しません", "--out", out4])
        text4 = _read(out4) if os.path.exists(out4) else ""
        head4 = _header_map(text4)
        check("quote-missing",
              code == 3 and head4.get("quote-found") == "no"
              and (_block(text4, "window") or "").strip() == ""
              and "存在しません" in (_block(text4, "quote") or "")
              and "not citable" in err4,
              "exit=%d found=%r window=%r"
              % (code, head4.get("quote-found"), (_block(text4, "window") or "")[:40]))

        # 5. extractor drops script/style/comments, decodes entities
        check("extract-visible",
              all(m not in text1 for m in ("SCRIPT_ONLY_TEXT", "STYLE_ONLY_TEXT",
                                           "COMMENT_ONLY_TEXT"))
              and "アンパサンド & と山括弧 <tag>" in text1
              and "fixture title" not in text1,
              "script/comment leak or entity not decoded")

        # 6. quote at the very start of the text: before small, window still >= 4096
        out6 = os.path.join(ev, "F6.txt")
        code, _, _ = _run(["--url", "file://" + edge_path, "--quote", EDGE_QUOTE,
                           "--out", out6, "--allow-file"])
        head6 = _header_map(_read(out6))
        geo6 = re.match(r"chars=(\d+) min=(\d+) pad=(\d+) before=(\d+) after=(\d+)",
                        head6.get("window", ""))
        check("window-edge",
              code == 0 and head6.get("quote-found") == "yes" and geo6 is not None
              and int(geo6.group(4)) == 0
              and int(geo6.group(1)) >= 4096 and int(geo6.group(5)) >= 400,
              "exit=%d window=%r" % (code, head6.get("window")))

        # 6b. a document shorter than the window minimum is stored whole and
        #     declared: window-scope whole-document, visible-chars == the stored
        #     length; that is the amended leg, so the capture verifies.
        out6b = os.path.join(ev, "F6b.txt")
        code, _, err6b = _run(["--url", "file://" + short_path,
                               "--quote", SHORT_QUOTE, "--out", out6b, "--allow-file"])
        text6b = _read(out6b) if os.path.exists(out6b) else ""
        head6b = _header_map(text6b)
        win6b = _block(text6b, "window") or ""
        check("window-whole-document",
              code == 0 and head6b.get("window-scope") == "whole-document"
              and head6b.get("visible-chars") == str(len(win6b))
              and len(win6b) < MIN_WINDOW
              and nfkc_ws(SHORT_QUOTE) in nfkc_ws(win6b)
              and head6b.get("window-sha256")
              == hashlib.sha256(win6b.encode("utf-8")).hexdigest(),
              "exit=%d err=%r scope=%r visible=%r win=%d"
              % (code, err6b.strip()[:80], head6b.get("window-scope"),
                 head6b.get("visible-chars"), len(win6b)))

        # 6c. whole-document is not a shortcut: a truncated whole-document window
        #     and a whole-document claim for a long text both fail verification
        trunc = os.path.join(ev, "F6c-trunc.txt")
        truncated = text6b.replace(win6b, win6b[:-6], 1)
        with open(trunc, "w", encoding="utf-8") as fh:
            fh.write(truncated)
        code_tr, _, err_tr = _run(["--verify", trunc, "--allow-file"])
        forged = os.path.join(ev, "F6c-forged.txt")
        lines_f = []
        for line in _read(out1).splitlines():
            if line.startswith("window-scope:"):
                line = "window-scope: whole-document"
            lines_f.append(line)
        with open(forged, "w", encoding="utf-8") as fh:
            fh.write("\n".join(lines_f) + "\n")
        code_fg, _, err_fg = _run(["--verify", forged, "--allow-file"])
        check("whole-document-guard",
              code_tr == 5 and "but visible-chars says" in err_tr
              and code_fg == 5 and "whole-document claimed" in err_fg,
              "trunc=%d forged=%d err=%r"
              % (code_tr, code_fg, (err_tr + err_fg).strip()[:140]))

        # 7. http.server: UA sent, status, bytes, sha256, GET line
        _FixtureHandler.payload = _fixture_html().encode("utf-8")
        _FixtureHandler.seen = []
        server = ThreadingHTTPServer(("127.0.0.1", 0), _FixtureHandler)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        base = "http://127.0.0.1:%d" % server.server_address[1]
        try:
            out7 = os.path.join(ev, "F7.txt")
            code, _, _ = _run(["--url", base + "/fixture.html", "--quote", CJK_QUOTE,
                               "--out", out7])
            text7 = _read(out7)
            head7 = _header_map(text7)
            sent = {ua for path, ua in _FixtureHandler.seen if path == "/fixture.html"}
            body_len = len(_FixtureHandler.payload)
            check("http-fetch",
                  code == 0 and head7.get("http") == "200"
                  and head7.get("http-status") == "200"
                  and head7.get("user-agent") == UA_BROWSER
                  and head7.get("ua") == UA_BROWSER
                  and sent == {UA_BROWSER}
                  and head7.get("bytes") == str(body_len)
                  and head7.get("sha256") == hashlib.sha256(_FixtureHandler.payload).hexdigest()
                  and head7.get("fetch") == "GET " + base + "/fixture.html"
                  and head7.get("content-length") == str(body_len)
                  and head7.get("transferred-bytes") == str(body_len)
                  and head7.get("fetch-attempts") == "1"
                  and "curl -sS -L" in head7.get("fetch-command", ""),
                  "exit=%d head=%r seen=%r"
                  % (code, {k: head7.get(k) for k in ("http", "bytes", "user-agent")}, sent))

            # 7b. a short body (curl exit 18) is retried, and the retry is recorded
            out7b = os.path.join(ev, "F7b.txt")
            _FixtureHandler.flaky["left"] = 1
            code, _, _ = _run(["--url", base + "/flaky.html", "--quote", CJK_QUOTE,
                               "--out", out7b])
            head7b = _header_map(_read(out7b)) if os.path.exists(out7b) else {}
            check("fetch-retry",
                  code == 0 and head7b.get("http") == "200"
                  and head7b.get("fetch-attempts") == "2"
                  and head7b.get("bytes") == str(body_len),
                  "exit=%d attempts=%r http=%r"
                  % (code, head7b.get("fetch-attempts"), head7b.get("http")))

            # 7c. retries exhausted: no file, exit 2, the failure is named
            out7c = os.path.join(ev, "F7c.txt")
            _FixtureHandler.flaky["left"] = 6
            code, _, err7c = _run(["--url", base + "/flaky.html", "--quote", CJK_QUOTE,
                                   "--out", out7c, "--retries", "1"])
            check("fetch-retry-gives-up",
                  code == 2 and not os.path.exists(out7c)
                  and "curl exit 18 after 2 attempt(s)" in err7c,
                  "exit=%d err=%r" % (code, err7c.strip()))
            _FixtureHandler.flaky["left"] = 0

            # 9. non-200: file written, exit 4, not citable
            out9 = os.path.join(ev, "F9.txt")
            code, _, err9 = _run(["--url", base + "/missing.html",
                                  "--quote", "not here", "--out", out9])
            head9 = _header_map(_read(out9))
            check("http-not-200",
                  code == 4 and head9.get("http") == "404" and "not citable" in err9,
                  "exit=%d http=%r" % (code, head9.get("http")))
        finally:
            server.shutdown()
            server.server_close()

        # 10. PDF body through pdftotext, no -layout
        if shutil.which("pdftotext") is None:
            check("pdf-extract", True, "SKIPPED: pdftotext absent")
        else:
            pdf_path = os.path.join(tmp, "fixture.pdf")
            with open(pdf_path, "wb") as fh:
                fh.write(_minimal_pdf("PDF fixture quote sentence."))
            out10 = os.path.join(ev, "F10.txt")
            code, _, err = _run(["--url", "file://" + pdf_path,
                                 "--quote", "PDF fixture quote sentence.", "--out", out10,
                                 "--allow-file"])
            head10 = _header_map(_read(out10))
            check("pdf-extract",
                  code == 0 and head10.get("quote-found") == "yes"
                  and "pdftotext -enc UTF-8" in head10.get("extract", "")
                  and "-layout" not in head10.get("extract", ""),
                  "exit=%d err=%r extract=%r"
                  % (code, err.strip(), head10.get("extract")))

        # 11. a GB18030 body declared only in <meta>: charset detection, CJK quote
        gb_quote = "世界观设定必须一层一层往下推。"
        gb_path = os.path.join(tmp, "fixture-gb.html")
        with open(gb_path, "wb") as fh:
            fh.write(("<html><head><meta charset=\"gb18030\"><title>gb</title></head>"
                      "<body><p>%s</p><p>%s</p><p>%s</p></body></html>"
                      % (FILLER, gb_quote, FILLER)).encode("gb18030"))
        out11 = os.path.join(ev, "F11.txt")
        code, _, _ = _run(["--url", "file://" + gb_path, "--quote", gb_quote,
                           "--out", out11, "--allow-file"])
        head11 = _header_map(_read(out11)) if os.path.exists(out11) else {}
        check("charset-gb18030",
              code == 0 and head11.get("quote-found-verbatim") == "yes"
              and "gb18030" in head11.get("extract", "")
              and gb_quote in (_block(_read(out11), "window") or ""),
              "exit=%d found=%r extract=%r"
              % (code, head11.get("quote-found-verbatim"),
                 head11.get("extract", "")[-40:]))

        # 12. --verify: passes on a good file, fails on a tampered window or digest
        code_ok, outv, errv = _run(["--verify", out1, "--allow-file"])
        tampered = os.path.join(ev, "F1-window-edit.txt")
        text_t = _read(out1)
        win_t = _block(text_t, "window") or ""
        text_t = text_t.replace(win_t, win_t[:-4] + "XXXX", 1)
        with open(tampered, "w", encoding="utf-8") as fh:
            fh.write(text_t)
        code_t, _, err_t = _run(["--verify", tampered, "--allow-file"])
        digest_t = os.path.join(ev, "F1-digest-edit.txt")
        lines_d = _read(out1).splitlines()
        lines_d = [("window-sha256: " + "0" * 64)
                   if l.startswith("window-sha256:") else l for l in lines_d]
        with open(digest_t, "w", encoding="utf-8") as fh:
            fh.write("\n".join(lines_d) + "\n")
        code_d, _, err_d = _run(["--verify", digest_t, "--allow-file"])
        check("verify-mode",
              code_ok == 0 and "VERIFY OK" in outv
              and code_t == 5 and "window-sha256 mismatch" in err_t
              and code_d == 5 and "window-sha256 mismatch" in err_d,
              "ok=%d tamper=%d digest=%d err=%r"
              % (code_ok, code_t, code_d, (err_t or err_d).strip()[:80]))

        # 13. usage guards: window minimum below the grammar floor, pad below its
        #     floor, an empty quote, and a quote that is only whitespace
        out12 = os.path.join(ev, "F12.txt")
        code_win, _, _ = _run(["--url", "file://" + html_path, "--quote", CJK_QUOTE,
                               "--out", out12, "--min-window", "100"])
        code_low, _, _ = _run(["--url", "file://" + html_path, "--quote", CJK_QUOTE,
                               "--out", os.path.join(ev, "F13.txt"), "--pad", "40"])
        code_empty, _, _ = _run(["--url", "file://" + html_path, "--quote", "   ",
                                 "--out", os.path.join(ev, "F14.txt")])
        check("guards",
              code_win != 0 and code_low != 0 and code_empty == 2
              and not os.path.exists(out12)
              and not os.path.exists(os.path.join(ev, "F13.txt"))
              and not os.path.exists(os.path.join(ev, "F14.txt")),
              "window-exit=%d pad-exit=%d empty-exit=%d"
              % (code_win, code_low, code_empty))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    passed = sum(1 for _, ok, _ in results if ok)
    for name, ok, detail in results:
        if not ok:
            print("SELFTEST FAIL: %s: %s" % (name, detail), file=sys.stderr)
    if passed == len(results):
        print("SELFTEST OK: %d scenarios" % len(results))
        return 0
    print("SELFTEST FAIL: %d/%d" % (passed, len(results)))
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
