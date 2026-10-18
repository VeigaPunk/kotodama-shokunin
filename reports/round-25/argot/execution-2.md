# R25-D12 — argot-derivation leg, execution 2: controls (tamper, false-red, exit codes)

- **Seat:** R25-D12 (argot execution 2 of 4), round 25, loop 3 build 1 of 4,
  claim **D** `argot-derivation-check` (`reports/round-25/claims.json:20-27`).
- **Date:** 2026-10-18. HEAD `f74fc9403d4b02c8ee76439eb133e3dea9b65b14`.
- **Write scope:** this file only; scratch under `.scratch/r25-d11/` only.
- **Canon:** NON-CANON engineering evidence.

Execution 1 established the positive result (12/12 replay clean). A green leg
with no control is not evidence — this execution supplies the negatives. Every
control runs in isolated scratch mirrors, never against the delivered tree.

## 1. Tamper control A — a derived lexeme the rule does not yield

Mirror `.scratch/r25-d11/mirror/packet.d4-tamper-lex.yml`: `L-46`'s term
`mesar` → `mesor` (one byte changed in the delivered form only; the rule
`CX-02` and the stated base `mes` are untouched).

```
python3 .scratch/r25-d11/argot-replay.py .scratch/r25-d11/mirror/packet.d4-tamper-lex.yml
→ "violations": 1
VIOL L-46 | mesor | derived | CX-02 | mesar | replay disagrees
```

**Result:** the leg names the violation and names the replayed value (`mesar`)
against the delivered value (`mesor`). A form the stated inputs and rules do
not yield is caught, and the finding names the record id, the rule id, and the
disagreeing pair.

## 2. Tamper control B — a name the rule does not yield

Mirror `.scratch/r25-d11/mirror/packet.d4-tamper-name.yml`: `NM-05`'s name
`haitik` → `haitka` (the `formation` block — stem `hai+tik`, rule `CX-01`,
`expected: haitik` — is left as delivered).

```
python3 .scratch/r25-d11/argot-replay.py .scratch/r25-d11/mirror/packet.d4-tamper-name.yml
→ "violations": 1
VIOL NM-05 | haitka | name | CX-01 | haitik | replay='haitik' name='haitka' expected='haitik'
```

**Result:** the name leg fires, and the message separates the three values
(replayed / delivered / the record's own `expected`), so a reader can see
whether the record disagreed with itself or with its rule.

## 3. The false-red control — the typed-pipeline L2 rebuild

The O claim's hazard (a) is a false red on derived-packet input. This leg
measures that hazard on the argot surface specifically, with three runs of the
**unmodified** gate over three inputs:

| run | input | exit | `grep -c DERIV` | receipt |
|---|---|---|---|---|
| A | `examples/culture-d4/packet.d4.yml` (source) | 1 | **0** | `.scratch/r25-d11/g-src.out` |
| B | `examples/culture-d4/packet.d4.typed.yml` (typed, read directly) | 1 | **0** | `.scratch/r25-d11/g-typ.out` |
| C | `.scratch/r25-o1/rebuilt-legacy.yml` (the gate's L2 mirror) | 1 | **8** | `.scratch/r25-d11/g-reb.out` |

Runs A and B are clean; run C manufactures **8 `DERIV-REPLAY` FAIL rows**
naming `NM-01`…`NM-08`:

```
FINDING DERIV-REPLAY: FAIL — name NM-01 'tumhai': rule 'CX-01' does not apply to stem 'tum+hai'; …
```

**Mechanism, measured.** The gate's L2 leg reconstructs the legacy packet by
copying the typed document (`tools/gates/typed-pipeline-gate.py:585-600`,
"reconstruct the legacy packet by moving the off-channel fields back"). The
copy re-serializes the packet-authored regex, and the backslash doubles. The
stored pattern is the only thing that changes:

```
source packet   stored CX-01 pattern: '^(?P<a>.+)\\+(?P<b>.+)$'  → re.match(…, 'tum+hai') → True
typed packet    stored CX-01 pattern: '^(?P<a>.+)\\+(?P<b>.+)$'  → re.match(…, 'tum+hai') → True
L2 rebuilt copy stored CX-01 pattern: '^(?P<a>.+)\\\\+(?P<b>.+)$' → re.match(…, 'tum+hai') → False
```

**Pin (live-edit hazard).** This measurement is against the gate bytes
`sha256 04ad4bb479562c419b48d750a8f9303c4a5a717ca7f2fe3b3658cc1bb9578a48`
(read 2026-10-18T17:29Z), which is HEAD `f74fc94`'s version. **A concurrent
round-25 O-claim repair is modifying the same file while this seat works**: an
`owed_slot_of` guard has been added (`git diff`, `:196-209`), a new
`L2-legacy-source` leg appears, and the file's sha256 has moved more than once
during this execution (`04ad4bb4…` → `08458233…` → `6e3b66c6…`, 17:29–17:34Z).
The pin is therefore the **HEAD `f74fc94` bytes named above**, not a live sha.
The rebuilt-mirror artifact this file measures is frozen in scratch
(`.scratch/r25-o1/rebuilt-legacy.yml`) and still shows the doubled backslash, so
the mechanism above stands as a record of the pre-repair state; whether the O
repair fully closes it is the O claim's to measure, not this seat's. The
`naming-collision-gate.py` digest this file and execution 1 cite
(`d9e4e8f4…`) is unchanged as of 17:34Z.

The regex now demands a literal backslash before the `+`, which no stem
carries, so every compound-rule name fails. The 8 rows are an artifact of the
rebuild, not a defect in D4 — exactly the round-8/round-19 corruption class the
adapter's text-transform architecture exists to avoid
(`tools/assemble-d4-typed.py` docstring; `SKILL.md:189-217`, "Round-trip
corruption class"). **The L2 rebuild re-introduces the corruption the adapter
was built to prevent.**

This leg's finding for the D claim: the replay surface is clean under direct
reads of both the source and the typed packet; the red is confined to the
gate's own in-memory rebuild. It is named here, not inherited as a D4 defect.
(Repairing the rebuild is the O claim's scope, not this seat's; the record
above is the evidence that repair needs.)

## 4. Exit codes and the delivered-surface control

- All three runs exit **1**, which is "findings", never 2 — no run
  could-not-evaluate, so the leg is measuring, not failing to read.
- The delivered surface is unmodified by every control: the two tamper mirrors
  and all receipts live under `.scratch/`, and `git status --short` is empty
  after this execution.
- `tools/gates/naming-collision-gate.py --selftest` remains green
  (`selftest: OK — fixture findings 12 across 11 ids …`), so the replay leg's
  own fixture controls still pass after this seat's read-only use of the gate.

## 5. Limits

- The controls tamper a *delivered form* and a *delivered name*; they do not
  tamper the rule table itself. A packet whose `pattern`/`output` pair is
  unusable is the gate's `DERIV-HOLD` class, exercised by the gate's own
  selftest fixture, not re-run here.
- The false-red control names the mechanism by pattern inspection of the three
  stored values; it does not patch the rebuild, and claims no repair.
