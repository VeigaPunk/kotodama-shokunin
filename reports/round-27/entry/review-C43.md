# R27-C51 — reviewer of the source-ledger fragment (`C43.md`)

- round 27, seat **C** (`R27-C51`, entry reviewer 3 of 6). Date 2026-10-18.
  Lane HEAD `b95fca1`; baseline `4f09c990d4c17f23b5e2cda0871f81db875635fc`.
- canon: NON-CANON engineering review. Author-side evidence; admits nothing,
  certifies no round, is not independent promotion verification.
- writes: this file only. No corpus, tool, packet or component byte touched.
  Scratch `.scratch/`, `TMPDIR=$PWD/.scratch`.
- reviews: `reports/round-27/entry/C43.md` (source ledger, pins, churn
  discipline) against the entry, `corpus/knowledge/linguistics/register-strata-attestation.md`
  (sha256 `811c5a032380d875…` at review close).

## 0. Verdict

**The ledger is accurate and the churn discipline is the right one — PASS. Two
defects found, one in the fragment (fixed) and one in the entry (fixed).**

| check | verdict |
|---|---|
| the ledger's counts match the instruments | pass |
| the four pinned digests re-derive | pass |
| the churn discipline is applied, not asserted | pass |
| the "pins=4 / sweeps=0" reading is honestly bounded | pass |
| fragment lemma `linguistic-anatomy.md` | **defect D-2** (fixed by author) |
| entry: framework-status label missing on three bullets | **defect D-4** (fixed by author) |

## 1. The ledger's counts, re-derived by this seat

```sh
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
python3 -B reports/round-27/audit/entry-audit.py corpus/knowledge/linguistics/register-strata-attestation.md
# bar=True filler=False src=19/19 refs_unres=0 digests_bad=0 couples_unres=0
python3 -B reports/round-27/audit/x63-entry-source-resolvability.py --offline --json <entry>
# locators.resolved 36 | unresolved 0 | exempt 0 | pins 4 | sweeps 0 | findings 0
```

Both match `C43.md` §1 exactly. The fragment's honesty about `sweeps=0` — it says
the entry's absence sweep is quoted as prose commands and is therefore not scored
as a machine-reproducible sweep cell — is the correct reading, and this seat
confirmed the sweep commands do reproduce when run by hand (see `review-C42.md`
§1).

## 2. The four pins, re-derived

```sh
sha256sum corpus/knowledge/linguistics/sociolinguistics-registers.md \
          corpus/knowledge/myth-symbol/ritual-liminality.md \
          reports/round-26/register/design.md reports/round-26/register/forms.md
# 95ea235f9e10…  b57bf9ac3f8c…  27d23fa67d0b…  06635a1c123e…
```

All four match the entry. All four are **filed** artifacts whose bytes cannot
legitimately move, which is exactly the rule the fragment states.

## 3. The churn discipline — verified as *applied*, not merely described

The fragment claims the entry cites round-27 peers by revision because they were
moving. This seat verified the claim against the bytes:

```sh
grep -c "sha256 \`[0-9a-f]\{64\}\`" <entry sources block>     # 4 — the filed four only
grep -c "Cited by revision, not by digest" <entry>            # 4 — the churning peers
```

and re-measured two of the peers to confirm they are still churning:

```
reports/round-27/law/design.md   9d5c1dd7… (moved from 00f201b3… during authoring)
reports/round-27/law/rules.md    c6935957… (moved from 9b0d1415… during authoring)
```

The `x63` history the fragment reports — 3 `pin-drift` → 1 → 0 — is consistent
with what this seat can still observe (the two law files moved again after the
fragment was written; had their digests been pinned, they would be drifting
today). **The discipline is correct and it is load-bearing.**

## 4. Defect D-2 — a fabricated lemma (fixed)

`C43.md` §4 named the Bourdieu citation path as `linguistic-anatomy.md:67`. No
such file exists:

```sh
ls corpus/knowledge/linguistics/linguistic-anatomy.md   # No such file or directory
ls corpus/knowledge/linguistics/linguistic-anthropology.md   # exists
```

The entry itself states the path correctly (`linguistic-anthropology.md:67`).
**Disposition: fixed by the author** in `C43.md`. Recorded because a
plausible-looking filename that resolves to nothing is the precise failure a
source ledger exists to prevent, and `x63`'s `X63-D` leg would have caught it if
the fragment were an entry.

## 5. Defect D-4 — three framework bullets carried no status label (fixed)

`corpus/QUALITY.md` item 2 requires every framework entry to name its status
(mainstream / contested / discredited). Measured over the entry's `sources`
block by this seat:

| source | status label before review |
|---|---|
| Austin, Searle, Tambiah, Bourdieu, Clanchy | **present** |
| Rappaport | **missing** |
| Irvine, Agha | **missing** |
| Labov, Gumperz | **missing** |

**Disposition: fixed by the author** — all three bullets now carry a framework
status and a stated limit (Rappaport: mainstream, but a comparative
generalisation not a tested universal; Irvine/Agha: mainstream, but enregisterment
describes how a register *reads*, not how it becomes binding; Labov/Gumperz:
mainstream, cited only for the reading mechanism and not relied on for any law
row). Re-measured after the fix: every external source bullet carries a status
token.

## 6. What this review did not do

Did not edit the entry or the fragment beyond the two fixes it asked for; did not
re-execute the entry's fetches; did not certify claim C.

## 7. Replay

```sh
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
python3 -B reports/round-27/audit/entry-audit.py corpus/knowledge/linguistics/register-strata-attestation.md
python3 -B reports/round-27/audit/x63-entry-source-resolvability.py --offline --json \
    corpus/knowledge/linguistics/register-strata-attestation.md
sha256sum corpus/knowledge/linguistics/sociolinguistics-registers.md \
    corpus/knowledge/myth-symbol/ritual-liminality.md \
    reports/round-26/register/design.md reports/round-26/register/forms.md
ls corpus/knowledge/linguistics/linguistic-anatomy.md   # must fail
```
