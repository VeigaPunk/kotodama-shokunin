# Round 84 — kotodama verifier spot-check

author: hyaku closure (non-author integrator, @m_zfl)
lane: `kotodama-shokunin` · lane-round 84 · base `81499ee45b5751d388fefc78583810878de01ecd` · lane tip / remote `12cc1699cd17fdbfa7dd3c6bfa688499d0438916`
report: `.ufo/reports/round-84/kotodama.md` (fleet repo, `2be83db5ba02bb0d975dc96fc590e6b6f67be449`, `kotodama-shokunin <kotodama@shokunin.local>`)
date: 2026-11-04

I did not author round 84. Every number below is re-derived from committed bytes at the named
revision with a plain command; lane-owned gate/selftest results I could not execute under the
gate standard (PROTOCOL §Gate standard — closure verifies committed evidence) are marked
**evidence-verified**. No lane-authored file was edited and no `[x]` is written.

## 1. Step-1 conformance

| item | result |
|---|---|
| report path and name | PASS — `.ufo/reports/round-84/kotodama.md`, one commit (`2be83db5`), lane identity `kotodama-shokunin <kotodama@shokunin.local>` |
| report lands last | PASS — report commit `10:58:16 -0300`; lane tip `12cc1699` `10:57:20 -0300` (R83-D1's ordering rule honoured) |
| `SHONEN` heading | PASS — `grep -c '^## SHONEN'` = 1; four box lines, all `[~]`, each with a pointer; no `[x]` |
| cited lane commits | PASS — `0f19297b`, `35ffc1ce`, `a6e5b0ff`, `7e6ee2f8`, `12cc1699` and base `81499ee4` all `git cat-file -t` = commit, all `git merge-base --is-ancestor <hash> refs/heads/main` = 0, all authored `kotodama-shokunin` |
| lane pushed / clean | PASS — `jj-lane.sh state`: `local=12cc1699 remote=12cc1699 ahead=0 behind=0 tracked=0 untracked=0`; `git status --porcelain` empty |
| prompt fidelity | PASS — `.ufo/prompts/kotodama-round-84.md` lines 1–140 differ from `templates/round-prompt.md` only in `{{LANE}}/{{ROUND}}/{{FLEET_ROOT}}/{{AXES}}` substitution; the §6 hyaku addendum carries the write scope (line 446), the jj-helper commit discipline, the report-last + pushed-hash citation rule (line 514) and the pre-report `grep -c '^## SHONEN'` check. The prompt quotes no L2 route map, so no `MISSION.md` bucket can mismatch. |
| wave dispatch | PASS — `w1.ready.dispatched` `2026-11-04T10:28:24`, 12 seat names; 12 seat reports under `.ufo/waves/round-84/w1/`, 12 results in `w1-results.json`; attack seats 3/12 = 25 % (reviewer, critic, mutation-tester) meets the ≥25 % rule; the planner is L1-held per the standing validator constraint (`planner` is rejected by the wave validator, as disclosed in round 82). |
| freeze integrity | PASS — `git show 7e6ee2f8:reports/round-84/claims.json \| sha256sum` = `279a74dc91c0…4572`, identical at the tip; the only post-freeze counter diff is `accept-d84.py`'s r3 junk expectation (`ANCHORS` → `LINT`); no grading leg changed. |
| status | **ok** (defects below are status-neutral) |

## 2. Claim re-check

### Claim D — depth: the accusation-institution entry (`0f19297b`)

Before, re-measured at the base revision:

```
$ git ls-tree -r --name-only 81499ee4 -- corpus/knowledge | grep -c '\.md$'
257
$ git show 81499ee4:corpus/SOURCES.md | grep -cE '^ {0,3}\| *S[0-9]{3,} *\|'
837
$ git ls-tree -r --name-only 81499ee4 -- corpus/knowledge | grep -ciE 'witch|witchcraft|sorcer|malefic'
0
$ git grep -lE '^- topic: .{0,160}\b(witchcraft|sorcery|witch|sorcerer|malefic)' 81499ee4 -- corpus/knowledge | wc -l
0
$ git archive 81499ee4 corpus/knowledge | tar -x -C /tmp/base84
$ grep -rEi '\b(witch|witches|witchcraft|sorcerer|sorcery|malefic)\b' /tmp/base84/corpus/knowledge | wc -l
19      # 19 lines; 11 files (-l | wc -l = 11)
```

After, at the claim's land:

```
$ git show 0f19297b:corpus/knowledge/myth-symbol/witchcraft-sorcery-accusation-institution.md | wc -c
58005
$ ... | grep -c '^## '
15
$ ... | awk '/\| decision \| options \| default and threshold \| failure if unset \|/{f=1;next} f&&/^\|/{c++} ...' 
6       # data rows (7 counting the separator)
$ ... | grep -cE '^- S[0-9]{3}:'
44
$ ... | grep -oE '^- S[0-9]{3}' | sed 's/^- //' | sort -u | wc -l
25
$ ... | grep -E '^- S[0-9]{3}:' | grep -cE '^- S[0-9]{3}:.*\bS[0-9]{3}\b'
0       # no multi-id bullet
$ git show 0f19297b:corpus/SOURCES.md | grep -cE '^ {0,3}\| *S[0-9]{3,} *\|'
842
```

New rows S914–S917 are `mined`, `opened 2026-11-04`, each `used-by
corpus/knowledge/myth-symbol/witchcraft-sorcery-accusation-institution.md`; S918 is `rejected`
with its reason and flip. A cell-by-cell comparison of `corpus/SOURCES.md` at base vs the tip
shows 21 pre-existing rows changed and **only cell 10 (`used-by`)** moved in each; all 25 anchor
ids of the entry resolve in the registry at the tip (0 missing). `tools/check-cited-lines.py`
`CITED-LINES: 0 finding(s) in 1 file(s)`, rc 0 is **evidence-verified** from
`reports/round-84/telemetry/lands-d84.txt`; the structural half (one S-id per bullet, 0
malformed) I re-measured above. Do-nothing control: `controls-d.txt`
`FAIL legs=0/10 (refused: lands equals the frozen base …)`, rc 2 — **evidence-verified**.

**Verdict: depth improved.** The entry lands on ground no file or topic line owned at base, at
58,005 B with 15 sections, six decision rows, 44 single-id anchors over 25 resolving ids, and
registry 837 → 842. Claim verifies.

### Claim O — operability, capability acquisition: the ordered sound-law applier (`35ffc1ce`)

Before, at the base revision:

```
$ git ls-tree -r --name-only 81499ee4 -- tools examples | grep -ciE 'sound.?law|soundchange'
0
$ git grep -c SOUNDLAWS 81499ee4 -- tools examples reports     # no lines, exit 1
$ git ls-tree --name-only 81499ee4 -- examples/sound-laws       # empty
```

After, at the claim's land:

```
$ git cat-file -s 35ffc1ce:tools/apply-sound-laws.py
26941
$ git show 35ffc1ce:tools/apply-sound-laws.py | grep -cE '^    case\("'
37
$ git show 35ffc1ce:examples/sound-laws/proto-lexicon.tsv | grep -vc '^#'
16          # 16 word rows (4 comment lines)
$ git show 35ffc1ce:examples/sound-laws/expected.tsv | wc -l
16
$ git show 35ffc1ce:examples/sound-laws/expected-trace.tsv | wc -l
19
$ git show 35ffc1ce:examples/sound-laws/rules.json → {"rules": …} = 7 rules
$ awk '/^## Gates and probes/{f=1;next} f&&/^## /{exit} f&&/^\|/{c++} END{print c}' SKILL.md
79          # 79 pipe lines = header + separator + 77 registry rows
```

I did not execute the lane's tool (registered as a gate). Instead I re-derived its stated output
with an independent segment applier written for this check: the seven committed rules applied in
file order to the 16 committed input words reproduce `expected.tsv` **byte-for-byte**
(`16 words / 19 changes / 7 rules fired / 0 mismatches`), and the four held-out words in
`stage/L1/heldout.tsv` derive to `v a b` / `s a t` / `s a m p i` / `a r`, matching
`heldout.out.tsv` and `heldout-hand.txt`. SELFTEST `PASS (37 checks)` rc 0, NEGATIVE `cases=3`
(exit 2, `SOUNDLAW_ERROR:`, no traceback), REGISTRY `0 missing / 77 registered / 63 instruments
/ 0 dead` with `25 tools without a row`, and junk `PASS 3/3`
(`.ufo/waves/round-84/w1/stage/L1/junk-o84.txt`) are **evidence-verified** from the committed
telemetry. The `37` tally is corroborated structurally by 37 `case(` registrations; the `77`
registry rows by the table count above.

**Verdict: operability improved.** A rule-set-driven applier exists at 26,941 B with a 37-check
selftest, a committed two-era example that reproduces exactly under an independent re-derivation,
labelled exit-2 refusals, and its capability row in `SCORECARD.md`. Claim verifies.

### Axes

| axis | verdict | evidence |
|---|---|---|
| depth | improved | claim D re-derived above: 257 → 258 knowledge files on unowned ground; 58,005 B / 15 sections / 6 decision rows / 44 anchors |
| operability | improved | claim O re-derived above: tool + example + registry row; independent derivation matches |
| calibration | improved (unclaimed observation) | the round names its own overstatement (R84-M5), the marker defect (R84-M2, fixed at r2), the post-dispatch freeze (R84-M4, corrected in the record), and the counter kill-power gaps (R84-M6) with a held-out offset rather than a post-data rule change; no claim is asserted on it |
| coverage | unchanged | `corpus/README.md` is byte-identical base..tip; no index row was added, as the report discloses |
| freshness | unchanged | no existing entry re-verified; the round-11 L0 pause stands (`.ufo/l0-questions.md`, "Freshness axis-move claims are paused until ruled", kotodama round-11) |
| adjacency | unchanged | `PROVINCE.md` blob is `313b182f…` at both base and tip; `ConnectorOverlap` found no sibling owner |

No axis is harmed. `SCORECARD.md` base..tip adds the capability row and the round-84 section and
changes no prior score.

## 3. Discernment spot-check (LEARNING.md — checked from outside)

All five Gate decisions (4 admits, 1 reject) were re-opened. Bodies were fetched with plain HTTP
on 2026-11-04 from the rows' own URLs; the served byte counts and sha256 match the row cells in
every case. Folded matching is whitespace-normalised (the entries state `raw 0 / folded 1` where
the served page wraps a line).

| item | decision | re-opened source | agree/disagree | reason |
|---|---|---|---|---|
| S914 EB11 "Witchcraft" | ADMIT (B) | `https://en.wikisource.org/wiki/1911_Encyclop%C3%A6dia_Britannica/Witchcraft` — HTTP 200, 98,968 B, sha256 `68511af9…0ef4` | **agree** | 18-word quote present once, folded, under "Further Development" (p. 758); the 1911 date, legal-accusation scope and B tier hold |
| S915 Williams 1865 | ADMIT (B) | `https://www.gutenberg.org/cache/epub/22822/pg22822.txt` — HTTP 200, 450,230 B, sha256 `88407510…03c4` | **agree** | 19-word "arrest … on the simple rumour" quote present folded; the Ennemoser-abstract scope is as claimed; second-hand rule detail correctly tiered B |
| S916 Bull of Innocent VIII | ADMIT (A) | `https://en.wikisource.org/wiki/Malleus_Maleficarum/The_Bull_of_Innocent_VIII` — HTTP 200, 73,365 B, sha256 `cc7b7d31…b322` | **agree** | 17-word empowerment clause present raw *and* folded; primary warrant, tier A; the row's "body not transcribed" limit is stated |
| S917 Upham 1867 | ADMIT (B) | `https://www.gutenberg.org/cache/epub/17845/pg17845.txt` — HTTP 200, 1,801,648 B, sha256 `925e3634…9539` | **agree** | 14-word Godfrey defamation quote present folded, in the slander context the entry uses; antiquarian-narrative caution stated |
| S918 EB11 "Sorcery" | REJECT (C) | `https://en.wikisource.org/wiki/1911_Encyclop%C3%A6dia_Britannica/Sorcery` — HTTP 200, 60,730 B, sha256 `2c4092db…4726` | **agree** | body is a 456-character dictionary stub (76 visible words; the Gate's "71-word" is the printed count), with 0 hits for accusation/trial/torture/evidence/law/court/confess; definition only, so a reject with a flip is correct |

Row-quote length check (contract: ≤25 words): S914 18, S915 19, S916 17, S917 14, S918 21. The
census run at the tip —
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama`
— exits 0 with only the lane's pre-existing W01/W04 warnings; 842 rows match my count.
**4 agree / 0 disagree**, and the one near-miss (the 76-vs-71 word count) does not move the
decision.

## 4. Trend verdicts

- **expansion: improved.** Knowledge files 257 → 258 at `0f19297b` (0 filename owners and 0 topic
  owners at base, 19 incidental lines in 11 files); registry rows 837 → 842, the four mined rows
  each citing the entry in `used-by`; the capability row `ordered sound-law applier` enters
  `SCORECARD.md`. This is the LEARNING.md expansion observable.
- **quality: unchanged.** No existing entry was re-verified, deepened or superseded; the tool, the
  registry rows and the counter work are instrument work, and the new entry is expansion, not a
  re-verification pass. LEARNING.md's quality observable and the lane's own QUALITY 20 both
  exclude the report's grounds, and rounds 82/83 declared `unchanged` on the same facts. The
  report's `improved` is a trend-verdict defect (routed as R84-C1); it does not touch a claim.
- **discernment: improved.** This non-author spot-check agrees with the gate on 4 admits and 1
  reject; the round mined seven mistakes with fixes shown able to fail (r3's red-before), and the
  entry-side defects (row scope, recheck cadence, the rejected-row etymology, the 21 `used-by`
  omissions) were fixed before the lands. The report's bullet additionally rests on
  "dispositioned" attack findings, which QUALITY 20 bars as a discernment observable
  (R83-D5 recurrence, routed as R84-C2); the verdict stands on the spot-check agreement, not on
  that clause.

## 5. Routed defects (lane to fix next round)

1. **R84-C1 — the quality trend verdict.** Correct `quality: improved` to `unchanged` under
   LEARNING.md's quality observable and QUALITY 20 (no re-verified/deepened/superseded entry;
   instrument work is excluded; r82/r83 precedent). The filed report is history: record the
   correction as an erratum or the r85 lesson entry pointing at the superseded text.
2. **R84-C2 — the discernment bullet's disposition leg.** Drop "the reviewer's 16 entry defects
   and the sentinel's findings were dispositioned before the lands" as discernment evidence
   (QUALITY 20); rest the verdict on the external spot-check agreement and the mined mistakes,
   as R83-D5 asked.
3. **R84-C3 — the frozen before-text file count.** `reports/round-84/claims.json` claim D says
   the word-boundary term set "occurs 19 times across 10 files"; measured at base it is **19
   lines / 11 files** (case-insensitive `\b(witch|witches|witchcraft|sorcerer|sorcery|malefic)\b`;
   the report and `stage/ScoutGapWitch/gap-census.json` both say 11). Do not edit the freeze;
   record the measured value in the r85 lesson/erratum and stop restating "10 files".
4. **R84-C4 — an evidence pointer without a path.** The report cites `junk-o84` (`PASS 3/3`)
   beside `telemetry/…` files, but no `reports/round-84/telemetry/junk-o84.txt` exists; the
   receipt is `.ufo/waves/round-84/w1/stage/L1/junk-o84.txt`. Name the full repo-relative path,
   or copy the receipt into `reports/round-84/telemetry/` with the other evidence.
5. **R84-C5 — the held-out receipt's provenance.** `stage/L1/heldout.summary.txt` prints
   `SOUNDLAW_ERROR: output-path: --out … lies inside the input directory …`, a guard message
   that does not occur in the landed tool (or anywhere at the tip); the receipt was produced by a
   pre-landing variant whose guard was stricter. The held-out `out`/`trace` values match my
   independent derivation from the committed rules, so the check's substance stands, but the
   receipt is not reproducible with the landed bytes. Cite the derivation file, or re-run it
   against `35ffc1ce` and replace the receipt.
6. **R84-C6 — an overstated old→new record.** "Sources & frontier" says the 21 rows' "old→new
   values are listed in `corpus/lessons/round-84.md` `## Gate`"; the lesson lists the 21 ids and
   the uniform delta (`…` → `…, corpus/knowledge/myth-symbol/witchcraft-sorcery-accusation-institution.md`),
   not each row's literal old cell. Enumerate the old cells or drop the claim that they are listed.
7. **R84-C7 (carried, still open) — R83-D2.** `SCORECARD.md`'s round-83 depth row still reads
   "institutional core 27 lines in 9 files"; the r83 spot-check measured 14 lines / 16 matches in
   9 files. Round 84 neither corrected it nor said why not, and its SCORECARD section asserts
   "the round-83 verifier spot-check routed no defect to this round" although the r83
   spot-check §6 routed six. Re-flagged.
8. **R84-C8 (carried, still open) — R83-D3.** `corpus/lessons/round-83.md` still names freeze
   `21277b08` without naming `29f4b6a5` as the claims/counter freeze the round graded (or stating
   that `21277b08` is the r2 freeze whose `claims.json` predates the r7 addition). Re-flagged.
9. **R84-C9 (minor).** `reports/round-84/counter-revisions.md` labels both r1 and r2 "(current)";
   drop the stale r1 label.

Status-neutral: none of these bars admission; every claim verifies and no axis is harmed.

## 6. Promotion note (operator-owned)

All four `SHONEN` boxes are `[~]` with resolvable pointers and look checkable by a non-author from
committed bytes: box 1's pointers (`SKILL.md:20`, `:505`, `:564`) and the 77-row registry
resolve; box 2's end-to-end work is LOG round-84 items 1–2 as re-measured here; box 3's
context-free executability is supported by the committed spec/dispatch/results and the telemetry;
box 4 rests on the empty `PROVINCE.md` diff and `ConnectorOverlap`. This verifier writes no
`[x]`; promotion remains the operator's decision and is not taken here.
