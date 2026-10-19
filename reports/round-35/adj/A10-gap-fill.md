- Seat: A10 | executor (spare) | claim A (adjacency) | date 2026-10-19 | baseline 4a7aede

# A10 — gap-fill across the A block

## What this is, and why it is not a slice

Mission: spare / gap-fill across the A block. At my dispatch time **no peer A-block
fragment existed** — `find reports/round-35 -type f` returned only `claims.json`,
`targets.json` and `telemetry/{availability-attempt-1,2,3,dispatch-declared}.json`
(command run 2026-10-19, HEAD `4a7aede`). So instead of filling one named hole I ran
the whole A-claim audit independently, so that whatever the peer seats land, the
integrator holds a complete second reading of every surface the claim names. Where a
peer slice later lands green, this document is its independent cross-check; where a
peer slice is short or missing, this document carries the verdict and the evidence.

Scope discipline: I read every surface; I wrote nothing but this file. No corpus
entry, no tool edit, no filed round byte, no `run-validation.py` execution — in-tree
or isolated (F-C13-1). The one instrument I executed is the round-34 adoption tool's
own `--selftest`, which is not a filed round runner and writes only into a disposable
in-tree `.scratch` temp dir (`tools/harness/receipt_guard_adoption.py:1083-1089`).

## Independent touched-surface census (K04's content, re-derived)

Derived from `git diff --name-status` against the two round commits, not from prose.
This is deliberately a *second* derivation, independent of K04's.

Round 33 (`da68a6d`) non-report changes:

| path | change |
|---|---|
| `AGENTS.md` | M (−2 lines) |
| `REGIMEN.md` | A |
| `SCORECARD.md` | M |
| `SKILL.md` | M (+35/−18) |
| `corpus/knowledge/linguistics/register-lexicon-ceilings.md` | M (+28) |
| `corpus/lessons/README.md` | M (+130/−28) |
| `examples/culture-d3/README.md` | M (1 line) |
| `examples/culture-d3/handoff.md` | M (2 lines) |
| `examples/handoff-packet.sample.md` | M (1 line) |
| `examples/handoff-packet.sample.yml` | M (2 lines) |

Round 34 (`4a7aede`) non-report changes:

| path | change |
|---|---|
| `tools/exercise-handoff-e2e.py` | M (the repointed renderer) |
| `tools/harness/receipt_guard_adoption.py` | A |

Round-34 report-tree artifacts the A-claim names: `reports/round-34/handoff/declared-in-r7/{packet.md,claims-map.md,expected.json,freeze.txt,twin.json}`,
`reports/round-34/handoff/repin.json`, `reports/round-34/op/adoption-inventory.json`,
`reports/round-34/craft/box1-resurvey-durable.json`, `reports/round-34/craft/anchor-reissue.md`;
round-33: `reports/round-33/adj/contract-read-record.md`.

**Census cross-check against R06's mission (diff-based):** the two commits touch
exactly the surfaces above and nothing else outside `reports/round-33|34/`. No
sibling-lane path, no world-bible path, no `.ufo/` path appears in either diff.

## Per-surface verdicts

Each cell is exactly `green` or `named-finding`, per the claim's `after_required`.

| surface | verdict | evidence |
|---|---|---|
| declared-in-r7 packet set (5 files) | **green** | All five digests match both `repin.json`'s record and the live bytes: `packet.md 45f57132…`, `twin.json 0e229138…`, `expected.json bbe15887…`, `freeze.txt 3969954b…`, `claims-map.md d181de28…` (recomputed `sha256` vs `repin.json` rows[2].digests — all MATCH). `expected.json`'s own `packet_sha256` self-record `45f5713261762a95…` equals live `packet.md`. |
| `repin.json` | **green** | `canon` field: "NON-CANON engineering evidence; a pin is integrity, never truth and never clearance" (`repin.json:5`); `limits`: "pins the cascade surfaces only; not canon, not lore acceptance, not round admission" (`:53`). R34-N1 (the KeyError) is `state: "routed"` with owner "renderer hardening (future round)" — routed, not absorbed. |
| `tools/harness/receipt_guard_adoption.py` | **green** (ownership) / **named-finding A10-F1** (inventory count) | No outside-repo path reference (`grep -nE "\.\./|/home/|siblings|\.ufo"` → 0 hits). Census is static AST analysis; it never executes a filed runner (`subprocess` appears only inside selftest fixture *string literals* at `:1029-1034`; the docstring states the no-execution contract at `:22-23`). Selftest observed green: `--selftest` → `controls_passed: 38`, `controls_total: 38`, `selftest_passed: true`, exit 0. |
| `reports/round-34/op/adoption-inventory.json` | **named-finding A10-F1** | Filed `runner_count: 28`, `class_counts: {guarded-refresh: 17, unguarded-in-place: 11}`; live census at HEAD reads `live_runner_count: 29`, `live_class_counts: {guarded-refresh: 18, unguarded-in-place: 11}`. Delta is exactly `reports/round-34/run-validation.py` (set difference: `live-not-filed = ['reports/round-34/run-validation.py']`, `filed-not-live = []`). See findings below. |
| examples digest repoints (4 surfaces) | **green** | Live contract digest `5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069` (`sha256sum corpus/knowledge/synthesis/worldbible-integration-contract.md`) is carried at `examples/culture-d3/README.md:104`, `examples/culture-d3/handoff.md:27,74`, `examples/handoff-packet.sample.md:21`, `examples/handoff-packet.sample.yml:45,78`, and `examples/culture-d3/expected.json:4`. No stale full digest `50c4c2f2…` survives on any live mutable surface (see the stale-digest adjudication below). |
| round-33 SKILL.md edits | **green** | Live `SKILL.md` is 732 lines, sha256 `f9bd07c2bd13462367be20e8d775cec1c5569eb2e575dc5d078519ecc72e5a9b` — byte-identical to the durable r34 receipt's `skill_lines: 732` / `skill_sha256: f9bd07c2…` (`box1-resurvey-durable.json`). |
| round-33 AGENTS.md excision | **green** | Live `AGENTS.md` is 40 lines with **0** fence markers (`grep -c '^\`\`\`'` → 0) and no `### 2.2` / "append one item" residue. The diff removed exactly a stray closing fence plus a stray patch-scaffold heading — matches `anchor-reissue.md:216`'s `R`-class row for `AGENTS.md:42` (42 → 40 lines). |
| ceilings edit (`register-lexicon-ceilings.md`) | **green** | The r33 diff is purely additive after line 287 — a new `## 12. Errata (round 33)` block opening "**Append-only.** Nothing above is rewritten." It corrects the entry's own false absence sweeps and routes the one pre-existing hit as `X63-F2` (r28 audit) rather than repairing or absorbing it. |
| box-1 / reissue records | **green** | `anchor-reissue.md:6,10,35` re-issues superseded anchors as a NEW table: "filed rows citing old anchors stay byte-identical as superseded readings", "never edited". `box1-resurvey-durable.json:9` carries `"not_a_promotion_verdict": "…promotion decisions stay operator-owned"` and reports 28/28 named executables resolvable, 0 unresolvable. |
| `contract-read-record.md` | **green** | `:9` reads `scope: §1 gate only; this record does not represent lore's read, acceptance, receipt, or canon standing.` Its recorded digest `5f4c02bf…` equals the live contract digest. Correctly one-sided; not describable as bilateral acknowledgement. |
| PROVINCE accuracy at HEAD | **green** | See the dedicated section below. |
| worktree / preservation | **green** | `git status --porcelain` returns only `?? reports/round-35/` — no uncommitted modification on any live surface, no filed-round byte moved, `tools/gates/frozen/**` untouched. |

## Findings

**A10-F1 — the filed adoption inventory contradicts its own round's SCORECARD
(severity: low; owner: integrator, record).** `reports/round-34/op/adoption-inventory.json`
records `runner_count: 28` and `class_counts {guarded-refresh: 17, unguarded-in-place: 11}`.
The live census at HEAD `4a7aede` reads 29 runners and `{guarded-refresh: 18,
unguarded-in-place: 11}`. The one-row delta is `reports/round-34/run-validation.py`,
which landed in the *same* commit `4a7aede` that filed the inventory — so the
inventory was a pre-landing snapshot of a tree that the same commit then changed.
This is not an ownership or bleed defect and it does not falsify the r34 claim (the
census was complete over the tree it read: `census_complete: true`, `gaps: []`). It is
a *reader hazard*: any consumer who cites "28 runners" at HEAD will be wrong by one,
and the drifted row is the `guarded-refresh` class — i.e. the class the round-34
finding is about. **Upgraded in the Delta section below:** `SCORECARD.md`'s own
round-34 row states "inventory of all 29 filed runners: 18 guarded-refresh / 11
unguarded-in-place", so the two round-34 artifacts contradict each other and the
SCORECARD is the one that matches the tree. Disposition: record the contradiction,
cite the count as 29/18/11 at HEAD per the SCORECARD row and the live census, name
the JSON field superseded by its own round. Do **not** edit the filed inventory bytes.

**A10-F2 — checked and NOT filed (adjudicated, recorded so no peer re-files it).**
`adoption-inventory.json:109` carries `"root": "/home/vgpnk/Projects/shokunin/kotodama-shokunin"`,
an absolute host path. I checked this against the lane's own convention before
filing it: 173 filed `reports/**/*.json` artifacts carry the same absolute lane root
(`grep -rl '/home/vgpnk/Projects/shokunin/kotodama-shokunin' reports/ --include=*.json | wc -l` → 173),
including `reports/round-20/wart/repin-r20.json`, `reports/round-26/audit/x63-lessons-receipt.json`,
`reports/round-26/remainders/pin-repoint-receipt.json`, `reports/round-27/audit/x57-lessons-receipt.json`,
`reports/round-28/audit/x57-lessons-receipt.json`. It is a standing convention, not a
new bleed class, and it is the lane's own root, not a sibling path. **No finding.**

## Stale-digest adjudication (the one live-corpus hit)

A repo-wide hunt for the superseded contract digest `50c4c2f2` outside filed rounds
1–33 and `.scratch` returns live-tree hits in `tools/gates/frozen/**`,
`reports/supplement-opencode-1/**`, `LOG.md`, `corpus/lessons/round-2-adjacency.md`,
`corpus/lessons/round-9.md`, and one `corpus/knowledge/` entry. Adjudicated:

- `tools/gates/frozen/**` — **pinned frozen bytes; must not change.** Their carrying
  the old digest is the freeze working as designed.
- `LOG.md`, `corpus/lessons/round-{2-adjacency,9}.md`, `reports/supplement-opencode-1/**`
  — append-only historical records. `corpus/lessons/round-9.md:142` records the
  transition itself (`50c4c2f2… → 5f4c02bf…`). Correct as history.
- `corpus/knowledge/verification/gate-frozen-run-standard.md:9` — the only hit on a
  live, mutable knowledge surface, and it is **not a defect**: the line reads "Digest
  of the file as read: `sha256:50c4c2f2…8fb7268c1`" inside a source list whose entry
  declares `verified-at: 2026-10-17` against lane revision `16887909ed66e8e4fb4c82a20d0d18084f430518`.
  It is a *revision-and-date-pinned historical reading*, which is exactly what this
  lane's own frozen-run standard demands of a verdict. Rewriting it to the current
  digest would **destroy** the evidence that the reading was taken at a named
  revision. Leave it; a naive scanner flagging it is the scanner's error, not the
  entry's. (This is the class of false positive R06/R07 should not re-file.)

## PROVINCE accuracy re-verification at HEAD (A06's content, re-derived)

- **Owns-list partitions all resolve.** `PROVINCE.md:10` names six partitions; all
  six exist with the census the round declared: linguistics 21 / myth-symbol 19 /
  culture-material 18 / synthesis 29 / verification 20 / civilizations 94 = 201
  (`for p in …; do ls corpus/knowledge/$p/*.md | wc -l; done` at HEAD `4a7aede`).
- **The three new/changed artifacts are in-lane under the owns clause as written.**
  `PROVINCE.md:11` claims "this lane's own gates, source-check records, non-canon
  examples and reports". Mapped: `tools/harness/receipt_guard_adoption.py` = a lane
  gate/check instrument; `reports/round-34/handoff/declared-in-r7/*` = a non-canon
  example/report set (the packet self-declares `canon_standing: not canonized —
  lore disposition required (lore-shokunin owns canon)`, `packet.md:7`); the
  repointed `tools/exercise-handoff-e2e.py` = a lane gate. **No PROVINCE amendment
  is required by the r33/r34 landings.**
- **Refuses-list still accurate and unamended.** `PROVINCE.md:16-20` refuses canon
  recording, real-world rights/attribution rulings, game mechanics, chousa general
  research method, kake publishing, kotoba prompt/skill craft. `SKILL.md:517-518`
  restates the same set, and the r33/r34 edits did not weaken either. No r33/r34
  artifact asserts a refused activity.
- **Contested-scope clause intact and honoured.** `PROVINCE.md:22-25` routes
  contested scope to the integrator, never absorbed. Observed compliance:
  `contract-read-record.md:9` (lore's read is not claimed),
  `repin.json` R34-N1 (`state: "routed"`), `box1-resurvey-durable.json:9`
  (promotion stays operator-owned).

## r33 ledger items closed at HEAD — verified by diff, not by prose

The round-33 audit left items open. I verified closure from the diffs themselves, so
the integrator does not have to re-open the r33 fragments:

| r33 open item | state at HEAD | evidence |
|---|---|---|
| OI-05 — `worldbible-integration-contract.md:183` mis-cite | **closed** | `SKILL.md:128` now cites `tools/harness/packet_uncertainty.py:205,209` with a dated erratum clause naming the old anchor's real content |
| OI-06 — dangling tool anchors `TL-01` / `TL-02` / `FIELD_DEFAULTS` | **closed** | all three retired in the r33 SKILL diff, each replaced by live tool line cites (`tools/d2-typed-labels.py:422,:810-814`; `:694-695,:774-775`; `:768-769`; `:500,:549,:565`) plus a dated erratum clause |
| OI-04 — loanword-dating cite cluster | **closed** | `loanword-material-dating.md:26,60` → `:30-31,63`; `:57` → `:59,63` in the r33 diff |
| OI-07 — cold-run N1/N4/N5 errata | **closed** | the r33 SKILL diff adds the "Expected verdicts at HEAD (dated 2026-10-19…)" block for the r5/r6/r7 runners, with the in-place-receipt warning |
| A09 SKILL receipt/anchor owed | **closed** | `anchor-reissue.md` (NEW table, superseded readings re-issued) + `box1-resurvey-durable.json` (durable receipt, SKILL digest `f9bd07c2…` = live) |
| A09 README hard-pin owed | **closed** | `corpus/lessons/README.md` at HEAD is blob `73f3e1bd29d4569ddd2a5d9a2309f4451fa35ae5`, sha256 `f752e1d79ae627a0d9728fe16fd1532e7cb9e587f6ac7025a880d8af46233868` — exactly the values the r33 audit recorded as *uncommitted worktree* state, now committed; `reports/round-34/calib/C09-final-receipt.md:264` records the supersession |
| OI-08 / OI-09 — bilateral read record; L0 digest ratification | **still open, correctly routed** | both lore-owned; `contract-read-record.md` is one-sided by construction |

## Preservation and hazard checks

- **No filed round byte moved by r35 so far.** `git status --porcelain` → only
  `?? reports/round-35/` (untracked round dir). Nothing under `reports/round-1..34/`,
  `corpus/lessons/`, `tools/gates/frozen/` is modified.
- **F-C13-1 respected.** I executed no `run-validation.py`, in-tree or isolated. The
  only instrument run was `receipt_guard_adoption.py --selftest`, which is a lane
  tool, not a filed round runner, and whose writes are confined to a
  `tempfile.TemporaryDirectory(dir=ROOT/".scratch")` (`:1083-1089`).
- **The declared-in-r7 freeze is intact.** All five recorded digests recompute to
  their filed values, and `expected.json`'s self-recorded `packet_sha256` matches
  live `packet.md`. Nothing in round 35 has disturbed the freeze.
- **Language/bleed scan (A04/A08's content, re-derived).** Scanned all ten
  r33/r34 non-report and named report surfaces for `canon|clearance|promotion|
  closure|ownership` outside negations. Every hit is a negation, a `limits` row, or
  a `not_a_promotion_verdict` field: `packet.md` (17 hits — all "not canonized /
  NON-CANON / canon standing is lore's alone / no real-language clearance"),
  `claims-map.md` (8 — same), `expected.json:184` (`limits` row), `repin.json:5,53`,
  `box1-resurvey-durable.json:9`, `contract-read-record.md:9`. The single
  bleed-pattern hit in `receipt_guard_adoption.py:28` is the phrase "Unknowns are
  `could-not-evaluate` rows with a named reason" — no ownership claim.
  **Zero unfiled cross-domain bleed found.**

## Delta — reconciliation with the peers who landed after my dispatch

Between my dispatch and my write, `adj/A05-records.md`, `adj/A06-province.md`,
`adj/A09-receipt.md`, `adj/A11-verify-2.md` and `review/R06-a-review.md` landed.
I read A06 and R06 in full and re-checked their load-bearing claims against my own
readings. Result: **no conflict; one agreement that upgrades my finding, and one
hole that R06 named and I then closed.**

### Agreement (independent double-reading)

- **R7 freeze integrity.** A06 verified four digests (packet, twin, claims-map,
  expected, `A06-province.md` §A06-3(b)) against `freeze.txt`/`repin.json`. I
  independently recomputed **five** (adding `freeze.txt`) against `repin.json`
  rows[2].digests and additionally checked `expected.json`'s self-recorded
  `packet_sha256` against live `packet.md`. Both readings agree; mine is one file
  wider and one relation deeper. **5/5 MATCH, plus self-record MATCH.**
- **PROVINCE accuracy.** A06's `Owns`/`Refuses` verdicts (PASS ×7) and my
  independent re-derivation agree on the load-bearing point: no PROVINCE amendment
  is owed by the r33/r34 landings, and the three new/changed artifacts fall under
  `PROVINCE.md:11`'s owns clause as written.
- **Census.** R06's diff window (`cdd66d7 4a7aede`) is wider than my per-commit
  window and yields 14 out-of-report surfaces to my 12 — R06 adds `LOG.md`,
  `SCORECARD.md` and the pre-baseline `.ufo` deletion. My per-commit census is a
  strict subset of R06's; I adopt R06's 14-surface list as the wider reading.

### A10-F1 upgraded from "stale snapshot" to "intra-round contradiction"

`SCORECARD.md`'s round-34 row states the operability claim's evidence as
"inventory of all **29** filed runners: **18** guarded-refresh / **11**
unguarded-in-place" (`git diff 4a7aede^ 4a7aede -- SCORECARD.md`, the
`| operability | improved (claim O, …)` row). The filed inventory JSON says
**28** / **17** (`adoption-inventory.json`, `runner_count` / `class_counts`), and
the live census at HEAD reads **29** / **18** (`--selftest` →
`live_runner_count: 29`, `live_class_counts {guarded-refresh: 18, unguarded-in-place: 11}`).

So the two round-34 artifacts **contradict each other**, and the SCORECARD — not
the JSON — is the one that matches the tree. This is no longer merely a dated
snapshot: a reader reconciling round 34's own record set gets two different
numbers for the same census, and the JSON is the one that is wrong at HEAD. The
delta remains exactly one row, `reports/round-34/run-validation.py`, which landed
in the same commit that filed the JSON. Severity stays **low** (nothing downstream
consumes the field; the tool re-derives it on every run) but the disposition
tightens: **owner integrator, disposition `record`**, and the assembled audit
should state the count as *29 / 18 / 11 at HEAD, per the SCORECARD row and the live
census*, naming the JSON field as superseded by its own round. Do not edit the
filed JSON.

### Gap closed — the surfaces R06 named that no A-seat owned

R06's `F-R06-1` correctly flagged `corpus/lessons/README.md` as the largest r33
live non-report edit (+130/−28, 448 lines, 33 pinned rows) that the A-claim's
surface list and every A01–A10 mission omit. My own per-surface table had the same
blind spot — I cited its digest as *evidence* for the A09 closure without auditing
it as a *surface*. That hole is now closed, and I extended it to the three other
surfaces R06 lists that no A-seat owns:

| surface | verdict | evidence |
|---|---|---|
| `corpus/lessons/README.md` | **green** | Independent re-derivation of all 33 index rows (parse `^\|\s*\`(corpus/lessons/[^\`]+\.md)\`\s*\|`, recompute sha256[:8] + `splitlines()` per row): 33 rows, 32 non-README files + the self-referential row, **0 files without a row, 0 rows without a file, 0 sha mismatches, 0 defects**. Agrees with R06's checker. Bleed scan: the single hit, `README.md:241` (Q-31-4 "the closure ledger's evidence commands…"), is an ordinary-sense reference to round 31's closure ledger inside a queue row — not a closure assertion. |
| `LOG.md` (r33 +93, r34 +54) | **green** | Both round diffs contain **zero deleted lines** (`git diff <commit>^ <commit> -- LOG.md \| grep -E "^-" \| grep -v "^---"` → empty for both). Append-only discipline holds. |
| `SCORECARD.md` (r33 +29, r34 +31/−3) | **green** | r33 diff is a pure append. The r34 `−3` are a superseded forward-pointer block ("Next: round 34 — loop 1 build 2 of 3…"), replaced by the actual round-34 verdict table — the standard advance-the-pointer pattern, not a rewrite of a filed verdict. No promoted/cleared/closed assertion outside a negation in either diff. |
| `REGIMEN.md` (new, r33) | **green** | Bleed scan: one hit, `:56` "closure ledger showing 42/42 closed" — the regimen's own lane-scoped done-condition. `:62-63` scopes siblings/world-bible/domain trees read-only; `:46` names `.ufo/reports/round-<N>/kotodama.md`, which R06 confirmed resolves at the fleet root. No out-of-lane authority asserted. |

## Owed

The peer fragments that were missing at my dispatch time have since landed
(`A05`, `A06`, `A09`, `A11`, `R06`). Still owed by their own seats, and not by me:

- `reports/round-35/scout/K04-touched-census.md` (census re-derived here and, wider, in R06 §2)
- `reports/round-35/adj/A01-r7-packet.md`, `A02-adoption-tool.md`, `A03-examples.md`,
  `A04-skill-agents.md` (all four surfaces audited here; A05/A06 landed)
- `reports/round-35/adj/A07-verify.md` (independent re-runs; this file and A11 are two)
- `reports/round-35/adj/A08-audit-draft.md` (assembly; the per-surface verdict table above plus the delta table is draftable from this file)
- `reports/round-35/review/R07-a-review.md` (adversarial pass on the PROVINCE leg)

Two live obligations this file creates for the integrator:

1. **A10-F1 must be recorded** — the round-34 adoption census reads 28/17 in
   `op/adoption-inventory.json` but 29/18 in `SCORECARD.md`'s own round-34 row and
   29/18/11 in the live census; owner `integrator`, disposition `record`, JSON
   field superseded, filed bytes untouched.
2. **The R06 F-R06-1 surface must be carried into the assembled audit** — with the
   `corpus/lessons/README.md` green verdict and the independent 33-row re-derivation
   above as its evidence, or recorded as an explicit exclusion with a reason.

## Citations

Commands run (all at HEAD `4a7aede`, `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`):

- `find reports/round-35 -type f | sort` — peer-fragment absence
- `git diff --name-status da68a6d^ da68a6d` / `git diff --name-status 4a7aede^ 4a7aede`
- `git show --stat --oneline da68a6d` / `4a7aede`
- `git diff da68a6d^ da68a6d -- AGENTS.md examples/ SKILL.md corpus/knowledge/linguistics/register-lexicon-ceilings.md`
- `for p in linguistics myth-symbol culture-material synthesis verification civilizations; do ls corpus/knowledge/$p/*.md | wc -l; done` → 21/19/18/29/20/94 = 201
- `sha256sum corpus/knowledge/synthesis/worldbible-integration-contract.md` → `5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069`
- `sha256sum SKILL.md` → `f9bd07c2bd13462367be20e8d775cec1c5569eb2e575dc5d078519ecc72e5a9b`; `wc -l SKILL.md` → 732
- `sha256sum corpus/lessons/README.md` → `f752e1d79ae627a0d9728fe16fd1532e7cb9e587f6ac7025a880d8af46233868`; `git rev-parse HEAD:corpus/lessons/README.md` → `73f3e1bd…`
- `wc -l AGENTS.md` → 40; `grep -c '^\`\`\`' AGENTS.md` → 0
- `python3 -B tools/harness/receipt_guard_adoption.py --selftest` → `controls_passed: 38`, `controls_total: 38`, `selftest_passed: true`, `live_runner_count: 29`, `live_class_counts {guarded-refresh: 18, unguarded-in-place: 11}`, exit 0
- `ls reports/round-*/run-validation.py | wc -l` → 29
- digest recomputation of the five r7 freeze files against `repin.json` rows[2].digests → 5/5 MATCH
- `git status --porcelain` → `?? reports/round-35/`
- `grep -rl '/home/vgpnk/Projects/shokunin/kotodama-shokunin' reports/ --include=*.json | wc -l` → 173
- `grep -nEi "\b(canon|clearance|promot|closure|ownership)\b" corpus/lessons/README.md` → 1 hit (`:241`, ordinary-sense "closure ledger" in queue row Q-31-4)
- `python3 -c` README index re-derivation (parse `^\|\s*\`(corpus/lessons/[^\`]+\.md)\`\s*\|`, recompute sha256[:8] + `splitlines()` per row) → 33 rows, 0 files without a row, 0 rows without a file, 0 sha mismatches, 0 defects
- `git diff <commit>^ <commit> -- LOG.md | grep -E "^-" | grep -v "^---"` → empty for both `da68a6d` and `4a7aede` (pure append)
- `git diff da68a6d^ da68a6d -- SCORECARD.md | grep -E "^-"` → empty (pure append); `git diff 4a7aede^ 4a7aede -- SCORECARD.md | grep -E "^-"` → the 3 superseded forward-pointer lines, replaced by the round-34 verdict table
- `grep -nEi "\b(canon|clearance|promot|closure|ownership)\b" REGIMEN.md` → 1 hit (`:56`, lane-scoped done-condition)
- `git diff 4a7aede^ 4a7aede -- SCORECARD.md` → the operability row reading "inventory of all 29 filed runners: 18 guarded-refresh / 11 unguarded-in-place"

Files cited:

- `PROVINCE.md:10,11,16-20,22-25`
- `SKILL.md:128,517,518`; `SKILL.md` at 732 lines / `f9bd07c2…`
- `AGENTS.md` at 40 lines, 0 fences
- `corpus/knowledge/linguistics/register-lexicon-ceilings.md` (r33 diff, additive after :287)
- `corpus/knowledge/verification/gate-frozen-run-standard.md:9` (+ its `verified-at` line)
- `corpus/lessons/round-9.md:142`
- `examples/culture-d3/README.md:104`; `examples/culture-d3/handoff.md:27,74`; `examples/culture-d3/expected.json:4`; `examples/handoff-packet.sample.md:21`; `examples/handoff-packet.sample.yml:45,78`
- `reports/round-34/handoff/declared-in-r7/packet.md:7`; `claims-map.md`; `expected.json:184`; `freeze.txt`
- `reports/round-34/handoff/repin.json:5,53` (+ `rows[2].digests`, `named_findings[0]` R34-N1)
- `reports/round-34/op/adoption-inventory.json:109` (+ `runner_count`, `class_counts`)
- `reports/round-34/craft/box1-resurvey-durable.json:9` (+ `skill_lines`, `skill_sha256`)
- `reports/round-34/craft/anchor-reissue.md:6,10,35,216`
- `reports/round-34/calib/C09-final-receipt.md:264`
- `reports/round-33/adj/contract-read-record.md:9`
- `reports/round-33/calib/open-items-ledger.json` (OI-01…OI-12)
- `reports/round-33/adj/audit-assembled.md`
- `tools/harness/receipt_guard_adoption.py:22-23,28,1029-1034,1083-1089`
- `tools/gates/frozen/**` (unmodified; carried only as preservation evidence)
- `corpus/lessons/README.md:241` (+ the 33-row index, re-derived; 448 lines / `f752e1d7…` / blob `73f3e1bd…`)
- `LOG.md` (r33 +93, r34 +54 — both pure appends)
- `SCORECARD.md` (r33 +29 pure append; r34 +31/−3, the −3 a superseded forward-pointer; its round-34 operability row carries the 29 / 18 / 11 census)
- `REGIMEN.md:46,56,62-63` (lane-scoped done-condition and read-only sibling scope)
- Peer fragments read for reconciliation: `reports/round-35/adj/A06-province.md` (§A06-2, §A06-3(b)), `reports/round-35/review/R06-a-review.md` (§2 census, F-R06-1, F-R06-4)
