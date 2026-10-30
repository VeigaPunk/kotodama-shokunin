#!/bin/sh
# check-receipt-digest.sh — append-only digest check for a historical receipt.
# Usage: check-receipt-digest.sh <repo> <measured-rev> <receipt-path> <expected-git-blob-sha1> <expected-sha256>
# Exit 0: committed bytes at <measured-rev> match BOTH digests (original preserved).
# Exit 1: mismatch — the receipt at <measured-rev> is NOT the bound original (in-place rewrite detected).
# Exit 2: usage/input error (not a commit, path missing at rev).
set -u
repo=$1; rev=$2; path=$3; want_blob=$4; want_sha256=$5
cd "$repo" || exit 2
git rev-parse --verify --quiet "$rev^{commit}" >/dev/null || { echo "ERROR: $rev not a commit"; exit 2; }
git cat-file -e "$rev:$path" 2>/dev/null || { echo "ERROR: $path absent at $rev"; exit 2; }
got_blob=$(git rev-parse "$rev:$path")
got_sha256=$(git show "$rev:$path" | sha256sum | awk '{print $1}')
echo "receipt: $path @ $rev"
echo "git blob  expected=$want_blob got=$got_blob"
echo "sha256    expected=$want_sha256 got=$got_sha256"
if [ "$got_blob" = "$want_blob" ] && [ "$got_sha256" = "$want_sha256" ]; then
  echo "DIGEST: PASS original receipt preserved"
  exit 0
fi
echo "DIGEST: FAIL receipt bytes differ from bound original"
exit 1
