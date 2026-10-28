#!/usr/bin/env bash
# verify-scratch-discipline.sh — re-run the round-77 wave-1 scratch audit.
#
# Read-only over the wave tree; every byte it writes lives under
# ${HYAKU_SCRATCH:-/fast/scratch/hyaku}/kotodama-r77/ExecTmpAudit/verify.
# No path in this script is a literal system temp root; it honours
# --work, then $HYAKU_SCRATCH, then $TMPDIR, then the operator tree, and
# refuses when none of them is set.
#
#   ./verify-scratch-discipline.sh [--work <dir>] [--stage <dir>] [--snapshot]
#
# Exit 0 = no fatal scratch defect in the scanned tree; 1 = at least one.
set -u

LANE=/home/vgpnk/Projects/shokunin/kotodama-shokunin
STAGE=$LANE/.ufo/waves/round-77/w1/stage
WORK=""
SNAP=0
while [ $# -gt 0 ]; do
    case $1 in
        --work) WORK=${2:-}; [ -n "$WORK" ] || { echo "verify: --work needs a dir" >&2; exit 2; }; shift 2 ;;
        --work=*) WORK=${1#--work=}; shift ;;
        --stage) STAGE=${2:-}; [ -n "$STAGE" ] || { echo "verify: --stage needs a dir" >&2; exit 2; }; shift 2 ;;
        --stage=*) STAGE=${1#--stage=}; shift ;;
        --snapshot) SNAP=1; shift ;;
        *) echo "verify: unknown argument $1" >&2; exit 2 ;;
    esac
done

ROOT=""
for candidate in "$WORK" "${HYAKU_SCRATCH:-}" "${SHOKUNIN_SCRATCH:-}" "${TMPDIR:-}"; do
    if [ -n "${candidate:-}" ]; then ROOT=$candidate; break; fi
done
if [ -z "$ROOT" ]; then
    echo "verify: no scratch root: pass --work, or set \$HYAKU_SCRATCH or \$TMPDIR" >&2
    exit 2
fi
ROOT=$ROOT/verify-scratch-audit
mkdir -p "$ROOT" || exit 2

SCANNERS=$LANE/.ufo/waves/round-77/w1/stage/ExecTmpAudit
TARGET=$STAGE
if [ "$SNAP" = 1 ]; then
    TARGET=$ROOT/snap-$$
    mkdir -p "$TARGET" && cp -a "$STAGE/." "$TARGET/" || exit 2
    echo "# snapshot of the live stage tree: $TARGET"
fi

echo "# == 1. literal-/tmp write targets (fatal) =="
python3 -B "$SCANNERS/check-scratch-root.py" --root "$TARGET" \
    --paths '**/*.py' --paths '**/*.sh' --allow "$SCANNERS/allow.txt"
echo "root-scan exit=$?"

echo "# == 2. resolution chain (--work / \$HYAKU_SCRATCH / \$TMPDIR) =="
python3 -B "$SCANNERS/check-scratch-chain.py" --root "$TARGET" \
    --paths '**/*.py' --paths '**/*.sh' --allow "$SCANNERS/allow.txt" | grep -v '^PROBE'
echo "chain-scan exit=$?"

echo "# == 3. counter resolvers, measured under four environments =="
for tool in ExecAdaptC/accept-c.py ExecAdaptCa/accept-ca.py ExecAdaptJunk/junk-fixtures.py; do
    f=$TARGET/$tool
    [ -f "$f" ] || continue
    TMPDIR="$ROOT/env-t" HYAKU_SCRATCH="$ROOT/env-h" python3 -B - "$f" "$ROOT" <<'PY'
import importlib.util, os, sys, tempfile, types
path, root = sys.argv[1], sys.argv[2]
spec = importlib.util.spec_from_file_location("probe_tool", path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
resolver = None
for name in ("_scratch_root", "scratch_root", "resolve_workroot", "scratch_dir"):
    if callable(getattr(module, name, None)):
        resolver = (name, getattr(module, name))
        break
if resolver is None:
    print("%-40s no exported resolver" % os.path.basename(path))
    raise SystemExit(0)
name, func = resolver
argnames = func.__code__.co_varnames[:func.__code__.co_argcount]
cases = (("--work", {}, {"explicit": os.path.join(root, "w")}, {"work": os.path.join(root, "w")}),
         ("$HYAKU_SCRATCH", {"HYAKU_SCRATCH": os.path.join(root, "h"), "TMPDIR": ""}, {}, {}),
         ("$TMPDIR", {"TMPDIR": os.path.join(root, "t"), "HYAKU_SCRATCH": ""}, {}, {}),
         ("$TMPDIR=/tmp", {"TMPDIR": "/tmp", "HYAKU_SCRATCH": ""}, {}, {}),
         ("none", {}, {}, {}))
for label, env, kw, fakeargs in cases:
    saved = {k: os.environ.get(k) for k in ("TMPDIR", "HYAKU_SCRATCH", "SHOKUNIN_SCRATCH")}
    try:
        for key in saved:
            os.environ.pop(key, None)
        for key, value in env.items():
            if value:
                os.environ[key] = value
        tempfile.tempdir = None  # drop the cached gettempdir() of a previous case
        try:
            if argnames[:2] == ("explicit", "round_no") or argnames[:1] == ("explicit",):
                out = func(explicit=kw.get("explicit"))
            else:
                out = func(types.SimpleNamespace(work=fakeargs.get("work")))
        except Exception as exc:  # noqa: BLE001 - a refusal is a result
            out = "REFUSED: %s: %s" % (type(exc).__name__, exc)
        print("%-28s %-14s -> %s" % (os.path.basename(path), label, out))
    finally:
        for key, value in saved.items():
            if value is None:
                os.environ.pop(key, None)
            else:
                os.environ[key] = value
PY
done

echo "# == 3b. capture-evidence: no-root fallback (dir=None -> interpreter temp) =="
if [ -f "$TARGET/ExecAdaptCapture/capture-evidence.py" ]; then
    env -u TMPDIR -u HYAKU_SCRATCH -u SHOKUNIN_SCRATCH python3 -B - \
        "$TARGET/ExecAdaptCapture/capture-evidence.py" <<'PY'
import importlib.util, sys, tempfile
spec = importlib.util.spec_from_file_location("ce", sys.argv[1])
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
print("work_base(None) with no --work/$HYAKU_SCRATCH/$TMPDIR ->",
      m.work_base(None), "| mkdtemp(dir=None) would use", tempfile.gettempdir())
PY
fi

echo "# == 4. tools whose no-root fallback is the interpreter temp dir =="
env -u TMPDIR -u HYAKU_SCRATCH -u SHOKUNIN_SCRATCH python3 -c 'import tempfile; print("tempfile.gettempdir() with no env ->", tempfile.gettempdir())'

echo "# == 5. shell control scripts: scratch default under a parent HYAKU_SCRATCH =="
for script in ExecFreezeChecklist/controls.sh ExecGapSweep/run-controls.sh; do
    f=$TARGET/$script
    [ -f "$f" ] || continue
    grep -n 'SCRATCH_BASE=\|SCRATCH=[^ ]*HYAKU_SCRATCH' "$f" | sed "s|^|$script:|"
done

echo "# == 6. selftests (a failing selftest invalidates every graded run) =="
for tool in ExecAdaptC/accept-c.py ExecAdaptCa/accept-ca.py ExecAdaptJunk/junk-fixtures.py; do
    f=$TARGET/$tool
    [ -f "$f" ] || continue
    case $tool in
        ExecAdaptJunk/*) HYAKU_SCRATCH="$ROOT/selftest-h" TMPDIR="$ROOT/selftest-t" \
            python3 -B "$f" --selftest > "$ROOT/$(basename "$f").selftest.txt" 2>&1
            echo "$tool --selftest exit=$? (receipt $ROOT/$(basename "$f").selftest.txt)" ;;
        *) HYAKU_SCRATCH="$ROOT/selftest-h" TMPDIR="$ROOT/selftest-t" \
            python3 -B "$f" --selftest > "$ROOT/$(basename "$f").selftest.txt" 2>&1
            echo "$tool --selftest exit=$? (receipt $ROOT/$(basename "$f").selftest.txt)" ;;
    esac
done

echo "# scratch used: $ROOT"
