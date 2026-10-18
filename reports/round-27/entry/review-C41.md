# R27-C49 — reviewer of entry `register-strata-attestation.md`

- round: 27 (operator: loop 3 of 3, build 3 of 4; 64 workers on
  `devin/deepseek-v4-1-flash-high`; `reports/round-27/claims.json`), lane
  `kotodama-shokunin`, claim **C**.
- assignment (verbatim): "C R27-C47..C52 (entry reviewers x6, paired): one per
  entry-author fragment, reviewing the same surface from a different instrument
  — frontmatter, source resolvability, no filler, no duplication; verdicts
  `reports/round-27/entry/review-<id>.md`."
- date: 2026-10-18, stamps UTC. Lane baseline
  `4f09c990d4c17f23b5e2cda0871f81db875635fc`; HEAD
  `b95fca1e40f32f7346937ab6426f9ccca60e319f`.
- canon: **NON-CANON** engineering review. Author-side review evidence only; it
  admits no entry, promotes no claim, and is **not** independent promotion
  verification (lane rule, `AGENTS.md`).
- writes: **this file only**, plus gitignored scratch under `.scratch/`
  (`export TMPDIR=$PWD/.scratch` preceded every scratch-writing command). No
  corpus, tool, packet, component or pin file touched. No commit, no push.

## 0. Artifact under review and verdict

`corpus/knowledge/linguistics/register-strata-attestation.md` — new linguistics
entry, gap `register-strata-attestation`. Anchor revision: sha256
`d905fd0e1095618da7b07935b2e4ac16a79baf641810417d748942c1a20d2fca`, 54,284 bytes,
299 lines, 12 sections + head block.

**Verdict: all four mandated checks pass; two defects found, both in the
`verified-at` block's internal accounting, both fixed by the author before this
review closed.** No fabrication, no filler, no duplication.

| mandated check | verdict |
|---|---|
| frontmatter completeness | **pass** |
| source resolvability | **pass** (36 locators, 0 unresolved, 4 pins re-derived) |
| no filler (gap named, real, delivered) | **pass** |
| no duplication of an existing entry | **pass** |

## 1. Frontmatter completeness — PASS

House profile of the five committed fields, each exactly once in the head block
(text before the first `## `, line 33): `- topic:` (3), `- gap filled:` (4),
`- sources:` (5, with 19 nested bullets), `- couples:` (25), `- source:` (26),
`- verified-at:` (27), `- recheck:` (28).

Instrument: `python3 -B reports/round-27/audit/entry-audit.py … --json` →
`header_fields ['couples','gap filled','recheck','source','sources','topic','verified-at']`,
`header_missing_required []`, `header_tail_ok True`. Independently,
`x63-entry-source-resolvability.py --offline --json` → `frontmatter.present`
all six, `missing []`.

## 2. Source resolvability — PASS, and here is what that does **not** mean

Re-run by this seat, lane root, `TMPDIR=$PWD/.scratch`, 2026-10-18:

| instrument | result |
|---|---|
| `entry-audit.py` | `src=19/19 refs_unres=0 digests_bad=0 couples_unres=0`, exit 0 |
| `x63 --offline --json` | `locators.resolved` 36, `unresolved 0`, `exempt 0`, `pins 4`, `findings 0`, exit 0 |
| `readme/sweep.py` | `rows 200 files 200`, `missing_from_index 0`, `topic_mismatch 0`, `header_drift {}`, exit 0 |

**The four pinned digests were re-derived by this seat** (not taken from the
entry): `sociolinguistics-registers.md` `95ea235f9e10…`,
`ritual-liminality.md` `b57bf9ac3f8c…`, `reports/round-26/register/design.md`
`27d23fa67d0b…`, `reports/round-26/register/forms.md` `06635a1c123e…`. All four
match.

**What this does not mean.** A resolving locator is not a correct source. Three
of the entry's bullets are **second-hand** citations (Tambiah, Bourdieu, Clanchy
are cited *by path through* neighbouring entries, not fetched), and the entry
says so in each bullet. This review confirms the paths resolve; it does not
confirm the underlying scholarship, and the entry does not claim it does.

## 3. No filler — PASS

The gap is named in the head block and is **not** invented by this entry:

- the lane declared it first, as a finding: `reports/round-26/register/review.md`
  §6.3 (`RD-5c`) — "the delivered tree has **no component that owns a register
  law**";
- it is measurable on delivered bytes by an instrument built on **different
  machinery** from the lane gate (`reports/round-27/audit/x59-register-law-negatives.py`
  uses a Ruby YAML loader and imports no lane code), which returns `HOLD` with
  named counters;
- the absence sweep **reproduces**: this seat re-ran the entry's own commands
  minus the entry and got `0` files for `illocutionary`, `perlocutionary`,
  `constitutive rule`, `deontic`, `attestation register`, `register law`; and
  got the two honest `felicity` hits the entry itself reports
  (`semantics-pragmatics.md:88`, `ritual-liminality.md:112`).

## 4. No duplication — PASS, with the boundary checked

The entry does not restate a neighbour. This seat ran the overlap check:

```sh
for f in $(grep -ril "speech act" corpus/knowledge/); do grep -qi register "$f" && echo "$f"; done
```

15 files come back, and every one is a **mention** (a one-line framework aside
or an unrelated sense of "register" as *speech style* or *musical/ritual
register*). The entry is the only file whose subject is the attestation register
and its law, and its §1 table states the separation explicitly rather than
asserting novelty. The four nearest neighbours are named and extended, not
copied: `semantics-pragmatics.md` §5 (framework survey),
`sociolinguistics-registers.md` §4 (social registers),
`politeness-taboo-euphemism.md` (politeness ≠ binding),
`ritual-liminality.md:112` (names the code, does not write it).

## 5. Defects found by this seat, and their disposition

### D-1 — the `verified-at` block asserted a digest "re-derived at write time" for files that were moving

The first draft's `verified-at` line read: "Every repo-path locator above was
resolved on disk and every digest in the `sources` list re-derived at write
time." Measured, that sentence was false for four round-27 peer files, which
moved inside the round:

```
reports/round-27/law/design.md    00f201b3… → 9d5c1dd7…
reports/round-27/law/rules.md     9b0d1415… → c6935957…
reports/round-27/audit/x59-register-law-negatives.py  f5f5d46a… → 7e3b3559…
reports/round-27/scribe/x54-syllabify-spotcheck.py    1bfa9e3a… → ee370f78…
```

`x63` scored three `X63-E pin-drift` findings on the first pass. **Disposition:
fixed by the author** — the round-27 peer bullets now cite **by revision** with
the movement recorded and the reason stated, and the `verified-at` line says
which files were stable and which were not. Re-measured: `pins=4`, `findings=0`.
This is the correct repair (change the citation form), not a re-pin, which would
have made the audit green while the file kept moving.

### D-2 — a fabricated lemma in this reviewer's own source ledger (`linguistic-anatomy.md`)

`reports/round-27/entry/C43.md` §4 named the Bourdieu citation path as
`linguistic-anatomy.md:67`. **No such file exists**; the real path is
`corpus/knowledge/linguistics/linguistic-anthropology.md:67`, as the entry
itself correctly states. **Disposition: fixed by the author** in `C43.md`. This
is recorded rather than silently corrected because it is exactly the failure the
review exists to catch — a plausible-looking filename that resolves to nothing —
and because the fragment is evidence, not a draft.

## 6. What this review did not do

- Did not edit the entry, the fragments, the packet, any component or any tool.
- Did not re-execute the entry's external fetches (the Stanford Encyclopedia
  reads are cited, not reproduced); the two documented fetch failures (404, 429)
  are taken as reported, and the entry's decision not to assert a locator it
  could not fetch is the correct one.
- Did not certify the round. Claim C's verdict belongs to
  `reports/round-27/run-validation.py`, which this seat read but did not run to
  acceptance.

## 7. Replay

```sh
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
python3 -B reports/round-27/audit/entry-audit.py corpus/knowledge/linguistics/register-strata-attestation.md
python3 -B reports/round-27/audit/x63-entry-source-resolvability.py --offline --json \
    corpus/knowledge/linguistics/register-strata-attestation.md
python3 -B reports/round-27/readme/sweep.py
sha256sum corpus/knowledge/linguistics/sociolinguistics-registers.md \
    corpus/knowledge/myth-symbol/ritual-liminality.md \
    reports/round-26/register/design.md reports/round-26/register/forms.md
```
