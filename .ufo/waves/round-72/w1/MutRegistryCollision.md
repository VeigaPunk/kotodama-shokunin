# MutRegistryCollision — mutation tests of the adoption's id-collision guard

Seat: `L1Kotodama72.MutRegistryCollision` (leaf; no delegation, no background jobs).
Round 72, hyaku run 6. Date 2026-10-25.
Claim context: C (coverage, assimilation-sourced), leg COLLCHECK — the id-collision
check for the admitted rows' new ids (S874/S875 not in reg-ids).

## 1. Contract / guard under test

- Extraction pattern (contract): `grep -oE '^ {0,3}\|[[:space:]]*S[0-9]{3,}'`
  — registry rows are markdown table lines: 0–3 leading spaces, `|`, optional
  whitespace, then an S-id (3+ digits).
- Guard = extract ids from the registry file AND from the staged file, then set
  intersection (`comm -12`). Non-empty intersection ⇒ collision.
- Detector implementation reproduced verbatim from the contract at
  `/tmp/r72-mut/guard.sh` (copied to `mutations/guard.sh`).

## 2. Probes and verdicts

| Probe | Fixture bytes | Expected | Actual output | Verdict |
|---|---|---|---|---|
| (a) indented row | `reg-slice-a.md`: `  \| S874 \| …` (2 leading spaces) + `\| S900 \|`; `staged-slice-a.md`: S874, S875 | guard catches S874 (indent tolerance) | reg={S874,S900}, staged={S874,S875}, intersection={S874} | **caught — KILLED** (no false negative) |
| (b) column-0 row | `reg-slice-b.md`: `\| S874 \| …` at column 0 + `\| S901 \|`; `staged-slice-b.md`: S874 | guard catches S874 | reg={S874,S901}, staged={S874}, intersection={S874} | **caught — KILLED** (no false negative) |
| control (pristine) | `control-reg.md` S900–S902 vs `control-staged.md` S910–S911 | empty intersection | empty | **no false positive** |
| boundary probe | `probe-reg-indent4.md`: `    \| S874 \|` (4 leading spaces) | (pattern caps at 3 spaces) | extraction empty — missed | **by design**; documented limitation, not a regression |
| (c) real data | lane `corpus/SOURCES.md` vs staged `…/shokuknow/merge/kotodama/SOURCES.append.md` | see §3 | see §3 | **collision caught; NEW ids S874/S875 next-free** |

## 3. Real-data measurements (probe c)

Both sides extracted with the contract pattern; sets sorted-unique.

- **Lane registry ids**: 797 unique, min `S001`, max `S873`, no duplicates
  (matches the claim's 797-row registry at base `b60c7b1`). S874/S875 absent.
- **Staged ids** (shokuknow `SOURCES.append.md`): 132 unique, min `S859`, max
  `S990`, complete contiguous S859–S990 (seq-check missing = 0), no duplicates.
- **Real intersection**: exactly `S859 S860 S861 S862 S863 S864 S865 S866 S867
  S868 S869 S870 S871 S872 S873` — 15 ids, the staged-overlap band.
  **The guard catches all of them.**
- **Adopted NEW ids**: `S874`, `S875` are both in the staged set and both absent
  from the lane reg-ids (`grep -x` exit 1) → next-free, no collision. This is
  exactly the COLLCHECK expectation (empty collisions file for S874/S875).

## 4. Restoration evidence

- The detector is read-only (`grep`/`comm`/`sort`); no fixture or real input was
  modified during the run. Restoration N/A; bytes unchanged.
- Hashes recorded in `mutations/hashes.txt` (all fixtures, guard.sh, and the two
  real inputs). Real input hashes:
  - lane `corpus/SOURCES.md`: `bf6ad0ea5b538855b487cbc89dca3c35c1a30dc874d57de486718b363a3eee8b`
  - staged `SOURCES.append.md`: `7fb4f488807e8364d204a3081a2e57379d6caafaa92dbab9dfbc381757223754`
- Outputs saved under
  `.ufo/waves/round-72/assimilation/mutations/` (guard.sh, fixtures a/b/control/probe,
  id lists reg/staged/intersection per probe, `reg-ids-real.txt`,
  `staged-ids-real.txt`, `intersection-real.txt`, `run-log.txt`, `VERDICT.md`, `hashes.txt`).

## 5. Adjacent observations (out of scope, for integrator)

- The wave's existing `reg-to-staged.txt` keys three ids with stray backticks
  (`S807``, `S812``, `S835``). They are not markdown-table rows, so the guard
  pattern does not apply; any other parser of that map should strip them.
- Tools used: `grep`, `comm`, `sort`, `sed`, `wc`, `seq`, `sha256sum` (all
  stock, present on host). No tool installed/updated; no RULES.md gate relevant.

## 6. Bottom line

The id-collision guard as specified catches both adversarial layouts (indented
and column-0 rows) and the entire real staged-overlap band S859–S873. The
adoption's new ids S874/S875 are next-free and avoid every collision. Guard
behavior verified; no contract change recommended.
