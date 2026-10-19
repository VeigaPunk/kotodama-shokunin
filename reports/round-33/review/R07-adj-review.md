- Seat: R07 | reviewer | claim A | date 2026-10-19 | baseline 139e3b6

# R07 — adversarial review of the adjacency (A) leg

**Assignment** (`reports/round-33/targets.json` R07): "Adversarial review of adj/
fragments: re-run cited commands, check the audit verdict table completeness, hunt
unfiled bleed." Out path: `review/R07-adj-review.md` (this file, my only write).

**Tree under review:** HEAD `139e3b662900557afe54f632b468619593dc9fcb` ==
`reports/round-33/claims.json:8`. All my commands were read-only at the lane root,
`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, 2026-10-19T03:52–03:58Z.
Two transient capture files (`/tmp/r07-a.txt`, `/tmp/r07-b.json`) were created for
exit-code capture and **removed** in the same session; no other write outside this
file. No git-mutating command, no install, no network. No promotion/canon/clearance/
closure verdict is made here; canon: NON-CANON engineering evidence.

**Fragments present at my reads** (the wave was in flight; the rest of A01–A16 was
unfiled): `adj/A01-province.md`, `adj/A10-receipt.md`, `adj/A13-verify-a07-a09.md`,
`adj/A15-audit-draft.md`, `adj/A16-shonen-material.md`, `adj/K04-method-scout.md`.
Because A02–A09 were absent, this review executes their check classes itself (below)
rather than certifying fragments that do not exist — per `targets.json:10`.

## 1. Independent re-runs (my execution, not a restatement)

Every row is a command I ran at the tree above; "matches" names the fragment claim it
reproduces or contradicts.

| # | command | observed | matches |
|---|---|---|---|
| 1 | `python3 -B tools/gates/handoff-packet-check.py examples/handoff-packet.sample.md` | exit 0, `fields=16/16 glossary-entries=20 findings=0` | A10 A02 row; A15 §2.2 |
| 2 | same, `examples/handoff-packet.sample.yml` | exit 0, `fields=16/16 glossary-entries=0 findings=0` | new datum — see R07-F3 |
| 3 | same, `reports/round-20/handoff/packet.md` | exit 0, `16/16`, `20`, `0` | r21 filed row `reports/round-21/adjacency/A11-A12-handoff.md:43`; A15 §2.2 |
| 4 | same, `reports/round-20/handoff/packet-v3-16.md` | exit 0, `16/16`, `20`, `0` | extra control (no fragment cites it) |
| 5 | same, `reports/round-30/handoff/declared-in-r6/packet.md` | exit 0, `16/16`, `20`, `0` | A15 §2.2 ("current packet pair") |
| 6 | same, `--selftest` | exit 0, `fixture findings 11 across 9 ids …; clean control exit 0` | A10 A02 row; A15 §2.2 |
| 7 | `python3 tools/check-gate-battery.py --selftest` | exit 0, `SELFTEST OK 44/44 controls behaved as expected` | A10 A09 row; `op/O07-baseline-receipt.md` |
| 8 | `python3 tools/check-gate-battery.py` (battery) | exit 0; `pass 7 fail 0 unevaluable 0`; coverage `10/10`, `pinned 20`; originals `files_hashed 33/33, modified 0, added 0, deleted 0, preserved true` | O07 "battery 10/10" leg, exactly |
| 9 | `python3 tools/check-craft-exercise.py --selftest` | exit 0, `SELFTEST OK 10/10 tamper cases detected` + `CLI-SELFTEST OK 18/18` | O07 leg 2 |
| 10 | `python3 tools/assemble-culture-d4.py --selftest` | exit 0, `81/81 checks passed` | O07 leg 3 |
| 11 | `python3 tools/check-evidence-coupling.py --selftest` | exit 0, `"selftest_passed": true` | O07 supplemental leg |
| 12 | `python3 -B reports/round-25/audit/c31-lessons-index-audit.py` | **exit 1**; `lesson files 33`, `index rows 26`, `FAIL C31_index_rows_eq_files`, `FAIL C34b_prose_arithmetic`, findings `C31-1` (7 files round-26..32), `C34-2 {stated [26,26], measured [26,33]}` | claim-O before-state; **contradicts A10-F3** — see R07-F1 |
| 13 | same, `--json` | **exit 0**, same two findings inside the JSON receipt | the nuance A10-F3 conflated |
| 14 | same, `--selftest` | exit 0, `SELFTEST OK: 28/28 checks passed` | O07 leg 4; A10 |
| 15 | `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | exit 0, `summary: 20/20 legs passed` | A10-F1 (r21 filed `19/19` at `A11-A12-handoff.md:46`) |
| 16 | `python3 tools/exercise-handoff-e2e.py --profile v3` | exit 0, `fields=16/16 glossary=20/20 findings=0 links=105/105 claims=27 statuses=16/7/4`, packet `sha256 6ced88ad009f1cfc94f7fc9e5656555f7da6682ce8f7afc3eb16734272f0f0bb`, `preservation: 58 read-set files byte-identical` | A10 A07 row (1); r21 filed values |
| 17 | `git diff --quiet -- PROVINCE.md`; `sha256sum PROVINCE.md`; `git rev-parse HEAD:PROVINCE.md` | exit 0; `05b34a579c5d4f4ec78957cdedb658246ff292df3e21181c66186403f2b942d6`; blob `313b182f251564b7997b06996b4f063370778f11` | A01; A10 A01/A07 rows; A13 rows 2–3; r21/r29 filed pins |
| 18 | `sha256sum SKILL.md corpus/lessons/README.md AGENTS.md` | `79fe91d3…`, `ec7469da…`, `1afaf106…` | A16; A10 A09; A10-F2 (r29 filed `be3a9477…`) |
| 19 | `git ls-files \| wc -l`; `-- reports/`; `-- tools/gates/frozen/` | `2655`; `1857`; `237` | `claims.json:57`; A15 §2.3 exactly |
| 20 | `git ls-files 'reports/round-*'` (8–32) + round-tagged frozen (8–32) | `1770` + `135` = **1905** | A15 §2.3 decomposition, exact |
| 21 | per-partition `find corpus/knowledge/*/ -type f \| wc -l` | 94 / 18 / 21 / 19 / 29 / 20 = **201** | A10 A05 total (the tool run itself not repeated by me) |
| 22 | `stat -c '%s %y' .ufo/reports/round-32/kotodama.md`; `ls .ufo/reports/` | `7541` bytes, `2026-10-18 22:01:59 -0300`; no round-33 dir | A01 A01-4; A10 A03 row |
| 23 | `grep -n -i kotodama /home/vgpnk/Projects/shokunin/.ufo/l0-questions.md`; `stat -c '%y'` | lines `44–47` (rounds 2/8/9/11); mtime `2026-10-18 17:14:10 -0300` (pre-declaration) | A01 A01-4; A10 A04; A15 §2.4 |

Not independently re-run by me (single-execution claims; integrator should treat them
as one-seat evidence, not two): the r21 inventory one-liner, the r29 ledger-census
assertion block and the four-sweep reconstruction (A13 rows 1, 4, 5), and
`tools/source-audit-inventory.py` (A10 A05).

## 2. Findings

**R07-F1 — material: A10-F3 is false as written. Owner: A10 fragment owner + integrator
(correct or withdraw before `adj/audit-assembled.md` is finalized).**

A10-F3 asserts the c31 audit "**exits 0 while reporting failures**" and that "an
integrator who checks only the exit code reads the pre-fix red census as green". The
tool's own code and two live runs say otherwise:

- `reports/round-25/audit/c31-lessons-index-audit.py:462` — `return 0 if not res["findings"] else 1`; plain mode therefore exits **1** on the two findings, which is what I measured twice (rows 12; also masked-pipe check `PIPESTATUS=1`).
- `--json` (`:456-458`) prints the receipt and `return 0` unconditionally — so the exit-0-with-findings behaviour exists **only** under `--json` (row 13).
- The round-26 validator uses the same convention deliberately (`reports/round-26/run-validation.py:1498-1499` appends a failure when the blob differs), i.e. exit codes are the lane's fail signal here.

Corrected form for the audit: *plain-mode exit code is informative (1 = findings); a
validator leg that runs `--json` must assert on `findings[]`, not the exit code.* The
practical warning survives; the stated mechanism does not. Left uncorrected, A10-F3 puts
a false verification-hole claim into the audit record.

**R07-F2 — material: the transient filed-byte mutation touched THREE filed files, not
two. Owner: A03 (scope watch) + X02 (conformance), integrator to carry.**

A01-5 observed `reports/round-5/validation.json` and `reports/round-7/validation.json`
modified at ~03:53:56Z and "gone" at ~03:55Z. My full-repo post-declaration scan (all
paths except `.git/`, `.scratch/`, `reports/round-33/`, `-newermt 2026-10-19T03:49:01Z`)
returns **exactly three** files:

```
./reports/round-5/validation.json
./reports/round-6/validation.json
./reports/round-7/validation.json
```

- **round-6/validation.json is the third file A01 did not name** — mtime `2026-10-19 00:54:32 -0300` (03:54:32Z), inside the same mutation window.
- round-5/round-7 mtimes are `00:55:27 -0300` (03:55:27Z) — **after** A01's second observation, so the restore (or a second write) happened after A01's window closed.
- Content is fully restored: `git status --porcelain` clean for all three, and `git hash-object <f>` equals `git rev-parse HEAD:<f>` for each (`778c3f5e…`, `9f6a0f45…`, `e7a8d449…`). The mtimes are the only residual evidence, and they persist.

So the honest reading is: three filed receipts were written in the working tree during
the wave and reverted; not residual drift, but a shared_rules[1] violation event that
A03/X02 must adjudicate (A01's round-23 `c64b2b3` refresh-receipt precedent is the
authorized path; a seat-side re-run of filed validators is not). The audit must carry
the three-file set, not A01's two-file set, and must not read "reverted" as "did not
happen".

*Reconciliation with A03 (§5):* A03's independent three-path digest table and timeline
agree with this measurement and refine it — **round-6 was written but came out
byte-identical**, so the content-mutated set is two (r5, r7) and the written set is
three; A03 also times three in-tree runs (03:53:25–28Z, 03:54:15–18Z, 03:54:32–35Z) plus
the 03:55:27Z restore, and names the probable writer (C05, `to-verify`). The audit should
carry A03's timeline and digests as the authoritative form; this finding's contribution
is the completeness of the touched set and the mtime evidence that outlives the restore.

**R07-F3 — naming: "the current packet pair" has three different referents across the
landed fragments; all candidates are green. Owner: A02 fragment owner; integrator must
fix one definition in the assembled audit.**

A10's A02 row and A15 §2.2 both claim "the current packet pair" but name different
surfaces: A10 → `examples/handoff-packet.sample.md`; A15 → `reports/round-30/handoff/
declared-in-r6/packet.md` (and, as the r21 re-run, `reports/round-20/handoff/packet.md`).
My runs show every candidate is green (rows 1, 3, 4, 5), so no verdict is at risk — but
a reader cannot tell which surface the claim's threshold ("handoff gate exit 0 re-run",
`claims.json:59`) was met on. Related datum no fragment records: the **YAML** sample
serialization scans as `fields=16/16 glossary-entries=0 findings=0` (row 2), because the
glossary count is a Markdown-surface property. `examples/handoff-packet.sample.md:6-8`
states verbatim that the Markdown "supersedes `examples/handoff-packet.sample.yml` …
the .yml's own validation block records the correction", so the 0 is expected — but it
must be *named* in the audit so an integrator re-running the yml does not read it as a
regression. Recommendation: A02's row names one canonical pair (the Markdown sample plus
`reports/round-30/handoff/declared-in-r6/packet.md` as the newest real packet) and
records the yml 0-glossary reading as expected shape.

*Reconciliation with A02 (§5):* A02 has since landed and **resolves the referent by
wiring, not by mtime** — `tools/exercise-handoff-e2e.py:1933-1934` sets
`V3_BASELINE_DEFAULT` / `V3_FROZEN_DIR_DEFAULT` to `reports/round-30/handoff/
declared-in-r6/`, corroborated by `SCORECARD.md:400` and the pair's `freeze.txt:1`. So
"current" = `declared-in-r6`, A10's `examples/` sample is the non-canon sample surface
(not the current pair), and the ambiguity is closed with a citation rather than a
convention. The yml 0-glossary datum stands and remains unnamed in A02's fragment; the
integrator should add it as an expected-shape note.

**R07-F4 — material: A10's A09 row is incomplete — the lessons README carries two live
filed-round pins outside `tools/gates/frozen/`. Owner: integrator; R08's pin pass must
use A13-F1's scope, not A10's row.**

A10's A09 row concludes "**GREEN — zero digest-pin exposure; no re-pin owed**" from a
frozen-surface grep (both live digests absent from `tools/gates/frozen/`; `SKILL.md`
appearing there only as prose). That negative is correct for the frozen surface but does
not cover the pins that actually exist. Verified by me, independently of A13:

- `reports/round-26/run-validation.py:97` — `README_BASELINE_BLOB = "a31870556c733498243b56697896504a2fb3679a"`; live `git rev-parse HEAD:corpus/lessons/README.md` returns the **same blob**, and `:1498-1499` appends the failure "the filed lessons index was edited in place" when it differs.
- `reports/round-25/validation.json` `input_sha256["corpus/lessons/README.md"]` = `ec7469dadf87df3e13cdc2b53445810840d22b9c003a6407e5a449e8f44b3f4c`, equal to live `sha256sum` (row 18).

Consequence: claim O's lessons leg and the r25/r26 pins are in tension (A13-F1, filed;
the same conclusion my README-digest and c31 rows independently support). The audit must
not carry A10's "no re-pin owed" as the A09 verdict for the README leg; it must carry
A13-F1's three options and the two pin rows above. For **SKILL.md** the A10 row is
confirmed correct: no frozen row pins it (`grep` for both digests over `tools/gates/
frozen/` → zero files), and the only live reader is the spec-reference docstring at
`tools/gates/argot-derivation-gate.py:4`.

*Reconciliation with A09 (§5):* `adj/A09-pins.md` landed after this finding was written
and carries the complete cascade — E1 (the r26 blob pin, plus the mirrored seat tool
`reports/round-26/lessons/c51-revision-audit.py:48`), E2 (receipt digest maps across
r25/r26/r30/r31/r32), E3 (box-1 re-survey obligation), E4 (line anchors incl.
`AGENTS.md:42`'s live `after :534` instruction), E5 (README-side in-file pins and the
stamp hazard), with the R1–R8 re-pin list and findings A09-F1..F5. Its §5 itself rules
A10's row **errata, not a second vote**, which is the disposition this finding asked for.
My two verified pin rows above (r26 blob; r25 `input_sha256`) are the same two artifacts
as A09's E1/E2, independently measured — so the README-leg cascade now has three
independent executions (mine, A13's, A09's) agreeing on the artifacts and the digests.
A09 adds one hazard worth carrying next to R07-F2: the in-place filed-byte write is
systemic across the historical runners (`reports/round-26/run-validation.py:90,1909`
writes `validation.json` in default mode), which is why R07-F2's event recurred and why
the "never re-run a filed round's runner in-tree" rule needs to be stated, not implied.

**R07-F5 — resolved: A15's F-A15-1 is closed by A01's precision correction. Owner:
integrator (carry A01-1's wording; do not carry the open slot).**

A15 §2.1/F-A15-1 reads the `claims.json:57` parenthetical "pre-round-8" against a
"post-regimen-1" reading and leaves it open. A01-1 resolved it against commit timestamps:
`c53782a` postdates round-4's admit `fe34faa` and predates round-5's prep commits, so the
true bound is **pre-round-5**; the claim's parenthetical is understated, not false. The
assembled audit should carry A01's form. A15's F-A15-2 (1,870 vs 2,655 are different
surfaces) is likewise confirmed exactly by my rows 19–20 (1857/237/561; 1770+135=1905),
so it needs only the reconciliation note, not further measurement.

**R07-F6 — confirmed, no action: A10-F1 and A10-F2 reproduce exactly.**

A10-F1: live `typed-pipeline-gate` = 20/20 (row 15) against r21's filed 19/19
(`A11-A12-handoff.md:46`) — historical leg-count drift, verdict unchanged. A10-F2: live
`AGENTS.md` `1afaf106…` vs r29's filed `be3a9477…`
(`reports/round-29/adjacency/province-entries.md:15`) — explained by later commits
touching AGENTS.md; `PROVINCE.md` and the contract still reproduce their r29 digests.

**R07-F7 — procedural: the audit-table completeness pass.**

Claim A's `after_required` (`claims.json:59`) lists six checks; A10's nine-row table
covers all six (PROVINCE→A01, handoff→A02, scope→A03, bleed→A04, contested→A06,
language→A08) plus three supporting classes (corpus→A05, history→A07, pins→A09). No
required class is missing. What is missing is **evidence** for five of the nine rows
(A02–A09 unfiled at my last read, 03:57Z): A10's own F5 already routes that to the
integrator. Two further gaps, both owed rather than defective:

- `reports/round-33/run-validation.py` — claim A's counting command (`claims.json:61`) — does not exist yet; no fragment could have run it.
- The language sweep (`claims.json:59`, "no promotion/canon/closure language anywhere in round-33 artifacts") was last executed over a partial fragment set: mine at 03:53:36Z covered 3 files (10 hits, all negations/requirements/substring artifacts of "canonicalize"); A13's at 03:54:52Z covered 7 files, clean. It must be re-run over the final set at assembly. A10-F4 says the same; this review adds two independent time-stamped partials to compare against.

## 3. Bleed hunt (my own scan — zero unfiled bleed)

- **Outside-repo references in round-33 artifacts:** `targets.json:6` (the shared-rule text naming the repo root) and `targets.json:13` (K01's mission naming fleet report paths read-only). No fragment, claim, or target proposes a write outside `reports/round-33/`; no answer to any L0 question.
- **L0 surface:** four kotodama rows, `.ufo/l0-questions.md:44-47`; file mtime `2026-10-18 17:14:10 -0300`, before the `2026-10-19T03:49:01Z` declaration (`claims.json:6`) — round 33 added and resolved nothing there. Both contested items (bilateral read → `:44`; contract-digest ratification → `:45`) remain routed-not-absorbed, matching A10's A06 row and A15 §5.
- **Write boundary:** the full-repo mtime scan returns only the three in-repo filed files of R07-F2; `.scratch/` writes are in-repo and gitignored (`.gitignore:6`); fleet root carries no round-33 report (`ls .ufo/reports/` → latest round-32). The empty untracked tree `kotodama-shokunin/reports/round-29/defects/` (0 files; `git check-ignore` exit 1, so not ignored — merely invisible to git status) is already named by A01-5; I confirm the measurement and add that it is a path-mimic hazard (a nested directory named like the repo root), worth optional integrator cleanup, not a PROVINCE matter.
- **Contested/canon posture:** every canon/clearance/promotion/closure occurrence in the artifacts present at my scans is a negation, a requirement to scan for the language, a mission text, or a substring artifact of "canonicalize/canonicalization" — no asserting hit. My 03:53:36Z sweep: 10 hits over `claims.json`/`targets.json`/`telemetry/dispatch-declared.json`; A13's 03:54:52Z sweep: clean over 7 files. A16's own SHONEN fragment repeats "no promotion/canon/clearance/closure verdict" as a negation.

## 4. Verdict summary (my leg only — not round acceptance)

| class | verdict | basis |
|---|---|---|
| re-run of cited commands | **green with one false finding (R07-F1)** | 23 independent executions, §1 |
| audit verdict-table completeness | **green on coverage; five rows lack fragments; two owed artifacts** | R07-F7; A10-F5 |
| unfiled bleed | **zero unfiled bleed** | §3 |
| new material findings routed | R07-F1 (A10-F3 false), R07-F2 (three filed files), R07-F4 (README pins) | §2 |

No axis is judged here; this is not a promotion, canon, clearance, or closure verdict
(`claims.json:68`).

## 5. Second pass — A02, A03, A04, A09 landed after §1–§4 were written

All three landed at ~03:57–03:59Z, after my first pass. Read in full; re-checked against
my own §1 rows.

**A02-handoff.md — reviewed, green; two additions.** Its pair determination (wiring
evidence, above) resolves R07-F3. Its green rows reproduce my rows 1, 5, 6, 16 (gate
16/16/20/0 on `declared-in-r6`; `--selftest` exit 0; e2e v3 exit 0 with packet sha256
`6ced88ad…`) and add work I did not do: a foreign-cwd gate run, `packet_links` 105/105
and `packet_uncertainty` 27-claim harness runs, 58/58 manifest digests re-derived, and
three stdin tamper probes that fire `HO-MISSING` / `HO-CANON-MARKER` / `HO-CANON-CLAIM`
as designed — plus an honest disclosure of two probe-design errors (a deleted
`- canon_standing:` line and a renamed `NON-CANON` banner both exit 0, because the gate
keys on the `not canonized` phrase, `tools/gates/handoff-packet-check.py:171`). That
disclosure is the kind of negative control the audit needs; I verified the mechanism
claim by reading `:171` (`CANON_MARKER_RE`). **Addition the audit must carry:** A02-H1,
a material content finding (the current pair's D4-CL05/06/07/09 and OQ-V3-05 prose is
stale against its own manifest rows and live bytes; routed to the packet/renderer
owner). It is outside my class (I re-ran commands, not the pair's arithmetic), and I did
not independently re-measure its seven-row table — flagged `to-verify` for A11/A14, who
own fragment verification.

**A03-scope.md — reviewed, green; supersedes my R07-F2 in form.** Its counts match mine
(2655/2655; 237 frozen; 179 `corpus/lessons`; protected-root status 0 rows) and its
A03-F1 timeline/digests are the fuller record of the same event (three in-tree runs
03:53:25Z–03:54:35Z, restore 03:55:27Z, probable writer C05 `to-verify`). One point of
method: A03's final reading (`03:57:47Z`, 3 status rows) predates the fragment landings,
so its "only working-tree delta" statement is true at that instant only — the audit
should cite it as a time-stamped reading, not a standing property. Its out-of-lane scan
also adds two fleet-root observations I did not make (a round-104 `game-dev-2d` report
from another lane; a stray `bash: `-named directory predating the round) — both
explicitly non-kotodama and non-bleed.

**A04-bleed.md — reviewed, green; agrees with my §3.** Its language table (scan
03:54:38Z/03:55:30Z over 7 files) classifies every hit as negation, mission text, routed
reference, or different-sense use — consistent with my 03:53:36Z sweep and A13's
03:54:52Z sweep, so the clean reading now has three independent time stamps. Its L0 and
lore-side work is deeper than mine (append-only proof: 4 additions / 0 removals, commit
map `b372a53`/`f2b68a7`/`2421e00`; contract digest chain `e834f503…`→`50c4c2f2…`→
`5f4c02bf…`; sibling `lore-shokunin/l0-questions.md:5-7` read-only). Its F-A04-1 is the
same event as R07-F2/A03-F1; F-A04-2 explains the `LOG.md` append. I did not
independently re-run its fleet-side commands (single-execution evidence; A12 owns that
verification).

**A09-pins.md — reviewed, green; supersedes A10's A09 row as errata (as its own §5
rules).** Its E1/E2 artifacts are exactly the two pins I verified independently (r26
`README_BASELINE_BLOB`; r25 `input_sha256`), so the README-leg cascade now has three
agreeing executions (mine, A13's, A09's). Its E4 line-anchor class is new material no
other fragment carries: `AGENTS.md:42` instructs an append "after :534" in a mutable
file, the SKILL.md self-cites at `:149`/`:183` point at `:47`, and ~15 filed lesson
citations key on SKILL.md line numbers — so the C14 drafts' line behaviour decides
whether the re-pin list R5 is a no-op (line-count-neutral edit) or a re-issue. A09's
A09-F4 also names two instruments that are red/stale at HEAD (`x45` exit 1 with
`X45-P1`; `x57 --selftest` 34/37) and correctly says neither may be quoted as green —
consistent with my own measurement that `x45`'s `index_sha256` pin (`ee2a15df…`) no
longer matches the live README (`ec7469da…`), which I had read as superseded-by-Revision-2
and A09 reads as a standing red pointer finding. Both readings agree on the fact; the
audit should carry A09's framing since it names the mechanism. I did not re-run x45/x57
myself, so that pair of readings is A09-single-execution (`to-verify` for A13/R08).

**Effect on my §4 verdicts:** unchanged in direction, one revision — R07-F3 is now
resolved-by-fragment rather than owed, and R07-F2's three-file set is carried in A03's
fuller timeline. A02/A03/A04/A09 are the A-fragments whose cited commands I could
compare against my own executions: **no contradiction found**; every overlapping
measurement agrees to the digit.

## Owed

- Remaining adj fragments: `adj/A05-corpus.md`, `adj/A06-contested.md`, `adj/A07-history.md`, `adj/A08-language.md`, `adj/A11-verify-a01-a03.md`, `adj/A12-verify-a04-a06.md`, `adj/A14-verify-a10.md` (unfiled at my last read 04:0xZ) — their cited commands remain un-reviewed by this seat; the integrator should route a post-wave pass (R08 or A14) over whichever land after this file.
- `reports/round-33/adj/audit-assembled.md` — integrator: carry R07-F1 (correct A10-F3), R07-F2 with A03-F1's timeline (three written / two content-mutated), R07-F3 as resolved by A02's wiring evidence, R07-F4 as superseded by A09's E1–E5 + R1–R8 (A10's row as errata), R07-F5 (close F-A15-1 with A01's wording), and A02-H1 as a named content finding.
- `reports/round-33/run-validation.py` — claim A's counting command; does not exist yet.
- Post-wave re-run of the A08 language sweep over the final fragment set; A02-H1's seven-row table and A09's x45/x57 readings await A11/A13-class verification.

## Citations

- `reports/round-33/claims.json:6,8,29,33,57,59,61,68`; `reports/round-33/targets.json:5-11,48,54,56,60,79`
- `reports/round-33/adj/A01-province.md` (A01-1, A01-4, A01-5); `adj/A10-receipt.md` (A02/A05/A07/A09 rows; A10-F1..F6); `adj/A13-verify-a07-a09.md` (rows 1–5; F1–F3); `adj/A15-audit-draft.md` (§2.1–2.6, F-A15-1/2); `adj/A16-shonen-material.md`
- `reports/round-33/op/O07-baseline-receipt.md` (four baseline legs)
- `reports/round-25/audit/c31-lessons-index-audit.py:36,436-438,456-462`; `reports/round-25/validation.json` (`input_sha256["corpus/lessons/README.md"]`)
- `reports/round-26/run-validation.py:95-99,1494-1499`
- `reports/round-21/adjacency/A11-A12-handoff.md:43,46`; `reports/round-21/adjacency/ledger.json` (`A21-D4-XF-01`); `reports/round-29/adjacency/province-entries.md:15`
- `reports/round-32/scope.md` (1,870 protected-surface reading, via A13-F2/A15-F-A15-2)
- `examples/handoff-packet.sample.md:1-20` (supersession statement at :6-8)
- `tools/gates/handoff-packet-check.py`; `tools/gates/typed-pipeline-gate.py`; `tools/gates/argot-derivation-gate.py:4`; `tools/check-gate-battery.py`; `tools/check-craft-exercise.py`; `tools/assemble-culture-d4.py`; `tools/check-evidence-coupling.py`; `tools/exercise-handoff-e2e.py` (all executed, §1)
- `/home/vgpnk/Projects/shokunin/.ufo/l0-questions.md:44-47`; `/home/vgpnk/Projects/shokunin/.ufo/reports/round-32/kotodama.md` (stat only)
- `.gitignore:6`; `PROVINCE.md:25,31`
- Commands (all 2026-10-19, lane root, read-only): the 23 rows of §1 plus `git status --porcelain=v1 -uall` (5 rows at 03:53Z; 23 rows at 03:57Z = 21 `reports/round-33/` fragments + `LOG.md` + `REGIMEN.md`; 36 rows at 03:59Z as landings continued); `find . -path ./.git -prune -o -path ./.scratch -prune -o -path ./reports/round-33 -prune -o -type f -newermt "2026-10-19T03:49:01Z" -print` (3 filed files); `git hash-object`/`git rev-parse HEAD:<f>` for those three (equal); `stat -c '%y %n'` for them; `git rev-parse HEAD:corpus/lessons/README.md`; `git check-ignore -v kotodama-shokunin/reports/round-29/defects` (exit 1); `find kotodama-shokunin -type f | wc -l` (0); `grep -rn -i "promotion\|promoted\|canon\|canoniz\|clearance\|closur" reports/round-33/` at 03:53:36Z (10 hits, classified).
