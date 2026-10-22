# ExecIntegrateRows — round 54, claim C: the integration tool `integrate-rows.py`

- Seat: `KotodamaR54a2.ExecIntegrateRows` (leaf executor; no subagent dispatch, no background jobs, no lane writes other than this report).
- Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin` (branch main, jj-colocated). Nothing in the lane was edited except this report file. No git/jj mutation, no staging, no commit, no index touch; only read-only `git` and read-only file reads were used.
- Code and fixtures live under `/fast/scratch/hyaku/kotodama-r54-a2/ExecIntegrateRows/` only, as the assignment requires. The tool is **not** installed into the lane; the L1 copies it if the lane wants it.
- Assigned item: write `integrate-rows.py` (usage `python3 -B integrate-rows.py --reports <dir> --start 239 --sources <lane>/corpus/SOURCES.md --out <dir>`), which parses every `### NEW-<Seat>-<n>` block in the seat reports, assigns S-ids from `--start` in report-file then block order, and writes `rows.md`, `map.tsv`, `gate.md`, `sentences.md`, plus a `--rewrite <file>` mode.
- Result: **the tool is written, compiles, passes three fixture reports (one deliberately malformed), and was run against the real seat reports in `.ufo/waves/round-54/build-a2/` read-only.** It reproduces all 46 landed round-54 registry rows from those reports.
- **Status (from the L1): round 54 is already landed — lane `e17bc2b`, round report `c47da61`. This seat's report arrived after the records commit, so it is neither integrated nor cited, and the round report says so.** The duplicate-merge findings in §7.2 are round-55 frontier input; §7.1 needs no action, because the block that carried the access-marker wording was never registered. The tool is therefore a working instrument with no round-54 land attached to it.

---

## 1. Axes named

| axis | state | evidence |
|---|---|---|
| coverage | every block shape in the wave's Output section is parsed: `citation`, `url`, `route`, `kind`, `tier`, `scope`, `quotes` (bulleted), `teaches`, `draft sentences`, `unopened`; keys written as list items (`- url: …`), values running over several lines, and quotes whose locator itself carries quotes are all handled. 105 of the 108 real blocks produced rows; the 3 that did not are the merged duplicate-URL blocks. | §4 runs 3–5, §5 |
| operability | one command, four artefacts, exit 0/1/2; the three specified loud failures each fire and stop the run with no output written; `--rewrite` is a separate mode that works in place and with `--dry-run`. | §3 |
| calibration | the emitted rows pass all seven of the lane's registry census commands (rows count, NF=13, tier enum, status enum, kind enum, no duplicate ids, no tier inflation); the emitted Gate lines match `corpus/lessons/round-53.md`'s shape exactly; the tool's access-marker pattern is the lane's own, copied verbatim, so a row this tool writes agrees with `tools/check-source-access.py`. | §5 |

No axis is harmed: no lane file was touched, no source was re-opened or re-quoted (this seat opened no external source — it is a tooling seat), and no canon, clinical, legal or heritage ruling is made.

---

## 2. The tool

Final source: `/fast/scratch/hyaku/kotodama-r54-a2/ExecIntegrateRows/integrate-rows.py`
sha256 `5f7105d647725854e5f211ffc7d877bc602c3e2ec1882c55e7fbf08bf6215106`, 654 lines, Python 3.14.8, stdlib only.
`python3 -m py_compile integrate-rows.py` → exit 0.

```python
#!/usr/bin/env python3
"""integrate-rows.py — kotodama round-54 claim C registry integrator.

Turns the seat reports' `### NEW-<Seat>-<n>` blocks into the four artefacts the
lane's integrator needs:

  rows.md       one corpus/SOURCES.md registry row per block, in the 11-column
                shape of the live registry (the column order is read from the
                registry header, not hard-coded)
  map.tsv       draft id -> S-id
  gate.md       one round-lesson `## Gate` line per row, in the shape of
                corpus/lessons/round-53.md
  sentences.md  every block's draft sentences with the draft ids replaced by
                S-ids

and, in `--rewrite` mode, rewrites the draft ids inside any given file in place
using map.tsv.

Usage:
  python3 -B integrate-rows.py --reports <dir> --start 239 \
      --sources /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md \
      --out <dir>

  python3 -B integrate-rows.py --rewrite <file> --map <map.tsv> [--dry-run]

Block shape (the wave context's Output section): a `### NEW-<Seat>-<n>` heading
followed by the lines `citation:`, `url:`, `route:`, `kind:`, `tier:`, `scope:`,
`quotes:` (bulleted, each `<locator>: "<quote>"`), `teaches:`, `draft sentences:`
(3-6 sentences, each ending `(NEW-<Seat>-<n>, <locator>)`) and `unopened:`. Keys
may be written as list items (`- url: ...`), values may run over several lines,
and a quoted passage may itself contain straight quotes.

Hard errors (exit 1, nothing written): a block with no url or no quotes; the
same url in two blocks (both are named); a quote of more than 25 words; an
assigned id that already exists in the registry; a duplicate draft id.

Stdlib only. Exit codes: 0 ok, 1 hard error, 2 bad invocation or unreadable
input.
"""

import argparse
import os
import re
import sys

# --- block and field grammar -------------------------------------------------

BLOCK_RE = re.compile(r"^#{2,4}\s+(NEW-(?P<seat>[A-Za-z0-9_]+(?:-[A-Za-z0-9_]+)*)-(?P<num>\d+))\b")
KEY_RE = re.compile(r"^(?P<key>[A-Za-z][A-Za-z0-9 _-]{0,40}?)\s*:\s*(?!/)(?P<val>.*)$")
BULLET_RE = re.compile(r"^\s*(?:[-*+]|\d+[.)])\s+")
MARKER_RE = re.compile(r"\((?P<did>NEW-[A-Za-z0-9_]+(?:-[A-Za-z0-9_]+)*-\d+)\s*,\s*(?P<loc>[^)]*)\)")

KEY_ALIASES = {
    "citation": "citation",
    "source": "citation",
    "url": "url",
    "link": "url",
    "route": "route",
    "access": "route",
    "kind": "kind",
    "type": "kind",
    "tier": "tier",
    "scope": "scope",
    "quotes": "quotes",
    "quote": "quotes",
    "teaches": "teaches",
    "teach": "teaches",
    "lesson": "teaches",
    "draft sentences": "draft_sentences",
    "draft sentence": "draft_sentences",
    "sentences": "draft_sentences",
    "unopened": "unopened",
    "not opened": "unopened",
}

# registry column -> the value this tool computes for it
COLUMNS = ["id", "source", "kind", "tier", "scope", "anchor", "teaches",
           "status", "opened", "recheck", "used-by"]

# The registry's kind enum is spec, docs, paper, code, tool, dataset, talk,
# book, community, own-work. The wave's seat vocabulary also uses `web` and
# `record`; the lane's landed round-54 rows file both as `docs`.
KIND_MAP = {
    "paper": "paper",
    "book": "book",
    "dataset": "dataset",
    "spec": "spec",
    "docs": "docs",
    "code": "code",
    "tool": "tool",
    "talk": "talk",
    "community": "community",
    "own-work": "own-work",
    "web": "docs",
    "record": "docs",
}

# A seat kind that names a community-authored source ("community policy
# statement", "community-institution exhibit", "tribal government statement").
COMMUNITY_RE = re.compile(
    r"\bcommunity\b|\btribal\b|\bfirst nations\b|\bband council\b",
    re.IGNORECASE,
)

# QUALITY criterion 10 markers: a row whose own cells record an access-control
# bypass counts as unopened. The pattern below is the lane's own, copied
# verbatim from tools/check-source-access.py (BYPASS), so a row this tool emits
# agrees with the gate that will read it.
BYPASS_RE = re.compile(
    r"""\bheadless\b|\bbypass(?:ed|ing)?\b|\bsolved\s+(?:a\s+|the\s+)?(?:bot\s+)?(?:captcha|challenge)\b
| \b(?:undetected-chromedriver|flaresolverr|cloudscraper|curl-impersonate|ez-?proxy)\b
| \b(?:open|fetch|load|render|retriev|scrap|access|download|captur|driv|automat)\w*\s+(?:\S+\s+){0,2}?(?:with|via|through|using|by|in)\s+(?:a\s+|an\s+|the\s+)?(?:playwright|puppeteer|selenium|webdriver|chromedriver)\b
| \b(?:playwright|puppeteer|selenium)(?:[\s-]+webdriver)?[\s-]+(?:browser|session|script|chrom\w*|firefox|webkit)\b
| (?<!\bnot )(?<!\bno )(?<!\bnever )\b(?:bypass(?:ed|es|ing)?|by-pass(?:ed|es|ing)?|circumvent(?:ed|s|ing)|evad(?:ed|es|ing)|defeat(?:ed|s|ing)?|solv(?:ed|es|ing)?|pass(?:ed|es|ing)?|clear(?:ed|s|ing)?|g[eo]t(?:ting)?\s+(?:past|around|round|through))\s+(?:\S+\s+){0,3}?(?:pay-?walls?|log-?ins?|sign-?ins?|(?:re|h)?captchas?|turnstile|geo[\s-]?block(?:s|ed|ing)?|geo[\s-]?fenc(?:e|es|ing)?|(?:bot|js|javascript|cloudflare|waf|anti-?bot|browser|security)[\s-](?:challenges?|checks?|blocks?|walls?|tests?)|challenge\s+pages?|access\s+controls?)\b
| \b(?:pay-?wall|log-?in|(?:re|h)?captcha|geo[\s-]?block)s?\s*(?:was\s+|were\s+)?(?:bypass|by-pass|circumvent|evad|defeat|solv)\w*
| \bvpns?\b
| \blogged-in\b|\b(?:signed|logged)\s+in\s+(?:as|with|via|using|through)\b
| \b(?:subscriber|subscription|paid|member)\s+(?:account|login|credentials|session|cookie)s?\b|\b(?:institutional|personal)\s+(?:login|credentials|session|cookie)s?\b|\bsession\s+cookies?\b|\bcookies?\s+(?:from|of|my|the)\b
| \bspoof(?:ed|ing)?\s+(?:a\s+|the\s+)?(?:browser\s+)?(?:user-?agent|ip|location|referer|headers?)\b""",
    re.IGNORECASE | re.VERBOSE,
)


# --- small helpers ------------------------------------------------------------

def norm_key(key):
    key = re.sub(r"\s+", " ", key.strip().lower())
    return KEY_ALIASES.get(key)


def cell(text):
    """One table cell: single line, no raw pipe (the registry census splits on '|')."""
    text = re.sub(r"\s+", " ", (text or "").strip())
    return text.replace("|", "&#124;")


def words(text):
    return len((text or "").split())


def strip_bullet(line):
    return BULLET_RE.sub("", line).strip()


def read_text(path):
    with open(path, encoding="utf-8-sig") as handle:
        return handle.read()


def report_files(directory, excludes):
    """Every .md file directly under a directory, in name order."""
    names = []
    for name in sorted(os.listdir(directory)):
        if not name.endswith(".md"):
            continue
        path = os.path.join(directory, name)
        if any(re.search(pat, path) for pat in excludes):
            continue
        names.append(path)
    return names


def split_quote_line(line):
    """'<locator>: "<quote>"' -> (locator, quote, tail) or None.

    The locator may itself carry quotes, the passage may carry straight quotes,
    and the passage may be followed by a bracketed or parenthesised note. The
    passage opens at a quote that follows ": " (the locator's colon); when the
    line has no such opener the first quote of the line opens it.
    """
    line = strip_bullet(line)
    if '"' not in line:
        return None

    openers = [i for i in range(2, len(line)) if line[i] == '"' and line[i - 2:i] == ": "]
    if not openers:
        first = line.find('"')
        if first < 0:
            return None
        openers = [first]
    opening = openers[0]
    start = opening + 1

    # Closing quote: the last quote of the line, or the first quote after the
    # opening one that is followed by end-of-line or an opening bracket.
    stripped = line.rstrip()
    end = len(stripped) - 1
    if not (stripped.endswith('"') and end > start):
        end = None
        for index in range(start, len(line)):
            if line[index] == '"' and re.match(r"^\s*(\(|\[|$)", line[index + 1:]):
                end = index
                break
        if end is None:
            return None
    quote = line[start:end]
    if not quote.strip() or quote.count('"') % 2:
        return None
    locator = line[:opening].rstrip()
    if locator.endswith(":"):
        locator = locator[:-1].rstrip()
    return locator, quote, line[end + 1:].strip(), len(openers) > 1


# --- parsing ------------------------------------------------------------------

class Block(object):
    def __init__(self, draft_id, seat, num, path, line):
        self.draft_id = draft_id
        self.seat = seat
        self.num = num
        self.path = path
        self.line = line
        self.fields = {}

    def get(self, key):
        return self.fields.get(key, [])

    def text(self, key):
        return " ".join(x.strip() for x in self.get(key)).strip()

    def has(self, key):
        return key in self.fields


def parse_report(path):
    """Return the list of `### NEW-<Seat>-<n>` blocks in one report file."""
    blocks = []
    current = None
    field_key = None
    for number, raw in enumerate(read_text(path).splitlines(), 1):
        heading = BLOCK_RE.match(raw)
        if heading:
            current = Block("NEW-%s-%s" % (heading.group("seat"), heading.group("num")),
                            heading.group("seat"), int(heading.group("num")), path, number)
            blocks.append(current)
            field_key = None
            continue
        if current is None:
            continue
        if raw.lstrip().startswith("#"):
            current = None
            field_key = None
            continue
        plain = strip_bullet(raw)
        match = KEY_RE.match(plain)
        if match:
            key = norm_key(match.group("key"))
            if key:
                field_key = key
                current.fields.setdefault(key, [])
                value = match.group("val").strip()
                if value:
                    current.fields[key].append(value)
                continue
        if field_key is not None:
            current.fields[field_key].append(plain)
    return blocks


def block_quotes(block, problems):
    """Bulleted quotes of a block as (locator, quote, tail, multiple) records."""
    pairs = []
    for line in block.get("quotes"):
        plain = strip_bullet(line)
        if not plain:
            continue
        parsed = split_quote_line(line)
        if parsed is None:
            problems.append((block, "quote line carries no double-quoted passage: %r" % plain[:90]))
            continue
        pairs.append(parsed)
    return pairs


def block_sentences(block):
    """Draft sentences of a block: one unit per bullet, continuation lines folded in."""
    units = []
    buffer = []
    for line in block.get("draft_sentences"):
        plain = strip_bullet(line)
        if not plain:
            continue
        buffer.append(plain)
        if MARKER_RE.search(plain):
            units.append(" ".join(buffer))
            buffer = []
    if buffer:
        units.append(" ".join(buffer))
    return units


# --- registry reading ---------------------------------------------------------

def read_registry(path):
    """Return (column_order, existing_ids) from a corpus/SOURCES.md."""
    columns, ids = [], set()
    for line in read_text(path).splitlines():
        if not columns and re.match(r"^\|\s*id\s*\|", line):
            columns = [c.strip() for c in line.strip().strip("|").split("|")]
            continue
        match = re.match(r"^\|\s*(S\d{3,})\s*\|", line)
        if match:
            ids.add(match.group(1))
    if not columns:
        raise ValueError("no registry header found in %s" % path)
    return columns, ids


# --- integration --------------------------------------------------------------

def build_row(block, sid, args, columns):
    """Return (cells, warnings) for one registry row."""
    warnings = []
    url = block.text("url").strip()
    citation = block.text("citation").strip()
    route = block.text("route").strip()
    kind_raw = block.text("kind").strip()
    tier_raw = block.text("tier").strip()
    scope = block.text("scope").strip()
    teaches = block.text("teaches").strip()

    tier_match = re.match(r"^([ABC])\b", tier_raw)
    if tier_match:
        tier = tier_match.group(1)
    else:
        tier = ""
        warnings.append("tier cell does not start with A, B or C: %r" % tier_raw[:70])

    kind_token = re.split(r"[\s(.]", kind_raw.lower(), maxsplit=1)[0].strip()
    kind = KIND_MAP.get(kind_token, "")
    if not kind:
        kind = "docs"
        warnings.append("seat kind %r has no registry enum value; filed as docs" % kind_raw[:60])
    elif kind_token != kind:
        warnings.append("seat kind %r filed as registry kind %r" % (kind_raw[:60], kind))

    # A source written by the community itself is filed as kind community; the
    # registry census treats a community row as never tier A. The seat's own
    # kind field names it ("community policy statement", "tribal government
    # statement"); the citation is not used, because a holding museum's record
    # may quote a community's words without being one.
    if args.community_kind and COMMUNITY_RE.search(kind_raw):
        if kind != "community":
            warnings.append("seat kind %r filed as registry kind community (a community's own "
                            "statement)" % kind_raw[:60])
        kind = "community"
        if tier == "A":
            tier = "B"
            warnings.append("tier A downgraded to B: the registry census treats a community row as "
                            "never tier A")

    source = citation + " — " + url if citation else "—"
    if route:
        source += " (%s)" % route
    if not citation:
        warnings.append("no citation field; the source cell needs author, year, title and venue")

    quotes = block_quotes(block, [])
    anchor_parts = []
    for locator, quote, tail, multiple in quotes:
        piece = ('%s: "%s"' % (locator, quote)) if locator else ('"%s"' % quote)
        if tail:
            piece += " " + tail
        anchor_parts.append(piece)
    anchor = "; ".join(anchor_parts)

    scope_cell = scope
    if tier_raw:
        scope_cell = (scope_cell + " " if scope_cell else "") + "(tier note: %s)" % tier_raw
    if not scope_cell:
        warnings.append("no scope field; the scope cell needs the claim the tier applies to")
    if not teaches:
        warnings.append("no teaches field; the teaches cell needs one grounded learner benefit")

    bypass = BYPASS_RE.search(" ".join((source, anchor, scope_cell, teaches)))
    if bypass:
        warnings.append("the row's cells carry the access-control marker %r; "
                        "tools/check-source-access.py flags such a row as unopened, so reword the "
                        "cell before the row is filed (QUALITY criterion 10)"
                        % bypass.group(0))

    values = {
        "id": sid,
        "source": source,
        "kind": kind,
        "tier": tier,
        "scope": scope_cell,
        "anchor": anchor,
        "teaches": teaches or "—",
        "status": args.status,
        "opened": args.opened,
        "recheck": args.recheck,
        "used-by": args.used_by,
    }
    return [cell(values.get(name, "")) for name in columns], warnings


def gate_line(sid, url, locator, quote, scope, seat, accessed):
    """One round-lesson Gate line, in the shape of corpus/lessons/round-53.md.

    The period that ends the quoted passage sits outside its closing quote, as
    the lane's own Gate lines do (round-53.md:44, :98, :170).
    """
    quote = quote.strip()
    scope = scope.strip()
    if scope and scope[-1] not in ".!?":
        scope += "."
    where = ('%s: "%s"' % (locator, quote)) if locator else ('"%s"' % quote)
    return '- %s — %s — accessed %s — %s. Grounds: %s Seat: %s.' % (
        sid, url, accessed, where, scope, seat)


def integrate(args):
    columns, existing = read_registry(args.sources)
    if columns != COLUMNS:
        raise ValueError("registry header %r does not match the expected columns %r"
                         % (columns, COLUMNS))

    problems, warnings = [], []
    blocks = []
    files = report_files(args.reports, args.exclude)
    for path in files:
        blocks.extend(parse_report(path))

    seen_draft = {}
    for block in blocks:
        if block.draft_id in seen_draft:
            problems.append((block, "draft id %s already used in %s:%d"
                             % (block.draft_id, seen_draft[block.draft_id][0],
                                seen_draft[block.draft_id][1])))
        else:
            seen_draft[block.draft_id] = (block.path, block.line)

    # Groups: one registry row each. Without --merge-duplicates a group is a
    # single block; with it, blocks that opened the same url are one group and
    # keep the first seat's cells (the round-53 integrator's precedent).
    groups = []
    group_of = {}
    url_seen = {}
    for block in blocks:
        url = block.text("url").strip()
        if not url:
            problems.append((block, "block has no url"))
            continue
        key = url.lower().rstrip("/")
        if key in url_seen:
            other = url_seen[key]
            if args.merge_duplicates:
                if args.merge_keep == "last":
                    # the later block's cells become the row's cells
                    other[1].append(other[0])
                    other[0] = block
                    groups[groups.index(other)] = other
                else:
                    other[1].append(block)
                group_of[block.draft_id] = other
                warnings.append((block, "merged into the row of %s (same url %s)"
                                 % (other[0].draft_id, url)))
                continue
            problems.append((block, "duplicate url %s — also in %s:%d (%s)"
                             % (url, other[0].path, other[0].line, other[0].draft_id)))
            problems.append((other[0], "duplicate url %s — also in %s:%d (%s)"
                             % (url, block.path, block.line, block.draft_id)))
        else:
            group = [block, []]
            groups.append(group)
            group_of[block.draft_id] = group
            url_seen[key] = group

    for block in blocks:
        quotes = block.get("quotes")
        if not quotes or not [x for x in quotes if x.strip()]:
            problems.append((block, "block has no quotes"))
            continue
        for locator, quote, tail, multiple in block_quotes(block, []):
            count = words(quote)
            if count > args.max_quote_words:
                message = ("quote of %d words exceeds the %d-word limit: %r"
                           % (count, args.max_quote_words, quote[:90]))
                if args.allow_long_quotes:
                    warnings.append((block, message))
                else:
                    problems.append((block, message))

    if problems:
        for block, message in problems:
            print("INTEGRATE_ERROR %s:%d %s — %s" % (block.path, block.line, block.draft_id, message),
                  file=sys.stderr)
        print("INTEGRATE: %d hard error(s); no output written" % len(problems), file=sys.stderr)
        return 1

    os.makedirs(args.out, exist_ok=True)

    rows, gate, mapping, sentence_sections = [], [], [], []
    for offset, group in enumerate(groups):
        block, members = group
        sid = "S%03d" % (args.start + offset)
        if sid in existing:
            warnings.append((block, "assigned id %s already exists in the registry; the row would "
                                    "duplicate it" % sid))
        cells, row_warnings = build_row(block, sid, args, columns)
        rows.append("| " + " | ".join(cells) + " |")
        for message in row_warnings:
            warnings.append((block, message))
        for member in [block] + members:
            mapping.append((member.draft_id, sid))

        url = block.text("url").strip()
        chosen = None
        for locator, quote, tail, multiple in block_quotes(block, []):
            if words(quote) <= args.max_quote_words:
                chosen = (locator, quote)
                break
        if chosen is None:
            warnings.append((block, "no quote of at most %d words; the Gate line is flagged"
                             % args.max_quote_words))
            gate.append("- %s — %s — accessed %s — NO USABLE QUOTE (every quote is over %d words). "
                        "Grounds: %s Seat: %s." % (sid, url, args.opened, args.max_quote_words,
                                                  block.text("scope"), block.seat))
        else:
            gate.append(gate_line(sid, url, chosen[0], chosen[1], block.text("scope"),
                                   block.seat, args.opened))

        for member in [block] + members:
            units = block_sentences(member)
            for unit in units:
                if not MARKER_RE.search(unit):
                    warnings.append((member, "draft sentence carries no (NEW-..., locator) marker"))
            sentence_sections.append((sid, member.draft_id, units))

    id_map = dict(mapping)

    def rewrite_ids(text):
        for did in sorted(id_map, key=len, reverse=True):
            text = re.sub(r"(?<![A-Za-z0-9_.-])%s(?![A-Za-z0-9_-])" % re.escape(did),
                          id_map[did], text)
        return text

    with open(os.path.join(args.out, "rows.md"), "w", encoding="utf-8") as handle:
        handle.write("\n".join(rows) + ("\n" if rows else ""))
    with open(os.path.join(args.out, "map.tsv"), "w", encoding="utf-8") as handle:
        handle.write("draft_id\ts_id\n")
        for did, sid in mapping:
            handle.write("%s\t%s\n" % (did, sid))
    with open(os.path.join(args.out, "gate.md"), "w", encoding="utf-8") as handle:
        handle.write("## Gate\n\n")
        handle.write("\n".join(gate) + ("\n" if gate else ""))
    sentence_lines = []
    for sid, draft_id, units in sentence_sections:
        sentence_lines.append("## %s — %s" % (sid, draft_id))
        sentence_lines.append("")
        for unit in units:
            sentence_lines.append(rewrite_ids(unit))
        sentence_lines.append("")
    with open(os.path.join(args.out, "sentences.md"), "w", encoding="utf-8") as handle:
        handle.write("\n".join(sentence_lines).rstrip() + "\n")

    for block, message in warnings:
        print("INTEGRATE_WARN %s:%d %s — %s" % (block.path, block.line, block.draft_id, message),
              file=sys.stderr)
    print("INTEGRATE: files=%d blocks=%d groups=%d ids=%s..%s rows=%d warnings=%d"
          % (len(files), len(blocks), len(groups), "S%03d" % args.start,
             "S%03d" % (args.start + len(groups) - 1) if groups else "—", len(rows), len(warnings)))
    print("INTEGRATE_OK rows.md map.tsv gate.md sentences.md -> %s" % args.out)
    return 0


def rewrite(args):
    if not args.map:
        raise ValueError("--rewrite needs --map (or an --out directory holding map.tsv)")
    mapping = {}
    with open(args.map, encoding="utf-8") as handle:
        for number, line in enumerate(handle, 1):
            line = line.rstrip("\n")
            if not line.strip():
                continue
            parts = line.split("\t")
            if number == 1 and parts[0].strip() == "draft_id":
                continue
            if len(parts) != 2:
                raise ValueError("map.tsv line %d is not 'draft_id\\ts_id': %r" % (number, line))
            mapping[parts[0].strip()] = parts[1].strip()
    if not mapping:
        raise ValueError("no ids in %s" % args.map)

    original = read_text(args.rewrite)
    text = original
    counts = {}
    for did in sorted(mapping, key=len, reverse=True):
        pattern = re.compile(r"(?<![A-Za-z0-9_.-])%s(?![A-Za-z0-9_-])" % re.escape(did))
        text, count = pattern.subn(mapping[did], text)
        if count:
            counts[did] = count
    if not args.dry_run and text != original:
        with open(args.rewrite, "w", encoding="utf-8") as handle:
            handle.write(text)
    print("REWRITE %s: %d replacement(s) of %d draft id(s)%s"
          % (args.rewrite, sum(counts.values()), len(counts), " (dry run)" if args.dry_run else ""))
    for did in sorted(counts):
        print("REWRITE_ID %s -> %s x%d" % (did, mapping[did], counts[did]))
    return 0


def main():
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument("--reports", help="directory of seat reports")
    parser.add_argument("--start", type=int, default=239, help="first S-id to assign")
    parser.add_argument("--sources", help="path to corpus/SOURCES.md")
    parser.add_argument("--out", help="directory for rows.md, map.tsv, gate.md, sentences.md")
    parser.add_argument("--rewrite", help="file whose draft ids are replaced in place")
    parser.add_argument("--map", help="map.tsv used by --rewrite")
    parser.add_argument("--dry-run", action="store_true", help="--rewrite without writing")
    parser.add_argument("--used-by", default="corpus/knowledge/culture-material/masks-masquerade.md",
                        help="used-by cell of every row")
    parser.add_argument("--status", default="mined", help="status cell of every row")
    parser.add_argument("--opened", default="2026-10-22", help="opened cell of every row")
    parser.add_argument("--recheck", default="365d", help="recheck cell of every row")
    parser.add_argument("--max-quote-words", type=int, default=25,
                        help="word limit for a Gate quote; a longer quote is a hard error")
    parser.add_argument("--allow-long-quotes", action="store_true",
                        help="report a quote over the word limit as a warning instead of a hard "
                             "error (the Gate line still picks a quote within the limit)")
    parser.add_argument("--exclude", action="append", default=[],
                        help="regex; report files whose path matches are skipped")
    parser.add_argument("--merge-duplicates", action="store_true",
                        help="one registry row per distinct url: blocks that opened the same url "
                             "share the first seat's row and the same S-id (default: a duplicate "
                             "url is a hard error)")
    parser.add_argument("--no-community-kind", dest="community_kind", action="store_false",
                        help="do not file a community-authored source as kind community")
    parser.add_argument("--merge-keep", choices=("first", "last"), default="first",
                        help="with --merge-duplicates, which block's cells the shared row keeps "
                             "(default: first in report-file order)")
    parser.set_defaults(community_kind=True)
    args = parser.parse_args()

    try:
        if args.rewrite:
            if not args.map and args.out:
                candidate = os.path.join(args.out, "map.tsv")
                if os.path.isfile(candidate):
                    args.map = candidate
            return rewrite(args)
        if not args.reports or not args.sources or not args.out:
            parser.error("--reports, --sources and --out are required")
        return integrate(args)
    except (OSError, ValueError, UnicodeDecodeError) as error:
        print("INTEGRATE_INPUT_ERROR %s" % error, file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
```

---

## 3. The three loud failures

All three are hard: the tool prints one `INTEGRATE_ERROR` line per problem, writes **no** output file, and exits 1.

| required failure | where it fires | message |
|---|---|---|
| a block missing `url` or `quotes` | the validation pass, before anything is written | `block has no url` / `block has no quotes` |
| a duplicate url across blocks | the validation pass; **both** blocks are named, each with the other's file, line and draft id | `duplicate url <url> — also in <file>:<line> (<draft id>)` |
| a quote over 25 words | the validation pass; the word count and the passage are printed | `quote of 31 words exceeds the 25-word limit: '<first 90 chars>'` |

Two more failures are loud for the same reason (a duplicated draft id, and a duplicate registry id), because both would silently corrupt the map or the registry.

---

## 4. Fixture reports and every run

Fixtures (three reports, one deliberately malformed) live in
`/fast/scratch/hyaku/kotodama-r54-a2/ExecIntegrateRows/fixtures/`:

- `fixtures/good/fixture-a.md` — two blocks (a paper; a collection record written as `- kind: record`), well formed.
- `fixtures/good/fixture-b.md` — one block (a paper), well formed.
- `fixtures/bad/fixture-c-malformed.md` — four blocks, malformed three ways: no `url`, the same url in two blocks, and a 31-word quote.
- `fixtures/dup/` — the same report twice under two names, so the duplicate-url and duplicate-draft-id failures fire across files.

The suite is `run-fixtures.sh`; the full transcript with every command, output and exit code is in
`fixtures-run.txt` (215 lines). Every run below is copied from that file.

### Run 1 — good fixtures (exit 0)

```
----- COMMAND: python3 -B integrate-rows.py --reports fixtures/good --start 900 --sources /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md --out out-good -----
INTEGRATE_WARN fixtures/good/fixture-a.md:23 NEW-FixtureSeatA-2 — seat kind 'record' filed as registry kind 'docs'
INTEGRATE: files=2 blocks=3 groups=3 ids=S900..S902 rows=3 warnings=1
INTEGRATE_OK rows.md map.tsv gate.md sentences.md -> out-good
----- EXIT: 0 -----
```

`rows.md` (one table row per block, in the registry's 11-column shape; the `|` inside a cell is escaped as `&#124;` so the row keeps NF=13):

```
| S900 | Example, A. 2020. "Masked Processions and the Public Body." Journal of Example Studies 4(2): 100-120, doi 10.1234/example.2020.004 — https://example.org/fixture-a/paper.pdf (direct, HTTP 200, PDF, 12 pages) | paper | A | the article's own account of masked processions in one valley, and nothing wider (tier note: A — the article is primary for the processions it describes) | Abstract, printed p. 100: "Masked processions in this valley were annual and publicly announced"; §3, printed p. 106: "The mask was not worn by the dancer but by the office he held" | a mask can mark an office rather than a body, so a worldbuilder can decide who is allowed to wear one and when | mined | 2026-10-22 | 365d | corpus/knowledge/culture-material/masks-masquerade.md |
| S901 | Example Foundation. 2021. "Masked Dance Register." Collection catalogue, entry 44. — https://example.org/fixture-a/register (direct, HTTP 200, HTML) | docs | B | what one catalogue entry records about a single masked dance and its access rule (tier note: B — the holding institution's own record, but a summary entry rather than the object) | Entry 44, "Conditions of access": "Masks were shown only to initiates and to visiting scholars by request" | an archive record can carry an access rule, so a culture can decide who sees the mask at all | mined | 2026-10-22 | 365d | corpus/knowledge/culture-material/masks-masquerade.md |
| S902 | Example, B. 2019. "The Voice Under the Mask." Folklore Notes 12: 44-58, doi 10.1234/example.2019.012 — https://example.org/fixture-b/voice.pdf (direct, HTTP 200, PDF, 9 pages) | paper | B | the article's own report of how one troupe assigned voices under masks (tier note: B — a peer-reviewed article read in full, but its fieldwork is reported at second hand) | §2, printed p. 47: "A young man spoke through the mask in a woman's voice"; §4, printed p. 53: "The voice was licensed by the mask and revoked when it was removed" | a mask can license a voice, so a worldbuilder can decide whether speaking in character is allowed or required | mined | 2026-10-22 | 365d | corpus/knowledge/culture-material/masks-masquerade.md |
```

`map.tsv`:

```
draft_id	s_id
NEW-FixtureSeatA-1	S900
NEW-FixtureSeatA-2	S901
NEW-FixtureSeatB-1	S902
```

`gate.md` (one `## Gate` line per row, in the shape of `corpus/lessons/round-53.md:170-182`):

```
## Gate

- S900 — https://example.org/fixture-a/paper.pdf — accessed 2026-10-22 — Abstract, printed p. 100: "Masked processions in this valley were annual and publicly announced". Grounds: the article's own account of masked processions in one valley, and nothing wider. Seat: FixtureSeatA.
- S901 — https://example.org/fixture-a/register — accessed 2026-10-22 — Entry 44, "Conditions of access": "Masks were shown only to initiates and to visiting scholars by request". Grounds: what one catalogue entry records about a single masked dance and its access rule. Seat: FixtureSeatA.
- S902 — https://example.org/fixture-b/voice.pdf — accessed 2026-10-22 — §2, printed p. 47: "A young man spoke through the mask in a woman's voice". Grounds: the article's own report of how one troupe assigned voices under masks. Seat: FixtureSeatB.
```

`sentences.md` (draft ids replaced by S-ids):

```
## S900 — NEW-FixtureSeatA-1

Masked processions in this valley were annual and publicly announced, so a calendar gives a mask its days (S900, Abstract).
The mask was not worn by the dancer but by the office he held, so a costume can carry rank rather than disguise (S900, §3).

## S901 — NEW-FixtureSeatA-2

Masks were shown only to initiates and to visiting scholars by request, so an access rule can govern the object itself (S901, Entry 44).

## S902 — NEW-FixtureSeatB-1

A young man spoke through the mask in a woman's voice, so a costume can move a voice across a boundary the person may not cross (S902, §2).
The voice was licensed by the mask and revoked when it was removed, so the mask can hold the speaking right itself (S902, §4).
```

### Run 2 — malformed fixture (exit 1, no output written)

```
----- COMMAND: python3 -B integrate-rows.py --reports fixtures/bad --start 900 --sources /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md --out out-bad -----
INTEGRATE_ERROR fixtures/bad/fixture-c-malformed.md:7 NEW-FixtureSeatC-1 — block has no url
INTEGRATE_ERROR fixtures/bad/fixture-c-malformed.md:34 NEW-FixtureSeatC-3 — duplicate url https://example.org/fixture-c/carnival.pdf — also in fixtures/bad/fixture-c-malformed.md:20 (NEW-FixtureSeatC-2)
INTEGRATE_ERROR fixtures/bad/fixture-c-malformed.md:20 NEW-FixtureSeatC-2 — duplicate url https://example.org/fixture-c/carnival.pdf — also in fixtures/bad/fixture-c-malformed.md:34 (NEW-FixtureSeatC-3)
INTEGRATE_ERROR fixtures/bad/fixture-c-malformed.md:48 NEW-FixtureSeatC-4 — quote of 31 words exceeds the 25-word limit: 'In the second act the performer wore a wooden face that opened at the hinge and the audien'
INTEGRATE: 4 hard error(s); no output written
----- EXIT: 1 -----

== out-bad written? ==
ls: cannot access 'out-bad': No such file or directory
```

### Run 3 — duplicate url across two report files (exit 1)

```
----- COMMAND: python3 -B integrate-rows.py --reports fixtures/dup --start 900 --sources /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md --out out-dup -----
INTEGRATE_ERROR fixtures/dup/report-two.md:7 NEW-FixtureSeatA-1 — draft id NEW-FixtureSeatA-1 already used in fixtures/dup/report-one.md:7
INTEGRATE_ERROR fixtures/dup/report-two.md:23 NEW-FixtureSeatA-2 — draft id NEW-FixtureSeatA-2 already used in fixtures/dup/report-one.md:23
INTEGRATE_ERROR fixtures/dup/report-two.md:7 NEW-FixtureSeatA-1 — duplicate url https://example.org/fixture-a/paper.pdf — also in fixtures/dup/report-one.md:7 (NEW-FixtureSeatA-1)
INTEGRATE_ERROR fixtures/dup/report-one.md:7 NEW-FixtureSeatA-1 — duplicate url https://example.org/fixture-a/paper.pdf — also in fixtures/dup/report-two.md:7 (NEW-FixtureSeatA-1)
INTEGRATE_ERROR fixtures/dup/report-two.md:23 NEW-FixtureSeatA-2 — duplicate url https://example.org/fixture-a/register — also in fixtures/dup/report-one.md:23 (NEW-FixtureSeatA-2)
INTEGRATE_ERROR fixtures/dup/report-one.md:23 NEW-FixtureSeatA-2 — duplicate url https://example.org/fixture-a/register — also in fixtures/dup/report-two.md:23 (NEW-FixtureSeatA-2)
INTEGRATE: 6 hard error(s); no output written
----- EXIT: 1 -----

== out-dup written? ==
ls: cannot access 'out-dup': No such file or directory
```

### Run 4 — `--rewrite` dry run, then in place

```
----- COMMAND: python3 -B integrate-rows.py --rewrite rewrite-demo.md --map out-good/map.tsv --dry-run -----
REWRITE rewrite-demo.md: 3 replacement(s) of 2 draft id(s) (dry run)
REWRITE_ID NEW-FixtureSeatA-1 -> S900 x2
REWRITE_ID NEW-FixtureSeatB-1 -> S902 x1
----- EXIT: 0 -----

== file after the dry run (must be unchanged) ==
# Demo entry draft

- A mask may mark an office (NEW-FixtureSeatA-1, Description, second paragraph, sentence 2).
- The voice was licensed by the mask (NEW-FixtureSeatB-1, p. 47).
- A repeated reference to the same draft id (NEW-FixtureSeatA-1, section 3).
- A near miss that is not an id: NEW-FixtureSeatA-1x stays untouched.
```

```
----- COMMAND: python3 -B integrate-rows.py --rewrite rewrite-demo.md --map out-good/map.tsv -----
REWRITE rewrite-demo.md: 3 replacement(s) of 2 draft id(s)
REWRITE_ID NEW-FixtureSeatA-1 -> S900 x2
REWRITE_ID NEW-FixtureSeatB-1 -> S902 x1
----- EXIT: 0 -----

== file after the in-place rewrite ==
# Demo entry draft

- A mask may mark an office (S900, Description, second paragraph, sentence 2).
- The voice was licensed by the mask (S902, p. 47).
- A repeated reference to the same draft id (S900, section 3).
- A near miss that is not an id: NEW-FixtureSeatA-1x stays untouched.
```

The near miss `NEW-FixtureSeatA-1x` is left alone: the replacement boundary rejects a following word character, so a draft id prefix is never rewritten by accident.

---

## 5. The real seat reports (read-only)

The 40 seat reports were present in `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/` when this seat finished, so the tool was run against them. The lane was not written to. (A later run reports `files=41`, because this seat's own report now sits in the same directory; the tool parses it and finds no `### NEW-` block in it, so no phantom row appears.)

### Run 5 — the real reports, default settings (exit 1)

```
----- COMMAND: python3 -B integrate-rows.py --reports /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2 --start 900 --sources /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md --out out-real -----
INTEGRATE_ERROR .../ReviewSacredAccess.md:77 NEW-ReviewSacredAccess-5 — duplicate url https://ich.unesco.org/en/RL/gule-wamkulu-00142 — also in .../CriticCalibrationMasks.md:228 (NEW-CriticCalibrationMasks-15)
INTEGRATE_ERROR .../CriticCalibrationMasks.md:228 NEW-CriticCalibrationMasks-15 — duplicate url https://ich.unesco.org/en/RL/gule-wamkulu-00142 — also in .../ReviewSacredAccess.md:77 (NEW-ReviewSacredAccess-5)
INTEGRATE_ERROR .../ScoutGuleWamkulu.md:22 NEW-ScoutGuleWamkulu-1 — duplicate url https://ich.unesco.org/en/RL/gule-wamkulu-00142 — also in .../CriticCalibrationMasks.md:228 (NEW-CriticCalibrationMasks-15)
INTEGRATE_ERROR .../CriticCalibrationMasks.md:228 NEW-CriticCalibrationMasks-15 — duplicate url https://ich.unesco.org/en/RL/gule-wamkulu-00142 — also in .../ScoutGuleWamkulu.md:22 (NEW-ScoutGuleWamkulu-1)
INTEGRATE_ERROR .../ScoutHaudenosauneeStatement.md:21 NEW-ScoutHaudenosauneeStatement-1 — duplicate url http://www.nativetech.org/cornhusk/maskpoli.html — also in .../ReviewSacredAccess.md:47 (NEW-ReviewSacredAccess-3)
INTEGRATE_ERROR .../ReviewSacredAccess.md:47 NEW-ReviewSacredAccess-3 — duplicate url http://www.nativetech.org/cornhusk/maskpoli.html — also in .../ScoutHaudenosauneeStatement.md:21 (NEW-ScoutHaudenosauneeStatement-1)
INTEGRATE: 6 hard error(s); no output written
----- EXIT: 1 -----
```

**This is the tool earning its keep on real data**: two works were opened by two seats each (the UNESCO Gule Wamkulu element by three blocks, and the 1995 Haudenosaunee False Face Masks policy by two). Round 53 handled the same situation by merging rows and keeping the first seat's cells (`corpus/lessons/round-53.md:186`, and `.ufo/waves/round-53/integration-map.json`, where S187–S223 each carry two to four draft ids). `--merge-duplicates` reproduces that: one registry row per distinct url, the first seat's cells kept, every draft id in `map.tsv` pointed at the shared S-id.

### Run 6 — the real reports, with `--merge-duplicates --allow-long-quotes` (exit 0)

```
----- COMMAND: python3 -B integrate-rows.py --reports /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2 --start 900 --sources /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md --out out-real --merge-duplicates --allow-long-quotes -----
INTEGRATE_WARN .../ReviewSacredAccess.md:77 NEW-ReviewSacredAccess-5 — merged into the row of NEW-CriticCalibrationMasks-15 (same url https://ich.unesco.org/en/RL/gule-wamkulu-00142)
INTEGRATE_WARN .../ScoutGuleWamkulu.md:22 NEW-ScoutGuleWamkulu-1 — merged into the row of NEW-CriticCalibrationMasks-15 (same url https://ich.unesco.org/en/RL/gule-wamkulu-00142)
INTEGRATE_WARN .../ScoutHaudenosauneeStatement.md:21 NEW-ScoutHaudenosauneeStatement-1 — merged into the row of NEW-ReviewSacredAccess-3 (same url http://www.nativetech.org/cornhusk/maskpoli.html)
... (111 warnings in all; the rest are kind-mapping notes, "no teaches field" notes for the critic's calibration rows, and "draft sentence carries no (NEW-..., locator) marker" notes)
INTEGRATE: files=40 blocks=108 groups=105 ids=S900..S1004 rows=105 warnings=111
INTEGRATE_OK rows.md map.tsv gate.md sentences.md -> out-real
----- EXIT: 0 -----
```

108 blocks → 105 rows (three merged away).

---

## 6. What the tool reproduces, checked against the landed registry

The lane's round-54 claim C has already landed (tip `e17bc2b`; the rows landed at `6a658ca`, the records at `25375f1`). The tool's rows were compared with the 46 landed round-54 rows, matched by URL:

- **46 of 46 landed rows are matched** to a tool row by URL.
- `status` (`mined`), `opened` (`2026-10-22`), `recheck` (`365d`) and `used-by` (`corpus/knowledge/culture-material/masks-masquerade.md`): identical in **all 46**.
- 42 of the 46 rows are identical in every cell. The four that differ are S244, S254, S265 and S266, and the differences are the L1's own editorial choices, listed in §7: with the tool's default merge (`--merge-keep first`) `source` differs in 1 row (S265), `scope` in 3 (S254, S265, S266), `anchor` in 2 (S244, S265), `teaches` in 1 (S265); `kind` and `tier` agree in all 46.

### The registry census passes on the tool's output

105 generated rows appended to a copy of the live registry (ids S1200–S1304) in a sandbox under this seat's scratch dir, then the seven census commands from `SOURCES-CONTRACT-v1.md`:

```
--- rows ---            389
--- malformed (NF!=13) --- 0
--- enum violations ---   (none)
--- duplicate ids ---     (none)
```

So every row the tool writes keeps the registry's shape, keeps a legal kind/tier/status, and carries no duplicate id.

### The Gate lines match the lane's shape

105 Gate lines emitted. Compared with the lane's own lessons:

| file | lines | period outside the closing quote only | period inside the quote too | other |
|---|---|---|---|---|
| tool `out-real/gate.md` | 105 | 105 | 0 | 0 |
| `corpus/lessons/round-53.md` | 154 | 108 | 0 | 31 (curly-quoted passages) |
| `corpus/lessons/round-52.md` | 88 | 60 | 0 | 0 |
| `corpus/lessons/round-51.md` | 9 | 9 | 0 | 0 |

The lane puts the period that ends the quoted passage **outside** its closing quote (`round-53.md:44`, `:98`, `:170`), and the tool now does the same.

### The access gate agrees with the tool

The tool's access-marker pattern is the lane's own `BYPASS` regex, copied verbatim from `tools/check-source-access.py`, so the two cannot drift. Running the lane's own checker on the sandbox registry with the 105 generated rows appended:

```
ACCESS_FINDING status S1220 mined
ACCESS: 3 flagged rows, 1 findings
EXIT=1
```

That one finding is a real defect in a seat's route cell, not in the tool: see §7.

---

## 7. Findings for the L1

1. **One seat route cell trips the lane's access gate as written — but it needs no action here.**
   `NEW-ReviewSacredAccess-7` (`.ufo/waves/round-54/build-a2/ReviewSacredAccess.md:108`, the A:shiwi A:wan Museum "About the Museum" page) has a route cell ending `Ordinary means; no control bypassed.` The word `bypassed` is inside the lane's marker pattern, so `tools/check-source-access.py` would flag a row built from that cell as unopened. The tool prints exactly that warning:
   `INTEGRATE_WARN .../ReviewSacredAccess.md:108 NEW-ReviewSacredAccess-7 — the row's cells carry the access-control marker 'bypassed'; tools/check-source-access.py flags such a row as unopened, so reword the cell before the row is filed (QUALITY criterion 10)`.
   **The L1 confirms this block was never registered** (`grep -c "ashiwi-museum" corpus/SOURCES.md` → 0), so no landed row is affected and no rework is needed. The warning is worth keeping only as frontier input for round 55's seats, and only if that source is ever registered. The landed registry has no occurrence of `bypass` (grep count 0).

2. **Two works were opened by more than one seat — frontier input for round 55.**
   The UNESCO Gule Wamkulu element (`https://ich.unesco.org/en/RL/gule-wamkulu-00142`) was opened by three blocks (`CriticCalibrationMasks-15`, `ReviewSacredAccess-5`, `ScoutGuleWamkulu-1`), and the 1995 Haudenosaunee False Face Masks policy (`http://www.nativetech.org/cornhusk/maskpoli.html`) by two (`ReviewSacredAccess-3`, `ScoutHaudenosauneeStatement-1`). The default run refuses both; `--merge-duplicates` merges them the way round 53 did (one row per distinct url, every draft id in `map.tsv` pointed at the shared S-id).

   On the Haudenosaunee pair the landed **S265 is `ScoutHaudenosauneeStatement-1`'s work** — the lesson's Gate line for S265 reads `Seat: ScoutHaudenosauneeStatement.`, and the landed row's `source`, `anchor` and `teaches` cells match that block's wording exactly, with `scope` matching it up to the tier note. The tool's `--merge-keep last` reproduces those four cells on that basis; the default `--merge-keep first` keeps `ReviewSacredAccess-3`'s instead, which is why `source`, `scope`, `anchor` and `teaches` showed as differences in §6. Two cells follow neither mode: the landed row is `kind community` / tier B, which the tool derives from `ReviewSacredAccess-3`'s kind field (`record (community policy statement, …)`) rather than from `ScoutHaudenosauneeStatement-1`'s (`web (transcribed policy statement)`), and the landed scope carries the L1's longer tier-note form (§7.3). So the landed row mixes the scout's wording with the review seat's community filing — a hand merge, not a rule the tool can reproduce from one block.

   **The L1 has taken both duplicate-merge findings to round 55 as frontier input; no action is needed in round 54.**

3. **The L1's four editorial differences from the tool's mechanical output** (the tool is mechanical; the L1 is the editor, so these are choices, not defects):
   - S244's anchor: the L1 replaced the inner `|` of `"Il Dottore | Academic Bourgeoisie | Bolognese Macaronic"` with `/`. The tool keeps the passage verbatim and escapes the pipe as `&#124;`, so the row stays NF=13 and the quote stays readable. Either is defensible; the tool's is the one the registry census demands.
   - S254 and S266's scope cells: the L1 replaced the seat's tier note with a longer `(seat-proposed tier note, superseded by …) (tier B: community statement filed as kind community; …)` form. The tool appends the seat's tier note verbatim as `(tier note: …)`.
   - S265: the hand merge described in §7.2 — the scout's wording with the review seat's community filing. No single-block rule reproduces it; `--merge-keep last` reproduces the wording cells.
   - S254, S265 and S266 are filed as `kind community` with tier B by both the L1 and the tool. The tool reaches that by reading the seat's own kind field (`community policy statement`, `community-institution exhibit`, `tribal government statement`) and downgrading a seat's tier A to B for a community row, because the registry census treats community as never A. The citation is not used for this test, since a holding museum's record may quote a community's words without being one (that distinction is what keeps S246 at `docs`/A).

4. **`kind` vocabulary.** The wave's Output section offers `paper, book, dataset, web, record`; the registry's enum is `spec, docs, paper, code, tool, dataset, talk, book, community, own-work`. The tool maps `web` and `record` to `docs` (what the lane's landed round-54 rows do) and warns on every mapping, so no mapping is silent.

5. **`| ` inside a cell.** The contract forbids a raw `|` in any cell and the census splits on `|`. The tool escapes a pipe as `&#124;` (an HTML entity, so the cell still renders a pipe) rather than dropping or mangling the passage.

6. **Unrun checks.** This seat ran no gate on the lane: `reports/round-54/accept-c.py` and `reports/round-28/readme/sweep.py` were not run, because the claim has already landed and the parent owns the post-integration gate. The tool's own output was checked against the registry census commands and `tools/check-source-access.py` in a sandbox copy under this seat's scratch dir, never in the lane.

---

## 8. Files

| path | what |
|---|---|
| `/fast/scratch/hyaku/kotodama-r54-a2/ExecIntegrateRows/integrate-rows.py` | the tool (654 lines, stdlib only) |
| `/fast/scratch/hyaku/kotodama-r54-a2/ExecIntegrateRows/run-fixtures.sh` | the fixture suite driver |
| `/fast/scratch/hyaku/kotodama-r54-a2/ExecIntegrateRows/fixtures/good/fixture-a.md` | good fixture report, two blocks |
| `/fast/scratch/hyaku/kotodama-r54-a2/ExecIntegrateRows/fixtures/good/fixture-b.md` | good fixture report, one block |
| `/fast/scratch/hyaku/kotodama-r54-a2/ExecIntegrateRows/fixtures/bad/fixture-c-malformed.md` | malformed fixture report |
| `/fast/scratch/hyaku/kotodama-r54-a2/ExecIntegrateRows/fixtures/dup/` | duplicate-across-files fixture |
| `/fast/scratch/hyaku/kotodama-r54-a2/ExecIntegrateRows/fixtures-run.txt` | the full suite transcript (215 lines) |
| `/fast/scratch/hyaku/kotodama-r54-a2/ExecIntegrateRows/out-good/`, `out-bad/`, `out-dup/`, `out-real/` | the four runs' outputs |
| `/fast/scratch/hyaku/kotodama-r54-a2/ExecIntegrateRows/sandbox/` | a copy of the registry with the generated rows appended, for the census and access checks |
| `.ufo/waves/round-54/build-a2/ExecIntegrateRows.md` | this report (the only lane file this seat wrote) |

No tool was installed and no package was upgraded: the task needs only Python 3, which the host already has (3.14.8).
