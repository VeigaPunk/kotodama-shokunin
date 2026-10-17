# R11-D13 — boundary tests: malformed typed packets → stable exit-2 diagnostics

- seat: **R11-D13** (test shard, boundary/malformed), round 11 (loop 1 of 3, build
  round 4 of 4), 2026-10-17
- assignment (verbatim): "DEPTH R11-D13 (test boundary): malformed typed packets ->
  stable exit-2 diagnostics; reports/round-11/depth/test-boundary.md."
- writes: this file only, plus in-lane scratch under `.scratch/d13/`. No tool, packet,
  component, gate, baseline or manifest is edited by this seat; `reports/round-{8,9,10}/**`
  and `tools/gates/{frozen,expected}/**` are filed and read-only here. No commit, no push.
- canon: NON-CANON engineering evidence. Nothing here admits a round, a capability or a
  canon fact; the lane's domain (linguistic-cultural worldbuilding) is untouched.
- status: **COMPLETE** — the round-8 projector boundary (§2–§5, F1–F7 at
  `tools/d2-typed-labels.py` `0da0015f…`) and the **wired** boundary (§6, W1–W16 at
  `tools/typed-gate-flow.py` `5758e315…`) are both measured; the projector's crash (F1)
  propagates through the wired CLI (W-F1) and one new wired-CLI crash is reported (W-F2).
  §7 says what is not tested.

## 0. Scope and subject

Claim D wires the round-8 typed-label projection into the D2 gate flow. This shard owns
the **malformed-input boundary**: a typed packet that is unparsable, structurally wrong
or schema-invalid must produce a **stable exit-2 diagnostic**, never a traceback and never
a silent pass (`reports/round-8/depth/design-spec.md:71-78` exit table; the wiring design
restates it — `reports/round-11/depth/design.md:199-203`: "2 could-not-evaluate: stale
projection pin, malformed packet, gate traceback, pin mismatch").

Subjects at the measurement stamps:

| artifact | sha256 | role here |
|---|---|---|
| `tools/d2-typed-labels.py` | `0da0015f700345c938184cb45ca07178c33e98f798c3c09729007487fb89c802` | typed-packet consumer (round 8) — subject of §2–§5 |
| `examples/culture-d2/packet.d2.yml` | `e0f21509e14ac03ed5747e6bbbb48183cbe56d6b61afff8c8475e4a50137b643` | base packet every mutation starts from |
| `examples/culture-d2/typed-labels.d2.yml` | `e70ba147…` at my stamps → **`a3aa452cd5ae77c351d9532a707fb1f1ababf77c3fad8b9d28089e6958364a43`** from 22:14Z | committed projection — re-pinned by a sibling shard mid-window (the `design.md` §5.1 predicted bytes); not read by any run of §2–§5, so no verdict here binds it |
| `tools/typed-gate-flow.py` | `5758e315593bb818dbf38c3c3ed7f79eb9ea555955331fadab4b50b2faa92075` | the round-11 wired entry point — subject of §6 |

Environment: Python 3.14.7, Linux, lane revision `e3ef1719c123ab4fb83ed94e033961dd61a2e8c7`
(`e3ef171`, the round-11 claims commit). `TMPDIR=$PWD/.scratch` before every scratch-writing
command. All runs happen in an **isolated mirror** (`.scratch/d13/repo`, built by the harness:
tool + reader gate + packet + all 15 components), so no lane file is reachable by a test —
including `--emit`, which the mirror redirects into scratch. Lane artifact digests were
re-read after the matrix; the only change during the window is the sibling re-pin of the
projection (row 3), which no run in this shard reads.

## 1. Method

Harness `.scratch/d13/harness.py` (case matrix) and `.scratch/d13/modes.py` (CLI modes);
results `.scratch/d13/results.json` and `.scratch/d13/modes.json`; cases in
`.scratch/d13/cases/*.yml` (31 files, the durable reproduction recipe).

- Every case is **one mutation** of a byte copy of the live packet, applied by anchor
  replacement (the harness asserts each anchor occurs exactly once; an unapplyable mutation
  aborts the run rather than testing something else).
- Every case runs **twice** through the real CLI
  (`python3 tools/d2-typed-labels.py --packet <case>`, cwd = mirror) and is recorded as
  repeat-stable only when exit code, stdout and stderr are byte-identical across runs.
- Recorded per case: exit code, first stdout line, first stderr line, a
  `Traceback (most recent call last)` flag, and the stability verdict. Streams matter here:
  loader/validation refusals print `FINDING D2L-DATA: [fail] …` on **stdout** (the report);
  `main()`'s exception path prints `d2-typed-labels error: …` on **stderr**; a crash prints
  its traceback on stderr and nothing on stdout.
- Group A mutates the packet **structure** (loader class); Group B appends a
  `typed_labels:` block and mutates **one field per case** inside it (the typed channel the
  round-11 wiring will route — `tools/d2-typed-labels.py:607-613`: "Explicit `typed_labels`
  entries pass through unchanged; they are the channel the malformed controls and
  hand-authored labels use"). The appended list is indented two spaces under the key to
  match the strict loader's subset — an earlier revision of this harness appended it at
  column 0 and every case died at the loader (`unconsumed content`) instead of reaching the
  channel; that defective harness output is not cited anywhere in this report.
- Control: `A11` (CRLF substituted throughout) and `B0` (a well-formed typed entry) must not
  turn exit 2; the **pristine** packet is the baseline for the silently-dropped probes
  (byte-identical stdout = the mutation had no observable effect).

## 2. Group A — loader-level malformation, 11 cases

Mutation of the live packet, one change each; command as in §1; stamps
2026-10-17T22:03–22:07Z.

| case | mutation | exit | first diagnostic (stdout; stderr empty) | stable | traceback |
|---|---|---:|---|---|---|
| A1 | tab indentation on the `canon:` line | 2 | `FINDING D2L-DATA: [fail] … — tab indentation is refused` | yes | no |
| A2 | `onset_clusters: false` → `[false` | 2 | `… — flow collection is not closed on its line` | yes | no |
| A3 | trailing `name:` line duplicating the top-level key | 2 | `… — duplicate key 'name'` | yes | no |
| A4 | `name:` value starts with anchor `&a` | 2 | `… — anchor, alias or tag is outside the accepted subset` | yes | no |
| A5 | appended `---` document marker | 2 | `… — document markers are not part of the subset` | yes | no |
| A6 | empty file | 2 | `… — no content lines` | yes | no |
| A7 | 70-deep flow nesting in `tones:` | 2 | `… — flow nesting deeper than 64` | yes | no |
| A8 | trailing `0xFF` byte (invalid UTF-8) | 2 | `… — 'utf-8' codec can't decode byte 0xff in position 156074` | yes | no |
| A9 | packet cut at 40% mid-content | 2 | `… — unterminated quote` | yes | no |
| A10 | root replaced by a scalar | 2 | `… — content 'just a scalar' is not a mapping line` | yes | no |
| A11 | CRLF substituted throughout (**control**) | 1 | `FINDING D2L-FORM-UNRESOLVED: [hold] GAR-01 — …` | yes | no |

10/10 malformation classes exit 2 with a distinct, repeat-stable diagnostic and no
traceback; the diagnostic is the *first line only* — the report continues with the full
finding list, and the exit code is what the claim keys on. A11 confirms CRLF is accepted
(the loader normalizes line endings), so that class is not malformed by this tool's
contract.

## 3. Group B — malformed `typed_labels` entries, 18 cases

Each case appends a `typed_labels:` list to the live packet and mutates exactly one field
(or adds one entry). `B0`, `B8`, `B10` and the probes deviate by design and are marked.

| case | injected defect | exit | diagnostic naming the defect | stable | tb |
|---|---|---:|---|---|---|
| B0 | well-formed entry, `status: absent` (**control**) | 1 | adds one expected `D2L-FORM-UNRESOLVED` hold (`TL-01`) | yes | no |
| **B1** | entry with **no `kind`** | **1** | **none — traceback (F1)** | yes | **yes** |
| B2 | `kind: nonsense` | 2 | `TL-03 — kind 'nonsense' is not one of (…)` | yes | no |
| B3 | `status: supplied` with no text | 2 | `TL-04 — status supplied requires text` | yes | no |
| B4 | `text: mirken`, `representation: null` | 2 | `TL-05 — representation 'null' is not one of (…)` | yes | no |
| B5 | costume-owned label with no `label_id` | 2 | `TL-06 — costume label carries no label_id for its form slot` | yes | no |
| B6 | two `status: supplied` sound forms on one `owner+label_id` | 2 | `TL-07 — two supplied sound forms on one record (05-lexicon LEX-DUP): identity collision` | yes | no |
| B7 | two entries, same `id` | 2 | `TL-09 — duplicate label record id` | yes | no |
| B8 | `era_ids: [E9]` | **1** | `TL-10 — era id 'E9' is not a contract tag …` (**`[fail]` finding, exit 1** — F5) | yes | no |
| B9 | bare-string entry | 1 | **none — dropped silently (F2)** | yes | no |
| B10 | `compare_only: true` | **1** | `TL-11 — compare_only is not a licensed exemption …` (**fail, exit 1** — F5) | yes | no |
| B11 | `representation: ipa-guess` | 2 | `TL-12 — representation 'ipa-guess' is not one of (…)` | yes | no |
| B12 | all four L3 fields null, no `issues` reason | 2 | `TL-13 — null representation carries no field-specific reason in issues` | yes | no |
| B13 | id `'TL 14/_'` | 2 | `TL 14/_ — id 'TL 14/_' is not a stable record id` | yes | no |
| B14 | duplicate key `id:` twice in one entry | 2* | `TL-16 — null representation …` — **the duplicate key itself is not diagnosed (F3)**; exit 2 only because the survivor entry trips L3 | yes | no |
| B15 | list of bare integers | 1 | **none — dropped silently (F2)** | yes | no |
| B16 | `typed_labels:` is a mapping, not a list | 1 | **none — dropped silently (F2)** | yes | no |
| B17 | `status: supplied`, `text: null` | 1 | **none — "null" is accepted as a supplied native form (F4)** | yes | no |

\* B14's exit 2 comes from the L3 null rule, not from the duplicate key.

Reading of the table: **9 of 18** cases are the clean target behavior (one malformed field
→ one named `D2L-DATA` diagnostic → exit 2, stable, no traceback). Five findings cover the
rest; the crash (B1) is the one that breaks the assignment's requirement outright.

## 3.1 Group C — declared sound kind, no bytes, 2 cases

The class `reports/round-11/depth/design.md` §8.3 carries forward from round 10 (shard-05
N2): a `native-form` whose `status: to-verify` declares *no bytes*. Design-spec R5 and the
routing table (§2.3 row 3) require it **off-channel and held** — "silent pass forbidden".

| case | shape | exit | observed | stable |
|---|---|---:|---|---|
| C1 | `native-form`, `to-verify`, no bytes, **no `issues` block** | 2 | `TL-19 — null representation carries no field-specific reason in issues` — caught only by the L3 reason rule, not by any R5 check | yes |
| C2 | same, **with** the four field reasons | **1** | **no finding naming `TL-20`**; stats stay `{fail: 0, hold: 15, note: 1, labels: 59}` | yes |

C2 is F7: at the projector boundary this class is silent. The hold the design requires must
therefore come from the adapter (design.md §8.3 leaves exactly that decision open).

## 4. CLI-mode boundary, 14 probes

Same mirror; `.scratch/d13/modes.py`; each probe run twice (all stable). `--emit` target
`.scratch/d13/emit-out.yml`, removed before each probe.

| probe | exit | first line | emit wrote? | tb |
|---|---:|---|---|---|
| A2 loader-malformed `--json` | 2 | `{"exit_code": 2, "findings": [{"code": "P-UNTERMINATED-FLOW", …` | — | no |
| A2 loader-malformed `--emit` | 2 | err: `could-not-evaluate: nothing to emit` | **no** | no |
| A2 loader-malformed `--check` | 2 | err: `could-not-evaluate: [{…}]` | — | no |
| **B1 missing-kind `--json`** | **1** | err: traceback | — | **yes** |
| **B1 missing-kind report** | **1** | (stdout empty) err: traceback | — | **yes** |
| **B1 missing-kind `--emit`** | **1** | err: traceback | **no** | **yes** |
| B5 validation-fail `--json` | 2 | `{"exit_code": 2, "findings": [{"code": "D2L-DATA", …` | — | no |
| B5 validation-fail `--emit` | 2 | `Wrote …emit-out.yml` | **yes (F6)** | no |
| B5 validation-fail `--check` | 1 | err: `…typed-labels.d2.yml differs …` | — | no |
| B8 scope-fail `--json` | 1 | `{"exit_code": 1, …` | — | no |
| absent path `--json` | 2 | `{"exit_code": 2, "findings": [{"code": "P-IO", "detail": "[Errno 2] No such file…` | — | no |
| absent path `--emit` | 2 | err: `could-not-evaluate: nothing to emit` | **no** | no |
| directory target `--json` | 2 | `{"exit_code": 2, … "[Errno 21] Is a directory…` | — | no |
| directory target (report) | 2 | `FINDING D2L-DATA: [fail] …/[Errno 21] Is a directory…` | — | no |

Every mode is repeat-stable. `--check` semantics stay as round 8 documented (byte-identity
only: B5's `--check` exits 1 on drift even though the *packet* was malformed — the `--json`
run of the same packet exits 2; a consumer must read the mode's question, not one global
code).

## 5. Findings (reported, not absorbed)

- **F1 — a typed entry with no `kind` crashes with a traceback (B1).** `project_labels`
  passes explicit `typed_labels` entries through unchanged
  (`tools/d2-typed-labels.py:612-617`); `validate_labels` records the missing field as a
  `D2L-DATA` finding and `continue`s (`:742-744`), but `run_pipeline` then computes the
  coverage counters with hard indexing —
  `kind: sum(1 for label in parse_result["labels"] if label["kind"] == kind)`
  (`tools/d2-typed-labels.py:2497`) — and raises `KeyError: 'kind'`. `main()` catches
  `Malformed, PacketSyntaxError, ReconciliationError, ValueError, OSError` (`:2908`) but not
  `KeyError`, so the process exits **1** with a traceback and **no diagnostic line**, in
  every mode (report/`--json`/`--emit`). This is the assignment's core requirement failing:
  a malformed typed packet does **not** get a stable exit-2 diagnostic. The crash is
  deterministic (identical traceback on repeat runs) and reproducible from the lane tool
  unchanged (`sha256 0da0015f…`); fix belongs to the D03–D08 implementation shards or a
  round-8-tool correction — not absorbed here.
- **F2 — malformed `typed_labels` shapes are dropped with no diagnostic (B9/B15/B16).**
  A bare-string entry, a list of integers, and a mapping-valued `typed_labels` all produce
  output **byte-identical to the pristine packet** (verified by `diff`): `project_labels`
  keeps only `isinstance(entry, dict)` entries (`:612-613`) and iterates
  `packet.get("typed_labels") or []`, so a mapping yields its keys (strings, dropped) and a
  scalar list yields non-dicts (dropped). A packet whose typed channel was mis-written is
  indistinguishable from one that carries no typed labels: no finding, no exit-2, exit 1
  from unrelated pre-existing holds. Whether the wiring's adapter coverage check (design.md
  §2.2: "no routing row names a record the projector did not type") catches this upstream is
  `to-verify`; at the projector boundary it is silent.
- **F3 — duplicate keys inside a sequence-item mapping are accepted, last one wins (B14).**
  The strict loader refuses a repeated key in a *mapping* block (`P-DUPLICATE-KEY`, case A3;
  `tools/d2-typed-labels.py:342`) and in a flow mapping (`:250`), but the sequence-item path
  assigns `entry[skey] = …` with no duplicate check (`:316`, `:321`). `- id: TL-15` followed
  by `  id: TL-16` loads as `TL-16` with no diagnostic. Same asymmetry would apply to any
  sequence of records a packet carries (the live packet's `lexicon`, `costumes`, … lists are
  all sequences of mappings), so this is a loader-class gap, not typed-channel-specific.
- **F4 — YAML `null` is read as the four-character string `"null"` (B17, B4).** `parse_scalar`
  has no null token: unquoted `null` falls through every case to the final `return s`
  (`tools/d2-typed-labels.py:262`; the token sets `_RAW_TRUE`/`_RAW_BOOL` cover only boolean
  words). Consequence in the typed channel: an entry with `status: supplied` and `text: null`
  is projected as `kind: native-form`, `status: supplied`, **`text: "null"`** (read from the
  emitted projection, `.scratch/d13/b17-proj.yml`), passes the L3 "supplied requires text"
  check and the inventory check (`n,u,l,l` are all declared), and the run exits 1 with **no
  finding on the entry** — an author's "no form" reads as a supplied native form. The same
  token explains B4's diagnostic naming `representation 'null'` (string) rather than a
  missing field. The live packet itself carries `maps_to: null` twice and `- null` items
  (a D1-class concern for the byte-frozen round-3 artifacts; not touched here). Recommended
  disposition: either teach the loader `null`/`~` → `None`, or refuse the token — leaving it
  as a string is the one option that cannot be detected by a reader.
- **F5 — `[fail]`-severity scope findings exit 1, not 2 (B8/B10).** An out-of-contract era
  id and `compare_only: true` both emit `D2L-SCOPE: [fail]` lines (kept, never laundered)
  but `run_pipeline`'s exit rule is `2 if any D2L-DATA else (1 if hard else 0)`
  (`tools/d2-typed-labels.py:2493`). This is consistent with the round-8 spec's exit
  table ("2 could-not-evaluate: malformed input"; a scope violation is decidable) — recorded
  so "stable exit-2 diagnostics" in the claim's wording is read against what actually exits
  2: **malformed/schema** classes, not every fail-class finding. A consumer keying on exit 2
  alone will not see B8/B10 as malformed.
- **F6 — `--emit` writes and exits 2 on a validation-level malformed packet (B5).** For a
  packet that loads but fails validation, `--emit` writes the full projection (containing
  the offending label) and returns the report exit 2; for a loader-level malformation it
  refuses with `could-not-evaluate: nothing to emit` (A2). Both are stable and documented
  behavior of `main()` (`:2900-2906`); flagged because a pipeline step that treats
  "exit 2" as "nothing was produced" will misread the first case — the artifact *was*
  written.
- **F7 — a declared sound kind with no bytes is silent once the L3 reasons are present
  (C2).** A `native-form` entry with `status: to-verify` and no `text`/`label_id`:
  without an `issues` block it exits 2, but only via the L3 null-reason rule (C1); **with**
  the four field reasons it emits **no finding at all** (C2: stdout carries no `TL-20` line,
  stats stay `{fail: 0, hold: 15, note: 1, labels: 59}`, exit 1). The wiring design already
  names this class: `reports/round-11/depth/design.md` §8.3 ("`to-verify` hold for
  declared-sound-kind-without-bytes (carried defect)" — round-10 shard-05 N2) requires it
  off-channel **and** held, and design-spec R5 forbids the silent pass; the routing table
  (§2.3, row 3) says "silent pass forbidden". At the projector boundary measured here the
  class is silent, so the adapter must inject the hold itself and this stands as a reported
  deviation against the projector (not patched here).

Stability verdict for the whole matrix: **45/45 case-and-probe pairs repeat-stable**
(31 cases + 14 probes, each run twice = 90 subprocess runs; every pair byte-identical on
exit, stdout and stderr, including the crashing B1). "Stable" is satisfied throughout; the
failures above are about *what* is emitted, not about flakiness.

## 6. Post-wiring boundary — measured at `tools/typed-gate-flow.py` `5758e315…`

The round-11 wiring landed during this shard's window as **`tools/typed-gate-flow.py`** —
one file consolidating the design's adapter and gate (`design.md` §7 named
`tools/assemble-d2-typed.py` + `tools/gates/typed-pipeline-gate.py`; the rename/merge is an
observation for the D20 wiring-vs-design reviewer, not a verdict here). Boundary probe
harness `.scratch/d13/wired-boundary.py`; mirror `.scratch/d13/wired/repo` (the flow's own
selftest tree set: the tool + `d2-typed-labels.py` + `assemble-d2.py`, the five gates, all
of `examples/culture-d2`); results `.scratch/d13/wired/results.json`; each probe (W1–W14 in
the harness, W15/W16 as direct CLI probes) run twice and byte-compared.

Revision record (the tool was live while probed): `ae55e6fa…` 22:15Z → `5afa6295…` 22:16Z
(probe run red: baseline exit 1, selftest FAIL) → `a7e1224f…` 22:17–22:18Z → **`5758e315…`**
22:18:32–22:20:16Z, verified **identical before and after** the cited probe run
(`results.json` `tool_sha256_before_run`/`after`), with baseline exit 0, `--check` exit 0 and
`--selftest` exit 0; re-sampled unchanged at 22:21:56Z and 22:23:15Z. All W-verdicts below
bind `5758e315…` only.

| # | probe (malformed input) | exit | first diagnostic | stable | tb |
|---|---|---:|---|---|---|
| W1 | baseline e2e (control) | 0 | report banner, `findings: 16 (hold 15, note 1)` | yes | no |
| W2 | `--packet` malformed YAML (§2 A2 case) | 2 | err: `could-not-evaluate: packet could not be loaded: [{'code': 'P-UNTERMINATED-FLOW', …` | yes | no |
| **W3** | `--packet` base packet whose `typed_labels` entry lacks `kind` (F1 case) | **1** | **err: traceback — `evaluate` (`typed-gate-flow.py:316`) → `KeyError: 'kind'` at `d2-typed-labels.py:2497` (F1 propagates)** | yes | **yes** |
| **W4** | `--typed-override` absent path | **1** | **err: traceback — `FileNotFoundError` at `typed-gate-flow.py:335` (`Path(typed_override).read_bytes()`)** | yes | **yes** |
| W5 | `--typed-override` garbage YAML | 2 | err: `could-not-evaluate: naming-collision-gate.py: exit 2: …` | yes | no |
| W6 | `--expected` garbage JSON | 1 | check `FAIL expected-parse — …: not valid JSON …`; `5/6 checks passed` | yes | no |
| W7 | `--expected` absent path | 1 | check `FAIL expected-present — missing: …` | yes | no |
| W8 | `--typed-packet` absent path | 1 | checks `FAIL typed-packet-pinned`, `FAIL expected-file-current` | yes | no |
| W9 | `--packet` directory | 2 | err: `could-not-evaluate: … [{'code': 'P-IO', 'line': 0, 'detail': "[Errno 21] Is a directory…` | yes | no |
| W10 | `--packet` non-UTF-8 | 2 | err: `could-not-evaluate: … 'P-ENCODING' …` | yes | no |
| W11 | `--json` over the W2 packet | 2 | err: same as W2 | yes | no |
| W12 | `--check` over the W2 packet | 2 | err: same as W2 | yes | no |
| W13 | `--check` baseline | 0 | `typed gate artifacts: byte-identical deterministic derivation` | yes | no |
| W14 | `--selftest` | 0 | `ok  positive: e2e exit 0` (all controls) | yes | no |
| W15 | `--packet` malformed YAML + `--emit` | 2 | err: same as W2; **no artifact written** | yes | no |
| W16 | `--packet` malformed YAML + `--freeze DIR` | 2 | err: same as W2; **no freeze directory written** | yes | no |

Wired-boundary findings (same numbering family as §5, reported not absorbed):

- **W-F1 — F1 propagates through the wired CLI (W3).** A base packet carrying a typed entry
  with no `kind` crashes the whole flow: `evaluate` calls the round-8 `run_pipeline`
  (`typed-gate-flow.py:316`) without catching `KeyError`, so the process exits 1 with a
  traceback and no report — the exact failure the wiring's contract puts in the exit-2 class
  (design.md `:199-203`, "gate traceback"). Either the projector's `:2497` must be fixed at
  the source or the flow must guard the call; no file in this shard fixes it.
- **W-F2 — `--typed-override <absent>` crashes with `FileNotFoundError` (W4)** at
  `typed-gate-flow.py:335`; an absent override path is a missing input and belongs in the
  exit-2 class by the tool's own docstring ("2 = could-not-evaluate (missing or malformed
  input, no traceback)").
- **W-F3 — missing/garbage *expected set* and missing *typed packet* exit 1, not 2
  (W6–W8).** The flow reports them as failed checks (`expected-parse`,
  `expected-present`, `typed-packet-pinned`) with the defect named, never silently — a
  deliberate split (`_parse_expected`: "a present-but-unparseable file is a loud check
  failure, never a silent pass") but a different code class from the docstring's "missing
  input → 2". A consumer keying exit 2 as "malformed input" will misread these three.
- W5, W9–W12 and W15/W16 confirm the intended behavior across modes: malformed *typed*
  content that reaches the gates, bad paths and bad encodings all refuse with exit 2, a
  named diagnostic and no traceback, repeat-stable — and the write modes (`--emit`,
  `--freeze`) refuse **before writing anything**.

Everything above is a snapshot: the tool was mid-iteration until 22:18Z (its `--check` was
red and its own selftest failing at `5afa6295…`), so a later revision must be re-probed with
the same harness before any verdict is reused.

## 7. Limits and to-verify

1. **Revision-bound.** All §2–§4 verdicts bind `tools/d2-typed-labels.py`
   `0da0015f…` and packet `e0f21509…` only; all §6 verdicts bind
   `tools/typed-gate-flow.py` `5758e315…` only (the tool moved four times in 12 minutes
   while probed — `ae55e6fa…` → `5afa6295…` → `a7e1224f…` → `5758e315…`). A later revision
   of either subject invalidates its section; re-run the harnesses first.
2. **The matrix is single-mutation synthetic.** Cases are constructed, not discovered:
   `to-verify` whether real hand-authored typed packets (e.g. the D3 path's inputs) hit
   classes this matrix missed.
3. **F1 / W-F1 fix status** is `to-verify`: the crash is a round-8-tool defect
   (`d2-typed-labels.py:2497`) that the wired CLI (`typed-gate-flow.py:316`) does not
   guard; no file in this shard fixes it, and the fix belongs to the D03–D08 shards or a
   round-8-tool correction.
4. **F2's adapter-level catch** is `to-verify` — at the flow's boundary (W-class) the
   silently-dropped `typed_labels` shapes of §3 were not re-probed directly; the flow's
   `no-untyped-records` check (`typed-gate-flow.py` `evaluate`) is the candidate guard.
5. **W-F3's code split is a design question above this shard:** whether a missing/garbage
   expected set should stay exit 1 (loud check failure) while the docstring says "missing
   input → 2" is the orchestrator's call; both behaviors are stable and named.
6. **Out of province (report, never absorb):** none. This shard touched no canon,
   no real-world rights and no game-mechanics surface; the D2 material is design-drill
   evidence (`examples/culture-d2/ASSEMBLY.md`).
7. **Scratch:** all under `.scratch/d13/` (two mirrors, 31 case files, three harnesses,
   results JSON, poll log); remove-safe, nothing outside the lane written, no filed
   round-8/9/10 byte touched.

## Receipts

```sh
# 2026-10-17T22:03–22:07Z (matrix), 22:11Z (C group), 22:18–22:20Z (wired), TMPDIR=$PWD/.scratch
python3 .scratch/d13/harness.py            # 31 cases ×2 runs → .scratch/d13/results.json
python3 .scratch/d13/modes.py              # 14 probes ×2 runs → .scratch/d13/modes.json
python3 .scratch/d13/wired-boundary.py     # 14 wired probes ×2 runs → .scratch/d13/wired/results.json
grep "Traceback" .scratch/d13/results.json | wc -l        # 1 (B1 only)
diff <(python3 .scratch/d13/repo/tools/d2-typed-labels.py --packet .scratch/d13/cases/B16-mapping-typed-labels.yml) \
     <(python3 .scratch/d13/repo/tools/d2-typed-labels.py --packet .scratch/d13/repo/examples/culture-d2/packet.d2.yml)
                                           # empty → B9/B15/B16 identical to pristine
python3 .scratch/d13/repo/tools/d2-typed-labels.py --packet .scratch/d13/cases/B1-missing-kind.yml
                                           # exit 1; KeyError: 'kind' at tools/d2-typed-labels.py:2497
python3 .scratch/d13/repo/tools/d2-typed-labels.py --packet .scratch/d13/cases/B17-null-text-as-form.yml --emit .scratch/d13/b17-proj.yml
                                           # TL-18 text: "null", kind native-form, status supplied — no finding
cd .scratch/d13/wired/repo && python3 tools/typed-gate-flow.py --packet ../cases/base-b1-missing-kind.yml
                                           # exit 1; traceback: typed-gate-flow.py:316 → KeyError (W3)
cd .scratch/d13/wired/repo && python3 tools/typed-gate-flow.py --typed-override ../cases/absent.yml
                                           # exit 1; traceback: typed-gate-flow.py:335 FileNotFoundError (W4)
cd .scratch/d13/wired/repo && python3 tools/typed-gate-flow.py --packet ../cases/base-a2-unterminated.yml --emit
                                           # exit 2; no artifact written (W15)
cd .scratch/d13/wired/repo && python3 tools/typed-gate-flow.py --packet ../cases/base-a2-unterminated.yml --freeze ../cases/freeze-out
                                           # exit 2; no freeze directory written (W16)
sha256sum tools/d2-typed-labels.py tools/typed-gate-flow.py \
          examples/culture-d2/packet.d2.yml examples/culture-d2/typed-labels.d2.yml
```

FILES: reports/round-11/depth/test-boundary.md | SUMMARY: D13 boundary complete — projector matrix (31 single-mutation cases + 14 CLI-mode probes, 45/45 pairs repeat-stable) over `tools/d2-typed-labels.py 0da0015f…`: 10/10 loader classes and 9/18 typed-channel classes give named exit-2 diagnostics, but a typed entry missing `kind` crashes with `KeyError` (traceback, exit 1, all modes — F1), non-dict/`typed_labels`-as-mapping shapes are dropped silently (F2), duplicate keys inside sequence items are last-wins (F3), `null` reads as the string "null" so `text: null` passes as a supplied native form (F4), `[fail]`-severity scope findings exit 1 not 2 (F5), `--emit` writes-and-exits-2 on validation-level malformation (F6), and a declared sound kind with no bytes is silent (F7); the wired CLI `tools/typed-gate-flow.py 5758e315…` (§6, 16 probes, green baseline/`--check`/`--selftest`) carries F1 through as a whole-flow traceback (W-F1), adds a `--typed-override <absent>` `FileNotFoundError` crash (W-F2), and exits 1 rather than 2 for a missing/garbage expected set or missing typed packet (W-F3).
