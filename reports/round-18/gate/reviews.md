# R18-O15..O20 — adversarial review: bypass paths and pin confusion in the generalized typed gate

- round: 18 (operator loop 2 of 3, build round 2 of 4; 64 workers) · shard:
  **O15..O20** (regression+review ×6, claim O `gate-generalization`) · owner: L2
  worker, kotodama-shokunin lane.
- assignment (verbatim): "… adversarial reviews of the generalization (bypass
  paths, pin-confusion); reports/round-18/gate/{regression,reviews}.md."
- date: 2026-10-18. Subject revision: `tools/gates/typed-pipeline-gate.py`
  sha256 `ea95e2a1452ef51d780a701a77c37b2daf38bdae5fe6ac25e404ce2dc65d282d`
  (10:33Z, first complete generalization) and `286d6e82711427ea03a9a42e5cb10f6c369f0f1b0cd589c74a4092f3b8c12af9`
  (10:41–10:43Z, the revision the re-pin manifest pins). **Every probe below was
  re-run at both revisions with identical readings**; the gate was still being
  edited by its owner while this seat worked, so each finding names its stamp.
- canon: NON-CANON engineering review. Nothing here is a canon record, a lore
  receipt, a handoff, a clearance, or a rights ruling. Findings are engineering
  defects, not culture conclusions.
- writes: **this file and `reports/round-18/gate/regression.md`** plus gitignored
  scratch under `.scratch/r18o/**` (clearly marked as this seat's own fixture tree).
  No gate, packet, baseline, manifest or earlier-round byte was edited by this
  seat; the probe fixtures live only under `.scratch/`. No commit, no push.

## 0. Verdict

**The generalization does what claim O requires on the surface that matters most —
the default D2 path is byte-identical and the D2 frozen verdict reproduces
(`regression.md` §3) — and its declared-identity leg is measurably real (a stale
`assembly.assembler_sha256` is refused, exit 2; a tampered packet is refused by the
adapter's own leg). But the declaration channel as implemented is *self-attesting
and packet-controlled*: a graded packet can name, as its own assembler, a file
outside the lane; the gate loads and executes it and then reports the identity leg
green. Three defects (F1 high, F2 medium, F3 medium) and two lower findings follow,
each with a re-runnable command and stamp.**

## 1. Scope and method

Reviewed: the generalized resolver and the L1/L2 changes in
`tools/gates/typed-pipeline-gate.py`; the re-pin cascade records
(`reports/round-18/repin/`), the three new frozen generations, and the r18-post
baselines. Not reviewed (other seats own them, still in flight at the stamp): the
D4 gate run and the D4 typed adapter (`reports/round-18/d4/`), the new
`d4-*-check-gate.py` adapters, the civ-map revision.

Method: read the code, then probe it with packets this seat authored under
`.scratch/r18o/probe/` (each a copy of a committed packet plus one declaration
block), run from the lane root with `TMPDIR=$PWD/.scratch`. Probe outputs kept as
`.scratch/r18o/probe/final-*.json` (`--json` runs) and
`.scratch/r18o/probe/EXECUTED-MARKER.txt`.

The mechanisms that were verified as intended:

- **Resolution order** `flags > packet declaration > family convention > D2 defaults`
  (`resolve_config`, gate lines 248-274). With every key on its D2 value the run is
  `generalized = False` and takes the pre-generalization path — measured
  byte-identical stdout at `15cdfbda…` before and after the change.
- **`L1-assembler`** calls the declared assembler's own `assemble()` and byte-compares
  its payload with the graded packet, never re-implementing it (`assembler_identity`).
- **`L1-expected-holds`** loads the declared expected file and fails closed on
  missing/unreadable/inconsistent content (probes: exit 2 with the leg named).
- **`--selftest-generalized`** is green `14/14` at `286d6e82…` (10:41Z), including
  default-resolution, tamper, drift, self-pin, missing-expected and stale-pin controls.
- **The frozen D2 verdict** reproduces byte-for-byte
  (`9a69985a…` == the filed `run.log`) and the re-pin manifest replays `11/11`.

## 2. Bypass findings

### F1 (HIGH) — the identity leg is self-attesting, and a packet's declaration is executed as code

*Evidence.* Probe `culture-d2c` (a copy of `examples/culture-d2/packet.d2.yml` plus
`typed_pipeline: {generator: "<absolute path under .scratch>/evil-assembler.py"}`):

```
python3 tools/gates/typed-pipeline-gate.py .scratch/r18o/probe/culture-d2c/packet.d2.yml --json
# exit 2; marker file written by the module's import-time code:
#   "this file was loaded and executed by the gate"
# checks: [('L1-assembler', True), ('L1-expected-holds', False, 'missing: …')]
# resolved.assembler: .scratch/r18o/probe/evil-assembler.py
```

Stamps: 10:36Z (`ea95e2a1…`) and 10:42Z (`286d6e82…`), identical reading.

*Why it works.* `candidate_path` (lines 203-208) accepts absolute paths and `..`
without any lane-containment check; `load_peer` is `runpy.run_path` (lines 169-170),
so the declared file is executed; `assembler_identity` compares the declared
assembler's own `assemble()` output with the packet — a file the packet names can
trivially reproduce the packet's bytes, so the leg passes; the optional self-pin
branch (`if declared_sha:`) runs only when the packet also carries
`assembly.assembler_sha256`, and `examples/culture-d2/packet.d2.yml` carries **no**
such pin (`grep -c assembler_sha256` → 0; D4's packet does pin
`943f487b…` at `examples/culture-d4/packet.d4.yml:2346`). The pin control itself
works when present — probe `culture-d2d` (stale `deadbeef…` pin) exits 2 with
`assembler self-pin broken: packet pins deadbeefdead, live … hashes 11eaed72`.

*Impact.* Any packet that reaches the gate — a design artifact under active editing,
which is exactly this lane's threat model — can (a) satisfy the "assembler identity"
leg with its own implementation and (b) cause an arbitrary file's code to run with
the gate's privileges. The reviewed design (`reports/round-18/gate/design.md` §0)
proposed a flagless, sha-pinned channel (`tools/gates/typed-pipelines.json`) partly
for this reason; that file is **absent** (`ls tools/gates/typed-pipelines.json` →
no such file, 10:45Z), and the round's own counting command now fails on exactly that
absence: at 10:47Z `run-validation.py --check` reports "the D4 gate run names no
declared assembler in its resolution line", "… no assembler digest in its resolution
line", and `tools/gates/typed-pipelines.json: [Errno 2] No such file or directory`
(claim-D failures 2/5). The mitigation the design review approved did not land, and
the round's instrument already says so.

*Minimal fix (one of).* Require an `assembler_sha256` pin for any generalized run and
fail closed without it; or resolve declarations through a committed registry with
digests; and reject declared paths that do not realpath inside the lane (the same
hygiene `tools/replay-frozen.py` already enforces on manifest paths).

### F2 (MEDIUM) — alias collision: `assembly.generator` silently overrides `typed_pipeline.assembler`

*Evidence.* Probe `culture-d9` (a copy of the D4 packet plus
`typed_pipeline: {assembler: "<scratch>/evil-assembler.py"}`): the `--json` run at
10:36Z and 10:42Z resolves `assembler = tools/assemble-culture-d4.py` — the packet's
own `assembly.generator` — and the declared path is ignored (no execution, no note).
Probe `culture-d2b` fails the same way for D2 (`assembly.generator: tools/assemble-d2.py`
beats the declaration).

*Why it works.* `declared_paths` (lines ~228-241) copies declaration keys through
`DECLARED_ALIASES`, and its dedup test is on the **alias**, not on the canonical key
(`if key in DECLARED_ALIASES and key not in declared`). Both `typed_pipeline.assembler`
and `assembly.generator` are therefore retained, and `resolve_config` then applies
each alias to the same canonical slot in iteration order, so the last one applied
wins. Both real packets in the lane carry `assembly.generator`, and no conflict is
refused — although `design.md` §0 promised "a conflict refusal when declaration and
flag disagree"; the implementation instead defines flags as silently overriding.

*Impact.* The declared channel the docstring advertises (`typed_pipeline.assembler`)
is dead for both committed packets, and which of two contradicting declarations wins
is an accident of iteration order. A reader — or a machine — that resolves the same
document can reach a different answer than the gate.

*Minimal fix.* Dedup by canonical key and refuse conflicting declarations (or emit a
`L1-declared-conflict` check item), then document the precedence explicitly.

### F3 (MEDIUM) — the identity leg is skipped when the resolved assembler is the D2 serializer, and the exemption is packet-controlled

*Evidence.* Probe `culture-d2` (D2 packet copy plus
`typed_pipeline: {assembler: tools/assemble-d2.py, expected: <scratch file>}`) at
10:42Z: the checks are `[L1-expected-holds, L1-assembler_identity, L1-build]` —
**no gate-level `L1-assembler`** — because `identity_requested` (lines 379-380) is
`(config["assembler"] != SERIALIZER) or bool(flags.get("assembler"))` and the
resolved assembler equals `tools/assemble-d2.py`. The tampered packet was still
refused, but by the D2 adapter's own `assembler_identity` record, not by the gate leg.

*Impact.* For the D2 pipeline the exemption is compensated by the adapter; for any
future family whose declared adapter lacks an equivalent check, a tampered packet
would get no assembler verification at all, and the gate would not say so. A packet
can also *choose* the exemption by declaring the D2 serializer.

*Minimal fix.* Run the identity leg whenever `generalized`, or surface the exemption
as an explicit check/note item so the reading is legible.

### F4 (LOW) — the expected-hold set becomes packet-supplied on generalized runs

`resolve_config` lets a packet (or `--expected`) replace the embedded 15-hold
constant, and `L1-expected-holds` accepts any internally consistent file. Probes
1/2/4 all resolved `expected` to this seat's scratch file and graded against it. The
packet's bytes still have to satisfy the declared adapter/assembler, but a packet
shipping its own expected set makes L3 vacuous. Fix: pin the expected file's digest
(registry again) or refuse a packet-declared expected outside
`examples/culture-<family>/`.

## 3. Pin-confusion review of the cascade — what held

| control | reading (stamp) | verdict |
|---|---|---|
| filed round-11 generation untouched | `MANIFEST.tsv aad230bf…`, `run-receipt c49ebc9e…`, `run.log 9a69985a…` identical before/after (10:42:59Z) | held — supersession is a **new file** |
| live round-11 replay | 10/11, row 1 `gate_digest_mismatch` (row pins `d102fd1d…`, live gate `286d6e82…`), 10:43Z | honest reading; the historical-pin class of `reports/round-10/drift/fix-18.md` |
| round-11 replay at the filed pin | iso tree with the gate restored from `HEAD`, `--repo-root <iso>` → **11/11 exit 0**, 10:37Z | held |
| new re-pin generation | `tools/gates/frozen/round-18/repin-d2/MANIFEST.tsv` `85d75c9a…`, row 1 pins `286d6e82…`, replay **11/11 exit 0** at 10:43:09Z and 10:46:00Z (the file was authored at `reports/round-18/repin/MANIFEST.tsv`, same bytes, and moved by its owner ~10:45Z) | held |
| round-3 replay (isolated) | 7/7 + 7/7 exit 0 with the six gates restored from `291c714`, 10:36–10:39Z | held |
| round-9 baselines | 8 `r9-pre` files unchanged; 7 new `r18-post` baselines, 0 pin values moved; battery `8 → 15` baselines, all pinned, exit 0 | held — new revision, not a rewrite |
| round-16 v2-07 | filed `expected-v2-07.json dc75c5d7…` unchanged; successor `expected-v2-07-r18.json d5fda399…`, 0 of 28 input pins moved | held |
| filed rounds 8–17 | `git status --porcelain reports/round-{8..17}` empty at 10:42Z | held |

**The one fragile point, stated plainly:** the re-pin manifest pins a gate revision
that was already superseded twice inside this window (the cascade table itself
records `ea95e2a1… → a201afee… → 286d6e82…`). My 11/11 reading holds only for
`286d6e82…`; the next gate edit turns it into a `gate_digest_mismatch` until the
owner re-freezes. **The integrator must re-run
`TMPDIR=<outside-repo> python3 tools/replay-frozen.py tools/gates/frozen/round-18/repin-d2/MANIFEST.tsv`
after the final gate revision lands, and a further change is another new re-pin, never
an edit.**

A construction hazard worth recording: two new `*.py` files now sit under
`tools/gates/` (`d4-assembly-check-gate.py`, `d4-typed-labels-check-gate.py`). They
are legitimate replay targets, but the battery's seven-name constant does not cover
them, and some validators derive their gate-stem set from `glob('*.py')`; the
round-11 README documents that an `expected.json` naming a gate outside the constant
makes the battery fail closed (`BASELINE-GATE-UNKNOWN`). Today the battery is exit 0
with 15 pinned / 7 covered — no defect; the hazard is for whoever files a baseline for
the new gates under a battery root.

## 4. Limits

- Engineering review of a moving revision; findings were reproduced twice (10:33Z
  `ea95e2a1…`, 10:42Z `286d6e82…`) plus the default-path control before the change,
  but a later edit can change the code under review — re-run the probes named in §1
  after the integrator's final run.
- Not reviewed here: D4-path negatives (owned by R18-O11..O14), the D4 adapter gap
  (`FAIL L1-build: adapter missing: tools/assemble-d4-typed.py` at the stamp), the
  civ-map revision. Exit 0 anywhere is reproduction, never clearance; the D2 hold set
  (15 holds + 1 note) and every D4 hold remain open design debt.
- No file outside `reports/round-18/gate/{regression,reviews}.md` and this seat's
  `.scratch/` tree was written; no in-lane artifact was mutated by any probe.
