- Seat: A08 | scribe | claim A | date 2026-10-19 | baseline 4a7aede

# Round 35 — adjacency audit, ASSEMBLED DRAFT v1 (A08)

**Status: DRAFT for integrator finalization.** This is the assembly skeleton for
`reports/round-35/adj/audit-assembled.md`, which has **no seat out** and is the
integrator's artifact. Nothing here is round acceptance, an axis verdict, a canon,
clearance, promotion or closure decision; no surface is promoted. Claim A is
`reports/round-35/claims.json:54-65`; thresholds at `:64`.

**Snapshot.** `git rev-parse HEAD` → `4a7aede22cd8395b01ce6dd9f46bcae364ca24e4`
(= declared baseline, `claims.json:9`); `git status --porcelain` → only
`?? reports/round-35/` (no tracked modification, before and after every command
below); environment `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`;
write scope = this file only (plus `.scratch/a08b/` working files).

**Fragment state at write time** (`ls reports/round-35/adj/`): **landed** —
`A01-r7-packet.md`, `A02-adoption-tool.md`, `A03-examples.md`,
`A04-skill-agents.md`, `A05-records.md`, `A06-province.md`,
`A07-verify.md` (verifier), `A09-receipt.md`, `A10-gap-fill.md`,
`A11-verify-2.md` (verifier); plus `scout/K04-touched-census.md`,
`review/R06-a-review.md`, `review/R07-a-review.md`, `scribe/S03-a-receipt.md`.
**Owed from the A-block: none** — A03 and A04 landed while this draft was being
written and are folded into §1 rows 1-2/5 and §3 (F12/F13); their verdicts govern
on any disagreement with this draft's earlier provisional wording.

Three evidence classes, never conflated: **fragment-backed** (a landed seat's
verdict, cited by file:line); **A08-direct** (this seat's own re-run, §2);
**carried** (a finding filed elsewhere that this draft must carry, §3).

## 1. Per-surface verdict table (claim A's core)

Surface list = the two commit diffs (`git diff --name-status 139e3b6 da68a6d` for
r33, `da68a6d 4a7aede` for r34), which is the authoritative form: 171 paths, of
which **13 are outside the two round-local report trees** (12 edited live files +
1 new tool, `git diff --name-only 139e3b6 4a7aede | grep -v '^reports/round-3[34]/'`
→ 13 rows); the other 158 are the two round-local report trees (filed fragments,
scanned in §2.2, never edited).

| # | surface | round | verdict | basis |
|---|---|---|---|---|
| 1 | `AGENTS.md` (42 → 40 lines, deletion-only) | r33 | **GREEN** | `A04-skill-agents.md:238` (deletion-only, complete, no residue, boundary repair); `A09-receipt.md:67`; A08-direct: `git diff --numstat` 0/2, hunk view empty — the excision adds no text to scan |
| 2 | `SKILL.md` (35/18) | r33 | **GREEN with named findings A04-1…A04-4** | `A04-skill-agents.md:234-237` (Fixes 1-3 + FD-N4/N5 green; Fix 4's r7 clause stale at HEAD; the re-keyed instrument's record-side glob still name/depth-keyed); `A09-receipt.md:68` (digest `f9bd07c2…`); A08-direct §2.2 |
| 3 | `corpus/knowledge/linguistics/register-lexicon-ceilings.md` §12 (append-only errata) | r33 | **GREEN** | `A05-records.md:29-40` (sweeps reproduce), `A09-receipt.md:69`; HEAD `afe8bf22…` pinned in §4 |
| 4 | `corpus/lessons/README.md` (revision-3 index, +130/−28) | r33 | **GREEN** | folded per **R06-F1** (`R06-a-review.md:62-83`: 33 rows, zero duplicate/missing/mismatched) and `A09-receipt.md:70` |
| 5 | `examples/culture-d3/{README.md,handoff.md}`, `examples/handoff-packet.sample.{md,yml}` (digest repoint) | r33 | **GREEN on the repoint; RED on one boundary leg — A03-F1** | `A03-examples.md:13-15` (PASS on 4 of 5 legs; repoint == live contract bytes, in-lane, no lore-asset claim) and `:75-129,196` (**A03-F1**: the repoint invalidated the D3 snapshot member `examples/culture-d3/expected.json:16`, so the documented frozen check now exits 2 / 1 × `D3-SNAPSHOT` where pre-r33 it exited 0 — unfiled); `A09-receipt.md:71` |
| 6 | `tools/exercise-handoff-e2e.py` (6 edits, 11/10) | r34 | **GREEN** | `A09-receipt.md:72`; A08-direct: live `34c85f57…` == `repin.json:12` `surface_sha256_after` (§2.3) |
| 7 | `tools/harness/receipt_guard_adoption.py` (new, 1309 lines) | r34 | **GREEN, one named gap** | `A02-adoption-tool.md:19-27` (in-lane, zero sibling paths; **A02-F2** registration); `A09-receipt.md:73` (selftest 38/38; only write path is `--out` via `_safe_out`) |
| 8 | `reports/round-34/handoff/declared-in-r7/**` (6 files, frozen) | r34 | **GREEN, one carried finding** | `A01-r7-packet.md:22-43` (8/8 digest claims resolve), `A09-receipt.md:74`; **R07-F3** self-description drift (§3) |
| 9 | `reports/round-34/handoff/repin.json` | r34 | **GREEN** | `A01-r7-packet.md:229`; `A09-receipt.md:75` (its own `canon` field is a limitation statement) |
| 10 | `reports/round-34/op/adoption-inventory.json` | r34 | **GREEN with one consolidated finding** | in-lane rows only; **the 28/17 filed census vs 29/18 live** — one finding, six filers, re-measured by this seat (§2.4, §3-F1) |
| 11 | `reports/round-34/craft/{box1-resurvey-durable.json,anchor-reissue.md}` | r34 | **GREEN with A05-F1** | `A05-records.md:29-40,102` (27/28 row digests; the stale row is the renderer, expected — see §3-F2); `A09-receipt.md:77` |
| 12 | `SCORECARD.md` (r33 29/0; r34 28/3) | r33+r34 | **GREEN with A09-F1** | `A09-receipt.md:78`: three deletions = the rolling "Next:" pointer, content preserved at `SCORECARD.md:604-626` |
| 13 | `LOG.md` (93/0 and 54/0) | r33+r34 | **GREEN** | `A09-receipt.md:79`; A08-direct: `git diff --numstat` → `147 0` cumulative for the window |
| 14 | `REGIMEN.md` (new, 77 lines) | r33 | **GREEN** | `A09-receipt.md:80`; A08-direct: bleed-scan hits are the read-only scope line (`REGIMEN.md:62-63`), all NEGATION |
| 15 | `reports/round-33/calib/open-items-ledger.json`, `reports/round-33/adj/contract-read-record.md`, `reports/round-33/telemetry/r25-28-devin-reading-errata.json`, `reports/round-33/op/lessons-reconciliation-receipt.json` | r33 | **GREEN** | `A05-records.md:29-40` (five-surface table: all GREEN; one digest-precision finding A05-F1); A08-direct §2.1–§2.2 |

**Cross-surface verdict:** zero unfiled cross-domain bleed, zero out-of-lane write
targets, zero lore-owned dispositions absorbed, on every surface above. No
surface carries promotion/canon/clearance/closure language outside a negation,
citation or routing reference (§2.2).

## 2. A08-direct evidence (this seat's own re-runs)

### 2.1 Cross-domain bleed scan — new instrument, 0 genuine bleed

Scanner `.scratch/a08b/bleedscan.py` (this seat, drafted for this audit): eight
PROVINCE-derived term families — canon/world-bible/lore (`L1-L3`), game mechanics
and game-dev (`G1-G2`), real-world rights (`R1`), general research method (`H1`),
web publishing (`K1`), prompt/skill craft (`B1`), sibling paths (`S1`),
ownership-absorption language (`D1`) — classified MENTION-EXEMPT / NEGATION /
ROUTED-REFERENCE / CITED-RESULT / UNSUPPORTED by the same precedence rule as the
filed round-33 language scanner. Selftest **10/10** (exit 0).

| scope | files | hits | MENTION | NEGATION | ROUTED | CITED | **UNSUPPORTED** |
|---|---|---|---|---|---|---|---|
| `reports/round-33/**` | 79 | 1451 | 753 | 596 | 58 | 40 | **4** |
| `reports/round-34/**` | 79 | 539 | 252 | 212 | 17 | 43 | **15** |
| changed hunks of the 12 live files | 12 | 14 | 2 | 11 | 0 | 1 | **0** |
| the 15 durable r33/r34 artifacts (r7 packet set, repin, inventory, box-1 + reissue, ceilings errata, ledger, records, errata JSON) | 15 | 216 | 40 | 150 | 10 | 13 | **3** |
| `reports/round-35/**` (in-flight snapshot, re-run **after** this file landed) | 68 | 1530 | 930 | 531 | 45 | 20 | **4** |

Every UNSUPPORTED row was hand-read. **r33 (4):** `calib/K03-open-items.md:41`
("2 lore-owned" = a debt class named with its owner → routed), `review/R04-calib-review.md:95`
("canonical table" = ordinary adjective, the same reading filed at
`reports/round-33/adj/A08-language.md:96`), `scribe/S01-op-receipt.md:33`
("sibling fragment directory" = in-round siblings, not sibling repos),
`reports/round-33/validation.json:935` (machine stdout containing the fixture id
`HO-CANON-CLAIM`).
**r34 (15):** `calib/C05-receipt.md:193` (sibling fragments), `depth/D04-oq-glossary.md:83`
(ordinary adjective), `handoff/declared-in-r7/expected.json:59` (the JSON field
value `"contract_id": "kotodama-lore-adjacency"` — a name, not a claim),
`handoff/declared-in-r7/packet.md:259` ×2 (the RD-02 blocker cell "canon standing
is lore's; truth status stays unresolved here" — **routed, the classifier's token
list simply misses the possessive `lore's`**), `op/O09-verify-routing.md:90`
("fail-closed" = technical), `plan/P01-d-plan.md:192` (field name `canon-standing`),
`run-validation.py:288` (the runner's own regex source), `scribe/S02-o-receipt.md:41-48`
×7 (the `publish-only` flavour column of the guard-adoption table = receipt
publication, the repo's own lifecycle word). **0 genuine bleed.**

**Precision ceiling (recorded, not papered over):** the `K1` family collides with
the repo's own receipt-publication vocabulary and `D1`/`S1` collide with in-round
"absorbed"/"sibling fragment" usage; and no lexical scanner sees a routed
possessive. **A08-direct instrument note** — the mitigation is a declared
term-collision exemption list, which is what an earlier R07 revision carried; the
R07 bytes at HEAD (198 lines, R07-F4 = owns-list probe width, `:116`) do **not**,
so that item is recorded here as `to-verify` rather than cited
(`reports/round-35/review/R07-a-review.md` re-read at write time).

### 2.2 Governance-language scan — 20 UNSUPPORTED, all adjudicated

The round-33 scanner (`reports/round-33/adj/A08-language.md:478-801`) was
rehydrated verbatim from its fenced block and run over `reports/round-34/**`, the
changed hunks and the new tool: extracted copy sha256
`73296aa4efbfebd714d88a918471df011d8ff8d715d442ce0c9a664069a67434` (identical to
the filed digest), selftest **17/17**.

`files=91`, pass 1 `hits=1331` (MENTION-EXEMPT 382 / NEGATION 735 /
ROUTED-REFERENCE 73 / CITED-RESULT 121 / **UNSUPPORTED-CLAIM 20**), pass 2
`hits=111` (31 / 69 / 1 / 9 / **1**). All 20 pass-1 residuals were hand-read and
are: program text or fixture strings (7: `run-validation.py:288,409,463,464` — the
runner's own `LANG_FRAME` regex and selftest counters; `depth/D07-gate-run.md:341`);
ordinary-sense usages ("false-green"/"wrong green"/"shape-green" at
`cross/X01-trades.md:57`, `depth/D02-render.md:62`, `depth/D07-gate-run.md:477`,
`op/O08-traps.md:423,425`; "canonical sorts"/"canonical correction" at
`run-validation.py:288`, `depth/D04-oq-glossary.md:83`; "fail-closed" at
`op/O09-verify-routing.md:90`); field-name mentions (`plan/P01-d-plan.md:192`);
owes-list or method frames (`calib/C01-survey-run.md:214`, `depth/D13-negatives.md:206`,
`depth/D14-scribe.md:80`, `depth/D16-gap-fill.md:159`). **0 asserting frames**; the
single pass-2 residual is the pass-1 line at `run-validation.py:288`.

**A09-F2 is answered by this leg** (`A09-receipt.md:155`): the round-33 fragment
set's own language verdict is the filed `reports/round-33/adj/A08-language.md`
(2371 pass-1 hits, 9 residuals, 0 genuine violations), and its post-hoc re-scan is
the r33 row of §2.1 — clean.

### 2.3 Pin resolution — every digest in the audited slice resolves

`sha256sum` at HEAD, compared against the digest claimed by the artifact:

| pin | claimed at | live | resolves |
|---|---|---|---|
| `declared-in-r7/packet.md` `45f57132…` | `repin.json:14`, `freeze.txt:2`, `expected.json` `packet_sha256` | same | yes |
| `declared-in-r7/twin.json` `0e229138…` | `repin.json:27`, `freeze.txt:3`, `expected.json` `twin_sha256` | same | yes |
| `declared-in-r7/expected.json` `bbe15887…` | `repin.json:28` | same | yes |
| `declared-in-r7/freeze.txt` `3969954b…` | `repin.json:29` | same | yes |
| `declared-in-r7/claims-map.md` `d181de28…` | `repin.json:30`, `freeze.txt:10` | same | yes |
| renderer `34c85f57…` (`surface_sha256_after`) | `repin.json:12` | same | yes |
| renderer `a5e4a8c5…` (`surface_sha256_before`) | `repin.json:11` | `git show 139e3b6:tools/exercise-handoff-e2e.py` | yes (pre-edit) |
| r6 stale row `ea1e2927…` | `repin.json:17` | same | yes |
| r6 row `packet_sha256 6ced88ad…` | `repin.json:18` | `reports/round-30/handoff/declared-in-r6/expected.json` | yes (the superseded pin, unchanged) |
| contract `5f4c02bf…` (the examples repoint target) | `examples/culture-d3/README.md:104` etc. | `corpus/knowledge/synthesis/worldbible-integration-contract.md` | yes |
| six history rows, two `reading_changed_not_verdict` paths, one precedent | `repin.json` `rows[4]` | all present | yes |

Independently corroborated: `A01-r7-packet.md:22-43` (8/8 claims, 58/58 input
members), `A11-verify-2.md:210`. No digest drift.

### 2.4 Adoption census re-run — 29 / 18 / 11 live vs 28 / 17 / 11 filed

The instrument's own read-only path was used — `python3 -B
tools/harness/receipt_guard_adoption.py --json --out .scratch/a08b/adoption-census-r35.json`
(exit 0; **no in-tree write**: the filed inventory's bytes and the worktree status
are unchanged after the run):

- live census → `runners=29`, `class_counts={guarded-refresh: 18, unguarded-in-place: 11}`, `gaps=[]`;
- filed `reports/round-34/op/adoption-inventory.json` → `runners=28`,
  `{17, 11}`, `census_complete=true`, `gaps=[]`;
- the missing row is exactly `reports/round-34/run-validation.py`, live class
  `guarded-refresh` (guard calls at `:517,:533`);
- `ls reports/round-*/run-validation.py | wc -l` → **29** (rounds 5-12, 14-34; no round 13).

`LOG.md:3605-3606` (mid-round note) says 28/17/11 = the filed artifact;
`LOG.md:3635` (admission) says 29/18/11 = live. See §3-F1.

### 2.5 PROVINCE re-verification — this seat's own reading

`sha256sum PROVINCE.md` → `05b34a579c5d4f4ec78957cdedb658246ff292df3e21181c66186403f2b942d6`
(31 lines); `git rev-parse HEAD:PROVINCE.md` → `313b182f…`, identical at `139e3b6`;
`git log --oneline -- PROVINCE.md` → only `c53782a` and `a527120`; `git diff c53782a HEAD -- PROVINCE.md` empty. **Rounds 33/34 did not touch it.** Owns-list
(`PROVINCE.md:9-14`): all six named partitions and `tools/gates/` present; the new
tool, the r7 packet and the repointed renderer all sit under owned
`tools/`+`reports/` (`PROVINCE.md:9-11`). Refuses-list (`:16-20`): no touched
artifact references `game-dev-2d/3d`, `chousa/`, `kake/` or `kotoba/` as a target
(§2.1 `G2/H1/K1/B1` families: zero hits outside the ordinary-sense classes above);
the only sibling mentions in the window are the read-only scope statements
(`REGIMEN.md:62-63`, and the r33 audit fragments that quote it). Independently
reproduced by `A06-province.md:22-124`, `A11-verify-2.md:24-110`, `R07-a-review.md:130-142`.

## 3. Findings register with owners

**F1 — the filed adoption inventory is one runner short of live (consolidated;
six filers, three independent measurements).** Filed 28/17/11 with
`census_complete: true`, `gaps: []`; live 29/18/11 (missing
`reports/round-34/run-validation.py`, itself `guarded-refresh`). Filed by
`A02-adoption-tool.md:150-153` (A02-F3, informational), `A07-verify.md:117-137`
(A07-F1, **medium**), `A09-receipt.md:156` (A09-F3), `A10-gap-fill.md:79-97,217`
(A10-F1, upgraded to intra-round contradiction), `A11-verify-2.md:243-295,304`
(A11-F1, low-mod), `scout/K04-touched-census.md:161-168` (K04-F1); re-measured by
this seat via the tool's own `--out` path (§2.4). **Owner: integrator** — the
remedy is a dated revision row or a new census artifact, never an in-place edit of
the filed JSON, plus one round-record line so `LOG.md:3605` and `:3635` are
reconciled. Not a bleed, not an ownership defect.

**F2 — box-1 durable receipt carries one stale row digest.** `A05-records.md:102`
(A05-F1): 27/28 row digests reproduce; `tools/exercise-handoff-e2e.py` is pinned
`a5e4a8c5…` (= `da68a6d`) but is `34c85f57…` at HEAD because the admission commit
that landed the receipt also edited the renderer. Independently re-hashed and
confirmed by `A07-verify.md:92`. **Owner: integrator** — a dated revision row; the
receipt's own `not_a_promotion_verdict` framing stands (`A09-receipt.md:77`).

**F3 — the frozen packet misdescribes its own claims-map source (carried; must
not be silently dropped).** `R07-a-review.md:104-115` (R07-F3):
`declared-in-r7/packet.md:3` says the twelve D4 rows come from
`reports/round-20/handoff/claims-map.md`, while its own manifest row A-57 (`:95`),
§reads (`:113`) and §claims (`:125`) name
`reports/round-34/handoff/declared-in-r7/claims-map.md`; the two revisions differ
(r20 `4b1b9a35…`, 275 lines; r34 `d181de28…`, 259 lines). Root cause: the
hard-coded literal at `tools/exercise-handoff-e2e.py:2700` was not repointed by
`4a7aede`, which moved `:184`, `:1933-1934` and `:2566`. **Owner: renderer/packet
owner (r34 D-block) + integrator** — remedy is a new packet revision or a named
errata row; **never an in-place edit, and a re-freeze is a round-35 non-goal**
(`claims.json:70`). Unfiled by A01, A06 and A11; carried here as instructed.

**F4 — A06 citation errata (precision only, verdicts unchanged).**
`R07-a-review.md:88-94` (R07-F1): the refuses line is at `lore-shokunin/PROVINCE.md:9`
(not `:10`, cited at `A06-province.md:133-134`) — **verified read-only at write
time**: that line is the `Refuses:` line of the sibling lane's province file — and
the chousa mint note is at the **fleet-root** `/home/vgpnk/Projects/shokunin/MANIFEST.json:2314`
(not `:2312`, cited at `A06-province.md:136`; `:2312` is the bare `"chousa"` array
element, `:2314` the note). Both pointers are outside this repo and were read
read-only, never written. **Owner:
integrator/A08** — carried with the corrected pointers here; same defect class as
r33-A11's D1/D1b/D3.

**F5 — new instrument not registered in SKILL.md's executable-authority table.**
`A02-adoption-tool.md:125-149` (A02-F2, low-medium). **Owner: integrator** —
registration edit + paired box-1 re-survey, or an explicit accepted-exception
record. A11's wording note (`A11-verify-2.md:303`, A11-N1) and R07-F4
(`R07-a-review.md:116-122`, owns-list probe width) are the same family and are
recorded as notes, not defects.

**F6 — write-scope claim broader than the mechanism.** `A02-adoption-tool.md:65-124`
(A02-F1, low): the tool's stated limit ("never writes into a filed round") is
enforced by `_safe_out` refusing absolute paths, `..` and `.git` — but not by
destination inspection. Verified by this seat's §2.4 run: `--out` honours the
declared scope. **Owner: integrator** (wording or an added refusal; not a live
hazard).

**F7 — repointed surfaces carry under-dated measurement provenance.**
`A07-verify.md:138-152` (A07-F2, low). **Owner: integrator** — answered in part by
this seat's durable pin row (§4), which gives the post-edit digests a round-35
measurement.

**F8 — the untracked `run.log` class.** `R06-a-review.md:85-105` (F-R06-2, low,
systemic not an r34 regression: `.gitignore:3` `*.log` also hides the r30 and ≥6
earlier handoff transcripts) and `scout/K04-touched-census.md:80` (K04-F2).
**Owner: integrator** — `git add -f` with a recorded exception, a non-`.log`
name, or an accepted-class record.

**F9 — SCORECARD r34 edit is the first with deletions in 12 commits.**
`A09-receipt.md:154` (A09-F1). Content preserved at `SCORECARD.md:604-626`.
**Owner: integrator** (append-only-discipline note).

**F10 — precision defects against sibling fragments (verdicts unchanged).**
`A07-verify.md:153-210`: A07-F3 (A04 slice wording — written while A04 was absent;
A04 has since landed, so the integrator should re-read that note against
`A04-skill-agents.md:1-297` before acting), A07-F5 and A07-F6 (against A05),
A07-F7 (against A01's game-dev enumeration).
**Owner: integrator** — route or record; none changes a surface verdict.

**F11 — claim-A threshold is met by the receipt's own table, not by independent
slices.** `A09-receipt.md:157` (A09-F4). Answered in part here: this draft folds
`A07` and `A11` (two independent verifiers) over the A01-A06 slices, and A03/A04
landed with their own §7 tables. **Owner: integrator** — the residual gap is only
the two verifier seats' coverage of the A03/A04 slices.

**F12 — the r33 examples repoint invalidated a D3 freeze-manifest member (real
finding; unfiled by r33/r34).** `A03-examples.md:75-129,196` (A03-F1): the
repointed `examples/handoff-packet.sample.md:21` moved the file `4e24bd3b…` →
`adfd7895…`, so `examples/culture-d3/expected.json:16` (a 24-member computational
snapshot declared at `:3-28`, coverage line `:32`) no longer matches; the
documented frozen check now exits 2 with `1 × D3-SNAPSHOT` where the pre-r33
baseline exits 0. The manifest's own limits line anticipates the class
(`expected.json:33`), so the red is the designed signal — what is missing is the
**record** and the per-input re-acknowledgement (`grep -rn "D3-SNAPSHOT"
reports/round-3[0-4]/` → 0 hits). No filed round claimed this leg green, so no
admission is contradicted. **Owner: round-33 repoint author / integrator** — a
record plus a remedy choice (re-acknowledge the snapshot, or pin the sample), never
an in-place edit of filed bytes. The plain (unfrozen) leg stays green
(`check-evidence-coupling.py examples/culture-d3/packet.json` → exit 0).

**F13 — the close-what-you-open rule is unmet for two filed records, and the
instrument cannot see it (high for the rule; owner: the round-33/34 integrating
parents, routed via the integrator).** `A04-skill-agents.md:128-182`:
`reports/round-33/telemetry/observed-dispatch.json` and
`reports/round-34/telemetry/observed-dispatch.json` are filed
`state: "open-at-seat-close"`, both rounds' `validation.json` have landed, and no
filed file names either record in a `closes` field (both snapshots close only
`dispatch-declared.json`); no `also_closes` key exists in the filed bytes
(`A04-skill-agents.md:155-182`). Related sub-findings, same owner: **A04-1**
(the re-keyed falsifier's record-side glob is still name-and-depth keyed, so it
cannot report the miss), **A04-3** (the landed N1 errata is stale on its r7 clause
at HEAD), **A04-4** (N1 applied at one of its three sites). The round-35 telemetry
draft repeats the same shape (`scribe/S05-telemetry-draft.md:245-246`), which is
why this is flagged now rather than at close.

**Not findings (recorded so peers do not re-file):** `A10-gap-fill.md:97-110`
(A10-F2, adjudicated not-filed); `R07-a-review.md:123-128` closes R06-F1 and
R06-F2's unfiled complaints (R06-F1 is answered by folding surface 4 in §1);
`A05-records.md:62-64` (the X63-F2 corpus sweep defect is routed, never repaired
in place); `A03-examples.md:197-198` (A03-F2: the r33 LOG block does not name the
four repoints — record completeness, no byte defect; A03-F3: the one remaining
live non-filed citation of the superseded digest is a truthful historical
read-record at `corpus/knowledge/verification/gate-frozen-run-standard.md:9`, and
the frozen copies retain it by design — no action).

## 4. Post-edit digest pin row (answers R07-F2)

Measured by this seat at HEAD `4a7aede` (`sha256sum`, `wc -l`); "pre" = the same
path at `139e3b6`. Durable so a later drift is detectable:

| path | lines | sha256 at HEAD | pre-139e3b6 |
|---|---|---|---|
| `SKILL.md` | 732 | `f9bd07c2bd13462367be20e8d775cec1c5569eb2e575dc5d078519ecc72e5a9b` | `79fe91d3…` |
| `AGENTS.md` | 40 | `5ae7a9c8abab0843cfc6db09849f2fff369c0e880085deb546ec7ab764333808` | `1afaf106…` |
| `REGIMEN.md` | 77 | `efb1bc3b41f536d74241a343b08c0552ab2cfc55cffa906b1d74a951ea54c5c4` | new |
| `SCORECARD.md` | 701 | `e972478ba82344a28a314c16b2b1b11034db39ad9c98a37c3ad92ea16b9568f7` | `456f0573…` |
| `LOG.md` | 3646 | `24331e826770415763177b86c630260cd1476197d8614f4f5e789d4f0eb0c4c9` | `3e786a81…` |
| `corpus/lessons/README.md` | 448 | `f752e1d79ae627a0d9728fe16fd1532e7cb9e587f6ac7025a880d8af46233868` | `ec7469da…` |
| `corpus/knowledge/linguistics/register-lexicon-ceilings.md` | 317 | `afe8bf229c863e05dc546aa63060b13ca08d7a444a5c59937570d0cbf2473790` | `bb579d51…` |
| `examples/culture-d3/README.md` | 171 | `946053ee973f5402d99c6252cf42d97d35acb57bb523a3e709a8afeb7415482b` | `d0f62ad7…` |
| `examples/culture-d3/handoff.md` | 286 | `c4fabccb39b51aac841ebaae42aa45781a1145b028ff054e23f491ce8ac0a1ad` | `0d8d660b…` |
| `examples/handoff-packet.sample.md` | 152 | `adfd7895461af85275d0170f7a2e057e0c5265ab2bc0ebadc298d2bae7766dc9` | `4e24bd3b…` |
| `examples/handoff-packet.sample.yml` | 656 | `751be0449edce03a54c21ed82b77f9d1f5e3faaf14ef2482c8525941e70cb95b` | `b900549e…` |
| `tools/exercise-handoff-e2e.py` | 4613 | `34c85f5773fb1925ff7d454f873a2e88fa8246af10c6830468041dd44452eea9` | `a5e4a8c5…` |
| `tools/harness/receipt_guard_adoption.py` | 1309 | `5858abcd0261e8176ebb285db6d80a7c36185d9a12895b4b43b75710db036544` | new |
| `PROVINCE.md` (unchanged) | 31 | `05b34a579c5d4f4ec78957cdedb658246ff292df3e21181c66186403f2b942d6` | same |
| `reports/round-34/op/adoption-inventory.json` | 1825 | `ceeb8d0413e2832a8555e5a9467f016208a477fc708c7f3834bcc429a6bebf04` | new |
| `reports/round-33/calib/open-items-ledger.json` | 519 | `ae35330fbcc20aaf189352c09a4296be45ae92cd8849a23e1bec18aad62471e5` | new |

Note (R07-F2): no round-35 text should restate the pre-edit ceilings reading
`bb579d51…` (289 lines) as current — it is the `139e3b6` reading.

## 5. Contested scope — routed, not absorbed

- **Bilateral read.** `reports/round-33/adj/contract-read-record.md:1-9` is a
  kotodama-side §1 read only; `:9` excludes a lore read, acknowledgement,
  acceptance or canon standing (`A05-records.md:165-193`). The fleet L0 rows 44/45
  and lore's own queue remain unanswered; nothing in this round closes them.
- **Freshness.** The axis-move pause stays in force (`claims.json:18`).
- **R34-N1/N2.** Named findings with owners in `repin.json:49-52`; the KeyError
  mechanism is routed to the renderer hardening (claim O), not repaired here
  (`A01-r7-packet.md:156-194`).
- **X63-F2 / corpus sweep defect.** Routed, never repaired in place
  (`A05-records.md:62-64`).
- **Box-1 marks.** Operator-owned; the durable receipt carries
  `not_a_promotion_verdict` (`A09-receipt.md:77`).

## 6. Adjacent observation, explicitly outside the audited surface

The §2.1 completeness pass over the in-flight `reports/round-35/**` snapshot found
4 UNSUPPORTED rows across two **coverage** seats' draft entries —
`cov/C08-entry-8.md:197,246` ("a world bible can specify"), `:178`
("absorbs" in a passive construction), and `cov/C09-entry-9.md:55` (a `canon`
occurrence). These are **not** claim-A surfaces (claim A audits what rounds 33/34
created or edited, not this round's drafts), and the entries are unlanded draft
bytes. Flagged here so the honesty/conformance critics see the rows were found and
scoped out with a reason. **Owner if they land unchanged: the C seats +
integrator** (one wording pass before the entries are applied).

## Owed

- **From the A-block: none.** A03 and A04 landed while this draft was being
  written and are folded in (§1 rows 1-2/5, §3 F12/F13); the earlier provisional
  wording resting on A09 rows 1-5 is superseded by their §7 verdict tables on any
  disagreement.
- **Integrator finalization:** `adj/audit-assembled.md` (no seat out) must fold §1
  + §3, keep §4's pin row durable, record F1's revision row and the `LOG.md:3605`
  vs `:3635` reconciliation, route F2-F13 owners, and carry **F12** (D3 snapshot
  member invalidated, remedy choice) and **F13** (the two `open-at-seat-close`
  telemetry records + A04-1/-3/-4) into the round record rather than leaving them
  in a draft.
- **Two verifier seats' coverage of A03/A04** (`adj/A07-verify.md` and
  `adj/A11-verify-2.md` landed before those slices) — the integrator should either
  route a re-check or record the coverage gap; it is the residual part of A09-F4.
- **Not owed by this seat:** any corpus/tools write; any `--freeze`; any
  `reports/round-*/run-validation.py` execution in-tree (none was run; §2.4 used
  the adoption instrument's `--out` path only).

## Citations

- Claims/thresholds: `reports/round-35/claims.json:9,18,54-65,70`;
  `reports/round-35/targets.json` seat `A08`; `REGIMEN.md:25-50`; `AGENTS.md:1-40`.
- Landed fragments: `reports/round-35/adj/A01-r7-packet.md:22-43,156-233,249`;
  `A02-adoption-tool.md:19-27,65-153,206-219`; `A03-examples.md:13-15,75-129,196-200,214,241`;
  `A04-skill-agents.md:32-40,128-211,230-248,287`;
  `A05-records.md:29-40,62-64,102,165-193,230-232`;
  `A06-province.md:22-124,133-136,169-200`; `A07-verify.md:92,117-210,252`;
  `A09-receipt.md:38-97,150-175,199-222`; `A10-gap-fill.md:66-110,217,255-269`;
  `A11-verify-2.md:24-110,210,243-304,370`; `scout/K04-touched-census.md:42,80-82,161-183`;
  `review/R06-a-review.md:62-105`; `review/R07-a-review.md:86-162`;
  `scribe/S03-a-receipt.md:362-363`; `scribe/S05-telemetry-draft.md:245-246`.
- Prior-round evidence: `reports/round-33/adj/A08-language.md:1-56,96,476-801`
  (scanner source, digest `73296aa4…`); `reports/round-33/adj/audit-assembled.md`;
  `reports/round-33/adj/A01-province.md`; `reports/round-33/adj/A05-corpus.md:76,275`.
- Commands run by this seat (all read-only or scratch-scoped):
  `git rev-parse HEAD`; `git status --porcelain`; `git diff --name-status 139e3b6 4a7aede`;
  `git diff --numstat 139e3b6 4a7aede -- <live files>`; `git show 139e3b6:<path> | sha256sum`;
  `git log --oneline -- PROVINCE.md`; `sha256sum <16 paths>`; `ls reports/round-*/run-validation.py | wc -l`;
  `python3 -B .scratch/a08b/bleedscan.py --selftest` (10/10) and `--roots …`;
  `python3 -B .scratch/a08b/langscan.py --selftest` (17/17) and `--root …`;
  `python3 -B tools/harness/receipt_guard_adoption.py --json --out .scratch/a08b/adoption-census-r35.json`.
- Working files (scratch, not filed): `.scratch/a08b/{langscan_r33.py,langscan.py,bleedscan.py,hunks/*,adoption-census-r35.json,adoption-census-stdout.txt,bleed-durable.json,bleed-broad.json}`.
