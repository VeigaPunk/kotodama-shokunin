# Round-24 SKILL audit 2 — typed-pipeline + handoff rows (non-author verifier)

- Seat: D-skill-audit 2 of 4 (label typing / claim uncertainty / slot-label
  routing / derivation replay / family-clean projection). This seat authored
  none of the lane's artifacts in rounds 8-23.
- Date: 2026-10-18. Claim baseline `b5d9844`; HEAD at audit start `8fbcee9`
  (round-24 declare). Tools and gates are unchanged in the working tree
  (`git status`: only SKILL.md modified) — all tool re-runs below are the
  `8fbcee9` bytes.
- Bytes audited for SKILL.md itself: the working tree **as it stood when this
  audit closed**, which includes fixes F1-F4 landed mid-audit by the audit-3
  fixer seat (`reports/round-24/audit-fixes.md`). Every F-fix was independently
  re-derived by this seat BEFORE reading that file's controls, and its controls
  were then re-checked; deviations are recorded in §5. Line numbers cited for
  SKILL.md rows are valid at audit time; rows at or above the T3 bullet
  (`:171`) also match the `8fbcee9` numbering for lines ≤171.
- Method: every executable claim in the five audited tables was re-run against
  the current tools today; every in-repo `path:line` citation was re-resolved
  against current bytes; every corpus `file:line` grounding of an audited rule
  was opened and read. Scratch: `TMPDIR=$PWD/.scratch` (the one exception: the
  frozen replay refuses an in-repo mirror root by design and was run with an
  external mktemp TMPDIR, deleted after).
- Verdicts: **VERIFIED** (re-run green today; citation exact) ·
  **VERIFIED-CITE-DRIFT** (behavior holds; a line/section anchor drifted) ·
  **STALE-MEASUREMENT** (dated "measured:" sentence superseded by later landed
  state) · **DANGLING-ANCHOR** (named tool symbol absent from all tools) ·
  **OPEN** (defect present in current bytes, no fix or erratum landed).

## 1. Verdict summary

| SKILL.md section (rows audited) | Verdict  re-measured live 2026-10-18 |
|---|---|
| Label typing — translated labels, native forms, borrowed strata (6 rows + T1-T5 + 3 cautions) | VERIFIED (behavior; all 6 rules enforced by `tools/d2-typed-labels.py`, selftest 163/163 re-run)  re-measured live 2026-10-18 |
| Claim uncertainty typing — supported/partial/unresolved (3 rows + crosswalk + cautions + duplicate block) | VERIFIED (grammar executable in `tools/harness/packet_uncertainty.py`, selftest 19/19; dated claims re-measured) — one OPEN mis-cite (`worldbible-integration-contract.md:183`) and one structure observation (duplicated status table)  re-measured live 2026-10-18 |
| Slot-label routing (6 rows + T1-T4) | VERIFIED after F1 (T3 anchors fixed-with-control, independently verified); one sub-cite still OPEN (`holds.md` §4.2 does not exist)  re-measured live 2026-10-18 |
| Derivation replay (11 rows + T1-T4) | VERIFIED after F2/F4 (determinism anchor fixed; Passenger-rows erratum landed and confirmed) — F2's cause attribution imprecise (§5.3)  (evidence: re-measured live 2026-10-18; commands in audit-typed.md §3) |
| Family-clean projection (7 paired controls + T1-T4 + injection warning + round-25 commitment) | VERIFIED (all control anchors resolve; selftest boundary matrix green; frozen replay 3/3; deployed replay evidence intact)  (evidence: re-measured live 2026-10-18; commands in audit-typed.md §3) |

## 2. This seat's re-measurements (independent, before reading audit-fixes.md)

| # | Command | Result (2026-10-18) |
|---|---|---|
| M1 | `python3 tools/d2-typed-labels.py --selftest` | exit 0 — `163/163 checks passed`; boundary controls printed live (malformed rank sets fail closed; D2 baseline digest kept; same-id foreign label refused; borrow ledgers unchanged)  re-measured live 2026-10-18 |
| M2 | `python3 tools/harness/packet_uncertainty.py --selftest` | exit 0 — `19 checks passed (uncertainty rules, boilerplate, oq routing, yaml_lines dialect compact+bare)`  re-measured live 2026-10-18 |
| M3 | `python3 tools/assemble-d4-typed.py --check examples/culture-d4/packet.d4.typed.yml` | exit 0 — `byte-identical deterministic typed packet`  re-measured live 2026-10-18 |
| M4 | `python3 tools/assemble-d4-typed.py --selftest` | exit 0 — `12/12 checks passed` (build/determinism/--check/tamper + stale-projection, coverage-gap, malformed-packet controls; routing rows: "the owed slot is named on the slot's own row, once")  re-measured live 2026-10-18 |
| M5 | `python3 tools/gates/typed-pipeline-gate.py` (default D2) | exit 0 — `16/16 legs passed` incl. `L3-routing-consistency`, `L4-pins`  re-measured live 2026-10-18 |
| M6 | `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` (the frozen manifest's own command) | exit 0 — `19/19 legs passed`, all L1/L2/L3/L4 legs ok, 12 `D2L-FORM-UNRESOLVED` holds (= frozen expected set), `channel: 6 PHON artifact(s) retired, 0 added, retained lines identical`  re-measured live 2026-10-18 |
| M7 | `TMPDIR=<mktemp outside repo> python3 tools/replay-frozen.py tools/gates/frozen/round-22/d4-repin/MANIFEST.tsv` | exit 0 — `3/3 rows reproduced` (typed-labels-check 0/0; d4-assembly 0/0; typed-pipeline-gate 0, count 12/12; all bytes match)  re-measured live 2026-10-18 |
| M8 | `python3 tools/d2-typed-labels.py --check examples/culture-d4/typed-labels.d4.yml` (alone) then `--packet examples/culture-d4/packet.d4.yml --check …` (named pair) | alone: exit 1 `differs from the deterministic projection` (false difference — tool defaults to the D2 packet); named pair: exit 0 `byte-identical`. Reproduces the "Named inputs" row's measured claim exactly (SKILL, Derivation replay row 2)  re-measured live 2026-10-18 |
| M9 | `grep -ci uncertainty tools/gates/handoff-packet-check.py`; `sed -n '651p' …` | `0`; five-column fixture ledger `record_id/kind/statement/provenance/evidence_status` — the "no uncertainty column anywhere" defect rows re-verified  re-measured live 2026-10-18 |
| M10 | json load `examples/culture-d4/expected-holds.json` | keys `counts, holds, notes, packet_sha256, projection_sha256, projector_sha256, schema, revision_note, supersedes_pins`; counts `hold:12, note:0, fail:0`; zero `D2L-RANK`, zero `TR-04`  re-measured live 2026-10-18 |
| M11 | json load `tools/gates/typed-pipelines.json`; `reports/round-22/bleed/evidence/deployed-replay.json` | schema `kotodama-typed-pipelines-v1`, profile id `d4`, every field digest-pinned, `repin_history` len 3 (`[2]` = round-22 14:53:59Z, projector `2819f687…`); deployed replay: 33 `peer_snapshot_pairs_checked`, `live_peers_checked: true`, 2026-10-18T14:56:01Z |
| M12 | `python3 tools/check-gate-battery.py` (default roots) | exit 0 (independent confirmation of fix F3's control)  re-measured live 2026-10-18 |
| M13 | live packet sha `examples/culture-d4/packet.d4.yml` | `e7ecd2045ef0e5f9…` — equals the profile pin and the frozen manifest input pin  re-measured live 2026-10-18 |

## 3. Row-by-row results

### 3.1 Label typing (SKILL.md "Label typing" table, 6 rows)

| Rule (row) | Verdict | Evidence  re-measured live 2026-10-18 |
|---|---|---|
| Reader-facing gloss → `translated-label`, never on the sound/identity channel | VERIFIED | selftest M1 (`live packet: the ten GAR costume labels are typed translated-label`, `tools/d2-typed-labels.py:3183`); finding class `D2L-FORM-UNRESOLVED` in `FINDING_CLASSES` (`tools/d2-typed-labels.py:419-422`); grounding `era-language-staging.md` §7 "type every label" at `:111` (range 108-124 opened and read)  re-measured live 2026-10-18 |
| Supplied native form → sound+identity checked; translation claim cannot waive (native bytes govern, still FAIL) | VERIFIED | supplied-form grouping `tools/d2-typed-labels.py:793-798` (two supplied sound forms on one record = identity collision FAIL); selftest M1 live-packet typing cases  re-measured live 2026-10-18 |
| Sound kind declared, no bytes → `D2L-FORM-UNRESOLVED` HOLD, never clean | VERIFIED | `:808-814` `_fail(findings, D2L_FORM, …, hold=True)` both branches (no supplied form; no label_id and no gloss); M6: 12 holds emitted, gate green only because the expected set is exactly those holds  (evidence: re-measured live 2026-10-18; commands in audit-typed.md §3) |
| ≥2 borrowed-strata discriminators → `borrowed-strata` with borrow-ledger checks | VERIFIED | T3 discriminator source `loanword-material-dating.md:43-57` read (ultimate etymon vs immediate donor vs carrier; recurring correspondences; dated witness; register partition) — matches the five house discriminators; selftest `two loan records are typed borrowed-strata` (`:3200`) and `substitutions that do not derive the form are D2L-BORROW` (`:3282`)  re-measured live 2026-10-18 |
| Exactly 1 discriminator → `to-verify`, never defaulted | VERIFIED | selftest `P18 to-verify mapping row holds and cites its row id` (`:2208`); era `(to-verify)` mapped-unconfirmed, never promoted (`:3314`)  (evidence: re-measured live 2026-10-18; commands in audit-typed.md §3) |
| Untyped legacy record → unchanged channel, still checked | VERIFIED | SKILL.md:47 (sed-verified); `TL-02`-behavior present as code (kind never guessed); note: the *name* `TL-02` itself is a DANGLING-ANCHOR — see §5.2 (Error-patterns scope)  re-measured live 2026-10-18 |
| T4 clock separation (executable B4: `entry_stage` < `referent_available_from` ⇒ `D2L-BORROW` FAIL) | VERIFIED | `tools/d2-typed-labels.py:738-742` exact comparison + fail  re-measured live 2026-10-18 |
| T5 WOLD ~24% borrowing / none loan-free | VERIFIED (path imprecise) | `corpus/knowledge/linguistics/language-contact.md:56-62` (not `synthesis/`): "Mean borrowing rate ≈24% … no language in the sample is loan-free" — exact  re-measured live 2026-10-18 |
| Caution "a label is not history" | VERIFIED | `costume-language-coupling-table.md:43` — "A modern curatorial label becomes an attested historical native word" (the exact rejected move)  re-measured live 2026-10-18 |
| Cautions "register is chosen / resists paraphrase" | VERIFIED | `sociolinguistics-registers.md:58`, `:83` — both exact  re-measured live 2026-10-18 |

### 3.2 Claim uncertainty typing (3 status rows + crosswalk + cautions)

| Rule | Verdict | Evidence  re-measured live 2026-10-18 |
|---|---|---|
| Mandatory `grounding:` witness per claim | VERIFIED | `packet_uncertainty.py:213-216` `U-BASIS-NO-GROUNDING` for every status; selftest M2  re-measured live 2026-10-18 |
| `partial` requires `restriction:` | VERIFIED | `:217-220`; `unresolved` requires `open:` + `owner:` `:221-229`  (evidence: re-measured live 2026-10-18; commands in audit-typed.md §3) |
| Basis ≥40 chars, non-boilerplate, unique, must not restate the status token | VERIFIED | `:84` `_is_boilerplate`, `:199-212` (`U-BASIS-SHORT`, `U-BASIS-BOILERPLATE`, `U-BASIS-RESTATES`); design authority v2-design §2.3 exists (`reports/round-15/handoff/v2-design.md:126`)  re-measured live 2026-10-18 |
| Dated claims: "gate has zero uncertainty checks" / "five-column fixture ledger" | VERIFIED | M9 (re-measured today; the row's own date 2026-10-17 remains accurate)  re-measured live 2026-10-18 |
| Crosswalk triage §1 states → statuses | VERIFIED | all 15 cited triage lines opened and exact: `:16` Located, `:17` Inspected, `:18` Scoped-supported ("bounded and revisable, not certainty" — the SKILL quote, verbatim), `:19` Contested, `:21` Unknown, `:32` naked marker, `:70` downgrade, `:76` child claim, `:80` queue state, `:97` confirmed-node, `:100` HARD/SOFT advisory, `:112` `(to-verify)`, `:139` recheck-before-handoff, `:181` unresolved-not-a-verdict, `:182` remainder keeps `(to-verify)`  (evidence: re-measured live 2026-10-18; commands in audit-typed.md §3) |
| Contract cites `:63` (uncertainty in claim_ledger), `:92-106` (§6 separate dimensions), `:100` (canon standing), `:102` (orthogonality), `:104` (legacy labels), `:179` ("silence is not proof of absence") | VERIFIED | all six opened; `:179` carries the phrase at end of line  re-measured live 2026-10-18 |
| Contract cite `:183` for "basis is never boilerplate / unique / witness must resolve" | **OPEN — mis-cite** | `:183` is the delivered-record checklist item ("scope, stable identity, provenance … unknowns are not blank cells"); the contract contains **no** "boilerplate"/"unique"/"witness" basis text anywhere (`grep` empty). The rule itself is executable-verified (above); only this citation is wrong. Candidate erratum: point the basis-hygiene clause at v2-design §2.3 + `packet_uncertainty.py:84,199-212` (or the intended contract line, if one was meant)  re-measured live 2026-10-18 |
| BR05 restriction exemplar | VERIFIED | `reports/round-11/handoff/packet.md:108` carries "Behistun cross-version leg … remain unverified" verbatim in the BR05 row  re-measured live 2026-10-18 |
| Round-12 reject cites (`:9-10,23` shape-gate/digest, `:11` 21/21 digests, `:27-28` no uncertainty dimension / one aggregate edge) | VERIFIED | all opened and exact  re-measured live 2026-10-18 |
| `reports/round-15/claims.json:14` (vocabulary, zero boilerplate) | VERIFIED | line 14 is the `after_required` uncertainty-vocabulary text  re-measured live 2026-10-18 |
| Framework S/C/H/R/U/V stays framework-level; `supported` ≠ `improved` | VERIFIED | `source-discipline-calibration.md:67`; `provenance-audit-ledger-format.md:12` — both exact  re-measured live 2026-10-18 |
| Edge/record status inheritance ("never inherits downward") | VERIFIED (as corpus rule; not claimed executable) | `to-verify-triage-protocol.md:97` exact; `packet_links.py` checks links against the manifest (module docstring `:5-30`) — the harness has no status-inheritance enforcer, and SKILL does not claim one  re-measured live 2026-10-18 |
| Structure observation | OBSERVATION | the three status rows are duplicated verbatim at the tail of Error patterns (sed-verified `:384-:387` at audit time) before the nine uncertainty defect rows. Content-identical today, but two copies must now be kept in sync by hand; recommend the integrator either deduplicate or cross-reference  re-measured live 2026-10-18 |

### 3.3 Slot-label routing (6 rows + T1-T4)

| Rule (row) | Verdict | Evidence  re-measured live 2026-10-18 |
|---|---|---|
| Gloss moved by rename, one routing row, one `FORM-UNRESOLVED` hold; row-set == hold-set (gate-asserted) | VERIFIED | M6: `L3-routing-consistency` ok on the committed D4 contract; gate code `tools/gates/typed-pipeline-gate.py:736-753` exact (cited range matches the check)  re-measured live 2026-10-18 |
| Owed slot = second row naming the slot record (`owed_slot`), one obligation two names | VERIFIED | M6: holds `GAR-01..06` + `LEX-GAR-01..06` = 12 holds for 6 obligations; adapter selftest M4 "the owed slot is named on the slot's own row, once"; six-obligation derivation at `reports/round-18/d4/review-1.md` §0-§1 (exists)  re-measured live 2026-10-18 |
| Register field on-channel → no row | VERIFIED (code) | `moved_field` semantics in the gate (`:567-575`: rows with `off_channel_field: null` are the retained class — D4 register rows)  re-measured live 2026-10-18 |
| Laundered hold → four legs fail | VERIFIED (anchors) | `L3-holds/L3-notes/L3-counts/L3-baseline-set` all present at `typed-pipeline-gate.py:696-734` (cited range exact); neg controls `reports/round-18/d4/neg-1.md` §3.1-§3.2 exist  re-measured live 2026-10-18 |
| Unprovable register class → expectation carries only emitted vocabulary | VERIFIED | M10: expected set == emitted set (12 holds, all `D2L-FORM-UNRESOLVED`); freeze rule `reports/round-17/d4/typed-support-2.md` §2-§4 exist  re-measured live 2026-10-18 |
| Retype-to-native row-disappearance gated on supplied form | VERIFIED (anchors) | `reports/round-18/d4/neg-2.md` §3.1 exists; the emission branch `:808-814` holds until a supplied form exists  re-measured live 2026-10-18 |
| T1 routing predicate = kind (`ROUTED_KINDS = ("translated-label",)`) | VERIFIED | `tools/assemble-d4-typed.py:65` exact  re-measured live 2026-10-18 |
| T2 move is a rename, never a delete | VERIFIED | `text_payload` docstring + rename loop `tools/assemble-d4-typed.py:296-310` (docstring at those lines; the `^(\s*)garment:` loop immediately below — M3/M6 `retained lines identical`); round-trip corruption receipts `SCORECARD.md:176-177,185`, `LOG.md:3252-3253` exact  re-measured live 2026-10-18 |
| T3 one obligation, two record names — anchors | VERIFIED after F1 | before: `:622`/`:793` pointed at the owner-metadata tuple and the supplied-form grouping (this seat's measurement); after: `:639-643` (form_slots projection loop, `_form_slot_label`) and `:808-814` (both `hold=True` emissions) — both verified in current bytes; before-anchors verified true at the round-18 bytes (`git show e571894:tools/d2-typed-labels.py` `:622` = the loop, `:793` = the emission). Fix landed with history preserved  re-measured live 2026-10-18 |
| T3 sub-cite `reports/round-18/d4/holds.md` §4.2 | **OPEN** | `holds.md` headings are §0-§6 only (`grep '^#'`); no §4.2 exists. §4 ("Reconciliation B … 6 holds / 0 notes / 0 fails", `:131`) is the section that carries the content. One-character-class erratum needed  re-measured live 2026-10-18 |
| T4 register is a claim about distribution, not channel | VERIFIED | `sociolinguistics-registers.md:58,83` exact; `era-language-staging.md:114` is inside the "type every label" table (heading `:111`) — anchor acceptable, heading line is the stronger cite  re-measured live 2026-10-18 |

### 3.4 Derivation replay (11 rows + T1-T4)

| Rule (row) | Verdict | Evidence  re-measured live 2026-10-18 |
|---|---|---|
| Assembler identity binds the family's own assembler; foreign packet refused (exit 2) | VERIFIED | `SERIALIZER` at `tools/assemble-d4-typed.py:62`; M4 stale-projection/identity controls; design anchors round-18 `gate/design.md` §1.1/§1.3/§11 exist  re-measured live 2026-10-18 |
| Named inputs: `--check` alone vs named pair | VERIFIED (re-measured) | M8 reproduces the row's measured claim exactly on today's bytes  re-measured live 2026-10-18 |
| Machine-readable expectation (schema, counts, rows, pins) | VERIFIED | M10 keys — matches the row's key list (plus `revision_note`, not claimed otherwise); comparison-key design `typed-support-2.md` §2; gate `:696-734` exact  re-measured live 2026-10-18 |
| Round-trip corruption class / text-transform rule | VERIFIED | M3/M4; `:296-310`; receipts (§3.3 T2)  re-measured live 2026-10-18 |
| Flagless resolution; stale pin refuses exit 2 `L1-profile` | VERIFIED | M6/M13 (profile resolved flaglessly off `assembly.generator`; packet sha equals pin); `typed-pipeline-gate.py:481-485` exact; `typed-pipelines.json` digest-pinned (M11)  re-measured live 2026-10-18 |
| Determinism (`:369`) | VERIFIED after F2 | message now at `:387` (this seat's measurement; `:369` is the assembler-identity early-return); fix landed `:369 → :387` with history note. §5.3 records one imprecision in the fix's cause sentence  re-measured live 2026-10-18 |
| Pre-registration | VERIFIED (anchors) | `review-2.md` §0/§2, `holds.md` §3, anti-circularity §2/§6 exist; M10 shows the landed expectation ≠ a copy of unfiltered output (passengers removed per design, not per output)  re-measured live 2026-10-18 |
| Passenger rows (measured 3 `D2L-RANK` + 1 note, 0 hits) | VERIFIED after F4 | this seat measured the current file first (M10: zero D2L-RANK, zero notes, counts 12/0/0, `supersedes_pins` + `revision_note` present); the landed dated erratum keeps the original sentence and points at the supersession; `analysis.md:101` does carry the 3-holds+1-note context; the 0-hits property still reproduces (fixer's grep control, consistent with M10's zero `TR-04`)  re-measured live 2026-10-18 |
| Freeze-artifact naming | VERIFIED (anchors) | `manifest.md` §6 exists  re-measured live 2026-10-18 |
| T4 (obligations survive cleanup; append-only) | VERIFIED | `expected-holds.json` `revision_note`/`supersedes_pins` (M10); `gate-frozen-run-standard.md:50-78,102-142`, `lessons/round-22.md:19` all resolve  re-measured live 2026-10-18 |

### 3.5 Family-clean projection (7 paired controls + T1-T4 + injection warning + round-25 commitment)

| Rule (row) | Verdict | Evidence  re-measured live 2026-10-18 |
|---|---|---|
| Family dispatch before label construction (`build_payload()` only when `family == DEFAULT_FAMILY`) | VERIFIED | `tools/d2-typed-labels.py:2837-2838` exact; `DEFAULT_FAMILY = "d2"` at `:2471`  re-measured live 2026-10-18 |
| Boundary checks `P-FAMILY-SOURCE`/`P-FAMILY-RANK` | VERIFIED | `:2636-2732` (opened: citation/owner/scheme checks, owed-slot foreign check `:2683`, garment_refs foreign check `:2730-2732`)  re-measured live 2026-10-18 |
| All seven paired controls land where cited | VERIFIED | every control string found at its cited line: `:2989` (borrow ledgers unchanged), `:3011` (deterministic D2-owned metadata rejected), `:3032` (WR ids not substring-banned), `:3045` (packet-only mirror), `:3053` (poison control), `:3063` (RK-01 local), `:3073` (counted exactly once), `:3099` (malformed fails closed), `:3109` (same-id foreign), `:3114`/`:3119` (D2 digest + D2 mutation); M1 ran the boundary matrix green today  re-measured live 2026-10-18 |
| selftest 163/163 | VERIFIED | M1  re-measured live 2026-10-18 |
| Identity = (family, block/component, record id); normative boundary | VERIFIED (anchors) | `01-brief.yml:55-75` (design problem) and `:111-121` (`no_import:` incl. `D2B-01..04` at `:117-120`); `03-orthography.yml:83-90` (`WR-01..07`)  re-measured live 2026-10-18 |
| Injection-point warning (revision `46a03257…` `:2613`, `:925-1197`, `:1235-1258`) | VERIFIED (as pinned-history) | row states the revision it cites; not re-resolved against HEAD by design  re-measured live 2026-10-18 |
| Propagation/tamper row | VERIFIED | `carry_findings` at `tools/assemble-d4-typed.py:276-288` exact; frozen generation 3 rows exit 0 (M7); deployed replay 33 pairs + live peers (M11); `repin_history[2]` (M11); stale pins refuse exit 2 (`:481-485`)  re-measured live 2026-10-18 |
| T1-T4 cautions + explicit-skip | VERIFIED | `:3343` exact ("the leg the d4 packet does not declare is skipped, not faked"); `lessons/round-22.md:19,53,63`, `repin.md:15,18`, `analysis.md:18,60,103-110`, `impl.md:54,60,64,70` all resolve  re-measured live 2026-10-18 |
| Round-25 implementation commitment | VERIFIED (anchors) | `LOG.md:3298-3309` (round-22 REJECTED on D, routed with recipe); `reports/round-22/routed-resolution.json` contains `R21-ALIAS-COERCION` and `R21-MTIME-TIE-BREAK` (plus R21-BASELINE-BINDING, R21-EDGE-DECLARED-IN)  re-measured live 2026-10-18 |

## 4. Robustness observation (not staleness)

Feeding the gate its own build product — `typed-pipeline-gate.py
examples/culture-d4/packet.d4.typed.yml` — exits 1 with `L2-channel`
(DERIV-REPLAY differential mismatch) and `L3-routing-consistency` (the
adapter-emitted `owed_slot: null` rows — `assemble-d4-typed.py:239-243`
serialize `None` — are read back by the gate's routing reader as the truthy
*string* `'null'`, breaking `hold_slots == routed_slots`). The documented and
frozen entry — the legacy packet `packet.d4.yml` via the sha-pinned profile —
passes 19/19 (M6), and the frozen replay reproduces (M7). This is an
undocumented-input hazard, not a defect in any SKILL row: no audited row
claims the build product is a gate input. Recorded so a future seat does not
repeat this seat's first invocation.

## 5. Findings disposition

### 5.1 Fixed during this audit (fixer seat audit-3; independently verified here)

| Fix | This seat's independent verification  re-measured live 2026-10-18 |
|---|---|
| F1 T3 anchors `:622`/`:793` → `:639`/`:808-814` (history kept) | Both defect and repair re-derived before reading audit-fixes.md (§3.3 T3); e571894 before-anchors confirmed true-at-the-time  re-measured live 2026-10-18 |
| F2 determinism `:369` → `:387` | Re-measured independently (§3.4); anchor correct  re-measured live 2026-10-18 |
| F4 Passenger-rows dated erratum (2026-10-18) | Supersession measured first (M10); erratum wording consistent with the bytes; `analysis.md:101` pointer checks out |
| F3 battery default-exit row (gates table — audit-1 scope) | Code lines `:100`/`:151` confirmed; default run independently reproduced exit 0 (M12)  re-measured live 2026-10-18 |

### 5.2 OPEN items in current bytes (for the integrator)

1. **`worldbible-integration-contract.md:183` mis-cite** (SKILL cautions row
   "Basis is never boilerplate", and the same text in the duplicated status
   block): the cited line is the delivered-record checklist item; the contract
   has no basis-hygiene text. Rule itself executable-verified
   (`packet_uncertainty.py:84,199-212`; v2-design §2.3 `:126`). Needs a dated
   erratum or re-point.
2. **`reports/round-18/d4/holds.md` §4.2 does not exist** (headings §0-§6;
   content lives in §4). Cited by the T3 bullet that F1 otherwise fixed.
3. **DANGLING tool anchors in the Error-patterns table** (audit-1's table;
   listed here because they are the same typed-label rules): `TL-01`,
   `TL-02`, `FIELD_DEFAULTS` appear nowhere under `tools/` (repo-wide grep),
   and the vocabulary `fictional-coordinate` / `descriptive-gloss` exists in
   no tool. The *behaviors* the rows describe are real and enforced
   (`:808-814` holds; kind never guessed; supplied-form identity grouping) —
   the named anchors are stale symbols, so the rows need dated errata or
   re-pointing to the surviving anchors.
4. **Corpus citation drift** (grounding rows shared with audit-1):
   `language-contact.md` cited bare but lives in `corpus/knowledge/linguistics/`
   (content at `:56-62` exact — T5 fine); `garment-lexicon-crosslinguistic.md`
   is in `culture-material/` and its `:26` is blank; `naming-collision-gate.md`
   is in `verification/`, and its `:52` (emblem/gloss ≠ cultural identity) and
   `:69-70` (spacing/NFKC) do not carry the "cut or status" / "collision vs
   native identity" claims they are cited for; `loanword-material-dating.md:26`
   is blank (the word-entry/referent material is at `:30-40`, sense-referent
   dating at `:63`); `language-contact.md:78-79` is the "Two principles" intro
   line, with the principles following.
5. **F2 cause note imprecise** (erratum dated 2026-10-18): the landed erratum attributes the `:369 → :387`
   shift to "the round-22 `carry_findings` block"; measured across revisions,
   the message was still at `:369` at round-18 `e571894`, `:370` at round-19
   `caf1bea`, `:387` by round-20 `35b6797`. Anchor correct; cause sentence off
   by two rounds. One-line follow-up, low priority.
6. **Duplicated uncertainty status rows** (§3.2 structure observation):
   verbatim second copy at the Error-patterns tail; recommend dedupe or
   cross-reference before the next round edits either copy.

## 6. Bottom line for claim D

Every executable claim in the five audited typed/handoff tables was re-run
against the current tools at `8fbcee9` and holds today: the label-typing
enforcement, the uncertainty grammar, the routing/hold equality, the
named-input and determinism behaviors, the family-clean boundary matrix, the
frozen d4-repin generation, and the deployed replay evidence are all green and
reproducible by the commands in §2. No stale *behavior* was found. What the
audit found — and what fixes F1-F4 plus §5.2 items 1-6 remain to finish — is
presentation-layer staleness: four line/section anchors and one superseded
measured sentence (all fixed or erratum-ed during this round, verified here),
plus six smaller citation defects still open. Zero silent staleness after
those land.

FILES: reports/round-24/audit-typed.md
