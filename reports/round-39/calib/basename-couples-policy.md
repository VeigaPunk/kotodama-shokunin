# Basename-couples resolution policy

Adopted by round 39 (claim Ca, leg c) as the lane audit rule for resolving
`couples:` reference tokens in corpus knowledge entries. This document closes the
documentation leg of queue item `basename-couples-policy`
(`reports/round-37/op/defect-queue.json:202-211`: "couples resolver leaves 15
basename-only references unresolved; a working unique-basename fallback exists but
is undocumented policy"). It changes no filed bytes: the round-19 instrument stays
as filed, and successor audit instruments implement this policy.

Method/audit rule only — no canon, no promotion, no corpus byte edit; corpus
admission stays governed by `corpus/QUALITY.md:13-20`.

## 1. Token extraction (fixed, so every audit counts the same population)

- Field: the `- couples:` line of the entry header (single physical line;
  extraction per `reports/round-19/audit/entry-audit.py:75`).
- Tokens: every match of `[A-Za-z0-9_./{},\-]+\.md` in the field value
  (`entry-audit.py:31`), brace-expanded one level (`{a,b}` -> `a`, `b`;
  `entry-audit.py:34-42`), deduplicated per entry. A `:NN` anchor after a token
  is not part of the token (`calibration-registry.md:91` -> token
  `calibration-registry.md`).
- Unit: per-entry deduplicated tokens. Cross-entry repeats count once per entry;
  a global-distinct total may be cited alongside it (r37 scan: 334 per-entry
  tokens vs 222 globally distinct strings — `reports/round-37/adj/A06-verify.md:29`).

## 2. Resolution — two tiers, four classes

Tier 1 — direct (the documented rule; `entry-audit.py:87-95`, unchanged):
a token is class `direct` iff any of

    <entry directory>/<token>   <lane root>/<token>   corpus/knowledge/<token>

names an existing file.

Tier 2 — unique-basename fallback (this policy). Fires only when ALL hold:

  (a) Tier 1 failed for the token;
  (b) the token contains no `/` (pure basename form; §5.1);
  (c) exactly one file under `corpus/knowledge/<partition>/` carries that
      basename, the index being one partition level: glob
      `corpus/knowledge/*/*.md` (index construction:
      `reports/round-35/cov/C14-audit-6-10.md:252-260`).

The token is then class `fallback`, carried with its explicit mapping
`token -> corpus-relative path` in the audit output. Zero index hits ->
`unresolved`; two or more -> `ambiguous`. Neither is ever dropped, guessed, or
counted as resolved.

## 3. Reporting rules

1. The four classes are reported separately, per entry and in totals
   (`C14-audit-6-10.md:332-334` output pattern). A "zero unresolved" claim must
   state the fallback count beside it; "zero dangling couples" without the
   fallback class named is not an admissible result (r37 integration ruling:
   `reports/round-37/scribe/S04-integration-draft.md:38,80`).
2. Fallback hits are never merged into the path-resolved count.
3. Every fallback mapping is listed, not only counted.

## 4. Group-alignment leg

When a `couples:` field groups tokens under domain labels (`myth-symbol —`,
`linguistics —`, ...), every `fallback` token must map into the partition its
group label names (`corpus/knowledge/<label>/...`). A mismatch is an
`alignment` finding, not a resolution. Current population: all 15 fallback
tokens of `corpus/knowledge/myth-symbol/sacred-kingship-mythic-charter.md:37`
align — 7 linguistics, 6 culture-material, 1 verification, 1 synthesis
(independently established at r37: `reports/round-37/adj/A12-gap-fill.md:11-24`;
re-verified with full coverage by §6).

## 5. Limits — what the fallback does not do

1. No re-partitioning of slash-bearing tokens. A token with a partition prefix
   resolves (or not) on Tier 1 alone; a wrong prefix stays a finding even when
   the basename is unique elsewhere. Declared delta: the r35 C14 instrument as
   implemented keys its index on `basename(ref)` for ANY unresolved token,
   slash-bearing included (`C14-audit-6-10.md:281`); this policy narrows that
   behavior. Demonstration: token `linguistics/hero-journey-variants.md` is
   `unresolved` under this policy but would fallback-resolve into
   `corpus/knowledge/myth-symbol/hero-journey-variants.md` under the C14 code
   as written (§6, Part 3).
2. `couples:` only. The `- sources:` locator legs keep their own rules —
   existing repo path, URL, digest — with no basename fallback
   (`C14-audit-6-10.md:291-299`).
3. Existence and one-level uniqueness only. The fallback certifies that the
   target file exists uniquely and (via §4) matches its declared group; it
   certifies neither content quality nor absence of cross-domain bleed
   (`reports/round-37/adj/A12-gap-fill.md:26`).
4. Tier 1 is never relaxed. A directly resolvable token is `direct` even when a
   same-basename file exists elsewhere. The entry-directory base is why the 14
   same-partition basenames in the sacred-kingship field are `direct`, not
   `fallback`.
5. Index scope is exactly one partition level (`corpus/knowledge/*/*.md`; 6
   partitions, 212 files at adoption). Nesting, a new top-level directory, or
   duplicate basenames across partitions change the uniqueness assumption:
   re-run §6 and re-adjudicate before relying on the fallback then.
6. Glob fragments are an extractor artifact, not couples references. Star
   patterns inside the field (`corpus/knowledge/verification/*-gate.md`,
   `tools/gates/*.py` — `corpus/knowledge/verification/gate-frozen-run-standard.md:15`)
   yield partial tokens such as `-gate.md`. A successor instrument should skip
   or separately class glob fragments; this policy forbids counting them as
   unresolved couples findings or resolving them via the fallback.

## 6. Verification recipe (read-only; reproduces the filed evidence)

Run from the lane root; no writes, no runner invocation
(`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`):
