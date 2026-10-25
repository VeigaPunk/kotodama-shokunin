#!/usr/bin/env bash
# Round-72 scratch mirror: re-pin the admitted entries and re-run the registry append gate.
#
# Idempotent. Re-run this after ANY revision of /tmp/r72-entries/*.md — the mirror
# copies are pinned by sha256 in the output, so a stale mirror is visible at a glance.
#
#   bash refresh-and-validate.sh            # refresh + validate
#   bash refresh-and-validate.sh --no-copy  # validate the mirror as it stands
#
# Writes: <lane>/.ufo/waves/round-72/assimilation/validate/{entry-pins.txt,
#         census-validate-mirror.out,.err,.exit, checks.out, cited-lines-mirror.out,
#         gate-summary.txt}
# Exit:   0 all gates clean · 1 at least one gate failed · 2 mirror/entries missing
set -u
LANE=/home/vgpnk/Projects/shokunin/kotodama-shokunin
MIRROR=/tmp/r72-mirror
ENTRIES=/tmp/r72-entries
CENSUS=/home/vgpnk/Projects/shokunin/scripts/sources-census.sh
V=$LANE/.ufo/waves/round-72/assimilation/validate
MIR_FILE=$MIRROR/corpus/SOURCES.md
BASE=heritage-taxonomy-models.md
AMEND=heritage-taxonomy-models.amend-2026-10-24-r13.md
COPY=1
[ "${1:-}" = "--no-copy" ] && COPY=0

mkdir -p "$V" || exit 2
[ -f "$MIR_FILE" ] || { echo "MISSING mirror registry: $MIR_FILE" >&2; exit 2; }

if [ "$COPY" = 1 ]; then
  for f in "$BASE" "$AMEND"; do
    if [ -f "$ENTRIES/$f" ]; then
      cp -p "$ENTRIES/$f" "$MIRROR/corpus/knowledge/culture-material/$f" || exit 2
    else
      echo "MISSING admitted entry: $ENTRIES/$f (mirror keeps its previous copy)" >&2
    fi
  done
fi

{
  echo "entry pins (validated revision):"
  sha256sum "$MIRROR/corpus/knowledge/culture-material/$BASE" \
            "$MIRROR/corpus/knowledge/culture-material/$AMEND" 2>&1
  echo "source-of-copy: $ENTRIES (source sha256 below; a mismatch means the mirror is stale)"
  sha256sum "$ENTRIES/$BASE" "$ENTRIES/$AMEND" 2>&1
  echo "mirror registry: $(sha256sum "$MIR_FILE")"
  echo "lane registry (pre-append): $(sha256sum "$LANE/corpus/SOURCES.md")"
} >"$V/entry-pins.txt" 2>&1

status=0

bash "$CENSUS" validate --file "$MIR_FILE" >"$V/census-validate-mirror.out" 2>"$V/census-validate-mirror.err"
census_rc=$?
printf 'census validate --file %s -> exit=%s\n' "$MIR_FILE" "$census_rc" >"$V/census-validate-mirror.exit"
[ "$census_rc" = 0 ] || status=1

python3 -B "$V/checks.py" >"$V/checks.out" 2>&1
checks_rc=$?
[ "$checks_rc" = 0 ] || status=1

python3 -B "$LANE/tools/check-cited-lines.py" \
  "$MIRROR/corpus/knowledge/culture-material/$BASE" \
  "$MIRROR/corpus/knowledge/culture-material/$AMEND" \
  >"$V/cited-lines-mirror.out" 2>"$V/cited-lines-mirror.err"
cited_rc=$?
[ "$cited_rc" = 0 ] || status=1

{
  echo "ROUND-72 SCRATCH-MIRROR GATE — $(date -Iseconds)"
  echo "mirror registry: $MIR_FILE"
  echo "census validate --file: exit=$census_rc  E-findings=$(grep -cE '	E[0-9]+	' "$V/census-validate-mirror.out")  W-findings=$(grep -cE '	W[0-9]+	' "$V/census-validate-mirror.out")"
  echo "checks.py (NF!=13, dup ids, dup urls, id collision): exit=$checks_rc  $(grep -E '^RESULT:' "$V/checks.out")"
  echo "check-cited-lines.py over the two entries: exit=$cited_rc  $(tail -1 "$V/cited-lines-mirror.out")"
  echo "overall: $([ "$status" = 0 ] && echo PASS || echo FAIL)"
} >"$V/gate-summary.txt" 2>&1

cat "$V/gate-summary.txt"
exit "$status"
