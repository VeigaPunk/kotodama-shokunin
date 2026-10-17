# R10-O02 — findings fixer: tracker rows 0 and 8

- **Shard:** R10-O02 (claim O, operability). **Round:** 10, loop 1 of 3, build round 3 of 4.
- **Date:** 2026-10-17 (commands below ran 21:2x–21:35Z; local = UTC-3).
- **Lane repo:** `/home/vgpnk/Projects/shokunin/kotodama-shokunin`; HEAD `e3a1ec9435787328ac9f828f96cb6390e4916b8f`.
- **Write scope:** this file and my two tracker rows (`reports/round-10/findings-tracker.json` rows idx 0 and idx 8). Scratch lives in `.scratch/o02/` (`TMPDIR=$PWD/.scratch`). No commit, no push, no other repository file written.
- **Baseline drift (not mine):** the worktree carried `M reports/round-9/validation.json` plus other workers' scratch throughout; the artifacts I measured (`tools/d2-typed-labels.py`, `examples/culture-d2/*`, `tools/gates/*`) were clean against HEAD.

## 0. Index resolution (tracker landed mid-shard)

The tracker was absent at shard start, so I began under the assignment's fallback ("read the four source files, take the 1st and 9th findings"): 1st = R8-D16 **S2**, 9th = R8-D17 **F-D17-2**. `reports/round-10/findings-tracker.json` landed at 18:28 (24 rows, severity-ranked) and is authoritative, so the rows I dispositioned are:

| tracker idx | source | finding | disposition recorded |
|---|---|---|---|
| 0 | `reports/round-8/depth/findings.md` | **S2** — no frozen manifest for the D2 packet | `wont-fix (superseded by round-8 acceptance decision; fix recipe demonstrated)` |
| 8 | `reports/round-8/depth/findings-17.md` | **F-D17-1** — borrow ledger: no `donor_form`/substitutions/derivation | `fixed-with-control` |

The fallback target **F-D17-2** is tracker row 14 (another fixer's row). I had already built its control before the tracker landed; the result is kept in §3 as bonus evidence, and row 14 is left for its owner.

## 1. Row 0 — R8-D16 S2 (blocking): no frozen manifest exists for the D2 packet

**As filed** (revision `e9209f28`, review close 17:31): `discover_manifest` found no round-8 manifest (`find . -name 'MANIFEST*.tsv'` → round-3 only), and the harness reported `claim D: FAIL — no frozen manifest found for the D2 packet`.

**Re-measured today:**

```sh
find . -name 'MANIFEST*.tsv' -not -path './.git/*' -not -path '*/.scratch/*'
# tools/gates/frozen/round-3/MANIFEST.tsv
# tools/gates/frozen/round-3/attempt-1/MANIFEST.tsv      (+ 6 copies inside reports/supplement-opencode-1/scratch/**)
python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv --json
# exit 2: {"rows": 7, "reproduced": 0, "mismatch": 0, "could_not_evaluate": 7} — every row gate_digest_mismatch
```

The gap is live: **no D2 frozen manifest exists**, and the only D2-relevant manifest is red. Round 8 closed claim D anyway, through the runner's declared fallback: `reports/round-8/validation.json` `claims.D.passed=true`, `replay_frozen.accepted="isolated-pinned-revisions"`, `isolated={exit 0, gates_restored_from_head 7, summary {rows 7, reproduced 7, mismatch 0, could_not_evaluate 0}}`, `round8_manifest_candidates=[]`.

**That acceptance no longer reproduces** (new evidence, demonstrated):

```sh
git archive HEAD | tar -x -C .scratch/o02/iso        # pristine HEAD e3a1ec9 tree
cd .scratch/o02/iso && python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv \
    --repo-root "$PWD" --json
# exit 2: {"rows": 7, "reproduced": 0, "mismatch": 0, "could_not_evaluate": 7}
# every row reason=gate_digest_mismatch
```

Mechanism: the round-3 manifest pins the **pre-repair** gate bytes, HEAD carries the repaired ones, and `replay_isolated()` copies HEAD blobs (`reports/round-8/run-validation.py:1205-1252`). The receipt's exit 0 was therefore produced while HEAD was still `cf338a7` (pre-admit) — the admit commit `e1694ba` itself invalidated the acceptance.

| gate | round-3 pin (= `cf338a7` bytes) | HEAD / live |
|---|---|---|
| `costume-era-consistency-gate.py` | `29a9361c…b3e5b3a43f03` | `e6bffd70…ceec478f` |
| `naming-collision-gate.py` | `8c5afb0a…f19aa526` | `d9e4e8f4…1a630a1d` |
| `phonology-sanity-gate.py` | `fb05c644…f85372655` | `d5fe087f…dec34230` |

**Demonstrated control (fix recipe, deliberately not landed):** a D2 manifest over the current bytes replays green with the real tool.

```sh
python3 .scratch/o02/build-d2-manifest.py .scratch/o02/iso
# exit 0; manifest tools/gates/frozen/round-10-d2/MANIFEST.tsv sha256 8eec188f89eb788f8d04be1255a8655ebd2d7a162cd50e170189952171cede83
# replay: {"rows": 5, "reproduced": 5, "mismatch": 0, "could_not_evaluate": 0, "exit": 0}
# rows (gate / recorded exit / findings): phonology 1/3, lexicon-coverage 0/0, myth 0/0, costume-era 0/0, naming 1/17
```

Two cross-checks fall out: the phonology row's output bytes (`1ce5f0cd…`) are byte-identical to the round-3 manifest's recorded phonology output, and the naming row (`ebc8850d08ec1b7e32616cbca9092ba66f3b6f148a61515a033e6bed6fa66f4b`, exit 1, 17 findings) matches the round-8 D17 §0 live baseline — the repaired gates are behaviour-neutral on this packet, so a re-pin would hide no verdict change. The scratch manifest is a recipe, not a repo artifact; landing it is an integration act (orchestrator / packet owner).

**Disposition (as recorded in the tracker row):** `wont-fix (superseded by round-8 acceptance decision; fix recipe demonstrated)` — reason: round 8 retired the per-round D2 manifest requirement through the runner's declared fallback, so no owner is chartered to land one, and landing it is outside a fixer's write scope; the residual is filed below and the recipe is proven green.

**Residual R10-O02-NEW-1 (new finding, reported not absorbed):** the round-8 claim-D green is **snapshot-bound** — at HEAD the accepted substitute is red (7/7 `gate_digest_mismatch`), so "the D2 packet replays frozen" is currently satisfied by no path in the delivered tree. Suggested owner: orchestrator; remedy is the §1 recipe plus a re-verification record (the R9-D09 S1 pattern).

## 2. Row 8 — R8-D17 F-D17-1 (medium): borrow ledger absent on the `kas` label

**As filed** (revision `623b5b1f`, 17:24): the L-26 `kas` label named the layer and donor but carried no `donor_form`, no substitutions, and ran no derivation check; artifact counts `gas` 0 / `donor_form` 0 / `substitution` 0.

**Control (demonstrated, exit 0):**

```sh
python3 .scratch/o02/control-f-d17-1.py     # exit 0, verdict fixed-at-current-revision
# label L-26: text 'kas', kind 'borrowed-strata'
#   borrow.donor_form 'gas'; borrow.substitutions {bh:p, dh:t, g:k, sh:s}; borrow.layer_ref 'Salt-road trade layer'
#   borrow.donor roles [carrier, immediate, ultimate]   (design-spec §1.4 B2 separation present)
# independent derivation apply({bh:p,dh:t,g:k,sh:s}, 'gas') == 'kas' == label text
# negative control apply({}, 'gas') == 'gas' != 'kas'   (the control discriminates)
python3 tools/d2-typed-labels.py --selftest  # exit 0, 39/39
#   incl. 'spec B3: substitutions that do not derive the form are D2L-BORROW'
#   and  'spec B3 positive: gas with g->k derives kas and is clean'
```

Artifact `examples/culture-d2/typed-labels.d2.yml` sha256 `e70ba1477dbeb830061db6fd12516b7d902587bddae173f55a3650015d380b2f`; tool `tools/d2-typed-labels.py` sha256 `0da0015f700345c938184cb45ca07178c33e98f798c3c09729007487fb89c802` (borrow path `:572-573` attachment, `:649-719` `apply_substitutions` + `D2L-BORROW`).

**Disposition:** `fixed-with-control`. All three sub-claims are false at the delivered revision; no residual. (The finding's own revision pin explains the gap: it was measured at `623b5b1f`, five rewrites before the committed `0da0015f`.)

## 3. Adjacent re-verifications (bonus; rows owned by others)

- **F-D17-2** (tracker row 14, still `pending`): the vocabulary divergence is fixed at the current revision — `typed_labels` statuses are exactly `supplied` (48) / `to-verify` (10) (`STATUSES = ("supplied", "to-verify", "absent")`, `tools/d2-typed-labels.py:416`), and every hold id is `D2L-*` (`D2L-FORM-UNRESOLVED` ×20, `D2L-NATIVE` ×4, `D2L-RANK` ×4, `D2L-SCOPE` ×9; zero `TL-01/02`). Control `python3 .scratch/o02/control-f-d17-2.py` → exit 0 (`fixed-at-current-revision`), with a mutant carrying `status: declared` + `TL-01` failing the same checks. **Residual for that row's owner:** `SKILL.md:86,88,90` and `SCORECARD.md:128` still cite the retired `TL-01`/`TL-02` ids.
- **R10-O02-NEW-2 (new, live, demonstrable):** `python3 tools/d2-typed-labels.py --check` → exit 1 — the committed artifact pins `packet_sha256 8da90b07…` while the packet (re-pinned inside the same admit commit `e1694ba`) is `e0f21509…`; the deterministic rebuild differs in exactly that one line (`.scratch/o02/diff.txt`, 4 lines). `python3 tools/assemble-d2.py --check` → exit 0, so only the typed-labels artifact is stale. Owner: the artifact's generator owner; remedy is a re-emit plus the `--check` receipt.
- Row 1 (S3, R10-O03) independently demonstrated the same D2-manifest recipe (`replay_remedy` in its tracker row: 5/5 exit 0) — converging evidence for the §1 recipe.

## 4. Tracker update record

- Targeted edits only (no whole-file rewrite): row 0's `"disposition": "pending"` replaced by the disposition + `control` (6 fields) + `reason`; row 8's likewise (+ `control`, `evidence`, `reason`). `json.load` re-validated afterwards: 24 rows, all rows carry `idx/source_file/finding/severity/disposition`.
- File sha256: `3bfd40181ca98c830ef1042b23c3e446328b915ced9773dbc12b431d6b22d353` before my edits (18:33), `ad803f3a0f3bf9b08d4c89cc1b6912be3b09cbd1d1dc9d0faa5c68240ae49889` immediately after (18:34); `d0136d1deb6a66d24cf708583f4620a23871c858e5da14f219ef434aaa6e9a56` at 21:35 — **other fixers are writing the file concurrently**; my two rows re-verified intact at 21:35 (row 0: 6 control keys, reason 706 chars; row 8: 5 control keys, reason 435 chars).
- Runner self-check (`reports/round-10/run-validation.py`, `measure_o()` imported read-only, 21:3xZ): `unrecognized_labels: []`, `fixed_without_control: []`, `documented_without_reason: []`; remaining failures were other workers' pending rows (2-7, 10-23), the 4 verifier files and the scribe — none from rows 0/8.
- Count command (`reports/round-10/findings-tracker.json` `count_command`): at 21:35 → `24 18` (24 rows, 18 pending; rows 0, 1, 8 dispositioned).

## 5. Reproduction

```sh
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
export TMPDIR=$PWD/.scratch
# row 0 evidence
find . -name 'MANIFEST*.tsv' -not -path './.git/*' -not -path '*/.scratch/*'
python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv --json            # exit 2, 7 CNE
mkdir -p .scratch/o02/iso && git archive HEAD | tar -x -C .scratch/o02/iso
(cd .scratch/o02/iso && python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv --repo-root "$PWD" --json)  # exit 2, 7 CNE
python3 .scratch/o02/build-d2-manifest.py .scratch/o02/iso                                # exit 0, 5/5 reproduced
# row 8 evidence
python3 .scratch/o02/control-f-d17-1.py                                                   # exit 0
python3 tools/d2-typed-labels.py --selftest                                               # exit 0, 39/39
# adjacent
python3 .scratch/o02/control-f-d17-2.py                                                   # exit 0
python3 tools/d2-typed-labels.py --check; echo $?                                         # exit 1 (NEW-2)
```

Evidence files (sha256): `control-f-d17-1.py 7a96c28e…e19d4`, `control-f-d17-2.py a59f41cb…8be545`, `build-d2-manifest.py bac540da…0841d3`, `d2-manifest-build.json 22a12eef…bf3207`, `iso-replay.json 41b054b1…dae9be`, `diff.txt 118c13c5…900ed8`. The three control scripts are inlined in this report's §1–§3 (commands) and are reconstructible from the quoted logic if `.scratch/` is swept.

## 6. Limits and to-verify

- Row 0 is dispositioned as superseded-with-reason, **not** fixed: no D2 manifest was landed (write scope), and whether the orchestrator wants one is an integration decision — the recipe and its green replay are handed over.
- The `wont-fix` label is about ownership/scope, not about the finding being wrong: the gap is confirmed live and the round-8 acceptance is shown non-reproducible.
- `to-verify`: whether any round-10 worker lands the D2 manifest and the `typed-labels` re-emit; both residuals (NEW-1, NEW-2) are stated as new findings here and are not tracker rows.
- Nothing here adjudicates canon, real-world rights, or game mechanics (out of province).

FILES: reports/round-10/fix-02.md, reports/round-10/findings-tracker.json (rows idx 0 and idx 8), .scratch/o02/control-f-d17-1.py, .scratch/o02/control-f-d17-2.py, .scratch/o02/build-d2-manifest.py, .scratch/o02/d2-manifest-build.json, .scratch/o02/iso-replay.json, .scratch/o02/diff.txt, .scratch/o02/rebuilt.d2.yml
SUMMARY: Dispositioned tracker rows 0 (R8-D16 S2 — wont-fix/superseded with a demonstrated green D2-manifest fix recipe; live gap and a non-reproducible round-8 acceptance shown, residual filed) and 8 (R8-D17 F-D17-1 — fixed-with-control: artifact now carries donor_form/substitutions and the derivation gas→kas reproduces, selftest 39/39); both tracker rows updated and re-verified under concurrent writers.
