# X01 — trades critic, round 47

- Seat: `X01` | role: **critic** | claim: **cross** (`reports/round-47/targets.json:56`)
- Baseline: `6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe` (`6e9a30d`) — equals `reports/round-47/claims.json:7`; `git rev-parse HEAD` at every read in this seat.
- Out path: `reports/round-47/cross/X01-trades.md` (the only file this seat writes).
- Observation window: `2026-10-19T17:50Z–18:07:49Z`. The round was live; several seat files were revised while this seat read them. Every verdict below is bound to the digests in §0 and to no later revision.
- Method: read `claims.json`, `targets.json`, the r43/r44/r46 filed records, and every r47 artifact present at the window; re-ran the measurement commands myself (census, sweep, resolver, `git show`/`git ls-tree` at baselines, CAP probe greps, digest checks, queue-JSON queries, Ca06 JSON parse). No filed byte edited; no corpus staging; no `reports/round-*/run-validation.py` executed; no git mutation/network/install; scratch only under `.scratch/`.

**One-line result.** C's ownership premise is clean and its drafts are real cartography, not a lithic find/replace; the live C defects are a **provenance-wording** defect ("no prior-round proposal") and a **README record-repair** tension. The O deliverable is **absent**, and its acceptance surface has a concrete reproducibility gap (the counting command cannot run the typed checks) plus a **theatrical Ca control** (a tautological absence probe over the round's own output, shielding a false sub-clause). Ca's successor is substantially correct but its provider wording needed the 12/13 correction it now carries, and its fragment digests are still drifting. No confirmed harm to corpus, ledger, or authority; the trades are in **acceptance evidence**, not in landed bytes.

---

## 0. Artifact state at this read (digest-bound)

Present at `18:07Z` (sha256, full):

| artifact | sha256 |
|---|---|
| `cov/C01-entry-a.md` | `cfb42955617373479a41d881fb6fd83f7df907aa7f563f51de95493d9ec8c44d` |
| `cov/C02-entry-b.md` | `bfce3acaf20e527b949a45b708f1d9e10c9ab9447651375f89075f1c80be3600` |
| `cov/C03-entry-c.md` | `4b699e06537115274807b64fbc5947cefc889348e5b4434b14a8ddb661eee3e5` |
| `cov/C04-entry-header.md` | `cb5a7489676de47e146e5055e07be9c8fa9d2df624c8872b0d438efcd67b68b0` (`- couples:` line pin `cf59ba1f…f5663`, 4096 chars + LF) |
| `cov/C05-freshness.md` | `62f9f702540f6b363d1c410ee8a58aa19619aa6b09b1c0caeb323ac4dd8ee5e3` |
| `cov/C09-readme.md` | `b63df413410150b44705e8f9999d1bb73c3682daaeea66e0347dbff5152b3008` |
| `cov/C10-sweep.md` | `916e8c6b186d423196df2b4199f7acc38eb5ace3e0fa43ece3b507055f83abc3` |
| `cov/C13-couples.md` | `bf57bdc7fbad64d557fcde89530ac3904ed3ef991418d8a4af6dca5b850d9881` |
| `op/O05-r43-demo.md` | `1fbeeed4a768626cb83e26e7dd311c0f6baa6cdaf1d7e672984b4e7ddc4fdcfd` |
| `op/O06-negative-control.md` | `daab9149a9baccc6fefdbe63afb1dc27be8ce294a3dfb7ba1250af5e295412be` |
| `op/O09-traps.md` | `90409c408f37af588cac7ad1348308c36d3b96f6e9a320281ebcd7454cbc4d93` |
| `op/O10-exit-codes.md` | `31f954fde809bd057e252bbfcda0ceadb2469a021d43bdff6cf566f4a2d8e81f` |
| `calib/Ca01-stale-premises.md` | `e0e51e5600a1537f425c2d8f20ea68937e42c6c01b78c14d8d25580cce52ce3c` |
| `calib/Ca04-provider-amendments.md` | `94b99878a31ae6aa8c376fa35af786e36d07f3210c9f368f9a014f4a4ac2136e` |
| `calib/Ca05-verify.md` | `31d244235a6c938d61b78b558c40b5d4c1153016124a7b3831ea0e69e20597ba` |
| `calib/Ca06-queue-successor.md` | `15bb86dfff09ff97cbf8e757bbf139e1cb7bc59f42c66475d19a5a1b02db5ec6` |

Absent at this read: `tools/harness/claims-freshness.py`; `reports/round-47/run-validation.py`; C06 source audit; C08 boundary audit; C12 shelf audit; C14 example audit; R03 content review; C11/W02/A02/Q01. Anything below that depends on those is labelled **could-not-evaluate**, never inferred green.

Two artifacts were revised mid-window and the earlier versions are not recoverable from filed bytes: `Ca06` (earlier `named_deviations` schema, now `provider_amendments`) and `Ca05` (earlier Ca01/Ca03/Ca04 "could-not-evaluate", now all PASS). Verdicts cite the current digest; the final integrator must re-pin after close.

---

## 1. Trade register

| # | suspected trade | verdict | strongest evidence |
|---|---|---|---|
| **T1** | C lands a topic that is owned or carried | **Ownership clean; wording defect confirmed** | 0 filename/0 topic owners; 0 prior claims; r44 K02 is the cited seed and recommends the exact landing (`K02-gap-scout.md:8`, `:207`, `:218-220`). The claim's "no prior-round proposal" is literally false at r47 unless read as "no prior claim/draft". |
| **T2** | C lands filler / the r42 lithic skeleton under a map title | **Not reproduced in content; integration watch** | C01/C02 headings follow the lithic-derived 15-section mission (`targets.json:21-23`), but the bodies are cartography: 50/50 in-fenced `path:line` refs resolve (C01 13, C02 19, C03 18), keyword census is survey/projection/portolan/legend-heavy, and the only stone/gem hits are legitimate comparisons (§2.2). |
| **T3** | README rev-2.5 "repairs" rev 2.4 by rewriting the dated record | **Mitigated, not eliminated** | C09 edits the 2.4 token in place **and** preserves the defective `25/23/26/25/24/94` (217) as a quoted record in rev 2.5 (`C09:61-70`, `:83-96`). C10's staged model also quotes the defective value in its rev-2.5 note (`C10:156-159`), but it edits the 2.4 block in place too; the remaining tension is the in-place edit, not a missing record. Apply a transform that keeps the 217 quote. |
| **T4** | O's counting command cannot produce the claimed flags | **Confirmed reproducibility gap** | Filed `reports/round-43/claims.json` has no `before_checks` (lines 27/40/53). O05's demonstration runs an **annotated copy** (`O05:93-196`, `:279-283`). The claim's command `--claims reports/round-43/claims.json` (`claims.json:44`) therefore yields `could-not-evaluate`/exit 3, not O+C STALE. |
| **T5** | The gate's "r43 Ca FRESH" is theater | **Confirmed weak control + a false sub-clause it hides** | The only Ca check is `path_absent reports/round-43/calib/dispositions-r38-r39.json` (`O05:183-192`) — the round's own output, necessarily absent at its baseline. Separately, the four queue rows have **non-null** `verification` at `7ceff59`, so "verification mostly None" is false (§3.2). |
| **T6** | The gate is a two-string lookup / over-claims freshness | **Prototype fails all three trap families; durable tool absent → could-not-evaluate** | O09 T1 llama → false STALE (51 "register" owners); T2 empty declared list → green; T3 annotated tag pins the tag object; prototype selftest 17/19, rc 1 (`O09:25-37`, `:163-184`, `:272-284`). |
| **T7** | Ca misclassifies the provider amendments | **Claim text misstates positions; successor corrects** | Claim says "positions 12/13 skipped" (`claims.json:52`); measured: pos 12 (r44) **re-routed and executed**, pos 13 (r45) **skipped** (`Ca04:89-98`; `Ca06` `PA-47-01`). Ca04/Ca06 use the correct wording; the claims.json sentence does not. |
| **T8** | Ca successor silently drops an item | **Not reproduced** | 5 retrospective bullets + 1 r46-audit schema item, `source_coverage` 5/5 mapped, 1 additional, `dropped: []` (`Ca06` fenced JSON, `loop1_coverage`). Two bullets map to one row by design and say so. |
| **T9** | Seats wrote outside their out paths / staged corpus | **Not observed** | `git status --porcelain` → only `?? reports/round-46/review/` (pre-existing) and `?? reports/round-47/`; no tracked corpus/tools/README edit; corpus 223 / culture-material 25 at every check. |
| **T10** | Baseline drift (the r43 claims.json defect class) | **Not reproduced** | `claims.json:7` = `git rev-parse HEAD` = `6e9a30d`; X05 independently PASS (`X05:13-15`). |

---

## 2. C — coverage

### 2.1 Ownership and the "not carried" wording (T1)

Measured at `6e9a30d` (commands in §8):

```
find corpus/knowledge -iname '*cartograph*' -o -iname '*mapmaking*' -o -iname '*portolan*' -o -iname '*cadastr*' | wc -l   -> 0
ls corpus/knowledge/culture-material/cartography-and-mapmaking.md                                                          -> No such file
grep -rniE '^- topic:.*(cartograph|mapmak|portolan|cadastr)' corpus/knowledge/ | wc -l                                      -> 0
grep -rliE 'cartograph|mapmak' corpus/knowledge/ | wc -l                                                                    -> 2 (both by-product/disclaimer)
grep -rniE 'cartograph|mapmaking' reports/round-*/claims.json reports/round-*/targets.json (r1-46) | wc -l                 -> 0
```

So **no prior round claimed or drafted the topic**, and no entry owns it. That part of the premise is true.

The wording is still wrong on its face. `reports/round-44/scout/K02-gap-scout.md:8` says "**Recommended landing:** `corpus/knowledge/culture-material/cartography-and-mapmaking.md`, total 223 → 224", and `:218-220` gives the slug, sort position and count effect. At r47 that is a prior-round scout file recommending the landing. The claim's `before` (`claims.json:27`) and threshold (`:34`) say "no prior-round proposal"; K01 independently flags the same literal falsehood and recommends the qualified form (`K01:230-239`), as does X00 (`X00:422-430`).

**Verdict:** not a carried-topic *failure* — the r44 seal was a never-drafted, never-landed seed, materially different from the r44 dream candidate that already had a body and a prior slug (`r44 validation` C failure; `R01-44-09`). But the round should not admit the sentence unqualified. Required at integration: record "0 prior-round **claims/drafts**; r44 K02 is the cited, never-drafted seed" in `validation.json`/LOG, and treat the threshold as registry-scoped. A global `grep_absent` over `reports/round-*/` would flag the seed itself; a gate probe must be scoped to the registry files (`X00:426-430`).

### 2.2 Topic fidelity: the lithic-skeleton mission (T2)

The risk is real and independently confirmed. `targets.json:21-23` asks C01 for "the property that makes a map a register + the map-meaning mechanisms + material/trade classes", C02 for "scarcity/prestige + provenance/charter + the **container-name fossil**". That is the r42 lithic wording, not the cartography seed — compare `reports/round-42/cov/C01-entry-1.md:53` ("the property that makes stone a register … the four stone-meaning mechanisms … the container-name fossil"). K02 flagged the mismatch (`K02:220-232`). C02's own interface note admits the headings follow the 15-section mission plan (`C02:32-38`).

What the drafts actually contain, measured:

- C01 sections: frame / "what makes a map a register — the five-condition test" / "map-meaning mechanisms — six decisions" / "material and trade classes — the map-object typology" (`C01:109,152,232`). The five-condition test is a real cartographic definition (ground index, bounded notation, structural selection, conventional readability, reproducibility); the object table correctly dispositions T-O diagrams, field books, paintings, stick charts and mental maps (`C01:120-145`).
- C02 sections: survey-to-symbol chain / scarcity and prestige of survey / mapmaker trade / provenance and charter / map-word fossil (`C02:40,167,248,323,397`). §9 is a genuine map-lexicon section (*mappa*, *charta*, atlas, portolan, cartouche, legend, scale, table, plat, gazetteer), not a stone section; it cites the vessel ear/lug and *sarcophagus* analogues as comparisons, not as subject (`C02:399-443`).
- In-fence citation resolution: C01 13/13 refs resolve; C02 19/19 refs resolve; C03 18/18 refs resolve (my script, §8). No invented path or out-of-range line. The `stone`/`gem` hits are legitimate (boundary stones, slate as a map medium, the *sarcophagus* etymology); none is a lithic-register residue.

**Residual integration risk:** the assembled entry will have **15 sections**, not the seed's 10 (`K02:64-81`). The extra apparatus (five-condition test, six decisions, seven links, five roles/four products/three customers) is coherent but increases the chance of duplicated tables. C02 itself warns that §4 and §9 could both run the *mappa/charta* table (`C02:32`); C01 deliberately leaves the etymology to §9 (`C01:295`). C03's cross-references assume the 15-section numbering (`C03:9`) and must be reconciled at assembly. This is an **integration audit condition**, not a confirmed filler trade: C06/C08/R03 must read the assembled body, and C07's content legs are still `could-not-evaluate` (C07 verdict table `:12-22`; its §7 re-runnable check was written before the drafts existed).

**Verdict:** the mission was lithic-shaped; the drafters adapted it to cartography. Do not land until the assembled body passes C06/C08/R03 and the §4/§9 duplication is checked.

### 2.3 README rev-2.5 and the rev-2.4 record (T3)

The arithmetic defect is confirmed: `corpus/README.md:10-11` reads `25/23/25/29/24/94 → 25/23/26/25/24/94` = 220 → **217**, while the live footer (`:548`) is `25/26/25/29/24/94` = 223. The r28 sweep is green over it because it never parses revision prose (`sweep.py:136-210`; no vector leg). C09 reproduces this with a control: reverting the defect leaves the sweep `ok: true` (`C09:51-59`, `:223`).

C09's repair is the right *forward-correction* form in substance: it edits the 2.4 token to `25/26/25/29/24/94` and **quotes the original 217 value, with the slot diagnosis, in the rev-2.5 block** (`C09:83-96`, `:61-70`). The defective reading remains retrievable as prose, matching the rev-1.8 "superseded reading preserved" precedent (`README:550`). C10's staged model also quotes the defective value in its rev-2.5 note (`C10:156-159`); its control D correctly says the sweep is blind (`:133-135`). The open question is the in-place edit of the 2.4 block, not whether the 217 value survives: both models preserve it in prose. C09's form is the clearer record because the correction sentence sits in the 2.5 block; do not apply a transform that drops the quote. C05's artifact prints the post-landing vector slot-swapped as `26/26/25/29/24/94` in three places (`C05:273,275,295`); C10 catches and corrects it (`C10:189-206`). **Do not copy C05's vector.** The correct landing vector is `25/26/26/29/24/94` (culture-material +1; `K02:204`, `P01:156`, `C10:193`).

**Verdict:** the repair is acceptable only with C09's preservation note; the rev-2.4 block is a dated record and the round should not let C10's silent transform become the applied edit. The claim's non-goal ("forward correction, not a rewrite", `claims.json:74`) supports C09's form.

### 2.4 Collision and landing mechanics (no trade)

- Target path absent at HEAD; `git cat-file -e` fails; `git check-ignore` says not ignored; a scratch clone confirms `A`, not `M` (`C05:160-196`).
- 21 couples tokens, all Tier-1 direct, all 21 basenames unique (`C13:10,53-92`); expected resolver delta +1 entry/+21 refs/+21 direct (`C13:103-120`).
- C04's `- topic:` value is 766 chars, sha256 `bc7274f4…f4495`, **byte-equal** to the r44 seed line (`C04:211-219`; my check §8). All six sha-pinned anchors match the live blobs; all 23 cited anchors exist.
- C10's staged 224 tree is sweep-green: rows 224 == files 224, footer `25/26/26/29/24/94`, all legs empty, exit 0 (`C10:95-109`). Its fixture body is explicitly not the draft (`C10:66-70`).

No collision, no overwrite, no second owner at this cut.

---

## 3. O — operability

### 3.1 The counting command does not run the claimed demonstration (T4)

The claim's acceptance command (`claims.json:44`) is:

```
python3 tools/harness/claims-freshness.py --claims reports/round-43/claims.json
```

The filed r43 claims have no `before_checks` — only free prose (`reports/round-43/claims.json:27,40,53`). Under the round's own contract a claims file with no declared checks is `could-not-evaluate`, exit 3, never a STALE verdict (`R01-44:243-247`; `P01:266-269`; `claims.json:47`). O05's demo does **not** run that file: it builds an annotated copy with `before_checks` and runs its scratch copy (`.scratch/o05/r43-claims-annotated.json`), with the suggested integrator target `reports/round-47/calib/r43-claims-annotated.json` (`O05:93-196`, `:279-283`; the calib copy did not exist at this read). O09 independently ran the prototype on the real r47 claims file and got `[O] UNVERIFIABLE (0/0)`, `[Ca] UNVERIFIABLE (0/0)`, exit 3 (`O09:328-333`).

**Consequence:** the claim is not satisfied by its own counting command. Either the tool must ship a documented sidecar/overlay mechanism and the validation must run it, or the claim's command must be read as the annotated-copy command. The honest receipt must name the annotated file and its sha256; the current `count` command cannot distinguish "verified stale" from "no checks". This is a **reproducibility trade**, not a data error — O05 is transparent about the annotated copy, but the claim's acceptance surface does not carry that qualification.

### 3.2 The r43 Ca control is tautological — and hides a false sub-clause (T5)

The demo's Ca check is:

```
{"probe_kind":"path_absent","target":"reports/round-43/calib/dispositions-r38-r39.json","expect":true}
— O05:183-192; also Ca01:62-70, X00:165-170
```

That path is the very artifact r43 Ca promises to file; it cannot exist at r43's baseline. The probe therefore returns `true` for **any** calibration claim shaped this way, regardless of whether its premise is true. The verdict "Ca FRESH" is a statement about the baseline being *before* r43, not about the premise "the four r38/r39 rows have no per-finding disposition".

Worse, the premise contains a measurable sub-clause that the probe never tests:

> "four r38/r39 carried rows … have no per-finding disposition on record (all carried-with-owner, **verification mostly None**)"
> — `reports/round-43/claims.json:53`

Measured at `7ceff59` from the filed queue (`git show 7ceff59:reports/round-40/op/defect-queue-v2.json`):

| row id | class | verification at `7ceff59` |
|---|---|---|
| `r38-O02-fragment-defects` | `carried-with-owner` | non-null: "O03 measured each defect on the filed artifacts (command outputs at O03 §4)" |
| `r38-O08-fragment-defect` | `carried-with-owner` | non-null: "O03 diffed O08's tree against O01's declared patch (one hunk)" |
| `r38-O07-empty-fragment` | `carried-with-owner` | non-null: "measured at HEAD by this seat" |
| `r39-review-findings-disposition` | `carried-with-owner` | non-null: "this seat's grep at HEAD; R01 verdict table read" |

So "verification mostly None" is **false (0/4 None)**. The class claim (no per-finding disposition) is arguably still true — the rows are `carried-with-owner`, not `fixed-with-evidence` — but the parenthetical is contradicted by the filed bytes. A correct, substantive Ca check would measure the four rows' class/verification and would report a **mixed** result, not the clean `FRESH 1/1` the demo prints. The demo's baseline-scoping lesson (§5.2: flip at HEAD) is real and useful, but it proves *when* the artifact exists, not *whether* the premise holds.

**Required fix:** (a) keep the r43 Ca as a labelled **trivial baseline control**, not as the semantic negative control; (b) use O06's r44 fixture as the real fresh-claim control (it is substantive: 9 clauses, 6 probe kinds, discriminates at HEAD, `O06:22-30,52-64`); (c) either add a substantive check on the four queue rows (e.g. count of `fixed-with-evidence` among those ids = 0, or read their `verification` fields) or record the "verification mostly None" parenthetical as a **precision correction** in the Ca01 row. Do not present "Ca FRESH" as proof the gate does not over-fire.

### 3.3 Gate theater and over-claim (T6)

The durable tool does not exist at this cut (`ls tools/harness/claims-freshness.py` → no such file; `O10:18-30`). The only implementation is the r44 `.scratch` prototype (`dd88d9e1…`), and it is nonconforming on every trap family:

- **T1 novel phrasing:** "the llama-herding register slot is unbuilt" → mined topic `register` → 51 owner hits → **false STALE**, exit 2; the phrase itself has 0 owners (`O09:68-105`).
- **T2 polarity:** unknown `probe_kind` and missing `expect` become **STALE**, a contradictory `expect:true` is silently ignored as **FRESH**, and `freshness_probes: []` falls back to prose mining and can exit **0** (`O09:163-184`) — the direct violation of "could-not-evaluate != green" (`claims.json:47`).
- **T3 tag baseline:** an annotated tag reports the **tag-object** sha as the baseline; a `^{tree}` is silently accepted; missing/blob revs exit 1, not 2 (`O09:238-284`).
- **Selftest:** 17/19, exit 1 (`O09:334-336`; my re-run confirms).

The prototype's r43 flags are nevertheless real (O stale 0/2, C stale 2/3, Ca FRESH 1/1) and the reference evaluator reproduces them at `7ceff59` (`O05:11-19,205-244`). So the method is proven; the deliverable is not.

**Over-claim risk in the durable implementation:**

1. **Capability probes must not be substring lookups.** `git grep -l 'four-class' c9f4eaa -- tools/` returns **2** files that do not implement a four-class census: `tools/harness/receipt_guard_adoption.py:1192` ("live-declared-hazard-four-classified") and `tools/gates/expected/d4-typed-labels-check-gate/.../12-rank-rules.yml:698` ("'four-class' style tidy pyramid"). A capability registry that greps `four-class` would report the capability present at `c9f4eaa` and turn the r44 negative control **STALE** — failing the claim's own "does not flag a fresh claim" threshold. O06's fixture scopes the probe to the extractor path (`O06:116-119`), which avoids this specific trap; the durable registry must keep that scoping and use signatures like `four_class_totals` / `def couples_block`, not the hyphenated substring.
2. **`topic_owner_absent` must anchor on the topic line and the declared phrase.** A corpus-wide `grep lithic` returns 24 files because of "Neolithic"; the anchored `- topic:.*lithic` returns exactly the one owner at `7ceff59`. For cartography, `\bmap\b` returns 11 owners; the probe must use `cartograph|mapmak|portolan|cadastr` (X00:85-87). The sidecar must declare the vocabulary; the tool must not mine generic tokens (`O09:142-148`).
3. **Exit codes must be pinned once.** The claim only says "non-zero on stale"; P01 specifies 0/1/2/3 (`P01:266-269`), O10 measures the prototype's inversion (stale 2, malformed 1, CNE 0 under a flag) and supplies a 14/14 conformance suite (`O10:18-49`). The validation must assert the P01 table, not just non-zero.
4. **The O claim's historical parenthesis is imprecise.** `claims.json:40` says "r43 and r44 both declared claims on stale premises (green resolver existed; owned/carried topics)". r44 O's `before` was true and its claim landed `improved`; r44 C failed for a **carried candidate**, not an owned topic (`X00:432-440`; `Ca01:129-160`). The actionable clause ("a scratch prototype… red-selftest and non-durable") is true, so the claim is not stale under its own narrow contract, but the gloss must not be repeated in LOG/validation. If the gate is ever run on r47's own claims with a substantive r44 probe, this sentence would be the first thing to flag — the round should correct it by record, not by editing the claims file.

### 3.4 O verdict at cut

`could-not-evaluate` on the durable deliverable; **unchanged**, not improved. No harm: the absent tool changes no live behavior; the prototype is `.scratch` only; no corpus/ledger bytes moved. All five `after_required` properties are unproven until a durable tool lands and O08/V02 run the O09 acceptance matrix. The acceptance receipt must record: tool sha, selftest count/rc, the annotated-copy demo (with its sha), the O06 negative control, the O09 trap matrix, and the exact exit codes.

---

## 4. Ca — calibration

### 4.1 Item mapping (T8) — no drop, but not "one row per bullet" literally

The retrospective has **five** bullets (`r46:43-53`): freshness gate; stale-premises pattern; resolver latent edge; antigravity outage; zai exhaustion. Ca06's current fenced JSON has **3 defect rows + 2 provider amendments** and an explicit `loop1_coverage` block: `retro_carried_bullets: 5`, `retro_bullets_mapped: 5`, `additional_loop1_close_items: 1`, `mapping` lists all five lines plus the r46 audit schema item, and `not_requeued` gives reasons for r44 C, r44 Ca, and the r42/r43 already-dispositioned items. The two freshness bullets map to one row **by design**; the row's `class_boundary` carries the narrow/broad distinction (`Ca06` JSON; `Ca01:129-160`). The sixth item (MANIFEST schemas) is explicitly **not** back-attributed to the retrospective; Ca03 corrects its provenance (`Ca03:25-38`; `Ca06` `provenance_correction`).

**Verdict:** no silent drop. The claim's phrase "one row per loop-1 carried item" is satisfied as a *disposition mapping*, not as a literal 5-row array; the successor must keep the `source_coverage`/`mapping` block so the fold is visible. A reader who counts only `rows[]` (3) will think items are missing; the `provider_amendments` array is separate because the parent queue's vocabulary is rule-breach-only (`Ca06` `not_a_defect_row_reason`). The integration note should say this explicitly.

### 4.2 Provider wording (T7) — claim text wrong, successor right

`claims.json:52` says "the antigravity-lane outage (positions 12/13 skipped)". The filed record says:

- position 12 (r44) scheduled antigravity, aborted twice with zero seat output, **re-routed to opencode-go and executed** (14 seats filed; `rejected-honest-stop`);
- position 13 (r45) **skipped** per operator ruling; `reports/round-45/` does not exist.

Ca04 measures this and corrects the mission wording (`Ca04:89-98`); Ca06's `PA-47-01` uses "pos 12 re-routed and executed, pos 13 skipped" and cites the fleet row via Ca05 (`Ca05:146-158`). **Verdict:** the successor is correctly classed as a named deviation, not a defect row; the **claims.json sentence remains an overstatement** and must be corrected in the validation/LOG wording, not by editing the claims file.

### 4.3 Successor integrity and digest drift

- Parent pin: `dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907`, unchanged at `ac47c78` and `6e9a30d` (`Ca06` JSON `G1-parent-pin`; my `sha256sum` matches). The r41 in-place edit is a filed fact, not a second edit by this successor (`Ca06` `parent_history`).
- `source_fragments` now includes Ca01–Ca04 and the retrospective. Current digests match for Ca01/Ca02/Ca03/Ca04; **Ca05's pinned digest is stale** (`747c0fdb…` pinned, current `31d24423…`), because Ca05 was revised after Ca06's assembly. Ca06's `G8-source-digests` says to re-hash and reconcile; the integrator must re-pin Ca05 (and Ca04 if it moves again) or record the digest-bound scope. This is normal open-round drift, not a defect, but an unreconciled G8 would make the successor's provenance claim false.
- Ca05's verdict is digest-bound to the versions it read: it currently PASSes Ca01–Ca04 and the parent, but its Ca04 pin (`5f370306…`) is the pre-revision Ca04, not the current `94b99878…`. Its Ca01/Ca03 facts remain valid; the final integration should either re-run Ca05 on the final bytes or cite the digest-bound scope explicitly.
- The successor is a `.md` with a fenced JSON (38.6 KB block, parses; 3 rows, 2 amendments, coverage 5/5+1). The claim allows `.json` **or** `.md` (`claims.json:54`), so the `.md` satisfies the letter; Ca06's own instructions ask the integrator to extract it to `queue-successor-r47.json`. Whichever is filed, the receipt must name the exact path and sha, and no filed byte may be edited.

### 4.4 Ca verdict at cut

**could-not-evaluate on landing / unproven-better.** The successor content is complete and correctly classed, the parent is pinned and untouched, and no filed byte was edited. It is not yet a durable machine artifact at the claim's named `.json` path, and its fragment digests are mid-flight. No axis harm; no calibration move until the artifact is filed and Ca05/Ca07 re-verify the final digests.

---

## 5. Cross-claim and write-surface checks

| check | measured | verdict |
|---|---|---|
| `claims.json.baseline_commit` == HEAD | `6e9a30d` == `6e9a30dca8…` | PASS |
| corpus total / culture-material | 223 / 25 at every check | PASS (pre-landing) |
| tracked corpus/tools/README edits | `git status --porcelain` → only `?? reports/round-46/review/`, `?? reports/round-47/` | PASS |
| parent queue untouched | `sha256sum` = `dfc9265d…`; `git status` clean | PASS |
| filed r43 claims unchanged | sha `9662e2bd…` (`O05:7`); no edit by any seat | PASS |
| resolver witness unchanged | `43ce341f…`; `--selftest` 27/27 | PASS |
| r28 sweep live | rows 223 == files 223, exit 0, sha `7c788a1d…` | PASS |
| README revision history arithmetic | rev 2.1 211→212, 2.2 212→216, 2.3 216→220, 2.4 220→223, 2.5 223→224; blocks match (`README:14-45`) | PASS |
| Ca06 JSON parses | 1 fenced block, 3 rows, 2 amendments, coverage 5/5+1 | PASS |

No scope bleed: no canon/lore/packet changes; `PROVINCE.md` untouched; the only prospective corpus delta is the single C entry + README.

---

## 6. Axis verdicts at this cut

| axis | verdict | reasoning |
|---|---|---|
| **coverage** | **unchanged** (premise clean; landing pending) | 223 entries; cartography 0 owners; drafts and staged sweep are green, but no byte has landed. C's ownership premise is true; the carried-wording needs the qualified record; the content needs C06/C08/R03. Post-landing 224 remains **could-not-evaluate**. |
| **operability** | **unchanged / could-not-evaluate** | The durable gate is absent; the prototype is red (17/19) and fails all three trap families. The method and acceptance matrix are real; no move is delivered. |
| **calibration** | **unproven-better** | Successor drafted with a 5+1 mapping and a pinned parent; not yet filed at the claim's durable path; digest drift to reconcile. |

No axis is **harmed** by what is on disk at this read.

---

## 7. Integration gates (what closes each trade)

```bash
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
# C — apply entry then README atomically; never C10's transform without C09's note
find corpus/knowledge -name '*.md' | wc -l                       # 224
ls corpus/knowledge/culture-material/*.md | wc -l                # 26
python3 -B reports/round-28/readme/sweep.py                      # rows 224 files 224; footer 25/26/26/29/24/94; exit 0
grep -n 'rev 2.4' corpus/README.md                               # the rev-2.5 note must quote the 217 defect
grep -c 'cartography-and-mapmaking' corpus/README.md             # 1 row
# O — the receipt must name the annotated copy, not only the filed claims
python3 tools/harness/claims-freshness.py --selftest             # green, count computed
python3 tools/harness/claims-freshness.py --claims reports/round-47/calib/r43-claims-annotated.json  # O,C STALE; Ca labelled trivial; exit 1
python3 tools/harness/claims-freshness.py --claims reports/round-47/calib/negative-control.claims.json  # FRESH; exit 0
# Ca — extract the fenced JSON or accept the .md, then re-pin
python3 - <<'PY'
import json,hashlib
p='reports/round-47/calib/queue-successor-r47.json'  # or the Ca06 .md path
d=json.load(open(p))
assert d['parent_sha256_at_assembly']=='dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907'
assert len(d['rows'])==3 and len(d['provider_amendments'])==2
assert d['loop1_coverage']['retro_bullets_mapped']==5
assert hashlib.sha256(open('reports/round-40/op/defect-queue-v2.json','rb').read()).hexdigest()==d['parent_sha256_at_assembly']
print('successor OK')
PY
```

Also: re-run Ca05 on the final Ca01–Ca04 digests (or cite its digest-bound scope); keep the r43 Ca probe labelled trivial; use O06 as the semantic negative control; and record the "0 prior claims/drafts, r44 K02 is the seed" qualification in `validation.json`/LOG.

---

## 8. Evidence appendix (measured commands)

```text
$ git rev-parse HEAD -> 6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe
$ find corpus/knowledge -name '*.md' | wc -l -> 223
$ ls corpus/knowledge/culture-material/*.md | wc -l -> 25
$ python3 -B reports/round-28/readme/sweep.py -> 223==223, exit 0, readme_sha256 7c788a1d…
$ python3 -B reports/round-28/readme/sweep.py --selftest -> 12/12, exit 0
$ find corpus/knowledge \( -iname '*cartograph*' -o -iname '*mapmaking*' -o -iname '*portolan*' -o -iname '*cadastr*' \) | wc -l -> 0
$ grep -rniE '^- topic:.*(cartograph|mapmak|portolan|cadastr)' corpus/knowledge/ | wc -l -> 0
$ grep -rliE 'cartograph|mapmak' corpus/knowledge/ | wc -l -> 2
$ grep -rniE 'cartograph|mapmaking' reports/round-*/claims.json reports/round-*/targets.json (excluding r47) | wc -l -> 0
$ grep -rliE 'cartograph|mapmak' reports/round-*/scout/ -> only reports/round-44/scout/K02-gap-scout.md
$ git grep -inE '^- topic:.*lithic' 7ceff59 -- corpus/knowledge -> myth-symbol/mineral-stone-symbolism.md:5
$ git grep -l 'basename-couples' 7ceff59 -- tools/ -> tools/harness/couples-reference-extractor.py
$ git grep -l 'def couples_block' c9f4eaa -- tools/ -> tools/harness/couples-reference-extractor.py
$ git grep -l 'four-class' c9f4eaa -- tools/ -> receipt_guard_adoption.py:1192, d4-.../12-rank-rules.yml:698
$ git grep -l 'four_class' c9f4eaa -- tools/ -> (none)
$ git show 7ceff59:tools/harness/couples-reference-extractor.py | sha256sum -> d8d23a26…79cf1
$ python3 .scratch/x01_extractor_7ceff59.py --selftest -> 8 PASS, rc 0
$ python3 .scratch/ca01/claims-freshness.py --selftest -> 17/19 FAIL, rc 1
$ python3 .scratch/ca01/claims-freshness.py --claims reports/round-43/claims.json -> O STALE 0/2, C STALE 2/3, Ca FRESH 1/1, exit 2
$ git show 7ceff59:reports/round-40/op/defect-queue-v2.json | python3 -c ... -> the four rows: class carried-with-owner, verification non-null 4/4
$ sha256sum reports/round-40/op/defect-queue-v2.json -> dfc9265d…a3253907
$ sha256sum tools/harness/basename-couples-resolver.py -> 43ce341f…8ad64
$ python3 tools/harness/basename-couples-resolver.py --selftest -> 27/27
$ python3 tools/harness/basename-couples-resolver.py --census -> entries=223 refs=2730, 2556/166/0/7 +1
$ sha256sum reports/round-47/cov/C04-entry-header.md -> cb5a7489…b68b0
$ python3 -c "topic value sha" -> 766 chars, bc7274f4…f4495 (== r44 seed)
$ python3 -c "C04 couples tokens" -> 21 tokens, 0 unresolved
$ sha256sum /home/vgpnk/Projects/shokunin/MANIFEST.json -> 509305c8…24e32 (281 rows; S1 33-42 11 keys; S2 43,44,46 15 keys)
$ python3 -c "parse Ca06 fenced JSON" -> rows 3, provider_amendments 2, coverage 5/5+1
$ git status --porcelain -> ?? reports/round-46/review/ ; ?? reports/round-47/
```

**Limits.** No network; no external cartography source was fetched or inspected (all Tier B remains `to-verify`). No durable O tool existed at this cut, so every O verdict is a contract/evidence judgment, not a run of the deliverable. The C post-landing state is staged, not live. Seat artifacts revised after `18:07:49Z` are outside this critique; the parent should re-run the §7 gates at close.

No filed byte was edited by this seat. Nothing under `corpus/` was staged. The only write is this file.
