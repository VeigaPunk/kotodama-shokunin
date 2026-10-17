# supplement-opencode-1 — 04 EXECUTOR D2: PAN-03 name correction

Role: executor (name correction), child of the supplement lane. Baseline revision
`fe34faaafbe0add59ff68827a0df6c5782a72404`, verified as `HEAD` at the start of work.
Wave: `supplement-opencode-1` (`reports/supplement-opencode-1/claims.json`); this is a
supplemental wave, **not** numbered round 5.

Files written (scope honoured — nothing else):

| path | sha256 before | sha256 after |
|---|---|---|
| `examples/culture-d2/components/06-pantheon.yml` | `ef0ebf64f787d04730b6a22c7cf9fafb4de0c5e6dae2db223f57cf53de460478` (511 lines) | `5642c3fc20e12e6b8a83a914ff1fa22201d4858aab7b4fbd43f179ceae33d492` (523 lines) |
| `examples/culture-d2/components/07-myths-motifs.yml` | `fe4426002890e18e876b826aeb50d98da28839f0fad103ad15a217a92ef11bae` (619 lines) | `f26584436d84a31f4ece5c4241777cfd685587195a816c56d91b1d1903c9476d` (624 lines) |

`git diff --stat fe34faa -- <the two files>`: 34 insertions, 17 deletions. The
`06-pantheon` before-hash matches the sha256 quoted for that file in
`examples/culture-d2/reviews/07-myths-motifs.md:21`, which is independent corroboration
that this work ran on the pinned baseline bytes and not on a drifted copy.

Status: **complete for the assigned scope.** Nothing outside the two component files and
this report was written by this worker; scratch lives in
`reports/supplement-opencode-1/scratch/04-executor-d2/`.

## 1. The defect

Baseline gate finding, reproduced byte-for-byte from the pinned packet:

```
FINDING PHON-CODA: FAIL — name PAN-03 'Humweha' cannot be syllabified: /m/ cannot
close the preceding syllable: declared coda set {l, n, r, s}
```

(`tools/gates/frozen/round-4/naming-collision-gate.out:7`; the same line opens
`tools/gates/frozen/round-3/naming-collision-gate.out` and
`tools/gates/frozen/round-3/attempt-1/naming-collision-gate.out`.)

Cause: PAN-03's derivation `huma + -weha` deleted the compound vowel, so the first
syllable closed on `/m/`. `02-phonology.yml` P-3 fixes the coda set as exactly
`{n, l, r, s}` (`examples/culture-d2/components/02-phonology.yml:140`, with the same set
transcribed into the packet by `tools/assemble-d2.py:85`). The name, not the phonology,
was the defect: this worker may not change an inventory or a gate to make a name legal
(assignment boundary, and 02-phonology owns P-3).

## 2. Repair basis (derived, not invented)

Two sibling artifacts already carry the repair form, and both point at 06-pantheon as
the owner to fix:

- `examples/culture-d2/components/05-lexicon.yml` revision 1.1 `naming_support` (lines 6-26):
  name-only bases `huma` [hu, ma] "shelter, low place" and `weha` [we, ha] "wind, breath of",
  and `compound: {term: humaweha, bases: [huma, weha], syllables: [hu, ma, we, ha]}`,
  with revision note "…so huma + weha yields humaweha without deleting the vowel that keeps /m/
  in an onset", and an `integration_gap` stating "06/07 must adopt the PAN-03 spelling consistently".
- `examples/culture-d2/components/13-naming.yml` `cross_component_repairs` (lines 154-170):
  application row "PAN-03: 06-pantheon owns name, derivation and its other occurrences;
  07-myths-motifs repeats the theonym. Adopt humaweha consistently…", and repair record
  `{id: PAN-03, name: humaweha, bases: [huma, weha], syllables: [hu, ma, we, ha]}` with the
  note "Same PAN-03 entity, role and cult; spelling repair, not a replacement deity."

So the replacement is `huma + weha` concatenated with **no vowel deletion**: `Humaweha`,
four open syllables `hu.ma.we.ha`, all legal under (C)V(C) with an empty coda. No gloss,
root, inventory or gate was invented or altered.

## 3. What was changed

`06-pantheon.yml`
- PAN-03 `name: Humaweha`; the eight other occurrences in this file follow (derivation,
  Kalweha/Suweha pairing notes, the role ledger, the PAN-MYTH-02 actor).
- New `alias:` field keeps the retired spelling as a dated retrieval alias.
- New PAN-03 `name_errata` record **NE-01** (dated 2026-10-17): was / now, the defect with
  its baseline gate evidence, the repair basis, the "same entity" scope note, and the
  unresolved L-id dependency.
- `derivation:` now states the concatenation explicitly ("…concatenated with the compound
  vowel kept: hu.ma.we.ha, four open syllables").
- `validation.runs` gains **V-P04** (the naming-gate evidence below) and **V-P05** (myth gate
  unchanged after the rename).

`07-myths-motifs.yml`
- All eight occurrences follow the owner (pantheon reference view, `breath-carriage` role
  agents, MOT-02 `var-recited` actor, MYTH-06 beat six, couplings, MYTH-07 cast and couplings).
- `alias:` on the reference-view entry, a dated erratum sentence in `pantheon_view_note`,
  and new reconciliation finding **RC-5** recording that this file follows the owner's
  repair by reference and does not decide it.

Old spelling remaining in each file: 4 occurrences in 06 and 3 in 07, **all inside the
dated alias/erratum text** (verified by scan), so the historic form stays retrievable
without being a gate-facing name.

Rejected alternatives, with reasons:

- *Widen the coda set to admit /m/*: refused. It edits another component's inventory to
  excuse a name error and changes a gate's expected input.
- *Keep the name and record an unresolved derivation*: not needed — the evidence
  (two sibling artifacts on the pinned baseline, plus the owner's own two roots) is
  sufficient and consistent, so "unresolved" would have been a mislabel.
- *Adopt some other legal shape (e.g. `Hunweha`, /n/-coda)*: the gate accepts it (see T3),
  but it is not derivable from the stated bases `huma` + `weha`; the gate checks legality,
  not derivation, so derivation evidence decides the form.

## 4. Verification actually run

Harness: `reports/supplement-opencode-1/scratch/04-executor-d2/verify.py` (stdlib only, no
network, writes only inside that scratch directory). Full output:
`…/scratch/04-executor-d2/verify-final.out`.

| # | command | observed result |
|---|---|---|
| T1 | pin check: sha256 of the packet from `git show fe34faa:examples/culture-d2/packet.d2.yml` | `d5fb408871dcb985c2f9b134a26c6d64e8640a6f1f17ba1c6bb3c5db1d6dbd96` = `claims.json.baseline.d2_packet_sha256`; `HEAD` = the claims.json baseline revision |
| T2 | `python3 tools/gates/naming-collision-gate.py examples/culture-d2/packet.d2.yml` on the still-baseline generated packet | exit 1, 18 findings, **byte-identical to `tools/gates/frozen/round-4/naming-collision-gate.out`**, including the PAN-03 PHON-CODA FAIL |
| T3 | naming gate API in memory (`evaluate_packet`) on a control packet carrying only the declared profile and one PAN-03 record | `Humweha` → **PHON-CODA FAIL** (rejected control, exact frozen message); `Humaweha` → no phonology finding (accepted); `Hunweha` → no phonology finding (documents that the gate is a legality check, not a derivation check). The only other finding is the packet-level `CROSS-HOLD`, which also fires on the baseline |
| T4 | gate API (`evaluate_text`) over the pinned packet text with the name exchanged in place | exit 1, 17 findings; **removed: exactly the PAN-03 PHON-CODA line; added: none** |
| T5 | end-to-end scratch assembly: `tools/assemble-d2.py` + `tools/gates/costume-era-consistency-gate.py` copied into scratch, all components from `fe34faa` **except** the two edited files from the working tree; then the naming gate on the scratch packet | assembler exit 0 (156 065 bytes); naming gate exit 1, 17 findings, removed = the PAN-03 PHON-CODA, added = none; myth gate on the same packet **exit 0, 0 findings** |
| T6 | myth gate on each owner file after the rename | `06-pantheon` exit 1, exactly the one `MC-S00` already recorded in V-P01; `07-myths-motifs` exit 0 clean — i.e. unchanged from baseline |

Limits of this evidence: the live `examples/culture-d2/packet.d2.yml` still holds the
baseline bytes, so the packet-level number is the **scratch** assembly, not the shipping
packet — the parent owns regeneration (T6's last line just re-confirms the live packet is
still the old bytes). T5 mixed pinned siblings with edited owners deliberately, to isolate
this change from other workers' in-flight edits. The frozen round-3/round-4 outputs were
not rewritten: they are the historic record of the defect.

## 5. Source rechecks and coupling audit

`WebSearch` was quota-blocked (HTTP 403) during this run; both rows below are direct
`FetchURL` retrievals of open-access institutional sources (WALS Online, Max Planck
Institute), read in full.

Honest counting note for the parent: `corpus/lessons/supplement-opencode-1/sources/phonetics.json`
(another worker) already audits the **same corpus entry** against WALS ch. 1 (`PHON-A02`,
verdict supported) and ch. 12 (`PHON-A04`, verdict contradicted — against the *other*
§2 sentence "CV(C)-type 'simple' syllable systems ~54% of 534"). My A-04/A-05 rows test a
**different claim text** (the §3 "universals of shape" line), so they are not a re-run of
PHON-A04; but the ch. 12 URL is shared, and the wave should count distinct claims, not
distinct URLs. My retrieval independently reproduces PHON-A02's numbers.

```json
{
  "wave": "supplement-opencode-1",
  "baseline_revision": "fe34faaafbe0add59ff68827a0df6c5782a72404",
  "entry": "examples/culture-d2/components/06-pantheon.yml",
  "entry_sha256_before": "ef0ebf64f787d04730b6a22c7cf9fafb4de0c5e6dae2db223f57cf53de460478",
  "checked_at_utc": "2026-10-17T15:45:15Z",
  "audits": [
    {
      "id": "PAN03-A01",
      "claim": "PAN-03's name is Humweha, derived as huma (shelter, low place) + -weha (wind, breath of), a transparent compound (the record's own derivation line).",
      "entry_locator": "examples/culture-d2/components/06-pantheon.yml:150-158 at the baseline revision",
      "source_url": "examples/culture-d2/components/02-phonology.yml",
      "retrieval_status": "local_repo_file_read (P-3 at line 140; frozen gate output re-run from the pinned packet)",
      "source_locator": "02-phonology.yml P-3 \"coda — exactly {n, l, r, s}\"; tools/gates/frozen/round-4/naming-collision-gate.out:7",
      "source_excerpt": "P-3: \"coda — exactly {n, l, r, s}. Three sonorants and one obstruent; no stop and no glide may close a syllable\"; gate: \"name PAN-03 'Humweha' … /m/ cannot close the preceding syllable: declared coda set {l, n, r, s}\"",
      "verdict": "contradicted",
      "basis": "The flagged statement is the defect itself: the elided form closes the first syllable on /m/, which the owner's coda set excludes. Reproduced byte-for-byte from the pinned packet (T2), and reproduced in isolation through the gate's own evaluate_packet (T3). Dated erratum NE-01 appended to the record; the retired spelling is kept as an alias only.",
      "access_limit": "Internal design rule — no external source can adjudicate a declared inventory; the check is rule-plus-gate, not scholarship."
    },
    {
      "id": "PAN03-A02",
      "claim": "The replacement Humaweha is derivable from the stated bases with no vowel deletion: huma + weha = hu.ma.we.ha.",
      "entry_locator": "examples/culture-d2/components/05-lexicon.yml:8-26 (revision 1.1 naming_support); examples/culture-d2/components/13-naming.yml:156-170 (cross_component_repairs)",
      "source_url": "examples/culture-d2/components/05-lexicon.yml",
      "retrieval_status": "local_repo_file_read (both files read at the pinned baseline)",
      "source_locator": "05-lexicon revision note line 8 and naming_support lines 13-26; 13-naming repair record lines 156-170",
      "source_excerpt": "05-lexicon: \"so huma + weha yields humaweha without deleting the vowel that keeps /m/ in an onset\"; 13-naming: \"Same PAN-03 entity, role and cult; spelling repair, not a replacement deity.\"",
      "verdict": "supported",
      "basis": "Two sibling artifacts on the same baseline carry the form and name 06/07 as the owners to apply it; the gate parses the repaired name with no finding (T3/T4/T5). The bases themselves are this file's own working_roots records, so no new root or gloss was invented.",
      "access_limit": "Internal design choice; 05-lexicon states plainly it is \"not real-language attestation\". No external confirmation is possible or claimed."
    },
    {
      "id": "PAN03-A03",
      "claim": "corpus §2 WALS anchor carried into 02-phonology F-1: modal consonant class 19–25, ~35% of 562 languages (Maddieson 2013) — the band rationale under which D2's 15-consonant chart, and therefore its coda set, was declared.",
      "entry_locator": "corpus/knowledge/linguistics/phonetics-phonology.md:96-98 (as carried by examples/culture-d2/components/02-phonology.yml follows F-1)",
      "source_url": "https://wals.info/chapter/1",
      "retrieval_status": "retrieved_full_text (WALS Online chapter HTML fetched 2026-10-17; Map 1A value table read)",
      "source_locator": "WALS Online ch. 1 'Consonant Inventories' (Maddieson 2013), section 1 text and Map 1A value table",
      "source_excerpt": "\"the mean for the 562 languages being 22.7, the modal value 22 and the median 21. Consonant inventories close to this size (22 ± 3) have been categorized as average\"",
      "verdict": "supported",
      "basis": "Chapter defines average as 22 ± 3 = 19–25 and gives Average = 201 of 563 map languages; 201/563 = 35.7%, matching the carried '~35%'. The band list \"small (from 6 to 14 consonants), moderately small (15-18), moderately large (26-33), and large (34 or more consonants)\" also confirms that D2's 15 consonants sit in the declared moderately-small band (02-phonology follows F-1). Independently reproduced by another worker's PHON-A02 row with the same verdict.",
      "access_limit": "Open access. Mean denominator 562 vs map total 563 — a WALS-internal discrepancy, not an error in the carried claim."
    },
    {
      "id": "PAN03-A04",
      "claim": "corpus §3 universals of shape carried as the design premise behind P-3: \"onsets easier than codas; codas restricted (often to sonorants) or banned; complex codas rarest (WALS 'Syllable Structure')\".",
      "entry_locator": "corpus/knowledge/linguistics/phonetics-phonology.md:121-122",
      "source_url": "https://wals.info/chapter/12",
      "retrieval_status": "retrieved_full_text (WALS Online chapter HTML fetched 2026-10-17; Map 12A value table read)",
      "source_locator": "WALS Online ch. 12 'Syllable Structure' (Maddieson 2013), section 2 definition of values and Map 12A value table",
      "source_excerpt": "Map 12A: \"Simple syllable structure 61 / Moderately complex … 274 / Complex … 151\" (total 486); \"languages which … allow three or more consonants in this onset position, and/or two or more consonants in the position after the vowel, are classified as having complex syllable structure\"",
      "verdict": "supported",
      "basis": "Only the complex class permits two or more post-vocalic consonants (151/486 ≈ 31%; simple + moderately complex = 335/486 ≈ 69% allow at most one), which supports both 'codas restricted or banned' and 'complex codas rarest' as the design premise for a (C)V(C) template with a four-member coda set. Consequence recorded for this repair: fitting the name to the declared template is the conservative direction; widening the coda set would have moved D2 out of the majority class for a naming convenience.",
      "access_limit": "Open access. WALS-internal prose/map disagreement noted (prose '150 languages (about 30.9%)' vs map 151). This row shares the ch. 12 URL with another worker's PHON-A04 but tests different claim text."
    },
    {
      "id": "PAN03-A05",
      "claim": "The parenthetical clause in the same §3 line — coda inventories are restricted \"often to sonorants\".",
      "entry_locator": "corpus/knowledge/linguistics/phonetics-phonology.md:121-122",
      "source_url": "https://wals.info/chapter/12",
      "retrieval_status": "retrieved_full_text (chapter read in full; no sonorant-specific coda statement found)",
      "source_locator": "WALS Online ch. 12, sections 1-4 (the chapter's liquids/glides limitation concerns the second element of onset clusters, not coda inventories)",
      "source_excerpt": "\"The second of two consonants is commonly limited to being one of a small set belonging to either the class of 'liquids' or the class of 'glides'.\"",
      "verdict": "unresolved",
      "basis": "The retrieved chapter supports coda restriction as such but does not assert that restricted coda inventories are 'often' sonorant; the only sonority statement found is about onset clusters. Left unresolved rather than upgraded. Not load-bearing: D2's coda set is a stipulated design choice, and no naming rule here depends on the universal.",
      "access_limit": "Open access, but a general sonorant-coda frequency claim would need a different source (e.g. a coda-inventory survey) that was not retrieved in this run."
    },
    {
      "id": "PAN03-C01",
      "claim": "Coupling audit, language ↔ myth ↔ era: the repaired name identifies one entity across the pantheon owner, the myth records and the role ledgers, and is legal under the single declared stratum for E0 and E1.",
      "entry_locator": "examples/culture-d2/components/06-pantheon.yml PAN-03 + roles; examples/culture-d2/components/07-myths-motifs.yml pantheon view, breath-carriage role, MOT-02 var-recited, MYTH-06 beat six",
      "source_url": "reports/supplement-opencode-1/scratch/04-executor-d2/verify-final.out (T5 scratch assembly) and examples/culture-d2/components/02-phonology.yml",
      "retrieval_status": "local_repo_files_read plus executed gates (naming gate and myth gate on the assembled scratch packet)",
      "source_locator": "02-phonology.yml strata_note (\"One stratum is declared — the native D2 lexicon across both stages\"); WS 2026-10-17: T5 output lines",
      "source_excerpt": "T5: \"naming gate exit 1; 17 findings (baseline 18) … removed: [PAN-03 PHON-CODA] added: none\" and \"myth gate on scratch packet: exit 0; 0 findings\"",
      "verdict": "supported",
      "basis": "The name is identical in owner and reference view and in both role ledgers; the packet's pantheon and motif records pass the myth gate after the rename, so the language↔myth coupling holds; every packet name record carries no stage override, i.e. it is read under the one native profile that 02-phonology declares across both stages, so no era-scoped spelling variant is needed. Dress is not coupled to theonyms (the GAR-* garment repairs belong to 13-naming's ledger and are another worker's scope) — stated rather than claimed.",
      "access_limit": "Local structural check only; it is not evidence about any real culture and not canon."
    }
  ]
}
```

## 6. Occurrences outside my two files (parent reconciliation)

Scan of the working tree for `Humweha`/`humweha`, excluding my scratch directory:

| path | count | disposition / recommendation |
|---|---|---|
| `examples/culture-d2/packet.d2.yml` | 10 | Generated artifact — parent regenerates with `tools/assemble-d2.py`; the scratch assembly in T5 shows the finding clearing. **Not written by this worker.** |
| `examples/culture-d2/ASSEMBLY.md` | 1 | Documents the defect as an assembly finding ("PAN-03 Humweha — PHON-CODA FAIL"). Another owner's file; parent may want a dated repair note. |
| `examples/culture-d2/reviews/07-myths-motifs.md` | 2 | Round-3 review bytes quoting the old theonym; historic review record — recommend leaving as is (the review is about the pinned revision). |
| `corpus/lessons/round-3-d2-build.md` | 1 | Historic corpus byte naming the defect; not rewritten (no corpus write in this scope). |
| `LOG.md` | 1 | Parent-owned bookkeeping. |
| `tools/gates/frozen/round-3/**`, `tools/gates/frozen/round-4/**` | 23 | Frozen artifacts; deliberately unchanged — they are the tamper-evident record of the defect. |
| `reports/supplement-opencode-1/03-assembler.md` | 1 | Another worker's report describing the same baseline finding. |
| `reports/supplement-opencode-1/scratch/**` (workers 02, 22, 29) | ~100 | Other workers' scratch copies. |
| `examples/culture-d2/components/13-naming.yml`, `05-lexicon.yml` | 0 (they use `humaweha`) | Already carry the repair form as `humaweha`; nothing to change. |

## 7. Limits and unresolved items

- The repair is a **legality** fix with derivation evidence; the gate does not validate
  derivation, and this report says so explicitly (T3 shows a legal-but-wrong `Hunweha`
  passing the gate). No canon, rank, or promotion is claimed — author-side evidence only.
- No `L-` id is claimed for `huma`/`weha`; the theonym stays provisional on the lexicon
  handoff (unchanged from the file's RG-04 rule), and the `name_errata` record says so.
- The public-source rows test claims *carried by the local corpus into 02-phonology*
  (F-1 band, §3 universals line). No external source can adjudicate a stipulated D2
  inventory; the one clause that failed to find support (`often to sonorants`) is recorded
  unresolved rather than smoothed.
- `WebSearch` was unavailable (quota 403); no search-snippet evidence was used, and no
  source is cited that was not fetched in full.
- The wave-level `sources/*.json` files are outside this worker's write scope, so the audit
  rows above live in this report for the parent to lift or discard (with the
  double-counting caveat in §5).

## 8. Reproduce

```bash
cd <repo>
python3 reports/supplement-opencode-1/scratch/04-executor-d2/verify.py
# T1 pin, T2 frozen replay, T3 accepted/rejected controls, T4 packet delta,
# T5 scratch end-to-end assembly, T6 owner-file gates
```

Left for the parent: regenerate `examples/culture-d2/packet.d2.yml`, re-run the gate
battery, and record the LOG/SCORECARD entries. `tools/gates/frozen/**` was intentionally
not touched, so the frozen round-4 naming output still shows the pre-repair finding.
