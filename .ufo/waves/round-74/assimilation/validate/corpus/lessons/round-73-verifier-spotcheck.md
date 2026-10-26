author: hyaku closure (non-author integrator, @m_sonnet)

# Round 73 — non-author closure spot-check (kotodama)

Base `8841ad3b896a0227674fa0725b818c999118046f` → lane HEAD `c1b5b4761b6ae5ef9ffd81267c3e5e2189ed428d`. Driver digest (`.ufo/watchdog.log`, mutable): `2026-10-25T18:56:34-03:00 launch kotodama round=73 pgid=88120 driver=hyaku-inline attempt=1` · `2026-10-25T20:43:58-03:00 complete kotodama round=73; hyaku-inline attempt=1`. Measured 2026-10-25 against committed bytes (`git show`/`ls-tree` at the two hashes) plus live re-opens.

## 1. Step-1 conformance

- Report `.ufo/reports/round-73/kotodama.md` committed by the lane identity: `kotodama-shokunin dad39efd27988bd28b1fe41f5e327529f0472d3c round-73: kotodama report`. `SHONEN` heading present with four box lines (all `[~]`, each saying "no non-author verifier on record"). Real report, not a marker.
- Every cited lane commit (`af65165 e62d731 3537899 85f17eb 0316b88 7aa8f99 2d1cd91 c1b5b47`, and the HEAD) passes `git merge-base --is-ancestor <h> main`.
- `jj-lane.sh state`: `branch=main local=c1b5b476… remote=c1b5b476… ahead=0 behind=0 head=detached tracked=5 untracked=0`; `git ls-remote origin refs/heads/main` = HEAD.
- Prompt carries the template contract (§1 mission binding, §2 claims, §2b frontier step) — confirmed on read.
- **Defect (status-neutral): leftover uncommitted round work.** `git status --porcelain` at closure shows five modified wave-2 seat reports (`.ufo/waves/round-73/w2/CritEntryAmendFinal.md`, `ExecSelftestAll.md`, `ScribeLogScorecard.md`, `SimplifierEntries.md`, `drafts/log-entry.md`) and an untracked `.ufo/waves/round-73/w2/RevengerOrigins.md` — late seat writes after the push. The report's "RevengerOrigins returned no report by filing time" is accurate for the filed bytes, but the seat kept writing into the tree afterwards. Not committed by this closure.
- Defect: report says Ca selftest "9 scenarios"; the committed `telemetry/selftest-r3.txt` prints `SELFTEST OK: 10 scenarios` (and carries an `ERROR: base … not a commit` line inside the BASEMISMATCH control). Cosmetic.
- Defect: **no committed PASS-at-lands receipt** for either counter. The only `ACCEPT-C-73`/`ACCEPT-CA-73` lines under `reports/round-73/telemetry/` are FAIL controls (`controls-c.txt` 1/11; `controls-ca*.txt` 4/9–5/9). The reported `PASS legs=11/11` and `PASS legs=9/9` exist only in wave-2 seat reports (`.ufo/waves/round-73/w2/ExecRerunC.md:76,113`, `ExecRerunCa.md:91,105`, `CritAppendOnly.md:153,162`), and the lane's own seats flagged this (ExecRerunC m1, ExecRerunCa F7). Routed below.

## 2. Per-claim re-check

Re-measured = I ran a plain measurement over committed bytes; evidence-verified = I read committed evidence and did not execute the lane's counter (PROTOCOL §Gate standard, Closure consequence).

### Claim C (coverage, assimilation-sourced) — re-measured
| measure | command | base | after | reported |
|---|---|---|---|---|
| conlang-scholarship knowledge files | `git ls-tree -r --name-only <h> \| grep -ci conlang-scholarship` (excl. `.ufo/` drafts) | 0 | 2 (`corpus/knowledge/linguistics/conlang-scholarship.md`, `.amend-2026-10-23.md`) | 0 → 2 ✔ |
| registry rows | `git show <h>:corpus/SOURCES.md \| grep -c '^| *S[0-9]'` | 799 | 804 | 799 → 804 ✔ |
| rows naming the five hosts (ojs.unito.it, philol.msu.ru, journals.rudn.ru, cyberleninka.ru, sanders.phonologist.org) | `grep -c <host>` per host | 0 each | 1 each (S876–S880) | 0 → 5 ✔ |
| knowledge `.md` files | `git ls-tree -r --name-only <h> corpus/knowledge \| grep -c '\.md$'` | 245 | 247 | "247 files" ✔ |
| entry → row citations | `grep -o 'S87[6-9]\|S880'` | — | base entry cites S876 ×5, S877 ×25; amendment cites S878 ×12, S879 ×15, S880 ×12 | two entries on newly entered ground citing mined rows ✔ |
| census | `scripts/sources-census.sh validate --root <fleet> kotodama` | exit 0 (committed `census-start.txt`) | exit 0 (my run: 28 W04 dup-url warnings, last line `kotodama ok …/corpus/SOURCES.md`; also committed `census-end.txt`) | exit 0 ✔ |

Counter `ACCEPT-C-73 PASS legs=11/11`: evidence-verified only — committed `selftest-r3.txt` `SELFTEST: 29/29`, `controls-c.txt` do-nothing control `ACCEPT-C-73: FAIL legs=1/11`, counter sha256 `95aee881…` pinned; PASS-at-lands text appears in wave-2 seat reports, no telemetry receipt. Verdict **verified** (plain measurements agree).

### Claim Ca (calibration, records) — re-measured pair by pair
| pair | command | observed | agrees |
|---|---|---|---|
| L01 243→245 | `git ls-tree -r --name-only 8841ad3 corpus/knowledge \| grep -c '\.md$'`; `corpus/README.md:732` at base | 245; README line reads `Total knowledge entries: 243.` at base and still at head (annotated, not rewritten); later footer `:775` `…247.` | ✔ |
| L02 36→38 | same over `corpus/knowledge/culture-material` | 38; README `:407` `## culture-material/ (36)` | ✔ |
| L03 243→245 | README `:736` `(total 243 files; directory totals 30/29/36/29/24/95)` at base | present | ✔ |
| L06 PASS→FAIL | `git show 8841ad3:reports/round-72/telemetry/measures-ca.txt \| grep -o 'ACCEPT-CA-72: [A-Z]*'`; `SCORECARD.md:1401` at base | receipt `FAIL`; SCORECARD says PASS legs=12/12 | ✔ |
| L07 F1-F9→8 ids | `claims.json` `pre_data_corrections` ids; `LOG.md:4280` at base | `F1, F2/F3, F4, F5, F6, F8, F9, SCOUT-LIVE` (no F7); LOG says "F1-F9" | ✔ |
| L04/L05 | `git diff 8841ad3 c1b5b47 -- SHONEN.md`; `sed -n 505p/564p SKILL.md` | `:468→:505`, `:522→:564`; SKILL.md:505 `## Error patterns`, :564 `## Checklist` | ✔ |
| L08 registry rows | `grep -n 'accept-' SKILL.md` at head | rows accept-c-71 … accept-ca-73 (697–704), last row `accept-ca-73` (base last `accept-o-69`) | ✔ |
| R1 tracked | `git ls-tree -r --name-only <h> .ufo/waves/round-72/w1/` filtered | 0 at base; `ScoutMergeScan.md`, `ScribeLesson.md` present at head | ✔ |

Eight of eight pairs reproduce (before red, after as stated). Counter `ACCEPT-CA-73 PASS legs=9/9`: evidence-verified only (`selftest-r3.txt` `SELFTEST OK`, `controls-ca-r3.txt` do-nothing FAIL 4/9, `counter-revisions.md` r1→r3 disclosed with red-before `red-before-r3.txt`, sha256 `222d4dd6…`). Verdict **verified**.

## 3. Per-axis verdicts (SCORECARD diff is append-only: +27 lines, 0 deleted)
`git diff 8841ad3 c1b5b47 --numstat` outside `.ufo/`: LOG +12/-0, SCORECARD +27/-0, SKILL +7/-0, QUALITY +16/-0, README +14/-0, SOURCES +5/-0, SHONEN +1/-1 (pointer repair). No existing knowledge entry modified.

| axis | verdict | reason |
|---|---|---|
| coverage | improved | claim C re-measured: 0→2 entries, 0→5 host rows, 799→804 rows |
| calibration | improved | claim Ca re-measured: 8/8 ledger pairs reproduce, two untracked files now tracked |
| depth | unchanged | no existing entry deepened |
| operability | unchanged | SKILL.md rows added are registry rows; no decision table/checklist change judged |
| freshness | unchanged | paused under the open L0 round-11 ruling (`.ufo/l0-questions.md`) |
| adjacency | unchanged | no cross-lane edits; no handoff obligation fires |

No axis harmed. Admission rests on both claims verifying.

## 4. Discernment spot-check (LEARNING.md)
Sample from `corpus/lessons/round-73.md` `## Gate`; every source re-opened by me (UA `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36`, no automation).

| item | decision | re-opened source | agree/disagree | reason |
|---|---|---|---|---|
| S880 Anderson/Grant/Sanders | admit (B) | `https://sanders.phonologist.org/Papers/anderson-etal-cjl-sotl.pdf` → HTTP 200, 193610 B (equals recorded bytes) | agree | quote "One innovation of this work is that it suggests that a multi-part, creative project can be part of a course even at the introductory level." present verbatim; 25 words (cap) |
| S876 Enguehard 2022 | admit (B) | `https://ojs.unito.it/index.php/ricognizioni/article/view/7099` → 200, 30289 B (equals) | agree | quote present; row's 16-word excerpt is within the sentence |
| S877 Sidorova & Shuvalova | admit, tier B not scout's A | `http://www.philol.msu.ru/~sidorova/files/conlangs.pdf` → 200, 1055723 B (equals) | agree | Russian sentence «Языки, используемые в художественных произведениях, называют вымышленными или фикциональными.» found in extracted text; a non-peer-reviewed monograph is B |
| S878 Novikov 2022 | admit (B) | `https://journals.rudn.ru/semiotics-semantics/article/viewFile/31528/20955` → 200, 959171 B (equals) | agree | 24-word abstract quote present |
| S879 Kostyukhin 2023 | admit (B), live leg only | `https://cyberleninka.ru/article/n/klassifikatsii-konlangov-v-sovremennoy-interlingvistike` → 200, 97656 B (record 97622, page drift) | agree | "2.2. Personal languages Это личные, или персональные, языки …" present; live-only is honest given the lane's no-capture-body finding |
| S894 Sowers-Wills clause | reject (status/429, out of declared set) | canonical Cambridge article URL → HTTP 429, 1302 B "Too many automated requests"; CDX `filter=statuscode:200` → captures 20241106195515 and 20241107004043 | agree | 429 is a rate limit, not UA-gating (QUALITY 16); the lane's corrected ground ("two 200 captures exist") matches the CDX; reject stands as outside the declared set, flip recorded |
| S909/S910 Springer chapter | reject/not adopted | `https://link.springer.com/chapter/10.1007/978-3-032-03277-5_15` → browser UA 200, 3038 B `Client Challenge`; `curl/8.7.1` 200, 325225 B | agree | reproduces the UA-dependent wall; an unreachability reject would be void, and the lane did not claim one (QUALITY 22) |

New-row quote check (`corpus/SOURCES.md` S876–S880): all five quotes in the lesson are ≤25 words and located; S878 (24) and S880 (25) are at/near the cap and found in source. Row quote cells in SOURCES.md are consistent with the Gate quotes. `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama` → exit 0.

7 of 7 sampled gate decisions (5 admits, 2 reject families) agreed; zero disagreements.

## 5. Trend verdicts
- **expansion: improved** — two admitted entries on ground absent at base (0 files), citing five rows mined this round (S876–S880, all re-opened above). Caveat the lane states: base+amendment is one ground.
- **quality: unchanged** — no pre-existing entry re-verified, deepened or superseded; wave-2 repairs concern this round's own entries (lesson `## Corrections`). Not harmed: the false statements wave-2 found in the new amendment were repaired in the committed head.
- **discernment: improved** — outside spot-check agrees with the gate on all sampled admits and rejects, and QUALITY 22/23/24 each cite a `## Mistakes`/Corrections lesson (R73-M3, counter-receipt, CDX control) — the "grounded criterion behind a lesson" condition of LEARNING.md. (The lane's own "unchanged" is a self-assessment made before this check.)

## 6. Routed defects (lane must fix next round)
1. Commit or discard the five modified + one untracked `.ufo/waves/round-73/w2/*` seat files; stop seats writing after the push; record what `RevengerOrigins.md` holds.
2. Commit a PASS-at-lands receipt for ACCEPT-C-73 and ACCEPT-CA-73 under `reports/round-73/telemetry/` (today only FAIL controls are committed; PASS lives in seat reports).
3. Reconcile "Ca 9 scenarios" (report/LOG) with `SELFTEST OK: 10 scenarios`; the `ERROR: base … not a commit` stderr line in `selftest-r3.txt` should be labelled as the control's expected output.
4. Counter hardening routed by the lane itself (junk landings pass 11/11, config read from graded tree, ledger constant-printers, SEPARABLE wider than frozen wording) — due round 74; frozen predicates stand this round.
5. The README footer lines `:732`/`:736`/`:407` still read 243/36 by append-only design; the later footer `:775` is the live value — any census reader must take the last footer.

## 7. SHONEN
The report marks all four boxes `[~]`. With this non-author verification on record the boxes look checkable by a non-author at closure for operator consideration (promotion remains operator-owned; nothing was written into `SHONEN.md`).
