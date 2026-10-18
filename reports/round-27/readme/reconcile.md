# R27-C47 — `corpus/README.md` reconciliation (round 27)

- **seat:** R27-C47 (C-readme). **lane:** `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
  **assignment (verbatim):** "C R27-C47..C48 (README + audit): corpus/README
  reconciled; entry audit (no filler, sources resolve)."
- **date:** 2026-10-18. **declared baseline:** `4f09c990d4c17f23b5e2cda0871f81db875635fc`
  (`reports/round-27/claims.json:5`); **HEAD at measurement:** `b95fca1e40f32f7346937ab6426f9ccca60e319f`.
  **measurement stamps:** 2026-10-18T19:19:25Z (pre-landing reading, revision
  1.6) and **19:20:45Z (final, after the register entry landed, revision 1.7)**.
  Both are carried below; the final reading is the binding one.
- **canon:** NON-CANON engineering evidence. This seat admits no entry, judges no
  entry's quality or sources, touches no gate, ledger, or canon.
- **writes:** `corpus/README.md`, this file, `reports/round-27/readme/sweep.py`,
  `reports/round-27/readme/verify.md`, and disposable scratch under `.scratch/`.
  No commit, no push.
- **counting command for this round:** `python3 reports/round-27/run-validation.py`
  — **absent at 19:19Z** (the round runner had not landed), and **run at 19:25Z
  in `--check` mode** (no receipt write) once it appeared: **claim C passes,
  `failures: []`**. The runner independently measures the same surfaces this
  receipt does — `corpus_readme.revision_head "1.7"`, partition headers
  `94/18/20/19/29/20`, `total_files 200`, `mismatches {}`, `names_the_entry
  true` — so its verdict and this receipt's own commands **agree**. The receipt
  still carries its own commands; the runner's verdict is quoted as
  corroboration, not substituted for them. The runner's D and O claims fail on
  their own seats' in-flight artifacts (gate/legality splits, un-re-pinned
  surfaces, battery not yet reporting), which are not C's legs.

## 0. Verdict at a glance

Final reading (19:20:45Z, revision 1.7, after the register entry landed):

| # | requirement | measured | status |
|---|---|---|---|
| C47-a | counts command-carried against actual contents | `20/19/18/29/20/94` = **200 files**, two independent methods (§1) | done |
| C47-b | index rows == files | **200 rows vs 200 files**; 0 missing, 0 ghosts, 0 duplicates, 0 header drift, totals line 200 (§2) | done |
| C47-c | every row is its entry's own `- topic:` text | **0 topic mismatches**, the new row included (§2) | done |
| C47-d | known-gaps current | revision 1.7 records the landing; revision 1.6's pre-landing reading kept as the dated record it was (§3) | done |
| C47-e | receipts | this file + `verify.md` (independent re-measure) + `sweep.py` (fresh committed instrument, 9/9 controls) | done |

Pre-landing reading (19:19:25Z, revision 1.6): 199 rows / 199 files, 0
mismatches, README sha `1a359d55…` — **identical to round 20's settled digest**,
i.e. no drift existed to repair at that pin. Both readings are measurements; the
final one is binding.

## 1. Counts, command-carried

Method 1 — the lane's own read-only inventory:

```sh
python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge
# totals.files = 200 (final); per-dir civilizations 94, culture-material 18,
# linguistics 20, myth-symbol 19, synthesis 29, verification 20
# at the pre-landing pin the same command read totals.files = 199,
# linguistics 19
```

Method 2 — an independent plain-filesystem count:

```sh
for d in linguistics myth-symbol culture-material synthesis verification civilizations; do
  find corpus/knowledge/$d -maxdepth 1 -name '*.md' -type f | wc -l; done
# 20 19 18 29 20 94
find corpus/knowledge -maxdepth 2 -name '*.md' -type f | wc -l   # 200
```

Both agree at both pins. The round-20 claim's declared `linguistics 20` was not
reproducible at the pre-landing pin (the tree measured 19, as revision 1.5
records); at the final pin the partition genuinely measures **20**, for a
different reason — the round-27 entry landed there. The two readings must not be
conflated.

## 2. The sweep — index rows vs the files they name

A fresh instrument was committed this round because round 20's sweep lived in
`.scratch/` and was never tracked. **Final reading** (19:20:45Z, after the
landing):

```sh
export TMPDIR=$PWD/.scratch
python3 reports/round-27/readme/sweep.py
# parts {"civilizations": 94, "culture-material": 18, "linguistics": 20,
#        "myth-symbol": 19, "synthesis": 29, "verification": 20}
# rows 200 files 200
# missing_from_index 0 []
# topic_mismatch 0 []
# orphan_rows 0 []
# header_drift {}
# totals_line 200 totals_ok True
# readme_sha256 d9d97d7f860c15bb00e9fca4e6b4df5469b62d6233b9168582481b353dd7c4e5
#                                                                     → exit 0
```

**Pre-landing reading** (19:19:25Z, revision 1.6), kept because it is what
establishes that the landing was the only change:

```sh
python3 reports/round-27/readme/sweep.py
# rows 199 files 199; 0 missing / 0 mismatches / 0 ghosts / 0 drift
# totals_line 199; readme_sha256 1a359d55387eef1aebd79316a7bf19d53a2ac6f0bcacb1cd109bdeff1294e7ce
#                                                                     → exit 0
```

The pre-landing digest `1a359d55…` is **the same digest round-20's `verify.md`
records at 13:07:53Z**, so at that pin the reconciliation was a re-measurement
that reproduced, not a repair — **no drift existed to fix.** The final reading
differs only by the one new row, its bumped header, and the bumped totals line;
the three edits are named in §3 and nothing else moved.

**Controls** — the sweep must be able to fail (fresh run, 9/9):

```sh
python3 reports/round-27/readme/sweep.py --selftest
# PASS live: rows == files / 0 missing / 0 topic mismatches / 0 ghosts / 0 drift
# PASS control: planted paraphrase flagged (1 mismatch)
# PASS control: truncated rewrite flagged (1 mismatch)
# PASS control: planted ghost row flagged
# PASS control: deleted row surfaces a missing file
# PASS control: wrong header count flagged
# PASS control: wrong totals line flagged
# PASS control: continuation lines space-joined
# PASS control: duplicate row reported
# selftest: 9/9 checks passed
```

The paraphrase and truncated-rewrite controls are the two defect classes round
20 measured (the ten round-19 rows were condensed rewrites); the deleted-row,
ghost-row, header-count and totals controls cover the other four legs.

## 3. Known-gaps currency — the landing and the three edits

**Revision 1.7** (final) records the round-27 C entry landing
(`linguistics/register-strata-attestation.md`) and the reconciliation to it. The
edit is exactly three changes, and nothing else in the README moved:

| edit | before → after |
|---|---|
| `## linguistics/` header | `(19)` → `(20)` |
| one new row | inserted in filename order (between `politeness-taboo-euphemism.md` and `semantic-fields-lexicon-building.md`), carrying the entry's own `- topic:` text byte-equal (1,193 chars) |
| totals line | `Total knowledge entries: 199.` → `200.` |

The row was inserted mechanically from the entry's own head block
(`.scratch/r27-c-insert.py`), not typed, so the byte-equality the sweep checks
is by construction rather than by care.

**Revision 1.6** (pre-landing) is kept below 1.7 unchanged, as the dated
reading it was: it recorded the re-measurement, the pin, the stamp, and the
explicit note that **the register-strata entry had not landed** (199 files at
every stamp 16:11Z–19:19:25Z) and that a landing would need "a new row, a bumped
section header, a bumped totals line, and its own revision block, never an edit
of this one". That is precisely what revision 1.7 does. The prediction and its
fulfilment are both in the file, which is what makes the pair readable as
evidence rather than as a rewrite.

## 4. Scope and limits

- This seat re-measured the index; it did **not** re-adjudicate any entry's
  scholarship, sources, or calibration. `QUALITY.md` conformance is the C48
  audit's leg (`reports/round-27/audit/x-c48-entry-audit.md`).
- The sweep is read-only over `corpus/`; it has no code path that writes inside
  the repo.
- The instrument is this seat's own. `verify.md` re-runs it from a fresh process
  with independent re-derivations and before/after controls; that is
  **same-seat** verification, and the limit is restated there rather than hidden.
