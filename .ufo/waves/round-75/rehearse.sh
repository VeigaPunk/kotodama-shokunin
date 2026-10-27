#!/bin/sh
# rehearse freeze -> Ca -> C in a scratch clone (scratch identity, scratch repo only); prints the three revs and both counter verdicts
L=/home/vgpnk/Projects/shokunin/kotodama-shokunin
B=f556d1049fe651d3d63975600b13acd9fb686f15
S=/fast/scratch/hyaku/kotodama-r75/L1-rehearse
rm -rf $S; mkdir -p $S; git clone -q --shared $L $S/lane || exit 2
D=$S/lane; test "$(git -C $D rev-parse --show-toplevel)" = "$D" || exit 2
git -C $D checkout -q -B main $B
G="git -C $D -c user.name=rehearsal -c user.email=r@r.invalid"
for p in $(sh $L/.ufo/waves/round-75/freeze-set.sh | sort -u); do mkdir -p $D/$(dirname $p); cp $L/$p $D/$p; done
$G add -A >/dev/null; $G commit -qm freeze; F=$(git -C $D rev-parse HEAD)
python3 $L/.ufo/waves/round-75/apply-landing.py $D ca || exit 3
$G add -A >/dev/null; $G commit -qm ca; CA=$(git -C $D rev-parse HEAD)
python3 $L/.ufo/waves/round-75/apply-landing.py $D c || exit 3
$G add -A >/dev/null; $G commit -qm c; C=$(git -C $D rev-parse HEAD)
echo "F=$F CA=$CA C=$C D=$D"
cd $D
echo "--- Ca at CA"; git -C $D branch -f main $CA >/dev/null 2>&1; git -C $D checkout -q main; python3 -B reports/round-75/accept-ca.py --root . --lands $CA --freeze $F --fleet-root /home/vgpnk/Projects/shokunin --combined $C | grep -E '^LEG|^ACCEPT' | cut -c1-260
git -C $D branch -f main $C; git -C $D checkout -q main; echo "--- C at C"; python3 -B reports/round-75/accept-c.py --root . --lands $C --freeze $F --fleet-root /home/vgpnk/Projects/shokunin | grep -E '^LEG|^ACCEPT|^     ' | cut -c1-260
