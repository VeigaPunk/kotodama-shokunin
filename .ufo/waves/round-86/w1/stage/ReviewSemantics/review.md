# Round 86 semantics review

Axes: **depth + operability**. Lane-review recommendations only; no admission, wave judgment, validator exception, or freshness waiver.

## Findings by severity

No outstanding actionable semantic defect found in the revised ScribeGenre `entry.md` (103 lines, read snapshot 2A00 for revised anchors; initial complete draft snapshot 3C9C).

Resolved: the initial S924 definition quotation changed internal quotation marks. The revised line 37 uses the exact six-word span “none has met with universal acceptance” and scopes it to the 1911 article rather than modern consensus.

## Named recommendations

- **ADMIT-D-SCOPED-DEEPENING (recommendation):** Draft lines 12–16 explicitly preserve prior genre coverage. Existing `corpus/knowledge/linguistics/orality-formulaic-language.md:82–97` already treats proverbs and riddles; the addition instead separates witnesses, origins, editorial selection, interventions, and proposed answers. Six decision rows at lines 24–29 and operating procedures at lines 58–70 supply a usable narrower layer.
- **ADMIT-S924-ATTRIBUTED (recommendation):** Independently reopened public Wikisource Proverb on 2026-11-04; article body agrees with retained `reports/round-86/evidence/S924.html:516–524`. Located quote: “none has met with universal acceptance” (6 words). Its four draft anchors are short and correctly attributed to the dated article. Popularity is the article's criterion, not measured uptake of a particular proverb. URL: https://en.wikisource.org/wiki/1911_Encyclop%C3%A6dia_Britannica/Proverb .
- **ADMIT-S925-PREFACE-METHOD (recommendation):** Independently read retained capture lines 35–81, 129–142, and 149–181. Approximate dating follows the compiler's distinction between speech and literary appearance (49–55); non-exhaustive classical parallels are limited to that project (45–47); exclusion of indecent material is explicit (77–81); literary preference is explicit (129–136). Draft anchors 39–43 preserve these scopes, including OCR `hterary`, rather than laundering them into oral-frequency observations. The six design decisions are labeled inferences, not quotations or universal history.
- **ADMIT-S926-EDITORIAL-LIMITS (recommendation):** Independently read retained capture lines 80–139. Draft 44–48 correctly distinguishes the editor's claimed method from verified results; manuscript departures are specifically those originating with the editor (123–124), and the Index records proposed answers (137–139), not consensus. Draft 68 refuses to reconstruct italics from flattened OCR; draft 70 explicitly asserts no numbered-riddle solution. The authority discussion at capture 95–99 begins with authorship, so the draft wisely anchors solution reasoning in 100–104 instead.
- **ADMIT-NONCANON-EXAMPLE (recommendation):** Lines 74–82 label every example element invented, keep witness/report/editorial clocks separate, preserve two situated senses, and record both candidate fits and failures. Lines 99–103 reserve world ownership and acceptance decisions to their owners.
- **REJECT-NOVEL-GENRE / REJECT-CONSENSUS / REJECT-SOLUTION-PROOF:** These broader claims would be unsupported; the current draft does not make them. Neither the dated prefaces nor a shape-counter pass establishes a modern consensus, ancient intention, complete repertoire, or correct individual solution.
- **REJECT-O-ACCEPTANCE-FROM-D:** This entry cannot establish paragraph extraction behavior. Frozen `measure86.py:86–110` requires tool, subprocess, Iron red/green, held-out, and registry legs; none is replaced by this semantic recommendation. O is containing-article paragraph ordinal, not first quote span.

## Frozen contract and functional limits

Read authoritative claims with read-only `git -C <lane> show 16c267832746e1cb98fb42a56180f8d1d12dc18b:reports/round-86/claims.json`; inspected counter logic at lines 37–153 without executing it. D legs at 68–85 check shape, table size, single-ID bullets, registry, and pinned lint; claims explicitly reserve semantic support for review. This dossier supplies the intended method depth, not attestation records or solutions for actual individual sayings beyond its preface anchors. No requirement for such a historical worked solution is added here. No runtime/rerouting/resume change is in this reviewed artifact; those contracts are not evaluated by this seat.

## Residual risk and verification gaps

- No mounted `lsp` device: `read xd://lsp` returned “No such tool.” Used literal grep and capture reads as fallback, not semantic caller proof. Markdown dossier introduces no code callers.
- S925 and S926 were read from L1 captures, not independently live-reopened. No source refusal or access flip occurred in this seat. S924 live body was opened successfully; no scan was inspected.
- Apperson's 1929 date is not established by the capture's opening title text. Raised this with ScribeGenre; its assignment explicitly supplied “Apperson 1929 preface.” Draft line 101 discloses assignment-supplied date and lack of title-page verification. Retain that limitation; this review independently confirms the body, not the year.
- Source registry integration, final production diff, pinned lint, byte/section counts, and O runtime checks remain L1 verification, not observed results here. No tests/builds/linters/formatters/counter selftest were run. No install, commit, index mutation, production edit, delegation, background job, or scratch directory was created.
- Freshness remains paused. L1 canonical-planner validator prohibition remains explicit and unadjudicated.

Self-evaluation: accuracy 4/5 (edition year not independently verified); completeness 4/5 (staged D semantics only, not integrated production/O runtime); clarity 4/5 (evidence and recommendations separated); actionability 4/5 (specific retain/accept boundaries); conciseness 4/5 (source-by-source evidence retained). Mean 4.0/5. Main should check final integrated rows and run only its authorized bounded verification; do not treat this report as external admission.
