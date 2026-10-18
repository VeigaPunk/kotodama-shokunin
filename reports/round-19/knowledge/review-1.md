# R19-D06 — adversarial review 1/2: citation resolvability of the D4 knowledge drafts

- round: 19 (operator: loop 2 of 3, build 3 of 4; `reports/round-19/claims.json`,
  claim **D** `depth`). Lane: `kotodama-shokunin`. Reviewer seat **D06**.
- date: 2026-10-18. Measurement set stamped **2026-10-18T11:37:10Z** (UTC,
  `date -u --iso-8601=seconds`). Baseline revision
  `e5718945a1ab0a0c3db955338d2cae77d68fd348`; declare `169c616`.
- objects reviewed (read-only, all five on disk at the stamp):
  `reports/round-19/knowledge/analyst-1.md`, `analyst-2.md`, `analyst-3.md`,
  `skill-draft-a.md`, `skill-draft-b.md`; plus `corpus/lessons/round-19.md`.
- canon: NON-CANON engineering review. Not a canon record, a clearance, or a
  rights statement.
- writes: **this file only**. No tool, gate, packet, projection, component,
  baseline, receipt or filed round-8..18 byte is edited. No commit, no push.
- scope of this seat: **citation resolvability** — does every cited path/line
  resolve, and does the text at the cited locus support the claim it is attached
  to? Rule correctness against the gate's measured behaviour is `review-2.md`
  (R19-D07); the two files share one measurement set and cross-cite.

## 0. Verdict

**Citations resolve far better than the lane's usual baseline — no fabricated
paths — but three classes of defect survive and one of them is load-bearing.**

- **Resolvable:** every file path cited by the five drafts exists; no
  out-of-range line reference was found in the set. Spot-checks of the
  load-bearing anchors all resolve to the text they are attached to (§3).
- **Defect A (BLOCKER): a green is attributed to the wrong input.** Three drafts
  describe the D4 path as green using a run over the *untyped* packet while the
  sentence names the *typed* pipeline. `review-2.md` §1 carries the full
  measurement; this file records it as a resolvability failure because the
  citation and the claim do not match.
- **Defect B: two leg names that do not exist.** `skill-draft-b.md` §2 names
  `L1-projection_freshness` and `L1-coverage`; the gate defines neither.
- **Defect C: "delivered run" controls that do not name the input**, so the same
  control row reads differently for `packet.d4.yml` and `packet.d4.typed.yml`.

## 1. The measurement set (one stamp, shared with review-2)

Run from the lane root with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`,
2026-10-18T11:37:10Z:

```sh
sha256sum tools/gates/typed-pipeline-gate.py tools/assemble-d4-typed.py \
  examples/culture-d4/{packet.d4.yml,packet.d4.typed.yml,expected-holds.json}
python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.typed.yml   # exit 1, 14/16
python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml         # exit 0, 19/19
python3 tools/assemble-d4-typed.py --selftest                                        # exit 1
```

| artifact | sha256 |
|---|---|
| `tools/gates/typed-pipeline-gate.py` | `04ad4bb479562c419b48d750a8f9303c4a5a717ca7f2fe3b3658cc1bb9578a48` |
| `tools/assemble-d4-typed.py` | `087846719041db0ba32c005a34a6075c452e122a1f7b7bc4527ae4e0bfc4d798` |
| `examples/culture-d4/packet.d4.yml` | `e7ecd2045ef0e5f9823ce0a067d21b8221b2ceb5e8f5799736981a1c88fa50d3` |
| `examples/culture-d4/packet.d4.typed.yml` | `f63ed5315f6889f8c411b4dda2e69d43b05ce4fc6152f941a2b36bb1d7a13ebe` |
| `examples/culture-d4/expected-holds.json` | `09490a2756d123ebbc2023be89fc01c95ec2f8cc7e6df42ecc5b8cd438058e98` |

Every claim below binds to these bytes only; a later edit is a re-read event
(round-15 lesson: a green at an earlier revision does not authorize later bytes).

## 2. Defect A — the green is attributed to the wrong input (BLOCKER)

Three drafts state the D4 pipeline is green while the run they measured is over a
different input than the sentence names:

| draft | quoted claim | input the citation measures | input the sentence names |
|---|---|---|---|
| `skill-draft-a.md` §0 | "The D4 typed pipeline is green end-to-end" | `packet.d4.yml` (untyped, 19/19) | "the D4 typed pipeline" |
| `skill-draft-a.md` §0 | "the gate's routing cross-check asserts that equality directly (`typed-pipeline-gate.py:736-753`)" | the leg, which **fails** on the typed packet | presented as a passing assertion |
| `analyst-2.md` §0 | "gate-verified (12 routing rows, 6 field moves, `L3-routing-consistency` green)" | `packet.d4.yml` (untyped) | "the delivered tree" / the typed shape |
| `analyst-2.md` §5 | "the gate's `L3-routing-consistency` and `L2-channel` legs green" | `packet.d4.yml` (untyped) | the delivered D4 packet's routing |
| `skill-draft-b.md` §0 | "the full chain runs green … `typed-pipeline-gate.py`, which exits **0** with `summary: 19/19 legs passed`" | `packet.d4.yml` (untyped) | "the full chain", whose last artifact is `packet.d4.typed.yml` |

**Measured counter-evidence** (2026-10-18T11:37:10Z, gate `04ad4bb4…`):

```
$ python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.typed.yml
FAIL L2-channel — naming-collision-gate.py: non-artifact removal: FINDING DERIV-REPLAY: FAIL — name NM-01 'tumhai' …
FAIL L3-routing-consistency — holds ['GAR-01'…'LEX-GAR-06'] vs routed ['GAR-01'…'LEX-GAR-06'];
     owed slots ['LEX-GAR-01'…'LEX-GAR-06'] vs routing ['LEX-GAR-01'…'LEX-GAR-06', 'null'×6]
summary: 14/16 legs passed
exit 1
```

The `corpus/lessons/round-19.md` seat (R19-D08..D10) is the **only** draft in the
set that measured this correctly: its item 8 and its finding `L19-D08-2` both
state "the *typed* packet … reads **14/16, exit 1** at the same revision". So the
round's own drafts are internally inconsistent, and the D-axis codification would
land a rule whose worked instance contradicts it.

**Why this is a resolvability failure, not only a rule error.** `skill-draft-a`
§4's measured-basis table cites the *untyped* command and the heading above the
section calls it "the D4 typed pipeline"; a reader following the citation lands on
19/19 and pastes the sentence. The citation does not resolve to the claim.

**Fix (with control).** In every draft, name the input path inside the claim, not
in a footnote; and where the equality is stated as an observed green, say which
input was observed. Control: re-run both commands in §1 and require the draft's
sentence to reproduce each exit code against its named path.

## 3. Defect B — two leg names that do not exist

`skill-draft-b.md` §2 (the paste-ready block) lists the executable authorities as:

> `tools/gates/typed-pipeline-gate.py` (`L1-profile`/`L1-assembler`/`L1-projection_freshness`/`L1-coverage`/`L1-build`, `L2-channel`, `L3-*`, `L4-pins`)

`L1-projection_freshness` and `L1-coverage` are not legs of this gate.

**Control** (2026-10-18):

```sh
grep -n 'check("L[0-9]' tools/gates/typed-pipeline-gate.py
grep -c "projection_freshness\|L1-coverage" tools/gates/typed-pipeline-gate.py   # → 0
```

The gate's actual leg set (same command, `04ad4bb4…`) is: `L1-profile`,
`L1-assembler`, `L1-expected-holds`, `L1-build`, `L1-schema`, `L1-routing`,
`L2-channel`, `L2-retention`, `L3-holds`, `L3-notes`, `L3-fails`, `L3-counts`,
`L3-baseline`, `L3-details`, `L3-baseline-set`, `L3-routing-consistency`,
`L4-pins`. (`L1-build` is reported as `L1-%s` when the adapter refuses, `:558`.)

Note the internal inconsistency: the *same* draft's §4 gives a correct leg list
(`:481-485` `L1-profile`, `:499` `L1-assembler`, `:696-734` `L3-*`, `:750`
`L3-routing-consistency`, `:763-791` `L4-pins` — all verified). Only the paste-ready
§2 block carries the two invented names, so the defect is in the text the parent
would land.

**Fix (with control).** Replace the two invented names with the real leg list from
the control above; drop `L1-projection_freshness`/`L1-coverage` or rename them to
the adapter's own fail-closed inputs (`assemble-d4-typed.py:127-148`
`projection_fresh`, `:242-249` coverage), which is where those concepts actually
live. Control: `grep -n "def projection_fresh\|coverage" tools/assemble-d4-typed.py`.

## 4. Defect C — "delivered run" controls that do not name the input

Two control rows give a "delivered run" reading that is true of one input and
false of the other:

| draft | control row | measured |
|---|---|---|
| `analyst-1.md` §3 R2 | "delivered D4 run: 12 rows, 6 field moves, 6 `PHON-` artifacts removed (`reports/round-18/d4/` verdict)" | `sound_channel.removed = 6` on `packet.d4.yml`; **14** on `packet.d4.typed.yml` |
| `analyst-2.md` §4 R8 | "delivered run: 12 rows, 6 moves, 6 removals" | same conflation |

**Control** (2026-10-18T11:37Z):

```sh
python3 tools/gates/typed-pipeline-gate.py --json examples/culture-d4/packet.d4.yml \
  | python3 -c 'import json,sys; print(json.load(sys.stdin)["sound_channel"])'
# {'added': 0, 'removed': 6, 'retained_on_channel': 0, 'routed': 12, 'translated_on_sound_channel': 0}
python3 tools/gates/typed-pipeline-gate.py --json examples/culture-d4/packet.d4.typed.yml \
  | python3 -c 'import json,sys; print(json.load(sys.stdin)["sound_channel"])'
# {'added': 0, 'removed': 14, 'retained_on_channel': 0, 'routed': 12, 'translated_on_sound_channel': 0}
```

**Fix (with control).** Write the input path into the control row ("on
`packet.d4.yml`") and, where the rule is stated for the typed shape, record both
readings. Control: the two `--json` commands above; a control row that reproduces
`removed: 6` must name `packet.d4.yml`.

## 5. Citations that resolve correctly (positive verification)

Spot-checked read-only at the stamp; each resolves to text supporting the claim:

| draft | citation | resolves to |
|---|---|---|
| analyst-1 §2, §3 | `typed-pipeline-gate.py:186-199` | `def moved_field(row):` + the null-ish docstring ("the lane's reader keeps an unquoted `null` as the string") |
| analyst-1 §3 | `typed-pipeline-gate.py:656-673`, `:677-682` | the D4 two-rows-one-move comment; the `L2-retention` leg |
| analyst-1 §3 | `typed-pipeline-gate.py:1130-1146` | the `d9` register fixture row (`off_channel_field: null`, `hold: "D9L-REGISTER-UNRESOLVED"`) |
| analyst-1 §2 | `d2-typed-labels.py:449`, `:498` | `_SLOT_RE = re.compile(r"LEX-GAR-[0-9]{2}")`; its use |
| analyst-1 §1 | `design-brief.md:254-281`, `:263-273`, `:373`, `:455-463` | Δ1; the class-2 rows; the `compare_only` rule; controls C-01..C-10 (C-06 at `:460`) |
| analyst-2 §1 | `assemble-d4-typed.py:65`, `:161`, `:170-175`, `:236-240`, `:242-249` | `ROUTED_KINDS`; `def build_typed_packet`; the two-carriers comment; the owed-slot comment; the coverage rule |
| analyst-2 §3 | `typed-pipeline-gate.py:736-753`, `:975` | the routing-consistency leg; the dropped-row selftest control (`owed_slot: "LEX-GAR-01"` deleted) |
| analyst-2 §2 | `packet.d4.typed.yml:2678-2800` | exactly 12 `typed_channel` rows, all `off_channel_field: "garment_gloss"` |
| analyst-3 §2 | `naming-collision-gate.py:1206-1220`, `:1223`, `:1370`, `:1403` | `_derivation_rules`; `MATCH_BUDGET_SECONDS = 0.5`; "derivation cannot be replayed"; "no `morphology.derivation_rules`; cannot replay the chain" |
| analyst-3 §1 | `packet.d4.yml:205-226`, `:1950`, `:1971` | `derivation_rules:` (CX-01..03); two `rule: "CX-01"` name records |
| analyst-3 §4 | `assemble-d4-typed.py:296-325`, `:367-370`, `:529-536`; `SCORECARD.md:176-177,185`; `LOG.md:3252-3253` | the text-transform docstring; the two-build guard; the `--check` branch; the serializer-corruption record |
| analyst-3 §4 | `assemble-d4-typed.py --check …` → exit 0 | reproduced: "byte-identical deterministic typed packet" |
| skill-draft-a §4 | `grep -c "REGISTER" tools/d2-typed-labels.py` → 0 | reproduced: 0 |
| skill-draft-a §4 | `grep -n "L3-routing-consistency" …` → `:750` | reproduced |

Three line ranges resolve but start one line early or point at the extraction
rather than the finding; all are non-blocking precision notes:

- `analyst-3.md` §2 cites `naming-collision-gate.py:1382-1386` for "a formation
  without a stem ⇒ 'the rule chain is not replayable'". The finding is at
  `:1387-1394` (the string is at `:1393`); `:1382-1386` is the
  stem/rule/affix extraction. Control:
  `sed -n '1386,1394p' tools/gates/naming-collision-gate.py`.
- `analyst-3.md` §3 cites `design-language.md:187-217`; §5 starts at `:186`.
  Control: `grep -n '^## 5' reports/round-17/d4/design-language.md` → `186`.
- `analyst-3.md` §2 cites `naming-collision-gate.py:1345-1410`; `def _gate_c` is at
  `:1346`. Control: `grep -n 'def _gate_c' tools/gates/naming-collision-gate.py`.

**Fix (with control).** Adjust the three ranges by their measured start line;
control: the three `grep`/`sed` commands above, re-run at landing time (the
`SKILL.md` and `corpus/` line numbers shift when the drafts are integrated —
`skill-draft-a` §5 item 3 and `skill-draft-b` §5 item 4 both say so).

## 6. What this seat does not decide

- Whether the `L3-routing-consistency` red on the typed packet is a gate defect or
  an adapter defect is `review-2.md`'s measurement and the owners' disposition —
  this file only records that the drafts call it green when it is red.
- No draft is rejected here: four of the five are paste-ready once Defects A–C are
  corrected, and `corpus/lessons/round-19.md` already carries the corrected
  reading.
- No canon, rights, clearance or freshness ruling is made or absorbed; the
  freshness axis-move pause stands and the two round-11 ratios remain separate.

## 7. Boundary record

Read-only throughout. Writes: this file only, plus gitignored scratch under
`.scratch/r19d0607/` (the citation resolver and the captured gate JSON);
`TMPDIR=$PWD/.scratch` preceded every scratch-writing command. No gate, adapter,
packet, projection, expectation, baseline or filed round-8..18 byte was edited.
No git commit or push. All counts carry their command and the shared
2026-10-18T11:37:10Z stamp; all quoted text names its locus.
