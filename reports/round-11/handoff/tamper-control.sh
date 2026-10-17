#!/usr/bin/env bash
# R11-O14 tamper control — falsifiability drill for the exercise's committed
# frozen baseline `reports/round-11/handoff/expected.json`
# (profile `kotodama-handoff-e2e/1`, written by
# `tools/exercise-handoff-e2e.py --freeze reports/round-11/handoff`).
#
# Every scenario runs in a fresh isolated copy of the repo (tools/examples/
# corpus/reports) under $TMPDIR (in-lane .scratch); the live tree is only read.
# The drill shows, on the committed bytes rather than on the tool's own
# fixtures, which tampering modes read could-not-evaluate (exit 2) and which
# read drift (exit 1) — never a silent pass.
#
# Usage:  bash reports/round-11/handoff/tamper-control.sh
# Exit:   0 when every scenario matched its expectation, 1 otherwise.
set -u

SELF="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$SELF/../../.." && pwd)"
EXERCISE="tools/exercise-handoff-e2e.py"
BASELINE="reports/round-11/handoff/expected.json"

export TMPDIR="$ROOT/.scratch"
WORK="$TMPDIR/o14-tamper"
rm -rf "$WORK"
mkdir -p "$WORK/tmp"
export TMPDIR="$WORK/tmp"

failures=0

report() {  # <scenario> <mutated> <observed-exit> <expected-exit> <code> <verdict>
  local scenario="$1" mutated="$2" got="$3" want="$4" code="$5" line="$6" verdict
  if [ "$got" = "$want" ]; then verdict="MATCH"; else verdict="MISMATCH"; failures=$((failures+1)); fi
  printf 'scenario: %s\n' "$scenario"
  printf '  mutated:       %s\n' "$mutated"
  printf '  observed exit: %s (expected %s)  %s\n' "$got" "$want" "$verdict"
  printf '  code:          %s\n' "$code"
  printf '  verdict line:  %s\n' "$line"
}

tree_copy() {  # $1 = destination; fresh isolated copy of every surface read
  local dest="$1"
  rm -rf "$dest"
  mkdir -p "$dest"
  for d in tools examples corpus reports; do cp -r "$ROOT/$d" "$dest/$d"; done
}

run_case() {  # $1 = tree, $2 = log; echoes exit code
  ( cd "$1" && python3 "$EXERCISE" ) >"$2" 2>&1
  echo $?
}

code_of() {  # first stable E2E-* code in a log, or '-' when the run was clean
  grep -o 'E2E-[A-Z-]*' "$1" | head -1 || true
}

verdict_of() { grep -m1 '^handoff-e2e: exit=' "$1" || tail -n 1 "$1"; }

echo "== R11-O14 tamper control =="
echo "root:      $ROOT"
echo "baseline:  $BASELINE ($(sha256sum "$ROOT/$BASELINE" | cut -d' ' -f1))"
echo "exercise:  $EXERCISE ($(sha256sum "$ROOT/$EXERCISE" | cut -d' ' -f1))"
echo "started:   $(date -Is)"
echo

# -- T0 positive control: the untouched copy passes ---------------------------
T="$WORK/t0"; tree_copy "$T"
code=$(run_case "$T" "$WORK/t0.log")
report "T0 positive control (untouched copy)" "none" "$code" 0 "$(code_of "$WORK/t0.log")" "$(verdict_of "$WORK/t0.log")"

# -- T1 absent baseline: could-not-evaluate (exit 2, E2E-BASELINE) ------------
T="$WORK/t1"; tree_copy "$T"
rm -f "$T/$BASELINE"
code=$(run_case "$T" "$WORK/t1.log")
report "T1 absent baseline" "$BASELINE removed" "$code" 2 "$(code_of "$WORK/t1.log")" "$(verdict_of "$WORK/t1.log")"

# -- T2 malformed baseline: could-not-evaluate (exit 2) -----------------------
T="$WORK/t2"; tree_copy "$T"
printf '{ not json\n' > "$T/$BASELINE"
code=$(run_case "$T" "$WORK/t2.log")
report "T2 malformed baseline (invalid JSON)" "$BASELINE truncated" "$code" 2 "$(code_of "$WORK/t2.log")" "$(verdict_of "$WORK/t2.log")"

# -- T3 baseline body edited: integrity digest refuses it (exit 2) ------------
T="$WORK/t3"; tree_copy "$T"
python3 - "$T/$BASELINE" <<'PY'
import json, sys
path = sys.argv[1]
doc = json.load(open(path, encoding="utf-8"))
doc["packet_sha256"] = "0" * 64
open(path, "w", encoding="utf-8").write(json.dumps(doc, indent=1, sort_keys=True) + "\n")
PY
code=$(run_case "$T" "$WORK/t3.log")
report "T3 baseline body edited (packet_sha256 -> 000…0)" "$BASELINE edited in place" "$code" 2 "$(code_of "$WORK/t3.log")" "$(verdict_of "$WORK/t3.log")"

# -- T4 read-set file deleted: could-not-evaluate (exit 2, E2E-ARTIFACT) ------
T="$WORK/t4"; tree_copy "$T"
rm -f "$T/corpus/lessons/round-6-sources/05.json"
code=$(run_case "$T" "$WORK/t4.log")
report "T4 read-set file deleted" "corpus/lessons/round-6-sources/05.json removed" "$code" 2 "$(code_of "$WORK/t4.log")" "$(verdict_of "$WORK/t4.log")"

# -- T5 read-set value edited: drift, mismatch (exit 1, E2E-DIGEST) -----------
T="$WORK/t5"; tree_copy "$T"
python3 - "$T/examples/culture-d2/typed-labels.d2.yml" <<'PY'
import json, sys
path = sys.argv[1]
doc = json.load(open(path, encoding="utf-8"))
def walk(node):
    if isinstance(node, dict):
        for key, value in node.items():
            if isinstance(value, str) and value and key not in ("canon",):
                node[key] = value + "x"; return True
            if walk(value): return True
    if isinstance(node, list):
        for index, value in enumerate(node):
            if isinstance(value, str) and value:
                node[index] = value + "x"; return True
            if walk(value): return True
    return False
walk(doc)
open(path, "w", encoding="utf-8").write(json.dumps(doc, indent=1))
PY
code=$(run_case "$T" "$WORK/t5.log")
report "T5 read-set value edited (one string in the typed-label projection)" \
  "examples/culture-d2/typed-labels.d2.yml value + x" "$code" 1 "$(code_of "$WORK/t5.log")" "$(verdict_of "$WORK/t5.log")"

# -- T6 gate script revised: read-set drift (exit 1) --------------------------
T="$WORK/t6"; tree_copy "$T"
printf '\n# tamper probe: revised gate revision\n' >> "$T/tools/gates/handoff-packet-check.py"
code=$(run_case "$T" "$WORK/t6.log")
report "T6 revised gate bytes (comment appended to the gate script)" \
  "tools/gates/handoff-packet-check.py + comment" "$code" 1 "$(code_of "$WORK/t6.log")" "$(verdict_of "$WORK/t6.log")"

# -- pin check over the committed baseline ------------------------------------
python3 - "$ROOT/$BASELINE" "$ROOT" <<'PY'
import hashlib, json, pathlib, sys
baseline = json.load(open(sys.argv[1], encoding="utf-8"))
root = pathlib.Path(sys.argv[2])
print()
print(f"pins: profile={baseline.get('profile')} expected_exit={baseline.get('expected_exit')} "
      f"packet_sha256={str(baseline.get('packet_sha256'))[:16]}…")
drifted = []
for rel, pin in sorted((baseline.get("inputs") or {}).items()):
    path = root / rel
    live = hashlib.sha256(path.read_bytes()).hexdigest() if path.is_file() else "MISSING"
    if live != pin:
        drifted.append(rel)
print(f"inputs: {len(baseline.get('inputs') or {})} pinned, {len(drifted)} drifted"
      + (f" -> {drifted}" if drifted else ""))
PY

echo
echo "finished: $(date -Is)"
if [ "$failures" -eq 0 ]; then
  echo "tamper-control: all scenarios matched their expectation"
  exit 0
fi
echo "tamper-control: $failures scenario(s) mismatched"
exit 1
