# Round-9 adjacency / connector report — X03

- round: 9 (loop 1 of 3, build round 2 of 4) · shard: X03
  (`reports/round-9/targets.json` `scribe_review`: "X03 adjacency/connector
  (git-scope check … handoff contract untouched by baseline/D3 work, PROVINCE
  still accurate, lore-boundary check)")
- date: 2026-10-17 · check window 17:48:58–17:59:51 local (-03:00) =
  20:48:58–20:59:51Z
- baseline revision (declared): `e1694bad6ac96aca45a11ca5746582b275929355`
  (`reports/round-9/claims.json:5`); worktree HEAD during the check:
  `a7bb205d3aecdaa24d91c047c8719cd8689e4ddd` (unchanged — no worker committed)
- writes: this file only. No acceptance verdict on F/O/D; boundaries only.
- **live-tree caveat**: the batch was still writing at the final stamp
  (17:59:51; `git status --porcelain=v1 -uall | wc -l` = 2072 at 17:59:51,
  path counts moving 1990→2081→2068 across my stamps). Every count below is
  stamped; every check names its re-run command.

## Verdicts

| # | check | verdict | key evidence |
|---|---|---|---|
| 1 | No canon decisions recorded (lore's province) | pass | §1 — all hits are disclaimers, fictional rule text, or planted negative controls |
| 2 | Handoff contract untouched by baseline/D3 work | pass (carry item) | §2 — digest `5f4c02bf…` identical at baseline/HEAD/worktree at 4 stamps; D3's stale pin (`50c4c2f2…`) lives in `expected.json`, not the contract; round-8 L0 escalation still open |
| 3 | `PROVINCE.md` still accurate | pass | §3 — unchanged (`05b34a57…`); round-9 writes map onto Owns; refusals unviolated |
| 4 | No writes outside `kotodama-shokunin/` | **breach found — 1 seat** | §4.2 — V09 metadata fragment landed in the **parent** tree (`/home/vgpnk/Projects/shokunin/reports/round-9/metadata/v09-myth.md`, 17:51:57); §4.3 unattributed stray PDF (not imputable to kotodama); no other out-of-lane writes |
| 5 | Git scope of lane changes | pass | §4.5 — all 2072 changed paths in-lane; only declared tracked edits; gate sources byte-frozen (also verified independently at `reports/round-9/baselines/audit-19.md` §2) |

## 1. No canon decisions recorded

Scan commands (2026-10-17T20:58:50Z, lane root):

```sh
grep -rniE "canon( |_)?(decision|ruling|status|standing)" reports/round-9/   # 24 hits
grep -rniE "canoniz|ratified" reports/round-9/
grep -rniE "accepted by lore|lore accepted|established as canon|admitted to the (world )?bible|world-bible entry established" reports/round-9/
grep -rln "l0-questions" reports/round-9/
```

Every occurrence is a disclaimer, a rule statement, fixture data, or a planted
negative control — no lane file asserts canon standing:

- `reports/round-9/baselines/handoff-packet-check/packet.md:193-194` — the
  frozen copy of the D3 handoff envelope: "canon standing stays lore's alone
  and none of these decisions requests canonization."
- `reports/round-9/baselines/handoff-packet-check/author.md:60` and
  `rerun.md:93` — a **planted** producer-side certification probe
  (`t2.md`, sha `5af09f9b…`) that the gate correctly fails with
  `HO-CANON-CLAIM`; constant `not canonized` marker preserved at
  `packet.md:629` equivalent.
- `reports/round-9/d3/capability-draft.md:29` — "The packet is
  `canon_status: NON-CANON`"; `d3/findings-10.md:221` poses canonization as an
  open question, not a decision.
- `reports/round-9/d3/check-diagnosis.md:8` — "this shard certifies no canon
  and absorbs no cross-shard decision."
- `reports/round-9/baselines/costume-era-consistency/author.md:199` —
  "never a canon ruling"; `myth-consistency-gate/rerun.md:171` etc. — "does
  **not** … prove … that lore accepted anything."
- `reports/round-9/freshness/R9-F03b-receipt.json:437` — "Out-of-province items
  (canon decisions; rights/attribution rulings; general research method) are
  reported, not absorbed."

False positives checked and dismissed: the `canoniz|ratified` sweep's F01c hits
are the substring inside `"unstratified"` in a quoted OIP 78 passage
(`R9-F01c-receipt.md:41`); the `ratified` hits in
`baselines/naming-collision-gate/packet.yml:2365,2418,2433` are in-fiction
timeline notes in drill data, and `:2` carries the `not canonized` marker.

`grep -rln "l0-questions" reports/round-9/` → 1 hit: the X04 draft
`report-draft.md:137` records the round-8 contract-digest escalation as open;
no worker touched or answered the L0 surface (§2.4).

## 2. Handoff contract — untouched by baseline/D3 work

Target: `corpus/knowledge/synthesis/worldbible-integration-contract.md`
(contract_id `kotodama-lore-adjacency`, revision `1.0.0`).

### 2.1 Digest chain (four stamps, no movement)

```sh
sha256sum corpus/knowledge/synthesis/worldbible-integration-contract.md
git show e1694bad6ac96aca45a11ca5746582b275929355:corpus/.../worldbible-integration-contract.md | sha256sum
git show HEAD:corpus/.../worldbible-integration-contract.md | sha256sum
git diff e1694bad6ac96aca45a11ca5746582b275929355 -- corpus/knowledge/synthesis/worldbible-integration-contract.md   # empty
```

| state | sha256 | stamped |
|---|---|---|
| baseline `e1694ba` blob | `5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069` | 17:48:58 |
| HEAD `a7bb205` blob | same | 17:48:58 |
| worktree | same | 17:48:58, 17:53:06, 17:56:05, 17:59:51 |

No diff in any scope, at any stamp. `git diff --name-only HEAD` covers 25
tracked files (§4.5) and none is `corpus/knowledge/synthesis/` — that
partition shows zero worktree changes.

### 2.2 Every round-9 reference to the contract is read-only

`grep -rn "worldbible-integration-contract" reports/round-9/` (20:56Z) — the
only hits are:

- the frozen copy of the D3 envelope at
  `baselines/handoff-packet-check/packet.md:4,27,74` and its twin under
  `tools/gates/frozen/handoff-packet-check/r9-pre/packet.md` —
  `cmp` against the delivered `examples/culture-d3/handoff.md`:
  **byte-identical** (checked 17:55:05); it cites the contract as a
  read-only pinned manifest entry (`A-CONTRACT`).
- `d3/check-diagnosis.md` §1/§6 — analysis of the pin drift (below).
- `d3/capability-draft.md:121-122`, `d3/contract-crosscheck.md` and the
  provenance-audit baseline's copied input tree — all read-only citations.

No round-9 file edits the contract, and no round-9 fragment claims to have
edited it. `git status --porcelain -- corpus/knowledge/synthesis/` → empty.

### 2.3 The pin drift D work found is in `expected.json`, not the contract

`reports/round-9/d3/check-diagnosis.md:40-49` (receipt 20:49:43Z):
`python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json
--frozen examples/culture-d3/expected.json` → exit 2 with 3 × `D3-SNAPSHOT`,
including the contract entry: declared `50c4c2f2…`, actual `5f4c02bf…`.
That declared digest is the **pre-round-8** contract byte
(round-8 metadata pass added 3 header lines; round-8 receipt:
`reports/round-8/metadata/m07-synth-13-24.md:126`). D3 never reads the
contract — `packet.json` contains no reference (`grep -c` → 0,
`check-diagnosis.md:103`) and tools match only the handoff gate's docstring
(`:106`). So: the contract is untouched; the stale pin is snapshot coverage
inside `examples/culture-d3/expected.json`, and the remediation
(re-author the pin, the mechanical recipe in `check-diagnosis.md:170-180`)
is the orchestrator's — flagged, not absorbed here. The D3
`--check` clause itself is green (`determinism.md:20-23`, exit 0).

### 2.4 Escalation carried forward (unchanged since round 8)

The D3 handoff envelope as shipped (`examples/culture-d3/handoff.md:27,74`,
mtime 16:48, byte-identical to both round-9 frozen copies) pins
`sha256:50c4c2f2…` with the phrase "re-measured 2026-10-17 from current
bytes" — stale relative to the current contract bytes. Contract §1
("changed revision/digest requires both lanes to re-read… before importing")
is not violated because no transfer has occurred (`packet.md:18`
`handoff_status: prepared-not-accepted`). The round-8 L0 question stands
unanswered: `../.ufo/l0-questions.md:45` ("kotodama | round-8 |
worldbible-integration-contract digest drift vs lore's open round-93
ratification…"), file mtime 17:45:00 — **no L0 write happened during round 9**
(`stat` at 17:56, 17:59 unchanged). Orchestrator decision still owed
(round-8 `adjacency.md` §2.4 options (a)/(b)); this report re-raises it.

## 3. PROVINCE.md still accurate

```sh
git diff e1694bad6ac96aca45a11ca5746582b275929355 -- PROVINCE.md   # empty
sha256sum PROVINCE.md   # 05b34a579c5d4f4ec78957cdedb658246ff292df3e21181c66186403f2b942d6
```

Digest equals the one recorded in round 8 (`reports/round-8/adjacency.md`
§3) — unchanged since baseline, and still accurate against round-9 surfaces:

- **Owns list covers the writes**: `corpus/knowledge/**` metadata fixes
  (24 tracked files — 22 `civilizations/`, 2 `culture-material/`, all
  attributed in `reports/round-9/metadata/v01…v11` fragments), the lane's own
  gates/baselines (`tools/gates/expected/`, `tools/gates/frozen/<gate>/r9-pre/`,
  `reports/round-9/baselines/**`), source-check records
  (`reports/round-9/freshness/**`), D3 records (`reports/round-9/d3/**`), and
  lane tooling (`tools/check-gate-battery.py` — the declared O15 edit,
  `+648/-19`). `SKILL.md` and `SCORECARD.md` are unmodified
  (`git diff --name-only HEAD --` both → empty).
- **Refusals unviolated**: no canon recording (§1); no real-world
  rights/attribution ruling; no game mechanics; F receipts are entry-scoped
  source rechecks carrying URL + accessed-at + passage; no web publishing; no
  prompt/skill craft (D07's capability row is a draft in `reports/round-9/d3/`,
  not a `SKILL.md` edit).
- The named adjacent-contract path exists and is the canonical lane copy
  (§2). The parent `.ufo/l0-questions.md` was not written this round, so the
  "allowed append-only L0 questions" clause was not exercised.
- One boundary-relevant nuance recorded, not adjudicated: the V09 breach
  (§4.2) is outside the PROVINCE wording's write surfaces — it is a *worker*
  deviation, not a PROVINCE inaccuracy; no amendment to `PROVINCE.md` is
  needed.

## 4. No writes outside kotodama-shokunin/

### 4.1 Repo topology (re-verified 17:58:40)

```sh
cd /home/vgpnk/Projects/shokunin && git check-ignore -v kotodama-shokunin
# .gitignore:1:*-shokunin/	kotodama-shokunin        (parent ignores all lane dirs)
git ls-files -s kotodama-shokunin          # empty — not tracked, no submodule (.gitmodules absent)
cd kotodama-shokunin && git rev-parse --show-toplevel
# /home/vgpnk/Projects/shokunin/kotodama-shokunin : standalone repo, own origin
git ls-files -s | awk '$1=="120000"'       # empty — no tracked symlink can route a write out
```

### 4.2 Breach found: one seat wrote into the parent tree

- **Path**: `/home/vgpnk/Projects/shokunin/reports/round-9/metadata/v09-myth.md`
  (12 251 bytes, sha256 `44d8a23bf6ad6b58f5e210bdcae008fa45078b4dde6d672e1421bb85682cc08c`,
  mtime **17:51:57**; dirs `reports/`, `reports/round-9/`,
  `reports/round-9/metadata/` created 17:51:43 — `stat` at 17:59:41).
- **Attribution**: content-confirmed kotodama round-9. The file's own first
  lines name round-9 shard V09 and cite `claims.json` `baseline_revision
  e1694ba…`; its close says "`reports/round-9/metadata/v09-myth.md` — this
  fragment (only file written by this shard)" (parent file :110). The in-lane
  metadata dir carries every other shard's fragment (v01–v08, v10, v11) and
  **no v09** (`ls reports/round-9/metadata/ | grep -i v09` → absent at 17:59;
  the in-lane audit already expects it: `reports/round-9/metadata/audit.md:90`
  lists V09 as "*pending at draft time*", `:167` "was not on disk when this
  audit [drafted]").
- **Scale**: one file, one seat; no other file in the parent tree or any
  sibling lane is kotodama-attributable (§4.4).
- **Secondary mismatch** (for the relocating party): the in-lane audit names
  the expected file `v09-myth-symbol.md`; the stray is `v09-myth.md`.
- **Recommended remediation (orchestrator, not absorbed here)**: move the
  file into `kotodama-shokunin/reports/round-9/metadata/` (or mirror it
  byte-verbatim) and record the deviation; then remove the stray parent
  `reports/round-9/` tree. X03 did not move it — the path is outside every
  write surface this shard owns.

### 4.3 Unattributed stray at the workspace root (not imputable to kotodama)

`/home/vgpnk/Projects/shokunin/mtk-zeichentragende.pdf` — 243 bytes,
mtime 17:49:24, content is an S3 error document
(`<Error><Code>AccessDenied</Code>…`), i.e. a failed download, not a document.
Attribution sweeps (all 2026-10-17, ~17:52–17:54): `grep -rniE
"zeichentragende|mtk-zeich"` over the whole workspace tree → 0 hits;
`find … -newermt "17:00" | xargs grep -l AccessDenied` → only this file
itself; kotodama `.scratch` and `reports/round-9/` name no such fetch. No
kotodama worker can be tied to it on text evidence; the fetch could belong to
any concurrent process (lore's round-96 wave is the only other live writer).
Reported for fleet hygiene; the orchestrator/operator should triage it.
Parent `git status` still shows it as `??` (untracked).

### 4.4 Sibling / fleet sweep (since the 17:46:36 declaration)

```sh
cd /home/vgpnk/Projects/shokunin
find . -newermt "2026-10-17 17:46:36" -not -path "./kotodama-shokunin/*" \
  -not -path "*/.git/*" -type f | sed -E 's|^\./([^/]+).*|\1|' | sort | uniq -c
#  5906 lore-shokunin      (lore's own round-96 wave: seats/V*, seats/Q*, V*-scratch)
#     1 reports             (the §4.2 V09 stray)
#     1 mtk-zeichentragende.pdf
```

- `lore-shokunin/` activity is lore's own concurrent wave (seat-scoped file
  names `V13-scratch/frozen1.txt`, `V22-c3-tamper…`, etc.); no kotodama-style
  artifact was found there. Proving who wrote a sibling-lane file is beyond
  observation from this lane; the consistent read is "each lane writes its
  own"; nothing in the lore delta cites kotodama round-9.
- Parent `.ufo/`: nothing newer than 17:46:36 (`.ufo/l0-questions.md` and
  `.ufo/reports/round-8/kotodama.md` are 17:45:00, the round-8 closeout —
  pre-window). Parent `git status` (17:59:45): only the §4.2/§4.3 paths.
- The lane's world-bible adjacency stay: **no kotodama write reached
  lore-shokunin or any world-bible surface**; the only cross-tree touch is
  the §4.2 stray, which is a lane-local report fragment in the wrong tree.

### 4.5 Git scope of lane changes (17:59:51)

```sh
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
git status --porcelain=v1 -uall | wc -l                                  # 2072
git status --porcelain=v1 -uall | sed -E 's/^...//' | awk -F/ '{print $1"/"$2}' | sort | uniq -c | sort -rn
```

| group | paths |
|---|---|
| `.scratch/` worker scratch (r9d02 1669, r9-prov 93, r9o17 88, r9f02c 42, …) | ~1937 |
| `reports/round-9/` fragments | 75 |
| `tools/gates/` baseline data (untracked `expected/`, `frozen/<gate>/`) | 35 |
| `corpus/knowledge/` tracked metadata fixes | 24 |
| `tools/check-gate-battery.py` (tracked, declared O15) | 1 |

No path outside the lane. Tracked modifications (25 total — the 24 corpus
files plus the battery) are all declared surfaces. Gate sources: `git diff
--name-only HEAD -- tools/gates/` → **empty** (no gate `.py` touched; also
independently re-verified byte-for-byte against `e1694ba` in
`reports/round-9/baselines/audit-19.md` §2, "61/61 MATCH").
`examples/` is untouched vs baseline (`git diff --stat e1694ba -- examples/`
empty); the two `handoff-packet.sample.*` files are unmodified.
`reports/round-7/` filed artifacts are untouched (no hits in status).

## 5. Observations outside this shard's verdict scope (reported, not adjudicated)

- **`.scratch/` is not gitignored** (`.gitignore` covers `*.log`,
  `__pycache__/`, `/reports/supplement-opencode-1/scratch/`, `.ufo/state/` —
  `git check-ignore .scratch` → no match). At 17:59:51 it contributes ~1937 of
  the 2072 status paths (one determinism seat alone: 1669 under
  `.scratch/r9d02/`). If the integration commit stages everything, the
  orchestrator should exclude/ignore `.scratch/` deliberately rather than
  sweep thousands of ephemeral files into history. Same for the byte-copies
  under `reports/round-9/freshness/.scratch-v03/`.
- **Baseline-root divergence (claim O scope).** Baselines landed in three
  roots (`tools/gates/expected/<gate>/r9-pre/`, `tools/gates/frozen/<gate>/r9-pre/`,
  `reports/round-9/baselines/<gate>/`); the extended battery scans only
  `tools/gates/{expected,frozen}`, so "7/7 covered" is not yet reachable
  through the runner (`reports/round-9/baselines/registry.md:204-214`;
  `baselines/audit-19.md` §6 records the same measurement). Orchestrator
  decision; no boundary issue — all roots are in-lane.
- **Frozen replay currently could-not-evaluate** (3 × `D3-SNAPSHOT`, §2.3) —
  expected under the pin regime; the re-pin will touch
  `examples/culture-d3/expected.json` (in-lane). Because re-pinning is
  "regenerate-and-bless" adjacent, the D09/D10 adversarial-review fragments
  are the right place for circularity scrutiny; flagged, not judged here.
- **Environment**: `/tmp` inode-exhausted at my stamps (`df -i /tmp` →
  `1048576 1048576 0 100%`, 17:56); the handoff baseline's `run.log` and
  `freeze.txt` are covered by `.gitignore:3` (`*.log`) —
  `baselines/handoff-packet-check/author.md` §6.2 documents the `git add -f`
  need. Both are integration-time notes.
- **Freshness state at my final stamp** (17:58:40): 9 receipts JSON + 11 MD
  under `reports/round-9/freshness/` (F01a-c, F03a-c, F04a-c); F02 receipts
  had not landed yet. §1's sweep covers what existed; re-scan at integration.
- **Addendum (18:01:13, extends the last sweep to this report's close)**: the
  F02 receipts (`R9-F02a/b/c`) landed after the final stamp; the §1 canon and
  lore-scope sweeps re-ran over the full round-9 set (12 receipts JSON at
  `ls reports/round-9/freshness/*.json | wc -l`) → 31 canon-class hits, all
  disclaimer/fixture class, and 0 lore-scope assertions; no new hit class.
  Contract digest re-checked at 18:01:13: still `5f4c02bf…`.
- **Adjacent shards already carry the other boundary verdicts**: gate-source
  immutability (`audit-19.md`), battery author+rerun halves
  (`baselines/battery-extension.md`, `baselines/*/rerun.md`), D3 contract
  cross-check (`d3/contract-crosscheck.md`). This scribe relies on them as
  their own evidence, not as mine.

## 6. Limits of this check

- Live tree: every count is a stamp, not a final state. Re-run the §2.1
  digest command and the §4.4/§4.5 sweeps at integration; the V09 stray may
  have been relocated by then (if so, the §4.2 finding stands as "breach
  occurred, remediated").
- The V09 attribution is by content + in-lane absence, not by observing the
  process; it is exact enough to relocate the file, not to name the seat
  beyond its self-declared shard id.
- No sibling lane or world-bible file was read beyond directory/mtime/
  status sweeps and the quoted lines; no cross-lane write was made by this
  shard.
- I did not run `reports/round-9/run-validation.py` (it writes
  `validation.json`, another shard's deliverable) — F/O/D counting is the
  orchestrator's.

## Evidence index

| claim | command / location |
|---|---|
| contract digest chain | §2.1 `sha256sum` + `git show` stamps; diff empty |
| D3 pin drift (contract entry) | `reports/round-9/d3/check-diagnosis.md:40-49,73`; round-8 receipt `reports/round-8/metadata/m07-synth-13-24.md:126` |
| D3 does not read the contract | `check-diagnosis.md:103,106` (`grep -c` → 0; `grep -rn` tools → docstring only) |
| round-8 L0 escalation open | `../.ufo/l0-questions.md:45`; mtime 17:45:00 unchanged at 17:56/17:59 |
| canon disclaimers | §1 commands and listed lines |
| PROVINCE unchanged | `git diff e1694ba -- PROVINCE.md` empty; sha `05b34a57…` |
| V09 stray (breach) | `../reports/round-9/metadata/v09-myth.md` (sha `44d8a23b…`, mtime 17:51:57); in-lane absence; `reports/round-9/metadata/audit.md:90,167` |
| stray PDF unattributed | `../mtk-zeichentragende.pdf` (17:49:24, S3 AccessDenied XML); sweep commands §4.3 |
| sibling sweep | §4.4 `find` grouping; parent `git status` |
| gate sources frozen | `git diff --name-only HEAD -- tools/gates/` empty; `baselines/audit-19.md` §2 (61/61 MATCH) |
| lane status scope | §4.5 stamped commands |
| battery edit declared | `git diff --numstat HEAD -- tools/check-gate-battery.py` → `648 19`; `targets.json` R9-O15 |
| freshness receipts state | `ls reports/round-9/freshness/*.json | wc -l` → 9; `*.md` → 11 (17:58:40) |
