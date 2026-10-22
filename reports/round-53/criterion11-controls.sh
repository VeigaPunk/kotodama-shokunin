#!/bin/sh
# Round-53 receipt for QUALITY criterion 11 "shown able to fail": the round-51 D argv and the
# round-52 C argv each pass (exit 0) on a scratch copy where one clause of their statement is false.
# Usage: sh reports/round-53/criterion11-controls.sh <lane-repo>   (read-only on the lane; scratch in mktemp)
set -u
LANE=${1:?lane repo}
T=$(mktemp -d)
trap 'rm -rf "$T"' EXIT

echo "## 1. round-51 claim D (pastoralism boundary table), tree 2b956d7"
mkdir "$T/r51" && git -C "$LANE" archive 2b956d7 | tar -x -C "$T/r51"
E=corpus/knowledge/culture-material/pastoralism-animal-husbandry.md
cd "$T/r51"
echo '$ (unmodified) sh -c '\''test "$(python3 -B reports/round-51/boundary-count.py)" = "rows=15 resolved=15 distinct=15"'\'''
python3 -B reports/round-51/boundary-count.py; test "$(python3 -B reports/round-51/boundary-count.py)" = "rows=15 resolved=15 distinct=15"; echo "exit $?"
grep -c '`numerals-and-measures.md:101`' "$E" | sed 's/^/anchor occurrences: /'
python3 - "$E" <<'PY'
import sys
p = sys.argv[1]
t = open(p, encoding="utf-8").read()
assert "`numerals-and-measures.md:101`" in t
open(p, "w", encoding="utf-8").write(t.replace("`numerals-and-measures.md:101`", "`linguistics/`", 1))
PY
echo '$ (one path:line anchor replaced by `linguistics/`; the statement says every row has a path:line anchor) same command'
python3 -B reports/round-51/boundary-count.py; test "$(python3 -B reports/round-51/boundary-count.py)" = "rows=15 resolved=15 distinct=15"; echo "exit $? (0 = the clause was not checked)"

echo
echo "## 2. round-52 claim C (speech-surrogates entry indexed in README), tree 6524184"
mkdir "$T/r52" && git -C "$LANE" archive 6524184 | tar -x -C "$T/r52"
cd "$T/r52"
python3 - <<'PY'
p = "corpus/README.md"
lines = open(p, encoding="utf-8").read().split("\n")
out = [l for l in lines if not l.startswith("- `speech-surrogates-whistled-drummed.md`")]
assert len(out) == len(lines) - 1
open(p, "w", encoding="utf-8").write("\n".join(out))
PY
echo '$ (README index row removed; the statement says the entry is indexed) the round-52 declared C argv'
python3 - <<'PY'
import json, subprocess
m = json.load(open("reports/round-52/separability-manifest.json"))
argv = [u for u in m["claims"] if u["id"] == "C"][0]["acceptance"]
r = subprocess.run(argv, capture_output=True, text=True)
print((r.stdout + r.stderr).strip())
print(f"exit {r.returncode} (0 = the clause was not checked)")
PY
echo '$ python3 -B reports/round-28/readme/sweep.py   (run on its own)'
python3 -B reports/round-28/readme/sweep.py | grep -E '^(rows|missing_from_index)'
python3 -B reports/round-28/readme/sweep.py >/dev/null; echo "exit $?"
