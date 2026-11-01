author: hyaku closure (non-author integrator, zcode subagent (fresh session, non-author))

# Round 81 verifier spot-check — kotodama (closed 2026-11-01, non-author closure judge)

Lane tip graded: `d89c96b6eef853ff5ae2d8ed5dba99d8557f1ea4` (branch `main`, pushed).
Base: `1c0e3d4d712da2fae25d27ece1eb799d26db0975`. Report:
`.ufo/reports/round-81/kotodama.md` (fleet repo commit `f84c495e716219677411d59671555d34905a8d87`,
author `kotodama-shokunin <kotodama@shokunin.local>`). This file is written by the
closure judge; the orchestrator commits it. Verdict: **admitted** — all three
claims verify and no owned axis is harmed. One status-neutral routed defect on the
C counter's REDRUN replayability (last section).

## 1. Step-1 conformance

| check | command | observed | result |
|---|---|---|---|
| report committed by lane identity | `git -C <fleet> log --format='%an %ae %H' -1 -- .ufo/reports/round-81/kotodama.md` | `kotodama-shokunin kotodama@shokunin.local f84c495e716219677411d59671555d34905a8d87` | PASS |
| `SHONEN` heading | read of the report | `## SHONEN` present; four `[~]` lines, each with resolvable pointers; no `[x]` written by the lane | PASS |
| cited lane commits exist and are ancestral | `git -C <lane> rev-parse --verify <c>^{commit}` + `git -C <lane> merge-base --is-ancestor <c> refs/heads/main` for all 12 cited commits (`316641d8`, `b1ebb609`, `d38135d6`, `d284058f`, `1ede6961`, `4ad08c83`, `d583ccae`, `c9dd27a1`, `427c627a`, `4de196ef`, `4ceccc51`, `d89c96b6`) | 12/12 `ANCESTOR-OK` | PASS |
| lane tip pushed | `git -C <lane> ls-remote origin refs/heads/main` vs `git -C <lane> rev-parse refs/heads/main` | both `d89c96b6eef853ff5ae2d8ed5dba99d8557f1ea4` | PASS |
| round work inside dispatch range | `git -C <lane> log --format='%h %an %s' 1c0e3d4d712d..d89c96b6eef8` | 12 commits, all `kotodama-shokunin`, all the round's cited work | PASS |
| dispatch digest | watchdog record per closure contract | launch `2026-11-01T03:40:33-08:00 launch kotodama round=81 base=1c0e3d4d712d`; complete `2026-11-01T08:06:41-08:00 complete kotodama round=81 head=d89c96b6eef8 pushed=True` | PASS |

## 2. Claim re-checks (all re-measured/re-run by this judge; none taken on the lane's receipt alone)

### Claim O — operability: W2 mutation pass + replace-ref builder re-runnable (commit `d284058f`)

- Before (re-measured): `git -C <lane> ls-tree -r --name-only 1c0e3d4d712d -- reports/round-80 | grep -cE 'mutants/|replacerefs.*build-fixture'` → `0`.
- After (re-measured): both files in the tip tree; extracted bytes hash-match the frozen pins exactly
  (`w2-mutants.py` sha256 `048f1c749ff2d05726a95936ff54a4d0919ce478c0e1256d31d057bf32f0af85`;
  `build-fixture.py` sha256 `aaefc36698cb2cfecdd2e2e98e6af0239d91ec119fec1e85f45406bf1bb3fbe6`).
- Counter re-run by this judge (scripts extracted from `d89c96b6` bytes; scratch workdir only):
  `python -I -B reports/round-81/accept-o81.py --root <lane> --lands d583ccae9a8f999a2428ea94d033293f760265cc --freeze d583ccae9a8f999a2428ea94d033293f760265cc --work <scratch>`
  → `LEG PASS` ×6, **`ACCEPT-O-81: PASS legs=6/6`, exit 0**. The MUTRUN leg re-derived
  `W2-RERUN: PASS 5/5 (clean green first)` live (m1/m3 byte-exact r80 shas re-frozen) and the FIXRUN leg
  re-derived `REPLACEREFS-FIXTURE: PASS (old PASS pairs=1 / hardened REFUSED refs/replace)` live.
- Selftest re-run by this judge: `python -I -B -X utf8 accept-o81.py --selftest --work <scratch>` →
  `SELFTEST-O81: PASS (6 checks)` (matches `telemetry/selftest-o81.txt`; counter sha `3da4dfcb…`).
- Host note: the selftests need `-X utf8` on this host (fixtures write 「」 quotes; the lane's receipts
  were produced under a UTF-8 session). Graded counter runs are unaffected.
- Verdict: **improved**.

### Claim C — calibration, capability acquisition: `tools/check-orphan-evidence.py` (commits `1ede6961`, `c9dd27a1`)

- Before (re-measured): `git -C <lane> ls-tree --name-only 1c0e3d4d712d -- tools/ | grep -c orphan` → `0`.
- After (re-measured): tool at tip; extracted bytes sha256
  `e99658dffdc6421396e10c65a73488500d53305ae63c19235352752b6b5a7045` = the frozen `tool_sha256`.
- Red-before kept: `reports/round-81/telemetry/orphan-sweep-red.txt` (landed first in the carry-in
  commit `316641d8`): 3 × `ORPHAN-ABSENT`, `ORPHAN-EVIDENCE: 3 orphan(s) over 510 cited path(s) in 103 report(s)`,
  lane HEAD at run = base, checker sha = the frozen pin. KEPT.
- Red/green demos run by this judge: (red, live fleet) exactly the 3 frozen orphans named, all
  `ORPHAN-ABSENT`, exit 1 — `corpus/knowledge/a.md`,
  `corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-24-r13.md`,
  `reports/round-63/telemetry/final-measures.txt`; (green, synthetic fixture in scratch: both cited
  paths committed) `ORPHAN-EVIDENCE: 0 orphan(s) over 2 cited path(s) in 1 report(s)`, exit 0;
  (red, synthetic: one cited path dropped from lane HEAD) `ORPHAN-ABSENT`, exit 1.
- Checker selftest re-run by this judge: `python -I -B tools-extracted/check-orphan-evidence.py --selftest`
  → 11 checks, `SELFTEST: PASS`, exit 0.
- Counter: committed receipt `telemetry/lands-c81-graded-r3.txt` (`ACCEPT-C-81: PASS legs=6/6` at lands
  `c9dd27a10b7702e386e9a84a9b5bf3793928170f`, freeze `d583ccae…`) is evidence-verified; counter bytes
  re-run by this judge: selftest `SELFTEST-C81: PASS (6 checks)` (sha `d77aa100…` matches
  `selftest-c81-r2.txt`), and the graded run re-executed at the same lands/freeze re-derived 5 of 6 legs
  green with REDRUN failing only on the summary-line pin — see the routed defect below. The orphan set,
  the classifications and the exit code (the claim's substance) re-derive exactly.
- Dispositions verified against their cited sources: round-68 fleet report line 10 says the frozen
  fixture "never creates `corpus/knowledge/a.md`" (fixture-hypothetical, never an evidence file);
  `reports/round-79/corrections/ca79-r78-s884.md` exists at tip and bounds the S884 r13 drift; the r63
  split receipts `final-measures-o.txt`/`final-measures-c.txt` exist at tip and the dead
  `final-measures.txt` path survives only inside the r63 spot-check's own defect record. Zero
  ORPHAN-ONDISK — honest; nothing fabricated.
- Verdict: **improved**.

### Routed defect R81-V1 (status-neutral, fix next round): the C counter's REDRUN summary pin ages immediately

The REDRUN leg requires the fresh sweep's summary line to equal the frozen
`ORPHAN-EVIDENCE: 3 orphan(s) over 510 cited path(s) in 103 report(s)`. At closure the same sweep
answers `ORPHAN-EVIDENCE: 3 orphan(s) over 522 cited path(s) in 104 report(s)` — the orphan set,
classifications and exit code are byte-identical to the frozen set, but the scan population grew by
exactly the round's own landed records: the round-81 fleet report (the 104th document, committed
after the lane's graded r3 run) cites 12 new lane-side paths (the entry, the lesson, the three
counters, `claims.json`, the checker, the red receipt, the dispositions record, the builder, the
generator, one graded receipt), all `OK-COMMITTED`, zero new orphans. The lane's own r3 receipt
honestly names its measured revision (`# measured revision (lane main): c9dd27a1…`), so this is not
a misreport — but a frozen counter whose leg pins a live mobile-surface count is not replayable at
closure. Route: next time a C-shaped counter is issued, pin the summary modulo population (orphan
set + exit code + classification) or re-freeze the summary at the closure-time counts. The monitor
itself stays red-by-design while the 3 disclosed orphans stand.

### Claim D — depth: ordeal/judicial-proof entry (commit `4ad08c83`)

- Before (re-measured): knowledge files at base `254`; `git ls-tree -r --name-only 1c0e3d4d712d corpus/knowledge | grep -ciE 'ordeal|judicial-proof|compurgat|wager-of'` → `0`; SOURCES rows at base `824`
  (`grep -cE '^\|\s*S[0-9]{3,}\s*\|' corpus/SOURCES.md` on `git show 1c0e3d4d712d:corpus/SOURCES.md`).
- After (re-measured): `255` files at tip; entry in tree; rows `827` at lands `4ad08c83` and at tip.
- Counter re-run by this judge: `python -I -B reports/round-81/accept-d81.py --root <lane> --lands d583ccae9a8f999a2428ea94d033293f760265cc --freeze d583ccae9a8f999a2428ea94d033293f760265cc --work <scratch>`
  → `LEG PASS` ×7, **`ACCEPT-D-81: PASS legs=7/7`, exit 0**. ENTRY sha `8871cf94…` matched;
  LINT re-ran the pinned `tools/check-cited-lines.py` on the entry: `CITED-LINES: 0 finding(s) in 1 file(s)`;
  ROWS verified S901/S902/S903 kind/tier/status `mined`/opened `2026-11-01`/used-by the entry, 「」
  quotes ≤25 words (12/23/16), capture records present naming their row ids; COUPLES 2 targets 0 missing;
  NOCANON present; SEPARABLE 0 foreign paths.
- Selftest re-run by this judge: `SELFTEST-D81: PASS (5 checks)` (sha `72b10d25…` matches
  `telemetry/selftest-d81.txt`).
- Verdict: **improved**.

## 3. Axis harm check

- `git -C <lane> diff-tree -r -p 1c0e3d4d712d d89c96b6 -- SCORECARD.md`: additions only — three
  capability rows (`orphaned-evidence sweep`, `W2 mutation re-run`, `replace-ref fixture builder`)
  and the round-81 section. No prior axis row or capability row modified or deleted.
- `PROVINCE.md`, `SKILL.md`, `SHONEN.md`, `AGENTS.md`, `README.md`, `MINT.md`, `REGIMEN.md`,
  `examples/`, `templates/`: diff-tree across the range is empty (untouched). No cross-domain bleed.
- Round-range changes: `reports/round-81/**` (32 files), `tools/check-orphan-evidence.py`,
  `corpus/knowledge/myth-symbol/ordeal-judicial-proof-rituals.md`, `corpus/lessons/round-81.md`,
  `corpus/SOURCES.md` (+3 rows, no prior-row cell changed), `SCORECARD.md`, `LOG.md` (appends +
  two append-only corrections). Write scope respected.
- Freshness stays paused by the open round-11 L0 question (operator item; same disposition as
  rounds 77–80, accepted by prior closures) — recorded, not a silent skip.

## 4. Discernment spot-check (outside judge; ≥1 admit + ≥1 reject re-opened)

| item | decision | re-opened source | agree/disagree | reason |
|---|---|---|---|---|
| Claim D admit, row S901 (Lea, *Superstition and Force*, tier A) | admit | refetched `https://www.gutenberg.org/cache/epub/58750/pg58750.txt`: HTTP 200, 1,460,416 bytes — byte-size identical to the capture record; quote 「I swear alone, if thou darest, deny my oath and fight me」 found exactly once, adjacent to the recorded 「Frisian code, where the pleader says」 locator | agree | quote and locator verify in the live plain text; tier A scoped to 19th-c. institutional history is curation-honest (row names it a synthesis, not a law-code edition) |
| Claim D admit, row S903 (EB11 "Ordeal", tier B) | admit | refetched `https://en.wikisource.org/wiki/1911_Encyclop%C3%A6dia_Britannica/Ordeal`: HTTP 200, 87,230 bytes — identical to capture; both spans found (nine-steps iron carry; hands examined/bound in leaves) | agree | article is fully served server-side as claimed; tier B "period claims stop at 1911" is the right scope |
| Claim C admit (capability: orphaned-evidence sweep) | admit | re-ran the tool (selftest 11/11; live sweep re-derived the exact frozen orphan set, exit 1; synthetic green demo exit 0) and verified each of the three dispositions against its cited source (round-68 report prose; r79 correction committed; r63 split receipts committed) | agree | the capability runs from committed bytes alone and the dispositions are honest: zero landable bytes, nothing fabricated |
| Fresh reject: heraldry/emblems entry | reject | `git ls-tree 1c0e3d4d712d -- corpus/knowledge/myth-symbol/heraldry-emblems-identity-marks.md` → exists at base | agree | ground already held; declaring it would be a do-nothing-with-extra-steps claim |
| Reject without row: EB11 "Coin"/"Mint" (probed first) | reject | refetched `https://en.wikisource.org/wiki/1911_Encyclop%C3%A6dia_Britannica/Coin`: HTTP 200 but the stripped body carries only wiki config/scaffold, no article prose in a plain fetch | agree | rejection reason ("stub; a plain fetcher cannot find quotes there") verifies live; no rows wasted, decision recorded in the lesson |
| Carried rejects: naming-systems expansion; dining/tableware | reject (carried) | lesson Gate record; prior-round rejections (r77–r80) unchanged | agree | no new evidence offered this round; upholding is the honest disposition |

Newly written SOURCES row quote check: S901/S902/S903 quotes are 12/23/16 words (all ≤25), each
inside 「」 with a located anchor and capture record; rows sit at `corpus/SOURCES.md` lines 857–859,
inside the Registry table (between `## Registry` and `## Paths`) — the R81-M5 fix verified.
`bash <fleet>/scripts/sources-census.sh validate --root <fleet> kotodama` → **exit 0**, verdict `ok`
(pre-existing W01 tierC-mined warnings only).

## 5. Honesty-preservation checks (kept, not laundered)

- Re-freeze red-before: `telemetry/lands-c81-graded-r1-TOOL-marker.txt` kept (`LEG FAIL TOOL (marker
  missing: 'SELFTEST: PASS')`, `ACCEPT-C-81: FAIL legs=4/6`, exit 1); `git diff b1ebb609 d583ccae --
  reports/round-81/claims.json` shows exactly the marker correction (`"SELFTEST: PASS"` → `"SELFTEST:"`)
  plus the in-file disclosure note; tool bytes unchanged (sha pinned before and after).
- Counter-r2 red-before: `telemetry/lands-c81-graded-r2.txt` kept (`LEG FAIL REDRUN (orphans [] !=
  frozen set (exit 2))`); `git diff b1ebb609 c9dd27a1 -- reports/round-81/accept-c81.py` is exactly the
  one-line REDRUN argv fix (`--repo` removed); `counter-revisions.md` records both revisions with
  old/new shas and "no predicate moved" (verified true by this judge's leg-table read).
- E12 preserved: `telemetry/census-end.txt` keeps the failed first run (three
  `E12 … row outside Registry section` lines, `census-end-exit=1`) beside the green
  `census-end-r2.txt`; the lesson's R81-M5 row carries class/evidence/captured-by/fix. R81-M1..M4
  likewise complete with evidence pointers.
- Do-nothing controls: `telemetry/dry-runs-prelanding.txt` — all three counters refuse at
  `--lands` = base, exit 2; freeze dry-runs fail on named land absences.
- Junk battery: `telemetry/junk-landings.txt` — seven landings (JO1–JO2, JC1–JC2, JD1–JD3), each
  FAIL on its named leg, on each claim's own lands with the original freeze `b1ebb609` (R81-M4
  geometry, self-recorded).

## 6. Per-axis verdicts (agree with the closure JSON)

| axis | verdict | evidence |
|---|---|---|
| operability | improved | claim O re-derived green (counter PASS 6/6 re-run; W2-RERUN and REPLACEREFS-FIXTURE re-derived live; before-count 0 re-measured) |
| calibration | improved | claim C capability verified (tool sha-pinned, selftest 11/11 re-run, red/green demos, exact orphan set re-derived; counter graded PASS 6/6 at its lands, evidence-verified) |
| depth | improved | claim D re-derived green (counter PASS 7/7 re-run; 254→255 files, 824→827 rows re-measured; lint 0 findings re-run; sources re-opened) |
| coverage | unchanged | no new domain surface beyond the D entry's scope; +3 rows are the D move itself |
| freshness | unchanged | paused by the open round-11 L0 question (operator item), recorded since r77 |
| adjacency | unchanged | EB11 transclusion observation reported in the lesson, not absorbed; PROVINCE.md untouched (verified) |

## 7. Trend verdicts

- **expansion: improved** — one new admitted knowledge entry on ground no file owned (filename and
  topic sweeps 0 at base, re-measured), citing three `mined` rows opened this round (used-by the
  entry, verified); SOURCES 824→827 re-measured. LEARNING.md observable met.
- **quality: unchanged** — no existing entry re-verified, deepened or superseded; instrument work is
  excluded from quality observables by the lane's own QUALITY 20 (read and confirmed this closure);
  no admitted entry failed a re-check (census-end-r2 exit 0; lint 0 findings).
- **discernment: unchanged** — no non-author spot-check was available inside the round (the lane said
  so); this closure's outside spot-check agrees on all six sampled admits/rejects (§4), which feeds
  the next round's discernment evidence rather than retroactively changing this round's trend.

## 8. Routed defects / notes for the operator

1. **R81-V1 (routed, status-neutral)** — the accept-c81 REDRUN leg pins the live sweep's summary
   counts; not replayable at closure (see §2, Claim C). Fix in the next C-shaped counter: pin orphan
   set + exit code + classifications, or re-freeze the summary at the measured population.
2. **SHONEN note (duty 6)** — all four boxes carry `[~]` with resolvable pointers and look fully
   checkable by a non-author on the committed bytes (SKILL decision tables cited; claim D is the
   end-to-end task, receipts verified; the counters/generator/builder/checker ran from committed
   bytes only under this closure; PROVINCE.md untouched). Operator may direct a promotion review.
3. Carry-in items 1, 2 and 4 executed and verified; item 3 stays routed around the open round-11 L0
   freshness pause (operator decision still owed).
4. No exploratory claims were declared; no `unprovable-but-better` rulings were required.
5. Conformance defects: none found. The `316641d8` commit-message census count (827 vs the receipt's
   824) was already corrected by the lane's append-only LOG correction in `d89c96b6` before closure.
