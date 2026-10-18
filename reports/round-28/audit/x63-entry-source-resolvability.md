# X63 — entry source-resolvability audit (round 28)

- round 28 (operator: loop 3 of 3, build 4 of 4 — the last build round; 64 workers
  on `devin/deepseek-v4-1-flash-high` per `reports/round-28/claims.json`) · seat
  **X63** (SCRIBE X63 — ceiling-entry auditor, source resolvability) · owner: L2
  worker, kotodama-shokunin lane.
- assignment (verbatim): "SCRIBE X63..X64: ceiling-entry auditors."
- date: 2026-10-18. Lane root `/home/vgpnk/Projects/shokunin/kotodama-shokunin`;
  declared baseline `6c0ac4484d7ee5d15aaf190e7ad3b8817ea13ede`
  (`reports/round-28/claims.json:5`); declaration HEAD
  `69cecbc7dcf575a29f29660ecac470e05260fd86`.
- canon: NON-CANON engineering evidence. This seat audits and reports; it admits
  no claim, certifies no round, disposes no candidate.
- writes: **this file**, its instrument
  `reports/round-28/audit/x63-entry-source-resolvability.py`, and gitignored
  scratch under `.scratch/`. **No `corpus/**` byte written.** No filed
  round-8–27 artifact, tool, gate, packet or component edited. No commit, no
  push.

## 0. Verdict at a glance

| # | reading | class |
|---|---|---|
| 1 | the instrument is green on **23 planted controls** (count reported by the tool itself, not asserted), including a baseline-aware classifier exercised on a real planted git repo | measured |
| 2 | both claim-C documents audit **clean on every graded surface**: frontmatter, gap, decision record, locators, pins, amendment discipline, ceiling record | measured |
| 3 | the amendment is **append-only by construction**: 123 lines inserted, **0 deleted or rewritten**, and the baseline's 12 section headers all survive | measured |
| 4 | **four absence-sweep rows do not reproduce**, and they split into **one authoring defect and three sibling-landing rows** | **findings X63-F1…F4** |
| 5 | **two false-green defects in this instrument were found and fixed by its own controls** — a greedy pointer walk that fabricated a rewrite magnitude, and a sweep leg blind to the `\| wc -l` form and the `-i` flag | **findings X63-H1, X63-H2** |

## 1. The documents

| field | value |
|---|---|
| path | `corpus/knowledge/linguistics/register-strata-attestation.md` (amended) |
| sha256 | `645d692932edec50c2ec4dbd07cc73da37efeb368a338f2eee5aa54a798c5784` |
| bytes / lines | 64 928 / 436 |
| status | modified (` M`), settled — three 30-second reads returned this digest |
| path | `corpus/knowledge/linguistics/register-lexicon-ceilings.md` (new) |
| sha256 | `bb579d51cea0a900571e77b6690978256a607ec08f500923674738107dc1bffe` |
| bytes / lines | 34 400 / 289 |
| status | untracked (`??`), settled |

The partition moved **20 → 21**; `corpus/README.md` was reconciled to revision
**1.9** (`## linguistics/ (21)`, totals 200 → 201, footer vector
`21/19/18/29/20/94`). §5 reads that reconciliation.

## 2. The instrument

`reports/round-28/audit/x63-entry-source-resolvability.py` — read-only, stdlib
only, exit 0 clean / 1 findings / 2 could-not-evaluate.

```sh
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
python3 -B reports/round-28/audit/x63-entry-source-resolvability.py --selftest --scratch "$TMPDIR/x63r28"
python3 -B reports/round-28/audit/x63-entry-source-resolvability.py --offline --json \
    --baseline 6c0ac4484d7ee5d15aaf190e7ad3b8817ea13ede
```

| id | surface | green means |
|---|---|---|
| X63-A | frontmatter | every lane-bar field (`topic`, `sources`, `verified-at`, `recheck`, `couples`) present and non-empty |
| X63-B | gap | the entry names the gap it fills, field form or heading form |
| X63-C | decision record | a `## … decision record …` heading exists |
| X63-D | locators | every repo-path locator resolves on disk |
| X63-E | pins | every `sha256` bound to a named repo path re-derives |
| X63-F | sweeps | every quoted absence sweep reproduces, **classified** when it does not |
| X63-G | amendment | an amended entry is **append/insert only** — no baseline line deleted or rewritten |
| X63-H | ceiling | the ceiling is recorded **as a design constraint** and cites the round-27 measurement |

The two round-28 legs (**G**, **H**) exist because claim C is an *amendment plus
a new entry*, not a single landing: the lane's rule is that a correction is a NEW
section or a new file, never an in-place rewrite, and the ceiling must be recorded
as a design constraint rather than as a defect to repair.

**Scope of the claim.** This is a **resolvability** instrument, not a merits
instrument. A locator that resolves is reported resolved even when the source it
names is weak; a sweep that reproduces is reported green even when the pattern is
a poor test of the claim it backs. It never says a source is the right source,
never says a calibration is warranted, and never says the ceiling is real. A
finding is only ever "the document says X and the bytes say not-X".

## 3. Both documents, audited

```
register-lexicon-ceilings.md       bb579d51cea0a900   34400 B / 289 lines
  frontmatter missing []   gap named: yes (field)   decision record: yes   canon boundary: yes
  ceiling recorded as a constraint: yes (ceiling + constraint language + round-27 citation)
  locators: 25 resolved, 0 unresolved, 0 declared-absent   pins: 0   sweeps: 5
register-strata-attestation.md     645d692932edec50   64928 B / 436 lines
  frontmatter missing []   gap named: yes (field)   decision record: yes   canon boundary: yes
  ceiling recorded as a constraint: yes
  locators: 46 resolved, 0 unresolved, 0 declared-absent
  pins: 4 re-derived, 0 drift   sweeps: 5
findings: 4 (X63-F1..F4)
```

### 3.1 The amendment is append-only — the round-28 rule holds

The rule the round is held to is that a correction to a filed entry is a **new
section**, never an in-place rewrite. Two independent readings of the same
condition:

| reading | instrument | result |
|---|---|---|
| line-level diff (`difflib.SequenceMatcher`) | X63-G | `preserved 313 / inserted 123 / deleted_or_rewritten 0` |
| section headers at baseline vs live | `run-validation.py` C-check | baseline 12, live 13, `lost_sections []`, `prefix_preserved true` |
| `git diff --numstat` in a clone | X64-G | `added 123, deleted 0` |

The single new section is `## 13. Amendment (round 28): the register-lexicon
ceiling, re-measured, with its mechanism`, with subsections 13.1–13.5. Every one
of the baseline's 12 `##` headers survives verbatim; **no baseline line was
rewritten.** The three legs use three different mechanisms and agree, which is
what makes the reading evidence rather than a shared assumption.

### 3.2 The ceiling is recorded as a design constraint, and cites the round-27 measurement

Both documents satisfy X63-H — each names a `ceiling`, calls it a constraint or
bound, and cites `round-27`/`RL-3`. The amendment's own §13.1 states the filed
round-27 arithmetic and §13.2 records that the count does not reproduce under the
delivered gate (19/8, not 18/9), which is the honest handling of a superseded
figure: the old reading is kept and the correction is a new section beside it.

### 3.3 The four pins re-derive

`reports/round-26/register/{design,forms,rules,review}.md` are pinned at
`27d23fa67d0b…`, `06635a1c123e…`, `535cf7a981c5…`, `0082f08b6298…` and all four
re-derive byte-equal. The round-27 entry's own red pin against
`examples/culture-d4/packet.d4.yml` is **not** carried by the amendment, so this
round introduces no new stale pin on that surface. The new entry pins no digest
at all (0 pins), citing its round-27/28 peers by revision — the correct handling
of a churning surface, and the reason its pin column is empty rather than green.

### 3.4 X63-F1..F4 — four absence sweeps do not reproduce, and they are two different things

Each document opens its `- gap filled:` cell with a run of `grep -rl -i "<pat>"
corpus/knowledge/ | wc -l` → **0** sweeps. Re-run against the settled tree,
**four rows do not reproduce**:

| # | document | pattern | pre-existing hits | baseline hits | class |
|---|---|---|---|---|---|
| F1 | ceilings (new) | `lexicon ceiling` | the amended strata entry | `[]` | **sibling-landing** |
| F2 | ceilings (new) | `which semantic fields` | `sound-symbolism.md`, the strata entry | `sound-symbolism.md` | **authoring-defect** |
| F3 | strata (amended) | `attestation register\|attestation speech` | the ceilings entry | `[]` | **sibling-landing** |
| F4 | strata (amended) | `register law\|register-law` | the ceilings entry | `[]` | **sibling-landing** |

**The classification is the finding, and it is the reason the leg was extended.**
In a parallel wave a sibling seat can land a document *between* the moment an
entry is authored and the moment it is audited, so a sweep that was true when
written reads false now. That is a different object from a sweep that was false
when written, and only the second is an authoring defect. The leg re-runs the same
pattern at the declared baseline with `git grep -G` (the quoted command's own BRE
dialect), **minus the audited document itself** (the lane's sweeps say "over
`corpus/knowledge/` minus this entry"). A surviving baseline hit ⇒
`authoring-defect`; no surviving hit ⇒ `sibling-landing`.

- **F2 is a real authoring defect.** `sound-symbolism.md:106` already reads
  "assign **which semantic fields** carry ideophones", at the baseline revision
  and still live. The sweep was false when written:
  ```sh
  git grep -n -i "which semantic fields" 6c0ac4484d7ee5d15aaf190e7ad3b8817ea13ede -- corpus/knowledge/linguistics/sound-symbolism.md
  # 6c0ac448…:corpus/knowledge/linguistics/sound-symbolism.md:106:  1. **Fields** — assign which semantic fields carry ideophones …
  ```
  The repair is one line in the entry — drop the sweep, or qualify it (the entry's
  own §6 already lists the real-world analogues, so the honest form is "the phrase
  occurs once, in `sound-symbolism.md`, in the ideophone sense"). It is a **corpus
  write** and this seat does not make it; the parent owns disposition.
- **F1, F3, F4 are sibling-landing rows, not defects in the author's work.** Each
  pattern had **zero** hits at the baseline once the audited document is excluded.
  The two round-28 documents name each other (`register law` in the new entry's
  gap cell; `attestation register`/`lexicon ceiling` in the cross-citations), so
  the wave's own landing is what broke the sweeps. F3/F4 live in the *amended*
  document and are artefacts of the amendment's own §13 text plus the new sibling
  entry; F1 is the new entry's sweep broken by the *amended* sibling.

**Neither document hides the movement.** The amended entry's §13 is titled
"re-measured" and §13.2 records the superseded count; the new entry's §10 states
its limits. The rows above are the audit's reading, and a consumer should read
them as "the sweep's claim is now false on the settled tree", with the class
telling them whose landing made it false.

**Cross-tool agreement.** The sibling `reports/round-28/audit/entry-audit.py`
reports both documents clean (`bar=True … refs_unres=0 digests_bad=0
couples_unres=0 index=ok`) — it does not score the `| wc -l` sweep form, so it
sees no sweep row at all. That is a coverage difference, not a disagreement: the
two tools grade disjoint surfaces here, and the sweep leg is this seat's.

## 4. Findings in this instrument — two false-greens, found by its own controls

### X63-H1 — the amendment leg fabricated a rewrite magnitude (fixed)

The first amendment check was a **greedy pointer walk**: advance a pointer
through the baseline lines, consuming a line each time the live line equals it.
A pointer that only advances on equality desynchronises the moment a line is
rewritten — it stalls at the first changed line, and every later baseline line is
then reported as deleted. **Measured on a planted one-line rewrite of the
round-27 entry, the walk reported `deleted_or_rewritten: 311` against the true
count of 1.** The finding's *existence* was right and its *magnitude* was
fabricated. A count a consumer will read must not be produced that way.

Fixed with a line-level diff (`difflib.SequenceMatcher`), so a single rewritten
line costs exactly one deleted row. Two controls now pin the magnitude, not just
the verdict: a 43-line planted document with one rewritten line must report
`deleted_or_rewritten 1` and `preserved baseline_lines - 1`. X64's independent
`git diff --numstat` leg reported the correct 1 throughout, which is how the
defect was caught from outside the leg that had it.

### X63-H2 — the sweep leg was blind to the `| wc -l` form and the `-i` flag (fixed)

Round 27's own audit recorded the limit in writing: "the sweep leg recognises
only the `grep -rln "…" <path> → 0 files` form … Extending the leg to the `| wc -l`
form is the next improvement." The round-27 entry quotes **all five** of its
sweeps in that form, so they were scored by hand, not by any instrument — a green
sweep column that no tool had produced.

Fixed: the recogniser now accepts `grep -rl[n] [-flags] "<pat>" <path> [| wc -l]`,
and the `-i` flag is honoured (a case-insensitive sweep is re-run
case-insensitively — reading it as case-sensitive would manufacture a false green
on any sweep whose pattern only matches in another case). Measured effect on the
round-27 entry, which previously produced zero sweep rows:

```
reproduces | illocutionary
reproduces | constitutive rule
reproduces | deontic
reproduces | attestation register\|attestation speech   (now sibling-landing, see F3)
reproduces | register law\|register-law                 (now sibling-landing, see F4)
```

Three controls pin it: the piped form must parse; a matching-free piped sweep
must stay green; and a case-insensitive piped sweep that *does* match must fire
with `ignore_case: true`. The last one is the false-green guard.

### X63-H3 — the classifier itself, controlled on a real git repo

The baseline classifier is the round's most load-bearing new logic, so it is
exercised on a **real planted git repository**, not a mock: a baseline commit
carrying `PRE-EXISTING TERM`, then a sibling file added after the baseline
carrying `FRESH TERM`. The same sweep pattern is then audited twice — a pattern
matching only the pre-existing term must classify `authoring-defect`, and one
matching only the post-baseline term must classify `sibling-landing`. Without
this control the classifier would be a claim, not a check.

## 5. The corpus README, and the sibling instruments

`corpus/README.md` was reconciled to revision **1.9** (`## linguistics/ (21)`,
totals line 201, footer `21/19/18/29/20/94`). The round-28 `readme/sweep.py`
reads it clean, and — recorded here because it is a real finding this round —
revision 1.8 exists precisely because round 27's sweep **never read the counts
footer**, so it went green over a stale present-tense claim. That is the same
class as X63-H1/H2: a leg that cannot fail cannot check.

Cross-instrument state on the two documents, all green:

| instrument | reading |
|---|---|
| `reports/round-28/audit/entry-audit.py` (sibling) | `bar=True filler=False src=11/11` (new) / `src=19/19` (amended), `refs_unres=0 digests_bad=0 couples_unres=0 index=ok` |
| `reports/round-28/run-validation.py` claim C | `passed: true`, `failures: []` |
| this seat, X63-A…H | clean except the four sweep rows (§3.4) |

## 6. What this seat did not do

- It **adjudicates no claim.** Claim C's verdict belongs to the round's runner and
  auditor; this fragment is evidence.
- It **repairs nothing.** X63-F2 is a corpus write and is routed; the three
  sibling-landing rows are reported, not "fixed", because a sweep broken by a
  parallel landing is a property of the wave, not of the author.
- It **does not re-derive the ceiling arithmetic** (19/8 vs 18/9) — that is the C
  seat's measurement and D20's review surface, not this seat's.
- It **writes no corpus byte**, touches no filed round-8–27 artifact, and does not
  run the round-28 counting command (its receipt belongs to the assigned runner).

## 7. Limits

- The **new-entry bar** (gap, decision record) is the round-10/round-19 admission
  rule. Over the whole corpus it reports 172/179 rows on entries that predate the
  bar — an instrument reach, not a defect list. §3 grades only the two round-28
  documents.
- The **baseline classifier** depends on `git grep` succeeding at the declared
  revision; a git failure returns `[]` and is therefore reported as
  `sibling-landing` — the leg errs toward *not* accusing the author, and the
  receipt carries the empty `baseline_hits` list so a consumer can see the
  evidence was empty rather than absent.
- **Both sweep forms are now recognised, but only those two.** A sweep written as
  prose, or with a pipe other than `wc -l`, is not scored — the leg errs toward
  silence, so a green sweep column is "no recognised sweep failed", not "no sweep
  is false".
- URL locators are probed with a bounded HEAD request and the outcome is an
  **observation**, never a finding. §3's run used `--offline`, so no URL was
  probed; the documents carry 2 and 3 URL locators respectively.
- The corpus is a live surface and the round-28 wave wrote throughout. Every count
  binds to the digest printed beside it. Both documents settled before §3 was
  taken (three 30-second reads each, identical digests); a re-read is a new
  measurement.

---

*Receipts: `.scratch/r28-x63-entry.json` (both documents), and the background
full-corpus control `.scratch/r28-x63-full-corpus.json` (200 entries).
Fragment written 2026-10-18.*
