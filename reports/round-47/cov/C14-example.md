# C14 — worked-example review (claim C): "one lagoon, two maps"

- Seat **C14** | role **verifier** | claim **C** (coverage) | round 47, loop 2, position 1.
- Out path: `reports/round-47/cov/C14-example.md` (this file). This seat writes no other file and edits no other seat's bytes.
- Under review: the worked example in `reports/round-47/cov/C03-entry-c.md` §11, lines `107-153` (whole-file sha256 `4b699e0653711527…`; §11 block sha256 `f01dc14ede931163…` at audit close, 2026-10-19).
- Baseline checked at audit time: HEAD `6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe`; `find corpus/knowledge -name '*.md' | wc -l` → **223**; `ls corpus/knowledge/culture-material/*.md | wc -l` → **25**; `ls corpus/knowledge/culture-material/cartography-and-mapmaking.md` → **No such file or directory**.
- Mission (verbatim, `reports/round-47/targets.json` seat `C14`): *"Worked-example reviewer: the draft's worked micro-example is declared invented/non-canon, internally consistent, and demonstrates the register's method."*

## Verdict in one line

**FAIL as filed, on two repair items — one blocking internal-consistency defect (F-1) and one required derive-leg defect (F-2); the non-canon label (PASS) and the method demonstration (PASS, strong) are not the problem.**

The example is a real demonstration, not filler: it runs the nine-step build order twice on one invented lagoon, yields two incompatible but question-correct sheets, and uses a storm to show that warrant and update rule decide the dispute. It cannot be certified as checked while its update rule says three different things and no decision-row id appears anywhere in the section.

---

## 1. Receipt (per `corpus/knowledge/verification/worked-example-verification.md:44`)

| Receipt field | Value |
|---|---|
| Entry and digest at check time | `reports/round-47/cov/C03-entry-c.md`, whole file sha256 `4b699e06537115274807b64fbc5947cefc889348e5b4434b14a8ddb661eee3e5` (41,114 bytes, mtime 2026-10-19 15:02:59 −0300); §11 block (`:107-153`) sha256 `f01dc14ede931163697dffebf5a10d10caea137f888183fd6b0eea01e2be8add` |
| Class | **(c) invented sectioned example** — a full section with two staged sub-examples and a comparison table, not the one-paragraph class (b) micro-example. The heading's word "micro-example" is a label collision; the stricter class (c) obligations were applied |
| Rules named in the example | **None.** Zero `DR-CT-` tokens in §11 (`sed -n '107,153p' … \| grep -c 'DR-CT-'` → **0**). The rule payloads exist at `C03-entry-c.md:195-203` (DR-CT-01..09) and the procedure at `:79-87` (build-order steps 1–9) |
| Consequence↔rule map | §4 below: six stated consequences, all map to existing DR-CT rows, none cited in §11 |
| Controls run | The storm is the class (c) reversal: Map A used for navigation (its class set has no channel) and Map B used for tax (its class set has no land ownership) both fail; the joint survey supplies the corrected question, warrant and update rule (`C03-entry-c.md:137`). No synthetic gate fixture is claimed |
| Label check (verbatim) | `## 11. Worked micro-example (NON-CANON) — one lagoon, two maps` (`:107`); "A demonstration, not a world decision. Working labels only … none of it is canon." (`:109`); "The worked example is **NON-CANON** and disposable" (`:228`) |
| Freshness basis | By construction: the Salt City, the salt office and the pilots' guild are invented here and appear in no other section of the assembled entry |
| Auditor and date | C14, 2026-10-19 |
| Re-audit trigger | Any edit to §11, to the §10 build-order steps, or to the DR-CT rows; re-run §7 |

The receipt is a debt record, not a clearance (`worked-example-verification.md:44`, DR-WE-09). It records what was checked; it certifies no world and no promotion.

---

## 2. What was measured (commands and outputs)

```text
$ git rev-parse HEAD
6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe
$ find corpus/knowledge -name '*.md' | wc -l
223
$ ls corpus/knowledge/culture-material/*.md | wc -l
25
$ ls corpus/knowledge/culture-material/cartography-and-mapmaking.md
ls: cannot access 'corpus/knowledge/culture-material/cartography-and-mapmaking.md': No such file or directory

$ grep -n '^## 11\.\|^## 12\.' reports/round-47/cov/C03-entry-c.md
107:## 11. Worked micro-example (NON-CANON) — one lagoon, two maps
154:## 12. Calibration bank — what not to ship as history

$ sed -n '107,153p' reports/round-47/cov/C03-entry-c.md | grep -c 'DR-CT-'
0

$ sed -n '107,153p' reports/round-47/cov/C03-entry-c.md | grep -o 'corpus/[A-Za-z0-9_./-]*\.md:[0-9]*' | sort -u
corpus/knowledge/culture-material/writing-media-surface-economy.md:48
corpus/knowledge/culture-material/writing-media-surface-economy.md:73
# both files exist and both cited lines are within range; contents checked below
```

The two in-example citations resolve and say what the example uses them for:

- `writing-media-surface-economy.md:48` — the palm-leaf/bark/cloth row, whose cost driver is "a *low-capital, high-labour* family"; the example uses cloth for the pilot chart's copies (`C03-entry-c.md:133`).
- `writing-media-surface-economy.md:73` — cost-ladder rung 3, "papyrus (coarse), paper (early), cloth — the office and the merchant"; the example uses paper copies for the tax collectors (`C03-entry-c.md:121`).

No other path is cited inside §11. The example's other materials (vellum, rope, bronze bar, lead line, compass) are design choices, not sourced factual claims.

### Class check

`worked-example-verification.md:26` defines class (c) as "a full section of staged steps"; this section has two nine-bullet stages plus a summary table (`:139-150`) and a consequence list (`:152`). Its per-class obligations are `worked-example-verification.md:52`: every exercised rule named at its step; step outputs chain with no silent leaps; at least one step reversed or one forbidden input shown; NON-CANON in the section heading or opening line. The last two pass; the first fails (F-2).

---

## 3. Mission criteria

| Mission criterion | Verdict | Evidence |
|---|---|---|
| **Declared invented / non-canon** | **PASS** | `C03-entry-c.md:107` carries `NON-CANON` in the heading; `:109` says "A demonstration, not a world decision … none of it is canon"; `:228` repeats "NON-CANON and disposable". Working labels are framed as working labels; no real-world tradition is used as a template; no canon-voiced "the culture does X" outside the invented frame |
| **Internally consistent** | **FAIL** | F-1 is blocking: the update rule is stated three incompatible ways (`:123`, `:137`, `:150`). Four further ambiguities are filed as M-1..M-5; two are material to the example's punchline (M-2, M-4) |
| **Demonstrates the register's method** | **PASS (strong)** | The example runs all nine build-order steps for two different questions/forms and shows the register's master claim in action: same water, two accurate-for-their-question sheets, incompatible because they classify different entities; authority decided by warrant and dates, politics by the blank. It exercises the form table's "minimum credible build" (`C03-entry-c.md:97-103`) rather than merely naming it |

### Four-leg verdict (`worked-example-verification.md:37-42`)

| Leg | Verdict | Basis |
|---|---|---|
| **Instantiate** | **PASS** | The nine bullets realize the payloads of DR-CT-01..09: question/reader (`:115`, `:127`), chain and error budget (`:116`, `:128`), projection/scale and distortion statement (`:117`, `:129`), orientation/zero (`:118`, `:130`), class definitions (`:119`, `:131`), blank policy (`:120`, `:132`), reproduction/copy control (`:121`, `:133`), warrant (`:122`, `:134`), update rule (`:123`, `:135`). The form table's "cannot do without" cells are satisfied for both forms: cadastral chain/baseline/parcel/warrant/archive; portolan bearings/soundings/hazard marks/copy control (`:97-103`) |
| **Derive** | **FAIL** | No rule id is named inside §11 (grep → 0), and the six consequence claims at `:152` carry no consequence↔rule map. F-2 |
| **Reject** | **PASS** | The storm is the class (c) reversal: the levy sheet cannot answer "which channel" (channel is deliberately not a class, `:119`), and the pilot chart cannot answer "what levy" (land ownership is deliberately not a class, `:131`); the barge grounding and the half-water assessment are the shown failures, and the joint survey's new question/warrant/update rule is the correction (`:137`). This is a control the example's own class definitions make inevitable, not a control that cannot fail |
| **Label** | **PASS** | Verbatim NON-CANON in the heading and the opening sentence (`:107`, `:109`); no canon drift in the section |

---

## 4. F-1 (blocking, internal consistency): the update rule is stated three ways

The example's own lesson (f) is "The update rule is the real institution; a map without one is a dated opinion" (`C03-entry-c.md:152`). Its update statements do not agree:

| Line | Text | What it implies |
|---|---|---|
| `:123` | "re-survey after any storm that breaches a dike" | **breach-triggered**: the storm in `:137` is exactly this trigger, so a re-survey is due now |
| `:137` | "its survey predates the storm, and the re-survey is not due until the levy year turns" | **levy-year-triggered**: the breach does not trigger a survey; the sheet is lawfully stale until the year turns |
| `:137` | the joint survey needs "a new update rule (re-survey after every breach, not every levy year)" | the **old rule was levy-year**, and the new rule is the breach trigger — the opposite of `:123` |
| `:150` | table cell: "after a dike breach, per levy year" | **conflates both**: it names the breach and the levy year in one cell without saying which is the trigger |

Why this blocks: the scene's causality (the levy sheet still shows the old pan; the pilot chart shows the new cut; the office taxes half water) depends on the levy sheet *not* having been re-surveyed. If `:123` is the rule, the office is violating its own rule, and the example should say so; if `:137` is the rule, `:123` is wrong, and the joint survey's "new rule" is genuinely new. As filed, the reader cannot tell whether the defect is the rule or the office, and consequence (f) does not follow from the stated premise.

**Proposed repair (option A — make the old rule the levy year; recommended, because it matches `:137` and makes the joint rule a real change):**

```diff
- - *Update:* re-survey after any storm that breaches a dike; superseded masters are stamped and kept for arrears.
+ - *Update:* re-survey at the levy year; a breach is recorded and assessed at the next levy unless the office orders an ad hoc survey; superseded masters are stamped and kept for arrears.
```

```diff
- | update | after a dike breach, per levy year | after a storm, by sounding boat |
+ | update | per levy year; a breach is recorded for the next levy | after a storm, by sounding boat |
```

With those two edits, `:137` reads consistently ("not due until the levy year turns"; joint rule "after every breach, not every levy year"), and the storm's lesson becomes true: the levy-year rule is the institution that fails, and the joint survey replaces it.

**Alternative (option B — keep `:123` breach-triggered and make the story about non-compliance):** change `:137` to say the office has *failed* to apply its own breach rule and is taxing on a sheet its own rule has condemned; change "a new update rule" to "an enforced update rule." This requires more edits and turns the example from a rule-design lesson into an office-failure lesson. Option A is the smaller, more coherent fix.

---

## 5. F-2 (required, derive leg): no rule ids and no consequence↔rule map

`sed -n '107,153p' … | grep -c 'DR-CT-'` → **0**. The bullets name the §10 *step titles*, not the decision rows. The six claims at `:152` each trace to a row; the mapping is unambiguous, which makes the repair additive rather than a redraft:

| Claim at `:152` | Nearest rule id (defined at `:195-203`) | Status in §11 |
|---|---|---|
| (a) "Form follows question" | DR-CT-01 | uncited |
| (b) "Two accurate maps can contradict each other … because they classify different entities" | DR-CT-05 with DR-CT-01 | uncited |
| (c) "The blank is a decision with a politics" | DR-CT-06 | uncited |
| (d) "The warrant, not the drawing, is what makes a sheet authoritative" | DR-CT-08 | uncited |
| (e) "Reproduction controls who can argue with the map" | DR-CT-07 (access also DR-CT-10) | uncited |
| (f) "The update rule is the real institution" | DR-CT-09 | uncited |

**Proposed repair (additive; two changes):**

1. Tag each of the nine bullet labels in both maps with its step and row, e.g. `- *Chain (§10 step 2 / DR-CT-02):*` … through `- *Update (§10 step 9 / DR-CT-09):*`. The labels already match the step titles, so no prose changes are needed.
2. Append a rule-map sentence after `:152`:

```text
**Rule map.** The nine bullets above are §10 steps 1–9, and each step's payload is the
matching row: DR-CT-01 question/reader; -02 chain and error budget; -03 projection/scale;
-04 orientation and zero; -05 class and legend; -06 silence register; -07 medium and copy
control; -08 warrant; -09 update rule. The storm is the reversal the rows predict: Map A is
used outside its question (channel is not a class) and Map B is used to tax (land ownership
is not a class); the joint survey answers by changing the question, the warrant and the
update rule.
```

That satisfies class (c)'s "each step names the rule" and the gate's consequence↔rule map requirement (`worked-example-verification.md:40`, `:52`).

---

## 6. Minor findings (fix if cheap; list if not)

### M-1 — one channel in the setup, several in the use

`:111` says "**one** deep channel runs from the open sea to the market quay"; `:127` asks "**which** channel, at what state of tide"; `:132` withholds "the temple's private channel." A single deep channel makes the pilot's choice trivial and leaves the private channel unmentioned in the setup. Fix: "one deep channel runs from the open sea to the market quay among several shallow cuts." This prefigures the choice without naming the temple's cut.

### M-2 — "two accurate maps" vs. a knowingly stale levy sheet

`:152` (b) says "Two **accurate** maps can contradict each other without either being false," but `:137` says the levy sheet's survey predates the storm and it still shows a pan that is now half water. The intended claim is accuracy-for-question-at-survey-date. Fix: "Two maps, each accurate for its question at its own survey date, can contradict each other without either being false, because they classify different entities."

### M-3 — the pilot-copy warrant is under-mechanized

`:133` says each pilot hand-copies the master and signs the copy; `:134` says "A pilot's copy is valid only with the mark." It is not stated who applies the mark to a hand copy or how a copied mark is distinguished from a forgery. Fix: "A pilot's copy is valid only when the guild master's mark is countersigned at the annual reading" (or state that the master marks each checked copy). This closes the copy-control loop that DR-CT-07 claims.

### M-4 — storm chronology: chart shows the new cut, pilot accused of navigating outside the chart

`:137`: "The pilot chart shows the new channel … the pilot is accused of navigating outside the chart." If the chart shows the cut, the accusation needs a stated reason — the cut is unsurveyed (a line, no soundings) or the pilot's copy predates the correction. Also, "a channel that did not exist when either sheet was sealed" sits awkwardly with `:135`, where the guild's master is corrected after the storm. Fix: "The pilot chart shows the new cut as a line without soundings; the pilot's copy predates the correction" and "when either master edition was sealed." This makes the dispute's dates-and-warrants resolution exact.

### M-5 — cross-fragment blank taxonomy (integration finding)

C01's frame gives blanks three readings as "unknown, empty, or forbidden" (`reports/round-47/cov/C01-entry-a.md:164`), while §10 step 6 and DR-CT-06 give "unknown / withheld / not-applicable" (`C03-entry-c.md:84`, `:200`). The assembled entry would carry two triads for one decision, and both example blanks are "withheld" (`:120`, `:132`), so the silence register is demonstrated in only one of its three classes. Recommend the integrator adopt one triad (C03's is the operational one), make C01's line point to §10 step 6 instead of restating a different triad, and optionally make one blank "unknown" (e.g. the unsurveyed outer shoals) to exercise a second class. This is not a defect of §11 alone; it is an assembly reconciliation item.

### Class-label note (not a defect)

The heading calls the section a "worked micro-example," but its shape is class (c). The integrator should record the audit class so a later reader does not apply class (b)'s lighter obligations (control may live in the receipt) to a section that supplies its own reversal.

---

## 7. What is genuinely good (so the repairs are not mistaken for a redraft)

- **It is a demonstration, not decoration.** The two maps differ in question, reader, chain, projection, orientation, classes, blank, medium, warrant and update rule; the comparison table (`:139-150`) makes the difference inspectable. This is the entry's master claim performed, not asserted.
- **The storm is a real reversal.** It is entailed by the two class definitions, not imposed: a channel is not a taxable class on Map A (`:119`), and land ownership is not a navigational class on Map B (`:131`). The failure is therefore a consequence of the method, which is exactly what a class (c) example owes.
- **The invented frame is honest.** Working labels only (`:109`), no real tradition's content, no canon claim; the two in-repo medium citations resolve and support the choices (`writing-media-surface-economy.md:48,:73`). No restricted or living-practice material is used in the example.
- **It couples to the assembled entry.** The cadastral/portolan requirements match C01's form table (`C01-entry-a.md:242-245`); the copy-drift and warrant-chain concerns match C02 (`C02-entry-b.md:143-154`, `:303-313`); C02's "a map is a perishable claim; the re-survey is a political event" (`:199`) is the example's premise. C04's topic line already declares "a NON-CANON worked example" (`C04-entry-header.md:114`). Peer line cites were re-resolved against their 15:06–15:08 revisions; if those fragments move again, resolve by section name (§5.7, §8.1).

---

## 8. Re-audit recipe (for C03's owner or the integrator)

Run from the lane root with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`:

```bash
sha256sum reports/round-47/cov/C03-entry-c.md
grep -n '^## 11\.\|^## 12\.' reports/round-47/cov/C03-entry-c.md
sed -n '107,153p' reports/round-47/cov/C03-entry-c.md | grep -c 'DR-CT-'
grep -n 'levy year\|dike breach\|re-survey' reports/round-47/cov/C03-entry-c.md
sed -n '107,153p' reports/round-47/cov/C03-entry-c.md | grep -o 'corpus/[A-Za-z0-9_./-]*\.md:[0-9]*' | sort -u
```

**The verdict flips to PASS when:**

1. F-1: every update statement is consistent. Under option A: `:123` says "at the levy year / at the next levy"; `:137` keeps "not due until the levy year turns"; `:150` says "per levy year"; the joint rule remains "after every breach, not every levy year."
2. F-2: `grep -c 'DR-CT-'` on §11 is **> 0**, and each of the nine bullets names its step + row; the consequence list (a)-(f) carries the rule map.
3. M-2 and M-4 are repaired (or explicitly accepted as deliberate ambiguity); M-1, M-3 and M-5 are repaired or listed as integration items.

If the §11 hash changes, re-run this receipt; if only other sections change, this receipt still governs §11 at the recorded digest.

---

## 9. Scope, writes, and handoff

- **Writes:** this file only. No `corpus/**`, `tools/**`, `README`, `LOG.md`, `reports/round-1..46/**`, `tools/gates/frozen/**`, or fleet `.ufo/**` byte was edited or staged. No commit, push, install, or network. No `reports/round-*/run-validation.py` was executed.
- **No corpus landing:** the target path remains absent at HEAD `6e9a30d` (`ls` → No such file); this seat neither stages nor proposes a corpus write. The patches in §4–§6 are proposed bytes for C03's owner or the integrator, not edits made here.
- **Handoff to C03 / integrator:** two repairs are required before the worked-example audit can pass — F-1 (blocking consistency, §4) and F-2 (derive leg, §5). The minor findings M-1..M-4 are cheap local edits; M-5 is an assembly reconciliation between C01 `:164` and C03 `:84,:200`.
- **What this receipt does not decide:** whether the entry lands, whether the C claim is admitted, and whether any world's map is canon. It records the worked example's audit status only; canon and promotion are lore-shokunin's and the integrator's.
- **Owed:** none for this seat. The re-audit is owed only if §11 changes.
