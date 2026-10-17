# R11-O17 review — glossary quality of the round-11 handoff packet

- shard: HANDOFF R11-O17 (adversarial reviewer, targets O16–O18); claim O (operability).
- reviewer: kotodama round-11 worker (this file is the only file this shard wrote in the lane; scratch harnesses live under `.scratch/r11-o17-*` and `.scratch/o17-*`, gitignored).
- measured: 2026-10-17 19:05–19:13(-03) / 22:05–22:13Z, repo revision `e3ef1719c123ab4fb83ed94e033961dd61a2e8c7`.
- question put to this review: **are the exercise packet's 20 glossary entries genuinely derived from the live D2/D3 lexicon content, or are they generic / placeholder / fixture material?**

## Verdict

**Genuinely derived, 20/20, on every check this review can make mechanically** — and
**not generic**: no row is a placeholder, no row reuses the committed sample's fixture
lexicon (`fala`/`fano`/…), and every form, gloss, status and derivation statement in the
shipped rows was recomputed by this review from the live bytes and matched. Five findings
are reported below; **two are open defects in the exercise tool** (a broken `--selftest`,
and a latent false-claim predicate in the etymology generator), **two are minor
conformance divergences against `reports/round-11/handoff/design.md` §5**, and one was
resolved while this review was running (the missing frozen baseline). None of the open
findings invalidates the 20 shipped rows themselves.

## Artifacts reviewed (sha256 measured this session)

| artifact | sha256 |
|---|---|
| `tools/gates/expected/handoff-exercise/r11/packet.md` (the exercise's assembled packet, committed freeze) | `2a058f7858127b98592439594c55974d93e6e672a600dd2036b47e21e71c8a63` |
| `tools/gates/expected/handoff-exercise/r11/expected.json` | `1ab17670c113bf5f10a80f5ba564b252d948a836c3793efe641c68154d286b33` |
| `tools/exercise-handoff-e2e.py` (source of the rows) | `38d1cba429d98af79a14201d6cdf44150dd935314f4536003253f8f576b4f4c1` |
| `reports/round-11/handoff/design.md` (O01 design; §5 is the glossary rule) | `39012d479c6b466572a63931073f9bce07f9eceed2df9f89f3cd83ec932a54df` |
| `reports/round-11/handoff/shard-glossary.md` (O04 builder shard) | `ac6d1d54105368bdb9fff8d243bb9fb9cb4a53e4d1bfff1a0658dfd7321d4fe1` |
| `reports/round-11/handoff/packet-attempt-1.md` (O06, D3) | `289c8ca25bbebca7708f6a15fa9b9b2b7c985d9d809693c36f47dd657c383172` |
| `reports/round-11/handoff/packet-attempt-2.md` (O07, D2) | `d59053a10f155d7e66751f5a2fc8f6e15f40d807c9bfecf4778ae33cfe430d1a` |
| `reports/round-11/handoff/packet-attempt-3.md` (O08, D3 bases + D2 names) | `a5f28c20165c6964229782d7e49b37ee4bfcf4d8b17ce1f7c55445c28327e82b` |
| `reports/round-11/handoff/packet-attempt-4.md` (O09, D3 records across registers) | `eb7eddb56d966b233b90c68c2de5eed58b8e9d8ff57acf0a7edb2dab24ce856e` |
| `reports/round-11/handoff/tamper-control.sh` (O14 drill, current revision) | `4a43cb5a43c9e5abc4f727f94f7949aaa6a8ba2177f6178ed174af97edf9ea6c` |
| live sources: `examples/culture-d3/packet.json` / `examples/culture-d2/packet.d2.yml` / `examples/culture-d3/components/04-language.json` / `examples/culture-d2/components/05-lexicon.yml` | `bdf635ce…` / `e0f21509…` / `fee4ad61…` / (component view of the 40 records) |
| gate `tools/gates/handoff-packet-check.py` (matches the packet's own manifest row) | `e2fa3223b2aa57382807c51099a4360c1a9cc2559d5b4bedad1b54e9ab0ad575` |

Note: the committed freeze `tools/gates/expected/handoff-exercise/r11/{packet.md,expected.json}`
is **byte-identical** to the copy this review froze independently into
`.scratch/o17-freeze/` at 19:07 (before the lane's freeze at 19:08 existed) — the
verification below is therefore against the committed artifact, not a private variant.

## What "genuinely derived" is defined to mean here

A row passes only if all of the following are recomputed from live bytes by this
review's own code (no reuse of the exercise's comparison logic):

1. `entry_id` resolves to a live lexicon record (`packet.json.lexicon` / `packet.d2.yml`);
2. `E0`/`E1` cells equal the record's own `forms` block;
3. `E1` equals an **independent SC1 replay** (`p→f` initial, `ordinary` register; unchanged
   otherwise) computed from the live `sound_changes` record — checked via `from`, `to`,
   `environment`, `from_era`, `to_era`, `register`;
4. the gloss cell is the record's `gloss` **verbatim**;
5. the etymology's status token is inside the licensed vocabulary
   (`attested/reconstructed/constructed/contested/unknown`, glossary-registry-format.md §4);
6. for changed rows the cell actually names the law with its environment and register;
   for unchanged rows the no-trigger statement is **true** of the form;
7. the term cell is the live native form — not an English display label, not a space-bearing
   string, not one of the committed sample fixture's terms (`fala`, `fano`, … `keranali`);
8. no cell carries placeholder metasyntax (`TBD`, `lorem`, `<…>`, `n/a`, `xxx`).

Genericity is additionally measured: distinct terms, distinct glosses, and distinct
etymology "middles" after stripping the shared template, status prefix and citation.

## Method (commands, all run this session, TMPDIR=$PWD/.scratch)

```
python3 .scratch/r11-o17-glossary-audit.py <packet> --json <out>   # source resolution, fixture/placeholder sweep
python3 .scratch/r11-o17-rederive-d3.py <packet> --json <out>      # checks 1–8 above + SC1 replay
python3 .scratch/r11-o17-rederive.py <table> d2 --json <out>       # D2-side re-derivation of the O04 emissions
python3 .scratch/o04/frag_glossary.py --emit .scratch/o17-emit     # reproduce the O04 tables byte-for-byte
python3 tools/exercise-handoff-e2e.py                              # normal run against the committed baseline
python3 tools/gates/handoff-packet-check.py <control>.md           # my own negative controls
```

## Results

### 1. Exercise packet glossary (the artifact under review)

20 rows, ids `L01…L20` in live-lexicon order (checked as a sequence, not a set),
one per `examples/culture-d3/packet.json` `lexicon[]` record:

| check | result |
|---|---|
| id resolves to live record | 20/20 |
| E0 cell = live `forms.E0` | 20/20 |
| E1 cell = independent SC1 replay | 20/20 |
| gloss verbatim from live record | 20/20 |
| status token licensed | 20/20 |
| changed rows name the law (id, environment, register, both eras); unchanged rows' no-trigger claim true | 20/20 |
| term is the live native form (no display label, no space, not a sample fixture term) | 20/20 |
| distinct terms / glosses / etymology middles | 20 / 20 / 20 |
| placeholder sweep (all cells) | 0 hits |
| overlap with the sample packet's fixture terms | 0 |

The change/unchanged split is 4 changed (`L01, L04, L05, L06` — exactly the initial-`p`
records) and 16 unchanged, matching the live `sound_changes` record and the header note
`examples/culture-d3/handoff.md:110–113`. Distinctness confirms the rows are not a
template with substituted nouns: each etymology middle carries the record's own E0/E1
forms and quoted gloss.

### 2. The other candidate packets

All four O06–O09 attempts were swept with the same generic checks: every one of the 80
rows carries a licensed status token (80/80), and none contains a fixture term, a
placeholder, or an English display label in its form/term cell. Their 20-row composition
differs by design: attempt-1 = 20/20 D3 lexemes; attempt-2 = 2 D2 lexemes + 8 D2 names +
10 costume holds; attempt-3 = 12 D3 lexemes + 8 D2 names; attempt-4 = 11 D3 lexemes/names
+ utterances/symbols/rank records. The per-attempt detail:

- **attempt-1 (O06, D3)**: independently re-derived 20/20 on the same checks; its
  changed/unchanged phrasing ("no initial /p/") is also true of every row (20/20). It is a
  legitimate second D3 emission with slightly different prose.
- **attempt-2 (O07, D2)**: 20 rows of a **different shape** — 10 costume records with the
  form cell `no native form (owed)` (the live `D2L-FORM-UNRESOLVED` hold), 8 name
  compounds, 2 loan lexemes. Verified mechanically: the 8 names' bases resolve to live
  lexicon ids **and** concatenating the bases reproduces the form exactly (8/8, e.g.
  `sunel = su(L-08) + nel(L-02)`); all 8 forms appear in `13-naming.yml`; both loan rows
  (`L-26 kas`, `L-27 per`) match live gloss, route `loan` and donor form. The 10 GAR rows
  carry live costume glosses (10 distinct) with an explicit licensed `unknown` + reason —
  but their form cells are identical hold markers, **not lexicon entries**. Reading: not
  generic, deliberately honest, and correctly left as holds; however if the operator's
  phrase "20 entries genuinely derived from D2/D3 lexicon" is read strictly, attempt-2
  delivers 10 lexeme/name rows, not 20. That choice belongs to the parent (which packet is
  the packet of record), not to this review.
- **attempt-3 (O08, mixed D3 bases + D2 names)**: header `entry_id | system | E0 form |
  E1 form | gloss | etymology`; 20 rows = 12 D3 lexeme rows (ungrepped) + 8 D2 name rows
  (`NM-01…NM-08`). Every cell's status is licensed (20/20); no fixture terms, no
  placeholders. The lexeme rows carry "base of N0x" pointers, tying each name to the
  lexemes it is built from.
- **attempt-4 (O09, D3 records across registers)**: header `entry_id | register | form |
  gloss | etymology (derivation status for non-lexical records)`; 20 rows = 6 D3 names
  (`N01…N06`), 4 utterances (`U01…U04`, with the spoken/written split carried in the
  status cell), plus symbols/rank records. Licensed statuses 20/20; no fixture terms, no
  placeholders. The 6 name rows were checked against the live `names[]` records:
  concatenating the listed E1 bases reproduces the declared form for 6/6 (an independent
  replay of `formation.expected`), and the utterance rows correctly state the AV1/SC1
  register behaviour instead of inventing a lexical etymology.
- **O04 shard emissions** (`shard-glossary.md` §4/§5): I reproduced all three emissions by
  running the shard's own fragment into `.scratch/o17-emit/` — byte-identical, hashes
  `2cd5e352…` (d2-stratified-20), `56a070ec…` (d3-all-20), `b2970b43…` (d2-first-20),
  matching the shard's §6/§7 claims — and re-derived both 20-row D2/D3 tables from the
  live records with my own parser: 20/20 id, term, gloss, status, stage, route/bases,
  citation; 20 distinct terms and glosses. Source digests the shard pins
  (`e0f21509…`, `bdf635ce…`, `fee4ad61…`, `4e24bd3b…`) all re-measured equal.

### 3. Negative controls — where the gate is blind and this review is not

Each control is a copy of the committed frozen packet with exactly one mutation, run
through the shipped gate; then through this review's sweep.

| mutation | gate verdict | this review |
|---|---|---|
| blank etymology cell on `L01` | exit 1, `HO-GLOSS-ETYM` | caught |
| unlicensed status (`status: borrowed`) | exit 1, `HO-GLOSS-ETYM` | caught |
| `L01` term swapped to the sample fixture `fala` | **exit 0, no finding** | caught (`fixture_terms_reused: [fala]`, gloss mismatch) |
| gloss replaced by `TBD` | **exit 0, no finding** | caught (placeholder hit) |
| 10 of 20 rows deleted | **exit 0**, scan says `glossary-entries=10` | caught (row count 10 ≠ 20) |

This is the operative point for O16–O18: the gate checks presence and the status
vocabulary only; genericity, placeholder content and the entry count are **not**
gate-enforced, so the exercise's own assertions and reviews like this one are the only
defence there. The exercise does assert the count and compares the id sequence against
the frozen baseline (`exercise-handoff-e2e.py:855–868, 1100–1103`), and my controls
above confirm both blind spots are real.

## Findings

### F-O17-01 — RESOLVED (was: no frozen baseline; exercise unrunnable)

At 19:07 the committed baseline did not exist: a normal run printed
`exercise-handoff-e2e: CANNOT EVALUATE — gate not reached` and `--selftest` died with
`FileNotFoundError: …/tools/gates/expected/handoff-exercise/r11/expected.json`.
The O14/O15 freeze landed at 19:08; the normal run now passes end-to-end:
`exercise-handoff-e2e: PASS — fields=16/16 glossary-entries=20 findings=0` with
`frozen-packet`, `frozen-fields`, `frozen-glossary`, `contract-crossref` and
`component-digests 13/13` all `OK`. **No action needed on this item**; recorded because
the review's own first measurement (and this review's scratch freeze) predates it.

### F-O17-02 — OPEN DEFECT (tool, blocks the O-claim's selftest clause)

`python3 tools/exercise-handoff-e2e.py --selftest` **fails** as committed
(hash `38d1cba4…`):

```
AssertionError: ["evaluated: cannot hash examples/culture-d2/components/02-phonology.yml:
 [Errno 2] No such file or directory: '…/.scratch/handoff-selftest-…/fixture/examples/culture-d2/components/02-phonology.yml'"]
```

Cause: `FIXTURE_INPUTS` (`tools/exercise-handoff-e2e.py:1232`) copies only the five
`SOURCES`, the gate and the two assemblers into the throwaway fixture root, but the
exercise's own component-digest re-measurement reads the **component files** (the D2 15
components and D3 4 components, all present on disk, `examples/culture-d2/components/`)
that the assemblers recorded in `assembly.source_sha256`. The positive run of the
selftest therefore cannot reach the gate path. Owner: the O02–O05 single writer. This
blocks the O claim's clause "selftest with positive + malformed controls" until fixed;
the fix is to extend the fixture copy set to the component directories (or to the exact
component paths the digests name).

### F-O17-03 — OPEN DEFECT, LATENT (tool, etymology generator)

`derived_etymology` (`tools/exercise-handoff-e2e.py:311–327`) selects the SC1 branch by
`entry.get("id", "").startswith("L01") or e0 != e1` — a form-difference test, not a test
of the law's applicability. Demonstrated live by calling the shipped function via `runpy`
with synthetic records against the live `sound_changes` record:

| synthetic entry | emitted claim | truth |
|---|---|---|
| `e0 = pana`, `e1 = pana` (unchanged, but starts with the trigger) | "unchanged into E1 (no word-initial sound-change trigger)" | **false** — the form does start with the trigger |
| id `L011`, `e0 = e1 = suma` | "by SC1 initial /p/ > /f/ (ordinary register)" | **false** — dead `startswith("L01")` clause |
| `e0 = talu`, `e1 = tali` (changed for another reason) | "by SC1 initial /p/ > /f/ …" | **false** — SC1 does not produce this |

No shipped row is affected: the live lexicon's 20 rows happen to satisfy both predicates
consistently (this review's SC1 replay 20/20, no-trigger claims 20/20), and the packet's
input digests are pinned, so today's artifact is truthful. The risk is the generator: a
future live lexicon (or a re-freeze after a legitimate source change) can emit a false
derivation claim *and still pass the gate*, because the gate cannot read the law. Suggested
fix (owner O02–O05): predicate on `e0.startswith(sound_change["from"])`, assert
`e1 == replay(e0)` when the law applies (else `Unevaluatable`), and delete the dead
`startswith("L01")` clause.

### F-O17-04 — CONFORMANCE, MINOR (design §5's A-GLOSS manifest row absent)

`design.md` §5 requires a manifest row
`| A-GLOSS | §glossary payload (inline, this packet) | … | sha256:<packet.json digest> | 20 |`.
The frozen packet's artifact manifest (rows `A-D2-PACKET … A-TOOL-D3-ASSEMBLER`) has **no
glossary row**; payload identity lives only in the scope table row
(`| glossary payload | examples/culture-d3/packet.json | … | 20 constructed lexemes … |`)
and in `dependency_manifest`. Consequence: an auditor reading the manifest alone cannot
map the 20 rows to their source bytes; the gate does not enforce this. If the row is
added, it must contain the literal word `inline` — otherwise the gate routes it to
`INFO glossary-external` (`tools/gates/handoff-packet-check.py:447–462`, `:585–589`); the
committed packet currently emits no such INFO. Owner: the O02–O05 writer (or the design,
if the row is being dropped deliberately).

### F-O17-05 — CONFORMANCE, MINOR (emission wording vs design §5 row rule)

`design.md` §5 fixes the row rule as
`status: <status> — E0 *<E0> → E1 <E1> (<changed by SC1|unchanged into E1>); available_from <era>`.
The exercise's rows instead emit
`status: constructed — E0 *pina 'spoken pledge' → E1 fina by SC1 initial /p/ > /f/ (ordinary register); a constructed design derivation of the fictional variety, no real-language derivation claimed` —
i.e. they drop `available_from` (uniformly `E0` for all 20 live records), name the law with
environment and register, and append a no-real-language disclaimer. Content-wise the
emission is at least as informative and safer, but design and emission should agree:
either update §5's rule to the shipped wording, or add `available_from E0`. Owner: O01
(design) or O02–O05 (emission).

## Observations (non-blocking)

- **O-O17-06 (adjacent, not my scope) — RESOLVED while this review ran**: the O14 drill
  `reports/round-11/handoff/tamper-control.sh` at hash `72ace18d…` reported
  `tamper-control: 1 scenario(s) mismatched` (19:11, scenario T5 "revised gate bytes":
  observed exit 1 where it expected 0). The revised drill at hash `4a43cb5a…` (19:12)
  now reports `tamper-control: all scenarios matched their expectation`, with T5 reading
  "the exercise itself reports the same drift through the embedded artifact_manifest
  digest as exit 1". Re-run this session; no action for this review.
- **O-O17-07**: row-level provenance in the exercise packet is by `entry_id` plus the
  payload-level scope/manifest position; rows do not cite `examples/culture-d3/packet.json`
  inline. The O04 emissions do cite their source path per row. Cheap improvement if
  reviewer convenience matters.
- **O-O17-08**: the 20 glossary entries are **D3-only** (packet.json lexicon). This
  conforms to `design.md` §5 and to the O04 recommendation not to merge two cultures'
  lexicons under one `scope`; D2 nevertheless appears in the envelope (9 `culture-d2`
  path references: artifact manifest, dependency manifest, claim ledger, scope). The O04
  `d2-stratified-20` emission (D2, verified above) remains available if a D2-inclusive
  glossary is wanted — a design decision for the parent, not a defect.

## Limits of this review (`to-verify`)

- Structural only: I verified that glosses are the live records' glosses verbatim; I did
  not independently judge whether handing off exactly these 20 lexemes is the right set.
- The exercise's self-assertions about *behaviour* (isolated-copy run, input-digest
  refusal, re-freeze diff printing) were read in code and partially exercised; the lane's
  own falsifiability drill (O14) is the authority for them and now passes
  (`tamper-control: all scenarios matched`, hash `4a43cb5a…`).
- Findings F-O17-02/03/04/05 were measured against tool hash `38d1cba4…` and design hash
  `39012d47…`; both files are still moving inside the wave — re-check by hash before
  closing them.
- Attempts 3/4 landed during the review and are covered in §2 at the level of row
  composition, licensed statuses and the replayed name/utterance claims; the full
  per-row SC1/gloss re-derivation script (`.scratch/r11-o17-rederive-d3.py`) was run on
  attempts 1 and the frozen exercise packet, not on attempts 3/4, whose headers differ —
  re-run it (or the generic sweep) on whichever packet is integrated.

## Reproduction

All commands above are re-runnable from the repo root with `export TMPDIR=$PWD/.scratch`.
Evidence JSONs: `.scratch/o17-frozen-rederive.json` (committed frozen packet, 20/20),
`.scratch/o17-audit-exercise-packet.json`, `.scratch/o17-exercise-rederive.json`,
`.scratch/o17-audit-attempt1.json`, `.scratch/o17-attempt1-rederive.json`,
`.scratch/o17-audit-attempt2.json`, `.scratch/o17-audit-attempt3.json`,
`.scratch/o17-audit-attempt4.json`, `.scratch/o17-d2-rederive.json`,
`.scratch/o17-d3-rederive.json`, `.scratch/o17-ctl-*.json` (controls).

FILES: reports/round-11/handoff/review-17.md
SUMMARY: Independent re-derivation of the exercise packet's 20 glossary entries passes 20/20 on every mechanical check (live-source resolution, verbatim glosses, SC1 replay, licensed statuses, no fixture/placeholder/display-label content); two open tool defects (broken `--selftest`; latent false-claim predicate) and two minor design-§5 divergences reported, with the baseline-absence item resolved mid-review.
