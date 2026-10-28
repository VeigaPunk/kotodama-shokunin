# RevengerHistory — acceptance-counter failure history, rounds 72–76

Seat: `RevengerHistory` (wave 1, kotodama round 77 / hyaku run 10). Lane: `kotodama-shokunin`, base
`211f9526800906e0c585d878d265c37e5e090c15`. Read-only over committed bytes; no counter was executed and no
lane/fleet byte was written except this file. No scratch directory was created (no fixture, no clone, nothing
to delete). No source was opened online: this seat's evidence is the lane's own record.

Purpose: extract every *acceptance-counter failure class* the lane hit in rounds 72–76, name the leg + round +
root cause, separate recurrence from first appearance, and check the round-77 DRAFT claims against the fix
surface that already exists (QUALITY criteria 23–29).

## 0. What this seat read

- `LOG.md:4278-4349` (rounds 72–76 entries).
- `corpus/lessons/round-72-verifier-spotcheck.md`, `…-73-…`, `…-74-…`, `…-75-…`, `…-76-…`.
- `corpus/lessons/round-73.md` `## Mistakes`, `round-74.md` `## Mistakes`, `round-75.md` `## Mistakes` +
  `## Routed to round 76`, `round-76.md` `## Mistakes` + `## Routed to round 77`.
- `reports/round-7{2,3,4,5,6}/telemetry/*` verdict and leg lines; `reports/round-76/measures-ca.txt`,
  `measures-c-final-c28ea.txt`, `controls-c.txt`, `selftest-c.txt`, `selftest-ca.txt`.
- `reports/round-7{3,4,5,6}/claims.json` frozen leg lists; `reports/round-7{4,5,6}/ledger.json`;
  `reports/round-76/accept-c.py` (`leg_rows`, `leg_collcheck`, `urls_compatible`, `leg_index`),
  `reports/round-76/accept-ca.py` (operand validator, rederive parse).
- `corpus/QUALITY.md` criteria 20–29; `corpus/SOURCES.md` header + `## Paths` / `## Search log`;
  `reports/round-73/counter-revisions.md`; `.ufo/waves/round-77/CLAIMS-DRAFT.md`.

## 1. Counter timeline (measured verdict lines only)

| round | claim C at its lands | claim Ca at its lands | red legs (polarity) |
|---|---|---|---|
| 72 | `ACCEPT-C-72: PASS legs=10/10` (`reports/round-72/telemetry/measures-c.txt:15`) | `ACCEPT-CA-72: FAIL legs=12/12` (`measures-ca.txt:29`); later rerun `PASS 12/12` (`reports/round-73/telemetry/measures-ca72-rerun.txt:34`) | Ca: REPORTCORR, REPORTLAST — **false reds** (report not yet landed) + missing receipt |
| 73 | no landing receipt committed; only `ACCEPT-C-73: FAIL legs=1/11` (`controls-c.txt:39`) | only `FAIL legs=5/9` / `4/9` controls; PASS 11/11 and 9/9 exist only in wave-2 seat reports, later re-run at `reports/round-74/telemetry/accept-c-73-at-lands.txt` and `accept-ca-73-at-lands.txt` | **receipt-absent** (evidence class, not a data leg) |
| 74 | `PASS legs=13/13` (`measures-c.txt:36`) | `PASS legs=11/11` at its own lands (`measures-ca.txt:48`); `FAIL legs=10/11` at the combined head (`measures-ca-head.txt:48`) | Ca: APPENDONLY — **false red** on a contract-permitted `used-by` cell |
| 75 | `PASS legs=13/13` (`measures-c.txt:43`) | `PASS legs=12/12` (`measures-ca.txt:52`) | none at lands; `r1exempt-{green,red}.txt` show the exemption both ways (`FAIL 6/12`, `FAIL 5/12`) |
| 76 | `FAIL legs=11/13` (`measures-c-final-c28ea.txt:45`) | `FAIL legs=5/12` (`measures-ca.txt:16`) | C: ROWS, COLLCHECK — **false reds** (claim/counter scope); Ca: LEDGER, REPAIR, ANNOTATE, NOSTUB, R1EXEMPT, SEPARABLE, COMBINED — **true detections** of claim/ledger defects |

Polarity matters for the r77 design: the r76 C failure is a *scope* failure, the r76 Ca failure is an
*authoring* failure. A single fix cannot close both.

## 2. History table — every class, its leg, its rounds, its root cause

`first` = first round the class is on record; `recurs` = rounds it reappears in, including `first`.
`fix` = what has landed; `—` means no criterion in 23–29 covers it.

| id | class (one line) | leg(s) / artifact | first | recurs | root cause | landed fix |
|---|---|---|---|---|---|---|
| **H1** | **receipt-absent**: a declared receipt/fixture is not committed at the revision its leg reads | REPORTLAST/REPORTCORR (Ca), RECEIPTS/TRACKED (Ca), R1EXEMPT (Ca) | r72 | 72, 73, 74, 76 | artifact written after the freeze, or never; the leg reads committed bytes | none in 23–29 (23 = selftest receipt only; 25(b) = junk/control receipts only) |
| **H2** | **statement→artifact drift**: a filed token/number is not at, or not equal to, the artifact+revision the sentence names | LEDGER, BASEMISMATCH, REPAIR, ANNOTATE; SCORECARD rows | r72 | 72, 73, 74, 75, 76 | statement carried from a draft or probe into a sentence about committed bytes; no build-time re-derivation at the named line | **QUALITY 29** (r76, after the fact) |
| **H3** | **unexecutable declared command**: the ledger's `rederive` string is not the argv that runs, and not runnable as written | ANNOTATE, NOSTUB | r76 | 76; sibling r75 (published measuring command omitted `--combined` and printed FAIL — r75 spot-check §2 caveat) | `rederive` is a hand-typed shell string while the validated form is an argv array; an unquoted multi-token regex and a 40-hex revision shift operand roles | none in 23–29 (criteria 8/9 predate and cover "run before dispatch") |
| **H4** | **calibration pair reads a claim-C path**: `stated_at` names a file the sibling claim owns | LEDGER (allowlist limb) + SEPARABLE | r76 | 76 | ledger built from claim-C-adjacent text without checking the frozen allowlist/forbidden-read set | **QUALITY 7** (since r49) + the r76 claim's own allowlist |
| **H5** | **frozen leg list ≠ implemented leg table** | LEGCOUNT refusal / FROZENCFG | r73 | 73, 76 | leg list hand-typed separately from the leg table | **QUALITY 26** (LEGCOUNT refusal) + **25(c)** — detection only |
| **H6** | **leg predicate wider than its frozen sentence** (false red on a compliant landing) | APPENDONLY (r74), SEPARABLE (r73), COMBINED (r76), ROWS (line-diff implemented r74, first red r76) | r73 | 73, 74, 76 | leg text names a *set*; the implementation grades the whole file diff, so a permitted non-set edit turns it red | — |
| **H7** | **leg authority read from the graded tree / surviving mutant** | FROZENCFG, CITEDLINES, LEDGER (r73 r1) | r73 | 73, 74, 75 | counter read config/ledger/tool from the materialized tree; mutant set did not kill the substitution | **QUALITY 25, 26, 28** |
| **H8** | **artifact-vs-leg shape drift**: leg reads a receipt shape the artifact does not have | GROUND, SCRATCHMIRROR, COLLCHECK (r73), EVIDENCE (r76 M4) | r73 | 73, 76 | legs and producers authored against different schemas; only data grading exposed it | **QUALITY 23** (freeze-run) — does not compare against the producer's own schema |
| **H9** | **circular/order-dependent artifact**: a leg or seat grades a report that cannot exist until after the measurement | REPORTCORR, REPORTLAST (r72); ScribeReportCheck (r76 M5) | r72 | 72, 76 | report is written last but graded by the claim receipt / reviewed by a pre-close seat | — (r77 draft carries it as a Mistake candidate only) |
| **H10** | **do-nothing control indistinct or green** | all control runs | r72 | 72, 73, 74 (fixed 75/76) | control run at `lands==base` only (all legs red for one reason), or `lands==freeze` graded PASS | **QUALITY 25(a)/26** — fixed and measured (`controls-c.txt` r75 `FAIL 4/13`, r76 `FAIL 1/13` at `lands==freeze`) |
| **H11** | **freeze/counter revision drift** | STAMP, FROZENCFG | r73 | 73, 74, 76 | several freezes, or a counter edited after freeze without a revision row | **QUALITY 23** (recorded revision) + **26** |
| **H12** | **number-drift in the round's own lesson** (the lesson is an artifact too) | feeds LEDGER pairs later | r74 | 74, 75, 76 (r76 M1) | lesson prose written from drafts/probe receipts | **QUALITY 29** |
| **H13** | **locator / reject-reason attribution**: a finding stated against the wrong artifact | GATE/REJECTS + QUALITY 27 check | r74 | 74, 75, 76 | staged-row vs register-row mispairing; reason cell without artifact+span | **QUALITY 27** (its r75 selector matched none of that round's reject rows) |

Apparatus classes (not counter legs, recorded for completeness):

| id | class | rounds | note |
|---|---|---|---|
| H14 | hardcoded `/tmp` scratch in a counter | r75 (`reports/round-75/accept-ca.py:2175 R74_TMPDIR = "/tmp"`), fixed r76 | r75's counter still carries the literal; r76/r77 RECEIPTS re-run it with `TMPDIR`/`--work` overridden |
| H15 | in-place rewrite of a filed artifact instead of an appended erratum | r76 (closure defect 1: report fix landed as commit `1cd8e33c` editing the filed bytes); r72 errata were correctly append-only | conformance, not a leg |
| H16 | seat writes outside its allowed path (misroot) | r71 (7 fetch files at fleet root), r75 (misrooted wave-1 seat file, R75-M4) | conformance, not a leg |

## 3. Recurrence ranking (how often the class is on record, 72–76)

| class | rounds on record | count |
|---|---|---|
| H2 statement→artifact drift | 72, 73, 74, 75, 76 | 5/5 |
| H1 receipt-absent | 72, 73, 74, 76 | 4/5 |
| H6 predicate wider than text | 73, 74, 76 | 3/5 |
| H7 graded-tree authority / survivor | 73, 74, 75 | 3/5 |
| H10 do-nothing indistinct | 72, 73, 74 (fixed 75/76) | 3/5 |
| H11 revision drift | 73, 74, 76 | 3/5 |
| H12 lesson number-drift | 74, 75, 76 | 3/5 |
| H13 reject attribution | 74, 75, 76 | 3/5 |
| H5 leg-list ≠ table | 73, 76 | 2/5 |
| H8 shape drift | 73, 76 | 2/5 |
| H9 circular artifact | 72, 76 | 2/5 |
| H3 unexecutable command | 76; sibling 75 (declared command drift) | 1/5 red |
| H4 pair reads claim-C path | 76 | 1/5 red |

Reading: the two strongest recurrences (H2, H1) are *authoring* classes, and their landed fixes (29, none) are
the weakest. The two r76 C legs are the weakest *recurrence* classes (H6, one new instance) but the ones the
draft spends its design on. That inversion is the main risk to round 77.

## 4. What is genuinely new in r76 — ROWS over-read and COLLCHECK doc-vs-url

The DRAFT calls both "routed defect r76". Measured, they are new as **failures**, and only one is new as a
**mechanism**. Both distinctions change what a fix must say.

### 4.1 ROWS over-read — new as first-red, not new as a defect

The r76 leg reads the whole-file line multiset:

```
$ grep -n 'every other non-row line added' reports/round-76/accept-c.py reports/round-75/accept-c.py
reports/round-76/accept-c.py:1532:       either side; every other non-row line added, and every non-blank line
reports/round-75/accept-c.py:1297:       either side; every other non-row line added, and every non-blank line
```
The `leg_rows` docstring reading R1 is "A blank line adds no row and hides no row and is tolerated on either
side; every other non-row line added, and every non-blank line removed, fails."

The line-level over-read entered at **r74**, not r73: r73's `leg_rows` grades the parsed row set
(`added = set(lands_rows) - set(base_rows)`, `reports/round-73/accept-c.py:594`) and would tolerate a non-row
added line; r74 replaced it with a line-multiset diff expressly widened for one known non-row change
("exactly the adopted rows added + the one used-by change on a reused row", `reports/round-74/accept-c.py:797`).
r75 repeats the reading verbatim (`reports/round-75/accept-c.py:1282`, same R1 sentence) and r76 freezes it as
"adds exactly the frozen row_set". So the defect was latent two rounds (74, 75) and fired on the first landing
whose shape it did not anticipate — and r74 had already demonstrated the shape of the fix: name the permitted
non-row change in the leg.

What is new at r76 is the *landing shape*: r76 is the first round whose `corpus/SOURCES.md` landing adds
non-row lines.

```
$ for spec in 72:b60c7b1:3adbd4a 73:8841ad3b:c1b5b47 74:f7104cb:5c5c9d3 75:f556d10:f601f7f 76:98c486b:c28ea219; do
    IFS=: read r b l <<<"$spec"
    git diff -U0 "$b" "$l" -- corpus/SOURCES.md | grep -E '^\+[^+]' | sed -e 's/^+//' \
      | awk -v r="r$r" '{ if ($0 ~ /^ *\| *S[0-9]+ *\|/) rows++; else nonrow++ }
                        END { printf "%s rows=%d nonrow=%d\n", r, rows+0, nonrow+0 }'
  done
r72 rows=2 nonrow=0
r73 rows=5 nonrow=0
r74 rows=5 nonrow=0
r75 rows=9 nonrow=0
r76 rows=3 nonrow=2

$ git diff -U0 98c486b c28ea219 -- corpus/SOURCES.md | grep -E '^\+[^+]' | sed -e 's/^+//' \
  | grep -vE '^ *\| *S[0-9]+ *\|' | cut -c1-100
- calendar-standard design — S896 → S895 → S894: start with the state-press account of the ann
**State-standard calendar compilation (round 76).** Question: does one staged calendar amendment sur
```

Root cause (both sides, and both must be fixed): the round applied the `## Paths` / `## Search log` convention
for the first time (`corpus/SOURCES.md:853`, `:890`) while the frozen claim text says only "adds exactly
S894-S896 (817 -> 820)" and its config has **no** `required_sections` or Paths/Search-log key:

```
$ python3 -c "import json;d=json.load(open('reports/round-76/claims.json'));s=json.dumps(d);
print('Paths' in s, 'Search log' in s, 'required_sections' in s)"
False False False
```

So the red is *correct behaviour for the frozen bytes* and a *claim-text omission*. Verdict: **new failure,
recurring defect** (H6, same family as r74 APPENDONLY and r73 SEPARABLE).

### 4.2 COLLCHECK doc-vs-url — new as a data condition, not new as a leg

The leg that failed is not new: the map-URL-vs-row-source-cell comparison with `urls_compatible` exists
verbatim in the r75 counter.

```
$ python3 - <<'EOF'
import re
def blk(p):
    s=open(p,encoding='utf-8').read()
    return re.search(r'def urls_compatible\(a, b\):.*?\n\n\n', s, re.S).group(0)
print(blk('reports/round-75/accept-c.py')==blk('reports/round-76/accept-c.py'))
EOF
True
```

And the rule is a host+path fold, not a document-identity fold:

```
$ python3 - <<'EOF'
import re
from urllib.parse import urlparse, parse_qs
src=open('reports/round-76/accept-c.py',encoding='utf-8').read()
ns={'urlparse':urlparse,'parse_qs':parse_qs}
for name in ('def norm_url(u):','def _norm_path(u):','def urls_compatible(a, b):'):
    exec(re.search(re.escape(name)+r'.*?\n\n\n', src, re.S).group(0), ns)
show='https://openstd.samr.gov.cn/bzgk/std/showGb?type=online&hcno=E107EA4DE9725EDF819F33C60A44B296'
new='https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=E107EA4DE9725EDF819F33C60A44B296'
print('urls_compatible(showGb, newGbInfo) =', ns['urls_compatible'](show,new))
print('norm_url(show) =', ns['norm_url'](show))
print('norm_url(new)  =', ns['norm_url'](new))
EOF
urls_compatible(showGb, newGbInfo) = False
norm_url(show) = ('openstd.samr.gov.cn', '/bzgk/std/showGb')
norm_url(new)  = ('openstd.samr.gov.cn', '/bzgk/std/newGbInfo')
```

The failure text (`reports/round-76/telemetry/measures-c-final-c28ea.txt:38`):

```
LEG FAIL COLLCHECK
     map record S938 -> S895 names a document the row does not: https://openstd.samr.gov.cn/bzgk/std/showGb?type=online&hcno; ids=817 staged=132 collisions=35 guard=ok/ok map=7
```

The frozen config already says these are one document — `row_set[1].document` reads "… newGbInfo?hcno=… ;
showGb is a 302 alias to this record" — and the map's own join-key note declares "normalized document URL
(round-75 norm_url)". Neither key can represent the alias. Verdict: **new data condition** (first landing on record where a map record carries an alias route and the
row carries the target; no earlier COLLCHECK red at a landing — measured), **not new leg behaviour**, and the DRAFT's
stated fix ("compares document identity (normalized document URL per staged→lane map), not raw URL strings")
describes what r76 already did and would still print red on the same pair.

Also material: the counter's selftest cannot see this class.

```
$ grep -ci alias reports/round-76/telemetry/selftest-c.txt
0
```

The seven `coll_*` mutants (`coll_adopted_in_regids`, `coll_adopted_in_collisions`, `coll_fourspace_found`,
`coll_plant_real_id`, `coll_tab_plant`, `coll_lowercase_plant`, `coll_staged_missing`) all exercise id/indent
collisions, none the URL-identity rule that actually failed.

## 5. DRAFT attack — does r77 repeat a class whose fix is already landed?

Coverage of the history classes by QUALITY criteria 23–29, and by the DRAFT's own mitigations. `covered` =
the landed criterion mechanically binds the class; `partial` = binds one limb; `—` = no landed criterion.

| class | criterion 23–29 | DRAFT mitigation (verbatim intent) | verdict |
|---|---|---|---|
| H1 receipt-absent | 23 (selftest receipt), 25(b) (junk/controls receipts); **not** claim-declared fixtures | "Receipts committed: every telemetry file a pair cites exists at the freeze" | **partial** — r76's failure was read *at Ca-lands* and the files existed at no revision; the check must also bind `R1EXEMPT`'s green/red fixtures (r76's exact miss) |
| H2 statement→artifact drift | 29 (numbers), 26/23 (fix ships red-before) | "`stated_text` is verified present at `stated_at` in the BASE tree at ledger build" | **partial** — no rule for `statement_after`; and the lookup must be line-scoped like the frozen leg (L76-19's sentence wraps lines 47–48 of `corpus/lessons/round-75.md`) |
| H3 unexecutable command | 8/9 only | "rederive strings must be argv-executable … no `grep -E` pattern operand holds a backtick or escaped pipe" | **partial** — `rederive` stays a hand-typed string; no rule that it equals `shlex.join(observe_cmd)`, no rule for 40-hex revision operands. L76-19/20/21 would still fail as worded |
| H4 pair reads claim-C path | 7 | `stated_at` allowlist (LOG, SCORECARD, lessons 75/76; README REPAIR-only) | **covered** |
| H5 leg list ≠ table | 26, 25(c) | "generated from the counter's own leg table at freeze; no hand-typed duplicates" | **contradicted by the draft itself** — the draft then prints a hand-typed list: `FROZENCFG, STAMP, LEDGELIST?, COUNTS, ENTRIES, ROWS, APPENDONLY, COLLCHECK, INDEX, EVIDENCE, GATE, REJECTS, CENSUS, GROUND, RECEIPTS` (literal `?`, C and Ca names mixed, `REPOINTED`/`CITEDLINES` gone) |
| H6 predicate wider than text | — | ROWS counts only `| S### |` lines in the row_set; required non-row edits in `required_sections[]` "checked by INDEX" | **partial + new hole** — in r76, `INDEX` reads `corpus/README.md` only; its own receipt detail is `corpus/README.md: 6 section(s), culture-material=41, …`. Nothing in the draft adds a SOURCES-reading limb, so the Paths/Search-log lines become **ungraded** instead of over-graded |
| H6 (COMBINED limb) | — | "Combined README exemption carries its required line number" | **repeats r74→r76** — a hand-typed pin; r76's `owned_inplace` already carried `base_text`/`after_text` and still failed. Derive the exemption from the frozen sibling claim's diff instead |
| H7 graded-tree authority | 25, 26, 28 | FROZENCFG only | **covered if CITEDLINES is retained with its pin**; the draft's leg list drops `CITEDLINES` (r76 printed `files=1 last-line=CITED-LINES: 0 finding(s) in 1 file(s)`) |
| H8 shape drift | 23 | not mentioned | **uncovered** — r76 M4 (three evidence files passing EVIDENCE without the producer's 17 anchor-binding headers) is a leg-vs-producer schema gap; a freeze run does not compare to the producer |
| H9 circular artifact | — | named only as a `## Mistakes` candidate | **uncovered mechanically** — r77's own Ca claim again depends on the C-lands commit (`--combined`), which is fine for measurement but any seat asked to review a pre-WAVE-DONE report repeats r76 M5 |
| H10 do-nothing | 25(a), 26 | "lands == freeze fails on data legs; lands == base refused exit 2" | **covered** |
| H11 revision drift | 23, 26 | not mentioned | acceptable — disclosure discipline held in r76 (F0–F5) |
| H12 lesson number-drift | 29 | `## Mistakes` candidate | **covered if** every Gate/Mistakes number is re-derived; 29 binds |
| H13 reject attribution | 27 (selector inert at r75) | REJECTS leg; Gate rejects with "reason + flip" | **partial** — a Gate reject row must name a repo-relative capture and the span with `absent`/`present` (criterion 27); the draft's reject bullets say "reason + flip" only |

### Findings for the L1 (ordered by recurrence weight, not by round-77 leg count)

**F1 (H2, 5/5 rounds).** No draft rule validates `statement_after` before freeze. r76's only REPAIR pair failed
on exactly that limb:

```
LEG FAIL REPAIR — L76-16 `statement_after` no-match in SKILL.md.
```
```
$ python3 …difflib on SKILL.md:707 base vs a43ed807
replace | base: ' at counter' | new: ': committed counter `reports/round-75/accept-c.py`'
insert  | new: " `315c5f3f27fd…`; the receipt header's"
```
The ledger's regex expects `committed counter sha256 \`([0-9a-f]{12})\``; the repaired row never says `sha256`.
Add: at ledger build, `statement_after.parse` must match the post-repair text **as it will be written**, and the
ledger must carry the byte-identical repair sentence.

**F2 (H1, 4/5).** Commit every declared fixture in the freeze commit and read it at Ca-lands. r76's
`R1EXEMPT` fixtures were absent everywhere:

```
$ for rev in df0f0309 a43ed807 c28ea219; do git cat-file -e $rev:reports/round-76/telemetry/r1exempt-green.txt …; done
df0f0309: absent
a43ed807: absent
c28ea219: absent
```
The draft's wording ("exists at the freeze") is right but must also name the lands-side read, because that is
where r76 failed.

**F3 (H3).** Make `rederive` the *same* command as `observe_cmd`: require
`rederive == shlex.join(observe_cmd_for_the_lands_read)`, or store it as an argv array. Then add two selftest
scenarios that the r76 set lacks: a 40-hex revision as a `git grep` operand, and a pattern containing a space.
The frozen r76 validator already accepts 40-hex revisions (`_git_grep_problem` matches `[0-9a-f]{40}`), so the
failure is purely the hand-typed string form.

**F4 (H6, ROWS).** Keep the ROWS narrowing, but give the non-row edits a grader that actually reads
`corpus/SOURCES.md`. "Checked by INDEX" is not true of the r76 INDEX leg (README-only). Otherwise r77 swaps a
false red for a false green on the two Paths/Search-log lines.

**F5 (H6, COLLCHECK).** The draft's identity fix is already the implemented rule. Choose one:
(a) the map records the document's carrier set (target + alias) and the leg accepts any member; or
(b) `urls_compatible` folds the shared registry identifier (`hcno`) — note the map's own `join_key` doc says
"normalized document URL (round-75 norm_url)", so (b) also needs a map-doc correction.
Either way add a red-before mutant carrying exactly the r76 alias pair; today `grep -ci alias
reports/round-76/telemetry/selftest-c.txt` = 0, so the leg cannot show the rule both ways.

**F6 (H5).** Resolve `LEDGELIST?` and publish one leg list per claim, generated from that claim's counter table
(the DRAFT's own sentence demands it and then violates it). Reconcile the dropped `REPOINTED`, `CITEDLINES`
and `SCRATCHMIRROR` names against r76's frozen set: r76's list already carried `INDEX` twice and omitted
`SCRATCHMIRROR` (`# frozen legs: 13 (ENTRIES,ROWS,REPOINTED,GATE,EVIDENCE,REJECTS,GROUND,CITEDLINES,CENSUS,INDEX,COLLCHECK,FROZENCFG,INDEX)`),
which is R76-M2 verbatim. Criteria 26/25(c) will *refuse* the freeze if this repeats — a cheap blocker to
avoid.

**F7 (H8).** Run both counters at the freeze against the round's *real* evidence and ledger shapes, not empty
placeholders (criterion 23 already says this; r76 M4 shows a leg can pass files the producer would reject).
State explicitly which producer headers the EVIDENCE leg requires.

**F8 (H13).** If r77 files any Gate reject row, run the criterion-27 one-liner over the drafted lesson *before*
the freeze and require it to print at least one `OK` line. In r75 the same selector matched none of that
round's reject rows, i.e. the criterion was inert in the round that added it.

## 6. Direct answers

1. **Every counter failure class 72–76**: H1–H13 above, each with leg, round and root cause; H14–H16 are
   apparatus classes outside the legs.
2. **Which recur**: H2 (5/5) and H1 (4/5) dominate; H6, H7, H10, H11, H12, H13 at 3/5; H5, H8, H9 at 2/5.
3. **Genuinely new in r76**: ROWS over-read is a **new failure of a defect latent since r74** (r73's leg grades
   the parsed row set; r74 introduced the line-multiset predicate, r75 repeated it; rounds 72–75 added zero
   non-row SOURCES lines — measured). COLLCHECK doc-vs-url
   is a **new data condition of a leg unchanged since r75** (`urls_compatible` byte-identical; returns `False`
   on the r76 alias pair — measured), not a new mechanism. Neither is a new class of counter defect.
4. **Does r77 repeat a landed-fix class?** Yes, in four places: H5 (the draft's own `LEDGELIST?` hand-typed
   list), H1 (freeze-only receipt wording), H6-COMBINED (hand-typed line number), and H3 (`rederive` as a
   string). H2's `statement_after` half and H8's producer-schema half have no landed fix and no draft rule.

## 7. Confidence and limits

- **High**: the leg/round/root-cause rows for r72–r76 (measured verdict lines and frozen leg text quoted
  above); the SOURCES non-row measurement; `urls_compatible` behavior; the r1exempt absence; the leg-list
  duplication (printed by the r76 counter itself).
- **Medium**: polarity calls where the leg is defensible and the claim text or the map is also at fault —
  ROWS (the W2 critics disagreed exactly there: `CritRowDiff` vs `ConnCounterPatterns`) and COLLCHECK (the map
  recorded the alias while the row recorded the target; either side alone would have been green). I record both
  as both-sides-dirty, not as pure counter bugs.
- **Inference, marked**: that r77's `required_sections[]` will be graded by a *new* INDEX limb rather than the
  r76 README-only `leg_index` [INFERENCE from the r76 leg's file scope; the draft does not say].
- **Unrun**: no counter was run to a verdict (two pure helpers, `norm_url` and `urls_compatible`, were executed
  in isolation from the r76 counter source — quoted in §4.2); no online source was opened; no fixture repo was
  created; this seat's evidence is the lane record. Criterion 27's one-liner was not re-run over r77 drafts (no
  draft Gate exists yet) — reported as unrun.
- **Negative claims**: the r76 selftest alias absence is a sweep (`grep -ci alias reports/round-76/telemetry/selftest-c.txt`
  → `0`), not the absence of a differently named mutant; the r73 "no landing receipt" claim rests on the
  telemetry listing (`ls reports/round-73/telemetry` shows `controls-c.txt`, `selftest*.txt` and no
  `measures-c.txt`) plus the r74 spot-check's own re-run (`accept-c-73-at-lands.txt` pairs) — r72, r74, r75
  and r76 do each have a committed landing receipt.
