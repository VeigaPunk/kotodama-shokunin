# neg-07 — negative control + repair receipt (shard R8-O07)

- **Round:** 8 · **shard:** R8-O07 (operability) · **claim:** O
- **Assigned defect:** defect **index 3** of
  `reports/round-8/operability/defect-inventory.json` = **`R26-D2-naming`**
  (review 26 §3 D2 at `tools/gates/naming-collision-gate.py`: duplicate keys
  silently last-win).
- **Date:** 2026-10-17. Assigned-defect verification run
  `checked_at_utc = 2026-10-17T20:24:00Z`.
- **Baseline:** declared `e7ca0fa…`; worktree HEAD `cf338a7`. The naming gate
  is byte-identical at `fe34faa` and `e7ca0fa`
  (`git rev-parse e7ca0fa:tools/gates/naming-collision-gate.py` →
  `a32267a7…`, the blob review 26 §0 pins; sha256
  `8c5afb0a5abc8b00a659120e3795586ddce688bd962ccc68f7308f7bf19aa526`).
- **Role:** repair shard. Writes only the gate repairs, this directory's
  controls/report/evidence, and nothing else. No commit.

## 0. Defect selection (dependency and index resolution)

`defect-inventory.json` (R8-O03) did **not exist** when this shard started:

```
$ ls -la reports/round-8/operability/
ls: cannot access 'reports/round-8/operability/': No such file or directory
```

Per the shard fallback, both named reviews were read, and the shard began on
its best reading of "defect index 3" (register order of review 26 §3:
D1–D9 defects, D10 a note) — **D3, anchors/tags guessed, not rejected**. That
work is complete and retained (§5, "additional repair"). A background poll
(60 s interval, 20-minute bound) then **found the inventory at
2026-10-17T20:21:08Z**, and its ordering is different: D1, then one D2 row per
gate (indices 2–6), then D3. Its **index 3 is `R26-D2-naming`**:

> `defect`: "D2: duplicate keys silently last-win in flow mappings (:348) and
> block mappings (:431); the loader has no duplicate-key diagnostic at all."
> · `evidence_pointer`: "Repro: 'orthography: {case: contrastive}' ->
> {CROSS-HOLD, NAME-CASE, PHON-INVENTORY}; adding a second 'orthography:
> {case: display-only}' -> {CROSS-HOLD, NAME-REUSE} — a stale key silently
> flips the verdict with no duplicate-key finding." · `suggested_control`:
> "assert exit 2 + a duplicate-key finding naming 'orthography'; fail-before =
> the NAME-REUSE verdict." · `severity`: high · `status_at_head`:
> `present_at_head`.

That assigned defect was implemented and verified after the inventory landed
(§1–§4). The D3 fallback repair is kept because it is a real, independently
verified operability improvement; its control is `neg-07-d3-control.py` (§5).

## 1. Assigned defect (index 3) and pre-fix reproduction

Review 26 §3 D2: the naming loader had no duplicate-key diagnostic anywhere;
overwrites last-win. Pre-fix bytes were extracted from the pinned blob and
hash-verified (`8c5afb0a…` == review 26 §0 pin). Three complete probe packets
were built by one textual replacement each inside the committed fixture
(`tools/gates/fixtures/naming-collision-gate.yml`, sha256 in
`evidence-fixture-hashes.txt`), replacing its `orthography:` block:

| probe | pre-fix rc | pre-fix ids (first three) | reading |
|---|---|---|---|
| A `orthography: {case: contrastive}` | 1 | NAME-REUSE, NAME-REUSE, **NAME-CASE** | single key: contrastive casing routed |
| B A + stale `orthography: {case: display-only}` | 1 | NAME-REUSE, NAME-REUSE, NAME-VISUAL | **NAME-CASE gone** — stale key last-won; verdict flipped, no duplicate-key finding |
| C `orthography: {case: contrastive, case: display-only}` | 1 | NAME-REUSE, NAME-REUSE, NAME-VISUAL | flow-mapping duplicate last-wins silently |

This is the inventory's verdict-flip pattern (the probe packet is the full
fixture rather than the inline packet, so extra planted ids appear; the flip
is exactly the presence/absence of `NAME-CASE` between A and B).

## 2. Repair

Two insertions in `tools/gates/naming-collision-gate.py`, raising the gate's
own `YamlError` so the existing boundary maps it to exit 2 + one `G-DATA`
finding; the message names the key, matching the myth gate's existing
`duplicate key %r` convention:

```diff
--- a/tools/gates/naming-collision-gate.py   (pinned blob a32267a7)
+++ b/tools/gates/naming-collision-gate.py
@@ _parse_flow (flow mappings)
         for part in _split_flow(s[1:-1]):
             key, rest = _split_key(part)
+            if key in out:
+                raise YamlError(f"duplicate key {key!r}")
             out[key] = _parse_value(rest, _TYPED_KEYS.get(key))
@@ _parse_map (block mappings; covers the plain, child-block and block-scalar paths)
         key, rest = _split_key(text)
+        if key in node:
+            raise YamlError(f"duplicate key {key!r}")
         if rest in ("|", "|-", "|+", ">", ">-", ">+"):
```

4 inserted lines, 0 deletions, 2 functions. **Frozen-run check:** the round-3
frozen manifest row for this gate (input snapshot
`tools/gates/frozen/round-3/inputs/examples/culture-d2/packet.d2.yml`, want
rc=1, stdout sha256 `e81bab66…`) re-executes against the repaired gate with
**identical** exit and stdout digest:

```
$ python3 tools/gates/naming-collision-gate.py tools/gates/frozen/round-3/inputs/examples/culture-d2/packet.d2.yml
rc=1  stdout sha256 e81bab661a994440eabaff640b5c34ab79992da36bf7323efbff67dce3628d01  (== manifest output_sha256)
```

**Concurrency note:** sibling O-shards edited the same file during the round
(e.g. `_parse_scalar` gained a `typed` parameter for the D4 row); the diff
above is this shard's insertions only. Naming gate sha256 at final
verification: `e4acaf56acaf5c15ff196d0d996bd58c69ba3ed0adefb648f5874994fb71597d`
(this shard's state plus concurrent siblings').

## 3. Post-fix verification

```
$ python3 tools/gates/naming-collision-gate.py <probe B / probe C>
probe B  rc=2  FINDING G-DATA: HOLD — input could not be evaluated: duplicate key 'orthography'
probe C  rc=2  FINDING G-DATA: HOLD — input could not be evaluated: duplicate key 'case'
probe A  rc=1  unchanged (NAME-CASE present) — no over-rejection

$ python3 tools/gates/naming-collision-gate.py --selftest        # read-only selftest, live tree
selftest: OK — fixture findings 12 across 11 ids …               # rc=0

$ python3 tools/check-gate-battery.py --selftest                 # 2026-10-17T20:24Z
SELFTEST OK 10/10 controls behaved as expected                   # rc=0
$ python3 tools/check-craft-exercise.py --selftest               # 2026-10-17T20:24Z
SELFTEST OK 10/10 tamper cases detected
CLI-SELFTEST OK 18/18 cases passed                               # rc=0
```

The naming `--selftest` is a reader (no `open(..., "w")` / `write_text` in the
file — the only `write` is `sys.stderr.write` in the usage line), so it ran
live. The five *writer* gates' selftests
rewrite their fixtures in place (review 29 F1), so their 7/7-green receipt was
taken on an isolated copy at 20:19Z (`phonology 15/15 + 26 controls, naming OK,
myth OK, costume OK, lexicon 14/14, provenance OK, handoff OK`); naming's
green is superseded by the live run above.

## 4. Negative control (assigned defect)

`reports/round-8/operability/neg-controls/neg-07/neg-07-control.py` — stdlib
only; probe packets written solely into `tempfile.TemporaryDirectory()`; the
gate invoked as a subprocess; nothing under the repository written. Five
checks: duplicate block-level keys rejected naming `'orthography'`, duplicate
flow-mapping keys rejected naming `'case'`, duplicate nested block keys
rejected naming `'case'`, the single-key contrastive twin still evaluates with
`NAME-CASE`, and the pristine fixture still evaluates to rc=1.

**Post-fix run (live gate, sha256 `e4acaf56…`, 2026-10-17T20:24Z):**

```
$ python3 reports/round-8/operability/neg-controls/neg-07/neg-07-control.py
NEG-07 dup-block-orthography        rc=2   ids=G-DATA  PASS
NEG-07 dup-flow-case                rc=2   ids=G-DATA  PASS
NEG-07 dup-nested-block-case        rc=2   ids=G-DATA  PASS
NEG-07 single-contrastive-twin      rc=1   ids=NAME-REUSE,NAME-REUSE,NAME-CASE  PASS
NEG-07 pristine-fixture-unchanged   rc=1   ids=NAME-REUSE,NAME-REUSE,NAME-VISUAL  PASS
NEG-07 RESULT: PASS (5/5 checks)
control rc=0
```

**Pre-fix run (same control, pinned pre-fix bytes):**

```
$ python3 …/neg-07-control.py --gate /tmp/neg07-prefix/naming-collision-gate.py
NEG-07 note: this is the review-26 pinned PRE-FIX byte copy (8c5afb0a...); checks below are expected to FAIL.
NEG-07 dup-block-orthography   rc=1  ids=NAME-REUSE,NAME-REUSE,NAME-VISUAL  FAIL
NEG-07 dup-flow-case           rc=1  ids=NAME-REUSE,NAME-REUSE,NAME-VISUAL  FAIL
NEG-07 dup-nested-block-case   rc=1  ids=NAME-REUSE,NAME-REUSE,NAME-VISUAL  FAIL
NEG-07 single-contrastive-twin rc=1  ids=NAME-REUSE,NAME-REUSE,NAME-CASE    PASS
NEG-07 pristine-fixture-unchanged rc=1  …                                   PASS
NEG-07 RESULT: FAIL (3/5 checks)
NEG-07 FAILURE: dup-block-orthography: PRE-FIX PATTERN OBSERVED: rc=1 … the second 'orthography:' block last-won with no duplicate-key finding (stale key silently changed the verdict) …
control rc=1
```

So the control **fails on the pre-fix pattern** (exit 1, naming it) and
**passes post-fix** (exit 0, 5/5). Full outputs:
`evidence-control-live.txt`, `evidence-control-prefix.txt`.

## 5. Additional repair (fallback D3: anchors/tags guessed, not rejected)

Before the inventory landed, the shard repaired review 26 §3 D3 as its
fallback reading of "index 3": a guard in each of the five packet gates'
scalar choke points rejecting unquoted `&`/`*`/`!` scalars with the gate's own
parse error → documented exit 2 (7 insertion sites, 14 inserted lines, 0
deletions; `_parse_scalar`/`_key_of` in naming, `_parse_scalar` in
phonology/myth, `_scalar` in costume, `_unquote_scalar`/`_unquote_key` in
lexicon). Blast-radius sweep before the edit: 0 unquoted indicator scalars in
25 fixture/example/frozen YAML files. Pre-fix receipt (naming, pinned bytes):
`FINDING PHON-INVENTORY: FAIL — name name#1 '*tag': symbol /*/ at position 1 …`
(the review's exact counterexample).

Control: `neg-07-d3-control.py` (5 gates × 4 checks; `--prefix-dir` mode for
pinned bytes). Live: **PASS 20/20, rc=0** (`evidence-d3-control-live.txt`);
pinned pre-fix: **FAIL 5/20, rc=1** with `PRE-FIX PATTERN OBSERVED`
(`evidence-d3-control-prefix.txt`). Over-rejection controls (quoted indicator,
mid-scalar indicator) pass on both byte sets.

**Overlap warning for the orchestrator:** the inventory's **index 7**
(`R26-D3`) is a different shard's assignment; that shard will find the D3
sites already repaired in-tree. This shard claims only the repair + control
above; index 7's owner may verify-and-close or supersede, and should not
double-patch blindly.

## 6. Reproduce

```bash
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
# assigned defect (index 3): control + pre-fix control
python3 reports/round-8/operability/neg-controls/neg-07/neg-07-control.py        # → exit 0
python3 reports/round-8/operability/neg-controls/neg-07/neg-07-d3-control.py \
        --extract-prefix /tmp/neg07-prefix                                       # → exit 0
python3 reports/round-8/operability/neg-controls/neg-07/neg-07-control.py \
        --gate /tmp/neg07-prefix/naming-collision-gate.py                        # → exit 1
python3 tools/gates/naming-collision-gate.py --selftest                          # → exit 0
python3 tools/check-gate-battery.py --selftest                                   # → exit 0
python3 tools/check-craft-exercise.py --selftest                                 # → exit 0
# additional D3 repair control
python3 reports/round-8/operability/neg-controls/neg-07/neg-07-d3-control.py     # → exit 0
python3 reports/round-8/operability/neg-controls/neg-07/neg-07-d3-control.py \
        --prefix-dir /tmp/neg07-prefix                                           # → exit 1
```

## 7. Limits (untested, stated)

- The repair rejects duplicates by **key text after `_key_of`/`_split_key`
  normalization** (quoted keys are unquoted first), which is the comparison
  the loader itself uses; two keys that normalize to different strings but
  compare equal under NFC are not caught here (the gate's other checks
  normalize separately).
- Only the **naming** gate was repaired for D2 (inventory indices 4–6 are the
  same defect in phonology/costume/lexicon — sibling shards; myth's block
  check already existed and its flow gap is index 6).
- The additional D3 repair leaves **myth mapping keys** unguarded (they are
  used raw) — a named residual, deliberately not raced against the D2
  siblings editing those regions.
- Selftest receipts for the five writer gates come from an isolated copy
  because their `--selftest` rewrites committed fixtures in place (review 29
  F1). The assert-based selftest hardening under `python3 -O` (inventory
  index 17) is not addressed here.
- Gate hashes changed repeatedly during the round (concurrent siblings);
  hashes quoted are the state at the verification timestamps. Naming:
  `e4acaf56…`; other four at 20:24Z: `d5fe087f…`, `48477d38…`, `6be04578…`,
  `989b1295…`.

## 8. Inventory poll outcome

**FOUND at 2026-10-17T20:21:08Z** (60 s interval poll, 20-minute bound); the
inventory's index-3 row (`R26-D2-naming`) was adopted as the assigned defect
and implemented per its `suggested_control` (§1–§4). Evidence:
`reports/round-8/operability/neg-controls/neg-07/`.

## 9. Integration note for the O harness (not this shard's file)

`reports/round-8/run-validation.py` (R8-O15) crashed when this shard ran it
(2026-10-17T20:24Z):

```
File "reports/round-8/run-validation.py", line 860, in measure_o_defects
    value = inventory.get(key)
AttributeError: 'list' object has no attribute 'get'
```

The inventory (R8-O03) is a bare JSON **list of rows**; the harness expects a
**mapping** with one of `INVENTORY_KEYS` = ("defects", "entries", "inventory",
"rows", "items") holding the row list, and reads each row's status through
`STATUS_FIELD_ALIASES` = ("status", "disposition", "decision", "verdict",
"state"). The inventory rows carry `status_at_head: "present_at_head"`, which
matches none of those aliases and none of `REPAIRED_STATUSES` — so even after
the shape fix the harness will report "defect … has no status" until O03/O15
agree on a status field. This shard's artifacts do not depend on either
convention: both controls exit 0 on the live tree (the harness's per-artifact
`run_cli` check), and every file under this directory carries the `pre-fix` /
`post-fix` leg markers the harness looks for (`SEPARATION_LEG_MARKERS`).
