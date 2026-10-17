# neg-06 — negative control + repair receipt (shard R8-O06)

- **Round:** 8 · **shard:** R8-O06 (operability) · **claim:** O
- **Date:** 2026-10-17 (all commands below; consolidated evidence run at
  `checked_at_utc = 2026-10-17T20:32Z` and re-run after the scratch hardening)
- **Baseline:** declared `e7ca0fa…`; worktree HEAD `cf338a7` — the pre-fix
  bytes of all three repaired loaders are byte-identical at both revisions and
  equal review 26 §0's pins (hashes in §3), so the defect and its control bind
  to the declared baseline.
- **Role:** repair shard. Writes only the three repaired loaders, this
  directory's control/evidence, and this report. No commit.

## 0. Defect selection (index reconciliation)

Assignment: "defect index 2". Two numbering schemes exist on disk and both
point at review 26 §3 **D2** (duplicate mapping keys silently last-win):

- register order (1-based over `D1…D9`): index 2 = D2;
- `reports/round-8/operability/defect-inventory.json` `idx` field (per-file
  rows): idx 2 = `R26-D2-phonology`.

Sibling receipts show the register entry was split across shards: `neg-05`
repaired and controlled **R26-D2-phonology**, `neg-07` repaired and controlled
**R26-D2-naming** (its control docstring cites inventory id `R26-D2-naming`).
Grep at this shard's start showed the remaining three rows still carrying the
defect — `costume-era-consistency-gate.py`, `lexicon-coverage-audit.py`,
`myth-consistency-gate.py` had **no** duplicate-key check anywhere
(`grep -c "duplicate key"` → 0 / 0 / 1, the last being myth's pre-existing
block-mapping check). This shard therefore closed the remaining three loaders,
completing review 26's recommended move 2 ("reject duplicate keys uniformly in
block and flow mappings, and on the JSON path") for all five packet gates.

## 1. Defect and pre-fix reproduction

Review 26 §3 D2 (`reports/supplement-opencode-1/26-parser-controls.md:82-99`):
"Duplicate mapping keys silently last-win in 4 of 5 loaders — no diagnostic …
An author's stale key silently changes the audit outcome". Cited overwrite
sites: phonology `:416`, naming `:430`, costume `:274`, lexicon `:465`, myth
`:249` (flow mappings only); JSON paths silent in costume and lexicon.

Pre-fix reproduction on the pinned pre-fix bytes (`git show HEAD:…`), payload =
the live example packet plus one colliding key:

```
$ python3 <pre-fix>/costume-era-consistency-gate.py packet.yml   # duplicate `name:` appended
rc=0 (clean verdict, no diagnostic)
$ python3 <pre-fix>/lexicon-coverage-audit.py packet.yml         # duplicate `name:` appended
rc=0 (clean verdict, no diagnostic)
$ python3 <pre-fix>/myth-consistency-gate.py packet.yml          # duplicate flow key appended
rc=0 (clean verdict, no diagnostic)
$ python3 -c 'parse_packet("{\"name\": \"a\", \"name\": \"b\"}")'   # in-memory, costume/lexicon
returned {'name': 'b'}   # silent last-win, no error
```

A stale key produced a *clean* audit verdict. Defect confirmed on all three
loaders (block, flow, sequence-entry merge and JSON paths).

## 2. Repair

Sites (post-fix line numbers) and diagnostics:

| loader | site | diagnostic |
|---|---|---|
| costume | `_parse_map` block mapping | `duplicate key %r` (ValueError → Malformed) |
| costume | `_flow` flow mapping | `duplicate key %r in flow mapping` |
| costume | `_parse_list` entry merge | `duplicate key %r in mapping entry` |
| costume | `parse_packet` JSON path | `object_pairs_hook` → `duplicate key %r in JSON mapping` |
| lexicon | `_parse_map` block mapping | `duplicate key %r` (PacketError) |
| lexicon | `_flow_value` flow mapping | `duplicate key %r in flow mapping` |
| lexicon | `load_packet` JSON path | `object_pairs_hook` → `duplicate key %r in JSON mapping` |
| myth | `_parse_flow` flow mapping | `duplicate key %r` (GateParseError) |

Each raise maps onto the loader's existing parse-error path (costume
`Malformed`, lexicon `PacketError`, myth `GateParseError`), so duplicates
become the documented exit 2 could-not-evaluate with a named diagnostic. No
docstring described the old lenient behaviour, so none needed amending. Myth's
block-mapping check pre-existed and was left untouched.

## 3. Post-fix verification (command evidence)

```
$ sha256sum tools/gates/costume-era-consistency-gate.py \
            tools/gates/lexicon-coverage-audit.py \
            tools/gates/myth-consistency-gate.py
e6bffd7020c0b1168828902853320bbf37e903457c83dae5477820aeceec478f  costume-era-consistency-gate.py
2c4dd39702a15ea3fa62d3597fe42304e3bda4122d7b17d6c00121f9d27d4287  lexicon-coverage-audit.py
5368b13542cd4b8a5bd850d83835e588df13a72b7d6c502b2aa016ee36b95f08  myth-consistency-gate.py

$ git show HEAD:tools/gates/<each>.py | sha256sum     # == review 26 §0 pins
29a9361c7b96a354c41a3994e3459a951ce0a43425b3984d6506b3e5b3a43f03
63ee4ec6b15188fefa3e997766971d66fe4d7d7bf9eed65cdcdd55f548fe8a80
26d246e9936db4375c31c6eb260545bf55051d11ec00bb1e757458399b1b55c5

$ python3 tools/gates/<each>.py --selftest
costume  self-test: 10/10 checks passed; fixture exit 1 with 21 planted finding IDs   rc=0
lexicon  selftest: 14/14 checks passed                                                rc=0
myth     selftest: OK — fixture exit 1; planted IDs present … clean control exit 0    rc=0

$ python3 tools/check-gate-battery.py --selftest
SELFTEST OK 10/10 controls behaved as expected          battery-rc=0
$ python3 tools/check-craft-exercise.py --selftest
CLI-SELFTEST OK 18/18 cases passed                      craft-rc=0

$ # live example packet, pre-fix vs post-fix bytes
costume  pre_rc=0 post_rc=0 output=IDENTICAL
lexicon  pre_rc=0 post_rc=0 output=IDENTICAL
myth     pre_rc=0 post_rc=0 output=IDENTICAL
```

Frozen-input equivalence (round-3 snapshot rows for these three gates):
pre-fix and post-fix bytes produce identical rc and stdout on the frozen
`packet.d2.yml` snapshot. `tools/replay-frozen.py` itself refuses to run gates
whose bytes differ from the manifest pin (fail-closed `gate_digest_mismatch`),
so the frozen rows are unaffected by this repair by construction; the
pre/post identity above is the direct no-verdict-drift evidence.

## 4. Negative control

`neg-06-control.py` — stdlib only; payloads written solely into a scratch
directory outside the repository (system temp when writable, else
`~/.cache/neg06-scratch`; the wave observed /tmp inode exhaustion, see §6);
gates invoked as subprocesses or imported read-only with bytecode writing
disabled. The CLI payloads are the live example packet plus one duplicate
appended, so a pre-fix run is a *verdict* about colliding keys, not an
unrelated rejection. The in-memory checks call the loader's own parse entry
point and assert a duplicate-key error (post-fix) versus a silently merged
last-wins value (pre-fix).

**Post-fix run (live tree, 17/17):**

```
NEG-06 RESULT: PASS (17/17 checks)      live-exit=0
```

**Pre-fix run (same control, pinned pre-fix bytes via `--pre-fix-from-git`):**

```
NEG-06 RESULT: FAIL (11/17 checks)      prefix-exit=1
NEG-06 FAILURE: costume … block-duplicate: PRE-FIX PATTERN OBSERVED: rc=0, no
  duplicate-key diagnostic — the loader evaluated or silently merged colliding
  keys; expected rc=2 naming the duplicate. output=[]
NEG-06 FAILURE: costume … json-duplicate-in-memory: PRE-FIX PATTERN OBSERVED:
  parse returned (no duplicate-key error) — last-wins value={'name': 'b'}
NEG-06 FAILURE: lexicon … block-duplicate: PRE-FIX PATTERN OBSERVED: rc=0 …
NEG-06 FAILURE: myth … flow-duplicate: PRE-FIX PATTERN OBSERVED: rc=0 …
```

So the control **fails on the pre-fix pattern** (exit 1, naming it: a clean
verdict or a last-wins dict for colliding keys) and **passes post-fix**
(exit 0, 17/17). Two checks pass on the pre-fix bytes by design and are kept
as controls: myth's block-mapping duplicate check pre-existed (review 26 §1.4)
and the unmodified example packet stays clean on both byte sets.

Evidence files: `evidence-live.txt`, `evidence-prefix.txt`,
`evidence-regression.txt` (this directory).

## 5. Reproduce

```bash
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
python3 reports/round-8/operability/neg-controls/neg-06/neg-06-control.py              # → exit 0
python3 reports/round-8/operability/neg-controls/neg-06/neg-06-control.py \
        --pre-fix-from-git                                                            # → exit 1
for g in costume-era-consistency-gate lexicon-coverage-audit myth-consistency-gate; do
  python3 tools/gates/$g.py --selftest; done                                          # → 0/0/0
python3 tools/check-gate-battery.py --selftest                                        # → exit 0
```

## 6. Limits (untested, stated)

- Scope: this shard repairs and controls D2 only in costume/lexicon/myth.
  The phonology and naming rows belong to shards R8-O05/R8-O07 and are not
  re-claimed here; the cross-shard claim "all five loaders uniform" is
  evidenced by the sibling receipts plus this one, not by a single run here.
- The CLI checks depend on the live example packet
  (`examples/culture-d2/packet.d2.yml`) still being a clean packet; a future
  edit that gives it findings would make the "live-example-packet-clean"
  checks fail loudly (rc=0 asserted), not silently pass.
- The control asserts this shard's diagnostic strings ("duplicate key"); a
  future reword fails loudly.
- **Environment hazard (affects the whole wave):** during this shard's runs
  `/tmp` reached 100% inodes (`df -i /tmp` → `1048576 1048575 1 100%`), and
  `tempfile.mkdtemp()` can succeed while writing a payload still raises
  `OSError: [Errno 28] No space left on device`. The round-8 harness runs
  every control bare and treats a stderr traceback as a failure, so under
  that condition sibling controls (and this one, before hardening) exit 1 with
  a traceback and the harness's O measurement marks the defects unrepaired
  (`repaired: ['D9','F5']` at 20:31Z). After hardening this control's scratch
  handling the harness measurement read `repaired: ['D1','D2',…,'F1','F5'],
  unrepaired: []` with zero traceback-failing controls. The orchestrator
  should clear /tmp (or require the scratch fallback) before the acceptance
  run; this shard does not edit the harness or sibling artifacts.
- The harness's `status_at_head` column in the inventory predates this
  repair (its rows 4/5/6 read `present_at_head`); the worktree is repaired.

## 7. Harness reconciliation

Re-running the harness's own measurement in-process (read-only; the filed
`reports/round-8/validation.json` was **not** rewritten by this shard):

```
repaired: ['D1','D2','D3','D4','D5','D6','D7','D8','D9','F1','F5']
unrepaired: []
neg-06 control entry: {'ids': ['D2'], 'exit': 0, 'traceback': False}
```

The control declares both legs (`pre-fix` / `post-fix`, `fail-before` /
`pass-after` wording present in this file and in the control docstring), so
the harness's separation-leg check is satisfied by this shard's artifacts.
