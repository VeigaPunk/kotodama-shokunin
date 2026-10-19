- Seat: S03 | scribe | claim A | date 2026-10-19 | baseline 4a7aede

# Round 35 — final adjacency receipt (S03)

Assignment (`reports/round-35/targets.json:421-427`): **"Final adjacency receipt
post-review."** Out path `scribe/S03-a-receipt.md`. Claim under receipt is
**A** (`reports/round-35/claims.json:53-65`), the bleed-scope audit of the
rounds-33/34 touched surfaces.

**Status: PRE-review and PRE-audit-fragment at first read; ten A-block siblings
folded in §6; the assembled audit and two slices still owed.** At this seat's
first read (2026-10-19T08:14–08:26Z) `reports/round-35/` held **only**
`claims.json`, `targets.json` and four telemetry files (`find reports/round-35
-type f`, §1 row 0): **every A-block dependency was absent** — A01–A11, A08's
assembled draft, A09's receipt, R06, R07 and the K04 census. Under the
missing-dependency rule (`targets.json:12`) this seat executed the audit itself
at HEAD rather than certifying absent fragments. **Ten siblings landed
afterwards** — A01, A02, A05, A06, A07, A09, A10, A11, R06 and R07 — and are
folded in §6 as agreement or named divergence; the fold includes **R07-F3, a real
defect on the frozen packet surface that this receipt's first draft missed**
(§3.1, S03-F7), and **A02-F1, which corrects the scope of this receipt's §3.2
write-surface reading**. **A03, A04, A08 and K04 remain owed.** Nothing here is
round acceptance, an axis verdict, or a promotion/canon/clearance/closure
statement (`claims.json:67-73`); it is NON-CANON engineering evidence.

---

## 1. Checks this seat ran itself (independent, re-runnable)

Lane root, `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, HEAD
`4a7aede22cd8395b01ce6dd9f46bcae364ca24e4` (`git rev-parse HEAD`, ==
`claims.json:8-9`), observation window **2026-10-19T08:14:10Z–08:26Z**. Read-only
except this file; no `reports/round-*/run-validation.py` executed
(`targets.json:10`, F-C13-1); no `--freeze` of any declared-in-r7 bytes (seat
brief hard boundary — the freeze bytes are pinned).

| # | check | command | result | verdict |
|---|---|---|---|---|
| 0 | dependency census | `find reports/round-35 -type f` | 6 files: claims, targets, 4 telemetry; **no A/B fragment exists** | see §4 / `## Owed` |
| 1 | preservation, whole tree | `git diff-index --quiet HEAD` | **exit 0** | GREEN |
| 2 | preservation, scoped | `git status --porcelain=v1 -uall -- reports/round-{1..34} corpus/lessons tools/gates/frozen` | **0 rows** | GREEN |
| 3 | tracked baseline | `git ls-files \| wc -l`; `… \| grep -c '^reports/round-'`; `… tools/gates/frozen \| wc -l`; `… corpus/lessons \| wc -l` | **2815** = 1988 round paths + 237 frozen + 179 lessons | GREEN |
| 4 | PROVINCE drift | `git diff --stat 139e3b6 HEAD -- PROVINCE.md`; `… da68a6d HEAD -- PROVINCE.md`; `sha256sum PROVINCE.md` | both **empty**; `05b34a579c5d4f4ec78957cdedb658246ff292df3e21181c66186403f2b942d6` | GREEN |
| 5 | PROVINCE last touch | `git log --oneline -3 -- PROVINCE.md` | `c53782a` (pre-round-5, the r33 A01-1 correction), `a527120` (mint) | GREEN |
| 6 | owns-list partitions | per-partition `ls corpus/knowledge/$p/*.md \| wc -l` | linguistics 21 / myth-symbol 19 / culture-material 18 / synthesis 29 / verification 20 / civilizations 94 = **201** | GREEN |
| 7 | partition set + strays | `ls -d corpus/knowledge/*/`; `ls -p corpus/knowledge \| grep -v /` | exactly the six named dirs; **no stray file** (grep exit 1) | GREEN |
| 8 | contract digest live vs every pin | `sha256sum corpus/knowledge/synthesis/worldbible-integration-contract.md`; `grep -n 5f4c02bf` over the r7 packet | `5f4c02bf…79069`; matches packet `:14,:39,:103` and `expected.json:125` | GREEN |
| 9 | r7 freeze bytes live | `sha256sum reports/round-34/handoff/declared-in-r7/{packet.md,twin.json,expected.json,freeze.txt,claims-map.md}` | all five **equal `repin.json`'s recorded digests** and `freeze.txt`'s own lines | GREEN |
| 10 | r7 packet gate | `python3 tools/gates/handoff-packet-check.py reports/round-34/handoff/declared-in-r7/packet.md` | `fields=16/16 glossary-entries=20 findings=0`, **exit 0** | GREEN |
| 11 | example pair gates | same tool on `examples/handoff-packet.sample.{md,yml}` | `16/16 20/20 0` exit 0; `16/16 0 0` exit 0 | GREEN |
| 12 | repointed renderer, non-freeze | `python3 tools/exercise-handoff-e2e.py --profile v3 --quiet` | **exit 0**, `fields=16/16 glossary=20/20 findings=0 links=105/105 claims=27 statuses=16/7/4 packet_sha256=45f57132…` | GREEN |
| 13 | run did not write in-tree | `git status --porcelain=v1 -uall` after row 12 | only `?? reports/round-35/**` | GREEN |
| 14 | adoption tool selftest | `python3 -B tools/harness/receipt_guard_adoption.py --selftest` | `selftest_passed: true`, `controls_passed 38/38`, exit 0 | GREEN |
| 15 | adoption census live | `… --json` (no `--out`) | `runner_count 29`, `class_counts {guarded-refresh 18, unguarded-in-place 11}`, `hazard_count 11`, `census_complete true` | see S03-F2 |
| 16 | box-1 survey live | `python3 -B reports/round-30/craft/box1-survey.py` | `named 28 resolvable 28 unnamed_in_skill []`, `skill_sha256 f9bd07c2…`, exit 0 | GREEN (see S03-F1) |
| 17 | box-1 durable receipt vs live | `python3 -c` sha256 compare of `reports/round-34/craft/box1-resurvey-durable.json` vs `SKILL.md` | `skill_sha256` **equal**, `resolvable 28` | GREEN |
| 18 | stale example digests | `grep -rn '50c4c2f2\|e834f503' examples/` | **0 hits** — the A10-F14/A06 stale-pointer finding is **closed at HEAD** | GREEN |
| 19 | nested stray tree (A10-F8) | `find kotodama-shokunin -type d`; `… -type f` | 4 dirs, **0 files** — empty, untracked, contentless (unchanged from r33) | note, cosmetic |
| 20 | fleet L0 kotodama rows | `grep -n kotodama ../.ufo/l0-questions.md` | 4 rows: `:44` bilateral read, `:45` digest ratification, `:46` /tmp inodes, `:47` freshness threshold | routed, not absorbed |

## 2. Touched-surface census (from git, not from prose)

`git show --numstat --format='' <landing>` for the two landing commits —
round 33 = `da68a6d`, round 34 = `4a7aede` — filtered to non-`reports/round-<N>/`
paths. This is the K04-class census, derived from the commits themselves so it
cannot inherit a prose omission.

| round | surface | change | cross-domain risk class scanned |
|---|---|---|---|
| 33 | `SKILL.md` | +35 / −18 | cross-domain language, PROVINCE conformance of new content |
| 33 | `AGENTS.md` | −2 (orphan fence + heading excised) | instruction-surface leak |
| 33 | `corpus/lessons/README.md` | +130 / −28 | corpus index vs partition census |
| 33 | `corpus/knowledge/linguistics/register-lexicon-ceilings.md` | +28 append-only | source resolvability, append-only discipline |
| 33 | `examples/culture-d3/{README.md,handoff.md}`, `examples/handoff-packet.sample.{md,yml}` | 1/1, 2/2, 1/1, 2/2 | digest-pointer currency, no lore-asset claims |
| 33 | `REGIMEN.md`, `LOG.md`, `SCORECARD.md` | +77 / +93 / +29 | lane-internal bookkeeping |
| 34 | `tools/exercise-handoff-e2e.py` | +11 / −10 | ownership drift, read-set correctness |
| 34 | `tools/harness/receipt_guard_adoption.py` | **+1309 (new)** | in-lane ownership, sibling-path writes, language |
| 34 | `SCORECARD.md`, `LOG.md` | +28/−3, +54 | bookkeeping |
| 34 | `reports/round-34/**` (the round's own artifacts) | new | the audit slices A01/A02/A05 |

**Cross-round note the census makes visible:** round 34 touched **no** shared
instruction or corpus file (`git show --numstat 4a7aede -- SKILL.md AGENTS.md
PROVINCE.md corpus/lessons/README.md` → empty, exit 0). The SKILL.md/AGENTS.md/
lessons-README/ceilings/examples edits are all **round 33's**, which is why the
A-claim's wording ("the round-33/34 SKILL.md and AGENTS.md and ceilings edits")
resolves to round 33 for those four surfaces and to round 34 for the tool, the
packet and the renderer.

## 3. Per-surface verdicts

Each verdict is `GREEN` or `named-finding`, one per claim-A after-required
clause (`claims.json:60`).

### 3.1 declared-in-r7 packet, claims-map, repin.json — GREEN with one named finding (R07-F3)

- **Packet** (`reports/round-34/handoff/declared-in-r7/packet.md`, 106,328 B):
  gate exit 0 (row 10); contract digest at `:14,:39,:103` equals the live file
  (row 8); `canon_standing: not canonized — lore disposition required
  (lore-shokunin owns canon)` at `:7`; the header states "no canon standing is
  asserted here. Canon standing is lore's alone (contract §6, §8.7)" (`:3`).
  Language scan: **7 hits, every one a negation or a routed question** —
  `not canonized` (`:1,:7,:144`), `no clearance or permission may be inferred`
  (`:143`), `no clearance may be inferred` (`:154`), `it never means canonize`
  (`:254`), and the `canon` word inside the D4 NON-CANON drill's own wording
  (`:144`). **Zero asserting hits.**
- **NAMED FINDING carried into this section — `R07-F3` (independently
  reproduced by this seat after the fold).** The frozen packet contradicts
  itself on its own provenance: the header prose at `:3` says "the twelve D4
  rows are carried from `reports/round-20/handoff/claims-map.md`", while the
  same file's manifest row A-57 (`:95`), §reads (`:113`) and §claims (`:125`)
  all name `reports/round-34/handoff/declared-in-r7/claims-map.md`. The two
  files are different revisions — `sha256sum` r20 `4b1b9a35a18f0a4c937eec804d438852c672f13303b7dcd6ccde3a3d917caae8`
  (275 lines) vs r34 `d181de28ccafda2d34e40277a5390f7e42c64247fbbdcdec3df9a592aa48980c`
  (259 lines). Root cause: the hard-coded literal at
  `tools/exercise-handoff-e2e.py:2700` was **not** repointed by `4a7aede`,
  which moved `:184`, `:1933-1934` and the manifest label `:2566`. Remedy is a
  **new packet revision or a named-errata row, never an in-place edit** — the
  freeze bytes are pinned and re-freeze is a round-35 non-goal
  (`claims.json:70`). **This seat's own §3.1 first draft quoted `packet.md:3`
  verbatim without catching the contradiction**; the finding is R07's, folded
  here with its own reproduction, and the packet verdict is therefore
  **GREEN with named finding**, not plain GREEN.
- **Lore-owned references stay routed:** `OQ-V2-02` (`:300`) says "this packet
  does not represent the acknowledgment as complete"; `OQ-V3-06` (`:308`) and
  `D4-CL12` (`:155`) route the D4 namespacing question to `lore-shokunin` as
  **non-blocking** and name the missing lore baseline/entity key/receipt
  surface. No absorption anywhere: the packet never asserts a lore receipt,
  a baseline revision, or an entity key.
- **claims-map** (`:184` is the renderer's `CLAIMS_MAP`): 4 language hits, all
  negations or routed-question prose (`:22` "referent, date, clearance or canon
  standing is claimed by any row"; `:61,:162,:163` are the carried `u.basis`
  strings of D4-CL01/CL11). The renderer re-parses it as **12 D4 rows** and
  raises `ArtifactError` otherwise (`tools/exercise-handoff-e2e.py:2291-2303`),
  and row 12's exit-0 chain proves the parse green.
- **repin.json**: 1 language hit — `"a pin is integrity, never truth and never
  clearance"` (`:5`), a negation. Its supersession discipline is explicit:
  "the filed r2..r6 rows and the r28 row stay byte-identical" (`:4`), and
  `R34-D-history` lists the six earlier baselines as "reading changed not
  verdict" rows (`:52` precedent). Row 9 confirms the five declared digests are
  the live bytes, so the freeze record is not stale.
- **Named finding carried (not this round's to fix): `R34-N1`** — the r6-row
  replay refusal surfaces as an unhandled `KeyError:
  'reports/round-20/handoff/claims-map.md'` rather than the designed
  `E2E-DIGEST` leg (`repin.json` `R34-D-stale-row`). Owner: renderer hardening
  — **which is round 35's claim O**, so this round's O block discharges it; the
  A claim only records that the r6 bytes stay untouched, which row 2 confirms.

### 3.2 receipt_guard_adoption.py + adoption-inventory.json — GREEN on scope, NAMED FINDING on registration

- **In-lane ownership:** `ROOT = Path(__file__).resolve().parents[2]`
  (`tools/harness/receipt_guard_adoption.py:58`, and again inside each fixture
  body at `:871,:897,:920,…`) resolves to the lane root; every write goes
  through `safe_path()` (`:881-891`). Live writes are confined to `.scratch`
  fixture trees (`:1023` `ROOT/.scratch/fixture-49.json`) and to fixture-body
  receipts under `reports/round-41…51/validation.json` (`:1024,:1035,:1045`) —
  **all inside disposable fixture bodies, never executed against the real
  tree** (the tool's own limits say so; §1 row 14 confirms the selftest runs
  synthetic runners only). **Scope correction folded from A02-F1:** this is
  true of the *automatic* write sites, but the `--out`/`--root` combination
  will accept a filed-round-shaped destination — A02's probe D
  (`--root .scratch/… --out reports/round-34/op/probe.json`) is **accepted**
  (`_safe_out`, `:1261-1267`, refuses only absolute paths, `..`, `.git` and any
  `validation.json` name). The honest form of the claim is therefore "the
  refusal set covers the escape classes the docstring names; it does not
  enforce a filed-round boundary". **Zero sibling or parent path references:**
  the `chousa|kake|kotoba|game-dev` scan over `op/adoption-inventory.json` →
  **0 hits** (grep exit 1), and A02's repo-wide `receipt_guard_adoption` grep
  resolves only to this lane's own files.
- **Language:** `grep -ciE 'promotion|canoniz|clearance|closure|certif'` over
  `tools/harness/receipt_guard_adoption.py` → **0**. The tool's docstring frames
  itself as a static census with a `could-not-evaluate` class for unknowns and
  "no green path for a mechanism it cannot resolve" — no verdict language.
- **The census is real and complete:** `census_complete: true`, `gaps: []`,
  selftest 38/38 (row 14). Its two findings are routed, not absorbed:
  `RGA-1-round-26` (the F-C13-1 parenthetical names `:90`/`:1909` as unguarded,
  live bytes classify **guarded-refresh**) and `RGA-2` (8 unguarded writers not
  in the declared set: r8, r9, r10, r11, r12, r19, r21, r29) — both
  `owner: integrator (round 34) — filed LOG.md bytes are not edited; this row is
  the new-record correction`.
- **NAMED FINDING S03-F1 — the new tool is the only live non-fixture module not
  registered on SKILL.md's executable surface.** `SKILL.md:446-458` is the
  lane's surface registry and names the four harness modules it uses
  (`packet_links.py:452`, `receipt_guard.py:453`, `r8_checks.py:454`, plus
  `packet_uncertainty.py:89`). `tools/harness/receipt_guard_adoption.py` is
  absent from `SKILL.md`, `AGENTS.md` and every `corpus/lessons/*.md`
  (`grep -n receipt_guard_adoption` → 0 hits). The box-1 survey cannot see it:
  `reports/round-30/craft/box1-survey.py:6` derives its set from
  `re.findall(r"tools/[\w./-]+\.py", skill)` — **SKILL.md → tools**, never
  tools → SKILL.md — so `unnamed_in_skill: []` means "every *named* tool
  resolves", not "every tool is named". A direct set-difference confirms
  `tools/harness/receipt_guard_adoption.py` is the **only** live tool outside
  the immutable `tools/gates/{frozen,expected}/**` snapshots that SKILL.md does
  not name. Owner: integrator (register it on the surface table, or record an
  explicit not-registered decision) — a **round-35 obligation**, since the
  registry is the surface the box-1 evidence rests on.

### 3.3 examples/ digest repoints + culture-d3 repoint — GREEN, stale-pointer finding CLOSED

Round 33's four example edits were exactly the digest repoint
`50c4c2f2… → 5f4c02bf…` (`git show da68a6d -- examples/`: `README.md:104`
digest chain, `handoff.md:27` contract_ref and `:74` A-CONTRACT row,
`sample.md:21` contract_ref, `sample.yml:45,:78`). Live state:

- `grep -rn '50c4c2f2\|e834f503' examples/` → **0 hits** (row 18). This
  **closes** the finding filed at `reports/round-33/adj/A10-receipt.md`
  A10-F14 / `reports/round-33/adj/A06-contested.md:121-140`, which recorded five
  stale pointers at
  `examples/handoff-packet.sample.md:21`, `sample.yml:45,78` and
  `culture-d3/handoff.md:27,74`. New-row record: the r33 landing **is** that
  record; no further repair is owed.
- Every surviving language hit in `examples/` is a negation or a
  non-assertion: `not canonized` (`sample.md:1,15`; `sample.yml:16,71`;
  `culture-d3/README.md:144,145,148`; `handoff.md:1,20,104,267`), `never
  canonize` (`handoff.md:38,194`), `no canon, promotion, or completion claim`
  (`handoff.md:254,286`), `no real-language clearance … may be inferred`
  (`handoff.md:17,104`; `README.md:13`). **Zero asserting hits.**
- Boundary correctness: both sample gates exit 0 (row 11); `examples/` remains
  in-lane non-canon per `PROVINCE.md:13` ("non-canon examples") and carries no
  lore-asset claim.

### 3.4 round-33 SKILL.md / AGENTS.md edits — GREEN

- **AGENTS.md:** `git show da68a6d -- AGENTS.md` is a **pure deletion** of the
  orphan fence and the `### 2.2 \`SKILL.md\` — append one item … (after :534)`
  heading. Live: `wc -l AGENTS.md` → **40**; `grep -c '^\`\`\`' AGENTS.md` →
  **0** (grep exit 1). This closes the r33 A10-F15 / A07-F1 / A14 orphan-fence
  finding as **removed**, not moved. Digest `5ae7a9c8…` unchanged since r33.
- **SKILL.md:** the +35/−18 diff is three erratum rewrites (retired anchors
  `TL-01`/`TL-02`/`FIELD_DEFAULTS` re-pointed to live tool lines), one
  history-retaining-copy clarification, and the D3 checklist item gaining its
  explicit path (`examples/culture-d3/packet.gates.yml`). Language scan over
  SKILL.md/AGENTS.md for the refuses-list vocabulary (`chousa|kake|kotoba|
  game-dev|web publish|prompt/skill craft`) returns **only the PROVINCE-mandated
  refuses lines** (`SKILL.md:3` description anti-triggers, `:517-518` the
  refuses block) — i.e. the negations PROVINCE itself requires, not bleed.
- Line-count movement 715 → 732 is recorded as new rows by round 34
  (`craft/anchor-reissue.md`); no filed anchor row was edited.

### 3.5 ceilings errata + box-1/reissue records + contract-read-record — GREEN, routed-not-absorbed

- **`corpus/knowledge/linguistics/register-lexicon-ceilings.md`:** the r33
  change is a `## 12. Errata (round 33)` block opening "**Append-only.** Nothing
  above is rewritten" — a self-consistent append-only correction that
  re-measures five absence sweeps and names the one pre-existing hit
  (`sound-symbolism.md:106`) as the authoring defect `X63-F2`, "reported … and
  routed, never repaired". Language scan for
  `promotion|canoniz|clearance|closure` → **0 hits** (grep exit 1).
- **`reports/round-34/craft/box1-resurvey-durable.json`:** 1 language hit, a
  negation field: `"not_a_promotion_verdict": "… promotion decisions stay
  operator-owned"` (`:9`). Digest matches live SKILL.md (row 17).
- **`reports/round-34/craft/anchor-reissue.md`:** 0 language hits.
- **`reports/round-33/adj/contract-read-record.md`:** a kotodama-side §1 read
  only — `read_at: 2026-10-19T04:33:17Z`, `file_sha256: 5f4c02bf…` (matches
  row 8), and a scope line that explicitly excludes the other side: "this
  record does not represent lore's read, acceptance, receipt, or canon
  standing" (`:9`). **Correctly routed, not absorbed.**
- **Contested items remain routed:** fleet L0 `:44` (bilateral read) and `:45`
  (digest ratification) are still open on the lore side; `:47` (freshness
  threshold) is operator-owned and the pause is in force (`claims.json:19`).
  The r7 packet restates the same posture at `:300`. **Zero absorption.**

### 3.6 PROVINCE accuracy at HEAD — GREEN

`PROVINCE.md` is byte-stable: unchanged since `c53782a` (pre-round-5), empty
diff against `139e3b6`, `da68a6d` and HEAD (row 4). Against the live tree:

| PROVINCE clause | live measurement | verdict |
|---|---|---|
| `:10-11` six named partitions own the craft's records | exactly those six dirs, no seventh, no stray file in the partition root | GREEN |
| `:13` "this lane's own gates, source-check records, non-canon examples and reports" | `tools/gates` (12 gates + frozen/expected/fixtures), `tools/harness` (5 modules incl. the new tool), `examples/` (non-canon), `reports/` | GREEN |
| the three new artifacts are in-lane | `tools/harness/receipt_guard_adoption.py`, `reports/round-34/handoff/declared-in-r7/**`, `reports/round-34/handoff/repin.json`, and the repointed `tools/exercise-handoff-e2e.py` — **all tracked, all under the owns-list surfaces** | GREEN |
| `:16-19` refuses canon/rights/game-dev/research-method/publishing/prompt-craft | none of the six refuses surfaces is written by r33/r34: the only hits are the refuses-list *statements* themselves (`SKILL.md:3,517-518`) | GREEN |
| `:22-25` adjacent contract, contested → report never absorb | contract digest unchanged and pinned; contested items restated routed (§3.5) | GREEN |
| `:27-29` write scope = this repo only | rows 1–2: zero tracked-byte change outside this repo; no sibling tree written | GREEN |

**No PROVINCE edit is owed at HEAD.** The r33 A01-1 precision correction
("pre-round-5", not "pre-round-8") is reproduced and still the correct wording
(`git log --oneline -3 -- PROVINCE.md` → `c53782a`, `a527120`).

### 3.7 Preservation — GREEN

`git diff-index --quiet HEAD` → exit 0 (row 1); the scoped status over rounds
1–34, `corpus/lessons` and `tools/gates/frozen` → **0 rows** (row 2); the only
untracked paths are this round's own `reports/round-35/**` (row 13). Tracked
total 2815 = 1988 round paths + 237 frozen + 179 lessons (row 3). The r33
mutation incident (r5/r6/r7 receipts rewritten then restored) is not repeated:
this seat ran **no** filed round runner, and the adoption census (row 15) is the
standing instrument against the class.

## 4. Findings carried by this receipt

| id | finding | owner | status |
|---|---|---|---|
| **S03-F1** | `tools/harness/receipt_guard_adoption.py` — round 34's new durable tool — is **not named in `SKILL.md`** (nor AGENTS.md/lessons), and is the only live non-fixture tool outside `tools/gates/{frozen,expected}/**` that SKILL.md does not name. The box-1 survey cannot detect this class: it reads SKILL.md → tools, so `unnamed_in_skill: []` is not a completeness statement about the tool set. **Independently confirmed by A02-F2**, which adds the consequence this receipt did not state: `SKILL.md` is the *population source* for box-1, so naming the tool moves the denominator 28 → 29 and **supersedes the r34 box-1 receipt** — the `SKILL.md` edit and a box-1 re-survey **must land together**, as a new row. The gap was anticipated at `reports/round-34/calib/C07-verify-survey.md:194-196`; round-34 claim O's `after_required` did not include registration, so this is a discoverability gap, not a missed deliverable. | integrator (register on `SKILL.md:446-458` **together with** a box-1 re-survey, or record an explicit not-registered decision) | **open — round-35 obligation, two-seat confirmed** |
| **S03-F2** | **Superseded reading in a round-34 durable artifact.** `reports/round-34/op/adoption-inventory.json` records `runner_count 28`, `class_counts {guarded-refresh 17, unguarded-in-place 11}` (its own `date: 2026-10-19`, written 04:37); the live census reads **29 / {18, 11}** (§1 row 15). The set difference is exactly `reports/round-34/run-validation.py` — the round-34 runner is classified `guarded-refresh`, so no hazard is added. The filed inventory is a correct reading of its own window, not an error; the **new row is owed** (append-only, never an edit of the filed inventory). **Independently reproduced by five seats** — A07-F1, A09-F3, A10-F1, A11-F1, A02-F3; A11-F1 adds that the missing runner is *in* the filed commit (`4a7aede`, blob `08f0ebbb…`) and `LOG.md`'s ADMITTED entry already carries 29/18, so the JSON alone is the stale artifact; A02-F3 adds that `SCORECARD.md:616` cites the inventory as the evidence row for the 29 figure while the artifact carries 28, and that `reports/round-34/run-validation.py:210-211` already asserts 29/18. Severity label is disputed between the filers (A07 "medium", A02 "informational") — a label difference only, the evidence agrees exactly. | integrator (new census row) | open, non-material — five-seat confirmed |
| **S03-F3** | **The receipt was pre-audit-fragment at first read; the fold is now partial.** At this seat's cut every A-block dependency was absent (§1 row 0), so the per-surface verdicts in §3 are this seat's own execution under the missing-dependency rule — **not** independent verification. Eight siblings landed afterwards (A01, A05, A06, A07, A09, A10, A11, R06) and are folded in §6; **A02, A03, A04, A08, R07 and K04 remain owed**, so claim A's threshold "every touched surface verdict-filed" is still uncheckable for the three unlanded slices and the review pair is incomplete. | integrator + A02/A03/A04/A08/R07/K04 | **partially resolved by §6** |
| **S03-F4** | Carried, not mine to judge: **R34-N1** (the r6-row `KeyError`) is routed to renderer hardening and is **round 35's claim O** — the A claim's only obligation on it is that the r6 bytes stay untouched, which row 9 / `repin.json` `R34-D-history` confirm. If O lands, R34-N1 closes this round; if O is rejected, R34-N1 stays routed and the A verdict is unaffected. | claim-O seats + integrator | carried |
| **S03-F5** | Carried: the r33 A10-F14 / A06 stale-digest finding is **CLOSED at HEAD** by the r33 landing (§3.3) — a new-row reading, no filed row edited. The integrator should not carry it forward as open. | integrator (carry as closed) | resolved |
| **S03-F6** | Carried, cosmetic: the empty nested tree `kotodama-shokunin/reports/round-29/defects/` (4 dirs, 0 files) still exists (§1 row 19). In-lane, contentless, invisible to git; no PROVINCE impact. | integrator (optional cleanup) | unchanged from r33 |
| **S03-F7** | **The frozen r7 packet misdescribes its own claims-map source — carried from `review/R07-a-review.md` R07-F3, independently reproduced here.** `packet.md:3` (the renderer's hard-coded header literal, `tools/exercise-handoff-e2e.py:2700`) names `reports/round-20/handoff/claims-map.md`; the same file's manifest row A-57 (`:95`), §reads (`:113`) and §claims (`:125`) name the r34 successor map. The two revisions differ (`4b1b9a35…`/275 lines vs `d181de28…`/259 lines). **This receipt's own §3.1 first draft quoted `packet.md:3` without catching the contradiction** — the finding is R07's. Remedy: a new packet revision or a named-errata row, **never an in-place edit** (freeze bytes pinned; re-freeze is a round-35 non-goal, `claims.json:70`). | renderer/packet owner (r34 D-block) + A08 must carry it | **open — carried, verified** |
| **S03-F8** | Carried from R07: **R07-F1** (A06 citation errata — `lore-shokunin/PROVINCE.md:9` not `:10`; `MANIFEST.json:2314` not `:2312`; verdicts unchanged), **R07-F2** (a continuity pin is owed for post-edit corpus/example bytes: the r33 ceilings reading `bb579d51…`/289 lines is the *pre-edit* reading, HEAD is `afe8bf22…`/317, and the four r33 example repoint targets are pinned nowhere), **R07-F4** (owns-list probe width). None is bleed; each needs an A08 row or an explicit exclusion. | integrator / A08 | carried |

## 5. What this receipt does not establish

- Not round acceptance, not an axis verdict, not a promotion/canon/clearance/
  closure statement (`claims.json:67-73`). No axis is judged here.
- Not a review pass: **R07 filed nothing**, so no adversarial finding from the
  second reviewer is folded; **R06 landed** and its findings are folded in §6,
  but a single adversarial pass is not the round's declared review pair.
- Not independent verification by *this* seat: §3 is this seat's own execution.
  The independence leg landed afterwards — **A11** re-derived the PROVINCE checks
  and spot-checked the A01/A02 slices, and **A07** re-ran the A-block command set
  — and both are folded in §6. Their coverage does not reach A03/A04/A08's slices.
- The language scans are **token-scoped and time-stamped**, not continuous: they
  cover the declared artifact set at 08:14–08:26Z and cannot prove the absence
  of a transient write-and-restore between samples (the r33 class).
- The preservation readings are sampled at the recorded instants (rows 1–3), not
  a watch; the adoption census is the standing instrument against that class.
- No fleet-root surface was assessed beyond the in-repo L0 pointer reads; no
  sibling tree, world bible or domain source tree was read.

## 6. Fold register — A-block fragments that landed after this seat's first read

Read at 2026-10-19T08:40–08:55Z, HEAD `4a7aede` unmoved. Eight A-block fragments
landed after this seat's §1 census: **A01, A05, A06, A07, A09, A10, A11, R06**
(plus the cross/scribe siblings S04/S05, not folded here). Each is folded as
**agreement or named divergence** — never averaged, and none is certified by
this receipt.

| sibling | cut | what it contributes | agreement with this receipt |
|---|---|---|---|
| `adj/A01-r7-packet.md` (283 lines) | landed post-cut | r7 slice: **all seven** digest claims re-measured and resolving (§1); a classified 10-family cross-domain language scan (§2); the lore-owned routing table (§3); **A01-F1** — an affirmative `canonical E0–E3 tag` usage (technical era-space sense); **A01-F2** — the `R34-N1` mechanism refined from `repin.json`'s wording; a machine-twin scope note (§4) | **agrees** with §3.1 on every overlapping leg (packet/claims-map/repin language = negations + routing; digests live; canon routed). A01-F1 ≡ A11-N3 (same non-bleed technical usage). Its §1 adds `run.log`'s digest `ffae4ecd…` and `repin.json`'s self-digest `1022b603…`, which §1 rows 9/13 did not take |
| `adj/A05-records.md` (304 lines) | landed post-cut | ceilings §12 + box-1/reissue + contract-read-record slice: all five **GREEN**; the five §12 absence sweeps **reproduce exactly** (§2.1); **A05-F1** — one row digest inside `box1-resurvey-durable.json` is **stale at the delivered revision** (27/28 row digests resolve); **A05-P1** — a precision note on the reissue's `:715 → :731-732` map | **agrees** with §3.5 on ceilings (0 tokens), the box-1 receipt's `skill_sha256` and the contract-read-record. **A05-F1 is a finding this receipt did not measure** — §1 row 17 checked only the top-level `skill_sha256`; carry A05-F1, do not treat my row 17 as its refutation |
| `adj/A06-province.md` (229 lines) | 08:17:02Z | five PROVINCE checks, all **PASS**: blob `313b182f…` at `139e3b6` and HEAD; owns-list six partitions (21/19/18/29/20/94 = 201); the three r33/r34 surfaces in-lane; refuses-list siblings all live with matching provinces; write scope | **agrees** with §3.6 on every leg. Adds what §3.6 did not measure: the six sibling `PROVINCE.md` reads, the new tool's in-lane roots (`:59-63` `SWEEP_ROOTS = ("reports","tools")`), the renderer's in-tool canon traps (`:228-235`, `:485`), and `run.log`'s gitignore status (`.gitignore:3`) |
| `adj/A07-verify.md` (212 lines) | landed post-cut | 14-row independent re-run table; **A07-F1** ≡ S03-F2 (inventory one runner short, "medium"); **A07-F2** — the repointed surfaces carry an under-dated measurement provenance (low); **A07-F3** — A04's slice wording attributes to r34 bytes r34 never moved (low); **A07-F4** — the language leg needs a term-collision exemption list; **A07-G1** — the r33/r34 added-lines language scan is green | **agrees** with §1 rows 9/10/12 and §3.1. Its `R34-N1` reproduction ran in an **isolated `git archive` copy** and names the raise site `tools/exercise-handoff-e2e.py:3822` (the `assembly.digests[rel]` lookup) — a sharper site than §3.1's file-level citation. A07-F3 **bears on §2/§3.4**: my census also attributes the SKILL.md/AGENTS.md/lessons-README/ceilings edits to round 33, so A07-F3 does not bite this receipt |
| `adj/A09-receipt.md` (278 lines) | 08:14–08:26Z | a parallel 14-surface verdict table with its own census; **A09-F1** — the r34 `SCORECARD.md` edit is 28/3, the **first with deletions in 12 commits** (the removed lines are the predecessor rolling "Next:" pointer, content preserved in the r34 axis table); **A09-F2** — the r33 fragment set's language leg is not verdict-filed (246/39/99/191 raw hits need A08's declared-scope verdict); **A09-F3** ≡ S03-F2; **A09-F4** ≡ S03-F3 (dependency gap) | **agrees** with §3.1–§3.7 on every overlapping verdict, and independently derives the same two-commit census. **A09-F1 and A09-F2 are findings this receipt did not measure** — carry both. Its §11 already registers this receipt as a sibling requiring row-for-row reconciliation, not merging |
| `adj/A10-gap-fill.md` (245 lines) | landed post-cut | a third independent full-A-claim pass with its own re-derived census; **A10-F1** ≡ S03-F2; **A10-F2** adjudicated-and-not-filed (recorded so no peer re-files it); a stale-digest adjudication; a PROVINCE re-derivation; r33 ledger items closed at HEAD | **agrees** with §3.1–§3.7. Its A10-F2 adjudication is the class my §5 language-scope caveat names |
| `adj/A11-verify-2.md` (372 lines) | landed post-cut | the **independent verifier** leg: PROVINCE re-derivation (§1a/§1b GREEN); A01 slice spot-check (§2: **12/12 rows content-identical** carry, 5/5 freeze digests live, both repin controls reproduced, 15/15 link targets resolve); A02 slice spot-check (§3: selftest 38/38, safe-by-construction, language clean); **A11-F1** ≡ S03-F2 with the decisive addition that `reports/round-34/run-validation.py` **is in the filed commit** (blob `08f0ebbb…`) and `LOG.md`'s ADMITTED entry already carries 29/18 — so the JSON, not the LOG, is the stale artifact; **A11-N1** — `PROVINCE.md` names "this lane's own gates" but not `tools/harness/` explicitly; **A11-N2** — the claims-map→packet carry is content-identical but **not byte-identical** (wrapping and link separators differ), so a byte-equality verifier false-fires; **A11-N3** ≡ A01-F1 | **agrees** with §3.1–§3.7 and is the strongest fold here: it is a *second seat* reproducing §1 rows 9/10/12/14/15/16/18 independently. **A11-N1 is adjacent to but distinct from S03-F1**: N1 says PROVINCE could name `tools/harness/`; S03-F1 says SKILL.md's executable-surface registry does not name the tool at all. Both stand |
| `review/R06-a-review.md` (222 lines) | landed post-cut | the adversarial diff-based census (`cdd66d7 → 4a7aede`: 172 paths = 160 A + 11 M + 1 D; 158 report files + 14 out-of-report surfaces; 160 − 1 = +159 = 2656 → 2815 fully reconciled); **F-R06-1** — `corpus/lessons/README.md` (r33's largest live non-report edit, +130/−28, 33 byte/line/sha8 pins) is **not named** in the A-claim's declared surface list nor assigned to any A01–A10 mission — re-measured green (33 rows, 0 duplicates, 0 mismatches) but **unfiled**; **F-R06-2** — `declared-in-r7/run.log` is untracked by `.gitignore:3` and so invisible to a fresh clone (systemic, ≥6 earlier handoff dirs, low severity); **F-R06-3** — the window's single deletion (`.ufo/reports/round-32/kotodama.md`) is pre-baseline; **F-R06-4** — the freeze read-set ∩ touched surfaces = **∅** (load-bearing for X00/R08); **F-R06-5** — language + PROVINCE spot check green | **agrees** with §2's census on every out-of-report surface, and **F-R06-1 is the important one**: this receipt's §2 *does* name `corpus/lessons/README.md` (row 3), so the missed-surface gap is in the *claim's declared list* (`claims.json:56`), not in this census. F-R06-2's `run.log` is the same artifact A06 and A11 also flagged (all three call it non-material). F-R06-4 independently supports §1 row 9 |
| `review/R07-a-review.md` (198 lines) | 08:19:34Z | the second adversarial A pass: a C1–C6 completeness criterion set for a PROVINCE re-verification; ten probes M1–M10; the **A06↔A11 reconciliation** (§4, the item A11 left owed) finding **zero disagreements**; **R07-F1** — A06 citation errata (precision only: `lore-shokunin/PROVINCE.md:9` not `:10`; `MANIFEST.json:2314` not `:2312`); **R07-F2** — a continuity pin is owed for post-edit corpus/example bytes (the r33 ceilings reading `bb579d51…`/289 is the **pre-edit** reading; HEAD is `afe8bf22…`/317, and the four example repoint targets are pinned nowhere); **R07-F3** — the frozen packet misdescribes its own claims-map source (folded into §3.1 above); **R07-F4** — owns-list probe width (A06 probes `ls tools/gates/` while the r34 surface lives in `tools/harness/`) | **agrees** with §3.6 and with A06/A11, and **adds three things this receipt did not measure**: R07-F3 (a real defect on the packet surface — see §3.1), R07-F2 (post-edit digest pins), and R07-F1's corrected sibling pointers. R07-F4 is the same ambiguity A11-N1 files. R07 also **closes R06-F1 and R06-F2** as answered by A09's receipt table and A06's gitignore note respectively — so those two do not need separate integrator rows |
| `adj/A02-adoption-tool.md` (234 lines) | landed at final read | the A02 slice, read in full and probed: in-lane ownership **green** (the tool's population is this lane's own runners, its sweep roots in-lane, zero sibling/world-bible/domain references repo-wide); language/bleed scan **green** (word-boundary scan → zero matches in both artifacts); **A02-F2 ≡ S03-F1** — the registration gap, with the decisive added consequence that `SKILL.md` is the *population source* for box-1, so **naming the tool moves the denominator to 29 and supersedes the r34 box-1 receipt**: the `SKILL.md` edit and a box-1 re-survey **must land together** as a new row; the gap was anticipated at `reports/round-34/calib/C07-verify-survey.md:194-196`; **A02-F1** — the write-scope claim is **broader than the mechanism**: `_safe_out` (`:1261-1267`) refuses absolute paths, `..`, `.git` and any `validation.json` destination, but probe D (`--root .scratch/… --out reports/round-34/op/probe.json`) is **accepted**, so "never writes into a filed round" is not a property the code enforces; **A02-F3 ≡ S03-F2** (independently re-derived; severity labeled "informational" vs A07's "medium"); **A02-O1** — a foreign `--root` emits `RGA-1-*` declared-hazard mismatch noise | **agrees** with §3.2 on ownership, in-lane roots and language, and **independently confirms S03-F1 as A02-F2 with a consequence I did not state** (the paired box-1 re-survey). **A02-F1 corrects the scope of my §3.2**: I wrote that live writes "are confined to `.scratch` fixture trees" — true for the *automatic* write sites, but the `--out`/`--root` combination will accept a filed-round-shaped destination, so the honest form is "the refusal set covers the escape classes the docstring names; it does not enforce a filed-round boundary". A02-F3 gives my S03-F2 its fifth independent reproduction |

**Net fold result:** no sibling contradicts any verdict in §3, and four
independent seats (A07-F1, A09-F3, A10-F1, A11-F1) reproduce S03-F2. Two
findings this receipt did not measure are carried in — **A05-F1** (stale row
digest inside the box-1 durable receipt) and **A09-F1/A09-F2** (the SCORECARD
deletion and the r33 fragment-set language gap) — and one claim-level gap is
confirmed: **R06-F1** shows the declared surface list omits the lessons index
even though this census and R06's both see it.

## Owed

**Landed since this seat's first read and folded in §6:** `adj/A01-r7-packet.md`,
`adj/A02-adoption-tool.md`, `adj/A05-records.md`, `adj/A06-province.md`,
`adj/A07-verify.md`, `adj/A09-receipt.md`, `adj/A10-gap-fill.md`,
`adj/A11-verify-2.md`, `review/R06-a-review.md`, `review/R07-a-review.md`.

**Still absent at this seat's final read (2026-10-19T08:26Z)** — their owners
land them; the integrator folds them into `reports/round-35/adj/A08-audit-draft.md`
(A08's mission, `targets.json:307`) and completes the post-review legs here.

- `reports/round-35/adj/A03-examples.md`
- `reports/round-35/adj/A04-skill-agents.md`
- `reports/round-35/adj/A08-audit-draft.md`
- `reports/round-35/scout/K04-touched-census.md`

Also owed, none of it this seat's to produce:

- **S03-F1's registration decision** — add `tools/harness/receipt_guard_adoption.py`
  to `SKILL.md`'s surface table, or record an explicit not-registered decision
  with its reason. Either way it is a **new row**, not an edit of filed bytes.
  A11-N1 is the adjacent-but-distinct PROVINCE-side wording question; neither
  substitutes for the other.
- **S03-F2's new census row** — the live 29-runner reading (§1 row 15) as an
  append-only successor to `reports/round-34/op/adoption-inventory.json`. Now
  **four-seat confirmed** (A07-F1, A09-F3, A10-F1, A11-F1); A11-F1's decisive
  addition is that the missing row is in the filed commit and `LOG.md` already
  carries 29/18, so the JSON alone is stale.
- **Carried findings from §6 that need integrator rows:** A05-F1 (box-1 stale row
  digest), A09-F1 (SCORECARD r34 deletion), A09-F2 (r33 fragment-set language
  verdict), R06-F1 (the declared surface list omits `corpus/lessons/README.md`),
  R06-F2 (`run.log` untracked), A07-F2/F3/F4, A10-F2, A11-N1/N2/N3, A01-F1/F2.
- **`reports/round-35/run-validation.py`** — claim A's only counting command
  (`claims.json:62`); it does not exist at this seat's reads, so no A threshold
  can be measured green until the integrator writes it.
- The **A-claim verdict itself** — this receipt supplies the evidence; the
  per-surface fold and the admit/reject call are the integrator's
  (`REGIMEN.md:36-43`).

## Citations

- `reports/round-35/claims.json:8-9,19,53-65,62,67-73` — baseline, pause,
  claim A (before/after/thresholds), counting command, non-goals
- `reports/round-35/targets.json:5-12,307,421-427` — shared rules,
  missing-dependency rule, A08 mission, S03 mission + out path
- `REGIMEN.md:25-50,60-69` — per-round contract and scope
- `PROVINCE.md:3-7,9-14,16-19,22-25,27-29`
- Landed surfaces audited: `SKILL.md:3,89,446-458,517-518`;
  `AGENTS.md` (40 lines, 0 fences); `corpus/lessons/README.md`;
  `corpus/knowledge/linguistics/register-lexicon-ceilings.md:291-317` (the
  append-only errata block);
  `examples/handoff-packet.sample.md:1,15,21`;
  `examples/handoff-packet.sample.yml:16,45,71,78`;
  `examples/culture-d3/README.md:13,104,144,145,148`;
  `examples/culture-d3/handoff.md:1,17,20,27,38,74,104,194,254,267,286`
- `tools/exercise-handoff-e2e.py:184,1933-1934,2290,2291-2303,2566,2779,3521-3531`
  (the round-34 repoint set, from `git show --unified=0 4a7aede`);
  `git show --numstat 4a7aede -- tools/exercise-handoff-e2e.py` → `11 10`
- `tools/harness/receipt_guard_adoption.py:13-14,58,66,68,113,782-783,871,881-891,1023-1045,1083-1089,1288-1299`
- `reports/round-34/handoff/declared-in-r7/{packet.md,claims-map.md,expected.json,freeze.txt,twin.json}`
  (digests, gates, contract pins); `reports/round-34/handoff/repin.json`
  (`R34-D-*` rows, `R34-N1`, `R34-N2`, limits)
- `reports/round-34/op/adoption-inventory.json` (`census_complete`,
  `runner_count 28`, `class_counts`, `findings` RGA-1-round-26 / RGA-2,
  `declared_hazards`, `gaps: []`)
- `reports/round-34/craft/box1-resurvey-durable.json:9`;
  `reports/round-34/craft/anchor-reissue.md`;
  `reports/round-30/craft/box1-survey.py:4-8,6`
- `reports/round-33/adj/contract-read-record.md:1-9`;
  `reports/round-33/adj/audit-assembled.md:3` (negation);
  `reports/round-33/adj/A01-province.md:27-48,50-60` (PROVINCE pre-round-5
  correction, owns-list convention);
  `reports/round-33/adj/A06-contested.md:121-140` (stale-pointer finding, now
  closed); `reports/round-33/adj/A10-receipt.md` A10-F14 (same);
  `reports/round-33/calib/open-items-ledger.json:93-220` (19 routed hits, all
  pointers to filed r24 promotion-review rows or operator-ownership routing)
- `/home/vgpnk/Projects/shokunin/.ufo/l0-questions.md:44,45,46,47` (read-only)
- **Folded A-block siblings (§6):** `reports/round-35/adj/A01-r7-packet.md`
  (7/7 digests, 10-family scan, A01-F1/F2, §3 routing table);
  `adj/A05-records.md` (§2.1 five-sweep reproduction, A05-F1, A05-P1);
  `adj/A06-province.md` (five PASS, sibling refuses reads,
  `receipt_guard_adoption.py:59-63`, `exercise-handoff-e2e.py:228-235,485`);
  `adj/A07-verify.md` (14-row table, A07-F1/F2/F3/F4/G1,
  `exercise-handoff-e2e.py:3822`);
  `adj/A09-receipt.md` (§3 14 surfaces, A09-F1/F2/F3/F4, §11 fold-in register);
  `adj/A10-gap-fill.md` (census re-derivation, A10-F1, A10-F2, PROVINCE
  re-derivation); `adj/A11-verify-2.md` (§1a/1b, §2a-2f, §3a-3d, A11-F1,
  A11-N1/N2/N3); `review/R06-a-review.md` (§2 172-path census, F-R06-1…F-R06-5,
  §4 method limitation); `review/R07-a-review.md` (§1 C1–C6 criteria, §2 M1–M10,
  §3 A06 coverage, §4 A06↔A11 reconciliation, **R07-F1/F2/F3/F4**, §6 verdict);
  `adj/A02-adoption-tool.md` (ownership/language green, **A02-F1** write-scope
  probe table A–E, **A02-F2** registration + paired box-1 consequence, **A02-F3**
  count reconciliation, A02-O1, reproduction-command table)
- **Fold-window commands (2026-10-19T08:40–09:0xZ, same env):**
  `find reports/round-35 -type f` (26 files at final read);
  `wc -l reports/round-35/adj/*.md reports/round-35/review/*.md
  reports/round-35/scout/*.md`; `sed -n`/`grep -n` reads of the nine folded
  fragments; R07-F3's independent reproduction — `grep -n "are carried from"
  reports/round-34/handoff/declared-in-r7/packet.md`, `sed -n '95p;113p;125p'`
  on the same file, `sed -n '2695,2705p' tools/exercise-handoff-e2e.py`,
  `sha256sum`/`wc -l` on both claims-map revisions; `python3 -` citation-resolver
  over this file (every full-path citation resolving except the deliberately-owed
  paths)
- Commands run by this seat, 2026-10-19T08:14:10Z–08:26Z, lane root, read-only
  except this file:
  `date -u '+UTC=%Y-%m-%dT%H:%M:%SZ'`; `git rev-parse HEAD`;
  `git log --oneline -8`; `git log --oneline --grep='round-33'|'round-34'`;
  `git show --numstat/--shortstat --format='' {da68a6d,4a7aede}` (filtered to
  non-`reports/round-<N>/` paths); `git show --format='' --numstat
  {da68a6d,4a7aede} -- {examples/,SKILL.md,AGENTS.md,PROVINCE.md,corpus/lessons/README.md}`;
  `git show --format='' --unified=0 4a7aede -- tools/exercise-handoff-e2e.py`;
  `git show --format='' {da68a6d,4a7aede} -- SCORECARD.md`;
  `git status --porcelain=v1 -uall` (whole tree and scoped to
  `reports/round-{1..34} corpus/lessons tools/gates/frozen`);
  `git diff-index --quiet HEAD`; `git diff --stat {139e3b6,da68a6d} HEAD -- PROVINCE.md`;
  `git log --oneline -3 -- PROVINCE.md`;
  `git ls-files | wc -l` (2815); `git ls-files | grep -c '^reports/round-'`
  (1988); `git ls-files tools/gates/frozen | wc -l` (237);
  `git ls-files corpus/lessons | wc -l` (179);
  `git ls-files 'reports/round-*/run-validation.py' | wc -l` (29);
  `git ls-files --error-unmatch <6 paths>`; `sha256sum PROVINCE.md AGENTS.md
  SKILL.md corpus/lessons/README.md
  corpus/knowledge/synthesis/worldbible-integration-contract.md
  reports/round-34/handoff/declared-in-r7/*`;
  per-partition `ls corpus/knowledge/$p/*.md | wc -l`;
  `ls -d corpus/knowledge/*/`; `ls -p corpus/knowledge | grep -v /`;
  `ls -la reports/round-35 reports/round-35/telemetry`;
  `find reports/round-35 -type f`; `find kotodama-shokunin -type d| -type f`;
  `ls -la out/ reports/round-34/{handoff,handoff/declared-in-r7,op,craft}`;
  `wc -l AGENTS.md`; `grep -c '^```' AGENTS.md`;
  `grep -rn '50c4c2f2\|e834f503\|5f4c02bf' examples/`;
  `grep -rniE 'promotion|canoniz|clearance|closure|certif'` over the declared
  artifact set; `grep -rniE 'chousa|kake|kotoba|game-dev|lore-shokunin|worldbible'`
  over `reports/round-34/handoff/` and `reports/round-34/op/adoption-inventory.json`;
  `grep -n receipt_guard_adoption SKILL.md AGENTS.md corpus/lessons/*.md`;
  `grep -n kotodama ../.ufo/l0-questions.md`;
  `python3 tools/gates/handoff-packet-check.py` (r7 packet + both samples);
  `python3 tools/exercise-handoff-e2e.py --profile v3 --quiet` (exit 0);
  `python3 -B tools/harness/receipt_guard_adoption.py --selftest` (38/38, exit 0)
  and `--json` (29 / {18,11}); `python3 -B reports/round-30/craft/box1-survey.py`
  (28/28, exit 0); two `python3 -c` set-difference probes (SKILL-named vs live
  `tools/**/*.py`; inventory runners vs live `git ls-files`); `python3 -c` digest
  compare of the box-1 durable receipt vs `SKILL.md`
