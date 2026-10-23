author: hyaku closure (non-author integrator, @m_opus)

# Round 58 — non-author verifier spot-check (kotodama)

Closure session `HyakuCloseKotodama58`, 2026-10-22 (-03; 2026-10-23 UTC). The hyaku orchestrator dispatched it, not the lane.
- Lane base: `91e50d7e976d0f94e3ce9d1e404c068b2ac2bcf0`.
- Lane tip: `af1a348980f9b9ac20cdf8829e5bdd176b401735`.
- Report: `.ufo/reports/round-58/kotodama.md` at fleet `7e41821a`.

All checks were read-only: `git show`/`git diff`/`grep`/`wc`/`curl` over committed bytes and live sources. No lane gate (`accept-c.py`, `rowcheck.py`, `check-claim-separability.py`) was executed. Five read-only seats ran the re-checks: `ReviewClaimC58`, `ReviewR57Repairs58`, `ReviewGateSpot58`, `ReviewContainment58` (reviewers) and `CriticStrict958` (critic). The closure itself re-opened S511.

Driver digest (copied from `.ufo/watchdog.log`, which is mutable):

    2026-10-22T21:37:18-03:00 launch kotodama round=58 pgid=3580278 driver=hyaku-inline attempt=1
    2026-10-22T22:00:51-03:00 lane-dead-no-report kotodama round=58; retry same round (hyaku-inline attempt=1: L1 died with the orchestrator session freeze at 00:54Z (attempt 1 landed nothing: lane tip = base))
    2026-10-22T22:00:53-03:00 launch kotodama round=58 pgid=3651885 driver=hyaku-inline attempt=2
    2026-10-22T23:18:00-03:00 complete kotodama round=58; hyaku-inline attempt=2

## 1. Step-1 conformance

| check | command | observed | result |
|---|---|---|---|
| report by lane identity | `git log --format='%an %H %cI' -- .ufo/reports/round-58/kotodama.md` | `kotodama-shokunin 7e41821a… 2026-10-22T23:17:43-03:00`, after the lane tip (23:16:48) | pass |
| SHONEN heading, one line per box | report §SHONEN | 4 lines, all `[~]`, matching `SHONEN.md` boxes at :5, :7, :9, :11; no `[x]` | pass |
| cited lane hashes are ancestors of `main` | `git merge-base --is-ancestor <h> main` for 91fb8fd9 3d790714 a43f5336 c42121f4 edecdc90 1a07344e 80f48c2c 6faef400 97577f6c adc28834 ee7caddc d4a5ea31 25919ac4 ddc17f4a a7e47abd e27c8a67 45bb7e1a af1a3489 (also the uncited 31cf8b62) | 19/19 `anc` | pass |
| pushed | `scripts/hyaku/jj-lane.sh state` | `branch=main local=af1a3489… remote=af1a3489… ahead=0 behind=0 head=detached tracked=0 untracked=11` | pass |
| no leftovers | `git status --porcelain` | 11 untracked files at the lane root (see defect D1) | **defect** |
| prompt carries the template contract | `diff` of `## ` headings, `templates/round-prompt.md` vs the dispatched prompt | identical plus `## 6. Campaign addendum — hyaku (百)` (includes §6 item 9, claim sizing) | pass |
| census | `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama` | `kotodama ok …/corpus/SOURCES.md`, exit 0 (W04 duplicate-url warnings only, e.g. S561, S564-S566, S569-S573) | pass |

The fleet prompt commits (`21b9f62c`, `6becaa50`) carry the lane identity but are the driver's "dispatch evidence" commits, the same pattern as other lanes this campaign. The report's statement that the prompt "was not committed from the lane" holds.

Step 1 passes: this is a real report with checkable work, so status is `ok`. The leftovers are a status-neutral defect.

## 2. Claims

One claim was declared: **C, coverage** (`reports/round-58/claims.json`, predicate ACCEPT-C-58, claim base `80f48c2c`).

### Claim C — coverage (evidence-verified, plain counts re-measured)

**§9 ordering (freeze before data).**
- First data dispatch: `find .ufo/waves/round-58 -maxdepth 1 -printf '%TH:%TM %p\n'` gives `build-dispatch.json` and `build-spec.json` at 22:48:29, `build/swarm-registry` at 22:48:52, and the first build report at 22:49:53. The dispatch context names base `80f48c2c` and dry-run `adc2883` (committed 22:48:27).
- Instrument commits all precede it by at least 23 minutes: 91fb8fd 22:05:16, 3d79071 22:06:06, **31cf8b6 22:08:06**, a43f533 22:09:28, c42121f 22:16:20, edecdc9 22:18:28, 1a07344 22:20:20, 80f48c2 22:25:25, 6faef40 22:25:34.
- Control seats scored the earlier revisions and drove them. `run.json` under `control/CtlOffTopicEcho58`, `CtlLexiconKey58` and `CtlNoReader58` shows exit 0 / `ACCEPT-C-58: PASS` at 01:14:25Z, 01:14:27Z and 01:19:14Z. These are the controls §9 requires before data; fixing the counter after them is sanctioned.
- The support-control reports (22:32:51, 22:34:21 and 22:36:06) and every data seat came after the final rule.

**No rule change after data.**
- `git diff --stat 80f48c2c af1a3489 -- reports/round-58/` shows only `claims.json`, where the base/base_note changed at 6faef40 (pre-data), `separability-manifest.json` (base field) and new telemetry.
- `git diff --name-only 6faef400 af1a3489 -- reports/round-58/{accept-c.py,rowcheck.py,reopen-quote.py,claims.json,claims-agree.py,dry-run.py,base-knowledge-files.txt,separability-manifest.json} tools/check-source-access.py` returns no output.
- The predicate judged is therefore the predicate declared before data.

**Frozen predicate and the committed verdict (evidence-verified, not executed).**
- Predicate text: `claims.json` `.claims[0].predicate` reads "python3 -B reports/round-58/accept-c.py exits 0 and prints `ACCEPT-C-58: PASS`". The code matches it: `accept-c.py:59` `ACCEPT-C-58: every leg above prints PASS.` and `:227` `verdict = all(ok …)`. `accept-c.py@80f48c2c:28` says "No slack: one unlocated row fails the leg", and `:30-33` says BOILER is "live; unfetchable root, source-is-root, or not located all fail".
- `reports/round-58/telemetry/final-measures.txt` contains four runs, each `ACCEPT-C-58: FAIL` with exit 1:

  | run | failing leg | row and reason |
  |---|---|---|
  | `a7e47ab` | BOILER | S510 page-unfetchable |
  | `e27c8a6` #1 | TOPIC | S511 page-unfetchable |
  | `e27c8a6` #2 | BOILER | S510 root-unfetchable |
  | `45bb7e1` | BOILER and TOPIC | S511 unfetchable |

- Every other leg passes on every run: cited 44, LOCATE 44/44, RELEVANCE 44/44, DISTINCT hosts 23, SUPPORT 44/44 by 6 seats.
- Today S510 and S511 both return HTTP 403 to `curl -A 'Mozilla/5.0'`. The failures are fetch-class, but the frozen rule allows none.

**Plain re-measure at the tip.**
- `git cat-file -e`: `corpus/knowledge/linguistics/toponymy-place-names.md` exists at af1a3489 and is absent at 91e50d7e.
- `grep -c '^| S[0-9]' corpus/SOURCES.md`: 465 → 525.
- The entry cites 44 distinct ids, exactly S500-S543 and none outside that range.
- Tiers in S500-S543: A 38 / B 6. Distinct hosts: 23.
- All of these agree with the report.

**Separability.**
- In the `separability-manifest.json` at the tip, C lands 3 corpus files and REC lands 9. `.ufo/waves/round-58/support/` is in neither.
- `accept-c.py:81,207,212` reads `.ufo/waves/round-58/support/registry.json` and the `<Seat>.md` verdicts.
- `final-measures.txt` records `SEPARABILITY_DEPENDENCY` at `e27c8a6`#2 (exit 1). No separability re-run is committed after `e27c8a6`.
- Disclosed by the author; confirmed.

**Ruling: C MISSED.** The predicate declared before data printed FAIL on 4/4 final runs, and no rule was changed after any data seat. The report says so ("C does not verify as declared … reported, not amended") and does not narrow the target. This is an honest stop.

### Routed round-57 repairs (independently re-checked; records, not claims)

- **CODH bukan erratum, S576: agree.**
  - `curl -sL https://codh.rois.ac.jp/bukan/han/H236/` returns HTTP 200 and 192,162 bytes, the exact size recorded in `round-58.md:108`.
  - The HTML carries the row's fields: `（記号）「丸にエ」3`, `大成武鑑`, `名古屋`.
  - The round-57 not-registered reason is false. S576 is registered as tier B, queued, and QUALITY criterion 12 is filed.
- **Heraldry :41 → S575: agree.**
  - `git show e27c8a6 -- corpus/knowledge/myth-symbol/heraldry-emblems-identity-marks.md` shows :41 narrowed to the younger-son petition to matriculate "with a small mark of difference (S575, Information Leaflet No. 4, p. 8)".
  - The S575 PDF re-fetched at 98,899 B and 12 pages, both exact matches. `pdftotext -f 8 -l 9` prints "Otherwise younger sons and their descendants inherit a right to apply for a Matriculation of their ancestral Arms with a small mark of difference added".
- **Tier count: agree.**
  - `awk -F'|' '$2 ~ /^ S4(1[3-9]|[2-4][0-9]|5[0-4]) $/ {print $5}'` over `SOURCES.md` gives 36 A / 6 B at af1a3489, at the round-57 tip 89b94b6, and at 78d83b5.
  - The round-57 "A 34, B 8" was wrong. The correction is filed in the lesson routing at :15, the errata at :110, and R58-M2.
- **S428, no row owed: agree.** `build/ReviewSupersedeB58.md:11-45` re-opened the archive.org djvu text: four of four anchors are LOCATED and the instrument joins line-end hyphens. The draft S563 was correctly not filed.

### Measured vs evidence-verified

- **Re-measured by the closure:** entry presence, row count 465 → 525, cited set 44 = S500-S543, tiers 38/6, hosts 23, round-57 tier count 36/6, commit and dispatch ordering, and the instrument diff after the freeze.
- **Evidence-verified (lane gate, not executed):** the ACCEPT-C-58 verdicts in `final-measures.txt`, the separability verdict, and `controls-c.txt`.

### Per-axis verdicts

| axis | verdict | reason |
|---|---|---|
| coverage | unprovable | Claim C missed on its frozen predicate (4/4 FAIL). The entry and its 44 rows landed and the sampled rows check out, but the declared counter did not verify the move. |
| calibration | unchanged | Not claimed. Records only: errata, S560-S576, criterion 12. |
| depth | unchanged | No claim; SCORECARD diff touches no depth row. |
| operability | unchanged | No claim. |
| freshness | unchanged | Paused by the open round-11 L0 question. |
| adjacency | unchanged | No claim. |

`git diff 91e50d7e af1a3489 -- SCORECARD.md` only appends the round-58 author table. That table already reports coverage as "NOT VERIFIED as declared" and edits no earlier rows, so no owned axis is harmed.

## 3. Discernment spot-check

Source: `corpus/lessons/round-58.md` `## Gate` and the new `SOURCES.md` rows.

| item | decision | re-opened source | agree/disagree | reason |
|---|---|---|---|---|
| S510 (NT place-names guidelines) | admit | `environment.nt.gov.au/…/place-names-committee/guidelines`: live HTTP 403; Wayback `20251018101254` | agree | The quote is verbatim in the archived capture under "Aboriginal and dual names" (22 words ≤ 25) and supports the entry line. Today's live 403 matches the disclosed fetch failure. |
| S511 (Geographic Names Victoria, "How to get started") | admit | `www.land.vic.gov.au/place-naming/aboriginal-place-naming/how-to-get-started`: live HTTP 403 (5,628 B); Wayback `20251208050610` (HTTP 200) | agree | "While these features are defined differently to western concepts of place, their Aboriginal names are just as important to preserve." is present verbatim (`q in text → True`, 20 words ≤ 25). Re-opened by the closure. |
| S514 (England place-name vocabulary) | admit | live HTTP 200, 32,469 B | agree | Near-verbatim; the only difference is that the page writes "place‑name" with a non-breaking hyphen (`&#8209;`). 13 words; the continuation supports the scope cell. |
| Toronto street-naming page | reject (TOPIC terms 0) | live HTTP 200, 73,914 B | agree | toponym, toponymy, exonym, endonym and gazetteer each have 0 hits; generic, specific and element have 1 incidental hit each. |
| Barnet street naming and numbering policy | reject (HTTP 403) | `barnet.moderngov.co.uk/…/Street Naming and Numbering Policy.pdf` | agree | Both a plain GET and a Mozilla UA return HTTP 403 with an HTML error page, not a PDF. |
| GSI Japan | reject (TLS) | `https://www.gsi.go.jp/ENGLISH/` | agree | curl returns `000`. `openssl s_client` shows "unsafe legacy renegotiation disabled" and "Secure Renegotiation IS NOT supported", the exact condition reported. |
| Innervate undergraduate essay | reject (tier judgment) | `…/innervate/23-24/engl3013-andrina-bettschen.pdf`, HTTP 200 | agree | Page 1 confirms an undergraduate journal (Volume 16, 2023-24). The tier exclusion is disclosed as a judgment. |

Result: 3/3 admits and 4/4 rejects agree. The two disclosed fetch failures are real and not quote defects.

## 4. Trend verdicts

- **expansion: improved.**
  - Evidence: one new entry on uncovered ground. At base, `git ls-tree -r --name-only 91e50d7e corpus/knowledge | grep -ciE 'topon|place-?name|placename|onomast'` gives 0. The entry cites 44 `mined` rows opened this round, and all three sampled rows hold their quotes.
  - The claim's counter failed on live fetches, not on the QUALITY bar the rows were admitted under. Critic `CriticStrict958` dissented and argued harmed; the closure records that dissent and does not adopt it.
- **quality: harmed (a trade, not admitted).**
  - Heraldry :41 was re-sourced to S575 and the CODH reason corrected, which is improvement.
  - But the round re-verified the twelve kongo-kingdom sentence fixes and still left them unapplied (lesson :16: "NOT applied … carried a third round"). For example, `kongo-kingdom.md:84` still states the unqualified *mestres* "white shoulder cloth" generalization, while `build/ReviewKongoA58.md:71` limits it to two figures in one watercolor.
  - An entry found false or stale and left unmarked meets LEARNING's harmed condition. Round 57 graded quality improved at the second carry; a third carry with a fresh re-verification ("all agree") no longer can be.
- **discernment: improved.** The outside spot-check agrees 7/7 (§3). The round-57 disagreements became grounded learning: QUALITY criterion 12 ("Re-test stated rejection grounds") cites the round-56/57 findings, and the CODH and S428 errata are filed.

## 5. Routed defects (owing lane: kotodama, next round)

1. **Containment: 11 untracked files at the lane root.** The files are `carriers.txt`, `flagged_rows.txt`, `locator_diff.txt`, `met_check.txt`, `plwiki_check.txt`, `s313_check.txt`, `s435_entry.txt`, `s452_locate.txt`, `tier_rule.txt`, `uncited_terms.txt` and `wayback_rows.txt` (mtimes 23:05:56-23:16:23 -03).
   - They were written by the cancelled round-58 seat **ExecReasonSweep58**. Each file's first line is the `echo` header of a command that seat ran from the lane root (its transcript lines 256-358), and the last two were written seconds before the cut.
   - The report's "not attributable to a round-58 seat" is false.
   - Fix: dispose of these files, and confine every seat's writes to its wave directory or scratch.
2. **Revision count.** Six pre-data revisions were made, not five. `31cf8b6` (22:08:06) added the TOPIC leg: TOPIC mentions in `accept-c.py` go 0 → 3. The report, SCORECARD and `claims.json` `revision_note` all omit it.
3. **Freeze provenance overstated.** In `claims.json`, `declared_at` says "before any wave dispatch and before any seat scored", but `revision_note` says "only pre-data control seats had scored". Fix: separate the control-forced calibration revisions from the final freeze.
4. **The "123 controls, 0 pass" claim is overstated.**
   - `controls-c.txt` records 18 fixtures that fail only SUPPORT, including the honest green (`MutLegIsolation58/green-final`: mechanical legs PASS, `SUPPORT FAIL … no registry: FileNotFoundError`).
   - Failing on a missing verdict file shows no discrimination. Fix: qualify the count.
5. **No-slack live legs.** Fetch-class 403s at two .gov.au hosts sank C. Next time, declare a fetch rule before data (an archived capture, or a bounded fetch-class allowance with its own control) — never after the result.
6. **Separability.** C's acceptance reads `.ufo/waves/round-58/support/`, a path its declared lands omit, and no separability re-run is committed after `e27c8a6`.
7. **Kongo-kingdom: carried a third round.** The twelve verified sentence fixes are re-verified but unapplied (entry lines 18, 65, 82, 84, 85, 89, 93, 97, 110, 140, 141, 146). Apply them or mark the lines next round; this defect is what makes quality harmed.
8. **Census at round start** was not run at round start; it was run late on a base clone (self-disclosed).

## 6. SHONEN note for the operator

All four boxes stay `[~]`, and no non-author verifier is on record for any of them. Boxes 2-4 cite resolvable committed evidence (LOG round 58, `.ufo/waves/round-58/support/` and `control/`, entry §2/§13). Resolvable evidence is not proof of an end-to-end success, though: this round's claim missed. No box looks fully checkable by a non-author yet. Promotion is operator-owned.
