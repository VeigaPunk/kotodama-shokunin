# CriticC96 — falsification attack on claim C (coverage)

Seat: CriticC96 (critic role, milestone r96-v1). Scope: attack coverage claim C only; I edited
nothing in the lane repo. Base `0539276c0e329743200b60e98bf289c540f78864`; freeze `deca7e6fff988061f01bfc501a91e18fca892822`;
correction `063f70c9ab9aed5297741773292ded6d713d537a`. Frozen instruments read first, never edited:
`reports/round-96/claims.json`, `reports/round-96/predispatch.py`, `reports/round-96/predispatch-base.txt`.
Scratch: `/fast/scratch/hyaku/kotodama-r96/CriticC96/` (deleted before yield). Tools installed: none.

## 1. Leg 1 — is the surface truly unowned at base?

My own re-runs (from lane root; rc recorded):

| command | rc | result |
|---|---|---|
| `git rev-parse --verify 0539276...^{commit}` | 0 | base resolves |
| `git ls-tree -r --name-only 0539276... \| grep -iE 'oath\|blessing\|curse\|imprecation\|sanction\|formula'` | 0 | matches are `*formula*` family files (greeting/lullaby/lament/petitionary/orality) — **no file named oath/blessing/curse** |
| same ls-tree grep without `formula` (ScoutSurface96 command 3, re-run) | 1 | **zero matches** — zero filename owners at base |
| `git grep -n -iE '^- topic:.*(oath\|blessing\|curse\|imprecation)' 0539276... -- corpus/knowledge/` | 0 | 7 topic-line files at base (my term set) |
| `git grep -c -iE '\boath' 0539276... -- corpus/knowledge/` | 0 | 63 files mention oath; max `myth-symbol/binding-speech-complex.md` = **59** |

**Finding (the strongest counterexample):** `corpus/knowledge/myth-symbol/binding-speech-complex.md`
owns most of the surface as content: topic line 4 names "the four channels (oath, curse, blessing,
name-power)" and "the oath in depth (formula anatomy: invocation / assertion / self-imprecation /
uptake...)"; dedicated sections `## 4. The oath` (41 lines), `## 5. The curse` (28), `## 6. The blessing`
(12) measured by awk section counts; its `- gap filled:` line claims "no entry owns the binding-speech
complex itself: the oath, the curse, the blessing". So "zero owned knowledge file at base" is true
**only under the filename sweep the claim itself freezes as its verification basis**. Content-level,
a near-twin owner exists. The frozen claim's premise is filename-scoped, so this is not a leg
failure — but it is a duplicate-authority risk. Mitigations observed in the landed tree: the new
entry's §1 explicitly defers ("That file owns who executes and what happens; this entry owns how
the words are built and parsed ... restates none of the machinery"), couples one-way to the
machinery file, and ConnectorOverlap96 §6.3 routes the seam to L0. Per the round-92 precedent
(ideophones vs sound-symbolism §6, open L0 line 356), the move counts as expansion on the
dedicated-entry surface with the contested-scope caveat. Verdict: not falsified; flagged.

## 2. Leg 2 — 8-gram overlap with adjacent owners (ConnectorOverlap96's list)

Tool: `overlap8.py` (scratch; word-level 8-grams, case-folded, tokens `[a-z0-9']+`,
SequenceMatcher for top spans). Entry: 5007 tokens, 4891 distinct 8-grams, 30143 B.

| adjacent owner | distinct shared 8-grams | occurrences |
|---|---|---|
| myth-symbol/binding-speech-complex.md | **14** | 14 |
| myth-symbol/ordeal-judicial-proof-rituals.md | 2 | 2 |
| myth-symbol/witchcraft-sorcery-accusation-institution.md | 1 | 1 |
| the other 17 named owners (petitionary-and-votive, guest-right, sacred-kingship, scythian-saka, ritual-garments, animal-symbolism, death-afterlife, mineral-stone, purity-pollution, ritual-liminality, verification-independence, sacred-registers, politeness-taboo, taboo-strata, synthesis/taboo-euphemism, deity-name-derivation, semantics-pragmatics) | 0 | 0 |

Top three shared spans with binding-speech-complex.md (all inside the entry's
deferral/citation prose, not restated machinery):

1. 15w: "cannot distinguish the curse that should land from the one that should not which is"
2. 11w: "a designer who has written one has mostly written the other"
3. 8w: "the four channels oath curse blessing name power"

Total verbatim overlap with the near-twin = 14 of 4891 grams (**0.29%**); the ordeal/witchcraft
hits are pointer lines ("myth symbol binding speech complex md owns the"). No copy-scale overlap.
Verdict: not falsified.

## 3. Leg 3 — quote recount, id equality, census/index/append-only

- Quote recount (my `recount.py`, dry-run-validated on round-95 rows S970–S974: 5/5 OK rc 0,
  matching the r95 verifier spotcheck): **S975–S984 all 10 rows count=1, ≤25 words, rc 0.**
  Longest: S975 19 words; shortest: S972-class n/a; all within the 25-word rule.
- Id equality: entry cites S975–S984 (3–4 mentions each) == `ExecRegistry96/rows.md` ids (10)
  == qualifying rows in `corpus/SOURCES.md` (10). Used-by cell byte-exact for all 10
  (awk `$12` mismatch scan printed nothing).
- Registry: rows 898 → **908** (grep -c rc 0), highest **S984** ≥ S977, 10 new qualifying
  (tier A/B, mined, opened 2026-11-05) ≥ 3. C2 shape holds.
- Append-only: `diff base-SOURCES.md SOURCES.md` → **removed=0 added=10** (matches
  ExecRegistry96's own receipt `added=10 removed=0`).
- Census: `scripts/sources-census.sh validate --file corpus/SOURCES.md` → **rc 0** (only the two
  pre-existing W04 duplicate-url warnings S927/S928, present at base before this round).
- Index: current tree `CORPUS-INDEX: FINDINGS files=268 rows=267 findings=5
  ids=FOOTER_DIR_TOTALS,FOOTER_TOTAL,HEADER_DRIFT,MISSING_ROW,TOTALS_DRIFT` **rc 1** —
  README bytes not yet landed. Landing path verified: `git apply --check -p0
  stage/ScribeEntry96/README.diff` **rc 0**; simulated landed mirror (diff applied, README.md.new
  moved in place) → `CORPUS-INDEX: OK files=268 rows=268 findings=0` **rc 0**. C5 passes at
  lands **iff the L1 lands the staged README diff** — a recorded dependency, not a falsification.
  (Note: my first `git apply --check` failure was my own default `-p1` strip aiming at the wrong
  file; `-p0` is correct for this diff's `corpus/...` headers.)
- Entry C1 shape (replicating the counter's exact norm/phrase logic): bytes 30143 (≥12000),
  h2 11 (≥6), table 19×5 (≥5×3), frozen phrases **6/6** (≥4), topic line byte-equal True.
- Captures: 10/10 present under `reports/round-96/evidence/` (SXXX.txt + raw).
- Frozen-counter run from my seat: launched read-only (`predispatch.py --work <scratch>
  --base-rev 0539276...`), killed at my own 280 s cap during the O legs (C legs print last);
  `counter_rc=1` reflects my timeout, not a C measurement. The lands measurement belongs to the
  scoring seats. Provenance spot-checks instead: S982 capture head matches row venue/authors and
  the quote sits in the oath/witness/punishment context; S984 (TheTorah.com) matches likewise.
- DONE hashes: `ScribeEntry96/DONE` = `4a604334...` = sha256 of the landed entry (verified);
  `ExecRegistry96/DONE` = `50466411...` = sha256 of `rows.md` (verified). Observed: Scribe's DONE
  was re-stamped once during the run (first sighting `9039cf79...` at 18:25, final `4a604334...`
  matching current bytes) — consistent revision, both observed values recorded.

## 4. Leg 4 — claims without a cited source and not marked inference

- Every real-tradition statement in the 229-line entry carries an `(SXXX)` id with the located
  quote; sweep for double-quoted spans without an adjacent S-id found only invented specimen
  formulae ("by whatever watches", "if I fail, then X happens to me", "whoever disturbs this
  grave"), path mentions, and §1's in-corpus citation line. **No uncited empirical claim found.**
- 45 `(design, not sourced)` markers; 0 uses of the word "inference" (house convention is the
  design marker; applied consistently). §11 scopes the small base and forbids generalization.
- One cosmetic defect: line 122 — "so the class it belongs to is the one it "a ritual, spell,
  curse, charm, incantation, blessing, hymn, or mantra" (S980)." — grammatically garbled
  quote integration (the claim stays attributed to S980). Not a falsification; a wording fix
  for the scribe if the L1 wants one.

## 5. Provenance hazard (recorded, non-fatal)

Round 95 staged unlanded candidates S975–S981 (lament-topic: Avdikos, Katsanevaki, Hytönen-Ng,
Stepanova, Ermakov, Koski, Alembi; captures in `waves/round-95/w1/stage/ScoutTopic95/evidence/`).
Round 96 landed S975–S981 as **different, oath-topic documents** (Faraone, Nygaard, Perseus
Iliad 19, Tuomi, Ní Mhaoldomhnaigh, Frangulov, Kokugakuin). The registry itself is append-only
and self-consistent, so no registry contradiction exists — but the round-95 lesson's "widening
the lament entry's citation set in a later round" option has lost its ids to a different topic.
Lane-level id-space collision across wave stages; for the L1's ledger, not a claim-C leg.

## 6. Verdict

**Claim C survives the attack.** Every falsification leg failed to falsify:
1. filename-surface unowned at base (rc 1 sweep) — content near-twin flagged, deferred in-tree, L0-routed;
2. verbatim overlap 0.29% with the near-twin, 17/20 owners zero, spans citation-shaped;
3. 10/10 quotes count=1 ≤25 words rc 0; ids equal everywhere; census rc 0; append-only removed=0;
   C1 shape 30143 B / 11 h2 / 19×5 / 6 phrases / topic byte-equal; captures 10/10;
4. no uncited empirical claim; one garbled sentence (line 122), cosmetic.

Landing dependency to watch: **C5 needs the L1 to land `stage/ScribeEntry96/README.diff`
(`-p0`, check rc 0; simulated landed index rc 0 268/268/0).** Without that landing, index rc is 1
on the tree as it stands.

## Commands and rc summary (key numbers)

- `git ls-tree -r --name-only 0539276... | grep -iE 'oath|blessing|curse|imprecation|sanction'` → rc 1 (zero)
- `git grep -c -iE '\boath' 0539276... -- corpus/knowledge/` → rc 0, 63 files, max 59 (binding-speech-complex.md)
- `python3 recount.py SOURCES.md reports/round-96/evidence` → rc 0, 10 rows all count=1
- `bash scripts/sources-census.sh validate --file corpus/SOURCES.md` → rc 0 (2 pre-existing W04)
- `python3 -B tools/check-corpus-index.py --root <lane>` → rc 1 (README unlanded, 5 findings)
- `git apply --check -p0 stage/ScribeEntry96/README.diff` → rc 0
- landed-mirror `check-corpus-index.py` → rc 0, `CORPUS-INDEX: OK files=268 rows=268 findings=0`
- `diff base-SOURCES.md SOURCES.md | grep -c '^<'` → removed=0; `grep -c '^>'` → added=10
- overlap8.py → 14/2/1 shared 8-grams, all others 0 (command line in §2)
