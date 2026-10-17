# R8-D06 — `d2-typed-labels` selftest + control receipt

- round: 8 (loop 1 of 3, build round 1 of 4); shard DEPTH R8-D06 (tests)
- date: 2026-10-17; receipts stamped UTC below
- lane: kotodama-shokunin; all commands run from the lane root
- tree HEAD: `cf338a713060f274269cdacb18cdc0085bb06aeb`; python 3.14.7
- environment note: `/tmp` is a 16G tmpfs that hit **0 free inodes** during
  this round (`df -i /tmp`: 1048576/1048576, 100%), so temp-writing runs can
  fail with "No space left on device" despite free space. Use
  `export TMPDIR=/var/tmp` (root btrfs, 782G free) for re-runs — note that the
  prefix form `TMPDIR=/var/tmp out=$(...)` does **not** redirect, because the
  command substitution runs before the assignment takes effect; the receipts
  below were taken while `/tmp` still had inodes available.

Scope: this shard tests the tool and records receipts. It writes no tool, no
example, no SKILL text. Where a leg could not be evaluated, it is stated as
such, never as a pass.

## 0. Revision churn during dispatch (why the receipts are revision-bound)

`tools/d2-typed-labels.py` was still being written while this shard polled.
Measured states, in order (`sha256sum tools/d2-typed-labels.py`):

| revision sha256 | lines | observed |
|---|---|---|
| `080a3b2f2753e50eaab2f94273c107ce7866749c6b0dba9de6ac26aa1d216d28` | 1,349 | `--selftest` exit 1, **26/30**; stdout sha256 `34ea49abd30d16e53238429924346f380f7d85874bcd01b761fbabee6fc41011` (byte-identical on two runs). FAILs: unreadable `maps_to` diagnostic, unknown institution id accepted, `'(translated label)'` and `'label (analyst label)'` accepted |
| `429191fd14e01d52c208b0ad7dffdf79f034e430760caf60f12b1859b63725aa` | 1,455 | `--check` crashed: `TypeError: eras_of() missing 1 required positional argument: 'tag_space'` |
| `623b5b1f2f9f50b3e306975b4107b5f70122e86e7d7b41aeca21bcb5a7979b03` | 1,455 | **fully tested revision** (stable at `20:23:48Z`): selftest 32/32 green, independent control 6/6, `--check` exit 0 — receipts in §1–§5 |
| `5d87d346…`, `9e84c548…`, `6a80ffe4…`, `3adbdeb7…` (2,487–2,604 lines) | 2,487+ | rework in progress: two `def selftest()` (line 1354 and a second one) plus trailing `selftest_rank_block = selftest` → the later `selftest()` calls the alias of itself → `RecursionError`, exit 1. CLI changed mid-rework (`--report` dropped, `--check [PATH]` added) |
| `11e23ca9d77f66f5a95bfabeed48e253ddcdb37308b9bd204d81dd33c1c24b41` | 2,665 | **state at write time** (`20:29:33Z`): `--check` exit 0 (`byte-identical deterministic projection`); `--selftest` exit 1 with `FileNotFoundError: <tmp>/repo/examples/culture-d2/typed-labels.d2.yml` (the fixture mirror does not build/copy the artifact it then reads); stdout sha256 `9630c56ae951c2b8edfa4c35662d9103f5049051f7075d80416a247058eb6b85` |

The churn means: the receipts in §1–§5 bind only to revision `623b5b1f`;
the delivered revision at write time is `11e23ca9` and its `--selftest` is
**red**. Re-run recipe for the integrator after the wave settles:

```sh
export TMPDIR=/var/tmp
sha256sum tools/d2-typed-labels.py
python3 tools/d2-typed-labels.py --selftest; echo "exit=$?"
python3 /var/tmp/r8d06/control.py; echo "exit=$?"
python3 tools/d2-typed-labels.py --check; echo "exit=$?"
```

## 1. Selftest — green on the fully tested revision `623b5b1f`

```sh
python3 tools/d2-typed-labels.py --selftest
# exit=0
# stdout sha256: 4818583d55e9e4691e2978c5f43ec2366f6edd463a89868f60ddf66bd5a24642
```

Final line, verbatim:

```
selftest: 32/32 checks passed — fixture CLI build/--check/tamper plus malformed span, unclassified rule, unreadable maps_to, unknown institution, label-parser and reconciliation-refusal controls; no file outside the temporary directory touched
```

The tested revision's sha256 was verified identical immediately before and
after the whole battery.

## 2. Independent positive control (outside the tool's fixtures)

Script: `/var/tmp/r8d06/control.py` (sha256 in §6) — mirrors the four
components the tool reads, the packet, the tool and the costume gate into a
`TemporaryDirectory`, then exercises the cases below; writes only under that
directory.

```sh
python3 /var/tmp/r8d06/control.py
# exit=0; output sha256: 936d664416881cd14824c0ee85a78bf88d3c04660d0a3af524ab64c6c65bfd31
```

| case | result |
|---|---|
| P-build | exit 0; artifact written (68,643 bytes) in the mirror |
| P-check | exit 0; `typed-labels.d2.yml: byte-identical deterministic build` |

## 3. Independent malformed-input controls

| case | expected | observed |
|---|---|---|
| M1 adaptation span dropped from `12-rank-rules.yml` | exit 2, no traceback | exit 2 — `d2-typed-labels error: adaptation for WR-02 cites a span that is not in prescription: 'None but a registered herd-master shall wear lowland-woven cloth'` |
| M2 institution id `(WI-2)` → `(WI-99)` in `11-costumes.yml` | exit 2, no traceback | exit 2 — `d2-typed-labels error: costumes[GAR-02]: unknown institution id(s) WI-99` |
| M3 end-to-end malformed annotation appended to a garment value | exit 2, no traceback | exit 2 — `d2-typed-labels error: unknown label kind 'analyst label' in 'winter valley coat (heavy felted wool; uncombed finish optional) (analyst label)'; known kinds: na…` |
| M4 five malformed parser strings in-process | each raises `Malformed` | all five `refused` |

No traceback appeared in any case; every refusal is a one-line stderr
diagnostic with exit 2.

## 4. Determinism legs (tested revision)

### 4.1 The typed-labels artifact

```sh
python3 tools/d2-typed-labels.py --check
# exit=0; "examples/culture-d2/typed-labels.d2.yml: byte-identical deterministic build"
sha256sum examples/culture-d2/typed-labels.d2.yml
# 820b75352fb0f20d3a76b523b202e6b8d4a8668f84a85f3fb78ebabb6422f778 (68,643 bytes)
```

(The artifact has since been regenerated by the rework; at `20:29Z` it was
`59a53456921f830243816a35dd4a1feb42d55ebe76253f9ba8f3fe2d749ab4d2` and the
then-current revision's `--check` still exited 0.)

### 4.2 The D2 example packet — `assemble-d2.py --check` red, cause pinned to claim O

```sh
python3 tools/assemble-d2.py --check
# exit=1; "packet.d2.yml differs from deterministic assembly"
sha256sum examples/culture-d2/packet.d2.yml
# 8da90b0788f86fd19babc67958715c8c16cb90a98e13572380b1c1892622b81e (unchanged from the 20:13Z baseline)
```

`tools/assemble-d2.py` is unmodified (`git diff` empty) and the components are
unchanged. Causal experiment in two mirrors differing only in the costume
gate, which the assembler imports via `runpy`:

| mirror | costume gate | `--check` | assembled packet sha256 |
|---|---|---|---|
| old | `git show HEAD:…` (pre-O-repair) | **exit 0** byte-identical | `8da90b07…` = live packet |
| new | live working tree (post-O-repair) | **exit 1** differs | `b74d8dca59c676d33a43b7400043c0c4eda690beb5b1ba780e4b6c07354b8b41` |

The two assemblies differ in **exactly one line**: the packet's recorded
`reader_sha256` (`29a9361c…` → `6be04578fc219949daf938838793c3413c152a7c4339ff867d32621ea228f8f7`).
The drift is the packet's self-recorded reader digest going stale when the
O-shard repaired the costume gate — not a content change. Regenerating the
packet (`python3 tools/assemble-d2.py`) after the gate repairs land resolves
it; until then O15's `run-validation.py` D-leg check `assemble-d2 --check
exit 0` reads red for a cause owned by claim O, not by the D2 tool.

## 5. Frozen replay — `tools/replay-frozen.py`

```sh
python3 tools/replay-frozen.py --selftest
# exit=0; "selftest: 79/79 checks passed"
# stdout sha256: 4d6aaea127ad99737b53ce50a7378efad5562b6fa01da88e9ca8610aa604ea16

python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv
# exit=2
# "REPLAY COULD-NOT-EVALUATE: 7 could-not-evaluate, 0 mismatch, 0 reproduced of 7 row(s)"
# stdout sha256: 76c00a6b80d4539a70ebe976d86600f8317b8da962a3ea6cdfcf8bace7e41f80
```

All seven rows report `reason=gate_digest_mismatch`: every gate in the
manifest was repaired by O-shards in this wave, so replay refuses to run them
(documented behavior: verify pinned bytes first; exit 2 has precedence). Not
D2-packet drift — replay reads the round-3 input snapshot, never the live
packet. Timeline: 7/7 reproduced at `20:11Z` (before repairs were visible),
6/7 + 1 mismatch at `20:14Z`, 7/7 could-not-evaluate at `20:24Z`. No round-8
frozen manifest for the D2 packet exists yet (`find reports/round-8
tools/gates/frozen examples/culture-d2 -name '*MANIFEST*'` → only round-3).
`reports/round-8/depth/docs.md` (D15) independently observed the same
fail-closed cause.

## 6. Summary (machine-readable)

```json
{
  "shard": "R8-D06",
  "date": "2026-10-17",
  "head": "cf338a713060f274269cdacb18cdc0085bb06aeb",
  "tested_revision": {"path": "tools/d2-typed-labels.py",
                      "sha256": "623b5b1f2f9f50b3e306975b4107b5f70122e86e7d7b41aeca21bcb5a7979b03",
                      "lines": 1455, "stable_across_battery": true},
  "write_time_revision": {"sha256": "11e23ca9d77f66f5a95bfabeed48e253ddcdb37308b9bd204d81dd33c1c24b41",
                          "lines": 2665, "measured_at": "2026-10-17T20:29:33Z",
                          "selftest_exit": 1,
                          "selftest_error": "FileNotFoundError: <tmp>/repo/examples/culture-d2/typed-labels.d2.yml",
                          "selftest_stdout_sha256": "9630c56ae951c2b8edfa4c35662d9103f5049051f7075d80416a247058eb6b85",
                          "check_exit": 0,
                          "note": "tool still being rewritten during dispatch; revision may have changed after this measurement"},
  "selftest": {"exit": 0, "passed": 32, "total": 32,
               "stdout_sha256": "4818583d55e9e4691e2978c5f43ec2366f6edd463a89868f60ddf66bd5a24642",
               "bound_to": "tested_revision"},
  "independent_control": {"script": "/var/tmp/r8d06/control.py",
                          "script_sha256": "60bd808d1ef01e864a49cfffd6256cf45d3b026ded3f48a79acae87708325ae3",
                          "exit": 0, "cases_passed": 6, "cases_total": 6,
                          "output_sha256": "936d664416881cd14824c0ee85a78bf88d3c04660d0a3af524ab64c6c65bfd31",
                          "bound_to": "tested_revision"},
  "determinism": {"typed_labels_check_exit": 0,
                  "artifact_sha256": "820b75352fb0f20d3a76b523b202e6b8d4a8668f84a85f3fb78ebabb6422f778",
                  "assemble_d2_check_exit": 1,
                  "drift_cause": "packet reader_sha256 line stale after O-shard costume-gate repair; old-gate mirror exits 0, new-gate mirror exits 1, assemblies differ in 1 line"},
  "replay": {"selftest_exit": 0, "selftest_checks": "79/79",
             "selftest_stdout_sha256": "4d6aaea127ad99737b53ce50a7378efad5562b6fa01da88e9ca8610aa604ea16",
             "manifest_exit": 2, "manifest_rows_reproduced": 0,
             "manifest_rows_could_not_evaluate": 7,
             "manifest_stdout_sha256": "76c00a6b80d4539a70ebe976d86600f8317b8da962a3ea6cdfcf8bace7e41f80",
             "round8_d2_manifest": "absent"},
  "environment": {"tmp_free_inodes": 0, "recommended_tmpdir": "/var/tmp"}
}
```

## 7. Limits

- The selftest's malformed controls are the tool's claims about itself; §3
  adds independently authored cases outside its fixtures. Neither proves
  arbitrary malformed-input safety.
- Determinism here means byte-identity of the typed-labels artifact and the
  packet-assembly leg; it does not certify the tool's design semantics.
- The packet-assembly drift and the replay fail-closed rows are cross-shard
  interactions with the O repairs, pinned with causal evidence; they are
  reported, not repaired here (out of this shard's write scope).
- The tool was still being edited when the churn states in §0 were measured;
  §1–§5 bind only to revision `623b5b1f`, and the delivered revision at write
  time (`11e23ca9`, `--selftest` red) is recorded in §0. The integrator must
  re-run the recipe there after the wave settles before treating the D claim's
  selftest leg as green.
