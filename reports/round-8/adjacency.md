# Round-8 adjacency / connector report — X04

- round: 8 (loop 1 of 3, build round 1 of 4) · shard: X04
  (`reports/round-8/targets.json` `scribe_review`: "X04 adjacency/connector
  (handoff contract + lore boundary check)")
- date: 2026-10-17 · check window 17:10–17:29 local (-03:00) = 20:10–20:29Z
- baseline revision (declared): `e7ca0faeb6680fa9891b907be628d9db578c28f4`
  (`reports/round-8/claims.json`); worktree HEAD during the check:
  `cf338a713060f274269cdacb18cdc0085bb06aeb` (unchanged — no worker committed)
- writes: this file only. This report verifies cross-domain boundaries; it
  issues no F/O/D acceptance verdict.
- live-tree caveat: the 64-worker batch was still writing at the last stamp
  (20:30:35Z; `git status --porcelain=v1 --untracked-files=all | wc -l` = 321,
  up from 314 at 20:28:55Z). Every count below is stamped; each check names its
  re-run command.

## Verdicts

| # | check | verdict | key evidence |
|---|---|---|---|
| 1 | No canon decisions recorded (lore's province) | pass | §1 scans — every hit is an explicit `not canonized` / "no canon decision" disclaimer |
| 2 | Handoff contract untouched by D work | pass | §2 — the only edit is the declared metadata sweep's 3 header lines; D artifacts cite the contract read-only; digest chain documented in M07. Escalation in §2.4 |
| 3 | `PROVINCE.md` still accurate | pass | §3 — unchanged since baseline; round-8 writes map onto the Owns list; refusals unviolated |
| 4 | No writes outside `kotodama-shokunin/` | pass | §4 — standalone repo, no tracked symlinks, sibling sweep shows only lore's own round-95 artifacts, parent `.ufo` untouched after 17:10 |
| 5 | Git status scope | pass | §4.4 — 314 changed paths, all in-lane; `reports/round-7/` filed artifacts untouched; HEAD unchanged |

## 1. No canon decisions recorded

Scan commands (2026-10-17T20:2xZ, from the lane root):

```sh
grep -rniE "canon( |_)?(decision|ruling|status|standing|iz)" \
  reports/round-8/ tools/d2-typed-labels.py examples/culture-d2/typed-labels.d2.yml corpus/lessons/round-8.md
grep -rniE "canoniz|ratified|approved for canon|canon-?status|established as canon|canon fact" \
  reports/round-8/ tools/d2-typed-labels.py examples/culture-d2/typed-labels.d2.yml corpus/lessons/round-8.md
grep -rln "l0-questions" reports/round-8/
```

Results — every occurrence is a disclaimer or in-fiction text, no lane file
asserts canon standing:

- `examples/culture-d2/typed-labels.d2.yml:2` — `canon: "not canonized (D2
  design drill); derived view of examples/culture-d2/components and
  packet.d2.yml"` (emitted by `tools/d2-typed-labels.py:1023`).
- `reports/round-8/depth/docs.md:21` "claims no new capability, no canon, and
  no acceptance"; `:267-269` "Regenerating it proves determinism, not design
  quality, not scholarship, not canon; lore-shokunin owns canon";
  `:309` "canon status is lore's — neither is decided here".
- `reports/round-8/depth/skill-table-draft.md:26` "a canon ruling, not a
  general phonology standard"; `reports/round-8/depth/scribe.md` header
  "canon: NON-CANON engineering evidence. A freeze pins bytes and verdicts,
  never design quality, scholarship or lore standing."
- `reports/round-8/freshness/R8-F06-receipt.md:79` "Scope: entry untouched;
  no canon decisions; no git commit."; `R8-F06-receipt.json:240` "No canon
  decision, no handoff change, no game mechanics".
- `reports/round-8/depth/neg/packet-13.era-material-scope.yml:14` — negative
  control fixture header `canon: "not canonized (round-8 D2 typed-labels
  negative control)"`.
- The only "ratified" hits are fictional rule text inside the drill
  (`design-spec.md:387`, `shard-rank.md:184`, `typed-labels.d2.yml:1191` —
  "caravan treaty ratified at the winter moot"), not canon rulings.

`grep -rln "l0-questions" reports/round-8/` → 0 hits: no worker touched or
answered the L0 surface. The handoff samples (`examples/handoff-packet.sample.*`)
are unmodified this round (`git status` shows no change under `examples/`
except the new `typed-labels.d2.yml`).

## 2. Handoff contract — untouched by D work

Target file: `corpus/knowledge/synthesis/worldbible-integration-contract.md`
(contract_id `kotodama-lore-adjacency`, declared revision `1.0.0`).

### 2.1 D-side write surfaces exclude the contract

`reports/round-8/targets.json` depth shards declare writes only to
`reports/round-8/depth/**` and (D02) `tools/d2-typed-labels.py`. D artifacts
cite the contract read-only:

```sh
grep -rn "worldbible-integration-contract" reports/round-8/ tools/d2-typed-labels.py examples/culture-d2/typed-labels.d2.yml
```

→ `depth/design-spec.md:6,214,271,297,571` (line 571: "(read 2026-10-17; hash
not taken at spec time — `to-verify`)"), `depth/docs.md:161,336`,
`metadata/m07-synth-13-24.md` (sweep), `targets.json` (declaration), and
fixture copies under the in-lane scratch tree
`depth/neg/scratch/exp1/repo/examples/culture-d2/components/*.yml`. No D shard
claims a contract edit; no D artifact carries an "edited the contract" line.

### 2.2 The contract did change this round — attribution: the metadata sweep

The file is modified relative to baseline; the diff is exactly three added
header lines and no body change:

```sh
git diff e7ca0faeb6680fa9891b907be628d9db578c28f4 -- \
  corpus/knowledge/synthesis/worldbible-integration-contract.md
```

→ single hunk at line 2–6, adding `- source:`, `- verified-at:`, `- recheck:`;
§§1–13 byte-identical. Final bytes:
`sha256 5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069`
(mtime 17:22:50, stable ≥7 min, re-checked 20:30:35Z).

The signature matches the declared sweep (`targets.json` `metadata_sweep`:
"12 workers audit corpus/knowledge/* frontmatter (source/verified-at/recheck)
… synthesis (2) … Fixes applied in place on own-lane files only; per-file
fragment under reports/round-8/metadata/"). Observed digest sequence within
the round (each `sha256sum`-stamped):

| state | sha256 | stamped |
|---|---|---|
| baseline (HEAD) | `50c4c2f25a728e69260b76d42f0d838a398cc4683a6149f74cceeec8fb7268c1` | 20:10Z |
| intermediate | `96659b6b4ec22055c75589af3b896f9a063f1fa015beafe68f971c4f27106cfb` | 17:18:48 |
| intermediate | `a0f9dc7e61a409ca61d366926e9bf5b81334cbba5c68026d6e48035e9c08dd43` | 17:20:19 |
| delivered (stable) | `5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069` | 17:22:50 |

The declared interface revision string remains `1.0.0` (contract §1).

### 2.3 Provenance record exists (not a silent change)

`reports/round-8/metadata/m07-synth-13-24.md` (mtime 17:23:35) carries the
sweep's own record: row 24 "worldbible-integration-contract.md | — / — / — |
added 3 fields | §1 verification date; §2 standards checks; §11 cautions", and
the hash chain line:

```
worldbible-integration-contract.md 50c4c2f2… -> 5f4c02bf…
```

### 2.4 Escalation to the orchestrator (report, not absorbed)

Lore's own L0 questions already track this exact class of issue.
`lore-shokunin/l0-questions.md:6` (round-93) asks kotodama to "ratify the
50c4… copy as the current rev-1.0.0 interface so lore can record its
read/acknowledge, or direct kotodama to bump the revision and re-issue".
Round 8's sweep then changed that same copy again (to `5f4c02bf`, still
declared `1.0.0`).

- Contract §9 classifies an editorial correction with unchanged forms,
  meanings, references and decisions as PATCH — "Publish corrected bytes and
  provenance; receivers explicitly record any adopted replacement". Bytes and
  provenance are published (M07); the revision string did not move.
- Contract §1: "Before later transfers, compare the pinned contract digest; a
  changed revision/digest requires both lanes to re-read and acknowledge
  before importing under it." Bilateral acknowledgement is still pending per
  §1 (no transfer has occurred), so no lane currently holds a stale *accepted*
  pin — but lore's pending question now targets a superseded digest.
- Orchestrator decision needed: (a) accept the sweep edit as a documented
  PATCH and have the lore-facing answer reference the post-round-8 digest
  `5f4c02bf` (rev still `1.0.0`), or (b) revert the sweep's contract edit and
  re-issue the header change with a revision bump per §9. Do not let the edit
  pass unremarked while the round-93 question is open.

## 3. PROVINCE.md still accurate

```sh
git diff e7ca0faeb6680fa9891b907be628d9db578c28f4 -- PROVINCE.md   # empty
sha256sum PROVINCE.md   # 05b34a579c5d4f4ec78957cdedb658246ff292df3e21181c66186403f2b942d6
```

Unchanged since baseline, and still accurate against this round's delivered
surfaces:

- Owns list covers the round's writes: `corpus/knowledge/**` metadata
  (metadata_sweep), the lane's own gates/validation tooling (`tools/gates/`,
  `tools/harness/`), reports (`reports/round-8/**`), non-canon examples
  (`examples/culture-d2/typed-labels.d2.yml`), and the lane's skill draft
  (`reports/round-8/depth/skill-table-draft.md`; `SKILL.md` itself untouched).
- Refusals unviolated: no canon recording (§1); no real-world rights/attribution
  ruling; no game mechanics; no general research method (F receipts are
  entry-scoped source rechecks, each carrying URL + accessed-at + passage);
  no web publishing; the D14 label-typing table is lane-domain content drafted
  inside the lane's own reports, not kotoba-style prompt/skill methodology.
- The named handoff contract path exists and is still the canonical copy in
  this lane (see §2.4 for the digest caveat).
- The parent `.ufo/l0-questions.md` append is pre-round (mtime 11:03:19, the
  lane's round-2 question) and matches PROVINCE's "allowed append-only L0
  questions" — not a round-8 write. No amendment to PROVINCE.md is needed.

## 4. No writes outside kotodama-shokunin/

### 4.1 Repo topology

```sh
git rev-parse --show-toplevel        # /home/vgpnk/Projects/shokunin/kotodama-shokunin
git remote -v                        # own origin (github.com/VeigaPunk/kotodama-shokunin.git)
git ls-files -s kotodama-shokunin    # (in the parent repo) empty — not tracked/submodule
```

The lane is a standalone local repo with its own remote; the parent
(`/home/vgpnk/Projects/shokunin`) neither tracks it nor declares it as a
submodule (no `.gitmodules`).

### 4.2 No tracked symlinks

```sh
git ls-files -s | awk '$1=="120000"'   # empty
```

Symlinks exist only under the gitignored scratch tree
(`reports/supplement-opencode-1/scratch/round7-15/`, round-7 fixtures) —
no tracked path can route a write outside the lane.

### 4.3 Filesystem sweeps (after the 17:10 dispatch)

```sh
find . -maxdepth 5 -newermt "2026-10-17 17:10" -not -path "./kotodama-shokunin*" \
  -not -path "./.git" -not -path "*/.git/*"
```

→ only lore's own wave activity: `lore-shokunin/.ufo/waves/round-95/receipt.json`
and `seats/` files. Parent `.ufo` files newer than 17:10: **0**. No file under
any of the 19 sibling lanes was written by a kotodama worker (the sibling
lanes' own tracked files show no kotodama-style edits; the only newer sibling
paths are lore's untracked `.ufo` wave scratch).

### 4.4 Git status scope (20:30:35Z)

```sh
git status --porcelain=v1 --untracked-files=all | wc -l   # 321
git status --porcelain=v1 --untracked-files=all | sed -E 's/^...//' | awk -F/ '{print $1"/"$2}' | sort | uniq -c
```

| group | changed paths |
|---|---|
| `corpus/knowledge/` (metadata sweep, own-lane) | 171 |
| `reports/round-8/` (worker fragments) | 140 |
| `tools/gates/` (O repairs) | 6 |
| `tools/harness/` (O02 fix) | 1 |
| `tools/d2-typed-labels.py` (D) | 1 |
| `examples/culture-d2/` (D artifact) | 1 |
| `corpus/lessons/` (X01 skeleton) | 1 |

Nothing outside the lane. `git status --porcelain -- reports/round-7/` →
empty: round-7 filed artifacts untouched (only the gitignored
`reports/round-7/__pycache__/run-validation.cpython-314.pyc` regenerated when
O01 diagnosed the round-7 runner). HEAD is still `cf338a7` — no worker
committed. Ephemeral OS scratch was used outside the project tree
(`/tmp/kotodama-r8-o14` copied tree, retrieval PDFs under `/tmp`) and in-lane
under the gitignored `reports/supplement-opencode-1/scratch/round8-f14/`;
neither is project state.

## 5. Observations outside this shard's verdict scope (reported, not adjudicated)

- **D tool live state is unstable.** At 17:22:33 local,
  `tools/d2-typed-labels.py` (sha `1756e8c0…`) passed `--selftest` 30/30 and
  `--check` exit 0. At 17:27:28 (sha `61b61eb4…`) both fail (`RecursionError`
  in `selftest()` lines 2296–2297; `--check`: "differs from the deterministic
  projection"). D18's own scribe records the same race
  (`reports/round-8/depth/scribe.md`: D02 kept editing after the pin; broken
  intermediates at 20:26:04Z/20:26:13Z). Final stamp 20:30:35Z: sha
  `3548185cd9c10c01…`, `--selftest` exit 0 again. `reports/round-8/validation.json`'s
  D failures were measured against an even earlier tool (sha `080a3b2f…`) and
  are a stale snapshot; integration must re-pin on the settled revision.
- **Possible harness false positive.** `validation.json` complains "SCORECARD
  carries the d2-typed-labels row although the tool selftest did not pass", but
  `grep -c "d2-typed-labels" SCORECARD.md` = 1 and that hit is the `## Planned`
  declaration bullet (`SCORECARD.md:117`); no capability row is present. O
  territory.
- **Determinism-positive signal.** `examples/culture-d2/packet.d2.yml` was
  rewritten during the round and shows no `git diff` — byte-identical
  regeneration.
- **Sweep breadth.** The delivered sweep diff (171 files, 449 insertions,
  21 deletions) is not purely additive: bold `**verified-at:**`/`**recheck:**`
  markers were normalized and `couples:` lines rewritten in culture-material
  files, plus 19 non-field added lines (e.g. a Hawkes 1954 journal/volume
  correction marked "corrected in the 2026-10-17 M10 sweep", and a "Triage
  round-2 additions" source block). All in-lane and attributed in the sweep's
  fragments, but wider than the "frontmatter" wording in `targets.json`.
- **SKILL.md pending.** The D claim's "SKILL.md gains the label-typing
  decision table" has not landed — `SKILL.md` is unmodified; the draft sits at
  `reports/round-8/depth/skill-table-draft.md` (orchestrator landing item).
- **Environment note.** `/tmp` (16G tmpfs) hit "No space left on device"
  transiently around 17:2x (45% used when checked at 20:2x); may have caused
  spurious worker failures.

## 6. Limits of this check

- Live tree: the batch was still writing at the final stamp (20:28:55Z); the
  contract hash was stable ≥6 min before that stamp but must be re-read at
  integration (`sha256sum corpus/knowledge/synthesis/worldbible-integration-contract.md`).
- The D-tool and SCORECARD/validation observations in §5 are snapshots, not
  verdicts; re-measure at integration.
- No sibling lane or world-bible file was read beyond directory/mtime sweeps
  and the two quoted L0 lines; no cross-lane write occurred.

## Evidence index

| claim | command / location |
|---|---|
| contract body unchanged, 3 header lines added | `git diff e7ca0fa -- corpus/knowledge/synthesis/worldbible-integration-contract.md` |
| contract digest chain | `sha256sum` stamps §2.2; `reports/round-8/metadata/m07-synth-13-24.md:110,126` |
| sweep declaration | `reports/round-8/targets.json` `metadata_sweep` |
| D read-only citations | `reports/round-8/depth/design-spec.md:6,214,271,297,571`; `depth/docs.md:161,336` |
| canon disclaimers | §1 command set and listed lines |
| PROVINCE unchanged | `git diff e7ca0fa -- PROVINCE.md` (empty); `sha256sum PROVINCE.md` |
| no outside writes | §4.1–4.4 commands |
| lore open question | `lore-shokunin/l0-questions.md:4-7` (round-93 ask at line 6) |
| D tool states | `sha256sum tools/d2-typed-labels.py`; `--selftest`/`--check` runs §5 |
