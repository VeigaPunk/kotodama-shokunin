# C14 — worked-example verification (claim C): FAIL on the assembled entry's example, with the gate and the r47 negative control

- Seat **C14** | role verifier | claim **C** (coverage) | round 48, loop 2, position 2.
- Out path: `reports/round-48/cov/C14-example.md` (this file). This is my only durable write.
- Baseline: HEAD `a01405dd36367292255c2652ac0a601f4cd6a0af` (`git rev-parse HEAD`) = `reports/round-48/claims.json:7`.
- Mission (verbatim, `reports/round-48/targets.json`, seat `C14`): *"Worked-example verifier: the NON-CANON worked micro-example is internally consistent (one update rule, stated once), demonstrates the register method, is declared invented."*

## Verdict in one line

**FAIL — blocking, on the derive leg** of the example actually assembled into the entry, `reports/round-48/cov/C01-entry.md:246-269` (24 lines, block sha256 `b85777ff5daba10021557f4d59d0e68b468355720bb34a41170c7c31aa81de46`). The example is **untagged**: 0 `DR-CM-` tokens, nine moves that name no build step, and a closing consequence sentence that hangs on no row (`:269`). Worse, the rule it calls decisive — the update rule (`:260`, `:269`) — has **no decision row** (the record at `:239-244` stops at DR-CM-06) and **no build-order step** (`:223-231`; step 9 is the calibration audit). The example teaches a rule the entry does not define. This is r47's F-2 defect class recurring at assembly. Label, invented frame, one-rule consistency, rejection and citations all pass; the length and two cross-section wording/coherence issues are P2.

The separately filed `M01-example.md` example **passes** the gate (with three P2 fixes), but it is **not** the bytes C01 assembled. The integrator has two viable repairs; §8 names them.

---

## 1. Receipt (schema per `corpus/knowledge/verification/worked-example-verification.md:44`)

| Receipt field | Value |
|---|---|
| Entry and digest at check time | `reports/round-48/cov/C01-entry.md`, file sha256 `4c2815a766f12926ba14e14e2b164a8f65245a246223ae4258993e0a831c272d` (473 lines); example block `:246-269`, sha256 `b85777ff…81de46` (2,798 bytes); entry fence `:69`–`:298` |
| Class | **(c) invented sectioned example** (`worked-example-verification.md:52`): nine staged moves + a counterfactual table + one consequence line |
| Rules named | **none** — `grep -c 'DR-'` on `:246-269` → **0**; the entry's record defines only `DR-CM-01..06` (`:239-244`) |
| Consequence↔rule map | **absent**: `:269` names no id |
| Controls run | W1–W10 (§5) on the assembled block; r47 negative fixture (§6); M01 fragment (§8) |
| Label check | `NON-CANON` in the heading (`:246`) and the bold declaration (`:248`) |
| Freshness basis | by construction: the Vessa delta, its board and temple archive are invented and appear in no other section |
| Auditor and date | C14, 2026-10-19 |
| Re-audit trigger | any edit to `:246-269`, to `:223-231` (build order), or to `:239-244` (decision record); re-run on the assembled bytes |
| Status | **debt record, not a clearance** (`worked-example-verification.md:44`, DR-WE-09) |

---

## 2. Baseline measured (not asserted)

Commands run from the lane root, 2026-10-19, `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`.

```text
$ git rev-parse HEAD
a01405dd36367292255c2652ac0a601f4cd6a0af
$ find corpus/knowledge -name '*.md' | wc -l
223
$ ls corpus/knowledge/culture-material/*.md | wc -l
25
$ ls corpus/knowledge/culture-material/cartography-and-mapmaking.md
ls: cannot access '...': No such file or directory
$ python3 -c "import glob,statistics; L=[sum(1 for _ in open(f)) for f in glob.glob('corpus/knowledge/culture-material/*.md')]; print(len(L),min(L),statistics.median(L),max(L),sum(L))"
25 103 149.0 221 3756
```

House example-section lengths (heading to next H2), measured by line range:

| Entry | Section | Lines |
|---|---|---:|
| `myth-symbol/divination-omen-systems.md` | `:161` | 6 |
| `myth-symbol/purity-pollution-boundary-systems.md` | `:158` | 6 |
| `myth-symbol/symbolism-synthesis-method.md` | `:158` | 11 |
| `verification/contact-strata-verification-gate.md` | `:149` | 12 |
| `myth-symbol/binding-speech-complex.md` | `:248` | **19 (house max)** |

The right-sized spec budgets **33 lines for its §8 "build + example"**, which must also hold the nine build steps (`reports/round-48/scout/K01-rightsized-spec.md:91`). The assembled entry's build order is 14 lines (`C01-entry.md:221-234`) and its example 24 (`:246-269`) — 38 combined. r47's example was 47 lines (`reports/round-47/cov/C03-entry-c.md:107-153`).

---

## 3. What "one update rule, stated once" means mechanically

The rule is stated once when the example contains **one canonical update cell or bullet per sheet**, and every other mention either (a) is a pointer to that cell/row, or (b) is a byte-identical substring of it. A table cell that paraphrases the trigger is a second statement and is a defect, because a reader cannot tell which text governs.

Allowed: the build-order step (definition), the decision row (decision), and the example cell (instantiation) each say the rule in their own register. **Not allowed:** two different trigger values inside the example, or a rule the example makes decisive that has no decision row at all.

---

## 4. The ten controls

W1–W7 are blocking (the r47 B7/F-1/F-2 class). W8–W10 are quality-class controls (bleed and over-build); a failure there is a must-fix before landing but not a factual defect.

| ID | Control | Prefilter command (on the example block) | Pass condition |
|---|---|---|---|
| **W1** | Label | `grep -n 'NON-CANON'` | ≥1 hit inside the heading or first two lines |
| **W2** | Invented frame | `grep -niE 'invented|working labels|not canon|design exercise|no canon'` | ≥1 sentence declaring the labels/elements invented |
| **W3** | One update rule | find the canonical update line — `^\s*[-*]\s*\*?Update` **or** a row beginning `\| *Update`; collect trigger tokens | exactly one canonical statement per sheet; singleton trigger; other mentions are pointers or verbatim |
| **W4** | Rule names at each step | `grep -c 'DR-'`; inspect each move | every move names `step n / DR-<id>` in ascending order; count ≥ number of moves |
| **W5** | Derive leg | inspect the consequence list | each consequence ends with `(DR-<id>)` (`worked-example-verification.md:39`) |
| **W6** | Reject leg | inspect the reversal | ≥1 use the example's own class definitions forbid; the refusal is stated |
| **W7** | Citations resolve | `grep -o 'corpus/[A-Za-z0-9_./-]*\.md:[0-9]*'` | every path exists, `line ≤ wc -l`, content supports the use |
| **W8** | Living-practice screen | `grep -niE 'lienzo|songline|polynesian|aboriginal|maori'` | none used as a template inside the example |
| **W9** | Length | `wc -l` on the block | ≤25 hard ceiling; ≤20 preferred (house max 19) |
| **W10** | No mechanism restatement | read against the build-order prose | the example supplies concrete values, not method prose |

W2, W6, W8 and W10 require a reader; the receipt must quote the sentence that satisfies each, not assert the verdict.

---

## 5. Controls on the assembled example

```text
$ sha256sum reports/round-48/cov/C01-entry.md
4c2815a766f12926ba14e14e2b164a8f65245a246223ae4258993e0a831c272d
$ sed -n '246,269p' reports/round-48/cov/C01-entry.md | grep -c 'DR-'
0
$ sed -n '246,269p' reports/round-48/cov/C01-entry.md | grep -c '^|'
5        # header + separator + 3 counterfactual rows
$ grep -n 'DR-CM-' reports/round-48/cov/C01-entry.md
239-244: DR-CM-01 … DR-CM-06   (six rows, no update rule)
```

| Control | Result | Evidence |
|---|---|---|
| W1 label | **PASS** | `:246` heading carries `NON-CANON`; `:248` bold declaration |
| W2 invented frame | **PASS** | `:248` "invented … nothing here is a claim about a real people" |
| W3 one update rule | **PASS** | canonical bullet `:260` ("stated once"); storm test `:261` applies it without a second trigger; the only other `re-survey` is the explicitly counterfactual table row `:265` |
| W4 rule names | **FAIL (blocking)** | 0 `DR-` tokens; nine moves (`:252-260`) name no step and no row |
| W5 derive leg | **FAIL (blocking)** | `:269` "the update rule, not the drawing, decides the dispute" names no row; no consequence carries an id |
| W6 reject leg | **PASS (weak)** | `:261` the board applies the rule and refuses to void the year-3 assessment — an adjudication, not a class-entailed refusal |
| W7 citations | **PASS** | no in-repo cite inside the example; none required (invented materials) |
| W8 living-practice | **PASS** | no real tradition used as template |
| W9 length | **FAIL (P2)** | 24 lines (25 with the separating blank) vs ≤20 preferred; 38 with the build order vs K01's 33-line §8 budget |
| W10 restatement | **PASS** | concrete values: 100-pace legs, 1:5,000, 1:25,000, twelve copies, year-3 storm |

**Verdict: FAIL.** Seven of ten controls pass (W4 and W5 blocking, W9 P2), and the two blocking failures are the exact half of r47's B7 that C01's own B7 audit row omits: that row addresses only the three-way wording, not the absent rule ids (`C01-entry.md:354`; self-audit §5.5 at `:436-440`).

### 5.1 Findings

| ID | Severity | Location | Finding | Fix |
|---|---|---|---|---|
| **F-1** | **Blocking** | `C01-entry.md:246-269`, `:239-244`, `:223-231` | The example's nine moves are untagged (0 `DR-` tokens), the consequence line names no row, and the rule the example makes decisive — the update rule at `:260` — has neither a decision row (record stops at DR-CM-06) nor a build-order step (step 9 is the calibration audit). The example therefore cannot derive its own punchline, and instantiates a rule the entry does not define. | Add **DR-CM-07 "fix the update rule: re-survey trigger, margin/variant entry, superseded-copy rule"** to `:239-244`; add the update step to the build order (renumber or fold the audit into recheck); tag each of the nine moves `step n / DR-CM-0n`; end `:269` with the row ids, e.g. `(DR-CM-01, -05, -07)`. |
| **F-2** | P2 | `:246-269` | 24 lines vs ≤20 preferred; with the 14-line build order the §8 block is 38 vs K01's 33 (`K01-rightsized-spec.md:91`). The entry's fenced body is 227 content lines (228 with the trailing blank), still under the 250 claim threshold. | Trim the counterfactual table to two rows or compress the storm test; do not cut the nine moves or the rule sentence. |
| **F-3** | P2 | `:257`, `:269`, `:180`, `:216` | The temple enclosure is called a "hatched blank" and "the blank is a legal symbol", but it is positively drawn and labelled. The entry carries **two blank taxonomies**: §5 lists "unknown interior, chartered exemption, taboo site, rival claim" (`:180`), while §8 lists six different silence classes (`:216`), none of which is chartered exemption. The example instantiates a class §8 does not own. | Reconcile the lists (add "chartered exemption" to §8's six, or make §5 point to §8); keep the example's use, which is coherent with §5. |
| **F-4** | P3 | `:253`, `:254` | "closing error ±1% → ±0.75 m per leg" is correct only if a pace is 0.75 m; the pace length is never stated. The rest checks: 0.2 mm × 5,000 = 1 m; × 25,000 = 5 m; 0.75 < 1.0. | State "100 paces ≈ 75 m" once, or give the leg in metres. |
| **F-5** | P3 (audit) | `:436-440` vs file | §5.5 cites "§11 line 191/192/196"; those are **fence-relative** (entry line 1 = file `:70`), while the live file has the rule at `:260`, the test at `:261`, the counterfactual at `:265`. Not wrong if read as entry-relative, but a `path:line` reader will miscite. | Give both forms: "§11 (entry line 191 = `C01-entry.md:260`)". |
| **F-6** | P3 (audit) | `:438` | §5.5 checks "1:2,500 limit 0.5 m → survey binds", but the example uses 1:5,000 and 1:25,000 only. The check is true arithmetic about a scale the example does not instantiate. | Drop it or add the 1:2,500 variant to the example. |

### 5.2 What the example does well

- **The update-rule wording is clean.** One bullet, one trigger ("when the levy year turns"), and the storm test applies it without restating a variant. The counterfactual table is explicitly labelled "If the rule were…", so it is not a second statement. This half of r47's B7 is genuinely fixed.
- **The storm test is a real adjudication.** The board applies the written rule against a sympathetic claim (a flooded parcel) and rules for the rule; the margin entry becomes evidence for the next year. That is the institution doing work, not a vignette.
- **Two forms from one survey** demonstrates the entry's form-by-question claim with concrete values (cadastral 1:5,000 vs chorographic 1:25,000), and the precision comparison is arithmetically sound.
- **The invented frame is honest.** No real tradition is used as a template; the polity, place and numbers are declared invented.

---

## 6. Negative control — r47's example, re-measured live

`reports/round-47/cov/C03-entry-c.md:107-153` (47 lines, filed bytes read-only):

```text
$ sed -n '107,153p' reports/round-47/cov/C03-entry-c.md | grep -c 'DR-CT-'
0
$ grep -n 'Update:\|update |\|re-survey\|levy year turns\|after every breach' reports/round-47/cov/C03-entry-c.md
123: - *Update:* re-survey after any storm that breaches a dike; ...
135: - *Update:* after a storm the guild sends a sounding boat; ...
137: **The storm.** ... the re-survey is not due until the levy year turns ... (re-survey after every breach, not every levy year) ...
150: | update | after a dike breach, per levy year | after a storm, by sounding boat |
```

Trigger tokens per mention: `:123` = {storm, breach}; `:137` = {storm, breach, levy year, new channel}; `:150` = {storm, breach, levy year}.

| Control | r47 result | Basis |
|---|---|---|
| W1 label | **PASS** | `:107` heading, `:109` working-labels declaration |
| W2 invented frame | **PASS** | `:109` "A demonstration, not a world decision … none of it is canon" |
| W3 one update rule | **FAIL (blocking)** | Map A stated three incompatible ways at `:123`, `:137`, `:150` |
| W4 rule names | **FAIL (blocking)** | 0 `DR-CT-` tokens |
| W5 derive leg | **FAIL (blocking)** | consequences (a)–(f) at `:152` carry no rule id |
| W6 reject leg | **PASS** | the storm: a channel is not a taxable class; land ownership is not navigational |
| W7 citations | **PASS** | `writing-media-surface-economy.md:48` and `:73`, both resolve |
| W8 living-practice | **PASS** | no real tradition inside §11 |
| W9 length | **FAIL** | 47 lines; 2.5× the house max |
| W10 restatement | **FAIL (minor)** | two maps repeat the same field structure; the volume is the over-build |

This reproduces R03's B7/F-1/F-2 (`reports/round-47/review/R03-c-content.md:184-196`; B7 at `:194`). A gate that failed nothing would be green by construction (`worked-example-verification.md:56-62`); this one rejects the filed defect — and now also rejects the assembled successor's derive leg.

---

## 7. Why the assembled example regressed

- `M01-example.md` (the seat assigned to author the example) filed a **tagged** example that passes the gate (§8). C01's assembled entry uses a **different, untagged** example. There is no indication in C01's file that it consumed M01's block; its §5.5 checks only the "one rule" half of B7.
- The entry's decision record was compressed from r47's 12 rows to 6, and the update rule — the one rule both r47 and the r48 example call decisive — was dropped in the compression. The example kept the lesson and lost its row.
- This is exactly the failure mode the round's `claims.json` non-goal names: a right-sized entry that is shorter but not audited on every leg. Length discipline is necessary, not sufficient.

---

## 8. Repair options (integrator's choice)

**Option A (smaller, recommended): repair C01's example in place.**
1. Add `DR-CM-07` (update rule) to `:239-244`, and add an update step to the build order (`:223-231`).
2. Tag the nine moves `step n / DR-CM-0n` and end `:269` with `(DR-CM-01, -05, -07)`.
3. Reconcile the two blank taxonomies (F-3) and state the pace (F-4).
4. Trim 2–4 lines (F-2).

**Option B: adopt M01's tagged example**, renumbered from `DR-CT-01..09` to the entry's `DR-CM-*` scheme, which also requires adding the update row and (optionally) the missing decision rows. M01's block is 27 lines and fails W9; adopt only with its N-1/N-2/N-3 fixes below.

### 8.1 M01's fragment — measured (secondary)

`reports/round-48/cov/M01-example.md:28-54`, 27 lines, block sha256 `b6aaaf47167c2423c2bc6cc26a940d36e229b0f9317542965df9f1baafd8c123`; file sha256 `04edaa45…08aaf1` (124 lines).

| Control | Result | Basis |
|---|---|---|
| W1 label | **PASS** | `:28` heading |
| W2 invented frame | **PASS** | `:30` working labels, none canon |
| W3 one update rule | **PASS** | canonical cell `:44`; Sheet B points left; reversal applies the same supersession event |
| W4 rule names | **PASS** | nine move rows tagged `step n / DR-CT-0n` (`:36-44`) |
| W5 derive leg | **PASS** | five consequences, each with an id (`:50-54`) |
| W6 reject leg | **PASS (strong)** | rockfall: a wall is not a turn class; a gap has length but no frontage |
| W7 citations | **PASS** | `writing-media-surface-economy.md:73` resolves |
| W8 living-practice | **PASS** | no hits |
| W9 length | **FAIL (P2)** | 27 lines vs ≤25 ceiling |
| W10 restatement | **PASS** | concrete values |

M01's P2 findings, if Option B is taken: **N-1** the corvée sheet's class cell already uses "segment" while the joint sheet is said to add "the segment" as a new class — say it promotes the segment from a label to a class with a condition field (`:40`, `:46`); **N-2** a printed zero is called "a different blank" (`:41`, `:52`) — call it a not-applicable exemption, not a blank; **N-3** 27 lines — trim to ≤23. M01's self-audit arithmetic recomputes exactly (27 lines; 11 table lines; 27/47 = 57%; 1:2,500 → 2.5 m; cited line and sha match).

---

## 9. What is verified, what is not

- **Verified on bytes:** the assembled example's text, its control results, the decision-record gap, the build-order gap, the blank-taxonomy mismatch, and the arithmetic that is present (0.2 mm scale conversions; the pace-based error only as an unstated assumption).
- **Not verified:** the final assembled entry after repair (re-run §10); the external shelf (no network); the Ca/README claim (not my seat).
- **Not mine to decide:** which repair option the integrator takes, and whether the entry lands. This receipt records the example's audit status only.

---

## 10. Re-audit recipe (copy-paste)

```bash
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
F=reports/round-48/cov/<assembled-entry>.md
sha256sum "$F"
S=$(grep -nE '^## .*([Mm]icro-example|[Ee]xample)' "$F" | head -1 | cut -d: -f1)
E=$(awk -v s="$S" 'NR>s && /^## /{print NR; exit}' "$F"); [ -z "$E" ] && E=$(($(wc -l < "$F")+1))
echo "block $S-$((E-1)) lines $((E-S))"
sed -n "${S},$((E-1))p" "$F" | grep -c 'DR-'                       # W4/W5: must be > 0
sed -n "${S},$((E-1))p" "$F" | grep -n 'NON-CANON'                 # W1
sed -n "${S},$((E-1))p" "$F" | grep -nE '^\s*[-*]\s*\*?Update|^\| *Update'  # W3
sed -n "${S},$((E-1))p" "$F" | grep -noE 'corpus/[A-Za-z0-9_./-]*\.md:[0-9]*' | sort -u  # W7
sed -n "${S},$((E-1))p" "$F" | grep -niE 'lienzo|songline|polynesian|aboriginal|maori'  # W8
grep -n 'DR-' "$F" | head                                            # the rule ids must exist in the record
```

**PASS requires:** block ≤25 lines (target ≤20); every move tagged with an existing decision row; the consequence line carrying ids; one canonical update statement with a singleton trigger; every citation resolving; no living-tradition template; and every id the example cites actually defined in the entry's decision record.

---

## 11. Scope and writes

- **Writes:** this file only. No scratch artifact remains; the earlier scratch fixture was removed after measurement.
- **No corpus write or staging.** `corpus/knowledge/culture-material/cartography-and-mapmaking.md` remains absent at HEAD (`ls` → No such file). No byte of `reports/round-1..47/**`, `corpus/lessons/*.md`, `tools/gates/frozen/**` or fleet `.ufo/**` was edited.
- **No commit, push, install, or network.** No `reports/round-*/run-validation.py` executed.
- **Handoff:** C01 fixes F-1 (blocking) and F-2..F-4; the integrator either repairs in place (Option A) or adopts M01's tagged block with N-1..N-3 fixes (Option B); C04/C05 and R03 re-run §10 on the assembled entry after the fix. The C claim's "audits clean incl. worked-example legs" threshold is **not met** at this digest.
