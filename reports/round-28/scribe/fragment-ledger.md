# R28-D24 — round-28 fragment ledger (read-time census)

- round: 28 (operator: loop 3 of 3, **build round 4 of 4 — the last build round**;
  64 declared workers, `devin/deepseek-v4-1-flash-high`). Seat **R28-D24**
  (D-scribe 4 of 4).
- date: 2026-10-18. Declared baseline `6c0ac4484d7ee5d15aaf190e7ad3b8817ea13ede`
  (the round-27 admit); lane HEAD `69cecbc7dcf575a29f29660ecac470e05260fd86`.
- **writes: this file and its machine-readable twin
  `reports/round-28/scribe/fragment-ledger.json`**, plus gitignored scratch under
  `.scratch/`. No commit, no push; no filed artifact of rounds 8–27 touched.
- canon: **NON-CANON integration ledger.** It admits nothing, certifies no round,
  and blesses no fragment. It is the index the parent uses to integrate the wave.

## 0. What this ledger is, and what it is not

A **read-time census** of every file under `reports/round-28/` at
**2026-10-18T20:18:12Z**, with byte size, line count, sha256 (8-char prefix
shown), mtime and an inferred owner seat, plus the round-28 artifacts that landed
**outside** that partition and the **tool** artifacts the wave's evidence is
about.

It is **not** a completeness claim and **not** a round verdict. **The wave was
still writing at the census and kept writing after it.** `reports/round-28/` grew
**2 → 5 → 22 → 26 → 29 → 81** files between 20:10:20Z and 20:18:12Z, and
individual artifacts moved under the reads: `run-validation.py`
`95 895 → 103 311` bytes; `gate-tests/run-gate-tests.py` `45 536 → 52 058`;
`audit/x61-pin-sweep.py` `33 769 → 37 705`; `audit/x57-lessons-audit.py`
`47 455 → 50 540`; `validation.json` `227 034 → 230 925`. **Every cell in §1 binds
to the 20:18:12Z stamp only.** Re-run on the settled tree:

```sh
export TMPDIR=$PWD/.scratch
find reports/round-28 -type f -not -path "*__pycache__*" | sort
find reports/round-28 -type f -not -path "*__pycache__*" | wc -l
git status --porcelain
```

The machine-readable twin carries the same rows plus `declared_baseline`,
`lane_head`, `census_utc`, `counts`, `outside_partition` and
`negative_measurements`.

**The movement is the round's most important structural fact, and §4 records it.**
The RL-4 `packet_keys` landing moved the D4 packet **once** (20:13Z), and the O
seats then froze **two** successor generations against the post-fix bytes
(`pinsweep/frozen/r28-post/`, `pinsweep/baselines/*/r28-post/`). Several round-28
artifacts therefore measured a tree that no longer exists.

## 1. Census — `reports/round-28/**` (81 files, 2026-10-18T20:18:12Z)

Owner seats are **inferred from the path convention** (the seat id in the filename
or the partition), not from a per-file declaration; where the convention gives
nothing the cell says so. An inferred owner is a pointer, never an authorship
claim.

| path | bytes | sha8 | mtime UTC | owner seat (inferred) |
|---|---:|---|---|---|
| `adjacency.md` | 44110 | `d91634ec` | 20:16:11 | X (adjacency) |
| `argot/D17-law-bypass.md` | 25053 | `bdc632eb` | 20:16:32 | D (law-replay derivation) |
| `argot/D18-force-overmatch.md` | 18645 | `e8d68cf5` | 20:16:46 | D |
| `argot/D19-ab-crosscheck.md` | 21264 | `b4d47a6e` | 20:17:12 | D |
| `argot/D20-ceiling-wording.md` | 23927 | `186ec1d1` | 20:18:08 | D |
| `audit/entry-audit.py` | 12626 | `bfe96eaa` | 20:13:07 | C/X (entry audit) |
| `audit/o37-sweep-inventory-audit.py` | 29505 | `a0a9aca9` | 20:17:28 | O (sweep inventory audit) |
| `audit/x57-lessons-audit.md` | 29513 | `5e359f14` | 20:18:05 | C (lessons) |
| `audit/x57-lessons-audit.py` | 50540 | `4f19f9e3` | 20:16:37 | C (lessons) |
| `audit/x57-lessons-live.txt` | 2952 | `f2a2a9b2` | 20:17:54 | C (lessons) |
| `audit/x57-lessons-receipt.json` | 17432 | `9fa6dd11` | 20:17:52 | C (lessons) |
| `audit/x57-lessons-selftest.json` | 7744 | `c4da75a4` | 20:17:53 | C (lessons) |
| `audit/x59-register-law-negatives.md` | 15057 | `6970a5bb` | 20:16:42 | D/X (law negatives) |
| `audit/x59-register-law-negatives.py` | 38945 | `a4482c9c` | 20:15:19 | D/X (law negatives) |
| `audit/x60-sweep-completeness.md` | 13492 | `19a2d78e` | 20:16:25 | O/X (sweep completeness) |
| `audit/x60-sweep-completeness.py` | 22568 | `81afd19d` | 20:14:46 | O/X |
| `audit/x61-pin-sweep.md` | 16214 | `1363dc6d` | 20:17:02 | O/X (pin sweep) |
| `audit/x61-pin-sweep.py` | 37705 | `12add076` | 20:18:06 | O/X |
| `audit/x62-frozen-record-audit.md` | 15981 | `e3abf337` | 20:17:17 | O/X (frozen record) |
| `audit/x62-frozen-record-audit.py` | 32078 | `7a3eea38` | 20:15:52 | O/X |
| `audit/x63-entry-source-resolvability.py` | 46296 | `6501965a` | 20:13:14 | C/X (entry resolvability) |
| `audit/x64-cold-rerun.py` | 25074 | `b74359b4` | 20:12:45 | D/X (cold rerun) |
| `audit/x-c48-entry-audit.md` | 7401 | `d4c2f1f8` | 20:14:17 | C/X (entry audit) |
| `availability.json` | 35597 | `aceb019c` | 20:14:38 | X (availability) |
| `claims.json` | 2453 | `c1a4ea22` | 20:10:20 | declaration (parent) |
| `gate-tests/receipt.json` | 40400 | `a788a106` | 20:17:38 | D/O (gate tests receipt) |
| `gate-tests/run-gate-tests.py` | 52058 | `3abd368d` | 20:18:10 | D/O (gate tests runner) |
| `law/design.md` | 27241 | `5f5ae426` | 20:15:59 | D (law-replay design) |
| `law/rl4-delta.md` | 18269 | `6e3dbb4a` | 20:17:04 | D (RL-4 pricing) |
| `law/vocab.md` | 19436 | `cc8a9a31` | 20:16:20 | D (law vocabulary) |
| `pinsweep/baselines/d4-assembly-check-gate/r28-post/…` (19 files) | — | — | 20:17:09 | O (pin sweep baseline) |
| `pinsweep/baselines/d4-typed-labels-check-gate/r28-post/…` (8 files) | — | — | 20:17:09 | O (pin sweep baseline) |
| `pinsweep/d4-pins.json` | 10486 | `b4867008` | 20:17:12 | O (pin rows + controls) |
| `pinsweep/frozen/r28-post/MANIFEST.tsv` | 1118 | `dfde2826` | 20:17:09 | O (pin sweep freeze) |
| `pinsweep/frozen/r28-post/d4-assembly.out` | 73 | `c60820a5` | 20:17:09 | O |
| `pinsweep/frozen/r28-post/d4-typed-labels.out` | 81 | `1c8add32` | 20:17:09 | O |
| `pinsweep/frozen/r28-post/freeze-receipt.json` | 1446 | `60bc0a93` | 20:17:09 | O |
| `pinsweep/frozen/r28-post/inputs/examples/culture-d4/packet.d4.yml` | 98841 | `543d68a8` | 20:17:09 | O |
| `pinsweep/frozen/r28-post/inputs/examples/culture-d4/typed-labels.d4.yml` | 82161 | `339bfd83` | 20:17:09 | O |
| `readme/reconcile.md` | 9108 | `c7e14ca3` | 20:14:30 | C (README) |
| `readme/sweep.py` | 17117 | `9b2ccac0` | 20:12:13 | C (README) |
| `readme/verify.md` | 5064 | `27cc3229` | 20:14:37 | C (README) |
| `run-validation.py` | 103311 | `6f8db1d2` | 20:18:11 | acceptance runner (O seat) |
| `scribe/capability-row.md` | 24784 | `d3fa86d7` | 20:17:03 | D (**this seat's sibling, R28-D21**) |
| `scribe/frozen-rows.md` | 23707 | `d3a1c039` | 20:17:44 | D (**this seat's sibling, R28-D22**) |
| `scribe/skill-rule-row.md` | 18876 | `a7aa1b2c` | 20:18:02 | D (**this seat's sibling, R28-D23**) |
| `scribe/x54-law-negatives-spotcheck.md` | 18661 | `74b63072` | 20:17:50 | D/X (law negatives spot-check) |
| `scribe/x54-law-negatives-spotcheck.py` | 36191 | `4dbb4132` | 20:16:56 | D/X |
| `scribe/x56-census.py` | 10747 | `9e5ab025` | 20:11:25 | X (census) |
| `sweep/poll-d-landing.py` | 2782 | `21512276` | 20:17:16 | O (landing poll) |
| `sweep/_prelanding-census.md` | 5198 | `34890484` | 20:13:04 | O (pre-landing census) |
| `sweep/repin.py` | 21004 | `9ed68104` | 20:15:57 | O (re-pin tool) |
| `sweep/repin-rows.json` | 8817 | `5aee088d` | 20:17:12 | O (re-pin rows) |
| `sweep/sweep.py` | 31288 | `cec54deb` | 20:12:51 | O (pin sweep) |
| `targets.json` | 191 | `040e3511` | 20:10:20 | declaration (parent) |
| `validation.json` | 230925 | `ef29a513` | 20:17:33 | acceptance runner/receipt |

**The two `pinsweep/baselines/*/r28-post/` directories are collapsed into two
rows above.** They hold 19 and 8 files respectively (snapshot copies of the D4
components, both assemblers, the frozen reader, the packets, the projection and
the expected files). Full per-file rows are in the JSON twin.

**Arithmetic.** 81 files, **2 493 108 bytes**, **51 843 lines**; the evidence
subdirectories are `argot/` (4), `audit/` (18), `gate-tests/` (2), `law/` (3),
`pinsweep/` (35 incl. the two baseline trees and the frozen generation),
`readme/` (3), `scribe/` (6), `sweep/` (5), plus 6 top-level files.

**A caution about this file's own row.** `scribe/fragment-ledger.md`'s row is
blank because this ledger is written **after** the census table was built, so its
own row is stale by construction — exactly the way round 27's ledger recorded the
same for itself. **A consumer re-measures rather than inherits.**

## 2. Outside the partition — the round-28 artifacts and the tool surface

**Two classes of round-28 write landed outside `reports/round-28/`**, measured at
20:18:12Z by `git status --porcelain` (77 untracked entries plus 7 modified):

| path | status | class |
|---|---|---|
| `examples/culture-d4/components/03-orthography.yml` | **M** | **the D claim's RL-4 fix** — `packet_keys: [orthography, records, literacy_institutions]` added (`0f2ff454…`) |
| `examples/culture-d4/components/09-costumes.yml` | **M** | **the RL-4 fix** — `enforcement` added to `packet_keys` (`f61cc684…`) |
| `examples/culture-d4/packet.d4.yml` | **M** | the three new blocks merged (`records:`, `literacy_institutions:`, `enforcement:`); `86079a67…` → **`543d68a8…`** |
| `examples/culture-d4/packet.d4.typed.yml` | **M** | derived (`1c4b8808…` → `15c81ec1…`) |
| `examples/culture-d4/typed-labels.d4.yml` | **M** | derived (`88a94422…` → **`339bfd83…`**) |
| `corpus/README.md` | **M** | the C claim's index reconciliation (revision **1.8**, counts-footer repair) |
| `tools/exercise-handoff-e2e.py` | **M** | `V3_BASELINE_DEFAULT` re-pointed to `reports/round-28/pinsweep/v3-baseline-r28/expected.json` (`:1933`) — **a path that does not exist yet** |

**`reports/round-27/gate-tests/receipt.json` was modified mid-round and then
restored**: it read `M` at 20:13Z and reads clean at 20:18Z. Recorded because the
movement was real.

**The files whose absence is itself the measurement:**

- **`SKILL.md` is byte-still** at `2d85bfea…`, 598 lines. `grep -c "Derivation
  relations" SKILL.md` → **0** and `grep -c "register law\|Register law"` → **0**.
  Both rules have now been absent for **two rounds**, and the three round-28
  D-scribe drafts (`scribe/{capability-row,frozen-rows,skill-rule-row}.md`) are
  drafts like their predecessors.
- **No `SCORECARD.md` or `LOG.md` round-28 entry exists.** Both are the parent's
  integration writes.
- **No `corpus/lessons/round-28.md`** — the lesson set is unchanged.
- **No `reports/round-28/pinsweep/v3-baseline-r28/expected.json`** — the default
  the handoff tool now names. `--profile v3` reads **exit 2** because of it.
- ~~**No `corpus/knowledge/linguistics/<new ceiling entry>`**~~ — **at §1's stamp
  this was true** (`ls corpus/knowledge/linguistics/ | wc -l` → **20**, and
  `register-strata-attestation.md` was **byte-identical to `HEAD`**: 313 lines, 12
  `##` headings). **Both landed after it** — see §4a: the amendment at 20:19:39Z
  (436 lines, 13 `##` headings) and the new entry at 20:20:06Z (287 lines, 21
  entries). The negative is recorded because it was the honest reading at the
  stamp; the correction is recorded because a ledger that hides its drift is not a
  ledger.

**The tool artifacts the round's evidence is about** (sha256 measured 20:15:52Z,
cwd = lane root):

| artifact | sha256 | moved this round? |
|---|---|---|
| `tools/gates/argot-derivation-gate.py` | `b5406bcdaf41c5950438bacd9ccf73ca2e97c044f631f505129cdd0e7e2352fb` | no (moved in round 27) |
| `tools/gates/typed-pipeline-gate.py` | `b749ad07cf1710279aea557c071587cf4b3a228a9fb4d03398b4b94d2f32ad85` | no |
| `tools/gates/naming-collision-gate.py` | `d9e4e8f4f93a21b3b8574856a7d8bc6b93d224eee490ab37ed5f98741a630a1d` | no |
| `tools/gates/d4-typed-labels-check-gate.py` | `05f99629d870280c55e15f46d799c29d7cfbc0645f0d0cd68a5fff1006181841` | no |
| `tools/gates/d4-assembly-check-gate.py` | `df1a364b3970365c217a9b6a16f075bab854ee87aefab831de50df4a9d71544a` | no |
| `tools/assemble-culture-d4.py` | `943f487ba991d45d369eb8fb6e9bb686046df165424d101cfa2670f79bb844b2` | no |
| `tools/assemble-d4-typed.py` | `92f5460bcc34ffbb43a771504d213d23aafd818b39c7017c823a363e99063fd0` | no |
| `tools/gates/typed-pipelines.json` | `69f250df363d70a2001840ab37f4f947e28244b4ac053a5a79d4a92860822f7a` | **no — and it is STALE** (pins `86079a67…`) |
| `examples/culture-d4/packet.d4.yml` | `543d68a82640e1b0c53b9cb7cb26c4dc60fce5878c2bf487050ead3af0945c4f` | **yes** |
| `examples/culture-d4/components/03-orthography.yml` | `0f2ff45439fd7db3e9014bd1012bd917e42d042f457b8cef2bed2c9a791d4e1b` | **yes** |
| `examples/culture-d4/components/09-costumes.yml` | `f61cc6845518d44f50e5179339a1a2fda2c5290efb52d6badb28cbec87768c23` | **yes** |
| `tools/exercise-handoff-e2e.py` | **M** (uncommitted; `V3_BASELINE_DEFAULT` re-pointed) | **yes** |

**No lane gate moved this round.** The `packet_keys` fix is a **component**
change; it needed no gate edit, and none was made. That is the cleanest possible
shape for a packet-surface landing, and it is why every D4 gate's verdict text is
byte-identical to its predecessors (§3).

## 3. The D partition — what the scribe seats and the D seats produced

| artifact | class | what it is |
|---|---|---|
| `law/design.md` | D design | the round-28 law-replay design (seat R28-D01) |
| `law/vocab.md` | D design | the law's field vocabularies: `speaker` resolves against 8 offices + 3 institutions, `register` against 2 names, `axis` against 3 values, **`force` against nothing** |
| `law/rl4-delta.md` | D design | the RL-4 fix priced: `+2 286 bytes`, `+8` records, `+3` blocks, `−3` `skipped_keys`; two sibling blocks deliberately left component-only |
| `argot/D17-law-bypass.md` | D derivation | a law-bypass route |
| `argot/D18-force-overmatch.md` | D derivation | a `force` over-match route |
| `argot/D19-ab-crosscheck.md` | D derivation | an A/B cross-check |
| `argot/D20-ceiling-wording.md` | D derivation | the ceiling's wording |
| `scribe/capability-row.md` | **this seat's sibling (R28-D21)** | the capability-row draft: RL-4 met, RL-1 open, eight tamper routes |
| `scribe/frozen-rows.md` | **this seat's sibling (R28-D22)** | the frozen-row draft: six successor rows, the `r28-post` generation, the `successors: 0/8` gap |
| `scribe/skill-rule-row.md` | **this seat's sibling (R28-D23)** | the SKILL law-replay rule draft, both halves |
| `scribe/x54-law-negatives-spotcheck.py` / `.md` | D/X witness | the independent 14-route law-negative spot-check |
| `audit/x59-register-law-negatives.py` / `.md` | D/X audit | the independent register-law checker (`ruby -ryaml`, own `reverse`/`lengthen`); `--controls` 8/8 |
| `gate-tests/run-gate-tests.py` + `receipt.json` | D/O battery | the round-28 gate-test battery. Its receipt reads **`passed: false`** at 20:17:38Z |

**One measured caution about the gate-tests receipt.** It reads `passed: false`
while the runner's own `--selftest` reads **20/20** — the receipt grades the
delivered tree, and the law leg's absence is what it grades. **A red receipt is
the measurement, not a defect in the battery.**

**And the sibling drafts measure a tree that moved under them.** All three were
written between 20:17:03Z and 20:18:02Z, i.e. **after** the RL-4 landing and
**before** the O seats' `r28-post` freeze; they record the movement and re-stamp.
A consumer must read their §0/§1 stamps rather than inherit a number.

## 4. The movement that matters most — one landing, two successor generations

Recorded because a ledger that hides its own drift is not a ledger. All stamps
UTC, 2026-10-18.

| stamp | `reports/round-28/` files | `packet.d4.yml` | what moved |
|---|---:|---|---|
| 20:10:20 | 2 | `86079a67…` | the declaration (`claims.json`, `targets.json`) |
| 20:11:25 | 5 | `86079a67…` | `scribe/x56-census.py`, `readme/sweep.py`, `sweep/sweep.py` land |
| 20:13:04 | 22 | `86079a67…` | `sweep/_prelanding-census.md`; the audit instruments land |
| **20:13:0x** | ~26 | **`543d68a8…`** | **the RL-4 `packet_keys` fix lands** — three blocks enter the packet; the argot census moves `records=175` → **`183`** |
| 20:14:38 | 29 | `543d68a8…` | `availability.json`, `validation.json`, the C and O fragments |
| **20:17:09** | ~78 | `543d68a8…` | **the O seats freeze `pinsweep/frozen/r28-post/` and `pinsweep/baselines/*/r28-post/`** against the post-fix bytes |
| 20:17:12 | ~78 | `543d68a8…` | `pinsweep/d4-pins.json` and `sweep/repin-rows.json` land |
| **20:18:12** | **81** | `543d68a8…` | this census |

**The load-bearing consequence, measured.** The O seats' round-28 freeze is the
**settled** generation and it replays clean:

```sh
TMPDIR=/var/tmp/r28-d22 python3 tools/replay-frozen.py \
  reports/round-28/pinsweep/frozen/r28-post/MANIFEST.tsv
# REPLAY OK: 2/2 rows reproduced the recorded verdicts
#   (reproduction only: a reproduced red verdict stays red)
```

Its `MANIFEST.tsv` pins exactly the rows §2.1 of the sibling `frozen-rows.md`
proposed — `packet 543d68a8…`, `typed-labels 339bfd83…`, both gates at their live
digests, exits 0, and output shas `c60820a5…`/`1c8add32…` **byte-identical to
every earlier row**. **Two independent seats, two working directories, the same
rows.**

**The round-27 generation is now the superseded one, and its red is supersession
not drift.** `reports/round-27/pinsweep/frozen/r27-post/MANIFEST.tsv` replays
**2 mismatch / 0 reproduced** because its pinned packet `86079a67…` was moved by
the RL-4 landing. `reports/round-28/audit/x61-pin-sweep.py` classifies every such
mismatch as **supersession** (the live input no longer hashes to the pin) rather
than **drift** (a pinned byte was tampered with): `8 mismatch (8 supersession, 0
drift)` at 20:17Z. **`0 drift` is the single most important reading in this
ledger for the O claim's disposition.**

**The residual gap, named and not smoothed.** `x61` also reads
**`successors: 0/8`** — eight superseded frozen rows exist and, at its stamp,
**none** carried a later row at the live digest. The O seats' `r28-post`
generation landed at 20:17:09Z, i.e. **after** that reading; a re-run should show
the count improve. **This ledger does not claim it does.**

## 4a. POST-STAMP DRIFT — the tree moved again after this census

Measured **2026-10-18T20:19:08Z**, 56 seconds after §1's stamp, and recorded
because a ledger that hides its own drift is not a ledger. **The wave is still
writing**, and it is writing **new partitions** rather than only new files.

| artifact | §1/§4 value | 20:19:08Z value | note |
|---|---|---|---|
| `reports/round-28/` file count | **81** (§1) | **88** | the wave added seven artifacts in under a minute |
| `reports/round-28/ceiling/measure-ceiling.py` | **absent** | 12 356 bytes | **a new partition** — the C claim's ceiling measurement seat |
| `reports/round-28/law/review.md` | absent | 17 368 bytes | the D law review lands |
| `reports/round-28/scope.md` | absent | 32 405 bytes | the X scope fragment |
| `reports/round-28/gate-tests/D13-argot-gate.md`, `D14-typed-gate.md` | absent | 6 283 / 6 231 | the gate-test reading fixtures |
| `reports/round-28/gate-tests/receipt.json` | 40 400 | **27 816** | **the receipt shrank** — a rewrite, not an append |
| `reports/round-28/run-validation.py` | 103 311 | **105 435** | still moving; its digest changed again (`6f8db1d2…` → `d4f05458…`) |
| `reports/round-28/audit/x62-frozen-record-audit.py` | 32 078 | **35 223** | |
| `reports/round-28/audit/x63-entry-source-resolvability.py` | 46 296 | **49 192** | |
| `reports/round-28/argot/D17-law-bypass.md` | 25 053 | **30 897** | |

**What did not move, and that is the point.** `packet.d4.yml` is still
`543d68a8…`, `typed-labels.d4.yml` still `339bfd83…`, `expected-holds.json` still
`857417e9…` (still pinning the pre-RL-4 packet), `typed-pipelines.json` still
`69f250df…` (still stale), and **`grep -rl "D4L-LAW" tools/` is still 0** — the law
replay leg has **not** landed.

**The C claim, by contrast, landed all three of its halves between 20:19:39Z and
20:20:23Z**, and the earlier reading of this section named two of them as
undelivered. Recorded because the correction is itself a measurement:

| stamp | what landed | reading before it |
|---|---|---|
| **20:19:39Z** | `corpus/knowledge/linguistics/register-strata-attestation.md` gains **`## 13. Amendment (round 28)`** — 313 → **436 lines**, 12 → **13** `##` headings, **all twelve earlier headings still present** (`ddeeee75…`) | "the entry is byte-identical to `HEAD`" |
| **20:20:06Z** | `corpus/knowledge/linguistics/register-lexicon-ceilings.md` — **287 lines**, frontmatter-complete, gap-named, external sources with calibration; the directory **20 → 21** | "no new ceiling entry exists" |
| **20:20:23Z** | `corpus/README.md` **revision 1.9** — an index row for the new entry (`:138`) and `Total knowledge entries: 201.` (`:469`) | "the index has not yet been reconciled" |
| **20:20:4xZ** | **`tools/gates/register-law-gate.py`** — the law replay leg (`cfbff16b…`), with eight named `D4L-LAW-*` finding ids | "`grep -rl D4L-LAW tools/` → 0" |
| **20:22:3xZ** | `examples/culture-d4/expected-holds.json` re-pinned to `65f5a03e…` (counts stay **12/0/0**); `tools/gates/typed-pipelines.json` re-pinned | "both still pin the pre-RL-4 packet" |
| **20:22:5xZ** | `reports/round-28/pinsweep/v3-baseline-r28/` — `--profile v3` goes **exit 2 → exit 0** | "that path does not exist yet" |
| **~20:28Z** | the `r28-post` frozen generation extended **2 → 4** rows (the typed gate's two D4 rows), replays **4/4** | the `X61R28-A2` gap this round's own audit named |

**Every claim this ledger recorded as undelivered at its stamp has since landed,
and the round's acceptance runner reads `claim D: PASS`, `claim O: PASS`,
`claim C: PASS`, `acceptance_checks_passed: True` (20:30:08Z).** The negatives are
kept above because they were the honest readings at their stamps, and because the
sequence — a leg landing at the wire, a constant re-pointed before its artifact,
a generation extended after its gap was named — is the round's actual shape.

**The C claim is therefore delivered in the amendment shape it specified** — a new
section, never an in-place rewrite — and its README reconciliation is landed, not
pending.

**What this means for a consumer, plainly.** The siblings
(`capability-row.md`, `frozen-rows.md`, `skill-rule-row.md`) and this ledger all
bind to the **20:15–20:19Z** stamps. The **qualitative findings are stable** — RL-4
is fixed and confirmed, RL-1 is open, the O seats' `r28-post` generation replays
2/2, the C claim is delivered — but **no digest in any of the four files may be
quoted without re-hashing**, and §1's file count is already seven out of date.
That is the round-25 lesson's own discipline ("a pin taken on bytes that are still
moving is not a pin") restated for round 28. **The one D leg that no sibling
landing touched is the replay leg.**

## 4b. THE TWIN IS REGENERATED AT A LATER STAMP — read it, do not assume it

`reports/round-28/scribe/fragment-ledger.json` carries the **same row schema** as
§1 but its own `census_utc`, which is **later than §1's table** because the twin is
written after the table is built. At the twin's last regeneration:

```
census_utc  2026-10-18T20:31:09Z      (56 s after §4a's reading)
files       130                        (§1's table: 81)
partitions  top-level 7, argot 4, audit 26, ceiling 13, gate-tests 6,
            law 12, pinsweep 42, readme 3, scribe 9, sweep 8
```

**A counting caveat so two honest counts reconcile.** An independent 60 s poll
run by this seat counted **133** files at the same time the twin counted **130**.
Both are right: the twin excludes `__pycache__` (three `.pyc` files under
`audit/`, `pinsweep/` and `sweep/`), and the poll did not. **A file count over
`reports/round-28` is only comparable if the `__pycache__` policy is stated** —
the twin states it, and §5's commands carry `-not -path "*__pycache__*"` for the
same reason.

**The partition grew from 81 to 130 files inside the same round**, because the D
and C seats landed their full evidence sets (`law/` 3 → 12, `ceiling/` 0 → 13,
`audit/` 18 → 26). The twin also carries `negative_measurements` at its own stamp,
and one entry there is worth flagging: **`law_replay_gate_sha256` changed again**
(`cfbff16b…` at 20:22Z → **`bbad3578…`** at 20:31Z) — the D seats are still
refining the gate after it first landed, with `--selftest` reading **33/33** at
both stamps. **A consumer must re-hash the gate rather than quote either digest.**

This is the same discipline round 27's ledger applied to itself: **a consumer
re-measures rather than inherits.**

## 5. Counting commands for this file

```sh
export TMPDIR=$PWD/.scratch
find reports/round-28 -type f -not -path "*__pycache__*" | sort
find reports/round-28 -type f -not -path "*__pycache__*" | wc -l      # 81 at 20:18:12Z
git status --porcelain | wc -l                                        # 84 (7 modified + 77 untracked)
git status --porcelain                                                # the seven outside writes (§2)
ls corpus/knowledge/linguistics/ | wc -l                              # 21 at 20:20:06Z (was 20)
git show HEAD:corpus/knowledge/linguistics/register-strata-attestation.md | wc -l   # 313, unchanged
grep -c "Derivation relations" SKILL.md                               # 0 — two rounds absent
grep -c "register law\|Register law" SKILL.md                         # 0 — never landed
grep -rl "D4L-LAW" tools/ | wc -l                                     # 0 — no replay leg
ls reports/round-28/pinsweep/v3-baseline-r28 2>&1                     # absent — the v3 default
sha256sum examples/culture-d4/packet.d4.yml examples/culture-d4/typed-labels.d4.yml \
  examples/culture-d4/components/03-orthography.yml examples/culture-d4/components/09-costumes.yml \
  tools/gates/typed-pipelines.json
TMPDIR=/var/tmp/r28-d22 python3 tools/replay-frozen.py \
  reports/round-28/pinsweep/frozen/r28-post/MANIFEST.tsv | tail -1    # REPLAY OK 2/2
python3 tools/check-gate-battery.py | tail -8                         # 7 pass / 0 fail; coverage 9/9
python3 reports/round-28/audit/x61-pin-sweep.py | tail -3
python3 reports/round-28/run-validation.py --check | tail -6
```

## 6. What this ledger does not do

- It **admits nothing**: no claim D/O/C verdict, no promotion, no canon. The
  round's counting command (`python3 reports/round-28/run-validation.py`) **ran**
  and wrote `reports/round-28/validation.json`; the receipt is the verdict, and
  this ledger only records that it exists. **It is not green**: the D claim's
  replay leg, the O claim's v3 baseline and the C claim's ceiling entry are all
  undelivered at this stamp.
- It **certifies no fragment**. The owner column is inferred from path
  convention; the byte/sha/mtime cells are measured and bound to the stamp beside
  them.
- It **reads no fragment in full**. Where §3 says "presence and size are
  measured", that is what was done.
- It **does not re-derive** the sibling scribe drafts' findings. §3 cites their
  digests and the cross-checks that matter (the `r28-post` replay and the
  byte-identical gate stdout).
- It **edits no filed byte**: no round-8–27 artifact, no `MANIFEST.tsv`, no
  `expected.json`, no receipt, no tool, gate, example, component or packet. Its
  own write is confined to `reports/round-28/scribe/`.
