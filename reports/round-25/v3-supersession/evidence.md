# R25-O11..O15 — v3 claim-prose supersession (`declared-in-r4`)

- **Seat:** O, round-25 claims R25-O11..O15 (v3 supersession x5). This seat
  authored none of the lane's filed round 8–24 artifacts.
- **Date:** 2026-10-18. Baseline revision `e06581b7fc2b50050a336f7f38a7e2baebcc6abc`.
- **Writes:** `reports/round-25/v3-supersession/` only (`build-revision.py`,
  `v3-supersession-check.py`, `declared-in-r4/{packet.md,expected.json,freeze.txt}`,
  `evidence/check-receipt.json`, this file). No git commit or push. No filed
  round 8–24 artifact touched. Scratch under `.scratch/` with
  `TMPDIR=$PWD/.scratch`.

## 1. The hazard, measured

The handoff v3 ledger carried stale D4 claim prose. On the live bytes, the r3
revision (`reports/round-23/wording/declared-in-r3/packet.md`, sha256
`084dc5db…`) asserted as D4's **present** state:

| surface | stale statement | live value |
|---|---|---|
| `D4-CL05` (`:150`) | `findings_total 16`, `findings_hold_or_fail 15`, "16 findings of which 15 are hold-or-fail" | 12 findings, all form holds |
| `D4-CL06` (`:151`) | `#counts (hold 15, note 1, fail 0)`, twelve form holds **and three `D2L-RANK` holds, plus one `D2L-RANK` note** | hold 12, note 0, fail 0; 12 rows, all `D2L-FORM-UNRESOLVED` |
| `D4-CL07` (`:152`) | "conflicts (4), quarantine handles (3) … carried as counts" | conflicts 0, quarantine handles 0 |
| `D4-CL09` (`:154`) | "re-carries D2's rank-rule adaptation rows with `adapt_status: cannot-evaluate`", 13 unresolved rank items, 3 quarantine handles, 4 conflicts | packet-native 4 RK rules, zero act rules / residuals / unresolved / quarantine / conflicts |
| `OQ-V3-05` (`:309`) | "twelve form holds + three rank holds + one note, thirteen unresolved rank items, three quarantine handles and four conflicts" | twelve form holds, zero rank holds, zero notes, zero fails |

The round-22 family-clean repair (`reports/round-22/bleed/design.md`,
`impl.md`) removed three inherited D2 rank holds and one D2 rank note from D4
ownership **without resolving them in D2**. The defect was filed by the round-22
re-pin and regression seats (`reports/round-22/bleed/repin.md:26-37`,
`reports/round-22/fixes/regression.md:136`) and survived the round-23 wording
supersession, which reworded exactly one D4-CL08 phrase and touched no D4 claim
prose (`D4-CL05/06/07/09` and `OQ-V3-05` are byte-identical between r2 and r3 —
verified in §4).

## 2. The fix, and why it is this shape

The filed convention for this class is the round-23 disposition pattern, not a
rewrite of filed bytes: a **new** revision directory built from the parent by a
declared delta, pinned by its own `expected.json` and re-verified by a dedicated
checker, with the frozen validators untouched.

`build-revision.py` derives `declared-in-r4/packet.md` from the r3 parent by
exactly **five line substitutions plus one provenance note**, and refuses to run
if any declared old line does not occur exactly once in the parent — so the delta
can never silently drift. Byte-delta proof (control
`byte-delta-is-one-note-plus-five-replacements`): the diff opcodes between parent
and revision are exactly `["insert", "replace", "replace", "replace"]`.

The corrected prose states the family-clean present state and, where the
inherited residual population is named, attributes it to D2 and to the
pre-family-clean generation rather than to D4's present state — so the correction
removes the misattribution without hiding the history. No claim status, row id,
link, count, edge, glossary row or other ledger line is touched; the packet
version stays `3.1.1` because this is a claim-prose revision, not a renderer
build.

## 3. Evidence

All commands ran with `TMPDIR=$PWD/.scratch` and `PYTHONDONTWRITEBYTECODE=1` on
2026-10-18. The isolated clone is `.scratch/r25-o11-clone2` (HEAD
`f74fc9403d4b02c8ee76439eb133e3dea9b65b14`).

### 3.1 Revision identity

- `python3 reports/round-25/v3-supersession/build-revision.py` → wrote
  `declared-in-r4/packet.md`, sha256
  **`5f58db4a52b688568eac054b1c75e9bd110843370a1943cf4353fff75b46aa03`**,
  109,817 bytes from the 107,119-byte parent.
- `expected.json` pins that digest in the `packet_sha256` key (the same binding
  mechanism as `reports/round-20/handoff/expected.json` and the r3 revision),
  names the r3 parent path and digest, records the five-row delta, the reason,
  the preserved census, the v2 subset digest and the live family-clean
  measurements the corrected prose asserts.

### 3.2 Live family-clean measurements (the corrected prose's facts)

`examples/culture-d4/expected-holds.json` — `counts {hold: 12, note: 0, fail: 0}`,
12 rows all `D2L-FORM-UNRESOLVED`, sha256
`3826ba68d705b3c379b2a12737c14075d9095a1ba2aa2eb525de1851a9ecd2f7`.

`examples/culture-d4/typed-labels.d4.yml` — coverage
`{typed_labels 74, findings_total 12, findings_hold_or_fail 12, label_findings_hold 12,
label_findings_fail 0, conflicts 0, rank_rules_unresolved_items 0,
rank_quarantine_handles 0, reconciliation_records 6, rank_rules_component 4,
rank_rules_normalized 4, rank_rules_gate_projected 4}`, `typed_labels.stats
{fail 0, hold 12, labels 74}`, sha256
`60b526b0b3d07141875d20c472451cdf6658f61936d39fe18af4f3d981981092`.

Zero `D2L-RANK` rows in `examples/culture-d4/{typed-labels.d4.yml,
expected-holds.json, packet.d4.typed.yml}` (grep count 0 each).

Alias state **landed** — `tools/d2-typed-labels.py --selftest` 163/163;
`tools/assemble-d4-typed.py --selftest` 12/12;
`tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` exit 0,
`summary: 19/19 legs passed`.

### 3.3 Preserved invariants

- Census **27 rows**, statuses **16 supported / 7 partial / 4 unresolved** —
  unchanged between parent and revision.
- The 15 carried v2 rows are **byte-identical** to the parent's, and the
  baseline's `v2_subset_digest` is the frozen
  `ad35c860acf3b452c6f8974cd08a8333fa1ffd7758b371c12123b6437bde069b`.
- Zero uncertainty-grammar problems under the frozen `PLACEHOLDER_RE` on both
  parent and revision; zero unresolved claim links on the revision.
- `D4-CL09` keeps status `unresolved` and its `owner: kotodama`;
  `OQ-V3-05` still references `D4-CL09`.

### 3.4 Checker controls (`v3-supersession-check.py`)

`--selftest` → exit 0, **44/44 controls** (receipt
`evidence/selftest-receipt.json`). The full `--check` arm adds the frozen-runner
arms and ends at **52/52** (receipt `evidence/check-receipt.json`). Highlights:

- `revision-is-parent-plus-declared-delta` — the filed revision equals the
  builder's rebuild from the filed parent.
- `builder-refuses-mutated-parent` / `builder-refuses-drifted-old-line` — a stray
  byte or a drifted old line makes the builder refuse rather than emit a silent
  delta.
- `stale-detector-fires-on-parent-five-rows` — the detector catches all five
  surfaces on the parent.
- `stale-detector-clean-on-revision` — none on the revision.
- `stale-detector-spares-d2-owned-residuals` — `OQ-V2-03`, which legitimately
  names D2's **own** 13 unresolved rank items / 3 quarantine handles / 4
  conflicts, is untouched and not flagged.
- `residual-mentions-carry-d2-attribution:{D4-CL09,OQ-V3-05}` — where the
  revision still names the inherited population, it carries explicit D2/removal
  attribution.
- `filed-rounds-8-24-unchanged` — the snapshot before/after the full run is
  byte-identical.

### 3.5 Frozen verify (the r3 successor check re-run)

`python3 reports/round-23/wording/wording-check.py --root .scratch/r25-o11-clone
--check` → exit 0, **17/17 controls**; the r3 revision and its pin are intact and
the frozen runner/adapter digests still match. This is the "frozen verify green"
requirement: the r3 check is unaffected by a new sibling revision.

### 3.6 The frozen runner over the new revision

`v3-supersession-check.py --root .scratch/r25-o11-clone2 --check` binds the
**unmodified** frozen round-20 runner (digest `2b7a252b…`) and the round-22
selector adapter (digest `2856a571…`) to the r4 revision via the successor
binding:

- **Positive arm** (r4 pin): the run parses `declared-in-r4/packet.md`, 27 rows,
  statuses 16/7/4, zero uncertainty findings, `v2_subset=equal`,
  `alias_leg=landed`, and **zero** findings against any D4 claim row or
  `OQ-V3-05`.
- **Negative arm** (r3 pin): the same runner over the r3 revision reports **no**
  finding against the stale D4 prose — the defect is not validator-detectable,
  which is exactly why the round-22 re-pin seat had to file it by content review.
  The detector sees it; the frozen grammar check does not. Both facts are
  asserted, so neither the validator's blindness nor the detector's power is
  assumed.
- Remaining failures in both arms are **exactly** the two open tails inherited
  from the round-23 successor check — the v2 successor row's projector re-pin
  and the v3 baseline pin re-point (the frozen round-20 baseline still pins the
  pre-round-22 packet) — both owned by other seats. This seat neither owns nor
  claims them; `positive-control-remaining-failures-are-inherited-open-tails-only`
  fails if any other failure appears.

## 4. What this seat did not do

- No round-8–24 artifact was edited. The `reports/round-20/handoff/claims-map.md`
  (the renderer's immutable claim source) is untouched, so a future renderer
  build will still copy the old rows until a renderer owner issues a new claim
  map — that is a named follow-up, not a claim of this seat.
- No renderer, profile, frozen row, `SKILL.md`, or shared bookkeeping was
  changed.
- The two inherited open tails are not resolved or waived here.

## 5. Follow-ups for the parent integrator

1. A renderer/claim-map owner must issue a superseding D4 claim map (or an
   equivalent renderer-side source) so a freshly rendered packet carries the
   corrected rows natively; this revision corrects the filed ledger, it does not
   change `tools/exercise-handoff-e2e.py`'s `CLAIMS_MAP` selection.
2. The v2 successor row projector re-pin and the v3 baseline pin re-point remain
   open (inherited from round 23).
