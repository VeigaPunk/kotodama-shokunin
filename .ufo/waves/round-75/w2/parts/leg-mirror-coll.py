"""SCRATCHMIRROR and COLLCHECK — the two provenance legs of claim C.

Wording graded (reports/round-75/claims.json, claim C legs[], frozen text):

  SCRATCHMIRROR: `.ufo/waves/round-75/assimilation/validate-receipt.txt` shows
  `validate --file` exit 0 on a mirrored corpus carrying the frozen rows and
  entries, committed strictly before the registry-append commit.

  COLLCHECK: reg-ids/staged-ids/collisions files and guard-proof show a planted
  1-3-space-indented collision found and a 4-space one not found; no adopted lane
  id is in reg-ids; the map maps staged->lane by document for every adopted id.

Readings (ambiguities resolved here; see .ufo/waves/round-75/w2/
ExecLegMirrorColl.md for the full list and the positive/mutant table):

  R1  "committed strictly before the registry-append commit" is graded on the
      first-parent chain between the frozen claim base and <lands>: the append
      commit is the first chain commit whose REGISTRY blob holds the first
      frozen row id; the receipt commit is the chain commit that adds (or
      touches) the receipt.  A receipt added in the append commit, or touched
      after it, is not "before".  No per-path rev-list: a merge could carry a
      receipt commit that is not on the chain the L1 lands on.
  R2  "carrying the frozen rows and entries" is graded from the receipt's named
      ids/basenames — the receipt is a rehearsal record; the counter does not
      re-run census inside a leg (the CENSUS leg owns execution, and a leg that
      re-ran the mirror would grade an input, not the committed artefact).
  R3  The receipt must name EVERY frozen entry basename, the three-entry
      round-75 set included: a receipt regenerated from a two-entry mirror does
      not carry the frozen entries.
  R4  reg-ids is the PRE-APPEND registry id set (the claim's base registry):
      the leg re-derives it from the claim base with the 0-3-space row pattern
      and requires the landed file to equal that set.  "No adopted lane id is in
      reg-ids" is vacuous if reg-ids is any list at all, so the file's
      provenance is graded, not assumed.
  R5  collisions is re-derived as comm -12 of the two lists (set intersection):
      the file's only meaning is that intersection, and a stale or hand-edited
      collision list cannot support the guard claim.
  R6  A planted 1-3-space "collision" needs the planted id to be a STAGED id
      the registry does not hold (that is what makes it a collision) and the
      plant to be a real row in the committed proof bytes — so a proof that
      only asserts "found" in prose, or that plants an id outside the staged
      universe, does not pass.  Same for the 4-space control, both ways.
  R7  "maps staged->lane by document for every adopted id": for each adopted
      lane id the map must carry at least one staged record, must carry every
      staged id the frozen row_set names for that row, and every such record's
      url must name a document the landed row's source cell names (document
      identity via urls_compatible, which folds the persee page-level view onto
      its document and the %20 form onto the raw-space form).
"""


def _mirrorcoll_ids(value):
    """One row_set `staged` cell as a list of staged ids.

    Round 75 freezes a LIST per lane id (four staged rows collapse onto S885:
    "S876/S885/S917/S921"); a single-id row stays a bare string.
    """
    if isinstance(value, (list, tuple)):
        items = list(value)
    elif isinstance(value, str):
        items = re.split(r"[/,;\s]+", value)
    else:
        items = []
    out = []
    for item in items:
        v = str(item).strip().upper()
        if v and TOKEN_RE.fullmatch(v) and v not in out:
            out.append(v)
    return out


def _mirrorcoll_brief(ids, limit=6):
    """A bounded id list for a leg detail line (<= 300 chars, contract)."""
    ids = sorted(ids)
    head = ", ".join(ids[:limit])
    if len(ids) > limit:
        head += " (+%d more)" % (len(ids) - limit)
    return head or "-"


def _mirrorcoll_detail(bad, info):
    """The leg detail line: every reason that fits in 300 characters.

    The contract fixes the first detail line at <= 300 characters; a landing
    that breaks several clauses at once is summarised as the first three plus a
    count, never truncated mid-reason.
    """
    msgs = dedupe(bad)
    text = "; ".join(msgs[:3])
    if len(msgs) > 3:
        text += "; (+%d more)" % (len(msgs) - 3)
    room = 296 - len(info)
    if len(text) > room:
        text = text[:max(room - 4, 0)].rstrip() + "..."
    return ("%s; %s" % (text, info)) if text else info


def _mirrorcoll_text(root, rev, path):
    """`path` at `rev` as text, or None when the path is absent there."""
    r = git(root, "show", "%s:%s" % (rev, path))
    return r.stdout if r.returncode == 0 else None


def leg_scratch_mirror(ctx):
    """SCRATCHMIRROR: the `validate --file` receipt is committed on <lands>'
    first-parent chain strictly before the registry-append commit, shows exit 0,
    and carries the frozen adopted ids and entry basenames."""
    root, mat, cfg, lands = ctx["root"], ctx["mat"], ctx["cfg"], ctx["lands"]
    try:
        receipt = read_tree(mat, RECEIPT)
    except Missing:
        return leg("SCRATCHMIRROR", False, "receipt missing: %s" % RECEIPT)
    bad = []
    if re.search(r"(?s)validate.{0,200}--file|--file.{0,200}validate", receipt) is None:
        bad.append("receipt does not show `validate --file`")
    if re.search(r"(?i)\b(?:exit|rc)\s*[=:]?\s*0\b", receipt) is None:
        bad.append("receipt does not show exit 0")
    missing = [sid for sid in cfg["rows"]
               if not re.search(r"\b%s\b" % re.escape(sid), receipt)]
    if missing:
        bad.append("receipt does not carry %s" % _mirrorcoll_brief(missing))
    for e in cfg["entries"]:
        if os.path.basename(e) not in receipt:
            bad.append("receipt does not carry the entry %s" % os.path.basename(e))

    chain = git(root, "rev-list", "--first-parent", "--reverse",
                "%s..%s" % (cfg["base"], lands)).stdout.split()
    first = cfg["rows"][0] if cfg["rows"] else None
    receipt_revs, append_rev = [], None
    # seed from the claim base: only commits INSIDE base..<lands> can add the
    # receipt or the first row, so a pre-existing file is not misread as this
    # round's commit
    prev = _mirrorcoll_text(root, cfg["base"], RECEIPT)
    had_row = bool(first) and first in parse_rows(
        _mirrorcoll_text(root, cfg["base"], REGISTRY) or "")
    for i, rev in enumerate(chain):
        text = _mirrorcoll_text(root, rev, RECEIPT)
        if text is not None and text != prev:
            receipt_revs.append(i)
        prev = text
        if append_rev is None and first and not had_row:
            reg = _mirrorcoll_text(root, rev, REGISTRY)
            if reg is not None and first in parse_rows(reg):
                append_rev = i
    if had_row:
        bad.append("the %s row already exists at the claim base" % (first or "-"))
    elif append_rev is None:
        bad.append("no first-parent commit in base..<lands> adds the %s row"
                   % (first or "-"))
    if not receipt_revs:
        bad.append("receipt is not committed on the base..<lands> first-parent chain")
    elif append_rev is not None:
        if append_rev in receipt_revs:
            bad.append("receipt committed in the registry-append commit (not before)")
        elif max(receipt_revs) >= append_rev:
            bad.append("receipt touched after the registry-append commit")
    detail = "receipt@%s append@%s rows=%d entries=%d" % (
        ",".join(str(i) for i in receipt_revs) or "-",
        "-" if append_rev is None else str(append_rev),
        len(cfg["rows"]), len(cfg["entries"]))
    return leg("SCRATCHMIRROR", not bad, _mirrorcoll_detail(bad, detail))


def _guard_files(mat):
    """(rel, text) for every committed file under the guard-proof dir.

    The frozen wording names `guard-proof`; a landing that keeps the proof
    elsewhere under the assimilation tree is still graded, from committed bytes.
    """
    for base in (GUARD_DIR, ASSIM):
        if not os.path.isdir(os.path.join(mat, base)):
            continue
        out = []
        for rel in tree_files(mat, base):
            try:
                out.append((rel, read_tree(mat, rel)))
            except Missing:
                continue
        if out:
            return out
    return []


def _negated(line):
    return re.search(r"(?i)(\b(?:not|no|none|zero|missed|absent|never)\b|n't\b)", line)


def leg_collcheck(ctx):
    """COLLCHECK: the three id lists (re-derived where the wording allows),
    the indent guard proved both ways on committed fixture bytes, and the
    by-document map covering every adopted id."""
    mat, cfg = ctx["mat"], ctx["cfg"]
    bad = []
    variants = (("reg-ids", "staged-ids", "collisions"),
                ("collcheck-reg-ids.txt", "collcheck-staged-ids.txt",
                 "collcheck-collisions.txt"))
    dirs = (ASSIM, ASSIM + "/validate", ASSIM + "/mutations")
    found = None
    for d in dirs:
        for v in variants:
            if all(os.path.isfile(os.path.join(mat, d, f)) for f in v):
                found = (d, v)
                break
        if found:
            break
    if found is None:
        return leg("COLLCHECK", False,
                   "collision id files missing under %s" % ASSIM)
    d, v = found
    try:
        reg_ids = set(TOKEN_RE.findall(read_tree(mat, d + "/" + v[0])))
        staged_ids = set(TOKEN_RE.findall(read_tree(mat, d + "/" + v[1])))
        collide_ids = set(TOKEN_RE.findall(read_tree(mat, d + "/" + v[2])))
    except Missing as e:
        return leg("COLLCHECK", False, "collision id file unreadable: %s" % e)

    if not staged_ids:
        bad.append("staged-ids is empty")
    for sid in cfg["rows"]:
        if sid in reg_ids:
            bad.append("%s present in reg-ids (adopted id is not free)" % sid)
        if sid in collide_ids:
            bad.append("%s listed in collisions" % sid)
        for s in _mirrorcoll_ids(cfg["row_staged"].get(sid)):
            if s not in staged_ids:
                bad.append("staged id %s (-> %s) absent from staged-ids" % (s, sid))

    base_reg = None
    try:
        base_reg = read_tree(ctx["mat_base"], REGISTRY)
    except Missing:
        pass
    if base_reg is None:
        bad.append("claim-base registry unreadable (cannot re-derive reg-ids)")
        base_ids = set()
    else:
        base_ids = set(parse_rows(base_reg))
        if reg_ids != base_ids:
            bad.append("reg-ids is not the claim-base registry id set (file %d, "
                       "base %d; missing %s; extra %s)"
                       % (len(reg_ids), len(base_ids),
                          _mirrorcoll_brief(base_ids - reg_ids),
                          _mirrorcoll_brief(reg_ids - base_ids)))
    derived_coll = reg_ids & staged_ids
    if collide_ids != derived_coll:
        bad.append("collisions is not comm -12 of the id lists (file %d, derived "
                   "%d; missing %s; extra %s)"
                   % (len(collide_ids), len(derived_coll),
                      _mirrorcoll_brief(derived_coll - collide_ids),
                      _mirrorcoll_brief(collide_ids - derived_coll)))

    lands_rows = {}
    try:
        lands_rows = parse_rows(read_tree(mat, REGISTRY))
    except Missing:
        pass
    real_ids = (base_ids | set(lands_rows) | set(cfg["rows"]) | set(cfg["reused"]))
    guard_files = _guard_files(mat)
    positive = re.compile(r"(?i)collision|detect|present|found|fail|survived|killed"
                          r"|exit\s*[=:]?\s*1|sees[^\n]*\b1\b")
    negative = re.compile(r"(?i)(?:^|[^\d])0(?:[^\d]|$)|not\s+(?:found|seen|detected|"
                          r"matched)|no\s+collision|missed")
    indent_ok, four_ok = None, None
    for rel, text in guard_files:
        lines = [l for l in text.splitlines()
                 if not (ROW_RE.match(l) or INDENTED_ROW_RE.match(l)
                         or FOURSPACE_ROW_RE.match(l))]
        planted = [p for p in INDENTED_ROW_RE.findall(text)
                   if p not in real_ids and p in staged_ids]
        if planted and indent_ok is None:
            for pid in planted:
                hit = [l for l in lines
                       if pid in l and not _negated(l) and positive.search(l)]
                if hit:
                    indent_ok = (rel, pid, hit[0].strip()[:90])
                    break
        fours = [p for p in FOURSPACE_ROW_RE.findall(text)
                 if p not in real_ids and p in staged_ids]
        if four_ok is None:
            for pid in fours:
                hit = [l for l in lines
                       if (pid in l or re.search(r"(?i)4[- ]space|four[- ]space", l))
                       and _negated(l) and negative.search(l)]
                if hit:
                    four_ok = (rel, pid, hit[0].strip()[:90])
                    break
        if four_ok is None:
            # a control file may state the 4-space plant was not seen without
            # quoting the row itself
            hit = [l for l in lines
                   if re.search(r"(?i)4[- ]space|four[- ]space", l)
                   and _negated(l) and negative.search(l)]
            if hit:
                four_ok = (rel, None, hit[0].strip()[:90])
    if indent_ok is None:
        bad.append("no indent-guard proof under %s (a staged-id row planted at "
                   "1-3 spaces with a positive detection marker)" % GUARD_DIR)
    else:
        rel, pid, _line = indent_ok
        if re.search(r"^ {4,}\|\s*%s\s*\|" % pid, read_tree(mat, rel), re.M):
            bad.append("guard proof %s plants %s at 4+ spaces, not 1-3"
                       % (rel, pid))
    if four_ok is None:
        bad.append("no four-space control under %s (a staged-id row planted at "
                   "4 spaces with a not-found marker)" % GUARD_DIR)
    elif four_ok[1] is not None:
        rel, pid, _line = four_ok
        if pid in set(INDENTED_ROW_RE.findall(read_tree(mat, rel))):
            bad.append("four-space control %s plants %s inside the 1-3-space "
                       "grammar" % (rel, pid))

    recs = _map_records(ctx)
    if not recs:
        bad.append("no renumber-map records at the freeze (%s:%s)"
                   % (cfg["freeze"][:12], cfg["map_path"]))
    else:
        for sid in cfg["rows"]:
            olds = set(old for (old, new) in recs if new == sid)
            if not olds:
                bad.append("map records no staged->lane for %s" % sid)
                continue
            want = set(_mirrorcoll_ids(cfg["row_staged"].get(sid)))
            missing = want - olds
            if missing:
                bad.append("map does not map %s -> %s (the row_set stages those "
                           "ids on it)" % (_mirrorcoll_brief(missing), sid))
            row = lands_rows.get(sid)
            cells = row_cells(row) if row is not None else []
            row_urls = urls_in(cells[SOURCE]) if len(cells) > SOURCE else []
            for old in sorted(olds):
                url = recs[(old, sid)]
                if not url:
                    bad.append("map record %s -> %s carries no url" % (old, sid))
                elif row is None or not row_urls:
                    continue  # the ROWS leg owns a missing row / source cell
                elif not any(urls_compatible(url, u) for u in row_urls):
                    bad.append("map record %s -> %s names a document the row "
                               "does not: %s" % (old, sid, url[:60]))
    detail = "ids=%d staged=%d collisions=%d guard=%s/%s map=%d" % (
        len(reg_ids), len(staged_ids), len(collide_ids),
        "ok" if indent_ok else "missing", "ok" if four_ok else "missing",
        len(recs))
    return leg("COLLCHECK", not bad, _mirrorcoll_detail(bad, detail))
