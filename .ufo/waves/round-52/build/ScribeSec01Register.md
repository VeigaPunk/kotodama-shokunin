# ScribeSec01Register — claim C, §1 "The register property"

- Seat: `KotodamaR52.ScribeSec01Register` (leaf; no subagent dispatch, no background jobs).
- Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, branch `main`, worktree at `dea5ece63ca4372c41766ab242df1e26c2e6898a` (claim D landed) plus another seat's uncommitted edit to the sign-language entry at its lines 87 and 93; base of the round `147cfde85eb13256438c1ed04d92e8d2ad09b76e`.
- Assigned item: draft §1 of the C entry `corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md` — bold master claim, Stern's 1957 split (abridging vs lexical-ideographic), and a `| Test | Pass when | Fails as (owner) |` table separating a speech surrogate from a signal code, a sign language, music and a secret language — within a 14-line budget.
- Date of the source round: 2026-10-22. All external sources below were opened in this session by ordinary means.
- Nothing in the corpus was written, staged or committed by this seat. This report is the only file this seat created.

## 1. Result

- Section text drafted and counted: **13 content lines** (14 with the blank line that separates it from §2) — inside the stated budget of 14 lines, counting the H2 line and the blank lines.
- Every factual claim in the draft carries either a NEW-id (draft row), an in-corpus `path:line`, or an inline `(to-verify)`.
- Partial owners are **pointed at, never restated**: `music-instrument-lexicon.md:98`, `phonetics-phonology.md:197`, `sociolinguistics-registers.md:84`, and the manual-modality owner `sign-languages-manual-modality.md:14`.
- Six content sources were opened this round (rows 1–6 below) plus two public metadata records (rows 7–8). Three of the named sources could not be opened by ordinary means; the substitutes used are named in §6 and the substitution is stated inside the draft text.
- The C entry does not exist yet, so no gate was run against it (see §8).

## 2. Drafted text ready to paste

Paste as the opening section of `corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md`. `NEW-ScribeSec01Register-<n>` are draft row ids; the L1 assigns the real `S134+` ids at integration and this seat's rows must carry `used-by` = that entry path.

```markdown
## 1. The register property: a surrogate carries a spoken language on another channel

**Master claim.** A speech surrogate substitutes the utterances of one spoken language with other sounds, systematically and in the acoustic modality — what Sebeok and Umiker-Sebeok called "a true substitutive system, 2) a first-order rather than a second-order system, and 3) in the acoustic modality" (NEW-1, quoting their 1976 definition; the 1976 volume itself was not opened this round). James's rendering: speech surrogacy is "systematically replacing utterances in 2) a spoken language with 3) other sounds" (NEW-1). A whistled language is "secondary speech codes based on whistles anchored to, and derived from, a spoken language" (NEW-2): Silbo Gomero (Spanish, La Gomera, Canary Islands), Mazatec and Chinantec (Oaxaca, Mexico) and the Surui (Rondônia, Brazil) each ride one spoken language (NEW-3, NEW-2). Status: **B** for the systems the sources describe; the test column is the lane's design frame (**H**).

Stern's 1957 split sorts surrogates by what the signal encodes: phonological "abridgment" systems, where the carrier reduces the spoken language's own sounds, against "lexical ideograph" systems, where the signal "arbitrarily signify words, phrases, or perhaps concepts" with no connection to the phonology of the spoken language (NEW-1, reporting Stern's terms; the page reference the source prints is unresolved `(to-verify)`). The abridging case is the one this entry owns: the signifier-to-signified relation "is not purely symbolic but is based on physical similarity with the vocal signal, combining abridgment and acoustic iconicity" (NEW-3, p. 4).

| Test | Pass when | Fails as (owner) |
|---|---|---|
| **Carries speech** | the signal replaces utterances of a spoken language with other sounds, systematically, in the acoustic modality (NEW-1) | a signal code: a bugle call or a fixed drum signal has "no systematic connection to language", and Morse code refers "to an alphabet rather than to speech itself" (NEW-1) |
| **Anchored in phonology** | the carrier reduces and re-shapes the spoken language's own sounds — abridgment plus acoustic iconicity (NEW-3) | a lexical-ideographic code: the signal fixes word or concept meanings without the spoken phonology (NEW-1) |
| **Not self-standing** | the surrogate stays anchored to, and derived from, one spoken language (NEW-2) | a sign language, which is "self-standing lexically, grammatically, and phonologically" (NEW-2); the manual modality's register test stays at `sign-languages-manual-modality.md:14` |
| **Carries words, not a performance** | the signal carries words and propositions of the spoken language (NEW-1) | music — the instrument register stays at `music-instrument-lexicon.md:98`; the drum and whistle channels at `phonetics-phonology.md:197` |
| **Secrecy in the channel** | the carrier hides the message by changing channel, not the vocabulary (NEW-2: whistled speech is used "to speak in secret from foreigners") | a secret language — anti-languages and registers stay at `sociolinguistics-registers.md:84` |
```

### Line accounting (budget 14)

| line | content |
|---|---|
| 1 | `## 1. The register property: a surrogate carries a spoken language on another channel` |
| 2 | blank |
| 3 | master-claim paragraph |
| 4 | blank |
| 5 | Stern-split paragraph |
| 6 | blank |
| 7 | table header `\| Test \| Pass when \| Fails as (owner) \|` |
| 8 | table separator |
| 9–13 | five data rows (signal code, lexical-ideographic code, sign language, music, secret language) |
| 14 | blank line that closes the section before `## 2.` (not part of the 13 content lines) |

## 3. In-corpus anchors used (re-read in the lane worktree at `dea5ece`)

| cited as | line | what the line says | use in §1 |
|---|---|---|---|
| `linguistics/sign-languages-manual-modality.md` | 14 | `## 1. The register property: a sign language is a full language in the visual-manual modality` | owner pointer for the sign-language row |
| `linguistics/sign-languages-manual-modality.md` | 16 | `**Master claim.** A sign language is a full natural language in the visual-manual modality …` | not quoted in §1; available if §2 needs the owner's master claim |
| `culture-material/music-instrument-lexicon.md` | 98 | `\| instruments that speak \| Yoruba dùndún 'talking drum' mimics lexical tone; Akan atumpan; Lokele drum-speech documented \| …` | owner pointer, music row (pointed at, not restated) |
| `linguistics/phonetics-phonology.md` | 197 | `- Whistled speech: mountains + long-distance herding → whistled registers` | owner pointer, drum/whistle channel |
| `linguistics/phonetics-phonology.md` | 199 | `- Drum language: tone + gongs → tone-and-rhythm coding of set phrases` | available for §3 (typology) |
| `linguistics/sociolinguistics-registers.md` | 84 | `- Anti-languages (Halliday 1976): underworlds, soldiery, prisons relexicalize … while keeping the grammar; …` | owner pointer, secret-language row |

Claim D's edit range does not touch any line cited above: `git diff 147cfde dea5ece -- corpus/knowledge/linguistics/sign-languages-manual-modality.md` shows a single hunk `@@ -80,17 +80,17 @@`, so lines 14 and 16 are unchanged by D, and the C claim's `must_not_cite` (D's changed lines) is respected. All six anchors were re-read in the lane worktree after the round's other seats began editing (the only uncommitted change to the sign-language entry is at its lines 87 and 93, another seat's in-flight work); the text at lines 14 and 16 and at `music-instrument-lexicon.md:98`, `phonetics-phonology.md:197` and `sociolinguistics-registers.md:84` is unchanged.

Other partial owners named in the claim, not restated and not cited in §1 (they belong to §2/§3): `linguistics/orality-formulaic-language.md:114,:124`, `linguistics/sound-symbolism.md:121`.

## 4. Registry row drafts (ids for the L1 to assign from S134 upward)

Columns are the 11 columns of `corpus/SOURCES.md`. `used-by` names the entry that does not exist yet; `status` is `mined` only for the rows the draft text cites.

| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
| NEW-ScribeSec01Register-1 | Lucas James 2021, "Systems of Communication: Aspects of Culture and Structure in Speech Surrogates", *Frontiers in Communication* 6:653268, doi 10.3389/fcomm.2021.653268 — https://www.frontiersin.org/journals/communication/articles/10.3389/fcomm.2021.653268/full | paper | B | the definition, terminology and typology of speech surrogates as surveyed in a peer-reviewed article; Stern's 1957 taxonomy is reported here, not original | "Defining Speech Surrogacy" section, article PDF pp. 1–2 of 15 | a surrogate systematically replaces utterances of a spoken language with other sounds, first-order and in the acoustic modality; alarm bells and Morse code are excluded; Stern's "lexical ideograph" systems against phonologically-based "abridgment" systems; the boundary between the two is contested | mined | 2026-10-22 | 365d | corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md |
| NEW-ScribeSec01Register-2 | Julien Meyer, David Díaz Reyes, Andre Batchelder-Schwab and Bernard Gautheron 2025, "Whistled Languages and Whistled Speech", *Encyclopedia of Language and Linguistics* (Elsevier), author-hosted copy — http://www.lemondesiffle.free.fr/media/WhistledLanguages_and_Whistled_Speech_Encyclopedy.pdf | book | B | the mechanism and social setting of whistled speech as a secondary speech code | Abstract and "Body Text", PDF pp. 1–2 of 17 | whistled languages are secondary speech codes anchored to, and derived from, one spoken language by acoustic iconicity, and are "substantially different from sign languages, which are self-standing lexically, grammatically, and phonologically"; whistled speech serves distance, secrecy and herding | mined | 2026-10-22 | 365d | corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md |
| NEW-ScribeSec01Register-3 | Julien Meyer 2015, *Whistled Languages: A Worldwide Inquiry on Human Whistled Speech*, Springer Heidelberg — public copy at https://archive.org/details/whistled-languages-a-worldwide-inquiry-on-human-whistled-speech-2015 (file `978-3-662-45837-2.pdf`) | book | B | the acoustic mechanism and typology of whistled speech; the abridgment/iconicity argument | Chapter 1 "Introduction", p. 4 (PDF p. 13 of 170); Chapter 7 typology, p. 107 | the whistle-to-utterance relation rests on physical similarity with the vocal signal, "combining abridgment and acoustic iconicity", unlike Morse code's symbolic chain through the alphabet; tonal and non-tonal whistling strategies | mined | 2026-10-22 | 365d | corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md |
| NEW-ScribeSec01Register-4 | Yoad Winter 2014, "On the Grammar of a Senegalese Drum Language", *Language* 90(3): 644–668, doi 10.1353/lan.2014.0061 — author manuscript in the Utrecht University Repository, https://dspace.library.uu.nl/items/88c9294a-10bf-4098-9d7c907e334f | paper | A | the Sabar drum language of Senegalese griots as Winter analyses it | Abstract, repository PDF p. 2 (journal p. 644) | drum languages are speech surrogacy in which a lexicon of rhythms and their meanings maps onto recited text; the rhythms do not acoustically mimic speech; a case that sits near the lexical-ideographic side of the line | queued | 2026-10-22 | 365d | — |
| NEW-ScribeSec01Register-5 | Julien Meyer and Bernard Gautheron 2006, "Whistled Speech and Whistled Languages", *Encyclopedia of Language & Linguistics*, 2nd ed. (Elsevier), author-hosted copy — http://www.lemondesiffle.free.fr/projet/science/ELL34.pdf | book | B | the description of whistled speech as an abridgment of speech | PDF p. 3 of 14 | whistled speech is identified as an abridgment of speech that encodes the essential phonology of the spoken language | queued | 2026-10-22 | 365d | — |
| NEW-ScribeSec01Register-6 | Laura McPherson 2021/2022, "Categoricity, Variation, and Gradience in Sambla Balafon Segmental Encoding", *Frontiers in Communication* 7:838286, doi 10.3389/fcomm.2021.652635 — in the open-access research topic "Surrogate Languages and the Grammar of Language-Based Music" (Winter & McPherson eds 2022, doi 10.3389/978-2-88974-716-0), copy at https://www.phil.uu.nl/~yoad/papers/WinterMcPhersonVolume.pdf | paper | B | a balafon surrogate system and the segmental encoding it carries | chapter opening, eBook PDF pp. 7–17 (Front. Commun. 7:838286) | a West African balafon surrogate maps language onto an instrument's own segmental system, so the surrogate's structure is jointly fixed by the language and the instrument | queued | 2026-10-22 | 365d | — |
| NEW-ScribeSec01Register-7 | Sebeok, Thomas A. and Umiker-Sebeok, Donna Jean (eds) 1976, *Speech Surrogates: Drum and Whistle Systems*, The Hague: Mouton — bibliographic record via Crossref, https://api.crossref.org/works/10.1515/9783110804416 | docs | B | the 1976 volume's bibliographic identity only (part 1 record: title, editors Thomas A. Sebeok, Alain Rey, Roland Posner; publisher DE GRUYTER; ISBN 9789027934239 / 9783110804416) | Crossref record fields `title`, `editor`, `publisher`, `ISBN` | resolves the volume's citation and part structure; it carries no substantive claim by itself, and the volume's own pages were not opened this round | queued | 2026-10-22 | 365d | — |
| NEW-ScribeSec01Register-8 | Stern, Theodore 1957, "Drum and Whistle 'Languages': An Analysis of Speech Surrogates", *American Anthropologist* 59(3): 487–506, doi 10.1525/aa.1957.59.3.02a00070 — bibliographic record via Crossref, https://api.crossref.org/works/10.1525/aa.1957.59.3.02a00070 | docs | B | the 1957 article's bibliographic identity only (title, journal, volume 59, issue 3, pages 487–506, June 1957) | Crossref record fields `title`, `container-title`, `volume`, `issue`, `page`, `published-print` | resolves Stern's citation and page range; the article's own text was not opened this round, so the taxonomy is cited through NEW-1 | queued | 2026-10-22 | 365d | — |

Advice for the integrator: rows 7 and 8 are metadata-only rows. If the lane prefers a single row per source, fold their citation data into row 1's `teaches` and drop them; keep the "not opened this round" note in the entry text either way, because the C claim's falsifier turns on rows that were genuinely opened.

## 5. Gate lines (for `corpus/lessons/round-52.md`)

Format follows `corpus/lessons/round-49.md:27-31`: `- <id> — <URL> — accessed <date> — <locator>: "<quote>". Grounds: <one line>.`

- NEW-ScribeSec01Register-1 — https://www.frontiersin.org/journals/communication/articles/10.3389/fcomm.2021.653268/full — accessed 2026-10-22 — "Defining Speech Surrogacy", article PDF p. 1: "speech surrogacy is a practice of 1) systematically replacing utterances in 2) a spoken language with 3) other sounds". Grounds: the master claim — a surrogate substitutes a spoken language's utterances with other sounds.
- NEW-ScribeSec01Register-1 — https://www.frontiersin.org/journals/communication/articles/10.3389/fcomm.2021.653268/full — accessed 2026-10-22 — "Defining Speech Surrogacy", article PDF p. 1: "An alarm bell (say) does not count, as it violates 1) by having no systematic connection to language". Grounds: the signal-code row of the table.
- NEW-ScribeSec01Register-1 — https://www.frontiersin.org/journals/communication/articles/10.3389/fcomm.2021.653268/full — accessed 2026-10-22 — "Defining Speech Surrogacy", article PDF p. 1: "Morse code does not count, as it violates 2) by referring to an alphabet rather than to speech itself". Grounds: the signal-code row, second case.
- NEW-ScribeSec01Register-1 — https://www.frontiersin.org/journals/communication/articles/10.3389/fcomm.2021.653268/full — accessed 2026-10-22 — "Defining Speech Surrogacy", article PDF p. 2: "this is what Stern (1957) calls “lexical ideograph” systems, in contrast with phonologically-based “abridgment” systems". Grounds: Stern's 1957 split, the section's second paragraph.
- NEW-ScribeSec01Register-1 — https://www.frontiersin.org/journals/communication/articles/10.3389/fcomm.2021.653268/full — accessed 2026-10-22 — "Defining Speech Surrogacy", article PDF p. 2: "the line between abridging and lexical ideograph systems is harder to draw than it appears". Grounds: calibration — the boundary is contested, so the entry must not present the two kinds as a clean partition.
- NEW-ScribeSec01Register-1 — https://www.frontiersin.org/journals/communication/articles/10.3389/fcomm.2021.653268/full — accessed 2026-10-22 — "Defining Speech Surrogacy", article PDF p. 1: "specimens of one species of transmutation, one which is 1) a true substitutive system, 2) a first-order rather than a second-order system". Grounds: the 1976 definition as James quotes it (the 1976 volume itself was not opened this round).
- NEW-ScribeSec01Register-2 — http://www.lemondesiffle.free.fr/media/WhistledLanguages_and_Whistled_Speech_Encyclopedy.pdf — accessed 2026-10-22 — Abstract, PDF p. 1: "Whistled languages are secondary speech codes based on whistles anchored to, and derived from, a spoken language thanks to a relation of acoustic iconicity." Grounds: the master claim's second sentence.
- NEW-ScribeSec01Register-2 — http://www.lemondesiffle.free.fr/media/WhistledLanguages_and_Whistled_Speech_Encyclopedy.pdf — accessed 2026-10-22 — "Body Text", PDF p. 2: "this also makes them substantially different from sign languages, which are self-standing lexically, grammatically, and phonologically". Grounds: the sign-language row of the table.
- NEW-ScribeSec01Register-2 — http://www.lemondesiffle.free.fr/media/WhistledLanguages_and_Whistled_Speech_Encyclopedy.pdf — accessed 2026-10-22 — "Geographical and Social Environments", PDF p. 2: "It is also often employed to speak in secret from foreigners or to remain hidden from animal prey". Grounds: the secrecy row of the table.
- NEW-ScribeSec01Register-3 — https://archive.org/details/whistled-languages-a-worldwide-inquiry-on-human-whistled-speech-2015 — accessed 2026-10-22 — Chapter 1 "Introduction", p. 4 (PDF p. 13): "is not purely symbolic but is based on physical similarity with the vocal signal, combining abridgment and acoustic iconicity". Grounds: the abridgment-and-iconicity argument the entry's second paragraph rests on.
- NEW-ScribeSec01Register-3 — https://archive.org/details/whistled-languages-a-worldwide-inquiry-on-human-whistled-speech-2015 — accessed 2026-10-22 — Chapter 1 "Introduction", p. 4: "Morse code relies on an intermediary, purely symbolic code that refers to the written alphabet". Grounds: why Morse code is a signal code and not a surrogate.
- NEW-ScribeSec01Register-4 — https://dspace.library.uu.nl/items/88c9294a-10bf-4098-9d7c907e334f — accessed 2026-10-22 — Abstract, repository PDF p. 2 (journal p. 644): "These practices of speech surrogacy are often referred to as drum languages." Grounds: the drummed-speech section's terminology.
- NEW-ScribeSec01Register-4 — https://dspace.library.uu.nl/items/88c9294a-10bf-4098-9d7c907e334f — accessed 2026-10-22 — Abstract, repository PDF p. 2: "The rhythms do not acoustically mimic speech, and the speech-drum matching is based on a lexicon of rhythms and their meanings." Grounds: a drum language on the lexical-ideographic side of the line; supports §5 and the calibration bank.
- NEW-ScribeSec01Register-5 — http://www.lemondesiffle.free.fr/projet/science/ELL34.pdf — accessed 2026-10-22 — PDF p. 3: "identified as abridgments of speech that encode essential phonology". Grounds: the older encyclopedic statement of the abridgment definition.
- NEW-ScribeSec01Register-6 — https://www.phil.uu.nl/~yoad/papers/WinterMcPhersonVolume.pdf — accessed 2026-10-22 — McPherson chapter opening, eBook PDF p. 7 (Front. Commun. 7:838286): "Categoricity, Variation, and Gradience in Sambla Balafon Segmental Encoding". Grounds: a balafon surrogate whose structure is fixed jointly by the language and the instrument.
- NEW-ScribeSec01Register-7 — https://api.crossref.org/works/10.1515/9783110804416 — accessed 2026-10-22 — record fields `title`, `editor`, `publisher`, `ISBN`: "Speech Surrogates, Part 1". Grounds: resolves the 1976 volume's citation only; no substantive claim.
- NEW-ScribeSec01Register-8 — https://api.crossref.org/works/10.1525/aa.1957.59.3.02a00070 — accessed 2026-10-22 — record fields `title`, `volume`, `issue`, `page`: "Drum and Whistle “Languages”: An Analysis of Speech Surrogates", 59(3), 487-506. Grounds: resolves Stern's citation and page range only; the taxonomy is cited through NEW-1.

## 6. Named sources that could not be opened, and the substitutes used

All attempts below used plain `curl` requests. No headless browser, captcha solver, login or paywall bypass was used at any point, and no source row is drafted for a page that was not actually reached.

| named source | attempt | outcome | substitute |
|---|---|---|---|
| Stern 1957, publisher page — https://anthrosource.onlinelibrary.wiley.com/doi/10.1525/aa.1957.59.3.02a00070 | plain GET | returned a Cloudflare "Just a moment..." challenge page (5,664 bytes) — an access control, so not opened | taxonomy via NEW-1 (James 2021, opened); citation via NEW-8 (Crossref, opened) |
| Stern 1957, JSTOR — https://www.jstor.org/stable/665914 | plain GET; Wayback availability API | blocked (no article body returned); Wayback availability API rate-limited (HTTP 429) on every retry | as above |
| Sebeok & Umiker-Sebeok 1976, De Gruyter — https://www.degruyter.com/document/doi/10.1515/9783112321243/html and https://www.degruyterbrill.com/document/doi/10.1515/9783112321243/html | plain GET, two hostnames, two DOIs | zero-byte response; the second host returns an AWS WAF cookie script — an access control, so not opened; the Wayback CDX query for the page returned an empty capture list | the definition is quoted verbatim inside NEW-1 (opened, with its own locator); the bibliographic identity is NEW-7 (Crossref, opened). The draft text says "the 1976 volume itself was not opened this round" |
| Meyer 2015, Springer page — https://link.springer.com/book/10.1007/978-3-662-45837-2 | plain GET | bot-challenge page (3,038 bytes) — not opened | the monograph was opened as a public copy at archive.org (NEW-3) |

Ordinary means that did work: a Frontiers open-access article page and PDF, author-hosted PDFs that the publisher states it supplied to the author, a repository author manuscript (Utrecht University Repository), an archive.org public copy of a Springer monograph, the Frontiers open-access eBook copy on a university site, and the public Crossref metadata API.

## 7. Calibration notes for the integrator

- Master claim: **B** (bounded to the systems the opened sources describe). The test column is the lane's design frame, **H** (`../verification/calibration-registry.md:38`).
- Stern's split is attributed as reported by NEW-1, not as read in the original; the printed page reference in the source ("(172)") is not resolvable in the open text, so the draft carries it as `(to-verify)`.
- The abridging / lexical-ideographic boundary is contested in the source itself (NEW-1, PDF p. 2) and Winter's Sabar case sits near the lexical side (NEW-4). Advice: the entry's calibration bank should carry this as **C**, not as a settled partition, and §5 should promote NEW-4 to `mined` with `used-by` = the C entry.
- Named communities and languages are given with their precise names and locations (Silbo Gomero, Spanish, La Gomera; Mazatec and Chinantec, Oaxaca; Surui, Rondônia; Sabar drums, Senegal). No community is exoticized, no living community's rights or heritage policy are ruled on, and nothing in §1 touches canon.
- §1 states a register property and a boundary test only; it does not decide what any world contains.

## 8. Unrun checks and limits

- The C entry does not exist yet, so the round-50 mechanical checker (§2.9-A), the provenance gate, the couples resolver, the README sweep and the S-id/`used-by` check (§2.9-B) could not be run against it. Only the §1 text was line-counted here.
- S-ids S134 upward are not assigned; the rows above are drafts with `NEW-ScribeSec01Register-<n>` ids.
- `tools/check-source-access.py` was not run: the drafted rows are not in `corpus/SOURCES.md`, and this seat writes no corpus file. The rows were checked against the criterion-10 rule by hand — none records a headless browser, a solved captcha, a bypassed paywall or a login.
- `reports/round-28/readme/sweep.py`, `tools/check-readme-heading.py`, `tools/check-readme-revisions.py` were not run; this seat touches neither `corpus/README.md` nor the entry.
- No git or jj mutating command was run in the lane; the only git use was read-only (`git log`, `git status`, `git diff` between two commits).
- Scope note: this seat drafted §1 only. §2 (one-owner boundary), §3 (typology), §4 (whistled speech), §5 (drummed speech), §6–§14 are other seats' or the L1's work; the rows in §4 are offered as opened evidence, not as a claim about those sections.

## 9. Tooling record

- No installs and no updates. Nothing was installed, upgraded, downgraded or removed; no pacman transaction was run (host-wide pacman transactions are paused).
- Tools used, all already present on the host: `curl`, `pdftotext` (poppler), `file`, `grep`, `awk`, `python3` (system), `git` (read-only). Temporary downloads were written under `/tmp` only; no lane file was written except this report.
