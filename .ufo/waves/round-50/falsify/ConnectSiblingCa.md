# ConnectSiblingCa — round 50, falsify wave

Seat `KotodamaR50-2.ConnectSiblingCa-21` (falsify, leaf). Item attacked: **Ca — calibration**
(`tools/check-claim-separability.py`, frozen `reports/round-50/separability/r49-fixture.json` +
`r49-expected-independent.txt`, `corpus/QUALITY.md` criterion 7) at landed commit
`1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0`, base `4ad26836552462d28a946ca3b067cab0b5ce3532`.
Plus the assigned cross-lane question: would the same tool have caught the game-dev-2d r105 and
kagi r27 separability rejections named in `.ufo/waves/round-50/build/ConnectSiblingSeparability.md`.

All reads at the commit via a private `git clone --shared` under `/tmp` (deleted at the end);
no installs; no lane write outside this file; no mutating git/jj command in the lane. No source
re-openers apply (the item has no external URL).

Axes named: **calibration** (does the checker's verdict separate real from declared?),
**operability** (durable tool, exit contract, reproducibility), **coverage** (does the round's
own dependency on the frontier stay visible?). The attack below finds that Ca improves both the
false-positive side (selftest negative controls) and the r49 detection, but its green on round 50
is manufactured by a second, contradicting lands declaration — the exact class the build wave
warned about.

## Verdict: PARTIAL (tool HOLDS; Ca's declared round-50 green does not)

The tool is real and does what its docstring says: 56/56 selftest controls pass, the frozen r49
fixture reproduces the independent prediction (exit 1, 6 findings), and the landed r50 manifest
exits 0 in a clean checkout of `1c779e4`. Three things do not hold:

1. Ca's own declared acceptance command is false. `reports/round-50/claims.json:50` says
   "run on `reports/round-50/claims.json` exits 0". The landed tool exits **2** on that file:
   `SEPARABILITY_INPUT_ERROR manifest is missing base, schema`. The validation receipt actually
   ran a different file (`reports/round-50/validation.json`, `claims.Ca.after.values.r50_manifest_rc: 0`;
   `reports/round-50/run-validation.py:62` defaults to `r50-manifest.json`).
2. The r50 manifest's C lands contradict the round's own claim declaration, and the contradiction
   is load-bearing. `claims.json:10` says "C's entry cites SOURCES rows opened by the frontier
   step **(not a claim)**" and `claims.json:18` gives C's lands as the entry + `corpus/README.md`.
   `r50-manifest.json:8-11` adds `corpus/SOURCES.md` to C's lands. Measured: with C's lands per
   `claims.json`, the same tool exits **1** with `C-><base> ... no declared unit's lands repairs
   it`; with the manifest's lands it exits **0**. The green is the declaration, not a measured
   property of the claim.
3. The tool cannot express the round's declared prerequisite shape as a pass. With a `FRONTIER`
   record unit landing `corpus/SOURCES.md` and C's lands per `claims.json`, it exits **1** with
   `C->FRONTIER ... passes on base+C.lands+FRONTIER.lands`. The landed schema has no `non_claim`
   (`tools/check-claim-separability.py:85` `MANIFEST_KEYS = (schema, base, claims)`), so the only
   route to 0 was to move the frontier's file into C. That is the build wave's own warning:
   "the prerequisite label **renames the r49 defect by declaration** — the judge must rule on
   that" (`.ufo/waves/round-50/build/ConnectSiblingSeparability.md:200`). The landed work did not
   rule; it absorbed the file and dropped the label.

`corpus/QUALITY.md:31` criterion 7 is present and grounded, but its last sentence — "Sources a
claim cites are that claim's lands" — is what licenses the absorption. Criterion 7 requires the
checker to be run on "the round manifest" without requiring that manifest to agree with
`claims.json`, and the tool has no lands-provenance/completeness check (zero occurrences of
`diff`/`name-only` in the tool; `_load_units` at `:469` reads only declared lands; overlap at
`:637` is path-level). Measured on the landed manifest: 93 changed paths (89 `.ufo/waves/round-50/`
evidence files + 4 `reports/round-50/telemetry/` files) are owned by no unit, and 3 declared REC
lands (`LOG.md`, `SCORECARD.md`, `corpus/lessons/README.md`) did not change between base and tip.
The build wave's proposed control ("any unassigned changed path exits 1",
`ConnectSiblingSeparability.md:227,262`) was not implemented.

Minor calibration caveat: `run-validation.py:387-405` (`_norm_finding`, `r49_matches`) compares
only `(kind, pair, via-kind, referent)`; it drops the hit locations and the independent file's
occurrence counts (`x1`, `x2`, `x9`, `x12`). "Matches the independent prediction" is therefore a
6-tuple set match, not a reproduction of the prediction's occurrence counts. The counts are
unverified decoration, not a measured claim.

## Evidence

Private checkout and the three runs (paths relative to the clone):

```
$ git clone -q --shared <lane> /tmp/kr50-falsify-ca
$ git -C /tmp/kr50-falsify-ca checkout -q 1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0
$ python3 -B tools/check-claim-separability.py --selftest | tail -1
selftest: 56/56 checks passed - negative controls (...), positive controls (...), malformed or
unevaluable input (exit 2)

$ python3 -B tools/check-claim-separability.py reports/round-50/separability/r49-fixture.json \
    --lane . --root . ; echo RC=$?
SEPARABILITY_DEPENDENCY C->Ca via land path 'tools/check-readme-revisions.py' named at corpus/README.md:18
SEPARABILITY_DEPENDENCY C->S via export '\\bS0(3[1-9]|4[0-7])\\b' matched corpus/knowledge/culture-material/hunting-foraging-subsistence.md:18
SEPARABILITY_DEPENDENCY C->S via land path 'corpus/SOURCES.md' named at corpus/knowledge/culture-material/hunting-foraging-subsistence.md:18
SEPARABILITY_DEPENDENCY S->C via land path 'corpus/knowledge/culture-material/hunting-foraging-subsistence.md' named at corpus/SOURCES.md:60
SEPARABILITY_DEPENDENCY S->Ca via land path 'tools/check-readme-revisions.py' named at corpus/lessons/round-49.md:12
SEPARABILITY_OVERLAP C/Ca corpus/README.md
SEPARABILITY: 6 findings
RC=1

$ python3 -B tools/check-claim-separability.py reports/round-50/separability/r50-manifest.json \
    --lane . --root . ; echo RC=$?
SEPARABILITY: 0 findings
RC=0

$ python3 -B tools/check-claim-separability.py reports/round-50/claims.json --lane . --root . ; echo RC=$?
SEPARABILITY_INPUT_ERROR manifest is missing base, schema
RC=2

# C's lands exactly as reports/round-50/claims.json:18 declares them (manifest otherwise identical):
$ python3 -B tools/check-claim-separability.py /tmp/.../c-claims-lands.json --lane . --root . ; echo RC=$?
SEPARABILITY_DEPENDENCY C-><base> via acceptance [...] fails on base+C.lands (rc=1) and no declared unit's lands repairs it
SEPARABILITY: 1 findings
RC=1

# C's lands per claims.json + a FRONTIER record landing corpus/SOURCES.md:
$ python3 -B tools/check-claim-separability.py /tmp/.../c-frontier.json --lane . --root . ; echo RC=$?
SEPARABILITY_DEPENDENCY C->FRONTIER via acceptance [...] fails on base+C.lands (rc=1) and passes on base+C.lands+FRONTIER.lands
SEPARABILITY: 1 findings
RC=1
```

Land completeness (base→tip, landed manifest):

```
$ git -C /tmp/kr50-falsify-ca diff --name-only 4ad2683 1c779e4 | wc -l   → 107
declared lands                                                          → 17
changed but undeclared                                                  → 93 (89 .ufo/…, 4 reports/round-50/telemetry/…)
declared but unchanged                                                  → 3 (LOG.md, SCORECARD.md, corpus/lessons/README.md)
```

Exact source lines: `reports/round-50/claims.json:10` (frontier not a claim), `:18` (C lands),
`:50` (the false acceptance text); `reports/round-50/separability/r50-manifest.json:8-11` (C lands
incl. `corpus/SOURCES.md` at `:11`), `:20` (C acceptance that fails without it);
`corpus/QUALITY.md:31` criterion 7; `tools/check-claim-separability.py:85,469,491,616,637,667`.

## Cross-lane: would the landed checker have caught r105 / kagi r27?

Short answer: **r105 yes; kagi r27 no, not on the claims as declared.** Both measured with the
same landed checker, private shared clones of the two lanes, no writes to them.

### game-dev-2d r105 — CAUGHT (reusable)

Claim split from that lane's own planner: C2 = `corpus/QUALITY.md` + `corpus/lessons/round-105.md`;
C3 = `corpus/SOURCES.md` + the three `corpus/knowledge/2026-10-19-*.md` entries
(`reports/round-105/r105-R105Planner.md:21-22`). Base `e8990516` has neither `QUALITY.md` nor
`SOURCES.md` (`git cat-file -e e8990516:corpus/QUALITY.md` → 128).

Manifest: base `e8990516`, both units at tree `f67c64ae` (same integrated tip; no per-claim commit
is needed), C2 exports `\bQ(?:[1-9]|1[0-9]|2[0-3])\b`, C3 exports `[]`:

```
SEPARABILITY_DEPENDENCY C2->C3 via land path 'corpus/SOURCES.md' named at corpus/QUALITY.md:6
SEPARABILITY_DEPENDENCY C3->C2 via export '\\bQ(?:[1-9]|1[0-9]|2[0-3])\\b' matched corpus/knowledge/2026-10-19-physics-replay-boundary.md:78
SEPARABILITY: 2 findings
RC=1
```

This is the rejection as stated — "C2 QUALITY creation was C3's admission prerequisite"
(`corpus/lessons/round-105.md:188`) — named in the correct direction at the exact line
(`## Claim-to-CASES binding (Q6)` in the physics-replay entry), plus the reverse edge
(`QUALITY.md:6` names `corpus/SOURCES.md`). With `exports: []` the tool still exits 1 on C2->C3;
the C3->C2 direction needs the Q export declared. Caveat: exports are hand-declared, never
derived from lands (`_check_novelty` at `:491` only rejects an export that matches base bytes of
its own lands), so a manifest that attributes the Q ids to C3 or leaves exports empty loses that
direction. The same-tip tree trick is a real operability win over kagi's revision-bound overlay
runner, which "cannot build one" without a C1-only/C2-only commit.

### kagi r27 — NOT CAUGHT as declared (not reusable for that rejection)

kagi's declared claim lands are the wave tool's own path sets
(`.ufo/waves/round-27/tools/separability.py:30-33`): C1 = `corpus/self-counts.tsv` + 8 knowledge
entries; C2 = `corpus/release-clock.py`. The wave's own artifact overlays exactly those paths and
leaves "their shared bookkeeping pins … at BASE" (`separability.py:14-16`;
`.ufo/waves/round-27/separability.json` `c1_only.overlaid` lists only those 9 paths). Fed the same
declaration, the landed checker returns **0 findings, RC=0** — it reproduces kagi's false green:

```
$ python3 -B tools/check-claim-separability.py kagi-declared.json --lane /tmp/kr50-kagi ; echo RC=$?
SEPARABILITY: 0 findings
RC=0
```

Only when the manifest is *corrected* to declare the nine shared bookkeeping paths under both
claims does it reject — and then by path overlap, not by the mixed hunk:

```
$ python3 -B tools/check-claim-separability.py kagi-shared-both.json --lane /tmp/kr50-kagi ; echo RC=$?
SEPARABILITY_DEPENDENCY C1->C2 via land path 'corpus/lessons/round-27.md' named at corpus/QUALITY.md:132
SEPARABILITY_DEPENDENCY C2->C1 via land path 'corpus/lessons/round-27.md' named at corpus/release-clock.py:375
SEPARABILITY_OVERLAP C1/C2 LOG.md
SEPARABILITY_OVERLAP C1/C2 PROVINCE.md
SEPARABILITY_OVERLAP C1/C2 SCORECARD.md
SEPARABILITY_OVERLAP C1/C2 SKILL.md
SEPARABILITY_OVERLAP C1/C2 corpus/QUALITY.md
SEPARABILITY_OVERLAP C1/C2 corpus/README.md
SEPARABILITY_OVERLAP C1/C2 corpus/claim-ledger.tsv
SEPARABILITY_OVERLAP C1/C2 corpus/lessons/round-27.md
SEPARABILITY_OVERLAP C1/C2 corpus/stamps.tsv
SEPARABILITY: 11 findings
RC=1
```

Assigning the shared files to a REC unit instead (the common integration-owned partition) yields
one finding, `C2->REC via land path 'corpus/lessons/round-27.md' named at corpus/release-clock.py:375`
(a docstring citation; RC=1) — a block, but not the rejection's reason. The rejection's file-level
claim ("C1 and C2 touch disjoint production files", `plans/round-27.md:39`) is only caught if
the manifest author already corrected it; `_overlap_findings` (`:637`) compares declarations and
never derives them. Hunk-level mixing (`SKILL.md @@ -46,3`, `README.md` one section,
`CritSeparability.md:105-120`) is not representable: path granularity reports the whole file as
overlap if both list it, or nothing if one/REC owns it. "The separation mechanism had no artifact"
is out of scope: the checker does not grade claims about overlays.

Reusable-or-not: **partially**. For r105-style dependencies (a claim citing an identifier or a
new path another unit lands) it is reusable and produced the named edge. For kagi-r27-style
co-authorship of a file/hunk it is not a detector; it will certify the round's own defective
partition unless a completeness/ownership rule it does not have is added first.

## Smallest fix

1. Record correction (one line): `reports/round-50/claims.json:50` — replace
   "run on `reports/round-50/claims.json` exits 0" with "run on
   `reports/round-50/separability/r50-manifest.json` exits 0", which is what
   `run-validation.py:62` actually runs.
2. Resolve the lands contradiction in one direction and state it: either add
   `corpus/SOURCES.md` to C's lands at `claims.json:18` and delete "opened by the frontier step
   (not a claim)" at `:10`; or keep the frontier as a producer, add a `non_claim`/`FRONTIER`
   unit to the schema (currently rejected as an unknown key, `:85`) and make its edge print as a
   declared prerequisite with exit 0 — the landed tool exits 1 on that shape, so criterion 7's
   "run … exits 0" cannot be true for the round as declared.
3. Tool gap that made the above invisible (≈20 lines, one place): in `_load_units`/`evaluate`,
   compute `git diff --name-only <base> <unit.tree>` for commit trees and require every changed
   path to be declared by some unit or by an explicit non-claim owner; report undeclared paths as
   `SEPARABILITY_UNOWNED` (exit 1) and a declared-but-unchanged land as an advisory. This is the
   build wave's control 1 (`ConnectSiblingSeparability.md:227`), absent from the landed bytes
   (0 occurrences of `diff`/`name-only`; `MANIFEST_KEYS` `:85`; `_load_units` `:469`). It would
   not by itself prove *who* owns a path, but it would have forced the r50 manifest to state the
   frontier absorption rather than silently add `corpus/SOURCES.md` to C.

## Risks

- Adding an ownership/completeness gate will exit 1 on every round whose wave evidence (`.ufo/…`)
  and telemetry are not declared; the owner must be an explicit non-claim class or the gate will
  be turned off in practice. Measured here: 93 undeclared changed paths, 89 of them wave evidence.
- A `FRONTIER`/`non_claim` pass renames a real dependency into a green prerequisite, which is
  exactly the r49 defect relabeled. If it is added, the label must be printed and counted on the
  round record; exit 0 alone is not evidence of separability.
- Hand-declared exports remain the weak point: r105's C3->C2 is only named because Q ids are
  attributed to C2; stale/biased attribution loses it. Mechanical derivation from the added rows
  (`QUALITY.md` table) was proposed in the build wave and is not in the landed tool.
- Path-level overlap can over-report: a file owned by one claim and only jointly stamped (kagi's
  `corpus/stamps.tsv`) reads as shared if both declare it. That is conservative for admission but
  not a hunk-level attribution.

## Verification

Reproduce in a private clone (≤30 s total, no network):

```
git clone -q --shared <kotodama-lane> /tmp/x && git -C /tmp/x checkout -q 1c779e4
cd /tmp/x
python3 -B tools/check-claim-separability.py --selftest | tail -1           # 56/56
python3 -B tools/check-claim-separability.py reports/round-50/separability/r49-fixture.json --lane . --root . ; echo RC=$?   # 6 findings, 1
python3 -B tools/check-claim-separability.py reports/round-50/separability/r50-manifest.json --lane . --root . ; echo RC=$? # 0 findings, 0
python3 -B tools/check-claim-separability.py reports/round-50/claims.json --lane . --root . ; echo RC=$?                     # exit 2
```

Cross-lane: build the two manifests above with the bases/trees named in this report
(`e8990516`→`f67c64ae`; `0a47dd1`→`144babcb`) against shared clones of the sibling lanes.
Temp dirs `/tmp/kr50-falsify-ca`, `/tmp/kr50-gd2d`, `/tmp/kr50-kagi` were removed after the run.
No tools installed or updated.

Report: `.ufo/waves/round-50/falsify/ConnectSiblingCa.md`
