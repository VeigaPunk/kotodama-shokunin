# ReviewCSec07: falsify attack on claim C, entry §7 (iconicity and arbitrariness)

- Seat: KotodamaR51a3.ReviewCSec07 (leaf reviewer; read-only on the lane; no delegation, no background jobs).
- Wave: round 51, attempt 3, falsify. Claim C landed at commit `da31d3c`.
- Attacked item: `corpus/knowledge/linguistics/sign-languages-manual-modality.md` §7, lines 110–120; rows S101, S102, S103 (`corpus/SOURCES.md:130–132`); in-corpus anchors `corpus/knowledge/linguistics/sound-symbolism.md:25,:32,:124`.
- Access date for every source below: 2026-10-22.
- Byte check: the working-tree blob equals the HEAD blob `b79c679f…` (223 lines), so the attacked text is the landed text.

## Verdict: HOLDS-WITH-FIXES

The core §7 claims survive at the scope their sources support:

- S101 reports handling and instrument strategies that differ across three unrelated sign languages, for hand-held tools.
- S102 reports a tendency for ASL signs to change toward arbitrariness.
- S103 (ch. 2, p. 8) treats the TREE forms as motivated but not determined by meaning.

As landed, §7 does not clear QUALITY criterion 1 in two places: an uncited clause (L112) and a Shape row that misreports its anchor (L118). The typology and design-use cells also lack clean provenance (criteria 1 and 6). Every fix is local: one row, one clause, one table block, three new registry rows, one superseding row. None of them changes claim C's file count or sweep.

## Findings (by severity)

Pointers are `file:line` in the lane. "L" means a line of the entry.

### F1 — HIGH — L118, Shape row
Text: "the hands trace the referent's outline — ASL, Danish and Chinese TREE are equally iconic yet trace differently (S103)".
- S103, excerpt p. 8: ASL TREE "the hands and forearms are positioned to resemble a tree growing out of the ground". Only the Danish and Chinese forms are described as tracing.
- The Danish trace description is contested. Hwang et al. 2017 p. 575 says Engberg-Pedersen (2004) "corrects the record": the Danish TREE sign is represented like the ASL-type form, "unlike what Klima and Bellugi (1979) describe". Engberg-Pedersen 2004 is a review of Taub's own book (Hwang reference list, p. 600). I did not open it.
- Hwang p. 575: "Both examples exemplify the strategy we call object" (the TREE pair, its Figs 1a–1b). Object forms are hands alone depicting size and shape, with the body de-emphasized (p. 577). So the TREE forms share one strategy; they do not "trace differently" as strategies.
- Smallest fix: replace the row with the object strategy and cite the registered Hwang row. Drop "trace differently". If Danish stays, mark it contested (Engberg-Pedersen 2004, via Hwang p. 575).

### F2 — HIGH — L112 ("pick a strategy — handling, instrument, or shape") and L114–118 (three-row table)
- Each row carries a source tag, but no cited source states this three-part list. S101 states two strategies (handling and instrument; abstract). S103 states none; its scope cell's "shape/outline strategies" is not in the excerpt (see F6).
- Hwang 2017 (pp. 576–577) gives two levels: manipulation, which divides into handling and instrument; object; and personification (animals). The table mixes levels (handling and instrument are two kinds of manipulation; object is a sibling category) and omits personification.
- Smallest fix: restate the typology per Hwang 2017 with its citation. Keep S101's handling/instrument pair attributed to S101. Mark anything else H.

### F3 — HIGH — L112, last clause: "— a young sign language reads more iconic than an old one"
- No S-id, no (H), no (to-verify). QUALITY criterion 1 (`corpus/QUALITY.md:5–8`) requires unverifiable claims to be marked "(to-verify)" and never laundered into assertion.
- The nearest sources do not carry a cross-language rule. Hwang 2017 p. 599 only speculates that fruit-and-vegetable strategies may change "as a function of language age". Pyers & Senghas 2020 (PMC7894619, §3.2) studies one emerging language, Nicaraguan Sign Language: 8 signers (4 + 4), 26 signs. Pantomimic iconicity fell from 63% (first cohort) to 45% (third), t(6)=3.95, p=.008; the perceptual change was non-significant. The abstract frames the general decline as "a puzzle".
- Smallest fix: delete the clause. Or write it as (H), citing only the NSL result, after registering Pyers & Senghas 2020.

### F4 — MEDIUM — L116–118, design-use column
- Unmarked. Unanchored design choices are H (`corpus/knowledge/verification/calibration-registry.md:38`; entry L164). No cell cites a registered row.
- "Handling → action/verb scenes; agent focus": S101 says nothing about verbs or agents. Hwang p. 599 says tools "are overwhelmingly represented through manipulation forms", and handling is one of the two manipulation forms, so handling also names tools. Candidate support is Brentari et al. 2015, reported at Hwang p. 598 as aligning handling handshapes with events involving human agents; I did not open it. Padden et al. 2015 ("nouns and verbs", Topics in Cognitive Science 7(1):81–94) is the other candidate; Wiley returned 403, so I could not open it.
- "Instrument → noun lexicon; tool categories": consistent with Hwang p. 599 and the S101 abstract on tools, but unregistered and incomplete, since handling also names tools.
- "Shape → depicting constructions; spatial layout": no source. Hwang p. 599 pairs object forms with fruit and vegetables; Hwang p. 595 pairs them with small or aquatic animals. Brentari 2015 (via Hwang p. 598) pairs object handshapes with object motion that involves no human agent.
- Smallest fix: mark the column H. Cite Hwang pp. 595, 598–599 and Brentari 2015 (once opened) for the category links. Drop "action/verb" unless Padden 2015 is opened.

### F5 — MEDIUM — L112 and L120, S101 claims
- The S101 abstract (`benjamins.com/catalog/gest.13.3.03pad`) describes "an elicitation task featuring pictures of hand-held manufactured tools", with hearing silent gesturers and signers of "three unrelated sign languages". §7 widens this to "lexical strategies" in general and to "no universal sign".
- Tier B is right: the row rests on the abstract only (QUALITY criterion 6, `corpus/QUALITY.md:29`). But calibration code B requires the task and population to be carried, with "no extrapolation by resemblance" (`calibration-registry.md:37`).
- Smallest fix: "In a picture-naming task for hand-held tools, signers of three unrelated sign languages differ in handling and instrument use (S101)."

### F6 — MEDIUM — `corpus/SOURCES.md:132` (S103 scope and teaches cells)
- The scope cell says the chapters teach "shape/outline strategies". The excerpt does not contain that: pp. 1–10 hold the TREE comparison (p. 8) and the motivation definition (p. 9).
- The teaches cell repeats "ASL/Danish/Chinese TREE all iconic, different forms" without the Engberg-Pedersen correction (F1).
- Smallest fix: a superseding row. `SOURCES.md:9–12` requires a new row whose teaches cell opens "supersedes S103 —"; no in-place edit. Draft below.

### F7 — MEDIUM — coverage (the judged axis)
- §7 rests on three registered rows, and S103 is ASL-only.
- Open-access or abstract-readable sources that are absent:
  - Hwang et al. 2017 (open access, CC BY 4.0). It is the classification §7 needs, and it revises the Klima & Bellugi "unpredictability" argument (pp. 574–575), which §7 presents as settled through S103.
  - Pyers & Senghas 2020. It is the only cohort data on iconicity change in the lane's reach, and it separates pantomimic from perceptual iconicity. §7 uses "pantomime" only as a foil.
  - Nyst et al. 2022 (Linguistic Typology 26(3); online 2021-12-10; Crossref abstract). It covers 11 sign languages, mostly African, reports "significant variation", and calls for going beyond the "instrument/manipulation alternation". It tests §7's "no universal sign" and its typology directly.
- Still-unopened leads: Padden et al. 2015 (TopiCS); Battison & Jordan 1976 (cited at Hwang p. 596); Brentari et al. 2015; Engberg-Pedersen 2004; Klima & Bellugi 1979 (p. 21).
- Smallest fix: register the first three (drafts below) and cite them in §7. List the others as leads.

### F8 — LOW — L112, "every iconic form is motivated but not determined (S103)"
- Taub uses "motivated" for a tendency, "rather than a strict rule" (excerpt p. 9). "Not determined" is shown for the TREE forms (p. 8). "Every" is not in S103.
- Smallest fix: "Taub (2001, ch. 2) finds the TREE forms motivated but not determined by meaning (S103)."

### F9 — MEDIUM — terminology: "conventional"
- L120, "iconic forms are conventional, standard lexicon (S103)", uses Taub's sense (standardized). The same section's arbitrariness drift (L112) and this corpus's own definition, "arbitrariness … form and meaning related by convention only" (`sound-symbolism.md:25`), make "conventional" read as "arbitrary". Same word, opposite meaning. L64 ("not a conventional system") uses the word too.
- Smallest fix: say "standardized" or "lexicalized" for Taub's sense. Define the word once in §7, or drop it.

### F10 — LOW — terminology: "conventionalization" (L112)
- It is used as the mechanism of drift toward arbitrariness. In Pyers & Senghas (§1 and §4), conventionalization means convergence on fewer variants. Loss of transparency, such as dropping pantomimic elements (§3.3), is a separate process.
- Smallest fix: name the two processes separately.

### F11 — LOW — L120, "there is no universal sign"
- S101 does not test universality. Hwang 2017 p. 596 says "there is not a universal sign language (Battison & Jordan, 1976)". §13 (L203) already says "universal sign language".
- Smallest fix: "there is no universal sign language (cf. §13)."

### F12 — LOW — L120, "sign is not mime" (cites S103)
- The excerpt sentence (p. 2) concerns ASL features, and S103 is an ASL book. The general claim has support at Hwang 2017 p. 597 ("sign languages are not pantomime").
- Smallest fix: scope to ASL, or cite Hwang.

### F13 — LOW — L112, "patterned, not pantomime"
- S101 also finds that silent gesturers "largely prefer a handling strategy", which is itself a patterned preference. The contrast S101 draws is shared patterns in gesture and sign, with variation across sign languages. It is not pattern versus pantomime.
- Smallest fix: state the gesturer finding.

### F14 — LOW — L116, handling gloss attributed to S101
- The S101 abstract defines instrument, not handling. Hwang p. 577 defines handling as "the hands show how an object is held by human hands".
- Smallest fix: cite Hwang for the handling gloss.

### F15 — LOW — L118 and L120, Klima & Bellugi not credited
- The TREE comparison is Klima & Bellugi's (1979, p. 21), reported in S103 and in Hwang p. 574.
- Smallest fix: "(Klima & Bellugi 1979, as reported in S103)."

### F16 — LOW — terminology across sections
- §6 L105, "entity vs handling types (S099)", and §7 L117, "instrument", name the same contrast: a handshape that represents the object. Hwang p. 577 separates instrument from object.
- Smallest fix: one sentence mapping entity (S099) to instrument and object. I did not open S099.

### F17 — LOW — bibliographic
- `SOURCES.md:130` gives the author as "Seegers Marie". The 2015 reprint page and Hwang 2017 (author line and reference list) give "Sharon Seegers". The 2013 catalog page lists "Aron Seegers Marie" for the same person ID.
- `SOURCES.md:131` has no DOI. The listing gives 10.2307/412894, taken from a search snippet; I did not open it.
- Smallest fix: correct the name and add the DOI.

### F18 — LOW (nit) — L120 anchor `sound-symbolism.md:32`
- The three definitions sit at :25–31. Line :32 is the design-consequence sentence. Smallest fix: cite :25–32.

### Checked and found clean
- No canon decision, clinical, education-policy or rights ruling appears in §7 (L110–120).
- Every S-id in §7 (S101, S102, S103) exists in `SOURCES.md`, and their used-by cells name the entry path.
- The entry does not name `corpus/lessons/round-51.md` or `reports/round-51/boundary-count.py` (grep: no matches).

## What survived the attack
- S101: the abstract quote is verbatim on the catalog page. "Three unrelated sign languages" holds. "Distribution differs" holds at abstract scope.
- S102: the ERIC abstract quote is verbatim. The drift claim holds at abstract scope (ASL, historical). Pyers & Senghas §1 reads Frishberg the same way and notes that her data cover about a century without analysis of mapping type, so the drift claim must not be extended to mapping types.
- S103: the Gate quote is verbatim at p. 2. "Motivated but not determined" holds for the TREE forms (p. 8). "Conventional features … not mime … standard ASL textbooks and dictionaries" holds for ASL.
- `sound-symbolism.md:124` matches the entry's description ("iconicity is a general property, stronger in signed languages", marked to-verify there).

## Proposed registry rows (drafts for the integrator; I did not write SOURCES.md)

Row A — Hwang, So-One, Nozomi Tomita, Hope Morgan, Rabia Ergin, Deniz İlkbaşaran, Sharon Seegers, Ryan Lepic & Carol Padden 2017, "Of the body and the hands: patterned iconicity for semantic categories", Language and Cognition 9(4):573–602, doi 10.1017/langcog.2016.28 — https://pure.mpg.de/rest/items/item_2506606/component/file_2506605/content (open access, CC BY 4.0) | paper | A (scope: eight sign languages plus American non-signer gesture; picture naming of tools, animals, fruit and vegetables) | pp. 575–577 (classification); pp. 596–599 (general discussion) | manipulation (handling, instrument) for tools; object (body de-emphasized); personification for animals; "there is not a universal sign language (Battison & Jordan, 1976)" (p. 596) | mined | 2026-10-22 | 365d | corpus/knowledge/linguistics/sign-languages-manual-modality.md

Row B — Pyers, Jennie & Ann Senghas 2020, "Lexical iconicity is differentially favored under transmission in a new sign language: the effect of type of iconicity", Sign Language & Linguistics 23(1–2):73–95, doi 10.1075/sll.00044.pye — https://pmc.ncbi.nlm.nih.gov/articles/PMC7894619/ (author manuscript) | paper | A within scope (one emerging language, Nicaraguan Sign Language; 8 signers; 26 signs) | Abstract; §3.2 | pantomimic iconicity 63% (first cohort) → 45% (third), t(6)=3.95, p=.008; perceptual change non-significant | mined | 2026-10-22 | 365d | corpus/knowledge/linguistics/sign-languages-manual-modality.md

Row C — Nyst, Victoria, Marta Morgado, Timothy Mac Hadjah, Marco Nyarko, Mariana Martins, Lisa van der Mark, Evans Burichani, Tano Angoua, Moustapha Magassouba, Dieydi Sylla, Kidane Admasu & Anique Schüller 2022, "Object and handling handshapes in 11 sign languages: towards a typology of the iconic use of the hands", Linguistic Typology 26(3), doi 10.1515/lingty-2021-0026 — https://doi.org/10.1515/lingty-2021-0026 (Crossref abstract; full text not opened) | paper | B (abstract only) | Abstract | "significant variation" across 11 sign languages in embodying and handling handshapes; the instrument/manipulation alternation is "now relatively well studied" | mined | 2026-10-22 | 365d | corpus/knowledge/linguistics/sign-languages-manual-modality.md

Row D (superseding S103) — "supersedes S103 — scope narrowed to ch. 1 p. 2 and ch. 2 pp. 8–9 (ASL): the TREE comparison (p. 8) describes ASL TREE as positioned, not traced; the excerpt has no strategy typology; the Danish trace description is contested (Engberg-Pedersen 2004, via Hwang 2017 p. 575)." | book | A (Taub's own ASL text) | opened 2026-10-22 | used-by: the entry path.

Gate quotes to log in the round lesson (verbatim as read):
- Hwang p. 575: "Engberg-Pedersen (2004) corrects the record and reports that the Danish Sign Language sign for 'tree' is also represented in this way …, unlike what Klima and Bellugi (1979) describe."
- Hwang p. 577: "(i) 'instrument', in which the hands depict the size and shape of an object, and (ii) 'handling', in which the hands show how an object is held by human hands."
- Hwang p. 599: "tools are overwhelmingly represented through manipulation forms, where the body depicts the body of a human agent."
- Pyers & Senghas §3.2: "pantomimic iconicity, where it was included in 63% of the first cohort's signs, but only in 45% of the third-cohort's responses (t(6)=3.95, p=.008)."
- Taub p. 8: "in ASL TREE (see Fig. 3.1), the hands and forearms are positioned to resemble a tree growing out of the ground".

## Commands run (exit codes)

| # | Command or call | Output (abridged) | Exit |
|---|---|---|---|
| 1 | `_bash`: `realpath -m` on the falsify folder; `test -d`; `git --no-optional-locks log --oneline -3` on the entry; `rev-parse HEAD:<entry>`; `git hash-object <entry>`; `wc -l`; `date -u` | folder resolves under the lane; "falsify dir exists"; last commit touching entry `da31d3c`; HEAD blob `b79c679f…`; worktree blob `b79c679f…`; 223 lines; 2026-10-22 | 0 (chain completed; git steps individually 0, 0, 0) |
| 2 | `_bash`: `command -v pdftotext curl python3`; `import pypdf`; `import pdfminer` | `/usr/bin/pdftotext`, `/usr/bin/curl`, `/usr/bin/python3`; pypdf absent; pdfminer absent | not captured (availability probe) |
| 3 | `_bash`: `curl -sL --max-time 120 <Hwang PuRe PDF> \| pdftotext -layout - -` | 1,363 text lines; second run 98,556 characters | PIPESTATUS 0 0 0 |
| 4 | `_bash`: `ls -la .ufo/waves/round-51/falsify/` | 23 peer files; no `ReviewCSec07.md` before this write | 0 |
| 5 | `_grep`: `round-51\|boundary-count\|lessons/round` on the entry | no matches | no match |
| 6 | `_grep`: `S10[0-4]` in SOURCES; `(?i)iconic` in SOURCES; age/emergence pattern in SOURCES; lead names (Hwang, Battison, Nyst, Padden 2015, Pyers, Senghas 2020, Lepic) in SOURCES; lead names and "diminish" in `corpus/`; `(?i)iconic\|arbitrar\|S10[123]` in the round-51 lesson | rows S098–S104; no registry row for any lead (only unrelated S091 Nyst 2007 and S094 Battison 1974); lesson Gate lines 58–60 | n/a (search) |
| 7 | `_read`: claims.json; RULES.md; the entry (full); QUALITY.md; SOURCES header and rows 129–133 (raw); calibration-registry.md; sound-symbolism.md 25–40 and 119–127; entry L4 (raw) | all read | n/a |
| 8 | `_read`: `ScribeSec07Iconicity.md` (author-lane context only, not evidence); `_glob` of the build folder | 37 build files; author's known-limits section noted | n/a |
| 9 | `web_search` ×5 | leads only (Padden 2013 open copy, Frishberg details, Hwang 2017 citation, Padden 2015 snippet, Nyst); no snippet treated as an opened source | n/a |

## Sources opened (2026-10-22)

| URL | What I did | Result | Does the row hold? |
|---|---|---|---|
| `https://www.benjamins.com/catalog/gest.13.3.03pad` (S101) | opened | Abstract read; full text "authorization required" | Quote verbatim; tier B holds; scope holds only once task and population are stated (F5) |
| `https://benjamins.com/catalog/bct.70.03pad` (2015 reprint of S101) | opened | Same abstract; "Where do nouns come from?" pp. 43–63 | Confirms abstract; adds nothing |
| `https://eric.ed.gov/?id=EJ124326` (S102) | opened twice: first attempt timed out; second attempt OK | ERIC abstract and metadata (Language 51(3), 696–719) | Quote verbatim; tier B holds; ASL-historical scope holds |
| `https://www.jstor.org/stable/412894` (S102 full text) | opened | "Client Challenge" page, no text | Not checked (as the row says) |
| `https://www.cambridge.org/core/journals/language/article/arbitrariness-and-iconicity-…` (S102) | opened | HTTP 429 | Not checked (as the row says) |
| `https://assets.cambridge.org/97805217/70620/excerpt/9780521770620_excerpt.pdf` (S103) | opened (PDF converted to text) | ch. 1 pp. 1–3; ch. 2 pp. 8–10 | Gate quote verbatim (p. 2); tier A holds for Taub's own text; scope fails for "shape/outline strategies" (F6) and for the Shape row's ASL example (F1) |
| `https://onlinelibrary.wiley.com/doi/10.1111/tops.12121` and `/doi/full/…` (Padden 2015) | opened (two URLs) | HTTP 403 both | Not checked |
| `https://signlab.haifa.ac.il/…/2013-Padden-…-offprint-copy.pdf` (author-hosted S101) | opened | "Request Rejected" HTML page | Not checked |
| `https://pmc.ncbi.nlm.nih.gov/articles/PMC7894619/` (Pyers & Senghas 2020) | opened | Author manuscript: abstract, §1, §3.1–3.3, §4 | Candidate Row B |
| `https://pure.mpg.de/rest/items/item_2506606/component/file_2506605/content` (Hwang 2017, open access) | first `read`: binary, not converted; then `curl` and `pdftotext` | Full text, pp. 573–602 | Candidate Row A |
| `https://doi.org/10.1515/lingty-2021-0026` (Nyst et al.) | opened via Crossref | Abstract | Candidate Row C (tier B) |

## Residual risk and verification gaps
- S101 and S102 full texts were not reachable (authorization required; JSTOR challenge; Cambridge 429; Wiley 403). Both are read at abstract scope, which is the tier they carry.
- Hwang 2017 was read from text extraction (`pdftotext -layout`). I did not view the figures. The figure-to-language mapping I rely on is the paper's own text.
- Engberg-Pedersen 2004, Klima & Bellugi 1979, Brentari et al. 2015, Padden et al. 2015, Battison & Jordan 1976 and Battison 1978 are cited through Hwang or Pyers & Senghas. I did not open them.
- Nyst et al. was read from the Crossref abstract only.
- My reading that ASL TREE is not a tracing form rests on Taub's own text (p. 8) and on Hwang's description of Fig. 1a (elbow resting on the other hand). The two agree.
- I did not read the peer reports in the falsify folder, to keep the attack independent. Author-lane context (`ScribeSec07Iconicity.md` §6) noted that the Shape row came from Taub's TREE examples rather than from Padden's typology. I treat that as context, not evidence.

## Unrun checks (outside §7 scope; listed as unrun)
- `find corpus/knowledge -name '*.md' | wc -l` (expect 227)
- `python3 -B reports/round-28/readme/sweep.py` (expect exit 0, total 227, linguistics 26)
- `python3 -B reports/round-51/boundary-count.py` (claim D)
- `python3 -B tools/check-claim-separability.py reports/round-51/separability-manifest.json` (expect exit 0)

## Tooling
No installs or updates. I used the existing `/usr/bin/pdftotext` and `/usr/bin/curl`, streamed to stdout, and wrote no file. No pacman, uv, npm or cargo was used. Nothing was written to the lane except this report.
