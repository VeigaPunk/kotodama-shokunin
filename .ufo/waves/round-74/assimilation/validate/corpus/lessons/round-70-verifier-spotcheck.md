# Round-70 verifier spot-check (non-author)

author: hyaku closure (non-author integrator, @m_flash)
closed: 2026-10-25 (hyaku run 6, kotodama lane round 70)
lane base: `21e6a7f3fb63e717f2021c46a172e396c4759a7c` · lane HEAD: `453676a2363c97e158cb112c9588906564d95a21`
report: `.ufo/reports/round-70/kotodama.md` (fleet commit `779e29bb756dabb06db59516053c9e46a8965205`, author `kotodama-shokunin`)

I did not author this round. Everything below is re-derived by me from committed bytes; every
before→after was re-run in a clone materialized at the cited revision, not read from the lane's
receipts.

## 1. Conformance (step 1)

| check | command | observed | verdict |
|---|---|---|---|
| report committed by lane identity | `git log --format='%an %H' -- .ufo/reports/round-70/kotodama.md` | `kotodama-shokunin 779e29bb…` | pass |
| report lands after the lane commit | report commit `2026-10-25 07:20:14 -0300` vs lane HEAD `453676a2` `07:19:51 -0300` | report is 23 s after the cited HEAD | pass |
| `SHONEN` heading, one line per box | report `## SHONEN` vs `SHONEN.md` box count | 4 boxes, 4 lines, all `[~]` with pointers; no `[x]` claimed | pass |
| every cited lane commit exists and is an ancestor | `git cat-file -t` + `git merge-base --is-ancestor <h> main` for `6cb51a4`, `acc2d614`, `453676a2`, `6a98d7d`, `e86ed3e`, `975e8f2`, `793f797` | all exist; `6cb51a4`, `acc2d614`, `453676a2` all ancestor-of-`main` | pass |
| lane repo clean and pushed | `scripts/hyaku/jj-lane.sh state …` + `git status --porcelain` | `ahead=0 behind=0 tracked=0 untracked=0`; status empty; `ls-remote origin refs/heads/main` = `453676a2…` | pass |
| dispatched prompt carries the contract | `.ufo/prompts/kotodama-round-70.md` | §2b frontier step, §3 L2 floor (≥8, one batched call — matches `MISSION.md` §L2 concurrency), §4 report contract with `SHONEN` heading + commit-hash citation rule, §5 commit-then-push + write scope + L0 channel, §6 hyaku addendum | pass |
| wave seats actually dispatched | report §"Round shape"; `.ufo/watchdog.log` digest | **0 of 33 planned wave seats dispatched** (dispatch refused 6× `Background job limit reached (100)`; validated spec + rendered payload committed at `.ufo/waves/round-70/`) | **defect V70-7** (status-neutral, orchestrator-side) |

Dispatch/complete digest (copied; the live log drifts):
`2026-10-25T06:59:32-03:00 launch kotodama round=70 pgid=3242996 driver=hyaku-inline attempt=1` ·
`2026-10-25T07:20:45-03:00 complete kotodama round=70; hyaku-inline attempt=1`.

Fleet root carries only driver state (`.ufo/state/*.report-baseline`), excluded per D6 — no lane
leftover.

## 2. Claims — re-derived, not evidence-verified

Method: `git clone --shared` of the lane into `/tmp`, `git checkout <rev>`, run the frozen
counting command verbatim. Round 69's rule (`QUALITY.md` 19) is satisfied here because the run
happens at the cited revision, not in a moving worktree. I executed the lane's counters as the
named closure verifier — this is not a sibling executing a gate.

### Claim O — operability (gate registry + accept-d selftest)

| leg | command | before (`21e6a7f`) | after (`453676a2`) | reported |
|---|---|---|---|---|
| registry rows | `grep -cE '^\| [^|]+\| (gate\|probe) \| .*reports/round-[0-9]+/accept-[a-z]+\.py' SKILL.md` | 0 | **36** | 36 ✔ |
| counter files | `find reports -name 'accept-*.py' \| sort \| wc -l` | 36 | 36 | 36 ✔ |
| registry set equality | registry paths vs `find` | — | **SET-EQUAL** (`diff` empty, 36/36) | asserted ✔ |
| selftest | `python3 -B reports/round-69/accept-d.py --selftest` | exit 1, `DO-NOTHING FIXTURE: PASS (unexpected)`, `SELFTEST: 1/2` | exit 0, `DO-NOTHING FIXTURE: FAIL (as required)`, `SELFTEST: 2/2` | ✔ |
| data predicate unharmed | `python3 -B reports/round-69/accept-d.py --root .` | — | `ACCEPT-D-69: PASS legs=8/8`, exit 0 | ✔ |

**O verified.** Beyond the two declared legs I checked the stronger property the claim implies —
every enumerated counter has its own row, no row points at a non-existent counter.

### Claim Ca — calibration (round-69 defect dispositions)

| leg | command | before (`21e6a7f`) | after (`453676a2`) | reported |
|---|---|---|---|---|
| unique ids | `awk -F'\|' '/^\| D(10\|[1-9]) \|/ {gsub(/[[:space:]]/,"",$2); print $2}' reports/round-70/corrections-r69.md \| sort -u \| wc -l` | file absent | **10** (`D1 D2 … D10`) | 10 ✔ |
| duplicates | same `\| sort -u \| uniq -d \| wc -l` | — | **0** | 0 ✔ |
| nonempty class/surface/landing | awk column test (fields 3, 4, 7) | — | no empty cell | asserted ✔ |
| SCORECARD correction row | `grep -c 'round-69 calibration' SCORECARD.md` | 0 | **1** (`:1383`, naming the superseded `improved` row at `:1331`) | ✔ |

**Ca verified.** I also read the SCORECARD diff: the D5 reword is in place at `:1353-1357` and the
one in-place exception is disclosed — consistent with the append-only convention's disclosure duty.

### Claim D — depth (settlement-checker hardening, sourced by S860)

| leg | command | before | after | reported |
|---|---|---|---|---|
| selftest | `python3 -B tools/check-supersession-settlement.py --selftest` | `SELFTEST: 7/7`, exit 0 | **`SELFTEST: 10/10`, exit 0** — new cases `missing-unique-file`, `malformed-rows-report`, `malformed-target-no-crash` all PASS | ✔ |
| regression | `python3 -B reports/round-69/accept-o.py --root .` | `ACCEPT-O-69: PASS legs=7/7` | **`ACCEPT-O-69: PASS legs=7/7`, exit 0** | ✔ |

**D verified.** I read the diff (`tools/check-supersession-settlement.py`, +46/−3): the three
behaviours are real code, not test-only — `classify()` returns `t_st="malformed"` instead of
`KeyError: 'status'`, `scan()` prints `MALFORMED-ROW <id>` per malformed row, `missing_paths` is a
`set` before counting, and `FIX5`/`FIX6` fixtures exercise multi-path and malformed cases. The
`malformed-target-no-crash` case asserts `rc == 1` (pending, not a crash) — weak but not false.

### Sourced-claim leg

Claim D's source is S860 (`corpus/SOURCES.md:815`, tier A, kind `own-work`, status `mined`,
`used-by` `SKILL.md, corpus/lessons/round-70.md`). Its pointer is inaccurate — see V70-2. The
quote itself is faithful.

## 3. Axis verdicts

| axis | verdict | evidence |
|---|---|---|
| operability | **improved** | 36/36 registry rows, set-equal to the enumerated counters; accept-d selftest green at the committed revision and its data predicate still 8/8 |
| calibration | **improved** | D1..D10 each carry a landing (10/10 unique, no dup, no empty cell); the SCORECARD self-contradiction is closed by an appended row marking round-69 calibration unprovable; the wave refusal is disclosed rather than papered over. Caveat: two trend verdicts overstate their observables (V70-4) and five record defects are routed below — the repair is real, the new record discipline is not yet clean |
| depth | **improved** | checker 7/7→10/10 with three named behaviours proven by fixtures; accept-o regression holds at 7/7 |

No claimed axis is harmed; the SKILL/SCORECARD/SOURCES/LOG diffs are additions plus one disclosed
in-place reword (`SCORECARD.md` 16+/1−), and no `corpus/` entry was deleted or rewritten.

## 4. Discernment spot-check

The round's `## Gate` holds one candidate, admitted, and records **no reject** (V70-5), so the
required admit+reject sample cannot both come from this round. I sampled the one admit and, to
exercise the lane's reject calibration, the nearest standing reject rows.

| item | decision | re-opened source | agree / disagree | reason |
|---|---|---|---|---|
| S860 — `tools/check-supersession-settlement.py` (own-work, tier A) | admitted, mined | `git show 453676a2:tools/check-supersession-settlement.py` lines 18-22; `--selftest` run by me | **agree** | the quoted sentence is verbatim at `:20-21`; the row's scope (multi-path `used-by`, `MALFORMED-ROW`) is exactly the behaviour the diff adds and the selftest proves (10/10). Tier A is right for a lane-owned re-runnable gate output; `own-work` is disclosed, not passed off as external evidence. The verify-at cell's revision pairing is wrong (V70-2) but the quote and scope hold |
| S857 — Britannica "dreadlocks" | rejected (Cloudflare wall) | live URL with a browser UA: `curl -w 'http=%{http_code} bytes=%{size_download}'` | **agree** | `http=403 bytes=5595`, body contains `Just a moment...` — byte-for-byte the row's recorded ground (~5,595 bytes); the flip condition (an openly reachable encyclopedia entry on dreadlocks) is named, not vague |
| S858 — Britannica "Tuareg" | rejected (already rowed + walled) | registry lookup of the URL's owner | **agree** | S701 (`corpus/SOURCES.md:656`) already owns `britannica.com/topic/Tuareg`; a second row would add no source, and the same wall applies |

Both ends of the lane's calibration hold on the samples I could open. The admit shows the lane
admits its own instrument at the right tier with a located quote; the rejects show it refuses a
walled page and a duplicate rather than padding the registry.

Census: `scripts/sources-census.sh validate --root … kotodama` → `ok …/corpus/SOURCES.md`,
**exit 0**, `W04` stable at 28 (same 28 duplicate-URL warnings as the round's start/end receipts).

## 5. Trend verdicts (as the named non-author reviewer)

| trend | report | closure | evidence |
|---|---|---|---|
| expansion | improved | **unchanged** | `CORPUS.md` criterion 4: "Expansion is knowledge, not rows" — it counts admitted `knowledge/` entries citing a `mined` row on uncovered ground. Registry 783→784 is frontier-step curation (S860, own-work). Zero knowledge entries admitted; the report itself disclaims coverage. `improved` contradicts the lane's own criterion |
| quality | improved | **unchanged** | no `corpus/knowledge/` entry was re-verified, deepened or superseded (`corpus/` diff = SOURCES +1 row, lessons +1 file). The depth work is real but is instrument quality, graded on the depth axis above. Against it: round-70's receipts dropped the `QUALITY.md` 17/19 header block that round-69's receipts carry (V70-1), so the round cannot claim `improved` on its own evidence discipline |
| discernment | improved | **unchanged** | the outside spot-check agrees on the one admit and on the standing rejects, but round 70 produced no reject decision to calibrate against and added no `QUALITY.md` criterion citing a lesson — neither `improved` clause in `LEARNING.md` fires. The report's ground (repairing round-69's record defects) is the calibration axis, not the discernment observable |

No trend is `harmed`; growth-without-quality is not being traded (no expansion is claimed).

## 6. Routed defects (durable queue — the lane fixes these next round)

| id | class | surface | observed | required fix |
|---|---|---|---|---|
| V70-1 | receipts vs the lane's own bar | `reports/round-70/telemetry/{measures-o,measures-ca,measures-d,controls-o,controls-ca,controls-d}.txt` | headers read `measured at lane 6cb51a4+landed edits`; no `# counter sha256`, `# stamped revision`, `# evaluated revision`, `# measured revision (lane main)`, `# tree`, `# worktree dirty` block. Round-69 receipts carry all six. `6cb51a4` is the declaration: its bytes do **not** contain the after-state (the hardened tool first exists at `acc2d614`) | re-stamp each receipt at `acc2d614` with the full `QUALITY.md` 17/19 header; preserve the original bytes below a marker. Criterion 19's `--lands <40hex>` leg is likewise absent from the round-70 counters |
| V70-2 | evidence pointer accuracy | `corpus/SOURCES.md:815` (S860 verify-at cell) | pairs hardened blob `6a314e9c7c5635a15a9b2f8b57bc34db8039a301` with "lane revision `6cb51a4…`". `6cb51a4:tools/check-supersession-settlement.py` is blob `1ef2e965…`; `6a314e9c` first exists at `acc2d614`. At `6cb51a4`, `grep -c MALFORMED-ROW` = **0**, so the blob named does not live at the revision named | repoint the cell to `acc2d614` (in-place `recheck` change is allowed; log old→new in the next lesson) |
| V70-3 | quote discipline | `corpus/lessons/round-70.md` `## Gate` under a "≤25 words" header; `.ufo/reports/round-70/kotodama.md` calls it "a 25-word located quote" | the quote is **27 words** (`A row whose … not globally…`); the ellipsis marks a cut at `—` mid-sentence | trim to ≤25 words next round and correct the "25-word" characterization in that round's report; the SOURCES cell (exactly 25 words) is compliant |
| V70-4 | trend verdicts vs observables | `.ufo/reports/round-70/kotodama.md` §Trend verdicts | `expansion: improved` contradicts `CORPUS.md` 4 (no knowledge entry); `discernment: improved` rests on record repair, not a gate decision or a new criterion | grade trends against the `LEARNING.md` observables; a repair round should declare `unchanged` where nothing in the observable moved |
| V70-5 | gate completeness | `corpus/lessons/round-70.md` `## Gate` | one candidate, admitted, and no reject row **and** no "rejected this round: none" statement (round 69 carried one), so the round offers no reject decision to spot-check | state the reject sweep outcome explicitly every round (even "none, and here is the sweep"), and open at least one candidate the frontier can refuse |
| V70-6 | selftest environment dependence | `reports/round-69/accept-d.py` (R69-M11 fix) | the fix seeds the do-nothing fixture from `git show 793f797:SKILL.md`; on an exported tree with no `.git` it falls back to the live `SKILL.md` and reports red — I measured `DO-NOTHING FIXTURE: PASS (unexpected)`, `SELFTEST: 1/2`, exit 1 on `git archive` output of the same revision | make the no-git path a declared `could-not-evaluate` (exit 2) or refuse explicitly, and say so in the `accept-d-69` registry row; a genuine red must never be indistinguishable from a missing object store |
| V70-7 | swarm conformance (orchestrator-side) | round shape | 0 of 33 planned wave seats dispatched; the one batched dispatch was refused 6× `Background job limit reached (100)`; `MISSION.md` §L2 concurrency floor (≥8, one call) unmet and the operator's swarm directive unmet | none owed by the lane — the cause is the shared session job cap, so it is status-neutral. Consequence recorded: no independent falsification wave attacked this round's claims; this file's re-measurement is the only independent check |

## 7. SHONEN note for the operator

All four boxes now carry resolvable pointers that a non-author can check from committed bytes:
box 1 (`SKILL.md` decision table `:20`, registry `:662-697`, error patterns `:505`, checklist
`:522`; 784-row registry with census exit 0), box 2 (this round's end-to-end counter runs, logged
at `LOG.md:4251`), box 3 (every command absolute and re-runnable — with the V70-6 caveat that one
needs `.git` present), box 4 (the diff stays inside the lane's own surfaces; I found no sibling
owner touched). The report correctly leaves all four `[~]`: promotion is operator-owned, and the
boxes look ready for that review.

## 8. Closure

Claims O, Ca, D all verified by independent re-measurement at `453676a2`; no axis harmed;
admitted. Trends: expansion `unchanged`, quality `unchanged`, discernment `unchanged`. Seven
defects routed (six owed by the lane, one orchestrator-side), none status-neutral-blocking.
