#!/bin/sh
# Round-76 freeze set — the repo-relative paths the L1 installs at the freeze
# commit (kotodama, hyaku run 10, base 98c486bdb4650ba5b8e651d332910e8ee60ad121).
#
# usage: freeze-set.sh [--check] [--root <lane>]
#
#   (default)   print every listed path that exists now, sorted and unique, one
#               per line, so a caller can `for p in $(freeze-set.sh); do ...` and
#               copy each with `cp "$LANE/$p" "$CLONE/$p"`.
#   --check     additionally print `CHECK ok|MISSING <item>` per mandated input
#               to stderr and exit 1 when one is absent.  Stdout is unchanged.
#   --root DIR  the lane to read (default: the git worktree toplevel of this
#               script's own directory).
#
# Mandated core (wave-1 seat spec):
#   reports/round-76/{claims.json,ledger.json,accept-c.py,accept-ca.py,
#   fixtures/*.json,telemetry/{selftest-c,selftest-ca,census-start,gap-sweep}.txt}
# plus the by-document map, the collision-guard proof, the wave specs/registries
# and the w1/w2 evidence.
#
# Round-75 predecessor: .ufo/waves/round-75/freeze-set.sh (read, never edited).
# Differences: round token 76, the round-76 mandatory telemetry names, the
# collision guard inputs, the orchestration scripts and the counters, the
# w1/w3 evidence sweeps, and a --check mode that names every missing input
# instead of letting a short freeze pass silently.
#
# Read-only: no git verb here mutates anything and nothing outside stdout/stderr
# is written.

set -u

CHECK=0
ROOT=

while [ $# -gt 0 ]; do
  case $1 in
    --check) CHECK=1 ;;
    --root)
      shift
      [ $# -gt 0 ] || { echo "freeze-set.sh: --root needs a directory" >&2; exit 2; }
      ROOT=$1
      ;;
    --root=*) ROOT=${1#--root=} ;;
    -h|--help) sed -n '2,28p' "$0"; exit 0 ;;
    *) echo "freeze-set.sh: unknown argument: $1" >&2; exit 2 ;;
  esac
  shift
done

HERE=$(CDPATH='' cd -- "$(dirname -- "$0")" && pwd) || exit 2
if [ -z "$ROOT" ]; then
  ROOT=$(git -C "$HERE" rev-parse --show-toplevel 2>/dev/null) || {
    echo "freeze-set.sh: cannot derive the lane root from $HERE; pass --root" >&2
    exit 2
  }
fi
ROOT=$(CDPATH='' cd -- "$ROOT" && pwd) || exit 2
TOP=$(git -C "$ROOT" rev-parse --show-toplevel 2>/dev/null) || {
  echo "freeze-set.sh: $ROOT is not a git worktree" >&2
  exit 2
}
[ "$TOP" = "$ROOT" ] || {
  echo "freeze-set.sh: $ROOT is not a worktree toplevel (git says $TOP)" >&2
  exit 2
}

W=.ufo/waves/round-76

# The inputs a freeze is not a freeze without.  One per line; a trailing `*`
# turns the item into a glob that must match at least once under --check.
MANDATED='reports/round-76/claims.json
reports/round-76/ledger.json
reports/round-76/accept-c.py
reports/round-76/accept-ca.py
reports/round-76/fixtures/*.json
reports/round-76/telemetry/selftest-c.txt
reports/round-76/telemetry/selftest-ca.txt
reports/round-76/telemetry/census-start.txt
reports/round-76/telemetry/gap-sweep.txt
'"$W"'/assimilation/id-renumber-map.json
'"$W"'/assimilation/guard-proof/*
'"$W"'/w1/spec.json
'"$W"'/w1/dispatch.json
'"$W"'/w1/swarm-registry.json'

# _emit <path-or-glob>: print the path (repo-relative) when it exists on disk.
_emit() {
  case $1 in
    *'*'*)
      for _p in "$ROOT"/$1; do
        [ -f "$_p" ] || continue
        printf '%s\n' "${_p#"$ROOT"/}"
      done
      ;;
    *)
      [ -f "$ROOT/$1" ] && printf '%s\n' "$1"
      ;;
  esac
  return 0
}

# _emit_tree <dir>: every file under dir, minus python bytecode.
_emit_tree() {
  [ -d "$ROOT/$1" ] || return 0
  (
    cd "$ROOT" || exit 0
    find "$1" -type f ! -name '*.pyc' ! -path '*__pycache__*'
  )
}

list_all() {
  # 1. claim inputs: claims, ledger, counters, fixtures, the four pre-freeze
  #    telemetry receipts (round 75 also froze census-start; round 76 keeps it
  #    in the telemetry directory the claim names).
  _emit reports/round-76/claims.json
  _emit reports/round-76/ledger.json
  _emit reports/round-76/accept-c.py
  _emit reports/round-76/accept-ca.py
  _emit 'reports/round-76/fixtures/*.json'
  _emit reports/round-76/telemetry/selftest-c.txt
  _emit reports/round-76/telemetry/selftest-ca.txt
  _emit reports/round-76/telemetry/census-start.txt
  _emit reports/round-76/telemetry/gap-sweep.txt

  # 2. the by-document map and the collision-guard inputs the counters read.
  _emit "$W/assimilation/id-renumber-map.json"
  _emit "$W/assimilation/reg-ids"
  _emit "$W/assimilation/staged-ids"
  _emit "$W/assimilation/collisions"
  _emit "$W/assimilation/build-map.py"
  _emit "$W/assimilation/substitution-table.txt"
  _emit "$W/assimilation/collision-documents.txt"

  # 3. guard proof (the planted-collision artefacts).
  _emit "$W/assimilation/guard-proof/*"

  # 4. the pre-data claim and the orchestration scripts.
  _emit "$W/CLAIMS-DRAFT.md"
  _emit "$W/freeze-set.sh"
  _emit "$W/run-controls.sh"
  _emit "$W/rehearse.sh"
  _emit "$W/apply-landing.py"
  _emit "$W/manifest.example.json"
  _emit "$W/build-w1.py"
  _emit "$W/build-w2.py"
  _emit "$W/validate.sh"
  _emit "$W/w1.ready*"
  _emit "$W/w2.ready*"

  # 5. counters and fixtures the counters drive.
  _emit_tree "$W/counters"

  # 6. wave evidence: w1 (recon receipts and staged artefacts), w2 (landing
  #    parts and stage), w3 (verifier receipts) when present.
  _emit_tree "$W/w1"
  _emit_tree "$W/w2"
  _emit_tree "$W/w3"
}

list_all | LC_ALL=C sort -u

[ "$CHECK" = 1 ] || exit 0

rc=0
while IFS= read -r item; do
  [ -n "$item" ] || continue
  case $item in
    *'*'*)
      n=0
      for _p in "$ROOT"/$item; do
        [ -f "$_p" ] && n=$((n + 1))
      done
      if [ "$n" -gt 0 ]; then
        printf 'CHECK ok      %s (%s)\n' "$item" "$n" >&2
      else
        printf 'CHECK MISSING %s (no match)\n' "$item" >&2
        rc=1
      fi
      ;;
    *)
      if [ -f "$ROOT/$item" ]; then
        printf 'CHECK ok      %s\n' "$item" >&2
      else
        printf 'CHECK MISSING %s\n' "$item" >&2
        rc=1
      fi
      ;;
  esac
done <<EOF
$MANDATED
EOF

[ "$rc" = 0 ] && echo "freeze-set: all mandated inputs present" >&2 \
              || echo "freeze-set: mandated inputs missing (see CHECK MISSING)" >&2
exit "$rc"
