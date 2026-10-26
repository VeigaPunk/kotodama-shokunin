#!/usr/bin/env python3
r"""ADDITIVE patch to .ufo/waves/round-75/counters/junk-fixtures.py — round 75.

WHY THIS FILE EXISTS
--------------------
The shipped generator covers only 3 of claim C's 13 legs (ENTRIES via J1,
EVIDENCE via J2, FROZENCFG via J3) and 9 of claim Ca's 12 legs (LEDGER,
ANNOTATE, NOSTUB, APPENDONLY, R1EXEMPT, SEPARABLE, RECEIPTS, STAMP,
FROZENCFG).  Every leg listed below had NO junk fixture, so a do-nothing or
junk landing was unattacked on that leg.

HOW TO APPLY (the L1 does this; this file never edits the generator)
--------------------------------------------------------------------
1. Append everything below the `# ---- begin additions ----` marker to
   `.ufo/waves/round-75/counters/junk-fixtures.py`, AFTER `R1_PAIR` and
   BEFORE the `# ------------------- grading ---` section, so the helpers
   (`read`, `write`, `read_json`, `write_json`, `replace_text`,
   `registry_columns`, `set_cell`, `split_cells`, `sanitize_cell`,
   `git_show`, `registry_row`, `ROW_RE`, `REGISTRY`, `SCORECARD`,
   `LESSON`, `EVIDENCE_DIR`, `TELEMETRY`, `R75_LEDGER`, `R75_CLAIMS`,
   `FixtureError`) and the frozen claim accessors (`_adopted_ids`,
   `_entry_paths`, `_claims`, `_round_of`) are already bound.
2. UPDATE the registry tables in the generator.  The three lines go
   immediately BEFORE the `# ------------------------------- CLI ---`
   section (NOT at end of file: `main()` runs under the `__main__` guard,
   which sits after the CLI section, so a table update placed at EOF is
   applied too late and `--list` silently omits the additions):
       FIXTURES.update(ADDITIONS)
       ORDER = ORDER + ORDER_ADDITIONS
       SURVIVORS = SURVIVOR_FIXTURES        # survivor table (JC6)
   and add `selftest_additions()` to the end of `_selftest()` so
   `--selftest` covers the additions too.
3. TWO PLUMBING LINES the L1 must add (this patch cannot, by its seat
   contract):
   a. `--list` must print the survivors table too (JC6), so the receipt is
      never silent about a fixture that cannot go red.
   b. COMBINED grading needs an extra argv element.  Add an optional 5th
      element to the FIXTURES tuple (default None) and in `_run_fixtures`
      pass `extra=` to `run_counter`; the value is produced by
      `EXTRA_ARGS[name](fx)` defined at the bottom of this patch.  Without
      it, JCA3 grades COMBINED with no `--combined` and the leg fails closed
      ("the explicit --combined revision is required"), which mimics a catch
      for the wrong reason.
4. The runner's ACCEPTED tally must also report UNGRADED count: a sweep in
   which every fixture errored still prints `ACCEPTED JUNK LANDINGS: none`
   and exits 0 (measured pre-freeze: `--only J6,J10,G,R` produced four
   "no verdict was produced" lines and exit 0).  Print
   `# GRADED: <graded>/<total>` and exit 2 when graded < total.

FIXTURES ADDED (a correct counter REFUSES every one except the survivor)

  JC1   C   one adopted registry row's `opened` cell set to 2026-10-28
            (ROWS: opened must be 2026-10-27)
  JC2   C   the two first entries' `source:` ids swapped, so each entry
            cites a row whose URL names a different document (REPOINTED)
  JC3   C   one Gate admit row's access date moved off 2026-10-27 (GATE)
  JC4   C   the lesson's `## Quarantine` heading renamed (REJECTS)
  JC5   C   gap-sweep.txt's base row count edited 808 -> 809 (GROUND)
  JC6   C   SURVIVOR — tools/check-cited-lines.py replaced by a stub that
            prints the required zero-findings line; no leg can see it
            (documents the CITEDLINES authority hole; must NOT be counted
            as a catch)
  JC11  C   SURVIVOR — an entry body is 480 words of repeated boilerplate
            under one `## Body` heading; ENTRIES is a length-and-shape gate
            only, so the leg must stay PASS (J1 covers only the header-only
            stub, never filler)
  JC6b  C   an entry body cites the unresolvable lane id S999
            (CITEDLINES, and REPOINTED by its own wording)
  JC7   C   an escaped pipe planted inside one adopted row's `teaches` cell
            (CENSUS row geometry; ROWS also bars a pipe in any cell)
  JC8   C   validate-receipt.txt declares the `validate --file` run exited
            non-zero while still naming the frozen rows/entries
            (SCRATCHMIRROR)
  JC9   C   id-renumber-map.json maps one staged id to a lane id whose
            document differs (COLLCHECK)
  JC10  C   the myth-symbol heading count is bumped one above the live
            partition count (INDEX)
  JCA1  Ca  an eleventh, structurally valid ledger pair whose stated token
            EQUALS its base observation — the fixture's own commit is the
            freeze, so BASEMISMATCH reads it (BASEMISMATCH)
  JCA2  Ca  a REPAIR pair's base `stated_text` is re-appended to its
            statement path at <lands> (REPAIR)
  JCA3  Ca  an existing line of a pre-existing knowledge entry is edited IN
            PLACE (not appended, not a REPAIR stated_at line), graded with
            --combined = the mutant (COMBINED)
  JCA4  Ca  the committed r1exempt-green.txt is flipped to the RED shape —
            `LEG FAIL APPENDONLY`, `appendonly: FAIL`, non-zero exit — so the
            exemption's green half is contradicted by its own receipt
            (R1EXEMPT)

All fixtures are landing-relative, exactly like the shipped ones: they mutate
the tree they are pointed at and never rebuild it.  Every one of them raises
FixtureError with the missing artifact named when the reference tree does not
carry the landing yet (the generator's existing F6 convention), so a
pre-landing run reports "no verdict was produced" and never a catch.
"""

# ---- begin additions ----

import re as _jc_re  # already imported as `re`; alias keeps the patch hermetic

_JC_ID_RE = _jc_re.compile(r"\bS\d{3,}\b")
_JC_GATE_RE = _jc_re.compile(r"^##\s+Gate\b")
_JC_QUAR_RE = _jc_re.compile(r"^##\s+Quarantine\b")
_JC_H2_RE = _jc_re.compile(r"^##\s")
_JC_SRC_RE = _jc_re.compile(r"^([-*\s]*)source:\s*(.*)$")


def _jc_adopted_row(repo, ctx):
    """(id, line) of the first adopted row present in the graded tree."""
    adopted = _adopted_ids(ctx["claims"])
    ids = row_ids(read(repo, REGISTRY))
    for rid in adopted:
        if rid in ids:
            return rid, ids[rid]
    raise FixtureError("none of the adopted ids %s has a registry row in the "
                       "tree" % (adopted or "(claim C names no row_set)"))


def _jc_section_lines(text, heading_re):
    """(start, stop) line indexes of the first section whose heading matches.

    `start` is the heading line itself, `stop` the next H2 (or EOF).
    """
    lines = text.splitlines(keepends=True)
    start = None
    for i, line in enumerate(lines):
        if start is None:
            if heading_re.match(line):
                start = i
            continue
        if _JC_H2_RE.match(line):
            return start, i
    if start is None:
        return None, None
    return start, len(lines)


def _jc_entry_header(text):
    """The entry's header lines (everything before the first `## `)."""
    out = []
    for line in text.splitlines():
        if _JC_H2_RE.match(line):
            break
        out.append(line)
    return out


# ------------------------------------------------------------- claim C legs ---

def junk_JC1(repo, ctx):
    """One adopted row's `opened` cell carries the wrong date (ROWS).

    The row keeps its id, status, recheck cadence and every other cell, so the
    only frozen sub-check that can fail is `opened == 2026-10-27`.
    """
    rid, line = _jc_adopted_row(repo, ctx)
    cols = registry_columns(repo)
    old = split_cells(line)[cols["opened"]].strip()
    if old == "2026-10-28":
        raise FixtureError("row %s already carries 2026-10-28" % rid)
    edited = set_cell(line, cols["opened"], "2026-10-28")
    text = read(repo, REGISTRY)
    write(repo, REGISTRY, replace_text(text, line + "\n", edited + "\n",
                                       REGISTRY))
    ctx["detail"] = ("row %s: opened cell %r -> '2026-10-28'; every other "
                     "cell and every other row byte-identical" % (rid, old))


def junk_JC2(repo, ctx):
    """Two entries cite each other's row, so one id/URL pair per entry is
    wrong (REPOINTED)."""
    entries = _entry_paths(ctx["claims"])
    if len(entries) < 2:
        raise FixtureError("claim C names fewer than two entries")
    gotten = []
    for path in entries[:2]:
        try:
            text = read(repo, path)
        except OSError:
            raise FixtureError("entry %s is absent from the tree" % path)
        src = None
        for line in _jc_entry_header(text):
            m = _JC_SRC_RE.match(line)
            if m:
                src = line
                break
        ids = _JC_ID_RE.findall(src or "")
        if len(ids) != 1:
            raise FixtureError("%s carries %d source ids on its `source:` "
                               "line, expected exactly one"
                               % (path, len(ids)))
        gotten.append((path, text, src, ids[0]))
    (pa, ta, sa, ia), (pb, tb, sb, ib) = gotten
    if ia == ib:
        raise FixtureError("both entries cite the same id %s" % ia)
    write(repo, pa, replace_text(ta, sa, sb, pa))
    write(repo, pb, replace_text(tb, sb, sa, pb))
    ctx["detail"] = ("entry %s now cites %s (whose row URL names the other "
                     "document) and %s cites %s" % (pa, ib, pb, ia))


def junk_JC3(repo, ctx):
    """One Gate admit row's access date is moved off the frozen date (GATE)."""
    try:
        text = read(repo, LESSON)
    except OSError:
        raise FixtureError("lesson %s is absent from the tree" % LESSON)
    start, stop = _jc_section_lines(text, _JC_GATE_RE)
    if start is None:
        raise FixtureError("%s carries no `## Gate` section" % LESSON)
    lines = text.splitlines(keepends=True)
    for i in range(start, stop):
        if "2026-10-27" in lines[i]:
            lines[i] = lines[i].replace("2026-10-27", "2026-10-26", 1)
            write(repo, LESSON, "".join(lines))
            ctx["detail"] = ("the Gate row at %s:%d now carries access date "
                             "2026-10-26 while the frozen date is 2026-10-27"
                             % (LESSON, i + 1))
            return
    raise FixtureError("no Gate row in %s carries the access date 2026-10-27"
                       % LESSON)


def junk_JC4(repo, ctx):
    """The lesson's `## Quarantine` section is renamed away (REJECTS)."""
    try:
        text = read(repo, LESSON)
    except OSError:
        raise FixtureError("lesson %s is absent from the tree" % LESSON)
    start, _stop = _jc_section_lines(text, _JC_QUAR_RE)
    if start is None:
        raise FixtureError("%s carries no `## Quarantine` section" % LESSON)
    lines = text.splitlines(keepends=True)
    lines[start] = _jc_re.sub(r"Quarantine", "Held verdicts", lines[start],
                              count=1)
    write(repo, LESSON, "".join(lines))
    ctx["detail"] = ("the lesson's `## Quarantine` heading renamed to "
                     "`## Held verdicts`; its body is untouched")


def junk_JC5(repo, ctx):
    """gap-sweep.txt's base row count is edited (GROUND)."""
    rel = GROUND_RECEIPT if "GROUND_RECEIPT" in globals() else \
        TELEMETRY + "/gap-sweep.txt"
    try:
        text = read(repo, rel)
    except OSError:
        raise FixtureError("%s is absent from the tree" % rel)
    if "808" not in text:
        raise FixtureError("%s does not name the base row count 808" % rel)
    write(repo, rel, text.replace("808", "809", 1))
    ctx["detail"] = ("%s now states the base registry holds 809 rows, not the "
                     "derived 808" % rel)


_CITEDLINES_STUB = (
    "#!/usr/bin/env python3\n"
    "\"\"\"junk fixture: this checker reports the required line and inspects "
    "nothing.\"\"\"\n"
    "import sys\n"
    "print('CITED-LINES: 0 finding(s)')\n"
    "sys.exit(0)\n"
)


def junk_JC6(repo, ctx):
    """SURVIVOR: the lands tree's cited-lines checker is replaced by a stub.

    The frozen CITEDLINES wording runs `tools/check-cited-lines.py` FROM THE
    MATERIALIZED TREE, so the landing controls its own instrument.  A stub
    that prints `CITED-LINES: 0 finding(s)` satisfies the wording with no
    inspection at all.  This fixture is registered as a SURVIVOR: a correct
    reading of the frozen wording ACCEPTS it, and the run must record that,
    never count it as a catch.
    """
    rel = "tools/check-cited-lines.py"
    try:
        original = read(repo, rel)
    except OSError:
        raise FixtureError("%s is absent from the tree" % rel)
    write(repo, rel, _CITEDLINES_STUB)
    ctx["detail"] = ("%s (%d bytes) replaced by a 4-line stub that prints the "
                     "required `CITED-LINES: 0 finding(s)` and never reads an "
                     "entry" % (rel, len(original)))


def junk_JC6b(repo, ctx):
    """An entry body cites the unresolvable lane id S999 (CITEDLINES).

    REPOINTED's own wording ("every inline S-id in the entries resolves to a
    frozen row") also fails, so both legs are expected red — that is a finding
    in itself: no C-owned inline-id defect can move CITEDLINES alone without a
    tool substitution (see JC6).
    """
    entries = _entry_paths(ctx["claims"])
    if not entries:
        raise FixtureError("claim C names no entries")
    path = entries[0]
    try:
        text = read(repo, path)
    except OSError:
        raise FixtureError("entry %s is absent from the tree" % path)
    write(repo, path, text.rstrip("\n")
          + "\n\nA dangling lane citation: see S999 above.\n")
    ctx["detail"] = ("%s now cites the unresolvable lane id S999 in its body"
                     % path)


def junk_JC7(repo, ctx):
    """An escaped pipe is planted inside one adopted row's `teaches` cell.

    CENSUS's registry geometry (id..used-by, 11 cells, census NF==13) and
    ROWS's "no pipe in any cell" both bar it; ROWS is declared as well because
    the escaped pipe is a cell-content defect by its own wording.
    """
    rid, line = _jc_adopted_row(repo, ctx)
    cols = registry_columns(repo)
    teaches = split_cells(line)[cols["teaches"]].strip()
    edited = set_cell(line, cols["teaches"], teaches + " \\| fixture")
    text = read(repo, REGISTRY)
    write(repo, REGISTRY, replace_text(text, line + "\n", edited + "\n",
                                       REGISTRY))
    cols_after = split_cells(edited)
    ctx["detail"] = ("row %s: teaches cell now carries an escaped pipe (the "
                     "row splits into %d cells); no other byte changed"
                     % (rid, len(cols_after) - 2))


def junk_JC8(repo, ctx):
    """validate-receipt.txt declares a NON-ZERO validation exit (SCRATCHMIRROR).

    The receipt still names the frozen rows and entries, so only the exit
    status clause of the frozen wording can reject it.  When the reference
    tree carries no receipt yet, one is written.
    """
    rel = ".ufo/waves/round-75/assimilation/validate-receipt.txt"
    ids = _adopted_ids(ctx["claims"])
    entries = _entry_paths(ctx["claims"])
    try:
        text = read(repo, rel)
    except OSError:
        text = None
    wrote = "declared exit 1"
    if text is None:
        body = ("# junk fixture: a validation receipt for %s\n"
                "# entries: %s\n"
                "$ sources-census.sh validate --file <mirror>/corpus/SOURCES.md\n"
                "E07 row %s: teaches cell does not parse\n"
                "exit 1\n"
                % (", ".join(ids) or "(no rows)",
                   ", ".join(entries) or "(no entries)",
                   ids[0] if ids else "S???"))
        write(repo, rel, body)
        wrote = "wrote a receipt declaring exit 1"
    else:
        for old, new in (("exit 0", "exit 1"), ("exit=0", "exit=1"),
                         ("exit: 0", "exit: 1")):
            if old in text:
                write(repo, rel, text.replace(old, new, 1))
                wrote = "%r -> %r" % (old, new)
                break
        else:
            write(repo, rel, text.rstrip("\n") + "\nexit 1\n")
            wrote = "appended `exit 1`"
    ctx["detail"] = ("%s %s while still naming the frozen rows/entries, so the "
                     "mirrored-corpus validation cannot have exited 0"
                     % (rel, wrote))


def junk_JC9(repo, ctx):
    """The by-document map points one staged id at the wrong lane document."""
    rel = _claims(ctx["claims"], "C").get("map", {}).get("path") \
        or ".ufo/waves/round-75/assimilation/id-renumber-map.json"
    try:
        doc = read_json(repo, rel)
    except OSError:
        raise FixtureError("%s is absent from the tree" % rel)
    mapping = doc.get("map")
    if not isinstance(mapping, dict) or len(mapping) < 2:
        raise FixtureError("%s carries no by-document `map` object" % rel)
    staged = sorted(k for k, v in mapping.items()
                    if isinstance(v, dict) and v.get("lane_id"))
    if len(staged) < 2:
        raise FixtureError("%s maps fewer than two staged ids" % rel)
    src, dst = staged[0], staged[1]
    wrong = mapping[dst].get("lane_id")
    right = mapping[src].get("lane_id")
    if not wrong or wrong == right:
        raise FixtureError("the two mapped lane ids do not differ")
    assert isinstance(mapping[src], dict)
    mapping[src]["lane_id"] = wrong
    mapping[src]["target"] = wrong
    mapping[src]["lane"] = wrong
    write_json(repo, rel, doc)
    ctx["detail"] = ("%s: staged %s now maps to lane id %s (document %r) "
                     "instead of %s (document %r)"
                     % (rel, src, wrong,
                        str(mapping[dst].get("normalized_document_url"))[:60],
                        right,
                        str(mapping[src].get("normalized_document_url"))[:60]))


def junk_JC10(repo, ctx):
    """The myth-symbol heading count is bumped one above the live count."""
    rel = "corpus/README.md"
    try:
        text = read(repo, rel)
    except OSError:
        raise FixtureError("%s is absent from the tree" % rel)
    m = _jc_re.search(r"^## myth-symbol/ \((\d+)\)\s*$", text, _jc_re.M)
    if not m:
        raise FixtureError("%s carries no `## myth-symbol/ (n)` heading" % rel)
    old = int(m.group(1))
    new = old + 1
    write(repo, rel, replace_text(
        text, m.group(0), "## myth-symbol/ (%d)" % new, rel))
    ctx["detail"] = ("%s myth-symbol heading %d -> %d; the partition itself is "
                     "unchanged" % (rel, old, new))


# ------------------------------------------------------------ claim Ca legs ---

_JC_NULL_TREE = "4b825dc642cb6eb9a060e54bf8d69288fbee4904"


def junk_JCA1(repo, ctx):
    """An eleventh structurally valid pair whose stated token EQUALS its base
    observation (BASEMISMATCH).

    BASEMISMATCH reads the pairs from the freeze, so — like J4f — the fixture's
    own commit must BE the freeze: the pair is written into the tree the
    counter pins, and then the counter's own re-run at base finds a pair that
    is not red.
    """
    base = ctx.get("base")
    if not base or not _jc_re.fullmatch(r"[0-9a-f]{40}", base):
        raise FixtureError("JCA1 needs --base <40-hex> to re-run at the base "
                           "revision; got %r" % (base,))
    doc = read_json(repo, R75_LEDGER)
    pairs = doc.get("pairs")
    if not isinstance(pairs, list):
        raise FixtureError("%s carries no pairs list" % R75_LEDGER)
    if any(str(p.get("id")) == "L75-J1" for p in pairs):
        raise FixtureError("the ledger already carries L75-J1")
    pair = {
        "id": "L75-J1",
        "disposition": "ANNOTATE",
        "stated_at": "corpus/README.md:447",
        "stated_text": "## synthesis/ (29)",
        "stated_parse": r"\((\d+)\)",
        "observe_cmd": ["git", "diff", "--shortstat", _JC_NULL_TREE, base,
                        "--", "corpus/knowledge/synthesis/*.md"],
        "parse": "([0-9]+) files? changed",
        "expected_after": "29",
        "observed_at_base": "29",
        "red_at_base": False,
        "rederive": ("git diff --shortstat %s %s -- "
                     "'corpus/knowledge/synthesis/*.md'" % (_JC_NULL_TREE, base)),
        "why": ("junk fixture JCA1: the heading says 29 and the base synthesis "
                "partition holds 29, so stated == observed — a calibration "
                "pair that calibrates nothing"),
    }
    pairs.append(pair)
    write_json(repo, R75_LEDGER, doc)
    ctx["detail"] = ("an eleventh pair L75-J1 whose stated token 29 equals its "
                     "base observation 29 (stated == observed at base); the "
                     "frozen ledger carries it, so BASEMISMATCH must redden")
    ctx["own_freeze"] = True


def junk_JCA2(repo, ctx):
    """A REPAIR pair's base stated_text is re-appended to its statement path."""
    pairs = [p for p in (ctx["ledger"].get("pairs") or [])
             if p.get("disposition") == "REPAIR"]
    if not pairs:
        raise FixtureError("the ledger carries no REPAIR pair")
    for pair in pairs:
        spec = pair.get("statement_after")
        path = spec.get("path") if isinstance(spec, dict) else None
        stext = str(pair.get("stated_text") or "")
        if not path or not stext:
            continue
        try:
            text = read(repo, path)
        except OSError:
            raise FixtureError("statement path %s is absent from the tree"
                               % path)
        write(repo, path, text.rstrip("\n") + "\n" + stext + "\n")
        ctx["detail"] = ("the base stated_text %r of pair %s re-appended to %s, "
                         "so the base claim is still present at the statement "
                         "path at <lands>"
                         % (stext[:48], pair.get("id"), path))
        return
    raise FixtureError("no REPAIR pair carries both statement_after.path and "
                       "stated_text")


def junk_JCA3(repo, ctx):
    """An existing line of a pre-existing knowledge entry is edited IN PLACE.

    Not an appended line (the APPENDONLY wording allows appended lines) and
    not a REPAIR stated_at line, so the combined tree's APPENDONLY comparison
    must reject it.  Grade this fixture with `--combined <fixture-lands>`.
    """
    rel = "corpus/knowledge/myth-symbol/comparative-frameworks.md"
    try:
        text = read(repo, rel)
    except OSError:
        raise FixtureError("%s is absent from the tree" % rel)
    lines = text.splitlines(keepends=True)
    for i, line in enumerate(lines):
        if line.startswith("#") or not line.strip() or "|" in line:
            continue
        lines[i] = line.rstrip("\n") + " [junk fixture: in-place edit]\n"
        write(repo, rel, "".join(lines))
        ctx["detail"] = ("line %d of %s edited in place (the pre-existing line "
                         "gains %r); nothing is appended"
                         % (i + 1, rel, " [junk fixture: in-place edit]"))
        return
    raise FixtureError("%s carries no editable prose line" % rel)


def junk_JCA4(repo, ctx):
    """The committed `r1exempt-green.txt` carries the RED shape (R1EXEMPT).

    The exemption's green half must show `LEG PASS APPENDONLY` and exit 0.  The
    mutation flips those two facts while leaving everything else alone, so a
    receipt that cannot demonstrate the exemption is refused and the leg cannot
    be satisfied by a receipt that merely exists.
    """
    names = (TELEMETRY + "/r1exempt-green.txt", "r1exempt-green.txt")
    for rel in names:
        try:
            text = read(repo, rel)
        except OSError:
            continue
        new = text.replace("LEG PASS APPENDONLY", "LEG FAIL APPENDONLY")
        for old, rep in (("exit: 0", "exit: 1"), ("exit=0", "exit=1"),
                         ("exit 0", "exit 1")):
            if old in new:
                new = new.replace(old, rep, 1)
                break
        new = new.replace("appendonly: PASS", "appendonly: FAIL")
        if new == text:
            raise FixtureError("%s carries neither `LEG PASS APPENDONLY` nor "
                               "an exit-0 line to flip" % rel)
        write(repo, rel, new)
        ctx["detail"] = ("%s now reports `LEG FAIL APPENDONLY`, `appendonly: "
                         "FAIL` and a non-zero exit, so the green half of the "
                         "exemption is contradicted by its own receipt" % rel)
        return
    raise FixtureError("neither %s exists in the tree" % " nor ".join(names))


def junk_JC11(repo, ctx):
    """SURVIVOR: an entry whose whole body is 480 words of filler.

    ENTRIES is, by its own frozen wording, "a length-and-shape gate only": it
    requires a header of non-placeholder fields, one `## ` section and >= 478
    words.  A body of repeated boilerplate clears all three while asserting
    nothing about the source.  J1 tests only the header-only stub, so without
    this survivor a receipt could imply that ENTRIES rejects filler; it does
    not, and the claim's kill rule binds prose only through the ordinary
    re-open, not through this leg.
    """
    entries = _entry_paths(ctx["claims"])
    if not entries:
        raise FixtureError("claim C names no entries")
    path = entries[0]
    try:
        text = read(repo, path)
    except OSError:
        raise FixtureError("entry %s is absent from the tree" % path)
    lines = text.splitlines()
    head = []
    for line in lines:
        if _jc_re.match(r"^##\s", line):
            break
        head.append(line)
    filler = ("The document names a structure, and the structure names a "
              "method that the entry restates at length. ") * 40
    write(repo, path, "\n".join(head) + "\n\n## Body\n\n" + filler + "\n")
    words = len(filler.split())
    ctx["detail"] = ("%s: body replaced by %d words of repeated boilerplate "
                     "under one `## Body` heading; the provenance header is "
                     "untouched (ENTRIES is a length-and-shape gate only)"
                     % (path, words))


# ------------------------------------------------------- additions selftest ---

def _jc_fixture_tree(root):
    """A synthetic landing tree carrying every artifact the additions mutate.

    It is NOT the lane: it exists only so the mutators can be exercised without
    a landing commit.  Values that a mutator does not read (the README heading
    counts, the ledger facts) are the round-75 frozen values where those are
    stable, so a failing assertion points at the mutator, not at the fixture.
    """
    def w(rel, text):
        write(root, rel, text)

    w(REGISTRY,
      "# registry\n\n"
      "| id | source | kind | tier | scope | anchor | teaches | status | opened "
      "| recheck | used-by |\n"
      "|---|---|---|---|---|---|---|---|---|---|---|\n"
      "| S001 | Glottolog | docs | A | scope | anchor | teaches text | mined | "
      "2026-10-19 | on-release | corpus/knowledge/linguistics/x.md |\n"
      "| S885 | Barthes | paper | A | narratology | anchor cell | teaches prose "
      "| mined | 2026-10-27 | 180d | corpus/knowledge/myth-symbol/"
      "narrative-structure-frameworks.md |\n"
      "| S886 | Todorov | paper | A | narratology | anchor | teaches | mined | "
      "2026-10-27 | 180d | corpus/knowledge/myth-symbol/"
      "narrative-structure-frameworks.md |\n")
    w("corpus/README.md",
      "# corpus\n\n## linguistics/ (32)\n## synthesis/ (29)\n"
      "## myth-symbol/ (32)\n\n- `narrative-structure-frameworks.md` — "
      "narrative structure as a design method\n")
    w("SHONEN.md", "# kotodama\n\nRegistry counts at round 75 Ca landing — "
                   "rows: 817, mined: 722, queued: 58, rejected: 37.\n")
    w("corpus/knowledge/myth-symbol/comparative-frameworks.md",
      "# comparative frameworks\n\nA prose line about mythic structures.\n")
    for path, rid, doc in (
            ("corpus/knowledge/myth-symbol/narrative-structure-frameworks.md",
             "S885", "1113"),
            ("corpus/knowledge/myth-symbol/"
             "narrative-structure-frameworks.amend-2026-10-23.md", "S886",
             "1120"),
            ("corpus/knowledge/myth-symbol/"
             "narrative-structure-frameworks.amend-2026-10-23b.md", "S886",
             "1120")):
        w(path, "# entry\n\n- source: %s — https://www.persee.fr/doc/"
                "comm_0588-8018_1966_num_8_1_%s\n- verified-at: 2026-10-27\n"
                "- recheck: 180d\n- ground: a ground line\n"
                "- topic: narrative structure as a design method\n"
                "- scope: a scope line\n\n## Body\n\nSome mined prose.\n"
                % (rid, doc))
    w(LESSON, "# round 75\n\n## Gate\n\n| id | url | date | quote | verdict |\n"
              "|---|---|---|---|---|\n| S885 | https://example.invalid/a | "
              "2026-10-27 | \"a located quote\" | admitted |\n| S886 | "
              "https://example.invalid/b | 2026-10-27 | \"another quote\" | "
              "rejected |\n\n## Quarantine\n\nF-1 standing verdict.\n\n"
              "## Mistakes\n\nnone.\n")
    w("tools/check-cited-lines.py",
      "#!/usr/bin/env python3\nprint('CITED-LINES: 0 finding(s)')\n")
    w(TELEMETRY + "/gap-sweep.txt",
      "base f556d104: 808 rows; 0 matches per fragment\n")
    w(".ufo/waves/round-75/assimilation/validate-receipt.txt",
      "# receipt\nrows: S885 S886\nentries: narrative-structure-frameworks.md\n"
      "$ sources-census.sh validate --file <mirror>/corpus/SOURCES.md\nexit 0\n")
    w(TELEMETRY + "/r1exempt-green.txt",
      "# r1exempt-green.txt — round-75 R1EXEMPT fixture G\n"
      "exit: 0\nACCEPT-CA-75: FAIL legs=6/12\n"
      "LEG PASS APPENDONLY\nappendonly: PASS\nother-legs-unchanged: yes\n")
    w(TELEMETRY + "/r1exempt-red.txt",
      "# r1exempt-red.txt — round-75 R1EXEMPT fixture R\n"
      "exit: 1\nACCEPT-CA-75: FAIL legs=6/12\n"
      "LEG FAIL APPENDONLY\nappendonly: FAIL\nother-legs-unchanged: yes\n")
    w(".ufo/waves/round-75/assimilation/id-renumber-map.json",
      json.dumps({"round": 75, "map": {
          "S876": {"lane_id": "S885", "target": "S885", "lane": "S885",
                   "normalized_document_url": "persee.fr/doc/x/1113"},
          "S902": {"lane_id": "S886", "target": "S886", "lane": "S886",
                   "normalized_document_url": "persee.fr/doc/x/1120"}}},
          indent=1) + "\n")
    # the frozen docs, so JCA1 (which reads the graded tree's ledger) and the
    # claim accessors see the same bytes the counter reads from the freeze
    claims, ledger = _jc_synthetic_docs()
    w(R75_CLAIMS, json.dumps(claims, ensure_ascii=False, indent=1) + "\n")
    w(R75_LEDGER, json.dumps(ledger, ensure_ascii=False, indent=1) + "\n")


def _jc_synthetic_docs():
    """(claims, ledger) for the selftest: the lane's frozen docs when present."""
    def _load(rel):
        try:
            return read_json(LANE, rel)
        except (OSError, ValueError):
            return None
    claims = _load(R75_CLAIMS)
    ledger = _load(R75_LEDGER)
    if claims is None:
        claims = {"round": 75, "claims": [{"id": "C", "row_set": [
            {"id": "S885"}, {"id": "S886"}], "entries": [
                "corpus/knowledge/myth-symbol/narrative-structure-frameworks.md",
                "corpus/knowledge/myth-symbol/"
                "narrative-structure-frameworks.amend-2026-10-23.md"]}]}
    if ledger is None:
        ledger = {"round": 75, "claim": "Ca", "pairs": [
            {"id": "L75-01", "disposition": "REPAIR",
             "stated_at": "SHONEN.md:3",
             "stated_text": "rows: 817",
             "statement_after": {"path": "SHONEN.md",
                                 "parse": "rows: (\\d+)"}}]}
    return claims, ledger


def selftest_additions():
    """Exercise every added mutator on a synthetic landing tree (no counter).

    Returns 0 on PASS, 1 on FAIL.  Scratch: one mkdtemp dir under
    $SHOKUNIN_SCRATCH (or the system temp dir), removed before returning.
    """
    import tempfile

    work = tempfile.mkdtemp(prefix="junk-additions-",
                            dir=os.environ.get("SHOKUNIN_SCRATCH"))
    failures = []

    def check(name, cond, why=""):
        if not cond:
            failures.append("%s: %s" % (name, why))

    try:
        claims, ledger = _jc_synthetic_docs()
        base = (claims.get("base") if isinstance(claims, dict) else None)
        if not isinstance(base, str) or not re.fullmatch(r"[0-9a-f]{40}", base):
            base = "f" * 40
        names = list(ORDER_ADDITIONS) + list(SURVIVOR_ORDER)
        trees = {}
        for name in names:
            table = FIXTURES if name in FIXTURES else SURVIVOR_FIXTURES
            root = os.path.join(work, "tree-" + name)
            _jc_fixture_tree(root)
            ctx = {"repo": root, "freeze": base, "lands": base, "base": base,
                   "claims": claims, "ledger": json.loads(json.dumps(ledger)),
                   "detail": ""}
            try:
                table[name][1](root, ctx)
            except Exception as exc:                       # noqa: BLE001
                check(name, False, "%s: %s" % (type(exc).__name__, exc))
                continue
            trees[name] = root
            check(name + ":detail", bool(ctx["detail"]), "empty detail")

        def body(name, rel):
            return read(trees[name], rel)

        if "JC1" in trees:
            check("JC1", "| S885 | Barthes | paper | A | narratology | anchor "
                         "cell | teaches prose | mined | 2026-10-28 | 180d |"
                  in body("JC1", REGISTRY))
        if "JC2" in trees:
            check("JC2", "- source: S886" in body(
                "JC2", "corpus/knowledge/myth-symbol/"
                       "narrative-structure-frameworks.md"))
        if "JC3" in trees:
            check("JC3", "2026-10-26" in body("JC3", LESSON))
        if "JC4" in trees:
            lesson = body("JC4", LESSON)
            check("JC4", "## Quarantine" not in lesson
                  and "Held verdicts" in lesson, lesson[:60])
        if "JC5" in trees:
            check("JC5", "809" in body("JC5", TELEMETRY + "/gap-sweep.txt"))
        if "JC6" in trees:
            check("JC6", "CITED-LINES: 0 finding(s)" in body(
                "JC6", "tools/check-cited-lines.py")
                and "def " not in body("JC6", "tools/check-cited-lines.py"),
                "the stub still carries logic")
        if "JC6b" in trees:
            check("JC6b", "S999" in body(
                "JC6b", "corpus/knowledge/myth-symbol/"
                        "narrative-structure-frameworks.md"))
        if "JC7" in trees:
            rows = [l for l in body("JC7", REGISTRY).splitlines()
                    if l.startswith("| S885 ")]
            check("JC7", len(rows) == 1 and "\\|" in rows[0]
                  and len(rows[0].split("|")) == 14,
                  "row fields %d" % (len(rows[0].split("|")) if rows else 0))
        if "JC8" in trees:
            check("JC8", "exit 1" in body(
                "JC8", ".ufo/waves/round-75/assimilation/validate-receipt.txt"))
        if "JC9" in trees:
            doc = read_json(trees["JC9"], ".ufo/waves/round-75/assimilation/"
                                         "id-renumber-map.json")
            check("JC9", doc["map"]["S876"]["lane_id"] == "S886",
                  doc["map"]["S876"].get("lane_id"))
        if "JC10" in trees:
            check("JC10", "## myth-symbol/ (33)" in body("JC10",
                                                          "corpus/README.md"))
        if "JCA1" in trees:
            doc = read_json(trees["JCA1"], R75_LEDGER)
            pairs = [p for p in doc.get("pairs") or [] if p.get("id") == "L75-J1"]
            check("JCA1", len(pairs) == 1
                  and pairs[0].get("expected_after")
                  == pairs[0].get("observed_at_base"),
                  "pair not appended or tokens differ")
        if "JCA2" in trees:
            stext = str((ledger.get("pairs") or [{}])[0].get("stated_text"))
            check("JCA2", stext and stext in body("JCA2", "SHONEN.md"),
                  "base stated_text absent from the statement path")
        if "JCA3" in trees:
            check("JCA3", "[junk fixture: in-place edit]" in body(
                "JCA3", "corpus/knowledge/myth-symbol/"
                        "comparative-frameworks.md"))
        if "JC11" in trees:
            entry = body("JC11", "corpus/knowledge/myth-symbol/"
                                 "narrative-structure-frameworks.md")
            section = entry.split("## Body", 1)[-1]
            check("JC11", "## Body" in entry
                  and len(section.split()) >= 478
                  and "- source:" in entry, "words=%d"
                  % len(section.split()))
        if "JCA4" in trees:
            green = body("JCA4", TELEMETRY + "/r1exempt-green.txt")
            check("JCA4", "LEG FAIL APPENDONLY" in green
                  and "LEG PASS APPENDONLY" not in green
                  and "exit: 1" in green, green[:80])
    finally:
        shutil.rmtree(work, ignore_errors=True)

    for name in failures:
        print("FAIL %s" % name)
    print("ADDITIONS SELFTEST: %s (%d checks, %d added fixtures)"
          % ("PASS" if not failures else "FAIL",
             len(ORDER_ADDITIONS) + len(SURVIVOR_ORDER), len(ORDER_ADDITIONS)))
    return 0 if not failures else 1


# ------------------------------------------------------- registry additions ---

ADDITIONS = {
    "JC1": ("C", junk_JC1, ("ROWS",),
            "FAIL: one adopted row's opened cell is 2026-10-28 (ROWS)"),
    "JC2": ("C", junk_JC2, ("REPOINTED",),
            "FAIL: two entries cite each other's row id, so each source id's "
            "row URL names a different document (REPOINTED)"),
    "JC3": ("C", junk_JC3, ("GATE",),
            "FAIL: a Gate admit row's access date is 2026-10-26 (GATE)"),
    "JC4": ("C", junk_JC4, ("REJECTS",),
            "FAIL: the lesson's `## Quarantine` heading is renamed away "
            "(REJECTS)"),
    "JC5": ("C", junk_JC5, ("GROUND",),
            "FAIL: gap-sweep.txt states the base holds 809 rows (GROUND)"),
    "JC6b": ("C", junk_JC6b, ("CITEDLINES", "REPOINTED"),
             "FAIL: an entry body cites the unresolvable lane id S999 "
             "(CITEDLINES; REPOINTED also bars it by its own wording)"),
    "JC7": ("C", junk_JC7, ("CENSUS", "ROWS"),
            "FAIL: an escaped pipe inside one adopted row's teaches cell "
            "(CENSUS row geometry; ROWS bars a pipe in any cell)"),
    "JC8": ("C", junk_JC8, ("SCRATCHMIRROR",),
            "FAIL: validate-receipt.txt declares the validation exited "
            "non-zero while naming the frozen rows/entries (SCRATCHMIRROR)"),
    "JC9": ("C", junk_JC9, ("COLLCHECK",),
            "FAIL: the by-document map points one staged id at a lane id whose "
            "document differs (COLLCHECK)"),
    "JC10": ("C", junk_JC10, ("INDEX",),
             "FAIL: the myth-symbol heading count is one above the live "
             "partition (INDEX)"),
    "JCA1": ("Ca", junk_JCA1, ("BASEMISMATCH",),
             "FAIL: an eleventh frozen pair states the token it observes at "
             "base (BASEMISMATCH)"),
    "JCA2": ("Ca", junk_JCA2, ("REPAIR",),
             "FAIL: a REPAIR pair's base stated_text is present again at its "
             "statement path (REPAIR)"),
    "JCA3": ("Ca", junk_JCA3, ("COMBINED",),
             "FAIL: a pre-existing knowledge line is edited in place; graded "
             "with --combined = the mutant (COMBINED)"),
    "JCA4": ("Ca", junk_JCA4, ("R1EXEMPT",),
             "FAIL: the committed r1exempt-green.txt reports `LEG FAIL "
             "APPENDONLY` and a non-zero exit (R1EXEMPT: the exemption's own "
             "receipts must demonstrate the rule-2 edit grading green)"),
}

ORDER_ADDITIONS = ("JC1", "JC2", "JC3", "JC4", "JC5", "JC6b", "JC7", "JC8",
                   "JC9", "JC10", "JCA1", "JCA2", "JCA3", "JCA4")

# The documented survivor: a correct reading of the frozen wording ACCEPTS it.
# Register it in its own table so no receipt can book it as a catch.
SURVIVOR_FIXTURES = {
    "JC6": ("C", junk_JC6, (),
            "SURVIVOR (must be ACCEPTED): the lands tree's "
            "tools/check-cited-lines.py is replaced by a stub printing "
            "`CITED-LINES: 0 finding(s)`; the frozen wording runs the "
            "lands-tree tool, so no leg can see the substitution.  Freeze the "
            "tool blob or the survivor stays open."),
    "JC11": ("C", junk_JC11, (),
             "SURVIVOR (ENTRIES must stay PASS): an entry body of 480 words of "
             "repeated boilerplate under one `## Body` heading.  ENTRIES is "
             "declared a length-and-shape gate only, so filler clears it; J1 "
             "covers only the header-only stub.  The claim's prose obligation "
             "is enforced by the ordinary re-open, never by this leg."),
}

SURVIVOR_ORDER = ("JC6", "JC11")

# Extras passed to run_counter per fixture (see plumbing note 3b).
EXTRA_ARGS = {
    "JCA3": lambda fx: ("--combined", fx.rev),
}
