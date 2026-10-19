- Seat: S03 | scribe | claim C | date 2026-10-19 | baseline da68a6d

# S03 — final claim-C receipt, post-review fold

Mission: `reports/round-34/targets.json:81` — "Final C receipt post-review."
Every number below is measured in this seat's own window (2026-10-19, ~04:0xZ,
lane HEAD `da68a6d705e41f369f21e8607bfaab5b54077f84`, `export
TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, repo root). No
`reports/round-*/run-validation.py` was executed (F-C13-1). No file outside
`reports/round-34/` was written by this seat.

## 1. Claim under receipt

`reports/round-34/claims.json:56` — claim **C** (axis: calibration): "Pin the
box-1 executable-surface evidence durable at the new SKILL digest: land a dated
box-1 re-survey receipt at SKILL.md sha256 f9bd07c2… (28/28 named executables
resolve at the post-round-33 bytes) and file the A09 R1–R8 SKILL anchor reissue
as new rows (old anchors recorded as superseded readings, filed rows
untouched)."

Thresholds (`reports/round-34/claims.json:65`): "28/28 at the new digest; the
reissue table covers every A09 R1–R8 row; zero filed-row edits."

| after_required item (`claims.json:60`) | state at this seat's cut | evidence |
|---|---|---|
| `reports/round-34/craft/box1-resurvey-durable.json` + receipt lands | **CONTENT LANDED AS FRAGMENTS, FILE NOT YET FILED** — `calib/C02-receipt-json.md` (28-row JSON, verified below) and `calib/C06-scribe.md` L1 supply it; `ls reports/round-34/craft` → still absent. Appendix A is S03's independent fallback copy | §2, §8.3, Appendix A |
| 28/28 executables resolve at f9bd07c2…, digest-pinned, dated, re-runnable | **MEASURED GREEN, non-author-verified** — S03 run (§2) + C07's independent re-run (§8.2) + negative controls (27/28, exit 1); the "dated" leg needs a field the tool does not emit (S03-F3 = C09-F1 = C06's S-C06-1) | §2, §8.2 |
| R1–R8 anchor reissue as old → new → owning row, each grep-verified | **SUPPLIED HERE** (8/8 rows, §4) and independently in `calib/C09-final-receipt.md:254-265`; `calib/C03`/`C08` still absent | §4, §8.1, §8.4 |
| promotion-dossier box-1 evidence current at HEAD | **SUPERSEDING ROW SUPPLIED**; the filed dossier row cannot be re-greened (S03-F2, corroborated by `scout/K04-anchor-census.md:98-103,118-120`) | §4 R4, §5 |
| zero filed-row edits | **MEASURED** — tree byte-clean vs `da68a6d`; independently confirmed by `calib/C04-byte-check.md:22` and `depth/D11-preservation.md` | §6 |

## 2. Evidence A — the counting command, re-run at HEAD

```
$ sha256sum SKILL.md
f9bd07c2bd13462367be20e8d775cec1c5569eb2e575dc5d078519ecc72e5a9b  SKILL.md
$ wc -l SKILL.md
732 SKILL.md
$ python3 -B reports/round-30/craft/box1-survey.py
{
 "date": "2026-10-18",
 "named": 28,
 "resolvable": 28,
 "unnamed_in_skill": [],
 "skill_sha256": "f9bd07c2bd13462367be20e8d775cec1c5569eb2e575dc5d078519ecc72e5a9b"
}
exit=0
```

The filed post-landing receipt this supersedes reads `83b0a78a…` 28/28
(`reports/round-30/craft/box1-landed-survey.json:4-6`) and the last filed
closure row reads `79fe91d3…`
(`reports/round-32/final-dossier.md:46`, `reports/round-31/validation.json:1026`,
`reports/round-32/validation.json:1000`). The digest move 715 → 732 lines is
`git show --numstat da68a6d -- SKILL.md` → `35  18  SKILL.md` (net +17).

## 3. Evidence B — the 28-row inventory (digest-pinned)

Method: the same regex the tool uses (`tools/[\w./-]+\.py`, i.e.
`reports/round-30/craft/box1-survey.py:6`) applied by this seat over the
`f9bd07c2…` bytes, reporting the **first** occurrence line per unique path
(the tool itself reports only the counts, so the address column is this seat's
additive measurement, not the tool's output):

| # | SKILL.md line | path | resolves |
|---|---|---|---|
| 1 | 35 | `tools/d2-typed-labels.py` | yes |
| 2 | 89 | `tools/harness/packet_uncertainty.py` | yes |
| 3 | 138 | `tools/gates/typed-pipeline-gate.py` | yes |
| 4 | 139 | `tools/assemble-d4-typed.py` | yes |
| 5 | 207 | `tools/assemble-culture-d4.py` | yes |
| 6 | 212 | `tools/replay-frozen.py` | yes |
| 7 | 375 | `tools/gates/argot-derivation-gate.py` | yes |
| 8 | 409 | `tools/gates/register-law-gate.py` | yes |
| 9 | 448 | `tools/exercise-handoff-e2e.py` | yes |
| 10 | 449 | `tools/assemble-d2-typed.py` | yes |
| 11 | 450 | `tools/gates/d4-assembly-check-gate.py` | yes |
| 12 | 451 | `tools/gates/d4-typed-labels-check-gate.py` | yes |
| 13 | 452 | `tools/harness/packet_links.py` | yes |
| 14 | 453 | `tools/harness/receipt_guard.py` | yes |
| 15 | 454 | `tools/harness/r8_checks.py` | yes |
| 16 | 500 | `tools/gates/handoff-packet-check.py` | yes |
| 17 | 606 | `tools/gates/phonology-sanity-gate.py` | yes |
| 18 | 607 | `tools/gates/lexicon-coverage-audit.py` | yes |
| 19 | 608 | `tools/gates/myth-consistency-gate.py` | yes |
| 20 | 609 | `tools/gates/costume-era-consistency-gate.py` | yes |
| 21 | 610 | `tools/gates/naming-collision-gate.py` | yes |
| 22 | 611 | `tools/gates/provenance-audit.py` | yes |
| 23 | 614 | `tools/source-audit-inventory.py` | yes |
| 24 | 615 | `tools/assemble-d2.py` | yes |
| 25 | 616 | `tools/check-craft-exercise.py` | yes |
| 26 | 617 | `tools/check-gate-battery.py` | yes |
| 27 | 673 | `tools/assemble-culture-d3.py` | yes |
| 28 | 674 | `tools/check-evidence-coupling.py` | yes |

28 unique paths, 28 resolving, 0 unnamed — identical set to the filed
`83b0a78a…` survey's 28/28 count, so the round-33 SKILL edits did not move the
`named_in_skill` set.

## 4. Evidence C — A09 R1–R8 reissue table (old anchor → current state → owning row)

A09's list is `reports/round-33/adj/A09-pins.md:105-116` (§3, rows R1–R8). Each
row below is re-measured at HEAD by this seat; "old" is the filed reading,
"now" is this seat's grep-verified address/content.

| row | old reading (filed) | state at HEAD `da68a6d` | verification |
|---|---|---|---|
| **R1** README blob pin | `reports/round-26/run-validation.py:97` `README_BASELINE_BLOB = "a3187055…"` | **SUPERSEDED** — live blob `73f3e1bd29d4569ddd2a5d9a2309f4451fa35ae5` (round-33 O landing edited the README) | `git hash-object corpus/lessons/README.md` = `git rev-parse HEAD:corpus/lessons/README.md`; pin line re-read at `:96-97`. New-row record owed (integrator); the r26 runner must not be re-run in-tree — `:90`/`:1909` rewrite its filed `validation.json` |
| **R2** README sha256 receipts | `ec7469da…` at 6+ filed sites (A09 §2.2) | **SUPERSEDED** — live `f752e1d79ae627a0d9728fe16fd1532e7cb9e587f6ac7025a880d8af46233868`; 41 filed files still carry `ec7469da` | `sha256sum corpus/lessons/README.md`; `grep -rl ec7469da reports/ tools/ \| wc -l` → 41 |
| **R3** SKILL.md sha256 receipts | `79fe91d3…` (8 sites), `83b0a78a…` (2 sites) | **SUPERSEDED** — live `f9bd07c2…`; 32 filed files carry `79fe91d3`, 11 carry `83b0a78a`; **zero filed files carry `f9bd07c2`** (only round-33's own audit-assembled draft and this round's claims/targets) | `sha256sum SKILL.md`; `grep -rl` counts above; `grep -rl f9bd07c2 reports/ tools/ SKILL.md AGENTS.md` |
| **R4** box-1 re-survey | `reports/round-30/craft/box1-landed-survey.json:4-6` → `83b0a78a…` 28/28 | **RE-SURVEYED GREEN at the new digest** (28/28, exit 0, `f9bd07c2…`, §2). Durable file owed: `reports/round-34/craft/box1-resurvey-durable.json` (content = Appendix A) | §2 command; `ls reports/round-34/craft` → absent |
| **R5** line anchors | `AGENTS.md:42`; `SKILL.md:149,:183` (self-cites of `:47`); `:522/:534/:535/:536`; `:660`; `:713-715`; audit at `:715` | **MIXED — see the anchor table below**; the `AGENTS.md:42` anchor is *gone*, not moved | `sed`/`grep` per line below |
| **R6** README prose arithmetic + row cells | A09 measured `C34b` FAIL (`stated 26/26` vs `measured 26/33`) and §2 cells unrestated | **GREEN** — c31 exit 0, `findings: 0`, `lesson files: 33`, `index rows: 33`, `PASS C31/C32/C33/C34/C34b/C34c` | `python3 -B reports/round-25/audit/c31-lessons-index-audit.py` (exit 0), output quoted in §5 |
| **R7** `x45` / `x57` instrument states | A09: `x45` exit 1 `X45-P1`; `x57 --selftest` 34/37 | **STILL RED, drift** — `x45` exit 1 with the same `X45-P1` class (4 unresolved-pointer tuples); `x57 --selftest` now **28/37** (9 named failures) | §5 commands; carried as named findings, never quoted green |
| **R8** README rows vs round-33 lesson landing order | hazard: a round-33 lesson landing after the stamp re-opens `C31-1` with one orphan | **CLOSED** — partition 33 `*.md`, index rows 33, `PASS C31_index_rows_eq_files`, no orphan | `ls corpus/lessons/*.md \| wc -l` → 33; c31 output §5 |

### R5 anchor reissue (grep-verified, old → now)

| old anchor | old content (filed citation) | address at 732 lines | status |
|---|---|---|---|
| `AGENTS.md:42` | `### 2.2 SKILL.md — append one item to "## Checklist (executable where a tool exists)" (after :534)` | **ABSENT** — `wc -l AGENTS.md` → 40; `grep -n "SKILL" AGENTS.md` → 0 hits | **anchor removed** by `da68a6d` (`git show da68a6d -- AGENTS.md` → `-` that heading and the closing fence, 2 lines deleted). Reissue = "no live anchor remains"; not a moved line |
| `SKILL.md:47` (self-cite target) | `\| Untyped legacy record \| no kind \| …` | `:47` unchanged, same content | holds |
| `SKILL.md:149`, `SKILL.md:183` (self-cites of `:47`) | register row / era-language row cite `SKILL.md:47` | `:149`, `:183` unchanged; both target `:47` still correct | holds |
| `SKILL.md:294` | `Propagation/tamper` register-law row | `:294` unchanged | holds (cited by `corpus/lessons/round-31.md:46`) |
| `SKILL.md:456-458` | "Run scratch-writing tools only after `export TMPDIR=$PWD/.scratch`…" | `:456-458` unchanged | holds (cited by `corpus/lessons/round-31.md:46`) |
| `SKILL.md:522` | `## Checklist (executable where a tool exists)` | `:522` unchanged | holds |
| `SKILL.md:534` / `:535` / `:536` | last checklist content line / blank / `## Corpus map` | `:534` / `:535` / `:536` unchanged | holds (cited by `corpus/lessons/round-31.md:46`) |
| `SKILL.md:660` | `## Source-bounded culture drill — D3 (round 7)` | **`:662`** (+2) | shifted; `corpus/lessons/round-32.md:33` cites `:660` → superseded reading, filed row untouched |
| `SKILL.md:713-715` | the round-31 availability checklist item (end of file) | now **`:729-732`** (+16/+17); the old address carries the round-33 O05 expected-verdict prose (`:713-720`) | shifted **and** its text was re-keyed; `corpus/lessons/round-32.md:33,55,57` cite `:713-715` → superseded readings |
| `SKILL.md:715` audit command (F-X16-3) | availability audit requiring `telemetry/closing-snapshot.json` | **`:732`**, semantics re-keyed to `closes` + `closes_sha256` + `availability-close-*.json` | shifted and repaired in place; **verified: it prints nothing at HEAD** (`python3 -c …` verbatim from `SKILL.md:732`, exit 0), i.e. the F-X16-3 false-fire no longer fires |

Address arithmetic is corroborated by the patch hunks: `da68a6d`'s SKILL
hunks are `@@ -125,7 +125,7 @@` (neutral), `@@ -476,19 +476,19 @@` (neutral),
`@@ -581,7 +581,9 @@` (+2), `@@ -691,17 +691,31 @@` (+14), `@@ -711,5 +727,6 @@`
(+1) — total +17, so everything after line 583 shifts by +2 and everything
after 727 by +16/+17, which is exactly what the table shows.

Every old-address reading above lives in **filed bytes** and was **not
edited**: `corpus/lessons/round-31.md:46`, `corpus/lessons/round-32.md:7,33,41,55,57,58`,
`reports/round-33/adj/A09-pins.md:105-116`, `reports/round-32/final-dossier.md:46`.

## 5. Evidence D — peer-instrument states at HEAD (named, not averaged)

```
$ python3 -B reports/round-25/audit/c31-lessons-index-audit.py
exit=0
index present: True
lesson files:  33
index rows:    33
queue rows:    78
formats:       {'gate-keeper': 21, 'fragment-index': 5, 'plain': 7}
  PASS C31_index_rows_eq_files
  PASS C32_owners_resolve
  PASS C33_formats_documented
  PASS C34_pins_rederived
  PASS C34c_shape_cells_rederived
  PASS C34b_prose_arithmetic
findings:      0

$ python3 -B reports/round-25/audit/x45-lessons-pointer-audit.py
exit=1
lesson files: 33 / index rows: 33 / queue rows: 78 / carry rows: 30
  FAIL P1_pointers_resolve   (findings: 1)   # X45-P1, 4 unresolved-pointer tuples
  PASS P2_prose_counts, P3_queue_cross_consistency

$ python3 -B reports/round-27/audit/x57-lessons-audit.py --selftest
exit=1   passed 28 / total 37
fails: partition is 27 md files; filed rows are 26; revision pins drift on exactly one
row (live control); filed orphan is exactly round-26.md (live control); revision has no
orphan (live control); filed queue is 49 rows (live control); G2 silent when the revision
pin matches the live bytes; I reads 49 queue ids and 49 disposition rows; I is green on
the live revision

$ python3 -c "… the SKILL.md:732 audit verbatim …"     # read-only, per r31 rule
(no output)  exit=0        # every open-at-seat-close record with a landed receipt is closed
```

All three peer instruments only print (`grep -n "write_text|open(…'w'|json.dump"`
over them → print-only), and `git status --porcelain` after the runs shows no
new or modified path (`?? reports/round-34/` only).

## 6. Evidence E — filed-byte preservation (this seat's own commands)

```
$ git diff-index --quiet HEAD; echo "EXIT=$?"          → EXIT=0
$ git diff --name-only HEAD | wc -l                    → 0
$ git status --porcelain                               → ?? reports/round-34/
$ for d in reports/round-22 reports/round-23 reports/round-25 reports/round-26 \
           reports/round-30; do git status --porcelain -- "$d" | grep -c .; done → 0 0 0 0 0
```

Round 33 is the admitted revision this round builds on (`da68a6d`); zero
tracked bytes differ, and the only untracked path is this round's own
directory. Independent witness from a neighbouring seat: the whole-set filed
fingerprint `1713e725abbd3a73b03ff2e42a8774adcd9b8c294c458f25d4657065b126ce71`
over the 1909 tracked files of `reports/round-5..33`
(`reports/round-34/depth/D11-preservation.md:107-170`).

## 7. Findings from this post-review

| id | finding | class | owner | evidence |
|---|---|---|---|---|
| **S03-F1** | A09's R5 anchor `AGENTS.md:42` no longer exists — `da68a6d` deleted the `### 2.2 … (after :534)` block. A reissue row that expects a *new* line number would invent one; the honest reissue row is "anchor removed, user of the anchor gone". | correction to the reissue table | integrator | `wc -l AGENTS.md` → 40; `grep -n SKILL AGENTS.md` → 0; `git show da68a6d -- AGENTS.md` |
| **S03-F2** | The round-30 box-1 leg can never be re-greened from outside round-30: `documents()` reads only `safe_path(ROUND).rglob("*.md")` (`reports/round-30/run-validation.py:294-302`) and a passing box report must contain the *current* SKILL digest (`:674-685`, `:697-698`). A round-34 durable receipt is therefore a **superseding record**, and the filed r30/r32 rows read as superseded readings at `f9bd07c2…` — not as falsified claims. | design constraint | integrator | `reports/round-30/run-validation.py:294-302,674-685,697-698` |
| **S03-F3** | `reports/round-30/craft/box1-survey.py:8` hard-codes `"date": "2026-10-18"`, so a durable receipt that quotes the tool's stdout verbatim carries a **stale survey date**. The receipt must carry its own `survey_date: 2026-10-19` (and may name `tool_date: 2026-10-18`). The tool is otherwise re-runnable and exit-code-correct. | correctness of the durable artifact | C02 / integrator | `reports/round-30/craft/box1-survey.py:8`; §2 output |
| **S03-F4** | `x57 --selftest` drifted 34/37 (round-33 baseline, `reports/round-33/adj/A09-pins.md:100`) → **28/37** at HEAD, with 9 named failing controls (historical partition/revision pins baked at r27/r28). It is on no live round-34 surface (`grep` over round-26..32 runners → 0 hits, A09 §2.5) but must not be quoted as a green instrument. | drift, named | integrator / A15-class owner | §5 command output |
| **S03-F5** | The round-31 rule's instrument is now clean: the re-keyed audit at `SKILL.md:729-732` prints nothing at HEAD while six rounds' `open-at-seat-close` records exist — the r31 sanitizer's F-X16-3 false-fire is repaired in place (new row). | confirmation | integrator | §5 command; `SKILL.md:729-732` |
| **S03-F6** | **Errata to `calib/C09-final-receipt.md`'s C09-F2 (partial).** C09 claims `:456-458`, `:522`, `:534-536` "have no live citer". Refuted by direct read: `corpus/lessons/round-31.md:46` carries exactly those tokens (shorthand `:N` form — no `SKILL.md:` prefix — which is why a `SKILL.md:N` census regex misses them). All are class U, so no staleness follows; but a table built on C09's census drops live citers A09 correctly grouped. C03's landed table agrees with this reading (`calib/C03-anchor-reissue.md:87,100-102` cites `round-31.md:46` as the citer for `:456-458`/`:522`/`:534`). C09-F2's other half **stands and is confirmed**: `corpus/lessons/README.md:242,244,245` and `corpus/lessons/round-32.md:34` are real citer sites A09 §2.4 did not list (coverage-counting completeness, not staleness) — independently found as C08-F4 (`calib/C08-verify-reissue.md:138`). | errata | integrator: fold C09-F2 as "partially accepted" | §8.4 grep output; `calib/C03-anchor-reissue.md:87,100-102`; `calib/C08-verify-reissue.md:138` |
| **S03-F7** | **C07's owed comparator is discharged.** Run by this seat against the landed `calib/C02-receipt-json.md`: 28/28 rows on both sides, 0 missing/extra, 0 field mismatches (`first_line`/`resolves`/`sha256`), identical `skill_sha256`; C02's `survey_script_sha256` equals this seat's own `sha256sum` of the tool. | verification (closes a filed `## Owed`) | integrator | §8.3 |

## 8. Post-review fold (what landed)

Reads ran 04:0xZ–07:1xZ. The C block landed after this seat's first pass, so
the fold below is against the files, not against their promise.

### 8.1 Fold table

| seat | artifact | verdict on content | fold |
|---|---|---|---|
| C01 | `calib/C01-survey-run.md` | survey run + row-shape analysis + independent 28-row derivation; consistent with §2/§3 | accepted |
| C02 | `calib/C02-receipt-json.md` | the canonical durable JSON: `measured_at_utc 2026-10-19T07:10:37Z`, `survey_script_sha256 d923ae0f…`, supersession provenance, `rerun_exit_code 0` | accepted — **land this, not Appendix A** (§8.3) |
| C04 | `calib/C04-byte-check.md:22` | "CONFIRMED — zero filed-round edits are needed" | accepted; agrees with §6 |
| C05 | `calib/C05-receipt.md` | before→after receipt draft; its anchor map §4 and R-row states §5 carry no row that conflicts with §4 here | accepted |
| C06 | `calib/C06-scribe.md:44-63` | S-C06-1: the durable JSON is hand-assembled (tool `date` hard-coded; field names differ; `REGISTER_CRAFT_SURVEY_MODE` is inert) | accepted; third independent seat on the same finding as S03-F3/C09-F1 |
| C07 | `calib/C07-verify-survey.md` | independent 28/28 at `f9bd07c2…`, two extraction methods, negative control 27/28 exit 1, 28/28 HEAD-tracked; row set identical to §3 | **accepted — this is the non-author check claim C needs** |
| C09 | `calib/C09-final-receipt.md` | material-complete fold; §5 anchor table agrees with §4 here on every address; F1 ≡ S03-F3; F3 (the "R1–R8" referent ambiguity) accepted | accepted with errata S03-F6 |
| K04 | `scout/K04-anchor-census.md:80-120` | the filed consumer's contract: r30 reads **`.md` only** and needs date + command token + `unnamed`/`executable(s)`/`inventory` + the full digest; adds that the r30 leg cannot be re-greened from outside round-30 | accepted; corroborates S03-F2 and sharpens the Appendix A carrier choice |
| C03 | `calib/C03-anchor-reissue.md` (landed after this seat's first pass) | the reissue rendered as rows from a difflib opcode map over `139e3b6:SKILL.md` → HEAD: eight same-line rewrites, five insertion hunks with cumulative deltas +2/+3/+5/+16/+17, `AGENTS.md:42` classified **retired** | **accepted** — agrees with §4 here on every address; its rows at `C03:87,100-102` cite `corpus/lessons/round-31.md:46` for `:456-458`/`:522`/`:534`, independently refuting C09-F2 (S03-F6) |
| C08 | `calib/C08-verify-reissue.md` | independent ground truth (shift map, acceptance checks A–F, both audit revisions executed: old `715` audit → 5 records, new `732` audit → 0 records), non-uniform shift C08-F6, era-blob caveat C08-F1 | **accepted** — corroborates S03-F1 (retirement), S03-F5 (re-key effective), S03-F6 (its C08-F4 is the same A09 §2.4 completeness gap); its own row-by-row verdict against C03 is still owed (see `## Owed`) |
| R06, R07 | `review/R06-c-review.md`, `review/R07-c-review.md` | **absent at every read** (`ls reports/round-34/review/` → R02, R03, R04, R05) | **owed** — no adversarial finding folded |

### 8.2 The non-author check

C07 re-ran the survey twice (byte-identical stdout), re-derived the rows through
a different code path (token-split + `grep -nEo` + per-row `test -f`), proved
the green is not an artefact (off-tree unmodified copy → 28/28 exit 0; one
mutated path → 27/28, exit 1, tool digest moves), and checked every row is
HEAD-tracked. Its 28/28 at `f9bd07c2…` and its anchor values match §2/§3.

### 8.3 C07's owed comparator, executed here

```
mine 28 C02 28
missing in C02: []
extra in C02  : []
digest C02: f9bd07c2bd13462367be20e8d775cec1c5569eb2e575dc5d078519ecc72e5a9b | mine: (same)
mismatches: 0
C02 top-level keys: ['date','executable_inventory_note','measured_at_utc','mode',
 'named_in_skill','provenance','rerun','rerun_exit_code','resolvable','reverify',
 'round','rows','rows_scope_note','skill','skill_lines','skill_sha256',
 'survey_script','survey_script_sha256','survey_stdout','survey_stdout_note','unresolvable']
```

C02's `survey_script_sha256` also equals this seat's own
`sha256sum reports/round-30/craft/box1-survey.py` →
`d923ae0fcd544513122851b55389111b3195528f8e3a4c8fb69703072132cf89`, so all three
pins the durable JSON carries (SKILL digest, line count, tool digest) are
independently confirmed. **C07's `## Owed` item is discharged by this run.**

### 8.4 Errata vs C09-F2 (with the grep)

```
$ grep -n ':456-458\|:522\|:534\|:535\|:536\|:294' corpus/lessons/round-31.md
46:- **The SKILL evidence rows verify.** `SKILL.md:294` carries the `mirror_unsafe`
   exit-2 r24 cold-run control; `:456-458` carries the mirror-safety prose; `:522`
   is `## Checklist (executable where a tool exists)`; `:534` is the checklist's
   last content line (`:535` blank, `:536` `## Corpus map`). The draft's SKILL
   anchor "append after :534" is **correct**.
```

The live citers exist in shorthand `:N` form — confirmed, not inferred. Every
one is class U (address and content unchanged), so no staleness follows; the
reissue table must nevertheless keep those rows, and a census that drops them is
wrong on coverage. C09's other half is confirmed: `corpus/lessons/README.md:242,244,245`
and `corpus/lessons/round-32.md:34` cite `:715`/`:713-715`/`:294` and were absent
from A09 §2.4's list.

## 9. Post-review verdict on claim C (this seat's; the round verdict is the integrator's)

Threshold 1 — 28/28 at the new digest: **measured, independently verified**
(§2, §8.2), with live negative controls (27/28, exit 1). Threshold 2 — the
reissue covers every A09 R1–R8 row: **supplied 8/8** (§4), with the C09-F3
referent ambiguity named. Threshold 3 — zero filed-row edits: **measured**
(§6; `calib/C04-byte-check.md:22`; `depth/D11-preservation.md:107-170`). Per
`REGIMEN.md:37-43` the admission verdict is not this seat's to make; what this
fold can state is that **no leg is unproven except those owned by the four
absent seats (C03, C08, R06, R07)**, and that the one red instrument on the
claim's surface (`x57 --selftest` 28/37, S03-F4) is pre-existing drift, not a
regression this claim caused.

## Appendix A — durable receipt content for `reports/round-34/craft/box1-resurvey-durable.json`

**Landing preference: use `calib/C02-receipt-json.md`'s JSON** — it is the
richer shape (dated `measured_at_utc`, `survey_script_sha256` `d923ae0f…`,
supersession provenance, `rerun_exit_code`) and it passed the C07 row-for-row
comparator when this seat ran it (§8.3). The block below is S03's independent
reconstruction, kept as (a) the parity reference and (b) the fallback if C02's
fragment is lost.

Land this byte-for-byte (integrator); `date` is the *tool's* frozen string and
`survey_date` is this seat's measurement date (finding S03-F3), and
`executables` is additive to the tool's own key shape. The receipt satisfies
the r30-style discovery contract independently of that leg's scoping: it
contains a `20\d{2}-\d{2}-\d{2}` date and a command token
(`reports/round-30/run-validation.py:43-45`), names "executables"/"inventory",
and contains the current digest verbatim. K04 adds a second carrier
requirement this file cannot meet alone: the r30 consumer reads **`.md` only**
(`scout/K04-anchor-census.md:98-103`), so the prose receipt must be the
markdown twin (or this fragment treated as one).

```json
{
  "schema": "kotodama-box1-resurvey-v1",
  "survey_date": "2026-10-19",
  "tool": "reports/round-30/craft/box1-survey.py",
  "tool_command": "python3 -B reports/round-30/craft/box1-survey.py",
  "tool_date": "2026-10-18",
  "tool_exit": 0,
  "survey_script_sha256": "d923ae0fcd544513122851b55389111b3195528f8e3a4c8fb69703072132cf89",
  "skill_sha256": "f9bd07c2bd13462367be20e8d775cec1c5569eb2e575dc5d078519ecc72e5a9b",
  "skill_lines": 732,
  "named": 28,
  "resolvable": 28,
  "unnamed_in_skill": [],
  "supersedes": {
    "path": "reports/round-30/craft/box1-landed-survey.json",
    "skill_sha256": "83b0a78ae7a0e09f5d12a686ac01b23f2ff10b312644fbc3b534a232a666f091",
    "reading": "28/28 at the pre-round-33 bytes; superseded reading, filed bytes untouched"
  },
  "executables": [
    {"line": 35, "path": "tools/d2-typed-labels.py", "resolves": true},
    {"line": 89, "path": "tools/harness/packet_uncertainty.py", "resolves": true},
    {"line": 138, "path": "tools/gates/typed-pipeline-gate.py", "resolves": true},
    {"line": 139, "path": "tools/assemble-d4-typed.py", "resolves": true},
    {"line": 207, "path": "tools/assemble-culture-d4.py", "resolves": true},
    {"line": 212, "path": "tools/replay-frozen.py", "resolves": true},
    {"line": 375, "path": "tools/gates/argot-derivation-gate.py", "resolves": true},
    {"line": 409, "path": "tools/gates/register-law-gate.py", "resolves": true},
    {"line": 448, "path": "tools/exercise-handoff-e2e.py", "resolves": true},
    {"line": 449, "path": "tools/assemble-d2-typed.py", "resolves": true},
    {"line": 450, "path": "tools/gates/d4-assembly-check-gate.py", "resolves": true},
    {"line": 451, "path": "tools/gates/d4-typed-labels-check-gate.py", "resolves": true},
    {"line": 452, "path": "tools/harness/packet_links.py", "resolves": true},
    {"line": 453, "path": "tools/harness/receipt_guard.py", "resolves": true},
    {"line": 454, "path": "tools/harness/r8_checks.py", "resolves": true},
    {"line": 500, "path": "tools/gates/handoff-packet-check.py", "resolves": true},
    {"line": 606, "path": "tools/gates/phonology-sanity-gate.py", "resolves": true},
    {"line": 607, "path": "tools/gates/lexicon-coverage-audit.py", "resolves": true},
    {"line": 608, "path": "tools/gates/myth-consistency-gate.py", "resolves": true},
    {"line": 609, "path": "tools/gates/costume-era-consistency-gate.py", "resolves": true},
    {"line": 610, "path": "tools/gates/naming-collision-gate.py", "resolves": true},
    {"line": 611, "path": "tools/gates/provenance-audit.py", "resolves": true},
    {"line": 614, "path": "tools/source-audit-inventory.py", "resolves": true},
    {"line": 615, "path": "tools/assemble-d2.py", "resolves": true},
    {"line": 616, "path": "tools/check-craft-exercise.py", "resolves": true},
    {"line": 617, "path": "tools/check-gate-battery.py", "resolves": true},
    {"line": 673, "path": "tools/assemble-culture-d3.py", "resolves": true},
    {"line": 674, "path": "tools/check-evidence-coupling.py", "resolves": true}
  ],
  "reproduce": "python3 -B reports/round-30/craft/box1-survey.py  # exit 0, named 28 == resolvable 28, skill_sha256 f9bd07c2…"
}
```

Line addresses are first-occurrence positions under the regex in
`reports/round-30/craft/box1-survey.py:6`; re-derive with the one-liner in
`## Citations`. Verify after landing:
`python3 reports/round-34/run-validation.py` (leg owed — the file does not
exist yet).

## Owed

- `reports/round-34/craft/box1-resurvey-durable.json` — **content landed as a
  fragment (`calib/C02-receipt-json.md`), the file itself not yet filed**
  (`ls reports/round-34/craft` → absent at this seat's cut). Land **C02's** JSON
  (preferred; §8.3 verified it row-for-row); Appendix A is S03's independent
  fallback and parity reference.
- `reports/round-34/craft/<box-1-named>.md` — the **markdown twin**: per
  `scout/K04-anchor-census.md:98-103` the r30 consumer reads `.md` only, so the
  prose receipt (not the JSON) is the shape-precedent carrier. `calib/C06-scribe.md`
  §5 carries the landed-changes material; this fragment can serve as the twin.
- C08's own `## Owed` — the row-by-row verdict of C03's table against C08's §3
  ground truth (`calib/C08-verify-reissue.md:151-164`): C03 landed **after** C08's
  reads, so the mechanical comparison (C08 §4 checks A–F) is still owed to the
  integrator or a follow-up verifier. This seat's spot-checks agree wherever the
  two overlap (retirement = S03-F1; item at `:729-732`; delta classes +0/+2/+16;
  non-uniform shift as in `calib/C03-anchor-reissue.md:21-54`).
- `reports/round-34/calib/C03-anchor-reissue.md`,
  `reports/round-34/calib/C08-verify-reissue.md` — **landed and folded** (§8.1);
  no longer owed.
- `reports/round-34/review/R06-c-review.md`, `reports/round-34/review/R07-c-review.md`
  — absent (`ls reports/round-34/review/` → R02, R04, R05). No adversarial
  finding is folded: this receipt is post-measurement and post-C-block-fold,
  **not** post-review. Claim C's admission should either wait for R06/R07 or
  record the gap explicitly.
- `reports/round-34/run-validation.py` (claim C's second counting command) — does
  not exist at this seat's reads; §2/§4/§8.3 are the evidence its C legs must
  check.
- Anchor reissue rows R1/R2/R3/R6/R7 new-row receipts (README blob
  supersession, README/SKILL digest reissues, c31/x45/x57 states) — not filed;
  §4 and §5 carry the readings the integrator files.
- C07's own `## Owed` item (its C02 comparator) — **discharged by §8.3**;
  `calib/C07-verify-survey.md:242-249` still shows it open, so the integrator
  should cite §8.3 as the closing record rather than editing C07's bytes.

## Citations

- `reports/round-34/claims.json:56,60,62,65` (claim C + after_required + thresholds); `:68-74` (non-goals); `reports/round-34/targets.json:81` (S03 mission/out), `:5-11` (shared rules)
- `REGIMEN.md:52-58` (per-round contract: record set, verdicts, telemetry)
- **commands (2026-10-19 ~04:0xZ, repo root, `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`):** `git rev-parse HEAD` → `da68a6d705e41f369f21e8607bfaab5b54077f84`; `git log -1 --format=%cI HEAD`; `sha256sum SKILL.md corpus/lessons/README.md AGENTS.md`; `wc -l SKILL.md AGENTS.md corpus/lessons/README.md`; `git hash-object corpus/lessons/README.md`; `git rev-parse HEAD:corpus/lessons/README.md`; `git show --numstat da68a6d -- SKILL.md`; `git show da68a6d -- SKILL.md AGENTS.md`; `sed -n '47p;128p;149p;183p;294p;456,458p;486p;488p;501p;522p;534,536p;660p;662p;710p;713,715p;729,732p' SKILL.md`; `grep -n '^## ' SKILL.md`; `grep -n "passing example checks…\|Every availability/dispatch record filed\|must print nothing once" SKILL.md`; python one-liner (regex `tools/[\w./-]+\.py` over SKILL.md, first occurrence per unique path → 28 rows, the table in §3); `python3 -B reports/round-30/craft/box1-survey.py` (exit 0); `python3 -B reports/round-25/audit/c31-lessons-index-audit.py` (exit 0, findings 0); `python3 -B reports/round-25/audit/x45-lessons-pointer-audit.py` (exit 1, X45-P1); `python3 -B reports/round-27/audit/x57-lessons-audit.py --selftest` (exit 1, 28/37); the `SKILL.md:732` audit verbatim (no output, exit 0); `grep -rl ec7469da|79fe91d3|83b0a78a|a3187055 reports/ tools/` (41/32/11/36 files); `grep -rl f9bd07c2 reports/ tools/ SKILL.md AGENTS.md`; `grep -n write_text|open(…'w')|json.dump` over c31/x45/x57 (print-only); `git diff-index --quiet HEAD`; `git diff --name-only HEAD | wc -l`; `git status --porcelain`; `ls corpus/lessons/*.md | wc -l` → 33; `ls reports/round-34/craft` → absent; `find reports/round-34 -type f` ×4
- `reports/round-30/craft/box1-survey.py:5,6,8,10`; `reports/round-30/craft/box1-landed-survey.json:4-6`; `reports/round-30/craft/review-D29-box1.md:158-162`; `reports/round-30/run-validation.py:43-45,290-302,674-685,697-698`
- `reports/round-33/adj/A09-pins.md:36,38-41,55-65,67-83,85-94,103-116,118-126` (E1–E5, R1–R8, F1–F5); `reports/round-33/adj/A10-receipt.md` §1 (A09 provisional row); `reports/round-33/calib/open-items-ledger.json` (OI-04/05/06 rows)
- `reports/round-26/run-validation.py:90,96-97,1909` (blob pin + in-place filed write); `reports/round-25/audit/c31-lessons-index-audit.py:36,51,53`; `reports/round-25/audit/x45-lessons-pointer-audit.py:178-179`; `reports/round-27/audit/x57-lessons-audit.py:563-565`
- `reports/round-32/final-dossier.md:46,133`; `reports/round-31/validation.json:1026`; `reports/round-32/validation.json:1000`; `reports/round-30/validation.json:449`; `corpus/lessons/round-31.md:46`; `corpus/lessons/round-32.md:7,33,41,55,57,58`; `corpus/lessons/round-30.md:11,172`
- `reports/round-34/depth/D11-preservation.md:107-170` (preservation fingerprint `1713e725…`, 1909 files)
- **second-phase commands (2026-10-19 ~07:1xZ), same env:** `sha256sum reports/round-30/craft/box1-survey.py` → `d923ae0fcd544513122851b55389111b3195528f8e3a4c8fb69703072132cf89`; python replay of C07's §7 comparator (`reports/round-34/calib/C07-verify-survey.md:214-235`) against `calib/C02-receipt-json.md` → `mine 28 C02 28`, `missing/extra []`, `mismatches: 0`, equal `skill_sha256`; `grep -n ':456-458\|:522\|:534\|:535\|:536\|:294' corpus/lessons/round-31.md` → line 46 carries all six tokens; `grep -n ':715\|:713-715\|:294\|:264' corpus/lessons/README.md` → `:242`,`:244`,`:245`; `grep -n 'SKILL\.md:[0-9]\|`:715`\|:713-715\|:660' corpus/lessons/round-32.md` → `:7,:33,:34,:41,:55,:57,:58`; `find reports/round-34 -type f` (×3, census in §8.1)
- **folded fragments:** `reports/round-34/calib/C01-survey-run.md`; `calib/C02-receipt-json.md:29,45,51` (durable JSON, `survey_script_sha256 d923ae0f…`, `measured_at_utc 2026-10-19T07:10:37Z`); `calib/C03-anchor-reissue.md:21-54,56-124,135-148,201-233`; `calib/C04-byte-check.md:22`; `calib/C05-receipt.md:112-163`; `calib/C06-scribe.md:44-63,101-136`; `calib/C07-verify-survey.md:16-27,40-56,63-78,80-171,173-205,242-249`; `calib/C08-verify-reissue.md:18-56,96-165`; `calib/C09-final-receipt.md:113-136,182-240,254-265,292-311,313-321,350-372`; `scout/K04-anchor-census.md:80-120,122-160,227-252`
- `reports/round-30/run-validation.py:290-303` (doc set = `reports/round-30/**.md` only), `:674-685` (box report classification), `:697-698` (the leg's failure text), `:43-45` (DATE_RE/CMD_RE)
