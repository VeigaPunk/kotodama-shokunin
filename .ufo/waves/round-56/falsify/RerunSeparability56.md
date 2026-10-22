# RerunSeparability56 — round 56 falsify, separability rerun (2026-10-22)

Seat: KotodamaR56.RerunSeparability56 (leaf, read-only in lane; all writes in sandbox
`/fast/scratch/hyaku/kotodama-r56-falsify/RerunSeparability56/` and this report).
Assignment: rerun the declared separability control on claim C's tree with the uncommitted
record draft (corpus/lessons/round-56.md) as stand-in, cross-grep the two claims' lands,
and run each claim's acceptance on base plus that claim's lands only.

## Verdict

**CARRIED — separability holds on the declared control and my independent probes found
no cross-dependency.** The declared command (`python3 -B tools/check-claim-separability.py
reports/round-56/separability-manifest.json`) at C's tree (767040e) with the stand-in
record draft exits 0: `SEPARABILITY: 0 findings`, note `units=3 ordered_pairs=6
acceptance_runs=2` (2.38 s). Cross-greps: O's landed tool names zero ids from C's block
S359-S418 (full-text scan of tools/check-gate-quotes.py at 7576fd4; its only S-ids are the
declared base fixture ids S900 and S901, 43 occurrences total, outside C's block); C's
landed files name zero O land paths (no occurrence of `check-gate-quotes`,
`check-source-access`, `check-claim-separability`, `accept-o` or `accept-c` in
kongo-kingdom.md, corpus/README.md or corpus/SOURCES.md — the single tool mention in the
entry is C's own accept-c.py). Both single-claim acceptance runs pass on base plus their
own lands only (accept-c exit 0, accept-o exit 0) and both fail on bare base (exit 1),
confirming each claim is load-bearing and non-dependent.

## Checked items

- **reports/round-56/separability-manifest.json — CARRIED.** Sandbox clone
  `/fast/scratch/hyaku/kotodama-r56-falsify/RerunSeparability56/lane` checked out at
  767040e; stand-in record draft copied from the lane worktree
  (uncommitted, 59 lines, 54 S-id mentions); run as declared: `python3 -B
  tools/check-claim-separability.py reports/round-56/separability-manifest.json`.
  Evidence: stdout `SEPARABILITY: 0 findings` / `SEPARABILITY_NOTE units=3
  ordered_pairs=6 acceptance_runs=2`, exit 0. 3 units (C, O, REC), 6 ordered pairs,
  2 acceptance runs — every declared leg actually ran.
- **tools/check-gate-quotes.py (O, 7576fd4) vs C's id block — CARRIED.** Full-text scan
  for `\bS(359|3[6-9][0-9]|40[0-9]|41[0-8])\b` over the O commit's tool bytes: zero
  matches. The only S-ids anywhere in the tool are S900 (41x) and S901 (2x), the declared
  base fixture ids, outside C's reserved block.
- **corpus/knowledge/civilizations/kongo-kingdom.md + corpus/README.md + corpus/SOURCES.md
  (C, 767040e) vs O's land path — CARRIED.** Grep for `check-gate-quotes`,
  `check-source-access`, `check-claim-separability`, `accept-o`, `accept-c`: only hit is
  kongo-kingdom.md:10 naming C's own `reports/round-56/accept-c.py`; no O land path
  (`tools/check-gate-quotes.py`) appears. The separability tool's whole-path rule
  (`tools/x.py` is not named by `old-tools/x.py` etc.) not needed — no near-miss either.
- **accept-c on base + C lands only — CARRIED.** Base materialized with
  `git archive 045f458 | tar -x` (git-free copy, mirroring the tool's git-free
  counterfactual), C's three lands overlaid, `python3 -B reports/round-56/accept-c.py`
  exit 0: all seven legs PASS (SET count=232 added=[kongo-kingdom.md] removed=[];
  SWEEP rows 232 files 232 missing_from_index 0; FLOOR cited=54 floor=20; RANGE,
  STATUS, USEDBY, ACCESS all PASS). Same run on bare base: exit 1 (SET FAIL count=231,
  SWEEP FAIL 231, FLOOR FAIL cited=0; RANGE/STATUS/USEDBY vacuous PASS) — matches the
  declared `before` behavior exactly.
- **accept-o on base + O lands only — CARRIED.** Base copy + O's one land
  (tools/check-gate-quotes.py at 7576fd4), `python3 -B reports/round-56/accept-o.py`
  exit 0, all eight legs PASS (ENTITY count=16, NOFALSE, EXIT round55=1 fixture=1,
  DECODE, KEEP, BADUTF8 exit=2, FORMAT, SELFTEST 38/38). On bare base: exit 1 with
  ENTITY FAIL count=0 (16 html-entity rows missing), EXIT FAIL round55=0, DECODE FAIL,
  BADUTF8 FAIL exit=1 traceback=True, SELFTEST 27/27 — i.e. the old tool fails exactly
  as O's claim says it did before.

## Residual risk / notes

- The declared command's dynamic leg runs acceptances git-free (`needs_git` unset in the
  manifest), so nothing git-write can leak from the declared run. My rerun in the sandbox
  used only read-only git against the lane (`archive`, `cat-file` equivalent, `worktree add`
  inside the sandbox clone — never the lane itself).
- One probe detail, not a defect: at a bare `git archive` materialization of base,
  accept-c fails SWEEP/FLOOR because the record draft (with the round's Gate lines) is
  absent — the tool's own counterfactual includes the record unit's lands only as
  *overlay candidates for repair*, not in the base fixture, so the declared 0-findings
  result rests on C passing on base+C.lands, which I verified directly (overlay run
  exit 0 above). No finding; the manifest's REC unit is declared `role: record` and the
  tool never scans it as a dependee, per the tool's documented rule.
- Not run: the agreement command `python3 -B reports/round-56/claims-agree.py` (out of my
  scoped axes), the full 91-file QUALITY rerun, and any re-opening of sources (other seats).

No tool installs were made (python3.13 stdlib + git only).
