# E02 — register-fit verification (claim C)

- Seat: `E02` | role: verifier | claim: **C** (coverage) | round 48, loop 2, position 2
- Baseline: HEAD `a01405dd36367292255c2652ac0a601f4cd6a0af` (`git rev-parse HEAD`, 2026-10-19), equal to `reports/round-48/claims.json:7` (`baseline_commit: "a01405d"`)
- Out path: `reports/round-48/cov/E02-register.md` (this file; the only path this seat wrote)
- Mission (verbatim, `reports/round-48/targets.json`, seat `E02`): *"Register-fit verifier: the entry satisfies the five-condition register test (the same test the other partition registers pass); confirm it belongs in culture-material not myth-symbol."*
- Read cut: first pass at `find reports/round-48 -type f` saw only `cov/C02-header.md`, `cov/C04-citations.md`, `cov/C09-couples.md`, `cov/M01-example.md`. I recorded the body legs `could-not-evaluate` in that pass. **Second pass, same session:** `cov/C01-entry.md` (a complete 227-line entry, `sha256 e52556572341bd82545f841cee01e7bf2c581c268910ff2a6f0c2f087cf44f84` of the fenced bytes) and `cov/M02-calibration.md` had filed. The verdict below is on **C01's fenced entry**, which is the drafted deliverable; the first-pass verdict is superseded and kept only where C01 disagrees with C02 (finding E02-4).
- Non-author statement: I drafted no cartography bytes and edited no fragment; every judgment below is from filed bytes plus commands I ran at `a01405d`.

**Verdict in one line.** **Register-fit PASS on all five admission conditions; partition ruling PASS (culture-material, not myth-symbol).** The 227-line drafted entry clears provenance (gate `findings=0`; 10 `to-verify` marks honestly placed), calibration (an **11-row** R/C/B/H/T bank at §12 plus a living-practice flag and a precision trap), coupling (14/14 unquoted `corpus/knowledge/...` targets in C01's field resolve; C02's separate field is 19/19 backticked tokens), usability (14 sections, decision tables, an 8-form "cannot show" table, one-rule NON-CANON example), and canon hygiene (scope + NON-CANON throughout). The partition ruling rests on the partition's own closed five-register family and the neighbours' own disclaimers, not on count arithmetic. Two P2 items: the word "register" in §1 could still be read as a sixth symbolic register (the r47 A02 naming risk), and **C01 and C02 file two different head blocks** — the assembly must pick one and re-run the couples/topic checks (E02-4).

---

## 1. Which five-condition test this seat is applying

The corpus has **two** different "five-condition" artifacts. The mission's parenthetical — "the same test the other partition registers pass" — selects the first; I name both so the seat cannot be read as conflating them.

**(a) The admission bar, `corpus/QUALITY.md:3-20`.** "An entry is admitted into `corpus/knowledge/` only when it clears all of":

| # | Condition | Text (paraphrase of the live clauses) | Clause lines |
|---|---|---|---|
| 1 | Provenance | every factual claim cited/checkable; unverifiable claims marked `(to-verify)` inline | `:5-8` |
| 2 | Calibration | every framework entry names its status — mainstream / contested / discredited — with the reason | `:9-12` |
| 3 | Coupling | the `- couples:` line names the systems/files the entry connects | `:13-15` |
| 4 | Usability | decision tables, typology tables, checklists, worked examples; no essays | `:16-17` |
| 5 | Canon hygiene | no entry decides what is true in any world; ends at the handoff | `:18-20` |

This bar is applied across the whole corpus, not to one partition: measured at `a01405d`, `culture-material` **25/25** and `myth-symbol` **26/26** entries carry `- topic:`, `- sources:`, `- couples:` and at least one `calibrat*` term; `- scope:` is the newer house convention (3/25 and 3/26, both partitions equally). Command in §7. A mechanical gate implements clauses 1–3: `tools/gates/provenance-audit.py:5` ("admission bar for provenance apparatus, corpus/QUALITY.md items 1-3"), with the documented limit that `missing-calibration` "fires only when the word `calibrat*` is absent entirely — the gate cannot judge whether the named status is warranted" (`:19-21`).

**(b) The entry's own cartographic test, r47 `cov/C01-entry-a.md:109`.** "What makes a map a register — the five-condition test": **ground index, bounded notation, structural selection, conventional readability, reproducibility/citability** (r48 renames the first "referent index", `C01-entry.md:93`). This is *content method* (what counts as a map), specified for r48 at `scout/K01-rightsized-spec.md:137` (`§2`, 18 lines). It is not the admission bar and cannot be used to admit or reject the entry; it is the entry's subject matter.

---

## 2. Clause-by-clause verdict on the drafted entry

Primary artifact under test: the complete fenced entry of `reports/round-48/cov/C01-entry.md` — **227 lines** (fence-exclusive; `wc -l` of the extracted bytes → 227), occupying file lines 70–296. Head fields (file lines): `:73` topic, `:72` gap filled, `:74` sources, `:77` couples, `:78` verified-at, `:79` recheck, `:80` scope; **no `- source:` field** (C02 supplies one; see E02-4). Secondary artifact: C02's separate 23-line head block (`C02-header.md:112-136`) and M01's 27-line example (`M01-example.md:28-55`; M01's `:39` reports 28 by its fence-inclusive convention — §4 Obs-1).

| Clause | Verdict | Basis (measured, not asserted) |
|---|---|---|
| 1 Provenance | **PASS** | C01's `- sources:` states every in-corpus anchor was "re-read in this seat" and that the external shelf is "**not consulted this round**", every edition/page `(to-verify)` (`C01-entry.md:74-76`). The gate returns `findings=0` with **10 marks on 9 lines** (§ gate below). I re-read the load-bearing anchors and all matched: `cosmology-cosmography.md:27` ("how the world is drawn (maps)"), `:71` ("symbolic, not survey maps"), `:102` ("not cartographic"), `sacred-topography-pilgrimage.md:5`, `direction-symbolism.md:51` ("compass trap"), `architecture-settlement-lexicon.md:95` ("surveyed with the groma"; "The grid is cadastral"), `craft-artisan-lexicon.md:54` (ladder header — **not** `:44`, the r47 B4 miscite), `:65`, `naming-systems.md:70` ("a map is an archive of coups"). I also checked the two anchors most likely to be off-by-one in the new body: `calibration-registry.md:35-39` is exactly the R/C/B/H/T rows (R `:35`, T `:39`), and `writing-media-surface-economy.md:78` is exactly "Cheapness widens the base … not … authority". The r47 B2 count is corrected to `cartograph` **2 files / 2 lines**. |
| 2 Calibration | **PASS** | §12 (`C01-entry.md:271-289`) is an **11-row** bank with a status column keyed to `calibration-registry.md:35-39`: neutral-map R, flat-earth R, portolan C, primitive-map R, map=territory "R as metaphysics; B as procedure", one-way-diffusion C, plus five further R/B rows. A living-practice flag (indigenous cartographic sovereignty) and a precision trap follow the table (`:287-288`). The R/C/B/H/T definitions I verified live at `calibration-registry.md:35-39`; the r47 P2-1 wording conflict is reconciled in the map=territory row rather than left as two flat assertions. This closes the clause the first pass could not evaluate. |
| 3 Coupling | **PASS** | C01's `- couples:` (`:77`) names **14 distinct `corpus/knowledge/...` targets, 14/14 resolve** at `a01405d` (all repo-relative, no dangling token); it includes the two C09 said were missing from C02's field (`celestial-symbolism-calendars.md`, `sacred-kingship-mythic-charter.md`) plus `to-verify-triage-protocol.md`. C02's separate field is 19 backticked tokens, **19/19 resolve** (my parse) and 19/19 Tier-1 `direct` per C09 (`cov/C09-couples.md`). Both fields are non-empty and resolve; the style/content mismatch is E02-4, not a clause-3 failure. |
| 4 Usability | **PASS** | 14 sections, each ending in a table, rule or decision rows: the 5-condition test applied to six object classes (§1), a 12-row boundary table (§2), a 7-link chain with failure column (§3), **8 of 8 forms** each with a "cannot show" column and minimum build (§4, closing r47 B9), projection/scale/orientation as claims (§5), reproduction and trade (§6), a 5-link warrant chain (§7), six silence classes and the legal instrument (§8), a 9-step build order (§9), a 6-row decision record (§10), the one-rule NON-CANON example (§11), the 11-row bank (§12). QUALITY's "decision tables … worked examples. No essays" (`QUALITY.md:16-17`) is met. The 227-line total is 1.03× the live partition max (221, `funerary-material-culture.md`) and inside the ≤~250 discipline. |
| 5 Canon hygiene | **PASS** | `- scope:` says the entry "decides nothing about any world, admits no map into canon" and hands canon to lore-shokunin (`C01-entry.md:80`; repeated at `:296`). §11 is headed `NON-CANON` and opens "**NON-CANON.** The culture, place and numbers below are invented … nothing below is canon" (`:246,248`). Every "canon" occurrence in the entry is a negation or a handoff (grep in §7). No promotion/clearance/closure verb. |

**Gate run on C01's entry.**

```
$ python3 -B tools/gates/provenance-audit.py .scratch/e02-c01-entry.md
INFO to-verify-count: .scratch/e02-c01-entry.md: 10 mark(s) on 9 line(s)
INFO scan: files=1 marks=10 mark-lines=9 findings=0 blocked=0
exit=0
```

10 unresolved marks on 9 lines is the honest posture (external shelf and page-level legs not inspected), not a defect; the gate counts marks as inventory (`provenance-audit.py:26-29`) and cannot judge clause 2 (`:19-21`), which is why §12 was read by hand.

---

## 3. Partition ruling: culture-material, not myth-symbol

**Ruling: culture-material.** Four independent legs; none of them is a row-count argument.

**3.1 Positive membership — the object is a production chain.** `culture-material` is the partition of made systems with a chain from raw step to object: `writing-media-surface-economy.md:3` (preparation chain → tool → ink → unit → cost driver), `timekeeping-instruments.md:3` (instrument families → resolution → institutions → archaeology), `architecture-settlement-lexicon.md:95` (castrum grid, groma, cadastral plan), `craft-artisan-lexicon.md:3` (workshop register), `trade-economy-lexicon.md` (measures and exchange). The cartography seed is the same shape: **survey → projection → drawing → reproduction → trade/legal use** (`reports/round-44/scout/K02-gap-scout.md` §4.3; `C02-header.md:114`; `K01-rightsized-spec.md:84-95`). Its master claim — "a map is an argument about space … its authority comes from the survey chain behind it" — is a production claim, and its scarcity regimes are survey labour, control network, drafting skill and reproduction (`K01-rightsized-spec.md:84`), i.e. material-culture variables.

**3.2 Negative test — the symbolic register family is closed at five.** `myth-symbol/symbolism-synthesis-method.md:23` defines the symbolic grammar as "a small closed inventory of signs — the five canonical registers: **color, animal, number, celestial body, direction**"; `direction-symbolism.md:3` confirms direction "named in symbolism-synthesis-method.md §1 as one of the five canonical symbol registers". Cartography is not one of the five, and the r47 draft already made the explicit ruling: "The map is a **composition register**, not a symbolic register … That is why the entry belongs in `culture-material`: a map is a made object with a production chain, not a value system" (`reports/round-47/cov/C01-entry-a.md:105`). Placing it in `myth-symbol` would either add a sixth register against the partition's own closed-family rule or leave the entry's production content homeless while it re-owned symbolic content.

**3.3 The neighbours already own the symbolic content and say so.** `cosmology-cosmography.md:27` defines cosmography as "how the world is drawn (maps), named (toponyms), walked (processions, pilgrimage), and built (cities, temples)"; `:71` then distinguishes the T-O diagram from "**survey maps**"; `:102` calls T-O diagrams "symbolic devices, **not cartographic**". `sacred-topography-pilgrimage.md:5` owns "sacred-geography mapping … as a diagram"; `direction-symbolism.md:51` owns the orientation register and the compass trap. What is missing is not the map's meaning but the made sheet: the surveyed, projected, reproduced object. That is `culture-material`'s slot. Both r48 heads disposition `:27` explicitly as "world-drawn content" versus "the surveyed sheet as production" (`C02-header.md:115`; `C01-entry.md:101-103`), which preserves the one-owner rule instead of over-claiming.

**3.4 The discriminating precedent.** `mineral-stone-symbolism.md:3` landed in `myth-symbol` because it filled a **symbolic register slot** the method file names (`symbolism-synthesis-method.md:29`, the lapidary component). Cartography fills no register slot; it is a made-object system whose symbolic components are borrowed from three neighbours and cited, not owned. The two are therefore opposite cases, and the lithic precedent argues *against* a myth-symbol landing here.

**3.5 Mechanics, verified (not inferred).** Slug free in both partitions (`ls` → "No such file" for `culture-material/cartography-and-mapmaking.md` and the same path under `myth-symbol/`); 0 filename owners and 0 topic-line owners at `a01405d` (my own probes: `find … -iname '*cartograph*' -o … | wc -l` → **0**; topic probe → **0**). Sort position verified: `ls corpus/knowledge/culture-material/*.md | sed -n '5,7p'` → `calendar-festival-systems.md`, `costume-semiotics.md`, `craft-artisan-lexicon.md`, so the new row inserts between positions 5 and 6. Landing in culture-material moves it **25 → 26** and leaves myth-symbol at 26. The README row must be byte-equal to the **landed** head's `- topic:`; because C01 and C02 disagree, that is E02-4's assembly condition, not a settled anchor.

**Why the alternative is worse, stated plainly.** A myth-symbol landing would (i) require the entry to claim a slot the partition's method file closes at five, (ii) put it in direct tension with `cosmology-cosmography.md:27`'s "drawn (maps)" sentence rather than in a cited boundary relation, and (iii) move the wrong partition's count (myth-symbol 26 → 27) while leaving culture-material at 25 — a placement error no later README arithmetic can repair.

---

## 4. Findings

| ID | Severity | Finding | Fix |
|---|---|---|---|
| **E02-1** | **P2** | The body's §1 is headed "The register property" and says the test "decides whether an object belongs to this register" (`C01-entry.md:82,91`). In a corpus where "register" is the closed symbolic family's term, that can be read as an eighth-register claim; r47 A02 measured the same ambiguity as "a **naming risk, not a second owner**" (`reports/round-47/adj/A02-ownership.md:95`). §2 now supplies the one-owner boundary and answers `cosmology-cosmography.md:27`, but it never says the map is **not one of the five symbolic registers** — the r47 sentence that did (`reports/round-47/cov/C01-entry-a.md:105`). | Add one clause to §1 or §2: "the map is a **composition** register, not a sixth symbolic register; the five canonical registers keep their meanings (`symbolism-synthesis-method.md:23`) and this entry owns only the sheet's syntax." This is also why the entry belongs in `culture-material`. |
| **E02-2** | **P3** | The mechanical gate's calibration check is vocabulary-only (`provenance-audit.py:19-21`). Now that §12 exists the clause genuinely passes, but a green gate is still not its evidence — the gate would pass the same file with the bank deleted so long as the topic line kept the word. | Cite gate output for clauses 1–3 only; judge clause 2 by the 11 R/C/B/H/T rows at `C01-entry.md:273-285`. |
| **E02-3** | **P3** | `reports/round-44/scout/K02-gap-scout.md:183` says "these **five**" before a seven-row neighbour table (independently found by C15, `cov/C15-neighbors.md:53`). Filed bytes cannot be edited; the r48 draft must carry all seven rows and should not repeat the count word. C01's §2 boundary table carries **12** rows, a superset — no row is dropped. | Keep "seven neighbours" (or omit the count word) in any prose that summarises the table. |
| **E02-4** | **P2 (assembly)** | **C01 and C02 file two different head blocks, and both are internally verified.** Measured: `- topic:` is 775 chars (`sha256 a42926b1d0fe5ac5…`, `C02-header.md:114`) vs **1054 chars** (`sha256 aed27f526727bef2…`, `C01-entry.md:73`); C02 has a `- source:` field, C01 does not; C02's couples field is 19 backticked tokens, C01's is 14 repo-relative unquoted paths (all resolve, but the lane resolver's token extraction and C09's 19/19 result cover C02's field only). The sweep compares the README row to the entry's `- topic:` **byte-for-byte** (`reports/round-28/readme/sweep.py`, `topic_mismatch`), so pairing C02's row with C01's body (or vice versa) turns the sweep red. | Assembly picks **one** head. If C01's: re-run C09's resolver on that field and make C10's README row byte-equal to `C01-entry.md:73`; if C02's: use that block with C01's body and add C01's two extra couples targets. Record which in C13/W01. Do not merge fields from both. |
| **Obs-1** | observation | Line-count conventions differ by one for the same example block: my extraction of the fenced content gives **27** lines; M01's awk (fence-to-fence) gives **28** (`M01-example.md:39`). Both are correct under their conventions; the assembled-entry budget check must name its convention. | State "content lines (fence-exclusive)" in the length verification; keep the ≤~250 ceiling on that basis. |

No finding repeats any of R03's B1–B9. In particular I re-checked the three that touch register fit and citations: B3's false quote accusation is not repeated (the `naming-systems.md:70` quote is verbatim — `grep -n 'archive of coups'` → `70:`), B4's ladder anchor is correct (`:54-65`), and B8's competing `:27` sentence is dispositioned in both heads (`C02-header.md:115`; `C01-entry.md:101-103`). The two new-body anchors I spot-checked for off-by-one were both exact: `calibration-registry.md:35-39` (R–T rows) and `writing-media-surface-economy.md:78` ("Cheapness widens the base").

---

## 5. Re-check recipe for the assembled entry (what the integrator must run)

The drafted entry is filed; the **assembly** is not. Run these on the assembled bytes before admitting:

```bash
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
# 1. Stage the assembled entry (never write under corpus/)
python3 -B tools/gates/provenance-audit.py .scratch/<assembled>/cartography-and-mapmaking.md; echo $?
# expect: findings=0, exit=0; read the to-verify count as inventory only
# 2. Clause 2, by hand: the bank must exist and carry statuses
grep -c '^| ' <bank-section>            # 11 data rows in the filed draft; each row R/C/B/H/T per calibration-registry.md:35-39
# 3. Clause 3: resolve the field that actually lands (C01's unbackticked paths or C02's backticked tokens)
python3 -B tools/harness/basename-couples-resolver.py --census   # delta +14..+21 refs, all direct
# 4. Register naming: no sixth-register claim
grep -n 'composition register\|sixth symbolic' <entry>   # E02-1's one clause present
# 5. Length discipline
wc -l <entry>                           # measured 227 (fence-exclusive); ceiling ~250
# 6. Head consistency (E02-4)
#    exactly one of C01-entry.md:73 / C02-header.md:114 may be the README row; compare byte-for-byte
```

Acceptance for this seat's clause: gate exit 0; 11 calibration rows with status codes; every couples target in the landed field resolves; the composition-register clause present; 227 lines (≤~250); one head, not two. If the assembled entry fails any of these, the register-fit verdict is **FAIL** for that assembly — the filed-draft PASS above attaches to the 227-line fenced draft I read, not to bytes I have not seen.

---

## 6. What I did not verify

- **The assembled file and the README apply.** I read C01's fenced deliverable, not the integrator's merge; C13/W01 own assembly. I did not treat `.scratch/w02/landable.md` or any other seat's staging as the draft — it is a 797-line r47-shaped assembly, not the right-sized draft.
- **Every anchor in the entry.** I re-read 9 load-bearing anchors plus the two off-by-one candidates (`calibration-registry.md:35-39`, `writing-media-surface-economy.md:78`); C04 owns the exhaustive 55-row resolution and C06/C07 own boundary content.
- **Every external bibliographic detail.** No network; all editions/pages are `(to-verify)` and I checked none.
- **The README rev 2.5 edit and the post-landing sweep.** Ca/C10/C11 own those; I verified only the sort position and the partition counts.
- **The freshness gate replay and the final census.** Cited from `reports/round-48/claims.json:23` ("C FRESH … Ca FRESH … O STALE"); O01/O04 and V01/F01 own the replay and the 224 count.

---

## 7. Commands and write-surface statement

All run from the lane root, 2026-10-19, with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`.

```
$ git rev-parse HEAD
a01405dd36367292255c2652ac0a601f4cd6a0af
$ find corpus/knowledge -name '*.md' | wc -l
223
$ ls corpus/knowledge/culture-material/*.md | wc -l
25
$ find corpus/knowledge -iname '*cartograph*' -o -iname '*mapmaking*' -o -iname '*portolan*' -o -iname '*cadastr*' | wc -l
0
$ grep -rniE '^- *topic:.*(cartograph|mapmak|portolan|cadastr|atlas|survey map|world map|graticule|theodolite)' corpus/knowledge/ | wc -l
0
$ ls corpus/knowledge/culture-material/cartography-and-mapmaking.md
ls: cannot access '...': No such file or directory
$ ls corpus/knowledge/culture-material/*.md | sed -n '5,7p'
calendar-festival-systems.md
costume-semiotics.md
craft-artisan-lexicon.md

# five-clause application across partitions
$ python3 - (count topic/sources/couples/scope/calibrat per partition)
culture-material: files=25 topic=25 sources=25 couples=25 scope=3 calibration_vocab=25
myth-symbol:     files=26 topic=26 sources=26 couples=26 scope=3 calibration_vocab=26

# independent couples resolution (C02 header fenced block)
token count 19 / distinct 19 / unresolved []

# C01 fenced entry extraction (primary artifact)
fence lines 227 / sha256 e52556572341bd82545f841cee01e7bf2c581c268910ff2a6f0c2f087cf44f84
head fields (file lines): gap filled:72 topic:73 sources:74 couples:77 verified-at:78 recheck:79 scope:80   (no - source:)
$ python3 -B tools/gates/provenance-audit.py .scratch/e02-c01-entry.md
INFO to-verify-count: .scratch/e02-c01-entry.md: 10 mark(s) on 9 line(s)
INFO scan: files=1 marks=10 mark-lines=9 findings=0 blocked=0
exit=0
# calibration table rows between '## 12.' and '## 13.' (header row excluded): 11
# C01 couples: 14 distinct repo-relative corpus/knowledge/*.md paths; unresolved []
# C02 vs C01 topic lines: 775 chars / sha256 a42926b1d0fe5ac5…  vs  1054 chars / sha256 aed27f526727bef2…

# staged gate (C02 header 23 lines + M01 example 27 lines = 51), first-pass evidence
$ python3 -B tools/gates/provenance-audit.py .scratch/e02-staged-entry.md
INFO to-verify-count: .scratch/e02-staged-entry.md: 12 mark(s) on 2 line(s)
INFO scan: files=1 marks=12 mark-lines=2 findings=0 blocked=0
exit=0

# sample anchor re-reads — all matched; verbatim examples above
$ sed -n '27p;71p;102p' corpus/knowledge/myth-symbol/cosmology-cosmography.md
$ sed -n '5p' corpus/knowledge/myth-symbol/sacred-topography-pilgrimage.md
$ sed -n '51p' corpus/knowledge/myth-symbol/direction-symbolism.md
$ sed -n '95p' corpus/knowledge/culture-material/architecture-settlement-lexicon.md
$ sed -n '54p;65p' corpus/knowledge/culture-material/craft-artisan-lexicon.md
$ grep -n 'archive of coups' corpus/knowledge/linguistics/naming-systems.md
70:- **Critical toponymy** … Every renaming is datable; a map is an archive of coups.
$ sed -n '35,39p' corpus/knowledge/verification/calibration-registry.md   # R/C/B/H/T definitions (R :35 … T :39)
$ sed -n '78p' corpus/knowledge/culture-material/writing-media-surface-economy.md
- **The two-way error to avoid**: … Cheapness widens the *base*, it does not redistribute the *authority*.
```

**Write surface:** this file only — `reports/round-48/cov/E02-register.md`. The only other writes were two disposable staging extractions under `.scratch/` for the gate runs (`e02-staged-entry.md`, `e02-c01-entry.md`; scratch, never under `corpus/`). No `corpus/**`, `tools/**`, `README`, `LOG.md`, `reports/round-1..47/**`, `tools/gates/frozen/**` or fleet `.ufo/**` byte was edited or staged. No git commit/push, no install, no network. No `reports/round-*/run-validation.py` was executed; no re-freeze; no packet-surface change.
