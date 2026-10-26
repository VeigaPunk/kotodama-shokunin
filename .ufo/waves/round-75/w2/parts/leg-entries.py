# part: leg-entries.py — ENTRIES leg (owner ExecLegEntries)
#
# Frozen leg text (reports/round-75/claims.json, claim C, legs[0]):
#   "ENTRIES: the frozen entries exist at <lands>, absent at base, provenance
#    header (source/verified-at/recheck/ground/topic/gap-filled/sources/
#    couples/scope) first, no header field value in {TODO, TBD, FIXME, XXX,
#    n/a, ?, —}, none matching <[^>]+>, at least one `## ` section, and a body
#    of at least 478 words (the smallest corpus/knowledge entry at base);
#    ENTRIES is a length-and-shape gate only"
#
# Readings of the ambiguous wording (each also stated in the seat report):
#  R1 "provenance header ... first": the nine fields are read only from the
#     header block, i.e. the lines before the first `## ` section (PART A
#     header_block/header_field_names). A provenance header written below the
#     body is therefore invisible and the leg fails; field ORDER inside the
#     block is not graded, because the frozen text enumerates the fields and
#     does not order them.
#  R2 "no header field value in {TODO, TBD, FIXME, XXX, n/a, ?, —}": a value
#     is a placeholder when, after casefolding and stripping the surrounding
#     dash/space, it equals a PART A PLACEHOLDERS member — or when its leading
#     whitespace token does, so "TBD — pending" is a placeholder value with an
#     excuse rather than a value. The empty value is a placeholder (PLACEHOLDERS
#     carries "").
#  R3 "none matching <[^>]+>": graded on header FIELD VALUES only — the frozen
#     clause binds the angle-marker test to the header fields, not to the H1
#     title or the body.
#  R4 "a body of at least 478 words": the body is every line from the first
#     `## ` section to EOF with heading lines removed, so heading text cannot
#     be spent as filler; the gate is the frozen constant 478 and the shared
#     _min_entry_words(mat_base) is used only to CONFIRM that constant's
#     parenthetical provenance (a mismatch is reported in the detail, never
#     graded), because the frozen text says this leg is a length-and-shape gate.
#  R5 "absent at base": the path does not exist as a file in the base tree
#     materialized from the frozen claim base.
# Deliberately NOT graded (the frozen text is shape-only, and w1
# CritCCounterVacuity's source-linked minimum was proposed, not frozen): prose
# quality, filler repetition inside an already >=478-word body, and whether a
# cited id resolves — REPOINTED/ROWS own the id resolution.
#
# Private helpers are prefixed _entries_ (the contract's `_<legfile>_` stem,
# with the file's dash written as an underscore). Shared helpers
# (_min_entry_words and the PART A functions) are CALLED, never redefined.

_ENTRIES_WORD_FLOOR = 478
_ENTRIES_HEADING_RE = re.compile(r"^#{1,6}\s")
_ENTRIES_FIELD_RE = re.compile(r"^[-*\s]*([A-Za-z][A-Za-z0-9 -]*):\s*(.*)$")


def _entries_placeholder(value):
    """R2: PLACEHOLDERS membership of the value or of its leading token."""
    v = value.strip()
    for cand in (v, v.strip("—-–").strip()):
        c = cand.casefold()
        if c in PLACEHOLDERS:
            return True
        toks = c.split()
        if toks and toks[0].rstrip(",;:.") in PLACEHOLDERS:
            return True
    return False


def _entries_body_words(lines):
    """R4: words after the first `## ` section with heading lines removed."""
    body = "\n".join(line for line in lines
                     if not _ENTRIES_HEADING_RE.match(line))
    return len(body.split())


def _entries_floor(mat_base):
    """(gate, derived): the frozen 478 is the gate; the shared helper confirms."""
    if not mat_base:
        return _ENTRIES_WORD_FLOOR, None
    try:
        derived = _min_entry_words(mat_base)
    except Exception:
        return _ENTRIES_WORD_FLOOR, None
    return _ENTRIES_WORD_FLOOR, (derived or None)


def leg_entries(ctx):
    """ENTRIES (length-and-shape gate): the frozen entries exist at <lands> and
    are absent at base; each carries the nine-field provenance header before
    its first section, no placeholder and no <...> field value, at least one
    `## ` section, and a body of at least 478 words (headings excluded)."""
    mat, mat_base, cfg = ctx["mat"], ctx.get("mat_base"), ctx["cfg"]
    bad, notes = [], []
    entries = list(cfg.get("entries") or [])
    if not entries:
        bad.append("frozen entry list is empty")
    floor, derived = _entries_floor(mat_base)
    if derived is not None and derived != floor:
        notes.append("frozen floor %d words; base derives %d" % (floor, derived))
    if not mat_base or not os.path.isdir(mat_base):
        notes.append("base tree unreadable: absent-at-base unconfirmed")
    wanted = set(norm_label(f) for f in HEADER_FIELDS)
    for e in entries:
        try:
            text = read_tree(mat, e)
        except Missing:
            bad.append("%s missing at lands" % e)
            continue
        except UnicodeDecodeError:
            # R6: an entry that is not UTF-8 text cannot carry the header or a
            # countable body; it is a shape failure, not a counter crash.
            bad.append("%s is not UTF-8 text" % e)
            continue
        if mat_base and os.path.isfile(os.path.join(mat_base, e)):
            bad.append("%s present at base (not uncovered ground)" % e)
        if not text.strip():
            bad.append("%s empty (no body)" % e)
            continue
        labels = header_field_names(text)
        missing = [f for f in HEADER_FIELDS if norm_label(f) not in labels]
        if missing:
            bad.append("%s provenance header before the first `## ` missing: %s"
                       % (e, ",".join(missing)))
        for line in header_block(text):
            m = _ENTRIES_FIELD_RE.match(line)
            if not m or norm_label(m.group(1)) not in wanted:
                continue
            value = m.group(2)
            if _entries_placeholder(value):
                bad.append("%s header field %r carries a placeholder value %r"
                           % (e, m.group(1), value.strip()[:40]))
            if ANGLE_RE.search(value):
                bad.append("%s header field %r carries a <...> template token"
                           % (e, m.group(1)))
        lines = text.splitlines()
        body_start = None
        for i, line in enumerate(lines):
            if H2_RE.match(line):
                body_start = i
                break
        if body_start is None:
            bad.append("%s has no `## ` section (header-only stub)" % e)
            continue
        words = _entries_body_words(lines[body_start:])
        if words < floor:
            bad.append("%s body has %d words (floor %d = the smallest "
                       "knowledge entry at base)" % (e, words, floor))
    # PART A prints one line per leg (`"     %s" % detail`) and the contract caps
    # that line at 300 characters; a three-entry landing can stack failures, so
    # the composed detail is cut at 295 (5 indent + 295 = 300), never reflowed.
    detail = "; ".join(dedupe(bad) + notes)
    if len(detail) > 295:
        detail = detail[:292] + "..."
    return leg("ENTRIES", not bad, detail)
