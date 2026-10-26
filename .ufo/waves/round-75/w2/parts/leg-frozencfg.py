# leg-frozencfg.py — round-75 claim C, leg FROZENCFG (owner: ExecLegFrozenCfg).
# Part of the assembled reports/round-75/accept-c.py (CFG-CONTRACT.md order 3).
# Function definitions only; only PART A imports are used.
#
# Frozen leg text (reports/round-75/claims.json, claims[id=C].legs[11]) — the rule:
#   "FROZENCFG: row set, entry paths, fragments, reject counts and every constant
#    are read from `git show <freeze>:reports/round-75/claims.json`; the
#    by-document map is read from `git show <freeze>:<map.path>` whose sha256
#    equals map.sha256; never from the graded tree; <freeze> is an ancestor of
#    <lands> on its first-parent chain (<lands> == <freeze> is graded, not
#    refused); claims.json at <lands> is byte-identical to the freeze blob"
#
# Readings of the ambiguous parts (each marked at the check it governs):
#
# R1 "read from the freeze" is proved by re-derivation, not by assertion: every
#    constant in ctx["cfg"] is re-read from the frozen blob by this leg and
#    compared with the value the loader handed it.  Because the frozen bytes
#    also have to be the bytes at <lands> (below), a cfg built from the graded
#    tree cannot pass: an edited graded tree both breaks byte identity and
#    diverges from the frozen constants.
# R2 "<freeze> is an ancestor of <lands> on its first-parent chain" = membership
#    in `git rev-list --first-parent <lands>`.  A freeze reachable only through
#    a merge side branch FAILS with that reason (it is not merely "not an
#    ancestor").  <lands> == <freeze> is graded: the freeze is the first element
#    of its own first-parent chain, so the check passes and no special case is
#    needed.
# R3 "<lands> == <freeze> is graded, not refused" — this leg never raises for
#    that case; every byte comparison below degenerates to comparing the freeze
#    blob with itself, which is why the do-nothing control prints FROZENCFG
#    green while the data legs are red.
# R4 "claims.json at <lands> is byte-identical to the freeze blob" is a byte
#    comparison (not a hash comparison): two different byte strings that a
#    hash collision would map together are not "byte-identical".
# R5 "the counter's own sha256 equals sha256sum of the committed
#    reports/round-75/accept-c.py at <lands> when that path exists" (wave-2
#    dispatch, H1 self-pin): conditional on the path existing, so a landing
#    that never commits the counter is not failed by this limb; at
#    <lands> == <freeze> the limb reduces to "the bytes at the freeze are the
#    bytes of the counter that is grading", i.e. the freeze-pinned counter is
#    the one running.  The path is derived from PART A's ROUND, never
#    hardcoded.
# R6 ledger (claim Ca's pin, per the wave-2 dispatch): the ledger path is read
#    from the frozen config (the claim that declares a `ledger`), and its bytes
#    at <lands> must equal its bytes at <freeze>.  Claim Ca's own FROZENCFG leg
#    pins the same bytes, so this cannot fail a combined tree that grades green;
#    it is kept here because the ledger is part of the round's frozen constant
#    surface, and because a C grader run at a tree where the ledger was edited
#    must not report a frozen configuration.
# R7 "reject counts" — the frozen `counts` object is an INTEGER surface
#    (adopted, path_present, refused, total_staged_files).  Both sides are
#    reduced to their integer keys (key -> int), so int-vs-str rendering and a
#    prose sibling that lands inside the object are not tests, while a drifted
#    or dropped count is.  When the freeze declares no counts there is no
#    frozen referent, so no failure is raised (CFG-CONTRACT allows {}).
# R8 "row set ... every constant" — a frozen row set, entry list, fragment
#    list or term list that is EMPTY makes the data legs vacuous, so empty
#    frozen lists are a FROZENCFG failure (carried from the round-74 leg).
# R9 the map must be readable JSON as well as hash-pinned: an unparseable map
#    is not a by-document map that any leg could read (COLLCHECK owns its
#    records; this leg owns only that it is the frozen, readable blob).


def _frozencfg_ids(value):
    """Every S-id token carried by a frozen `staged`/prose value."""
    if value is None:
        return []
    if isinstance(value, (list, tuple)):
        text = " ".join(str(x) for x in value)
    elif isinstance(value, dict):
        text = " ".join(str(x) for x in value.values())
    else:
        text = str(value)
    return dedupe(TOKEN_RE.findall(text.upper()))


def _frozencfg_paths(value):
    """Repo-relative paths from a frozen `entries`-shaped value."""
    out = []

    def take(v):
        if isinstance(v, str):
            s = v.strip()
            if s:
                out.append(s[2:] if s.startswith("./") else s)
        elif isinstance(v, (list, tuple)):
            for item in v:
                take(item)
        elif isinstance(v, dict):
            for key in ("path", "paths", "entries", "amendments", "canonical",
                        "admitted"):
                if key in v:
                    take(v[key])

    take(value)
    return dedupe(out)


def _frozencfg_strings(value):
    """The frozen list of strings (paths, fragments, terms, file specs)."""
    if value is None:
        return []
    if isinstance(value, (list, tuple)):
        return [str(x).strip() for x in value]
    return [str(value).strip()]


def _frozencfg_counts(value):
    """A rejects.counts object as {key: int-string} (integer keys only).

    The frozen `counts` is an integer surface (adopted, path_present, refused,
    total_staged_files); a prose sibling that a later freeze puts *inside* the
    object (or a non-numeric value) is not a count the loader can carry, so it
    is dropped on both sides instead of being stringified into a false red.
    """
    if not isinstance(value, dict):
        return {}
    out = {}
    for k, v in value.items():
        try:
            out[str(k)] = str(int(v))
        except (TypeError, ValueError):
            continue
    return out


def _frozencfg_blob(root, rev, path):
    """The committed bytes of `path` at `rev`, or None when it is not there."""
    r = git_bytes(root, "show", "%s:%s" % (rev, path))
    if r.returncode != 0:
        return None
    return r.stdout


def _frozencfg_ledger_path(doc):
    """The ledger path the frozen round config pins (claim Ca declares it)."""
    for c in doc.get("claims") or []:
        if isinstance(c, dict):
            p = c.get("ledger")
            if isinstance(p, str) and p.strip():
                return p.strip()
    p = doc.get("ledger")
    return p.strip() if isinstance(p, str) and p.strip() else ""


def _frozencfg_rows(spec):
    """[(lane id, {staged ids})] from a frozen row_set/reused_rows list."""
    out = []
    for item in spec or []:
        if not isinstance(item, dict):
            continue
        rid = str(item.get("id", "")).strip().upper()
        out.append((rid, set(_frozencfg_ids(item.get("staged")))))
    return out


def _frozencfg_staged_map(value):
    """{lane id -> set(staged ids)} from the cfg row_staged/reused_staged dict."""
    out = {}
    if not isinstance(value, dict):
        return out
    for k, v in value.items():
        out[str(k).strip().upper()] = set(_frozencfg_ids(v))
    return out


def _frozencfg_compare(cfg, doc, claim, raw_text, bad):
    """R1: every cfg constant re-read from the frozen claims.json claims[C]."""
    note = bad.append

    # base: the top-level frozen base (a claim-local base is accepted as a
    # fallback exactly as the loader does).
    want_base = str(doc.get("base") or claim.get("base") or "").strip().lower()
    got_base = str(cfg.get("base") or "").strip().lower()
    if got_base != want_base:
        note("cfg base %s is not the frozen base %s"
             % (got_base[:12] or "-", want_base[:12] or "-"))

    # row set (order is part of the frozen constant) and the staged lists.
    rows = _frozencfg_rows(claim.get("row_set"))
    want_rows = [rid for rid, _staged in rows]
    got_rows = [str(x).strip().upper() for x in (cfg.get("rows") or [])]
    if got_rows != want_rows:
        note("cfg row set %s is not the frozen row set %s"
             % (" ".join(got_rows) or "-", " ".join(want_rows) or "-"))
    want_staged = {}
    for rid, staged in rows:
        want_staged.setdefault(rid, set()).update(staged)
    got_staged = _frozencfg_staged_map(cfg.get("row_staged"))
    if got_staged != want_staged:
        for rid in sorted(set(want_staged) | set(got_staged)):
            if got_staged.get(rid, set()) != want_staged.get(rid, set()):
                note("cfg staged ids for %s are %s, the frozen row declares %s"
                     % (rid, " ".join(sorted(got_staged.get(rid, set()))) or "-",
                        " ".join(sorted(want_staged.get(rid, set()))) or "-"))
    reused = _frozencfg_rows(claim.get("reused_rows"))
    want_reused = [rid for rid, _staged in reused]
    got_reused = [str(x).strip().upper() for x in (cfg.get("reused") or [])]
    if got_reused != want_reused:
        note("cfg reused rows %s are not the frozen reused_rows %s"
             % (" ".join(got_reused) or "-", " ".join(want_reused) or "-"))
    want_reused_staged = {}
    for rid, staged in reused:
        want_reused_staged.setdefault(rid, set()).update(staged)
    got_reused_staged = _frozencfg_staged_map(cfg.get("reused_staged"))
    if got_reused_staged != want_reused_staged:
        note("cfg reused_staged %s is not the frozen reused mapping %s"
             % (sorted(got_reused_staged) or "-", sorted(want_reused_staged) or "-"))

    # entry paths and the ground lists (sets: the freeze declares membership).
    want_entries = set(_frozencfg_paths(claim.get("entries")))
    got_entries = set(_frozencfg_paths(cfg.get("entries")))
    if got_entries != want_entries:
        note("cfg entry paths [%s] are not the frozen entry paths [%s]"
             % (", ".join(sorted(got_entries)) or "-",
                ", ".join(sorted(want_entries)) or "-"))
    ground = claim.get("ground") if isinstance(claim.get("ground"), dict) else {}
    want_frag = set(_frozencfg_strings(ground.get("fragments")))
    got_frag = set(_frozencfg_strings(cfg.get("fragments")))
    if got_frag != want_frag:
        note("cfg ground fragments [%s] are not the frozen fragments [%s]"
             % (", ".join(sorted(got_frag)) or "-",
                ", ".join(sorted(want_frag)) or "-"))
    terms_src = ground.get("terms")
    if terms_src is None:
        terms_src = ground.get("cjk_terms")
    want_terms = set(_frozencfg_strings(terms_src))
    got_terms = set(_frozencfg_strings(cfg.get("terms")))
    if got_terms != want_terms:
        note("cfg ground terms [%s] are not the frozen terms [%s]"
             % (", ".join(sorted(got_terms)) or "-",
                ", ".join(sorted(want_terms)) or "-"))

    # rejects: the refused staged ids, the refused file specs and (when the
    # freeze declares them, R7) the counts.
    rejects = claim.get("rejects") if isinstance(claim.get("rejects"), dict) else {}
    prose = rejects.get("refused_staged_not_appended")
    if prose is None:
        prose = rejects.get("refused_staged")
    prose_ids = set(_frozencfg_ids(prose))
    got_refused = set(_frozencfg_ids(cfg.get("refused_staged")))
    want_allowed = set(want_rows) | set(want_reused)
    if got_refused - prose_ids:
        note("cfg refused_staged %s names ids the frozen rejects prose does not"
             % " ".join(sorted(got_refused - prose_ids)))
    if prose_ids - got_refused - want_allowed:
        note("the frozen rejects prose refuses %s but cfg records %s"
             % (" ".join(sorted(prose_ids - got_refused - want_allowed)),
                " ".join(sorted(got_refused)) or "-"))
    files_src = rejects.get("refused_files_pending_triage")
    if files_src is None:
        files_src = rejects.get("refused_files")
    want_files = set(_frozencfg_strings(files_src))
    got_files = set(_frozencfg_strings(cfg.get("refused_files")))
    if got_files != want_files:
        note("cfg refused file specs [%s] are not the frozen [%s]"
             % ("; ".join(sorted(got_files)) or "-",
                "; ".join(sorted(want_files)) or "-"))
    if "counts" in rejects:
        want_counts = _frozencfg_counts(rejects.get("counts"))
        got_counts = _frozencfg_counts(cfg.get("counts"))
        if got_counts != want_counts:
            note("cfg reject counts %s are not the frozen counts %s"
                 % (sorted(got_counts.items()), sorted(want_counts.items())))

    # the by-document map path and its pin.
    map_spec = claim.get("map") if isinstance(claim.get("map"), dict) else {}
    want_map_path = str(map_spec.get("path") or "").strip()
    want_map_sha = str(map_spec.get("sha256") or "").strip().lower()
    got_map_path = str(cfg.get("map_path") or "").strip()
    got_map_sha = str(cfg.get("map_sha256") or "").strip().lower()
    if got_map_path != want_map_path:
        note("cfg map.path %r is not the frozen map.path %r"
             % (got_map_path, want_map_path))
    else:
        if not got_map_path or got_map_path.startswith("/") or \
                ".." in got_map_path.split("/"):
            note("the frozen map.path %r is not a relative repo path"
                 % got_map_path)
    if got_map_sha != want_map_sha:
        note("cfg map.sha256 %s is not the frozen map.sha256 %s"
             % (got_map_sha[:16] or "-", want_map_sha[:16] or "-"))
    elif not got_map_sha:
        note("the frozen map.sha256 is empty: the by-document map is "
             "uncheckable at this freeze")

    # the frozen leg list (its length and order are the leg-set contract).
    want_legs = [str(x).split(":", 1)[0].strip().upper()
                 for x in (claim.get("legs") or [])]
    got_legs = [str(x).strip().upper() for x in (cfg.get("frozen_legs") or [])]
    if got_legs != want_legs:
        note("cfg leg list %s is not the frozen leg list %s"
             % (" ".join(got_legs) or "-", " ".join(want_legs) or "-"))

    # the frozen claim's key set (claim_keys is a frozen constant surface) —
    # either the claim object's keys or the round document's keys, r74's
    # `sorted(claim.keys())` being the loader's declared shape.
    want_keys = sorted(str(k) for k in claim.keys())
    got_keys = [str(k) for k in (cfg.get("claim_keys") or [])]
    if got_keys != want_keys and got_keys != sorted(str(k) for k in doc.keys()):
        note("cfg claim_keys %s are not the frozen claim keys %s"
             % (" ".join(got_keys) or "-", " ".join(want_keys) or "-"))

    # row_doc / owned_inplace when the loader exposes them (CFG-CONTRACT cfg):
    # each document string must come from the frozen row_set document text, and
    # the owned_inplace list must be the frozen claim's list.
    row_doc = cfg.get("row_doc")
    if isinstance(row_doc, dict):
        for item in claim.get("row_set") or []:
            if not isinstance(item, dict):
                continue
            rid = str(item.get("id", "")).strip().upper()
            want_doc = str(item.get("document") or "")
            got_doc = str(row_doc.get(rid) or "").strip()
            if want_doc and (not got_doc or not want_doc.startswith(got_doc)):
                note("cfg row_doc[%s] %r is not the frozen document %r"
                     % (rid, got_doc[:60], want_doc[:60]))
    if "owned_inplace" in cfg:
        want_own = claim.get("owned_inplace") or []
        got_own = cfg.get("owned_inplace") or []
        if json.dumps(got_own, sort_keys=True) != json.dumps(want_own, sort_keys=True):
            note("cfg owned_inplace %r is not the frozen owned_inplace %r"
                 % (got_own, want_own))

    # the access date: declared at the freeze, or derived from frozen prose
    # (PART A docstring) — in which case it must occur in the frozen bytes.
    want_date = str(claim.get("access_date") or doc.get("access_date")
                    or "").strip()
    got_date = str(cfg.get("access_date") or "").strip()
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", got_date):
        note("cfg access_date %r is not a frozen YYYY-MM-DD date" % got_date)
    elif want_date and want_date != got_date:
        note("cfg access_date %s is not the frozen access_date %s"
             % (got_date, want_date))
    elif not want_date and got_date not in raw_text:
        note("cfg access_date %s does not occur in the frozen claims.json"
             % got_date)

    # the id namespace split derived from the frozen rows.
    allowed = set(str(x).strip().upper() for x in (cfg.get("allowed_ids") or []))
    if allowed != want_allowed:
        note("cfg allowed ids %s are not the frozen lane ids %s"
             % (" ".join(sorted(allowed)) or "-",
                " ".join(sorted(want_allowed)) or "-"))
    staged_all = set()
    for staged in want_staged.values():
        staged_all |= staged
    for staged in want_reused_staged.values():
        staged_all |= staged
    want_forbidden = sorted(staged_all - want_allowed)
    got_forbidden = sorted(str(x).strip().upper()
                           for x in (cfg.get("forbidden_ids") or []))
    if got_forbidden != want_forbidden:
        note("cfg forbidden ids %s are not the frozen staged ids %s"
             % (" ".join(got_forbidden) or "-",
                " ".join(want_forbidden) or "-"))

    # R8: empty frozen lists would make the data legs vacuous.
    if not want_rows:
        note("the frozen row set is empty")
    if not want_entries:
        note("the frozen entry list is empty")
    if not want_frag:
        note("the frozen ground fragments are empty")
    if not want_terms:
        note("the frozen ground terms are empty")


def _frozencfg_detail(bad, summary):
    """First detail line <= 300 characters; reasons first, then the summary."""
    if bad:
        head = str(bad[0])
        if len(head) > 300:
            head = head[:297] + "..."
        return "\n".join([head] + ["  - " + str(r) for r in bad[1:]] + summary)
    return "\n".join(summary)


def leg_frozencfg(ctx):
    """FROZENCFG: constants from the freeze blob only, map pinned by sha256,
    freeze on lands' first-parent chain, claims.json at lands frozen-identical."""
    root = ctx.get("root") or ""
    lands = str(ctx.get("lands") or "").strip().lower()
    cfg = ctx.get("cfg") or {}
    bad = []

    required = ("freeze", "frozen_sha256", "base", "access_date", "rows",
                "row_staged", "entries", "fragments", "terms",
                "refused_staged", "refused_files", "counts", "map_path",
                "map_sha256", "frozen_legs", "allowed_ids", "forbidden_ids",
                "claim_keys")
    for key in required:
        if key not in cfg:
            bad.append("cfg lacks the frozen constant %r (CFG-CONTRACT cfg)" % key)

    freeze = str(cfg.get("freeze") or "").strip().lower()
    hex40 = re.compile(r"[0-9a-f]{40}")
    if not hex40.fullmatch(freeze):
        bad.append("cfg freeze %r is not a 40-hex revision" % freeze)
    if not hex40.fullmatch(lands):
        bad.append("lands %r is not a 40-hex revision" % lands)
    valid = hex40.fullmatch(freeze) and hex40.fullmatch(lands)

    # R2: <freeze> on <lands>' first-parent chain.  R3: lands == freeze is
    # graded — the freeze heads its own first-parent chain, no special case.
    same_commit = bool(valid) and freeze == lands
    on_chain = False
    if valid:
        rev = git(root, "rev-list", "--first-parent", lands)
        if rev.returncode != 0:
            bad.append("cannot read lands' first-parent chain: %s"
                       % (rev.stderr or "").strip()[:120])
        else:
            chain = rev.stdout.split()
            on_chain = freeze in chain
            if not on_chain:
                if is_ancestor(root, freeze, lands):
                    bad.append("freeze %s is reachable from lands %s but not on "
                               "its first-parent chain (merge-side freeze)"
                               % (freeze[:12], lands[:12]))
                else:
                    bad.append("freeze %s is not an ancestor of lands %s"
                               % (freeze[:12], lands[:12]))

    # the frozen claims blob: the ONLY source of every constant.
    frozen_raw = None
    doc = None
    claims_state = "missing"
    if hex40.fullmatch(freeze):
        frozen_raw = _frozencfg_blob(root, freeze, CLAIMS)
        if frozen_raw is None:
            bad.append("cannot read %s at freeze %s" % (CLAIMS, freeze[:12]))
        else:
            sha = hashlib.sha256(frozen_raw).hexdigest()
            if sha != str(cfg.get("frozen_sha256") or "").strip().lower():
                bad.append("%s at freeze hashes to %s, cfg says %s"
                           % (CLAIMS, sha[:16],
                              str(cfg.get("frozen_sha256") or "-")[:16]))
            try:
                doc = json.loads(frozen_raw.decode("utf-8"))
            except (ValueError, UnicodeDecodeError) as exc:
                bad.append("%s at freeze is not readable JSON: %s"
                           % (CLAIMS, str(exc)[:120]))
            if not isinstance(doc, dict):
                bad.append("%s at freeze is not a JSON object" % CLAIMS)
                doc = None

    claim = None
    if doc is not None:
        for c in doc.get("claims") or []:
            if isinstance(c, dict) and str(c.get("id", "")).upper() == "C":
                claim = c
                break
        if claim is None:
            bad.append("%s at freeze carries no claim with id C" % CLAIMS)
        else:
            _frozencfg_compare(cfg, doc, claim, frozen_raw.decode("utf-8", "replace"),
                               bad)

    # R4: claims.json at <lands> is byte-identical to the freeze blob.
    if frozen_raw is not None and hex40.fullmatch(lands):
        lands_raw = _frozencfg_blob(root, lands, CLAIMS)
        if lands_raw is None:
            bad.append("%s is not committed at lands %s" % (CLAIMS, lands[:12]))
        elif lands_raw != frozen_raw:
            claims_state = "differs"
            bad.append("%s at lands %s differs from the freeze blob "
                       "(counter config edited in the graded tree)"
                       % (CLAIMS, lands[:12]))
        else:
            claims_state = "frozen-bytes"

    # the by-document map: pinned at the freeze, unchanged at lands (R9).
    map_path = str(cfg.get("map_path") or "").strip()
    map_sha = str(cfg.get("map_sha256") or "").strip().lower()
    map_state = "nocheck"
    frozen_map = None
    if hex40.fullmatch(freeze) and map_path:
        frozen_map = _frozencfg_blob(root, freeze, map_path)
        if frozen_map is None:
            map_state = "missing"
            bad.append("the by-document map %s is not committed at freeze %s"
                       % (map_path, freeze[:12]))
        else:
            sha = hashlib.sha256(frozen_map).hexdigest()
            map_state = "sha256-match"
            if map_sha:
                if sha != map_sha:
                    map_state = "sha256-drift"
                    bad.append("the map %s at freeze hashes to %s, the frozen "
                               "map.sha256 is %s"
                               % (map_path, sha[:16], map_sha[:16]))
            try:
                json.loads(frozen_map.decode("utf-8"))
            except (ValueError, UnicodeDecodeError) as exc:
                map_state += ",unparseable"
                bad.append("the map %s at freeze is not readable JSON: %s"
                           % (map_path, str(exc)[:120]))
            if hex40.fullmatch(lands):
                lands_map = _frozencfg_blob(root, lands, map_path)
                if lands_map is None:
                    map_state += ",lands-missing"
                    bad.append("the by-document map %s is not committed at "
                               "lands %s" % (map_path, lands[:12]))
                elif lands_map != frozen_map:
                    map_state += ",lands-differs"
                    bad.append("the map %s at lands %s differs from the freeze "
                               "blob" % (map_path, lands[:12]))

    # R6: the ledger pin (claim Ca's frozen path) — same bytes at lands.
    ledger_path = _frozencfg_ledger_path(doc) if isinstance(doc, dict) else ""
    ledger_state = "no-pin"
    if ledger_path and hex40.fullmatch(freeze) and hex40.fullmatch(lands):
        frozen_ledger = _frozencfg_blob(root, freeze, ledger_path)
        if frozen_ledger is None:
            ledger_state = "missing-at-freeze"
            bad.append("the frozen ledger %s is not committed at freeze %s"
                       % (ledger_path, freeze[:12]))
        else:
            lands_ledger = _frozencfg_blob(root, lands, ledger_path)
            if lands_ledger is None:
                ledger_state = "missing-at-lands"
                bad.append("the frozen ledger %s is not committed at lands %s"
                           % (ledger_path, lands[:12]))
            elif lands_ledger != frozen_ledger:
                ledger_state = "differs"
                bad.append("the ledger %s at lands %s differs from the freeze "
                           "blob" % (ledger_path, lands[:12]))
            else:
                ledger_state = "frozen-bytes"

    # R5: the counter's own sha256 against the committed counter at lands.
    counter_path = "reports/round-%d/accept-c.py" % ROUND
    counter_state = "absent"
    if hex40.fullmatch(lands):
        committed = _frozencfg_blob(root, lands, counter_path)
        if committed is not None:
            sha = hashlib.sha256(committed).hexdigest()
            mine = counter_sha256()
            if sha != mine:
                counter_state = "mismatch"
                bad.append("the counter's own sha256 %s is not %s's committed "
                           "%s (%s), so this run is not the frozen counter"
                           % (mine[:16], lands[:12], counter_path, sha[:16]))
            else:
                counter_state = "self-pinned"

    # the frozen claim base is a STRICT ancestor of lands (lands == base is the
    # counter's own refusal; an ancestor test that also accepted equality would
    # silently grade a tree that never landed anything).
    base = str(cfg.get("base") or "").strip().lower()
    if hex40.fullmatch(base) and hex40.fullmatch(lands):
        if not is_ancestor(root, base, lands):
            bad.append("the frozen claim base %s is not a strict ancestor of "
                       "lands %s" % (base[:12], lands[:12]))

    summary = [
        ("freeze %s: constants from git show %s:%s (sha256 %s); rows %s; "
         "entries %d; fragments %d; terms %d; refused %s; access %s"
         % (freeze[:12] or "-", freeze[:12] or "-", CLAIMS,
            str(cfg.get("frozen_sha256") or "-")[:16],
            " ".join(str(x) for x in (cfg.get("rows") or [])) or "-",
            len(cfg.get("entries") or []), len(cfg.get("fragments") or []),
            len(cfg.get("terms") or []),
            " ".join(str(x) for x in (cfg.get("refused_staged") or [])) or "-",
            cfg.get("access_date") or "-")),
        ("  lands %s: lands==freeze=%s first-parent-chain=%s claims@lands=%s "
         "map=%s(%s) ledger=%s counter=%s"
         % (lands[:12] or "-", "yes" if same_commit else "no",
            "yes" if on_chain else "no", claims_state,
            map_path or "-", map_state, ledger_state, counter_state)),
    ]
    return leg("FROZENCFG", not bad, _frozencfg_detail(bad, summary))
