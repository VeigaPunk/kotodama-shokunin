# ConnectorFrontier — kotodama round 76, wave 1 (cross-source pattern finder)

Seat: ConnectorFrontier (leaf; no delegation, no background jobs, no scratch used, no installs).
Lane: /home/vgpnk/Projects/shokunin/kotodama-shokunin. Base: 98c486bdb4650ba5b8e651d332910e8ee60ad121.
Read-only throughout. Nothing written to the fleet repo, sibling lanes, git state, or the shokuknow merge package.

## Verdict (3 lines)

1. Frontier: the calendar/era theme advances exactly one frontier pointer (Round 65 partial scope for `calendar-festival-systems.md`, README:737). The new ground sits in core culture-material. Four candidate sentences/passages stray into adjacent territory (source-access method, Barthes/narrative codes, lane-process history, archival/library classification). Details §1.3.
2. Sibling overlap on lunisolar/era terms: none in any sibling `corpus/knowledge/`. Contested scope exists only at the in-world-dating boundary (lore-shokunin) and the citation-metadata grammar (chousa). Reported, not absorbed. §2.
3. Gate sample: admit = `era-periodization-models.amend-2026-10-23b.md` (row S908 / S935, one document); reject = `calendar-festival-systems.amend-2026-10-23c.md` (row S916, sole tier-C support, body says "in the standard's own words"). §3.

## 0. Inputs read and reading notes

- `corpus/README.md` has **no `## Frontier` heading**. The frontier section is `## Known gaps (frontier)` at README:608 (`sed -n '608,640p'`). The draft's "frontier step" therefore has no literal row table to cite; the calendar pointer is a prose bullet (README:737, §1.1).
- `PROVINCE.md` (31 lines) has no frontier rows. Its boundaries: refuses canon (→ lore-shokunin), game mechanics (→ game-dev-2d/3d), general source-research method (→ chousa), web publishing (→ kake), prompt craft (→ kotoba). Contested scope → report to integrator.
- `.ufo/waves/round-76/CLAIMS-DRAFT.md` (66 lines): Claim C with four candidates a–d; Claim Ca; frontier step. Not edited.
- Staged candidate files read in full from `/home/vgpnk/Projects/shokuknow/merge/kotodama/knowledge/corpus/knowledge/culture-material/` (read-only): `calendar-festival-systems.amend-2026-10-23c.md` (30 lines, = d), `calendar-festival-systems.amend-2026-10-24.md` (98 lines, = a, includes a superseded round-7 passage), `calendar-festival-systems.amend-2026-10-24-r10.md` (43 lines, = b), `era-periodization-models.amend-2026-10-23b.md` (25 lines, = c).
- Merge package `MERGE-REPORT.md`, `SOURCES.append.md` (rows S908, S916, S919, S921, S932, S935, S937, S938 read in full).

## 1. Frontier: rows advanced, core vs adjacent, strays

### 1.1 Frontier rows the theme advances

Command: `grep -n -iE 'calendar|era|GB|lunar|chin|japan|nengo|archiv|frontier' corpus/README.md` restricted to 608–831.

- README:737 — `Round 65 adds games-play-sport-contests.md ... Partial scopes remain in ... culture-material/calendar-festival-systems.md` — **the one frontier pointer this theme advances** (partial → scoped for the standard-clause and era-table sub-area).
- README:646 — `scoped material/era reconciliation` (round-5/6 era reconciliation; mention only, not a row the claim names). — `sed -n '608,640p'` line 39 → file line 646.
- No frontier pointer names `era-periodization-models.md` as partial. [negative claim, sweep: the `Known gaps` section 608–831 grep above; "era" matches only at 646]

Verdict: the staged work advances the 737 pointer. It does not close it: `calendar-festival-systems.md` §12 canon boundary and the clause text (GB/T 33661-2017 normative wording) stay unread by the lane's own admitted rows (S938 says so; see §1.3 item 3).

### 1.2 Core vs adjacent-sibling territory

- **Core (culture-material):** GB/T 33661-2017 identity/promulgation rules (S937, S932, S938, S916 as reproduction), and the National Archives era-name table (S908/S935) as a *dating instrument* — these are real-world calendar compilation and era-name facts, the core of `culture-material/` (`calendar-festival-systems.md` §1–§10; `era-periodization-models.md` §3, §11). Core.
- **Adjacent, not core:**
  - lore-shokunin: world-bible canon, in-world dating. Candidate sentences that recommend a fictional calendar/era design are method (allowed); none names a canon polity or in-world date. Checked: `grep -niE 'canon|bible|lore|in-world|fictional' <a,b,c,d>` → only "fictional calendar modelled on this standard" (c, §N+1) and "a culture adopting an era-name system" (b, §N+2). Both are method, inside the entry's stated scope ("decides no culture's calendar"). Not stray.
  - game-dev (calendars-as-mechanics): `grep -niE 'mechanic|gameplay|timer|cooldown|quest|player|UI'` over the four candidates → **zero hits**. Game-dev corpus/knowledge has zero `calendar` hits (sweep: `grep -rnie calendar game-dev-2d-shokunin/corpus/knowledge game-dev-3d-shokunin/corpus/knowledge` → no output).
  - chousa (general research method): see §1.3 items 1–3.

### 1.3 Candidate sentences that stray (file + sentence)

1. **a — `calendar-festival-systems.amend-2026-10-24.md`, §N "What the lane may and may not claim from the standard"** (superseded passage, lines ~73–80): "*it exists to keep the lane's own standing rule visible*"; and lines ~87–89: "*the authoritative copy is behind a script-driven reader that serves no standard text to a non-browser client, and the alternate host fails TLS verification. Until that reader is driven with a real browser or a licensed copy is consulted, every statement ... must be declared as such.*" — **source-access and claim-discipline method** (chousa's surface and the lane's verification partition; PROVINCE: the verification partition "do[es] not expand ownership into general research method"). Not calendar content. Recommend: strip from the admitted knowledge text, keep the one-line fact (clause text not reached) in the row's own `scope` column.
2. **a — same file, §N+1 "The contrast that keeps the standard honest"** (lines ~92–95): "*from S919 and S921: where a rule-making text is legible in the publisher's own copy ... the 1966 article's three named levels*". S919 = Marrone (lane S892); S921 = Barthes (lane S885). Both rows are about narrative-structure codes, and the passage's own text says "*Neither is a source about GB/T 33661-2017*". **Adjacent-sibling / out-of-theme** (myth-symbol/narrative-structure-frameworks, which already holds these rows). Strip from the calendar file. Note the merge report's `used-by` correction (S919, S921 now listed as used by both narrative and calendar entries) — the same stray in the registry.
3. **b — `calendar-festival-systems.amend-2026-10-24-r10.md`, §N+1** (lines ~33–36): "*any future attempt should stop at the browser, not at another URL*" — an **instruction about access procedure**, not a fact about the calendar. Chousa/verification method. Recommend keeping the measured fact ("24148 bytes each, md5 9791d9dc0f17384eeab4ff4791eed437", both routes) and dropping the instruction sentence.
4. **c — `era-periodization-models.amend-2026-10-23b.md`, §N+1** (line ~23): "*the library's classification ladder; the museum's exhibition periods; the heritage filing ladder*" — library/museum/heritage classification is **adjacent** (heritage-taxonomy-models.md, a separate kotodama file; and library classification is general archival method, chousa's `archives-verified-r9`/`archived-export-intake` territory). Borderline; the era-table point itself is core. Recommend trimming to the era-name sequence only.
5. **Lane-process leakage (all four files; not a sibling stray but must not land in knowledge text):**
   - a: line 8 `recheck: 180d — re-run the three row recheck commands in round 9's SOURCES-PROPOSED.md` and line 9 `ground: round 8's CANNOT-ANSWER §2`; line 16 `Round 9 adds`; line 62 `round 7's SOURCES-PROPOSED.md`. Verified: `ls SOURCES-PROPOSED.md` in the lane → `No such file or directory`; the merge package holds only MERGE-REPORT.{md,json}, SOURCES.append.md, amendments/, knowledge/ (`ls /home/vgpnk/Projects/shokuknow/merge/kotodama/`). So the `recheck` pointers reference a file that does not exist in the lane or package. **Defect: unresolvable pointer.**
   - b: `ground: round 9's CANNOT-ANSWER §2`, `round 10's SOURCES-PROPOSED.md`: same defect.
   - c: `round 5's SOURCES-PROPOSED.md` — same defect.
   - d: `round 6's SOURCES-PROPOSED.md`; `ground: round 5's CANNOT-ANSWER §2` — same defect.
   - Sweep: `grep -n "SOURCES-PROPOSED" calendar-festival-systems.amend-2026-10-23c.md calendar-festival-systems.amend-2026-10-24.md calendar-festival-systems.amend-2026-10-24-r10.md era-periodization-models.amend-2026-10-23b.md` (all four files, staged). Each `recheck:` line names it.
6. **Citation ids — kill-rule relevant (not a sentence stray):** the staged bodies cite campaign ids S908, S916, S919, S921, S932, S935, S937, S938. `comm -12 <(sort staged-ids) <(sort reg-ids) | wc -l` → `35` (only S859–S893 collide; `tail -2 reg-ids` → `S892`, `S893`). The eight cited campaign ids are therefore not lane ids and must be re-pointed by document (draft plan: S894–S898 new, S892/S885 existing). Verified existing lane rows: `grep -m1 '^| S885 |'` → Barthes, Persee; `grep -m1 '^| S892 |'` → Marrone. Planned S894–S898 are unused in `reg-ids` (`grep -cx` → 0 each). Confirmed the draft's "campaign S919 → lane S892, campaign S921 → lane S885" mapping against the held rows.

## 2. Sibling overlap on lunisolar calendar / 农历 / Japanese era names (contested scope, reported not absorbed)

Command 1 (sibling knowledge only):
`grep -rlE 'GB/T 33661|nengō|元号|农历|lunisolar' /home/vgpnk/Projects/shokunin/*-shokunin/corpus/knowledge` → matches **only** inside `/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/knowledge/`: `culture-material/era-periodization-models.md`, `culture-material/calendar-festival-systems.md`, `synthesis/era-language-staging.md`, `civilizations/china-tang.md`, `civilizations/japan-edo.md`, `civilizations/japan-heian.md`. The `ls` of the sibling `corpus/knowledge` dirs printed listings for audio, chousa and others; **no sibling knowledge file carries these terms**.

Command 2 (sibling lanes, all non-knowledge trees, including the fleet `.ufo/waves`): the broad pattern (`era name|nengō|元号|农历|GB/T 33661|lunisolar`) matched:
- `lore-shokunin/corpus/SOURCES.md:58` and `lore-shokunin/.ufo/waves/round-103/rejected/r103-in-world-dating-and-uncertain-time.md` (matched the word "era name" in a grep recipe) — **in-world dating** (OWL-Time, EDTF, competing in-world calendars). Adjacent: lore's CM-c coverage row. Lore owns canon; kotodama's §12/§14 canon boundary already hands off. **Contested scope**: an in-world era/calendar encoding (lore) vs real-world era-name tables (kotodama). No text overlap in the candidates. Reported.
- `game-dev-2d-shokunin/reports/round-86/r86-scout.md:385` ("3.x-era names") — false positive.
- `kotoba-shokunin/.ufo/waves/round-47/...`, `kagi-shokunin/.ufo/waves/round-28/...`, `kaidoku-shokunin/.ufo/waves/arc2-loop1-round10/E25.md` — false positives ("era" in other senses).
- `.ufo/waves/kaika-w1/kotodama-art.md:221` — fleet-root art dossier (outside any lane) that couples to `era-periodization-models.md`, `calendar-festival-systems.md`, `linguistics/naming-systems.md`. Read-only; no action.
- chousa: `chousa-shokunin/corpus/knowledge/recheck-due-r26.md`, `metadata-screen-r25.md` use "calendar-valid" as the **recheck-date grammar**. The candidates' `verified-at:` / `recheck: 180d` / `tier A/B/C` header lines use that grammar. Contested only at the metadata surface; chousa owns the method. Reported, not absorbed.

Sibling-lane `corpus/knowledge` for "calendar" (`grep -rnie calendar game-dev-2d-shokunin/corpus/knowledge game-dev-3d-shokunin/corpus/knowledge lore-shokunin/corpus/knowledge`) → lore: `r91-c9-watch.md:211` only (the word "clarification" inside a sentence — false positive); no calendar knowledge in game-dev.

Negative claim sweep: no sibling lane holds a knowledge entry on the Chinese lunisolar calendar, 农历, GB/T 33661 or Japanese nengō. Sweep = Command 1 above.

## 3. Gate sample (≥1 admit, ≥1 reject from the assimilation set)

Assimilation set = the 132 staged rows (`staged-ids`, S859–S990, `wc -l` → 132) in the four candidate files plus the other staged files.

**Recommended ADMIT sample: candidate c — `era-periodization-models.amend-2026-10-23b.md`, row S908 (= S935, same National Archives page).**
- Why a non-author is most likely to dispute it: the row's body claims a span ("令和 2019 … 文治 1185 and onward to the earliest names") that the quoted evidence cannot show as a complete table, and "and onward to the earliest names" is not a checkable quote. Also S908 and S935 are one document under two campaign ids; the draft's plan counts it once (S894). Admission therefore tests two things the Gate must test: the quote-in-window check and the one-document-one-row rule.
- Clean single-row file (no bundled stray passage); its only off-theme sentence is §1.3 item 4 (borderline, trimmable).
- [INFERENCE — not run] I did not open the S908 evidence window; whether the quoted span sits in a committed window is for the closure to check. I did not run the Gate or any census.

**Recommended REJECT sample: candidate d — `calendar-festival-systems.amend-2026-10-23c.md`, row S916.**
- Why a non-author is most likely to disagree with it as written: (i) S916 is the **only tier-C row** in the set and is the **sole support** of the file, which the draft's kill rule forbids ("no tier-C row is the sole support of an admitted entry"); (ii) the body says "*from S916: rule (4) in the standard's own words*" while the row itself says "*a reproduction, not the publisher's copy*"; (iii) the lane's own admitted sibling rows contradict the body: S938 (candidate b) states the authoritative route serves no clause text to a plain client, and candidate a states "every statement about the standard's rules rests on a third-party reproduction … and must be declared as such". Candidate d declares the tier in its header, but its body does not carry the declaration. Those two candidate files cannot both be read as admissible without rewording d's body.
- A reject of d does not reject the S938/S937 standard facts, only the clause-text claim. This is a real test with a real defect, not a manufactured one.

Honourable mention (second reject, if the closure wants two): candidate a's superseded passage (§1.3 items 1–2), which is out of theme and cites narrative-structure rows. Recommend the L1 trim, not reject, the file.

## 4. Summary of checks (command → number)

- Frontier heading present? `grep -n '^## Frontier' corpus/README.md` → none; `grep -n 'Known gaps (frontier)'` → `608`.
- Calendar frontier pointer → `README:737` (via `sed -n '736,740p' corpus/README.md`).
- Staged candidate row count → `wc -l staged-ids` → 132.
- Staged ∩ registry → `35` (S859–S893).
- Registry lines → `wc -l reg-ids` → 817; merge report claims "782 rows" (`MERGE-REPORT.md`). **Discrepancy 817 vs 782 — flagged for the L1**; the draft uses 817.
- SOURCES-PROPOSED.md referenced by 4 candidate files, present in lane? → no; in merge package? → no.
- Sibling knowledge overlap → kotodama only (see §2).

## 5. Install / mutation record

- Installs: none. Tools used: grep, sed, comm, wc, ls, cat (all pre-installed).
- Writes: this report only. No scratch directory created. No git commands run. No fixture repos.

## 6. Blockers / unrun

- Unrun: opening S908/S916 evidence windows; running `accept-c.py`/`accept-ca.py`; any Gate or census. Out of this seat's scope.
- Blocker to reporting certainty: the `## Frontier` heading the draft names does not exist (see §0); I mapped to `## Known gaps (frontier)` and the Round 65 bullet. The L1 should confirm that mapping.
