#!/usr/bin/env bash
# id-collision guard under test. Contract extraction pattern:
#   grep -oE '^ {0,3}\|[[:space:]]*S[0-9]{3,}'
set -euo pipefail

extract() {
  grep -oE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' "$1" \
    | grep -oE 'S[0-9]{3,}' \
    | sort -u
}

case "${1:-}" in
  extract)
    extract "$2"
    ;;
  intersect)
    comm -12 <(extract "$2") <(extract "$3")
    ;;
  *)
    echo "usage: guard.sh extract <registry-file> | guard.sh intersect <reg-file> <staged-file>" >&2
    exit 2
    ;;
esac
