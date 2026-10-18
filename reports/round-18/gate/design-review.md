# R18-O02 — adversarial design review of R18-O01 (declared-assembler identity + re-pin cascade)

- round: 18 (operator loop 2 of 3, build round 2 of 4) · shard: **O02**
  (generalization design ×2; this file is the review half of the pair with
  `reports/round-18/gate/design.md`, R18-O01). Claim O `gate-generalization`.
- assignment (verbatim): "O R18-O01..O02 (generalization design x2): read
  tools/gates/typed-pipeline-gate.py L1 + reports/round-17 ruling; design the
  declared-assembler mechanism (packet-declared pin preferred; flag fallback);
  specify the re-pin cascade exactly (which manifests/baselines pin which shas);
  reports/round-18/gate/{design,design-review}.md."
- date: 2026-10-18. Reference revision HEAD `c66ac3c…`; measurements
  10:19–10:35Z; stamps local (-03:00) unless marked Z.
- canon: NON-CANON engineering review. Nothing here is canon, a lore receipt, a
  handoff, or a real-world clearance/rights statement.
- writes: **this file only** plus gitignored scratch under
  `.scratch/r18-gate-design/` (`TMPDIR` exported before every scratch-write; the
  frozen replays ran with `TMPDIR=/var/tmp/kotodama-r18-design` because
  `tools/replay-frozen.py` refuses an in-repo mirror root by its own design).
  `reports/round-18/gate/design.md` was **not** edited by this seat; findings
  below are dispositions for the implementer and integrator, not in-place fixes.
  No commit, no push.

## 0. Verdict

**The design is implementable and its load-bearing constraints are measured, not
asserted; when first reviewed it carried two structural gaps and one
under-specified surface (F1, F2, F3), all seven actionable findings were closed
in the design's §10 before this pair was handed off (the review's §3 records the
mapping), and eleven findings in total stand as the record of what the
implementation must satisfy.** The core decision — declared pin preferred, flag
fallback, the D2 default path frozen byte-for-byte, and a single-digest-change
re-pin cascade — is the right shape for the round-17 rejection and for the two
binding constraints I could not weaken (§1): the frozen round-11 rows'
replayability and `replay-frozen`'s flagless launch contract. Nothing in §1
contradicts the design; one of its numbers I could not reproduce from my own
commands (the `--json` before-sha) is marked `to-verify` with the reason.

## 1. Independent verification of the design's load-bearing facts

All commands cwd = lane root, 2026-10-18, this seat. "verified" = I ran it and
read the output at the stamp; "cited" = the design cites another seat's receipt
that I read but did not re-execute.

| design claim | my measurement | verdict |
|---|---|---|
| gate sha `d102fd1d…` (design §1.1) | `sha256sum tools/gates/typed-pipeline-gate.py` 10:27Z → match | verified |
| D4 packet declares `tools/assemble-culture-d4.py` @ `943f487b…` (§1.5) | `sed -n '2344,2347p' examples/culture-d4/packet.d4.yml` → the pair; `sha256sum tools/assemble-culture-d4.py` → `943f487b…` | verified |
| the D4 refusal message (§1.3) | `.scratch/r18d/gate-d4.out` read 10:24Z: `FAIL L1-assembler_identity: packet bytes are not assemble-d2.py's deterministic assembly (e7ecd2045ef0 vs e0f21509e14a)`; twins in `reports/round-18/gate/tests-2.md` R1 and `reports/round-18/d4/interop-1.md` | verified (file) + cited (sibling runs) |
| adapter leg is hard-coded D2 (§2) | `tools/assemble-d2-typed.py:112-125` read: `SERIALIZER` load + `serializer["assemble"]()` compare, no argument | verified |
| uniform build interface exists on both assemblers (§2) | `assemble-d2.py:93 def assemble()`; `assemble-culture-d4.py:396 def assemble()` (docstring: "returns the packet bytes") | verified |
| default stdout sha `15cdfbda…` (§1.2, A1) | ran the gate twice, `cmp` identical, sha match | verified |
| frozen-row stdout sha `9a69985a…` == `run.log` (§1.2, A3) | round-11 manifest row 1 output sha read; R18-D14 measured `cmp` byte-identical; this seat verified the manifest pin value | cited (D14) + verified (pin read) |
| `--json` sha `19765ddf…` (§1.2, A2) | I did **not** re-run `--json`; value comes from `reports/round-11/validation.json` and R18-D14's re-measurement | **to-verify** (low risk: two independent records agree) |
| round-11 replay 11/11 exit 0 (§1.4) | ran it (`TMPDIR=/var/tmp/…/`) → `REPLAY OK: 11/11`, exit 0 | verified |
| r17-D4 manifest 5/5 exit 0 | ran `reports/round-17/tests/frozen/MANIFEST.tsv` → 5/5, exit 0 | verified |
| r3 all 7 rows `gate_digest_mismatch`, r4 no manifest (§1.4) | ran both: r3 exit 2, 7/7 could-not-evaluate; r4 `manifest_unreadable` (no `MANIFEST.tsv`) | verified |
| battery 7 pinned / 0 unevaluable; craft 10/10 + 18/18 (§1.2) | ran both, exit 0 | verified |
| the filed manifest/receipt shas (§1.1, P1–P6) | `sha256sum` on all six: match | verified |

The rejection text quoted in design §1.3 is verbatim from `LOG.md:3232-3236` as
read; the D2-bound leg's identity as D2-bound is additionally recorded in the
round-17 lane at `reports/round-17/d4/typed-support-1.md:354` and
`reports/round-17/d4/typed-run.md:96-171`.

## 2. Findings against the design

### F1 — (high) the design never specifies L3/L4 *authority* in non-default mode; as written, a D4 run would fail L3 against D2's embedded constants

**Evidence.** `tools/gates/typed-pipeline-gate.py` carries the D2 hold set as
module constants (`EXPECTED_HOLDS`, `EXPECTED_NOTES`, `EXPECTED_COUNTS`, lines
80-98) and L3 compares the observed set against them (`:305-313`) *and* against
the expected file (`:314-338`); the report prints `EXPECTED_COUNTS`
(`json_document`, `:426`). The design's §3/§4 generalize the assembler and the
artifact selection but say nothing about L3's authority switch, while design
A8 expects the D4 run to exit 0 with findings equal to
`examples/culture-d4/expected-holds.json` (15 holds + 1 note, sha `09490a27…`,
this seat re-hashed). A generalized gate that still gates D4 findings against
`EXPECTED_HOLDS` exits 1 by construction — the round-17 rejection at a new
address.

**Required addition.** In non-default modes: L3's expected set, notes and counts
come from the resolved expected file alone; the embedded D2 constants are
consulted only in `default` mode (protecting A1–A3 byte identity), and
`json_document`'s `counts` reflects the active set. The selftest's both-directions
constant check stays D2-only and unchanged.

### F2 — (high) the resolution's scope is under-specified: which entry paths run it

**Evidence.** `main()` (`:594-605`) routes a file carrying `typed_channel` to
the typed-packet path; the legacy path is the only one that builds through an
adapter. The design's §3.2 does not state that the typed-packet path
(`typed_arg`) is out of the resolution's scope; but A4's re-pin replay exercises
exactly that path with the new gate, and its bytes must stay `9a69985a…`. A
generalizer who wires the resolution into `main()` unconditionally changes that
path's output (a resolution line would fail A4 and the re-pin manifest).

**Required addition.** State: resolution runs only on the legacy path
(`typed_arg is None`); the typed-packet path keeps its embedded pins and its
current output bytes; if a future round wants a declared channel there, it is a
new claim with its own re-pin.

### F3 — (medium-high) the D4 frozen row is a live-tree-dependent row; the design does not say so

**Evidence.** `replay-frozen` copies only the row's *input snapshot* into a
mirror and runs `[python3, <live gate>, <input>]` with cwd = mirror
(`tools/replay-frozen.py:170-198`). The profile-resolved projection/adapter/
expected are resolved against the lane root by the gate, and the D4 snapshot is
the packet only — so the P9 row is green only while the live
`tools/assemble-d4-typed.py`, `examples/culture-d4/typed-labels.d4.yml` and
`examples/culture-d4/expected-holds.json` keep exactly the shas the row's
`run.log` witnessed. This is the same class as the round-11 typed row (it pins
the live adapter), so it is acceptable — but a reader will otherwise read the
D4 row as artifact-independent.

**Required addition.** Say it in the P9 receipt and in the frozen README: the
row asserts (frozen packet bytes, live pinned companions at their recorded shas,
gate revision); any D4 companion edit makes the row read exit 1 at `L4-pins`,
which is the pin working, not the row rotting.

### F4 — (medium) the profile file is a new declaration surface the row does not pin directly

The design mitigates this (resolution line in stdout, receipt pins, per-field
shas; §4.2, §4.5, P9) and I could not construct a cheaper mitigation: the row's
columns cannot carry a `--profile` argument and a profile sha column would be a
schema change to a tool the round must not touch. Residual risk stated: an
edited profile shows up in the **output bytes** of any post-freeze run
(the resolution line names the profile sha and each resolved sha), and any
attempt to re-point a run without moving the pins refuses
(`PROFILE-PIN-MISMATCH`). Disposition: accepted as designed; the implementer
must make the resolution line unconditional in non-default modes (it is the
only witness the frozen bytes carry).

### F5 — (medium) "exactly one `L1-assembler_identity`" needs a concrete suppression rule

The design (§3.3) suppresses the adapter's own identity record in non-default
modes, but the printing loop is generic: `for name, record in built["inputs"].items():
check("L1-%s" % name, …)` (`:195-197`). The D4 adapter contract must keep the key
name `assembler_identity` for its own record (as the D2 adapter does,
`tools/assemble-d2-typed.py:275`) so the suppression rule has a stable target —
otherwise a D4 adapter that reports its identity under another key yields two
identity checks with different names, and the "names the assembler it checked"
requirement becomes ambiguous. Required addition to §6's adapter contract;
implementer may instead have the D4 adapter not emit the record (then the rule is
a no-op) — either is acceptable, but the contract must say which.

### F6 — (medium) mode `flag-pinned` / `flag` record no pin-source; a reader cannot tell a self-consistent run from a pinned one

With `--assembler` alone, the effective pin is `sha256(live file)` — a
tautology that still catches a mid-run swap but proves nothing about the
assembler the operator meant. The design's A-matrix has no row requiring the
run's *receipt* to state the pin source (`declared` / `flag-pinned` / `flag` /
`default`). Required addition: the resolution line and the `resolved` JSON block
carry the mode; the round-18 receipt records it for every non-default run.

### F7 — (low) the TOCTOU window between pin check and `runpy` load is narrowed but not closed

Design §3.2.7 already requires a post-load re-hash. Residual: the executable
bytes loaded are a second read of the path. This is the lane's existing trust
base (`load_peer` is used by the gate and the adapters today), so the disposition
is "accept, and say so": the pin is an integrity control against drift, not a
sandbox. No change required; the review records the limit so no later reader
upgrades it into a security claim.

### F8 — (low) A5 (the filed round-11 manifest reading `gate_digest_mismatch` after the change) must be classed in the runner, or it looks like a new red

The design does say this (P8, A5) and cites the standard's §6 "revised gate"
class. The review adds the operational detail from `reports/round-18/scope.md`
O-item 4: the runner must print the class and the reason string
(`gate_digest_mismatch`, row 1) next to the pre-change 11/11 and the re-pin
manifest's 11/11 — three readings, one judgement — or a reader sees a bare red.

### F9 — (low) N3's expected behavior was imprecise: the digest-less declaration case

The original N3 read "digest removed, no flag → default → fails naming
assemble-d2.py". That is wrong twice over: `packet.d4.yml` with its
`assembler_sha256` removed but `generator` kept does **not** fall to the default
(the generator still names `tools/assemble-culture-d4.py`), so the control as
written would have graded the D4 packet against the D4 assembler and proved
nothing; and a non-default declaration without its digest had no defined mode in
the original mode vocabulary at all. **Disposition (closed in design §3.2
steps 2/4 and the §7 N3 row):** the mode set gains the `missing pin` refusal — a
non-default `generator` without `D`/`S` → exit 2 `DECL-ASSEMBLER-PIN-MISSING`;
a pin without an assembler (`S` present, neither `F` nor `G`) → exit 2
`DECL-ASSEMBLER-CONFLICT`; and N3 became three variants (no `assembly` block →
default → identity fails naming `tools/assemble-d2.py`; digest-only removal →
PIN-MISSING; pin-without-assembler → conflict). A control that cannot fail is a
probe; this one can.

### F10 — (low) the design's D4-run expectation (A8 exit 0) presumes the D-side channel differential

A8 (exit 0 over `packet.d4.yml`) additionally requires the D4 typed build's
routing to retire the legacy D4 naming findings exactly (the L2 leg compares the
typed and legacy gate runs; the round-17 frozen D4 row records naming 8 over the
round-17 snapshot). That is a D-side property (routing rows ↔ PHON artifacts),
not an O-side one. Required: the design should name the dependency so a red A8
is not mis-routed to the gate seat; the O seats vouch for the mechanism, the D
seats for the D4 routing.

### F11 — (low) `tools/gates/typed-pipelines.json` placement

Adding a data file under `tools/gates/` does not break `replay-frozen` (its
whitelist governs the row's `gate` value only) or the battery
(`tools/check-gate-battery.py` header: it copies the seven `.py` scripts and the
fixture tree). Recorded as an accepted placement with one alternative
(`tools/typed-pipelines.json`, outside the gates directory) if the implementer
prefers to keep `tools/gates/` byte-stable except for the gate itself. No
finding.

## 3. Dispositions (checklist for the implementer/integrator)

All seven additions below were folded into the design as its §10 before this
pair was handed off (the review keeps the reasoning; the design carries the
normative text). Implementers must satisfy the §10 text, not re-derive it:

1. F1: L3/`json_document` authority switch (non-default = expected file) — design §10.1.
2. F2: resolution scope = legacy path only; typed-packet path untouched — §10.2.
3. F3: the D4 row's live-companion dependency stated in its receipt/README — §10.3.
4. F5: D4 adapter identity-record key discipline (or no record) — §10.4.
5. F6: pin-source mode recorded in the resolution line + receipt — §10.5.
6. F9: N3 control corrected (three variants, incl. the missing-pin refusal) — §10.6
   and the design's §3.2/§3.5/§7 text.
7. F10: A8's D-side dependency named in the runner's receipt text — §10.7.

## 4. What this review does not vouch for

- The D4 typed adapter, the round-18 runner and the D4 frozen generation do not
  exist at my stamp; their interfaces are judged as specifications only.
- The `--json` before-pin (`19765ddf…`) is a cited value, not a re-measurement
  (F-table row, §1).
- No claim about the D4 expected set's content is made here beyond the pins and
  counts I re-hashed; the D claim's evidence is `reports/round-18/d4/**`.
- NON-CANON throughout; no clearance, canon or rights statement.

## 5. Post-stamp observation (2026-10-18 ~10:45Z)

While this pair was being finished, a generalized gate landed uncommitted in
the working tree (`sha256sum tools/gates/typed-pipeline-gate.py` →
`84dc177e79688e0ed7f323ead42233205b7df7c68183d434bd32a906d647bad4`, 1220 lines;
`git status --porcelain tools/` → ` M tools/gates/typed-pipeline-gate.py`). It
implements a **packet-block + family-convention + flag** channel rather than
this design's profile-file channel; the divergences (channel, flag-above-
declaration precedence, mismatch-as-exit-2) are enumerated in `design.md` §11.
Two consequences for the reviewer of the *implementation*:

1. Findings F1, F2, F3, F5, F6, F9, F10 of this review are obligations against
   **any** channel, not only the designed one; the implementer's revision must
   be measured against §10's text or its own recorded equivalent — a landed
   file is not evidence that they are satisfied.
2. The re-pin cascade (design §5, P1–P10) and the A1–A3 byte pins are the
   regression contract; a variant implementation is acceptable only if A1–A3,
   A6 and the re-pin manifest (A4) reproduce their before values, and if the
   supersession classes (A5/P8) are filed rather than hidden.
3. `--selftest-generalized` exists in the landed revision; whether it carries
   the N1–N8 negatives (forged pin, conflict, missing pin, path hygiene,
   adapter-missing, profile-equivalent pin drift, interface, malformed) is
   unmeasured by this seat and belongs to the O-tests seats.
