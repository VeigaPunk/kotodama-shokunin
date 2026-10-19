# X01 — trades critic: axis moves that could harm another axis

- Seat: **X01** | role critic | claim cross | round 43, loop 1
- Baseline: `7ceff59a0216a8ea21ee43262d9fc72abf770cee` (`reports/round-43/claims.json:7`)
- Observation window: 2026-10-19T16:45Z–17:02Z, HEAD `7ceff59` throughout
- Writes: this file only. No corpus byte, no tool byte, no filed round-1..42 byte; no `run-validation.py` executed; no git/network/install. All commands read-only with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`.

## 0. Verdict at a glance

| # | trade | axis nominally moved | axis actually harmed | status at this cut | severity |
|---|---|---|---|---|---|
| **T1** | Land the r42 lithic spare as myth-symbol entry 27 | coverage 26→27, 223→224 | calibration (one-topic-owner), depth/adjacency (duplicate register) | **not realized — 9 seats report the collision; do not land** | blocking if applied |
| **T2** | File README rev 2.5 on a duplicate row | coverage (index count) | calibration (index truth) | avoided while T1 is blocked; C02/C05 draft is conditional | high if applied |
| **T3** | Mint `basename-couples-resolver.py` beside the r42 extractor | operability (+1 tool) | operability (two parsers), calibration (two authorities) | bounded by O07's authority rule; residual duplication | medium |
| **T4** | Re-label the same 2730 tokens as “four classes” | operability (policy conformance) | calibration (unresolved count 2 vs 7 vs 8) | O06/O10 resolve it as `2729 = 2556+166+0+7` + 1 excluded; O04/K01 still print 8 | medium-high |
| **T5** | Accept “wrapped field reads 4/4” as a count | operability (green selftest) | calibration (wrong token identity passes) | avoided only if the identity set is asserted | medium |
| **T6** | Disposition the four r38/r39 rows in one pass | calibration | calibration (class/citation disagreements between Ca01 and Ca03) | Ca02 resolves: D-3 `recorded`, R01-4 r39 citation, R01-13 fixed; adds a Ca01 counts-line self-contradiction | medium |
| **T7** | Mark the aggregate r39 row `fixed-with-evidence` before it is filed | calibration | honesty (fixed claim without post-apply output) | conditional; Ca03 gate G2 names the required assertion | medium |
| **T8** | Run the O census before deciding C | operability | calibration (census denominator 223 vs 224; +30 direct) | O06 §3.1 makes the landing a precondition; O10 §10 says 223 is legitimate — direct conflict | high |
| **T9** | Two “binding” O contracts bind incompatible filenames and CLI write behavior | operability (specified artifact) | operability (unimplementable as written) | O06 vs O07/O10: `couples-census-r43.json` vs `basename-couples-census.json`; default-write vs stdout-only | medium-high |

No trade in **filed bytes** was found: the tree is clean apart from untracked `reports/round-43/`; no seat staged under `corpus/`; no filed byte was proposed for edit. The trades below are threats in the **claim texts and integration order**, not realized corpus damage.

---

## T1 — Coverage would move up by duplicating an owned topic (blocking)

**Mechanism.** Claim C asks to land `reports/round-42/cov/C01-mineral-spare.md` “as the partition's stone/gem/metal register entry, completing myth-symbol's named lapidary slot” (`claims.json:39`), with the threshold “the spare's fenced bytes applied unmodified or with only the path/front-matter adjustments its own header sanctions” (`claims.json:47`). But the lithic slot is already owned:

- `corpus/knowledge/myth-symbol/mineral-stone-symbolism.md:1` — “Stone, gem and metal symbolism — **the lithic register**: the lapidary code, material prestige, and the quarry-to-regalia chain”; `:5` — “the lithic register of a fictional culture's symbolic grammar — the mineral slot the register family lacks”. 192 lines / 61,884 B / sha256 `c99f44ca79a7c50306259c1c9038cefd92787d9a5e0dd66910f46dda95adb99f`.
- It is C04's fenced body: the r42 audit pins the same content digest at `reports/round-42/cov/C05-audit.md:54`.
- The r42 audit's D1 is explicit: C01 and C04 “declare the same topic at the same landing path … would leave the lithic register owned twice — the partition's one-owner rule is violated either way”, disposition “Admit **one** lithic entry … Do **not** land both” (`reports/round-42/cov/C05-audit.md:262-274`).
- The r42 receipt permits the spare only “under a re-scoped claim” (`reports/round-42/validation.json:9,15`); the spare's own line 1 says “routed as the named spare for a future **re-scoped** claim” (`reports/round-42/cov/C01-mineral-spare.md:1`).
- The r43 claim is not re-scoped; its `before` calls the slot “unbuilt” (`claims.json:40`). That is false at HEAD.

**The harm if the threshold is followed literally.** The spare's head block would land false measurements: `:7` says “the lithic slot is named but never built” and “**no entry owns stone**”; `:24` says HEAD `ac47c78`, 220 files, myth-symbol 23. At HEAD the filename sweep returns **1** hit and the topic-line sweep returns the owner (commands below). So the coverage metric (+1) is bought with a false provenance claim and a duplicate topic — coverage up, calibration and depth/adjacency down.

**The sweep cannot see it.** My run at HEAD is green: `rows 223 files 223`, `missing_from_index 0`, `topic_mismatch 0`, `totals_ok True`, `footer_ok True`, exit 0. C05 demonstrated the blind spot directly: on a staged 224 tree with both lithic entries, the same sweep is green while `grep -rl '^- topic:.*lithic register'` returns **2** files (`reports/round-43/cov/C05-delta-receipt.md:312-324`). A green 224==224 is a count/text reconciliation, not a one-owner certificate (`reports/round-28/readme/sweep.py` has no duplicate-topic leg).

**Independent convergence (this trade was hunted, not missed).** K02 `scout/K02-landing-scout.md:9-19,123-147`; C01 `cov/C01-prepare.md:7-11`; C03 `cov/C03-audit.md:12-29`; C04 `cov/C04-contract-audit.md:9-28` (N2 apply-blocking); C05 `cov/C05-delta-receipt.md:25-33`; C06 `cov/C06-collision.md:8-18`; C07 `cov/C07-scribe.md:12-22`; A01 `adj/A01-scope.md:124-161`; X00 `cross/X00-connector.md:12,153-167`. Nine seats, same measurement.

**Verdict.** Do not apply. Record claim C as blocked/could-not-land-as-declared; coverage stays 26/223 and README stays rev 2.4. That is an **unchanged** axis, not a harmed one. The only way C “passes” is by taking the trade; the round should refuse it. If a future round re-scopes to a genuinely unowned gap, the spare's bytes are not the deliverable — its scope is the whole owned register (C07 §4.3; X00 §3.3).

---

## T2 — README rev 2.5 would be sweep-green but substantively wrong (conditional)

**Mechanism.** C02 provides a mechanically verified rev 2.5 diff (`cov/C02-readme-draft.md:63-120`) and C05 independently stages a 224 tree with `rows 224 files 224 … exit 0` (`cov/C05-delta-receipt.md:249-276`). The README would gain a second lithic row and a +1 count while the corpus gains a duplicate owner (T1). The revision prose would then assert a coverage move that is not a coverage move.

**Evidence that the mechanism is real, not hypothetical.** C02 states it outright: “A README rev 2.5 at 224 would be **mechanically sweep-green but substantively wrong** — the r28 sweep checks row↔file topic equality, not duplicate topics across files” (`cov/C02-readme-draft.md:16`). C05 §4.4 measures two owners on the staged tree while the sweep is green. My live run confirms the sweep's legs (rows/files/topic/totals/footer) and its silence on ownership.

**Additional integrity issue in the current README (pre-existing).** A01-M2: `corpus/README.md:10-11` rev 2.4 prose vector `25/23/26/25/24/94` sums to 217, while the footer and sweep read `25/26/25/29/24/94` = 223 (`adj/A01-scope.md:193-195`). C02's Variant A does not repair this line. If any README edit is applied this round, fix it in the same edit; if no edit is applied (the recommended outcome), record it as a carried docs defect, not a new one.

**Verdict.** No rev 2.5 while T1 stands. A staged green is a prediction, not a delivery certificate; the durable practice requires the post-apply sweep on the landed tree (`cov/C05-delta-receipt.md:186-196,333-357`).

---

## T3 — A second resolver could fork the instrument of record (bounded)

**Mechanism.** Claim O's `before` says “no durable instrument implements the r39 basename-couples policy” (`claims.json:27`). At HEAD that is false: `tools/harness/couples-reference-extractor.py` is tracked in `7ceff59`, 332 lines, sha256 `d8d23a265d12d290de69a6eb50454273af4ca699986812c6e203a030f4679cf1`; its `--selftest` is 8/8 PASS and its `--census` reads the wrapped field 4/4 (my runs, §Commands). r42's claim O is `"passed": true`; r42 was refused on C, not O. K01, O02, O04, O07, O12 and A01 all independently flag the stale `before`.

**The trade.** Minting `tools/harness/basename-couples-resolver.py` as a standalone re-implementation (the claim's literal path) gives operability a nominal second tool while:
- two parsers (`couples_block`, `join_parts`, brace expansion, classify) exist with no runtime coupling — O07 explicitly rejects a shared helper module (`op/O07-durability.md:63-70`);
- the r42 extractor stays live and cited, with a **six-class** vocabulary (direct/fallback/ambiguous/unresolved/prospective/glob-fragment), while the new tool must report the policy's **four** classes;
- the same corpus yields different “unresolved” numbers depending on which tool is cited (see T4).

O07's mitigation is the right shape: the new tool becomes the **single census authority**, the r42 extractor is demoted to the N6 regression witness, and a parity receipt must record both runs and a digest (`op/O07-durability.md:322-333,441-443`). If that rule is filed in the census header and the LOG, the trade is bounded to duplicated code and future double-fixes. If both instruments are cited as authorities, the calibration axis is harmed by definition.

**Verdict.** Proceed only if (a) the new tool is the named authority, (b) the r42 tool is labelled witness-only in the same artifact, (c) the O07 §4.4 parity receipt is filed (one wrapped field, same four token names, differences explained solely by the documented subclass separation). The claim's `before` line must be corrected in the round record; filing the stale wording would misrepresent the operability gain.

---

## T4 — The same 2730 tokens can be reported as 2, 7, or 8 unresolved (calibration)

This is the subtlest trade in the round: no corpus byte moves, but the headline number does.

| view | direct | fallback | ambiguous | unresolved | other | total |
|---|---:|---:|---:|---:|---:|---:|
| r42 extractor, six classes (my run) | 2556 | 166 | 0 | **2** | prospective 5, glob-fragment 1 | 2730 |
| policy four classes, 5 prospective folded in, glob quarantined (my recompute) | 2556 | 166 | 0 | **7** (6 distinct) | glob 1 | 2729 + 1 = 2730 |
| policy four classes with glob also counted as unresolved (O04 oracle) | 2556 | 166 | 0 | **8** (7 distinct) | — | 2730 |

All three are arithmetically defensible; they are not the same statement. The r39 policy says:
- §2 has exactly four classes (`reports/round-42/calib/basename-couples-policy-full.md:27-48`);
- §3.1 requires the four classes separately, per entry and in totals (`:50-58`);
- §5.6: glob fragments are “an extractor artifact, not couples references … this policy forbids counting them as unresolved couples findings” (`:97-102`).

Therefore the **policy-correct finding count is 7 unresolved** (2 slash-bearing/phantom + 3 never-written seeds + 2 wrapped-field phantoms), with **1 glob artifact quarantined** and **2730 extracted tokens** (2729 couples references + 1 artifact). Reporting `unresolved=8` without a quarantine sub-bucket over-counts findings by one against §5.6; reporting only `unresolved=2` (the r42 six-class line) silently hides five policy-unresolved tokens behind a non-policy `prospective` label.

**Evidence the risk is live in the round's own texts.** O03 predicts `unresolved 7 + glob 1` (`op/O03-predicted.md:10-21`) and says either 7 or 8 is reconcilable (`:38-39`). O04's oracle prints `unresolved=8` (`op/O04-verify.md:127-148`) and its G1 asks the successor to fold prospective into unresolved or state the mapping (`:233-241`). K01's contract example prints `unresolved: 8` with subclasses (`scout/K01-resolver-scout.md:256-290`) while its rule 4 says glob is excluded from the finding count. X00 recommends keeping both views in `totals_policy_four` + `totals_auxiliary` (`cross/X00-connector.md:57-63,88-114`). None of these is wrong as an internal note; the harm is a **filed census** that picks one number and labels it “the policy's four classes”.

**Mitigation (must be in the artifact, not prose).** The census must print the identity:

```
extracted_tokens = 2730
couples_refs     = 2729   (extracted_tokens - quarantined_glob)
direct 2556 + fallback 166 + ambiguous 0 + unresolved 7 = 2729
quarantined_glob_fragment = 1  (-gate.md, gate-frozen-run-standard.md:15)
```

and, if it also prints the r42 six-class view, label it `auxiliary_classification` with `prospective=5` as a **sub-reason of unresolved**, never as a fifth policy class. The five prospective tokens and their reasons are enumerated at `op/O03-predicted.md:405-420`.

**Verdict.** A four-class census that prints `unresolved=8` and calls it the finding count takes a calibration trade: it looks more thorough (more findings visible) while violating §5.6's exclusion rule. A census that prints only r42's `unresolved=2` hides five findings. Only the 7+1 accounting is simultaneously policy-conformant and non-dropping.

**Post-cut update (O06/O10 landed after this analysis began).** Both artifacts now specify exactly this 7+1 accounting: O06 §5 invariant I9 and O10 §5 identities both give `2729 = 2556+166+0+7`, `2730 = 2729+1`, `7 = 2+5`, `1 = 1`, and O10 prints the five strict/native identities (`op/O06-disposition-leg.md:212-242,371-399`; `op/O10-census-artifact.md:113-125,376-399`). That **resolves the number** in the filed shape. The residual inconsistency is in the surrounding prose: O04's oracle still says `unresolved=8` (`op/O04-verify.md:127-148`) and K01's contract example still prints `unresolved: 8` (`scout/K01-resolver-scout.md:256-290`). A verifier who diffs the filed census against O04's oracle will see a −1 and must read it as the glob exclusion, not a dropped token. Label both views in the census and the comparison is closed.

---

## T5 — “Wrapped field reads 4/4” can pass a wrong parse (verification quality)

The claim's threshold is “the wrapped field reads 4/4” (`claims.json:34`). O12 measured three join rules on the live six-line field:

| join | tokens | correct identity? |
|---|---|---|
| newline join | `sound-change.md`, **`prosody.md`**, `sound-symbolism.md`, `writing-systems.md` | no |
| space join | same as above | no |
| hyphen-retained heal | `sound-change.md`, **`tone-prosody.md`**, `sound-symbolism.md`, `writing-systems.md` | yes |

All three return **4 tokens** (`op/O12-negative-proof.md:175-213`, finding O12-F1). A selftest asserting `len(tokens) == 4` is therefore a false green over a defective parse; it mints `prosody.md`, which exists nowhere, while dropping the intended `tone-prosody.md`. O02's controls already require the identity set and the mangling exclusion (`op/O02-controls.md:54-71,190-195`); O04 independently requires the set, not the count (`op/O04-verify.md:87-119`).

**Trade.** If O01's draft or the runner's acceptance leg checks only arity, operability moves up on a green selftest while the calibration value of the instrument is negative (it certifies a wrong parse). **Mitigation:** the selftest must assert `{sound-change.md, tone-prosody.md, sound-symbolism.md, writing-systems.md}` exactly and assert `prosody.md`/`toneprosody.md` absent; the runner must grep for the identity line, not a bare “4/4”. This is cheap and already specified by O02/O12.

**A second false-green source: controls that do not exercise the bug.** O02's 25-control battery is 25/25 green, but R01 §2.3 and O05 §3.4 both measure that its S7a boundary fixture uses **non-indented** prose after the blank line (`- couples: …\n\nBody prose …`). The landed parser already stops at non-indented text, so S7a passes without the blank-line `break` that the defect requires; the discriminating fixture needs an **indented** prose paragraph after the blank line. O05 §3.3 adds a second: the r42 classifier checks `glob-fragment` **after** Tier 2, so `-gate.md` becomes `fallback` with one injected basename hit and `ambiguous` with two, even though §5.6 forbids both. The live zero-hit case hides the bug. A green battery that never exercises the failing input is the same trade as a count-only 4/4: operability looks improved while the verification value is negative. The successor's selftest must include the indented-prose boundary and a glob-with-index-hit case, and the runner must assert those controls exist, not just count PASS lines.

---

## T6 — The disposition pass has internally inconsistent tables (calibration)

Ca01, Ca02 and Ca03 all disposition the four rows, agree on the headline classes for three of them, and disagree in three places that a merged artifact could silently blend. Ca02 (the independent verifier) has since adjudicated all three: D-3 `recorded`, R01-4 the r39 audit, R01-13 `fixed-with-evidence`. The table records the evidence so the integrator does not have to re-derive it.

| finding | Ca01 (`calib/Ca01-dispositions.md`) | Ca03 (`calib/Ca03-queue-update.md`) | evidence check |
|---|---|---|---|
| `r38-O02-fragment-defects` | `could-not-recover` (D-1/D-2/D-3 absent from filed O02) | row `recorded`; D-1/D-2 `could-not-recover`, D-3 `recorded` | **reproduced**: `grep '44 controls'` → no match; filed O02 says 45 at `:20,:62,:203`; single commit `dfb0719`; `git log -S'44 controls'` empty. My independent check agrees. |
| O02 D-3 (tamper leg) | `could-not-recover` (the quoted prediction string is absent) | `recorded` (the surviving sentence still names the assembled-vs-frozen compare, while O03 measured the component-digest leg firing) | both true: the quote is unrecoverable **and** the surviving mechanism sentence is wrong. `reports/round-38/op/O02-isolated.md:160-166` names `v3_verify_component_digests` at `:161` but also says the component “surfaces through the assembled-vs-frozen packet compare (`:3951-3957`)”; `reports/round-38/op/O03-verify.md:288-306` measured the per-component leg. Ca03's `recorded` is the more useful disposition because it corrects the surviving sentence; Ca01's `could-not-recover` is right about the quote. The row should carry both legs, not one class. |
| `r38-O08-fragment-defect` | `recorded` | `recorded` | **reproduced**: O08:83 claims identity; O01:144/:309 declare `e5812751…`; O08:80 prints `ae22013b…`. |
| `r38-O07-empty-fragment` | `recorded` + prevention `routed-with-owner` | `recorded` + prevention routed | **reproduced**: `wc -c` → 0; sha256 `e3b0c442…`. |
| R01-4 | `fixed-with-evidence`, cites **r39** `cov/C05-audit.md` 28,221 B `/ :46 4/4 PASS` | `fixed-with-evidence`, cites **r40** `cov/C05-audit.md:26-27` | both files exist and both say 4/4 PASS, but R01-4 is about the **r39** audit's absence; Ca01's citation is the on-point one. Ca03's is a different artifact. |
| R01-13 | `recorded` (“C05-audit carries as gaps”) | `fixed-with-evidence` (r40 landed G2–G4 as four entries) | `reports/round-40/claims.json:14` says “Land K01-r39's routed gaps G2-G4 as four sourced entries”; `SCORECARD.md:790` records cost 21→25. Ca03's class is supported; Ca01 under-claims. |

**Why this is a trade, not a nit.** The claim Ca's threshold is “every one of the four named rows reaches a class … with a citation; zero silently dropped” (`claims.json:58`). Both tables satisfy that at row level, but a successor artifact that merges them without adjudicating R01-13/R01-4 would carry two classes for one finding and two C05-audit citations for one defect. Calibration then nominally moves (a disposition file exists) while its internal consistency is harmed. Ca03's own gate G3 says Ca01 wins “only if it names committed bytes”; Ca01's R01-4 citation does, and its R01-13 class does not match the r40 record. So the correct merge is: **Ca01's R01-4, Ca03's R01-13**, with both citations preserved.

**Ca02 independently confirms this merge and adds a fourth defect in the disposition artifact itself.** It re-measured every row and scores: O07 agree, O08 agree, O02 partial disagree (D-1/D-2 `could-not-recover`; **D-3 `recorded`** because O02 `:164` carries the weaker surviving error), R01-4 `fixed` with **Ca01's r39 citation** (Ca03's r40 audit is “a different audit” and cannot evidence R01-4), R01-13 **`fixed-with-evidence`, `fixed_at: round-40`** (Ca03), R01-12 Ca01's HEAD-11 number (`calib/Ca02-verify.md:10-21,90-158`). It also finds a self-contradiction inside Ca01: the prose counts line at `Ca01-dispositions.md:86-87` says `1/8/6/5 = 20` while the JSON's `counts` block and a programmatic recount give **`1/10/7/4 = 22`** (`Ca02:160-167`). A disposition artifact whose own summary line contradicts its JSON is the calibration version of the count-only false green: the file exists, so the axis looks moved, but its arithmetic does not close. The integrator must apply Ca02 §6's five amendments (D-3 `recorded`; R01-13 fixed; R01-4 r39 citation; counts line corrected; parent-row ranges fixed) before filing `dispositions-r38-r39.json`.

**Also relevant (positive finding, not a trade):** Ca03 OBS-1 measures that the r41/r42 runners' min-bytes check is vacuous by construction — `missing` contains only non-existent paths, then `empty` filters that list for existing zero-byte files, an empty intersection, never read (`reports/round-41/run-validation.py:168-173,183`; r42 `:177-182,192`). The r38-O07 prevention leg therefore must stay `routed`; marking it fixed would be a false green. Ca01 and Ca03 both keep it routed, correctly.

---

## T7 — “Fixed-with-evidence” before the fix is filed (conditional honesty gap)

Ca01 assigns the aggregate `r39-review-findings-disposition` row `fixed-with-evidence` (`calib/Ca01-dispositions.md:78,183-185`), on the ground that the per-finding list now exists. But at this cut the list is a **fenced draft in Ca01's out file**, not yet `reports/round-43/calib/dispositions-r38-r39.json`; Ca03 gate G2 requires the integrator to run a 14-finding parse assertion and paste its output before the fixed claim is admissible (`calib/Ca03-queue-update.md:238-244,298-300`). The claim's threshold says “each 'fixed' claim carries a re-run command output” (`claims.json:58`).

**Trade.** Filing the row fixed without the post-application parse would move calibration +1 on the strength of an artifact that does not exist yet — the same “record asserted, not measured” shape the round is chartered to stop. **Mitigation:** apply the JSON, run the 14/14 assertion, paste the output into the successor artifact or the validation receipt, then keep `fixed-with-evidence`; otherwise down-class the row to `routed-with-owner` (owner: integrator) until it lands. This is a sequencing gate, not a criticism of the dispositions' content.

---

## T8 — Census ordering vs the C decision (cross-claim)

If C were landed after the O census is taken:

- entries 223 → 224; refs 2730 → 2760; direct 2556 → 2586; fallback/ambiguous/unresolved unchanged — **+30 direct only**, because the spare's `- couples:` field is one physical line with 30 unique tokens, all resolving through Tier-1 bases (my run: `wrapped=False tokens=30`, all `direct`; O03 §8 independently predicts the same +30; X00 §3.2 agrees). C07's “34 refs” is a raw-count slip: the field has 30 unique/30 raw tokens (my `MD_RE.findall` → 30, `field_refs` → 30), no duplicates. The C-draft numbers in C07 §5 should not be copied.
- A census filed at 223 while README says 224 would be stale; O04's owed note already requires the artifact to carry its denominator and commit (`op/O04-verify.md:304-308`).

**Trade.** Filing a 223-entry census as the round's corrected baseline while a 224-entry README is also filed makes both artifacts internally true and mutually inconsistent. **Mitigation:** decide C first (recommended: no landing), then run O's census last, and print `entries`, `baseline_commit`, and the partition vector in the artifact header. If C is ever re-scoped and landed, re-run the census; do not add +30 by hand.

**Post-cut update — the ordering rule is now stated in two incompatible forms.** O06 §3.1 makes the landing a precondition: “**Generate it after the C01 lithic entry is applied.** The claim's census is the post-landing state (224 entries); a pre-landing run records `corpus.entries: 223` and cannot satisfy the claim” (`op/O06-disposition-leg.md:100-105`). O10 §10 states the opposite and the correct rule: “223 is a legitimate closed-tree value, and the claim-C shortfall is a separate finding, not a reason to fake 224. The census must never be adjusted to match a claim's expected count” (`op/O10-census-artifact.md:534`). Since T1 blocks C, O06's sentence, if treated as binding, would **pressure the integrator to land a duplicate lithic entry to make the census “satisfy the claim.”** That is the purest form of this round's trade: an operability artifact contract forcing a coverage move that harms calibration and depth. The resolver must run on the actual closed tree (223 if C is not re-scoped) and the round must record the C shortfall separately. O06's §3.1 sentence needs correction at integration; O10's §10 rule is the one to keep.

---

## T9 — Two “binding” O contracts cannot both be implemented (operability)

O06, O07 and O10 landed independently and each declares a binding contract for the same census artifact. Three concrete collisions:

| item | O06 (`op/O06-disposition-leg.md`) | O07 (`op/O07-durability.md`) / O10 (`op/O10-census-artifact.md`) | consequence |
|---|---|---|---|
| canonical filename | `reports/round-43/calib/couples-census-r43.json` — “One artifact, one name. O10 must use this exact path; do not file a second census under `op/`” (`:87-99`) | `reports/round-43/calib/basename-couples-census.json` (+ `.md`) — “What the integrator files” (`O10 :54-62`) | two files, two schemas named `kotodama-couples-census-v3`; if both are filed, the round has two censuses; if one, one seat's contract is violated |
| who writes the file | “`--census` writes this path by default. `--out PATH` overrides; `--stdout` prints the same JSON and writes nothing” (`:97-99`) | “The tool never chooses a `reports/` path and has no `--out` switch … filed by the integrator as a shell redirection” (`O07 :162-173`); O10 allows either, with a text fallback (`:63-72`) | O01 cannot implement both. A default-writer is a larger write surface than O07/O12's read-only contract |
| topology keys | `totals.policy_four` + `totals.aux` (`:119-128,371-375`) | `totals_policy_strict` + `totals_tool_native` (`O10 :113-145`) | both valid shapes, but a consumer written to one fails on the other; the verifier recipe in O06 §9 and the arithmetic checker in O10 §11 are not interchangeable |

**Why this is a trade, not coordination noise.** Operability's value in this round is a **durable, filed, single-authority census**. Two binding names/schemas and two write models turn that into an integration choice that will leave one seat's acceptance criteria unmet no matter which is chosen. If the integrator files both, the calibration axis is harmed by two artifacts with the same schema id and different contents; if it files one, the other seat's “binding” language is falsified. The fix is cheap: the integrator must **pick one** before applying the tool, record the choice in the census header and LOG, and correct the other draft's path in the integration record.

**O09 has since arbitrated the filename:** “O06 owns the name by mission; file **one** artifact, not two” (`op/O09-scribe.md:14`), and its assembled body writes via `--census --json > reports/round-43/calib/couples-census-r43.json` — stdout, matching O07, not O06's “writes this path by default” (`op/O09-scribe.md:882`; body docstring `:366-367`). That resolves the name and the write model in favor of O06's path + O07's stdout contract, but it leaves **O06 §3.1's default-write sentence and O10's filename** to be corrected at integration. If the integrator treats those sentences as binding instead, the conflict reappears. The schema fork also remains: O09's body emits a JSON whose per-token shape is closer to O10's skeleton than O06's full v3; O09 §0.7 calls the gap “the remaining O01/full-body task.” File one artifact, one schema, and state which contract it satisfies.

**Severity: medium-high.** No corpus harm; a real risk to the operability claim's single-authority requirement and to the validation's ability to parse one shape.

---

## 9. Smaller findings worth carrying (no axis harm found)

1. **Staged README digests are not comparable.** C02 stages `8078c479…` (`cov/C02-readme-draft.md:135`), C05 stages `3128ec38…` (`cov/C05-delta-receipt.md:239`), C07 stages `1c165a99…` (`cov/C07-scribe.md:157`) — three different 224-row staging trees with different filenames/prose. Each is a valid prediction of its own draft, none is a delivery. The integrator must not quote one as “the” prediction while applying another; the post-apply sweep is the only certificate (the `readme-prediction-vs-delivery` practice, cited by C05 §3.1).
2. **Four invented target slugs across seats** (`stone-symbolism.md`, `stone-gem-metal-lithic-register.md`, `stone-gem-metal-register.md`, `lithic-register-symbolism.md`) are evidence that no author-sanctioned path exists (A01 §5.4 lists them). This is a symptom of T1, not a separate trade.
3. **`claims.json` digest mismatch.** `telemetry/dispatch-declared.json` declares 6,353 B / `beda7644…`; live is 6,546 B / `9662e2bd…` (A01-M1; S02 independently). The round's contract file was amended after declaration. This does not harm an axis by itself, but a validation receipt that cites the declared digest would certify different bytes than were executed. Fix by re-declaring or recording the amendment.
4. **O-claim verifier pair is complete in number, not in object.** O04 and O05 have both filed (`op/O04-verify.md`, `op/O05-traps.md`), satisfying the count; but O01's draft never appeared, and the only full body is O09's assembled fenced script (515 lines, sha256 `43ce341f…`, O09 claims 27/27 selftest). Neither named verifier read those bytes, and I did not execute them. Re-run both matrices against the assembled body and O12's gate before counting verification as done; otherwise the pair verifies the requirement surface, which is what O04 §6 says it is.
5. **No trade in write surfaces.** `git status --porcelain` → only `?? reports/round-43/`; `git diff HEAD` empty; no corpus staging; no filed-byte edit. O12's negative proof and A01's scope audit independently confirm this. The O tool drafts are read-only by contract; the Ca successor records are new files; the C drafts were not applied.

---

## 10. Trade-specific verdict candidates (for the reviewers/scribe)

- **Operability (O):** conditionally improved *if and only if* the durable resolver is the single census authority, the four-class identity `2729 = 2556 + 166 + 0 + 7` plus one quarantined glob is printed, every fallback mapping and every unresolved reason is listed, the ambiguous and blank-line controls are green, two named verifiers read the actual bytes, and the O07 parity receipt is filed. Otherwise unchanged/unprovable.
- **Coverage (C):** **unchanged** (26/223, README rev 2.4). The declared move is blocked; taking it would harm calibration and depth. The honest outcome is a recorded collision, not a 224.
- **Calibration (Ca):** conditionally improved *if* the successor disposition artifact is filed, Ca02 independently re-measures the four rows, the post-application 14/14 assertion is pasted, and the R01-4/R01-13 citations are reconciled to the on-point artifacts. Otherwise the pass is a draft, not a disposition.
- **No axis is harmed at HEAD.** The only realized damage would come from applying one of the conditional drafts against its own blocking evidence.

---

## 11. Commands run (this seat, read-only, HEAD `7ceff59`)

```
$ ls corpus/knowledge/myth-symbol/*.md | wc -l                         -> 26
$ find corpus/knowledge -name '*.md' | wc -l                           -> 223
$ for d in corpus/knowledge/*/; do ...; done                           -> 94/25/25/26/29/24
$ python3 -B reports/round-28/readme/sweep.py                          -> rows 223 files 223; totals_ok True; footer_ok True; exit 0
$ ls corpus/knowledge/*/ | grep -ic 'mineral\|stone\|gem\|lithic'      -> 1 (mineral-stone-symbolism.md)
$ grep -rliE -- '^- topic:.*(mineral|gem|lapidary|lithic|precious)' corpus/knowledge/
    -> 3 files: linguistics/sound-symbolism.md (substring), myth-symbol/death-afterlife-eschatology.md (substring),
       myth-symbol/mineral-stone-symbolism.md (owner)
$ sha256sum corpus/knowledge/myth-symbol/mineral-stone-symbolism.md    -> c99f44ca…, 61,884 B
$ sha256sum reports/round-42/cov/C01-mineral-spare.md                  -> 2b9326e3…; fenced body 6999a912…, 55,101 B
$ python3 -B tools/harness/couples-reference-extractor.py --selftest   -> 8 PASS, exit 0
$ python3 -B tools/harness/couples-reference-extractor.py --census
    -> entries=223 refs=2730 -> direct=2556 fallback=166 unresolved=2 prospective=5 glob-fragment=1
$ python3 -B tools/harness/couples-reference-extractor.py corpus/knowledge/linguistics/phonetics-phonology.md
    -> wrapped=True tokens=4; sound-change.md/tone-prosody.md prospective; sound-symbolism.md/writing-systems.md direct
$ four-class recompute (import the r42 parser; fold prospective into unresolved; quarantine glob)
    -> direct 2556, fallback 166, ambiguous 0, unresolved 7 (6 distinct), glob 1; 2729 + 1 = 2730
$ python3 -B tools/harness/couples-reference-extractor.py reports/round-42/cov/C01-mineral-spare.md
    -> wrapped=False tokens=30, all direct
$ wc -c reports/round-38/op/O07-scribe.md                              -> 0
$ grep -Fn 'plus 44 controls' reports/round-38/op/O02-isolated.md      -> no match (exit 1)
$ git log --format='%h' -- reports/round-38/op/O02-isolated.md         -> dfb0719 (single commit)
$ git show dfb0719:reports/round-38/op/O02-isolated.md | grep -c 'plus 44' -> 0
$ grep -n 'is exactly the digest O01' reports/round-38/op/O08-regression.md -> :83
$ grep -n 'e5812751' reports/round-38/op/O01-guard-design.md           -> :144, :309
$ git status --porcelain                                               -> ?? reports/round-43/ only
$ git log --oneline -3                                                 -> 7ceff59, ac47c78, 456674d
```

## 12. Limits / to-verify

- **Snapshot.** At this final cut: O01 (`op/O01-tool-draft.md`), O08, R02, X02 and `reports/round-43/run-validation.py` are absent; O02–O07, O09, O10, O12, Ca01–Ca03, R01, S01, S02, A01 and X00 have filed. O09 supplies an assembled 515-line successor body (sha256 `43ce341f783041cfa4af538a2ce9275729daf13fb6e118f0b5ac66308ab5ad64`; O09 claims 27/27 selftest) but O04/O05 predate it, so the two named verifiers still have not read the bytes the round would land. I did not execute O09's body; its claims are quoted, not verified. Re-run T3–T5 and O12's gate against the actual body before any acceptance.
- **The C trade is settled by bytes, not by a future artifact.** Any later C artifact that proposes a landing must answer T1 first; a green sweep does not.
- **Ca02 has now filed and confirms the T6 merge** (D-3 `recorded`, R01-4 r39 citation, R01-13 `fixed-with-evidence`) and adds the Ca01 counts-line correction. My remaining Ca caveat is only the absent R02/X02 cross-reads; if either contradicts Ca02, its measured bytes govern.
- **No claim of acceptance.** This file is a trade report, not an axis verdict or a round admission. It edits nothing and decides no canon.
