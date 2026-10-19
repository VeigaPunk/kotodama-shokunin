# r18 D4-adapter baseline — successor named (round-33 disposition of D13 debt 12)

Filed state (unchanged, append-only): `tools/gates/frozen/round-18/MANIFEST.tsv`
pins two rows at recorded exit 0 (typed-labels.d4.yml a59990bbfe5a8992ffa6e67e9b3e43e7ff477df9fc754e5af92b6f40d23fe11d, packet.d4.yml
e7ecd2045ef0e5f9823ce0a067d21b8221b2ceb5e8f5799736981a1c88fa50d3; freeze-receipt.json:20,:35). The live D4 bytes have since moved
(typed-labels c23b0ab532cfb9d4bb403405c6996982a447098048e08facbbc9f341ea13f82e, packet aac91246cede8840a52b710e8d17a6254c68ff7d93f6720c4a4a458b6c76eee3), so the generation replays exit 1,
2/2 mismatch — its declared expected code (`reports/round-31/sweep/run-sweep.py:132-133`).

Successor: `reports/round-31/sweep/frozen/r31-post/MANIFEST.tsv` — same two
D4-adapter gates at the live bytes, replay exit 0, 4/4 reproduced
(`TMPDIR=/var/tmp/... python3 -B tools/replay-frozen.py <manifest>`, 2026-10-19).

Semantics restated: a pin is integrity, never truth; a reproduced red verdict
stays red; filed generations are retained as controls, and a successor is a NEW
generation — never an in-place edit. No promotion or clearance verdict is
claimed here.
