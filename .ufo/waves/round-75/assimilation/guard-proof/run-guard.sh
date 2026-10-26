#!/bin/sh
# CORPUS item-10 guard proof, round 75, seat ExecRenumber.
#
# The guard under test (prompt §6 item 10 / CORPUS.md):
#     ITEM10='^ {0,3}\|[[:space:]]*S[0-9]{3,}'
# The control pattern (the false-green the contract warns about):
#     COLZERO='^\|[[:space:]]*S[0-9]{3,}'
#
# For each fixture mirror (real registry at base + ONE planted row carrying a
# staged id that the lane does NOT hold at base, at a given indent):
#   1. the ITEM10 extractor lists the planted id  -> the guard SEES it
#   2. comm -12 (fixture reg-ids, staged-ids) names the planted id -> a real
#      staged-vs-lane collision is REPORTED
#   3. the COLZERO-only extractor misses the indented planted id
#   4. sources-census.sh census --file counts the planted row as a row (the
#      census parser accepts 0-3 leading spaces) and validate finds no new error
#
# The real registry is run last: the guard's own id lists, and the collision set.
#
# Usage: sh run-guard.sh <scratch-root> <out-dir>
set -u
ROOT=${1:?scratch root with the mirror trees}
OUT=${2:?output dir}
mkdir -p "$OUT"
LANE=/home/vgpnk/Projects/shokunin/kotodama-shokunin
STAGE=/home/vgpnk/Projects/shokuknow/merge/kotodama/SOURCES.append.md
CENSUS=/home/vgpnk/Projects/shokunin/scripts/sources-census.sh
ITEM10='^ {0,3}\|[[:space:]]*S[0-9]{3,}'
COLZERO='^\|[[:space:]]*S[0-9]{3,}'

# the staged id set, once
grep -oE "$ITEM10" "$STAGE" | grep -oE 'S[0-9]+' | sort -u > "$OUT/staged-ids"
cp "$OUT/staged-ids" "$ROOT/staged-ids"

run_one() {
  label=$1; reg=$2; plant=$3; indent=$4
  grep -oE "$ITEM10" "$reg" | grep -oE 'S[0-9]+' | sort -u > "$OUT/$label.reg-ids"
  comm -12 "$OUT/$label.reg-ids" "$OUT/staged-ids" > "$OUT/$label.collisions"
  grep -oE "$COLZERO" "$reg" | grep -oE 'S[0-9]+' | sort -u > "$OUT/$label.colzero-ids"
  "$CENSUS" census --file "$reg" > "$OUT/$label.census-rows.out" 2>&1
  census_rc=$?
  "$CENSUS" validate --file "$reg" > "$OUT/$label.census-validate.out" 2>&1
  validate_rc=$?
  {
    echo "### fixture=$label  registry=$reg"
    echo "planted id: $plant   indent: $indent leading char(s)"
    echo "ITEM10 reg-id count: $(wc -l < "$OUT/$label.reg-ids")"
    echo "ITEM10 sees the planted id: $(grep -c "^$plant$" "$OUT/$label.reg-ids")"
    echo "collision count (comm -12 reg-ids staged-ids): $(wc -l < "$OUT/$label.collisions")"
    echo "planted id listed in collisions: $(grep -c "^$plant$" "$OUT/$label.collisions")"
    echo "COLZERO id count: $(wc -l < "$OUT/$label.colzero-ids")"
    echo "COLZERO sees the planted id: $(grep -c "^$plant$" "$OUT/$label.colzero-ids")"
    echo "census rows line: $(grep -P '\trows\t' "$OUT/$label.census-rows.out" | head -1)"
    echo "census census exit: $census_rc"
    echo "census validate exit: $validate_rc"
    echo "census validate findings (E/W lines): $(grep -cE '^file[[:space:]]+[EW][0-9]+' "$OUT/$label.census-validate.out")"
  } > "$OUT/$label.summary.txt"
  cat "$OUT/$label.summary.txt"
}

for n in control 1sp 2sp 3sp 4sp tab; do
  case $n in
    control) plant="(none)"; indent=0 ;;
    1sp) plant=S985; indent="1 space" ;;
    2sp) plant=S986; indent="2 spaces" ;;
    3sp) plant=S987; indent="3 spaces" ;;
    4sp) plant=S988; indent="4 spaces" ;;
    tab) plant=S989; indent="1 tab" ;;
  esac
  run_one "$n" "$ROOT/mirror-$n/corpus/SOURCES.md" "$plant" "$indent"
done

# the real lane registry at base, and the real staged package
run_one real "$LANE/corpus/SOURCES.md" "(none)" 0
{
  echo "### the real collision set (lane registry at base vs the staged package)"
  echo "reg-ids count: $(wc -l < "$OUT/real.reg-ids")"
  echo "staged-ids count: $(wc -l < "$OUT/staged-ids")"
  echo "collisions count: $(wc -l < "$OUT/real.collisions")"
  echo "collisions: $(tr '\n' ' ' < "$OUT/real.collisions")"
  echo "adopted lane ids S885..S893 present in reg-ids: $(grep -cE '^S(88[5-9]|89[0-3])$' "$OUT/real.reg-ids")"
  echo "adopted lane ids S885..S893 present in collisions: $(grep -cE '^S(88[5-9]|89[0-3])$' "$OUT/real.collisions")"
} > "$OUT/real-collision-set.txt"
cat "$OUT/real-collision-set.txt"
