#!/bin/sh
# prints the repo-relative paths of the freeze commit (claims, ledger, counters, fixtures, controls inputs, assimilation scratch evidence)
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin || exit 2
W=.ufo/waves/round-75
echo reports/round-75/claims.json; echo reports/round-75/telemetry/gap-sweep.txt
echo reports/round-75/ledger.json
echo reports/round-75/accept-c.py
echo reports/round-75/accept-ca.py
for f in reports/round-75/fixtures/*.json; do echo $f; done
for f in selftest-c selftest-ca r1exempt-green r1exempt-red r1exempt-run census-start; do echo reports/round-75/telemetry/$f.txt; done
for f in assimilation/reg-ids assimilation/staged-ids assimilation/collisions assimilation/id-renumber-map.json assimilation/build-map.py assimilation/substitution-table.txt assimilation/collision-documents.txt; do echo $W/$f; done
find $W/assimilation/guard-proof -type f | sort
echo $W/census-start.txt; echo $W/assimilation/validate-receipt.txt; echo $W/assimilation/validate-receipt-draft.txt; find $W/assimilation/validate-fetch -type f | sort
echo $W/build-w1.py; echo $W/build-w2.py; echo $W/build-claims-draft.py 2>/dev/null | grep -v draft
for f in build-claims-final build-claims-final2 build-claims-final3 build-claims-final4 build-claims-final5 build-rows apply-landing run-controls; do ls $W/$f.* 2>/dev/null; done
echo $W/skill-rows.md
find $W/counters -type f -not -name '*.pyc' | sort
find $W/w1 -type f | sort
find $W/w2 -type f -not -path '*/stage/*' -not -name '*.pyc' | sort
find $W/w2/stage -type f | sort
echo $W/w1.ready; echo $W/w1.ready.dispatched; echo $W/w2.ready; echo $W/w2.ready.dispatched
