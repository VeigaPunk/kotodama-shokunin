#!/usr/bin/env bash
# Reproduces every registry, corpus, entry and census number in receipts.md from committed bytes.
# Usage: receipts.sh <lane-repo> <base-rev> <lands-rev> <scratch-dir>
set -eu
R=$1; B=$2; L=$3; S=$4; mkdir -p "$S/tmp"; export TMPDIR="$S/tmp"
git -C "$R" --no-pager show "$B:corpus/SOURCES.md" > "$S/SOURCES.B.md"
git -C "$R" --no-pager show "$L:corpus/SOURCES.md" > "$S/SOURCES.L.md"
for n in B L; do
  f="$S/SOURCES.$n.md"
  echo "[$n] registry rows:    $(grep -c '^| S[0-9]' "$f")"
  echo "[$n] tier A/B/C:       $(awk -F'|' '/^\| S[0-9]/{gsub(/^ +| +$/,"",$5); print $5}' "$f" | sort | uniq -c | awk '{printf "%s=%s ",$2,$1}')"
  echo "[$n] status:           $(awk -F'|' '/^\| S[0-9]/{gsub(/^ +| +$/,"",$9); print $9}' "$f" | sort | uniq -c | awk '{printf "%s=%s ",$2,$1}')"
done
awk -F'|' '/^\| S[0-9]+ /{ n=split($0,a,"|"); id=a[2]; gsub(/ /,"",id); line=""; for(i=3;i<n;i++){c=a[i]; gsub(/^ +| +$/,"",c); line=line c "\x1f"}; print id "\t" line }' "$S/SOURCES.B.md" | sort > "$S/cells.B.tsv"
awk -F'|' '/^\| S[0-9]+ /{ n=split($0,a,"|"); id=a[2]; gsub(/ /,"",id); line=""; for(i=3;i<n;i++){c=a[i]; gsub(/^ +| +$/,"",c); line=line c "\x1f"}; print id "\t" line }' "$S/SOURCES.L.md" | sort > "$S/cells.L.tsv"
echo "base ids absent at lands: $(comm -23 <(cut -f1 "$S/cells.B.tsv") <(cut -f1 "$S/cells.L.tsv") | wc -l)"
echo "new ids at lands:         $(comm -13 <(cut -f1 "$S/cells.B.tsv") <(cut -f1 "$S/cells.L.tsv") | tr '\n' ' ')"
echo "base rows cell-changed:   $(join -t $'\t' "$S/cells.B.tsv" "$S/cells.L.tsv" | awk -F'\t' '$2!=$3' | wc -l)"
echo "SOURCES.md deleted lines: $(diff "$S/SOURCES.B.md" "$S/SOURCES.L.md" | grep -c '^<')"
echo "SOURCES.md added lines:   $(diff "$S/SOURCES.B.md" "$S/SOURCES.L.md" | grep -c '^>')"
for d in B L; do :; done
