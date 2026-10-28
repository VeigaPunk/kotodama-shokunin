#!/usr/bin/env python3
r"""Round-76 claim-C evidence capture (adapted from round 75).

Fetches one URL, records what was actually served, and writes the evidence file
the claim-C EVIDENCE leg reads: `reports/round-76/evidence/<id>.txt`.

Provenance.  This is the round-75 tool (`.ufo/waves/round-75/counters/
capture-evidence.py`, itself the round-74 tool's successor) carried forward with
two fixes the round-75 verifier routed (R75-M2 and the PDF-window defect), plus
the round-76 rule that every round token comes from the frozen claims.json.  The
extraction, the folding tiers, the digest rule and the self-verification are the
round-75 code paths, unchanged -- one grammar across rounds, so a counter reads
any round's evidence file the same way.

Round-76 changes, and why (each one shown able to fail in `--selftest`):

 1. ANCHOR BINDING (R75-M2).  Round 75's probe receipts stored a `quote:` that
    was not the row's anchor span (a title instead of the sentence the registry
    row cites), so two receipts stored a window that did not contain the anchor
    at all.  Round 76 requires `--anchor-quote`: the row's anchor span, recorded
    as `anchor-quote:` and located in the document.  The capture is REFUSED
    (exit 7, no file written) when the anchor span is absent from the stored
    window after NFKC + whitespace folding -- which is exactly the S888/S892
    failure: a window cut at the document head cannot reach an anchor on p. 3.
    `quote-in-anchor:` and `quote-anchor-distance:` record how the stored quote
    sits against the anchor, so a reviewer sees the binding instead of trusting
    it; `anchor-in-window:` is the graded fact.

 2. PDF WINDOWS BY THE PAGE THE LOCATOR NAMES.  Round 75 cut its window around
    the quote, so a receipt whose quote was the title stored the first 4096
    characters -- the head -- and the anchor's page never entered the window.
    Round 76 cuts the window around `--find`: the first occurrence of the
    locator string in the WHOLE decoded document (never the head), and a PDF
    capture without `--find` is refused.  For a PDF the file records
    `find-char:`, `find-page:`, `find-hits:`, `page-count:` and
    `window-pages:`, so "p. 3" is a fact in the file rather than a locator
    claim in prose.

 3. BYTE COUNTS ARE NOT CANONICAL.  One Persée URL served three different byte
    counts across round 75 (109588 / 111487 / a third), so every capture now
    carries its own `fetch:`, `window-sha256:` and a `bytes-rule:` line stating
    that `bytes:`/`sha256:` describe THIS fetch only.  A lesson that restates a
    byte count as canonical is restating one observation of an unstable page.

 4. CONSTANTS FROM THE FROZEN CLAIMS.  `round`, `base`, the access date, the
    evidence directory and the verdict prefix are read from
    `git show <freeze>:reports/round-76/claims.json` (QUALITY 25/26/28), not
    written into the tool.  The claims document is the contract; the keys read
    are listed under "Claims schema" below, and `--print-config` prints every
    resolved value with its provenance, so a missing key is visible before a
    capture runs.  A round token, an access date or a base that the claims do
    not carry is a refusal (exit 2), never a default: a receipt is never graded
    against a date nobody froze.

Grammar written (the round-75 keys first, in the round-75 order, then the
round-76 keys; every round-75 parser still reads the file):

  # evidence <id> -- claim C GATE (round 76)
  url:            requested URL
  ua:             exact User-Agent sent (verbatim)
  http:           HTTP status, or `file` for a local path
  bytes:          length of the stored body in bytes (this fetch only)
  sha256:         64-hex digest of those bytes
  fetched:        UTC ISO-8601 second of the fetch
  quote-found:    yes | no   (after NFKC/NFKD + whitespace folding)
  quote-words:    whitespace tokens, `wc -w` reading
  quote-chars:    characters, `wc -m` reading
  visible-chars:  characters of the whole extracted visible text, collapsed
  window-scope:   excerpt | whole-document
  window:         chars=<n> min=<n> pad=<n> before=<n> after=<n>
                  anchor-before=<n> anchor-after=<n>
  window-sha256:  sha256 of the stored window line (see the rule below)
  window-bytes:   byte length of that same string
  window-rule:    the hashing rule, restated inside the file
  quote-found-verbatim: yes | no  (exact substring of the extracted text)
  anchor-quote:   the ROW'S anchor span, on one line          (round 76)
  anchor-quote-chars: characters of that span                 (round 76)
  anchor-quote-words: whitespace tokens of that span          (round 76)
  anchor-found:   yes | no -- located in the extracted text   (round 76)
  anchor-in-window: yes | no -- present in the stored window after
                  NFKC+whitespace folding (the graded binding) (round 76)
  anchor-char:    character offset of the anchor in the text, or -
  quote-in-anchor: yes | no -- the quote's fold inside the anchor's fold
  quote-anchor-distance: characters between the two starts in the window, or -
  find:           the locator string and its first occurrence
  find-char:      character offset of that first occurrence, or -
  find-page:      1-based page of that occurrence (PDF), or -
  find-hits:      occurrences of the locator after the counter's fold
  page-count:     pages in the decoded document (PDF), or -
  window-pages:   pages the stored window spans, `a..b` (PDF), or -
  bytes-rule:     the "no byte count is canonical" rule, in the file
  claims-source:  `git show <rev>:reports/round-76/claims.json` (or `file:...`)
  claims-frozen:  yes | no -- whether claims-source is a committed revision
  challenge:      none | js-challenge | captcha | login-wall | consent-wall |
                  geo-wall | empty-body  (QUALITY 10)
  challenge-detail: what in the body named the challenge
  content-type:   response Content-Type (or a local-file guess)
  final-url:      url_effective after redirects
  extract:        the extraction performed and the text length
  fetch:          GET <url>                    (round-73 key)
  user-agent:     exact User-Agent             (round-73 key)
  access-date:    YYYY-MM-DD, from the claims   (round-73 key)
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
  <ONE line: >=`min_window` chars of extracted visible text around the quote
   (or around the --find locator), whitespace-collapsed>
  --- quote ---
  <the quote as supplied>

The window rule (claim C's EVIDENCE leg).  The window is stored as a single
whitespace-collapsed line, so "the window text" is unambiguous: it is the one
line between the `--- window ---` marker line and the `--- quote ---` marker
line, with no trailing newline.

`window-scope: excerpt` is the ordinary case: at least `min_window`
(default 4096) characters around the quote (or the locator).  When the whole
extracted visible text is shorter than `min_window` no excerpt can reach the
minimum, so the tool stores the whole text and declares
`window-scope: whole-document`; the leg then requires the stored text to be
exactly that whole text, which is why the same run writes `visible-chars:` and
the verifier requires `len(window) == visible-chars` *and*
`visible_chars < min_window`.  A short window under a long `visible-chars`, or a
whole-document claim for a text that could have been excerpted, is a
verification failure.  `window-sha256:` is the sha256 of those bytes as UTF-8,
`window-bytes:` their length.  The verifier recomputes both from the stored
line, and no flag in the file is read -- `quote-found` is recorded for a human,
not trusted by the grader.

Anchor binding (round 76, R75-M2).  `--anchor-quote` is the registry row's
anchor cell, the span the row says it mined.  The capture locates it in the
document, cuts the window (around the quote, or around `--find` when given) and
then REFUSES -- exit 7, nothing written -- when the anchor's fold does not occur
in the stored window's fold.  The refusal prints the anchor offset, the window's
character range and the gap, so the caller's next move is visible: pass `--find`
with a locator on the page that holds the anchor, or raise `--pad`.  Round 75's
defect was not that a quote was wrong; it was that nothing bound the quote to
the anchor the row cites.

PDF windows (round 76).  A PDF body goes through `pdftotext -enc UTF-8`, whose
form feeds are kept, so page numbers are derived from the document itself: the
window is cut around the FIRST occurrence of `--find` in the whole decoded text
(not the head), and the file records the page of that occurrence, the page
count, and the page range the window covers.  A PDF capture without `--find` is
refused (exit 7): a window cut at the head proves nothing about p. 3.

Claims schema (the contract this tool reads; `--print-config` shows it):
  top level        {"round": 76, "base": "<rev>", "frozen": "YYYY-MM-DD",
                    "claims": [{"id": "C", ...}], "capture": {...}}
  capture block    {"access_date": "YYYY-MM-DD", "min_window": 4096,
                    "min_pad": 400, "default_pad": 400,
                    "evidence_dir": "reports/round-76/evidence",
                    "verdict_prefix": "ACCEPT-C-76",
                    "window_rule": "<text>", "ua": "Mozilla/5.0 ...",
                    "anchor_required": true, "find_required_for_pdf": true}
  The `capture` block may also sit inside claim C.  Round tokens (`round`,
  `base`, `access_date`) have NO literal fallback: an access date is required
  (capture block, claim C `access_date`, an `opened YYYY-MM-DD` clause in claim
  C's text, or a top-level `frozen` date, in that order).  The grammar floors
  (min_window 4096, min_pad/default_pad 400), the browser UA and the window
  rule fall back to the grammar constants when the claims do not override them,
  and the provenance says so.

Quote matching.  Tiers, strongest first: (1) exact substring of the extracted
text; (2) NFKC per character, every whitespace run collapsed to one space, ends
stripped; (3) the same with all whitespace removed -- a source line break inside
a Japanese or Chinese run must not stop a quote from matching; (4) and (5)
repeat (2) and (3) under NFKD, for bodies that use combining sequences.  Both
sides are folded identically and the fold carries an index map back to source
offsets, so the window is cut from the undecorated text.  `quote-found-verbatim:
yes` is the stronger claim and is what a Gate citation should carry;
`normalise:` records the tier that matched.  A quote that matches only the
whitespace-free tier is found and written, but the capture exits 5: the
counter's fold would not confirm it, so re-quote the span.

Bytes.  `bytes:`/`sha256:` always describe the decompressed body of THIS fetch,
so they equal an uncompressed fetch of the same page.  `transferred-bytes:` is
the wire size, below `bytes:` when the server negotiated gzip;
`content-length:` is `-` in that case because the response is chunked.  The
Persée notices are not byte-stable (round 75 measured 109588 / 111487 bytes for
one URL), so the file says in `bytes-rule:` that no byte count is canonical.

Fetching.  http(s) goes through curl with the browser-shaped User-Agent, `-L`,
`--compressed`, a 20 s connect timeout and a 90 s total.  Transport failures
(curl exit 7/18/28/35/52/55/56) are retried with backoff and `fetch-attempts:`
records how many runs it took.  HTTP-level failures are never retried: a 404 is
an answer.

Scratch.  Every temporary file lives under `--work`, else `$HYAKU_SCRATCH`,
else `$TMPDIR`, else the interpreter's temporary directory (`tempfile`); the
tool contains no literal scratch root (prompt §7.4).  The directory is removed
when the run ends.

Dependencies: python3 stdlib, plus `curl` for http(s) and `pdftotext` for PDF
bodies.  No third-party Python.

Exit codes: 0 written and self-verified; 2 fetch/extract/usage/claims error (no
file); 3 written but the quote is not in the extracted text; 4 written but
HTTP != 200; 5 written but self-verification failed (window digest, window
length, status not 200, or the quote absent after NFKC+whitespace folding);
6 written but the served body is a bot challenge or interstitial -- the
challenge was MET, not passed, so the source is UNOPENED (QUALITY 10);
7 REFUSED before writing: the anchor span is absent from the document or from
the stored window, the locator string is absent, a PDF has no `--find`, or the
quote lies outside the window the locator names.  A refusal leaves no file: a
receipt whose binding cannot be proven must not be citable.

Usage:
  capture-evidence.py --repo /path/to/lane --freeze <rev> --id S894 \
      --url https://example/x --quote-file <span> --anchor-quote-file <anchor> \
      --find "locator on the page" --out reports/round-76/evidence/S894.txt
  capture-evidence.py --repo /path/to/lane --freeze <rev> --verify <path>
  capture-evidence.py --selftest --work /fast/scratch/hyaku/kotodama-r76/<seat>
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
CLAIMS_PATH = "reports/round-76/claims.json"
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
BYTES_RULE = ("bytes:/sha256: describe THIS fetch only; a byte count is not "
              "canonical across fetches (one URL served three counts in "
              "round 75)")


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
    "anchor_required": ("anchor_required", "anchor-required"),
    "find_required_for_pdf": ("find_required_for_pdf", "find-required-for-pdf"),
}
DATE_RE = re.compile(r"\d{4}-\d{2}-\d{2}")


class Config:
    """The constants one capture or verification uses, with their provenance."""

    def __init__(self, round_token, base, access_date, min_window, min_pad,
                 default_pad, evidence_dir, verdict_prefix, window_rule, ua,
                 anchor_required, find_required_for_pdf, claims_source,
                 claims_frozen, provenance):
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

    Default: `git -C <repo> show <freeze>:reports/round-76/claims.json`.
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
                  anchor_required, find_required_for_pdf, source, frozen, prov)


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


def fetch(url, ua, work, retries=2):
    """Fetch `url`; return a dict with body bytes and the served metadata.

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
        }

    body_path = os.path.join(work, "body.bin")
    header_path = os.path.join(work, "headers.txt")
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


def extract_text(body, content_type, work):
    """Return (text, extract-line description)."""
    ctype = (content_type or "").lower()
    if ctype.startswith("application/pdf") or body[:5] == b"%PDF-":
        body_path = os.path.join(work, "body.pdf")
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
# render
# --------------------------------------------------------------------------

def _relative_window_position(window_text, span):
    """(before, after) of `span` inside the stored window, or (-1, -1)."""
    hit = locate(window_text, span)
    if not hit["found"]:
        return -1, -1
    return hit["start"], len(window_text) - hit["end"]


def render(ident, url, meta, body, text, extract_line, quote, hit, locator,
           pad, min_window, window_text, scope, visible_chars, cfg, bind,
           access_date=None):
    """Build the evidence file text and the body and window digests."""
    digest = hashlib.sha256(body).hexdigest()
    now = datetime.now(timezone.utc)
    content_length = meta["headers"].get("content-length", "-") if meta["headers"] else "-"
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
    challenge, challenge_detail = detect_challenge(body, meta["content_type"], text)

    lines = [
        "# evidence %s — claim C GATE (round %d)" % (ident, cfg.round),
        "url: %s" % url,
        "ua: %s" % meta["ua_sent"],
        "http: %s" % meta["http"],
        "bytes: %d" % len(body),
        "sha256: %s" % digest,
        "fetched: %s" % now.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "quote-found: %s" % ("yes" if hit["found"] else "no"),
        "quote-words: %d" % len(quote.split()),
        "quote-chars: %d" % len(quote),
        "visible-chars: %d" % visible_chars,
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
        "bytes-rule: %s" % BYTES_RULE,
        "claims-source: %s" % cfg.claims_source,
        "claims-frozen: %s" % cfg.claims_frozen,
        "challenge: %s" % (challenge or "none"),
        "challenge-detail: %s" % (challenge_detail or "(none)"),
        "content-type: %s" % (meta["content_type"] or "unknown"),
        "final-url: %s" % meta["final_url"],
        "extract: %s" % extract_line,
        "fetch: GET %s" % url,
        "user-agent: %s" % meta["ua_sent"],
        "access-date: %s" % (access_date or cfg.access_date),
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


BASE_KEYS = ("url", "fetch", "user-agent", "access-date", "http-status",
             "bytes", "sha256", "locator", "quote-words", "quote-chars",
             "window-sha256", "window-bytes", "window-scope", "visible-chars")
R75_KEYS = BASE_KEYS + ("challenge",)
R76_KEYS = R75_KEYS + ("anchor-quote", "anchor-quote-chars", "anchor-found",
                       "anchor-in-window", "bytes-rule", "claims-source",
                       "claims-frozen")
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


def verify_file(path, cfg, quote=None, anchor=None, min_window=None,
                allow_file=False):
    """Re-read an evidence file and check it the way the counter will.

    Returns (problems, header, window).  Checks: the required keys exist; the
    status is 200 and the access date is the claims' date; the stored window is
    one line of >= min_window characters; its sha256 and byte length match the
    header (`window-sha256` recomputed from the stored bytes); the quote occurs
    in it after whole-string NFKC + whitespace folding; and -- round 76 -- the
    ROW'S ANCHOR SPAN occurs in it too, with `anchor-found:`/`anchor-in-window:`
    saying yes and a non-empty `bytes-rule:`/`claims-source:`.

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
    for key in (R76_KEYS if is_r76 else R75_KEYS):
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
        if (head.get("find") or "").strip().lower().startswith("(none supplied)") \
                and is_pdf:
            problems.append("a PDF capture carries no locator: the window must "
                            "be cut by --find, never by the head")
    challenge = (head.get("challenge") or "").strip().lower()
    if challenge and challenge != "none":
        problems.append("the served body carries a %s challenge (%s): the "
                        "source was met, not opened"
                        % (challenge, head.get("challenge-detail", "")[:80]))
    return problems, head, win


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
          "quote-in-window=yes anchor-in-window=%s access-date=%s "
          "http-status=%s"
          % (args.verify, head["window-sha256"], len(win.encode("utf-8")),
             len(win), head.get("anchor-in-window", "n/a"),
             head["access-date"], head["http-status"]))
    return 0


# --------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------

def parse_args(argv):
    ap = argparse.ArgumentParser(
        prog="capture-evidence.py",
        description="Capture one URL's bytes, quote and anchor span into a "
                    "round-76 evidence file. The round tokens come from the "
                    "frozen claims.json (--repo/--freeze).")
    ap.add_argument("--id", help="evidence id (default: the --out file stem)")
    ap.add_argument("--url", help="URL to fetch (http(s)://, file:// or a path)")
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
                    help="the revision holding reports/round-76/claims.json "
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


def capture(args, cfg):
    quote = read_span(args, "quote", "quote_file", "quote")
    anchor = ""
    if args.anchor_quote or args.anchor_quote_file:
        anchor = read_span(args, "anchor_quote", "anchor_quote_file",
                           "anchor-quote")
    if cfg.anchor_required and not anchor:
        raise CaptureError("--anchor-quote is required: round 76 binds the "
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
    work = make_work_dir(args.work)
    try:
        meta = fetch(args.url, args.ua or cfg.ua, work, args.retries)
        text, extract_line = extract_text(meta["body"], meta["content_type"], work)
        # A served challenge is named, not passed (QUALITY 10): the wall is what
        # the run must record, so a challenge body skips the anchor gates and is
        # written with `challenge:` set, then exits 6.
        challenge, _ = detect_challenge(meta["body"], meta["content_type"], text)
        ctype = (meta["content_type"] or "").lower()
        is_pdf = ctype.startswith("application/pdf") or meta["body"][:5] == b"%PDF-"
        if is_pdf and not find and cfg.find_required_for_pdf:
            return _refuse(cfg, ident,
                           "a PDF capture needs --find: the window is cut by "
                           "the locator's page (its first occurrence in the "
                           "whole decoded document), never by the head")
        hit = locate(text, quote)
        anchor_hit = locate(text, anchor) if anchor else {"found": False,
                                                          "start": None,
                                                          "end": None}
        find_hit = locate(text, find) if find else None
        if cfg.anchor_required and not anchor_hit["found"] and not challenge:
            return _refuse(cfg, ident,
                           "the row's anchor span is absent from the extracted "
                           "text (%d characters decoded): the anchor is not on "
                           "the opened document" % len(collapse(text)))
        if find_hit is not None and not find_hit["found"]:
            return _refuse(cfg, ident,
                           "the locator string is absent from the decoded "
                           "document (%d characters): --find names a page the "
                           "document does not carry" % len(collapse(text)))
        visible = collapse(text)
        pages = page_count(text) if is_pdf else None
        if not hit["found"]:
            scope = "none"
            window_text, wstart, wend = "", 0, 0
        elif len(visible) < min_window:
            scope = "whole-document"
            window_text, wstart, wend = visible, 0, len(text)
        else:
            scope = "excerpt"
            centre = find_hit if find_hit else hit
            window_text, wstart, wend = make_window(text, centre, pad, min_window)
        if window_text and not challenge:
            if not folded_has(window_text, anchor):
                where = ("the anchor sits at char %d and the window covers "
                         "chars %d-%d" % (anchor_hit["start"], wstart, wend)
                         if anchor_hit["found"] else "the anchor was not located")
                return _refuse(cfg, ident,
                               "the row's anchor span is absent from the stored "
                               "window after NFKC+whitespace folding (%s): cut "
                               "the window with --find on the anchor's page, or "
                               "raise --pad" % where)
            if hit["found"] and not folded_has(window_text, quote):
                return _refuse(cfg, ident,
                               "the quote is absent from the window cut around "
                               "the locator (char %d): the quote and the "
                               "locator name different places"
                               % (find_hit["start"] if find_hit else -1))
        if is_pdf:
            find_page = str(page_at(text, find_hit["start"])) if find_hit else "-"
            window_pages = ("%d..%d" % (page_at(text, wstart),
                                        page_at(text, max(wstart, wend - 1)))
                            if window_text else "-")
            page_total = str(pages)
        else:
            find_page, window_pages, page_total = "-", "-", "-"
        bind = {
            "anchor": anchor,
            "anchor_hit": anchor_hit,
            "find_line": ("%s (first occurrence at char %d of %d)"
                          % (collapse(find), find_hit["start"], len(text))
                          if find_hit else "(none supplied)"),
            "find_char": str(find_hit["start"]) if find_hit else "-",
            "find_page": find_page,
            "find_hits": count_fold(text, find) if find else 0,
            "page_count": page_total,
            "window_pages": window_pages,
        }
        document, digest, window_digest = render(
            ident, args.url, meta, meta["body"], text, extract_line, quote, hit,
            args.locator, pad, min_window, window_text, scope, len(visible),
            cfg, bind, access_date)
        out_dir = os.path.dirname(os.path.abspath(args.out))
        if out_dir:
            os.makedirs(out_dir, exist_ok=True)
        with open(args.out, "w", encoding="utf-8") as fh:
            fh.write(document)
        in_window = "yes" if (window_text and folded_has(window_text, anchor)) else "no"
        print("EVIDENCE %s: quote-found=%s verbatim=%s anchor-in-window=%s "
              "http=%s bytes=%d sha256=%s window-chars=%d window-scope=%s "
              "window-sha256=%s find-page=%s -> %s"
              % (ident, "yes" if hit["found"] else "no",
                 "yes" if hit["verbatim"] else "no", in_window,
                 meta["http"], len(meta["body"]), digest[:16],
                 len(window_text), scope, window_digest[:16],
                 bind["find_page"], args.out))
        if meta["http"] not in ("200", "file"):
            print("EVIDENCE %s: HTTP %s is not 200 — the capture is not citable"
                  % (ident, meta["http"]), file=sys.stderr)
            return 4
        challenge = (head_challenge(document) or "").strip().lower()
        if challenge and challenge != "none":
            print("EVIDENCE %s: the served body carries a %s challenge — the "
                  "challenge was MET, not passed, so the source is UNOPENED "
                  "and the capture is not citable" % (ident, challenge),
                  file=sys.stderr)
            return 6
        if not hit["found"]:
            print("EVIDENCE %s: quote not found in the extracted text — the "
                  "capture is not citable" % ident, file=sys.stderr)
            return 3
        problems, head, win = verify_file(args.out, cfg, quote, anchor,
                                          min_window,
                                          allow_file=(meta["http"] == "file"))
        for problem in problems:
            print("EVIDENCE %s: verify: %s" % (ident, problem), file=sys.stderr)
        if problems:
            print("%s: VERIFY FAIL: %s (%d problem(s)); the file was left on disk"
                  % (cfg.verdict_prefix, args.out, len(problems)))
            return 5
        print("VERIFY OK: %s window-sha256=%s window-bytes=%d window-chars=%d "
              "quote-in-window=yes anchor-in-window=yes"
              % (args.out, head["window-sha256"], len(win.encode("utf-8")),
                 len(win)))
        print("%s: CAPTURE OK: %s window-sha256=%s window-bytes=%d "
              "window-chars=%d quote-in-window=yes anchor-in-window=yes "
              "claims-frozen=%s"
              % (cfg.verdict_prefix, args.out, head["window-sha256"],
                 len(win.encode("utf-8")), len(win), cfg.claims_frozen))
        return 0
    finally:
        shutil.rmtree(work, ignore_errors=True)


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

# Fixtures are committed next to the tool when there are any, so the selftest
# can run on the bytes a reader can read; the inline fallbacks keep a copy of
# the tool self-testing.
FIXTURE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fixtures")


def _fixture(name, fallback):
    path = os.path.join(FIXTURE_DIR, name)
    try:
        with open(path, "r", encoding="utf-8") as fh:
            return fh.read()
    except OSError:
        return fallback


def _fixture_html():
    return _fixture("r76-fixture.html", """<!doctype html>
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
""" % (FILLER, CJK_ANCHOR, FILLER))


def _fixture_edge_html():
    return _fixture("r76-edge.html",
                    "<html><body><p>%s</p><p>%s</p></body></html>"
                    % (EDGE_QUOTE, FILLER))


def _fixture_short_html():
    return _fixture("r76-short.html",
                    "<html><body><p>%s</p><p>ほんの少しの本文です。</p></body></html>"
                    % SHORT_QUOTE)


def _fixture_challenge_html():
    return _fixture("r76-challenge.html",
                    "<html><head><title>Checking your browser</title></head>"
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
            try:
                self.wfile.write(body)
            except OSError:
                pass
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


def _fixture_repo(root, claims, message):
    """A throwaway git repo holding reports/round-76/claims.json; returns its
    HEAD revision.  The identity is scoped to these commits only."""
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
        "round": 76,
        "base": "98c486bdb4650ba5b8e651d332910e8ee60ad121",
        "frozen": "2026-10-27",
        "claims": [{"id": "C", "axis": "coverage",
                    "title": "calendar and era instruments"}],
        "capture": {
            "access_date": "2026-10-27",
            "min_window": 4096,
            "min_pad": 400,
            "default_pad": 400,
            "evidence_dir": "reports/round-76/evidence",
            "verdict_prefix": "ACCEPT-C-76",
            "window_rule": WINDOW_RULE_GRAMMAR,
            "ua": UA_BROWSER,
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

    def headers(path):
        return _header_map(_read(path)) if os.path.exists(path) else {}

    html_path = os.path.join(tmp, "fixture.html")
    edge_path = os.path.join(tmp, "edge.html")
    short_path = os.path.join(tmp, "short.html")
    far_path = os.path.join(tmp, "far.html")
    challenge_path = os.path.join(tmp, "challenge.html")
    with open(html_path, "w", encoding="utf-8") as fh:
        fh.write(_fixture_html())
    with open(edge_path, "w", encoding="utf-8") as fh:
        fh.write(_fixture_edge_html())
    with open(short_path, "w", encoding="utf-8") as fh:
        fh.write(_fixture_short_html())
    with open(far_path, "w", encoding="utf-8") as fh:
        fh.write(_fixture_far_anchor_html())
    with open(challenge_path, "w", encoding="utf-8") as fh:
        fh.write(_fixture_challenge_html())
    ev = os.path.join(tmp, "evidence")
    os.makedirs(ev, exist_ok=True)

    try:
        repo, rev = _fixture_repo(tmp, _claims_doc(), "r76 claims fixture")
        common = ["--repo", repo, "--freeze", rev]

        # 0. the tool contains no literal scratch root (prompt §7.4)
        try:
            source = _read(os.path.abspath(__file__))
        except OSError as e:
            source = ""
            check("source-readable", False, str(e))
        # the needle is composed so this check does not carry the literal it bans
        banned = "/" + "tmp"
        check("no-tmp-literal",
              source and ('"' + banned) not in source
              and (banned + "/") not in source,
              "source carries a literal scratch root")

        # 1. claims are read through `git show <freeze>:reports/round-76/claims.json`
        code, outlog, err = _run(common + ["--print-config"])
        conf = json.loads(outlog) if outlog.strip().startswith("{") else {}
        check("claims-git-read",
              code == 0 and conf.get("round") == 76
              and conf.get("claims_frozen") == "yes"
              and conf.get("access_date") == "2026-10-27"
              and conf.get("evidence_dir") == "reports/round-76/evidence"
              and conf.get("verdict_prefix") == "ACCEPT-C-76"
              and conf.get("base", "").startswith("98c486b")
              and conf.get("provenance", {}).get("access_date")
              == "claims.capture.access_date"
              and "git show %s:%s" % (rev, CLAIMS_PATH) == conf.get("claims_source"),
              "exit=%d conf=%r err=%r" % (code, conf, err.strip()[:120]))

        # 2. a claims variant moves the constants: access date, min window,
        #    evidence dir and prefix are not hardcoded
        repo2, rev2 = _fixture_repo(
            tmp, _claims_doc(capture={"access_date": "2026-11-01",
                                      "min_window": 8192,
                                      "evidence_dir": "reports/round-76/alt",
                                      "verdict_prefix": "ACCEPT-C-76-ALT"}),
            "r76 claims variant")
        # 2a. an access-date mismatch is refused (exit 2, no file)
        out2a = os.path.join(ev, "V0.txt")
        code, _, err = _run(["--repo", repo2, "--freeze", rev2,
                             "--url", "file://" + html_path, "--quote", CJK_QUOTE,
                             "--anchor-quote", CJK_ANCHOR, "--out", out2a,
                             "--access-date", "2026-10-27", "--allow-file"])
        check("claims-constant-refusal",
              code == 2 and not os.path.exists(out2a)
              and "differs from the claims" in err,
              "exit=%d err=%r" % (code, err.strip()[:120]))

        out2 = os.path.join(ev, "V1.txt")
        code, outlog, err = _run(["--repo", repo2, "--freeze", rev2,
                                  "--url", "file://" + html_path, "--quote", CJK_QUOTE,
                                  "--anchor-quote", CJK_ANCHOR, "--out", out2,
                                  "--allow-file"])
        head2 = headers(out2)
        win2 = _block(_read(out2), "window") or "" if os.path.exists(out2) else ""
        check("claims-variant-constants",
              code == 0 and head2.get("access-date") == "2026-11-01"
              and len(win2) >= 8192
              and head2.get("window", "").find("min=8192") > 0,
              "exit=%d access-date=%r window=%r err=%r"
              % (code, head2.get("access-date"), head2.get("window"),
                 err.strip()[:100]))

        # 2b. a claims document with no round token is refused, and the refusal
        #     names the key
        repo3, rev3 = _fixture_repo(tmp, {"base": "98c486bdb4650ba5b8e651d332910e8ee60ad121",
                                          "frozen": "2026-10-27"},
                                    "r76 claims without a round")
        out2b = os.path.join(ev, "V2.txt")
        code, _, err = _run(["--repo", repo3, "--freeze", rev3,
                             "--url", "file://" + html_path, "--quote", CJK_QUOTE,
                             "--anchor-quote", CJK_ANCHOR, "--out", out2b,
                             "--allow-file"])
        check("claims-missing-round",
              code == 2 and not os.path.exists(out2b) and "`round`" in err,
              "exit=%d err=%r" % (code, err.strip()[:140]))

        # 3. file:// + CJK: the full round-76 grammar, window >= 4096, digest,
        #    and the anchor bound inside the window
        out3 = os.path.join(ev, "F1.txt")
        code, outlog, err = _run(common + ["--id", "F1", "--url", "file://" + html_path,
                                           "--quote", CJK_QUOTE,
                                           "--anchor-quote", CJK_ANCHOR,
                                           "--out", out3, "--locator", "fixture p2",
                                           "--allow-file"])
        text3 = _read(out3) if os.path.exists(out3) else ""
        head3 = headers(out3)
        window3 = _block(text3, "window") or ""
        quote3 = _block(text3, "quote") or ""
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
        check("file-cjk-window",
              code == 0
              and head3.get("quote-found") == "yes"
              and head3.get("quote-found-verbatim") == "yes"
              and head3.get("anchor-found") == "yes"
              and head3.get("anchor-in-window") == "yes"
              and head3.get("anchor-quote") == CJK_ANCHOR
              and head3.get("anchor-quote-chars") == str(len(CJK_ANCHOR))
              and head3.get("quote-in-anchor") == "yes"
              and geo is not None
              and int(geo.group(1)) >= 4096 and int(geo.group(1)) == len(window3)
              and int(geo.group(4)) >= 400 and int(geo.group(5)) >= 400
              and "\n" not in window3
              and folded_has(window3, CJK_QUOTE) and folded_has(window3, CJK_ANCHOR)
              and head3.get("window-sha256")
              == hashlib.sha256(window3.encode("utf-8")).hexdigest()
              and head3.get("window-bytes") == str(len(window3.encode("utf-8")))
              and head3.get("window-scope") == "excerpt"
              and int(head3.get("visible-chars", "0")) >= len(window3)
              and quote3.strip() == CJK_QUOTE
              and head3.get("bytes-rule", "").startswith("bytes:/sha256:")
              and head3.get("claims-frozen") == "yes"
              and head3.get("claims-source", "").startswith("git show ")
              and head3.get("access-date") == "2026-10-27"
              and head3.get("quote-chars") == str(len(CJK_QUOTE))
              and len(head_pos) == len(order) and head_pos == sorted(head_pos)
              and "VERIFY OK" in outlog and "CAPTURE OK" in outlog,
              "exit=%d err=%r window=%r geo=%r" % (code, err.strip(), head3.get("window"), geo))

        # 4. an anchor absent from the document: refused, nothing written
        out4 = os.path.join(ev, "F4.txt")
        code, _, err = _run(common + ["--url", "file://" + html_path,
                                      "--quote", CJK_QUOTE,
                                      "--anchor-quote", "この錨はページに存在しません",
                                      "--out", out4, "--allow-file"])
        check("anchor-absent-document",
              code == 7 and not os.path.exists(out4)
              and "absent from the extracted text" in err and "REFUSED" in err,
              "exit=%d exists=%s err=%r"
              % (code, os.path.exists(out4), err.strip()[:140]))

        # 5. an anchor outside the window: refused -- the R75-M2 / S888 shape
        out5 = os.path.join(ev, "F5.txt")
        code, _, err = _run(common + ["--url", "file://" + far_path,
                                      "--quote", CJK_QUOTE,
                                      "--anchor-quote", FAR_ANCHOR,
                                      "--out", out5, "--allow-file"])
        check("anchor-outside-window",
              code == 7 and not os.path.exists(out5)
              and "absent from the stored window" in err
              and "cut the window with --find" in err,
              "exit=%d exists=%s err=%r"
              % (code, os.path.exists(out5), err.strip()[:180]))

        # 6. an anchor that matches only the whitespace-free tier cannot be
        #    confirmed by the counter's fold: refused, not written
        out6 = os.path.join(ev, "F6.txt")
        code, _, err = _run(common + ["--url", "file://" + html_path,
                                      "--quote", SPACED_QUOTE,
                                      "--anchor-quote", SPACED_ANCHOR,
                                      "--out", out6, "--allow-file"])
        check("anchor-fold-refused",
              code == 7 and not os.path.exists(out6)
              and "absent from the stored window after NFKC" in err,
              "exit=%d exists=%s err=%r"
              % (code, os.path.exists(out6), err.strip()[:160]))

        # 7. a missing --anchor-quote is a usage error (no file)
        out7 = os.path.join(ev, "F7.txt")
        code, _, err = _run(common + ["--url", "file://" + html_path,
                                      "--quote", CJK_QUOTE, "--out", out7,
                                      "--allow-file"])
        check("anchor-required",
              code == 2 and not os.path.exists(out7) and "--anchor-quote" in err,
              "exit=%d err=%r" % (code, err.strip()[:120]))

        # 8. absent quote: file written, window empty, exit 3
        out8 = os.path.join(ev, "F8.txt")
        code, _, err = _run(common + ["--url", "file://" + html_path,
                                      "--quote", "この文はページに存在しません",
                                      "--anchor-quote", CJK_ANCHOR,
                                      "--out", out8])
        text8 = _read(out8) if os.path.exists(out8) else ""
        head8 = _header_map(text8)
        check("quote-missing",
              code == 3 and head8.get("quote-found") == "no"
              and head8.get("anchor-in-window") == "no"
              and (_block(text8, "window") or "").strip() == ""
              and "存在しません" in (_block(text8, "quote") or "")
              and "not citable" in err,
              "exit=%d found=%r err=%r"
              % (code, head8.get("quote-found"), err.strip()[:100]))

        # 9. extractor drops script/style/comments, decodes entities, and the
        #    reader still finds the CJK narrative quote verbatim
        out9 = os.path.join(ev, "F9.txt")
        code, _, _ = _run(common + ["--url", "file://" + html_path,
                                    "--quote", NARR_QUOTE,
                                    "--anchor-quote", NARR_ANCHOR,
                                    "--out", out9, "--allow-file"])
        head9 = headers(out9)
        check("extract-visible",
              code == 0
              and all(m not in text3 for m in ("SCRIPT_ONLY_TEXT", "STYLE_ONLY_TEXT",
                                               "COMMENT_ONLY_TEXT"))
              and "アンパサンド & と山括弧 <tag>" in text3
              and "fixture title" not in text3
              and head9.get("quote-found-verbatim") == "yes",
              "exit=%d script-leak=%s" % (code, "SCRIPT_ONLY_TEXT" in text3))

        # 9b. an anchor argument that is itself line-wrapped (a registry cell
        #     that wraps) is collapsed for the stored line and its count, so the
        #     file still self-verifies
        out9b = os.path.join(ev, "F9b.txt")
        wrapped = "The settings note holds\nfive sections in one file."
        code, _, err = _run(common + ["--url", "file://" + html_path,
                                      "--quote", LATIN_QUOTE,
                                      "--anchor-quote", wrapped,
                                      "--out", out9b, "--allow-file"])
        head9b = headers(out9b)
        check("anchor-wrapped-argument",
              code == 0 and head9b.get("anchor-quote") == LATIN_ANCHOR
              and head9b.get("anchor-quote-chars") == str(len(LATIN_ANCHOR))
              and head9b.get("anchor-in-window") == "yes"
              and head9b.get("quote-in-anchor") == "yes",
              "exit=%d anchor=%r chars=%r err=%r"
              % (code, head9b.get("anchor-quote"), head9b.get("anchor-quote-chars"),
                 err.strip()[:120]))

        # 10. quote at the very start of the text: before small, window >= 4096
        out10 = os.path.join(ev, "F10.txt")
        code, _, _ = _run(common + ["--url", "file://" + edge_path,
                                    "--quote", EDGE_QUOTE,
                                    "--anchor-quote", EDGE_QUOTE,
                                    "--out", out10, "--allow-file"])
        head10 = headers(out10)
        geo10 = re.match(r"chars=(\d+) min=(\d+) pad=(\d+) before=(\d+) after=(\d+)",
                         head10.get("window", ""))
        check("window-edge",
              code == 0 and head10.get("anchor-in-window") == "yes"
              and geo10 is not None and int(geo10.group(4)) == 0
              and int(geo10.group(1)) >= 4096 and int(geo10.group(5)) >= 400,
              "exit=%d window=%r" % (code, head10.get("window")))

        # 11. a document shorter than the window minimum is stored whole and
        #     declared; the anchor is inside it, so the capture verifies
        out11 = os.path.join(ev, "F11.txt")
        code, _, err = _run(common + ["--url", "file://" + short_path,
                                      "--quote", SHORT_QUOTE,
                                      "--anchor-quote", SHORT_QUOTE,
                                      "--out", out11, "--allow-file"])
        text11 = _read(out11) if os.path.exists(out11) else ""
        head11 = _header_map(text11)
        win11 = _block(text11, "window") or ""
        check("window-whole-document",
              code == 0 and head11.get("window-scope") == "whole-document"
              and head11.get("visible-chars") == str(len(win11))
              and len(win11) < 4096
              and head11.get("anchor-in-window") == "yes"
              and head11.get("window-sha256")
              == hashlib.sha256(win11.encode("utf-8")).hexdigest(),
              "exit=%d err=%r scope=%r visible=%r win=%d"
              % (code, err.strip()[:80], head11.get("window-scope"),
                 head11.get("visible-chars"), len(win11)))

        # 12. whole-document is not a shortcut: a truncated window and a forged
        #     scope both fail verification
        trunc = os.path.join(ev, "F11-trunc.txt")
        with open(trunc, "w", encoding="utf-8") as fh:
            fh.write(text11.replace(win11, win11[:-6], 1))
        code_tr, _, err_tr = _run(common + ["--verify", trunc, "--allow-file"])
        forged = os.path.join(ev, "F1-forged.txt")
        lines_f = [("window-scope: whole-document"
                    if line.startswith("window-scope:") else line)
                   for line in text3.splitlines()]
        with open(forged, "w", encoding="utf-8") as fh:
            fh.write("\n".join(lines_f) + "\n")
        code_fg, _, err_fg = _run(common + ["--verify", forged, "--allow-file"])
        check("whole-document-guard",
              code_tr == 5 and "but visible-chars says" in err_tr
              and code_fg == 5 and "whole-document claimed" in err_fg,
              "trunc=%d forged=%d err=%r"
              % (code_tr, code_fg, (err_tr + err_fg).strip()[:140]))

        # 13. an anchor stripped from a valid file fails verification (R75-M2
        #     is graded, not decorative)
        stripped = os.path.join(ev, "F1-noanchor.txt")
        lines_s = [line for line in text3.splitlines()
                   if not line.startswith(("anchor-quote:", "anchor-in-window:"))]
        with open(stripped, "w", encoding="utf-8") as fh:
            fh.write("\n".join(lines_s) + "\n")
        code_s, _, err_s = _run(common + ["--verify", stripped, "--allow-file"])
        win_edit = os.path.join(ev, "F1-window-edit.txt")
        with open(win_edit, "w", encoding="utf-8") as fh:
            fh.write(text3.replace(window3, window3[:-4] + "XXXX", 1))
        code_w, _, err_w = _run(common + ["--verify", win_edit, "--allow-file"])
        digest_edit = os.path.join(ev, "F1-digest-edit.txt")
        lines_d = [("window-sha256: " + "0" * 64)
                   if line.startswith("window-sha256:") else line
                   for line in text3.splitlines()]
        with open(digest_edit, "w", encoding="utf-8") as fh:
            fh.write("\n".join(lines_d) + "\n")
        code_d, _, err_d = _run(common + ["--verify", digest_edit, "--allow-file"])
        check("verify-mode",
              code_s == 5 and "anchor" in err_s
              and code_w == 5 and "window-sha256 mismatch" in err_w
              and code_d == 5 and "window-sha256 mismatch" in err_d,
              "anchor=%d window=%d digest=%d err=%r"
              % (code_s, code_w, code_d, (err_s + err_w + err_d).strip()[:160]))

        # 14. http.server: UA sent, status, bytes, sha256, GET line, retry
        _FixtureHandler.payload = _fixture_html().encode("utf-8")
        _FixtureHandler.seen = []
        server = ThreadingHTTPServer(("127.0.0.1", 0), _FixtureHandler)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        base = "http://127.0.0.1:%d" % server.server_address[1]
        try:
            out14 = os.path.join(ev, "F14.txt")
            code, _, _ = _run(common + ["--url", base + "/fixture.html",
                                        "--quote", CJK_QUOTE,
                                        "--anchor-quote", CJK_ANCHOR,
                                        "--out", out14])
            text14 = _read(out14)
            head14 = _header_map(text14)
            sent = {ua for path, ua in _FixtureHandler.seen if path == "/fixture.html"}
            body_len = len(_FixtureHandler.payload)
            check("http-fetch",
                  code == 0 and head14.get("http") == "200"
                  and head14.get("http-status") == "200"
                  and head14.get("user-agent") == UA_BROWSER
                  and head14.get("ua") == UA_BROWSER
                  and sent == {UA_BROWSER}
                  and head14.get("bytes") == str(body_len)
                  and head14.get("sha256")
                  == hashlib.sha256(_FixtureHandler.payload).hexdigest()
                  and head14.get("fetch") == "GET " + base + "/fixture.html"
                  and head14.get("content-length") == str(body_len)
                  and head14.get("transferred-bytes") == str(body_len)
                  and head14.get("fetch-attempts") == "1"
                  and "curl -sS -L" in head14.get("fetch-command", ""),
                  "exit=%d head=%r seen=%r"
                  % (code, {k: head14.get(k) for k in ("http", "bytes", "user-agent")},
                     sent))

            out14b = os.path.join(ev, "F14b.txt")
            _FixtureHandler.flaky["left"] = 1
            code, _, err = _run(common + ["--url", base + "/flaky.html",
                                          "--quote", CJK_QUOTE,
                                          "--anchor-quote", CJK_ANCHOR,
                                          "--out", out14b])
            head14b = headers(out14b)
            check("fetch-retry",
                  code == 0 and head14b.get("http") == "200"
                  and head14b.get("fetch-attempts") == "2"
                  and head14b.get("bytes") == str(body_len),
                  "exit=%d attempts=%r err=%r"
                  % (code, head14b.get("fetch-attempts"), err.strip()[:100]))

            out14c = os.path.join(ev, "F14c.txt")
            _FixtureHandler.flaky["left"] = 6
            code, _, err = _run(common + ["--url", base + "/flaky.html",
                                          "--quote", CJK_QUOTE,
                                          "--anchor-quote", CJK_ANCHOR,
                                          "--out", out14c, "--retries", "1"])
            check("fetch-retry-gives-up",
                  code == 2 and not os.path.exists(out14c)
                  and "curl exit 18 after 2 attempt(s)" in err,
                  "exit=%d err=%r" % (code, err.strip()[:120]))
            _FixtureHandler.flaky["left"] = 0

            out14d = os.path.join(ev, "F14d.txt")
            code, _, err = _run(common + ["--url", base + "/missing.html",
                                          "--quote", "not here",
                                          "--anchor-quote", "not here",
                                          "--out", out14d])
            head14d = headers(out14d)
            check("http-not-200",
                  code == 4 and head14d.get("http") == "404" and "not citable" in err,
                  "exit=%d http=%r" % (code, head14d.get("http")))
        finally:
            server.shutdown()
            server.server_close()

        # 15. a bot challenge is named, not passed: the file records it, the run
        #     exits 6, and the source stays UNOPENED
        out15 = os.path.join(ev, "F15.txt")
        code, _, err = _run(common + ["--url", "file://" + challenge_path,
                                      "--quote", CJK_QUOTE,
                                      "--anchor-quote", CJK_ANCHOR,
                                      "--out", out15, "--allow-file"])
        head15 = _header_map(_read(out15)) if os.path.exists(out15) else {}
        check("challenge-detected",
              code == 6 and head15.get("challenge") == "js-challenge"
              and "enable javascript" in head15.get("challenge-detail", "").lower()
              and "UNOPENED" in err,
              "exit=%d challenge=%r err=%r"
              % (code, head15.get("challenge"), err.strip()[:120]))

        # 16. PDF: no --find is refused; --find cuts the window by the locator's
        #     page and the file records find-page/page-count/window-pages
        if shutil.which("pdftotext") is None:
            check("pdf-find-required", True, "SKIPPED: pdftotext absent")
            check("pdf-find-page", True, "SKIPPED: pdftotext absent")
            check("pdf-find-first-occurrence", True, "SKIPPED: pdftotext absent")
            check("pdf-bytes-rule", True, "SKIPPED: pdftotext absent")
        else:
            pdf_path = os.path.join(tmp, "fixture-pdf.pdf")
            with open(pdf_path, "wb") as fh:
                fh.write(_pdf(_pdf_pages("PDF fixture quote sentence.",
                                         "PDF fixture anchor span.",
                                         locator_on_page=5)))
            out16 = os.path.join(ev, "F16.txt")
            code, _, err = _run(common + ["--url", "file://" + pdf_path,
                                          "--quote", "PDF fixture quote sentence.",
                                          "--anchor-quote", "PDF fixture anchor span.",
                                          "--out", out16, "--allow-file"])
            check("pdf-find-required",
                  code == 7 and not os.path.exists(out16)
                  and "needs --find" in err,
                  "exit=%d exists=%s err=%r"
                  % (code, os.path.exists(out16), err.strip()[:140]))

            out16b = os.path.join(ev, "F16b.txt")
            code, outlog, err = _run(common + ["--url", "file://" + pdf_path,
                                               "--quote", "PDF fixture quote sentence.",
                                               "--anchor-quote", "PDF fixture anchor span.",
                                               "--find", "LOCATOR-MARKER page five",
                                               "--locator", "p. 5",
                                               "--out", out16b, "--allow-file"])
            text16b = _read(out16b) if os.path.exists(out16b) else ""
            head16b = _header_map(text16b)
            win16b = _block(text16b, "window") or ""
            pages16 = re.match(r"^(\d+)\.\.(\d+)$", head16b.get("window-pages", ""))
            check("pdf-find-page",
                  code == 0 and head16b.get("find-page") == "5"
                  and pages16 is not None
                  and int(pages16.group(1)) <= 5 <= int(pages16.group(2))
                  and int(head16b.get("page-count", "0")) >= 5
                  and head16b.get("anchor-in-window") == "yes"
                  and folded_has(win16b, "PDF fixture quote sentence.")
                  and folded_has(win16b, "PDF fixture anchor span.")
                  and head16b.get("window-sha256")
                  == hashlib.sha256(win16b.encode("utf-8")).hexdigest()
                  and head16b.get("fetch") == "GET file://" + pdf_path
                  and "pdftotext -enc UTF-8" in head16b.get("extract", ""),
                  "exit=%d err=%r find-page=%r pages=%r window-pages=%r page-count=%r"
                  % (code, err.strip()[:120], head16b.get("find-page"), pages16,
                     head16b.get("window-pages"), head16b.get("page-count")))

            # the locator's FIRST occurrence wins: the marker on page 2 moves
            # the window to p. 2, so the p. 5 quote is refused rather than
            # silently windowed at the head
            out16c = os.path.join(ev, "F16c.txt")
            code, _, err = _run(common + ["--url", "file://" + pdf_path,
                                          "--quote", "PDF fixture quote sentence.",
                                          "--anchor-quote", "PDF fixture anchor span.",
                                          "--find", "LOCATOR-MARKER",
                                          "--out", out16c, "--allow-file"])
            check("pdf-find-first-occurrence",
                  code == 7 and not os.path.exists(out16c)
                  and "absent from the stored window" in err,
                  "exit=%d exists=%s err=%r"
                  % (code, os.path.exists(out16c), err.strip()[:160]))

            check("pdf-bytes-rule",
                  head16b.get("bytes-rule", "").startswith("bytes:/sha256:")
                  and "not canonical" in head16b.get("bytes-rule", ""),
                  "bytes-rule=%r" % (head16b.get("bytes-rule"),))

        # 17. usage floors come from the claims (--min-window / --pad below the
        #     frozen values is a refusal, and nothing is written)
        out17 = os.path.join(ev, "F17.txt")
        code_low, _, _ = _run(common + ["--url", "file://" + html_path,
                                        "--quote", CJK_QUOTE,
                                        "--anchor-quote", CJK_ANCHOR,
                                        "--out", out17, "--min-window", "100",
                                        "--allow-file"])
        code_pad, _, _ = _run(common + ["--url", "file://" + html_path,
                                        "--quote", CJK_QUOTE,
                                        "--anchor-quote", CJK_ANCHOR,
                                        "--out", os.path.join(ev, "F18.txt"),
                                        "--pad", "40", "--allow-file"])
        code_empty, _, _ = _run(common + ["--url", "file://" + html_path,
                                          "--quote", "   ",
                                          "--anchor-quote", CJK_ANCHOR,
                                          "--out", os.path.join(ev, "F19.txt")])
        check("guards",
              code_low == 2 and code_pad == 2 and code_empty == 2
              and not os.path.exists(out17)
              and not os.path.exists(os.path.join(ev, "F18.txt"))
              and not os.path.exists(os.path.join(ev, "F19.txt")),
              "window=%d pad=%d empty=%d" % (code_low, code_pad, code_empty))

        # 18. an uncommitted claims document is recorded as unfrozen
        claims_path = os.path.join(tmp, "claims-rehearsal.json")
        with open(claims_path, "w", encoding="utf-8") as fh:
            json.dump(_claims_doc(), fh)
        out18 = os.path.join(ev, "F20.txt")
        code, _, _ = _run(["--claims-file", claims_path,
                           "--url", "file://" + html_path, "--quote", CJK_QUOTE,
                           "--anchor-quote", CJK_ANCHOR, "--out", out18,
                           "--allow-file"])
        head18 = headers(out18)
        check("claims-file-rehearsal",
              code == 0 and head18.get("claims-frozen") == "no"
              and head18.get("claims-source", "").startswith("file:")
              and "sha256=" in head18.get("claims-source", ""),
              "exit=%d claims-frozen=%r source=%r"
              % (code, head18.get("claims-frozen"),
                 head18.get("claims-source", "")[:80]))
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
