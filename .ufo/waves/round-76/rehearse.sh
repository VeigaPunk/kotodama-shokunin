#!/bin/sh
# Round-76 rehearsal: base -> freeze -> claim Ca landing -> claim C landing,
# all inside a scratch clone, then both counters at their own landings.
#
# usage: rehearse.sh [options]
#
#   --base REV        lane revision to start from (default
#                     98c486bdb4650ba5b8e651d332910e8ee60ad121).
#   --drafts DIR      draft set handed to apply-landing.py (default
#                     .ufo/waves/round-76/w2/stage under the lane).
#   --manifest FILE   manifest handed to apply-landing.py (default
#                     <drafts>/manifest.json).
#   --scratch DIR     scratch parent (default
#                     ${HYAKU_SCRATCH:-/fast/scratch/hyaku/kotodama-r76});
#                     the clone lives at <scratch>/L1-rehearse/lane.
#   --combined REV    --combined handed to accept-ca.py (default: the C landing
#                     this run produced).
#   --allow-missing-freeze
#                     proceed even when freeze-set.sh --check reports a
#                     mandated input missing (mechanics rehearsal only; the real
#                     freeze must carry every mandated input).
#   --rm              delete the scratch clone on exit (default: keep it and
#                     print its path so the L1 can inspect it).
#
# Guarantees
#   * the clone's toplevel is asserted equal to its own path before the first
#     commit, and every later git call names the clone with -C;
#   * the commit identity `rehearsal <r@r.invalid>` is passed per command with
#     -c, never written to any config, and never used outside the clone;
#   * the lane repository is only cloned from and read (git clone, rev-parse,
#     the freeze-set copy loop) — no lane ref, index or worktree byte changes;
#   * all scratch lives under --scratch (no literal /tmp anywhere);
#   * counters run with HYAKU_SCRATCH and TMPDIR pointing into the same scratch,
#     and with --work inside it.
#
# Exit: 0 both counters ran; 2 setup error (clone, freeze set, missing counter);
# 3 apply-landing refused the draft set (this is the expected outcome for an
# empty draft set, and is printed as REFUSED).

set -u

L=/home/vgpnk/Projects/shokunin/kotodama-shokunin
BASE=98c486bdb4650ba5b8e651d332910e8ee60ad121
SCRATCH=${HYAKU_SCRATCH:-/fast/scratch/hyaku/kotodama-r76}
SUB=L1-rehearse
# Where this script and its sibling tools live: the installed wave directory
# (.ufo/waves/round-76/) at the freeze, or the wave-1 stage directory when the
# tool set is rehearsed before installation.
HERE=$(CDPATH='' cd -- "$(dirname -- "$0")" && pwd) || exit 2
W=${REHEARSE_TOOLS:-$HERE}
# The draft set is always a lane path: wave 2 assembles it in w2/stage.
DRAFTS=$L/.ufo/waves/round-76/w2/stage
COMBINED=
MANIFEST=
ALLOW_MISSING=0
RM=0
FL=/home/vgpnk/Projects/shokunin

while [ $# -gt 0 ]; do
  case $1 in
    --base)
      shift; [ $# -gt 0 ] || { echo "rehearse.sh: --base needs a revision" >&2; exit 2; }
      BASE=$1 ;;
    --base=*) BASE=${1#--base=} ;;
    --drafts)
      shift; [ $# -gt 0 ] || { echo "rehearse.sh: --drafts needs a directory" >&2; exit 2; }
      DRAFTS=$1 ;;
    --drafts=*) DRAFTS=${1#--drafts=} ;;
    --scratch)
      shift; [ $# -gt 0 ] || { echo "rehearse.sh: --scratch needs a directory" >&2; exit 2; }
      SCRATCH=$1 ;;
    --scratch=*) SCRATCH=${1#--scratch=} ;;
    --combined)
      shift; [ $# -gt 0 ] || { echo "rehearse.sh: --combined needs a revision" >&2; exit 2; }
      COMBINED=$1 ;;
    --combined=*) COMBINED=${1#--combined=} ;;
    --manifest)
      shift; [ $# -gt 0 ] || { echo "rehearse.sh: --manifest needs a file" >&2; exit 2; }
      MANIFEST=$1 ;;
    --manifest=*) MANIFEST=${1#--manifest=} ;;
    --allow-missing-freeze) ALLOW_MISSING=1 ;;
    --rm) RM=1 ;;
    -h|--help) sed -n '2,38p' "$0"; exit 0 ;;
    *) echo "rehearse.sh: unknown argument: $1" >&2; exit 2 ;;
  esac
  shift
done

case $BASE in
  *[!0-9a-f]*|'') echo "rehearse.sh: --base must be 40 hex, got '$BASE'" >&2; exit 2 ;;
esac
[ ${#BASE} -eq 40 ] || { echo "rehearse.sh: --base must be 40 hex, got '$BASE'" >&2; exit 2; }

TOP=$(git -C "$L" rev-parse --show-toplevel 2>/dev/null) || {
  echo "rehearse.sh: $L is not a git worktree" >&2; exit 2; }
[ "$TOP" = "$L" ] || {
  echo "rehearse.sh: $L is not a worktree toplevel (git says $TOP)" >&2; exit 2; }
git -C "$L" cat-file -e "$BASE^{commit}" 2>/dev/null || {
  echo "rehearse.sh: base $BASE is not a commit in $L" >&2; exit 2; }
[ -f "$W/apply-landing.py" ] || {
  echo "rehearse.sh: missing $W/apply-landing.py" >&2; exit 2; }
[ -f "$W/freeze-set.sh" ] || {
  echo "rehearse.sh: missing $W/freeze-set.sh" >&2; exit 2; }

S=$SCRATCH/$SUB
rm -rf -- "$S"
mkdir -p "$S/tmp" "$S/work" || exit 2
D=$S/lane

git clone -q --shared "$L" "$D" || { echo "rehearse.sh: clone failed" >&2; exit 2; }
DTOP=$(git -C "$D" rev-parse --show-toplevel 2>/dev/null) || {
  echo "rehearse.sh: clone has no worktree toplevel" >&2; exit 2; }
[ "$DTOP" = "$D" ] || {
  echo "rehearse.sh: clone toplevel '$DTOP' != '$D'; refusing to commit" >&2; exit 2; }

git -C "$D" checkout -q -B main "$BASE" || {
  echo "rehearse.sh: cannot check the clone out at base $BASE" >&2; exit 2; }

# --- freeze -----------------------------------------------------------------
sh "$W/freeze-set.sh" --root "$L" > "$S/freeze.list" || {
  echo "rehearse.sh: freeze-set.sh failed" >&2; exit 2; }
if ! sh "$W/freeze-set.sh" --root "$L" --check > /dev/null 2> "$S/freeze-check.txt"; then
  cat "$S/freeze-check.txt" >&2
  if [ "$ALLOW_MISSING" = 1 ]; then
    echo "rehearse.sh: WARNING mandated freeze inputs missing (--allow-missing-freeze)" >&2
  else
    echo "rehearse.sh: refusing to build the freeze commit: mandated inputs missing" >&2
    exit 2
  fi
fi

while IFS= read -r p; do
  [ -n "$p" ] || continue
  mkdir -p "$D/$(dirname "$p")" || exit 2
  cp "$L/$p" "$D/$p" || { echo "rehearse.sh: cannot copy $p" >&2; exit 2; }
done < "$S/freeze.list"

G="git -C $D -c user.name=rehearsal -c user.email=r@r.invalid -c commit.gpgsign=false"
# shellcheck disable=SC2086  # G is a deliberate command prefix
$G add -A > /dev/null || { echo "rehearse.sh: clone add failed" >&2; exit 2; }
# shellcheck disable=SC2086
$G commit -qm "round-76 freeze (rehearsal)" || {
  echo "rehearse.sh: freeze commit failed (empty freeze set?)" >&2; exit 2; }
F=$(git -C "$D" rev-parse HEAD) || exit 2
echo "freeze: F=$F base=$BASE files=$(wc -l < "$S/freeze.list")"

# --- landings ---------------------------------------------------------------
MANIFEST_OPT=
[ -n "$MANIFEST" ] && MANIFEST_OPT="--manifest $MANIFEST"

apply_claim() {
  claim=$1
  echo "--- apply-landing --claim $claim --drafts $DRAFTS${MANIFEST:+ --manifest $MANIFEST}"
  # shellcheck disable=SC2086  # MANIFEST_OPT is a deliberate two-word option pair
  python3 -B "$W/apply-landing.py" --root "$D" --claim "$claim" --drafts "$DRAFTS" $MANIFEST_OPT
  rc=$?
  if [ "$rc" -ne 0 ]; then
    echo "REFUSED: claim $claim landing — apply-landing.py exit $rc (drafts=$DRAFTS; freeze $F already committed on base $BASE)"
    return 3
  fi
  # shellcheck disable=SC2086
  $G add -A > /dev/null || return 2
  # shellcheck disable=SC2086
  $G commit -qm "$claim landing (rehearsal)" || return 2
  return 0
}

apply_claim ca
rc=$?
if [ "$rc" -ne 0 ]; then
  echo "rehearse: stopping after the freeze (no Ca landing); scratch kept at $S"
  [ "$RM" = 1 ] && rm -rf -- "$S"
  exit "$rc"
fi
CA=$(git -C "$D" rev-parse HEAD) || exit 2

apply_claim c
rc=$?
if [ "$rc" -ne 0 ]; then
  echo "rehearse: stopping after the Ca landing CA=$CA; scratch kept at $S"
  [ "$RM" = 1 ] && rm -rf -- "$S"
  exit "$rc"
fi
C=$(git -C "$D" rev-parse HEAD) || exit 2

echo "F=$F CA=$CA C=$C D=$D"

# --- measurement ------------------------------------------------------------
for c in reports/round-76/accept-c.py reports/round-76/accept-ca.py; do
  [ -f "$D/$c" ] || {
    echo "rehearse: no freeze-installed counter at $c in the clone; stopping before measurement" >&2
    echo "rehearsal ok: base=$BASE F=$F CA=$CA C=$C D=$D"
    [ "$RM" = 1 ] && rm -rf -- "$S"
    exit 2
  }
done

cd "$D" || exit 2
[ -n "$COMBINED" ] || COMBINED=$C

echo "--- Ca at CA ($CA)"
HYAKU_SCRATCH="$S" TMPDIR="$S/tmp" python3 -B reports/round-76/accept-ca.py \
    --root . --lands "$CA" --freeze "$F" --fleet-root "$FL" \
    --combined "$COMBINED" --work "$S/work/ca" > "$S/ca.out" 2>&1
rc=$?
grep -E '^LEG|^ACCEPT' "$S/ca.out" | cut -c1-260
echo "ca counter exit=$rc (full output $S/ca.out)"

git -C "$D" branch -f main "$C" > /dev/null 2>&1
git -C "$D" checkout -q main

echo "--- C at C ($C)"
HYAKU_SCRATCH="$S" TMPDIR="$S/tmp" python3 -B reports/round-76/accept-c.py \
    --root . --lands "$C" --freeze "$F" --fleet-root "$FL" \
    --work "$S/work/c" > "$S/c.out" 2>&1
rc=$?
grep -E '^LEG|^ACCEPT|^     ' "$S/c.out" | cut -c1-260
echo "c counter exit=$rc (full output $S/c.out)"

if [ "$RM" = 1 ]; then
  rm -rf -- "$S"
else
  echo "scratch kept at $S (delete with --rm)"
fi
exit 0
