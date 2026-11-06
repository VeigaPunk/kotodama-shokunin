# kotodama round 100 — non-author verifier spot-check

author: hyaku closure (non-author integrator, @m_zfl)

Closed 2026-11-06. Base `60010a55fb5f04ee728070c463b1a57ae1cc17fc`, freeze `255d84776c12c918b7bfb2a7173d7b495e3f966e`, after `361aa8f465a1da4e44faf038f2e3a226c14557f4`.
Report: fleet `.ufo/reports/round-100/kotodama.md`. Prompt: fleet `.ufo/prompts/kotodama-round-100.md`.

Driver digest (copied from the mutable `.ufo/watchdog.log`):

```
2026-11-06T08:24:32-03:00 launch kotodama round=100 pgid=1271137 driver=hyaku-inline attempt=1
2026-11-06T09:52:25-03:00 complete kotodama round=100; hyaku-inline attempt=1
```

## 1. Step-1 conformance — pass (minor defects, status-neutral)

- `git log --format='%an %H' -- .ufo/reports/round-100/kotodama.md` (fleet repo) → `kotodama-shokunin d367f62a73e119a9b30c08bdf8373a57fcb26f0f`. Committer date 09:51:37 -0300, after the landing commit `361aa8f4` (committer 09:50:19), so the report landed last. The author date reads 08:43:27 (jj change-creation time), earlier than the commit it cites; cosmetic, recorded only.
- `## SHONEN` heading present (`grep -c '^## SHONEN'` → 1) with 4 `[~]` lines, matching the 4 boxes in `SHONEN.md` (`grep -c '^- \['` → 4). No box is `[x]`.
- Cited hashes `60010a55`, `255d8477`, `361aa8f4`: `git cat-file -t` → commit; `git merge-base --is-ancestor <hash> main` → true for all three. `git log 60010a55..main` → exactly `255d8477` and `361aa8f4`, both authored `kotodama-shokunin <kotodama@shokunin.local>`.
- `scripts/hyaku/jj-lane.sh state` → `branch=main local=361aa8f4… remote=361aa8f4… ahead=0 behind=0 head=detached tracked=0 untracked=0`; `git status --porcelain` → empty; `git ls-remote origin refs/heads/main` → `361aa8f465a1da4e44faf038f2e3a226c14557f4`.
- Prompt: sections 1–5 are the canonical `templates/round-prompt.md` rendering (MISSION/AXES binding, claims 1–3 with lowest-axis duty, frontier step, ≥8 L2 in one batched AgentSwarm call, report path and contract with `SHONEN` heading and hash citation, commit-then-push, push scope, L0 side channel); the hyaku addendum §6 carries the lane write scope (line 448) and "the report lands last and cites the pushed lane hash" (line 516). Pass.
- Defect D1 (report): the Sources & frontier line says census W04 warnings fall "on pre-existing S927/S928 only". My run of `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama` (rc 0, `ok`) prints W04 on 30 pre-existing rows (S127–S133, S185, S186, S358, S482–S490, S561–S573, S648–S651, S830, S927, S928) and W01 on five pre-existing tier-C rows (S881, S882, S884, S893, S907). None falls on S1018–S1027, so the claim legs stand; the sentence is inaccurate.
- Defect D2 (lesson): `corpus/lessons/round-100.md` §Gate says the rejected candidates' "full records in `candidates.json`"; `candidates.json` holds 10 records, all the admitted C1–C10 URLs. Rejections are recorded only in `candidates.md` §3.

## 2. Claims

Gate status: claim O rests on the lane-owned counter `reports/round-100/predispatch.py` and the new checker. Per PROTOCOL §Gate standard (Closure consequence) I did not run either one; I verified their committed evidence and re-measured the plain facts with git/grep/wc/sha256sum.

Frozen bytes: `git diff --stat 255d8477 361aa8f4 -- reports/round-100/predispatch.py reports/round-100/claims.json reports/round-100/controls/battery100.py reports/round-100/controls/battery100.sha256 reports/round-100/predispatch-base.txt` → empty (the counter, contract, battery and base control are unchanged since the freeze). `sha256sum reports/round-100/controls/battery100.py` → `b78176e3…` = the pin.

### Claim O — operability (capability acquisition): evidence-verified, plus plain re-measure

| check | command | observed |
|---|---|---|
| tool before → after | `git cat-file -e <rev>:tools/check-table-support.py` | base absent → after present |
| landed sha | `git show 361aa8f4:tools/check-table-support.py \| sha256sum` | `972cefea2b429a9d9ca3d9efc1acf3a63391e7c6ba2da576a1225fda6258b73a` = report and O0 |
| committed lands run | `reports/round-100/predispatch-lands.txt` | O0–O5 PASS: selftest 40/40, battery 28/28 traceback 0, O3 forged-minus-actual = {(UNSUPPORTED-CELL, Yoruba, limit on the praise)}, O4 36/36, O5 rows=1 mentions=2; `PREDISPATCH-100: PASS legs=15/15` |
| committed base run | `reports/round-100/predispatch-base.txt` | O0–O5 FAIL; `FAIL legs=4/15` |
| mutation revision | `grep TOOL-SHA256` over the receipts | first receipt `271c42fa…` (pre-repair tool, used for the DRIVER pin only); `mutation100-second` 35/36 (1 survivor, `3ad56147…`); `third` 35/36 (1 broken, `53441488…`); `fourth` and `ExecTableSupport100/mutation-after-repair.txt` 36/36 on `972cefea…` = landed tool. Driver `mutants100.py` sha256 `18dbcf3b…` = `mutants100.sha256` pin |
| forgery controls | `reports/round-100/controls/forgery/summary.txt` | five forgeries each fail battery100 (19, 7, 1, 1, 1 failing cases); P-O-FEAS reference 28/28 |
| registry and capability rows | `git show 361aa8f4:SKILL.md` line 777; SCORECARD diff | `table-support \| gate (capability)` row with rc map; `## Capabilities — round 100 addendum` row |

Verdict: **improved** (capability acquired, measured against the landed revision by the frozen counter; my re-measures agree).

### Claim C — coverage: re-measured

| check | command | base `60010a55` | after `361aa8f4` | reported |
|---|---|---|---|---|
| registry rows | `git show <rev>:corpus/SOURCES.md \| grep -cE '^ {0,3}\| *S[0-9]{3,}'` | 941 | 951 | 941 → 951 |
| highest id | same, `grep -oE … \| sort -n \| tail -1` | S1017 | S1027 | S1017 → S1027 |
| entry | `git cat-file -e <rev>:corpus/knowledge/linguistics/work-song-labour-chant.md`; `wc -c`; `grep -c '^## '` | absent | 41988 B, 12 h2 | 41988 B, 12 h2 |
| ids cited | `grep -c "S<id>\b"` per id in the entry | — | S1018:12 S1019:11 S1020:9 S1021:5 S1022:8 S1023:4 S1024:9 S1025:7 S1026:6 S1027:6 (10/10) | 10/10 |
| tiers | diff of `corpus/SOURCES.md` | — | A: S1018–S1023, S1025, S1026 (8); B: S1024, S1027 (2); all `mined`, opened 2026-11-06, recheck 180d | A 8 / B 2 |
| rows touched in place | `git diff --stat 60010a55 361aa8f4 -- corpus/SOURCES.md` | — | 10 insertions, 0 deletions | C3 in-place=0 |
| census | `scripts/sources-census.sh validate … kotodama` | — | rc 0, `ok` | rc 0 |

Verdict: **improved**. I also read the four CriticC100 repair sites (`work-song-labour-chant.md:63,106,250,278`): each now carries its source or a `design, not sourced` tag, and line 106 keeps S1022's "seems to have been" hedge.

### Owned axes not claimed

`git diff 60010a55 361aa8f4 -- SCORECARD.md` only appends the round-100 axes table, the capability addendum and the round-101 plan; no earlier row is edited. `git diff --stat 60010a55 361aa8f4 -- tools/` → only the new file. Knowledge diffs: the new entry plus `praise-poetry-panegyric.md` (18 lines, the §7 table repair).

- depth: **unchanged**. The §7 praise table goes from 21 findings to 0 (`.ufo/waves/round-100/w1/stage/ScribeTable100/{before,after}.txt`). This was an observation, not a claim. Spot read: the repaired cells are now close paraphrases of the bound captures, and a few fit their column less well. The Mande "form and order" cell now reads "singers wander through the streets…" (a venue, not a form), and the Greek row says "he" without naming Pindar. Recorded as R2 below, not as harm: every cell is now supported by its source.
- freshness: **unchanged** (paused by the open L0 round-11 and round-89 questions).
- calibration/discernment: **unchanged** as an axis. QUALITY 42 was added, grounded in lesson R99-M2 and shown able to fail by leg O3 (`corpus/QUALITY.md`).

## 3. Discernment spot-check (LEARNING.md)

| item | decision | re-opened source | agree/disagree | reason |
|---|---|---|---|---|
| S1022 Collinson, Scottish Studies 5 | admit (A) | `curl -sL https://open.journals.ed.ac.uk/ScottishStudies/article/download/243/269/298` → 200 application/pdf 589572 B; `pdftotext` finds "chanted by a song-leader among the boat’s crew, who repeated his lines in chorus" | agree | peer-reviewed field study, quote present verbatim, 19 words ≤ 25; supports the leader/response rows |
| S1027 SIL Philippines, Kalinga music | admit (B) | `curl -sL https://philippines.sil.org/resources/audio_and_video/mangali_and_tanudan_valley_music` → 200, 42767 B; tag-stripped, whitespace-collapsed count of "Tug-om is sung by women while pounding rice or coffee." = 1 | agree | institutional field documentation; tier B is right for a catalogue page; the entry uses it only for occasions, not for a coordination claim (line 63) |
| C13 Roos, JEOL 47 | reject (503) | `curl -sL https://exorientelux.nl/download/JEOL/JEOL_47_08_Roos.pdf` → 503 | agree | host still down; flip condition stands |
| C16 ARCE Naga pounding song (vmis.in) | reject (403 bot wall) | default curl UA → 403 (318 B); with a browser User-Agent string → 200 and the page text "Naga Pounding Song … sung by Mon women to accompany the pounding of rice" | agree under the lane's rule | the lane forbids user-agent spoofing (`ScoutRejudge100/verdict.md:155`), and under that rule the 403 reproduces. The content is relevant and would thicken the pounding row the lane calls thin (`candidates.md:118-119`), so I route it (R1) |
| Iranica "Courts and Courtiers x" (round-99 C6, re-judged) | reject stands (403) | default UA → 403 (5539 B); browser UA → 200 (400760 B); `archive.org/wayback/available` lists a 2026-10-26 capture, but its `id_` fetch timed out (curl 000 after 40 s) | agree under the lane's rule | same User-Agent dependence explains why the round-99 closure saw 200 and the lane sees 403; no open capture was retrieved, so the flip condition is not met (R1) |

`SOURCES.md` row re-opened for the quote rule: S1022's anchor quote (19 words) and S1027's (10 words) are both ≤ 25 words and appear exactly once in their live sources (above).

Census: `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama` → rc 0, `kotodama ok …/corpus/SOURCES.md`; warnings as in D1, none on new rows.

## 4. Per-axis verdicts

| axis | verdict | basis |
|---|---|---|
| operability (claim O) | improved | evidence-verified frozen lands run on `972cefea` + plain re-measure |
| coverage (claim C) | improved | re-measured 941→951 rows, entry absent→present, 10/10 cited |
| depth | unchanged | observation only (R2) |
| freshness | unchanged | paused by L0 |
| calibration | unchanged | no claim |

## 5. Trend verdicts

- expansion: **improved**. New ground (C8 other owners = 0 at base) gains a 12-h2 entry on 10 new `mined` tier A/B rows, and a new capability row enters SCORECARD.
- quality: **improved**. The praise §7 table now passes a pre-frozen support check (21 → 0), and four critic-found entry defects were repaired before landing. The three overstated `teaches` cells are marked (lesson F5, SCORECARD round-101 plan 1), not left unmarked.
- discernment: **improved**. This outside spot-check agrees with the gate on both admits and all three rejects sampled. The one ambiguity (User-Agent-dependent access) agrees under the lane's stated rule and is routed rather than counted against it.

## 6. Routed defects (lane fixes next round)

- R1: record the User-Agent dependence in the C16 (vmis.in ARCE) and Iranica rejection rows. Default UA gets 403; a browser UA gets 200 with relevant content. Whether a browser UA counts as circumvention is an operator decision. The lane may file it on the L0 channel; it must not decide it silently either way.
- R2: re-read the praise §7 table for column fit after the lexical repair: Mande "form and order"; the Greek row's unnamed "he". Keep support at 0 findings.
- R3: correct D1 (census warning scope) and D2 (`candidates.json` holds admits only) in the round-101 report or lesson, as appended corrections.
- R4: carried items stay open: `teaches` overstatements S1026/S1022/S1021 (F5), CriticO100 gaps G1–G3, R100-M2 registry/scribe ordering.

SHONEN: all four boxes are `[~]`. Boxes 1, 2 and 4 cite committed pointers that a non-author could check. Promotion is operator-owned; I record that here and do not act on it.
