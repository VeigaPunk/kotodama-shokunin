# Round-93 counter revisions

Made before any round-93 data was produced (no lands commit, no entry, no
registry row existed when these were made).

## Revision 1 -> 2 (freeze 1928e00d -> freeze 2)

- Old: `measure93.py` CENSUS leg ran the census tool from inside the materialized
  lands tree (`<mat>/scripts/sources-census.sh`). The census script lives at the
  fleet root (`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh`), outside
  every lane, so the leg reported `absent` on the freeze-1 control run (receipt
  `reports/round-93/controls/C-freeze-rev1.txt`).
- New: the leg runs the fleet-root script in file mode on the materialized
  `corpus/SOURCES.md`: `scripts/sources-census.sh validate --file <mat>/corpus/SOURCES.md`.
  C.census_tool in claims.json is the absolute fleet path.
- Why file mode: the census `--root` form needs a fleet `shokunin.conf` and cannot
  validate a standalone tree. Measured probes (2026-11-05): file mode on
  `kotodama-shokunin/corpus/SOURCES.md` from inside the lane: rc 0, zero E-findings.
  File mode on the same bytes copied to a scratch directory outside the lane: rc 1
  with E11 "missing used-by" findings, because `used-by` paths resolve against the
  file's own tree. The counter places the file inside the materialized tree, so the
  E11 false positives cannot arise.
- No predicate threshold, base, claim text, refusal list or counter leg name changed.
