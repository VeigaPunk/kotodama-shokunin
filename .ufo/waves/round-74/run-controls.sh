#!/bin/sh
# usage: run-controls.sh <freeze> ; writes reports/round-74/telemetry/controls-{c,ca}.txt
F=$1; B=f7104cbce186bc2e1522abf0cfd619cc834628bb; T=reports/round-74/telemetry; FL=/home/vgpnk/Projects/shokunin
{ echo "# controls-c.txt — claim C do-nothing controls (round 74), measured at freeze $F by the freeze-installed counter"
echo "## control 1: lands == freeze (legal ancestor relation; no data landed)"
echo "\$ python3 -B reports/round-74/accept-c.py --root . --lands $F --freeze $F"
python3 -B reports/round-74/accept-c.py --root . --lands $F --freeze $F 2>&1; echo "exit=$?"; echo
echo "## control 2: lands == base (refusal prints FAIL)"
echo "\$ python3 -B reports/round-74/accept-c.py --root . --lands $B --freeze $F"
python3 -B reports/round-74/accept-c.py --root . --lands $B --freeze $F 2>&1; echo "exit=$?"; } > $T/controls-c.txt &
{ echo "# controls-ca.txt — claim Ca do-nothing controls (round 74), measured at freeze $F by the freeze-installed counter"
echo "## control 1: lands == freeze"
echo "\$ python3 -B reports/round-74/accept-ca.py --root . --lands $F --freeze $F --fleet-root $FL"
python3 -B reports/round-74/accept-ca.py --root . --lands $F --freeze $F --fleet-root $FL 2>&1; echo "exit=$?"; echo
echo "## control 2: lands == base"
echo "\$ python3 -B reports/round-74/accept-ca.py --root . --lands $B --freeze $F --fleet-root $FL"
python3 -B reports/round-74/accept-ca.py --root . --lands $B --freeze $F --fleet-root $FL 2>&1; echo "exit=$?"; } > $T/controls-ca.txt &
wait
