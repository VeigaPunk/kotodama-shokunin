# R10-O10 — findings verifier: fixers R10-O02 and R10-O03

- shard: R10-O10 (claim O verifier; round 10, loop 1 of 3, build round 3 of 4) — 2026-10-17, local UTC-03, verification window ~21:27Z–21:50Z.
- assignment (verbatim): "FINDINGS R10-O10 (verifier): re-run/validate fixer O02+O03's controls and reasons; reports/round-10/findings-verify-1.md."
- scope: the four tracker rows dispositioned by the two fixers —
  - **R10-O02** → idx 0 (R8-D16 S2, `wont-fix (superseded…)`, fix recipe) and idx 8 (R8-D17 F-D17-1, `fixed-with-control`);
  - **R10-O03** → idx 1 (R8-D16 S3, `fixed-with-control`) and idx 9 (R8-D16 S11, `fixed-with-control`).
- method: every control the fixers cite was re-run here, from the lane root, at the fixers' recorded revisions; every documented reason was validated against the source files it invokes; where the fixer's control lived only in `.scratch/`, I re-ran the fixer's own script and, for the manifest recipe, re-built it in a fresh `git archive HEAD` tree of my own. Read-only over the repository apart from this file; scratch under `.scratch/r10o10*` (`TMPDIR=$PWD/.scratch`); `replay-frozen.py` mirror runs used `TMPDIR=/var/tmp/r10o10` (it refuses an in-repo temporary root: `mirror_unsafe`).
- baseline revision: `e3a1ec9435787328ac9f828f96cb6390e4916b8f` (HEAD) + dirty wave worktree (concurrent workers); tracker read at its live state.
- canon: NON-CANON engineering evidence. Nothing here adjudicates canon, real-world rights or game mechanics.

## Verdict summary

| tracker idx | finding | fixer | recorded disposition | my verdict |
|---|---|---|---|---|
| 0 | R8-D16 S2 — no frozen manifest for the D2 packet | R10-O02 | `wont-fix (superseded by round-8 acceptance decision; fix recipe demonstrated)` | **reason valid, control confirmed** (one wording caveat, §1) |
| 8 | R8-D17 F-D17-1 — borrow ledger absent on `kas` | R10-O02 | `fixed-with-control` | **control confirmed** (§2) |
| 1 | R8-D16 S3 — D2 regeneration + round-3 replay red | R10-O03 | `fixed-with-control` | **control confirmed** (§3) |
| 9 | R8-D16 S11 — harness cannot enforce demonstrated-run SCORECARD row | R10-O03 | `fixed-with-control` | **control confirmed, residual accurate** (§4) |

All four rows' controls reproduce exactly, including the cited stdout sha256 values where the fixers quoted them. No control was found to be toothless; no reason was found false.

## 1. idx 0 — R8-D16 S2 (fixer R10-O02)

**Recorded:** disposition `wont-fix (superseded by round-8 acceptance decision; fix recipe demonstrated)`, with a 6-field `control` and a reason; residual filed as `R10-O02-NEW-1` in `reports/round-10/fix-02.md` §1.

**Controls re-run (all reproduced):**

```sh
python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv --json
# exit 2; {"rows":7,"reproduced":0,"mismatch":0,"could_not_evaluate":7,"exit":2}; every row gate_digest_mismatch
# stdout sha256 cbde6c5e17c7f77e6bcf2f57d1359af1a6ef41c6c201c0b11687ad18daeab528   (== fixer's quote)

mkdir -p .scratch/r10o10-iso && git archive HEAD | tar -x -C .scratch/r10o10-iso
TMPDIR=/var/tmp/r10o10 python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv \
    --repo-root .scratch/r10o10-iso --json
# exit 2; 7/7 could-not-evaluate, reason gate_digest_mismatch — the round-8 "isolated-pinned-revisions"
# acceptance does not reproduce at HEAD (my own pristine-HEAD tree, independent of the fixer's .scratch/o02/iso)

# pin matrix, all six gates (awk over tools/gates/frozen/round-3/MANIFEST.tsv):
#   pin == `git show cf338a7:<gate>` bytes : YES x6;  `git show HEAD:<gate>` == live : YES x6
#   e.g. costume 29a9361c… == cf338a7, live/HEAD e6bffd70…; naming 8c5afb0a… / d9e4e8f4…
#   phonology fb05c644… / d5fe087f…; lexicon 63ee4ec6… / 2c4dd397…; myth 26d246e9… / 5368b135…
#   provenance 4aaea6e9… / 8a96aaf4…

# fix recipe re-run in MY iso tree (writes only inside the iso copy):
TMPDIR=/var/tmp/r10o10 python3 .scratch/o02/build-d2-manifest.py .scratch/r10o10-iso
# exit 0; manifest tools/gates/frozen/round-10-d2/MANIFEST.tsv sha256
# 8eec188f89eb788f8d04be1255a8655ebd2d7a162cd50e170189952171cede83   (exact match to the fixer's quote)
# replay {"rows":5,"reproduced":5,"mismatch":0,"could_not_evaluate":0,"exit":0}
# rows phonology 1/3, lexicon 0/0, myth 0/0, costume 0/0, naming 1/17

# fixer's two cross-checks, re-derived from my run's manifest:
#   phonology output sha 1ce5f0cdabad… == the round-3 manifest's recorded phonology output sha  (behaviour-neutral)
#   naming output sha ebc8850d08ec1b7e… == reports/round-8/depth/findings-17.md §0 live baseline (exit 1, 17 findings)

# round-8 receipt block (read directly): reports/round-8/validation.json claims.D.measurement.replay_frozen
#   accepted "isolated-pinned-revisions", isolated {7/7 reproduced, exit 0}, round8_manifest_candidates []
```

**Reason validated.** Round 8 did close claim D through the runner's declared fallback rather than a landed manifest (`reports/round-8/claims.json` claim D required the replay leg; `reports/round-8/validation.json` records the accepted substitute); the round-8 scribe charter (targets `R8-D18..D20`, "frozen-manifest records") produced a *record*, not a manifest — `reports/round-8/depth/scribe.md:76-91` concludes the capability cannot be recorded in the round-3-style `MANIFEST.tsv` schema and reports the question upward ("reported, not absorbed") — and no D2 manifest exists anywhere in the repo today. Landing one is outside a fixer's named write scope (the fixer's assignment writes `fix-02.md` + its rows). The disposition therefore stands.

**Wording caveat (not a defect):** the reason's phrase "no owner was chartered to land a per-round D2 manifest" is imprecise — `R8-D18..D20` *did* charter "frozen-manifest records". What is true, and what the disposition needs, is that the charter did not land a manifest and the question was escalated; the fixer's own fragment states the residual precisely. No action needed for acceptance; the scribe may want the sentence tightened if this row is quoted.

**Residual R10-O02-NEW-1 independently confirmed:** the round-8 D green is snapshot-bound — in a pristine HEAD tree the accepted substitute is 7/7 `gate_digest_mismatch` (my run above). Cross-reference: the F-side sibling repair to `reports/round-8/run-validation.py` (documented in `reports/round-10/drift/shard-13.md:153-171`, made by another R10 worker at 21:32:28Z) restores the *runner's* isolated replay by resolving pins through git history — that mitigates NEW-1 on the runner path but does not create the D2 packet manifest. NEW-1's suggested remedy (recipe + a re-verification record) remains open for the orchestrator.

## 2. idx 8 — R8-D17 F-D17-1 (fixer R10-O02)

**Recorded:** `fixed-with-control`; no residual; reason: superseded by the post-review rewrite (finding measured at `623b5b1f`; tool now `0da0015f`).

**Control re-run:**

```sh
python3 .scratch/o02/control-f-d17-1.py        # exit 0, verdict fixed-at-current-revision
```

Observed (my run): label `L-26` text `kas`, kind `borrowed-strata`; `borrow.donor_form` `gas`; `borrow.substitutions` `{bh:p, dh:t, g:k, sh:s}`; `borrow.layer_ref` `"Salt-road trade layer"`; `borrow.donor` keys `[carrier, immediate, ultimate]` (B2 separation present); independent derivation `apply({bh:p,dh:t,g:k,sh:s}, 'gas') == 'kas' == text` → true; negative control `apply({}, 'gas') == 'gas' != 'kas'` → discriminates (true).

```sh
python3 tools/d2-typed-labels.py --selftest     # exit 0, 39/39, incl.
#   "spec B3: substitutions that do not derive the form are D2L-BORROW"
#   "spec B3 positive: gas with g->k derives kas and is clean"
```

Artifact inspected directly (not via the control): `examples/culture-d2/typed-labels.d2.yml` sha256 `e70ba1477dbeb830061db6fd12516b7d902587bddae173f55a3650015d380b2f` carries the full L-26 borrow block; tool sha256 `0da0015f700345c938184cb45ca07178c33e98f798c3c09729007487fb89c802` implements `apply_substitutions` + `D2L-BORROW` (`:649-719`) and the attachment (`:572-573`). All three sub-claims of the finding (no `donor_form`, no substitutions, no derivation check) are false at the delivered revision. **Control confirmed; no residual.**

## 3. idx 1 — R8-D16 S3 (fixer R10-O03)

**Recorded:** `fixed-with-control`; control keys `regeneration` / `replay_remedy` / `round3_replay`; residual: the demonstrated D2 manifest is scratch-only.

**Controls re-run (all exact):**

```sh
python3 tools/assemble-d2.py --check            # exit 0, "packet.d2.yml: byte-identical deterministic assembly"
# stdout sha256 2fa0c8c197459f549de2f0822b8895477e27dcce38def75e18346ba6d672e386   (== fixer's quote)
sed -n '3322p' examples/culture-d2/packet.d2.yml # reader_sha256 "e6bffd70…ceec478f"
sha256sum tools/gates/costume-era-consistency-gate.py # e6bffd70…ceec478f  (exact equality)

TMPDIR=/var/tmp/r10o10 python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv --json
# exit 2; 7/7 could-not-evaluate reason=gate_digest_mismatch
# stdout sha256 cbde6c5e17c7f77e6bcf2f57d1359af1a6ef41c6c201c0b11687ad18daeab528   (== fixer's quote)

sha256sum .scratch/r10o03/frozen-d2/MANIFEST.tsv  # 9adb38aea4fde88f9903ede521da7be56fcc27b08aee709e462c177e4e402df4
TMPDIR=/var/tmp/r10o10 python3 tools/replay-frozen.py .scratch/r10o03/frozen-d2/MANIFEST.tsv --json   # run 1
TMPDIR=/var/tmp/r10o10 python3 tools/replay-frozen.py .scratch/r10o03/frozen-d2/MANIFEST.tsv --json   # run 2
# both exit 0; {"rows":5,"reproduced":5,"mismatch":0,"could_not_evaluate":0,"exit":0}
# stdout sha256 ce78801e13353e72c824546066837750940e63af7f5a7c5cbd7d5f2c3dfc4a93, byte-identical across runs (cmp)
# manifest pins == live gate bytes for all five rows (phonology d5fe087f…, lexicon 2c4dd397…, myth 5368b135…,
#   costume e6bffd70…, naming d9e4e8f4…)
```

**"By design" reading validated:** `corpus/knowledge/verification/gate-frozen-run-standard.md:100` ("barred from any conformance claim, and never silently re-pinned", KTD-FR-S-0002) is at the quoted location; the round-3 pins resolve to `cf338a7` gate bytes (§1 matrix) while HEAD/live carry the round-8-repaired gates — the mismatch is the standard working, not a defect. Round-8's own filed receipt recorded the same live-red/isolated-green pair (§1). The residual (scratch-only manifest; landing is an orchestrator act) is accurate: `find` shows no D2 manifest in the repo. **Control confirmed.**

## 4. idx 9 — R8-D16 S11 (fixer R10-O03)

**Recorded:** `fixed-with-control`; control keys `fail_before` / `fail_after` / `pass_after` / `receipt`; residual: filed harness bytes untouched, anchored matcher is a drop-in for the round-10 runner.

**Controls re-run:**

```sh
python3 .scratch/r10o03/s11/probe2.py           # exit 0
# ANCHORED MATCHER on mention-only SCORECARD : rows = 0 -> FAIL (no demonstrated-run row)
# ANCHORED MATCHER on real SCORECARD        : [{"line":128,"name":"d2-typed-labels",
#   "command_evidence":"`python3 tools/d2-typed-labels.py --selftest`; `examples/culture-d2/typed-labels.d2.yml`"}]
# receipt .scratch/r10o03/s11/receipt2.json: filed_check.mention_only {scorecard_row: true, failures: []}  (fail-before)
```

The filed whole-file regex still decides the row: `reports/round-8/run-validation.py:1357` (`re.search(r"d2[-_ ]typed[-_ ]labels", scorecard, re.I)`) — line 1357, not 1323, because of the sibling repair noted in §1; the tracker's parenthetical "(1323 before a…)" is correct. The filed harness sha256 is `d78da29fdacc75d425e21c21fa2d299deff487f17724e8fa7bd73f5b4fc14735` — identical to the fixer's recorded before/after value, so the fixer did not edit it.

**Evidence-hygiene note (explained, not a defect):** the filed runner changed *during* O03's window — `receipt.json` (21:31) recorded the pre-repair sha `7eaa36789b…` (== HEAD bytes), `receipt2.json` (21:32) the post-repair `d78da29f…`. The change is the F-side sibling repair documented at `reports/round-10/drift/shard-13.md:153-158` ("Fix landed during this shard's run (by a sibling R10 worker, not by R10-F13)"), timestamped 18:32:28 local. O03's "before and after" both read `d78da29f` only if "before" means after 21:32:28; the substance of its claim (it edited nothing) holds, and its S11 probe exercises `measure_d_docs()`, which the repair did not touch. The scribe should carry the worktree-modified status of `reports/round-8/run-validation.py` into the integration record.

**Residual validated:** the round-10 runner does not adopt the anchored matcher (`grep -c anchored reports/round-10/run-validation.py` → 0) and does not check the `d2-typed-labels` capability row at all (`grep -c 'd2-typed-labels'` → 0), so the enforcement gap is not re-created in the round-10 harness; adoption remains a named, open residual for X03 or any successor harness. **Control confirmed; residual accurate.**

## 5. Cross-checks and notes for the scribe / orchestrator

- **No regression observed:** every previously-green surface I touched still passes (d2-typed-labels `--selftest` 39/39; `assemble-d2.py --check` exit 0; D3 frozen replay exit 0 — the last one read in passing while validating R9 rows, not my scope).
- **R10-O02-NEW-2 (filed in `fix-02.md` §3) independently confirmed:** `python3 tools/d2-typed-labels.py --check` → exit 1; the committed artifact pins `packet_sha256 8da90b07…` while the packet hashes `e0f21509…`; the diff is exactly that one line. Four independent emits (mine plus three other workers' `.scratch` copies) are byte-identical at `a3aa452c…`, so the re-emit remedy is deterministic. This is the artifact's generator owner's / orchestrator's call.
- **NEW-1/NEW-2 are not tracker rows** (the tracker covers the four source files' findings; these are round-10 discoveries). The scribe may want them recorded in the integration/lessons trail.
- **Scope limits:** I verified the four rows' controls and reasons only; I did not re-adjudicate the round-8 gate repairs themselves, the D2 packet's re-pin, or any other fixer's rows (idx 2/3/6/11/14 and beyond are other verifiers' scope). The tracker was written concurrently by several workers during this verification; the rows I verified were read at their post-fix state and their content matches the fixers' fragments.
- Out of province and untouched: canon decisions, real-world rights rulings, game mechanics, general research method.

## 6. Reproduction (all commands 2026-10-17, lane root unless noted)

```sh
export TMPDIR=$PWD/.scratch
python3 .scratch/o02/control-f-d17-1.py && python3 .scratch/o02/control-f-d17-2.py
python3 .scratch/r10o03/s11/probe2.py
python3 tools/d2-typed-labels.py --selftest            # 39/39
python3 tools/assemble-d2.py --check; echo $?          # 0
TMPDIR=/var/tmp/r10o10 python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv --json     # exit 2, 7 CNE
TMPDIR=/var/tmp/r10o10 python3 tools/replay-frozen.py .scratch/r10o03/frozen-d2/MANIFEST.tsv --json      # exit 0, 5/5
git archive HEAD | tar -x -C .scratch/r10o10-iso
TMPDIR=/var/tmp/r10o10 python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv --repo-root .scratch/r10o10-iso --json   # exit 2, 7 CNE
TMPDIR=/var/tmp/r10o10 python3 .scratch/o02/build-d2-manifest.py .scratch/r10o10-iso                     # exit 0, manifest 8eec188f…
python3 tools/d2-typed-labels.py --check; echo $?      # 1 (NEW-2, still live)
# my scratch receipts: .scratch/r10o10-baseline.txt, r10o10-v-{check,isohead,recipe}.json, r10o10-v-r3.json, r10o10-v-fresh{1,2}.json
```

FILES: reports/round-10/findings-verify-1.md | SUMMARY: Re-ran every control of fixers R10-O02 (tracker idx 0 S2 wont-fix-superseded with a fix recipe, idx 8 F-D17-1 fixed) and R10-O03 (idx 1 S3, idx 9 S11, both fixed) — all controls reproduce exactly (stdout sha256 matches where quoted; D2 manifest recipe re-built in my own pristine-HEAD tree at the exact 8eec188f hash and 5/5 replay; pristine-HEAD round-3 replay 7/7 gate_digest_mismatch; F-D17-1 derivation gas→kas with a discriminating negative control; S11 fail-before/anchored pass-after probe) — reasons validated with one wording caveat on idx 0 and one explained hash-shift (the F-side sibling repair to reports/round-8/run-validation.py, documented in drift/shard-13.md, shifted O03's receipt-window hash and the regex line 1323→1357); residuals R10-O02-NEW-1/NEW-2 independently confirmed; verdicts: all four rows control-confirmed, no toothless control, no false reason.
