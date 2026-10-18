# R27-C53 — reviewer of the decision-record fragment (`C45.md`)

- round 27, seat **C** (`R27-C53`, entry reviewer 5 of 6). Date 2026-10-18.
  Lane HEAD `b95fca1`; baseline `4f09c990d4c17f23b5e2cda0871f81db875635fc`.
- canon: NON-CANON engineering review. Author-side evidence; admits nothing,
  certifies no round, is not independent promotion verification.
- writes: this file only. No corpus, tool, packet or component byte touched.
  Scratch `.scratch/`, `TMPDIR=$PWD/.scratch`.
- reviews: `reports/round-27/entry/C45.md` (the decision record) against the
  entry, `corpus/knowledge/linguistics/register-strata-attestation.md`
  (sha256 `0d993a267f6beb43…` at review close).

## 0. Verdict

**The decision record is real, its evidence pointers resolve, and its
measured/adopted split is honest — PASS. One defect (a stale reading the
fragment had not yet absorbed), fixed by the author.**

| check | verdict |
|---|---|
| the record exists, with the heading the instruments look for | pass |
| every row's evidence pointer resolves to a real section or file | pass |
| the measured/adopted split is accurate | pass |
| the two landing-derived rows generalise correctly | pass |
| the record's readings are current | **defect D-5** (fixed) |

## 1. The record's structure, verified

```sh
grep -n "## 10. Decision record" <entry>        # line 280
grep -c "^| \*\*RSA-" <entry>                    # 10 rows
```

Ten rows. `entry-audit.py` → `decision_record: true`; `x63` → `decision_record
{present: true, heading: "## 10. Decision record — the rules this entry
adopts"}`. Section-number pointers checked against the entry's own headings:

```python
present: ['1'..'12']  cited: ['1','2','4','5','6','7','8']  missing: []
```

**No row cites a section that does not exist.** The fragment's §2 claim — "five
of the ten rows rest on a command run this round" — was checked row by row
against the entry: the measured rows are `RSA-1`, `RSA-4`, `RSA-6`, `RSA-9`,
`RSA-10`; the adopted rows are `RSA-2`, `RSA-3`, `RSA-5`, `RSA-7`, `RSA-8`. The
count and the membership are correct.

## 2. The measured/adopted split is not rhetorical

The fragment's §2 argues that a record with all-measured rows would be thin or
dishonest, and one with all-opinion rows cannot be rechecked. This seat tested
that the split is real, not decorative: every "measured" row names a counter
that appears in a runnable command's output.

| row | named counter | runnable? |
|---|---|---|
| `RSA-1` | `law_rows`, `register_rows`, `speech_act_rows` | yes — `x59-register-law-negatives.py` |
| `RSA-4` | `0 legal / 5 illegal` | yes — the classification is published in `reports/round-27/law/design.md` §3.2 lines 205–220 |
| `RSA-6` | `not-applies` | yes — re-executing the projector with the widened guard |
| `RSA-9` | `L9-HOLD`, and the `id`-stripping differential | yes — `x59`, `L9` |
| `RSA-10` | `FAIL L1-profile` | yes — `typed-pipeline-gate.py` |

`RSA-4`'s counter was independently located by this seat in the law design's own
text (`mark-axis plain words: 27 reverse-legal: 18 reverse-ILLEGAL: 9`;
`abstract reverse-legal= 0 reverse-ILLEGAL= 5`), so the entry is quoting a
published measurement rather than restating its own conclusion.

## 3. Defect D-5 — the fragment recorded reading 2 as the current state

`C45.md` §3 states that `RSA-9` and `RSA-10` "generalise the two defects that
re-measurement exposed", and describes `RSA-10`'s stale-pin failure as
**present**: "`typed-pipeline-gate.py` now reports `FAIL L1-profile` naming all
three stale digests".

Measured by this seat at review time:

```sh
python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml
# summary: 20/20 legs passed   (exit 0)
```

The O seat had re-pinned `tools/gates/typed-pipelines.json` profile `d4` to
`packet 86079a67…`, discharging the failure. So the fragment's present tense was
**stale**, and it is the same failure class the entry itself is about — a record
that describes a superseded state.

**Disposition: fixed by the author.** `C45.md` §3 now records the full sequence
(failure at reading 2, discharge at reading 3) and the entry's `RSA-10` evidence
column carries both halves. This is the correct repair: not deleting the
observation, but dating it.

## 4. What the record refuses to do — verified

- **No canon claim.** `CANON_CLAIM_RE` (`\bis canon|canoniz(ed|es)|adopted as
  canon`) returns no match on the entry; `PROVINCE.md`'s boundary is stated in
  §12.
- **No invented hold id.** `RSA-6`/`RSA-7` describe a discipline; the entry
  names where a hold would live and coins none. `grep -c "D4L-REGISTER-LAW"` on
  the entry → 0.
- **No merge into the rank ledger.** §7 refutes the Δ6 shape mechanically, and
  `RSA-5` states the link-not-merge rule.

## 5. What this review did not do

Did not edit the entry or the fragment beyond the fix it asked for; did not
re-run `x59`'s `L9` differential (taken as published in the instrument's own
output, which this seat read); did not certify claim C.

## 6. Replay

```sh
export TMPDIR=$PWD/.scratch
grep -c "^| \*\*RSA-" corpus/knowledge/linguistics/register-strata-attestation.md
python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml | tail -2
python3 -B reports/round-27/audit/x59-register-law-negatives.py | tail -3
python3 -B reports/round-27/audit/entry-audit.py corpus/knowledge/linguistics/register-strata-attestation.md
```
