# ------------------------------------------------------------ part-cfg.py ---
# owner: ExecCtrCfgMain.  Function definitions only (no top-level code, no new
# imports); spliced by the L1 immediately after PART A and before the leg
# parts.  Round-74 provenance: `.ufo/waves/round-74/counters/accept-c.py`
# lines 473-745 (`_frozen_claim _paths_from_spec _id_list _row_pairs
# load_frozen_config _row_url_keys _gate_admit_row _min_entry_words _evidence
# _window _entry_citations`), names and signatures kept.
#
# Round-75 deltas carried here, each traceable to a w1 finding:
#
#  D1 multi-id staged rows.  `row_set[i].staged` may be one id, a
#     "/"-separated string or a JSON list; `cfg["row_staged"]` maps a lane id
#     to a LIST of staged ids (S885 <- S876/S885/S917/S921).  One registry row
#     per DOCUMENT, not per staged occurrence (SimplifierRows §4, ExecRenumber
#     §2/§3).  `_row_pairs` also rejects a staged id claimed by two lane rows:
#     a by-document map with an ambiguous staged side is not a map.
#  D2 by-document map.  cfg carries `map_path`/`map_sha256` (read from the
#     freeze blob; a null/absent sha256 makes the frozen config unusable) and
#     `row_doc` (the claim's `document` string per lane id).  Nothing here does
#     id arithmetic; identity is the document URL (ExecRenumber §1).
#  D3 page-level Persée URLs, and the two carrier/view folds.  A per-page
#     transcription `/doc/page/<slug>/<page>` is a VIEW of `/doc/<slug>`; a
#     `web.archive.org/web/<ts>/…` wrapper is a CARRIER of the embedded
#     original; `%20` and a raw space name the same document (S892).  These are
#     folded by `_doc_url_key`, and `_row_url_keys`/`_gate_admit_row` compare
#     with `_url_keys` (raw key UNION folded key) so a page-level citation and
#     a document-level source cell still join.  Legs that compare a cited or
#     fetched URL against a row MUST use `_url_keys(urls_in(...))` against
#     `_row_url_keys(...)` (raw-key-only intersection misses a page view).
#  D4 evidence window scope.  `window-scope: excerpt` needs >= 4096 characters,
#     `whole-document` needs a window shorter than 4096 whose length equals
#     `visible-chars:`; `_evidence`/`_window` only parse — the scope rule is
#     graded by the EVIDENCE leg (leg-evidence.py, `_evidence_core`).
#  D5 `terms` (the r74 `cjk_terms` slot, renamed by the round-75 claim text;
#     `ground.cjk_terms` is still accepted as the source key).
#  D6 `owned_inplace`.  The claim's in-place README heading edit
#     (`## myth-symbol/ (29)` -> `## myth-symbol/ (32)`) is carried so the
#     INDEX leg can exempt exactly those heading lines from the README diff
#     scope (H4) instead of failing on Ca's partition-count lines.
#  D7 `refused_staged` holds STAGED ids only (extracted ids - lane ids), so
#     S885 (staged AND a lane id) and S893 (the lane id the refusal prose also
#     names) are never reported as a refused staged row.  The raw prose is kept
#     in `refused_staged_text` for the REJECTS leg.  r75 freezes no
#     `forced_new_quotes` list: a re-quoted row is derived as
#     `row_staged[sid] & set(refused_staged)`.
#
# Ambiguities in the frozen text and their readings (also in the seat report):
#  A1 GATE "per adopted row URL + access date 2026-10-27" — the access date is
#     not a literal key of claims.json at the round-75 draft, so it is derived
#     from the frozen `after`/`legs` text (most frequent YYYY-MM-DD) and the
#     configuration refuses when no candidate exists (PART A docstring).
#  A2 REPOINTED "no campaign-namespace id is cited as a lane row except the
#     staged->lane substitutions in the frozen map" — read as: the forbidden set
#     is (staged ids NOT adopted as lane ids), so S885 is never forbidden
#     (CritCCounterVacuity repair 4, SimplifierRows §8(c)).
#  A3 INDEX "the myth-symbol heading equals the live partition count (32)" —
#     that line belongs to claim Ca's pairs L75-02/L75-03; this part only
#     exposes `owned_inplace` so the INDEX leg can exempt it (H4).


def _frozen_claim(doc):
    """The claim object with id C (case-insensitive) inside a claims document."""
    for c in doc.get("claims") or []:
        if isinstance(c, dict) and str(c.get("id", "")).upper() == "C":
            return c
    return None


def _cfg_pct_decode(s):
    """Percent-decode `%XX` runs without importing urllib (PART A imports are
    fixed; `%20` is the only form that occurs, the general form is free)."""
    def take(m):
        try:
            return chr(int(m.group(1), 16))
        except ValueError:
            return m.group(0)
    return re.sub(r"%([0-9A-Fa-f]{2})", take, s)


def _doc_url_key(u):
    """The DOCUMENT a URL names: (host without `www.`, document path).

    Folds the two carriers/views claim C's row set depends on:
      * `web.archive.org/web/<ts><mod>/<original>` -> key of <original>
        (a capture is a carrier of the document, not a second document);
      * `persee.fr/doc/page/<slug>/<page>` and `/docAsPDF/<slug>.pdf` ->
        `/doc/<slug>` (a per-page transcription is a view of the document).
    `%20` and a raw space are the same character after decoding, so the S892
    claim string and its row cell name one document.  Never numeric, never
    arithmetic.
    """
    u = (u or "").strip()
    host, path = norm_url(u)
    if host.startswith("www."):
        host = host[4:]
    path = _cfg_pct_decode(path)
    if host == "web.archive.org":
        m = re.match(r"^/web/\d{8,14}[a-z_]*/(.+)$", path)
        if m:
            return _doc_url_key(m.group(1))
    m = re.match(r"^/doc/page/([^/]+)/", path)
    if m:
        path = "/doc/" + m.group(1)
    else:
        m = re.match(r"^/docAsPDF/([^/]+?)(?:\.pdf)?$", path)
        if m:
            path = "/doc/" + m.group(1)
    return (host, path)


def _url_keys(urls):
    """Both keys of every URL: the raw norm_url key and its document key.

    A set, so a comparison is order-insensitive; the union lets a page-level
    citation (raw page key) meet a source cell that carries the page URL, and
    lets a document-level citation meet a row that carries a page URL.
    """
    out = set()
    for u in urls:
        try:
            out.add(norm_url(u))
        except ValueError:
            continue
        out.add(_doc_url_key(u))
    return out


def _paths_from_spec(spec):
    """Repo-relative paths from a claim `entries`-like value (string, list or
    object with a named path key), `./` stripped, order preserved."""
    out = []

    def take(value):
        if isinstance(value, str):
            v = value.strip()
            if v:
                out.append(v[2:] if v.startswith("./") else v)
        elif isinstance(value, list):
            for item in value:
                take(item)
        elif isinstance(value, dict):
            for key in ("path", "paths", "entries", "amendments", "canonical",
                        "admitted"):
                if key in value:
                    take(value[key])

    if isinstance(spec, dict):
        for key in ("paths", "entries", "amendments", "canonical", "admitted"):
            if key in spec:
                take(spec[key])
    else:
        take(spec)
    return list(dict.fromkeys(out))


def _id_list(value, what):
    """A list of S-ids from a list/string claim value (order preserved)."""
    if isinstance(value, str):
        value = [value]
    out = []
    if not isinstance(value, list):
        raise ConfigError("%s is not a list" % what)
    for item in value:
        v = str(item).strip().upper()
        if not TOKEN_RE.fullmatch(v):
            raise ConfigError("%s carries a non-S-id item: %r" % (what, item))
        out.append(v)
    return list(dict.fromkeys(out))


def _staged_ids(value, what):
    """D1: the staged side of one row_set item, always a LIST.

    Accepts one id (`"S902"`), a "/"-separated string (`"S876/S885/S917/S921"`)
    or a JSON list (of either form).  Order is the claim's, duplicates dropped.
    """
    if isinstance(value, str):
        parts = re.split(r"[/,;\s]+", value.strip())
    elif isinstance(value, list):
        parts = []
        for item in value:
            if isinstance(item, str):
                parts.extend(re.split(r"[/,;\s]+", item.strip()))
            else:
                raise ConfigError("%s carries a non-string staged item: %r"
                                  % (what, item))
    else:
        raise ConfigError("%s carries no staged ids: %r" % (what, value))
    out = []
    for part in parts:
        v = part.strip().upper()
        if not v:
            continue
        if not TOKEN_RE.fullmatch(v):
            raise ConfigError("%s carries a non-S-id staged item: %r"
                              % (what, part))
        if v not in out:
            out.append(v)
    if not out:
        raise ConfigError("%s carries no staged ids" % what)
    return out


def _row_pairs(spec, what):
    """[(lane id, [staged ids])] from a row_set/reused_rows list (D1).

    A lane id is the row the registry will hold; the staged ids are the
    campaign ids it absorbs by document.  A staged id claimed by two lane rows
    is an ambiguous by-document map and is refused here, not graded later.
    """
    if not isinstance(spec, list):
        raise ConfigError("%s is not a list" % what)
    pairs, seen, owners = [], set(), {}
    for item in spec:
        if not isinstance(item, dict):
            raise ConfigError("%s carries a non-object item: %r" % (what, item))
        rid = str(item.get("id", "")).strip().upper()
        if not TOKEN_RE.fullmatch(rid):
            raise ConfigError("%s item needs an S-id lane id: %r" % (what, item))
        staged = _staged_ids(item.get("staged", ""), what)
        if rid in seen:
            raise ConfigError("%s repeats lane id %s" % (what, rid))
        seen.add(rid)
        for sid in staged:
            other = owners.get(sid)
            if other is not None and other != rid:
                raise ConfigError("%s maps staged %s to both %s and %s"
                                  % (what, sid, other, rid))
            owners[sid] = rid
        pairs.append((rid, staged))
    return pairs


def _cfg_refusal_text(rejects):
    """D7: the raw refused-staged strings, from whichever key carries them.

    The frozen file is the contract, so the accepted spellings are the PART A
    docstring's set: prose (`refused_staged_not_appended`, `refused_staged`) and
    id lists (`forced_new_quotes`, `folded_dropped`).
    """
    out = []
    for key in ("refused_staged_not_appended", "refused_staged",
                "forced_new_quotes", "folded_dropped"):
        value = rejects.get(key)
        if value is None:
            continue
        items = value if isinstance(value, list) else [value]
        for item in items:
            text = str(item).strip()
            if text:
                out.append(text)
    return out


def _cfg_access_date(claim, doc):
    """A1: the claim's access date, or the date the frozen text repeats.

    Every date-shaped token of the frozen `after` clause and `legs` list is a
    candidate; the most frequent one wins (ties: the earliest, so the choice is
    deterministic).  No candidate, or an explicit non-YYYY-MM-DD value, makes
    the frozen configuration unusable (PART A docstring).
    """
    explicit = str(claim.get("access_date") or doc.get("access_date") or "").strip()
    if explicit:
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", explicit):
            raise ConfigError("access date at freeze is not YYYY-MM-DD: %r"
                              % explicit)
        return explicit
    text = " ".join([str(claim.get("after") or ""),
                     str(claim.get("before") or ""),
                     " ".join(str(x) for x in (claim.get("legs") or []))])
    dates = re.findall(r"\b(20\d\d-\d\d-\d\d)\b", text)
    if not dates:
        raise ConfigError("the frozen claim carries no access date (no "
                          "access_date key and no YYYY-MM-DD in its after/legs "
                          "text)")
    best = sorted(Counter(dates).items(), key=lambda kv: (-kv[1], kv[0]))[0][0]
    return best


def load_frozen_config(root, freeze):
    """H1: every constant comes from `git show <freeze>:claims.json`.

    Returns exactly the CFG-CONTRACT keys: freeze, frozen_sha256, base,
    access_date, rows, row_staged, row_doc, reused, reused_staged, entries,
    fragments, terms, refused_staged, refused_staged_text, refused_files,
    counts, map_path, map_sha256, frozen_legs, allowed_ids, forbidden_ids,
    owned_inplace, claim_keys.
    """
    r = git_bytes(root, "show", "%s:%s" % (freeze, CLAIMS))
    if r.returncode != 0:
        raise ConfigError("cannot read %s at freeze %s: %s"
                          % (CLAIMS, freeze[:12],
                             r.stderr.decode("utf-8", "replace").strip()))
    raw = r.stdout
    try:
        doc = json.loads(raw.decode("utf-8"))
    except (ValueError, UnicodeDecodeError) as e:
        raise ConfigError("%s at freeze %s is not JSON: %s"
                          % (CLAIMS, freeze[:12], e))
    if not isinstance(doc, dict):
        raise ConfigError("%s at freeze is not a JSON object" % CLAIMS)
    claim = _frozen_claim(doc)
    if claim is None:
        raise ConfigError("%s at freeze carries no claim with id C" % CLAIMS)
    missing = [k for k in CLAIM_KEYS if k not in claim]
    if missing:
        raise ConfigError("claim C at freeze lacks %s" % ", ".join(missing))
    base = str(doc.get("base") or claim.get("base") or "").strip().lower()
    if not re.fullmatch(r"[0-9a-f]{40}", base):
        raise ConfigError("claim base at freeze is not a 40-hex revision: %r" % base)

    # D1: one lane row per document, staged side a list.
    row_pairs = _row_pairs(claim["row_set"], "row_set")
    if not row_pairs:
        raise ConfigError("row_set at freeze is empty")
    reused_pairs = _row_pairs(claim.get("reused_rows") or [], "reused_rows")

    entries = _paths_from_spec(claim["entries"])
    if not entries:
        raise ConfigError("entries at freeze is empty")
    for e in entries:
        if e.startswith("/") or ".." in e.split("/"):
            raise ConfigError("entry path at freeze is not repo-relative: %r" % e)

    ground = claim["ground"]
    if not isinstance(ground, dict):
        raise ConfigError("ground at freeze is not an object")
    fragments = [str(x) for x in (ground.get("fragments") or [])]
    terms = [str(x) for x in (ground.get("terms")
                              or ground.get("cjk_terms") or [])]
    if not fragments:
        raise ConfigError("ground.fragments at freeze is empty")
    if not terms:
        raise ConfigError("ground.terms at freeze is empty")

    rejects = claim["rejects"]
    if not isinstance(rejects, dict):
        raise ConfigError("rejects at freeze is not an object")
    refused_staged_text = _cfg_refusal_text(rejects)
    refused_files = []
    for key in ("refused_files_pending_triage", "refused_files", "families"):
        value = rejects.get(key)
        if value is None:
            continue
        items = value if isinstance(value, list) else [value]
        refused_files.extend(str(x) for x in items if str(x).strip())
    counts = rejects.get("counts") or {}
    if not isinstance(counts, dict):
        raise ConfigError("rejects.counts at freeze is not an object")
    parsed_counts = {}
    for key, value in counts.items():
        try:
            parsed_counts[str(key)] = int(value)
        except (TypeError, ValueError):
            continue

    # D2: the by-document map is named by path and digest at the freeze.
    map_spec = claim.get("map")
    if not isinstance(map_spec, dict):
        raise ConfigError("claim C at freeze carries no map object")
    map_path = str(map_spec.get("path") or "").strip()
    map_sha = str(map_spec.get("sha256") or "").strip().lower()
    if not map_path or map_path.startswith("/") or ".." in map_path.split("/"):
        raise ConfigError("claim map.path at freeze is not a relative repo "
                          "path: %r" % map_path)
    if not re.fullmatch(r"[0-9a-f]{64}", map_sha):
        raise ConfigError("claim map.sha256 at freeze is not a 64-hex digest "
                          "(the by-document map cannot be pinned): %r"
                          % (map_spec.get("sha256")))

    frozen_legs = []
    for item in claim.get("legs") or []:
        name = str(item).split(":", 1)[0].strip().upper()
        if name:
            frozen_legs.append(name)

    access_date = _cfg_access_date(claim, doc)

    # D6: the claim's in-place edit (README partition heading), normalised to
    # objects carrying at least `path`.
    owned_inplace = []
    for item in claim.get("owned_inplace") or []:
        if isinstance(item, dict) and str(item.get("path") or "").strip():
            owned_inplace.append(dict(item))
        elif isinstance(item, str) and item.strip():
            owned_inplace.append({"path": item.strip()})

    rows = [p[0] for p in row_pairs]
    row_staged = dict(row_pairs)
    row_doc = {}
    for item in claim["row_set"]:
        if isinstance(item, dict):
            rid = str(item.get("id", "")).strip().upper()
            row_doc[rid] = str(item.get("document") or "").strip()
    reused = [p[0] for p in reused_pairs]
    reused_staged = dict(reused_pairs)
    lane_ids = set(rows) | set(reused)
    staged_ids = set()
    for staged in row_staged.values():
        staged_ids |= set(staged)
    for staged in reused_staged.values():
        staged_ids |= set(staged)
    # D7: a staged id that is also a lane id is not a refused staged row.
    refused_staged = []
    for text in refused_staged_text:
        for sid in TOKEN_RE.findall(text.upper()):
            if sid in staged_ids and sid not in lane_ids \
                    and sid not in refused_staged:
                refused_staged.append(sid)

    cfg = {
        "freeze": freeze,
        "frozen_sha256": hashlib.sha256(raw).hexdigest(),
        "base": base,
        "access_date": access_date,
        "rows": rows,
        "row_staged": row_staged,
        "row_doc": row_doc,
        "reused": reused,
        "reused_staged": reused_staged,
        "entries": entries,
        "fragments": fragments,
        "terms": terms,
        "refused_staged": sorted(refused_staged),
        "refused_staged_text": refused_staged_text,
        "refused_files": refused_files,
        "counts": parsed_counts,
        "map_path": map_path,
        "map_sha256": map_sha,
        "frozen_legs": frozen_legs,
        "allowed_ids": lane_ids,
        "forbidden_ids": sorted(staged_ids - lane_ids),
        "owned_inplace": owned_inplace,
        "claim_keys": sorted(claim.keys()),
    }
    return cfg


def _row_url_keys(lands_rows, sid):
    """The URL keys a registry row names: raw key UNION document key (D3).

    A page-level Persée transcription in the source cell therefore also carries
    its document's key, and the row's document key meets a page-level citation
    through `_url_keys`.
    """
    row = lands_rows.get(sid)
    if row is None:
        return set()
    cells = row_cells(row)
    if len(cells) <= SOURCE:
        return set()
    return _url_keys(urls_in(cells[SOURCE]))


def _row_has_url(lands_rows, sid, url):
    """True when `url` names a document/URL the row's source cell carries."""
    return bool(_url_keys([url]) & _row_url_keys(lands_rows, sid))


def _gate_admit_row(gate_rows, sid, lands_rows):
    """The Gate admit row for `sid`: joined by document URL first, by id token
    second.  With D3 the first join also reaches a page-level Gate URL that the
    row names only at document level (and a Wayback carrier)."""
    admits = [r for r in gate_rows if is_admit_row(r)]
    keys = _row_url_keys(lands_rows, sid)
    if keys:
        for r in admits:
            if keys & _url_keys(urls_in(r)):
                return r
    for r in admits:
        if re.search(r"\b%s\b" % re.escape(sid), r):
            return r
    return None


def _min_entry_words(mat_base):
    """The smallest corpus/knowledge entry at the claim base, in words (0 when
    the base tree carries none — the ENTRIES leg then has no floor)."""
    best = None
    for rel in tree_files(mat_base, KNOWLEDGE):
        if not rel.endswith(".md"):
            continue
        try:
            text = read_tree(mat_base, rel)
        except Missing:
            continue
        n = len(text.split())
        best = n if best is None else min(best, n)
    return best or 0


def _archive_original(u):
    """The original URL a `web.archive.org/web/<ts>/…` carrier embeds, else None.

    Returned in the carrier's own encoding (`%20` kept): the value is re-parsed
    by `urls_in`, which stops at a raw space, and the registry cell carries the
    percent-encoded form — decoding here would truncate the document path.
    """
    host, path = norm_url(u)
    bare = host[4:] if host.startswith("www.") else host
    if bare != "web.archive.org":
        return None
    m = re.match(r"^/web/\d{8,14}[a-z_]*/(.+)$", path)
    return m.group(1) if m else None


def _evidence(mat, rid):
    """Parse reports/round-75/evidence/<id>.txt at lands (capture-evidence.py
    grammar): the first occurrence of each `name: value` header line wins, the
    stored window comes from `_window`, and the raw lines are kept under `_all`
    so a QUALITY 22 two-request record is still reachable.

    Carrier disclosure (D3): when a fetch/url/final-url line names a
    `web.archive.org` capture, the document the capture carries is appended to
    the parsed value — `fetch: GET <wrapper> (original <url>)` — so a leg that
    intersects `neutral_url_keys(urls_in(ev["fetch"]))` with the row's keys
    still joins the ROW's document (S892: the live URL is challenge-walled and
    only the same-page capture is open).  The stored bytes are untouched; the
    verbatim line stays in `_text`/`_all`.
    """
    try:
        text = read_tree(mat, EVIDENCE_DIR + "/" + rid + ".txt")
    except Missing:
        return None
    out, pairs = {}, []
    for line in text.splitlines():
        m = re.match(r"^([A-Za-z][A-Za-z0-9_-]*):\s*(.*)$", line)
        if m:
            key = m.group(1).lower()
            pairs.append((key, m.group(2)))
            if key not in out:
                out[key] = m.group(2)
    originals = []
    for key in ("fetch", "url", "final-url"):
        value = out.get(key)
        if not value:
            continue
        found = [o for o in (_archive_original(u) for u in urls_in(value)) if o]
        if found:
            found = list(dict.fromkeys(found))
            originals.extend(found)
            out[key] = value + " (original %s)" % " ; ".join(found)
    out["_all"] = pairs
    out["_text"] = text
    out["_original"] = list(dict.fromkeys(originals))
    out["_window"] = _window(text)
    return out


def _window(text):
    """The stored window exactly as capture-evidence.py stores it: the lines
    between the `--- window ---` marker and `--- quote ---`, trailing empty
    lines dropped, joined by newlines (the producer writes ONE line)."""
    lines = text.splitlines()
    start = None
    for i, line in enumerate(lines):
        if line.strip() == "--- window ---":
            start = i + 1
            break
    if start is None:
        return None
    body = []
    for line in lines[start:]:
        if line.strip() == "--- quote ---":
            while body and body[-1] == "":
                body.pop()
            return "\n".join(body)
        body.append(line)
    return None


def _entry_citations(mat, entries, bad):
    """{S-id: {entry paths}} from the `source:` lines of the frozen entries."""
    cited = {}
    for e in entries:
        try:
            text = read_tree(mat, e)
        except Missing:
            bad.append("%s missing (cannot derive used-by)" % e)
            continue
        for sline in source_lines(text):
            for sid in TOKEN_RE.findall(sline):
                cited.setdefault(sid, set()).add(e)
    return cited
