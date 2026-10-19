- Seat: S01 | scribe | claim C | date 2026-10-19 | baseline 4a7aede

# S01 — final claim-C (coverage) receipt, post-review fold

Mission (`reports/round-35/targets.json`, seat `S01`): "Final coverage receipt
post-review." Out path: `reports/round-35/scribe/S01-c-receipt.md`.

Every number below was measured by this seat in its own window (2026-10-19,
lane HEAD `4a7aede22cd8395b01ce6dd9f46bcae364ca24e4`, `export
TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, repo root). No
`reports/round-*/run-validation.py` was executed (F-C13-1). No file outside
`reports/round-35/` was written by this seat. `git status --porcelain` at the
cut → `?? reports/round-35/` only (1 entry), i.e. the tracked tree is
byte-clean.

**Post-review status of this receipt.** The adversarial reviews (R01/R02/R03),
the third auditor (C17), the honesty critic (X04) and the coverage verifiers
(C13/C14) are peers in the same 64-seat batch and their fragments were **not on
disk** when this seat cut (`find reports/round-35 -type f` → `claims.json`,
`targets.json`, `telemetry/*` only). §7 carries the post-review fold slots this
receipt owes them; the `## Owed` section records the exact owed paths. Four
claim-C peer fragments landed while this receipt was being written and **are
folded** — `cov/C11-readme-delta.md`, `cov/C15-receipt.md`, `cov/C12-audit-runbook.md`
and `cov/C02-entry-2.md`; §7.1 records the reconciliation. Everything in §1–§6
is this seat's own independent measurement and does not depend on any peer
fragment.

## 1. Claim under receipt

`reports/round-35/claims.json:21-35` — claim **C** (axis: **coverage**):
"Expand the two thinnest knowledge partitions with ten new sourced entries: +6
culture-material (18 -> 24) and +4 myth-symbol (19 -> 23), each entry
gap-named, frontmatter-complete (source / verified-at / recheck / scope),
decision-record carrying, and source-resolving; corpus README index reconciled
to the new counts."

Thresholds (`reports/round-35/claims.json:35`): "10/10 new entries audited
clean (two independent auditors); README counts == live census; inventory
total 211."

`after_required` (`:29`): "culture-material 24, myth-symbol 23, total 211;
every new entry passes the entry audit (frontmatter 4/4 or documented 3/4
class, source pointers resolve, decision record present, gap named in-file);
corpus/README.md partition counts and index rows reconciled by the counting
command; zero fabricated sources (every citation resolves or is marked
to-verify in-file)."

## 2. Before state — re-measured at HEAD by this seat

Counting command 1 (`reports/round-35/claims.json:31`), verbatim, repo root:

```
$ for p in linguistics myth-symbol culture-material synthesis verification civilizations; do ls corpus/knowledge/$p/*.md | wc -l; done
21
19
18
29
20
94
$ ls corpus/knowledge/*/*.md | wc -l
201
$ find corpus/knowledge -name '*.md' | wc -l
201
```

Counting command 2 (`reports/round-35/claims.json:32`):

```
$ python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge
{"schema": "kotodama-source-audit-inventory/1", ..., "totals": {"files": 201,
 "files_with_any_mark": 147, "files_with_marker": 135, "lines": 36395,
 "raw_lines": 717, "raw_occurrences": 731, "marker_occurrences": 655, ...}}
exit=0
```

`totals.files 201`; the per-file array carries exactly 201 `files[]` rows.
(The tool's JSON has no `directory_totals` key — the 21/19/18/29/20/94 vector
is the plain `ls` count above, which the README footer names as its
cross-check. `grep -c` of the tool's own keys: `dir_totals` → absent.)

Both readings reproduce the declared `before` (`claims.json:26`): "linguistics
21 / myth-symbol 19 / culture-material 18 / synthesis 29 / verification 20 /
civilizations 94 = 201 files". **Before confirmed, two methods, 201/201.**

### 2.1 README baseline pins (for the integrator's edit)

```
$ sha256sum corpus/README.md
053966a2147e5e71675b290d12bd4e523b73b31c764513ccb26a672bed37d57c  corpus/README.md
$ git hash-object corpus/README.md
ff8d779f58f95fb5c96710a9d47d692e5a5472d4
$ git rev-parse HEAD:corpus/README.md
ff8d779f58f95fb5c96710a9d47d692e5a5472d4
$ wc -l corpus/README.md
493 corpus/README.md
```

The working-tree blob equals the HEAD blob, so the integrator's edit is
checkable against `ff8d779f…` / `053966a2…` as the pre-edit reading.

### 2.2 README index state at the cut — clean 6/6

```
$ python3 -B reports/round-19/audit/coverage-audit.py
linguistics      clean declared=21 rows=21 disk=21 missing=0 ghosts=0
myth-symbol      clean declared=19 rows=19 disk=19 missing=0 ghosts=0
culture-material clean declared=18 rows=18 disk=18 missing=0 ghosts=0
synthesis        clean declared=29 rows=29 disk=29 missing=0 ghosts=0
verification     clean declared=20 rows=20 disk=20 missing=0 ghosts=0
civilizations    clean declared=94 rows=94 disk=94 missing=0 ghosts=0
TOTAL rows=201 disk=201 clean=6/6
exit=0
```

Independently corroborated by the round-28 entry audit's index leg
(`python3 -B reports/round-28/audit/entry-audit.py --all` → `indexed 201; index
clear 201; index failing 0 []`). The README is **not** in the r7 freeze
read-set (§5), so this edit is free to land.

## 3. After state required — the exact deltas

The integrator applies `cov/C11-readme-delta.md`; this table is the receipt's
acceptance target. Section headers and the totals line are the only README
lines that must move for claim C (plus one new `revision:` block per the
file's own append-only revision convention, `corpus/README.md:3-115`).

| README site | line at cut | before | after required |
|---|---|---|---|
| `## culture-material/ (18)` | `corpus/README.md:169` | `(18)`, 18 rows (`:171-188`) | `(24)`, 24 rows — +6 rows in filename order |
| `## myth-symbol/ (19)` | `corpus/README.md:147` | `(19)`, 19 rows (`:149-167`) | `(23)`, 23 rows — +4 rows in filename order |
| totals line | `corpus/README.md:469` | `Total knowledge entries: 201.` | `Total knowledge entries: 211.` |
| counts footer | `corpus/README.md:473` | `(total 201 files; directory totals 21/19/18/29/20/94)` | `(total 211 files; directory totals 21/23/24/29/20/94)` |
| revision block | top of file (`:3`) | `revision: 1.9 …` | new `revision: 2.0 …` block above it; `1.9` stays as the dated reading it was |

Vector order is linguistics / myth-symbol / culture-material / synthesis /
verification / civilizations, read from the revision-1.9 arithmetic
(`corpus/README.md:8` moves `20/19/18/29/20/94 → 21/19/18/29/20/94` for a
linguistics +1). Unchanged by claim C: linguistics 21, synthesis 29,
verification 20, civilizations 94.

**Post-edit acceptance command set** (all three must reproduce):

```
$ python3 -B reports/round-19/audit/coverage-audit.py
TOTAL rows=211 disk=211 clean=6/6            # expect; exit 0
$ for p in linguistics myth-symbol culture-material synthesis verification civilizations; do ls corpus/knowledge/$p/*.md | wc -l; done
21 23 24 29 20 94
$ python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge   # totals.files 211
```

The instrument's selftest is green at the cut, so the 6/6 reading is not a
vacuous pass: `python3 -B reports/round-19/audit/coverage-audit.py --selftest`
→ `PASS parse: two sections` / `PASS parse: declared count 2` / `PASS parse:
rows ['a.md','b.md']` / `PASS parse: ignores non-rows`, exit 0 (4/4).

## 4. Entry-audit instrument contract — the leg the runbook must name

**Finding (this seat's own measurement, load-bearing for C12/C13/C14/C17):**
the round-19 instrument is *not* the one to run. Measured on two live exemplars:

```
$ python3 -B reports/round-19/audit/entry-audit.py \
    corpus/knowledge/myth-symbol/plant-symbolism.md \
    corpus/knowledge/culture-material/textile-technology.md
FAIL corpus/knowledge/culture-material/textile-technology.md src=0/0 couples=11 unresolved=['language-contact.md'] gap=False dec=False
FAIL corpus/knowledge/myth-symbol/plant-symbolism.md src=0/0 couples=17 unresolved=[] gap=True dec=True
TOTAL 0/2 clear the bar
exit=2
```

The `src=0/0` reading is a parser artifact, not an entry defect: the round-19
parser collects source bullets only when they are nested two-space bullets
under `- sources:` (`reports/round-19/audit/entry-audit.py:67`, `if line.startswith("  - ")`,
inside `source_locators` at `:49`), while these entries carry a single-line
`- sources:` block. The `unresolved=['language-contact.md']` row is likewise a
shorthand miss — `textile-technology.md` writes a bare filename inside its
couples list, which the resolver tries only against three fixed bases
(`reports/round-19/audit/entry-audit.py:74-94`).

**The current-generation instrument is `reports/round-28/audit/entry-audit.py`**
— it imports the round-27 core verbatim and adds the index-coupling leg
(`reports/round-28/audit/entry-audit.py:2-42`). Measured at the cut:

```
$ python3 -B reports/round-28/audit/entry-audit.py --selftest
PASS core imports round 27's audited instrument
PASS index leg: a correct row is clean ...
PASS index leg: a drifted row topic is flagged ...
PASS index leg: a wrong partition is flagged ...
PASS index leg: an unindexed entry is flagged ...
PASS index leg: a duplicate row is flagged ...
PASS index leg: every entry is indexed cleanly []
PASS index leg: every disk entry audited and rows == files entries=201 readme_rows=201
PASS inherited bar runs on a live entry {"unresolved": []}
selftest: 11/11 checks passed
exit=0

$ python3 -B reports/round-28/audit/entry-audit.py \
    corpus/knowledge/myth-symbol/plant-symbolism.md \
    corpus/knowledge/culture-material/textile-technology.md
corpus/knowledge/culture-material/textile-technology.md    bar=False filler=True  src=1/1 refs_unres=0 digests_bad=0 couples_unres=0 index=ok
corpus/knowledge/myth-symbol/plant-symbolism.md            bar=True  filler=False src=1/1 refs_unres=0 digests_bad=0 couples_unres=0 index=ok
audited 2; bar clear 1; bar failing 1 [...]
indexed 2; index clear 2; index failing 0 []
exit=0
```

The `src=1/1` / `couples_unres=0` readings on the same two files show the
format artifact is fixed in this generation.

**S01-F1 (named finding — owner: the instrument's authoring seat; filed, not
absorbed; now live).** The summary line `selftest: 11/11 checks passed` is
**not** a reading. The tool prints exactly **9** `PASS` controls, and the string
is hardcoded at `reports/round-28/audit/entry-audit.py:221`
(`print("selftest: %s" % ("11/11 checks passed" if passed else "FAILED"))`),
while the selftest body contains 9 `check()` calls (`:149`, `:156`, `:160`,
`:166`, `:172`, `:178`, `:187`, `:193`, `:199`). Measured: `… --selftest 2>&1 |
grep -c '^PASS'` → **9**. All nine execute and pass, so the instrument's verdict
is sound; the **count is overstated by 2** and must not be quoted as 11/11 in
the round-35 runbook or validator. This is the lane's own
`corpus/knowledge/verification/verification-independence-anti-circularity.md`
"green-by-construction self-test" mode: a count asserted in a summary string
rather than read off the executed controls.

**The defect has already propagated into a peer fragment.** `review/R03-c-review.md:138`
and `:251` both report the instrument's selftest as "**11/11 checks passed**" —
R03 read the summary string, as this seat first did. R03's *other* readings on
the same instrument (its docstring semantics at `:143`, the r19 parser defect at
`:145-147`, the `- scope:` 0/201 census at `:162-165`) all reproduce and agree
with §4 and §7.1; only the control count is wrong. **The round-35 runbook,
validator and any receipt must cite 9, or cite the count they measured
themselves.**

**Contrast — the sibling instrument is accurate, and it is the same authoring
round.** `reports/round-28/readme/sweep.py:419` hardcodes the same pattern
(`print("selftest: %s" % ("12/12 checks passed" if passed else "FAILED"))`), but
that instrument prints exactly **12** `PASS` control lines (`… --selftest 2>&1 |
grep -c '^PASS'` → 12). So the hardcoding is a shared style, and the *only*
misreported count measured by this seat is the entry audit's. The r19 instrument
carries the matching property in the other direction (8 `check()` calls and no
summary line — `… --selftest 2>&1 | grep -c '^PASS'` → 8). Rule for the round:
**no control count is taken from a summary string; the count is the number of
executed `PASS` lines.**

**The `--new` leg is the round-35 admission gate.** The tool's own docstring
fixes its semantics: the bar "is an **admission rule for new entries**, not a
retroactive verdict … a `--new` entry must clear the bar unconditionally"
(`reports/round-28/audit/entry-audit.py:20-26`). Negative control run by this
seat — a legacy entry named as `--new` must fail:

```
$ python3 -B reports/round-28/audit/entry-audit.py --new corpus/knowledge/culture-material/textile-technology.md
... (full corpus audit follows; the --new row is the last line) ...
new corpus/knowledge/culture-material/textile-technology.md bar=False filler=True src=1/1 index=[]
exit=1
```

Exit 1 is the required behaviour, so the gate can fail. Corpus-wide reading at
the cut, for the record: `audited 201; bar clear 17; bar failing 184`;
`indexed 201; index clear 201; index failing 0`. **17/201 is the legacy split,
not a defect count** — the docstring records the same split at round 27.

**Required round-35 invocation** (the integrator/C12 should name exactly this):

```
python3 -B reports/round-28/audit/entry-audit.py \
  --new corpus/knowledge/culture-material/<e1>.md ... --new corpus/knowledge/myth-symbol/<e10>.md
# expect: each `new … bar=True`, `index=[]`, exit 0
```

Note the CLI quirk measured above: `--new` does not restrict the audit set, so
the run also prints the whole corpus; the verdict to read is the trailing
`new …` line per named entry and the exit code.

The second, independent per-entry leg is the shipped gate
(`reports/round-35/claims.json:32`'s inventory is the third):

```
$ python3 -B tools/gates/provenance-audit.py corpus/knowledge/myth-symbol/plant-symbolism.md corpus/knowledge/culture-material/textile-technology.md
INFO to-verify-count: corpus/knowledge/myth-symbol/plant-symbolism.md: 7 mark(s) on 7 line(s)
INFO to-verify-count: corpus/knowledge/culture-material/textile-technology.md: 0 mark(s) on 0 line(s)
INFO scan: files=2 marks=7 mark-lines=7 findings=0 blocked=0
exit=0
```

`findings=0` on both; the `to-verify-count` line is an INFO observation, not a
finding (`tools/gates/provenance-audit.py:20-27`).

### 4.1 Entry-shape contract, read from the exemplars

From `corpus/knowledge/myth-symbol/direction-symbolism.md:1-15`,
`corpus/knowledge/myth-symbol/plant-symbolism.md:1-9` and
`corpus/knowledge/culture-material/textile-technology.md:1-6`, the corpus entry
head is: H1 title; `- topic:` (one long line, byte-copied into the README row);
`- sources:` (nested bullets with locators); `- couples:` (backticked paths);
`- source:` (single-line roll-up); `- verified-at:` (dated pass + what was and
was not re-retrieved); `- recheck:` (the trigger that forces re-verification).
`plant-symbolism.md:3` adds `- gap:` as its first field — the gap-named form
claim C requires. `corpus/QUALITY.md:3-20` is the admission bar: provenance
(claims 1), calibration (2), coupling (3), usability (4), canon hygiene (5).

## 5. Freeze / cross-claim finding — claim C cannot move the r7 pins

`reports/round-34/handoff/declared-in-r7/expected.json` pins a **58-file read
set** (`"inputs"`, 58 keys). Partitioned by path prefix:

| prefix | members |
|---|---|
| `corpus/knowledge` | **1** |
| `corpus/lessons` | 4 |
| `examples/culture-d2` | 6 |
| `examples/culture-d3` | 8 |
| `examples/culture-d4` | 18 |
| `reports/*` | 9 |
| `tools/` + `tools/gates/` + `tools/harness/` | 12 |

The single `corpus/knowledge` member is
`corpus/knowledge/synthesis/worldbible-integration-contract.md`
@`sha256:5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069`
(`reports/round-34/handoff/declared-in-r7/packet.md:39`, row `A-01`).

**Zero read-set members live under `corpus/knowledge/culture-material/` or
`corpus/knowledge/myth-symbol/`** (filter over all 58 keys → `NONE`).
Therefore claim C's ten new entries, all in those two partitions, **cannot
drift the declared-in-r7 read set**; a re-freeze would see no new-entry drift.
Corollary measured the same way: `tools/exercise-handoff-e2e.py` is **not** a
read-set member either (the 12 `tools/` members are the assemblers,
`d2-typed-labels.py`, `check-evidence-coupling.py`, three gates and two
harness modules), so the claim-O renderer hardening also does not move read-set
digests. This is the receipt's answer to the X00/R08 cross-claim question, with
the member list as evidence; the freeze's own bytes stay pinned
(`freeze.txt` → `packet_sha256: 45f57132…`, `twin_sha256: 0e229138…`).

## 6. Preservation leg

```
$ git status --porcelain
?? reports/round-35/
```

One untracked entry, the round's own directory. No tracked file was modified
by this seat; nothing under `reports/round-1..34/**`, `corpus/lessons/*.md`,
`tools/gates/frozen/**` or `.ufo/**` was touched. `corpus/README.md` and
`corpus/knowledge/**` are untouched at the cut (blob equal to HEAD, §2.1).

## 7. Post-review fold slots (owed to the review seats)

| slot | source | state at this cut |
|---|---|---|
| R01 entries-1-5 adversarial verdicts | `review/R01-c-review.md` | **owed** — fragment absent |
| R02 entries-6-10 adversarial verdicts | `review/R02-c-review.md` | **owed** — fragment absent |
| R03 README-delta + runbook adequacy | `review/R03-c-review.md` | **LANDED, FOLDED** (§7.1) — agrees on the instrument, the parser defect, the `scope` census and the after-state; repeats the `11/11` count (S01-F1) |
| C13 audit 1-5 / C14 audit 6-10 / C17 sample | `cov/C13-audit-1-5.md`, `cov/C14-audit-6-10.md`, `cov/C17-audit-sample.md` | C17 **LANDED, FOLDED** (§7.1) — pre-registered, not performed (`:330-331`); C14 on disk, unaudited by this seat; C13 **owed** |
| X04 fabrication / to-verify census | `cross/X04-honesty.md` | **owed** — fragment absent |
| the ten entry drafts themselves | `cov/C01..C10-*.md` | **9 of 10 owed** — only `cov/C02-entry-2.md` is on disk; §3 gives the README target, §4 the audit gate, §4.1 the shape contract, §7.1 C02's fold |
| `reports/round-35/run-validation.py` | integrator | **owed** — file does not exist at the cut (`find reports/round-35 -type f`); it is a filed runner and was not executed (F-C13-1) |

Fold rule for whoever completes this receipt: a slot resolves only from the
named fragment's own text, never by inference from this seat's measurements.
The §2/§3 numbers are this seat's independent reading and stand on their own.

### 7.1 Landed-fragment reconciliation (folded after this seat's first cut)

Six claim-C peer fragments landed while this receipt was being written. Each
was read by this seat, and the load-bearing numbers were **re-measured
independently** before folding:
| fragment | its numbers | this receipt's independent check | verdict |
|---|---|---|---|
| `cov/C11-readme-delta.md` (README delta draft) | myth-symbol header `:147` `(19)`→`(23)`; culture-material header `:169` `(18)`→`(24)`; totals line `Total knowledge entries: 211.`; footer `(total 211 files; directory totals 21/23/24/29/20/94)`; rows 149–167 / 171–188; new `revision: 2.0` block | §3 table, line for line; C11's own negative control at `:382-389` (planted `missing_from_index 1 ['culture-material/bead-currency-systems.md']`) shows its 211/211 sweep can fail | **AGREE** — apply as §3 specifies |
| `cov/C15-receipt.md` (coverage receipt draft) | before census 21/19/18/29/20/94 = 201; HEAD `4a7aede…`; `claims.json:24` claim, `:26-27` before, `:29` after_required, `:31-33` commands, `:35` thresholds | §2 census; §1 citations — the `claims.json` line numbers re-read and correct | **AGREE** — this receipt supersedes C15 as the post-review fold and adds §4/§5 |
| `cov/C12-audit-runbook.md` (audit instrument, schema `kotodama-entry-audit-runbook/2`) | `- scope:` → **0** of 201; `- couples:` → 201; `- sources:` → 201; `- source:` → 134; `- verified-at:` → 201; `- recheck:` → 201 (`:55`) | re-measured by this seat, identical for all six; this seat adds `- gap:` → 2 | **AGREE** — C12's central reading holds: the claim's `scope` leg cannot be read literally |
| `cov/C02-entry-2.md` (culture-material entry 2 draft) | entry head carries `- gap:` first, then topic / sources (nested bullets with `path:line` anchors) / couples / source / verified-at / recheck; proposed path `corpus/knowledge/culture-material/agrarian-field-system-lexicon.md` | §4.1 shape contract — the head matches the exemplar field set and order | **AGREE on shape**; scholarship unaudited here (C13/C14/C17/R01/R02) |
| `review/R03-c-review.md` (README-delta + runbook adequacy review) | instrument choice = `reports/round-28/audit/entry-audit.py` (`:137`); r19 parser defect (`:145-147`); `- scope:` **0/201** (`:162-165`); `--new` legacy → exit 1 (`:143`); README after-state `myth-symbol 19→23, culture-material 18→24, total 211, vector 21/23/24/29/20/94` (`:142`) | §4 instrument contract; §7.1 C12 row; §3 table | **AGREE on every reading except one** — R03 repeats the instrument's `11/11` summary string at `:138` and `:251`, which is the S01-F1 defect (§4); the correct executed-control count is **9** |
| `cov/C17-audit-sample.md` (third auditor, pre-registered) | expected after-state `myth-symbol 19→23, culture-material 18→24, total 211, vector 21/23/24/29/20/94` (`:142`); live README census `rows == files 21/19/18/29/20/94`, topic byte-equal 201/201 (`:138`); README digest `053966a2…` (`:141`) | §3 table; §2.1 digest; §2.2 index state | **AGREE** — and C17 states its own pass is **pre-registered, not performed** (`:330-331`): the three sampled drafts and the delta do not exist at its stamp, so no `10/10` reading exists yet |

Two review-side defects filed by R03 against C11 are recorded here rather than
re-litigated: **R03-C-1** (C11 cites `reports/round-28/readme/sweep.py:21` for a
regex that lives elsewhere) and **R03-C-2** (C11's "no other live document
carries a stale count" claim is too broad — `corpus/lessons/round-19.md` and
`corpus/lessons/round-28.md` carry dated stale readings). Both are
citation-precision defects in C11, **not** errors in the delta numbers, which
is why the §7.1 C11 row still reads AGREE. Owner for both: C11's authoring seat
or the integrator.

**Two findings this fold raises, filed not absorbed:**

- **S01-F2 (instrument duplication; owner: the integrator).** C12 drafted a
  *new* auditor (`.scratch/c12/entry-audit-runbook.py`, 3 positive + 4 negative
  controls per `cov/C12-audit-runbook.md:801-805`) and never names the existing
  audited instrument — `grep -c "round-28" cov/C12-audit-runbook.md` → **0**.
  Two independent readers of the same bytes is exactly the situation the lane's
  own `corpus/knowledge/verification/two-reader-interop-agreement.md` requires
  be *compared, not assumed*. The round therefore owes either an interop
  comparison of C12's runbook against
  `reports/round-28/audit/entry-audit.py` (the instrument with the index leg
  and the `--new` admission gate, §4), or a recorded reason for the new
  instrument. Neither choice is this seat's to make.
- **S01-F3 (reading named, not a defect).** Claim C's `after_required`
  (`claims.json:29`) names four frontmatter legs including `scope`, and no live
  entry carries a literal `- scope:` field — measured **0/201** by this seat and
  by C12. The scope leg must therefore be read through `- couples:` (C12's
  §1a reading `R35-4F-1`), or the claim's own phrasing reports 0/10 on
  compliant drafts. This is a *reading*, in the sense of
  `corpus/knowledge/verification/header-conformance-readings.md`, and the
  round-35 validator must name which one it implements.

C11 additionally records a read-only sweep with its own negative control
(`cov/C11-readme-delta.md:382-389`: planted `missing_from_index 1
['culture-material/bead-currency-systems.md']`), so its 211/211 reading is a
measured leg, not a green-by-construction one. None of the six fragments is
edited by this seat; each keeps its own bytes.

## 8. Receipt summary

| threshold (`claims.json:35`) | state at this seat's cut | evidence |
|---|---|---|
| README counts == live census | **BEFORE MEASURED GREEN** (6/6 clean, rows 201 == disk 201); after-state is the §3 target | §2.2 |
| inventory total 211 | **BEFORE MEASURED 201**; after-state owed to the integrator's landing | §2 |
| 10/10 new entries audited clean (two independent auditors) | **OWED** — no audit reading exists: C02/C03/C05/C06 are on disk (only C02 folded here), C17 states its own pass is pre-registered not performed, and C13 is absent. Instrument contract supplied in §4, with **S01-F1** (control-count correction), **S01-F2** (two auditors exist, no interop comparison filed) and **S01-F3** (the `scope` leg needs a named reading) all filed in §4/§7.1 | §4, §7.1 |
| zero fabricated sources | **OWED** — X04's and R01/R02's census; §4 names the gate that reads it | §7 |
| r7 freeze bytes preserved | **MEASURED GREEN** — no new entry can enter the read set | §5 |
| filed rounds 1-34 unedited | **MEASURED GREEN** — `git status` clean apart from `reports/round-35/` | §6 |

## Owed

- `reports/round-35/scribe/S01-c-receipt.md` post-review fold (§7): the R01,
  R02, R03, C13, C14, C17, X04 verdict rows and the ten entry drafts' audit
  results cannot be written from this seat — those fragments were not on disk
  at the cut. The integrator (or a post-batch S01 pass) folds them in using the
  §4 instrument contract and the §3 acceptance numbers. **Already folded** (read
  and re-measured, §7.1): `cov/C11-readme-delta.md`, `cov/C15-receipt.md`,
  `cov/C12-audit-runbook.md`, `cov/C02-entry-2.md`, `review/R03-c-review.md`,
  `cov/C17-audit-sample.md`. Still owed at this cut: `cov/C01`, `cov/C03`–`C10`
  (six of ten drafts — C02, C03, C05, C06 are on disk but only C02 is folded
  here), `cov/C13-audit-1-5.md`, `review/R01-c-review.md`,
  `review/R02-c-review.md`, `cross/X04-honesty.md`. On disk but **not** read or
  folded by this seat: `cov/C14-audit-6-10.md`, `cross/X00`–`X03`, `scout/K01`–`K03`,
  `plan/P02`, `review/R04`, `R06`–`R09` (out of this receipt's claim-C scope).
- **S01-F2** (§7.1) — the interop comparison of `cov/C12-audit-runbook.md`
  against `reports/round-28/audit/entry-audit.py`, or a recorded reason for the
  second instrument. Owner: integrator. Not absorbed here.
- **S01-F3** (§7.1) — the named reading for the claim's `scope` frontmatter leg
  in `reports/round-35/run-validation.py`. Owner: the validator author.
- `reports/round-35/run-validation.py` — the claims.json counting-command leg
  (`claims.json:33`) does not exist at the cut and was not executed.

## Citations

Files read or measured:
- `reports/round-35/claims.json:21-35`, `:31-33`
- `reports/round-35/targets.json` (seat `S01`; `shared_rules`)
- `REGIMEN.md:25-58`
- `corpus/README.md:3-112`, `:123`, `:147`, `:169`, `:190`, `:222`, `:245`,
  `:469`, `:471-473`, `:493` (sha256 `053966a2…`, blob `ff8d779f…`)
- `corpus/QUALITY.md:3-20`
- `corpus/knowledge/myth-symbol/plant-symbolism.md:1-9`
- `corpus/knowledge/myth-symbol/direction-symbolism.md:1-15`
- `corpus/knowledge/culture-material/textile-technology.md:1-6`
- `reports/round-34/handoff/declared-in-r7/expected.json` (`inputs`, 58 keys)
- `reports/round-34/handoff/declared-in-r7/packet.md:39`
- `reports/round-34/handoff/declared-in-r7/freeze.txt`
- `reports/round-34/scribe/S03-c-receipt.md:1-31` (receipt convention)
- `reports/round-19/audit/coverage-audit.py:1-40`, `:125-170`
- `reports/round-19/audit/entry-audit.py:1-20`, `:49-130` (`source_locators`
  `:49`, nested-bullet check `:67`, `couples_targets` `:74`)
- `reports/round-28/audit/entry-audit.py:1-60`, `:205-290`, `:221` (S01-F1
  hardcoded count), `:149`–`:199` (the 9 `check()` calls)
- `reports/round-28/readme/sweep.py:239-420` (`selftest`), `:419` (the
  `12/12` string that its 12 executed `PASS` lines *do* support)
- `corpus/knowledge/verification/verification-independence-anti-circularity.md`
  (cited by name for the S01-F1 mode; its own bytes were not opened by this
  seat — the mode name is quoted from its README row,
  `corpus/README.md:242`)
- `corpus/knowledge/verification/two-reader-interop-agreement.md` (same
  convention for the S01-F2 mode — named from its README row,
  `corpus/README.md:241`; bytes not opened by this seat)
- `corpus/knowledge/verification/header-conformance-readings.md` (same
  convention for the S01-F3 reading discipline — named from its README row,
  `corpus/README.md:230`; bytes not opened by this seat)
- `tools/gates/provenance-audit.py:1-27`

Peer fragments read and reconciled (§7.1):
- `reports/round-35/cov/C11-readme-delta.md:33`, `:49-52`, `:77-143`,
  `:165-176`, `:366-370`, `:382-389`
- `reports/round-35/cov/C15-receipt.md:1-60`
- `reports/round-35/cov/C12-audit-runbook.md:1-60`, `:55`, `:801-805`
- `reports/round-35/cov/C02-entry-2.md:1-40`
- `reports/round-35/review/R03-c-review.md:17-18`, `:63-64`, `:70-72`,
  `:75-90`, `:102`, `:112-122`, `:137-147`, `:153-165`, `:186-207`, `:232-251`
- `reports/round-35/cov/C17-audit-sample.md:11-12`, `:20-27`, `:42-46`,
  `:109-127`, `:138-145`, `:205-220`, `:330-331`

Commands run (repo root, `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`):
- `git rev-parse HEAD`; `git log -1 --format='%H %ci %s'` → `4a7aede…`
- `for p in linguistics myth-symbol culture-material synthesis verification civilizations; do ls corpus/knowledge/$p/*.md | wc -l; done` → 21/19/18/29/20/94
- `ls corpus/knowledge/*/*.md | wc -l`; `find corpus/knowledge -name '*.md' | wc -l` → 201 / 201
- `python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge` → `totals.files 201`, exit 0
- `sha256sum corpus/README.md`; `git hash-object corpus/README.md`; `git rev-parse HEAD:corpus/README.md`; `wc -l corpus/README.md` → `053966a2…` / `ff8d779f…` / `ff8d779f…` / 493
- `python3 -B reports/round-19/audit/coverage-audit.py` → `TOTAL rows=201 disk=201 clean=6/6`, exit 0
- `python3 -B reports/round-19/audit/coverage-audit.py --selftest` → 4/4 PASS, exit 0
- `python3 -B reports/round-19/audit/entry-audit.py --selftest` → 8/8 PASS, exit 0
- `python3 -B reports/round-19/audit/entry-audit.py corpus/knowledge/myth-symbol/plant-symbolism.md corpus/knowledge/culture-material/textile-technology.md` → `TOTAL 0/2 clear the bar`, exit 2
- `python3 -B reports/round-28/audit/entry-audit.py --selftest` → prints 9 `PASS` controls (`grep -c '^PASS'` → 9) and the summary string `selftest: 11/11 checks passed`, exit 0 (S01-F1: the count is the tool's hardcoded prose, not a reading)
- `python3 -B reports/round-28/audit/entry-audit.py corpus/knowledge/myth-symbol/plant-symbolism.md corpus/knowledge/culture-material/textile-technology.md` → `bar=True`/`bar=False`, `index clear 2`, exit 0
- `python3 -B reports/round-28/audit/entry-audit.py --new corpus/knowledge/culture-material/textile-technology.md` → `new … bar=False filler=True src=1/1 index=[]`, exit 1 (negative control); corpus-wide `audited 201; bar clear 17; index clear 201`
- `python3 -B tools/gates/provenance-audit.py corpus/knowledge/myth-symbol/plant-symbolism.md corpus/knowledge/culture-material/textile-technology.md` → `findings=0 blocked=0`, exit 0
- `ls corpus/lessons/*.md | wc -l` → 33
- `git status --porcelain` → `?? reports/round-35/`
- `find reports/round-35 -type f` → `claims.json`, `targets.json`, `telemetry/{availability-attempt-1,availability-attempt-2,availability-attempt-3,dispatch-declared}.json`
