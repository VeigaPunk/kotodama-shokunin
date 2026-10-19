- Seat: R03 | reviewer | claim C | date 2026-10-19 | baseline 4a7aede

# R03 — third-pass review: the README delta (C11) and audit-runbook adequacy (C12)

**Mission** (`reports/round-35/targets.json`, seat `R03`): "Third pass: the README delta +
audit-runbook adequacy." Out path `reports/round-35/review/R03-c-review.md`. Shared rules read at
`reports/round-35/targets.json:5-13`; the F-C13-1 rule (`:10`) was honoured — no
`reports/round-*/run-validation.py` was executed in-tree or anywhere.

**Method and limits.** This seat is read-only over the lane; its only write is this fragment.
Every command below ran from the lane root with
`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1` at HEAD
`4a7aede22cd8395b01ce6dd9f46bcae364ca24e4` (`git status --porcelain corpus/` empty at the cut).
Dependency status at the cut: `cov/C11-readme-delta.md` **landed mid-run and was tested** (§2);
`cov/C12-audit-runbook.md` **absent** — §4 therefore files the runbook's *adequacy legs* as
measured requirements instead of a review of bytes that do not exist, and the path is owed in
`## Owed`. Instruments executed by this seat: `reports/round-28/readme/sweep.py` (live, `--selftest`,
and its `sweep()` imported read-only for synthetic-tree controls), `reports/round-28/audit/entry-audit.py`
(`--selftest`, two-file run, `--new` negative control), `tools/source-audit-inventory.py`,
C11's §3 generator (extracted verbatim to `.scratch/r03/readme-delta.py`, disposable), and
read-only censuses. No filed round byte was written; no corpus byte was written.

## 1. Verdicts

1. **C11 README delta — PASS, independently reproduced end-to-end** (§2), with two
   citation/precision defects filed as R03-C-1/R03-C-2 (neither is a byte risk) and one
   acceptance-completeness recommendation (R03-C-3).
2. **C12 audit runbook — could-not-review: absent at the cut.** The adequacy legs the runbook must
   satisfy are specified in §4, each with a measured baseline so C13/C14/C17 can run them the
   moment C12 lands; `cov/C12-audit-runbook.md` is owed.
3. **Delta control matrix measured** (§3): the five edit sites must move together, and two
   instrument blind spots are named with evidence — a stale footer **date** reads green under the
   sweep, and a missing **row** is invisible to the totals line alone (both caught only by legs
   the runbook/acceptance block must carry).

## 2. C11 tested independently (what I ran, what I saw)

Pins re-measured by this seat: `corpus/README.md` sha256
`053966a2147e5e71675b290d12bd4e523b73b31c764513ccb26a672bed37d57c`, 106 218 bytes, 493 lines —
byte-equal to C11 §0's pin (`cov/C11-readme-delta.md:11-13`). Instrument digest re-measured:
`reports/round-28/readme/sweep.py` sha256
`9b2ccac0046831fdaf48863ccd0ff6ca0fa390d044746c876e83a71c06f0cdd3` — equal to C11's
(`C11-readme-delta.md:25-26`). C11's line map (§1, `:43-58`) checked against live bytes:
`:147` `## myth-symbol/ (19)`, `:169` `## culture-material/ (18)`, `:469`
`Total knowledge entries: 201.`, `:471` date line, `:472` inventory command, `:473` footer vector,
`:475-480` superseded paragraph, `:482-493` three dated `Index rows` paragraphs — all resolve.

C11's §3 generator was extracted from its fenced block verbatim (140 lines) and run:

- **Calibration leg.** On the live tree the generator is a **no-op**: `missing_rows` total 0,
  totals before → after `Total knowledge entries: 201.` → `Total knowledge entries: 201.`, footer
  before → after identical, exit 0. (C11 §4 bullet 1, reproduced.)
- **Synthetic +10 tree, this seat's own stubs.** A copy of `corpus/knowledge` plus 10 stubs with
  **multi-line** `- topic:` heads: 6 culture-material (`aardvark-probe.md` first-in-section,
  `bead-currency-systems.md`, `custom-a.md` + `custom-b.md` as an adjacent pair sharing the
  `cuisine-food-lexicon.md` anchor, `vessel-container-lexicon-2.md`, `zzz-tail-cm.md` tail) and 4
  myth-symbol (`aardvark-myth-probe.md` first-in-section, `flood-traditions-2.md`,
  `hero-journey-variants-2.md`, `zzz-tail-ms.md` tail). `--apply` to a scratch README copy emitted
  all 10 rows with the anchors C11 §3 specifies: first-in-section → header line + 1
  (`after_line 148` / `170`, `after_row None`); the shared-anchor pair → both `after_line 176`
  (after `cuisine-food-lexicon.md`); tails → `167` / `188`; exit 0.
- **The instrument of record reads it green.** `sweep()` (imported read-only) over the applied
  README against the synthetic tree: `ok True`, **211 rows / 211 files**, `missing 0`, `ghosts 0`,
  `rewrite 0`, `drift {}`, `totals_ok True`, `footer_findings []` — C11 §4's end-to-end proof
  reproduced with this seat's own stubs, not C11's.
- **Independent order/format check** (own re-implementation, not C11's): after apply, both
  sections are filename-sorted and no row sits directly under a header; the existing rows are
  filename-sorted at HEAD in both partitions (checked before the test), so C11's "filename order"
  rule is well-defined.
- `python3 -B reports/round-28/readme/sweep.py --selftest` → `selftest: 12/12 checks passed`,
  exit 0; live run → `rows 201 files 201`, footer `201` / `21/19/18/29/20/94`, exit 0. The sweep
  writes only inside its `--selftest` temp trees (`reports/round-28/readme/sweep.py:251-259,395-402`),
  so C11 §0's "read-only in live mode" holds.

**R03-C-1 (citation defect, low).** C11 cites `reports/round-28/readme/sweep.py:21` for `ROW_RE`
and `:22` for `TOPIC_RE` (`cov/C11-readme-delta.md:22-23`, repeated at `:444`). The live file has
`SECTION_RE` at `:59`, **`ROW_RE` at `:60`**, **`TOPIC_RE` at `:61`**, `TOTALS_RE` at `:62`,
`FOOTER_RE` at `:66-71`, `topic_of` at `:74` (which C11 does cite correctly, `:74-79`), the
equality test at `:140` (correct), the continuation control at `:398-401` (correct). The `:21`/`:22`
citations do not resolve to those objects; corrected pins above. No byte risk — the instrument
digest pin is the stronger anchor and it verifies.

**R03-C-2 (scope-precision defect, low).** C11 §6 states "No other live document carries a
`Total knowledge entries` line (grep 2026-10-19)" (`cov/C11-readme-delta.md:425-426`). That grep
does not reproduce as worded: `grep -rl "Total knowledge entries" --include="*.md" .` returns
`corpus/README.md` plus `corpus/lessons/round-19.md:115,224`, `corpus/lessons/round-28.md:66`,
`corpus/lessons/round-27.md`, `corpus/lessons/round-20.md`, and several filed
`reports/round-10/**` fragments. **None of the hits is an updateable live count surface** — the
lessons and reports hits are dated historical narrative inside filed, append-only records
(`corpus/lessons/round-19.md:115` quotes the *stale* 189 reading as the defect it was), so C11's
actionable conclusion (README `:469`/`:473` are the live surfaces; `LOG.md` is parent-owned)
stands. Recommended wording: "no other **updateable** live document carries the line" — the
grep-as-evidence then reproduces. Overlaps R09's cross-review lane ("any counting command the
integrator must update beyond corpus/README.md"); filed here for that seat to fold, not absorbed.

**R03-C-3 (acceptance completeness, recommendation).** C11 §4's required readings
(`cov/C11-readme-delta.md:366-370`) list every leg the sweep measures **except the footer date**,
and the sweep is measured blind to it (§3, control I). C11's E5 does move the date line
(`:112-113`), so the *draft* covers it; the gap is that the acceptance block would not catch an
integrator who applied the vector but not the date. Add to §4's required readings:
`Counts checked 2026-10-19 from the repo root:` present, and no line matching
`Counts checked 2026-10-18` in the footer block. This is exactly the round-28 defect species
(`corpus/README.md:17-35`: a present-tense footer claim that survived a count move), with a
subtler tell; one added leg closes it. Owner: integrator/C12 acceptance, cheap.

## 3. Delta control matrix (measured; the legs any reviewer/integrator can re-run)

All controls: the applied README against the same synthetic +10 tree, `sweep()` read-only.

| control | edit | observed reading |
|---|---|---|
| A full delta (headers + totals + footer + 10 rows, date moved) | all five sites | `ok True`, 211/211, exit-equivalent 0 |
| B no-footer delta | footer left at 201 / 21/19/18/29/20/94 | `ok False`, `FOOTER_TOTAL` + `FOOTER_DIR_TOTALS` |
| C no-totals delta | totals line left at 201 | `ok False`, `totals_ok False` |
| D headers-only | only `(23)`/`(24)` moved | `missing_from_index 10`, `totals_ok False`, both footer classes |
| G vector order swapped | `21/24/23/29/20/94` | `ok False`, `FOOTER_DIR_TOTALS` — the vector is **PARTS order** (linguistics, myth-symbol, culture-material, synthesis, verification, civilizations), not sorted |
| H one row omitted | 9 of 10 rows | `ok False`, `missing_from_index 1` — **`totals_ok` still True**, so the totals line alone cannot catch a missing row |
| E paraphrase row | one row's text condensed | `ok False`, `REWRITE` on that row (byte-equality is strict; continuation lines space-joined, `sweep.py:74-82`) |
| I stale footer date kept | counts all correct, date `2026-10-18` | **`ok True`** — the instrument does not read the date; see R03-C-3 |

**Sequencing (measured).** Applying the delta README against the **live** (pre-landing) tree reads
`ok False`: `rows 211 / files 201`, `ghosts 10`, header drift `{culture-material: 24 vs 18,
myth-symbol: 23 vs 19}`. The delta can only read green **after** the ten entries land; the
integrator order is entries → README edits (generator `--apply` + E1/E5-prose/E6 by hand, per
`cov/C11-readme-delta.md:350-354`) → `sweep.py` → E6's reading written from the measured run, never
predicted (`:410-413`).

## 4. Audit-runbook (C12) adequacy legs — measured requirements

C12's mission (`reports/round-35/targets.json`, seat `C12`): the per-entry checklist (frontmatter,
resolving pointers, decision record, gap statement, no-bleed language) "as a runnable recipe + the
expected results for the 10 drafts". Absent at the cut; the following are the legs I measured, each
with its baseline, so the runbook (and C13/C14/C17 through it) can be checked against evidence
rather than intent.

**4.1 The instrument it must name (and the one it must not).** The current-generation entry audit
is `reports/round-28/audit/entry-audit.py` — I verified at HEAD: **no write calls** (read-only);
`--selftest` → **11/11 checks passed**, exit 0; on two live exemplars the two-file run reads
`plant-symbolism.md bar=True … index=ok` and `textile-technology.md bar=False filler=True …
index=ok`, `bar clear 1`, `index clear 2`; and the admission gate **can fail**:
`--new corpus/knowledge/culture-material/textile-technology.md` → exit 1 (a legacy entry named as
new fails, as its docstring requires: "a `--new` entry must clear the bar unconditionally",
`reports/round-28/audit/entry-audit.py:20-26`). Its `index` leg is a hard check (row byte-equality
in the right partition), which makes it a second, independent instrument over the same property as
the README sweep. The round-19 instrument is **not** the one to name: its source-bullet parser
counts only two-space nested bullets under `- sources:`
(`reports/round-19/audit/entry-audit.py:59-67`), so entries carrying the house single-line
`- sources:` block read `src=0/0` (S01 §4 measured `TOTAL 0/2 clear the bar`, exit 2 on two live
exemplars; this seat did not execute that instrument — its only write calls are inside its
tempdir `selftest()`, `:152-179`, but the format artifact is visible in the parser source).

**4.2 Frontmatter leg — pin the documented class, not a slogan.** Measured census (this seat's
command, `- source:`/`- sources:`/`- verified-at:`/`- recheck:`/`- scope:` head-block regexes over
each partition):

| partition | files | `- source:` | `- sources:` | verified-at | recheck | **scope** |
|---|---|---|---|---|---|---|
| culture-material | 18 | 0 | 18 | 18 | 18 | **0** |
| myth-symbol | 19 | 19 | 19 | 19 | 19 | **0** |
| all six partitions | 201 | — | — | — | — | **0** |

`- scope:` appears in **0 of 201** entries corpus-wide, so claim C's "frontmatter 4/4
(source / verified-at / recheck / scope)" (`reports/round-35/claims.json:29`) is unachievable by
any entry, old or new. The runbook must therefore define the "documented 3/4 class" as
**source(s) + verified-at + recheck present, scope documented-absent**, cite this census, and
refuse any weaker reading — otherwise a 2/4 draft could be waved through as "documented". The
class precedent is round 10's A/B/C readings (`reports/round-10/coverage/audit-myth-culture.md`
§1.5: culture-material A 0/18, B 18/18 — the partition's established plural-only form).

**4.3 Gap leg — mechanically detectable or it repeats F1.** At HEAD, `- gap filled:` is **0/18**
(culture-material) and **0/19** (myth-symbol): the strict frontmatter form exists only in
linguistics (3/21) and verification (5/20). Round 10's F1 defect was exactly entries naming their
gaps in prose the runner's regex rejects (`reports/round-10/coverage/audit-myth-culture.md` §5,
§7). The runbook must require a **mechanically detectable** gap form (a frontmatter field, or a
body heading naming the gap — the r10 runner's accepted classes,
`reports/round-10/run-validation.py:361-368`), and the round-35 runner's gap regex must be
published *before* C13/C14/C17 audit, or audits and validation will disagree (the r19 runner's
looser `\bgap\b` + `.md` reading vs r10's regex is the filed precedent,
`reports/round-19/audit-1.md:16-20`).

**4.4 Decision-record leg.** The r10 runner accepted a `#{2,4}` heading containing
`decision[- ]record` (`reports/round-10/run-validation.py:369-370`); the corpus carries any
decision-record vocabulary in only **2/18** culture-material and **3/19** myth-symbol (my census).
The new-entry bar is deliberately stricter than the legacy form; the runbook must state the
accepted class (the r19 audit's looser `decision record|decision table|decisions? taken`,
`reports/round-19/audit/entry-audit.py:28`) **and** mirror the r28 instrument's non-retroactivity
note so the legacy split is not reported as a defect count.

**4.5 Pointer-resolution leg.** Broken repo-path references in the two partitions: **0** (census
over all backticked `corpus/…`/`tools/…`/`reports/…`/`examples/…` paths, this seat's command) — a
clean baseline the ten drafts must not degrade. No network this round (`reports/round-35/targets.json:9`),
so the URL leg must be a documented **non-fetch**: URL syntax + the entry's own access stamp +
`to-verify` marking for what was not retrieved — the round-19 criterion ("URLs get a documented
access attempt", `reports/round-19/audit-1.md:14-17`) reads as a fetch and is not runnable here;
a runbook that says "fetch each URL" fails its own runnability test.

**4.6 No-bleed leg.** Handoff language `lore-shokunin` is present in **18/18** and **19/19**
entries of the two partitions (census). The runbook leg should require the handoff/negation
sentence (QUALITY.md §5, `corpus/QUALITY.md:26-28`) **and** scan for positive
canon/promotion/clearance/closure assertions outside negations — the same language rule the A
claim audits cross-surface (`reports/round-35/claims.json:60-70`); C's leg is per-entry, A's is
per-surface, and the runbook should say which it is checking.

**4.7 README parity + expected results.** The runbook should name both byte-equality instruments
(`sweep.py` exit code, and the entry-audit `index` leg) and carry the post-landing expected
readings: `--new` on the ten landed paths exits **0**; corpus-wide index reading 211/211; the
sweep's `ok True` with `footer 211 / 21/23/24/29/20/94`. Anything the runbook asserts that is not
one of these commands or a mechanical rule is not a runnable recipe.

## Owed

- `reports/round-35/cov/C12-audit-runbook.md` — absent at this seat's cut (`ls reports/round-35/cov/`
  → `C11-readme-delta.md`, `C15-receipt.md`, `C16-scribe.md`). §4 above is the adequacy spec it
  must be reviewed against; when it lands, its checklist must be checked against §4.1–§4.7's
  measured baselines (a slot for a post-batch R03 fold, or C13/C14/C17's own reading).
- `reports/round-35/run-validation.py` — the validation legs my surfaces require, for S04/the
  integrator to fold: (a) footer **date** leg (the sweep is blind to it — control I; expected
  `Counts checked 2026-10-19`); (b) row byte-equality leg (sweep + entry-audit index leg);
  (c) `--new` exit 0 on the ten landed paths. The file does not exist at this seat's cut
  (`ls reports/round-35/run-validation.py` → rc 2) and was not executed anywhere (F-C13-1).

## Citations

- `reports/round-35/targets.json:5-13,236` — shared rules; seat R03 mission (`:5-13` also seat C12's
  mission text)
- `reports/round-35/claims.json:21-35,29,31-35,60-70` — claim C, after_required, counting commands,
  claim A's bleed scope
- `reports/round-35/cov/C11-readme-delta.md:11-13,22-26,43-58,112-113,350-354,366-370,410-413,425-426,444`
  — pins, line map, E5 date edit, apply order, acceptance readings, E6 rule, §6 grep sentence
- `corpus/README.md:1-15,17-35,123,147,149-167,169,171-188,469,471-480,482-493` — live bytes and
  the revision convention (read at sha256 `053966a2…`)
- `reports/round-28/readme/sweep.py:59-62,66-71,74-82,119-212,251-259,394-402,415-427` — row/topic
  contract, footer leg, CLI, selftest writes (digest `9b2ccac0046831fdaf48863ccd0ff6ca0fa390d044746c876e83a71c06f0cdd3`)
- `reports/round-28/audit/entry-audit.py:1-42,20-26` — current-generation entry audit, `--new`
  semantics, read-only claim (verified by this seat)
- `reports/round-19/audit/entry-audit.py:28,49-67,152-179` — r19 instrument's parser and decision
  classes; write calls confined to its tempdir selftest
- `reports/round-10/run-validation.py:81-82,354-370` — r10 frontmatter fields, gap/decision regexes
- `reports/round-10/coverage/audit-myth-culture.md` §1.5, §5, §7 — A/B/C frontmatter readings, F1
- `reports/round-19/audit-1.md:14-20` — round-19 audit criteria and regex-looseness note
- `corpus/QUALITY.md:1-28` — the admission bar (canon hygiene §5)
- Commands run by this seat (all read-only; `.scratch/r03/**` is disposable scratch, not evidence):
  - `sha256sum corpus/README.md reports/round-28/readme/sweep.py` → `053966a2…`, `9b2ccac0…`
  - `python3 -B reports/round-28/readme/sweep.py` → `rows 201 files 201`, `footer_ok True`, exit 0;
    `--selftest` → `12/12 checks passed`
  - generator extracted verbatim from `cov/C11-readme-delta.md` §3 → `.scratch/r03/readme-delta.py`;
    live no-op run (`missing_rows 0`, totals/footer before==after, exit 0); synthetic +10 tree
    (`cp -r corpus/knowledge` + 10 stubs, multi-line topics) → `--apply` exit 0, 10 rows, anchors
    148/156/157/167 and 170/172/176/176/186/188; `sweep()` over applied README → `ok True`, 211/211
  - control matrix A/B/C/D/E/G/H/I (§3) — same synthetic tree, hand-applied deltas
  - `python3 -B reports/round-28/audit/entry-audit.py --selftest` → 11/11, exit 0; two-file run →
    `bar clear 1`, `index clear 2`, exit 0; `--new corpus/knowledge/culture-material/textile-technology.md`
    → exit 1
  - `python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge` →
    `totals.files 201`, exit 0
  - frontmatter/pointer/decision/handoff census over the six partitions (script in the run log;
    readings in §4.2–§4.6)
  - `grep -rl "Total knowledge entries" --include="*.md" .` → README + lessons + filed r10 fragments
    (R03-C-2)
