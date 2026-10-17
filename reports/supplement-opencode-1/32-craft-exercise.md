# 32 — Craft exercise: sound change vs. taboo vs. borrowed garment terms

Wave: `supplement-opencode-1` (not a numbered GLM round). Baseline revision:
`fe34faaafbe0add59ff68827a0df6c5782a72404`. Author-side evidence only: no
`SHONEN` marks and no rank promotion are claimed here; this report is a lane
record and its exercise output is non-canon.

Deliverables (only files written by this worker):

- `examples/supplement-opencode-1/sound-change-vs-taboo.json` — the worked
  exercise (non-canon) plus the source-recheck envelope (`wave`,
  `baseline_revision`, `entry`, `entry_sha256_before`, `checked_at_utc`,
  `audits[]`) and a machine-checkable expectations table.
- `reports/supplement-opencode-1/scratch/32/check_exercise.py` — stdlib
  in-memory checker (scratch path per worker rules; the report carries the
  commands and outputs for durability).
- This report.

Baseline entry hashes (measured, not remembered):

```
$ git show fe34faaafbe0add59ff68827a0df6c5782a72404:corpus/knowledge/linguistics/historical-linguistics.md | sha256sum
258350fbe09059a910caddfcbd9c1cdb5d7ef37c5e15cf202977fc26e2653dbd
$ git show fe34faa:...:corpus/knowledge/synthesis/taboo-euphemism-lifecycle.md | sha256sum
ee606018e86f73d5501862b6194b5aaa7335e55b966761e7b5a45503af11296c
$ git show fe34faa:...:corpus/knowledge/synthesis/loanword-material-dating.md | sha256sum
bb08d4585033d856aaccb6b3548cfb8ce598ad226db4648d878109b9188e6fd8
```

## Commands

All commands run from the repo root on 2026-10-17 (UTC), Python 3.14.7.

```
$ python3 reports/supplement-opencode-1/scratch/32/check_exercise.py \
    examples/supplement-opencode-1/sound-change-vs-taboo.json
OK all checks passed (audits=7, mech_cases=11, derivations=9, approx_checks_runner=37)   # exit 0

$ python3 reports/supplement-opencode-1/scratch/32/check_exercise.py \
    examples/supplement-opencode-1/sound-change-vs-taboo.json --report \
    reports/supplement-opencode-1/32-craft-exercise.md
OK all checks passed (audits=7, mech_cases=11, derivations=9, approx_checks_runner=37)   # exit 0

$ python3 reports/supplement-opencode-1/scratch/32/check_exercise.py \
    examples/supplement-opencode-1/sound-change-vs-taboo.json --counts
{"retrieval_status_blocked": 1, "retrieval_status_full_text": 6, "total": 7,
 "verdict_contradicted": 0, "verdict_supported": 5, "verdict_unresolved": 2, ...}        # exit 0

$ python3 reports/supplement-opencode-1/scratch/32/check_exercise.py --selftest
SELFTEST OK 10/10 tamper cases detected                                                 # exit 0
```

What the checker does: rebuilds the toy law engine from `law_list.order`,
recomputes all 11 `mech_expectations` cases (14 forms) in memory, runs the
reversed-order control, checks each derivation has positive **and** negative
controls and a `method_trace`, checks the audit rows' schema/verdicts/excerpt
lengths and that the declared `audit_counts` reproduce, checks the name-avoidance
distribution test, the loan strata (S1/S2), the register partition (D8), that the
symbol readings are audience-distinct and multiple, and screens exercise text for
universal one-domain phrasing and for real sacred terms (word-boundary match with
an explicit "world bible" exception for this repo's own term of art).

Correction recorded (calibration): the checker's first run produced 2 false
positives — substring matching flagged "world bible" as the term "Bible". Fixed
by word-boundary matching plus the explicit exception; the sacred-term screen
stays active for the exercise body. The negative selftest (10 planted tampers,
including a tampered derived form, a stripped negative control, a 41-word
excerpt, an invalid verdict, a count mismatch, and a universal-phrasing
injection) still detects all 10 after the fix.

Derivations were also dry-run before the JSON was written, with the same engine:

```
tapa -> tav (rev tap) | pata -> pat | saku -> sah (rev sak) | kasa -> has
miru -> mir | mirutapa -> mirutav (rev mirutap) | apika -> avih (rev avik)
vesava -> vesav | kalu -> har (rev hal) | haru -> har | aku -> ah | salpa -> salp
sakra -> sakr
```

## Design assumptions

1. Toy forward calendar; years 40–120 are the only window in which laws L1–L4
   are productive (Era I), Era II runs 320–420.
2. L1–L4 are exceptionless in their stated environments; apparent exceptions
   would need a loan, learned channel, or analogy — none is modeled.
3. Loans enter from one invented donor variety through one channel per stratum;
   dialect mixture excluded by assumption.
4. The avoidance rule targets a referent's designation, not a sound sequence:
   homophones of the avoided form survive (D9's dawn word).
5. The recitation register is a memorized frozen form; its retention of `aku`
   and `kalu` proves nothing about everyday speech.
6. Every dated witness (roll of year 95, roll of year 340, inventory of year
   352) is invented; the exercise shows method, not history.

## Derivations

| id | mechanism | positive control | negative control |
|---|---|---|---|
| D1 | L1 lenition p>v /V_V | tapa → tav | pata → pat (p word-initial; L1 must not fire) |
| D2 | L2 l>r feeding L3 | kalu → har | salpa → salp (l and p non-intervocalic) |
| D3 | L3 k>h /#_V and /V_V | saku → sah; kasa → has | sakra → sakr (k in cluster) |
| D4 | L4 word-final vowel loss | miru → mir | mirutapa → mirutav (internal u kept) |
| D5 | ordering/feeding | declared order gives tav, har | reversed order gives tap, hal |
| D6 | pre-law loan | apika → avih (participates in the laws) | must not resurface as avih in the post-law stratum |
| D7 | post-law reborrowing | apika → apika (no law applies) | avih must not appear in the post-law witness |
| D8 | taboo replacement + register partition | vesava → vesav in everyday speech | recitation keeps aku; everyday avoids aku/ah |
| D9 | name avoidance (referent, not sound) | year-340 roll designates the founder `en` | same roll keeps `har` "dawn" (homophone survives) |

Mechanical cases are recomputed by the checker from the law list, not compared
against constants held only in the script.

## Source rechecks

7 audits in the JSON's `audits[]`; 6 rows retrieved full text via the fetch
channel, 1 blocked; verdicts 5 supported, 2 unresolved, 0 contradicted. The
`WebSearch` backend was quota-blocked (HTTP 403) for this whole round, so all
retrievals were direct page fetches; `etymonline` returned 403 and the Met
object page returned HTTP 429 twice.

- `audit-01` (supported; coupling language+myth): bear-name avoidance
  substitution — retrieved full text [wiktionary.org/wiki/bear].
- `audit-02` (unresolved; coupling language+myth): the motivation cannot be
  stated as settled — the same page hedges ("presumably") and cites Ringe
  2006:106 doubting the *bʰer- root. **Flagged for the parent**: the corpus
  bullet in `historical-linguistics.md` §9 presents the coupling without that
  hedge. No erratum was written (the entry is outside this worker's write
  scope); this is a routed defect candidate, not a verification.
- `audit-03` (supported): Latin `castra` → OE `ceaster` → English place-name
  elements [wiktionary.org/wiki/Chester].
- `audit-04` (supported; language+myth): `zounds` < "God's wounds"
  [wiktionary.org/wiki/zounds].
- `audit-05` (supported; language+era): naming-taboo substitution/blanks/stroke
  omission [en.wikipedia.org/wiki/Naming_taboo] — reference-tier corroboration
  only; the entry's cited manual (W22) and chinaknowledge.de were not
  retrievable.
- `audit-06` (supported; language+era+material): `キリシタン` < Portuguese
  `cristão` [wiktionary.org/wiki/キリシタン].
- `audit-07` (unresolved; era+dress coupling): the Met rank-badge record could
  not be re-verified (HTTP 429; JSON API not extractable through the fetch
  channel). Preserved unresolved, not counted as confirmation.

Unresolved outcomes are preserved by design: nothing blocked was laundered into
a supported verdict, and no page numbers or quotations were invented.

## Lore handoff limits

- Non-canon: all forms, dates, roles, and rules are design variables; lore-
  shokunin (world bible) owns canon decisions.
- Hand off law lists, strata tables, and the avoidance ledger as options with
  confidence grades (`design hypothesis` / `conditional`), not as world facts.
- Do not copy any real ritual, oath, or restricted text into the world bible on
  the strength of this exercise; the audits license method choices only.
- Symbol readings are role- and era-bound; the exercise carries an explicit
  constraint against any single-domain universal reading, and in-world
  disagreements (is `har` one etymon or two?) stay open.
- The merged founder-name and dawn forms remain indistinguishable in Era II —
  keep that ambiguity in the handoff rather than resolving it here.

## Limits / unresolved

- Scratch checker lives under `reports/supplement-opencode-1/scratch/32/` —
  if scratch is cleaned, regenerate it from this report's Commands section
  before re-running.
- `audit-02` and `audit-07` remain unresolved; the former is a possible errata
  candidate for the owning lane, the latter needs a non-rate-limited retrieval
  route.
- No corpus bytes were modified; no erratum was appended (no assigned
  knowledge entry to correct).
