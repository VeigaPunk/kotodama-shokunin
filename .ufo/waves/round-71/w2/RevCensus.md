# RevCensus — kotodama round 71 wave 2 (falsify seat)

Verdict: **PASS**. The census validator exits 0 at HEAD with exactly 28 standing W04 rows and no E-class rows. The 13 new registry rows (S861-S873) produce no findings.

## HEADs
- shokunin root (script repo): `29103b3ff121b64b3a30511f8a9f78e84ea2efb1`; `scripts/sources-census.sh` == HEAD (`git diff --quiet HEAD -- scripts/sources-census.sh`).
- kotodama-shokunin: `14c88d9b9bb3c9e47b0cb836f1c98ce5d6f05cc6`; `corpus/SOURCES.md` == HEAD (last touched by `1d1b432 round-71: records — ...`). The worktree has one untracked file, `reports/round-71/telemetry/measures-c.txt`, which the validator does not read.

## Checks
| Check | Command | Result |
|---|---|---|
| Exit 0 | `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama; echo $?` | 0 — PASS |
| W04 = 28 | `... validate ... kotodama \| awk -F'\t' '{print $2}' \| sort \| uniq -c` | `28 W04`, `1 ok` — PASS |
| No E-class rows | same breakdown; stderr is 0 bytes | No E01-E12 rows — PASS |
| New rows are clean | `rg -c 'S8(6[1-9]\|7[0-3])\b' <validate stdout>` | 0 matches — PASS |
| New rows exist | `rg -c '^\s*\|\s*S8(6[1-9]\|7[0-3])\s*\|' corpus/SOURCES.md` | 13 — PASS |
| Validator health | `scripts/sources-census.sh selftest` | exit 0, `selftest ok` — PASS |

## The 28 standing W04 rows (duplicate URL across scopes)
S127, S128, S129, S130, S131, S132, S133, S185, S186, S358, S482, S483, S485, S490, S561, S564, S565, S566, S569, S570, S571, S572, S573, S648, S649, S650, S651, S830.

All 28 are older than S861. None of them comes from round-71 additions.

## Findings
- None actionable in scope.

## Residual risk / gaps
- W04 is advisory, so it does not affect the exit code. The 28 cross-scope duplicates stand as accepted; this seat did not re-judge whether each one is legitimate.
- The `godspeed` skill could not be found anywhere on disk (searched `~/.omp` and a filesystem-wide `SKILL.md` scan), so the check ran without it.
- Tooling: no installs or updates.
