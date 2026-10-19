# Instrument of record — basename-couples resolution

Recorded round 44 (claim O). This note is the durable demotion record; it edits no
instrument byte.

- **Census authority:** `tools/harness/basename-couples-resolver.py`
  (sha256 `43ce341f783041cfa4af538a2ce9275729daf13fb6e118f0b5ac66308ab5ad64`,
  body authored as the r43 O09 successor draft, landed byte-exact at r44).
  It implements the r39 basename-couples policy's four classes (direct / fallback /
  ambiguous / unresolved) plus the disposition leg (every fallback mapping listed,
  every unresolved/ambiguous row carrying a named reason) and the §5.6 glob-fragment
  quarantine. `--selftest` 27/27; `--census` 223/2730 → 2556/166/0/7 +1 glob.
- **N6 regression witness (read-only, not a census authority):**
  `tools/harness/couples-reference-extractor.py` (sha256
  `d8d23a265d12d290de69a6eb50454273af4ca699986812c6e203a030f4679cf1`, r42). Its bytes
  are untouched; it remains the witness for the r42 N6 fix and its six-class
  `prospective`/`glob-fragment` split. Token-level parity with the successor is 0-diff
  after the documented `prospective → unresolved` fold (`op/O07-parity.md`).

Authority rule (per r43 O07 arbitration): the successor is the single census
authority; the witness is never cited as a resolving authority, only as the N6
regression control. A future change to either is a new recorded act.
