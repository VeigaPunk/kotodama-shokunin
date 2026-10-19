- Seat: A06 | executor | claim A | date 2026-10-19 | baseline 4a7aede

# A06 — PROVINCE accuracy re-verification at HEAD

**Assignment (`reports/round-35/targets.json`, seat A06):** "PROVINCE accuracy
re-verification at HEAD: owns/refuses lists vs the tree (new tool, r7 packet,
repointed renderer all in-lane; refuses-list siblings unchanged)."

**Snapshot:** `date -u '+%Y-%m-%dT%H:%M:%SZ'` → `2026-10-19T08:17:02Z`;
`git rev-parse HEAD` → `4a7aede22cd8395b01ce6dd9f46bcae364ca24e4` (== the
declared baseline, `reports/round-35/claims.json:8-9`); `git status
--porcelain` → only `?? reports/round-35/` (clean tree, no seat write outside
this round). All commands read-only, lane root.

**Scope note:** this leg re-runs the r33-A01 province check
(`reports/round-33/adj/A01-province.md`) at the new HEAD and adds the three
surfaces rounds 33/34 created or edited. It does not re-adjudicate the r33
bleed audit; that is the other claim-A seats' leg.

## Check A06-1 — `PROVINCE.md` itself: byte-stable, no edit owed by r33/r34 — PASS

| probe | command | result |
|---|---|---|
| blob identity | `git rev-parse HEAD:PROVINCE.md` | `313b182f251564b7997b06996b4f063370778f11` (== r33-A01's reading at `139e3b6`) |
| no drift | `git diff --stat c53782a HEAD -- PROVINCE.md` | empty (exit 0) |
| live bytes | `sha256sum PROVINCE.md`; `wc -l -c PROVINCE.md` | `05b34a579c5d4f4ec78957cdedb658246ff292df3e21181c66186403f2b942d6`; 31 lines, 1636 bytes |
| last touch | `git log --oneline -- PROVINCE.md` | only `c53782a` (supplement-opencode-1) and `a527120` (mint) |

Rounds 33 and 34 did not touch it: `git show --stat da68a6d` lists `AGENTS.md`
and `SKILL.md` but not `PROVINCE.md`; `git show --stat 4a7aede -- tools/
examples/ SKILL.md AGENTS.md PROVINCE.md corpus/` lists only
`tools/exercise-handoff-e2e.py` and `tools/harness/receipt_guard_adoption.py`.

## Check A06-2 — `Owns` list vs the live tree at HEAD — PASS

`PROVINCE.md:9-14` owns "the generative/coupling craft and its records in this
repo (`corpus/knowledge/{linguistics,myth-symbol,culture-material,synthesis,verification,civilizations}`),
this lane's own gates, source-check records, non-canon examples and reports."

| claim | live measurement at HEAD | verdict |
|---|---|---|
| six named partitions | `find corpus/knowledge -maxdepth 1 -mindepth 1 -type d` → exactly those six | PASS |
| partitions populated | md counts: linguistics 21, myth-symbol 19, culture-material 18, synthesis 29, verification 20, civilizations 94 = **201** (== the claim-C before-state, `reports/round-35/claims.json:26-27`) | PASS |
| own gates | `ls tools/gates/` → 12 gate scripts + `frozen/` + `expected/` + `fixtures/` | PASS |
| source-check records | `corpus/lessons/` present incl. `round-{5,6,7}-sources/`, `supplement-opencode-1/sources/` | PASS |
| non-canon examples | `ls examples/` → `culture-d2/`, `culture-d3/`, `culture-d4/`, `supplement-opencode-1/`, `handoff-packet.sample.{md,yml}`; 7 files carry explicit non-canon stamps (`examples/culture-d2/ASSEMBLY.md`, `culture-d3/handoff.md`, `culture-d3/README.md`, `culture-d4/ASSEMBLY.md`, `culture-d4/brief.md`, `culture-d4/README.md`, `handoff-packet.sample.md`) | PASS |
| reports | `ls -d reports/round-*` → 31 round dirs (rounds 1-34 filed, round 35 live) | PASS |
| verification/civilizations caveat | `PROVINCE.md:12-14` limits those partitions to linguistic-cultural coupling; the contract repeats the split at `corpus/knowledge/synthesis/worldbible-integration-contract.md:17` ("Kotodama owns generative craft and its reproducible design records; lore owns world-bible entities … canon decisions") | PASS |

## Check A06-3 — the three new/changed surfaces are in-lane — PASS

### (a) New tool `tools/harness/receipt_guard_adoption.py` — in-lane

- Origin: added by `4a7aede` (round-34 claim O, "land
  tools/harness/receipt_guard_adoption.py", `reports/round-34/claims.json`);
  1309 lines; `sha256sum` → `5858abcd0261e8176ebb285db6d80a7c36185d9a12895b4b43b75710db036544`.
- Reads/writes only in-lane roots: `receipt_guard_adoption.py:59-63` —
  `GUARD_TOOL = "tools/harness/receipt_guard.py"`,
  `RUNNER_GLOB = "reports/round-*/run-validation.py"`,
  `SWEEP_ROOTS = ("reports", "tools")`.
- Zero out-of-province content: `grep -nEi 'canon|promot|clearance|lore-shokunin|fleet'`
  → no matches; `grep -nE '/home/|\.\./\.\./|Projects/shokunin/[a-z]'` → no matches.
- Discipline statements in the tool itself: docstring `:26-29` — "this tool
  never executes a runner, never writes into a filed round … Unknowns are
  `could-not-evaluate` rows with a named reason". Selftest fixtures materialize
  only inside a temp dir (`:1084-1086`, `tempfile.TemporaryDirectory(prefix="rga-", dir=scratch)`),
  so the `reports/round-41|49|51/…` strings at `:1023-1045` never reach the
  real repo.
- Ownership reading: it is the same class of lane harness as
  `tools/harness/receipt_guard.py` (added round-14, commit `b02cfbc`), already
  accepted lane tooling; `PROVINCE.md:9-11`'s "this lane's own gates … and
  reports" covers it under the same reading r33-A01 applied to `tools/gates/`.
  It makes no new ownership claim.

### (b) r7 packet `reports/round-34/handoff/declared-in-r7/` — in-lane

- Authored by this lane as producer and routed to lore: `packet.md:15`
  "producer | kotodama-shokunin (round-20 handoff-e2e exercise v3; generative
  craft and design records only)", `:16` "recipient | lore-shokunin (canon,
  world-bible entities, chronology, bible-wide consistency)".
- Non-canon, canon routed not absorbed: `packet.md:1` "not canonized",
  `:3` "NON-CANON handoff packet … no canon standing is asserted here. Canon
  standing is lore's alone (contract §6, §8.7). All native spellings are
  constructed and unscreened ASCII lowercase; no real-language clearance,
  community consultation, or cultural permission is claimed, performed, or
  granted", `:7` "canon_standing: not canonized — lore disposition required".
  `claims-map.md:22` "…clearance or canon standing is claimed by any row";
  `:60` "canon standing is not its to give".
- Read set is entirely in-lane: manifest rows cover `examples/` (32),
  `tools/` (12), `reports/` (9), `corpus/` (5); `grep -nE '/home/|\.\./'` on
  `packet.md` → no matches. It follows the contract's §4 envelope and names
  `corpus/knowledge/synthesis/worldbible-integration-contract.md` as
  authority (`packet.md:14,39`).
- Freeze integrity at HEAD (no re-freeze this round — the r35 non-goal):
  `sha256sum` packet `45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19`,
  twin `0e22913850cd85bc393fe6d0d7a8bf448e9b253aa2884457d4c8999ac9096599`,
  claims-map `d181de28ccafda2d34e40277a5390f7e42c64247fbbdcdec3df9a592aa48980c`,
  expected `bbe15887b710bb36def5e1c82fa5b1c1ef37df3cb5581c7c2982a0498e829d55`
  — all four equal `freeze.txt` / `repin.json` R34-D-new-row digests.
  `run.log` in the same dir is gitignored (`.gitignore:3` `*.log`) and outside
  the pinned digest set; noted, not a defect.
- Note (no owner): authoring a handoff packet is the lane's owned craft
  (`PROVINCE.md:9-11`); accepting it would be lore's, and nothing here claims
  acceptance.

### (c) Repointed renderer `tools/exercise-handoff-e2e.py` — in-lane

- Repoint sites verified in the `4a7aede` diff (21 lines changed total):
  `:184` `CLAIMS_MAP = "reports/round-34/handoff/declared-in-r7/claims-map.md"`;
  `:1933-1934` `V3_BASELINE_DEFAULT` / `V3_FROZEN_DIR_DEFAULT` → the r7 pair
  (both lines together); `:2290` docstring, `:2566` artifact-manifest
  description, `:2779` scope cell (twelve → thirteen components),
  `:3521-3531` OQ-V3-05 reworded to live numbers. Live bytes:
  `sha256sum` → `34c85f5773fb1925ff7d454f873a2e88fa8246af10c6830468041dd44452eea9`
  (== `repin.json` R34-D-default-pointer `surface_sha256_after`).
- All repointed targets are in-lane (`reports/round-34/…`); `grep -nE
  '/home/vgpnk|Projects/shokunin/(lore|chousa|kake|kotoba|game-dev)'` → no
  matches; writes land only under in-lane `reports/round-*` surfaces and
  isolated temp dirs.
- The refusal boundary is enforced in-tool, not merely asserted:
  `CANON_MARKER_RE` `:228`, `CANON_TRAP_RES` `:229-235` (traps
  "certify/grant/award … canon", "canonized by lore", etc.), limits line `:485`
  "pins computational inputs only; not lore acceptance, not canon".
- Verdict: in-lane; the round-34 edit added no out-of-province surface.

## Check A06-4 — `Refuses` list vs the siblings at HEAD — PASS (unchanged)

`PROVINCE.md:16-20` refuses six matters. Each named sibling still resolves to a
live lane whose province matches the refusal label:

| refusal (`PROVINCE.md:16-20`) | sibling at HEAD | evidence |
|---|---|---|
| canon — "that is lore-shokunin" | `lore-shokunin/` (roster id `lore`) | `lore-shokunin/PROVINCE.md:3` "Owns: fictional-world records … with consistency verification"; `:10` refuses "claiming canon without an in-world citation" |
| real-world rights/attribution rulings | `lore-shokunin/` also refuses "real-world rights claims (art-east-asian-design)" (`PROVINCE.md:10`) — non-overlapping refusals, consistent | same |
| game mechanics (game-dev-2d/3d) | `game-dev-2d-shokunin/`, `game-dev-3d-shokunin/`; roster ids are exactly `game-dev-2d` / `game-dev-3d` | `game-dev-2d-shokunin/PROVINCE.md:3` "2D game production verified by executable headless fixtures — loop, input, physics …"; `game-dev-3d-shokunin/PROVINCE.md:3-4` "3D game production … 3D movement and collision …" |
| general source-research method (chousa) | `chousa-shokunin/` | `chousa-shokunin/PROVINCE.md:3` "**Domain:** deep-research method (調査) — the reusable craft of source research."; `MANIFEST.json:2312` mint note: "the general source-research method is unowned [by other lanes]" |
| web publishing (kake) | `kake-shokunin/` (roster id `kake`) | `kake-shokunin/PROVINCE.md:3` "**Domain:** web properties & publishing"; `MANIFEST.json` roster `{"id": "kake", "domain": "web properties & publishing"}` |
| prompt/skill craft (kotoba) | `kotoba-shokunin/` (roster id `kotoba`) | `kotoba-shokunin/PROVINCE.md:3` "**Domain:** prompt & skill craft"; roster row `{"id": "kotoba", "domain": "prompt & skill craft"}` |

Corroboration that the routing was correct at mint time and is unchanged:
`MANIFEST.json:2888-2890` (kotodama mint entry) — "lore records/verifies canon
(complementary handoff recipient, not the generative craft); kotoba is
prompt/skill craft; chousa is research method only; production/host lanes
refuse narrative canon or have no scope." No sibling was renamed, retired, or
added to this list since `c53782a` in a way that changes these labels.

Newly observed at HEAD, no PROVINCE defect: the fleet roster has **no kotodama
row** ("Probation >=3 verified rounds; roster row withheld", `MANIFEST.json:2890`)
— consistent with `PROVINCE.md:27` "Only writes this standalone lane
repository (`kotodama-shokunin/`)". Also no in-lane artifact among the three
surfaces decides a refused matter (see A06-3 greps); the r7 packet's own
clearance sentences disclaim rather than rule.

## Check A06-5 — write-scope statement vs observed surfaces — PASS

`PROVINCE.md:27-29`: "Only writes this standalone lane repository
(`kotodama-shokunin/`), its own fleet round reports, and allowed append-only
L0 questions."

- lane repo: rounds 33/34 artifacts and this fragment — in-lane.
- fleet round reports: `/home/vgpnk/Projects/shokunin/.ufo/reports/round-34/`
  contains `kotodama.md` (round-34 filed); `.ufo/reports/round-35/` not yet
  present — expected, filed at round close by the integrator.
- L0 questions: `.ufo/l0-questions.md` (50 lines) carries exactly 4 kotodama
  rows, lines 44-47 (rounds 2, 8, 9, 11) — append-only surface, untouched by
  this seat.
- this seat's only write: `reports/round-35/adj/A06-province.md`.

## Verdict table

| check | verdict | basis |
|---|---|---|
| A06-1 `PROVINCE.md` byte-stable, untouched by r33/r34 | **PASS** | blob `313b182f…` at HEAD == `c53782a`; empty diff; 31 lines / 1636 bytes |
| A06-2 `Owns` list accurate at HEAD | **PASS** | six partitions (21/19/18/29/20/94 = 201), gates, source records, non-canon examples, reports all live |
| A06-3 new tool in-lane | **PASS** | in-lane roots only; zero canon/lore/fleet/cross-repo refs; same harness class as round-14 `receipt_guard.py` |
| A06-3 r7 packet in-lane | **PASS** | producer kotodama / recipient lore; NON-CANON stamps; canon routed; in-lane read set; digests equal freeze.txt (no re-freeze) |
| A06-3 repointed renderer in-lane | **PASS** | repoints to in-lane r7 pair; in-tool canon traps; no cross-repo refs |
| A06-4 `Refuses` list accurate, siblings unchanged | **PASS** | all six named siblings exist with matching provinces; no absorbed refusal in the new surfaces |
| A06-5 write-scope statement accurate | **PASS** | fleet r34 report present; 4 L0 rows; no out-of-lane write by this seat |

**Net: `PROVINCE.md` needs no edit at HEAD.** No scope drift and no absorbed
out-of-province matter found on the three round-33/34 surfaces or in the
refuses-list routing.

## Limits / to-verify

- Not re-run here (other seats' legs): the full bleed/cross-domain audit of all
  r33/r34 artifacts (claim A's other seats), the renderer gate chain and
  selftest (claim O), and the corpus census reconciliation (claim C).
- The `chousa-shokunin` refusal label was verified against the sibling
  directory and its `PROVINCE.md` only; chousa carries no fleet roster row at
  HEAD (`MANIFEST.json:2890` notes probation), so its lane status is
  `to-verify` at the fleet level — the PROVINCE reference itself resolves.
- `corpus/README.md` census prose is stale at HEAD (`:44`, `:56-57`, `:90-91`
  read 19/20 for linguistics vs the live 21) — already filed by r33-A01 and
  owned by claim C's README reconciliation this round; not a PROVINCE defect.
- `run.log` inside `declared-in-r7/` is untracked by design (`.gitignore:3`);
  digest-pinned integrity rests on the five tracked files, all verified equal.

## Owed: none

## Citations

- `PROVINCE.md:1-31` (read in full; owns :9-14, refuses :16-20, adjacent :22-25, write scope :27-29)
- `reports/round-35/claims.json:8-9` (baseline commit), `:26-27` (partition census before-state)
- `reports/round-35/targets.json` (seat A06 mission), `shared_rules`
- `reports/round-33/adj/A01-province.md:1-198` (prior province check at `139e3b6`)
- `reports/round-34/claims.json` (claim O tool origin), `reports/round-34/handoff/repin.json` (R34-D rows, digests, named findings R34-N1/N2)
- `reports/round-34/handoff/declared-in-r7/{freeze.txt,packet.md:1,3,7,14-20,39,claims-map.md:22,56-62,expected.json,twin.json}`
- `tools/harness/receipt_guard_adoption.py:1-39,59-63,1023-1045,1084-1086`; `tools/harness/receipt_guard.py` (round-14 origin, `b02cfbc`)
- `tools/exercise-handoff-e2e.py:184,228-235,485,1933-1934,2290,2566,2779,3521-3531`
- `corpus/knowledge/synthesis/worldbible-integration-contract.md:1-70` (§1 ownership split `:17`, §4 envelope, §9)
- Siblings (read-only): `lore-shokunin/PROVINCE.md:3,10`; `chousa-shokunin/PROVINCE.md:3`; `kake-shokunin/PROVINCE.md:3`; `kotoba-shokunin/PROVINCE.md:3`; `game-dev-2d-shokunin/PROVINCE.md:3`; `game-dev-3d-shokunin/PROVINCE.md:3-4`
- `/home/vgpnk/Projects/shokunin/MANIFEST.json` roster rows (`lore`, `kake`, `kotoba`, `game-dev-2d`, `game-dev-3d`) and kotodama/chousa mint notes at `:2888-2890`, `:2312`
- `/home/vgpnk/Projects/shokunin/.ufo/reports/round-34/kotodama.md` (present); `/home/vgpnk/Projects/shokunin/.ufo/l0-questions.md:44-47` (4 kotodama rows)
- Commands (lane root, snapshot `2026-10-19T08:17:02Z`, HEAD `4a7aede`):
  - `git rev-parse HEAD`; `git status --porcelain`; `git rev-parse HEAD:PROVINCE.md`; `git diff --stat c53782a HEAD -- PROVINCE.md` (empty); `git log --oneline -- PROVINCE.md`; `sha256sum PROVINCE.md`; `wc -l -c PROVINCE.md` (31/1636)
  - `git show --stat --oneline 4a7aede`; `git show --stat 4a7aede -- tools/ examples/ SKILL.md AGENTS.md PROVINCE.md corpus/`; `git show 4a7aede -- tools/exercise-handoff-e2e.py`
  - `git log --diff-filter=A --format='%h %ad %s' --date=short -- tools/harness/{receipt_guard_adoption,receipt_guard}.py`
  - `find corpus/knowledge -maxdepth 1 -mindepth 1 -type d`; per-partition `ls corpus/knowledge/$p/*.md | wc -l` (21/19/18/29/20/94)
  - `ls tools/gates/` (12 scripts + frozen/expected/fixtures); `ls tools/harness/`; `ls examples/`; `ls -d reports/round-* | wc -l` (31); `git ls-files reports/round-34/handoff/`; `git ls-files tools/harness/`
  - `sha256sum reports/round-34/handoff/declared-in-r7/{packet.md,twin.json,claims-map.md,expected.json}`; `sha256sum tools/exercise-handoff-e2e.py tools/harness/receipt_guard_adoption.py`
  - `grep -nEi 'canon|promot|clearance|lore-shokunin|fleet' tools/harness/receipt_guard_adoption.py` (no matches); `grep -nE '/home/|\.\./\.\./' …` (no matches); same pair over `tools/exercise-handoff-e2e.py` and `reports/round-34/handoff/declared-in-r7/packet.md`
  - `grep -nEi 'canon|lore disposition|clearance|promotion' reports/round-34/handoff/declared-in-r7/claims-map.md`; `grep -cEi 'non-canon|not canonized|lore' packet.md` (25)
  - `git check-ignore -v reports/round-34/handoff/declared-in-r7/run.log` → `.gitignore:3:*.log`
  - `grep -oE '\| [A-Z]-[0-9]+ \| [^ |]+' packet.md | … | cut -d/ -f1 | sort | uniq -c` (examples 32 / tools 12 / reports 9 / corpus 5)
  - `for d in lore-shokunin chousa-shokunin kake-shokunin kotoba-shokunin game-dev-2d-shokunin game-dev-3d-shokunin; do grep -nE '^\*\*(Domain|Owns|Refuses)' -A2 $d/PROVINCE.md; done`
  - `grep -c -i kotodama /home/vgpnk/Projects/shokunin/MANIFEST.json` (84); `ls /home/vgpnk/Projects/shokunin/.ufo/reports/round-34/`; `grep -n -i kotodama /home/vgpnk/Projects/shokunin/.ufo/l0-questions.md` (44-47); `wc -l` (50)
  - `date -u '+%Y-%m-%dT%H:%M:%SZ'` → `2026-10-19T08:17:02Z`
