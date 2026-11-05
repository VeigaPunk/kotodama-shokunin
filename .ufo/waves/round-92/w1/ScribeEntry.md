# ScribeEntry — round-92 coverage entry on ideophones and mimetic vocabulary

Seat: ScribeEntry-22 (scribe). Lane: kotodama. Round 92, wave 1. Milestone r92-v1.
Date: 2026-11-05.

## Files written

| path | bytes | sha256 |
|---|---|---|
| `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-92/w1/stage/ScribeEntry/entry.md` | 28814 | `2521a3d16086e219686028dd69eaa487f187b97a9e42eba7f16f6cd7dfd010d9` |
| `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-92/w1/ScribeEntry.md` | this report | — |

The stage file is the deliverable; the L1 copies it byte-for-byte to
`corpus/knowledge/linguistics/ideophones-mimetics.md`. Nothing outside the stage dir and this
report was written in the lane repo. Scratch dir `/fast/scratch/hyaku/kotodama-r92/ScribeEntry/`
is deleted at yield.

## Numbers measured (all commands and exit codes below)

| measure | observed | frozen floor | command | rc |
|---|---|---|---|---|
| entry bytes | 28814 | >=12000 | `wc -c .ufo/waves/round-92/w1/stage/ScribeEntry/entry.md` | 0 |
| `## ` heading count | 12 | >=6 | `grep -c "^## " <entry>` | 0 |
| header keys | `topic:`, `sources:`, `verified-at:`, `recheck:` all present; `verified-at: 2026-11-05` | all four | grader ENTRY leg | 0 |
| table shape | 23 data rows x 5 cols (three tables: typology 9x5, integration 5x4, naming 5x4) | >=5 data rows x >=3 cols | `tools/check-advance-evidence.py` SHAPE leg | 0 |
| prose/topic content-word overlap | 27 | >=10 | grader TOPIC leg | 0 |
| filename words present | `ideophones` hit, `mimetics` hit (2/2) | >=1 | grader TOPIC leg | 0 |
| sub-topic phrase anchors | 6/6 present: ideophone, mimetic, onomatopoeia, depictive, expressive, sound-symbolic | >=4 of 6 | grader TOPIC leg | 0 |
| anchor span | 10 heading/table surfaces (9 headings + table rows) | >=3 | grader TOPIC leg | 0 |
| ids cited | S957, S958, S959, S960 — no other id anywhere in the file | only these four | grader NEWIDS leg + regex sweep | 0 |
| lines carrying >1 distinct id | 0 | 0 (QUALITY 15) | `python3 -B tools/check-cited-lines.py <entry>` | 0 |
| table rows carrying an id | 0 | 0 (QUALITY 15) | same lint | 0 |
| worst repeated prose sentence | 1 | <=2 | grader SHAPE leg | 0 |
| to-verify marks | 0 | — | `python3 -B tools/gates/provenance-audit.py <entry>` | 0 |

## Frozen-instrument verification (not just a local re-implementation)

The entry was graded by the **freeze-pinned** `tools/check-advance-evidence.py` (sha256
`905be2fe…`, the frozen v3), entry mode, with the floors read from `reports/round-92/claims.json`
section C:

```
LEG PASS ENTRY      observed=clean
LEG PASS SHAPE      observed=clean
LEG PASS TOPIC      observed=clean
LEG PASS NEWIDS     observed=clean
LEG PASS UNIQUENESS observed=clean
LEG PASS GATE       observed=clean
LEG PASS CAPTURE    observed=clean
LEG PASS APPENDONLY observed=clean
ENTRY-EVIDENCE: PASS legs=8/8
rc=0
```

The frozen counter `reports/round-92/measure92.py --claim C` was then run over a fixture clone
(base `21350361500aa000b90f91082bf9d7295a9c24cd`, freeze `066b9728fc64e78735769c4740d05c1000d31a3b`,
lands a fixture commit carrying this entry plus the four registry rows, the round-92 lesson gate
lines and the README row):

```
LEG PASS MATERIALIZE observed=…/work/mat
LEG PASS ENTRY       observed=clean
LEG PASS INDEX       observed=CORPUS-INDEX: OK files=264 rows=264 findings=0
LEG PASS APPENDONLY  observed=clean
MEASURE92-C: PASS legs=4/4
rc=0
```

`tools/check-corpus-index.py --root <fixture>` → `CORPUS-INDEX: OK files=264 rows=264 findings=0`,
rc 0.

**Negative controls** (to show the fixture is not vacuously green): a variant with the phrase
anchors stripped → `FAIL TOPIC` (phrase anchors 4/6, filename words absent) + `FAIL NEWIDS`, rc 1;
a variant with the S960 line removed → `FAIL TOPIC` + `FAIL NEWIDS`, rc 1. Both controls fail for
the right reason, so the pass is discriminating.

## Commands run (with rc)

```
python3 -B tools/check-advance-evidence.py entry --root <fixture> … --rc 0 (8/8 legs)
python3 -B tools/check-corpus-index.py --root <fixture>                       rc 0
python3 -B tools/check-cited-lines.py <stage entry>                           rc 0 (0 findings)
python3 -B tools/gates/provenance-audit.py <stage entry>                      rc 0 (0 findings)
python3 -B reports/round-92/measure92.py --root <clone> --freeze 066b9728… \
    --lands a76aa39f… --claim C --work <work>                                rc 0 (4/4 legs)
sha256sum over the four committed captures vs manifest.json                  rc 0 (4/4 match)
```

## Ids cited, and how each is bound

Only the four ids frozen for this round appear in the entry, and each appears on its own line:

- **S957** — Marsault, Lahaussois & Treis 2024, "Ideophones: honing in on a descriptive and typological concept", *Linguistic Typology at the Crossroads* 4-1: 1-13, tier A. Carries the typological definition, the word-class-status debate, the ideophone/onomatopoeia/interjection boundary relations, the label traditions, and the survey of integration patterns.
- **S958** — Treis 2024, "Ideophones in Kambaata (Cushitic)", *Linguistic Typology at the Crossroads* 4-1: 147-200, tier A. Carries the Cushitic grammar: language-internal definition, support verbs, phonotactics, derivation, semantics, and the 162/31 frequency figures.
- **S959** — Meyer 2024, "Ideophones and verbal constructions with the verb 'say' in Amharic", *Linguistic Typology at the Crossroads* 4-1: 201-243, tier A. Carries the Ethiosemitic grammar: the coverb plus light verb analysis, the noncausal/causal contrast, and the intensive/attenuative derivation templates.
- **S960** — Benítez-Burraco 2026, "Sensitivity to ideophones by child non-native speakers increases with age", *Frontiers in Language Sciences* 5, tier A. Carries the acquisition and processing material.

Locates verified in the committed captures (all four capture sha256 match `manifest.json`):
`[a] member of an open lexical class of marked words that depict sensory imagery` (S957);
`Ideophones are defined in Kambaata as an open word class of morphologically invariant lexemes…`
(S958); `complex predicates consisting of an invariant coverb followed by an inflecting light verb…`
(S959); `Sound-symbolic effects have been claimed to facilitate word learning…` (S960, present in the
visible abstract body text, not only in a meta tag).

## Figures kept exactly as sourced (L1 fix item 3)

- Kambaata frequency: 13 ideophone types and 73 tokens across 11,851 words in a translated Gospel,
  about one ideophone per 162 words, against about one per 31 words in a 1,135-word conversation
  (S958).
- S960 sample: 64 Spanish children, 29 boys and 35 girls, six groups across three grades, ten or
  eleven children per group, one school in Cádiz; 30 ideophones from five languages in five
  families; only the sixth-grade children above chance in both tasks (p = 0.0002 words, p = 0.017
  pictures); age effect only on the word task (p = 0.0053); no sex effect and no ideophone-type
  effect; youngest group could not do the written-word task and was given the picture version
  (S960).

## Structure delivered

12 `## ` sections: scope/ownership; the typological definition; the label traditions; the
onomatopoeia/expressive/interjection boundary; a 9-row **typology table** of how the class
integrates grammatically across nine languages/areas (predicated, adverbial, holophrastic,
quotative-only, and the negative case); the Cushitic grammar; the Ethiosemitic grammar; sensory
semantics and the depictive field hierarchy; acquisition and processing; a **ten-step design
procedure**; two **decision tables** (integration mode → class marker → syntax → failure mode;
label chosen → claim committed to → claim refused → typological precedent); and a closing
boundaries/calibration/handoff section.

Worldbuilder-usable, not an essay: the typology table and both decision tables are keyed on
choices, and each procedure step names the evidence it rests on.

**Boundary named (adjacent owner).** `sound-symbolism.md` stays authoritative for sound-symbolic
token effects — the cross-linguistic shape-sound biases, the bouba/kiki complex, the frequency code
and phonestheme banks. This entry restates none of it and makes no claim about sound-symbolic
effects on individual words. The single point of contact is the acquisition question in §9, read
narrowly. The `- couples:` header names `sound-symbolism.md` as owner, with
`register-lexicon-ceilings.md` (a pointer, not an owner), `phonetics-phonology.md`,
`orality-formulaic-language.md`, `semantics-pragmatics.md` and `synthesis/myth-to-language-derivation.md`.

**Handoff boundary.** The entry ends at the handoff: the deliverable is method (typology table,
two decision tables, ten-step procedure). The five decisions left to the receiving world are named
as open — label, integration mode, class marker, sensory domains, frequency budget. No canon
decision is taken; the in-world belief that a depicting word does what it sounds like is routed to
the myth and synthesis entries, not asserted here.

## Recheck cadence chosen

**180 days**, matching the `180d` recheck cell carried by the round-91 registry rows this entry's
neighbours use, and recorded in the entry's own `- recheck:` header. `- recheck-scope:` states the
trigger: re-open the four captured surfaces and re-locate the quoted spans before the entry is
used as the basis for a real language design.

## Deviations and reconciliation notes (for the L1)

1. **`- sources:` header (L1 fix item 1) — implemented in the round-91 house style, not as inline
   `S957 S958 S959 S960`.** Putting all four ids on one line is exactly the MULTI-ID shape that
   QUALITY criterion 15 and `tools/check-cited-lines.py` refuse, and the L1's own fix item 2 asks
   for one id per cited line. The two instructions conflict, so the one-id-per-line rule won.
   Resolution: the header line is non-empty (`- sources: the four sources mined this round, one per
   line below; each line carries exactly one S-id …`) and each of the four ids follows on its own
   indented line. This is byte-compatible with `corpus/knowledge/linguistics/secret-and-ludic-languages.md`
   (the round-91 entry, which passes the same lint at rc 0). The older round-90 entry uses the
   inline form and carries 2 recorded MULTI-ID findings; I did not copy it.
   `tools/gates/provenance-audit.py` reads the indented continuation as the field value and reports
   `0 findings`, so the header is not empty to that gate.
2. **Table rows carry no S-ids.** QUALITY 15 forbids an id in a table row, so both tables were
   written id-free and the source binding for every table row moved into a short prose block
   immediately under each table, one id per line.
3. **The `- topic:` line is byte-identical to `claims.json` C.topic** (verified by string equality).
   The corpus index tool compares the README row topic against the entry's `- topic:` field, so
   the README row must reproduce that string exactly; it is reproduced verbatim in the fixture that
   produced `CORPUS-INDEX: OK files=264 rows=264 findings=0`.
4. **The README partition header must move from `## linguistics/ (36)` to `(37)`** and the footer
   totals must go 263 → 264 files, 36/36/43/29/24/95 → 37/36/43/29/24/95, or `check-corpus-index.py`
   reports HEADER_DRIFT and TOTALS_DRIFT. Both were applied in the fixture that passed rc 0; they
   are the L1's landing work, not mine.
5. **Registry rows and lesson gate lines are the L1's.** My fixture shows the shape that passes:
   four new rows S957–S960, tier A, status mined, opened 2026-11-05, recheck 180d, used-by
   `corpus/knowledge/linguistics/ideophones-mimetics.md`; a lesson `## Gate` line per id carrying
   the id, the row URL, `accessed 2026-11-05`, and the manifest quote verbatim. The gate quotes used
   are the four manifest quotes; each occurs in its committed capture and shares content words with
   the row's teaching cell, which is what GATE and CAPTURE check.

## What I could not measure, and why

- **The scholarly truth of each statement is not measured.** The grader counts structure, source
  binding and topic binding; it does not judge whether the entry's linguistics are correct. That is
  the closure's re-open job. I checked each quoted span against its capture with a normalized
  substring match, which proves the span is present, not that it carries the meaning I assign to it.
- **No live re-fetch was done.** The four sources were opened by the round before the freeze and
  are committed as captures with sha256, HTTP status and fetch instant in
  `reports/round-92/evidence/manifest.json`; this seat re-read the committed bytes only. The
  recheck cadence above is what a future wave owes.
- **The counter was exercised over a fixture lands commit, not the real lands.** The real lands
  revision does not exist yet; the L1's landing will be the first run over real bytes.
- **No fresh sources were opened.** Four new ids were needed and the frozen manifest supplies
  exactly four; opening more would have meant ids the round did not freeze.

## Out of scope for this seat (not done, deliberately)

- No production file was written: `corpus/`, `tools/`, `reports/` outside the stage dir,
  `SKILL.md`, `PROVINCE.md`, `SCORECARD.md` and `LOG.md` are untouched.
- No commit, push, publish or deploy; no mutating git/jj command in the lane repo. The only git
  mutation was inside the scratch fixture clone, after asserting
  `git rev-parse --show-toplevel` printed that fixture dir.
- `claims.json`, `measure92.py`, `mutants.py`, the stub control and every predicate were read
  only.
- No tool was installed or upgraded: the lane's own frozen Python 3 tools were sufficient and
  authoritative, so no pacman/uv/npx transaction was needed (the pacman guard was therefore never
  engaged).
- No subagent dispatch (leaf member).

## Review outcome (ReviewerEntry-5) and my independent re-verification

The reviewer seat graded the exact bytes this seat delivered (`sha256 2521a3d1…`, confirmed
byte-identical between the stage file and the L1's landed
`corpus/knowledge/linguistics/ideophones-mimetics.md` by `cmp`):

- Frozen claims.json-C floor sweep: **9/9 PASS** (C1 bytes 28814, C2 h2 12, C3 header keys 4/4,
  C4 table 23x5, C5 phrases 6/6 spanning 10 surfaces, C6 both filename stems, C7 cited-line
  grooming rc 0, C8 capture spans PASS-with-notes, C9 recheck 180d + recheck-scope).
- corpus/QUALITY.md criteria 1-5: **5/5 PASS** (provenance, calibration, couples, decision tables,
  no canon decisions).

The reviewer raised three LOW review-only findings and one note. I re-verified each independently
rather than restating them:

**F-1 — `"does my language have ideophones"` does not bind to any capture. Confirmed, and it is the
house convention, not a defect.** The span is authorial prose posing a design question, not a
source quote, and it appears in no capture. I ran the same sweep over the two peer entries against
the captures of *their own* rounds: `secret-and-ludic-languages.md` has 7 quoted spans and all 7
are unbound against round-92's captures; 3 of its 8 spans are still unbound even against its own
round-91 captures (`"the meeting has moved to the west stair."`, `"Pig Latin style"`,
`"temporarily usable"`). `petitionary-and-votive-formulae.md` is 9 of 11 unbound. Authorial prose
in quotation marks is normal in this corpus and is not expected to bind. **No change made**, and
no change is warranted.

**F-2 — the S959 title uses ASCII `'say'` where the capture uses curly `‘say’`. Confirmed as a
real collation divergence.** `norm()` folds U+2019 but not U+2018, so the ASCII title does not
collate to the capture's title while the capture's own curly form does. This is confined to the
title string in the `- sources:` header; the grader's GATE and CAPTURE legs check the *manifest
quote field* per row, not the title, and both already pass (legs 8/8, rc 0). The reviewer classified
it advisory. **No change made**, for the byte-freeze reason below.

**F-3 — the S958 title also occurs in S959's capture as a cross-reference, so the span could read
as bound to two ids.** Confirmed: `Ideophones in Kambaata (Cushitic)` binds to both `S958.txt` and
`S959.txt`. The span is used only as the S958 source title; no S959 claim rests on it. The
reviewer logged it as a trace path, not laundering. **No change made.**

**One additional observation of my own, not raised by the reviewer.** My independent sweep of all
9 double-quoted spans in the entry found the same class of authorial prose at two more places —
`"this happened"` / `"this was caused"` in §7 — and one *spurious* bind: `"strongly"` collides
with the S958 capture's own gloss `‘do tightly, strongly, deeply’`. These confirm the F-1 class is
generic prose quotation and that a bare span-collision sweep over an entry is not evidence of
mis-citation. It is recorded here so the next round does not read the sweep as a defect.

**Byte-freeze reason for making no edit.** Three constraints converge on leaving the bytes alone:
the L1 has already landed this exact sha256 into `corpus/`; the reviewer's judged object is pinned
to this sha256, and QUALITY criterion 14 requires the judged object to stay frozen through
adjudication (`check-judged-object.py` compares the packet key against the entry at the measured
revision); and the L1 instructed in writing that the stage file not be edited after the final
yield. Re-cutting the bytes to chase two review-only, non-blocking findings would break the
judged-object key for a cosmetic gain. **The entry stands as delivered.**

**Scope note on the reviewer's tool-clone note.** The reviewer's own fixture run of the frozen
grader v3 returned 7/8 with an EXPECTED NEWIDS FAIL, because that fixture had no S957-S960
registry rows. My fixture carried the four rows and returned 8/8. The failure is the fixture's
missing registry rows, not an entry defect, and the L1's landing closes it — as the reviewer
states.

**Lesson still owed by the L1.** `corpus/lessons/round-92.md` does not exist yet in the lane, and
the registry rows and README row are still uncommitted working-tree changes. The GATE and CAPTURE
legs need that lesson file; the row shape that passed is recorded above under
*Integration items for the L1*.

**Cost of the optional F-2 patch.** The reviewer seat is standing by and has offered to re-run the
full sweep set on any new sha in under 30 seconds, so the F-2 fix — if the L1 decides to spend it —
costs one re-review, not a re-sweep from scratch. That is the only reason the patch is worth
recording as a live option rather than closing. No edit was made and none is requested here.
