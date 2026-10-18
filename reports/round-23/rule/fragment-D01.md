# R23-D01 — rule statement + injection-point warning (draft pass)

- Seat: D R23-D01 (rule drafter 1 of 3). Date: 2026-10-18.
- Axes: depth (family-owned provenance), operability (fail-closed dispatch).
- Scope: draft contribution only; this seat writes no source, no gate, no
  SKILL.md, and no filed round artifact. Consolidated output:
  `reports/round-23/rule/skill-draft.md` §1 (paragraphs 1-2).

## Contribution

**Rule statement.** Merged from `reports/round-22/bleed/design.md` §Decision
(`:5-11`) and its closing draft rule (`:50-52`) into one opening paragraph:
family selected **before** construction of labels/ledgers/coverage/findings;
shared machinery (parser/gate code, tool paths, `D2L-*` diagnostic names)
reusable; foreign fixture records, bare citations, owner labels, schemes,
residuals, and conflict findings banned from family-owned fields; identity at
least `(family, source block/component, record id)` (design.md:9, carried
verbatim); declared borrow ledgers are not import permission (design.md:7,41);
determinism is not isolation, grounded in the measured pre-fix 19/19 pass
(`reports/round-22/bleed/repin.md:15,18`; rejected reading at
`corpus/lessons/round-22.md:63`).

**Injection-point warning.** The claim's parenthetical "(unconditional D2
build_payload)" is verified at source: at round-21 baseline `46a03257…`,
`run_pipeline` called `build_payload()` unconditionally at
`tools/d2-typed-labels.py:2613`, with the embedded D2 constants at `:925-1197`
and the helper taking no packet/family argument (`:1235-1258`); the alias leg
followed at `:2614` and annotated the foreign ledger without localizing it
(`analysis.md` §D02 `:90-101`). The no-disk-read proof is C3
(`analysis.md:103-110`): with `load_packet_file` replaced by a raising
sentinel, `build_payload()` still returned the exact D2 ledger byte-equal to
the filed D4 `rank_rules` (2/2 helper probes, 2026-10-18T14:42:15.772158+00:00,
combined command exit 0 at `analysis.md:112-170`). The landed shape to
preserve is the family-side dispatch now at `tools/d2-typed-labels.py:2837-2838`
(`build_payload()` only when `family == DEFAULT_FAMILY` (`:2471`), else
`family_rank_payload`).

## Review findings

- **F1 (claim wording verified).** "Unconditional D2 build_payload" matches
  the pinned source, not a paraphrase: the call precedes any family branch and
  the helper reads module-level D2 constants. Verified by
  `git show 46a03257…:tools/d2-typed-labels.py | sed -n '2599,2615p'`,
  2026-10-18.
- **F2 (historical record vs landed source — cite both, reconcile neither).**
  `LOG.md:3298-3309` records round-22 D as "never implemented — the impl
  seats were interrupted. Routed to round 25 with the full recipe", while the
  same closing commit `0e81d9d` carries the impl seat's family-clean source
  (live `tools/d2-typed-labels.py` = `2819f687…`, verified by `sha256sum`,
  matching `reports/round-22/bleed/impl.md:3,41`). Both are filed facts: the
  LOG line is the round verdict as recorded; the digest is the tree state. The
  draft cites each for what it is and the orchestrator must not edit the LOG
  entry to "fix" the tension (`corpus/lessons/round-22.md:19` — keep
  historical verdict, current reproduction, and supersession distinct).
- **F3 (revision-pinned citations).** Line numbers in the warning paragraph
  are valid at the revision stated (`46a03257…` for the defect;
  `0e81d9d` for the landed dispatch). The drift is real — the same call site
  moved from `:2613` to `:2837` between the two revisions — so any future
  revalidation must use `git show <rev>:…`, never HEAD alone.
- **F4 (identity definition).** The `(family, source block/component, record
  id)` formulation is design.md:9 verbatim; do not shorten it to bare record
  IDs in integration, because the same-ID foreign-record control
  (`tools/d2-typed-labels.py:3109`) is what gives it teeth.

## Verification record (all 2026-10-18, read-only)

- `git show 46a03257ee75dd8f685a105e47da3f45a0154172:tools/d2-typed-labels.py`
  piped to `sed -n '2599,2615p'` → unconditional `ledger = build_payload()`.
- `grep -n "build_payload()" tools/d2-typed-labels.py` at `0e81d9d` →
  `:2837` family-side dispatch; `sed -n '2825,2845p'` confirms the branch.
- `sha256sum tools/d2-typed-labels.py` →
  `2819f68769dfc0b57f46cdaeb4c9a96324c5711c46348f5a8308382dfd7053c3`.
- `grep -n "Round 22 REJECTED\|Routed to round 25" LOG.md` → `:3298`, `:3308`.

Status: draft pass complete; no claims of gate passes made here. The D
claim's counting command belongs to the orchestrator.
