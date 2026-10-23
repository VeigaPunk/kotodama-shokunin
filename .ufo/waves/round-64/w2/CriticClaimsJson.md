# CriticClaimsJson — declaration drift and control review

Axes: **coverage**, **operability**, **calibration**. Independent leaf critique only; no claim admission, round verdict, counter execution, integration, index mutation, commit, or runtime invocation.

## Snapshot and dependency

Reviewed at `2026-10-23T23:51:46-03:00`. SHA-256:

| Artifact | SHA-256 |
|---|---|
| `reports/round-64/claims.json` | `e970aaceafa377230c91775f5b1b34e69aeb176faa52404715653d911a09bd3a` |
| `reports/round-64/accept-c.py` | `4df7b32b430282c81970acf9b6565c6ef96e598038f82ca843a2cace2de08a68` |
| `reports/round-64/accept-o.py` | `c27a9fefb37c4a107e83867fd03f9194d89ce4e0dc8364e9b1b23e7821987b18` |
| `reports/round-64/accept-ca.py` | `f222648ea45517d5e4f7cf27c888e686253fdc67741b23ab458e9ef82081d678` |

**The requested post-revision state was not available at this snapshot.** The headers still say C revision 0, O revision 3, Ca revision 0. More importantly, C still lacks both new guards (`accept-c.py:248–314`); Ca still uses whole-log bare-token NITS (`:143–145`); O still accepts an unvalidated selector set (`:426–448`) and uses the broad m5 replacement. Thus this is not merely a stale header. A targeted glob found no `w2/RevCounters.md`, `w2/RevVerify*.md`, `w2/CounterDrift.md`, `w2/ReSourceS729.md`, or telemetry `*rev*.txt`. These are snapshot dependencies, not assertions that the other seats will not finish. No waiting or re-execution of reported failures was performed.

## CJ1 — C's disposition description is already false

**Counterexample / evidence:** `claims.json:11` says “six rejected rows S744-S749”; `:20` exports the entire block as rejected. The staged rows actually contain:

| IDs | Status and evidence |
|---|---|
| S744 | `rejected`; ordinary request serves Khanka rather than ushanka |
| S745 | `rejected`; ordinary request returned 403 |
| S747 | `rejected`; ordinary request returned 403; its repaired anchor no longer invents a quotation |
| S746 | `queued`; `QUEUED-CANDIDATE`; reconstructed catalogue wording locates, but exact historical wording remains unrecovered |
| S748 | `queued`; `QUEUED-CANDIDATE`; fresh 200 and LOCATED contradict the prior no-page ground |
| S749 | `queued`; `QUEUED-CANDIDATE`; fresh 200 and substantive LOCATED text contradict listing-only rejection |

Direct evidence: `.ufo/waves/round-64/rows/ScribeRejS744/row.txt:1` through the corresponding S749 files. Wave-1 independent support evidence: `w1/ReviewSupportC.md:33–44`. The counter's REJECTS description already permits `rejected` **or** `queued` (`accept-c.py:24–29`), as does its implementation (`:233–245`). This is declaration-versus-real-disposition drift, not grounds to force reachable candidates back to rejected.

**Impacted axes:** calibration and coverage accounting.

**Smallest honest L1 patch, without changing a predicate or leg:**

- In `C.statement`, replace only `six rejected rows S744-S749` with `six disposition rows S744-S749 (S744/S745/S747 rejected; S746/S748/S749 queued candidates)`.
- In `C.exports`, replace the disposition suffix with `S744/S745/S747 (rejected), S746/S748/S749 (queued candidates)`; retain `S718-S743 (mined)`.
- The matching prose in `accept-c.py:8–10,39–40` still says rejected candidates / `26 mined + 6 rejected`; the counter owner should describe disposition rows there, not alter APPEND or REJECTS behavior.

### Remaining C statement elements, including S729

| Statement element | Effect of the planned repairs |
|---|---|
| “26 registry rows S718-S743” | Retain. An ID-preserving replacement of S729 changes source identity, not the row count or range. Do not shrink the claim to 25. |
| “opened this round” | Retain as a requirement for the replacement source, with fresh source/quote/access evidence. The old paper's opening cannot prove that the new paper was opened. |
| “and cited by it” | Retain, not weaken. The planned citation guard repairs enforcement of this existing promise. No post-repair citation receipt was available here. |
| One new entry, corpus 237→238, linguistics 29→30 | These repairs do not imply any change to those planned counts. They remain targets, not measurements made by this review. |
| Registry 643→675 | Retain: 26 mined + 3 rejected + 3 queued still adds exactly 32 rows. Queued is not deletion or admission into the new entry. |
| Curating routed defect 7 | Retain: honest retest reversals are dispositions of that defect. S746 must not be described as having disproved the original absent-quote ground, because the exact original wording is unrecovered. |
| S687 mined→queued, logged old→new | No effect from these row repairs; no statement patch justified here. |

At the last direct read, S729 was **still** Farran et al. 2016, e0151518 via PLOS, with the Lebanese-versus-American IDS finding. `w1/ReviewerRegistry.md:64–76` identifies it as the same work/finding as S718 via PMC. `nw2-spec.json`'s ReSourceS729 item requires a genuinely different peer-reviewed open-access source while keeping S729 and its topic slot. Therefore the replacement is an outstanding source-identity dependency, not a completed repair observed by this critic. The existing claim says 26 **rows**, not 26 distinct papers: do not silently invent a stronger source-count claim. Conversely, do not reuse the old `ReviewSupportB`/PLOS LOCATED verdict, capture, or bullet as evidence for the replacement. Regenerate the assembled S729 bullet from the final row and obtain support for that new identity.

## CJ2 — literal predicate-byte identity is not satisfied; lexical content agrees

The canonical strings in `claims.json:12,33,54` are:

```text
ACCEPT-C-64: every leg of reports/round-64/accept-c.py prints PASS.
ACCEPT-O-64: every leg of reports/round-64/accept-o.py prints PASS.
ACCEPT-CA-64: every leg of reports/round-64/accept-ca.py prints PASS.
```

Raw docstring reads show the following exact difference (`\n` denotes a literal LF):

| Counter | Predicate substring in docstring | Drift |
|---|---|---|
| C `:50–51` | `ACCEPT-C-64: every leg of reports/round-64/accept-c.py prints\nPASS.` | LF replaces the JSON space before `PASS.` |
| O `:118–119` | `ACCEPT-O-64: every leg of reports/round-64/accept-o.py prints\nPASS.` | Same LF-versus-space difference |
| Ca `:41–42` | `ACCEPT-CA-64: every leg of reports/round-64/accept-ca.py\nprints PASS.` | LF replaces the JSON space before `prints` |

There is **no word, counter-path, claim-ID, or punctuation drift after unwrapping those line breaks** in this snapshot. That is not literal byte equality, and it is not a post-revision result. Keep these two conclusions separate.

Receipt bodies do not contain the frozen sentence at all. They contain outcome labels:

- `dry-run-c.txt:13`: `ACCEPT-C-64: FAIL`.
- `dry-run-ca.txt:8`: `ACCEPT-CA-64: FAIL`.
- `final-measures-o.txt:28`, `mut-o.txt:26`, `edge-o.txt:15`, `control-o.txt:41`: `ACCEPT-O-64: PASS`.
- `dry-run-o.txt` and `dry-run-o-baseline-copy.txt` end after PRIV, without any ACCEPT label.
- The C control receipt named by JSON, `telemetry/controls-c.txt`, was absent.

The **label identifiers agree** with the canonical predicates wherever labels exist; a status label is not a byte-identical predicate sentence. Absence/truncation is not evidence that a different sentence was printed.

**Impacted axes:** calibration; operability if equality checks silently normalize or treat a short status label as a complete predicate.

**Smallest safe correction:** preserve all three JSON predicates exactly. In the authorized pre-data documentation repair, serialize each quoted predicate as one uninterrupted line in its counter docstring. Receipt metadata should carry that exact sentence separately from unmodified observed stdout, alongside counter hash and command/scope. Do not replace or fabricate historical output. If the intended check is only label-ID equality or whitespace-normalized sentence equality, state that explicitly instead of reporting a byte-identical result.

## CJ3 — an O PASS label alone is not the declared all-legs predicate

**Strongest local counterexample:** `telemetry/edge-o.txt` explicitly records `--only EDGE_SCHEMEREL,...,DRIP`, prints `TOOL SKIP` and `MUT SKIP`, yet ends `ACCEPT-O-64: PASS`. `telemetry/mut-o.txt` records `--only MUT`, prints the eight edge/DRIP legs SKIP, and ends the identical PASS label. `control-o.txt` similarly selects GEN,MUT. The full `final-measures-o.txt` separately records a no-`--only` rev3 run and all 23 PASS legs. These receipts have different scope despite sharing the outcome label.

Wave-1 `ReviewerCounterO2.md:23–51` additionally records `--only NOSUCHLEG` returning the same PASS/exit 0. I did not rerun that reported failure. The proposed rev4 selector repair addresses unknown names; it does not turn legitimate selected-leg receipts into full acceptance evidence.

**Impacted axes:** calibration and operability.

**Smallest safe correction:** classify selected runs as controls/diagnostics; only a complete no-`--only` receipt can evidence the unchanged all-legs predicate. Preserve exact predicate metadata and the actual command. After revision, do not cite the existing rev3 full receipt as a rev4 measurement: its header explicitly binds `c27a9fef…`/revision 3. Update the declaration's receipt references to the actual newly measured paths rather than silently using an old path or treating a planned `*-rev4.txt` as present.

## CJ4 — the four named control families remain useful, but their old descriptions are insufficient

Here “four” means the named C stub, O old-counter baseline, O cosmetic-tool patch, and Ca records-only intervention. JSON also names the Ca base-tree baseline; C's do-nothing baseline exists outside `controls.C`. Inventorying all of them avoids dropping a baseline through counting ambiguity.

| Control | Post-revision assessment and smallest safe correction |
|---|---|
| **C: sourceless stub + copied registry rows** (`claims.json:70`) | Keep the negative. **Its historical expected vector changes:** `w1/CriticClaims.md:61–80` uses one cited S719 bullet and observes `ONEID PASS cited_lines=1`. A guard requiring every S718–S743 exactly once must reject that specimen. Do not weaken the new guard to preserve JSON's unconditional “passes ONEID.” For that existing specimen, say FILE/SWEEP pass while ROWS/RESTATE and the completeness guard fail. Alternatively identify a distinct 26-citation stub explicitly, rather than pretending it is the same fixture. File the named `controls-c.txt`, currently absent. |
| **O: round-63 counter lacks EDGE_/DRIP** (`:71`) | Keep: it establishes the missing baseline scoring surface. `control-o.txt:4–16` supplies the grep/unsupported-option evidence now. The truncated, duplicated `dry-run-o*.txt` files are not a substitute for that evidence or a completed baseline run. |
| **O: docstring-only tool patch** (`:71`) | Keep as a mutation-harness control: GEN remains green while each rebuilt mutant dies on its pins. This control deliberately prints `MUT PASS`; it is not a must-FAIL whole-O negative, nor evidence that a cosmetic tool edit created the capability. Rerun against rev4/m5 bytes and bind the receipt to that hash. The current control header says revision 3. |
| **Ca: records-only prose without named values** (`:72`) | Keep, but it does not discriminate the repaired NITS requirement. Extend with the actual bare-token/W04 forcing specimen and a wrong-association/lookalike-phrase negative; require NITS FAIL in addition to the original PTRS/HISTOGRAM/REVNAMES failures. Preserve a genuine scoped-correction positive. `w1/CriticCa.md:74–95` demonstrates the old NITS false positive despite the three originally named legs remaining FAIL. |

Additional controls required to explain the authorized revisions, not replacements for the old ones:

1. **C teaches-copy:** the 26-copy specimen in `w1/CriticClaims.md:105–124` observed `RESTATE PASS lines=26`; revised RESTATE must reject it for copying teaches, not merely rely on LINK/NOHARM to fail elsewhere.
2. **C citation completeness:** the zero-citation specimen in `w1/ReviewerCounterC.md:132–150` observed a whole-counter PASS; zero and 25-of-26 citations must fail, paired with one supported citation of each required ID.
3. **O m5 selectivity and selector fail-closure:** retain the cross-failure receipt; on the narrowed m5, EDGE_SCHEMEREL must pass while EDGE_SLASHLESS fails. Unknown-only and mixed valid/unknown selectors must exit 2, not print a success claim.
4. **Ca base:** keep the all-seven-fail baseline. `dry-run-ca.txt` contains only six leg results (REVNAMES absent), so it cannot prove “every leg” of the seven-leg revised counter fails. `w1/CriticCa.md:33–45` supplies a seven-leg historical rev1 negative; a rev2 assertion needs a rev2-bound observation.

**Impacted axes:** all three; particularly calibration of what each control establishes. These are fixable evidence/description defects, not acceptable axis tradeoffs or saturation evidence.

## CJ5 — O's “exactly their pinned leg” remains stronger than the stated repair can prove

Although the requested C patch is above, this matters to the controls' adequacy. `claims.json:32` promises ten mutants each fail **exactly** their pinned leg. m8 is explicitly pinned to **two** legs, GEN+BOUND (`accept-o.py:1049–1052`). More importantly, the current MUT loop invokes each mutant with `--only` its pins (`:1076–1091`), so no unselected leg can expose a cross-failure in MUT. Narrowing m5 and checking two legs repairs the known counterexample, but does not establish exclusivity for all ten mutants.

Evidence: `w1/ReviewerCounterO2.md:53–66`; `w1/ReviewerOReceipt.md:30,38`; `w1/CriticO.md:128–148`; the current code above. The saved rev3 m5's observed failure set includes both EDGE_SCHEMEREL and EDGE_SLASHLESS, despite its singleton pin.

**Impacted axes:** operability and calibration.

**Smallest safe correction:** do not mark the stronger statement established from pinned-only receipts. At minimum use plural **pinned leg(s)**. To retain the declared exclusivity promise, evidence must cover non-pinned applicable behavior as well, while avoiding recursive MUT execution. Narrowing the statement to “every pinned leg fails” would change the promise; that is an explicit L1 pre-data declaration decision, not a critic's wording cleanup and not authority to weaken any counter leg. This report neither edits that promise nor judges it accepted.

## Scope and exercised checks

Read the named wave-1 attack receipts, the current claim/counter sections, staged disposition/S729 rows, and receipt bodies. Ran only SHA-256 fingerprinting and a timestamp command; used targeted static reads/searches/globs. No acceptance commands, builds, tests, mutations, network reopens, source installs, or tool updates were run. No claim/counter/row was edited. The only lane write is this requested report. Post-revision comparison and replacement-source evidence were unavailable at the snapshot; findings above distinguish observed defects from those missing dependencies.

Report: `.ufo/waves/round-64/w2/CriticClaimsJson.md`
