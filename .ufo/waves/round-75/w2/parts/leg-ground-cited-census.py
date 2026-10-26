def _ground_cited_census_has_zero(text):
    """A standalone 0 token: `0`, never `10`, `808`, `0x`, `-0.5`."""
    return re.search(r"(?:^|[^\d])0(?:[^\d]|$)", text) is not None


def _ground_cited_census_ecodes(out):
    """E-code findings in a sources-census.sh TSV stream.

    The frozen wording is "prints no `^E[0-9][0-9]` line".  The fleet script
    emits `<lane>\\t<E-code>\\t<value>` (e.g. `file\\tE01\\tS894`), so the literal
    anchored form can never match the script's own output; the field form
    below implements the wording's reading — no E-code finding line — and also
    accepts a bare `E01` line should the format ever change.  The exit status
    remains the load-bearing check: sources-census.sh exits 1 on any E finding.
    """
    return dedupe(re.findall(r"(?:^|\t)(E\d\d)(?=\t|$)", out, re.M))


def leg_ground(ctx):
    """GROUND: reports/round-75/telemetry/gap-sweep.txt names the 808-row
    registry and 0 matches per fragment at base; the counter independently
    re-derives 0 at base from mat_base.

    Reading of the frozen text: it names the registry count and the fragments
    only, so `cfg["terms"]` (part of the ground config) is NOT graded here —
    the leg may neither add nor drop a term check — and "absent at base" for
    the entry paths belongs to ENTRIES.  The receipt is graded from `mat`
    (committed bytes at <lands>); the re-derivation is read from `mat_base`,
    which the counter materialized itself, so the receipt cannot vouch for
    itself.
    """
    mat, mat_base, cfg = ctx["mat"], ctx["mat_base"], ctx["cfg"]
    frags = list(cfg.get("fragments") or [])
    if not frags:
        return leg("GROUND", False, "cfg carries no ground fragments")
    try:
        base_text = read_tree(mat_base, REGISTRY)
    except Missing as e:
        return leg("GROUND", False, "base registry unreadable: %s" % e)
    base_rows = parse_rows(base_text)
    bad = []
    try:
        receipt = read_tree(mat, GROUND_RECEIPT)
    except Missing:
        receipt = ""
    if not receipt.strip():
        bad.append("receipt missing: %s" % GROUND_RECEIPT)
    else:
        m = re.search(r"(\d+)[- ]row", receipt)
        if not m:
            bad.append("receipt names no N-row registry")
        elif int(m.group(1)) != len(base_rows):
            bad.append("receipt names a %d-row registry; the base holds %d"
                       % (int(m.group(1)), len(base_rows)))
        lines = receipt.splitlines()
        for frag in frags:
            idxs = [i for i, line in enumerate(lines) if frag in line]
            if not idxs:
                bad.append("receipt does not name fragment %r" % frag)
                continue
            found_zero = False
            for i in idxs:
                # the 0 must belong to this fragment's own entry: its line plus
                # any continuation lines, stopping at a blank line or at the
                # next fragment's line, so a zero printed for a different item
                # (or for a whole-list total) cannot vouch for this one
                window = [lines[i]]
                for nxt in lines[i + 1:i + 3]:
                    if not nxt.strip() or any(f in nxt for f in frags):
                        break
                    window.append(nxt)
                text = "\n".join(window)
                # the fragment's own digits are stripped before the zero is
                # looked for, so e.g. `_0588` can never supply one
                for other in frags:
                    text = text.replace(other, "")
                if _ground_cited_census_has_zero(text):
                    found_zero = True
                    break
            if not found_zero:
                bad.append("receipt shows no 0 for fragment %r" % frag)
    low_registry = base_text.lower()
    for frag in frags:
        if frag.lower() in low_registry:
            bad.append("base registry already names the fragment %r" % frag)
    return leg("GROUND", not bad, "; ".join(dedupe(bad))[:300])


def leg_citedlines(ctx):
    """CITEDLINES: tools/check-cited-lines.py over the entries from the
    materialized tree prints `CITED-LINES: 0 finding(s)`.

    Reading of the frozen text: the tool is the one read from `mat` (the
    materialized lands tree) — the frozen wording pins no blob, so this leg
    does not pin one either; the entries are exactly `cfg["entries"]`, and a
    missing entry is a FAIL rather than a silently shorter run.
    """
    mat, cfg = ctx["mat"], ctx["cfg"]
    entries = list(cfg.get("entries") or [])
    if not entries:
        return leg("CITEDLINES", False, "cfg carries no entries")
    tool = os.path.join(mat, "tools/check-cited-lines.py")
    if not os.path.isfile(tool):
        return leg("CITEDLINES", False, "tools/check-cited-lines.py missing at lands")
    bad, paths = [], []
    for e in entries:
        p = os.path.join(mat, e)
        if os.path.isfile(p):
            paths.append(p)
        else:
            bad.append("%s missing" % e)
    if not paths:
        return leg("CITEDLINES", False, "; ".join(dedupe(bad)))
    r = subprocess.run([sys.executable, "-B", tool] + paths,
                       capture_output=True, text=True)
    out = (r.stdout or "").strip()
    if r.returncode != 0:
        bad.append("tool exit=%d" % r.returncode)
    if "CITED-LINES: 0 finding(s)" not in (r.stdout or ""):
        last = out.splitlines()[-1] if out else "(no stdout)"
        bad.append("no zero-findings line over %d file(s): %s"
                   % (len(paths), last))
    detail = "files=%d" % len(paths)
    if out:
        detail += " last-line=%s" % out.splitlines()[-1]
    if bad:
        detail = "; ".join(dedupe(bad)) + " (" + detail + ")"
    return leg("CITEDLINES", not bad, detail[:300])


def leg_census(ctx):
    """CENSUS: sources-census.sh validate against the materialized registry
    exits 0 with no `^E[0-9][0-9]` line.

    Materialization: the registry is `<mat>/corpus/SOURCES.md` where `mat` is
    the git-archive tree of <lands> the counter built itself; `--file` makes
    the fleet script resolve every row's `used-by` path against the parent of
    `corpus/` — i.e. against the same graded tree — so no lane directory name
    and no fleet-root lane layout are needed (`--root` would have required
    symlinking <mat> under a lane name the fleet conf knows).  `--today` is the
    frozen access date, so the E08 open-date check is deterministic.
    """
    mat, cfg = ctx["mat"], ctx["cfg"]
    fleet_root = ctx["fleet_root"]
    script = os.path.join(fleet_root, "scripts/sources-census.sh")
    if not os.path.isfile(script):
        return leg("CENSUS", False, "census script not found: %s" % script)
    registry = os.path.join(mat, REGISTRY)
    if not os.path.isfile(registry):
        return leg("CENSUS", False, "registry missing at lands: %s" % REGISTRY)
    today = cfg.get("access_date")
    if not today:
        return leg("CENSUS", False,
                   "cfg carries no access_date; the census date is undeterminable")
    r = subprocess.run([script, "validate", "--file", registry, "--today", today],
                       capture_output=True, text=True)
    out = r.stdout or ""
    bad = []
    if r.returncode != 0:
        bad.append("census exit=%d" % r.returncode)
    ecodes = _ground_cited_census_ecodes(out)
    if ecodes:
        bad.append("census TSV carries E-code line(s): %s" % ",".join(ecodes))
    detail = "exit=%d" % r.returncode
    tail = out.strip().splitlines()[-1] if out.strip() else ""
    if tail:
        detail += " last-line=%s" % tail
    if bad:
        detail = "; ".join(dedupe(bad)) + " (" + detail + ")"
    return leg("CENSUS", not bad, detail[:300])
