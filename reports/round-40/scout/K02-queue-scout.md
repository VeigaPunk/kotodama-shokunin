- Seat: K02 | scout | claim Ca | date 2026-10-19 | baseline fd55e1f

# K02 — queue scout: the r37 defect queue's 24 rows + every finding added in the r38 / r38-wave / r39 records

**Mission** (`reports/round-40/targets.json` seat `K02`): *"Queue scout: inventory the r37 queue's
24 rows + every finding added in r38/r38-wave/r39 records; each with origin and current
owner-state."* This fragment is the input Ca01's `defect-queue-v2.json` assembly and Ca02's
row-sampling verify against. Ca01's assembly landed before this scout existed (it records my
absence at its cut, `reports/round-40/calib/Ca01-queue-v2.md:80`); §7 cross-checks its deltas so
Ca02/R02 can sample both.

**Method.** Read the filed queue and every r38/r38-wave/r39 round record's finding-bearing
sections (op/depth/cross/review/scout/adj/calib/scribe + telemetry + LOG.md r38/r39 entries);
every owner-state below is either read from a cited record or measured live at HEAD `fd55e1f`
(command outputs inline). Owner-state vocabulary: **OPEN-carried** (no movement found since its
origin), **OPEN-worsened** (new evidence deepens it), **OPEN-new** (born in r38/r39, no
disposition yet), **CLOSED-fixed** (fixed-with-evidence in a filed round record),
**CLOSED-recorded** (incident/practice recorded, nothing owed), **ROUTED** (assigned forward with
an owner), **to-verify** (unknown, never guessed).

What this seat did **not** do: no in-tree `reports/round-*/run-validation.py` executed anywhere
(F-C13-1; the greps below read the receipt bytes, they did not run them); no filed byte touched
(`git rev-parse --short HEAD` → `fd55e1f`; the only write is this fragment); no re-freeze, no
git/network/install.

---

## 1. The object under inventory

`reports/round-37/op/defect-queue.json` — schema `kotodama-defect-queue-v1`, 24 rows, measured
this seat: `sha256sum` → `5cf827e2dd17b638acf023b1c6423b0602ba88e3c08d9698b68bae6c6cc60d5d`
(byte-identical to the pin r39 S01 recorded at its cut, `reports/round-39/scribe/S01-integration-draft.md:94`);
`python3 -c` row census → `rows: 24 / named: 19 / null-id: 5`. The queue's own
`census_coverage` block (`defect-queue.json:6-10`) declares set-equality **carried, not claimed** —
that carry is exactly what this scout and Ca02's sample exist to service.

---

## 2. Inventory A — the 12 census-origin rows (`defect-queue.json:12-131`, origin "r33-36 census (K02)")

| # | id (filed line) | filed owner | current owner-state at r40 cut |
|---|---|---|---|
| 1 | `F-C13-1` (:12-21) | integrator | **OPEN-carried.** No r38/r39 record closes it; next_touch "r38+ per O09-routing" is unsatisfied by any filed row I found — the r38 O-block landed the guard but no O09-style routing record for this row. |
| 2 | `F-C15-1` (:22-31) | integrator | **OPEN-carried.** No movement in r38/r39 records. |
| 3 | `RC-4` (:32-41) | integrator/operator | **OPEN-carried.** No movement. |
| 4 | `R36-D-DECLARATION` (:42-51) | r38+ defect-queue completion | **CLOSED-fixed** by the admitted r38 claim D landing (`LOG.md:3732-3735`: F-6 counters byte-exact patch + RL-8 era leg as D4L-ARGOT-ERA, selftest 39/39, live counters 8/8). |
| 5 | `R36-D-F6` (:52-61) | r38+ defect-queue completion | **CLOSED-fixed**, same evidence as row 4 (`LOG.md:3732-3735`). Residual to-verify: the F-6 *consumer* durability — R03 §7 found D03's non-vacuous-pass probe lives only under `.scratch/d03/` (r38 S01 §11.2, `S01-integration-draft.md:608-616`), while `LOG.md:3735` records "planted-probe visibility verified"; whether a *filed* durable consumer/probe exists is to-verify for Ca02. |
| 6 | `OI-02` (:62-71) | r38+ defect-queue completion | **OPEN-carried.** r38 R01 §6 ruled `head2` out of that claim because its empty proper domain **is** OI-02, carried (`reports/round-38/scribe/S01-integration-draft.md:675-677`; D08 §6 "recorded, not claimed", `reports/round-38/depth/D08-gap-fill.md:324`). |
| 7 | `R36-D-RL8` (:72-81) | r38+ defect-queue completion | **CLOSED-fixed**, same evidence as row 4. |
| 8 | `R36-R7-READSET-13` (:82-91) | r38+ defect-queue completion | **OPEN-carried, route now documented.** One lifecycle with row 21 (`r37-A01-readset-roster-defect`, `Ca01-queue-v2.md:289-290`); the r38 O claim documented the fix route (next re-freeze absorbs the member; O04 §4–§5, O05-verified) and landed the naming guard, zero freeze bytes moved (`LOG.md:3736-3738`). Fix lands with the loop-2 successor baseline. |
| 9 | `R36-ABSOLUTE-ROOT` (:92-101) | r38+ defect-queue completion | **OPEN-worsened.** Census alias of `O12-runner-isolation-hazard` (X00-4 dedupe ruling, `reports/round-39/cross/X00-connector.md:236`); the absolute-ROOT streak grew to **six** runners r34–r39 — my direct measurement: `ROOT = "/home/vgpnk/…"` in `reports/round-{34,35,36,37,38,39}/run-validation.py` (r39 adds `os.chdir(ROOT)` at `:13`); see §6 finding F39-1. |
| 10 | `R36-README-DUPLICATE-HEADING` (:102-111) | r38+ defect-queue completion | **OPEN-carried, re-confirmed twice.** Same defect as the r38/r39 duplicate-H1 finding (F38-6 below); live at HEAD: `grep -c '^# kotodama-shokunin corpus index' corpus/README.md` → **2** (my run); sweep-blind per r39 X00-7; do-not-touch inside any corpus delta (which binds r40's rev-2.3 delta too). |
| 11 | `R36-README-E3-PLACEHOLDERS` (:112-121) | r38+ defect-queue completion | **CLOSED-fixed** — removed at r37 integration (r37 integrator repair, `LOG.md:3715-3717`); Ca01's HEAD grep → no match (`Ca01-queue-v2.md:34-35`). |
| 12 | `R36-README-ORDER-CONTIGUITY-REVERIFY` (:122-131) | r38+ defect-queue completion | **CLOSED-fixed** — the r39 rev-2.2 landing ran the r28 sweep green 216 rows == 216 files (`LOG.md:3750-3752`), the independent control r37 lacked (`Ca01-queue-v2.md:36-37`). |

---

## 3. Inventory B — the five `id: null` rows, origin "r37 O01 unresolved" (`defect-queue.json:132-181`)

All five filed `class: carried-with-owner / owner: unassigned / reason: unclassified at the census
cut`. Their distinguishing text is the `next_touch` field; Ca01 minted stable ids `R37-O01-CAND-*`
for v2 uniqueness with a 1:1 mapping by next-touch text (`Ca01-queue-v2.md:59-60`, :72-75).

| # | filed lines | next_touch gist (quoted/condensed) | current owner-state |
|---|---|---|---|
| B1 | :132-141 | "A02 rechecks the landed entry; O03 then confirms owner/reason/next-touch; O09 files the round-38+ route" | **OPEN-new (reconciliation owed at r40 integration).** No r38/r39 record shows the O03 confirmation or an O09 routing row for it. |
| B2 | :142-151 | "Reconcile each census ID to its audit finding and later resolution evidence after K02/O03 land; retain aliases for merged mentions" | **OPEN-new.** Partially serviced: the r38/r39 alias/canonical rulings exist for two clusters (X00-4: O12 canonical / ABSOLUTE-ROOT alias; R36-R7-READSET-13 ≡ r37-A01-readset-roster-defect per `Ca01-queue-v2.md:72`), not yet as a filed reconciliation of this row. |
| B3 | :152-161 | "K02 reconciles the ledger's canonical IDs and aliases; O02 verifies any proposed fixed row; O03 checks every carry; OI-02 must not be duplicated" | **OPEN-new — and this fragment is that seat's (K02's) r40 contribution to the reconciliation pass**, together with Ca02's sample (Ca01's next_touch for the cluster: "r40: K02's scout + Ca02's sample constitute the first reconciliation pass", `Ca01-queue-v2.md:220`). |
| B4 | :162-171 | "K02 classifies each candidate against its underlying source; Ca rows stay in the recount ledger; add only independently evidenced defect-lifecycle rows" | **OPEN-new, mostly settled by r39:** the recount/defect separation held — the four c-n-r recount rows were re-dispositioned in the successor ledger, not imported here (`recount-ledger-successor.json:9-49`; `Ca01-queue-v2.md:239`). |
| B5 | :172-181 | "K02 reconciles the names to source findings; preserve the historical r34/r35/r36 records and their declared route/status" | **OPEN-new, one member adjudicated:** the "historical fixed-with-evidence" exclusion was affirmed at v2 (`R37-O01-CAND-HISTORICAL`, `Ca01-queue-v2.md:39-40`); the remainder routes at r40 integration. |

---

## 4. Inventory C — the seven later-origin rows (`defect-queue.json:182-251`)

| # | id (filed line) | origin | current owner-state at r40 cut |
|---|---|---|---|
| C1 | `O10-runner-sha256-null` (:182-191) | r36 receipt (O10-gap-fill) | **OPEN-worsened.** Now **three** receipts carry `runner_sha256: null`: the carried r36 receipt plus `reports/round-38/validation.json:130` and `reports/round-39/validation.json:126` (both grepped by this seat). The r37 next_touch ("fix in a future round's own runner; add a schema leg") was not satisfied by the r38 or r39 runners. |
| C2 | `O12-runner-isolation-hazard` (:192-201) | r37 recounts (Ca02 + O12) | **OPEN-worsened (mitigated, not remediated).** The r39 isolation-replay protocol (bwrap mount-namespace, Tier A/B/C) makes safe *replays* possible (`reports/round-39/calib/isolation-replay-protocol.md`; `LOG.md:3755-3757`), but the hazard shape persists in the runner fleet itself: six absolute-ROOT runners r34–r39 including r39's own (§6 F39-1; `Ca01-queue-v2.md:269`). Canonical id per X00-4; row 9 is its census alias. |
| C3 | `basename-couples-policy` (:202-211) | r37 A-block (K04/A06/A12) | **CLOSED-fixed with a successor defect.** The policy is documented and Ca04-verified (`reports/round-39/calib/basename-couples-policy.md`; `LOG.md:3758-3759`), closing this row — but Ca04 filed two one-sentence defects against the policy (F39-2) and the landed file carried them verbatim (my grep: `blocker\|disposition` in the landed policy → **0** matches). |
| C4 | `r37-A01-readset-roster-defect` (:212-221) | r37 A01 adjudication | **OPEN-carried, population widened.** Same lifecycle as row 8; the asymmetry is no longer r7-only — four filed baselines are row-locally inconsistent (F38-2); fix route = loop-2 successor baseline at the next re-freeze-owning round. |
| C5 | `contract-digest-lore-drift` (:222-231) | r37 A04 | **OPEN-carried.** r38 explicitly recorded it untouched ("Contested scope carried, not absorbed — the live contract digest question … is untouched by round 38", `reports/round-38/adj/A01-scope.md:58-59`); no r39 record names it (repo grep over `reports/round-38/`+`round-39/` → only A01-scope). |
| C6 | `r36-in-tree-runner-incident` (:232-241) | r36 wave | **CLOSED-recorded.** Repeat-prevention note re-issued with every future prompt (in force in this round's targets). Note the r39 wave produced a *related but distinct* staging incident — F39-4 — which did not breach the absolute rule. |
| C7 | `readme-prediction-vs-delivery` (:242-251) | r36 C landing | **CLOSED-recorded (adopted as standing practice).** The r39 leg spec + X00-3 adopted "predict by staged-tree sha, cite the post-apply sweep" (`reports/round-39/cross/X00-connector.md:230`; `Ca01-queue-v2.md:38-39`); it binds r40's rev-2.3 delta audit. |

---

## 5. Findings added by the r38 records (incl. the r38 wave)

| # | finding | origin record | current owner-state |
|---|---|---|---|
| F38-1 | **Guard row-blindness** — the landed manifest-roster guard reads the *live* `V3_READ_SET`, so it names `13-register-law.yml` identically on **all 10** filed v3 rows and cannot distinguish defective rows from clean ones; naming-not-detection. The G5 frozen-row self-consistency formulation (names exactly the 4 defective rows, keeps the r7 chain green and freeze-safe) is measured but is **not** what landed and would be a new claim. | `reports/round-38/op/O03-verify.md:134-164, 206-231` (census-10 at :232-253); `LOG.md:3739-3740` ("filed to the queue's successor") | **OPEN-new.** v2 row `r38-guard-row-blindness` (Ca01). Future-claim candidate; nothing owed before loop 2. |
| F38-2 | **Frozen-row asymmetry census** — the r37 roster defect generalizes: initial 2-row form (X02 §4a: r6 + r7), 6-row live-read-set form over the declared-in family (K02-r38 §5.1), full row-local census = **4** internally-inconsistent baselines: `round-27/pinsweep`, `round-28/pinsweep`, `round-30/…/declared-in-r6`, `round-34/…/declared-in-r7` (prose says 13, frozen `inputs` carry 12). Also falsified the O08 threshold as written ("only the r7 row names; others stay green"). | `reports/round-38/cross/X02-honesty.md:160` (§4a), :187 (§4b); `reports/round-38/scout/K02-roster-guard.md:279-338`; `reports/round-38/op/O03-verify.md:166-196` (G5 table), :418 (`O08-regression.md` §0(b) concurrence) | **OPEN-new.** v2 row `r38-frozen-row-asymmetry-census` (Ca01). Fix rides the same loop-2 successor baseline as C4/row 8. The 4-vs-6 population precision note is in §7. |
| F38-3 | **O02 fragment defects D-1/D-2/D-3** — selftest count `44` wrong (artifact yields `45`); `m15b` description contradicts the landed assertion (the leg names the member, green — not "names nothing"); §7's tamper prediction names the wrong leg (component digest leg fires, not the frozen-packet leg). Conclusions stand; three statements are wrong. | `reports/round-38/op/O03-verify.md:257-307`; Owed :394-397; `LOG.md:3740` | **OPEN-new (doc-level).** v2 row `r38-O02-fragment-defects` (Ca01). |
| F38-4 | **O08 fragment defect D-4** — O08 §1/§8 claim its patched digest `ae22013b…` "is exactly the digest O01 §6 declares" is false; O01 declares `e5812751…`; the two differ by exactly the `m15b` result string. O08's readings and census stand. | `reports/round-38/op/O03-verify.md:308-341`; Owed :398-402; `LOG.md:3740` | **OPEN-new (doc-level).** v2 row `r38-O08-fragment-defect` (Ca01). |
| F38-5 | **O07's 0-byte fragment** — `reports/round-38/op/O07-scribe.md` filed empty (my `wc -c` → 0). | `LOG.md:3741` | **CLOSED-recorded.** v2 row `r38-O07-empty-fragment` (Ca01). |
| F38-6 | **`corpus/README.md` duplicated H1** — live corpus-surface defect, sweep-blind; "do-not-touch inside any corpus delta … repair must be a separate recorded correction"; needs an owner. Same lifecycle as row 10 (`R36-README-DUPLICATE-HEADING`). | r38: A01 §5, A02 F-A02-2 (`reports/round-38/scribe/S01-integration-draft.md:548-550`, Owed :718); r39 re-confirmation: X00-7 (`X00-connector.md:252`), r39 S01 :217, :510-511, Owed :620-621; live at HEAD: my `grep -c` → **2** | **OPEN-carried (ownerless).** Ca01 keeps it open and re-verified it at `fd55e1f` (`Ca01-queue-v2.md:179`). Directly binds r40's C06 rev-2.3 delta: must not be silently repaired there. |
| F38-7 | **F-S01-1: declaration-form gap** — the r38 seat list carries a claim id `claims.json` does not declare (declaration-form difference, not a seat-count defect). | `reports/round-38/scribe/S01-integration-draft.md:131-145` | **OPEN-new (process).** Owner: declaration process (integrator). Not a telemetry deviation row under the r37 "rule breaches only" practice — but it belongs in the queue's visibility per this inventory. |
| F38-8 | **F-S01-2: no declared fallback at position 6** — grok 403 out-of-credits on all 32 seats (0 launched); devin/deepseek-v4-1-flash-high substitution as a named deviation; one interrupted 32-seat dispatch (22 landed) + one 10-seat completion = 32/32. | `reports/round-38/telemetry/availability-attempt-1.json` (failure_class, disposition); `telemetry/observed-dispatch.json` (route_deviation, wave_shape); `LOG.md:3728-3731` | **CLOSED-recorded; recurrence partially addressed.** Operator amendment 7 (`LOG.md:3763-3771`) now authorizes devin for deepseek-v4.1-flash waves without a named-deviation ruling — the general "no declared fallback" exposure for *other* positions remains. |
| F38-9 | **Wave completeness: 10 declared outputs absent** at the interrupted batch (incl. D01-f6-design and O01-guard-design at S01's cut). | `reports/round-38/scribe/S01-integration-draft.md:170` (§2.5), :681-687 (§11.10) | **CLOSED-recorded** — the 10-seat completion dispatch landed 32/32 (`LOG.md:3730-3731`; all 10 files exist in the filed tree today, `ls reports/round-38/`). |
| F38-10 | **O05's fix-route defects + cascade** — variant B leaves the named D4_COMPONENTS tuple at 12; variant C's successor digest is path-dependent; the expansion adds no detection power; cascade surface O04 did not reach: the **filed r34/r35 validators assert the old literals**. | r38 S01 §11.7 (`S01-integration-draft.md:653-661`, citing O05 §2–§5) | **OPEN-new, documented-not-applied.** Owner: the next re-freeze-owning round (same train as C4/row 8). |
| F38-11 | **R01/R02/R03 falsifications, resolved in-round** — R01: era hole; era leg moves a third pinned surface; F-6 routes not equivalent; F-6 numbers a relabel (vacuous pass) — resolved by the landing shape (D4L-ARGOT-ERA host/id, live counters 8/8, planted-probe visibility). R02 F2/F3: global/raising guard shapes are false-red machines → the record-only naming guard landed. R03-C1: rendered-text source is vacuous → the guard reads the mined manifest. | r38 S01 §11.5, §11.9 (`S01-integration-draft.md:635-645, 672-677`); `LOG.md:3732-3738` | **CLOSED-fixed in-round.** Residual carried in row 5's to-verify (F-6 consumer durability). |
| F38-12 | **head2 recorded-not-claimed** — D08 §6 records it; R01 §6 rules its empty proper domain is OI-02. | `reports/round-38/depth/D08-gap-fill.md:324`; r38 S01 :675-677 | **No new row** — folds into row 6 (`OI-02`), which stays OPEN-carried. |

---

## 6. Findings added by the r39 records

| # | finding | origin record | current owner-state |
|---|---|---|---|
| F39-1 | **r39 runner ROOT regression** — the r39 runner re-carried `ROOT = "/home/vgpnk/…"` + `os.chdir(ROOT)` **against its own dossier's load-bearing spec** (r39 S01 §5 "constants that must NOT be inherited"; §8 step 5 "relative ROOT") and r38's X01 ruling. My direct measurement: `reports/round-39/run-validation.py:5` (absolute ROOT), `:13` (`os.chdir(ROOT)`); streak now six runners r34–r39. | `Ca01-queue-v2.md:41-48`; r39 S01 §5/:492; my grep output (this seat, 2026-10-19) | **OPEN-new.** v2 row `r39-runner-root-regression` (Ca01). Fix route: r40-close relative-ROOT runner, flags-before-chdir (one fix closing rows 9 + C2). |
| F39-2 | **Basename-policy successor defects** — Ca04 D1: the policy's single-line extractor silently zeroes the corpus's one wrapped couples field (`corpus/knowledge/linguistics/phonetics-phonology.md:72-77`; 0 tokens captured vs 4 named, 2 of them phantom targets); a line-break-mangling extractor hazard no current instrument handles (to-verify corpus-wide). D2: the disposition leg P01 §2.4.4 requires (C12-row-2 blocker/document mapping) is absent. Plus one nit and one to-verify. **The policy landed verbatim without the fixes** — my grep: `blocker\|disposition` in the landed policy → 0 matches. Related live fact Ca04 measured: the r19 instrument FAILs the admitted sacred-kingship entry today (15 unresolved, exit 2) until a successor instrument implements the policy. | `reports/round-39/calib/Ca04-verify.md:76-115` (D1 :78-93, D2 :94-101, nit :102-105, to-verify :114-115); `LOG.md:3758-3759` ("two one-sentence defects filed") | **OPEN-new.** v2 row `r39-basename-successor-instrument` (Ca01). Owner: successor-instrument round; the explicit verbatim-vs-fix choice Ca04 demanded at integration was: landed verbatim (recorded here and by Ca01's grep — the "explicit recorded choice" Ca04's Owed requires, `Ca04-verify.md:108-113`). |
| F39-3 | **R01-1 mechanism ruling (the round's top review finding) + the R01 disposition debt** — Ca02's replay reproduced the filed receipts normalized-identical; the replay mechanism altered executed bytes by design; ruled as the disposition basis and folded into the successor ledger's note. The remaining R01 items (R01-2 protocol scope: three absolute runners named, more exist; R01-3 Tier B hardening; R01-5 substrate is a shared clone; R01-6 `or True` probe; R01-7/8/9 minor pins; R01-10/11 notes; R01-4 C05-absence gate — resolved when C05 landed 4/4 PASS) are tabled in the review, but their individual dispositions are in **no** round record: my grep `R01-` in `reports/round-39/validation.json` → **0** matches. | `reports/round-39/review/R01-review.md:25-33` (verdict table; R01-1 :32), findings at :75, :93, :128, :140-146, :147, :182, :191, :203, :208; `recount-ledger-successor.json:8` (note folding the ruling); `LOG.md:3756-3758` | **PARTIALLY CLOSED** (R01-1 adjudicated; R01-4 resolved) + **OPEN-new disposition debt** on the rest. v2 row `r39-review-findings-disposition` (Ca01). Owner: the r40 integrator at receipt time. |
| F39-4 | **Stray corpus staging** — a seat's stray `corpus/knowledge/verification/C03-draft.md` was removed at integration (digest-proven provenance). Did not breach the absolute rule (a staging artifact, not a filed byte edit). | `LOG.md:3752-3754` | **CLOSED-recorded.** v2 row `r39-stray-corpus-staging` (Ca01). |
| F39-5 | **X00-1..7 connector findings** — X00-1 topic/filename allocation race (made real by C01/C02 self-allocation; controlled by the uniqueness pre-check; recorded as a named fact, not a defect, `reports/round-39/scribe/S01-integration-draft.md:181, 196`); X00-2 a git worktree alone does NOT satisfy replay isolation (→ the protocol's bwrap design); X00-3 README delta verified on LANDED bytes (→ adopted leg); X00-4 one canonical queue id (→ held, C2/row 9); X00-5 filed-ledger immutability (→ held, successor file); X00-6 "the resolver" is two audit instruments, not a module (scope note, folded into the policy); X00-7 duplicate H1 (= F38-6). | `reports/round-39/cross/X00-connector.md:215, 222, 230, 236, 241, 246, 252` | **CLOSED-recorded** as process controls (X00-2/3/4/5/6 absorbed by the protocol/leg spec/policy as designed); X00-1 and X00-7 remain live items per their rows above. |
| F39-6 | **Ca02's two recorded fidelity limits** — the replay's inputs were live fleet-root reads and the replayed source was an adapted copy (provenance recorded). Limits, not defects. | r39 S01 §11.3 (`S01-integration-draft.md:565-570`); `reports/round-39/calib/Ca02-replay-verify.md` | **CLOSED-recorded.** No queue row; relevant context for any future replay adjudication. |
| F39-7 | **Absolute-ROOT census extension** — at its cut the r39 scribe measured the absolute set at five runners (r34–r38), extending K02-r39's census; superseded the same day by F39-1 (six, including r39's own). Also one `to-verify`: the r19 runner's unclassified ROOT shape ("OTHER"). | `reports/round-39/scribe/S01-integration-draft.md:560-563` (§11.2), :512-513 (§8), :646-648 (§3.2 census: 5 absolute / 27 relative / 1 other over 33) | **Folded into F39-1 / C2.** The r19 OTHER shape stays to-verify for whoever next extends the census. |
| F39-8 | **K01's G1–G4 coverage gaps + alternates** — scouted, sourced topic gaps routed to r40's C-block (G2 taboo-euphemism lifecycle, G3 dialect/register-consistency, G4 translation-protocol fidelity; G1 contact-strata was consumed by r39's own C03 entry). Not defect rows: routed coverage work. | `reports/round-39/scout/K01-verification-gaps.md:84, 106, 125, 148, 169` | **ROUTED** to the r40 C-block owners (claim C); tracked here for set-equality visibility only — the defect queue must not import them as defects. |
| F39-9 | **Dispatch fact (not a defect row)** — C05 concurrency-failed and was re-dispatched as the completion seat, 16/16. Recovery-complete, recorded; excluded from the queue per the r37 "rule breaches only" practice (which Ca01 also applies to the r38 route deviation). | `LOG.md:3747-3749`; `reports/round-39/telemetry/observed-dispatch.json` | **CLOSED-recorded.** No row. |

---

## 7. Cross-check vs Ca01's v2 assembly (for Ca02 / R02)

My independent inventory **agrees** with every Ca01 headline delta (`Ca01-queue-v2.md:31-60`):
the 8 closures (rows 4/5/7/11/12 + C3 + C7 + one minted exclusion), the 2 worsened rows (C1
three-null receipts — my greps at `validation.json:130`/`:126` confirm; rows 9+C2 six-runner
streak — my direct grep of all six runners confirms), and the same 9 new-row set (F38-1..5, F39-1,
F39-2, F39-4, F39-3). Two precision notes for the verifiers:

1. **The frozen-row population is 4 (row-local), and the 6/10 figures are a different measure.**
   Ca01's `r38-frozen-row-asymmetry-census` reason correctly names r27/r28 joining r6/r7
   (`Ca01-queue-v2.md:329`). The "six filed rows" figure in r38 records (K02-r38 §5.1,
   `K02-roster-guard.md:279-294`) measured *manifest-members-not-in-the-row's-inputs* against the
   live read-set family (r20/r2×2/r5/r6/r7), and the "all 10" figure (O03 §3.1) is the
   row-blindness replay count. Keep the 4-row row-local census canonical; the 6/10 figures belong
   to F38-1's row-blindness row, not the asymmetry-census row.
2. **Ca04's demanded "explicit recorded choice" at policy integration** (apply D1+D2, or land
   verbatim and queue both) — the landed state is **verbatim without the fixes** (my grep → 0
   matches for blocker/disposition). That choice is now recorded (here and in Ca01's grep note),
   which satisfies the record-a-choice-or-apply obligation; the queue row must carry it so the
   successor instrument round inherits both defects.

---

## Owed

- **B1–B5 reconciliation** (the five `id: null` r37 rows): this scout inventories them and is B3's
  assigned K02 contribution; the filed adjudication of each surviving row routes at **r40
  integration** (Ca01's next_touch, `Ca01-queue-v2.md:220`) — owner: the r40 integrator with Ca02's
  sample. This fragment does not adjudicate them.
- **F-6 consumer durability** (row 5 residual): whether a *filed* durable consumer/probe for the
  F-6 counters exists (R03 §7 found D03's probe `.scratch`-only) — to-verify, owner: Ca02's sample
  or the next depth round.
- **R01-2..R01-14 individual dispositions**: in no round record (my grep → 0 in r39
  `validation.json`) — owner: the r40 integrator at receipt time (v2 row
  `r39-review-findings-disposition`).
- **`SCORECARD.md` r38/r39 row cites**: Ca01 cites `SCORECARD.md:755` for the r38 D closure; my
  `grep -n "Round 38\|Round 39" SCORECARD.md` returned no match at this cut, so I cite
  `LOG.md:3732-3735` (first-hand) for that closure and leave the SCORECARD line to-verify — the
  row format may simply differ from my grep pattern.
- **Not owed by this seat**: no v2 assembly (Ca01's), no row sampling (Ca02's), no receipt, no
  corpus bytes, no filed-byte edits, no runner execution, no freeze operations.

## Citations

- Filed queue: `reports/round-37/op/defect-queue.json` (digest `5cf827e2…`; rows :12-251; census
  block :6-10; row lines per the tables above).
- r38 records: `op/O03-verify.md` (:134-164, :166-196, :206-231, :232-253, :257-341, :378-407);
  `op/O07-scribe.md` (0 bytes); `op/O08-regression.md` (via O03 :418); `op/O04-fix-route.md` /
  `op/O05-verify-route.md` (via S01 §11.7 :653-661); `scout/K02-roster-guard.md` (:279-338);
  `cross/X02-honesty.md` (:160, :187); `review/R01-d-review.md` (via S01 §11.9 :672-677);
  `depth/D08-gap-fill.md:324`; `adj/A01-scope.md:58-59`; `scribe/S01-integration-draft.md`
  (:131-170, :548-550, :608-616, :635-645, :653-661, :672-687, :718);
  `telemetry/availability-attempt-1.json`; `telemetry/observed-dispatch.json`.
- r39 records: `calib/Ca04-verify.md` (:76-115); `calib/Ca02-replay-verify.md` (via S01 §11.3);
  `calib/recount-ledger-successor.json` (:8, :9-49); `calib/isolation-replay-protocol.md` (via
  LOG :3755-3757); `calib/basename-couples-policy.md` (grep → 0 blocker/disposition matches);
  `review/R01-review.md` (:25-33, :75, :93, :128, :140-147, :182, :191, :203, :208);
  `cross/X00-connector.md` (:96-100, :192-252); `scout/K01-verification-gaps.md` (:84, :106,
  :125, :148, :169); `scribe/S01-integration-draft.md` (:94, :181, :196, :217, :219-262, :492,
  :510-513, :560-570, :596-625, :646-648); `telemetry/observed-dispatch.json`.
- Round records: `LOG.md` :3715-3717 (r37 repairs), :3725-3743 (r38 entry), :3745-3761 (r39
  entry), :3763-3771 (operator amendment 7); `reports/round-38/validation.json:130`;
  `reports/round-39/validation.json:126`.
- This seat's live measurements at HEAD `fd55e1f` (2026-10-19, `TMPDIR=$PWD/.scratch`,
  `PYTHONDONTWRITEBYTECODE=1`, all read-only): `git rev-parse --short HEAD` → `fd55e1f`;
  `sha256sum reports/round-37/op/defect-queue.json` → `5cf827e2…`; python row census → 24/19/5;
  `ROOT =` grep over `reports/round-{34..39}/run-validation.py` → absolute in all six, `os.chdir`
  additionally at r39 `:13`; `grep -n runner_sha256 reports/round-38/validation.json
  reports/round-39/validation.json` → `:130`/`:126` null; `grep -c '^# kotodama-shokunin corpus
  index' corpus/README.md` → 2; `grep -c "blocker\|disposition"
  reports/round-39/calib/basename-couples-policy.md` → 0; `grep -c "R01-"
  reports/round-39/validation.json` → 0; `wc -c reports/round-38/op/O07-scribe.md` → 0.
- v2 assembly cross-checked: `reports/round-40/calib/Ca01-queue-v2.md` (:31-60, :72-80, :179,
  :220, :269-270, :289-290, :329).
