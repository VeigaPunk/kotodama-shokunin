# R03 — cartography entry: content review (non-author), round 48

- Seat: `R03` | role: reviewer | claim: **C** (coverage) | round 48, loop 2, position 2
- Baseline: HEAD `a01405dd36367292255c2652ac0a601f4cd6a0af` (`git rev-parse HEAD`, 2026-10-19) = `reports/round-48/claims.json:7` (`baseline_commit: "a01405d"`)
- Out path: `reports/round-48/review/R03-c-content.md` (this file)
- Non-author statement: I drafted no C fragment and edited no fragment. I wrote only this file. Every judgement is from the fenced bytes, live corpus lines, or a command reproduced in §9.
- Read cut: 2026-10-19T19:52Z. `cov/C01-entry.md` and `cov/C02-header.md` exist; no assembled `corpus/knowledge/culture-material/cartography-and-mapmaking.md` exists.

**One-line judgment.** The r48 draft is a **real domain entry and a decisive right-sizing of r47** — 227 fenced lines (239 assembled with C02's head), 4,545 words, 81 table rows, 14 H2, **0 H3**, and B1–B9 are answered on the bytes rather than asserted. It is **not landing-ready as filed**: §1's five-condition test excludes the star chart and the cosmographic diagram while §2/§4/the `- topic:` line list both among the eight map forms this entry owns — a central-definition contradiction no other filed seat catches — and the landing inherits the two-head/topic seam plus a shelf that does not cover the body's external citations. **Verdict: PASS on depth-per-line; FAIL on landing readiness.** The fix is roughly eight lines and a re-run of the audits on the assembled bytes.

---

## 1. What I reviewed, pinned

| Artifact | Lines | sha256 |
|---|---:|---|
| `cov/C01-entry.md` fenced entry (head + body) | 227 | `2a66774974b80d9be2659a9e0e09a265114631c21189eae506acba5edfbdb3ca` |
| `cov/C01-entry.md` body from `## 1.` | 215 | `771f136566d9c4bb1821de90936a0d8c1e3bce4f88b09939cb9c0d025578792f` |
| `cov/C02-header.md` fenced head | 23 | `4692a3347faf8efbdfcd8b3b362d6812ca7c7a1abc439ca644b6d13dc1feea38` |
| Assembly shape I reviewed: C02 head + blank + C01 body | 239 | `3538bb3efdab2d13ad13f7f41fb2fd271cc6f52da73e61495e1bc8c6a5381be1` |

The C01 fragment file itself was revised during the review window (`a075a9da…` → `4c2815a7…`), but the fence I judge is stable at `2a66774…` before and after. Counts are mine: 4,545 words, 81 table lines, 14 H2, 0 H3, 6 parenthetical `(to-verify)` marks (10 `to-verify` tokens including the shelf preamble and recheck prose), 177 nonblank lines.

**Live base re-measured:** `find corpus/knowledge -name '*.md' | wc -l` → **223**; `ls corpus/knowledge/culture-material/*.md | wc -l` → **25**; `python3 -B reports/round-28/readme/sweep.py` → `rows 223 files 223`, exit 0. Cartography remains unowned: `find … -iname '*cartograph*' -o -iname '*mapmaking*' -o -iname '*portolan*' -o -iname '*cadastr*' | wc -l` → **0**; slug absent.

---

## 2. Is it a real entry? — depth verdict (PASS)

### 2.1 What each section actually does

| Entry § | What it does | Representative evidence (fragment lines) | Verdict |
|---|---|---|---|
| §1 | Master claim + four load-bearing choices + a five-condition test with diagnostic failures | `C01-entry.md:84-99` | real method; one contradiction (D1) |
| §2 | One-owner boundary; answers the `cosmology-cosmography.md:27` competing sentence; 12-row division-of-labour table | `:101-118` | real; B8 closed |
| §3 | Seven-link survey→symbol chain, weakest-link rule, recomputed error budget, field book vs fair copy | `:120-137` | real and arithmetic-clean |
| §4 | Eight forms with question, exemplar, **what each structurally cannot show**, and eight minimum builds | `:139-165` | real; B9 closed |
| §5 | Projection table (preserves/distorts), scale as three numbers, orientation as a decision, the blank as a class | `:167-180` | real; tables carry decision content |
| §6 | Six media, copy economics, workshop roles/organisation/products/customers in one bullet each, cost and prestige rules | `:182-196` | real, heavily compressed from r47 |
| §7 | Five-link warrant chain, authority ladder, five provenance failures, contest rule, performative-map split | `:198-212` | real; P2-1 closed |
| §8 | Six silence classes and the legal-instrument argument | `:214-219` | real |
| §9 | Nine build steps, each naming its artifact | `:221-233` | real; sequences rather than re-describes |
| §10 | Six decision rows with trigger and failure | `:235-244` | real |
| §11 | One lagoon, two sheets, one storm; one update rule stated once | `:246-269` | real; one P2 geometry issue |
| §12 | Eleven calibration rows with R/C/B/H/T statuses, living-practice flag, precision trap | `:271-288` | real |
| §13–14 | Recheck triggers and scope | `:290-296` | real |

No section is an essay. The longest prose blocks are the five condition definitions and the chain bullets; every section ends in a rule, lever, table or decision row, matching `corpus/QUALITY.md:16-17`.

### 2.2 Depth per line, measured against r47 and the partition

| Metric | r47 body (R03 r47 §1) | r48 fenced entry | Live culture-material (25 files) |
|---|---:|---:|---:|
| Lines | 739 | 227 | median 149, max 221, mean 150.2 |
| Words | 17,601 | 4,545 | — |
| Table rows | 240 | 81 | table rows/line median **0.312** |
| Table rows per line | 0.325 | **0.357** | 0.312 |
| H2 / H3 | 15 / 44 | **14 / 0** | H2 median 11 |
| `(to-verify)` marks | 29 | 6 parenthetical (10 tokens) | — |

The r48 entry is **30% of r47's length, 26% of its words and 34% of its table rows**, yet it keeps every load-bearing block: register test, boundary, chain, eight forms, projection/scale, media/trade, warrant, silences, build order, decision record, example, bank. It has **higher table density than r47 and than the partition median**, and it removes r47's 44-H3 fragmentation entirely. That is better depth-per-line, not r47's bloat renamed.

**Discrete decision surfaces counted:** 5 conditions + 7 chain links + 8 forms + 8 minimum builds + 5 projection rows + 6 media rows + 5 warrant links + 6 silence classes + 9 build steps + 6 decision rows + 11 calibration rows = **76**, in 227 lines. r47 carried the same method in 739. This is the measured answer to the over-build class.

### 2.3 What was cut, and why it was right to cut it

- The 13-row word-fossil bank (r47 §9, 55 lines, the highest `(to-verify)` density): gone. Its single most useful survivor — the claim that map words are a loan-stratum archive — is not load-bearing for this entry's method.
- The standalone 12-row decision record (r47 §13): compressed to six rows in §10.
- The six-role/six-organisation/four-product/three-customer trade prose (r47 §6–§7, 129 lines): compressed to four bullets in §6.
- The duplicated mechanism bullets (`C01:164` vs `C02:109`; `C01:204` vs `C02:110` in r47) and the projection/scale restatement in r47 §10: absent; §9 sequences what §5 describes.
- 44 H3 subsections → 0. This is the structural signature of the over-build, and it is gone.

**Depth verdict: PASS.** This is a real cartography method entry, not filler and not a renamed r47.

---

## 3. Blocking findings

### D1 (blocking, content) — the register test contradicts the form typology

The entry's central definition and its central typology disagree on the same two objects.

- `C01-entry.md:93`: condition 1, "**Referent index** — the object asserts positions or relations in a **ground space someone could traverse**."
- `C01-entry.md:99`: "a **T-O diagram** has convention but no ground index (a cosmogram …); … a **star chart** indexes the sky, not the ground (**another register's sheet**)."
- `C01-entry.md:110`: the boundary row says this entry owns "**the star chart as a map form**".
- `C01-entry.md:149-150`: §4's "eight map forms" table lists `celestial/star chart` and `cosmographic/world diagram` as two of the eight, with questions and "cannot show" columns.
- `C01-entry.md:73` (the `- topic:` line) and `:141` ("One polity can make a cadastral sheet and a **cosmogram** in the same century") repeat the ownership claim.

A reader applying the test to §4's own table gets the opposite answer from §4. The same ambiguity hits the itinerary row: `:99` fails "an itinerary" for having "no area", while `:145` admits `itinerary/strip` as a form. r47 avoided the star-chart case with "the test is ground-indexed, not earth-indexed" (`reports/round-47/cov/C01-entry-a.md:132`); the right-sized rewrite dropped that clause and re-created the problem in a sharper form.

**Fix (3 lines, no section change):** make condition 1 "a **referent space** under a declared correspondence — terrestrial or celestial; the space need not be traversable"; drop the star-chart failure clause (it passes under the corrected condition) and change "an itinerary" to "an itinerary **list**" (the strip map is the form that passes). For the cosmogram, keep the form row but state in §2 or §4 that it is admitted as a **boundary form** whose correspondence is doctrinal, not measured — which is exactly what the "cannot show: survey; it is symbolic" cell already says. Do not delete the forms: the `- topic:` line and the README row promise all eight.

I checked the sibling evidence for this: C04 (citations), C17 (structure), C12 (content — written before C01 landed), E02 (register fit), M03 (method — still auditing r47 bytes) and R01/R02 do not flag it. It is the one substantive coherence defect still open.

### D2 (blocking, assembly) — two heads, three topics, and a red sweep

Confirmed independently; R02 §9.2 and C04 §8.4 reach the same conclusion, and C17 §7 recommends the same assembly.

| Source | `- topic:` value chars | sha256 (first 16) | Matches seed? |
|---|---:|---|---|
| r44 seed (`K02-gap-scout.md`, the `text` block line) | 766 | `bc7274f411cc6977` | — |
| `C02-header.md:114` | 766 | `bc7274f411cc6977` | **yes** |
| `C10-readme.md:132` (and `:210`) | 766 | `bc7274f411cc6977` | **yes** |
| `C01-entry.md:73` (head included in its fence) | **1,045** | `23d94f4122d6ab88` | **no** |

C01's own fence says the two heads "must agree byte-for-byte on `- topic:`" (`C01-entry.md:67`); they do not. Landing C01's head with C10's row produces `topic_mismatch 1` (R02 staged it and measured exactly that). C01's head is also non-conforming on the field set: **7 fields, no `- source:`, `gap filled` before `topic`** (`:70-80`), against the house order `topic, gap filled, sources, source, couples, verified-at, recheck, scope` (`corpus/knowledge/culture-material/timekeeping-instruments.md:3-10`) and C02's 8 fields.

**Fix:** strip C01's head, apply C02's 23-line head verbatim, and start the body at `## 1.`. That is the 239-line assembly I pinned in §1, not 227 and not 250. Do not merge fields, and do not use the C13 scribe's third topic text.

### D3 (P1, provenance — blocks apply) — the landing head's shelf does not cover the body's citations

If the D2 fix is applied, the landed shelf is C02's ten-item list (`C02-header.md:129`). The body cites four external works that are **not on that shelf**: Mundy 1996 (`C01-entry.md:278`), al-Idrisi (`:280`), Needham (`:280`), Russell 1991 (`:276`). C02's `- source:` line then says "the external frameworks are **the shelf above**" (`C02-header.md:131`) — false for those four. C01's own shelf (`:76`) covers Mundy, al-Idrisi and Russell but **still omits Needham**, so switching heads does not close it either.

**Fix (one grouped shelf line):** "Mundy (1996); Needham (1959) vol. 3; al-Idrisi (1154); Russell (1991, carried in-corpus at `cosmology-cosmography.md:102`) — `(to-verify)`". Then the `- source:` claim is true. This is the same gap C12-F3 filed against M02; it survives assembly because the body, not M02, is what lands.

---

## 4. B1–B9 regression audit on the r48 bytes

Every r47 defect was re-tested against the filed fence, not against the author's audit.

| ID | r47 failure | r48 bytes | My independent check | Verdict |
|---|---|---|---|---|
| **B1** | 0.2 mm at 1:50,000 called "ten times" a 200 m closure | `:135`: "a 200 m closure … 10 m … a **20× overstatement**" | `0.2×50000/1000 = 10.0`; `200/10 = 20.0` | **closed** |
| **B2** | "2 files / 3 lines"; `:71` counted as a `cartograph` hit | `:72`: "**2 lines in 2 files**"; `:71` named as the `survey map` disclaimer without the token | `grep -rni 'cartograph' corpus/knowledge/` → 2 lines (`cosmology:102`, `mesoamerica:58`); `grep -ci cartograph` on `:71` → 0 | **closed** |
| **B3** | false accusation that "archive of coups" is not in the file | `:216` quotes "Every renaming is datable; a map is an archive of coups" and `:6`/`:75` say it is not corrected | `grep -n 'archive of coups' naming-systems.md` → `70:` contains it verbatim; "archive of renamings" exists only in r47 fragments | **closed** |
| **B4** | ladder cited at `craft-artisan-lexicon.md:44` | `:115` cites `:54-65`; `:75` explicitly says `:44` is the steel-grading row | `sed -n '44p'` → Steel (Japan) row; `:54` header, `:56-63` systems, `:65` design rule | **closed** |
| **B5** | typology cross-refs to "§1–3" / "§2" | four `§` refs only: `:79` (§12, §13), `:288` (§3, §5) | §3 = chain; §5 = projection; §12 = bank; §13 = recheck — all resolve | **closed**, with P3-1 (§12 "arithmetic" is a pointer, not the arithmetic) |
| **B6** | provenance/charter called §9 | `:198` is `## 7. Provenance and charter`; no `§9` reference anywhere in the fence | heading map read | **closed** |
| **B7** | three incompatible update rules | `:260` states the rule once; `:261` applies it; `:265` is an explicitly labelled counterfactual; `grep 're-survey'` → only `:260`, `:261`, `:265`, plus the audit prose | one rule, consistent storm outcome | **closed** |
| **B8** | "owns no made map" overstated against `cosmography:27` | `:103` quotes `:27` ("how the world is drawn, named, walked and built") and assigns it to cosmography; the 12-row table repeats the split | `sed -n '27p'` live matches the quoted clause | **closed** |
| **B9** | minimum build covered 5 of 8 forms | `:143-152` has 8 form rows; `:156-163` has 8 minimum-build bullets and says "the eight forms above, not a sample" | counted 8 and 8 | **closed** |

r47's should-fix list: **P2-1** closed by `:279` (metaphysics/procedure split); **P2-2** moot (no "six anchors" claim); **P2-3** moot (duplicates cut); **P2-5** moot (the stick chart is not used at all — a legitimate cut); **P2-7** answered in the body's 12 rows, though C02's couples field still omits two of them (P3-5).

**No B1–B9 recurrence.** The remaining work is new-seam and coherence, not inherited defect.

---

## 5. Should-fix and note findings

| ID | Severity | Finding | Evidence | Fix |
|---|---|---|---|---|
| P2-1 | P2 | §6's "Preparation" column restates the writing-media entry's owned preparation chains (skin/scraping, beating/sizing, sizing/painting) | `C01-entry.md:184-190`; the boundary row at `:112` says writing-media owns the surface families and cost ladder; `writing-media-surface-economy.md:3`, `:48` | cite `:48` and cut the column's process detail, or relabel it "map-specific consequence" |
| P2-2 | P2 | Exemplar dates are not inline-marked; the column header scopes `(to-verify)` to "edition" only, yet `:145-152` assert "late 13th c.", "c. 700 CE", "c. 1300", "1869", "1854", "16th c." | `:143-152`; QUALITY clause 1 (`corpus/QUALITY.md:5-8`) | change the header to "(`to-verify` for edition and date)" — one token, no line |
| P2-3 | P2 | "south at top (Chinese)" is a broad historical generalisation with no citation | `:179` | mark `(to-verify)` or cite a shelf item |
| P2-4 | P2 | "portolan … makes no projection claim" is stated as settled while the entry's own bank codes portolan accuracy **C** | `:148` vs `:277` | soften to "its construction is contested; it makes no *stated* projection claim" |
| P2-5 | P2 | The worked example's extent and scale imply a **4 m-wide** cloth master: 20 km at 1:5,000 = 4.0 m | `:255` ("the delta is about 20 km across"), `:254` (1:5,000), `:258` (one cloth master) | state that the cadastral register is multi-sheet, or reduce the delta extent |
| P2-6 | P2 | §11 demonstrates all six `DR-CM` decisions but tags none; r47's C14 F-2 class (example names no decision row) returns in weak form | `:246-269`; `grep -c 'DR-CM'` on §11 → **0** | add parenthetical `(DR-CM-0n)` tags to the nine bullets and the consequence sentence; no new lines |
| P2-7 | P2 | The boundary table's "live anchor" column has three rows with no anchor: celestial, trade-economy, sacred-kingship | `:110`, `:116`, `:118` | add `celestial-symbolism-calendars.md:3`, `trade-economy-lexicon.md:92,:121`, `sacred-kingship-mythic-charter.md:70` (C02 already verified these) |
| P2-8 | P2 | No "composition register, not a sixth symbolic register" clause; the word "register" can read as an eighth symbolic register claim | `C01-entry.md:82,90`; r47 had the clause at `C01-entry-a.md:105`; E02-1 | add one sentence to §1 or §2 citing `symbolism-synthesis-method.md:23` |
| P3-1 | P3 | Head `- recheck:` says "re-run §12's arithmetic"; §12 is the calibration bank, the arithmetic is §3/§5 (which §12 itself says) | `:79`, `:288` | say "§3/§5's arithmetic and §13's recheck list" |
| P3-2 | P3 | Flat-earth row attaches "symbolic, not survey maps" to `cosmology:102`; that wording is live only at `:71` (`:102` says "not cartographic claims") | `:276`; C04-W1 | cite `:71,:102` |
| P3-3 | P3 | Rarity row cites `writing-media:73-78`; `:73` is rung 3, the ladder is `:67-75`, the authority rule `:78` | `:281`; C04-W2 | cite `:67-78` |
| P3-4 | P3 | C01's length note says 227 is "+6 over the 221 max"; that uses its own 11-line head. With C02's 23-line head the entry is **239**, +18 over max (still ≤250) | `C01-entry.md:313`; §1 pin | state the assembled number in the landing wire |
| P3-5 | P3 | C02's `- couples:` omits `celestial-symbolism-calendars.md` and `sacred-kingship-mythic-charter.md`, both of which the body's boundary table owns | `C02-header.md:130`; `C01-entry.md:110,118`; C09 P2 | add two tokens if C02's head lands |
| P3-6 | P3 | C14's PASS certifies M01's 27-line Tamber example, not C01's 25-line Vessa example; the two are different artifacts and only one can land | `C14-example.md:6`; `C01-entry.md:246-269` | state which example lands; if C01's, C14's N-1..N-3 do not transfer and its one-rule leg was independently verified here |

---

## 6. QUALITY.md clause verdicts (r48 bytes)

| Clause | Verdict | Basis |
|---|---|---|
| Provenance (`corpus/QUALITY.md:5-8`) | **PASS-with-fixes** | In-corpus anchors resolve (I re-read 20+); external shelf honestly unread and marked; but D3 (shelf/body mismatch), P2-2 (dates), P2-3 (Chinese south-up), P3-2/P3-3 (anchor precision) must be fixed. |
| Calibration (`:9-12`) | **PASS** | 11 rows with live R/C/B/H/T codes (`calibration-registry.md:35-39`, verified); living-practice flag; precision trap; P2-1 conflict resolved. |
| Coupling (`:13-15`) | **PASS-with-P2** | C01's field has 14 root-relative tokens, all resolve; C02's has 19 relative tokens, all resolve; whichever lands must include the two body-owned neighbours (P3-5). |
| Usability (`:16-17`) | **PASS** | 81 table rows, 76 decision surfaces, 9 build steps, 6 decision rows, a worked example; no essay padding. |
| Canon hygiene (`:18-20`) | **PASS** | §11 declares NON-CANON and invented; §14 and the head scope decide no world; no promotion/clearance verbs. |

---

## 7. Axis verdict and landing recommendation

**Coverage: +1 genuine, conditional on the fixes.** The gap is real and fresh (0 filename owners, 0 topic owners, slug absent at `a01405d`); the demand is stated honestly as low; the entry adds method the 223 do not have (projection/scale as claims, the seven-link chain, the form's structural silences, reproduction economics, the performative map). It does not inflate demand and does not restate the neighbours' owned registers.

**Calibration/operability: no harm.** No tool, gate, queue or README byte is touched by the entry; the README rev 2.5 belongs to C10/Ca.

**Usability: harmed only by D1.** The contradiction is a reader-facing defect in the entry's own method; the P2s are local.

**Landing recommendation: do not apply as filed.** Apply in this order:

1. **Fix D1** (`:93`, `:99`, plus one boundary sentence) so the test and the eight forms agree.
2. **Assemble C02's head + C01's body from `## 1.`** (239 lines). Strip C01's head. Normalize the `- topic:` to the 766-char seed/C02/C10 text.
3. **Fix D3** (one grouped shelf line) and **C04-W1/W2** (`:276`, `:281`).
4. Add the two missing couples tokens (P3-5) and the three boundary anchors (P2-7).
5. Decide the example: C01's §11 (25 lines, one rule, no tags) or M01's (27 lines, tagged, C14-certified). Whichever lands, add the `DR-CM` tags (P2-6) and state the choice in W01.
6. Re-run C04 (citations), C14 (example), C17 (structure) and C03 (arithmetic) **on the assembled bytes**, then land and run the staged 224 sweep. The expected green is `rows 224 files 224`, `topic_mismatch 0`, `totals_line 224`, footer `25/26/26/29/24/94`, exit 0.

**What would make me withdraw the coverage verdict:** landing C01's head as-is (the sweep goes `topic_mismatch 1`), or shipping D1 (an entry that says a star chart is "another register's sheet" and also one of its eight map forms).

---

## 8. What I did not verify

- **Every external bibliographic detail.** No network at seat time; every edition, volume and page remains `(to-verify)`. I did not check the shelf against a catalogue.
- **Historical dates** (Carte Pisane, Dunhuang, Hereford, Minard, Snow, Quauhquechollan, Mercator/Ortelius) and the 0.296 m Roman foot. These are conventional inputs the entry routes to recheck; I recomputed the arithmetic that follows from them, not the inputs.
- **The staged 224 sweep and the README rev 2.5 bytes.** C11, R02 and C10 own those; I confirmed only that C10's row text is byte-equal to the seed/C02 topic (`bc7274f4…`, 766 chars) and that C01's is not (`23d94f41…`, 1,045 chars).
- **The final assembled file.** I measured and reviewed the assembly shape (C02 head + C01 body, 239 lines, sha `3538bb3e…`); the integrator's apply could differ by a trailing newline or a field choice. Re-run the checks on the landed bytes.
- **The Ca claim and the O-claim drop.** Other seats; I did not re-run the freshness gate or review the queue successor.
- **r47's fragment bytes beyond the defect sites.** I re-read the nine B-defect lines and the r44 seed, not all four r47 fragments.

---

## 9. Commands and write surface

All commands run from the lane root, 2026-10-19, with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`.

```
$ git rev-parse HEAD
a01405dd36367292255c2652ac0a601f4cd6a0af
$ find corpus/knowledge -name '*.md' | wc -l            # 223
$ ls corpus/knowledge/culture-material/*.md | wc -l      # 25
$ python3 -B reports/round-28/readme/sweep.py            # rows 223 files 223; exit 0
$ grep -rni 'cartograph' corpus/knowledge/               # 2 lines: cosmology:102, mesoamerica:58
$ grep -ci cartograph <(sed -n '71p' corpus/knowledge/myth-symbol/cosmology-cosmography.md)   # 0
$ grep -n 'archive of coups' corpus/knowledge/linguistics/naming-systems.md                   # 70:
$ sed -n '44p;54p;56,63p;65p' corpus/knowledge/culture-material/craft-artisan-lexicon.md      # steel row; ladder
$ sed -n '27p;71p;102p' corpus/knowledge/myth-symbol/cosmology-cosmography.md                 # :27 competing sentence
$ python3 (fence extraction, C01)   # 227 lines; 4,545 words; 81 table rows; 14 H2; 0 H3; sha 2a66774…
$ python3 (assembly)                # C02 head 23 + C01 body 215 = 238; +1 blank = 239; sha 3538bb3e…
$ python3 -c "print(0.2*50000/1000, 200/10, 20000/5000)"   # 10.0 20.0 4.0
$ python3 -c "print(25+26+26+29+24+94)"                   # 224
```

**Write surface:** this file only — `reports/round-48/review/R03-c-content.md`. No `corpus/**`, `tools/**`, `README`, `LOG.md`, `reports/round-1..47/**`, `corpus/lessons/*.md`, `tools/gates/frozen/**` or fleet `.ufo/**` byte was edited or staged. No git commit/push, no install, no network. No `reports/round-*/run-validation.py` was executed. `git status --porcelain` at my write cut showed only the pre-existing untracked `reports/round-46/review/` and `reports/round-48/`.
