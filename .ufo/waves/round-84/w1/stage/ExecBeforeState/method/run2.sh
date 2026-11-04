#!/usr/bin/env bash
# Normalised copy of the driver executed in this seat's scratch directory.
# Substitutions applied: the scratch root -> ${STAGE:?set STAGE to a writable dir},
# the lane repository -> ${LANE:?set LANE to the lane repository root}.
# The tip-materialisation revision is pinned to the measured lane tip.
#!/usr/bin/env bash
# ExecBeforeState — second pass: exact counter BEFORE legs, gate at base, content sweeps.
set -u
LANE=${LANE:?}
BASE=81499ee45b5751d388fefc78583810878de01ecd
FREEZE=3ca2cf288fb593618e0559ea86a36e2dd3110eb8
S=${STAGE:?}
RAW=$S/raw
mkdir -p "$RAW" "$S/base"

r() {
  local id=$1 cwd=$2 cmd=$3 rc
  printf '%s\t%s\t%s\n' "$id" "$cwd" "$cmd" >> "$S/index.tsv"
  ( cd "$cwd" && eval "$cmd" ) > "$RAW/$id.stdout" 2> "$RAW/$id.stderr"
  rc=$?
  printf '%s\n' "$rc" > "$RAW/$id.rc"
  printf '%-6s rc=%-3s out=%sB\n' "$id" "$rc" "$(wc -c < "$RAW/$id.stdout")"
}

echo "== provenance (cont.) =="
r P5 "$LANE" 'git cat-file -e 81499ee45b5751d388fefc78583810878de01ecd:reports/round-84/claims.json'
r P6 "$LANE" 'git merge-base --is-ancestor 81499ee45b5751d388fefc78583810878de01ecd HEAD'
r P7 "$LANE" 'git merge-base --is-ancestor 3ca2cf288fb593618e0559ea86a36e2dd3110eb8 HEAD'
r P8 "$LANE" 'git diff --stat 81499ee45b5751d388fefc78583810878de01ecd HEAD -- tools examples'
r P9 "$LANE" 'git diff --stat 81499ee45b5751d388fefc78583810878de01ecd HEAD -- SKILL.md'

echo "== exact frozen BEFORE legs =="
r B1 "$LANE" 'python3 -B ${STAGE:?}/probe_before_legs.py ${LANE:?} 81499ee45b5751d388fefc78583810878de01ecd'

echo "== content-level sound-law absence at base =="
r O1g "$LANE" 'git grep -liE "sound.?law|soundchange" 81499ee45b5751d388fefc78583810878de01ecd -- tools | wc -l'
r O1h "$LANE" 'git grep -liE "sound.?law|soundchange" 81499ee45b5751d388fefc78583810878de01ecd -- tools examples'
r O1i "$LANE" 'git grep -liE "sound.?law" 81499ee45b5751d388fefc78583810878de01ecd -- examples | wc -l'
r O1j "$LANE" 'git grep -liE "sound.?law|soundchange" 81499ee45b5751d388fefc78583810878de01ecd -- reports | wc -l'

echo "== gate registry at BASE =="
python3 -B "$S/materialize.py" "$LANE" "$BASE" "$S/base"
r O4g "$S/base" 'python3 -B tools/check-gate-registry.py --root .'
r O4h "$LANE" 'git ls-tree -r --name-only 81499ee45b5751d388fefc78583810878de01ecd -- reports | grep -cE "^reports/round-84/"'

echo "== D source rows in the working tree (seat-literal form) =="
r SW1 "$LANE" 'grep -c "| S914 |" corpus/SOURCES.md'
r SW2 "$LANE" 'grep -c "| S915 |" corpus/SOURCES.md'
r SW3 "$LANE" 'grep -c "| S916 |" corpus/SOURCES.md'
r SW4 "$LANE" 'grep -c "| S917 |" corpus/SOURCES.md'
r SW5 "$LANE" 'grep -cE "\| S91[4-7] \|" corpus/SOURCES.md'

echo "== regex-instrument validity (word boundary) =="
r V1 "$S" 'printf "%s\n" sandwich switch bewitched | grep -cE "\bwitch\b"'
r V2 "$S" 'printf "%s\n" "a witch" "witches" | grep -cE "\bwitch\b"'
r V3 "$LANE" 'git grep -c "switch" 81499ee45b5751d388fefc78583810878de01ecd -- corpus/knowledge | wc -l'
r V4 "$LANE" 'printf "%s\n" "witch mark" "witchcraft" "sorcery" | grep -cE "(witch|witchcraft|sorcer|sorcery|malefic)"'
r V5 "$LANE" 'git grep -cE "^- gap filled:.*(witch|witchcraft|sorcer|sorcery|malefic)" 81499ee45b5751d388fefc78583810878de01ecd -- corpus/knowledge'
r V6 "$LANE" 'git grep -nE "^- gap filled:.*\b(witch|witchcraft|sorcerer|sorcery|malefic)\b" 81499ee45b5751d388fefc78583810878de01ecd -- corpus/knowledge'
r V7 "$LANE" 'git grep -nE "^- gap filled:.*\b(witch|witchcraft|sorcerer|sorcery|malefic)\b" 81499ee45b5751d388fefc78583810878de01ecd -- corpus/knowledge | wc -l'

echo "done: $(wc -l < "$S/index.tsv") entries"
