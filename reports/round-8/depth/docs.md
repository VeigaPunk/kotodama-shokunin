# R8-D15 — docs shard: example regeneration evidence + tool docstring/README fragment

- round: 8 (loop 1 of 3, build round 1 of 4); shard: D15 (docs)
- date: 2026-10-17 (all receipts below carry UTC `accessed-at`/`observed-at` stamps)
- baseline revision: `e7ca0faeb6680fa9891b907be628d9db578c28f4` (declared in
  `reports/round-8/claims.json`); measurement tree HEAD at run time:
  `cf338a713060f274269cdacb18cdc0085bb06aeb` (one dirty file and three
  untracked paths, listed in §1)
- owns: this file only (`reports/round-8/depth/docs.md`). The docstring and
  README text below are **fragments** for other shards/the orchestrator to
  land; this shard writes no tool, no example and no README.
- status: **partial** — regeneration evidence is complete for the existing D2
  example, including the post-sweep re-measurement (§2.7); the shipped tool's
  docstring is audited in §3.0 and its three-way CLI divergence from the D01
  spec and the D03 fragment is registered there; §3.1's draft fragment is
  retained only as the audit checklist. The frozen replay is fail-closed
  round-wide (§2.4/§2.7) and the D tool does not run at this revision (§3.0) —
  both flagged to the parent, neither fixed here. Details in §5.

Axis framing (what this shard measures): **depth** — the D claim's
"regenerates deterministically and replays frozen without digest drift"
clause needs a receipts-grade regeneration record and a docstring/README
fragment that a reader can follow without inventing an interface. This file
supplies both; it claims no new capability, no canon, and no acceptance.

## 1. Measurement tree and dependency status

Commands run from the lane root `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.

```sh
git rev-parse HEAD
git status --porcelain
```

Observed `2026-10-17T20:14:37Z`:

```
cf338a713060f274269cdacb18cdc0085bb06aeb
 M tools/gates/phonology-sanity-gate.py
?? corpus/lessons/round-8.md
?? reports/round-8/operability/
?? tools/harness/
```

- `tools/gates/phonology-sanity-gate.py` is dirty from a concurrent O-shard
  repair (unterminated flow-sequence/flow-mapping now raise `PacketError`
  instead of silently truncating; `git diff` at this stamp: 6 insertions,
  2 deletions). It is not this shard's file and is not modified here.
- Dependency status at this stamp: `reports/round-8/depth/design-spec.md`
  (D01) **absent**; `tools/d2-typed-labels.py` (D02) **absent**;
  `reports/round-8/depth/` did not exist before this file. Per the shard
  rule, the dependency-free parts (§2, §3, §4) were completed first, then the
  dependency paths were polled (§5.3). Two neighbor shards landed while this
  file was open and are used as corroboration, not authority:
  `reports/round-8/depth/findings-17.md` (D17 adversarial review, `20:15Z`)
  and `reports/round-8/depth/shard-parser.md` (D03 parser fragment, `20:16Z`,
  whose §4.3 fixes the `--packet`/`--selftest` CLI contract the §3 docstring
  fragment is written against).

## 2. Example regeneration evidence — the D2 example packet

The D2 example is `examples/culture-d2/`: 15 hand-authored component files
under `components/`, deterministically merged by `tools/assemble-d2.py` into
`packet.d2.yml` (156,071 bytes) using the costume gate's stdlib YAML-subset
reader (`tools/gates/costume-era-consistency-gate.py`). The generated packet
is git-clean at HEAD (bytes below equal `git show HEAD:examples/culture-d2/packet.d2.yml`).

### 2.1 Read-only drift check

```sh
python3 tools/assemble-d2.py --check
```

Observed `2026-10-17T20:14:37Z`: `packet.d2.yml: byte-identical deterministic
assembly`, **exit 0**.

### 2.2 True regeneration into an isolated tree (byte-identity, not just --check)

`--check` compares without writing; a stronger receipt is an actual rebuild in
a copied tree. Recipe (read-only with respect to the lane; writes only under
`/tmp`):

```sh
rm -rf /tmp/r8d15-build && mkdir -p /tmp/r8d15-build/tools/gates /tmp/r8d15-build/examples/culture-d2/components
cp tools/assemble-d2.py /tmp/r8d15-build/tools/
cp tools/gates/costume-era-consistency-gate.py /tmp/r8d15-build/tools/gates/
cp examples/culture-d2/components/*.yml /tmp/r8d15-build/examples/culture-d2/components/
(cd /tmp/r8d15-build && python3 tools/assemble-d2.py)
sha256sum /tmp/r8d15-build/examples/culture-d2/packet.d2.yml
cmp /tmp/r8d15-build/examples/culture-d2/packet.d2.yml examples/culture-d2/packet.d2.yml
```

Observed `2026-10-17T20:14:37Z`:

| step | observed |
|---|---|
| isolated build | `Wrote examples/culture-d2/packet.d2.yml (156071 bytes)`, exit 0 |
| isolated packet sha256 | `8da90b0788f86fd19babc67958715c8c16cb90a98e13572380b1c1892622b81e` |
| lane packet sha256 | `8da90b0788f86fd19babc67958715c8c16cb90a98e13572380b1c1892622b81e` |
| `cmp` | byte-identical (exit 0) |

The build wrote exactly one file: `find /tmp/r8d15-build -type f` at the same
stamp lists only the 15 copied components, the two copied tool files, and the
generated `examples/culture-d2/packet.d2.yml` — no scratch or side output.

### 2.3 Component digests and the assembler self-test

```sh
sha256sum examples/culture-d2/components/*.yml
python3 tools/assemble-d2.py --selftest
```

Observed `2026-10-17T20:14:37Z` (`sha256sum` of the 15 component inputs):

| component | sha256 |
|---|---|
| `01-brief.yml` | `ea0d67d0179aba4b118016f32f6cbf0d5e0dde92b1e8468ee6535e5026f2ea19` |
| `02-phonology.yml` | `23500df0f97a43c8800e3a678df6928f476254e56ff844fabe0c71829ecbb538` |
| `03-morphosyntax.yml` | `bd2f78c19eb4d788319760bcebd49973f53b416f3067737c507064b98ad8688d` |
| `04-orthography.yml` | `fa0d2000539cf63921b9629d320a96b359888b044f11bc486032aa76e0faade6` |
| `05-lexicon.yml` | `9bdcb8d895be0592047260361c4c12493569e7d38318b3508a5bde314d87abdf` |
| `06-pantheon.yml` | `5642c3fc20e12e6b8a83a914ff1fa22201d4858aab7b4fbd43f179ceae33d492` |
| `07-myths-motifs.yml` | `f26584436d84a31f4ece5c4241777cfd685587195a816c56d91b1d1903c9476d` |
| `08-symbols.yml` | `b8da2cb0181c54b0dd06fdcc400f94ded357e754309e27ff215905876d93c369` |
| `09-eras-calendar.yml` | `540a9339627fdcb802a7f59915a3c72e8234fff37c4a771783382af9c863b030` |
| `10-materials.yml` | `11a374d3a5b937a49ed10dc3026a1b681332e6081060ff5710e85a28d519865d` |
| `11-costumes.yml` | `b6e2c5c29cc5d68900d6cde5a8487e64f27d85ecb3d2bd7f3f5beb1113483f22` |
| `12-rank-rules.yml` | `28696a5a70404984fbf1a453f66c9e7618e318ebf93f25bce461fdb7dfcd35a3` |
| `13-naming.yml` | `e0c01eb22977e76e78251cd0b6f8f0b81d1917ca77c9ead04d06b1559b47b6df` |
| `14-kin-address.yml` | `4bfa35d08ae7345dea47852ebfc4734b469c671764bbefd2cc0f3a257330a6a6` |
| `15-pragmatics.yml` | `48484788bb69808d7d688951e87347107617a4b6572de0215e86d3f09cc323fd` |

`--selftest` observed at the same stamp: `selftest: 42/42 checks passed —
fixture CLI assemble/--check/tamper plus malformed, missing, duplicate-ID,
incomplete-record, duplicate-key, empty and wrong-wrapper controls; no file
outside the temporary directory touched`, **exit 0**.

### 2.4 Frozen replay — two observations, and the current fail-closed row

```sh
sha256sum tools/gates/frozen/round-3/MANIFEST.tsv          # d5337590b343c65b42fd6e55457862fa325c138ad652e59c81b887daf9971399
sha256sum tools/gates/frozen/round-3/inputs/examples/culture-d2/packet.d2.yml
python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv
```

- The frozen input copy still matches its pin: `54be6319e4907d20c8239555e3f79fcb9bb6b36d102a30a6beabf34b146459f4`
  = the `input_sha256` column of all five packet-gate rows in the manifest
  (verified `2026-10-17T20:14Z`).
- **Observation A** (this shard, `~2026-10-17T20:10Z`, before the concurrent
  phonology-gate edit appeared in the worktree): `REPLAY OK: 7/7 rows
  reproduced the recorded verdicts`, every row `bytes=match`, **exit 0**.
- **Observation B** (this shard, `2026-10-17T20:14:37Z`, after the edit):
  **exit 2** —
  `ROW 2 could-not-evaluate reason=gate_digest_mismatch gate=tools/gates/phonology-sanity-gate.py ... launched=no`
  with detail `gate: on-disk bytes are not the pinned revision`, then
  `REPLAY COULD-NOT-EVALUATE: 1 could-not-evaluate, 0 mismatch, 6 reproduced
  of 7 row(s)`. Live gate digest `660278f22d9f4e1d295aba19afa3b3014b7bd8b0e4fd1a503b594a84ab98e1f8`
  vs the manifest pin `fb05c644cafb0855481beb5d8bc3f619ae688d8b12787e530f01543f85372655`.

Interpretation, stated narrowly: the pin is doing exactly what the frozen-run
standard requires — a later hand-edit of a pinned gate contradicts the run
instead of silently re-blessing it (`corpus/knowledge/verification/gate-frozen-run-standard.md`
§§1–3; `corpus/knowledge/synthesis/worldbible-integration-contract.md` §4
"changing a referenced file invalidates that delivery's digest"). But the D
claim's literal wording — "replays frozen (`python3 tools/replay-frozen.py`)
without digest drift" — is **not satisfied at this revision**: 1 of 7 rows is
could-not-evaluate because the O-shard repaired a legacy parser defect in the
pinned gate. This is a cross-shard integration question, not a defect this
shard may fix: either (a) the O-shard/parent re-freezes a new baseline for the
repaired gate revision under `tools/gates/frozen/round-8/`, or (b) the claim
text is read as "the historical round-3 baseline replays" and the repaired
gate's row is honestly reported as could-not-evaluate. **Flagged to the
parent; not absorbed.** The five other packet rows and both provenance rows
still reproduce byte-identically from the retained snapshots.

Row-numbering note for re-runners: `replay-frozen.py` numbers rows from 2
(the manifest header is line 1); "7/7" means the seven data rows.

### 2.5 Digest history (pin vs live, so a reader does not mistake drift for regression)

| revision | packet sha256 | where recorded |
|---|---|---|
| round-3 initial capture | `f424fcf1b9613eb21d2901b19819a7e6c2a998cbcbd492a1a210d94eaae400cd` | `examples/culture-d2/ASSEMBLY.md:109` |
| round-3 frozen snapshot (pinned in MANIFEST) | `54be6319e4907d20c8239555e3f79fcb9bb6b36d102a30a6beabf34b146459f4` | `tools/gates/frozen/round-3/MANIFEST.tsv`, `input_sha256` column (re-verified `2026-10-17T20:14Z`) |
| committed round-4 baseline (`fe34faa`) | `d5fb408871dcb985c2f9b134a26c6d64e8640a6f1f17ba1c6bb3c5db1d6dbd96` | measured here: `git show fe34faa:examples/culture-d2/packet.d2.yml \| sha256sum`; corroborated at `reports/supplement-opencode-1/23-myth-coverage.md:7` |
| HEAD / worktree now (`cf338a7`) | `8da90b0788f86fd19babc67958715c8c16cb90a98e13572380b1c1892622b81e` | measured here `2026-10-17T20:14:37Z`; equals `git show HEAD:...` |

The changes between those revisions are the recorded round-4 component
reconciliation and later authored component edits, not silent drift: the
worktree packet is byte-identical to the deterministic assembly of the
worktree components (§2.2) and git-clean at HEAD.

### 2.6 Re-freeze path, if the parent takes option (a) of §2.4

Documentation only — this shard writes no baseline. Per
`corpus/knowledge/verification/gate-frozen-run-standard.md` §3–§5, a later
gate revision earns a **new** baseline (append-only; existing baselines are
never rewritten), laid out as
`tools/gates/frozen/<gate-name>/<round>-<phase>/` with `packet.yml`,
`expected.json`, `run.log`, `freeze.txt`; `expected.json` pins every input
digest, the `gate_sha256` at freeze time, and the finding-ID **set** (compare
by set, never stdout order). The round-3 TSV manifest is the legacy layout —
`examples/culture-d2/ASSEMBLY.md:127` already records that it is "not the
committed per-gate `expected.json` layout prescribed by the corpus frozen-run
standard", so re-freezing is also the step that retires that debt rather than
extending it. Until then the honest receipt is §2.4 observation B: the
round-3 pin stays legible, one row is could-not-evaluate, and no claim of
drift-free replay is made.

### 2.7 Post-sweep re-measurement (`2026-10-17T20:19:36Z`–`20:19:41Z`)

Between §2.2 and this subsection the O-shard repairs landed in all six gate
files (digests changed for `phonology-sanity-gate` → `722ff91b…`,
`lexicon-coverage-audit` → `989b1295…`, `myth-consistency-gate` → `270e4e0f…`,
`costume-era-consistency-gate` → `590e7f65…`, `naming-collision-gate` →
`ab98fe1a…`, `provenance-audit` → `8a96aaf4…`; first 8 hex digits). Re-run:

| command (same stamps) | observed |
|---|---|
| `replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv` | exit 2 — `REPLAY COULD-NOT-EVALUATE: 7 could-not-evaluate, 0 mismatch, 0 reproduced of 7 row(s)`; every row now `gate_digest_mismatch` |
| `assemble-d2.py --check` | exit 1 — `packet.d2.yml differs from deterministic assembly` |
| isolated rebuild (`/tmp/r8d15-build2`, same recipe) | wrote 156,071 bytes; sha256 `bad64fd4ae3b2a60dec51f7267f6e182b05272b815487d05ff132069bd6f5a24` ≠ committed `8da90b07…62b81e` |

The regeneration delta is **exactly one line**, and it is a provenance pin, not
content: `diff` between the rebuild and the committed packet is a single
hunk at `packet.d2.yml:3322`, `reader_sha256: "590e7f65…"` (rebuilt, = the
repaired costume gate) vs `reader_sha256: "29a9361c…"` (committed, = the
pre-repair reader). Content-level determinism therefore holds; what broke is
the committed packet's own reader-revision pin. Fixing it means regenerating
`examples/culture-d2/packet.d2.yml` with the repaired reader (a generated
artifact — the parent's call, not this shard's) and then either re-freezing or
honestly reporting the invalidated round-3 pin. Both consequences are the
same integration decision as §2.4/§2.6, now round-wide rather than single-row.

## 3. Tool docstring — audit of the shipped docstring, with the draft fragment as checklist

### 3.0 Audit result (the tool landed `2026-10-17T20:19Z`; this supersedes the draft as the docstring source)

The tool shipped with its own docstring (read at `tools/d2-typed-labels.py:1-58`,
file digest `080a3b2f2753e50eaab2f94273c107ce7866749c6b0dba9de6ac26aa1d216d28`
at `2026-10-17T20:19:54Z`). Audit of its interface claims against observed
behavior:

| docstring claim (line) | observed | verdict |
|---|---|---|
| Interface: default run writes the artifact; `--check` 0 identical / 1 drift / 2 error; `--report` prints, writes nothing; `--selftest` fixture controls (`:44-48`) | `--help` usage line `[-h] [--check \| --report \| --selftest]`; `--self-test` also accepted | matches |
| `--selftest` "drives this same CLI over a fixture component tree … touches no file outside that directory" (`:49-53`) | exit 1, `selftest: 0/2 checks passed` — at `20:19:21Z` (60,029-byte revision): `d2-typed-labels error: materials[CMAT-06].maps_to is unreadable: '10-materials MAT-05 lowland-plant-cloth (same slot) — note the convergent exclusions…'`; at `20:19:54Z` (digest `080a3b2f…`): `NameError: name 'assemble' is not defined` (`tools/d2-typed-labels.py:1132`, in `main`) | **not demonstrated; the tool is mid-edit by D02** |
| "The output (`examples/culture-d2/typed-labels.d2.yml`) is also a gate-facing projection" (`:33-38`) | the artifact does not exist; `--check` and `--report` on the live tree both exit 2 with the CMAT-06 error | not demonstrated |
| "stdlib only; read-only with respect to every source file; no network" (`:53-55`) | imports are `argparse, hashlib, json, pathlib, re, runpy, sys, tempfile` (`:59-66`) — stdlib only; read-only/no-network not independently exercised | partial: imports verified, behavior `to-verify` |
| "Design spec: `reports/round-8/depth/design-spec.md` when present" (`:57`) | the spec landed `20:18Z`; the conditional phrasing stays true | matches |

**Observation series (this shard; the tool is a moving target — D02 is editing
it while this file is written):**

| stamp (UTC) | tool digest (sha256) | `--selftest` | `--check` / `--report` |
|---|---|---|---|
| `20:19:21Z` | not measured (60,029 bytes) | exit 1, `selftest: 0/2 checks passed`; error `materials[CMAT-06].maps_to is unreadable` | `--check` exit 2, same error |
| `20:19:54Z` | `080a3b2f2753e50eaab2f94273c107ce7866749c6b0dba9de6ac26aa1d216d28` | exit 1, `selftest: 0/2 checks passed`; `NameError: name 'assemble' is not defined` (`:1132`) | not re-run |
| `20:21:07Z` | `429191fd14e01d52c208b0ad7dffdf79f034e430760caf60f12b1859b63725aa` | exit 1, `selftest: 0/2 checks passed`; `TypeError: eras_of() missing 1 required positional argument: 'tag_space'` | `--check` **exit 1** (drift) on an internal crash — contradicting its own documented `2 error` |
| `20:21:28Z` (shard close) | `f0192bc4f411fd116fa4c1e4e1e0460f0592dde8f4a2b9022fbaf4f51a5a6c7c` | exit 1, `selftest: 0/2 checks passed`; `NameError: name 'LEXICON_LAYER_KINDS' is not defined` | `--check` exit 1 |

The series is left **open**: D02 is editing the file while this shard closes,
and the last observed revision still fails. A stable revision that passes
`--selftest` is the precondition for the D-claim verdict and for finalizing
the docstring; nothing here substitutes for that.

Two further defects visible in the series, beyond "not yet working": (a) the
crash path (`TypeError`) is classified as drift (exit 1) instead of
could-not-evaluate (exit 2), so a broken tool can read as "packet drifted" —
the exact confusion the exit map exists to prevent; (b) at `20:19:21Z` the
tool's own parser could not read the real `10-materials` component
(`CMAT-06.maps_to` is a long descriptive string, not a slot id), so the
positive path fails on the live input, not only on fixtures. Both are D02's to
fix; recorded here as the docs audit.

**Interface divergence register** (report to the parent; D01/D02 own the
artifacts — this shard fixes nothing):

1. D01 spec outputs (`reports/round-8/depth/design-spec.md:55-62`): default = deterministic report to stdout, no writes; `--emit PATH` = write the projection; `--check`; `--selftest`.
2. D02 shipped tool (`tools/d2-typed-labels.py:44-48`): default = **write** the artifact; `--report` = print, writes nothing; `--check`; `--selftest`; no `--emit`.
3. D03 parser fragment (`reports/round-8/depth/shard-parser.md`, §4.3.1): `--packet <packet.yml>` printing one JSON document (`ok`/`stats`/`findings`).

Three shards, three CLIs; the shipped tool follows neither the spec's
default-no-write form nor D03's `--packet` form exactly. §3.1's draft fragment
was anchored to D03's contract and is therefore also wrong about the verbs. No
docstring can be final until D01/D02 reconcile — flagged to the parent, not
absorbed.

### 3.1 Draft fragment (retained as the audit checklist; superseded as the docstring source)

**Status: draft-pending-interface, anchored to the D03 parser contract.**
The tool file did not exist at `2026-10-17T20:16Z`, but the parser shard
landed `reports/round-8/depth/shard-parser.md` and its §4.3 fixes the
integration contract: `python3 tools/d2-typed-labels.py --packet <packet.yml>`
prints one JSON document with `ok`, `stats` and `findings`; exit 0 clean, 2
when an `E-*` (label) or loader `P-*` code fired; `--selftest` drives the same
CLI over isolated fixtures. The fragment below is rewritten to that contract.
The design spec (D01) was still absent at this stamp; if it lands with a
different interface, D02 reconciles and records the delta in its integration
log, and this fragment is re-cut to match the shipped CLI. **Anything that
does not match the real interface is `to-verify` and must not ship as the
docstring** — a docstring that advertises a flag the tool lacks is a
documentation defect of exactly the kind O-shards are repairing this round.

```python
#!/usr/bin/env python3
"""Type D2 labels before a packet claims them, without inventing canon.

Run from any directory:

    python3 tools/d2-typed-labels.py --packet examples/culture-d2/packet.d2.yml

prints one JSON document with `ok`, `stats` and `findings`; exit 0 clean,
2 when an E-* (label) or P-* (loader) code fired.

    python3 tools/d2-typed-labels.py --selftest

drives this same CLI over fixtures written into a temporary directory
(positive path plus malformed-input controls) and touches no file outside
that directory.

Kinds are declared, never guessed: `translated-label` (a modern/editorial
gloss, e.g. the English descriptive text a costume record carries),
`native-form` (the form as spelled in the culture's own system, with
language/stage and script/representation), and `borrowed-strata` (a form
carried in from a contact language; the layer_ref names the layer record
that supplies donor, entry stage and substitutions). A label record without
a kind is a finding, not a default.

Only a native-form or borrowed-strata surface form is graded on the sound
channel; a translated label is a reader-facing gloss and is never graded as
a form, and a donor form is provenance, never a D2 form to check or to
substitute. A label marked `verification: to-verify` keeps its finding
visible as a warning instead of vanishing, and an owed form slot is
reported as held — never dropped and never resolved to a nearby lexeme the
record does not own.

Scoped reconciliation resolves `era_window` against the packet's era
registry, `material_ids` against the material inventory and `layer_ref`
against the packet's layers; a label outside its referent's scope is
reported as out-of-scope rather than reconciled. The rank-rule adapter
groups rank rules against typed labels for the gate-facing view; it
executes and rewrites no rule.

Output is a design artifact (NON-CANON): typing a label does not establish
a real-world etymology, and a native form is a design record, not an
attested spelling.
"""
```

Checklist for D02 before embedding (each line must be true of the shipped tool):

- [ ] the run forms are the real ones (`--packet <path>`, `--selftest`), or the lines are rewritten;
- [ ] the JSON keys are exactly `ok`, `stats`, `findings` (D03 §4.3.1);
- [ ] the three kinds are spelled exactly as the parser accepts them (`translated-label`, `native-form`, `borrowed-strata`);
- [ ] exit codes: 0 clean, 2 for `E-*`/`P-*` — could-not-evaluate never exits 1;
- [ ] `--selftest` really writes only into a temp dir and touches no lane file;
- [ ] `to-verify` downgrades findings to warnings but keeps them visible;
- [ ] the non-canon/etymology limit sentence survives review (D16–D17);
- [ ] the grading-channel and held-slot clauses match the shipped behavior, not just the design intent.

**Peer expectation set (corroboration, not authority).** The D17 adversarial
reviewer derived two cases blind from the components alone
(`reports/round-8/depth/findings-17.md`, landed `2026-10-17T20:15Z`): C1
GAR-01 (`11-costumes.yml:215-233`) is a translated/display gloss with an owed
slot (`form: "(to-verify)"`, `05-lexicon.yml:407`) that must stay held and
must not be resolved to the base lexeme `mirken`; C2 L-26 `kas`
(`05-lexicon.yml:562-576`) is a loan-strata form whose donor `gas` is
provenance and whose layer (`Salt-road trade layer`, E1) must survive in the
typed output. Its named divergence modes — English string graded as a native
form, record silently passed, slot resolved to an invented form, donor form
checked or emitted as the D2 form — are exactly the failure classes the
docstring above is written to make impossible. The design spec (D01) and the
shipped tool (D02) remain the authority; this paragraph only records that a
blind independent derivation agrees with the fragment's semantics.

## 4. README fragment — regeneration section for the D2 example (DRAFT)

Intended landing surface: a new `examples/culture-d2/README.md`, or a
"Regenerate" section appended to `examples/culture-d2/ASSEMBLY.md`
(orchestrator's call; this shard writes neither). It mirrors the observed-table
style of `examples/culture-d3/README.md` §Reproduce.

````markdown
## Regenerate (D2 packet)

From the repository root. `packet.d2.yml` is a generated file: never
hand-edit it. After any intentional edit to a file under `components/`,
rebuild and re-check:

```sh
python3 tools/assemble-d2.py            # default build: writes exactly packet.d2.yml
python3 tools/assemble-d2.py --check    # read-only drift check (0 equal / 1 drift / 2 error)
python3 tools/assemble-d2.py --selftest # isolated positive + malformed-input controls
python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv
```

Observed 2026-10-17T20:14:37Z (docs shard, read-only lane runs):

| command | exit | observed |
|---|---:|---|
| `assemble-d2.py --check` | 0 | `packet.d2.yml: byte-identical deterministic assembly` |
| `assemble-d2.py` in an isolated copy (`/tmp`) | 0 | wrote 156071 bytes; sha256 `8da90b07…62b81e`; `cmp` byte-identical to the committed packet |
| `assemble-d2.py --selftest` | 0 | 42/42 checks passed |
| `replay-frozen.py …/round-3/MANIFEST.tsv` | 2 | fail-closed: 1 could-not-evaluate (`gate_digest_mismatch`, phonology gate repaired after the round-3 pin), 6/7 rows reproduced byte-identically |

This directory is a **non-canon design drill**. Regenerating it proves
determinism, not design quality, not scholarship, not canon; lore-shokunin
owns canon. The freeze that matters here is the round-3 gate manifest under
`tools/gates/frozen/round-3/`; documentation files are outside it by
construction (no self-digest cycle). A red or could-not-evaluate replay is
reported, never waved through: reproducing a red verdict does not clear D2,
and a changed gate revision invalidates its row rather than re-blessing it.
````

Contract anchors a reviewer can check this fragment against
(`corpus/knowledge/synthesis/worldbible-integration-contract.md`):
§2 separates concept identity from labels (SKOS row) — the reason labels are
typed rather than asserted; §4 `artifact_manifest`/`dependency_manifest`
require exact delivered bytes and pinned versions — the reason the digest
table exists; §5's lexicon row requires tracing a garment/ritual term to both
its linguistic rules and its material referent — the reason era/material
scoping is part of the tool rather than a gloss convention.

## 5. Limits, to-verify, and polling record

1. **The docstring source is now the shipped tool's own; §3.1's fragment is
   superseded as the docstring and retained only as the audit checklist**
   (§3.0). At this revision the shipped tool fails its own `--selftest`
   (0/2) and cannot build its artifact on the live tree, so every interface
   line in §3.0 stays **`to-verify`** until D02 lands a stable revision that
   passes. The D capability is **not** delivered at this revision; §4's
   replay row is red too (§2.4/§2.7).
2. **No new capability, no acceptance, no canon.** This file is documentation
   evidence; the D-claim verdict belongs to `reports/round-8/run-validation.py`
   (O15) and the parent.
3. **Polling record.** Dependency paths were polled at
   `2026-10-17T20:14Z`–`20:17Z` (30 s cadence, background poll): both
   **absent** at every stamp. They landed at `2026-10-17T20:19:14Z`
   (`tools/d2-typed-labels.py`, `reports/round-8/depth/design-spec.md`, plus
   `skill-table-draft.md`, `scribe.md`). The tool was then observed at
   `20:19:21Z` (60,029-byte revision, CMAT-06 error) and `20:19:54Z`
   (digest `080a3b2f…`, `NameError`), both failing; §3.0 records the audit.
   A final re-check is run before this shard closes and any change is
   appended here.
4. **Concurrency caveat for re-runners.** During this measurement window the
   worktree was heavily edited by sibling shards: all six gate files (O-shard
   repairs), ~110 corpus knowledge files (metadata sweep), and the D tool
   itself (mid-edit). Every digest above names its observation stamp; a re-run
   after integration may legitimately differ where sibling fixes land. Re-run
   §2's commands after the batch settles.
5. **Out of province, reported not absorbed:** the frozen-replay invalidation
   (§2.4/§2.7) is an O-shard/parent integration decision (re-freeze or report
   as historical); the three-way CLI divergence (§3.0) is D01/D02's; and canon
   status is lore's — none is decided here.

FILES: reports/round-8/depth/docs.md | SUMMARY: D15 docs shard — D2 regeneration evidence complete (isolated rebuild byte-identical at 20:14Z; post-sweep delta of exactly one line: the packet's `reader_sha256` pin), frozen replay now 7/7 could-not-evaluate after the O-shard gate repairs, and the shipped tool's docstring audited (tool does not run at this revision; three-way CLI divergence D01/D02/D03 registered) — all flagged to the parent, nothing fixed outside this file.
