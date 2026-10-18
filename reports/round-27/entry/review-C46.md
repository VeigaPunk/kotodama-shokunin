# R27-C54 — reviewer of the README-reconciliation fragment (`C46.md`)

- round 27, seat **C** (`R27-C54`, entry reviewer 6 of 6). Date 2026-10-18.
  Lane HEAD `b95fca1`; baseline `4f09c990d4c17f23b5e2cda0871f81db875635fc`.
- canon: NON-CANON engineering review. Author-side evidence; admits nothing,
  certifies no round, is not independent promotion verification.
- writes: this file only. No `corpus/README.md` byte touched by this seat.
  Scratch `.scratch/`, `TMPDIR=$PWD/.scratch`.
- reviews: `reports/round-27/entry/C46.md` (README reconciliation) against
  `corpus/README.md` and the entry,
  `corpus/knowledge/linguistics/register-strata-attestation.md`
  (sha256 `0d993a267f6beb43…` at review close).

## 0. Verdict

**The index is reconciled and the row is byte-equal to the entry's topic —
PASS. One defect (a fabricated title in the fragment), fixed by the author.**

| check | verdict |
|---|---|
| the sweep is green and reproduces | pass |
| the row is byte-equal to the entry's own `- topic:` text | pass |
| the section header and totals line moved with the file count | pass |
| the append-only discipline held (1.6 preserved under 1.7) | pass |
| the fragment's source title | **defect D-6** (fixed) |

## 1. The sweep, re-run by this seat

```sh
export TMPDIR=$PWD/.scratch
python3 -B reports/round-27/readme/sweep.py
# parts {"civilizations": 94, "culture-material": 18, "linguistics": 20,
#        "myth-symbol": 19, "synthesis": 29, "verification": 20}
# rows 200 files 200
# missing_from_index 0 []  topic_mismatch 0 []  orphan_rows 0 []
# header_drift {}          totals_line 200 totals_ok True
# readme_sha256 d9d97d7f860c15bb…
# exit 0
```

Every leg clean, at the review stamp. The `topic_mismatch 0` result is the
load-bearing one, and this seat verified it independently rather than trusting
the instrument:

```python
topic = <entry's `- topic:` text>       # 1155 chars
row   = <README's row text>             # 1155 chars
byte-equal: True
```

The row is the entry's own topic line, verbatim — the convention rounds 10/19/20
settled on after revision 1.4 was found to carry condensed paraphrases.

## 2. The append-only discipline, verified on the index itself

```sh
grep -n "^revision:" corpus/README.md
# 3:revision: 1.7 — Round-27 register-strata landing
# 15:revision: 1.6 — Round-27 re-measurement
# 35:revision: 1.5 — Round-20 reconciliation
grep -c "had not landed" corpus/README.md      # 1
```

Revision 1.6's carried item ("the round-27 register-strata entry had not landed
at this pin") is **still present** under 1.7, and 1.7 says so explicitly. That is
the lane's append-only rule applied to the index: a revision block is a dated
measurement, and a later measurement is a new block, not a rewrite. The fragment
records this correctly.

## 3. The gap the index does **not** close — confirmed

`C46.md` §4 says the entry adds no bullet to `§ Known gaps (frontier)`. Verified:

```sh
sed -n '274,436p' corpus/README.md | grep -c -i "register law\|attestation\|speech act\|illocution"
# 0
```

No frontier bullet mentions the subject. The fragment's statement is accurate,
and it matters: a reader who searched the frontier section for this gap would
find nothing. The same limitation is now also stated in `C42.md` after its own
review (`review-C42.md` §3).

## 4. Defect D-6 — a fabricated name in the source list (fixed)

`C46.md` §3 listed the entry's external frameworks as "Austin, Searle, Tambiah,
Rappaport, Bourdieu, **Clanville**, Irvine". There is no `Clanville`; the source
is **Clanchy** (1979/1993), as the entry and the entry's own `sources` block both
state.

**Disposition: fixed by the author** in `C46.md`. This is the third fabricated or
mistyped name this review pair found (after `linguistic-anatomy.md` and the
present-tense `L1-profile`), and all three are in **fragments**, not in the
entry — which is the correct distribution: the entry's locators all resolve
(`x63`: `locators=41 unresolved=0`), while the fragments are prose that no
instrument parses.

## 5. Scope of this review

- Did not edit `corpus/README.md`; did not edit the entry.
- Did not certify claim C. The round validator's claim-C reading (this seat read
  it, did not run it to acceptance) records `corpus_readme.revision_head 1.7`,
  `total_files 200`, `names_the_entry true`, `mismatches {}`.
- The sweep is read-only and was re-run at review time; its counts are a
  point-in-time reading and must be re-measured before quoting.

## 6. Replay

```sh
export TMPDIR=$PWD/.scratch
python3 -B reports/round-27/readme/sweep.py
grep -n "^revision:" corpus/README.md
grep -n "^- \`register-strata-attestation.md\`" corpus/README.md
grep -c "Clanville" reports/round-27/entry/C46.md   # must be 0 after the fix
```
