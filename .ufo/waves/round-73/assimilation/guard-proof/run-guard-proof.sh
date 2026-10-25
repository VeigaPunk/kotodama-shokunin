#!/usr/bin/env bash
# item-10 id-collision guard proof (round 73, seat ExecRenumber)
# Scratch only: every path written lives under $A/guard-proof.
# Three fixtures, one variable: whether the planted `  | S881 |` row is indented.
set -u
A=/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-73/assimilation
G=$A/guard-proof
L=/home/vgpnk/Projects/shokunin/kotodama-shokunin
S=/home/vgpnk/Projects/shokuknow
CENSUS=/home/vgpnk/Projects/shokunin/scripts/sources-census.sh
STAGED="$S/merge/kotodama/SOURCES.append.md"
COL0='^\|[[:space:]]*S[0-9]{3,}'          # column-zero-only control (broken pattern)
GUARD='^ {0,3}\|[[:space:]]*S[0-9]{3,}'   # CORPUS item-10 pattern

plant='  | S881 | Planted guard fixture (Enguehard 2022, ojs.unito.it article 7099) — https://ojs.unito.it/index.php/ricognizioni/article/view/7099 | paper | B | guard-proof fixture only, never a real registry row | Abstract + Keywords — fixture page as served 2026-10-25 | planted indented row proving the 0-3-space extractor; not corpus knowledge | queued | 2026-10-25 | 90d | — |'

# mirror/ is the "lane root" the census derives from --file: dirname(file)/..
# symlinks let E11 (used-by on disk) resolve without copying 13M of knowledge.
mkdir -p "$G/mirror/corpus" "$G/mirror-a3/corpus"
ln -sfn "$L/corpus/knowledge" "$G/mirror/corpus/knowledge"
ln -sfn "$L/corpus/lessons"   "$G/mirror/corpus/lessons"
ln -sfn "$L/SKILL.md"         "$G/mirror/SKILL.md"
ln -sfn "$L/corpus/knowledge" "$G/mirror-a3/corpus/knowledge"
ln -sfn "$L/corpus/lessons"   "$G/mirror-a3/corpus/lessons"
ln -sfn "$L/SKILL.md"         "$G/mirror-a3/SKILL.md"

extract() { # $1=pattern $2=file
  grep -oE "$1" "$2" | grep -oE 'S[0-9]+' | sort
}
collide() { # $1=regfile -> collisions on stdout
  local r=$1 c=$G/.reg.$$ s=$G/.stg.$$
  extract "$GUARD" "$r" > "$c"
  extract "$GUARD" "$STAGED" > "$s"
  comm -12 "$c" "$s"; rm -f "$c" "$s"
}

echo "## 0. inputs"
echo "lane registry : $L/corpus/SOURCES.md"
echo "staged package: $STAGED"
echo "census parser accepts 0-3 leading ASCII spaces (sources-census.sh:40-42; row_pass/usedby_findings use ^ {0,3})"
echo

echo "## 1. fixture A1 — unmodified copy (baseline, no planted row)"
cp "$L/corpus/SOURCES.md" "$G/mirror/corpus/SOURCES.md"
echo "census rows: $("$CENSUS" census --file "$G/mirror/corpus/SOURCES.md" | awk -F'\t' '$2=="rows"{print $3; exit}')"
"$CENSUS" validate --file "$G/mirror/corpus/SOURCES.md" --today 2026-10-25 > "$G/validate-A1.txt" 2>&1
echo "validate exit: $?  (E-codes: $(awk -F'\t' '$2 ~ /^E[0-9]+$/' "$G/validate-A1.txt" | wc -l); W-codes: $(awk -F'\t' '$2 ~ /^W[0-9]+$/' "$G/validate-A1.txt" | wc -l))"
extract "$COL0"  "$G/mirror/corpus/SOURCES.md" > "$G/A1.reg.col0";  extract "$GUARD" "$G/mirror/corpus/SOURCES.md" > "$G/A1.reg.guard"
extract "$COL0"  "$STAGED" > "$G/A1.stg.col0"; extract "$GUARD" "$STAGED" > "$G/A1.stg.guard"
comm -12 "$G/A1.reg.col0" "$G/A1.stg.col0"   > "$G/A1.collisions.col0"
comm -12 "$G/A1.reg.guard" "$G/A1.stg.guard" > "$G/A1.collisions.guard"
echo "A1 ids: reg.col0=$(wc -l < "$G/A1.reg.col0") reg.guard=$(wc -l < "$G/A1.reg.guard") staged=$(wc -l < "$G/A1.stg.guard")"
echo "A1 collisions: col0=$(wc -l < "$G/A1.collisions.col0") guard=$(wc -l < "$G/A1.collisions.guard") -> identical: $(cmp -s "$G/A1.collisions.col0" "$G/A1.collisions.guard" && echo yes || echo NO)"
echo

echo "## 2. fixture A2 — same copy + PLANTED INDENTED row (2 spaces) before the closing table"
anchor=$(grep -n '^| S875 |' "$G/mirror/corpus/SOURCES.md" | cut -d: -f1)
echo "S875 row at scratch line: $anchor"
gawk -v n="$anchor" -v row="$plant" 'NR==n{print; print row; next}{print}' \
  "$G/mirror/corpus/SOURCES.md" > "$G/mirror/corpus/SOURCES.md.tmp" && mv "$G/mirror/corpus/SOURCES.md.tmp" "$G/mirror/corpus/SOURCES.md"
echo "planted line, leading spaces + first 60 chars (cat -A):"
grep -n 'Planted guard fixture' "$G/mirror/corpus/SOURCES.md" | cut -c1-70 | cat -A
echo "leading-space count on planted line: $(grep 'Planted guard fixture' "$G/mirror/corpus/SOURCES.md" | sed -E 's/[^ ].*//' | awk '{print length($0)}')"
echo "census rows (parser sees the indented row): $("$CENSUS" census --file "$G/mirror/corpus/SOURCES.md" | awk -F'\t' '$2=="rows"{print $3; exit}')"
"$CENSUS" validate --file "$G/mirror/corpus/SOURCES.md" --today 2026-10-25 > "$G/validate-A2.txt" 2>&1
echo "validate exit: $?  (E-codes: $(awk -F'\t' '$2 ~ /^E[0-9]+$/' "$G/validate-A2.txt" | wc -l); W-codes: $(awk -F'\t' '$2 ~ /^W[0-9]+$/' "$G/validate-A2.txt" | wc -l))"
echo "validate findings naming S881 (must be none): $(grep -c 'S881' "$G/validate-A2.txt")"
extract "$COL0"  "$G/mirror/corpus/SOURCES.md" > "$G/A2.reg.col0";  extract "$GUARD" "$G/mirror/corpus/SOURCES.md" > "$G/A2.reg.guard"
comm -12 "$G/A2.reg.col0"  "$G/A1.stg.col0"  > "$G/A2.collisions.col0"
comm -12 "$G/A2.reg.guard" "$G/A1.stg.guard" > "$G/A2.collisions.guard"
echo "A2 ids: reg.col0=$(wc -l < "$G/A2.reg.col0") reg.guard=$(wc -l < "$G/A2.reg.guard") (guard must be +1)"
echo "A2 control (column-zero-only): sees S881? $(grep -c '^S881$' "$G/A2.reg.col0")  collisions=$(wc -l < "$G/A2.collisions.col0")"
echo "A2 guard   (0-3 spaces)     : sees S881? $(grep -c '^S881$' "$G/A2.reg.guard")  collisions=$(wc -l < "$G/A2.collisions.guard")"
echo "A2 delta (guard minus control):"; comm -13 "$G/A2.collisions.col0" "$G/A2.collisions.guard" | sed 's/^/  /'
echo

echo "## 3. fixture A3 — separability: copy with the 17 pre-existing colliding rows dropped, planted indented row kept"
# drop registry rows whose ids already collide (S859..S875), leaving the planted S881 as the only possible collision
cut -d' ' -f1 "$G/A1.collisions.guard" > "$G/A3.dropped-ids"
gawk 'BEGIN{while((getline l < "'"$G/A3.dropped-ids"'")>0) drop[l]=1}
      { line=$0; if (match(line, /^ {0,3}\|[ \t]*S[0-9]+/)) { id=substr(line, RSTART, RLENGTH); gsub(/^ {0,3}\|[ \t]*/, "", id); if (id in drop) next } print }' \
  "$G/mirror/corpus/SOURCES.md" > "$G/mirror-a3/corpus/SOURCES.md"
echo "A3 rows dropped: $(wc -l < "$G/A3.dropped-ids"); census rows: $("$CENSUS" census --file "$G/mirror-a3/corpus/SOURCES.md" | awk -F'\t' '$2=="rows"{print $3; exit}')"
"$CENSUS" validate --file "$G/mirror-a3/corpus/SOURCES.md" --today 2026-10-25 > "$G/validate-A3.txt" 2>&1
echo "validate exit: $?  (E-codes: $(awk -F'\t' '$2 ~ /^E[0-9]+$/' "$G/validate-A3.txt" | wc -l); W-codes: $(awk -F'\t' '$2 ~ /^W[0-9]+$/' "$G/validate-A3.txt" | wc -l))"
extract "$COL0"  "$G/mirror-a3/corpus/SOURCES.md" > "$G/A3.reg.col0"
extract "$GUARD" "$G/mirror-a3/corpus/SOURCES.md" > "$G/A3.reg.guard"
comm -12 "$G/A3.reg.col0"  "$G/A1.stg.col0"  > "$G/A3.collisions.col0"
comm -12 "$G/A3.reg.guard" "$G/A1.stg.guard" > "$G/A3.collisions.guard"
echo "A3 control (column-zero-only) collisions: $(wc -l < "$G/A3.collisions.col0") -> $(tr '\n' ' ' < "$G/A3.collisions.col0")"
echo "A3 guard   (0-3 spaces)      collisions: $(wc -l < "$G/A3.collisions.guard") -> $(tr '\n' ' ' < "$G/A3.collisions.guard")"
echo

echo "## 4. real pair (no fixture) — the item-10 command exactly as written in CORPUS.md"
grep -oE "$GUARD" "$L/corpus/SOURCES.md" | grep -oE 'S[0-9]+' | sort > "$A/reg-ids"
grep -oE "$GUARD" "$STAGED"              | grep -oE 'S[0-9]+' | sort > "$A/staged-ids"
comm -12 "$A/reg-ids" "$A/staged-ids" > "$A/collisions"
echo "reg-ids=$(wc -l < "$A/reg-ids") staged-ids=$(wc -l < "$A/staged-ids") collisions=$(wc -l < "$A/collisions")"
echo "real column-zero-only control collisions: $(extract "$COL0" "$L/corpus/SOURCES.md" | comm -12 - "$A/staged-ids" | wc -l) (identical -> no indented row hides a collision today)"
echo

echo "## 5. verdict"
fail=0
[ -s "$G/A1.collisions.guard" ] || { echo "FAIL: real baseline collisions empty"; fail=1; }
[ "$(wc -l < "$G/A2.collisions.guard")" -eq "$(( $(wc -l < "$G/A2.collisions.col0") + 1 ))" ] || { echo "FAIL: planted row did not add exactly one collision"; fail=1; }
[ "$(grep -c '^S881$' "$G/A2.reg.col0")" -eq 0 ] || { echo "FAIL: control saw the indented row"; fail=1; }
[ "$(grep -c '^S881$' "$G/A2.reg.guard")" -eq 1 ] || { echo "FAIL: guard missed the indented row"; fail=1; }
[ ! -s "$G/A3.collisions.col0" ] || { echo "FAIL: A3 control not empty"; fail=1; }
[ "$(wc -l < "$G/A3.collisions.guard")" -eq 1 ] || { echo "FAIL: A3 guard did not yield exactly S881"; fail=1; }
awk -F'\t' '$2 ~ /^E[0-9]+$/' "$G/validate-A2.txt" | grep -q . && { echo "FAIL: planted row raises an E-code (not census-valid)"; fail=1; }
[ "$fail" -eq 0 ] && echo "GUARD-PROOF: PASS"
exit "$fail"
