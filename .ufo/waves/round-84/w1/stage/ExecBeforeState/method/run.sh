#!/usr/bin/env bash
# Normalised copy of the driver executed in this seat's scratch directory.
# Substitutions applied: the scratch root -> ${STAGE:?set STAGE to a writable dir},
# the lane repository -> ${LANE:?set LANE to the lane repository root}.
# The tip-materialisation revision is pinned to the measured lane tip.
#!/usr/bin/env bash
# ExecBeforeState — red-before receipts for claims D and O at the lane base.
set -u
LANE=${LANE:?}
BASE=81499ee45b5751d388fefc78583810878de01ecd
FREEZE=3ca2cf288fb593618e0559ea86a36e2dd3110eb8
S=${STAGE:?}
RAW=$S/raw
rm -rf -- "$RAW" "$S/head"
mkdir -p "$RAW" "$S/head"
: > "$S/index.tsv"

r() {
  local id=$1 cwd=$2 cmd=$3 rc
  printf '%s\t%s\t%s\n' "$id" "$cwd" "$cmd" >> "$S/index.tsv"
  ( cd "$cwd" && eval "$cmd" ) > "$RAW/$id.stdout" 2> "$RAW/$id.stderr"
  rc=$?
  printf '%s\n' "$rc" > "$RAW/$id.rc"
  printf '%-6s rc=%-3s out=%sB\n' "$id" "$rc" "$(wc -c < "$RAW/$id.stdout")"
}

echo "== provenance =="
r P0 "$LANE" 'git rev-parse HEAD'
r P0b "$LANE" 'date -u +%Y-%m-%dT%H:%M:%SZ'
r P0c "$LANE" 'git log --oneline -3'
r P1 "$LANE" 'git status --porcelain | wc -l'
r P2 "$LANE" 'git status --porcelain -- tools examples corpus SKILL.md reports/round-84 | wc -l'
r P3 "$LANE" 'git rev-parse 81499ee45b5751d388fefc78583810878de01ecd'
r P4 "$LANE" 'git rev-parse 3ca2cf288fb593618e0559ea86a36e2dd3110eb8'
r P5b "$LANE" 'git rev-parse e160a72e4adf1620e09f812b913d4ece0fcd5243'
r P5c "$LANE" 'git rev-parse 7e6ee2f8f7b54dbeecf42cfe96050e533a86a6e2'

echo "== D1 knowledge-file census at base =="
r D1a "$LANE" 'git ls-tree -r --name-only 81499ee45b5751d388fefc78583810878de01ecd -- corpus/knowledge | grep -c "\.md$"'
r D1b "$LANE" 'git ls-tree -r --name-only 81499ee45b5751d388fefc78583810878de01ecd -- corpus/knowledge | wc -l'
r D1c "$LANE" 'git ls-tree -r --name-only 81499ee45b5751d388fefc78583810878de01ecd -- corpus/knowledge | grep "\.md$" | cut -d/ -f3 | sort | uniq -c | sort -k2'
r D1d "$LANE" 'git diff --stat 81499ee45b5751d388fefc78583810878de01ecd HEAD -- corpus/knowledge'
r D1e "$LANE" 'find ${LANE:?}/corpus/knowledge -type f -name "*.md" | wc -l'

echo "== D2 registry-row census at base =="
r D2a "$LANE" 'git show 81499ee45b5751d388fefc78583810878de01ecd:corpus/SOURCES.md | grep -cE "^ {0,3}\| *S[0-9]{3,}"'
r D2b "$LANE" 'git show 81499ee45b5751d388fefc78583810878de01ecd:corpus/SOURCES.md | grep -cE "^ {0,3}\| *S[0-9]{3,} *\|"'
r D2c "$LANE" 'python3 -B ${STAGE:?}/probe_counter.py ${LANE:?} 81499ee45b5751d388fefc78583810878de01ecd'
r D2d "$LANE" 'git diff --stat 81499ee45b5751d388fefc78583810878de01ecd HEAD -- corpus/SOURCES.md'
r D2e "$LANE" 'git show 81499ee45b5751d388fefc78583810878de01ecd:corpus/SOURCES.md | grep -cE "^ *\|"'
r D2f "$LANE" 'git show 81499ee45b5751d388fefc78583810878de01ecd:corpus/SOURCES.md | grep -oE "^ {0,3}\| *S[0-9]{3,}" | grep -oE "S[0-9]+" | sort -V | tail -1'
r D2g "$LANE" 'git show 81499ee45b5751d388fefc78583810878de01ecd:corpus/SOURCES.md | grep -oE "^ {0,3}\| *S[0-9]{3,}" | grep -oE "S[0-9]+" | sort | uniq -d | wc -l'
r D2h "$LANE" 'git show 81499ee45b5751d388fefc78583810878de01ecd:corpus/SOURCES.md | grep -oE "^ {0,3}\| *S[0-9]{3,}" | grep -oE "S[0-9]+" | sort -V | head -1'

echo "== D3 four absences at base (ScoutGapWitch brief) =="
r D3a "$LANE" 'git ls-tree -r --name-only 81499ee45b5751d388fefc78583810878de01ecd -- corpus/knowledge | grep -icE "witch|witches|witchcraft|sorcer|sorcery|malefic"'
r D3b "$LANE" 'git ls-tree -r --name-only 81499ee45b5751d388fefc78583810878de01ecd -- corpus/knowledge | grep -iE "witch|witches|witchcraft|sorcer|sorcery|malefic"'
r D3c "$LANE" 'git grep -lE "^- topic: .{0,160}\b(witchcraft|sorcery|witch|sorcerer|malefic)" 81499ee45b5751d388fefc78583810878de01ecd -- corpus/knowledge'
r D3d "$LANE" 'git grep -lE "^- topic: .{0,160}\b(witchcraft|sorcery|witch|sorcerer|malefic)" 81499ee45b5751d388fefc78583810878de01ecd -- corpus/knowledge | wc -l'
r D3e "$LANE" 'git grep -niE "\b(witch|witches|witchcraft|sorcerer|sorcery|malefic)\b" 81499ee45b5751d388fefc78583810878de01ecd -- corpus/knowledge'
r D3f "$LANE" 'git grep -niE "\b(witch|witches|witchcraft|sorcerer|sorcery|malefic)\b" 81499ee45b5751d388fefc78583810878de01ecd -- corpus/knowledge | wc -l'
r D3g "$LANE" 'git grep -liE "\b(witch|witches|witchcraft|sorcerer|sorcery|malefic)\b" 81499ee45b5751d388fefc78583810878de01ecd -- corpus/knowledge | wc -l'
r D3h "$LANE" 'git grep -nE "^- gap filled:.*(witch|witchcraft|sorcer|sorcery|malefic)" 81499ee45b5751d388fefc78583810878de01ecd -- corpus/knowledge'
r D3i "$LANE" 'git grep -nE "^- gap filled:.*(witch|witchcraft|sorcer|sorcery|malefic)" 81499ee45b5751d388fefc78583810878de01ecd -- corpus/knowledge | wc -l'
r D3j "$LANE" 'git grep -c "^- topic:" 81499ee45b5751d388fefc78583810878de01ecd -- corpus/knowledge | wc -l'
r D3k "$LANE" 'git grep -c "^- gap filled:" 81499ee45b5751d388fefc78583810878de01ecd -- corpus/knowledge | wc -l'
r D3l "$LANE" 'git grep -liE "witch|witchcraft|sorcer|malefic" 81499ee45b5751d388fefc78583810878de01ecd -- corpus reports | wc -l'
r D3m "$LANE" 'git grep -liE "witch|witchcraft|sorcer|malefic" 81499ee45b5751d388fefc78583810878de01ecd -- corpus reports'

echo "== D3w the same four sweeps in the working tree, brief-literal form =="
r W1 "$LANE" 'find corpus/knowledge -name "*.md" | grep -icE "witch|witches|witchcraft|sorcer|sorcery|malefic"'
r W2 "$LANE" 'grep -rlE "^- topic: .{0,160}\b(witchcraft|sorcery|witch|sorcerer|malefic)" corpus/knowledge | wc -l'
r W3 "$LANE" 'grep -rniE "\b(witch|witches|witchcraft|sorcerer|sorcery|malefic)\b" corpus/knowledge | wc -l'
r W3b "$LANE" 'grep -rliE "\b(witch|witches|witchcraft|sorcerer|sorcery|malefic)\b" corpus/knowledge | wc -l'
r W4 "$LANE" 'grep -rnE "^- gap filled:.*(witch|witchcraft|sorcer|sorcery|malefic)" corpus/knowledge | wc -l'

echo "== D4 entry path absent at base =="
r D4a "$LANE" 'git cat-file -e 81499ee45b5751d388fefc78583810878de01ecd:corpus/knowledge/myth-symbol/witchcraft-sorcery-accusation-institution.md'
r D4b "$LANE" 'git ls-tree -r --name-only 81499ee45b5751d388fefc78583810878de01ecd -- corpus/knowledge/myth-symbol | wc -l'
r D4c "$LANE" 'test -e ${LANE:?}/corpus/knowledge/myth-symbol/witchcraft-sorcery-accusation-institution.md'
r D4d "$LANE" 'git ls-tree -r --name-only 81499ee45b5751d388fefc78583810878de01ecd -- corpus/knowledge/myth-symbol'

echo "== O1 tool/example absence at base =="
r O1a "$LANE" 'git ls-tree -r --name-only 81499ee45b5751d388fefc78583810878de01ecd -- tools examples | grep -ciE "sound.?law|soundchange"'
r O1b "$LANE" 'git ls-tree -r --name-only 81499ee45b5751d388fefc78583810878de01ecd -- tools examples | grep -iE "sound.?law|soundchange"'
r O1c "$LANE" 'git grep -liE "sound.?law|soundchange" 3ca2cf288fb593618e0559ea86a36e2dd3110eb8 -- reports | wc -l'
r O1d "$LANE" 'git grep -liE "sound.?law|soundchange" 3ca2cf288fb593618e0559ea86a36e2dd3110eb8 -- reports'
r O1e "$LANE" 'git grep -li "sound" 81499ee45b5751d388fefc78583810878de01ecd -- corpus/knowledge | wc -l'
r O1f "$LANE" 'git ls-tree -r --name-only 81499ee45b5751d388fefc78583810878de01ecd -- tools examples | wc -l'

echo "== O2 SOUNDLAWS marker absence at base =="
r O2a "$LANE" 'git grep -c SOUNDLAWS 81499ee45b5751d388fefc78583810878de01ecd -- tools examples reports'
r O2b "$LANE" 'git grep -c SOUNDLAWS 3ca2cf288fb593618e0559ea86a36e2dd3110eb8 -- tools examples reports'
r O2c "$LANE" 'git grep -l SOUNDLAWS 3ca2cf288fb593618e0559ea86a36e2dd3110eb8 -- tools examples reports'
r O2d "$LANE" 'git grep -c SOUNDLAW_ERROR 81499ee45b5751d388fefc78583810878de01ecd -- tools examples reports'

echo "== O3 examples/sound-laws absence at base =="
r O3a "$LANE" 'git ls-tree -r --name-only 81499ee45b5751d388fefc78583810878de01ecd -- examples/sound-laws | wc -l'
r O3b "$LANE" 'git ls-tree --name-only 81499ee45b5751d388fefc78583810878de01ecd:examples'
r O3c "$LANE" 'git cat-file -e 81499ee45b5751d388fefc78583810878de01ecd:examples/sound-laws'
r O3d "$LANE" 'git ls-tree -r --name-only 81499ee45b5751d388fefc78583810878de01ecd -- examples | wc -l'
r O3e "$LANE" 'git ls-tree -r --name-only 81499ee45b5751d388fefc78583810878de01ecd -- examples | cut -d/ -f2 | sort -u'
r O3f "$LANE" 'git cat-file -e 81499ee45b5751d388fefc78583810878de01ecd:tools/check-craft-exercise.py'

echo "== O4 gate registry at the lane tip =="
TIP=$(git -C "$LANE" rev-parse HEAD)
printf 'TIP=%s\n' "$TIP" > "$S/tip.txt"
python3 -B "$S/materialize.py" "$LANE" "$TIP" "$S/head"
r O4a "$S/head" 'python3 -B tools/check-gate-registry.py --root .'
r O4b "$LANE" 'python3 -B tools/check-gate-registry.py --root .'
r O4c "$LANE" 'git ls-tree -r --name-only 81499ee45b5751d388fefc78583810878de01ecd -- tools | wc -l'
r O4d "$LANE" 'git ls-tree -r --name-only 81499ee45b5751d388fefc78583810878de01ecd -- reports | grep -cE "^reports/round-[^/]+/accept-[^/]+\.py$"'
r O4e "$LANE" 'git show 81499ee45b5751d388fefc78583810878de01ecd:SKILL.md | grep -cE "^ {0,3}\|"'
r O4f "$LANE" 'git ls-tree -r --name-only 81499ee45b5751d388fefc78583810878de01ecd -- tools | grep -cE "^tools/[^/]+\.py$"'

echo "== S source-side row absence for S914-S917 =="
r S1 "$LANE" 'git show 81499ee45b5751d388fefc78583810878de01ecd:corpus/SOURCES.md | grep -c "| S914 |"'
r S2 "$LANE" 'git show 81499ee45b5751d388fefc78583810878de01ecd:corpus/SOURCES.md | grep -c "| S915 |"'
r S3 "$LANE" 'git show 81499ee45b5751d388fefc78583810878de01ecd:corpus/SOURCES.md | grep -c "| S916 |"'
r S4 "$LANE" 'git show 81499ee45b5751d388fefc78583810878de01ecd:corpus/SOURCES.md | grep -c "| S917 |"'
r S5 "$LANE" 'git show 81499ee45b5751d388fefc78583810878de01ecd:corpus/SOURCES.md | grep -cE "\| S91[4-7] \|"'
r S6 "$LANE" 'git show 81499ee45b5751d388fefc78583810878de01ecd:corpus/SOURCES.md | grep -cE "S91[4-9]|S9[2-9][0-9]"'
r S7 "$LANE" 'git show 81499ee45b5751d388fefc78583810878de01ecd:corpus/SOURCES.md | grep -c "S913"'
r S8 "$LANE" 'git show 81499ee45b5751d388fefc78583810878de01ecd:corpus/SOURCES.md | grep -E "^ {0,3}\| *S913"'
r S9 "$LANE" 'git show 81499ee45b5751d388fefc78583810878de01ecd:corpus/SOURCES.md | grep -E "^ {0,3}\| *S913" | awk -F"|" "{print NF-2}"'

echo "done: $(wc -l < "$S/index.tsv") entries"
r P0d "$LANE" 'git rev-parse HEAD'
r P0e "$LANE" 'date -u +%Y-%m-%dT%H:%M:%SZ'
