#!/usr/bin/env python3
r"""Round-61 re-open locator: reports/round-57/reopen-quote.py with only this first docstring line changed (instrument of claim C's LOCATE leg; also the scribes' pre-filing check).

  python3 -B reports/round-57/reopen-quote.py URL QUOTE      one source, one quote
  python3 -B reports/round-57/reopen-quote.py --row S###     a corpus/SOURCES.md row (from the lane root)

It fetches URL live with an ordinary GET (urllib, a desktop User-Agent string, redirects followed,
no cookies, no challenge solving, up to three attempts on HTTP 429, 5xx or 508 honouring Retry-After
up to 30 s (else 8 s), Wayback requests one at a time, 120 s timeout, 120 MB cap), turns the body
into text and looks for QUOTE in it. Text: a body starting `%PDF` goes through pypdf 5.4.0 (run as
`uv run --no-project --quiet --with pypdf==5.4.0 python3 -c ...`); a JSON body has every string
value joined; an HTML body keeps the text nodes outside script and style, with character
references decoded; any other body is decoded as UTF-8 (errors replaced). Match rule, applied to
QUOTE and to the text alike: NFKC, casefold, every run of characters that are not letters or
digits (\W, and the underscore) becomes one space. QUOTE must have at least 8 normalised words.
QUOTE is located when its normalised word sequence occurs in the normalised text, or in the text
after a hyphen or a not-sign at a line end is joined (`fidal-\nlgos` -> `fidallgos`). A URL cannot
vouch for a quote when its host is a search, echo or code-hosting service (DENY_HOSTS), its path
names a search and carries a query, or its query carries a search key (q, query, search, text, keys, term, s), it names
the lane (`kotodama`, `shokunin`), or it carries any three consecutive words of the quote (a page
that reflects its request). A row is located when any http(s) URL in its `source` cell (at most
four, in order) locates the first double-quoted span ("..." or a curly pair) of its `anchor` cell.
Revised before any data after the pre-dispatch critic CriticClauseListC57
(.ufo/waves/round-57/predispatch/CriticClauseListC57.md) located invented quotes through echo and
search URLs and located the anchor quotes "a" and "of the" on arbitrary pages.

Prints one line `LOCATED <url>` or `NOT_LOCATED <reason>`; exit 0 located, 1 not located, 2 on a
usage error. A fetch error is NOT_LOCATED, never a pass. Read-only; writes only a temporary PDF.
"""
import html.parser
import json
import os
import re
import subprocess
import sys
import tempfile
import threading
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request

UA = "Mozilla/5.0 (X11; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0"
CAP = 120 * 1024 * 1024
URL = re.compile(r"https?://[^\s<>\"|`]+")
QUOTE = re.compile(r'"([^"]+)"|“([^“”]+)”')
ROW = re.compile(r"^\|\s*(S\d{3,})\s*\|")
PDF_SCRIPT = ("import sys,pypdf\n"
              "r=pypdf.PdfReader(sys.argv[1])\n"
              "for p in r.pages:\n"
              "    try:\n        sys.stdout.write((p.extract_text() or '')+'\\n')\n"
              "    except Exception:\n        pass\n")


class _Text(html.parser.HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts, self.skip = [], 0

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self.skip += 1

    def handle_endtag(self, tag):
        if tag in ("script", "style") and self.skip:
            self.skip -= 1

    def handle_data(self, data):
        if not self.skip:
            self.parts.append(data)


def normalise(text):
    return " ".join(re.sub(r"[\W_]+", " ", unicodedata.normalize("NFKC", text).casefold()).split())


def fetch(url):
    request = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    for attempt in (1, 2, 3):
        try:
            with urllib.request.urlopen(request, timeout=120) as response:
                body = response.read(CAP + 1)
                ctype = response.headers.get("Content-Type", "")
            break
        except urllib.error.HTTPError as error:
            if attempt == 3 or error.code not in (429, 500, 502, 503, 504, 508, 520, 522, 524):
                raise
            wait = error.headers.get("Retry-After", "") if error.headers else ""
            time.sleep(min(int(wait), 30) if wait.isdigit() else 8)
    if len(body) > CAP:
        raise ValueError("body over cap")
    return body, ctype


def _strings(value, out):
    if isinstance(value, str):
        out.append(value)
    elif isinstance(value, dict):
        for item in value.values():
            _strings(item, out)
    elif isinstance(value, list):
        for item in value:
            _strings(item, out)


def to_text(body, ctype):
    if body[:5] == b"%PDF-" or body.lstrip()[:5] == b"%PDF-":
        with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as handle:
            handle.write(body)
            name = handle.name
        try:
            done = subprocess.run(["uv", "run", "--no-project", "--quiet", "--with", "pypdf==5.4.0",
                                   "python3", "-c", PDF_SCRIPT, name],
                                  capture_output=True, text=True, timeout=900)
            return done.stdout
        finally:
            os.unlink(name)
    text = body.decode("utf-8", errors="replace")
    if "json" in ctype or text.lstrip()[:1] in "[{":
        try:
            out = []
            _strings(json.loads(text), out)
            return "\n".join(out)
        except ValueError:
            pass
    if "html" in ctype or re.search(r"<(?:!doctype|html|body|p|div)\b", text[:5000], re.I):
        parser = _Text()
        parser.feed(text)
        parser.close()
        return "\n".join(parser.parts)
    return text


def locate_in(text, quote):
    want = normalise(quote)
    if not want:
        return False
    joined = re.sub(r"(\w)[-¬­]\s*\n\s*(\w)", r"\1\2", text)
    return (" " + want + " ") in (" " + normalise(text) + " ") or \
           (" " + want + " ") in (" " + normalise(joined) + " ")


MIN_WORDS = 8
DENY_HOSTS = ("httpbin.org", "postman-echo.com", "bing.com", "google.", "duckduckgo.com", "yahoo.com",
              "yandex.", "baidu.com", "github.com", "githubusercontent.com", "gitlab.com", "pastebin.com",
              "gist.", "bitbucket.org", "codeberg.org")
QUERY_KEYS = re.compile(r"(?:^|&)(?:q|query|search|text|keys|term|s)=", re.I)
_WAYBACK = threading.Lock()


def url_refusal(url, quote):
    """Why a URL cannot vouch for a quote (empty when it can): a search, echo or code host, a query
    or path that names a search, the lane's own name, or any three consecutive quote words in the URL."""
    parts = urllib.parse.urlsplit(url)
    host = parts.netloc.lower()
    if any(d in host for d in DENY_HOSTS):
        return "denied-host"
    if ("search" in parts.path.lower() and parts.query) or QUERY_KEYS.search(parts.query):
        return "search-url"
    if "kotodama" in url.lower() or "shokunin" in url.lower():
        return "self-hosted"
    in_url = " " + normalise(urllib.parse.unquote_plus(url)) + " "
    words = normalise(quote).split()
    if any(" " + " ".join(words[i:i + 3]) + " " in in_url for i in range(max(len(words) - 2, 0))):
        return "url-reflects-quote"
    return ""


def locate(urls, quote):
    """(located, detail) for the first URL that locates quote; urls tried in order."""
    if len(normalise(quote).split()) < MIN_WORDS:
        return False, f"quote under {MIN_WORDS} words"
    reasons = []
    for url in urls[:4]:
        refusal = url_refusal(url, quote)
        if refusal:
            reasons.append(f"{url} {refusal}")
            continue
        try:
            if "web.archive.org" in url:
                with _WAYBACK:
                    body, ctype = fetch(url)
            else:
                body, ctype = fetch(url)
            if locate_in(to_text(body, ctype), quote):
                return True, url
            reasons.append(f"{url} quote-absent")
        except Exception as error:  # every fetch or parse failure is a non-location
            reasons.append(f"{url} {type(error).__name__}")
    return False, "; ".join(reasons) or "no-url"


def trim(url):
    """Drop trailing punctuation, and a closing parenthesis only when it is unbalanced."""
    while url and (url[-1] in ".,;:'" or (url[-1] == ")" and url.count(")") > url.count("("))):
        url = url[:-1]
    return url


def row_target(cells):
    """(urls, quote) of a SOURCES row split on `|`: URLs of the source cell, first quote of anchor."""
    urls = [trim(u) for u in URL.findall(cells[2])]
    found = QUOTE.search(cells[6])
    quote = (found.group(1) or found.group(2)) if found else ""
    return urls, quote


def main(argv):
    if len(argv) == 2 and argv[0] == "--row":
        for line in open("corpus/SOURCES.md", encoding="utf-8"):
            match = ROW.match(line)
            if match and match.group(1) == argv[1]:
                urls, quote = row_target(line.split("|"))
                break
        else:
            print(f"NOT_LOCATED no row {argv[1]}")
            return 1
    elif len(argv) == 2:
        urls, quote = [argv[0]], argv[1]
    else:
        print(__doc__.splitlines()[0], file=sys.stderr)
        return 2
    if not quote:
        print("NOT_LOCATED no quote")
        return 1
    ok, detail = locate(urls, quote)
    print(("LOCATED " if ok else "NOT_LOCATED ") + detail)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
