# ScribeMistakes — round 77, wave 1

Seat: ScribeMistakes (leaf scribe, no delegation). Lane `/home/vgpnk/Projects/shokunin/kotodama-shokunin`,
lane base `211f9526800906e0c585d878d265c37e5e090c15`. Date 2026-10-27. Nothing was written outside
`.ufo/waves/round-77/w1/stage/ScribeMistakes/` and this file; `CLAIMS-DRAFT.md` was read only.

## Verdict

**Delivered: 12 mistake rows** for `corpus/lessons/round-77.md` `## Mistakes`, covering all six routed
defects of the round-76 closure (§5.1–§5.6) and both §1 conformance defects, plus one row (R77-M3) the
mining surfaced from the same receipts. One of the twelve has an executed red-before inside this round
(R77-M12, validator probe); one has an executed red-before on r76 bytes (R77-M10, `LEGCOUNT` refusal);
ten are explicitly `owed`, each named with its fixture and expected red line, because **no round-77
counter exists yet** (`ls reports/round-77/` → `telemetry/` only). Answer to the posed question: the
in-place-report-rewrite class does **not** belong in `corpus/QUALITY.md`; a checklist line is proposed
with a one-command check.

Rows file: `.ufo/waves/round-77/w1/stage/ScribeMistakes/mistakes.md`.

## What was mined

- `corpus/lessons/round-76-verifier-spotcheck.md` (committed at the lane base by `protocol-shokunin`,
  `211f952`; `git log -1 --format='%H %an %ad %s' -- corpus/lessons/round-76-verifier-spotcheck.md`
  → `211f9526800906e0c585d878d265c37e5e090c15 protocol-shokunin Tue Oct 27 22:17:31 2026 -0300 round-76
  verifier spot-check (integrator, hyaku): non-author admit/reject`).
- The receipts each §5 item names, re-opened at the revision they name: `reports/round-76/telemetry/`
  (`measures-c-final-c28ea.txt`, `measures-ca.txt`, `controls-c.txt`, `controls-ca.txt`, `selftest-ca.txt`),
  `reports/round-76/accept-c.py`, `reports/round-76/ledger.json`,
  `.ufo/waves/round-76/w1/stage/L1/{freeze-control-legcount-redbefore,pre-data-counter-repair,freeze-ca-control-ledger-redbefore}.txt`,
  `.ufo/waves/round-76/w2/{ExecMapAudit.md,CritRowDiff.md}`, `.ufo/waves/round-76/w1/CritLedgerDesign.md`.
- The rules that were supposed to catch them: `corpus/QUALITY.md`, `/home/vgpnk/Projects/shokunin/PROTOCOL.md`,
  `MISSION.md`, the round-77 prompt, `~/.omp/agent/config.yml`, and the dispatch validator
  `/home/vgpnk/Projects/ufo-fsd-alpha/scripts/ufo-swarm-wave.mjs`.

## Measurements (command → raw output)

Every number below is a run, not a carried value.

**C claim, ROWS and COLLCHECK (r76 final lands `c28ea2194ae6d0c874c011d3b1b59409a20bd422`).**

```
$ grep -n 'LEG FAIL ROWS' -A2 reports/round-76/telemetry/measures-c-final-c28ea.txt
25:LEG FAIL ROWS
26:     registry line added outside the frozen row_set: '- calendar-standard design — S896 → S895 → S894: start with '; registry line added outside the frozen row_set: '**State-standard calendar compilation (round 76).** Question
$ grep -n 'LEG FAIL COLLCHECK' -A1 reports/round-76/telemetry/measures-c-final-c28ea.txt
38:LEG FAIL COLLCHECK
39:     map record S938 -> S895 names a document the row does not: https://openstd.samr.gov.cn/bzgk/std/showGb?type=online&hcno; ids=817 staged=132 collisions=35 guard=ok/ok map=7
$ grep -n 'ACCEPT-C' reports/round-76/telemetry/measures-c-final-c28ea.txt
45:ACCEPT-C-76: FAIL legs=11/13
```

The two "out-of-set" lines are the round's own required registry edits, and they landed **during the
freeze chain**, not with the data:

```
$ git log --format='%h %s' -S 'calendar-standard design — S896' -- corpus/SOURCES.md
cab5247 round-76: correct base ground and mirror receipts
$ git log --format='%h %s' -S 'State-standard calendar compilation (round 76).** Question' -- corpus/SOURCES.md
cab5247 round-76: correct base ground and mirror receipts
```

`cab5247` is F2 of the freeze chain (`df0f0309` is F4; chain at `LOG.md:4335`), so from the freeze on the
declared ROWS target
("adds exactly S894-S896") was unsatisfiable. The implementation that rejects them is a whole-file line
multiset diff (`reports/round-76/accept-c.py:1588-1605`, message at `:1603`), while the frozen claim text
(`git show df0f0309:reports/round-76/claims.json`, C `legs[1]`) only constrains *rows*.

**Both red legs were already red at `lands == freeze`.**

```
$ grep -n 'LEG FAIL ROWS\|LEG FAIL COLLCHECK\|ACCEPT-C\|# expected' reports/round-76/telemetry/controls-c.txt
30:LEG FAIL ROWS
48:LEG FAIL COLLCHECK
55:ACCEPT-C-76: FAIL legs=1/13
57:# expected: exit=1, FAIL on the data legs and PASS on FROZENCFG
```

At that control the two ROWS diagnostics are the *same two lines* as at lands, and COLLCHECK's cause is
the frozen map record, not the missing entry — so the C control's expectation line could not separate
"map is wrong" from "data is absent".

**Ca claim: the freeze control's own expectation was falsified and the freeze stood.**

```
$ grep -n 'LEG FAIL\|LEG PASS\|ACCEPT-CA\|# expected' reports/round-76/telemetry/controls-ca.txt
40:LEG FAIL LEDGER
42:LEG PASS BASEMISMATCH
44:LEG FAIL REPAIR
46:LEG FAIL ANNOTATE
48:LEG FAIL NOSTUB
50:LEG PASS APPENDONLY
52:LEG FAIL R1EXEMPT
54:LEG FAIL SEPARABLE
56:LEG PASS RECEIPTS
58:LEG FAIL COMBINED
61:LEG PASS FROZENCFG
63:LEG PASS STAMP
65:ACCEPT-CA-76: FAIL legs=5/12
67:# expected: exit=1, FAIL on REPAIR/ANNOTATE/R1EXEMPT, PASS on FROZENCFG and LEDGER
```

Line 40 is `LEG FAIL LEDGER`; line 67 expects `LEDGER` to PASS. The expectation also under-describes
the red set: it names three expected-red legs (`REPAIR/ANNOTATE/R1EXEMPT`) while
`grep -c '^LEG FAIL'` counts 8 red at the F0 control and 7 at this one (`ACCEPT-CA-76: FAIL legs=4/12`
and `5/12`), so 4–5 red legs appear nowhere in the expectation. The ledger never changed between the
first freeze and the Ca lands:

```
$ for r in b4965d5c0f3c2609a3de8fce63750bf02bda19e4 df0f0309d61e5485bb17035d3f8791b1e6a11d40 a43ed807ea38b5fc5a7875a839d576cea73aba7c; do printf '%s ' "$r"; git show "$r:reports/round-76/ledger.json" | sha256sum; done
b4965d5c0f3c2609a3de8fce63750bf02bda19e4 d609c8b06b9abfa29701ddb12e4f4c6cdace7a50dc7025a6f48a9327bf071677  -
df0f0309d61e5485bb17035d3f8791b1e6a11d40 d609c8b06b9abfa29701ddb12e4f4c6cdace7a50dc7025a6f48a9327bf071677  -
a43ed807ea38b5fc5a7875a839d576cea73aba7c d609c8b06b9abfa29701ddb12e4f4c6cdace7a50dc7025a6f48a9327bf071677  -
```

The Ca lands receipt then reports the same limbs:

```
$ grep -n 'LEG FAIL\|ACCEPT-CA' reports/round-76/telemetry/measures-ca.txt
4:LEG FAIL LEDGER — L76-13 ANNOTATE stated_at path `corpus/knowledge/myth-symbol/narrative-structure-frameworks.md` is outside the frozen append-only allowlist; L76-19 stated_text is not found at the specified base lesson line.
6:LEG FAIL REPAIR — L76-16 `statement_after` no-match in SKILL.md.
7:LEG FAIL ANNOTATE — three rows unannotated because L76-19/20/21 `rederive` commands are not executable under the frozen argv parser; L76-20/21 treat the base revision as a path operand and L76-19 treats `chars=` as a path operand.
8:LEG FAIL NOSTUB — stubs L76-19:rederive-cmd, L76-20:rederive-cmd, L76-21:rederive-cmd.
10:LEG FAIL R1EXEMPT — green/red receipts `reports/round-76/telemetry/r1exempt-green.txt` and `r1exempt-red.txt` are not committed at Ca-lands.
11:LEG FAIL SEPARABLE — L76-13's stated_at path is a forbidden read (`corpus/knowledge/**`).
13:LEG FAIL COMBINED — the C-owned README heading change at line 410 is outside Ca's frozen APPENDONLY exemption; the `owned_inplace` config has no valid line number.
16:ACCEPT-CA-76: FAIL legs=5/12
```

The executability predicate itself existed and had red fixtures before the freeze; only the *actual*
ledger was not checked by any seat:

```
$ grep -n 'SELFTEST' reports/round-76/telemetry/selftest-ca.txt
44:SELFTEST OK: 170 checks across 43 scenarios reported-fail=0: do-nothing, clean, lands-eq-base, combined-required, scratch-noroot, legcount, legorder, stub-rows, no-rederive, annotate-other-token, rederive-backtick, … constant-printer, out-of-clone, dead-pin, …
45:SELFTEST: 170/170
$ grep -n 'unrun' .ufo/waves/round-76/w1/CritLedgerDesign.md
50:… No checks of round-76 counter or final ledger run (unrun).
```

**Frozen leg list (routed defect 5).**

```
$ grep -n 'frozen legs' reports/round-76/telemetry/measures-c-final-c28ea.txt
12:# frozen legs: 13 (ENTRIES,ROWS,REPOINTED,GATE,EVIDENCE,REJECTS,GROUND,CITEDLINES,CENSUS,INDEX,COLLCHECK,FROZENCFG,INDEX)
$ sed -n '6381,6397p' reports/round-76/accept-c.py
LEGS = (
    ("ENTRIES", leg_entries),
    ("ROWS", leg_rows),
    …
    ("INDEX", leg_index),
    ("COLLCHECK", leg_collcheck),
    ("FROZENCFG", leg_frozencfg),
    ("INDEX", leg_index),
)
$ sed -n '6,8p' .ufo/waves/round-76/w1/stage/L1/freeze-control-legcount-redbefore.txt
REFUSED: LEGCOUNT: the frozen claims.json lists 13 legs (ENTRIES,ROWS,REPOINTED,GATE,EVIDENCE,REJECTS,GROUND,CITEDLINES,CENSUS,INDEX,COLLCHECK,FROZENCFG,INDEX); this counter implements 13 (ENTRIES,ROWS,REPOINTED,GATE,EVIDENCE,REJECTS,GROUND,CITEDLINES,CENSUS,SCRATCHMIRROR,COLLCHECK,FROZENCFG,INDEX)
ACCEPT-C-76: FAIL legs=0/13 (refused: LEGCOUNT: …)
exit=2
```

**Filed-report rewrite (routed defect 6 / §1 defect 1), in the fleet repo.**

```
$ git -C /home/vgpnk/Projects/shokunin log --format='%h %an %s' -- .ufo/reports/round-76/kotodama.md
1cd8e33c kotodama-shokunin round-76: correct final counter command
d7f0596d kotodama-shokunin round-76: kotodama report
$ git -C /home/vgpnk/Projects/shokunin show --stat --format='%H %an %s' 1cd8e33c | sed -n '1,6p'
1cd8e33c068ae977ac400845fd806f2933391f82 kotodama-shokunin round-76: correct final counter command
 .ufo/reports/round-76/kotodama.md | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
```

The deleted byte is inside an already-filed sentence (`-` `…--work /fast/scratch/hyaku/kotodama-r76/final-c-counter`,
`+` `…final-c28ea-counter`), against `/home/vgpnk/Projects/shokunin/PROTOCOL.md:134-137` ("never a rewrite
of the filed bytes, labelled or silent").

**Planner role and route table (§1 defect 2).**

```
$ grep -n '1× planner' .ufo/prompts/kotodama-round-77.md
86:- 1× planner, 1× connector (sibling-overlap scan)
$ sed -n '345,348p' /home/vgpnk/Projects/shokunin/.ufo/prompts/kotodama-round-77.md
   **Planner seat (orchestrator ruling 2026-10-19):** the validator rejects `planner` — a
   frozen-topology seat, never a swarm role. You, the L1, hold the canonical §3 planner seat; a
   bounded planning data-walk may ride a scout, connector or revenger item. Record that mapping in
   the report; never bypass validation to add a planner.
$ grep -rln 'unknown_role' .ufo/waves/round-76 reports/round-76
   (no output; grep exit 1 — no refusal receipt existed in r76)
```

Executed probe this round (stage receipt `probe-roles.txt`; imports the validator module, writes nothing
outside seat scratch):

```
$ node probe-roles.mjs
SWARM_ROLES size= 10 has(planner)= false
control: real spec items= 36 roles= scout,executor,scribe,critic,reviewer,mutation-tester,sentinel,connector,revenger
control: planSwarmWave(real spec) OK agents= 0
mutant: planSwarmWave(items[0].role=planner) REFUSED SwarmWaveError code=unknown_role | items[0].role "planner" is not a swarm role
exit=0
```

Route-table drift, prompt restatement vs live table:

```
$ sed -n '151,153p' /home/vgpnk/Projects/shokunin/.ufo/prompts/kotodama-round-77.md
- **Routing: the map live at the end of run 9, unchanged** (never pass `model`): task `@m_kfc`;
  main/planner `@m_opus`; executor `@m_mim`; critic/scout/reviewer/mutation-tester `@m_kfc`;
  security-reviewer `@m_zfl`; scribe/sonic/simplifier/revenger/labrat/sentinel `@m_flash`; connector
$ sed -n '351,368p' /home/vgpnk/.omp/agent/config.yml | grep -E 'task:|critic:|scout:|reviewer:|mutation-tester:|connector:|security-reviewer:'
    task: "@m_swe"
    mutation-tester: "@m_zfl"
    scout: "@m_swe"
    critic: "@m_swe"
    reviewer: "@m_zfl"
    connector: "@m_haiku"
    security-reviewer: "@m_zfl"
```

Six named roles drift (`task`, `critic`, `scout`, `reviewer`, `mutation-tester`, `connector`);
`main`/`planner` (`@m_opus`) and `security-reviewer` (`@m_zfl`) agree. The prompt itself makes
`config.yml` the authority (`:349-350` Routing is `task.agentModelOverrides` … The role decides the
route), so the restated table is status-neutral — recorded in R77-M12, not graded.

**The posed question: QUALITY criterion or checklist line?**

```
$ grep -c -E '^[0-9]{1,2}\. \*\*' corpus/QUALITY.md
29
$ grep -oE '^[0-9]{1,2}\. \*\*' corpus/QUALITY.md | tail -1
29. **
$ grep -c '^30\.' corpus/QUALITY.md
0
$ grep -c -i 'lane report' corpus/QUALITY.md
0
$ grep -n -i -E 'filed report|erratum|report-correction' corpus/QUALITY.md
141:| the same row with 「非凡特性来自最初造物主」 substituted | 1 | `MISFILED reports/round-74/evidence/S883.txt count=1 (reason asserts absence)` |
```

Line 141 matches only because `MISFILED reports` contains `FILED reports`; it is a fixture cell, not a
criterion. So: **no** QUALITY criterion — a criterion gates corpus admission and has no corpus artifact
here; the obligation is the *record* rule at `PROTOCOL.md:134-137`; and slot 30 is already being drafted
by seat `ScribeQuality30` for "ledger pairs execute" (`grep -c '^30\.'` → `0` at base, so the slot is free
but spoken for). Proposed installable line, in the rows file:

> **Filed reports are append-only.** A correction to a filed round report lands as (a) an entry in the
> correcting round's report, or (b) an erratum appended after the filed bytes in its own commit, naming
> the text it supersedes. Never rewrite the filed bytes. Check: `git -C <fleet-root> log --format='%h %s'
> -- .ufo/reports/round-<N>/<lane>.md` lists one filing commit per attempt; every later commit touching
> that file must print `0` deletions in `git -C <fleet-root> show --numstat <commit> --
> .ufo/reports/round-<N>/<lane>.md`.

Suggested homes (both outside this seat's write scope): round-prompt §4 *Report contract* as a closing
bullet, and the `LOG.md` `## Round 77` conformance bullets.

## Findings the L1 needs before the freeze

1. **Leg lists are still hand-typed in prose** — the `LEDGELIST?` stopper is closed by the 22:33 DRAFT
   revision (`sha256 ed249cdf9a089eb201b6e2411c77662748df789f42b140b3fd424e43c392fa8b`, 8456 bytes):
   claim C now names the 13 lineage legs with `SCRATCHMIRROR` and "exactly one INDEX", so the r76 refusal
   shape cannot recur by accident. The residual risk is the class R77-M10 fixes — both claims still
   enumerate the names by hand (C: 13, Ca: 12). Generate `legs[]` from the counter's table at freeze and
   keep the LEGCOUNT assert (`ExecFreezeChecklist` already emits it).
2. **Two r76 freezes stood over a red control they had written as green.** R77-M3 is the row; the r76
   `controls-ca.txt` at `df0f0309` is a ready-made red fixture for a per-leg expected-green freeze gate.
   Without that gate, round 77 can repeat the shape with a red `LEDGER`.
3. **R77-M9 has no mechanism in the draft.** The `row_set` is richer but no leg closes the map over the
   *staged* side; `ExecMapAudit` documents three residue classes from r76. Either add a `COLLCHECK`
   closure limb or declare the clause review-only (QUALITY 11 forbids a weaker stand-in).
4. **No r77 red proof exists yet**, by construction: `ls reports/round-77/` prints `telemetry/` only, and
   `reports/round-77/telemetry/` holds `census-start.txt`. The ten `owed` rows each name their fixture and
   expected red line so the freeze can close them.
5. **R77-M6 and the in-flight QUALITY 30 must not diverge** (both describe the same argv-executability
   contract). `ScribeQuality30`'s draft and the `LEDGER` leg text should be diffed once, before freeze.
6. **The D2 quote locator points one page past the quote** (found first by `ScribeLesson-8`, who holds it
   as their own row; independently confirmed here). `CLAIMS-DRAFT.md` says "§3 ¶1, journal p.115 / PDF
   p.5". The live PDF — plain `curl/8.x` UA, HTTP 200, 417093 bytes, sha256
   `5d1bfa5a5f01bee68e090155ed683d848e6f75dbc456b8b631be81c1fa8d29bc`, 13 pages — carries the phrase on
   **PDF p.4 / journal p.114**: one hit across 13 pages, zero hits on PDF p.5 (`p5.txt:3` carries the
   printed label `115`). The sentence opens "According to Kałużyńska (2008, pp. 223, 232), there were
   altogether 88 terms …", so the 10-word draft quote is a mid-sentence span that drops that attribution
   clause. Receipt: `.ufo/waves/round-77/w1/stage/ScribeMistakes/d2-locator-sweep.txt`. Fix the locator
   to p.114 / PDF p.4 and either keep the span (it locates there) or quote from the sentence start and
   re-count the words.

## Corrections after peer review (2026-10-27, same session)

Two defects in this seat's first draft were found by `ScribeLesson-8`; both are corrected above and
verified by the commands shown here.

1. **R77-M7 cited the `RECEIPTS` red at the wrong revision.** The first draft said
   `controls-ca.txt:56` showed `LEG FAIL RECEIPTS`; it does not.

   ```
   $ sed -n '56,57p' reports/round-76/telemetry/controls-ca.txt
   LEG PASS RECEIPTS
        rev=012e8d3c8b92 combined=4f5e3b2535c2 receipts=['accept-ca-75=05a10a4e745e'] problems=[]
   $ grep -n 'LEG FAIL RECEIPTS' -A1 .ufo/waves/round-76/w1/stage/L1/freeze-ca-control-ledger-redbefore.txt
   56:LEG FAIL RECEIPTS
   57-     rev=012e8d3c8b92 combined=4f5e3b2535c2 receipts=[] problems=['receipt reports/round-76/telemetry/accept-ca-75-at-lands.txt is not committed at lands']
   ```

   The row now records `RECEIPTS` red at the **F0** control and green at the final freeze, with
   `R1EXEMPT` red at both. The lesson feeds R77-M7's own class: a leg verdict quoted from a receipt must
   name the receipt's freeze revision, not only the file.

2. **The `LEDGELIST?` stopper came from a superseded draft.** `CLAIMS-DRAFT.md` was revised at 22:33,
   after this seat's 22:27 read: now 8456 bytes, `sha256 ed249cdf…`, and
   `grep -n 'LEDGELIST' .ufo/waves/round-77/CLAIMS-DRAFT.md` prints nothing (exit 1). R77-M10 and
   finding 1 record the revised state; the row's class (hand-typed leg list) survives, the token claim
   does not.

## Out of scope / unrun

- No round-77 counter, ledger, claims or fixture was run or created; no r77 leg is claimed to have fired.
- The lane's git/jj state, `LOG.md`, `SCORECARD.md`, `SKILL.md`, `SHONEN.md`, `corpus/**`,
  `reports/round-76/**`, `reports/round-77/**` and the fleet repo were not modified. The only fleet-repo
  reads were `git log/show` and file reads.
- Tools installed or upgraded: **none**. pacman not run. Both seat scratch directories
  (`/fast/scratch/hyaku/kotodama-r77/ScribeMistakes` for the validator probe and
  `…/ScribeMistakes-verify` for the D2 PDF) were deleted after `probe-roles.txt`/`probe-roles.mjs` and
  `d2-locator-sweep.txt` were copied into the stage directory.

## Artifacts

| path (lane-relative) | what |
|---|---|
| `.ufo/waves/round-77/w1/stage/ScribeMistakes/mistakes.md` | the 12 draft rows, the defect→row map, the owed red-before checklist, the QUALITY-vs-checklist decision and the proposed line |
| `.ufo/waves/round-77/w1/stage/ScribeMistakes/probe-roles.txt` | executed validator probe receipt (control accepted, `planner` mutant refused `code=unknown_role`) |
| `.ufo/waves/round-77/w1/stage/ScribeMistakes/probe-roles.mjs` | the probe script (imports the validator module by absolute path; no writes) |
| `.ufo/waves/round-77/w1/stage/ScribeMistakes/d2-locator-sweep.txt` | executed D2 PDF receipt — fetch status/size/sha256, 13-page sweep (phrase on PDF p.4 only), printed journal labels 114/115, sentence context with the dropped attribution clause |
| `.ufo/waves/round-77/w1/ScribeMistakes.md` | this report |
