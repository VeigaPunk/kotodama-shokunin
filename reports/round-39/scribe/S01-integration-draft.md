- Seat: S01 | scribe | claim cross | date 2026-10-19 | baseline dfb0719

# S01 — round-39 integration dossier: fleet-report material + validation-leg spec

**Mission (binding, `reports/round-39/targets.json:117-123`):** *"Integration dossier: fleet-report
material + validation-leg spec."* Out path: this file only.

**Status: DRAFT — integration material, not a fleet report, not a validation receipt, not an
acceptance verdict.** Every number below was measured by this seat at the revision and in the
window named in §1, unless it is explicitly attributed to a sibling fragment (§11 folds each one).
Nothing here asserts promotion, canon, clearance or closure; those tokens appear only as negations,
routed references, or inside quoted scanner patterns (§10).

**Seat context.** Single 16-seat batch (`claims.json:8`; REGIMEN.md:17 row 7 — 16 requested is
**inside** the declared 16–32 range, no deviation this round). This dossier is written mid-wave:
at finalization (§1 window) **6 of 16 declared outputs had landed** (K01, K02, C01, C02, Ca02,
X00) plus the two declarations and the telemetry record. The census is recomputed in §2.3; the
integrator must recompute it again at close, not trust either count.

---

## §0 — The headline the integrator must read first

**At this seat's cut, not one byte of either declared claim's after-state exists.**
`git diff --name-status dfb0719` is **empty** (zero modified tracked bytes); all untracked rows are
`?? reports/round-39/…`. Specifically:

| claim | what exists (drafts) | what does not exist |
|---|---|---|
| **C** (coverage) | K01's gap scout with 4 topic recommendations and the entry contract (`scout/K01-verification-gaps.md`); two executed entry drafts with measured gap-absence sweeps of their own (`cov/C01-entry-1.md`, `cov/C02-entry-2.md`) | any `corpus/knowledge/verification/*.md` addition (partition still **20**); C03/C04 drafts; C05's audit; C06's README rev-2.2 delta + receipt; any `corpus/README.md` byte (still revision 2.1, sha `b80274bc…`, sweep green at 212/212) |
| **Ca** (calibration) | Ca02's replay verification — all four r37 could-not-reproduce rows **REPRODUCED** (`calib/Ca02-replay-verify.md`, verdict + disposition mapping); K02's isolation scout (the O12 mechanics and protocol design inputs) | `calib/Ca01-protocol.md` and the canonical `calib/isolation-replay-protocol.md`; the **successor ledger** redispositioning R37-Ca-05..08; `calib/Ca03-basename-policy.md` and the canonical `calib/basename-couples-policy.md`; Ca04's verification |

Consequences carried into the leg spec rather than papered over:

1. **Claim C's after-state is unreachable at my cut** — the four entries and the README delta are
   drafts, and corpus changes are integrator-applied by the round's shared rule
   (`targets.json:6`). A close-time runner measuring the tree before the apply measures the
   *before* state; the C legs are written to be run **after** the §8 ordering steps 3–5.
2. **Claim Ca's counting command does not exist.** `ls reports/round-39/run-validation.py` → *No
   such file or directory*; `ls reports/round-39/validation.json` → the same. Claim Ca's counting
   command (`claims.json:23`) and threshold are close-time only, and per F-C13-1
   (`targets.json:8`) the runner must **never** be executed in-tree — this dossier is the
   specification the integrator implements (§5–§6), not a runner this seat ran.
3. **The Ca replay's central adjudication is open, and it is the round's honest-crux.** Ca02
   reproduced all four rows with a **one-line-adapted** replay copy (`ROOT = os.getcwd()`,
   digest-pinned `46e55b80…`, `Ca02-replay-verify.md §Protocol 3`), while the filed r37 precedent
   excluded an altered-ROOT run from its recount ("source-redirected diagnostics do not count",
   `reports/round-37/calib/Ca02-r34.md:20`; P01's r37 plan forbade runner patching,
   `reports/round-37/plan/P01-ca-plan.md:19-24` via `Ca02-r34.md:18`) and both K02 (§4 item 3) and
   X00 (§3 item 3) specified **unmodified-source** replays (bwrap bind-over). Both readings are
   defensible: `claims.json:21` declares the "relative-root requirement" as **part of the
   protocol**, which the adaptation instantiates. §6.3 leg Ca5 requires the integrator to
   **record the mechanism and rule on the disposition** — with R01's review as the adversarial
   input — rather than let a green verdict imply an unmodified-source reproduction that did not
   happen. Either declared disposition satisfies claim Ca(b) (`claims.json:21`).
4. **The absolute-ROOT runner set is five, not three — and the streak is live.** K02 §1 names
   r34/r35/r36; this seat's census (§3.2) measures **five** filed runners carrying the absolute
   `ROOT = "/home/vgpnk/…"` + `os.chdir` shape: r34, r35, r36, **r37, r38**. The two most recent
   runners re-carried the O12 hazard shape even though round 38's own record rules "copy the r33
   relative-ROOT shape, never the r34/r35 absolute os.chdir shape"
   (`reports/round-38/cross/X01-trades.md:367-369`; `reports/round-38/scribe/S01-integration-draft.md:418-425`).
   The round-39 runner must break the streak (§5), and Ca01's protocol should state its scope over
   all five, not three.

---

## §1 — Window, state pins, and what "first-hand" means here

| pin | value | command |
|---|---|---|
| lane root | `/home/vgpnk/Projects/shokunin/kotodama-shokunin` | — |
| baseline | `dfb0719711204b5943432034bd80c8dc248acddd` | `git rev-parse HEAD`; `git rev-parse dfb0719` (equal; the r38 admission commit) |
| tracked cleanliness | **empty** — zero modified tracked bytes | `git diff --name-status dfb0719` |
| untracked scope | 7 rows at first census (12:12Z), all `?? reports/round-39/…`; 9 by finalization (K02, C02 landed) | `git status --porcelain -uall` |
| observation window | `2026-10-19T12:12:14Z`–`12:2xZ` | `date -u +%FT%TZ` |
| interpreter | Python **3.14.7** | `python3 -V` |
| env | `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1` | before every python invocation |

Every command in §1–§4 was run by this seat in that window from the lane root. **No
`reports/round-*/run-validation.py` was executed anywhere** — in-tree or in a copy (F-C13-1,
`targets.json:8`) — no `--freeze` was issued against `reports/round-34/handoff/declared-in-r7`,
and no git-mutating command was run. The one sweep this seat ran is the round-28 README sweep,
read-only over `corpus/` (`reports/round-28/readme/sweep.py:28-30`, the same read-only contract
X00 cites at its header).

**Digests this dossier binds to** (measured at `dfb0719`, lane root):

```
73347e55fb56a3bc03230aa59afe033703b9fdef4c82efb736d335567db301e3  reports/round-39/claims.json
f696833ebaa8c9653f102ff6567ae533c034baed054109903109eb261921852a  reports/round-39/targets.json
1b21ed5b6c45db7b05f020c89450a325eb95327daef1542ff996f7bf279308a5  reports/round-39/telemetry/dispatch-declared.json
b80274bcd24b8b6e621f499fb20d4a07aa3b7b48dbb3508e0a9ac974f68e1d74  corpus/README.md
73d2d48d6b6f902802503371dae9e9b60cd3bf0190a71518ed7ec0713d5f4b22  reports/round-37/calib/recount-ledger.json
5cf827e2dd17b638acf023b1c6423b0602ba88e3c08d9698b68bae6c6cc60d5d  reports/round-37/op/defect-queue.json
88db61bfe4bb6784bce039013d180853e171068c7bf5ce19a300d3d86b8fce6e  reports/round-38/validation.json
be11ff46f1fe399cbedcba956d39134a39e25fcfbb74e4b3dc958f2ab47090f9  reports/round-34/run-validation.py
46e55b803dbb0b2b1f42ea9ef06617b98000336297510624016457e6f694ce63  Ca02's replay copy (adapted ROOT; Ca02 §Protocol 3)
4a7aede22cd8395b01ce6dd9f46bcae364ca24e4                          r34 close commit (K02 §4; Ca02 §Protocol 1)
```

**Cross-check PASS:** the two declaration digests equal
`telemetry/dispatch-declared.json` `durable_sources` (`73347e55…`, `f696833e…`) — the filed
dispatch record is bound to the same bytes this seat read. The r34 runner digest equals the filed
`runner_sha256` (`reports/round-34/validation.json:196`) and is unchanged live↔close-commit
(K02 §4, Ca02 §Protocol 2).

**Before-state of claim C, first-hand and green** (all three counters measured by this seat):

```
$ ls corpus/knowledge/verification/*.md | wc -l          → 20
$ find corpus/knowledge -name '*.md' | wc -l (per dir)   → civilizations 94, culture-material 25,
                                                           linguistics 21, myth-symbol 23,
                                                           synthesis 29, verification 20 (= 212)
$ python3 -B reports/round-28/readme/sweep.py            → exit 0; rows 212 files 212;
  missing_from_index 0; topic_mismatch 0; orphan_rows 0; header_drift {}; totals_line 212 ok;
  footer {total 212, dir_totals [21,23,25,29,20,94]}; readme_sha256 b80274bc…
```

This confirms `claims.json:14` (verification 20, total 212) and K01 §1 / X00 §0 independently.
C06's target vector `21/23/25/29/24/94` is in the sweep's own section order — only the fifth slot
(verification) moves 20 → 24 (`reports/round-28/readme/sweep.py:50-57`; X00 §0).

**Canon.** NON-CANON engineering evidence. A digest is integrity, never truth, and never clearance.

---

## §2 — Declaration facts, measured

### §2.1 Schema and identity

`claims.json` carries exactly these 12 keys: `round`, `regimen`, `loop`, `position`,
`declared_at_utc`, `baseline_commit`, `dispatch`, `axes_in_play`, `lowest_axis_reasoning`,
`freshness_pause_in_force`, `claims`, `non_goals`. The declared baseline token is `dfb0719`
(`:7`) and resolves to the live HEAD (§1). `axes_in_play` is `["coverage", "calibration"]`
(`:9`) and the two claim objects are exactly `{C: coverage, Ca: calibration}` (`:13-24`) —
distinct axes; `lowest_axis_reasoning` names coverage least-claimed (2), calibration follows (3),
depth resting after r38 (`:10`). `freshness_pause_in_force: true` (`:11`) and `non_goals[0]` is
*"no freshness axis-move"* (`:26`); `non_goals` also forbids filed byte rewrites, in-tree
round-runner execution, and any re-freeze of declared-in-r7 (`:26-27`).

### §2.2 Dispatch honesty

Declared allocation: `zai-coding-plan / glm-5.3-flash`, 16 requested workers, 1 batched call
(`claims.json:8`; `telemetry/dispatch-declared.json` allocation block). `REGIMEN.md:17` (schedule
row 7–8) declares "zai-coding-plan / glm-5.3-flash MAX-effort seats | 16–32 | build" — **16 is the
range floor, so the allocation is in-contract**; no fallback clause is needed and none is invoked.
Contrast round 38, whose lane died 403 at launch: nothing in the round-39 telemetry names any
launch failure. The observed launch/completion/failure counters for this batch are **unknown to
this seat** (workers do not see the orchestrator's dispatch stream): they are `null` with owner
`orchestrator (goal-mode parent)` until an `observed-dispatch.json` or the closing snapshot lands —
never inferred zeroes, never a claimed completion rate (`AGENTS.md:15-31`). The telemetry record's
`closing_snapshot` field reads `open-at-seat-close: owed once validation.json lands`.

### §2.3 Seat census (reported as a measurement, never as launches)

```
seat_count 16   rows 16   unique ids 16   unique out paths 16   duplicates []
claims {C: 6, Ca: 6, cross: 4}
roles  {executor: 7, verifier: 3, scout: 2, scribe: 1, reviewer: 1, planner: 1, connector: 1}
dirs   {cov: 6, calib: 6, scout: 2, plan: 1, cross: 1, review: 1, scribe: 1}
```

**No undeclared claim block this round** (contrast r38's A block): the seat census's claim values
`{C, Ca, cross}` are exactly `claims.json`'s two claims plus the `cross` convention used by
planner/connector/reviewer/scribe seats in every prior round. No `baseline_expanded` key exists,
so the r36 Trap 1 does not repeat.

**Landed at this dossier's finalization (6/16):** `scout/K01-verification-gaps.md`,
`scout/K02-isolation.md`, `cov/C01-entry-1.md`, `cov/C02-entry-2.md`,
`calib/Ca02-replay-verify.md`, `cross/X00-connector.md`.
**Absent (10):** `plan/P01-plan.md`, `cov/C03-entry-3.md`, `cov/C04-entry-4.md`,
`cov/C05-audit.md`, `cov/C06-delta-receipt.md`, `calib/Ca01-protocol.md`,
`calib/Ca03-basename-policy.md`, `calib/Ca04-verify.md`, `review/R01-review.md`, and this file.
**Recompute, never trust this list** (§12). The absences that bind:
`Ca01-protocol.md` — Ca02 explicitly replayed **before** the protocol existed, applying the
mechanics declared in `claims.json:21` and pinning what ran (`Ca02-replay-verify.md ## Owed`);
`Ca03`/`Ca04` — the basename policy half of claim Ca(b)-adjacent work is entirely unexecuted at my
cut; `C05` — no audit exists, so no entry draft is audited yet and claim C's own threshold
("entries audited before landing", `claims.json:18`) is unmet for all four.

### §2.4 The C-block topic deviation from K01's recommendations (named, not smoothed)

K01 recommended four topics (G1 contact-strata, G2 taboo-euphemism, G3 dialect-register, G4
translation-protocol fidelity; `K01 §4`). The two landed executors chose **different topics**, each
with its own measured gap-absence sweep:

- **C01 — worked-examples verification gate:** 22 files carry NON-CANON, 18 carry the phrase
  "worked example", 20 entries carry a dedicated example/fixture section under ≥12 headings;
  absence probes ("example audit", "example gate", …) → 0 files each; near-misses dispositioned
  line-by-line (`C01-entry-1.md` `- gap filled:`).
- **C02 — corpus-index-sweep verification:** `grep -rliE "index sweep|counts footer|totals
  line|header drift|ghost row|orphan row|duplicate row" corpus/knowledge/` → **0 files**; false
  friends dispositioned (`C02-entry-2.md` `- gap filled:`).

The missions bind only "Author entry N with the same contract" (`targets.json` C01–C04 rows) —
no topic binding — so this is **permitted, not a defect**; but it means X00-1's allocation race
resolved by executors self-allocating, K01's §4 list is **not** the allocator of record, and the
integrator's pre-apply uniqueness check (§6.2 C3) is the only control left. My own re-sweeps agree
the two chosen topics are real gaps: "worked example" has no dedicated entry among the 20 (2
incidental files: `verification-method-overview.md`, `gate-frozen-run-standard.md` — both
dispositioned as near-misses by C01); "sweep" hits 11 files, all incidental mentions inside other
procedures (file list in this seat's transcript). Whether C03/C04 pick K01 topics or fresh ones,
the same check applies, and K01's G1–G4 remain the scouted gap set if any executor wants them.

---

## §3 — Landed-fragment cross-check: the measurements every block agrees on

### §3.1 Premises (three or more seats, no coordination)

| premise | sources |
|---|---|
| verification partition = 20, corpus = 212, sweep green, footer vector [21,23,25,29,20,94] | K01 §1, X00 §0, this seat §1 — **converges** |
| the four c-n-r rows are exactly R37-Ca-05..08, all `python3 reports/round-34/run-validation.py`, groups C/D/O/cross, filed cause = absolute-root chdir | ledger `:60-111,451-455`; K02 §2; X00 §3; Ca02 verdict — **converges** |
| the O12 mechanism: absolute `ROOT` + import-time `os.chdir` escapes any copy; `--check` measures the live tree because the chdir precedes flag parsing; publish mode is the clobber path with `REFRESH_RECEIPTS=1` defeating the guard | K02 §1; X00 §3; Ca02 Run 1 (live demonstration: the D4 tamper probe wrote into the **live tree**, removed after); `reports/round-34/run-validation.py:10,26,522-538` — **converges** |
| "the resolver" for couples references is **two audit instruments** (`reports/round-35/cov/C14-audit-6-10.md:239-288`, `reports/round-19/audit/entry-audit.py:74-96`), not a production module; A12 measured 334 tokens = 319 path-resolved + 15 basename-only, 0 ambiguous, all 15 from `sacred-kingship-mythic-charter.md:37` | X00 §4; queue row `basename-couples-policy` (`defect-queue.json:202-211`); `reports/round-37/adj/A12-gap-fill.md:9-26` — **converges** |
| `corpus/README.md` carries a duplicated H1 (lines 1 and 3) | X00-7, this seat (`grep -c '^# kotodama-shokunin corpus index'` → **2**) — **converges**; X00's do-not-touch ruling stands: not this round's defect, must not be silently repaired inside the rev-2.2 delta |

### §3.2 Filed-runner isolation census (this seat's measurement; extends K02)

Of the **33** filed runners (`ls reports/round-*/run-validation.py | wc -l` → 33; r13 never
dispatched):

```
ABSOLUTE  5  : reports/round-{34,35,36,37,38}/run-validation.py  (ROOT = "/home/vgpnk/…" literal)
RELATIVE 27  : r5–r12, r14–r18, r20–r33                        (Path(__file__).resolve-based)
OTHER     1  : r19 (no ROOT constant and no Path-resolve in its first 14 lines — shape unclassified)
```

All five absolute runners also carry an `os.chdir(ROOT)` at import, and all five expose `--check`
(r34 `:522-531`, r35 `:492-508`, r36 `:256-264`, r37 `:226`, r38 `:228`); r38 additionally routes
its default path through `guard_receipt()` (`:218-233`). **This is the protocol's true scope
surface** — Ca01's document should name all five (K02 §1 names three), and the four r37 rows
happen to target only one of them (r34). Note the revision boundary: the census moves 33 → **34**
when the round-39 runner lands; r34's runner pins a runner census of 29
(`reports/round-34/run-validation.py:209-211`, already red at 30+ by design) while r38's pins
none — so no *new* filed runner reddens, but the successor ledger and the r39 runner must read
**digests**, never re-computed historical verdicts.

### §3.3 The replay result and its mechanism (the round's crux, restated precisely)

Ca02's Run 2: worktree at `4a7aede` (r34 close), replay copy with exactly one line changed
(`ROOT = os.getcwd()`, diff `10c10`, pristine `be11ff46…` → copy `46e55b80…`), `--check` from the
worktree root with isolated TMPDIR → rc=0; all legs green; **normalized diff vs the filed receipt
IDENTICAL** (only `measured_at_utc` and the X1-X3 pending-manifest note differ, both explained,
`Ca02 ## Run 2`). Run 1 (negative control): the **unmodified** runner from the worktree escaped to
the live tree exactly as O12 predicts — one census failure (33 live runners vs close-time 29) and
a live-tree scratch write as mechanical proof.

What this settles: the four rows' *filed results* are reproducible at the close commit; the r37
c-n-r dispositions are not sustained; the hazard is real and mechanically demonstrated. What it
leaves open (§6.3 Ca5): whether `reproduced-under-protocol` may be recorded on an
adapted-source replay when filed precedent (r37) refused to count exactly that shape. K02 §2
adds the split-history fact the successor ledger must carry regardless: Ca08's r37 bwrap run
already covers C/D on unmodified source; **r34 O and cross had never been safely replayed before
Ca02's run** (`Ca08-verify.md:27,32`) — Ca02's Run 2 is the first all-four-groups reproduction,
and its fleet-root inputs (`FLEET_REPORT`, `MANIFEST`) were read from the **live** fleet root, a
recorded fidelity limit (`Ca02 ## Fidelity limits`).

---

## §4 — Fleet-report draft for `.ufo/reports/round-39/kotodama.md`

The fleet root is `/home/vgpnk/Projects/shokunin/.ufo/`; `ls .ufo/reports/round-39/` → *No such
file or directory* (parent-owed). The four required headings are the tuple the filed runners check
(`reports/round-36/run-validation.py:319`; the r37/r38 runners' `SECTIONS`) and match the landed
`reports/round-38/kotodama.md`. Use them **verbatim**. Everything below is drafted from the
6/16 landed set — **the integrator must re-derive each sentence from the 16/16 set and the
close-time tree**, and strike or rewrite any line a later fragment falsifies.

### Draft header

```text
# kotodama — round 39 report (2026-10-19)

Regimen 2 (`REGIMEN.md:17`), loop 1, position 7 — the first zai-coding-plan build round.
Declared allocation `zai-coding-plan / glm-5.3-flash` (MAX-effort seats), 16 requested
workers, one batched AgentSwarm (`claims.json:8`; `telemetry/dispatch-declared.json`) — 16
is within the row's declared 16–32 range; no fallback declared and none invoked. Declared
baseline `dfb0719` (`claims.json:7`) =
`dfb0719711204b5943432034bd80c8dc248acddd` (the r38 admission commit).
Claims C/Ca on coverage/calibration (`claims.json:13-24`); freshness axis-move claims stay
paused (`claims.json:11`). Observed launch/completion counters: per the closing snapshot
(availability-close-39.json) — never inferred at seat time. Seat accounting: `seat_count:
16`, 16 rows, 16 unique out paths (measured, `scribe/S01-integration-draft.md` §2.3).
Dispatch honesty: allocation declared and digest-pinned (durable_sources 73347e55… /
f696833e…); the round is not admitted to LOG.md while the closing snapshot is owed.
```

### Draft — Work performed

```text
- **Coverage (claim C):** the declared target is the verification partition, the thinnest
  after r35/r36 (20 entries; closed to additions since round 19 — K01 §1 traces the
  add-history by git). Before-state measured at dfb0719: partition 20, corpus 212, README
  rev 2.1, sweep green 212/212. K01 inventoried all 20 entries, swept seven absence probes
  (translation-note strongest at 0 files), recommended four gap-named topics with
  already-registered sources, and supplied the round-35/36 entry contract. Executors C01/C02
  landed drafts on two gap-named topics of their own (worked-examples verification;
  corpus-index-sweep verification), each carrying its own measured absence sweep and
  line-by-line near-miss dispositions — a named deviation from K01's recommendation list,
  permitted by the missions, controlled by the integrator's pre-apply uniqueness check.
  C03/C04, the C05 audit, and the C06 README rev-2.2 delta had not landed at this report's
  source dossier's cut; whether all four entries + delta + audit + sweep-green verify is
  recorded by `reports/round-39/validation.json`, not asserted here.
- **Calibration (claim Ca):** three sub-moves. (a) Protocol: Ca01's isolation-replay
  protocol addresses O12 (`O12-runner-isolation-hazard`, defect-queue.json:192-201) —
  [status at close: landed/absent per validation.json]. (b) Replay: Ca02 verified the
  protocol mechanics against the filed r34 runner at its close commit 4a7aede in a git
  worktree — Run 1 demonstrated the escape live (unmodified runner measured the live tree,
  wrote one scratch probe into it, removed); Run 2 reproduced the filed receipt
  normalized-identical with a digest-pinned one-line relative-root adaptation
  (46e55b80…), turning all four r37 could-not-reproduce rows (R37-Ca-05..08) into
  reproduced-under-protocol candidates; the r37 ledger itself stays filed and untouched
  (sha 73d2d48d…) — the redisposition lands in a NEW successor ledger. Mechanism
  adjudication (adapted-copy vs unmodified-bwrap) recorded per the runner's legs, not
  smoothed. (c) Basename policy: Ca03/Ca04 document and verify the couples-reference
  resolution order + unique-basename fallback as policy — [status at close].
- **Cross:** X00's collision matrix (four apply-time collisions; integration order);
  this dossier's fleet-report material, validation-leg spec and the filed-runner isolation
  census (five absolute-ROOT runners, not three — the r37/r38 runners re-carried the O12
  shape; the r39 runner must clone r33's relative ROOT).
```

### Draft — Landed changes

```text
- At the source dossier's cut: **no claim artifact landed.** `git diff --name-status
  dfb0719` → empty; untracked rows all `?? reports/round-39/…`. The C deliverables exist
  only as fenced drafts (C01/C02 landed, C03/C04/C05/C06 pending); the Ca deliverables as
  one verifier fragment (Ca02) plus owed canonical copies. Corpus/knowledge/verification:
  still 20 files; corpus/README.md: still revision 2.1 (b80274bc…).
- If the integrator applies the drafts, the landed set is: four new
  `corpus/knowledge/verification/*.md` entries (names per the drafts, unique vs the 20
  existing), one `corpus/README.md` revision 2.2 (header 24, four filename-ordered
  byte-equal `- topic:` rows, totals 216, footer 216 + 21/23/25/29/24/94),
  `reports/round-39/calib/isolation-replay-protocol.md` and
  `reports/round-39/calib/basename-couples-policy.md` (digest-pinned copies of Ca01/Ca03's
  out paths), one NEW successor recount ledger, and the round's own runner + receipt.
  Filed bytes: zero moves anywhere (`reports/round-1..38/**`, `corpus/lessons/*.md`,
  `tools/gates/frozen/**`, fleet `.ufo/**`, and the r7 freeze set) — asserted by the
  runner's digest sweep, not by this prose.
- The round's evidence artifacts (16 seat fragments) are evidence, not product changes.
```

### Draft — Before → after measurements

Fill from §6's leg table at close. Every after-value names the fragment/leg that measured it
and the counting command; the before-values are this seat's §1 measurements.

| axis | before (measured at `dfb0719`) | after required (`claims.json`) | status at my cut |
|---|---|---|---|
| coverage (C) | verification 20; total 212; README rev 2.1; sweep green 212/212; footer [21,23,25,29,20,94] | verification 24, total 216; README rev 2.2 sweep-green (216 rows == 216 files); entries audited before landing | **not landed** — 2/4 entry drafts + no audit + no delta |
| calibration (Ca) | 4 c-n-r rows in the r37 ledger (the O12 hazard demonstrated live by Ca02 Run 1); the basename fallback undocumented (queue row, `verification: null`) | protocol durable at `calib/isolation-replay-protocol.md`; the 4 rows re-dispositioned in a successor ledger with evidence; the basename policy documented at `calib/basename-couples-policy.md`; replay-verified by an independent seat; zero filed byte edits | **half-landed** — replay evidence on file (Ca02), protocol + successor ledger + policy + policy-verify owed |
| cross | runner absent; 10/16 outputs absent; fleet report / MANIFEST row / LOG entry / SCORECARD row absent (all measured 0/absent) | runner + receipt; report with 4 headings; MANIFEST/SCORECARD/LOG rows; telemetry closed by a digest-pinned snapshot | **owed** (§8, §9) |

### Draft — SHONEN

```text
No SHONEN box was re-surveyed by this round, and no fragment in this round establishes a new
end-to-end domain-task result. Carry the prior status only as *last recorded*, not as a
round-39 re-verification: `reports/round-36/scribe/S01-integration-draft.md:248-267` records
boxes 1–4 as `verified-with-conditions` (with the box-1 citation conditions, the box-2 D4
garment/RL-3/head2 debts, the box-3 N1/N4/N5/N7 items and the box-4 standing readings), and
rounds 37/38 landed no box change. Round-39 findings do not alter those records. No promotion
decision is taken or implied; the decision remains operator-owned (`SHONEN.md:10-11`).
```

---

## §5 — The round-39 runner: constants that must NOT be inherited

Cloning the most recent runner (`reports/round-38/run-validation.py`) produces a runner that
**re-carries the O12 hazard**. Every inherited constant that is wrong for r39, with the measured
replacement:

| r38 constant / path | r38 value | round-39 value | evidence |
|---|---|---|---|
| `ROOT` | **absolute literal + `os.chdir(ROOT)`** (`:5,:11`) — the O12 shape | **relative**: `ROOT = Path(__file__).resolve().parents[2]` (the r33 shape, `reports/round-33/run-validation.py:23`) | §3.2 census; §0 item 4; r38's own ruling (`X01-trades.md:367-369`) |
| `ROUND` / `COMMAND` | `reports/round-38` / `python3 reports/round-38/run-validation.py` | `reports/round-39` / `python3 reports/round-39/run-validation.py` | `claims.json:23` |
| `BASELINE` | `9bccc9b` | `dfb0719` → `dfb0719711204b5943432034bd80c8dc248acddd` | §1 |
| seat count | 32 | **16** | `targets.json:3`, measured §2.3 |
| `claims_declared` | `{D: depth, O: operability}` | `{C: coverage, Ca: calibration}` | `claims.json:13-24` |
| r7 sha pin | `45f57132…` (r7 packet) | keep as a **regression** leg only (zero freeze bytes moved is a non_goal, `claims.json:26-27`) | X00 §2 red lines |
| calibration input | `op/defect-queue.json` (r37) / none (r38) | **new**: the successor ledger + the two canonical calib copies + Ca02's evidence pins | `claims.json:22` |
| coverage input | none | **new**: partition count, sweep exit/footers, README digest + rev-2.2 fields, C05 audit presence | `claims.json:16-18` |
| fleet report path | `…/.ufo/reports/round-38/kotodama.md` (landed) | `…/.ufo/reports/round-39/kotodama.md` (absent at my cut) | §4 |
| closing snapshot | `availability-close-38.json` | `availability-close-39.json` (the landed naming convention) | §9 |
| mode surfaces | `--check` at `:228`; guard at `:218-233` | keep `--check` print-only; keep the guard; **parse flags before any chdir** (r33 does this implicitly by never chdiring to a literal) | K02 §1 mode ordering |

**The `ROOT` line is the load-bearing one.** Five filed runners carry the absolute shape and the
r36 in-tree incident (`LOG.md` round-36 entry; `reports/round-36/scribe/S01-integration-draft.md
§0.2`) is its realized cost. A relative-ROOT r39 runner makes the F-C13-1 rule mechanically
enforceable for this round's own artifact instead of promissory.

---

## §6 — Validation-leg spec (machine-checkable)

Format: `id | claim | check | expected`. Every leg is written so it is true and useful whether or
not the integrator applies the drafts — where an after-state does not exist, the leg records
`could-not-evaluate` rather than passing, and no `could-not-evaluate` counts toward acceptance.

### §6.1 Coherence / schema / declaration legs (cross)

| ID | check | expected |
|---|---|---|
| **CO1** | strict-parse `claims.json`, `targets.json`, `telemetry/dispatch-declared.json` (duplicate keys refused); `round == 39` in all three; `baseline_commit == "dfb0719"`; `git rev-parse --verify dfb0719^{commit}` → `dfb0719711204b5943432034bd80c8dc248acddd`; record declared token and resolved id separately | pass |
| **CO2** | `{c.id: c.axis}` == `{"C": "coverage", "Ca": "calibration"}`; `set(axes_in_play) == {"coverage","calibration"}`; axes distinct; `freshness_pause_in_force is True`; `"freshness"` absent from every claim axis; `non_goals` contains the no-freshness, no-filed-rewrite, no-in-tree-runner, no-re-freeze items (`claims.json:26-27`) | pass |
| **CO3** | seat census: `len(seats) == 16 == seat_count`; 16 unique ids; 16 unique `out` paths, all under `reports/round-39/`; every id/role/mission non-empty; report the claim/role/dir vectors (§2.3) as the measurement | pass |
| **CO4** | declared-output completeness: the 16 `out` paths exist at close, and any absent one is named in `missing_dependencies` with owner — an empty `missing_dependencies` over an incomplete wave is the false green this leg exists to catch | pass |
| **CO5** | dispatch shape: assert the declared allocation exactly (`zai-coding-plan`, `glm-5.3-flash`, 16 requested, 1 batched call) across `claims.json:8` and `dispatch-declared.json`; assert 16 is within `REGIMEN.md:17`'s declared 16–32 (record the range, not just the number); `durable_sources` digests equal the live declaration bytes (`73347e55…`, `f696833e…`) | pass |
| **CO6** | observed dispatch: if `observed-dispatch.json` or the closing snapshot exists, keep requested allocation and observed launches/completions/failures as **separate fields**; if not, record each counter `null` with owner `orchestrator (goal-mode parent)` + reason. Never infer zeroes; provider liveness is not round acceptance | pass / could-not-evaluate |
| **CO7** | protected-tree census: enumerate with `git ls-tree -r --name-only dfb0719…` plus a regex walk (`reports/round-(?:[1-9]|[12][0-9]|3[0-8])/`, `corpus/lessons/(?!README)`, `tools/gates/frozen/round-`, `reports/round-34/handoff/declared-in-r7/`), comparing live bytes to `git show dfb0719…:<path>` digests. **Never** a literal `reports/round-1..38` pathspec (git treats it as literal — the dead check, r38 dossier §3.4) | pass |
| **CO8** | runner census / revision boundary: `ls reports/round-*/run-validation.py \| wc -l` → 34 at close (33 + this round's); record the count and the digest of every filed `reports/round-*/validation.json`; assert **digests**, never re-computed verdicts; a count change is a revision boundary, not a failure | pass |
| **CO9** | godspeed lead: not machine-checkable from durable artifacts (prompts not persisted; `AGENTS.md:30-31` forbids private prompt payloads in telemetry) → `could-not-evaluate` with owner `orchestrator`, `dispatch-declared.json` the only evidence. Never scored as passed from absence of evidence | could-not-evaluate |
| **CO10** | regression floor: the r28 sweep exits 0 pre-apply (212/212) **and** post-apply (216/216) as §8's ordering runs it; the §1 digest block is unmoved across the run | pass |

### §6.2 Claim-C legs (coverage: the verification partition)

| ID | check | expected |
|---|---|---|
| **C1** | **before-state pins** (binding): partition `ls corpus/knowledge/verification/*.md \| wc -l` → 20 pre-apply / 24 post-apply; `find corpus/knowledge -name '*.md'` per-dir → 94/25/21/23/29/20 pre / 94/25/21/23/**24**/94 post (total 212 → 216); record both so the delta is visible | pass |
| **C2** | the four entries exist, each with the round-35/36 contract: H1 + `- topic:` / `- gap filled:` / `- sources:` (numbered, locators) / `- calibration:` / `- couples:` / `- source:` / `- verified-at:` / `- recheck:` (contract exemplar: `corpus/knowledge/verification/gate-battery-surface-verification.md:1-18,75-82` via K01 §5), plus a gap statement and a numbered decision record in the body | pass / failed |
| **C3** | **uniqueness + audit ordering** (claim's own threshold, `claims.json:18` "entries audited before landing"): C05's audit exists, is clean or names defects, and **predates or is cited by** the landing record; the four filenames are unique vs each other and vs the 20 existing entries; the four topics are disjoint (the X00-1 control — C01/C02's self-allocated topics make this non-vacuous). Record the K01-recommendation deviation as a note, not a failure | pass / failed |
| **C4** | **source-pointer resolution**: every `- sources:` locator and in-body file cite resolves (the C05 runbook's source-pointer sweep); external sources are already-registered in-corpus entries (K01 §4 policy: no new bibliography); unresolved pointers are named defects, not silent | pass / failed |
| **C5** | **README rev-2.2 delta, byte-level**: `## verification/` header 20 → 24; exactly 4 new rows in filename order; each row's `- topic:` text **byte-equal** to its entry's own (sweep `topic_mismatch` would catch drift); totals line 212 → 216; footer total 216, vector `21/23/25/29/**24**/94` (fifth slot only); a new revision-2.2 block on top; footer date = the re-measure date | pass / failed |
| **C6** | **the sweep is green on the LANDED tree**: `python3 -B reports/round-28/readme/sweep.py` → exit 0, rows 216 files 216, 0 missing/ghost/mismatch/drift — run **after** entries+README both land (an intermediate sweep reds by construction; X00 §2 row 2); plus `diff` landed README vs C06's draft — the r35 placeholder lesson (`__E3_PLACEHOLDER__` repair, LOG r37) and the r36 staged-prediction divergence (queue row `readme-prediction-vs-delivery`) both say verify landed bytes | pass |
| **C7** | **do-not-touch held**: the README's duplicated H1 (lines 1 and 3) is **not** repaired inside the rev-2.2 delta (X00-7); no other `corpus/` byte beyond the 4 entries + README moved (CO7's census covers it) | pass |
| **C8** | **corpus lessons gate untouched**: `corpus/lessons/*.md` count still 33 with digests unmoved (the corpus surface the round must not edit) | pass |

### §6.3 Claim-Ca legs (calibration: replay protocol, redisposition, basename policy)

| ID | check | expected |
|---|---|---|
| **Ca1** | **protocol durable at the canonical path**: `reports/round-39/calib/isolation-replay-protocol.md` exists; it is a byte-identical, digest-pinned copy of `calib/Ca01-protocol.md` when that lands (both digests recorded); content covers the four declared mechanics (worktree at close commit, relative-root requirement, TMPDIR isolation, step-by-step replay recipe) **and** the protocol-design decisions K02 §4 items 1–4 force (substrate/worktree-vs-namespace reconciliation, `--check`-only rule, unmodified-source policy, fleet-input policy) and cites the canonical queue id `O12-runner-isolation-hazard` exactly once as the hazard (X00-4 dedupe) | pass / failed |
| **Ca2** | **the four rows redispositioned in a NEW successor ledger** (filename integrator-chosen and recorded; X00 suggests `recount-ledger-successor.json`): one successor row per R37-Ca-05..08, each with `reproduced-under-protocol` or `confirmed-could-not-reproduce` + owner + evidence path; the Ca08 C/D namespace evidence carried forward (K02 §2), not discarded; **the filed r37 ledger untouched** — its digest still `73d2d48d…` and its 4 rows byte-unchanged, gaining at most nothing (no pointer edits in filed bytes; the pointer lives in the successor and the round record) | pass / failed |
| **Ca3** | **replay evidence is durable**: Ca02's fragment carries the worktree pin (`4a7aede22cd8395b01ce6dd9f46bcae364ca24e4`), the pristine/copy digests (`be11ff46…` / `46e55b80…`), the rc=0, the normalized-identical verdict, and the Run 1 escape demonstration; the runner records these as the replay legs' evidence, and its own run does **not** re-execute any r34 runner in-tree | pass |
| **Ca4** | **zero filed byte edits** (claim threshold, `claims.json:24`): CO7's digest sweep is empty over every protected surface; specifically the r34 receipt still hashes `ba2fa4dcf8f29a136f6de3f6d03914de34d5c0354785c42e665c1c9d8838e08a` (K02 §4) and `reports/round-34/handoff/declared-in-r7/**` is byte-identical | pass |
| **Ca5** | **the mechanism adjudication, recorded not smoothed**: the receipt names which replay mechanism produced the counted reproduction — (i) Ca02's digest-pinned adapted copy (one-line `ROOT = os.getcwd()`), or (ii) an unmodified-source bwrap bind-over — and states the integrator's ruling on whether (i) satisfies `reproduced-under-protocol` given `claims.json:21` declares the relative-root requirement as protocol content while r37 precedent excluded altered-ROOT runs (`Ca02-r34.md:20`; `P01-ca-plan.md:19-24` via `Ca02-r34.md:18`). R01's review is the named adversarial input. Disposition (ii)-or-`confirmed-could-not-reproduce`-with-owner both satisfy claim Ca(b) as declared; **a green leg must not imply (ii) happened when (i) is what ran** | pass-with-recorded-ruling |
| **Ca6** | **basename policy durable at the canonical path**: `reports/round-39/calib/basename-couples-policy.md` exists (digest-pinned copy of `calib/Ca03-basename-policy.md`); content codifies: the resolution order (entry dir → repo root → `corpus/knowledge/` → unique-basename fallback), the fallback's uniqueness + group-alignment limits, its non-guarantees (existence and group alignment only, never content quality), the measured population (334 tokens = 319 path + 15 basename-only, 0 ambiguous, all 15 from `sacred-kingship-mythic-charter.md:37`), and the scope fact that the resolver is the two audit instruments (`reports/round-35/cov/C14-audit-6-10.md:239-288`, `reports/round-19/audit/entry-audit.py:74-96`), not a production module | pass / failed |
| **Ca7** | **policy verified**: `calib/Ca04-verify.md` exists and its verification of Ca03 against the resolver instruments + A12's cross-check is folded (agreements recorded; disagreements filed, never absorbed); the queue row's `verification: null` (`defect-queue.json:210`) is superseded **only** by new round-39 records, never by editing the filed queue | pass / failed |
| **Ca8** | **cross-block coupling holds**: the four new entries' `- couples:` references are path-resolvable or uniquely-basename (X00 §2 coupling note; C01 reports all 24 of its in-repo couples targets resolving by script) — the entries must not *depend* on the undocumented fallback Ca03 is documenting | pass / to-verify |

### §6.4 Cross / close legs

| ID | check | expected |
|---|---|---|
| **X1** | fleet report at `/home/vgpnk/Projects/shokunin/.ufo/reports/round-39/kotodama.md` with all four headings verbatim, an ISO date, and a citation of `reports/round-39/run-validation.py`. Outside this repo → integrator writes | pass / owed |
| **X2** | MANIFEST: a round-39 entry in the fleet-root `MANIFEST.json` `rounds[]` with a kotodama lane pointer. Measured at my cut: `grep -c '"round": 39'` → **0** (the r38 row exists: count 1). Absent → `pending-by-construction`, owner integrator | pass / owed |
| **X3** | telemetry: `dispatch-declared.json` `durable_sources` equal live bytes (**verified true**, §1); `observed-dispatch.json` exists **or** owed with owner+reason; **`availability-close-39.json`** exists **or** owed — schema `kotodama-availability-closing-snapshot-v1`, naming `closes` = the dispatch record and `closes_sha256` = `1b21ed5b…` at close time. The round is **not admitted to LOG.md while the closing snapshot is owed** (`AGENTS.md` close-what-you-open) | pass / owed |
| **X4** | receipt self-consistency: `round == 39`, exact `counting_command` strings from `claims.json:17,23`, `baseline_revision == "dfb0719"`, per-claim measurements present, `limits` non-empty, `missing_dependencies` ⊇ absent declared outputs, and `acceptance_checks_passed` true only if every leg is green (no `could-not-evaluate` counted as a pass) | pass |
| **X5** | language scan over every `reports/round-39/**` file: zero unadjudicated grant/completion frames; every declared seat `out` path present in the scan including absent ones, named as absent | pass |
| **X6** | SCORECARD/LOG: a round-39 SCORECARD row with per-axis verdicts (measured absent: `grep -c "round-39"` → 0) and an append-only LOG entry under the lane identity (measured: `grep -c "Round 39" LOG.md` → 0) — integrator-only writes, listed owed | pass / owed |

---

## §7 — The non-vacuous test each claim must survive

Each row is a test that **fails today** and passes only if the claim's substance lands.

| # | claim | test that is not vacuous | why a green reading fails today |
|---|---|---|---|
| 1 | C / partition | `ls corpus/knowledge/verification/*.md \| wc -l` → **24** | 20 at baseline (measured §1); the partition has been closed since r19 (K01 §1) |
| 2 | C / README | sweep exit 0 at **216 rows == 216 files** with footer `[…,24,…]` | green at 212/212 today; an entries-without-rows or rows-without-entries intermediate state reds by construction |
| 3 | C / row byte-equality | each new row's `- topic:` == its entry's own text | the sweep's `topic_mismatch` leg is the only instrument that catches paraphrase (the r19 lesson C02 documents) |
| 4 | C / audit ordering | C05's audit exists and precedes/cites the landing | `cov/C05-audit.md` absent at my cut; the claim's own threshold is unmet for all four drafts |
| 5 | Ca / protocol | `calib/isolation-replay-protocol.md` exists and cites the canonical `O12-runner-isolation-hazard` id | absent; the queue row's `verification` is `null` |
| 6 | Ca / redisposition | a NEW successor ledger carries 4 non-c-n-r dispositions **and** the r37 ledger's digest is still `73d2d48d…` | the filed ledger still reads 4 × could-not-reproduce (`:451-455`) — a green that edited filed bytes would fail Ca4 instead |
| 7 | Ca / replay | the counted reproduction is durable: worktree at `4a7aede`, `--check`-mode, digests pinned, normalized-identical | before Ca02, r34 O/cross had **never** been reproduced anywhere (Ca08 covered C/D only) |
| 8 | Ca / policy | `calib/basename-couples-policy.md` exists and Ca04's verification is folded | absent; the fallback is still undocumented policy (queue `:202-211`) |
| 9 | runner | `reports/round-39/run-validation.py` exists, carries the **relative** ROOT, and passes in an isolated copy | absent at baseline; and §3.2's census shows why "clone the last runner" fails the round |

---

## §8 — Integration order, collisions, owed rows

**Ordering** (X00 §5.1 is the matrix of record; this seat concurs and adds two pins):

1. Census the wave (16/16 outs; headers well-formed). Recompute §2.3 — do not trust either of
   this dossier's counts.
2. **C-block first, in this order:** C05's audit clean → apply the 4 entries (pre-check
   filename+topic uniqueness vs each other and vs the 20 existing — the X00-1 control, now
   non-vacuous because C01/C02 self-allocated) → apply C06's README rev-2.2 delta in the **same
   motion** → run the sweep on the landed tree (216/216) → diff landed README vs draft.
3. **Ca-block (independent of 2):** copy Ca01 → `calib/isolation-replay-protocol.md` and Ca03 →
   `calib/basename-couples-policy.md`, digests pinned both sides; fold Ca02's evidence into the
   NEW successor ledger (r37 ledger untouched, `73d2d48d…`); fold Ca04's verification; record the
   Ca5 mechanism ruling.
4. Disposition R01's findings: fixed-with-evidence or routed-with-owner, never absorbed. The Ca5
   adjudication is the likely review target — rule it on the record, with the §3.3 tension stated.
5. Author `reports/round-39/run-validation.py` — **relative ROOT (§5)** — run it in an isolated
   copy only; then SCORECARD row, LOG append (lane identity), MANIFEST rounds[], fleet report.
6. File `telemetry/availability-close-39.json` (§9). The round is not admissible to LOG.md while
   it is owed.

**Collision surface.** All 16 out paths are disjoint by construction (X00 §1). Apply-time
collisions are exactly X00's four: (i) the four entries converge on one corpus surface (C5's
byte-equality chain); (ii) the replay's collision with the r34 runner's absolute chdir (Ca5's
adjudication); (iii) canonical-path ≠ out-path for both Ca copies (digest-pinned); (iv) filed-byte
immutability for the r37 ledger (successor file only). The one C↔Ca coupling: the entries'
couples references enter the surface Ca03's policy governs — leg Ca8.

**Routed ambiguities the integrator must decide, not the runner:**

- The **Ca5 mechanism ruling** (adapted-copy vs unmodified-source as the counted reproduction).
- The **successor-ledger filename** (undeclared in claims.json; pick and record).
- Whether **C03/C04** take K01's remaining topics (G1–G4 stay scouted-and-unclaimed) or their own
  gap sweeps — either is in-contract; uniqueness is the only hard control.
- The README **duplicated H1** — live defect, do-not-touch inside rev 2.2 (X00-7); needs an owner
  in a round that owns corpus-surface repair.
- The r19 runner's unclassified ROOT shape (§3.2 OTHER) — one `to-verify` for whoever next extends
  the isolation census; it does not gate this round.

---

## §9 — Telemetry material (draft pointers, not measurements)

The telemetry seat's slot (S02 in r36/r38) is **not staffed this round** — the 16-seat roster has
one scribe (this seat), so the close obligations belong to the integrator directly:

- `telemetry/dispatch-declared.json` is filed; `durable_sources` verified live (§1); its
  `closing_snapshot` field reads `open-at-seat-close: owed once validation.json lands`.
- **Owed at close** (`AGENTS.md:32-39`): an `observed-dispatch.json` (zai batch counters — `null`
  with owner + reason where unobservable) and the closing snapshot **`telemetry/availability-close-39.json`**
  (the landed naming convention: `availability-close-{19,25,26,27,28,33,34,35,36,37,38}.json` all
  exist; `closing-snapshot.json` exists nowhere), schema `kotodama-availability-closing-snapshot-v1`,
  naming `closes` = the dispatch record, `closes_sha256` = `1b21ed5b6c45db7b05f020c89450a325eb95327daef1542ff996f7bf279308a5`
  at close time, with `closed_fields`, `could_not_recover`, `sources`, owner. Keep requested
  allocation (zai/glm-5.3-flash/16) separate from observed launches/completions/failures/runtime
  concurrency/actual route; label partial observations; unknown counters stay `null` with owner and
  reason.
- Never persist credentials, authorization headers or private prompt payloads. The only route
  string in the round's declarations is the lane name `zai-coding-plan`.

---

## §10 — Language and negation posture (binding on every leg)

No leg, fragment, receipt or report in this round asserts promotion, canon, clearance or closure.
Every occurrence of those tokens must be a **negation**, a **routed reference**, or a **quoted
scanner pattern**. The legitimate shapes, all present in this file: *"No promotion decision is
taken or implied"* (§4 SHONEN draft), *"canon decisions are lore-shokunin's"*
(`AGENTS.md`; entry drafts' own closing clauses), and quoted sweep/leg names. The r34/r35 scanner's
frame rule is the contract: **token presence alone never fires; only grant/completion frames do.**

---

## §11 — Landed-fragment cross-check (folded, attributed)

**§11.1 — K01 (scout, C).** The partition's 20-entry inventory, the closed-since-r19 add-history
(git, not count), seven absence sweeps, four sourced topic recommendations (G1–G4), the entry
contract exemplar (`gate-battery-surface-verification.md:1-18,75-82`), and C06's index
implications. **Converges** with this seat's §1 before-state. **Extended by the wave**: executors
C01/C02 chose their own gap-named topics (§2.4) — K01's list remains the scouted alternative set.

**§11.2 — K02 (scout, Ca).** The O12 mechanics with mode-dependent blast radius (`--check`
measures live; publish mode is the clobber path with `REFRESH_RECEIPTS=1` defeating the guard —
`tools/harness/receipt_guard.py:7-8,144-149`), the four rows' precise citations, the r33-vs-r34/35
root contrast, and protocol design inputs §4 items 1–7. **Converges** with Ca02's Run 1 and X00
§3. **Extended by this seat**: the absolute-ROOT set is five runners (r37/r38 too, §3.2), and the
close-commit pins (r35 `ce103bf…`, r36 `57c8409…`) plus the r34 receipt digest pin (`ba2fa4dc…`)
are adopted into Ca2/Ca4.

**§11.3 — Ca02 (verifier, Ca).** The REPRODUCED verdict, the digest-pinned adapted copy, the
normalized-identical diff, the live escape demonstration, the disposition mapping, and the two
recorded fidelity limits (live fleet-root inputs; adapted-source provenance). **This fragment is
the round's calibration evidence of record**; §6.3 Ca3/Ca5 exist to land it without letting its
mechanism be overstated. Its self-declared owed items (protocol re-check; successor ledger) are
§Owed rows.

**§11.4 — C01/C02 (executors, C).** Two entry drafts, each with measured absence sweeps,
line-by-line near-miss dispositions, full head-blocks, and (C01) a script-verified couples
resolution. Content audit is **C05's job, not this dossier's**; §6.2 C2–C4 spec the checks. Their
topic deviation from K01 is recorded at §2.4 as a named fact, not a defect.

**§11.5 — X00 (connector, cross).** The collision matrix, integration order, the bwrap-feasibility
measurement (`/usr/bin/bwrap` present — this seat re-confirmed), the X00-1..7 findings, and the
baseline control block. **Converges** with §1 (sweep green, digests, runner digest). This dossier
adopts X00's ordering as the matrix of record (§8) and adds what X00's write-time could not have:
the landed-fragment facts (§2.3–§2.4), the five-runner census (§3.2), the r38-runner inheritance
trap (§5), and the full leg spec (§6).

**§11.6 — Dependency state, and it moved under this seat.** At this seat's first sample
(12:12Z) `reports/round-39/` held 5 fragment-less declarations + 4 fragments (K01, Ca02, C01,
X00); at finalization it holds 6 (+K02, C02). Ten outputs remain absent (§2.3). The absences that
bind: **Ca01** (Ca02 replayed against the declared mechanics, not an authored document — the
protocol and the applied mechanics must be reconciled or the delta recorded), **Ca03/Ca04** (the
policy half of Ca is unstarted), **C05** (no entry is audited; claim C's own threshold unmet),
**C03/C04/C06** (claim C numerically unreachable), **P01/R01** (the plan and the adversarial
review — R01 should hit §3.3/Ca5 hardest). §6.3 Ca1 is written as a **constraint on whatever
protocol lands**, not as a verification of a document this seat could read.

---

## Owed

- **`reports/round-39/run-validation.py` + `reports/round-39/validation.json`** — absent at this
  seat's cut; claim Ca's counting command (`claims.json:23`) is `to-verify` until they land. Must
  carry the **relative ROOT** (§5) and must **never** be run in-tree (F-C13-1). Owner: the round-39
  integrator.
- **Every claim artifact.** No corpus byte and no canonical calib byte has landed (§0). If the
  integrator applies the drafts, the landed set is §4's roster; until then the fleet report's
  *Landed changes* must say so plainly rather than list drafts as changes.
- **Absent fragments** (10 at cut, §2.3): `plan/P01-plan.md`; `cov/C03-entry-3.md`,
  `cov/C04-entry-4.md`, `cov/C05-audit.md`, `cov/C06-delta-receipt.md`; `calib/Ca01-protocol.md`,
  `calib/Ca03-basename-policy.md`, `calib/Ca04-verify.md`; `review/R01-review.md`; this file's own
  write closes the scribe slot.
- **Canonical copies + successor ledger** — `calib/isolation-replay-protocol.md`,
  `calib/basename-couples-policy.md`, and the redisposition ledger (filename integrator-chosen),
  each digest-pinned; the filed r37 ledger stays at `73d2d48d…`. Owner: integrator.
- **The Ca5 mechanism ruling** — integrator decision with R01's review as adversarial input;
  recorded in the receipt, never smoothed.
- **Telemetry close** — `observed-dispatch.json` (or null-fields with owner) and
  `availability-close-39.json`; the round is not admissible to LOG.md while owed. Owner:
  integrator.
- **`../.ufo/reports/round-39/kotodama.md`** (§4 draft), the fleet-root MANIFEST round-39 row
  (measured 0), the SCORECARD round-39 row (measured absent), the LOG.md entry (measured 0) —
  integrator-only writes.
- **`corpus/README.md` duplicated H1** — live, sweep-blind, routed; not to be repaired inside rev
  2.2 (X00-7). Needs an owner.
- **Not measured by this seat:** the zai batch's launch/completion counters (CO6); whether
  C03–C06, Ca01/Ca03/Ca04, P01, R01 land and what they say; the r19 runner's ROOT shape
  (classified OTHER, §3.2); whether Ca01's protocol, when it lands, matches the mechanics Ca02
  applied (Ca02's own owed item).

## Citations

**Binding rules and this seat's assignment.** `reports/round-39/targets.json:4-9` (shared rules;
`:8` F-C13-1), `:117-123` (the S01 seat row: role scribe, claim cross, mission, out path),
`:11-124` (all 16 seat rows; C01–C04 missions at the cov rows), `:3` (seat_count 16);
`reports/round-39/claims.json:1-28` (`:7` baseline, `:8` dispatch, `:9-11` axes/lowest-axis/pause,
`:13-18` claim C, `:19-24` claim Ca with after_required/counting_commands/thresholds, `:26-27`
non_goals); `REGIMEN.md:17` (row 7–8: zai/glm-5.3-flash MAX, 16–32, build), `:25-50` (per-round
contract), `:52-58` (done-when), `:66-69` (deviation rule), `:73-75` (stop rule); `AGENTS.md`
(telemetry availability/dispatch rules; close-what-you-open).

**Measured by this seat.** §1 state pins (`git rev-parse HEAD`, `git rev-parse dfb0719`,
`git diff --name-status dfb0719`, `git status --porcelain -uall`, `date -u`, `python3 -V`, the
`sha256sum` block); §1 before-state (`ls corpus/knowledge/verification/*.md | wc -l` → 20;
per-directory find sweep → 94/25/21/23/29/20; `python3 -B reports/round-28/readme/sweep.py` →
exit 0, 212/212, footer [21,23,25,29,20,94], readme_sha256 `b80274bc…`); §2 (JSON parses: 12
claims keys, axes, non_goals; seat census 16; durable-sources cross-check; telemetry
closing_snapshot field); §2.4 + transcript (topic grep of C01/C02; the worked-example and sweep
absence re-sweeps → 2 incidental files / 11 incidental files); §3.1 (`grep -c '^# kotodama-shokunin
corpus index' corpus/README.md` → 2); §3.2 (the runner ROOT census over 33 files: 5 absolute /
27 relative / 1 other; `grep -n '^ROOT\|os.chdir'` over r34–r38; `--check` grep r37 `:226`, r38
`:228`; r38 guard lines `:218-233`); §3.3 (quoted from Ca02/K02 with their pins); §0/§2.5/§11.6
(`ls reports/round-39/...` censuses; `ls reports/round-39/run-validation.py` and
`validation.json` → absent; `ls /home/vgpnk/Projects/shokunin/.ufo/reports/round-39/` → absent);
§6.4 X2/X6 (`grep -c '"round": 39' MANIFEST.json` → 0; `"round": 38` → 1; `grep -c "Round 39"
LOG.md` → 0; `grep -c "round-39" SCORECARD.md` → 0; `.ufo/reports/round-38/kotodama.md` present);
`command -v bwrap` → `/usr/bin/bwrap`; `sed -n '192,201p'` + `:202-211` of
`reports/round-37/op/defect-queue.json` (O12 + basename rows).

**Source lines (read, not executed).** `reports/round-33/run-validation.py:23` (relative ROOT
shape); `reports/round-34/run-validation.py:6,10,21-22,26,209-211,522-538` (via K02 §1/§4); 
`reports/round-35/run-validation.py:9,36`; `reports/round-36/run-validation.py:8,13,319`;
`reports/round-37/run-validation.py:5,10,226`; `reports/round-38/run-validation.py:5,11,218-233,228`;
`tools/harness/receipt_guard.py:7-8,144-149` (via K02); `reports/round-28/readme/sweep.py:28-30,50-57`
(read-only contract; PARTS order); `corpus/README.md:1,3,5-12` (duplicated H1; rev 2.1 block);
`reports/round-37/calib/recount-ledger.json:60-111,451-455`; `reports/round-37/op/defect-queue.json:192-201,202-211,242-251`;
`reports/round-37/adj/A12-gap-fill.md:9-26`; `reports/round-37/calib/Ca02-r34.md:18,20`;
`reports/round-37/calib/Ca08-verify.md:13-14,23-27,32`; `reports/round-37/plan/P01-ca-plan.md:19-24`;
`reports/round-35/cov/C14-audit-6-10.md:239-288`; `reports/round-19/audit/entry-audit.py:74-96`;
`corpus/knowledge/verification/gate-battery-surface-verification.md:1-18,75-82`;
`corpus/QUALITY.md:3-23`; `reports/round-38/cross/X01-trades.md:367-369`;
`reports/round-38/scribe/S01-integration-draft.md:418-425`;
`reports/round-36/scribe/S01-integration-draft.md:248-267` (SHONEN last-recorded), `§0.2` (the
in-tree incident); `SHONEN.md:10-11`; `LOG.md` (round-36 conformance entry; rounds 37/38 entries).

**Round-39 fragments folded, each read in full.** `scout/K01-verification-gaps.md` (§1–§5);
`scout/K02-isolation.md` (§1–§4, Owed); `calib/Ca02-replay-verify.md` (verdict, protocol
mechanics, Runs 1–2, disposition mapping, fidelity limits, Owed); `cross/X00-connector.md`
(§0–§6, Owed, Citations); `cov/C01-entry-1.md` and `cov/C02-entry-2.md` (head-block fields,
`- gap filled:` absence sweeps, couples sections — content audit explicitly left to C05).

**Prior-round precedent reviewed.** `reports/round-38/scribe/S01-integration-draft.md` (dossier
shape, §3.4 digest-sweep form, §5 constants table, §6 leg format); `reports/round-38/cross/X00-connector.md`
(format precedent); `reports/round-37/scribe/S04-integration-draft.md` (via r38 citations); the
r36/r37/r38 runners' mode surfaces; `reports/round-36/scribe/S01-integration-draft.md` (the
in-tree incident and the dead-pathspec finding).

---

*This dossier claims no promotion, no canon, no clearance and no closure. It is integration
material: a fleet-report draft, a leg specification the integrator implements, and the
recorded-state baseline a close-time runner asserts against. A green gate is a measurement, not a
verdict, and a draft is not a landed change.*
