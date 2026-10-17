# R8-F05 — freshness recheck receipt

- Round: 8 (2026-10-17) · axis: freshness · worker: R8-F05
- Prior row: **R6-04-A** (disposition at round 6: `partial-support`)
- Entry: `corpus/knowledge/civilizations/aegean-minoan-mycenaean.md`
- Entry sha256 at recheck: `a9b16ab15d4d9078a86cedf024f04a54382f356a87b5167d7ca4221202a58d47` · lane revision `cf338a713060f274269cdacb18cdc0085bb06aeb`
- Prior ledger: `corpus/lessons/round-6-sources/04.json`
- Question: verify the entry's distinction between undeciphered Linear A / Minoan affiliation and readable Greek Linear B — sign similarity and B-based transliteration are not proof of Minoan pronunciation, meaning or divine names.

**Line-numbering note.** All entry line numbers below refer to the file at the recorded sha256 (read 2026-10-17T17:19-03:00). The round-8 metadata sweep concurrently added three frontmatter lines (`source` / `verified-at` / `recheck`) after the `couples:` line, shifting everything below it by +3: the same passages carried 51–56 / 63 / 103 / 198 in the pre-sweep numbering. Cross-check cited passages by content, not by number; the hash is a point-in-time record.

## Verdict (worker label, author-side)

**`partial-support` → supported (passage-level), with one entry-wording delimitation filed for reconciliation.**

The named round-6 limit — *"Salgarella's language-affiliation wording … remain unread"* — is closed: her own sentences were retrieved in full from the University of Cambridge Apollo deposit of the Oxford Classical Dictionary entry the entry itself cites (line 11). The second named limit (Duhoux's *da-ma-te* argument) is now documented through a peer-reviewed article that cites and weighs it, but the 1997 article itself is still unretrieved. Passage support is not a whole-claim promotion; raw label and reconciled disposition are kept apart per the round-8 F requirement.

## Receipts (all retrieved 2026-10-17, -03:00, minute-approximate)

### 1. Main — Salgarella, "Linear A", *Oxford Classical Dictionary* (Apollo deposit)

- Item: https://www.repository.cam.ac.uk/items/f50c0df4-f355-4bc0-be2a-8e960b2bb5da (handle 1810/357340); item metadata: *Is Part Of* Oxford Classical Dictionary, publisher OUP, ISBN 9780199381135.
- Bitstream: https://www.repository.cam.ac.uk/bitstreams/f6fd5b2a-3c52-4edd-856e-def4e71eb8db/download — `curl` → **HTTP 200, 336172 bytes**, sha256 `f2451475c6c65371897d760b9b1a4e197e37a181c099bb50bfd495b92ddaadb3`. Line locators below are from `pdftotext -layout salgarella.pdf -`.

Quoted (section locator → text):

- §"The Minoan language", line 534: *"At present Minoan is understood to be an isolated language, that is to say not affiliated to any of the linguistic families so far known."*
- §"The Minoan language", lines 564–566: *"All these attempts at identifying the language behind the script have so far proved untenable, as not supported by enough probative evidence."*
- §"The Minoan language", line 574: *"Although we are currently at an impasse at identifying the Minoan language, we understand that:"*
- §"The Minoan language", lines 621–623: *"Linear A still resists decipherment for the relative paucity of extant evidence, the short and formulaic nature of most inscriptions (which therefore do not display insightful syntactical structures) and the lack of an agreed cognate language, not to mention that not a single bilingual inscription has been discovered to date."*
- §"Script relations and 'readability' of Linear A", lines 208–212: *"Linear A was used as graphic template for the development of Linear B, within a script transmission process which entailed language change from Minoan (unidentified linguistic family) to Greek (Indo-European). Graphically, the two scripts show a 70% sign similarity with respect to syllabic signs […]"*
- same section, lines 220–222: *"it is assumed that most homomorphic signs (i.e. signs showing the same morphological shape in both Linear A and B) may be read with the same, or closely approximate, phonetic value in both scripts"*
- same section, lines 233–236: *"It is therefore possible to 'read' Linear A inscriptions in phonetic transcription with approximation (e.g. inscriptions from Haghia Triada, inspcriptions from elsewhere), although an appropriate understanding of the language behind the script still defies us."*
- note 21, lines 553–556, attached to *"some of which have been successfully identified by scholars"*: cites *"Yves Duhoux, 'Une analyse linguistique du linéaire A', BCILL 14.1 (1978): 65-129. Yves Duhoux, 'LA > B da-ma-te = Déméter? Sur la langue du linéaire A', Minos 29-30 (1997 [1994-1995]): 289-294. […]"*

This is the entry's own cited warrant: all four items of its line-11 characterization (undeciphered; unaffiliated; proposed identifications untenable; no bilingual or agreed cognate) appear in her sentences, and the source itself splits "Minoan (unidentified linguistic family)" from "Greek (Indo-European)".

### 2. Corroboration A — Steele & Meißner 2017, "From Linear B to Linear A: The problem of the backward projection of sound values"

- Apollo deposit: https://www.repository.cam.ac.uk/bitstreams/635fb0e4-fed6-4dd0-a369-16067170b87f/download — `curl` → **HTTP 200, 559018 bytes, 19 pages**, sha256 `1d9818c307dc55ddebbff4ca978c8573ce383139d6de743c608d02851f57a2ea`; text via `pdftotext -layout steele-meissner.pdf steele-meissner.txt`.

- §11 "Conclusion", txt lines 699–703: *"there is, quite simply, very little room for a random reallocation of sound values, and positive identifications of sound values in Linear A are so numerous, systematic, and based on a whole number of approaches supporting one another that, on the basis of the evidence so far, in principle the backward projection of sound values from Linear B to Linear A must be regarded as legitimate."*
- §3, txt lines 293–295: *"The exact phonetic values in Linear A cannot be recovered with precision … but the shared values are close enough to reconstruct the values approximately."*
- §1, txt lines 48–52: *"For if we apply the sound values of Linear B to Linear A the result is a language of which we understand neither the grammatical structure nor, with a few minor exceptions, the content."*
- §4, txt lines 328–336: name equations are weak evidence — *"Personal names are not a particularly good guide as there usually is no independent confirmation available that two identically or very similarly written forms render the same name"*; worked example: Linear B `a-ka-re-u` (a man's name) vs Linear A `a-ka-ru` (a heading, possibly a transactional term) — *"Linear A a-ka-ru would thus have nothing to do with Linear B a-ka-re-u."*

### 3. Corroboration B — Thomas 2020, *Kadmos* 59(1–2): 1–23 (author-hosted proof)

- DOI `10.1515/kadmos-2020-0001` (published citation from publisher search metadata; the De Gruyter page itself did not render). Proof PDF: https://www.finnishsyntax.co.uk/wp-content/uploads/sites/3/2022/01/Reflections_on_Morphology_in_the_Language_of_the_Linear_A_Libation_Formula.pdf — `curl` → **HTTP 200, 424283 bytes**, sha256 `dd3f7ac1af0fb7cb015ce7bd0d5405a44e85cc7383320635b7e5ccc437e34040`.

- §3 "Noun morphology", txt lines 185–187: *"Duhoux (1997, 291–293) has argued that the prefix <i-> in sequences such as <i-da-ma-te>, which occurs on AR Zf1 and AR Zf29 means "to/in" (cf. <da-ma-te>, on KY Za2)."*
- §2 note 5, txt lines 130–132 (weighing it): *"Another possibility is that we have here the prefix i-, meaning "to/in" (Duhoux 1997, 291–293) before a word beginning with a-, though in many cases, it is difficult to see how this could be the case."*
- §1, txt lines 50–53: *"So far, the language (or languages) of Linear A has not been convincingly linked to any other known language, though there have been several attempts at decipherment."*
- §4, txt lines 508–512: *"It does not, however, follow that the language is Indo-European – co-incidences of form can occur, and can easily be misleading."*

### 4. Context note — fresh 2026 circulation (source itself not retrieved)

Arkeonews report of a 2026 Zenodo preprint (Schümann, IO Za 2; DOI `10.5281/zenodo.20698076`) proposing divine names "Tinu"/"Ida-Mate". The news text itself hedges: *"Linear A has never been securely deciphered, and the proposed reading depends on Schümann's own phonetic and linguistic interpretations"*; *"They should therefore be treated as a hypothesis rather than an established decipherment."* The Zenodo record returned **HTTP 403** (both `doi.org` and `zenodo.org/records/` paths), so nothing is asserted about the preprint's contents.

## What this does to the entry

**Strengthens** lines 11, 54, 59, 66 (exactness/meaning half), 106 and 201 — see the quote mapping above. In particular the round-6 formulation "undeciphered status alone does not establish every affiliation or divine-name proposition" now has the source's own sharper two-part form: approximate B-based reading is *legitimate*, while exact values, grammatical structure, content and any divine-name reading remain unrecovered.

**Delimits** (filed for the reconciler; this worker wrote no entry edits):

1. **Line 56** — *"conventional B-based transliterations are useful analytical notation"* understates the position of the entry's own evidence base. Salgarella 2022 assumes homomorphic signs "may be read with the same, or closely approximate, phonetic value", and Steele & Meißner 2017 conclude backward projection "must be regarded as legitimate" in principle (while denying exactness and understanding). Suggested refinement: keep "analytical notation" but add "and approximate readings; legitimacy argued, exactness not recoverable".
2. **Line 12** — *"recorded in Salgarella 2022's bibliography as an unproven etymological proposal"* is imprecise for the retrieved deposit: the *da-ma-te* article appears only in **note 21** (works on successfully identified affixes), and the end-of-entry bibliography lists only Duhoux's *Études minoennes I* (1978). The "unproven" verdict is the entry's own summary — defensible (the 1997 title is itself a question; Thomas 2020 cites and doubts its *i-* prefix argument) but not a Salgarella sentence about that article. Suggested rewording: "cited in Salgarella 2022 (note 21, among works on identified affixes); its Déméter identification remains contested".

Neither candidate was applied; entry edits are the reconciler's / entry owner's call.

## Limits

- **Duhoux 1997 itself remains unread.** Minos 29–30 (1994) is not digitized on the journal's current platform; the *da-ma-te* leg rests on a peer-reviewed article's citation of its pages 291–293.
- The Salgarella text is the **Apollo deposit** (accepted author text), not the published OCD digital edition; `oxfordre.com` returned HTTP 403 in round 6 and was not re-attempted.
- The Thomas text is an **author-hosted proof** (DOI placeholder in the proof); published pagination comes from publisher search metadata.
- No claim is made about the 2026 preprint's contents.
- Passage-level support only; author-side worker label.
- The entry was concurrently edited by the round-8 metadata sweep between the initial read (17:11) and the hash snapshot (17:19); the recorded sha256 is a point-in-time value and may drift again during the wave.

## Documented access failures (attempted 2026-10-17)

| Target | Status |
|---|---|
| `oxfordre.com/classics/…acrefore-9780199381135-e-8927` | HTTP 403 (bot wall) — round-6 record, unchanged |
| `doi.org/10.5281/zenodo.20698076`, `zenodo.org/records/20698076` | HTTP 403 both |
| `degruyterbrill.com/document/doi/10.1515/kadmos-2020-0001/html` | JS-only, no content extracted |
| `revistas.usal.es` Minos archive + search (`query=da-ma-te`) | only site footer rendered; vol. 29–30 not available |
| Dialnet issue 208168 + document search | JS-only; metadata in search snippets only |
| `repository.cam.ac.uk/search?query=Salgarella…` | JS-rendered; item page reached via search result instead |

Search sweeps run this round are listed in the JSON receipt (`sweeps[]`), each with its query text and date.

## Reproduce

```
curl -sSL -o salgarella.pdf https://www.repository.cam.ac.uk/bitstreams/f6fd5b2a-3c52-4edd-856e-def4e71eb8db/download   # HTTP 200, 336172 bytes
sha256sum salgarella.pdf                       # f2451475c6c65371897d760b9b1a4e197e37a181c099bb50bfd495b92ddaadb3
pdftotext -layout salgarella.pdf - | grep -n "isolated language\|proved untenable\|single bilingual\|homomorphic\|with approximation"
curl -sSL -o steele-meissner.pdf https://www.repository.cam.ac.uk/bitstreams/635fb0e4-fed6-4dd0-a369-16067170b87f/download   # HTTP 200, 559018 bytes
sha256sum steele-meissner.pdf                  # 1d9818c307dc55ddebbff4ca978c8573ce383139d6de743c608d02851f57a2ea
pdftotext -layout steele-meissner.pdf steele-meissner.txt
curl -sSL -o thomas2020.pdf https://www.finnishsyntax.co.uk/wp-content/uploads/sites/3/2022/01/Reflections_on_Morphology_in_the_Language_of_the_Linear_A_Libation_Formula.pdf   # HTTP 200, 424283 bytes
sha256sum thomas2020.pdf                       # dd3f7ac1af0fb7cb015ce7bd0d5405a44e85cc7383320635b7e5ccc437e34040
pdftotext -layout thomas2020.pdf thomas2020.txt
# quote verification (count 1 for each quoted string):
pdftotext -layout salgarella.pdf - | tr '\n' ' ' | tr -s ' ' | grep -c "not affiliated to any of the linguistic families so far known"
```

Scratch downloads live in `/tmp/r8-05` (outside the lane repo). `/tmp` ran out of inodes mid-session, so the Salgarella extraction was read from stdout; the PDF and its hash are recorded above and the extraction is reproducible with the command shown.

## Worker label

Author-side disposition recorded as `partial-support → supported (passage-level), with one entry-wording delimitation filed for reconciliation`. This is a raw worker label; reconciled dispositions belong in `reports/round-8/freshness/reconciliation.json` and are not claimed here.
