- Seat: O04 | verifier (independent verifier 1) | claim O | date 2026-10-19 | baseline `7ceff59` (HEAD)

# O04 — independent verification of the basename-couples successor draft: parse trace + 4/4 + no-drop audit

Mission (`reports/round-43/targets.json` seat `O04`): *"Independent verifier 1:
given O01's draft, trace its parse logic against the wrapped field bytes and the
policy classes by reading (no execution of run-validation); confirm it would read
4/4 and never drop a token. Report pass/fail per requirement."* Out:
`op/O04-verify.md`.

**Object under test: `reports/round-43/op/O01-tool-draft.md` — ABSENT at every cut
of this seat** (`ls reports/round-43/op/` → empty at 16:40Z, 16:51Z, 16:55Z; the
path never appeared during a 240 s poll ending 16:55Z). This fragment therefore
does three things, each labelled:

1. **It verifies the requirement surface** the draft must satisfy — claim O
   (`reports/round-43/claims.json:23-35`), the filed r39 policy, and the two
   defects (D1 block extraction, disposition leg) the claim exists to close.
2. **It files the measured trace of the wrapped field** and the **live four-class
   oracle** at HEAD, independently computed, so any later draft can be graded
   against measured numbers rather than its own claims.
3. **It verifies the only durable implementation at HEAD**
   (`tools/harness/couples-reference-extractor.py`, landed r42) against claim O
   and names the exact gaps a conformant draft must close.

**Verdict on the draft itself: `could-not-evaluate` — the draft does not exist at
this cut.** This is not a pass, and no requirement below should be read as
cleared for O01. Owner for the missing artifact: O01 (author) / integrator
(dispatch). If O01 lands after this cut, the matrix in §3 is the re-run checklist.

All commands below were read-only; no filed byte was edited, nothing was staged
under `corpus/`, no `reports/round-*/run-validation.py` was executed, no
git/network/install action was taken. My own probes live in `.scratch/o04/`
(`measure.py`, `oracle.py`, `oracle.json`).

## 1. The wrapped field: byte trace, four extraction modes, 4/4 result

The corpus has **exactly one** wrapped `couples:` field (indent-bounded census,
§2). Its live bytes at HEAD:

```
corpus/knowledge/linguistics/phonetics-phonology.md:72-77
sha256 b4f9b00384bc6840bdd1d7d7e7ae9bbb127a2fd1f5010c98d5b253df65d7776b
72  - couples: language (this file, core method); myth (divine/true names, taboo
73    naming, onomatopoeic etiologies); symbol (sound symbolism, name-shape,
74    bouba/kiki iconography); era (Neolithic bite → f/v, sound-change dating of
75    strata); costume (masks/mouthgear vs articulation, whistle & drum channels);
76    environment/anatomy design; prospective sibling files: sound-change.md, tone-
77    prosody.md, sound-symbolism.md, writing-systems.md
```

Line 78 is blank; line 79 is `## 1. Two levels: phonetics vs phonology`. The
field is bounded on both sides.

### 1.1 The field is read, not inferred — step-by-step trace

I traced the extraction the claim requires, by reading the bytes (my probe
`.scratch/o04/measure.py`, output quoted verbatim):

1. **Field capture.** `^- couples:` matches line 72; the value is
   `language (this file, core method); myth (divine/true names, taboo`.
2. **Continuation parts.** Lines 73-77 pass the indentation test
   (`^[ \t]+\S`), so the block is six parts:
   ```
   ['language (this file, core method); myth (divine/true names, taboo',
    'naming, onomatopoeic etiologies); symbol (sound symbolism, name-shape,',
    'bouba/kiki iconography); era (Neolithic bite → f/v, sound-change dating of',
    'strata); costume (masks/mouthgear vs articulation, whistle & drum channels);',
    'environment/anatomy design; prospective sibling files: sound-change.md, tone-',
    'prosody.md, sound-symbolism.md, writing-systems.md']
   ```
3. **Join.** Parts 1-5 are joined with a single space; part 5 ends in `tone-`,
   a hyphen preceded by a word character (`e`), so part 6 is concatenated
   directly and **the hyphen is kept** → `… sound-change.md, tone-prosody.md,
   sound-symbolism.md, writing-systems.md`.
4. **Tokenization.** The policy regex `[A-Za-z0-9_./{},\-]+\.md` over the joined
   value yields exactly four tokens:
   `sound-change.md`, `sound-symbolism.md`, `tone-prosody.md`,
   `writing-systems.md`.
5. **Resolution** (Tier 1 bases entry-dir → lane-root → `corpus/knowledge/`):
   `sound-symbolism.md` → **direct** (exists in `corpus/knowledge/linguistics/`);
   `writing-systems.md` → **direct**; `sound-change.md` → no file anywhere,
   slash-free, zero index hits → **unresolved**; `tone-prosody.md` → same →
   **unresolved**.
6. **Result: 4/4 named targets, 2 direct + 2 unresolved, zero dropped.**

### 1.2 The four join modes, measured (why the rule is load-bearing)

Same six parts, four joins I executed in `.scratch` (read-only):

| extraction mode | tokens on `:72-77` | meets 4/4? |
|---|---|---|
| single-line (`reports/round-19/audit/entry-audit.py:75`) | `[]` | **no** — 0/4, the N6 zeroing |
| block + space join | `['prosody.md', 'sound-change.md', 'sound-symbolism.md', 'writing-systems.md']` | **no** — mints `prosody.md`, which exists nowhere |
| block + hyphen-delete join | `['sound-change.md', 'sound-symbolism.md', 'toneprosody.md', 'writing-systems.md']` | **no** — mints `toneprosody.md` |
| block + hyphen-keeping heal | `['sound-change.md', 'sound-symbolism.md', 'tone-prosody.md', 'writing-systems.md']` | **yes** — 4/4 |

Existence check (my probe):

```
sound-change.md      False
tone-prosody.md      False
sound-symbolism.md   True
writing-systems.md   True
prosody.md           False
toneprosody.md       False
```

In-file witness for the reading: the same entry writes `tone-prosody.md` in
full, unwrapped, at `corpus/knowledge/linguistics/phonetics-phonology.md:279`
(`Natural partners: \`sound-change.md\` (diachrony → §5), \`tone-prosody.md\`,`).
So the heal recovers a name the entry itself uses; it is not an invented token.
(Still an authorial-intent reading, not a filed rule — `to-verify`, inherited
from r42 O02/O04.)

**Requirement this fixes for the draft:** the join must be specified as
*hyphen-retained*; `" ".join` and hyphen-deletion both produce four tokens and
therefore cannot be distinguished by a count-only check. A verifier must assert
the token **set**, not the total.

## 2. Live four-class oracle at HEAD `7ceff59` (independently measured)

My own classifier (` .scratch/o04/oracle.py` ), implementing the filed policy
§1-§2 exactly — brace-expanded, per-entry deduplicated, Tier 1 three bases,
slash gate before the Tier 2 index, `corpus/knowledge/*/*.md` index:

```
entries=223 refs=2730 -> direct=2556 fallback=166 ambiguous=0 unresolved=8
distinct tokens: 422
fallback distinct basenames: 50
duplicate basenames across corpus/knowledge/*/*.md: 0
```

Partition census: 223 entries, 223 `- couples:` fields, **1 wrapped field**
(`corpus/knowledge/linguistics/phonetics-phonology.md`).

The 8 unresolved rows, every row attributable (never dropped):

| entry | token | reason |
|---|---|---|
| `linguistics/language-contact.md` | `honorifics-and-register.md` | never-written "sibling knowledge files to seed" (line 7) |
| `linguistics/language-contact.md` | `naming-and-onomastics.md` | same seed line |
| `linguistics/language-contact.md` | `phonology-basics.md` | same seed line |
| `linguistics/phonetics-phonology.md` | `sound-change.md` | "prospective sibling files:" (`:76`) — N6-exposed |
| `linguistics/phonetics-phonology.md` | `tone-prosody.md` | same prospective line — N6-exposed |
| `synthesis/typed-label-routing-workflow.md` | `../linguistics/phonology-sanity.md` | X26-1 phantom, second carrier (`:16`) |
| `verification/gate-frozen-run-standard.md` | `-gate.md` | glob fragment inside `…/verification/*-gate.md` (policy §5.6) |
| `verification/label-channel-routing-verification.md` | `../linguistics/phonology-sanity.md` | X26-1 phantom, first carrier (`:14`) |

**Reconciliation with the landed r42 tool (six classes).** The r42 instrument
prints `direct=2556 fallback=166 unresolved=2 prospective=5 glob-fragment=1`
(executed, §4). Sum: `2556 + 166 + 0 + 2 + 5 + 1 = 2730`, i.e. the two extra
classes absorb exactly 6 of the policy's 8 raw-unresolved tokens (the 5
"prospective" seeds and the 1 glob fragment).

**Three presentations exist; the draft must state which it uses and reconcile.**
They are arithmetically identical over the same 2730 tokens but differ in where
the 6 non-direct/non-fallback tokens sit:

| presentation | four-class line | aux line | source |
|---|---|---|---|
| my raw oracle (glob counted as unresolved) | `2556/166/0/8` | — | §2 above |
| §5.6-strict (`prospective` folded into unresolved; glob excluded) | `2556/166/0/7` | `glob-fragment=1`; `2556+166+0+7+1=2730` | O03 §0/§6; O10 §5 (`2729 classified + 1 excluded`) |
| O06 artifact contract (native `unresolved=2`; both aux) | `policy_four.unresolved=2` | `prospective=5`, `glob-fragment=1`; `2556+166+0+2+5+1=2730` | `reports/round-43/op/O06-disposition-leg.md` §3.3, §5 |

All three are defensible **only if the census states its convention and every
identity closes**. Policy §5.6 prefers quarantining the glob fragment; claim O's
threshold names four classes. What is inadmissible is mixing conventions —
printing r42's `unresolved=2` as if it were the four-class total without the
`prospective=5` line beside it, or dropping the 5 seeds to make the four-class
sum look clean. O06's five invariants (§5 I1-I11) are the reconciliation test.

**`ambiguous` is untested live:** zero duplicate basenames exist, so a synthetic
ambiguous control is the only coverage. Claim O explicitly asks for one.

### 2.1 Boundary shapes the draft's parser must survive (measured, 223 entries)

`- couples:` fields are followed by: next header field **200**, blank then `## `
heading **20**, indented continuation **1** (the wrapped field), other **2**. The
two "other" rows are benign under an indentation-bounded rule:

- `corpus/knowledge/linguistics/conlang-methodology.md:7` — blank line 8, then
  **non-indented** body prose at line 9. A blank-line-blind parser (C14
  `fields_of` shape) would swallow the prose; an indent-bounded parser stops.
- `corpus/knowledge/myth-symbol/mineral-stone-symbolism.md:11` — blank line 12,
  then `- source:` at line 13; the next-field stop fires.

Other measured facts: **49 entries** carry braces in their `couples:` field
(e.g. `corpus/knowledge/civilizations/akan.md` — `../linguistics/{phonetics-phonology,writing-systems,…}.md`),
**no nested braces**, **no unbalanced braces**, **no entry with two `couples:`
fields**. Brace expansion one level is therefore exercised corpus-wide, not
theoretical.

## 3. Requirement matrix — what O01's draft must pass, and current status

Status vocabulary: `PASS` = I verified it from bytes I read/measured;
`FAIL` = verified absent/wrong; `could-not-evaluate` = the object is missing.

| # | Requirement (source) | Acceptance test I will apply | Status at this cut |
|---|---|---|---|
| R1 | Durable tool under `tools/harness/` (claim O `after_required`, `claims.json:28`) | path exists as a fenced draft with `#!/usr/bin/env python3`, stdlib only, read-only contract stated | **could-not-evaluate** (draft absent; target path `tools/harness/basename-couples-resolver.py` also absent, verified) |
| R2 | Parses the `- couples:` header only, single line **and** wrapped continuations (claim O; policy §1) | trace `couples_block`-equivalent; stop at next `- key:` / **blank line** / non-indented line / EOF; blank lines must not cause body-prose capture (K01 F5, r42 O02 control 4) | **could-not-evaluate**; live boundary fixtures measured in §2.1 |
| R3 | Token grammar `[A-Za-z0-9_./{},\-]+\.md`, brace-expanded one level, per-entry dedup, `:NN` anchor excluded (policy §1) | read the regex and expansion; check `calibration-registry.md:91`-shaped token; check 49 brace fields | **could-not-evaluate**; oracle applies this grammar (§2) |
| R4 | Wrapped field reads **4/4** named targets (claim O threshold, `claims.json:34`) | token **set** equals `{sound-change.md, tone-prosody.md, sound-symbolism.md, writing-systems.md}`; excludes `prosody.md`, `toneprosody.md`, `[]` | **could-not-evaluate** for the draft; the requirement is measured in §1 |
| R5 | Policy two-tier/four-class resolution: direct (3 bases) → slash gate → unique-basename fallback → ambiguous/unresolved (policy §2; §5.1, §5.4) | trace `classify`; Tier 1 order exact; slash-bearing tokens never fall back; fallback mapping is `corpus-relative path` | **could-not-evaluate**; the r42 tool passes this leg (§4) |
| R6 | Four classes reported separately, per entry **and** totals; fallback never merged into direct; zero-unresolved claim states fallback count (policy §3) | read the census/per-entry output shape; check the four totals sum to refs | **could-not-evaluate**; the r42 tool **fails** this as written — six classes, totals-only (§4 G1) |
| R7 | Disposition leg: every fallback row carries `token -> path`; every unresolved/ambiguous row a named reason; nothing dropped/guessed (claim O; r39 Ca04 D2; C12 row 2) | enumerate all 166 fallback rows and every unresolved row (7 policy + 1 glob, or 8 raw) from the output; each has mapping/reason | **could-not-evaluate**; the r42 tool **fails** this in `--census` (§4 G4) |
| R8 | `--selftest` green incl. wrapped-field positive **and** synthetic phantom **and** synthetic ambiguous negatives (claim O threshold) | read the selftest controls; ambiguous fixture must produce `ambiguous` from two injected index hits, not a hard-coded label; `classify` must accept `index=` (O02 §3) | **could-not-evaluate**; the r42 tool has wrapped positive + phantom but **no ambiguous control** and a non-injectable index (§4 G3) |
| R9 | Zero tokens silently dropped; totals arithmetic closes (claim O threshold) | sum of class counts == refs; per-entry token count == classified count; wrapped entry contributes exactly 4; a quarantined glob class must reconcile, not vanish | **could-not-evaluate**; oracle closes both ways: `2556+166+0+8 = 2730` and `2556+166+0+7+1 = 2730` |
| R10 | No writes outside `tools/harness/` + `reports/round-43/`; no corpus staging; no filed-byte edits (shared rules) | read the tool's write surface; `git status` after any run | **could-not-evaluate**; r42 tool is read-only (opens for read only) |
| R11 | Corrected census filed at `reports/round-43/calib/` (claim O `after_required`) | a calib artifact exists with four-class totals + every fallback mapping, at the one name the draft's `--census` writes | **could-not-evaluate**; `reports/round-43/calib/` has no census yet, and O06 vs O10 disagree on the filename (§6) |

## 4. The only durable implementation at HEAD, audited against claim O

`tools/harness/couples-reference-extractor.py` (r42, blob
`1ded489bbb2bb90b3ad883ec0cd052822d870225`, sha256
`d8d23a265d12d290de69a6eb50454273af4ca699986812c6e203a030f4679cf1`, 332 lines)
is the predecessor claim O's successor must supersede or extend. I ran it
read-only:

```
$ python3 -B tools/harness/couples-reference-extractor.py --selftest
PASS wrapped positive 4/4 tokens ['sound-change.md', 'sound-symbolism.md', 'tone-prosody.md', 'writing-systems.md']
PASS wrapped positive heals soft wrap
PASS unwrapped regression
PASS over-capture trap (prose excluded) ['sound-symbolism.md']
PASS phantom negative: absent wrapped targets are visible, not zeroed {'sound-change.md': 'prospective', 'sound-symbolism.md': 'fallback', 'tone-prosody.md': 'prospective', 'writing-systems.md': 'fallback'}
PASS N6 regression guard: single-line capture still yields 0 tokens
PASS N6 regression guard: block read yields 4 tokens ['sound-change.md', 'sound-symbolism.md', 'tone-prosody.md', 'writing-systems.md']
PASS glob fragment classified
exit=0

$ python3 -B tools/harness/couples-reference-extractor.py --census
entries=223 refs=2730 -> direct=2556 fallback=166 unresolved=2 prospective=5 glob-fragment=1
  wrapped fields: 1 ['corpus/knowledge/linguistics/phonetics-phonology.md']
  unresolved distinct=1: ../linguistics/phonology-sanity.md(x2)
  misaligned: none
exit=0
```

What it proves (PASS legs): block extraction is correct (`couples_block:50-73`),
the soft-wrap heal keeps the hyphen (`join_parts:76-93`), the four-token set is
right, Tier 1/Tier 2 classification matches the policy (`classify:134-150`), the
wrapped field is not zeroed, and the corpus census reconciles with my
independent oracle to the token (§2).

**Gaps a conformant r43 draft must close** (these are the *measured* reasons a
new instrument is claimed, not restatements):

- **G1 — six classes, not the policy's four.** `census:186-211` totals
  `prospective` and `glob-fragment` as separate classes. Claim O requires the
  four policy classes with a disposition leg; the successor must either fold
  those into `unresolved` with named reasons, or state explicitly that the
  four-class report plus two non-finding exclusions is the mapping (policy §5.6
  permits the latter for glob fragments, not for prospective seeds).
- **G2 — no census artifact.** `main:298-330` prints to stdout only; nothing is
  written under `reports/round-43/calib/`. Claim O's `after_required` names a
  filed census.
- **G3 — no ambiguous control.** `selftest:242-296` has a wrapped positive, an
  unwrapped regression, an over-capture trap, a prospective-phantom negative,
  two N6 guards and a glob-fragment check — **no synthetic ambiguous** (two
  index hits). Live ambiguous = 0 (§2), so this class has zero coverage.
- **G4 — `--census` has no per-row disposition leg.** It aggregates unresolved
  by distinct token (`:309-315`) and does not list the 166 fallback mappings or
  a reason per unresolved row. The per-entry mode (`:318-327`) prints
  `class` + `mapping` per token, so the data exists; the *filed census* shape
  the claim requires does not.
- **G5 — totals mislabel risk.** Printing `unresolved=2` beside
  `prospective=5 glob-fragment=1` is arithmetically consistent with the policy's
  8 but is **not** a four-class census. Any r43 draft that copies this line and
  labels it "the policy's four classes" fails R6 even though the arithmetic
  closes.
- **G6 — blank lines are skipped, not terminating (`couples_block:64-65`).**
  `if not following.strip(): continue` keeps scanning past a blank line, so an
  **indented prose** line after a blank would be swallowed into the field. The
  live corpus has **0** such cases (my boundary census: `blank_then_heading=20`,
  `blank-then-indented=0`), so the 2730 figure is correct today — but the
  selftest has no discriminating fixture (its `OVER_CAPTURE_TRAP:231-239` uses
  non-indented prose, which `INDENT_RE` stops), so the rule is latent-broken.
  Independently found by K01 (`reports/round-43/scout/K01-resolver-scout.md`
  §5 F5, with an executed synthetic over-capture); r42's own controls required
  termination (`reports/round-42/op/O02-controls.md:27,90-105`;
  `reports/round-42/op/O05-traps.md:190-196`). A conformant r43 parser must
  `break` on a blank line and add that fixture. **The defect is propagating into
  the r43 contract:** O06's artifact skeleton still specifies
  `"continuation_rule": "…; blank lines skipped"`
  (`reports/round-43/op/O06-disposition-leg.md:364`). O01 must not implement that
  sentence literally; the integrator should correct O06's `extraction` object to
  "stop at a blank line" before filing.
- **Interface requirement for the synthetic controls (O02):**
  `classify(ref, entry_dir, index=None)` must accept an injected index. The r42
  signature's third position is `prospective=False` (`classify:134`), so the
  ambiguous/fallback/phantom synthetic cases cannot run without one
  (`reports/round-43/op/O02-controls.md:304-316`).

## 5. No-drop audit — the test the draft must survive

For each of the 223 entries, the draft's token set `T(entry)` must satisfy:

1. every token in `T` appears in exactly one of `direct | fallback | ambiguous |
   unresolved`;
2. `sum(class counts) == sum(|T|)` per entry and corpus-wide (oracle: **2730**);
3. the wrapped entry contributes exactly **4** tokens, 2 direct + 2 unresolved;
4. no token is synthesized (`prosody.md`, `toneprosody.md` absent) and no token
   is lost (`sound-change.md`, `tone-prosody.md` present as unresolved);
5. brace-bearing entries (49) expand one level and dedupe per entry; no
   nested-brace case exists to confound the rule;
6. the two boundary entries in §2.1 do not gain body-prose tokens
   (`conlang-methodology.md` must not acquire anything from its line-9 prose),
   and a synthetic blank-line + **indented** prose fixture yields no token
   (K01 F5 / r42 O02 control 4).

The r42 tool satisfies 1-5 (I reconciled its six-class output to the oracle)
and satisfies 6 on the live corpus (0 blank-then-indented fields today), but its
parser **fails** the blank-line rule in general (`couples_block:64-65` skips
blanks; its selftest fixture is non-indented prose, so it cannot catch this).
A draft that meets all six, closes G1-G6, and exposes
`classify(..., index=None)` satisfies claim O's `after_required`.

## 6. Verdict and owed

**Verdict: `could-not-evaluate` for O01's draft — it is absent at this cut.**
Claim O's threshold ("selftest green …, wrapped field reads 4/4, four-class
census filed with every fallback mapping listed, zero tokens silently dropped;
two independent verifiers") cannot be certified by verifier 1 without the
object. The threshold is **not** met today: no `tools/harness/basename-couples-resolver.py`,
no `reports/round-43/calib/` census artifact, and the durable r42 instrument
fails R6/R7/R8 as written (§4).

**Independently verified and durable as evidence:**

- the wrapped field's six physical lines and sha256 (`b4f9b003…`);
- the 4/4 token set and the three wrong join modes (§1.2);
- the live four-class oracle `2730 = 2556 + 166 + 0 + 8` with all 8 unresolved
  rows attributed (§2);
- the r42 instrument's green selftest and its exact six gaps (§4).

**Same-wave agreement (read after my measurements, not used to derive them):**
K01 independently measured the same 223/2730/2556/166/0/8 oracle, the same
wrapped-field identity, and adds F5 (blank-line skip, folded here as G6) —
`reports/round-43/scout/K01-resolver-scout.md` §2, §5, §7. O07 names the same
canonical path and the same "do not edit r42" rule
(`reports/round-43/op/O07-durability.md` §0-§4). O12 independently reproduces the
0-token single-line read and the 4-token correct read and files the same
count-vs-identity trap (`reports/round-43/op/O12-negative-proof.md` §5, O12-F1).
O02's control draft is the source of the index-injectable `classify` requirement
and the S1f "2 direct + 2 unresolved" assertion
(`reports/round-43/op/O02-controls.md` §1, §3).

**Owed:**

- **O01 / integrator:** land `op/O01-tool-draft.md`; then verifier 1 must re-run
  §3 against its actual bytes. A draft that reports the r42 six-class totals as
  "four classes", or whose join is space/hyphen-delete, fails R4/R6 on the
  evidence above.
- **Integrator:** when the successor instrument lands, require the filed census
  to carry its denominator (223 entries, or the closed-tree count) and commit
  (`7ceff59`) — the r39 `2504` figure is a 212-entry measurement and must not be
  used as a subtraction baseline (r42 O12-F1; the denominator moved).
- **Integrator — resolve two contract conflicts before filing** (both are
  cross-seat, not O01 defects):
  1. **Filename.** O06 §3.1 declares
     `reports/round-43/calib/couples-census-r43.json` binding and says O10 must
     use it (`O06-disposition-leg.md:90-99`); O10 §1 files
     `basename-couples-census.json` + `.md` (`O10-census-artifact.md:60-61`).
     One name must win, and the draft's `--census` default must write it.
  2. **Continuation rule.** O06's artifact skeleton says "blank lines skipped"
     (`O06-disposition-leg.md:364`); the correct rule (K01 F5, r42 O02 control 4,
     r42 O05 F15) is "stop at a blank line". This one changes tokens on any
     future field with blank-then-indented prose; it must not ship as written.
- **to-verify:** `tone-prosody.md` as authorial intent (in-file witness at
  `:279`, no filed rule names the token); inherited, not re-litigated here.
- **to-verify:** whether the r43 draft folds `prospective` into `unresolved`
  with a reason or reports the policy's four classes plus a non-finding
  exclusion; claim O's wording says four classes, policy §5.6 permits exclusion
  only for glob fragments.

## Citations

- Assignment and shared rules: `reports/round-43/targets.json:20` (seat O04),
  `:4-10` (shared rules); claim O `reports/round-43/claims.json:23-35`
  (`after_required` `:28`, counting commands `:29-33`, thresholds `:34`).
- Policy: `reports/round-39/calib/basename-couples-policy.md` (107 lines, sha256
  `105dfff6c667ad5b77c28be8d6070ec243b5e19029fb60ae83d6028aa2e941cf`):
  §1 `:14-25`, §2 `:27-48`, §3 `:50-58`, §4 `:60-69`, §5 `:71-102`, §5.6
  `:97-102`, §6 opening `:104-107` (the landed file is a truncated prefix;
  arithmetic lives in `reports/round-39/calib/Ca03-basename-policy.md:35,268,355`
  and `reports/round-39/calib/Ca04-verify.md:29`).
- Defect rows: `reports/round-40/op/defect-queue-v2.json` rows
  `N6-couples-extractor-wrapped-field`, `r39-basename-successor-instrument`
  (owner "successor-instrument author … r43/r44"), `r39-ic05-resolver-durability`;
  origin `reports/round-39/calib/Ca04-verify.md:78-105` (D1) and `:94-106` (D2);
  second read `reports/round-39/review/R01-review.md:262-274` (R01-7).
- Wrapped field: `corpus/knowledge/linguistics/phonetics-phonology.md:72-77`
  (sha256 `b4f9b00384bc6840bdd1d7d7e7ae9bbb127a2fd1f5010c98d5b253df65d7776b`),
  in-file witness `:279`; boundary entries
  `corpus/knowledge/linguistics/conlang-methodology.md:7-9`,
  `corpus/knowledge/myth-symbol/mineral-stone-symbolism.md:11-13`; brace sample
  `corpus/knowledge/civilizations/akan.md:7`.
- Filed single-line host: `reports/round-19/audit/entry-audit.py:75` (sha256
  `e7992c325a479aa7415c42722a034a95a9ea342a58367ead9cd2636a5a62830c`);
  second copy `reports/round-27/audit/entry-audit.py:275`.
- Durable r42 predecessor: `tools/harness/couples-reference-extractor.py`
  (blob `1ded489b…`, sha256 `d8d23a26…`): `couples_block:50-73`,
  `join_parts:76-93`, `expand_braces:100-110`, `field_refs:112-121`,
  `basename_index:124-132`, `classify:134-150`, `resolve_entry:153-184`,
  `census:186-211`, `selftest:242-296`, `main:298-330`.
- Target path absence: `ls tools/harness/` → `basename-couples-resolver.py`
  absent (this seat, 2026-10-19); `find reports/round-43 -type f` → only
  `claims.json`, `targets.json`, `telemetry/dispatch-declared.json`.
- Command outputs (this seat, 2026-10-19, lane root, HEAD
  `7ceff59`, `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, all
  read-only): (a) `.scratch/o04/measure.py` → single-line `[]`; block parts (6)
  quoted; four joins as tabulated; existence booleans; `entries=223
  couples_fields=223 wrapped=1`; duplicate basenames 0. (b) `.scratch/o04/oracle.py`
  → `entries=223 refs=2730 -> direct=2556 fallback=166 ambiguous=0 unresolved=8`,
  422 distinct tokens, 50 distinct fallback basenames, 8 unresolved rows printed.
  (c) r42 instrument `--selftest` → 8 PASS, exit 0; `--census` → the six-class
  line quoted in §4; per-entry mode on the wrapped entry → `wrapped=True
  tokens=4` with `sound-change.md prospective`, `sound-symbolism.md direct`,
  `tone-prosody.md prospective`, `writing-systems.md direct`. (d) field-follow
  shapes `next_field=200 blank_then_heading=20 indented_cont=1 other=2`;
  49 brace-bearing fields, 0 nested, 0 unbalanced. (e) `ls reports/round-43/op/`
  empty throughout. No `run-validation.py` executed; no filed byte edited; no
  git/network/install.
