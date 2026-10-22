# ScribeSec06Grammar — Claim C, section 6 "Grammar in space" (draft + sources)

- Seat: KotodamaR51a3.ScribeSec06Grammar (leaf; no delegation, no background jobs).
- Lane: /home/vgpnk/Projects/shokunin/kotodama-shokunin, branch main, base `bff83ba65bf9559af4d7567e81703059667a0005` (claim base). No lane file was edited, created or deleted except this report.
- Assigned item: draft `## 6. Grammar in space` for the C entry `corpus/knowledge/linguistics/sign-languages-manual-modality.md`, budget 15 lines total (counting the H2 line and blank lines), with pipe tables and every factual claim citing a NEW-id, an in-corpus `path:line`, or `(to-verify)`. Open: Sandler, Meir, Padden & Aronoff 2005 PNAS (ABSL); one primary source on classifier/depicting constructions (Cormier et al. 2012, opened); one source on nonmanual markers (Pfau & Quer, opened).

## 1. Drafted text (ready to paste; 15 lines exactly)

```markdown
## 6. Grammar in space

Signed sentences run several grammatical channels at once: loci and verbs carry argument structure while face and body carry clause type — a surface with no spoken analogue.

| Channel | Attested pattern | Design rule |
|---|---|---|
| Referential loci and pointing | INDEX localizes a referent in signing space; pronouns may be placed anywhere in it (NEW-KotodamaR51a3.ScribeSec06Grammar-3) | fix one locus per participant; point back to it |
| Indicating / agreement verbs | verb movement and orientation can be modulated to agree with subject and object (NEW-KotodamaR51a3.ScribeSec06Grammar-3) | let verb trajectory point at loci: morphology becomes geometry |
| Depicting constructions | handshape "identifies the class of the referent"; entity vs handling types (NEW-KotodamaR51a3.ScribeSec06Grammar-2) | design productive handshape classes, not frozen lexicon |

| Channel | Attested pattern | Design rule |
|---|---|---|
| Simultaneity | nonmanuals layer over manual signs; headshake is "the most common marker" of negation (NEW-KotodamaR51a3.ScribeSec06Grammar-3) | write each channel separately; let them co-occur |
| Question, negation, topic markers | brows mark yes/no questions; topics sit at clause-left with their own marking (NEW-KotodamaR51a3.ScribeSec06Grammar-3) | scope of the marker tracks the constituent, not the sentence |
| Emerging word order | ABSL shows regular S-O-V within one generation; subject precedes object in all 32 two-noun clauses (NEW-KotodamaR51a3.ScribeSec06Grammar-1) | ordered arguments are the simplest disambiguator; do not assert a universal default (`syntax-typology.md:99`) |
```

Line count verified: 15 lines (H2 = line 1; blank lines at 2, 4, 10; two pipe tables of 3 rows each). All six required topics are covered: referential loci and pointing, indicating/agreement verbs, classifier/depicting constructions, simultaneity, nonmanual grammatical markers (questions, negation, topics), and word-order evidence from an emerging sign language. Every factual row cites a NEW-id or an in-corpus `path:line`; no `(to-verify)` needed because every cited fact is opened. No "deaf-mute"/"dumb"/"hearing-impaired" labels; sign languages are never framed as deficient or pantomime. Method-only content (the intro line and the Design-rule cells) is lane framing, not factual claims.

NB: the entry names `syntax-typology.md:99` (the in-corpus warning that SOV-as-human-default claims from emerging sign languages are contested). The draft does not name the C entry itself, `corpus/lessons/round-51.md`, or `boundary-count.py`.

## 2. Registry rows (draft; L1 renumbers to S071+)

Exact column order: `| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |`

| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
| NEW-KotodamaR51a3.ScribeSec06Grammar-1 | Sandler, Meir, Padden & Aronoff 2005, The emergence of grammar: Systematic structure in a new language, PNAS 102(7):2661–2665, doi 10.1073/pnas.0405448102 — https://pmc.ncbi.nlm.nih.gov/articles/PMC548320/ | paper | A | the ABSL word-order findings as reported in this paper (second generation; not the third-generation studies, not other sign languages) | Abstract; Results (Fig. 3 discussion) | systematic grammar emerges within one generation; S-O-V in all 32 two-noun clauses; head-modifier order; independent of ambient Arabic/Hebrew/ISL | mined | 2026-10-22 | 365d | corpus/knowledge/linguistics/sign-languages-manual-modality.md |
| NEW-KotodamaR51a3.ScribeSec06Grammar-2 | Cormier, Quinto-Pozos, Sevcikova & Schembri 2012, Lexicalisation and de-lexicalisation processes in sign languages: Comparing depicting constructions and viewpoint gestures, Language & Communication 32(4):329–348, doi 10.1016/j.langcom.2012.09.004 — https://pmc.ncbi.nlm.nih.gov/articles/PMC3688355/ | paper | A | depicting (classifier) constructions in signed languages vs non-signer gesture — entity vs handling handshape types and their lexicalization; CC BY 3.0 | Abstract; §1 Introduction; §2 Depicting constructions in signed languages | "classifier" terminology is contested; depicting handshape "identifies the class of the referent"; entity vs handling two-way distinction; iconicity/gestural status debated | mined | 2026-10-22 | 365d | corpus/knowledge/linguistics/sign-languages-manual-modality.md |
| NEW-KotodamaR51a3.ScribeSec06Grammar-3 | Pfau & Quer, Nonmanuals: their grammatical and prosodic roles — https://cnlse.es/antiguos/Nonmanuals.their%20grammatical%20and%20prosodic%20roles.pdf | book | B | grammatical and prosodic functions of nonmanual markers across sign languages (negation, interrogatives, topics, agreement, pronominalization); survey chapter, not a primary empirical study | Intro §1; §2.3.1 Negation; §2.3.2 Interrogatives; §2.3.3 Topics; §2.3.6 Agreement; §2.3.7 Pronominalization | nonmanuals are linguistic, not affective; headshake negation; eyebrow-marked questions; topic marking at clause-left; loci and pointing; agreement verbs | mined | 2026-10-22 | 365d | corpus/knowledge/linguistics/sign-languages-manual-modality.md |

## 3. Gate lines (for the round lesson's `## Gate`)

- NEW-KotodamaR51a3.ScribeSec06Grammar-1 — https://pmc.ncbi.nlm.nih.gov/articles/PMC548320/ — accessed 2026-10-22 — Abstract: "In the space of one generation from its inception, systematic grammatical structure has emerged in the language." Also Results (Fig. 3): "Where two nouns are mentioned in a clause, subject precedes object (in all 32 cases)."
- NEW-KotodamaR51a3.ScribeSec06Grammar-2 — https://pmc.ncbi.nlm.nih.gov/articles/PMC3688355/ — accessed 2026-10-22 — §2: "The core component of the DC has usually been described as the handshape which identifies the class of the referent."
- NEW-KotodamaR51a3.ScribeSec06Grammar-3 — https://cnlse.es/antiguos/Nonmanuals.their%20grammatical%20and%20prosodic%20roles.pdf — accessed 2026-10-22 — §2.3.2: "In fact, in most sign languages, the nonmanual is the only indication that we are dealing with a question, since the word order does not change." Also §2.3.1: "the most common marker is a side-to-side headshake (hs)"; §2.3.3: "Sentence topics are characteristically realized as constituents at the left edge of the clause and are co-articulated with specific nonmanual markers."

All quotes ≤25 words and verbatim from the pages opened this session (2026-10-22). No quote was invented; no page/date fabricated.

## 4. Evidence

- Sandler et al. 2005 opened at PubMed Central (PMC548320), full text; DOI 10.1073/pnas.0405448102; PNAS 102(7):2661–2665; publication date 2005-02-07. The S-O-V result and the one-generation emergence quote are taken from the Abstract and Results sections as shown above. Tier A for the ABSL word-order scope.
- Cormier et al. 2012 opened at PubMed Central (PMC3688355), full text under CC BY 3.0; Language & Communication 32(4):329–348, doi 10.1016/j.langcom.2012.09.004. Primary comparative study of depicting constructions; provides the entity/handling dichotomy used in the draft. Tier A.
- Pfau & Quer, "Nonmanuals: their grammatical and prosodic roles", opened as PDF at cnlse.es (the PDF itself gives no print citation; it is a survey chapter by the two leading authors of nonmanual research). Tier B (strong secondary survey). Scope column notes this.
- In-corpus anchor re-read at the lane worktree: `corpus/knowledge/linguistics/syntax-typology.md:99` ("Claims that SOV is 'the human default' draw on emerging sign languages and homesign … suggestive, interpretively contested — don't assert it flat"), cited in the draft's word-order design rule.

## 5. Result

- Section draft delivered: 15 lines, pipe tables, all six required topics covered, every factual row cited (NEW-ids 1–3 and `syntax-typology.md:99`).
- Three sources opened and registered as drafts (rows + Gate lines above), all with access date 2026-10-22.
- No mined mistake found in the opened sources (the S060/S070 page-range correction already exists in SOURCES and is unrelated). "One mined mistake" for the frontier step: none reported by this seat.
- No installs or updates (read RULES.md first; used only the read/web_search tools). No pacman transactions.
- No lane file changed except this report; no git/jj commands run; no /fast/scratch/hyaku/kotodama-r51-* or reports/round-51/calibration/ material read.

## 6. Unrun checks

- The entry's full acceptance (provenance audit, sweep, S-id resolution, README index) is the L1/integrator's job, not this seat's; not run here.
- The three NEW-ids above are drafts; the L1 renumbers them to S071+ at integration. The draft cites the NEW-ids as they appear here; the L1 must renumber inside the pasted section when assigning rows.
- The Pfau & Quer PDF's print provenance was not identified on the file; tier B and recheck 365d are set accordingly. If a print citation is required, it should be confirmed by the L1 before the row is finalized.
