#!/usr/bin/env python3
"""Re-open a curated-source row: refetch its pages and say whether the row's
anchor quote is still there, and where.

WHAT THIS TOOL DOES
  Given one or more row ids (S123, S456, ...) it looks the row up in a
  registry file (a markdown table whose rows look like "| S123 | ... |"), pulls
  the row's URLs out of its source cell, pulls the row's quote out of its
  anchor cell, fetches those pages and reports where the quote was found.

  Verdict per row:
    LOCATED       the quote is in the BODY text of a page that answered 2xx
    CAPTION_ONLY  the quote is only in caption material (figcaption, an
                  element whose class or id contains caption, thumbnail or
                  gallery, or an alt / title / aria-label / content / data-*
                  attribute value) of a page that answered 2xx
    ABSENT        some page answered 2xx but the quote is nowhere in it
    UNREACHABLE   no page answered 2xx (HTTP error, timeout, dead host)
    REFUSED       every URL of the row was refused by the private-address
                  policy before any request was made
    NO_QUOTE      the row has no usable quote (no quoted span, a quote shorter
                  than 8 normalised words, or no URL at all) - no request made
    NO_ROW        the registry has no row with that id - no request made

  Within one pass the row's URLs are tried in order and the pass stops at the
  first BODY match.  A pass verdict is LOCATED > CAPTION_ONLY > ABSENT >
  REFUSED > UNREACHABLE; the row verdict is the best pass verdict, ranked
  LOCATED > CAPTION_ONLY > ABSENT > UNREACHABLE > REFUSED.

HOW A ROW IS READ
  A registry row is a line that starts with "| S" and has at least 7 cells
  when split on "|".  Cell 1 is the id, cell 2 is the source cell (title,
  publisher, date, live URL and optionally " ; capture <archive url>"), cell 6
  is the anchor cell (where the quote lives).  The quote is the first
  double-quoted span of the anchor cell, straight or curly.  The URLs are the
  http(s) URLs of the source cell, in order; trailing ".,;:'" and an
  unbalanced ")" are trimmed off each.

HOW TEXT IS COMPARED
  NFKC, then casefold, then every run of characters that is not a letter or a
  digit becomes a single space.  The quote's normalised words must appear as
  one contiguous run of whole words in the page's normalised words.

HOW HTML IS SPLIT
  A caption element is figcaption, or any element whose class or id contains
  "caption", "thumbnail" or "gallery" (case-insensitive).  BODY text is every
  text node outside script, style, noscript and template, and outside every
  caption element; the descendants of a caption element are excluded from the
  body as well.  CAPTION text is the text of figcaption and of the caption
  elements and their descendants, plus the values of the alt, title,
  aria-label, content and data-* attributes.  Script and style text is
  neither.  A body that is not HTML (text/plain, JSON, ...) is BODY text as a
  whole.

HOW PAGES ARE FETCHED
  GET with a 30 s timeout.  A transient result (HTTP 429, any 5xx, a timeout,
  a connection error) is retried, at most 3 attempts per URL per pass, waiting
  min(gap, 5) s between attempts.  Any other HTTP error ends that URL for the
  pass after one attempt.  Without --allow-private a URL whose host is, or
  resolves to, a loopback, private, link-local, reserved or unspecified
  address - or that does not resolve at all - is refused without a request.
  Another pass runs, after gap seconds, only when the pass was not LOCATED and
  some URL of that pass ended on a transient result; at most --passes passes
  run (3 by default, gap 60 s by default).

OUTPUT
  One line per id, in argument order:
      ROW <ID> <VERDICT> attempts=<n> url=<url or ->
  where <n> is the number of HTTP requests and connection attempts made for
  that row over all passes and <url> is the URL that produced the verdict's
  match ("-" when the verdict has no match).  Then one summary line:
      REOPEN: <located>/<rows> located
  Exit status: 0 when every row is LOCATED, 1 otherwise, and 2 on an input
  error, in which case a line starting with REOPEN_ERROR is printed and no
  traceback is shown.

USAGE
  reopen-row.py [--registry PATH] [--passes N] [--gap SECONDS]
                [--allow-private] [--selftest] ID...

  --registry PATH   registry to read; default corpus/SOURCES.md, taken
                    relative to the working directory
  --passes N        maximum number of passes per row; integer >= 1, default 3
  --gap SECONDS     seconds between passes; the wait between retries of one
                    URL is min(gap, 5) s; number >= 0, default 60
  --allow-private   allow URLs that point at private or loopback addresses
  --selftest        run the built-in offline fixtures and exit
"""
import ipaddress
import os
import re
import socket
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from html.parser import HTMLParser

DEFAULT_REGISTRY = os.path.join("corpus", "SOURCES.md")
DEFAULT_PASSES = 3
DEFAULT_GAP = 60.0
FETCH_TIMEOUT = 30.0
MAX_BODY_BYTES = 4 * 1024 * 1024
MAX_ATTEMPTS_PER_URL = 3
MIN_QUOTE_WORDS = 8
USER_AGENT = "kotodama-reopen-row/1.0 (row re-check; stdlib urllib)"

URL_RE = re.compile(r"https?://[^\s]+", re.IGNORECASE)
NONWORD_RE = re.compile(r"[\W_]+", re.UNICODE)
TRAILING_JUNK = ".,;:'"
CAPTION_ATTRS = ("alt", "title", "aria-label", "content")
CAPTION_KEYWORDS = ("caption", "thumbnail", "gallery")
VOID_TAGS = frozenset((
    "area", "base", "br", "col", "embed", "hr", "img", "input", "link",
    "meta", "param", "source", "track", "wbr",
))
SKIP_TAGS = frozenset(("script", "style", "noscript", "template"))

VERDICT_RANK = {
    "LOCATED": 5,
    "CAPTION_ONLY": 4,
    "ABSENT": 3,
    "UNREACHABLE": 2,
    "REFUSED": 1,
}


class InputError(Exception):
    """A bad invocation or an unreadable registry."""


class TransientFetch(Exception):
    """429, 5xx, timeout or connection error: worth retrying."""


class FatalFetch(Exception):
    """Any other HTTP error: the URL is done for this pass."""


# ---------------------------------------------------------------- text bits


def normalise_words(text):
    """NFKC, casefold, fold every non-word run to a single space, then split."""
    folded = unicodedata.normalize("NFKC", text).casefold()
    return NONWORD_RE.sub(" ", folded).split()


def quote_in_words(haystack, needle):
    """True when needle occurs as one contiguous run of whole words."""
    if not needle or len(needle) > len(haystack):
        return False
    first = needle[0]
    span = len(needle)
    for index, word in enumerate(haystack):
        if word == first and haystack[index:index + span] == needle:
            return True
    return False


def trim_url(raw):
    """Drop trailing punctuation and an unbalanced closing parenthesis."""
    url = raw.strip()
    changed = True
    while changed and url:
        changed = False
        while url and url[-1] in TRAILING_JUNK:
            url = url[:-1]
            changed = True
        if url.endswith(")") and url.count("(") < url.count(")"):
            url = url[:-1]
            changed = True
    return url


def cell_urls(source_cell):
    """The http(s) URLs of a source cell, in order."""
    urls = []
    for match in URL_RE.findall(source_cell):
        url = trim_url(match)
        if url:
            urls.append(url)
    return urls


QUOTE_PAIRS = {
    '"': '"',
    "\u201c": "\u201d",
    "\u201e": "\u201c",
    "\u201f": "\u201d",
}


def cell_quote(anchor_cell):
    """The first double-quoted span of an anchor cell, or None."""
    for index, char in enumerate(anchor_cell):
        closer = QUOTE_PAIRS.get(char)
        if not closer:
            continue
        end = anchor_cell.find(closer, index + 1)
        if end != -1:
            return anchor_cell[index + 1:end]
    return None


# ---------------------------------------------------------------- html split


def _captionish(attr):
    """True when the element's class or id marks it as caption material.

    A caption element is figcaption, or any element whose class or id
    contains "caption", "thumbnail" or "gallery" (case-insensitive).  Such an
    element and its descendants are caption text, never body text.
    """
    for name in ("class", "id"):
        value = (attr.get(name) or "").lower()
        for keyword in CAPTION_KEYWORDS:
            if keyword in value:
                return True
    return False


class _Splitter(HTMLParser):
    """Collects body text and caption text out of one HTML document."""

    def __init__(self):
        HTMLParser.__init__(self, convert_charrefs=True)
        self.body = []
        self.caption = []
        self.stack = []
        self.caption_depth = 0
        self.skip_depth = 0

    def _open(self, tag, attrs, push):
        attr = {}
        for name, value in attrs:
            attr.setdefault(name.lower(), value or "")
        if tag in SKIP_TAGS:
            kind = "skip"
        elif tag == "figcaption":
            kind = "caption"
        elif _captionish(attr):
            kind = "caption"
        else:
            kind = "normal"
        if self.skip_depth:
            kind = "skip"
        elif self.caption_depth and kind == "normal":
            kind = "caption"
        for name, value in attrs:
            lowered = name.lower()
            if value and (lowered in CAPTION_ATTRS or lowered.startswith("data-")):
                self.caption.append(value)
        if push and tag not in VOID_TAGS:
            self.stack.append((tag, kind))
            if kind == "skip":
                self.skip_depth += 1
            elif kind == "caption":
                self.caption_depth += 1

    def handle_starttag(self, tag, attrs):
        self._open(tag, attrs, True)

    def handle_startendtag(self, tag, attrs):
        self._open(tag, attrs, False)

    def handle_endtag(self, tag):
        for index in range(len(self.stack) - 1, -1, -1):
            if self.stack[index][0] == tag:
                for _, kind in self.stack[index:]:
                    if kind == "skip":
                        self.skip_depth -= 1
                    elif kind == "caption":
                        self.caption_depth -= 1
                del self.stack[index:]
                return

    def handle_data(self, data):
        if self.skip_depth:
            return
        if self.caption_depth:
            self.caption.append(data)
        else:
            self.body.append(data)


def split_html(markup):
    """Return (body text, caption text) for an HTML document."""
    parser = _Splitter()
    try:
        parser.feed(markup)
        parser.close()
    except Exception:
        pass
    return " ".join(parser.body), " ".join(parser.caption)


def decode_body(raw, charset):
    if charset:
        try:
            return raw.decode(charset, "replace")
        except (LookupError, TypeError):
            pass
    return raw.decode("utf-8", "replace")


def split_content(raw, content_type, charset):
    """Return (body text, caption text) for a fetched response."""
    ctype = (content_type or "").lower()
    text = decode_body(raw, charset)
    looks_html = "html" in ctype
    if not ctype or ctype in ("application/octet-stream", "binary/octet-stream"):
        head = text.lstrip()[:512].lower()
        looks_html = (
            head.startswith("<!doctype html")
            or head.startswith("<html")
            or "<html" in head
            or "<body" in head
        )
    if looks_html:
        return split_html(text)
    return text, ""


# ---------------------------------------------------------------- fetching


class Fetcher(object):
    """Fetches pages, honouring the private-address policy."""

    def __init__(self, allow_private=False, timeout=FETCH_TIMEOUT):
        self.allow_private = allow_private
        self.timeout = timeout
        self._resolved = {}

    def refused(self, url):
        """True when the URL must not be requested (private or unresolvable)."""
        if self.allow_private:
            return False
        parts = urllib.parse.urlsplit(url)
        host = parts.hostname
        if not host:
            return True
        port = parts.port or (443 if parts.scheme == "https" else 80)
        if host in self._resolved:
            addresses = self._resolved[host]
        else:
            try:
                infos = socket.getaddrinfo(host, port, proto=socket.IPPROTO_TCP)
            except (socket.gaierror, UnicodeError, OSError):
                infos = []
            addresses = [info[4][0] for info in infos]
            self._resolved[host] = addresses
        if not addresses:
            # does not resolve: refused without a request
            return True
        for address in addresses:
            try:
                ip = ipaddress.ip_address(address.split("%")[0])
            except ValueError:
                return True
            if (ip.is_loopback or ip.is_private or ip.is_link_local
                    or ip.is_reserved or ip.is_unspecified):
                return True
        return False

    def fetch(self, url):
        """Fetch one URL once.

        Returns (status, body bytes, content type, charset).  Raises
        TransientFetch for a retryable failure, FatalFetch for any other HTTP
        error.
        """
        request = urllib.request.Request(
            url,
            headers={"User-Agent": USER_AGENT, "Accept": "*/*"},
        )
        try:
            with urllib.request.urlopen(request, timeout=self.timeout) as response:
                raw = response.read(MAX_BODY_BYTES)
                status = getattr(response, "status", None) or response.getcode()
                ctype = response.headers.get("Content-Type", "")
                charset = response.headers.get_content_charset()
                return status, raw, ctype, charset
        except urllib.error.HTTPError as error:
            code = error.code
            try:
                error.read()
            except Exception:
                pass
            error.close()
            if code == 429 or 500 <= code < 600:
                raise TransientFetch("HTTP %s" % code)
            raise FatalFetch("HTTP %s" % code)
        except urllib.error.URLError as error:
            raise TransientFetch(str(error.reason))
        except (socket.timeout, TimeoutError, ConnectionError, OSError) as error:
            raise TransientFetch(str(error))


# ---------------------------------------------------------------- registry


def load_registry(path):
    """Return {id: (source cell, anchor cell)} for a registry file."""
    try:
        with open(path, "rb") as handle:
            raw = handle.read()
    except OSError as error:
        raise InputError("cannot read registry %s: %s" % (path, error))
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as error:
        raise InputError("registry %s is not valid UTF-8: %s" % (path, error))
    rows = {}
    for line in text.splitlines():
        if not line.startswith("| S"):
            continue
        cells = line.split("|")
        if len(cells) < 7:
            continue
        row_id = cells[1].strip()
        if not row_id:
            continue
        rows[row_id] = (cells[2], cells[6])
    return rows


# ---------------------------------------------------------------- the work


def run_pass(urls, quote_words, fetcher, gap):
    """Run one pass over a row's URLs.

    Returns (verdict, url or None, transient_seen, attempts).
    """
    attempts = 0
    answered = False
    caption_hit = False
    caption_url = None
    refused_all = True
    transient_seen = False
    for url in urls:
        if fetcher.refused(url):
            continue
        refused_all = False
        for attempt in range(MAX_ATTEMPTS_PER_URL):
            try:
                status, raw, ctype, charset = fetcher.fetch(url)
            except TransientFetch:
                attempts += 1
                transient_seen = True
                if attempt + 1 < MAX_ATTEMPTS_PER_URL:
                    time.sleep(min(gap, 5.0))
                continue
            except FatalFetch:
                attempts += 1
                break
            attempts += 1
            if 200 <= status < 300:
                answered = True
                body_text, caption_text = split_content(raw, ctype, charset)
                if quote_in_words(normalise_words(body_text), quote_words):
                    return "LOCATED", url, transient_seen, attempts
                if (caption_text and not caption_hit
                        and quote_in_words(normalise_words(caption_text), quote_words)):
                    caption_hit = True
                    caption_url = url
            break
    if caption_hit:
        return "CAPTION_ONLY", caption_url, transient_seen, attempts
    if answered:
        return "ABSENT", None, transient_seen, attempts
    if refused_all:
        return "REFUSED", None, transient_seen, attempts
    return "UNREACHABLE", None, transient_seen, attempts


def process_row(row, passes, gap, fetcher):
    """Return (verdict, attempts, url) for one registry row."""
    source_cell, anchor_cell = row
    urls = cell_urls(source_cell)
    quote = cell_quote(anchor_cell)
    quote_words = normalise_words(quote) if quote else []
    if not urls or len(quote_words) < MIN_QUOTE_WORDS:
        return "NO_QUOTE", 0, None
    best_verdict = None
    best_url = None
    total_attempts = 0
    for index in range(passes):
        verdict, url, transient_seen, attempts = run_pass(
            urls, quote_words, fetcher, gap)
        total_attempts += attempts
        if best_verdict is None or VERDICT_RANK[verdict] > VERDICT_RANK[best_verdict]:
            best_verdict = verdict
            best_url = url
        if verdict == "LOCATED" or not transient_seen:
            break
        if index + 1 < passes:
            time.sleep(gap)
    return best_verdict, total_attempts, best_url


# ---------------------------------------------------------------- command line


USAGE = (
    "usage: reopen-row.py [--registry PATH] [--passes N] [--gap SECONDS]\n"
    "                      [--allow-private] [--selftest] ID...\n"
)


def parse_args(argv):
    registry = DEFAULT_REGISTRY
    passes = DEFAULT_PASSES
    gap = DEFAULT_GAP
    allow_private = False
    selftest = False
    ids = []
    index = 0
    while index < len(argv):
        arg = argv[index]
        if arg in ("-h", "--help"):
            sys.stdout.write(USAGE)
            raise SystemExit(0)
        if arg == "--selftest":
            selftest = True
        elif arg == "--allow-private":
            allow_private = True
        elif arg in ("--registry", "--passes", "--gap"):
            if index + 1 >= len(argv):
                raise InputError("%s needs a value" % arg)
            value = argv[index + 1]
            index += 2
            if arg == "--registry":
                registry = value
            elif arg == "--passes":
                passes = value
            else:
                gap = value
            continue
        elif arg.startswith("--registry="):
            registry = arg.split("=", 1)[1]
        elif arg.startswith("--passes="):
            passes = arg.split("=", 1)[1]
        elif arg.startswith("--gap="):
            gap = arg.split("=", 1)[1]
        elif arg.startswith("-") and arg != "-":
            raise InputError("unknown option %s" % arg)
        else:
            ids.append(arg)
        index += 1
    try:
        passes = int(passes)
    except (TypeError, ValueError):
        raise InputError("--passes must be an integer >= 1")
    if passes < 1:
        raise InputError("--passes must be an integer >= 1")
    try:
        gap = float(gap)
    except (TypeError, ValueError):
        raise InputError("--gap must be a number >= 0")
    if gap < 0:
        raise InputError("--gap must be a number >= 0")
    return registry, passes, gap, allow_private, selftest, ids


def main(argv):
    try:
        registry, passes, gap, allow_private, selftest, ids = parse_args(argv)
    except InputError as error:
        sys.stderr.write("REOPEN_ERROR: %s\n" % error)
        return 2
    if selftest:
        return run_selftest()
    if not ids:
        sys.stderr.write("REOPEN_ERROR: no row ids given\n")
        return 2
    try:
        rows = load_registry(registry)
    except InputError as error:
        sys.stderr.write("REOPEN_ERROR: %s\n" % error)
        return 2
    fetcher = Fetcher(allow_private=allow_private)
    located = 0
    all_located = True
    for row_id in ids:
        row = rows.get(row_id)
        if row is None:
            verdict, attempts, url = "NO_ROW", 0, None
        else:
            verdict, attempts, url = process_row(row, passes, gap, fetcher)
        if verdict == "LOCATED":
            located += 1
        else:
            all_located = False
        sys.stdout.write(
            "ROW %s %s attempts=%d url=%s\n" % (row_id, verdict, attempts, url or "-")
        )
    sys.stdout.write("REOPEN: %d/%d located\n" % (located, len(ids)))
    sys.stdout.flush()
    return 0 if all_located else 1


# ---------------------------------------------------------------- selftest


def _start_fixture_server(routes):
    """Start a local HTTP server; returns (server, hits)."""
    import http.server
    import threading

    hits = {}
    lock = threading.Lock()

    class Handler(http.server.BaseHTTPRequestHandler):
        protocol_version = "HTTP/1.1"

        def do_GET(self):
            with lock:
                count = hits.get(self.path, 0)
                hits[self.path] = count + 1
                route = routes.get(self.path)
            if route is None:
                body = b"<html><body><p>missing</p></body></html>"
                self.send_response(404)
                self.send_header("Content-Type", "text/html")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)
                return
            statuses, payload, ctype = route
            status = statuses[min(count, len(statuses) - 1)]
            if status == 200:
                body = payload
            else:
                body = b"<html><body><p>error page</p></body></html>"
            self.send_response(status)
            self.send_header("Content-Type", ctype)
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def log_message(self, *args):
            pass

    server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    return server, hits


def run_selftest():
    """Offline fixtures: body, caption kinds, transient, dead+archive, 404,
    closed port and bad inputs."""
    import contextlib
    import io
    import tempfile

    failures = []
    checks = 0

    def check(label, got, want):
        nonlocal checks
        checks += 1
        if got != want:
            failures.append("%s: got %r want %r" % (label, got, want))
            print("FAIL %s: got %r want %r" % (label, got, want))
        else:
            print("ok   %s: %r" % (label, got))

    words = ["Alpha", "bravo", "charlie", "delta", "echo", "foxtrot", "golf",
             "hotel", "india", "juliet"]
    quote = " ".join(words)
    filler = " ".join(["lima"] * 30)
    page = ("<!doctype html><html><head><title>t</title></head><body>"
            "%s</body></html>")

    def html(inner):
        return (page % inner).encode("utf-8")

    routes = {
        "/body": ([200], html("<p>%s</p><p>%s.</p>" % (filler, quote)), "text/html"),
        "/plain": ([200], ("%s\n%s.\n" % (filler, quote)).encode("utf-8"),
                   "text/plain; charset=utf-8"),
        "/split": ([200], html("<p>%s</p><div><span>%s</span></div>"
                               % (filler, quote.upper())), "text/html"),
        "/capfig": ([200], html("<p>%s</p><figure><figcaption>%s.</figcaption></figure>"
                                % (filler, quote)), "text/html"),
        "/capattr": ([200], html("<p>%s</p><img src='x.png' alt=\"%s.\">"
                                % (filler, quote)), "text/html"),
        "/capclass": ([200], html("<p>%s</p><div class=\"wp-caption-text\">"
                                 "<span>%s.</span></div>" % (filler, quote)),
                      "text/html"),
        "/capthumb": ([200], html("<p>%s</p><div class=\"thumbnail-description\">"
                                  "<span>%s.</span></div>" % (filler, quote)),
                      "text/html"),
        "/capgallery": ([200], html("<p>%s</p><div class=\"Gallery-item\">"
                                    "<span>%s.</span></div>" % (filler, quote)),
                        "text/html"),
        "/capid": ([200], html("<p>%s</p><div id=\"figCaption1\">"
                               "<span>%s.</span></div>" % (filler, quote)),
                   "text/html"),
        "/capidcase": ([200], html("<p>%s</p><div id=\"thumbnail-note4\">"
                                   "<span>%s.</span></div>" % (filler, quote)),
                       "text/html"),
        "/script": ([200], html("<p>%s</p><script>var t = \"%s.\";</script>"
                                % (filler, quote)), "text/html"),
        "/absent": ([200], html("<p>%s</p><p>short tail</p>" % filler), "text/html"),
        "/transient": ([503, 503, 200], html("<p>%s.</p>" % quote), "text/html"),
        "/dead": ([403], html("<p>gone</p>"), "text/html"),
        "/archived": ([200], html("<p>%s.</p>" % quote), "text/html"),
        "/gone": ([404], html("<p>gone</p>"), "text/html"),
    }
    server, hits = _start_fixture_server(routes)
    port = server.server_address[1]
    base = "http://127.0.0.1:%d" % port
    probe = socket.socket()
    probe.bind(("127.0.0.1", 0))
    closed_port = probe.getsockname()[1]
    probe.close()

    work = tempfile.mkdtemp(prefix="reopen-row-selftest-")
    registry_path = os.path.join(work, "REGISTRY.md")

    def row(row_id, urls, anchor):
        return ("| %s | Title, Press, 2025 - %s. | docs | B | scope x | %s | "
                "teaches y | mined | 2026-10-23 | 180d | corpus/knowledge/x.md |"
                % (row_id, urls, anchor))

    quoted = 'section a: "%s"' % quote
    rows = [
        row("S1", "%s/body" % base, quoted),
        row("S2", "%s/plain" % base, quoted),
        row("S3", "%s/split" % base, quoted),
        row("S4", "%s/capfig" % base, quoted),
        row("S5", "%s/capattr" % base, quoted),
        row("S6", "%s/capclass" % base, quoted),
        row("S15", "%s/capthumb" % base, quoted),
        row("S16", "%s/capgallery" % base, quoted),
        row("S17", "%s/capid" % base, quoted),
        row("S18", "%s/capidcase" % base, quoted),
        row("S7", "%s/script" % base, quoted),
        row("S8", "%s/absent" % base, quoted),
        row("S9", "%s/transient" % base, quoted),
        row("S10", "%s/dead ; capture %s/archived" % (base, base), quoted),
        row("S11", "%s/gone" % base, quoted),
        row("S12", "http://127.0.0.1:%d/deadport" % closed_port, quoted),
        row("S13", "%s/body" % base, "section a: no quoted span here"),
        row("S14", "%s/body" % base, 'section a: "only three short words"'),
    ]
    with open(registry_path, "w", encoding="utf-8") as handle:
        handle.write("| id | source | kind | tier | scope | anchor | teaches |\n")
        handle.write("\n".join(rows) + "\n")

    def run(ids, extra=()):
        argv = ["--registry", registry_path, "--passes", "3", "--gap", "0",
                "--allow-private"] + list(extra) + list(ids)
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            code = main(argv)
        return code, buffer.getvalue()

    def verdicts_of(text):
        found = {}
        for line in text.splitlines():
            if line.startswith("ROW "):
                parts = line.split()
                found[parts[1]] = (parts[2], parts[3])
        return found

    print("-- selftest: verdicts --")
    code, out = run(["S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10",
                     "S11", "S12", "S13", "S14", "S15", "S16", "S17", "S18"])
    verdicts = verdicts_of(out)
    expected = {
        "S1": ("LOCATED", "attempts=1"),
        "S2": ("LOCATED", "attempts=1"),
        "S3": ("LOCATED", "attempts=1"),
        "S4": ("CAPTION_ONLY", "attempts=1"),
        "S5": ("CAPTION_ONLY", "attempts=1"),
        "S6": ("CAPTION_ONLY", "attempts=1"),
        "S7": ("ABSENT", "attempts=1"),
        "S8": ("ABSENT", "attempts=1"),
        "S9": ("LOCATED", "attempts=3"),
        "S10": ("LOCATED", "attempts=2"),
        "S11": ("UNREACHABLE", "attempts=1"),
        "S12": ("UNREACHABLE", "attempts=9"),
        "S13": ("NO_QUOTE", "attempts=0"),
        "S14": ("NO_QUOTE", "attempts=0"),
        "S15": ("CAPTION_ONLY", "attempts=1"),
        "S16": ("CAPTION_ONLY", "attempts=1"),
        "S17": ("CAPTION_ONLY", "attempts=1"),
        "S18": ("CAPTION_ONLY", "attempts=1"),
    }
    for row_id in sorted(expected):
        check("verdict %s" % row_id, verdicts.get(row_id), expected[row_id])
    check("summary", "REOPEN: 5/18 located" in out.splitlines(), True)
    check("exit code", code, 1)

    code, out = run(["S999"])
    check("no row", verdicts_of(out).get("S999"), ("NO_ROW", "attempts=0"))

    print("-- selftest: retry bound --")
    hits.clear()
    code, out = run(["S9"])
    check("transient hits", hits.get("/transient", 0), 3)
    check("transient verdict", verdicts_of(out).get("S9"),
          ("LOCATED", "attempts=3"))

    print("-- selftest: private refusal --")
    hits.clear()
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        code = main(["--registry", registry_path, "--passes", "3", "--gap", "0",
                     "S1"])
    text = buffer.getvalue()
    check("refused verdict", "ROW S1 REFUSED attempts=0" in text, True)
    check("refused hits", hits.get("/body", 0), 0)
    check("refused exit", code, 1)

    print("-- selftest: bad inputs --")
    for label, argv in (
        ("no ids", ["--registry", registry_path]),
        ("missing registry", ["--registry", os.path.join(work, "nope.md"), "S1"]),
        ("passes zero", ["--registry", registry_path, "--passes", "0", "S1"]),
        ("gap not a number", ["--registry", registry_path, "--gap", "x", "S1"]),
        ("unknown option", ["--registry", registry_path, "--nope", "S1"]),
    ):
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            code = main(argv)
        check("%s exit" % label, code, 2)

    bad = os.path.join(work, "BAD.md")
    with open(bad, "wb") as handle:
        handle.write(b"| S1 | \xff\xfe bad |\n")
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        code = main(["--registry", bad, "S1"])
    check("bad utf-8 exit", code, 2)

    server.shutdown()
    server.server_close()
    print("-- selftest: %d checks, %d failures --" % (checks, len(failures)))
    for failure in failures:
        print("FAILED %s" % failure)
    return 0 if not failures else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
