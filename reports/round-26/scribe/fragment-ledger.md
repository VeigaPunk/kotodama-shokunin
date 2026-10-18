# R26-D28 — round-26 fragment ledger (read-time census)

- round: 26 (operator: loop 3 of 3, build round 2 of 4; 64 declared workers,
  `devin/deepseek-v4-1-flash-high`). Seat **R26-D28** (D-scribe 4 of 4).
- date: 2026-10-18. Lane head `1ad491a1a4b0aef9ebdc1861dfb8237727503825`
  (declared baseline `fc13cd27b9e78d5d7c4f70740fd26c9383a7447b`, round-25 admit).
- **writes: this file and its machine-readable twin
  `reports/round-26/scribe/fragment-ledger.json`**, plus gitignored scratch under
  `.scratch/r26d/`. No commit, no push; no filed artifact of rounds 8–25 touched.
- canon: **NON-CANON integration ledger.** It admits nothing, certifies no
  round, and blesses no fragment. It is the index the parent uses to integrate
  the wave.

## 0. What this ledger is, and what it is not

A **read-time census** of every file under `reports/round-26/` at
**2026-10-18T18:08:19Z**, with byte size, line count, sha256 (8-char prefix
shown), mtime and an inferred owner seat, plus the round-26 artifacts that landed
**outside** that partition and the **tool** artifacts the wave's evidence is
about.

It is **not** a completeness claim and **not** a round verdict. **The wave was
still writing at the census and kept writing after it.** `reports/round-26/` grew
**2 → 7 → 15 → 16 → 36 → 41 → 44 → 47 → 48** files between 17:59:43Z and
18:08:19Z, and individual artifacts moved under the reads: `run-validation.py`
`19 955 → 44 891` bytes and `401 → 904` lines in 27 seconds; `register/design.md`
`14 251 → 14 451` bytes in 20 seconds; `argot/D21-adversarial-replay.md`
`14 197 → 14 725` bytes in a minute; `audit/x60-register-derivation-spotcheck.py`
`22 666 → 22 909` bytes. **Every cell in §1 binds to the 18:08:19Z stamp only.**
Re-run on the settled tree:

```sh
export TMPDIR=$PWD/.scratch
python3 .scratch/r26d/census.py > .scratch/r26d/census.json   # or the commands in §5
find reports/round-26 -type f | sort
ls corpus/lessons/*.md | wc -l
```

The machine-readable twin carries the same rows plus `declared_baseline`,
`lane_head`, `census_utc`, `counts`, `negative_measurements` and `stamps`.

**Census stamps used in this file.** The §1 table was rebuilt at
**2026-10-18T18:08:19Z (48 files, 945 329 bytes, 17 007 lines)** and supersedes
this seat's earlier tables at 18:04:32Z (7), 18:04:56Z (16), 18:05:17Z (16),
18:07:19Z (36), 18:07:42Z (41), 18:07:49Z (44) and 18:08:13Z (47). Rows that
changed between stamps are the wave's own movement, not a re-measurement of the
same bytes. **A consumer must re-measure rather than inherit.**

## 1. Census — `reports/round-26/**` (48 files, 2026-10-18T18:08:19Z)

Owner seats are **inferred from the path convention** (the seat id in the
filename or the partition), not from a per-file declaration; where the convention
gives nothing the cell says so. An inferred owner is a pointer, never an
authorship claim.

| path | bytes | lines | sha8 | mtime UTC | owner seat (inferred) |
|---|---:|---:|---|---|---|
| `__pycache__/run-validation.cpython-314.pyc` | 27278 | 150 | `ebc4435f` | 18:07:35 | unattributed (path convention gives no seat) |
| `argot/D21-adversarial-replay.md` | 14725 | 273 | `aa401251` | 18:08:15 | D (argot analysis) |
| `argot/D22-label-typing-crosscheck.md` | 11585 | 211 | `2892404f` | 18:06:30 | D (argot analysis) |
| `argot/D23-overmatch.md` | 11191 | 200 | `7d31da7d` | 18:07:23 | D (argot analysis) |
| `argot/D24-forecast-closure.md` | 12247 | 167 | `c7581a02` | 18:07:49 | D (argot analysis) |
| `audit/x60-register-derivation-spotcheck.md` | 17312 | 292 | `541abd22` | 18:07:23 | X (audit seats) |
| `audit/x60-register-derivation-spotcheck.py` | 22909 | 593 | `31eebca8` | 18:07:59 | X (audit seats) |
| `audit/x63-lessons-audit.md` | 16876 | 275 | `ed933058` | 18:07:04 | X (audit seats) |
| `audit/x63-lessons-audit.py` | 22851 | 478 | `33e27e78` | 18:05:27 | X (audit seats) |
| `audit/x63-lessons-receipt.json` | 4912 | 214 | `d90aebc2` | 18:06:53 | X (audit seats) |
| `availability.json` | 20144 | 255 | `bc8d5465` | 18:07:41 | X (availability, R26-X59) |
| `claims.json` | 2383 | 33 | `363498ed` | 17:59:43 | declaration (parent) |
| `gate-tests/fixtures/n1-maximal-coda.yml` | 539 | 11 | `460cae84` | 18:05:57 | D/X (gate-test battery) |
| `gate-tests/fixtures/n2-rule-mismatch.yml` | 485 | 13 | `ef2ad71b` | 18:05:57 | D/X (gate-test battery) |
| `gate-tests/fixtures/n3-positive-control.yml` | 553 | 14 | `92e14150` | 18:05:57 | D/X (gate-test battery) |
| `gate-tests/fixtures/n4-unknown-rule.yml` | 350 | 7 | `77b31d15` | 18:05:57 | D/X (gate-test battery) |
| `gate-tests/fixtures/n5-borrow-mismatch.yml` | 339 | 6 | `04f54be6` | 18:05:57 | D/X (gate-test battery) |
| `gate-tests/fixtures/n6-coverage-hold.yml` | 408 | 9 | `5b455472` | 18:05:57 | D/X (gate-test battery) |
| `gate-tests/fixtures/n7-malformed.yml` | 46 | 2 | `c19d69c0` | 18:05:57 | D/X (gate-test battery) |
| `gate-tests/freeze.py` | 9070 | 219 | `f8853dc1` | 18:08:04 | D/X (gate-test battery) |
| `gate-tests/receipt.json` | 100640 | 2160 | `cf19a9fc` | 18:06:57 | D/X (gate-test battery) |
| `gate-tests/run-gate-tests.py` | 26118 | 554 | `b30f181c` | 18:07:55 | D/X (gate-test battery) |
| `lessons/C53.md` | 19950 | 284 | `b71fe796` | 18:08:10 | C (lessons census) |
| `lessons/r26-census.py` | 8295 | 224 | `e560c023` | 18:07:36 | C (lessons census) |
| `open-questions/build-dispositions.py` | 42812 | 645 | `c48b357b` | 18:07:26 | C (open-question dispositions) |
| `open-questions/dispositions.json` | 94032 | 2561 | `6812dbc5` | 18:07:59 | C (open-question dispositions) |
| `open-questions/dispositions.md` | 7964 | 113 | `8e5022bd` | 18:07:59 | C (open-question dispositions) |
| `open-questions/verify-dispositions.py` | 7179 | 179 | `2ea881b3` | 18:07:54 | C (open-question dispositions) |
| `open-questions/verify.json` | 765 | 37 | `9a7c76de` | 18:07:50 | C (open-question dispositions) |
| `register/design.md` | 14451 | 244 | `15505be7` | 18:08:07 | D (register stratum) |
| `remainders/pin-repoint-check.py` | 12165 | 262 | `5674a6b3` | 18:06:54 | O (remainders) |
| `remainders/pin-repoint-receipt.json` | 4722 | 136 | `ffe8269d` | 18:07:04 | O (remainders) |
| `remainders/v2-successor-r26/expected.json` | 4435 | 70 | `f695b910` | 18:04:35 | O (remainders) |
| `remainders/v3-baseline-r26/expected.json` | 10856 | 208 | `4879e760` | 18:04:39 | O (remainders) |
| `remainders/v3-baseline-r26/freeze.txt` | 521 | 8 | `adad86ab` | 18:04:39 | O (remainders) |
| `remainders/v3-baseline-r26/packet.md` | 105582 | 335 | `a97a0f0a` | 18:04:39 | O (remainders) |
| `remainders/v3-baseline-r26/run.log` | 1603 | 14 | `ba68aee7` | 18:04:39 | O (remainders) |
| `remainders/v3-baseline-r26/twin.json` | 103155 | 2598 | `d3de56a8` | 18:04:39 | O (remainders) |
| `report-draft.md` | 12427 | 75 | `a48c9dd4` | 18:07:54 | unattributed (path convention gives no seat) |
| `run-validation.py` | 44891 | 904 | `10fafb94` | 18:07:38 | acceptance runner (O seat) |
| `scope.md` | 13386 | 140 | `12681452` | 18:04:50 | X (scope) |
| `scribe/capability-row.md` | 21731 | 310 | `96adcfe3` | 18:05:47 | D (scribe seats — **this seat's sibling**) |
| `scribe/fragment-ledger.json` | 17076 | 514 | `592f1730` | 18:08:13 | D (scribe seats — **this file's twin**) |
| `scribe/fragment-ledger.md` | 16160 | 243 | `e878b3aa` | 18:08:09 | D (scribe seats — **this file, superseded by its own next write**) |
| `scribe/frozen-rows.md` | 24656 | 366 | `72dbcfef` | 18:07:14 | D (scribe seats — **this seat's sibling**) |
| `scribe/skill-rule-row.md` | 18337 | 222 | `15e4b2a9` | 18:06:33 | D (scribe seats — **this seat's sibling**) |
| `scribe/x64-d4-chain-cold-rerun.md` | 15025 | 168 | `8bf6cdfc` | 18:07:28 | D (scribe seats) |
| `targets.json` | 192 | 11 | `50a30752` | 17:59:43 | declaration (parent) |

**Arithmetic.** 48 files, **945 329 bytes**, **17 007 lines**; 9 evidence
subdirectories (`argot`, `audit`, `gate-tests` + its `fixtures`, `lessons`,
`open-questions`, `register`, `remainders` + two revision dirs, `scribe`) plus
`__pycache__` and 7 top-level files.

**A caution about this file's own row.** `scribe/fragment-ledger.md`'s row shows
the bytes of a **previous** write. This ledger is rewritten to the 18:08:19Z
table, so its own row is stale by construction, exactly the way
`corpus/lessons/round-25.md`'s row was stale in the round-25 README. The twin
(`fragment-ledger.json`) was regenerated after the table and carries the same 48
rows; a consumer re-measures rather than inherits.

**The wave kept growing after this stamp.** At 18:09:53Z the partition held
**57 files / 1 055 319 bytes / 19 108 lines** — nine more files than §1's table,
including `lessons/C53.md`, `gate-tests/freeze.py`, `open-questions/dispositions.md`
and this seat's own rewrites. **§1's table is a 18:08:19Z snapshot, not the
round's file list.** The §5 commands reproduce the live count.

## 2. Outside the partition — the round-26 artifacts and the evidence surface

**One artifact landed outside `reports/round-26/` this round:**
`tools/gates/frozen/round-26/` (16 files, 1 146 670 bytes, untracked at
18:09:53Z), the new frozen generation — the response to the pin cascade, recorded
at `freeze-receipt.json` `frozen_at: 2026-10-18T18:08:08.652644+00:00` and
replaying **6/6 OK**. It is not part of §1's partition, and it is the round's
only `tools/` write. Measured 2026-10-18T18:09:53Z:

```sh
git status --porcelain
# ?? reports/round-26/… (12 untracked paths, all inside the partition)
# ?? tools/gates/frozen/round-26/          <- the new generation
find tools/gates/frozen/round-26 -type f | wc -l   # 16
```

At the §1 stamp (18:08:19Z) there was **no** `corpus/lessons/round-26.md`
(`ls corpus/lessons/*.md | wc -l` → **26**, the same set round 25 left). **It
landed afterwards**: at 18:12:12Z `corpus/lessons/round-26.md` exists
(`37 265 B`, 145 lines, `sha256 c9cf68e6c14e4546bdadb8837a54a43c3bdbf94864f8424304d35e56c61fc745`,
mtime 18:11Z) and the lesson count is **27**. That file is the X56 gate-keeper
lesson, and it cites this ledger by path (`corpus/lessons/round-26.md` `scope:`
records that this file's own `:115` was the only pre-existing reference). **A
round-26 lesson therefore exists at this seat's close, and this ledger did not
create it** — this seat writes only `reports/round-26/scribe/`.

No `corpus/lessons/README.md` revision had landed at either stamp — the C claim
requires the README revision to be a **new file** with the filed bytes
byte-unchanged, and at this seat's close neither the revision nor the change
exists.

**No pre-existing tool, gate, example, component or packet was modified this
round; one new frozen generation was added.** This is measured, not assumed:
`git status --porcelain` lists no modification (` M`) under `tools/`,
`examples/`, `corpus/` or `SKILL.md`/`SCORECARD.md`/`LOG.md` — only untracked
paths (`corpus/lessons/round-26.md`, `tools/gates/frozen/round-26/`) — and every
digest below is byte-equal to its round-25-settled value.

**The tool artifacts the round's evidence is about** (sha256 measured
18:05:08Z, cwd = lane root):

| artifact | sha256 | moved this round? |
|---|---|---|
| `tools/gates/argot-derivation-gate.py` | `5b5abe7865ed906c23fba87fd0dae8b6187c8dfc1a80137adbd364d4d88b0211` | no (round 25 settled it) |
| `tools/gates/typed-pipeline-gate.py` | `b749ad07cf1710279aea557c071587cf4b3a228a9fb4d03398b4b94d2f32ad85` | no (equal at the declared baseline `fc13cd2`) |
| `tools/gates/naming-collision-gate.py` | `d9e4e8f4f93a21b3b8574856a7d8bc6b93d224eee490ab37ed5f98741a630a1d` | no |
| `tools/gates/d4-typed-labels-check-gate.py` | `05f99629d870280c55e15f46d799c29d7cfbc0645f0d0cd68a5fff1006181841` | no |
| `tools/gates/d4-assembly-check-gate.py` | `df1a364b3970365c217a9b6a16f075bab854ee87aefab831de50df4a9d71544a` | no |
| `examples/culture-d4/packet.d4.yml` | `e7ecd2045ef0e5f9823ce0a067d21b8221b2ceb5e8f5799736981a1c88fa50d3` | no |
| `examples/culture-d4/typed-labels.d4.yml` | `60b526b0b3d07141875d20c472451cdf6658f61936d39fe18af4f3d981981092` | no |
| `examples/culture-d4/expected-holds.json` | `3826ba68d705b3c379b2a12737c14075d9095a1ba2aa2eb525de1851a9ecd2f7` | no |
| `tools/gates/frozen/round-25/gate-input/MANIFEST.tsv` | `40e6c28d…` | no |

**The load-bearing negative measurement: the register stratum is not on disk.**
`grep -rls "D4L-REGISTER-UNRESOLVED\|doublet_of" examples/ tools/` → **0 files**,
re-measured at 18:03:17Z, 18:05:08Z, 18:06:36Z, 18:07:38Z and 18:08:15Z. Claim
D's central artifact therefore did **not** land, and §3 lists the `register/`
partition (one file, `design.md`) as **design only** at this stamp. This is the
census's most important row and it is a negative one.

## 3. The D partition — what the scribe seats and the D seats produced

Named so the parent can see the D claim's evidence surface without reading 48
files.

| artifact | class | what it is |
|---|---|---|
| `argot/D21-adversarial-replay.md` | D evidence | adversarial replay of the argot leg (presence and size measured; not read in full by this seat) |
| `argot/D22-label-typing-crosscheck.md` | D evidence | label-typing cross-check |
| `argot/D23-overmatch.md` | D evidence | over-match analysis |
| `argot/D24-forecast-closure.md` | D evidence | the forecast-closure fragment |
| `register/design.md` | **design only** | the register stratum's design; **no code, no schema, no packet** — the stratum is not on disk (§2) |
| `gate-tests/run-gate-tests.py` + `freeze.py` + `fixtures/n1..n7` + `receipt.json` | D/X battery | a gate-test battery with 7 fixtures (`maximal-coda`, `rule-mismatch`, `positive-control`, `unknown-rule`, `borrow-mismatch`, `coverage-hold`, `malformed`) and a 100 640-byte receipt |
| `scribe/capability-row.md` | **this seat's sibling (R26-D25)** | the capability-row draft; 21 731 B / 310 lines / `96adcfe3` |
| `scribe/skill-rule-row.md` | **this seat's sibling (R26-D26)** | the SKILL register-rule row draft; 18 337 B / 222 lines / `15e4b2a9` |
| `scribe/frozen-rows.md` | **this seat's sibling (R26-D27)** | the frozen-rows draft; 24 656 B / 366 lines / `72dbcfef` |
| `scribe/x64-d4-chain-cold-rerun.md` | D/X | a cold re-run of the D4 chain |
| `audit/x60-register-derivation-spotcheck.py/.md` | X audit | an independent register-derivation instrument (different parser: `ruby -ryaml`) with a `--controls` mode |

**One measured caution about the sibling files.** `capability-row.md`,
`skill-rule-row.md` and `frozen-rows.md` are this seat's lane-mates' drafts, and
they are **drafts**: none landed a `SCORECARD.md`/`SKILL.md` row. The measured
fact that makes this concrete: `grep -c "Derivation relations" SKILL.md` → **0**,
i.e. the **round-25** SKILL rule that `skill-rule-row.md` builds on never landed
either (`SKILL.md` byte-still at `2d85bfea…`, 598 lines, last written `e06581b`).

## 4. Movement under this seat's reads — the stamps that matter

Recorded because a ledger that hides its own drift is not a ledger. All stamps
UTC, `2026-10-18`.

| stamp | `reports/round-26/` files | bytes | what moved |
|---|---:|---:|---|
| 17:59:43 | 2 | — | `claims.json`, `targets.json` (the declaration) |
| 18:04:32 | 7 | — | audit, availability, lessons, scope land |
| 18:04:56 | 16 | — | `remainders/` v2 + v3 revision dirs land |
| 18:05:17 | 16 | — | `x63-lessons-audit.md` lands |
| 18:07:19 | 36 | — | `argot/`, `gate-tests/`, `open-questions/`, `run-validation.py` land |
| 18:07:42 | 41 | 841 100 | `open-questions/dispositions.md`, `verify-dispositions.py` land |
| 18:07:49 | 44 | 881 431 | `argot/D24`, `register/design.md`, `report-draft.md` land |
| 18:08:13 | 47 | 927 725 | `gate-tests/freeze.py`, `lessons/C53.md`, this ledger land |
| **18:08:19** | **48** | **945 329** | `argot/D21` re-written |

**Four artifacts moved inside a single 40-second window**, and the most
load-bearing is the acceptance runner:

- `reports/round-26/run-validation.py` — `19 955 B / 401 lines` at 18:07:11Z →
  `44 891 B / 904 lines` at 18:07:38Z, and it **still carries no `__main__`
  block** at this stamp (`grep -c "__main__"` → **0**), so `python3
  reports/round-26/run-validation.py --selftest` and `--check` both exit **0
  with empty stdout** — the file compiles and imports, but it does not yet
  dispatch. **The declared counting command is therefore not yet runnable.**
- `reports/round-26/gate-tests/run-gate-tests.py` — `24 849 B` (18:06:38Z) →
  `25 570 B` (18:07:48Z) → `26 118 B` (18:07:55Z).
- `reports/round-26/audit/x60-register-derivation-spotcheck.py` — `22 666 B`
  (18:03:36Z) → `22 909 B` (18:07:59Z).
- `reports/round-26/register/design.md` — `14 251 B` (18:07:47Z) → `14 451 B`
  (18:08:07Z).
- `reports/round-26/run-validation.py` — `10fafb94…` (no dispatch) at 18:09:47Z →
  `1096269f…` (dispatch present, `grep -c "__main__"` → **1**) at 18:11:12Z →
  `1f74a85f…` at 18:11:49Z. It is now runnable: `--selftest` reads **29/29
  checks passed**, exit 0.

**The declared counting command's first runs, measured by this seat.**

```sh
export TMPDIR=$PWD/.scratch
python3 reports/round-26/run-validation.py --selftest     # 29/29, exit 0
python3 reports/round-26/run-validation.py --check        # exit 2:
# could-not-evaluate: SameFileError:
#   …/reports/round-26/adjacency.md and …/reports/round-26/adjacency.md are the same file
```

The `--check` refusal is an **input-class refusal, not a verdict**: the runner
tries to copy a file onto itself, and it names the path. It reproduced across two
stamps (18:11:12Z and 18:11:49Z) and two runner digests (`1096269f…`,
`1f74a85f…`), so it is not a one-off. **No `reports/round-26/validation.json`
receipt exists**, and the claim's `counting_command` (`python3
reports/round-26/run-validation.py`) therefore has no receipt at this seat's
close. This is recorded as a measured obstacle for the parent, not as a defect
diagnosis — the runner is mid-write and this seat did not edit it.

A consumer that ran any of them earlier read a different file. This is the
round-25 lesson's own discipline ("a pin taken on bytes that are still moving is
not a pin") restated for the round-26 wave, and it is why §1's table carries a
single stamp.

## 5. Counting commands for this file

```sh
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
python3 .scratch/r26d/census.py > .scratch/r26d/census.json      # this seat's census
find reports/round-26 -type f | sort                              # 48 at 18:08:19Z; 57 at 18:09:53Z
find reports/round-26 -type f | wc -l
find tools/gates/frozen/round-26 -type f | wc -l                  # 16 — the round's one tools/ write
git status --porcelain                                            # reports/round-26/… plus tools/gates/frozen/round-26/
ls corpus/lessons/*.md | wc -l                                    # 26 — no round-26 lesson yet
grep -c "__main__" reports/round-26/run-validation.py             # 1 at 18:11:12Z (0 at 18:09:47Z — it moved)
python3 reports/round-26/run-validation.py --selftest             # 29/29, exit 0
python3 reports/round-26/run-validation.py --check                # exit 2, SameFileError on adjacency.md
grep -rls "D4L-REGISTER-UNRESOLVED\|doublet_of" examples/ tools/  # 0 — the stratum is not on disk
sha256sum tools/gates/argot-derivation-gate.py tools/gates/typed-pipeline-gate.py \
  examples/culture-d4/packet.d4.yml examples/culture-d4/expected-holds.json
grep -c "Derivation relations" SKILL.md                           # 0 — the round-25 rule never landed
```

## 6. What this ledger does not do

- It **admits nothing**: no claim D/O/C verdict, no promotion, no canon. The
  round's counting command (`python3 reports/round-26/run-validation.py`) had
  **no receipt** at any stamp in this seat's window, and at 18:08:19Z the runner
  could not dispatch (§4).
- It **certifies no fragment**. The owner column is inferred from path
  convention; the byte/line/sha cells are measured and bound to the stamp beside
  them.
- It **reads no fragment in full**. Where §3 says "presence and size are
  measured", that is what was done; the content of `argot/D21..D24`,
  `register/design.md`, the `gate-tests` battery and the `open-questions`
  dispositions is not characterized here.
- It **does not re-derive** the sibling scribe drafts' findings. §3 cites their
  digests and the one cross-check that matters (the absent round-25 SKILL rule),
  and stops.
- It **edits no filed byte**: no round-8–25 artifact, no `MANIFEST.tsv`, no
  `expected.json`, no receipt, no tool, gate, example, component or packet.
