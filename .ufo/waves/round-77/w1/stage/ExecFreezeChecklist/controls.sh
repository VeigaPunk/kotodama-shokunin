#!/bin/sh
# Round-77 freeze-gate controls — reproduce every receipt this seat reports.
#
# usage: controls.sh [--lane DIR] [--scratch DIR]
#
#   Section A  legcount.py unit controls against the round-76 pair (read-only):
#              P1 positive (C and Ca green, the duplicate INDEX handled), P2
#              committed-blob read (--rev), N1..N5 frozen-list defects, N6/N7
#              unusable counter tables.
#   Section B  the four emitted one-liners from manifest.json `legcount.checks`
#              (syntax + exit on the round-76 pair; same argv shape, r76 paths).
#   Section C  manifest-check.py end-to-end on a throwaway fixture repo under the
#              scratch root: record -> commit -> freeze PASS, worktree tamper
#              (still PASS: blob authority), committed tamper (MISMATCH), revert
#              (PASS), committed delete (MISSING), recovery + leg drift (LEGCOUNT
#              FAIL only), legcount.py --rev on the drift.
#
# Nothing is written outside the scratch directory; the fixture repo gets a
# repo-local identity (user.name/user.email set in that repo only) and its
# toplevel is asserted before the first commit.  The lane is only read.
#
# Exit: 0 when every control produced its expected verdict, 1 when one did not,
# 2 on a usage/setup error.
#
# Scratch policy: the default root is
#   ${HYAKU_SCRATCH:-/fast/scratch/hyaku/kotodama-r77}/ExecFreezeChecklist-controls.$$
# and only that directory is removed on exit.

set -u

LANE=/home/vgpnk/Projects/shokunin/kotodama-shokunin
SCRATCH_BASE=${HYAKU_SCRATCH:-/fast/scratch/hyaku/kotodama-r77}

while [ $# -gt 0 ]; do
  case $1 in
    --lane) shift; [ $# -gt 0 ] || { echo "controls.sh: --lane needs a dir" >&2; exit 2; }; LANE=$1 ;;
    --lane=*) LANE=${1#--lane=} ;;
    --scratch) shift; [ $# -gt 0 ] || { echo "controls.sh: --scratch needs a dir" >&2; exit 2; }; SCRATCH_BASE=$1 ;;
    --scratch=*) SCRATCH_BASE=${1#--scratch=} ;;
    -h|--help) sed -n '2,30p' "$0"; exit 0 ;;
    *) echo "controls.sh: unknown argument: $1" >&2; exit 2 ;;
  esac
  shift
done

ST=$(CDPATH='' cd -- "$(dirname -- "$0")" && pwd) || exit 2
[ -f "$ST/legcount.py" ] && [ -f "$ST/manifest-check.py" ] || {
  echo "controls.sh: legcount.py / manifest-check.py not beside $0" >&2; exit 2; }

mkdir -p "$SCRATCH_BASE" || exit 2
S=$SCRATCH_BASE/ExecFreezeChecklist-controls.$$
mkdir -p "$S" || exit 2
case $S in
  "$SCRATCH_BASE"/ExecFreezeChecklist-controls.*) ;;
  *) echo "controls.sh: refusing scratch path $S" >&2; exit 2 ;;
esac
trap 'rm -rf -- "$S"' EXIT

RC=0
expect() { # <label> <want> <got>
  if [ "$2" = "$3" ]; then
    printf 'EXPECT %-10s %s (got %s)\n' "$1" "$2" "$3"
  else
    printf 'EXPECT %-10s %s (got %s)  <-- MISMATCH\n' "$1" "$2" "$3"
    RC=1
  fi
}

L=$LANE
R76C=$L/reports/round-76/accept-c.py
R76CA=$L/reports/round-76/accept-ca.py
R76J=$L/reports/round-76/claims.json
BASE=211f9526800906e0c585d878d265c37e5e090c15

echo "# round-77 freeze-gate controls"
echo "# scripts: $ST"
( cd "$ST" && sha256sum legcount.py manifest-check.py controls.sh 2>/dev/null | sed 's/^/#   sha256 /' )
echo "# lane (read-only): $L"
echo "# scratch: $S (removed on exit)"
echo

echo "## Section A1 — positive control: the round-76 pair must be green"
echo "\$ legcount.py --claim C --claims reports/round-76/claims.json --counter reports/round-76/accept-c.py"
python3 -B "$ST/legcount.py" --claim C --claims reports/round-76/claims.json --counter reports/round-76/accept-c.py
expect P1-C 0 $?
echo
echo "\$ legcount.py --claim Ca --claims reports/round-76/claims.json --counter reports/round-76/accept-ca.py"
python3 -B "$ST/legcount.py" --claim Ca --claims reports/round-76/claims.json --counter reports/round-76/accept-ca.py
expect P1-Ca 0 $?
echo

echo "## Section A2 — committed-blob read (--rev $BASE)"
echo "\$ legcount.py --claim Ca --claims reports/round-76/claims.json --counter reports/round-76/accept-ca.py --rev $BASE"
python3 -B "$ST/legcount.py" --claim Ca --claims reports/round-76/claims.json --counter reports/round-76/accept-ca.py --rev "$BASE"
expect P2 0 $?
echo

echo "## Section A3 — negative controls: mutated copies of the round-76 claims (scratch)"
mkdir -p "$S/fx"
python3 - "$R76J" "$S/fx" <<'PY'
import copy, json, os, sys
src, out = sys.argv[1], sys.argv[2]
base = json.load(open(src))
def dump(name, doc):
    json.dump(doc, open(os.path.join(out, name), 'w'), indent=1)
c = copy.deepcopy(base)
legs = c['claims'][0]['legs']
legs[9] = "SCRATCHMIRROR:" + legs[9].split(':', 1)[1]
dump('n1-renamed.json', c)
c = copy.deepcopy(base)
legs = c['claims'][0]['legs']
legs[0], legs[1] = legs[1], legs[0]
dump('n2-reordered.json', c)
c = copy.deepcopy(base)
del c['claims'][0]['legs'][3]
dump('n3-short.json', c)
c = copy.deepcopy(base)
c['claims'][0]['legs'].append(c['claims'][0]['legs'][0])
dump('n4-duplicated.json', c)
c = copy.deepcopy(base)
legs = c['claims'][0]['legs']
legs[5] = "LEDGELIST?:" + legs[5].split(':', 1)[1]
dump('n5-placeholder.json', c)
PY
for fx in n1-renamed n2-reordered n3-short n4-duplicated n5-placeholder; do
  echo "\$ legcount.py --claim C --claims $S/fx/$fx.json --counter reports/round-76/accept-c.py"
  python3 -B "$ST/legcount.py" --claim C --claims "$S/fx/$fx.json" --counter reports/round-76/accept-c.py
  expect "$fx" 1 $?
  echo
done
mkdir -p "$S/fx/n6" "$S/fx/n7"
printf 'NAMES = ("ENTRIES", "ROWS")\nLEGS = tuple(NAMES)\n' > "$S/fx/n6/accept-c.py"
printf 'LEGS = (("ENTRIES", leg_entries)\n' > "$S/fx/n7/accept-c.py"
for fx in n6 n7; do
  echo "\$ legcount.py --claim C --claims reports/round-76/claims.json --counter $S/fx/$fx/accept-c.py"
  python3 -B "$ST/legcount.py" --claim C --claims reports/round-76/claims.json --counter "$S/fx/$fx/accept-c.py"
  expect "$fx" 2 $?
  echo
done

echo "## Section B — the manifest's emitted one-liners (round-76 paths: same argv shape)"
echo '$ python3 -c "…sorted(F)==sorted(LEGS)…"   # claim C'
python3 -c "import ast,json;t=ast.parse(open('reports/round-76/accept-c.py').read());g=[n.value for n in t.body if isinstance(n,ast.Assign) and any(getattr(x,'id','')=='LEGS' for x in n.targets)][0];LEGS=[e.elts[0].value for e in g.elts];c=json.load(open('reports/round-76/claims.json'));F=[l.split(':',1)[0].strip() for l in c['claims'][0]['legs']];assert sorted(F)==sorted(LEGS),(F,LEGS)"
expect B-C-set 0 $?
echo '$ python3 -c "…F==LEGS…"   # claim C, order included'
python3 -c "import ast,json;t=ast.parse(open('reports/round-76/accept-c.py').read());g=[n.value for n in t.body if isinstance(n,ast.Assign) and any(getattr(x,'id','')=='LEGS' for x in n.targets)][0];LEGS=[e.elts[0].value for e in g.elts];c=json.load(open('reports/round-76/claims.json'));F=[l.split(':',1)[0].strip() for l in c['claims'][0]['legs']];assert F==LEGS,(F,LEGS)"
expect B-C-order 0 $?
echo '$ python3 -c "…sorted(F)==sorted(LEGS)…"   # claim Ca'
python3 -c "import ast,json;t=ast.parse(open('reports/round-76/accept-ca.py').read());g=[n.value for n in t.body if isinstance(n,ast.Assign) and any(getattr(x,'id','')=='REQUIRED_LEGS' for x in n.targets)][0];LEGS=[e.value for e in g.elts];c=json.load(open('reports/round-76/claims.json'));F=[l.split(':',1)[0].strip() for l in c['claims'][1]['legs']];assert sorted(F)==sorted(LEGS),(F,LEGS)"
expect B-Ca-set 0 $?
echo '$ python3 -c "…F==LEGS…"   # claim Ca, order included'
python3 -c "import ast,json;t=ast.parse(open('reports/round-76/accept-ca.py').read());g=[n.value for n in t.body if isinstance(n,ast.Assign) and any(getattr(x,'id','')=='REQUIRED_LEGS' for x in n.targets)][0];LEGS=[e.value for e in g.elts];c=json.load(open('reports/round-76/claims.json'));F=[l.split(':',1)[0].strip() for l in c['claims'][1]['legs']];assert F==LEGS,(F,LEGS)"
expect B-Ca-order 0 $?
echo

echo "## Section C — manifest-check.py end-to-end (fixture repo under the scratch root)"
D=$S/e2e
mkdir -p "$D"
git -C "$D" init -q .
TOP=$(git -C "$D" rev-parse --show-toplevel 2>/dev/null) || { echo "controls.sh: fixture init failed" >&2; exit 2; }
[ "$TOP" = "$D" ] || { echo "controls.sh: fixture toplevel $TOP != $D" >&2; exit 2; }
git -C "$D" config user.name e2e-fixture
git -C "$D" config user.email e2e@fixture.invalid
python3 - "$D" <<'PY'
import json, os, sys
D = sys.argv[1]
files = ["reports/round-77/claims.json", "reports/round-77/ledger.json",
         "reports/round-77/accept-c.py", "reports/round-77/accept-ca.py",
         "reports/round-77/counters/capture-evidence.py",
         "reports/round-77/counters/junk-fixtures.py",
         "reports/round-77/fixtures/r1exempt-green.json",
         "reports/round-77/fixtures/r1exempt-mixed.json",
         "reports/round-77/fixtures/r1exempt-red.json",
         "reports/round-77/telemetry/controls-c.txt",
         "reports/round-77/telemetry/controls-ca.txt",
         "reports/round-77/telemetry/junk-c.txt",
         "reports/round-77/telemetry/junk-ca.txt",
         "reports/round-77/telemetry/census-start.txt",
         "reports/round-77/telemetry/census-start-counts.txt",
         "reports/round-77/telemetry/selftest-c.txt",
         "reports/round-77/telemetry/selftest-ca.txt",
         "reports/round-77/telemetry/gap-sweep.txt"]
for rel in files:
    path = os.path.join(D, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, 'w').write("fixture bytes for %s\n" % rel)
json.dump({"round": 77, "claims": [{"id": "C", "legs": ["ALPHA: one", "BETA: two"]},
                                   {"id": "Ca", "legs": ["GAMMA: three"]}]},
          open(os.path.join(D, "reports/round-77/claims.json"), 'w'))
open(os.path.join(D, "reports/round-77/accept-c.py"), 'w').write(
    'LEGS = (("ALPHA", leg_alpha), ("BETA", leg_beta))\n')
open(os.path.join(D, "reports/round-77/accept-ca.py"), 'w').write(
    'REQUIRED_LEGS = ("GAMMA",)\n')
PY
cp "$ST/manifest.json" "$D/manifest.json"
MC="python3 -B $ST/manifest-check.py"

# runm <argv...>: run it, print the last 4 lines, return ITS exit status
# ($? after a pipe is tail's, which would make every expectation vacuous)
runm() {
  _out=$("$@" 2>&1); _rc=$?
  printf '%s\n' "$_out" | tail -4
  return $_rc
}

echo "\$ manifest-check.py --root $D --manifest $D/manifest.json --record"
runm $MC --root "$D" --manifest "$D/manifest.json" --record
expect C1-record 0 $?
echo "\$ git -C $D add -A; git -C $D commit -qm freeze-fixture; manifest-check.py … --freeze HEAD"
git -C "$D" add -A && git -C "$D" commit -q -m freeze-fixture
runm $MC --root "$D" --manifest "$D/manifest.json" --freeze HEAD
expect C2-freeze-pass 0 $?
echo "\$ printf tamper >> reports/round-77/telemetry/junk-c.txt  (NOT committed)"
printf 'tamper\n' >> "$D/reports/round-77/telemetry/junk-c.txt"
runm $MC --root "$D" --manifest "$D/manifest.json" --freeze HEAD
expect C3-blob-authority 0 $?
echo "\$ git -C $D commit -qam tamper; manifest-check.py … --freeze HEAD"
git -C "$D" commit -qam tamper
runm $MC --root "$D" --manifest "$D/manifest.json" --freeze HEAD
expect C4-committed-tamper 1 $?
echo "\$ git -C $D revert the tamper (checkout HEAD~1 -- the file; commit); manifest-check.py … --freeze HEAD"
git -C "$D" checkout HEAD~1 -- reports/round-77/telemetry/junk-c.txt
git -C "$D" commit -q -m untamper
runm $MC --root "$D" --manifest "$D/manifest.json" --freeze HEAD
expect C5-revert-pass 0 $?
echo "\$ git -C $D rm -q reports/round-77/fixtures/r1exempt-mixed.json; commit; manifest-check.py … --freeze HEAD"
git -C "$D" rm -q reports/round-77/fixtures/r1exempt-mixed.json
git -C "$D" commit -q -m drop
runm $MC --root "$D" --manifest "$D/manifest.json" --freeze HEAD
expect C6-committed-drop 1 $?
echo "\$ restore the dropped file, re-spell claim C legs[1] (BETA -> GAMMA), re-record, commit"
git -C "$D" show HEAD~1:reports/round-77/fixtures/r1exempt-mixed.json \
  > "$D/reports/round-77/fixtures/r1exempt-mixed.json"
python3 - "$D" <<'PY'
import json, os, sys
D = sys.argv[1]
json.dump({"round": 77, "claims": [{"id": "C", "legs": ["ALPHA: one", "GAMMA: two"]},
                                   {"id": "Ca", "legs": ["GAMMA: three"]}]},
          open(os.path.join(D, "reports/round-77/claims.json"), 'w'))
PY
runm $MC --root "$D" --manifest "$D/manifest.json" --record
git -C "$D" add -A && git -C "$D" commit -q -m legdrift
echo "\$ manifest-check.py … --freeze HEAD   (digests pinned: the only red must be LEGCOUNT)"
runm $MC --root "$D" --manifest "$D/manifest.json" --freeze HEAD
expect C7-leg-drift 1 $?
echo "\$ legcount.py --claim C --root $D --rev HEAD"
python3 -B "$ST/legcount.py" --claim C --root "$D" --rev HEAD
expect C8-legcount-direct 1 $?
echo
echo "## manifest-check.py build mode on the real lane (expected PENDING: freeze-installed inputs)"
echo "\$ manifest-check.py --root $L"
runm python3 -B "$ST/manifest-check.py" --root "$L"
echo
if [ "$RC" = 0 ]; then
  echo "CONTROLS: all expectations met"
else
  echo "CONTROLS: at least one expectation unmet (see MISMATCH lines)"
fi
exit "$RC"
