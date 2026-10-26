# ------------------------------------------------------------- leg: INDEX ---
# Claim C, leg 13 (INDEX), frozen text (reports/round-75/claims.json, claim C,
# legs[-1]; the SHONEN.md:6 clause was removed from this leg by the L1 before
# data, SHONEN.md being claim Ca's, so this leg never reads SHONEN.md):
#
#   corpus/README.md at <lands> has exactly one index row per adopted entry in
#   the myth-symbol section, each entry's own `- topic:` text verbatim under the
#   `- `name.md` — ` prefix, the myth-symbol heading equals the live partition
#   count (32), the last 'Counts checked' footer's total equals the live file
#   count with the per-directory vector 32/32/40/29/24/95; every base footer
#   block is preserved byte-identical and in order (the new footer is a new
#   appended block); README lines changed, removed or added outside {the three
#   adopted index rows, the myth-symbol heading, the appended footer block
#   (`Total knowledge entries: N.` and its `Counts checked` paragraph),
#   partition-heading lines whose only change is the count parenthetical
#   (claim Ca's), index rows naming a knowledge file that exists at base (claim
#   Ca's index-gap rows)} fail, and an added row-shaped `| S-id |` line fails.
#
# The SHONEN.md:6 clause was removed from this leg by the L1 before data
# (SHONEN.md is claim Ca's), so this leg never reads SHONEN.md.  Claim Ca lands
# BEFORE claim C, so the graded tree carries Ca's two partition-heading count
# repairs and its four index-gap rows; both are exempt, nothing else is.
#
# Readings where the wording is ambiguous (each stated in the w2 report):
#   R1 "live partition count" / "live file count" are counted from the graded
#      tree (mat), never from the README and never from the lane worktree.
#   R2 "exactly one index row per adopted entry in the myth-symbol section" is
#      read as the round-74 counter read the identical culture-material wording:
#      exactly one row for the basename anywhere in README, and that row inside
#      the myth-symbol section (r74 MutIndexLeg M8 killed a trailing-block
#      duplicate that way).
#   R3 "verbatim" compares the row body byte-for-byte against the entry's
#      `- topic:` value; the README-side body is not stripped, so a trailing
#      space on a row fails (r74 MutIndexLeg F2/M10 was the strip()-lenient
#      survivor).
#   R4 "older footers are byte-identical" = every base `Counts checked` block:
#      the base footer-block sequence must be a prefix of the lands one, which
#      also closes r74 MutIndexLeg F1 (the immediately-preceding live footer was
#      exempt under the old `[:-1]` loop).
#   R5 "the appended footer block" = the last `Counts checked` line of the
#      lands file, the paragraph that starts there (through its last non-blank
#      line), and the `Total knowledge entries: N.` line with the blank lines
#      that separate it from the previous paragraph.  A line appended outside
#      that block, an appended section heading or an extra prose paragraph,
#      fails.  (The base file's own footers are multi-line paragraphs that end
#      with prose, so the block's prose lines are part of it.)
#   R6 the per-directory vector is the six `## <part>/ (N)` partitions in README
#      section order; the last footer's vector must equal the frozen
#      (32, 32, 40, 29, 24, 95) AND the live per-partition .md counts, so the
#      footer states a true directory reading for the landed tree.
#   R7 the base README must embed, line by line and in order, into the lands
#      README: every base line survives verbatim (only partition-count heading
#      parentheticals may be replaced) and every lands line is either matched or
#      in the exemption set.  No diff algorithm is used, so repeated lines (the
#      footers repeat their closing lines; the file is full of blank lines)
#      cannot be matched against the wrong occurrence.


def _readme_sections(text):
    """[(partition, start, end)] char spans of the `## <part>/ (N)` sections."""
    marks = [(m.start(), m.group(1)) for m in README_SECTION_RE.finditer(text)]
    out = []
    for i, (pos, part) in enumerate(marks):
        end = marks[i + 1][0] if i + 1 < len(marks) else len(text)
        out.append((part, pos, end))
    return out


def _footer_blocks(text):
    """Paragraph blocks whose first line is a `Counts checked` footer."""
    blocks = []
    for block in re.split(r"\n[ \t]*\n", text):
        stripped = block.strip("\n")
        if stripped.startswith("Counts checked "):
            blocks.append(stripped)
    return blocks


def _entry_topic(mat, path):
    """The entry's own `- topic:` header value (first one, in the pre-body header)."""
    try:
        text = read_tree(mat, path)
    except Missing:
        return None
    for line in header_block(text):
        m = re.match(r"^[-*\s]*topic:\s*(.*)$", line)
        if m:
            value = m.group(1).strip()
            return value or None
    return None


def _md_count(mat, prefix):
    return len([p for p in tree_files(mat, prefix) if p.endswith(".md")])


def leg_index(ctx):
    """INDEX: one verbatim myth-symbol row per adopted entry, the heading equal
    to the live partition count, the last footer true to the landed tree with
    the frozen six-partition vector, every older footer byte-identical, and no
    README change outside the frozen exemption set."""
    mat, mat_base, cfg = ctx["mat"], ctx["mat_base"], ctx["cfg"]
    wanted_vec = (32, 32, 40, 29, 24, 95)      # frozen in the claim's leg text
    bad = []
    try:
        lands_text = read_tree(mat, README)
    except Missing:
        return leg("INDEX", False, "%s missing at lands" % README)
    try:
        base_text = read_tree(mat_base, README)
    except Missing:
        base_text = ""

    entries = list(cfg.get("entries") or [])
    names = [os.path.basename(e) for e in entries]
    lines = lands_text.splitlines()
    sections = _readme_sections(lands_text)
    parts = [p for p, _s, _e in sections]
    heading_counts = {}
    for h in README_SECTION_RE.finditer(lands_text):
        heading_counts[h.group(1)] = int(h.group(2))

    myth = [s for s in sections if s[0] == "myth-symbol"]
    if not myth:
        bad.append("%s has no `## myth-symbol/ (N)` section" % README)
        first = last = -1
    else:
        _p, myth_start, myth_end = myth[0]
        first = lands_text.count("\n", 0, myth_start)
        last = lands_text.count("\n", 0, myth_end)

    # R2/R3: one row per adopted entry, inside the myth-symbol section, body
    # equal to the entry's own `- topic:` value.
    for path, name in zip(entries, names):
        topic = _entry_topic(mat, path)
        if topic is None:
            bad.append("%s has no non-empty `- topic:` header line" % path)
        hits = []
        for k, line in enumerate(lines):
            m = README_ROW_RE.match(line)
            if m and m.group(1) == name:
                hits.append((k, m.group(2)))
        if len(hits) != 1:
            bad.append("%s has %d index rows in %s (want exactly one)"
                       % (name, len(hits), README))
            continue
        k, body = hits[0]
        if not 0 <= first <= k < last:
            bad.append("%s index row is not inside the myth-symbol section"
                       % name)
        if topic is not None and body != topic:
            bad.append("%s index row is not the entry's `- topic:` text verbatim"
                       % name)

    # R1: the myth-symbol heading equals the live count of that partition.
    live_parts = [_md_count(mat, KNOWLEDGE + "/" + part) for part in parts]
    if "myth-symbol" in heading_counts:
        live_myth = _md_count(mat, KNOWLEDGE + "/myth-symbol")
        if heading_counts["myth-symbol"] != live_myth:
            bad.append("myth-symbol heading (%d) != the %d live .md files in "
                       "corpus/knowledge/myth-symbol"
                       % (heading_counts["myth-symbol"], live_myth))

    # R1/R6: the last footer's total and six-partition vector.
    lands_blocks = _footer_blocks(lands_text)
    base_blocks = _footer_blocks(base_text)
    shown_total = shown_vec = "-"
    if not lands_blocks:
        bad.append("%s carries no `Counts checked` footer" % README)
    else:
        m = README_FOOTER_RE.search(lands_blocks[-1])
        if not m:
            bad.append("the last `Counts checked` footer carries no "
                       "(total N files; directory totals V) reading")
        else:
            total = int(m.group(1))
            vector = tuple(int(x) for x in m.group(2).split("/") if x)
            shown_total, shown_vec = str(total), m.group(2)
            live_total = _md_count(mat, KNOWLEDGE)
            if total != live_total:
                bad.append("last footer total %d != the %d .md files at lands"
                           % (total, live_total))
            if len(parts) != len(wanted_vec):
                bad.append("%s declares %d partition sections (want %d)"
                           % (README, len(parts), len(wanted_vec)))
            if vector != wanted_vec:
                bad.append("last footer vector %s != the frozen %s"
                           % ("/".join(str(v) for v in vector),
                              "/".join(str(v) for v in wanted_vec)))
            elif live_parts != list(wanted_vec):
                bad.append("the live partition counts %s differ from the frozen "
                           "vector %s"
                           % ("/".join(str(v) for v in live_parts),
                              "/".join(str(v) for v in wanted_vec)))

    # R4: every base footer (older than the new last one) byte-identical, in
    # order: the base block sequence is a prefix of the lands block sequence.
    for pos, blk in enumerate(base_blocks):
        if pos >= len(lands_blocks) or lands_blocks[pos] != blk:
            bad.append("an older `Counts checked` footer is not preserved "
                       "byte-identically: %r" % blk.splitlines()[0][:60])

    # R5 + the exemption set: base is embedded line by line, in order, into
    # lands.  Every base line must survive verbatim unless it is one of the
    # partition-count headings (whose parenthetical a landing may replace), and
    # every lands line must be matched unless it is in the exemption set.  The
    # walk is greedy and ordered, so a rewritten, moved or deleted line fails
    # and an inserted line outside the set fails.
    base_lines = base_text.splitlines()
    adopted = set(names)
    try:
        base_knowledge = set(os.path.basename(p)
                             for p in tree_files(mat_base, KNOWLEDGE))
    except OSError:
        base_knowledge = set()
    base_parts = set(m.group(1) for m in
                     (README_SECTION_RE.match(x) for x in base_lines) if m)
    lands_parts = set(m.group(1) for m in
                      (README_SECTION_RE.match(x) for x in lines) if m)
    exempt = set()
    if lands_blocks:
        cf = None
        for k, line in enumerate(lines):
            if line.startswith("Counts checked "):
                cf = k
        if cf is not None:
            hi = cf
            while hi + 1 < len(lines) and lines[hi + 1].strip():
                hi += 1
            lo = cf
            back = lo - 1
            if back >= 0 and not lines[back].strip():    # blank before Counts
                lo = back
                back -= 1
            if back >= 0 and lines[back].startswith("Total knowledge entries:"):
                lo = back
            if lo > 0 and not lines[lo - 1].strip():     # blank before the block
                lo -= 1
            exempt.update(range(lo, hi + 1))
    base_occ = Counter(base_lines)
    lands_occ = Counter(lines)
    for k, line in enumerate(lines):
        if lands_occ[line] <= base_occ.get(line, 0):
            continue                     # a line the base already carries
        if ROW_SHAPED_LINE_RE.match(line):
            bad.append("README line %d is a row-shaped registry line (this file "
                       "never asserts registry rows): %r" % (k + 1, line[:90]))
            continue
        rm = README_ROW_RE.match(line)
        if rm and rm.group(1) not in adopted and rm.group(1) not in base_knowledge:
            bad.append("README line %d adds an index row for %r, which is "
                       "neither a frozen adopted entry nor a knowledge file "
                       "existing at base" % (k + 1, rm.group(1)))
    for k, line in enumerate(lines):
        if lands_occ[line] <= base_occ.get(line, 0):
            continue                     # a line the base already carries
        m = README_SECTION_RE.match(line)
        if m and m.group(1) in base_parts:
            exempt.add(k)
            continue
        rm = README_ROW_RE.match(line)
        if rm and (rm.group(1) in adopted or rm.group(1) in base_knowledge):
            exempt.add(k)
    i = j = 0
    while i < len(base_lines) and j < len(lines):
        if base_lines[i] == lines[j]:
            i += 1
            j += 1
        elif j in exempt:
            j += 1
        else:
            m = README_SECTION_RE.match(base_lines[i])
            if m and m.group(1) in lands_parts:
                i += 1                   # count parenthetical replaced at lands
            else:
                bad.append("README line %d removed/edited outside the exemption "
                           "set: %r" % (i + 1, base_lines[i][:90]))
                i += 1
    while i < len(base_lines):
        m = README_SECTION_RE.match(base_lines[i])
        if not (m and m.group(1) in lands_parts):
            bad.append("README line %d removed/edited outside the exemption "
                       "set: %r" % (i + 1, base_lines[i][:90]))
        i += 1
    while j < len(lines):
        if j not in exempt:
            line = lines[j]
            rm = README_ROW_RE.match(line)
            if ROW_SHAPED_LINE_RE.match(line):
                bad.append("README line %d is a row-shaped registry line (this "
                           "file never asserts registry rows): %r"
                           % (j + 1, line[:90]))
            elif rm:
                bad.append("README line %d adds an index row for %r, which is "
                           "neither a frozen adopted entry nor a knowledge file "
                           "existing at base" % (j + 1, rm.group(1)))
            else:
                bad.append("README line %d added outside the exemption set: %r"
                           % (j + 1, line[:90]))
        j += 1

    detail = ("%s: %d section(s), myth-symbol=%s, last footer total=%s vector=%s, "
              "%d adopted row(s), %d base / %d lands line(s), %d exempt line(s)"
              % (README, len(parts), heading_counts.get("myth-symbol"),
                 shown_total, shown_vec, len(names), len(base_lines), len(lines),
                 len(exempt)))
    if bad:
        reasons = dedupe(bad)
        if len(reasons) > 4:
            reasons = reasons[:4] + ["(+%d more)" % (len(reasons) - 4)]
        detail = "; ".join(reasons) + " | " + detail
    return leg("INDEX", not bad, detail[:300])
