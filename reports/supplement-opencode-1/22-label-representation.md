# 22 — Naming representation: the ten English-label findings (review + source recheck)

- wave: `supplement-opencode-1` (not a numbered GLM round)
- worker scope: 22 REVIEWER — naming representation; artifact set = baseline
  `naming-collision-gate.py`, `11-costumes.yml`, frozen round-4 output
- baseline revision: `fe34faaafbe0add59ff68827a0df6c5782a72404`
- checked: 2026-10-17 (UTC timestamps below)
- canon: NON-CANON review record; nothing here edits gates, components, or packets
- files written: this report only; scratch evidence under
  `reports/supplement-opencode-1/scratch/22-label-representation/`

## 1. What was reproduced, and how

| Item | Baseline value |
|---|---|
| gate `tools/gates/naming-collision-gate.py` | sha256 `8c5afb0a5abc8b00a659120e3795586ddce688bd962ccc68f7308f7bf19aa526` |
| assembled packet `examples/culture-d2/packet.d2.yml` | sha256 `d5fb408871dcb985c2f9b134a26c6d64e8640a6f1f17ba1c6bb3c5db1d6dbd96` |
| component `examples/culture-d2/components/11-costumes.yml` | sha256 `b6e2c5c29cc5d68900d6cde5a8487e64f27d85ecb3d2bd7f3f5beb1113483f22` |
| assembler `tools/assemble-d2.py` (baseline; a sibling worker is editing it concurrently) | sha256 `2a1cbe855c4885c66b9f2cfa36eb658327001a594f688f5a6a3fba03d5ed5e60` |
| frozen `tools/gates/frozen/round-4/naming-collision-gate.out` | sha256 `4d70252bdf7745dea76af07b41a94560b5789ff278cdbb5af4bf6924688bb19e`, 18 lines |

All line-number citations below are to the baseline revision `fe34faa` (the tree
is being edited by sibling workers as this report is written; the gate file
itself was still at its baseline hash when re-verified).

Command and observed result:

```sh
python3 tools/gates/naming-collision-gate.py examples/culture-d2/packet.d2.yml
# exit 1; output byte-identical to the frozen round-4 file (diff empty,
# both sha256 4d70252b…): 6 NAME-NEAR + 1 PHON-CODA + 10 PHON-INVENTORY + 1 CROSS-HOLD
```

So the frozen round-4 naming record is live-reproducible on the pinned baseline,
and `claims.json`'s `naming_findings` counts (NAME-NEAR 6, PHON-CODA 1,
PHON-INVENTORY 10, CROSS-HOLD 1) are accurate.

### Minimal in-memory packet — the 10 findings isolated

`reports/supplement-opencode-1/scratch/22-label-representation/repro-minimal-packet.py`
reads the baseline packet via `git show fe34faa:…` (never the working tree),
imports the gate read-only, and builds a minimal packet whose only name-bearing
records are the ten costume records (`id`, English `garment` label, `form_slot`)
plus one native lexicon-form name (`mirken`, L35) and a recorded no-hit review.

```sh
python3 reports/supplement-opencode-1/scratch/22-label-representation/repro-minimal-packet.py
# == exit code: 1 ==
# == PHON-INVENTORY findings: 10 ==
# == minimal vs frozen PHON-INVENTORY line sets identical: True ==
```

All ten reproduced messages are literally of the form:

```
FINDING PHON-INVENTORY: FAIL — name GAR-01 'winter valley coat (heavy felted wool; uncombed finish optional)': symbol /v/ at position 7 is not in the declared inventory (…)
```

### The checked channel vs the supplied channel

The gate's record reader selects one form key per class
(`tools/gates/naming-collision-gate.py:614-618`): `costumes → garment`. Nothing
in the gate reads `form_slot`, `native_form`, `form_kind`, or any translation
typing (grep over the baseline gate: no `form_slot`, no `native_form`).

For all ten records the comparison is therefore (verbatim from the run above):

| Record | Channel the gate reads (`garment`) | Channel actually supplied (`form_slot`) | `native_form` present |
|---|---|---|---|
| GAR-01 | "winter valley coat (heavy felted wool; uncombed finish optional)" | "LEX-GAR-01, the valley grade of L35 mirken (to-verify with 05-lexicon)" | no |
| GAR-02 | "high-pasture coat (fine first-shear felt; narrow placket; wind-flap at the shoulder)" | "LEX-GAR-02, the high grade of L35 mirken (to-verify)" | no |
| GAR-03 | "transit coat (felted outer; fringed hem-cords at the hem-line; the coat of the pass)" | "LEX-GAR-03 (to-verify)" | no |
| GAR-04 | "lowland-cloth coat (woven plant-thread cloth of the lowland partner; a lowland cut)" | "LEX-GAR-04 (to-verify)" | no |
| GAR-05 | "mast-sash (narrow woven wool band, lineage-issued; the wind standard's sash)" | "LEX-GAR-05 (to-verify)" | no |
| GAR-06 | "stranger's fair coat (flat-woven lowland cut, no fringed hem; the treaty stranger's coat)" | "LEX-GAR-06 (to-verify)" | no |
| GAR-07 | "mourning coat (felt left shaggy, undyed, hem-cords cut back)" | "LEX-GAR-07 (to-verify)" | no |
| GAR-08 | "bale cord (imported plant-thread cord in coils; the legal channel of the banned import)" | "LEX-GAR-08 (to-verify)" | no |
| GAR-09 | "down under-tunic (combed pack-ox underfleece, worn next to the skin at both poles)" | "LEX-GAR-09 (to-verify)" | no |
| GAR-10 | "gale legging (smoke-cured leather, wind-cut: no slack at the ankle, no inner seam)" | "LEX-GAR-10 (to-verify)" | no |

The component states its own typing in prose: "Surface forms are the lexicon
component's: this file coins none and carries its requirements as form slots
(LEX-GAR-*)" (`11-costumes.yml`, `scope_note`), and `form_slots_note`: "This file
coins no surface form". The assembler copies the whole costume block
(`tools/assemble-d2.py:95`) and requires only `(id, garment, material,
wearer_rank, rite, era)` from it (`tools/assemble-d2.py:113`), so no step in the
chain distinguishes a reader-facing translation from a native form.

**Verdict on the ten:** they are representation-channel FAILs, not resolved
scholarship. Each message is true of the *string* it names — but the string is
an English gloss, and the record supplies no native form, so the FAIL grades a
translation against D2 phonotactics. Operability consequence: a downstream
reader counting these as "10 real name violations" overstates clearance work by
exactly this class; they cannot be closed by renaming garments, only by typing
the records (or by the gate holding unresolved forms).

### Correction to the round-4 diagnosis (calibration)

`corpus/lessons/round-4-sol-fixes-and-audits.md` records: "PHON-INVENTORY ×10 in
naming-collision: suspect class — either real coda/segment violations in 05/13 or
an encoding mismatch (accent marks / long-vowel digraphs read as unknown
segments). Diagnose before fixing."

The frozen round-4 evidence falsifies both branches for these ten: every one of
the ten findings names a `GAR-*` **English garment label** (evidence: the frozen
file, sha256 above; the minimal-packet line-set equality above). No `05-lexicon`
or `13-naming` form is involved in the PHON-INVENTORY class; those records' names
(`PAN-03 Humweha`, era tags) appear under PHON-CODA and NAME-NEAR instead. I did
not edit the lesson file (parent-owned); proposed appended correction text is in
§5(c).

## 2. Proposed typed adapter — native form vs translation (design, not landed)

Contract (fail-closed; field names are proposals):

| Field | Type | Gate B/A use | Notes |
|---|---|---|---|
| `native_form` | string | **checked** (the only sound/identity form) | supplied by the form owner (05-lexicon here) |
| `display_label` / existing `garment`, `name` | string | never on the sound channel | reader-facing translation; keeps Gate A uniqueness available only via the native form |
| `form_kind` | `native \| translation \| unresolved` | routes the above | required once the adapter lands |
| `form_slot` + `form_owner` | id + lane | triggers `unresolved` | the 11-costumes case: LEX-GAR-0x owed by 05-lexicon |

Rules (prototype `adapter-prototype.py`, wrapper around the unmodified baseline gate):

1. `native_form` present ⇒ it is the checked form (Gate A + Gate B).
2. Label-only record (`form_kind: translation`, or a `form_slot` with no native
   form) ⇒ removed from the sound channel **and** reported `FORM-UNRESOLVED`
   HOLD — never a silent pass.
3. Contradiction (`form_kind: translation` *and* a `native_form`) ⇒ the native
   bytes govern; the check cannot be waived by labelling.
4. `form_kind: native` with no `native_form` ⇒ HOLD (a claim without bytes is
   not a pass).
5. Untyped legacy record ⇒ unchanged channel (checked) — dropping the typing
   fields cannot exempt a string.

Controls and observed results (all pass; script exits 0):

```
PASS  C0 untyped labels (today's channel, no form_slot)   [PHON-INVENTORY=10, identical-to-frozen=True, exit=1]
PASS  C1 label+form_slot, no native_form -> artifact gone, all held  [PHON-INVENTORY=0, FORM-UNRESOLVED=10, exit=1]
PASS  C1b labels typed translation -> artifact gone, all held        [PHON-INVENTORY=0, FORM-UNRESOLVED=10, exit=1]
PASS  C2 translation claim + violating native_form -> still FAIL      [PHON-INVENTORY('vinter')=1, exit=1]
PASS  C3 declared native, no native_form -> HOLD, not clean           [FORM-UNRESOLVED=1, exit=1, clean=False]
PASS  C4 untyped label -> still checked (no omission bypass)          [PHON-INVENTORY=1, exit=1]
PASS  C5 resolved native form that passes -> clean                    [exit=0, findings=0]
```

C2 is the negative control this task asks for: an inventory-violating native
form (`vinter`, /v/ unlicensed) is still FAILed even when the same record claims
`form_kind: translation`. C1/C1b are the positive control: the ten label
artifact findings disappear, and all ten records are held, so the aggregate is
still red — the artifact is removed without clearing the real gap.

Prototype limits, stated plainly: the adapter here is a wrapper, not a gate
edit; held records leave the gate's per-form key index, so the landed version
must build identity keys from `native_form` and surface `FORM-UNRESOLVED` as a
declared finding id. Landing points for the parent's integrator: gate
`_collect_records` key selection (`naming-collision-gate.py:614-618`) plus a new
finding id; assembler `required`/projection for costumes
(`tools/assemble-d2.py:113`). Not done by me — no gate or component edits were
in scope.

## 3. Adjacent class seen in the frozen output (flagged, not analyzed)

The same frozen run emits 6 NAME-NEAR findings on `E0`–`E3` era tags ("entities
era#1 and era#2 … 'E0' vs 'E1'") — the gate indexes the packet's `eras` list as
name forms. I did not verify whether the packet's `eras` block is a tag list or
record list, nor whether the lane wants era labels graded on the name channel.
Flagged for the parent as a second representation class (labels treated as name
uses); no further claim made here.

## 4. Source rechecks (freshness)

Retrieval notes: `WebSearch` was unavailable (host quota, HTTP 403) for this
worker; all sources below were reached by direct fetch. `iranicaonline.org`
returned HTTP 403 and archive.org *metadata/JSON* endpoints do not render for
the fetch tool, so those routes are unretrieved and not used as evidence.

`entry` (primary): `corpus/knowledge/verification/naming-collision-gate.md`,
sha256 before `60491baec7b1aa916432cf1e27cebac0d3ac3a093d57c6cbec997ecfc48b2b1d`
(via `git show fe34faa:…`). Secondary entry for the dress/language-coupling
audits: `corpus/knowledge/culture-material/garment-lexicon-crosslinguistic.md`,
sha256 before `10fba861fb2919f496fb3032450373d8bd7ccf3e84e75b465d27924725e024bf`
— it is the entry 11-costumes.yml cites (`alias_garlex §4`) for exactly the
claim audited, and it is the dress-coupling knowledge my artifact set exercises.

| id | claim (narrow) | locator | verdict | basis |
|---|---|---|---|---|
| U15-TR58 | [U15] = UAX #15, Unicode 18.0.0, rev 58, 12 August, versioned at tr15-58.html; NFC is a canonical-equivalence form | naming-collision-gate.md §1 sources, §4 canonical layer | supported | fetched page header (version/date/revision/editor) + NFC sentence |
| U39-TR34 | [U39] = UTS #39, version 18.0.0, rev 34, 27 August, §4 Confusable Detection | naming-collision-gate.md §1 sources, §4 skeleton layer | supported | fetched page header + table of contents §4 |
| UNESCO-ICH | [C] endorsed by Decision 10.COM 15.a; principles 1, 4–5, 7–10 used for access/consultation duties | naming-collision-gate.md §1 sources, §9.5 | supported | fetched page: 2015 Windhoek tenth session, twelve principles text |
| WALS-CH12 | [S] = Maddieson, "Syllable Structure", WALS chapter 12; sequencing restrictions are distinct from inventory size | naming-collision-gate.md §1 sources, §6 | supported (chapter identity); author line unconfirmed in retrieved body text | fetched chapter text separates inventory size (ch. 1–2) from sequencing rules; byline not present in extraction |
| HJ-DRESS-A | "Hobson-Jobson (Yule & Burnell 1886)" carries bandana (bāndhnū 'tie-dye'), chintz (Hind. chint < Skt chitra 'variegated'), calico, shawl (Pers. shāl) | garment-lexicon-crosslinguistic.md §4 (secondary entry) | supported | 1886 first edition, retrieved entries (Census id `cu31924012794628`) |
| HJ-DRESS-B | "dungaree (< Dongri, Bombay quarter — toponym)" attributed to HJ **1886** | garment-lexicon-crosslinguistic.md §4 (secondary entry) | contradicted (narrowly: edition attribution) | 1886 text says "Hind. dangri? but it is not in any dictionary that we know"; the Dongri/Fort George toponym + Molesworth line is an editorial addition present only in the 1903 Crooke edition (`hobsonjobson029985mbp`) |

Excerpts (each ≤40 words, retrieved verbatim; OCR spelling preserved):

- U15: "Normalization Form C uses canonical composite characters where possible, and maintains the distinction between characters that are compatibility equivalents." Header: "Version Unicode 18.0.0 … Editor Ken Whistler … Date 2026-08-12 … Revision 58".
- U39: "Version 18.0.0 … Editors Josh Hadley, Roozbeh Pournader … Date 2026-08-27 … Revision 34"; contents list a section "4 Confusable Detection".
- UNESCO: "endorsed, at its tenth session in Windhoek, Namibia, from 30 November to 4 December 2015, the following twelve ethical principles … (Decision 10.COM 15.a)".
- WALS: "In addition to the number of segments that languages use, it is also important to consider the ways that the segments are allowed to combine with each other in making longer structures".
- HJ-A, bandana: "The etymology may be gathered from Shakespeare's Dict., which gives 'Bándhnu; 1. A mode of dyeing in which the cloth is tied in different places…'"; chintz: "It comes apparently from the Sansk. chitra, 'variegated, speckled.'"; shawl: "Pers. and Hind. shal, … 'a pair of shawls.'"
- HJ-B, 1886: "A kind of coarse and inferior cotton cloth; the word is not in any dictionary that we know." ‖ 1903: "a term originally for the common country cloth sold in the quarter contiguous to the Dongari Killa (Fort George, Bombay)".

Not tested (out of the two-claim minimum, stated for honesty): [N] Hough 2016,
[P] IPA 1999, [M] Haspelmath & Sims 2010, [E] Wagner & Fischer 1974 — those
citations remain as the entry carries them, neither supported nor contradicted
by this pass. The pyjama item of HJ-DRESS-A: the 1886 first edition shows
"Pyjamma" only in a word list and the 1903 edition body entry was not located in
the retrieved OCR (cross-references only) — left unresolved rather than scored.

### Required audit JSON

```json
{
  "wave": "supplement-opencode-1",
  "baseline_revision": "fe34faaafbe0add59ff68827a0df6c5782a72404",
  "entry": "corpus/knowledge/verification/naming-collision-gate.md",
  "entry_sha256_before": "60491baec7b1aa916432cf1e27cebac0d3ac3a093d57c6cbec997ecfc48b2b1d",
  "checked_at_utc": "2026-10-17T15:43:30Z",
  "audits": [
    {
      "id": "U15-TR58",
      "claim": "[U15] is Unicode Standard Annex #15, Unicode 18.0.0, revision 58, dated 12 August, at https://www.unicode.org/reports/tr15/tr15-58.html; NFC is the canonical-composite normalization form used by the entry's canonical layer.",
      "entry_locator": "corpus/knowledge/verification/naming-collision-gate.md: sources [U15]; section 4 table row 'Canonical Unicode'",
      "source_url": "https://www.unicode.org/reports/tr15/tr15-58.html",
      "retrieval_status": "retrieved",
      "source_locator": "document header (version/date/editor/revision) and section 1.2",
      "source_excerpt": "Normalization Form C uses canonical composite characters where possible, and maintains the distinction between characters that are compatibility equivalents. Header: Version Unicode 18.0.0; Editor Ken Whistler; Date 2026-08-12; Revision 58.",
      "verdict": "supported",
      "basis": "Header fields match the citation exactly (version, revision, date); the retrieved NFC sentence supports the entry's use of NFC for canonical equivalence.",
      "access_limit": "none; page retrieved in full"
    },
    {
      "id": "U39-TR34",
      "claim": "[U39] is Unicode Technical Standard #39, version 18.0.0, revision 34, 27 August, with section 4 Confusable Detection at https://www.unicode.org/reports/tr39/tr39-34.html.",
      "entry_locator": "corpus/knowledge/verification/naming-collision-gate.md: sources [U39]; section 4 table row 'Confusable skeleton'",
      "source_url": "https://www.unicode.org/reports/tr39/tr39-34.html",
      "retrieval_status": "retrieved",
      "source_locator": "document header and table of contents",
      "source_excerpt": "Version 18.0.0; Editors Josh Hadley, Roozbeh Pournader; Date 2026-08-27; Revision 34; contents include '4 Confusable Detection'.",
      "verdict": "supported",
      "basis": "Version, revision, date, editors, and the section title match the entry's citation; the gate's own docstring already limits its use to a hand-checked subset.",
      "access_limit": "none; page retrieved in full (large output saved by the fetch tool, header and contents inspected)"
    },
    {
      "id": "UNESCO-ICH",
      "claim": "[C] UNESCO Ethical Principles for Safeguarding Intangible Cultural Heritage were endorsed by Decision 10.COM 15.a, and the entry's consultation/access duties map to principles 1, 4-5, 7-10.",
      "entry_locator": "corpus/knowledge/verification/naming-collision-gate.md: sources [C]; section 9.5",
      "source_url": "https://ich.unesco.org/en/ethics-and-ich-00866",
      "retrieval_status": "retrieved",
      "source_locator": "endorsement paragraph and the twelve-principle list",
      "source_excerpt": "endorsed, at its tenth session in Windhoek, Namibia, from 30 November to 4 December 2015, the following twelve ethical principles for safeguarding intangible cultural heritage (Decision 10.COM 15.a).",
      "verdict": "supported",
      "basis": "The decision, session, and year match; the retrieved principles include the consultation/consent and access-condition texts the entry cites for restricted evidence.",
      "access_limit": "principle numbers are not printed in the extracted list; numbering inferred from order, so the mapping 1, 4-5, 7-10 is confirmed in substance, not by visible numerals"
    },
    {
      "id": "WALS-CH12",
      "claim": "[S] is WALS chapter 12, 'Syllable Structure', and supports treating sequencing restrictions and broad syllable-type limits as separate from segment-inventory size (entry section 6).",
      "entry_locator": "corpus/knowledge/verification/naming-collision-gate.md: sources [S]; section 6 ('Inventory, syllable template, and distribution restrictions are separate inputs [P, S]')",
      "source_url": "https://wals.info/chapter/12",
      "retrieval_status": "retrieved",
      "source_locator": "chapter title and section 1 (introduction), section 4 (correlations)",
      "source_excerpt": "In addition to the number of segments that languages use, it is also important to consider the ways that the segments are allowed to combine with each other in making longer structures, such as words and syllables.",
      "verdict": "supported",
      "basis": "The chapter is chapter 12 titled 'Syllable Structure' and explicitly separates inventory size (chapters 1-2) plus a caveat that the three-way classification overlooks distributional detail - which is exactly the entry's 'separate inputs' claim. The chapter's author line (Maddieson 2013) is not present in the extracted body text and was not independently confirmed.",
      "access_limit": "author byline not visible in the retrieved text extraction; author attribution remains unconfirmed by this pass"
    },
    {
      "id": "HJ-DRESS-A",
      "claim": "Hobson-Jobson is a dated archive of trade-borne wardrobe vocabulary: it carries bandana (Hindi bandhnu, tie-dye), chintz (Hindi chint < Skt chitra 'variegated'), calico, and shawl (Persian shal).",
      "entry_locator": "corpus/knowledge/culture-material/garment-lexicon-crosslinguistic.md section 4 (secondary entry; cited by examples/culture-d2/components/11-costumes.yml alias_garlex)",
      "source_url": "https://archive.org/download/cu31924012794628/cu31924012794628_djvu.txt",
      "retrieval_status": "retrieved",
      "source_locator": "Yule & Burnell 1886, entries Bandanna, Chintz, Calico, Shawl (djvu text lines 12893, 30991, 24121, 106531)",
      "source_excerpt": "The etymology may be gathered from Shakespeare's Dict., which gives 'Bandhnu; 1. A mode of dyeing in which the cloth is tied in different places'. ... 'It comes apparently from the Sansk. chitra, variegated, speckled.' ... 'Pers. and Hind. shal, ... a pair of shawls.'",
      "verdict": "supported",
      "basis": "Four of the entry's cited words were located with matching etymological content in the 1886 first edition text; calico's Calecut origin also appears. Retrieved via the Internet Archive scan of the 1886 edition (OCR text, so wording is OCR-normalized).",
      "access_limit": "OCR text; the pyjama headword was not located in the 1886 body (word list only) and the 1903 body entry was not located, so the pyjama item is left unresolved (recorded in the report, not scored)"
    },
    {
      "id": "HJ-DRESS-B",
      "claim": "The entry attributes 'dungaree (< Dongri, Bombay quarter - toponym)' to Hobson-Jobson (Yule & Burnell 1886).",
      "entry_locator": "corpus/knowledge/culture-material/garment-lexicon-crosslinguistic.md section 4 (secondary entry)",
      "source_url": "https://archive.org/download/cu31924012794628/cu31924012794628_djvu.txt",
      "retrieval_status": "retrieved",
      "source_locator": "1886 entry Dungaree (djvu text line 46947) vs 1903 Crooke edition entry DUNGAREE (https://archive.org/download/hobsonjobson029985mbp/hobsonjobson029985mbp_djvu.txt line 57689)",
      "source_excerpt": "1886: 'A kind of coarse and inferior cotton cloth; the word is not in any dictionary that we know.' 1903: 'a term originally for the common country cloth sold in the quarter contiguous to the Dongari Killa (Fort George, Bombay)'.",
      "verdict": "contradicted",
      "basis": "Narrow scope: the word itself is in both editions, and the Dongri/Fort George toponym appears in the 1903 Crooke edition as an editor's addition. The 1886 first edition, which the entry cites, offers only 'Hind. dangri?' and says the word is not in any dictionary - so the 1886 attribution for this etymology is wrong in its edition.",
      "access_limit": "OCR text of two scans; both excerpt lines were retrieved directly. No page numbers invented; locators are the archive.org item text lines"
    }
  ]
}
```

## 5. Proposed follow-ups (parent-owned; nothing landed by me)

(a) **Land the typing and re-run.** Add `native_form`/`form_kind` to the costume
records (05-lexicon supplies the ten LEX-GAR forms) and route the gate channel;
then re-run the frozen battery. Falsifiable expectation: `PHON-INVENTORY` 10 → 0
with 10 `FORM-UNRESOLVED` HOLDs on still-empty slots; falsified if any English
label keeps a PHON-* FAIL or any record without a native form reports clean.

(b) **Recount honestly.** The frozen 18 findings include these 10 representation
items; any tally that treats them as cleared name violations, or as
"unresolved scholarship", should say which class each count is.

(c) **Proposed appended correction** (do not rewrite old bytes):

- to `corpus/lessons/round-4-sol-fixes-and-audits.md` (append): the round-4
  PHON-INVENTORY ×10 diagnosis ("real coda/segment violations in 05/13 or an
  encoding mismatch") is contradicted by the frozen round-4 output
  (sha256 4d70252b…): 10/10 findings name `GAR-*` English garment labels; the
  class is a label-vs-native-form representation gap.
- to `garment-lexicon-crosslinguistic.md` §4 (append erratum): "dungaree
  (< Dongri, Bombay quarter)" is the 1903 Crooke edition's etymology; the 1886
  first edition reads "Hind. dangri? but it is not in any dictionary that we
  know." (retrieved: archive.org `cu31924012794628` and `hobsonjobson029985mbp`).

## 6. Evidence pointers and limits

- Frozen/live gate run: `tools/gates/frozen/round-4/naming-collision-gate.out`
  (sha256 `4d70252b…`) vs live output (same hash);
  scratch copy `scratch/22-label-representation/live-run.out`.
- Minimal repro: `scratch/22-label-representation/repro-minimal-packet.py`
  (reads `git show fe34faa:…`); adapter + controls:
  `scratch/22-label-representation/adapter-prototype.py` (exit 0, 7/7 controls).
- Retrieved texts: `scratch/22-label-representation/hj1886_djvu.txt`
  (sha256 `6465a42adaf222308b574a0a683a215006843059943b8c88a5bdb011f448bd72`),
  `hj1903_djvu.txt` (sha256 `aae017f73353d29577ea77b6343e5c5ceb5da4fdb5aebdec57edfe762144d92c`).
  Web sources: tr15-58, tr39-34, ich.unesco.org, wals.info/chapter/12 (URLs in
  the JSON above).
- Limits: no search engine (quota) so source selection used known/derivable
  URLs; Iranica and JSON endpoints unretrieved; OCR texts are not critical
  editions; the adapter is a scratch prototype, the ten findings remain present
  in the baseline gate output until the parent lands typing. This worker
  modified nothing outside this report and its own scratch directory: no gate,
  component, packet, corpus, LOG, or SCORECARD file was touched by worker 22 and
  no commits were made. (Sibling workers have edited other files in the same
  working tree since this report's baseline reads; the line locators above are
  pinned to `fe34faa` for that reason.)
