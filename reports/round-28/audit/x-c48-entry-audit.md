# R28-C48 — entry audit: no filler, sources resolve, index couples (round 28)

- **seat:** R28-C48 (C-audit). **lane:** `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
  **assignment (verbatim):** "C R28-C47..C48 (README + audit): README reconciled;
  entry audits."
- **date:** 2026-10-18. **declared baseline:** `6c0ac4484d7ee5d15aaf190e7ad3b8817ea13ede`;
  **HEAD at measurement:** `69cecbc7dcf575a29f29660ecac470e05260fd86`.
  **measurement stamps:** 20:13:39Z (pre-landing, 200 entries) and
  **20:20:50Z (final, binding, after the round-28 ceiling entry landed)**.
- **canon:** NON-CANON engineering evidence. This audit admits nothing, certifies
  no round, blesses no source, and adjudicates no entry's scholarship.
- **writes:** `reports/round-28/audit/entry-audit.py`, this file, and scratch
  under `.scratch/`. **No `corpus/**` byte written by this instrument.** No
  commit, no push.
- **instrument:** `python3 reports/round-28/audit/entry-audit.py`
  (sha256 `918a0c1e5654db6ea5cecaa0b8b1eea6aef37e2f2cf1c74d1a7ec2e0850a3e5c`
  at the final stamp). It **imports** round 27's audited core
  (`reports/round-27/audit/entry-audit.py`) rather than copying it, so a fix to
  the core cannot silently diverge between rounds.

## 0. Headline

Final reading (20:20:50Z, 201 entries — the round-28 ceiling entry is included):

| leg | result | force |
|---|---|---|
| **sources resolve** | 0 unresolved path refs across the corpus; every source bullet carries a locator | a hard check — a broken path is a defect |
| **index couples** | **201/201 entries indexed cleanly**: one README row each, in its own partition, byte-equal to the entry's `- topic:` text | a hard check (new this round) |
| **no filler** | 17/201 entries clear the full admission bar; 184 do not | an **admission rule for new entries**, not a retroactive verdict — see §3 |

**The round-28 ceiling entry clears every leg and the full admission bar**
(`bar=True`, `filler=False`, `src=11/11`, `index=[]` at 20:20:50Z). It is
gap-named, frontmatter-complete, decision-record carrying, grounded in round-27
artifacts and dated sources, makes no canon claim, and is indexed in the README
with a row byte-equal to its own `- topic:` head. The round-28 runner's claim C
measures the same entry from the delivered bytes and reports `failures: []`.

The bar leg's 184 is **not** a finding of 184 bad entries, and reporting it that
way would be false. The lane's gap-naming discipline was introduced in round 10
and extended in round 19; most of the corpus predates it. Round 27's audit
recorded the same split (27/200 gap-naming, 173 not) and refused the same false
reading. This instrument reports the count, prints the interpretation, and exits
0 on it; `--strict-bar` fails on it for a caller that wants that reading.

## 1. Method

```sh
export TMPDIR=$PWD/.scratch
python3 -B reports/round-28/audit/entry-audit.py --selftest   # 11/11, exit 0
python3 -B reports/round-28/audit/entry-audit.py --all        # exit 0
python3 -B reports/round-28/audit/entry-audit.py --partition linguistics
```

The instrument checks each entry against `corpus/QUALITY.md` and this round's
claim-C requirements: required header fields (`topic`/`sources`/`couples`), the
`verified-at`+`recheck` tail, locator presence on every source bullet, repo-path
resolution, sha256 pin classification, `couples:` resolution, a named gap, a
decision record, calibration vocabulary and canon hygiene — plus the new
index-coupling leg.

## 2. The index-coupling leg (new this round)

Round 27 audited the corpus and the README **separately**, so an entry could
clear the admission bar while sitting in the index under the wrong partition, or
while its README row had drifted off its `- topic:` text. Those are both
C-seat surfaces, so the legs are joined here. For every entry the instrument
requires exactly one README row, in the entry's own partition, whose text is
byte-equal to the entry's `- topic:` head text.

```sh
python3 -B reports/round-28/audit/entry-audit.py --all --json | \
  python3 -c 'import json,sys; d=json.load(sys.stdin); print(d["entries"], len(d["index_failing"]))'
# 201 0
```

Five planted controls (in `--selftest`) prove the leg fires in each failure
shape and stays quiet when clean:

| control | planted | expected |
|---|---|---|
| correct row | row text == entry topic | clean |
| drifted row | a condensed paraphrase | `ROW_TOPIC_DRIFT` |
| wrong partition | the row under `myth-symbol/` for a `linguistics/` entry | `WRONG_PARTITION` |
| unindexed entry | no row at all | `NOT_INDEXED` |
| duplicate row | the same file twice | `DUPLICATE_INDEXED` |

The live leg is clean for all 201 entries, which is the coupling claim: the
README indexes exactly the corpus, with no drift and no orphan. The live leg
asserts the invariant (`every disk entry audited and rows == files`), not a
frozen count, so a landing does not require editing the instrument — an earlier
draft asserted `200`, which the ceiling entry's landing correctly broke.

## 3. The sources-resolve leg and the bar leg

**Sources resolve.** Across all 201 entries, every repo-path locator in a source
bullet resolves on disk, and no bullet lacks a locator. This is the leg with the
hardest force: a broken path or an unlocatable claim is a provenance defect, not
a style question, and `corpus/QUALITY.md` item 1 is explicit that an invented
source is a conformance defect.

**The bar leg, read honestly.** `quality_bar` requires a named gap and a
decision record in addition to the provenance and coupling legs. 17 entries
clear it; 184 do not, and in almost every case the missing element is the
gap-naming discipline that postdates the entry:

```sh
python3 -B reports/round-28/audit/entry-audit.py --partition linguistics
# audited 21; bar clear 5; bar failing 16
# index clear 21; index failing 0
```

The five linguistics entries that clear it are the ones written under the
current discipline (`language-shift-obsolescence-revival`,
`numerals-and-measures`, `register-lexicon-ceilings`,
`register-strata-attestation`, `sound-symbolism`). The other sixteen predate it.
That is the correct reading of the number, and the instrument prints it so a
reader cannot mistake the count for a verdict.

**A digest note.** The audit classifies sha256 pins rather than blindly matching
them: `repo_matched` (a 64-hex digest matching the file its bullet names),
`repo_mismatch` (the laundering shape — a digest pinned to a different file),
`external_uncheckable` (a digest on a fetched page or offline artefact) and
`abbrev` (a truncated digest). A `repo_mismatch` fails the bar; the other classes
are reported, because a fetched page's digest cannot be re-derived from the tree.

## 4. The round-28 ceiling entry, measured

The round-28 **C-ceiling entry** landed at 17:20Z and is audited here:

```sh
python3 -B reports/round-28/audit/entry-audit.py \
    --new corpus/knowledge/linguistics/register-lexicon-ceilings.md
# new corpus/knowledge/linguistics/register-lexicon-ceilings.md \
#   bar=True filler=False src=11/11 index=[]
# exit 0
```

It clears the full bar **and** is indexed, so the round's own admission claim is
measured rather than asserted. `--new` fails the run unless both hold.

## 5. Limits of this audit

- **Same-seat instrument.** The core is round 27's audited instrument; the
  index leg and its controls are this seat's. Independent corroboration is the
  round-28 runner's own claim-C measurement, which reads the ceiling entry's
  frontmatter, grounding and canon hygiene from the delivered bytes and reports
  `failures: []`.
- **The bar leg is an admission rule.** It is not a quality verdict on the
  legacy corpus, and this audit does not present it as one.
- **Point-in-time.** The final reading is at 20:20:50Z, 201 entries. The tree
  moves under the round; re-run before quoting any count.
- **Non-canon.** This audit admits nothing, blesses no source, and makes no
  claim about any entry's scholarship.
