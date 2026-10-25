#!/bin/sh
# CORPUS item-10 guard proof: the exact guard pair on each mirror fixture and on
# the real registry, plus the column-zero-only control pattern and the census.
set -u
G=/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-74/assimilation/guard-proof
OUT="$G/out"; mkdir -p "$OUT"
S=/home/vgpnk/Projects/shokuknow
LANE=/home/vgpnk/Projects/shokunin/kotodama-shokunin
CENSUS=/home/vgpnk/Projects/shokunin/scripts/sources-census.sh
ITEM10='^ {0,3}\|[[:space:]]*S[0-9]{3,}'
COLZERO='^\|[[:space:]]*S[0-9]{3,}'

grep -oE "$ITEM10" "$S/merge/kotodama/SOURCES.append.md" | grep -oE 'S[0-9]+' | sort > "$G/staged-ids"

run_one() {
  label=$1; reg=$2
  grep -oE "$ITEM10" "$reg" | grep -oE 'S[0-9]+' | sort > "$OUT/$label.reg-ids"
  comm -12 "$OUT/$label.reg-ids" "$G/staged-ids" > "$OUT/$label.collisions"
  "$CENSUS" validate --file "$reg" > "$OUT/$label.census.out" 2>&1
  rc=$?
  "$CENSUS" census --file "$reg" > "$OUT/$label.census-rows.out" 2>&1
  {
    echo "### fixture=$label  registry=$reg"
    echo "census-mode rows line: $(grep -P '\trows\t' "$OUT/$label.census-rows.out" | head -1)"
    echo "ITEM10 reg-id count: $(wc -l < "$OUT/$label.reg-ids")"
    echo "ITEM10 sees planted S883: $(grep -c '^S883$' "$OUT/$label.reg-ids")"
    echo "collisions count: $(wc -l < "$OUT/$label.collisions")"
    echo "collisions: $(tr '\n' ' ' < "$OUT/$label.collisions")"
    echo "COLZERO pattern id count: $(grep -oE "$COLZERO" "$reg" | grep -oE 'S[0-9]+' | sort -u | wc -l)"
    echo "COLZERO pattern sees planted S883: $(grep -oE "$COLZERO" "$reg" | grep -oE 'S[0-9]+' | grep -c '^S883$')"
    echo "census --file exit: $rc"
    echo "census findings: $(grep -cE '^file[[:space:]]+[EW][0-9]+' "$OUT/$label.census.out")"
    echo "census E01 (malformed row): $(grep -c 'E01' "$OUT/$label.census.out")"
    echo "census E12 (row outside Registry): $(grep -c 'E12' "$OUT/$label.census.out")"
    echo "census lines naming S883: $(grep -c 'S883' "$OUT/$label.census.out")"
    echo "census verdict line: $(tail -1 "$OUT/$label.census.out")"
  } > "$OUT/$label.summary.txt"
  cat "$OUT/$label.summary.txt"
}

for n in control 2sp 3sp 4sp; do
  run_one "$n" "$G/mirror-$n/corpus/SOURCES.md"
done

grep -oE "$ITEM10" "$LANE/corpus/SOURCES.md" | grep -oE 'S[0-9]+' | sort > "$OUT/real.reg-ids"
comm -12 "$OUT/real.reg-ids" "$G/staged-ids" > "$OUT/real.collisions"
{
  echo "### real registry $LANE/corpus/SOURCES.md"
  echo "ITEM10 reg-id count: $(wc -l < "$OUT/real.reg-ids")"
  echo "ITEM10 sees any theme id S883/S884/S899/S900: $(grep -cE '^S(883|884|899|900)$' "$OUT/real.reg-ids")"
  echo "collisions count: $(wc -l < "$OUT/real.collisions")"
  echo "collisions: $(tr '\n' ' ' < "$OUT/real.collisions")"
  echo "collisions containing a theme id: $(grep -cE '^S(883|884|899|900)$' "$OUT/real.collisions")"
  echo "COLZERO pattern id count: $(grep -oE "$COLZERO" "$LANE/corpus/SOURCES.md" | grep -oE 'S[0-9]+' | sort -u | wc -l)"
} > "$OUT/real.summary.txt"
cat "$OUT/real.summary.txt"
