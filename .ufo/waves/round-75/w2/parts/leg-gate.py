# ===================================================================== GATE ===
# Claim C, leg GATE (reports/round-75/claims.json, frozen text):
#
#   "corpus/lessons/round-75.md `## Gate` carries per adopted row URL + access
#    date 2026-10-27 + a located quote of at most 25 whitespace tokens and at
#    most 80 characters + locator, and >=1 admit and >=1 reject; every reject
#    row of a probed URL carries its probed URL, reason and flip"
#
# Readings taken here (each one is a decision, recorded in
# .ufo/waves/round-75/w2/ExecLegGate.md; nothing below is stronger or weaker
# than that sentence):
#
#   R1 "per adopted row" = every lane id in cfg["rows"] + cfg["reused"].  The
#      admit row is joined to the registry row by URL first and by id token
#      second, through the shared _gate_admit_row helper (never a second join
#      rule), and the joined row must itself carry one of that registry row's
#      URLs.  A page-level Persee URL counts as the row URL because
#      _row_url_keys carries every URL of the source cell: one document row
#      owns all of its pages.
#   R2 "a located quote" = a quoted span, never a declared count.  Whatever a
#      `quote-words:` field or an `(N chars, M tokens)` note says is ignored:
#      the tokens are recounted from the span by whitespace splitting and the
#      characters by len().  A CJK span is therefore one whitespace token and
#      as many characters as it prints, so a long CJK span fails the
#      80-character cap instead of passing on a fabricated word count.
#      (Whether the span occurs on the opened page is the EVIDENCE leg's window
#      check; GATE never reads a self-attested `quote-found` flag.)
#   R3 "quote == the row's anchor quote" = the Gate span equals, after NFKC and
#      whitespace folding, the span the registry row's anchor cell marks as
#      located: the quoted span(s) after its `quote located:` marker, or every
#      quoted span of the cell when the row carries no marker.  When the cell
#      writes the anchor span without delimiters (the CJK rows are drafted that
#      way), the folded anchor span occurring verbatim in the cell is accepted,
#      so the leg binds the quote's identity to the row and not to a
#      typographic bracket.  This is what keeps a staged, absent-on-page span
#      out of the admit table after a document is re-opened under a new id.
#   R4 "locator" = a place inside the document, not the document itself.  A
#      dash/placeholder cell is no locator and neither is the row URL repeated
#      in the cell: once its URLs are removed at least one alphanumeric
#      character must remain (so `p. 11`, `§3` and `PDF p. 1, abstract` count).
#   R5 ">=1 admit and >=1 reject" = rows of the Gate section's tables, never a
#      prose marker.  A verdict that says both admitted and rejected counts as
#      neither (one row cannot satisfy the two halves at once), reject rows are
#      table rows only, and a rejection written as prose with no probed URL
#      satisfies nothing.
#   R6 "every reject row of a probed URL carries its probed URL, reason and
#      flip" = every reject row lies in a table whose header names reason and
#      flip columns, and it carries its probed URL in that table's probed-URL
#      (or URL) column -- a URL appearing only in the flip cell (the archive
#      copy a refusal flips to) is not the probed URL -- with a non-dash cell
#      in both reason and flip.


def _leg_gate_rows(lines):
    """The Gate section's Markdown table rows: lines that start with `|`.

    PART A's table_rows() also slurps any indented line into the previous row,
    which is how a prose bullet's wrapped continuation line becomes the last
    cell of the table's last row and silently turns that row's verdict into
    prose (the Gate-notes block sits right under the reject table in the
    drafted lesson).  A Markdown table row is one line, so GATE reads one line
    per row and never lets a wrapped note answer for a row.
    """
    return [line.strip() for line in lines if line.lstrip().startswith("|")]


def _leg_gate_sep(row):
    """True for a Markdown table separator row (`|---|---|`, `|:--|--:|`)."""
    cells = [c for c in row_cells(row) if c]
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", c) for c in cells)


def _leg_gate_tables(rows):
    """Split the Gate section's table rows into [{"header":..,"rows":[..]}].

    A table starts at the row directly above its separator row; the header is
    therefore always a real header and a data row that happens to contain the
    word "quote" can never be mistaken for one.  A table written without a
    separator keeps its first row as the header (tolerance, not strength).
    """
    tables = []
    for i, row in enumerate(rows):
        if _leg_gate_sep(row):
            if i == 0:
                continue
            hdr = rows[i - 1]
            if tables and tables[-1]["rows"] and tables[-1]["rows"][-1] == hdr:
                tables[-1]["rows"].pop()
            tables.append({"header": hdr, "rows": []})
            continue
        if tables:
            tables[-1]["rows"].append(row)
    if not tables and rows:
        tables = [{"header": rows[0], "rows": rows[1:]}]
    return tables


def _leg_gate_header(tables, needles):
    """The first table header whose cells satisfy every needle (needles are
    substrings of some cell, compared case-insensitively)."""
    for t in tables:
        cells = [c.lower() for c in row_cells(t["header"])]
        if all(any(n in c for c in cells) for n in needles):
            return row_cells(t["header"])
    return None


def _leg_gate_anchor_quotes(lands_rows, sid):
    """(spans, why) — the anchor quote(s) of the registry row `sid`.

    The located span(s) after the anchor cell's own `quote located:` marker
    when the marker carries any; every quoted span of the cell otherwise.  An
    empty list with a reason means the row cannot bind a quote at all.
    """
    row = lands_rows.get(sid)
    if row is None:
        return [], "no registry row at lands"
    cells = row_cells(row)
    if len(cells) <= ANCHOR:
        return [], "registry row has no anchor cell"
    cell = cells[ANCHOR]
    marker = None
    for marker in re.finditer(r"quote\s+located\s*[:：]", cell, re.I):
        pass
    if marker is not None:
        after = quoted_spans(cell[marker.end():])
        if after:
            return after, None
    spans = quoted_spans(cell)
    if not spans:
        return [], "registry anchor cell carries no quoted span"
    return spans, None


def _leg_gate_locator(cell):
    """R4: a locator is a place inside the document — not a dash, not the URL."""
    if cell is None:
        return False
    text = cell.strip()
    if text.lower() in DASHES:
        return False
    for url in urls_in(text):
        text = text.replace(url, "")
    return any(ch.isalnum() for ch in text)


def _leg_gate_quote(cell, anchor_spans):
    """R2+R3: (quote, None) when the cell carries the row's anchor quote within
    the caps, else (None, why).  Declared counts in the cell are never read."""
    spans = quoted_spans(cell)
    folded = nfkc_ws(cell)
    anchors = [(nfkc_ws(a), a) for a in anchor_spans if nfkc_ws(a)]
    seen = []
    for span in spans:
        fs = nfkc_ws(span)
        for fa, _anchor in anchors:
            if fs == fa:
                seen.append(span)
    for fa, anchor in anchors:
        if fa in folded:
            seen.append(anchor)
    if seen:
        for quote in seen:
            if quote_ok(quote):
                return quote, None
        return None, ("quote exceeds 25 whitespace tokens / 80 characters "
                      "(recounted from the span: tokens=%s chars=%s)"
                      % ([len(q.split()) for q in seen], [len(q) for q in seen]))
    if spans:
        return None, ("quoted span differs from the row's anchor quote "
                      "(recounted: tokens=%s chars=%s)"
                      % ([len(s.split()) for s in spans],
                         [len(s) for s in spans]))
    return None, ("no quoted span, and the row's anchor quote does not occur in "
                  "the quote cell (a declared word count is not a quote)")


def leg_gate(ctx):
    """GATE: the lesson's ## Gate carries, per adopted row, the row URL, the
    access date, the row's anchor quote within 25 whitespace tokens and 80
    characters, and a locator; >=1 admit and >=1 reject row; every reject row
    carries its probed URL, a reason and a flip."""
    mat, cfg = ctx["mat"], ctx["cfg"]
    try:
        text = read_tree(mat, LESSON)
        lands_rows = parse_rows(read_tree(mat, REGISTRY))
    except Missing as e:
        return leg("GATE", False, "%s" % e)
    section = gate_section(text)
    if not "".join(section).strip():
        return leg("GATE", False, "no ## Gate section in %s" % LESSON)
    tables = _leg_gate_tables(_leg_gate_rows(section))
    bad = []
    admits, rejects = [], []          # (header cells, row)
    for t in tables:
        hdr = row_cells(t["header"])
        for row in t["rows"]:
            admit, reject = is_admit_row(row), is_reject_row(row)
            if admit and reject:
                bad.append("Gate row verdict is both admitted and rejected: %s"
                           % row.strip()[:60])
            elif admit:
                admits.append((hdr, row))
            elif reject:
                rejects.append((hdr, row))

    ahdr = _leg_gate_header(tables, ("quote",))
    if ahdr is None:
        bad.append("admit table header lacks a quote column")
    else:
        if col_index(ahdr, ("date",)) is None:
            bad.append("admit table header lacks an access-date column")
        if col_index(ahdr, ("locator", "grounds", "anchor", "location")) is None:
            bad.append("admit table header lacks a locator column")
    rhdr = _leg_gate_header(tables, ("reason", "flip"))
    if rhdr is None:
        bad.append("reject table header lacks reason+flip columns")

    admit_rows = [r for _h, r in admits]
    for sid in cfg["rows"] + cfg["reused"]:
        row = _gate_admit_row(admit_rows, sid, lands_rows)
        if row is None:
            bad.append("%s has no admit row in Gate" % sid)
            continue
        hdr = ahdr
        for h, r in admits:
            if r == row:
                hdr = h
                break
        cells = row_cells(row)
        quote_i = col_index(hdr, ("quote",)) if hdr is not None else None
        date_i = col_index(hdr, ("date",)) if hdr is not None else None
        loc_i = (col_index(hdr, ("locator", "grounds", "anchor", "location"))
                 if hdr is not None else None)
        if not any(_row_has_url(lands_rows, sid, u) for u in urls_in(row)):
            bad.append("%s admit row does not carry the row URL" % sid)
        if date_i is not None:
            got = cells[date_i] if date_i < len(cells) else None
            if got != cfg["access_date"]:
                bad.append("%s admit row access date %r (want %s)"
                           % (sid, got, cfg["access_date"]))
        if loc_i is not None:
            if loc_i >= len(cells) or not _leg_gate_locator(cells[loc_i]):
                bad.append("%s admit row carries no locator cell" % sid)
        if quote_i is not None:
            if quote_i >= len(cells):
                bad.append("%s admit row has no quote cell" % sid)
            else:
                anchors, why = _leg_gate_anchor_quotes(lands_rows, sid)
                if why:
                    bad.append("%s admit row quote cannot be bound: %s"
                               % (sid, why))
                else:
                    _quote, why = _leg_gate_quote(cells[quote_i], anchors)
                    if why:
                        bad.append("%s admit row %s" % (sid, why))

    if not admits:
        bad.append("no admit row (want >=1)")
    if not rejects:
        bad.append("no reject row (want >=1)")
    for hdr, row in rejects:
        cells = row_cells(row)
        reason_i = col_index(hdr, ("reason",))
        flip_i = col_index(hdr, ("flip",))
        probed_i = col_index(hdr, ("probed", "url", "source"))
        if reason_i is None or flip_i is None:
            bad.append("reject row sits in a table without reason+flip "
                       "columns: %s" % row.strip()[:60])
            continue
        if reason_i >= len(cells) or cells[reason_i].strip().lower() in DASHES:
            bad.append("reject row carries no reason cell: %s"
                       % row.strip()[:60])
        if flip_i >= len(cells) or cells[flip_i].strip().lower() in DASHES:
            bad.append("reject row carries no flip cell: %s" % row.strip()[:60])
        if probed_i is None:
            bad.append("reject table has no probed-URL column: %s"
                       % row.strip()[:60])
        elif probed_i >= len(cells) or not urls_in(cells[probed_i]):
            bad.append("reject row carries no probed URL: %s"
                       % row.strip()[:60])
    return leg("GATE", not bad, "; ".join(dedupe(bad)))
