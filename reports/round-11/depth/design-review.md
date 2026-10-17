# R11-D02 — adversarial design review: is the expected hold set complete? any silent-channel risk?

- seat: **R11-D02** (design reviewer), round 11 (loop 1 of 3, build round 4 of 4), 2026-10-17
- assignment (verbatim): "DEPTH R11-D02 (design reviewer): adversarially review D01's plan
  (poll for it, max 15 min) — is the expected hold set complete? Any silent-channel risk?
  File findings to `reports/round-11/depth/design-review.md`."
- writes: this file only (plus in-lane scratch under `.scratch/d02-*`). No tool, gate, packet,
  component, baseline, manifest or earlier-round byte is edited by this seat;
  `reports/round-{8,9,10}/**`, `tools/gates/frozen/**` and `tools/gates/expected/**` are read-only here.
- clock: all stamps UTC (`date -u +%FT%TZ`); local time is UTC-03:00.
- canon: NON-CANON engineering review. Nothing here admits a round, a capability or a canon fact;
  no domain, canon, attribution or rights claim is made (`PROVINCE.md`; `AGENTS.md`).
- review target: `reports/round-11/depth/design.md` (R11-D01..D02). **Absent at 22:05:45Z** (poll
  evidence §1), **landed 22:06:21Z** (19:06:21-03:00) — inside this seat's poll window, so the
  plan-level review **is filed**: see the **ADDENDUM at the foot of this file** (§10), which reads
  the plan, reproduces four of its load-bearing measurements byte-for-byte, and files DR-10..DR-16
  against it. §1–§9 below were written before the plan was read and stand as the independent
  measurement baseline: the hold-set populations (§3), the silent-channel risk register against the
  *live gate code paths* (§4), and the contract the plan must pin (§5).

## 0. Verdict

Claim D requires "findings **exactly equal** to the expected hold set". As of 22:05:45Z the
tree does not contain a document that names that set, and the live artifacts do not agree on
what it is. Measured, the typed projection carries **three disjoint finding/debt populations**
(16 top-level findings = 15 holds + 1 note; 9 nested-only `R-MAT-BRIDGE-MISSING` holds; a rank
debt carried as counters), and its own `coverage` block reports a **severity account that
contradicts its findings list**. Any equality assertion that does not pin *population, tuple
identity and severity account* is ill-defined and can be satisfied by choosing the narrow one —
which is the "hold laundered as clean" hazard the round-11 negative shards (D17–D19) exist to catch.

Nine findings follow. None of them is a claim that D01's plan is wrong — D01's plan was not
available to be wrong. They are the adversarial acceptance criteria the plan (and D03–D08)
must close, each with the command that measured it.

| id | severity | finding |
|---|---|---|
| DR-01 | high | "the 16 findings" excludes a second, disjoint hold population: 9 nested-only `R-MAT-BRIDGE-MISSING` holds |
| DR-02 | high | one emitted document reports two severity accounts for the same two findings (`coverage.label_findings_fail: 2` vs `/findings` severity `hold` and `stats.fail: 0`) |
| DR-03 | high | the round-8 spec's hold set (§1.5: ten holds) is **five holds short** of the live output (15 holds); a plan citing the spec as authority is incomplete |
| DR-04 | medium | `/era_reconciliation/verdicts` is a 5-label worked table with an embedded negative control, not a live per-record disposition; an adapter keyed on it reads a fixture |
| DR-05 | medium | rank debts are carried as counters (13 unresolved, 3 quarantine, 3 jurisdiction gaps, 2 assay gaps), not findings; "findings equal" cannot imply rank clearance |
| DR-06 | high | the claim's "exits 0 with findings exactly equal to the expected hold set" contradicts every exit convention in the lane; producer and judge must be named, and suppression must be barred |
| DR-07 | high | the live sound-channel mechanisms available to a wiring are **silent** (`compare_only` skip; record construction from `costumes[].garment`), so a wiring can remove the ten PHON artifacts *and* the ten holds without any finding |
| DR-08 | medium | the committed typed projection is stale (`--check` exit 1) and "frozen replay re-pinned and green" has no definition yet: live replay is fail-closed red by design, and the re-pin precedent forbids editing the round-3 manifest in place |
| DR-09 | observation (out-of-lane) | five **filed** earlier-round artifacts are modified in the worktree during round 11 (mtime evidence); reported, not absorbed |

## 1. Reviewable status of D01's plan

Poll (60 s cadence) from 22:00:0xZ to 22:05:45Z, then again at 22:05:45Z:

```sh
ls -la reports/round-11/depth/      # 22:05:45Z
# capability-draft.md  review-22.md  scribe.md  test-cli.md  test-determinism.md
# test-interop-d3.md        — no design.md
```

Corroboration that this is not this seat's mis-read: three independent seats parked on the same
absence — `reports/round-11/depth/scribe.md` ("D01..D02 … `depth/design.md` — pending"),
`reports/round-11/depth/capability-draft.md:138` ("**pending** (design.md not landed at 22:03Z)")
and `reports/round-11/depth/review-22.md` §0 ("had not landed").

Consequence for this review, stated plainly: the answer to "is **D01's** expected hold set
complete?" is `to-verify` — there is no set to check. Filing a pass or a fail on it would be
fabrication. What follows is the measured contract: the populations, mechanisms and conventions
that any admissible plan must pin, each measured live by this seat against revision
`e3ef171` (round-11 claims commit) on 2026-10-17T22:00–22:06Z.

## 2. Independent measurements (pre-plan baseline; re-runnable, §9)

Subject hashes at measurement time (`sha256sum`, 22:01Z):

| artifact | sha256 |
|---|---|
| `tools/d2-typed-labels.py` | `0da0015f700345c938184cb45ca07178c33e98f798c3c09729007487fb89c802` |
| `tools/assemble-d2.py` | `8ea6bdde9514ee966fe58cf219d4d0228ecc3b041e30549c68073cc822c8655d` |
| `examples/culture-d2/packet.d2.yml` | `e0f21509e14ac03ed5747e6bbbb48183cbe56d6b61afff8c8475e4a50137b643` |
| `examples/culture-d2/typed-labels.d2.yml` | (stale committed projection; `assembly.packet_sha256` = `8da90b07…`, §DR-08) |
| `tools/gates/naming-collision-gate.py` | `d9e4e8f4f93a21b3b8574856a7d8bc6b93d224eee490ab37ed5f98741a630a1d` |

### 2.1 The typed projection's finding populations

```sh
export TMPDIR=$PWD/.scratch
python3 tools/d2-typed-labels.py --json    # exit 1
# stats: {'fail': 0, 'hold': 15, 'labels': 58, 'note': 1}; findings = 16
# id counts: D2L-FORM-UNRESOLVED 10 · D2L-RANK 4 · D2L-NATIVE 2
python3 tools/d2-typed-labels.py --emit .scratch/proj.json   # exit 1
```

Populations in the emitted projection (measured, `.scratch/proj.json`):

| population | n | content |
|---|---|---|
| `/findings` | 16 | `D2L-FORM-UNRESOLVED` ×10 (GAR-01..GAR-10, hold) · `D2L-NATIVE` ×2 (L-15 `sára`, L-16 `sará`, hold) · `R-RANK-CONFLICT` ×4 (`TR-04#a|TR-06#a`, `WR-02#g|WR-09#g`, `WR-08#g|WR-09#g` hold; `SR-01#a|SR-01#b` note) |
| `/era_material_reconciliation/findings` | **9** | `R-MAT-BRIDGE-MISSING`, all `hold` (CMAT→MAT bridge absent) — **absent from `/findings`** |
| `/rank_rules/{unresolved,quarantine,jurisdiction_gaps,assay_gaps,residuals,entitlement_edges}` | 13/3/3/2/1/2 | debts carried as data lists, never as findings |
| `/era_reconciliation/verdicts` | 5 | worked table incl. `"E9 no such label"` → `unmapped` (a control row, not a D2 record) |

`coverage` and the findings list disagree on severity for the same two entries (measured,
`/coverage/label_findings_fail = 2`, `/stats/fail = 0`, and the two `D2L-NATIVE` entries carry
`severity: hold` with detail "…held for the form's owner rather than failed"): the parser
account is produced before `reclassify_parser_finding` demotes it (`tools/d2-typed-labels.py`
~`:2449`). Both numbers are in the same emitted document.

### 2.2 The gate-facing (legacy) population over the live packet

```sh
for g in naming-collision-gate costume-era-consistency-gate phonology-sanity-gate \
         myth-consistency-gate lexicon-coverage-audit; do
  python3 tools/gates/$g.py examples/culture-d2/packet.d2.yml; done
```

| gate | exit | findings |
|---|---|---|
| naming-collision-gate | 1 | **17**: `PHON-INVENTORY` FAIL ×10 (GAR-01..GAR-10, English `garment` strings) · `NAME-NEAR` REVIEW ×6 · `CROSS-HOLD` HOLD ×1 |
| phonology-sanity-gate | 1 | 3: `A-NEUTRAL` REVIEW ×3 (phonology profile, no GAR involvement) |
| costume-era-consistency-gate | 0 | 0 — the round-3 ten `G-ERA` holds are **not live**; the round-4 era reconciliation removed them |
| myth-consistency-gate | 0 | 0 |
| lexicon-coverage-audit | 0 | 0 |

So the "before" of claim D is narrower than the round-3 narrative suggests: exactly the ten
`PHON-INVENTORY` FAILs are the legacy artifacts that the wiring must replace, and the six
`NAME-NEAR` REVIEWs plus the `CROSS-HOLD` are the non-GAR findings a live naming-gate run keeps
producing. The phonology gate never reads costumes (no `garment`/`costumes` reference in
`tools/gates/phonology-sanity-gate.py`; grep, 22:03Z), so "the D2 gates" in the claim has a
determinate membership only if the plan names it.

### 2.3 Exit conventions (three different ones in play)

| process | convention | source |
|---|---|---|
| `tools/d2-typed-labels.py` | 0 = no HOLD/FAIL (notes only); 1 = findings; 2 = could-not-evaluate | tool docstring `:40`; measured exit 1 with 15 holds |
| gates (`naming-collision-gate.py`) | 0 = clean (no findings, of any level); 1 = findings; 2 = could-not-evaluate | gate docstring `:15-18` |
| `tools/replay-frozen.py` | 0 = reproduced; 1 = mismatch; 2 = could-not-evaluate | `reports/round-8/depth/test-replay.md:24` |
| `tools/assemble-d2.py --check` | 0 = byte-identical; 1 = differs | measured exit 0 (byte-identical, 22:02Z) |

Under every one of these, **a run that reports the expected holds cannot exit 0**. The claim's
phrase "end-to-end command over examples/culture-d2 exits 0 with findings exactly equal to the
expected hold set" is therefore only satisfiable by a *judge* whose subject is the equality, not
by a *producer* whose subject is the findings (§5, DR-06).

### 2.4 Frozen replay and the typed projection's own `--check`

```sh
python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv
# live tree: exit 2 — 7/7 could-not-evaluate gate_digest_mismatch (22:01Z)
python3 tools/d2-typed-labels.py --check
# exit 1 — "typed-labels.d2.yml differs from the deterministic projection" (22:02Z)
python3 tools/assemble-d2.py --check
# exit 0 — "packet.d2.yml: byte-identical deterministic assembly" (22:02Z)
```

Independent control this seat ran (fix-18 §Control recipe, re-executed 22:05:23Z): isolated tree
built from `291c714` gate bytes + committed frozen tree + committed replay tool →
`tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv --repo-root $ISO --json` →
**exit 0, 7/7 reproduced, 0 mismatch, 0 could-not-evaluate** (`.scratch/d02/iso`; command §9).

Both halves of the recorded claim in the round-10 ledger (rows 61/88/104: live exit 2,
pinned-revision recipe exit 0) therefore still hold at 22:05Z. The *live* tree cannot be green
without re-pinning, and the round-8 precedent is explicit:
"no shard should re-bless the pins by editing the round-3 manifest in place"
(`reports/round-8/depth/test-replay.md` §6, re-freeze under a new generation directory).

## 3. Hold-set completeness (DR-01..DR-05)

**DR-01 — the expected set has a population problem, not a naming problem.** The projection's
`/findings` is the only list a `--json` consumer sees, and it omits 9 holds of its own document.
If the plan defines the expected set as the `--json` findings, then nine `R-MAT-BRIDGE-MISSING`
holds are excluded *by construction* from "findings exactly equal" — the equality would be true
and the nine debts invisible. If instead the design counts every `severity != ok` entry anywhere
in the projection, the expected set is 24 holds + 1 note. Both are defensible; the plan must
choose, in writing, and give the excluded population's own disposition (carried where? surfaced
by which command?) with the reason it is out of the gate channel:
`/era_material_reconciliation/scopes` = `{era: packet-eras, material: packet-materials}` and the
per-record summary `{claims: 10, findings: 9}` are already in the document, so the exclusion is
*visible* — it must be *stated*.

**DR-02 — the severity account must be pinned.** A checker that reads `coverage.label_findings_fail`
computes 2 FAILs; a checker that reads `/findings` computes 0 fails and 15 holds; a checker that
reads `/stats` computes the same 15. The demotion is deliberate (detail text: "held for the form's
owner rather than failed") — but a plan that does not name the account, and the demotion step,
leaves the equality check comparing different universes. Required: the plan names the canonical
account (recommended: the emitted `/findings`), and the canonicalization rule for a finding's
identity, e.g. the tuple `(code, where, severity)` sorted — with `notes` explicitly in or out.
The live set of `(code, where, severity)` under that rule is enumerated in §3.1.

**DR-03 — the spec is not the authority for the count.** `reports/round-8/depth/design-spec.md`
§1.5 predicts exactly ten projected holds ("`D2L-FORM-UNRESOLVED` HOLD ×10"), and
`reports/round-8/depth/test-consistency.md:228` pins the label account as `fail 2, hold 10`. The
live tool emits 15 holds and its own coverage says `label_findings_fail: 2`. A plan that copies
the spec's ten (the natural move — it is the only written "expected hold set" in the tree) is
five holds short: the two `D2L-NATIVE` accent holds and the three `R-RANK-CONFLICT` holds. The
plan must derive its set from a *named* rule over the artifact (e.g. "every `severity != ok`
entry of the wired projection's `/findings`") and then name each member — not cite §1.5.

**DR-04 — the era verdicts are a table, not a disposition.** `era_reconciliation.verdicts` is
built from a hardcoded 5-label tuple including `"E9 no such label"`, a control row
(`tools/d2-typed-labels.py:2458-2461`). An adapter that reads `verdicts` to decide "is this tag
in scope" is reading a worked example; the live per-record verdicts are the
`era_material_reconciliation.records[*].era` codes (`R-ERA-IN-SCOPE`, tag `E0`/`E1`/`E2`, 10/10
records, 0 findings). The plan must say which surface the gate consumes. Related but distinct:
the ten `G-ERA` holds of round 3 are *not* live (§2.2), so no part of the wiring may claim to
"resolve" them; they are absent, and the plan should say whether that absence is accepted
(the round-4 reconciliation) or re-opened.

**DR-05 — rank debts are not in any findings list.** `rank_rules.coverage` = `{component_rules:
21, normalized: 9, gate_projected: 5, partitioned: true}` with 13 `unresolved` items, 3
`quarantine` handles, 3 `jurisdiction_gaps`, 2 `assay_gaps`, 1 `residual`, 2 `entitlement_edges`
— data lists. Only 4 `R-RANK-CONFLICT` entries reach `/findings`. "Findings exactly equal to the
expected set" must not be read as "the rank layer is clear"; the plan should state, per debt
class, whether it is (a) in the expected set, (b) carried with a named owner, or (c) out of scope
for this claim — ASSEMBLY.md:89's "does not establish rank-rule consistency" is the standing
limit.

### 3.1 Candidate expected hold set this review measured (for the plan to confirm or correct)

Under the recommended identity `(code, where, severity)` over `/findings`, sorted:

```
(D2L-FORM-UNRESOLVED, GAR-01..GAR-10, hold)                 ×10
(D2L-NATIVE, L-15, hold)  (D2L-NATIVE, L-16, hold)          ×2
(R-RANK-CONFLICT, TR-04#a|TR-06#a, hold)
(R-RANK-CONFLICT, WR-02#g|WR-09#g, hold)
(R-RANK-CONFLICT, WR-08#g|WR-09#g, hold)
(R-RANK-CONFLICT, SR-01#a|SR-01#b, note)                    ← note, not a hold
```

= **15 holds + 1 note**, plus (excluded, to be dispositioned) the 9 nested `R-MAT-BRIDGE-MISSING`
holds; and, on the gate side, the naming gate's non-GAR findings (6 `NAME-NEAR` REVIEW, 1
`CROSS-HOLD`) must be either retained in the gate-facing set or explicitly out of it. This is a
*measured candidate*, not the contract: D01's plan is the authority (per `capability-draft.md` §5,
which independently reached the same two readings — the design decides).

## 4. Silent-channel risk register (DR-07)

Each risk is named against the **live code path**, with the control that would catch it.
"Silent" here means: the channel stops testing a form **and no finding records it**.

| id | mechanism (live code) | what goes silent | required control |
|---|---|---|---|
| SC-1 | `compare_only` skip: `tools/gates/naming-collision-gate.py:1045`, `:1090`, `:1121`, `:1154` — `if record.get("compare_only"): continue` (no finding) | a garment record can leave the sound channel with zero output; exactly the R3 misuse the spec forbids (`design-spec.md` §1.3 R3) | a *packet-input* control (not projection-side): set `compare_only` on GAR-01 and assert the wired run still emits the hold / the `D2L-SCOPE` misuse finding |
| SC-2 | record construction only from `costumes[].garment` (`:655-676`, via `_make_record(entry, "garment", …)`) | blanking, renaming or re-typing the `garment` field removes the record from Gate B entirely — no FAIL and no HOLD | assert the wired pipeline emits one named hold per owed form *from the component*, and that a dropped owed form (component row removed) flips the verdict |
| SC-3 | population split (§2.1): nested findings never merged into `/findings` | 9 `R-MAT-BRIDGE-MISSING` holds invisible to a `--json` consumer | the equality check enumerates populations explicitly; a control asserts the excluded population is unchanged-and-reported, not merely absent |
| SC-4 | severity demotion `reclassify_parser_finding` (~`:2449`) vs `coverage.label_findings_fail` | two accounts of the same severity in one document (§2.1) | the check pins one account; a document-level consistency assertion (`coverage` counters == recomputed counts over `/findings`) |
| SC-5 | exit code: nothing in the lane exits 0 on findings (§2.3) | a "green e2e" achieved by suppressing findings, or by judging the wrong process | producer/judge split with named exit contracts (§5); a negative test where a smuggled label yields exit 0 |
| SC-6 | `form_slot` prose in the packet (`examples/culture-d2/packet.d2.yml:1850ff`, e.g. `"LEX-GAR-01, the valley grade of L35 mirken (to-verify with 05-lexicon)"`) | requirement prose typed as a *supplied* form would enter the sound channel and manufacture FAILs against English text — the round-8 F1 defect class, closed at R2 by not emitting the requirement as a label | the wiring must never project `form_slot` text as `status: supplied`; a control asserts no label `text` equals a `form_slot` string |
| SC-7 | borrowed strata: R2 requires loans to stay **checked** (`design-spec.md` §1.3 R2); 2 `borrowed-strata` labels exist (L-26/L-27) | a blanket "non-native ⇒ off-channel" wiring silently exempts the loans too | differential test: `native-form` + `borrowed-strata` records still receive phonotactic checks; only `translated-label` leaves the channel |
| SC-8 | untyped legacy record: R6 ("dropping the typing fields cannot exempt a string") | a packet where the typing is absent degrades to "no channel", not to "legacy channel" | a control packet with labels removed must reproduce the *legacy* checked behaviour (naming gate FAILs), not silence |

The differential that the claim asks for ("translated labels never enter the sound channel") is
only meaningful as a *pair*: legacy packet → 10 `PHON-INVENTORY` FAILs (§2.2, measured); wired
packet → 0 such FAILs **and** 10 named holds. Either half alone is satisfiable by suppression.
This matches the three D17–D19 negative targets in `targets.json` verbatim; SC-1/SC-2 are the
concrete mechanisms those negatives must exercise (mutating the *input*, not the projection — the
C6 pattern already named in `review-22.md` §1.1).

## 5. The exit / equality contract the plan must pin (DR-06)

The claim text contains a contradiction that is easy to implement the wrong way:

> "…the D2 gates evaluate the typed packet such that translated labels never enter the sound
> channel and owed native forms are carried as named holds (not PHON artifacts); end-to-end
> command over `examples/culture-d2` exits 0 with findings exactly equal to the expected hold set"

- a *gate* reporting 15 holds exits 1 (§2.3);
- `d2-typed-labels.py` reporting the same holds exits 1;
- `replay-frozen.py` exits 0 only for reproduction;
- `assemble-d2.py --check` exits 0 for byte-identity (and says nothing about findings).

Recommended reading (to be confirmed or corrected by D01 — and, if corrected, the corrected
reading must be stated *and* the counting commands adjusted to it):

1. **Producer** — the wired e2e command emits the typed packet's findings over
   `examples/culture-d2`; its exit code is the *findings* code (1 when the expected holds are
   present). It must not exit 0 by suppressing anything.
2. **Judge** — a separate command (the natural home is `reports/round-11/run-validation.py`,
   X03's file; `capability-draft.md:138` already records the expectation "the e2e entry named by
   D01–D02") compares the produced finding multiset to the design's named set and exits 0 iff
   *exactly equal* under the canonicalization of DR-02, with `notes` in/out pinned.
3. **Barred** — any wiring whose "green" is obtained by dropping findings; the judge's own
   negative control is a mutated packet that must fail the equality (SC-1/SC-2).
4. **Wording** — the claim row (capability draft §4) must be re-worded to match whatever is
   pinned: "exits 0" belongs to the judge, "findings exactly equal" belongs to the comparison,
   and the row's `⟨n holds / m notes⟩` placeholders must be filled with the §3.1 numbers or the
   plan's corrected ones.

## 6. Re-pin definition (DR-08) and the filed-artifact observation (DR-09)

**DR-08.** "Frozen replay re-pinned and green" needs three definitions the plan must supply:

1. *which* manifest is re-pinned — the precedent (`reports/round-8/depth/test-replay.md` §6;
   `corpus/knowledge/verification/gate-frozen-run-standard.md`: "never silently re-pinned")
   forbids editing `tools/gates/frozen/round-3/MANIFEST.tsv` in place; a new generation
   directory/id is the recorded pattern, with the old generation left legible;
2. what "green" is measured *over* — live tree with the new generation (the current live tree
   reads exit 2 / 7-of-7 `gate_digest_mismatch`, measured §2.4) or the isolated pinned-revision
   control (exit 0, measured by this seat §2.4) — the claim must say which, because only the
   first actually re-pins;
3. the **verdict-preservation probe**: the wiring changes the naming gate's behaviour for
   garment records; the re-pinned generation must show that the historical snapshot's verdict is
   *reproduced or explicitly changed with a per-change justification* (the C5 pattern in
   `review-22.md` §1.1), not merely re-pinned to whatever the new gate now says.

Additionally, the plan's counting command for claim D is
`python3 reports/round-11/run-validation.py; python3 tools/assemble-d2.py --check` — but
`assemble-d2.py --check` only pins the **untyped** packet's byte-identity and was green (exit 0)
both before and after the typed projection went stale. If the wiring changes the assembler output,
`--check` becomes meaningful again; if it does not, the counting command tests nothing about the
typed pipeline. The plan should either add `python3 tools/d2-typed-labels.py --check` (currently
exit 1 — the committed artifact records `assembly.packet_sha256 = 8da90b07…` while the live packet
is `e0f21509…`; round-10 rows already record this as A2) or state why not.

**DR-09 (out-of-lane, reported not absorbed).** Filed earlier-round artifacts are modified in the
worktree *during* round 11 (`git status --porcelain`, 22:05Z; mtimes):

```
 M reports/round-5/validation.json              19:03:00  (-361 lines; acceptance recomputed)
 M reports/round-6/validation.json              19:03    (-421 lines)
 M reports/round-6/checkpoint-validation.json   19:03
 M reports/round-7/validation.json              19:03
 M reports/round-8/validation.json              19:03    (claim D flipped to passed:false)
 M reports/round-9/validation.json              19:03
 M reports/round-10/coverage/index-update-22.md 19:01
```

`reports/round-8/validation.json`'s diff re-runs its acceptance checks against the *current* tree
(its D claim's `replay_frozen.isolated` now reads `could_not_evaluate: 7`), i.e. filed round-8
evidence is being recomputed rather than preserved. This seat writes none of these files and does
not absorb the question; it is routed to the parent integrator / X02 adjacency watch (the same
observation was independently parked by `capability-draft.md` §7.4 for rounds 5/6/10). Effects on
this review: none — every measurement here came from live tools, not from those files.

## 7. What the plan must contain to close these findings

Minimum content checklist for `reports/round-11/depth/design.md` (or its successor), one line each:

1. the expected hold set, **named member by member**, with the derivation rule, the population
   (§3 DR-01), the severity account (DR-02) and the canonicalization tuple (DR-02/§5);
2. a per-member disposition of everything measured but *not* in the set: 9 nested material bridge
   holds, 13 rank unresolved items, 3 quarantine handles, 3 jurisdiction gaps, 2 assay gaps,
   1 residual, 6 `NAME-NEAR` REVIEW, 1 `CROSS-HOLD`, 3 `A-NEUTRAL` REVIEW (DR-01/DR-05);
3. the wiring surface: where typed labels enter (assembler block vs adapter step), and the exact
   gate-side read path — with a statement that **no** gate script currently reads any typed
   surface (`grep -rln "typed_labels\|translated-label\|native-form\|label_kind" tools/gates/*.py`
   → no match, 22:04Z), so the adapter is new code with its own controls;
4. the three-way routing proof (SC-7): `translated-label` off-channel, `native-form` +
   `borrowed-strata` on-channel, untyped → legacy channel (SC-8);
5. the producer/judge exit contract (§5) and the counting-command adjustment for
   `assembler --check` (DR-08);
6. the re-pin definition in the three parts of §6, with the new generation's id and the
   verdict-preservation probe;
7. the three negative controls as *input-mutation* tests (SC-1/SC-2/SC-5), not projection-side
   assertions.

## 8. Limits, to-verify, and open items

- **V1 (to-verify).** The D01-specific reconciliation — "is D01's expected hold set complete?" —
  is unanswered because `reports/round-11/depth/design.md` was absent at 22:05:45Z (poll evidence
  §1). If it lands later in the wave, this file's §3.1 and §0 need a re-read against it by a
  reviewer (this seat's window is closed at filing).
- Everything measured here is revision-bound to `e3ef171` and the artifact hashes in §2. Two
  tools in this lane changed 24 times in 15 minutes during round 8 (`test-consistency.md` §6);
  a later revision invalidates the binding and must be re-measured.
- The pinned-revision replay control (§2.4) verifies *bytes and recorded verdicts* only; it says
  nothing about design quality or scholarship (`gate-frozen-run-standard.md`).
- No domain, canon, attribution, rights or game-mechanics claim is made here; those are out of
  province (`PROVINCE.md`).
- This review names no capability row, admits no round, and edits nothing.

## 9. Reproduction

```sh
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
export TMPDIR=$PWD/.scratch
python3 tools/d2-typed-labels.py --json > .scratch/d02-typed.json; echo $?      # 1; stats hold 15
python3 tools/d2-typed-labels.py --emit .scratch/d02-proj.json; echo $?          # 1
python3 - <<'EOF'
import json; p=json.load(open('.scratch/d02-proj.json'))
print("findings:", len(p["findings"]), "nested:", len(p["era_material_reconciliation"]["findings"]))
print("coverage:", p["coverage"])
EOF
for g in naming-collision-gate costume-era-consistency-gate phonology-sanity-gate \
         myth-consistency-gate lexicon-coverage-audit; do
  python3 tools/gates/$g.py examples/culture-d2/packet.d2.yml | grep -c '^FINDING'; done   # 17 0 3 0 0
python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv; echo $?            # 2 (live)
ISO=.scratch/d02/iso; mkdir -p "$ISO/tools/gates"
cp tools/replay-frozen.py "$ISO/tools/"; cp -a tools/gates/frozen "$ISO/tools/gates/frozen"
for g in phonology-sanity-gate lexicon-coverage-audit myth-consistency-gate \
         costume-era-consistency-gate naming-collision-gate provenance-audit; do
  git show 291c714:tools/gates/$g.py > "$ISO/tools/gates/$g.py"; done
(cd "$ISO" && python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv --repo-root "$PWD" --json)
                                                                                            # 0; 7/7 reproduced
python3 tools/d2-typed-labels.py --check; echo $?                                          # 1 (stale artifact)
python3 tools/assemble-d2.py --check; echo $?                                              # 0
```

---

# ADDENDUM — D01's plan landed at 22:06:21Z; the review it enables

This section **updates §0**: DR-03 is closed by the plan, DR-06 is partially closed (residue =
DR-14), DR-01/DR-02/DR-05 remain open, and seven new findings (DR-10..DR-16) are filed against the
plan. §1's V1 is closed: `reports/round-11/depth/design.md` (29 099 B, mtime 2026-10-17T19:06:21-03:00)
was read by this seat at 22:07–22:10Z and reviewed below.

## 10.1 Independent reproduction of the plan's load-bearing measurements — 4/4 exact

I re-ran the plan's own experiments from the lane root at revision `e3ef171` (packet `e0f21509…`,
naming gate `d9e4e8f4…`) in my own scratch, without reading D01's scratch files:

| plan claim | my command | my result | plan's recorded value | verdict |
|---|---|---|---|---|
| §1.1 legacy naming run: 17 findings, stdout sha `ebc8850d…` | `python3 tools/gates/naming-collision-gate.py examples/culture-d2/packet.d2.yml` (22:07Z) | 17 findings (`PHON-INVENTORY`×10 FAIL, `NAME-NEAR`×6 REVIEW, `CROSS-HOLD`×1 HOLD), file sha `ebc8850d08ec1b7e32616cbca9092ba66f3b6f148a61515a033e6bed6fa66f4b` | `ebc8850d…` | **match** |
| §1.3 exp. 1: GAR-01 field renamed → 16 findings, PHON 10→9, no other line changed, sha `842d606a…` | own byte copy, first `garment:` in the costumes block → `garment_gloss:` (`.scratch/d02/packet-route-gar01.yml`) | 16 findings (9 PHON), sha `842d606a1cc2d6ffb1c5368a90f75e69ff399f3d662dd47748d1bd2a7124505c` | `842d606a…` | **match** |
| §1.3 exp. 2: all ten routed → 7 findings, PHON ×0, exit 1, sha `feb64881…` | own byte copy, all ten `garment:` → `garment_gloss:` | exit 1, 7 findings (0 PHON), sha `feb6488127f115f986bf7602c0b074ce911c951751e5e2c63e32e5d23bb52bd9` | `feb64881…` | **match** |
| §5.1 predicted post-re-pin projection bytes `a3aa452c…` | `python3 tools/d2-typed-labels.py --emit .scratch/proj.yml` (22:02Z) | sha `a3aa452cd5ae77c351d9532a707fb1f1ababf77c3fad8b9d28089e6958364a43` | `a3aa452c…` | **match** |

Byte-for-byte agreement on all four, including the two mutation experiments that carry §1.3's whole
argument. The channel differential ("typed = legacy minus exactly the ten `PHON-INVENTORY` lines";
17 → 7) is therefore **confirmed independently**, and the one-line re-pin prediction is exact.
Also confirmed by this seat: `--json` stats `{fail 0, hold 15, note 1, labels 58}` and the all-routed
run's exit **1** with zero FAIL lines (the plan's §8 item 2 anticipated exactly this).

## 10.2 Hold-set completeness — the plan's 15 match, three gaps remain

The plan's §4.2 table names 15 holds and §4.3 the one note. Against this seat's independent
extraction (`--json`, §2.1): identical in `(id, severity, where)` for all 16 entries, `fail ∅`,
counts `hold 15 / note 1`. The plan also got the derivation right in the way that matters: it takes
the set from the **live artifact** (`--json` at pinned shas), not from the round-8 spec's ten — so
DR-03 is closed with evidence, and §4.2's "items 11–15 are in the set because a wiring that silently
dropped them would be indistinguishable from one that fixed them" is the correct instinct.

Remaining gaps (**not** closed by the plan):

1. **DR-01 stands — the excluded population is unnamed.** `grep -n "R-MAT\|BRIDGE" reports/round-11/depth/design.md`
   → no match (22:07Z). The 9 nested `R-MAT-BRIDGE-MISSING` holds do not appear in §4.2, §4.3 or the
   exclusion language of §4.4(4). The plan's derivation command (`--json`) structurally cannot see them,
   so the omission is invisible from inside the plan. Consequence: a reviewer or a future gate comparing
   `--emit`'s finding populations (24 holds) against the frozen 15 has no document that says which
   population is authoritative and why the 9 are out. The plan should add them to §4.3's exclusion table
   with the reason (they are the *material-bridge* debts, surfaced only in the full projection, and the
   typed pipeline's channel claim does not touch them) and a pointer to the command that does surface them.
2. **DR-02 stands (partially).** §4.4(1)/(3) pins the counts from the `--json` stats account (`fail 0,
   hold 15, note 1`) — the right choice — but the projection document that §5.2 freezes still reports
   the pre-demotion parser account (`coverage.label_findings_fail: 2`) for the same two findings. A
   checker reading `coverage` disagrees with the gate's `fail ∅`. One sentence in §4.4 (or a projector
   note) should state that `coverage.label_findings_*` is the label-level, pre-demotion account and is
   not the pipeline account.
3. **DR-05 stands.** The rank debt carried as counters — 13 `unresolved` items, 3 `quarantine`
   handles, 3 `jurisdiction_gaps`, 2 `assay_gaps`, 1 `residual`, 2 `entitlement_edges` — is neither in
   the expected set nor dispositioned. §4.2 items 13–15 (the three rank *holds*) are correctly in the
   set, but "findings exactly equal" must not be readable as rank clearance; `ASSEMBLY.md:89`'s standing
   limit belongs in §8.

**DR-04 does not apply:** the plan keys the routing on the projector's label records, not on
`era_reconciliation.verdicts`; the era surface is untouched (the costume gate's live run over the D2
packet is 0 findings anyway, §2.2). Recommend the plan say so explicitly so no implementer reaches for
the `verdicts` table.

## 10.3 New findings against the plan (DR-10..DR-16)

**DR-10 (medium-high) — the bundle's other live findings are in no expected set and no exclusion table.**
Measured at 22:03Z: naming gate 6 `NAME-NEAR` REVIEW + 1 `CROSS-HOLD` HOLD; phonology gate 3
`A-NEUTRAL` REVIEW; costume/myth/lexicon 0. The plan's L2 pins that these do **not change** (the right
control), but the document never says what they are. A reader asking "what is the D2 flow's complete
finding population after the wiring?" gets an answer for the projector (15+1) and for the ten replaced
PHON FAILs, and no answer for these eleven. Add an "accepted legacy background" table with counts and
the L2 role, or extend the set.

**DR-11 (medium-high) — §2.2's typed-packet schema carries only 10 of the 16 pinned findings.**
§2.2 shows `typed_channel:` rows with `hold: D2L-FORM-UNRESOLVED` — a carrier for the ten routing holds
— and no block for the 2 `D2L-NATIVE` holds, the 3 `D2L-RANK` holds or the 1 note, while §3.1's L3
reads "the pipeline finding set from the typed run (projector findings carried in the typed packet)" and
§4.2's prose says items 11–15 are carried through. D03/D04 implement §2.2 verbatim; the gap resolves
itself as an implementation choice unless the plan closes it. Either the schema adds a
`findings:`/`notes:` block (with the note distinct from holds, per §4.3), or L3 is re-worded to name its
actual source — and if that source is the projection file itself rather than the typed packet, say it:
the gate then reads the projector output directly, L4's pins must cover that read, and "the D2 gates
evaluate the typed packet" is true only for the ten routing holds.

**DR-12 (medium) — exit 0 with 15 `FINDING` lines is a novel aggregate in this lane.** Under every other
convention measured (§2.3), exit 0 means *clean*; the naming gate exits 1 for REVIEW/HOLD-only runs
(measured: the all-routed typed run exits 1 with zero FAILs). `typed-pipeline-gate.py` would be the
first lane artifact that prints findings and exits 0. §3.2's banner is a human mitigation; make the
semantics machine-checkable: `--json` carries `{"clean": false, "holds": 15, "equal_to_pinned_hold_set":
true}`, and §5.2's `expected.json` pins `clean: false` next to `exit: 0` so a consumer that reads only
the frozen record cannot read "green culture".

**DR-13 (low) — line format deviates from the family.** §3.2 pins `FINDING D2L-…: [hold] <where> —
<detail>`; the family format is `FINDING <id>: <LEVEL> — <message>` with `LEVEL ∈ {FAIL, HOLD, REVIEW}`
(naming gate docstring `:15-18`; the typed tool prints none). No parser breaks today — the only lane
parser keys on the `FINDING ` prefix (`tools/replay-frozen.py:63`), verified by grep — but a reader or
script grepping `: HOLD —` counts zero holds. Recommend the family form
(`FINDING D2L-FORM-UNRESOLVED: HOLD — GAR-01: label_id LEX-GAR-01 has no supplied native/borrowed form`)
or a deliberate, documented deviation.

**DR-14 (medium-high) — the claim's counting command does not (yet) witness the plan.**
Claim D's counting command is `python3 reports/round-11/run-validation.py; python3 tools/assemble-d2.py
--check`. `grep -n "run-validation" reports/round-11/depth/design.md` → the only hit is line 115, which
mentions the counting command solely to justify not touching `assemble-d2.py`. Nothing in the plan runs
`tools/gates/typed-pipeline-gate.py` from the acceptance runner or compares against
`examples/culture-d2/expected-holds.json`. If X03's `run-validation.py` does not invoke the typed gate
(the e2e entry `capability-draft.md:138` is still the placeholder `⟨e2e entry from design.md⟩`), then no
counting command exercises L1–L4 and the claim is evidenced by fragments only. The plan should hand
X03 the exact command line, its pinned inputs and its expected verdict (`exit 0`, 15 holds, 1 note,
fail ∅), and name it in §3.1/§5.

**DR-15 (medium) — the differential cannot prove borrowed strata stay checked.** §2.3 row 4 keeps
supplied `borrowed-strata` on the checked channel; §1.3's measurement produces no loan finding in
either the legacy or the typed run, so L2 cannot distinguish "L-26/L-27 checked and clean" from
"L-26/L-27 skipped". The design-spec's R2 forbids the skip. Recommend a fourth negative control
(N-loan): mutate L-26's supplied form to a symbol outside the declared inventory and require the typed
run to emit the native/inventory finding for it — proving the loans are still on the channel.

**DR-16 (high, live, cross-lane) — "battery remains green" is already false, and not because of the D
wiring.** §5.4 pins the predicate "`{pass: 7, fail: 0, findings: []}` plus the unchanged exit-2 coverage
gap". Measured 22:09:39Z (`.scratch/d02/battery-final.json`, sha `e6de0bf09d0d833d`):

```
python3 tools/check-gate-battery.py   →  battery_exit 2, pass 7, fail 0, unevaluable 0
```

with **seven baseline findings** on `tools/gates/expected/handoff-exercise/r11/expected.json`
(file mtime 2026-10-17T22:08:52Z — it landed two minutes after the design was written):
`BASELINE-GATE-UNKNOWN` ("declared gate None is not one of the seven registered gates"),
`BASELINE-EXTERNAL-INPUT` ×5 ("resolved … outside the baseline; §3 requires a committed copy inside it"
for `worldbible-integration-contract.md`, `packet.d2.yml`, `typed-labels.d2.yml`, further D2/D3 inputs),
`BASELINE-EXPECTED-ABSENT` ×1. The `findings: []` half of the predicate is falsified not by the D wiring
but by an apparent **O-claim artifact** (the exercise baseline of R11-O14..O15) placed inside a battery
default root while declaring no gate. The documented remedy root no longer reaches green either:
`--baselines-root tools/gates/expected --baselines-root tools/gates/frozen --baselines-root
reports/round-9/baselines` → exit 2 with the same seven findings (22:07Z), against round-10 ledger row
177 / fix-21's recorded "exit 0, baselines_found 8, pinned 8, gates_uncovered []". Routing: the parent
decides whether the exercise baseline moves out of `tools/gates/expected/**` or conforms to the
`kotodama-frozen-run-v1` schema; either way the D claim's "battery remains green" leg needs a re-stated
predicate (and the F claim's ledger rows 65/99/177 are now drifting for this reason).

## 10.4 Updated finding table

| id | status after D01's plan | note |
|---|---|---|
| DR-01 | **open** | 9 nested material holds unnamed/un-dispositioned (§10.2.1) |
| DR-02 | **open (narrowed)** | counts pinned correctly; the frozen projection's `coverage` account still disagrees (§10.2.2) |
| DR-03 | **closed** | the plan derives all 15 from live output, names each, and beats the spec's ten (§10.2) |
| DR-04 | **n/a** | the plan does not key on `era_reconciliation.verdicts`; recommend stating it (§10.2) |
| DR-05 | **open** | rank debts (21 counters) still outside both expected set and exclusion table (§10.2.3) |
| DR-06 | **partially closed** | §3.2 makes the new gate the judge (defensible); residue = DR-14 (counting command) and DR-12 (aggregate semantics) |
| DR-07 | **addressed, one hole** | three-layer defence (adapter coverage, L2 differential, L3 exactness) with input-side negatives D17–D19; hole = DR-15 (loans) |
| DR-08 | **closed** | §1.4/§5.2/§5.3: new generation manifest, old pins untouched, divergence reported; §5.4's predicate is the residue (DR-16) |
| DR-09 | **observation** | unchanged; out-of-lane |
| DR-10..DR-16 | **new** | §10.3 |

Net: the plan is a strong, measured design — its four load-bearing claims reproduce byte-for-byte here,
its hold set is complete *for the population it names*, and its routing avoids the silent mechanisms by
construction (§2.3 + L2). The seven open items above are all closure work on boundaries the plan drew
around itself: the excluded populations (DR-01, DR-05, DR-10), the typed-packet carrier for non-routing
findings (DR-11), the aggregate/exit semantics (DR-12, DR-13), the acceptance wiring (DR-14), the loans
control (DR-15) and the battery predicate (DR-16). None requires abandoning the design.

