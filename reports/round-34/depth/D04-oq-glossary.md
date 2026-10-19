- Seat: D04 | executor | claim D | date 2026-10-19 | baseline da68a6d

# D04 — OQ/glossary refresh (claim D)

Mission (targets.json D04): rewrite OQ-V3-05 and any other stale OQ row of the
current default pair to live state; verify the glossary entries against the
current artifacts. Deliverable shape: audit + exact before/after rewrite drafts
for the integrator. No filed byte was edited, no round runner was executed
(`git status --porcelain -- reports/` at seat close shows only `?? reports/round-34/`).

## 1. Live reference values (ground truth for every number below)

Measured 2026-10-19 at baseline `da68a6d`, `TMPDIR=$PWD/.scratch
PYTHONDONTWRITEBYTECODE=1`, by `python3 -B .scratch/d04/oq-audit.py`
(D04's own read-only audit script, `.scratch/d04/oq-audit.out`):

| surface | live value | citation |
|---|---|---|
| D4 typed_labels | 82 | examples/culture-d4/typed-labels.d4.yml:46 (`"typed_labels": 82`) |
| D4 labels_by_kind | native-form 64, translated-label 12, borrowed-strata 6 | examples/culture-d4/typed-labels.d4.yml:36-38 |
| D4 findings | findings_total 12, findings_hold_or_fail 12, label_findings_hold 12, label_findings_fail 0 | examples/culture-d4/typed-labels.d4.yml:31-35 |
| D4 rank leg | conflicts 0, rank_rules_unresolved_items 0, rank_quarantine_handles 0, reconciliation_records 6 | examples/culture-d4/typed-labels.d4.yml:30,40,44,45 |
| D4 hold set | hold 12, note 0, fail 0; 12 rows, every row `D2L-FORM-UNRESOLVED` (6 GAR-* + 6 LEX-GAR-*) | examples/culture-d4/expected-holds.json `counts`; row list |
| D4 era alias leg | alias_rows 4, basis family-local (explicit skip of the D2 leg) | examples/culture-d4/typed-labels.d4.yml:136-165 |
| D2 residuals | rank_rules_unresolved_items 13, rank_quarantine_handles 3, conflicts 4, reconciliation_records 10 | examples/culture-d2/typed-labels.d2.yml:30,40,44,45 |
| D3 lexicon / bridges | 20 lexemes, 5 bridges; S01 partial-support, S02/S03/S04 scoped-support, S05 partial-support | examples/culture-d3/packet.json `lexicon`, `references[].support_scope` |
| D3 screening | real_language_sweep_performed false | examples/culture-d3/packet.json `screening` |
| D3 beliefs | B01, B02 truth_status `unresolved` | examples/culture-d3/packet.json `beliefs` |
| contract | digest sha256 5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069, revision 1.0.0, bilateral read pending | `sha256sum corpus/knowledge/synthesis/worldbible-integration-contract.md`; contract:11,15 |
| r6 pair digests | packet.md 6ced88ad009f…, twin.json 6633443d70ce… | `sha256sum`; reports/round-30/handoff/declared-in-r6/freeze.txt:2-3 |

## 2. OQ row audit — all 10 rows

Rows live at `reports/round-30/handoff/declared-in-r6/packet.md:299-308`
(rendered) and in the twin at `twin.json` `open_questions`. Verdicts:

| OQ id | packet.md | live check performed | verdict | action |
|---|---|---|---|---|
| OQ-V2-01 | :299 | d3 screening carries `real_language_sweep_performed: false`; no sweep receipt exists | current | none |
| OQ-V2-02 | :300 | contract digest re-measured equals the row's `5f4c02bfc4e6…`; revision 1.0.0 (contract:11); no bilateral read record exists (contract:15, corpus/lessons/README.md:171 Q-02-3 open) | current | none |
| OQ-V2-03 | :301 | D2 live = 13 unresolved rank items / 3 quarantine handles / 4 conflicts / 10 reconciliation records, exactly as worded | current | none |
| OQ-V2-04 | :302 | B01/B02 `truth_status: unresolved` on live bytes | current | none |
| OQ-V2-05 | :303 | 5 bridges; support_scope values are partial/scoped exactly as worded | current | none |
| OQ-V2-06 | :304 | no numeric assertion; no live contradiction found | current | none |
| OQ-V2-07 | :305 | superseded in kind: the v3 renderer **is** the durable builder and emits its own freeze pair (`expected.json` tools/exercise-handoff-e2e.py:4077; `freeze.txt` :4126; landed at reports/round-30/handoff/declared-in-r6/) | stale-by-lifecycle | supersession note, §3b |
| OQ-V3-04 | :306 | era_alias leg family-local (typed-labels.d4.yml:163-165 names the packet's own `named_eras` and declares the explicit skip), alias_rows 4; row is retained only as re-open id | current | none |
| OQ-V3-05 | :307 | **stale on all four clauses**: says "twelve form holds + three rank holds + one note, thirteen unresolved rank items, three quarantine handles and four conflicts"; live is 12 holds / 0 rank holds / 0 notes (expected-holds.json counts) and 0 / 0 / 0 in the D4 coverage block | **STALE** | rewrite, §3a |
| OQ-V3-06 | :308 | no lore baseline revision, entity key or receipt surface exists for the D4 culture (D4-CL12 stays `unresolved`, packet.md:155; corpus/knowledge/synthesis/ holds no D4 receipt) | current | none |

Method control (negative): the same audit applied to OQ-V2-03 flags nothing, and
applied to OQ-V3-05 flags all four clauses — so the scan discriminates, it does
not flag every row. Re-run command in §7.

## 3. Rewrite drafts

### 3a. OQ-V3-05 — the generator literal (required)

Defect class, already filed once: the row's prose is a **hard-coded string
literal** that cannot self-correct (`corpus/lessons/round-25.md:82`). Round 25
corrected the row inside a filed supersession build
(`reports/round-25/v3-supersession/declared-in-r4/packet.md:310`) but never the
generator, so the round-30 rebuild re-emitted the stale text at packet.md:307 —
this is the OQ half of round-33 finding A02-H1
(`reports/round-33/adj/A02-handoff.md:106`; `reports/round-33/adj/A15-audit-draft.md:177`).
Fixing the bytes again without fixing the literal would repeat the round-25 miss.

**Before** (`tools/exercise-handoff-e2e.py:3523-3532`, verbatim):

```python
            {
                "id": "OQ-V3-05",
                "question": (
                    "D4's inherited and own holds stay open: twelve form holds + three rank holds + one "
                    "note, thirteen unresolved rank items, three quarantine handles and four conflicts — "
                    "kotodama; blocking for the affected D2 rank records and the six garment terms, not for "
                    "this envelope"
                ),
                "unresolved_claims": "D4-CL09",
            },
```

**After** (replacement, every number live-backed; wording follows the round-25
canonical correction and re-measures it against today's bytes):

```python
            {
                "id": "OQ-V3-05",
                "question": (
                    "D4's own holds stay open: twelve form holds, zero rank holds, zero notes and zero "
                    "fails; the inherited D2 rank residuals (13 unresolved rank items, 3 quarantine "
                    "handles, 4 conflicts) stay D2-owned and still open under OQ-V2-03, not resolved — "
                    "kotodama; blocking for the six owed D4 garment terms, not for this envelope"
                ),
                "unresolved_claims": "D4-CL09",
            },
```

Live backing per token (audit output, section 7): "twelve form holds" =
expected-holds.json `counts.hold` = 12 with 12 rows all `D2L-FORM-UNRESOLVED`;
"zero rank holds / zero notes / zero fails" = counts.note 0, counts.fail 0 and
zero `D2L-RANK` rows in examples/culture-d4/{expected-holds.json,typed-labels.d4.yml};
the three parenthesised D2 numbers = examples/culture-d2/typed-labels.d2.yml:44,40,30.

Notes for the integrator:
- `unresolved_claims` is kept at `D4-CL09`. The harness leg only requires that
  every `unresolved` claim be *referenced* by an OQ row
  (`tools/harness/packet_uncertainty.py:16`, `(--require-oq)` in the usage at
  :29); D03 owns whether D4-CL09's own status stays `unresolved` (the round-25
  census invariant kept statuses at 16 supported / 7 partial / 4 unresolved when
  the same numbers were corrected). If D03 flips D4-CL09 to `supported`, keep
  this row (surplus rows are tolerated — OQ-V3-04 carries `unresolved_claims:
  "—"`) but re-point the field to the still-open claim on the live reading; the
  six owed garment terms are claim D4-CL04 (`partial`, packet.md:147).
- The replacement must land in the generator, not in the emitted packet: the
  twin's OQ row (twin.json `open_questions`, now carrying the stale text) is
  built from this same literal, so both the Markdown row at packet.md:307 and
  the twin row flip together on the next build.
- Shared-file rule: I did **not** edit tools/exercise-handoff-e2e.py; this is a
  draft for the integrator (and it is the same file pair the D-block re-pin
  cascade already touches at :1933-1934).

### 3b. OQ-V2-07 — supersession note (no filed-byte edit)

The row is carried **verbatim** from the filed v2 twin: the renderer loads
`open_questions` through `v3_load_v2_rows` (tools/exercise-handoff-e2e.py:2261-2283,
reading reports/round-15/handoff/packet-v2-05.yml with the harness reader), just
as it loads the 15 claim rows. Editing the v2 file is out of scope (filed bytes),
and deleting the row would drop the carry. The round-20 claims-map already
prescribes the resolution for exactly this row: "the v3 exercise now *is* the
builder; the packet seat should say so in that row's text rather than delete it"
(`reports/round-20/handoff/claims-map.md:256`).

Live facts that close the row's "process gap": the v3 renderer writes its own
`expected.json` (tools/exercise-handoff-e2e.py:4077) and `freeze.txt` (:4126) into
the frozen directory, and the current pair's freeze receipt binds the delivered
bytes (`reports/round-30/handoff/declared-in-r6/freeze.txt:1-8`; packet_sha256
6ced88ad009f… equals `sha256sum` of the delivered packet.md).

**Draft, option B (recommended) — add a new literal row after OQ-V3-06**
(keeps the v2 carry untouched; no post-processing of the loader):

```python
            {
                "id": "OQ-V3-07",
                "question": (
                    "OQ-V2-07's builder/freeze process gap is closed for this build: the v3 exercise is "
                    "the durable builder and emits its own expected.json "
                    "(tools/exercise-handoff-e2e.py:4077) and freeze.txt (:4126) beside the packet, and "
                    "the current pair's freeze receipt binds the delivered bytes (packet_sha256 "
                    "6ced88ad009f…, reports/round-30/handoff/declared-in-r6/freeze.txt:2) — the v2 row "
                    "itself stays carried verbatim per reports/round-20/handoff/claims-map.md:256"
                ),
                "unresolved_claims": "—",
            },
```

**Draft, option A (alternative)** — append a supersession clause to the carried
row at render time. Before (rendered bytes, packet.md:305): the row as worded.
After (appended sentence, only the tail changes):

> …but the freeze step is not this file's — round-15 integrator; process gap, not
> a packet-content gap. **Superseded in kind by this build: the v3 exercise is the
> durable builder and freezes its own pair (expected.json, freeze.txt), so the gap
> is closed for this revision; the row is retained per
> reports/round-20/handoff/claims-map.md:256.**

Option B is lower risk (A requires a post-load text mutation in the renderer,
which the twin would then mirror only if the mutation runs before the twin is
built). Both options leave every filed byte untouched. Whichever the integrator
picks must be idempotent: re-running the renderer must not double-append.

### 3c. Rows needing no change

OQ-V2-01, -02, -03, -04, -05, -06, OQ-V3-04, OQ-V3-06: audited current per §2 —
no rewrite owed, and no filed byte touched to leave them as they read.

## 4. Glossary verification — 20/20 exact

Method: parsed the 20 rendered rows from packet.md:316-335 and compared them
field-for-field against the live D3 lexicon
(examples/culture-d3/packet.json — digest bdf635ce…, equal to the packet's own
A-02/A-GLOSS manifest rows, packet.md:97). All 20 rows match exactly on
`entry_id`, E0 form, E1 form, gloss, and the etymology cell, including the
per-row derivation ("changed by SC1 initial /p/ > /f/ (ordinary register)" on
L01/L04/L05/L06 — the four /p/-initial lexemes — and "unchanged into E1" on the
other 16) and `available_from E0`; source order L01–L20 equals the live lexicon
order. Script and output: `.scratch/d04/glossary-verify.txt` (ALL 20 EXACT: True).

The prose at packet.md:310-313 is also accurate: 20 rows, "the assembled D3
packet's lexicon in source order", "computed E1 ordinary form", "Every etymology
carries `status: <record status>`"; the live lexicon carries `status:
constructed` and `available_from: E0` on every row.

Drift-proof by construction (why this section needed no correction while OQ-V3-05
did): the glossary is generated live from the D3 packet each build
(`v1_build_glossary`, tools/exercise-handoff-e2e.py:645-670 — it reads
`d3["lexicon"]`, requires exactly 20 entries, requires exactly one
ordinary-register sound change, and derives each etymology from that change), so
it has no hard-coded numbers to go stale. The gate leg that judges it is a count
(`glossary_entries` 20, frozen in
reports/round-30/handoff/declared-in-r6/expected.json `expected_scan`).

Observation for D06/D08 (not a defect in claim D's scope): the machine twin does
not carry the glossary at all — `twin.json` top-level keys are
`artifact_manifest, claim_ledger, coupling_edges, open_questions, packet_id,
packet_version, profile` — so the glossary's only machine check is the gate's
entry count, and no twin-parity leg exists or is needed for it.

## 5. Cross-claim couplings and a caught shorthand error

- **claims.json shorthand is misleading.** claims.json:27 (claim D `before`)
  writes live as "82/64/12/12"; the four live values are typed_labels 82 /
  native-form 64 / translated-label 12 / **borrowed-strata 6** (the fourth "12"
  is `findings_total`, not borrowed-strata — 64+12+6 = 82). The same shorthand
  appears in D03's mission (`targets.json:25`). Flagged so no ledger row lands
  "borrowed-strata 12"; D03 should take the field values from
  examples/culture-d4/typed-labels.d4.yml:36-38,46.
- **D03 dependency** — OQ-V3-05's `unresolved_claims: "D4-CL09"` and D4-CL09's own
  rewritten status must agree; see §3a notes.
- **D10/integrator dependency** — the OQ literal lives in the same file the re-pin
  cascade edits (tools/exercise-handoff-e2e.py); the two edits are disjoint
  (3523-3532 vs 1933-1934) and can land in one revision.
- **D05 dependency** — the after-text in §3a/§3b is the source text for the
  packet draft's OQ section; D05 should copy it verbatim rather than paraphrase.

## 6. Landing instructions (integrator)

1. Apply §3a's after-block in place of tools/exercise-handoff-e2e.py:3523-3532
   (the OQ-V3-05 dict entry; the surrounding OQ-V3-04/V3-06 entries are unchanged).
2. Apply either §3b option (recommended B: the new OQ-V3-07 dict entry appended to
   the same list).
3. Rebuild the packet pair into reports/round-34/handoff/declared-in-r7/; the new
   packet's OQ section must then read the §3a/§3b text and the twin's
   `open_questions` must carry it identically.
4. No glossary change is needed; the 20 rows regenerate byte-equal from the live
   D3 packet (already proven by §4 against the current build).

## 7. Verification commands (re-runnable)

```
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
python3 -B .scratch/d04/oq-audit.py            # live values + per-row flags + after-text consistency
python3 -B .scratch/d04/oq-audit.py reports/round-34/handoff/declared-in-r7/packet.md   # after the r7 build
python3 -B .scratch/d04/glossary-verify.py     # (as run: .scratch/d04/glossary-verify.txt; 20/20 EXACT)
```
Observed at seat close (`.scratch/d04/oq-audit.out`): live values as in §1, OQ-V3-05
flagged on all four stale clauses, OQ-V2-03 flagged clean, and
"VERDICT: after-text fully live-backed".

## Owed

none — every dependency this mission names was present (the pair, the live D2/D3/D4
artifacts, the renderer source, the filed round-20/25 precedents). Application of
§3a/§3b is integration work (D05 + integrator), not a missing dependency; the only
open judgement handed upward is D03's D4-CL09 status decision (§5).

## Citations

Paths: reports/round-30/handoff/declared-in-r6/{packet.md,twin.json,expected.json,freeze.txt};
reports/round-30/handoff/declared-in-r6/packet.md:97,147,152,156,299-308,310-313,316-335;
reports/round-30/handoff/declared-in-r6/twin.json (open_questions; top-level keys);
reports/round-30/handoff/declared-in-r6/expected.json (counts, expected_scan, cross_refs);
reports/round-30/handoff/declared-in-r6/freeze.txt:1-8;
examples/culture-d4/typed-labels.d4.yml:30-46,136-165; examples/culture-d4/expected-holds.json (counts, holds);
examples/culture-d4/packet.d4.yml form_slots (6 unfilled, owners GAR-01..06);
examples/culture-d2/typed-labels.d2.yml:30,40,44,45; examples/culture-d3/packet.json (lexicon, screening, beliefs, references[].support_scope, bridges);
tools/exercise-handoff-e2e.py:645-670 (v1_build_glossary), 1933-1934 (pins), 2261-2283 (v3_load_v2_rows),
2289+ (v3_parse_claims_map), 2599-2618 (v3_build_claim_rows), 3507-3541 (OQ literals), 4077,4126 (freeze emission);
tools/harness/packet_uncertainty.py:16,29 (--require-oq semantics);
reports/round-20/handoff/claims-map.md:99,104,109,116,124,154,158,251,256;
reports/round-25/v3-supersession/declared-in-r4/packet.md:310 and expected.json/freeze.txt (canonical prior correction);
corpus/lessons/round-25.md:82; reports/round-33/adj/A02-handoff.md:106,110,118; reports/round-33/adj/A15-audit-draft.md:177;
corpus/knowledge/synthesis/worldbible-integration-contract.md:11,15; corpus/lessons/README.md:171 (Q-02-3);
reports/round-34/claims.json:24-37; reports/round-34/targets.json:25-26.

Commands: `python3 -B .scratch/d04/oq-audit.py`; `.scratch/d04/glossary-verify.txt` run;
`sha256sum examples/culture-d4/typed-labels.d4.yml examples/culture-d4/expected-holds.json examples/culture-d3/packet.json
reports/round-30/handoff/declared-in-r6/packet.md reports/round-30/handoff/declared-in-r6/twin.json
corpus/knowledge/synthesis/worldbible-integration-contract.md`;
`git log --oneline -3`; `git status --porcelain -- reports/`;
`git show 71cd9d3:examples/culture-d4/typed-labels.d4.yml` (coverage already 82/64/12/6 at round-30 admission,
so the staleness is the round-20 carry, not later drift).
