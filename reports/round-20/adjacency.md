# R20-X23 — adjacency / connector: lore-boundary check on all round-20 content

- seat: **R20-X23** (scribe, adjacency/connector), round 20 (operator loop 2 of 3,
  build round 4 of 4; 64 workers on `opencode-go/deepseek-v4.1-flash`). Lane
  `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
- assignment (verbatim): "SCRIBE X23: adjacency/connector."
- writes: **this file only**, plus gitignored scratch under `.scratch/x23/`
  (`export TMPDIR=$PWD/.scratch` preceded every scratch-writing command; the
  watcher at `.scratch/x23/watch.py` logs `.scratch/x23/watch.jsonl`). This seat
  edits no filed byte, no tool, gate, pin, packet or corpus file; it makes no
  commit and no push. It does **not** run the counting command
  `reports/round-20/run-validation.py` (round-14 guard: a counting command can
  itself be a writer — and this round's own incident, §1.4, is that guard
  materialised). It runs only read-only instruments, each named in §4.
- revision binding: lane `HEAD = 122086bce0aa577bec221bb2d37eedf20f4f3ed2`
  ("round-20: declare claims D/O/C", 2026-10-18T09:53:37-03:00), **unmoved at
  every check**; `HEAD^ = caf1beac19b55f3bbce47e4a9e7e8710cc1c581d` = the declared
  `baseline_revision` (`reports/round-20/claims.json:5`, round-19 admit). Fleet
  root HEAD unchanged; fleet root porcelain 0 throughout.
- clock: all stamps UTC; lane-local clock is UTC−03:00.
- canon: **NON-CANON engineering record.** Nothing here admits a round, a
  capability or a canon fact. Boundary observations only.
- status: **live in-flight audit** — the wave was writing through the whole
  window (observation window 12:54–13:40Z; first round-20 artifact after the
  declaration landed 12:56:40Z, the tree read 81 round-20 files at 13:39:53Z and
  `tools/exercise-handoff-e2e.py` was still changing at 13:35:40Z). Every list
  and count is a stamped snapshot, not a close.

## 0. Verdict summary

| # | check | verdict | key evidence |
|---|---|---|---|
| 1 | No canon decision recorded (lore's province) | **pass** | §3.1 — assertion-shaped sweep → 0 residual; 9 deferral-shaped hits classified |
| 2 | Every reference to the lore handoff contract is read-only | **pass** | §3.2 — contract `5f4c02bf…` identical at baseline/HEAD/worktree |
| 3 | No write outside `kotodama-shokunin/` | **pass with observation** | §3.4 — fleet root 0; lore sibling dirty with 0 kotodama refs; two `/tmp` scratch mirrors noted |
| 4 | Filed rounds 8–19 untouched | **pass, one recorded incident** | §1.3–1.4 — 892 tracked / 897 on-disk byte-identical; rounds 5/7/9 were transiently rewritten 13:00:55–13:01:01Z and restored 13:03:17Z |
| 5 | `PROVINCE.md` still accurate; no absorption | **pass** | §2 — `05b34a57…` unchanged; every round-20 surface maps onto `Owns` |
| 6 | L0 surface untouched | **pass** | §3.5 — `../.ufo/l0-questions.md` mtime 2026-10-17 19:34:37, unchanged |
| 7 | New-content boundary discipline | **pass with observations** | §3.3 — every round-20 artifact NON-CANON; canon deferrals throughout |
| 8 | Connector: claim ↔ evidence references | **pass with 2 routed refs** | §4, §5 — 669 backticked refs, 18 distinct unresolved, all classified |

## 1. Git-scope

### 1.1 Fleet root — clean at every stamp

```sh
cd /home/vgpnk/Projects/shokunin && git status --porcelain -uall | wc -l   # → 0 @ 12:55Z, 13:33:41Z, 13:39Z
```

`*-shokunin/` is ignored by the fleet `.gitignore` (line 1), so the busy lane
tree is invisible to fleet git by design; the 0 is the out-of-lane write check.

### 1.2 Lane tree — HEAD unmoved; no commit

`git rev-parse HEAD` → `122086bc…` at every check (12:55Z–13:39Z). No worker
commit, no push. The declaration commit touched exactly
`reports/round-20/{claims,targets}.json` (`git diff --name-status caf1bea HEAD`).

### 1.3 Filed rounds 8–19 — byte-identical

```sh
git status --porcelain reports/round-{8..19} | wc -l        # → 0 @ 13:33:41Z, 13:39Z
git ls-files reports/round-{8..19} | wc -l                  # → 892 tracked
find reports/round-{8..19} -type f ! -path '*__pycache__*' | wc -l   # → 897 on disk (5 git-ignored *.log)
```

The runner's own filed leg (`reports/round-20/validation.json`,
`filed_rounds.baseline`, stamp 13:21:07Z) compares **897** baseline Git blobs
against the live bytes: all `byte-identical`, `violations 0`,
`untracked_ignored` counted informationally. Rounds 5–7 (outside the operator's
declared range) are recorded separately as `outside_scope`: `changed 0` at that
stamp.

### 1.4 The recorded incident — rounds 5/7/9 `validation.json` transiently rewritten, then restored

**What happened.** At 13:00:55Z / 13:00:58Z / 13:01:01Z the worktree showed
` M reports/round-5/validation.json`, ` M reports/round-7/validation.json`,
` M reports/round-9/validation.json` (mtimes, `stat -c %y`; round 9 is **inside**
the operator's protected 8–19 set). The diffs replaced each file's claim-O error
block and/or counts with a fresh re-run's output (round-5: `replay-frozen.py`
`gate_digest_mismatch` string + `tested_file_sha256["tools/check-gate-battery.py"]`
`0a126b70… → cd8c0ec2…`; round-7: knowledge-inventory totals 189→199 files;
round-9: `acceptance_checks_passed true → false`, +594 lines).

**Mechanism (named, not a person).** A round-20 gap-measurement run executed the
historical counting commands live; each validator writes its own filed receipt as
a side effect (`reports/round-5/run-validation.py:194` →
`(HERE / "validation.json").write_text(...)`). The runner of that measurement is
evidenced by `.scratch/r20-c-gaps/stamp.txt` (`stamp 2026-10-18T13:00:53Z`) with
its per-round captures `r5-run.json`, `r6-run.json`, `r7-run.json`,
`r9-run.json` (13:00–13:01Z); round-6's re-run produced byte-identical output and
therefore no diff. This is the round-14 guard materialised: a counting command
can itself be a writer.

**Restoration.** By 13:03:17Z all three paths carried an identical batch mtime
and `git status --porcelain reports/round-{5,7,9}` → 0; the worktree bytes are
back to the baseline. The runner's later stamps (13:21:07Z) measure `changed 0`
for rounds 5–7 and 897/897 for 8–19 — i.e. the runner ran after the restore and
does not measure the transient.

**Independent corroboration (same class, other seats).** X17's round lesson
(`corpus/lessons/round-20.md:120`, 13:00:02Z snapshot) records the same mutation
"inside this survey's window by live seats … the parent owns the disposition";
X19/X20's scribe scratch captured the diffs (`.scratch/x19/filed-r5-r7.diff`,
`.scratch/x19/filed-r9.diff`, 10:01Z local). This seat's observation is
independent and agrees.

**Disposition.** Parent's — restore is already in the worktree; no byte of
rounds 8–19 is dirty at this report's stamps. Routed as F-X23-1 (§5).

### 1.5 Landing curve (`.scratch/x23/watch.jsonl`, 30 s cadence)

Round-20 files: 2 (declaration) → 9 keys at 12:55:40Z → 12 keys 12:57:40Z → 20
13:03:40Z → 31 13:08:10Z → 45 13:11:10Z → 63 13:16:40Z → **73 13:34:40Z** → **81
13:39:53Z**; porcelain entries 0 → 99 across the window. The tree had not settled
at this report's close: `tools/exercise-handoff-e2e.py` changed at 13:35:40Z (and
earlier at 13:29–13:34Z); D-side artifacts (`reports/round-20/handoff/**`) were
the last wavefront. Tracked modifications at 13:39Z: 9 files —
`corpus/README.md`, `examples/culture-d2/expected-holds.json`,
`examples/culture-d4/{expected-holds.json,packet.d4.typed.yml,typed-labels.d4.yml}`,
`tools/{assemble-d4-typed.py,d2-typed-labels.py,exercise-handoff-e2e.py}`,
`tools/gates/typed-pipelines.json`.

## 2. PROVINCE accuracy

`PROVINCE.md` is **unchanged** (`sha256 05b34a579c5d4f4ec78957cdedb658246ff292df3e21181c66186403f2b942d6`,
identical to the round-10/11/18/19 records); no correction is proposed. Mapping of
the round-20 write surfaces onto its clauses:

- **`Owns`** names the six `corpus/knowledge/` partitions, "this lane's own gates,
  source-check records, non-canon examples and reports". Every round-20 surface
  falls inside: `tools/d2-typed-labels.py`, `tools/assemble-d4-typed.py`,
  `tools/exercise-handoff-e2e.py`, `tools/gates/typed-pipelines.json` (the lane's
  own gates/tools); `examples/culture-{d2,d4}/**` pin and projection bytes
  (non-canon examples); `corpus/README.md` (index) and
  `corpus/lessons/round-20.md` (report/craft record); `reports/round-20/**`;
  `tools/gates/expected/d4-typed-labels-check-gate/r20-post/**` and
  `tools/gates/frozen/round-20/repin-d2/**` (new baseline/pin rows).
- **`Refuses`** — no canon recorded (§3.1); no real-world rights/attribution
  ruling observed (the v3 packet's own "no real-language clearance" clause is a
  refusal, not a ruling); no game mechanics; no general source-research method
  (round-20 adds none); no web publishing; no prompt/skill craft (`SKILL.md` is
  byte-unchanged, `ea829038…`).
- **Adjacent contract** path exists and is untouched (§3.2). The "allowed
  append-only L0 questions" clause was **not exercised** (§3.5).
- The verification/civilizations "support, do not expand ownership" clause holds:
  the new lesson and the v3 packet state scope as lane method and defer canon.

## 3. Lore-boundary and out-of-lane watch

### 3.1 Canon sweep — zero assertion-shaped hits

```sh
grep -rniE "established as canon|is canon|canon (approved|accepted|recorded|ruled)|decide.*canon" \
  reports/round-20 corpus/lessons/round-20.md \
  | grep -viE "never canon|not canon|no canon|belongs to lore|canon decisions belong|canon lives|non-canon|canon hygiene|canon_status|canon standing|owns canon|not a canon|certifies no canon|is canon and theirs|is canon →|decide canon|decides canon|to decide canon|canon facts|canon rulings|canon decision to lore|canon standing is not|canon is lore|canon and belong"
```

Residual: **9 hits, all deferral-shaped**, none an assertion — e.g.
`handoff/claims-map.md:189` and `packet-v3-13..16.md:150` "cannot be imported as
canon without a lore baseline … owner: lore-shokunin"; `handoff/frozen.md:136`
"nothing here says … is canon, that lore accepted anything"; `scope.md:147` is
the sweep command itself; `validation.json:5835` restates the packet row. The
wider vocabulary sweep (`canon( |_)?(decision|ruling|status|standing)|canoniz|ratified`)
over `reports/round-20/` returns only the same disclaimers plus
`audit/x21-v3-claims-spotcheck.md:117` quoting the D4 packet's own
`canon: "not canonized (D4 NON-CANON design drill)"`. The independent X21
spot-check reaches the same class of reading. No lane file asserts canon.

### 3.2 Handoff contract — untouched; every reference read-only

Target: `corpus/knowledge/synthesis/worldbible-integration-contract.md`
(contract_id `kotodama-lore-adjacency`, revision 1.0.0).

| state | sha256 | stamped |
|---|---|---|
| worktree | `5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069` | 12:55:02Z, 13:33:41Z |

Identical to the round-9/10/11/18/19 records — the contract has not moved. Every
round-20 reference to it is a read-only citation (design §2 read set, the
exercise's read set, the freeze/audit receipts), not an edit.

### 3.3 New-content boundary discipline

Representative quotes from the new surfaces:

- `reports/round-20/handoff/packet-v3-13.md:1,3` — "deliberately unbound
  research packet; not canonized … no canon standing is asserted here. Canon
  standing is lore's alone (contract §6, §8.7)"; `:5` `canon_standing: not
  canonized — lore disposition required`.
- `reports/round-20/handoff/frozen.md:136` — "nothing … says is canon, that lore
  accepted anything, or that the round is complete."
- `corpus/lessons/round-20.md:9` (scope line) — "Filed artifacts of rounds 8–19
  are read-only; round-20 corrections land as new files, never as in-place edits
  of filed bytes … All round-20 artifacts are NON-CANON; no real-world
  rights/clearance ruling is made or absorbed here."
- `corpus/README.md` revision 1.5 — "Non-canon examples and passing structural
  gates do not certify historical truth" (carried from 1.4); "Canon lives with
  lore-shokunin" unchanged.

Pin discipline (the O re-pin cascade): old pin surfaces are **byte-unchanged** —
`reports/round-16/handoff/expected-v2-07.json` `dc75c5d7…`,
`reports/round-18/repin/expected-v2-07-r18.json` `d5fda399…`,
`tools/gates/frozen/round-18/repin-d2/run-receipt-repin.json` `d90c09e8…` — while
the new pins are **new rows/files** (`reports/round-20/repin/{expected-v2-07-r20.json,O11…O14}.md`,
`reports/round-20/wart/{expected-v2-07-r20.json,repin-r20.json,shard-1..6.md}`,
`tools/gates/frozen/round-20/repin-d2/{MANIFEST.tsv,freeze.txt,run-receipt-repin.json}`,
`tools/gates/expected/d4-typed-labels-check-gate/r20-post/**`). The two
`expected-holds.json` files are re-pinned **in place** with a `revision_note`
naming the before→after digests (D4 also carries a `supersedes_pins` block) —
recorded here as the seats' chosen form, with the receipts as the new rows.

### 3.4 Out-of-lane watch

- **No kotodama write crossed into a sibling repo or the world bible.** Fleet
  root porcelain 0 throughout. `lore-shokunin`'s worktree is dirty (27 entries —
  its own wave, the recurring r16–r19 F-class), but
  `git -C ../lore-shokunin status --porcelain -uall | grep -i kotodama` → **0**.
- **No out-of-lane write route in the new content.** Sweeps over
  `reports/round-20/` for write-shaped commands targeting
  `/home/vgpnk/Projects/shokunin/<non-kotodama>` or `../<sibling>-shokunin` → 0;
  the only absolute out-of-lane paths are `/tmp` scratch mirrors:
  `reports/round-20/audit-12.md:184-195` replays frozen manifests with
  `TMPDIR=/tmp/kotodama-r20-audit` and materialises isolated era trees there
  (`git show … > /tmp/kotodama-r20-audit/iso-r3/tools/gates/$g.py`;
  `git archive a3f6fce examples | tar -x -C /tmp/kotodama-r20-audit/iso-r11`).
  `/tmp/kotodama-r20-audit` (43 MB) is still on disk at 13:39Z, as is a
  `/tmp/kotodama-r8-o14` from an earlier round. This is a scratch-location
  deviation from the lane's `TMPDIR=$PWD/.scratch` convention — **no repo or
  sibling byte is written** — routed as F-X23-3 (§5).
- New scripts' write targets are lane-local or `.scratch`: the runner writes only
  `reports/round-20/validation.json`; the ledger generator writes only
  `reports/round-20/integration/fragment-ledger.{json,md}`; the O selftests
  assert "no file outside the temporary directory/mirror touched" (reproduced by
  this seat, §4).

### 3.5 L0 surface untouched

```sh
stat -c '%y %s' ../.ufo/l0-questions.md   # 2026-10-17 19:34:37.743244517 -0300, 37339 B
```

mtime equals the round-9-close write and did not move through 13:40Z. No
round-20 seat appended an L0 question.

## 4. Independent re-runs (connector evidence, read-only instruments)

Run by this seat at the stamps shown (`export TMPDIR=$PWD/.scratch`; no counting
command executed):

| command | result | stamp |
|---|---|---|
| `python3 tools/d2-typed-labels.py --check` | exit 0 — "byte-identical deterministic projection" (D2 default) | 13:39:26Z |
| `python3 tools/d2-typed-labels.py --selftest` | exit 0 — **50/50 checks passed** | 13:39:26Z |
| `python3 tools/assemble-d4-typed.py --selftest` | exit 0 — **12/12 checks passed** | 13:39:26Z |
| alias probe: projector `--check` over D4 in a mirror **without** `examples/culture-d2` | exit **0** (round-19 regression seat's identical probe read exit 2 "missing …/12-rank-rules.yml") — wart closed | 13:39:30Z |
| `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | exit 0 — **19/19 legs passed** | 13:39:31Z |
| `python3 tools/gates/handoff-packet-check.py reports/round-20/handoff/packet-v3-16.md` | exit 0 — `fields=16/16 glossary-entries=20 findings=0` | 13:39:44Z |
| `python3 tools/gates/handoff-packet-check.py --selftest` | exit 0 — OK | 13:39:44Z |

D2 byte-identity at the same stamps: `examples/culture-d2/packet.d2.yml`
`e0f21509…` and `examples/culture-d2/typed-labels.d2.yml` `a3aa452c…` — unchanged
from this seat's 12:55Z baseline; the projector itself moved
`0da0015f… → 76536a92…` (new pin rows above). D4 projection regenerated
`a59990bb… → cbcf997f…` with `expected-holds.json` re-pinned in place
(`18d0cfce…`, `supersedes_pins` present). The runner receipt
(`reports/round-20/validation.json`, `runner_sha256 6da4f7ed…`) read
`acceptance_checks_passed: true`, `failures: []` at 13:21:07Z — a stamp bound to
that run only; the D surface was still mid-write after it (X17's lesson records
red receipts earlier for the same reason).

## 5. Cross-cutting observations (reported, not adjudicated — routed to the parent)

1. **F-X23-1 — filed-artifact transient (rounds 5/7/9).** Rewritten 13:00:55–13:01:01Z by a
   live gap-measurement run of historical counting commands, restored 13:03:17Z.
   Round 9 is inside the operator's 8–19 set. The runner's filed window covers
   8–19 (and records 5–7 informationally), so a future close should state whether
   the restore is accepted or the incident is carried in LOG/SCORECARD. Evidence:
   §1.4; corroborated by X17 lesson:120 and X19 diffs.
2. **F-X23-2 — claim C's declared count.** `reports/round-20/claims.json` declares
   "linguistics 20"; the tree measures **19** at every stamp, and README 1.5 and
   the runner's `declared_deltas` both record the delta explicitly
   ("declared 20, live 19, documented_in_readme: true"). The claim text remains
   the only surface still carrying the unreproducible figure.
3. **F-X23-3 — `/tmp` scratch mirrors.** `audit-12.md`'s isolated replays use
   `/tmp/kotodama-r20-audit` (43 MB, left in place) instead of `.scratch`; a
   `/tmp/kotodama-r8-o14` from an earlier round also persists. Scratch-location
   deviation only; no repo/sibling write.
4. **F-X23-4 — two round-20-internal path-shaped refs that do not resolve.**
   `reports/round-20/wart/review.md:99` recommends a `reports/round-20/repin/table.md`
   (landed as `O14-repin-table.md`); `reports/round-20/wart/shard-2.md:47` names
   `examples/culture-d4/probe-bare.yml` / `probe-rows.yml` which are explicitly
   in-memory dict labels ("no file is read or written"). Both are citation-style
   items, not missing deliverables; a lessons/audit path resolver will list them
   as missing (class: the same shape as X24-L2's stale filed-lesson refs, which
   the X24 audit already reports).
5. **In-flight status (not a finding).** At this report's close the wave had not
   settled: 81 round-20 files, `tools/exercise-handoff-e2e.py` still changing, D
   receipts (contract-audit re-run over v3, v3 baseline `expected.json` readers)
   landing. §4's readings bind their stamps; the parent's close must re-measure.

## 6. Limits and open items (to-verify)

- All observations are stamped snapshots of a live wave (12:54–13:40Z); the tree
  did not settle, so lists/counts bind their stamps. The parent integrates after
  this seat's close; `reports/round-20/validation.json`, the handoff directory and
  `tools/exercise-handoff-e2e.py` may change after them.
- The canon sweeps are lexical; a canon claim phrased outside the swept
  vocabulary would not be caught. X21's spot-check is a second lexical pass, not
  a semantic proof.
- §3.4 is name/content evidence, not process attribution: a lane-local seat
  cannot prove the fleet-wide negative "no out-of-lane write ever happened"; it
  establishes that this lane's history, the declaration commit, and the new
  content touch in-lane paths only, and that the fleet root is clean.
- This seat did not run `reports/round-20/run-validation.py` (it writes
  `validation.json` — the round-14 guard; and §1.4 is that guard's live
  demonstration). C/D/O counting is the parent's.
- The round-5/7/9 restore is attested by git state and mtimes; the restoring
  actor is unattributed here by design.

## 7. Stamps and receipts

Representative commands (lane root, `export TMPDIR=$PWD/.scratch`; stamps as
executed, 2026-10-18 UTC):

```sh
date -u '+%Y-%m-%dT%H:%M:%SZ'                                        # 12:55:02Z … 13:39:53Z
cd /home/vgpnk/Projects/shokunin && git status --porcelain -uall | wc -l   # 0 @ 12:55Z, 13:33:41Z, 13:39Z
git rev-parse HEAD                                                   # 122086bc @ every check
git status --porcelain reports/round-{8..19} | wc -l                 # 0 @ 13:33:41Z
git ls-files reports/round-{8..19} | wc -l                           # 892; on disk 897 (5 ignored *.log)
git status --porcelain reports/round-5 reports/round-7 reports/round-9   # 0 after 13:03:17Z restore
stat -c '%y %n' reports/round-{5,7,9}/validation.json                # 2026-10-18 10:00:55/58, 10:01:01 → 10:03:17 -03
sha256sum PROVINCE.md                                                # 05b34a57…
sha256sum corpus/knowledge/synthesis/worldbible-integration-contract.md   # 5f4c02bf…
stat -c '%y %s' ../.ufo/l0-questions.md                              # 2026-10-17 19:34:37, 37339 B
sha256sum SKILL.md examples/culture-d2/packet.d2.yml examples/culture-d2/typed-labels.d2.yml
                                                                     # ea829038…, e0f21509…, a3aa452c… (all unchanged)
sha256sum reports/round-16/handoff/expected-v2-07.json reports/round-18/repin/expected-v2-07-r18.json \
  tools/gates/frozen/round-18/repin-d2/run-receipt-repin.json        # dc75c5d7…, d5fda399…, d90c09e8… (old pins unchanged)
python3 tools/d2-typed-labels.py --check                             # exit 0 byte-identical (13:39:26Z)
python3 tools/d2-typed-labels.py --selftest                          # 50/50 (13:39:26Z)
python3 tools/assemble-d4-typed.py --selftest                        # 12/12 (13:39:26Z)
python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml   # 19/19 (13:39:31Z)
python3 tools/gates/handoff-packet-check.py reports/round-20/handoff/packet-v3-16.md  # 16/16, 20 entries, 0 findings (13:39:44Z)
python3 tools/gates/handoff-packet-check.py --selftest               # OK (13:39:44Z)
python3 reports/round-20/audit/x24-lessons-audit.py --json           # read, not run, by this seat: X24's receipt
find reports/round-20 -type f ! -path '*__pycache__*' | wc -l        # 2 → 73 → 81 across the window
```

Scratch (gitignored): `.scratch/x23/{watch.py,watch.jsonl,watch.out,watch2.out,sweep.sh}`.

## 8. Addendum (13:41:49Z) — post-write re-check

Re-ran the boundary checks after writing §1–§7: lane HEAD `122086bc…` unmoved;
fleet root porcelain 0; `git status --porcelain reports/round-{8..19}` → 0;
`PROVINCE.md` `05b34a57…` and the contract `5f4c02bf…` unchanged; L0 mtime
2026-10-17 19:34:37 unchanged; `examples/culture-d2/typed-labels.d2.yml`
`a3aa452c…` unchanged. The round-20 tree read **82 files** (one further in-lane
artifact past the 81-file snapshot in §1.5 — a stamped snapshot, not a
contradiction); porcelain 99, the last change being this file's own write. The
wave was still in flight at 13:41:21Z (`tools/exercise-handoff-e2e.py` last
moved 13:35:40Z); no verdict in §0 changes.

FILES: reports/round-20/adjacency.md
SUMMARY: X23 adjacency — fleet root clean, HEAD `122086bc` unmoved, filed rounds 8–19 byte-identical (892 tracked/897 on-disk; rounds 5/7/9 transiently rewritten 13:00:55–13:01:01Z and restored 13:03:17Z, F-X23-1); PROVINCE `05b34a57…`, contract `5f4c02bf…`, L0 and SKILL unchanged; zero assertion-shaped canon claims in the 81-file round-20 tree; independent re-runs green (projector 50/50 + D2 byte-identical, adapter 12/12, alias probe exit 0 in a D2-free mirror, D4 gate 19/19, v3 packet gate 16/16 + 20 entries + 0 findings); connector scan 669 refs / 18 unresolved all classified (2 round-20-internal naming items routed).
