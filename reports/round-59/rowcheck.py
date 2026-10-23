#!/usr/bin/env python3
r"""Round-59 row checks (instrument of claim C's LOCATE, BOILER, RELEVANCE and TOPIC legs; also the
scouts' pre-filing check). Copied from reports/round-58/rowcheck.py with three changes, all made
before any round-59 data seat: (1) TOPIC's sets name the round-59 topic (amulets, talismans and
apotropaic marks) instead of place names; (2) FETCH-59, the declared fetch rule below, replaces
round 58's independent re-fetches (round-58 verifier spot-check §5 item 5: two live 403s at
.gov.au hosts sank claim C because each leg re-fetched and no fetch rule was declared before data);
(3) BOILER's root falls back to an archived capture of the root under FETCH-59.

FETCH-59 (declared before data; never relaxed after): every URL is fetched at most once per run
(reopen-quote.py `fetch`: an ordinary GET, three attempts on HTTP 429/5xx/508) and its body, or its
error, is reused by every leg. A row's source cell lists its live page URL first and may list a
Wayback capture of the same page (`https://web.archive.org/web/<14 digits>id_/<live URL>`); LOCATE
tries the URLs in order (at most four), a URL whose fetch raises an error is skipped and never
passes, and LOC_URL is the first URL whose text locates the quote. BOILER and TOPIC read LOC_URL's
cached body (no second fetch). BOILER's ROOT is fetched once; when the live ROOT raises a fetch
error and LOC_URL is not itself a capture, the capture root
`https://web.archive.org/web/<TS>id_/<scheme>://<host>/` is fetched instead, TS being the timestamp
of the row's first Wayback URL, or `2026` when the row lists none. A row with no URL that locates,
or whose ROOT and capture root both fail, FAILS. No slack, no per-row allowance, no retry beyond
the three attempts.

  python3 -B reports/round-59/rowcheck.py --row S### [--entry PATH]   a corpus/SOURCES.md row
  python3 -B reports/round-59/rowcheck.py --draft FILE [--entry PATH] each `| S### | ...` line of FILE

Per row (cells split on `|` as in corpus/SOURCES.md: cells[2] source, cells[6] anchor,
cells[7] teaches), with QUOTE the first double-quoted span of the anchor (reports/round-59/
reopen-quote.py `row_target`):

  LOCATE     reopen-quote.locate(urls, QUOTE) is true: the quote (at least 8 normalised words) is in
             the text one of the row's source URLs (at most four) serves now. LOC_URL is that URL.
  BOILER     the quote is not site boilerplate and not a page label: the ROOT page of LOC_URL's site
             is fetched live (same fetch and text rules) and QUOTE is NOT located in it; and QUOTE is
             NOT located in the page's own labels (the text of its <title>, <h1> elements and every
             <meta content="..."> value, tags stripped, entities decoded). ROOT is
             `<scheme>://<host>/`; for a Wayback URL `web.archive.org/web/<ts>[flags]/<orig>` it is
             `https://web.archive.org/web/<ts>/<orig scheme>://<orig host>/`. BOILER fails when the
             row is not located (no LOC_URL), when ROOT or LOC_URL cannot be fetched, when LOC_URL is
             ROOT itself, when QUOTE is located in ROOT, or when it is located in the page labels. A
             footer, header, cookie or navigation sentence a site prints on every page is printed on its
             home page too; a title, heading or meta description can be quoted without reading the body.
  RELEVANCE  the quote is bound to the row's teaching, and both to the entry:
             (a) stems(QUOTE) and stems(teaches) share at least 2 stems;
             (b) teaches carries no run of 6 consecutive normalised words of QUOTE (no copied quote);
             (c) with --entry, stems(teaches) and stems(L) share at least 2 stems, where L is every
                 line of the entry that cites the row's id as a whole word (`\bS###\b`), joined,
                 S-ids removed; a row the entry does not cite fails (c);
             (d) with --entry, stems(QUOTE) and stems(L) share at least 2 stems;
             (e) teaches is a sentence: at least TEACHES_WORDS (8) whitespace words, ending with `.`.
             stems(text): the locator's normalisation (NFKC, casefold, non-letters and non-digits
             to spaces), words of at least 4 characters not in STOP, a final `s` dropped when the
             word is longer than 4 characters, then the first 5 characters.
  TOPIC      the quote and the page that located it are about protective objects and marks
             (page-anchored text, not a cell the author writes): a CHARM-GUARD window is a word
             whose stem is in CHARM with a word whose stem is in GUARD at most WINDOW (3)
             normalised words away (the same word counts when its stem is in both sets, such as
             `amule`, `talis`, `apotr` or `phyla`; sets below). The quote holds at least 1 window and
             at least 2 DISTINCT FUNCTION words (a sentence, not a heading or list fragment); the text
             LOC_URL serves (its cached body) holds at least PAGE_HITS (3) windows and at least
             PAGE_TERMS (2) matches of DISCIPLINE (the field's own terms: amulet*, talism*,
             apotropai*, phylacter*, evil eye, charm(s), protective magic/symbol/mark ..., witch
             marks, ofuda, omamori, mezuz*, hamsa, nazar, wedjat, udjat, bulla, scarab(s) ...).
             Not located fails.

Prints one line per row: `S### LOCATE <ok> BOILER <ok> RELEVANCE <ok> TOPIC <ok> <details>`
(ok = PASS|FAIL). Exit 0 when every checked leg passes for every row, 1 otherwise, 2 on usage or
unreadable input. Read-only; network GETs only.
"""
import html
import importlib.util
import os
import re
import sys
import threading
import urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("reopen_quote_59", os.path.join(HERE, "reopen-quote.py"))
locator = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(locator)

# FETCH-59: one fetch per URL per run; bodies and errors are reused by every leg.
_CACHE = {}
_CACHE_LOCK = threading.Lock()
_RAW_FETCH = locator.fetch


def _fetch_once(url):
    with _CACHE_LOCK:
        hit = _CACHE.get(url)
    if hit is None:
        try:
            hit = _RAW_FETCH(url)
        except Exception as error:  # cached so that no later leg re-fetches
            hit = error
        with _CACHE_LOCK:
            hit = _CACHE.setdefault(url, hit)
    if isinstance(hit, Exception):
        raise hit
    return hit


locator.fetch = _fetch_once

MIN_SHARED = 2
COPY_RUN = 6
WINDOW = 3
PAGE_HITS = 3
TEACHES_WORDS = 8
STOP = set("""
about above across after again against also although among an and another any are around because
been before being below between both but by can cannot could did does doing done down during each
either else even ever every few for from further had has have having her here hers herself him
himself his how however into its itself just least less like made make many more most much must
near neither never next none nor not now off often once only onto other others otherwise our ours
over own per perhaps rather same seem seen shall she should since some such than that their theirs
them themselves then there these they this those though through thus till too toward towards under
unless until upon very was were what whatever when where whether which while who whom whose why will
with within without would yet you your yours also being shows show shown given gives give used uses
using use one two three four five first second third part parts page pages text texts says said
""".split())
WAYBACK = re.compile(r"^/web/(\d+)[a-z_]*/(https?)://([^/]+)", re.I)


def stems(text):
    out = set()
    for word in locator.normalise(text).split():
        if len(word) < 4 or word in STOP:
            continue
        if len(word) > 4 and word.endswith("s"):
            word = word[:-1]
        out.add(word[:5])
    return out


def copied(quote, teaches):
    words = locator.normalise(quote).split()
    hay = " " + locator.normalise(teaches) + " "
    return any(" " + " ".join(words[i:i + COPY_RUN]) + " " in hay for i in range(max(len(words) - COPY_RUN + 1, 0)))


def root_of(url):
    parts = urllib.parse.urlsplit(url)
    if parts.netloc.lower() == "web.archive.org":
        found = WAYBACK.match(parts.path)
        if found:
            return f"https://web.archive.org/web/{found.group(1)}/{found.group(2)}://{found.group(3)}/"
    return f"{parts.scheme}://{parts.netloc}/"


LABELS = [re.compile(r"<title[^>]*>(.*?)</title>", re.I | re.S),
          re.compile(r"<h1[^>]*>(.*?)</h1>", re.I | re.S),
          re.compile(r"<meta\b[^>]*\bcontent\s*=\s*\"([^\"]*)\"", re.I),
          re.compile(r"<meta\b[^>]*\bcontent\s*=\s*'([^']*)'", re.I)]


def capture_root(loc_url, urls):
    """FETCH-59 capture root of LOC_URL's site: the row's first Wayback timestamp, else 2026."""
    stamp = "2026"
    for url in urls:
        parts = urllib.parse.urlsplit(url)
        found = WAYBACK.match(parts.path) if parts.netloc.lower() == "web.archive.org" else None
        if found:
            stamp = found.group(1)
            break
    parts = urllib.parse.urlsplit(loc_url)
    return f"https://web.archive.org/web/{stamp}id_/{parts.scheme}://{parts.netloc}/"


def _get_text(url):
    if "web.archive.org" in url:
        with locator._WAYBACK:
            body, ctype = locator.fetch(url)
    else:
        body, ctype = locator.fetch(url)
    return locator.to_text(body, ctype)


def boiler(loc_url, quote, urls=()):
    """(ok, detail): the quote is not located on the site's root page (FETCH-59 root rule)."""
    if not loc_url:
        return False, "not-located"
    root = root_of(loc_url)
    if root.rstrip("/").lower() == loc_url.rstrip("/").lower():
        return False, f"source-is-root {root}"
    try:
        text = _get_text(root)
    except Exception as error:  # FETCH-59: the live root failed; try the capture root once
        if "web.archive.org" in loc_url:
            return False, f"root-unfetchable {root} {type(error).__name__}"
        fallback = capture_root(loc_url, urls)
        try:
            text = _get_text(fallback)
        except Exception as error2:  # an unfetchable root cannot clear the quote
            return False, (f"root-unfetchable {root} {type(error).__name__}; "
                           f"capture {fallback} {type(error2).__name__}")
        root = fallback
    if locator.locate_in(text, quote):
        return False, f"quote-on-root {root}"
    try:
        if "web.archive.org" in loc_url:
            with locator._WAYBACK:
                body, ctype = locator.fetch(loc_url)
        else:
            body, ctype = locator.fetch(loc_url)
    except Exception as error:
        return False, f"page-unfetchable {type(error).__name__}"
    raw = body.decode("utf-8", "replace") if isinstance(body, bytes) else str(body)
    labels = []
    for pattern in LABELS:
        labels.extend(pattern.findall(raw))
    label_text = html.unescape(re.sub(r"<[^>]+>", " ", "\n".join(labels)))
    if label_text.strip() and locator.locate_in(label_text, quote):
        return False, "quote-is-title-heading-or-meta"
    return True, f"root-clear {root}; not a title, h1 or meta label"


def relevance(sid, quote, teaches, entry_text):
    shared = stems(quote) & stems(teaches)
    problems = []
    if len(shared) < MIN_SHARED:
        problems.append(f"quote-teaches shared={sorted(shared)}")
    if len(teaches.split()) < TEACHES_WORDS or not teaches.strip().endswith("."):
        problems.append(f"teaches-not-a-sentence words={len(teaches.split())}")
    if copied(quote, teaches):
        problems.append("teaches-copies-quote")
    if entry_text is not None:
        lines = [l for l in entry_text.splitlines() if re.search(rf"\b{sid}\b", l)]
        if not lines:
            problems.append("entry-does-not-cite")
        else:
            cited_text = re.sub(r"\bS\d{3,}\b", " ", "\n".join(lines))
            bound = stems(teaches) & stems(cited_text)
            if len(bound) < MIN_SHARED:
                problems.append(f"teaches-entry shared={sorted(bound)}")
            qbound = stems(quote) & stems(cited_text)
            if len(qbound) < MIN_SHARED:
                problems.append(f"quote-entry shared={sorted(qbound)}")
    return not problems, ("; ".join(problems) or f"shared={sorted(shared)[:6]}")


CHARM = {"amule", "talis", "apotr", "phyla", "charm", "mezuz", "tefil", "omamo", "ofuda", "scara",
         "bulla", "nazar", "hamsa", "wedja", "udjat", "fetis", "token", "penda", "neckl", "bead",
         "ring", "inscr", "scrol", "seal", "plaqu", "figur", "image", "icon", "mark", "symbo", "sign",
         "eyes", "objec", "devic", "stone", "relic", "cross", "knot", "spell", "incan", "pazuz",
         "gorgo"}
GUARD = {"amule", "talis", "apotr", "phyla", "prote", "ward", "warde", "wardi", "avert", "guard",
         "evil", "harm", "misfo", "demon", "spiri", "witch", "luck", "lucky", "heal", "heali",
         "bless", "magic", "curse", "dange", "illne", "disea", "safe", "safet", "power", "sacre",
         "holy", "fortu", "ghost", "malev", "malef", "envy", "jealo", "defen", "repel", "banis",
         "exorc", "sickn"}


def stem_seq(text):
    """One entry per normalised word: its stem (as in stems()) or None for a short or stop word."""
    out = []
    for word in locator.normalise(text).split():
        if len(word) < 4 or word in STOP:
            out.append(None)
            continue
        if len(word) > 4 and word.endswith("s"):
            word = word[:-1]
        out.append(word[:5])
    return out


def window_hits(text):
    """Number of word positions holding a CHARM stem with a GUARD stem at most WINDOW words away."""
    seq = stem_seq(text)
    hits = 0
    for i, stem in enumerate(seq):
        if stem in CHARM and any(seq[j] in GUARD for j in range(max(i - WINDOW, 0), min(i + WINDOW + 1, len(seq)))):
            hits += 1
    return hits


def page_text(url):
    if "web.archive.org" in url:
        with locator._WAYBACK:
            body, ctype = locator.fetch(url)
    else:
        body, ctype = locator.fetch(url)
    return locator.to_text(body, ctype)


DISCIPLINE = re.compile(r"\b(?:amulet\w*|talism\w*|apotropai\w*|phylacter\w*|evil eye|charms?"
                        r"|protective (?:magic|symbols?|marks?|signs?|devices?|objects?|charms?)"
                        r"|witch(?:es)? marks?|ritual protection marks?|ofuda|omamori|mezuz\w*|tefillin"
                        r"|hamsa|nazar|wedjat|udjat|bullae?|scarabs?|pazuzu|lamashtu|gorgoneion"
                        r"|magic(?:al)? (?:texts?|scrolls?|bowls?|papyr\w*))\b")
FUNCTION = set("the a an of in on at is are was were be been to from by for and or that which as with its their this".split())
PAGE_TERMS = 2
QUOTE_FUNCTION = 2


def topic(quote, loc_url):
    """(ok, detail): the quote is a sentence about protective objects and its page is about them."""
    quote_hits = window_hits(quote)
    function_words = len({w for w in locator.normalise(quote).split() if w in FUNCTION})
    if not loc_url:
        return False, f"quote_hits={quote_hits} not-located"
    try:
        text = page_text(loc_url)
    except Exception as error:  # an unfetchable page cannot show its topic
        return False, f"quote_hits={quote_hits} page-unfetchable {type(error).__name__}"
    page_hits = window_hits(text)
    terms = len(DISCIPLINE.findall(locator.normalise(text)))
    ok = (quote_hits >= 1 and function_words >= QUOTE_FUNCTION and page_hits >= PAGE_HITS
          and terms >= PAGE_TERMS)
    return ok, (f"quote_hits={quote_hits} function_words={function_words} page_hits={page_hits} "
                f"page_terms={terms} need=1/{QUOTE_FUNCTION}/{PAGE_HITS}/{PAGE_TERMS}")


def check_row(cells, entry_text=None):
    """{'LOCATE'|'BOILER'|'RELEVANCE'|'TOPIC': (ok, detail)} for one row."""
    sid = cells[1].strip()
    urls, quote = locator.row_target(cells)
    if quote:
        located, detail = locator.locate(urls, quote)
    else:
        located, detail = False, "no quote in anchor"
    result = {"LOCATE": (located, detail)}
    result["BOILER"] = boiler(detail if located else "", quote, urls)
    result["RELEVANCE"] = relevance(sid, quote, cells[7] if len(cells) > 7 else "", entry_text)
    result["TOPIC"] = topic(quote, detail if located else "")
    return result


def main(argv):
    entry_text = None
    if "--entry" in argv:
        i = argv.index("--entry")
        try:
            entry_text = open(argv[i + 1], encoding="utf-8").read()
        except (IndexError, OSError) as error:
            print(f"ROWCHECK_INPUT_ERROR {error}", file=sys.stderr)
            return 2
        argv = argv[:i] + argv[i + 2:]
    if len(argv) != 2 or argv[0] not in ("--row", "--draft"):
        print(__doc__.splitlines()[0], file=sys.stderr)
        return 2
    try:
        if argv[0] == "--row":
            lines = [l for l in open("corpus/SOURCES.md", encoding="utf-8")
                     if (m := locator.ROW.match(l)) and m.group(1) == argv[1]]
        else:
            lines = [l for l in open(argv[1], encoding="utf-8") if locator.ROW.match(l)]
    except OSError as error:
        print(f"ROWCHECK_INPUT_ERROR {error}", file=sys.stderr)
        return 2
    if not lines:
        print("ROWCHECK no row")
        return 1
    ok_all = True
    for line in lines:
        cells = line.split("|")
        if len(cells) < 13:
            print(f"{cells[1].strip()} MALFORMED cells={len(cells)}")
            ok_all = False
            continue
        result = check_row(cells, entry_text)
        ok_all &= all(ok for ok, _ in result.values())
        print(cells[1].strip() + " " + " ".join(f"{k} {'PASS' if ok else 'FAIL'}" for k, (ok, _) in result.items())
              + " | " + " | ".join(f"{k}: {d[:200]}" for k, (_, d) in result.items()))
    return 0 if ok_all else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
