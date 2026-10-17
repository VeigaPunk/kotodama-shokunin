# R11-D06 — holds mapping: the round-8 typed holds -> named gate holds (claim D, `d2-typed-pipeline`)

- seat: **R11-D06** (implementation shard: holds mapping), round 11 (loop 1 of 3, build round 4 of 4), 2026-10-17
- assignment (verbatim): "DEPTH R11-D06 (holds mapping): TL-01/TL-02 holds -> named gate holds (not PHON artifacts); fragment reports/round-11/depth/shard-holds.md."
- writes: this file only. Scratch under `.scratch/D06/` (`TMPDIR=$PWD/.scratch` before every scratch-writing command; `/tmp` untouched). No tool, gate, packet, projection, baseline or earlier-round byte was edited; no commit, no push. `reports/round-{8,9,10}/**` are filed and read-only here.
- canon: NON-CANON engineering evidence. Nothing here admits a round, a capability, or a canon fact.
- stamp: 2026-10-17T22:0xZ, lane revision `e3ef171` + in-flight sibling edits; every live pin below is as-read at that stamp and is a re-read event if a hash moved.
- purpose: fix the **name mapping** the wiring depends on — which historical round-8 hold ids correspond to which live hold codes, what each live code does today (measured), and which *named* hold the D2 gate flow must carry per typed-label condition, so that the e2e's "findings == expected hold set" pin and the adapter/negative-control seats (R11-D04/D05/D17..D19) share one vocabulary.

## 0. Verdict

1. **The two historical ids are dead strings; the mapping is onto the `D2L-*` classes.** `TL-01`/`TL-02` occur **0** times in the live tool (`grep -c "TL-01\|TL-02" tools/d2-typed-labels.py` = 0, 22:07Z). The live vocabulary is `D2L-FORM-UNRESOLVED` / `D2L-DATA` / `D2L-NATIVE` / … (`tools/d2-typed-labels.py:423-431`), the round-8 design-spec's §6 contract classes. The mapping table in §2 is the table the design-spec reserved at `reports/round-8/depth/design-spec.md:581` ("ids are names, the classes in §6 are the contract").
2. **TL-01 → `D2L-FORM-UNRESOLVED` (hold) is live and exact.** The translated-label owed-form condition emits one named hold per owed slot (`tools/d2-typed-labels.py:786-797`); over `examples/culture-d2` that is exactly ten holds at `GAR-01..GAR-10`.
3. **The exchange is 1:1: ten legacy `PHON-INVENTORY` FAIL lines ↔ ten named holds, same ten records** (§3, measured as exact set equality). This is what "not PHON artifacts" means executably: the wired flow must show `PHON-INVENTORY ∩ typed_channel records = ∅` while the ten holds stay in the finding set (the aggregate stays red; nothing is laundered clean).
4. **Two live behavior gaps relative to the declared semantics remain** (both already on the round-10 record; reproduced here with fixtures): a declared sound kind with no bytes is **silent** (design-spec R5 unmet — the adapter must inject the hold per `reports/round-11/depth/design.md` §2.3/§8.3), and a kindless record makes the **CLI crash** with a raw `KeyError: 'kind'` traceback instead of the documented exit-2 stable message. Findings F-D06-1/F-D06-2.
5. **Independent corroboration of the design's expected hold set.** My re-derivation from the live projector output (identical command to `design.md` §4.1) yields exactly the design's §4 set: 15 holds + 1 note + 0 fails, same ids, same `where`s, same details (§4). Canonical `expected-holds.json` content is embedded ready-to-land in §4.3.

## 1. Mapping ground — the historical ids and the live vocabulary

Round-8 declared ids, quoted:

- `reports/round-8/depth/skill-table-draft.md:266-268`: "`lexicon.term → from the record's own layer`), or `unannotated` → `TL-02` hold. Executable holds: `TL-01` = a form slot with no native form; `TL-02` = no declared kind (`:316-320`, `:386-390`)."
- `SKILL.md:86`: "…label-only → off the sound channel **and** a hold, so the aggregate stays red (…; executable `TL-01`)"; `SKILL.md:88`: "A sound kind declared with no bytes supplied | HOLD, not clean (…; executable `TL-01`)"; `SKILL.md:90`: "A record with no declared kind at all | hold with a stable reason — the kind is never guessed from the text's language (`tools/d2-typed-labels.py` `TL-02`)".
- `SCORECARD.md:128` cites "holds (TL-01/TL-02)" for the `d2-typed-labels` row.

Round-10 already diagnosed the id drift and the tool was re-pinned to the spec vocabulary (filed): `reports/round-10/drift/shard-05.md:32-37` and `:54` ("`grep -c "TL-01"…` = **0**; live id is `D2L-FORM-UNRESOLVED` (tool:426…)"), disposition `fixed-with-control` in `reports/round-10/fix-08.md:90-96` (fresh emit and committed artifact: `TL-01` 0, `D2L-FORM-UNRESOLVED` ×20, `D2L-` ×37). Live confirmation at this stamp:

```sh
# 2026-10-17T22:07Z, lane root, TMPDIR=$PWD/.scratch
grep -c "TL-01\|TL-02" tools/d2-typed-labels.py          # 0
grep -n "FINDING_CLASSES\|^D2L_" tools/d2-typed-labels.py | head
#   423 FINDING_CLASSES = ("D2L-DATA", "D2L-FORM-UNRESOLVED", "D2L-NATIVE", "D2L-BORROW",
#        "D2L-ERA", "D2L-MATERIAL", "D2L-RANK", "D2L-SCOPE")
#   425 D2L_DATA = "D2L-DATA"; 426 D2L_FORM = "D2L-FORM-UNRESOLVED"; 427 D2L_BORROW = …
```

The contract classes are `reports/round-8/depth/design-spec.md:533-545` (§6, "ids are names, the classes in §6 are the contract"). So the mapping below is a **legacy-name → live-name → class** mapping, not a new vocabulary.

## 2. The mapping table (deliverable)

Legend — "named hold" = the finding a wired D2 run must carry for the condition, with a stable id and a record-addressed `where`; "live" = measured on the shipped tool at this stamp (receipts in §6).

| historical id | round-8 declared semantics | live code (class) | live behavior measured | wired flow's named hold | D2 instances |
|---|---|---|---|---|---|
| **TL-01a** (the ten-GAR case) | a form slot with no native form; "label-only → off the sound channel **and** a hold" (`SKILL.md:86`) | `D2L-FORM-UNRESOLVED` (§6 class: typed label with no supplied sound form; `tools/d2-typed-labels.py:426`) | exit 1; one **hold** per owed slot: `{code: D2L-FORM-UNRESOLVED, severity: hold, where: GAR-01, detail: "label_id LEX-GAR-01 has no supplied native/borrowed form"}` — reproduced live ×10 | **`D2L-FORM-UNRESOLVED` hold @ `<record>`**, carried by the adapter's routing row (`hold: D2L-FORM-UNRESOLVED`, `design.md` §2.2/§2.3) | `GAR-01..GAR-10` (label_id `LEX-GAR-01..10`), source `11-costumes.yml` field `garment` |
| **TL-01b** (R5 class) | a sound kind declared with no bytes supplied → `D2L-FORM-UNRESOLVED` HOLD (`design-spec.md:174-176`; `SKILL.md:88`) | `D2L-FORM-UNRESOLVED` (contract) | **silent** — library probe `native-form` + `status: to-verify`, no bytes, field issues declared: exit 0, zero findings; CLI probe: zero findings for the probe record. No code path emits R5: `check_sound_form` returns for any non-supplied status (`tools/d2-typed-labels.py:668-673`) and `validate_labels` has no other branch for it | **`D2L-FORM-UNRESOLVED` hold**, injected by the adapter (per `design.md` §2.3 row 3 and §8.3) until the projector implements R5; the deviation is a projector finding, never a silent typed-packet patch | none today in D2 (no such record in the ten routed rows); the class exists for the wiring + negative control D18 |
| **TL-02** | no declared kind → "hold with a stable reason — the kind is never guessed" (`SKILL.md:90`) | `D2L-DATA` (§6 class: malformed input / schema; `tools/d2-typed-labels.py:425`) | library: exit 2, two **fails** (`required field 'kind' is missing`; `kind None is not one of (…)`) — i.e. the spec's §1.2 L1 malformed rule (`design-spec.md:537`). CLI: **raw `KeyError: 'kind'` traceback at `tools/d2-typed-labels.py:2497`**, exit 1 — violates the tool's own documented contract ("exit 2 … stable message, no traceback", `tools/d2-typed-labels.py:40-42`) | **`D2L-DATA` exit-2 refusals** — a malformed packet is could-not-evaluate, never a hold and never a pass; the wired CLI must keep the stable-message discipline | none in D2 (all 58 labels carry a kind) |
| (context row) | a supplied native form that violates the declared profile with a declared diacritic | `D2L-NATIVE` (hold-for-owner, integration reclassification `tools/d2-typed-labels.py:2285-2311`) | exit 1; ×2 holds `@ L-15` `sára`, `@ L-16` `sará` | kept in the hold set unchanged (design §4.2 items 11-12); on the **checked** channel, not off-channel | `L-15`, `L-16` |

Reading: TL-01 splits into two live rows (a: translated-label owed form — the D2 fact; b: R5 no-bytes — projected class, currently silent); TL-02 is not a hold live but the malformed-input class. Only TL-01a produces holds in `examples/culture-d2` today, and it produces exactly one per routed record.

## 3. Worked instance — the ten-line exchange over `examples/culture-d2`

### 3.1 Both sides, measured

```sh
# 2026-10-17T22:0xZ, lane root, TMPDIR=$PWD/.scratch
python3 tools/gates/naming-collision-gate.py examples/culture-d2/packet.d2.yml \
        > .scratch/D06/naming-collision-gate.out 2>&1     # exit 1; 17 lines; sha256 ebc8850d08ec1b7e32616cbca9092ba66f3b6f148a61515a033e6bed6fa66f4b
#   10 PHON-INVENTORY (GAR-01..GAR-10), 6 NAME-NEAR (era labels), 1 CROSS-HOLD
python3 tools/d2-typed-labels.py --json > .scratch/D06/typed-live.json   # exit 1; stats {fail: 0, hold: 15, note: 1, labels: 58}
#   10 D2L-FORM-UNRESOLVED holds @ GAR-01..GAR-10, 2 D2L-NATIVE holds @ L-15/L-16, 4 D2L-RANK (3 hold + 1 note)
grep -c "PHON-INVENTORY" tools/gates/frozen/round-4/naming-collision-gate.out   # 10 (frozen round-4, all GAR-*)
```

The naming-gate stdout sha256 `ebc8850d…` equals the one recorded independently in `reports/round-11/depth/design.md` §1.1 — same bytes, different seats. The frozen round-4 file shows the class was exactly these ten all along (`corpus/lessons/round-4-sol-fixes-and-audits.md:28`).

### 3.2 The 1:1 table (record-level exchange)

| record | legacy line (offending symbol @ position) | gloss (first 44 chars) | named hold the wired flow carries | owed slot |
|---|---|---|---|---|
| GAR-01 | `/v/` @ 7 | winter valley coat (heavy felted wool; uncom… | `D2L-FORM-UNRESOLVED` hold | `LEX-GAR-01` |
| GAR-02 | `/-/` @ 5 | high-pasture coat (fine first-shear felt; na… | `D2L-FORM-UNRESOLVED` hold | `LEX-GAR-02` |
| GAR-03 | `/c/` @ 8 | transit coat (felted outer; fringed hem-cord… | `D2L-FORM-UNRESOLVED` hold | `LEX-GAR-03` |
| GAR-04 | `/-/` @ 8 | lowland-cloth coat (woven plant-thread cloth… | `D2L-FORM-UNRESOLVED` hold | `LEX-GAR-04` |
| GAR-05 | `/-/` @ 5 | mast-sash (narrow woven wool band, lineage-i… | `D2L-FORM-UNRESOLVED` hold | `LEX-GAR-05` |
| GAR-06 | `/'/` @ 9 | stranger's fair coat (flat-woven lowland cut… | `D2L-FORM-UNRESOLVED` hold | `LEX-GAR-06` |
| GAR-07 | `/c/` @ 9 | mourning coat (felt left shaggy, undyed, hem… | `D2L-FORM-UNRESOLVED` hold | `LEX-GAR-07` |
| GAR-08 | `/c/` @ 5 | bale cord (imported plant-thread cord in coi… | `D2L-FORM-UNRESOLVED` hold | `LEX-GAR-08` |
| GAR-09 | `/-/` @ 10 | down under-tunic (combed pack-ox underfleece… | `D2L-FORM-UNRESOLVED` hold | `LEX-GAR-09` |
| GAR-10 | `/(/` @ 12 | gale legging (smoke-cured leather, wind-cut:… | `D2L-FORM-UNRESOLVED` hold | `LEX-GAR-10` |

Set-equality check (script `.scratch/D06/table-extract.txt`, run 22:04Z): PHON-line record set = hold `where` set = `{GAR-01 … GAR-10}` — `exact 1:1: True`, no extra record on either side.

### 3.3 What "not PHON artifacts" means executably (assertions for L2/L3 seats)

1. **Typed run:** `PHON-INVENTORY` lines naming a `typed_channel` record = **0**. (Legacy run: 10 — the minus-basis; the design's L2 differential, `design.md` §1.3/§3.1, is exactly this set.)
2. **Hold set:** `D2L-FORM-UNRESOLVED` holds @ `typed_channel` records = **10** (one per routed row), i.e. the exchange removes an artifact per record and clears nothing (`reports/round-8/depth/skill-table-draft.md:105-146` "removes an artifact; it does not clear the name").
3. **No laundering:** the ten holds are in the pinned hold set (§4) at severity `hold`; dropping one drops the count to 14 (negative control D18), downgrading one to `note` breaks the note pin (D19).

## 4. The re-derived expected hold set (label-channel contribution + canonical content)

### 4.1 Independent re-derivation

Same command as `design.md` §4.1 (`python3 tools/d2-typed-labels.py --json`, exit 1), run and parsed by this seat at 22:06Z. Result, sorted `(id, where)`: **holds 15 = 10× `D2L-FORM-UNRESOLVED` @ GAR-01..10 + 2× `D2L-NATIVE` @ L-15/L-16 + 3× `D2L-RANK`; notes 1 = `D2L-RANK` @ `SR-01#a|SR-01#b`; fails 0.** Identical id/`where`/`detail` to `design.md` §4.2-4.3 — independent corroboration, different seat, different run.

Label-channel rows (this shard's mapping scope): the ten §3.2 holds plus the two `D2L-NATIVE` rows; the rank-channel rows are carried for set completeness only (rank adapter seat's scope).

### 4.2 Counts the wired e2e must pin

`counts = {hold: 15, note: 1, fail: 0}`; comparison key `(id, severity, where)` as a set, details pinned (design §4.4).

### 4.3 Canonical `expected-holds.json` content (ready to land)

Per `design.md:299`/§4.5 and the interface map at `design.md:408`, the file `examples/culture-d2/expected-holds.json` is seat D06's interface duty; my dispatch names only this fragment, so the content is embedded here (sha256 of the scratch original `.scratch/D06/canonical-holds.json`, same content, pretty-printed: `e9444f94fd201285d10bbb135f2355cc10430b7f0acc67abad556e345c2a5114`; regenerate from the live run, never hand-edit):

```json
{"schema": "kotodama-typed-pipeline-holds-v1",
 "packet_sha256": "e0f21509e14ac03ed5747e6bbbb48183cbe56d6b61afff8c8475e4a50137b643",
 "projection_sha256": "e70ba1477dbeb830061db6fd12516b7d902587bddae173f55a3650015d380b2f",
 "projector_sha256": "0da0015f700345c938184cb45ca07178c33e98f798c3c09729007487fb89c802",
 "counts": {"hold": 15, "note": 1, "fail": 0},
 "holds": [
  {"id": "D2L-FORM-UNRESOLVED", "severity": "hold", "where": "GAR-01", "detail": "label_id LEX-GAR-01 has no supplied native/borrowed form"},
  {"id": "D2L-FORM-UNRESOLVED", "severity": "hold", "where": "GAR-02", "detail": "label_id LEX-GAR-02 has no supplied native/borrowed form"},
  {"id": "D2L-FORM-UNRESOLVED", "severity": "hold", "where": "GAR-03", "detail": "label_id LEX-GAR-03 has no supplied native/borrowed form"},
  {"id": "D2L-FORM-UNRESOLVED", "severity": "hold", "where": "GAR-04", "detail": "label_id LEX-GAR-04 has no supplied native/borrowed form"},
  {"id": "D2L-FORM-UNRESOLVED", "severity": "hold", "where": "GAR-05", "detail": "label_id LEX-GAR-05 has no supplied native/borrowed form"},
  {"id": "D2L-FORM-UNRESOLVED", "severity": "hold", "where": "GAR-06", "detail": "label_id LEX-GAR-06 has no supplied native/borrowed form"},
  {"id": "D2L-FORM-UNRESOLVED", "severity": "hold", "where": "GAR-07", "detail": "label_id LEX-GAR-07 has no supplied native/borrowed form"},
  {"id": "D2L-FORM-UNRESOLVED", "severity": "hold", "where": "GAR-08", "detail": "label_id LEX-GAR-08 has no supplied native/borrowed form"},
  {"id": "D2L-FORM-UNRESOLVED", "severity": "hold", "where": "GAR-09", "detail": "label_id LEX-GAR-09 has no supplied native/borrowed form"},
  {"id": "D2L-FORM-UNRESOLVED", "severity": "hold", "where": "GAR-10", "detail": "label_id LEX-GAR-10 has no supplied native/borrowed form"},
  {"id": "D2L-NATIVE", "severity": "hold", "where": "L-15", "detail": "supplied form 'sára' carries symbols outside the declared inventory: ['á'] — but the offending symbol(s) ['á'] are acute-accented vowels, the accent mark 02-phonology.yml declares by its own minimal pair (02-phonology.yml:73 sara [sára] vs sara [sará]); the segment inventory is not the test for a diacritic, so this is held for the form's owner rather than failed"},
  {"id": "D2L-NATIVE", "severity": "hold", "where": "L-16", "detail": "supplied form 'sará' carries symbols outside the declared inventory: ['á'] — but the offending symbol(s) ['á'] are acute-accented vowels, the accent mark 02-phonology.yml declares by its own minimal pair (02-phonology.yml:73 sara [sára] vs sara [sará]); the segment inventory is not the test for a diacritic, so this is held for the form's owner rather than failed"},
  {"id": "D2L-RANK", "severity": "hold", "where": "TR-04#a|TR-06#a", "detail": "act-collision: genuine-priority-gap"},
  {"id": "D2L-RANK", "severity": "hold", "where": "WR-02#g|WR-09#g", "detail": "R-05-class: genuine-priority-gap"},
  {"id": "D2L-RANK", "severity": "hold", "where": "WR-08#g|WR-09#g", "detail": "R-05-class: genuine-priority-gap"}],
 "notes": [
  {"id": "D2L-RANK", "severity": "note", "where": "SR-01#a|SR-01#b", "detail": "act-collision: band-keyed-pair"}]}
```

(The committed file, when landed, should carry this content in canonical pretty JSON; the scratch original is `.scratch/D06/canonical-holds.json`, 3,434 bytes.)

## 5. Findings for the wiring (evidence-first)

- **F-D06-1 — R5 is unimplemented; the adapter must inject the hold.** Contract: `design-spec.md:174-176` ("R5 declared sound kind with `status: absent`/`to-verify` ⇒ `D2L-FORM-UNRESOLVED` HOLD… a claim without bytes is not a pass"). Live: library probe (`native-form`, `to-verify`, no bytes, field issues declared) → **exit 0, zero findings**; the code has no branch (`check_sound_form` returns for non-supplied statuses, `tools/d2-typed-labels.py:668-673`; `validate_labels` handles only translated-label owed forms). Consequence for this claim: "owed native forms are carried as named holds" holds for the ten D2 rows but a same-class record in any future packet would pass silently unless the adapter carries the hold. Disposition per design `§2.3` row 3 + `§8.3`: adapter injects; report as projector deviation. (Same gap as round-10 shard-05 N2, reproduced here independently.)
- **F-D06-2 — kindless records: fail is spec-correct, the CLI crash is a defect.** The malformed classification (`D2L-DATA`, exit 2) matches `design-spec.md:533-544` §6 (the `D2L-DATA` row `:537`; rule §1.2 L1) and `SKILL.md:90`'s "the kind is never guessed" — but `SKILL.md:90`'s word "hold" and `skill-table-draft.md:266-268`'s "`TL-02` hold" are stale versus both the spec and the live behavior. The CLI crash: `KeyError: 'kind'` at `tools/d2-typed-labels.py:2497` (the `labels_by_kind` comprehension inside the coverage block, `:2494-2500`), exit 1 with traceback, against the tool's own contract ("exit codes … 2 = malformed input …, stable message, no traceback", `:40-42`). It only triggers on packets that reach the coverage block with kindless labels; the wired pipeline's malformed controls (D16) should include it so the crash cannot be mistaken for a finding.
- **F-D06-3 — label-channel accounting divergence (small, must be decided once).** The committed projection's `coverage` block reports `label_findings_fail: 2, label_findings_hold: 10` (sourced from parser-layer stats, `tools/d2-typed-labels.py:2494-2500`), while the artifact's own `findings` rows carry those same two `D2L-NATIVE` findings at severity **hold** (integration-layer reclassification, `:2285-2311`). Both statements are live in one file. The wired e2e pins one layer only (the report/`--json` layer, per `design.md` §4.4): `fail = 0`, `hold = 15`. Recorded so the L3 seat pins the right layer and the D21 reviewer sees it named, not accidental.
- **F-D06-4 (context, not this shard's fix) — the committed projection is stale by one pin line.** `python3 tools/d2-typed-labels.py --check` exit 1 (22:07Z): the projection's `assembly.packet_sha256` is `8da90b07…` while the packet hashes `e0f21509…`. The mapping above is unaffected (finding set identical across the two runs), and design §5.1 fixes the one-line re-pin; recorded here because the canonical §4.3 pins must be re-read after the re-pin (`expected-holds.json`'s `projection_sha256` will move when the re-pinned bytes land).

## 6. Method and receipts

Probe fixtures (scratch, `TMPDIR=$PWD/.scratch`, all under `.scratch/D06/`):

- `.scratch/D06/probe.py` — library probes through the shipped tool's own `parse_typed_labels` (runpy import; the same surface the tool's selftest controls use) over four packets: (C) the shipped `GAR-01` label verbatim; (K) the same record with `kind` omitted; (R5) `native-form`+`to-verify`, no bytes, field issues declared; (R5b) `borrowed-strata`+`absent` with no issues.
- `.scratch/D06/probe-{ctl,kindless,nobytes}.yml` — minimal CLI packets (eras + one material + one costume + one explicit typed label), driven through `python3 tools/d2-typed-labels.py --packet <fixture> --json`. Fixture note for the test seats: the YAML loader keeps `null` as the *string* `"null"` for these fields — omit the key to make a field legally absent; writing `representation: null` produces a representation-vocabulary `D2L-DATA` fail instead of the silent-status case.

Observed (receipts `.scratch/D06/probe-receipt.txt`, `cli-*.json`, `*.err`):

| probe | surface | exit | key output |
|---|---|---|---|
| C control | library | 1 | `D2L-FORM-UNRESOLVED` hold @ GAR-01 |
| K kindless | library | 2 | `D2L-DATA` ×2 fail (`required field 'kind' is missing`; `kind None is not one of …`) |
| K kindless | CLI | **1** | raw `KeyError: 'kind'` traceback at `tools/d2-typed-labels.py:2497` |
| R5 no-bytes | library | **0** | no findings |
| R5 no-bytes | CLI | 1 | zero findings for the probe record (exit 1 is the unrelated GAR-01 hold) |
| R5b absent-kind, no issues | library | 2 | `D2L-DATA` ×2 (null-field issue rule) — not an R5 hold |
| ctl | CLI | 1 | holds for both the costume-projected GAR-01 and the explicit probe label |

Standing pins at stamp (sha256): `tools/d2-typed-labels.py` `0da0015f…`, `tools/assemble-d2.py` `8ea6bdde…`, `examples/culture-d2/packet.d2.yml` `e0f21509…`, `examples/culture-d2/typed-labels.d2.yml` `e70ba147…`, `tools/gates/naming-collision-gate.py` `d9e4e8f4…`; `--selftest` 39/39 exit 0; `--check` exit 1 (F-D06-4). Producer-file hashes in §1-§3 are of scratch receipts.

## 7. Limits and handoff

- **Scope note for the parent/integrator.** `design.md:408` assigns seat **D06** the file `examples/culture-d2/expected-holds.json` (§4.5); this dispatch names only `reports/round-11/depth/shard-holds.md`. I did not write the JSON file (write-scope rule); §4.3 carries its exact content, sha-pinned, so the owner can land it mechanically. If the intent was for this seat to land it, that is a one-command action: write §4.3's JSON to `examples/culture-d2/expected-holds.json`.
- **What this fragment vouches for.** The name mapping, the 1:1 exchange, the live behavior of each hold class, and the re-derivation of the expected set — each with a command and a hash. It does not vouch for the adapter/gate seats' code (D03/D05), the re-pin (D07), or the freeze (D08); those are checked by their own fragments and the reviewers.
- **Adjacent observation while tying evidence (reported, not absorbed; not this seat's write).** At 22:0xZ the lane worktree shows unstaged rewrites of **filed** round artifacts: `reports/round-{5,6,7,8,9}/validation.json` (mtimes 19:03:00-19:03:17 local = 22:03Z; `git diff --stat`: 6 files, +125/-859; e.g. round-8's `acceptance_checks_passed` true→false with a new D-failure string) and `reports/round-10/coverage/index-update-22.md`. None of my commands write those paths (my receipts are scratch-only; `reports/round-11/run-validation.py:6` declares it "never edits the evidence it reads"). Round-10 has the precedent: filed-receipt rewrites were reverted by the integrator and the staleness documented instead. Recommend the integrator inspect who wrote them and restore the filed bytes (e.g. `git checkout --` on those paths) before any round-11 admission reads a filed validation.json.
- **Out of province (report, never absorb).** Canon status of the ten owed garment forms, and whether an English gloss is ever a licensable in-world name, are lore questions (`PROVINCE.md`).
