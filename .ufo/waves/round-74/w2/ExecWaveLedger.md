# ExecWaveLedger — attack on the wave-1 seat ledger the report will cite

Wave 2 (falsify), kotodama round 74. Attacked surface: `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-74/w1/{w1-results.json,swarm-registry.json,spec.json,dispatch.json}` plus every file present in that directory. Base `f7104cbce186bc2e1522abf0cfd619cc834628bb`; operative freeze F3 `00c408a0af2fa5ddf65af2224152ce258b26d896`; claim C lands `c4bf61a8d722f9168ce0fd8021a6261c000610c5`; lane main at this seat = `1d7add3` (4 commits over F3: `5e4796c`, `d7a3840`, `c4bf61a`, `1d7add3`).

Verdict up front: the 42/42-report claim **survives** and is better evidenced than round 73's. Four numbers in the log-shaped record do **not** survive as written or are undefined: the attack share (below the prompt's own ≥25% floor), the m_flash share (two defensible values, 57.1% vs 40.5%), the R74-M10 seat-name list (10 named, 26 actual collisions, 2 of the 10 verifiable nowhere), and the "seat ledger" schema itself (no `status`, no `id`; 42/42 `note` null).

No network fetch was performed, so no User-Agent is recorded (nothing was fetched; this seat only read git objects and files). No tool installed. Scratch: `/tmp/ExecWaveLedger/` (three name lists). Writes: this file only.

---

## 1. Census: one seat set, four artifacts agree

```
$ python3 -B - <<'EOF'   # summarized
reg=load('swarm-registry.json')['members']; spec=load('spec.json')['items']
res=load('w1-results.json'); disp=load('dispatch.json')
EOF
counts 42 42 42 {'spawn': 42, 'resume': 0, 'total': 42}
roles_reg {'scout': 12, 'connector': 2, 'scribe': 6, 'executor': 10, 'reviewer': 3, 'critic': 6, 'mutation-tester': 1, 'sentinel': 1, 'simplifier': 1}
roles_spec {…identical…}
roles_res  {…identical…}
setdiff reg-spec set()  spec-reg set()  setdiff reg-res set()  res-reg set()
agentId null count 42   item null count 42   kind Counter({'spawn': 42})
m_flash-class(fl) 24 / 42      attack 10
```

`w1-results.json` carries `seats: 42` and `len(results) == 42`; the dispatch `counts` = `{"spawn": 42, "resume": 0, "total": 42}`; `spec.json` has 42 items, each with a `Report:` trailer; the registry has 42 members. **Name sets are identical across all four.** The attack on "42 seats" fails.

File census of the directory (worktree = F3 = lands for every file except one, see F4):

```
$ git ls-tree -r --name-only 00c408a0af2fa5ddf65af2224152ce258b26d896 -- .ufo/waves/round-74/w1 | wc -l
53
44 (md) + dispatch.err dispatch.json gap-sweep-draft.txt id-map-draft.json
          receipts/measures-c73-at-lands.txt receipts/measures-ca73-at-lands.txt
          spec.json swarm-registry.json w1-results.json
```

## 2. The seat table (42 rows)

`report` = `<name>.md` exists in the wave dir; `at F3` = that exact path is a blob in the freeze commit; `out-chars` = length of the captured `output` string in `w1-results.json`; `status key` = the seat's *own* output JSON carries a `status` field; `partiality fields` = non-empty `not_run`/`unrun`/`could_not_check`/`not_exercised`/`gates_not_run`/`not_checked`/`not_verified`/`blockers` in that output (honest-scope markers, not failure statuses).

| # | seat | role | report | bytes | at F3 | out-chars | status key | partiality fields |
|---|---|---|---|---|---|---|---|---|
| 1 | ScoutLitmemo | scout | present | 20860 | yes | 2240 | — | — |
| 2 | ScoutTuduku | scout | present | 17929 | yes | 1222 | — | — |
| 3 | ScoutChinawriter2025 | scout | present | 18482 | yes | 921 | — | — |
| 4 | ScoutChinawriter2022 | scout | present | 20531 | yes | 2151 | — | — |
| 5 | ScoutSidorovaWorldview | scout | present | 15656 | yes | 2279 | — | — |
| 6 | ScoutQuarantine816817 | scout | present | 13558 | yes | 2305 | — | — |
| 7 | ScoutGapSweep | scout | present | 8348 | yes | 3333 | — | — |
| 8 | ScoutMapIds | scout | present | 9076 | yes | 1918 | — | not_checked |
| 9 | ScoutLedgerSweepA | scout | present | 18756 | yes | 2549 | — | — |
| 10 | ScoutLedgerSweepB | scout | present | 17401 | yes | 1223 | — | — |
| 11 | ScoutLedgerSweepC | scout | present | 29203 | yes | 3405 | — | not_exercised |
| 12 | ScoutWayback | scout | present | 11324 | yes | 2117 | — | — |
| 13 | ConnectorSiblings | connector | present | 20171 | yes | 2331 | — | — |
| 14 | ConnectorPatterns | connector | present | 29622 | yes | 2209 | — | — |
| 15 | ScribeEntryBase | scribe | present | 32363 | yes | 5486 | — | — |
| 16 | ScribeEntryAmend | scribe | present | 24507 | yes | 8171 | — | not_run |
| 17 | ScribeMistakes | scribe | present | 6973 | yes | 4890 | — | gates_not_run |
| 18 | ScribeQuality25 | scribe | present | 21441 | yes | 4508 | — | not_verified |
| 19 | ScribeReadmeIndex | scribe | present | 12733 | yes | 9374 | — | — |
| 20 | ScribeSkillGates | scribe | present | 14343 | yes | 6144 | complete | — |
| 21 | ExecCCounter | executor | present | 28954 | yes | 7211 | complete | — |
| 22 | ExecCaCounter | executor | present | 38821 | yes | 5541 | — | — |
| 23 | ExecLedger | executor | present | 20619 | yes | 5519 | — | — |
| 24 | ExecReceiptRerun73 | executor | present | 17593 | yes | 5054 | — | not_run |
| 25 | ExecRenumber | executor | present | 13375 | yes | 7333 | complete | — |
| 26 | ExecScratchMirror | executor | present | 12197 | yes | 4900 | — | — |
| 27 | ExecSelftest72 | executor | present | 14125 | yes | 7124 | — | not_run |
| 28 | ExecJunkFixtures | executor | present | 27231¹ | yes | 4589 | — | — |
| 29 | ExecEvidence | executor | present | 34145 | yes | 8325 | complete | not_run |
| 30 | ExecLeftovers | executor | present | 22143 | yes | 8176 | complete | — |
| 31 | RevClaimsFidelity | reviewer | present | 37894 | yes | 10793 | — | blockers, not_run |
| 32 | RevEntryQuality | reviewer | present | 29912 | yes | 6024 | — | — |
| 33 | RevAssimilationContract | reviewer | present | 30035 | yes | 5601 | — | not_exercised |
| 34 | CritCCounterVacuity | critic | present | 22813 | yes | 6121 | — | could_not_check |
| 35 | CritCaVacuity | critic | present | 28318 | yes | 5781 | — | — |
| 36 | CritTrendObservables | critic | present | 18031 | yes | 5800 | complete — pre-declaration… | not_ran |
| 37 | CritMistakeFix | critic | present | 31209 | yes | 8285 | — | unrun |
| 38 | CritFrozenCfg | critic | present | 30367 | yes | 3636 | — | not_exercised |
| 39 | CritQuality25 | critic | present | 21550 | yes | 6445 | — | — |
| 40 | MutRegistryCollision | mutation-tester | present | 10666 | yes | 3109 | — | unrun |
| 41 | SentinelScope | sentinel | present | 26811 | yes | 9868 | — | not_run |
| 42 | SimplifierRows | simplifier | present | 25671 | yes | 6934 | — | — |

¹ 27 231 B is the **main/worktree** size; at F3/lands the blob is 15 900 B (`git cat-file -s 00c408a0…:.ufo/waves/round-74/w1/ExecJunkFixtures.md`), and the delta is F4.

Answers to the four questions posed:

- **seats by role**: scout 12, connector 2, scribe 6, executor 10, reviewer 3, critic 6, mutation-tester 1, sentinel 1, simplifier 1 (sum 42).
- **report names with no report file**: **0**. `seats with no report` = ∅ by name, and every declared `report`/`report_path` path that a seat output states also resolves (15 seats state no path at all — F6).
- **reports with no seat**: **2** — `ExecLedger.postwave.md` (10 315 B) and `ScribeReadmeIndex.postwave.md` (4 379 B). Both are the R74-M10 misdelivery copies, both tracked at F3, neither a seat. `ls w1/*.md | wc -l` therefore prints **44**, not 42; any count cited as a seat count must subtract these two (F7).
- **seats whose output says a status other than complete**: **0**. Six outputs carry `status`; five are exactly `"complete"`, one is `"complete — pre-declaration written before data; no lands, no counter, no fetch, no tool install"`. The other **36 seats carry no status field at all**, so "complete" is an inference from (non-null captured output ∧ report at F3), not a recorded fact (F5). No report contains `BLOCKED`, `ABORTED` or `could not complete/finish`.

## 3. Recount: m_flash-class share and attack share

Definition source (the only authoritative one — the ledger carries **no model field**):

```
$ sed -n '89p' .ufo/waves/round-74/build-w1.py
fl = {"executor", "scribe", "critic", "sentinel", "simplifier", "revenger"}
print(len(items), "items;", sum(1 for i in items if i["role"] in fl), "m_flash-class;",
      sum(1 for i in items if i["role"] in {"reviewer", "critic", "mutation-tester"}), "attack")
```

and the run-7 routing that set mirrors (`/home/vgpnk/Projects/shokunin/.ufo/prompts/kotodama-round-74.md:157-162`):

> "executor/labrat/scribe/sonic/simplifier/critic/revenger/sentinel
> `@m_flash`" … "m_flash roles carry the
> majority of every wave (≥50% of seats as executor/scribe/labrat/sonic/simplifier)" … "attack share (≥25%) is met with
> reviewer/critic/mutation-tester/labrat seats."

| count | definition | wave-1 value | share | round-73 wave 1 (same def) |
|---|---|---|---|---|
| m_flash-class | run-7 routing list ∩ builder `fl` = {executor, scribe, critic, sentinel, simplifier, revenger} (+labrat, sonic: 0 seats) | **24 / 42** | **57.1%** | 19/37 = 51.4% |
| "majority" set as literally parenthesised in the prompt | {executor, scribe, labrat, sonic, simplifier} | **17 / 42** | **40.5%** | 13/37 = 35.1% |
| attack | {reviewer, critic, mutation-tester} (+labrat: 0) | **10 / 42** | **23.8%** | 10/37 = 27.0% |
| attack if `sentinel` is folded in | + sentinel | 11 / 42 | 26.2% | 11/37 = 29.7% |
| wave 2 (reference, from `w2/spec.json`) | attack set above | 23 / 44 | 52.3% | — |
| round total | 42 + 44 | **86** | within 64–100 | — |

Command (summarised): `python3 -B` over `w1-results.json` / `w2/spec.json`, role = the `agent` field, `Counter(agent)`.

## 4. Findings

### F1 — HIGH — the attack share is 23.8%, below the prompt's own ≥25% floor, and no landed byte records the number

```
$ python3 -B …  # counts by the builder's own attack set
round-74 wave1 n=42 roles={… reviewer:3, critic:6, mutation-tester:1, sentinel:1 …}
  m_flash=24(57.1%) narrow=17(40.5%) attack=10(23.8%)
```

The prompt's floor is 25% ("attack share (≥25%) is met with reviewer/critic/mutation-tester/labrat seats", `kotodama-round-74.md:161-162`). 10/42 = 23.81%; 11 seats are needed. The wave *validated* anyway: `.ufo/waves/round-74/w1.ready` is only `{"lane":"kotodama","round":74,"wave":"w1","dispatch":"…/w1/dispatch.json","l1":"KotodamaR74"}` — no band, no role mix, no attack fraction — and `dispatch.json`'s `counts` carries spawn/resume/total only, so no artifact shows the floor was ever computed. The prompt's other sentence makes the shortfall avoidable by wording only: "Seat counts, dead seats and role mix come from results.json" (`:178`) — but results.json has no role-share field either, so the reviewer must recompute it, as here.

Fix: state it, do not launder it. Wave-1 accounting line to file verbatim: `attack 10/42 = 23.8% (reviewer 3, critic 6, mutation-tester 1) — one seat short of the prompt's ≥25% floor; sentinel (11/42 = 26.2%) is an m_flash role under run-7 routing, not an attack role under :161-162`. If any landed text asserts the floor was met, it needs a SCORECARD correction row (the lesson is append-only). No claim leg reads the ledger, so claim C/Ca are unaffected.

### F2 — MEDIUM — "m_flash-class share" has two defensible values; the report must name which one it cites

57.1% (routing list, = builder `fl`) vs 40.5% (the literal parenthetical "≥50% of seats as executor/scribe/labrat/sonic/simplifier"). The lane's own LOG has already used three different attack definitions: round-71 "Wave-1 37 seats (18 attack roles)" (48.6%), round-72 "16/32 attack roles = 50%: reviewer 6, critic 5, mutation-tester 3, sentinel 1, revenger 1" (folds sentinel+revenger into attack), round-74 builder (excludes them). So the same word yields 23.8% or 26.2% for this wave depending on which precedent is followed, and the builder's number wins only because it is the only one written down.

Fix: cite `m_flash 24/42 = 57.1% under the run-7 routing list; the prompt's ≥50% parenthetical set is 17/42 = 40.5%` — both, with the definition, exactly as §3 does. Note the model class itself is **not observable** from `spec.json`/`dispatch.json`/`w1-results.json` (no model field anywhere; `agent` holds the *role*, not the model); this is the same defect `ScoutLedgerSweepB.md` recorded for round 73's "19 m_flash-class".

### F3 — HIGH — R74-M10's seat-name list is not the collision set: 26 names collide, and 2 of the 10 listed exist in no round-71..73 wave artifact

`corpus/lessons/round-74.md:177` says: "Wave-1 follow-up messages to seats named like the round-73 seats of this lane (`ExecCCounter`, `ExecCaCounter`, `ExecLedger`, `ScribeEntryBase`, `ScribeEntryAmend`, `ScribeMistakes`, `ScribeReadmeIndex`, `ScribeSkillGates`, `ScribeQuality25`, `ExecEvidence`) reached same-named parked round-73 seats".

```
$ python3 -B …  # name sets from results.json / spec.json / swarm-registry.json of rounds 71-73 w1+w2
73 seats 37 74 seats 42
intersection 26
['ConnectorPatterns', 'ConnectorSiblings', 'CritCCounterVacuity', 'CritCaVacuity', 'CritMistakeFix',
 'CritTrendObservables', 'ExecCCounter', 'ExecCaCounter', 'ExecLedger', 'ExecRenumber', 'ExecScratchMirror',
 'MutRegistryCollision', 'RevAssimilationContract', 'RevClaimsFidelity', 'RevEntryQuality', 'ScoutGapSweep',
 'ScoutLedgerSweepA', 'ScoutLedgerSweepB', 'ScoutMapIds', 'ScribeEntryAmend', 'ScribeEntryBase',
 'ScribeMistakes', 'ScribeReadmeIndex', 'ScribeSkillGates', 'SentinelScope', 'SimplifierRows']
--- listed names and where they existed before:
ExecCCounter           ['round-72/w1', 'round-73/w1']
ExecCaCounter          ['round-72/w1', 'round-73/w1']
ExecLedger             ['round-73/w1']
ScribeEntryBase        ['round-73/w1']
ScribeEntryAmend       ['round-73/w1']
ScribeMistakes         ['round-73/w1']
ScribeReadmeIndex      ['round-73/w1']
ScribeSkillGates       ['round-73/w1']
ScribeQuality25        NOWHERE-PRIOR
ExecEvidence           NOWHERE-PRIOR
--- 74 names with prior existence: 26 of 42
```

(The intersection line above is transcribed from the raw run; the 26th entry printed verbatim was `CritTrendObservables`.) Two consequences: (a) the hazard surface is **26 names**, not 10 — 16 colliding seats are omitted from the mistake row, so a reader will under-estimate the routing risk; (b) `ScribeQuality25` and `ExecEvidence` appear in **no** round-71/w1, round-71/w2, round-72/w1, round-72/w2, round-73/w1 or round-73/w2 `spec.json` / `swarm-registry.json` / `w1-results.json` — if those two follow-ups really landed on same-named parked seats, the colliding identity lives in an unrecorded residual `task` call, and the row as filed overstates what the artifacts can witness. (The two damaged files, `ExecLedger.md` and `ScribeReadmeIndex.md`, are both inside the 26 and both restored — see "attacks that failed".)

Fix (append-only path: a correction row, not an edit to the lesson sentence): reword to `the ten seats actually messaged (two of them — ScribeQuality25, ExecEvidence — have no same-named seat in any recorded round-71..73 wave, so their misroute is attested only by the misroot sweep); 26 of wave 1's 42 names also exist in round-73 wave 1, so name-routed sends must be replaced by wave-qualified ids.`

### F4 — MEDIUM — a wave-1 seat report was rewritten after claim C's lands; at main the ledger's captured output and the report disagree

```
$ git diff --stat 00c408a0af2fa5ddf65af2224152ce258b26d896 main -- .ufo/waves/round-74/w1
 .ufo/waves/round-74/w1/ExecJunkFixtures.md | 157 ++++++++++++++++++++++++++++-
 1 file changed, 155 insertions(+), 2 deletions(-)
$ git log --oneline 00c408a0af2fa5ddf65af2224152ce258b26d896..main -- .ufo/waves/round-74/w1
1d7add3 round-74: junk-landing receipts, measured receipts at each claim's own landing, wave-2 builder
$ git diff c4bf61a… main -- .ufo/waves/round-74/w1/ExecJunkFixtures.md | sed -n '1,20p'
-| sha256 | `d4789c39740de5b6679e63f8fe0b2c54794f9eb358c8e8ab4660de622de9693f` |
-| size / language | 774 lines, Python 3 stdlib only …
+| sha256 | `ce6505fc7d973ced8ad663ee5201eae4931129684dd9794744f115a49fba6d76` |
+| size / language | 1481 lines, Python 3 stdlib only …
+## Post-wave update 2 — round-74 freeze landings (`--run-r74 --freeze F3`)
```

`w1-results.json` still records the seat's capture as `"…junk-fixtures.py (new, 774 lines, stdlib only, sha256 d4789c39…)"` while the report at main states `ce6505fc…`, 1481 lines — and the file on disk is `ce6505fc…`, 1481 lines. So the ledger is consistent at F3/lands and stale at main; the report is the reverse. This is the R74-M1 class (a tracked wave-1 artifact changing after its round's landing), now inside round 74, by the L1 rather than a seat.

Fix: quote the seat ledger at F3 (`git show 00c408a0…:.ufo/waves/round-74/w1/w1-results.json`) and the report at main, and say which revision each number comes from; or move the post-lands text to a `*.postwave.md` sibling exactly as R74-M10's fix did for `ExecLedger`/`ScribeReadmeIndex`, so the 42 seat report paths stay byte-stable across F3 → main. Related, same class: **9 of 42** reports carry L1 `## Post-wave update` sections (`ExecCCounter`, `ExecCaCounter` ×3, `ExecEvidence` ×2, `ExecJunkFixtures`, `ExecScratchMirror`, `ScribeEntryAmend`, `ScribeEntryBase`, `ScribeQuality25`, `ScribeSkillGates`); eight of them are inside F3, one is not. A report is therefore not coextensive with the seat's captured output — the ledger's `output` is the capture, the report is the deliverable.

### F5 — MEDIUM — the ledger has no `status` and no `id`; the prompt declares both

The prompt declares the results shape verbatim (`kotodama-round-74.md:177-178`): "per seat: name, agent, id, status, final output" and "Seat counts, dead seats and role mix come from results.json".

```
$ python3 -B …
round-74 w1 n= 42 keys= ['agent', 'name', 'note', 'output'] nonnull note= 0
round-73 w1 n= 37 keys= ['agent', 'name', 'note', 'output'] nonnull note= 37
```

So `id` and `status` are absent (same shape defect as round 73), and round 74 additionally drops the `note` (round 73's note carried the retention caveat: "orchestrator kernel restarted mid-wave; seat output was delivered … not retained — read the seat report file in the wave dir"). Dead-seat detection therefore reduces to two tests, both of which do discriminate:

```
round-73 w1: seats 37 | null/empty output 37 | …
round-74 w1: seats 42 | null/empty output 0  | …
```

and report-presence (round 73: 3 of 37 missing → the 3 dead seats named in its LOG; round 74: 0 of 42 missing). Both green for wave 1.

Fix: cite the inference, not a status field — `42/42 seats have a non-null captured output (min 921 chars) and a report file that is a blob at F3; 0 seats lack either` — and keep the raw predicates in the report so the statement stays falsifiable. The dispatch tooling should be asked to emit `id`/`status` (this is host-side, not this lane's to change).

### F6 — LOW/MEDIUM — the seat↔report join is name-only, and 26 names are round-ambiguous

```
no report key: 15 | declared path missing: []
trailer mismatches: []
role mismatches: []
w1∩w2 names: []   w2 seats 44 unique 44
```

All 42 spec `Report:` trailers point at `.ufo/waves/round-74/w1/<name>.md` and all 42 exist; 15 seat outputs state no report path, so the join must be by name. Since 26 of the 42 names also exist in round 73 and two report files carry seat names but are not seats (`*.postwave.md`), any cross-round join on the bare name resolves to the wrong file. This is the same root cause R74-M10 records.

Fix: join on `(round, wave, name)` always, e.g. `git ls-tree <rev> -- .ufo/waves/round-74/w1/` then match the basename inside that listing (as §1 does), never a fleet-wide `find -name "<seat>.md"`.

### F7 — LOW — two `*.md` in the wave dir are not seat reports

`ExecLedger.postwave.md`, `ScribeReadmeIndex.postwave.md`: L1 copies of the appended sections (`## Post-wave update — round 74 ledger finalization (L1 follow-up)`; `## Post-wave update`), tracked at F3. `ls *.md | wc -l` = 44. A seat-count citation of 44 would be wrong; 42 is right.

### F8 — LOW — `swarm-registry.json` is a dispatch manifest, not a completion record

```
stats: createdAt == updatedAt == 2026-10-25T23:56:10.341Z (= 20:56:10 -03, the dispatch minute;
       spec.json 20:56:05, dispatch.json 20:56:10, w1.ready 20:56:14; last seat 21:44; results 21:57)
wave: null | members 42 | agentId null 42/42 | item null 42/42 | kind {"spawn": 42}
```

It is written once at dispatch and never updated; it cannot corroborate that any seat ran. Round 73's registries have the same shape (`createdAt == updatedAt`, `wave: null`), so this is a standing convention, not a round-74 regression — but the report must not cite the registry as evidence of completion, and `item: null` means it cannot even be joined to the spec items without the name.

## 5. Numbers in `corpus/lessons/round-74.md` that disagree

- `:177` R74-M10's ten-name list — see F3. The row's own class (`scope`) and fix (copy + restore + name the misdelivery) stand; the **set** is wrong on both sides: 10 named vs 26 colliding, and 2 of the 10 unverifiable in any recorded wave.
- The lesson carries **no** wave-accounting sentence at all: no seat total, no role mix, no m_flash share, no attack share, no dead-seat count (`grep -n 'seats' corpus/lessons/round-74.md` matches only the M6/M10/`wave-1 follow-up` prose). Rounds 71, 72 and 73 each carry a "Wave accounting" line in `LOG.md`; round 74 has no `LOG.md` entry yet, so the only place these numbers can be filed is the closure report/LOG. Silence is not a wrong number, but it is a gap the report must close, and the numbers to close it with are §3's, not the builder's bare `24`/`10`.

## 6. Attacks that FAILED (the ledger survived)

- **Seat total 42.** Four independent artifacts agree exactly (results `seats`/`len`, spec items, registry members, dispatch counts); no duplicate name in any of them; 42 unique names.
- **Every seat reported.** 42/42 seat-named `.md` present, non-empty (smallest 6 973 B), all 42 tracked at F3 **and** at lands (`git diff --stat F3 c4bf61a -- .ufo/waves/round-74/w1` prints nothing); 0 reports without a seat once the two `*.postwave.md` copies are excluded; 0 seats without a report.
- **Dead seats 0.** Discriminating test (`output` null/empty) fires 37/37 on round 73 and 0/42 here; report-presence 3/37 vs 0/42.
- **Role mix.** Identical in results, spec and registry; no seat's `agent` differs from its spec `role`.
- **Trailer routing.** All 42 spec `Report:` trailers resolve to the seat's own `<name>.md`; 0 misdirected trailers (the R74-M10 failure was in a *follow-up send*, not in the spec).
- **Wave separation.** w1 ∩ w2 names = ∅; w2 = 44 unique names; round total 86 inside the 64–100 band (operator floor 64).
- **Claim exposure.** No claim leg reads the ledger: `grep -n 'w1-results\|swarm-registry\|seats' reports/round-74/accept-c.py reports/round-74/accept-ca.py reports/round-74/claims.json` → 0 lines. Every finding above is a record defect, none can move a `legs=` count.
- **Round-73 restoration (R74-M10's fix).** `git show f7104cb:.ufo/waves/round-73/w1/{ExecLedger,ScribeReadmeIndex}.md | grep -c 'Post-wave update'` → `0` and `0`; `git diff --name-status f7104cb main -- .ufo/waves/round-73` lists only the six w2 files (five `M` + `RevengerOrigins.md` `A`) — no round-73 w1 file was touched, so the two reports were restored byte-exactly.

## 7. What the closure should file (paste-ready, derived above)

> **Wave 1 — 42 seats** (scout 12, connector 2, scribe 6, executor 10, reviewer 3, critic 6, mutation-tester 1, sentinel 1, simplifier 1), **42/42 reports present and tracked at F3 `00c408a0`**, **0 dead** (every captured output non-null; no seat lacks a report). m_flash-class **24/42 = 57.1%** on the run-7 routing list (the prompt's narrower `executor/scribe/labrat/sonic/simplifier` set is 17/42 = 40.5%); attack roles **10/42 = 23.8%** (reviewer 3, critic 6, mutation-tester 1) — **one seat short of the ≥25% floor**, with sentinel counted it is 26.2%. Wave 2 — 44 seats, attack 23/44 = 52.3%. Round total **86**.
> Seat-name hygiene: 26 of the 42 names also exist in round-73 wave 1 (R74-M10 lists the 10 actually messaged; `ScribeQuality25`/`ExecEvidence` match no recorded round-71..73 seat).

Two things the report must not say: "44 reports" (that counts the two `*.postwave.md` copies) and "all seats reported complete" as if read from a status field (there is none; it is inferred from output + report at F3).

## 8. Tooling, scope, honesty

- Tools installed: **none**. Package manager: not invoked (pacman paused host-wide).
- Network: **no fetch**, therefore no UA record; every fact above comes from a git object or a worktree file under the lane, or from `git show` of F3/lands/main.
- Writes: this report only. Scratch `/tmp/ExecWaveLedger/{a.txt,b.txt}` (name lists). No write to the fleet repo, `corpus/**`, `reports/**`, `LOG.md`, `SCORECARD.md`, `SKILL.md`, `.ufo/state`, or any sibling lane; lane git index untouched (read-only `git log/show/ls-tree/diff` only).
- Unrun: no execution of the round counters (they belong to other seats' beats and the parent's post-integration gate), no `jj-lane.sh`, no wave-2 results file exists to compare (`w2/w2-results.json` absent at this seat).
