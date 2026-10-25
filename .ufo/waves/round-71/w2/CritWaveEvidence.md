# CritWaveEvidence — round 71, wave 2: wave-1 evidence audit (falsify)

Seat: `L1Kotodama71.CritWaveEvidence` (UFO-FSD falsify critic, leaf). Date: 2026-10-25.
Findings only; no lane bytes edited except this file. No tools installed or updated.

Audited assertion (wave-2 spec:108): *"37 wave-1 seat reports exist under `.ufo/waves/round-71/w1/`,
each with a findings summary and no lane mutation; verify the dispatched task call count matches
the registry (37)."*

## Verdict

| axis | claim | verdict |
|---|---|---|
| A1 | 37 wave-1 seat reports exist (committed, non-empty) | **PASS** |
| A2 | dispatch task set = registry set = spec items = assignments = plan tasks = on-disk reports, 37 names, no extras | **PASS** |
| A3 | each report carries a findings/results summary | **PASS** (13/37 use domain-specific headings, not the word "findings"/"summary") |
| A4 | **no lane mutation** | **FAIL** — 2 of 37 seats wrote lane files |
| A5 | dispatched task call count matches the registry (37) | **PASS** (1 `taskCall` × 37 tasks; runtime call count not independently observable — see Limit) |
| A6 | wave summary's own completeness list (derived) | **FAIL** — enumerates 27 names while calling it "37 total" |
| A7 | committed artifact matches the seat's own description (derived) | **FAIL** — `accept-d.py` is 106 lines, its report claims 83 |

## A1 — report cardinality: PASS

```
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
ls -1 .ufo/waves/round-71/w1/*.md | wc -l                      # 37
git show --name-only --format='' 1d1b432 | grep -c '^\.ufo/waves/round-71/w1/.*\.md$'   # 37
find .ufo/waves/round-71/w1 -name '*.md' -empty | wc -l         # 0
git status --porcelain .ufo/waves/round-71/w1                   # empty (all committed, none untracked)
git log --diff-filter=A --format='%h' -- .ufo/waves/round-71/w1/*.md | sort -u   # single commit 1d1b432
```

No duplicate report: 37 distinct sha256, and no copy attack — the highest 9-gram shingle Jaccard
over all 666 pairs is 0.019 (`RevCaDefectGroundTruth` × `RevRound70Gate`), and the highest
`difflib` ratio among the eight highest-overlap pairs is 0.106 (`ExecDraftEntryShell` ×
`RevDanceEntryShape`, shared method boilerplate). The 0.9 `quick_ratio` hits are character-multiset
coincidence, e.g. "No tools installed".

## A2 — name-set identity: PASS

```
cd .ufo/waves/round-71/w1
python3 - <<'PY'
import json,os
d=json.load(open('wave1-dispatch.json')); r=json.load(open('swarm-registry.json'))
a=json.load(open('assignments.json')); s=json.load(open('spec.json')); p=json.load(open('plan.json'))
T={t['name'] for t in d['taskCall']['tasks']}; R=set(r['members']); A=set(a); S={i['name'] for i in s['items']}
P={t['name'] for t in p['tasks']}; M={f[:-3] for f in os.listdir('.') if f.endswith('.md')}
print(len(T),len(R),len(A),len(S),len(P),len(M))          # 37 37 37 37 37 37
print(T==R==A==S==P==M)                                   # True
PY
```

Also verified: 37 unique `agentId`s, all `L1Kotodama71.<Name>`; task `agent` field == registry `role`
for all 37; every brief's `Report:` trailer points at its own `w1/<Name>.md`; role histogram
scout 10 / reviewer 8 / critic 7 / executor 5 / mutation-tester 3 / sentinel 2 / connector 1 /
scribe 1 = 37.

## A3 — findings summary present: PASS (with a wording qualifier)

24/37 reports carry a heading literally containing findings/summary/verdict/result/conclusion. The
other 13 carry an equivalent results section under a domain heading — e.g. `CritNoGitHypothesis`
("Counterexample and evidence", "Impacted axes", "Smallest safe correction"), `ExecDCounterStub`
("Evidence — exact observed output"), `ScoutQuarantineFetch2` (per-row PRESENT/REFUSED verdicts),
`ScoutCensusBaseline` ("Observed facts / boundary"). Every report states an outcome; none is a
method-only stub. Thinnest are `ExecCaCounterStub.md` (1 230 B, 7 lines — summary only, and it says
"Verification intentionally not run; the parent owns post-integration checks") and
`RevRound70Gate.md` (867 B, 11 lines, but carries the decisive 27-word count and the
`acc2d614` vs `6cb51a4` blob evidence).

So "each with a findings summary" holds in substance; it would not hold under a literal
"heading named Findings/Summary" test.

## A4 — "no lane mutation": FAIL (the counterexample that matters)

Two wave-1 seats wrote into the lane, not just into `.ufo/`:

1. `ExecDCounterStub.md:7` — *"**Created/refined (draft):** `reports/round-71/accept-d.py`
   (untracked; 83 lines …)"*, while line 19 of the same report says *"No mutation of the lane"*.
   The file's mtime is inside the wave-1 window, so the bytes are the seat's:
   ```
   ls -l --time-style=+%H:%M:%S reports/round-71/accept-d.py   # 08:22:29
   ls -l --time-style=+%H:%M:%S .ufo/waves/round-71/w1/*.md | awk '{print $6}' | sort | sed -n '1p;$p'
                                                               # 08:21:44 .. 08:26:50
   ```
2. `ExecCaCounterStub.md:3` — *"Implemented `reports/round-71/accept-ca.py` as a read-only draft
   acceptance counter."* Independently corroborated mid-wave by a sibling seat:
   `RevCounterPredicates.md:61` — *"`reports/round-71/accept-ca.py` appeared in the working tree
   during this review (draft executor artifact)"*.

Both writes were **authorised by the wave-1 briefs themselves** (each brief names the lane path to
build: `… /reports/round-71/accept-ca.py (this is a DRAFT …)`, `… /reports/round-71/accept-d.py
(DRAFT; the L1 freezes the final)`), and both files land in `1d1b432`
(`git show --stat 1d1b432 -- reports/round-71/accept-ca.py reports/round-71/accept-d.py` →
`+141` / `+106`, both adds). So the invariant that actually holds is **"no seat wrote outside its
assigned paths"**, not "no lane mutation" — and the wave as a whole mutated the lane by design
(accept-c.py in `498db73`; S861–S873 in `498db73`/`8c203bd`; the dance entry; six round-70
receipts re-stamped, `corpus/SOURCES.md` S860 cell, `corpus/lessons/round-70.md` quote,
`SCORECARD.md`, `corpus/lessons/round-71.md`, `quarantine-verdicts.md`, `census-end.txt` in
`1d1b432`; `measures-ca.txt`/`measures-d.txt` in `3764c2d`).

No evidence of an **out-of-scope** write was found: the write-scope sentinel
(`SentinelWriteScope.md`) reports path-boundary findings for *reads* only ("No instruction directs
a write to those prohibited targets"), and `git show --name-only 1d1b432` shows no corpus path
touched by a seat that was barred from it (`ExecDraftEntryShell` wrote only `/tmp`,
`ExecSOURCESRowTemplate` only `/tmp/row-template-builder.py`, `ScribeWaveSummary` only `/tmp` +
its report).

**Smallest safe correction:** restate the evidence line as *"37 reports; 2 executors wrote their
assigned draft counters (`accept-ca.py`, `accept-d.py`); no seat wrote outside its assigned
paths"* — or drop the mutation clause from the wave-2 assertion entirely, since the wave's
deliverables are lane mutations.

## A5 — dispatch call count vs registry: PASS

```
cd .ufo/waves/round-71/w1
python3 -c "import json;d=json.load(open('wave1-dispatch.json'));print(len(d['taskCall']['tasks']), d['counts'], d['resumeSends'], d['compaction']['applied'])"
# 37 {'spawn': 37, 'resume': 0, 'total': 37} [] False
python3 -c "import json;r=json.load(open('swarm-registry.json'));print(len(r['members']))"   # 37
```

One recorded `taskCall` holding 37 tasks; `resumeSends` empty; compaction not applied (payload
intact, `savedBytes: 0`), so no seat was silently dropped from the batch.

**Limit (not a defect):** the registry is a *dispatch* ledger — every member is
`{kind: "spawn", agentId, role, item: null}` with no status field, and `wave` is `null`. It cannot
evidence that a seat ran; the 37 committed report files are the execution evidence. Likewise the
runtime task-call count is not observable from the lane: what is verifiable is that exactly one
dispatch artifact exists and it carries 37 tasks. "Matches the registry (37)" therefore means
"one call, 37 dispatched, 37 members" — not "37 calls".

## A6 — wave summary completeness list: FAIL

`ScribeWaveSummary.md:53` — *"Seat reports in `.ufo/waves/round-71/w1/` (37 total: 23 on disk + 4
pending incl. this report):"* — then enumerates **27** names. `23 + 4 = 27 ≠ 37`, and 10 landed
seats are missing from the list:

```
CritCaSeparability, CritClaimSizing, CritTrendObservables, ExecSOURCESRowTemplate,
RevCounterPredicates, RevQuarantineCrossCheck, ScoutGapScan, ScoutLessonMistakeSweep,
ScoutQuarantineFetch2, ScoutQuarantineFetch3
```

(reproduce: parse the parenthetical block after that line and diff against `ls -1 *.md`).

**Smallest safe correction:** append an erratum line to the report (append-only) —
*"List as-of-stamp enumerates 27 (23 landed + 4 pending); the wave completed at 37 — missing:
<the 10 names>"* — and make sure the wave-2 summary lists from `ls`, not from a hand-carried
stamp.

## A7 — committed artifact vs seat description: FAIL (minor, provenance)

`ExecDCounterStub.md:7` describes `reports/round-71/accept-d.py` as *"83 lines"*; the committed
artifact is **106** lines (`wc -l reports/round-71/accept-d.py`; `1d1b432` adds exactly 106). The
file's mtime (08:22:29) is inside the wave window, and every other lane write in `1d1b432` is
08:36–08:43, so the 106-line bytes are the seat's own — the report's line count is simply wrong,
not stale-by-later-edit. Harmless to the counter's behaviour (it passes, see below) but it means
the report is not a byte-accurate description of what it landed.

**Smallest safe correction:** correct the line count to 106 (erratum line), or drop line counts
from executor reports in favour of a sha256 of the landed file.

## Corroboration that the wave-1 artifacts are live (other seats' grading axis, noted only)

```
python3 -B reports/round-71/accept-c.py    # ACCEPT-C-71: PASS  (exit 0; culture-material=36 corpus=243; cited 13)
python3 -B reports/round-71/accept-ca.py   # ACCEPT-CA-71: PASS (exit 0; V70-1..V70-5 + QUARANTINE 21/21/True; V70-3 words=25)
python3 -B reports/round-71/accept-d.py    # ACCEPT-D-69: PASS legs=8/8 (exit 0)
```

Read-only: the three counters contain no write calls (`grep -n "open(.*['\"]w\|write_text\|os.remove"`
returns nothing; only `accept-c.py:35` spawns `subprocess.run` for the declared checkers). Worktree
before/after: `?? .ufo/waves/round-71/w2/Filler37.md` only.

## Impacted axes

- **Wave-evidence integrity (A4, A6, A7)** — the wave-2 audit sentence is false as written and the
  wave-1 summary under-enumerates its own evidence by 10 seats. Neither touches claim C/Ca/D
  predicates, so no claim leg changes verdict; what changes is the evidence *description* that the
  round's receipts and lesson will inherit.
- Not impacted: claim C, Ca, D acceptance (all three counters PASS at HEAD), the S861–S873 row set,
  the quarantine verdict table (21/21), and the Gate legs.

## Tooling record

No installs or updates (python3/git present). No pacman transaction.
