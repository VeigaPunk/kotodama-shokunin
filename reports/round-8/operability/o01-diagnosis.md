# R8-O01 — diagnosis: round-7 F-check parent-check identity collision

- Round: 8 (loop 1 of 3, build round 1 of 4) · Date: 2026-10-17 (UTC 2026-10-17T20:15:02Z at time of measurement)
- Lane repo: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`
- Defect under diagnosis: `reports/round-7/validation.json` claims.F.error =
  `wrong rejection for duplicate-parent-receipt-does-not-inflate: parent check identity collision`
  (same string in `failures[0]`, `reports/round-7/validation.json:6` and `:166`)
- Files inspected (hashes are the ones the round-7 receipt itself recorded, `reports/round-7/validation.json` → `evidence_sha256`):
  - `reports/round-7/run-validation.py` sha256 `c3b8418445d03bee2ba394ab6e4e4767e5ef07168c1a70dc904b3813e878c1e7` (1192 lines) — **the defect is here**
  - `tools/check-evidence-coupling.py` sha256 `849494b0c4113885223f6d865110cd34ed6bb3aeec8b449d020f7b571eb2197e` — **not in this path** (sweep below)
  - inputs used by the reproduction: `reports/round-7/parent-source-spotchecks.json` sha256 `d77c8cd8d4694ab9471617b108877471626a78db6016d0d51f63ecc7c2869c64`, `reports/round-7/parent-reconciliation.json` sha256 `5034d0a61111d59adf2040b5ed52fdf152b815b02e3622e4da35ce50866e4f52`
- No file outside this diagnosis was written; no round-7 artifact was edited. Reproduction scripts live in a disposable `/tmp` scratch dir and are inlined below so they can be re-run.

## 1. Reproduction (fail-before), exact command and output

Driver (inlined; saved to `/tmp/r8o01/repro.py`, run from the lane repo root):

```python
import copy, importlib.util, json
REPO = "/home/vgpnk/Projects/shokunin/kotodama-shokunin"
spec = importlib.util.spec_from_file_location("r7", REPO + "/reports/round-7/run-validation.py")
r7 = importlib.util.module_from_spec(spec); spec.loader.exec_module(r7)
recon = r7.load("reports/round-7/parent-reconciliation.json")
spot  = r7.load("reports/round-7/parent-source-spotchecks.json")
bundle = r7.f_bundle_with(recon, spot)

# A. unmutated baseline
print("A", json.dumps(r7.measure_f_parents(bundle["reconciliation"], bundle["spotchecks"],
                                           bundle["targets"], bundle["ledgers"]), sort_keys=True))

# B. the exact mutation from run-validation.py:435-438
b = copy.deepcopy(bundle)
clone = dict(b["spotchecks"]["checks"][0]); clone["id"] = "PX99"
b["spotchecks"]["checks"] = [clone, dict(clone)]
try: r7.measure_f_parents(b["reconciliation"], b["spotchecks"], b["targets"], b["ledgers"])
except ValueError as e: print("B", e)

# E. whole parent negative-control battery
try: r7.f_negative_controls(copy.deepcopy(bundle), True)
except ValueError as e: print("E", e)
```

Command: `python3 /tmp/r8o01/repro.py` (2026-10-17). Output:

```
A {"parent_checks": 2, "parent_dispositions": {"partial-support": 2, "scoped-support": 3},
   "parent_distinct_passage_keys": 2, "parent_distinct_refetch_urls": 2, "reconciliation_rows": 5}
B ValueError: parent check identity collision
E ValueError: wrong rejection for duplicate-parent-receipt-does-not-inflate: parent check identity collision
```

`E` is byte-identical to the string filed in `reports/round-7/validation.json:6`. Note `A`: the **unmutated** parent measurement is clean (2 checks, 2 distinct passage keys, 2 distinct refetch URLs, dispositions 3 scoped + 2 partial) — the defect is entirely inside the control battery, not in the round-7 data.

## 2. Code path (file:line, `reports/round-7/run-validation.py`)

1. `main()` → `:1080` `negatives = f_negative_controls(bundle, parents_present=True)`
2. `f_negative_controls` `:386` → parent branch `:428` → control declared `:440-441`:
   `reject("duplicate-parent-receipt-does-not-inflate", duplicate_parent_receipt, "fewer than two distinct parent passage receipts", mutate_parents=True)`
3. mutation `:435-438` — clones `checks[0]`, relabels **both** copies `PX99`, so the receipt list becomes `[PX99, PX99]` with identical content
4. `reject` closure `:389-404` → `:394-395` dispatches to `measure_f_parents(...)`
5. `measure_f_parents` `:282` → **`:313-315`**
   `require(len(checks) == len({check["id"] for check in checks}), "parent check identity collision")` → raises
6. back in `reject` `:398-400`: `require(expected in str(error), f"wrong rejection for {name}: {error}")` → raises `wrong rejection for duplicate-parent-receipt-does-not-inflate: parent check identity collision`
7. `main` `:1091-1094` catches `ValueError` → `report["claims"]["F"] = {"passed": False, "error": str(error)}` → filed as `reports/round-7/validation.json` claims.F

The guard the control *expects* to fire is `:336-337` (`require(len(parent_keys) >= 2, f"fewer than two distinct parent passage receipts: {len(parent_keys)}")`), which sits **after** the identity guard at `:313-315`. The identity guard therefore always wins when the mutation repeats a label — the expected diagnostic is unreachable for this mutation.

## 3. Root cause

**RC-1 (primary): the collision guard's predicate is `count(checks) == count(distinct labels)`, which is not a collision test.**
A collision in the sense that matters is *one label bound to two different receipts* (ambiguous provenance: which record does `row_id` bind to, which prose is authoritative?). `len(set(...))` instead forbids **any** repeated label, including a byte-identical duplicate receipt that binds the same row to the same passage. Two distinct properties are conflated:

| property | what it protects | correct predicate |
|---|---|---|
| label ambiguity (genuine collision) | diagnostics and provenance: one id must not denote two different receipts | ∃ label with ≥2 **distinct receipt identities** |
| receipt redundancy (benign duplicate) | nothing — it adds no information | none (dedupe silently) |
| anti-inflation | the ≥2 distinct-passage / ≥2 distinct-URL minimums | already enforced by `parent_keys` / `parent_urls` being **sets** (`:316-317`, `:333-339`) |

**RC-2: the anti-inflation property the control exists to prove is carried by set semantics, not by the label guard.** `passage_key` `:136-138` = `(url, NFKC-normalized locator, excerpt)`; `parent_keys.add(key)` at `:334` makes duplicate receipts count once. Any duplicate receipt — same label or relabeled — leaves `len(parent_keys)` at 1, so `:336` fires. The label guard contributes nothing to non-inflation; it only rejects label reuse.

**RC-3 (contributing): the mutation is label-degenerate.** `:435-438` sets `clone["id"] = "PX99"` and then emits `[clone, dict(clone)]` — both entries carry `PX99`. The mutation was evidently meant as "a receipt plus its relabeled copy", which would need one distinct label per record. As written it trips RC-1's guard first, so the control tests the label guard rather than the counting rule it names.

**RC-4 (attribution defect): the `reject` helper cannot distinguish "wrong diagnostic" from "the harness itself is broken".** `:399-400` reports `wrong rejection for <control>`; the same wording would appear if an unrelated guard regressed. The control's own name is the only hint, and the filed error text reads as a control failure while the actual fault is in the guard. A control record should name the guard that fired.

**Scope sweep (negative claim):** `tools/check-evidence-coupling.py` contains **0** occurrences of `spotcheck` and **1** of `identity` (`:48`, the unrelated wording `object, material identity or gate-name anchor mismatch`); command `grep -c "spotcheck" tools/check-evidence-coupling.py` → `0`, `grep -n "identity" tools/check-evidence-coupling.py` → `48:...gate-name anchor mismatch` (2026-10-17). The guard is not on the F parent-check path; the defect is confined to `reports/round-7/run-validation.py:313-315`.

**Lineage:** the same count-vs-label-set guard exists in the previous round at `reports/round-6/run-validation.py:144`. Round 6's duplicate control (`:202-209`, `duplicate-passage-inflation`) mutates **passages**, not the check list, so it never collided. Round 7 added a check-level duplicate control and thereby exposed the guard's semantics for the first time.

**No genuine-collision control exists:** the complete round-7 control list (`grep -n 'reject("' reports/round-7/run-validation.py` → lines 409, 410, 413, 416, 426, 440, 442, 444, 448, 452; 10 controls) contains no case of one label bound to two different receipts. So today nothing pins the guard's intended behavior in either direction.

## 4. Minimal correct semantics (normative spec for R8-O02)

Definitions (all normalization reused from the harness so identity and counting cannot drift):

- **label** `L = check["id"]`
- **receipt identity** `R = (row_id, url(source_url), source_kind, norm(locator), norm(excerpt))` — the fields that bind a receipt to a source row and passage; `norm` = the harness's existing NFKC + whitespace normalization (`passage_key`, `:136-138`, plus `url()`), i.e. `R` extends `passage_key` with `row_id` and `source_kind`.
- **passage key** `P = passage_key(source_url, locator, excerpt)` (unchanged, `:136-138`)
- Non-binding fields (`basis`, `limits`, `accessed_at`, `retrieval_method`, `language_and_mediation`, `excerpt_form`, `citation`) must **not** enter `R`.

Rules:

- **S1 (genuine collision → reject).** Group checks by `L`. If any label group contains ≥2 distinct `R`, reject with
  `parent check identity collision: <label>` (label named for attribution, RC-4). Comparison is exact on the `R` tuple after normalization.
- **S2 (benign duplicate → accept into measurement).** Repeated labels whose members share one `R` are **not** a collision. They may be deduplicated to one representative per label (readability only — no counting property depends on it, because `parent_keys`/`parent_urls` are sets).
- **S3 (counting unchanged).** `parent_keys`, `parent_urls`, `len(parent_keys) >= 2`, `len(parent_urls) >= 2` (`:333-339`) keep exactly their current set semantics and diagnostics. Anti-inflation remains enforced here, never by label counting.
- **S4 (per-check binding checks unchanged).** `:318-332` (`row_id ∈ FIXED_IDS`, success + `retrieved_passage` + `directly_relevant_nonbibliographic`, URL/kind match against the bound ledger row, required text fields) run over the deduplicated representatives, unchanged.
- **S5 (determinism).** Iterate label groups in sorted label order so the emitted diagnostic is reproducible.
- **S6 (positive measurement must not drift).** On the real inputs the measurement stays `parent_checks=2, parent_distinct_passage_keys=2, parent_distinct_refetch_urls=2, parent_dispositions={scoped-support: 3, partial-support: 2}`.
- **S7 (required controls, both directions).** Keep `duplicate-parent-receipt-does-not-inflate` (mutation may stay exactly as filed at `:435-438`: same label, identical content) — it must now reach the `:336` diagnostic `fewer than two distinct parent passage receipts`. Add a **new** control `genuine-parent-check-identity-collision`: same label, one binding-relevant field changed (`excerpt` or `source_url`) → must be rejected with `parent check identity collision: <label>`. Without this second control, S1 is unpinned.

Reading of the round-8 O claim, disambiguated: "accepts duplicate-parent-receipt-does-not-inflate" means **the control is recorded as passed** (the harness rejects the mutation with the expected counting diagnostic). It must **not** mean the mutated bundle measures clean — that would delete the anti-inflation property the control is named for. Under S1-S7 both readings are satisfied simultaneously: the benign duplicate passes through the collision guard and is still rejected by the counting guard.

## 5. Executable proof of the spec (fail-before / pass-after)

Shadow patch = `measure_f_parents` source with **only** the `:313-315` guard replaced (no round-7 file touched; function body taken via `inspect.getsource` and re-executed):

```python
    checks = spotchecks["checks"]
    by_label = collections.defaultdict(list)
    for check in checks:
        by_label[check["id"]].append(check)

    def receipt_identity(check):
        return (check.get("row_id"),
                url(check["source_url"], check["id"]),
                check["source_kind"],
                unicodedata.normalize("NFKC", " ".join(check["locator"].split())),
                unicodedata.normalize("NFKC", " ".join(check["excerpt"].split())))

    for label in sorted(by_label):
        require(len({receipt_identity(check) for check in by_label[label]}) == 1,
                f"parent check identity collision: {label}")
    checks = [by_label[label][0] for label in sorted(by_label)]
```

Case table — `python3 /tmp/r8o01/shadow.py` (2026-10-17), columns are the filed guard vs the shadow guard:

| case | before (round-7 `:313-315`) | after (shadow S1/S2) |
|---|---|---|
| positive baseline | ACCEPTED (2 checks / 2 keys / 2 URLs) | ACCEPTED, counts identical (S6) |
| duplicate receipt, same label `PX99`, identical content | REJECTED: `parent check identity collision` | REJECTED: `fewer than two distinct parent passage receipts: 1` ← **expected diagnostic, control passes** |
| duplicate receipt, distinct labels `PX98`/`PX99`, identical content | REJECTED: `fewer than two distinct parent passage receipts: 1` | REJECTED: same (anti-inflation intact, S3) |
| same label, differing `excerpt` | REJECTED: `parent check identity collision` | REJECTED: `parent check identity collision: P01` (S1) |
| same label, differing `source_url` | REJECTED: `parent check identity collision` | REJECTED: `parent check identity collision: P01` (S1) |
| single receipt only | REJECTED: `fewer than two distinct parent passage receipts: 1` | REJECTED: same (S3) |

Whole battery — `python3 /tmp/r8o01/battery.py` (2026-10-17), `f_negative_controls(bundle, parents_present=True)` with `measure_f_parents` rebound to the shadow:

```
fail-before: ValueError: wrong rejection for duplicate-parent-receipt-does-not-inflate: parent check identity collision
pass-after:  passed: 10
  missing-fifth-ledger: ledger ids do not match the fixed five
  invalid-result-value: invalid result value: R7-F01
  bool-like-invalid-flag: retrieved_passage is not a real boolean: R7-F01
  excerpt-over-40-tokens: excerpt over 40 whitespace tokens: R7-F01
  insufficient-entries: main passages cover fewer than three entries: 2
  duplicate-parent-receipt-does-not-inflate: fewer than two distinct parent passage receipts: 1
  wrong-disposition-mix: parent dispositions must stay conservative 3 scoped + 2 partial: {'scoped-support': 4, 'partial-support': 1}
  bad-parent-url: parent URL does not match the bound ledger row: P01
  parent-not-success: unsuccessful/non-content parent check: P01
  insufficient-parents: fewer than two distinct parent passage receipts: 1
```

10/10 controls pass, the target control now emits the diagnostic it declares, and no other control's diagnostic changed. The S7 `genuine-parent-check-identity-collision` control does not exist in round 7 and is **not** covered by this run — it must ship with the round-8 fix (row 4/5 of the case table is the fail-before/pass-after pair for it).

## 6. Handoff notes for R8-O02 and the defect inventory

- Fix lands in the round-8 harness only (`tools/harness/r8_checks.py` per targets.json R8-O02). Do not edit `reports/round-7/run-validation.py`; its filed receipt must stay reproducible, and `reports/round-7/validation.json` `evidence_sha256` pins its current digest.
- Secondary finding for the O03/O04 inventory (not part of this defect's fix): on the F error path, `main` `:1091-1094` **overwrites** `report["claims"]["F"]`, discarding the already-computed clean `parent_measurement` — which is why `reports/round-7/validation.json` shows only `{"error": ..., "passed": false}` and the 10-control battery result is lost. The round-8 harness should record partial measurements alongside the error.
- Secondary finding, attribution: `reject` `:399-400` (`wrong rejection for <control>`) cannot distinguish a wrong diagnostic from a harness regression; round-8 control records should carry the guard id that fired (per RC-4).

## 7. Limits / to-verify

- Everything above is measured against the filed round-7 artifacts at the hashes recorded in `reports/round-7/validation.json`; it is a code-path and semantics diagnosis, not a judgment about whether the round-7 F claim's substantive evidence was adequate.
- The shadow patch is a demonstration of the spec, not the shipped fix; its `receipt_identity` uses inline NFKC/whitespace normalization equivalent to the harness helpers rather than calling them (the harness exposes no separate `norm` function). O02 must reuse the harness's own normalization so identity and `passage_key` normalization cannot drift.
- `to-verify`: whether any downstream round-8 consumer reads `parent_measurement` from the round-7 receipt shape (not swept; no such consumer observed in this diagnosis).
