# round-94 verifier spot-check — kotodama

author: hyaku closure (non-author integrator, @m_zfl)
round: kotodama lane-round 94 (fleet round 94, attempt 1); closure date 2026-11-05
inputs: report `.ufo/reports/round-94/kotodama.md`; dispatched prompt `.ufo/prompts/kotodama-round-94.md`;
lane base `e7fa8eafb7c5d9edd706f860cfc023e6c99b1ab2` → tip `b715fffc6ca396f2631959ea461a6a50acf74566`;
watchdog digest: `2026-11-05T13:37:49-03:00 launch kotodama round=94 pgid=2727365 driver=hyaku-inline attempt=1` / `2026-11-05T14:41:12-03:00 complete kotodama round=94; hyaku-inline attempt=1` (watchdog.log lines 2882/2895, read at closure).

## 1. Step-1 conformance

- Report attribution: fleet commit `f7d9cb93febea21f6fa097cf1b031eb6618c18a9`, author `kotodama-shokunin <kotodama@shokunin.local>` — the lane identity. PASS.
- `## SHONEN` heading at report line 155 with exactly four `[~]` box lines (4 counted), each with one indented evidence line; no `[x]` written anywhere by the lane. PASS.
- Cited lane commits exist and are ancestors of the branch ref `refs/heads/main` (jj-colocated repo; ancestry tested against the branch ref, not `@{u}`): `d4ff93c8`, `314ad124`, `2aadb4a8`, `5dad8720`, `b715fffc` — all `git merge-base --is-ancestor <hash> refs/heads/main` → OK. PASS.
- Pushed and clean: `scripts/hyaku/jj-lane.sh state` → `branch=main local=b715fffc… remote=b715fffc… ahead=0 behind=0`; `git status --porcelain` → empty. PASS.
- Prompt fidelity: `.ufo/prompts/kotodama-round-94.md` (committed at fleet `5996fb16`) is the canonical round-prompt rendering plus the hyaku addendum §6. It embeds the round-level contract — MISSION/AXES binding (§1), 1–3 falsifiable claims with the lowest-axis rule (§2), the L2 minimum "at least 8 L2 subagents in ONE batched" (§3), commit-then-push ordering, push scope and the L0 side channel (§5) — and all five child-lane items: exact report path and filename (§4), commit-before-report ordering (§4/§5), the SHONEN heading requirement (§4), the commit-hash citation rule (§4 "Landed changes"), and the lane write scope (§5). PASS.
- Dispatch evidence: the watchdog digest above matches the live log lines verbatim; the wave handoff `.ufo/waves/round-94/w1-results.json` records `seats 13` and 13/13 results (ExecBattery94, ExecMutants94, ExecGraderV5, ScoutLullaby94, ConnectorLullaby94, ScribeLullaby94, ScribeLesson94, ExecRegistry94, ExecAdjacency94, ReviewerC94, ReviewerO94, CriticO94, MutationTester94); attack share 4/13 = 31 % ≥ 25 %. PASS.
- Real report, not a marker: work performed, evidence pointers, landed changes tied to LOG entries and commit hashes, before→after measurements, Sources & frontier, trend verdicts, SHONEN assessment — all present. Conformance defects: none found this round.

## 2. Per-claim re-check

### Claim O (operability) — grader v4 → v5 — FAILED AS DECLARED, evidence-verified

Claim O rests on lane-owned instruments (selftest, battery, mutation harness). Per PROTOCOL §Gate standard (Closure consequence) I verified the committed evidence — self-test tally, frozen-run verdicts, revision measured — and did not execute the sibling's gate.

- Revision measured: `controls/instrument-shas.txt` pins `7957945db8036f52ab46436b281e92887c6fc22d0a89531d6f80279bcbad01ff  .ufo/waves/round-94/w1/stage/ExecGraderV5/check-advance-evidence.py`; `sha256sum` over the lands bytes of `tools/check-advance-evidence.py` at `b715fffc` returns the identical digest; the counter's `O0 tool-sha256` line at lands matches. Base tool sha `9799a96c…` confirmed by running the committed rev2 counter over the base tree.
- SELFTEST evidence: `controls/selftest-lands.txt` → `SELFTEST PASS 126/126`; `grep -c '^  ok '` → 126 (floor ≥ 120; v4 base floor named 114). MATCH.
- BATTERY evidence: `controls/battery-lands.txt` → `BATTERY-SUMMARY survivors=0 unnamed=0 refused=7`; per-class lines A1/B1/G1/H1/I1/J1/K1 all `outcome=REFUSED` with named diagnostics (`VERDICT-NONASCII`, `VERDICT-SOFTHYPHEN`, `TOPIC`, `MANIFEST-ROW-TYPE`, `NEWIDS`, `gained_a_NOT-LOCATED_line`, `VERDICT-LOWERCASE`), `traceback=no` throughout. MATCH.
- MUTATION evidence: `reports/round-94/mutation-score-lands.txt` counted directly — 86 ` KILLED ` + 1 ` SURVIVED ` (`head-qualify-off`) + 1 ` BROKEN-PATTERN ` (`dispo-fallback-off`) = 88 total; trailer `MUTATION-SCORE: 86/88 killed, 1 survived, 1 broken-pattern`; the wave copy `.ufo/waves/round-94/w1/stage/MutationTester94/mutation-score.txt` prints the same score. The five routed mutants (`script-strip-off`, `comment-strip-off`, `unescape-off`, `dispo-any-casei`, `baserows-drop-cell8`) are all KILLED. The frozen leg (killed == total, 0 survived, 0 broken-pattern) is therefore **unmet → the claim fails as declared, exactly as the report states**. MATCH (including the failure).
- Regression control: `diff controls/reg-v4.txt controls/reg-v5.txt` → empty (34 REG cases byte-identical to v4). MATCH.
- Red-before receipts: `stage/ExecBattery94/red-before-v4.txt` → `BATTERY-SUMMARY survivors=4 unnamed=3 refused=0` against the pinned v4 sha; `stage/ExecMutants94/red-before-v4.txt` header pins tool sha `9799a96c…`. Stub controls red on all three legs (`stub-selftest.txt` 89/89 < 120; `stub-battery.txt` survivors=7; `stub-mutants.txt` 0/88) — the fixes are shown able to fail.

Re-measured vs evidence-verified: O is **evidence-verified** (gate evidence inspected, gate not executed); C and A are **re-measured** below.

### Claim C (coverage) — improved — re-measured, MATCHES

Commands run by this verifier over `git archive` extractions of both commits:

- `git archive e7fa8eaf… | tar -x -C /tmp/k94-base` and `git archive b715fffc… | tar -x -C /tmp/k94-lands`.
- Entry: absent at base; at lands `wc -c corpus/knowledge/linguistics/lullaby-child-song-formulae.md` → `43409`; `grep -c '^## '` → 11. MATCH (report: 43409 B, 11 `## `).
- Registry: `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` → 888 at base, 893 at lands; highest id `S964` → `S969`. MATCH.
- Append-only: `git diff --numstat e7fa8eaf b715fffc -- corpus/SOURCES.md` → `7 0`. MATCH (5 rows + 2 search-log lines added, 0 removed).
- Counter `python3 -B reports/round-94/predispatch.py --root .` at lands → `C1 entry-present 1`, `C2 registry-rows 893 highest-id S969`, `CENSUS rc=0`, `INDEX rc=0 last-line: CORPUS-INDEX: OK files=266 rows=266 findings=0`; over the base tree the same counter prints `C1 entry-present 0`, `C2 registry-rows 888 highest-id S964`, index `files=265 rows=265`. MATCH.

### Claim A (adjacency) — improved — re-measured, MATCHES

- Counter rev2 over the base tree → `A1 dangling-greeting-pointers 2 :: corpus/knowledge/culture-material/adornment-body-codes.md:5 corpus/knowledge/culture-material/costume-semiotics.md:143` (identical to the frozen receipt).
- Counter rev2 over the lands tree → `A1 dangling-greeting-pointers 0 ::`. MATCH.
- Scope: `git diff --numstat e7fa8eaf b715fffc -- corpus/knowledge/culture-material` → exactly `1 1` on `adornment-body-codes.md` and `1 1` on `costume-semiotics.md`; the diff shows the costume-semiotics greeting pointer re-pointed to `linguistics/greeting-leave-taking-formulae.md`, which resolves at lands. MATCH.

### No axis harmed

`git diff e7fa8eaf b715fffc -- SCORECARD.md` → 56 insertions, 0 deletions: append-only, no owned axis row edited or degraded; spot reads of the appended blocks show verdicts consistent with the receipts. PASS.

## 3. Discernment spot-check (non-author, outside)

Sampled from `corpus/lessons/round-94.md` `## Gate`: 2 admits (S965 live; S969 via committed capture) and 1 reject (Berbel 2026, "opened, not a row").

| item | decision | re-opened source | agree/disagree | reason |
|---|---|---|---|---|
| S965 — TIPA 35 (2019), Geniex-Rabault & Wacalie (kanak berceuses) | admit (tier A, mined) | live `https://journals.openedition.org/tipa/2987` (curl, HTTP 200, 177416 B — byte-count equal to the committed capture) plus committed capture `reports/round-94/evidence/S965.html` | **agree** | the located quote "Les premières berceuses qui sont adressées aux nouveau-nés sont constituées de sons vocaux rythmiques" (14 words) occurs exactly once in the live page and exactly once in the capture; capture sha256 `10a71613…` matches the Gate table; peer-reviewed primary source grounds the entry's vocal-material claim |
| S969 — Okon 2021, Ibibio lullabies (Art and Design Review) | admit (tier A, mined) | committed capture `S969.pdf` + text rendering `S969.txt` (resolvable repo paths) | **agree** | capture sha256 `d7147c8d…` matches the Gate table; quote "the refrain stands out as the leading sound modulator in the song." (12 words) is an exact single-occurrence substring; grounds the refrain/repetition claim |
| Berbel 2026, "Kinderlieder in Translation" — rejected: opened, not a row | reject | live `https://linguistische-treffen.pl/articles/29/03_berbel.pdf` (curl, HTTP 200, 814173 B, application/pdf — byte-count equal to the recorded size), text extracted and grepped | **agree** | re-opened and searched: zero occurrences of nonsense/vocable; the 25 Kinderlied hits are a translation-study corpus of five finger-play songs with nothing locatable about nonsense-syllable refrains, archaic retention in lullaby text, or the lullaby as archive — no anchor for the entry's claims, so the no-row decision is sound |

- Quote discipline: all five new rows' ≤25-word quotes (S965–S969) re-verified as exact single-occurrence substrings of the committed captures (`bytes.count(quote) == 1`, word counts 14/13/12/17/12); all five capture sha256 digests match the Gate table (5/5).
- Registry rows: S965–S969 are tier A, `paper`, status `mined`; the rejected/unreachable candidates (Berbel, Aubinet preview DOI 10.4324/9781003667513, Humanus OJS viewer, UNT dissertation, MDPI 403s) are absent from the registry — the only taylorfrancis hits are pre-existing rows S204/S953 with different DOIs.
- Census: `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama` → exit 0, last line `kotodama ok`; findings are the pre-existing W04 cross-scope duplicates and W01 tierC-mined rows, none on S965–S969; zero E-findings.

## 4. Per-axis verdicts (this table agrees with the MANIFEST closure entry)

| axis | verdict | reason |
|---|---|---|
| operability | **unchanged** | Claim O fails its own frozen predicate (MUTATION leg 86/88 < 88/88: 1 survived, 1 broken-pattern), so the axis-move does not verify as declared and is not scored as a move (fleet precedent: unmet claims grade `unchanged`, e.g. kake r94/r95 closures). The measured instrument gains — routed mutants 0/5 → 5/5 killed, battery 4 survivors/3 unnamed → 0/0 with 7 named refusals, selftest 114 → 126, REG byte-identical — are evidence-verified and recorded above; nothing regressed (no axis harmed). |
| coverage | **improved** | Re-measured: entry absent → landed (43409 B, 11 h2); registry 888 → 893, S964 → S969, 5 new tier-A mined rows; census rc 0; index 265 → 266 rows OK. |
| adjacency | **improved** | Re-measured: A1 2 → 0; exactly two files, one line each; targets resolve. |
| depth | unchanged | No admitted entry deepened or superseded; the knowledge diff names only the new entry and the two adjacency repoints. |
| freshness | unchanged | Paused under open L0 kotodama round-11 and round-89 (standing operator hold, consistent with the r90–r93 closures); no freshness claim declared and none hidden. |
| calibration | unchanged | SCORECARD appends observations only; no calibration claim. |

## 5. Trend verdicts

- **expansion: improved** — re-measured. A dedicated admitted-shape entry on ground with no filename owner at base, citing five new mined tier-A rows on uncovered coverage-map ground; census rc 0; index row present (evidence: §2 Claim C above).
- **quality: unchanged** — re-measured. `git diff --name-only e7fa8eaf b715fffc -- corpus/knowledge` lists exactly the new entry and the two adjacency repoints; no admitted entry re-verified, deepened, or superseded.
- **discernment: improved** — the outside check confirms the author-side verdict: this spot-check agrees with the gate on the sampled admit (S965) **and** the sampled reject (Berbel 2026), which is precisely LEARNING.md's `improved` condition for discernment.

## 6. Routed defects (the lane must fix next round)

- **R95-1 (operability):** the v5 selftest does not pin the ≥2-token heading rule — mutant `head-qualify-off` survives with selftest rc 0 (`mutation-score-lands.txt`). Add a named selftest pin; this is the surviving MUTATION delta blocking 88/88.
- **R95-2 (operability):** `mutants94.py`'s `dispo-fallback` pattern is stale against the v5 bytes (BROKEN-PATTERN, selftest_rc=n/a). Refresh the pattern against v5 or retire the mutant with a reason in the mutation manifest.
- **R95-3 (operability):** CriticO94's seven surviving new counterfeit classes (combining mark, LRM, tab, small-cap id, three heading-numbering variants) — routed to round 95 by the lane; confirmed by closure (`.ufo/waves/round-94/w1/CriticO94.md`).
- **R95-4 (bookkeeping, operator-visible):** the SCORECARD capabilities row "grader v5 counterfeit refusals" landed marked "author-side pending closure". This closure does not admit it (the round is rejected); the row should be re-demonstrated inside an admitted round or explicitly marked unadmitted by the lane.
- Standing note (operator-owned): the lowest-axis obligation (freshness) is neither met nor waived this round; it rests on the open L0 kotodama round-11/round-89 questions. Consistent with r90–r93 closures; the operator owns the ruling.
- SHONEN note for the operator (promotion is operator-owned; no `[x]` written by closure): boxes 1 (SKILL decision tables/error patterns/checklists with cited sources) and 3 (instructions executable without oral context — claims.json predicates and committed counters are re-runnable from committed bytes) look checkable by a non-author from committed bytes; box 2 (end-to-end task logged in LOG.md) is evidenced by the round-94 LOG entry; box 4 needs a province-accuracy sweep. No box is marked by this verifier.

## Closure ruling

Conformance: PASS (no defects). Claims: O fails as declared (evidence-verified), C and A verify (re-measured); no axis harmed. The lane stopped honestly on its own frozen gate and reported the failure without narrowing it. Verdict: **rejected-honest-stop, not admitted** (every-claim-verifies rule unmet on O); lane-round status `ok` (real report, real landed work). C and A's improvements stand as re-measured; O's residual work is routed above.
