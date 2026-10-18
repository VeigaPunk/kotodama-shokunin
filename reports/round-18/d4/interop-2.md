# R18-D15 — interop 2/3: assembler checks and the standing regression set

- round 18 (operator: loop 2 of 3, build round 2 of 4; `reports/round-18/claims.json`,
  claim **D**, shard **D15**). Lane: `kotodama-shokunin`.
- assignment (verbatim): "D R18-D14..D16 (interop x3): D2 path (typed gate on D2
  packet) verdict identical to round-11's recorded verdict; d2/d3 assemblers
  --check green; battery green; reports/round-18/d4/interop-{1..3}.md."
- date: 2026-10-18. Evidence window 10:20:00Z–10:22:30Z UTC. Reference revision
  HEAD `c66ac3c951b346a2a56f9386e3324b4f5fe33902`. Baseline `3dd37542…` (round-17).
- canon: NON-CANON engineering evidence.
- writes: **this file only** plus gitignored scratch under `.scratch/r18interop*`
  (TMPDIR exported before every scratch-writing command). No earlier-round byte
  edited; no commit, no push.

## 0. Verdict

**GREEN — both named assemblers `--check` exit 0 with byte-recorded stdout
identical to round-11's own recording, and all 13 commands of the lane's
standing regression set exit 0 with empty stderr.** Twelve of the thirteen
stdout sha256 values match a previous round's recorded value exactly (the
exception is the battery binary run, whose stdout embeds its temp mirror path
and is documented non-byte-stable — `reports/round-15/rerun.json`
`battery_stdout_stability_probe`).

The sha comparisons are the point: this is not "commands exit 0 today" but
"the same bytes as when the capability was admitted".

## 1. The named assemblers

| command | exit | stdout sha256 (2026-10-18) | recorded reference | reading |
|---|---|---|---|---|
| `python3 tools/assemble-d2.py --check` | 0 | `2fa0c8c197459f549de2f0822b8895477e27dcce38def75e18346ba6d672e386` | r11 `validation.json` claims.D assembly.assembler_check = same sha; r14/r15 regression row 6 = same sha | **byte match** |
| `python3 tools/assemble-culture-d3.py --check` | 0 | `e20620fabdf285323c021ae11cad32b1ece58a28d59dd74f7df237578ffb560a` | r11 `validation.json` interop_d3.d3_assembler_check = same sha; r14/r15 regression row 10 = same sha | **byte match** |
| `python3 tools/assemble-d2-typed.py --check` (adapter, adjacent) | 0 | `e3b16d3bae56cce5760cbde277716263636a4d9fad83c5c5f2f9a05b181bc924` | r14/r15 regression row 12 = same sha | **byte match** |
| `python3 tools/d2-typed-labels.py --check` (projector, adjacent) | 0 | `17064af53c48304def6b2a5f5c80c10161182b5715678a61d6d5b0d80e1ef427` | r11 `validation.json` claims.D typed_projection_check = same sha; r14/r15 row 8 = same sha | **byte match** |
| `python3 tools/assemble-culture-d4.py --check` (not in the standing set) | 0 | — | — | green |

Verbatim stdout:

```
packet.d2.yml: byte-identical deterministic assembly
packet.json: byte-identical deterministic assembly; packet.gates.yml: byte-identical deterministic assembly
examples/culture-d2/packet.d2.typed.yml: byte-identical deterministic typed packet
examples/culture-d2/typed-labels.d2.yml: byte-identical deterministic projection
packet.d4.yml: byte-identical deterministic assembly
```

`assemble-d2.py --check` also matters for the typed-pipeline gate's
`L1-assembler_identity` leg — the leg the round-18 generalization widens. Its
input pins were re-hashed at 10:19Z (`interop-1.md` §2) and match round-11's
frozen receipt.

## 2. The 13-command standing regression set (r14/r15 set, re-run 1:1)

Reproduced with file redirection (not shell command substitution — trailing
newlines matter for byte comparison). Run 2026-10-18 ~10:22Z, repo root,
`TMPDIR=$PWD/.scratch/r18interop-reg2`.

| # | command | exit | stderr | stdout sha256 (this run) | reference | reading |
|---|---|---|---|---|---|---|
| 1 | `python3 tools/check-gate-battery.py --selftest` | 0 | empty | `2812a3270ce97583eaa9a7a16f78f95c60e703b00076fd2fc95f0802783442c2` | r14/r15 = same | byte match |
| 2 | `python3 tools/check-gate-battery.py` | 0 | empty | `0d2d14503929e7b814840406c07a3ad97202c70d895796d7b67b13312233d710` | r14 `7b1485cb…`, r15 `12f7947b…`, r15 note: not byte-stable | exit-level match; non-stable by design (mirror path inside the JSON). Summary green — `interop-3.md` §1 |
| 3 | `python3 tools/check-craft-exercise.py --selftest` | 0 | empty | `77d408e10a494fa58fcaa5872d7ad20b6daaa9c5725329d1a0ae65ab8f0e7d32` | r14/r15 = same | byte match |
| 4 | `python3 tools/check-craft-exercise.py examples/supplement-opencode-1/sound-change-vs-taboo.json` | 0 | empty | `18128adfc703fd268ec70684f35a2a05b3257faf4b31add8f21b3313ad4a2650` | r14/r15 = same | byte match |
| 5 | `python3 tools/assemble-d2.py --selftest` | 0 | empty | `a81294c0347660d9b46952146bac967fc80c79c9d629d7f34e69d0411bec0336` | r14/r15 = same | byte match |
| 6 | `python3 tools/assemble-d2.py --check` | 0 | empty | `2fa0c8c197459f549de2f0822b8895477e27dcce38def75e18346ba6d672e386` | r14/r15 = same | byte match |
| 7 | `python3 tools/d2-typed-labels.py --selftest` | 0 | empty | `7231139c5b06089866270f4869caa1ffe04a4011502014979c996c9b1ab83252` | r14/r15 = same | byte match |
| 8 | `python3 tools/d2-typed-labels.py --check` | 0 | empty | `17064af53c48304def6b2a5f5c80c10161182b5715678a61d6d5b0d80e1ef427` | r14/r15 = same | byte match |
| 9 | `python3 tools/assemble-culture-d3.py --selftest` | 0 | empty | `91a0653948d48a10f6bd84af7adb3dd4cda3b25e8a15a77a3bf2cd92a4deac2b` | r14/r15 = same | byte match |
| 10 | `python3 tools/assemble-culture-d3.py --check` | 0 | empty | `e20620fabdf285323c021ae11cad32b1ece58a28d59dd74f7df237578ffb560a` | r14/r15 = same | byte match |
| 11 | `python3 tools/check-evidence-coupling.py --selftest` | 0 | empty | `cf62bc50e303b793b6b930c83a5ddd7d462c39cc39fef133385db830c1d380ce` | r14/r15 = same | byte match |
| 12 | `python3 tools/assemble-d2-typed.py --check` | 0 | empty | `e3b16d3bae56cce5760cbde277716263636a4d9fad83c5c5f2f9a05b181bc924` | r14/r15 = same | byte match |
| 13 | `python3 tools/gates/typed-pipeline-gate.py --json` | 0 | empty | `19765ddf2c36a7db5d71bd262079d6164b24f6222d9df83d0cefdeaeb8f47e62` | r11 `validation.json` e2e rerun, r12 recount ledger, r14/r15 = same | byte match |

Totals: **13/13 exit 0; 13/13 stderr empty** (sha
`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` on every
child — the same value r14/r15 recorded as "empty on every child");
**12/12 commands with a byte reference match exactly**.

Recorded runner: `.scratch/r18interop/regression2.sh` (scratch, not a
deliverable; per-command outputs under `.scratch/r18interop/reg/`).

## 3. Selftest counts observed

- `tools/gates/typed-pipeline-gate.py --selftest` → 12/12 checks passed
  (constant==expected-holds.json both directions; positive exit 0; banner;
  15/1 line counts; determinism; `--json` one document 16 findings; the
  smuggled-label, dropped-row, laundered-hold, adapter-drift, malformed and
  missing controls) — same 12/12 as round-17's record
  (`reports/round-17/d4/typed-run.md` §3).
- `tools/assemble-d2.py --selftest` / `assemble-culture-d3.py --selftest`
  outputs byte-match r14/r15 (rows 5, 9 above); `d2-typed-labels.py
  --selftest` byte-matches (row 7).

## 4. Boundary — what this does NOT prove

- Observations are at the round-11-frozen gate sha `d102fd1d…`; the claim-O
  generalization had not landed during this window (`interop-3.md` §3 watch
  log). The D2-path rows here must be re-run after that change; the re-run
  recipe is in `interop-3.md` §4 and `interop-1.md` §5.
- `--check` legs prove byte-identical deterministic assembly of the committed
  artifacts; they do not re-verify any baseline's verdict (that is the frozen
  replay's job, `interop-3.md` §2).
- Row 2's non-stability is documented behaviour, not a finding against this
  round: the battery is judged by its JSON summary and exit code.

---

## 5. Post-change re-run — appended 2026-10-18 (10:35Z, 10:42Z)

Claim O's generalization changed `tools/gates/typed-pipeline-gate.py` after the
table in §2 was taken. Re-run of the gate-dependent and assembler rows:

| command | exit | stdout sha256 now | reading |
|---|---|---|---|
| `python3 tools/assemble-d2.py --check` | 0 | `2fa0c8c1…6d672e386` (unchanged) | byte match to r11/r14/r15 |
| `python3 tools/assemble-culture-d3.py --check` | 0 | `e20620fabdf28532…ffb560a` (unchanged) | byte match to r11/r14/r15 |
| `python3 tools/gates/typed-pipeline-gate.py --json` | 0 | `19765ddf…8f47e62` (unchanged) | byte match to r11/r12/r14/r15 — the D2 path is untouched by the generalization |
| `python3 tools/check-gate-battery.py` | 0 | non-stable by design | summary green; **now 15/15 baselines pinned** (the re-pin cascade's seven `tools/gates/frozen/*/r18-post/expected.json` baselines landed), `gates_uncovered []`, `findings []` |

The remaining rows of the §2 set do not execute the typed-pipeline gate; a full
13-row re-run after the wave settles is the parent's post-settle step (recipe in
`interop-3.md` §4/§6). The three D2 identity artifacts stayed byte-identical at
every generalized revision tested (`interop-1.md` §6).
