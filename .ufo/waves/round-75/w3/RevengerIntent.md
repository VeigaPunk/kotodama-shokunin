# RevengerIntent — round 75, wave 3 (falsify): the round-74 routed defects, intent reconstructed and attacked

Leaf seat. Lane `kotodama-shokunin`. Base `f556d1049fe651d3d63975600b13acd9fb686f15`; freeze
`5d0167464309d8133991b30f7d7a7011a6a0fd14`; claim Ca landed `012e8d3c8b92f47c734f735d58d118d574fe6a14`;
claim C landed `4f5e3b2535c2c06c51627dc2736c40183847cae1`; lane main at dispatch `82ced5cc205a116516e40895c4241415d54dae52`
(measurements + w3 spec only). Everything below is read over committed bytes or re-derived by me in a
scratch clone; no network fetch, no source re-open (out of this seat's scope), no full counter run.

Method: (1) reconstruct what each round-74 routed item was *for*; (2) test whether round 75's landing
serves that intent; (3) classify **LANDED / POINTER-ONLY / DROPPED / RECURRED / VOID** with `file:line`
evidence. Probes that grade code call the **frozen counter's own** `sources_diff`
(`reports/round-75/accept-ca.py:488`) rather than a paraphrase of it.

---

## 1. The routed set, and what each item was for

`corpus/lessons/round-74-verifier-spotcheck.md` §5 (R1–R4) and `corpus/lessons/round-74.md`
`## Routed to round 75` (items 1–5). Intent, reconstructed from the routing text and the defect it names:

| id | routed item | intent (what the item is *for*) |
|---|---|---|
| R1 | APPENDONLY treats a contract-permitted SOURCES `used-by` edit as a violation | make the counter agree with `corpus/SOURCES.md:9-11` **rule 2** — the three cells may change in place — so a tree carrying two claims can be green, *without* licensing the edits rule 2 forbids |
| R2 | round-74 Gate reject reasons for staged S899/S900 are false | correct the record append-only (never rewrite round-74), keep register S816/S817 refused, and add a criterion so a reject reason names the artifact it was observed on |
| R3 | report's dangling "see the closing line below" pushed-hash pointer (D1) | every future report states the pushed lane hash **inline**, so the filed revision is resolvable without a live remote |
| R4 | the carried-over lane items | clear accumulated lane debt in the files that own it (SHONEN, README index/headings, `sweep.py`, frozen-control timing, the `lands == freeze` pass, the S877 scope row) |
| item 1 | 34 remaining staged files need a registered parent + captured quote | register parents *before* any amendment cites them |
| item 2 | 4 (now 6) path-present files need a **byte-level decision** | stop the same staged copies resurfacing: diff for new claims, or record as superseded |
| item 4 | R73-M4: lesson row + **QUALITY 23 addendum** | a re-pointed read path lands with its fixture; a mutant's redness is shown against a green-first fixture |
| item 5 | R74-M5 register URL↔quote adjacency guard | the pairing checker needs a guard so a register row cannot carry its neighbour's quote |

---

## 2. Disposition

| # | item | disposition | evidence |
|---|---|---|---|
| 1 | **R1** rule-2 exemption | **LANDED, with a widened rule (D1) and stale receipts (D2)** | `accept-ca.py:259` `RULE2_CELLS = ("status","recheck","used-by")`; `sources_diff` (:488-554) exempts a pre-existing row whose differing cells are all rule-2; wired at `:1905`; new leg `R1EXEMPT` `:2458-2512`; fixtures `reports/round-75/fixtures/r1exempt-{green,red,mixed}.json` (all three in the freeze commit). `measures-ca.txt`: `LEG PASS R1EXEMPT verdicts={'green': True, 'red': False, 'mixed': False}` |
| 2 | **R2** S899/S900 reasons | **LANDED** | `corpus/lessons/round-75.md:380-403` (new lesson, append-only; `round-74.md` byte-identical base→C, `git diff --stat f556d1 4f5e3b2 -- corpus/lessons/round-74.md` empty); rows `:392`/`:393`; ledger pairs L75-08/L75-09 (`ledger.json`), SCORECARD rows carry the evidence path; QUALITY 27 at `corpus/QUALITY.md:127` (012e8d3). My re-runs: both spans `→1`, all three cross-checks `→0` (§4 receipts) |
| 3 | **R3** pushed-hash inline | **NOT LANDED — no carrier exists** | `git log --all -- .ufo/reports/round-75` → empty; `/home/vgpnk/Projects/shokunin/.ufo/reports/round-75/` holds `audio.md game-dev-2d.md game-dev-3d.md kotoba.md` only. The round-74 defect is verbatim at fleet pin `3a74016:.ufo/reports/round-74/kotodama.md:20` (`Lane pushed hash: see the closing line below …`) with no closing line. The w1 draft had a ledger pair measuring it (`.ufo/waves/round-75/w1/ScoutLedgerSweepB.md:12`, `w1/ScribeSkillGates.md:96-101`); the frozen ledger replaced L75-08 with the S899 correction — the machine carrier was dropped, and `round-75.md:337` files R3 as "stays pointer" without an action item |
| 4 | **R4a** S877 superseding row | **DROPPED (deferred)** | `grep -n 'supersedes S877' corpus/SOURCES.md` → 0; base→C changes 0 registry lines; routed again at `round-75.md:346-348` ("No S877 successor is in this round's row set") |
| 5 | **R4b** SHONEN `412 rows` | **LANDED** | `SHONEN.md:6` at 012e8d3: "rows: 808, mined: 713, queued: 58, rejected: 37"; ledger L75-01 REPAIR, `measure_ca` row `observed_lands='808'` |
| 6 | **R4c** README index 245/247 | **LANDED** | base→Ca inserts the two heritage rows (`git diff f556d1 012e8d3 -- corpus/README.md` → `+ heritage-taxonomy-models.md`, `+ ….amend-2026-10-24-r13.md`); index rows 247→249; `sweep-fixed-after-ca.txt` `rows 249 files 249 / missing_from_index 0 / orphan_rows 0 / exit 0`; footer discrepancy kept as ANNOTATE L75-04 (249 vs 247) |
| 7 | **R4d** `sweep.py` first-footer | **LANDED, load-bearing** | `reports/round-28/readme/sweep.py` repaired (sha256 `7e0566ad…`), base `9b2ccac0…` red on the same tree (`sweep-base.txt`: `totals_line 243 totals_ok False`, exit 1); control C1 (base bytes on the after-Ca tree) still red → the repair, not the landing, greens it |
| 8 | **R4e** junk receipts post-dating the freeze | **RECURRED, and now asserted false** | freeze commit carries **no** `controls-*.txt`, `junk-*.txt`, `measures-*.txt`, no `reports/round-75/evidence/` (`git ls-tree -r 5d01674 reports/round-75` → 14 files, 7 telemetry: census-start, gap-sweep, r1exempt-{green,red,run}, selftest-{c,ca}); `controls-c/ca` added at 012e8d3, `junk-*` + `measures-*` at 82ced5c (after both landings). Yet `claims.json:3` says the freeze commit adds "…both counters, **the do-nothing and junk-landing controls and the build evidence**" |
| 9 | **R4f** `accept-c.py` passing at `lands == freeze` | **LANDED** | `controls-c.txt` control 1: `ACCEPT-C-75: FAIL legs=4/13`, exit 1, data legs red with FROZENCFG green; lands==base refused (0/13, exit 2) |
| 10 | **item 2** six path-present byte decision | **DROPPED (deferred one round, disclosed)** | `round-75.md:109-120`, closing "none was written this round, and **no decision is taken here**"; routed to 76 at `:341-342`. Round-74 said "the next round **must** either diff them … or record them as superseded". Neither counter names any of the six files (`grep -c` = 0 in `accept-c.py`, `accept-ca.py`); the set is graded only as the integer 6 |
| 11 | **item 1** 34 staged files | **PARTIAL; dropped from the routing chain (D10)** | narrative family handled (5 files: 3 adopted, 2 refused, `round-75.md:92-96,107`); 29 others re-refused with reason+flip (`:100-107`) but the obligation is absent from `## Routed to round 76` (`:339-360`) |
| 12 | **item 4** R73-M4 + QUALITY 23 addendum | **LANDED** | `corpus/QUALITY.md:164` addendum (both limbs: re-pointed path lands with its fixture; mutant redness against a green-first fixture) at 012e8d3; the lesson row was already in `round-74.md` `## Mistakes` |
| 13 | **item 5** R74-M5 adjacency guard | **POINTER-ONLY** | `round-75.md:322-323` and Routed-to-76 `:343-345`; no checker added (no new tool path in the round) |
| 14 | `SKILL.md:594` civilizations 94 vs 95 | **VOID at base** (already repaired) | `git show f556d1:SKILL.md | sed -n 594p` → "95 entries"; no round-75 action owed |
| 15 | fleet report `c1b5b476…` stale HEAD sentence | **VOID at the pinned bytes; round-75 silent** | `grep -c c1b5b476` in the fleet-pinned report (sha256 `354273bc…` = the pin) → 0; 0 mentions in `round-75.md` |

---

## 3. Defects (exact list)

**D1 — (HIGH) The R1 exemption enforces rule 2's cell list but not rule 2's logging clause.**
`corpus/SOURCES.md:9-11`: "only `status`, `recheck` and `used-by` change in place, **each change logged
old→new in a round lesson**". `accept-ca.py:488-554` decides the exemption on the differing cell set only;
nothing in either counter or in `scripts/sources-census.sh` reads a lesson log (grep: no match). Proven on
the frozen counter (§4): an **unlogged** `used-by` edit and an **unlogged** `status: mined → rejected` edit
on pre-existing row S004 both return `problems=[]` → APPENDONLY green. Before R1 every in-place change was
refused (over-broad but safe); after R1 a silent status downgrade of any mined row is accepted and no leg
reports it. The routed wording ("exempt rule-2 cells") was met literally, so this is a *routing* defect as
much as an implementation one — but the landed rule is now broader than the rule it cites.

**D2 — (MEDIUM-HIGH) The frozen R1EXEMPT receipts cite a revision that does not exist, and do not match the
frozen fixtures.**
`reports/round-75/telemetry/r1exempt-green.txt:6` `# freeze: cb7fe05518dfa7722e108d9299819464564331e0`;
`git cat-file -t cb7fe055…` → *fatal: could not get object info* (not on any branch). Both receipts print
`LEG FAIL R1EXEMPT` — the counter that produced them rejected its own receipt check. Receipts name
`# edited-row: S001` (`r1exempt-green.txt:13`) while the committed descriptors name `"row": "S004"`
(`fixtures/r1exempt-green.json:3`): the descriptors committed "with the freeze" are not the ones the
receipts ran. The leg still passes because it only string-matches the receipts
(`accept-ca.py:2491-2508`: `LEG PASS APPENDONLY`, `exit 0`). *Substance is not harmed* — I rebuilt the
fixtures from the descriptors and graded them with the frozen `sources_diff` (green/red/mixed all as
claimed, §4) — so this is an evidence-provenance defect, not a false claim.

**D3 — (MEDIUM) COMBINED never exercises the exemption at the graded tree, but is claimed to.**
`claims.json:175` (Ca `after`): "COMBINED separately checks APPENDONLY at the explicit tree carrying both
landings, **including the in-place rule-2** and C-owned README heading changes." At `012e8d3` and at
`4f5e3b2` the number of changed lines versus base in `corpus/SOURCES.md` is **0** (`git diff -U0 base <rev>
-- corpus/SOURCES.md | grep -cE '^-[^-]'` → 0 for both), so there is no in-place rule-2 change and
`rule2-edits=0` at the combined tree. The COMBINED pass is therefore green but vacuous for R1; R1 is
exercised only by the synthetic leg.

**D4 — (HIGH) R4e recurs, and the frozen claims assert the opposite.**
The freeze commit does not carry the do-nothing or junk-landing controls, nor "the build evidence", yet
`claims.json:3` says it does. Controls land with Ca (`012e8d3`), junk + measures after both landings
(`82ced5c`). This is exactly `corpus/lessons/round-74.md` `## Corrections` item 2 ("the freeze commit does
not carry the junk receipts … they show the frozen counters reject 11 of 11 fixtures, not that they were
frozen with them") — routed to round 75 and reproduced, now with a false sentence in the frozen claims.

**D5 — (MEDIUM) The landed lesson says four routed items are still open when the round's own claim closes
them.**
`corpus/lessons/round-75.md:336-337`: "R2 is answered below; **R1, R3 and R4 stay pointers**"; `:359-360`:
"R74-M3, … and **closure R1/R3/R4** stay pointers as listed under Mistakes; **none is closed by this
round**." Against that: R1 has a dedicated leg and fixtures (claim Ca, `R1EXEMPT` PASS), R4b/R4c/R4d/R4f
are repaired by Ca (ledger L75-01…L75-04, `sweep.py`, `controls-c.txt`). A reader of the lesson cannot see
that R1 was implemented; the routing text contradicts the claim. Only R3 (D9) and R4a (D8) are truly open.

**D6 — (LOW-MEDIUM) Stale draft sentences landed unedited.**
`round-75.md:5`: "no freeze commit exists — `git cat-file -e HEAD:reports/round-75/claims.json` → absent,
so the round's files are untracked working bytes and this lesson grades none of them" — at the commit that
lands the lesson (`4f5e3b2`) `git cat-file -e 4f5e3b2:reports/round-75/claims.json` **succeeds**. Same class:
`:312` (R75-M1: "At this wave `git cat-file -e HEAD:reports/round-75/claims.json` still fails") and
`:330-333` (R74-M8 "at this wave neither is committed … Open until freeze" — both counters are in the freeze
commit).

**D7 — (MEDIUM) The six path-present files get no byte-level decision, and no counter binds the set.**
`round-75.md:109-120`. The digest pairs are **correct** (all twelve 12-hex values reproduced, §4), but
neither counter names the six files (only the integer `6`), so the "decision owed per file" has no carrier
and round 74's "the next round must" is unmet. Terminology defect in the same sentence: the second column
is content sha256, not the lane's *blob* id — `git rev-parse f556d1:corpus/knowledge/<path>` yields
`be88f79dd5f3`, `7bc1b6da656b`, `866793be9912`, `af8a4edacd5d`, `1a4efeed402a`, `87a0a0590bc5`, none of
which is the printed hex, so the stated reproduction command does not return the printed value.

**D8 — (MEDIUM) The S877 superseding row is not written.**
No `supersedes S877` row; the used-by cell is untouched (0 changed registry lines base→C). Routed to 76
(`round-75.md:346-348`). Round-74 named it inside R4, so the group "R4" cannot be reported closed, which is
also what D5's blanket sentence hides.

**D9 — (LOW) R3 has no artifact to be judged on, and its only machine carrier was removed.**
No round-75 report anywhere reachable (§2 row 3). The w1 draft pair that measured the round-74 pointer was
replaced in the frozen ledger. Until the L1 files `.ufo/reports/round-75/kotodama.md`, R3 is unobservable;
if that report repeats the round-74 template ("see the closing line below") the defect lands again.

**D10 — (LOW) Routing-chain drop of round-74 item 1.**
The refusals of 29 staged files carry reason + flip (`round-75.md:100-107`), so nothing is silently
re-refused; but the standing obligation — "each needs a registered parent row with a captured,
exactly-once quote before any amendment can cite it" — does not appear in `## Routed to round 76`
(`:339-360`). The next round is told about the six files but not about the 29.

**D11 — (LOW) The correction's added attribution is true but uncited.**
`round-75.md:393` adds "the Sowers-Wills clause … belongs to lane S880's document". Verified true:
`reports/round-73/evidence/S880.txt` carries `Sowers-Wills's “Phonology from the inside out: Constructed
language as a pedagogical Tool”` (1 hit, curly quotes). But the row's own re-derivation command greps only
the 2022 page, and the register's exact span (straight quotes) is **0** hits in that capture — so the added
clause names an artifact that the correction neither cites nor re-derives, and the span as written is not
present on it. That is the artifact-vs-span class QUALITY 27 was written for, committed one paragraph above
the criterion it cites.

---

## 4. Receipts (verbatim; produced in `/fast/scratch/hyaku/kotodama-r75/RevengerIntent/`, since removed)

### 4a. Exemption semantics — frozen counter's `sources_diff`, fixtures built on base `f556d1`

```
CASE: rule2 used-by (UNLOGGED in any lesson)
  changed paths : ['corpus/SOURCES.md']
  lesson touched: False
  rule2_edits   : ['S004']
  problems      : []
  -> APPENDONLY green: True
CASE: rule2 status mined->rejected (UNLOGGED)
  changed paths : ['corpus/SOURCES.md']
  lesson touched: False
  rule2_edits   : ['S004']
  problems      : []
  -> APPENDONLY green: True
CASE: non-rule2 teaches (control)
  changed paths : ['corpus/SOURCES.md']
  lesson touched: False
  rule2_edits   : []
  problems      : ['row S004 changed outside the rule-2 cells (teaches)']
  -> APPENDONLY green: False
MIXED teaches+used-by -> rule2_edits=[] problems=['row S004 changed outside the rule-2 cells (teaches)'] green=False
```

Driver: `git clone -q --shared /home/vgpnk/Projects/shokunin/kotodama-shokunin …/fix`, checkout
`f556d1049fe651d3d63975600b13acd9fb686f15`, one commit per case
(`git -c user.name=fixture -c user.email=f@f.invalid`), then
`importlib` the frozen counter (`sha256 98d8e7974c82d048db67fe8eebd06cd78308bc0e3233c922ec16f527fd1ac235`,
identical to `git show 5d01674:reports/round-75/accept-ca.py | sha256sum`) and call `sources_diff(FIX, BASE, head)`.
`git -C …/fix rev-parse --show-toplevel` → `…/fix`. No lesson file in any fixture → the log limb is untouched.

### 4b. R2 re-derivation (the frozen ledger's own commands)

```
$ git grep -c '非凡特性来自最初造物主' f556d1 -- reports/round-74/evidence/S883.txt
f556d1…:reports/round-74/evidence/S883.txt:1
$ git grep -c '这个我肯定考虑过' f556d1 -- reports/round-74/evidence/S884.txt
f556d1…:reports/round-74/evidence/S884.txt:1
$ (cross-checks) 这个我肯定考虑过 in S883 ; 非凡特性… in S884 ; Sowers in S884  → no output, exit 1 (0 hits) each
$ git diff --stat f556d1 4f5e3b2 -- corpus/lessons/round-74.md      → (empty)
$ git show 012e8d3:corpus/QUALITY.md | grep -n '^27\.'
127:27. **A reject reason names the artifact it was observed on** …
```

### 4c. Freeze contents vs `claims.json:3`

```
$ git ls-tree -r --name-only 5d01674 reports/round-75
… claims.json · ledger.json · accept-c.py · accept-ca.py · fixtures/r1exempt-{green,mixed,red}.json
   telemetry/{census-start,gap-sweep,r1exempt-green,r1exempt-red,r1exempt-run,selftest-c,selftest-ca}.txt
$ git ls-tree -r --name-only 5d01674 reports/round-75/evidence | wc -l      → 0
$ for f in controls-c controls-ca junk-c junk-ca junk-r75-run measures-c measures-ca; do
    git log --format='%h %ci' --diff-filter=A -- reports/round-75/telemetry/$f.txt | tail -1; done
controls-c.txt 012e8d3 17:44:16 ; controls-ca.txt 012e8d3 17:44:16
junk-c.txt 82ced5c 17:49:01 ; junk-ca.txt 82ced5c ; junk-r75-run.txt 82ced5c
measures-c.txt 82ced5c ; measures-ca.txt 82ced5c
```

### 4d. Six path-present digests (staged = `sha256sum` of the read-only staged file; lane = `git show base:path | sha256sum`)

| file | staged | lane base | lesson printed pair | verdict |
|---|---|---|---|---|
| heritage-taxonomy-models.md | b17223b9a04b | 09175b1849fb | `b17223b9a04b` / `09175b1849fb` | equal |
| …amend-2026-10-24-r13.md | 9ed5ceefe5b1 | 8544fe1ec531 | `9ed5ceefe5b1` / `8544fe1ec531` | equal |
| worldbuilding-setting-practice.md | 44a0899c5054 | 990e667c34bf | `44a0899c5054` / `990e667c34bf` | equal |
| …amend-2026-10-23.md | 39ac34ea0292 | 49a4432ae83b | `39ac34ea0292` / `49a4432ae83b` | equal |
| conlang-scholarship.md | ce666a2bf15d | fe7e214adb04 | `ce666a2bf15d` / `fe7e214adb04` | equal |
| …amend-2026-10-23.md | 8f889666b32c | 01029a642c9f | `8f889666b32c` / `01029a642c9f` | equal |

Staged tree counts reproduced: 40 files (culture-material 9, linguistics 17, myth-symbol 5,
verification 9); families 11/5/3/2/2/2/1/9/5 = 3 adopted + 6 path-present + 31 refused = 40.

### 4e. Zero in-place registry edits at either landing

```
$ git diff -U0 f556d1 012e8d3 -- corpus/SOURCES.md | grep -cE '^-[^-]'   → 0
$ git diff -U0 f556d1 4f5e3b2 -- corpus/SOURCES.md | grep -cE '^-[^-]'   → 0
```

---

## 5. Silent drops (items with no carrier and no pointer)

1. **R3's machine carrier** — the w1 ledger pair measuring `see the closing line below` was removed from the
   frozen ledger with no note; the lesson keeps R3 only as a "stays pointer" phrase, not as an action item.
2. **Round-74 item 1's obligation** for the 29 remaining staged files — absent from `## Routed to round 76`.
3. **The six path-present identities/digests** — printed in the lesson but bound by nothing (no counter, no
   ledger pair, no routed action naming the files).
4. **`c1b5b476…`** — void at the pinned report; round 75 neither says so nor closes it (a stale loop, not a
   byte-level drop).

---

## 6. Verdict

**PARTIAL.**

- Genuinely landed and re-derived by me: **R2** (correction + QUALITY 27 + both ledger pairs, round-74 bytes
  untouched), **R4b/R4c/R4d/R4f** (SHONEN 808, heritage index rows + repaired sweep with a red instrument
  mutant, `lands == freeze` now 4/13 FAIL), **round-74 item 4** (QUALITY 23 addendum).
- Landed but wider than its own stated rule: **R1** — the exemption accepts unlogged rule-2 edits, including
  a silent `mined → rejected` status change (D1), and its committed receipts cite a non-existent freeze and
  a different row than the frozen fixtures (D2); the COMBINED check that is supposed to show the exemption on
  real data sees zero rule-2 edits (D3).
- Recurred: **R4e** — junk/do-nothing controls still post-date the freeze, and `claims.json:3` now asserts
  the freeze carries them (D4).
- Dropped: **R3** (no report; draft ledger pair removed — D9), **R4a** S877 superseding row (D8), **the six
  path-present byte decision** (D7, deferred by its own text), **round-74 item 1's obligation** (D10).
- The round's own record misstates the disposition: `round-75.md:336-337,359-360` reports R1/R4 as still
  open while the round closed most of them, and three stale pre-freeze sentences landed at `:5`, `:312`,
  `:330-333` (D5, D6). The correction that fixes a false reject reason adds one true but uncited attribution
  (D11).

Confidence: high on every byte-level statement above (re-derived in-session); medium on the *intent*
readings in §1 (reconstructed from the routing text, marked as inference where the routing is silent,
notably R1's logging limb — the contract states it, the routing does not).

Limits: no source was re-opened and no counter was run end-to-end by this seat; leg verdicts are cited from
the committed receipts and, for the exemption, re-derived from the frozen counter's own function. Nothing
was written outside this report and my scratch dir (`/fast/scratch/hyaku/kotodama-r75/RevengerIntent`,
removed). No tool was installed or upgraded.

---

## 7. Late addendum — text appended to the lesson after this seat's reads (checked, not deferred)

While this seat was writing, an uncommitted `## Status at landing` block appeared at
`corpus/lessons/round-75.md:405`+ (working tree only; the last commit touching the lesson is `4f5e3b2`, and
`git diff 4f5e3b2 -- corpus/lessons/round-75.md` = +32 lines at the file's end, all after `:401`, so every
line number cited above is unchanged).

- **D6 is partly answered in the working tree, not at the graded revisions.** The block explicitly
  supersedes the pre-freeze tense ("no freeze commit exists", "the claims are `DRAFT`", "neither counter is
  committed", "at this wave") and names the freeze, both landings and both measures receipts. At
  `82ced5c` — the newest committed revision, and the one a grader reads — the stale sentences are still the
  only text. The remedy is honest but uncommitted; commits-before-report is the rule that binds it.
- **D4 stands unchanged.** `reports/round-75/claims.json` is clean in the working tree, so the frozen status
  sentence ("the commit that adds this file together with … the do-nothing and junk-landing controls and the
  build evidence") is still false at every revision; the new block lists the freeze's contents accurately
  (claims, ledger, both counters, R1EXEMPT fixtures + receipts, selftests, map, wave-1/2 evidence) and
  separately cites the controls, without repeating the false claim.
- **New reference-drift nit in the appended block:** it says the nine evidence captures were made "by
  `counters/capture-evidence.py`". No such path exists (`ls counters/` → absent; `git ls-files counters/` →
  empty); the file is `.ufo/waves/round-75/counters/capture-evidence.py`. Same class as R74-M8 and as D7's
  "blob" wording — a path printed from a scratch cwd that does not resolve from the lane root.
