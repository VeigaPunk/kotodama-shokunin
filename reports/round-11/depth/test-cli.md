# R11-D14 — CLI surface tests: the typed-pipeline wiring CLI

- seat: **R11-D14** (test shard, CLI negatives), round 11 (loop 1 of 3, build
  round 4 of 4), 2026-10-17
- assignment (verbatim): "DEPTH R11-D14 (test CLI): wiring CLI surface:
  `--help`, missing args, wrong packet; exit codes documented;
  reports/round-11/depth/test-cli.md."
- writes: this file only, plus in-lane scratch under `.scratch/r11d14/`. No
  tool, packet, component, gate, baseline or manifest is edited by this seat;
  `reports/round-{8,9,10}/**` and `tools/gates/{frozen,expected}/**` are filed
  and read-only here. No commit, no push.
- canon: NON-CANON engineering evidence. Nothing here admits a round, a
  capability or a canon fact; the lane's domain (linguistic-cultural
  worldbuilding) is untouched by this shard.
- status: **BOTH PHASES COMPLETE** — §1–§4 measure the pre-wiring surface
  (22:01–22:04Z); §5 measures the landed wiring CLI `tools/typed-gate-flow.py`
  (22:18–22:20Z) with 27 cases, six surface findings (CLI-1..CLI-4, §5.5) and
  the D-claim e2e leg confirmed green. §6 says what is not tested.

## 0. What this shard tests, and what it does not

Claim D (`reports/round-11/claims.json`) wires the round-8 typed-label
projection into the D2 flow and requires "end-to-end command over
`examples/culture-d2` exits 0 with findings exactly equal to the expected hold
set". This shard owns the **CLI surface of that wiring**: does the entry point
answer `--help`, refuse a missing argument, refuse a wrong packet, and are its
exit codes documented? Domain correctness, the hold-set equality, determinism,
frozen replay and the battery are other shards' claims (R11-D09..D16); the
wiring design is R11-D01..D02 and its implementation R11-D03..D08.

Environment (all commands below, unless a row says otherwise):
`Python 3.14.7 (main, Aug 10 2026)`, Linux, `TMPDIR=$PWD/.scratch` exported
before every scratch-writing command (`/tmp` inode exhaustion is the standing
environment defect, `reports/round-8/depth/test-cli.md` §6). Lane revision at
first stamp: `e3ef1719c123ab4fb83ed94e033961dd61a2e8c7` (`e3ef171`, the
round-11 claims commit). All scratch runs happen in an isolated copy
(`.scratch/r11d14/iso-baseline`, `cp -r tools examples corpus`, `__pycache__`
removed) so no lane file can be written by a test — including the modes that
do write (`assemble-d2.py` without `--check`, `d2-typed-labels.py --emit`).

## 1. Pre-wiring CLI surface (baseline, 2026-10-17T22:01–22:04Z)

Subject hashes at this stamp (`sha256sum`, run at 22:03:48Z):

| artifact | sha256 |
|---|---|
| `tools/assemble-d2.py` | `8ea6bdde9514ee966fe58cf219d4d0228ecc3b041e30549c68073cc822c8655d` |
| `tools/d2-typed-labels.py` | `0da0015f700345c938184cb45ca07178c33e98f798c3c09729007487fb89c802` |
| `examples/culture-d2/packet.d2.yml` | `e0f21509e14ac03ed5747e6bbbb48183cbe56d6b61afff8c8475e4a50137b643` |
| `examples/culture-d2/typed-labels.d2.yml` | `e70ba1477dbeb830061db6fd12516b7d902587bddae173f55a3650015d380b2f` |

### 1.1 The surface as shipped, verbatim

`python3 tools/assemble-d2.py --help` → exit 0:

```text
usage: assemble-d2.py [-h] [--check | --selftest]

Assemble D2's gate-facing records, without reconciling design disagreements.
...
options:
  -h, --help            show this help message and exit
  --check               compare packet.d2.yml against the assembly without writing
  --selftest, --self-test
                        run the fixture controls in a temporary directory
```

`python3 tools/d2-typed-labels.py --help` → exit 0:

```text
usage: d2-typed-labels.py [-h] [--packet PACKET] [--json] [--emit PATH]
                          [--check [PATH]] [--selftest]
```

Neither tool takes a positional argument; `assemble-d2.py` has no packet
flag at all (its output path is fixed to `examples/culture-d2/packet.d2.yml`,
`tools/assemble-d2.py:25`), so today a "wrong packet" cannot be presented to
it. That is the gap claim D's wiring has to close, and §5 re-tests it.

### 1.2 Case matrix (pre-wiring), 17 cases, isolated copy

Runner `.scratch/r11d14/cli-cases.py` (records exit, stdout/stderr sha256,
first line, line counts, traceback flag); spec
`.scratch/r11d14/spec-baseline.json`; results
`.scratch/r11d14/results-baseline.json`. `pass=16 fail=1 tracebacks=0`.

| # | case | exit | first line (stdout unless err) | verdict |
|---|---|---|---|---|
| 1 | `assemble-d2.py --help` | 0 | `usage: assemble-d2.py [-h] [--check \| --selftest]` | as expected |
| 2 | `assemble-d2.py -h` | 0 | same usage | as expected |
| 3 | `assemble-d2.py --check` | 0 | `packet.d2.yml: byte-identical deterministic assembly` | as expected |
| 4 | `assemble-d2.py --selftest` | 0 | `selftest: 42/42 checks passed …` | as expected |
| 5 | `assemble-d2.py --check --selftest` | 2 | err: usage + `argument --selftest: not allowed with argument --check` | as expected |
| 6 | `assemble-d2.py --bogus` | 2 | err: usage + `unrecognized arguments: --bogus` | as expected |
| 7 | `assemble-d2.py extra` (positional) | 2 | err: usage + `unrecognized arguments: extra` | as expected |
| 8 | `d2-typed-labels.py --help` | 0 | usage line | as expected |
| 9 | `d2-typed-labels.py` (report) | 1 | `FINDING D2L-FORM-UNRESOLVED: [hold] GAR-01 — …` | as expected |
| 10 | `d2-typed-labels.py --json` | 1 | `{"exit_code": 1, "findings": [{"code": "D2L-FORM-UNRESOLVED"…` | as expected |
| 11 | `d2-typed-labels.py --check` | **1** | err: `…/typed-labels.d2.yml differs from the deterministic projection` | **expected 0 — drift, §4** |
| 12 | `d2-typed-labels.py --bogus` | 2 | err: usage + `unrecognized arguments: --bogus` | as expected |
| 13 | `d2-typed-labels.py --packet` (no value) | 2 | err: usage + `expected one argument` | as expected |
| 14 | `d2-typed-labels.py --packet absent.yml` | 2 | `FINDING D2L-DATA: [fail] … — [Errno 2] No such file…` | as expected |
| 15 | `d2-typed-labels.py --emit fixtures/absent.yml` | 1 | `Wrote fixtures/absent.yml` (copy tree only) | as expected |
| 16 | `d2-typed-labels.py extra` (positional) | 2 | err: usage + `unrecognized arguments: extra` | as expected |
| 17 | `d2-typed-labels.py --selftest` | 0 | `selftest: 39/39 checks passed …` | as expected |

`grep -c Traceback` over the results JSON → `0` (2026-10-17T22:02Z), i.e. no
malformed input in this matrix produced a traceback. Case 4's `42/42` and case
17's `39/39` were additionally re-run in the lane tree at 22:03Z with the same
results and exit 0.

### 1.3 Wrong-packet matrix (pre-wiring), 8 cases

Same runner, spec `.scratch/r11d14/spec-wrongpacket.json`, results
`.scratch/r11d14/results-wrongpacket-prewire.json`; all cases are
`d2-typed-labels.py --packet <fixture>` because that is the only packet-taking
CLI in the lane. `pass=8 fail=0 tracebacks=0`.

| fixture (bytes) | exit | diagnostic (first line) |
|---|---|---|
| `empty.yml` (0) | 2 | `FINDING D2L-DATA: [fail] fixtures/empty.yml — no content lines` |
| `wrong-root.yml` (19) | 2 | err: `d2-typed-labels error: packet.eras: expected a non-empty list of era tags` |
| `latin1.yml` (11, ISO-8859) | 2 | `FINDING D2L-DATA: … 'utf-8' codec can't decode byte 0xe9…` |
| `truncated.yml` (400, first 400 B of the real packet) | 2 | `FINDING D2L-DATA: … — unterminated quote` |
| `partial.yml` (25) | 2 | err: `packet.eras: expected a non-empty list of era tags` |
| `adir` (directory) | 2 | `FINDING D2L-DATA: … — [Errno 21] Is a directory…` |
| `d3-packet.json` (37222, the D3 example packet) | 2 | `FINDING D2L-DATA: … content '{' is not a mapping line` |
| real packet (control) | 1 | `FINDING D2L-FORM-UNRESOLVED: [hold] GAR-01 — …` |

So the round-8 surface already fails closed on every wrong-packet class this
shard could construct; the wiring inherits this behavior only if its new CLI
reuses the same loader path — §5 tests exactly that on the wired entry point.

### 1.4 Sibling surface census (context, not this shard's subject)

`.scratch/r11d14/surface-scan.py` records each tool's sha256, `--help` exit
code and visible flags (`.scratch/r11d14/census-prewire.json`, 15 tools,
22:02Z). `--help` split: exit 0 for `assemble-d2`, `assemble-culture-d3`,
`check-gate-battery`, `d2-typed-labels`, `replay-frozen`,
`source-audit-inventory`, `gates/handoff-packet-check`, `gates/provenance-audit`,
`gates/lexicon-coverage-audit`, `gates/costume-era-consistency-gate`; **exit 2**
for `check-craft-exercise`, `check-evidence-coupling`, `gates/phonology-sanity-gate`,
`gates/myth-consistency-gate`, `gates/naming-collision-gate` (the last three treat
`--help` as a packet path: `FINDING G-DATA: cannot read --help`). This matches
`reports/round-8/depth/test-cli.md` §7 — the split is standing, not new. The
census is re-run after the wiring lands and diffed in §5.6.

## 2. Exit codes — documented contract (pre-wiring, as observed)

| code | meaning | receipts |
|---|---|---|
| 0 | clean: `--check` byte-identical; `--selftest` all controls pass; a flow that found only *expected* holds (this last sense is claim D's requirement, untested pre-wiring) | cases 3, 4, 17 |
| 1 | findings emitted (report/`--json`/`--emit`), or `--check` byte-drift | cases 9, 10, 11, 15 |
| 2 | usage error (argparse) **or** could-not-evaluate (unreadable / non-UTF-8 / unparsable / schema-less packet, unwritable output path) | cases 5–7, 12–14, 16; §1.3 all rows |

Convention cross-check: the lane's standard is 0/1/2 with `2` reserved for
could-not-evaluate (`SKILL.md:132`; `corpus/knowledge/verification/gate-frozen-run-standard.md`
"`2` is reserved for could-not-evaluate"; `reports/round-8/depth/design-spec.md:71-77`).
Both shipped tools match. The one nuance a consumer keying on the exit code
alone must know is inherited from round 8: `--check` answers **byte-identity
only** and exits 0 even when the same packet carries findings
(`reports/round-8/depth/test-cli.md` §3).

## 3. `--help` / usage behavior worth stating (pre-wiring)

- Both tools use argparse, so `-h ≡ --help`, exit 0, usage on stdout — unlike
  the five sibling tools in §1.4 that exit 2 on `--help`.
- Neither tool enforces mutual exclusion across all modes:
  `d2-typed-labels.py` has no mutually-exclusive group, so `--json --emit X`
  is legal and silently drops the write (observable precedence
  `--check > --json > --emit > report`, `reports/round-8/depth/test-cli.md` §2,
  restated by this shard's reading of `tools/d2-typed-labels.py:2865-2907`).
  `assemble-d2.py` does enforce one group (`--check | --selftest`), exit 2.
  A wired CLI adding flags should state its precedence in `--help`, or the
  R8-D10 O6 finding repeats in a new surface (report, not absorbed).

## 4. Pre-wiring precondition: `d2-typed-labels.py --check` exits 1

Reproduced at 22:02Z in the isolated copy and at 22:03Z in the lane root:

```sh
python3 tools/d2-typed-labels.py --check
# exit 1: examples/culture-d2/typed-labels.d2.yml differs from the deterministic projection
```

Cause (independently on record — `reports/round-10/findings-scribe.md` A2,
`reports/round-10/findings-verify-1.md` NEW-2, and this wave's
`reports/round-11/depth/scribe.md` §1.2): the committed artifact records
`assembly.packet_sha256 = 8da90b07…` while the committed packet hashes
`e0f21509…`; masking any 64-hex string makes `diff` empty, i.e. that single
recorded digest is the whole drift. The pair has been inconsistent since the
round-8 admit commit `e1694ba` re-pinned the packet without re-emitting the
artifact. This shard re-measured it (one-line diff, `sha256sum`; 22:02Z) rather
than adopting the earlier claim, and reports that the pre-wiring state is
**red by design of the round-8 integration, not by CLI defect**. Whether
round-11's wiring re-emits the artifact and turns this command green is the D
claim's business; §5 records the post-wiring value.

**Post-stamp (22:14Z): the re-pin landed.** `examples/culture-d2/typed-labels.d2.yml`
is now `a3aa452cd5ae77c351d9532a707fb1f1ababf77c3fad8b9d28089e6958364a43` and
`python3 tools/d2-typed-labels.py --check` → exit 0,
`examples/culture-d2/typed-labels.d2.yml: byte-identical deterministic projection`.
The §4 drift is closed in the live tree; the paragraph above stands as the
pre-re-pin record.

## 5. Post-wiring surface (measured)

### 5.1 What landed, at which hashes (22:18–22:20Z)

| subject | revision |
|---|---|
| the wiring CLI | `tools/typed-gate-flow.py` sha256 `5758e315593bb818dbf38c3c3ed7f79eb9ea555955331fadab4b50b2faa92075` (38525 bytes, docstring: "the D2 typed-pipeline wiring (round 11, R11-D05)") |
| typed packet (committed artifact) | `examples/culture-d2/packet.d2.typed.yml` sha256 `e8a83445e46deadde358e3ebb20c2d47decee91d3f2a1341d28ebfe6934e09bb` |
| expected set (committed artifact) | `examples/culture-d2/typed-gate.expected.json` sha256 `7ed597317b32b238d880af0a602fcbfa1ffd92608008879f049db9fd02aa03aa` |
| projection (re-pinned, §4) | `examples/culture-d2/typed-labels.d2.yml` sha256 `a3aa452cd5ae77c351d9532a707fb1f1ababf77c3fad8b9d28089e6958364a43` |

The wiring shipped **not** under the two tool names design.md §2.2/§3.1
specifies: `tools/assemble-d2-typed.py` and `tools/gates/typed-pipeline-gate.py`
did not exist at 22:20Z (`ls` → "No such file or directory"), and
`tools/assemble-d2.py` / `tools/d2-typed-labels.py` kept their §1 hashes. This
shard tests what shipped; the design-vs-shipped naming/integration question
belongs to the R11-D20 wiring-vs-spec reviewer.

### 5.2 Surface as shipped (verbatim, exit 0)

```text
usage: typed-gate-flow.py [-h] [--packet PACKET] [--typed-packet TYPED_PACKET]
                          [--expected EXPECTED] [--typed-override PATH]
                          [--json] [--flow] [--emit] [--check]
                          [--freeze [DIR]] [--selftest]

typed-gate-flow — the D2 typed-pipeline wiring (round 11, R11-D05).

options:
  -h, --help            show this help message and exit
  --packet PACKET       the assembled D2 packet (default: examples/culture-d2/packet.d2.yml)
  --typed-packet TYPED_PACKET
                        the committed typed gate packet (default: examples/culture-d2/packet.d2.typed.yml)
  --expected EXPECTED   the committed expected set (default: examples/culture-d2/typed-gate.expected.json)
  --typed-override PATH
                        evaluate this typed packet instead of deriving one
  --json                one JSON document
  --flow, --e2e, --typed-flow, --wired-flow
                        run the end-to-end D2 typed flow (the default report)
  --emit                write the derived typed packet and expected set
  --check               byte-compare the derived artifacts; writes nothing
  --freeze [DIR]        write a frozen replay generation (default: tools/gates/frozen/round-11)
  --selftest, --self-test
                        mirrored e2e plus mutation controls
```

Its docstring states the exit contract this shard tests: "0 = every check
passes …; 1 = a check failed (findings printed); 2 = could-not-evaluate
(missing or malformed input, **no traceback**)."

(Transcription note: the usage block above is verbatim; inside `options:` the
line wrapping is normalized to this doc's width — flag names, defaults and help
sentences are as emitted. The same note applies to §1.1.)

### 5.3 Case matrix — 27 cases, isolated copy `iso-flow`

Runner/spec/results: `.scratch/r11d14/{cli-cases.py,spec-typed-flow.json,results-typed-flow.json}`;
`pass=21 fail=6 tracebacks=2`. The assigned surfaces (`--help`, missing args,
wrong packet) and every supporting case:

| # | case | exit | observed | verdict |
|---|---|---|---|---|
| 1 | `--help` | 0 | usage (§5.2) | as documented |
| 2 | `-h` | 0 | same | as documented |
| 3 | default e2e | 0 | banner + 15 hold lines; `summary: 10/10 checks passed` | **claim-D leg: exit 0 with findings == expected set** |
| 4 | `--flow` | 0 | same as #3 | alias works |
| 5 | `--e2e`, `--typed-flow`, `--wired-flow` | 0 | same as #3 (re-run 22:19Z) | aliases work |
| 6 | `--json` | 0 | one JSON document, `exit_code: 0`, `findings` 16 (15 hold + 1 note), `translated_on_sound_channel: 0`, `owed_native_forms: 10`, 10/10 checks ok | as documented |
| 7 | `--check` | 0 | `typed gate artifacts: byte-identical deterministic derivation` | as documented |
| 8 | `--emit` | 0 | `Wrote examples/culture-d2/packet.d2.typed.yml and examples/culture-d2/typed-gate.expected.json` (copy tree) | as documented |
| 9 | `--freeze` (into copy) | 0 | writes `tools/gates/frozen/round-11/{MANIFEST.tsv,inputs,legacy,*.out}` | as documented |
| 10 | `--selftest` | 0 | `summary: 10/10 checks passed` | as documented |
| 11 | `--bogus` | 2 | err: usage + `unrecognized arguments: --bogus` | as documented |
| 12 | `--packet` (no value) | 2 | err: usage + `expected one argument` | as documented |
| 13 | extra positional | 2 | err: usage + `unrecognized arguments` | as documented |
| 14 | `--packet` missing file | 2 | `could-not-evaluate: packet could not be loaded: [{'code': 'P-IO' …}` | as documented |
| 15 | `--packet` empty file | 2 | `… [{'code': 'P-EMPTY' … 'no content lines'}` | as documented |
| 16 | `--packet` truncated | 2 | `… [{'code': 'P-UNTERMINATED-FLOW', 'line': 28 …}` | as documented |
| 17 | `--packet` Latin-1 | 2 | `… [{'code': 'P-ENCODING' …}` | as documented |
| 18 | `--packet` directory | 2 | `… [{'code': 'P-IO' … Errno 21}` | as documented |
| 19 | `--packet` D3 JSON packet | 2 | `… [{'code': 'P-UNTERMINATED-FLOW', 'line': 1 …}` | as documented |
| 20 | **`--packet` wrong root key** | **1** | **raw `ReconciliationError` traceback**, 16 stderr lines | **CLI-1, §5.5** |
| 21 | `--packet` partial stub (`packet: eras:`) | **1** | same `ReconciliationError` traceback (re-run 22:19Z) | **CLI-1** |
| 22 | `--typed-override` missing file | **1** | **raw `FileNotFoundError` traceback** | **CLI-2** |
| 23 | `--typed-override` truncated | 2 | `could-not-evaluate: costume-era-consistency-gate.py: exit 2:` | as documented |
| 24 | `--typed-packet` missing | **1** | `FAIL typed-packet-pinned — derived typed packet differs from fixtures/absent.yml` + 49-line report | **CLI-3** |
| 25 | `--typed-packet` empty | **1** | `FAIL typed-packet-pinned — … differs from fixtures/empty.yml` | **CLI-3** |
| 26 | `--expected` missing | **1** | `FAIL expected-present — missing: fixtures/absent.json` | **CLI-4** |
| 27 | `--expected` malformed / wrong schema | **1** | `FAIL expected-parse — … not valid JSON`; with valid-JSON-wrong-shape `{'x': 1}`: `schema is None, expected 'kotodama-typed-gate-expected-v1'` | **CLI-4** |

Composite-flag behaviour (re-run 22:19Z, all exit 0): `--json --check` prints
the **check** message, not JSON (`--check` wins, as in `d2-typed-labels.py`);
`--emit --check` **does both** — writes the artifacts *and* prints
`byte-identical deterministic derivation`. So the flag precedence a consumer
must know is `--check` > `--json`, while `--emit` composes with `--check`
(contrast §3: `d2-typed-labels.py`'s `--check` suppresses `--emit`).

Tamper control (not a CLI case; confirms exit-1 has teeth): appending
`\n# tamper\n` to the copy's committed `packet.d2.typed.yml` turns `--check`
→ exit 1 `typed-packet-pinned: derived typed packet differs …` and the e2e →
exit 1 with `FAIL typed-packet-pinned`; restoring the byte restores exit 0.

### 5.4 Exit codes — documented vs observed (wired surface)

| code | tool docstring says | observed |
|---|---|---|
| 0 | every check passes | 17 cases (#1–10, aliases, composites, tamper-restored) |
| 1 | a check failed | tamper control; **and four missing/malformed-input classes (#20–22, 24–27)** |
| 2 | could-not-evaluate, no traceback | five malformed-packet classes (#14–19, 23) — **but not #20–22** |

The D-claim sentence "end-to-end command over examples/culture-d2 exits 0 with
findings exactly equal to the expected hold set" is confirmed at the CLI level:
case 3 exits 0 while printing the 15 named holds and one note, and `--json`
reports `findings` 16 / `hold-set-equal: true` / `translated_on_sound_channel: 0`
(the banner line exists so this is not readable as "clean"). Exit 0 therefore
means *pipeline consistent with the frozen expectation*, not *no findings* — the
same nuance this doc records for `--check` in §2, in a stronger form.

### 5.5 Findings (reported to the owner, not fixed here)

- **CLI-1 — uncaught `ReconciliationError` on a schema-less packet.**
  `python3 tools/typed-gate-flow.py --packet fixtures/wrong-root.yml` (a legal
  YAML mapping whose root keys are wrong) exits **1** with a 16-line traceback:
  `tools/d2-typed-labels.py:1587 raise ReconciliationError("packet.eras: expected
  a non-empty list of era tags")` reached through
  `tools/typed-gate-flow.py:316 typed_ns["run_pipeline"](str(packet_path))`.
  The projector's own CLI catches this class and returns 2
  (`tools/d2-typed-labels.py:2908`); the flow's handler does not, contradicting
  its docstring's "no traceback" promise. Reproduced twice (22:18Z, 22:19Z).
- **CLI-2 — uncaught `FileNotFoundError` on `--typed-override`.**
  `--typed-override fixtures/absent.yml` exits **1** with a traceback from
  `tools/typed-gate-flow.py:335 Path(typed_override).read_bytes()`; same
  contract contradiction. The neighbouring malformed case (#23) does exit 2.
- **CLI-3/CLI-4 — missing/malformed committed artifacts exit 1, not 2.**
  `--typed-packet <absent|empty>` and `--expected <absent|malformed>` produce
  *named* check failures (`typed-packet-pinned`, `expected-present`,
  `expected-parse`) and exit 1 with a full report. Read as artifact-drift
  detection this is defensible; read against the docstring's "missing or
  malformed input → 2" it is a divergence. Flagged for the owner's decision —
  this shard does not absorb it, and does not call it a defect either way.

None of the four affects the green path (cases 3–10) or the claim-D counting
command; all four are *fail-closed* (no case produced a wrong-success exit 0).

**Independent corroboration** (same tool revision `5758e315…`): the sibling
boundary shard `reports/round-11/depth/test-boundary.md` §6, row W4, records
exactly CLI-2 (`--typed-override` absent → exit 1, traceback at
`typed-gate-flow.py:335`), and rows W6–W8 record CLI-3/CLI-4's exit-1 behaviour
for `--expected`/`--typed-packet` absent or malformed. Its W3 records one more
member of the same handler-seam class (`KeyError: 'kind'` from
`tools/d2-typed-labels.py:2497` reaching the flow at `:316`). This shard's
CLI-1 (`ReconciliationError` from the same `:316` call, reached with a packet
that is legal YAML but schema-less) is a distinct input class from W3 and was
not in that table; both are uncaught-exception paths of the flow's
`evaluate()` seam. Corroboration is cited, not adopted: each doc's own commands
are its receipts.

### 5.6 Census diff (pre → post)

`.scratch/r11d14/surface-diff.py --before census-prewire.json --after census-post.json`
→ `surface changes: 2` (17 tools): **NEW TOOL `tools/typed-gate-flow.py`** (this
claim's wiring) and **NEW TOOL `tools/exercise-handoff-e2e.py`** (claim O's
exercise — not this shard's subject; it is noted here only because the census
reports it). Every other tool's sha256 is unchanged; `--help` split unchanged
from §1.4.

### 5.7 Superseded fragment, recorded for the record

The R11-D03 fragment delivered a *different* prototype
(`.scratch/D03/assemble-d2-typed.py`, sha256 `95ac9d05…`, staged for landing as
`tools/assemble-d2-typed.py`, which did not land by 22:20Z). Tested in an
isolated copy at 22:09–22:12Z, its CLI behaved well on 20/20 cases (all
wrong-packet and wrong-projection classes exit 2 fail-closed, no tracebacks,
`--emit` creates missing parent directories) — with one defect that matters
**only if that file is landed as-is**: its `--selftest` asserts the *committed*
projection is stale (`.scratch/D03/assemble-d2-typed.py:94-98`, "stale committed
projection refused with exit 2"), so on a re-pinned tree it exits **1** with
`21/22 checks passed` (reproduced in `.scratch/r11d14/iso-typed2`, 22:11Z).
A selftest bound to mutable repo state inverts the moment claim D's own re-pin
succeeds. The landed `tools/typed-gate-flow.py --selftest` has no such
dependency (case 10, 10/10).

## 6. Limits

- Revision-bound: every digest and exit code in §1–§4 describes the hashes in
  §1 at 22:03Z; §5 describes `tools/typed-gate-flow.py`
  `5758e315593bb818dbf38c3c3ed7f79eb9ea555955331fadab4b50b2faa92075` at
  22:18–22:20Z. Tools in this lane were live during earlier waves (24 distinct
  revisions in 15 minutes during round 8); **a later revision of the wired CLI
  invalidates §5** and must be re-tested. The landed wiring did *not* change
  `tools/assemble-d2.py` or `tools/d2-typed-labels.py` (their §1 hashes held
  through 22:20Z), so §1.1/§1.2 rows 1–17 and §1.3 stay valid; §1.2 row 11 and
  §4 describe the pre-re-pin state and are superseded by §5.1's post-stamp.
- Only CLI surface behavior is measured. No domain, canon, attribution or
  rights claim is made or implied (`PROVINCE.md`; `AGENTS.md`). Whether the
  routed/labelled content is *right* is not tested here.
- The wrong-packet fixtures are synthetic except `d3-packet.json` (a verbatim
  copy of the D3 example) and `truncated.yml` (the first 400 bytes of the real
  packet); no fixture is claimed to be a legal packet.
- Scratch lives in-lane under `.scratch/r11d14/` (watcher log, specs, results,
  census, fixtures); nothing outside the lane was written, and no filed
  artifact of rounds 8–10 was touched. One copy-only exception is stated where
  it applies: tamper controls and `--emit`/`--freeze` runs wrote inside the
  isolated copies `iso-flow`/`iso-typed`/`iso-typed2`, never in the lane tree.
- Observed while polling (reported, not absorbed, not this shard's subject):
  `git status` at 22:14Z showed modified filed receipts
  `reports/round-{5,6,7,8,9}/validation.json` and
  `reports/round-10/coverage/index-update-22.md`. That is the round-10
  "filed receipt bytes rewritten" conformance-defect pattern recurring; the
  X02 adjacency seat and the orchestrator own it, and this shard touched none
  of those files.

## 7. Reproduction

```sh
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
export TMPDIR=$PWD/.scratch
ISO=$PWD/.scratch/r11d14/iso-baseline          # or any isolated copy
python3 .scratch/r11d14/cli-cases.py --spec .scratch/r11d14/spec-baseline.json \
        --cwd "$ISO" --out .scratch/r11d14/results-baseline.json --env TMPDIR=$TMPDIR
python3 .scratch/r11d14/cli-cases.py --spec .scratch/r11d14/spec-wrongpacket.json \
        --cwd "$ISO" --out .scratch/r11d14/results-wrongpacket-prewire.json --env TMPDIR=$TMPDIR
python3 .scratch/r11d14/surface-scan.py --root . --out .scratch/r11d14/census-prewire.json
```

## Receipts

```sh
# 2026-10-17 22:01–22:04Z, lane root, TMPDIR=$PWD/.scratch
sha256sum tools/assemble-d2.py tools/d2-typed-labels.py \
          examples/culture-d2/packet.d2.yml examples/culture-d2/typed-labels.d2.yml
git rev-parse HEAD                      # e3ef1719c123ab4fb83ed94e033961dd61a2e8c7
python3 .scratch/r11d14/cli-cases.py --spec .scratch/r11d14/spec-baseline.json …      # pass=16 fail=1 tracebacks=0
python3 .scratch/r11d14/cli-cases.py --spec .scratch/r11d14/spec-wrongpacket.json …   # pass=8  fail=0 tracebacks=0
python3 .scratch/r11d14/surface-scan.py --root . --out .scratch/r11d14/census-prewire.json   # 15 tools
python3 tools/d2-typed-labels.py --selftest        # exit 0, 39/39 checks passed
python3 tools/assemble-d2.py --selftest            # exit 0, 42/42 checks passed (isolated copy)
python3 tools/d2-typed-labels.py --check           # exit 1 — §4 precondition
```

```sh
# 2026-10-17 22:14–22:20Z, post-wiring (isolated copies iso-flow / iso-typed2)
sha256sum tools/typed-gate-flow.py examples/culture-d2/{packet.d2.typed,typed-gate.expected.json,typed-labels.d2.yml}
python3 .scratch/r11d14/cli-cases.py --spec .scratch/r11d14/spec-typed-flow.json \
        --cwd "$PWD/.scratch/r11d14/iso-flow" --out .scratch/r11d14/results-typed-flow.json \
        --env TMPDIR=$PWD/.scratch/r11d14/tmp                    # pass=21 fail=6 tracebacks=2
python3 .scratch/r11d14/cli-cases.py --spec .scratch/r11d14/spec-typed-adapter.json \
        --cwd "$PWD/.scratch/r11d14/iso-typed" …                 # 20/20 on the superseded fragment
python3 .scratch/r11d14/surface-scan.py --root . --out .scratch/r11d14/census-post.json   # 17 tools
python3 .scratch/r11d14/surface-diff.py --before …/census-prewire.json --after …/census-post.json  # 2 new tools
python3 tools/d2-typed-labels.py --check           # exit 0 — drift closed by the re-pin
python3 tools/typed-gate-flow.py                   # exit 0, 15 holds + 1 note, 10/10 checks
```
