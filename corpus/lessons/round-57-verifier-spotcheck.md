author: hyaku closure (non-author integrator, @m_opus)

# Round 57 — non-author verifier spot-check (kotodama)

Closure session `HyakuCloseKotodama57`, 2026-10-22 (-03; 2026-10-23 UTC). The hyaku orchestrator dispatched it, not the lane.
- Lane base: `86d08883e3c2a04f35db1aae7bde6b9d889f53b1`.
- Lane tip: `89b94b694ac6b06bf69b787166bc0bdd1a8bb848`.
- Report: `.ufo/reports/round-57/kotodama.md` at fleet `d6c792b4`.

Every execution ran in throw-away clones under `/tmp/kclose57/`, never in the lane. Seven read-only reviewer seats ran the re-checks: `CloseReC57`, `CloseReO57`, `CloseTimeline57`, `CloseRowsA57`, `CloseRowsB57`, `CloseRowsC57`, `CloseRejects57`. The closure itself re-opened S421.

Driver digest (copied from `.ufo/watchdog.log`, which is mutable):
- `2026-10-22T19:48:42-03:00 launch kotodama round=57 pgid=1485070 driver=hyaku-inline attempt=1`
- `2026-10-22T21:19:49-03:00 complete kotodama round=57; hyaku-inline attempt=1`

## 1. Step-1 conformance

| check | command | observed | result |
|---|---|---|---|
| report landed by the lane | `git log --format='%an %H %cI' -- .ufo/reports/round-57/kotodama.md` | `kotodama-shokunin d6c792b44341776673d6c252a9f019145ae120eb 2026-10-22T21:19:28-03:00`; lane tip committed 21:18:36-03 | pass |
| `SHONEN` heading, one line per box | report lines 47-52 against `SHONEN.md:5,7,9,11` | 4 lines for 4 boxes, all `[~]` with pointers | pass |
| cited hashes exist and are ancestors of `main` | `git cat-file -t <h>; git merge-base --is-ancestor <h> main` for `86d08883 6f08c494 51726fa6 0c16d15d 0314aa98 13226c18 286288f4 43f1e781 78d83b5e 89b94b69` | 10/10 `commit`; 10/10 ancestors | pass |
| lane pushed, clean | `scripts/hyaku/jj-lane.sh state …`; `git status --porcelain \| wc -l`; `git ls-remote origin refs/heads/main` | `ahead=0 behind=0 head=detached tracked=0 untracked=0`; `0`; remote `89b94b69…` | pass |
| prompt carries the template contract | `diff <(sed -n 1,140p .ufo/prompts/kotodama-round-57.md) templates/round-prompt.md` | only the `{{LANE}}`, `{{ROUND}}`, `{{FLEET_ROOT}}` and `{{AXES}}` substitutions differ; the §6 addendum (with §9 claim sizing) follows at line 141; all five child-lane items and the round-level items are present | pass |
| report sections | report headings | Work performed, Landed changes, Before → after, Sources & frontier, Trend verdicts, SHONEN, round shape, Stale-lane line, tool installs | pass |
| seat shape | report :56; `.ufo/waves/round-57/build-dispatch.json` `counts`; `ls .ufo/waves/round-57/residual` | pre-dispatch 2 + build 50 (`"spawn": 50`) + residual 8 files = 60 seats; no wave 2; HOLD `kotodama51-prereg-critic` not recreated | pass |

Marker test: the report names real committed work, so status is `ok`.

Status-neutral defects:
- The lane identity committed the dispatched prompt (`698531c`, 19:48:41-03), not the integrator. Round 56 had the same defect.
- The fleet root has untracked files `bm.json`, `live_s228.html`, `nama.html`, `s395.txt` and `tf_bavelas.html`. Their mtimes run from 12:45 to 19:12 -03, all before the 19:48 launch. The report names them. They are not round-57 debt.

## 2. Claims

Owned-axis harm check:
- `git diff 86d08883 89b94b69 -- SCORECARD.md` adds one capability row and the round-57 axes section. It changes no earlier score and records no harm.
- `git diff --stat` over `SKILL.md`, `PROVINCE.md` and `SHONEN.md` is empty.
- `PROVINCE.md:4` already covers "mythic and symbolic systems", so it stays accurate.

§9 ordering (CloseTimeline57; committed bytes plus filesystem mtimes):

| event | time (-03) | pointer |
|---|---|---|
| pre-dispatch critics CriticClauseList{O,C}57 | 20:17-20:18 | `.ufo/waves/round-57/predispatch/` |
| instruments revised (rule frozen) `0314aa9` | 20:25:48 | git log |
| controls re-run and locator calibration, both measuring `0314aa98` | 20:26 | receipt headers |
| control receipts committed `13226c1` | 20:27:48 | `git show --stat` (controls-c.txt, controls-o.txt, locator-calibration.txt) |
| build dispatch files written | 20:28 | `build-dispatch.json` mtime; its `taskCall.context` names the claim base `0314aa98` and the declaration `13226c18` |
| ExecGateBareNumeric builds on a `13226c18` clone | 20:30-20:33 | seat report; sha256 `54981859…` |
| first data commit (O) / C committed | 20:34 author / 21:01:52 | git log |

- `git diff --stat 13226c1 89b94b6 -- reports/round-57/accept-c.py reports/round-57/accept-o.py reports/round-57/reopen-quote.py reports/round-57/controls reports/round-57/claims.json` is empty. `git rev-parse <rev>:reports/round-57/accept-c.py` gives `ef6ee4a6…` from `0314aa9` to the tip.
- The claims.json legs equal the leg tuples in `accept-c.py:87-158` and `accept-o.py:444-452`, and the receipt labels (`SHARE = 0.8`, `need=34`).
- `claims-agree.py` prints `AGREE claims=['C','O']`. `dry-run.py check` on both receipts prints `MISSING_FROM_RECEIPT [] UNDECLARED_IN_RECEIPT []`.
- Result: the controls were committed before any data seat ran, and no rule changed after a seat scored. The rule changed after the pre-dispatch critics, but they scored cheats against the instrument, not claim data. §9 says to fix exactly that "before data".

### Claim C — coverage (re-measured)

Command `python3 -B reports/round-57/accept-c.py`, run in a clone at each revision:
- At `13226c1`: `SET FAIL count=232 required=233`, `SWEEP FAIL rows 232`, `FLOOR FAIL cited=0 floor=20`, `LOCATE FAIL located=0 cited=0 need=0`, exit 1.
- At `78d83b5` and `89b94b6` (plus one rerun): all nine legs PASS, `FLOOR PASS cited=42 floor=20`, `LOCATE PASS located=41 cited=42 need=34`, `FRESH PASS`, `ACCEPT-C-57: PASS`, exit 0.
  - The one miss is S452, a Wayback `HTTPError`.
  - The report's 40/42 and 42/42 are other live runs. `final-measures.txt:11,24` record `located=42` and `located=40`.

Plain counts (the closure's own, at the tip):

| measure | command | base → tip |
|---|---|---|
| knowledge files | `git ls-tree -r --name-only <rev> corpus/knowledge \| wc -l` | 232 → 233 |
| filename owners | `… \| grep -ciE 'herald\|emblem\|kamon\|tamga\|insign'` | 0 → 1 |
| registry rows | `grep -c '^\| S[0-9]' corpus/SOURCES.md` | 412 → 465 (42 rows S413-S454 + 11 rows S481-S491) |
| S-ids in the entry | — | exactly S413-S454, each cited |

Tier and kind of S413-S454, from `awk -F'|' '/^\| S4(1[3-9]|[2-4][0-9]|5[0-4]) /{print $5}' corpus/SOURCES.md | sort | uniq -c` (column 5 is `tier`):
- Tiers: **A 36, B 6**.
- Kinds: docs 28, book 7, paper 4, community 3. The three community rows (S427, S444, S449) are all tier B.
- The report's "tier A 34, B 8 incl. community 3" (report :36) is off by two rows. This is a numeric defect in the report's frontier section, not in the claim's counter (routed defect 5).

Controls:
- CloseReC57 re-ran the `stub-invalid` control at the claim-base instruments: `LOCATE FAIL located=0 cited=20 need=16 … URLError`, with the other eight legs PASS. The result has the same shape as `telemetry/controls-c.txt` (`stub-invalid → exactly ['LOCATE'] AS-EXPECTED`).
- An invented-source entry therefore reaches eight of nine legs. LOCATE carries the claim.

Can the target fail on the quality it claims?
- **Closure's own cheat:** the landed tree with 10 of the 42 anchors (S413-S422) replaced by invented 10-word sentences, URLs unchanged. Result: `LOCATE FAIL located=32 cited=42 need=34`, exit 1, on both runs. Invented sourcing fails the predicate.
- **Footer test:** `reopen-quote.py <S454 URL> "and cookies Terms of use Accessibility statement Victoria and Albert Museum London"` prints `LOCATED`. LOCATE checks only that the quote is on the page (at least 8 words, deny-listed hosts). It does not check whether the quote is relevant or supports the row.
- So the predicate catches fabricated quotes. It does not catch real but irrelevant on-page text, and its 20% slack lets up to 8 of 42 unlocated rows pass.
- The declaration lists relevance and sentence support as review-only. §3 samples them, and 14/14 admits agree.

Axis naming: the surface named is frontier → core, a topic file with 0 filename owners at base. The unmoved command is named in `claims.json` `surface`. The sourceless fixture does not satisfy the full predicate.

Verdict: **verifies as declared.**

### Claim O — operability (re-measured; closure probe)

Command `python3 -B reports/round-57/accept-o.py`, no `--seed`:
- At `13226c1`: `GEN FAIL lessons=5 failing=5`, `REAL FAIL lessons=3 failing=3`, `MUTANTS FAIL … survivors=['double-decode','stop-at-first-bad-file','label-rename']`, `SELFTEST: 38/38`, exit 1.
- At `43f1e78` and `89b94b6`: all seven legs PASS, `SELFTEST: 52/52 pass`, exit 0.

Tool sha256:
- `3a13ab9c…` at the base and at `13226c1`.
- `54981859…` at `43f1e78` and at the tip. This matches the build seat's hash and `final-measures.txt`.

`tools/check-gate-quotes.py --selftest` prints 38/38 at the base and 52/52 at the tip.

Controls: `controls-o.py` re-run at `13226c1` exits 0 with `CONTROLS-O-57: every control as expected`. All 16 `## control … -> AS-EXPECTED` lines are identical to `telemetry/controls-o.txt`, and so are the 112 leg words.
- The round-56 `sidcheat` checker (sha256 `e3060c1c…`) exits 1 with `failed_legs ['GEN','MULTI','MUTANTS','REAL']`.
- The critic's honest checker exits 0.

Closure's probe: CloseReO57 wrote its own lesson and registry, rows S701-S707, from a design independent of the lane's fixtures.

| checker | findings | exit |
|---|---|---|
| landed tool `89b94b6` | 5: bare `&#8220` and `&#x201C` flagged, `&#8220;` flagged, `&amp;hellip;` flagged once (no double decode), `&#xD800;` flagged; `&mdash` without `;` not bound (policy); clean row silent | 1 |
| base tool `86d08883` | 3: misses both bare numeric refs | 1 |
| `sidcheat` control | 0 | 0 |

- An invalid-UTF-8 file run with a valid file, in either order, exits 2 with `GATE_QUOTES_ERROR` and still prints all 5 findings for the valid file.
- **New shortcut not in the control set:** the landed tool with its bare-hex arm deleted (`hexonly`, sha256 `8ed00473…`). It fails GEN, REAL, MUTANTS and SELFTEST (49/52), so `ACCEPT-O-57: FAIL`, exit 1.
- Axis naming: the surface is the checker's reference grammar (a new edge class) and its selftest's kill set.

Verdict: **verifies as declared.** No tested shortcut reaches the target. This repairs the round-56 ruling (spot-check §5 items 1-2).

### Measured vs evidence-verified

Both claims were re-measured by re-running their frozen predicates in clean clones. They are acceptance predicates, not registered gates. The landed tool's `--selftest` was run as a read-only probe in a clone.

Evidence-verified only:
- the dry-run receipts (`dry-run.py check`, not `run`, because `run` writes under `/fast/scratch`);
- the residual seats' 3× O re-runs and the 7 grammar mutants.

### Per-axis verdicts

| axis | verdict | basis |
|---|---|---|
| coverage | improved | C re-measured: 232 → 233 files, filename owners 0 → 1, 42 mined rows cited, LOCATE 41/42 (need 34); sample agrees 14/14 |
| operability | improved | O re-measured: FAIL → PASS, selftest 38 → 52; sidcheat, base and hexonly fail; closure probe 5/5 against base 3/5 and sidcheat 0/5 |
| calibration | unchanged | not claimed; records only (QUALITY c10, errata, S481-S491) |
| depth | unchanged | not claimed |
| freshness | unchanged | paused by the open round-11 L0 question |
| adjacency | unchanged | not claimed |

Both claims verify and no axis is harmed, so the round is **admitted**.

## 3. Discernment spot-check

Sample: 14 admits among the new rows S413-S454, and all five rejects or not-registered items in the lesson's Gate. Quotes were counted by whitespace split; the lane minimum is 8 words and the CORPUS maximum is 25. For each admit, at least one entry sentence citing the row was also read against the source.

| item | decision | re-opened source | agree/disagree | reason |
|---|---|---|---|---|
| S416 | admit | archive.org `aglossarytermsu08parkgoog` djvu.txt (HTTP 200, 1,622,219 B) | agree | Introduction quote verbatim (9 words); the blazon-order anchors pp. 64-67 are found; entry :67 supported |
| S420 | admit | courtofthelordlyon.scot `coats of arms.htm` (200, 26,393 B) | agree | LYON-COATS-1..4 verbatim (13 words). Entry :41 "a cadet matriculates with a difference" is not on the page (`grep -ci diffe` → 0) (defect 3) |
| S421 | admit | courtofthelordlyon.scot `blazoning.htm` (200, 41,791 B; re-opened by the closure) | agree | Rule of tincture, "of the First", regardant/dormant and "all Arms are individual" are all on the page. The quote drops the served commas ("no metal on a metal, no colours…"), 12 words |
| S424 | admit | gg.ca public-register project 622 (200, 74,742 B) | agree | Inukshuk quote located (20 words); the blazon and the Inuvialuktun motto are served; entry :112 supported |
| S427 | admit | heraldica.org `le-mans.htm` (200, 5,464 B) | agree | Quote verbatim (14 words); ca 1150-55, 1149 seal and 1170-75 chronicle are on the page; tier B is fair |
| S431 | admit | emuseum.nich.go.jp record 101117 (200, 22,292 B) | agree | Quote located (24 words); the "said to have" hedges are kept in entry :93 |
| S433 | admit | maiask.ru Yatsenko/Rogozhinskii (200, 18,744 B, equal to the row) | agree | Quote verbatim (22 words). The locator says "abstract page", but the page never prints "abstract" |
| S435 | admit | bazhum.muzhp.pl PDF (200, 1,104,463 B, equal) | agree | Polish quote exact, p. 2 §1 (11 words); all four quotes locate; entry :84 supported |
| S438 | admit | ag.colorado.gov `about-brands` (200, 91,391 B) | agree | Quote located (14 words). The `teaches` cell says "since 1865", but the source and entry :58 say "approximately/about 1865" |
| S443 | admit | vatican.va AAS 61 (1969) PDF (200, 4,095,490 B, equal) | agree | §9 on printed p. 336 (PDF index 335), 9 words after OCR-hyphen normalisation; entry :60 ("simplex atque perspicuus", p. 339) supported |
| S446 | admit | archive.org DLI `2015.178234` djvu.txt (200, 734,288 B, equal) | agree | Quote exact with the hedge (20 words); heredity framed as Mayer's hypothesis; the digitising programme's own scan passes amended c10 |
| S449 | admit | lukeuedasarson.com `NDshields.html` (200, 8,471 B) | agree | Quote exact (12 words); the oval clause is served; "never labels" rests on "no known ancient source … let alone says"; tier B calibrated C |
| S451 | admit | rbcm.ca Thunderbird Park ex8 (200, 23,665 B, equal) | agree | Quote located (20 words); "represent and honour" four nations supported at entry :111 |
| S454 | admit | collections.vam.ac.uk O456793 (200, 48,355 B, equal) | agree | Object-description quote located (18 words); second-rank golden pheasant supported at entry :91 |
| Kashgari / Dankoff-Kelly 1982 | reject | archive.org `CompendiumOfTheTurkicDialectsPart1-…` (200; uploader a private address, `licenseurl` null) | agree | In-copyright 1982 translation, private upload, no permission; fails every amended-c10 prong |
| Özalp 2008 thesis | reject | islamawareness.net PDF (200, 7,499,471 B; no permission line on pp. 1-4) | agree | Third-party community host; not the publisher or the institutional repository |
| Manchester Corp. v Palace of Varieties [1955] | reject | archive.org documentcloud re-upload (200; no licence) | agree | A blogger's re-upload of a law report, not an archive's own scan |
| pl.wikipedia "Zawołanie" | not registered | pl.wikipedia.org (200, 113,233 B) | agree | A tier-C lead cannot be sole support (`QUALITY.md:25-26`); S435 carries the claim |
| CODH bukan | not registered | codh.rois.ac.jp/bukan/ and `/han/H236/` (200) | **disagree** | The stated reason is false. The scout's four quotes normalise to 11/10/15/11 words and each prints `LOCATED` under `reopen-quote.py` (defect 1) |

New SOURCES row quote check: S421's anchor LYON-BLAZ-1, "Basic rule - no metal on a metal no colours on a colour", has 12 words (≤25). It is located in the served text, with commas normalised.

Census: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama` prints `kotodama ok …/corpus/SOURCES.md`, exit 0. It also prints 14 W04 cross-scope duplicate-URL warnings:
- ten on older rows (S127-S133, S185, S186, S358);
- four on superseding rows S482, S483, S485 and S490, which re-use their superseded rows' URLs by design;
- none in S413-S454.

Tally: admits agree 14/14, with four minor cell or entry notes. Rejects agree 4/5; the CODH reason is false.

Criterion-10 consistency (CloseRejects57):
- S413-S415 and S417 are Robarts/University of Toronto scans, and S446 is a Digital Library India scan. All five fit "the digitising library's or archive's own scan".
- S416 is a grey edge: a Google scan of a Harvard copy uploaded by `tpb`. It fits the spirit of the criterion, not its letter.

## 4. Trend verdicts

- **expansion: improved.**
  - New ground: the heraldry/identity-marks topic had 0 filename owners at base (0 → 1, re-measured), and files rose 232 → 233.
  - 42 new `mined` rows.
  - One new checker edge class (bare numeric references), verified on the closure's own fixture.
- **quality: improved.**
  - The round-56 quality instrument gap is closed. O now defeats the exact round-56 cheat, six other cheats and the closure's new `hexonly` shortcut, and its selftest kills the three round-56 survivors (38 → 52).
  - The carried round-56 row findings are superseded by S481-S491.
  - The entry critic's fixes landed in `89b94b69`.
  - Residual: cell defects in S413, S417, S428, S440, S445, S452 and S453 are carried, the kongo-kingdom sentence fixes are carried a second round, and §3 adds four minor notes.
- **discernment: improved.**
  - Criterion 10 was amended from the round-56 outside check and applied to three rejects; the outside re-open agrees 3/3.
  - Both pre-dispatch critiques were adopted before data.
  - Sampled admits agree 14/14.
  - Against this, one not-registered reason is false (CODH). It is the same class as round 56's koon1244.

## 5. Routed defects (owing lane: kotodama, next round)

1. **`corpus/lessons/round-57.md:92` CODH bukan reason is false.** Append an erratum; never rewrite the filed bytes. The quotes normalise to at least 10 words and locate live. Either register the rows or state the real ground. This is the second round running with a false not-registered reason (after koon1244). Add a QUALITY check that each not-registered reason is re-tested by the tool it names.
2. **LOCATE is blind to relevance and has an 8-row slack.** Real off-topic page text passes (the closure's footer test), and 8 of 42 rows may go unlocated. The next sourced-claim predicate should bind each quote to the row's `teaches` cell, for example with a reviewer-sampled support leg or a keyword overlap. It should also make each unlocated row carry a committed capture or a named failure class.
3. **Entry `heraldry-emblems-identity-marks.md:41`:** "in Scotland a cadet matriculates with a difference (S420)". S420's page does not say this. Re-source the sentence or scope it out.
4. **Cell defects, owed as superseding rows:**
   - S421 anchor drops the served commas;
   - S438 `teaches` "since 1865" should be hedged "approximately 1865";
   - S433 locator "abstract page";
   - plus the lesson's own Frontier list (S413, S417, S428, S440, S445, S452, S453).
5. **Report `.ufo/reports/round-57/kotodama.md:36` tier count.** It says "tier A 34, B 8 incl. community 3"; the committed rows are A 36 and B 6, and the three community rows are kind `community`, tier B. File the correction in the next report.
6. **Carried a second round:** the kongo-kingdom.md sentence fixes (entry lines 18, 65, 82, 84, 85, 89, 93, 97, 110, 140, 141, 146), and the round-56 carry list (S135, S141, S147, S151, S159).
7. **Note, no action:** `reports/round-56/accept-c.py` was edited in place (raw docstring). The records say stdout is byte-identical, and round 56 is closed, so this is recorded only. Future fixes to a filed instrument should land as a new file.

## 6. SHONEN note for the operator

All four boxes are `[~]` (author-asserted). Box 3, "Instructions executable by an agent without oral context", again has non-author evidence: this closure re-ran both predicates, both control suites, the census and the plain counts from committed paths in fresh clones, and every claim value matched. Boxes 1, 2 and 4 still need a non-author promotion review. Promotion is operator-owned; this file writes no `[x]`.
