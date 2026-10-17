# neg-05 — negative control + repair receipt (shard R8-O05)

- **Round:** 8 · **shard:** R8-O05 (operability) · **claim:** O
- **Date:** 2026-10-17 (all commands below; final verification sweep at
  `checked_at_utc = 2026-10-17T20:23:38Z`)
- **Baseline:** declared `e7ca0fa…`; worktree HEAD `cf338a7`. The repaired
  gate was byte-identical to the review-26 §0 pin
  (`fb05c644cafb0855481beb5d8bc3f619ae688d8b12787e530f01543f85372655`)
  before this shard's edit, so the defect and its control bind to the
  declared baseline.
- **Role:** repair shard. Writes only the repaired gate, this directory's
  control and evidence, and this report. No commit.

## 0. Defect selection (dependency status)

`reports/round-8/operability/defect-inventory.json` (R8-O03's artifact) was
absent when this shard started, so both named reviews were read first:
`reports/supplement-opencode-1/26-parser-controls.md` (defect register
§3 D1-D9) and `29-local-boundaries.md` (F1-F6). The inventory landed during
the shard's poll window, and it settles the index:

```
$ python3 -c "import json; d=json.load(open('reports/round-8/operability/defect-inventory.json')); print(len(d)); print(d[1]['defect_id'], '|', d[1]['file'])"
20
R26-D2-phonology | tools/gates/phonology-sanity-gate.py
```

**Defect index 1 (0-based; `idx: 2` in the inventory) = `R26-D2-phonology`**
— "duplicate mapping keys silently last-win with no diagnostic — block
mapping overwrite at :416, flow-mapping overwrite at :382; no duplicate-key
check exists anywhere in this loader." Index 0 is `R26-D1` (sibling shard
R8-O04, which already landed its repair in the same file — see §6).

## 1. Defect and pre-fix reproduction

Review 26 §3 D2: an author's stale key silently changes the audit outcome.
The two-block counterexample and the flow-mapping shape were reproduced
against the pinned pre-fix bytes (extracted with `git show`, run read-only):

```
$ git show cf338a7:tools/gates/phonology-sanity-gate.py > ~/tmp/neg05/prefix-gate.py
$ sha256sum ~/tmp/neg05/prefix-gate.py
fb05c644cafb0855481beb5d8bc3f619ae688d8b12787e530f01543f85372655   # == review 26 §0 pin

$ python3 <pre-fix copy> /…/dup-block.yml
FINDING G-DATA: REVIEW — phonology.notable_rules is missing — …
FINDING M-EJECT: REVIEW — ejective /qʼ/ with no plain stop at the uvular place: …
rc=1
```

The second `phonology:` block (which adds `qʼ`) silently won and the gate
printed a *linguistic* finding about a document whose keys collide. The
flow shape `phonology: {consonants: [p], consonants: [k]}` likewise parsed
without error (pre-fix winner: `['k']`). The loader has no JSON branch
(`grep -c json tools/gates/phonology-sanity-gate.py` → `0`), so the JSON
`object_pairs_hook` leg of review 26 §3 D2 does not apply to this file; it
belongs to the costume/lexicon shards.

## 2. Repair

`tools/gates/phonology-sanity-gate.py` — a duplicate key is now a parse
error (`PacketError`), which the existing `run_text` catch maps to exit 2 +
one `G-DATA` finding. Three overwrite sites closed (post-fix lines):

| site | post-fix line | new diagnostic |
|---|---|---|
| flow mapping (`_parse_scalar`) | `:358` | `duplicate key %r in flow mapping` |
| sequence mapping entry (`_parse_sequence`) | `:416-419` | `duplicate key %r in mapping entry` |
| block mapping (`_parse_mapping`) | `:445` | `duplicate key %r at line %d` |

The block check sits before all four `result[key] = …` assignments, so the
whole block-mapping path is covered. The reader header comment (`:264-269`)
now declares the closed subset, including the duplicate-key rule, so the
policy the review found undeclared is documented next to the code.

```diff
@@ -387,6 +413,10 @@ def _parse_sequence(lines, i, indent):
                 sub, i = _parse_block(lines, i, lines[i][0])
                 if isinstance(sub, dict):
+                    clash = sorted(set(sub) & set(entry))
+                    if clash:
+                        raise PacketError("duplicate key %r in mapping entry"
+                                          % clash[0])
                     entry.update(sub)
@@ -411,6 +441,8 @@ def _parse_mapping(lines, i, indent):
         key = str(_parse_scalar(key.strip()))
+        if key in result:
+            raise PacketError("duplicate key %r at line %d" % (key, lineno))
@@ -323,19 +340,28 @@ def _flow_parts(body):
             if not sep:
                 raise PacketError("flow mapping entry without ':'")
-            result[str(_parse_scalar(key))] = _parse_scalar(val)
+            key = str(_parse_scalar(key))
+            if key in result:
+                raise PacketError("duplicate key %r in flow mapping" % key)
+            result[key] = _parse_scalar(val)
```

Hunk headers above are verbatim from `git diff`; the first hunk
(`-323,19 +340,28`) also carries sibling shard R8-O04's D1 change in the
same region.

Also added three `CONTROL_CASES` entries (`:1252`, `:1258`, `:1260`) so the
registered battery itself can see this class (review 26 D10's gap).

## 3. Post-fix verification (command evidence)

```
$ sha256sum tools/gates/phonology-sanity-gate.py
d5fe087ffb2342e54cd6d6f3ef1e891315a95224bc25cdc5bc425b91dec34230

$ python3 tools/gates/phonology-sanity-gate.py --selftest
selftest: fixture exit 1; 15/15 planted finding IDs present; 29 control cases passed
selftest rc=0            # 26 cases before this shard's three additions

$ python3 tools/check-gate-battery.py            # isolated mirror, 2026-10-17
{"summary": {"battery_exit": 0, "fail": 0, "pass": 7, "unevaluable": 0}, …}
"originals": {"modified": 0, "preserved": true, "files_hashed_before": 28, …}
battery rc=0

$ python3 tools/check-gate-battery.py --selftest
SELFTEST OK 10/10 controls behaved as expected        # rc=0

$ python3 tools/check-craft-exercise.py --selftest
SELFTEST OK 10/10 tamper cases detected
CLI-SELFTEST OK 18/18 cases passed                    # rc=0
```

The three malformed shapes now exit 2 with the named diagnostic, while the
duplicate-free twin and the complete valid packet are unchanged:

```
POST-FIX block-dup run_text -> 2 G-DATA packet could not be parsed: duplicate key 'phonology' at line 7
POST-FIX flow-dup  run_text -> 2 packet could not be parsed: duplicate key 'consonants' in flow mapping
POST-FIX seq-dup   run_text -> 2 packet could not be parsed: duplicate key 'name' in mapping entry
POST-FIX clean packet -> 1
```

## 4. Negative control

`reports/round-8/operability/neg-controls/neg-05/neg-05-control.py` —
stdlib only; payloads written solely into a temp directory **outside the
repository**; the gate under test is invoked as a subprocess; nothing under
the repo is written by the control. Seven checks: the exact duplicate block,
the review's verdict-flip block, the duplicate flow key, the duplicate
sequence-entry key, the stdin path, plus two positive twins (duplicate-free
packet still evaluates; complete valid packet still clean).

**Post-fix run (live gate):** `evidence-postfix-live.txt`

```
NEG-05 gate sha256: d5fe087ffb2342e54cd6d6f3ef1e891315a95224bc25cdc5bc425b91dec34230
NEG-05 duplicate-block-key                rc=2 ids=G-DATA PASS
NEG-05 duplicate-block-verdict-flip       rc=2 ids=G-DATA PASS
NEG-05 duplicate-flow-key                 rc=2 ids=G-DATA PASS
NEG-05 duplicate-sequence-entry-key       rc=2 ids=G-DATA PASS
NEG-05 first-block-twin-still-evaluates   rc=1 ids=G-DATA PASS
NEG-05 valid-packet-still-clean           rc=0 ids=- PASS
NEG-05 stdin-duplicate-block              rc=2 ids=G-DATA PASS
NEG-05 RESULT: PASS (7/7 checks)
postfix-control rc=0
```

**Pre-fix run (same control, pinned pre-fix bytes):** `evidence-prefix-pinned.txt`

```
NEG-05 note: this is the review-26 pinned PRE-FIX byte copy (fb05c644...); checks below are expected to FAIL.
NEG-05 duplicate-block-key                rc=1 ids=G-DATA FAIL
NEG-05 duplicate-block-verdict-flip       rc=1 ids=G-DATA,M-EJECT FAIL
NEG-05 duplicate-flow-key                 rc=1 ids=G-DATA,G-DATA,G-DATA,M-CLASS,P-PATTERN,T-C FAIL
NEG-05 duplicate-sequence-entry-key       rc=1 ids=G-DATA FAIL
NEG-05 first-block-twin-still-evaluates   rc=1 ids=G-DATA PASS
NEG-05 valid-packet-still-clean           rc=0 ids=- PASS
NEG-05 stdin-duplicate-block              rc=1 ids=G-DATA FAIL
NEG-05 RESULT: FAIL (5/7 checks)
prefix-control rc=1
```

So the control **fails on the pre-fix pattern** (exit 1, each failure naming
the silent-merge observation, e.g. `rc=1 ids=['G-DATA', 'M-EJECT']`) and
**passes post-fix** (exit 0, 7/7). The two positive twins pass in both
directions, so the control is not merely asserting "more rejections".

## 5. Reproduce

```bash
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
python3 reports/round-8/operability/neg-controls/neg-05/neg-05-control.py          # → exit 0
git show cf338a7:tools/gates/phonology-sanity-gate.py > ~/tmp/neg05/prefix-gate.py
python3 reports/round-8/operability/neg-controls/neg-05/neg-05-control.py \
        --gate ~/tmp/neg05/prefix-gate.py                                          # → exit 1
python3 tools/gates/phonology-sanity-gate.py --selftest                            # → exit 0
python3 tools/check-gate-battery.py                                                # → exit 0, 7/7
```

## 6. Limits (untested, stated)

- **Concurrency:** sibling shards have edited this same file concurrently in
  five concern areas (D1 `:337-345`, D3 anchors `:364`, D5 tabs `:296-298`,
  D6 depth cap `:307` and `RecursionError` `:1120-1122`, F1 fixture pinning
  `:1267`). The sha256 above
  is the state this shard wrote; a later sibling edit changes the digest
  while this shard's hunks stay as shown. No sibling file was edited by this
  shard.
- The inventory's D2 items for the other four loaders (`idx` 3-6: naming,
  costume, lexicon, myth) are sibling shards' scope; this shard repaired
  only the phonology item, index 1.
- The flow-mapping check treats a repeated key as an error even when both
  values are identical; that is deliberate (the packet is malformed either
  way) but is stricter than YAML processors that last-win silently.
- Sequence-entry coverage is limited to the inline `- key: value` form plus
  its following block merges; a duplicate introduced by two separate
  sequence items is two items, not a duplicate key, and stays legal.
- The control exercises the file-argument and stdin paths; it does not test
  JSON input (this loader has no JSON branch).
- Repairing the code does not by itself update
  `corpus/knowledge/verification/phonology-sanity-gate.md`; a one-line
  subset-policy note there is routed to the parent, not absorbed by this
  shard.

## 7. Host note and inventory poll outcome

- **`/tmp` is exhausted on this host** (`df -i /tmp` → `1048576 1048576 0
  100%`): payload writes to `/tmp` fail with `No space left on device`.
  The control therefore probes for the first writable scratch parent
  (`$NEG05_SCRATCH`, then system temp, then `~/tmp`) and the receipt above
  shows `NEG-05 scratch parent: /var/tmp`. Pre-fix byte copies live at
  `~/tmp/neg05/`, outside the repository.
- **Inventory poll outcome:** the inventory landed inside this shard's poll
  window (`reports/round-8/operability/defect-inventory.json`, 20 items), so
  the fallback selection (§0) was confirmed by the inventory's own index
  rather than left inferred.

## 8. Handoff to the parent (integration notes, not absorbed)

1. **Inventory status field.** `reports/round-8/run-validation.py:879` reads a
   row's status through `first_value(row, ("status", "disposition",
   "decision", "verdict", "state"))` (`:140`) — exact key match. The
   inventory's `status_baseline` / `status_working_tree` keys do not match,
   so every row currently reads as "no status" and the validator's `repaired`
   set stays empty. For claim O to count this repair, the row
   `R26-D2-phonology` needs a `"status": "repaired"` field (receipts: this
   directory); that edit belongs to O03/the integrator, not to this shard.
2. **Control discovery.** `measure_neg_controls` (`:912-962`) selects
   `matches[0]` — the first sorted artifact that references the defect id —
   and requires both leg markers on that one file. Today D2's first match is
   `neg-controls/neg-04/neg-04-report.md` (it lists "D2-D9") and it does
   declare both legs, so the check passes; this shard's own carrier is
   `neg-05-control.py` (references `D2`; legs `pre_fix=True, post_fix=True`;
   exit 0; no traceback).
3. **Validator crash (not this shard's artifact).**
   `python3 reports/round-8/run-validation.py` currently aborts in `main`
   with `json.decoder.JSONDecodeError: Illegal trailing comma before end of
   array: line 192 column 203` while loading the F-side reconciliation file.
4. **Evidence to cite.** Gate sha256
   `d5fe087ffb2342e54cd6d6f3ef1e891315a95224bc25cdc5bc425b91dec34230`;
   control 7/7 live (rc=0) and 5/7-fail on the pinned pre-fix bytes (rc=1);
   gate selftest 29 cases (rc=0); 7-gate battery 7/7 with
   `originals.preserved: true`; final sweep at `2026-10-17T20:25:22Z`.
5. **Cross-shard break found while sweeping (not caused by this shard).**
   `python3 tools/assemble-d2.py --check` now exits 1 with
   `packet.d2.yml differs from deterministic assembly`. Cause: the assembly
   payload embeds the reader pin `"reader_sha256": digest(READER)`
   (`tools/assemble-d2.py:148`, READER = the costume gate) and the committed
   packet carries the pre-repair value
   `reader_sha256: 29a9361c…` (`examples/culture-d2/packet.d2.yml:3322`,
   the review-26 §0 costume-gate hash), while the live costume gate has since
   been repaired by a sibling shard and hashes
   `087aa6a444104c42cdf6444998d32ab1cd0cb1cfd51b94607681eb0dcdeb662e`.
   The packet references the phonology gate nowhere
   (`grep -c phonology-sanity-gate examples/culture-d2/packet.d2.yml` → `0`),
   so this shard's repair is not in that hash chain. Regenerating the D2
   example packet (D02/D15 scope) is needed before any O/D measurement that
   runs the assembler check.
6. **Host-level:** the `/tmp` inode exhaustion also breaks sibling tools that
   use system temp — `python3 tools/replay-frozen.py --selftest` died with
   `OSError: [Errno 28] No space left on device` under
   `/tmp/replay-frozen-selftest-*` (this shard's own control avoids `/tmp`).
