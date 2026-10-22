# ReviewSurrogates79 — round-53 routed defect 4, line 79 ("Oaxaca", "single-clause")

Carried item: `corpus/lessons/round-53-verifier-spotcheck.md`, routed defect 4, second bullet —
"Line 79 'Oaxaca' and 'single-clause'" in
`corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md:79`.

Line 79 as it stands:

```
| Chinantec (Sochiapam Chinantec, San Pedro Sochiápam, Oaxaca) | lexical tone: a rich tone system carries unpredictable sentences (S135) | discourse length: whistles stay short, single-clause, with simple repairs (S135) | Oaxaca; an archive deposit records spoken and whistled Chinantec elicited from children in San Pedro Sochiápam (S151); the age at which the register is learned is (to-verify) |
```

Rows re-opened this session (2026-10-22), both by ordinary plain requests:

- **S135** — Meyer, Díaz Reyes, Batchelder-Schwab & Gautheron 2025, "Whistled Languages and Whistled Speech", *Encyclopedia of Language and Linguistics* (Elsevier), author-hosted copy. URL read: `http://www.lemondesiffle.free.fr/media/WhistledLanguages_and_Whistled_Speech_Encyclopedy.pdf`. Route: direct, plain `curl`, HTTP 200, `application/pdf`, 1,439,365 bytes, 17 pages (matches the row's "of 17").
- **S151** — The Language Archive, MPI Nijmegen, deposit CAM20459. URL read: `https://archive.mpi.nl/tla/islandora/object/lat%3A1839_00_0000_0000_0016_B509_0`. Route: direct, plain `curl`, HTTP 200, `text/html`, 29,609 bytes.

## Verdict on each flagged word

### 1. "single-clause" — CARRIED, with a wording fix (not CARRIED as written)

The claim itself is carried by S135, PDF p. 7 (section "Intelligibility", which opens on p. 6), verbatim:

- p. 7, "Intelligibility": "whistled sentences tend to be simple with single-clause utterances and equally simple conversational repairs"
- p. 7, "Intelligibility": "These allow for longer discussions than in shouted speech because whistling prevents vocal fatigue"

Two defects in the entry's rendering:

1. **"whistles stay short" over-reads.** The source says "tend to be simple with single-clause utterances" — simplicity, single-clause structure, simple repairs. "Short" is not the source's word, and the very next source sentence says the practice *allows longer discussions than shouted speech*. As a "discourse length" cell, "stay short" points the worldbuilder the wrong way.
2. **Scope cell of the S135 row under-declares the pages.** The row's scope reads "Abstract and 'Body Text', PDF pp. 1–2 of 17", but both supporting sentences sit on PDF p. 7 (running header "Whistled Languages and Whistled Speech 7" confirmed). Line 79's reliance on S135 is real but rests outside the row's declared pages. Registry fix below S285 — extend the S135 scope cell to cover p. 7 (e.g. "pp. 1–2, 7 of 17"). L1-owned; not edited by this seat.

### 2. "Oaxaca" — NOT CARRIED by the rows the line cites

- S135: 0 occurrences of "Oaxaca" in the full extracted text (checked case-insensitively on the newline-joined text; "Mexico" appears 3 times, and the Fig. 3 map places "Chinantec, Mazatec, Mixtec" in Mexico without naming a state).
- S151: 0 occurrences of "Oaxaca" on the opened deposit page; the title carries only "San Pedro Sochiápam".

The placement *is* carried elsewhere: the S155 row (Sicoli 2016 abstract via the Crossref deposit) records "San Pedro Sochiapam Chinantec, Oaxaca" in its own scope cell, and entry line 91 already cites S155 for exactly that placement. Line 79 cites only S135 and S151, so its two "Oaxaca" tokens hang on rows that never say it. Also, the reach cell's bare "Oaxaca;" is a place name standing where every sibling row carries a distance or terrain figure — the table's own convention for an unattested figure is "distance (to-verify)" (used on the Mazatec, Hmong and Siberian Yupik rows).

## Exact corrected line text

```
| Chinantec (Sochiapam Chinantec, San Pedro Sochiápam, Oaxaca) | lexical tone: a rich tonal system for lexical load holds intelligibility even in unpredictable sentences (S135) | discourse length: whistled sentences tend to be simple, single-clause utterances, with equally simple conversational repairs (S135) | San Pedro Sochiápam, Oaxaca (S151; S155); distance (to-verify); an archive deposit records spoken and whistled Chinantec elicited from children in San Pedro Sochiápam (S151); the age at which the register is learned is (to-verify) |
```

Every token in the corrected line is carried by an opened page: S135 p. 7 for the keeps/drops cells (quotes above); S151's deposit title for the archive sentence ("David Yetman and Mark Sicoli elicit spoken and whistled Chinantec from children in San Pedro Sochiápam"); S155's abstract scope (as already mined in the row and used at line 91) for "Oaxaca"; the S135 row's own silence on any Chinantec distance figure is honored by "distance (to-verify)". The S155 row's "never as sole support" rule is satisfied because S151 sits beside it for the placement. This seat edits no corpus file; the correction is offered for the L1.

## Source quotes (S135, opened 2026-10-22, direct HTTP 200)

- PDF p. 7, "Intelligibility": "whistled sentences tend to be simple with single-clause utterances and equally simple conversational repairs"
- PDF p. 7, "Intelligibility": "high levels of intelligibility can be reached in unpredictable sentences in tonal languages with rich tonal systems for lexical load"
- PDF p. 7, "Intelligibility": "These allow for longer discussions than in shouted speech because whistling prevents vocal fatigue"

## Result

- "single-clause": carried in substance, wording corrected above; registry scope cell of S135 needs p. 7 added (routed fix).
- "Oaxaca": not carried by S135/S151; corrected line re-anchors it on S151+S155 and replaces the bare place-name reach cell with "distance (to-verify)" per the table's convention.
- Note on method: no language server applies to these Markdown corpus rows, so this check is text evidence against opened sources, with all three S135 quotes verified verbatim on newline-joined extracted text (`pdftotext`, poppler 26.08.0, already installed; no new tools installed this session).

## Unrun checks

- Díaz Reyes 2008 and Sicoli 2016 bodies were not opened: S135 itself states the single-clause/repairs claim on p. 7, so the rows behind S135's own citations were not needed for this verdict.
- No independent source was opened for the fact that San Pedro Sochiápam municipality lies in Oaxaca; the corrected line grounds "Oaxaca" on the S155 abstract scope instead.
- The other three leftover bullets of routed defect 4 (line 75 / S145–S185 supersession, registry cells S135, S141, S147, S151, S159) are out of this seat's scope and were not re-checked, except the S135 scope cell noted above.
