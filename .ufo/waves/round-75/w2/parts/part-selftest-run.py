# --------------------------------------------------------------------------
# selftest -- runner half (owner: ExecSelftestMutants)
#
# Every case builds a fixture repo (part-selftest-fixtures.py), runs THIS
# counter as a subprocess against it, and asserts the exact verdict shape the
# claim needs: the positive tree PASSes 13/13, every mutant is caught on its
# named leg, `lands == base` is REFUSED with a FAIL line, `lands == freeze` is
# GRADED (FROZENCFG green, data legs red), and a missing --lands/--freeze is
# an input error (exit 2).
#
# Scratch (fixtures, the counter's own grading clone via TMPDIR, and this
# runner) lives under $HYAKU_SCRATCH/kotodama-r75 (never /tmp) and is removed
# on exit.  $SHOKUNIN_SCRATCH is honoured as the older spelling the PART A
# docstring still carries; /fast/scratch/hyaku is the operator default.
# --------------------------------------------------------------------------

_STR_LEG_ORDER = ("ENTRIES", "ROWS", "REPOINTED", "GATE", "EVIDENCE",
                  "REJECTS", "GROUND", "CITEDLINES", "CENSUS",
                  "SCRATCHMIRROR", "COLLCHECK", "FROZENCFG", "INDEX")
_STR_TIMEOUT = 600


def _str_scratch():
    """The selftest scratch root: the fixture builder's own root when it is
    present (so both halves agree on one tree), else the env/default chain."""
    helper = globals().get("_selftest_scratch")
    if callable(helper):
        try:
            root = helper()
        except Exception:
            root = None
        if root:
            return root
    base = (os.environ.get("HYAKU_SCRATCH")
            or os.environ.get("SHOKUNIN_SCRATCH")
            or "")
    if base:
        return os.path.join(base, "kotodama-r75")
    fast = "/fast/scratch/hyaku"
    if os.path.isdir(fast) and os.access(fast, os.W_OK):
        return os.path.join(fast, "kotodama-r75")
    return os.path.join(tempfile.gettempdir(), "kotodama-r75")


def _str_tmpdir():
    """This run's own temporary directory inside the scratch root (QUALITY 14:
    never /tmp).  Named by pid so two selftests can run side by side and the
    cleanup can never touch a seat directory or another run's files.  The
    caller creates it; the cleanup only ever removes this exact path."""
    return os.path.join(_str_scratch(), "selftest-tmp-%d" % os.getpid())


def _str_slug(text):
    return re.sub(r"[^A-Za-z0-9._-]+", "-", str(text)).strip("-") or "mutant"


def _str_mutants():
    """MUTANTS normalised to [(name, expected_leg, spec_or_callable), ...].

    The frozen shape is the fixture builder's list of 3-tuples; a mapping
    (r74 shape, with EXPECTED_FAIL beside it) is accepted as well so an
    assembly order mistake cannot silently skip every mutant.
    """
    table = globals().get("MUTANTS")
    if table is None:
        return []
    if isinstance(table, dict):
        expected = globals().get("EXPECTED_FAIL") or {}
        items = [(name, expected.get(name, ""), spec)
                 for name, spec in table.items()]
    else:
        items = list(table)
    rows = []
    for item in items:
        try:
            name, leg, spec = item
        except (TypeError, ValueError):
            rows.append((item, "", None))
            continue
        rows.append((name, leg, spec))
    return rows


def _run_counter(lane, fleet, lands, freeze=None, extra=None, omit_lands=False):
    """Run the assembled counter as a subprocess against one fixture.

    TMPDIR points into the selftest scratch so the counter's own grading clone
    and the fixtures' temp dirs never land in /tmp.  A hang is reported as
    exit 124 rather than killing the whole selftest.
    """
    cmd = [sys.executable, "-B", os.path.abspath(__file__),
           "--root", lane, "--fleet-root", fleet]
    if not omit_lands:
        cmd += ["--lands", lands]
    if freeze:
        cmd += ["--freeze", freeze]
    if extra:
        cmd += list(extra)
    tmp = _str_tmpdir()
    os.makedirs(tmp, exist_ok=True)
    env = dict(os.environ)
    env.setdefault("PYTHONHASHSEED", "0")
    env["TMPDIR"] = tmp
    env.pop("TMP", None)
    env.pop("TEMP", None)
    try:
        return subprocess.run(cmd, capture_output=True, text=True, env=env,
                              cwd=tmp, timeout=_STR_TIMEOUT)
    except subprocess.TimeoutExpired as e:
        out = e.stdout if isinstance(e.stdout, str) else (e.stdout or b"").decode(
            "utf-8", "replace")
        err = e.stderr if isinstance(e.stderr, str) else (e.stderr or b"").decode(
            "utf-8", "replace")
        return subprocess.CompletedProcess(
            cmd, 124, out, err + "\nTIMEOUT after %ds" % _STR_TIMEOUT)


def run_selftest():
    results = []
    dirs = []

    def emit(name, problems, note=""):
        ok = not problems
        detail = note if ok else " | ".join(p.strip() for p in problems if p.strip())
        detail = " ".join(str(detail).split())
        if len(detail) > 280:
            detail = detail[:277] + "..."
        results.append(ok)
        print("CASE %s: %s%s" % (name, "PASS" if ok else "FAIL",
                                 (" -- " + detail) if detail else ""),
              flush=True)
        return ok

    def verdict(r, want_code, want_line, green=(), red=(), stderr_has=None):
        problems = []
        if r.returncode != want_code:
            problems.append("exit %d, want %d" % (r.returncode, want_code))
        if want_line and want_line not in r.stdout:
            problems.append("stdout lacks %r (exit %d)"
                            % (want_line, r.returncode))
        for pl in green:
            if "LEG PASS %s" % pl not in r.stdout:
                problems.append("%s must be green" % pl)
        for nl in red:
            if "LEG FAIL %s" % nl not in r.stdout:
                problems.append("%s must be red" % nl)
        if stderr_has and stderr_has not in r.stderr:
            problems.append("stderr lacks %r" % stderr_has)
        return problems

    build = globals().get("build_fixture")
    if not callable(build):
        emit("fixtures", ["build_fixture is not defined: "
                          "part-selftest-fixtures.py is missing or assembled "
                          "after part-selftest-run.py"])
        print("SELFTEST: 0/1")
        return 1

    def fixture(prefix, mut=None):
        try:
            got = build(prefix, mut)
        except Exception as e:
            return None, "build_fixture(%s) raised %s: %s" % (
                prefix, type(e).__name__, " ".join(str(e).split())[:200])
        if not (isinstance(got, (tuple, list)) and len(got) == 5):
            return None, ("build_fixture(%s) returned %r, want "
                          "(lane, fleet, base, freeze, lands)" % (prefix, got))
        lane, fleet, base, freeze, lands = got
        for d in (lane, fleet):
            if isinstance(d, str) and d and d not in dirs:
                dirs.append(d)
        bad = [v for v in (base, freeze, lands)
               if not (isinstance(v, str) and re.fullmatch(r"[0-9a-f]{40}", v))]
        if bad:
            return None, "build_fixture(%s) returned a non-40-hex commit: %r" % (
                prefix, [base, freeze, lands])
        return (lane, fleet, base, freeze, lands), ""

    try:
        # 1. the mutant table itself: every one of the 13 legs must be
        #    exercised by at least one named mutant, and nobody may expect a
        #    leg that does not exist.
        rows = _str_mutants()
        problems = []
        if not rows:
            problems.append("MUTANTS is empty: no leg is exercised")
        seen = {}
        for name, leg, _spec in rows:
            if not isinstance(name, str) or not name:
                problems.append("a mutant has no name: %r" % (name,))
                continue
            if leg not in _STR_LEG_ORDER:
                problems.append("mutant %s expects unknown leg %r" % (name, leg))
                continue
            seen.setdefault(leg, []).append(name)
        missing = [n for n in _STR_LEG_ORDER if n not in seen]
        if missing:
            problems.append("no mutant exercises: %s" % " ".join(missing))
        emit("mutant-table", problems,
             note="%d mutants over %d/%d legs" % (len(rows), len(seen),
                                                 len(_STR_LEG_ORDER)))

        # 2. the positive fixture: PASS 13/13, every leg green, receipt
        #    stamped with the evaluated and frozen revisions.
        clean, err = fixture("r75st-clean")
        if clean is None:
            emit("clean", [err])
        else:
            lane, fleet, base, freeze, lands = clean
            r = _run_counter(lane, fleet, lands, freeze)
            problems = verdict(r, 0, "ACCEPT-C-75: PASS legs=13/13",
                               green=_STR_LEG_ORDER)
            if "# evaluated revision: %s" % lands not in r.stdout:
                problems.append("receipt does not stamp the evaluated "
                                "revision %s" % lands[:12])
            if "# freeze revision: %s" % freeze not in r.stdout:
                problems.append("receipt does not name the freeze %s"
                                % freeze[:12])
            emit("clean", problems, note="PASS 13/13 at %s" % lands[:12])

        if clean is None:
            # the dependent cases must still be accounted for: a case that
            # cannot run is a failure, never a silently smaller denominator.
            for name in ("lands-eq-base", "freeze-eq-lands", "missing-lands",
                         "missing-freeze"):
                emit(name, ["clean fixture unavailable: %s" % err])
        else:
            lane, fleet, base, freeze, lands = clean

            # 3. do-nothing control (2): lands == the frozen base is REFUSED
            #    (exit 2) and still prints a FAIL line -- never a PASS.
            r = _run_counter(lane, fleet, base, freeze)
            problems = []
            if r.returncode != 2:
                problems.append("exit %d, want 2 (refusal)" % r.returncode)
            if "ACCEPT-C-75: FAIL" not in (r.stdout + r.stderr):
                problems.append("refusal prints no ACCEPT-C-75: FAIL line")
            if "ACCEPT-C-75: PASS" in (r.stdout + r.stderr):
                problems.append("refusal prints a PASS line")
            emit("lands-eq-base", problems, note="refused, FAIL printed")

            # 4. do-nothing control (1): lands == freeze is GRADED -- the data
            #    legs are red, FROZENCFG stays green, exit 1 (not a refusal).
            r = _run_counter(lane, fleet, freeze, freeze)
            problems = verdict(r, 1, "ACCEPT-C-75: FAIL",
                               green=("FROZENCFG",),
                               red=("ENTRIES", "ROWS"))
            if "REFUSED" in r.stderr:
                problems.append("lands==freeze was refused, not graded")
            emit("freeze-eq-lands", problems, note="graded FAIL, FROZENCFG green")

            # 5. an input error, not a verdict: no --lands / no --freeze.
            r = _run_counter(lane, fleet, lands, freeze, omit_lands=True)
            emit("missing-lands", verdict(r, 2, None, stderr_has="--lands"),
                 note="exit 2 naming --lands")

            r = _run_counter(lane, fleet, lands, None)
            emit("missing-freeze", verdict(r, 2, None, stderr_has="--freeze"),
                 note="exit 2 naming --freeze")

        # 6. a lands commit after the freeze that lands no claim-C artefact
        #    must fail the data legs while the frozen config stays green.
        nodata, err = fixture("r75st-nodata", {"no_data": True})
        if nodata is None:
            emit("no-data", [err])
        else:
            lane, fleet, _b, freeze, lands = nodata
            r = _run_counter(lane, fleet, lands, freeze)
            problems = verdict(r, 1, "ACCEPT-C-75: FAIL",
                               green=("FROZENCFG",),
                               red=("ENTRIES", "ROWS"))
            emit("no-data", problems, note="data legs red, FROZENCFG green")

        # 7. one case per mutant: exit 1 with the expected leg red.
        for name, leg, spec in rows:
            label = "mutant:%s" % name
            if not isinstance(name, str) or not name:
                emit(label, ["unnamed mutant: %r" % (name,)])
                continue
            try:
                mut = spec() if callable(spec) else spec
            except Exception as e:
                emit(label, ["mutant spec raised %s: %s"
                             % (type(e).__name__, " ".join(str(e).split())[:150])])
                continue
            if mut is not None and not isinstance(mut, dict):
                emit(label, ["mutant spec is %s, want dict" % type(mut).__name__])
                continue
            tup, err = fixture("r75st-" + _str_slug(name), mut)
            if tup is None:
                emit(label, [err])
                continue
            lane, fleet, _b, freeze, lands = tup
            r = _run_counter(lane, fleet, lands, freeze)
            problems = verdict(r, 1, "ACCEPT-C-75: FAIL")
            if leg in _STR_LEG_ORDER and "LEG FAIL %s" % leg not in r.stdout:
                found = [n for n in _STR_LEG_ORDER
                         if "LEG FAIL %s" % n in r.stdout]
                problems.append("expected LEG FAIL %s, got [%s] (exit %d)"
                                % (leg, " ".join(found) or "none",
                                   r.returncode))
            emit(label, problems, note="LEG FAIL %s" % leg)
    finally:
        # Remove exactly what this run created: the fixtures the builder
        # returned, an emptied per-fixture parent, and this run's own TMPDIR.
        # Never a shared parent and never a seat directory by name.
        root = _str_scratch()
        for d in dirs:
            shutil.rmtree(d, ignore_errors=True)
        # A builder that keeps lane and fleet inside one per-fixture directory
        # leaves that directory behind (the fixture owns it, both paths point
        # into it); remove it only when it sits strictly below the scratch root
        # and every fixture path lives inside it.
        by_parent = {}
        for d in dirs:
            by_parent.setdefault(os.path.dirname(d), []).append(d)
        for p, kids in by_parent.items():
            if p == root or not p.startswith(root + os.sep):
                continue
            if all(d.startswith(p + os.sep) for d in kids):
                shutil.rmtree(p, ignore_errors=True)
        shutil.rmtree(_str_tmpdir(), ignore_errors=True)

    total = len(results)
    passed = sum(1 for ok in results if ok)
    print("SELFTEST: %d/%d" % (passed, total))
    return 0 if passed == total else 1
