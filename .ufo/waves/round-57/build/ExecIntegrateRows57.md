# ExecIntegrateRows57 — Round 57 claim C integrator

## Axes and result

- Operability: copied the read-only round-56 integrator into /fast/scratch/hyaku/kotodama-r57/ExecIntegrateRows57/integrate-rows.py; its default inclusive allocation is S413–S480 and over-capacity input returns 1 before creating artifacts.
- Calibration: each block's first quote is passed to round-57 reopen-quote.py in URL mode; locate.md records the exact command, LOCATED/NOT_LOCATED result, URL, and quote. The source-cell URL is written first and the original first quote remains first in anchor.
- Character references: report fields are rejected when recognized by the explicit pattern or Python's html.unescape; literal table pipes in registry cells are rejected. All five generated artifacts are checked before writing. No HTML entity encoding is used.
- The only lane write is this exclusive report. Script, synthetic fixture, and generated test artifacts are under the assigned /fast/scratch/hyaku/kotodama-r57/ExecIntegrateRows57/ directory. No source registry, knowledge file, lesson, or lane tool was changed.
- Python 3 standard library only; no package installation or update. No git/jj writes. LSP was unavailable in the seat tool inventory, so no symbol operation was possible; this is a standalone script.

## Usage

python3 -B /fast/scratch/hyaku/kotodama-r57/ExecIntegrateRows57/integrate-rows.py --reports <reports-dir> --start 413 --end 480 --sources /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md --out <scratch-output-dir>

--start defaults to 413, --end to 480, --locator defaults to /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-57/reopen-quote.py, and --used-by defaults to corpus/knowledge/myth-symbol/heraldry-emblems-identity-marks.md. Outputs: rows.md, map.tsv, gate.md, sentences.md, and locate.md. Existing --rewrite and --self-check options were retained.

## Commands and retained output

The first demonstration pass preceded the final hardening that also detects semicolonless named references through html.unescape. All requested demonstrations were rerun against the final script below; both passes are retained here because every execution is requested.

### Initial demonstration pass

Command:

    python3 -B /fast/scratch/hyaku/kotodama-r57/ExecIntegrateRows57/integrate-rows.py --reports /fast/scratch/hyaku/kotodama-r57/ExecIntegrateRows57/fixtures --sources /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md --out /fast/scratch/hyaku/kotodama-r57/ExecIntegrateRows57/out-synthetic

Output:

    LOCATOR NEW-SyntheticReservedDomains-1 LOCATED
    INTEGRATE: files=1 blocks=1 groups=1 ids=S413..S413 rows=1 warnings=0
    INTEGRATE_OK rows.md map.tsv gate.md sentences.md locate.md -> /fast/scratch/hyaku/kotodama-r57/ExecIntegrateRows57/out-synthetic
    EXIT_CODE=0

Command:

    python3 -B /fast/scratch/hyaku/kotodama-r57/ExecIntegrateRows57/integrate-rows.py --reports /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-56/build --exclude '^(?!.*ScoutUnescoMbanzaKongo\.md$)' --sources /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md --out /fast/scratch/hyaku/kotodama-r57/ExecIntegrateRows57/out-unesco

Output:

    LOCATOR NEW-ScoutUnescoMbanzaKongo-1 LOCATED
    LOCATOR NEW-ScoutUnescoMbanzaKongo-2 LOCATED
    INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-56/build/ScoutUnescoMbanzaKongo.md:32 NEW-ScoutUnescoMbanzaKongo-1 — seat kind 'record' filed as registry kind 'docs'
    INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-56/build/ScoutUnescoMbanzaKongo.md:32 NEW-ScoutUnescoMbanzaKongo-1 — draft sentence carries no (NEW-..., locator) marker
    INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-56/build/ScoutUnescoMbanzaKongo.md:64 NEW-ScoutUnescoMbanzaKongo-2 — seat kind 'record' filed as registry kind 'docs'
    INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-56/build/ScoutUnescoMbanzaKongo.md:64 NEW-ScoutUnescoMbanzaKongo-2 — draft sentence carries no (NEW-..., locator) marker
    INTEGRATE: files=1 blocks=2 groups=2 ids=S413..S414 rows=2 warnings=4
    INTEGRATE_OK rows.md map.tsv gate.md sentences.md locate.md -> /fast/scratch/hyaku/kotodama-r57/ExecIntegrateRows57/out-unesco
    EXIT_CODE=0

Command:

    python3 -B /fast/scratch/hyaku/kotodama-r57/ExecIntegrateRows57/integrate-rows.py --reports /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-56/build --exclude '^(?!.*ScoutRaffiaCloth\.md$)' --sources /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md --out /fast/scratch/hyaku/kotodama-r57/ExecIntegrateRows57/out-raffia

Output:

    LOCATOR NEW-ScoutRaffiaCloth-1 LOCATED
    LOCATOR NEW-ScoutRaffiaCloth-2 NOT_LOCATED
    LOCATOR NEW-ScoutRaffiaCloth-3 NOT_LOCATED
    INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-56/build/ScoutRaffiaCloth.md:57 NEW-ScoutRaffiaCloth-2 — live quote locator: NOT_LOCATED https://web.archive.org/web/20220523145743/https://www.britishmuseum.org/collection/object/E_Af1951-04-118 HTTPError
    INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-56/build/ScoutRaffiaCloth.md:88 NEW-ScoutRaffiaCloth-3 — live quote locator: NOT_LOCATED https://web.archive.org/web/20151110063110/http://www.metmuseum.org/exhibitions/listings/2015/kongo/blog/posts/kongo-textiles-renaissance-european-collections URLError
    INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-56/build/ScoutRaffiaCloth.md:25 NEW-ScoutRaffiaCloth-1 — draft sentence carries no (NEW-..., locator) marker
    INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-56/build/ScoutRaffiaCloth.md:57 NEW-ScoutRaffiaCloth-2 — seat kind 'record' filed as registry kind 'docs'
    INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-56/build/ScoutRaffiaCloth.md:57 NEW-ScoutRaffiaCloth-2 — draft sentence carries no (NEW-..., locator) marker
    INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-56/build/ScoutRaffiaCloth.md:88 NEW-ScoutRaffiaCloth-3 — seat kind 'web' filed as registry kind 'docs'
    INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-56/build/ScoutRaffiaCloth.md:88 NEW-ScoutRaffiaCloth-3 — draft sentence carries no (NEW-..., locator) marker
    INTEGRATE: files=1 blocks=3 groups=3 ids=S413..S415 rows=3 warnings=7
    INTEGRATE_OK rows.md map.tsv gate.md sentences.md locate.md -> /fast/scratch/hyaku/kotodama-r57/ExecIntegrateRows57/out-raffia
    EXIT_CODE=0

Overflow command:

    python3 -B /fast/scratch/hyaku/kotodama-r57/ExecIntegrateRows57/integrate-rows.py --reports /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-56/build --exclude '^(?!.*ScoutRaffiaCloth\.md$)' --start 413 --end 414 --sources /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md --out /fast/scratch/hyaku/kotodama-r57/ExecIntegrateRows57/out-overflow

Output:

    INTEGRATE_ERROR /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-56/build/ScoutRaffiaCloth.md:88 NEW-ScoutRaffiaCloth-3 — reserved id block S413-S414 holds 2 blocks; found 3; no output written
    EXIT_CODE=1
    ROWS_FILE=absent

### Final-source demonstration rerun

Command:

    python3 -B /fast/scratch/hyaku/kotodama-r57/ExecIntegrateRows57/integrate-rows.py --reports /fast/scratch/hyaku/kotodama-r57/ExecIntegrateRows57/fixtures --sources /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md --out /fast/scratch/hyaku/kotodama-r57/ExecIntegrateRows57/out-synthetic

Output:

    LOCATOR NEW-SyntheticReservedDomains-1 LOCATED
    INTEGRATE: files=1 blocks=1 groups=1 ids=S413..S413 rows=1 warnings=0
    INTEGRATE_OK rows.md map.tsv gate.md sentences.md locate.md -> /fast/scratch/hyaku/kotodama-r57/ExecIntegrateRows57/out-synthetic
    EXIT_CODE=0

Command:

    python3 -B /fast/scratch/hyaku/kotodama-r57/ExecIntegrateRows57/integrate-rows.py --reports /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-56/build --exclude '^(?!.*ScoutUnescoMbanzaKongo\.md$)' --sources /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md --out /fast/scratch/hyaku/kotodama-r57/ExecIntegrateRows57/out-unesco

Output:

    LOCATOR NEW-ScoutUnescoMbanzaKongo-1 LOCATED
    LOCATOR NEW-ScoutUnescoMbanzaKongo-2 LOCATED
    INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-56/build/ScoutUnescoMbanzaKongo.md:32 NEW-ScoutUnescoMbanzaKongo-1 — seat kind 'record' filed as registry kind 'docs'
    INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-56/build/ScoutUnescoMbanzaKongo.md:32 NEW-ScoutUnescoMbanzaKongo-1 — draft sentence carries no (NEW-..., locator) marker
    INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-56/build/ScoutUnescoMbanzaKongo.md:64 NEW-ScoutUnescoMbanzaKongo-2 — seat kind 'record' filed as registry kind 'docs'
    INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-56/build/ScoutUnescoMbanzaKongo.md:64 NEW-ScoutUnescoMbanzaKongo-2 — draft sentence carries no (NEW-..., locator) marker
    INTEGRATE: files=1 blocks=2 groups=2 ids=S413..S414 rows=2 warnings=4
    INTEGRATE_OK rows.md map.tsv gate.md sentences.md locate.md -> /fast/scratch/hyaku/kotodama-r57/ExecIntegrateRows57/out-unesco
    EXIT_CODE=0

Command:

    python3 -B /fast/scratch/hyaku/kotodama-r57/ExecIntegrateRows57/integrate-rows.py --reports /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-56/build --exclude '^(?!.*ScoutRaffiaCloth\.md$)' --sources /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md --out /fast/scratch/hyaku/kotodama-r57/ExecIntegrateRows57/out-raffia

Output:

    LOCATOR NEW-ScoutRaffiaCloth-1 NOT_LOCATED
    LOCATOR NEW-ScoutRaffiaCloth-2 NOT_LOCATED
    LOCATOR NEW-ScoutRaffiaCloth-3 NOT_LOCATED
    INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-56/build/ScoutRaffiaCloth.md:25 NEW-ScoutRaffiaCloth-1 — live quote locator: NOT_LOCATED https://journals.flvc.org/athanor/article/download/126740/126293/207658 HTTPError
    INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-56/build/ScoutRaffiaCloth.md:57 NEW-ScoutRaffiaCloth-2 — live quote locator: NOT_LOCATED https://web.archive.org/web/20220523145743/https://www.britishmuseum.org/collection/object/E_Af1951-04-118 URLError
    INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-56/build/ScoutRaffiaCloth.md:88 NEW-ScoutRaffiaCloth-3 — live quote locator: NOT_LOCATED https://web.archive.org/web/20151110063110/http://www.metmuseum.org/exhibitions/listings/2015/kongo/blog/posts/kongo-textiles-renaissance-european-collections URLError
    INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-56/build/ScoutRaffiaCloth.md:25 NEW-ScoutRaffiaCloth-1 — draft sentence carries no (NEW-..., locator) marker
    INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-56/build/ScoutRaffiaCloth.md:57 NEW-ScoutRaffiaCloth-2 — seat kind 'record' filed as registry kind 'docs'
    INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-56/build/ScoutRaffiaCloth.md:57 NEW-ScoutRaffiaCloth-2 — draft sentence carries no (NEW-..., locator) marker
    INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-56/build/ScoutRaffiaCloth.md:88 NEW-ScoutRaffiaCloth-3 — seat kind 'web' filed as registry kind 'docs'
    INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-56/build/ScoutRaffiaCloth.md:88 NEW-ScoutRaffiaCloth-3 — draft sentence carries no (NEW-..., locator) marker
    INTEGRATE: files=1 blocks=3 groups=3 ids=S413..S415 rows=3 warnings=8
    INTEGRATE_OK rows.md map.tsv gate.md sentences.md locate.md -> /fast/scratch/hyaku/kotodama-r57/ExecIntegrateRows57/out-raffia
    EXIT_CODE=0

Overflow command:

    python3 -B /fast/scratch/hyaku/kotodama-r57/ExecIntegrateRows57/integrate-rows.py --reports /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-56/build --exclude '^(?!.*ScoutRaffiaCloth\.md$)' --start 413 --end 414 --sources /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md --out /fast/scratch/hyaku/kotodama-r57/ExecIntegrateRows57/out-overflow

Output:

    INTEGRATE_ERROR /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-56/build/ScoutRaffiaCloth.md:88 NEW-ScoutRaffiaCloth-3 — reserved id block S413-S414 holds 2 blocks; found 3; no output written
    EXIT_CODE=1
    ROWS_FILE=absent

Artifact scan on final output directories: pattern &(?:#(?:[0-9]+|[xX][0-9A-Fa-f]+);?|[A-Za-z][A-Za-z0-9]+;) returned exactly: No matches found.

## Risks and blockers

- LOCATE outcomes are network-sensitive. On the final run, the three Raffia first quotes reported NOT_LOCATED (Athanor HTTPError; British Museum and Met Wayback URLs URLError). These outcomes are retained, not rewritten or routed around. UNESCO and synthetic first quotes were LOCATED. Earlier pass statuses differed for the Athanor request.
- Round-56 demo reports contain expected adapter warnings: record/web map to registry kind docs; several legacy draft sentences have no NEW marker. They were not edited, and the tool surfaced them.
- No implementation blocker. No package install/update. LSP tool unavailable as noted above.

## Final integrator source

```python
#!/usr/bin/env python3
"""integrate-rows.py — kotodama round-57 claim C registry integrator.

Turns seat reports' `### NEW-<Seat>-<n>` blocks into four artefacts:

  rows.md       one corpus/SOURCES.md registry row per block, in the 11-column
                shape of the live registry (column order is read from its header)
  map.tsv       draft id -> S-id
  gate.md       one round-lesson `## Gate` line per row, grounded by the full
                `teaches` sentence and carrying one quoted source span
  sentences.md  every block's draft sentences with draft ids replaced by S-ids

In `--rewrite` mode, draft ids inside a given file are rewritten in place using
map.tsv.

Usage:
  python3 -B integrate-rows.py --reports <dir> --start 413 --end 480 \
      --sources /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md \
      --out <dir> --self-check

  python3 -B integrate-rows.py --rewrite <file> --map <map.tsv> [--dry-run]

Block shape: a `### NEW-<Seat>-<n>` heading followed by `citation:`, `url:`,
`route:`, `kind:`, `tier:`, `scope:`, `quotes:` (bulleted, each `<locator>:
"<quote>"`), `teaches:`, `draft sentences:` (3-6 sentences, each ending
`(NEW-<Seat>-<n>, <locator>)`) and `unopened:`. Keys may be list items, values
may run over multiple lines, and quoted passages may contain straight quotes.

Hard errors (exit 1, nothing written): a block with no url, quotes or teaches
sentence; an unparseable quote or no quote at most 25 words; a duplicate url
unless `--merge-duplicates` is set; a duplicate draft id; any character
reference in report fields; literal table pipes in registry-cell values; or
more blocks than the inclusive 413–480 id range. The first anchor quote is sent
to reopen-quote.py in URL mode; each result is recorded in locate.md.
Registry id collisions and failed live locations are warnings. Stdlib only.
Exit codes: 0 success, 1 hard error, 2 bad invocation or unreadable input.
"""

import argparse
from html import unescape as html_unescape
import os
import re
import shlex
import subprocess
import sys
import tempfile

# --- block and field grammar -------------------------------------------------

BLOCK_RE = re.compile(r"^#{2,4}\s+(NEW-(?P<seat>[A-Za-z0-9_]+(?:-[A-Za-z0-9_]+)*)-(?P<num>\d+))\b")
KEY_RE = re.compile(r"^(?P<key>[A-Za-z][A-Za-z0-9 _-]{0,40}?)\s*:\s*(?!/)(?P<val>.*)$")
BULLET_RE = re.compile(r"^\s*(?:[-*+]|\d+[.)])\s+")
MARKER_RE = re.compile(r"\((?P<did>NEW-[A-Za-z0-9_]+(?:-[A-Za-z0-9_]+)*-\d+)\s*,\s*(?P<loc>[^)]*)\)")
CHAR_REF_RE = re.compile(r"&(?:#(?:[0-9]+|[xX][0-9A-Fa-f]+);?|[A-Za-z][A-Za-z0-9]+;)")
LOCATOR_DEFAULT = "/home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-57/reopen-quote.py"


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
# book, community, own-work. The wave vocabulary also uses `web` and `record`.
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

# A seat kind that names a community-authored source.
COMMUNITY_RE = re.compile(
    r"\bcommunity\b|\btribal\b|\bfirst nations\b|\bband council\b",
    re.IGNORECASE,
)

# QUALITY criterion 10 markers, copied from tools/check-source-access.py.
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


def character_reference(text):
    """Recognize semicolonless HTML names as well as explicit references."""
    if "&" not in text:
        return None
    match = CHAR_REF_RE.search(text)
    if match:
        return match.group(0)
    return "recognized HTML reference" if html_unescape(text) != text else None


def cell(text, field):
    """Normalize one registry cell without encoding or emitting character references."""
    raw = text or ""
    reference = character_reference(raw)
    if reference:
        raise ValueError("character reference %r is not permitted in %s field"
                         % (reference, field))
    normalized = re.sub(r"\s+", " ", raw.strip())
    if "|" in normalized:
        raise ValueError("literal table pipe is not permitted in %s field" % field)
    return normalized


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


def _locator_key(text):
    """Normalize punctuation only for detecting a repeated locator echo."""
    return re.findall(r"[\w]+", text.casefold(), re.UNICODE)


def split_quote_line(line):
    """Parse a quoted source passage and discard a repeated locator echo.

    Reports usually delimit passages with double quotes, but some older reports
    use single quotes around passages that contain double-quoted words. The
    locator may itself carry quotes, and the passage may be followed by a
    bracketed or parenthesised note. A round-54 defect duplicated the locator
    inside the quoted passage; when the first double-quoted text repeats the
    locator before another `: "`, keep only the actual passage.
    """
    line = strip_bullet(line)

    single_openers = [i for i in range(2, len(line))
                      if line[i] == "'" and line[i - 2:i] == ": "]
    if single_openers:
        opening = single_openers[0]
        locator = line[:opening].rstrip()
        if locator.endswith(":"):
            locator = locator[:-1].rstrip()
        start = opening + 1
        stripped = line.rstrip()
        end = len(stripped) - 1
        if not (stripped.endswith("'") and end > start):
            end = None
            for index in range(start, len(line)):
                if line[index] == "'" and re.match(r"^\s*(\(|\[|$)", line[index + 1:]):
                    end = index
                    break
            if end is None:
                return None
        quote = line[start:end]
        if not quote.strip():
            return None
        return locator, quote, line[end + 1:].strip(), False

    if '"' not in line:
        return None
    openers = [i for i in range(2, len(line)) if line[i] == '"' and line[i - 2:i] == ": "]
    if not openers:
        first = line.find('"')
        if first < 0:
            return None
        openers = [first]

    first_opening = openers[0]
    locator = line[:first_opening].rstrip()
    if locator.endswith(":"):
        locator = locator[:-1].rstrip()

    opening = first_opening
    locator_key = _locator_key(locator)
    for next_opening in openers[1:]:
        echoed = line[first_opening + 1:next_opening]
        if locator_key and _locator_key(echoed) == locator_key:
            opening = next_opening
            break

    start = opening + 1
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


def input_reference_problems(block):
    """Reject character references in every report field; never encode a substitute."""
    problems = []
    for field, values in block.fields.items():
        for value in values:
            reference = character_reference(value)
            if reference:
                problems.append((block, "character reference %r is not permitted in %s field"
                                 % (reference, field)))
    return problems


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

    # Community-authored sources are never tier A in the registry census.
    if args.community_kind and COMMUNITY_RE.search(kind_raw):
        if kind != "community":
            warnings.append("seat kind %r filed as registry kind community (a community's own "
                            "statement)" % kind_raw[:60])
        kind = "community"
        if tier == "A":
            tier = "B"
            warnings.append("tier A downgraded to B: the registry census treats a community row as "
                            "never tier A")

    source = url + (" — " + citation if citation else "")
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

    bypass = BYPASS_RE.search(" ".join((source, anchor, scope_cell, teaches)))
    if bypass:
        warnings.append("the row's cells carry the access-control marker %r; "
                        "tools/check-source-access.py flags such a row as unopened, so reword the "
                        "cell before the row is filed (QUALITY criterion 10)"
                        % bypass.group(0))

    teaches_cell = cell(teaches or "—", "teaches")
    values = {
        "id": sid,
        "source": source,
        "kind": kind,
        "tier": tier,
        "scope": scope_cell,
        "anchor": anchor,
        "teaches": teaches_cell,
        "status": args.status,
        "opened": args.opened,
        "recheck": args.recheck,
        "used-by": args.used_by,
    }
    return [cell(values.get(name, ""), name) for name in columns], warnings, teaches_cell


def gate_label(text):
    """Render metadata without converting punctuation to character references."""
    return (text or "").translate(str.maketrans({
        '"': "'",
        "“": "‘",
        "”": "’",
        "«": "‹",
        "»": "›",
    }))


def gate_quote(text):
    """Choose an unused delimiter without changing the source quotation."""
    quote = (text or "").strip()
    for opening, closing in (("“", "”"), ("«", "»"), ('"', '"')):
        if opening not in quote and closing not in quote:
            return opening + quote + closing
    raise ValueError("quote contains every supported Gate delimiter; refusing to alter quote text")


def gate_line(sid, url, locator, quote, teaches, seat, accessed):
    """Keep Grounds identical to the registry teaches cell."""
    where = ("%s: " % gate_label(locator)) if locator else ""
    where += gate_quote(quote)
    return "- %s — %s — accessed %s — %s. Grounds: %s Seat: %s." % (
        sid, gate_label(url), accessed, where, teaches, seat)


def locate_quote(args, block, quote):
    """Run the round locator in URL mode and retain its exact result."""
    url = block.text("url").strip()
    command = ["python3", "-B", args.locator, url, quote]
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                universal_newlines=True)
        output = (result.stdout or "").strip()
        if result.stderr:
            output = (output + " | stderr: " + result.stderr.strip()).strip(" |")
        status = "LOCATED" if result.returncode == 0 and output.startswith("LOCATED ") else "NOT_LOCATED"
        if status == "NOT_LOCATED" and not output.startswith("NOT_LOCATED "):
            output = "NOT_LOCATED " + (output or "locator returned no output")
    except OSError as error:
        status = "NOT_LOCATED"
        output = "NOT_LOCATED locator invocation failed: %s" % error
    return status, shlex.join(command), output

def self_check(args, rows_path, gate_path):
    """Run the lane quote checker on a lesson shell with matching source rows."""
    if not args.self_check:
        return 0
    with tempfile.TemporaryDirectory(prefix=".gate-self-check-", dir=args.out) as work:
        corpus = os.path.join(work, "corpus")
        lessons = os.path.join(corpus, "lessons")
        os.makedirs(lessons)
        source_path = os.path.join(corpus, "SOURCES.md")
        lesson_path = os.path.join(lessons, "gate.md")
        with open(rows_path, encoding="utf-8") as handle:
            rows = handle.read()
        with open(source_path, "w", encoding="utf-8") as handle:
            handle.write("| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |\n")
            handle.write(rows)
        with open(gate_path, encoding="utf-8") as handle:
            gate = handle.read()
        with open(lesson_path, "w", encoding="utf-8") as handle:
            handle.write("# Round 57 — lesson (kotodama)\n\n")
            handle.write(gate)
            if gate and not gate.endswith("\n"):
                handle.write("\n")
            handle.write("\n## Status\n")

        command = ["python3", "-B", args.checker, lesson_path]
        print("SELF_CHECK_COMMAND %s" % " ".join(command))
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                universal_newlines=True)
        if result.stdout:
            sys.stdout.write(result.stdout)
        if result.stderr:
            sys.stderr.write(result.stderr)
        print("SELF_CHECK_EXIT %d" % result.returncode)
        return result.returncode


def integrate(args):
    columns, existing = read_registry(args.sources)
    if columns != COLUMNS:
        raise ValueError("registry header %r does not match the expected columns %r"
                         % (columns, COLUMNS))
    if args.end < args.start:
        raise ValueError("--end must be greater than or equal to --start")

    problems, warnings = [], []
    blocks = []
    files = report_files(args.reports, args.exclude)
    for path in files:
        blocks.extend(parse_report(path))

    capacity = args.end - args.start + 1
    if len(blocks) > capacity:
        block = blocks[capacity]
        print("INTEGRATE_ERROR %s:%d %s — reserved id block S%03d-S%03d holds %d blocks; "
              "found %d; no output written"
              % (block.path, block.line, block.draft_id, args.start, args.end,
                 capacity, len(blocks)), file=sys.stderr)
        return 1

    seen_draft = {}
    for block in blocks:
        problems.extend(input_reference_problems(block))
        if block.draft_id in seen_draft:
            problems.append((block, "draft id %s already used in %s:%d"
                             % (block.draft_id, seen_draft[block.draft_id][0],
                                seen_draft[block.draft_id][1])))
        else:
            seen_draft[block.draft_id] = (block.path, block.line)
        if not block.text("teaches"):
            problems.append((block, "block has no teaches sentence"))

    # One row per URL only when explicitly requested; by default duplicate URLs
    # are a hard error, so every block has one unambiguous registry row.
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
        quote_problems = []
        parsed_quotes = block_quotes(block, quote_problems)
        problems.extend(quote_problems)
        if not parsed_quotes:
            problems.append((block, "block has no parseable quote"))
            continue
        usable_quote = False
        for locator, quote, tail, multiple in parsed_quotes:
            count = words(quote)
            if count <= args.max_quote_words:
                usable_quote = True
            else:
                message = ("quote of %d words exceeds the %d-word limit: %r"
                           % (count, args.max_quote_words, quote[:90]))
                if args.allow_long_quotes:
                    warnings.append((block, message))
                else:
                    problems.append((block, message))
        if not usable_quote:
            problems.append((block, "block has no quote of at most %d words" % args.max_quote_words))
    if problems:
        for block, message in problems:
            print("INTEGRATE_ERROR %s:%d %s — %s" % (block.path, block.line, block.draft_id, message),
                  file=sys.stderr)
        print("INTEGRATE: %d hard error(s); no output written" % len(problems), file=sys.stderr)
        return 1

    locator_results = {}
    for block in blocks:
        # The first report quote is both the locator target and the first anchor span.
        first_quote = block_quotes(block, [])[0]
        status, command, output = locate_quote(args, block, first_quote[1])
        locator_results[block.draft_id] = (status, command, output)
        print("LOCATOR %s %s" % (block.draft_id, status))
        if status != "LOCATED":
            warnings.append((block, "live quote locator: %s" % output))

    os.makedirs(args.out, exist_ok=True)

    rows, gate, mapping, sentence_sections = [], [], [], []
    for offset, group in enumerate(groups):
        block, members = group
        sid = "S%03d" % (args.start + offset)
        if sid in existing:
            warnings.append((block, "assigned id %s already exists in the registry; the row would "
                                    "duplicate it" % sid))
        cells, row_warnings, teaches_cell = build_row(block, sid, args, columns)
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
                        "Grounds: %s Seat: %s." % (sid, gate_label(url), args.opened,
                                                   args.max_quote_words, teaches_cell, block.seat))
        else:
            gate.append(gate_line(sid, url, chosen[0], chosen[1], teaches_cell,
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

    sentence_lines = []
    for sid, draft_id, units in sentence_sections:
        sentence_lines.append("## %s — %s" % (sid, draft_id))
        sentence_lines.append("")
        for unit in units:
            sentence_lines.append(rewrite_ids(unit))
        sentence_lines.append("")

    sid_for_draft = dict(mapping)
    locator_lines = ["# Live quote locator results", ""]
    for block in blocks:
        status, command, output = locator_results[block.draft_id]
        locator_lines.extend([
            "### %s" % block.draft_id,
            "",
            "- assigned id: %s" % sid_for_draft[block.draft_id],
            "- URL: %s" % block.text("url").strip(),
            "- first anchor quote: %s" % block_quotes(block, [])[0][1],
            "- status: %s" % status,
            "- command: %s" % command,
            "- locator output: %s" % output,
            "",
        ])

    artifacts = {
        "rows.md": "\n".join(rows) + ("\n" if rows else ""),
        "map.tsv": "draft_id\ts_id\n" + "".join(
            "%s\t%s\n" % (draft_id, sid) for draft_id, sid in mapping),
        "gate.md": "## Gate\n\n" + "\n".join(gate) + ("\n" if gate else ""),
        "sentences.md": "\n".join(sentence_lines).rstrip() + "\n",
        "locate.md": "\n".join(locator_lines).rstrip() + "\n",
    }
    for name, text in artifacts.items():
        reference = character_reference(text)
        if reference:
            raise ValueError("refusing to write character reference %r to %s" % (reference, name))
    for name, text in artifacts.items():
        with open(os.path.join(args.out, name), "w", encoding="utf-8") as handle:
            handle.write(text)
    self_check_status = self_check(
        args, os.path.join(args.out, "rows.md"), os.path.join(args.out, "gate.md"))
    if self_check_status:
        return self_check_status


    for block, message in warnings:
        print("INTEGRATE_WARN %s:%d %s — %s" % (block.path, block.line, block.draft_id, message),
              file=sys.stderr)
    print("INTEGRATE: files=%d blocks=%d groups=%d ids=%s..%s rows=%d warnings=%d"
          % (len(files), len(blocks), len(groups), "S%03d" % args.start,
             "S%03d" % (args.start + len(groups) - 1) if groups else "—", len(rows), len(warnings)))
    print("INTEGRATE_OK rows.md map.tsv gate.md sentences.md locate.md -> %s" % args.out)
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
        reference = character_reference(text)
        if reference:
            raise ValueError("refusing to write character reference %r in rewritten text"
                             % reference)
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
    parser.add_argument("--start", type=int, default=413, help="first S-id to assign")
    parser.add_argument("--end", type=int, default=480, help="last S-id to assign (inclusive)")
    parser.add_argument("--sources", help="path to corpus/SOURCES.md")
    parser.add_argument("--out", help="directory for rows.md, map.tsv, gate.md, sentences.md, locate.md")
    parser.add_argument("--locator", default=LOCATOR_DEFAULT,
                        help="round-57 reopen-quote.py invoked in URL mode for each first anchor quote")
    parser.add_argument("--self-check", action="store_true",
                         help="run tools/check-gate-quotes.py on the generated Gate in a lesson shell")
    parser.add_argument("--checker", default="/home/vgpnk/Projects/shokunin/kotodama-shokunin/tools/check-gate-quotes.py",
                        help="quote checker used by --self-check")
    parser.add_argument("--rewrite", help="file whose draft ids are replaced in place")
    parser.add_argument("--map", help="map.tsv used by --rewrite")
    parser.add_argument("--dry-run", action="store_true", help="--rewrite without writing")
    parser.add_argument("--used-by", default="corpus/knowledge/myth-symbol/heraldry-emblems-identity-marks.md",
                        help="used-by cell of every row")
    parser.add_argument("--status", default="mined", help="status cell of every row")
    parser.add_argument("--opened", default="2026-10-22", help="opened date in Gate lines and rows")
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
