# ------------------------------------------------------------- REPOINTED ---
#
# Leg wording (reports/round-75/claims.json, claim C, legs[2]), as read here:
#
#   "REPOINTED: every `source:` line carries exactly one id whose row URL names
#    the cited document; every inline S-id in the entries resolves to a frozen
#    row; no campaign-namespace id is cited as a lane row except the
#    staged->lane substitutions in the frozen map; the staged S870 id is
#    replaced by lane S893; no unrelated staged id is preserved"
#
# Readings used by the implementation, each stated because the wording admits
# more than one:
#
#   R1 "source: line" is every line of the entry that carries the source field
#      (`[-*<space>]*source:`, the same line grammar PART A's header-only
#      source_lines() uses) -- not only the first provenance block: the frozen
#      entries keep one file per path with a SECOND provenance block for their
#      Part 2, and a header-only read would leave every citation below the first
#      `## ` ungraded (measured: a source line deleted from the registry and a
#      two-id source line in Part 2 both stayed green under the header-only
#      read).  The plural `sources:` field does not match that pattern and is not
#      a source line, so its ids are graded only by the inline rule.
#   R2 "row URL names the cited document" is a BY-DOCUMENT join, never
#      arithmetic: a source line's URLs and the row's source-cell URLs are
#      reduced to the frozen map's join key (host lowercased without `www.`,
#      default port dropped, path percent-decoded, persee.fr `/doc/page/<slug>/…`
#      collapsed to `/doc/<slug>`, a `web.archive.org/web/<ts>[flag]/…` wrapper
#      stripped to the embedded original) and the cited keys must be a SUBSET of
#      the row's keys -- the row may also carry page-level views the entry does
#      not quote.  A source line with no URL, or a row whose source cell carries
#      no URL, cannot be joined: both FAIL rather than pass silently.
#   R3 "inline S-id" is every S-id token anywhere in the entry (header and
#      body, source lines included); each must resolve to a frozen row
#      (cfg["allowed_ids"]).  This is what rejects the campaign-scope ids the
#      registry already reuses for unrelated documents (S744 -> the ushanka
#      page, S763 -> the tafl-games article).
#   R4 "campaign-namespace id" is an id the frozen by-document map names as
#      staged, the row_set/reused_rows `staged` values, or the frozen
#      forbidden/refused staged sets.  Such an id is legal ONLY when its map
#      target is itself (the identity substitution staged S885 -> lane S885);
#      a staged id whose map target differs (S864 -> S888) or that has no lane
#      row at all (S876, S902, S904, S905, S917, S919, S921, S870) FAILS.
#      Lane ids that are also staged ids in the campaign namespace but are not
#      in the frozen map (S886..S892, S893) cannot be distinguished from lane
#      citations by any frozen byte, so they are graded by R2's document join
#      and R3's row resolution -- the map is the only frozen authority for the
#      campaign namespace.
#   R5 "the staged S870 id is replaced by lane S893": S870 FAILS by R4, and the
#      replacement must be observable -- at least one entry cites the map's
#      lane target for S870 (S893), else the substitution did not happen.  The
#      target is read from the frozen map, never hard-coded.
#   R6 The map is read with `git show <freeze>:<cfg.map_path>` and its blob must
#      hash to cfg.map_sha256; an unpinned (empty) or mismatched map is a FAIL,
#      because the substitution table's authenticity is the clause's whole
#      content.  A map that is not ONE lookup table (one staged id with two
#      different targets) is a FAIL for the same reason.
#   R7 Absence of a `source:` line in an entry is NOT graded here: the frozen
#      ENTRIES leg owns the provenance-header field set.  This leg grades the
#      citations that exist plus R5's observable replacement.
#
# No new imports (PART A's re/hashlib/json/urlparse/... only); no network.



def _repointed_source_lines(text):
    """Every source-field line in the whole entry (R1), not only the first block.

    PART A's source_lines() stops at the first `## `; the frozen entries carry a
    second provenance block (their Part 2), whose `source:` lines are just as
    binding.  Same line grammar, whole document.
    """
    field = re.compile(r"^[-*\s]*source:\s*(.*)$")
    out = []
    for line in text.splitlines():
        m = field.match(line)
        if m:
            out.append(m.group(1))
    return out


def _repointed_unquote(s):
    """Percent-decode a URL path without importing urllib.parse.unquote."""
    if "%" not in s:
        return s
    out = bytearray()
    i, n = 0, len(s)
    while i < n:
        ch = s[i]
        if ch == "%" and i + 2 < n and re.fullmatch(r"[0-9A-Fa-f]{2}", s[i + 1:i + 3]):
            out.append(int(s[i + 1:i + 3], 16))
            i += 3
            continue
        out.extend(ch.encode("utf-8", "surrogateescape"))
        i += 1
    return bytes(out).decode("utf-8", "surrogateescape")


def _repointed_doc_key(url):
    """The frozen map's join key for one URL: (host, document path) or None.

    Strips a web.archive.org carrier wrapper (a capture is a carrier of the
    document, not a second document), lowercases the host, drops `www.` and a
    default port (:80 under http, :443 under https), percent-decodes the path
    and collapses a persee.fr per-page transcription
    (`/doc/page/<slug>/<transcription>`) onto the document `/doc/<slug>`.
    Scheme is not part of the key and no number is ever compared.
    """
    wrapper = re.compile(r"^/web/\d{8,14}[A-Za-z_]*/(.+)$")
    page = re.compile(r"^/doc/page/([^/]+)(?:/.*)?$")
    u = str(url or "").strip().rstrip(".,;:!?)]}\u3002\uff0c\uff1b\uff1a\uff01\uff1f"
                                  "\uff09\u3011\u300b\u00bb\"'")
    if not u:
        return None
    for _ in range(3):
        p = urlparse(u)
        host = (p.netloc or "").lower()
        path = p.path or ""
        if not host:
            return None
        if host == "web.archive.org" or host.endswith(".web.archive.org"):
            m = wrapper.match(path)
            if not m:
                return None
            inner = m.group(1)
            if not inner.lower().startswith(("http://", "https://")):
                inner = "https://" + inner.lstrip("/")
            u = inner
            continue
        break
    else:
        return None
    scheme = (p.scheme or "").lower()
    if "@" in host:
        host = host.rsplit("@", 1)[1]
    if host.endswith(":80") and scheme != "https":
        host = host[:-3]
    elif host.endswith(":443") and scheme == "https":
        host = host[:-4]
    if host.startswith("www."):
        host = host[4:]
    path = _repointed_unquote(path)
    if host == "persee.fr" or host.endswith(".persee.fr"):
        m = page.match(path)
        if m:
            path = "/doc/" + m.group(1)
    path = path.rstrip("/") or "/"
    return (host, path)


def _repointed_url_keys(urls):
    keys = set()
    for u in urls:
        k = _repointed_doc_key(u)
        if k is not None:
            keys.add(k)
    return keys


def _repointed_map_blob(ctx):
    """(doc, error): the by-document map read from the freeze commit, hash-pinned."""
    root, cfg = ctx["root"], ctx["cfg"]
    rel = str(cfg.get("map_path") or "").strip()
    if not rel:
        return None, "claim map.path is empty: no frozen by-document map to read"
    freeze = str(cfg.get("freeze") or "")
    r = git_bytes(root, "show", "%s:%s" % (freeze, rel))
    if r.returncode != 0:
        why = r.stderr.decode("utf-8", "replace").strip().splitlines()
        return None, ("cannot read the frozen map %s at %s: %s"
                      % (rel, freeze[:12], (why[0] if why else "git show failed")[:160]))
    raw = r.stdout
    want = str(cfg.get("map_sha256") or "").strip().lower()
    got = hashlib.sha256(raw).hexdigest()
    if not want:
        return None, ("claim map.sha256 is empty at freeze: the by-document map "
                      "%s is not hash-pinned" % rel)
    if want != got:
        return None, ("the frozen map %s hashes to %s, the claim pins %s"
                      % (rel, got, want))
    try:
        doc = json.loads(raw.decode("utf-8"))
    except (ValueError, UnicodeDecodeError) as e:
        return None, "the frozen map %s is not JSON: %s" % (rel, e)
    if not isinstance(doc, dict):
        return None, "the frozen map %s is not a JSON object" % rel
    return doc, None


def _repointed_ids(value):
    """Every S-id in a staged spec: one id, a "/"-separated list or a JSON list."""
    if isinstance(value, (list, tuple)):
        text = " ".join(str(x) for x in value)
    elif isinstance(value, str):
        text = value
    else:
        text = ""
    return [t.upper() for t in TOKEN_RE.findall(text)]


def _repointed_pairs(doc):
    """({(staged, lane): url}, error) from the frozen map, one lookup table only."""
    pairs = {}
    per_staged = {}

    def add(old, new, url):
        old = str(old or "").strip().upper()
        new = str(new or "").strip().upper()
        if not TOKEN_RE.fullmatch(old) or not TOKEN_RE.fullmatch(new):
            return
        key = (old, new)
        if key not in pairs:
            pairs[key] = str(url) if url else None
        elif url and not pairs[key]:
            pairs[key] = str(url)

    for a in doc.get("assignments") or []:
        if not isinstance(a, dict):
            continue
        add(a.get("staged_id") or a.get("old"),
            a.get("new_lane_id") or a.get("new_target") or a.get("new")
            or a.get("target") or a.get("lane"),
            a.get("url"))
    mapping = doc.get("map")
    if isinstance(mapping, dict):
        for old, val in mapping.items():
            if isinstance(val, dict):
                add(old, val.get("lane_id") or val.get("target") or val.get("lane"),
                    val.get("url"))
            else:
                add(old, val, None)
    conflict = []
    for (old, new) in pairs:
        if old in per_staged and per_staged[old] != new:
            conflict.append("%s -> %s and %s" % (old, per_staged[old], new))
        per_staged.setdefault(old, new)
    if conflict:
        return {}, ("the frozen map is not one lookup table: %s"
                    % "; ".join(dedupe(conflict)))
    return pairs, None


def _map_records(ctx):
    """{(staged_id, lane_id): url} from the frozen by-document map.

    Contract-named accessor: `git show <freeze>:<map.path>`, hash-pinned to
    cfg.map_sha256, never read from the graded tree.  Returns {} when the map
    cannot be read or does not pin (leg_repointed reports the reason).
    """
    doc, err = _repointed_map_blob(ctx)
    if err:
        return {}
    pairs, perr = _repointed_pairs(doc)
    if perr:
        return {}
    return pairs


def _repointed_staged_universe(cfg, lane_by_staged):
    """Every id the frozen config names as campaign-namespace (staged) side."""
    out = set(lane_by_staged)
    for key in ("row_staged", "reused_staged"):
        spec = cfg.get(key) or {}
        if isinstance(spec, dict):
            for val in spec.values():
                out.update(_repointed_ids(val))
        else:
            out.update(_repointed_ids(spec))
    for key in ("forbidden_ids", "refused_staged"):
        out.update(_repointed_ids(cfg.get(key) or []))
    return out


def _repointed_row_keys(row):
    """The document keys of one registry row's source cell."""
    cells = row_cells(row)
    if len(cells) <= SOURCE:
        return set()
    return _repointed_url_keys(urls_in(cells[SOURCE]))


def _repointed_problem(sid, allowed, staged, lane_by_staged, base_rows):
    """Why `sid` may not be cited as a lane row, or None when it resolves."""
    if sid in allowed:
        target = lane_by_staged.get(sid)
        if sid in staged and target not in (None, sid):
            return ("%s is a campaign-namespace id; the frozen map substitutes "
                    "it with lane %s" % (sid, target))
        return None
    if sid in staged:
        target = lane_by_staged.get(sid)
        if target:
            return ("%s is a campaign-namespace id cited as a lane row (frozen "
                    "map: %s -> %s)" % (sid, sid, target))
        return "%s is a campaign-namespace id cited as a lane row" % sid
    if sid in base_rows:
        return ("%s resolves to no frozen row; the lane registry reuses %s for "
                "an unrelated document" % (sid, sid))
    return "%s resolves to no frozen row" % sid


def leg_repointed(ctx):
    """REPOINTED: every source line names exactly one id whose registered row
    URL names the cited document (by-document join); every inline id resolves to
    a frozen row; campaign-namespace ids appear only as the frozen map's
    substitutions; the staged S870 id is replaced by its lane row."""
    mat, cfg = ctx["mat"], ctx["cfg"]
    try:
        lands_rows = parse_rows(read_tree(mat, REGISTRY))
    except Missing as e:
        return leg("REPOINTED", False, "registry unreadable at lands: %s" % e)
    doc, err = _repointed_map_blob(ctx)
    if err:
        return leg("REPOINTED", False, err)
    pairs, perr = _repointed_pairs(doc)
    if perr:
        return leg("REPOINTED", False, perr)
    allowed = set(cfg.get("allowed_ids") or ())
    if not allowed:
        return leg("REPOINTED", False,
                   "the frozen config names no lane rows (cfg.allowed_ids empty)")
    entries = cfg.get("entries") or []
    if not entries:
        return leg("REPOINTED", False, "the frozen config names no entries")
    lane_by_staged = {}
    for (old, new) in pairs:
        lane_by_staged[old] = new
    staged = _repointed_staged_universe(cfg, lane_by_staged)
    mat_base = ctx.get("mat_base")
    try:
        base_rows = parse_rows(read_tree(mat_base, REGISTRY)) if mat_base else {}
    except Missing:
        base_rows = {}
    bad = []
    cited = set()
    for e in entries:
        try:
            text = read_tree(mat, e)
        except Missing:
            bad.append("%s missing at lands" % e)
            continue
        for sline in _repointed_source_lines(text):
            ids = TOKEN_RE.findall(sline)
            if len(ids) != 1:
                bad.append("%s source line carries %d ids %s (want exactly one)"
                           % (e, len(ids), ids or "[]"))
                continue
            sid = ids[0]
            cited.add(sid)
            problem = _repointed_problem(sid, allowed, staged, lane_by_staged,
                                         base_rows)
            if problem:
                bad.append("%s source line: %s" % (e, problem))
                continue
            if sid not in lands_rows:
                bad.append("%s source line names %s with no registry row at "
                           "lands" % (e, sid))
                continue
            row_keys = _repointed_row_keys(lands_rows[sid])
            if not row_keys:
                bad.append("%s carries no document URL in its source cell, so "
                           "the cited document cannot be named" % sid)
                continue
            line_urls = urls_in(sline)
            if not line_urls:
                bad.append("%s source line for %s carries no URL (the row URL "
                           "cannot be joined to a document)" % (e, sid))
                continue
            for u in line_urls:
                key = _repointed_doc_key(u)
                if key is None or key not in row_keys:
                    bad.append("%s source line for %s cites a URL outside the "
                               "row's document: %s" % (e, sid, u))
        for lineno, line in enumerate(text.splitlines(), 1):
            for sid in TOKEN_RE.findall(line):
                cited.add(sid)
                problem = _repointed_problem(sid, allowed, staged,
                                             lane_by_staged, base_rows)
                if problem:
                    bad.append("%s:%d %s" % (e, lineno, problem))
    target = lane_by_staged.get("S870") or "S893"
    if target in allowed and target not in cited:
        bad.append("no entry cites lane %s: the staged S870 id is not replaced "
                   "by its lane row" % target)
    detail = "; ".join(dedupe(bad))
    if len(detail) > 300:
        detail = detail[:297] + "..."
    return leg("REPOINTED", not bad, detail)
