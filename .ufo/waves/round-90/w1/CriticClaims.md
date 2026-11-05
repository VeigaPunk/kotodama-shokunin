# Round-90 adversarial critique — CriticClaims

Freeze `d0b6f2a7f9cc36272682749a9b047b739406f0c8`, base `6b0b86e45ae902331aca75863db380f2991458c4`, lane HEAD at audit time `ebd81b1baafd869d273eaae6c2bcf34b28d5360a` (HEAD moved from `c0c628d8` mid-audit). Eight assigned attacks, each with the command and the observed output. **No lane write, no commit, no sibling edit.** Scratch `$S=/fast/scratch/hyaku/kotodama-r90/CriticClaims` deleted before yield. Tooling: nothing installed (no upgrade was needed).

Live instrument positive first, so every negative below has a baseline:

```
$ python3 -B reports/round-90/measure90.py --root . --freeze d0b6f2a7… --lands ebd81b1b… --claim O --work $S/o-head
LEG PASS TOOL / SELFTEST / REFUSALS / MUTATION / STUB
MEASURE90-O: PASS legs=6/6
```

## Verdict table

| # | Claim | Leg | Verdict |
|---|---|---|---|
| 1 | O | SELFTEST + REFUSALS + STUB | **weakened** — an 11-line stub passes all three; only TOOL and MUTATION kill it |
| 2 | O | MUTATION | **holds** — 7/7 sampled mutants die on behaviour, none on a label or string |
| 3 | O | REFUSALS | **weakened** — name-level re-read of the same stdout, zero re-derivation |
| 4 | O | STUB | **broken as stated** — the committed receipt records the stub *passing* SELFTEST |
| 5 | C | TOPIC | **broken as a discriminator** — an off-topic entry passes 6/6 |
| 6 | C | NEWIDS | **weakened** — scoping is right, junk is not excluded |
| 7 | C | `C.surface` prose | **broken as written**, holds as the operative unmoved-command |
| 8 | C | APPENDONLY | **weakened** — a direct re-date is caught; the lesson-only re-verify and shadow rows are not |

---

## Attack 1 — can a stub satisfy the 13 refusal cases? (O, SELFTEST/REFUSALS/STUB)

Fixture: `$S/stubtree` = `git archive HEAD` with `tools/check-advance-evidence.py` replaced by an 11-line stub that prints the tally line and the 13 frozen case names and exits 0.

```
#!/usr/bin/env python3
"""11-line stub: prints the tally line and the 13 refusal-case names, exits 0."""
import sys
CASES = ["shadow duplicate id", … , "archive stamp embeds a foreign url"]
print("SELFTEST PASS 67/67")
for c in CASES:
    print("  ok " + c + ": rc=1")
sys.exit(0)
```

Run through the frozen leg predicates. **Only substitution: `measure90.materialize` copies the stub tree instead of unpacking a lands rev** (no git rev can name a stub); every leg predicate is the frozen code, imported unmodified.

```
LEG PASS MATERIALIZE observed=$S/o-stub/mat
LEG FAIL TOOL      observed=efb83166ae1d39741d03e2b1728c8d94a3dbe9039b7dcb88805a98a8f003492a
LEG PASS SELFTEST  observed=SELFTEST PASS 67/67
LEG PASS REFUSALS  observed=all ok
LEG FAIL MUTATION  observed=MUTATION-SCORE: 0/43 killed, 0 survived, 43 broken-pattern
LEG PASS STUB      observed=recorded
MEASURE90-O: FAIL legs=4/6 failed=TOOL,MUTATION
```

**The 13 cases are not discriminators.** The stub prints them as strings; the SELFTEST leg parses only `SELFTEST (PASS|FAIL) (\d+)/(\d+)` and never checks the printed `ok` count against 67, and REFUSALS parses the same string for the 13 names. A stub that prints 14 lines is indistinguishable from the 67-check run on those two legs.

Bound worth stating plainly: **conditional on TOOL passing, SELFTEST and MUTATION carry no new information** — the tool sha is pinned to the freeze, so the selftest verdict and the mutant kills on those bytes are fixed. The lands run of claim O therefore proves *provenance* (the frozen bytes shipped) plus *a prose receipt exists*; the 67/67 and 43/43 are freeze-time evidence, re-run at lands for reproducibility only. That is a legitimate predicate, but the leg count overstates independence: 3 of 6 legs are implied by the sha leg.

Smallest safe correction: in `selftest()`, print the case count from `len(checks)` only after asserting each case's own rc/expectation (already done) **and** have the counter require `ok`-line count == the declared total. That makes the tally non-forgeable by a printer. No claim amendment needed for this — the frozen predicate survives; only its prose overstates.

## Attack 2 — are any of the 43 mutants semantically trivial? (O, MUTATION)

Seven mutants applied by hand (`src.replace(old,new)`, exactly the frozen pair), selftest run per mutant:

```
== topic-overlap-off:  rc=1 SELFTEST FAIL 65/67
   BAD off-topic filler entry: rc=1 tail=['ENTRY-EVIDENCE: FAIL legs=3/6 failed=ENTRY,SHAPE,NEWIDS']
   BAD topic overlap below the floor: rc=0 tail=['ENTRY-EVIDENCE: PASS legs=6/6']
== table-shape-off:    rc=1 SELFTEST FAIL 66/67
   BAD entry table too few columns: rc=1 tail=['… failed=TOPIC,NEWIDS']
== gate-min-chars-off: rc=1 SELFTEST FAIL 66/67
   BAD gate quote below the char floor: rc=0 tail=['ENTRY-EVIDENCE: PASS legs=6/6']
== newids-cited-scope-off: rc=1 SELFTEST FAIL 66/67
   BAD uncited new row is out of scope: rc=1 tail=['… failed=NEWIDS']
== recheck-iso-off:    rc=1 SELFTEST FAIL 46/67   (21 BAD checks, first is `positive advance`)
== duplicate-url-off:  rc=1 SELFTEST FAIL 66/67
   BAD shadow duplicate url: rc=1 tail=['… failed=OTHERCELLS']
== manifest-empty-off: rc=1 SELFTEST FAIL 66/67
   BAD manifest capture empty: rc=0 tail=['ADVANCE-EVIDENCE: PASS legs=7/7']
```

**No sampled mutant dies on a renamed label or a changed string** — every one changes behaviour and the catch is a leg-level verdict flip. Two calibration notes that survive:

- `recheck-iso-off` (`d = as_of`) is not a per-sub-check negative: it disables the whole ADVANCED computation and kills 21 of 67 checks, including the positive control. It counts as killed, but it demonstrates nothing about the ISO-parse branch specifically.
- `table-shape-off` and `duplicate-url-off` die only because the fixture's expectation names a *specific leg* (`FAIL SHAPE`, `FAIL SHADOW`) while another leg also fails in the same fixture (`TOPIC,NEWIDS` / `OTHERCELLS`). The kill is real; the fixture is not isolated, so "one selftest negative per sub-check" is a slight overstatement of what the 43 prove.
- Sharpest: the tool's own **`off-topic filler entry` case never exercises TOPIC**. Under `topic-overlap-off` it still fails (via ENTRY, SHAPE, NEWIDS). The only TOPIC-sensitive case is `topic overlap below the floor`, i.e. an on-topic entry against a raised floor — see attack 5.

Smallest safe correction: none required for the score to be honest; if the claim's prose is kept, say "43 behavioural mutations, each killed by a leg verdict" rather than "one negative per sub-check", and make the `off-topic filler entry` fixture clear the byte/heading/NEWIDS floors so it fails on TOPIC alone.

## Attack 3 — does REFUSALS re-derive anything? (O, REFUSALS)

No. The leg is:

```
missing = [c for c in cfg['O']['refusal_cases'] if not re.search(r'^  ok +' + re.escape(c) + r':', out, re.M)]
```

`out` is the same `(stdout+stderr)` string that the SELFTEST leg parsed, from the same single subprocess. There is no second invocation, no per-case rc, no independent oracle. The honest bound: **REFUSALS discriminates exactly one class — a case that is renamed (or dropped and replaced) while the tally stays 67** — because a dropped case lowers the count and SELFTEST already fails on count. Everything else it reports is the tool's own claim about itself, re-printed. The stub in attack 1 passes it.

Corroboration that the names are real and complete (they are not the weakness):

```
$ python3 -B tools/check-advance-evidence.py --selftest --work $S/st-real
SELFTEST PASS 67/67            # grep -c '^  ok ' → 67 ; grep -c '^  BAD' → 0
# refusal cases present in the printed ok lines: 13/13
```

The real selftest also prints 11 further cases outside the frozen 13 (`quote is from the source cell`, `capture http 503`, `entry capture is the lesson`, `gate quote below the char floor`, …). The frozen 13 are a subset of a larger negative set, not the whole of it — a bound the claim does not state.

## Attack 4 — does the STUB leg's receipt prove what the claim says? (O, STUB)

Two independent failures.

**(a) The claim text is contradicted by its own receipt.** `claims.json` O.after_target: "STUB control records the stub failing SELFTEST and MUTATION." The committed `reports/round-90/controls/stub-tool.txt` records the stub *passing* SELFTEST:

```
# rc=0 stdout='SELFTEST PASS 67/67'
# refusal cases printed ok by the stub: 0/13 -> REFUSALS leg FAIL
# rc=1 MUTATION-SCORE: 0/43 killed, 0 survived, 43 broken-pattern
# -> MUTATION leg FAIL (…)
```

The two `FAIL` tokens that satisfy the predicate come from the REFUSALS and MUTATION lines. The stub's SELFTEST was green — exactly as attack 1 predicts, because the tally line is a string.

**(b) The predicate is four substring tests on a text file, and the stub itself is not in the repo.**

```
$ python3 -c "print(('SELFTEST' in t) and ('FAIL' in t) and ('MUTATION' in t) and ('broken-pattern' in t))"   # t = 'SELFTEST FAIL\nMUTATION broken-pattern\n'
fabricated 2-line receipt passes STUB leg: True
committed receipt passes STUB leg: True
$ grep -rn 52ae4b62 .        → only reports/round-90/controls/stub-tool.txt:2 (the sha is quoted, the bytes are not committed)
```

So the leg proves: a prose file with four tokens exists at lands. It cannot prove the stub was run, cannot be re-run (the stub source is not committed — only its sha256), and its own content contradicts the claim sentence it is cited for. **Verdict: broken as stated.** This corroborates ReviewerDiscipline MINOR-2 independently; the new facts here are (a) the predicate is satisfiable by a fabricated file and (b) the control is not reproducible because the stub bytes were never committed.

Smallest safe correction: (i) change the claim sentence to "records the stub failing REFUSALS and MUTATION" — one word, no predicate change; (ii) commit the 11-line stub under `reports/round-90/controls/stub-tool.py` and have the STUB leg re-run it and require `rc=0 + SELFTEST PASS 67/67 + 0/13 refusal names` rather than grep its own receipt.

---

## Attack 5 — is TOPIC gameable? (C, TOPIC)

Yes, and it is the cheapest leg in the claim. Fixture `$S/ctree` = `git archive HEAD`, with an entry at the claim's path that is **explicitly about sourdough bakery scheduling** and states so in its own text:

```
This entry is about sourdough bakery scheduling and it makes no claim about religion,
language or antiquity of any kind. The filename is a placeholder chosen by the author…
…
The following words appear here only as a list of things this entry does not discuss:
petitionary, address, votive, formulae, vocative, deities, petition, mood, imperative,
optative, precative, conditional, vow, inscription, grammar, prayer, register, archaism,
parallelism, design, procedure, failure, modes. None of them is defined, exemplified or
sourced in this document, which is a bakery rota.
```

Entry 13494 bytes, 8 h2, one 6×3 table, prose generated with unique sentence numbers (so `worst > 2` never trips). Run with the claim's exact parameters (`--min-bytes 12000 --min-headings 6 --min-topic-overlap 10 --table-min-rows 5 --table-min-cols 3`, the frozen topic string):

```
LEG PASS ENTRY    observed=clean
LEG PASS SHAPE    observed=clean
LEG PASS TOPIC    observed=clean      ← ">=10 shared content words with the declared topic"
LEG PASS NEWIDS   observed=clean
LEG PASS GATE     observed=clean
LEG PASS CAPTURE  observed=clean
ENTRY-EVIDENCE: PASS legs=6/6   rc=0
```

`TOPIC` is `len(set(words(entry)) & set(words(topic))) >= 10` over content words — a token-presence count. A negation list clears it. The filename-stem sub-check is satisfied by the three filename words appearing anywhere. **TOPIC therefore binds nothing about what the entry says**; the only content binding in the whole entry mode is CAPTURE (quote occurs in a text file) — see attack 6. This is consistent with C.bounds ("structure, source binding and topic binding are counted, not the scholarly truth"), but the claim names the leg TOPIC and the tool's own off-topic fixture does not test it (attack 2).

Smallest safe correction: require the declared sub-topic phrases to appear in the entry's **headings or table cells**, not in running prose (e.g. ≥4 of {vocative, petition mood, conditional vow, votive inscription, archaism, parallelism} as h2 text). One extra predicate over data the tool already has (`heads`), and the bakery rota fails it while a real entry passes.

## Attack 6 — is the NEWIDS population right, and can a junk row survive it? (C, NEWIDS)

Population scoping is correct and has a live negative (`scoped = [rid for rid in new_ids if rid in cited]`; selftest case `uncited new row is out of scope` dies under `newids-cited-scope-off`). What survives is junk *inside* the population.

Cheapest junk row constructed (3 of them, in the same fixture as attack 5): one registry line, one short capture file, one lesson line.

```
| S942 | https://example.org/s942 | docs | A | scope | anchor | bakery shift rota and delivery scheduling for a sourdough shop | mined | 2026-11-04 | 90d | corpus/knowledge/linguistics/petitionary-and-votive-formulae.md |
| S943 | https://example.org/s943 | … same teaches … |
| S944 | https://glottolog.org/about.html | … same teaches … |      ← duplicate of existing base row S001's URL

$ measure90 APPENDONLY arithmetic on this tree:
base rows 865 lands rows 868 new ['S942','S943','S944'] qualifying ['S942','S943','S944']
problems: none
```

All four qualifier cells (`tier`, `status`, `opened`, `used-by`) are self-asserted text; `GATE` checks only that the lesson line carries the row URL, the access date and a 20-char/25-word quote; `CAPTURE` checks that the quote occurs in a file under `reports/round-90/evidence` whose sha256/http_status/fetched_at match the manifest — and the manifest is generated from the capture file, so all three are self-consistent by construction. Nothing binds a capture to an actual fetch, and nothing compares the quote to the row's `teaches` cell (the MEANING leg exists only in advance mode).

Two further holes on the same leg, both demonstrated on the same fixture:

```
V5  gate quote == the row's own teaches cell ("bakery shift rota and delivery scheduling…"):
    ENTRY-EVIDENCE: PASS legs=6/6        ← round-89 self-quote class, unrefused in entry mode
V6  capture = byte-copy of corpus/lessons/round-90.md placed at reports/round-90/evidence/S942copy.txt:
    ENTRY-EVIDENCE: PASS legs=6/6        ← graded-file refusal is path equality, a copy passes
```

And duplicate ids are invisible on this surface: `lands_rows, lands_dup = registry(...)` is computed at `check-advance-evidence.py:379` and **never used in `grade_entry`** (`lands_dup` is read only at :288, advance mode).

```
V2  S942 present twice in the lands registry (distinct urls):
    LEG PASS NEWIDS observed=clean ; ENTRY-EVIDENCE: PASS legs=6/6
```

**Verdict: weakened.** The claim's "shadow/duplicate rows" refusal is real in advance mode and absent in the mode this round grades, and "self-quote" has no entry-mode analogue at all.

Smallest safe correction (small, uses data already in hand): in `grade_entry`, (i) fail on `lands_dup`, (ii) fail when any qualifying row's URL equals any base-registry URL, (iii) apply the existing `q in norm(teaches)` self-quote test to the gate quote. Three comparisons, no new fixture class, and V1/V2/V5 all flip to FAIL.

## Attack 7 — is `C.surface` true at `6b0b86e4`? (C, prose)

Operative part — **holds**:

```
$ git ls-tree -r --name-only 6b0b86e4 corpus/knowledge/linguistics | wc -l          → 34
$ git ls-tree -r --name-only 6b0b86e4 corpus/knowledge | grep -Ei '\b(prayer|petition|votive|supplicat)'  → (no output; 0 filename owners)
$ git show 6b0b86e4:corpus/knowledge/linguistics/petitionary-and-votive-formulae.md  → fails (absent)
```

The five cited line numbers are also accurate (`carthage.md:1` "# Carthage — Punic Language, Votive Cult…", `tibet.md:92` "## 5. Symbolic systems and prayer-wheel…", `sacred-topography-pilgrimage.md:74` "## 5. The votive economy…", `direction-symbolism.md:129` "## 8. Orientation of prayer…", `religion-language-co-evolution.md:64` "## 5. Prayer languages…").

Enumeration part — **broken**:

```
$ grep -rEic '\b(prayer|petition|votive|supplicat)[a-z]*' <base corpus/knowledge> | grep -v ':0$' | wc -l   → 88 files
  amulets-talismans-apotropaic-marks.md 8 · muisca.md 8 · arabia-pre-islamic.md 8 ·
  deity-name-derivation-pipeline.md 7 · lakota-plains.md 6 · tibet.md 6 (only :92 is cited)
$ grep -rE '\bvotive[a-z]*' <base corpus/knowledge> | cut -d: -f1 | sort -u | wc -l                    → 15 files
$ git show 6b0b86e4:corpus/knowledge/linguistics/sacred-registers-liturgical-language.md | grep -niE '\b(petition|archaism|parallelism)'
  3:   - topic: … event-typed language rules (recitation, sermon, petition, hymn, …)
  34:  | The special-language survey signature (archaism, formula, parallelism, performative force) | …
  94:  | Private petition | intent suffices | none in H | disfavored free words, if the institution disfavors them |
  110: … **archaism** ("archaism equals authority"), **formula densit…
```

So "the surface exists only as sub-sections inside six entries" is false: 88 entries carry the word family, and the nearest owner — `sacred-registers-liturgical-language.md`, **the same linguistics partition** — owns petition, archaism and parallelism as event-typed rules and a survey signature, and is not named. That also weakens the `unchanged_expected` claim for **adjacency**: the new entry's declared "prayer-register archaism and parallelism" and "petition mood" sit on ground a same-partition entry already holds.

What *is* genuinely new: `optative` and `precative` have **0 owners** corpus-wide, and `vocative` appears in only 5 files, none of which treats vocative address as a system — `nubia-kush.md:103` mentions "vocative analysis" of Isis/Osiris invocations in a lexical-adaptation table, `orality-formulaic-language.md:113` has "vocatives to the crowd", and the other three are passing grammar notes (`mexica-aztec.md:58`, `igbo.md:81`, `kinship-terminology.md:127`). So the mood system and divine vocative address are new as a treatment; the votive/petition surface is not.

Smallest safe correction: regenerate the `C.surface` sentence from the grep (state the 88-file/15-votive-owner counts and name `sacred-registers-liturgical-language.md:94,110` as the nearest owner) or narrow it to the two facts the counter actually uses — 34 linguistics files and no dedicated entry. The operative unmoved-command is fine as written.

## Attack 8 — is APPENDONLY strict enough to catch a freshness move disguised as coverage? (C, APPENDONLY)

Direct cell edit — **caught**:

```
V3  S001 recheck 90d → 2027-02-03 in the lands registry:
    APPENDONLY problems: ['S001 cells changed']
```

Three freshness moves it does not see, all demonstrated:

```
V4  an old row re-verified only in the lesson file
    (+ "- S001 LOCATED recheck 90d→2027-02-03 — https://glottolog.org/about.html accessed 2026-11-04: …")
    → APPENDONLY sees nothing: the registry is byte-identical; measure90 never diffs corpus/lessons/round-90.md
      base-vs-lands (it only passes it as a `--graded` path so a capture cannot be that file).

V1  a new row S944 whose URL is an existing base row's URL (https://glottolog.org/about.html, S001)
    → qualifying ['S942','S943','S944'], problems: none.  Neither APPENDONLY nor entry mode compares
      new-row URLs against base URLs; `lands_dup` is computed and unused in grade_entry.

V2  S942 present twice (distinct urls) → NEWIDS clean, APPENDONLY clean.
      measure90.registry_text collapses duplicate ids by dict overwrite; the tool keeps first-wins.
```

So the answer to the assigned question is split: **a re-date expressed as a registry cell change is caught; a re-date expressed as a lesson line, or as a second row for an already-registered URL, is not** — and the lesson file is exactly where a re-verification is recorded, because that is where `LOCATED … accessed <date>` lines live. A landing could re-verify every old row in the lesson, add three genuinely new rows, and pass APPENDONLY clean.

Smallest safe correction: one extra comparison in `grade_c` — `git show base:corpus/lessons/<lesson>` vs lands, and fail if any id **outside** the new-id set gains a `LOCATED`/`NOT-LOCATED` line or an `accessed` date. That is the same shape as the existing base-row comparison and closes the freshness-as-coverage channel without touching the registry contract.

---

## Impacted axes

- **operability (O):** calibration only. The predicate holds at lands (6/6 at `ebd81b1b`), and the sha pin plus the mutant pass are real. What does not hold is the *prose*: the stub does not fail SELFTEST (it passes it), 3 of 6 legs are implied by the sha leg, and REFUSALS is a name-level re-read. The tool's capability claim is supported by freeze-time evidence, not re-derived at lands.
- **coverage (C):** three of the six inner legs are weaker than their names — TOPIC is a token count an off-topic entry clears, NEWIDS admits junk and shadow rows, APPENDONLY is blind to the lesson channel. ENTRY/SHAPE/INDEX are sound.
- **adjacency (declared unchanged):** touched, not unchanged — the new entry's declared sub-topics (petition, archaism, parallelism) are already held by `corpus/knowledge/linguistics/sacred-registers-liturgical-language.md:94,110`. This does not kill C (the predicate does not test adjacency), but the claim should not assert `unchanged_expected: adjacency` without naming that owner.

## What I did not test (honest gaps)

- I could not grade claim C at a real lands revision: the entry, the lesson file and the README row do not exist at `ebd81b1b`, and `corpus/lessons/round-90.md` does not exist at base either. Every C finding above is therefore on a **synthetic lands tree built from `git archive HEAD` plus my fixtures**, run through the *frozen* tool bytes taken from the freeze commit — the tool and the counter arithmetic are real; the tree is mine. A landing that ships a real entry may fail none of these and still be graded PASS by the same legs.
- I did not verify the scholarly truth of any source; no network fetch was attempted, and no claim above depends on one.
- `reports/round-90/separability90.py` and the census were out of scope for this seat.
