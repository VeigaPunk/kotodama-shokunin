# CritMistakeRows — attack on `## Mistakes` (R73-M1..R73-M6), round 73

**Seat:** CritMistakeRows, wave 2 (FALSIFY), leaf. **Target:** `corpus/lessons/round-73.md:104-121`
(the six-row table at `:108-113` plus the sweep paragraph at `:115-121`).
**Revision attacked:** `0316b8883b4f8d44b8efd720140e7f52f734a102` (lane), base
`8841ad3b896a0227674fa0725b818c999118046f`, freeze `af65165`.
**Method:** every pointer opened; every red-before re-derived in a throwaway clone
(`/tmp/CritMistakeRows.KRgR`, `rev-parse --show-toplevel` = that dir); counters re-run at the
landing; the two wall measurements re-fetched live. No lane byte, index or jj/git state touched;
the only lane write is this file.

## Vocabulary and shape baseline (what a row must satisfy)

- `CORPUS.md:171-174`: one row per mistake, `class · evidence pointer · captured-by (the
  QUALITY.md criterion or protocol rule that should have caught it, or none) · fix`; classes from
  the `mistakes.md` §5 vocabulary: `vacuous, survivor, stale-premise, reference-drift,
  number-drift, scope, attribution, landing, provider` (`CORPUS.md:173-176`).
- `CORPUS.md:179-183`: "A claimed repair ships one red-before state in which the same command exits
  non-clean for the named reason, with the fix as the only delta; the observed failure text is
  committed."

## Per-row verdicts

| row | class in vocabulary | every pointer resolves | captured-by honest | fix shown able to fail | `fixed` true at 0316b88 | verdict |
|---|---|---|---|---|---|---|
| M1 landing | yes (`landing`) | yes (`spotcheck:65`, base tree, landing tree, `controls-ca.txt`) | defensible, with a caveat (F13) | red-before committed and re-derived; green reproduced but **not committed as a receipt** (MINOR F6b) | yes (TRACKED PASS at 0316b88) | **PASS with 1 MINOR** |
| M2 reference-drift | yes | yes (SCORECARD:1401, measures-ca.txt:29, spotcheck:66, L06, rerun receipt re-run) | yes in substance; "stamp only" understates QUALITY 17 (MINOR F12) | yes — rerun reproduces `PASS legs=12/12` at 21ad3088 | yes (ANNOTATE leg PASS, 9 rows) | **PASS with 1 MINOR** |
| M3 stale-premise | yes | **no** — the round-72 attribution is false (F1) | yes (QUALITY 21 has no UA field) | yes (QUALITY 22 + `quality22-controls.txt`) | yes | **FAIL — MAJOR (F1)** |
| M4 survivor | yes | yes — `SELFTEST: 10/11`, exit 1 reproduced at base | yes (`none`; QUALITY 19 requires `--lands`, not a selftest) | yes (freeze-time selftest receipts) | yes (round-72 counter untouched; round-73 receipts at `af65165`) | **PASS with 1 MINOR (F7 wording)** |
| M5 survivor | yes | yes | **no** — "the r1 selftest" is not a criterion/rule (F4) | **yes — re-derived byte-for-byte** | yes (guard + scenario 7b present; selftest 10/10 exit 0) | **PASS with 1 MINOR (F4)** |
| M6 scope | **no** — the defect is `vacuous`, not `scope` (F5) | yes for the four shapes (verified pre-repair at `85f17eb`; Ca SEPARABLE reproduced) | no — criterion 8 is *not* blind to shape (F6) | the repair description is false for 2 of 4 artifacts (F2); the criterion it adds is unexercised (F3) | partly | **FAIL — MAJOR (F2, F3)** |

## Findings

### F1 — MAJOR — M3 attributes a Springer/Cambridge wall reading to notes that never contained one

Row `corpus/lessons/round-73.md:110` says "wave-1 seats **and the round-72 Routed-to-73 notes**
read a Springer/Cambridge 'wall' from one UA each". The wave-1 half is true; the round-72 half is
false. The round-72 lesson contains no Springer or Cambridge token at all, and its only wall note is
UNESCO — the *opposite* direction (plain-curl walled, browser UA clean), which is the premise that
licensed the seats' one-UA reading.

```
$ grep -n -i -E 'springer|cambridge|10\.1007|10\.1017|S910|S894' corpus/lessons/round-72.md
(no output)
$ grep -n -i 'wall' corpus/lessons/round-72.md
103:- The UNESCO "live CAPTCHA wall" was a UA artefact: all eight element URLs serve HTTP 200 full
narrative under a browser-shaped UA; the wall appears only with a plain-curl UA. ...
$ grep -n -i -E 'springer|cambridge|wall' /home/vgpnk/Projects/shokunin/.ufo/reports/round-72/kotodama.md
11:- **K71-8** — Capoeira reject reason falsified ... (the wall is UA-gated) ...
55:**Post-landing erratum 3 (appended):** ... showed the UNESCO CAPTCHA wall was a UA artefact. ...
```

The wave-1 half does resolve, from the seats themselves (not from round 72):

```
$ sed -n '7,19p' .ufo/waves/round-73/w1/RevSowersAccess.md
Date of all probes: 2026-10-25. User-Agent for every live fetch recorded below as UA-B;
plain `curl` default UA was not used for any publisher fetch this round.
...
The publisher tier is indeed walled (Cambridge 429, Springer JS client challenge), but the
$ sed -n '41p' .ufo/waves/round-73/w1/ScoutAmendTriage.md | cut -c1-200
- S910 `https://doi.org/10.1007/978-3-032-03277-5_15` → 200 → `https://link.springer.com/10.1007/
978-3-032-03277-5_15` (JS challenge page, 3,038 bytes; not bypassed); ...
```

The row's *measurement* is true and reproduces today (see fetch record below), so the defect is the
attribution, not the numbers. **Smallest safe correction:** replace "and the round-72 Routed-to-73
notes" with the real sources — `.ufo/waves/round-73/w1/RevSowersAccess.md:8,19` and
`ScoutAmendTriage.md:41` — and, if the round-72 premise is wanted, cite the UNESCO note at
`corpus/lessons/round-72.md:103` for what it actually says (one direction, plain-UA).

### F2 — MAJOR — M6's fix says the artifacts were repaired "append-only / additively"; two of the four were not

Row `:113`: "the artifacts were repaired append-only / additively (gap-sweep.txt section [7],
validate-receipt.txt ids block, `map` key in id-renumber-map.json, README footer without claim-C
ids)". The commit that made the repair deletes 133 lines from the renumber map (a re-serialization,
not an addition) and rewrites the README footer line in place:

```
$ git diff --numstat 85f17eb 0316b88
233	133	.ufo/waves/round-73/assimilation/id-renumber-map.json
9	0	.ufo/waves/round-73/assimilation/validate-receipt.txt
1	1	corpus/QUALITY.md
1	1	corpus/README.md
1	0	corpus/lessons/round-73.md
7	0	reports/round-73/telemetry/gap-sweep.txt

$ git diff 85f17eb 0316b88 -- corpus/README.md | grep '^[-+]Registry'
-Registry: 799 → 804 rows (S876–S880, all mined, used-by exactly the two entries; ...)
+Registry: 799 → 804 rows (five new rows, all mined, used-by exactly the two entries; ...)
```

The in-place README-footer edit is *authorized* by the claim's APPENDONLY leg ("in-place edits
permitted only inside SKILL.md '## Gates and probes' or a README footer"), and the map is outside
every guarded file — so no leg is violated. But the row's description of the repair is wrong as
written. **Smallest safe correction:** "gap-sweep and validate-receipt appended; id-renumber-map
re-serialized (233+/133−, `map` key added); README footer edited in place under the APPENDONLY
footer exception".

### F3 — MAJOR — the criterion M6 adds (QUALITY 23 freeze-commit run) is not exercised by the round that adds it

M6's fix: "QUALITY 23 now also requires running the counter at the FREEZE commit (receipts present,
landing absent) so shape mismatches show before data". `corpus/QUALITY.md:77` does say that, and the
landing commit message says "QUALITY 23 freeze-commit run" — but no freeze-commit counter receipt
exists anywhere in the committed tree, and no committed command line runs a counter at `af65165`:

```
$ git ls-tree -r af65165 --name-only reports/round-73/telemetry/
reports/round-73/telemetry/census-start.txt
reports/round-73/telemetry/controls-c.txt
reports/round-73/telemetry/controls-ca.txt
reports/round-73/telemetry/gap-sweep.txt
reports/round-73/telemetry/selftest.txt
$ git ls-tree -r 0316b88 --name-only reports/round-73/telemetry/ | wc -l
13        # no freeze-commit receipt among them
$ git grep -n -- '--lands af65165' 0316b88
(no output)
```

`controls-c.txt` / `controls-ca.txt` are `lands == base` runs (base has neither claims nor ledger);
they cannot show artifact shape. So the new requirement is prospective only, and the commit message
overstates it. **Smallest safe correction:** file the freeze-commit run receipt (or state in the row
that the requirement binds from round 74 and round 73's shape defects were found by grading).

### F4 — MINOR — M5's `captured-by` is not a criterion or rule

Row `:112` fills `captured-by` with "the r1 selftest (blind to the class)". `CORPUS.md:172-174`
allows "the QUALITY.md criterion or protocol rule that should have caught it, or `none`". The row
itself says the r1 selftest *could not* see the class, so the field is self-contradictory. The
honest value is `none` (QUALITY 23 is the rule that now supplies the capture). Everything else in
M5 is sound — see the re-derivation under "Fixes re-derived".

### F5 — MINOR — M6's class is `vacuous`, not `scope`

`mistakes.md` §5 C03 "Scope overreach" is over-claiming beyond measurement (M022-M026: "~80% with no
measure named", a prediction refuted by its own test). C04 "Vacuous or inert verification" is a
probe/control that cannot fail or reads green vacuously (M027-M035). M6 is exactly the latter — the
do-nothing control "ran at `lands == base` only, where every artifact-shaped leg is red for the
single reason 'missing'", i.e. the control could not distinguish the failure classes. The vocabulary
word is `vacuous` (`CORPUS.md:174`).

### F6 — MINOR — M6's `captured-by` misreads criterion 8, which is *not* blind to artifact shape

Row `:113` says "QUALITY 8/9 (declared commands run on their declared input before dispatch) —
satisfied at base, blind to artifact shape". Criterion 8 names the shape class explicitly:

```
$ sed -n '33p' corpus/QUALITY.md | cut -c1-320
  8. **Declared inputs run before dispatch** — ... An input-shape error (missing manifest keys, an
unreadable file, unrecognized arguments) fails the declaration, not the round: correct the declared
command or input and re-run before dispatch; never substitute a different input after measuring.
```

The round's dry run was blind because it ran only where the artifacts were absent — not because the
criterion was. The distinction matters: a future round reading this row would not learn that
criterion 8 already makes a shape error a declaration failure.

### F6b — MINOR — M1's "green at the landing" has no committed receipt

M1's fix: "red-before: `reports/round-73/telemetry/controls-ca.txt` TRACKED FAIL at base, green at
the landing". The red is committed; the green is not — round 73 commits no `measures-ca.txt` /
`measures-c.txt` landing receipt at all. Its 13 telemetry files are the four control receipts
(`controls-c`, `controls-ca`, `-r2`, `-r3`), the three selftest receipts, the round-72 rerun, the
QUALITY 22 controls, `red-before-r3`, `census-start`/`census-end` and `gap-sweep`
(`git ls-tree -r 0316b88 --name-only reports/round-73/telemetry/ | wc -l` = 13). The green is *reproducible* (I reproduced it, below) and the round may still file the
receipt at closure; as landed, the pair's second half rests on a command in the claim, not on a
committed receipt.

### F7 — MINOR — M4's evidence clause about the round-72 report/SCORECARD does not resolve as written

Row `:111`: "the round-72 report and SCORECARD cite the counter's mode with no selftest receipt".
No committed round-72 artifact mentions `--selftest` at all:

```
$ grep -c -i 'selftest' reports/round-72/claims.json corpus/lessons/round-72.md
reports/round-72/claims.json:0
corpus/lessons/round-72.md:0
$ grep -n -i 'selftest' /home/vgpnk/Projects/shokunin/.ufo/reports/round-72/kotodama.md
(no output)
```

Under the reading "cite the counter's `--selftest` mode" the clause is false; under "cite the
counter without ever running its selftest" it is true. The substantive part (no selftest receipt in
`reports/round-72/telemetry/`) is true — `ls reports/round-72/telemetry/ | grep -i selftest` exits 1.
**Smallest safe correction:** "the round-72 records cite the counter's verdicts and ship no
`--selftest` receipt".

### F12 — MINOR — M2's "QUALITY 17/19 (stamp only)" understates criterion 17

Criterion 17 also names the round-72 defect's exact shape: "stamping a revision whose bytes fail the
receipt's own legs, is a calibration defect" (`corpus/QUALITY.md:55`). The round-72 receipt stamped
21ad3088 and its own legs read `FAIL legs=12/12`. So 17 did cover the receipt; what no criterion
covered is the SCORECARD verdict text — which the row's "not the verdict text" already says. The
parenthetical "stamp only" is the imprecise half.

### F13 — MINOR (judgment call) — M1's `none` for `captured-by` is arguable

`PROTOCOL.md:118-120`: "Landed means committed, so changes that exist only in a working tree do not
count for the round." That clause covers the two untracked seat reports; M1's parenthetical ("names
the report and the lane work, no leg lists the wave seat files") describes the missing
*enforcement*, not a rule that did not apply. `none` is defensible if the field means "a leg that
would have caught it"; under CORPUS's wording ("protocol rule that should have caught it") the value
should be that clause. I do not grade this a defect — the parenthetical is honest either way.

## Fixes re-derived (what did hold)

All commands run in the throwaway clone at the named revision, `--fleet-root` the fleet root.

**M1** — base tree lacks both seat reports, landing has both; the TRACKED leg is green at the
landing:

```
$ git ls-tree -r 8841ad3 --name-only | grep -E 'round-72/w1/(ScoutMergeScan|ScribeLesson)'   # exit 1, no output
$ git ls-tree -r 0316b88 --name-only | grep -E 'round-72/w1/(ScoutMergeScan|ScribeLesson)'
.ufo/waves/round-72/w1/ScoutMergeScan.md
.ufo/waves/round-72/w1/ScribeLesson.md
$ python3 -B reports/round-73/accept-ca.py --root . --lands 0316b8883b4f8d44b8efd720140e7f52f734a102 --fleet-root ... | grep -E 'TRACKED|ACCEPT-CA'
LEG PASS TRACKED
     paths=2 problems=[]
ACCEPT-CA-73: PASS legs=9/9
```

**M2** — the filed divergence is real and the rerun receipt reproduces:

```
$ sed -n '1401p' SCORECARD.md | cut -c1-120
| calibration | improved (claim Ca, records) | ... ACCEPT-CA-72 PASS legs=12/12 at the measured revision
$ grep -n 'ACCEPT-CA-72' reports/round-72/telemetry/measures-ca.txt
29:ACCEPT-CA-72: FAIL legs=12/12
$ # clone at 21ad3088, round-72 counter unchanged (sha f080c240...)
ACCEPT-CA-72: PASS legs=12/12
EXIT=0
```

**M3** — numbers reproduce exactly (fetch record below). **M4** — reproduced at base:

```
$ python3 -B reports/round-72/accept-c.py --selftest
SELFTEST: 10/11
--- clean fixture: expected PASS 10/10, got exit=1
...
LEG FAIL GROUND
     receipt missing: reports/round-72/telemetry/gap-sweep.txt
EXIT=1
```

**M5** — red-before re-derived with the guard as the only delta (3 lines removed, nothing else):

```
$ python3 -B accept-ca-noguard.py --selftest        # r3 with only the LEDGER_REL guard removed
selftest: worktree-only ledger (r2 bug class)
ERROR: --lands must be 40 hex
ERROR: base 8841ad3b896a0227674fa0725b818c999118046f is not a commit in /tmp/r73-ca-selftest-zvobskvx/lane
SELFTEST FAIL: wt-only LEDGER: got 'PASS' want 'FAIL'
EXIT=1
```

That is byte-for-byte the committed `reports/round-73/telemetry/red-before-r3.txt`, including the two
ERROR lines. The unmodified r3 at 0316b88 prints `SELFTEST OK: 10 scenarios`, exit 0.

**M6** — each pre-repair shape verified at `85f17eb`, and the Ca side reproduced:

```
$ git show 85f17eb:.ufo/waves/round-73/assimilation/validate-receipt.txt | grep -c 'S876\|S877\|S878\|S879\|S880'
0
$ git show 85f17eb:.ufo/waves/round-73/assimilation/id-renumber-map.json | python3 -c "..."
False ['assignments', 'assignment_order_rule', 'conditional_assignments', 'not_assigned']
$ git show 85f17eb:corpus/README.md | grep -n 'S876' | cut -c1-100
773:... rows (S876–S880, all mined, used-by exactly the two entries; ...
$ sed -n '44,48p' reports/round-73/telemetry/gap-sweep.txt      # section [4]: escaped regexes
grep -inE 'ojs\.unito\.it|philol\.msu\.ru|journals\.rudn\.ru|...' corpus/SOURCES.md
  -> 0 matching rows
$ # clone at e62d731 with counter r1
LEG FAIL SEPARABLE
     problems=['in-place added line cites S876', 'in-place added line cites S880']
```

## Missing rows (mistakes the table does not carry)

### G1 — MAJOR — routed defect R3 is repaired but never rowed

The table rows the round-72 spot-check's R1 (M1) and R2 (M2) and drops R3, which the round also
repairs (ledger pair L08). R3 is real at base:

```
$ sed -n '67p' corpus/lessons/round-72-verifier-spotcheck.md
- **R3** `SKILL.md` §Gates and probes registry stops at accept-\*-69 — no rows for accept-ca-70..72 / accept-c-70..72; add round-72 rows (and backfill or explain 70/71).
$ git show 8841ad3:SKILL.md | sed -n '697p' | cut -c1-60
| accept-o-69 | gate | `python3 -B reports/round-69/accept-o.py --root .` ...
$ git ls-tree -r 8841ad3 --name-only | grep -E 'reports/round-7[12]/accept-.*\.py'
reports/round-71/accept-c.py
reports/round-71/accept-ca.py
reports/round-71/accept-d.py
reports/round-72/accept-c.py
reports/round-72/accept-ca.py
$ grep -n 'R3' corpus/lessons/round-73.md
5:... plus the round-72 routed defects R1–R3). Frozen at
```

So the lesson names R1–R3 as the round's scope (`:5`) and rows only two of the three. Class:
`reference-drift` (a registry whose last row is not the truth), the same class M2 uses.

### G2 — MAJOR — three of 37 wave-1 seats returned nothing, and both pointers to their record dangle

`w1-results.json` carries 37 seats; 34 report files exist. The three missing seats include
`ScribeMistakes`, the seat chartered to draft this very table.

```
$ python3 -c "…spec items vs *.md files…"
spec items: 37
reports present: 34
missing: ['ConnectorSiblings', 'ScribeMistakes', 'ExecScratchMirror']
$ ls .ufo/waves/round-73/w1/ConnectorSiblings.md .ufo/waves/round-73/w1/ScribeMistakes.md .ufo/waves/round-73/w1/ExecScratchMirror.md
ls: cannot access ...: No such file or directory   (all three)
```

Both records are dangling. `w1-results.json` tells the reader to "read the seat report file in the
wave dir" for each of the three — there is none. The lesson says "dead seat, see the fleet report"
(`corpus/lessons/round-73.md:72`), and no round-73 fleet report exists:

```
$ python3 -c "…the three results entries…"
{"name": "ConnectorSiblings", "agent": "connector", "output": null,
 "note": "orchestrator kernel restarted mid-wave; seat output was delivered to the orchestrator
 session but not retained — read the seat report file in the wave dir"}
$ ls /home/vgpnk/Projects/shokunin/.ufo/reports/round-73/
audio.md
game-dev-3d.md
```

Class: `provider` (C13 operational abort — `mistakes.md:320-331`, "Capture: none fleet-level"), with
a `landing` edge (the seat work does not exist in the tree). The cause is stated in the results file
(kernel restart) and is exactly the kind of round-73 mistake the table was built to record; the row
would also explain why the table has no independent author.

### G3 — MINOR — the draft claims' R3 named two gates that never existed

The round-73 draft Ca text (and the wave-1 prompt derived from it) copied the spot-check's
`accept-ca-70..72 / accept-c-70..72` wording; no round-70 counter bytes exist. Wave-1 caught it and
the freeze records the fix as `pre_data_corrections.F4`, but no Mistakes row carries it:

```
$ ls reports/round-70/ | head
claims.json  corrections-r69.md  telemetry        # no accept-*.py
$ sed -n '13p' .ufo/waves/round-73/w1/ScribeSkillGates.md | cut -c1-220
1. **Five rows are missing, not six.** ... reports/round-70/ contains **no** `accept-*.py` ...
So the R3 wording "accept-ca-70..72 / accept-c-70..72" names two gates that never existed ...
$ python3 -c "…pre_data_corrections…"
F4 | RevClaimsFidelity F4 + ExecLedger | R3 names the gates whose counters are tracked ...
```

Note the source is still filed: `corpus/lessons/round-72-verifier-spotcheck.md:67` still says
"backfill or explain 70/71", and the lesson's own sweep paragraph (`:115-121`) does not mention it.
Class: `reference-drift` / `stale-premise`.

### G4 — MINOR — the wave-1 prompt carried two stale premises (S882 booklet; one-directional UA rule)

```
$ grep -o '.\{60\}announcement booklet.\{60\}' .ufo/waves/round-73/w1/spec.json
... against the PDF; list claims the PDF does NOT carry. Check the row's tier-B reason (a
publisher-style announcement booklet, not the book). Report must contain: ...
$ grep -o '.\{0,120\}often walled.\{0,200\}' .ufo/waves/round-73/w1/spec.json
... when you fetch a live page, record the exact User-Agent you used; a plain-curl UA is often
walled where a browser-shaped UA (Mozilla/5.0 ... Chrome/130.0 Safari/537.36) is not — retry with it
before ruling a source unreachable, never bypass a ...
```

The booklet premise was falsified by ScoutS882 (the 184-page monograph) and the correction is
recorded in `claims.json` S882 and the lesson Gate, but the table does not row it. The UA sentence
is the *root cause* of M3: it tells seats to retry only in the browser-UA direction, which is exactly
the licence under which `RevSowersAccess.md:19` concluded "The publisher tier is indeed walled" from
one UA. Both are `stale-premise`.

**Correction to the assignment's hypothesis:** no wave-1 prompt states the Springer wall as
UA-independent. The prompts treat it as (a) an open hypothesis to falsify (`RevSowersAccess` prompt:
"Falsifiable hypothesis H: ... cannot be opened by ORDINARY means"), or (b) a bare DOI with no wall
claim (`ScoutAmendTriage`). The defect is the one-directional retry rule, not a flat assertion.

## Fetch record (F1 re-measurement)

Downloaded to `/tmp/CritMistakeRows/` only; nothing installed. No challenge was passed, no
automation, no captcha.

| UA (exact) | URL | status | bytes | marker |
|---|---|---|---|---|
| `curl/8.7.1` | `https://link.springer.com/chapter/10.1007/978-3-032-03277-5_15` | 200 | 325225 | `Client Challenge` 0 |
| `curl/8.7.1` | `https://link.springer.com/10.1007/978-3-032-03277-5_15` | 200 | 325225 | 0 |
| `curl/8.7.1` | `https://doi.org/10.1017/cnj.2024.21` | 429 | 1302 | 0 |
| `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36` | `https://link.springer.com/chapter/10.1007/978-3-032-03277-5_15` | 200 | 3038 | `Client Challenge` 1 |
| `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36` | `https://link.springer.com/10.1007/978-3-032-03277-5_15` | 200 | 3038 | 1 |
| `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36` | `https://doi.org/10.1017/cnj.2024.21` | 429 | 1302 | 0 |

M3's four numbers and QUALITY 22's grounding are exact.

## What I could NOT check

- **The round-73 fleet report's future contents.** "see the fleet report" may resolve at closure;
  at `0316b88` the path `/home/vgpnk/Projects/shokunin/.ufo/reports/round-73/kotodama.md` does not
  exist. I report the pointer as unresolvable *now*, not as permanently false.
- **A post-`0316b88` Ca landing receipt.** I attacked only up to the named revision; if wave 2
  files `measures-ca.txt` later, F6b closes.
- **The round-72 close-time tree.** I verified base `8841ad3` lacks both seat reports (what the row
  cites); I did not reconstruct the round-72 close commit itself.
- **The staged amendments' full text** beyond the register rows and the two amendments' headings I
  grepped in `/home/vgpnk/Projects/shokuknow` (read-only; no campaign tools run).
- **Sibling w2 seat claims** (e.g. `RevLessonGate.md`'s reproductions) — not re-verified; I derived
  my own.
- **The Gate locators** (S877 printed p. 10, S879 PDF p. 5, S880 §3 p. 5) — outside this seat's
  item; not opened.
- **M4's "the round-72 report"** — no lane round-72 report file exists (`reports/round-72/` holds
  only the counters, claims and telemetry), so I read the fleet report; if a different artifact was
  meant, I did not find it.

## Tooling

Nothing installed or upgraded (no pacman, no uv/npx/official binary). Downloads: three URLs above,
both UAs, under `/tmp/CritMistakeRows/`; experiment clone `/tmp/CritMistakeRows.KRgR` (throwaway,
detached checkouts only).
