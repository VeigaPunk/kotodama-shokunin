# neg-04 — negative control + repair receipt (shard R8-O04)

- **Round:** 8 · **shard:** R8-O04 (operability) · **claim:** O
- **Date:** 2026-10-17 (all commands below; consolidated evidence run at
  `checked_at_utc = 2026-10-17T20:15:43Z`)
- **Baseline:** declared `e7ca0fa…`; worktree HEAD `cf338a7` — the repaired gate
  is byte-identical at both revisions
  (`fb05c644cafb0855481beb5d8bc3f619ae688d8b12787e530f01543f85372655`,
  the same hash review 26 §0 pins), so the defect and its control bind to the
  declared baseline.
- **Role:** repair shard. Writes only the repaired gate, this directory's
  control, and this report. No commit.

## 0. Defect selection (dependency status)

`reports/round-8/operability/defect-inventory.json` (R8-O03's artifact) did
**not exist** when this shard started:

```
$ ls -la reports/round-8/operability
ls: cannot access 'reports/round-8/operability/': No such file or directory
```

Per the shard fallback ("if absent, read the two reviews directly and take the
1st defect you confirm"), both named reviews were read:
`reports/supplement-opencode-1/26-parser-controls.md` and
`reports/supplement-opencode-1/29-local-boundaries.md`. The first defect in
register order is review 26 §3 **D1**; it was confirmed by direct
reproduction (below), so this shard owns **D1: unterminated flow sequence is
silently closed — `tools/gates/phonology-sanity-gate.py:323-330` (pre-fix
numbering)**. A background poll (60 s interval, 20 min cap) watched for the
inventory; it **landed at 2026-10-17T20:20:34Z**, and its index 0 is
`R26-D1` — the same defect — with `status_at_head: "repaired_at_head"` and
R8-O03's own repro recorded (`phonology rc=2 G-DATA 'unterminated flow
sequence'`). The inventory's `suggested_control` ("fail-before = pre-fix bytes
rc=1 evaluated, pass-after = HEAD") matches this shard's control semantics, so
the fallback selection is corroborated by the authoritative artifact. See §7.

## 1. Defect and pre-fix reproduction

Review claim: `_parse_scalar` used `body = s[1:-1] if s.endswith("]") else s[1:]`,
so a truncated `[p, t, k` became the 3-item list `['p', 't', 'k']`; the gate
audited a document that is not valid YAML and exited 1 with findings instead of
the module docstring's documented exit 2 for an "unparseable packet"
(`phonology-sanity-gate.py:11-15`).

Pre-fix command and output (2026-10-17, before the edit; payload written to a
disposable path, no repo scratch):

```
$ python3 tools/gates/phonology-sanity-gate.py /tmp/neg04-repro/p.yml
FINDING G-DATA: REVIEW — phonology.notable_rules is missing — allophony consistency could not evaluate
FINDING M-CLASS: REVIEW — no phonemic nasals, fricatives in the inventory: …
FINDING T-C: REVIEW — 3 distinct consonants — outside the WALS sample bands …
phonology rc=1
$ python3 tools/gates/naming-collision-gate.py /tmp/neg04-repro/p.yml
FINDING G-DATA: HOLD — input could not be evaluated: unterminated flow sequence: '[p, t, k'
naming rc=2
```

`p.yml` = `name: t` / `phonology:` / `  consonants: [p, t, k` / `  vowels: [a, e, i]` /
`  phonotactics: (C)V` / `  tones: 0`. The phonology gate printed a *linguistic
finding* (T-C) about invalid YAML; the naming gate on identical bytes returned
the documented exit 2. Defect confirmed.

## 2. Repair

`tools/gates/phonology-sanity-gate.py`, `_parse_scalar` (pre-fix lines 323-330;
the shard's hunk sits at 328-338 after sibling repairs landed in the same file)
— reject unbalanced flow starts, mirroring the naming gate's `_parse_flow`
policy (`naming-collision-gate.py:335-339`, review 26's recommended move 1). The
existing `PacketError` catch in `run_text` already maps the raise to `exit 2` +
one `G-DATA` finding, so no other code changes.

```diff
 def _parse_scalar(s):
     s = s.strip()
     if s.startswith("["):
-        body = s[1:-1] if s.endswith("]") else s[1:]
+        if not s.endswith("]"):
+            raise PacketError("unterminated flow sequence: %r" % s[:40])
+        body = s[1:-1]
         return [_parse_scalar(p) for p in _flow_parts(body)]
     if s.startswith("{"):
-        body = s[1:-1] if s.endswith("}") else s[1:]
+        if not s.endswith("}"):
+            raise PacketError("unterminated flow mapping: %r" % s[:40])
+        body = s[1:-1]
```

At this shard's write time `git diff --stat` showed
`1 file changed, 6 insertions(+), 2 deletions(-)` for this file (sha256
`660278f2…`). Sibling O-shards then landed their own repairs in the same file
(tab-indentation rejection, anchor/tag rejection, fixture pinning); the
combined tree now carries all of them and this shard's hunk is unchanged
within it (sha256 `722ff91b…`, verified by re-running the control, below).
No docstring described the old lenient behavior, so none needed amending; the
`:11-15` contract now matches the code.

## 3. Post-fix verification (command evidence)

```
$ sha256sum tools/gates/phonology-sanity-gate.py
660278f22d9f4e1d295aba19afa3b3014b7bd8b0e4fd1a503b594a84ab98e1f8   # this shard's write, 20:15:43Z
722ff91bd0d41482ee14be37b9b410d887f77b007a9b0c8555d0bf3f48b43cb7   # combined tree, 20:18:59Z

$ python3 tools/gates/phonology-sanity-gate.py --selftest
selftest: fixture exit 1; 15/15 planted finding IDs present; 26 control cases passed
selftest rc=0

$ python3 tools/gates/phonology-sanity-gate.py /tmp/neg04-repro/p.yml
FINDING G-DATA: UNEVALUABLE — packet could not be parsed: unterminated flow sequence: '[p, t, k'
rc=2

$ for g in phonology-sanity-gate naming-collision-gate myth-consistency-gate \
           costume-era-consistency-gate lexicon-coverage-audit; do
      python3 tools/gates/$g.py /tmp/neg04-repro/p.yml; done   # 2026-10-17T20:15:29Z
phonology-sanity-gate  rc=2  (unterminated flow sequence)
naming-collision-gate  rc=2  (unterminated flow sequence)
myth-consistency-gate  rc=2  (unterminated flow sequence)
costume-era-consistency-gate rc=2
lexicon-coverage-audit rc=2  (unterminated flow value)

$ python3 tools/check-gate-battery.py        # isolated mirror, 2026-10-17
{"summary": {"battery_exit": 0, "fail": 0, "pass": 7, "unevaluable": 0}, …}
battery-main rc=0    # all seven gate selftests pass, originals preserved

$ python3 tools/check-gate-battery.py        # re-run 20:19Z on the COMBINED tree
                                             # (sibling repairs to all gates landed)
{"summary": {"battery_exit": 0, "fail": 0, "pass": 7, "unevaluable": 0}}
battery rc=0    # costume/handoff/lexicon/myth/naming/phonology/provenance all exit=0

$ python3 tools/check-gate-battery.py        # 20:21Z, mid-swarm transient
{"summary": {"battery_exit": 2, "fail": 0, "pass": 6, "unevaluable": 1}}
battery rc=2    # naming-collision-gate.py unevaluable: its --selftest raised
                # AssertionError "fixture finding counts changed" at :1634 —
                # a concurrent sibling edit in that gate (51+/13- in flight), NOT
                # this shard's file. phonology passed in this run too.

$ python3 tools/check-gate-battery.py        # 20:21:59Z, after the sibling landed
{"summary": {"battery_exit": 0, "fail": 0, "pass": 7, "unevaluable": 0}}
battery rc=0    # naming recovered; all seven green again
```

Post-fix the repaired gate now agrees with its four siblings on the truncated
bytes (all rc=2) while keeping its own 26-case selftest green and the
seven-gate battery green (7/7, no tree drift) at 20:15Z, 20:19Z and 20:21:59Z.
The 20:21Z red run is recorded above for honesty: it was a transient mid-edit
state in the naming gate (a different shard's file, since recovered), and this
shard deliberately did not touch it. Independent corroboration of the battery
method (and its explicit pre-repair caveat) is R8-O14's
`reports/round-8/operability/battery-rerun.json`; the green runs above are this
shard's own measurements.

## 4. Negative control

`reports/round-8/operability/neg-controls/neg-04/neg-04-control.py` — stdlib
only; writes payloads solely into `tempfile.TemporaryDirectory()`; invokes the
gate under test as a subprocess; never writes inside the repository. Six
checks: three truncated-flow shapes must be rejected (`rc=2`, only `G-DATA`,
named diagnostic), the same truncated payload on the `-` stdin path must be
rejected, a *closed twin* of the same packet must still evaluate (`rc=1`,
`G-DATA`+`T-C`), and a complete valid packet must stay clean (`rc=0`).

**Post-fix run (live gate, 2026-10-17T20:18:59Z, combined tree sha256
`722ff91b…`; the earlier run at 20:15:43Z against this shard's own bytes
`660278f2…` was 5/5 with the same five checks before the stdin check was
added):**

```
$ python3 reports/round-8/operability/neg-controls/neg-04/neg-04-control.py
NEG-04 gate sha256: 722ff91bd0d41482ee14be37b9b410d887f77b007a9b0c8555d0bf3f48b43cb7
NEG-04 truncated-flow-sequence     rc=2 ids=G-DATA PASS
NEG-04 truncated-flow-mapping      rc=2 ids=G-DATA PASS
NEG-04 nested-unbalanced-flow      rc=2 ids=G-DATA PASS
NEG-04 closed-twin-still-evaluates rc=1 ids=G-DATA,M-CLASS,T-C PASS
NEG-04 valid-packet-still-clean    rc=0 ids=- PASS
NEG-04 stdin-truncated-flow        rc=2 ids=G-DATA PASS
NEG-04 RESULT: PASS (6/6 checks)
control rc=0
```

**Pre-fix run (same control, pinned pre-fix bytes):**

```
$ git show cf338a7:tools/gates/phonology-sanity-gate.py > /tmp/neg04-prefix.py
$ sha256sum /tmp/neg04-prefix.py
fb05c644cafb0855481beb5d8bc3f619ae688d8b12787e530f01543f85372655   # == review 26 §0 pin
$ python3 …/neg-04-control.py --gate /tmp/neg04-prefix.py
NEG-04 note: this is the review-26 pinned PRE-FIX byte copy (fb05c644...); checks below are expected to FAIL.
NEG-04 truncated-flow-sequence     rc=1 ids=G-DATA,M-CLASS,T-C FAIL
NEG-04 truncated-flow-mapping      rc=1 ids=G-DATA FAIL
NEG-04 nested-unbalanced-flow      rc=1 ids=G-DATA,M-CLASS,T-C FAIL
NEG-04 closed-twin-still-evaluates rc=1 ids=G-DATA,M-CLASS,T-C PASS
NEG-04 valid-packet-still-clean    rc=0 ids=- PASS
NEG-04 stdin-truncated-flow        rc=1 ids=G-DATA,M-CLASS,T-C FAIL
NEG-04 RESULT: FAIL (4/6 checks)
NEG-04 FAILURE: truncated-flow-sequence: PRE-FIX PATTERN OBSERVED: rc=1 ids=['G-DATA', 'M-CLASS', 'T-C'] …
prefix-control rc=1
```

So the control **fails on the pre-fix pattern** (exit 1, naming the pattern:
the gate evaluated invalid YAML) and **passes post-fix** (exit 0, 6/6).

## 5. Reproduce

```bash
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
python3 reports/round-8/operability/neg-controls/neg-04/neg-04-control.py        # → exit 0
git show cf338a7:tools/gates/phonology-sanity-gate.py > /tmp/neg04-prefix.py
python3 reports/round-8/operability/neg-controls/neg-04/neg-04-control.py \
        --gate /tmp/neg04-prefix.py                                              # → exit 1
python3 tools/gates/phonology-sanity-gate.py --selftest                          # → exit 0
python3 tools/check-gate-battery.py                                              # → exit 0, 7/7
```

## 6. Limits (untested, stated)

- Only review 26 D1 is this shard's scope. Register entries D2-D9 and review 29
  F1-F6 are sibling shards' (or the review's own) business; review 26 D10 (no
  cross-gate conformance fixture) remains open and is not claimed here.
- The control's checks assert this shard's diagnostic strings
  ("unterminated flow sequence" / "unterminated flow mapping"); a future reword
  of those messages would require updating the control (it would then fail
  loudly, not silently pass).
- The battery's `--selftest` mode runs the battery's own 10 controls only; the
  seven-gate run is the no-flag mode used above. R8-O14's formal rerun receipt
  predates the repairs (its own caveat says so), so the post-repair battery
  green is this shard's own measurement, not O14's.
- Concurrency note: sibling O-shards kept landing their own repairs in the same
  gate file (tab-indentation rejection, anchor/tag rejection, fixture pinning)
  after this shard's write; the file hash moved `660278f2…` (this shard's own
  bytes, 20:15:43Z) → `722ff91b…` (20:18:59Z) → `b3764f00…` (20:21:16Z) →
  `e8d8ee9a…` (20:22:06Z, latest observed). At every observed state this
  shard's hunk was unchanged within the file (`_parse_scalar` raises at
  `:338`/`:343`), the control passed 6/6, and the seven-gate battery was 7/7
  (the single 20:21Z red run was the naming gate mid-edit; it recovered at
  20:21:59Z). The hashes keep moving as siblings land work; a final
  integrated-tree hash belongs to the orchestrator's commit, not this receipt.

## 7. Inventory poll outcome

The poll ran its full 20-check window. `defect-inventory.json` landed at
2026-10-17T20:20:34Z (check 8 of 20) and is R8-O03's artifact listing 20
defects. Index 0 is `R26-D1` — this shard's defect, marked
`status_at_head: "repaired_at_head"`; indices 2-13 are the other review-26
entries and 15-20 the review-29 entries, distributed across shards
R8-O05..O13. No renumbering conflict arose: the fallback selection and the
inventory's index 0 agree. (The poll's own `/tmp` copy of the inventory
failed with "No space left on device" during the swarm's tmpfs pressure; the
in-repo file was read directly, so no evidence here depends on that copy.)
