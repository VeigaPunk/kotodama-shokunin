#!/bin/sh
# RevMalformed (round-79 W1) reproduction. Scratch-only: every write goes under $WORK.
# Read-only against the lane: the counter source is `git show` of a pinned blob.
# Usage: sh repro.sh <explicit scratch dir>
set -eu
WORK="${1:?explicit scratch dir required}"
LANE=/home/vgpnk/Projects/shokunin/kotodama-shokunin
BASE=44f76d456c1b326a71ffdb381590af825cbf11be
STAGE="$LANE/.ufo/waves/round-79/w1/stage/RevMalformed"
mkdir -p "$WORK"
cd "$WORK"
git -C "$LANE" show "$BASE:reports/round-76/accept-ca.py" > "$WORK/r76-accept-ca.py"
echo "counter blob: $(git -C "$LANE" rev-parse "$BASE:reports/round-76/accept-ca.py")"
sha256sum "$WORK/r76-accept-ca.py"
python3 -B "$STAGE/build_fixtures.py" --work "$WORK/fx" --stage "$STAGE"
python3 -B "$STAGE/probe_malformed.py" --work "$WORK/fx" --stage "$STAGE" --counter-src "$WORK/r76-accept-ca.py"
