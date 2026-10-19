- Seat: O05 | verifier (independent verifier 2) | claim O | date 2026-10-19T16:57Z | baseline `7ceff59` | out `op/O05-traps.md`

# O05 — trap hunt for the basename-couples successor instrument

Mission (verbatim, `reports/round-43/targets.json:21`): *"Independent verifier 2:
hunt the traps — a token with a :NN anchor, a brace-expanded token, a token that
is a pure basename with two index hits, a couples field that is the last header
line. Confirm the draft's class assignment for each is the policy's, not a
guess."*

**Object under test: `reports/round-43/op/O01-tool-draft.md` — ABSENT at every
cut of this seat** (`ls -1 reports/round-43/op/` at 16:57Z lists only
`O02, O03, O04, O06, O07, O12`, no `O01`). Verdict on the draft itself:
`could-not-evaluate`; this is not a pass. To keep the seat load-bearing I

1. built an independent policy oracle and measured every named trap against the
   live corpus at HEAD;
2. audited the only durable implementation at HEAD
   (`tools/harness/couples-reference-extractor.py`, sha256
   `d8d23a265d12d290de69a6eb50454273af4ca699986812c6e203a030f4679cf1`), since
   any O01 draft will either replace or fork it;
3. ran O02's control surface against the traps and found two controls that do
   not discriminate the host's actual failure shapes;
4. filed exact pass/fail vectors so a later O01 can be graded without repeating
   the measurement (O04's §3 matrix is the companion; this file is the trap
   oracle it points to).

All commands read-only; no filed byte edited, nothing staged under `corpus/`, no
`reports/round-*/run-validation.py` executed, no git/network/install action.
`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1` throughout. Probe scripts
live in `.scratch/o05/` (`oracle.py`, `synth2.py`, `host_probe.py`, `leak.py`,
`final_probe.py`).

## 1. Trap matrix — policy-correct assignment, measured

| # | trap | live population at 223 entries | policy rule | correct assignment | failure shape if mishandled |
|---|---|---|---|---|---|
| 1 | `:NN`/`:NN-NN` anchor | **18 distinct anchored tokens, 8 entries, 19 occurrences** | §1 `:21-22`: anchor not part of token | strip anchor, then classify the `.md` token; 17 direct, 1 fallback (`calibration-registry.md:91`) | anchor retained → false unresolved or failed dedup |
| 2 | brace-expanded token | **79 entries, 218 `{…}.md` groups, 977 expanded occurrences**, all direct | §1 `:18-20`: one-level expansion before resolution | expand first, classify **each** expanded token | raw group kept → slash-bearing group unresolved (16 false rows in `akan.md` alone) |
| 3 | pure basename, two index hits | **0 live** (223 basenames, 223 files, 0 duplicates) | §2 `:36-48`: ≥2 hits → `ambiguous` | `ambiguous`, all hits named, never `hits[0]` | first-hit guess; or `ambiguous` conflated with fallback |
| 4 | `couples:` as the last header line | **21 entries** (20 blank+`## ` heading, 1 wrapped+heading) | §1 field capture; boundary termination | stop at blank / non-indented line / next `- key:` / EOF | body prose swallowed: naive shape +34 tokens over these 21, corpus total 2772 vs 2730 (r42's pathological `FIELD_RE` shape: 3396, `Ca01-gap-fill.md:187-196`) |
| 5 | wrapped field hyphenation (**added; decisive**) | **1 field**, `phonetics-phonology.md:72-77` | claim O `claims.json:28,34` "4 named targets" + Ca04 D1 `Ca04-verify.md:78-93` | `{sound-change.md, tone-prosody.md, sound-symbolism.md, writing-systems.md}` | newline/space join yields `prosody.md`; **class totals stay identical (2 direct + 2 unresolved)**, so an arity/totals-only control is a false green |
| 6 | glob fragment (§5.6, adjacent) | **1**, `-gate.md` from `gate-frozen-run-standard.md:15` | §5.6 `:97-103`: skip or separately class; **never** unresolved, **never** fallback | separate `glob-fragment` / artifact class, held out of the four-class findings | host classifies it `fallback` when its basename has one index hit (probe §3.3) |
| 7 | slash-bearing token with unique basename elsewhere (§5.1, adjacent) | **2 occurrences**, `../linguistics/phonology-sanity.md` (`label-channel-routing-verification.md:14`, `typed-label-routing-workflow.md:16`) | §5.1 `:73-87`: no re-partitioning; Tier 1 only | `unresolved` | C14-as-written shape would resolve it into a partition by basename |

## 2. Per-trap evidence and exact expected classes

### 2.1 Anchors — 18 distinct tokens, 17 direct + 1 fallback

`grep`-equivalent probe over every `couples:` block (anchored tokens only):

```
agrarian-field-system-lexicon.md  textile-technology.md:76                  direct (entry dir)
funerary-material-culture.md      craft-artisan-lexicon.md:106              direct (entry dir)
taboo-strata-lifecycle.md         politeness-taboo-euphemism.md:23, :37      direct (entry dir; one token after dedup)
mineral-stone-symbolism.md        corpus/knowledge/civilizations/maya-classic.md:10   direct (lane root)
                                  civilizations/maori.md:13-14              direct (corpus/knowledge base)
                                  civilizations/siam-thai.md:126            direct
                                  civilizations/china-shang-zhou.md:106     direct
                                  civilizations/israel-ancient-hebrew.md:150 direct
purity-pollution-boundary-systems.md ritual-liminality.md:14               direct (entry dir)
sacred-kingship-mythic-charter.md corpus/knowledge/civilizations/benin.md:42 direct (lane root)
                                  civilizations/persia-achaemenid.md:1     direct (corpus/knowledge base)
                                  calibration-registry.md:91               FALLBACK -> corpus/knowledge/verification/calibration-registry.md
sacred-topography-pilgrimage.md   five civilizations/... tokens             direct (corpus/knowledge base)
worked-example-verification.md    corpus/knowledge/linguistics/historical-linguistics.md:55 direct (lane root)
```

The decisive anchor case is `sacred-kingship-mythic-charter.md:37`
`calibration-registry.md:91`: Tier 1 fails at all three bases, the token is
slash-free, and exactly one file under `corpus/knowledge/*/` carries the
basename — so it is **fallback with an explicit mapping**, not unresolved and
not direct. The host produces exactly this
(`host_probe.py`: `{'class': 'fallback', 'mapping':
'corpus/knowledge/verification/calibration-registry.md', 'alignment': 'ok'}`).
`taboo-strata-lifecycle.md:21` carries the same token twice (`:23`, `:37`);
per-entry dedup must leave **one** token, or the census gains a phantom row.

Regex-level anchor stripping is implicit: `:` is outside
`[A-Za-z0-9_./{},\-]+\.md`, so `civilizations/maori.md:13-14` yields
`civilizations/maori.md`. A split-based extractor that passes the anchored
string through fails; the tool must be tested on the anchored form, not only on
the bare name.

### 2.2 Braces — 79 entries, 218 groups, 977 expanded occurrences, all direct

`grep -rl '^- couples:.*{' corpus/knowledge/*/*.md | wc -l` → **79**;
script count of literal `{…}.md` groups → **218**; no nested braces, no
unbalanced braces. Every expanded token is `direct` (977 occurrences, 0
non-direct in the probe). Distribution: civilizations 54, culture-material 11,
synthesis 9, verification 5.

The canonical case is `corpus/knowledge/civilizations/akan.md:4`:

```
- couples: language—`../linguistics/{phonetics-phonology,writing-systems,orality-formulaic-language,naming-systems,sociolinguistics-registers,kinship-terminology}.md`;
  myth/symbol—`../myth-symbol/{cosmology-cosmography,pantheon-archetypes,myth-ritual-theories,symbolism-synthesis-method}.md`;
  era/costume—`../culture-material/{era-periodization-models,textile-technology,costume-semiotics,sumptuary-law-rank-display,ritual-garments,material-culture-inference-method}.md`
```

16 expanded tokens, all direct. If expansion is skipped, the three raw matches
bear `/` and become 3 unresolved rows; if the group is classified as a unit
before expansion, the same. Expansion must precede both Tier 1 and Tier 2.

### 2.3 Two-hit basename — no live instance; synthetic is mandatory

`corpus/knowledge/*/*.md` = 223 files, 223 distinct basenames, **0 duplicates**
(also `reports/round-42/calib/Ca01-gap-fill.md:180-184`; O03 `:407`). So
`ambiguous` has zero live coverage and only a synthetic injected index can test
it. My fixture (`.scratch/o05/fixture`, in-memory index; nothing written under
`corpus/`) and results:

```
INDEX {'dup.md': ['know/p1/dup.md','know/p2/dup.md'], ...}
PASS ambiguous: dup.md, 2 index hits, no entry-dir hit          -> ambiguous
PASS direct precedence: dup.md, 2 hits, entry-dir file exists  -> direct
PASS fallback: only1.md, 1 index hit                           -> fallback know/p1/only1.md
PASS unresolved: ghost.md, 0 hits                              -> unresolved
PASS unresolved: p9/dup.md, slash-bearing wrong prefix          -> unresolved
PASS direct: p1/only1.md, slash-bearing correct prefix          -> direct
SUMMARY 6 / 6
```

The direct-precedence row is the one most likely to be missed: §5.4 `:89-92`
says Tier 1 is never relaxed, so a basename with two index hits is still
`direct` when the entry directory (or lane root, or `corpus/knowledge/<token>`)
holds the file. The host passes it (`('direct', None)`); a tool that checks the
index first would flip it to `ambiguous`.

### 2.4 Last-header-line — 21 entries, and 25 legitimate zero-token fields

`couples:` is the last header field, followed by a blank line and `## 1. …`, in
**21 entries** (list: color-terminology:7, historical-linguistics:7,
kinship-terminology:24, language-contact:7,
language-shift-obsolescence-revival:30, linguistic-anthropology:7,
morphological-typology:7, naming-systems:36, numerals-and-measures:27,
orality-formulaic-language:28, phonetics-phonology:72 (wrapped 72-77),
politeness-taboo-euphemism:37, semantic-fields-lexicon-building:7,
semantics-pragmatics:7, sociolinguistics-registers:43, sound-symbolism:19,
syntax-typology:7, writing-systems:7, citation-format-and-source-registry:11,
myth-consistency-gate:4, provenance-audit-ledger-format:4). Correct field
values are just the couples line/continuations; a boundary-blind parser leaks
body `.md` mentions. My measured leak for a "stop only at the next `- key:`"
parser: **2772 vs 2730 tokens** (+42; +34 over these 21 entries). The r42 audit
of the pathological three-name `FIELD_RE` shape measured **3396**
(`reports/round-42/calib/Ca01-gap-fill.md:187-196`).

Two boundary sub-cases must be pinned:
- **No blank before the heading** (synthetic): termination must fire on the
  non-indented line, not only on a blank.
- **Indented prose after a blank** (synthetic): the host's
  `couples_block` skips blank lines (`couples-reference-extractor.py:64-65`), so
  it captures an indented body line. Probe:
  `blank_then_indented_prose → parts=['a.md','prose mentions b.md'],
  tokens=['a.md','b.md']` (wrong); `blank_then_heading` and
  `no_blank_then_heading → tokens=['a.md']` (right). Live corpus has **0**
  blank-then-indented cases (O04 G6 `:259-270` independently), so today's
  counts are unaffected; the rule is latent-broken and must `break` on a blank.

Separately, **25 entries have a couples field with zero `.md` tokens**
(prose-only couples prose: e.g. `color-terminology:7`, `animal-symbolism`,
`number-symbolism`, `verification-method-overview`). A zero there is legitimate
and must be reported as `tokens=0`, not as a missing/skipped field. This is a
different zero from the wrapped-field zero Ca04 D1 fixed.

### 2.5 Wrapped field — the decisive trap

`corpus/knowledge/linguistics/phonetics-phonology.md:72-77` (sha256
`b4f9b00384bc6840bdd1d7d7e7ae9bbb127a2fd1f5010c98d5b253df65d7776b`), lines
76-77: `…sound-change.md, tone-` / `prosody.md, sound-symbolism.md,
writing-systems.md`.

Measured join variants (`final_probe.py`):

```
newline join  -> ['prosody.md', 'sound-change.md', 'sound-symbolism.md', 'writing-systems.md']
space join    -> ['prosody.md', 'sound-change.md', 'sound-symbolism.md', 'writing-systems.md']
dehyphenated  -> ['sound-change.md', 'sound-symbolism.md', 'tone-prosody.md', 'writing-systems.md']
```

Expected policy classes: `sound-symbolism.md` direct, `writing-systems.md`
direct, `sound-change.md` unresolved, `tone-prosody.md` unresolved. **The first
two variants produce the same class totals (2 direct + 2 unresolved) and the
same arity (4).** A control that asserts only "4 tokens" or only totals passes a
tool that has minted the phantom `prosody.md` and lost `tone-prosody.md` — the
exact false green O02 S1b/S1c/S1e is designed to stop (`O02-controls.md:57-61`).
The O01 tool and its selftest must assert the **token set**, and the filed
census must name `tone-prosody.md`.

The four-class result for this entry is 2 direct + 2 unresolved; the r42 host
instead prints `sound-change.md prospective`, `tone-prosody.md prospective`
(§3.2), which is the class-label failure, not a count failure.

### 2.6 Glob fragment and the slash gate (adjacent traps)

- `-gate.md` is produced by `corpus/knowledge/verification/*-gate.md` in
  `gate-frozen-run-standard.md:15`. Policy §5.6 forbids counting it as an
  unresolved couples finding and forbids resolving it via the fallback. The
  four-class census should therefore show **7 unresolved + 1 separately classed
  glob artifact**, not 8 unresolved. O04 `:128` reports `unresolved=8` (folding
  the glob in); see §5 for the reconciliation.
- `../linguistics/phonology-sanity.md` occurs twice
  (`label-channel-routing-verification.md:14`,
  `typed-label-routing-workflow.md:16`); it is slash-bearing, Tier 1 fails, and
  §5.1 forbids the basename fallback even though
  `corpus/knowledge/verification/phonology-sanity-gate.md` exists. Expected:
  `unresolved` in both carriers.

## 3. Audit of the only durable host at HEAD

`tools/harness/couples-reference-extractor.py` (r42 N6). Its own selftest is
green (8/8, exit 0) and it already reads the wrapped field whole:

```
PASS wrapped positive 4/4 tokens ['sound-change.md', 'sound-symbolism.md', 'tone-prosody.md', 'writing-systems.md']
PASS wrapped positive heals soft wrap
PASS over-capture trap (prose excluded)
PASS glob fragment classified
```

But a green self-test is not trap conformance. Measured against the matrix:

### 3.1 Passes
- Block extraction + hyphen healing (`couples_block:50-74`, `join_parts:76-94`):
  live wrapped entry → 4 tokens, `tone-prosody.md` present, `prosody.md` absent.
- Anchors: `resolve_entry` on the three anchor-heavy entries shows **0** token
  names containing `:`; `calibration-registry.md` → fallback with the correct
  mapping and group alignment `ok`.
- Braces: `akan.md` → 16 tokens, all direct.
- Ambiguous: injected two-hit index → `('ambiguous', None)`; never `hits[0]`.
- Direct precedence: entry-dir hit + two index hits → `('direct', None)`.
- Slash gate: `p9/dup.md` with a unique basename elsewhere → `('unresolved', None)`.
- Zero-token entry: `color-terminology.md` → `tokens=0`, no exception.

### 3.2 Fails the four-class contract: fifth `prospective` class
Host census at 223 entries:

```
entries=223 refs=2730 -> direct=2556 fallback=166 unresolved=2 prospective=5 glob-fragment=1
```

The 5 `prospective` rows are `honorifics-and-register.md`,
`naming-and-onomastics.md`, `phonology-basics.md` (language-contact:7),
`sound-change.md`, `tone-prosody.md` (phonetics-phonology:72-77). Policy §2 has
four classes; claim O (`claims.json:28`) requires the policy's four classes.
`sound-change.md`/`tone-prosody.md` must be `unresolved` with a named reason
("prospective sibling declared, never written"), not a fifth class. O02 S1f
fails the host by design (`O02-controls.md:61`); O04 G1/G5
(`O04-verify.md:250-272`) reaches the same finding.

### 3.3 Fails §5.6 ordering: glob check runs after Tier 2
`classify` checks `fallback` (`:143`) and `ambiguous` (`:145`) **before**
`glob-fragment` (`:147`). With an injected index:

```
glob fragment '-gate.md', one basename hit   -> ('fallback', 'x')      # §5.6 violation
glob fragment '-gate.md', two basename hits  -> ('ambiguous', None)   # §5.6 violation
glob fragment '-gate.md', zero hits          -> ('glob-fragment', None) # live case only
```

The live `-gate.md` has zero hits, so the host's filed 2730 is correct today —
but the rule is wrong and O02 S8 cannot catch it because S8 injects an **empty**
index (`O02-controls.md:282-285`, `glob_class, _ = _cls("-gate.md", entry_dir,
empty)`). The successor must classify glob context **before** Tier 2 (or pass
the pre-token `*` context into `classify`), and the control must include
one-hit and two-hit indexes.

### 3.4 Fails the blank-line boundary
See §2.4; `couples_block:64-65` `continue`s past blank lines. Live impact 0,
synthetic impact one false token per indented prose line. O04 G6 and K01 F5
agree; O02 S7a uses non-indented prose and therefore passes the host.

### 3.5 Census shape
`--census` prints totals only (`:298-330`); there is no per-entry four-class
report and no fallback mapping list. That is O06/G4 territory, not a class
error, but it means the current host cannot file the claim's census artifact
without a successor output leg.

## 4. Independent oracle at HEAD (cross-check for O03/O04)

Block extraction + hyphen join + per-entry dedup + four classes + §5.6 glob
quarantine, over all 223 entries:

```
TOTALS {'direct': 2556, 'fallback': 166, 'ambiguous': 0, 'unresolved': 7, 'glob': 1} sum 2730
four-class findings 2729 + 1 glob artifact = 2730 raw token rows
```

Unresolved rows (7 occurrences, 6 distinct): `honorifics-and-register.md`,
`naming-and-onomastics.md`, `phonology-basics.md` (all
`language-contact.md:7`), `sound-change.md`, `tone-prosody.md`
(`phonetics-phonology.md:72-77`), `../linguistics/phonology-sanity.md` ×2
(`label-channel-routing-verification.md:14`,
`typed-label-routing-workflow.md:16`). Glob artifact: `-gate.md`
(`gate-frozen-run-standard.md:15`).

Baseline reproduction on the policy's eleven r35/r36 entries: **334 = 319
direct + 15 fallback + 0 ambiguous + 0 unresolved** (my probe; matches policy
`basename-couples-policy-full.md:220-233` and `A06-verify.md:29`). This confirms
the trap extractor did not disturb the filed baseline.

Cross-check: O03 predicts exactly these totals (`O03-predicted.md:10-21,125`,
`2556+166+7+1=2730`, 422 global-distinct). O04's oracle reports the same
direct/fallback/ambiguous but folds the glob into `unresolved=8`
(`O04-verify.md:128`). Reconciliation: §5.6 says a glob fragment is "not a
couples finding"; report **7 unresolved + 1 glob artifact**, or report 8 rows
with the glob row explicitly labelled non-finding. An unqualified
`unresolved=8` overstates the finding population by one.

Discrepancy to correct: O04 `:188` says "**49 entries** carry braces". Measured
at HEAD: **79 entries**, 218 groups
(`grep -rl '^- couples:.*{' corpus/knowledge/*/*.md | wc -l` → 79; script →
218 groups, 0 nested, 0 unbalanced). O03 `:472` independently says 218 groups.
The 49 figure should not propagate into O09's claim summary.

## 5. Conformance checklist for O01 (run when the draft lands)

Status vocabulary: PASS / FAIL / `could-not-evaluate` (object absent). Every row
has an executable vector; none requires writing under `corpus/`.

| # | requirement | expected | status now |
|---|---|---|---|
| C1 | field capture, single line and wrapped; stop at blank / non-indented / next `- key:` / EOF | wrapped field → 4 tokens; 21 last-header entries leak 0 body tokens; 25 zero-token entries report 0 | `could-not-evaluate` (draft); host passes live, fails synthetic blank+indented |
| C2 | hyphen-aware join | token set exactly `{sound-change.md, tone-prosody.md, sound-symbolism.md, writing-systems.md}`; `prosody.md`, `toneprosody.md`, `tone- prosody.md` absent | `could-not-evaluate`; host passes |
| C3 | token grammar + anchor stripping | 18 distinct anchored tokens; `calibration-registry.md:91` → `calibration-registry.md` fallback to `corpus/knowledge/verification/calibration-registry.md`; `taboo-strata-lifecycle` dedups to 1 | `could-not-evaluate`; host passes |
| C4 | brace expansion before classification | 79 entries / 218 groups; `akan.md` → 16 direct; every expanded token classified separately | `could-not-evaluate`; host passes |
| C5 | Tier 1 three bases, direct precedence | entry-dir hit with two index hits → direct | `could-not-evaluate`; host passes |
| C6 | slash gate | `../linguistics/phonology-sanity.md` ×2 → unresolved; `linguistics/hero-journey-variants.md` → unresolved | `could-not-evaluate`; host passes |
| C7 | fallback mapping listed | 166 rows each `token -> corpus-relative path` | `could-not-evaluate`; host **fails** (totals-only census) |
| C8 | ambiguous ≥2 hits, no guess | injected 2-hit index → `ambiguous`, both hits named; live 0 | `could-not-evaluate`; host passes classify, no control |
| C9 | glob before Tier 2 | `-gate.md` with 0/1/2 injected hits → glob artifact, never fallback/ambiguous/unresolved | `could-not-evaluate`; host **fails** 1-hit and 2-hit probes |
| C10 | four classes only | `sound-change.md`/`tone-prosody.md` → `unresolved`, no `prospective` | `could-not-evaluate`; host **fails** (5 prospective) |
| C11 | per-entry dedup | `taboo-strata-lifecycle:21` counts once despite `:23`+`:37` | `could-not-evaluate`; host passes |
| C12 | no-drop arithmetic | per-entry counts sum to 2730; four-class findings 2729 + 1 glob; wrapped entry 4 = 2+2 | `could-not-evaluate`; host closes 2730 via six labels, not four |

## 6. Handoff / owed

- **O01 (owner of the missing draft):** when it lands, run C1-C12. Minimum
  fixes against the current host: drop/fold `prospective` into `unresolved`
  with named reasons; move glob classification before Tier 2; break on a blank
  line; add per-entry + fallback-mapping output. Keep the hyphen-aware join and
  the anchor/brace/slash/direct order — they are correct.
- **O02:** S8 currently has no teeth (empty index only). Add one-hit and two-hit
  glob indexes and assert the class in all three. S7a should add an
  **indented**-prose-after-blank fixture; the current non-indented prose passes
  a blank-skipping parser.
- **O03:** prediction agrees with my oracle exactly (2730 = 2556+166+0+7+1);
  keep the 7+1 split and the `tone-prosody.md` identity.
- **O04:** correct 49 → 79 brace entries; reconcile `unresolved=8` to 7 findings
  + 1 glob artifact (§5.6), or label the eighth row non-finding.
- **O06:** disposition leg should carry 166 fallback mappings, 7 unresolved rows
  with reasons (3 "sibling seed", 2 "prospective sibling", 2 X26-1 phantom
  carriers), and 1 glob artifact row; `ambiguous` has zero rows today.
- **Integrator:** re-run the census **after** the C landing. In-memory
  measurement of the r42 C01 spare's fenced block at HEAD: 30 couples tokens,
  all direct at the current index (one line, 3,820 chars); if applied
  unmodified, the forecast is 224 entries / 2760 raw rows / direct 2586 — label
  this a forecast, not a filed count, and re-run rather than copying it.
- `to-verify`: O01 conformance (absent); whether the hyphen-rejoin can over-join
  a legitimate field ending in `-` (no live case; the only wrapped field is the
  one measured); whether a later landing introduces a duplicate basename and
  activates the ambiguous branch (none at HEAD).

## 7. Citations

- Claim: `reports/round-43/claims.json:24-35` (O), `:28` four classes, `:34`
  thresholds; seat: `reports/round-43/targets.json:21`.
- Policy: `reports/round-42/calib/basename-couples-policy-full.md:14-25` (§1
  extraction, anchor at `:21-22`), `:27-48` (§2 two tiers/four classes), `:50-58`
  (§3 reporting), `:73-87` (§5.1 slash gate), `:89-92` (§5.4), `:97-103` (§5.6
  glob), `:220-233` (filed eleven-entry and Part 2 runs).
- Wrapped-field defect: `reports/round-39/calib/Ca04-verify.md:78-93` (D1 names
  the four targets incl. `tone-prosody.md`); r42 mangling/false-green:
  `reports/round-42/calib/Ca01-gap-fill.md:111-127,187-196`.
- Prior instruments: `reports/round-19/audit/entry-audit.py:31,34-42,75,87-95`;
  `reports/round-35/cov/C14-audit-6-10.md:227-236,249-288`;
  `reports/round-27/audit/entry-audit.py:129-131`.
- Host: `tools/harness/couples-reference-extractor.py:50-97` (block/join),
  `:134-150` (classify order), `:242-296` (selftest), `:298-330` (census).
- Live traps: `corpus/knowledge/linguistics/phonetics-phonology.md:72-77`;
  `corpus/knowledge/myth-symbol/sacred-kingship-mythic-charter.md:37`;
  `corpus/knowledge/linguistics/taboo-strata-lifecycle.md:21`;
  `corpus/knowledge/civilizations/akan.md:4`;
  `corpus/knowledge/verification/gate-frozen-run-standard.md:15`;
  `corpus/knowledge/verification/label-channel-routing-verification.md:14`;
  `corpus/knowledge/synthesis/typed-label-routing-workflow.md:16`;
  `corpus/knowledge/linguistics/language-contact.md:7`.
- Peer evidence: O02 `reports/round-43/op/O02-controls.md:57-71` (control
  matrix), O03 `reports/round-43/op/O03-predicted.md:10-21,125,407`,
  O04 `reports/round-43/op/O04-verify.md:128,164-176,235-270`.
- Digests (this seat, HEAD `7ceff59`): phonetics field file
  `b4f9b00384bc6840bdd1d7d7e7ae9bbb127a2fd1f5010c98d5b253df65d7776b`;
  policy `8c3d7c356ea7c1df3bcaab414ccc2035f6dc90272aaed305e4edf35b2890cdd6`;
  host `d8d23a265d12d290de69a6eb50454273af4ca699986812c6e203a030f4679cf1`.
- Command outputs: host `--selftest` 8/8 PASS exit 0; host `--census`
  `223/2730 -> 2556/166/2/5/1`; independent oracle `2730 -> 2556/166/0/7 + 1
  glob`; eleven-entry `334 = 319+15`; brace count `79` entries / `218` groups;
  anchor probe `18` distinct; synthetic fixture `6/6 PASS`; join variants
  (§2.5); glob-order probe (§3.3); boundary probe (§2.4).

No filed byte was edited; the only tracked-tree write from this seat is this
file (plus disposable `.scratch/o05/`). `git status --porcelain` at this cut
shows only the round-43 report tree as untracked. No `run-validation.py`, no
git mutation, no network, no install.
