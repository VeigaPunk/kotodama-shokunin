# Round-64 verifier spot-check (kotodama)

author: hyaku closure (non-author integrator, @m_kfc)
date: 2026-10-24
lane HEAD judged: 8bab271c691c6b1006da95316a24ae1958ec01e2 (base 097c21d0eba5023cfd38b767fb41d59409eef125, grand base ff30a205)
report: .ufo/reports/round-64/kotodama.md (committed by lane identity kotodama-shokunin, e1fe5c97)

## 1. Conformance (step-1)

| check | command | observed | result |
|---|---|---|---|
| report author | `git log --format='%an %H' -- .ufo/reports/round-64/kotodama.md` | `kotodama-shokunin e1fe5c973…` | pass |
| SHONEN heading | read | `## SHONEN`, 4 boxes each one line, all `[~]` (no `[x]` claimed) | pass |
| cited commits exist + ancestor of `main` | `git merge-base --is-ancestor <h> main` for 6f3e0b24, 95c9194e, 8bab271c, 097c21d0, ff30a205 | all exit 0 | pass |
| lane pushed / no uncommitted work | `scripts/hyaku/jj-lane.sh state …` ; `git status --porcelain` | `ahead=0 behind=0`, head=detached (jj-colocated, expected), porcelain empty | pass |
| prompt contract | diff of `.ufo/prompts/kotodama-round-64.md` §§1–5 vs `templates/round-prompt.md` | differences are template-variable substitutions only; §6 hyaku addendum present | pass |

Dispatch digest (watchdog): launches 19:43:56 / 19:48:07 / 19:57:24 / 20:17:55 / 20:33:32 / 22:40:27 all attempt-tagged, attempts 1–4 died to orchestrator freezes/dispatch error (zero lane progress each); attempt 1 of launch 5 completed 2026-10-24T00:47:04-03:00. Inherited work re-verified by the landing L1; no marker-report predicate involved.

## 2. Per-claim re-check

### Claim C (coverage, sourced) — re-measured independently; gate receipt evidence-verified (counter not executed)

| reported | my measurement | result |
|---|---|---|
| corpus 237→238 | `git ls-tree -r --name-only <rev> -- corpus/knowledge \| grep -c '\.md$'` → 237 @ff30a205, 238 @8bab271c | match |
| linguistics 29→30 | same over `corpus/knowledge/linguistics` → 29→30 | match |
| registry 643→675, +32 rows | `grep -c '^\| *S[0-9]' corpus/SOURCES.md` → 643 @ff30a205, 675 @HEAD; 32 rows S718–S749 (26 mined S718–S743 + 6 disposition S744–S749) | match |
| entry 26 bullets, one S-id each, S718–S743 | 26 bullets, 26 distinct S-ids, exactly S718–S743 | match |
| NOHARM = exactly the new file | counter NOHARM line `diff=['corpus/knowledge/linguistics/language-socialization-and-acquisition.md']`; `git diff ff30a205..8bab271c --stat -- corpus` touches only README/SOURCES/new entry (34++ 1− on SOURCES = 32 appends + S687 line) | match |
| S687 flip mined→queued logged old→new | base row `mined` → HEAD row `queued`, otherwise byte-identical; lesson L321/L508 + LOG record old→new | match |
| ACCEPT-C-64 PASS 11/11 @95c9194e | receipt `final-measures-c.txt` committed: 11 PASS legs, `measured revision: 95c9194e` (entry/SOURCES legitimately committed there — attribution sound), counter sha 979050ce… matches HEAD bytes and report | verified (evidence) |
| census exit 0 | ran `scripts/sources-census.sh validate --root … kotodama` myself → `kotodama ok`, exit 0 (pre-existing W04 duplicate-URL warnings only) | match |
| base ownership 0 filename/topic-line owners | `git grep -il 'socialization\|socialisation' ff30a205 -- corpus/knowledge` → 3 incidental mentions (hopi, dialect-register-consistency, linguistic-anthropology), no owner entry; README topic lines at base own gesture/shift/sacred-registers, not this topic | plausible, match |

### Claim O (operability, counter hardening) — evidence-verified per §Gate standard (no counter executed)

| reported | observed (seat + integrator) | result |
|---|---|---|
| r63 counter 0 EDGE_/DRIP legs | `git show 097c21d:reports/round-63/accept-o.py \| grep -c 'EDGE_\|DRIP'` → 0 | match |
| counter rev5 `cdee063e…` | `sha256sum reports/round-64/accept-o.py` at HEAD = cdee063e… | match |
| PASS 23/23, MUT bad=[] mutants=10, m5 isolation | `final-measures-o.txt` committed: 23 PASS legs in claims.json order, `MUT PASS bad=[] mutants=10`, m5 `EDGE_SCHEMEREL PASS / EDGE_SLASHLESS FAIL`, `ACCEPT-O-64: PASS`, exit 0; sha256 `8e5c7ade…` and independent copy `-rev5.txt` `1cb15569…` both match committed bytes | verified (evidence) |
| red rev4 receipt | `final-measures-o-rev4.txt` committed: `MUT FAIL`, `ACCEPT-O-64: FAIL`, exit 1 (uncompilable m5 caught pre-data) | match |
| do-nothing control | `control-o.txt` committed: docstring-only tool patch, GEN green, MUT all die | match, caveat R5 |
| tool byte-equal to base | `tools/reopen-row.py` sha c0f10a84… at ff30a205 = 097c21d0 = HEAD; diff empty | match |

### Claim Ca (calibration, bookkeeping) — substance re-measured at HEAD; receipt defective in attribution (H1)

All seven round-63 routed repairs are present at HEAD and independently spot-replayed by me:
histogram leg: `A=13 B=11` for S694–S717 at base (matches the correction; S702 tier B docs) — PASS. PTRS leg targets `final-measures-o.txt`, `final-measures-c.txt`, `rev-separability.txt` all exist at HEAD — PASS. CANONLOG leg: root LOG.md has the Round-64 entry — PASS. w1/ReviewerCa.md (141 lines, seven-row re-derivation), w2/CaReceipts.md, w2/RevVerifyCa.md all committed.

**H1 (routed):** `final-measures-ca.txt:2` stamps `measured revision: 95c9194e`, but at that revision the receipt's own legs fail — verified: `git show 95c9194e:LOG.md | grep -c '## Round 64'` → 0, `git show 95c9194e:SCORECARD.md | grep -c 'Round-63 corrections'` → 0 (records committed 17 min later in 8bab271c, 00:45:02 vs receipt run 00:28:55). The run happened over a worktree with uncommitted records; the receipt bytes correspond to HEAD state (independent replay reproduces its detail strings exactly at 8bab271c: 7/7 PASS). Protocol §Gate standard: "a verdict names the revision it was measured against: a run over a moving worktree is not comparable to one over the cited commit." The stamped revision is false — same class as routed defect 8, inside the receipt that closes defect 8. Substance of the claim (repairs done, leg-verified) is true at HEAD; the attribution is not. Routed records-only correction (R1).

## 3. Per-axis verdicts

| axis | verdict | basis |
|---|---|---|
| coverage | improved | independent re-measurement (table C above) + census exit 0 + Gate admits hold under re-open |
| operability | improved | counter pins committed, receipts + red receipt + control committed, tool byte-equal; F1 wording routed (predicate unaffected) |
| calibration | improved | seven repairs present and leg-verified at HEAD; H1/M1 attribution defects routed, disclosed-not-hidden |
| depth / freshness / adjacency | unchanged | no derivations claimed; freshness pause respected; SCORECARD row consistent |

## 4. Discernment spot-check (LEARNING.md — non-author sample)

| item | decision | re-opened source | agree/disagree | reason |
|---|---|---|---|---|
| S718 (Gate admit, tier A) | admit | live curl `http=200`, PLOS ONE article identity confirmed; quote "Lebanese mothers, compared to American mothers, produced more IDS" verbatim 2× incl. named Results paragraph; 9 words ≤25 | agree | registry URL/quote/date byte-equal to Gate and row.txt; tier A fits peer-reviewed source |
| S730 (Gate admit, tier B) | admit | live curl `http=200`, Genesee & Nicoladis BFLA chapter PDF; quote verbatim on manuscript p.1; 24 words ≤25 | agree | handbook chapter → tier B honest; registry byte-equal |
| S744 (Gate reject) | reject | live curl `http=200` but serves Dictionary.com **khanka** (lake) headword after redirect; ushanka wording absent | agree | reject reason reproduces exactly; NOT-LOCATED annotation honest |
| S747 (Gate reject) | reject | live curl `http=403` Cloudflare challenge | agree | access-based reject stated as such; row carries no quote — confirmed 0 quoted words |
| S745 (corroboration, not sampled) | reject | `http=403` at merriam-webster.com/dictionary/tiara | agree | matches recorded evidence |
| SOURCES.md rows S718/S730 (new rows) | admit | same re-opens as above | agree | quote ≤25 words located at cited anchor; row ↔ Gate ↔ row.txt byte-equal |

Gate structure: 32 rows confirmed (26 mined + 6 disposition); 29 located-asserting + 3 NOT-LOCATED (S744/S745/S747) with verbatim re-open evidence; queued rows S746/S748/S749 re-opened LOCATED by the round. All four sampled decisions: **agree**.

## 5. Trend verdicts

- expansion: **improved** — 237→238 on previously unowned ground (independently re-measured), registry 643→675.
- quality: **improved** — frozen-predicate receipts committed for all three claims; blind-support ring findings (S719 hedge, S729 duplicate re-sourced, S739 re-anchored, S747 fabricated anchor removed) repaired with named evidence, not amended away; tier inflation corrected S721/S726/S737 → B.
- discernment: **improved** — the round disclosed its own blind spots pre-data (four counter revisions forced by receipts; R64-M1..M19 in the lesson); my non-author sample of 2 admits + 2 rejects all agree; honesty practices (NOT-LOCATED rows carry no quote; S747 zero-word anchor) hold under re-open.

## 6. Defects routed to the lane (round 65)

1. **R1 (HIGH, records-only):** re-stamp `reports/round-64/telemetry/final-measures-ca.txt` to `8bab271c` (or record "worktree dirty at run; read-path bytes = 8bab271c") and correct the three repeats: report line "After at `95c9194e`: ACCEPT-CA-64 PASS 7/7", `LOG.md` round-64 final-measures entry, `SCORECARD.md` Ca row measured evidence, `w2/LessonFinal.md`. Receipts must pin a tree hash of read inputs, not only the counter sha.
2. **R2 (MEDIUM):** `reports/round-63/telemetry/revisions.txt:12-13` still asserts `8d2041fa` added `final-measures-c.txt` — false (added by 0c892ce; path absent at 8d2041fa). Named correction entry, append-only.
3. **R3 (MEDIUM):** report cites `w2/ReviewerCa.md` — actual path `w1/ReviewerCa.md`. (SCORECARD cites both correctly.)
4. **R4 (MEDIUM, already self-routed by the lane, keep on queue):** `claims.json` O statement "ten byte-patched mutants each fail exactly their pinned leg" is contradicted by the lane's own `exactness-sweep-o.txt` (m1 also fails EDGE_USERINFO/EDGE_HTTPS; m2 also fails EDGE_MALTARG); frozen-predicate rule routes the wording; SCORECARD already states the honest version.
5. **R5 (LOW):** `control-o.txt` binds counter rev3 `c27a9fef…` / measured `b7d22703`, not final rev5 — the report does not state the binding; name it next round.
6. **R6 (LOW):** lesson R64-M12 wave-2 status sentence ("closed in the worktree, open in the index") is a pre-land snapshot; at HEAD the S687 flip is committed in 95c9194e. Append a status correction.
7. **R7 (LOW):** new entry's `verified-at: 2026-10-23` line still reads "skeleton structure prepared; cited source claims await L1 insertion" — stale after insertion; correct in round 65's entry touch or a named erratum.

## 7. SHONEN observation for the operator

All four boxes are `[~]` with concrete pointers and a named non-author review chain (closure spot-check this file). Promotion is operator-owned; nothing here mints or promotes. Boxes 3–4 (`[x]`) would require the operator's promotion decision — flag only.

## 8. Tool installs

None this session (integrator + 4 read-only seats used host git/curl/python3/pdftotext only; no installs).
