# R17-D34 — reviewer: D4 language-sketch soundness

- **Seat:** R17-D34 (reviewer, claim D `culture-d4-assembly`), round 17 (operator
  loop 2 of 3, build round 1 of 4; 64 declared workers, `opencode-go/deepseek-v4.1-flash`).
- **Assignment (verbatim):** "D4 R17-D33..D37 (reviewers x5): internal consistency;
  language sketch soundness; myth-costume coupling; hold-set hand re-derivation;
  D2/D3-lesson cross-check. reports/round-17/reviews/review-<n>.md."
- **Date / clock:** 2026-10-18, local -03:00; measurements 09:4x–09:5xZ. The wave
  was in flight; statements are pinned to the digests in review-1 §1 (packet
  `2776d85c…35d72`, HEAD `9b49a4a`).
- **Write scope:** this file only, plus scratch under `.scratch/r17-review/`
  (`TMPDIR=$PWD/.scratch` set). No artifact under `examples/`, `tools/`,
  `reports/round-{8..16}/`, or `corpus/` was written; no commit, no push.
- **Canon:** NON-CANON engineering review. Nothing here is canon, a lore receipt,
  a handoff, or a real-world clearance/rights statement.

## 0. Verdict

**The D4 language sketch is sound as a sketch: every mechanical soundness check I
ran passes, every rule output is an allophone outside the declared inventory (no
rule merges two phonemes), every delivered form I tested respects the declared
template and coda set, all eight names replay from delivered bases, and the
recorded gaps are held as `to-verify`, not laundered.** Two design-level items are
carried forward, not repaired here: the phonology gate's `A-CLASS` REVIEW on
`s → z / V _ V` (needs a finite expansion; owner D06) and the cross-referenced
coda-text contradiction F1 from review-1. The length contrast is declared with a
**notation witness only** (W-06 `sal`/`saal`; no delivered minimal pair) — that is
exactly the state amendment A-19-1 cites when dropping the conditional
`D4L-NATIVE` row, and it is recorded honestly in `02-phonology` `STR-01`.

## 1. Evidence — what was checked and observed

All commands cwd = lane root, `TMPDIR=$PWD/.scratch`, 2026-10-18. Mechanical checks
by scratch script `.scratch/r17-review/langcheck.py` over the delivered packet;
component-level facts read from `examples/culture-d4/components/02-phonology.yml`,
`03-orthography.yml`, `04-lexicon.yml`, `05-naming.yml`.

### 1.1 Phonology (`02-phonology.yml`, packet `phonology` block)

| check | observed |
|---|---|
| inventory | 14 consonants `p t k b d g m n s r l w j h`; 5 vowels `a e i o u`; `tones: 0`; `accent_levels: 1` |
| template | `(C)V(V)(C)`; `onset_clusters: false`; `coda: [n m s k l r t d]` (eight); no coda clusters |
| finite rule outputs | 6 `notable_rules`; outputs `ŋ z ts c ç` — **none is a phoneme** (allophony, no merger) |
| allophony records | 6 (`AL-1..6`) each with `output_status: allophone`, a trigger witness and a blocked witness; family and drift origin named |
| sound changes | 2 ordered (`SC-1` E0→E1 `*p → b / V_V`; `SC-2` E1→E2 `*h → ∅ / V_V` + lengthening) with ordering note and worked witnesses marked as internal reconstructions |
| loan adaptation | 2 filters (`LA-1` deaspiration `sh→s, kh→k, gh→g`; `LA-2` vowel lowering `o→a`) with delivered witnesses (`sal←shal`, `kar←khar`, `gul←ghul`, `res←resh`, `gal←gol`, `mar←mor`) |
| stress/length | fixed root-initial stress; length contrastive only under stress; `STR-01.minimal_pairs` records **no delivered length pair** (`to-verify`) and that no stress pair exists by construction |
| contrast witnesses | `W-01..W-07` (voicing ×3, nasal place, liquid, length notation `sal`/`saal` — `saal` explicitly not a delivered lexeme, coda `nes`/`nesk` illegal-cluster witness) |
| gate result (my run) | `phonology-sanity-gate` exit 1, **1 finding retained**: `A-CLASS` REVIEW — `notable_rules[3] 's → z / V _ V'` conditions on a natural class; expansion into finite contextual rules required (owner D06). No FAIL. |

### 1.2 Lexicon (`04-lexicon.yml`, 54 records)

- **Template compliance: 0 violations.** All 54 terms parse as `(C)V(V)(C)`
  sequences with single-consonant onsets and codas from the declared eight;
  0 identical-CV-syllable words; 0 vowel-sequence violations (long VV and `ai`/`au`
  only) — mechanical check, `.scratch/r17-review/langcheck-2.json`.
- **Derivations replay by hand:** `L-45 tikmes = tik+mes` (CX-01 concat) ✓;
  `L-46 mesar = mes + -ar` (CX-02) ✓; `L-47 kalen = kal + -en` (CX-03) ✓;
  `L-48 haitun = hai+tun` (CX-01) ✓. `morphology.derivation_rules` ids match the
  `constructions` block (CX-01..03), as its note states.
- **Loans:** 6 borrowed records (4 salt-road, 2 north-road), each with
  `donor_form`, `substitutions`, `entry_stage`, `referent_available_from`; entry
  stages E0/E1 respect the referent clocks.
- **Layers:** declared `LY-01` (salt-road) / `LY-02` (north-road); delivered layer
  counts native 48 / 4 / 2 match the declarations (review-1 §4 notes the
  `coverage_notes` field/route staleness, which is bookkeeping, not lexicon data).

### 1.3 Orthography (`03-orthography.yml`)

- Type: abugida with inherent `a`; four vowel marks (`e i o u`); length mark;
  seam mark; unicameral; no diacritics in the romanization (`D4-roman-1`,
  lowercase ASCII).
- Signs `SG-01..SG-20` = 14 consonant signs + 4 vowel marks + length mark + seam
  mark = **20**, matching `orthography.signs: 20`; every sign carries an origin
  dated to an E0 stamp or an E1 extension (`SG-04/05/06` derived from `SG-01/02/03`
  by the E1 voicing seam). The sign inventory derives from 02's segments, not from
  a donor script; no alphabet-first premise, no D1 letter ids.
- Length notation (`WR-03`, `SG-19`) is fixed against `STR-01`, closing the loop
  from phonology to script.

### 1.4 Naming (`05-naming.yml`, 8 names)

- Formation policy: each record exposes `formation.stem` `B1+B2`, bases, rule id,
  operation and `expected`; the plus is analysis-only. **All 8 names replay:**
  bases are delivered lexicon terms (checked: 8/8) and `expected == name` (8/8):
  `tumhai, kalker, samren, mestum, haitik, meslun, kalnes, salwer`.
- Syllable rule `(C)V(V)(C)`, codas only the eight, no clusters/geminates —
  consistent with 02.
- Licenses separate the bearer from the slot and the office: e.g. NM-02 "not an
  office claim (the hearth-keeper is appointed, not named)"; NM-05/NM-06 are
  affiliations, not titles; NM-08 declares its borrowed element (LY-01) without
  making the road a foreign institution.
- Naming gate (my run): exit 1, 8 findings — `NAME-NEAR` REVIEW (NM-05 `haitik`
  vs PAN-01 `haitir`, 1 edit, recall-oriented), 6 `PHON-INVENTORY` FAILs on the
  **English garment glosses** `GAR-01..06` (the translated-label class the typed
  routing must move off-channel), and 1 `CROSS-HOLD` HOLD (no bounded
  cross-cultural review; no clearance claimed). The two non-gloss findings are
  correctly retained, not suppressed.

### 1.5 Held gaps (recorded, not laundered)

| gap | where recorded | status |
|---|---|---|
| no delivered length minimal pair | `02-phonology` `STR-01.minimal_pairs`; A-19-1 in `expected-holds.fragment.json` | `to-verify`; the D4L-NATIVE conditional row is dropped on this basis |
| northern sister variety's inventory unmodelled | `02-phonology` `OQ-P1`; `11-contact-history` | `to-verify` |
| E0 stamp inventory size before extension | `03-orthography` `OQ-O2` | `to-verify` |
| E0/E1 witnesses are internal reconstructions | `02-phonology` `CAL-P2` | `to-verify` |
| `s → z / V_V` needs finite expansion | phonology gate `A-CLASS` REVIEW; retained in `ASSEMBLY.md` §3 | open, owner D06 |
| coda text contradicts coda data | review-1 F1 (`02-phonology.yml:30` vs `:120`) | open, owner D06 |

## 2. Findings

- **F5 (low, cross-reference) — the finite-expansion gap is named by the gate but
  not yet answered.** `notable_rules[3] 's → z / V _ V'` conditions on the natural
  class `V`; the phonology gate's `A-CLASS` REVIEW is retained (exit 1), which is
  the correct behavior, but the component's own claim that "every rule's output is
  an allophone outside the phoneme inventory" does not by itself satisfy the
  gate's finite-context requirement. Owner: D06. Control: after expansion, the
  phonology gate over the packet must show the `A-CLASS` line replaced by a finite
  rule or a recorded disposition.
- No other soundness finding. F1, F3 and F4 (review-1) are cross-referenced, not
  re-filed; findings in this file are numbered in the five-review sequence
  (F5 here; F6+ in reviews 3–5).

## 3. Limits

- This review tests the **sketch's internal soundness**, not linguistic
  naturalness, not any real-language claim, and not typological truth; no
  real-world source, community, or language is compared. The sketch's own
  `to-verify` items remain open by design.
- The typed pipeline's treatment of forms (which strings enter the sound channel)
  is review-4's subject; the six `PHON-INVENTORY` FAILs here are the legacy-run
  class, not typed-run findings.
- The tree was moving during the review; digests in review-1 §1 are the contract.
