# R11-D23 — reviewer: SKILL.md label-typing table vs the wired behavior

- seat: **R11-D23** (adversarial reviewer), round 11 (loop 1 of 3, build round
  4 of 4), 2026-10-17
- assignment (verbatim): "DEPTH R11-D23 (reviewer): cross-check SKILL.md
  label-typing table claims vs the wired behavior; staleness = finding;
  reports/round-11/depth/review-23.md."
- writes: this file only (scratch under `.scratch/rev23/`). No tool, gate,
  packet, component, baseline, manifest, `SKILL.md` or earlier-round byte is
  edited by this seat. `reports/round-{8,9,10}/**` and
  `tools/gates/{frozen,expected}/**` are read-only here.
- canon: NON-CANON engineering review. Nothing here admits a round, a
  capability or a canon fact; the lane's domain claims are untouched.
- clock: all stamps UTC (`date -u +%FT%TZ`); local is UTC-03:00.
- status: **COMPLETE** — pre-wiring phase measured 22:00–22:08Z, post-wiring
  phase measured 22:12–22:19Z, both 2026-10-17. The wiring landed mid-review
  under different filenames than the design planned (see §6); everything below
  that says "wired" was measured on the delivered revisions.
- pins at the post-wiring stamp: lane HEAD `e3ef1719c123ab4fb83ed94e033961dd61a2e8c7`
  (`e3ef171`, the round-11 claims commit; no round-11 commit was made during
  this review); `SKILL.md` `52d5f4d1be6ac97a143323306eafa9c9649484f25de60de8a3ee7630d8c6792c`
  (unchanged through the wiring); `tools/d2-typed-labels.py`
  `0da0015f700345c938184cb45ca07178c33e98f798c3c09729007487fb89c802`;
  `tools/assemble-d2.py` `8ea6bdde9514ee966fe58cf219d4d0228ecc3b041e30549c68073cc822c8655d`;
  `tools/typed-gate-flow.py` **under active edit during this review** — `ae55e6fa…`
  at 22:12Z → `a7e1224f…` (22:17Z) → `5758e315…` (22:18:09Z local, last observed
  at 22:19Z). Every measured leg was re-run green at each observed revision
  (e2e 10/10, `--check` 0, `--selftest` 0, replay 10/10, 16 findings / 15
  holds + 1 note), and the findings stayed identical across all three; the
  rows below cite the `a7e1224f…`/`5758e315…` runs, §6.1/§6.2. Admission must
  re-verify at the frozen revision;
  `examples/culture-d2/typed-labels.d2.yml` `a3aa452cd5ae77c351d9532a707fb1f1ababf77c3fad8b9d28089e6958364a43`;
  `examples/culture-d2/packet.d2.typed.yml` `e8a83445e46deadde358e3ebb20c2d47decee91d3f2a1341d28ebfe6934e09bb`;
  `examples/culture-d2/typed-gate.expected.json` `7ed597317b32b238d880af0a602fcbfa1ffd92608008879f049db9fd02aa03aa`
  (`e962849a…` at 22:12Z, re-emitted to `7ed59731…` with the second tool
  revision);
  `tools/gates/frozen/round-11/MANIFEST.tsv` `4ddb911ced45288533b8f3dadc76a339b966f31611351a9b86645349d5904376`
  (unchanged across all observed revisions).

## 0. Verdict — final

**The wired flow keeps the table's core promise; the table itself does not yet
describe the wired flow.** The pipeline over `examples/culture-d2` now exits 0
with findings exactly equal to the expected set (15 holds + 1 note + 0 fails),
the ten translated labels leave the sound channel with the ten
`PHON-INVENTORY` artifacts retired exactly (10 removed, 0 added, every other
gate line byte-identical), the ten owed slots are carried as named
`D2L-FORM-UNRESOLVED` holds and cross-checked against the component's own
`form_slot` declarations, the projection's stale pin is re-emitted green, and
the new round-11 frozen generation replays 10/10 (all receipts §6).

Against the SKILL.md label-typing region (lines 31–98), four problem classes
remain — all measured at the wired surface as well as the projector:

- **F1 — R5 silent pass (high).** "A declared sound kind with no bytes →
  `D2L-FORM-UNRESOLVED` HOLD, never clean" (SKILL.md:44, :88, :54) still fails
  at both surfaces: the projector emits no hold, and the wired flow carries no
  adapter injection for the class (design `§8.3` ordered the adapter to inject
  it; the delivered adapter does not). Latent for D2, which has no such
  record; false as a general promise. §4 F1.
- **F2 — kindless record crashes (high).** "Hold with a stable reason"
  (SKILL.md:90) fails at both surfaces: an unhandled `KeyError: 'kind'`
  traceback at `tools/d2-typed-labels.py:2497` propagates through the wired
  entry point (exit 1 + traceback). The correct class per the design authority
  is a stable exit-2 `D2L-DATA` refusal (`design-spec.md:127-129`), so :90
  also carries the wrong class word ("hold"). §4 F2.
- **F3 — borrow-ledger check unenforced (medium).** One of the five checks the
  table names at :45 ("domain/register declared") has no code path; the probe
  emits no `D2L-BORROW`. §4 F3.
- **F4 — "never on the … identity channel" is imprecise (low; latent).** The
  wiring routes labels via the gate's `compare_only` ("key-equivalence checks
  only"); the glosses leave the sound/similarity channels but remain
  key-equivalence participants in layers 1–4. No finding fires on this data.
  §4 F4.
- **S1–S3 — staleness (medium/low).** `TL-01`/`TL-02` (SKILL.md:86, :88, :90),
  `FIELD_DEFAULTS` + the retired kind names (:98) do not exist in the live
  tool; seven corpus pointers are off by 2–3 lines (:92, :93, :94, :95, :97,
  :99, :100); the T3 range at :58 ends two rows early. `SKILL.md` is byte-
  unchanged (`52d5f4d1…`, `git diff e3ef171` empty), so all of these are open
  for the orchestrator's admission edit. §3.

Verified true (with receipts in §5): the ten-GAR-label class at :42/:85;
native-bytes-govern at :43/:87 (probe R4); the label-only hold's semantics at
:86; borrow checks B1–B4; the untyped-legacy channel at :47/:89 at the legacy
surface; `compare_only` misuse at :91; T2's first two clauses; T4.

## 1. Scope and method

Review object: the label-typing region of `SKILL.md` — intro block (:31–:38),
the six-row condition table (:40–:47), thresholds T1–T5 (:49–:65), the three
cautions (:67–:73), and every error-pattern row that names a typing behavior or
an executable (:85–:100).

Cross-checked at three surfaces:

1. **projector** — `python3 tools/d2-typed-labels.py …` over the live packet
   and over probe packets in `.scratch/rev23/` (`probe-kindless.yml`,
   `probe-nobytes2*.yml`, `probe-absent.yml`, `probe-r4*.yml`,
   `probe-b5*.yml`, `probe-compare.yml`, and `packet-r5.yml` = the live packet
   plus one injected R5-class record);
2. **legacy gate bundle** — the five gates over the raw packet (the "before");
3. **wired flow** — `python3 tools/typed-gate-flow.py` and its `--json`,
   `--selftest`, `--check`, `--packet` modes, plus the round-11 frozen replay.

All probe packets carry the declared inventory (`consonants: [p, t, k, m, n,
s, r, l]`, `vowels: [a, e, i, o, u]`); a first probe round without it read the
empty inventory and is superseded. The staleness checks re-verify, at
`e3ef171`, the items round-10's `reports/round-10/drift/shard-05.md` §2 counted
stale-documented, each by `grep -n` against the live files.

Cross-corroboration is named where it exists, not absorbed: R11-D06's mapping
fragment (`reports/round-11/depth/shard-holds.md`) independently reproduces F1
and F2 (its F-D06-1/F-D06-2) and refined F2's class reading; `design.md` §8.3
names F1 as a carried defect and orders the adapter to compensate.

## 2. Claim-by-claim cross-check — final

Verdict key: **holds** = measured behavior matches; **contradicted** = measured
behavior is the opposite; **stale-cite** = pointer or identifier does not
resolve (finding per assignment); **partial** = some clauses hold, some do not.

| SKILL.md | claim (condensed) | verdict after wiring | evidence |
|---|---|---|---|
| :33–:35 | type every form-bearing record before any gate reads it; gloss never the checked form; loan never typed by look | **holds for the typed run; qualified** — the typed run's gates read the typed packet (labels `compare_only`); the legacy run remains, by design, as the differential's minus-basis | §6.1, §6.3; V7 |
| :35 | executable authority `tools/d2-typed-labels.py --selftest` | **holds** — exit 0, 39/39; the wiring adds a second entry point (`typed-gate-flow.py --selftest` 14/14) that the table does not cite yet | V0, V10 |
| :36–:37 | design authority `design-spec.md` §1; receipts `skill-table-draft.md` | **holds** — both files present | paths verified |
| :38 | grounding `era-language-staging.md:108-124` | **holds loosely** — the section is :111 (heading), table :113–:123; range starts 3 lines early but covers the source | §3 |
| :42 | gloss → `translated-label`, never sound/identity channel; owed form stays held; 10/10 frozen round-4 class | **sound channel: holds (wired, measured); identity channel: partial (F4); owed form: holds (wired)** | §4 F4; V1, V7 |
| :43 | supplied native form → sound + identity; exactly one checked form; translation claim cannot waive | **holds** — L2 collision control (selftest); probe R4: claim over violating form `xaka` still FAILs on the native bytes | V2 |
| :44 | sound kind declared, no bytes → nothing checked; silent pass forbidden — `D2L-FORM-UNRESOLVED` HOLD, never clean | **contradicted at both surfaces** — projector silent; wired flow adds no injection | §4 F1 |
| :45 | borrowed-strata → recipient check + ledger: layer resolves, donor separated, substitutions reproduce, clocks ordered, domain/register declared | **four of five hold; one contradicted** — B5 ("domain/register declared") unenforced | §4 F3; V3 |
| :46 | exactly 1 discriminator → kind not asserted, `to-verify` with the discriminator named | **not executable (house rule)** — no discriminator-count path in any tool (`grep -c discriminator` = 0); coherent as human policy, not machine-checked | §4 F-note |
| :47 | untyped legacy record → unchanged channel, legacy form field still checked | **holds at the legacy surface** — the wired differential's minus-basis is exactly this: the ten glosses still produce legacy `PHON-INVENTORY` lines, retired only in the typed run | V5, V7 |
| :49–:52 (T1) | inventory **and** syllable-profile tokenization; label signature routes off channel | **partial** — segment test implemented; tokenization clause not in any executable; routing implemented as field-role typing + `compare_only`, not signature detection | §4 F-note |
| :53–:54 (T2) | one checked form per record; native bytes govern; declared no-bytes → HOLD | **first two hold; third contradicted** (F1) | V2, §4 F1 |
| :55–:58 (T3) | house rule ≥2 of 5; 1 → to-verify; 0 → native default | **not executable (house rule)**; citation boundary stale (:43-57 vs table :54–:59) | §3 S3 |
| :58 (T3 cites) | `loanword-material-dating.md:43-57` | **stale-cite (boundary)** | §3 S3 |
| :60–:62 (T4) | clock separation; B4 executable | **holds** — selftest "spec B4" family | V3 |
| :62–:65 (T5) | WOLD band calibration, never overrides packet history | **holds** — `language-contact.md` :56 heading, :58 sample, :60 rates, :62 hierarchy | §3 |
| :67–:73 | three cautions | **hold for the ten GAR labels (wired)**: the aggregate stays red with the ten holds; caution 2 does **not** hold for the R5 class (F1) | V1, V7, §4 F1 |
| :85 | English garment label fails inventory → type/hold, never rename | **holds** — wired: 10 `PHON-INVENTORY` retired in the typed run, 10 named holds carried | V1, V7 |
| :86 | label-only record passes silently → forbidden; executable `TL-01` | **semantics hold (wired: the ten holds); identifier stale** | V7, §3 S1 |
| :87 | translation claim over violating native form | **holds** — probe R4 | V2 |
| :88 | sound kind declared, no bytes → HOLD, not clean; executable `TL-01` | **contradicted (behavior) + stale (identifier)** | §4 F1, §3 S1 |
| :89 | untyped legacy label still checked | **holds at the legacy surface** | V5 |
| :90 | no declared kind → hold with a stable reason; `TL-02` | **contradicted (behavior) + stale (identifier + class word)** | §4 F2, §3 S1 |
| :91 | `compare_only` while unresolved → misuse, not a pass | **holds at the typed-label layer** — a typed label setting it emits `D2L-SCOPE` fail while the hold stands (probe `probe-compare.yml`); the wired flow sets `compare_only` on *derived gate-packet records*, not on typed labels, and carries the holds — recorded so the mechanism is not mistaken for the misuse the table forbids | V4, §6.1 |
| :92–:95, :97, :99, :100 | corpus pointers | **stale-cite** — seven pointers off by 2–3 lines | §3 S2 |
| :96 | curatorial label promotion rejected (`costume-language-coupling-table.md:43`) | **holds** — cited row is exactly :43 | §3 |
| :98 | era tags/slot glosses typed `fictional-coordinate`/`descriptive-gloss`; tool `FIELD_DEFAULTS` | **stale-cite** — none of the three identifiers exists in the live tool (three kinds ship, `KINDS` tool:414) | §3 S1 |

## 3. Findings — staleness (assignment: staleness = finding)

Checks by `grep -n`/`sed -n` at `e3ef171`, 22:06–22:07Z and re-confirmed 22:16Z
against the unchanged `SKILL.md` (`sha256sum` = `52d5f4d1…`; `git diff e3ef171
-- SKILL.md` empty). Commands carry their patterns.

### S1 — retired identifiers still cited (SKILL.md:86, :88, :90, :98) — open

```sh
grep -c "TL-01" tools/d2-typed-labels.py               # 0
grep -c "TL-02" tools/d2-typed-labels.py               # 0
grep -c "FIELD_DEFAULTS" tools/d2-typed-labels.py      # 0
grep -c "fictional-coordinate" tools/d2-typed-labels.py   # 0
grep -c "descriptive-gloss" tools/d2-typed-labels.py   # 0
grep -n "KINDS = " tools/d2-typed-labels.py            # :414 — three kinds
```

Semantics live under `D2L-*` (`D2L-FORM-UNRESOLVED` ×10 on the live packet).
Round 10 dispositioned the tool side (`reports/round-10/fix-02.md` §3 residual:
"`SKILL.md:86,88,90` and `SCORECARD.md:128` still cite the retired `TL-01`/
`TL-02` ids"); round-10's shard-05 also counted :98 (`reports/round-10/drift/
shard-05.md` §2, "stale — id + kind names"). This review confirms all four
lines are still open at admission time. Severity: medium.

### S2 — seven corpus line pointers off by 2–3 (SKILL.md:92–:95, :97, :99, :100) — open

| SKILL.md | cited | actual at `e3ef171` | off-by |
|---|---|---|---|
| :92 | `language-contact.md:78-79` | principle at :80 | +2 |
| :93 | `loanword-material-dating.md:26,60` | :26 blank; clocks :27–:33; "sense–referent pairing" :63 | +3/+2 |
| :94 | `garment-lexicon-crosslinguistic.md:26` | "switched referent in transit" :28; "two coexisting names" :30 | +2 |
| :95 | `loanword-material-dating.md:57` | "Dictionary selection bias…" :59 | +2 |
| :97 | `era-language-staging.md:124` | "Apply sound laws… separately track…" :127 | +3 |
| :99 | `naming-collision-gate.md:69-70` | "…not native-script identity" :72 | +2/+3 |
| :100 | `naming-collision-gate.md:52` | "…not mean identical cut or status" :54 | +2 |

Residue of round-10 shard-05's count; the only in-range fix since is :96's
`:40 → :43` (verified still correct). Severity: low, doc-hygiene.

### S3 — T3 citation boundary (SKILL.md:58, `loanword-material-dating.md:43-57`) — open

The discriminators' source table runs :54–:59; the range excludes its last two
rows. Low severity; extend to :59.

## 4. Findings — behavior vs the table's promises

### F1 — a declared sound kind with no bytes is silently clean, projector and wired flow (contradicts SKILL.md:44, :88, T2's third clause)

Pre-wiring (projector), 22:05Z:

```sh
export TMPDIR=$PWD/.scratch
python3 tools/d2-typed-labels.py --packet .scratch/rev23/probe-nobytes2.yml
#   label_findings_fail=0, label_findings_hold=0 — no D2L-FORM-UNRESOLVED for the record
python3 tools/d2-typed-labels.py --packet .scratch/rev23/probe-absent.yml
#   same: label_findings_hold=0
```

Post-wiring (wired flow), 22:14Z — the live packet plus one injected R5-class
record (`kind: native-form`, `status: to-verify`, no bytes, field issues):

```sh
python3 tools/typed-gate-flow.py --packet .scratch/rev23/packet-r5.yml --json
#   PROBE-R5 findings: []   (16 findings total, 15 holds — all from the live example set)
#   failed checks: typed-packet-pinned, expected-pins, expected-file-current
#   (the packet was modified, so those pins are expected to fail; the finding set is the readout)
```

The flow's finding set is the projector's set verbatim (`tools/typed-gate-flow.py`
:288-292: `result = typed_ns["run_pipeline"](...)`; `findings = result["findings"]`),
and `build_typed_packet` (:143-187) routes costume records only — no code path
emits or injects an R5-class hold. Design `§8.3` records the class as a carried
defect and orders the adapter to inject the hold; the delivered adapter does not.
Latent for `examples/culture-d2` (no such record among the 58 labels), false for
the table's general promise. Severity: high; the fix is the R5 branch (projector
or adapter, recorded as design says).

### F2 — a record with no declared kind crashes instead of refusing (contradicts SKILL.md:90)

```sh
python3 tools/d2-typed-labels.py --packet .scratch/rev23/probe-kindless.yml
#   exit 1, traceback: KeyError: 'kind' at tools/d2-typed-labels.py:2497
#     kind: sum(1 for label in parse_result["labels"] if label["kind"] == kind)
python3 tools/typed-gate-flow.py --packet .scratch/rev23/probe-kindless.yml --json
#   exit 1, the same KeyError traceback propagates through the wired entry point
```

The wired CLI's own contract (`tools/typed-gate-flow.py` docstring: "2 =
could-not-evaluate (missing or malformed input, no traceback)") is violated, as
is the projector's (:40-42). The class word is also wrong: per
`design-spec.md` §1.2 L1 (:127-129) and §6, a missing/ill-typed field is a
malformed-input refusal (`D2L-DATA`, exit 2), not the "hold" SKILL.md:90 names
(refinement corroborated by R11-D06's F-D06-2). Severity: high; fixes: a
`label.get("kind")` guard plus a class-correct refusal (or the table row
re-worded to the spec's class).

### F3 — the borrow-ledger check "domain/register declared" is not enforced (SKILL.md:45)

```sh
python3 tools/d2-typed-labels.py --packet .scratch/rev23/probe-b5-phon.yml
#   label_findings_fail=0, label_findings_hold=0 — no D2L-BORROW
```

The probe's borrow block has a resolving layer, separated donor, donor_form +
substitutions deriving `kas` from `gas`, ordered clocks, and a channel — but no
register and no domain. `check_borrow` (:692–:731) implements B1, B2, B3, B4
and the layer-contradiction check; B5 (`design-spec.md` §1.4 B5) has no path.
The wiring is silent on the class (the projector is untouched). Severity:
medium — one of five named checks missing.

### F4 — "never on the sound or identity channel": sound verified, key-equivalence not (SKILL.md:42)

The wired routing marks each translated-label costume `compare_only: true`
(`tools/typed-gate-flow.py:165-170`). The naming gate's `compare_only`
semantics, read at the live gate (sha `d9e4e8f4…`), skip only:

- Layer 5 spoken form (:1045), Layer 6 NAME-NEAR (:1090), NAME-LEXEME (:1121),
  Gate B sounds (:1154) — i.e. the sound and similarity channels;

while the key-equivalence layers 1–4 (:936, :983, :1011) still build keys from
the gloss string — the gate docstring itself calls `compare_only`
"key-equivalence checks only" (:93). Measured: the typed run's naming gate
emits 7 lines (6 NAME-NEAR on era entities + 1 CROSS-HOLD), none naming a GAR
record, so the divergence is latent on this data; the flow's sound-channel
cleanliness check only rejects `PHON-*` lines naming off records
(`PHON_ARTIFACT = "PHON-"`), and the differential tolerates retained lines. So
the table's "**never** — not on the sound or identity channel" holds for the
sound channel (verified) and is imprecise for the identity/key-equivalence
channel (mechanism). Severity: low; either the table should say "sound and
similarity channels", or the routing should also exempt the key layers — a
decision for the orchestrator/next round, reported here.

### F-notes (observations, not findings)

- **Duplicated emission in the R4 path.** Probe R4 emits the same `D2L-NATIVE`
  FAIL twice for one form (`label_findings_fail=2`): the R4 loop's explicit
  call plus the final `check_sound_form` pass. Latent on the live packet; the
  hold-set equalities are unaffected (16 findings observed == expected).
- **T1's tokenization clause and T3's discriminator count are not executable**
  (`grep -c "tokeniz" tools/d2-typed-labels.py` = 0; `grep -c "discriminator"`
  = 0; no counterpart in `typed-gate-flow.py`). The source draft says T3/T5 are
  house policy, not tool-enforced; the SKILL.md condensation keeps "T1–T4
  hard" without repeating that limit. A reader may over-read "hard" as
  "machine-checked".

## 5. Verified claims (positive receipts)

- **V0** `python3 tools/d2-typed-labels.py --selftest` → exit 0,
  "selftest: 39/39 checks passed" (22:00:41Z; re-run 22:06Z and 22:14Z).
- **V1** live packet projector: 10 `D2L-FORM-UNRESOLVED` holds, one per
  GAR-01…10, each naming its `LEX-GAR-0x` slot; stats `{labels: 58, hold: 15,
  note: 1, fail: 0}`. Frozen round-4: `grep -c "PHON-INVENTORY"
  tools/gates/frozen/round-4/naming-collision-gate.out` = 10 and `… | grep -c
  "GAR-"` = 10 (SKILL.md:42's "10/10" verified).
- **V2** probe R4 (`probe-r4-phon.yml`): violating native form `xaka` +
  translated-label claim over it → `D2L-NATIVE` FAIL on the native bytes; no
  waiver.
- **V3** borrow checks B1–B4 (selftest families "spec B3", "spec B3 positive";
  `check_borrow` :692–:731). Probe B5 isolates the missing check (§4 F3).
- **V4** `compare_only` misuse at the typed-label layer: probe
  `probe-compare.yml` → `FINDING D2L-SCOPE: [fail] GAR-T — compare_only is not
  a licensed exemption for typed labels` **and** `D2L-FORM-UNRESOLVED` hold
  stands (both emitted).
- **V5** legacy surface: `python3
  tools/gates/naming-collision-gate.py examples/culture-d2/packet.d2.yml` →
  exit 1, 10 × `PHON-INVENTORY: FAIL` on the ten GAR labels (22:07Z; also
  `reports/round-11/depth/capability-draft.md` §2.1).
- **V6** pins: as in the header; `git rev-parse HEAD` = `e3ef171…`,
  `git diff e3ef171 -- SKILL.md` empty (22:16Z).
- **V7 (wired)** `python3 tools/typed-gate-flow.py` → **exit 0, 10/10 checks
  passed**: `typed-packet-pinned`, `no-untyped-records`, `sound-channel-clean`,
  `differential-exact` ("10 PHON artifact(s) retired, 0 added, retained lines
  identical"), `owed-slots-crosscheck`, `hold-set-equal`, `expected-pins`,
  `expected-delta-match`, `expected-verdicts-match`, `expected-file-current`.
  Findings: **16 (hold 15, note 1, fail 0)** = 10 `D2L-FORM-UNRESOLVED`
  (GAR-01..10) + 2 `D2L-NATIVE` (L-15, L-16) + 3 `D2L-RANK` holds + 1
  `D2L-RANK` note — the set named independently in `design.md` §4.2-4.3 on
  22:06Z and re-derived by R11-D06 and R11-D21.
- **V8 (wired)** frozen replay: `python3 tools/replay-frozen.py
  tools/gates/frozen/round-11/MANIFEST.tsv --repo-root .scratch/rev23/iso` →
  **exit 0, "REPLAY OK: 10/10 rows reproduced the recorded verdicts"**
  (22:13Z). Invocation note: the mirror must sit outside the repo root, and
  `/tmp` is inode-exhausted, so the runnable form is an isolated tree under
  `.scratch` passed as `--repo-root` with `TMPDIR=$PWD/.scratch` — the plain
  in-repo invocation exits 2 with `mirror_unsafe` on every row (an invocation
  constraint, not an artifact defect).
- **V9 (wired)** projection re-pin: `python3 tools/d2-typed-labels.py --check`
  → exit 0; `typed-labels.d2.yml` sha `a3aa452c…` = `design.md` §5.1's
  predicted post-re-pin bytes.
- **V10 (wired)** selftest battery: `typed-gate-flow.py --selftest` exit 0
  (14/14); `--check` exit 0 ("byte-identical deterministic derivation");
  `assemble-d2.py --selftest` exit 0; `d2-typed-labels.py --selftest` exit 0;
  `assemble-culture-d3.py --selftest` exit 0; `check-gate-battery.py --selftest`
  exit 0; `check-gate-battery.py` exit 2 with `{pass: 7, fail: 0,
  unevaluable: 0}` (standing coverage verdict, unchanged).

## 6. Post-wiring verification log

**6.1 What landed and where.** The delivered wiring is `tools/typed-gate-flow.py`
(R11-D05, sha `ae55e6fa…`, mtime 19:13:37 local) plus the derived artifacts
`examples/culture-d2/packet.d2.typed.yml`, `examples/culture-d2/typed-gate.expected.json`,
and the frozen generation `tools/gates/frozen/round-11/`. This differs from the
design's planned names (`tools/assemble-d2-typed.py` + `tools/gates/typed-pipeline-gate.py`
+ `examples/culture-d2/expected-holds.json`, design §2.2/§3.1) and from its
planned mechanism (design §2.2 said the checked field would be renamed off
channel; the delivery marks the derived records `compare_only` instead). Those
divergences are the wiring-vs-design reviewer's desk (R11-D20), not this
review's; they are named here because they move what "the wired behavior" is.
Observed mid-flight and resolved: between 22:11:56Z and 22:13:37Z the tool's
expected-file default moved `.yml`→`.json` while the `.yml` artifact was
committed, so one e2e run exited 1 (`expected-present`) and one selftest run
raised its launder-control assertion; both were re-measured green after the
shard's next write (§5 V7/V10). The tool then moved a second time
(`ae55e6fa…` → `a7e1224f…`, mtime 19:17:01 local = 22:17Z) and the expected
set was re-emitted (`e962849a…` → `7ed59731…`); all measured legs were re-run
green at the later revision before this file was finalized (e2e 10/10,
`--check` exit 0, `--selftest` exit 0, replay 10/10, 16 findings / 15 holds).
No transient is counted as a finding.

**6.2 Process.** Polled every 60 s from 22:00Z (the round rule); the wiring
landed ~22:12Z and was **still being edited at the end of this review's window**
(three revisions in seven minutes: `ae55e6fa…` → `a7e1224f…` → `5758e315…`,
last observed 22:19Z local 19:18:09). All four core legs were re-run green at
each observed revision, and the finding set was identical (16 findings, 15
holds, 1 note); the final observed revision was green on all of them. Because
the file was moving, the pins above are as-read stamps, not the admission
revision — the integrator must re-run V7–V10 at the frozen revision. All
scratch under `TMPDIR=$PWD/.scratch`; the one command needing a temp root
outside the repo root used the `--repo-root` isolated-tree form (§5 V8). No
file outside the lane was written; `reports/round-{8,9,10}` bytes were not
touched by this seat.

**6.3 Corrections to the pre-wiring phase.** (a) SKILL.md byte-unchanged:
every §3 finding is open at admission time. (b) F1 and F2 persist at the wired
surface (measured, §4). (c) The wired flow closes the pre-wiring "gates do not
consume typed labels" limit: the typed run now consumes the typed packet and
the ten artifacts are retired; the ten holds are carried by name and
cross-checked against the component's own `form_slot` declarations. (d) The
stale projection pin (round-10 A2) is closed (§5 V9).

**6.4 Discrepancy note for the parent (adjacent, not this seat's finding file).**
`git status --porcelain` at 22:18Z shows six **earlier-round filed artifacts**
modified in the worktree: `reports/round-{5,6,7,8,9}/validation.json` (five
files) and `reports/round-10/coverage/index-update-22.md` — plus one legitimate
round-11 write, `examples/culture-d2/typed-labels.d2.yml` (the D07 re-pin,
§5 V9). Round 10 already recorded this defect class once ("a stale-fixer
rewrote filed receipt bytes"); the five `validation.json` writes look like
by-products of re-running those rounds' `run-validation.py` scripts during the
round-11 F recheck. Reported, not absorbed; whether they are reverted or
documented is the integrator's call before admission.

## 7. Limits

- Behavior findings are pinned to the hashes in the header at 22:12–22:17Z;
  sibling seats were editing concurrently, so any later revision invalidates
  the pins and must be re-measured.
- This review does not audit the wiring's design conformance (R11-D20), the
  hold-set's independent completeness (R11-D21), or re-pin circularity
  (R11-D22). In particular, the wired flow's `hold-set-equal` compares against
  `typed-gate.expected.json`, which the same tool emitted — this review's
  independent check is that the set matches `design.md` §4.2, authored before
  the implementation, and R11-D06's separate re-derivation.
- The staleness findings S1–S3 are documentation defects. `SKILL.md` is the
  orchestrator's to edit; this seat reports and does not rewrite it.
- No domain, canon, attribution or rights claim is made or implied
  (`PROVINCE.md`; `AGENTS.md`). D2 is a declared non-canon design drill; the
  label-typing table is representation discipline, not real-language
  clearance (`skill-table-draft.md` §7).
