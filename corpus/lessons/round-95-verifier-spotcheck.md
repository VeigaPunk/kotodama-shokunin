author: hyaku closure (non-author integrator, @m_zfl)

# kotodama round 95 — non-author verifier spot-check

Integrator of record: hyaku closure session (non-author; did not author round 95). Lane HEAD under review: `feb94bc3353182e9554e41faa4203d8c5707335f` (branch `main`). Base: `19aa4dd03dfd37b435d0b8ea5b313635d9d51592`. Freeze: `d41eb594d27fa71869c0c28d9c2dc051fda40079`. Report: `.ufo/reports/round-95/kotodama.md`, committed in the fleet repo as `fd3fb9fd433ab3862e22141eb7c79b7927657faa` by `kotodama-shokunin <kotodama@shokunin.local>`.

Driver digest (copied from `.ufo/watchdog.log` at closure; the log is mutable):

- `2026-11-05T14:54:20-03:00 launch kotodama round=95 pgid=507845 driver=hyaku-inline attempt=1`
- `2026-11-05T16:47:22-03:00 complete kotodama round=95; hyaku-inline attempt=1`

Method rule: lane gates (selftest, battery, mutation, REG, corpus index, entry grader) were NOT executed. Their committed receipts were verified by bytes and tallies. Plain measurements (sha256, grep, wc, python string counts over committed bytes, curl re-opens of sources) were run here.

## 1. Conformance (step 1)

| check | observed | result |
|---|---|---|
| report author | `git log -- .ufo/reports/round-95/kotodama.md` → `kotodama-shokunin`, fleet commit `fd3fb9fd` | pass |
| SHONEN heading | `grep -c '^## SHONEN' …/kotodama.md` → 1; four box lines, each `[~]` with pointer | pass |
| cited lane commits ancestor of branch | `merge-base --is-ancestor` vs `main`: `19aa4dd0` yes, `d41eb594` yes, `feb94bc3` yes | pass |
| lane pushed, no ahead | `jj-lane.sh state …` → `branch=main local=feb94bc3 remote=feb94bc3 ahead=0 behind=0`; `ls-remote origin refs/heads/main` → `feb94bc3…` | pass |
| uncommitted round work | `git status --porcelain` → `?? reports/round-95/census-head.txt` (4091 B, untracked) | defect (see R2) |
| watchdog digest | both lines present in `.ufo/watchdog.log` as quoted above | pass |
| report contract items | Work performed, Landed changes, Before→after, Sources & frontier, Trend verdicts, SHONEN present | pass |
| stale-lane line | report says "no other mission of this lane is open" with no progressing/silent grade | defect (see R3) |
| L2 role split | seats listed: executor 4, scout 1, scribe 2, connector 1, reviewer 2, critic 2, mutation-tester 1 = 13; no planner seat, though the dispatched prompt §3 names 1× planner | defect (see R4) |
| dispatched prompt | `.ufo/prompts/kotodama-round-95.md` carries §1–§6 incl. frontier step, L2 floor, report contract, commit/push; not diffed byte-for-byte against the canonical template here | partial |

Conformance defects are status-neutral (PROTOCOL §Closure step 1). Lane status: `ok`.

## 2. Claim re-checks

### Claim O — operability (successor move, grader v5 → v6)

Re-measured here (plain):

- O0 tool sha256 over committed bytes: `git show feb94bc3:tools/check-advance-evidence.py | sha256sum` → `f7981ba2881bff2a49a5c603436caefb90f416e6d6843e8e9cd6a63813ac1fec`; base `19aa4dd0` → `7957945db8036f52ab46436b281e92887c6fc22d0a89531d6f80279bcbad01ff`. Matches the claim's before and after. Pass.
- Named refusal classes, `grep -c` over committed tool bytes, base → head: `VERDICT-COMBINE` 0 → 3; `VERDICT-FORMAT` 0 → 3; `VERDICT-TAB` 0 → 2; `ID-NONASCII` 0 → 2; `TOPIC` 16 → 20. The new refusals are present in the shipped bytes.
- Tool size: 1763 lines (base) → 1880 lines (head).

Evidence-verified only (committed receipts, lane gates not run):

- O1 selftest: `controls/selftest-lands-run{1..4}.txt` each end with `SELFTEST PASS 134/134`. Floor 134 met. Base control `126/126` in claim text.
- O2 battery: `controls/battery-lands.txt` → `BATTERY-SUMMARY survivors=0 unnamed=0 refused=14`. Before: `controls/red-before-v5.txt` → `survivors=7 unnamed=0 refused=7`.
- O3 mutation: `controls/mutation-score-lands.txt` → `MUTATION-SCORE: 95/95 killed, 0 survived, 0 broken-pattern`. The committed `mutants95.py` re-hashed here: `ff450980dec9e79b…` matches `instrument-shas.txt`; the independent copy under `MutationTester95/` has the same hash.
- battery95.py re-hashed here: `342237cdcc980d6e…` matches `instrument-shas.txt`.
- O4 REG: `controls/reg-diff-v6-vs-v5.txt` is 0 bytes.

Caveat (disclosed by the lane, not amended): the frozen claim text states the v5 mutation before as `86/88` over the 88-entry set. The measured v5 red-before on the 95-entry set is `87/95` (`controls/mutation-red-before-v5.txt`). The after leg (`killed == total`, `total >= 95`, 0 survived, 0 broken) is met either way. Recorded as a routed note (R6).

Verdict O: **operability improved** (every frozen leg met; O0 and the refusal-class greps re-measured, O1–O4 evidence-verified). Re-measured: O0, refusal-class greps, tool size. Evidence-verified: O1–O4.

### Claim C — coverage (sourced knowledge entry)

Re-measured here (plain):

- Entry `corpus/knowledge/linguistics/funerary-lament-dirge-formulae.md` at HEAD: 50614 bytes (floor 12000); `^## ` headings 12 (floor 6); table data rows 11 (floor 5); frozen phrases in h2 headings or table rows: 6 of 6 (floor 4): `professional keeners`, `antiphonal lament`, `lament refrain`, `praise of the dead`, `gendered mourning rules`, `fictional mourning register`; `- topic:` line present at line 12, matches frozen topic.
- Entry cites S970 (5 times), S971 (8), S972 (5), S973 (6), S974 (5).
- Registry `corpus/SOURCES.md` pipe-row count (`grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'`): base `19aa4dd0` 893 → head 898. Highest id S974.
- Removed lines in the SOURCES diff: 0. Added lines: 7 (8 `^\+` lines minus the `+++` header).
- S970–S974 rows: tier A, status `mined`, opened 2026-11-05, recheck 180d, used-by the entry path. Qualifying rows = 5 (floor 3).
- Census: `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama` → exit 0, last line `kotodama ok`.
- Corpus index (lane gate `tools/check-corpus-index.py`): not run; committed receipt `controls/…` line `LEG C5 PASS index rc=0 last: CORPUS-INDEX: OK files=267 rows=267 findings=0` in `reports/round-95/predispatch-lands.txt`. Evidence-verified.

Quotes re-verified against committed captures (`git show feb94bc3:reports/round-95/evidence/S97x.txt`, python `bytes.count`):

| row | table quote (words) | count in capture | gate quote (words) | count in capture |
|---|---|---|---|---|
| S970 | "the antiphonal way of performing Seto songs" (7) | 1 | 14 words | 1 |
| S971 | "The antiphonal nature of voceru performance" (6) | 1 | 15 words | 1 |
| S972 | "Professional keeners took over." (4) | 1 | 8 words | 1 |
| S973 | "was important in the role of the female professional mourner" (10) | 1 | 12 words | 1 |
| S974 | "ends with a refrain exclamation" (5) | 1 | 11 words | 1 |

All quotes ≤25 words. S970 capture sha256 `dc7394e9…` matches `manifest.json`.

Verdict C: **coverage improved** (every frozen leg met; counts re-measured, index receipt evidence-verified).

### Axes

| axis | verdict | basis |
|---|---|---|
| operability | improved | claim O, §2 |
| coverage | improved | claim C, §2 |
| depth | unchanged | no depth claim; no depth file touched |
| freshness | unchanged | paused by open L0 (round-11, round-89); no freshness claim declared |
| calibration | unchanged | no calibration claim declared |
| adjacency | unchanged | no adjacency claim declared |

No axis harmed. `git diff 19aa4dd0 feb94bc3 -- SCORECARD.md` → 52 insertions, 0 deletions (append-only).

Claim-type note: no claim is exploratory; no `unprovable-but-better` grade is needed.

## 3. Discernment spot-check (LEARNING.md)

Lesson `corpus/lessons/round-95.md` `## Gate`: five admits (S970–S974), 20+ rejected or unreachable candidates with reasons. Re-opened by this closure:

| # | item | decision | re-opened source | agree / disagree | reason |
|---|---|---|---|---|---|
| 1 | S970 (Pärtlas 2025, Seto laments) | admit, tier A | `curl -sL https://sciendo.com/pdf/10.2478/jef-2025-0006` → HTTP 200, 950971 B (matches `manifest.json` `pdf_bytes`); `pdftotext` | agree | quote "antiphonal way of performing Seto songs makes it possible for the lead singer" present in live text |
| 2 | S974 (Mzhavanadze & Scherbaum 2021, Svan zär) | admit, tier A | `curl -sL https://dergipark.org.tr/en/download/article-file/1673889` → HTTP 200, 1156987 B; `pdftotext` | agree | gate quote "recitation, Sima praises the good deeds and grace of the deceased," and table quote "ends with a refrain exclamation" both present once in live text |
| 3 | S973 (Williams & Ó Laoire 2024, Irish keening woman) | admit, tier A | committed capture only (`S973.txt`) | agree on committed bytes; live not re-opened | quote count 1, ≤25 words |
| 4 | Kama 2017 (Estonian runosong burial motifs) | reject, scope | `curl -sL https://www.folklore.ee/folklore/vol68/kama.pdf` → HTTP 200, 8226843 B; `pdftotext` page 1 | agree | abstract: archaeological dating of runosong motifs using burial songs as a dating instrument; not a lament register study |
| 5 | Thrênoi to Moirológia (Oral Tradition 23/2, 2008) | reject, "UNREACHABLE — access: curl exit 28 on PDF, site root and issue page" | `curl -sL https://journal.oraltradition.org/issues/23ii/` → HTTP 200 (43010 B), lists the article; `…/wp-content/uploads/files/articles/23ii/07_23.2.pdf` → HTTP 200, 302080 B; page 1 title "Thrênoi to Moirológia: Female Voices of Solitude, Resistance, and Solidarity", Andrea Fishman; body discusses professional mourners and antiphonal thrênoi | **disagree** | the access reason does not hold on re-open. The article is retrievable and on-point (the lesson itself calls it "the most on-point candidate for the moirologia professional-mourner facet"). No row was admitted from it, so no admitted entry is wrong; the reject reason is wrong and the candidate is unlearned. Routed R1. |

Not re-opened (rule: "could not re-open" grades unprovable, not harmed): MDPI article pages (403), Burgenland Croatian (503), Olonets (404), Pure Corpses (403), doiserbia (timeout), De Gruyter (202, 0 B), Mäetagused and Kalkun 404s, OpenAlex/Crossref non-OA records. Not re-opened, so not graded. The disagreement in row 5 is graded because the source was re-opened.

Discernment result: admits agree (2 of 2 re-opened live, 1 on committed bytes); rejects agree on 1 of 2 re-opened; one access-reason disagreement (row 5) routed as a lesson for round 96.

Newly written SOURCES rows re-opened: S970 and S974 (rows 1, 2 above). Quote length ≤25 words for all five rows (§2 table).

## 4. Trend verdicts (LEARNING.md)

- **expansion: improved.** A new admitted-shape entry on a surface with no prior owner (filename sweep 0 at base), five new tier-A rows with census rc 0. Evidence: §2 claim C, `census` run here, `predispatch-lands.txt` C1–C2.
- **quality: unchanged.** No admitted entry was re-verified, deepened or superseded; the only `corpus/knowledge/` change is the new entry. Evidence: `git diff --stat 19aa4dd0 feb94bc3 -- corpus/knowledge`.
- **discernment: unchanged.** Admits agree with re-opened sources; one reject-reason disagreement (row 5). The disagreement is new to the lane and is routed as a lesson (R1), so the trend is not `harmed`; it is not `improved` because the disagreement is not yet a grounded `QUALITY.md` criterion.

## 5. Routed defects for round 96 (lane must fix)

- **R1 (discernment, reject reason).** Re-open `https://journal.oraltradition.org/wp-content/uploads/files/articles/23ii/07_23.2.pdf` (Thrênoi to Moirológia; HTTP 200, 302080 B on 2026-11-05). Withdraw the access-based reject and decide on content. Add a `QUALITY.md` line if the reject is access-based and the access reason was wrong (lesson must name the criterion).
- **R2 (uncommitted receipt).** `reports/round-95/census-head.txt` is untracked and cited in the report's before→after and Sources & frontier sections. Commit it or cite only committed receipts (`census-end.txt` is committed and carries the same census rows).
- **R3 (stale-lane grade).** The report's stale-lane line must grade every open mission as progressing or silent, per PROTOCOL §Stale-lane actuator.
- **R4 (L2 role split).** The round's L2 minimum names 1× planner; the seat list has no planner. Name the planner seat or record the deviation in the report.
- **R5 (lowest-axis obligation).** Freshness has been the paused lowest axis since at least round 16 (SCORECARD rows). The L0 pause is not the AXES stagnation-nudge waiver; the waiver needs the saturation line and stagnation window recorded in SCORECARD. Route to operator (L0 lines 47 and 303 still unanswered).
- **R6 (before-value).** Frozen claim O before `86/88` vs measured v5 `87/95` on the 95-entry set. Future claims must measure before on the exact set they score.

## 6. SHONEN

No box is ruled fully checkable by non-author closure here. Box 2 (end-to-end task logged) has non-author re-measurement of the claim C entry, but the report's `[~]` stays; promotion is operator-owned.
