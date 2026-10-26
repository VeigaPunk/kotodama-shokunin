def _rows_quote_core(value):
    """The stored `quote:` value with one wrapping quotation pair removed.

    The evidence producer may write the located span bare (`quote: Innombrables
    sont les récits du monde.`) or wrapped in the document's own marks
    (`quote: «Innombrables sont les récits du monde.»`).  The anchor cell wraps
    the span in its own `«…»`/`「…」`, so grading only the wrapped form would
    fail a landing whose only difference is the wrapper.  Both forms are tried;
    what has to be inside the anchor cell is the *text* of the quote.
    """
    v = value.strip()
    m = QUOTE_RE.fullmatch(v)
    if m:
        return m.group(0)[1:-1].strip()
    return v.strip('"\'“”‘’')


def _rows_cadence_ok(cell):
    """True for a cadence-ONLY recheck cell.

    PART A's RECHECK_RE documents the rule ("a cadence-only recheck cell:
    `180d`, `90d`, `on-release`, `quarterly` — never an ISO date, never a
    composite cell with prose in it"), but its body is a lowercase-phrase
    pattern that also accepts a campaign recheck sentence such as
    `re-open on 2026-10-23 and re-count the span in the served transcription`.
    The leg wording is "a cadence-only recheck cell", so the documented intent
    is enforced here too: a `NNd` cadence, or at most three lower-case/hyphen
    words carrying no digits (the lane's own vocabulary is `365d 180d 90d
    on-release`).
    """
    cell = cell.strip()
    # `re.fullmatch` on a string pattern is cached by the stdlib, so this
    # compiles once without a module-level constant.
    return bool(RECHECK_RE.match(cell)) and re.fullmatch(
        r"\d+d|[a-z][a-z-]{0,23}(?: [a-z][a-z-]{0,23}){0,2}", cell) is not None


def leg_rows(ctx):
    """ROWS: the registry diff base..<lands> adds exactly the frozen row_set.

    Frozen wording (reports/round-75/claims.json, claim C, legs[1]): "the
    registry diff base..<lands> adds exactly the frozen row_set (contiguous
    ids), none removed; each row status mined, opened 2026-10-27, a cadence-only
    recheck cell, 11 cells, no pipe in any cell, the evidence quote inside the
    anchor cell, used-by exactly the admitted entries whose source: lines cite
    it; every pre-existing row is byte-identical".

    Readings taken here (each also stated in the seat report):

    R1 "adds exactly the frozen row_set" / "none removed" is graded on the
       line multiset of both revisions, so a duplicated line cannot hide behind
       its twin.  A blank line adds no row and hides no row and is tolerated on
       either side; every other non-row line added, and every non-blank line
       removed, fails.
    R2 "contiguous ids" is a run check on the ids actually added (a gap such as
       S885..S890 + S892..S893 fails whatever the frozen set says).
    R3 "no pipe in any cell": `row_cells` splits on every `|`, so an escaped
       `\\|` from a staged cell splits one cell into two; the row is failed for
       the escaped pipe first (the as-is tell) and for the cell count second.
    R4 "the evidence quote inside the anchor cell" is the evidence file's own
       `quote:` field against the anchor cell after NFKC + whitespace folding
       (H2/R74 discipline); the self-attested `quote-found:` flags are never
       read.  A row with no committed evidence file has no quote to sit inside
       its anchor cell and fails here (the EVIDENCE leg fails it too).
    R5 "used-by exactly the admitted entries whose source: lines cite it" is
       graded BOTH ways per row: the cell names no entry that does not cite the
       row, names every entry that does, AND the citing set is non-empty.  An
       orphan row whose `used-by` is a dash because no configured entry cites it
       is not "exactly the citing entries" in the claim's sense: the after-state
       adopts each row through an entry, and an empty `used-by` cell is a
       staged row appended as-is (the kill rule's own limb).  The citing set is
       derived from `_entry_citations`, i.e. only `source:` header lines bind.
    R6 the frozen claim declares `reused_rows: []`, and the wording grants no
       in-place exception ("every pre-existing row is byte-identical"), so any
       changed pre-existing row fails.
    """
    mat, mat_base, cfg = ctx["mat"], ctx["mat_base"], ctx["cfg"]
    try:
        base_text = read_tree(mat_base, REGISTRY)
        lands_text = read_tree(mat, REGISTRY)
    except Missing as e:
        return leg("ROWS", False, "registry unreadable: %s" % e)
    base_rows = parse_rows(base_text)
    lands_rows = parse_rows(lands_text)
    want = list(cfg["rows"])
    bad = []

    # R1/R6: the line multiset diff.  Order-insensitive; a blank line is
    # tolerated, any other added line and every removed non-blank line fails.
    base_lines = [l.rstrip() for l in base_text.splitlines()]
    lands_lines = [l.rstrip() for l in lands_text.splitlines()]
    added_lines = list((Counter(lands_lines) - Counter(base_lines)).elements())
    removed_lines = list((Counter(base_lines) - Counter(lands_lines)).elements())
    inserted = []
    for line in removed_lines:
        if not line.strip():
            continue
        m = ROW_RE.match(line)
        bad.append("pre-existing %s line removed (every pre-existing row must "
                   "stay byte-identical): %r"
                   % (m.group(1) if m else "non-row", line[:60]))
    for line in added_lines:
        if not line.strip():
            continue
        m = ROW_RE.match(line)
        if not m:
            bad.append("registry line added outside the frozen row_set: %r"
                       % line[:60])
            continue
        inserted.append(m.group(1))
    if sorted(inserted) != sorted(want):
        bad.append("row lines added %s (want the frozen row_set %s)"
                   % (sorted(inserted), want))
    dup = sorted(i for i in set(inserted) if inserted.count(i) > 1)
    if dup:
        bad.append("a row line is added twice: %s" % dup)

    # the parsed-row view, for the failure a line-level diff alone words badly
    added = set(lands_rows) - set(base_rows)
    removed = set(base_rows) - set(lands_rows)
    if added != set(want):
        bad.append("rows present at lands but not at base: %s (want %s)"
                   % (sorted(added), want))
    if removed:
        bad.append("rows present at base but not at lands: %s" % sorted(removed))

    # R2: contiguous ids
    nums = sorted(int(x[1:]) for x in added)
    if nums and nums != list(range(nums[0], nums[0] + len(nums))):
        bad.append("added ids are not contiguous: %s" % nums)

    # R5: the citing entries, from the admitted entries' `source:` header lines
    cited = _entry_citations(mat, cfg["entries"], bad)

    missing = []
    for sid in want:
        row = lands_rows.get(sid)
        if row is None:
            missing.append(sid)
            continue
        if "\\|" in row:
            bad.append("%s row carries an escaped pipe (a staged cell appended "
                       "as-is): %r" % (sid, row[:60]))
            continue
        cells = row_cells(row)
        if len(cells) != NCELLS:
            bad.append("%s row has %d cells (want %d: no pipe inside any cell)"
                       % (sid, len(cells), NCELLS))
            continue
        if cells[STATUS] != "mined":
            bad.append("%s status=%r (want mined)" % (sid, cells[STATUS]))
        if cells[OPENED] != cfg["access_date"]:
            bad.append("%s opened=%r (want %s)"
                       % (sid, cells[OPENED], cfg["access_date"]))
        if not _rows_cadence_ok(cells[RECHECK]):
            bad.append("%s recheck=%r is not a cadence-only cell"
                       % (sid, cells[RECHECK]))
        want_used = set(cited.get(sid) or ())
        got_used = row_usedby(cells)
        if not want_used:
            bad.append("%s is cited by no admitted entry (orphan row; used-by=%r)"
                       % (sid, cells[USEDBY]))
        elif got_used != want_used:
            bad.append("%s used-by=%s (want exactly the admitting entries %s)"
                       % (sid, sorted(got_used), sorted(want_used)))

        # R4: the evidence quote lives inside the anchor cell
        ev = _evidence(mat, sid)
        if ev is None:
            bad.append("%s has no committed evidence file (%s/%s.txt)"
                       % (sid, EVIDENCE_DIR, sid))
            continue
        quote = (ev.get("quote") or "").strip()
        if not quote:
            bad.append("%s evidence file carries no quote: line" % sid)
            continue
        anchor = nfkc_ws(cells[ANCHOR])
        forms = dedupe([nfkc_ws(quote), nfkc_ws(_rows_quote_core(quote))])
        if not any(f and f in anchor for f in forms):
            bad.append("%s anchor cell does not contain its evidence quote (%r)"
                       % (sid, quote[:60]))
    if missing:
        bad.append("rows missing at lands: %s" % missing)
    return leg("ROWS", not bad, "; ".join(dedupe(bad)))
