#!/usr/bin/env python3
r"""Round-62 claim D acceptance (revision 1, before any data: KEEP and FRESH legs, ROWS same-page
capture within the locator budget, LOCATE pass loop factored for its control) (depth, sourced): the four footwear-entry lines the round-61 closure
routed (corpus/lessons/round-61-verifier-spotcheck.md section 7 item 1) are repaired at the lines
they stand on, and the talaria line rests on a tier A/B row opened this round. Run from the lane root:

  python3 -B reports/round-62/accept-d.py [--root DIR]

BASE is the round base d42ffb89 (read with read-only `git show BASE:<path>` from --root's history).
Line numbers are 1-based lines of ENTRY at BASE: 63 (S692, sabot), 74 (S665, heel origin), 75 (S666,
earliest heel evidence), 93 (S687, talaria). One leg per mechanical clause, each printed PASS or FAIL:
  SET      ENTRY has as many lines as at BASE, and the lines that differ from BASE are exactly
           63, 74, 75 and 93 (every other line byte-identical; each of the four changed). Revision 1
           (MutCounterD): the entry is read as bytes split on LF, so a CR added to any line counts
  ONEID    each of the four lines is a bullet line (`- `) carrying exactly one distinct S-id
  NOMARK   none of the four lines carries a defect mark instead of a repair: `to-verify`, `overstat`,
           `unsupported`, `not supported`, `defect`, `[` or `]` (case-insensitive). Revision 1
           (CtlDMarkOnly met revision 0 with HTML comments and parentheticals that kept every original
           assertion): each line must be `- <clause> (S###)`; the clause may carry no HTML comment and
           none of ( ) [ ] { } < > † ‡ *; OPEN, HEDGE, CAPTION, LINK, COPY and KEEP read the clause only
  OPEN     line 63 cites S692 and keeps the source's open list: it matches
           `belgium,?\s+(etc\b|and elsewhere|and other|among other)` (case-insensitive) and does not
           contain `france, and belgium`
  HEDGE    line 75 cites S666 and keeps the source's hedge: it matches
           `\bwe have\b|\bbbc\b|\bthe (article|programme|program) (names|cites|gives|reports)\b`
           (case-insensitive) and does not contain `evidence of someone wearing heels comes from`
  CAPTION  line 74 either cites S665 and names the caption (`\bcaption\b`, case-insensitive), or
           cites a NEW-block id (S693-S699)
  SOLE     line 93 cites one NEW-block id (S693-S699), not S687, whose row tier is A or B and whose
           anchor quote (normalised) contains `talaria` or `hermes`; revision 1 (CtlDOffTopicRow met
           revision 0 with the Hermes spaceplane): the quote must also pass round 61's footwear TOPIC
           rule (a strong footwear word, or a weak one backed by a second lexicon or context word)
  ROWS     the NEW-block ids the entry cites and the NEW-block rows in corpus/SOURCES.md are the same
           non-empty set; each such row splits on `|` into 13 cells (11 columns), status `mined`, opened `2026-10-23`, ENTRY as a
           whole used-by item, and a source cell listing at least one http(s) URL that is not a
           Wayback URL followed by at least one `web.archive.org/web/` capture URL (the archived-copy
           fallback of QUALITY criterion 13, frozen before data). Revision 1 (CriticFetchRule): the
           capture must be among the first four URLs (the locator's budget) and must be a capture of
           the SAME page: the URL after `/web/<14-digit timestamp><flags>/` equals one of the row's
           live URLs under FRESH's normalisation, with a timestamp not in the future (CtlDCaptureShapes met
           revision 0 with different-page, bare `/web/` and future-dated captures)
  APPEND   corpus/SOURCES.md at BASE, with S687's row allowed to differ only in its last (used-by)
           cell, is an in-order subsequence of the file now (no base line deleted or edited), and
           every inserted `| S### |` row is a NEW-block row (revision 1: an inserted line whose first
           cell starts with `S` but is not `S###`, e.g. `| S650b |`, fails too)
  LINK     each of the four lines restates its cited row's anchor quote (first double-quoted span of
           the anchor cell): content words (normalised, 4+ characters, outside STOP, not digits) >= 5,
           >= 3 distinct of them in the quote, and >= max(4, ceil(0.4 x content)) in quote order (LCS)
  COPY     none of the four lines repeats more than 12 consecutive normalised words of its quote
  KEEP     (revision 1) each of lines 63, 74 and 75 keeps at least 60% of the distinct content words
           of the same line at BASE (same normalisation as LINK): the repair edits the claim in place
           rather than replacing it with token salad (CtlDJunkTokens met revision 0's line legs with
           five-content-word junk carrying the OPEN/HEDGE/CAPTION tokens)
  FRESH    (revision 1) no NEW-block row names a source URL that a BASE registry row also names
           (URLs compared lower-cased, without scheme, `www.`/`m.`, query, fragment and trailing `/`,
           Wayback prefix removed). CtlDRegistryEdits met revision 0 with a full PASS: a new tier-A
           row reusing S688's live URL with a located heading quote
  LOCATE   every NEW-block row the entry cites is LOCATED by the base locator
           reports/round-61/reopen-quote.py (`locate(urls, quote)`, unchanged: at most the first four
           source-cell URLs, three attempts per URL on 429/5xx, refusals for search, echo, code,
           private or self-named hosts). Bounded retry: up to PASSES=3 passes per row, GAP=60 s apart;
           a row is located when any pass locates it and NOT_LOCATED only when all three passes fail.
           No allowance beyond this: an unreachable row after three passes fails the leg.
           Revision 1 (CriticFetchRule): the pass loop is the function locate_row(); its paired
           recovery/exhaustion control is reports/round-62/locate-control.py (stubbed fetch, virtual
           clock), run before data with its receipt committed
  ACCESS   python3 -B tools/check-source-access.py exits 0 (QUALITY criterion 10)
  LINT     python3 -B tools/check-cited-lines.py ENTRY exits 0 (QUALITY criterion 15)
Frozen predicate (the same sentence in reports/round-62/claims.json and in every receipt):
  ACCEPT-D-62: every leg above prints PASS.
Exit 0 only when every leg passes; 1 when any leg fails; 2 on unreadable input.
Review-only (no leg): whether each repaired line's wording is carried by its page beyond the shared
words; whether the new row's quote is page body text (not a caption).
"""
import argparse
import importlib.util
import math
import os
import re
import subprocess
import sys
import time
import unicodedata
from datetime import datetime, timezone

BASE = "d42ffb890a54c8431fa891380b6c38bb608b8362"
ENTRY = "corpus/knowledge/culture-material/footwear-codes-terminology.md"
REG = "corpus/SOURCES.md"
LOCATOR = "reports/round-61/reopen-quote.py"
LINES = {63: "S692", 74: "S665", 75: "S666", 93: "S687"}
NEW = range(693, 700)
OPENED = "2026-10-23"
PASSES = 3
GAP = 60
COPY_MAX = 12
CONTENT_MIN = 5
LINK_MIN = 3
ORDER_MIN = 4
ORDER_SHARE = 0.4
KEEP_SHARE = 0.6
SID = re.compile(r"\bS\d{3,}\b")
SPACED = re.compile(r"\bS\s+(\d{3,})\b")
ROWID = re.compile(r"^\|\s*(S\d{3,})\s*\|")
MARKS = ("to-verify", "overstat", "unsupported", "not supported", "defect", "[", "]")
OPEN_RE = re.compile(r"belgium,?\s+(etc\b|and elsewhere|and other|among other)", re.I)
HEDGE_RE = re.compile(r"\bwe have\b|\bbbc\b|\bthe (article|programme|program) (names|cites|gives|reports)\b", re.I)
# revision 1 (CtlDOffTopicRow met revision 0 with a located Hermes-spaceplane row): the round-61 footwear
# lexicon of reports/round-61/accept-c.py, copied unchanged
TOPIC_WORDS = frozenset("""
shoe shoes shod unshod barefoot footwear sandal sandals boot boots clog clogs moccasin moccasins
slipper slippers heel heels sole soles insole insoles geta zori zōri waraji tabi chopine chopines
poulaine poulaines patten pattens sabot sabots lapti opanak opanci caliga caligae kamik kamiks kamiit
mukluk mukluks paduka padukas shoemaker shoemakers shoemaking cordwainer cordwainers cobbler cobblers
footgear brogue brogues buskin buskins talaria
""".split())
WEAK = frozenset("boot boots sole soles slipper slippers tabi".split())
CONTEXT = frozenset("wear wears wore worn wearing wearer foot feet leather pair pairs walk walking".split())
STOP = frozenset("""
that this with from were which have been their they them there these those what when where while
into onto upon than then also only such some more most other over under about after before during
between because could would should shall will your yours ours here very much many each every both
either neither same like just even ever made make makes been being does done have having
""".split())


def cited_ids(line):
    folded = unicodedata.normalize("NFKC", line)
    return set(SID.findall(folded)) | {"S" + d for d in SPACED.findall(folded)}


def on_topic(words):
    """round-61 TOPIC rule: a strong footwear word, or a weak one backed by a second lexicon or context word."""
    hits = words & TOPIC_WORDS
    return bool(hits - WEAK) or (bool(hits) and (len(hits) >= 2 or bool(words & CONTEXT)))


def new_id(sid):
    return sid.startswith("S") and sid[1:].isdigit() and int(sid[1:]) in NEW


def longest_run(a, b):
    best, prev = 0, [0] * (len(b) + 1)
    for x in a:
        cur = [0] * (len(b) + 1)
        for j, y in enumerate(b, 1):
            if x == y:
                cur[j] = prev[j - 1] + 1
                best = max(best, cur[j])
        prev = cur
    return best


def lcs(a, b):
    prev = [0] * (len(b) + 1)
    for x in a:
        cur = [0]
        for j, y in enumerate(b, 1):
            cur.append(prev[j - 1] + 1 if x == y else max(prev[j], cur[j - 1]))
        prev = cur
    return prev[-1]


def url_key(url):
    """FRESH normalisation: Wayback prefix removed, scheme, www./m., query, fragment, trailing / dropped."""
    url = re.sub(r"^https?://web\.archive\.org/web/\d{14}[a-z_]*/", "", url.strip(), flags=re.I)
    url = re.sub(r"^[a-z]+://", "", url.lower())
    url = url.split("#", 1)[0].split("?", 1)[0]
    url = re.sub(r"^(www\.|m\.)", "", url)
    return url.rstrip("/")


def locate_row(locator, urls, quote, passes=PASSES, gap=GAP, sleep=time.sleep):
    """Bounded retry over the base locator: up to `passes` passes, `gap` seconds apart."""
    ok, why = False, "not-run"
    for p in range(1, passes + 1):
        ok, why = locator.locate(urls, quote)
        if ok:
            return True, why, p
        if p < passes:
            sleep(gap)
    return False, why, passes


def content_words(locator, text):
    words = locator.normalise(SID.sub(" ", unicodedata.normalize("NFKC", text))).split()
    return [w for w in words if len(w) >= 4 and w not in STOP and not w.isdigit()]


def run(root, argv):
    try:
        return subprocess.run(argv, cwd=root, capture_output=True, text=True, timeout=600)
    except (OSError, subprocess.TimeoutExpired) as error:
        print(f"ACCEPT_D_INPUT_ERROR {' '.join(argv)} {error}", file=sys.stderr)
        return None


def rows_of(text):
    out = {}
    for line in text.splitlines():
        m = ROWID.match(line)
        if m:
            out.setdefault(m.group(1), []).append(line)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    root = os.path.abspath(ap.parse_args().root)
    try:
        base_entry = subprocess.run(["git", "-C", root, "show", f"{BASE}:{ENTRY}"], capture_output=True,
                                    check=True).stdout.decode("utf-8").split("\n")
        base_reg = subprocess.run(["git", "-C", root, "show", f"{BASE}:{REG}"], capture_output=True,
                                  check=True).stdout.decode("utf-8").split("\n")
        entry = open(os.path.join(root, ENTRY), "rb").read().decode("utf-8").split("\n")  # rev 1: bytes, no newline translation
        reg_text = open(os.path.join(root, REG), "rb").read().decode("utf-8")
        spec = importlib.util.spec_from_file_location("reopen_quote", os.path.join(root, LOCATOR))
        locator = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(locator)
    except (OSError, UnicodeDecodeError, subprocess.CalledProcessError, ImportError, SyntaxError) as error:
        print(f"ACCEPT_D_INPUT_ERROR {error}", file=sys.stderr)
        return 2
    reg = reg_text.split("\n")
    rows = rows_of(reg_text)
    legs = []

    def leg(name, ok, detail):
        legs.append(ok)
        print(f"{name} {'PASS' if ok else 'FAIL'} {detail}")

    def line(n):
        return entry[n - 1] if 0 < n <= len(entry) else ""

    differ = [i + 1 for i in range(min(len(entry), len(base_entry))) if entry[i] != base_entry[i]]
    leg("SET", len(entry) == len(base_entry) and differ == sorted(LINES),
        f"lines={len(entry)} base={len(base_entry)} differ={differ[:20]}")

    ids = {n: cited_ids(line(n)) for n in LINES}
    leg("ONEID", all(re.match(r"^\s*- ", line(n)) and len(ids[n]) == 1 for n in LINES),
        " ".join(f"{n}:{sorted(ids[n])}" for n in sorted(LINES)))

    def clause(n):
        """Revision 1 (CtlDMarkOnly): the asserted clause, i.e. the bullet text before its final `(S###)`,
        with HTML comments removed; None when the line is not `- <clause> (S###)`."""
        text = re.sub(r"<!--.*?-->", " ", line(n))
        m = re.match(r"^\s*- (.+?)\s*\(\s*S\d{3,}\s*\)\s*$", text)
        return " ".join(m.group(1).split()) if m else None

    marked = [n for n in LINES if clause(n) is None or "<!--" in line(n)
              or any(ch in clause(n) for ch in "()[]{}<>†‡*")
              or any(m in clause(n).casefold() for m in MARKS)]
    leg("NOMARK", not marked, f"marked={marked}")

    l63 = clause(63) or ""
    leg("OPEN", ids[63] == {"S692"} and bool(OPEN_RE.search(l63)) and "france, and belgium" not in l63.casefold(),
        f"ids={sorted(ids[63])}")
    l75 = clause(75) or ""
    leg("HEDGE", ids[75] == {"S666"} and bool(HEDGE_RE.search(l75))
        and "evidence of someone wearing heels comes from" not in l75.casefold(), f"ids={sorted(ids[75])}")
    l74 = clause(74) or ""
    leg("CAPTION", (ids[74] == {"S665"} and bool(re.search(r"\bcaption\b", l74, re.I)))
        or (len(ids[74]) == 1 and new_id(next(iter(ids[74])))), f"ids={sorted(ids[74])}")

    def cells(sid):
        found = rows.get(sid, [])
        return found[0].split("|") if len(found) == 1 else None

    def quote_of(sid):
        c = cells(sid)
        if not c or len(c) < 8:
            return ""
        m = locator.QUOTE.search(c[6])
        return (m.group(1) or m.group(2)) if m else ""

    s93 = next(iter(ids[93])) if len(ids[93]) == 1 else ""
    c93 = cells(s93) if s93 else None
    leg("SOLE", bool(s93) and new_id(s93) and c93 is not None and len(c93) == 13
        and c93[4].strip() in ("A", "B") and re.search(r"\b(talaria|hermes)\b", locator.normalise(quote_of(s93))) is not None
        and on_topic(set(locator.normalise(quote_of(s93)).split())),
        f"id={s93 or '-'} tier={c93[4].strip() if c93 and len(c93) > 4 else '-'}")

    cited_new = {s for line_text in entry for s in cited_ids(line_text) if new_id(s)}
    reg_new = {s for s in rows if new_id(s)}
    bad = []
    for sid in sorted(reg_new | cited_new):
        c = cells(sid)
        if c is None or len(c) != 13:
            bad.append(f"{sid}:cells")
            continue
        urls = [locator.trim(u) for u in locator.URL.findall(c[2])]
        live = [i for i, u in enumerate(urls) if "web.archive.org/" not in u]
        wb = [i for i, u in enumerate(urls) if re.search(r"web\.archive\.org/web/", u)]
        used = [u.strip() for u in re.split(r"[,;]", c[11])]
        if c[8].strip() != "mined":
            bad.append(f"{sid}:status")
        if c[9].strip() != OPENED:
            bad.append(f"{sid}:opened")
        if ENTRY not in used:
            bad.append(f"{sid}:used-by")
        live_keys = {url_key(urls[i]) for i in live}
        if not live or not wb or min(wb) < min(live) or min(wb) > 3 or \
                not any(url_key(urls[i]) in live_keys and re.search(r"web\.archive\.org/web/\d{14}[a-z_]*/https?://", urls[i])
                        and re.search(r"/web/(\d{14})", urls[i]).group(1) <= datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")
                        for i in wb if i <= 3):
            bad.append(f"{sid}:urls")
    leg("ROWS", bool(cited_new) and cited_new == reg_new and not bad,
        f"cited={sorted(cited_new)} registry={sorted(reg_new)} bad={bad}")

    want = []
    for text in base_reg:
        m = ROWID.match(text)
        want.append((text, m.group(1) if m else ""))
    j, missing, inserted = 0, [], []
    for text in reg:
        if j < len(want):
            base_text, sid = want[j]
            if text == base_text or (sid == "S687" and text.split("|")[:-2] == base_text.split("|")[:-2]
                                     and text.split("|")[-1] == base_text.split("|")[-1]):
                j += 1
                continue
        m = ROWID.match(text)
        if m:
            inserted.append(m.group(1))
        elif re.match(r"^\s*\|\s*S", text):  # revision 1 (CtlDRegistryEdits: `| S650b |` passed)
            inserted.append("malformed:" + text.split("|")[1].strip()[:12])
    missing = [w[1] or w[0][:40] for w in want[j:]]
    leg("APPEND", not missing and all(new_id(s) for s in inserted),
        f"base_lines={len(want)} matched={j} missing={missing[:5]} inserted_rows={inserted}")

    link_bad, copy_bad = [], []
    for n in sorted(LINES):
        if len(ids[n]) != 1:
            link_bad.append(f"{n}:ids")
            copy_bad.append(f"{n}:ids")
            continue
        q = locator.normalise(quote_of(next(iter(ids[n])))).split()
        words = locator.normalise(unicodedata.normalize("NFKC", clause(n) or "")).split()
        content = [w for w in words if len(w) >= 4 and w not in STOP and not w.isdigit()]
        shared = {w for w in content if w in q}
        need = max(ORDER_MIN, math.ceil(ORDER_SHARE * len(content)))
        if not q or len(content) < CONTENT_MIN or len(shared) < LINK_MIN or lcs(content, q) < need:
            link_bad.append(f"{n}:content={len(content)} shared={len(shared)} order={lcs(content, q) if q else 0}/{need}")
        if not q or longest_run(words, q) > COPY_MAX:
            copy_bad.append(f"{n}:run={longest_run(words, q) if q else '-'}")
    leg("LINK", not link_bad, f"bad={link_bad}")
    leg("COPY", not copy_bad, f"bad={copy_bad}")
    keep_bad = []
    for n in (63, 74, 75):
        before = set(content_words(locator, base_entry[n - 1]))
        after = set(content_words(locator, clause(n) or ""))
        kept = len(before & after)
        if not before or kept < math.ceil(KEEP_SHARE * len(before)):
            keep_bad.append(f"{n}:kept={kept}/{len(before)}")
    leg("KEEP", not keep_bad, f"bad={keep_bad}")
    base_keys = set()
    for text in base_reg:
        m = ROWID.match(text)
        if m:
            base_keys |= {url_key(locator.trim(u)) for u in locator.URL.findall(text.split("|")[2])}
    reused = []
    for sid in sorted(reg_new | cited_new):
        c = cells(sid)
        if c is None or len(c) != 13:
            continue
        reused += [f"{sid}:{u}" for u in locator.URL.findall(c[2]) if url_key(locator.trim(u)) in base_keys]
    leg("FRESH", not reused, f"reused={reused[:5]}")

    detail, located = [], 0
    for sid in sorted(cited_new):
        c = cells(sid)
        if c is None or len(c) != 13:
            detail.append(f"{sid}: no row")
            continue
        urls = [locator.trim(u) for u in locator.URL.findall(c[2])]
        ok, why, _ = locate_row(locator, urls, quote_of(sid))
        if ok:
            located += 1
        else:
            detail.append(f"{sid}: {why} (passes={PASSES})")
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ")
    leg("LOCATE", bool(cited_new) and located == len(cited_new),
        f"located={located} cited={len(cited_new)} at={stamp} not_located={detail}")

    acc = run(root, [sys.executable, "-B", "tools/check-source-access.py"])
    leg("ACCESS", acc is not None and acc.returncode == 0, f"exit={acc.returncode if acc else 'error'}")
    lint = run(root, [sys.executable, "-B", "tools/check-cited-lines.py", ENTRY])
    leg("LINT", lint is not None and lint.returncode == 0,
        f"exit={lint.returncode if lint else 'error'} {(lint.stdout.strip().splitlines() or [''])[-1] if lint else ''}")

    verdict = all(legs)
    print(f"ACCEPT-D-62: {'PASS' if verdict else 'FAIL'}")
    return 0 if verdict else 1


if __name__ == "__main__":
    sys.exit(main())
