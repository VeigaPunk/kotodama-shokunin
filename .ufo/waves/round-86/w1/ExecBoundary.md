# ExecBoundary — r86-v1 controls review (frozen measure86.py pre-dispatch)

Seat: ExecBoundary (leaf executor, godspeed). Axes: depth + operability. Date: 2026-11-04.
Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, base `1e6b10a0`, freeze `16c26783`, HEAD at probe time `079fbf59`.
Artifact: `.ufo/waves/round-86/w1/stage/ExecBoundary/controls-review.json` (+ `receipts/`).

## What ran

Extracted the frozen counter with `git show freeze:reports/round-86/measure86.py` (read-only, `-C` lane) and asserted its sha256 `15cf5412…f19fe` equals both the freeze blob and the `# counter sha256 (self)` line L1 captured — probe copy, frozen bytes and L1's executed counter are identical. Ran 15 CLI probes (P01–P14 + selftest) against the lane repo with the frozen copy; all lane access read-only; the only git writes anywhere were the counter's own selftest fixtures inside its `TemporaryDirectory` toplevels under the seat `--work` dir. Lane invariant held: HEAD, porcelain status and `count-objects -v` identical before/after; zero fixture leftovers. No installs (python 3.14.8 / git 2.56.0 preexisting); pacman pause honored.

## Observed control verdicts

| Control | Observed | Verdict |
|---|---|---|
| full 40-hex commit ids | rc2 `refused: full commit id required` (short sha P07, tree sha P08, absent sha P09) | green (coarse, L4) |
| freeze ⊆ first-parent(lands) | rc2 `refused: freeze not on lands first-parent chain` (P01,P02,P10,P13); freeze is first-parent ancestor of HEAD | green |
| frozen cfg loads at freeze | rc2 raw json error at freeze=base (P11) | green (leaky, L5) |
| LEGCOUNT | P03/P04 passed (`# frozen legs: 7/8`), lists match claims.json | green; refusal path unexercised (L2) |
| existing `--work` | rc2 `refused: existing --work required` (P12) | green |
| unchanged base (lands==cfg.base) | shadowed: P01/P02 refused at ancestry first | **finding** (L1) |
| lint authority | freeze blob sha256 == pinned `a9b0fb…804a`; lint executes from the freeze blob, not lands | green |
| counter self-attestation | per-run sha line == extraction == L1 capture | green |

Leg dispositions (pre-landing, expected red): D lands=freeze/HEAD → `FAIL legs=3/7` (FROZENCFG, BEFORE, LINT pass; LINT vacuously green on the empty entry, L6). O lands=freeze/HEAD → `FAIL legs=2/8` (TOOL absent → SELFTEST/IRON_*/HELDOUT fail `tool absent`; REGISTRY red — SKILL.md at freeze and HEAD mentions neither the tool path nor `paragraph-locator`). Iron.html blob is present at freeze, so IRON has its substrate.

## Headline findings

1. **`unchanged base` refusal is dead under the lane shape.** The code orders ancestry before unchanged-base; with base a first-parent ancestor of freeze (observed), `--lands base` always refuses with `freeze not on lands first-parent chain` (P01/P02), never `unchanged base`. The predicate is reachable only when `cfg.base` is freeze-or-descendant — a degenerate cfg nothing exercises. The selftest's final check asserts only the `refused:` prefix, so its 8-check PASS cannot distinguish which predicate fired; kill_rule's "refusing the unchanged base is necessary" holds behaviorally (rc2) but the named predicate is unproven. No post-data revision made; recorded as limitation L1 + repair R1.
2. **LEGCOUNT refusal has no selftest coverage** (no `c['legs']` mutation case); alignment is static plus observed pass-through (L2/L3).
3. **Tool authority asymmetry:** lint is freeze-pinned; the O tool is measured from the lands blob unpinned — by design for capability acquisition, but nothing freezes a tool reference (L7, R7).
4. `# measured revision (lane main)` prints lands verbatim; no control ties lands to actual lane main (L8). Hard 60s subprocess ceiling escalates to whole-claim refusal (L9). `TypeError` escapes the refusal handler (L10). No presence pre-check for cfg-declared freeze blobs like `c['html']` (L11). First-parent-only ancestry means merges off the freeze chain refuse — landing must stay linear (L12).

Drift check: HEAD `079fbf59` ("preserve predispatch refusal and absent-land controls") changed **no frozen bytes** — counter and claims blobs are unchanged; it only added L1 capture files (numstat observed). My independent outputs reproduce L1's `pre-dispatch-controls.json`, leg lines and `counter-selftest.txt` exactly.

Post-probe note: lane HEAD advanced to `8efa380a` ("round-86: add article paragraph ordinal locator") after the probe window; frozen counter and claims blobs re-verified unchanged vs freeze (read-only diff). Probes above were observed against `079fbf59`.

## Repairs suggested (future rounds only; none applied)

R1 exact refusal-string assertions in selftest + degenerate `cfg.base==freeze` fixture; R2 selftest mutations for LEGCOUNT/short-sha/tree-sha/missing-work/truncated-cfg; R3 split rev refusal causes; R4 context-wrap cfg parse errors; R5 pre-dispatch presence check for cfg freeze blobs; R6 catch TypeError; R7 pin the O tool sha in a future freeze; R8 distinct timeout refusal label.

## Compliance

No commits, no ref/index mutation anywhere; frozen predicate/counter/claims unmodified (blob equality observed). No builds/lint/tests beyond the assigned bounded probes. No sibling/operator files touched; writes limited to this seat's stage dir, receipts and this report. Scratch `/fast/scratch/hyaku/kotodama-r86/ExecBoundary` removed after receipts were copied into stage.

Report: .ufo/waves/round-86/w1/ExecBoundary.md
Controls-Review: .ufo/waves/round-86/w1/stage/ExecBoundary/controls-review.json
