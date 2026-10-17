# R9-D10 — adversarial review: independent re-derivation of the D3 assembly step

- **Assignment:** R9-D10, adversarial reviewer (round 9, claim D / depth). Independently
  re-derive one D3 assembly step by hand from `examples/culture-d3/components/` and compare
  against the committed packet; divergence = finding.
- **Step chosen:** the legacy-projection step of `tools/assemble-culture-d3.py` —
  component merge → native-form-only `name`/`garment`/`term` slots, the six per-name concat
  replay rules, the E1 lexicon terms, the era ordering and the
  `assembly.trace` of `examples/culture-d3/packet.gates.yml`, plus the packet core of
  `examples/culture-d3/packet.json`.
- **Reviewer run (UTC):** 2026-10-17T20:48Z–20:52Z. **Working tree:** HEAD
  `a7bb205d3aecdaa24d91c047c8719cd8689e4ddd` plus round-9 peer fragments; the D3 artifacts
  themselves are unmodified (`git status --short -- examples/culture-d3
  tools/assemble-culture-d3.py tools/check-evidence-coupling.py` → empty, run 2026-10-17).
- **Harness:** `/var/tmp/d3-r9/rederive_projection.py`,
  sha256 `182ad385ec2fd52e579f62c628a981af46ae70923f492f52b568b0f2b84ca13b`
  (`sha256sum`, 2026-10-17). Scratch lives outside the repo; this shard writes only its own
  file. Per the round's write rule the harness is **not** committed — it is reconstructible
  from §0 and §1 (inputs, joins, serializer, checks) and every one of its results is quoted
  inline below.
- **Verdict:** the projection is **reproducible from the components alone**: 62/63 independent
  checks pass, and the single failure is a 36-byte presentation-prose divergence between the
  two committed artifacts (Finding F1), not a data divergence. The frozen pin of the packet is
  red on this tree (Finding F2) — independently confirmed, already diagnosed by R9-D01.

## 0. What "independent" means here

The harness never imports or executes `tools/assemble-culture-d3.py`. It re-reads the four
component JSONs and rebuilds the projection itself:

| derived by this harness from components only | declared text taken from elsewhere (listed, not derived) |
|---|---|
| phonology + `coda` projection from `coda_subset` | the FILE-name/canon sentence and `morphology.type` (tool module constants, cross-checked against the packet declaration) |
| the six rule records (`pattern` built with my own `re.escape`, `output`, `gloss`, `source`) | the `assembly.rule` and 8 `assembly.limits` sentences (from `packet.json` `assembly.legacy_projection`, cross-artifact consistency only) |
| lexicon `term` + `era_forms`, name records (`stem`/`bases`/`expected`/`name`), eras, costumes (`garment` + `material` join through `material_id` → `gate_name`), materials, whole `assembly.trace` | `trace[*].display_label` (carried through from the components) |

The only shared code is the serializer: `yaml_lines` is loaded read-only from
`tools/assemble-d2.py`, the declared serializer whose digest the packet itself pins
(`tools/assemble-culture-d3.py:51` path constant; `packet.json` `assembly.serializer_sha256`).

Command (2026-10-17):

```
$ cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && python3 /var/tmp/d3-r9/rederive_projection.py
exit=1   # 62 checks passed, 1 failed (F1); 0 harness errors
```

## 1. Hand re-derivation of the name/rule step

E1 forms are taken from each lexeme's `forms.E1` in
`examples/culture-d3/components/04-language.json`; the projection's `stem`, `pattern` and
`name` are recomputed from those strings, then compared with the component records, the
committed `packet.gates.yml` and the `assembly.trace` of `packet.json`:

| name | bases | E1(b1) | E1(b2) | concat(E1b1,E1b2) | stem | rule id | pattern (parsed) |
|---|---|---|---|---|---|---|---|
| N01 | L02+L03 | `suma` | `talu` | `sumatalu` | `suma+talu` | `D3-N01-CONCAT` | `^(?P<B1>suma)\+(?P<B2>talu)$` |
| N02 | L08+L11 | `kila` | `nisu` | `kilanisu` | `kila+nisu` | `D3-N02-CONCAT` | `^(?P<B1>kila)\+(?P<B2>nisu)$` |
| N03 | L04+L12 | `falu` | `lura` | `falulura` | `falu+lura` | `D3-N03-CONCAT` | `^(?P<B1>falu)\+(?P<B2>lura)$` |
| N04 | L09+L05 | `ruma` | `fira` | `rumafira` | `ruma+fira` | `D3-N04-CONCAT` | `^(?P<B1>ruma)\+(?P<B2>fira)$` |
| N05 | L16+L20 | `ami` | `kuru` | `amikuru` | `ami+kuru` | `D3-N05-CONCAT` | `^(?P<B1>ami)\+(?P<B2>kuru)$` |
| N06 | L06+L13 | `fuka` | `sina` | `fukasina` | `fuka+sina` | `D3-N06-CONCAT` | `^(?P<B1>fuka)\+(?P<B2>sina)$` |

All six rows: `concat(E1(b1), E1(b2))` equals the component's `native_form` **and**
`formation.expected`, and equals the committed projection's `name` at
`examples/culture-d3/packet.gates.yml:259`, `:272`, `:285`, `:298`, `:311`, `:324` and the
`trace.names[*].name_projected` in `packet.json`. Every committed rule pattern equals the
pattern I rebuilt by hand, and `re.fullmatch(pattern, stem)` with `output = "{B1}{B2}"`
reproduces the projected name for all six (harness checks `replay: N01..N06`, all OK).

**Forcedness check (not just consistency):** for each projected name I enumerated all
400 ordered pairs of declared E1 lexeme forms. Each name has **exactly one** decomposing pair,
and it is the declared one:

```
$ python3 - <<'PY'    # 2026-10-17, components read directly, no assembler import
... enumerate all ordered pairs of declared E1 lexeme forms per projected name ...
PY
N01 'sumatalu': 1 concat pair(s) -> [('L02', 'L03')] declared=['L02', 'L03'] unique=True
N02 'kilanisu': 1 concat pair(s) -> [('L08', 'L11')] declared=['L08', 'L11'] unique=True
N03 'falulura': 1 concat pair(s) -> [('L04', 'L12')] declared=['L04', 'L12'] unique=True
N04 'rumafira': 1 concat pair(s) -> [('L09', 'L05')] declared=['L09', 'L05'] unique=True
N05 'amikuru': 1 concat pair(s) -> [('L16', 'L20')] declared=['L16', 'L20'] unique=True
N06 'fukasina': 1 concat pair(s) -> [('L06', 'L13')] declared=['L06', 'L13'] unique=True
```

So the derivation is not merely self-consistent: the declared bases are the *only* pair that
yields each projected name under the declared E1 forms.

## 2. Findings

### F1 — the two committed artifacts declare the projection rule with different sentences (minor, informational)

`packet.gates.yml:438` carries

> `rule: "native constructed forms only in gate-facing slots; English display labels are never projected as native strings"`

while `packet.json:16` (`assembly.legacy_projection.rule`) carries

> `"… English display labels are carried here and in packet records, never projected as native strings"`

They are two distinct literals in the generator
(`tools/assemble-culture-d3.py:374-375` for the projection, `:396-398` for the packet). Both
statements are true; they are simply not the same text.

Receipt and scope of the divergence — it is the *only* byte difference between my independent
reconstruction and the committed projection:

```
$ sha256sum /var/tmp/d3-r9/mine.yml examples/culture-d3/packet.gates.yml
829c5eb99779d1fed1b336ade42d6174cc5a47e52c7fbfad4dce2693e4eb2cf3  /var/tmp/d3-r9/mine.yml      (14227 B)
306bcac7b920840ae26f544afcf39a1f09666d6a8c5e786a5089e89af4c70425  examples/culture-d3/packet.gates.yml (14191 B)
$ # unified diff of committed vs mine: exactly one line, the rule sentence above
$ python3  # replace the 36-byte-longer sentence with the YAML's own text, then re-hash
patched bytes == committed bytes: True
len mine/committed/patched: 14227 14191 14191
sha256 patched: 306bcac7b920840ae26f544afcf39a1f09666d6a8c5e786a5089e89af4c70425
```

The byte delta (36 B) equals exactly the length of `"carried here and in packet records, "`.
Patching that one sentence makes my reconstruction **byte-identical** to the committed
projection, which is the strongest available evidence that every derived value (20 terms, 6
names, 6 rules, 4 garments, materials, eras, trace, phonology projection) is byte-exact.

Recommendation: either unify the sentence (the longer one is the more accurate: the projection
*does* carry labels in its trace) or record in the acceptance ledger that the two `rule` keys
are intentionally worded differently. Until then, **no byte-level cross-artifact assertion may
assume `packet.gates.yml`'s `assembly.rule` equals `packet.json`'s
`assembly.legacy_projection.rule`** — a re-pin or a drift-pin written against one will read as
drift against the other. No behavior impact: no gate reads either string.

### F2 — the D3 frozen pin is red on this tree (acceptance-affecting; independent confirmation)

```
$ python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json --frozen examples/culture-d3/expected.json
exit=2   counts {"D3-SNAPSHOT": 3, "total": 3}
  D3-SNAPSHOT: corpus/knowledge/synthesis/worldbible-integration-contract.md  declared 50c4c2f2…8fb7268c1, actual 5f4c02bf…fd4f79069
  D3-SNAPSHOT: tools/gates/costume-era-consistency-gate.py                    declared 29a9361c…b3e5b3a43f03, actual e6bffd70…ceec478f
  D3-SNAPSHOT: tools/gates/naming-collision-gate.py                           declared 8c5afb0a…f19aa526, actual d9e4e8f4…1a630a1d
```

(re-run 2026-10-17T20:52:10Z; stdout is one JSON object.) I reached this independently, by a
full sweep of the pin's own manifest — 24 entries, sha256 computed per path in Python — before
reading the peer shards:

```
manifest entries: 24 | mismatches: 3      # declared vs actual, three paths quoted above
```

It reproduces `reports/round-9/d3/check-diagnosis.md:19-20` and
`reports/round-9/d3/evidence-coupling.md:311-353`, and my `git show --stat e1694ba` agrees the
three files were last touched by round-8's admit commit.

Consequence for claim D: the clause *"D3 replays frozen without digest drift"* cannot be
recorded as clean today on this tree. The pin is doing its job (a stale pin reads
could-not-evaluate, never a silent pass), so the correct follow-up is a **re-acknowledgement**
of the three inputs, per input, not a re-run of the generator against the current tree:

- **Circularity warning for the re-pin.** Regenerating `expected.json`'s manifest from the live
  bytes would convert a real, explained drift into a green line with no evidence — the exact
  shape this review is chartered to catch. The re-pin should instead cite, per entry: the
  commit (`e1694ba`), what changed, and why the change is legitimate (D01's diagnosis already
  supplies this). Only then does a green `--frozen` mean something.
- **Behavior neutrality of the two drifted gates on this artifact is verified** (see §3), so
  the re-pin does not hide a D3 verdict change: the pinned round-7 gate code and the current
  gate code emit the *same* findings and exits on the committed projection.

Owner: orchestrator / R9-D01 / R9-D04. This shard does not edit `expected.json` or any other
worker's file.

## 3. Checks that came back clean (with receipts)

| check (2026-10-17) | command | result |
|---|---|---|
| assembler `--check` | `python3 tools/assemble-culture-d3.py --check` | exit 0, "packet.json: byte-identical …; packet.gates.yml: byte-identical …" |
| assembler self-test | `python3 tools/assemble-culture-d3.py --selftest` | exit 0, `selftest: 85/85 checks passed` |
| coupling self-test | `python3 tools/check-evidence-coupling.py --selftest` | exit 0, `"selftest_passed": true` |
| packet core | committed `packet.json` minus `assembly` | **equals** `{profile,name}` + my independent merge of the four components |
| packet bytes | `json.dumps(doc, sort_keys=True, indent=2, ensure_ascii=False)+"\n"` | equals the committed bytes |
| component digests | my `hashlib` recomputation vs `assembly.source_sha256` | identical (also matches `sha256sum examples/culture-d3/components/*.json`) |
| serializer digest | `hashlib.sha256(tools/assemble-d2.py)` vs `assembly.serializer_sha256` | identical (`8ea6bdde…`) |
| projection sections | my derived phonology / lexicon / names / eras / costumes / materials / rank_rules / cross_culture_review / rules / trace vs the parsed committed YAML | all deep-equal |
| native-only boundary | every `name`, `garment`, `term` string uses only the declared inventory | no offending symbol; no display-label value in any gate-facing slot |
| payload boundary | structural scan of the projection's sections | no `utterances`/`speech_rules`/`beliefs`/`symbols`/`objects`/`references`/`bridges`/`scope_notes`/`screening`/`naming_rule`/`sound_changes` section present; token occurrences (`AV1`, `utterance`, `beliefs`, `screening`) sit only in the declared `assembly.limits` prose |
| `compact()` hazard | every projected field non-`None` | no field silently dropped |
| gate verdicts, current gates | `python3 tools/gates/naming-collision-gate.py examples/culture-d3/packet.gates.yml` → exit 1: `NAME-NEAR` REVIEW + 2× `CROSS-HOLD` HOLD, no FAIL; `python3 tools/gates/costume-era-consistency-gate.py …` → exit 1: `R-01` note | as declared |
| gate verdicts, **pinned round-7 gates** | `git show 57c3ce6:tools/gates/naming-collision-gate.py > /var/tmp/d3-r9/naming-gate-r7.py` (sha256 `8c5afb0a…`, matches the pin), same for the costume gate (`29a9361c…`), then run both on the committed projection | **byte-identical output** to the current gates, same exits — the round-8 hardening is behavior-neutral on this artifact |

Boundary-is-load-bearing control (adversarial mutation, copies under `/var/tmp/d3-r9/`, repo
untouched): replacing one projected garment with its English label
(`leak-garment.yml`: `garment: "mila"` → `"visitor assembly robe (translated label)"`) makes
the real naming gate emit
`FINDING PHON-INVENTORY: FAIL — name C03 'visitor assembly robe (translated label)': symbol /v/ at position 1 is not in the declared inventory`;
replacing a projected `name` (`leak-name.yml`) additionally emits
`FINDING DERIV-REPLAY: FAIL … 'suma+talu' yields 'sumatalu'; the stated inputs and rules do not yield the candidate`.
So the native-only projection rule is not decorative: the committed artifact is on the safe
side of a gate that fails loudly on leakage.

## 4. Self-disclosure: one harness defect, found and fixed

My first run failed a boundary probe I wrote myself — a raw-token scan of the whole YAML for
`AV1`/`utterance`/`beliefs`/`screening`. Those tokens legitimately occur **inside the
`assembly.limits` sentence** ("AV1 substitution, utterance register law, beliefs, … have no
legacy-gate consumer"). The probe, not the artifact, was wrong. It is replaced by a structural
check over the parsed sections plus a line-scoped token check (a token line is acceptable only
if it carries the `no legacy-gate consumer` marker). Re-run: 62/63 (the remaining failure is
F1). Recorded here because a reviewer's own false positive is evidence too.

## 5. Limits and what this review did not do

- The re-derivation covers the **projection step** and the packet core. It does not re-implement
  the whole `build_legacy` (prose constants are taken as declared text, as tabulated in §0),
  and it does not re-derive the `d3-contract.json` field-by-field mapping (R9-D11's shard).
- The YAML is parsed for comparison with the lane's own reader
  (`tools/gates/costume-era-consistency-gate.py`'s `parse_packet`); no third-party YAML parser
  is installed (`import yaml` → `ModuleNotFoundError`), so cross-parser agreement is untested
  — `to-verify` for any future consumer that reads the projection with a different parser.
- Byte identity depends on `yaml_lines` (declared serializer, digest-pinned). A future change to
  that serializer would invalidate the byte comparison while leaving the derived values valid.
- Out of province and not assessed: whether the constructed forms should be screened against
  real languages (the packet's `screening.status: unresolved`), whether the packet should be canonized
  (lore-shokunin's decision), and the round-7 contract's own adequacy.
- Nothing here adjudicates the frozen-pin disposition; F2 states the constraint the
  orchestrator must satisfy and the circularity to avoid.

## 6. Hand-off to the orchestrator

- Claim D as written cannot include "frozen replay clean" until `examples/culture-d3/expected.json`
  is re-acknowledged per input (F2); the three drifts are legitimate but unexplained-in-artifact
  as of this review.
- If a D3 capability row is drafted, it should record: the step is reproducible from the
  components alone (62/63, F1 being prose only), the native-only boundary is enforced by a gate
  that fails on leakage, and the two committed artifacts carry different wording for the
  projection rule (F1).
- No source claim in this shard: every statement above is backed by a file path with line
  number, a command, or a hash, all produced on 2026-10-17.
