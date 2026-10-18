# R18-O01 — Design: the declared-assembler identity leg + the re-pin cascade

- round: 18 (operator loop 2 of 3, build round 2 of 4; 64 workers on
  `opencode-go-2/deepseek-v4.1-flash`) · shard: **O01** (generalization design ×2,
  claim O `gate-generalization`). This file is the design half; the adversarial
  review is `reports/round-18/gate/design-review.md` (R18-O02).
- assignment (verbatim): "O R18-O01..O02 (generalization design x2): read
  tools/gates/typed-pipeline-gate.py L1 + reports/round-17 ruling; design the
  declared-assembler mechanism (packet-declared pin preferred; flag fallback);
  specify the re-pin cascade exactly (which manifests/baselines pin which shas);
  reports/round-18/gate/{design,design-review}.md."
- date: 2026-10-18. Reference revision HEAD `c66ac3c951b346a2a56f9386e3324b4f5fe33902`
  ("round-18: declare claims O/D/C", 2026-10-18 07:17:35 -0300; `git log --oneline -2`).
  Baseline `3dd3754207032cb81f5fb3e202fe85cf79211339` (round-17 close: "C/O verified;
  D rejected (typed gate D2-bound …)"). Stamps local (-03:00) and UTC where stated;
  measurements 10:19–10:33Z.
- canon: NON-CANON engineering design. No culture content, no canon record, no
  handoff, no real-world clearance or rights statement.
- writes: **this file only** plus gitignored scratch under
  `.scratch/r18-gate-design/` (`export TMPDIR=$PWD/.scratch/r18-gate-design` before
  every scratch-writing command; the frozen replays below use `/var/tmp/...`
  because `tools/replay-frozen.py` refuses an in-repo mirror root by design — its
  own docstring and `tools/gates/frozen/round-11/README.md`). No tool, packet,
  projection, baseline, manifest or earlier-round byte was written by this seat.
  No commit, no push.
- **status: design complete and implementable; the gate generalization itself is
  the implementer seats' write (O03+ and the D4 adapter owner). This seat does not
  touch `tools/gates/typed-pipeline-gate.py`.**

---

## 0. The design in one paragraph

The round-17 rejection measured one blocking leg: `tools/gates/typed-pipeline-gate.py`
L1 checks the graded packet against **`tools/assemble-d2.py`'s deterministic build,
hard-coded**, so a D4 packet cannot reach the typed pipeline (receipts §1.3). The
generalization replaces that hard binding with a **resolved, declared assembler
identity**: the packet's own `assembly.generator` + `assembly.assembler_sha256`
pair is read first (the delivered `examples/culture-d4/packet.d4.yml:2344-2347`
already carries exactly this pair — `tools/assemble-culture-d4.py` @
`943f487b…`), with an `--assembler PATH [--assembler-sha256 HEX]` flag as the
fallback for packets that declare no digest. The resolution is fail-closed:
path hygiene, pin equality against the live file, a required module-level
`assemble()` interface, and a conflict refusal when declaration and flag
disagree. **When the resolution is the D2 default (no digest-bearing declaration,
no flag) the gate takes its existing code path verbatim**, so D2 stdout bytes,
exit codes and `--json` bytes are unchanged; the frozen round-11 row replays
green under a **new re-pin manifest** (a new file; the round-11 bytes are never
edited). Because `tools/replay-frozen.py` launches `[python3, <gate>, <input>]`
and never reads the `command` column, a flag-only D4 path could not be frozen;
the design therefore adds one **flagless resolution channel**: a new, sha-pinned
data file `tools/gates/typed-pipelines.json` whose profile is matched on the
packet's declared generator and names the D4 projection, adapter and expected
set. The cascade of every pin that moves — and of every pin that must be proven
not to move — is specified in §5.

---

## 1. The measured before-state (all receipts dated 2026-10-18)

### 1.1 Subject shas (command: `sha256sum <paths>`, 10:22–10:31Z)

| path | sha256 (as-read) | role |
|---|---|---|
| `tools/gates/typed-pipeline-gate.py` | `d102fd1dd1bae3cc4c9d0ea33844b2f706a2098707938c82c75ce9fb6368e27d` | the gate (round-11 frozen revision) |
| `tools/assemble-d2-typed.py` | `c7e5a7493601d3312f2eb55185ac4d081139cdaa0e11f67dd69f67250b037071` | D2 typed adapter |
| `tools/d2-typed-labels.py` | `0da0015f700345c938184cb45ca07178c33e98f798c3c09729007487fb89c802` | projector (also the D4 projection's pinned projector) |
| `tools/assemble-d2.py` | `8ea6bdde9514ee966fe58cf219d4d0228ecc3b041e30549c68073cc822c8655d` | D2 serializer/assembler |
| `tools/assemble-culture-d4.py` | `943f487ba991d45d369eb8fb6e9bb686046df165424d101cfa2670f79bb844b2` | D4 assembler (declared by the D4 packet) |
| `examples/culture-d2/packet.d2.yml` | `e0f21509e14ac03ed5747e6bbbb48183cbe56d6b61afff8c8475e4a50137b643` | D2 gate-facing packet |
| `examples/culture-d2/packet.d2.typed.yml` | `1b5010b7f449ec78755e9a8b0efea62c705af7ec5c592ceda6cf2c072dfac8a3` | D2 typed packet (pins adapter `c7e5a749…`) |
| `examples/culture-d2/expected-holds.json` | `a5dc26d5b495a90e05ce42d4d8b6d08f047359c377e458f9190b1d310d6dde3a` | D2 frozen hold set (pins projector `0da0015f…`) |
| `examples/culture-d4/packet.d4.yml` | `e7ecd2045ef0e5f9823ce0a067d21b8221b2ceb5e8f5799736981a1c88fa50d3` | D4 gate-facing packet (declares its assembler) |
| `examples/culture-d4/typed-labels.d4.yml` | `a59990bbfe5a8992ffa6e67e9b3e43e7ff477df9fc754e5af92b6f40d23fe11d` | D4 projection (pins packet `e7ecd204…`) |
| `examples/culture-d4/expected-holds.json` | `09490a2756d123ebbc2023be89fc01c95ec2f8cc7e6df42ecc5b8cd438058e98` | D4 expected set (15 holds + 1 note; pins packet, projection, projector) |
| `tools/gates/frozen/round-11/MANIFEST.tsv` | `aad230bfdcc1bfe4cc137339b47daf0154208b6c69225e0c0a4505ce52532063` | round-11 frozen generation (11 rows) |
| `tools/gates/frozen/round-11/typed-pipeline/run-receipt.json` | `c49ebc9e71ce870af621604bb0e00886b45ad8f4028777f202ec845ede6cc902` | round-11 row-1 receipt |
| `reports/round-16/handoff/expected-v2-07.json` | `dc75c5d7e347987e81efe6f6fe17314e8f6a2ce26a12a1ca7ec3567a21dcaad1` | handoff baseline (**7** `tools/` pins) |
| `reports/round-9/baselines/handoff-packet-check/packet.md` | `0d8d660bf9797d1c15da477f96ded75553a8d2ca7f04f75aa86a8a65e28fd2fc` | round-9 baseline; `A-SERIALIZER` pin (`tools/assemble-d2.py 8ea6bdde…`, `:68`) |

### 1.2 The D2 default path is green and byte-pinned (before)

- `python3 tools/gates/typed-pipeline-gate.py` → exit 0, 35 stdout lines,
  stdout sha256 `15cdfbda73cd56cb6107d2fdbee533dbce47e9381e2082085ca1f0c45f2e695b`
  (run twice, `cmp` identical, this seat, 10:2xZ). Corroborated byte-for-byte by
  R18-O11 receipt t0 (`reports/round-18/gate/tests-1.md`; `.scratch/r18-o11/receipt-t0.json`:
  same sha from tree and mirrors) and R18-D14 (`reports/round-18/d4/interop-1.md`).
- `python3 tools/gates/typed-pipeline-gate.py --json` → exit 0, stdout sha256
  `19765ddf2c36a7db5d71bd262079d6164b24f6222d9df83d0cefdeaeb8f47e62`
  (recorded in `reports/round-11/validation.json`; re-measured byte-identical by
  R18-D14; this seat re-ran the non-JSON path only).
- Frozen row 1 path: `python3 tools/gates/typed-pipeline-gate.py
  tools/gates/frozen/round-11/typed-pipeline/packet.d2.typed.yml` → exit 0,
  stdout byte-identical to `tools/gates/frozen/round-11/typed-pipeline/run.log`
  (`9a69985aabdf3e9bf233653f7b31ce6f3bf5fd12858cfedf7e9ebca14ada4606`;
  R18-O11/R18-D14 receipts; this seat verified the same sha via the manifest pin).
- `python3 tools/check-gate-battery.py` → exit 0, summary `pass 7 / fail 0 /
  unevaluable 0` (this seat, 10:2xZ, `TMPDIR=$PWD/.scratch/r18-gate-design`).
- `python3 tools/check-craft-exercise.py --selftest` → exit 0, `10/10 tamper`,
  `18/18 CLI cases` (this seat, 10:2xZ).

### 1.3 The D4 refusal (the round-17 blocker, reproduced)

- `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml`
  → the gate L1 reports `FAIL L1-assembler_identity: packet bytes are not
  assemble-d2.py's deterministic assembly (e7ecd2045ef0 vs e0f21509e14a)`
  (receipt `.scratch/r18d/gate-d4.out`, read 10:24Z; the adapter-level twin,
  exit 2, is R18-D14/D17 receipt in `reports/round-18/d4/interop-1.md` §3 and
  `reports/round-18/gate/tests-2.md` receipt 1, 10:26–10:29Z).
- Round-17 ruling (verbatim, `LOG.md:3232-3236`): "the round-11
  typed-pipeline-gate's L1 assembler-identity leg pins assemble-d2 output and
  cannot consume a D4 packet … Generalization + re-pin cascade routed to round
  18." Round-17's own measurement of the leg as D2-bound:
  `reports/round-17/d4/typed-support-1.md:354` (F-D18-3) and
  `reports/round-17/d4/typed-run.md:96-171`.

### 1.4 Frozen replays today (green set, measured by this seat 10:2xZ)

| manifest | result | note |
|---|---|---|
| `tools/gates/frozen/round-11/MANIFEST.tsv` | **11/11 reproduced, exit 0** | the only green typed generation today |
| `reports/round-17/tests/frozen/MANIFEST.tsv` | **5/5 reproduced, exit 0** | five reader gates over the round-17 D4 snapshot |
| `tools/gates/frozen/round-3/MANIFEST.tsv` | exit 2 — **all 7 rows `gate_digest_mismatch`** (pre-existing) | superseded generation; every pinned gate was revised after round 3 |
| `tools/gates/frozen/round-4/` | no `MANIFEST.tsv` exists | `.out` files only |

Defining "frozen replays all green" therefore means: **nothing green today goes
red**, and the surfaces this change moves get a green replacement (§5, §7).
The round-3 red is a pre-existing class, recorded here, not repaired.

### 1.5 The declared pair exists on the D4 packet already

`examples/culture-d4/packet.d4.yml:2344-2347` (read 10:24Z):

```yaml
assembly:
  generator: "tools/assemble-culture-d4.py"
  assembler_sha256: "943f487ba991d45d369eb8fb6e9bb686046df165424d101cfa2670f79bb844b2"
  reader: "tools/gates/costume-era-consistency-gate.py"
  reader_sha256: "e6bffd7020c0b1168828902853320bbf37e903457c83dae5477820aeceec478f"
  ...
```

`sha256sum tools/assemble-culture-d4.py` = `943f487b…` (live, 10:22Z) — the
declaration is already self-consistent, so the packet-declared pin is preferred
and costs zero packet bytes. The D2 packet's analogue carries `generator:
"tools/assemble-d2.py"` with **no** `assembler_sha256` (`examples/culture-d2/packet.d2.yml:3319-3325`),
which is exactly the digest-less case that keeps the D2 default path default.

---

## 2. The D2-bound surface, named

- `tools/gates/typed-pipeline-gate.py:55-64` hard-codes `PACKET_DEFAULT`,
  `PROJECTION_DEFAULT`, `EXPECTED_HOLDS_PATH`, `ADAPTER`, `PROJECTOR`,
  `SERIALIZER`, five `GATE_NAMES`. `:594-605` (`main`) decides typed-vs-legacy
  by looking for `typed_channel` in the input.
- `tools/assemble-d2-typed.py:112-125` (`assembler_identity`) loads
  `SERIALIZER` and compares the packet bytes against `serializer["assemble"]()`
  with **no path argument**; its failure string is "packet bytes are not
  assemble-d2.py's deterministic assembly (… vs …)".
- The three other bindings the round-18 scope names
  (`reports/round-18/scope.md` §"O", item 1) are `PROJECTOR` (used inside the
  adapter), `PROJECTION_DEFAULT` and `EXPECTED_HOLDS_PATH`.

Both extant assemblers expose the uniform build interface this design relies on:
`tools/assemble-d2.py:93 def assemble()` and
`tools/assemble-culture-d4.py:396 def assemble()` — module-level, no arguments,
returns the packet bytes (read 10:21Z; the D4 docstring says "The deterministic
build path; returns the packet bytes").

---

## 3. The declared-assembler mechanism (normative)

### 3.1 Declaration keys

| key | location | meaning |
|---|---|---|
| `assembly.generator` | packet root | repo-relative path of the assembler that built this packet |
| `assembly.assembler_sha256` | packet root | pin: sha256 of that assembler file's bytes |

No new packet key is invented; both key names are as delivered on the D4 packet.
A packet with no `assembly` block at all keeps today's behavior (default).

### 3.2 Resolution algorithm

Inputs: the packet document, `--assembler` (F, optional path),
`--assembler-sha256` (S, optional hex). Constants: `DEFAULT_ASSEMBLER =
tools/assemble-d2.py`.

1. **Read** `G = assembly.generator` (string or absent), `D =
   assembly.assembler_sha256` (string or absent). A packet that fails to parse in
   this prescan is **not** an error here: the gate delegates to the legacy code
   path so the existing adapter produces today's canonical diagnostic (byte
   identity, §3.4).
2. **Conflict check.** If `G` and `F` are both present and do not name the same
   file → refuse, exit 2, `DECL-ASSEMBLER-CONFLICT`. If `D` and `S` are both
   present and differ → refuse, exit 2, `DECL-ASSEMBLER-CONFLICT`. If `S` is
   present while neither `F` nor `G` is → refuse, exit 2,
   `DECL-ASSEMBLER-CONFLICT` (a pin without an assembler is incoherent; supply
   `--assembler` or fix the packet).
3. **Path.** `path = F or G or DEFAULT_ASSEMBLER`.
4. **Pin and mode.** `pin = D if D else S if S else sha256(live(path))`.
   Mode vocabulary, exhaustive:
   - `default` — no `D`, no `S`, no `F`, and (`G` absent or
     `G == DEFAULT_ASSEMBLER`). The next steps are skipped for this mode; the
     gate takes the existing code path (§3.3).
   - `declared` — `D` present (regardless of `F`/`S`, which must agree, step 2).
   - `flag-pinned` — `D` absent, `S` present.
   - `flag` — `D` and `S` absent, `F` present.
   - **missing pin** — `D` and `S` absent, and `G` names an assembler other
     than `DEFAULT_ASSEMBLER`: refuse, exit 2, `DECL-ASSEMBLER-PIN-MISSING`
     ("`<G>` is declared without `assembly.assembler_sha256`; supply
     `--assembler-sha256` or fix the packet"). A non-default declaration
     without its digest is unpinned; it is refused, never silently pinned to
     the live bytes. This is also why the review's F9 control correction
     matters: stripping only the digest must refuse here, not fall through.
5. **Path hygiene** (for `G` and `F`): repo-relative, no absolute path, no `..`
   component, no symlink component, must resolve inside the repo, must be a
   direct child of `tools/`, basename must match `assemble-[a-z0-9-]+\.py` →
   else refuse, exit 2, `DECL-ASSEMBLER-PATH`. (Same refusal grammar as
   `tools/replay-frozen.py:repo_path`; reused discipline, not its code.)
6. **Pin equality.** `sha256(live(path)) == pin` → else refuse, exit 2,
   `DECL-ASSEMBLER-PIN-MISMATCH` (a forged or stale declaration is
   could-not-evaluate, never a mismatch to be compared against).
7. **Interface.** Load the file read-only with the lane's `runpy.run_path`
   idiom (the gate already loads the adapter this way) and require a callable
   `assemble` → else refuse, exit 2, `DECL-ASSEMBLER-INTERFACE`. Re-hash the
   file after load; a change between hash and load → `DECL-ASSEMBLER-PIN-MISMATCH`
   (the check is a control against a mid-flight edit, not a sandbox claim).
8. **Identity.** `packet_bytes == assemble()` →
   check `L1-assembler_identity` **ok**, detail naming the resolved path; else
   the check fails → exit 1, detail: "packet bytes are not `<resolved path>`'s
   deterministic assembly (`<packet digest[:12]>` vs `<build digest[:12]>`)".
   The resolved path is named in **both** outcomes (the reviewable statement
   round-18 scope asks for).

### 3.3 Mode → code path

| mode | gate behavior |
|---|---|
| `default` | the **existing** code path verbatim: adapter `build()`; the adapter's own `assembler_identity` record is printed as today (`L1-assembler_identity`). No new line, no changed string. |
| `declared` / `flag-pinned` / `flag` | the gate runs §3.2 itself and prints exactly one `L1-assembler_identity` check naming the resolved assembler; the selected adapter's own identity record (if any) is **suppressed** for this run so the leg is reported once, by the resolver that actually checked. |

Precedence, stated as the claim states it: **packet-declared pin preferred;
flag fallback** — the flag is authoritative only where the declaration carries
no digest; where both exist they must agree or the run refuses.

### 3.4 Byte-identity guardrails for the D2 path

1. The D2 prescan result is `default` for every D2 input today (`§1.5`), and
   the default mode must not import, open or print anything new. The check:
   default stdout sha `15cdfbda…`, `--json` sha `19765ddf…`, frozen-row sha
   `9a69985a…`, all three re-measured after the change (§7).
2. A prescan parse failure on the default path must be swallowed (treated as
   "no declaration") so the adapter's canonical exit-2 diagnostic is the one
   the user sees — a new pre-parse error message on the D2 path would be a
   behavior change.
3. New resolution/declaration lines are printed **only** in non-default modes;
   the `--json` document grows a `resolved` block only in non-default modes.

### 3.5 Diagnostics vocabulary (stable strings)

`DECL-ASSEMBLER-CONFLICT`, `DECL-ASSEMBLER-PATH`,
`DECL-ASSEMBLER-PIN-MISMATCH`, `DECL-ASSEMBLER-PIN-MISSING`,
`DECL-ASSEMBLER-INTERFACE` — all exit 2 (could-not-evaluate), printed on stderr
like the gate's other refuse paths and never inside a `FINDING ` line. Exit 1 is
reserved for the identity failure (§3.2.8) and the existing L2/L3/L4 mismatches.

---

## 4. The flagless resolution channel (why it is required, what it is)

`tools/replay-frozen.py` runs `[python3, <pinned gate>, <input>]` with cwd = a
scratch mirror and **never parses the `command` column** (docstring: "no string
from the `command` column is ever parsed or executed"). Consequence: a D4 run
that needs `--adapter/--projection/--expected` flags **cannot be frozen**. The
round-18 D claim requires a round-18 frozen manifest that replays green, and the
O claim requires the D4 path to be reachable. A flag-only design therefore
fails claim D at the freeze step, and editing `examples/culture-d4/packet.d4.yml`
to carry the typed-chain pointers is refused by this design because that file is
a delivered round-17 artifact whose digest is pinned by two filed round-17/18
artifacts (`typed-labels.d4.yml` `assembly.packet_sha256 = e7ecd204…`;
`expected-holds.json` `packet_sha256 = e7ecd204…`) and by the round-17 frozen
D4 snapshot — an edit would break all three rather than re-pin them.

Chosen channel: **a new data file `tools/gates/typed-pipelines.json`** (schema
`kotodama-typed-pipelines-v1`), matched on the packet's declared generator:

```json
{"schema": "kotodama-typed-pipelines-v1",
 "profiles": [
   {"id": "d4",
    "match": {"assembly_generator": "tools/assemble-culture-d4.py"},
    "projection": {"path": "examples/culture-d4/typed-labels.d4.yml",
                   "sha256": "a59990bb…"},
    "adapter":    {"path": "tools/assemble-d4-typed.py", "sha256": "…"},
    "expected":   {"path": "examples/culture-d4/expected-holds.json",
                   "sha256": "09490a27…"}}]}
```

Rules:

1. Matching is by `assembly.generator` string equality (a declared,
   packet-resident key), or by explicit `--profile <id>`; no path or filename
   heuristics, no sibling-name guessing.
2. Every profile field carries a sha256 that must equal the live file's bytes at
   resolution time; a mismatch → exit 2, `PROFILE-PIN-MISMATCH`, naming the
   field. Editing the profile therefore cannot silently re-point a run: the
   pins move with it or the run refuses.
3. Precedence: explicit flags override profile fields for that run (the run
   prints the effective set); a non-default assembler with **neither** a profile
   match nor `--adapter` → exit 2, `PIPELINE-ADAPTER-MISSING` (never fall back
   onto the D2 adapter: the D2 adapter's own identity leg would refuse anyway,
   and a silent adapter substitution is the laundering class this round is
   closing).
4. Profile path hygiene as §3.2.5, `tools/` or `examples/` allowed for
   adapter/projection/expected (adapter additionally must be a `tools/*.py`).
5. The gate prints, in non-default modes only, one resolution line naming the
   profile id + profile file sha256 + each resolved path + its sha256 (so the
   frozen row's recorded **output bytes** witness the resolution that produced
   them), and the same data appears in the `resolved` block of `--json`.
6. The profile file is data, never code; it is not named `expected.json` and
   does not live under any battery-scanned baseline root, so
   `tools/check-gate-battery.py` cannot mistake it for a gate baseline.

Rejected alternatives, with the forcing reason:

| alternative | why rejected |
|---|---|
| flags only | `replay-frozen` cannot replay a flagged command; claim D's frozen manifest would not exist or would not be replayable |
| edit `packet.d4.yml` to declare the chain | breaks the filed `typed-labels.d4.yml` and `expected-holds.json` packet pins and the round-17 D4 snapshot (filed bytes) |
| filename convention (sibling `typed-labels.<x>.yml`, `assemble-<x>-typed.py`) | resolution by guesswork; a rename silently re-points grading; no pin line |
| environment variables | replays inherit the environment; the frozen verdict would depend on ambient state |

---

## 5. The re-pin cascade (normative; before → after)

Before-shas as-read 2026-10-18 (§1.1). "New pins are new rows/files": no filed
byte of rounds 8–17 (including `tools/gates/frozen/round-11/**` and
`reports/round-16/**`) is edited. The precedence argument: `replay-frozen`
evaluates a manifest atomically, and a row whose `gate_sha256` no longer matches
the live gate reads `gate_digest_mismatch` (exit 2) — so superseded rows cannot
be "fixed" in place without making the filed file itself the record of two gate
revisions.

| # | surface (pins) | before | action | after (record) |
|---|---|---|---|---|
| P1 | `tools/gates/frozen/round-11/MANIFEST.tsv` row 1: gate `d102fd1d…`, snapshot `1b5010b7…`, output `9a69985a…`, exit 0, findings 15 | file sha `aad230bf…` | **new file** `tools/gates/frozen/round-18/repin-d2/MANIFEST.tsv` = byte-copy of the round-11 manifest with **only** row 1's `gate_sha256` cell replaced by the post-change gate sha; row 1's input/snapshot/output/exit/finding cells byte-equal to round-11 | replay `TMPDIR=/var/tmp/... python3 tools/replay-frozen.py tools/gates/frozen/round-18/repin-d2/MANIFEST.tsv` → 11/11 reproduced; round-11 file re-hashed `aad230bf…` before and after |
| P2 | `tools/gates/frozen/round-11/typed-pipeline/run-receipt.json`: gate `d102fd1d…`, `tool_pins{projector 0da0015f, adapter c7e5a749, serializer 8ea6bdde, reader×5}`, `stdout_sha256 9a69985a…` | file sha `c49ebc9e…` | **new file** `tools/gates/frozen/round-18/repin-d2/run-receipt-repin.json` (schema `kotodama-frozen-run-v1`, `supersedes: r11`, before/after gate sha, `tool_pins` identical, `stdout_sha256` = `9a69985a…` unchanged) | the byte-identity claim in one file; round-11 receipt re-hashed `c49ebc9e…` |
| P3 | `reports/round-9/baselines/handoff-packet-check/packet.md:68` `A-SERIALIZER` = `tools/assemble-d2.py 8ea6bdde…` | file sha `0d8d660b…` | **control**: serializer must not move; re-hash receipt (command+date) | before == after (`8ea6bdde…`); if a future touch-set moves it, the re-pin is a new file, never an edit |
| P4 | round-9 baselines / `tools/gates/expected/**` expected.json set: gate shas of the five reader gates + `packet.yml e0f21509…` | battery reading "7 pinned / 0 unevaluable" (this seat, 10:2xZ) | **control**: reader gates must not move; re-run the battery after the change | battery exit 0 with every discovered baseline still `pinned` (§7) |
| P5 | `reports/round-16/handoff/expected-v2-07.json` `inputs`: 7 `tools/` pins (`assemble-culture-d3 ba8d19d5…`, `assemble-d2 8ea6bdde…`, `check-evidence-coupling 849494b0…`, `d2-typed-labels 0da0015f…`, `gates/handoff-packet-check e2fa3223…`, `harness/packet_links 66d854cc…`, `harness/packet_uncertainty cdcc1931…`) + examples/corpus/report pins | file sha `dc75c5d7…` | **control**: none of the seven may move; re-hash each, command+date, and re-run the round-15/16 frozen verify | before == after per pin; a moved pin would require a new `expected-v2-08`-style file (not an edit) |
| P6 | `examples/culture-d2/packet.d2.typed.yml` `assembly.adapter_sha256 c7e5a749…`; `examples/culture-d2/expected-holds.json` projector `0da0015f…` (packet `e0f21509…`, projection `a3aa452c…`) | shas §1.1 | **control**: adapter/projector/packets must not move | before == after; both files re-hashed |
| P7 | prose references to `d102fd1d…` in filed rounds (`git grep -l d102fd1d…` → 12 files, 10:27Z: 10 historical prose — `corpus/lessons/round-17.md`, `reports/round-11/depth/integration.md`, `reports/round-14/{rerun.json,validation.json,verify-4.md}`, `reports/round-17/{d4/design-brief.md,d4/typed-support-1.md,scribe-2.md,tests/neg-1.md,tests/neg-2.md}` — plus P1's `MANIFEST.tsv` and P2's `run-receipt.json` themselves) | historical records | **must not be edited**; supersession is signalled only by the round-18 receipts | the sweep itself (command+date+count) is filed as the control |
| P8 | round-11 row 1 post-change class | — | **record the expected class**: after the gate edit, replaying the *filed* round-11 manifest yields row 1 `gate_digest_mismatch` → exit 2 (the standard's §6 "revised gate" class, could-not-evaluate). This is supersession, not a regression; the green replacement is P1 | filed in the round-18 receipt with both readings (pre-change 11/11; post-change r11 row-1 reason; P1 11/11) |
| P9 | new D4 frozen generation | — | **new** `tools/gates/frozen/round-18/typed-pipeline-d4/`: `packet.d4.yml` (byte copy of `e7ecd204…`), snapshot copy, `run.log` (gate stdout over the frozen copy), `MANIFEST.tsv` (gate = post sha; input = the frozen path; exit 0; finding_count 15), `run-receipt.json` (schema `kotodama-frozen-run-v1`; pins the profile file sha, the resolved adapter/projection/expected shas, the assembler declaration) | `TMPDIR=/var/tmp/... python3 tools/replay-frozen.py tools/gates/frozen/round-18/typed-pipeline-d4/MANIFEST.tsv` → green |
| P10 | the gate's own new sha | `d102fd1d…` | recorded in the round-18 `validation.json` receipt, the new manifests and the LOG entry | before → after printed by the runner |

Cascade rules:

1. **Single digest change.** Only `tools/gates/typed-pipeline-gate.py` (plus new
   files) may move. §6 names the forbidden touch-set and why.
2. **Every before/after pin carries the reading command and date.**
3. **No filed receipt is edited**; the immutability controls (P1, P3–P7) are
   re-hashed before and after the change and their equality filed.
4. **The re-pin manifest is derived, not hand-written**: generated from the
   filed manifest by substituting one cell, then replayed; its `--json`
   receipt is filed (the R18-O11 `repin_replay.py` idiom, measured green
   pre-change: `.scratch/r18-o11/repin-receipt-before.json`, 11/11).

---

## 6. The forbidden touch-set (and the forcing reason)

`tools/assemble-d2-typed.py`, `tools/d2-typed-labels.py`, `tools/assemble-d2.py`
and the five reader gates **must not change bytes in round 18**.

Reason, measured: the round-11 frozen typed packet (`1b5010b7…`) pins the D2
adapter `c7e5a749…` (`assembly.adapter_sha256`), and the gate's L4 in the
typed-packet path compares that pin against the **live** adapter
(`typed-pipeline-gate.py:367-371`). If the adapter changes, the re-pinned
round-11 row cannot reproduce the recorded exit 0 — it becomes exit 1 at
`L4-pins`, i.e. the strongest available proof of "the re-pin is a digest change,
not a verdict change" (R18-O11's method) would be red. The same argument
protects the serializer (`8ea6bdde…`, pinned by `expected-v2-07.json` and by
`run-receipt.json`) and the projector (`0da0015f…`, pinned by
`examples/culture-d2/expected-holds.json` and `expected-v2-07.json`).

Consequence for the D4 chain: the D4 typed build belongs in a **new** file
(`tools/assemble-d4-typed.py`, named in the R17 brief §9.1 and in the profile),
not in a generalization of the D2 adapter. At this seat's stamp that file does
not exist (`ls tools/assemble-d4-typed.py tools/d4-typed-labels.py` → both
"No such file", 10:29Z); the D4 projection itself already runs on the D2
projector (`reports/round-18/gate/tests-2.md` receipt 2: stats `{fail:0,
hold:15, labels:74, note:1}`), so the projector needs no D4 twin. The D4
adapter's interface contract (from this design):

- CLI: `--packet PATH --projection PATH [--emit PATH] [--check PATH]
  [--selftest]` (the round-17 runner's discovery/replay shape,
  `reports/round-17/run-validation.py:579-601`);
- module: `build(packet_path, projection_path)` → `{exit, problems, inputs,
  payload, doc}` (the D2 adapter's shape, `tools/assemble-d2-typed.py:265`);
- identity: uses the §3.2 resolution (declared assembler), **not** a second
  D2-bound check; renders twice and requires byte equality before returning
  (the D2 adapter's two-consecutive-builds control);
- emits exactly `examples/culture-d4/packet.d4.typed.yml` on a default build.

---

## 7. Acceptance and evidence matrix (what the runner must measure)

The round-18 runner (`reports/round-18/run-validation.py`, another seat's
write) records, at minimum:

| # | measurement | expected |
|---|---|---|
| A1 | default stdout sha + exit over `examples/culture-d2/packet.d2.yml` | `15cdfbda…`, exit 0 (byte-identical before/after) |
| A2 | `--json` stdout sha | `19765ddf…`, exit 0 |
| A3 | frozen typed packet path stdout sha | `9a69985a…` == `run.log` |
| A4 | replay of P1 re-pin manifest | 11/11 reproduced, exit 0 |
| A5 | replay of the filed round-11 manifest (post-change) | row 1 `gate_digest_mismatch`; recorded as the supersession class (P8), not as a new failure |
| A6 | r17-D4 manifest replay | 5/5 reproduced, exit 0 (unchanged) |
| A7 | `--selftest` (post-change) | exit 0, including the D2 both-directions constant check and the new controls below |
| A8 | D4 run `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | exit 0; findings equal `examples/culture-d4/expected-holds.json` as a set keyed `(id, severity, where)` with details; run twice byte-identical; the resolution line names `tools/assemble-culture-d4.py` @ `943f487b…` |
| A9 | P9 D4 frozen manifest replay | green |
| A10 | battery / craft / validators | battery exit 0 (all baselines `pinned`); craft exit 0; runner green |
| A11 | P1–P7 control re-hashes | every filed byte before == after |

New selftest controls (mirror-only, `TMPDIR=$PWD/.scratch`, no live writes):

| # | control | expected |
|---|---|---|
| N1 | forged declaration: D4 packet copy with one byte flipped (and its `assembler_sha256` left stale, or updated to a forged value) | stale forged pin → exit 2 `DECL-ASSEMBLER-PIN-MISMATCH`; internally-consistent forged pin whose build differs → exit 1 naming the resolved assembler |
| N2 | conflict: `--assembler tools/assemble-d2.py` over the D4 packet (declaration says `assemble-culture-d4.py`) | exit 2 `DECL-ASSEMBLER-CONFLICT` |
| N3 | declaration edited, three variants, over the D4 packet: (a) `assembly` block removed entirely, no flag; (b) `assembler_sha256` removed but `generator` kept, no flag; (c) both keys removed and `--assembler-sha256` (no `--assembler`) supplied | (a) resolution `default` → the identity leg fails naming `tools/assemble-d2.py` (a packet with no declaration resolves to the documented default, never to "identity not checked"); (b) exit 2 `DECL-ASSEMBLER-PIN-MISSING` (an unpinned non-default declaration is refused, not silently pinned to live bytes); (c) exit 2 `DECL-ASSEMBLER-CONFLICT` (a pin without its assembler is incoherent) |
| N4 | path hygiene: `--assembler ../x.py`, absolute path, symlink, `tools/gates/typed-pipeline-gate.py` as assembler | exit 2 `DECL-ASSEMBLER-PATH`, and nothing is executed |
| N5 | non-default assembler with no profile match and no `--adapter` | exit 2 `PIPELINE-ADAPTER-MISSING` (no silent D2-adapter substitution) |
| N6 | profile pin drift: profile copy with a wrong projection sha | exit 2 `PROFILE-PIN-MISMATCH` |
| N7 | interface missing: a mirror `tools/assemble-x.py` (declared+sha-consistent) with no `assemble()` | exit 2 `DECL-ASSEMBLER-INTERFACE` |
| N8 | malformed packet on the default path, before/after | identical exit 2 and identical stderr message (prescan must not add a new diagnostic) |

---

## 8. Implementation order and ownership (single-writer surfaces)

1. **O gate seat (single writer)**: edit `tools/gates/typed-pipeline-gate.py`
   (§3, §4), add `tools/gates/typed-pipelines.json`, extend `--selftest`
   (N1–N8). No other file.
2. **D4 adapter seat (single writer)**: `tools/assemble-d4-typed.py` to the
   §6 contract; emits `examples/culture-d4/packet.d4.typed.yml`.
3. **Frozen/receipt seat**: P1, P2, P9 (`tools/gates/frozen/round-18/**`),
   using the R18-O11 derived-manifest idiom; TMPDIR outside the repo for every
   replay.
4. **Runner seat**: A1–A11 in `reports/round-18/run-validation.py`; never
   pipes a replay into `tail` (pipeline exit trap, `reports/round-18/scope.md`
   §"Gate", O item 4 precedent).
5. **Integrator**: before/after pin table (P1–P7) in the round-18 receipt and
   one LOG.md entry; no filed byte of rounds 8–17 touched.

---

## 9. Limits

- The D4 typed adapter and the round-18 runner are **not landed** at this
  seat's stamp (§6; `reports/round-18/scope.md` census). A8/A9 cannot be
  demonstrated until they do; this design fixes their interfaces, it does not
  vouch for them.
- The profile file is a new declaration surface; the review seat
  (R18-O02, `reports/round-18/gate/design-review.md`) stress-tests it, and its
  findings are part of this design's record.
- Every sha in this file is as-read at the stamps above; a later revision is a
  re-read event, never a licence to compare across revisions.
- NON-CANON throughout; nothing here is a clearance, a handoff, or a canon
  decision.

---

## 10. Additions folded in from the review (R18-O02)

The following are normative parts of this design, added in response to
`reports/round-18/gate/design-review.md` before implementation (the review's
findings F1–F3, F5, F6, F9; the review's own record keeps the reasoning):

1. **L3/L4 authority in non-default modes (review F1).** In `declared` /
   `flag-pinned` / `flag` modes the L3 expected set, note set, counts and
   detail pins come from the **resolved expected file alone**; the embedded
   `EXPECTED_HOLDS` / `EXPECTED_NOTES` / `EXPECTED_COUNTS` constants
   (`typed-pipeline-gate.py:80-98`) are consulted only in `default` mode, and
   `json_document`'s `counts` reflects the active set. Without this a D4 run
   exits 1 by construction (F1's measurement). The selftest's both-directions
   constant check stays D2-only and byte-unchanged. L4 in non-default modes
   compares the pins embedded in the graded build against the **resolved**
   packet/projection/adapter (the default-mode expectation map is unchanged).
2. **Resolution scope (review F2).** The resolution runs on the legacy path
   only (`typed_arg is None` in `main()`, `:594-605`). The typed-packet path
   keeps its embedded pins and its current output bytes — the re-pin replay
   (A4) exercises exactly that path and must stay `9a69985a…`.
3. **The D4 frozen row's live-companion dependency (review F3) must be stated
   in `tools/gates/frozen/round-18/typed-pipeline-d4/README.md` and its
   receipt**: the row asserts (frozen packet bytes, live companions at the
   recorded shas, gate revision); any D4 companion edit makes it read exit 1 at
   `L4-pins` — the pin working, not the row rotting.
4. **Identity-record key discipline (review F5).** The D4 adapter's build
   result reports its own identity record under the key `assembler_identity`
   (the D2 adapter's key, `tools/assemble-d2-typed.py:275`) or omits it; the
   suppression rule in §3.3 targets that key and nothing else.
5. **Pin source recorded (review F6).** The resolution line and the `resolved`
   JSON block carry the mode (`declared`/`flag-pinned`/`flag`); the round-18
   receipt records the mode of every non-default run.
6. **N3 corrected (review F9)** — see the §7 table: the three-variant control
   (no block → default-and-fail; digest-only removal →
   `DECL-ASSEMBLER-PIN-MISSING`; pin-without-assembler → conflict refusal).
7. **A8's dependency named (review F10).** A8's exit-0 expectation presumes the
   D4 typed build's routing retires the legacy D4 naming artifacts exactly; a
   red A8 on the channel leg is routed to the D4-routing owner, not to the gate
   seat.

---

## 11. Post-stamp addendum — the implementation landed while this pair was written

At the addendum stamp (2026-10-18, ~10:45Z; `sha256sum tools/gates/typed-pipeline-gate.py`
→ `84dc177e79688e0ed7f323ead42233205b7df7c68183d434bd32a906d647bad4`,
1220 lines; `git status --porcelain tools/` → ` M tools/gates/typed-pipeline-gate.py`)
a generalized gate exists in the working tree, uncommitted. Its docstring
declares a **different resolution channel than §4 of this design**: a packet
`typed_pipeline` block (or `assembly.generator` / `assembly.assembler` keys)
plus `--assembler/--projection/--adapter/--expected/--legacy-packet` flags,
with precedence "flags > packet declaration > family convention > D2 defaults",
and the identity leg calling the declared assembler's own `assemble()` with a
mismatch as exit 2. Observed divergences from this design, listed for the
reviewer and the runner (not repaired here — this seat writes design files only):

1. **Channel.** The profile-file channel (§4) is absent
   (`ls tools/gates/typed-pipelines.json` → absent, 10:45Z); the flagless
   requirement is instead served by the packet block + family convention. The
   forcing constraint of §4 (a `replay-frozen` row cannot carry flags) still
   holds; whether the landed channel satisfies it is measured by A9/P9, not by
   this design.
2. **Precedence.** The landed precedence puts flags above the packet
   declaration; this design put the **declared pin** above the flag where both
   carry digests, refusing conflicts (claim text: "packet-declared pin
   preferred; flag fallback"). The runner should record which reading the
   round admits and that a conflict (declaration vs flag naming different
   assemblers) is refused rather than silently resolved.
3. **Exit class.** This design: packet-vs-build mismatch = exit 1 (the L1 leg
   fails), pin/path/interface = exit 2. Landed gate docstring: "a mismatch is
   exit 2". The difference is class-only (both block), but A8's negatives (N1)
   must be written to whichever class is admitted, or the control records the
   wrong expectation.
4. **§3.3's suppression rule / §6's forbidden touch-set** still apply to the
   landed revision: the D2 adapter, serializer and projector must hash as in
   §1.1, and the D2 default bytes must equal `15cdfbda…` / `9a69985a…` /
   `19765ddf…` (A1–A3). The D4 adapter (`tools/assemble-d4-typed.py`) is still
   absent at this stamp, so A8/A9 remain unproven.
5. **New round-18 surfaces observed at this stamp** (untracked, for the
   runner's cross-check): `tools/gates/d4-assembly-check-gate.py`
   (`df1a364b…`), `tools/gates/d4-typed-labels-check-gate.py` (`05f99629…`),
   `tools/gates/frozen/round-18/`, and r18-post baseline dirs under
   `tools/gates/frozen/*/r18-post/`. Their pins are their owners' to file;
   this design only notes they exist when the cascade is re-run.

All line-number citations in this file (`:55-69`, `:80-98`, `:195-197`,
`:305-313`, `:314-338`, `:367-371`, `:426`, `:594-605`) are against the
pre-change revision `d102fd1d…` (612 lines) and shift under the landed
revision; they are stamps, not live pointers.
