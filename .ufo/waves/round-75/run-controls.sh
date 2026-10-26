#!/bin/sh
# usage: run-controls.sh <freeze> [base]
#
# Round-75 do-nothing controls, measured at the freeze commit by the
# freeze-installed counter.  Modeled on .ufo/waves/round-74/run-controls.sh:
# two controls per claim, written to reports/round-75/telemetry/.
#
#   control 1: lands == <freeze>   — the legal ancestor relation with no data
#               landed.  Per the frozen claims: claim C must FAIL with the
#               data legs red and FROZENCFG green; claim Ca must FAIL with
#               REPAIR, ANNOTATE and R1EXEMPT red and FROZENCFG/LEDGER green.
#   control 2: lands == <base>     — the counter must REFUSE (the base is not
#               a descendant of the freeze) and print FAIL.
#
# The L1 runs this at the freeze; the script only runs the two counters and
# records their stdout and exit status.  It writes nothing outside the lane
# repository's own telemetry directory.
#
# Optional third argument "--junk" additionally runs the junk-landing fixture
# generator (reports/round-75/telemetry/junk-r75-run.txt, split into
# junk-c.txt / junk-ca.txt by the ===== SECTION markers), which needs a
# landing to be meaningful:
#
#   run-controls.sh <freeze> <base> --junk <landing-rev>
#
set -u

F=${1:-}
B=${2:-f556d1049fe651d3d63975600b13acd9fb686f15}
EXTRA=${3:-}
FL=/home/vgpnk/Projects/shokunin
LANE=/home/vgpnk/Projects/shokunin/kotodama-shokunin
T=reports/round-75/telemetry
WA=.ufo/waves/round-75

if [ -z "$F" ]; then
  echo "usage: run-controls.sh <freeze> [base] [--junk <landing-rev>]" >&2
  exit 2
fi

cd "$LANE" || exit 2
mkdir -p "$T" || exit 2

# The counter bytes the L1 installs at the freeze commit; the wave copy is
# the fallback when the reports/ path is not populated yet.
pick_counter() {
  for c in "reports/round-75/$1" "$WA/counters/$1"; do
    if [ -f "$c" ]; then echo "$c"; return 0; fi
  done
  echo "MISSING:$1"
  return 1
}

CC=$(pick_counter accept-c.py)
CCA=$(pick_counter accept-ca.py)

if [ "${CC#MISSING:}" != "$CC" ] || [ "${CCA#MISSING:}" != "$CCA" ]; then
  echo "ERROR: no round-75 counter found (need accept-c.py and accept-ca.py" >&2
  echo "       at reports/round-75/ or $WA/counters/)" >&2
  exit 2
fi

{ echo "# controls-c.txt — claim C do-nothing controls (round 75), measured at freeze $F by the freeze-installed counter"
echo "# counter: $CC"
echo "## control 1: lands == freeze (legal ancestor relation; no data landed)"
echo "\$ python3 -B $CC --root . --lands $F --freeze $F"
python3 -B "$CC" --root . --lands "$F" --freeze "$F" 2>&1; echo "exit=$?"; echo
echo "## control 2: lands == base (refusal prints FAIL)"
echo "\$ python3 -B $CC --root . --lands $B --freeze $F"
python3 -B "$CC" --root . --lands "$B" --freeze "$F" 2>&1; echo "exit=$?"; } > "$T/controls-c.txt" &
CPID=$!

{ echo "# controls-ca.txt — claim Ca do-nothing controls (round 75), measured at freeze $F by the freeze-installed counter"
echo "# counter: $CCA"
echo "## control 1: lands == freeze"
echo "\$ python3 -B $CCA --root . --lands $F --freeze $F --fleet-root $FL"
python3 -B "$CCA" --root . --lands "$F" --freeze "$F" --fleet-root "$FL" 2>&1; echo "exit=$?"; echo
echo "## control 2: lands == base"
echo "\$ python3 -B $CCA --root . --lands $B --freeze $F --fleet-root $FL"
python3 -B "$CCA" --root . --lands "$B" --freeze "$F" --fleet-root "$FL" 2>&1; echo "exit=$?"; } > "$T/controls-ca.txt" &
CAPID=$!

wait $CPID
wait $CAPID

# Optional: the junk-landing fixture sweep.  It needs a landing revision to
# be attributable (the J* fixtures mutate the landing tree; the R1EXEMPT pair
# is measured against the freeze tree and the lane base).
if [ "$EXTRA" = "--junk" ]; then
  LAND=${4:-}
  if [ -z "$LAND" ]; then
    echo "ERROR: --junk needs a landing revision as the fourth argument" >&2
    exit 2
  fi
  python3 -B "$WA/counters/junk-fixtures.py" --run \
      --freeze "$F" --base "$B" --lands "$LAND" \
      --out-dir "$T" --out "$T/junk-r75-run.txt" 2>&1
  echo "exit=$?"
  # Split the sweep into the two per-claim telemetry files the frozen
  # do_nothing_control sentences name (junk-c.txt / junk-ca.txt).
  awk '/^# ===== SECTION C =====/{sec="C"} /^# ===== SECTION Ca =====/{sec="Ca"} \
       sec=="C"' "$T/junk-r75-run.txt" > "$T/junk-c.txt"
  awk '/^# ===== SECTION Ca =====/{sec="Ca"} sec=="Ca"' \
      "$T/junk-r75-run.txt" > "$T/junk-ca.txt"
fi

echo "controls written to $T/controls-c.txt and $T/controls-ca.txt"
exit 0
