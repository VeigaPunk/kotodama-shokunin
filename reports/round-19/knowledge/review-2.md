# R19-D07 — adversarial review 2/2: rule correctness against the gate's actual behaviour

- round: 19 (operator: loop 2 of 3, build 3 of 4; `reports/round-19/claims.json`,
  claim **D** `depth`). Lane: `kotodama-shokunin`. Reviewer seat **D07**.
- date: 2026-10-18. Measurement set stamped **2026-10-18T11:37:10Z** (UTC,
  `date -u --iso-8601=seconds`); adapter selftest re-read 2026-10-18T11:38Z.
  Baseline revision `e5718945a1ab0a0c3db955338d2cae77d68fd348`; declare `169c616`.
- objects reviewed (read-only): `reports/round-19/knowledge/analyst-1.md`,
  `analyst-2.md`, `analyst-3.md`, `skill-draft-a.md`, `skill-draft-b.md`;
  `corpus/lessons/round-19.md`. Shared measurement set and citation audit:
  `review-1.md` (R19-D06).
- canon: NON-CANON engineering review. Not a canon record, a clearance, or a
  rights statement.
- writes: **this file only**. No tool, gate, adapter, packet, projection,
  component, baseline, receipt or filed round-8..18 byte is edited. No commit, no
  push.
- scope of this seat: **rule correctness** — does each codified rule describe what
  the gate and adapter actually do on the delivered bytes, and does its control
  hold? Citation resolvability is `review-1.md`; this file carries the root-cause
  measurements it cross-cites.

## 0. Verdict

**Most codified rules are correct and their citations resolve; four defects would
land a rule the delivered bytes contradict, and two of them are the round's own
subject matter.**

1. **BLOCKER — the routing equality is codified as observed-green; the gate's own
   leg is red on the delivered typed packet.** `analyst-2` R7/R9 and
   `skill-draft-a` Rule 1 state "the routing row set equals the `FORM-UNRESOLVED`
   hold set" as an equality the gate asserts and passes. On
   `examples/culture-d4/packet.d4.typed.yml` the gate's `L3-routing-consistency`
   leg **fails** (§1.2). The rule is a good rule; the green is the wrong input.
2. **BLOCKER — a control cited for a rule is red.** `analyst-3` R17 and §4 cite
   `tools/assemble-d4-typed.py --selftest` controls as holding; the selftest exits
   **1**, 4/11 checks, and R17's cited leg (`:467-477`) is one of the failures
   (§3). (`analyst-2` R10 and `analyst-1` R1 cite controls that do pass.)
3. **The round-trip corruption class has a delivered instance the drafts miss.**
   `analyst-3` R16 documents the class from the adapter docstring; the gate's own
   L2 legacy-rebuild path is a *live* instance of it, and it is the reason the
   typed-packet run fails `L2-channel` (§2). This strengthens R16 and should be
   cited.
4. **Two controls name a reading without naming the input** (`analyst-1` R2,
   `analyst-2` R8); `review-1.md` §4 carries the commands.

`corpus/lessons/round-19.md` (R19-D08..D10) is the only draft whose rules survive
this review unchanged on the typed-packet question: it measured 14/16 and reported
it as a finding rather than a green.

## 1. The routing equality: codified green, measured red

### 1.1 What the drafts codify

- `analyst-2.md` §0: "the model is delivered and gate-verified (12 routing rows,
  6 field moves, `L3-routing-consistency` green)"; §3.2 describes the leg; §5:
  "the gate's `L3-routing-consistency` and `L2-channel` legs green".
- `skill-draft-a.md` Rule 1: "the set of records named by a `typed_channel` row
  equals the set of records named by the `FORM-UNRESOLVED` holds … an equality the
  gate asserts, not an intention"; §0 item 3 cites `typed-pipeline-gate.py:736-753`
  as asserting it.
- `corpus/lessons/round-19.md` item 2 states the same rule but does not call it
  green on the typed packet.

### 1.2 What the gate does on the delivered typed packet

Measured 2026-10-18T11:37:10Z, gate `04ad4bb4…`, typed packet `f63ed531…`:

```
$ python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.typed.yml
ok   L1-profile
ok   L1-assembler
ok   L1-expected-holds
ok   L1-build
ok   L1-schema
ok   L1-routing
FAIL L2-channel — naming-collision-gate.py: non-artifact removal: FINDING DERIV-REPLAY: FAIL — name NM-01 'tumhai' …
ok   L3-holds … L3-baseline-set
FAIL L3-routing-consistency — holds ['GAR-01'…'LEX-GAR-06'] vs routed ['GAR-01'…'LEX-GAR-06'];
     owed slots ['LEX-GAR-01'…'LEX-GAR-06'] vs routing ['LEX-GAR-01'…'LEX-GAR-06', 'null'×6]
ok   L4-pins
summary: 14/16 legs passed
exit 1
```

The same gate over `examples/culture-d4/packet.d4.yml` reads exit **0**,
`19/19 legs passed`. So `analyst-2`'s and `skill-draft-a`'s greens are true of the
*untyped* input and false of the typed one (`review-1.md` §2).

### 1.3 Root cause — measured, not inferred

`L3-routing-consistency` (`tools/gates/typed-pipeline-gate.py:750`) is

```
check("L3-routing-consistency",
      hold_records == moved_records and hold_slots == routed_slots, …)
```

with `routed_slots` built at `:748-749` as

```
routed_slots = sorted(row.get("owed_slot") for row in routing
                      if moved_field(row) and row.get("owed_slot"))
```

Two facts collide:

1. The committed typed packet writes `owed_slot: null` on the six `GAR-0n` rows
   (`packet.d4.typed.yml:2688`, and five siblings; measured: 12 `typed_channel`
   rows, `owed_slot` `null`×6 + `LEX-GAR-01..06`).
2. The lane's reader keeps an unquoted `null` as the **string** `"null"` — stated
   in the gate's own `moved_field` docstring (`:188-190`) and confirmed by
   `--json`: the parsed routing row for `GAR-01` carries
   `owed_slot = 'null'` (a truthy string), not `None`.

So `routed_slots` collects 6 slot ids **plus** 6 `"null"` strings = 12, while
`hold_slots` collects the 6 ids the findings name = 6 → the leg fails.

**Why the untyped run passes:** with `typed_arg is None`, `routing` is read from
the adapter's in-memory build (`built["doc"]`, `:563`), where `owed_slot` is the
Python object `None` (`assemble-d4-typed.py:236-240` returns `None`, not the
string), which is falsy and is excluded. The two runs differ only in whether the
null survived a serialization round trip — which is precisely the class the D
claim asks the round to codify.

`moved_field` (`:186-199`) already applies the null-ish test
(`value.strip().lower() in ("", "null", "none", "~")`); the `routed_slots`
comprehension does not. The asymmetry is the defect; whether the fix belongs in
the gate (apply the null-ish test to `owed_slot`) or the adapter (omit the key on
garment rows) is the owners' disposition, not this seat's.

### 1.4 The fix for the drafts, with control

Keep the rule (it is correct and valuable); attach it to the input it was
measured on, and record the typed-packet reading as an open finding:

- `analyst-2` §0/§5 and `skill-draft-a` Rule 1: replace "green" with the measured
  reading per input — "`packet.d4.yml`: 19/19, `L3-routing-consistency` green;
  `packet.d4.typed.yml`: 14/16, `L3-routing-consistency` red (null round-trip)" —
  or mark the typed-packet equality `(to-verify)` per `AGENTS.md` ("claims you
  cannot verify are marked `to-verify`").
- Control: re-run both commands in §1.2 and require the draft's sentence to match
  each exit code against its named path; then
  `python3 tools/gates/typed-pipeline-gate.py --json examples/culture-d4/packet.d4.typed.yml | python3 -c 'import json,sys; r=json.load(sys.stdin)["routing"]; print([x["owed_slot"] for x in r[:6]])'`
  must print six `"null"` strings for the finding to still stand.

## 2. The round-trip corruption class has a delivered instance (strengthens R16)

`analyst-3` R16 states the class from the adapter docstring
(`tools/assemble-d4-typed.py:296-301`) and `SCORECARD.md:185`, and its §8 limit
says the seat "did not re-run a round-trip serializer to reproduce the
corruption". The delivered bytes contain a reproduction, and it is the cause of
the second `FAIL` on the typed packet.

**Measured mechanism.** The gate's L2 leg reconstructs the legacy packet by
re-serializing the typed document:

```
typed-pipeline-gate.py:590   rebuilt = copy.deepcopy(typed_doc)
typed-pipeline-gate.py:605   legacy_bytes = ("\n".join(load_peer(SERIALIZER)["yaml_lines"](rebuilt)) + "\n").encode("utf-8")
```

with `SERIALIZER = ROOT / "tools/assemble-d2.py"` (`:78`) — **D2's** serializer,
used unchanged on a D4-family run. The D4 packet's `morphology.derivation_rules`
CX-01 carries a regex backslash (`examples/culture-d4/packet.d4.yml:209`), the
byte class the serializer mangles. Consequence, measured: the legacy run's
naming gate emits 8 `DERIV-REPLAY` FAILs (`NM-01 'tumhai' … rule 'CX-01' does not
apply to stem 'tum+hai'`) that the typed run lacks, so the delta reports them as
"non-artifact removal" and `L2-channel` fails.

**Control** (2026-10-18):

```sh
grep -n 'load_peer(SERIALIZER)\|^SERIALIZER' tools/gates/typed-pipeline-gate.py
sed -n '209p' examples/culture-d4/packet.d4.yml        # pattern: "^(?P<a>.+)\+(?P<b>.+)$"
python3 tools/gates/naming-collision-gate.py examples/culture-d4/packet.d4.yml | grep -c DERIV-REPLAY   # 0
```

and the typed-packet run in §1.2, whose `L2-channel` detail names the 8 rows. On
the untyped run the same leg is green because `legacy_bytes = Path(packet_path).read_bytes()`
(`:608`) — raw bytes, no re-serialization.

**Fix for the drafts, with control.** `analyst-3` R16 and
`corpus/lessons/round-19.md` item 3 should add this as a *delivered* instance
(gate-side re-serialization, not only the adapter docstring), which also makes the
rule sharper: the class bites any code path that re-serializes a packet carrying
regexes, not only the typed-packet builder. Control: the three commands above; the
`grep -c DERIV-REPLAY` must read `0` on the raw packet and the typed run must show
8 such lines in its `L2-channel` detail.

## 3. The adapter selftest is red; a cited control does not hold (BLOCKER)

Measured 2026-10-18T11:38Z, adapter `08784671…` (committed at `e571894`, worktree
clean):

```
$ python3 tools/assemble-d4-typed.py --selftest
selftest: 4/11 checks passed — failures: positive: --emit exit 0; determinism: two builds byte-identical;
  --check: exit 0 on the build; tamper: --check exit 1 on a changed byte; tamper: restored build passes;
  stale projection: exit 2 and the pin is named; routing: the checked field is moved, not flagged
FAIL positive: --emit exit 0 — exit 2: FAIL assembler_identity: assembler refused the components:
     required file not found: tools/assemble-d2.py
FAIL routing: the checked field is moved, not flagged — [{… 'owed_slot': None}]
exit 1
```

Two controls cite the adapter selftest, and one of them is red:

- `analyst-3.md` R17 control: "adapter selftest `:467-477` (moved field present,
  original gone)". That is the `routing: the checked field is moved, not flagged`
  leg — the one that **fails**, on the same `owed_slot: None` value §1.3
  measures. R17's rule (rename by byte-level substitution) is sound and its other
  evidence (`--check` exit 0) holds; only the selftest control is red.
- `analyst-3.md` §4: "the adapter's `--selftest` carries build / determinism /
  `--check` / tamper plus stale-projection, coverage-gap and malformed-packet
  controls (`assemble-d4-typed.py:397-497`)". The controls *exist* at that range;
  they do **not pass**. The positive leg fails inside the selftest mirror
  ("required file not found: `tools/assemble-d2.py`") and takes determinism,
  `--check`, tamper and stale-projection down with it.
- **Not a defect:** `analyst-2.md` R10 control cites `:454-466`, the
  coverage-control block, which **passes** (`ok coverage: an untyped garment
  record is a problem`); R10 stands as written.
- **Not a defect:** `analyst-1.md` R1's control is the *gate's* selftest fixture
  (`typed-pipeline-gate.py:1130-1146`), a different tool: measured green
  (`typed-pipeline-gate.py --selftest` → 12/12; `--selftest-generalized` → 14/14,
  2026-10-18T11:39Z). Only the adapter's selftest is red.

`corpus/lessons/round-19.md` `L19-D08-1` reports both defects correctly and notes
round-18's `validation.json` never ran this selftest. Claim O's
`after_required` ("battery + craft + all typed/assembly selftests green") makes it
a round-19 obligation, so the drafts must not cite it as a standing green.

**Fix (with control).** In `analyst-3` R17 and §4, state the selftest reading
("4/11, exit 1, two defects") rather than citing it as a passing control, or cite
only the legs that pass (`coverage: …`, `malformed packet: exit 2, no traceback`).
Control: `python3 tools/assemble-d4-typed.py --selftest` → exit 1, and the
`ok`/`FAIL` lines above; the gate's own selftest stays green
(`python3 tools/gates/typed-pipeline-gate.py --selftest` → 12/12).

## 4. Rules verified correct against the gate's actual behaviour

These survive review; each control was run or read at the stamp.

| draft | rule | verified against |
|---|---|---|
| `analyst-1` R1 | a routing row has two independent axes; null-ish `off_channel_field` ⇒ stays on channel | `typed-pipeline-gate.py:186-199`; the `d9` fixture `:1130-1146` |
| `analyst-1` R3 | a retained on-channel row may not lose its inventory line | `L2-retention` leg `:677-682` (skipped on the typed run: `retained_records` empty) |
| `analyst-1` R4 | neither direction of the T1 law is waivable | design controls C-01/C-03/C-09, `design-brief.md:455-463` — **design-forecast**, correctly labelled forecast in §5 |
| `analyst-1` §5 | class-2 register rows are **not** delivered | 12 routing rows all `off_channel_field: "garment_gloss"`; `grep -c REGISTER tools/d2-typed-labels.py` → 0 — reproduced |
| `analyst-2` R6 | a form-bearing record is keyed by record id and slot-label id | `packet.d4.typed.yml:2678-2800`: 12 rows, `GAR-01..06` + `LEX-GAR-01..06` — reproduced |
| `analyst-2` R7 | the owed slot is named once, on the slot's own row | adapter `:236-240`; but see §1 — the *gate leg that checks it* is red on the typed packet |
| `analyst-2` R11 | slot cardinality / `doublet_of` pair | correctly marked forecast (`grep -c doublet packet.d4.yml` → 0) |
| `analyst-3` R12–R14 | pattern/output pair is the join key; unreplayable ⇒ HOLD; packet regex matched under a budget | `packet.d4.yml:205-226`, `:1950`/`:1971`; `naming-collision-gate.py:1206-1220`, `:1223`, `:1370`, `:1403` — reproduced |
| `analyst-3` R15 | a derivation must be spellable | correctly marked forecast (`design-language.md:186-217`) |
| `analyst-3` R16 | derive by text transform, never re-serialize foreign content | adapter `--check` exit 0 reproduced; **strengthened** by §2 |
| `analyst-3` R17 | rename by byte-level substitution, not parse-and-re-emit | adapter `:296-316`; `--check` exit 0 |

`analyst-1` §5's honesty ledger is the model the other drafts should follow: it
separates what the bytes carry (class 1) from what the design forecasts (class 2)
and marks the forecast `(to-verify)`. The same discipline applied to the routing
equality (§1) and the selftest (§3) would clear both blockers.

## 5. Landing conditions (what the parent must require before integrating)

1. Every green in `analyst-2` §0/§5, `skill-draft-a` §0 and `skill-draft-b` §0
   must name its input path; the typed-packet reading (14/16) must appear where
   the typed shape is the subject. Control: the two commands in §1.2.
2. `skill-draft-b` §2's leg list must drop `L1-projection_freshness` and
   `L1-coverage` (they do not exist; `review-1.md` §3). Control:
   `grep -c "projection_freshness\|L1-coverage" tools/gates/typed-pipeline-gate.py` → 0.
3. The adapter-selftest citations (`analyst-3` R17's `:467-477` control and §4)
   must state the measured 4/11 red. Control: `python3 tools/assemble-d4-typed.py
   --selftest` → exit 1; `python3 tools/gates/typed-pipeline-gate.py --selftest`
   → exit 0, 12/12 (the gate's own selftest is unaffected).
4. R16 and the lesson item 3 should carry the gate-side re-serialization instance
   (§2). Control: `grep -n "load_peer(SERIALIZER)" tools/gates/typed-pipeline-gate.py`.
5. The three off-by-one line ranges in `analyst-3` (`review-1.md` §5) must be
   corrected at landing, since `SKILL.md`/`corpus` line numbers shift on
   integration.

## 6. What this seat does not decide

- Whether the two typed-packet `FAIL`s are gate defects or adapter defects is the
  gate owner's and adapter owner's disposition; this file records the mechanism
  and routes it. It does not edit either tool (single-writer surfaces; round-18
  lesson 7).
- No draft is rejected: `analyst-1` and `corpus/lessons/round-19.md` are sound as
  written; `analyst-3` needs only its selftest control (§3) and three line ranges
  (`review-1.md` §5) corrected; `analyst-2` and the two skill drafts need the
  named-input qualifier; `skill-draft-b` §2 needs the leg list fixed.
- No canon, rights, clearance or freshness ruling is made or absorbed; the
  freshness axis-move pause stands and the two round-11 ratios remain separate
  and un-reopened.

## 7. Boundary record

Read-only throughout. Writes: this file only, plus gitignored scratch under
`.scratch/r19d0607/` (captured gate JSON, adapter-selftest output);
`TMPDIR=$PWD/.scratch` preceded every scratch-writing command. No gate, adapter,
packet, projection, expectation, baseline or filed round-8..18 byte was edited.
No git commit or push. Every count carries its command and the shared
2026-10-18T11:37:10Z stamp (adapter selftest 11:38Z); every quoted string names
its locus; every proposed fix carries a control command.
