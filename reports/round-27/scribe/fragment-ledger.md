# R27-D24 — round-27 fragment ledger (read-time census)

- round: 27 (operator: loop 3 of 3, build round 3 of 4; 64 declared workers,
  `devin/deepseek-v4-1-flash-high`). Seat **R27-D24** (D-scribe 4 of 4).
- date: 2026-10-18. Lane head `b95fca1e40f32f7346937ab6426f9ccca60e319f`
  (declared baseline `4f09c990d4c17f23b5e2cda0871f81db875635fc`, the round-26 admit).
- **writes: this file and its machine-readable twin
  `reports/round-27/scribe/fragment-ledger.json`**, plus gitignored scratch under
  `.scratch/`. No commit, no push; no filed artifact of rounds 8–26 touched.
- canon: **NON-CANON integration ledger.** It admits nothing, certifies no
  round, and blesses no fragment. It is the index the parent uses to integrate
  the wave.

## 0. What this ledger is, and what it is not

A **read-time census** of every file under `reports/round-27/` at
**2026-10-18T19:25:35Z**, with byte size, line count, sha256 (8-char prefix
shown), mtime and an inferred owner seat, plus the round-27 artifacts that landed
**outside** that partition and the **tool** artifacts the wave's evidence is
about.

It is **not** a completeness claim and **not** a round verdict. **The wave was
still writing at the census and kept writing after it.** `reports/round-27/` grew
**2 → 8 → 18 → 75 → 88 → 90 → 93** files between 19:11:04Z and 19:25:35Z, and
individual artifacts moved under the reads: `audit/x59-register-law-negatives.py`
`18 662 → 20 323 → 23 147` bytes across three writes; `audit/x63-…py`
`27 177 → 33 765 → 36 664 → 36 967`; `gate-tests/run-gate-tests.py`
`35 688 → 38 708 → 40 234 → 41 650`; `adjacency.md` `31 145 → 35 287 → 37 252 →
37 606`. **Every cell in §1 binds to the 19:25:35Z stamp only.** Re-run on the
settled tree:

```sh
export TMPDIR=$PWD/.scratch
find reports/round-27 -type f | sort
find reports/round-27 -type f | wc -l
git status --porcelain
```

The machine-readable twin carries the same rows plus `declared_baseline`,
`lane_head`, `census_utc`, `counts`, `outside_partition` and `negative_measurements`.

**The movement is the round's most important structural fact, and §4 records it.**
Two landings (the syllabify fix, the register-law merge) moved the D4 packet
**twice** inside this wave, so several round-27 artifacts measured a tree that no
longer exists — including the two `pinsweep/baselines/*/r27-post/` directories,
which are **already stale** (§4).

## 1. Census — `reports/round-27/**` (90 files, 2026-10-18T19:25:35Z)

Owner seats are **inferred from the path convention** (the seat id in the
filename or the partition), not from a per-file declaration; where the convention
gives nothing the cell says so. An inferred owner is a pointer, never an
authorship claim.

| path | bytes | lines | sha8 | mtime UTC | owner seat (inferred) |
|---|---:|---:|---|---|---|
| `adjacency.md` | 37606 | 653 | `c4c778e8` | 19:25:35 | X (adjacency) |
| `audit/entry-audit.py` | 21446 | 480 | `fb589b28` | 19:23:32 | C/X (entry audit) |
| `audit/o37-sweep-inventory-audit.py` | 9341 | 205 | `053be6c1` | 19:22:10 | O (sweep inventory audit) |
| `audit/x-c48-entry-audit.md` | 14593 | 254 | `6eef2b70` | 19:24:28 | C/X (entry audit) |
| `audit/x-c48-receipt.json` | 175262 | 7173 | `de4a4634` | 19:23:37 | C/X (entry audit receipt) |
| `audit/x57-lessons-audit.md` | 16970 | 259 | `78ed683d` | 19:16:30 | C (lessons) |
| `audit/x57-lessons-audit.py` | 36947 | 773 | `3b5aa5c6` | 19:15:38 | C (lessons) |
| `audit/x57-lessons-receipt.json` | 12672 | 673 | `9ea21438` | 19:16:34 | C (lessons) |
| `audit/x57-lessons-selftest.json` | 4398 | 234 | `0b6d9ea4` | 19:16:33 | C (lessons) |
| `audit/x59-register-law-negatives.md` | 13062 | 228 | `9775c4bc` | 19:19:25 | D/X (law negatives) |
| `audit/x59-register-law-negatives.py` | 23147 | 488 | `52672606` | 19:25:09 | D/X (law negatives) |
| `audit/x60-sweep-completeness.py` | 18502 | 437 | `6c56a7fc` | 19:21:05 | O/X (sweep completeness) |
| `audit/x61-pin-sweep.md` | 18760 | 327 | `b15e0139` | 19:25:15 | O/X (pin sweep) |
| `audit/x61-pin-sweep.py` | 29623 | 655 | `c97e442a` | 19:19:55 | O/X (pin sweep) |
| `audit/x62-frozen-record-audit.md` | 13863 | 232 | `948cbb36` | 19:24:11 | O/X (frozen record) |
| `audit/x62-frozen-record-audit.py` | 28143 | 586 | `4e0c16be` | 19:23:40 | O/X (frozen record) |
| `audit/x63-entry-source-resolvability.md` | 17870 | 310 | `da4ebde0` | 19:25:10 | C/X (entry resolvability) |
| `audit/x63-entry-source-resolvability.py` | 36967 | 901 | `0622aa72` | 19:25:03 | C/X (entry resolvability) |
| `audit/x64-cold-rerun.py` | 20650 | 451 | `8f67ea5d` | 19:23:42 | D/X (cold rerun) |
| `availability.json` | 29324 | 316 | `987b04e1` | 19:23:36 | X (availability) |
| `claims.json` | 2355 | 32 | `373df289` | 19:11:04 | declaration (parent) |
| `gate-tests/D13-argot-gate.md` | 7553 | 148 | `7aafb193` | 19:24:09 | D (gate tests) |
| `gate-tests/D14-typed-gate.md` | 5581 | 93 | `3bcd4e10` | 19:24:15 | D (gate tests) |
| `gate-tests/D15-law-negative.md` | 8477 | 165 | `8c41c98c` | 19:24:26 | D (gate tests) |
| `gate-tests/D16-syllabify-negative.md` | 8645 | 165 | `642a775c` | 19:24:54 | D (gate tests) |
| `gate-tests/fixtures/s1-head2-unconstrained.yml` | 686 | 11 | `b503ec44` | 19:21:28 | D (fixtures) |
| `gate-tests/fixtures/s2-head2-constrained.yml` | 601 | 10 | `c3e35714` | 19:21:28 | D (fixtures) |
| `gate-tests/fixtures/s3-head2-maximal-coda.yml` | 774 | 14 | `622c054e` | 19:16:51 | D (fixtures) |
| `gate-tests/fixtures/s4-head2-prefix-reading.yml` | 642 | 10 | `0d812394` | 19:21:28 | D (fixtures) |
| `gate-tests/receipt.json` | 22122 | 788 | `13ba0164` | 19:25:09 | D (gate tests receipt) |
| `gate-tests/run-gate-tests.py` | 41650 | 828 | `56d2e80d` | 19:25:32 | D (gate tests runner) |
| `law/design.md` | 22728 | 348 | `9d5c1dd7` | 19:20:37 | D (register law) |
| `law/review.md` | 27313 | 466 | `9a3f1071` | 19:22:35 | D (register law) |
| `law/rules.md` | 17739 | 276 | `c6935957` | 19:20:12 | D (register law) |
| `pinsweep/baselines/d4-assembly-check-gate/r27-post/…` (19 files) | — | — | — | 19:19:19 | O (pin sweep baseline) |
| `pinsweep/baselines/d4-typed-labels-check-gate/r27-post/…` (9 files) | — | — | — | 19:19:19 | O (pin sweep baseline) |
| `pinsweep/frozen/r27-post/MANIFEST.tsv` | 1118 | 3 | `7c159ade` | 19:21:44 | O (pin sweep freeze) |
| `pinsweep/frozen/r27-post/d4-assembly.out` | 73 | 1 | `c60820a5` | 19:21:44 | O |
| `pinsweep/frozen/r27-post/d4-typed-labels.out` | 81 | 1 | `1c8add32` | 19:21:44 | O |
| `pinsweep/frozen/r27-post/freeze-receipt.json` | 1413 | 22 | `78f8b524` | 19:21:44 | O |
| `pinsweep/frozen/r27-post/inputs/examples/culture-d4/packet.d4.yml` | 95274 | 3028 | `c5441e3d` | 19:21:44 | O |
| `pinsweep/frozen/r27-post/inputs/examples/culture-d4/typed-labels.d4.yml` | 82161 | 2871 | `072fa806` | 19:21:44 | O |
| `pinsweep/o37-inventory-receipt.json` | 11397 | 417 | `74348eff` | 19:20:59 | O |
| `pinsweep/o37-sweep-inventory-audit.md` | 16987 | 267 | `9b581478` | 19:23:18 | O |
| `pinsweep/v3-baseline-r27/expected.json` | 10856 | 208 | `855603f6` | 19:19:41 | O |
| `pinsweep/v3-baseline-r27/freeze.txt` | 521 | 8 | `0b2ae5e7` | 19:19:41 | O |
| `pinsweep/v3-baseline-r27/packet.md` | 105582 | 335 | `e3fb1ca5` | 19:19:41 | O |
| `pinsweep/v3-baseline-r27/run.log` | 1603 | 14 | `43fded40` | 19:19:41 | O |
| `pinsweep/v3-baseline-r27/twin.json` | 103370 | 2613 | `b849e2f9` | 19:19:41 | O |
| `readme/reconcile.md` | 7912 | 157 | `744a1491` | 19:21:18 | C (README) |
| `readme/sweep.py` | 12665 | 326 | `368bd669` | 19:13:30 | C (README) |
| `readme/verify.md` | 8731 | 167 | `1016c725` | 19:24:21 | C (README) |
| `report-draft.md` | 14995 | 245 | `fcba7baa` | 19:19:36 | unattributed (path convention gives no seat) |
| `rerun.json` | 14946 | 184 | `a0ffa8fa` | 19:19:22 | O (acceptance) |
| `run-validation.py` | 84730 | 1778 | `7c8c725c` | 19:20:30 | acceptance runner (O seat) |
| `scope.md` | 21085 | 182 | `a632f989` | 19:17:11 | X (scope) |
| `scribe/capability-row.md` | 28826 | 386 | `db893d07` | 19:24:10 | D (**this seat's sibling, R27-D21**) |
| `scribe/fragment-ledger.json` | — | — | — | — | D (**this file's twin**) |
| `scribe/fragment-ledger.md` | — | — | — | — | D (**this file**) |
| `scribe/frozen-rows.md` | 23867 | 319 | `cbd759bd` | 19:25:01 | D (**this seat's sibling, R27-D22**) |
| `scribe/skill-rule-row.md` | 21639 | 247 | `f784daec` | 19:25:21 | D (**this seat's sibling, R27-D23**) |
| `scribe/x54-syllabify-spotcheck.md` | 42988 | 751 | `1a6f5dc7` | 19:24:35 | D (syllabify witness) |
| `scribe/x54-syllabify-spotcheck.py` | 22069 | 543 | `ee370f78` | 19:21:16 | D (syllabify witness) |
| `scribe/x56-census.py` | 9849 | 256 | `f414082e` | 19:13:35 | X (census) |
| `scribe/x58-d4-chain-cold-rerun.md` | 42601 | 720 | `6034c99a` | 19:22:57 | D/X (cold rerun) |
| `scribe/x64-entry-source-resolvability-cold.md` | 12632 | 246 | `6e147099` | 19:24:26 | C/X (cold) |
| `targets.json` | 191 | 10 | `04c18533` | 19:11:04 | declaration (parent) |
| `validation.json` | 121206 | 1391 | `d75fa1eb` | 19:24:55 | acceptance runner/receipt |

**The `pinsweep/baselines/*/r27-post/` directories are collapsed into two rows
above.** They hold 19 and 9 files respectively (snapshot copies of the D4
components, both assemblers, the frozen reader, the packets, the projection and
the expected files). Full per-file rows are in the JSON twin.

**Arithmetic.** 90 files, **2 623 941 bytes**, **56 884 lines**; the evidence
subdirectories are `audit/` (20), `gate-tests/` + `fixtures/` (10), `law/` (3),
`pinsweep/` (44 incl. the two baseline trees and the frozen generation),
`readme/` (3), `scribe/` (9), plus 9 top-level files.

**A caution about this file's own row.** `scribe/fragment-ledger.md`'s row is
blank because this ledger is written **after** the census table was built, so its
own row is stale by construction — exactly the way round 26's ledger recorded the
same for itself. The twin is regenerated after the table and carries the same
rows; **a consumer re-measures rather than inherits.**

**The wave kept growing after this stamp.** At 19:25:35Z the partition held
**93** files — three more than §1's 90, all `pinsweep/` artifacts written after
the table was built. **§1's table is a 19:25:35Z snapshot, not the round's file
list.**

## 2. Outside the partition — the round-27 artifacts and the tool surface

**Two classes of round-27 write landed outside `reports/round-27/`**, measured at
19:25:35Z by `git status --porcelain` (23 entries):

| path | status | class |
|---|---|---|
| `examples/culture-d4/components/13-register-law.yml` | **??** (new) | **the D claim's component** — `register_law: RGL-01..05`, 19:21Z |
| `corpus/knowledge/linguistics/register-strata-attestation.md` | **??** (new) | **the C claim's entry**, 234 lines, `8dd62923…` |
| `corpus/README.md` | **M** | the C claim's index reconciliation (revision 1.7) |
| `examples/culture-d4/components/01-brief.yml` | **M** | C-04 registry row + `record_fields.registers` |
| `examples/culture-d4/packet.d4.yml` | **M** | the two landings merged (`registers:` + `register_law:`) |
| `examples/culture-d4/packet.d4.typed.yml` | **M** | derived |
| `examples/culture-d4/typed-labels.d4.yml` | **M** | derived |
| `examples/culture-d4/expected-holds.json` | **M** | re-pinned; counts still 12/0/0 |
| `tools/gates/argot-derivation-gate.py` | **M** | **the syllabify fix** (`5b5abe78…` → `d7a3ad1a…`, selftest 21/21 → 27/27) |
| `tools/gates/typed-pipelines.json` | **M** | the `d4` profile re-pinned to the final packet/projection |

`git status --porcelain | grep -v "reports/round-27"` returns exactly these ten.
**No other pre-existing tool, gate, example or corpus byte was modified.** This
is measured, not assumed: the list contains no path under `tools/gates/` other
than the two above, and no `SKILL.md`/`SCORECARD.md`/`LOG.md` entry.

**The two files whose absence is itself the measurement:**

- **`SKILL.md` is byte-still** at `2d85bfea…`, 598 lines. `grep -c "Derivation
  relations" SKILL.md` → **0**. The round-25 rule has now been absent for three
  rounds, and the round-27 D-scribe draft (`scribe/skill-rule-row.md`) is a draft
  like its predecessors.
- **No `SCORECARD.md` or `LOG.md` round-27 entry exists.** `grep -c "Round 27"
  LOG.md` → 0; `SCORECARD.md` carries no round-27 axes section. Both are the
  parent's integration writes.
- **No `corpus/lessons/round-27.md`** — `ls corpus/lessons/round-27.md` → absent.
  The lesson set stands at 36 entries (including `round-26.md`).

**The tool artifacts the round's evidence is about** (sha256 measured
19:23:26Z, cwd = lane root):

| artifact | sha256 | moved this round? |
|---|---|---|
| `tools/gates/argot-derivation-gate.py` | `d7a3ad1a6ad1c4c5993b7d74bf8bc96326916f113a07e6472d90ceecd7faf1aa` | **yes** (was `5b5abe78…`) |
| `tools/gates/typed-pipeline-gate.py` | `b749ad07cf1710279aea557c071587cf4b3a228a9fb4d03398b4b94d2f32ad85` | no |
| `tools/gates/naming-collision-gate.py` | `d9e4e8f4f93a21b3b8574856a7d8bc6b93d224eee490ab37ed5f98741a630a1d` | no |
| `tools/gates/d4-typed-labels-check-gate.py` | `05f99629d870280c55e15f46d799c29d7cfbc0645f0d0cd68a5fff1006181841` | no |
| `tools/gates/d4-assembly-check-gate.py` | `df1a364b3970365c217a9b6a16f075bab854ee87aefab831de50df4a9d71544a` | no |
| `tools/gates/typed-pipelines.json` | `be3069088c3ff0f5807084e626e48df2d45da4ba7482e8b1cb9454f3494db507` | **yes** (was `35946c8d…`) |
| `tools/assemble-culture-d4.py` | `943f487ba991d45d369eb8fb6e9bb686046df165424d101cfa2670f79bb844b2` | no |
| `tools/assemble-d4-typed.py` | `92f5460bcc34ffbb43a771504d213d23aafd818b39c7017c823a363e99063fd0` | no |
| `examples/culture-d4/packet.d4.yml` | `c5441e3d0b237f331cfabe8002ad3bf4db7694e2666c21ba8c723ac66bf21f6a` | **yes** (twice) |
| `examples/culture-d4/components/13-register-law.yml` | `40f774cb7a69abae9d5914abad54d4c8b6bf63b30003b151c48ae3fbfb7dad7a` | **new** |

## 3. The D partition — what the scribe seats and the D seats produced

| artifact | class | what it is |
|---|---|---|
| `law/design.md`, `law/rules.md`, `law/review.md` | D design | the register law's machine-readable rule registry (`RLAW-01..06`) with the replayable/unowned column; the design authority for `13-register-law.yml` |
| `scribe/capability-row.md` | **this seat's sibling (R27-D21)** | the capability-row draft for the register law + the syllabify residue |
| `scribe/frozen-rows.md` | **this seat's sibling (R27-D22)** | the frozen-row draft; the pin cascade and the stale-baseline finding |
| `scribe/skill-rule-row.md` | **this seat's sibling (R27-D23)** | the SKILL register-law rule draft |
| `scribe/x54-syllabify-spotcheck.py` / `.md` | D/X witness | the three-witness syllabify instrument (gate executed / design re-implemented / packet's own `syllables:`) |
| `scribe/x58-d4-chain-cold-rerun.md` | D/X | a cold re-run of the D4 chain |
| `audit/x59-register-law-negatives.py` / `.md` | D/X audit | the independent register-law checker (`ruby -ryaml`, own `reverse`/`lengthen`); `--controls` 7/7 |
| `gate-tests/run-gate-tests.py` + `receipt.json` + `D13..D16` + `fixtures/s1..s4` | D battery | the round-27 gate-test battery and its four reading fixtures |

**Two measured cautions about the sibling files.** All three scribe drafts are
**drafts**: none landed a `SCORECARD.md`/`SKILL.md` row, and the measured fact
that makes this concrete is that `grep -c "Derivation relations" SKILL.md` → **0**
— the round-25 rule they build on never landed either.

**And the siblings measure a tree that moved under them.** `capability-row.md`
and `frozen-rows.md` both record the movement and re-stamp; a consumer must read
their §0/§1 stamps rather than inherit a number from an earlier section.

## 4. The movement that matters most — two landings, two stale generations

Recorded because a ledger that hides its own drift is not a ledger. All stamps
UTC, 2026-10-18.

| stamp | `reports/round-27/` files | `packet.d4.yml` | what moved |
|---|---:|---|---|
| 19:11:04 | 2 | `dd25077b…` | the declaration (`claims.json`, `targets.json`) |
| 19:13:35 | 8 | `dd25077b…` | `readme/sweep.py`, `scribe/x56-census.py`, audit instruments land |
| 19:16:51 | 18 | `dd25077b…` | `gate-tests/`, `law/`, `scope.md`, `pinsweep/baselines/` land |
| **19:21:20** | ~75 | `dd25077b…` | **the syllabify fix lands** (`argot-derivation-gate.py` → `d7a3ad1a…`) |
| **19:21:29** | ~75 | **`c5441e3d…`** | **the register law merges**; the typed gate goes exit 2 / `L1-profile` |
| **19:21:44** | ~75 | `c5441e3d…` | **the O seats freeze `pinsweep/frozen/r27-post/`** against the post-law bytes |
| 19:22:54 | 88 | `c5441e3d…` | the `typed-pipelines.json` re-pin lands; the typed gate green again |
| **19:25:35** | **90** (93 at close) | `c5441e3d…` | this census |

**The load-bearing consequence, measured.** The
`pinsweep/baselines/*/r27-post/` directories were frozen at **19:19:19Z** against
`dd25077b…`/`d03f6391…` — i.e. **before the register law merged at 19:21:29Z** —
so they are **already stale against the live tree**:

```sh
# 1 of 16 inputs stale in the assembly baseline, 2 of 6 in the typed-labels baseline
#   examples/culture-d4/packet.d4.yml        dd25077bc016 -> c5441e3d0b23
#   examples/culture-d4/typed-labels.d4.yml  d03f6391fb8d -> 072fa806ed78
```

Run as a replacement battery root they also read **coverage 2/9, exit 2**, because
that root holds only the two D4 baselines while the battery requires one for all
nine registered gates (`--baselines-root` replaces the roots rather than adding
to them). **The settled successor is `pinsweep/frozen/r27-post/`** (2 rows,
19:21:44Z), which pins `c5441e3d…`/`072fa806…` and replays **2/2 OK**.

**The frozen generations also moved under the wave.** `round-26/post-register`
replayed **6/6 OK** at 19:16Z and reads **2 mismatch / 4 reproduced** at 19:25Z,
because the law landing moved the packet its D4 rows pin. That is the designed
behaviour — a re-freeze is a new generation, never an in-place edit — and it is
the clearest instance in the round of a generation going red because the artifact
it graded **moved**, not because it was wrong. `reports/round-27/audit/x61-pin-sweep.py`
classifies every such mismatch as **supersession** (the live input no longer
hashes to the pin) rather than **drift** (a pinned byte was tampered with).

## 5. Counting commands for this file

```sh
export TMPDIR=$PWD/.scratch
find reports/round-27 -type f | sort
find reports/round-27 -type f | wc -l                      # 90 at 19:25:35Z; 93 at close
git status --porcelain | wc -l                             # 23
git status --porcelain | grep -v "reports/round-27"        # the ten outside writes (§2)
ls corpus/lessons/ | wc -l                                 # 36 — no round-27 lesson
ls corpus/knowledge/linguistics/ | wc -l                   # 20 (was 19)
grep -n "Total knowledge entries" corpus/README.md         # 200
grep -c "Derivation relations" SKILL.md                    # 0 — the round-25 rule never landed
grep -c "Round 27" LOG.md                                  # 0 — no round-27 log entry yet
sha256sum tools/gates/argot-derivation-gate.py tools/gates/typed-pipelines.json \
  examples/culture-d4/packet.d4.yml examples/culture-d4/components/13-register-law.yml
```

## 5a. POST-STAMP DRIFT — the tree moved again after this census

Measured **2026-10-18T19:26:09Z**, 34 seconds after §1's stamp, and recorded
because a ledger that hides its own drift is not a ledger. **The wave is still
writing.**

| artifact | §1/§4 value | 19:26:09Z value | note |
|---|---|---|---|
| `tools/gates/argot-derivation-gate.py` | `d7a3ad1a…` | **`b5406bcd…`** | a **second** write to the gate inside the round; `--selftest` **27/27** and the D4 coverage line `records=175 register_scoped=14 derived_pairs=8 … violations=0 rule_holds=0` are **unchanged**, so the syllabify semantics did not move with it |
| `examples/culture-d4/packet.d4.yml` | `c5441e3d…` | **`86079a67…`** | a **third** packet state; `assemble-culture-d4.py --check` still exits 0, and `registers:`/`register_law:` are both still present (1 each) |
| `examples/culture-d4/packet.d4.typed.yml` | `7dff3ea7…` | **`1c4b8808…`** | derived |
| `examples/culture-d4/typed-labels.d4.yml` | `072fa806…` | **`88a94422…`** | derived |
| `examples/culture-d4/expected-holds.json` | `b9f98381…` | **`857417e9…`** | re-pinned again |
| `examples/culture-d4/components/13-register-law.yml` | `40f774cb…` | **`c0d77181…`** | the law component was revised after the merge |
| `tools/gates/typed-pipelines.json` | `be306908…` | **`69f250df…`** | re-pinned again to the third packet |
| `reports/round-27/` file count | 90 (§1) / 93 (close) | **98** | the wave added five more artifacts |

**What this means for a consumer, plainly.** The siblings
(`capability-row.md`, `frozen-rows.md`, `skill-rule-row.md`) and this ledger all
bind to the **19:23–19:25Z** stamp and **every D4 digest in them is now one or
two writes out of date**. The **qualitative findings are stable** — the law is on
disk with `RGL-01..05`, the packet carries both blocks, the syllabify legality
clause is fixed, the argot leg reads `derived_pairs=8`, the typed gate reads
20/20, and the claim's counting command reports `acceptance_checks_passed: false`
— but **no digest in any of the four files may be quoted without re-hashing**.
That is the round-25 lesson's own discipline ("a pin taken on bytes that are
still moving is not a pin") restated for round 27, and it is the single most
important caution in this ledger.

## 6. What this ledger does not do

- It **admits nothing**: no claim D/O/C verdict, no promotion, no canon. The
  round's counting command (`python3 reports/round-27/run-validation.py`) **ran**
  and wrote `reports/round-27/validation.json` with
  **`acceptance_checks_passed: false`** and named D and O failures — two of which
  this seat measured green at the final stamp (they are mid-write artifacts) and
  three of which are real. The siblings' §6 is the measurement; this ledger only
  records that the receipt exists and is red.
- It **certifies no fragment**. The owner column is inferred from path
  convention; the byte/line/sha cells are measured and bound to the stamp beside
  them.
- It **reads no fragment in full**. Where §3 says "presence and size are
  measured", that is what was done.
- It **does not re-derive** the sibling scribe drafts' findings. §3 cites their
  digests and the one cross-check that matters.
- It **edits no filed byte**: no round-8–26 artifact, no `MANIFEST.tsv`, no
  `expected.json`, no receipt, no tool, gate, example, component or packet. Its
  own write is confined to `reports/round-27/scribe/`.
