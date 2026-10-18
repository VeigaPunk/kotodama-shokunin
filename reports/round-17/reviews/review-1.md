# R17-D33 — reviewer: D4 internal consistency

- **Seat:** R17-D33 (reviewer, claim D `culture-d4-assembly`), round 17 (operator
  loop 2 of 3, build round 1 of 4; 64 declared workers, `opencode-go/deepseek-v4.1-flash`).
- **Assignment (verbatim):** "D4 R17-D33..D37 (reviewers x5): internal consistency;
  language sketch soundness; myth-costume coupling; hold-set hand re-derivation;
  D2/D3-lesson cross-check. reports/round-17/reviews/review-<n>.md."
- **Date / clock:** 2026-10-18, stamps local (-03:00) and UTC where stated; this
  file's measurements ran 09:4x–09:5xZ. The wave was **in flight** while this
  file was written; every statement is pinned to the digests in §1.
- **Write scope:** this file only, plus in-lane scratch under `.scratch/r17-review/`
  (`TMPDIR=$PWD/.scratch` exported before every scratch-writing command). No tool,
  component, packet, corpus, or filed round-8–16 byte was written; no commit, no
  push. Every mutation control ran in an isolated mirror under `.scratch/`.
- **Canon:** NON-CANON engineering review. Nothing here is canon, a lore receipt,
  a handoff, or a real-world clearance/rights statement. All reviewed artifacts
  are NON-CANON.

## 0. Verdict

**The delivered D4 tree is internally consistent at the record level, with two
minor component-level bookkeeping defects (F1, F2) and three recorded
normalizations (N1–N3).** The 12-component registry lands exactly; the assembled
packet is byte-deterministic (my own mirror build reproduces the delivered packet
byte-for-byte); every id-shaped cross-reference resolves to a declared id or
names its owning component; the costume/material/era/rank/myth couplings resolve
mechanically; no duplicate record id exists in the packet. The typed chain
(`typed-labels.d4.yml`, `packet.d4.typed.yml`, `expected-holds.json`, the D4 typed
tools, a round-17 frozen manifest) is **not landed** at this stamp — the typed
consistency legs are therefore unevaluable here and are covered in review-4
(R17-D36) and review-5 (R17-D37).

| # | severity | finding | owner of the disposition |
|---|---|---|---|
| F1 | low | `02-phonology.yml` self-contradiction: its `follows` F-2 text says "codas limited to four consonants" while its delivered data declares **eight** | D06 / parent |
| F2 | low | `04-lexicon.yml` `coverage_notes` counts are stale against its own delivered lexicon (fields 49 vs 54; routes root 44 vs 43 + 1 lexicalized) | D07 / parent |
| F3 | low | `06-myth.yml:19` refers to "the register component" — a component the landed 12-component registry does not contain (stale weigh-court reference) | D11 / parent |
| F4 | low | two rank/office terms used in delivered records are not declared anywhere: `broker` (GAR-06, RK-04) and `weigh-master` (SYM-06) | D14 / parent |

## 1. Subject under review, stamped

HEAD `9b49a4a0fca6ceeab917d401945358fdedeb7e11` (round-17 declare; all round-17
work untracked). Digests measured with `sha256sum` at 09:52Z:

| artifact | sha256 |
|---|---|
| `examples/culture-d4/packet.d4.yml` | `2776d85cb2b3f03bf084df3974b3ff59c44b81b0004997c4e4bd830b05335d72` |
| `tools/assemble-culture-d4.py` | `03a0754eec5565aad76598be53de4ba26e0199c81a30814ec88e87e31951f466` |
| `examples/culture-d4/brief.md` | `00aa85ff6f9959fa8388f6d05a2c074c965e4bf843c27a8969476f3472c5eed2` |
| `examples/culture-d4/ASSEMBLY.md` | `37b6a98901bd4244b166398fecf6d9472b9ac36ed4028fb57b240fd4d44fee2a` |
| `reports/round-17/run-validation.py` | `6b98abadef9951be7cfce006f339dad036f7b341cee6713ecc00be6e5f9095ec` |
| `reports/round-17/d4/design-brief.md` | `a5fdc84dfe3f98e92068e2737f6447c9adec82ff669914b3e22963ee8447e78f` |
| `reports/round-17/d4/design-costume.md` | `77d0fde81dbe59d5dbbeee4450be326f8a948e9e666e3fdc1732873d274515e2` |
| `reports/round-17/d4/design-myth-era.md` | `0e33758b60a7f9d9c39f62844c4d7d1383547c925a779eb9729290dae2a127a2` |
| `reports/round-17/d4/design-language.md` | `cfc2d698559ed552c85b527c3a34e32e4fe308cfd093137483f9d3c782b462cc` |
| `reports/round-17/d4/expected-holds.fragment.json` | `ee0908e108b22feafb014da40851db34c421a5ae91a3e37ff2791d45a266686a` |

If these digests no longer match the tree, the parent must re-run §2–§4 on the
final bytes; this review is stated against the stamped bytes only.

## 2. What was measured

All commands cwd = lane root, `TMPDIR=$PWD/.scratch`, `PYTHONDONTWRITEBYTECODE=1`,
2026-10-18 ~09:45–09:52Z. Helper scripts are scratch-only
(`.scratch/r17-review/{census.py,xref.py,langcheck.py}`); their outputs are the
numbers below.

| # | command | observed |
|---|---|---|
| M1 | `python3 tools/assemble-culture-d4.py --check` | exit 0 — `packet.d4.yml: byte-identical deterministic assembly` |
| M2 | mirror build: copy `assemble-culture-d4.py` + `assemble-d2.py` + reader + the 12 components into `.scratch/r17-review/mirror-a/`, run the assembler there | exit 0 — `Wrote examples/culture-d4/packet.d4.yml (82635 bytes)`; sha256 `2776d85c…35d72` **equals** the delivered packet byte-for-byte |
| M3 | `ls examples/culture-d4/components/ \| wc -l`; registry cross-read | 12 files; the registry's 12 stems (`01-brief`…`12-provenance`) and every registry `packet_keys` entry land in the packet |
| M4 | census (`.scratch/r17-review/census.py`) | packet top keys 33; declared ids **162**; **no duplicate id within any block** (cross-block pairing `ER-01..03` is recorded in N3) |
| M5 | cross-reference resolution (`.scratch/r17-review/xref.py`) | every id-shaped token in the packet and in each component resolves to a declared id, or is an external/lesson id, or names its owning file (`03's OR-01`, `03's WR-07`, `03's LI-03`, `12-provenance (SW-07)`) — **0 dangling references** |
| M6 | coupling matrix (costumes→`material_ref`→materials; materials/rank-rule/symbol/name eras→eras; festivals→roles/rites; narratives↔motifs) | **0 unresolved couplings** (6/6 costumes reference a declared `CMAT-*`; 5/5 materials' route eras declared; 6/6 festivals' `role_served`/`rite` declared) |
| M7 | component duplicate-id census (per file) | packet none; intentional re-use only: `CX-01..03` in `constructions` **and** `morphology.derivation_rules` (04, note: "rule ids match the constructions block"), `ER-01..03` in `named_eras` **and** `era_records` (08), `D4L-FORM-UNRESOLVED` ×6 rows in the hold declaration (01, distinct `where`) |
| M8 | count declarations vs delivered data (grep + recount) | `09-costumes` "Six garments, five materials, two cloth" → 6/5/2 ✓; `05-naming` "eight delivered names" → 8 ✓; `10-ritual-calendar` "six festivals, four rites" → 6/4 ✓; `06-myth` "three narratives" → 3 ✓; **`04-lexicon` `coverage_notes` ✗ (F2)** |

## 3. Findings

### F1 (low) — `02-phonology.yml` contradicts its own coda declaration

- `examples/culture-d4/components/02-phonology.yml:30` (`follows` F-2,
  `decision_followed`): "template written first: (C)V(V)(C); no onset clusters and
  no coda clusters; **codas limited to four consonants**; no word of identical CV
  syllables".
- Same file, delivered data: `coda:` lists **eight** consonants (`:83-91`) and
  `phonotactics_record` (`:118-120`) says "a coda is a single consonant **from the
  eight**; word-final codas are the same eight". The packet's `phonology.coda`
  carries the eight.
- Effect: the component cites a corpus decision it does not follow, in the file
  that other components cite as their phonotactic authority (03's and 05's `XR`
  cross-refs). The gate reads the data (eight), so no gate result is affected.
- Owner: D06 (component 02) / parent. Control: `grep -n "four consonants"
  examples/culture-d4/components/02-phonology.yml` → 0 hits after fix, or the
  coda list reduced to four with the witnesses re-derived.

### F2 (low) — `04-lexicon.yml` `coverage_notes` stale against its own lexicon

- `examples/culture-d4/components/04-lexicon.yml:199` declares
  `fields: {body: 4, kinship: 4, weather: 5, landscape: 5, subsistence: 6, war: 3,
  religion: 5, costume: 3, craft: 7, trade: 7}` — sum **49**; the delivered
  lexicon has **54** records: landscape **6**, craft **10**, trade **8**.
- `:200` declares `routes: {root: 44, compound: 2, derived: 2, borrowed: 6}`;
  the delivered data is `root: 43, lexicalized: 1, compound: 2, derived: 2,
  borrowed: 6` (L-05 `mam` is `route: lexicalized` with a `sense_note`).
- `:201` `layers` **matches** (`native: 48`, Salt-road 4, North-road 2).
- Effect: a reader or tool that trusts `coverage_notes` gets the wrong coverage
  picture (it undercounts the lexicon and misses the lexicalized route). The
  lexicon-coverage gate reads the records, not this note — its exit 0 stands.
- Owner: D07 / parent. Control: recompute the three maps from the delivered
  records; all three must equal the declarations.

### F3 (low) — `06-myth.yml` cites a component the landed registry does not contain

- `examples/culture-d4/components/06-myth.yml:19` (`scope`): "Attributed sayings
  and oath formulas belong to **the register component** and are not written here."
- The landed registry (`01-brief.yml` `registry`) names 12 components —
  `01-brief` … `12-provenance` — and none of them is a register contract; the
  packet carries no `registers`, `oaths`, or `sayings` block (packet top keys,
  review-1 §2 M4). The sentence is a stale reference from the divergent
  weigh-court design (whose registry had `06-register-contract.yml`), left inside
  a delivered component. Effect: a reader of 06-myth is pointed at an owner that
  does not exist; no gate result is affected (myth gate exit 0).
- Owner: D11 / parent. Control: the sentence is reworded to name the landed owner
  of oath/saying material, or the claim is removed; `grep -n "register component"
  examples/culture-d4/components/06-myth.yml` → 0 hits.

### F4 (low) — undeclared rank/office terms in delivered records

- `09-costumes.yml` `GAR-06` and `RK-04` list **`broker`** among `wearer_ranks`;
  `07-symbolism.yml` `SYM-06` names **`weigh-master`** as holder. Neither term
  appears in the brief's ranking rows (`SEED-03`: smith lineages, league council
  of furnace-masters) nor in any declared rank list; the declared costume ranks
  are `smith`, `furnace-master`, `league delegate`, `stamp-holder`, `kiln tender`,
  `charcoal burner`, `market-goer`.
- Effect: the rank vocabulary drifts by two terms that no component owns — the
  costume gate does not check vocabulary completeness, so its exit 0 does not
  cover this. Owner: D14 (costumes) / parent. Control: either declare the two
  offices in the registry/rank vocabulary or replace them with declared terms;
  `grep -rn "broker\|weigh-master" examples/culture-d4/components/*.yml` shows the
  remaining uses.

## 4. Recorded normalizations and observations (no action required by this seat)

- **N1 — block-scalar prose is elided by the assembler, recorded.** The packet's
  `narratives[*].summary` reads `<block scalar elided by tools/assemble-culture-d4.py>`;
  `assembly.block_scalars_elided` records the per-file counts (01:4, 02:2, 03:2,
  04:2, 05:2, 06:5, 07:2, 08:2, 09:2, 10:2, 11:2, 12:2) and
  `assembly.normalizations` names the reason (the stdlib subset reader would read
  indented continuation lines as mapping entries). The components carry the prose;
  the gate-facing packet does not. This is a documented trade-off, not a silent
  drop — but a reader of `packet.d4.yml` alone cannot read the myth summaries.
- **N2 — `eras` is a record list, not a tag list (documented deviation).**
  `packet.d4.yml` `eras` carries mapping records (`id/name/tag/label/span`);
  D2's projector family requires a string tag list (`packet.eras: expected a
  non-empty list of era tags`, measured by R17-D17 and re-recorded in
  `12-provenance` `SW-07`). `08-eras.yml` supplies a flat `era_tags` list for
  consumers that read the D2 shape. Any D4 projector must accept the record
  shape or read `era_tags`; this is an interface constraint on the pending typed
  chain, not an inconsistency in the tree.
- **N3 — intentional id re-use across blocks** (M7): `CX-01..03` (constructions ↔
  derivation rules), `ER-01..03` (named eras ↔ era records), and the six
  `D4L-FORM-UNRESOLVED` rows (distinct `where`) are deliberate, documented
  pairings, not collisions. The packet's own duplicate-id check is clean.
- **O1 — `weigh-master` is an office named once, never declared.** `07-symbolism`
  `SYM-06` names "the weigh-master" as holder; the rank vocabulary in
  `09-costumes`/`05-naming` does not declare that office. See review-3 (R17-D35)
  §couplings for the disposition.

## 5. Limits

- This review did not run the round-17 counting command (it writes
  `reports/round-17/validation.json`, outside this seat's write scope); the D-leg
  status quoted in review-4 is from the O seat's read-only runner snapshot
  (`.scratch/r17-o/validation-check.json`, 06:44 local) plus my own read-only
  re-checks.
- The typed artifacts are not landed at this stamp; every typed-consistency leg
  (hold-set equality, channel differential, pins) is outside this file.
- The tree was moving during the review (components/packet regenerated at
  ~06:44–06:51 local). The pin table in §1 is the contract; a later tree is a
  re-read event.
- No canon, lore, rights, or clearance judgment is made or implied.
