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
    TRUNCATED     a page answered 2xx but its body was cut at the 4 MiB cap
                  before the quote could be found in the bytes read
    UNREACHABLE   no page answered 2xx (HTTP error, timeout, dead host)
    REFUSED       every URL of the row was refused by the private-address
                  policy before any request was made, or was refused at a
                  redirect hop
    MALFORMED     every URL of the row is unparseable (a port that does not
                  parse, an unbalanced bracketed IPv6 literal, an empty host,
                  a scheme that is not http(s)) - no request made
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
  GET with a wall budget of --timeout seconds for every single request
  (30 by default).  The budget covers connecting, the answer's head and the
  body together: a body that stalls or drips cannot outlive it, and an
  expired budget counts as a transient result.  A transient result (HTTP
  429, any 5xx, an expired budget, a connection error) is retried, at most
  3 attempts per URL per pass, waiting min(gap, 5) s between attempts.  Any
  other HTTP error ends that URL for the pass after one attempt.  Without
  --allow-private a URL whose host is, or resolves to, a loopback, private,
  link-local, reserved or unspecified address - or that does not resolve at
  all - is refused without a request.  Another pass runs, after gap
  seconds, only when the pass was not LOCATED and some URL of that pass
  ended on a transient result; at most --passes passes run (3 by default,
  gap 60 s by default).

  Redirects are never followed by the fetching library: every hop is
  resolved by hand against the URL that answered, and every request of the
  chain counts as one attempt.  A chain makes at most 5 requests; a
  redirect that arrives on the 5th answer ends that URL for the pass.  A
  hop to an authority (lowercased host, effective port) other than the one
  that answered must pass the private-host refusal even under
  --allow-private, so that a public page cannot send the fetcher to a
  loopback or private address; without --allow-private every hop must pass
  it.  A refused hop ends that URL for the pass, and the requests already
  made are counted as attempts.

HOW BODIES ARE READ
  At most 4 MiB of a body is read, one byte more than the cap.  A body
  that fills the cap without an end is cut: when the quote is absent from
  the bytes actually read the verdict is TRUNCATED (ranked like ABSENT),
  and when the quote is inside them the verdict is LOCATED or
  CAPTION_ONLY as usual.  A body that carries Content-Encoding: gzip is
  decompressed (at most 64 MiB of expansion) before it is decoded and
  matched.

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
                [--timeout SECONDS] [--allow-private] [--selftest] ID...

  --registry PATH   registry to read; default corpus/SOURCES.md, taken
                    relative to the working directory
  --passes N        maximum number of passes per row; integer >= 1, default 3
  --gap SECONDS     seconds between passes; the wait between retries of one
                    URL is min(gap, 5) s; number >= 0, default 60
  --timeout SECONDS wall budget of one request (connect, head and body
                    together); number > 0, default 30
  --allow-private   allow URLs that point at private or loopback addresses
  --selftest        run the built-in offline fixtures and exit
"""
import http.client
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
import zlib
from html.parser import HTMLParser

DEFAULT_REGISTRY = os.path.join("corpus", "SOURCES.md")
DEFAULT_PASSES = 3
DEFAULT_GAP = 60.0
FETCH_TIMEOUT = 30.0
MAX_BODY_BYTES = 4 * 1024 * 1024
MAX_ATTEMPTS_PER_URL = 3
MAX_REQUESTS_PER_CHAIN = 5
GZIP_LIMIT = 64 * 1024 * 1024
READ_CHUNK = 64 * 1024
REDIRECT_CODES = (301, 302, 303, 307)
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
    "TRUNCATED": 3,
    "UNREACHABLE": 2,
    "REFUSED": 1,
    "MALFORMED": 0,
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


# ---------------------------------------------------------------- urls


class BadUrl(Exception):
    """A URL that cannot be parsed: malformed, not refused."""


def parse_target(url):
    """Return (parts, host, port) of an http(s) URL, or raise BadUrl.

    A URL whose port does not parse, whose bracketed IPv6 literal is
    unbalanced, whose host is empty, or whose scheme is not http(s) is
    malformed: the row must say so instead of raising.
    """
    try:
        parts = urllib.parse.urlsplit(url)
        host = parts.hostname
        port = parts.port
    except ValueError as error:
        raise BadUrl(str(error))
    scheme = (parts.scheme or "").lower()
    if scheme not in ("http", "https"):
        raise BadUrl("scheme %r is not http(s)" % (parts.scheme or "",))
    if not host:
        raise BadUrl("empty host")
    if port is None:
        port = 443 if scheme == "https" else 80
    if port < 1 or port > 65535:
        raise BadUrl("port %r is out of range" % (port,))
    return parts, host.lower(), port


def gunzip(raw, limit=GZIP_LIMIT):
    """Decompress a gzip body; say whether the expansion was cut."""
    decompressor = zlib.decompressobj(16 + zlib.MAX_WBITS)
    try:
        out = decompressor.decompress(raw, limit + 1)
    except zlib.error as error:
        raise FatalFetch("gzip: %s" % error)
    if len(out) > limit:
        return out[:limit], True
    return out, False


# ---------------------------------------------------------------- fetching


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    """Keeps the fetching library from following redirects by itself."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


class Response(object):
    """One HTTP answer: its status, the bytes read and the head of interest."""

    __slots__ = ("status", "body", "content_type", "charset", "encoding",
                 "truncated", "location")

    def __init__(self, status, body=b"", content_type="", charset=None,
                 encoding="", truncated=False, location=None):
        self.status = status
        self.body = body
        self.content_type = content_type
        self.charset = charset
        self.encoding = encoding
        self.truncated = truncated
        self.location = location


class RedirectRefused(Exception):
    """A redirect hop that the private-address policy will not allow."""


class Fetcher(object):
    """Fetches pages, honouring the private-address policy."""

    def __init__(self, allow_private=False, timeout=FETCH_TIMEOUT):
        self.allow_private = allow_private
        self.timeout = timeout
        self._resolved = {}
        self._opener = urllib.request.build_opener(_NoRedirect())

    def private_host(self, url):
        """True when the URL's host is private, reserved or unresolvable.

        This is the private-address check without the --allow-private
        exemption: a redirect hop to another authority has to pass it even
        when that exemption was given.
        """
        parts, host, port = parse_target(url)
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

    def refused(self, url):
        """True when the URL must not be requested (private or unresolvable)."""
        if self.allow_private:
            return False
        return self.private_host(url)

    def fetch(self, url):
        """Fetch one URL once, without following any redirect.

        Returns a Response.  Raises TransientFetch for a retryable failure
        and FatalFetch for any other HTTP error.  A 3xx answer comes back as
        a Response that carries the location and no body.
        """
        deadline = time.monotonic() + self.timeout
        request = urllib.request.Request(
            url,
            headers={"User-Agent": USER_AGENT, "Accept": "*/*"},
        )
        budget = deadline - time.monotonic()
        if budget <= 0:
            raise TransientFetch("timeout")
        try:
            with self._opener.open(request, timeout=budget) as answer:
                headers = answer.headers
                status = getattr(answer, "status", None) or answer.getcode()
                body, truncated = self._read_body(answer, deadline)
                encoding = (headers.get("Content-Encoding") or "").lower()
                if "gzip" in encoding:
                    body, cut = gunzip(body)
                    truncated = truncated or cut
                return Response(status, body,
                                headers.get("Content-Type", ""),
                                headers.get_content_charset(),
                                encoding, truncated,
                                headers.get("Location"))
        except urllib.error.HTTPError as error:
            code = error.code
            location = None
            try:
                location = error.headers.get("Location")
            except Exception:
                pass
            try:
                error.read()
            except Exception:
                pass
            error.close()
            if code in REDIRECT_CODES:
                return Response(code, b"", "", None, "", False, location)
            if code == 429 or 500 <= code < 600:
                raise TransientFetch("HTTP %s" % code)
            raise FatalFetch("HTTP %s" % code)
        except urllib.error.URLError as error:
            raise TransientFetch(str(error.reason))
        except http.client.HTTPException as error:
            raise TransientFetch(str(error))
        except (socket.timeout, TimeoutError, ConnectionError, OSError) as error:
            raise TransientFetch(str(error))

    def _read_body(self, answer, deadline):
        """Read at most the cap plus one byte; say whether the body was cut."""
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            raise TransientFetch("timeout")
        self._set_read_timeout(answer, remaining)
        chunks = []
        total = 0
        limit = MAX_BODY_BYTES + 1
        while total < limit:
            want = min(READ_CHUNK, limit - total)
            # read1, not read: a buffered read blocks until `want` bytes or EOF,
            # so a dripping body would outlive the budget (rev-hold-lift MEDIUM-1);
            # read1 returns after at most one raw socket read, letting the
            # deadline check run between chunks.
            reader = getattr(answer, "read1", None)
            chunk = reader(want) if reader is not None else answer.read(want)
            if not chunk:
                break
            chunks.append(chunk)
            total += len(chunk)
            if deadline - time.monotonic() <= 0:
                raise TransientFetch("timeout")
        body = b"".join(chunks)
        return body, len(body) > MAX_BODY_BYTES

    @staticmethod
    def _set_read_timeout(answer, seconds):
        """Bound the socket's own timeout by what is left of the budget."""
        handle = None
        for path in (("fp", "raw", "_sock"), ("fp", "fp", "raw", "_sock")):
            node = answer
            try:
                for name in path:
                    node = getattr(node, name)
            except AttributeError:
                continue
            handle = node
            break
        if handle is None:
            return
        try:
            handle.settimeout(max(0.05, seconds))
        except (OSError, AttributeError):
            pass


def follow(fetcher, url, counter):
    """Fetch one URL and follow its redirects by hand.

    counter is a one-element list that counts the requests made.  Returns
    (Response, final URL).  Raises TransientFetch, FatalFetch or
    RedirectRefused.
    """
    current = url
    for _ in range(MAX_REQUESTS_PER_CHAIN):
        counter[0] += 1
        response = fetcher.fetch(current)
        if response.status not in REDIRECT_CODES:
            return response, current
        location = response.location
        if not location:
            raise FatalFetch("redirect without a location")
        target = urllib.parse.urljoin(current, location.strip())
        try:
            _, host, port = parse_target(target)
            _, source_host, source_port = parse_target(current)
        except BadUrl as error:
            raise FatalFetch("malformed redirect target: %s" % error)
        if (host, port) != (source_host, source_port):
            # a hop to another authority must pass the private-host refusal
            # even when --allow-private was given
            if fetcher.private_host(target):
                raise RedirectRefused(target)
        elif not fetcher.allow_private and fetcher.private_host(target):
            raise RedirectRefused(target)
        current = target
    raise FatalFetch("more than %d requests in one chain"
                     % MAX_REQUESTS_PER_CHAIN)


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
    transient_seen = False
    clean_absent = False
    truncated_seen = False
    outcomes = []
    for url in urls:
        try:
            parse_target(url)
        except BadUrl:
            # malformed: no request is made for this URL
            outcomes.append("MALFORMED")
            continue
        if fetcher.refused(url):
            outcomes.append("REFUSED")
            continue
        outcomes.append("TRIED")
        for attempt in range(MAX_ATTEMPTS_PER_URL):
            counter = [0]
            try:
                response, final_url = follow(fetcher, url, counter)
            except RedirectRefused:
                attempts += counter[0]
                outcomes[-1] = "REFUSED"
                break
            except TransientFetch:
                attempts += counter[0]
                transient_seen = True
                if attempt + 1 < MAX_ATTEMPTS_PER_URL:
                    time.sleep(min(gap, 5.0))
                continue
            except FatalFetch:
                attempts += counter[0]
                break
            attempts += counter[0]
            if 200 <= response.status < 300:
                answered = True
                body_text, caption_text = split_content(
                    response.body, response.content_type, response.charset)
                if quote_in_words(normalise_words(body_text), quote_words):
                    return "LOCATED", final_url, transient_seen, attempts
                if (caption_text and not caption_hit
                        and quote_in_words(normalise_words(caption_text), quote_words)):
                    caption_hit = True
                    caption_url = final_url
                elif response.truncated:
                    truncated_seen = True
                else:
                    clean_absent = True
            break
    if caption_hit:
        return "CAPTION_ONLY", caption_url, transient_seen, attempts
    if answered:
        if truncated_seen and not clean_absent:
            return "TRUNCATED", None, transient_seen, attempts
        return "ABSENT", None, transient_seen, attempts
    if outcomes and all(item == "REFUSED" for item in outcomes):
        return "REFUSED", None, transient_seen, attempts
    if outcomes and all(item == "MALFORMED" for item in outcomes):
        return "MALFORMED", None, transient_seen, attempts
    if "TRIED" not in outcomes and "REFUSED" in outcomes:
        return "REFUSED", None, transient_seen, attempts
    if "TRIED" not in outcomes and "MALFORMED" in outcomes:
        return "MALFORMED", None, transient_seen, attempts
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
    "                      [--timeout SECONDS] [--allow-private] [--selftest]\n"
    "                      ID...\n"
)


def parse_args(argv):
    registry = DEFAULT_REGISTRY
    passes = DEFAULT_PASSES
    gap = DEFAULT_GAP
    timeout = FETCH_TIMEOUT
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
        elif arg in ("--registry", "--passes", "--gap", "--timeout"):
            if index + 1 >= len(argv):
                raise InputError("%s needs a value" % arg)
            value = argv[index + 1]
            index += 2
            if arg == "--registry":
                registry = value
            elif arg == "--passes":
                passes = value
            elif arg == "--gap":
                gap = value
            else:
                timeout = value
            continue
        elif arg.startswith("--registry="):
            registry = arg.split("=", 1)[1]
        elif arg.startswith("--passes="):
            passes = arg.split("=", 1)[1]
        elif arg.startswith("--gap="):
            gap = arg.split("=", 1)[1]
        elif arg.startswith("--timeout="):
            timeout = arg.split("=", 1)[1]
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
    try:
        timeout = float(timeout)
    except (TypeError, ValueError):
        raise InputError("--timeout must be a number > 0")
    if not timeout > 0 or timeout in (float("inf"), float("-inf")):
        raise InputError("--timeout must be a number > 0")
    return registry, passes, gap, timeout, allow_private, selftest, ids


def main(argv):
    try:
        registry, passes, gap, timeout, allow_private, selftest, ids = parse_args(argv)
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
    fetcher = Fetcher(allow_private=allow_private, timeout=timeout)
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
            statuses, payload, ctype = route[0], route[1], route[2]
            headers = route[3] if len(route) > 3 else {}
            status = statuses[min(count, len(statuses) - 1)]
            if status == 200:
                body = payload
            else:
                body = b"<html><body><p>error page</p></body></html>"
            self.send_response(status)
            self.send_header("Content-Type", ctype)
            for name, value in headers.items():
                self.send_header(name, value)
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def log_message(self, *args):
            pass

    server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    return server, hits


def _start_stall_server():
    """Start a server that answers the head and then stalls the body."""
    import http.server
    import threading

    class Handler(http.server.BaseHTTPRequestHandler):
        protocol_version = "HTTP/1.1"

        def do_GET(self):
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.send_header("Content-Length", str(1024 * 1024))
            self.end_headers()
            try:
                self.wfile.write(b"x" * 100)
                self.wfile.flush()
                time.sleep(20)
            except (BrokenPipeError, ConnectionResetError):
                pass

        def log_message(self, *args):
            pass

    server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    return server


def run_selftest():
    """Offline fixtures: body, caption kinds, transient, dead+archive, 404,
    closed port and bad inputs."""
    import contextlib
    import gzip
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
    other_routes = {
        "/secret": ([200], html("<p>%s</p>" % quote), "text/html"),
    }
    other_server, other_hits = _start_fixture_server(other_routes)
    other_base = "http://127.0.0.1:%d" % other_server.server_address[1]
    stall_server = _start_stall_server()
    stall_base = "http://127.0.0.1:%d" % stall_server.server_address[1]
    routes["/redir"] = ([302], b"", "text/html", {"Location": "/redirtarget"})
    routes["/redirtarget"] = ([200], html("<p>%s.</p>" % quote), "text/html")
    routes["/hop"] = ([302], b"", "text/html",
                      {"Location": other_base + "/secret"})
    routes["/gz"] = ([200], gzip.compress(html("<p>%s.</p>" % quote)),
                     "text/html", {"Content-Encoding": "gzip"})
    pad = "lima " * 900000
    routes["/truncfar"] = ([200], html("<p>%s</p><p>%s</p>" % (pad, quote)),
                            "text/html")
    routes["/truncnear"] = ([200], html("<p>%s</p><p>%s</p>" % (quote, pad)),
                             "text/html")
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
        row("S19", "%s/redir" % base, quoted),
        row("S20", "%s/hop" % base, quoted),
        row("S21", "http://127.0.0.1:99999/x", quoted),
        row("S22", "http://[2001:db8::1/x", quoted),
        row("S23", "http://:80/x", quoted),
        row("S24", "%s/gz" % base, quoted),
        row("S25", "%s/truncfar" % base, quoted),
        row("S26", "%s/truncnear" % base, quoted),
        row("S27", "%s/stall" % stall_base, quoted),
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

    def url_of(text, row_id):
        for line in text.splitlines():
            if line.startswith("ROW %s " % row_id):
                return line.split("url=", 1)[1]
        return None

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
        ("timeout zero", ["--registry", registry_path, "--timeout", "0", "S1"]),
        ("timeout not a number", ["--registry", registry_path, "--timeout", "x", "S1"]),
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

    print("-- selftest: redirect chain --")
    hits.clear()
    code, out = run(["S19"])
    check("redirect verdict", verdicts_of(out).get("S19"), ("LOCATED", "attempts=2"))
    check("redirect hits", (hits.get("/redir", 0), hits.get("/redirtarget", 0)),
          (1, 1))
    check("redirect url", url_of(out, "S19"), base + "/redirtarget")

    print("-- selftest: cross-authority redirect refused --")
    hits.clear()
    other_hits.clear()
    code, out = run(["S20"])
    check("hop refused", verdicts_of(out).get("S20"), ("REFUSED", "attempts=1"))
    check("hop source hit", hits.get("/hop", 0), 1)
    check("hop target untouched", other_hits.get("/secret", 0), 0)

    print("-- selftest: malformed urls --")
    code, out = run(["S21", "S22", "S23"])
    verdicts = verdicts_of(out)
    check("malformed port", verdicts.get("S21"), ("MALFORMED", "attempts=0"))
    check("malformed ipv6", verdicts.get("S22"), ("MALFORMED", "attempts=0"))
    check("malformed empty host", verdicts.get("S23"), ("MALFORMED", "attempts=0"))
    check("malformed exit", code, 1)

    print("-- selftest: gzip --")
    code, out = run(["S24"])
    check("gzip verdict", verdicts_of(out).get("S24"), ("LOCATED", "attempts=1"))

    print("-- selftest: truncation --")
    code, out = run(["S25", "S26"])
    verdicts = verdicts_of(out)
    check("truncated far", verdicts.get("S25"), ("TRUNCATED", "attempts=1"))
    check("truncated near", verdicts.get("S26"), ("LOCATED", "attempts=1"))
    check("truncated url", url_of(out, "S25"), "-")

    print("-- selftest: request budget --")
    code, out = run(["S27"], extra=["--timeout", "1", "--passes", "1"])
    check("stall verdict", verdicts_of(out).get("S27"),
          ("UNREACHABLE", "attempts=3"))

    server.shutdown()
    server.server_close()
    other_server.shutdown()
    other_server.server_close()
    stall_server.shutdown()
    stall_server.server_close()
    print("-- selftest: %d checks, %d failures --" % (checks, len(failures)))
    for failure in failures:
        print("FAILED %s" % failure)
    return 0 if not failures else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
