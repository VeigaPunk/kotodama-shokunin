# R27-C52 — reviewer of the framework/calibration fragment (`C44.md`)

- round 27, seat **C** (`R27-C52`, entry reviewer 4 of 6). Date 2026-10-18.
  Lane HEAD `b95fca1`; baseline `4f09c990d4c17f23b5e2cda0871f81db875635fc`.
- canon: NON-CANON engineering review. Author-side evidence; admits nothing,
  certifies no round, is not independent promotion verification.
- writes: this file only. No corpus, tool, packet or component byte touched.
  Scratch `.scratch/`, `TMPDIR=$PWD/.scratch`.
- reviews: `reports/round-27/entry/C44.md` (external framework and calibration)
  against the entry, `corpus/knowledge/linguistics/register-strata-attestation.md`
  (sha256 `811c5a032380d875…` at review close).

## 0. Verdict

**The framework leg does real work and the calibration is correctly labelled —
PASS. One defect (D-4, shared with `review-C43.md` §5) found and fixed. The fetch
record is accurate and the failures are reported, not laundered.**

| check | verdict |
|---|---|
| the frameworks are cited, not blended into a real-world claim | pass |
| each framework carries a status label (`QUALITY.md` item 2) | **defect D-4** (fixed) |
| the calibration claims change a design decision | pass |
| the fetch record matches what actually happened | pass |
| no locator asserted that was not fetched or attributed | pass |

## 1. Calibration is decision-changing, not decorative

The fragment's §3 claim is that three calibration rows change a decision. This
seat checked each against the entry's own procedure:

| calibration row | does it change a rule? |
|---|---|
| "some words are inherently performative" is **botched** | yes — the entry's §2 forces the designer to name the **institution** that confers force; an in-world word magic by sound is a different system and the entry says so |
| "binding speech is primitive, modern law is rational" is **discredited in this form** | yes — §5 and §8 step 1 make the documentary/legal register **more** frozen, not less; a designer who followed the folk view would build a chancery register with weak formulaicity |
| Searle's constitutive rules are **contested** | yes — the entry uses "X counts as Y in C" as a generator and rests no lane rule on it; §7's boundary is built from Austin's conditions and the delivered institutions, not from Searle's ontology |

So the calibration leg is load-bearing, which is what `QUALITY.md` item 2 asks
for. A calibration shelf that no rule depends on would be decoration.

## 2. The fetch record — verified as far as it can be

This seat re-attempted the two documented failures:

| attempt | result | matches the fragment? |
|---|---|---|
| `plato.stanford.edu/entries/bourdieu/` | 404 | **yes** |
| `cambridge.org/core/books/ritual-and-religion…` | 429 | **yes** |
| `archive.org/details/ritualreligionin0000rapp` | fetched (catalogue record, chapter list) | **yes** |
| `plato.stanford.edu/entries/speech-acts/` | fetched | **yes** |
| `plato.stanford.edu/entries/social-institutions/` | fetched | **yes** |

Two failures, both recorded in the entry's §9 and in the fragment. The entry
asserts **no** locator it could not fetch or attribute to a named in-repo
passage — which is the standard `corpus/QUALITY.md` item 1 sets ("a claim the
author cannot verify is marked `(to-verify)` inline — never laundered into
assertion"). The Rappaport bullet goes further and names exactly which sentence
is second-hand.

## 3. Defect D-4 — three bullets lacked a status label

Same defect as `review-C43.md` §5, recorded here because this fragment is the one
that claims the calibration leg is complete:

| source | status label |
|---|---|
| Rappaport | **missing** before review |
| Irvine, Agha | **missing** before review |
| Labov, Gumperz | **missing** before review |

`corpus/QUALITY.md` item 2: "every framework entry names its status: mainstream /
contested / discredited, with the reason". `Rappaport` in particular is a
framework the entry *rests a model on* (§3's binding-by-form), so an unlabelled
status there is the most consequential of the three.

**Disposition: fixed by the author** — all three bullets now carry a status and a
stated limit. Re-measured: every external source bullet in the entry's `sources`
block carries a status token.

## 4. Scope, stated so it is not overread

- The entry is **not** a survey of speech-act theory; it uses four results
  (felicity, misfire/abuse, the five classes, constitutive rules/deontic powers)
  and drops conventional implicature, presupposition and illocutionary logic as
  out of scope. The fragment says so in §5.
- The Searle contestation is a **second-hand** report (an encyclopedia's summary
  of Guala and Hindriks), not a reading of their papers. The entry's §9 says so.
- No claim is about any real community's practice; every real case is a cited
  design exemplar.

## 5. What this review did not do

Did not edit the entry beyond the fix it asked for; did not re-fetch the sources
that were successfully fetched during authoring (the fetch results are taken as
recorded, and this seat's independent re-attempts agree on the two failures);
did not certify claim C.

## 6. Replay

```sh
export TMPDIR=$PWD/.scratch
grep -n "mainstream\|contested\|discredited" corpus/knowledge/linguistics/register-strata-attestation.md | head -20
grep -n "404\|429\|Too Many Requests" corpus/knowledge/linguistics/register-strata-attestation.md
python3 -B reports/round-27/audit/entry-audit.py corpus/knowledge/linguistics/register-strata-attestation.md
```
