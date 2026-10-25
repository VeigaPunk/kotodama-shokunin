# CritTrends — round-71 trend verdicts vs LEARNING.md observables

- Seat: `L1Kotodama71.CritTrends` (leaf critic; read-only on the lane; this file is the only write).
- Date: 2026-10-25. Target: `.ufo/reports/round-71/kotodama.md:63-67` ("## Trend verdicts") — the
  filed claims `expansion — improved`, `quality — improved`, `discernment — improved`.
- Revision pin for every "after" measurement: lane commit **`edd7895`**, materialized with
  `git archive edd7895 | tar -x -C /tmp/crit-trends-r71` (a git-less copy, so no counter can grade
  a moving worktree). "Before" measurements: base **`b94a543c`** via `git show`/`git ls-tree`.
- Worktree disclosure: while this seat measured, the lane worktree carried uncommitted edits
  (`corpus/README.md` counts-date, one `(S873)` added to a calibration bullet of the entry, a
  truncated `reports/round-71/telemetry/census-end.txt`). None of them is in `edd7895`; the entry's
  judged bytes are byte-stable from the C lands commit to `edd7895`
  (`git diff 8c203bd9..edd7895 -- corpus/knowledge` prints nothing), so the expansion verdict is not
  affected. The pending `(S873)` edit was re-tested in the scratch copy: `check-cited-lines` still
  exits 0 (one id on that line).
- Observables read verbatim: `LEARNING.md:33` (expansion), `:34` (quality), `:35` (discernment),
  `:37-38` (growth-without-quality is a trade), `:42-47` (the outside spot-check; "A subagent the
  lane dispatched is still the lane", `:45-46`).

## Verdict set

| trend | filed verdict | this seat | basis (one line) |
|---|---|---|---|
| **expansion** | improved | **improved — AGREE** | one net-new admitted `knowledge/` entry on ground the coverage map did not hold, its 13 `source:` lines all citing `mined` rows opened this round, its README index row added |
| **quality** | improved | **unchanged — DISAGREE** | no existing entry re-verified, deepened or superseded; `QUALITY.md` untouched; the only `verified-at` line added is the new entry's admission stamp |
| **discernment** | improved | **unchanged — DISAGREE** | no outside spot-check exists for round 71 and the filed ground is lane-dispatched seats (`LEARNING.md:45-46`); no disagreement added a `QUALITY.md` criterion |

No trend is **harmed** on the evidence examined. Because quality is `unchanged`, not `harmed`,
`expansion: improved` is **not** a growth-without-quality trade (`LEARNING.md:37-38`): the corpus
grew and the bar it was admitted under was not lowered.

## 1. expansion — improved (filed verdict survives)

Before, at base `b94a543c` (re-derived, not read from the receipts):

```sh
git ls-tree -r --name-only b94a543c corpus/knowledge/culture-material | grep -i 'danc'      # (none)
for f in $(git ls-tree -r --name-only b94a543c corpus/knowledge/culture-material); do \
  git show b94a543c:$f; done | grep -niE '^- topic:.*\b(danc|choreograph|movement culture|performance)\b'   # (none)
git show b94a543c:corpus/README.md | grep -c 'dance-performance-movement'                   # 0
git ls-tree -r --name-only b94a543c corpus/knowledge/culture-material | wc -l              # 35
git ls-tree -r --name-only b94a543c corpus/knowledge | grep -c '\.md$'                     # 242
git show b94a543c:corpus/SOURCES.md | grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}'           # 784
```

The word-bounded sweep is the corrected one (the unbound variant false-matches "avoidance" in
`funerary-material-culture.md:4`; that correction is recorded as mistake R71-M1). After, at
`edd7895` in the git-less copy:

```sh
python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge   # totals.files 243
find corpus/knowledge/culture-material -maxdepth 1 -type f | wc -l                    # 36
find corpus/knowledge -type f -name '*.md' | wc -l                                    # 243
grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md                          # 797
python3 -B tools/check-cited-lines.py corpus/knowledge/.../dance-performance-movement-codes.md
                                                                                      # 0 findings, exit 0
python3 reports/round-28/readme/sweep.py   # exit 0; rows 243 files 243; header_drift {}; totals_ok True; footer_ok True
python3 -B reports/round-71/accept-c.py --root .
# LEG PASS ENTRY / COUNTS culture-material=36 corpus=243 / CITED distinct S-ids cited=13 /
# ROWS missing=[] not-mined=[] usedby-missing=[] / USEDBY-PATHS missing-paths=[] /
# CITED-LINES exit=0 / SWEEP entry-only  ->  ACCEPT-C-71: PASS, exit 0
```

Row facts re-derived from `corpus/SOURCES.md` (all 13 rows: 11 columns, no pipe-in-cell, tier A 12 /
B 1, status `mined`, `opened` 2026-10-25, `used-by` exactly the entry path). The entry cites exactly
S861–S873 and no other id. Registry census legs all clean at `edd7895`: duplicate ids none,
malformed rows 0, enum/tier violations none, missing `used-by` paths none.

Provenance re-located by this seat, live (two independent anchors, beyond RevGate's 13/13):

```sh
curl -sSL -A 'Mozilla/5.0' https://www.abt.org/explore/learn/ballet-dictionary/ | grep -o 'positions of the feet are standard[^<]*'
# "positions of the feet are standard in all methods, the positions of the arms are not, ..."  (S868, HTTP 200)
curl -sSL -A 'Mozilla/5.0' http://ickl.org/ ...   # "Its members practice the system ... originated by Rudolf Laban,
                                                  #  known as Kinetography Laban or Labanotation ."  (S870, HTTP 200)
```

Harmed condition tested and not met: the entry carries provenance, a calibration shelf naming the
promotional-heritage limit of the UNESCO records and the unread print editions, `- couples:`, a
11-step application checklist, `- scope:`/`- refuses:` and a one-way handoff — i.e. it does not
fail the bar it was admitted under.

**Residual (does not flip the verdict):** the claims.json C `type` and the lesson header say
"frontier → core", but `PROVINCE.md` never named this ground and is untouched
(`git diff --stat b94a543c..edd7895 -- PROVINCE.md` empty) and `LOG.md`'s round-71 entry records no
province move. Expansion's observable needs only uncovered coverage-map ground, which holds; the
label overstates the province bookkeeping.

## 2. quality — unchanged (filed verdict fails)

The filed ground is: "The round's record instruments are re-verified: receipt headers restored to
the QUALITY 17/19 bar (V70-1), S860 pointer accuracy repaired (V70-2), Gate quote discipline
restored (V70-3). No admitted entry fails its re-check."

That is the **calibration** axis (and partly depth/operability), not the quality observable.
`LEARNING.md:34` improves when "a weaker entry is superseded by a stronger one, or stale entries
re-verify". Counterexample, exact commands:

```sh
git diff --name-status b94a543c..edd7895 -- corpus/knowledge corpus/QUALITY.md
# A	corpus/knowledge/culture-material/dance-performance-movement-codes.md
#   (one added file, zero M lines: no existing entry was touched)
git diff --stat b94a543c..edd7895 -- corpus/QUALITY.md     # empty (bar untouched)
git diff b94a543c..edd7895 -- corpus/knowledge | grep -E '^[-+]- verified-at'
# +- verified-at: 2026-10-25      (the new entry's admission stamp only)
git diff b94a543c..edd7895 | grep -cE '^\+.*supersedes S[0-9]'      # 0
```

So: no entry re-verified, none deepened, none superseded, no `supersedes S…` row, and the only
freshness byte added is the new entry's own stamp. The strongest counter-argument — "the new entry
carries `verified-at: 2026-10-25`, so freshness improved" — fails because a first admission is not a
re-verification of an existing entry; it is the expansion event itself (and the lane's freshness
axis is paused by `reports/round-71/claims.json` `non_goals`).

Not `harmed`: no admitted entry was found false or stale and left unmarked; the round's own record
repairs (V70-1..V70-3) are real, they just grade on calibration. What would flip it: any existing
entry re-verified/deepened/superseded with a receipt, or a stale entry re-checked and re-stamped.

## 3. discernment — unchanged (filed verdict fails)

The filed ground has two halves, and both fail the observable at `LEARNING.md:35`.

**(a) "The outside round-70 spot-check's five disagreements were turned into landings
(V70-1..V70-5)."** Acting on a previous round's spot-check is not this round's spot-check agreeing
on this round's admits *and* rejects. The second clause is "a disagreement becomes a lesson that
adds a grounded `QUALITY.md` criterion" — the V70-4 disagreement was landed as a `SCORECARD.md`
row + `reports/round-71/corrections-r70.md`, and `corpus/QUALITY.md` was not touched
(`git diff --stat b94a543c..edd7895 -- corpus/QUALITY.md` empty). Clause not fired.

**(b) "the Gate admits 13 and rejects 8 with reasons+flips (both ends sampled by wave-2 seats)."**
Wave-2 seats are dispatched by this lane (`reports/round-71/claims.json` wave block;
`.ufo/waves/round-71/w2/wave2-dispatch.json`), and `LEARNING.md:45-46` says: "A subagent the lane
dispatched is still the lane." They cannot be the non-author spot-check. At filing time the report
itself says the seats "are still returning", so the sample was not even complete. And no round-71
spot-check exists in any form:

```sh
ls corpus/lessons/ | grep 71        # round-71.md only (round 69/70 each have -verifier-spotcheck.md)
git show edd7895:corpus/lessons/round-71.md | grep -niE 'spot-check|spotcheck'   # (none)
```

The qualifying mechanism the lane itself used last round is the hyaku closure integrator
(`corpus/lessons/round-70-verifier-spotcheck.md:1-3`, author "hyaku closure (non-author
integrator, @m_flash)"), and it has not been written for round 71.

Not `harmed`: the V70-4 disagreement was recorded (SCORECARD row + corrections file + lesson
Corrections), so nothing was "left unlearned" in the narrow sense; no criterion was added at all,
so the second harmed clause cannot fire either.

## Counterexample: the round-70 correction did not generalize

The same error class the lane corrected one round ago recurs verbatim in the filed round-71 report.
Round 70 (filed bytes, `.ufo/reports/round-70/kotodama.md:111-113`):

> "**expansion — improved.** Registry 783→784 rows (S860 …). Small and bounded; no knowledge entry,
> so coverage is not claimed."

Round 71 (`.ufo/reports/round-71/kotodama.md:66`):

> "**quality — improved.** The round's record instruments are re-verified: receipt headers restored
> … S860 pointer accuracy repaired … Gate quote discipline restored."

Both substitute record/instrument repair for a LEARNING observable. Round 70's instance was
corrected by a `SCORECARD.md` row (V70-4) but by **no criterion**, and the class recurred in the very
next round. That is the strongest local evidence that a correction row is not a durable fix and that
a `QUALITY.md` criterion is owed — the same shape as every prior criterion's grounding
(the twelve criteria that carry an explicit `Grounded in …` line, `QUALITY.md:29-49,59`).

Two contributing record defects make the recurrence harder to see from inside the lane:

- **The lesson `## Mistakes` table is structurally broken at `edd7895`.** `corpus/lessons/round-71.md`
  line 49 is a one-cell row `| attribution |`; its remaining cells are an orphan line 57 outside the
  table; and blank lines 51, 53, 55 split the table into four tables, so the instrument-provenance,
  guard-gap and declared-counter-defect rows are not rows of the Mistakes table at all
  (`git show edd7895:corpus/lessons/round-71.md | nl -ba | sed -n '42,58p'`). `LEARNING.md:19-21`
  requires each mistake as a row. Smallest fix: rejoin 49+57 into one five-cell row and delete the
  three blank lines inside the table.
- **The reject sweep is not a countable reject set.** `corpus/lessons/round-71.md:33-40` says
  "ScoutOpenSourcesC refused 8 candidates … None is admitted as a row", but its first group is the
  UNESCO live pages whose elements *are* admitted as rows via captures (S861–S867), and its last
  group ("Britannica/RAD live 403") mixes a source that landed as S869 with one that landed as no
  row. Separately, `ScoutOpenSourcesC.md` opened 17 candidates; the 4 opened B-tier ones
  (Britannica "dance", Hanna, Royce, Sachs) have **no recorded disposition and no registry row**
  (`grep -c '<url>' corpus/SOURCES.md` → 0 for each). The Gate therefore does not yet satisfy
  "candidates considered, admitted, rejected (with reasons)" for every candidate it opened — and it
  is exactly the material a spot-check must agree on. (RevGate/RevEntry own the gate-quote and
  entry-shape legs; this is a cross-reference, not a re-litigation.)

## Impacted axes and next-round routing

- expansion → `coverage`, `adjacency`: a real, countably verified gain (one entry, 13 mined rows,
  coverage map reconciled).
- quality → `depth` (claim D's no-git guard), `operability`/`calibration` (Ca's records): axis gains,
  **no trend gain**. `freshness` stays paused.
- discernment → `calibration`: no trend gain until the non-author spot-check lands in the lesson.
- `LEARNING.md:86-87` ("Choose the round's claims from the trend that is furthest behind"): after
  this round, **quality and discernment are the two trends furthest behind**; round 72 should claim
  one of them, not another coverage entry.

## Smallest safe correction (ordered, smallest first)

1. **Restate the filed trend section** to: `expansion — improved`, `quality — unchanged`,
   `discernment — unchanged`, each with its observable basis (`LEARNING.md:33-35`); drop the
   record/instrument and lane-seat grounds. This alone makes the report honest and is a
   report-bytes edit, not a lane-bytes edit.
2. **Record the round-71 non-author spot-check** in `corpus/lessons/round-71.md` (hyaku closure
   integrator; ≥1 admit from S861–S873 and ≥1 reject from the refusal list, `agree`/`disagree` with
   reasons). The material exists this round (13 admits + a real refusal list), unlike round 70. If it
   lands before closure, `discernment: improved` becomes legitimate through the first clause.
3. **Add one `QUALITY.md` criterion** grounded in `round-70-verifier-spotcheck.md` §5 and this
   round's recurrence: *trend verdicts are graded on the `LEARNING.md` observables only; record and
   instrument repair is graded on the calibration axis; a seat the lane dispatched is not the
   non-author spot-check.* That is the only durable fix for the class (a SCORECARD row already
   failed to prevent it once). Do not back-claim it for round 71; it fires the discernment clause for
   the round in which it lands, and the grounding lesson is already on record.
4. **Repair the `## Mistakes` table** (lines 49/51/53/55/57 at `edd7895`), **add the V70-4 recurrence
   as a mistake row**, and **record a disposition for the 4 unaccounted opened candidates**
   (queued/rejected row or a "considered, not admitted: reason" line in the Gate).

## Verification disclosure

Read-only; no lane file was modified and no subagent was dispatched. All "after" numbers come from
`/tmp/crit-trends-r71` (a `git archive edd7895` copy); all "before" numbers from `git show`/
`git ls-tree` at `b94a543c`. Two live anchors were re-fetched (S868, S870); the archive-captured
UNESCO rows were left to ScoutReopen/RevGate, whose 13/13 verbatim result this seat treats as
corroboration, not as its own measurement. Tool installs: none.
