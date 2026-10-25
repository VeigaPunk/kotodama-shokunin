# CritTrendFinal — round-73 wave 2 (FALSIFY): the three trend verdicts, attacked pre-filing

Seat: leaf, no delegation, no background jobs. Lane repo `/home/vgpnk/Projects/shokunin/kotodama-shokunin`,
landed revision `0316b8883b4f8d44b8efd720140e7f52f734a102`, base `8841ad3b896a0227674fa0725b818c999118046f`,
frozen claims `reports/round-73/claims.json` (freeze commit `af65165`). No lane write except this file; the
one byte-changing experiment ran in `/tmp/CritTrendFinal/` (no clone needed — a two-line fixture and two regexes).
No tool installed, no fetch made, no counter run by this seat.

Verdicts are **not yet filed**: `SCORECARD.md` carries no `## Axes — round 73` row (only `## Corrections — round 73`
at :1411) and `/home/vgpnk/Projects/shokunin/.ufo/reports/round-73/` holds only `audio.md` and `game-dev-3d.md`
(`ls`). This attack lands where it was aimed: before the bytes exist.

---

## 1. Proposed verdicts

### expansion — **improved** (with a counting caveat)

| | |
|---|---|
| what the landed evidence supports | Ground the coverage map did not hold was entered, and the entries cite rows mined this round. At base: `git ls-tree -r 8841ad3 --name-only corpus/knowledge \| grep -i conlang` → `corpus/knowledge/linguistics/conlang-methodology.md`, `corpus/knowledge/synthesis/conlang-blueprint-template.md` (2, neither `*conlang-scholarship*`); `git show 8841ad3:corpus/SOURCES.md \| grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'` → `799`; the five ground fragments → `0` each (`ojs.unito.it`, `philol.msu.ru`, `journals.rudn.ru`, `cyberleninka.ru/article/n/klassifikatsii`, `sanders.phonologist.org`). At lands: `find corpus/knowledge -iname '*conlang*'` → 4 files, the two new ones `conlang-scholarship.md` and `conlang-scholarship.amend-2026-10-23.md`; registry `804` rows. Both entries carry the nine-field header and cite only ids ≥ S876; the five rows carry `mined` / `2026-10-25` / `180d` and `used-by` exactly the citing entry (S876–S877 → base, S878–S880 → amendment); coverage-map rows exist at `corpus/README.md:770-771`; the counts the append block states hold (`247` files, linguistics `32`, dirs `32/38/29/29/24/95`). |
| evidence pointers | `corpus/knowledge/linguistics/conlang-scholarship.md:1-13`, `…amend-2026-10-23.md:1-14`, `corpus/SOURCES.md:831-835`, `corpus/README.md:766-775`, `reports/round-73/evidence/S876.txt`..`S880.txt`, `corpus/lessons/round-73.md:14-30` |
| counting caveat | **Does an amendment co-admitted with its base count twice?** As filed: two files, two README rows, two headers — so two admitted *files*. But the amendment's own `ground:` cell defines its ground **against the base** ("the base entry `linguistics/conlang-scholarship.md` rests on two source rows"), so the pair enters **one** ground with two files. The lane's convention is already split: round 72 filed `two admitted entries on verified uncovered ground` for expansion and `the amendment co-admitted with its base is one admission event, not a deepening` for quality (`.ufo/reports/round-72/kotodama.md:36-37`). Proposed wording: *two admitted files on one newly entered ground, five mined rows* — not *two entries on uncovered ground*. The verdict does not change: one net-new entry on uncovered ground already fires the observable. |
| what would downgrade it | **harmed**, if the closure judges the amendment to fail the bar it was admitted under — the one live path is criterion 4 ("Usability … No essays"): the amendment has **0 table rows** (`grep -c '^|' corpus/knowledge/linguistics/conlang-scholarship.amend-2026-10-23.md` → `0`, against `26` in `conlang-scholarship.md`) and its only act-on-able form is four unnumbered directives in §4. Also downgraded to `unchanged` if the closure holds the pair to be one entry *and* requires ≥2 net-new entries (nothing in LEARNING.md says that). Not downgraded by the recheck-pointer defect F1 below: that is a header-content defect, not an entry-bar failure. |

### quality — **unchanged**

| | |
|---|---|
| what the landed evidence supports | No existing entry was re-verified, deepened or superseded: `git diff --name-status 8841ad3..0316b88 -- corpus/knowledge` → `A` ×2, **no `M`**, so no `verified-at:` in the corpus moved and no entry byte was touched. The round's one proposed deepening of an *existing* entry — `conlang-methodology.amend-2026-10-24.md` — was **refused** (`corpus/lessons/round-73.md:43`). Every other repair in the round is a record repair under criterion 20: README counts (`L01–L03`), SHONEN pointers (`L04/L05`), SCORECARD verdict text (`L06`), LOG range token (`L07`), SKILL registry (`L08`). No entry was found false and left unmarked: the three campaign-id citations that exist in the corpus resolve to the lane rows' actual documents — `S728` in `linguistics/language-socialization-and-acquisition.md:40` is the Frye/Qaqet line, `S769` in `culture-material/games-play-sport-contests.md:63` is the Opie children's-lore line, `S806` in `culture-material/medicine-healing-codes.md:11` is the Ayurveda line (`grep -rno` on those three files). The staging-side `S728`/`S769`/`S806` collisions are a shokuknow defect, not a lane-entry falsehood. |
| evidence pointers | `git diff --name-status 8841ad3..0316b88 -- corpus/knowledge`; `corpus/lessons/round-73.md:43` (refused deepening), `:108-113` (M1/M2 record classes); `SCORECARD.md:1411-1423` |
| what would downgrade it | **harmed** only if an entry is shown false/stale and unmarked, or if the amendment is counted as deepening an existing entry (it cannot be: its base did not exist at base). No such case found. |

### discernment — **unchanged** (strict; this is the verdict I would defend)

| | |
|---|---|
| what the landed evidence supports | Neither branch of the observable fires yet. **Branch 1 (outside spot-check):** no non-author spot-check of any round-73 gate decision exists — the lesson's `## Gate` carries no spot-check row (`grep -n -i 'spot-check' corpus/lessons/round-73.md` → only `:108` and `:109`, both citing the *round-72* spot-check). **Branch 2 (disagreement → lesson → grounded criterion):** criteria 22 and 23 are new and their citations do resolve — 22 → `R73-M3` (`corpus/lessons/round-73.md:110`), 23 → `R73-M4` (`:111`) and `R73-M5` (`:112`); `M6`'s content appears in 23 without its id (`:113`). But they are lane-authored from **lane-internal** measurements (a wave-1 premise re-measured, a round-72 counter's red selftest, the lane's own counter bug) — not from a checked disagreement about an admit/reject. The lane's own filing precedent settles this: **round 71 added criterion 20, grounded in the round-70 outside spot-check V70-4, and still filed `discernment — unchanged`**, deferring to the hyaku closure (`.ufo/reports/round-71/kotodama.md:67`: "a subagent the lane dispatched is still the lane and the wave-2 seats are not an outside spot-check"). Round 72 filed `improved` only once the outside spot-check had **agreed with both admits and a sampled reject** (`corpus/lessons/round-72-verifier-spotcheck.md:48-53,61`). Round 73 has no such agreement. Criterion 23 is additionally instrument-shaped, which criterion 20's first clause excludes by name, and its own round's receipts fail two of its own clauses (F4). |
| evidence pointers | `corpus/QUALITY.md:61` (criterion 20), `:66-75` (22), `:77` (23); `corpus/lessons/round-73.md:110-113`; `.ufo/reports/round-71/kotodama.md:67`; `.ufo/reports/round-72/kotodama.md:36-38`; `corpus/lessons/round-72-verifier-spotcheck.md:61` |
| what would upgrade it | The hyaku closure's **outside non-author** spot-check agreeing with this round's admits (S876–S880) **and** a sampled reject (S894 / S909 / S910 / S869) — exactly round 72's route. Then `improved`, and criteria 22/23 are corroboration, not the trigger. |
| the reading I reject, stated | Criterion 20's second clause read literally ("or a new lesson-grounded criterion") would fire `improved` on 22/23 today. I reject it because it makes criterion 20's first clause dead letter — every round that mines a mistake would fire discernment — and because the lane's own round-71 filing applied the clause and answered `unchanged`. If the closure adopts the literal reading, the verdict flips to `improved` **on criterion 22 only**: criterion 23 would still not carry it (F4), and 22's filed check is weaker than its rule (F3) with its S894 application missing the criterion-16 gaps (F2). |

---

## 2. Findings (each with its reproducing command and output)

### F1 — BLOCKER — an admitted entry's `recheck:` names a gate record that does not carry what it says it carries

`corpus/knowledge/linguistics/conlang-scholarship.amend-2026-10-23.md:7` states, of the three re-open commands:
"the three commands and their 2026-10-25 outputs stand in the round-73 gate record". They stand nowhere: the
lesson's `## Gate` has no grep command, and no evidence capture carries one.

```
$ grep -n 'grep' corpus/lessons/round-73.md | cut -c1-120
90:  `curl … | grep` recheck prose (with a literal pipe) moved out of the row and into the entry
115:Sweep for further mistakes in rounds 70–72 lessons: `grep -c '^| .* | none |' corpus/lessons/round-7[012].md` is a
$ grep -l 'grep' reports/round-73/evidence/*.txt || echo "(no evidence file carries grep)"
(no evidence file carries grep)
$ cat reports/round-73/evidence/S878.txt
# evidence S878 — claim C GATE (round 73)
fetch: GET https://journals.rudn.ru/semiotics-semantics/article/viewFile/31528/20955
user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36
access-date: 2026-10-25
http-status: 200
bytes: 959171
sha256: 9f745ddaccdbccbf254c5d890cd5b621ab241ea6d6de0219287c2e0c075ed07c
extract: pdftotext -enc UTF-8 S878.pdf -
locator: Abstract, p. 455
quote-words: 24
quote-found-verbatim: yes
```

The captures carry the fetch line, UA, status, bytes, sha256, locator and `quote-found-verbatim: yes` per row —
everything except the three grep commands and their "prints 1" outputs the recheck cites. Smallest safe
correction: repoint `recheck:` at `reports/round-73/evidence/S878.txt`/`S879`/`S880.txt` (which do re-verify the
spans), or paste the three commands and outputs into the lesson's Gate. Does not fire C's `kill_rule` (the leg
checks the header's shape, not the pointer's truth); it is an admitted statement that is false.

### F2 — MAJOR — criterion 22's first application S894 omits the criterion-16 gaps, and no retry budget was ever declared

Criterion 22's own text: "A 429 records its attempts and gaps per criterion 16 and is never read as UA-gating."
The S894 Gate record is the 429 record in scope:

```
$ python3 -c "import re;ln=[l for l in open('corpus/lessons/round-73.md',encoding='utf-8') if l.startswith('| conlang-scholarship.amend-2026-10-23.md (embedded')][0];print([c.strip() for c in ln.strip().strip('|').split('|')][2])"
status: UA "curl/8.7.1" -> HTTP 429, 1302 B, wall present ("Too many automated requests"); retry UA "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36" -> HTTP 429, 1302 B, wall present ("Too many automated requests"); automation: none; the 429 is a rate limit read per QUALITY 16, not UA-gating; no Wayback capture of the same page …
$ python3 -c "import re;s=open('reports/round-73/claims.json',encoding='utf-8').read();print({w:len(re.findall(w,s,re.I)) for w in ['retry','budget','attempt','gap between','passes']})"
{'retry': 0, 'budget': 0, 'attempt': 0, 'gap between': 0, 'passes': 0}
```

Two attempts, **no gap between them**, and the frozen claims declare no retry budget at all — so "read per
QUALITY 16" cites a budget that does not exist in the frozen bytes, and criterion 22's in-scope record fails
criterion 22's own 429 clause. Smallest safe correction: state the gap (the two requests' interval) in the S894
record and either declare the budget in the lesson or drop the "per QUALITY 16" claim.

### F3 — MAJOR — criterion 22's filed check is weaker than its rule: the one-UA record passes it

The criterion defines `SHAPE` as one request and adds "twice on the line". The regex in `QUALITY.md:73` is the
single unit; only `reports/round-73/telemetry/quality22-controls.txt:3` files the **doubled** variant. A record
carrying one UA therefore passes a re-opener who copies the criterion:

```
$ printf '%s\n' '| x | S900 | status: UA "curl/8.7.1" -> HTTP 200, 1234 B, wall absent; automation: none; no second UA recorded |' > /tmp/CritTrendFinal/oneua.txt
$ GROUND='^[|*-].*\| *(wall|captcha|status):'; SHAPE='UA "[^"…]{8,}" -> HTTP [1-5][0-9]{2}, [0-9]+ B, wall (present|absent)'; grep -Ec "$GROUND" oneua.txt; grep -Ec "$SHAPE" oneua.txt
1
1
$ # with the receipt's doubled SHAPE:
1
0
```

Under the criterion's literal `$SHAPE`, `GROUND=SHAPE=1` → **PASS** for exactly the round-72 one-UA defect the
criterion exists to catch. (The real Gate does pass both ways — `GROUND=2 SHAPE=2`, 2 occurrences per line,
`automation: none` ×2 — so the round's own application is sound; the criterion's text is not.) Smallest safe
correction: write `$SHAPE` in `QUALITY.md` as the doubled expression the controls receipt already uses.

### F4 — MAJOR — criterion 23's two new clauses are not satisfied by the round that authored them

Criterion 23 requires "its verdict line, **exit code** and counter sha256" and "the counter is also run at the
**FREEZE commit** (receipts present, landing absent) so artifact-vs-leg shape mismatches show **before data**".

```
$ grep -n '^exit=' reports/round-73/telemetry/selftest*.txt || echo "(none)"
(none)
$ grep -Hn 'stamped revision' reports/round-73/telemetry/*.txt | cut -c1-95
controls-c.txt:5: 8841ad3b896a0227674fa0725b818c999118046f
controls-ca.txt:4: 8841ad3b896a0227674fa0725b818c999118046f
controls-ca-r2.txt:4: 8841ad3b896a0227674fa0725b818c999118046f
controls-ca-r3.txt:4: 8841ad3b896a0227674fa0725b818c999118046f
measures-ca72-rerun.txt:3: 21ad3088cb64f7275e5541804e168f15d21d26d0
```

No selftest receipt carries an exit code (only `red-before-r3.txt` does), and **no committed telemetry receipt
stamps `af65165`** — the freeze run appears only in a wave-2 seat's report (`.ufo/waves/round-73/w2/ConnectorRoutes.md:56`),
i.e. after data, which is the very ordering R73-M6 names as the defect the clause is meant to prevent. Criterion
23 also has no "binds from" statement (criterion 22 has one), so a reader cannot tell whether round 73 conforms.
Smallest safe correction: commit an exit-code-bearing selftest receipt and a freeze-commit run receipt, or state
in the criterion and the lesson that it binds from round 74 and that round 73 did not run it.

### F5 — MINOR — an admitted entry's ground command contradicts itself at its own lands

`conlang-scholarship.md:7` states the command "= 0, run 2026-10-25". At the entry's own landing it prints 2:

```
$ grep -c 'ojs.unito.it\|philol.msu.ru' corpus/SOURCES.md
2
```

True only at base, which the sentence does not say. Correction: "= 0 at base 8841ad3".

### F6 — MINOR — criterion 22's three controls are filed as counts, not as fixtures

```
$ cat reports/round-73/telemetry/quality22-controls.txt
# QUALITY 22 controls (red-before): GROUND / SHAPE / automation counts over three fixture Gate lines
GROUND='^[|*-].*\| *(wall|captcha|status):'
SHAPE='UA "[^"…]{8,}" -> HTTP [1-5][0-9]{2}, [0-9]+ B, wall (present|absent).*UA "[^"…]{8,}" -> HTTP [1-5][0-9]{2}, [0-9]+ B, wall (present|absent)'
missing: GROUND=1 SHAPE=0 automation-none=0 -> FAIL
compliant: GROUND=1 SHAPE=1 automation-none=1 -> PASS
automation: GROUND=1 SHAPE=1 automation-none=0 -> FAIL
real lesson corpus/lessons/round-73.md: GROUND=2 SHAPE=2 automation-none=2 -> PASS
```

The fixture lines are not filed, so a re-opener cannot re-derive the three verdicts. Correction: append the three
fixture lines to the receipt.

### F7 — MINOR — criterion 23 describes R73-M6 but does not cite it by id

`QUALITY.md:77` names `R73-M4` and `R73-M5`; the freeze-commit clause's ground ("GROUND, SCRATCHMIRROR and
COLLCHECK read the committed receipts in shapes the receipts did not have") is `R73-M6` at
`corpus/lessons/round-73.md:113` and is not cited by id. M3/M4/M5 citations all resolve (verified by line). Add
the id.

### F8 — MAJOR — the S879 row lists no archived capture, against criterion 16's letter

Criterion 16: "each row lists its live URL followed by an archived capture of that same page".

```
$ python3 -c "import re;[print('archive present:', 'web.archive.org' in [c.strip() for c in l.strip().strip('|').split('|')][1]) for l in open('corpus/SOURCES.md',encoding='utf-8') if re.match(r'^ {0,3}\|\s*S879\s*\|',l)]"
archive present: False
```

The round documents the choice and leans on criterion 18's live-leg clause (`corpus/lessons/round-73.md:31-35`),
which permits a capture-less row only by implication; criterion 16 is not superseded and states no exception.
Smallest safe correction: record the 16/18 conflict in the lesson (or give S879 the Save-Page-Now capture as a
named second anchor while saying it does not carry the span). Note this does not make the entry fail the bar it
was admitted under, so it does not move the expansion verdict.

### F9 — MINOR — `counter-revisions.md` r2 row carries its sha outside the table

```
$ sed -n '1,12p' reports/round-73/counter-revisions.md | cut -c1-120
| r2 | reports/round-73/accept-ca.py | see `sha256sum` below | after the Ca landing commit e62d731 was first graded | …
be1917950bfb992dc4be30be00c0f1bf3b317b6fc88bea2431344cafaec4cde0  reports/round-73/accept-ca.py
```

Resolvable, but a row whose sha cell is prose is not the "old sha, new sha" record criterion 23 names. (Checked
and **clean**: the file's closing claim that the claim-C counter's selftest receipt is `selftest-r2.txt` /
`selftest-r3.txt` is true — both receipts run `accept-c.py --selftest` and print `SELFTEST: 29/29`.)

---

## 3. Checked and clean (so the closure does not re-derive these)

- Criterion 22's own check over the real Gate: `GROUND=2`, `SHAPE=2` (doubled form), 4 occurrences across the 2
  lines, `automation: none` on both — S894 and S910 are compliant applications of the **UA-binding** clause.
- Registry rows S876–S880: 11 cells each, `mined`, `2026-10-25`, `180d`, `used-by` exactly the citing entry;
  collision guard files re-counted: `reg-ids` 799, `staged-ids` 132, and `grep -cE 'S87[6-9]|S880'` → `0` in both
  `reg-ids` and `collisions`.
- README append block's counts: `find corpus/knowledge -type f -name '*.md' | wc -l` = `247`; linguistics = `32`;
  dirs `32/38/29/29/24/95`; registry `804`.
- Quote word counts as the lesson states them (S876 16, S877 9, S878 24, S879 16, S880 25) — recounted.
- Entry 1's ground claim about its predecessor: `conlang-methodology.md` cites Rosenfelder 6, Peterson 5,
  Okrent 2, Higley 2, WALS 8, PHOIBLE 7, APiCS 4.
- `accept-c.py` is byte-identical at freeze and lands (`95aee88…` both), so the "counter stays at r1" statement
  holds; `accept-ca.py` moved `f8ebb5d8…` → `222d4dd6…` with a recorded revision and a red-before.
- The round-72 wall figures criterion 22 cites resolve: `43,419 B` / `154,144 B` at
  `.ufo/waves/round-72/w1/ScoutCDXCanonical.md:79-80`; "5/5 wall plain, 5/5 clean browser" at
  `.ufo/waves/round-72/w1/ScoutCapoeiraReopen.md:353`.
- Census receipts both end `exit=0` (`census-start.txt`, `census-end.txt`).

## 4. What I could NOT check

- **No live fetch by this seat.** I did not re-open S876–S880, the Springer/Cambridge pages, or the cyberleninka
  CDX; the UA measurements (M3, criterion 22's ground) and the five quotes are taken as filed. A fetch here would
  need its own UA record and belongs to the claim seats.
- **No counter run.** I did not run `accept-c.py` or `accept-ca.py` at lands; leg counts are unverified by me.
- **No wave-1 seat report read in depth** (34 of 37): pointers only.
- **No guard-proof or mirror receipt content check** (`.ufo/waves/round-73/assimilation/guard-proof/*`,
  `validate-receipt.txt`) beyond the lesson's quotes.
- **The hyaku closure's spot-check does not exist yet**, so the discernment branch that would upgrade the verdict
  is untestable today by construction — which is why I filed `unchanged`.
- I did not evaluate whether the amendment's §4 directives clear criterion 4; that is a review-only judgment
  (criterion 11) and I have flagged it as the expansion downgrade path rather than ruling it.
