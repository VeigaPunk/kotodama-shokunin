# R28-C56 — reviewer of `C46.md` (the README reconciliation)

- **seat:** R28-C56 (C-ceiling, reviewer 6 of 6). **lane:**
  `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
- **date:** 2026-10-18. **lane HEAD** `69cecbc`.
- **canon:** NON-CANON engineering review. Author-side evidence; admits nothing,
  certifies no round, is not independent promotion verification.
- **writes:** this file only. No corpus byte touched beyond reading. Scratch
  `.scratch/`, `TMPDIR=$PWD/.scratch`.
- **reviews:** `reports/round-28/ceiling/C46.md` against `corpus/README.md`
  (sha256 `053966a2147e5e71675b290d12bd4e523b73b31c764513ccb26a672bed37d57c`).

## 0. Verdict

**PASS. No defect. Every leg of the reconciliation is clean, the row text is
byte-equal to the entry's `- topic:` line, and the fragment's honesty about the
author-side limit is correct.**

| check | verdict |
|---|---|
| rows == files | pass — 201 / 201 |
| the new row's text is byte-equal to the entry's `- topic:` | pass |
| section header, totals line, footer all moved together | pass |
| the amendment added no index row (and the README says so) | pass |
| the new revision block is append-only | pass |
| the author-side limit is stated | pass |

## 1. The sweep, re-run from a fresh process

```sh
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
python3 -B reports/round-28/readme/sweep.py
# parts {"civilizations": 94, "culture-material": 18, "linguistics": 21,
#        "myth-symbol": 19, "synthesis": 29, "verification": 20}
# rows 201 files 201
# missing_from_index 0 []   topic_mismatch 0 []
# orphan_rows 0 []          header_drift {}
# totals_line 201 totals_ok True
# footer_findings [] footer_ok True
# readme_sha256 053966a2147e5e71675b290d12bd4e523b73b31c764513ccb26a672bed37d57c
```

Matches `C46.md` §1 exactly, including the digest. `--selftest` → **12/12**.

## 2. The byte-equal row, re-derived

`C46.md` §1 says the new row's text is byte-equal to the entry's own `- topic:`
head text. This seat re-derived it by string comparison rather than trusting the
sweep's `topic_mismatch 0`:

```sh
python3 -B - <<'PY'
import re
ent = open('corpus/knowledge/linguistics/register-lexicon-ceilings.md').read()
rd  = open('corpus/README.md').read()
topic = re.search(r'(?m)^- topic:(.*)$', ent).group(1).strip()
row = [l for l in rd.splitlines() if l.startswith('- `register-lexicon-ceilings.md`')][0]
rowtext = row.split('— ', 1)[1].strip()
print('byte-equal:', rowtext == topic, '| len', len(topic), len(rowtext))
PY
# byte-equal: True | len 921 921
```

921 characters on both sides, identical. This is the convention rounds 10/19/20
settled on after revision 1.4 was found to carry condensed paraphrases, and it is
the check that matters most for a new row.

## 3. The four coupled surfaces, checked together

The reconciliation moves four surfaces, and a landing that moves three of them is
the exact defect revision 1.8 was created to fix. Verified all four moved:

```sh
grep -n '^## linguistics/ (21)' corpus/README.md            # present
grep -n '^Total knowledge entries: 201' corpus/README.md    # present
grep -n 'directory totals 21/19/18/29/20/94' corpus/README.md  # footer
grep -n '^revision: 1.9' corpus/README.md                   # new head block
```

All four present, and the sweep's `header_drift {}` / `totals_ok True` /
`footer_ok True` confirm none is stale. The superseded readings (199/19 and
200/20) are preserved below the footer line as dated records, per the file's
convention.

## 4. The amendment adds no row — checked, not assumed

`C46.md` §3 states that the §13 amendment adds no index row and that revision
1.9's block says so. Verified both:

```sh
grep -c 'register-lexicon-ceilings.md' corpus/README.md   # 1 row + mentions in the revision block
grep -n 'amendment section' corpus/README.md
# revision 1.9's block: "... the round-28 amendment section in
# `linguistics/register-strata-attestation.md` (§13) is a new section in an
# existing entry and adds no index row ..."
```

The count of 21 `linguistics/` rows matches the 21 files, so no phantom row was
created for the amended entry — the correct outcome, since `register-strata-attestation.md`
already had its row.

## 5. The author-side limit, checked

`C46.md` §5 states that this reconciliation was landed by the same worker that
authored the entry, so the README→entry coupling is **author-side** evidence, and
names the runner's claim-C README leg as the independent check. That is the right
disclosure and it is accurate: the round-28 assignment gives C41..C46 to one seat,
so the pairing is author-side by construction. The runner's leg re-reads the
partition headers and the entry's presence from the tree:

```sh
python3 -B reports/round-28/run-validation.py --check
# claims.C.measurement.corpus_readme: revision_head "1.9", names_the_entry true,
#   names_the_amendment true, mismatches {}
# claims.C.failures []            -> claim C PASS
```

**The limit is real and the fragment does not hide it.** No defect, but worth
stating in the review record: the strongest available check of this surface is
still author-side, and a future round that wants independent verification of the
README→entry coupling should have a different seat land the row.

## 6. What this review did not do

Did not edit the README; did not re-author the row; did not certify claim C.

## 7. Replay

```sh
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
python3 -B reports/round-28/readme/sweep.py
python3 -B reports/round-28/readme/sweep.py --selftest        # 12/12
python3 -B reports/round-28/audit/entry-audit.py --partition linguistics
python3 -B reports/round-28/run-validation.py --check        # claim C PASS
sha256sum corpus/README.md                                   # 053966a2…
```
