> 2026-10-18 integrator erratum: the reviews' red measurements (L2-channel fail; adapter selftest 1/4) were pre-repair states — the integrator's L2-family patch and the adapter bytes fix landed after the review seats measured. Re-verified at close: typed gate 19/19 exit 0; adapter selftest green. Defect A correction: greens cited from runs over the untyped packet now name the typed run explicitly. Defect B (two wrong leg names in skill-draft-b) corrected to the legs the gate actually emits.

# R19-D03 — craft analysis 3/3: derivation replay and the text-transform rule

- round: 19 (operator loop 2 of 3, build round 3 of 4; `reports/round-19/claims.json`,
  claim **D**, shard **D03**). Lane: `kotodama-shokunin`.
- assignment (verbatim): "D R19-D01..D03 (craft analysts x3): mine rounds 17-18 D4
  artifacts … for codifiable craft rules: register-scoped slot routing; **derivation replay
  requirements**; the slot-label routing model; **the text-transform rule**.
  reports/round-19/knowledge/analyst-{1..3}.md."
- this file: the **derivation-replay requirement** (machine-readable pattern/output pairs)
  and the **text-transform rule** (never re-serialize foreign content), which are coupled:
  the regex patterns a replay reads are exactly the bytes a round-trip serializer corrupts.
  Siblings: `analyst-1.md`, `analyst-2.md`.
- date: 2026-10-18; readings 11:3xZ. Baseline revision
  `e5718945a1ab0a0c3db955338d2cae77d68fd348`.
- canon: NON-CANON engineering evidence.
- writes: **this file only** + gitignored scratch `.scratch/r19d03/`. Rounds 8–18
  read-only; no tool/packet/baseline byte edited. No commit, no push.
- status: **analysis complete; the replay requirement is delivered and green on the D4
  packet; the text-transform rule is the adapter's architecture with a byte-identity
  control.**

## 0. The rules in one sentence

- **Derivation replay**: a derived form is only checked if the packet declares its rule as a
  **machine-readable `pattern`/`output` pair** with a stable rule id, so a checker can
  **recompute** the form from the base and compare — a derivation that cannot be replayed is
  a `HOLD`, never a pass (`tools/gates/naming-collision-gate.py:1345-1410`).
- **Text-transform**: the typed packet is derived by a **text transform over the assembler's
  bytes**, never by re-serializing foreign content, because the lane's round-trip serializer
  corrupts regex backslashes, booleans and nulls — and D4 is the first culture whose packet
  carries derivations with regex patterns (`tools/assemble-d4-typed.py:296-325`).

## 1. The machine-readable pattern/output pair (delivered data)

`examples/culture-d4/packet.d4.yml` (sha256 `e7ecd204…`) carries
`morphology.derivation_rules` (`:205-226`):

```yaml
morphology:
  derivation_rules:
    - id: "CX-01"
      kind: "compound"
      pattern: "^(?P<a>.+)\\+(?P<b>.+)$"
      output: "{a}{b}"
      note: "STACK-COMPOUND: modifier root before head root …"
    - id: "CX-02"
      kind: "suffix"
      affix: "-ar"
      pattern: "^(?P<stem>.+)$"
      output: "{stem}ar"
    - id: "CX-03"
      kind: "suffix"
      affix: "-en"
      pattern: "^(?P<stem>.+)$"
      output: "{stem}en"
  derivation_note: "the three rules replay the four derived or compound records in this file and the eight names in 05-naming; rule ids match the constructions block"
```

The `constructions` block re-uses the same rule ids (`:995-1030`), and name records point at
them via `rule: "CX-01"` (`:1950`, `:1971`). The **rule id is the join key**; the
`pattern`/`output` pair is the recomputable algorithm.

## 2. The replay leg (executable authority)

`tools/gates/naming-collision-gate.py`, gate C:

1. `_derivation_rules(packet)` (`:1206-1220`) builds an id→rule table from
   `morphology.derivation_rules`; `None` when the packet declares none.
2. `_gate_c` (`:1345-1410`) walks every name record: a name that **claims an etymology but
   declares no formation record or explicit opacity** ⇒ `DERIV-HOLD` — "derivation cannot be
   replayed" (`:1370`); a formation without a stem ⇒ "the rule chain is not replayable"
   (`:1382-1386`); a packet with no `derivation_rules` ⇒ "cannot replay the chain" (`:1403`);
   an unknown `rule_id` ⇒ a finding naming the licensed affixes (`:1409+`).
3. **ReDoS guard**: a packet-authored `formation.pattern` is matched under a wall-clock
   budget (`MATCH_BUDGET_SECONDS = 0.5`, `:1223`; `_MatchBudgetExceeded`, `:1226-1229`) —
   `re.error` covers non-compiling patterns, but catastrophic backtracking compiles, so the
   match itself is budgeted. A replay engine must not trust a packet-authored regex.

**Control (measured this seat, 2026-10-18, `TMPDIR=$PWD/.scratch`):**
`python3 tools/gates/naming-collision-gate.py examples/culture-d4/packet.d4.yml` → exit
**1**, **14** `FINDING`/`NOTE` lines, **0** matching `deriv` (all 14 are `NAME-NEAR`
recall rows) — i.e. every D4 name's declared rule **replayed clean**; the gate's other legs
produce the findings, not the replay.

## 3. The D4 argot derivations (design forecast — mark `(to-verify)`)

`reports/round-17/d4/design-brief.md` §6 Δ3 (`:296-315`) requires quote forms derived from
their plain base by two declared operations, checked via `derived_from` + `derivation`
fields (`D4L-ARGOT-DERIV` in controls only). `reports/round-17/d4/design-language.md` §5
(`:187-217`) fixes the **exact algorithms**:

- **`head2`** — the first two syllables of the base, syllabification **maximal-onset**:
  `saalumi` → `saa.lu.mi` → `saalu` (not `saalum`). The algorithm is stated because the two
  readings disagree, "and a derivation that is not deterministic cannot be checked."
- **`reverse`** — character-level string reversal: `min` → `nim`, `makun` → `nukam`, etc.
  (11 worked derivations, "all recomputed by the checker, all agreeing").
- Design law: "Every numeral was chosen so that its own reversal is a legal D4 form … A
  derivation the language cannot spell is not a derivation, it is a defect."

`reports/round-17/d4/typed-support-1.md:283-284` records the argot-derivation check as a leg
the D2 engine never carried; no delivered D4 byte carries a `D4L-ARGOT-DERIV` row
(`grep -c "ARGOT-DERIV" examples/culture-d4/packet.d4.yml` → 0). The forecast half must be
labelled `(to-verify)` in any codification.

## 4. The text-transform rule (executable authority)

`tools/assemble-d4-typed.py` (`:296-325`), docstring verbatim:

> Derive the typed packet by TEXT transform, never re-serializing foreign content: the
> round-trip serializer corrupts regex backslashes, booleans and nulls (D4 is the first
> culture whose packet carries derivations with regex patterns). Only the costume `garment`
> key is renamed (moved), and the adapter-owned blocks (schema/typed_channel/typed_assembly/
> findings) are appended, serialized from adapter-generated data alone.

Mechanism:

1. Walk the packet **text line by line**; inside the `costumes` block, rename `garment:` →
   `garment_gloss:` by regex substitution (`:304-316`) — a byte-level rename, not a parse
   and re-emit.
2. Append the adapter-owned blocks (`schema`, `typed_channel`, `typed_assembly`,
   `pipeline_findings`, `pipeline_counts`) serialized from adapter-generated data alone
   (`:317-325`).
3. **Determinism control**: `build()` runs `text_payload` twice and refuses if the two
   builds differ (`:367-370`), and `--check` byte-compares against the committed typed packet
   (`:529-536`).

`SCORECARD.md:185` records the same class as an unclaimed calibration observation: "the
serializer round-trip corruption class recorded (D4 first culture with derivations)". The
trigger is visible in the delivered bytes: the CX-01 pattern carries a backslash
(`packet.d4.yml:209 pattern: "^(?P<a>.+)\\+(?P<b>.+)$"`) — precisely the byte class a
parse-and-re-emit serializer mangles.

**Control (measured this seat, 2026-10-18):**
`python3 tools/assemble-d4-typed.py --check examples/culture-d4/packet.d4.typed.yml` →
exit **0**, `byte-identical deterministic typed packet`; the adapter's `--selftest` carries
build / determinism / `--check` / tamper plus stale-projection, coverage-gap and
malformed-packet controls (`assemble-d4-typed.py:397-497`).

## 5. Codifiable craft rules (for the D-axis SKILL.md decision-table row)

| # | rule | citation | control |
|---|---|---|---|
| R12 | A derived form is checked only if its rule is a **machine-readable `pattern`/`output` pair** with a stable id; the rule id is the join key between the rule table and the records. | `packet.d4.yml:205-226`, `:995-1030`; `naming-collision-gate.py:1206-1220` | naming gate over D4 packet: exit 1, 0 `deriv` findings (§2) |
| R13 | A derivation that **cannot be replayed** (no formation record, no stem, no rule table, unknown rule id) is a `HOLD`, never a pass. | `naming-collision-gate.py:1370`, `:1382-1386`, `:1403`, `:1409+` | the gate's `DERIV-HOLD` findings themselves |
| R14 | A packet-authored regex is matched under a wall-clock budget — `re.error` is not enough against catastrophic backtracking. | `naming-collision-gate.py:1223-1240` | `_MatchBudgetExceeded` raises on over-budget matches |
| R15 | A derivation must be **spellable**: a derived form that the declared inventory cannot spell is a defect, not a derivation. | `design-language.md:198-217` | the 11 worked derivations, "all recomputed by the checker" |
| R16 | Derive a typed packet by **text transform over the assembler's bytes**; never re-serialize foreign content, because the round-trip serializer corrupts regex backslashes, booleans and nulls. Append adapter-owned blocks from adapter-generated data alone. | `assemble-d4-typed.py:296-325`; `SCORECARD.md:185` | `--check` byte-identity (`:529-536`) + two-build determinism (`:367-370`) |
| R17 | Rename (move) a field by byte-level substitution inside its block, not by parse-and-re-emit; the moved field must survive the round trip. | `assemble-d4-typed.py:304-316` | adapter selftest `:467-477` (moved field present, original gone) |

## 6. Forecast vs delivered

- **Delivered**: R12–R14, R16, R17 — the CX-01..03 rule table, the naming gate's replay leg
  (green over D4), the adapter's text-transform architecture with byte-identity control.
- **Forecast (mark `(to-verify)`)**: R15's argot derivations (`head2`/`reverse`,
  `D4L-ARGOT-DERIV`) are design-brief Δ3 / design-language §5; no delivered D4 byte carries
  a `D4L-ARGOT-DERIV` row or an `ARGOT` token.

## 7. Destination

- **D-axis SKILL.md**: a decision-table row under the derivation/naming area — condition =
  "a record claims a derived or compound form", routing = declared `pattern`/`output` pair +
  rule id, check = replay (recompute and compare), consequence = unreplayable ⇒ HOLD; and a
  companion row for the serializer: "the typed packet is derived by text transform, never by
  re-serializing foreign content."
- **Corpus lesson**: the D4 lesson entry records the corruption class (regex backslashes,
  booleans, nulls) with the `--check` control, and the replay requirement with the naming
  gate citation.

## 8. Limits

- Readings bind to the shas/stamps above; a later edit to the packet, adapter or naming gate
  is a re-read event.
- The argot-derivation half is design-forecast (R15), not delivered; the codification must
  mark it `(to-verify)`.
- "The serializer corrupts X" is the adapter docstring's and `SCORECARD.md:185`'s claim
  (corroborated by the delivered backslash in the CX-01 pattern); this seat did not re-run a
  round-trip serializer to reproduce the corruption, and does not present it as re-measured.
