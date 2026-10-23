# CriticClaimsAxes59 — frozen declaration framing review

Axes: **C / coverage** = previously unowned protective-object/mark design surface, not a file or source-row count; **D / depth** = source-faithful detail in existing cultural knowledge, not verification receipts. Calibration/provenance and freshness are affected where the counters overstate what they establish.

Reviewed declaration `1b80ee41f544d17c0410733a47a3eecac01bf25e`, claim base `39c9ce8a6be5e5625d8befb54df53d621a3a7929`. Fixtures and executions were confined to `/fast/scratch/hyaku/kotodama-r59/CriticClaimsAxes59/clone`; no counter, claim declaration, manifest, or frozen fix specification was edited. The existing lane dry-run receipt was read separately because it was not present in the declaration clone. No judge/admission/runtime orchestration was invoked. No tools installed or updated.

## Controls actually scored

CONTROL sid4 | claim C | exit 1 | ACCEPT-C-59: FAIL | failing legs: [SWEEP, FLOOR, LOCATE, BOILER, RELEVANCE, TOPIC, DISTINCT, SUPPORT]

Fixture: add only the declared entry path, containing `- source: S1000` and `This intentionally out-of-block source is cited as (S1000).` No new source row, index row, or reviewer evidence. This attacks RANGE's universal, not the other legs.

Command, from the clone root:

```sh
timeout 900 python3 -B reports/round-59/accept-c.py
```

Pasted output:

```text
SET PASS count=235 required=235 added=['corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md'] removed=[]
SWEEP FAIL exit=1 rows 234 files 235 missing_from_index 1 ['myth-symbol/amulets-talismans-apotropaic-marks.md']
FLOOR FAIL cited=0 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
TIER PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LOCATE FAIL passing=0 cited=0 at=2026-10-23T02:47Z failing=[]
BOILER FAIL passing=0 cited=0 at=2026-10-23T02:47Z failing=[]
RELEVANCE FAIL passing=0 cited=0 at=2026-10-23T02:47Z failing=[]
TOPIC FAIL passing=0 cited=0 at=2026-10-23T02:47Z failing=[]
FRESH PASS rows_reusing_registry_urls=[]
DISTINCT FAIL shared=[] hosts=0 need=10
SUPPORT FAIL unsupported=[] qualified_seats=[] need_seats=2 planted=[] no registry: FileNotFoundError no planted key: FileNotFoundError
ACCEPT-C-59: FAIL
```

CONTROL undeclared-reader | claim C | exit 1 | ACCEPT-C-59: FAIL | failing legs: [SWEEP, FLOOR, LOCATE, BOILER, TOPIC, DISTINCT]

Fixture: the entry cites S600 and S1000. Append one S600 row with no URL, quote `Amulets protect the people and guard their houses from evil.`, teaches `Protective amulets are meaningful objects that people use for domestic safety.`, tier B, status mined, and used-by the declared entry. The entry's substantive line is `Protective amulets guard people and their houses from evil (S600). This out-of-block citation is also present (S1000).` Register two **invented** reviewer identities, `OutsideManifestOne59` / `invented-agent-one` and `OutsideManifestTwo59` / `invented-agent-two`, both role reviewer. Neither seat's report or packet is among C's declared lands. Each key maps P01 to S600 and P02 to PLANTED; each report contains only `VERDICT P01 SUPPORTED` and `VERDICT P02 NOT-SUPPORTED`. Each packet prints the S600 quote under `### P01`, and an invented quote under `### P02`. No reader was dispatched and no source was opened. PLANTED_ROWS contains only `Intentionally fabricated planted control row. No source was read.` and terminal whitespace; neither planted file nor hash was committed.

Exact key JSON: `{"seats":{"OutsideManifestOne59":{"P01":"S600","P02":"PLANTED"},"OutsideManifestTwo59":{"P01":"S600","P02":"PLANTED"}}}`. Observed SHA-256 values placed in the two expected hash files:

```text
6fd77fc5890db806d4bbce976da98c9f37baef9c66ce7a32b525b6ecaef6a56d  .ufo/waves/round-59/support/planted-key.json
8b28002b600f46a6cd4e6d9f1486540c26d5bd6271d0427d7eea5692c42dca21  .ufo/waves/round-59/support/planted-rows.md
```

Command, from the same clone root:

```sh
timeout 900 python3 -B reports/round-59/accept-c.py
```

Pasted output:

```text
SET PASS count=235 required=235 added=['corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md'] removed=[]
SWEEP FAIL exit=1 rows 234 files 235 missing_from_index 1 ['myth-symbol/amulets-talismans-apotropaic-marks.md']
FLOOR FAIL cited=1 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
TIER PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LOCATE FAIL passing=0 cited=1 at=2026-10-23T02:49Z failing=['S600: no-url']
BOILER FAIL passing=0 cited=1 at=2026-10-23T02:49Z failing=['S600: not-located']
RELEVANCE PASS passing=1 cited=1 at=2026-10-23T02:49Z failing=[]
TOPIC FAIL passing=0 cited=1 at=2026-10-23T02:49Z failing=['S600: quote_hits=1 not-located']
FRESH PASS rows_reusing_registry_urls=[]
DISTINCT FAIL shared=[] hosts=0 need=10
SUPPORT PASS unsupported=[] qualified_seats=['OutsideManifestOne59', 'OutsideManifestTwo59'] need_seats=2 planted=['OutsideManifestOne59:Q1', 'OutsideManifestTwo59:Q1']
ACCEPT-C-59: FAIL
```

Neither control is MEETS-COUNTER or MEETS-MECHANICAL. In sid4, SUPPORT failed for missing registry/key as well as absent citations. In undeclared-reader, SUPPORT **passed**; source-location and other independent legs correctly prevented whole-counter acceptance. These are demonstrated per-leg weaknesses, not a claim that either complete frozen predicate was met.

## Findings: verdict, counterexample, affected axes, smallest safe correction

All lane-relative references below refer to the frozen declaration unless explicitly called the live receipt. Contract references are `/home/vgpnk/Projects/shokunin/.ufo/prompts/kotodama-round-59.md`.

1. **fine — the axis names identify changed surfaces.** C's `claims.json:31-35` names frontier → core and an entry path; D's `:92-96` names sentence-level source fidelity in two existing entries. That satisfies the naming part of contract §6 item 9 (`:361-365`), rather than calling 235 files or 27 tokens an axis. The counters are bounded before→after predicates (`accept-c.py:131-145`, `accept-d.py:76-95`); a do-nothing tree cannot satisfy SET/KONGO/SPEECH. Smallest correction: none to the names themselves; do not equate a green count with substantive novelty or semantic truth.

2. **risk — C has a real dedicated-owner gap, not an empty subject area.** The filename sweep is true: searching frozen `reports/round-59/base-knowledge-files.txt` for `amulet|talism|apotrop` returned no match. However, a case-insensitive corpus/knowledge sweep for `\b(amulets?|talismans?|talismanic|apotropa\w*|evil[\s-]+eye)\b` returned 21 existing files, including one topic-line partial owner (`myth-symbol/mineral-stone-symbolism.md:5`). Strongest counterexample to treating all protective objects/marks as uncovered: `myth-symbol/binding-speech-complex.md:164` already owns counter-curse defense with **amulets, apotropaic writing and threshold deposits**. More partial owners: `civilizations/egypt-ancient.md:96-97` (wedjat, scarab/amulet), `israel-ancient-hebrew.md:108-113` (protective silver inscriptions and dating), `germanic-norse.md:65` (inscribed amulets), `china-tang.md:126` (talismanic writing), `japan-medieval-sengoku.md:89` (specialists/talismans), `culture-material/adornment-body-codes.md:20` and `ritual-garments.md:118` (bulla), `craft-artisan-lexicon.md:121` (building protection/hostile writing), `warrior-material-culture.md:91,110` (worn protective script), `myth-symbol/color-symbolism.md:79`, `celestial-symbolism-calendars.md:128`, `mineral-stone-symbolism.md:65-77,175` (lapidary virtue/application and the false universal). The remaining matches are `burma.md:72`, `carthage.md:143`, `rapa-nui.md:161`, `vessel-container-lexicon.md:90`, `death-afterlife-eschatology.md:91`, `divination-omen-systems.md:102`, `synthesis/era-myth-language-costume-matrix.md:91,183`, and `migration-founder-effects.md:147`. Alias sweep also finds `civilizations/amazigh-berber.md:100` (afus/khamsa protective pendant), `greece-classical.md:118` (gorgoneion), and `myth-symbol/monsters-hybrid-beings.md:97,179` (Pazuzu protection). An exact `\bevil[\s-]+eye\b` sweep returned no match; this is bounded negative evidence, not proof all eye-protection knowledge is absent. Impact: coverage, depth/duplication. Smallest correction: before data, state the missing **integrated object/mark typology and genuinely new sub-surfaces**, list these partial owners and point to them one-way. New URLs alone do not establish new ground. `claims.json:41` correctly makes substance review-only; that review remains necessary.

3. **fine — D is not merely records work, though its speech remap alone would be.** `d-fixes.json:41-47` changes a generic mestres uniform claim into two figures in a dated watercolor; `:60-66` separates Batsîkama's narration from the Randels block quotation; `:125-132` restores the scholarly contrast rather than merely relabelling a receipt. These change admitted knowledge's scope and source interpretation: depth under fleet `AXES.md:11`. Closure `corpus/lessons/round-58-verifier-spotcheck.md:134-137,153` expressly identifies leaving this knowledge false/stale as quality harm. Conversely, the 27 substitutions in `d-fixes.json:145-159` are citation maintenance; don't sell that token count as independent deepening. Smallest correction: keep the Kongo content repairs as D's justification and the remap as supporting maintenance, not a second axis claim.

4. **risk — the literal lowest-axis obligation has no demonstrated waiver here.** Contract `:14-17` requires the lowest non-retired axis unless the stagnation nudge waives it. `claims.json:14` and `SCORECARD.md:11-16` call freshness historically lowest; `SCORECARD.md:932-935` says no retirement and no nudge without calibrated scores. Fleet `.ufo/l0-questions.md:47` records the unanswered threshold question and the pause. That explains avoiding a fresh threshold claim; it is not, by itself, evidence of an operator-granted exception to §2. Impact: calibration/claim conformance, not proof C or D harms freshness. Smallest correction: explicitly distinguish the existing pause from retirement/saturation and record the applicable waiver/eligibility rationale; do not invent saturation or a numeric ranking.

5. **defect — C's universal citation clauses omit a valid identifier class.** `claims.json:34,78` says all cited ids are in S600-S659. `accept-c.py:151-152` enumerates only `S\d{3}`, while the registry parser at `:154`, locator ROW, and fleet `CORPUS.md:89` admit three **or more** digits. Both controls leave S1000 present and get `RANGE PASS`; sid4 even prints `cited=0`. Thus subsequent row universals also exclude it. Impact: coverage evidence and calibration. Smallest safe correction before data: use the canonical 3+-digit identifier grammar for citation/range extraction, then reject every extracted id outside the reserved block; test S1000 and a range reaching it on an otherwise green fixture.

6. **defect — C's SUPPORT read set is larger than its declared lands.** `claims.json:21` says every SUPPORT input path is named; `:53-68` and `separability-manifest.json:17-32` enumerate only SupportA59 through SupportH59 reports/packets. But `accept-c.py:228-229,248-257` trusts **any** registry member name with a nonempty agentId and reviewer role, then opens name-derived paths. undeclared-reader actually reads and counts four undeclared report/packet paths, printing both outside names as qualified. Impact: causal separability and evidence provenance. Smallest safe correction: require the registry's permitted seat names to equal the declared support_seats, constrain names to the fixed filenames, and reject extra members before any dynamic open. Merely listing A–H in JSON does not constrain the implementation.

7. **defect — hash equality and token verdicts are not the temporal/reader provenance promised.** `claims.json:34` requires rows/key hashes committed before data/support dispatch; `accept-c.py:55-60` describes that order and real returned agentIds; `:63-65` says a no-reader report fails. Actual `:235-243` checks only filesystem hash equality, `:229` only a nonempty string, and `:258-273` only keyed verdict/quote tokens. undeclared-reader gets `SUPPORT PASS` using invented identities, uncommitted keys/hashes and no reader. This is not a whole-counter bypass, but it disproves those SUPPORT assurances. Impact: calibration/provenance and the trust supporting coverage. Smallest correction: bind registry identities to the actual dispatch receipt and the hashes to pinned committed order evidence, then exercise key/label-aware no-reader controls. If order/diligence is reviewed outside the command, name it review-only rather than claiming the counter establishes it.

8. **risk — SUPPORT is not bound to the complete proposition reviewed.** `accept-c.py:246,255-265` binds a verdict to the normalized anchor quote only, not the teaches cell, all citing entry sentences, the source URL, or an entry revision. `rowcheck.py:228-238` joins all citing lines for two-stem overlap. [INFERENCE] Changing a teaching or adding a contradictory clause while preserving that quote/stem overlap can retain earlier SUPPORT verdicts. The declaration honestly puts per-sentence support and substantive novelty in review_only (`claims.json:36-41`), so don't silently broaden ACCEPT into those universals. Impact: depth/quality and provenance. Smallest correction: bind review packets/verdicts to the full row and exact citing content at a pinned revision, or keep the advertised outcome explicitly limited and obtain the separate substantive review.

9. **fine at the aggregate; defect at one detailed promise — predicate identity is not just matching labels.** C's declared command/label at `claims.json:34,73,75` matches `accept-c.py:278-280`; D's `claims.json:95,106,108` matches `accept-d.py:107-109`: exit 0 iff all listed legs pass, with the same ACCEPT-C-59 / ACCEPT-D-59 labels. Live receipt `reports/round-59/telemetry/declaration-dry-run.txt:3,19-20,41,45-46` uses those exact commands, labels and exit codes. The long predicate sentences and short counter docstrings are not literally identical text; their aggregate condition agrees. Detailed assurances need their own code correspondence: in addition to findings 5–8, D says **byte-for-byte, nothing else changed** (`claims.json:95`, `accept-d.py:13-20`), but tips are read with universal-newline text mode at `accept-d.py:68-69` while base bytes are decoded without that translation at `:53`. Rewriting fully fixed LF files as CRLF is therefore invisible to equality. This seat did not execute that D control. Peer `KotodamaR59.CtlDShortcuts59` subsequently reported KONGO PASS and SPEECH PASS on the CRLF mutant, but full ACCEPT-D-59 FAIL solely on a transient CARRY fix-93 fetch failure; that is peer-reported leg evidence, **not** a whole-counter PASS. Impact: calibration/exactness, not necessarily substantive cultural harm. Smallest correction: compare encoded expected bytes with binary tip reads.

10. **risk — C/D are structurally disjoint, but final causal separability is not yet demonstrated and registry bookkeeping crosses their semantic boundary.** The manifest gives D only its two existing knowledge files (`:44-56`), C its entry/index/registry/support evidence (`:6-41`), and no D exports; S570-S574 genuinely exist at base (`corpus/SOURCES.md:548-552`). D's `needs_git: true` correctly covers `git show`. `claims-agree.py` passed below. But the existing declaration receipt `:55-58` reports exit 2 at C's absent entry: no dynamic separability leg ran. Checker `tools/check-claim-separability.py:647-669` only tests acceptance under overlays; it is not a complete file-read tracer. Moreover `claims.json:24` expressly assigns D's old/new source-row status/used-by transitions to C's SOURCES land, while D's counter does not read SOURCES. [INFERENCE] C-only overlay carrying those transitions would name the speech entry as using S570-S574 while the base speech entry still cites the old ids; D-only overlay retains queued/unused new rows. Fleet `CORPUS.md:103-108` defines mined/used-by from actual citing paths. Impact: separability and truthful provenance. Smallest correction: keep D-specific bookkeeping out of C-only evidence and explicitly resolve row ownership/shared records before data; don't infer end-to-end registry consistency from the counters' chosen read sets. Run the unchanged manifest on the fully materialized final claims; an absent-land receipt is not a separability PASS.

11. **risk — live fetches remain an external input, and the one-fetch guarantee has a race.** Contract `:344-347` asks for a concrete value re-derivable over committed bytes; the declaration deliberately also depends on live source/root responses (`claims.json:9,34,95`). This is disclosed, and round-58 closure `:151` specifically asked for a declared fetch rule, so FETCH-59 is not an after-result relaxation. Nevertheless a committed tree can change verdict with network state. More specifically, `rowcheck.py:88-97` drops _CACHE_LOCK before _RAW_FETCH and only setdefaults afterward; [INFERENCE from that code] concurrent identical URLs can be fetched twice, contrary to its `:10-21` universal. `accept-d.py:100-101` runs repeated source URLs from d-fixes concurrently. Impact: freshness/reproducibility and predicate identity. Smallest correction: make fetching single-flight per URL before the final freeze, retain bodies/errors for the run, and keep committed receipt evidence distinct from later live replays. The fetch-rule seat has separately reported reproducing this race; that report is independent evidence, not a control executed here.

12. **fine — the present dry-run receipt matches declared commands, with the right pre-landing failures.** The live receipt names declaration revision 1b80ee41 (`:2`), runs C twice for counting/acceptance (`:3,22`), D twice (`:41,48`), separability (`:55`) and agreement (`:59`). It reports exactly the declared before-state failures and expressly marks later separability legs unevaluated (`:58`). Commands and roles therefore match; there is no substituted easier input in this receipt. Limitation: `dry-run.py:94-107` checks command-string sets plus existence of a revision line, not labels/results/role multiplicities. We checked the actual receipt as well as running that guard. Smallest correction: none to this receipt's commands; don't treat the two-way command guard as verification of substantive predicates or source provenance.

13. **risk — freeze_note names a different hash artifact.** `claims.json:27` points to `reports/round-59/planted.sha256`, while the predicate, code and lands use **planted-rows.sha256** and **planted-key.sha256** (`claims.json:34,51-52`, `accept-c.py:102-103`). It is still explicitly pending, not false proof of a completed freeze. Impact: calibration/provenance. Smallest correction before final freeze: point at both actual artifacts and the carrying commit; don't leave a non-resolving third name in the freeze claim.

## C acceptance path inventory

This distinguishes mutable lands from legitimate frozen base inputs; reading a base file is not automatically a C→D dependency.

| Read/open site | Actual input | Declaration relationship |
|---|---|---|
| accept-c.py:124 | reports/round-59/base-knowledge-files.txt | Frozen instrument, named in claims.json:7, exists at base. |
| accept-c.py:131-132 | Directory walk of corpus/knowledge, including the two D paths | Base path set plus C entry; SET reads path membership, not all contents. |
| accept-c.py:136 → reports/round-28/readme/sweep.py:45-47,74-82,125-140 | Sweep code; corpus/README.md; topic metadata of every indexed knowledge entry | README is C land; other entries are pre-existing base inputs. D's fixes do not change their topic fields. |
| accept-c.py:150,182 | Declared new entry | C land. |
| accept-c.py:153 | Entire corpus/SOURCES.md | C land, including old rows used by FRESH. |
| accept-c.py:172 → tools/check-source-access.py:65-87 | Access-check code; SOURCES; all Markdown knowledge entry contents when flagged ids exist | Frozen base code plus C SOURCES/entry and existing base knowledge. This transitive global read includes D paths; it must not be omitted from a read-set description. |
| accept-c.py:178 → rowcheck.py:77-80 | rowcheck.py and reopen-quote.py | Frozen instruments named in claims.json:7, present at base. |
| accept-c.py:228 | support/registry.json | C land. |
| accept-c.py:236-242 | planted-key.json, planted-rows.md, planted-key.sha256, planted-rows.sha256 | All four are C lands. |
| accept-c.py:249-257 | support/<registry name>.md and support/packet-<registry name>.md | A–H files declared, arbitrary registry-derived names are not. Demonstrated defect above. |
| rowcheck.py:334,344,347 | --entry argument; SOURCES in --row mode; --draft argument | CLI-only opens, **not invoked** by accept-c's imported check_row path. Do not invent a --draft dependency for C. |
| rowcheck.py:170-215,277-283 → reopen-quote.py:78-93,106-118 | Source and root HTTP bodies; temporary PDF and pinned pypdf subprocess when needed | External/runtime inputs explicitly described by FETCH-59/locator, not new corpus lands. They make a live replay different from a pure committed-byte computation. |

No additional hard-coded mutable corpus/support input appeared in accept-c.py or rowcheck.py beyond this inventory. The dynamic reviewer-name family prevents claiming that the finite A–H list is exhaustive.

## Other commands actually exercised

Both ran in the sandbox clone, under timeout 900; both exited 0.

```sh
timeout 900 python3 -B reports/round-59/dry-run.py check /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-59/telemetry/declaration-dry-run.txt
```

```text
MISSING_FROM_RECEIPT []
UNDECLARED_IN_RECEIPT []
MEASURED_REVISION ['1b80ee41f544d17c0410733a47a3eecac01bf25e']
```

```sh
timeout 900 python3 -B reports/round-59/claims-agree.py
```

```text
AGREE claims=['C', 'D']
```

No D counter or full dynamic separability check was executed by this seat; their declaration-receipt outputs were evidence-read, not re-measured. All processes started by this seat have exited; no background job or server was started.

counter weaknesses: demonstrated C RANGE ignores valid 4+-digit citations; demonstrated SUPPORT reads undeclared reviewer paths and qualifies invented/uncommitted no-reader evidence. Fix before final freeze by enumerating canonical ids, pinning reviewer names/provenance and making temporal promises actually checked or explicitly review-only. Static additional weaknesses: quote-only review binding, text-mode D byte comparison, non-single-flight FETCH-59, and the unproven semantic separation of D's registry bookkeeping. C's substantive gap remains a review obligation: partial owners exist, and merely counting another file or fresh URLs cannot establish coverage. These are counter/framing findings, not an admission judgment or a report of any complete control meeting either frozen counter.
