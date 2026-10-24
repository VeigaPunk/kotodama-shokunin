#!/bin/sh
# Rebuild the ACCEPT-C-66 fixture tree and replay every mutation probe.
# Deterministic: the fixture bytes below are the exact bytes the probes ran on.
set -eu
LANE=/home/vgpnk/Projects/shokunin/kotodama-shokunin
HERE=$(cd "$(dirname "$0")" && pwd)
CTL="$HERE/control"

rm -rf "$CTL"
git clone --shared --quiet "$LANE" "$CTL"
cp "$HERE/SOURCES.pristine.md" "$CTL/corpus/SOURCES.md"
cp "$HERE/ENTRY.pristine.md"   "$CTL/corpus/knowledge/culture-material/scent-perfume-aromatics-codes.md"
cp "$HERE/README.pristine.md"  "$CTL/corpus/README.md"

run() {
  set +e
  ( cd "$CTL" && python3 -B "$LANE/reports/round-66/accept-c.py" --root . )
  rc=$?
  set -e
  echo "EXIT=$rc"
}

echo "### baseline (pristine fixture)"
run

for m in "$HERE"/mut*.SOURCES.md; do
  echo "### $(basename "$m")"
  cp "$HERE/SOURCES.pristine.md" "$CTL/corpus/SOURCES.md"
  cp "$HERE/ENTRY.pristine.md"   "$CTL/corpus/knowledge/culture-material/scent-perfume-aromatics-codes.md"
  cp "$m" "$CTL/corpus/SOURCES.md"
  case "$(basename "$m")" in
    mut3c-purecopy-both*) cp "$HERE/mut3c-purecopy-both.entry.md" \
      "$CTL/corpus/knowledge/culture-material/scent-perfume-aromatics-codes.md" ;;
    mut3d-padded-both*)   cp "$HERE/mut3d-padded-both.entry.md" \
      "$CTL/corpus/knowledge/culture-material/scent-perfume-aromatics-codes.md" ;;
  esac
  run
done
