# ----------------------------------------------------------- part-main.py ---
# owner: ExecCtrCfgMain.  LEGS / run_legs / print_receipt / refuse / main and
# the `__main__` guard.  Round-74 provenance: `.ufo/waves/round-74/counters/
# accept-c.py` lines 1832-1990 (main) and its LEGS/run_legs/print_receipt.
#
# Round-75 deltas (each from a w1 finding or from the frozen claim text):
#  M1 `<lands> == <base>` is REFUSED (exit 2) and still prints
#     `ACCEPT-C-75: FAIL legs=0/13 (refused: ...)`: the do-nothing control at
#     the claim base is never a graded PASS.  A claim base that is not an
#     ancestor of <lands> at all is refused for the same reason (the graded
#     revision is not descended from the claim's before-state).
#  M2 `<lands> == <freeze>` is GRADED, not refused: the frozen claim text says
#     "`<lands> == <freeze>` is graded, not refused", so the data legs go red
#     and FROZENCFG stays green on the frozen tree (control (1) of the
#     do-nothing receipt).
#  M3 LEGCOUNT against the frozen `legs[]` list in claims.json order; a frozen
#     list that is absent, shorter, longer or differently spelled is a refusal
#     (exit 2), never a partial grade.
#  M4 every clone/materialization lives under the scratch root: `--work` or
#     `$HYAKU_SCRATCH/kotodama-r75/counter` or
#     `/fast/scratch/hyaku/kotodama-r75/counter`; a system temporary directory
#     is refused (QUALITY 14 / prompt §7.4) and the per-run directory is
#     removed on exit.
#  M5 the receipt header carries the round-75 fields (counter sha256 (self),
#     stamped/evaluated/measured, tree, base, freeze, config sha256, frozen
#     legs/map, materialized, lane worktree HEAD disclosure, access date,
#     adopted rows with their staged ids, entries).
#  M6 `--selftest` calls `run_selftest()`, which the selftest parts define;
#     when those parts are not assembled the counter says so instead of
#     raising NameError.
#
# ASSEMBLY: `part-selftest-fixtures.py` and `part-selftest-run.py` must be
# concatenated immediately BEFORE the `__main__` guard below, so `run_selftest`
# exists before the guard runs (CFG-CONTRACT item 5).  The guard is deliberately
# the last three lines of the assembled counter.

LEGS = (
    ("ENTRIES", leg_entries),
    ("ROWS", leg_rows),
    ("REPOINTED", leg_repointed),
    ("GATE", leg_gate),
    ("EVIDENCE", leg_evidence),
    ("REJECTS", leg_rejects),
    ("GROUND", leg_ground),
    ("CITEDLINES", leg_citedlines),
    ("CENSUS", leg_census),
    ("SCRATCHMIRROR", leg_scratch_mirror),
    ("COLLCHECK", leg_collcheck),
    ("FROZENCFG", leg_frozencfg),
    ("INDEX", leg_index),
)


def run_legs(ctx):
    """Run every leg in frozen order; one leg's failure never stops the rest.

    A leg that raises is a red leg with a one-line reason, never a traceback:
    `Missing` is the materialization telling the leg a path is absent, and the
    rest is any defect (a KeyError from a shape the leg expected included) that
    must be visible in the receipt rather than fatal to the run.
    """
    results = []
    for name, fn in LEGS:
        try:
            ok = fn(ctx)
        except Missing as e:
            ok = leg(name, False, "missing at lands: %s" % e)
        except (OSError, RuntimeError, ValueError, TypeError,
                KeyError, AttributeError, subprocess.SubprocessError) as e:
            ok = leg(name, False, "%s: %s" % (type(e).__name__, e))
        results.append((name, bool(ok)))
    passed = sum(1 for _n, ok in results if ok)
    return passed, len(results), results


def print_receipt(root, lands, mat, cfg, how):
    """The receipt header (PART A docstring; tools/check-receipt-seq.py
    grammar): stamped == evaluated == measured == <lands>, the tree of that
    revision, the claim base, the freeze the constants came from, the frozen
    legs and map, where the graded bytes were materialized, and the lane
    worktree HEAD as a disclosure only (never graded)."""
    tree = git(root, "rev-parse", "%s^{tree}" % lands).stdout.strip()
    head = git(root, "rev-parse", "HEAD").stdout.strip()
    print("# round-75 acceptance counter — claim C "
          "(shokuknow narrative-structure-frameworks assimilation)")
    print("# counter sha256 (self): %s" % counter_sha256())
    print("# stamped revision: %s" % lands)
    print("# evaluated revision: %s" % lands)
    print("# measured revision (lane main): %s" % lands)
    print("# tree: %s" % tree)
    print("# base revision: %s" % cfg["base"])
    print("# freeze revision: %s" % cfg["freeze"])
    print("# config sha256 (frozen claims.json): %s" % cfg["frozen_sha256"])
    print("# config source: git show %s:%s (never the graded tree)"
          % (cfg["freeze"], CLAIMS))
    print("# frozen legs: %d (%s)" % (len(cfg["frozen_legs"]),
                                      ",".join(cfg["frozen_legs"])))
    print("# frozen map: %s sha256=%s"
          % (cfg["map_path"], cfg["map_sha256"]))
    print("# materialized: %s at %s" % (how, mat))
    print("# worktree graded: no (leg bytes read only from the checkout and the "
          "git-archive base tree)")
    print("# lane worktree HEAD (disclosure only): %s" % head)
    print("# access date: %s" % cfg["access_date"])
    print("# adopted rows: %s (staged %s)"
          % (" ".join(cfg["rows"]),
             " ".join("/".join(cfg["row_staged"][r]) for r in cfg["rows"])))
    print("# reused rows: %s (staged %s)"
          % (" ".join(cfg["reused"]) or "-",
             " ".join("/".join(cfg["reused_staged"][r]) for r in cfg["reused"])
             or "-"))
    print("# entries: %s" % " ; ".join(cfg["entries"]))
    print()


def refuse(msg):
    """Refuse to grade (H1/M1/M3/M4).  The verdict line is a FAIL, never a
    PASS: no leg ran, and the exit code (2) marks the refusal as an input
    error, not a graded verdict."""
    print("REFUSED: %s" % msg, file=sys.stderr)
    print("ACCEPT-C-75: FAIL legs=0/%d (refused: %s)"
          % (len(LEGS), msg.splitlines()[0]))
    return 2


def _scratch_root(args):
    """M4: the scratch root for every clone, materialization and temp dir.

    `--work` wins; then `$HYAKU_SCRATCH/kotodama-r75/counter`; then the
    operator's scratch tree.  Never the system temporary directory.
    """
    work = (getattr(args, "work", None) or "").strip()
    if work:
        return os.path.abspath(work)
    env = (os.environ.get("HYAKU_SCRATCH") or "").strip()
    if env:
        return os.path.join(os.path.abspath(env), "kotodama-r75", "counter")
    return "/fast/scratch/hyaku/kotodama-r75/counter"


def _forbidden_scratch(path):
    """True when `path` is (inside) the system temporary directory."""
    p = os.path.abspath(path)
    banned = {os.path.abspath("/tmp"), os.path.abspath(tempfile.gettempdir())}
    for b in banned:
        if p == b or p.startswith(b + os.sep):
            return True
    return False


def main(argv=None):
    ap = argparse.ArgumentParser(
        description="round-75 coverage counter (claim C)")
    ap.add_argument("--root", default=".", help="lane repository root")
    ap.add_argument("--lands", default=None,
                    help="required lands revision (40-hex commit)")
    ap.add_argument("--freeze", default=None,
                    help="required freeze revision (40-hex commit; graded when "
                         "it equals --lands, refused only for the claim base)")
    ap.add_argument("--fleet-root", default=None,
                    help="fleet root (default: the lane's parent directory)")
    ap.add_argument("--work", default=None,
                    help="scratch root for the clone/materialization "
                         "(default: $HYAKU_SCRATCH/kotodama-r75/counter or "
                         "/fast/scratch/hyaku/kotodama-r75/counter)")
    ap.add_argument("--selftest", action="store_true", help="run in-process cases")
    args = ap.parse_args(argv)

    if args.selftest:
        runner = globals().get("run_selftest")
        if runner is None:
            return refuse("--selftest needs part-selftest-fixtures.py and "
                          "part-selftest-run.py assembled before the __main__ "
                          "guard (CFG-CONTRACT item 5)")
        return runner()

    if not args.lands or not re.fullmatch(r"[0-9a-fA-F]{40}", args.lands.strip()):
        print("ERROR: --lands must be a 40-hex commit "
              "(the worktree is never graded, QUALITY 19)", file=sys.stderr)
        return 2
    if not args.freeze or not re.fullmatch(r"[0-9a-fA-F]{40}",
                                           args.freeze.strip()):
        print("ERROR: --freeze must be a 40-hex commit "
              "(the claim constants are read from it, H1)", file=sys.stderr)
        return 2
    lands = args.lands.strip().lower()
    freeze = args.freeze.strip().lower()
    root = args.root if os.path.isabs(args.root) else os.path.join(LANE, args.root)
    if not os.path.isdir(os.path.join(root, ".git")):
        print("ERROR: not a git repository: %s" % root, file=sys.stderr)
        return 2
    for name, rev in (("--lands", lands), ("--freeze", freeze)):
        if git(root, "cat-file", "-e", "%s^{commit}" % rev).returncode != 0:
            print("ERROR: %s revision not found: %s" % (name, rev),
                  file=sys.stderr)
            return 2
    try:
        cfg = load_frozen_config(root, freeze)
    except ConfigError as e:
        return refuse("%s" % e)
    if lands == cfg["base"]:
        return refuse("lands %s is the frozen claim base %s (the do-nothing "
                      "control: no data landed)" % (lands[:12], cfg["base"][:12]))
    if not is_ancestor(root, cfg["base"], lands):
        return refuse("claim base %s is not an ancestor of lands %s (the graded "
                      "revision is not descended from the claim's before-state)"
                      % (cfg["base"][:12], lands[:12]))
    ours = [name for name, _fn in LEGS]
    frozen_legs = cfg["frozen_legs"]
    if not frozen_legs:
        return refuse("the frozen claims.json carries no legs list (LEGCOUNT)")
    if len(frozen_legs) != len(ours) or frozen_legs != ours:
        return refuse("LEGCOUNT: the frozen claims.json lists %d legs (%s); "
                      "this counter implements %d (%s)"
                      % (len(frozen_legs), ",".join(frozen_legs),
                         len(ours), ",".join(ours)))
    if git(root, "cat-file", "-e", "%s^{commit}" % cfg["base"]).returncode != 0:
        print("ERROR: frozen claim base not found: %s" % cfg["base"],
              file=sys.stderr)
        return 2
    fleet_root = args.fleet_root or os.path.dirname(os.path.abspath(root))

    scratch = _scratch_root(args)
    if _forbidden_scratch(scratch):
        return refuse("scratch root %s is the system temporary directory "
                      "(pass --work or set $HYAKU_SCRATCH; QUALITY 14)"
                      % scratch)
    try:
        os.makedirs(scratch, exist_ok=True)
    except OSError as e:
        return refuse("cannot create scratch root %s: %s" % (scratch, e))

    tmp_root = tempfile.mkdtemp(prefix="r75-lands-", dir=scratch)
    try:
        mat = os.path.join(tmp_root, "clone")
        mat_base = os.path.join(tmp_root, "base")
        os.makedirs(mat_base)
        try:
            clone_at(root, lands, mat)
            how = ("git clone of %s, checkout --detach %s"
                   % (os.path.abspath(root), lands[:12]))
        except RuntimeError:
            shutil.rmtree(mat, ignore_errors=True)
            os.makedirs(mat)
            materialize(root, lands, mat)
            how = ("git archive of %s (the clone refused the revision)"
                   % lands[:12])
        try:
            materialize(root, cfg["base"], mat_base)
        except RuntimeError as e:
            print("ERROR: %s" % e, file=sys.stderr)
            return 2
        ctx = {"root": root, "lands": lands, "mat": mat, "mat_base": mat_base,
               "cfg": cfg, "fleet_root": fleet_root, "scratch": scratch}
        print_receipt(root, lands, mat, cfg, how)
        passed, total, _results = run_legs(ctx)
    finally:
        shutil.rmtree(tmp_root, ignore_errors=True)
    ok = passed == total
    print("ACCEPT-C-75: %s legs=%d/%d" % ("PASS" if ok else "FAIL", passed, total))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
