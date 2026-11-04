# ScoutOverlap — round 89 w1 reconnaissance (read-only)

Lane HEAD read: `9ad00be1a48d33a4f54e1663a1d46e4590cc3438` (freeze 1cbd0efc, base 42816d25). All paths are relative to
`/home/vgpnk/Projects/shokunin/kotodama-shokunin` unless absolute. Probes 2026-11-04T19:10-03:00 (local), plain curl,
no challenge passed. These probes are recon only. They are NOT F captures: the F author seats must fetch and commit their own.

## (a) Evidentiality in the corpus today

### Dedicated evidentiality content (the substantive surface)

| path:line | gist |
|---|---|
| corpus/knowledge/linguistics/semantics-pragmatics.md:3 | topic names "evidentials" as one of four "act through it" devices |
| semantics-pragmatics.md:6 | recheck clause: "before using a classifier/evidential datum" |
| semantics-pragmatics.md:7 | couples: myth files "(name-taboo, dream ontology, omen registers feed mirativity)" |
| **semantics-pragmatics.md:66** | `## 4. Evidentiality and mirativity: grammar of where you know from`, the only `##` section on the topic in the corpus |
| semantics-pragmatics.md:68 | "Evidentials mark information **source**; miratives mark **unexpectedness** (DeLancey 1997)… Evidential ≠ epistemic modality (certainty): Palmer (1986) keeps them separate." |
| semantics-pragmatics.md:69 | Willett (1988) hierarchy, attested > inferred > reported |
| semantics-pragmatics.md:70 | Tuyuca 5 suffixes (Barnes 1984); Cusco Quechua -mi/-si/-chá; Korean -te; Turkish -mIş as mirative (Aksu-Koç 1988) |
| semantics-pragmatics.md:71 | Matses dream reports take experienced-past evidentials (Fleck 2007; Aikhenvald 2004: 345) |
| semantics-pragmatics.md:73-79 | 5-row inventory → model → cultural-effect table (none / 2 / 3 / 4-5 / optional-rich Turkish) |
| semantics-pragmatics.md:81-82 | futures cannot be witnessed; calibration: habit, not vigilance (Slobin 1996); "evidentials encode source, not truth" |
| semantics-pragmatics.md:92,124,125,133 | speech-act row "testimony bound by evidentials (§4)"; design-procedure steps; delta worked example "3-term evidentials" |
| corpus/knowledge/linguistics/syntax-typology.md:3,4,7 | topic and sources list Willett 1988, Aikhenvald 2004, Aikhenvald & Dixon 2003, Faller 2002, DeLancey 1997, Fleck 2007 |
| **syntax-typology.md:69-82** | second treatment: Willett split (70); Aikhenvald "2–5 terms", Tariana five, Turkish -DI/-mIş, Quechua (71); 5-row sizing table (74-80); cultural consequences (81); mirativity (82) |
| syntax-typology.md:65,108 | RC strategy for "testimony-driven (evidential)" cultures; checklist item 5 "Evidential system sized to the culture's information economy" |
| corpus/knowledge/linguistics/semantic-fields-lexicon-building.md:7,80,81,98,106,117 | Aikhenvald 2004, Tuyuca/Barnes 1984; scripture/hearsay defaults; "grammaticalized categories (evidentials…) are stronger evidence than any word count" |
| corpus/knowledge/linguistics/conlang-methodology.md:21,31,72,80,96,121,153 | pipeline stage 6; "evidentials: who may attest what"; TAM/evidential inflection; scaffold sentence "evidentially marked statement"; table row "evidentiality \| grammar of how you know \| Aikhenvald 2004"; typological passport; checklist |
| corpus/knowledge/linguistics/morphological-typology.md:80 | polysynthetic: "evidentials and switch-reference are frequent riders on the verb" |
| corpus/knowledge/linguistics/register-strata-attestation.md:66 | assertives row "testimony bound by evidentials" |
| corpus/knowledge/linguistics/translation-protocol-fidelity.md:21,78 | reuses semantics-pragmatics :82 "grammaticalized lying" as an analogue for criterion C3 |
| corpus/knowledge/linguistics/gesture-co-speech-pointing.md:58,61 | palm-up *epistemic* gesture variant (S199); gesture, not grammar |
| corpus/knowledge/linguistics/semantics-pragmatics.md:41 | subjectification "content → epistemic" (Traugott 1989); the one epistemic-modality line, as a semantic-change path |
| corpus/knowledge/civilizations/inca.md:36,37,155 | Quechuan evidential distinctions [A04 ch.3]; "Do not make evidentiality a biological truth detector"; pragmatics ≠ cause of evidentiality |
| corpus/knowledge/civilizations/haudenosaunee.md:23 | D24: "evidential" is a function, not a word class |
| corpus/knowledge/synthesis/consistency-verification-checklist.md:14,49,100 | "a grammatical evidential does not certify truth"; T10 routes to semantics-pragmatics §4 evidential-inventory table; C12 "information source is not metaphysical truth" |

All other hits of `evidential*` in corpus/knowledge (about 40 lines: aegean :107, anatolia :63, austronesia :52, burma :183, china-qing :1,:145-150 kaozheng "evidential research", finnic-sami :210, india-* , maya :101,:125,:139, nazca, newar, olmec, rome, scythian, tibet, material-culture-inference-method :85, coupling-model :40,:185, era-myth matrix :53, glossary-registry-format :3,:155, migration, source-discipline :62, symbolism-consistency :67, taboo-euphemism :117, typed-label-routing :10, calibration-registry :103, lexicon-coverage-audit :193, verification-independence :40, verification-method-overview :6,:63,:196) use **"evidential" in the archaeological or scholarly-evidence sense**, not the grammatical one. Count only the rows in the table above as topic overlap.
myth-symbol partition: no grammatical-evidential hits. Quotative or hearsay mentions only (monsters-hybrid-beings.md:78 *φασι* hearsay marker; narrative-structure-frameworks.md:91).
No line anywhere mentions WALS 77A/78A, de Haan, egophoricity/conjunct-disjunct, or evidential acquisition.

### Registry coverage (corpus/SOURCES.md)
- **Zero rows** cover evidentiality, mirativity or epistemic modality. `grep -i` for `evidential|mirativ|aikhenvald|willett|delancey|de haan|palmer.*mood|plungian` over SOURCES.md finds no row. The only `epistemic` hit is S199 (SOURCES.md:228, Cooperrider et al. 2018, the palm-up *epistemic gesture*), which is a different topic.
- **No `wals.info/chapter/*` or `wals.info/feature/*` URL is a registry row.** WALS enters only as S002 (SOURCES.md:31, the CLDF dataset repo, release-level "cite the release used"). numerals-and-measures.md:19-21 cites wals.info/chapter/131 and /55 inline, without S-ids.
- Every Aikhenvald/Willett/DeLancey/Palmer/Barnes/Faller/Fleck citation in the entries above is bibliography-only, with no S-id. The `verified-at` lines of semantics-pragmatics.md:5 and syntax-typology.md:5 say "apparatus audit only … no dated source recheck for this entry on record".
- Couple to S002 (WALS dataset) by id if the entry quotes 77A/78A counts. **New-id candidates, live and 200 at probe time:** `https://wals.info/chapter/77` (de Haan, "Semantic Distinctions of Evidentiality"; 77A values No grammatical evidentials 181 / Only indirect 166 / Both direct and indirect 71, Total 418) and `https://wals.info/chapter/78` (de Haan, "Coding of Evidentiality"; 78A values: verbal affix or clitic 131 / part of the tense system 24 / separate particle 65 / modal morpheme 7 / mixed 10, plus 181 none). Feature pages /feature/77A and /78A are also 200. All four pages are server-rendered text, so quotes are extractable.

### New ground or repackaging? (judgement)
- **Overlap risk is real.** The corpus already has two parallel sub-sections: semantics-pragmatics.md:66-82, 17 lines with a 5-row table, and syntax-typology.md:69-82, 14 lines with a 5-row table. They carry the core typology: Willett's split, the 2/3/5-term sizes, Tuyuca/Tariana/Quechua/Turkish/Matses, mirativity, the "evidential ≠ epistemic modality" one-liner (:68), "source not truth" (:82). An entry that restates these is a repackaging. C's predicate cannot see this: it counts bytes, headings, a table and new ids, not novelty.
- **What is genuinely absent** (new ground the entry can own):
  1. The evidentiality/epistemic-modality separation, argued with sources. Today it is one clause citing Palmer 1986 (:68), without a row.
  2. WALS 77A/78A areal counts and the *coding* dimension (affix/clitic vs tense-fused vs particle vs modal morpheme). Nothing covers this today.
  3. Registry-backed, dated source verification. No existing evidential line has an S-id or a recheck.
  4. Evidential × person (egophoric/conjunct-disjunct), evidential × tense or aspect, and evidentials in questions and commands. Absent.
  5. An existing inconsistency an entry should resolve, not copy. semantics-pragmatics.md:79 classes Turkish as "optional but rich … not forced". syntax-typology.md:77 classes Turkish -DI/-mIş as a 2-term system "marked even in formal writing". WALS 78A's "part of the tense system" value bears directly on that split.
- Recommendation for C: make the entry the *registry-backed* layer. Point one-way to semantics-pragmatics §4 and syntax-typology §4 for the design tables they already own. Put the new table on coding × semantics × design consequence (WALS 78A/77A), not on a sixth "system size → culture" table. Treat the Turkish inconsistency as a finding with its source. Do not edit the two neighbours (production files; not in C's paths).

## (b) Freshness history — is F a repeat?

- **Earlier freshness rounds rechecked knowledge claims, not registry rows.** The registry (SOURCES.md) was born in round 49.
  - r1/r2: to-verify flag triage (LOG.md:390, :1436).
  - supplement-opencode-1: claim-level source rechecks (LOG.md:2062-2080).
  - r5: 20 original-question follow-ups (LOG.md:2309-2315, :2421).
  - r6: 24 question rows (LOG.md:2477, :2588).
  - r7: 5 rule-drift source checks, which "recheck current source-derived constraints" (LOG.md:2719-2723).
  - r8/r9: residual rechecks (LOG.md:2926-2930, :2958-2962).
  - r10/r11: 192-row hash-drift ledger. r11 FAILED at 0.778 < 0.95 (LOG.md:2996, :3021-3029; SCORECARD.md:550-562).
- **Registry `recheck` cells have never been advanced by a re-verification.** The only in-place recheck change on record is policy, not re-verification: corpus/lessons/round-49.md:89 sets S028, S029, S030 and S043 `recheck` `—` → `365d`. round-55.md:147 records S256 365d→365d (unchanged). `tools/check-sources-recheck.py` landed in r82 (LOG.md:4525-4531; corpus/lessons/round-82.md:29-35; round-82-verifier-spotcheck.md:67-70), and no round has consumed its queue since. **In form, F is new:** it is the first use of the r82 queue and the first re-verification-driven advance of recheck cells.
- **In substance, it is a short-interval repeat.** All 16 rows were opened 2026-10-19 (S009-S033), 2026-10-22 (S084-S163) or 2026-10-25 (S875), so F re-verifies surfaces 10-16 days old. Their place in the queue comes from the `90d` cadence, not from observed staleness. Most were already re-opened by non-author seats in their own round:
  - S009-S033: round-50 build seats `ScoutCensus` and `ReviewSourcesContract`; S012/S020/S021 also round-51 `falsify/ReviewSourcesRegistry`.
  - S084, S104-S107: round-51 falsify `ReviewSourcesRegistry`, `ReopenS101`, `ReopenS107`, `ReviewLessonGate`.
  - S157/S163: round-52 closure, via Wayback after a captcha (corpus/lessons/round-52-verifier-spotcheck.md:51,104).
  - S875: round-72 closure, live, 231736 B (round-72-verifier-spotcheck.md:51).
  - S142: no non-author re-open file found by filename grep.
  The information gain is a 2-week liveness check. It is not drift detection.
- **Round-11 L0 pause, the main risk to F's admissibility.** The fleet queue line `/home/vgpnk/Projects/shokunin/.ufo/l0-questions.md:47` (kotodama | round-11) ends: "Freshness axis-move claims are paused until ruled." That line has **no `L0 ANSWER`** (other lines in the file carry one, e.g. kama round-11). Rounds 25-86 restate the pause: SCORECARD.md:1017,1033,1048,1062,1075,1088,1101; LOG.md:3028,3128,3510,4014,4361,4373,4424,4431,4499,4617,4665,4722,4818. `claims.json` `lowest_axis` says F "does not depend on the open round-11 L0 drift-threshold question". That reading is defensible, because the question is about the *hash-stability threshold*. It is not what the question's own last sentence says, and no ruling or L0 answer narrows it. F is the first freshness axis-move claim since r11. The closure should be told, not left to find it.

## (c) The 16 F rows — original Gate quote, live probe, and r89-bound fit

"r89 ok" means `measure89.quote_ok` (≤25 words, ≥20 normalised chars) together with `first_quote` extraction. "live" means `measure89.contains` on the raw bytes fetched 2026-11-04 19:10 -03.

| id | original Gate (path:line) | original quote | r89 ok | live probe (status, bytes) | original quote in live raw? | notes for the F author |
|---|---|---|---|---|---|---|
| S009 | lessons/round-49.md:37 | "97.9% of all features are from WALS" | yes | 200, 5164 | **no**: raw is `97<span>.9%`, so markup splits the number | `"of all features are from WALS"` (29 chars) matches the raw bytes |
| S012 | round-49.md:40 | "a multi-hop pipeline that decomposes language design into modular stages -- phonology, …translation." | yes (18 w) | 200, 41410 | yes | — |
| S020 | round-49.md:49 | "identified 2,670 motif expressions of 200 different motifs across 58,450 sentences for training and testing" | yes | 200, 42002 | yes | — |
| S021 | round-49.md:50 | "common mitigation strategies, including negative prompting and temperature scaling, fail to meaningfully address this homogeneity" | yes | 200, 40108 | yes | — |
| S031 | round-49.md:63 | "Of the 63 different foraging societies, 50 (79%) of the groups had documentation on women hunting." | yes | 200, 214483 | yes | — |
| S032 | round-49.md:64 (URL **api.crossref.org**, a host not in the row cell) | title field "Female foragers sometimes hunt, yet gendered divisions of labor are real: a comment on …" (24 w) | yes | doi.org → linkinghub.elsevier.com, 200, 2774 B redirect stub carrying the title | yes (title on stub) | A Crossref capture **fails `url_ok`** (the row URL is doi.org only). Record the manifest url as the doi.org URL. The tier-A scope is title-level only; the body is unread and ScienceDirect was 403 in r49 |
| S033 | round-49.md:65 | "concerns were raised about the reliability and replicability of the results." | yes | 200, 90003 | yes | — |
| S084 | round-51.md:41 | "Sign Languages are written languages!" | yes | 200, 425114 | yes | — |
| S104 | round-51.md:61 | "Pseudo Family: LSFic" | **no (19 chars < 20)** | 200, 112819 | **no**: `<span class="level-family">` splits it | needs a different, longer quote from a single text node |
| S105 | round-51.md:62 | `"name": "LSFic", "id": "lsfi1234"` | words/chars yes; **`first_quote` breaks** on the inner straight quotes | 200, 1580 | yes | wrap in curly “…”. **S105 is superseded by S126** (SOURCES.md:155 "supersedes S105"). Advancing a superseded row's recheck is low-value; NOT-LOCATED is not required, but say it in the lesson |
| S106 | round-51.md:63 | "The BANZSL subgroup is argued by Adam Schembri and Kearsy Cormier and … Bencie Woll (2010)" | yes (24 w) | 200, 84742 | **no**: each author is an `<a title=…>` link | `"The BANZSL subgroup is argued by"` (32 chars) matches raw |
| S107 | round-51.md:64 | `'British Sign Language [brit1235][bfi]-l-':1,'New Zealand Sign Language [newz1236][nzs]-l-':1` | yes | 200, 1094 | yes | — |
| S142 | round-52.md:68 | "their primary function was that of a memory aid for a repertoire transmitted orally from teacher to pupil" | yes | Wayback PDF 200, 321469 | yes, **after `pdftotext`**; raw PDF bytes will not match | the row's only URL is already a Wayback capture; the committed capture must be extracted text (sha256 over that text) |
| S157 | round-52.md:91,92 | "two distinct whistles replace the five Spanish vowels, and there are four whistles for consonants" | yes | live 200, 50214, **F5/TSPD bot-challenge page** | no (challenge) | Wayback `web/2026/` → 20260830052642, 200, 178541: **quote present**. S157 also has access-note superseder S186 (rejected, SOURCES.md:215) |
| S163 | round-52.md:98 | "…the steep mountains and rugged topography of the region, which required the local population to find an alternative way to communicate across long distances" | yes (24 w) | live 200, 43470, **TSPD challenge** | no | Wayback latest 20261022024508 is **itself an archived TSPD challenge**; 20260922232938 also TSPD. **20260312095851 `id_` contains the quote, but only when fetched with `--compressed`.** Without it the body is gzip bytes and `contains` fails |
| S875 | round-72.md:19 | "安土・桃山" | **no (5 chars)** | 200, 231736 | yes | needs a ≥20-char CJK run. `"記録作成等の措置を講ずべき無形の民俗文化財"` (21 chars, a 指定区分 option in the row's anchor) matches raw. Era names sit in a JS array with `"` delimiters, so avoid them |

Probe hashes: stage copy `probes-sha256.txt` (26 files). Bodies are not kept.

## Counter facts the F author must respect (measure89.py, frozen; no change proposed)
1. **Window edge.** ADVANCED needs `2026-11-04+90d < d`, which is strictly after **2027-02-02**, with d ≤ 2027-11-05 (measure89.py:156-157,167). Re-arming the row's own 90-day cadence (2027-02-02) **does not advance**. Use a date ≥ 2027-02-03, e.g. a 180d or 365d date.
2. The lesson line must contain the literal `recheck 90d→<ISO>` or `recheck 90d-><ISO>` and `2026-11-04` (:172). The old value for all 16 is `90d`.
3. `contains()` runs on the **committed capture bytes**, NFKC/casefold, with every non-word run collapsed to one space (:75-82). Raw HTML tag names and attributes therefore become tokens. A quote spanning inline markup fails on a raw capture. Gzip or PDF bytes never match. Choose quotes inside one text node, or commit an extracted-text capture. The latter widens the fabricated-capture surface that claims.json `bounds` already concedes.
4. `first_quote()` takes the **first** `"…"` or `“…”` on the LOCATED line (:105-107). Put the quote first, and wrap quotes that contain `"` in curly quotes.
5. `url_ok` accepts an exact row URL, or any `https://web.archive.org/web/…` string that **ends with** a row URL (:98-102). `api.crossref.org` (S032's r49 URL) fails. S142's row URL is itself a Wayback URL, so the exact string or a Wayback-of-Wayback is required.
6. `datetime.date.fromisoformat` (:166) accepts compact/week forms on Python ≥3.11 (e.g. `20270301`). This is a lenient-parse surface. It is not a defect that blocks honest use.
7. `rows()` splits cells on every `|` (:85-92). A pipe inside a population row's cell would shift index 9. All 16 rows parse to 11 cells today.

## Unresolved
- Whether the round-11 pause covers F is an L0/operator question, not a scout's to settle.
- S142: no non-author re-open record found (filename grep only, not exhaustive).
- Probes were single plain requests. Hosts can change behaviour per request (TSPD on UNESCO, PLOS).
