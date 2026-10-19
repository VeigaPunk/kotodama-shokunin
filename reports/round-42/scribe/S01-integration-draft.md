- Seat: S01 | scribe | cross | date 2026-10-19 | baseline ac47c78

# S01 — round-42 integration dossier: fleet-report material + validation-leg spec

**Mission (binding, `reports/round-42/targets.json`, seat `S01`):** *"Integration dossier:
fleet-report material + validation-leg spec."* Out path: this file only.

**Status: DRAFT — report material and a leg spec, not a fleet report, not a receipt, not an
acceptance verdict.** This seat wrote **zero** bytes outside this file (no corpus, no tool, no
filed-round byte, no round-42 peer fragment). No `reports/round-*/run-validation.py` was executed
anywhere, in-tree or in a copy (absolute rule, `targets.json` shared_rules). Every number below was
measured read-only by this seat at `ac47c78` under
`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1` unless attributed to a sibling fragment
(§8 folds each). Nothing here asserts promotion, canon, clearance or closure; those tokens appear
only as negations, routed references, or quoted scanner patterns.

**Seat context.** Single batched 32-seat `devin/deepseek-v4-1-flash-high` dispatch
(`reports/round-42/claims.json:5-8`; `REGIMEN.md:20` row 10 — 32 requested is **inside** the
declared 32–64 band, no deviation). Written mid-wave and corrected at finalization: the round-42
tree grew from **5 files** at this seat's first census (2026-10-19T15:59:35Z —
`claims.json`, `targets.json`, `telemetry/dispatch-declared.json`, `op/O09-scribe.md`,
`op/O10-gap-fill.md`) to **24 files** by the finalization census. Both censuses are this seat's
`find reports/round-42 -type f | sort` output; §8 folds the fragments that arrived between them.
The integrator recomputes the census at close; never trust either count.

---

## §0 — The headline the integrator must read first

1. **Claim O's census arithmetic is confirmed, and the wave's own predicted census is already on
   disk.** `op/O10-gap-fill.md` (landed) states `entries=220 tokens=2611 direct=2437 fallback=166
   ambiguous=0 unresolved=8` under its rule D. This seat independently reproduced that exact
   quadruple (§2.3) — and the r39 policy's own `2504 = 2335 + 163 + 0 + 6` (§2.2). Both reproduce.
2. **The claims' "2 phantom attributions in the census" is a mis-description that must not enter
   LOG.md as written.** The r39 census's 6 unresolved tokens contain **no phantom** — all 6 are real
   dangling references, already attributed by `Ca04-verify.md`. The two tokens the fixed extractor
   adds (`sound-change.md`, `tone-prosody.md`) are *newly surfaced* references from the one wrapped
   field, not pre-existing phantom attributions (§2.2, §2.4). The corrected baseline is
   `2508 = 2337 + 163 + 0 + 8`, i.e. **the corrected census is not "the r39 arithmetic minus the
   phantoms" — it is the r39 arithmetic plus 2 direct and plus 2 unresolved** (claims.json:15).
3. **The rejoin rule is the whole claim, and two of the four plausible rules produce a false
   green.** Block extraction joined with a space (rule C, the obvious reading) yields 4 tokens for
   the wrapped field — satisfying the claim's "4/4 targets" wording — but one of them is the
   phantom `prosody.md`. Only rule D (a hyphen-terminated line rejoined with **no** separator)
   yields the 4 intended tokens (§2.4). O02's synthetic phantom negative must mirror C, not D.
4. **A new filed-byte defect, found this seat and not in the queue:** the landed
   `reports/round-39/calib/basename-couples-policy.md` is **107 lines and truncated**. Its §6
   heading at `:104` is followed by the recipe's three intro lines and then EOF; the fenced
   `python` recipe body, §7 Adoption evidence, `## Owed` and `## Citations` are all absent (§3).
   It has been 107 lines at every commit since `fd55e1f` (`git show <c>:… | wc -l` = 107 for
   `fd55e1f`, `456674d`, `ac47c78`, `HEAD`). The r39 acceptance leg only greps for the literal
   string `fallback` in the file (`reports/round-39/run-validation.py:117-118`), so it passed and
   the round was admitted. **Fix is a filed-round byte change and therefore integrator/operator-
   owned, not a seat action.**
5. **The r19 gate still fails the phonetics entry, for a reason adjacent to — but not caused by —
   the wrapped field.** `python3 -B reports/round-19/audit/entry-audit.py
   corpus/knowledge/linguistics/phonetics-phonology.md` → `src=15/15 couples=0 unresolved=[] …
   TOTAL 0/1`, `gap=False`. The `couples=0` is the wrapped-field defect; the bar failure is
   `gap=False` (§2.5). A fix that reports `couples=4` will **not** flip this gate green, and no
   leg may claim it will.
6. **The claim's own "4/4 targets" threshold is satisfiable by a wrong parser, and the queue's
   literal terminator over-reads.** X00's connector found a fourth variant — "block extraction
   through the next header field" taken literally, ignoring blank lines — and measured it at
   `2615` refs / 3 over-reading entries (`cross/X00-connector.md:80-140`). This seat re-measured
   the same shape and got **`2653` refs / 5 over-reading entries**
   (`conlang-methodology.md`, `language-shift-obsolescence-revival.md`, `numerals-and-measures.md`,
   `phonetics-phonology.md`, `sound-symbolism.md`), so the figure is **implementation-sensitive**
   and must not be quoted as one number. The stable finding is the *class*: the terminator must be
   **blank line OR next header field**, not the next field alone (§7 O1). Variants B/C/D all read
   "4 tokens" for the wrapped field, so an arity-only assertion is a false green (§0.3).
7. **Two write-time blockers for the integrator:** `reports/round-42/op/runner-census.json`
   (referenced by the r41 precedent) does not apply here; but round 42's own runner,
   `validation.json`, `telemetry/observed-dispatch.json`, the closing snapshot, the `.ufo` fleet
   report, the `MANIFEST.json rounds[]` row, the `SCORECARD.md` row and the `LOG.md` entry are all
   absent at this cut (§6.4). The r41 leg-6 boundary stands unchanged: the round command
   `python3 reports/round-42/run-validation.py` is **close-time and integrator-only, in an
   isolated copy**.
8. **Two claim-C slugs collide on one topic.** C01 (`cov/C01-entry-1.md:3`) proposes
   `myth-symbol/purity-pollution-codes.md` and C02 (`cov/C02-entry-2.md`) proposes
   `myth-symbol/purity-pollution-systems.md` — the same purity/pollution system, drafted twice
   under the missing-dependency rule because K02's scout had not landed. K02 has since landed and
   **confirms** the topic as its gap 4 (`scout/K02-myth-gaps.md:310-332`). So claim C has one real
   topic and two competing drafts for it, plus K02's other three gaps
   (`mineral-stone-symbolism.md`, `dream-vision-trance.md`, `pilgrimage-sacred-geography.md`,
   K02 `:212,:259,:303`) with no author. The integrator must pick one slug and re-slot the other
   draft, or the README gains a duplicate-topic row (§4, §7 C1).

---

## §1 — Window, state pins, and what "first-hand" means here

| pin | value | command |
|---|---|---|
| lane HEAD / declared baseline | `ac47c7861b0b2cdb8e3c2f985c2220406d3ba0b4` | `git rev-parse HEAD`; `git rev-parse ac47c78` |
| working tree | only `?? reports/round-42/` untracked; no tracked modification | `git status --porcelain` |
| round-42 tree | 5 files (3 instruments + `op/O09-scribe.md` + `op/O10-gap-fill.md`) | `find reports/round-42 -type f \| sort` |
| corpus total | 220 (`linguistics 25`, `myth-symbol 23`, `culture-material 25`, `synthesis 29`, `verification 24`, `civilizations 94`) | `ls corpus/knowledge/<part>/*.md \| wc -l` |
| corpus README | revision 2.3, totals line 220, footer vector `25/23/25/29/24/94` | `grep -n '^revision:' corpus/README.md`; `:532`; `:534-536` |
| sweep baseline | exit 0, `rows 220 files 220`, `footer_ok True` | `python3 -B reports/round-28/readme/sweep.py` |
| sweep instrument sha | `9b2ccac0046831fdaf48863ccd0ff6ca0fa390d044746c876e83a71c06f0cdd3`; selftest 12/12 | `sha256sum reports/round-28/readme/sweep.py`; `--selftest` |
| round-42 declared digests | `claims.json` `513ae210…`, `targets.json` `6db0a9eb…` | `sha256sum`; `telemetry/dispatch-declared.json` `durable_sources` |

"First-hand" means: opened or executed by this seat at `ac47c78` in the window above. Sibling
figures are attributed in §8 and were **not** re-derived; where a sibling figure and this seat's
measurement disagree, both are printed (§2.4 note on O10's rule-B token list).

---

## §2 — Claim O (operability): the corrected census, measured three ways

### 2.1 The wrapped field

`corpus/knowledge/linguistics/phonetics-phonology.md:72-77` is the corpus's **only** wrapped
`couples:` field. Corpus-wide scan of all 220 `corpus/knowledge/*/*.md`: fields with at least one
indented non-bullet continuation line = **1** (this one, 5 continuation lines, `:73-77`). This
reproduces r39 `Ca04-verify.md` D1 and round-42 `op/O10-gap-fill.md` §3 independently.

Raw field bytes (this seat's block read, `:72-77`):

```
- couples: language (this file, core method); myth (divine/true names, taboo
  naming, onomatopoeic etiologies); symbol (sound symbolism, name-shape,
  bouba/kiki iconography); era (Neolithic bite → f/v, sound-change dating of
  strata); costume (masks/mouthgear vs articulation, whistle & drum channels);
  environment/anatomy design; prospective sibling files: sound-change.md, tone-
  prosody.md, sound-symbolism.md, writing-systems.md
```

The line break falls **inside** a filename: `:76` ends `…sound-change.md, tone-` and `:77` begins
`  prosody.md, …`. Intended token: `tone-prosody.md`.

### 2.2 The r39 census reproduces exactly (rule A)

Re-running the r39 policy's own two-tier logic (§1 token grammar, §2 four-class resolution,
slash-free fallback gate) over the **212-entry r39 tree** (the live 220 minus the eight entries
that landed in r39/r40):

```
212 [A single-line] refs=2504 -> direct=2335 fallback=163 ambiguous=0 unresolved=6
  distinct=5: -gate.md(x1), ../linguistics/phonology-sanity.md(x2),
              honorifics-and-register.md(x1), naming-and-onomastics.md(x1),
              phonology-basics.md(x1)
```

This is **byte-equal to the r39 policy's filed Part 2** (`Ca03-basename-policy.md:268-269`:
`entries=212 refs=2504 -> direct=2335 fallback=163 ambiguous=0 unresolved=6`, 5 distinct). The
five distinct names match `Ca03-basename-policy.md:270-277` attribution for attribution, including
`-gate.md` x1 = the §5.6 glob fragment (`gate-frozen-run-standard.md:15`) and
`../linguistics/phonology-sanity.md` x2 = the r19 X26-1 phantom. **No phantom attribution exists
in this census.** The claims.json:13 "2 phantom attributions" therefore does not describe the r39
census's 6-token set.

### 2.3 The corrected census (rule D) — and the live 220-entry reading

Four rejoin rules, measured on the same 220 entries:

| rule | mechanism | refs | direct | fallback | ambiguous | unresolved | wrapped-field tokens |
|---|---|---|---|---|---|---|---|
| **A** | single physical line (`reports/round-19/audit/entry-audit.py:75`, `reports/round-27/audit/entry-audit.py:275`) | 2607 | 2435 | 166 | 0 | 6 | **none** — 0 tokens captured |
| **B** | block, lines joined with `\n` (C14 `fields_of`, `C14-audit-6-10.md:225-236`) | 2611 | 2437 | 166 | 0 | 8 | 4, incl. phantom `prosody.md` |
| **C** | block, lines joined with a single space (`" ".join`, `tools/gates/provenance-audit.py:259`) | 2611 | 2437 | 166 | 0 | 8 | 4, incl. phantom `prosody.md` |
| **D** | block, hyphen-terminated line rejoined with **no** separator | 2611 | 2437 | 166 | 0 | 8 | **the correct 4**, incl. `tone-prosody.md` |

Rule D is the correct one, confirmed by the entry's own body: `phonetics-phonology.md:279-280`
reads `- Natural partners: \`sound-change.md\` (diachrony → §5), \`tone-prosody.md\`,
\`sound-symbolism.md\` (§8), \`writing-systems.md\` (orthography mismatch).` — the intended token
spelled by the entry's own bytes, not by inference. No file named `prosody.md` exists anywhere in
the repo. B and C differ from D only in the token spelling, **not in any count** — so a validation
leg that checks the four-class arithmetic alone is a **false green**: B, C and D all report
`2611 / 2437 / 166 / 0 / 8`. The leg must assert the *token identity* `tone-prosody.md` (and the
absence of `prosody.md`). **A fifth variant exists and over-reads** — see §2.6.

**Corrected baseline arithmetic (220 entries, rule D):**

```
2607 -> 2611   (+4 refs from the wrapped field)
2435 -> 2437   (+2 direct: sound-symbolism.md, writing-systems.md — both exist in linguistics/)
   166 -> 166  (fallback unchanged; the wrapped field contributes no fallback token)
     6 -> 8    (+2 unresolved: sound-change.md, tone-prosody.md — both phantoms/prospective)
```

And the same transformation over the **212-entry r39 tree** (for a like-for-like successor note
against the filed policy):

```
A:  2504 = 2335 + 163 + 0 + 6   (r39 filed, reproduced)
B/C:2508 = 2337 + 163 + 0 + 8   (phantom prosody.md)
D:  2508 = 2337 + 163 + 0 + 8   (tone-prosody.md)
```

**So the successor note's corrected r39 arithmetic is `2508 = 2337 + 163 + 0 + 8`** — not
"2504 minus phantoms". Both added unresolved tokens are *prospective* declarations (the line reads
"prospective sibling files"), not dangling references; §7 leg O3 carries the disposition.

### 2.4 Agreement and disagreement with the wave

`op/O10-gap-fill.md` §4 (landed) states `entries=220 tokens=2611 direct=2437 fallback=166
ambiguous=0 unresolved=8` under its rule D — **identical to this seat's rule-D row**. Its §1 rule
table matches A/B/C/D semantics and its rule-D token set matches this seat's. Its §2 identifies the
live host as `tools/gates/provenance-audit.py:244-260` with the space-join at `:259`; this seat
opened `:244-260` and confirms the code shape verbatim (`parts.append(following.strip())` at
`:256`, `return True, " ".join(part for part in parts if part)` at `:259`, `FIELD_RE` at `:76`
matching only `topic|sources|couples`, `INDENT_RE` at `:77` = `^[ \t]+\S`). Its §3 census (1
`couples` soft-wrap, 5 lines) matches this seat's. **One presentation difference to reconcile at
integration:** O10's §1 table labels rule B as producing 4 tokens
(`prosody.md`, `sound-change.md`, `sound-symbolism.md`, `writing-systems.md`); this seat's raw
block read of the same bytes also returns those four — consistent. No substantive disagreement
found between this seat and O10 on claim O.

`op/O09-scribe.md` (landed) reports the pre-landing snapshot and names the same single-line
extractor hosts; nothing in it contradicts §2.

### 2.6 The terminator is load-bearing: a fifth variant over-reads (measured twice, two answers)

The queue's literal wording for the fix is "block extraction **through the next header field**"
(`defect-queue-v2.json`, row `N6-couples-extractor-wrapped-field`). Taken literally — accumulate
continuations until the next `- <field>:` line, ignoring blank lines — that shape absorbs body
prose for any entry whose `couples:` line is the *last* header field. X00's connector measured
**3 such entries and `2615` corpus refs** (`cross/X00-connector.md:80-140`); this seat re-measured
the same shape and got **5 entries and `2653` refs**:

| entry | refs, correct terminator | refs, next-field-only terminator |
|---|---|---|
| `linguistics/conlang-methodology.md` | 19 | 27 |
| `linguistics/language-shift-obsolescence-revival.md` | 0 | 10 |
| `linguistics/numerals-and-measures.md` | 17 | 33 |
| `linguistics/phonetics-phonology.md` | 4 | 5 |
| `linguistics/sound-symbolism.md` | 17 | 24 |

The two seats disagree on the *magnitude* (3/2615 vs 5/2653) because "the next header field" admits
more than one regex. **That is the finding, and it must be filed as such:** the terminator is not a
detail — it is worth ±38 refs on this corpus and it is not pinned by the queue's wording. The
correct terminator, which both seats agree on semantically, is **blank line OR next header field**,
and it yields `2611 / 2437 / 166 / 0 / 8`. Do not let the round record a single over-read number as
if it were a measurement; record the class and the chosen terminator (§7 O1).

### 2.5 The r19 gate consequence (measure, do not over-claim)

```
$ python3 -B reports/round-19/audit/entry-audit.py corpus/knowledge/linguistics/phonetics-phonology.md
FAIL corpus/knowledge/linguistics/phonetics-phonology.md src=15/15 couples=0 unresolved=[] gap=False dec=True
TOTAL 0/1 clear the bar
```

Two distinct causes: `couples=0` (the wrapped field, claim O's target) and `gap=False` (the r19
`GAP_RE`, `reports/round-19/audit/entry-audit.py:27`, does not match this entry's `- gap filled:`
text). Claim O's fix addresses only the first. **No leg may assert the r19 gate goes green after
the fix.**

The `couples=0` reading is explained by the single-line extractor and nothing else. A body-scan
alternative is ruled out by measurement: the entry's **body** does name `.md` tokens — `:279-280`
reads `- Natural partners: \`sound-change.md\` (diachrony → §5), \`tone-prosody.md\`, \`sound-symbolism.md\`
(§8), \`writing-systems.md\` (orthography mismatch).` — so a body scan would return 4 tokens, not 0.
Note what that body line independently establishes: it spells the intended token **`tone-prosody.md`**,
confirming rule D over rule B/C by the entry's own bytes rather than by inference (§2.3).

---

## §3 — New finding: the landed r39 policy file is truncated

`reports/round-39/calib/basename-couples-policy.md` — `wc -l` = **107**; sha256
`105dfff6c667ad5b77c28be8d6070ec243b5e19029fb60ae83d6028aa2e941cf`. Its `## ` headings are §1–§6
only (`:14, :27, :50, :60, :71, :104`). Lines `:104-107` are the §6 heading plus the recipe's
three-line intro, then **EOF**:

```
104  ## 6. Verification recipe (read-only; reproduces the filed evidence)
105
106  Run from the lane root; no writes, no runner invocation
107  (`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`):
```

Absent versus the authoring draft `reports/round-39/calib/Ca03-basename-policy.md` (359 lines,
sha256 `125ede77e3f50e3c58af61fb2fad246c8378b4dcfc4ee5d1749da8dd53a17850`): the fenced `python`
recipe (draft `:149-258`), the filed-run summary (draft `:260-290`), `## 7. Adoption evidence`
(draft `:292-303`), `## Owed` (draft `:306`) and `## Citations` (draft `:326`). The landed `:107`
is byte-identical to the draft's `:147`, and the draft's `:148` is the fence-opening ` ```python ` —
so the mechanism is consistent with the fence-opening line and everything after it being dropped
at apply time. `git show <c>:… | wc -l` = 107 for `fd55e1f` (the r39 admission commit), `456674d`,
`ac47c78` and `HEAD`: the truncation is original, not a later regression.

Why it passed: the r39 acceptance leg only requires the literal marker `fallback` in the file
(`reports/round-39/run-validation.py:117-120`), which survives in §2's prose. The r39
`validation.json` records `Ca1-Ca3` green and `acceptance_checks_passed: true`. The r39 runner's
`Ca3` leg instead greps `334` from `calib/Ca04-verify.md` (`run-validation.py:129-130`), not from
the policy — so the missing recipe was never read by any leg.

**Consequences the integrator must carry:**
- The policy's §6 recipe is the reproduction mechanism for both the 2504 and the corrected 2508
  arithmetic. It is not in the filed file; the only copy is the r39 authoring draft
  (`Ca03-basename-policy.md:149-258`), itself a filed round-39 byte. **The consequence is
  upstream, not numerical:** §6's `REFERENCE CODE` block — not its filed output — is what a
  successor instrument implements, so a successor author reading only the landed file would
  reconstruct the two-tier logic from prose (§1–§2 survive intact) and lose the exact glob index,
  the slash-free gate and the group-alignment join that §6 encodes. §7's adoption evidence
  (`Ca03-basename-policy.md:292-303`, six filing pointers) is likewise lost. The three landed
  prose sections the r39 gates actually read are unaffected.
- `reports/round-40/op/defect-queue-v2.json` row `basename-couples-policy` is `fixed-with-evidence`
  ("policy documented and verified"). The *documentation* leg is incomplete as filed. This is a
  **new row or an amendment**, not a re-class the seats may make.
- Fixing it edits a filed round-39 byte → **operator/integrator-owned** (the round's non-goal "no
  filed byte rewrites" and `targets.json` shared_rules both bar a seat). Route it, do not absorb.
- The `N6-couples-extractor-wrapped-field` and `r39-basename-successor-instrument` rows
  (`defect-queue-v2.json`) should name this alongside the D1/D2 fix route.

---

## §4 — Claim C (coverage): the delta's executable bar

Baseline measured this seat (`ac47c78`): `myth-symbol 23`, total `220`, README rev **2.3**,
totals line `220` (`:532`), footer `(total 220 files; directory totals 25/23/25/29/24/94)`
(`:534-536`), sweep exit 0.

**Vector order is fixed by the README's own section order** (`sweep.py:50-57`, confirmed by the
footer's `order` key in this seat's sweep output):
`linguistics, myth-symbol, culture-material, synthesis, verification, civilizations`.

**The C06 mission's vector bytes are arithmetically wrong; use `25/27/25/29/24/94`.** The mission
(`reports/round-42/targets.json`, seat `C06`) specifies "vector `25/23/27/25/24/94`". That vector
sums to **218**, not 224, and it moves the wrong two slots: it leaves `myth-symbol` at 23 and moves
`culture-material` 25 → 27 and `synthesis` 29 → 25. Only `myth-symbol` 23 → 27 changes this round.
Independently found by `review/R02-review.md` Trap D (§12) before this seat read it; this seat
confirms the arithmetic (`sum([25,23,27,25,24,94]) = 218`; `sum([25,27,25,29,24,94]) = 224`). A
README built to the mission vector is **sweep-red** because the footer leg compares the six totals
positionally (`sweep.py:179-190`). Correct target state: `## myth-symbol/ (27)`, totals line `224`,
footer `(total 224 files; directory totals 25/27/25/29/24/94)`, `revision: 2.4` block prepended
above the current `:5` rev-2.3 block.

**Index-row contract (measured, not assumed).** An index row is ``- `<file>.md` — <text>`` where
`<text>` is the entry's own `- topic:` head-block text with continuation lines space-joined to one
line (`reports/round-28/readme/sweep.py:60` `ROW_RE`, `:61` `TOPIC_RE`, `:74-79` `topic_of`;
selftest control "continuation lines space-joined" passes, 12/12). Four rows go in **filename
order** inside `## myth-symbol/ (23)` (`corpus/README.md:196-220`; current order starts
`animal-symbolism.md`, `binding-speech-complex.md`, `celestial-symbolism-calendars.md`, …). Each
row's topic text must be **byte-equal** to the landed entry's own `- topic:` line — so the README
rows cannot be finalized before C01–C04's entries are chosen and audited.

**Do not repair carried README defects in this delta** (r39 C06 precedent). Observed live this
round: the H1 heading is duplicated at `corpus/README.md:1` and `:3`. Queue row
`R36-README-DUPLICATE-HEADING` is `carried-with-owner`; it stays carried.

**Blocking dependency for claim C at this cut:** `scout/K02-myth-gaps.md` had **not landed** when
C01 and C02 were written; both self-derived under the missing-dependency rule and **both picked the
same topic**. C01 (`cov/C01-entry-1.md:3`) proposes
`corpus/knowledge/myth-symbol/purity-pollution-codes.md` (citing r35 census row MS-2); C02
(`cov/C02-entry-2.md`) proposes `myth-symbol/purity-pollution-systems.md`. K02 has since landed and
**confirms that topic as its gap 4** (`scout/K02-myth-gaps.md:310-332`), explicitly noting it is
"confirming rather than re-recommending" C02's draft. So: **one topic, two competing slugs, and
three of K02's four gaps still have no author** — `mineral-stone-symbolism.md` (K02 `:212`),
`dream-vision-trance.md` (`:259`), `pilgrimage-sacred-geography.md` (`:303`). C03, C04, C05, C06
remain absent; `cov/C07-verify.md`, `cov/C08-verify.md` and `adj/A01-entries-bleed.md` have landed
but audit fewer than four entries (below).

`cov/C07-verify.md` independently reached the same vector conclusion as §4 ("`25/23/27/25/24/94`
sums to **218**, not the declared `224`, and names the wrong partition slot") and reports that it
**proved with the filed sweep** that applying the declared bytes leaves the tree sweep-red. It also
records a r39-policy consequence worth carrying: at 224 entries the basename index still has no
duplicate for C02's name, so the policy's §2(c) uniqueness assumption holds at the target size.
Claim C's after-state is apply-time and entirely unestablished at this cut.

**Audit-leg gap to reconcile.** Claim C's threshold is "audits 4/4 PASS" and the mission set gives
three verifiers (C05, C07, C08). At this seat's final cut `cov/C07-verify.md`, `cov/C08-verify.md`
and `adj/A01-entries-bleed.md` are on disk, but **C05 is absent**, only **two** entry drafts
(`C01`, `C02`) exist, and C08's own record says its lot-drawn targets C02 and C03 included an
absent C03. So no 4/4 audit is possible yet. `adj/A01-scan-instrument.py` is a second
file written under seat A01's directory beyond its declared `out` — worth the integrator's note
(it is read-only, self-locating, and writes nothing; `adj/A01-entries-bleed.md` header, and the
instrument's own `_find_root` docstring).

---

## §5 — Claim-O host decision (route, do not absorb)

The claim leaves the host to the wave ("its owning instrument identified by the wave"). Measured
facts:

| candidate host | state | editable by a seat? |
|---|---|---|
| `reports/round-19/audit/entry-audit.py:75` | filed round-19 byte; single-line extractor | **no** — filed-byte rule |
| `reports/round-27/audit/entry-audit.py:275` | filed round-27 byte; single-line extractor | **no** — filed-byte rule |
| `reports/round-35/cov/C14-audit-6-10.md:225-236` | a *report* containing the block parser, not a tool | **no** — filed round-35 byte |
| `tools/gates/provenance-audit.py:244-260` | **live** gate; block reader, space-join at `:259` | yes — but it does not tokenize `couples`; its only `couples` finding is `empty-couples` |
| `tools/harness/` | carries `packet_links.py`, `packet_uncertainty.py`, `r8_checks.py`, `receipt_guard.py`, `round_runner_conformance.py` — **no couples resolver** | n/a |

So the only live host that *reads a couples block* is `tools/gates/provenance-audit.py`, and its
defect is **latent** (the field's value is non-empty, so no `empty-couples` misfire today — this
seat confirms the gate's `field_block` returns the space-joined string, non-empty). A successor
resolver in `tools/harness/` is the natural durable home. Both are round-43+ work; the integrator
decides. **Do not let a leg claim a live mis-gating defect that does not exist.**

**K01 and X00 resolved this further, and the integrator should adopt their conclusion.** K01
(`scout/K01-n6-scout.md:103-110,230-240,326`) and X00 (`cross/X00-connector.md:33-79`) both
establish that the fix **cannot** be an edit to any filed r19/r27/r28 instrument (three divergent
copies, all read-only), that `reports/round-35/cov/C12-audit-runbook.md` is a fragment containing
no resolver code, and that the durable shape is a **new file under `tools/harness/`** authored to
`provenance-audit.py`'s `field_block` stop semantics. X00 also flags that `tools/gates/` carries
frozen snapshots and fixtures for `provenance-audit.py`, so patching *it* would drag a freeze
review in. This seat's §5 table is consistent with that conclusion and adds the latent-defect
qualifier: `provenance-audit.py` is the **template**, not the host.

---

## §6 — Fleet-report material (draft)

**Work performed (draft).** Claim O: fix the N6 wrapped-field extractor defect and re-derive the
reference census; claim C: +4 myth-symbol entries (23 → 27, total 220 → 224) with README rev 2.4.
Freshness stays paused (`claims.json:24`); no promotion/canon/clearance/closure; no filed-byte
rewrites; no in-tree runner execution; no re-freeze of `declared-in-r7`; no packet-surface changes.

**Landed changes.** Leave **pending integration evidence**. At this cut no claim-O implementation
(a *landed* fixed extractor, a *run* selftest, a corrected-census artifact) and no claim-C artifact
(four entries, a 4/4 audit, a README delta) is present in the round-42 tree. What the wave did land
is fenced drafts and analysis: `op/O01`-class patch drafts (`O02`'s control battery, `O03`'s
predicted census, `O08`'s queue-row text), one entry draft (`cov/C02-entry-2.md`), and the O03/O04
reproductions of the corrected census. Per the round's shared rule the fix and the entries are
**integrator-applied**; `op/O08-queue-update.md`'s own `verification` field records that **no landed
fix exists to verify**. No S01-owned source change and no independent acceptance result is asserted.

**Before → required after (not measured here).**

- **O / operability.** Before: the single-line extractor at `entry-audit.py:75` captures 0 tokens
  from `phonetics-phonology.md:72-77`; the filed r39 census reads `2504 = 2335 + 163 + 0 + 6`;
  the only live couples-block reader space-joins (`provenance-audit.py:259`) and mangles
  `tone-prosody.md` into `prosody.md`. Required after: a durable fixed extractor, the wrapped field
  read whole (4/4 intended targets under rule D), the corrected census filed
  (`2611 = 2437 + 166 + 0 + 8` live; `2508 = 2337 + 163 + 0 + 8` on the r39 tree), selftest green
  with a wrapped-field positive and a synthetic phantom negative, zero phantom tokens remaining,
  and each of the 8 unresolved tokens dispositioned.
- **C / coverage.** Before: `myth-symbol 23`, total 220, README rev 2.3. Required after:
  `myth-symbol 27`, total 224, README rev 2.4 with four byte-equal rows in filename order, sweep
  green (`rows 224 files 224`, footer `[25,27,25,29,24,94]`), audits 4/4 PASS.

**SHONEN.** No promotion, canon, clearance or closure conclusion. Capability wording stays
conditional until the fixed extractor, the corrected census, the four audited entries, the README
delta and the round's receipt have landed. Named for the report: the "phantom attributions"
mis-description (§0.2); the truncated r39 policy (§3); the rule-B/C false green (§2.3); the
unpinned terminator worth ±38 refs (§2.6); the C06 vector arithmetic error (§4); the duplicated
purity topic across C01/C02 (§0.8, §4); the r19 gate's independent `gap=False` failure (§2.5).

---

## §7 — Validation-leg spec

Use these as acceptance legs in round 42's validation integration; **missing artifacts and
`could-not-evaluate` are never green** (`reports/round-41/run-validation.py` precedent).

**O-legs**

1. **O1 — fixed extractor is durable, its host is named, and its terminator is pinned.** Require a
   **new** live instrument (K01/X00: under `tools/harness/`, never a patch to a filed
   `reports/round-19|27|28/audit/*` byte and never an edit to `tools/gates/provenance-audit.py`,
   which carries frozen snapshots). Require its terminator to be **blank line OR next header
   field** — not the next field alone, which over-reads body prose on 3–5 entries for ±38 refs
   (§2.6). Require the chosen terminator and the hyphen rule to be **written down in the
   instrument**, since §2.3 and §2.6 show the corpus result is sensitive to both.
2. **O2 — wrapped-field positive: the 4 intended targets by identity, under rule D.** Require the
   extractor to return exactly `{sound-change.md, tone-prosody.md, sound-symbolism.md,
   writing-systems.md}` from `phonetics-phonology.md:72-77`. **Require the absence of `prosody.md`
   and `toneprosody.md`.** A leg that checks only "4 tokens" passes under rules B, C and D and is a
   false green (§2.3, §2.6). O02's control 1 already asserts exactly this pair of legs.
3. **O3 — corrected census reproduces, and every unresolved token is dispositioned.** Require the
   four-class quadruple `2437/166/0/8` (or the tool's own reported total `2611`) on the live 220
   tree, and `2337/163/0/8` (`2508`) on the r39 212 tree. Require all 8 unresolved tokens listed
   with a disposition: `language-contact.md:7` ×3 and `phonetics-phonology.md:76-77` ×2 are
   *prospective* (the lines read "to seed" / "prospective sibling files"); `-gate.md` is the §5.6
   glob fragment (`gate-frozen-run-standard.md:15`); the
   `../linguistics/phonology-sanity.md` ×2 are the r19 X26-1 wrong-path defect, live in
   `synthesis/typed-label-routing-workflow.md:16` and
   `verification/label-channel-routing-verification.md:14`. The r39 four-class vocabulary cannot
   hold the *prospective* rows; the policy needs a fifth class (O10 §4 argues the same).
4. **O4 — selftest controls.** Require the wrapped-field positive, a synthetic phantom negative
   that fails when the rejoin is a plain space, and an unwrapped single-line regression control.
   Require the selftest to be **red** if rule C is substituted for rule D.
5. **O5 — adversarial fixture.** A hand-crafted wrapped field with a planted phantom token; require
   the extractor to classify it unresolved, not resolved, and not to invent a token.
6. **O6 — queue rows.** Require `N6-couples-extractor-wrapped-field` and
   `r39-basename-successor-instrument` to move to `fixed-with-evidence` **only** with the landed
   extractor path and the measured census as `verification`. Never edit the filed r37/r40 queue
   bytes in place; a new round-42 queue artifact or an append-only update record.
7. **O7 — do not over-claim the r19 gate.** Any leg asserting the r19 instrument now passes must be
   rejected: the bar fails on `gap=False`, independent of `couples` (§2.5).

**C-legs**

8. **C1 — four entries, established contract.** Require four new `corpus/knowledge/myth-symbol/`
   entries whose slugs are distinct from the 23 existing ones
   (`animal-symbolism, binding-speech-complex, celestial-symbolism-calendars, color-symbolism,
   comparative-frameworks, cosmology-cosmography, creation-myths-taxonomy,
   death-afterlife-eschatology, direction-symbolism, divination-omen-systems,
   eschatology-world-end-systems, flood-traditions, hero-journey-variants, motif-index-usage,
   myth-folktale-genres, myth-ritual-theories, number-symbolism, pantheon-archetypes,
   plant-symbolism, ritual-liminality, sacred-kingship-mythic-charter, symbolism-synthesis-method,
   trickster`), each carrying the r35 four-leg head block (`- sources:`/`- source:`,
   `- verified-at:`, `- recheck:`, and `- scope:` or `- couples:`), a `- gap filled:` statement
   with real absence-sweep output, and a decision record.
9. **C2 — one slug per topic, then audits pre-landing.** Require the integrator to resolve the
   C01/C02 duplicate **before** applying: one purity slug, and the other draft either re-slotted
   onto a K02 gap or dropped (§0.8, §4). Require C05's 4/4 verdict, C07's independent verification
   and C08's spot-audit **before** the entries are applied. Claim C's own threshold says "audits
   pre-landing"; a post-apply audit does not satisfy it, and C08's lot draw already hit an absent
   C03 once.
10. **C3 — README rev 2.4, mechanically.** Require `revision: 2.4`, `## myth-symbol/ (27)`,
    `Total knowledge entries: 224.`, footer `(total 224 files; directory totals 25/27/25/29/24/94)`
    — **not** the C06 mission's `25/23/27/25/24/94`, which sums to 218 and is sweep-red (§4) —
    and four rows whose `- topic:` text is byte-equal to the entries' own `- topic:` lines, in
    filename order. Require the **post-apply** sweep reading, never a predicted one
    (`readme-prediction-vs-delivery`, `defect-queue-v2.json`): `rows 224 files 224`, `footer_ok
    True`, `missing_from_index 0`, `topic_mismatch 0`, `orphan_rows 0`, exit 0.
11. **C4 — no carried-defect repair in this delta.** The duplicated H1 at `:1`/`:3` and any other
    carried README row stay carried.

**Cross legs**

12. **X1 — filed-byte preservation.** Require zero writes to `reports/round-1..41/**`,
    `corpus/lessons/*.md`, `tools/gates/frozen/**`, fleet `.ufo/**`, and zero corpus staging. The
    r41 precedent leg compares each candidate path's live sha256 against `git show HEAD:<path>`;
    reuse it. **Exception to surface, not to take:** the truncated r39 policy (§3) is a *found*
    filed-byte defect; it must be routed to the operator, never fixed in-wave.
13. **X2 — L1 lexicon.** The round-42 fragments must not contain an unnegated
    `promot*/canon*/clearance/closure/verified` claim in an assertive frame. Note this seat's own
    §3/§5 use `fixed-with-evidence` and `verified` only as quoted queue vocabulary and negations.
14. **X3 — telemetry closure.** `telemetry/observed-dispatch.json` must land and the
    `availability-close-42.json` closing snapshot must be a **new append-only file** naming
    `reports/round-42/telemetry/dispatch-declared.json` and its sha256 **at close time**
    (`50d29b3f60e3cff471842796798507fc8c0df321893988eccf6dbec70713aff4` at this seat's read).
    `runtime_concurrency` stays `null` with owner + reason unless measured.
15. **X4 — fleet report + MANIFEST + LOG.** Require
    `<fleet>/.ufo/reports/round-42/kotodama.md` with the four headings (Work performed / Landed
    changes / Before → after measurements / SHONEN), the `MANIFEST.json rounds[]` row, the
    `SCORECARD.md` per-axis verdict rows and the append-only `LOG.md` entry. All four are absent at
    this cut.
16. **X5 — receipt boundary.** `python3 reports/round-42/run-validation.py` is close-time and
    **integrator-only, in an isolated copy**. This seat did not execute it and neither did any leg
    above. Note `op/O06-receipt.md` and `op/O11-final.md` are receipt *drafts*, not runs.

---

## §8 — Peer fragments folded

Landed at this seat's final cut (`find reports/round-42 -type f | sort` → 30 files incl. this one;
6 declared `out` paths still absent). Each figure below was **read, not re-derived**; where this
seat measured independently the measurement is labeled "this seat".

| fragment | bearing on this dossier |
|---|---|
| `scout/K01-n6-scout.md` | §2.3, §2.4, §5. Confirms the wrapped field, the single-line hosts, the join-rule table, and that the fix must be a **new** file (§5). **Its rule table lists `" ".join(parts)` as producing two tokens (`tone-` and `prosody.md`); this seat and O10 both measured C14's newline-join as one mangled token `prosody.md`.** No count changes. |
| `scout/K02-myth-gaps.md` | §0.8, §4, §7 C2. Four gap-named topics: `mineral-stone-symbolism.md` (`:212`), `dream-vision-trance.md` (`:259`), `pilgrimage-sacred-geography.md` (`:303`), and the purity/pollution system (`:310-332`), which it **confirms** rather than re-recommends because C02 drafted it first. |
| `plan/P01-plan.md` | landed; leg structure only. |
| `cross/X00-connector.md` | §0.6, §2.6, §5, §7 O1. Resolves the host to a new `tools/harness/` file (`:33-79`) and finds the fourth extractor variant that over-reads (`:80-140`), measured by it at 3 entries/`2615` refs and by this seat at 5 entries/`2653` refs — §2.6. Its C6 (measure O before or after C, pick and record) is the ordering trade this seat folds in §8 below. |
| `cross/X01-trades.md` | §0.2, §4, §8 below. T1 the O↔C shared measurement surface. |
| `cross/X02-honesty.md` | landed; honesty critique of the claims. |
| `op/O02-controls.md` | §7 O4/O5. Control 1 asserts the 4 intended tokens present **and** `{prosody.md, toneprosody.md, "tone- prosody.md"}` absent — exactly the discrimination §7 O2 requires. |
| `op/O03-predicted.md` | §2.3, §7 O2/O3. Same corrected census on both trees. Its §5 recommends "drop the hyphen and merge" — see the join-rule wording note below. |
| `op/O04-verify.md` | §2.3, §2.5, §7 O2/O7. Independent isolated-copy verification; rule table agrees with this seat's on all four rules and both trees; states a block parser alone reads **3/4**, hyphen-aware **4/4**. |
| `op/O05-traps.md` | §7 O5. The adversarial fixture. |
| `op/O06-receipt.md`, `op/O11-final.md` | §7 X5. Receipt drafts. |
| `op/O07-gap-fill.md`, `op/O08-queue-update.md` | §7 O6. O08's `verification` field records that **no landed fix exists to verify**. |
| `op/O09-scribe.md`, `op/O10-gap-fill.md` | §2.3–§2.5, §5. (O10 read before it was joined by the others.) |
| `op/O12-policy-check.md` | §3, §2.3. Confirms the truncation independently (`:13` — "the 2504 census lives only outside it"; grep for `2504\|2335\|163` in the landed file → 0 hits) and states the successor-note arithmetic as `2508 = 2337 + 163 + 0 + 8`, unresolved **rising** 6 → 8. |
| `cov/C01-entry-1.md` | §0.8, §4, §7 C1/C2. Entry 1 draft, slug `purity-pollution-codes.md` — collides on topic with C02. |
| `cov/C02-entry-2.md` | §0.8, §4, §7 C1/C2. Entry 2 draft, slug `purity-pollution-systems.md`. |
| `cov/C07-verify.md` | §4, §7 C3. Independently reaches the §4 vector conclusion and proves with the filed sweep that the mission bytes are sweep-red; records that C02's name stays unique at 224 entries. |
| `cov/C08-verify.md` | §4 audit gap, §7 C2. Lot draw selected C02 and C03; C03 was absent, so its spot-audit is incomplete by its own record. |
| `adj/A01-entries-bleed.md` + `adj/A01-scan-instrument.py` | §4. Bleed scan; its own header files a mirror-target correction (the mission names `A02-r40`, a PROVINCE seat; the entries precedent is `reports/round-37/adj/A02-entries-bleed.md`). |
| `review/R02-review.md` | §0.2, §4, §7 O2. Trap D is the vector finding this seat adopted. |
| `calib/Ca01-gap-fill.md`, `scribe/S02-telemetry-draft.md` | cross-claim; no bearing on §2–§5. |
| **still absent** | `scout/…` none; `op/O01-fix-draft.md`, `review/R01-review.md`, `cov/C03-entry-3.md`, `cov/C04-entry-4.md`, `cov/C05-audit.md`, `cov/C06-delta-receipt.md` — 6 declared `out` paths. |

**Three cross-seat items the integrator must adjudicate, not a seat:**

1. **Join-rule wording (token identical, description differs).** K01 §4, O03 §5, O04 §4 and O08 §3
   describe the fix as *de-hyphenation* ("drop the hyphen and merge"); O10 §1 and this seat describe
   it as *rejoining the hyphen-terminated continuation keeping the hyphen*. All five produce the
   same token `tone-prosody.md`, and the negative controls reject both wrong variants
   (`prosody.md`, `toneprosody.md`). The successor instrument and the selftest must use one wording;
   a reader implementing "drop the hyphen" literally on the *other* branch risks the over-merge O02
   control 1 already guards against.
2. **X01 T1 / X00 C6 — O and C share one mutable measurement surface, and the counting order is
   load-bearing.** The four new myth-symbol entries are themselves couples-bearing census inputs
   (`cross/X01-trades.md` T1; `cross/X00-connector.md:185-215`). Measured, only the entry set
   differs; **X01's table shows the live 220-entry tree at `unresolved 6`, where this seat, O03,
   O04 and O10 all measure `8` under block extraction** — X01's row is single-line-semantics.
   X00 offers two admissible orders and requires the integrator to pick and record one:
   (1) measure O first at 220 entries (`2611` on the correct extractor), then apply C, stating C's
   effect separately as +4 entries; or (2) apply C first, then measure at 224 entries, with O03
   stating the 224-entry prediction explicitly. Either way **O03 and O04 must agree on the entry
   count they measured**, not only on the token counts, and A01's bleed scan must state which
   extractor it used. This is a declared trade with a real sequencing consequence for claim O's
   `after_required`.
3. **The over-read magnitude is not agreed between seats (3/2615 vs 5/2653, §2.6).** Do not file
   one number as *the* measurement. File the terminator rule and the chosen implementation, and let
   the successor instrument's own run produce the count. `op/O12-policy-check.md` already states the
   successor-note arithmetic as `2508 = 2337 + 163 + 0 + 8` with unresolved **rising** 6 → 8.

---

## Owed

- `reports/round-42/op/O01-fix-draft.md` and `review/R01-review.md`: **absent** at this seat's final
  cut — the fix patch and the first adversarial review are owed. (`O02`–`O12` except `O01` landed;
  §8.)
- `reports/round-42/scout/K01-n6-scout.md`, `K02-myth-gaps.md`: **landed** (§8). The host decision in
  §5 stands as this seat's independent read, corroborated by K01 and X00, not derived from them.
- `reports/round-42/cov/C03-entry-3.md`, `C04-entry-4.md`, `C05-audit.md`, `C06-delta-receipt.md`:
  **absent** — claim C has two entry drafts of four, no 4/4 audit and no README delta.
  (`C01`, `C02`, `C07`, `C08` landed; §8.)
- `reports/round-42/plan/P01-plan.md`, `cross/X00-connector.md`, `cross/X01-trades.md`,
  `cross/X02-honesty.md`: **landed**. `review/R01-review.md`: **absent**.
- **Operator/integrator decision owed:** the C06 mission's vector bytes `25/23/27/25/24/94` sum to
  218 and are wrong; use `25/27/25/29/24/94` (§4; R02 Trap D and C07 both found it independently).
- **Operator/integrator decision owed:** the truncated `reports/round-39/calib/basename-couples-policy.md`
  (§3). Fixing it edits a filed round-39 byte; no seat may. Route it as a new queue row or an
  amendment to `basename-couples-policy` / `r39-basename-successor-instrument`. O12's check
  independently confirms the truncation.
- **Operator/integrator decision owed:** the claims.json:13 "2 phantom attributions" wording
  (§0.2) — the corrected census is `+2 direct / +2 unresolved` versus r39, not "minus phantoms".
- **Integrator adjudication owed:** the C01/C02 duplicate purity slug and the three unauthored K02
  gaps (§0.8, §4); the join-rule wording, the O/C counting order (X00 C6) and the unpinned
  terminator (§2.6, §8).
- `to-verify`: whether the two `../linguistics/phonology-sanity.md` wrong-path references and the
  `language-contact.md:7` prospective seeds should be repaired in a corpus byte change (a new
  finding, not this round's claim).
- `to-verify`: whether the "prospective" fifth class is adopted into the policy by successor note
  or by a new policy revision.
- `reports/round-42/validation.json`, `telemetry/observed-dispatch.json`,
  `telemetry/availability-close-42.json`, `<fleet>/.ufo/reports/round-42/kotodama.md`,
  `MANIFEST.json rounds[]`, `SCORECARD.md` rows, `LOG.md` entry: close-time, integrator-owned.

---

## Citations

- `REGIMEN.md:20` (position 10, devin/deepseek-v4-1-flash-high, 32–64); `:34-50` (per-round record set).
- `reports/round-42/claims.json:5-8` (declared dispatch), `:9-23` (claims O/C, before/after,
  thresholds), `:24` (non-goals); `reports/round-42/targets.json` (shared_rules; seat `S01`).
- `reports/round-42/telemetry/dispatch-declared.json` (allocation; `durable_sources` digests;
  `closing_snapshot: open-at-seat-close`).
- `corpus/knowledge/linguistics/phonetics-phonology.md:72-77` (the wrapped field), `:279-280`
  (the body line naming `tone-prosody.md`, `sound-symbolism.md`, `writing-systems.md`).
- `reports/round-19/audit/entry-audit.py:25-32` (`HEADER_RE`/`GAP_RE`/`DECISION_RE`/`MDREF_RE`),
  `:74-96` (`couples_targets`), `:75` (single-line extractor); `reports/round-27/audit/entry-audit.py:274-280`.
- `reports/round-35/cov/C14-audit-6-10.md:225-236` (`fields_of` block parser), `:263-288`
  (`couples_refs`), `:332-336` (four-class output).
- `reports/round-39/calib/basename-couples-policy.md:14,27,50,60,71,104-107` (the truncated file's
  full heading set and its EOF); sha256 `105dfff6c667ad5b77c28be8d6070ec243b5e19029fb60ae83d6028aa2e941cf`.
- `reports/round-39/calib/Ca03-basename-policy.md:144-258` (the missing §6 recipe in the draft),
  `:268-277` (filed Part 2 output + the five attributed unresolved names), `:292-303` (§7, missing
  from the landed file); 359 lines, sha256
  `125ede77e3f50e3c58af61fb2fad246c8378b4dcfc4ee5d1749da8dd53a17850`.
- `reports/round-39/calib/Ca04-verify.md` (D1 the wrapped field; D2 the disposition leg;
  `to-verify` full block-parser recount).
- `reports/round-39/run-validation.py:117-120` (the `fallback`-marker leg that let the truncation
  pass), `:129-130` (the `334` leg reading `Ca04-verify.md`, not the policy).
- `tools/gates/provenance-audit.py:76-77` (`FIELD_RE`, `INDENT_RE`), `:244-260` (`field_block`;
  `" ".join` at `:259`), `:103,215,224` (`empty-couples`), `:235` (expected count 0).
- `corpus/README.md:1,3` (duplicated H1), `:5` (rev 2.3), `:168,196,222,249,281,308` (section
  headers 25/23/25/29/24/94), `:532` (totals 220), `:534-536` (footer).
- `reports/round-28/readme/sweep.py:50-57` (section order), `:60-61,74-79` (row/topic contract),
  `:106-115` (footer parse); sha256 `9b2ccac0046831fdaf48863ccd0ff6ca0fa390d044746c876e83a71c06f0cdd3`.
- `reports/round-40/op/defect-queue-v2.json` rows `N6-couples-extractor-wrapped-field`,
  `r39-basename-successor-instrument`, `basename-couples-policy` (`fixed-with-evidence`),
  `O12-runner-isolation-hazard`, `R36-README-DUPLICATE-HEADING`.
- `reports/round-41/run-validation.py:5-13` (relative `ROOT`, `BASELINE`), `:117-152` (the leg
  shapes reused in §7); `reports/round-41/scribe/S01-integration-draft.md:28-35` (dossier heading
  precedent); `reports/round-41/telemetry/availability-close-41.json` (closing-snapshot shape).
- `reports/round-42/op/O10-gap-fill.md` §§1-4 (rule table, live host, wrapped-field census,
  `2611/2437/166/0/8`); `reports/round-42/op/O09-scribe.md` (pre-landing snapshot).
- `reports/round-42/scout/K01-n6-scout.md:103-110,131-147,167-180,230-240,326` (host, join-rule
  table, corrected census, new-file conclusion);
  `reports/round-42/scout/K02-myth-gaps.md:212,259,303,310-332` (the four gap topics and the
  purity collision check).
- `reports/round-42/cross/X00-connector.md:33-79` (host resolution: new `tools/harness/` file),
  `:80-140` (the over-reading fourth variant and the `2615` figure), `:185-215` (C6 counting order);
  `reports/round-42/cross/X01-trades.md` T1 (the shared measurement surface);
  `reports/round-42/review/R02-review.md:23-25,126-140,182-183` (Trap D, the vector arithmetic).
- `reports/round-42/op/O02-controls.md:24,168-169,209-211` (control 1's must-contain/must-not sets);
  `op/O03-predicted.md:19-20,105-121,143-154` (recommended rule, both-tree census);
  `op/O04-verify.md:105-133,169-175,199-201` (isolated verification, 3/4 vs 4/4);
  `op/O08-queue-update.md:167-170` (queue-row draft; "NO landed fix exists to verify");
  `op/O12-policy-check.md:13-26,101-102` (independent truncation check; `2508` arithmetic).
- `reports/round-42/cov/C01-entry-1.md:3,15` (slug `purity-pollution-codes.md`; MS-2 citation);
  `cov/C02-entry-2.md:3-21` (slug `purity-pollution-systems.md`);
  `cov/C07-verify.md:36-39,53,73,159-162` (vector finding, negative controls, uniqueness at 224);
  `cov/C08-verify.md:112,213,224-244` (lot draw, incomplete spot-audit);
  `adj/A01-entries-bleed.md:1-12` (mirror-target correction).
- Command outputs (this seat, 2026-10-19, lane root at `ac47c78`, `export TMPDIR=$PWD/.scratch
  PYTHONDONTWRITEBYTECODE=1`, all read-only; no runner executed anywhere):
  (a) four-rule census over the 220 tree → `2607/2435/166/0/6`; `2611/2437/166/0/8` (rules B, C and
  D, differing only in the wrapped-field token); the next-field-only terminator → `2653` refs over 5
  over-reading entries;
  (b) two-rule census over the 212-entry r39 tree → `2504/2335/163/0/6` (reproduces the filed Part 2)
  and `2508/2337/163/0/8`;
  (c) wrapped-field scan → exactly 1 wrapped `couples` field, 5 continuation lines;
  (d) `python3 -B reports/round-19/audit/entry-audit.py corpus/knowledge/linguistics/phonetics-phonology.md`
  → `FAIL … src=15/15 couples=0 unresolved=[] gap=False dec=True`, `TOTAL 0/1`;
  (e) `python3 -B reports/round-28/readme/sweep.py` → exit 0, `rows 220 files 220`, `footer_ok True`,
  footer `[25,23,25,29,24,94]`, `readme_sha256 d2eed26b…ac4f`; `--selftest` → 12/12;
  (f) `python3 tools/harness/round_runner_conformance.py --selftest` → `selftest_passed: true`;
  (g) `git show <fd55e1f|456674d|ac47c78|HEAD>:reports/round-39/calib/basename-couples-policy.md | wc -l` → 107 for all four;
  (h) vector sums → `sum([25,23,27,25,24,94]) = 218`, `sum([25,27,25,29,24,94]) = 224`;
  (i) `find reports/round-42 -type f | sort` → 5 files at first census, 30 at finalization;
  `git status --porcelain` → `?? reports/round-42/` only (no tracked modification).
