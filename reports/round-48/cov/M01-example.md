# M01 — NON-CANON worked micro-example (claim C)

- Seat: **M01** | role: executor | claim: **C** (coverage) | round 48, loop 2, position 2
- Out path: `reports/round-48/cov/M01-example.md` (this file). I wrote no other file, edited no fragment, and staged nothing under `corpus/`.
- Baseline: `git rev-parse HEAD` → `a01405dd36367292255c2652ac0a601f4cd6a0af` (= `reports/round-48/claims.json` `baseline_commit`); `git status --porcelain` → only `?? reports/round-46/review/` and `?? reports/round-48/` at seat open.
- Mission (verbatim, `reports/round-48/targets.json` seat `M01`): *"Micro-example author: write the NON-CANON worked cartography micro-example (a fictional culture's map register) — one consistent rule, declared invented, demonstrates the survey-to-symbol method."*

## 1. What the example has to clear, and where that came from

I read the r47 evidence before drafting, not after:

- `reports/round-47/review/R03-c-content.md:194` (B7): the r47 example stated its update rule **three incompatible ways** (`reports/round-47/cov/C03-entry-c.md:123`, `:137`, `:150`). This draft states it once, in one table cell, and the second sheet explicitly declines to restate it.
- `reports/round-47/cov/C14-example.md:123-140` (F-2): the r47 example named **zero** `DR-CT-` rows (`sed -n '107,153p' … | grep -c 'DR-CT-'` → 0, `C14-example.md:125`) and its six consequences carried no rule map. This draft tags every move with its build-order step **and** its decision row, and ends with a consequence→row list.
- `reports/round-47/cov/C14-example.md:92-120` (F-1): the deeper failure was not the wording but a staged dispute that required knowing which of two triggers the office followed. This draft stages a dispute that is **outside both class sets**, so no rule has to be violated for the scene to work — the update rule is not the source of the conflict, it is the reason the sheets stayed lawfully usable.
- `reports/round-47/review/R03-c-content.md:92` (§2.3): the r47 example occupied 47 lines (`reports/round-47/cov/C14-example.md:5`, `:107-153` inclusive) inside a 739-line entry. This one is a **9-row table plus one paragraph plus a five-item map**, **27** lines with blanks — compact enough for a ≤250-line entry.
- `corpus/QUALITY.md:16-17`: usability means decision tables, typology tables, checklists, worked examples; no essays. The example is a table and a decision, not a vignette.

## 2. Assumptions for integration (stated, not hidden)

1. **Section numeral `7`** in the heading is my assumption about the right-sized skeleton (property → chain → classes → trade → provenance → build order → example → calibration → recheck → scope). If the assembled entry numbers it differently, change the numeral only; nothing inside the section depends on it.
2. **Decision-row ids `DR-CT-01..09`** follow the semantics defined at `reports/round-47/cov/C03-entry-c.md:195-203` (01 question/reader … 09 update rule). `targets.json` seat C01 tells the drafter to cover the same chain; if r48's decision record renumbers, substitute mechanically and **keep the row semantics** — the tags in the table are the derive leg and must not be dropped.
3. **Build-order step numbers 1–9** refer to the entry's survey-to-symbol sequence (select → measure → control → reduce → project → symbolize → reproduce → warrant → update). The table names each step's content, so a renumbered build order can be matched by name.
4. The only in-repo citation inside the example is `writing-media-surface-economy.md:73`, verified live below. Everything else is invented design content and is labelled as such.

## 3. The section, integration-ready (fenced)

```markdown
## 7. Worked micro-example (NON-CANON) — one valley, two sheets

A demonstration of the procedure, not a world decision. Working labels only: "the Tamber terraces", "the weir house", "the corvée office". Every element below is a design option, and none of it is canon. Each move is tagged to its build-order step and to the decision row it exercises.

**The ground.** Seven terraces on one stream, a weir at the head, and a common wall along the west face that every terrace shares; the top (seventh) terrace is held by a shrine and is exempt from both the water turn and the corvée by charter.

| Move (build step / decision row) | Sheet A — the turn sheet | Sheet B — the corvée sheet |
|---|---|---|
| Question and reader — step 1 / DR-CT-01 | which sluice opens, in what order, for how long; read by the water bailiff at the weir | which terrace owes how many days of wall repair; read by the corvée clerk and the ward elders |
| Chain and error budget — step 2 / DR-CT-02 | turns allocated to named holders; measure the weir notch and a marked staff; control against the bronze bar kept in the weir house; error budget = silt and a shifted notch, so the sheet promises order and duration, not volume | liable frontage measured in staff-lengths along each wall face against the same bronze bar; error budget = slumped footings, so liability is stated in whole and half staff-lengths |
| Projection, scale and distortion — step 3 / DR-CT-03 | no plan: a strip in channel order, distance in paces, no scale bar; the cartouche reads "order and duration are true at the notch; distance is a walk" | a local plane at 1:2,500 — one millimetre on the sheet is 2.5 m on the ground; the cartouche reads "frontage lengths are true; terrace areas are not shown" |
| Orientation and zero — step 4 / DR-CT-04 | upstream at the top; zero at the weir notch | upstream at the top; zero at the weir notch — the same frame, and the sheets remain incomparable |
| Classes and legend — step 5 / DR-CT-05 | numbered turn holder, channel (line), sluice (point), shrine terrace (exempt glyph); a wall is not a class | liable terrace (days), exempt terrace (named, zero days), common wall (line) whose every segment is labelled with the two terraces it separates; a turn is not a class |
| Silence register — step 6 / DR-CT-06 | the shrine terrace carries no turn number: **withheld** (charter exemption), not unknown | the shrine terrace is drawn and named with **zero** days: a stated exemption; the same fact is a different blank because the reader differs |
| Reproduction and access — step 7 / DR-CT-07 | master painted on a board, sealed and kept at the weir house; working copies on the cheap office surface (cost rung 3, `corpus/knowledge/culture-material/writing-media-surface-economy.md:73`), valid only with the bailiff's countermark; read aloud at the opening, so no holder need read | master a paper register in the office; copies read at the ward meeting and posted; the elders' assent marks are the copy control |
| Warrant — step 8 / DR-CT-08 | the water court's seal, the bailiff's oath, the season's opening date; admissible in the water court and nowhere else | the clerk's signature, the elders' marks, the season; admissible in the ward court, not the water court |
| Update rule — step 9 / DR-CT-09 | **stated once, here, and it governs both sheets:** a sheet is current for the season stamped on it and is superseded by the joint walk at the opening; the superseded sheet is kept, stamped "old", for arrears | the same rule; not restated — see the cell to the left |

**The rockfall (the reversal).** A rockfall takes out three staff-lengths of the common wall between terraces 4 and 5. The turn sheet does not change: a wall is not one of its classes, and the turn order still runs. The corvée sheet charges 4 and 5 for a segment that is now a gap. The ward court asks which sheet is right, and the answer is neither: "who rebuilds the gap" was not the question either sheet was built to answer. The rockfall is chalked on the board the day it happens; the next joint walk does the rest. The joint sheet they commission adds one new class — the **segment**, a wall run between two terraces with a condition field (standing / breached / rebuilt) — and keeps the same warrant rule, both offices sealing. The correction is a new class, not a corrected number: the corvée sheet's class is frontage, and a gap has length but no frontage; the turn sheet's class is the turn, and a gap has no turn.

**What the example demonstrates** (each claim mapped to the row it exercises):

- (a) **Form follows question** (DR-CT-01): one valley, two forms, and neither is wrong.
- (b) **A shared frame does not make sheets comparable** (DR-CT-03, -04, -05): the same zero, the same orientation, and still no common class.
- (c) **A blank is a decision about the reader, not the land** (DR-CT-06): withheld on A, a printed zero on B.
- (d) **Warrant decides admissibility before content** (DR-CT-08): each sheet is evidence in one court only.
- (e) **The update rule is the institution** (DR-CT-09): both sheets stay lawfully current through an event no class set can represent, which is why the event goes to court — and why the repair is a new class, not a re-survey.
```

## 4. Self-audit before filing (commands run at seat time)

### 4.1 Length

```
$ awk '/^```markdown$/{f=1;next} /^```$/{f=0} f' reports/round-48/cov/M01-example.md | wc -l
27
$ awk '/^```markdown$/{f=1;next} /^```$/{f=0} f' reports/round-48/cov/M01-example.md | grep -c '^|'
11        # 2 header lines + 9 move rows
```

27 lines including blanks; 11 table lines. r47's §11 occupied `:107-153` of `reports/round-47/cov/C03-entry-c.md` = **47** lines inclusive (`153 − 107 + 1`), so this is **27/47 ≈ 57% of the length**, i.e. ~43% shorter (`(47 − 27) / 47 ≈ 0.426`), while keeping all nine moves.

### 4.2 One rule, stated once

```
$ awk '/^```markdown$/{f=1;next} /^```$/{f=0} f' reports/round-48/cov/M01-example.md | grep -n 'update\|superseded\|joint walk'
17:| Update rule — step 9 / DR-CT-09 | **stated once, here, and it governs both sheets:** a sheet is current for the season stamped on it and is superseded by the joint walk at the opening; the superseded sheet is kept, stamped "old", for arrears | the same rule; not restated — see the cell to the left |
19:**The rockfall (the reversal).** … The rockfall is chalked on the board the day it happens; the next joint walk does the rest. …
27:- (e) **The update rule is the institution** (DR-CT-09): both sheets stay lawfully current through an event no class set can represent, which is why the event goes to court — and why the repair is a new class, not a re-survey.
$ awk '/^```markdown$/{f=1;next} /^```$/{f=0} f' reports/round-48/cov/M01-example.md | grep -c 'after any storm\|per levy year\|not due until'
0
```

Three matching lines, but only **line 17** states a trigger: line 19 is an application sentence that introduces **no second trigger** ("chalked … the day it happens" is a recording act; "the next joint walk does the rest" names the same supersession event), and line 27 names the row without restating it. The B7 defect strings (`after any storm`, `per levy year`, `not due until`) return **0** — the exact class of r47's contradiction is absent by construction.

### 4.3 Arithmetic

Only one numeric conversion exists, and it is exact:

- `1:2,500` → `1 mm × 2,500 = 2,500 mm = 2.5 m`. The text says "one millimetre on the sheet is 2.5 m on the ground" — correct. (`python3 -c 'print(1*2500/1000)'` → `2.5`.)
- "Seven terraces", "the top (seventh)", "terraces 4 and 5", "three staff-lengths": these are design counts, not derived quantities, and are used consistently (4 and 5 are interior terraces, not the shrine's 7th).

### 4.4 Citations

```
$ sed -n '73p' corpus/knowledge/culture-material/writing-media-surface-economy.md
| 3 | papyrus (coarse), paper (early), cloth | the office and the merchant | the account, the contract, the register, the ledger |
$ sha256sum corpus/knowledge/culture-material/writing-media-surface-economy.md
f039e6e120ed050ff16adebc0ad5cd9cff7965337799fe7cbc725ba0823d4601  corpus/knowledge/culture-material/writing-media-surface-economy.md
```

The cited line is cost-ladder rung 3, whose owner column is "the office and the merchant" — exactly the use made of it (cheap working copies for an office). No other in-repo path appears inside the fenced block:

```
$ awk '/^```markdown$/{f=1;next} /^```$/{f=0} f' reports/round-48/cov/M01-example.md | grep -o 'corpus/[A-Za-z0-9_./-]*\.md:[0-9]*' | sort -u
corpus/knowledge/culture-material/writing-media-surface-economy.md:73
```

### 4.5 Label and canon hygiene

The heading carries `(NON-CANON)`; the first sentence says "not a world decision" and "none of it is canon"; every proper noun is a working label; no real-world tradition is used as a template, so no boundary-protocol citation is owed. The example decides nothing about any world.

### 4.6 Method coverage (the mission's real test)

| Mission element | Where it is demonstrated |
|---|---|
| survey-to-symbol chain | every step 1–9 is a table row; steps 1–3 and 7 carry the chain itself (question → measure/control → reduce/project/symbolize → reproduce) |
| one consistent rule | the single `DR-CT-09` cell; sheet B refuses to restate it |
| declared invented | heading + opening sentence |
| demonstrates the method, not describes maps | the rockfall forces a **new class**, which is the entry's method claim (a class boundary is a claim, DR-CT-05) rather than a drawing lesson |

## 5. What I did not do

- No write outside this path; no `corpus/` staging; no edits to `reports/round-1..47/**`.
- No `run-validation.py` execution, no re-freeze, no packet-surface change, no network, no git command beyond read-only `rev-parse`/`status`.
- The external shelf and any real-world cartographic case are out of scope for this seat; the example invents all content and needs no `(to-verify)` marks. If the integrator inserts a real-world analogy into this section, it must carry its own marker.
- **Open for the integrator:** confirm the section numeral and the `DR-CT-0N` numbering against the assembled entry (§2.1–2.2). That is mechanical renumbering; the row semantics and the tags must survive it.
