# MutLandedC — wave-2 FALSIFY, claim-C landed bytes, mutation sweep (kotodama round 73, hyaku run 7)

Seat: MutLandedC (leaf). Scope: attack the landed claim-C bytes at lands `0316b8883b4f8d44b8efd720140e7f52f734a102`
(base `8841ad3b896a0227674fa0725b818c999118046f`) by applying one mutation at a time in a throwaway clone and
grading each with the frozen counter `reports/round-73/accept-c.py --root . --lands <mutant>`.

## Verdict up front

- 22 mutants graded (all 20 ticketed + 2 companions), **19 killed, 3 survived**. The landed claim-C bytes are
  NOT shown false by any mutant; the three survivors are **counter-coverage gaps**, not proof the claim is wrong.
- Survivors: **M10** (reject-row URL check skips every "not adopted" row), **M11** (reason/flip enforced only as
  word presence), **M17** (guard-proof satisfied by fixture debris; 4-space control unchecked). Each is a
  MAJOR coverage finding against the claims.json leg wording. No BLOCKER found.
- Lane working tree untouched except this Report file; all mutations lived in `/tmp/MutLandedC/clone.VAYZpWqx`.

## Environment and honesty notes

- Clone (per tasking): `D=$(mktemp -d /tmp/MutLandedC/clone.XXXXXXXX)`, `git -C "$D" init -q`,
  `git clone -q <lane> "$D/lane"`, `git -C "$D/lane" checkout -q --detach 0316b888…`.
  Verified `git -C "$D" rev-parse --show-toplevel` = `/tmp/MutLandedC/clone.VAYZpWqx` and
  `git -C "$D/lane" …` = `…/lane` before the first commit. Every mutant commit made with
  `-c user.name=mut -c user.email=mut@mut.invalid` on branch `mut-NN` inside `$D/lane` only.
- **Environment fix (declared):** first pristine run printed `ACCEPT-C-73: FAIL legs=10/11` with only CENSUS red —
  `census script not found: /tmp/.../scripts/sources-census.sh` (the counter defaults fleet-root to the clone
  parent). I copied the fleet's script: `cp /home/vgpnk/Projects/shokunin/scripts/sources-census.sh "$D/scripts/"`.
  This is a /tmp write; the fleet repo and lane were not touched. After the copy the pristine run is the
  counter's intended environment. All 22 mutants were graded under the fixed environment.
- **Baseline (pristine):** `ACCEPT-C-73: PASS legs=11/11`, counter self-sha256
  `95aee88166023f4b0dc78cda5f0f3a769e94de476f5558bd6e33650922fea416`, lands tree `9b10fa06a2d3756c…`,
  receipt header `stamped = evaluated = measured (lane main) = 0316b888…`.
- **Restoration evidence:** after every mutant: `git checkout -q --detach 0316b888… && git clean -fdq`
  then `rev-parse HEAD` = `0316b8883b4f8d44b8efd720140e7f52f734a102`, `status --porcelain | wc -l` = `0`,
  and a restored-bytes detector re-run printing `ACCEPT-C-73: PASS legs=11/11` — recorded 22/22 times
  (log line `restored-head=… dirty=0` in every run). Final clone state: detached at lands, clean,
  branches `mut-01…mut-20, mut-10b, mut-17b` retained as evidence.
- Lane check: tracked tree clean at `0316b888…`; the only `status --porcelain` entries are the orchestrator's
  untracked wave-2 scaffolding (`build-w2.py`, `w2.ready*`, `w2/`) — none of them mine.
- Tooling: **nothing installed** (python3/git/bash already present); pacman not used. No downloads; no live-web
  fetches (byte-level attack only).

## Mutation table

Legend: expected = leg the claims.json leg text implies should redden; observed = legs red under the frozen
counter; survivor = mutant stayed `PASS legs=11/11`.

| # | mutant (bytes changed at lands) | expected leg | observed legs red | survivor? |
|---|---|---|---|---|
| M01 | S876 row status `mined`→`queued` | ROWS | ROWS | no |
| M02 | S880 used-by cell → `—` | ROWS | ROWS | no |
| M03 | S878/S879 live source URLs swapped | ROWS, REPOINTED | ROWS, REPOINTED, GATE | no |
| M04 | S879 opened `2026-10-25`→`2026-10-23` | ROWS | ROWS | no |
| M05 | literal pipe inside S876 teaches cell | ROWS, CENSUS | ROWS, CENSUS | no |
| M06 | delete `reports/round-73/evidence/S877.txt` | EVIDENCE | EVIDENCE | no |
| M07 | S877 evidence quote one word (`называют`→`именуют`) | EVIDENCE | ROWS, EVIDENCE | no |
| M08 | S877 `quote-found-verbatim: yes`→`no` | EVIDENCE | EVIDENCE | no |
| M09 | S879 Gate row verdict `admitted`→`dropped` (no admit row for S879) | GATE | GATE | no |
| M10 | S915 reject row probed-URL cell emptied | GATE | — | **YES** |
| M10b | S894 *refused* row probed-URLs emptied (companion) | GATE | GATE | no |
| M11 | S869 reject row reason+flip cells emptied to `—` | GATE, REJECTS | — | **YES** |
| M12 | campaign id `(cf. S728)` planted in base entry §2 | REPOINTED | REPOINTED | no |
| M13 | inline `(S875)` citation added in base entry §9 | REPOINTED | REPOINTED | no |
| M14 | first `source:` line split to two ids (`S876 S877`) | REPOINTED | REPOINTED, CITEDLINES | no |
| M15 | amend entry body emptied (header kept) | ENTRIES | ENTRIES | no |
| M16 | regenerated map `"S901": "S880"`→`"S901": "S881"` | COLLCHECK | COLLCHECK | no |
| M17 | delete `guard-proof/guard-proof.txt` | COLLCHECK | — | **YES** |
| M17b | M17 + delete `guard-proof/mirror{,-a3}` fixtures (companion) | COLLCHECK | COLLCHECK | no |
| M18 | round-71 stale map `"next_free": "S874"`→`"S875"` | COLLCHECK | COLLCHECK | no |
| M19 | claims.json `row_set` narrowed to S876..S879 | ROWS | ROWS | no |
| M20 | registry append reverted (`git checkout <base> -- corpus/SOURCES.md`) | ROWS, REPOINTED | ROWS, REPOINTED | no |

Mutant commits (all in `/tmp/MutLandedC/clone.VAYZpWqx/lane`, branch per mutant):
M01 `25332b6e8c9b…`, M02 `ec97b85872ee…`, M03 `77f512850f20…`, M04 `3b81af615c73…`, M05 `e091632c2433…`,
M06 `17625e0c39f1…`, M07 `a2105594b027…`, M08 `843e1b53e494…`, M09 `22173070b636…`, M10 `a459290b73f6…`,
M10b `98150437bd3d…`, M11 `d567077404fe…`, M12 `ba952995074d…`, M13 `4889ee05f108…`, M14 `33d0f33f129f…`,
M15 `2dd051ba8c7a…`, M16 `85be4e406385…`, M17 `452eb75bbeec…`, M17b `62993a1a1be1…`, M18 `74ded5841490…`,
M19 `094c26a889df…`, M20 `b3aefc4fef2d…`.

Reproduce any row: `git -C /tmp/MutLandedC/clone.VAYZpWqx/lane checkout -q <mutant-commit> && cd …/lane && python3 -B reports/round-73/accept-c.py --root . --lands <mutant-commit>` (with the census script copied to the clone parent as declared above; restore with `git checkout -q --detach 0316b888… && git clean -fdq`).

## Survivors — what the leg should have checked

### M10 — reject-row URL check ignores every "not adopted" row (MAJOR)

Mutant: the S915 refuse-table row's `probed URLs` cell emptied. Output: `ACCEPT-C-73: PASS legs=11/11` (all legs green).

Cause (accept-c.py `is_reject_row`): a Gate table row counts as a reject row only if its verdict cell contains
`rejected` or `refused`. The refuse table's four `not adopted` rows (S909/S910, S915, S929/S930, S920/S922/S923)
are classified as neither admit nor reject, so GATE's per-row checks (`reject row records no probed URL`,
`names no staged entry or row`) never run on them. Companion M10b proves the check itself works once the
classifier fires: emptying the S894 row's URLs (verdict `refused`) → `LEG FAIL GATE`.
The claims GATE leg says "every reject row carries its probed URL, reason and flip" — as enforced, 4 of the 6
refuse-table rows are exempt. What the leg should check: classify every row of the refuse table (e.g. verdict in
{refused, rejected, not adopted}) or key the per-row checks off the table's header/columns, not verdict substrings.

### M11 — reason/flip enforced only as word presence (MAJOR)

Mutant: the S869 row (verdict `refused`, i.e. a classified reject row) had BOTH its reason cell and flip cell
replaced with `—`. Output: `ACCEPT-C-73: PASS legs=11/11`.

Cause: GATE ends with `if "reason" not in low or "flip" not in low` over the Gate section, and REJECTS does the
same over the whole lesson — the substrings `reason`/`flip` still occur in the table header (`| reason | flip |`),
the prose "(reason + flip; every row names the probed URL…)" and "Tier reasons recorded:" … so a reject row
carrying no reason and no flip at all passes. The claims kill_rule "any correction …" and the GATE leg's
"every reject row carries … reason and flip" are enforced as vocabulary, not per-row content. What the leg should
check: for each classified reject row, the reason and flip cells are non-empty and not `—`/placeholder.

### M17 — guard-proof leg satisfied by fixture debris; 4-space control unchecked (MAJOR)

Mutant: delete `guard-proof/guard-proof.txt` — the file the renumber map names as the proof
(`GUARD-PROOF: PASS; planted 2-space-indented | S881 | row: control sees 0, guard sees 1, census-valid exit 0`).
Output: `ACCEPT-C-73: PASS legs=11/11`.

Cause: COLLCHECK's guard search scans *every* file under `guard-proof/` for (indented `| S<id> |` row +
"collision" + a detection marker). Two fixture corpora backfill it — verified by predicate re-run:
`SATISFIES: mirror-a3/corpus/SOURCES.md planted: ['S881']` and `mirror/corpus/SOURCES.md planted: ['S881']`.
Companion M17b (guard-proof.txt + both mirror dirs removed) → `LEG FAIL COLLCHECK`, so the leg only detects
total absence. Additionally, the claims sentence "a planted 1-3-space-indented collision found **and a 4-space
one not found**" is half-enforced: no leg checks the 4-space control (not-found) side at all. What the leg should
check: pin the proof to the named file (or require the marker in a `guard-proof.txt`), and require evidence of
the 4-space negative control.

## Minor observations (killed mutants that exposed weak spots)

- M06: with `evidence/S877.txt` deleted, ROWS stays green because its "evidence quote inside the anchor cell"
  check is skipped when the evidence file is missing (`if ev is not None`); EVIDENCE catches the absence, so net
  coverage holds — but the ROWS half of the claim degrades to vacuous on exactly the defect it names.
- M20: with the registry append reverted, GATE and EVIDENCE stay green — when a cited row is missing from the
  registry, GATE's URL check degrades to "the Gate row contains any URL". ROWS+REPOINTED catch the revert.
- M03: CENSUS stayed green after the S878/S879 URL swap (no E04 duplicate-URL finding); the row-level legs
  (ROWS/REPOINTED/GATE) carry the detection.

## What I could NOT check

- Live-source truth: I did not re-fetch any URL or re-verify quotes against the actual pages/PDFs — this seat
  attacks landed bytes and counter coverage only; reachability/quote fidelity was wave-1 scouts' ground.
- `accept-c.py --selftest` (29 fixture scenarios) was not re-run; the ticket asked for the landed-bytes sweep.
- CENSUS could only be exercised after copying the fleet census script into the clone parent (declared above);
  in a bare clone parent without that copy, CENSUS is environment-red for pristine AND mutants alike.
- Claim Ca bytes (ledger.json, SCORECARD corrections, accept-ca.py) are outside this seat's item; not attacked.
- Whether any *other* wave-2 seat's report lands in `w2/` alongside mine; I read no sibling reports.

## Bounds compliance

- Writes: `/tmp/MutLandedC/**` (clone + runner script) and this Report file only. No writes under
  `/home/vgpnk/Projects/shokunin/**` except this file; no writes to shokuknow; no pacman; no installs;
  no subagents; no background jobs; no sibling messaging.
- All 22 mutant commits used the throwaway identity inside `$D/lane` only, after toplevel verification; the
  lane's git state and index were never touched (read-only `status`/`rev-parse`/`log` against the lane only).
