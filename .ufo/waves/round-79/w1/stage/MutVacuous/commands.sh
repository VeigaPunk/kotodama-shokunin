#!/bin/sh
# MutVacuous W1 reproduction. Run from any directory; all writes go to $WORK.
# The counter is READ from the lane (round-77 stage copy, sha256 in SHA256SUMS).
# The lane is only read: clones are made under $WORK by the counter itself.
LANE=/home/vgpnk/Projects/shokunin/kotodama-shokunin
STAGE=$LANE/.ufo/waves/round-79/w1/stage/MutVacuous
COUNTER=$LANE/.ufo/waves/round-77/w1/stage/ExecAdaptCa/accept-ca.py
BASE=211f9526800906e0c585d878d265c37e5e090c15
WORK=${WORK:?set WORK to an explicit scratch dir, e.g. /fast/scratch/hyaku/kotodama-r79/MutVacuous/work}
mkdir -p "$WORK"

# 1. integrity of the counter and fixtures
(cd "$STAGE" && sha256sum -c SHA256SUMS | grep -v ': OK$' ; echo "checksum-check-done")

# 2. the round-77 counter's pre-freeze ledger check, per fixture (LEDGER-level only)
for f in "$STAGE"/fixtures/*.json; do
  python3 -B "$COUNTER" --ledger-check "$f" --root "$LANE" --base "$BASE" --work "$WORK"; echo "exit=$?  $(basename "$f")"
done

# 3. the round-77 counter's BASEMISMATCH leg over every fixture (in-process, base clone)
python3 -B "$STAGE/driver/matrix-driver.py" --counter "$COUNTER" --lane "$LANE" --work "$WORK" --fixtures "$STAGE/fixtures"

# 4. consolidated V-series (recorded in out/final-run-raw.txt)
python3 -B "$STAGE/driver/mutvacuous-basemismatch.py" --counter "$COUNTER" --lane "$LANE" --work "$WORK" --fixtures "$STAGE/fixtures"

# 5. regenerate fixtures from the truthful control (optional; recorded inputs are in fixtures/)
#    python3 -B "$STAGE/driver/build-clean2.py"   # writes $SCRATCH/ledgers/clean-control-v2.json (edit W path first)
#    python3 -B "$STAGE/driver/make-fixtures.py" <dir-with-clean-control-v2.json> <out-dir>
