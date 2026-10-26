# MutRegistryCollision — round-75 w1 mutation probe, item-10 id-collision guard

Seat: `MutRegistryCollision` (leaf; no delegation, no installs, no lane mutation beyond this report).
Lane base: `f556d1049fe651d3d63975600b13acd9fb686f15`. Date: 2026-10-27.

## Fixture

- Scratch: `/fast/scratch/hyaku/kotodama-r75/MutRegistryCollision/` (deleted before yield; receipts embedded below).
- Registry: `git show f556d104…:corpus/SOURCES.md` → 808 rows, max id S884, sha256 `c8da0a5a765de26506a1c4d9b66d9b47c9ffe4e0d62a87fc510077a7f83c5614`.
- Staged package copy: `/home/vgpnk/Projects/shokuknow/merge/kotodama/SOURCES.append.md` → sha256 `7fb4f488807e8364d204a3081a2e57379d6caafaa92dbab9dfbc381757223754`, staged-ids 132 (S859…S990).
- Mirror: full `corpus/` copy + lane `SKILL.md`, registry swapped to the base bytes (needed for `used-by` resolution; without the tree the pristine census floods E11 and every case is inconclusive — first run hit exactly that and was discarded).
- Planted rows: appended directly after the S884 row (line 839), inside the `## Registry` section, 11 cells, kind `book`, tier `C`, status `queued`, opened `2026-10-27`, recheck `180d`, unique `example.org/mutprobe-*` URL.

## Detectors

Canonical item-10 pair (round-74 `ExecRenumber.md` §1, re-derived, not copied on faith):

```
grep -oE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' REG | grep -oE 'S[0-9]+' | sort > reg-ids
grep -oE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' STG | grep -oE 'S[0-9]+' | sort > staged-ids
comm -12 reg-ids staged-ids > collisions
```

Raw-pair variant (secondary): `comm -12` on un-normalised `grep -oE '^ {0,3}\|…'` output.
Census: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --file <registry>`.

## Baseline (must be green or every case is inconclusive)

- Guard: reg-ids **808**, collisions **26** = `S859 S860 … S884`. **S885 ∉ collisions, S886 ∉ collisions** — the lane registry does NOT yet hold S885/S886 while staged-ids holds both.
- Census: **rc=0, 0 E-codes** (32 info lines; pre-existing W04 warnings only).

## Mutation × outcome

| mut | planted id cell | guard reg-ids | guard collisions | probe in collisions | raw variant | census | verdict vs expectation |
|---|---|---|---|---|---|---|---|
| m1 | `␣␣\| S886` | 809 | 27 (+S886) | **1** | miss (0) | rc=0, 0 E | **killed** — found, as COLLCHECK requires |
| m2 | `␣␣␣\| S886` | 809 | 27 (+S886) | **1** | miss (0) | rc=0, 0 E | **killed** — found |
| m3 | `␣␣␣␣\| S886` | 808 | 26 | 0 | 0 | rc=0, 0 E | **survives both, silently** — expected: `^ {0,3}` misses 4-space; the claim *requires* not-found |
| m4 | `\| S886` (col 0) | 809 | 27 (+S886) | **1** | **fires (1)** | rc=0, 0 E | **killed** — found |
| m5 | `⇥\| S886` (tab) | 808 | 26 | 0 | 0 | rc=0, 0 E | **survives both, silently** — guard blind and census row-binding (`!~ /^ {0,3}\|/`) both drop the row; under-count, no error |
| m6 | `␣␣\| s885` | 808 | 26 | 0 | 0 | **rc=1, E02 `s885`** | guard **survives** (uppercase-only pattern); census **kills** via E02 — matches round-74 |
| m7 | `␣␣\| S1005` | 809 (**S1005 admitted**) | 26 (no staged counterpart) | 0 | 0 | **rc=0, 0 E** | **survives BOTH** — see finding F3 |
| m8 | `␣␣\| S885` | 809 | 27 (**+S885**) | **1** | miss (0) | rc=0, 0 E | **killed** — see finding F4 |

Restoration: every mutation planted into a fresh pristine copy; final `cmp pristine fixture` **OK**; both sha256 `c8da0a5a…f83c5614`. No /tmp used; no lane or fleet bytes written except this report.

## Findings

- **F1 — normalization step is load-bearing (reproduced on round-75 inputs).** The raw variant fires only m4 (column zero matches the staged package's own column-zero rows byte-for-byte) and misses m1/m2/m8: 2- and 3-space indents change the matched prefix string, so `comm` on raw output silently under-reports. The second `grep -oE 'S[0-9]+'` is not decoration.
- **F2 — 4-space and tab rows vanish from both detectors** (m3, m5): guard pattern `^ {0,3}` and the census's row binding share the same anchor, so a mis-indented append is a silent row-count under-count, never an error. This is the documented "4-space not found" half of COLLCHECK; the round must not read census row-count equality as evidence of correct indentation.
- **F3 — new this round: a 4-digit id S1005 survives both detectors.** Guard pattern `S[0-9]{3,}` admits it (reg-ids 808→809) and the census id check `^S[0-9]{3,}$` accepts 4+ digits (no E02/E03, rc=0). No E-code binds ids to the S001…S884 frontier, so a typo'd 4-digit id enters the registry id universe unflagged. Coverage gap, not a contract breach; the id-renumber map review is the only remaining net.
- **F4 — m8 before/after proof (the S885 hand-off).** Pristine run: staged-ids holds S885, collisions does not (26 ids, S859…S884) — the guard output itself certifies the lane registry does NOT yet hold S885. Planting one 2-space `| S885 |` row moves collisions to 27 with S885 present. So the moment the lane adopts staged S885 (claim C row_set, identity map staged S885 → lane S885), S885 becomes a permanent collisions pair accepted only by-document; until then any premature S885 byte in the registry is caught by the guard — but **not by the census**, which is lane-internal only (rc=0 before and after m8).
- **F5 — the guard is an intersection only**: blind to intra-registry duplicates (structurally reconfirmed; that half is delegated to census E03, which fires on a well-formed twin — round-74 m7b, not re-run here).
- Baseline discipline: first fixture attempt (registry file only) had census rc=1 via E11 `used-by` misses on the *pristine* bytes — a detector-setup failure, discarded as inconclusive; the mirrored corpus fixed it. Baseline must be green before any mutant verdict counts.

## Receipts

Verbatim driver output (also mirrored here as the receipt; scratch now deleted):

```
staged-ids: 132  staged sha256: 7fb4f488807e8364d204a3081a2e57379d6caafaa92dbab9dfbc381757223754
----- baseline (pristine) -----
== pristine probe=S885
guard: reg-ids=808 collisions=26 probe_in_regids=0 probe_in_collisions=0
raw-variant: probe_in_raw_collisions=0
census: rc=0 ecodes=0
restore: pristine==mutated-prior cmp OK
== pristine probe=S886
guard: reg-ids=808 collisions=26 probe_in_regids=0 probe_in_collisions=0
raw-variant: probe_in_raw_collisions=0
census: rc=0 ecodes=0
restore: pristine==mutated-prior cmp OK
----- mutations (each plants into a fresh pristine copy) -----
== m1 probe=S886
guard: reg-ids=809 collisions=27 probe_in_regids=1 probe_in_collisions=1
raw-variant: probe_in_raw_collisions=0
census: rc=0 ecodes=0
== m2 probe=S886
guard: reg-ids=809 collisions=27 probe_in_regids=1 probe_in_collisions=1
raw-variant: probe_in_raw_collisions=0
census: rc=0 ecodes=0
== m3 probe=S886
guard: reg-ids=808 collisions=26 probe_in_regids=0 probe_in_collisions=0
raw-variant: probe_in_raw_collisions=0
census: rc=0 ecodes=0
== m4 probe=S886
guard: reg-ids=809 collisions=27 probe_in_regids=1 probe_in_collisions=1
raw-variant: probe_in_raw_collisions=1
census: rc=0 ecodes=0
== m5 probe=S886
guard: reg-ids=808 collisions=26 probe_in_regids=0 probe_in_collisions=0
raw-variant: probe_in_raw_collisions=0
census: rc=0 ecodes=0
== m6 probe=s885
guard: reg-ids=808 collisions=26 probe_in_regids=0 probe_in_collisions=0
raw-variant: probe_in_raw_collisions=0
census: rc=1 ecodes=1
  censusE       1 file	E02	s885
== m7 probe=S1005
guard: reg-ids=809 collisions=26 probe_in_regids=1 probe_in_collisions=0
raw-variant: probe_in_raw_collisions=0
census: rc=0 ecodes=0
== m8 probe=S885
guard: reg-ids=809 collisions=27 probe_in_regids=1 probe_in_collisions=1
raw-variant: probe_in_raw_collisions=0
census: rc=0 ecodes=0
----- final restore -----
restored: cmp OK
c8da0a5a765de26506a1c4d9b66d9b47c9ffe4e0d62a87fc510077a7f83c5614  pristine-SOURCES.md
c8da0a5a765de26506a1c4d9b66d9b47c9ffe4e0d62a87fc510077a7f83c5614  fixture/corpus/SOURCES.md
pristine collisions S885 count: 0
m8 collisions S885 count: 1
pristine collisions list: S859 S860 S861 S862 S863 S864 S865 S866 S867 S868 S869 S870 S871 S872 S873 S874 S875 S876 S877 S878 S879 S880 S881 S882 S883 S884
m1 collisions delta vs pristine: S886
```

## Notes

- No tools installed (none needed). No pacman. No model routing. `/tmp` unused.
- Claim C's COLLCHECK requirement "planted 1-3-space collision found, 4-space not found" holds exactly on the round-75 base registry against the current staged package; m8 additionally pins the S885 before/after state the lane is about to step through.
