# R21-O16 — superseded R18 frozen replay row

- **Disposition:** open; route an append-only successor or explicit supersession note to the R22 frozen-replay owner.
- **Finding:** the original round-18 D4 frozen row no longer reproduces after the projection moved. This is a documented supersession, not a reason to edit the old manifest.
- **Control:** `reports/round-21/defects/regression.md` §Frozen replay measurements records the isolated-scratch command `python3 tools/replay-frozen.py tools/gates/frozen/round-18/MANIFEST.tsv --json`, run 2026-10-18 at 10:50:16 -03:00. It reports exit 1, one of two rows reproduced, and the D4 projection row as `replay_mismatch`; the same report identifies the changed projection digests and says the filed manifest was not changed. The R20 precursor is `reports/round-20/regression.md` §4 (F-O15-1).
- **R22 route / owner:** add a new frozen generation or a named supersession record, with fresh digest and replay evidence. Leave `tools/gates/frozen/round-18/MANIFEST.tsv` byte-for-byte intact.
- **Limit:** the replay result is attributed to the independent R21 regression seat; this worker did not rerun it or promote the round.
