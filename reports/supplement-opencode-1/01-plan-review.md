# 01 — Plan review: falsifiability and no-harm checks for the three supplement-opencode-1 claims

- role: 01 PLANNER (read-only, baseline-scoped)
- baseline revision: `fe34faaafbe0add59ff68827a0df6c5782a72404`
- reviewed artifacts: `reports/supplement-opencode-1/claims.json`, `SCORECARD.md`,
  committed round-4 outputs (`git show fe34faa:…`), and the round-3 frozen baseline
- fleet governance read: `../PROTOCOL.md` §Gate standard, §Evidence standard, §Two evidences;
  `../AXES.md`
- lane governance read: `AGENTS.md`, `PROVINCE.md`, `corpus/QUALITY.md`
  (`corpus/knowledge/verification/gate-frozen-run-standard.md` read in full at HEAD)
- author-side only: no rank, no `SHONEN` change, no canon, no commit. I redefined no declared
  target; the acceptance conditions below are *evidence requirements on top of* the declared
  targets, not substituted targets.

## 1. Baseline facts I established (re-executed, not quoted)

| # | Command (cwd = lane root unless stated) | Observed |
|---|---|---|
| B1 | `python3 tools/assemble-d2.py --check` | `packet.d2.yml: byte-identical deterministic assembly`, exit 0 |
| B2 | `python3 tools/assemble-d2.py --selftest` | `error: unrecognized arguments: --selftest`, exit 2 — flag absent |
| B3 | `ls tools/replay-frozen.py tools/source-audit-inventory.py` | both absent at baseline |
| B4 | `for g in tools/gates/*.py; do python3 $g --selftest; done` | 7/7 exit 0 (costume 10/10, handoff 9 ids, lexicon, myth 6 IDs, naming 11 ids, phonology 15/15 + 26 controls, provenance); `git status --porcelain` afterwards shows only `?? reports/` → fixtures byte-untouched |
| B5 | python count over `corpus/knowledge/**/*.md` | 179 files, 123 files carrying the marker, **590 lines** with `to-verify`, **595 occurrences** |
| B6 | `sha256sum examples/culture-d2/packet.d2.yml` | `d5fb4088…dbd96` = the `d2_packet_sha256` pinned in `claims.json` → the claim-2 baseline digest is accurate |
| B7 | round-3 MANIFEST cross-check (7 rows) | all 7 `gate_sha256` match today's gate bytes; all 3 `input_sha256` match the committed snapshots under `frozen/round-3/inputs/` |
| B8 | round-3 replay from repo root, gates pointed at the **snapshot** paths | 5/7 rows reproduce **byte-exact** (exit + stdout sha256); the 2 `provenance-audit` rows differ in stdout only |
| B9 | the 2 provenance rows re-run with `cwd = tools/gates/frozen/round-3/inputs` and the *live relative* input path | **byte-exact** (`57a537ae…`, `1b8bf0b8…`) → 7/7 reproducible, exit 0, same counts (39 marks/32 lines; 1 mark/1 line) |
| B10 | 5 culture gates over the **live** packet vs over the **snapshot** | live: 3/0/0/0/18 = **21** findings; snapshot: 3/0/1/10/20 = **34** findings (live packet `d5fb4088…` ≠ snapshot `54be6319…`) |
| B11 | `cat tools/gates/frozen/round-4/*.out \| grep -c FINDING` | **21** FINDING lines across 5 files (phonology 3, lexicon 0, myth 0, costume 0, naming 18); no `MANIFEST`, no `inputs/`, no `expected.json` in `frozen/round-4/` |
| B12 | `ls corpus/lessons/round-4-audit/ \| wc -l` | **16** report files; the "17" figure is recorded in four committed places (LOG.md:2013; SCORECARD.md:12 and :31; `corpus/lessons/round-4-sol-fixes-and-audits.md:11`) plus the `fe34faa` subject |
| B13 | re-read LOG.md:2001–2003 | round 4 recorded "D2 design findings <= 10 … Measured: 24 (phonology 3 …, lexicon 0, myth 0, naming 18)" — the parenthetical sums to 21, not 24 |
| B14 | retrieval probe (2 fetches) | [WALS ch. 12](https://wals.info/chapter/12) full text retrieved; [UAX #15](https://unicode.org/reports/tr15/) full text retrieved; a Cambridge Core article returned **HTTP 429** (access limit) |

Round-4 frozen set reading under the fleet clause: 5 `.out` files with no digest pin are an
**`unpinned (legacy)`** measurement, not a frozen run — they are readable evidence, barred from a
conformance claim, and must never be silently re-pinned (`PROTOCOL.md` §Two evidences).

## 2. Claim 1 — freshness (source rechecks)

Declared: ≥10 distinct rechecked claims with URL/locator/limits/verdict; ≥5 with directly
retrieved supporting/contradicting passages; observable = structured rows in
`corpus/lessons/supplement-opencode-1/sources/*.json`; marker removal is not the metric.

**Falsifiability.** The claim is falsifiable *if and only if* the counting rules for "distinct",
"retrieved" and "5 rows" are pinned. As written, four readings pass the letter while failing intent:

- **C1a — distinctness.** Ten rows over one entry and one sentence ("X holds (to-verify)") satisfy
  "10 distinct claims" if distinct means "10 rows". Acceptance should require rows distinct as
  *(entry_locator + proposition)* pairs, drawn from ≥2 entries of ≥2 partitions; the parent's
  spot-check can then verify no locator repeats with a paraphrase.
- **C1b — snippet laundering.** The claim already bars snippets for the 5 retrieved rows; the check
  must be executable: for each of those 5, the parent re-fetches `source_url` and locates the
  `source_excerpt` string. An abstract, a citation index, or a record page is a locator, not a
  passage — `retrieval_status` must separate `full_text` / `record_or_abstract` / `blocked`.
- **C1c — unresolved rows counted as retrieved.** A row may have a retrieved source *and* verdict
  `unresolved`. Retrieved-nothing rows must not reach the ≥5 minimum; otherwise a worker can meet 5
  while confirming nothing. Acceptance should report the split explicitly (e.g. supported n /
  contradicted n / unresolved n among the retrieved rows).
- **C1d — digest drift.** `entry_sha256_before` must be the hash of the committed blob
  (`git show fe34faa:<path> | sha256sum`), not the working-tree file: other workers in this wave may
  append errata to the same entry, which would make two rows for one entry mutually inconsistent.

**Counterexample that would falsify a claim of success**: 5 retrieved rows that quote the *same*
source and the *same* sentence, plus 5 unresolved rows with record-only access, all written to
`sources/*.json`. Accepts as "10 rechecked, 5 retrieved"; fails QUALITY.md §1 (provenance) and the
axis intent. A second: any row whose `source_excerpt` cannot be found in the retrieved artifact.

**Coupling requirement is not yet falsifiable where it lives.** The batch contract demands ≥1 audit
testing language/myth/era/dress coupling, but `claims.json` claim 1 never mentions coupling, so a
score computed from `claims.json` alone cannot see whether it was met. Record it as a batch-level
acceptance item with its own row-level assertion (e.g. one row must cite a coupling entry such as
`corpus/knowledge/synthesis/era-myth-language-costume-matrix.md` and test a statement that binds
two systems, not a bibliography fact).

**Feasibility (measured).** Full-text public retrieval works in this environment: B14 retrieved
WALS ch. 12 verbatim, e.g. "there is a significant though not strong correlation between these two
measures of complexity (the correlation coefficient is .203 and the statistical significance level
is very high, p < .0001)" — a directly usable ≤40-word coupling passage (phonology ↔ syllable
structure). So the ≥5-passage bar is realistic; the realistic failure mode is *claims chosen that
only exist behind a paywall*, and the honest response is `unresolved` + `access_limit`, not a
laundered confirmation. My two fetches are feasibility probes only; they are **not** claimed as
claim-1 audits, and I wrote no `sources/*.json`.

**No-harm checks.** (i) Errata appended to a knowledge entry must not introduce the literal
`to-verify` string into `corpus/knowledge/` — that string *is* the SCORECARD counting command's
input, so a correction would silently move the freshness number (currently 590 lines). If a
correction must name it, report the before/after count with its unit and command. (ii) An erratum
to an entry that is also frozen (e.g. `mesoamerica-primary-sources.md`, snapshot-pinned in round 3)
does **not** invalidate the frozen run (it grades a byte copy) and must not be cited as making it
stale. (iii) `corpus/lessons/supplement-opencode-1/sources/` is outside `corpus/knowledge/`, so it
does not enter the admission bar or the index; it must not be listed in `corpus/README.md` by a
worker (parent-owned).

## 3. Claim 2 — operability (assembler selftest + frozen replay)

Declared: `assemble-d2.py --selftest` and `--check` pass; a stdlib frozen-replay command verifies all
pinned input digests before rerunning gates and rejects a tampered scratch input with exit 2 and
`snapshot_tampered`; all 7 gate selftests remain passing.

**Falsifiability.** Four of the five observables are exact commands (B1–B4 give the baseline side of
each). The underspecified one is **"actual frozen round-3 replay"** — it names no comparator, no
cwd, and no path semantics, and my measurements show those choices decide the result:

- B8/B9: from repo root against snapshot paths, `provenance-audit` stdout differs from the pin.
  The difference is only the echoed input path (`INFO to-verify-count: <path as passed>`); exit 0,
  findings 0, and the counts (39 marks/32 lines, 1/1) are identical. With `cwd = frozen/round-3/inputs`
  and the recorded *relative* path, all 7 rows reproduce byte-exact.
- Therefore the acceptance must name one comparator: **(a)** byte-level stdout equality with
  `cwd` = the baseline's input-snapshot root, or **(b)** the fleet comparator — exit code + finding
  set/count — with `stdout_sha256` advisory (the lane's own standard §4 says exactly this: "Compare by
  finding-ID **set**, not stdout order"; `stdout_sha256` is "optional; advisory"). A tool that runs
  gates by absolute snapshot path from repo root **and** compares raw stdout bytes fails 2/7 rows for
  a reason unrelated to tamper, and the tempting "fix" (rewriting the frozen `.out` bytes) would
  violate the lane standard's append-only rule and the fleet's unpinned-legacy rule.

**Counterexamples.**

- **C2a — wrong tamper target.** Tampering a scratch copy of a file the gate never reads proves
  nothing. The negative control must mutate a file that *is* a pinned input, and the tool must
  refuse *before* rerunning (observable: no gate stdout), printing `snapshot_tampered` and exiting 2.
- **C2b — re-pinning on the fly.** A replay that recomputes expected digests from the live tree on
  each run reads "match" after any edit. Digests must be compared against the committed
  `MANIFEST.tsv` values only.
- **C2c — verbatim command replay.** The round-3 manifest's `command` column names the **live**
  path (`python3 tools/gates/naming-collision-gate.py examples/culture-d2/packet.d2.yml`), while
  `input_snapshot` names the byte copy. Replaying the recorded command verbatim today measures the
  round-4 packet: 21 findings, exit pattern 1/0/0/0/1 (B10), i.e. drift for the wrong reason. The
  acceptance must state that the snapshot column is authoritative.
- **C2d — selftest without a negative control.** `--selftest` that only asserts "`--check` exits 0"
  would pass a weak reading. The assignment already requires positive *and* negative controls; make
  it checkable: at least one assertion must fail if the assembler's extraction or duplicate-ID guard
  is disabled, and the negative control must not write `packet.d2.yml`.

**No-harm checks.** (i) The 7 gate scripts must keep their bytes — B7 shows every round-3
`gate_sha256` still matches; editing any gate would flip baselines to `gate_revised` (could-not-
evaluate) and break the declared replay. (ii) `--check` byte-compat must hold before and after the
change: `packet.d2.yml` = `d5fb4088…` (B6); the parent owns regeneration, workers must not rewrite it.
(iii) `--selftest` must leave the tree clean; my B4 battery run shows the gates' own selftests are
byte-idempotent (`git status` clean), so the same rule is enforceable for the new flags.
(iv) The new files are `tools/replay-frozen.py` (new) and an added flag in
`tools/assemble-d2.py`; no frozen artifact may be rewritten.

**Standard gap to report, not absorb.** Fleet §Two evidences requires *the gate* to verify the pinned
digests before comparing verdicts, and the lane standard §8 lists gate-internal
`--frozen <baseline-dir>` as unbuilt; an external replay command achieves the effect but not the
letter. Also, the committed round-3 layout is `MANIFEST.tsv` + `inputs/` + `.out` files, not the
standard's per-gate `expected.json` layout (§3–§4). The claim's verdict must say which of the two it
implements so the fleet clause is neither claimed nor silently dropped. The round-4 `.out` set stays
`unpinned (legacy)`; the claim correctly targets round 3 only.

## 4. Claim 3 — calibration (count corrections + uncertainty inventory)

Declared: append an evidence-backed LOG correction with *exact* dispatch/item and finding totals
"that can be established"; unresolved historical facts stay unresolved; produce a reproducible
uncertainty inventory; no score increase without a defined derivation.

**Falsifiability.** "That can be established" is an escape hatch: any number can be declared
unestablishable without evidence and the claim still reads satisfied. Acceptance requirement: for
every corrected number, the entry must name (i) the artifact, (ii) the counting command, (iii) the
scope/unit; and for every number it declines to correct, the reason must be a *specific*
irrecoverable fact (e.g. "the result set was never persisted"), not a bare "unclear".

**Count discrepancies I can demonstrate from committed bytes** (attribution unresolved — this is
exactly the honest-correction zone):

1. **D2 findings, round 4.** LOG:2001–2003 and the `fe34faa` subject say `34->24`. The five committed
   round-4 `.out` files contain **21** FINDING lines (B11). Derivations: `34 − 10 (costume) = 24`
   leaves myth's 1 and naming's 20 in place, i.e. 24 matches a *pre-naming-fix, pre-myth-fix* state;
   `34 − 1 (myth) − 10 (costume) − 2 (naming 20→18) = 21` matches the artifacts. Which is right
   depends on the revision each number was measured at, and no committed file pins it. Counting
   command for the recomputation: `cat tools/gates/frozen/round-4/*.out | grep -c FINDING`.
   The correction must either cite a revision whose artifacts sum to 24 or record 21 with that
   command — and must not re-base the round-4 claim, which stays falsified as declared (round-4
   lesson: no silent re-basing).
2. **Audit-report count.** `corpus/lessons/round-4-audit/` holds **16** files, while "17" is recorded
   in four committed places (LOG.md:2013; SCORECARD.md:12 and :31;
   `corpus/lessons/round-4-sol-fixes-and-audits.md:11`) plus the commit subject. The plausible 17th
   is `corpus/lessons/round-4-sol-fixes-and-audits.md` in the parent directory. Correction: state the
   scope ("16 under `round-4-audit/` + 1 round-4 lesson file"). Command:
   `ls corpus/lessons/round-4-audit/ | wc -l`. A same-string collision to watch while sweeping:
   `corpus/lessons/round-4-audit/civ-08-14.md:31` has a heading "Current-marker coverage — 17 audit
   rows" — that is a marker-row count, not the report count.
3. **Round-2 dispatch arithmetic.** LOG:1451–1455: "46/49 completed, 7 filter-killed"
   (1 + 1 + 5 named) → 46 + 7 = 53 ≠ 49. Round-1 (62 = 47 + 15), round-3 (34 = 25 + 3 + 6) and
   round-4 (32 = 31 + 1) are each internally consistent. Either 49 counts something other than
   "dispatched" or the completion figure is wrong; unestablishable from the committed text — record
   as unresolved with the arithmetic shown, do not guess.
4. **Marker-count units.** `SCORECARD.md` freshness uses `grep -rc` → **lines** (612 at round 3;
   my B5 count at fe34faa = **590 lines**, matching `claims.json`'s `raw_to_verify_lines`), while
   many LOG entries report `grep -o` → **occurrences** (595 now). Every "exact total" must carry its
   unit and command; a total that mixes them is a defect.

**Uncertainty inventory.** `tools/source-audit-inventory.py` does not exist at baseline (B3) yet is
in the claim's observable, so it is a required new file. Falsifiability requirements:
- deterministic: two runs over the unchanged tree produce identical output (byte or sorted-lines
  identical);
- non-trivially populated: it must classify markers into at least (i) unresolved claims, (ii)
  resolved-with-retrieved-source, (iii) non-claim vocabulary/scheme tokens. Rounds 1–4 recorded
  large non-claim classes (V3 "30 vocabulary tokens", V04 "5 `n/a — not a claim`", V07 "4 rule
  tokens retained"), and the method entries are the concentrated case (measured at fe34faa:
  `to-verify-triage-protocol.md` 12 marks, `provenance-audit-ledger-format.md` 9,
  `verification-method-overview.md` 9). Note the vintage trap: `mesoamerica-primary-sources.md`
  reads 39 marks/32 lines in the round-3 frozen snapshot but 12 occurrences/11 lines at HEAD
  (the round-4 triage edited it), so any inventory must name the revision it counted;
- **counterexample C3a**: an inventory that prints "0 unresolved" or merely counts markers would
  satisfy "produce an inventory" while asserting the opposite of the axis intent. Seed it with ≥3
  known-unresolved items (e.g. the S18/SN16 full-text gaps recorded at
  `mesoamerica-primary-sources.md:144`) that must appear as unresolved; and it must never treat
  marker absence as verification (QUALITY.md §1).
- Adding `corpus/lessons/supplement-opencode-1/sources/*.json` and the inventory tool must not
  change the 590-line marker count (no new markers in `corpus/knowledge/`).

**No-harm checks.** (i) `LOG.md` is parent-owned — the claim's observable names an appended LOG
correction, so worker evidence must be *proposed text with locators*; two workers must not both edit
LOG.md (double-append race), and the appended entry must cite the `fe34faa` hash and the artifacts.
(ii) Append, never rewrite (fleet §Evidence standard; the round-4 lesson file and the round-4 LOG
entry stay legible as falsified-as-declared). (iii) The superseded mention inside the `fe34faa`
commit message cannot be edited; the correction must name it and sweep the other mentions. My sweep
found the "17" in four committed files — LOG.md:2013, SCORECARD.md:12 and :31,
`corpus/lessons/round-4-sol-fixes-and-audits.md:11` — so the sweep is a multi-file edit, not a
single-line fix. Two collisions to avoid in that sweep: `civ-08-14.md:31` ("17 audit rows", a
marker-row count) and `costume-semiotics.md:95` ("*Wars* 8.17 reports", prose). The round-4 "24" sits
at LOG.md:2001 and in the immutable commit subject; LOG.md:226 carries a same-looking 24 for an
unrelated round-1 marker count. A concurrent uncommitted report
(`reports/supplement-opencode-1/27-claims-critic.md:92`) flags the same 24/21 mismatch independently —
not my evidence, but it means the correction will be cross-read. (iv) `SCORECARD.md`
evidence-link updates are parent-owned; no numeric score may rise without the derivation the claim
demands.

## 5. No-harm summary across the three claims (ranked risks)

| # | Risk | Where it would show | Guard |
|---|---|---|---|
| R1 | Frozen bytes rewritten or re-pinned to make a replay green | `tools/gates/frozen/round-3/**`, `round-4/*.out` digests change | replay compares to committed MANIFEST values only; append-only; round-4 stays `unpinned (legacy)` |
| R2 | A gate script edited, invalidating the replay baseline | gate `sha256` ≠ B7 values | verify gate hashes before/after; `gate_revised` is exit 2 and must be reported, not smoothed |
| R3 | Errata adding `to-verify` markers to `corpus/knowledge/` | raw count ≠ 590 lines | erratum text discipline; report any delta with its command |
| R4 | Concurrent writers on shared bookkeeping | LOG/SCORECARD diff conflicts or duplicates | workers hand off proposed text; parent appends once |
| R5 | Marker removal counted as source verification | `sources/*.json` rows without retrieved passages | `retrieval_status` split (C1c); `stdout`/record pages never counted as passages |
| R6 | Claim scored off `claims.json` alone, missing the coupling-audit and batch-level requirements | verdict text | verdict must name the coupling row and the batch-level items explicitly |

## 6. Limits of this review

- Read-only: I wrote only this report (a scratch dir I created was emptied and removed; one
  auto-cleaned `/tmp` file). No code, corpus, LOG, SCORECARD, or frozen artifact was touched. At my
  measurement batch the tree was clean except `?? reports/`; by the end of my run the working tree
  carried *other workers'* edits (`tools/assemble-d2.py`, `tools/replay-frozen.py`,
  `tools/source-audit-inventory.py`, several corpus entries) — none of them mine, none of them
  assessed here, and all B1–B14 numbers remain baseline-vintage measurements at `fe34faa`.
- I did **not** produce claim-1 audit rows; my two successful fetches and one HTTP 429 are
  feasibility probes quoted here as such, not rechecks of assigned entries.
- Attribution for every count discrepancy in §4 remains **unresolved**: the committed bytes show
  the mismatch, not which revision each recorded number measured. Resolving them requires evidence
  that no longer exists in the repo (per-run result sets) or a cited intermediate revision.
- Two-sided uncertainty: B9's 7/7 byte-exact reproduction is measured at `fe34faa` with today's gate
  bytes; if a worker edits `assemble-d2.py` only, the replay should still hold, but if any gate file
  changes the replay must be reported `gate_revised`, not adjusted.
- Concurrent uncommitted work by other workers was present during my run (other scratch directories;
  `corpus/lessons/supplement-opencode-1/` appeared mid-run). I judged nothing that is not in the
  committed baseline.
