author: hyaku closure (non-author integrator, @m_zfl)

# kotodama round 97 — non-author verifier spot-check

Base `1ffc5a83d2c70e3bc581594efbcf32c562ba2569` → freeze `24eac1e91688d8aa0696a07eff17beeacd407763` → lane HEAD
`fc5ba047df8a3baf7159a3d7cdfa1b72fc14768e` (branch `main`).
Report `.ufo/reports/round-97/kotodama.md` (fleet commit `eb616de6f27165fc9adcad14492496dbc756356e`).
Driver digest (copied from `.ufo/watchdog.log`):
`2026-11-05T19:21:19-03:00 launch kotodama round=97 pgid=531026 driver=hyaku-inline attempt=1` /
`2026-11-05T22:10:44-03:00 complete kotodama round=97; hyaku-inline attempt=1`.
All measurements below were re-run by this closure on 2026-11-05 over the committed bytes at `fc5ba047`
(the lane working copy is clean, `tracked=0 untracked=0`, so the tree equals the commit). Scratch for
re-opened sources: `~/.hyaku-scratch/closure-kotodama-r97/` (not evidence; the commands are).

## 1. Step-1 conformance

| check | command | observed | result |
|---|---|---|---|
| report landed by lane identity | `git log --format='%an %H %ad' -- .ufo/reports/round-97/kotodama.md` | `kotodama-shokunin eb616de6… Thu Nov 5 22:09:44 2026 -0300` (before the 22:10:44 complete line) | pass |
| prompt committed | `git log -- .ufo/prompts/kotodama-round-97.md` | `kotodama-shokunin 7f4a36b6… 19:20:48` (before launch 19:21:19) | pass |
| `SHONEN` heading, one line per box | report §SHONEN | 4 lines, all `[~]` + pointer | pass |
| cited hashes exist and are ancestors of `main` | `git cat-file -t <h>`; `git merge-base --is-ancestor <h> main` for 1ffc5a83, 24eac1e9, fc5ba047 | `commit` ×3, ancestor ×3 | pass |
| pushed, no leftovers | `scripts/hyaku/jj-lane.sh state <lane>`; `git status --porcelain`; `git ls-remote origin refs/heads/main` | `local=remote=fc5ba047… ahead=0 behind=0 tracked=0 untracked=0`; porcelain empty; remote `fc5ba047…` | pass |
| prompt carries template contract | `grep -n` over the prompt | §1 MISSION/AXES binding + 1–3 claims + lowest axis; §2b frontier step; §3 L2 floor (≥8, one batched swarm); §4 report path `.ufo/reports/round-97/kotodama.md`, SHONEN, hash citation; §5 commit-then-push, push scope, L0 side channel; write scope item 3 | pass |
| frozen counter and claims unchanged after freeze | `git diff --stat 24eac1e9 fc5ba047 -- reports/round-97/{predispatch.py,claims.json,sweep-control.py}` | empty | pass |

Not a marker: the report names real committed round work. Status `ok`.

## 2. Claims

### Claim O — operability (grader v8 → v9) — evidence-verified (lane gate) + re-measured shas

The O legs rest on the lane's own grader selftest, battery and mutation drivers; per PROTOCOL §Gate standard
(Closure consequence) this closure did not execute them and verified their committed evidence instead.

- Tool sha re-measured: `sha256sum tools/check-advance-evidence.py` → `1021dc9d…5717b`;
  `git show 1ffc5a83:tools/check-advance-evidence.py | sha256sum` → `f29ab013…bcd9c0` (v8). O0 holds.
- Pin = driver = receipt, re-measured: `cat reports/round-97/controls/{battery97,mutants97}.sha256` →
  `79efb67c…fb94c`, `f9c623fd…22259`; `sha256sum` of `.ufo/waves/round-97/w1/stage/ExecBattery97/battery97.py`
  and `…/MutationTester97/mutants97.py` → the same two values; first line of `battery97-control-v8.txt` is
  `BATTERY-SHA256 79efb67c…` with `TOOL-SHA256 f29ab013…` (v8) and `BATTERY-SUMMARY survivors=7 unnamed=0 refused=24`
  (CR1, US1, OGH1, IS1, NUL1, CM1, CMW2 each `outcome=SURVIVOR`); first line of `mutation97-first.txt` is
  `DRIVER-SHA256 f9c623fd…`, `TOOL sha256=1021dc9d…`, `MUTATION-SCORE: 121/121 killed, 0 survived, 0 broken-pattern`.
- Committed v9 evidence: `stage/ExecGraderV9/selftest.txt` `SELFTEST PASS 155/155`; `battery-v9.txt`
  `BATTERY-SUMMARY survivors=0 unnamed=0 refused=31 traceback=0`; `critic96-on-v8.txt` `CRITIC-O96 survivors=7 … refused=12`.
- O4 re-measured: `grep '^REG' reports/round-95/controls/reg-v5.txt | sort` (34 lines) vs the REG lines of
  `battery-v9.txt`: `comm -23` prints 0 missing.
- Frozen-run verdict: `reports/round-97/predispatch-lands.txt` names tool sha `1021dc9d…` and prints
  `PREDISPATCH-97: PASS legs=13/13 rc=0`; the base control prints `FAIL legs=4/13` (O0–O4 all FAIL); ReviewerO97
  (`stage/ReviewerO97/review.md` lines 18–20) records the same O legs independently.
- Attack on v9: CriticO97 (`stage/CriticO97/attacks.md`) leaves 8 survivors on v9 where v8 leaves 19 of the same 28
  fixtures; that is residual surface routed to round 98, not harm.

Verdict: **improved** (every frozen O target met; re-measured shas agree with the reported values).
Observation: the battery and mutation pins land in the round commit `fc5ba047`, not at the freeze, so "control
receipt taken before any v9 byte existed" rests on seat mtimes checked by ReviewerO97, not on commit order. The
receipt's own `TOOL-SHA256` is v8, so the 7/0/24 measurement is valid either way. Status-neutral.

### Claim C — coverage (verbal duelling and ritual insult) — re-measured

| leg | command (lane root) | observed | reported | agree |
|---|---|---|---|---|
| C1 | `wc -c` / `grep -c '^## '` on the entry; `grep -i '^## ' \| grep -ic <phrase>` per frozen phrase; `grep '^- topic:'` | 36739 B; 13 h2; each of the 6 phrases in one h2; topic line present and equal to `claims.json` `frozen_topic` | 36739, 13, 6/6, equal | yes |
| C2 | `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` at fc5ba047 and at 1ffc5a83; highest id by `sort -V` | 917 / 908; highest S993; S985–S992 tier A×7 + B×1 (S988), `mined`, opened `2026-11-05`, used-by exactly the entry | 917, S993, 8 qualifying | yes |
| C3 | `git diff 1ffc5a83 fc5ba047 -- corpus/SOURCES.md`, count `^-` / `^+` content lines | removed 0, added 9 | 0 / 9 | yes |
| C4 | `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama` | rc 0, `ok`; only legacy W01/W04 warnings on S127–S928, none on S985–S993 | rc 0 | yes |
| C5 | `grep -n verbal-duelling corpus/README.md`; `## linguistics/ (42)` | index row line 404 + section prose line 1078; 269 `.md` under `corpus/knowledge` (`ls -R \| grep -c '\.md$'`) | 269/269/0 | yes |
| C6 | `grep -c <id>` on the entry | S985 10, S986 4, S987–S992 3 each | 8/8 | yes |
| C7 | `ls reports/round-97/evidence`; manifest check (every `captures[].file` and `quote_capture` exists and its sha256 matches) | 16 capture files for S985–S993; 9 entries, 11 captures, 0 bad | 8/8 | yes |
| C8 | `grep -rniE '<six phrases>' corpus/knowledge \| grep -v <entry>` restricted to `- topic:` or heading lines | 0 owner lines (2 other files mention a phrase in body prose only) | owners 0 | yes |

Repaired text sampled (the report asked the closure to): S986 quotes at entry lines 95 and 97 each count 1 in
`reports/round-97/evidence/S986.txt`, and the capture continues "…carried on for years, just for the fun of it"
and "He who is most heartily applauded is 'winner'", which support the repaired "years" and applause-verdict
sentences. The funerary S993 sentence (`funerary-lament-dirge-formulae.md` line 70): both quotes count 1 in
`S993.txt`, and the capture reads "the modern Maniat thrínos holds no association with professional mourners;
nevertheless, highly skilled mourners are often given prec[edence]", which supports "skill earns precedence, not a
fee". Agree with the repairs.

Verdict: **improved**.

### Owned axes not claimed

- adjacency: **unchanged**. Re-measured 8-gram overlap (lowercased `\w+` tokens) of the entry against
  `corpus/knowledge/linguistics/oath-blessing-curse-formulae.md`: 35 shared of 6178 (reported 35 of 6181; the
  denominator differs by tokenizer). The copied boundary prose was removed before landing; no harm.
- depth: **unchanged** (one sourced sentence added to the lament entry; supported, see above).
- freshness: **unchanged** (paused by open L0 round-11 and round-89 questions; lowest-axis obligation neither met
  nor waived, stated honestly in the report).
- calibration: **unchanged** (criterion 39 is grounded in R97-M1 and its able-to-fail control
  `reports/round-97/sweep-control.txt` prints `R96-REPLAY … owners=2`; the author's `[~]` SHONEN marks and SCORECARD
  rows match the measured state).

`git diff 1ffc5a83 fc5ba047 -- SCORECARD.md` is append-only (a round-97 axes section, a capabilities addendum and a
round-98 plan); no axis row is lowered.

## 3. Discernment spot-check (`corpus/lessons/round-97.md` `## Gate`)

| item | decision | re-opened source | agree/disagree | reason |
|---|---|---|---|---|
| S987 Bellows, *Lokasenna* (Wikisource) | admit, tier A | `curl -sL 'https://en.wikisource.org/wiki/The_Poetic_Edda_(tr._Bellows)/Lokasenna'` → 200, 307750 B; tag-stripped, whitespace-normalised count of the 20-word quote = 1 | agree | the public-domain translation is the primary text for the senna scope; the quote grounds `teaches` |
| S991 Nadera & Mooney-Singh 2019 (SARE) | admit, tier A | `curl -sL https://ojie.um.edu.my/index.php/SARE/article/download/19055/10299` → 200, PDF 19 pp; `pdftotext`, quote count = 1 | agree | peer-reviewed article, primary for the balagtasan scope; the row bounds the lakandiwa role to the Philippines |
| S992 Nicholson 1907 (Gutenberg #37985) | admit, tier A | `curl -sL https://www.gutenberg.org/files/37985/37985-0.txt` → 200, 1203657 B; quote count = 1, context continues "…superior to his rival.[454]" | agree on admit; disagree on tier | admission is sound and the quote is exact, but a 1907 literary-history survey is a strong secondary (CORPUS tier B: "survey, textbook"), not primary for the naqāʾiḍ's partisan audience; the row's own `teaches` calls it "secondhand" |
| Labov, "Rules for ritual insults" (Springer chapter page) | reject | `curl -sL https://link.springer.com/chapter/10.1007/978-1-349-25582-5_37` → 200, 228734 B; raw counts 6 and 5 for the two preview spans (visible text 2 and 2); `https://www.ling.upenn.edu/~wlabov/WL.BIB.pdf` → 403, 118 B | agree | no unique ≤25-word span exists on the opened page, and only a publisher preview was reachable; the flip condition (an authorised open copy) is the right one |

New `corpus/SOURCES.md` row re-opened: S991 (line 948). Its anchor quote "Balagtasan is an indigenous form of
competitive Filipino debate poetry in the Tagalog language" is 14 words (≤25) and counts 1 in the re-opened PDF.
Gate-table capture hashes match `sha256sum reports/round-97/evidence/*` for all nine rows (S993's value is the PDF's).

Census: `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama` → rc 0.

## 4. Trend verdicts

- **expansion: improved.** A surface with no topic or heading owner at base (C8 re-measured 0) now has an admitted
  entry citing eight `mined` tier A/B rows opened this round; census rc 0.
- **quality: unchanged.** No entry was re-verified or superseded as a claim. The sampled repaired sentences and the
  lament addition are supported by their captures, so no admitted entry fails its re-check.
- **discernment: improved.** The spot-check agrees with the gate on 3 admits and 1 reject. Criterion 39 is grounded
  in a mined mistake and shown able to fail. The one disagreement is a tier grade (S992 A → B). It does not change
  admission and is routed below as a lesson for round 98.

## 5. Routed defects (lane fixes next round)

1. S992 tier: the row grades a 1907 survey tier A. Append a superseding row or log the tier change old→new in the
   round-98 lesson per SOURCES rule 2. If tier is an append-only cell, supersede rather than edit.
2. Pin timing: freeze the battery/mutation pin files in the freeze commit (or a commit before any v(N+1) byte) so
   the control-before-candidate order is shown by commit order, not mtimes.
3. Gate-table hash column: name the capture file each hash refers to (S993's hash is the PDF while the quote is
   counted in the `.txt`).
4. Report detail: "manifest repointed… (30 fields, all resolved)" does not match the manifest's 11 `captures[].file`
   + 9 `quote_capture` fields. State the counting command.
5. Carried from the report: CriticO97 v9 survivors (ENC1 U+20DD, DEL1 U+007F, non-ASCII heading numbering) and the
   sentence-support sweep of the round-96 oath entry.

SHONEN: boxes 2 (end-to-end task logged, `LOG.md` round 97 + `.ufo/waves/round-97/w1/`) and 3 (instructions
executable: frozen counter 13/13 committed, selftest 155/155) look checkable by a non-author. Promotion is
operator-owned; no box is marked here.
