#!/usr/bin/env python3
r"""Round-77 claim-C evidence capture (adapted from round 76).

Fetches the LIVE URL and its SAME-PAGE Wayback capture, records what each
request was actually served, and writes the evidence file the claim-C EVIDENCE
leg reads: `reports/round-77/evidence/<id>.txt`.

Round-77 changes, and why (each one is shown able to fail in `--selftest`):

 1. TWO FETCHES PER RECEIPT (QUALITY 18).  Round 76 captured one URL.  Round 77
    requires a row's source cell to carry a live URL *and* its same-page
    Wayback capture, so one receipt now holds two responses: the live fetch and
    the capture.  Which one the window was cut from is a fact in the file
    (`window-source:`), not an assumption: a page the live web still serves is
    windowed from the live fetch, and a page that answers a 403 wall (D1/S897)
    is windowed from the capture, which is the ordinary-means copy.

 2. SAME-PAGE IS PROVEN, NOT ASSERTED.  archive.org names the captured page
    inside the replay path (`/web/<ts>[id_|if_]/<original>`).  The tool reads
    the embedded original out of the URL it was asked to fetch and requires it
    to equal the live URL after normalisation (scheme dropped, a leading
    `www.` dropped, trailing slash dropped).  `wayback-original:`,
    `wayback-same-page:` and `wayback-final-original:` (the original embedded in
    the URL the archive redirected to, e.g. `http://www.example.com/` when we
    asked for `https://example.com/`) make the binding visible; a capture of a
    different page is REFUSED (exit 7, nothing written).

 3. UA -> RESPONSE BINDING (QUALITY 22).  Each fetch record binds the exact
    User-Agent that request sent to the response that request received, in one
    line: `response-bind-live:` / `response-bind-wayback:` carry `ua="…" ->
    http=… bytes=… sha256=… final-url=…` (plus the capture's memento).  The
    per-fetch `live-*` / `wayback-*` atoms repeat the same values, so a counter
    can check the binding instead of trusting that both fetches used one UA.
    `--wayback-ua` exists so the two records can differ and still be bound.

 4. A CAPTURE MUST BE DATABLE.  A Wayback replay states when it was captured in
    `Memento-Datetime`.  The tool records it (`wayback-memento-datetime:`) and
    whether it matches the timestamp requested in the replay URL
    (`wayback-timestamp-matches: yes | nearest | -`); `nearest` is the normal
    case when that exact second was never captured.  A 200 capture that serves
    no memento is REFUSED, because a copy nobody can date is not evidence.

 5. THE ROW PAIR IS A REFUSAL, NOT A WARNING.  A capture that is not HTTP 200
    for the live URL's page is refused before writing (exit 7): QUALITY 18 asks
    for a pair, and a pair with a missing half cannot be cited.

Everything else is the round-76 tool (`.ufo/waves/round-76/counters/
capture-evidence.py`), itself the round-75 successor: the extraction, the
folding tiers, the window and digest rule, the anchor binding, the PDF page
window, the challenge detector and the self-verification are unchanged, so a
counter reads a round-77 file with the same grammar it read round 76 with.  The
round-77 keys are appended to the header and every round-76 key keeps its
meaning; `http-status:`, `bytes:`, `sha256:`, `ua:` and `final-url:` now
describe the fetch named by `window-source:`.

Grammar written (round-73/75/76 keys first, in their order, then the round-77
keys; every earlier parser still reads the file):

  # evidence <id> -- claim C GATE (round 77)
  url:            the LIVE URL requested        (the row's live URL)
  ua:             User-Agent sent for the window source's fetch
  http:           HTTP status of that fetch
  bytes:          length of that fetch's body in bytes (this fetch only)
  sha256:         64-hex digest of those bytes
  fetched:        UTC ISO-8601 second of that fetch
  quote-found:    yes | no   (in the window source's text, after folding)
  quote-words:    whitespace tokens, `wc -w` reading
  quote-chars:    characters, `wc -m` reading
  visible-chars:  characters of the window source's extracted visible text
  window-scope:   excerpt | whole-document | none
  window:         chars=<n> min=<n> pad=<n> before=<n> after=<n>
                  anchor-before=<n> anchor-after=<n>
  window-sha256:  sha256 of the stored window line
  window-bytes:   byte length of that same string
  window-rule:    the hashing rule, restated inside the file
  quote-found-verbatim: yes | no  (exact substring of the extracted text)
  anchor-quote / anchor-quote-chars / anchor-quote-words
  anchor-found / anchor-in-window / anchor-char
  quote-in-anchor / quote-anchor-distance
  find / find-char / find-page / find-hits / page-count / window-pages
  quote-page / anchor-page   (round 77: the page each cited span sits on,
                  recorded because the stored window drops the form feeds)
  bytes-rule / claims-source / claims-frozen
  challenge / challenge-detail        (window source)
  content-type / final-url / extract  (window source)
  fetch / user-agent / access-date / http-status / content-length
  transferred-bytes / fetch-attempts / fetch-command
  locator / normalise / quote
  window-source:  live | wayback -- the fetch the window was cut from
  window-fetch:   GET <that fetch's URL>
  wayback-url:    the capture URL requested
  wayback-original:  the page the replay path says it captured
  wayback-same-page: yes | no -- normalised equality with `url:`
  wayback-final-original: the page embedded in the redirected replay URL
  wayback-final-same-page: yes | no
  wayback-timestamp: the timestamp token in the replay path
  wayback-modifier:  id_ / if_ / (empty)
  wayback-memento-datetime: the replay's Memento-Datetime, or `-`
  wayback-timestamp-matches: yes | nearest | -
  wayback-rule:   the QUALITY 18/22 rule, restated inside the file
  wayback-http / wayback-ua / wayback-bytes / wayback-sha256 / wayback-fetched
  wayback-final-url / wayback-content-type / wayback-challenge / wayback-extract
  wayback-quote-found / wayback-quote-found-verbatim
  live-http / live-ua / live-bytes / live-sha256 / live-fetched
  live-final-url / live-content-type / live-challenge / live-extract
  live-quote-found / live-quote-found-verbatim
  live-fetch-attempts / live-fetch-command / wayback-fetch-attempts
  wayback-fetch-command
  response-bind-live:     ua="..." -> http=... bytes=... sha256=... final-url=...
  response-bind-wayback:  ua="..." -> http=... bytes=... sha256=... final-url=...
                          memento=...
  --- window ---
  <ONE line: >=`min_window` chars of the window source's visible text around
   the quote (or around the --find locator), whitespace-collapsed>
  --- quote ---
  <the quote as supplied>

The window rule (claim C's EVIDENCE leg).  The window is stored as a single
whitespace-collapsed line, so "the window text" is unambiguous: the one line
between the `--- window ---` marker line and the `--- quote ---` marker line,
with no trailing newline.  `window-scope: excerpt` needs >= `min_window`
(default 4096) characters; when the whole extracted visible text is shorter the
tool stores the whole text, declares `whole-document`, and the verifier requires
the stored text to BE that whole text (`len(window) == visible-chars` and
`visible_chars < min_window`).  `window-sha256:` is the sha256 of those bytes as
UTF-8, `window-bytes:` their length; the verifier recomputes both from the
stored line and trusts no flag in the file.

Anchor binding (round 76, R75-M2).  `--anchor-quote` is the registry row's
anchor cell, the span the row says it mined.  The capture locates it in the
window source's document, cuts the window (around the quote, or around `--find`
when given) and REFUSES -- exit 7, nothing written -- when the anchor's fold
does not occur in the stored window's fold.

PDF windows (round 76).  A PDF body goes through `pdftotext -enc UTF-8`, whose
form feeds are kept, so page numbers come from the document itself: the window
is cut around the FIRST occurrence of `--find` in the whole decoded text, and
the file records the page of that occurrence, the page count and the page range
the window covers.  A PDF capture without `--find` is refused (exit 7).  The
S898 row (D2, an Onomastica PDF) is captured this way, live or from the capture.

Claims schema (the contract this tool reads; `--print-config` shows it):
  top level        {"round": 77, "base": "<rev>", "frozen": "YYYY-MM-DD",
                    "claims": [{"id": "C", ...}], "capture": {...}}
  capture block    {"access_date": "YYYY-MM-DD", "min_window": 4096,
                    "min_pad": 400, "default_pad": 400,
                    "evidence_dir": "reports/round-77/evidence",
                    "verdict_prefix": "ACCEPT-C-77",
                    "window_rule": "<text>", "ua": "Mozilla/5.0 ...",
                    "wayback_prefix": "https://web.archive.org/web",
                    "anchor_required": true, "find_required_for_pdf": true}
  The `capture` block may also sit inside claim C.  Round tokens (`round`,
  `base`, `access_date`) have NO literal fallback: an access date comes from the
  capture block, claim C `access_date`, an `opened YYYY-MM-DD` clause in claim
  C's text, or a top-level `frozen` date, in that order.  The grammar floors
  (min_window 4096, min_pad/default_pad 400), the browser UA, the archive prefix
  and the window rule fall back to the grammar constants when the claims do not
  override them, and the provenance says so.

Quote matching.  Tiers, strongest first: (1) exact substring of the extracted
text; (2) NFKC per character, every whitespace run collapsed to one space, ends
stripped; (3) the same with all whitespace removed; (4) and (5) repeat (2) and
(3) under NFKD.  A quote that matches only the whitespace-free tier is found and
written, but the capture exits 5: the counter's fold would not confirm it.

Fetching.  http(s) goes through curl with the browser-shaped User-Agent, `-L`,
`--compressed`, a 20 s connect timeout and a 90 s total.  Transport failures
(curl exit 7/18/28/35/52/55/56) are retried with backoff and `fetch-attempts:`
records how many runs it took.  HTTP-level failures are never retried: a 404 is
an answer.  A `file://` source is a local read (the selftest's fixtures).

Scratch.  Every temporary file lives under `--work`, else `$HYAKU_SCRATCH`,
else `$TMPDIR`, else the interpreter's temporary directory; the tool contains no
literal scratch root.  The directory is removed when the run ends.

Dependencies: python3 stdlib, plus `curl` for http(s) and `pdftotext` for PDF
bodies.  No third-party Python.

Exit codes: 0 written and self-verified; 2 fetch/extract/usage/claims error (no
file); 3 written but the quote is not in the window source's text; 4 written but
the window source's HTTP status is not 200; 5 written but self-verification
failed; 6 written but the served body is a bot challenge or interstitial -- the
challenge was MET, not passed, so the source is UNOPENED (QUALITY 10);
7 REFUSED before writing: the anchor span is absent from the document or from
the stored window, the locator string is absent, a PDF has no `--find`, the
capture is not the live page's capture, the capture did not answer 200 or served
no memento, the quote lies outside the window the locator names, or
`--window-from` names a fetch that cannot be cited.

Usage:
  capture-evidence.py --repo /path/to/lane --freeze <rev> --id S897 \
      --url <live url> --wayback-url <replay url> \
      --quote-file <span> --anchor-quote-file <anchor> --find "locator" \
      --out reports/round-77/evidence/S897.txt
  capture-evidence.py --repo /path/to/lane --freeze <rev> --id S897 \
      --url <live url> --wayback-timestamp 20240111092427 ...
  capture-evidence.py --repo /path/to/lane --freeze <rev> --verify <path>
  capture-evidence.py --selftest --work /fast/scratch/hyaku/kotodama-r77/<seat>
  capture-evidence.py --print-config --repo /path/to/lane --freeze <rev>

`--allow-file` exists for the selftest only: it lets `--verify` accept
`http-status: file`, which a graded capture must never carry.
`--claims-file` reads an uncommitted claims document (a pre-freeze rehearsal);
the file records `claims-frozen: no` and a counter may refuse it.
"""

import argparse
import hashlib
import html
import html.parser
import io
import json
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

# --------------------------------------------------------------------------
# constants
# --------------------------------------------------------------------------
# The claims path is the file's identity (it names the round), not a derived
# value: the round token itself is read from that file.
CLAIMS_PATH = "reports/round-77/claims.json"
CLAIM_ID = "C"

# Grammar constants.  These are the grammar's own floors, identical in every
# round since round 74 (R74-M6); the frozen claims may override them and
# `--print-config` prints which source won.
MIN_WINDOW_GRAMMAR = 4096
MIN_PAD_GRAMMAR = 400
DEFAULT_PAD_GRAMMAR = 400
WINDOW_RULE_GRAMMAR = ("sha256 of the single stored window line, UTF-8, "
                       "no trailing newline")
# Fleet constant (operator ruling): the browser-shaped User-Agent every fetch
# records.  A claims document may override it; the provenance says so.
UA_BROWSER = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
              "(KHTML, like Gecko) Chrome/130.0 Safari/537.36")
WAYBACK_PREFIX_GRAMMAR = "https://web.archive.org/web"

SKIP_TAGS = {"script", "style", "noscript", "template", "svg", "math", "head"}
BLOCK_TAGS = {
    "address", "article", "aside", "blockquote", "br", "dd", "details", "div",
    "dl", "dt", "fieldset", "figcaption", "figure", "footer", "form", "h1",
    "h2", "h3", "h4", "h5", "h6", "header", "hr", "li", "main", "nav", "ol",
    "p", "pre", "section", "table", "tbody", "td", "tfoot", "th", "thead",
    "tr", "ul", "caption", "summary",
}
ASCII_SPACE = re.compile(r"[ \t\r\f\v]+")
ROUND_MARK_RE = re.compile(r"\(round (\d+)\)")
PDF_WINDOW_RE = re.compile(r"^(\d+)\.\.(\d+)$")
# The replay path archive.org uses: /web/<timestamp>[id_|if_]/<original page>.
WAYBACK_RE = re.compile(r"^.*?/web/(\d{4,14})([a-z]{0,3}_)?(/.*)?$")
SCHEME_RE = re.compile(r"^[a-z][a-z0-9+.-]*://")
MEMENTO_FORMAT = "%a, %d %b %Y %H:%M:%S GMT"
BYTES_RULE = ("bytes:/sha256: describe the fetch named by window-source only; "
              "a byte count is not canonical across fetches (one URL served "
              "three counts in round 75), and the live and Wayback fetches are "
              "two observations of two requests with no shared count")
WAYBACK_RULE = ("a row's evidence is a live URL and a same-page Wayback "
                "capture: the replay path's embedded original, normalised "
                "(scheme, leading www., trailing slash dropped), must equal "
                "the live URL; and each fetch record binds the User-Agent "
                "actually sent to the response that request got "
                "(QUALITY 18, QUALITY 22)")

# Statuses a fetch can carry and still be cited: 200 over the wire, `file` for
# a local fixture read (selftest only, gated by --allow-file in --verify).
CITABLE_STATUSES = ("200", "file")


class CaptureError(Exception):
    """The capture could not be produced (fetch, decode or extraction)."""


class ClaimsError(Exception):
    """The frozen configuration is unusable: the counter refuses to capture."""


# --------------------------------------------------------------------------
# claims: the frozen configuration
# --------------------------------------------------------------------------

CAPTURE_ALIASES = {
    "access_date": ("access_date", "access-date", "accessDate"),
    "min_window": ("min_window", "min-window", "window_min",
                   "window_min_chars"),
    "min_pad": ("min_pad", "min-pad", "pad_min"),
    "default_pad": ("default_pad", "default-pad", "pad"),
    "evidence_dir": ("evidence_dir", "evidence-dir", "evidence"),
    "verdict_prefix": ("verdict_prefix", "verdict-prefix", "verdict"),
    "window_rule": ("window_rule", "window-rule"),
    "ua": ("ua", "user_agent", "user-agent"),
    "wayback_prefix": ("wayback_prefix", "wayback-prefix"),
    "anchor_required": ("anchor_required", "anchor-required"),
    "find_required_for_pdf": ("find_required_for_pdf", "find-required-for-pdf"),
}
DATE_RE = re.compile(r"\d{4}-\d{2}-\d{2}")


class Config:
    """The constants one capture or verification uses, with their provenance."""

    def __init__(self, round_token, base, access_date, min_window, min_pad,
                 default_pad, evidence_dir, verdict_prefix, window_rule, ua,
                 wayback_prefix, anchor_required, find_required_for_pdf,
                 claims_source, claims_frozen, provenance):
        self.round = round_token
        self.base = base
        self.access_date = access_date
        self.min_window = min_window
        self.min_pad = min_pad
        self.default_pad = default_pad
        self.evidence_dir = evidence_dir
        self.verdict_prefix = verdict_prefix
        self.window_rule = window_rule
        self.ua = ua
        self.wayback_prefix = wayback_prefix
        self.anchor_required = anchor_required
        self.find_required_for_pdf = find_required_for_pdf
        self.claims_source = claims_source
        self.claims_frozen = claims_frozen
        self.provenance = provenance

    def as_dict(self):
        return {
            "round": self.round,
            "base": self.base,
            "access_date": self.access_date,
            "min_window": self.min_window,
            "min_pad": self.min_pad,
            "default_pad": self.default_pad,
            "evidence_dir": self.evidence_dir,
            "verdict_prefix": self.verdict_prefix,
            "window_rule": self.window_rule,
            "ua": self.ua,
            "wayback_prefix": self.wayback_prefix,
            "anchor_required": self.anchor_required,
            "find_required_for_pdf": self.find_required_for_pdf,
            "claims_source": self.claims_source,
            "claims_frozen": self.claims_frozen,
            "provenance": self.provenance,
        }


def _git(repo, *args):
    """Run a read-only git command in `repo`; return the CompletedProcess."""
    return subprocess.run(["git", "-C", repo] + list(args),
                          capture_output=True)


def _lane_root(start):
    """The git top level of `start`, or None."""
    if not os.path.isdir(start):
        start = os.path.dirname(start)
    proc = _git(start, "rev-parse", "--show-toplevel")
    if proc.returncode == 0:
        root = proc.stdout.decode("utf-8", "replace").strip()
        if root:
            return root
    d = os.path.abspath(start)
    while True:
        if os.path.isdir(os.path.join(d, ".git")):
            return d
        nd = os.path.dirname(d)
        if nd == d:
            return None
        d = nd


def _claim_c(doc):
    """Claim C's object, whichever shape the frozen file uses."""
    claims = doc.get("claims")
    if isinstance(claims, list):
        for item in claims:
            if isinstance(item, dict) and str(item.get("id", "")).upper() == CLAIM_ID:
                return item
    if isinstance(claims, dict) and isinstance(claims.get(CLAIM_ID), dict):
        return claims[CLAIM_ID]
    if isinstance(doc.get(CLAIM_ID), dict):
        return doc[CLAIM_ID]
    return None


def _capture_blocks(doc):
    """Every mapping a capture constant may sit in, most specific first."""
    out = []
    for key in ("capture", "capture_config", "config"):
        if isinstance(doc.get(key), dict):
            out.append(("claims." + key, doc[key]))
    claim = _claim_c(doc)
    if claim is not None:
        for key in ("capture", "config"):
            if isinstance(claim.get(key), dict):
                out.append(("claim C." + key, claim[key]))
        out.append(("claim C", claim))
    out.append(("claims", doc))
    return out


def _lookup(doc, name):
    """(value, provenance) for a capture constant, aliases tried in order."""
    blocks = _capture_blocks(doc)
    for alias in CAPTURE_ALIASES[name]:
        for block_name, block in blocks:
            if alias in block and block[alias] not in (None, ""):
                return block[alias], "%s.%s" % (block_name, alias)
    return None, None


def _claim_text(doc):
    """Claim C's prose fields joined, for the fallbacks that read prose."""
    claim = _claim_c(doc)
    if not isinstance(claim, dict):
        return ""
    parts = []
    for key, value in claim.items():
        if isinstance(value, str):
            parts.append(value)
        elif isinstance(value, list):
            parts.extend(v for v in value if isinstance(v, str))
        elif isinstance(value, dict):
            parts.extend(v for v in value.values() if isinstance(v, str))
    return "\n".join(parts)


def _access_date_from_prose(doc):
    """A date clause in claim C's text, or a top-level `frozen` date."""
    text = _claim_text(doc)
    for pattern in (r"opened\s+(\d{4}-\d{2}-\d{2})",
                    r"access[- ]date[^0-9]{0,20}(\d{4}-\d{2}-\d{2})"):
        match = re.search(pattern, text, re.I)
        if match:
            return match.group(1), "claim C text (%s)" % pattern.split("(")[0].strip()
    frozen = doc.get("frozen")
    if isinstance(frozen, str):
        match = DATE_RE.fullmatch(frozen.strip())
        if match:
            return match.group(0), "claims.frozen"
    return None, None


def load_claims(args):
    """Resolve every constant from the frozen claims document.

    Default: `git -C <repo> show <freeze>:reports/round-77/claims.json`.
    `--claims-file` reads an uncommitted document (pre-freeze rehearsal) and
    records `claims-frozen: no`.
    """
    repo = args.repo or _lane_root(os.path.dirname(os.path.abspath(__file__)))
    if args.claims_file:
        path = os.path.abspath(args.claims_file)
        try:
            with open(path, "rb") as fh:
                raw = fh.read()
        except OSError as e:
            raise ClaimsError("cannot read --claims-file: %s" % e)
        shown = path
        if repo:
            try:
                rel = os.path.relpath(path, repo)
            except ValueError:
                rel = path
            if not rel.startswith(".."):
                shown = rel
        source = "file:%s sha256=%s" % (shown, hashlib.sha256(raw).hexdigest())
        frozen = "no"
    else:
        if not repo:
            raise ClaimsError("no git repository found for the claims document; "
                              "pass --repo")
        rev = args.freeze or "HEAD"
        proc = _git(repo, "show", "%s:%s" % (rev, CLAIMS_PATH))
        if proc.returncode != 0:
            raise ClaimsError("cannot read %s at %s in %s: %s"
                              % (CLAIMS_PATH, rev, repo,
                                 proc.stderr.decode("utf-8", "replace").strip()))
        raw = proc.stdout
        source = "git show %s:%s" % (rev, CLAIMS_PATH)
        frozen = "yes"
    try:
        doc = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, ValueError) as e:
        raise ClaimsError("%s is not UTF-8 JSON: %s" % (source, e))
    if not isinstance(doc, dict):
        raise ClaimsError("%s is not a JSON object" % source)
    return resolve_config(doc, source, frozen)


def resolve_config(doc, source, frozen):
    """Read the round tokens from `doc`; refuse rather than invent a token."""
    prov = {}
    round_raw = doc.get("round")
    if isinstance(round_raw, bool) or not isinstance(round_raw, (int, str)):
        raise ClaimsError("%s carries no integer `round` (read from %s)"
                          % (source, source))
    round_text = str(round_raw).strip()
    if not round_text.isdigit():
        raise ClaimsError("claims.round %r is not an integer" % (round_raw,))
    round_token = int(round_text)
    prov["round"] = "claims.round"

    base = doc.get("base")
    if not isinstance(base, str) or not base.strip():
        raise ClaimsError("claims.base is missing: a receipt is never graded "
                          "against an unnamed base")
    base = base.strip()
    if not re.fullmatch(r"[0-9a-f]{7,40}", base):
        raise ClaimsError("claims.base %r is not a git revision" % base[:60])
    prov["base"] = "claims.base"

    access_date, access_src = _lookup(doc, "access_date")
    if access_date is None:
        access_date, access_src = _access_date_from_prose(doc)
    if access_date is None:
        raise ClaimsError("no access date in the claims document: put "
                          "capture.access_date (YYYY-MM-DD), a claim-C "
                          "access_date, an `opened YYYY-MM-DD` clause or a "
                          "top-level `frozen` date in %s" % source)
    access_date = str(access_date).strip()
    if not DATE_RE.fullmatch(access_date):
        raise ClaimsError("access date %r is not YYYY-MM-DD" % access_date)
    prov["access_date"] = access_src

    def number(name, fallback):
        value, src = _lookup(doc, name)
        if value is None:
            prov[name] = "grammar default"
            return fallback
        try:
            number_value = int(value)
        except (TypeError, ValueError):
            raise ClaimsError("capture.%s %r is not an integer" % (name, value))
        if number_value <= 0:
            raise ClaimsError("capture.%s %r is not positive" % (name, value))
        prov[name] = src
        return number_value

    min_window = number("min_window", MIN_WINDOW_GRAMMAR)
    min_pad = number("min_pad", MIN_PAD_GRAMMAR)
    default_pad = number("default_pad", DEFAULT_PAD_GRAMMAR)

    def text_constant(name, fallback):
        value, src = _lookup(doc, name)
        if value is None:
            prov[name] = "grammar default"
            return fallback
        prov[name] = src
        return str(value).strip()

    evidence_dir = text_constant(
        "evidence_dir", "reports/round-%d/evidence" % round_token)
    verdict_prefix = text_constant(
        "verdict_prefix", "ACCEPT-C-%d" % round_token)
    window_rule = text_constant("window_rule", WINDOW_RULE_GRAMMAR)
    ua = text_constant("ua", UA_BROWSER)
    wayback_prefix = text_constant("wayback_prefix", WAYBACK_PREFIX_GRAMMAR)

    def flag(name, fallback):
        value, src = _lookup(doc, name)
        if value is None:
            prov[name] = "fix default (round 76)"
            return fallback
        prov[name] = src
        if isinstance(value, bool):
            return value
        return str(value).strip().lower() in ("1", "true", "yes", "on")

    anchor_required = flag("anchor_required", True)
    find_required_for_pdf = flag("find_required_for_pdf", True)

    return Config(round_token, base, access_date, min_window, min_pad,
                  default_pad, evidence_dir, verdict_prefix, window_rule, ua,
                  wayback_prefix, anchor_required, find_required_for_pdf,
                  source, frozen, prov)


# --------------------------------------------------------------------------
# scratch
# --------------------------------------------------------------------------

def work_base(explicit):
    """The scratch root: --work, else $HYAKU_SCRATCH, else $TMPDIR, else the
    interpreter's temporary directory (tempfile honours TMPDIR itself)."""
    for candidate in (explicit, os.environ.get("HYAKU_SCRATCH"),
                      os.environ.get("TMPDIR")):
        if candidate:
            path = os.path.abspath(os.path.expanduser(candidate))
            os.makedirs(path, exist_ok=True)
            return path
    return None


def make_work_dir(explicit, prefix="capture-evidence-"):
    return tempfile.mkdtemp(prefix=prefix, dir=work_base(explicit))


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


def fetch(url, ua, work, retries=2, tag="body"):
    """Fetch `url`; return a dict with body bytes and the served metadata.

    `tag` names this fetch's scratch files, so the live and the Wayback fetch
    of one receipt never overwrite each other.

    Transport failures (curl exit 7/18/28/35/52/55/56) are retried `retries`
    times with a short backoff: one origin reset connections and aborted TLS
    handshakes intermittently in round 75, and a transient reset must not decide
    a Gate.  HTTP-level failures are never retried: a 404 is an answer.
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
            "memento": "-",
            "fetched": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        }

    body_path = os.path.join(work, "body-%s.bin" % tag)
    header_path = os.path.join(work, "headers-%s.txt" % tag)
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
        "memento": headers.get("memento-datetime", "-"),
        "fetched": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
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


def detect_challenge(body, content_type, text):
    """Name the bot challenge / interstitial a body carries, or None.

    QUALITY 10: a source is OPENED only when it was reached by ordinary means.
    A body that is a captcha, a JS proof-of-work wall, a "please verify you are
    human" interstitial or a login wall was NOT opened -- it is a challenge that
    was met, not one that was passed.  The capture tool records what the server
    actually served, so the challenge must be visible in the evidence file
    rather than silently producing an empty window.

    Two tiers, because a raw-HTML keyword is not the same as a wall:

    (1) STRONG markers -- the body IS the interstitial.  These are checked in
        the raw bytes because the interstitial's own text is what a reader
        would see, and the served page has almost no other content.

    (2) SOFT markers -- "captcha", "login", "consent", "geo".  These are
        checked in the VISIBLE text only, and only when that visible text is
        short (an interstitial has little to say).  A real article page may
        legitimately carry a hidden download widget, a "Se connecter" nav link
        or a cookie notice; none of those make the page a wall.
    """
    ctype = (content_type or "").lower()
    raw = body[:200000].decode("latin-1", "replace").lower()
    visible = (text or "").strip()
    vis_low = visible.lower()

    for needle, label in (
            ("enable javascript and cookies to continue", "js-challenge"),
            ("checking your browser before accessing", "js-challenge"),
            ("cf-browser-verification", "js-challenge"),
            ("incapsula incident id", "js-challenge"),
            ("ddos protection by", "js-challenge"),
            ("just a moment", "js-challenge"),
            ("attention required! | cloudflare", "js-challenge"),
            ("enable javascript to run this app", "js-challenge"),
    ):
        if needle in raw:
            return (label, "the body carries %r" % needle)

    if len(visible) < 3000:
        for needle, label in (
                ("captcha", "captcha"),
                ("verify you are human", "captcha"),
                ("are you a robot", "captcha"),
                ("i am not a robot", "captcha"),
                ("sign in to continue", "login-wall"),
                ("please log in", "login-wall"),
                ("log in to read", "login-wall"),
                ("cookies must be enabled", "consent-wall"),
                ("accept cookies to continue", "consent-wall"),
                ("not available in your country", "geo-wall"),
                ("not available in your region", "geo-wall"),
        ):
            if needle in vis_low:
                return (label, "the visible text carries %r" % needle)

    if ctype.startswith("text/html") and not visible:
        return ("js-challenge",
                "the HTML body yielded no visible text (%d bytes served)" % len(body))
    if not visible and len(body) < 4096:
        return ("empty-body",
                "the body is %d bytes and yielded no visible text" % len(body))
    return (None, "")


def extract_text(body, content_type, work, tag="body"):
    """Return (text, extract-line description)."""
    ctype = (content_type or "").lower()
    if ctype.startswith("application/pdf") or body[:5] == b"%PDF-":
        body_path = os.path.join(work, "body-%s.pdf" % tag)
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
        # split on "\n" only: str.splitlines() would also split on the form
        # feeds pdftotext writes between pages, and page numbers come from them
        text = "\n".join(line.rstrip(" \t") for line in text.split("\n"))
        return text, ("pdftotext -enc UTF-8 BODY - (stdlib subprocess, form "
                      "feeds kept for page numbers); %d chars, %d page(s)"
                      % (len(text), page_count(text)))

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
# pages (PDF)
# --------------------------------------------------------------------------

def page_at(text, offset):
    """1-based page of `offset`, counting the form feeds pdftotext writes."""
    return 1 + text.count("\f", 0, max(0, offset))


def page_count(text):
    """Pages with visible content in a decoded document."""
    return sum(1 for page in text.split("\f") if page.strip())


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


def folded_has(haystack, needle):
    """The counter's containment test, verbatim."""
    needle_fold = nfkc_ws(needle)
    return bool(needle_fold) and needle_fold in nfkc_ws(haystack)


def count_fold(text, needle):
    """Occurrences of `needle` in `text` after the counter's fold."""
    needle_fold = nfkc_ws(needle)
    if not needle_fold:
        return 0
    return nfkc_ws(text).count(needle_fold)


def make_window(text, hit, pad, min_window):
    """Whitespace-collapsed window of >= min_window chars around `hit`.

    Returns (window_text, start, end) with the source offsets, so the caller can
    name the pages the window covers.  Symmetric where the text allows it; near
    a document edge the window slides into the remaining text so the minimum is
    still met when the document is long enough.  A document shorter than the
    minimum yields its whole text and the caller declares whole-document.
    """
    span = hit["end"] - hit["start"]
    want = max(pad, (min_window - span) // 2 + 4)
    start = max(0, hit["start"] - want)
    end = min(len(text), hit["end"] + want)
    for _ in range(16):
        chunk = collapse(text[start:end])
        if len(chunk) >= min_window or (start == 0 and end == len(text)):
            return chunk, start, end
        need = min_window - len(chunk) + 2
        if end < len(text) and (start == 0 or end + need <= len(text)):
            end = min(len(text), end + need)
        elif start > 0:
            start = max(0, start - need)
        else:
            return chunk, start, end
    return collapse(text[start:end]), start, end


# --------------------------------------------------------------------------
# same-page capture (round 77)
# --------------------------------------------------------------------------

def norm_url(url):
    """Comparison key for same-page: host (no `www.`), path, query.

    Archive.org serves the same page under `http`, `https`, `www.` and no
    `www.` interchangeably (a replay of `https://example.com/` redirected to
    `http://www.example.com/` in the round-77 probe), so the key drops the
    scheme, a leading `www.`, a default port and a trailing slash.  The path
    and the query are kept: a capture of another page is another page.
    """
    parts = urllib.parse.urlsplit(url.strip())
    host = (parts.hostname or "").lower()
    if host.startswith("www."):
        host = host[4:]
    try:
        port = parts.port
    except ValueError:
        port = None
    if port and not ((parts.scheme == "http" and port == 80)
                     or (parts.scheme == "https" and port == 443)):
        host = "%s:%d" % (host, port)
    path = parts.path or "/"
    if path != "/":
        path = path.rstrip("/") or "/"
    query = ("?" + parts.query) if parts.query else ""
    return host + path + query


def same_page(live_url, original):
    """Whether `original` (read out of a replay path) is the live URL's page."""
    if not original:
        return False
    a, b = norm_url(live_url), norm_url(original)
    if a == b:
        return True
    return (urllib.parse.unquote(a) == urllib.parse.unquote(b))


def wayback_parts(wayback_url, live_url):
    """(timestamp, modifier, original) read out of a replay URL, or None.

    archive.org names the captured page inside the replay path:
    `/web/<timestamp>[id_|if_]/<original>`.  The original is read from the URL
    we asked for -- never from a caller flag -- so the same-page check is made
    against the artifact that was fetched.  A scheme-less original
    (`/web/2024.../host/path`, which archive.org also serves) takes the live
    URL's scheme; a `file://` live URL must embed a full `file://` original.
    """
    parts = urllib.parse.urlsplit(wayback_url)
    match = WAYBACK_RE.match(parts.path)
    if not match:
        return None
    timestamp = match.group(1)
    modifier = match.group(2) or ""
    rest = (match.group(3) or "")[1:]          # drop the single leading '/'
    if not rest:
        return None
    if parts.query and "?" not in rest:
        rest += "?" + parts.query
    if SCHEME_RE.match(rest):
        original = rest
    else:
        scheme = urllib.parse.urlsplit(live_url).scheme
        if scheme not in ("http", "https"):
            return None
        original = "%s://%s" % (scheme, rest)
    return {"timestamp": timestamp, "modifier": modifier, "original": original}


def replay_url(prefix, timestamp, url):
    """`<prefix>/<timestamp>id_/<url>`: the exact-bytes replay of `url`.

    `id_` is archive.org's identity modifier: it returns the archived bytes
    without the replay banner and without rewriting the page's links, which is
    what makes the capture comparable with the live fetch.
    """
    return "%s/%sid_/%s" % (prefix.rstrip("/"), timestamp.strip(), url)


def memento_stamp(value):
    """`Thu, 11 Jan 2024 09:28:27 GMT` -> `20240111092827`, or None."""
    if not value or value == "-":
        return None
    try:
        when = datetime.strptime(value.strip(), MEMENTO_FORMAT)
    except ValueError:
        return None
    return when.strftime("%Y%m%d%H%M%S")


def timestamp_relation(requested, stamp):
    """yes | nearest | - : does the served memento match the requested stamp.

    archive.org redirects an uncaptured second to the nearest capture, so
    `nearest` is a normal, datable answer and the memento states the truth.
    """
    if not stamp:
        return "-"
    if not requested:
        return "nearest"
    want = re.sub(r"[^0-9]", "", requested)
    if want and stamp.startswith(want[:len(want)]):
        return "yes"
    return "nearest"


class Source:
    """One fetch: what it was served, what that decodes to, and the hits in it.

    `ok` is the status fact, `citable` adds "not a challenge wall".  The two
    fetches of a round-77 receipt are two independent Sources; which one the
    window is cut from is chosen in `capture()` and recorded as
    `window-source:`.
    """

    def __init__(self, kind, url, meta, text, extract_line, quote, anchor, find):
        self.kind = kind
        self.url = url
        self.meta = meta
        self.text = text
        self.extract = extract_line
        self.challenge, self.challenge_detail = detect_challenge(
            meta["body"], meta["content_type"], text)
        self.visible = collapse(text)
        self.is_pdf = ((meta["content_type"] or "").lower().startswith("application/pdf")
                       or meta["body"][:5] == b"%PDF-")
        self.hit = locate(text, quote)
        self.anchor_hit = (locate(text, anchor) if anchor
                           else {"found": False, "verbatim": False, "form": None,
                                 "tier": None, "start": None, "end": None})
        self.find_hit = locate(text, find) if find else None
        self.ok = meta["http"] in CITABLE_STATUSES
        self.citable = self.ok and not self.challenge

    def header(self, name):
        return (self.meta["headers"] or {}).get(name, "-")

    def digest(self):
        return hashlib.sha256(self.meta["body"]).hexdigest()

    def bytes(self):
        return len(self.meta["body"])


# --------------------------------------------------------------------------
# render
# --------------------------------------------------------------------------

def _relative_window_position(window_text, span):
    """(before, after) of `span` inside the stored window, or (-1, -1)."""
    hit = locate(window_text, span)
    if not hit["found"]:
        return -1, -1
    return hit["start"], len(window_text) - hit["end"]


def _source_lines(src):
    """The per-fetch atoms of one fetch, ending with its UA->response bind line.

    QUALITY 22: the bind line holds the User-Agent actually sent and the
    response that request received (`http`, `bytes`, `sha256`, `final-url`), so
    the pairing is one record rather than two lists a reader has to trust are
    parallel.  The atoms above it repeat the same values for machine reading.
    """
    bind = ('ua="%s" -> http=%s bytes=%d sha256=%s final-url=%s'
            % (src.meta["ua_sent"], src.meta["http"], src.bytes(),
               src.digest(), src.meta["final_url"]))
    if src.kind == "wayback":
        bind += " memento=%s" % (src.meta["memento"] or "-")
    return [
        "%s-http: %s" % (src.kind, src.meta["http"]),
        "%s-final-url: %s" % (src.kind, src.meta["final_url"]),
        "%s-ua: %s" % (src.kind, src.meta["ua_sent"]),
        "%s-bytes: %d" % (src.kind, src.bytes()),
        "%s-sha256: %s" % (src.kind, src.digest()),
        "%s-fetched: %s" % (src.kind, src.meta.get("fetched", "-")),
        "%s-content-type: %s" % (src.kind, src.meta["content_type"] or "unknown"),
        "%s-challenge: %s" % (src.kind, src.challenge or "none"),
        "%s-extract: %s" % (src.kind, src.extract),
        "%s-quote-found: %s" % (src.kind, "yes" if src.hit["found"] else "no"),
        "%s-quote-found-verbatim: %s"
        % (src.kind, "yes" if src.hit["verbatim"] else "no"),
        "%s-fetch-attempts: %d" % (src.kind, src.meta["attempts"]),
        "%s-fetch-command: %s" % (src.kind, src.meta["command"]),
        "response-bind-%s: %s" % (src.kind, bind),
    ]


def render(ident, live, wb, chosen, bind, quote, hit, locator, pad,
           min_window, window_text, scope, cfg, access_date=None):
    """Build the evidence file text and the window digest."""
    digest = chosen.digest()
    now = datetime.now(timezone.utc)
    fetched = chosen.meta.get("fetched") or now.strftime("%Y-%m-%dT%H:%M:%SZ")
    content_length = chosen.header("content-length")
    if hit["found"] and window_text:
        window_bytes = window_text.encode("utf-8")
        window_digest = hashlib.sha256(window_bytes).hexdigest()
        before, after = _relative_window_position(window_text, quote)
        anchor_before, anchor_after = _relative_window_position(
            window_text, bind["anchor"])
        window_line = ("window: chars=%d min=%d pad=%d before=%d after=%d "
                       "anchor-before=%d anchor-after=%d"
                       % (len(window_text), min_window, pad, before, after,
                          anchor_before, anchor_after))
        normalise = ("normalise: %s(per-character)+whitespace-fold; matched=%s"
                     % (hit["form"], hit["tier"]))
    else:
        window_text = ""
        window_bytes = b""
        window_digest = hashlib.sha256(window_bytes).hexdigest()
        window_line = ("window: chars=0 min=%d pad=%d before=n/a after=n/a "
                       "anchor-before=n/a anchor-after=n/a"
                       % (min_window, pad))
        normalise = "normalise: NFKC,NFKD(per-character)+whitespace-fold; matched=none"

    quote_line = collapse(quote)
    anchor_line = collapse(bind["anchor"])
    in_window = bool(window_text) and folded_has(window_text, bind["anchor"])
    quote_in_anchor = ("yes" if hit["found"] and folded_has(bind["anchor"], quote)
                       else "no")
    distance = "-"
    if window_text:
        qhit = locate(window_text, quote)
        ahit = locate(window_text, bind["anchor"])
        if qhit["found"] and ahit["found"]:
            distance = str(abs(qhit["start"] - ahit["start"]))
    challenge, challenge_detail = chosen.challenge, chosen.challenge_detail
    wb_facts = bind["wayback"]

    lines = [
        "# evidence %s — claim C GATE (round %d)" % (ident, cfg.round),
        "url: %s" % live.url,
        "ua: %s" % chosen.meta["ua_sent"],
        "http: %s" % chosen.meta["http"],
        "bytes: %d" % len(chosen.meta["body"]),
        "sha256: %s" % digest,
        "fetched: %s" % fetched,
        "quote-found: %s" % ("yes" if hit["found"] else "no"),
        "quote-words: %d" % len(quote.split()),
        "quote-chars: %d" % len(quote),
        "visible-chars: %d" % len(chosen.visible),
        "window-scope: %s" % scope,
        window_line,
        "window-sha256: %s" % window_digest,
        "window-bytes: %d" % len(window_bytes),
        "window-rule: %s" % cfg.window_rule,
        "quote-found-verbatim: %s" % ("yes" if hit["verbatim"] else "no"),
        "anchor-quote: %s" % anchor_line,
        "anchor-quote-chars: %d" % len(anchor_line),
        "anchor-quote-words: %d" % len(anchor_line.split()),
        "anchor-found: %s" % ("yes" if bind["anchor_hit"]["found"] else "no"),
        "anchor-in-window: %s" % ("yes" if in_window else "no"),
        "anchor-char: %s" % (str(bind["anchor_hit"]["start"])
                             if bind["anchor_hit"]["found"] else "-"),
        "quote-in-anchor: %s" % quote_in_anchor,
        "quote-anchor-distance: %s" % distance,
        "find: %s" % bind["find_line"],
        "find-char: %s" % bind["find_char"],
        "find-page: %s" % bind["find_page"],
        "find-hits: %d" % bind["find_hits"],
        "page-count: %s" % bind["page_count"],
        "window-pages: %s" % bind["window_pages"],
        "quote-page: %s" % bind["quote_page"],
        "anchor-page: %s" % bind["anchor_page"],
        "bytes-rule: %s" % BYTES_RULE,
        "claims-source: %s" % cfg.claims_source,
        "claims-frozen: %s" % cfg.claims_frozen,
        "challenge: %s" % (challenge or "none"),
        "challenge-detail: %s" % (challenge_detail or "(none)"),
        "content-type: %s" % (chosen.meta["content_type"] or "unknown"),
        "final-url: %s" % chosen.meta["final_url"],
        "extract: %s" % chosen.extract,
        "fetch: GET %s" % live.url,
        "user-agent: %s" % chosen.meta["ua_sent"],
        "access-date: %s" % (access_date or cfg.access_date),
        "http-status: %s" % chosen.meta["http"],
        "content-length: %s" % content_length,
        "transferred-bytes: %d" % chosen.meta["transferred"],
        "fetch-attempts: %d" % chosen.meta["attempts"],
        "fetch-command: %s" % chosen.meta["command"],
        "locator: %s" % (locator or "(none supplied)"),
        normalise,
        "quote: %s" % quote_line,
        "window-source: %s" % chosen.kind,
        "window-fetch: GET %s" % chosen.url,
        "wayback-url: %s" % (wb.url if wb is not None else "(none supplied)"),
        "wayback-original: %s" % (wb_facts["original"] or "-"),
        "wayback-same-page: %s" % wb_facts["same_page"],
        "wayback-final-original: %s" % (wb_facts["final_original"] or "-"),
        "wayback-final-same-page: %s" % wb_facts["final_same_page"],
        "wayback-timestamp: %s" % (wb_facts["timestamp"] or "-"),
        "wayback-modifier: %s" % (wb_facts["modifier"] or "-"),
        "wayback-memento-datetime: %s" % (wb_facts["memento"] or "-"),
        "wayback-timestamp-matches: %s" % wb_facts["timestamp_matches"],
        "wayback-rule: %s" % WAYBACK_RULE,
    ]
    lines.extend(_source_lines(live))
    if wb is not None:
        lines.extend(_source_lines(wb))
    lines.extend([
        "--- window ---",
        window_text,
        "--- quote ---",
        quote,
    ])
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


BASE_KEYS = ("url", "fetch", "user-agent", "access-date", "http-status",
             "bytes", "sha256", "locator", "quote-words", "quote-chars",
             "window-sha256", "window-bytes", "window-scope", "visible-chars")
R75_KEYS = BASE_KEYS + ("challenge",)
R76_KEYS = R75_KEYS + ("anchor-quote", "anchor-quote-chars", "anchor-found",
                       "anchor-in-window", "bytes-rule", "claims-source",
                       "claims-frozen")
R77_KEYS = R76_KEYS + ("window-source", "window-fetch", "wayback-url",
                       "wayback-original", "wayback-same-page",
                       "wayback-final-original", "wayback-final-same-page",
                       "wayback-timestamp", "wayback-memento-datetime",
                       "wayback-timestamp-matches", "wayback-rule",
                       "wayback-http", "wayback-ua", "wayback-bytes",
                       "wayback-sha256", "wayback-fetched", "wayback-final-url",
                       "wayback-challenge", "wayback-quote-found",
                       "wayback-quote-found-verbatim", "live-http", "live-ua",
                       "live-bytes", "live-sha256", "live-fetched",
                       "live-final-url", "live-challenge", "live-quote-found",
                       "live-quote-found-verbatim", "response-bind-live",
                       "response-bind-wayback", "quote-page", "anchor-page")
PDF_KEYS = ("find", "find-char", "find-page", "find-hits", "page-count",
            "window-pages")
UA_ROBOT_RE = re.compile(
    r"(?i)(?:curl/|wget/|python-requests|python-urllib|libwww|scrapy"
    r"|go-http-client|phantomjs|headless|spider|crawler)")


def _declared_round(text):
    for line in text.splitlines()[:3]:
        match = ROUND_MARK_RE.search(line)
        if match:
            return int(match.group(1))
    return None


def _ua_ok(ua):
    return ua.startswith("Mozilla/5.0") and not UA_ROBOT_RE.search(ua)


def verify_file(path, cfg, quote=None, anchor=None, min_window=None,
                allow_file=False):
    """Re-read an evidence file and check it the way the counter will.

    Returns (problems, header, window).  Checks: the required keys exist; the
    window source's status is 200 and the access date is the claims' date; the
    stored window is one line of >= min_window characters; its sha256 and byte
    length match the header; the quote occurs in it after whole-string NFKC +
    whitespace folding; the ROW'S ANCHOR SPAN occurs in it too; and -- round 77
    -- the receipt holds two fetches, the capture is the live page's capture
    with a datable memento, and each fetch's bind line pairs the UA it recorded
    with the response it recorded.

    The scope rule: `window-scope: excerpt` needs >= min_window characters and
    cannot exceed the whole text; `window-scope: whole-document` is allowed only
    when the whole extracted visible text is shorter than min_window, and then
    the stored window must BE that whole text -- its length must equal
    `visible-chars:`, written by the same run from the same extraction.
    """
    min_window = cfg.min_window if min_window is None else min_window
    try:
        with open(path, "r", encoding="utf-8") as fh:
            text = fh.read()
    except OSError as e:
        return ["cannot read %s: %s" % (path, e)], {}, ""
    head = parse_evidence(text)
    win = stored_window(text)
    problems = []
    declared = _declared_round(text)
    if declared is None:
        problems.append("the first lines do not name the round (`# evidence "
                        "<id> — claim C GATE (round N)`)")
    elif declared != cfg.round:
        problems.append("the file names round %d but the frozen configuration "
                        "is round %d" % (declared, cfg.round))
    is_r76 = declared is not None and declared >= 76
    is_r77 = declared is not None and declared >= 77
    for key in (R77_KEYS if is_r77 else (R76_KEYS if is_r76 else R75_KEYS)):
        if not head.get(key):
            problems.append("missing header key %r" % key)
    status = (head.get("http-status") or head.get("http") or "").strip()
    if status != "200" and not (allow_file and status == "file"):
        problems.append("http-status %r (want 200)" % status)
    if head.get("access-date") != cfg.access_date:
        problems.append("access-date %r (want %s)"
                        % (head.get("access-date"), cfg.access_date))
    ua = (head.get("user-agent") or head.get("ua") or "").strip()
    if status == "200":
        if not ua.startswith("Mozilla/5.0"):
            problems.append("user-agent is not browser-shaped: %r" % ua[:40])
        elif UA_ROBOT_RE.search(ua):
            problems.append("user-agent carries a client/robot token: %r" % ua[:60])
    fetch = (head.get("fetch") or "").strip()
    if fetch and head.get("url") and head["url"].strip() not in fetch:
        problems.append("fetch line does not name `url:`: %r" % fetch[:70])
    if win is None:
        problems.append("no --- window --- block")
        return problems, head, ""
    payload = win.encode("utf-8")
    recomputed = hashlib.sha256(payload).hexdigest()
    if head.get("window-sha256") != recomputed:
        problems.append("window-sha256 mismatch: header %r recomputed %s"
                        % (head.get("window-sha256"), recomputed))
    if head.get("window-bytes") != str(len(payload)):
        problems.append("window-bytes %r (stored %d)"
                        % (head.get("window-bytes"), len(payload)))
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
    wanted = quote if quote is not None else (stored_quote(text).strip()
                                              or head.get("quote", ""))
    if not wanted:
        problems.append("no quote to check")
    elif not folded_has(win, wanted):
        problems.append("quote absent from the stored window after NFKC+whitespace fold")
    if is_r76:
        wanted_anchor = (anchor if anchor is not None
                         else head.get("anchor-quote", ""))
        if not wanted_anchor:
            problems.append("no anchor-quote to check (R75-M2: the receipt must "
                            "carry the row's anchor span)")
        else:
            if head.get("anchor-found") != "yes":
                problems.append("anchor-found %r (want yes)"
                                % head.get("anchor-found"))
            if head.get("anchor-in-window") != "yes":
                problems.append("anchor-in-window %r (want yes)"
                                % head.get("anchor-in-window"))
            if head.get("anchor-quote-chars") != str(len(collapse(wanted_anchor))):
                problems.append("anchor-quote-chars %r != the stored anchor's %d"
                                % (head.get("anchor-quote-chars"),
                                   len(collapse(wanted_anchor))))
            if not folded_has(win, wanted_anchor):
                problems.append("the anchor span is absent from the stored "
                                "window after NFKC+whitespace fold (R75-M2)")
        ctype = (head.get("content-type") or "").lower()
        is_pdf = "application/pdf" in ctype or "pdftotext" in (head.get("extract") or "")
        if is_pdf:
            for key in PDF_KEYS:
                if not head.get(key):
                    problems.append("PDF evidence lacks %r" % key)
            match = PDF_WINDOW_RE.match((head.get("window-pages") or "").strip())
            if not match:
                problems.append("window-pages %r is not `a..b`"
                                % (head.get("window-pages"),))
            else:
                first, last = int(match.group(1)), int(match.group(2))
                find_page = (head.get("find-page") or "").strip()
                if not find_page.isdigit():
                    problems.append("find-page %r is not a page number"
                                    % (head.get("find-page"),))
                elif not (first <= int(find_page) <= last):
                    problems.append("find-page %s is outside window-pages %s..%s"
                                    % (find_page, first, last))
                if first < 1 or last < first:
                    problems.append("window-pages %s..%s is not an increasing "
                                    "page range" % (first, last))
                if is_r77:
                    # The page each cited span sits on is recorded because the
                    # counter cannot recompute it from the stored window (the
                    # form feeds are stripped): grading it against window-pages
                    # is what makes "the window reached p. 4" checkable.
                    for name in ("quote-page", "anchor-page"):
                        page_value = (head.get(name) or "").strip()
                        if not page_value.isdigit():
                            problems.append("%s %r is not a page number"
                                            % (name, page_value))
                        elif not (first <= int(page_value) <= last):
                            problems.append("%s %s is outside window-pages "
                                            "%s..%s: the stored window did not "
                                            "reach the span it cites"
                                            % (name, page_value, first, last))
        if (head.get("find") or "").strip().lower().startswith("(none supplied)") \
                and is_pdf:
            problems.append("a PDF capture carries no locator: the window must "
                            "be cut by --find, never by the head")
    if is_r77:
        problems.extend(_verify_round77(head, allow_file))
    challenge = (head.get("challenge") or "").strip().lower()
    if challenge and challenge != "none":
        problems.append("the served body carries a %s challenge (%s): the "
                        "source was met, not opened"
                        % (challenge, head.get("challenge-detail", "")[:80]))
    return problems, head, win


def _verify_round77(head, allow_file):
    """The round-77 legs: the pair, the same-page proof and the UA bindings.

    `window-source:` says which fetch the top-level atoms describe, so their
    equality with that fetch's own atoms is checked rather than assumed: a
    receipt whose window came from the capture must not also claim the live
    fetch's status.  A challenged LIVE fetch is allowed only when the window
    came from the capture -- that is D1/S897's shape, where the live page is a
    403 wall and the ordinary-means copy is the capture.
    """
    problems = []
    source = (head.get("window-source") or "").strip()
    if source not in ("live", "wayback"):
        return ["window-source %r (want live or wayback)"
                % head.get("window-source")]
    for top, sub in (("http-status", "http"), ("bytes", "bytes"),
                     ("sha256", "sha256"), ("user-agent", "ua"),
                     ("final-url", "final-url"), ("fetched", "fetched")):
        got = head.get("%s-%s" % (source, sub)) or ""
        if (head.get(top) or "") != got:
            problems.append("`%s:` %r does not match `%s-%s:` %r: the top-level "
                            "atoms must describe the window source"
                            % (top, head.get(top), source, sub, got))
    wanted_fetch = "GET " + (head.get("wayback-url" if source == "wayback"
                                      else "url") or "")
    if (head.get("window-fetch") or "").strip() != wanted_fetch:
        problems.append("window-fetch %r (want %r)"
                        % (head.get("window-fetch"), wanted_fetch))
    if head.get("wayback-same-page") != "yes":
        problems.append("wayback-same-page %r (want yes): the capture is not a "
                        "capture of `url:`" % head.get("wayback-same-page"))
    if not same_page(head.get("url", ""), head.get("wayback-original")):
        problems.append("wayback-original %r is not the page `url:` names"
                        % (head.get("wayback-original"),))
    if head.get("wayback-final-same-page") != "yes":
        problems.append("wayback-final-same-page %r (want yes): the replay "
                        "redirected away from the live page"
                        % head.get("wayback-final-same-page"))
    wb_status = (head.get("wayback-http") or "").strip()
    if wb_status != "200" and not (allow_file and wb_status == "file"):
        problems.append("wayback-http %r (want 200): QUALITY 18 asks for a live "
                        "URL AND a capture, and a capture that did not answer "
                        "is not half of a pair" % wb_status)
    if not memento_stamp(head.get("wayback-memento-datetime")):
        problems.append("wayback-memento-datetime %r is not a memento date: the "
                        "capture cannot be dated"
                        % head.get("wayback-memento-datetime"))
    if (head.get("wayback-timestamp-matches") or "").strip() not in ("yes",
                                                                     "nearest"):
        problems.append("wayback-timestamp-matches %r (want yes or nearest)"
                        % head.get("wayback-timestamp-matches"))
    for kind in ("live", "wayback"):
        line = head.get("response-bind-" + kind) or ""
        recorded_ua = head.get("%s-ua" % kind) or ""
        recorded_http = head.get("%s-http" % kind) or ""
        recorded_digest = head.get("%s-sha256" % kind) or ""
        if not line:
            problems.append("missing header key 'response-bind-%s'" % kind)
            continue
        if ('ua="%s"' % recorded_ua) not in line:
            problems.append("response-bind-%s does not bind the recorded UA (%r)"
                            % (kind, recorded_ua[:40]))
        if "http=%s" % recorded_http not in line or recorded_digest not in line:
            problems.append("response-bind-%s does not bind the response the "
                            "fetch recorded (http=%s, its sha256)"
                            % (kind, recorded_http))
        if recorded_http == "200" and not _ua_ok(recorded_ua):
            problems.append("%s fetch UA is not browser-shaped: %r"
                            % (kind, recorded_ua[:40]))
    live_challenge = (head.get("live-challenge") or "none").strip().lower()
    if live_challenge not in ("", "none") and source != "wayback":
        problems.append("the live fetch carries a %s challenge and the window "
                        "was not cut from the capture" % live_challenge)
    return problems


def head_challenge(text):
    """The `challenge:` header value of an evidence document, or None."""
    for line in text.splitlines():
        match = re.match(r"^challenge:\s*(.*)$", line)
        if match:
            return match.group(1).strip()
    return None


def verify_command(args, cfg):
    quote = None
    if args.quote or args.quote_file:
        quote = read_span(args, "quote", "quote_file", "quote")
    anchor = None
    if args.anchor_quote or args.anchor_quote_file:
        anchor = read_span(args, "anchor_quote", "anchor_quote_file",
                           "anchor-quote")
    problems, head, win = verify_file(args.verify, cfg, quote, anchor,
                                      args.min_window if args.min_window else None,
                                      args.allow_file)
    for problem in problems:
        print("VERIFY %s: %s" % (args.verify, problem), file=sys.stderr)
    if problems:
        print("%s: VERIFY FAIL: %s (%d problem(s))"
              % (cfg.verdict_prefix, args.verify, len(problems)))
        return 5
    print("VERIFY OK: %s window-sha256=%s window-bytes=%d window-chars=%d "
          "quote-in-window=yes anchor-in-window=%s window-source=%s "
          "wayback-same-page=%s wayback-memento=%s access-date=%s "
          "http-status=%s"
          % (args.verify, head["window-sha256"], len(win.encode("utf-8")),
             len(win), head.get("anchor-in-window", "n/a"),
             head.get("window-source", "n/a"),
             head.get("wayback-same-page", "n/a"),
             head.get("wayback-memento-datetime", "n/a"),
             head["access-date"], head["http-status"]))
    return 0


# --------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------

def parse_args(argv):
    ap = argparse.ArgumentParser(
        prog="capture-evidence.py",
        description="Capture a live URL and its same-page Wayback capture into "
                    "a round-77 evidence file. The round tokens come from the "
                    "frozen claims.json (--repo/--freeze).")
    ap.add_argument("--id", help="evidence id (default: the --out file stem)")
    ap.add_argument("--url", help="the LIVE URL to fetch (http(s)://, "
                                  "file:// or a path)")
    group = ap.add_mutually_exclusive_group()
    group.add_argument("--quote", help="the quoted span, verbatim")
    group.add_argument("--quote-file", help="file holding the quoted span")
    agroup = ap.add_mutually_exclusive_group()
    agroup.add_argument("--anchor-quote",
                        help="the registry row's ANCHOR span (round 76, "
                             "R75-M2): required for a capture, and required to "
                             "occur in the stored window")
    agroup.add_argument("--anchor-quote-file",
                        help="file holding the row's anchor span")
    fgroup = ap.add_mutually_exclusive_group()
    fgroup.add_argument("--find",
                        help="locator string: the window is cut around its "
                             "first occurrence in the whole document (required "
                             "for a PDF, where it names the page)")
    fgroup.add_argument("--find-file", help="file holding the locator string")
    wgroup = ap.add_mutually_exclusive_group()
    wgroup.add_argument("--wayback-url",
                        help="the capture's replay URL "
                             "(<prefix>/web/<ts>id_/<the live url>)")
    wgroup.add_argument("--wayback-timestamp",
                        help="the capture timestamp (YYYY[MMDD[hhmmss]]): the "
                             "replay URL is built from wayback_prefix (default "
                             "https://web.archive.org/web) and --url")
    ap.add_argument("--wayback-ua", default=None,
                    help="User-Agent for the capture fetch (default: the same "
                         "as --ua; recorded per fetch either way)")
    ap.add_argument("--window-from", choices=("live", "wayback"), default=None,
                    help="which fetch to cut the window from (default: the "
                         "live fetch when it answered 200 without a challenge "
                         "and carries the quote, else the capture)")
    ap.add_argument("--out", help="evidence file to write (<evidence_dir>/<id>.txt)")
    ap.add_argument("--locator", default="", help="where the quote sits in the page")
    ap.add_argument("--ua", default=None,
                    help="User-Agent to send (recorded verbatim; default from "
                         "the claims, else the browser-shaped fleet constant)")
    ap.add_argument("--retries", type=int, default=2,
                    help="retries after a transient curl transport failure "
                         "(default 2; HTTP errors are never retried)")
    ap.add_argument("--pad", type=int, default=None,
                    help="floor for the symmetric window pad (default and "
                         "minimum from the claims, else 400)")
    ap.add_argument("--min-window", type=int, default=None,
                    help="minimum stored window characters (default and "
                         "minimum from the claims, else 4096)")
    ap.add_argument("--access-date", default=None,
                    help="the access date to record (YYYY-MM-DD); it must equal "
                         "the claims' access date, because the counter grades "
                         "against that date")
    ap.add_argument("--repo", default=None,
                    help="the lane repository holding the frozen claims "
                         "(default: the tool's git top level)")
    ap.add_argument("--freeze", default=None,
                    help="the revision holding reports/round-77/claims.json "
                         "(default: HEAD)")
    ap.add_argument("--claims-file", default=None,
                    help="read an UNCOMMITTED claims document instead of "
                         "`git show <freeze>:...` (pre-freeze rehearsal only; "
                         "the file records `claims-frozen: no`)")
    ap.add_argument("--work", default=None,
                    help="scratch root (default: $HYAKU_SCRATCH, else $TMPDIR, "
                         "else the interpreter's temporary directory)")
    ap.add_argument("--print-config", action="store_true",
                    help="print the resolved constants and their provenance")
    ap.add_argument("--verify", metavar="PATH",
                    help="re-verify an existing evidence file and exit")
    ap.add_argument("--allow-file", action="store_true",
                    help="with --verify: accept `http-status: file` (local "
                         "fixtures only; a graded capture must be HTTP 200)")
    ap.add_argument("--selftest", action="store_true", help="run the fixture suite")
    args = ap.parse_args(argv)

    if args.selftest:
        return args
    if args.id and not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]*", args.id):
        ap.error("--id %r is not a file-stem id" % args.id)
    if args.verify:
        return args
    if args.print_config:
        return args
    missing = [name for name in ("url", "out")
               if not getattr(args, name)]
    if not (args.quote or args.quote_file):
        missing.append("quote|quote-file")
    if not (args.wayback_url or args.wayback_timestamp):
        missing.append("wayback-url|wayback-timestamp (QUALITY 18: a row's "
                       "evidence is a live URL AND its same-page capture)")
    if missing:
        ap.error("missing required argument(s): %s" % ", ".join(missing))
    return args


def read_span(args, inline_attr, file_attr, name):
    path = getattr(args, file_attr, None)
    if path:
        try:
            with open(path, "r", encoding="utf-8") as fh:
                value = fh.read()
        except OSError as e:
            raise CaptureError("cannot read --%s: %s" % (file_attr.replace("_", "-"), e))
    else:
        value = getattr(args, inline_attr, None) or ""
    value = value.strip()
    if not value:
        raise CaptureError("%s is empty" % name)
    return value


def _refuse(cfg, ident, reason):
    print("%s: REFUSED %s: %s" % (cfg.verdict_prefix, ident, reason),
          file=sys.stderr)
    return 7


def main(argv):
    args = parse_args(argv)
    if args.selftest:
        return selftest(args)
    try:
        cfg = load_claims(args)
        if args.print_config:
            print(json.dumps(cfg.as_dict(), indent=1, sort_keys=True))
            return 0
        if args.verify:
            return verify_command(args, cfg)
        return capture(args, cfg)
    except (CaptureError, ClaimsError) as e:
        print("ERROR: %s" % e, file=sys.stderr)
        return 2


# --------------------------------------------------------------------------
# capture
# --------------------------------------------------------------------------

def capture(args, cfg):
    quote = read_span(args, "quote", "quote_file", "quote")
    anchor = ""
    if args.anchor_quote or args.anchor_quote_file:
        anchor = read_span(args, "anchor_quote", "anchor_quote_file",
                           "anchor-quote")
    if cfg.anchor_required and not anchor:
        raise CaptureError("--anchor-quote is required: the receipt binds the "
                           "stored quote to the row's anchor span (R75-M2)")
    find = ""
    if args.find or args.find_file:
        find = read_span(args, "find", "find_file", "find")
    ident = args.id or os.path.splitext(os.path.basename(args.out))[0]
    min_window = args.min_window if args.min_window else cfg.min_window
    pad = args.pad if args.pad else cfg.default_pad
    if min_window < cfg.min_window:
        raise ClaimsError("--min-window %d is below the frozen minimum of %d "
                          "(capture.min_window)" % (min_window, cfg.min_window))
    if pad < cfg.min_pad:
        raise ClaimsError("--pad %d is below the frozen minimum of %d "
                          "(capture.min_pad)" % (pad, cfg.min_pad))
    access_date = args.access_date or cfg.access_date
    if access_date != cfg.access_date:
        raise ClaimsError("--access-date %r differs from the claims' %r: the "
                          "counter grades against the frozen date"
                          % (access_date, cfg.access_date))

    wb_url = (args.wayback_url if args.wayback_url
              else replay_url(cfg.wayback_prefix, args.wayback_timestamp,
                              args.url))
    wb_parts = wayback_parts(wb_url, args.url)
    if wb_parts is None:
        return _refuse(cfg, ident,
                       "the capture URL %r does not carry a replay path "
                       "(`/web/<timestamp>[id_]/<the live url>`): the fetch "
                       "would prove nothing about `url:`" % wb_url)
    wb_original = wb_parts["original"]
    wb_same = same_page(args.url, wb_original)

    work = make_work_dir(args.work)
    try:
        meta_live = fetch(args.url, args.ua or cfg.ua, work, args.retries,
                          "live")
        meta_wb = fetch(wb_url, args.wayback_ua or args.ua or cfg.ua, work,
                        args.retries, "wayback")
        text_live, extract_live = extract_text(
            meta_live["body"], meta_live["content_type"], work, "live")
        text_wb, extract_wb = extract_text(
            meta_wb["body"], meta_wb["content_type"], work, "wayback")
        live = Source("live", args.url, meta_live, text_live, extract_live,
                      quote, anchor, find)
        wb = Source("wayback", wb_url, meta_wb, text_wb, extract_wb,
                    quote, anchor, find)

        # Which fetch the window comes from.  The live web wins when it answers
        # and carries the quote; otherwise the capture is the opened document
        # (that is D1/S897: the live page is a 403 wall, the capture is the
        # ordinary-means copy).  `--window-from` overrides; the choice is
        # recorded, never assumed.
        if args.window_from == "live":
            chosen = live
        elif args.window_from == "wayback":
            chosen = wb
        else:
            chosen = None
            for candidate in (live, wb):
                if candidate.citable and candidate.hit["found"]:
                    chosen = candidate
                    break
            if chosen is None:
                chosen = live if not live.challenge else wb
        wall = chosen.challenge

        if not wb_same:
            return _refuse(cfg, ident,
                           "the capture embeds %r, which is not the page "
                           "`url:` names (%r) after normalising scheme, a "
                           "leading www. and a trailing slash: a capture of "
                           "another page is not this row's capture"
                           % (wb_original, args.url))
        wb_final = wayback_parts(meta_wb["final_url"], args.url)
        final_original = wb_final["original"] if wb_final else None
        final_same = ("yes" if same_page(args.url, final_original)
                      else ("no" if final_original else "-"))
        wb_facts = {
            "original": wb_original,
            "same_page": "yes",
            "final_original": final_original,
            "final_same_page": final_same,
            "timestamp": wb_parts["timestamp"],
            "modifier": wb_parts["modifier"],
            "memento": meta_wb["memento"] or "-",
            "timestamp_matches": timestamp_relation(
                wb_parts["timestamp"], memento_stamp(meta_wb["memento"])),
        }
        # A wall is recorded, not passed (QUALITY 10): when the served body IS
        # the interstitial, the run writes the file and exits 6, so the pair
        # gates below do not hide it.
        if not wall:
            if meta_wb["http"] != "200":
                return _refuse(cfg, ident,
                               "the same-page capture answered HTTP %s (want "
                               "200): QUALITY 18 asks for a live URL AND a "
                               "capture, and half a pair is not evidence"
                               % meta_wb["http"])
            if not memento_stamp(wb_facts["memento"]):
                return _refuse(cfg, ident,
                               "the capture served no Memento-Datetime "
                               "(headers: %s): a copy nobody can date is not "
                               "evidence"
                               % ", ".join(sorted(meta_wb["headers"]))[:120])
            if wb_facts["final_same_page"] != "yes":
                return _refuse(cfg, ident,
                               "the replay redirected to %r, which is not the "
                               "live page: the capture that is cited is not "
                               "the capture that was served"
                               % (meta_wb["final_url"],))
        if chosen.is_pdf and not find and cfg.find_required_for_pdf:
            return _refuse(cfg, ident,
                           "a PDF capture needs --find: the window is cut by "
                           "the locator's page (its first occurrence in the "
                           "whole decoded document), never by the head")
        if cfg.anchor_required and not chosen.anchor_hit["found"] and not wall:
            other = live if chosen is wb else wb
            return _refuse(cfg, ident,
                           "the row's anchor span is absent from the window "
                           "source's text (%d characters decoded from %s): the "
                           "anchor is not on the opened document%s"
                           % (len(chosen.visible), chosen.kind,
                              "" if other.anchor_hit["found"] else
                              " (and not on the other fetch either)"))
        if chosen.find_hit is not None and not chosen.find_hit["found"]:
            return _refuse(cfg, ident,
                           "the locator string is absent from the decoded "
                           "document (%d characters from %s): --find names a "
                           "page the document does not carry"
                           % (len(chosen.visible), chosen.kind))
        if not chosen.hit["found"]:
            scope = "none"
            window_text, wstart, wend = "", 0, 0
        elif len(chosen.visible) < min_window:
            scope = "whole-document"
            window_text, wstart, wend = chosen.visible, 0, len(chosen.text)
        else:
            scope = "excerpt"
            centre = chosen.find_hit if chosen.find_hit else chosen.hit
            window_text, wstart, wend = make_window(chosen.text, centre, pad,
                                                    min_window)
        if window_text and not wall:
            if not folded_has(window_text, anchor):
                where = ("the anchor sits at char %d and the window covers "
                         "chars %d-%d" % (chosen.anchor_hit["start"], wstart,
                                          wend)
                         if chosen.anchor_hit["found"] else "the anchor was not located")
                return _refuse(cfg, ident,
                               "the row's anchor span is absent from the stored "
                               "window after NFKC+whitespace folding (%s): cut "
                               "the window with --find on the anchor's page, or "
                               "raise --pad" % where)
            if chosen.hit["found"] and not folded_has(window_text, quote):
                return _refuse(cfg, ident,
                               "the quote is absent from the window cut around "
                               "the locator (char %d): the quote and the "
                               "locator name different places"
                               % (chosen.find_hit["start"]
                                  if chosen.find_hit else -1))
        if chosen.is_pdf:
            find_page = (str(page_at(chosen.text, chosen.find_hit["start"]))
                         if chosen.find_hit else "-")
            window_pages = ("%d..%d" % (page_at(chosen.text, wstart),
                                        page_at(chosen.text, max(wstart, wend - 1)))
                            if window_text else "-")
            page_total = str(page_count(chosen.text))
            # The page each cited span actually sits on.  The counter cannot
            # recompute these from the stored window (form feeds are stripped),
            # so without them "the window reached the quote's page" is prose.
            quote_page = (str(page_at(chosen.text, chosen.hit["start"]))
                          if chosen.hit["found"] else "-")
            anchor_page = (str(page_at(chosen.text, chosen.anchor_hit["start"]))
                           if chosen.anchor_hit["found"] else "-")
        else:
            find_page, window_pages, page_total = "-", "-", "-"
            quote_page, anchor_page = "-", "-"
        bind = {
            "anchor": anchor,
            "anchor_hit": chosen.anchor_hit,
            "find_line": ("%s (first occurrence at char %d of %d)"
                          % (collapse(find), chosen.find_hit["start"],
                             len(chosen.text))
                          if chosen.find_hit else "(none supplied)"),
            "find_char": (str(chosen.find_hit["start"])
                          if chosen.find_hit else "-"),
            "find_page": find_page,
            "find_hits": count_fold(chosen.text, find) if find else 0,
            "page_count": page_total,
            "window_pages": window_pages,
            "quote_page": quote_page,
            "anchor_page": anchor_page,
            "wayback": wb_facts,
        }
        document, digest, window_digest = render(
            ident, live, wb, chosen, bind, quote, chosen.hit, args.locator,
            pad, min_window, window_text, scope, cfg, access_date)
        out_dir = os.path.dirname(os.path.abspath(args.out))
        if out_dir:
            os.makedirs(out_dir, exist_ok=True)
        with open(args.out, "w", encoding="utf-8") as fh:
            fh.write(document)
        print("EVIDENCE %s: quote-found=%s verbatim=%s anchor-in-window=%s "
              "window-source=%s live-http=%s wayback-http=%s "
              "wayback-same-page=yes memento=%s bytes=%d sha256=%s "
              "window-chars=%d window-scope=%s window-sha256=%s find-page=%s "
              "-> %s"
              % (ident, "yes" if chosen.hit["found"] else "no",
                 "yes" if chosen.hit["verbatim"] else "no",
                 "yes" if (window_text and folded_has(window_text, anchor)) else "no",
                 chosen.kind, meta_live["http"], meta_wb["http"],
                 wb_facts["memento"], len(chosen.meta["body"]), digest[:16],
                 len(window_text), scope, window_digest[:16], find_page,
                 args.out))
        if chosen.meta["http"] not in CITABLE_STATUSES:
            print("EVIDENCE %s: HTTP %s is not 200 — the capture is not citable"
                  % (ident, chosen.meta["http"]), file=sys.stderr)
            return 4
        challenge = (head_challenge(document) or "").strip().lower()
        if challenge and challenge != "none":
            print("EVIDENCE %s: the served body carries a %s challenge — the "
                  "challenge was MET, not passed, so the source is UNOPENED "
                  "and the capture is not citable" % (ident, challenge),
                  file=sys.stderr)
            return 6
        if not chosen.hit["found"]:
            print("EVIDENCE %s: quote not found in the extracted text — the "
                  "capture is not citable" % ident, file=sys.stderr)
            return 3
        problems, head, win = verify_file(
            args.out, cfg, quote, anchor, min_window,
            allow_file=(chosen.meta["http"] == "file"))
        for problem in problems:
            print("EVIDENCE %s: verify: %s" % (ident, problem), file=sys.stderr)
        if problems:
            print("%s: VERIFY FAIL: %s (%d problem(s)); the file was left on disk"
                  % (cfg.verdict_prefix, args.out, len(problems)))
            return 5
        print("VERIFY OK: %s window-sha256=%s window-bytes=%d window-chars=%d "
              "quote-in-window=yes anchor-in-window=yes window-source=%s "
              "wayback-same-page=yes wayback-memento=%s"
              % (args.out, head["window-sha256"], len(win.encode("utf-8")),
                 len(win), head["window-source"],
                 head["wayback-memento-datetime"]))
        print("%s: CAPTURE OK: %s window-sha256=%s window-bytes=%d "
              "window-chars=%d quote-in-window=yes anchor-in-window=yes "
              "window-source=%s wayback-same-page=yes "
              "wayback-memento=%s claims-frozen=%s"
              % (cfg.verdict_prefix, args.out, head["window-sha256"],
                 len(win.encode("utf-8")), len(win), head["window-source"],
                 head["wayback-memento-datetime"], cfg.claims_frozen))
        return 0
    finally:
        shutil.rmtree(work, ignore_errors=True)


# --------------------------------------------------------------------------
# selftest
# --------------------------------------------------------------------------

FILLER = "見出しの前後の本文です。" * 400       # 4400 chars, CJK
CJK_QUOTE = "世界観の作り方は、一つの場所に集めることです。"
CJK_ANCHOR = "世界観の作り方は、一つの場所に集めることです。"
SPACED_QUOTE = "設定ノートの構成例 です。"
SPACED_ANCHOR = "設定ノートの構成例 です。"
LATIN_QUOTE = "The settings note holds five sections in one file."
LATIN_ANCHOR = "The settings note holds five sections in one file."
EDGE_QUOTE = "冒頭の一文です。"
SHORT_QUOTE = "短い文書の一文です。"
NARR_QUOTE = "ナレーション理論は、物語の構造を記述する学問である。"
NARR_ANCHOR = "ナレーション理論は、物語の構造を記述する学問である。"
FAR_ANCHOR = "この錨は窓の外にある遠い段落です。"
WALL_BODY = "<html><body><p>Access denied.</p></body></html>"


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
<p>ナレーション理論は、物語の構造を記述する学問である。</p>
<!-- COMMENT_ONLY_TEXT -->
</body></html>
""" % (FILLER, CJK_ANCHOR, FILLER)


def _fixture_edge_html():
    return ("<html><body><p>%s</p><p>%s</p></body></html>"
            % (EDGE_QUOTE, FILLER))


def _fixture_short_html():
    return ("<html><body><p>%s</p><p>ほんの少しの本文です。</p></body></html>"
            % SHORT_QUOTE)


def _fixture_challenge_html():
    return ("<html><head><title>Checking your browser</title></head>"
            "<body><div>Please enable JavaScript and cookies to continue.</div>"
            "</body></html>")


def _fixture_far_anchor_html():
    """A long body whose quote sits at the head and whose anchor sits 6000+
    characters later: the default 4096-character window cannot reach it."""
    middle = "".join("<p>%s 段落 %03d</p>" % (FILLER[:400], number)
                     for number in range(20))
    return ("<html><body><p>%s</p><p>%s</p>%s</body></html>"
            % (CJK_QUOTE, "前置きの段落です。", middle) + "<p>%s</p>" % FAR_ANCHOR)


def _pdf(pages):
    """A PDF whose `pages` are lists of 60 text lines each; xref offsets
    computed.  `pdftotext` writes a form feed between pages, which is what the
    page numbers are derived from."""
    contents = []
    for lines in pages:
        body = ["BT /F1 6 Tf 7 TL 36 740 Td"]
        for line in lines:
            body.append("(%s) Tj T*" % line)
        body.append("ET")
        contents.append("\n".join(body).encode("ascii"))
    count = len(pages)
    font_id = 3 + 2 * count
    kids = " ".join("%d 0 R" % (3 + 2 * index) for index in range(count))
    objects = [b"<</Type/Catalog/Pages 2 0 R>>",
               ("<</Type/Pages/Kids[%s]/Count %d>>" % (kids, count)).encode()]
    for index in range(count):
        objects.append(("<</Type/Page/Parent 2 0 R/MediaBox[0 0 612 792]"
                        "/Resources<</Font<</F1 %d 0 R>>>>/Contents %d 0 R>>"
                        % (font_id, 4 + 2 * index)).encode())
        objects.append(b"<</Length %d>>stream\n%s\nendstream"
                       % (len(contents[index]), contents[index]))
    objects.append(b"<</Type/Font/Subtype/Type1/BaseFont/Helvetica>>")
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


def _pdf_pages(quote, anchor, locator_on_page=None):
    """Six pages of 60 lines; the quote and anchor sit on page 5, and the
    locator marker sits on page 2 and (when asked) on page 5 as well."""
    pages = []
    for page in range(1, 7):
        lines = []
        for number in range(60):
            if page == 2 and number == 10:
                lines.append("LOCATOR-MARKER page two")
            elif page == 5 and number == 10:
                lines.append("LOCATOR-MARKER page five" if locator_on_page == 5
                             else "LOCATOR-MARKER absent here")
            elif page == 5 and number == 20:
                lines.append(quote)
            elif page == 5 and number == 21:
                lines.append(anchor)
            else:
                lines.append("Evidence window filler line page %d line %03d"
                             % (page, number))
        pages.append(lines)
    return pages


class _FixtureHandler(BaseHTTPRequestHandler):
    """Serves the selftest's routes and records the User-Agent of each request.

    `/flaky.html` sends a body shorter than its Content-Length the first
    `flaky["left"]` times, to exercise the transport retry.
    """

    routes = {}
    seen = []
    flaky = {"left": 0}

    def do_GET(self):                      # noqa: N802 - http.server API
        _FixtureHandler.seen.append((self.path, self.headers.get("User-Agent")))
        if self.path == "/flaky.html" and _FixtureHandler.flaky["left"] > 0:
            _FixtureHandler.flaky["left"] -= 1
            body = _FixtureHandler.routes["/fixture.html"][2]
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body) + 5000))
            self.end_headers()
            try:
                self.wfile.write(body)
            except OSError:
                pass
            self.close_connection = True
            return
        route = _FixtureHandler.routes.get(self.path)
        if route is None:
            body = b"<html><body><p>no such route</p></body></html>"
            self.send_response(404)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        status, ctype, body, extra = route
        self.send_response(status)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        for name, value in extra.items():
            self.send_header(name, value)
        self.end_headers()
        if body:
            self.wfile.write(body)

    def log_message(self, *args):          # silence the selftest's stderr
        pass


MEMENTO_HEADER = {"Memento-Datetime": "Thu, 11 Jan 2024 09:24:27 GMT"}


def _read(path):
    with open(path, "r", encoding="utf-8") as fh:
        return fh.read()


def _run(argv):
    """Run main() in-process, capturing stdout/stderr."""
    out, err = io.StringIO(), io.StringIO()
    with redirect_stdout(out), redirect_stderr(err):
        try:
            code = main(argv)
        except SystemExit as e:            # argparse usage errors
            code = e.code if isinstance(e.code, int) else 2
    return code, out.getvalue(), err.getvalue()


def _fixture_repo(root, claims, message):
    """A throwaway git repo holding reports/round-77/claims.json; returns its
    path and HEAD revision.  The identity is scoped to these commits only."""
    path = os.path.join(root, "claims-repo")
    if not os.path.isdir(os.path.join(path, ".git")):
        os.makedirs(path)
        subprocess.run(["git", "-C", path, "init", "-q"], check=True)
        top = subprocess.run(["git", "-C", path, "rev-parse", "--show-toplevel"],
                             capture_output=True, text=True)
        if os.path.realpath(top.stdout.strip()) != os.path.realpath(path):
            raise RuntimeError("fixture repo top level is %r, not %r"
                               % (top.stdout.strip(), path))
    target = os.path.join(path, CLAIMS_PATH)
    os.makedirs(os.path.dirname(target), exist_ok=True)
    with open(target, "w", encoding="utf-8") as fh:
        json.dump(claims, fh, indent=1, ensure_ascii=False)
    subprocess.run(["git", "-C", path, "add", "--", CLAIMS_PATH], check=True)
    subprocess.run(["git", "-C", path, "-c", "user.name=fixture",
                    "-c", "user.email=fixture@invalid", "commit", "-q",
                    "-m", message], check=True)
    rev = subprocess.run(["git", "-C", path, "rev-parse", "HEAD"],
                         capture_output=True, text=True, check=True)
    return path, rev.stdout.strip()


def _claims_doc(**overrides):
    doc = {
        "round": 77,
        "base": "211f9526800906e0c585d878d265c37e5e090c15",
        "frozen": "2026-10-27",
        "claims": [{"id": "C", "axis": "coverage",
                    "title": "Chinese naming system, assimilation-sourced"}],
        "capture": {
            "access_date": "2026-10-27",
            "min_window": 4096,
            "min_pad": 400,
            "default_pad": 400,
            "evidence_dir": "reports/round-77/evidence",
            "verdict_prefix": "ACCEPT-C-77",
            "window_rule": WINDOW_RULE_GRAMMAR,
            "ua": UA_BROWSER,
            "wayback_prefix": WAYBACK_PREFIX_GRAMMAR,
            "anchor_required": True,
            "find_required_for_pdf": True,
        },
    }
    for key, value in overrides.items():
        if key == "capture":
            doc["capture"].update(value)
        else:
            doc[key] = value
    return doc


def selftest(args):
    tmp = make_work_dir(args.work, "capture-evidence-selftest-")
    results = []

    def check(name, ok, detail=""):
        results.append((name, bool(ok), detail))
        return bool(ok)

    server = ThreadingHTTPServer(("127.0.0.1", 0), _FixtureHandler)
    base = "http://127.0.0.1:%d" % server.server_address[1]
    html = _fixture_html().encode("utf-8")
    pdf_bytes = _pdf(_pdf_pages("PDF fixture quote sentence.",
                                "PDF fixture anchor span.", locator_on_page=5))
    routes = {
        "/fixture.html": (200, "text/html; charset=utf-8", html, {}),
        "/edge.html": (200, "text/html; charset=utf-8",
                       _fixture_edge_html().encode("utf-8"), {}),
        "/short.html": (200, "text/html; charset=utf-8",
                        _fixture_short_html().encode("utf-8"), {}),
        "/far.html": (200, "text/html; charset=utf-8",
                      _fixture_far_anchor_html().encode("utf-8"), {}),
        "/challenge.html": (200, "text/html; charset=utf-8",
                            _fixture_challenge_html().encode("utf-8"), {}),
        "/challenge2.html": (200, "text/html; charset=utf-8",
                             _fixture_challenge_html().encode("utf-8"), {}),
        "/wall.html": (403, "text/html; charset=utf-8",
                       WALL_BODY.encode("utf-8"), {}),
        "/pdf.pdf": (200, "application/pdf", pdf_bytes, {}),
        "/missing.html": (404, "text/html; charset=utf-8",
                          b"<html><body><p>not here</p></body></html>", {}),
        "/uncaptured.html": (200, "text/html; charset=utf-8", html, {}),
        "/nomemento.html": (200, "text/html; charset=utf-8", html, {}),
        "/flaky.html": (200, "text/html; charset=utf-8", html, {}),
        "/other.html": (200, "text/html; charset=utf-8",
                        b"<html><body><p>other page</p></body></html>", {}),
    }

    def wb_path(live_path, ts="20240111092427"):
        return "/web/%sid_/%s%s" % (ts, base, live_path)

    # The capture of each page is the page's own bytes plus a memento, except:
    # /challenge.html's capture is clean (D1's shape: wall live, clean capture),
    # /challenge2.html's capture is a wall too, /wall.html's capture is the
    # article the live server refuses, and /missing.html's capture still answers.
    for path in ("/fixture.html", "/edge.html", "/short.html", "/far.html",
                 "/pdf.pdf", "/nomemento.html", "/flaky.html",
                 "/challenge2.html"):
        if path == "/nomemento.html":
            routes[wb_path(path)] = (200, "text/html; charset=utf-8", html, {})
            continue
        status, ctype, body, _ = routes[path]
        routes[wb_path(path)] = (200, ctype, body, dict(MEMENTO_HEADER))
    routes[wb_path("/challenge.html")] = (200, "text/html; charset=utf-8", html,
                                          dict(MEMENTO_HEADER))
    routes[wb_path("/wall.html")] = (200, "text/html; charset=utf-8", html,
                                     dict(MEMENTO_HEADER))
    routes[wb_path("/missing.html")] = (
        200, "text/html; charset=utf-8", routes["/missing.html"][2],
        dict(MEMENTO_HEADER))
    routes[wb_path("/other.html")] = (200, "text/html; charset=utf-8",
                                      routes["/other.html"][2],
                                      dict(MEMENTO_HEADER))
    _FixtureHandler.routes = routes
    _FixtureHandler.seen = []
    _FixtureHandler.flaky["left"] = 0
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()

    def wb(live_path, ts="20240111092427"):
        return base + wb_path(live_path, ts)

    def headers(path):
        return parse_evidence(_read(path)) if os.path.exists(path) else {}

    ev = os.path.join(tmp, "evidence")
    os.makedirs(ev, exist_ok=True)

    try:
        repo, rev = _fixture_repo(
            tmp, _claims_doc(capture={"wayback_prefix": base + "/web"}),
            "r77 claims fixture")
        common = ["--repo", repo, "--freeze", rev]
        live_fixture = base + "/fixture.html"

        # 0. the tool contains no literal scratch root
        source = _read(os.path.abspath(__file__))
        # the needle is composed so this check does not carry the literal it bans
        banned = "/" + "tmp"
        check("no-tmp-literal",
              source and ('"' + banned) not in source
              and (banned + "/") not in source,
              "source carries a literal scratch root")

        # 1. claims are read through `git show <freeze>:reports/round-77/claims.json`
        code, outlog, err = _run(common + ["--print-config"])
        conf = json.loads(outlog) if outlog.strip().startswith("{") else {}
        check("claims-git-read",
              code == 0 and conf.get("round") == 77
              and conf.get("claims_frozen") == "yes"
              and conf.get("access_date") == "2026-10-27"
              and conf.get("evidence_dir") == "reports/round-77/evidence"
              and conf.get("verdict_prefix") == "ACCEPT-C-77"
              and conf.get("wayback_prefix") == base + "/web"
              and conf.get("base", "").startswith("211f9526")
              and conf.get("provenance", {}).get("access_date")
              == "claims.capture.access_date"
              and conf.get("provenance", {}).get("wayback_prefix")
              == "claims.capture.wayback_prefix"
              and "git show %s:%s" % (rev, CLAIMS_PATH) == conf.get("claims_source"),
              "exit=%d conf=%r err=%r" % (code, conf, err.strip()[:120]))

        # 2a. an access-date mismatch is refused (exit 2, no file)
        out2a = os.path.join(ev, "V0.txt")
        code, _, err = _run(common + ["--url", live_fixture,
                                      "--wayback-url", wb("/fixture.html"),
                                      "--quote", CJK_QUOTE,
                                      "--anchor-quote", CJK_ANCHOR,
                                      "--out", out2a,
                                      "--access-date", "2026-10-26"])
        check("claims-constant-refusal",
              code == 2 and not os.path.exists(out2a)
              and "differs from the claims" in err,
              "exit=%d err=%r" % (code, err.strip()[:120]))

        # 2b. a claims variant moves the constants: access date, min window
        repo2, rev2 = _fixture_repo(
            tmp, _claims_doc(capture={"access_date": "2026-11-01",
                                      "min_window": 8192,
                                      "evidence_dir": "reports/round-77/alt",
                                      "verdict_prefix": "ACCEPT-C-77-ALT",
                                      "wayback_prefix": base + "/web"}),
            "r77 claims variant")
        out2 = os.path.join(ev, "V1.txt")
        code, outlog, err = _run(["--repo", repo2, "--freeze", rev2,
                                  "--url", live_fixture,
                                  "--wayback-url", wb("/fixture.html"),
                                  "--quote", CJK_QUOTE,
                                  "--anchor-quote", CJK_ANCHOR, "--out", out2])
        head2 = headers(out2)
        win2 = stored_window(_read(out2)) if os.path.exists(out2) else ""
        check("claims-variant-constants",
              code == 0 and head2.get("access-date") == "2026-11-01"
              and win2 is not None and len(win2) >= 8192
              and head2.get("window", "").find("min=8192") > 0,
              "exit=%d access-date=%r window=%r err=%r"
              % (code, head2.get("access-date"), head2.get("window"),
                 err.strip()[:100]))

        # 2c. a claims document with no round token is refused, and names the key
        repo3, rev3 = _fixture_repo(
            tmp, {"base": "211f9526800906e0c585d878d265c37e5e090c15",
                  "frozen": "2026-10-27"},
            "r77 claims without a round")
        out2c = os.path.join(ev, "V2.txt")
        code, _, err = _run(["--repo", repo3, "--freeze", rev3,
                             "--url", live_fixture,
                             "--wayback-url", wb("/fixture.html"),
                             "--quote", CJK_QUOTE,
                             "--anchor-quote", CJK_ANCHOR, "--out", out2c])
        check("claims-missing-round",
              code == 2 and not os.path.exists(out2c) and "`round`" in err,
              "exit=%d err=%r" % (code, err.strip()[:140]))

        # 3. the canonical receipt: live window, both fetches, same-page proof,
        #    memento, UA->response binding, window >= 4096, digest, anchor bound
        out3 = os.path.join(ev, "S897.txt")
        _FixtureHandler.seen = []
        code, outlog, err = _run(common + ["--id", "S897", "--url", live_fixture,
                                           "--wayback-url", wb("/fixture.html"),
                                           "--quote", CJK_QUOTE,
                                           "--anchor-quote", CJK_ANCHOR,
                                           "--out", out3, "--locator", "fixture p2"])
        text3 = _read(out3) if os.path.exists(out3) else ""
        head3 = headers(out3)
        window3 = stored_window(text3) or ""
        quote3 = stored_quote(text3)
        geo = re.match(r"chars=(\d+) min=(\d+) pad=(\d+) before=(\d+) after=(\d+) "
                       r"anchor-before=(\d+) anchor-after=(\d+)",
                       head3.get("window", ""))
        order = ["url", "ua", "http", "bytes", "sha256", "fetched", "quote-found",
                 "quote-words", "quote-chars", "visible-chars", "window-scope"]
        keys_in_order = []
        for line in text3.splitlines():
            match = re.match(r"^([A-Za-z][A-Za-z0-9_-]*):", line)
            if match:
                name = match.group(1).lower()
                if name not in keys_in_order:
                    keys_in_order.append(name)
        head_pos = [keys_in_order.index(k) for k in order if k in keys_in_order]
        sent = {ua for path, ua in _FixtureHandler.seen}
        facts3 = {
            "exit0": code == 0,
            "quote-found": head3.get("quote-found") == "yes",
            "verbatim": head3.get("quote-found-verbatim") == "yes",
            "anchor-found": head3.get("anchor-found") == "yes",
            "anchor-in-window": head3.get("anchor-in-window") == "yes",
            "anchor-quote": head3.get("anchor-quote") == CJK_ANCHOR,
            "anchor-chars": head3.get("anchor-quote-chars") == str(len(CJK_ANCHOR)),
            "quote-in-anchor": head3.get("quote-in-anchor") == "yes",
            "geo": geo is not None,
            "window-min": geo is not None and int(geo.group(1)) >= 4096
            and int(geo.group(1)) == len(window3),
            "pad": geo is not None and int(geo.group(4)) >= 400
            and int(geo.group(5)) >= 400,
            "one-line": "\n" not in window3,
            "window-has-quote": folded_has(window3, CJK_QUOTE),
            "window-has-anchor": folded_has(window3, CJK_ANCHOR),
            "window-digest": head3.get("window-sha256")
            == hashlib.sha256(window3.encode("utf-8")).hexdigest(),
            "window-bytes": head3.get("window-bytes")
            == str(len(window3.encode("utf-8"))),
            "scope": head3.get("window-scope") == "excerpt",
            "visible": int(head3.get("visible-chars", "0")) >= len(window3),
            "quote-block": quote3.strip() == CJK_QUOTE,
            "bytes-rule": head3.get("bytes-rule", "").startswith("bytes:/sha256:")
            and "not canonical" in head3.get("bytes-rule", ""),
            "frozen": head3.get("claims-frozen") == "yes",
            "claims-source": head3.get("claims-source", "").startswith("git show "),
            "access-date": head3.get("access-date") == "2026-10-27",
            "quote-chars": head3.get("quote-chars") == str(len(CJK_QUOTE)),
            "key-order": len(head_pos) == len(order) and head_pos == sorted(head_pos),
            "verdicts": "VERIFY OK" in outlog and "CAPTURE OK" in outlog,
        }
        check("live-window", all(facts3.values()),
              "failed=%r err=%r window=%r"
              % ([k for k, ok in facts3.items() if not ok], err.strip(),
                 head3.get("window")))

        # 3b. the round-77 pair: window-source, same-page, memento, bindings
        check("round77-pair",
              head3.get("window-source") == "live"
              and head3.get("window-fetch") == "GET " + live_fixture
              and head3.get("fetch") == "GET " + live_fixture
              and head3.get("url") == live_fixture
              and head3.get("live-http") == "200"
              and head3.get("wayback-http") == "200"
              and head3.get("http-status") == head3.get("live-http")
              and head3.get("bytes") == head3.get("live-bytes")
              and head3.get("sha256") == head3.get("live-sha256")
              == hashlib.sha256(html).hexdigest()
              and head3.get("bytes") == str(len(html))
              and head3.get("wayback-sha256") == hashlib.sha256(html).hexdigest()
              and head3.get("wayback-url") == wb("/fixture.html")
              and head3.get("wayback-original") == live_fixture
              and head3.get("wayback-same-page") == "yes"
              and head3.get("wayback-final-original") == live_fixture
              and head3.get("wayback-final-same-page") == "yes"
              and head3.get("wayback-timestamp") == "20240111092427"
              and head3.get("wayback-modifier") == "id_"
              and head3.get("wayback-memento-datetime")
              == "Thu, 11 Jan 2024 09:24:27 GMT"
              and head3.get("wayback-timestamp-matches") == "yes"
              and head3.get("wayback-rule", "").startswith("a row's evidence")
              and 'ua="%s"' % UA_BROWSER in head3.get("response-bind-live", "")
              and "http=200" in head3.get("response-bind-live", "")
              and head3.get("live-sha256", "")[:16] in head3.get("response-bind-live", "")
              and 'ua="%s"' % UA_BROWSER in head3.get("response-bind-wayback", "")
              and "memento=Thu, 11 Jan 2024 09:24:27 GMT"
              in head3.get("response-bind-wayback", "")
              and head3.get("live-ua") == UA_BROWSER
              and head3.get("wayback-ua") == UA_BROWSER
              and sent == {UA_BROWSER}
              and head3.get("live-challenge") == "none"
              and head3.get("wayback-challenge") == "none"
              and head3.get("live-quote-found") == "yes"
              and head3.get("wayback-quote-found") == "yes",
              "head=%r sent=%r"
              % ({k: head3.get(k) for k in ("window-source", "wayback-http",
                                            "wayback-same-page",
                                            "wayback-memento-datetime",
                                            "response-bind-wayback")}, sent))

        # 4. --window-from wayback: the capture's atoms become the top-level
        #    ones, the live fetch is still recorded
        out4 = os.path.join(ev, "S897-wb.txt")
        code, outlog, err = _run(common + ["--url", live_fixture,
                                           "--wayback-url", wb("/fixture.html"),
                                           "--window-from", "wayback",
                                           "--quote", CJK_QUOTE,
                                           "--anchor-quote", CJK_ANCHOR,
                                           "--out", out4])
        head4 = headers(out4)
        win4 = stored_window(_read(out4)) if os.path.exists(out4) else ""
        check("wayback-window",
              code == 0 and head4.get("window-source") == "wayback"
              and head4.get("window-fetch") == "GET " + wb("/fixture.html")
              and head4.get("fetch") == "GET " + live_fixture
              and head4.get("http-status") == "200"
              and head4.get("http-status") == head4.get("wayback-http")
              and head4.get("bytes") == head4.get("wayback-bytes")
              and head4.get("sha256") == head4.get("wayback-sha256")
              and head4.get("anchor-in-window") == "yes"
              and win4 is not None and len(win4) >= 4096
              and "VERIFY OK" in outlog and "CAPTURE OK" in outlog,
              "exit=%d head=%r err=%r"
              % (code, {k: head4.get(k) for k in ("window-source", "bytes",
                                                  "wayback-bytes")},
                 err.strip()[:120]))

        # 5. the D1 shape: the live page is a 403 wall (no challenge marker),
        #    the capture is the opened document
        out5 = os.path.join(ev, "S897-wall.txt")
        code, outlog, err = _run(common + ["--url", base + "/wall.html",
                                           "--wayback-url", wb("/wall.html"),
                                           "--quote", CJK_QUOTE,
                                           "--anchor-quote", CJK_ANCHOR,
                                           "--out", out5])
        head5 = headers(out5)
        check("live-wall-capture-window",
              code == 0 and head5.get("window-source") == "wayback"
              and head5.get("live-http") == "403"
              and head5.get("wayback-http") == "200"
              and head5.get("http-status") == "200"
              and head5.get("live-challenge") == "none"
              and head5.get("anchor-in-window") == "yes"
              and "CAPTURE OK" in outlog,
              "exit=%d head=%r err=%r"
              % (code, {k: head5.get(k) for k in ("window-source", "live-http",
                                                  "http-status")},
                 err.strip()[:120]))

        # 6. a challenged live page with a clean capture: the wall is recorded,
        #    the capture is the window
        out6 = os.path.join(ev, "S897-chall.txt")
        code, outlog, err = _run(common + ["--url", base + "/challenge.html",
                                           "--wayback-url", wb("/challenge.html"),
                                           "--quote", CJK_QUOTE,
                                           "--anchor-quote", CJK_ANCHOR,
                                           "--out", out6])
        head6 = headers(out6)
        check("challenge-live-clean-capture",
              code == 0 and head6.get("window-source") == "wayback"
              and head6.get("live-challenge") == "js-challenge"
              and head6.get("challenge") == "none"
              and head6.get("anchor-in-window") == "yes",
              "exit=%d head=%r err=%r"
              % (code, {k: head6.get(k) for k in ("window-source",
                                                  "live-challenge",
                                                  "challenge")},
                 err.strip()[:120]))

        # 7. both halves are walls: the file records the challenge, exit 6
        out7 = os.path.join(ev, "S897-bothwall.txt")
        code, _, err = _run(common + ["--url", base + "/challenge2.html",
                                      "--wayback-url", wb("/challenge2.html"),
                                      "--quote", CJK_QUOTE,
                                      "--anchor-quote", CJK_ANCHOR,
                                      "--out", out7])
        head7 = headers(out7)
        check("challenge-detected",
              code == 6 and head7.get("challenge") == "js-challenge"
              and head7.get("wayback-challenge") == "js-challenge"
              and "enable javascript" in head7.get("challenge-detail", "").lower()
              and "UNOPENED" in err,
              "exit=%d challenge=%r err=%r"
              % (code, head7.get("challenge"), err.strip()[:120]))

        # 8. an anchor absent from the document: refused, nothing written
        out8 = os.path.join(ev, "F8.txt")
        code, _, err = _run(common + ["--url", live_fixture,
                                      "--wayback-url", wb("/fixture.html"),
                                      "--quote", CJK_QUOTE,
                                      "--anchor-quote", "この錨はページに存在しません",
                                      "--out", out8])
        check("anchor-absent-document",
              code == 7 and not os.path.exists(out8)
              and "absent from the window source" in err and "REFUSED" in err,
              "exit=%d exists=%s err=%r"
              % (code, os.path.exists(out8), err.strip()[:140]))

        # 9. an anchor outside the window: refused -- the R75-M2 / S888 shape
        out9 = os.path.join(ev, "F9.txt")
        code, _, err = _run(common + ["--url", base + "/far.html",
                                      "--wayback-url", wb("/far.html"),
                                      "--quote", CJK_QUOTE,
                                      "--anchor-quote", FAR_ANCHOR,
                                      "--out", out9])
        check("anchor-outside-window",
              code == 7 and not os.path.exists(out9)
              and "absent from the stored window" in err
              and "cut the window with --find" in err,
              "exit=%d exists=%s err=%r"
              % (code, os.path.exists(out9), err.strip()[:180]))

        # 10. an anchor that matches only the whitespace-free tier cannot be
        #     confirmed by the counter's fold: refused, not written
        out10 = os.path.join(ev, "F10.txt")
        code, _, err = _run(common + ["--url", live_fixture,
                                      "--wayback-url", wb("/fixture.html"),
                                      "--quote", SPACED_QUOTE,
                                      "--anchor-quote", SPACED_ANCHOR,
                                      "--out", out10])
        check("anchor-fold-refused",
              code == 7 and not os.path.exists(out10)
              and "absent from the stored window after NFKC" in err,
              "exit=%d exists=%s err=%r"
              % (code, os.path.exists(out10), err.strip()[:160]))

        # 11. a missing --anchor-quote is a usage error (no file)
        out11 = os.path.join(ev, "F11.txt")
        code, _, err = _run(common + ["--url", live_fixture,
                                      "--wayback-url", wb("/fixture.html"),
                                      "--quote", CJK_QUOTE, "--out", out11])
        check("anchor-required",
              code == 2 and not os.path.exists(out11) and "--anchor-quote" in err,
              "exit=%d err=%r" % (code, err.strip()[:120]))

        # 11b. a capture URL is required: a receipt without one is a usage error
        out11b = os.path.join(ev, "F11b.txt")
        code, _, err = _run(common + ["--url", live_fixture,
                                      "--quote", CJK_QUOTE,
                                      "--anchor-quote", CJK_ANCHOR,
                                      "--out", out11b])
        check("wayback-required",
              code == 2 and not os.path.exists(out11b)
              and "wayback-url|wayback-timestamp" in err,
              "exit=%d err=%r" % (code, err.strip()[:140]))

        # 12. absent quote: file written, window empty, exit 3
        out12 = os.path.join(ev, "F12.txt")
        code, _, err = _run(common + ["--url", live_fixture,
                                      "--wayback-url", wb("/fixture.html"),
                                      "--quote", "この文はページに存在しません",
                                      "--anchor-quote", CJK_ANCHOR,
                                      "--out", out12])
        text12 = _read(out12) if os.path.exists(out12) else ""
        head12 = parse_evidence(text12)
        check("quote-missing",
              code == 3 and head12.get("quote-found") == "no"
              and head12.get("anchor-in-window") == "no"
              and (stored_window(text12) or "").strip() == ""
              and "存在しません" in (stored_quote(text12) or "")
              and "not citable" in err,
              "exit=%d found=%r err=%r"
              % (code, head12.get("quote-found"), err.strip()[:100]))

        # 13. extractor drops script/style/comments, decodes entities, and the
        #     reader still finds the CJK narrative quote verbatim
        out13 = os.path.join(ev, "F13.txt")
        code, _, _ = _run(common + ["--url", live_fixture,
                                    "--wayback-url", wb("/fixture.html"),
                                    "--quote", NARR_QUOTE,
                                    "--anchor-quote", NARR_ANCHOR,
                                    "--out", out13])
        head13 = headers(out13)
        check("extract-visible",
              code == 0
              and all(m not in text3 for m in ("SCRIPT_ONLY_TEXT", "STYLE_ONLY_TEXT",
                                               "COMMENT_ONLY_TEXT"))
              and "アンパサンド & と山括弧 <tag>" in text3
              and "fixture title" not in text3
              and head13.get("quote-found-verbatim") == "yes",
              "exit=%d script-leak=%s" % (code, "SCRIPT_ONLY_TEXT" in text3))

        # 13b. an anchor argument that is itself line-wrapped (a registry cell
        #      that wraps) is collapsed for the stored line and its count
        out13b = os.path.join(ev, "F13b.txt")
        wrapped = "The settings note holds\nfive sections in one file."
        code, _, err = _run(common + ["--url", live_fixture,
                                      "--wayback-url", wb("/fixture.html"),
                                      "--quote", LATIN_QUOTE,
                                      "--anchor-quote", wrapped,
                                      "--out", out13b])
        head13b = headers(out13b)
        check("anchor-wrapped-argument",
              code == 0 and head13b.get("anchor-quote") == LATIN_ANCHOR
              and head13b.get("anchor-quote-chars") == str(len(LATIN_ANCHOR))
              and head13b.get("anchor-in-window") == "yes"
              and head13b.get("quote-in-anchor") == "yes",
              "exit=%d anchor=%r chars=%r err=%r"
              % (code, head13b.get("anchor-quote"),
                 head13b.get("anchor-quote-chars"), err.strip()[:120]))

        # 14. quote at the very start of the text: before small, window >= 4096
        out14 = os.path.join(ev, "F14.txt")
        code, _, _ = _run(common + ["--url", base + "/edge.html",
                                    "--wayback-url", wb("/edge.html"),
                                    "--quote", EDGE_QUOTE,
                                    "--anchor-quote", EDGE_QUOTE,
                                    "--out", out14])
        head14 = headers(out14)
        geo14 = re.match(r"chars=(\d+) min=(\d+) pad=(\d+) before=(\d+) after=(\d+)",
                         head14.get("window", ""))
        check("window-edge",
              code == 0 and head14.get("anchor-in-window") == "yes"
              and geo14 is not None and int(geo14.group(4)) == 0
              and int(geo14.group(1)) >= 4096 and int(geo14.group(5)) >= 400,
              "exit=%d window=%r" % (code, head14.get("window")))

        # 15. a document shorter than the window minimum is stored whole and
        #     declared; the anchor is inside it, so the capture verifies
        out15 = os.path.join(ev, "F15.txt")
        code, _, err = _run(common + ["--url", base + "/short.html",
                                      "--wayback-url", wb("/short.html"),
                                      "--quote", SHORT_QUOTE,
                                      "--anchor-quote", SHORT_QUOTE,
                                      "--out", out15])
        text15 = _read(out15) if os.path.exists(out15) else ""
        head15 = parse_evidence(text15)
        win15 = stored_window(text15) or ""
        check("window-whole-document",
              code == 0 and head15.get("window-scope") == "whole-document"
              and head15.get("visible-chars") == str(len(win15))
              and len(win15) < 4096
              and head15.get("anchor-in-window") == "yes"
              and head15.get("window-sha256")
              == hashlib.sha256(win15.encode("utf-8")).hexdigest(),
              "exit=%d err=%r scope=%r visible=%r win=%d"
              % (code, err.strip()[:80], head15.get("window-scope"),
                 head15.get("visible-chars"), len(win15)))

        # 16. whole-document is not a shortcut: a truncated window and a forged
        #     scope both fail verification
        trunc = os.path.join(ev, "F15-trunc.txt")
        with open(trunc, "w", encoding="utf-8") as fh:
            fh.write(text15.replace(win15, win15[:-6], 1))
        code_tr, _, err_tr = _run(common + ["--verify", trunc])
        forged = os.path.join(ev, "S897-forged.txt")
        lines_f = [("window-scope: whole-document"
                    if line.startswith("window-scope:") else line)
                   for line in text3.splitlines()]
        with open(forged, "w", encoding="utf-8") as fh:
            fh.write("\n".join(lines_f) + "\n")
        code_fg, _, err_fg = _run(common + ["--verify", forged])
        check("whole-document-guard",
              code_tr == 5 and "but visible-chars says" in err_tr
              and code_fg == 5 and "whole-document claimed" in err_fg,
              "trunc=%d forged=%d err=%r"
              % (code_tr, code_fg, (err_tr + err_fg).strip()[:140]))

        # 17. the graded facts are graded: a stripped anchor, an edited window,
        #     a forged digest, a tampered bind and a swapped window-source each
        #     fail verification
        stripped = os.path.join(ev, "S897-noanchor.txt")
        lines_s = [line for line in text3.splitlines()
                   if not line.startswith(("anchor-quote:", "anchor-in-window:"))]
        with open(stripped, "w", encoding="utf-8") as fh:
            fh.write("\n".join(lines_s) + "\n")
        code_s, _, err_s = _run(common + ["--verify", stripped])
        win_edit = os.path.join(ev, "S897-window-edit.txt")
        with open(win_edit, "w", encoding="utf-8") as fh:
            fh.write(text3.replace(window3, window3[:-4] + "XXXX", 1))
        code_w, _, err_w = _run(common + ["--verify", win_edit])
        digest_edit = os.path.join(ev, "S897-digest-edit.txt")
        lines_d = [("window-sha256: " + "0" * 64)
                   if line.startswith("window-sha256:") else line
                   for line in text3.splitlines()]
        with open(digest_edit, "w", encoding="utf-8") as fh:
            fh.write("\n".join(lines_d) + "\n")
        code_d, _, err_d = _run(common + ["--verify", digest_edit])
        check("verify-mode",
              code_s == 5 and "anchor" in err_s
              and code_w == 5 and "window-sha256 mismatch" in err_w
              and code_d == 5 and "window-sha256 mismatch" in err_d,
              "anchor=%d window=%d digest=%d err=%r"
              % (code_s, code_w, code_d, (err_s + err_w + err_d).strip()[:160]))

        bind_edit = os.path.join(ev, "S897-bind-edit.txt")
        lines_b = [("response-bind-wayback: ua=\"curl/8.0\" -> http=200")
                   if line.startswith("response-bind-wayback:") else line
                   for line in text3.splitlines()]
        with open(bind_edit, "w", encoding="utf-8") as fh:
            fh.write("\n".join(lines_b) + "\n")
        code_b, _, err_b = _run(common + ["--verify", bind_edit])
        src_edit = os.path.join(ev, "S897-src-edit.txt")
        lines_x = [("live-bytes: 1" if line.startswith("live-bytes:") else line)
                   for line in text3.splitlines()]
        with open(src_edit, "w", encoding="utf-8") as fh:
            fh.write("\n".join(lines_x) + "\n")
        code_x, _, err_x = _run(common + ["--verify", src_edit])
        check("pair-graded",
              code_b == 5 and "does not bind the recorded UA" in err_b
              and code_x == 5 and "does not match `live-bytes:`" in err_x,
              "bind=%d source=%d err=%r"
              % (code_b, code_x, (err_b + err_x).strip()[:180]))

        # 18. a capture of another page, a capture that did not answer, and a
        #     capture that cannot be dated are each refused (nothing written)
        out18 = os.path.join(ev, "F18.txt")
        code_wp, _, err_wp = _run(common + ["--url", live_fixture,
                                            "--wayback-url", wb("/other.html"),
                                            "--quote", CJK_QUOTE,
                                            "--anchor-quote", CJK_ANCHOR,
                                            "--out", out18])
        out18b = os.path.join(ev, "F18b.txt")
        code_nc, _, err_nc = _run(common + ["--url", base + "/uncaptured.html",
                                            "--wayback-url", wb("/uncaptured.html"),
                                            "--quote", CJK_QUOTE,
                                            "--anchor-quote", CJK_ANCHOR,
                                            "--out", out18b])
        out18c = os.path.join(ev, "F18c.txt")
        code_nm, _, err_nm = _run(common + ["--url", base + "/nomemento.html",
                                            "--wayback-url", wb("/nomemento.html"),
                                            "--quote", CJK_QUOTE,
                                            "--anchor-quote", CJK_ANCHOR,
                                            "--out", out18c])
        check("capture-pair-refusals",
              code_wp == 7 and "not the page" in err_wp
              and code_nc == 7 and "answered HTTP 404" in err_nc
              and code_nm == 7 and "Memento-Datetime" in err_nm
              and not any(os.path.exists(p) for p in (out18, out18b, out18c)),
              "wrong=%d missing=%d nometa=%d err=%r"
              % (code_wp, code_nc, code_nm,
                 (err_wp + err_nc + err_nm).strip()[:220]))

        # 19. --wayback-timestamp builds the replay URL from wayback_prefix
        out19 = os.path.join(ev, "F19.txt")
        code, _, err = _run(common + ["--url", live_fixture,
                                      "--wayback-timestamp", "20240111092427",
                                      "--quote", CJK_QUOTE,
                                      "--anchor-quote", CJK_ANCHOR,
                                      "--out", out19])
        head19 = headers(out19)
        check("wayback-timestamp-builds-url",
              code == 0
              and head19.get("wayback-url") == wb("/fixture.html")
              and head19.get("wayback-memento-datetime")
              == "Thu, 11 Jan 2024 09:24:27 GMT"
              and head19.get("wayback-timestamp-matches") == "yes",
              "exit=%d wayback-url=%r err=%r"
              % (code, head19.get("wayback-url"), err.strip()[:120]))

        # 20. http.server: UA sent, status, bytes, sha256, GET line, retry
        out20 = os.path.join(ev, "F20.txt")
        _FixtureHandler.seen = []
        code, _, _ = _run(common + ["--url", live_fixture,
                                    "--wayback-url", wb("/fixture.html"),
                                    "--quote", CJK_QUOTE,
                                    "--anchor-quote", CJK_ANCHOR,
                                    "--out", out20])
        head20 = headers(out20)
        sent20 = {ua for path, ua in _FixtureHandler.seen}
        check("http-fetch",
              code == 0 and head20.get("http") == "200"
              and head20.get("http-status") == "200"
              and head20.get("user-agent") == UA_BROWSER
              and head20.get("ua") == UA_BROWSER
              and sent20 == {UA_BROWSER}
              and head20.get("bytes") == str(len(html))
              and head20.get("sha256") == hashlib.sha256(html).hexdigest()
              and head20.get("fetch") == "GET " + live_fixture
              and head20.get("content-length") == str(len(html))
              and head20.get("transferred-bytes") == str(len(html))
              and head20.get("fetch-attempts") == "1"
              and "curl -sS -L" in head20.get("fetch-command", ""),
              "exit=%d head=%r seen=%r"
              % (code, {k: head20.get(k) for k in ("http", "bytes",
                                                   "user-agent")}, sent20))

        out21 = os.path.join(ev, "F21.txt")
        _FixtureHandler.flaky["left"] = 1
        code, _, err = _run(common + ["--url", base + "/flaky.html",
                                      "--wayback-url", wb("/flaky.html"),
                                      "--quote", CJK_QUOTE,
                                      "--anchor-quote", CJK_ANCHOR,
                                      "--out", out21])
        head21 = headers(out21)
        check("fetch-retry",
              code == 0 and head21.get("http") == "200"
              and head21.get("fetch-attempts") == "2"
              and head21.get("bytes") == str(len(html)),
              "exit=%d attempts=%r err=%r"
              % (code, head21.get("fetch-attempts"), err.strip()[:100]))

        out22 = os.path.join(ev, "F22.txt")
        _FixtureHandler.flaky["left"] = 6
        code, _, err = _run(common + ["--url", base + "/flaky.html",
                                      "--wayback-url", wb("/flaky.html"),
                                      "--quote", CJK_QUOTE,
                                      "--anchor-quote", CJK_ANCHOR,
                                      "--out", out22, "--retries", "1"])
        check("fetch-retry-gives-up",
              code == 2 and not os.path.exists(out22)
              and "curl exit 18 after 2 attempt(s)" in err,
              "exit=%d err=%r" % (code, err.strip()[:120]))
        _FixtureHandler.flaky["left"] = 0

        # 23. the window source is not 200: the file is written and the run
        #     says so (the capture still answered, so the pair holds)
        out23 = os.path.join(ev, "F23.txt")
        code, _, err = _run(common + ["--url", base + "/missing.html",
                                      "--wayback-url", wb("/missing.html"),
                                      "--window-from", "live",
                                      "--quote", "not here",
                                      "--anchor-quote", "not here",
                                      "--out", out23])
        head23 = headers(out23)
        check("http-not-200",
              code == 4 and head23.get("http") == "404"
              and head23.get("wayback-http") == "200"
              and "not citable" in err,
              "exit=%d http=%r err=%r"
              % (code, head23.get("http"), err.strip()[:140]))

        # 24. PDF: no --find is refused; --find cuts the window by the locator's
        #     page and the file records find-page/page-count/window-pages
        if shutil.which("pdftotext") is None:
            for name in ("pdf-find-required", "pdf-find-page",
                         "pdf-find-first-occurrence"):
                check(name, True, "SKIPPED: pdftotext absent")
        else:
            out24 = os.path.join(ev, "S898.txt")
            code, _, err = _run(common + ["--url", base + "/pdf.pdf",
                                          "--wayback-url", wb("/pdf.pdf"),
                                          "--quote", "PDF fixture quote sentence.",
                                          "--anchor-quote", "PDF fixture anchor span.",
                                          "--out", out24])
            check("pdf-find-required",
                  code == 7 and not os.path.exists(out24)
                  and "needs --find" in err,
                  "exit=%d exists=%s err=%r"
                  % (code, os.path.exists(out24), err.strip()[:140]))

            out24b = os.path.join(ev, "S898b.txt")
            code, outlog, err = _run(common + ["--url", base + "/pdf.pdf",
                                               "--wayback-url", wb("/pdf.pdf"),
                                               "--quote", "PDF fixture quote sentence.",
                                               "--anchor-quote", "PDF fixture anchor span.",
                                               "--find", "LOCATOR-MARKER page five",
                                               "--locator", "p. 5",
                                               "--out", out24b])
            text24b = _read(out24b) if os.path.exists(out24b) else ""
            head24b = parse_evidence(text24b)
            win24b = stored_window(text24b) or ""
            pages24 = re.match(r"^(\d+)\.\.(\d+)$",
                               head24b.get("window-pages", ""))
            check("pdf-find-page",
                  code == 0 and head24b.get("find-page") == "5"
                  and pages24 is not None
                  and int(pages24.group(1)) <= 5 <= int(pages24.group(2))
                  and int(head24b.get("page-count", "0")) >= 5
                  and head24b.get("anchor-in-window") == "yes"
                  and head24b.get("window-source") == "live"
                  and head24b.get("wayback-same-page") == "yes"
                  and head24b.get("wayback-memento-datetime")
                  == "Thu, 11 Jan 2024 09:24:27 GMT"
                  and head24b.get("quote-page") == "5"
                  and head24b.get("anchor-page") == "5"
                  and folded_has(win24b, "PDF fixture quote sentence.")
                  and folded_has(win24b, "PDF fixture anchor span.")
                  and head24b.get("window-sha256")
                  == hashlib.sha256(win24b.encode("utf-8")).hexdigest()
                  and head24b.get("fetch") == "GET " + base + "/pdf.pdf"
                  and "pdftotext -enc UTF-8" in head24b.get("extract", ""),
                  "exit=%d err=%r find-page=%r pages=%r window-pages=%r page-count=%r"
                  % (code, err.strip()[:120], head24b.get("find-page"), pages24,
                     head24b.get("window-pages"), head24b.get("page-count")))

            out24c = os.path.join(ev, "S898c.txt")
            code, _, err = _run(common + ["--url", base + "/pdf.pdf",
                                          "--wayback-url", wb("/pdf.pdf"),
                                          "--quote", "PDF fixture quote sentence.",
                                          "--anchor-quote", "PDF fixture anchor span.",
                                          "--find", "LOCATOR-MARKER",
                                          "--out", out24c])
            check("pdf-find-first-occurrence",
                  code == 7 and not os.path.exists(out24c)
                  and "absent from the stored window" in err,
                  "exit=%d exists=%s err=%r"
                  % (code, os.path.exists(out24c), err.strip()[:160]))

            # the cited spans' own pages are recorded and graded: a file whose
            # quote-page falls outside window-pages (the p5-window/p4-quote
            # shape) is not citable, and a non-numeric page is not a page
            page_edit = os.path.join(ev, "S898b-page-edit.txt")
            lines_p = [("quote-page: 2" if line.startswith("quote-page:") else line)
                       for line in text24b.splitlines()]
            with open(page_edit, "w", encoding="utf-8") as fh:
                fh.write("\n".join(lines_p) + "\n")
            code_p, _, err_p = _run(common + ["--verify", page_edit])
            blank_edit = os.path.join(ev, "S898b-page-blank.txt")
            lines_q = [("anchor-page: n/a" if line.startswith("anchor-page:") else line)
                       for line in text24b.splitlines()]
            with open(blank_edit, "w", encoding="utf-8") as fh:
                fh.write("\n".join(lines_q) + "\n")
            code_q, _, err_q = _run(common + ["--verify", blank_edit])
            check("pdf-page-facts",
                  code_p == 5 and "is outside window-pages" in err_p
                  and code_q == 5 and "is not a page number" in err_q,
                  "page=%d blank=%d err=%r"
                  % (code_p, code_q, (err_p + err_q).strip()[:200]))

        # 25. usage floors come from the claims (--min-window / --pad below the
        #     frozen values is a refusal, and nothing is written)
        out25 = os.path.join(ev, "F25.txt")
        code_low, _, _ = _run(common + ["--url", live_fixture,
                                        "--wayback-url", wb("/fixture.html"),
                                        "--quote", CJK_QUOTE,
                                        "--anchor-quote", CJK_ANCHOR,
                                        "--out", out25, "--min-window", "100"])
        code_pad, _, _ = _run(common + ["--url", live_fixture,
                                        "--wayback-url", wb("/fixture.html"),
                                        "--quote", CJK_QUOTE,
                                        "--anchor-quote", CJK_ANCHOR,
                                        "--out", os.path.join(ev, "F26.txt"),
                                        "--pad", "40"])
        code_empty, _, _ = _run(common + ["--url", live_fixture,
                                          "--wayback-url", wb("/fixture.html"),
                                          "--quote", "   ",
                                          "--anchor-quote", CJK_ANCHOR,
                                          "--out", os.path.join(ev, "F27.txt")])
        check("guards",
              code_low == 2 and code_pad == 2 and code_empty == 2
              and not os.path.exists(out25)
              and not os.path.exists(os.path.join(ev, "F26.txt"))
              and not os.path.exists(os.path.join(ev, "F27.txt")),
              "window=%d pad=%d empty=%d" % (code_low, code_pad, code_empty))

        # 26. an uncommitted claims document is recorded as unfrozen
        claims_path = os.path.join(tmp, "claims-rehearsal.json")
        with open(claims_path, "w", encoding="utf-8") as fh:
            json.dump(_claims_doc(capture={"wayback_prefix": base + "/web"}), fh)
        out26 = os.path.join(ev, "F28.txt")
        code, _, _ = _run(["--claims-file", claims_path,
                           "--url", live_fixture,
                           "--wayback-url", wb("/fixture.html"),
                           "--quote", CJK_QUOTE,
                           "--anchor-quote", CJK_ANCHOR, "--out", out26])
        head26 = headers(out26)
        check("claims-file-rehearsal",
              code == 0 and head26.get("claims-frozen") == "no"
              and head26.get("claims-source", "").startswith("file:")
              and "sha256=" in head26.get("claims-source", ""),
              "exit=%d claims-frozen=%r source=%r"
              % (code, head26.get("claims-frozen"),
                 head26.get("claims-source", "")[:80]))
    finally:
        server.shutdown()
        server.server_close()
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
