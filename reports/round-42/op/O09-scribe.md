- Seat: O09 | scribe | claim O | date 2026-10-19 | baseline ac47c78

# O09 — landed-changes material (claim O)

**In-flight snapshot, not a round census and not an admission.** Census command
run read-only at `2026-10-19T15:57:47Z` under
`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`:
`find reports/round-42 -type f | sort` →
`reports/round-42/claims.json`, `reports/round-42/targets.json`,
`reports/round-42/telemetry/dispatch-declared.json` (3 files). Every declared
claim-O implementation and verification output was absent at this cut —
`op/O01-fix-draft.md`, `op/O02-controls.md`, `op/O03-predicted.md`,
`op/O04-verify.md`, `op/O05-traps.md`, `op/O06-receipt.md`,
`op/O08-queue-update.md`, `op/O12-policy-check.md` all absent (per-path `[ -f ]`
test). So **no fixed extractor, no selftest run, and no corrected census exist
to describe as landed.** The claim's after-state is unestablished here.

## What the delivered revision does show (pre-landing, read-only)

These are the before-state facts a landed-changes record must move, measured at
`ac47c78`; none of them is the claim's after-state.

1. **The wrapped field is real and singular.** Exactly one of the corpus's 220
   `- couples:` fields carries continuation lines:
   `corpus/knowledge/linguistics/phonetics-phonology.md:72-77` (5 continuation
   lines, ending `:77`). Corpus-wide scan: `total couples fields: 220`,
   `wrapped (continuation lines): 1`. This independently reproduces r39 Ca04 D1
   (`reports/round-39/calib/Ca04-verify.md`, D1).
2. **Every located extractor host is single-line.** Both filed resolver
   instruments capture the field with `re.M` single-line semantics:
   `reports/round-19/audit/entry-audit.py:75` and
   `reports/round-27/audit/entry-audit.py:275`, each
   `re.search(r"^- couples:\s*(.*)$", text, re.M)`. The r19 capture on the live
   field returns the truncated string `'language (this file, core method); myth
   (divine/true names, taboo'` — no `.md` token at all. `tools/` carries no
   couples resolver (grep for `- couples` in `tools/` hits only gate
   docstring/fixture text in `provenance-audit.py`, `source-audit-inventory.py`),
   so the host a fix must patch is a filed `reports/round-19|27/audit/entry-audit.py`
   — which the round's non-goal "no filed byte rewrites" bars editing in place.
   **The claim's own wording anticipates this** ("its owning instrument
   identified by the wave — likely the r39 C12 runbook's resolver or a
   tools/harness couples checker; the wave confirms the host"); that
   identification is owed by K01/O01, not by this seat.
3. **Block extraction recovers 4 tokens, 2 of them phantoms — and one mangled.**
   A read-only block read of `:72-77` yields tokens
   `['sound-change.md', 'prosody.md', 'sound-symbolism.md', 'writing-systems.md']`
   (4). Existence against `corpus/knowledge/linguistics/`:
   `sound-symbolism.md` ✓, `writing-systems.md` ✓, `sound-change.md` ✗,
   `prosody.md` ✗. The fourth token is a **line-break artifact**: the field
   writes `tone-` at the end of `:76` and `prosody.md` at the start of `:77`, so
   a naive block join that does not undo the soft wrap produces `prosody.md`
   rather than `tone-prosody.md` — matching r39 Ca04 D1's `to-verify` note about
   C14's `prosody.md` mangling. A fix that only concatenates continuations
   without de-hyphenating the wrap will still mis-tokenise this field.
4. **Corpus-wide extractor delta is exactly 4 tokens.** Same scan, single-line
   vs block token sets per file: only one file differs —
   `corpus/knowledge/linguistics/phonetics-phonology.md`,
   `block-only: ['prosody.md', 'sound-change.md', 'sound-symbolism.md', 'writing-systems.md']`,
   `single-only: []`. Totals: `single-line token total: 1848`,
   `block token total: 1852` over 220 files. This is a raw token count over the
   whole corpus, **not** the r39 policy's ref census (which counts refs after
   brace expansion and dedup per entry, and reports 2504 at 212 entries —
   `reports/round-39/calib/Ca03-basename-policy.md:35-36,268`). The two numbers
   are different units; a corrected census must state which it is.
5. **The r39 baseline arithmetic a corrected census must reproduce.**
   `2504 = 2335 direct + 163 fallback + 0 ambiguous + 6 unresolved` at
   `entries=212` (`reports/round-39/calib/Ca03-basename-policy.md:35-36,268,355`).
   The corpus is now 220 entries (`find corpus/knowledge -name '*.md' | wc -l`),
   so the successor census is not a subtraction of 2 phantoms from 2504; the
   entry denominator itself moved (216 → 220 across r39–r40 landings,
   `LOG.md` r39/r40 entries). Stating "2504 minus the phantoms" without
   re-running at 220 would be a unit/denominator error.

## Report-ready material (draft, for the integrator)

- **Work performed (draft):** operability claim O — the N6 couples-reference
  extractor gains block parsing so the corpus's one wrapped couples field reads
  whole; corpus-wide recount re-derives the reference census; selftest controls
  incl. wrapped-field positive and synthetic phantom negative
  (`reports/round-42/claims.json`, claim O).
- **Landed changes:** *pending integration evidence.* The declared deliverables
  are the fixed extractor durable at a named host, the corrected census filed,
  green selftest, and queue-v2 N6 re-classed
  (`reports/round-42/targets.json:92-94`, `claims.json` claim O). None is
  asserted by this snapshot.
- **Before → required after:** before is the single-line extractor zeroing the
  wrapped field (0 tokens captured vs 4 named; 2 phantoms, one of them the
  `prosody.md` wrap artifact — items 1–3 above). Required after is the wrapped
  field read 4/4, the corrected census reproducing the r39 arithmetic minus the
  dispositioned phantoms at the current denominator, selftest green, and zero
  undispositioned phantom attributions.
- **SHONEN:** no promotion, canon, clearance or closure conclusion. Any
  capability wording ("corpus couples census is exact") must stay conditional
  until the fix host is identified, the fixed tool is durable under a path the
  non-goals permit, and `reports/round-42/run-validation.py` has been run in an
  isolated copy by the parent (the in-tree run is prohibited for this seat).

## Owed

- The landed fix itself: no durable fixed extractor exists at this cut, and the
  two located hosts (`reports/round-19/audit/entry-audit.py:75`,
  `reports/round-27/audit/entry-audit.py:275`) are filed bytes. The integrator
  must resolve where the fixed instrument durably lives; a `tools/harness/`
  couples checker is the only route consistent with the round's non-goals, and
  that choice is not this seat's to make.
- `op/O01-fix-draft.md`, `op/O02-controls.md`, `op/O03-predicted.md`,
  `op/O04-verify.md`, `op/O05-traps.md`, `op/O06-receipt.md`,
  `op/O08-queue-update.md`, `op/O12-policy-check.md` — all absent at
  `2026-10-19T15:57:47Z`; the predicted census (O03) and its isolated
  verification (O04/O05) are the comparison basis for any landed recount.
- The wrap de-hyphenation question (item 3) is **to-verify**: whether the
  intended token is `tone-prosody.md` (the field's prose reads `tone-` /
  `prosody.md` across `:76-77`) is a reading of the source, not something this
  seat can prove; a fix that joins continuations verbatim will emit
  `prosody.md`.
- Recompute this census at close on the delivered revision; the in-tree
  `reports/round-42/run-validation.py` remains prohibited
  (`reports/round-42/targets.json:8`).

## Citations

- Assignment and boundary: `reports/round-42/targets.json:92-101` (seat O09,
  out `op/O09-scribe.md`), `:4-9` (shared rules), `:8` (no in-tree
  run-validation). Declared claim and thresholds: `reports/round-42/claims.json`
  (claims `O` and `C`; non-goals incl. "no filed byte rewrites").
- Baseline commit and declared dispatch: `reports/round-42/telemetry/dispatch-declared.json`
  (`baseline_commit: ac47c78`, devin/`deepseek-v4-1-flash-high`, 32 requested,
  1 batched call, closing snapshot `open-at-seat-close`); `git log --oneline -5`
  → `ac47c78 round-41: admit O/Ca …` at HEAD.
- Wrapped-field bytes: `corpus/knowledge/linguistics/phonetics-phonology.md:72-77`.
- Extractor hosts: `reports/round-19/audit/entry-audit.py:75` (and `:74-96`
  resolution), `reports/round-27/audit/entry-audit.py:275` (and `:270-288`).
- r39 baseline arithmetic and D1: `reports/round-39/calib/Ca03-basename-policy.md:35-36,268,355`;
  `reports/round-39/calib/Ca04-verify.md` (D1, incl. the `prosody.md`
  mangling note and the 1-wrapped-field census).
- Queue row: `reports/round-40/op/defect-queue-v2.json:362-369`
  (`N6-couples-extractor-wrapped-field`, class `carried-with-owner`).
- Command outputs (this seat, 2026-10-19, lane root, tree at `ac47c78`, all
  read-only, no `run-validation.py` executed, no git/network/install):
  (a) `find reports/round-42 -type f | sort` → 3 files (claims, targets,
  telemetry/dispatch-declared); per-path `[ -f ]` tests → the eight named O
  outputs absent.
  (b) corpus-wide `- couples:` scan → `total couples fields: 220`,
  `wrapped (continuation lines): 1` at
  `corpus/knowledge/linguistics/phonetics-phonology.md line 72`.
  (c) single-line capture on that field → `'language (this file, core method);
  myth (divine/true names, taboo'`; block capture of `:72-77` → 4 tokens
  `sound-change.md` (absent), `prosody.md` (absent), `sound-symbolism.md`
  (present), `writing-systems.md` (present).
  (d) single-line vs block token totals over 220 files → `1848` vs `1852`;
  sole differing file is `phonetics-phonology.md` with
  `block-only: [prosody.md, sound-change.md, sound-symbolism.md, writing-systems.md]`.
  (e) `ls corpus/knowledge/myth-symbol/*.md | wc -l` → 23;
  `find corpus/knowledge -name '*.md' | wc -l` → 220 (claim C's before-state,
  recorded for the integrator; not this seat's claim).
