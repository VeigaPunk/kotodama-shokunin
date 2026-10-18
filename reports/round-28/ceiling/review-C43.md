# R28-C53 — reviewer of `C43.md` (the amendment)

- **seat:** R28-C53 (C-ceiling, reviewer 3 of 6). **lane:**
  `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
- **date:** 2026-10-18. **lane HEAD** `69cecbc`.
- **canon:** NON-CANON engineering review. Author-side evidence; admits nothing,
  certifies no round, is not independent promotion verification.
- **writes:** this file only. No corpus byte touched. Scratch `.scratch/`,
  `TMPDIR=$PWD/.scratch`.
- **reviews:** `reports/round-28/ceiling/C43.md` against the amended entry
  `corpus/knowledge/linguistics/register-strata-attestation.md`
  (sha256 `645d692932edec50c2ec4dbd07cc73da37efeb368a338f2eee5aa54a798c5784`).

## 0. Verdict

**PASS. No defect. The append-only claim is verified by two independent methods,
and the fragment's supersede-vs-stand table is accurate against the amendment's
own text.**

| check | verdict |
|---|---|
| the entry's bytes are a strict prefix of the live file | pass — `startswith` True |
| no baseline section was removed | pass — `lost_sections []` |
| the new section carries the ceiling vocabulary | pass |
| the amendment cites a round-27 measurement | pass |
| the supersede/stand table matches the amendment | pass |
| the `C45.md` citation the fragment rests on resolves | pass |

## 1. The append-only claim, re-derived

```sh
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
python3 -B - <<'PY'
import re, subprocess
base = subprocess.run(['git','show','6c0ac4484d7ee5d15aaf190e7ad3b8817ea13ede:'
    'corpus/knowledge/linguistics/register-strata-attestation.md'],
    capture_output=True).stdout.decode()
live = open('corpus/knowledge/linguistics/register-strata-attestation.md').read()
S = re.compile(r'(?m)^##\s+(.+?)\s*$')
print('prefix', live.startswith(base), 'bytes', len(base.encode()), len(live.encode()))
print('sections', len(S.findall(base)), len(S.findall(live)))
print('lost', [h for h in S.findall(base) if h not in S.findall(live)])
print('new', [h for h in S.findall(live) if h not in S.findall(base)])
PY
# prefix True bytes 57996 64928
# sections 12 13
# lost []
# new ['13. Amendment (round 28): the register-lexicon ceiling, re-measured, with its mechanism']
```

The fragment's §1 block matches exactly. **The strict-prefix result is the strong
form of the claim**: not merely "no section was lost" but "every baseline byte is
still present, in order, at the front of the file". A rewrite that changed a
round-27 number in place would fail this test.

## 2. The amendment's content, spot-checked

```sh
python3 -B - <<'PY'
live = open('corpus/knowledge/linguistics/register-strata-attestation.md').read()
s13 = live[live.index('## 13.'):]
for token in ['19 legal', '18/9', 'L-45', 'licensed coda', 'LL-1', 'superseded', 'mechanism']:
    print(token, s13.count(token))
PY
# 19 legal 1 | 18/9 3 | L-45 5 | licensed coda 4 | LL-1 2 | superseded 2 | mechanism 5
```

Every element the fragment says §13 contains is present. The **supersede-vs-stand
distinction** (`C43.md` §3) is verified against the amendment's own §13.4 table:
the four `superseded`/`corrected` readings and the two `stands` readings are all
there, and the amendment states explicitly that "No decision in §10 changes."

## 3. The citation the fragment rests on

`C43.md` §4 argues that editing the round-27 numbers in place would break a
citation, and quotes `reports/round-27/entry/C45.md`. Verified:

```sh
grep -n 'RSA-4' reports/round-27/entry/C45.md
# 27:| `RSA-4` | the derivational operation picks the register's semantic profile | **measured** (`0 legal / 5 illegal` over institutional abstractions) |
```

The citation is real and it does read `0 legal / 5 illegal` — a round-27 reading
that §13.4 now supersedes while leaving the round-27 file's bytes intact. **This
is the strongest argument for the amendment form over an edit**, and the fragment
makes it correctly.

## 4. What this review did not do

Did not edit the amendment; did not re-measure the ceiling arithmetic (that is
`review-C41.md`'s subject); did not certify claim C.

## 5. Replay

```sh
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
python3 -B reports/round-28/run-validation.py --check | python3 -c \
  "import json,sys; d=json.load(sys.stdin); print(d['claims']['C']['measurement']['amendment'])"
git show 6c0ac4484d7ee5d15aaf190e7ad3b8817ea13ede:corpus/knowledge/linguistics/register-strata-attestation.md | wc -c   # 57996
wc -c corpus/knowledge/linguistics/register-strata-attestation.md       # 64928
sha256sum corpus/knowledge/linguistics/register-strata-attestation.md   # 645d6929…
```
