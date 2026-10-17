# kotodama — round 10 report (DRAFT BODY — orchestrator finalizes)

> **Scribe X04 draft.** Assembled 2026-10-17 from the fragments landed by
> **21:38Z (18:38 local)** — the wave was still writing when this draft was
> assembled, so every count below carries its source and time, and the
> acceptance numbers are the last receipt's, not a settled tree's. The
> orchestrator finalizes, re-runs the counting command on the settled tree,
> adds the carrying work commit and the admission verdicts, and files this at
> `.ufo/reports/round-10/kotodama.md`. Nothing here is an admission.

Loop 1 of 3, build round 3 of 4 — operator regimen (3 loops × 7 rounds, lane
rounds 8–28). Declared baseline `9dc18ec1339bffd6f81e74f1a5742464ef578749`
(`reports/round-10/claims.json`); declaration commit
`eb348f3ed4dfa5258be3fba15be0618a1667b962` ("round-10: declare claims C/F/O",
18:18:45 −03:00). Cross-revision sweep (scribe, 21:27Z): `git diff --stat
9dc18ec..HEAD` touches only `reports/round-10/{claims,targets}.json` and the
three availability-attempt files (127 insertions, 0 deletions); the committed
artifact tree is identical at baseline and HEAD.

**Availability history (all four attempts recorded in-lane).** 64 workers on
`opencode-go/deepseek-v4.1-flash`; attempts 1–3 (`opencode-go-3/4/5`, files
`reports/round-10/availability-attempt-{1,2,3}.json`) each returned HTTP 402
"Insufficient account funds" with **zero workers launched** ("all 64 workers
failed at launch, no work performed"); attempt 4 retried key 1 within the
sanctioned provider — the run this draft reports. The wave's first scratch
writes appear 18:25–18:26 local; fragments began landing in
`reports/round-10/` from 18:26.

## Work performed

**Coverage (claim C).** Ten entry authors (linguistics ×3, myth-symbol ×3,
culture-material ×2, verification ×2), ten reviewers polling for their entry,
two index updaters, four partition auditors (`reports/round-10/targets.json`).
Landed by the 21:38Z refresh: **10 new `corpus/knowledge/` entries** —
linguistics ×3 (`numerals-and-measures.md` C03; `language-shift-obsolescence-revival.md`;
`sound-symbolism.md`), myth-symbol ×3 (`direction-symbolism.md`,
`plant-symbolism.md`, `divination-omen-systems.md`), culture-material ×2
(`transport-mobility-lexicon.md` C08; `vessel-container-lexicon.md`),
verification ×2 (`verification-independence-anti-circularity.md` C09,
`header-conformance-readings.md` C10) — so C's per-partition floors (≥2 each)
are **met at 3/3/2/2 and the ≥10 total is met at 10**, pending the reviewers'
landed-bytes verdicts and the index update. Author fragments landed for
C03/C08/C09/C10 so far; **7 reviewer fragments**
(`review-C01/03/04/05/06/08/10.md`) and **2 auditors**
(`audit-ling-verif.md` C23: linguistics/verification index-vs-files exact
16=16=16 and 13=13=13 at T0, 29/29 existing entries carry the five-field
profile, whole-corpus README totals 16/16/16/24/13/94=179 under three methods;
`audit-unchanged.md` C25: civilizations/synthesis unchanged, **118/118
per-file hashes match** the round-9 close). Not yet landed at the refresh: the
remaining author fragments (myth-symbol, culture-material, linguistics), the
index update (`index-update.md`), and post-landing T1 re-checks. The reviewers
opened while `coverage/` was empty and are polling (20-min cap); their
pre-landing sections freeze the exact check instruments, and their §2s carry
out-of-seat observations (see Hazards).

**Freshness (claim F, lowest non-retired axis).** Thirteen shard re-runners
(**13/13 landed by 21:38Z**: shards 01–14 minus none — 05 and 12, absent at
the 21:34Z snapshot, arrived later), each re-running every runnable command in
its byte range with output sha256 + exit and writing
`reports/round-10/drift/shard-NN.md`; the drift-ledger scribe merged them into
`reports/round-10/drift/ledger.json` (first version landed 21:33Z; **179 rows
at 21:39Z** — sha256 `40e1bc2b7731de64…` — with verdicts 144 `current` / 25
`stale-documented` / 10 `stale-fixed`). Four stale-fixers (F15–F18) have begun
patching surfaces **in place** with landed fix evidence
(`reports/round-10/fix-{03,04,05,07,08,09}.md` and
`reports/round-10/drift/fix-{16…23}.md`, 8 files at 21:38Z): `git diff SKILL.md`
(21:36Z) shows 18 insertions/9 deletions — the calibration-vocabulary line now
reads "per-claim set S/C/H/R/U/V" with a `shard-06` §06-G pointer, the
checklist header now says "executable where a tool exists", the civilizations
map now says "94 entries: 92 bases plus two source maps", and the round-3
replay row now records the live-tree `gate_digest_mismatch` finding with a
pinned-revision replay recipe citing `reports/round-10/drift/fix-18.md` —
initially unresolvable at 21:36Z, but the file landed at **21:36:50Z** (see
Hazards 6 — closed as a timing race, not a defect). One in-place **code**
repair is recorded too: `reports/round-8/run-validation.py` (48+/14−, the
isolated-replay pin repair, `drift/fix-20.md` — a runner, not filed report
prose; the file itself calls the lane rule that filed report bytes are never
rewritten). Stale items observed across landed shards include: shard-02
§S02-08 (design-spec §9 pin vs live `era-language-staging.md` hash —
documented, not rewritten), shard-07 DR-07-01/02 (calibration vocabulary; the
`92` count), shard-14 (registry: all 7 gate rows current; 4 stale-documented
harness items), shard-06 §06-G (checklist item 1 has no lane executable — now
documented in SKILL.md itself). The independent drift auditor (F19,
`drift/audit.md`) had not landed at the refresh.

**Operability (claim O).** The findings inventory (`findings-tracker.json`,
21:27Z, sha256 `fb88314d…`) compiles **24 findings** from the four adversarial
files (round-8 `depth/findings.md` 13, `findings-17.md` 3; round-9
`d3/findings.md` 6, `findings-10.md` 2), severity-ranked, with 6 rows already
`resolved_at_source` and 18 open. Eight fixers and four verifiers are working;
at the 21:38Z refresh **14 rows were still pending, 8 `fixed-with-control`,
and 2 `wont-fix`** (idx 0 superseded by the round-8 acceptance decision with a
demonstrated replay recipe); **1 of 4 verifier verdict files had landed**
(`findings-verify-2.md`, R10-O11 re-running O04/O05's controls independently,
window 21:33–21:40Z), and `findings-scribe.md` is absent — claim O's
zero-undispositioned requirement is not yet met.

**Scribe/audit.** X01 lessons gate-keeper (`corpus/lessons/round-10.md`) had
not landed at refresh; X02 adjacency/connector landed
(`reports/round-10/adjacency.md`, 21:31Z; its §6.1 records the round-9 receipt
modification and recommends reverting to HEAD bytes); X03 the acceptance runner
landed (`reports/round-10/run-validation.py`, sha256 `4529ac3d…`) with its
first receipt; X04 this draft + the drift-ledger consistency audit (§ below).

## Landed changes (refresh 21:38Z)

- `corpus/knowledge/` — 10 new entries (untracked at refresh): linguistics ×3,
  myth-symbol ×3, culture-material ×2, verification ×2; `corpus/README.md`
  modified (one civilizations index row rewritten — see Hazards).
- `reports/round-10/coverage/` — 4 author fragments, 7 reviews, 2 auditors.
- `reports/round-10/drift/` — 13 shard fragments + `ledger.json`.
- `reports/round-10/fix-{03,04,05,07,08,09}.md` and
  `reports/round-10/drift/fix-{16…23}.md` — stale-fixer evidence files
  (8 in `drift/` at 21:38Z).
- `reports/round-10/{findings-tracker.json, findings-verify-2.md, adjacency.md,
  run-validation.py, validation.json, __pycache__/}`.
- `SKILL.md` — fixer patches (uncommitted; 18+/9−; the cited `fix-18.md` path
  resolved at 21:36:50Z — Hazard 6).
- `reports/round-8/run-validation.py` — documented in-place runner repair
  (48+/14−; `drift/fix-20.md`).
- `reports/round-9/validation.json` — modified in the worktree (filed receipt
  bytes; X02 `adjacency.md` §6.1 recommends reverting to HEAD — Hazards).

## Before → after measurements

Counting command (declared): `python3 reports/round-10/run-validation.py` →
`reports/round-10/validation.json`. Latest receipt read by the scribe:
**18:31:40 −03:00**, runner sha256 `4529ac3d…`, `acceptance_checks_passed:
False`, `missing_dependencies: [index-update.md, drift/audit.md,
drift/ledger.json, findings-scribe.md]`. That receipt **predates the ledger**
(21:33Z) and most entries, so it is a floor, not a verdict.

| claim | runner verdict (18:31:40) | before (verified) → after (snapshot) |
|---|---|---|
| C / coverage | **passed = false**, 14 failures | 179 entries, thin partitions 16/16/16/13 (scribe re-count 21:27Z, `find corpus/knowledge -name '*.md' \| wc -l` → 179) → **10 of ≥10 new entries landed at 21:38Z (linguistics 3, myth-symbol 3, culture-material 2, verification 2 — every per-partition floor met)**; runner failures name the pre-landing shortfalls + README row gaps (still open: index update, reviewer verdicts) |
| F / freshness | **passed = false**, 3 failures | no round-10 drift ledger → ledger landed (179 rows at 21:39Z: 144 current / 25 stale-documented / 10 stale-fixed) and **13/13 shards**; runner (pre-ledger) failed on "ledger.json absent", "9 shards < 13", "audit.md absent"; fixers patching in place with landed fix evidence |
| O / operability | **passed = false**, 3 failures | 24 open findings across 4 files with no dispositions → tracker compiled (24 rows, 6 resolved-at-source); at 21:38Z **14 pending / 8 fixed-with-control / 2 wont-fix**, 1/4 verifier verdicts (`findings-verify-2.md`), no scribe report |
| coverage/adjacency | observations | 179 entries at baseline; `PROVINCE.md` untouched; handoff contract untouched; no out-of-lane writes recorded yet by X02 (adjacency.md landed 21:31Z, not fully read by this scribe) |

## Drift-ledger consistency audit (X04 assignment)

**Question:** does every command recorded in the ledger actually correspond to
the source locator it claims? **Method:** mechanical, independent of the F
seats' own canonical extraction — parse each row's `source_locator` into
file:line pairs, read the locator's bytes **at the declared baseline revision**
(`9dc18ec`, via `git show`), and classify correspondence: the row command is
the cited command (exact / script-token), or the locator cites the artifact the
command verifies (target-cited / harness-script-exists), or the locator is
prose and the command is an instrument (range-ok), or no correspondence is
mechanically visible (flagged). Tool + raw output:
`.scratch/x04/ledger-audit.py`, `.scratch/x04/ledger-audit-baseline.json`
(untracked scratch, disposable).

**Result at ledger sha256 `40e1bc2b7731de64…` (179 rows, 21:39Z; the ledger
read 150 rows / `5abe8c1c` two minutes earlier and 122 rows / `baa9365b` before
that, and it was already at 189 rows / `ee5b750b` by 21:39:11Z — it is live, so
this audit is a snapshot, and the orchestrator must re-run it at freeze):**

| correspondence class | rows | reading |
|---|---|---|
| cited command, exact string at locator | 41 | strongest — command is in the surface text |
| cited command via script token (args differ) | 31 | e.g. gate table `<packet.yml>` placeholders |
| target artifact cited at locator | 14 | instrument verifies a path the locator names |
| harness script exists (semantic link) | 8 | selftest/run instruments; subject described in prose |
| instrument against prose claim (range resolves) | 22 | locator range exists; correspondence is semantic |
| non-file locator (isolation checks, "invoked by …") | 59 | ledger hygiene, not a locator mismatch |
| chain locator ("via design-spec §9") | 1 | manually checked: chain coherent (shard-02 S02-08) |
| **no mechanical correspondence** | **3** | all three listed below; all targets exist |

The 3 flagged rows are one benign pattern — an instrument verifying an artifact
semantically related to a prose claim, with no textual citation at the locator:
`test -f corpus/knowledge/synthesis/worldbible-integration-contract.md` at
`SKILL.md:3,13` (that path occurs **0** times in SKILL.md — `grep -c` at
baseline and live), `ls corpus/knowledge/verification/real-world-inspiration-boundaries.md`
at `SKILL.md:108–109` (file exists; line is the refusals prose), and
`python3 .scratch/s04-b4-probe.py` at `SKILL.md:61-62` (an ephemeral scratch
probe — not re-runnable after the wave). No row cites a nonexistent surface
file or out-of-bounds line.

**Ledger coverage of the surfaces** (independent extraction of backticked
commands from the surfaces, then match against ledger rows; tool
`.scratch/x04/coverage-crosscheck.py`): `SKILL.md` **18/18** unique cited
commands covered; `SCORECARD.md` **19/20** covered — the one uncovered item,
`git status` at SCORECARD.md:117, is a prose "scope read" mention, not a
counting command. Hygiene gaps in the ledger at the 179-row read: **13 rows
carry no `output_sha256`** (0 lack `exit`), and 59 rows use non-file locators
("shard-08 receipts table", registry-file locators without line numbers, bare
`SKILL.md`, "invoked by …", isolation checks).

**Audit caveat that matters for re-runs:** the F-fixers are editing the live
surfaces, so the same 179 rows classify differently against the *worktree*
than against the declared baseline revision — baseline mode reads 41 exact /
31 script-token / 8 harness, live mode reads 34 exact / 4 script-token / 43
harness, because edited lines no longer contain the commands they cited. The
flagged count is 3 in both modes, so no finding is an artifact of the edits,
but any re-run must state which revision it read; treat live edits as
`stale-fixed` evidence and audit locators against `9dc18ec`.

## Known integration hazards

1. **Filed receipt bytes rewritten in the worktree.** `reports/round-9/
   validation.json` is `M` in `git status` (18 lines changed: two
   `stdout_sha256` values, `git_status`/`untracked_additions` emptied) — a
   rewrite of filed receipt bytes, which round-10's F targets say must not
   happen ("never rewrite filed report bytes — corrections are new entries").
   X02's `adjacency.md` §6.1 records it and recommends reverting to HEAD bytes
   (`git show HEAD:reports/round-9/validation.json`) or recording the decision;
   reviewer C01's §2 also recorded a transient `M reports/round-5/validation.json`
   that is no longer dirty. By contrast, the `M reports/round-8/run-validation.py`
   repair is documented in `drift/fix-20.md` as an in-place runner fix (a
   runner, not filed report prose). The round-9 receipt decision is the
   orchestrator's.
2. **`corpus/README.md` civilizations row rewritten** (`africa-primary-sources.md`,
   expanded prose) — no C01–C10 target partition covers civilizations; whether
   this is an authorised index-updater act is the orchestrator's call.
3. **Seat-ID collision `R10-F14`.** `targets.json` assigns R10-F14 to the
   drift-ledger scribe, but `drift/shard-14.md` also claims seat R10-F14 (the
   registry-vs-gates shard). Both landed; the ledger's `shard` field
   disambiguates, but the collision should be named.
4. **Scratch must not be committed** (`.scratch/`, `__pycache__/` under
   `reports/round-10/`); `/tmp` remains inode-exhausted (`df -i /tmp` →
   `1048576 1048576 0 100% /tmp`, re-confirmed 21:27Z) — all workers used
   in-lane `.scratch/`.
5. **Runner receipt is stale relative to the wave** — re-run
   `python3 reports/round-10/run-validation.py` on the settled tree and file
   the receipt; C/F/O verdicts in the fleet report derive from that run.
6. **Fix-citation race (closed).** The fixer patch at `SKILL.md:166` and `:191`
   cites `reports/round-10/drift/fix-18.md`; at 21:36Z the path did not exist,
   and at **21:36:50Z the file landed** (with `fix-16/17/19` alongside it), so
   the citation now resolves — recorded here as a timing observation for the
   audit trail, not an open defect. Fix evidence on disk at the refresh:
   `reports/round-10/fix-{03,04,05,07,08,09}.md` and
   `reports/round-10/drift/fix-{16,17,18,19}.md`.

## SHONEN skeleton

- [~] SKILL.md real decision tables/error patterns/cited sources — round-10
  fixer patches land on top of the round-8/9 tables (uncommitted at refresh;
  cited fix paths resolve as of 21:36:50Z)
- [~] At least one end-to-end domain task executed and logged — 8 new entries
  + drift ledger + tracker landed; LOG entry is the orchestrator's to append
- [~] Instructions executable without oral context — runner exists; acceptance
  is currently False on all three claims (floor receipt)
- [~] No cross-domain bleed — no sibling-repo writes recorded at refresh;
  X02 adjacency verdict not yet read by this scribe

## Open items for the orchestrator

1. **Finish-or-admit decision.** At the 21:38Z refresh the artifact floors are
   nearly met — entries 10/10 with every per-partition floor, shards 13/13,
   ledger landed and growing, fix evidence landing — but the **verification
   layers are not**: no F19 drift audit, 0/4 O verifier verdicts, 14/24
   findings still pending, no `index-update.md`, no `findings-scribe.md`, and
   the last runner receipt (18:31:40) still reads acceptance False because it
   predates the work. Whether the wave completes or the round is admitted
   partial is the orchestrator's call — this draft records state, not verdict.
2. **Re-run the X04 audit on the frozen ledger** (`.scratch/x04/ledger-audit.py
   --ledger --baseline`) and attach its JSON to the report; the 3 flagged rows
   and the hash/exit hygiene gaps (13 rows without `output_sha256` at the
   150-row read) should be dispositioned or documented.
3. **Receipt integrity.** Decide on `reports/round-9/validation.json` (restore
   or record an authorised-rerun note as a new entry, never a rewrite) and on
   the `corpus/README.md` civilizations row.
4. **Ledger hygiene.** Give the 32 non-file locators resolvable form, or mark
   them `instrument` explicitly in the ledger schema.
5. **Fix evidence.** No action needed on the `fix-18.md` citation (landed
   21:36:50Z); confirm at integration that every path cited by a fixer patch
   resolves, and that no fix file was edited after its citation was frozen.
6. **`/tmp` inode exhaustion** — environment-level, still live; carry to the
   operator, not into the lane's gates.
