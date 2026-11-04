#!/usr/bin/env bash
set -u
B=c285b2afb19d4b64320e18df1f55e426bf2d0b0c
L=/home/vgpnk/Projects/shokunin/kotodama-shokunin
OUT=/fast/scratch/hyaku/kotodama-r82/ScoutGap/raw-transcript.txt
: > "$OUT"

show() { printf '$ %s\n' "$*" >> "$OUT"; }
done_() { printf '[exit %s]\n\n' "$1" >> "$OUT"; }

# knowledge: count matching lines per file, -icE
runk() {
  show "git -C $L grep -icE '$1' $B -- corpus/knowledge"
  git -C "$L" grep -icE "$1" "$B" -- corpus/knowledge >> "$OUT" 2>&1; done_ "$?"
}
# knowledge: matching lines, -inE
runkl() {
  show "git -C $L grep -inE '$1' $B -- corpus/knowledge"
  git -C "$L" grep -inE "$1" "$B" -- corpus/knowledge >> "$OUT" 2>&1; done_ "$?"
}
# knowledge: fixed-string count, -icF
runkF() {
  show "git -C $L grep -icF '$1' $B -- corpus/knowledge"
  git -C "$L" grep -icF "$1" "$B" -- corpus/knowledge >> "$OUT" 2>&1; done_ "$?"
}
# registry: matching lines, -inE / -inF
runs() {
  show "git -C $L grep -inE '$1' $B -- corpus/SOURCES.md"
  git -C "$L" grep -inE "$1" "$B" -- corpus/SOURCES.md >> "$OUT" 2>&1; done_ "$?"
}
runsF() {
  show "git -C $L grep -inF '$1' $B -- corpus/SOURCES.md"
  git -C "$L" grep -inF "$1" "$B" -- corpus/SOURCES.md >> "$OUT" 2>&1; done_ "$?"
}
sh_() {
  show "$1"
  bash -c "$1" >> "$OUT" 2>&1; done_ "$?"
}

printf 'BASE=%s\nLANE=%s\nDATE=%s\n\n' "$B" "$L" "$(date -Is)" >> "$OUT"

echo "## 1. filename sweep + positive controls" >> "$OUT"
sh_ "git -C $L ls-tree -r --name-only $B corpus/knowledge | grep -icE 'guest|hospital|xenia|hospitium|stranger'"
sh_ "git -C $L ls-tree -r --name-only $B corpus/knowledge | grep -c '\.md\$'"
sh_ "git -C $L ls-tree -r --name-only $B corpus/knowledge | wc -l"
sh_ "git -C $L ls-tree -r --name-only $B corpus/knowledge | grep -cE 'ritual'"
sh_ "git -C $L ls-tree -r --name-only $B corpus/knowledge | grep -iE 'cuisine|ritual-liminality'"

echo "## 2. topic sweep (xenia family)" >> "$OUT"
runk 'xenia|hospitium|guest-friend|guest-right|guest right|theoxeny|hospitality'
runkl 'xenia|hospitium|guest-friend|guest-right|guest right|theoxeny|hospitality'
runkl 'guest-right|guest right|guest-friend|hospitium|xenia|theoxeny'

echo "## 3. synonym sweep + method controls" >> "$OUT"
runk '\bguest'
runk '\bguest-'
runk '\bstranger'
runk '\bforeigner'
runk '\bsupplia'
runk '\basylum\b'
runk 'Zeus Xenios'
runk '\bxen(o|i)'
runk '\bhospit'
runk 'sacral legal|sacral-legal|sacred law'
runk 'theoxen'
runk 'Philemon|Baucis'
runkF 'van Gennep'

echo "## 4. registry duplicate-document probes" >> "$OUT"
runs 'pg1727|epub/1727|1727\.txt'
runs '(^|[^0-9])1727([^0-9]|$)'
runs 'Poetic_Edda'
runs '(^|[^0-9])26073([^0-9]|$)'
runs 'Britannica/Guest'
runs '\bOdyssey\b'
runs '\bHomer\b'
runs '\bButler\b'
runs '\bOvid\b'
runs '\bMetamorphoses\b'
runs 'Poetic Edda|Hovamol|Bellows'
runs 'Hav[aá]m[aá]l|Hovamol'
runs 'xenia|hospitium|guest-right|guest right|hospitality|theoxeny'
echo "--- positive controls (must hit) ---" >> "$OUT"
runsF 'gutenberg.org/cache/epub/73533'
runsF '1911_Encyclop%C3%A6dia_Britannica/Chess'
echo "--- target exact strings (must miss) ---" >> "$OUT"
runsF 'gutenberg.org/cache/epub/1727'
runsF 'gutenberg.org/cache/epub/26073'
runsF 'The_Poetic_Edda_(tr._Bellows)/Hovamol'
runsF '1911_Encyclop%C3%A6dia_Britannica/Guest'

echo "## 5. registry shape / id space" >> "$OUT"
sh_ "git -C $L show $B:corpus/SOURCES.md | grep -oE '^\\| S[0-9]+ ' | tr -d '| ' | sort -V | tail -1"
runs '^\| S90[4-7] '
sh_ "git -C $L show $B:corpus/SOURCES.md | awk -F'|' 'NF-2==11 && \$2 ~ /^ S[0-9]+ \$/ {n++} END {print n}'"
sh_ "git -C $L show $B:corpus/SOURCES.md | sed -n '349p'"

echo "## 6. nearest owners" >> "$OUT"
sh_ "git -C $L show $B:corpus/knowledge/myth-symbol/ritual-liminality.md | grep -nE '^-( topic| couples| gap filled| scope):'"
sh_ "git -C $L show $B:corpus/knowledge/culture-material/cuisine-food-lexicon.md | grep -nE '^-( topic| couples| gap filled| scope):'"
runkl 'hospital|guest|xenia'
sh_ "git -C $L show $B:corpus/knowledge/culture-material/cuisine-food-lexicon.md | grep -nE 'guest-right|salt covenant'"

echo "## 7. prior knowledge use of the planned works" >> "$OUT"
runkl '\bOdyssey\b|\bHomer\b|Hav[aá]m[aá]l|Hovamol|\bMetamorphoses\b|\bOvid\b'
runkl 'Philemon|Baucis|suppliant'

echo "## 8. layout" >> "$OUT"
sh_ "git -C $L ls-tree --name-only $B corpus/knowledge/"
sh_ "git -C $L ls-tree -r --name-only $B corpus/knowledge/myth-symbol"
