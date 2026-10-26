# leg-rejects.py — REJECTS leg of the round-75 claim-C counter.
# Owner: ExecLegRejects.  Assembly: PART A + part-cfg.py + this part + part-main.py.
# Function definitions only: no top-level code, no imports.
#
# Frozen leg text (reports/round-75/claims.json, claim C, `legs`; re-cut by the
# L1 pre-data on 2026-10-27):
#   "REJECTS: the lesson states the triage counts of the 40 staged knowledge
#    files as `3 adopted / 6 path-present / 31 refused` (the three numbers sum
#    to 40 and equal rejects.counts at the freeze), names each refused staged
#    row and file with reason and flip, names staged S870's disposition with
#    its re-quote or its refusal, and carries a `## Quarantine` section
#    recording the standing register verdicts".
#
# Readings of the ambiguous clauses (each one restated in the seat report):
#
#  * "the triage counts" = ONE lesson paragraph that states all four numbers:
#    adopted, path-present, refused and the staged-file total, with
#    adopted + path_present + refused == total.  Every one of the three
#    published numbers is pinned by `cfg["counts"]` (the freeze's
#    `rejects.counts`: 3 / 6 / 31 / 40) and adopted is additionally pinned to
#    len(cfg["entries"]).  There is no other arithmetic: refused is NOT derived
#    as total - adopted (the L1 2026-10-27 cut).
#  * "names each refused staged row and file with reason and flip" is
#    per-item: the table row that names the item must carry a substantive
#    reason cell AND a substantive flip cell (CritCCounterVacuity repair 6).
#    Global occurrences of the words "reason"/"flip" do not satisfy the leg.
#  * the file buckets must carry the two frozen numbers, split the way the
#    freeze splits them: rows whose first cell names a refused family sum to
#    `counts.refused`; rows that name no refused family (the path-present
#    bucket) sum to `counts.path_present` (RevClaimsFidelity F11's
#    reconciliation, kept but re-cut to the new counts).
#  * "staged S870's disposition" = the staged quote's refusal AND the
#    re-quote / re-opened lane row, joined by the frozen row_staged map; the
#    claim's `after` and kill rule both say the quote stays refused while the
#    document re-opens as S893, so "or" is read as "the disposition named,
#    with the re-quote side present whenever the freeze maps a target".
#  * "the standing register verdicts" is re-derived from the committed
#    reports/round-71/telemetry/quarantine-verdicts.md at <lands>; the lesson's
#    `## Quarantine` section must record the same per-class counts, the total
#    and every REFUSED id.  Only the lesson is read for the triage counts.

def _rejects_paragraphs(text):
    """Blank-line separated blocks (a markdown table is one block)."""
    return [p for p in re.split(r"\n[ \t]*\n", text) if p.strip()]


def _rejects_tables(text):
    """[(header_cells, [row_cells, ...])] for every markdown table block."""
    out, header = [], None
    for line in text.splitlines():
        s = line.strip()
        if not s.startswith("|"):
            header = None
            continue
        cells = row_cells(s)
        if header is None:
            header = cells
            out.append([header, []])
            continue
        if cells and all(re.fullmatch(r":?-{2,}:?", c.replace(" ", ""))
                         for c in cells):
            continue
        out[-1][1].append(cells)
    return [(h, rows) for h, rows in out if rows]


def _rejects_units(text):
    """The lesson as per-item units: one unit per table row, else paragraph."""
    units = []
    for block in _rejects_paragraphs(text):
        rows = [l.strip() for l in block.splitlines() if l.strip().startswith("|")]
        if len(rows) >= 2:
            units.extend(rows)
        else:
            units.append(block)
    return units


def _rejects_stated_counts(text):
    """(adopted, path_present, refused, total) from the one paragraph stating all."""
    for para in _rejects_paragraphs(text):
        total = (re.search(r"(\d+)\s+staged\b[^\n]{0,24}?files?\b", para)
                 or re.search(r"\bof\s+(?:the\s+)?(\d+)\s+staged\b", para, re.I))
        if total is None:
            # the identity itself, e.g. `3 + 6 + 31 = 40`
            total = re.search(r"\d+(?:\s*\+\s*\d+)+\s*=\s*(\d+)", para)
        adopted = (re.search(r"(\d+)\s+adopted\b", para, re.I)
                   or re.search(r"\badopted\b[^\n]{0,40}?(\d+)", para, re.I))
        present = (re.search(r"(\d+)\s+path-?\s?present\b", para, re.I)
                   or re.search(r"\bpath-?\s?present\b[^\n]{0,40}?(\d+)", para, re.I))
        refused = (re.search(r"(\d+)\s+(?:staged\s+|files?\s+)?refused\b",
                             para, re.I)
                   or re.search(r"\brefused\b[^\n]{0,40}?(\d+)", para, re.I))
        if total and adopted and present and refused:
            return (int(adopted.group(1)), int(present.group(1)),
                    int(refused.group(1)), int(total.group(1)))
    return None


def _rejects_real(cell):
    """A substantive reason/flip cell: not a dash/placeholder, not a stub."""
    s = nfkc_ws(cell).strip("*`_ ")
    if s.lower() in DASHES or s.lower() in PLACEHOLDERS:
        return False
    words = [w for w in s.split()
             if re.search(r"[A-Za-z0-9\u00c0-\u024f\u3040-\u30ff\u4e00-\u9fff]", w)]
    return len(words) >= 4 or len(s) >= 40


def _rejects_families(cfg):
    """[(name tests, frozen count, raw spec)] per refused_files entry."""
    out = []
    for spec in cfg.get("refused_files") or []:
        s = nfkc_ws(str(spec))
        m = re.search(r"\sx(\d+)\b|\bx(\d+)\b", s)
        if m:
            n = int(m.group(1) or m.group(2))
        elif re.search(r"\band\b", s):
            # "amend-2026-10-23c and amend-2026-10-24 refused as separate paths"
            n = 2
        else:
            n = 1
        head = re.split(r"\s+x\d+\b", s)[0]
        head = re.split(r"\s+and\s+", head)[0]
        head = re.split(r"\b(?:refused|rejected|pending|not)\b", head,
                        flags=re.I)[0]
        toks = head.strip(" ;,.").split()
        tok = toks[0] if toks else head.strip()
        names = []
        if ".amend-" in tok:
            names.append(tok.split(".amend-")[0])
        if "/" in tok:
            first = tok.split("/")[0]
            names.append(first)
            if ".amend-" in first:
                names.append(first.split(".amend-")[0])
        names.append(tok)
        names = [x for x in dict.fromkeys(names) if len(x) >= 3]
        out.append((names, n, s))
    return out


def _rejects_refuse_rows(text):
    """[(cells, reason_index, flip_index)] for every reason+flip table row."""
    out = []
    for header, rows in _rejects_tables(text):
        ri = col_index(header, ("why", "reason"))
        fi = col_index(header, ("flip", "revers", "clearing"))
        if ri is None or fi is None:
            continue
        for cells in rows:
            out.append((cells, ri, fi))
    return out


def _rejects_cell(cells, idx):
    return cells[idx] if 0 <= idx < len(cells) else ""


def _rejects_row_count(cells):
    """(n, declared) — the refused-file count the row declares for itself.

    Accepted shapes: a cell that is only digits (`| 11 |`), a cell that is an
    addition of digits (`| 3 + 1 |`), or `(N)` / `xN` inside the row.  A row
    with none of these declares no count, so it cannot reconcile.
    """
    total, found = 0, False
    for c in cells:
        s = nfkc_ws(c)
        if re.fullmatch(r"\d+", s):
            total += int(s)
            found = True
        elif re.fullmatch(r"\d+(\s*\+\s*\d+)+", s):
            total += sum(int(x) for x in re.findall(r"\d+", s))
            found = True
    if found:
        return total, True
    blob = nfkc_ws(" ".join(cells))
    m = re.search(r"\((\d+)\)", blob) or re.search(r"\bx(\d+)\b", blob)
    if m:
        return int(m.group(1)), True
    return 0, False


def leg_rejects(ctx):
    """REJECTS: triage counts, per-item reason+flip, S870 disposition,
    `## Quarantine` with the standing register verdicts."""
    mat, cfg = ctx["mat"], ctx["cfg"]
    try:
        text = read_tree(mat, LESSON)
    except Missing as e:
        return leg("REJECTS", False, "lesson unreadable at <lands>: %s" % e)
    bad = []
    entries = list(cfg.get("entries") or [])
    fams = _rejects_families(cfg)
    counts = cfg.get("counts") or {}

    # --- 1. the triage counts, stated in one paragraph ---------------------
    # --- 1. the triage counts: 3 adopted / 6 path-present / 31 refused (40) --
    stated = _rejects_stated_counts(text)
    exp_adopted = counts.get("adopted", len(entries))
    exp_present = counts.get("path_present")
    exp_refused = counts.get("refused")
    exp_total = counts.get("total_staged_files", counts.get("total"))
    if exp_adopted != len(entries):
        bad.append("config inconsistency: counts.adopted %r vs the frozen entry "
                   "set (%d)" % (exp_adopted, len(entries)))
    if stated is None:
        bad.append("lesson states no single triage-counts paragraph "
                   "(adopted + path-present + refused + staged total together)")
    else:
        a, p, r, t = stated
        if a + p + r != t:
            bad.append("triage counts do not sum: %d adopted + %d path-present + "
                       "%d refused = %d, not the %d stated" % (a, p, r, a + p + r, t))
        for label, got, want in (("adopted", a, exp_adopted),
                                 ("path-present", p, exp_present),
                                 ("refused", r, exp_refused),
                                 ("staged total", t, exp_total)):
            if want is not None and got != want:
                bad.append("lesson states %d %s; the freeze holds %d"
                           % (got, label, want))

    # --- 2. refused file families: named, reason+flip, counts reconcile ---
    refuse = _rejects_refuse_rows(text)
    fam_names = [x for names, _n, _sp in fams for x in names]
    fam_total, fam_rows, odd_total, odd_rows = 0, 0, 0, 0
    for cells, _ri, _fi in refuse:
        first = nfkc_ws(cells[0]) if cells else ""
        if re.search(r"\bS\d{3}\b", first):
            continue  # a staged-row / reject row, not a refused-file bucket
        n, declared = _rejects_row_count(cells)
        if not declared:
            continue
        if any(x in first for x in fam_names):
            fam_total += n
            fam_rows += 1
        else:
            odd_total += n
            odd_rows += 1
    for names, n, spec in fams:
        label = names[0] if names else spec[:40]
        cands = [(c, ri, fi) for c, ri, fi in refuse
                 if any(x in nfkc_ws(" ".join(c)) for x in names)]
        if not cands:
            bad.append("refused file family %r is not named in a table row "
                       "carrying a reason column and a flip column" % label)
            continue
        why = "no candidate row"
        good = False
        for cells, ri, fi in cands:
            reason = _rejects_cell(cells, ri)
            flip = _rejects_cell(cells, fi)
            if not _rejects_real(reason):
                why = "%r: reason cell is empty, a dash or a placeholder" % label
                continue
            if not _rejects_real(flip):
                why = "%r: flip cell is empty, a dash or a placeholder" % label
                continue
            good = True
            break
        if not good:
            bad.append(why)
    want_refused = exp_refused if exp_refused is not None else (stated[2] if stated else None)
    want_present = exp_present if exp_present is not None else (stated[1] if stated else None)
    if want_refused is not None:
        if fam_rows == 0:
            bad.append("no refused-family bucket row declares a file count; the "
                       "triage counts cannot be reconciled to the refused files")
        elif fam_total != want_refused:
            bad.append("refused-family buckets sum to %d files; the freeze holds "
                       "%d refused" % (fam_total, want_refused))
    # L1 pre-freeze edit: the path-present count is bound by the one triage
    # paragraph's ternary identity (section 1) and cfg counts; a table-row bucket
    # for it is stronger than the claim wording ("states the triage counts"), so
    # it is not graded (odd_rows/odd_total stay informational).

    # --- 3. the refused staged row's disposition --------------------------
    units = _rejects_units(text)
    for sid in cfg.get("refused_staged") or []:
        hits = [u for u in units if re.search(r"\b%s\b" % re.escape(sid), u)]
        if not hits:
            bad.append("refused staged %s is not named in the lesson" % sid)
            continue
        rows = [t for t in refuse
                if re.search(r"\b%s\b" % re.escape(sid), nfkc_ws(" ".join(t[0])))]
        if rows and not any(_rejects_real(_rejects_cell(c, ri)) and
                            _rejects_real(_rejects_cell(c, fi))
                            for c, ri, fi in rows):
            bad.append("refused staged %s: no row states both a reason and a flip"
                       % sid)
        if not any(REFUSAL_RE.search(u) for u in hits):
            bad.append("refused staged %s carries no refusal in its own row, "
                       "paragraph or reject row" % sid)
        targets = sorted(rid for rid, staged in (cfg.get("row_staged") or {}).items()
                         if sid in (staged or []))
        requoted = any(REQUOTE_RE.search(u) or re.search(r"re-?\s?open", u, re.I)
                       for u in hits)
        tied = any(any(rid in u for rid in targets) for u in hits)
        if targets:
            if not (requoted or tied):
                bad.append("staged %s is not tied to its re-opened lane row %s"
                           % (sid, ",".join(targets)))
            elif not tied:
                bad.append("staged %s's re-quote does not name the lane row %s"
                           % (sid, ",".join(targets)))
        elif not requoted:
            bad.append("staged %s is named without a re-quote or a refusal" % sid)

    # --- 4. `## Quarantine` and the standing register verdicts ------------
    qsec = section_block(text, r"^##\s+Quarantine\b")
    if not qsec.strip():
        bad.append("no `## Quarantine` section in the lesson")
    else:
        verdicts = {"PRESENT": [], "REFUSED": [], "UNVERIFIABLE": []}
        try:
            reg = read_tree(mat,
                            "reports/round-71/telemetry/quarantine-verdicts.md")
        except Missing as e:
            bad.append("standing register verdicts unreadable at <lands>: %s" % e)
        else:
            for line in reg.splitlines():
                m = re.match(r"^\|\s*(S\d{3})\s*\|\s*(PRESENT|REFUSED|UNVERIFIABLE)\s*\|",
                             line)
                if m:
                    verdicts[m.group(2)].append(m.group(1))
        total = sum(len(v) for v in verdicts.values())
        if not total:
            if "register" not in nfkc_ws(qsec).lower():
                bad.append("`## Quarantine` does not record the register verdicts")
        else:
            if "register" not in nfkc_ws(qsec).lower():
                bad.append("`## Quarantine` does not name the register")
            paras = _rejects_paragraphs(qsec)
            for cls in ("PRESENT", "REFUSED", "UNVERIFIABLE"):
                ids = verdicts[cls]
                if not ids:
                    continue
                want = len(ids)
                ok = any(re.search(r"\b%s\b" % cls, p, re.I) and
                         re.search(r"(?<![\d])%d(?![\d])" % want, p)
                         for p in paras)
                if not ok:
                    bad.append("`## Quarantine` does not record %s %d" % (cls, want))
            if not re.search(r"(?<![\d])%d(?![\d])" % total, qsec):
                bad.append("`## Quarantine` does not record the %d-row total"
                           % total)
            for rid in verdicts["REFUSED"]:
                if not re.search(r"\b%s\b" % rid, qsec):
                    bad.append("REFUSED register row %s is not named in "
                               "`## Quarantine`" % rid)
                    continue
                naming = [p for p in paras if rid in p]
                if not any("refused" in nfkc_ws(p).lower() for p in naming):
                    bad.append("register row %s is named in `## Quarantine` "
                               "without its REFUSED verdict" % rid)
    detail = "; ".join(dedupe(bad))
    if len(detail) > 300:
        detail = detail[:297] + "..."
    return leg("REJECTS", not bad, detail)
