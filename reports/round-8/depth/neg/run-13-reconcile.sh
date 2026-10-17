#!/bin/sh
# R8-D13 — re-runnable verifier for the negative fixture
# reports/round-8/depth/neg/packet-13.era-material-scope.yml.
#
# The fixture carries one plausible-but-unsupported era/material scope claim:
# GAR-R13-02, a coat of imported lowland plant-thread cloth, is declared at era
# E0 while the packet's own material record (CMAT-13-02) excludes E0 and routes
# the cloth only from E1. This script checks three things:
#
#   1. the D2 typed-labels reconciliation path flags the claim
#      (D2L-MATERIAL [reject], raw code R-MAT-ERA-EXCLUDED, on GAR-R13-02);
#   2. the clean control (GAR-R13-01, felt) gets no material finding, and a
#      corrected twin of the fixture (era E0 -> E1 on GAR-R13-02 only) loses
#      the finding — the flag is causally tied to the unsupported scope;
#   3. the frozen costume-era-consistency gate, run on the same fixture,
#      independently rejects the same record (MAT-02 [reject]).
#
# Expectations are about FINDING lines, not exit codes: every run of the tool
# also carries rank-conflict findings from its static rank-rule ledger, and
# some revisions carried tool-side D2L-DATA noise. Exit codes are printed.
#
# Read-only with respect to the repository except for the corrected twin
# written under scratch/. Usage: sh run-13-reconcile.sh
set -u

HERE=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
REPO=$(CDPATH= cd -- "$HERE/../../../.." && pwd)
TOOL="$REPO/tools/d2-typed-labels.py"
GATE="$REPO/tools/gates/costume-era-consistency-gate.py"
FIX="$HERE/packet-13.era-material-scope.yml"
SCRATCH="$HERE/scratch"
CORR="$SCRATCH/packet-13-corrected.yml"

failures=0
say() { printf '%s\n' "$*"; }
fail() { failures=$((failures + 1)); say "FAIL $*"; }

say "tool: $TOOL"
say "tool sha256: $(sha256sum "$TOOL" | cut -d' ' -f1)  (D02 owns this file; it was edited during round 8 — the digest pins the revision this run used)"
say "fixture: $FIX"
say "fixture sha256: $(sha256sum "$FIX" | cut -d' ' -f1)"
say ""

# --- 1. the claim is flagged ------------------------------------------------
say "== 1. tool on the fixture (the claim must be flagged) =="
python3 "$TOOL" --packet "$FIX" > "$SCRATCH/run-13-check.txt" 2>&1
rc=$?
say "exit: $rc"
grep -F "FINDING D2L-MATERIAL: [reject] GAR-R13-02" "$SCRATCH/run-13-check.txt" \
  || fail "expected 'FINDING D2L-MATERIAL: [reject] GAR-R13-02' not observed"
grep -F "CMAT-13-02 is not available in E0" "$SCRATCH/run-13-check.txt" \
  || fail "expected the exclusion detail not observed"
if grep -F "D2L-MATERIAL" "$SCRATCH/run-13-check.txt" | grep -F "GAR-R13-01" >/dev/null; then
  fail "the clean control GAR-R13-01 carries a material finding"
fi
say ""

# --- 2. corrected twin loses the finding ------------------------------------
say "== 2. corrected twin (era E0 -> E1 on GAR-R13-02 only; finding must disappear) =="
mkdir -p "$SCRATCH"
python3 - "$FIX" "$CORR" <<'PY'
import sys
from pathlib import Path
src, dst = Path(sys.argv[1]), Path(sys.argv[2])
t = src.read_text(encoding="utf-8")
block = ('  - id: GAR-R13-02\n'
         '    garment: "lowland-cloth valley coat"\n'
         '    form_slot: "LEX-GAR-02 (to-verify with the lexicon owner)"\n'
         '    era: E0\n')
if block not in t:
    raise SystemExit("fixture no longer matches the expected GAR-R13-02 block")
dst.write_text(t.replace(block, block.replace("    era: E0\n", "    era: E1\n")),
               encoding="utf-8")
PY
python3 "$TOOL" --packet "$CORR" > "$SCRATCH/run-13-corrected-check.txt" 2>&1
say "exit: $?"
if grep -F "D2L-MATERIAL" "$SCRATCH/run-13-corrected-check.txt" >/dev/null; then
  fail "the corrected twin still carries a material finding"
fi
say "no D2L-MATERIAL finding on the corrected twin: ok"
say ""

# --- 3. the frozen gate agrees ----------------------------------------------
say "== 3. frozen costume-era-consistency gate on the fixture (independent check) =="
python3 "$GATE" "$FIX" > "$SCRATCH/run-13-gate-check.txt" 2>&1
say "exit: $?"
grep -F "FINDING MAT-02: [reject] GAR-R13-02" "$SCRATCH/run-13-gate-check.txt" \
  || fail "expected 'FINDING MAT-02: [reject] GAR-R13-02' not observed"
say ""

if [ "$failures" -eq 0 ]; then
  say "PASS: the reconciliation path flags the claim, the corrected twin passes, the frozen gate agrees."
  exit 0
fi
say "FAIL: $failures expectation(s) not met at this tool revision (see scratch/run-13-*-check.txt)."
exit 1
