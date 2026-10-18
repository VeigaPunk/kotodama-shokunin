# R17-D36 — reviewer: D4 hold-set hand re-derivation

- **Seat:** R17-D36 (reviewer, claim D `culture-d4-assembly`), round 17 (operator
  loop 2 of 3, build round 1 of 4; 64 declared workers, `opencode-go/deepseek-v4.1-flash`).
- **Assignment (verbatim):** "D4 R17-D33..D37 (reviewers x5): internal consistency;
  language sketch soundness; myth-costume coupling; hold-set hand re-derivation;
  D2/D3-lesson cross-check. reports/round-17/reviews/review-<n>.md."
- **Date / clock:** 2026-10-18, local -03:00; measurements 09:4x–09:57Z. Wave in
  flight; statements pinned to the digests in review-1 §1 (packet `2776d85c…35d72`)
  and to the filed reports cited below.
- **Write scope:** this file only, plus scratch under `.scratch/r17-review/`
  (`TMPDIR=$PWD/.scratch` set). No artifact under `examples/`, `tools/`,
  `reports/round-{8..16}/`, or `corpus/` was written; no commit, no push.
- **Canon:** NON-CANON engineering review. Nothing here is canon, a lore receipt,
  a handoff, or a real-world clearance/rights statement.

## 0. Verdict — what could and could not be re-derived by hand

**The hold set's record-level basis re-derives cleanly; the typed equality itself
is unevaluable at this stamp because the typed chain is not landed.** Concretely:

- **Re-derived (pass):** the declared hold set is named pre-implementation, and
  its basis exists in the delivered bytes exactly once per record — 6 costumes
  `GAR-01..06`, each with `form_slot LEX-GAR-0n`; 6 `form_slots` records
  `LEX-GAR-01..06` with `status: unfilled`, `owner: GAR-0n`; the legacy naming
  gate emits **exactly 6** `PHON-INVENTORY` FAIL lines naming those six glosses
  (my run) — so the minus-basis of the typed channel differential is identified
  1:1 with the six declared holds. The runner's D8 leg (ids/wheres named in
  design docs) passes for this set (my read-only check of
  `reports/round-17/d4/**/*.md`).
- **Unevaluable (blocked):** the typed packet, the projection, the expected-holds
  file and the D4 typed tools **do not exist** at this stamp. The equality leg
  (emitted findings == expected set), the determinism leg (two adapter builds)
  and the pins leg cannot be re-derived by hand or by tool; the D2 projector is
  **measured refusing** the delivered packet (exit 2, `packet.eras: expected a
  non-empty list of era tags`, my run 09:56Z, reproducing R17-D17's filed run).
  The replay leg, by contrast, **can now be measured and is green**: the
  round-17 frozen manifest landed (`reports/round-17/tests/frozen/MANIFEST.tsv`,
  6 rows over packet `2776d85c…35d72`) and my replay run at 09:58:46Z
  (`TMPDIR=/tmp`) reports `REPLAY OK: 5/5 rows reproduced`, exit 0.
- **Divergence (reported, not repaired):** two competing pre-implementation
  declarations exist — the delivered registry's **6 holds / 0 notes / 0 fails**
  (`D4L-FORM-UNRESOLVED` @ `GAR-01..06`) and the D19 fragment's **17 / 1 / 0**
  (weigh-court ids `GD-*/AL-*/RG-*/SM-03`). The delivered tree, its brief, its
  contract, and the runner's D8 leg are all consistent with the **6/0/0** set;
  the fragment names the divergent weigh-court brief and carries null pins.
  `ASSEMBLY.md` §6 and `typed-run.md` §7(3) report the divergence. The parent
  must record which declaration is authoritative before the equality leg can
  mean anything.

| # | severity | finding | owner |
|---|---|---|---|
| F6 | **high (claim D)** | typed chain absent: typed packet / projection / expected file / D4 projector+adapter+gate; equality, determinism and pins legs unevaluable; D2 projector refuses the packet (eras shape) and cannot emit the declared set (12 label holds + D2 rank rows, measured); replay leg now green (round-17 manifest, 5/5) | parent / D-typed seats |
| F7 | medium | two pre-implementation hold-set declarations (6/0/0 registry vs 17/1/0 fragment); no reconciliation record choosing one | parent |

## 1. The declared set, and its record-level re-derivation

Declared set (three independent locations, all agreeing):

1. `examples/culture-d4/components/01-brief.yml` `contract.hold_set_declaration`
   — `counts {hold: 6, note: 0, fail: 0}`; 6 rows `D4L-FORM-UNRESOLVED` @
   `GAR-01..GAR-06`, each with its reason ("label_id LEX-GAR-0n has no supplied
   native/borrowed form").
2. `examples/culture-d4/brief.md` §"Named hold set (pre-implementation)" — the
   same 6/0/0, naming `LEX-GAR-nn` slots.
3. `examples/culture-d4/ASSEMBLY.md` §4 — the same, with the legacy-run witness.

Hand re-derivation from delivered records (my checks, 09:45–09:51Z):

| step | command / read | observed |
|---|---|---|
| costumes | packet `costumes` | 6 records `GAR-01..06`, each `form_slot: LEX-GAR-0n` |
| owed slots | packet `form_slots` | 6 records `LEX-GAR-01..06`, `status: unfilled`, `kind_owed: native-form`, `owner: GAR-0n` |
| minus-basis | `python3 tools/gates/naming-collision-gate.py examples/culture-d4/packet.d4.yml` | exit 1; **exactly 6** `PHON-INVENTORY` lines, one per `GAR-0n` gloss; plus `NAME-NEAR` REVIEW and `CROSS-HOLD` HOLD (neither is a routing candidate) |
| pre-implementation naming (runner D8) | read-only `id_boundary` check over `reports/round-17/d4/**/*.md` | `D4L-FORM-UNRESOLVED` named; `GAR-01`…`GAR-06` each named (design-costume.md's reconciled wardrobe table; design-brief.md's reconciliation table) → **D8 satisfiable** for this set |
| 1:1 coupling | cross-read of the three declarations against the two records above | 6 costumes ↔ 6 slots ↔ 6 declared holds ↔ 6 legacy FAIL lines — one hold per owed record, no orphan |

**This is a record-level derivation only.** It establishes that the declared set
is well-founded and singular; it does **not** establish that any typed run emits
it. That is F6.

## 2. What the typed chain would have to emit — and what is measured instead

- **The D2 projector cannot be the D4 projector.** My run (09:56Z):
  `python3 tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml
  --json` → `exit 2`, `packet.eras: expected a non-empty list of era tags`
  (D4's `eras` is a record list; D2 requires tags). This reproduces R17-D17's
  filed run (`reports/round-17/d4/typed-run.md` §0, §4).
- **Even with the eras shape normalized, the pinned engine does not emit the
  declared set.** R17-D17's filed diagnostic (typed-run.md §5, scratch-only,
  cited as their measurement, not mine) reports: label leg 74 labels,
  `{fail: 0, hold: 12}` — 6 `D2L-FORM-UNRESOLVED` @ `GAR-01..06` **and** 6 more
  @ `LEX-GAR-01..06` (from the packet's own `form_slots` block, which D2's packet
  does not carry); rank leg adds D2's constant 4 rows (`WR-02#g|WR-09#g`,
  `WR-08#g|WR-09#g`, `TR-04#a|TR-06#a`, note `SR-01#a|SR-01#b`). The declared set
  is 6 holds with **no** `LEX-GAR-*` `where`s and no rank rows.
- **Consequences for the D4 projector (requirements, not repairs):** accept the
  `eras` record shape (or read `era_tags`, which `08-eras.yml` supplies); emit
  **one** hold per owed costume record (do not double-count `form_slots`);
  omit or D4-bind the rank leg; emit the ids and `where`s the declared set names
  (`D4L-FORM-UNRESOLVED` @ `GAR-0n`), with details pinned to the emitted text.
  `design-brief.md` §9.1 names `tools/d4-typed-labels.py` +
  `tools/assemble-d4-typed.py`; neither exists (`ls tools/ | grep -i d4` →
  `assemble-culture-d4.py` only).
- **No expected file, no typed packet, no manifest.** `examples/culture-d4/`
  contains `brief.md`, `README.md`, `ASSEMBLY.md`, `components/` (12),
  `packet.d4.yml` — and nothing typed; no `tools/gates/frozen/round-17*/`,
  no `reports/round-17/**/MANIFEST.tsv`, no `examples/culture-d4/**/MANIFEST.tsv`
  (globs the round-17 runner searches). The runner's D-leg at this stamp is
  therefore red for missing artifacts (plus, before the 06:5xZ brief.md
  rewording, a false clearance-positive — see review-5 F8).

## 3. Findings

### F6 (high, claim D) — the typed chain is not landed; the equality leg is unevaluable

- Missing: `examples/culture-d4/typed-labels.d4.yml`, `packet.d4.typed.yml`,
  `expected-holds.json`; `tools/d4-typed-labels.py`, `tools/assemble-d4-typed.py`
  (and any D4 gate entry point).
- Landed since the first draft of this finding: the round-17 frozen manifest
  (`reports/round-17/tests/frozen/MANIFEST.tsv`) — it replays green, 5/5 rows,
  exit 0 (my run 09:58:46Z, `TMPDIR=/tmp`). The replay leg is therefore measured
  green at this stamp; the equality, determinism and pins legs remain blocked.
- Measured blockers (mine, plus R17-D17's filed run): the D2 projector refuses
  the delivered packet (exit 2, eras shape); the pinned engine's would-be output
  (12 label holds + 4 D2 rank rows, `D2L-*` ids) is not the declared set; the D2
  rank leg is a D2 constant block; the `LEX-GAR-` slot regex crashes on foreign
  prefixes (D17 measured; `tools/d2-typed-labels.py:449`).
- Owner: parent / D-typed seats. **Controls to run when the chain lands** (fixed,
  read-only, `TMPDIR=$PWD/.scratch` except replay which needs `TMPDIR` outside the
  repo):
  1. `python3 tools/d4-typed-labels.py --packet examples/culture-d4/packet.d4.yml --emit examples/culture-d4/typed-labels.d4.yml` then `--check` → exit 0;
  2. two fresh adapter builds byte-compared to each other and to the delivered typed packet;
  3. the D4 gate over `packet.d4.typed.yml` → its printed finding set keyed
     `(id, severity, where)` must equal `expected-holds.json` **both directions**,
     counts `{hold: 6, note: 0, fail: 0}`, details pinned (D17's
     `.scratch/r17d17/compare-holds.py` is the shape);
  4. `python3 reports/round-17/run-validation.py` (writes its own receipt) on the
     settled tree.
  This review does not pre-claim any of these legs green.

### F7 (medium) — two pre-implementation hold-set declarations, one tree

- The D19 fragment (`reports/round-17/d4/expected-holds.fragment.json`, schema
  `kotodama-typed-pipeline-holds-v1`, `named_by` `design-brief.md` §7.1, amendment
  A-19-1) declares **17 holds / 1 note / 0 fails** with weigh-court ids
  (`GD-01..06`, `AL-01..06#plain`, `AL-03`, `RG-02`, `RG-05/06/07/08/09`,
  `SM-03`) and null pins.
- The delivered tree declares **6/0/0** with `GAR-01..06` (brief.md; contract;
  ASSEMBLY.md §4).
- **Both declarations satisfy the runner's D8 leg** (ids/wheres named in
  `reports/round-17/d4/**/*.md`): I checked `D4L-FORM-UNRESOLVED` and
  `GAR-01..06` (present) **and** the fragment's full id/where list —
  `D4L-REGISTER-UNRESOLVED`, `D4L-BORROW`, `D4L-ERA`, `D4L-RANK`,
  `D4L-MATERIAL`, `GD-01..06`, `AL-01..06#plain`, `AL-03`, `RG-02`,
  `RG-05#a|RG-07#a`, `RG-06#a|RG-09#a`, `SM-03`, `RG-08#a|RG-08#b`, `QN-01` —
  all present in the .md docs (design-brief.md §7.1 and the reconciled tables).
  D8 therefore does not discriminate between the two declarations; the
  **equality leg will** (the delivered records — 6 costumes, 6 owed
  `LEX-GAR-0n` slots, one hold per record — match the 6/0/0 set, not the 17/1/0
  set, whose `GD-*`/`AL-*` records do not exist in the delivered packet).
- Owner: parent. Disposition needed: record the fragment as **superseded** by the
  landed registry (recommended: the tree's brief/contract/ASSEMBLY.md are the
  operative declaration, and the fragment keeps its role as the weigh-court
  design record), or amend the registry — but do not let both stand as live
  declarations. When `expected-holds.json` lands, its details must come from the
  emitted run (never guessed) and its pins from delivered bytes; the fragment's
  own `pins_note` correctly leaves `projector_sha256` null for the runner's pin
  semantics.

## 4. Limits

- This seat did not run the round-17 counting command (it writes
  `reports/round-17/validation.json`, outside this seat's write scope); the
  runner-side statements above are read-only observations of its discovery globs
  and the O seat's filed snapshot (`.scratch/r17-o/validation-check.json`, 06:44
  local), plus my own re-checks.
- R17-D17's §5 diagnostic is cited as **their** measurement; I reproduced only
  the refusal (exit 2) and the record-level basis, not the 12-hold diagnostic.
- The typed chain may land after this stamp; every leg above is a re-run event,
  not a verdict about a later tree.
- No canon, lore, rights, or clearance judgment is made or implied.
