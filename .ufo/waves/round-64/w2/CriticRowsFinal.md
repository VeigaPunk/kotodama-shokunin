# CriticRowsFinal — scoped staged-row attack

## Axes and scope

- **Coverage:** distinct works rather than different hosts for one paper.
- **Operability:** normalized URL identity, counter-normalized quote bounds, public hosts, and row-format constraints.
- **Calibration:** tier authority must match the evidence actually opened and anchored.

Critic only: no judgment/admission, integration, row/counter/registry edit, commit, index/jj mutation, subagent dispatch, or alternate agent runtime. This report is the only lane write. No tools installed or updated; pacman untouched.

All 32 row files were read in the initial parallel batch. **Not yet repaired at that initial read, therefore excluded from final-row findings:** **S719, S728, S729, S735, S739, S742, S747**. Their older caveat/duplicate/attempt-versus-success/tier/setting/fabricated-anchor issues were visible; those are dependencies on the assigned repair seats, not newly scored findings here. S722 already named `New Directions and Next Steps`, so it is included. The remaining **25 rows** are the scoped final-row review.

A second complete raw-read snapshot was retained in memory before analysis (capture metadata `2026-10-24T02:51:31.356102+00:00`). These parallel reads are **not an atomic post-repair snapshot**: S747 had changed by the second batch, and S735 was briefly an intermediate bare bullet. The S735 owner was notified and replied that the required `BULLET: - ` prefix had been restored before their checker run. No repaired exclusions were silently promoted into this review. A complete final 32-row assurance is unavailable at this review's start; do not describe this report as one.

## Findings — smallest corrections only

### RF1 — S721: tier A describes a secondary definition as primary authority

**Counterexample:** S721 is A for `infant vocal turn-taking and protoconversation in early development`; its quote defines proto-conversation, rather than reporting the review's own quantitative result. In the full article, the selected sentence ends with citations to **Hsu & Fogel (2003), Hsu et al. (2001), and Kaye (1977)**. It is presented in the literature-background section immediately before reports from Bateson and other earlier studies.

**Evidence:** `.ufo/waves/round-64/rows/ScribeRowS721/row.txt:1`; [Nguyen et al., “The developmental trajectory of turn-taking and its moderators,” first paragraph](https://pmc.ncbi.nlm.nih.gov/articles/PMC9271548/). Independently opened in this review. Wave-1 `ReviewerRegistry.md:99–103` called A acceptable because this was the paper's own statement; the full sentence's explicit upstream citations are the stronger counterevidence to that rationale. A meta-analysis can be primary for its own synthesis results; that does not make every background definition primary.

**Impacted axes:** calibration; coverage provenance. **Smallest safe correction:** retain this source/quote/bullet and mark B with scope explicitly describing the review's secondary definition, or re-anchor A to the review's own result and adjust the dependent clause. The former is smaller and preserves useful coverage. No counter change.

### RF2 — S726: ERIC abstract-only evidence is tier A for a substantive paradigm claim

**Counterexample:** the anchor explicitly says `ERIC record abstract, numbered claim (1)`, while the A scope is Ochs and Schieffelin's foundational paradigm and the benefit concerns speech development/social membership. This is not merely bibliographic metadata. The opened ERIC page is a summary ending `(MSE)` and separately links the full paper; the selected row does not anchor that paper.

**Evidence:** `.ufo/waves/round-64/rows/ScribeRowS726/row.txt:1`; [ERIC ED252065](https://eric.ed.gov/?id=ED252065), independently reopened. `corpus/QUALITY.md:29` explicitly makes abstracts B for substantive claims about a work. Existing registry **S102**, `corpus/SOURCES.md:131`, is B for a paper's substantive claim known through its ERIC abstract; S044–S046 provide the established abstract/description correction pattern.

**Impacted axes:** calibration; coverage provenance. **Smallest safe correction:** B for the abstract-reported claim, keeping the current quote and benefit; alternatively open and quote the original paper for A. This does not require changing a counter or dropping the source.

### RF3 — S737: the same ERIC abstract-only tier inflation

**Counterexample:** A is assigned to Schwartz's study's operational definition, but the anchor is `ERIC abstract, verbal-play definition`. The evidence actually opened is the ERIC summary (ending `(BD)`), not the original full-text study. The row's ACCESS records a **404** for its linked full-text attempt.

**Evidence:** `.ufo/waves/round-64/rows/ScribeRowS737/row.txt:1,5`; [ERIC ED149852](https://eric.ed.gov/?id=ED149852), independently reopened; the same explicit QUALITY criterion 6 and S102 precedent as RF2. Wave-1 `ReviewSupportC.md:24` confirmed quote/bullet support, but support does not independently establish primary-source tier.

**Impacted axes:** calibration. **Smallest safe correction:** B, explicitly scoped to the ERIC-reported operational definition; retain the honest full-text access limit. No new work/URL is needed.

### RF4 — S723: teaches cell exceeds the stated row bound

**Counterexample/evidence:** `.ufo/waves/round-64/rows/ScribeRowS723/row.txt:1`, cell 7, is **44 words** both by the counter normalizer and whitespace count, against the assignment's **≤25-word teaches** rule. It combines overextension, underextension, a developmental trajectory and a design gloss. Its **anchor quote is valid at 13 words**; these are different cells.

**Impacted axes:** operability; calibration of the clean-row assertion. **Smallest safe correction:** shorten cell 7 to one ≤25-word learner benefit grounded in the selected overextension quote. For example: `Worldbuilders can depict overextension as a child using one simple word for many different things.` Preserve the source, locator, and citation identity. The checker does not currently measure teaches length (`check-rows.py:97–154`), so its historical clean output does not cover this constraint.

### RF5 — S740: teaches cell also exceeds the stated row bound

**Counterexample/evidence:** `.ufo/waves/round-64/rows/ScribeRowS740/row.txt:1`, cell 7, is **45 counter-normalized words / 43 whitespace words**, both above 25. It combines noun-title overgeneralization, a parental-age result and a worldbuilding inference. The selected quote is valid at **22 words**.

**Impacted axes:** operability; calibration. **Smallest safe correction:** reduce cell 7 to the single benefit grounded in the selected overgeneralization quote, retaining its inferential hedge. For example: `Worldbuilders can model Japanese noun-title overgeneralizations as suggesting rule learning rather than input memorization.` No evidence supports weakening the bound.

**Important non-finding:** S740's A tier was tested against the full same-page capture. The selected paragraph explicitly says `Another example of these overgeneralizations from our corpora`; unlike S721, these are the paper's own observations. Its full-text location is not an abstract-only authority. Do not downgrade it merely because it is a paper about acquisition.

## Executed scans and limits

### URL and work identity

The **complete 770-line current registry, 643 registry rows**, was read in ranged parallel pages, filling every truncation gap before comparison. Registry evidence snapshot SHA-256: `7a77cabcf633bc4868ac72807d88192092d21ed2db477f26aeee151d03009434`.

URL key: NFKC/casefold, remove leading `http://` or `https://`, remove leading `www.`, remove trailing `/` (plus source punctuation). **Query strings were retained**, avoiding the false equation of ERIC's `?id=ED252065` and `?id=ED149852`. Each staged live URL was compared with all other staged live URLs and URLs in every registry row, not only the first URL in a cell.

- Normalized staged live-URL collision groups: **0**.
- Normalized staged-versus-registry live-URL collisions: **0**.
- Title/source metadata and literal DOI scan: no further same-work candidate in the scoped 25 rows. Full normalized title matches against the registry: **0**. Token-overlap candidates S723/S119 and S730/S228 were inspected and are unrelated titles/authors, not duplicates.
- The initial **S718/S729 same-title, same-paper pair still existed**, despite different normalized URLs. It is the already-forced S729 repair dependency, excluded above—not a new recurrence or evidence that normalized URLs alone prove distinct works.

### Quote bounds using the counter's normalizer

Used the actual `norm_words` and `anchor_quote` function definitions extracted via AST from `reports/round-64/accept-c.py:89–100`; no acceptance command was run. NFKC → casefold → Unicode nonword/underscore splitting, using the counter's first ASCII/curly double-quoted anchor match. All **25 in-scope rows are within 8–25**, range **9–25**.

| Row | Quote words | Row | Quote words | Row | Quote words |
|---|---:|---|---:|---|---:|
| S718 | 9 | S720 | 24 | S721 | 18 |
| S722 | 17 | S723 | 13 | S724 | 16 |
| S725 | 19 | S726 | 19 | S727 | 16 |
| S730 | 24 | S731 | 23 | S732 | 19 |
| S733 | 15 | S734 | 16 | S736 | 10 |
| S737 | 25 | S738 | 20 | S740 | 22 |
| S741 | 12 | S743 | 10 | S744 | 14 |
| S745 | 11 | S746 | 17 | S748 | 11 |
| S749 | 21 | | | | |

The second snapshot's S747 has **0 quoted words**, because its repair replaced fabricated quotation with an honest unreachable-record anchor. S747 was excluded at start; this is not an in-scope quote-bound defect, nor a recommendation to restore fabricated text. Disposition handling belongs to its repair owner and the canonical assignment.

### Private hosts

Scanned every URL-bearing line of all 32 captured row files for userinfo, missing/single-label hosts, localhost/private suffixes, reserved placeholder suffixes and non-global IP literals: **0 hits**. Concurrent DNS resolution of the **25 distinct cited hosts** (including archive hosts) produced **0 errors and 0 non-global addresses**. This is a point-in-time hostname/address scan, not a claim about every future redirect or DNS answer. No live locator was invoked.

## Evidence custody and closure

Scratch only: `/home/vgpnk/.cache/hyaku/kotodama-r64-w2/CriticRowsFinal/`:

- `row-snapshot.json`: complete row text, fields, paths and SHA-256 hashes for all 32 raw reads; preserves the explicitly excluded in-flight transitions.
- `registry-snapshot.txt`: all 770 registry lines used for comparison.
- `analysis.json`: exclusions, scope, normalized collision results, per-row quote/teaches counts and all DNS results.

Finding-row snapshot SHA-256:

| Row | SHA-256 |
|---|---|
| S721 | c1492af6f6ec47af06d5a33d85e115e6184d55a689f5a6231cf48c4c4d858d28 |
| S726 | da1dda3b407e6597b4d84bcb13e93a1e1eed2f981431e80c2d7116d5105b9522 |
| S737 | f8df43e2e3701066d056400cdbbbb15a8604a9134399b302740aab337db2353a |
| S723 | e2e4696cdcc5be9af460e16278a0d533a19cd8d4d2b4e43528b01e01a028414f |
| S740 | 4a14dec0ab7806e930e292e7a0a7d915473aa5b117f1d7e0e86f1b51e4a507a0 |

Wave-1 receipts named in the assignment were read for their attack evidence, not treated as new instructions or as current acceptance data. No builds, linters, acceptance counters or row checker were run by this seat. **Five fixable findings on five rows; no tradeoff is proposed.** Any claim/admission decision remains with the canonical Rust judge. The seven initial repair dependencies prevent a full final-32 assurance from this report.

Report: .ufo/waves/round-64/w2/CriticRowsFinal.md
