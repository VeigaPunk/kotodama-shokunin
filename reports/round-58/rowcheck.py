#!/usr/bin/env python3
r"""Round-58 row checks: relevance binding and site boilerplate (instrument of claim C's RELEVANCE
and BOILER legs; also the scouts' pre-filing check). Written for the round-57 closure's routed
defect 2 (corpus/lessons/round-57-verifier-spotcheck.md §5 item 2: LOCATE is blind to relevance;
real off-topic page text such as a site footer passes it).

  python3 -B reports/round-58/rowcheck.py --row S### [--entry PATH]   a corpus/SOURCES.md row
  python3 -B reports/round-58/rowcheck.py --draft FILE [--entry PATH] each `| S### | ...` line of FILE

Per row (cells split on `|` as in corpus/SOURCES.md: cells[2] source, cells[6] anchor,
cells[7] teaches), with QUOTE the first double-quoted span of the anchor (reports/round-58/
reopen-quote.py `row_target`):

  LOCATE     reopen-quote.locate(urls, QUOTE) is true: the quote (at least 8 normalised words) is in
             the text one of the row's source URLs (at most four) serves now. LOC_URL is that URL.
  BOILER     the quote is not site boilerplate: the ROOT page of LOC_URL's site is fetched live
             (same fetch and text rules) and QUOTE is NOT located in it. ROOT is
             `<scheme>://<host>/`; for a Wayback URL `web.archive.org/web/<ts>[flags]/<orig>` it is
             `https://web.archive.org/web/<ts>/<orig scheme>://<orig host>/`. BOILER fails when the
             row is not located (no LOC_URL), when ROOT cannot be fetched, when LOC_URL is ROOT
             itself, or when QUOTE is located in ROOT. A footer, header, cookie or navigation
             sentence that a site prints on every page is printed on its home page too.
  RELEVANCE  the quote is bound to the row's teaching, and both to the entry:
             (a) stems(QUOTE) and stems(teaches) share at least 2 stems;
             (b) teaches carries no run of 6 consecutive normalised words of QUOTE (no copied quote);
             (c) with --entry, stems(teaches) and stems(L) share at least 2 stems, where L is every
                 line of the entry that cites the row's id as a whole word (`\bS###\b`), joined,
                 S-ids removed; a row the entry does not cite fails (c);
             (d) with --entry, stems(QUOTE) and stems(L) share at least 2 stems.
             stems(text): the locator's normalisation (NFKC, casefold, non-letters and non-digits
             to spaces), words of at least 4 characters not in STOP, a final `s` dropped when the
             word is longer than 4 characters, then the first 5 characters.
  TOPIC      the quote and the page that located it are about place names (page-anchored text,
             not a cell the author writes): a NAMING-PLACE window is a word whose stem is in
             NAMING with a word whose stem is in PLACE at most WINDOW (3) normalised words away
             (the same word counts when its stem is in both sets, such as `topon` or `hydro`; sets
             below). The quote holds at least 1 window and the text LOC_URL serves (fetched live
             again) at least PAGE_HITS (3). Not located or an unfetchable page fails.

Prints one line per row: `S### LOCATE <ok> BOILER <ok> RELEVANCE <ok> TOPIC <ok> <details>`
(ok = PASS|FAIL). Exit 0 when every checked leg passes for every row, 1 otherwise, 2 on usage or
unreadable input. Read-only; network GETs only.
"""
import importlib.util
import os
import re
import sys
import urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("reopen_quote_58", os.path.join(HERE, "reopen-quote.py"))
locator = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(locator)

MIN_SHARED = 2
COPY_RUN = 6
WINDOW = 3
PAGE_HITS = 3
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


def boiler(loc_url, quote):
    """(ok, detail): the quote is not located on the site's root page."""
    if not loc_url:
        return False, "not-located"
    root = root_of(loc_url)
    if root.rstrip("/").lower() == loc_url.rstrip("/").lower():
        return False, f"source-is-root {root}"
    try:
        if "web.archive.org" in root:
            with locator._WAYBACK:
                body, ctype = locator.fetch(root)
        else:
            body, ctype = locator.fetch(root)
        text = locator.to_text(body, ctype)
    except Exception as error:  # an unfetchable root cannot clear the quote
        return False, f"root-unfetchable {root} {type(error).__name__}"
    if locator.locate_in(text, quote):
        return False, f"quote-on-root {root}"
    return True, f"root-clear {root}"


def relevance(sid, quote, teaches, entry_text):
    shared = stems(quote) & stems(teaches)
    problems = []
    if len(shared) < MIN_SHARED:
        problems.append(f"quote-teaches shared={sorted(shared)}")
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


NAMING = {"name", "named", "namin", "namen", "ortsn", "flurn", "nombr", "topon", "hydro", "orony",
          "ethno", "endon", "exony", "onoma", "gazet", "etymo", "renam", "epony"}
PLACE = {"place", "topon", "hydro", "orony", "endon", "exony", "gazet", "river", "town", "villa",
         "city", "citie", "mount", "hill", "islan", "lake", "settl", "regio", "count", "paris",
         "coast", "valle", "stree", "burgh", "ford", "farm", "geogr", "lands", "terri", "distr",
         "provi", "natio", "strea", "creek", "brook", "fores", "harbo", "cape", "penin"}


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
    """Number of word positions holding a NAMING stem with a PLACE stem at most WINDOW words away."""
    seq = stem_seq(text)
    hits = 0
    for i, stem in enumerate(seq):
        if stem in NAMING and any(seq[j] in PLACE for j in range(max(i - WINDOW, 0), min(i + WINDOW + 1, len(seq)))):
            hits += 1
    return hits


def page_text(url):
    if "web.archive.org" in url:
        with locator._WAYBACK:
            body, ctype = locator.fetch(url)
    else:
        body, ctype = locator.fetch(url)
    return locator.to_text(body, ctype)


def topic(quote, loc_url):
    """(ok, detail): the quote and the page that located it are about place names."""
    quote_hits = window_hits(quote)
    if not loc_url:
        return False, f"quote_hits={quote_hits} not-located"
    try:
        page_hits = window_hits(page_text(loc_url))
    except Exception as error:  # an unfetchable page cannot show its topic
        return False, f"quote_hits={quote_hits} page-unfetchable {type(error).__name__}"
    ok = quote_hits >= 1 and page_hits >= PAGE_HITS
    return ok, f"quote_hits={quote_hits} page_hits={page_hits} need=1/{PAGE_HITS}"


def check_row(cells, entry_text=None):
    """{'LOCATE'|'BOILER'|'RELEVANCE'|'TOPIC': (ok, detail)} for one row."""
    sid = cells[1].strip()
    urls, quote = locator.row_target(cells)
    if quote:
        located, detail = locator.locate(urls, quote)
    else:
        located, detail = False, "no quote in anchor"
    result = {"LOCATE": (located, detail)}
    result["BOILER"] = boiler(detail if located else "", quote)
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
