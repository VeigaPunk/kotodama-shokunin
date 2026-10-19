- Seat: D12 | executor | claim D | date 2026-10-19 | baseline da68a6d

# Claim D — depth receipt draft

Status: **before-state measured, after-state owed** (the `declared-in-r7` revision does
not exist at this seat's observation time; `ls reports/round-34/handoff` → `No such file
or directory`, exit 2). Every number below was measured by this seat at baseline
`da68a6d`, at HEAD bytes, with the command shown; nothing is carried from a fragment.
Run environment for all commands: lane root, `export TMPDIR=$PWD/.scratch
PYTHONDONTWRITEBYTECODE=1`.

Digests of the evidence files read (command: `sha256sum`):
`examples/culture-d4/typed-labels.d4.yml` = `c23b0ab532cfb9d4bb403405c6996982a447098048e08facbbc9f341ea13f82e`;
`examples/culture-d4/expected-holds.json` = `e6ae9828d6c82aa6e14431a02840ad565f9f7c30a660afcbed1b1079166bfba3`;
`tools/exercise-handoff-e2e.py` = `a5e4a8c5dda9d63c177a3dce75a8716ba5d285371d0a37a2535f6c323e7619df`;
`reports/round-20/handoff/claims-map.md` = `4b1b9a35a18f0a4c937eec804d438852c672f13303b7dcd6ccde3a3d917caae8`.

## 1. BEFORE — the wire (pins and defaults)

| surface | value at HEAD | citation |
|---|---|---|
| renderer baseline default | `"reports/round-30/handoff/declared-in-r6/expected.json"` | `tools/exercise-handoff-e2e.py:1933` |
| renderer frozen dir default | `"reports/round-30/handoff/declared-in-r6"` | `tools/exercise-handoff-e2e.py:1934` |
| current pair on disk | `packet.md` `6ced88ad…`, `twin.json` `6633443d…`, `expected.json` `ea1e2927…` | `sha256sum reports/round-30/handoff/declared-in-r6/{packet.md,twin.json,expected.json}` |
| pair's own freeze record | `packet_sha256: 6ced88ad009f1cfc94f7fc9e5656555f7da6682ce8f7afc3eb16734272f0f0bb` | `reports/round-30/handoff/declared-in-r6/freeze.txt:2` |
| pair's frozen scan | `gate: exit 0, fields=16/16, glossary-entries=20, findings=0` | `reports/round-30/handoff/declared-in-r6/freeze.txt:4` |

The pair is self-consistent: `sha256sum reports/round-30/handoff/declared-in-r6/packet.md`
= `6ced88ad009f1cfc94f7fc9e5656555f7da6682ce8f7afc3eb16734272f0f0bb` equals
`freeze.txt:2`. The defect claim D names is therefore semantic, not structural: the
gate cannot see it (§2, command 1) and the freeze self-check passes on stale prose.

## 2. BEFORE — the three counting commands, with observed output

### Command 1 — `python3 tools/gates/handoff-packet-check.py reports/round-34/handoff/declared-in-r7/packet.md`

Observed stdout (2026-10-19, lane root):

```
FINDING HO-DATA: HOLD — input could not be evaluated: [Errno 2] No such file or directory: 'reports/round-34/handoff/declared-in-r7/packet.md'
```

exit **2**. The new revision does not exist yet, so this command is **owed** (see §6).
Substitute reading — the same gate over the *current* default pair, which is what the
new pair must at minimum match:

```
$ python3 tools/gates/handoff-packet-check.py reports/round-30/handoff/declared-in-r6/packet.md
INFO scan: fields=16/16 glossary-entries=20 findings=0
EXIT=0
```

**Finding (this seat): a green shape gate is compatible with arbitrary stale claim
prose.** The gate judges §4 envelope shape and glossary etymology licensing
(`tools/gates/handoff-packet-check.py:1-30`), never the numbers inside `claim_ledger`
rows. Claim D's semantic leg cannot be evidenced by this command alone; it needs the
live-vs-row audit in §4.

### Command 2 — `python3 tools/exercise-handoff-e2e.py --profile v3 --quiet`

Observed stdout (2026-10-19, wall ≈ 3.6 s):

```
handoff-v3: exit=0 fields=16/16 glossary=20/20 findings=0 links=105/105 claims=27 statuses=16/7/4 v2_subset=equal alias_leg=landed packet_sha256=6ced88ad009f1cfc94f7fc9e5656555f7da6682ce8f7afc3eb16734272f0f0bb
```

exit **0**. The rendered `packet_sha256` equals the filed r6 `packet.md` digest
(`freeze.txt:2`), i.e. the exercise currently validates the pair it also reproduces.

### Command 3 — `python3 reports/round-34/run-validation.py`

Observed stderr:

```
python3: can't open file '/home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-34/run-validation.py': [Errno 2] No such file or directory
```

exit **2**. Absent by construction this round (shared rule: "this round's own
`reports/round-34/run-validation.py` does not exist yet"). **Owed** to the
integrator's validation leg; no filed runner was executed anywhere in this seat's
work (F-C13-1 prevention honoured — the only `run-validation.py` invocation above
targeted a non-existent path).

## 3. The byte-identity proof: a re-render reproduces the stale prose

```
$ python3 tools/exercise-handoff-e2e.py --profile v3 --freeze .scratch/D12-freeze --quiet
froze .scratch/D12-freeze: packet sha256 6ced88ad009f1cfc94f7fc9e5656555f7da6682ce8f7afc3eb16734272f0f0bb
EXIT=0
$ cmp reports/round-30/handoff/declared-in-r6/packet.md .scratch/D12-freeze/packet.md && echo IDENTICAL
IDENTICAL
$ cmp reports/round-30/handoff/declared-in-r6/twin.json .scratch/D12-freeze/twin.json && echo IDENTICAL
IDENTICAL
$ diff -u reports/round-30/handoff/declared-in-r6/run.log .scratch/D12-freeze/run.log   # empty, exit 0
```

A fresh freeze from **live bytes at HEAD** is byte-identical to the filed r6 packet and
twin. Only `expected.json` differs, in exactly two fields:

| field | r6 | fresh freeze (2026-10-19) |
|---|---|---|
| `frozen_at` | `2026-10-18` | `2026-10-19` |
| `baseline_digest` | `714b41fc58595b96e56888cdd9ee7612a423ee9ef68fe24b10bafccec6a36256` | `c2dd169b1fdde5dd8689ea65898613643a1baa84fa391f8fd8cd806298f37518` |

(`baseline_digest` is the JSON digest of the baseline body excluding that one key —
`tools/exercise-handoff-e2e.py:3763-3768, 3790-3792` — so it moves with `frozen_at`;
it is not evidence that the read set changed.) The two files also differ in a
freeze-provenance line: r6 `freeze.txt:8` reads `re-frozen packet_sha256:
ec30b11f12accfa4c43e24a36e53fca858eddb07… -> 6ced88ad009f1cfc94f7fc9e5656555f7da6682c…`,
the fresh one reads `no tracked value changed since the previous freeze`.

**Consequence for claim D's `after_required`:** "regenerates the packet from the
current D2/D3/D4 artifacts, rewrites the claim-ledger/OQ prose to live numbers" is
**not achievable by re-running the renderer**. The prose is not derived from the D2/D3/D4
artifacts; it is carried from two sources outside them (§5), and byte-identity here is
the measuring instrument that proves it.

## 4. The stale-figure inventory, measured against live bytes

Live readings this seat took itself (no fragment inherited):
`examples/culture-d4/typed-labels.d4.yml:29-46` (`coverage` block: `conflicts: 0` at
`:30`, `findings_total: 12` at `:32`, `findings_hold_or_fail: 12` at `:31`,
`label_findings_fail: 0` at `:33`, `label_findings_hold: 12` at `:34`,
`labels_by_kind {borrowed-strata: 6, native-form: 64, translated-label: 12}` at
`:35-39`, `rank_quarantine_handles: 0` at `:40`, `rank_rules_unresolved_items: 0` at
`:44`, `reconciliation_records: 6` at `:45`, `typed_labels: 82` at `:46`), the `stats`
block at `:2865-2869` (`fail 0, hold 12, labels 82`), and
`examples/culture-d4/expected-holds.json:46-49` (`counts {hold: 12, note: 0, fail: 0}`,
12 hold rows, 0 note rows).

| # | surface | r6 says | live value | live citation |
|---|---|---|---|---|
| 1 | `D4-CL05` basis+prose — `typed_labels` | 74 | **82** | `typed-labels.d4.yml:46` |
| 2 | `D4-CL05` — `labels_by_kind.native-form` | 56 | **64** | `:37` |
| 3 | `D4-CL05` — `findings_total` | 16 | **12** | `:32` |
| 4 | `D4-CL05` — `findings_hold_or_fail` | 15 | **12** | `:31` |
| 5 | `D4-CL05` — `#stats labels` | 74 | **82** | `:2869` |
| 6 | `D4-CL06` — `expected-holds#counts` | hold 15, note 1 | **hold 12, note 0** | `expected-holds.json:47-48` |
| 7 | `D4-CL07` — `conflicts` | 4 | **0** | `typed-labels.d4.yml:30` |
| 8 | `D4-CL07`/`D4-CL09` — `rank_quarantine_handles` | 3 | **0** | `:40` |
| 9 | `D4-CL09` — `rank_rules_unresolved_items` | 13 | **0** | `:44` |
| 10 | `D4-CL09` — "D2's rank-rule adaptation rows … 13 `act_rules` at `cannot-evaluate`" | present | **`act_rules: []`** (the rows no longer exist) | `:303` (`"act_rules": []`) |
| — | `D4-CL07` — `reconciliation_records` 6, `era_material_reconciliation.findings` 0 | 6 / 0 | unchanged (correct) | `:45`, `:48-49` |
| — | `D4-CL05` — `translated-label 12`, `borrowed-strata 6`, `label_findings_fail 0` | 12 / 6 / 0 | unchanged (correct) | `:38`, `:36`, `:33` |

Row 10 matters beyond arithmetic: `D4-CL09`'s whole narrative (re-carried D2 rank
adaptation rows) describes records the live projection no longer emits, so the rewrite
is a **content** rewrite, not a digit substitution.

Stale surfaces, located by grep over the filed pair:
`reports/round-30/handoff/declared-in-r6/packet.md:148` (D4-CL05), `:149` (D4-CL06),
`:150` (D4-CL07), `:152` (D4-CL09), `:307` (OQ-V3-05); twin-side mirrors
`reports/round-30/handoff/declared-in-r6/twin.json:1087,1089` (statement/basis),
`:1105` (CL06 basis), `:1120` (CL07 statement), `:1157` (CL09 basis), `:2619`
(OQ-V3-05 question). `twin.json` is generated with the packet, so any prose fix must
be re-frozen rather than patched in the twin.

**The intra-file contradiction claim D asserts is real and located:** the manifest rows
at `packet.md:68` (`82 labels (64 native-form / 12 translated-label / 6 borrowed-strata),
12 findings, 0 unresolved rank items, 4 era-alias rows`) and `:69` (`12 holds / 0 note /
0 fail`) already agree with the live bytes, while the claim rows four sections later do
not. The packet contradicts itself about the same artifact within one document.

D2 rows are **not** stale (checked because they sit in the same table): the live D2
projection reads `typed_labels 58`, `labels_by_kind 46/10/2`, `findings_total 16`,
`findings_hold_or_fail 15` (`examples/culture-d2/typed-labels.d2.yml:29-46`), which is
exactly what `packet.md:129` (D2-CL01) states. The staleness is D4-local.

## 5. Root cause: two non-D2/D3/D4 sources carry the prose

1. **The twelve D4 rows are parsed verbatim from a filed round-20 file.**
   `tools/exercise-handoff-e2e.py:184` `CLAIMS_MAP = "reports/round-20/handoff/claims-map.md"`;
   `:2289-2319` `v3_parse_claims_map()` extracts each row's `statement` / `u.basis` /
   `links` and the packet carries them "verbatim" (`:2566`, `:2881`). The stale text
   lives there: `reports/round-20/handoff/claims-map.md:104` (D4-CL05 basis — `typed_labels 74`,
   `native-form 56`, `findings_total 16`, `findings_hold_or_fail 15`, `#stats … labels 74`),
   `:116` (D4-CL06 basis — `hold 15, note 1`), `:124` (D4-CL07 statement — `conflicts (4)`),
   `:158` (D4-CL09 basis — `rank_rules_unresolved_items 13`, `rank_quarantine_handles 3`,
   `conflicts 4`). **`reports/round-20/**` is filed-round bytes and cannot be edited**
   (round shared rule 2), so the r7 build needs a *new* claims source plus a renderer
   that reads it — the renderer is a shared file, so that change is a **draft**, applied
   by the integrator.
2. **`OQ-V3-05` is a hard-coded string literal in the renderer.**
   `tools/exercise-handoff-e2e.py:3524-3532`, the question text at `:3527`:
   `"D4's inherited and own holds stay open: twelve form holds + three rank holds + one "
   "note, thirteen unresolved rank items, three quarantine handles and four conflicts — "`.
   A literal cannot self-correct; it must be rewritten in the renderer (shared-file
   draft). The filed `packet.md:307` line is the rendered form of that literal.

Both sources were independently recorded before this seat at
`corpus/lessons/round-25.md:82-85` ("the stale prose has **two** sources, not one"),
which also notes the same defect survived a filed supersession because the default was
never moved — matching the before-state measured here at `:1933-1934`.

Two sibling D seats reached the same two-route conclusion independently while this
receipt was being written (`reports/round-34/depth/D02-render.md:140,142` route A/B;
`reports/round-34/depth/D04-oq-glossary.md:56-65`), so the root cause is corroborated by
three separate readings; this seat's addition is the byte-identity instrument in §3 and
the complete live-vs-row inventory in §4.

Precedent for the fix shape: `reports/round-25/v3-supersession/build-revision.py:1-25`
— a delta constructor that derives a new revision by a fixed list of line substitutions
and **refuses to run if a declared old line does not occur exactly once**, so the delta
cannot drift. A round-34 `declared-in-r7` build is the same shape, plus the extra
requirement that the corrected prose is *live-derived* rather than hand-typed.

## 6. AFTER — what must be observed (owed until the r7 revision lands)

None of the following can be observed at this seat's time; each is stated as a checkable
row for the integrator/verifiers (D07, D17, D18, R01–R03), not as a result.

| leg | command | pass condition | status |
|---|---|---|---|
| L1 gate | `python3 tools/gates/handoff-packet-check.py reports/round-34/handoff/declared-in-r7/packet.md` | exit 0; `fields=16/16 glossary-entries=20 findings=0` | owed (path absent, §2 cmd 1) |
| L2 e2e | `python3 tools/exercise-handoff-e2e.py --profile v3 --quiet` | exit 0; `packet_sha256` equals `sha256sum reports/round-34/handoff/declared-in-r7/packet.md` and `freeze.txt`'s `packet_sha256` | owed (default still r6, §1) |
| L3 validator | `python3 reports/round-34/run-validation.py` | exit 0 | owed (runner absent, §2 cmd 3) |
| L4 semantics | re-run §4's live readings and diff them against the new rows | zero stale figures: no `74`/`56`/`16`/`15`-hold/`note 1`/`conflicts (4)`/`quarantine handles (3)`/`13 unresolved` in `D4-CL05..CL09` and `OQ-V3-05`; `act_rules` narrative matches `act_rules: []` | owed |
| L5 re-pin | `grep -rn "declared-in-r6" tools/ reports/round-34/ examples/` | no live surface left pointing at r6 except as a recorded superseded row | owed (D10/K02 own the census) |
| L6 preservation | `git status --porcelain reports/round-{2,4,5,6,20,30}/` and `git diff --stat` over them | zero filed-byte changes | owed (D11) |

L2's `packet_sha256 == freeze.txt` condition is *currently satisfiable* — it holds today
for the old pair (§1) — so it is not by itself evidence that the prose was fixed; the
decisive leg is **L4**. A re-frozen pair whose prose still reads 74/56/16 will pass L1,
L2, L3 and L6 and fail only L4, which is exactly how the r6 pair came to be green and
stale.

Adjacent tamper evidence this seat did take (negative controls belong to D13, recorded
here because L2 depends on them): `python3 tools/exercise-handoff-e2e.py --selftest`
→ exit **0**, positive run plus **17 controls**, among them `tamper baseline: exit 2
E2E-BASELINE (integrity digest mismatch), never a pass`; `tamper read-set: exit 1
E2E-DIGEST naming the changed file`; `tamper scan expectation: exit 2 E2E-BASELINE (a
re-signed expectation is refused, not honoured)`; `preservation: the 21 read-set files
are byte-identical before and after a run`. So the freeze machinery will not accept an
edited-but-not-re-frozen baseline — the new pair must be produced by a real freeze.

## 7. Side observations (for the planners, not verdicts)

- Because a fresh render is byte-identical to r6 (§3), the **predicted** new packet will
  differ from r6 only in the rows the build rewrites; its `packet_sha256` is therefore
  unknown until the build lands — **to-verify**, no value asserted here.
- `typed-labels.d4.yml`'s `#stats` anchor cited by D4-CL05 still exists (`:2865`), so the
  corrected row may keep that anchor — only its `labels` value (74 → 82) is stale.
- The fresh freeze's `expected.json` will carry `frozen_at: 2026-10-19` and a new
  `baseline_digest`; a byte-diff against r6's `expected.json` that shows exactly those two
  fields is expected and is **not** a defect (§3 table).

## Owed

Dependency fragments named by this seat's mission/claim that were still absent when
this receipt was finalized (all under `reports/round-34/`; the directories were listed
at 2026-10-19 04:07–04:09):

- `depth/D05-packet-draft.md` — the assembled `declared-in-r7` packet bytes; L1/L2/L4
  cannot be observed without it.
- `depth/D07-gate-run.md` — the gate run over the draft (L1).
- The after-readings of §2 commands 1 and 3, plus §6 L2/L4/L5/L6, which can only be
  taken once the r7 revision and the renderer-default draft are applied by the
  integrator.
- Not owed by this seat, recorded because they were missing at observation time and
  have since landed (this receipt could not cross-check against them mid-run):
  `depth/D10-repin-drafts.md`, `depth/D11-preservation.md`,
  `scout/K01-packet-state.md`, `scout/K02-repin-census.md`,
  `plan/P01-d-plan.md`. Cross-checks against them are left to the D verifiers and the
  integrator.

## Citations

Files read (line citations are to HEAD at baseline `da68a6d`):

- `tools/exercise-handoff-e2e.py:184, 1933-1934, 2289-2319, 2566, 2881, 3524-3532, 3763-3768, 3790-3792`
- `reports/round-30/handoff/declared-in-r6/packet.md:68, 69, 148, 149, 150, 152, 307`
- `reports/round-30/handoff/declared-in-r6/twin.json:1087, 1089, 1105, 1120, 1157, 2619`
- `reports/round-30/handoff/declared-in-r6/freeze.txt:2, 4, 8`; `…/run.log`
- `examples/culture-d4/typed-labels.d4.yml:29-46, 48-49, 303, 2865-2869`
- `examples/culture-d4/expected-holds.json:46-49`
- `examples/culture-d2/typed-labels.d2.yml:29-46`
- `reports/round-20/handoff/claims-map.md:104, 116, 124, 158`
- `corpus/lessons/round-25.md:82-85`
- `reports/round-25/v3-supersession/build-revision.py:1-25`; `…/declared-in-r4/packet.md:151, 155, 310`
- `tools/gates/handoff-packet-check.py:1-30, 40-60`

Commands run (lane root, `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`):

- `python3 tools/gates/handoff-packet-check.py reports/round-34/handoff/declared-in-r7/packet.md` → `HO-DATA: HOLD`, exit 2
- `python3 tools/gates/handoff-packet-check.py reports/round-30/handoff/declared-in-r6/packet.md` → `INFO scan: fields=16/16 glossary-entries=20 findings=0`, exit 0
- `python3 tools/exercise-handoff-e2e.py --profile v3 --quiet` → `handoff-v3: exit=0 … packet_sha256=6ced88ad009f1cfc94f7fc9e5656555f7da6682ce8f7afc3eb16734272f0f0bb`, exit 0
- `python3 tools/exercise-handoff-e2e.py --profile v3 --freeze .scratch/D12-freeze --quiet` → `froze .scratch/D12-freeze: packet sha256 6ced88ad…`, exit 0
- `python3 tools/exercise-handoff-e2e.py --selftest` → exit 0, positive + 17 controls
- `python3 reports/round-34/run-validation.py` → file not found, exit 2
- `cmp`/`diff -u` over `reports/round-30/handoff/declared-in-r6/{packet.md,twin.json,run.log,expected.json}` vs `.scratch/D12-freeze/*`
- `sha256sum reports/round-30/handoff/declared-in-r6/{packet.md,twin.json,expected.json} examples/culture-d4/{typed-labels.d4.yml,expected-holds.json} tools/exercise-handoff-e2e.py reports/round-20/handoff/claims-map.md`
- `grep -n` / `sed -n` reads as cited above; `python3 -c` JSON reads of `expected-holds.json` and the two typed-label files
