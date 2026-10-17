# neg-09 — negative control + repair receipt (shard R8-O09, defect index 5)

- **Round:** 8 · **shard:** R8-O09 (operability) · **claim:** O
- **Date:** 2026-10-17 (all commands below; UTC clock read
  `2026-10-17T20:19:38Z` at the last evidence run)
- **Baseline:** declared `e7ca0fa…` (`reports/round-8/claims.json`), worktree
  HEAD `cf338a7` — the four repaired gates were byte-identical at both
  revisions (their sha256 equals the review-26 §0 pins, e.g.
  `fb05c644…` for phonology), so the defect and its control bind to the
  declared baseline.
- **Role:** repair shard. Writes only the repaired gate regions, this
  directory's control/evidence, and this report. No commit.
- **Defect owned:** review 26 §3 **D5** — "Tab indentation has four different
  outcomes" (medium), including that register entry's multi-document note for
  `naming-collision-gate.py`.

## 0. Defect selection (dependency status)

`reports/round-8/operability/defect-inventory.json` (R8-O03's artifact) did
**not exist** for the whole work window:

```
$ ls reports/round-8/operability/            # 2026-10-17, first check ~17:12 local
battery-rerun.json  neg-controls/  o01-diagnosis.md  o02-fix.md
$ find reports/round-8 -name defect-inventory.json   # last check 2026-10-17T20:19:38Z
(no output)
```

Per the shard fallback ("if inventory lands late, fall back to the two named
reviews directly"), both named reviews were read:
`reports/supplement-opencode-1/26-parser-controls.md` and
`reports/supplement-opencode-1/29-local-boundaries.md`. Register order is
review 26 §3 **D1–D9**, then review 29 **F1–F5**; the 5th register entry is
review 26 §3 **D5**. The same convention is visible in the sibling receipt
`reports/round-8/operability/neg-controls/neg-04/neg-04-report.md` §0, which
documents the identical fallback and owns the 1st register entry (D1). D5 was
confirmed by direct reproduction (§1) before any edit.

## 1. Defect and pre-fix reproduction

Review 26 §3 D5 claims tab indentation had four outcomes across the five
culture-packet gates, and that `naming-collision-gate.py` merged
`---`-separated documents instead of rejecting the stream its own docstring
declares outside the subset (`naming-collision-gate.py:57-60`).

Pre-fix capture (2026-10-17, before the edit; payloads written to a
`TemporaryDirectory`, nothing under the repo):

```
$ python3 reports/round-8/operability/neg-controls/neg-09/probe-prefix.py
tab-indent      phonology-sanity-gate.py         rc=0   (silent)
tab-indent      naming-collision-gate.py         rc=2   FINDING G-DATA: HOLD — … tab indentation is not supported by this subset
tab-indent      myth-consistency-gate.py         rc=2   FINDING G-DATA: unparsed YAML content at token 7
tab-indent      costume-era-consistency-gate.py  rc=2   FINDING G-DATA: … no `costumes` declared: nothing to review
tab-indent      lexicon-coverage-audit.py        rc=2   ERROR: … tabs are not allowed for indentation
multi-document  naming-collision-gate.py         rc=1   FINDING PHON-ONSET: FAIL — name N2 'tl' cannot be syllabified …
leading-marker  naming-collision-gate.py         rc=1   FINDING NAME-INVENTORY: HOLD — packet supplies no `names` inventory …
```

Full capture: `evidence-prefix-live.txt`. On the minimal packet the costume
gate exits 2 for a different reason (no `costumes` key), so the silent
acceptance was re-measured on the committed fixtures, converted with 2-space →
1-tab indentation:

| gate | space-indented fixture | tab-indented twin (pre-fix) |
|---|---|---|
| phonology | rc=1, 16 finding ids | **rc=1, identical 16 ids** (tabs silently rewritten to 2 spaces) |
| costume | rc=1, 25 finding ids | **rc=1, identical 25 ids** (tabs silently rewritten to 4 spaces) |
| myth | rc=1, `MC-P01`… | **rc=2, `unparsed YAML content at token 6`** (guard misses leading tabs) |
| naming | rc=1, `NAME-REUSE`… | rc=2, tab diagnostic (already correct) |
| lexicon | rc=1, `C-contrast-lost`… | rc=2, tab diagnostic (already correct) |

And the naming gate on a two-document stream (`---` between two packets):
pre-fix **rc=1** with `PHON-ONSET, CROSS-HOLD` — i.e. the union of both
documents was evaluated, exactly as the review filed it.

## 2. Repair

Four surgical edits; every raise reuses the gate's own error type so the
existing CLI boundary maps it to the documented exit 2:

- `tools/gates/phonology-sanity-gate.py:291-294` (`_preprocess`) — reject a tab
  in the leading whitespace before the existing tab-normalization runs:
  `raise PacketError("tab indentation is not supported by this subset (line N)")`.
- `tools/gates/costume-era-consistency-gate.py:343-345` (`parse_packet`) — same
  check on the raw line before `text.replace("\t", "    ")` rewrites it:
  `raise Malformed("tab indentation is not supported by this subset")`.
- `tools/gates/myth-consistency-gate.py:335` (`parse_packet`) — the guard
  computed its indent from spaces only, so a leading tab produced an empty
  prefix and slipped through; the prefix now strips `" \t"`:
  `indent_text = stripped[: len(stripped) - len(stripped.lstrip(" \t"))]`.
- `tools/gates/naming-collision-gate.py:146-165` (`_split_lines`; multi-document
  guard at `:152-158`) — a
  `---`/`...` line after any content (or after another marker) now raises
  `YamlError("multi-document streams are not supported by this subset")`
  instead of being skipped and merging the documents. A single leading `---`
  (document-start marker, not a second document) stays accepted.

Semantics chosen: the family's declared subset policy, already implemented by
`naming-collision-gate.py` and `lexicon-coverage-audit.py` and recommended by
review 26 §6 moves 3–4 — input outside the subset exits 2 with an explicit
diagnostic instead of being guessed. No docstring described the old lenient
behavior in phonology/costume/myth (their exit-2 contracts say
"unparseable packet/input"), and the naming docstring's "No … multi-document
streams … exits 2" line is now true; no docstring amendments were needed.
No committed fixture, example packet, or corpus packet uses tab indentation or
a `---` marker (`grep -rn "^---" examples/ corpus/ tools/gates/fixtures/` →
no matches; no fixture contains a tab), so the repair cannot regress a
committed packet.

## 3. Post-fix verification (command evidence)

```
$ python3 tools/check-gate-battery.py --selftest
SELFTEST OK 10/10 controls behaved as expected          # rc=0
$ python3 tools/check-craft-exercise.py --selftest
SELFTEST OK 10/10 tamper cases detected
CLI-SELFTEST OK 18/18 cases passed                      # rc=0

# five gate selftests, copied tree (fixture-writing gates never touch the repo):
phonology-sanity-gate exit=0 :: selftest: fixture exit 1; 15/15 planted finding IDs present; 26 control cases passed
naming-collision-gate  exit=0 :: selftest: OK — fixture findings 12 across 11 ids
myth-consistency-gate  exit=0 :: selftest: OK — fixture exit 1; planted IDs present
costume-era-consistency-gate exit=0
lexicon-coverage-audit exit=0 :: selftest: 14/14 checks passed

# both example packets, live (repaired) gates vs pre-fix baseline copies,
# full stdout compared byte-for-byte:
examples/culture-d2/packet.d2.yml   all five gates: rc and output IDENTICAL
examples/culture-d3/packet.gates.yml all five gates: rc and output IDENTICAL
```

Post-fix, identical tab-indented bytes now produce the same verdict class in
all five gates (rc=2, tab diagnostic): see `evidence-postfix-live.txt`.

**Cross-shard consequence — frozen replay (report, not absorb).** Repairing
gate bytes invalidates the round-3 manifest's gate pins:

```
$ python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv   # live gates
REPLAY COULD-NOT-EVALUATE: 7 could-not-evaluate, 0 mismatch, 0 reproduced of 7 row(s)
$ # same copy with the five PRE-FIX gate files restored:
REPLAY COULD-NOT-EVALUATE: 2 could-not-evaluate, 0 mismatch, 5 reproduced of 7 row(s)
```

The 2 residual rows are the pre-existing `provenance-audit.py` mismatch (its
on-disk bytes already differ from the round-3 pin; that file is unmodified in
the worktree — review 29 §F2 flagged the same rows). So the change 5/7 → 0/7 is
caused by the round-8 gate repairs (this shard's D5 plus the D1/D4 owners'
edits). The replay tool is behaving correctly (refusing to replay unpinned
code); the round-8 D-claim replay requirement needs either a re-frozen manifest
or a replay run against pinned copies. Evidence:
`evidence-replay-gate-digest.txt` (live-vs-pin digests included).

## 4. Negative control

`reports/round-8/operability/neg-controls/neg-09/neg-09-control.py` — stdlib
only; payloads and extracted baseline bytes live in
`tempfile.TemporaryDirectory()`; gates are subprocesses; nothing under the
repository is written. 17 checks: per-gate tab rejection (C1–C5), a cross-gate
conformance check on identical bytes (C6, review 26 §6 rec 7), space-indented
fixture twins that must keep their captured pre-fix verdicts (C7), the naming
multi-document rejection (C8), and the leading-marker no-over-rejection case
(C9). `--baseline-rev REV` extracts `REV:tools/gates/<gate>.py` with `git show`
and verifies the review-26 §0 pins before running.

**Post-fix run (live gates):**

```
$ python3 …/neg-09-control.py                    # 2026-10-17T20:20:5xZ
NEG-09 phonology-sanity-gate.py         sha256=b3764f00a0571198 (post-fix/modified)
NEG-09 naming-collision-gate.py         sha256=db3cee7cd907ab28 (post-fix/modified)
NEG-09 myth-consistency-gate.py         sha256=48477d38dfa16178 (post-fix/modified)
NEG-09 costume-era-consistency-gate.py  sha256=6be04578fc219949 (post-fix/modified)
NEG-09 lexicon-coverage-audit.py        sha256=989b129535f24c6c (post-fix/modified)
… 17 checks, all PASS
NEG-09 RESULT: PASS (17/17 checks)                      # rc=0
```

The control re-hashes the gates on every run; sibling O-shards kept editing the
same files during this window (earlier post-fix runs recorded
`722ff91b…/ab98fe1a…/270e4e0f…/590e7f65…/989b1295…` and still passed 17/17),
which is incidental evidence that the repair survives concurrent sibling
edits.

**Pre-fix run (pinned baseline bytes):**

```
$ python3 …/neg-09-control.py --baseline-rev cf338a7
NEG-09 note: all five gates match the review-26 §0 pre-fix pins; the tab and multi-document checks below are expected to FAIL.
NEG-09 phonology-sanity-gate/tab-indent       rc=0 ids=- FAIL
NEG-09 costume-era-consistency-gate/tab-indent rc=1 ids=T-03,EAR-04,… FAIL
NEG-09 myth-consistency-gate/tab-indent       rc=2 ids=G-DATA FAIL   # message: unparsed YAML content at token 6
NEG-09 naming-collision-gate/multi-document   rc=1 ids=PHON-ONSET,CROSS-HOLD FAIL
NEG-09 RESULT: FAIL (7/17 checks)                       # rc=1
```

So the control **fails on the pre-fix pattern** (exit 1, each failure naming
its pattern) and **passes post-fix** (exit 0, 17/17). Full outputs:
`evidence-control-prefix.txt`, `evidence-control-postfix.txt`.

## 5. Reproduce

```bash
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
python3 reports/round-8/operability/neg-controls/neg-09/neg-09-control.py               # → exit 0
python3 reports/round-8/operability/neg-controls/neg-09/neg-09-control.py \
        --baseline-rev cf338a7                                                          # → exit 1
python3 reports/round-8/operability/neg-controls/neg-09/probe-prefix.py                 # matrix probe
for g in phonology-sanity-gate naming-collision-gate myth-consistency-gate \
         costume-era-consistency-gate lexicon-coverage-audit; do
  python3 tools/gates/$g.py --selftest; done                                            # → exit 0 ×5
python3 tools/check-gate-battery.py --selftest                                          # → exit 0
python3 tools/check-craft-exercise.py --selftest                                        # → exit 0
```

## 6. Limits (untested, stated)

- Scope is review 26 §3 D5 only (tabs across the five gates + the naming
  multi-document merge). Register entries D1–D4 and D6–D9 and review 29
  F1–F5 belong to sibling shards; D10 (no cross-gate conformance fixture in
  the registered battery) is **partially** answered by this control's C6 but
  the control is not registered in `tools/check-gate-battery.py`, so the
  battery still does not cover it.
- Tab detection covers the indentation prefix only. A tab *inside* a scalar
  (after content) is still normalized to spaces by phonology/costume, as
  before the repair — unchanged behavior, not newly controlled.
- `replay-frozen.py --selftest` could not be completed: it aborted with
  `OSError: [Errno 28] No space left on device` in `/tmp` while this shard's
  copies filled the tmpfs; the copies were removed afterwards
  (`df /tmp` → 8.5 G free). The replay experiment in §3 was run in a copied
  tree, not against the live tree.
- Concurrency: the worktree carries other shards' edits to the same files (live
  hashes move between runs). The post-fix control run above records the gate
  hashes at its own run time; my four fix sites were re-verified present
  immediately before that run.
- The pre-fix demonstration uses the declared baseline `cf338a7` bytes, which
  equal the review-26 §0 pins; the control verifies those pins and prints
  "PRE-FIX pinned bytes" per gate when they match.

## 7. Inventory poll outcome

`reports/round-8/operability/defect-inventory.json` never appeared during this
shard's window (first check ~17:12 local, last check 2026-10-17T20:19:38Z;
`find reports/round-8 -name defect-inventory.json` → no output). The fallback
selection in §0 stands. If O03's inventory later numbers its entries
differently, the defect this shard repaired is identified unambiguously by
content: review 26 §3 D5 (tab indentation) plus the same entry's
multi-document note.
