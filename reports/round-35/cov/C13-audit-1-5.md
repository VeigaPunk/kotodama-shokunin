- Seat: C13 | verifier | claim C | date 2026-10-19 | baseline 4a7aede

# C13 — audit of entry drafts 1–5 against C12's runbook (claim C / coverage)

- Round 35 (regimen 2, loop 1, build 3 of 3), seat **C13**, role **verifier**, claim **C**.
  Mission (verbatim, `reports/round-35/targets.json` → `seats[id=C13].mission`): *"Audit entries
  1-5 against C12's runbook: every check with observed result; defects severity-ranked."*
  Out path: `reports/round-35/cov/C13-audit-1-5.md`.
- Lane root `/home/vgpnk/Projects/shokunin/kotodama-shokunin`; `git rev-parse HEAD` →
  `4a7aede22cd8395b01ce6dd9f46bcae364ca24e4`; `git status --porcelain` → `?? reports/round-35/`
  (no corpus byte moved during this audit).
- **Canon: NON-CANON.** This seat audits bytes and reports; it admits no entry, certifies no round,
  promotes nothing, and is not promotion verification. A green reading below is a structural reading
  of the bytes at a named digest — never a verdict on the scholarship, never canon.
- **Writes**: this file only, plus gitignored scratch under `.scratch/c13/`. No `corpus/**`, no
  `tools/**`, no filed round-1..34 byte, no `.ufo/**`. No commit, no push, no network.
- **F-C13-1**: no `reports/round-*/run-validation.py` was executed anywhere, in-tree or in a copy.
  The runner for this round does not exist yet (`ls reports/round-35/run-validation.py` → rc=2).

## 0. Verdict at a glance

| # | reading | class |
|---|---|---|
| 1 | **4 of the 5 assigned targets exist** (C01, C02, C03, C05); `cov/C04-entry-4.md` is absent | measured |
| 2 | all four staged drafts **PASS** the runbook's structural contract on **two independent instruments**; 2 of 4 are additionally `clean` | measured |
| 3 | **322 `path:line` citations** across the four drafts resolve: 0 unresolvable, 0 out-of-range, 0 ambiguous; 22 needle checks confirm cited lines say what the drafts claim | measured |
| 4 | **every quoted absence sweep reproduces**: C01 7/7, C02 19/19, C03 7/7, C05 14/15 | measured |
| 5 | **one current defect** (C05's census vector reports an occurrence count inside a file-count vector, S2) and **one superseded defect** (C05's dangling pointer, repaired by the author mid-audit) | findings F1, F2 |
| 6 | **five review-tier hits are false positives**, adjudicated against the bytes (F4–F7, F8/F9) | findings |
| 7 | **four defects in C12's runbook instrument** (stager fence limit, pointer-leg coverage, pin-leg false positive, locator undercount) — the runbook's own recipe cannot audit 3 of these 4 drafts | findings F11–F14 |
| 8 | **three false-greens in this seat's own instruments were found and fixed by their controls** (§5) | measured |
| 9 | the four fragments **moved during the audit** (C01 twice); every number below is pinned to the §1 digests | measured |

## 1. The audited bytes, and the churn

Audited snapshot stamp **2026-10-19T08:30:14Z**; entry bytes extracted from each fragment's fenced
block by this seat's fence-run parser (`.scratch/c13/audit-c13.py`, 11/11 controls) and staged under
`.scratch/c13/final/stage/`; digests recorded in `.scratch/c13/final/pins.json`.

| seat | fragment | fragment sha256[:16] | staged entry | entry sha256[:16] | entry bytes |
|---|---|---|---|---|---|
| C01 | `cov/C01-entry-1.md` | `4e4c355e6c2e1f3d` | `culture-material/mortuary-material-culture.md` | `88fc8f4459bc9651` | 87 880 |
| C02 | `cov/C02-entry-2.md` | `6746faf32a2f28ad` | `culture-material/agrarian-field-system-lexicon.md` | `23564220aa3befa4` | 37 792 |
| C03 | `cov/C03-entry-3.md` | `82af002e2253ee2f` | `culture-material/writing-media-and-surface-economy.md` | `f039e6e120ed050f` | 46 482 |
| C05 | `cov/C05-entry-5.md` | `d6f930b272fa50a1` | `culture-material/furniture-interior-lexicon.md` | `eaa48a8988d27466` | 39 981 |
| C04 | — | — | — | **absent** | — |

**Churn, stated rather than hidden.** These drafts are live: at this seat's first staging (08:24Z)
the four fragments hashed `40e29858…` (C01), `ff50245f…` (C02), `b5511031…` (C03), `ff75110d…` (C05);
by the final snapshot all four had moved (C01 twice: `40e29858…` → `4e4c355e…`, entry 86 097 →
87 880 bytes). Two findings observed on the earlier revisions were **repaired by the authors before
this audit was filed** and are reported as dated observations, not current defects (F2, and the
`cleared` review hit on C02). A re-run is required if the fragments move again before integration —
`python3 -B .scratch/c13/audit-c13.py --selftest && python3 -B .scratch/c13/audit-c13.py <staged
entries>` reproduces §2 in one command (§4 recipe).

## 2. Every check, with its observed result

Two instruments were run on the same staged bytes, and their readings are reported separately rather
than merged (`verification/two-reader-interop-agreement.md`: agreement is a consistency result, not
correctness).

- **I-C12** = the runbook's own instrument, installed from `cov/C12-audit-runbook.md` §5 by
  `awk '/^```python$/{f=1;next} /^```$/{f=0} f'` → sha256
  **`973610275404e9e3183d46e33e5352562265e6c2e397c92291e63c401ed7562d`**, 663 lines — byte-identical
  to the digest the runbook declares (`cov/C12-audit-runbook.md:99,184`); `--selftest` → **exit 0**,
  "3 positive controls … and 4 negative controls … behave".
- **I-C13** = this seat's independent instrument (`.scratch/c13/audit-c13.py`), 11/11 planted
  controls, plus `check-anchors.py` (citation resolver) and hand re-runs of every quoted sweep.

Per runbook check family (`cov/C12-audit-runbook.md:33-44`), observed on the §1 bytes:

| family | reading | C01 | C02 | C03 | C05 |
|---|---|---|---|---|---|
| 1a | `R35-4F-1` frontmatter 4/4 (source\|sources, verified-at, recheck, couples\|scope) | **pass** | **pass** | **pass** | **pass** |
| 1b | `R35-5F-1` round-10 field set 5/5 | **pass** | **pass** | **pass** | **pass** |
| 1c | no empty scalar field; `verified-at` ISO-dated | pass / ISO | pass / ISO | pass / ISO | pass / ISO |
| 2 | repo-path pointers resolve | 9/9 resolved (I-C12); 32 paths, 0 unresolved (I-C13) | 1/1; 11 paths, 0 unresolved | 11/11; 11 paths, 0 unresolved | 5/5; 21 paths, 0 unresolved |
| 2b | digest pins compared / stale candidates | 1 / 1 (**false positive**, F6) | 0 / 0 | 0 / 0 | 0 / 0 |
| 3 | decision record present | **pass** (`## 10. Decision record`, DR-MMC-01..09) | **pass** (DR-AG-01..10) | **pass** (DR-1..9) | **pass** |
| 4 | gap statement present | **pass** (`- gap filled:`) | **pass** (`- gap:`) | **pass** (`- gap filled:`) | **pass** (`- gap:`) |
| 5a | bleed strict candidates | 1 (**false positive**, F4) | 0 | 0 | 0 |
| 5b | ownership-assertion candidates | 0 | 0 | 0 | 0 |
| 5c | unnegated `canon` mentions | 1 (**false positive**, F5) | 0 | 2 (**false positives**, F7) | 0 |
| 6 | canon boundary named | **pass** | **pass** | **pass** | **pass** |
| — | I-C12 verdict | `PASS/review` | `PASS/clean` | `PASS/review` | `PASS/clean` |
| — | I-C13 findings | 0 structural | 0 structural | 0 structural | 1 (F3, reading note) |

**Independent legs this seat ran, beyond both instruments** (each a command over bytes, not a
re-reading of the draft's own self-audit):

| leg | command shape | result |
|---|---|---|
| citation resolution | `python3 -B .scratch/c13/check-anchors.py <staged>` (attached `path.md:13,:33` **and** detached `` `path.md` `:47,149` `` forms; bare names resolved in the six partitions then in `reports/round-35/{scout,cov,plan}`) | **322 resolved, 0 unresolvable, 0 out-of-range, 0 ambiguous** (C01 176, C02 59, C03 32, C05 55) |
| needle checks | `sed -n "<line>p" <file>` vs the claim the draft attaches to it, 22 sampled citations | **22/22 match** (e.g. `material-culture-inference-method.md:81` grave-résumé; `ritual-liminality.md:61` substitution arc; `writing-systems.md:117` clay/bamboo/stone media bias; `architecture-settlement-lexicon.md:49` "not furniture"; `trade-economy-lexicon.md:87` bench→bank) |
| C01 sweeps | the 7 commands quoted in its `- gap filled:` line, re-run verbatim | **7/7 reproduce**: `ls corpus/knowledge/*/ \| grep -iE 'death\|mortu\|funer\|burial\|grave\|mourn\|tomb'` → no match, exit 1; the three `grep -rliE` sweeps → 0/0/0; `grep -rli 'mortuary' corpus/knowledge/ \| wc -l` → 13; `grep -rliE 'burial\|grave\|tomb\|funerar' corpus/knowledge/culture-material/ \| wc -l` → 13 |
| C02 census | the 19-term loop quoted in its gap line, re-run verbatim | **19/19 reproduce**: three-field 0, open field 0, chinampa 0, qanat 1, shaduf 0, noria 0, acequia 1, fallow 3, granary 3, Geoponica 0, Columella 0, mouldboard 0, carucate 0, virgate 0, tribulum 0, flail 0, swidden 1, paddy 2, Hesiod 8 |
| C03 sweeps | the 7 commands quoted in its gap line, re-run verbatim (BRE for the `\\\|` alternation, as quoted) | **7/7 reproduce**: papyrus-family over culture-material → 4; `inscription surface`, `surface econom`, `medium econom`, `wax tablet`, `ostraka` → 0 each; `papyrus` over the whole corpus → 11 |
| C05 census | the 15-keyword loop quoted in its gap line, re-run verbatim | **14/15 reproduce exactly** (furniture 5, chair 3, stool 0, bench 2, seat 3, throne 2, cushion 2, mattress 0, bedstead 0, canopy 0, screen 2, cabinet 1, chest 8, desk 0); the `table` row is **F1** |
| duplicate-slug check | each draft's proposed target path vs the 201 live corpus filenames | 0 collisions; no draft duplicates an existing entry's filename or topic head |

## 3. Findings, severity-ranked

Severity follows the runbook's own tiering (`cov/C12-audit-runbook.md:28-29`): **S1** = blocker
(fails the structural contract), **S2** = major/precision, **S3** = review-tier observation.

| # | sev | finding | evidence | owner |
|---|---|---|---|---|
| **F1** | **S2** | **C05's census vector mislabels an occurrence count as a file count.** The quoted command is a file-count loop, but the reported vector prints `table 108 occurrences` where that command yields **18**. | `grep -ril "table" corpus/knowledge/culture-material/*.md \| wc -l` → **18**; `grep -o -i "table" corpus/knowledge/culture-material/*.md \| wc -l` → **108**. The number is true under a *different, unquoted* definition, and the entry's own word "occurrences" says so — but a reader re-running the quoted loop reads 18. Fix is one cell: quote the occurrence command beside the number, or write 18. | C05 / integrator |
| **F2** | **S2 (superseded)** | **C05 carried a literal dangling pointer** `corpus/knowledge/era-periodization-models.md` (partition segment missing; the file lives at `culture-material/`). Observed at entry sha `9dddc9d1fb1a3175` (staging 08:24Z), where I-C12 read `FAIL … [blocker] unresolved-pointer:corpus/knowledge/era-periodization-models.md`; **repaired in the current revision** (`eaa48a8988d27466`: I-C12 now reads `ptr=5/5`, I-C13 reads 0 unresolved). Filed as the dated observation it is; no current defect. | the two readings above, on two digests | C05 (done) |
| **F3** | **S3** | **C05 carries no singular `- source:` field** — the only one of the four. The binding reading `R35-4F-1` accepts `- sources:` (`cov/C12-audit-runbook.md:34,53-63`), so this is **not** a contract failure; the strict fleet reading (reading A, `verification/header-conformance-readings.md`) is 3/4. The fragment does not record the deviation either way. | I-C13 `strict=2/3` on C05; `grep -c '^- source:'` → C01 1, C02 1, C03 1, **C05 0**; deviation note absent from `cov/C05-entry-5.md` | C05 / integrator |
| **F4** | **S3 (FP)** | C01's `bleed-candidate: closed as` is a **substring match inside "A closed assemblage dates and connects"** (`:168`) — the sentence is about seriation, not a clearance. | the flagged line, read in full | I-C12 false positive |
| **F5** | **S3 (FP)** | C01's unnegated `canon` mention is the phrase **"canon hygiene"** — the name of `corpus/QUALITY.md` item 5, quoted inside a sources bullet. | `sed -n '13p'` contains "canon hygiene" | I-C12 false positive |
| **F6** | **S3 (FP)** | C01's `stale-pin-candidate: reports/round-35/targets.json` compares the **git commit id** `4a7aede22cd8395b01ce6dd9f46bcae364ca24e4` (same line, `:40`) against that file's sha256. The pin leg compares any 8–64-hex token on a pointer line. | I-C12 JSON: `pin=4a7aede22cd…`, `file_sha256=56ad03927c70…`, `historical_pin_heuristic=False` | I-C12 false positive |
| **F7** | **S3 (FP)** | C03's two unnegated `canon` mentions are **in-world text-canon senses**: "a perishable-medium culture has an active canon (what gets recopied)" (`:144`) and "the canonizing culture" (`:175`). Neither asserts a lane canon. | the two flagged lines | I-C12 false positive (polysemy the runbook itself anticipates, `:41,60`) |
| **F8** | **S3 (FP)** | I-C13 flags **4 source bullets on C01 as carrying no locator**: Cicero *De Legibus* 2.58–2.59, and the Zoroastrian / Tibetan *bya gtor* / Hindu complexes. Adjudication: the Cicero bullet is a **standard-edition locator** (work + section), which `corpus/QUALITY.md:5-7` accepts as a checkable source; the three complexes are **explicitly marked `to-verify` inline** with the instruction to open the named work, which is exactly the escape hatch `QUALITY.md:7-8` provides. None is a fabricated source. The count is a regex lower bound, not a defect count — the same limitation applies to I-C12's `src=22/32`. | the four bullets, read in full; `corpus/QUALITY.md:5-8` | I-C13 / I-C12 false positive |
| **F9** | **S3 (FP)** | I-C13's canon-assertion hit on C01 is the verb **"clears"** in DR-MMC-05 ("unproven until it clears the inference ladder"). | the flagged row | I-C13 false positive |
| **F10** | **S2 (process)** | **The audited fragments moved under the audit** (C01 twice), so any number quoted without its digest is a reading of a superseded revision. §1 pins every number; the repair of F2 and the disappearance of C02's earlier `cleared` review hit are both artefacts of that churn. | §1 table vs the 08:24Z digests | integrator (re-run before quoting) |

## 4. Interop findings against C12's runbook instrument (F11–F14)

The runbook is a good contract; its *instrument* has four coverage holes, all measured on the §1
bytes. They are filed here because the same instrument is the round's named audit tool (C14, C17,
the integrator and `run-validation.py`'s C-leg all lean on it), and because a green from a leg that
cannot see the surface is not a reading of that surface.

| # | sev | finding | evidence |
|---|---|---|---|
| **F11** | **S2** | **The stager cannot read a four-backtick fence.** Run per the runbook's own §4 step 2 (`cp reports/round-35/cov/C0*-entry-*.md .scratch/c12/drafts/` then `--fragments … --stage …`), I-C12 exits **2** with `no corpus target path or no fenced block` on **C01, C03 and C05** — the three drafts (and C08) that open their entry with ` ````markdown `, which is the correct fence when the entry body itself contains ``` code blocks. Its block regex is `^```(?:markdown\|md)\s*$([\s\S]*?)^```\s*$` (`cov/C12-audit-runbook.md:766`). C02 stages fine (37 793 bytes vs this seat's 37 792 — a one-byte leading-newline convention difference). | `python3 -B .scratch/c13/c12-instrument.py --fragments .scratch/c13/drafts --stage .scratch/c13/stage-c12` → rc=2, three CANNOT-EVALUATE lines; fence-run census: C01 `[4,4]`, C03 `[4,4]`, C05 `[4,4,3,3]`, C02 `[3,3,3,3,3,3]` |
| **F12** | **S2** | **The pointer leg reads only bare-path tokens, not `path:line` citations.** Its `REPO_PATH_RE` requires the token to end at the closing backtick, so the corpus's dominant citation form (`` `…/file.md:117,:149` ``) is invisible. Measured coverage on these four drafts: **26 pointers compared against 322 `path:line` citations** (C01 9/176, C02 1/59, C03 11/32, C05 5/55). C02's earlier `ptr=0/0 PASS` was a **vacuous green** — the leg compared nothing while the draft carried 59 citations (all of which this seat resolved, 0 unresolved). | I-C12 `pointers_resolved` lists per entry vs `check-anchors.py` counts |
| **F13** | **S3** | **The pin leg treats any 8–64-hex token on a pointer line as that pointer's digest** → a git commit id reads as a stale pin (F6). | I-C12 JSON `digest_pins_stale_candidates` |
| **F14** | **S3** | **`LOCATOR_RE` counts standard-edition locators as "no locator"** (`\b(19\|20)\d{2}\b` or a backticked path or a 16–64-hex digest), so C01's `src=22/32` and the `source-entries-without-locator` major are lower bounds: three of the ten "unlocated" bullets are standard-edition citations (F8). | I-C12 `source_entries_with_locator` vs the bullet text |

**What is *not* an interop finding.** Where both instruments grade the same surface they **agree on
every graded value**: frontmatter 4/4 and 5/5, no empty field, ISO `verified-at`, gap present,
decision record present, canon boundary named, zero unresolved pointers on the final revision. The
divergences above are coverage differences (a leg that sees fewer tokens), not contradictory verdicts.

## 5. Defects in this seat's own instruments (found by their controls, fixed)

Recorded because a verifier's instrument is evidence and its false-greens are findings too
(`corpus/knowledge/verification/verification-independence-anti-circularity.md`'s discipline; round 28's `X63-H1/H2` is
the precedent).

1. **The sweep leg could not fail on the `\| wc -l` form.** A planted sweep claiming `0` while the
   live tree holds 2 went **green** — the recogniser required the count to follow the closing backtick
   immediately. Fixed (backticks/space tolerated before the arrow); the control now fires. This is
   the same defect class round 28 filed as `X63-H2`, which is why the leg has a planted control.
2. **The fence extractor silently truncated four-backtick drafts.** The first version matched
   ``` fences greedily, so on C02's original four-backtick block it captured **9 831 of 36 987 bytes**
   and stopped at the first inner fence — an audit of 27 % of an entry that would have been reported
   as complete. Replaced with a fence-run parser (open with N backticks closes at ≥ N with no info
   string); a `nested_fence` control now asserts the tail marker survives.
3. **The citation resolver was blind to the detached `path` + `:lines` form** (`` `writing-systems.md`
   `:47,149` ``), reporting **0 citations for C03** while the draft carries 32. Extended; C03 reads
   32 resolved, 0 unresolved. (Same blindness affects I-C12's pointer leg — F12.)

## 6. Coverage limits of this audit, stated rather than hidden

- **Entry 4 is not audited.** `cov/C04-entry-4.md` does not exist (`ls reports/round-35/cov/` at the
  snapshot). Claim C's threshold is *"10/10 new entries audited clean (two independent auditors)"*;
  this fragment can therefore certify at most 4 of the 5 entries assigned to C13, and **the round's
  threshold cannot be met while C04 is missing** (see `## Owed`).
- **No external source was fetched** (no network in this wave, `reports/round-35/targets.json`
  `shared_rules[3]`). Every external citation in the four drafts is a dated reference carrying
  author + year + publisher, and each URL-bearing or chapter-level item is flagged `to-verify` in
  the entry. This audit can verify that the *flag is present and honest*; it cannot verify the
  external work. `to-verify` counts are therefore **not** defects, and the entries' frames are
  correctly stated to rest on their in-corpus halves.
- **The sweep leg is manual.** Neither this seat's instrument nor I-C12 parses the
  `for k in …; do grep …; done` loop form these drafts quote, so §2's sweep rows are this seat's
  hand re-runs of the exact quoted commands, not a tool's output.
- **A passing structural audit is not an admission.** Nothing here judges whether the topics are
  worth their slots (P01's plan is still absent — see `## Owed`), whether the gap claims are the
  right gaps, whether the scholarship is sound, or whether the entries should be promoted.
- **This is not the second independent auditor.** Claim C's threshold names two independent
  auditors; C14 audits entries 6–10 and C17 re-audits a sample by lot. Overlap with those seats is
  for the integrator to reconcile.
- **Paths this fragment names but that do not resolve, on purpose**: `corpus/knowledge/era-periodization-models.md`
  (quoted as the *defect text* in F2 — it is the dangling pointer, and the file actually lives at
  `corpus/knowledge/culture-material/era-periodization-models.md`), `reports/round-35/run-validation.py`
  and `reports/round-35/cov/C04-entry-4.md` (declared absent in `## Owed`), and the four
  `culture-material/<slug>.md` rows of §1, which are **staged copies under
  `.scratch/c13/final/stage/`**, not corpus paths. A self-check of this fragment's own 31 cited repo
  paths found exactly one genuine error (a misnamed anti-circularity entry), corrected before filing;
  the rest of the non-resolving set is the declared-absent class above.

## 7. Addendum (appended 2026-10-19T08:36Z) — C04 audited, entries 1–5 now 5/5

**This section is an append, not a rewrite**: §§0–6 above read "C04 absent" and were true at the
08:30:14Z snapshot. `cov/C04-entry-4.md` landed after that snapshot and is audited here. Nothing
above is edited.

| field | value |
|---|---|
| fragment | `reports/round-35/cov/C04-entry-4.md`, sha256[:16] `6d5e7832ae253e9a` |
| staged entry | `culture-material/timekeeping-instruments.md` (intended path), sha256[:16] `9805c0b854334ed3`, 40 234 bytes |
| fence | 3-backtick open/close (this draft does **not** use the four-backtick form) |
| I-C12 | `PASS/review` — 4of4 True, 5f True, `src=1/1`, `ptr=25/25`, gap True, dec True, `bleed=0/4`, 2 canon mentions (`canon`, `canonical`) |
| I-C13 | 0 structural findings; 28 repo paths, **0 unresolved**; canon boundary present |
| citations | 17 `path:line` citations resolved, **0 unresolvable / 0 out-of-range / 0 ambiguous** |
| needles | 5/5 (`celestial-symbolism-calendars.md:83` decans; `numerals-and-measures.md:135` sexagesimal base; `aksum-ethiopia.md:98` hour labels; `architecture-settlement-lexicon.md:90` minaret/beacon; `calendar-festival-systems.md` "three clocks") |
| sweeps | the quoted instrument-term loop re-run verbatim: **every quoted term returns 0 files** (26 terms in the command; the draft's `- verified-at:` line calls them "28 instrument terms" — the sweep reproduces, the term count is off by two, S3) |
| near-miss counts | re-run and confirmed: astrolabe 2, "star clock" 2, chronometer 2, obelisk 1, meridian 1, "time zone" 1, bell 81, `clock` in culture-material 6 |
| one count needs its flag named | the draft reports `hour` **8** files. That is the **word-boundary** count (`grep -rilw -- "hour" corpus/knowledge/*/*.md \| wc -l` → **8**); the plain-substring count is **12** and the culture-material-only count is 4. The number is reproducible under `-w`, which the entry does not quote — same class as F1, smaller blast radius, S3 |

**Adjudications on C04's review-tier hits (both false positives):** the unnegated `canon` mentions
are `canonical hour` (the divine office — an institution the entry is *about*) and the phrase
`canon decisions belong to lore-shokunin`; neither asserts a lane canon. No bleed candidate survived
reading: `bleed=0/4` means four negated mentions, all ordinary boundary prose.

**The claim's frontmatter readings, updated:** C04 carries a literal `- scope:` field
(`- scope: reference knowledge and craft method for the culture-material partition only …`), the
**only** draft of the five to do so — so C04 satisfies even the literal 4/4 reading the claim's
shorthand implies (`reports/round-35/claims.json:29`), while the other four satisfy the substituted
reading `R35-4F-1`. F3 (C05 lacking `- source:`) is therefore the only frontmatter-reading note in
the set.

**Revised verdict for the assignment.** All **5 of 5** C13-assigned drafts now exist and all five
pass the structural contract on both instruments (I-C12: 3 `PASS/review`, 2 `PASS/clean`; I-C13:
0 structural findings apart from the F3 reading note). The §§0/§1/§6 statements about C04 are
superseded by this addendum and the `## Owed` item naming C04 is discharged; the round's 10/10
threshold leg remains C14's and C17's to complete — this seat certifies entries 1–5.

**Churn note (final, 08:38Z).** At the close of this audit `C01-entry-1.md` had moved again
(`4e4c355e…` → `3164d10dce12e7ff`); C02/C03/C04/C05 still match the §1/§7 pins. Every C01 number in
§2–§3 therefore describes revision `4e4c355e…` (entry `88fc8f4459bc9651`), not the newest bytes —
which is exactly the re-run item this fragment already owes, and the reason the integrator must
re-derive §2 on the frozen revision before quoting any number as current.

## Owed

- **`reports/round-35/cov/C04-entry-4.md` — absent at this seat's snapshot.** Entry 4 of the 5
  assigned to C13 is unaudited; without it the claim's *"10/10 new entries audited clean"*
  threshold cannot be reached, and the culture-material count cannot reach 24 (6 drafts: C01, C02,
  C03, C05, C06 present, C04 missing). The integrator must either obtain C04's bytes or record the
  shortfall against claim C.
- **A re-run of this audit on the frozen revision.** The four audited fragments moved during the
  audit (F10); if they move again before integration, §2's numbers must be re-derived on the
  integrated bytes. Recipe: `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1; python3 -B
  .scratch/c13/audit-c13.py --selftest; python3 -B .scratch/c13/c12-instrument.py --selftest;
  python3 -B .scratch/c13/audit-c13.py <staged entries>; python3 -B
  .scratch/c13/check-anchors.py <staged entries>` (the two instruments' bytes are installed from
  `cov/C12-audit-runbook.md` §5 and this fragment's scratch paths; both are stdlib-only and
  read-only apart from staging).
- **The four interop findings (F11–F14) need an owner's decision**, not this seat's repair: the
  runbook's instrument is C12's artifact and the round's named audit tool. The minimal fix is the
  fence-run parser (F11) plus widening `REPO_PATH_RE` to accept `:line` suffixes (F12); without F11
  the runbook's own §4 step 2 cannot audit 4 of the 10 drafts.
- **`reports/round-35/plan/P01-c-plan.md`** — still absent; all four authors chose their topics
  under the missing-dependency rule and flagged the topic authority as owed. Nothing in this audit
  depends on P01, but the slug/topic reconciliation does.
- **`reports/round-35/run-validation.py`** — absent (`ls` → rc=2); claim C's third counting command
  has no runner yet, and per `shared_rules[4]` it may only ever be executed from an isolated
  `git archive` copy.
- **Discharge note (§7, appended 08:36Z):** the C04 item at the head of this list is **discharged** —
  `cov/C04-entry-4.md` landed and is audited in §7; the bullet above is preserved as the record of
  the 08:30:14Z state, per the lane's rule that a correction is a new row or section, never an
  in-place rewrite. The re-run, interop-owner, P01 and `run-validation.py` items remain open.

## Citations

- `reports/round-35/targets.json:5-13` (shared rules; `:8` drafts are integrator-applied, `:10`
  F-C13-1 absolute, `:12` missing dependency), `:149-153` (seat C13 id/role/claim/mission/out).
- `reports/round-35/claims.json:8-10` (baseline `4a7aede22cd8395b01ce6dd9f46bcae364ca24e4`),
  `:21-35` (claim C: `:24` claim text, `:29` after_required incl. "frontmatter 4/4 or documented
  3/4 class", `:31-33` counting commands, `:35` thresholds "10/10 new entries audited clean (two
  independent auditors)").
- `reports/round-35/cov/C12-audit-runbook.md:26-49` (check families 1a–6 with tiers), `:51-63`
  (`R35-4F-1` vs literal `- scope:`; 0 of 201 live entries carry `- scope:`), `:84-128` (the §4
  recipe and its exit codes), `:182-187` (instrument bytes, sha256
  `973610275404e9e3183d46e33e5352562265e6c2e397c92291e63c401ed7562d`, 663 lines), `:766` (the
  stager's fenced-block regex — F11).
- Audited drafts (final snapshot, §1 digests): `reports/round-35/cov/C01-entry-1.md`,
  `C02-entry-2.md`, `C03-entry-3.md`, `C05-entry-5.md`; staged copies under
  `.scratch/c13/final/stage/`; pins in `.scratch/c13/final/pins.json`.
- `corpus/QUALITY.md:3-21` (the five-item admission bar; `:5-8` provenance and the `(to-verify)`
  escape hatch — F8; `:18-20` canon hygiene — F5).
- `corpus/knowledge/verification/header-conformance-readings.md` (the three readings of the header
  trio; the reason F3 is a reading note, not a contract failure).
- `reports/round-10/run-validation.py:81` (`C_FRONTMATTER_FIELDS = ("topic","sources","verified-at",
  "recheck","couples")` — the runbook's `R35-5F-1`).
- `reports/round-28/audit/x63-entry-source-resolvability.md` (the `X63-H1/H2` precedent for filing
  false-greens found by an instrument's own controls; §5 above).
- Commands run (2026-10-19, lane root, `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`,
  outputs quoted in §§1–5): `git rev-parse HEAD`; `git status --porcelain`;
  `awk '/^```python$/{f=1;next} /^```$/{f=0} f' reports/round-35/cov/C12-audit-runbook.md >
  .scratch/c13/c12-instrument.py` + `sha256sum` + `wc -l`; `python3 -B
  .scratch/c13/c12-instrument.py --selftest`; `python3 -B .scratch/c13/audit-c13.py --selftest`
  (11/11); `python3 -B .scratch/c13/c12-instrument.py .scratch/c13/final/stage/*/*.md`;
  `python3 -B .scratch/c13/audit-c13.py .scratch/c13/final/stage/*/*.md`; `python3 -B
  .scratch/c13/check-anchors.py .scratch/c13/final/stage/*/*.md`; the seven C01 sweep commands; the
  nineteen-term C02 census loop; the seven C03 sweep commands; the fifteen-keyword C05 loop plus
  `grep -ril "table" corpus/knowledge/culture-material/*.md | wc -l` → 18 and `grep -o -i "table"
  corpus/knowledge/culture-material/*.md | wc -l` → 108; `sed -n "<line>p"` on 22 cited lines;
  `python3 -B .scratch/c13/c12-instrument.py --fragments .scratch/c13/drafts --stage
  .scratch/c13/stage-c12` → rc=2 on C01/C03/C05.
- Not run, deliberately: any `reports/round-*/run-validation.py` (F-C13-1); any freeze mode of
  `tools/exercise-handoff-e2e.py` (claim O, pinned bytes); no network call of any kind.
