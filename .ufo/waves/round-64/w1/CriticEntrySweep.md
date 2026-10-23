# CriticEntrySweep — claim C entry falsification

## Scope and review verdict

Axes: **coverage, operability, calibration**. This is a leaf critique of the supplied entry skeleton plus staged bullet values, using the assigned section map. It is not a native-judge, claim-admission, or round verdict. No entry, registry, counter, index, git index, or jj state was changed.

**Review verdict: counterexamples found; the supplied inputs are not ready unchanged.** A definite citation-shape defect, two source-qualification defects, and stale/incomplete staging require correction. The developmental-sequence and lore-boundary sweeps found no violation in the visible framing. Seven mapped bullet values are absent, so this is not certification of a complete assembled entry.

Reviewed snapshots: `.ufo/waves/round-64/rows/ScribeEntrySkeleton/entry.md` read snapshot `F69B`; `.ufo/waves/round-64/stage/bullets.json` snapshot `84C5`. Line numbers below refer to these inputs, not a subsequently assembled file.

## Findings and smallest safe corrections

### CE1 — source metadata itself violates the citation shape

- **Location:** skeleton line 4, before §1.
- **Counterexample:** `- source: S718–S743 in ...` contains two distinct registered IDs. An en-dash range is not one citation.
- **Local evidence:** `tools/check-cited-lines.py:44,53–61` has no metadata exemption; its explicit `range-endash` case at lines 148–151 expects `MULTI-ID` for this shape. `reports/round-64/accept-c.py:253–266` likewise checks every entry line.
- **Integration consequence [INFERENCE from code]:** `.ufo/waves/round-64/integrate-w2.py:169–172` replaces a different, older sentence beginning `Round-64 row citations`; it does not match the current source line. Its generated-entry guard at lines 203–207 would reject the retained range. This consequence was not executed here.
- **Impacted axes:** operability; calibration if the skeleton is called citation-clean.
- **Smallest safe correction:** replace the metadata range with a generic reference to the round's registry rows; retain concrete IDs only on their supported bullets. Do not merely split the range across metadata lines: `RESTATE` also requires cited entry lines to have the bullet shape. No checker exemption or frozen-leg change is warranted.

### CE2 — attempted classroom scaffolding becomes successful scaffolding

- **Location:** §7, staged JSON line 15, S735; the same wording is in `rows/ScribeRowS735/row.txt:2`.
- **Claim at issue:** teacher questions and comments “shape” discourse toward structure and focus, followed by the literacy-rehearsal inference.
- **Strongest counterexample:** the cited article expressly allows the opposite result when teacher and child do not share narrative conventions. Its abstract says collaboration is “often unsuccessful” in that case, and sharing time can “either provide or deny access to key literacy-related experiences.”
- **Evidence:** the row's selected abstract quote says the teacher **tries to help**, not that every intervention succeeds. The original 1981 abstract was independently retrieved through [DOI/CrossRef](https://doi.org/10.1017/S0047404500008861), including both the successful and unsuccessful cases. The Ohio-hosted scan reader exposed only the cover; Cambridge requests returned 429 and JSTOR a client challenge. These retrieval failures are not negative evidence about the article.
- **Verdict:** confirmed loss of a material qualification. The conditional phrase “can rehearse literacy” is not itself false; the problem is the unqualified successful-shaping premise and omission of the countercondition central to the source.
- **Impacted axes:** coverage and calibration. A conditional classroom reference is useful coverage; replacing the source's differential outcomes with uniformly successful scaffolding is not a harmless trade.
- **Smallest safe correction:** narrow to the observed teacher's attempt, for example: `- In the observed classroom, the teacher tried through questions and comments to help children structure and focus their discourse. (S735)` If retaining a literacy-outcome clause, explicitly condition it on shared discourse conventions. Do not change the frozen counter.

### CE3 — infant prosody preference loses its age/stimulus exceptions

- **Location:** §2, staged JSON line 3, S719; the current row bullet has the same unqualified preference premise.
- **Claim at issue:** “Infants attend preferentially to IDS-like prosody” supplies an apparently general attention cue.
- **Strongest counterexample:** the very review cited reports that “newborns can actually prefer their mother’s ADS over her IDS.” It also describes opposite or absent preferences in simplified pitch experiments and age-dependent contributions from repetition rather than prosody.
- **Evidence:** [Cristia 2013, §3, printed pp. 161–162](https://pure.mpg.de/rest/items/item_1094677/component/file_1703379/content), independently fetched and read as a PDF. The selected §4 quote itself ends with “with the aforementioned caveats.” The cached extraction has these passages at `S719.pdf:71–80` in this review's permitted scratch directory.
- **Verdict:** confirmed caveat deletion, not a rejection of the documented general tendency. A generic sentence can be read as a tendency, but the source supplies a direct counterexample to an exceptionless design rule; the qualification belongs in the exported claim rather than only its source.
- **Impacted axes:** calibration and coverage.
- **Smallest safe correction:** retain the tendency and its limits, for example: `- Infants often attend preferentially to IDS-like prosody, with age- and stimulus-dependent exceptions to that attention cue. (S719)` Do not infer a universal age schedule from the reported exceptions.

### CE4 — inherited stage values no longer match their selected row anchors

- **Locations:** §5 S738 at JSON line 18; §8 S739 at line 19; §5 S742 at line 20.
- **Counterexample:** the JSON still exports older bullets, while the current contribution files have different anchor-scoped bullets. This is a second, stale content authority if the JSON is reused as current input.
- **S738:** the staged well-being/accommodation sentence is supported by the full chapter, but not restated from the current selected quote about instructions to delay introducing Polish. The source is one studied family, not general adoption guidance. The current row's bullet instead states the Polish-introduction instruction.
- **S739:** the current selected quote is about parents varying address **to children** with situational context. The staged bullet instead exports children modeling address to relatives. The latter is discussed later in the full article, so it is not a fabricated source claim, but it is not the selected-anchor restatement. The current row bullet correctly stays with parent-to-child address variation.
- **S742:** the selected quote describes morning greetings becoming routine and expected. The staged singular `greeting ritual`/`explicit instruction`/`community-building` wording contains no three in-order content-word matches to that quote. The current row bullet instead uses morning greetings, students, and shared classroom practice.
- **Mechanical consequence [INFERENCE from the frozen algorithm]:** `accept-c.py:270–297` requires three in-order content words from the selected quote. The staged S738 wording supplies only `children` in order, S739 only `address` then `children`, and S742 none. These are static derivations, not a claimed `RESTATE` execution.
- **Independent source countertest:** [Kozminska & Zhu, PDF p. 8, paragraph before Excerpt 4.2](https://eprints.bbk.ac.uk/id/eprint/47679/3/47679.pdf) explicitly supports well-being/accommodation; [Kurniawati et al., PDF pp. 14–15](https://journal.uny.ac.id/index.php/litera/article/download/39455/pdf) explicitly discusses address as community-model input; [Shields-Lysiak et al., p. 48](https://files.eric.ed.gov/fulltext/EJ1271032.pdf) explicitly discusses greeting instruction and connection. The initially plausible accusation that these ideas were absent from the full sources was therefore **not sustained**.
- **Impacted axes:** operability and calibration; coverage if stale values erase the case-specific restrictions.
- **Smallest safe correction:** derive assembled values from the current reviewed contribution files rather than this inherited JSON, or regenerate the JSON from that same authority before reuse. Keep the single-family/local-classroom bounds. This is an input/provenance repair, not grounds to relax `RESTATE` or invent different anchors.

### CE5 — supplied staged entry is incomplete for its assigned map

- **Location:** marker insertions for §§3–6 and §8.
- **Observed key sweep:** JSON lines 2–20 hold S718, S719, S720, S722, S724, S725, S726, S728, S729, S730, S731, S732, S734, S735, S736, S737, S738, S739, S742.
- **Missing assigned values:** §3 S721 and S723; §4 S743; §5 S727; §6 S733; §8 S740 and S741. These follow directly by comparing the observed keys with the assignment's map. §9 intentionally has no source bullet and is not an omission.
- **Inherited defects named:** S723 and S740 contribution files were still absent at this review's file-discovery snapshot. S721, S727, S733, S741, and S743 contribution files did exist, showing that the inherited JSON is older than the available row set. `stage/report.txt` also retains earlier missing/problem records; it was read as historical data, not rerun or accepted as a current receipt. No inherited “30/32 clean” result is asserted here.
- **Impacted axes:** coverage and calibration; operability if a complete map is required for assembly.
- **Smallest safe correction:** complete and review the two missing contributions, then assemble the full mapped set from the current authority. Do not fabricate omitted clauses or certify them from row existence alone.

### CE6 — prospective signed-language framing conflates modality with multilingualism

- **Location:** skeleton §6 heading at line 33 and opening at line 35; assigned map and `integrate-w2.py:39` place S733 there. Its JSON value is currently absent, so this is a prospective assembly-framing defect, not a statement already inserted.
- **Counterexample:** S733 concerns productive ASL vocabulary in native-signing deaf children. Neither its row nor the reopened [primary abstract/method](https://pmc.ncbi.nlm.nih.gov/articles/PMC5507709/) establishes that the finding is about acquiring more than one language. Signed modality alone does not establish a bilingual or heritage context. Equally, this review does not assert that the participants were monolingual.
- **Impacted axes:** calibration and coverage.
- **Smallest safe correction:** broaden the heading/opening to distinguish bilingual/heritage contexts from signed-language modality, or place the signed-vocabulary claim in a modality-neutral acquisition section. Preserve the ASL-specific sample bound rather than generalizing it to all sign languages.

## Requested negative sweeps and section disposition

- **Universal developmental sequence:** no violation found in the visible skeleton. Lines 3 and 10 explicitly reject a universal sequence/schedule; line 20 says not to derive the early topics from one another; line 30 rejects a single ladder; line 35 rejects a uniform pathway. Early-vocalization/first-word headings are topic groupings, not an asserted ordering. CE3 concerns an overgeneral preference, not a newly alleged universal stage sequence.
- **Citation shape:** skeleton line 4 is the only multiple-ID line found by the recorded skeleton sweep. A separate leading-pipe/S-ID sweep returned no matches. Every visible staged **bullet value** carries one terminal ID; the JSON key repeating its value's ID is serialization, not an additional citation in the rendered bullet.
- **Lore boundary:** no violation found in the visible text. §9 lines 50–59 presents conditional worldbuilder choices, not named world-facts. Line 63 explicitly disclaims canon decisions and gives the world bible and consistency verification to lore. That matches `PROVINCE.md:9–25` and `worldbible-integration-contract.md:17–19,96–106`. No invented canon entity, approved import, bilateral acceptance, or lore receipt is asserted.
- **§1:** S726's social-membership link supports the stated community-design use; no additional overclaim identified against its selected quote.
- **§2:** S718 is sample-bounded; S729 says this caregiving setting; S724 matches the textbook's telegraphic first-multiword description. S719 requires CE3's qualification. The production/register distinction should remain explicit rather than treating early child syntax as a caregiver register.
- **§3:** S720's `may` is consistent with the source's selective, subtle ambient-language finding; S722's listed processes match its review quote. Missing values remain CE5, not reviewed claims.
- **§4:** S725 says `may imitate`, not durable grammatical learning; S737 identifies the source's verbal-play dimensions. No additional quote-level overclaim identified in those visible values; S743 is absent from the JSON.
- **§5:** S728's explicit-prompt description matches Frye's secondary report about Kaluli mothers; it must not be mistaken for Frye's contrasting Qaqet observations. S738/S742 require the authority/anchor repair in CE4; S727 is absent.
- **§6:** S730 is an available dual-language design path, not a required path. S731 retains `in this sample`, and the reopened study supports avoiding DLD diagnosis from switch frequency; S732 retains `sometimes`. CE6 concerns S733's placement, not an inference that signing is deficient or inherently bilingual.
- **§7:** S734 uses `may` and S736 `can`; no additional quote-level overclaim identified. S735 requires CE2.
- **§8:** S739's full-source support was checked rather than falsely rejected; CE4 still applies to its selected anchor. S740/S741 are absent from the JSON, so honorific/taboo coverage is not certified.
- **§9/§10:** conditional design table and handoff are within scope. No S-ID appears in the table.

## Commands, tool calls, and observed evidence

Only source retrieval and static inspection were performed. No acceptance script, cited-line CLI, row checker, build, formatter, native judge, or other agent runtime was invoked.

Actual static sweep:

```text
functions.grep(
  pattern="\\bS\\d{3,}\\b.*\\bS\\d{3,}\\b|^\\s*\\|.*\\bS\\d{3,}\\b",
  path="kotodama-shokunin/.ufo/waves/round-64/rows/ScribeEntrySkeleton/entry.md")
Observed match: line 4, the source metadata containing S718–S743.

functions.grep(pattern="^\\s*\\|.*\\bS\\d{3,}\\b", same skeleton path)
Observed output: No matches found

functions.grep(pattern='^ "S\\d{3}":',
  path="kotodama-shokunin/.ufo/waves/round-64/stage/bullets.json")
Observed keys, transcribed as line→key:
2→S718; 3→S719; 4→S720; 5→S722; 6→S724; 7→S725;
8→S726; 9→S728; 10→S729; 11→S730; 12→S731; 13→S732;
14→S734; 15→S735; 16→S736; 17→S737; 18→S738; 19→S739; 20→S742.
```

The no-extension S719 URL initially returned `Content-Type: application/pdf` but reader extraction failed as unsupported `.bin`. This tooling inconsistency was reported to `xd://report_issue`. The permitted scratch workaround command was:

```sh
mkdir -p /home/vgpnk/.cache/hyaku/kotodama-r64-w1/CriticEntrySweep && curl --fail --location --max-time 60 --silent --show-error --output /home/vgpnk/.cache/hyaku/kotodama-r64-w1/CriticEntrySweep/S719.pdf https://pure.mpg.de/rest/items/item_1094677/component/file_1703379/content
```

Observed Bash output: `(no output)`. A subsequent `functions.read` of that `.pdf` extracted the article with page markers; §3's newborn counterexample and §4's qualification were read directly, not accepted from search-generated summaries.

Actual `functions.read("https://doi.org/10.1017/S0047404500008861")` result: `Method: crossref`, original 1981 article metadata and abstract; the abstract included both `tries to help` and the successful/unsuccessful collaboration conditions described in CE2.

For the integration owner only, after all corrections land, the unmodified checks to run are:

```sh
python3 -B tools/check-cited-lines.py corpus/knowledge/linguistics/language-socialization-and-acquisition.md
python3 -B reports/round-64/accept-c.py
```

These commands were **not run here** and have no claimed result. The current assembled entry was not reviewed by this ticket. All source-support conclusions above are bounded to the named staged inputs and reopened source passages.

Tool installs/updates: none. Scratch contains only the retrieved S719 PDF. The only lane write by this reviewer is this requested report.

Report: .ufo/waves/round-64/w1/CriticEntrySweep.md
