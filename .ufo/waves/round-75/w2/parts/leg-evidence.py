# part: leg-evidence.py — EVIDENCE leg (owner ExecLegEvidence)
#
# Frozen leg text (reports/round-75/claims.json, claim C, legs[4]):
#   "EVIDENCE: reports/round-75/evidence/<id>.txt for every adopted row at
#    <lands>, each with fetch line, the UA used, HTTP status, bytes, the sha256
#    of the fetched body, the stored `--- window ---` text and its own
#    `window-sha256:` which the counter recomputes, with a `window-scope:`
#    header: `excerpt` (window >= 4096 characters around the quote) or
#    `whole-document` (allowed only when the whole extracted visible text is
#    shorter than 4096 characters and equal to the recorded `visible-chars:`);
#    the Gate quote occurs in the stored window after NFKC and whitespace
#    folding"
#
# Readings of the ambiguous wording (each is also stated in the seat report,
# .ufo/waves/round-75/w2/ExecLegEvidence.md):
#
#  R1 "<id>" is the ADOPTED LANE id (cfg["rows"] + cfg["reused"]), one file per
#     adopted row, never a staged id: every other leg keys the row set on the
#     lane ids, and the by-document map is what turns staged ids into them. A
#     staged-only id has no file requirement (and no file is read for it).
#  R2 "fetch line" names the row's document. The file is evidence FOR that row,
#     so its `fetch:`/`url:` URL must name a URL the row's SOURCE cell carries.
#     The join is the shared part-cfg predicate _row_has_url (raw norm_url key
#     union _doc_url_key: host without `www.`, percent-decoded, /doc/page/… and
#     /docAsPDF/… folded to /doc/<slug>, web.archive.org/web/<ts>/<original>
#     folded to <original>). That is what lets one row carry the document URL
#     plus page-level Persee URLs, and what joins S892's committed
#     web.archive.org capture to the iris.unipa.it URL its source cell names.
#     No local URL-matching rule is defined here: `_row_url_keys`' key space is
#     part-cfg's, and an intersection with PART A neutral_url_keys is a
#     DIFFERENT key space (netloc keeps `www.`, no document folding) that would
#     never meet it.
#  R3 "the Gate quote" is read from the Gate admit row's QUOTE COLUMN, not from
#     any quoted text in that row: a source cell carries the document title in
#     `«»` and authenticating the title would not authenticate the quote. When
#     the admit table has no identifiable quote column the leg falls back to
#     every quoted span of the admit row (the round-74 grammar). Candidates are
#     the column's delimited spans UNION the registry row's anchor-cell spans
#     that the column carries after NFKC + whitespace folding, because the GATE
#     leg (leg-gate.py R2/R3) binds an undelimited CJK quote cell to the row's
#     anchor quote: without the second half the two legs would disagree about
#     which string "the Gate quote" is on the drafted S888/S893 cells. At least
#     one candidate of <=25 whitespace tokens and <=80 characters is required
#     (PART A quote_ok) and at least one candidate must occur in the stored
#     window; the GATE leg owns the quote's identity, its size and its locator.
#  R4 "bytes" and "the sha256 of the fetched body" are graded for SHAPE here: a
#     positive byte count and a 64-hex digest. A leg has no network, so it
#     cannot re-derive the body; the ordinary re-open routed in the claim is
#     what binds body truth, and the w1 vacuity finding is reported, not
#     papered over.
#  R5 "the UA used" is graded as browser-shaped: recorded, starting
#     "Mozilla/5.0", and carrying no client/robot token (curl/, Wget/,
#     python-requests, python-urllib, libwww, scrapy, java/, go-http-client,
#     bot, spider, crawler, headless, phantomjs).
#  R6 "no challenge" (claim kill rule; QUALITY 10): the capture must RECORD its
#     challenge state and it must be `none`. A missing `challenge:` line is not
#     proof of a clean response; a met challenge is an UNOPENED source.
#  R7 `quote-found:` / `quote-found-verbatim:` are NEVER read. The capture tool
#     records them for a human; the recomputed window digest and the NFKC +
#     whitespace fold are the grader. A file saying `quote-found: no` whose
#     window does contain the quote PASSES, and a file saying `quote-found: yes`
#     whose window does not PASS-FREE fails.
#  R8 an all-whitespace stored window is a FAIL, never a skip: round-74's
#     counter skipped its quote test on a blank window (`if window is None or
#     not window.strip(): continue`), which let a landing blank every window
#     and grade green (w1 ExecJunkFixtures F2). Here the fold of the window is
#     computed once and an empty fold is reported.
#  R9 `excerpt` has a floor and no ceiling, but a window cannot be longer than
#     the visible text it was cut from: when `visible-chars:` is present on an
#     excerpt it must be >= len(window). This is internal consistency, not a
#     new scope rule - no file the capture tool writes can violate it - and it
#     is the mirror of the tool's own "short window under a long visible-chars"
#     verification rule. `visible-chars:` is REQUIRED only for
#     `whole-document`, which is the only scope the frozen text couples it to.
#  R10 the window is the exact stored bytes: the single line between the
#     `--- window ---` and `--- quote ---` markers, hashed as UTF-8 with no
#     trailing newline (part-cfg _window). `window-bytes:`, when present, must
#     equal that byte length; `window-sha256:` must equal its sha256.
#
# Private helpers are prefixed _evidence_ (the contract's `_<legfile>_` stem).
# Shared helpers (_evidence, _window, _row_url_keys, _gate_admit_row and the
# PART A functions) are CALLED, never redefined.

_EVIDENCE_UA_ROBOT_RE = re.compile(
    r"(?i)(?:curl/|wget/|python-requests|python-urllib|libwww|scrapy"
    r"|java/|go-http-client|phantomjs|headless|bot\b|spider|crawler)")
_EVIDENCE_CLEAN_CHALLENGE = ("", "none")


def _evidence_count(value):
    """A recorded non-negative integer, or None (`12` yes, `1,024` no)."""
    s = (value or "").strip()
    return int(s) if s.isdigit() else None


def _evidence_fold(text):
    """The one fold in play: NFKC, whitespace runs to one space, ends stripped."""
    return nfkc_ws(text or "")


def _evidence_fetch_names_row(fetch, lands_rows, sid):
    """R2: the fetch line names the row's document (part-cfg _row_has_url)."""
    fetch_urls = urls_in(fetch or "")
    if not fetch_urls:
        return False
    return any(_row_has_url(lands_rows, sid, u) for u in fetch_urls)


def _evidence_gate_quote_text(gate_rows, grow):
    """R3: the admit row's quote column, falling back to the whole row."""
    header = table_header(gate_rows, ("quote",))
    if header is None:
        return grow
    qi = col_index(header, ("quote",))
    if qi is None:
        return grow
    cells = row_cells(grow)
    return cells[qi] if qi < len(cells) else grow


def _evidence_anchor_spans(lands_rows, sid):
    """The delimited spans of the registry row's ANCHOR cell (quote_ok only)."""
    row = lands_rows.get(sid)
    if row is None:
        return []
    cells = row_cells(row)
    if len(cells) <= ANCHOR:
        return []
    return [s for s in quoted_spans(cells[ANCHOR]) if quote_ok(s)]


def _evidence_gate_quote_candidates(gate_rows, grow, lands_rows, sid):
    """R3: the strings the Gate record may be carrying as its quote.

    Delimited spans of the quote column, plus the row's anchor spans that the
    column carries after the fold (the undelimited CJK cell GATE's R3 binds).
    Returned folded, empty strings dropped.
    """
    cell = _evidence_gate_quote_text(gate_rows, grow)
    cell_fold = _evidence_fold(cell)
    cands = [_evidence_fold(s) for s in quoted_spans(cell) if quote_ok(s)]
    for span in _evidence_anchor_spans(lands_rows, sid):
        folded = _evidence_fold(span)
        if folded and folded in cell_fold:
            cands.append(folded)
    return [c for c in cands if c]


def _evidence_core(ev, sid, access_date, lands_rows):
    """Header, digest, length and scope checks for one evidence file.

    Returns (bad, window). `window` is the exact stored window string (or None
    when the file stores no window block); the caller runs the quote test on it
    and NEVER skips that test for a short or blank window (R8).

    The scope rule is re-derived from the stored bytes: `excerpt` needs at
    least MIN_WINDOW_CHARS characters; `whole-document` is allowed only when the
    stored window is shorter than MIN_WINDOW_CHARS and its length equals the
    recorded `visible-chars:`. No flag in the file decides either.
    """
    bad = []
    status = (ev.get("http-status") or ev.get("http") or "").strip()
    if status != "200":
        bad.append("%s http-status %r (want 200)" % (sid, status))
    if ev.get("access-date") != access_date:
        bad.append("%s access-date %r (want %s)"
                   % (sid, ev.get("access-date"), access_date))
    size = _evidence_count(ev.get("bytes"))
    if size is None or size <= 0:
        bad.append("%s bytes %r is not a positive byte count"
                   % (sid, (ev.get("bytes") or "")[:20]))
    if not re.fullmatch(r"[0-9a-f]{64}", (ev.get("sha256") or "").strip().lower()):
        bad.append("%s sha256 line is not a 64-hex digest of the fetched body" % sid)
    ua = (ev.get("user-agent") or ev.get("ua") or "").strip()
    if not ua:
        bad.append("%s records no user-agent" % sid)
    elif not ua.startswith("Mozilla/5.0"):
        bad.append("%s user-agent is not browser-shaped: %r" % (sid, ua[:40]))
    elif _EVIDENCE_UA_ROBOT_RE.search(ua):
        bad.append("%s user-agent carries a client/robot token: %r"
                   % (sid, ua[:60]))
    fetch = (ev.get("fetch") or ev.get("url") or "").strip()
    if not fetch:
        bad.append("%s carries no fetch line" % sid)
    elif not _evidence_fetch_names_row(fetch, lands_rows, sid):
        bad.append("%s fetch line does not name the row's document: %r"
                   % (sid, fetch[:70]))
    challenge = ev.get("challenge")
    if challenge is None:
        bad.append("%s records no challenge line (a clean response must say so)"
                   % sid)
    elif challenge.strip().lower() not in _EVIDENCE_CLEAN_CHALLENGE:
        bad.append("%s records a served challenge (%r): a challenge met is an "
                   "UNOPENED source" % (sid, challenge.strip()[:40]))
    window = ev["_window"]
    if window is None:
        bad.append("%s stores no --- window --- block" % sid)
        return bad, None
    payload = window.encode("utf-8")
    digest = hashlib.sha256(payload).hexdigest()
    declared = (ev.get("window-sha256") or "").strip().lower()
    if declared != digest:
        bad.append("%s window-sha256 %r != the recomputed digest of the stored "
                   "window (%s)" % (sid, declared[:16], digest[:16]))
    declared_bytes = (ev.get("window-bytes") or "").strip()
    if declared_bytes and declared_bytes != str(len(payload)):
        bad.append("%s window-bytes %r != the stored window's %d bytes"
                   % (sid, declared_bytes, len(payload)))
    scope = (ev.get("window-scope") or "").strip().lower()
    if scope not in ("excerpt", "whole-document"):
        bad.append("%s window-scope %r (want excerpt|whole-document)"
                   % (sid, (ev.get("window-scope") or "")[:30]))
    visible_raw = ev.get("visible-chars")
    visible = _evidence_count(visible_raw)
    if visible_raw is not None and visible is None:
        bad.append("%s visible-chars %r is not a character count"
                   % (sid, (visible_raw or "")[:20]))
    if scope == "excerpt":
        if len(window) < MIN_WINDOW_CHARS:
            bad.append("%s excerpt window is %d characters (want >= %d)"
                       % (sid, len(window), MIN_WINDOW_CHARS))
        elif visible is not None and visible < len(window):
            bad.append("%s excerpt window is %d characters but the recorded "
                       "visible text is %d (a window cannot exceed its document)"
                       % (sid, len(window), visible))
    elif scope == "whole-document":
        if visible is None:
            bad.append("%s whole-document window records no visible-chars" % sid)
        else:
            if len(window) >= MIN_WINDOW_CHARS:
                bad.append("%s whole-document window is %d characters (>= %d: "
                           "declare excerpt)" % (sid, len(window),
                                                 MIN_WINDOW_CHARS))
            if visible != len(window):
                bad.append("%s whole-document window is %d characters but "
                           "visible-chars is %d" % (sid, len(window), visible))
    return bad, window


def leg_evidence(ctx):
    """EVIDENCE (H2/R1-R10): a committed capture per adopted/reused row - fetch
    line naming the row's document, browser-shaped UA, HTTP 200, recorded bytes,
    64-hex body digest, a stored window whose scope rule holds, and the Gate
    quote INSIDE that window after NFKC + whitespace folding. No flag is read
    and a blank window fails rather than skipping the quote test."""
    mat, cfg = ctx["mat"], ctx["cfg"]
    try:
        gate_rows = table_rows(gate_section(read_tree(mat, LESSON)))
        lands_rows = parse_rows(read_tree(mat, REGISTRY))
    except Missing as e:
        return leg("EVIDENCE", False, "%s" % e)
    bad = []
    for sid in cfg["rows"] + cfg["reused"]:
        ev = _evidence(mat, sid)
        if ev is None:
            bad.append("%s evidence file missing (%s/%s.txt)"
                       % (sid, EVIDENCE_DIR, sid))
            continue
        row_bad, window = _evidence_core(ev, sid, cfg["access_date"], lands_rows)
        bad.extend(row_bad)
        if window is None:
            continue
        folded = _evidence_fold(window)
        if not folded:
            bad.append("%s stored window carries no visible text" % sid)
            continue
        grow = _gate_admit_row(gate_rows, sid, lands_rows)
        if grow is None:
            bad.append("%s has no Gate admit row to couple the window to" % sid)
            continue
        qspans = dedupe(_evidence_gate_quote_candidates(gate_rows, grow,
                                                        lands_rows, sid))
        if not qspans:
            bad.append("%s Gate admit row carries no <=25-token, <=80-char quote"
                       % sid)
            continue
        if not any(q in folded for q in qspans):
            bad.append("%s Gate quote is absent from the stored window "
                       "(substring after NFKC+whitespace folding)" % sid)
    return leg("EVIDENCE", not bad, "; ".join(dedupe(bad)))
