#!/bin/sh
# usage: run-controls.sh <freeze> [base] [options]
#
# Round-76 do-nothing controls, measured at the freeze commit by the
# freeze-installed counters.  Modeled on .ufo/waves/round-75/run-controls.sh
# (read, never edited); the round tokens, the base, the telemetry directory,
# the counter fallback path and the junk generator path are round 76's.
#
#   control 1: lands == <freeze>   — the legal ancestor relation with no data
#               landed.  Per the frozen claims: claim C must FAIL with the data
#               legs red and FROZENCFG green; claim Ca must FAIL with REPAIR,
#               ANNOTATE and R1EXEMPT red and FROZENCFG/LEDGER green.
#   control 2: lands == <base>     — the counter must REFUSE (the base is not a
#               descendant of the freeze) and print FAIL.
#
# Options:
#   --base REV         override the round-76 base (default 98c486bdb4650b…).
#   --combined REV     pass the combined (C-lands) revision to accept-ca.py.
#                      The Ca COMBINED leg requires it; without it that leg is
#                      red by construction (the round-75 control shape).
#   --junk REV         also run the junk-landing sweep against landing REV and
#                      split it into telemetry/junk-c.txt and junk-ca.txt.
#   --fleet-root DIR   fleet root handed to both counters (default
#                      /home/vgpnk/Projects/shokunin).
#   --work DIR         counter scratch root (default
#                      ${HYAKU_SCRATCH:-/fast/scratch/hyaku/kotodama-r76}/controls).
#
# The script only runs the two counters and records their stdout and exit
# status.  It writes nothing outside the lane's own reports/round-76/telemetry
# directory; the counters keep their scratch under --work (never a literal /tmp).
#
# Exit: 0 when both receipts were written, 2 on a usage or counter-setup error.

set -u

BASE_DEFAULT=98c486bdb4650ba5b8e651d332910e8ee60ad121
F=${1:-}
if [ $# -gt 0 ]; then shift; fi
B=$BASE_DEFAULT
if [ $# -gt 0 ]; then
  case $1 in
    -*) ;;
    *) B=$1; shift ;;
  esac
fi

FL=/home/vgpnk/Projects/shokunin
COMBINED=
JUNK=
WORK=${HYAKU_SCRATCH:-/fast/scratch/hyaku/kotodama-r76}/controls

while [ $# -gt 0 ]; do
  case $1 in
    --base)
      shift; [ $# -gt 0 ] || { echo "run-controls.sh: --base needs a revision" >&2; exit 2; }
      B=$1 ;;
    --base=*) B=${1#--base=} ;;
    --combined)
      shift; [ $# -gt 0 ] || { echo "run-controls.sh: --combined needs a revision" >&2; exit 2; }
      COMBINED=$1 ;;
    --combined=*) COMBINED=${1#--combined=} ;;
    --junk)
      shift; [ $# -gt 0 ] || { echo "run-controls.sh: --junk needs a landing revision" >&2; exit 2; }
      JUNK=$1 ;;
    --junk=*) JUNK=${1#--junk=} ;;
    --fleet-root)
      shift; [ $# -gt 0 ] || { echo "run-controls.sh: --fleet-root needs a directory" >&2; exit 2; }
      FL=$1 ;;
    --fleet-root=*) FL=${1#--fleet-root=} ;;
    --work)
      shift; [ $# -gt 0 ] || { echo "run-controls.sh: --work needs a directory" >&2; exit 2; }
      WORK=$1 ;;
    --work=*) WORK=${1#--work=} ;;
    *) echo "run-controls.sh: unknown argument: $1" >&2; exit 2 ;;
  esac
  shift
done

if [ -z "$F" ]; then
  echo "usage: run-controls.sh <freeze> [base] [--combined REV] [--junk REV]" >&2
  echo "                      [--fleet-root DIR] [--work DIR]" >&2
  exit 2
fi
case $F in
  *[!0-9a-f]*|'') echo "run-controls.sh: --freeze must be 40 hex, got '$F'" >&2; exit 2 ;;
esac
case $B in
  *[!0-9a-f]*|'') echo "run-controls.sh: --base must be 40 hex, got '$B'" >&2; exit 2 ;;
esac

LANE=/home/vgpnk/Projects/shokunin/kotodama-shokunin
T=reports/round-76/telemetry
WA=.ufo/waves/round-76

cd "$LANE" || exit 2
TOP=$(git -C "$LANE" rev-parse --show-toplevel 2>/dev/null) || {
  echo "run-controls.sh: $LANE is not a git worktree" >&2; exit 2
}
[ "$TOP" = "$LANE" ] || {
  echo "run-controls.sh: $LANE is not a worktree toplevel (git says $TOP)" >&2; exit 2
}
git -C "$LANE" cat-file -e "$F^{commit}" 2>/dev/null || {
  echo "run-controls.sh: freeze $F is not a commit in $LANE" >&2; exit 2
}
git -C "$LANE" cat-file -e "$B^{commit}" 2>/dev/null || {
  echo "run-controls.sh: base $B is not a commit in $LANE" >&2; exit 2
}

mkdir -p "$T" "$WORK" || exit 2

# The counter bytes the L1 installs at the freeze commit; the wave copy is the
# fallback when the reports/ path is not populated yet.
pick_counter() {
  for c in "reports/round-76/$1" "$WA/counters/$1"; do
    if [ -f "$c" ]; then echo "$c"; return 0; fi
  done
  echo "MISSING:$1"
  return 1
}

CC=$(pick_counter accept-c.py)
CCA=$(pick_counter accept-ca.py)

if [ "${CC#MISSING:}" != "$CC" ] || [ "${CCA#MISSING:}" != "$CCA" ]; then
  echo "ERROR: no round-76 counter found (need accept-c.py and accept-ca.py" >&2
  echo "       at reports/round-76/ or $WA/counters/)" >&2
  exit 2
fi

# The C counter takes no --combined; the Ca counter requires it for a green
# COMBINED leg and treats its absence as red, which is the control-1 shape.
CA_COMBINED=
[ -n "$COMBINED" ] && CA_COMBINED="--combined $COMBINED"

{
  echo "# controls-c.txt — claim C do-nothing controls (round 76), measured at freeze $F by the freeze-installed counter"
  echo "# counter: $CC"
  echo "# work: $WORK (the counter's own scratch; never a literal /tmp)"
  echo "## control 1: lands == freeze (legal ancestor relation; no data landed)"
  echo "\$ python3 -B $CC --root . --lands $F --freeze $F --fleet-root $FL --work $WORK"
  python3 -B "$CC" --root . --lands "$F" --freeze "$F" --fleet-root "$FL" --work "$WORK" 2>&1
  rc=$?
  echo "exit=$rc"
  echo "# expected: exit=1, FAIL on the data legs and PASS on FROZENCFG"
  echo
  echo "## control 2: lands == base (refusal prints FAIL)"
  echo "\$ python3 -B $CC --root . --lands $B --freeze $F --fleet-root $FL --work $WORK"
  python3 -B "$CC" --root . --lands "$B" --freeze "$F" --fleet-root "$FL" --work "$WORK" 2>&1
  rc=$?
  echo "exit=$rc"
  echo "# expected: exit=2, the counter refuses the frozen base"
} > "$T/controls-c.txt" &
CPID=$!

{
  echo "# controls-ca.txt — claim Ca do-nothing controls (round 76), measured at freeze $F by the freeze-installed counter"
  echo "# counter: $CCA"
  echo "# work: $WORK (the counter's own scratch; never a literal /tmp)"
  echo "## control 1: lands == freeze"
  echo "\$ python3 -B $CCA --root . --lands $F --freeze $F --fleet-root $FL --work $WORK $CA_COMBINED"
  # shellcheck disable=SC2086  # CA_COMBINED is a deliberate two-word option pair
  python3 -B "$CCA" --root . --lands "$F" --freeze "$F" --fleet-root "$FL" --work "$WORK" $CA_COMBINED 2>&1
  rc=$?
  echo "exit=$rc"
  echo "# expected: exit=1, FAIL on REPAIR/ANNOTATE/R1EXEMPT, PASS on FROZENCFG and LEDGER"
  echo
  echo "## control 2: lands == base"
  echo "\$ python3 -B $CCA --root . --lands $B --freeze $F --fleet-root $FL --work $WORK"
  python3 -B "$CCA" --root . --lands "$B" --freeze "$F" --fleet-root "$FL" --work "$WORK" 2>&1
  rc=$?
  echo "exit=$rc"
  echo "# expected: exit=2, the counter refuses the frozen base"
} > "$T/controls-ca.txt" &
CAPID=$!

wait $CPID
wait $CAPID

# Optional: the junk-landing fixture sweep.  It needs a landing revision to be
# attributable (the J* fixtures mutate the landing tree; the R1EXEMPT pair is
# measured against the freeze tree and the lane base).
if [ -n "$JUNK" ]; then
  python3 -B "$WA/counters/junk-fixtures.py" --run \
      --freeze "$F" --base "$B" --lands "$JUNK" \
      --out-dir "$T" --out "$T/junk-r76-run.txt" 2>&1
  echo "exit=$?"
  # Split the sweep into the two per-claim telemetry files the frozen
  # do_nothing_control sentences name (junk-c.txt / junk-ca.txt).
  awk '/^# ===== SECTION Ca =====/{sec="Ca"} sec!="Ca"' "$T/junk-r76-run.txt" > "$T/junk-c.txt"
  awk '/^# ===== SECTION Ca =====/{sec="Ca"} sec=="Ca"' "$T/junk-r76-run.txt" > "$T/junk-ca.txt"
fi

echo "controls written to $T/controls-c.txt and $T/controls-ca.txt"
exit 0
