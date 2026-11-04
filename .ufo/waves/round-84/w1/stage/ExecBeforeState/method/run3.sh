#!/usr/bin/env bash
# Normalised copy of the driver executed in this seat's scratch directory.
# Substitutions applied: the scratch root -> ${STAGE:?set STAGE to a writable dir},
# the lane repository -> ${LANE:?set LANE to the lane repository root}.
# The tip-materialisation revision is pinned to the measured lane tip.
#!/usr/bin/env bash
# ExecBeforeState — third pass: contract-vs-counter evidence, revision drift, dirt.
set -u
LANE=${LANE:?}
BASE=81499ee45b5751d388fefc78583810878de01ecd
R0=3ca2cf288fb593618e0559ea86a36e2dd3110eb8
R1=e160a72e4adf1620e09f812b913d4ece0fcd5243
R2=7e6ee2f8f7b54dbeecf42cfe96050e533a86a6e2
S=${STAGE:?}
RAW=$S/raw

r() {
  local id=$1 cwd=$2 cmd=$3 rc
  printf '%s\t%s\t%s\n' "$id" "$cwd" "$cmd" >> "$S/index.tsv"
  ( cd "$cwd" && eval "$cmd" ) > "$RAW/$id.stdout" 2> "$RAW/$id.stderr"
  rc=$?
  printf '%s\n' "$rc" > "$RAW/$id.rc"
  printf '%-6s rc=%-3s out=%sB\n' "$id" "$rc" "$(wc -c < "$RAW/$id.stdout")"
}

r P1b "$LANE" 'git status --porcelain'
r P1c "$LANE" 'git rev-list --count 3ca2cf288fb593618e0559ea86a36e2dd3110eb8..HEAD'

echo "== contract vs counter =="
r X1 "$LANE" 'git show 7e6ee2f8f7b54dbeecf42cfe96050e533a86a6e2:reports/round-84/claims.json | grep -c "\-\-selftest"'
r X2 "$LANE" 'git show 7e6ee2f8f7b54dbeecf42cfe96050e533a86a6e2:reports/round-84/accept-o84.py | grep -n "\"--selftest\""'
r X3 "$LANE" 'git show 7e6ee2f8f7b54dbeecf42cfe96050e533a86a6e2:reports/round-84/accept-o84.py | grep -n "SOUNDLAW_ERROR"'
r X4 "$LANE" 'git show 3ca2cf288fb593618e0559ea86a36e2dd3110eb8:reports/round-84/claims.json | grep -n "decision_heading\|\"anchors_heading\""'
r X5 "$LANE" 'git show 7e6ee2f8f7b54dbeecf42cfe96050e533a86a6e2:reports/round-84/claims.json | grep -n "decision_heading\|\"anchors_heading\""'
r X6 "$LANE" 'git show 7e6ee2f8f7b54dbeecf42cfe96050e533a86a6e2:reports/round-84/claims.json | grep -n "\"shape_markers\"" -A 4'
r X7 "$LANE" 'git show 7e6ee2f8f7b54dbeecf42cfe96050e533a86a6e2:reports/round-84/accept-o84.py | grep -c "min_trace_columns\|semantics"'
r X8 "$LANE" 'git show 7e6ee2f8f7b54dbeecf42cfe96050e533a86a6e2:reports/round-84/claims.json | grep -n "min_trace_columns\|\"semantics\""'
r X9 "$LANE" 'git show 7e6ee2f8f7b54dbeecf42cfe96050e533a86a6e2:reports/round-84/accept-d84.py | grep -n "SID = \|ROW_LINE = \|LINT_SUMMARY = "'
r X10 "$LANE" 'git show 7e6ee2f8f7b54dbeecf42cfe96050e533a86a6e2:reports/round-84/accept-d84.py | sed -n "163,180p"'
r X11 "$LANE" 'git show 7e6ee2f8f7b54dbeecf42cfe96050e533a86a6e2:reports/round-84/counterlib.py | sed -n "138,156p"'
r X12 "$LANE" 'git show 7e6ee2f8f7b54dbeecf42cfe96050e533a86a6e2:reports/round-84/accept-d84.py | sed -n "204,222p"'
r X13 "$LANE" 'git show 7e6ee2f8f7b54dbeecf42cfe96050e533a86a6e2:reports/round-84/accept-o84.py | sed -n "197,215p"'
r X14 "$LANE" 'git show 7e6ee2f8f7b54dbeecf42cfe96050e533a86a6e2:reports/round-84/claims.json | grep -n "min_selftest_checks\|min_changes\|min_rules_fired\|min_decision_rows\|min_anchors"'
r X15 "$LANE" 'git show 7e6ee2f8f7b54dbeecf42cfe96050e533a86a6e2:reports/round-84/claims.json | grep -n "\"own_paths\"" -A 3'
r X16 "$LANE" 'git diff --stat 3ca2cf288fb593618e0559ea86a36e2dd3110eb8 7e6ee2f8f7b54dbeecf42cfe96050e533a86a6e2 -- reports/round-84'
r X17 "$LANE" 'git log --oneline 3ca2cf288fb593618e0559ea86a36e2dd3110eb8..7e6ee2f8f7b54dbeecf42cfe96050e533a86a6e2'

echo "done: $(wc -l < "$S/index.tsv") entries"
