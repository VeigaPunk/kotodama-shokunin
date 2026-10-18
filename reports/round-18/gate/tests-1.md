# R18-O11 — default-path byte-identity: the D2 gate verdict is unchanged

- round: 18 (operator loop 2 of 3, build round 2 of 4; 64 workers on
  `opencode-go-2/deepseek-v4.1-flash`) · shard: **O11** (tests ×4, claim O
  `gate-generalization`) · owner: L2 worker, kotodama-shokunin lane.
- assignment (verbatim): "O R18-O11..O14 (tests x4): default-path byte-identity
  proof (D2 gate verdict unchanged before/after on the same D4-untouched
  inputs); D4-path positive; D4-path negatives (forged assembler pin rejected,
  stale packet rejected); selftest additions;
  reports/round-18/gate/tests-{1..4}.md."
- date: 2026-10-18. Baseline revision `c66ac3c` (`reports/round-18/claims.json:6`
  names `3dd3754207032cb81f5fb3e202fe85cf79211339`; `c66ac3c` is its child and
  is the round-18 declare — it changes only `reports/round-18/{claims,targets}.json`,
  `git show --stat c66ac3c`). Measurements stamped 10:19–10:25Z.
- canon: NON-CANON engineering evidence. No culture design, no canon record, no
  handoff, no real-world clearance or rights statement is made here.
- writes: **this file only** plus gitignored scratch under `.scratch/r18-o11/`
  (`export TMPDIR=$PWD/.scratch` preceded every scratch-writing command; the
  one exception is the frozen-replay mirror, which `tools/replay-frozen.py`
  refuses to place inside the repo by design — see §2). No tool, gate, packet,
  projection, manifest, receipt or earlier-round byte is edited by this seat.
  No commit, no push.
- **status: COMPLETE — the generalized gate is byte-identical on the default
  path.** §3/§4 are the pre-change half (measured at the baseline revision
  `d102fd1d…`); §6 is the after half, measured at the landed generalized
  revision `d4785d9a…`. The two halves are the same three invocations, the same
  comparison, the same recorded round-11 verdict.

## 1. What is measured

Claim O's regression half: "the default D2 gate path must remain byte-identical
in behavior — regression-proof everything" (verbatim from the round-18 task
brief); claim O's own text: "Generalized gate: the assembler-identity leg
accepts a declared assembler pin (packet-declared or flag), default D2 behavior
byte-identical" (`reports/round-18/claims.json:14`).

Two independent halves, because either alone is weak:

1. **Direct** — pin the pre-round-18 gate bytes, run the same three D2
   invocations under the pinned revision and under the working-tree revision,
   and compare stdout bytes and exit codes. Byte equality of stdout is the
   strongest available statement of "unchanged behavior" for a gate whose
   entire interface is stdout, an exit code and the files it reads.
2. **Recorded** — replay the round-11 frozen manifest with **only** the
   typed-pipeline row's `gate_sha256` cell re-pointed at the live gate bytes.
   The row's recorded exit (`0`), recorded finding count (`15`) and recorded
   output bytes (`tools/gates/frozen/round-11/typed-pipeline/run.log`,
   `sha256 9a69985a…`) are left at their round-11 values. Green therefore means
   the re-pin is a digest change and not a verdict change.

## 2. Method (scratch-only, no live-tree write)

- Pinned revision: `git show c66ac3c:tools/gates/typed-pipeline-gate.py` →
  `.scratch/r18-o11/typed-pipeline-gate.pre.py`, sha256
  `d102fd1dd1bae3cc4c9d0ea33844b2f706a2098707938c82c75ce9fb6368e27d` — equal to
  the working-tree file at measurement time (§3 pins).
- Two isolated mirrors of the working tree, composed by `tar` with `.git`,
  `.scratch`, `out` and `__pycache__` excluded (driver:
  `.scratch/r18-o11/byte_identity.py`). `mirror-pre` then has its gate file
  replaced by the pinned pre bytes; `mirror-live` keeps the working-tree bytes.
- Three invocations per place (`tree` = the real repo, `mirror-live`,
  `mirror-pre`), run with cwd = that place, `PYTHONDONTWRITEBYTECODE=1`,
  `TMPDIR=$PWD/.scratch`:
  1. `python3 tools/gates/typed-pipeline-gate.py` (the default D2 path),
  2. `… --json`,
  3. `… tools/gates/frozen/round-11/typed-pipeline/packet.d2.typed.yml` (the
     frozen typed-packet path the round-11 manifest exercises).
  Stdout is captured verbatim to `.scratch/r18-o11/stdout/<label>-<place>-<name>.txt`
  and its sha256 recorded in `.scratch/r18-o11/receipt-<label>.json`.
- Frozen replay: `.scratch/r18-o11/repin_replay.py <label>` writes a **copy** of
  `tools/gates/frozen/round-11/MANIFEST.tsv` to
  `.scratch/r18-o11/MANIFEST-repin-<label>.tsv` with the `gate_sha256` cell of
  the `tools/gates/typed-pipeline-gate.py` row substituted (the filed manifest
  is never opened for writing), then runs
  `python3 tools/replay-frozen.py <copy> --json`. `TMPDIR=/var/tmp/kotodama-r18-o11`
  because `replay-frozen.py` exits 2 with `mirror_unsafe` when its temp root is
  inside the repo — documented in `tools/gates/frozen/round-11/README.md`
  ("TMPDIR must be outside the repo"). Receipt:
  `.scratch/r18-o11/repin-receipt-<label>.json`.

## 3. Receipts — the nine runs (2026-10-18, 10:20–10:24Z)

All nine runs **exit 0**. stdout sha256:

| invocation | tree | mirror-live | mirror-pre | bytes |
|---|---|---|---:|---:|
| default (no args) | `15cdfbda…2e695b` | `15cdfbda…2e695b` | `15cdfbda…2e695b` | 2677 |
| `--json` | `19765ddf…8f47e62` | `19765ddf…8f47e62` | `19765ddf…8f47e62` | 8643 |
| frozen round-11 typed packet | `9a69985a…14ada4606` | `9a69985a…14ada4606` | `9a69985a…14ada4606` | 2604 |

Comparisons asserted by the driver, all **true** (6/6): `tree vs mirror-pre` and
`mirror-live vs mirror-pre` for each of the three invocations, on stdout sha256
**and** exit code.

Input pins at measurement time (`.scratch/r18-o11/receipt-t0.json`,
`tree_pins`), each equal to the pin already filed for it:

| input | sha256 | filed pin it equals |
|---|---|---|
| `examples/culture-d2/packet.d2.yml` | `e0f21509…137b643` | `expected-holds.json` `packet_sha256` |
| `examples/culture-d2/typed-labels.d2.yml` | `a3aa452c…e8364a43` | `expected-holds.json` `projection_sha256` |
| `examples/culture-d2/expected-holds.json` | `a5dc26d5…10d6dde3a` | — (the committed baseline itself) |
| `examples/culture-d2/packet.d2.typed.yml` | `1b5010b7…2dfac8a3` | round-11 manifest row 1 `input_sha256` |
| `tools/assemble-d2.py` | `8ea6bdde…822c8655d` | — |
| `tools/d2-typed-labels.py` | `0da0015f…487fb89c802` | `expected-holds.json` `projector_sha256` |
| `tools/assemble-d2-typed.py` | `c7e5a749…250b037071` | live L4 pin target |
| the five reader gates | `d9e4e8f4…` / `d5fe087f…` / `e6bffd70…` / `2c4dd397…` / `5368b135…` | round-11 manifest `gate_sha256` cells |

**The D2 inputs are D4-untouched**: every D4 artifact named in claims D/C lives
under `examples/culture-d4/`, `tools/assemble-culture-d4.py` and
`reports/round-1{7,8}/`; no D2 input above is read or written by the D4 path
(`grep -rn "culture-d2" tools/assemble-culture-d4.py` → 0 hits, rerun at
10:24Z). The 13 pinned files hash identically **before and after** the nine
runs — `tree_untouched: true` in the receipt.

Baseline selftest, pre-change gate: `python3 tools/gates/typed-pipeline-gate.py
--selftest` → exit 0, `selftest: 12/12 checks passed` (10:23Z). This is the
count that the additions in `tests-4.md` must keep green.

## 4. Receipt — frozen re-pin replay (before)

`python3 .scratch/r18-o11/repin_replay.py before` (10:24Z), receipt
`.scratch/r18-o11/repin-receipt-before.json`:

- repin line: `d102fd1d… -> d102fd1d…` (the live bytes *are* the pinned bytes at
  this stamp — the substitution is a no-op until the generalization lands),
- `REPLAY OK`: **11/11 rows reproduced**, `could_not_evaluate: 0`,
  `mismatch: 0`, exit 0,
- the typed-pipeline row (line 2): `exit 0/0`, `count 15/15`, `bytes_match: true`
  — the recorded `run.log` bytes and the freshly observed bytes are identical.

The filed manifest also replays green **unpatched** (same command without the
substitution, 10:21Z): `REPLAY OK: 11/11 rows reproduced`. So the baseline is
green both as filed and under a re-pin, and the only column a re-pin may move
is the gate digest.

**Expected post-generalization reading, so it is not misread as drift.** Once
the generalized gate is in the tree, the *filed* round-11 manifest replays
**10/11 with one `gate_digest_mismatch`** on its typed-pipeline row — by design:
that row pins `d102fd1d…` and the live gate is `286d6e82…`, and
`tools/replay-frozen.py` refuses a row whose on-disk gate bytes are not the
pinned revision. The filed verdicts are intact and are reproduced two ways: by
isolating the replay at the filed pin (an iso tree carrying the `HEAD` gate
bytes → 11/11, exit 0), and by the round-18 re-pin generation, which is the
append-only fix for exactly this (row 1 pins `286d6e82…`, replay 11/11, §6). This
seat measured the unpatched 11/11 *before* the generalization landed (10:21Z)
and the re-pinned 11/11 after (10:24Z, 10:34Z, 10:39Z, 10:42Z); the
`gate_digest_mismatch` reading of the filed manifest against the live gate was
independently recorded by the O seats in `reports/round-18/gate/regression.md`
§2 row 4 (10/11), with the same cause.

## 5. What this does not say

- Byte-identity is asserted for **these three invocations** of the default D2
  path on the pinned inputs. A future default-path invocation not covered here
  (a new flag, a new input class) is not covered by this proof; the selftest and
  the battery are the standing nets for those (`tests-4.md`).
- `9a69985a…14ada4606` is the round-11 **recorded** output and it is reproduced,
  which is reproduction, not clearance: the default path stays red at the design
  level (15 open holds), exactly as `tools/gates/frozen/round-11/README.md`
  states ("A reproduced red verdict stays red").

## 6. The after half — the generalized gate, measured

Landed revision: `tools/gates/typed-pipeline-gate.py` sha256
**`d4785d9afc0306afb0a9c78c3c2b014097090413bf9c889ed72fa9558c394ba0`**
(38352 bytes at the first read; the O seats wrote the file in several steps
between 10:26Z and 10:34Z — the intermediate digests `2a08fb2d…`, `b4232690…`,
`a2948ebb…`, `edfec5f3…`, `3897833101…`, `5b4501a9…` are recorded in
`tests-3.md` §3). Both drivers were re-run unchanged at 10:34Z, with the gate sha
re-hashed immediately before and after each run and identical, so one revision
was measured end to end.

| # | command (lane root, `TMPDIR=$PWD/.scratch`) | receipt | observed |
|---|---|---|---|
| 1 | `python3 .scratch/r18-o11/byte_identity.py after` | `.scratch/r18-o11/receipt-after.json` | `gate_live_sha256 d4785d9a…` ≠ `gate_pre_sha256 d102fd1d…` (the change landed); **6/6 comparisons true**; all nine runs **exit 0**; stdout digests exactly the §3 values (`15cdfbda…`, `19765ddf…`, `9a69985a…`); `tree_untouched: true` |
| 2 | `python3 .scratch/r18-o11/repin_replay.py after` | `.scratch/r18-o11/repin-receipt-after.json` | substituted digest `d4785d9a…`; **REPLAY OK: 11/11 rows reproduced**, `could_not_evaluate 0`, `mismatch 0`, exit 0; typed row `exit 0/0`, `count 15/15`, `bytes_match: true` |
| 3 | `python3 tools/gates/typed-pipeline-gate.py --selftest` | `tests-4.md` §3 | exit 0, **12/12** — the baseline control set is intact |

**Re-measured at the last revision of the window** (10:39Z, sha256
`84dc177e79688e0ed7f323ead42233205b7df7c68183d434bd32a906d647bad4`, unchanged
across both runs; receipts `byte_identity.py final` →
`.scratch/r18-o11/receipt-final.json`, `repin_replay.py final` →
`.scratch/r18-o11/repin-receipt-final.json`): **6/6 comparisons true, all nine
runs exit 0, `tree_untouched: true`**, and the re-pin replay again
**11/11 reproduced** with the typed row `exit 0/0`, `count 15/15`,
`bytes_match: true`. Two revisions of the generalized gate now carry the same
proof; the §5 caveat is therefore a re-run rule, not an open question.

**Reading.** The pre-generalization bytes and the generalized bytes emit the same
stdout bytes and the same exit codes on all three default-path invocations, and
the round-11 recorded verdict reproduces under the new gate with **only** the
manifest's `gate_sha256` column re-pointed (§4 vs §6 row 2). That is the claim-O
requirement — "default D2 behavior byte-identical" — measured, not argued.

Caveats, stated rather than hidden: the identity is asserted for revisions
`d4785d9a…`, `84dc177e…` and `286d6e82…`; a later O-seat edit invalidates it
until the two drivers are re-run (the commands do not change), and a new
default-path invocation (a new flag, a new input class) is outside this proof's
scope — the selftest and the battery are the standing nets for those
(`tests-4.md`).

**Re-measured once more before this file was closed** (10:42Z, sha256
`286d6e82711427ea03a9a42e5cb10f6c369f0f1b0cd589c74a4092f3b8c12af9`, unchanged
across both runs; receipts `byte_identity.py last` →
`.scratch/r18-o11/receipt-last.json`, `repin_replay.py last` →
`.scratch/r18-o11/repin-receipt-last.json`): again **6/6 comparisons true**, all
nine runs **exit 0**, stdout digests `15cdfbda…` / `19765ddf…` / `9a69985a…`,
`tree_untouched: true`; re-pin replay **11/11 reproduced**, exit 0. Three
revisions of the generalized gate now carry the same verdict-identity proof.

**The re-pin cascade itself, verified.** The O seats landed the round-18 re-pin
as a **new** manifest directory, `tools/gates/frozen/round-18/repin-d2/`
(`MANIFEST.tsv` sha256 `85d75c9a1a7c937de2860ad9fdf25f62e6a6b0be7f3b2650ee04230860b52c8c`,
11 rows) whose typed-pipeline row pins the generalized gate
`286d6e82…` with `exit_code 0`, `finding_count 15`; the round-11 manifest is
byte-untouched (`aad230bfdcc1bfe4cc137339b47daf0154208b6c69225e0c0a4505ce52532063`,
`git status --short` → no modification), i.e. append-only held. My independent
replay of the new manifest (`TMPDIR=/var/tmp/kotodama-r18-o11`, required because
`tools/replay-frozen.py` refuses in-repo mirrors): **REPLAY OK: 11/11 rows
reproduced**, exit 0 — the same recorded round-11 verdicts, now under the pinned
generalized bytes. The round-18 D4 manifest
(`tools/gates/frozen/round-18/MANIFEST.tsv`, two rows pinning
`d4-typed-labels-check-gate.py` and `d4-assembly-check-gate.py`) also replays
**2/2 reproduced**, exit 0 (10:43Z, same TMPDIR rule).
