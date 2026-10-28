#!/bin/sh
# Round-76 orchestration selftest — the checks that need no claim data.
#
# usage: selftest.sh [--scratch DIR]
#
# Runs, and prints one `SELFTEST ok|FAIL <name>` line per check plus a final
# `SELFTEST: n/m`:
#
#   1. syntax      sh -n on freeze-set.sh, run-controls.sh, rehearse.sh
#   2. shellcheck  shellcheck -S warning on the three shell scripts (skipped
#                  with a printed note when shellcheck is not installed)
#   3. pycompile   python3 -m py_compile on apply-landing.py
#   4. no-tmp      no literal /tmp scratch root in any of the four tools
#   5. manifest    manifest.example.json parses as JSON and its own anchors
#                  compile as Python regexes
#   6. reject      apply-landing.py refuses a path-traversal draft (exit 3)
#   7. empty       rehearse.sh builds the freeze commit against an EMPTY draft
#                  set and then refuses the landing cleanly (exit 3, REFUSED)
#
# Scratch: <scratch>/selftest only, default ${HYAKU_SCRATCH:-/fast/scratch/
# hyaku/kotodama-r76}; removed on exit.  The lane repository is read only
# except for `git clone --shared` of it into the scratch dir.

set -u

HERE=$(CDPATH='' cd -- "$(dirname -- "$0")" && pwd) || exit 2
BASE=98c486bdb4650ba5b8e651d332910e8ee60ad121
SCRATCH=${HYAKU_SCRATCH:-/fast/scratch/hyaku/kotodama-r76}/selftest

while [ $# -gt 0 ]; do
  case $1 in
    --scratch)
      shift; [ $# -gt 0 ] || { echo "selftest.sh: --scratch needs a directory" >&2; exit 2; }
      SCRATCH=$1 ;;
    --scratch=*) SCRATCH=${1#--scratch=} ;;
    *) echo "selftest.sh: unknown argument: $1" >&2; exit 2 ;;
  esac
  shift
done

rm -rf -- "$SCRATCH"
mkdir -p "$SCRATCH" || exit 2
trap 'rm -rf -- "$SCRATCH"' EXIT

n=0
ok=0
pass() { n=$((n + 1)); ok=$((ok + 1)); echo "SELFTEST ok   $1"; }
fail() { n=$((n + 1)); echo "SELFTEST FAIL $1"; }

# 1. syntax
bad=
for f in freeze-set.sh run-controls.sh rehearse.sh selftest.sh; do
  sh -n "$HERE/$f" || bad="$bad $f"
done
[ -z "$bad" ] && pass "syntax (sh -n on four scripts)" || fail "syntax:$bad"

# 2. shellcheck
if command -v shellcheck > /dev/null 2>&1; then
  if shellcheck -S warning "$HERE/freeze-set.sh" "$HERE/run-controls.sh" \
       "$HERE/rehearse.sh" "$HERE/selftest.sh" > "$SCRATCH/shellcheck.txt" 2>&1; then
    pass "shellcheck -S warning (clean)"
  else
    fail "shellcheck -S warning (see $SCRATCH/shellcheck.txt)"
    cat "$SCRATCH/shellcheck.txt"
  fi
else
  echo "SELFTEST skip shellcheck (not installed)"
fi

# 3. pycompile
if PYTHONPYCACHEPREFIX="$SCRATCH/pyc" python3 -m py_compile "$HERE/apply-landing.py"; then
  pass "py_compile apply-landing.py"
else
  fail "py_compile apply-landing.py"
fi

# 4. no literal /tmp scratch root.  The pattern is assembled from parts so this
#    script does not itself contain the byte sequence it forbids.
P=$(printf '/%s' tmp)
PAT="\"$P|$P/"
if grep -nE "$PAT" "$HERE/freeze-set.sh" "$HERE/run-controls.sh" \
     "$HERE/rehearse.sh" "$HERE/apply-landing.py" > "$SCRATCH/tmpgrep.txt" 2>&1; then
  fail "literal /tmp found:"
  cat "$SCRATCH/tmpgrep.txt"
else
  pass "no literal /tmp scratch root"
fi

# 5. example manifest
if python3 - "$HERE/manifest.example.json" <<'PY'
import json, re, sys
doc = json.load(open(sys.argv[1], encoding="utf-8"))
assert doc["round"] == 76, doc.get("round")
assert sorted(doc["claims"]) == ["c", "ca"], sorted(doc["claims"])
for claim in doc["claims"].values():
    for op in claim["ops"]:
        if "anchor" in op:
            re.compile(op["anchor"])
sys.exit(0)
PY
then
  pass "manifest.example.json parses, round 76, anchors compile"
else
  fail "manifest.example.json"
fi

# 6. a traversal draft is refused (against a throwaway git fixture: --root must
#    be a worktree toplevel, and the lane itself is refused by design)
FIX=$SCRATCH/fixture
mkdir -p "$FIX/corpus"
git -C "$FIX" init -q
if [ "$(git -C "$FIX" rev-parse --show-toplevel)" = "$FIX" ]; then
  :
else
  fail "fixture toplevel is not $FIX"
fi
D=$SCRATCH/traversal
mkdir -p "$D"
cat > "$D/manifest.json" <<'JSON'
{"round": 76, "claims": {"c": {"ops": [
  {"op": "copy", "from": "../escape.md", "to": "corpus/x.md"}]}}}
JSON
python3 -B "$HERE/apply-landing.py" --root "$FIX" --claim c --drafts "$D" \
    > "$SCRATCH/traversal.out" 2>&1
rc=$?
if [ "$rc" -eq 3 ] && grep -q '^REFUSED: .*escapes its base directory' "$SCRATCH/traversal.out"; then
  pass "traversal draft refused (exit 3)"
else
  fail "traversal draft: exit=$rc output=$(cat "$SCRATCH/traversal.out")"
fi

# 7. empty draft set: freeze builds, landing refuses
E=$SCRATCH/empty-drafts
mkdir -p "$E"
sh "$HERE/rehearse.sh" --base "$BASE" --drafts "$E" --allow-missing-freeze \
    --scratch "$SCRATCH/rehearse" > "$SCRATCH/rehearse-empty.out" 2>&1
rc=$?
if [ "$rc" -eq 3 ] && grep -q '^REFUSED: claim ca landing' "$SCRATCH/rehearse-empty.out" \
   && grep -q '^freeze: F=' "$SCRATCH/rehearse-empty.out"; then
  pass "empty drafts: freeze committed, landing refused (exit 3)"
else
  fail "empty drafts: exit=$rc"
  tail -20 "$SCRATCH/rehearse-empty.out"
fi

echo "SELFTEST: $ok/$n"
[ "$ok" = "$n" ] && exit 0 || exit 1
