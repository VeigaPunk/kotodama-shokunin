- Seat: C05 (completion) | verifier | claim C | date 2026-10-19 | baseline dfb0719

# C05 — audit of the four verification-partition entry drafts (claim C / coverage)

Round 39 (regimen 2, loop 1, position 7), seat **C05**, role **verifier**, claim **C**. Mission
(verbatim, `reports/round-39/targets.json` → `seats[id=C05].mission`): *"Audit all 4 drafts (runbook
checks + source-pointer resolution); defects filed."* This is the **completion seat**: the original
C05 hit a concurrency error; all 15 sibling seats landed. A prior C05 draft landed at ~12:39Z
(fragment sha256[:16] `91a4b4165fe4a96a`, superseded by this file — see §7); R01-4 recorded C05
absent at its close. Every reading below was **re-measured from the filed bytes by this seat**;
where the prior draft is confirmed the reading is unchanged, where corrected the correction is named.

- Lane root `/home/vgpnk/Projects/shokunin/kotodama-shokunin`; `git rev-parse HEAD` →
  `dfb0719711204b5943432034bd80c8dc248acddd` (== declared baseline `dfb0719`); audit window
  2026-10-19 13:05–13:25Z; at close `git status --porcelain` → `?? reports/round-39/` only.
- **Canon: NON-CANON.** This seat audits bytes and files defects; it admits no entry, certifies no
  round, promotes nothing. A green reading is a structural reading of named digests — never a
  verdict on the scholarship, never canon (`PROVINCE.md`).
- **Writes**: this file only, plus gitignored `.scratch/c05c/`. No `corpus/**` byte, no `tools/**`,
  no filed round-1..38 byte. No commit, no push, no install, no network.
- **F-C13-1**: no `reports/round-*/run-validation.py` was executed anywhere, in-tree or in a copy.
  The only filed code executed is read-only: `reports/round-28/readme/sweep.py` (index instrument,
  run twice — §2.2/§5) and the round-35 audit instrument installed from filed bytes (§0).

## 0. Instruments and audited bytes

| instrument | source | digest / result |
|---|---|---|
| **I-C12** (round-35 runbook instrument) | `reports/round-35/cov/C12-audit-runbook.md` §5, installed by its own step-0 awk | sha256 `973610275404e9e3183d46e33e5352562265e6c2e397c92291e63c401ed7562d`, 663 lines — equals the filed digest; `--selftest` → exit 0, SELFTEST PASS; byte-identical to the original seat's install |
| **I-C05** (resolver, carried from the original seat) | `.scratch/c05/c05-audit.py`, sha256 `4326bb856e13e34a3334e4769140e4ee20a1a1d1266a91d8616eb557da75cbd6` | `--selftest` → exit 0, SELFTEST PASS (fence-run 4bt+inner, multi-block; attached/bare/detached citations; out-of-range; dangling; determinism) |
| **corrected-binding re-check** (this seat) | inline script, nearest-preceding detached-`:n` binding (the I-C05 docstring's stated rule; see F6) | 137 line refs over the four staged entries, **0 out-of-range** |

Audited bytes (extracted fresh by this seat with a fence-run parser, 2026-10-19 ~13:10Z):

| seat | fragment | fragment sha256[:16] | entry block bytes | entry sha256[:16] | fence |
|---|---|---|---|---|---|
| C01 | `cov/C01-entry-1.md` | `91ba710d95c9f4a8` | 31 562 | `b46e66ea86bf1740` | one 4-backtick block |
| C02 | `cov/C02-entry-2.md` | `788af6bccbf2baab` | 19 743 | `f19c61551868cd9a` | one 3-backtick block |
| C03 | `cov/C03-entry-3.md` | `d476c8dce5373607` | 33 525 | `581214d045d9a1bf` | 4-backtick entry + 3-backtick receipt |
| C04 | `cov/C04-entry-4.md` | `94348f9601d7f92480e` | 24 296 | `1a8485e733709907` | one 3-backtick block |

Staged shapes: C02 by the r35 stager regex → 19 745 B, sha256 `eabb1d63ddc66b7c…` (equals the
entry's own pin); C03 block0 + `\n` → 33 526 B, sha256 `3fa037ae9f95de74…` (equals R01 §2.3's
staged digest **and** the F1 transient's recorded digest, §5).

**Verdict at a glance:** **4/4 PASS** the round-35/36 structural contract; 2 of 4 additionally
`clean` (C03, C04) — the runbook's review-tier hits on C01 (×5) and C02 (×1) are all adjudicated
false positives (§4). **129 attached `path:line` citations / 134 line numbers: 0 unresolvable,
0 out-of-range, 0 missing files** (independent corrected binder: 137 refs, 0 out-of-range). Every
quoted absence sweep reproduces at the clean tree; every pinned digest matches live bytes. No S1
finding. Defects: one **S2 process** (transient, closed on tree, §5) and **five S3** (§6).

## 1. C01 — `worked-example-verification.md`

**Verdict: PASS-with-named-defects** (one S3: the `24/24` couples count, §6 F2).

| # | check | observed result |
|---|---|---|
| 1a | head-block: `- topic` / `- gap filled` / `- sources` / `- source` / `- couples` / `- verified-at` / `- recheck` / `- scope` | all 8 present; `verified-at` ISO `2026-10-19`; no `- calibration:` head field (the clause is body §8 "Calibration") — the executable bar does not require it (R01-11 agrees) |
| 1b | round-10 five-field set (`topic, sources, verified-at, recheck, couples`) | 5/5 present |
| 2 | source-pointer resolution | I-C12 pointer leg 15/15 resolve; I-C05: 46 unique repo paths, **0 unresolved**; 44 attached citations / 44 line numbers, **0 out-of-range**; corrected binder 44/0 |
| 3 | couples resolution | 19 backticked in-repo path tokens (+ plain-text `AGENTS.md`) — **all resolve**; the entry's stated "24/24 targets resolve" is **not reproducible** (F2) |
| 4 | decision record | `## 9. Decision record` with `DR-WE-01..10`, all ten defined in-section, none dangling (§10 also quotes `DR-TK-1..5` from the demonstrated file) |
| 5 | absence sweeps re-run | `grep -rl "NON-CANON" corpus/knowledge/*/*.md \| wc -l` → **22** ✓; `grep -ril "worked example" …` → **18** ✓; `grep -rEc "^## .*([Ee]xample\|[Ff]ixture)" … \| awk sum` → **20** ✓; five absence probes → **0 0 0 0 0** ✓; heading sweep → 20 distinct example/fixture headings ≥ the "at least twelve" claimed ✓ |
| 6 | digest pins | 1 pin, MATCH: `corpus/knowledge/culture-material/timekeeping-instruments.md` sha256[:16] `9805c0b854334ed3` = live bytes ✓ (the I-C12 pin line was classed historical/false-positive — its heuristic bound the pin to the nearest pointer, `claims.json`; r35 F13 class) |
| 7 | fabrication spot-checks (13 needles) | `verification-method-overview.md:54,:161,:206`; `internal-consistency-audit.md:168`; `label-channel-routing-verification.md:82`; `gate-frozen-run-standard.md:144`; `verification-independence-anti-circularity.md:3`; `worked-example-mini-culture.md:2`; `historical-linguistics.md:55`; `timekeeping-instruments.md:111,:112,:134` — every cited line says what the entry claims |
| 8 | cross-domain bleed | 1 candidate (L80 "cleared") + 4 `canon` mentions (L7, L27, L42, L80): all read in full, all false positives (§4); canon boundary named ✓; admission idioms 0 |
| 9 | fence/staging | one 4-backtick fence — the r35 3-backtick stager regex does **not** match it (R01-10; integrator must stage both shapes) |
| — | `to-verify` census (parenthesised form) | 5 (all `(**to-verify**)`-shaped) ✓ |

## 2. C02 — `index-sweep-verification.md`

**Verdict: PASS-with-named-defects** (two S3: unnamed `ghost` reading + "folklore files" descriptor, §6 F3).

| # | check | observed result |
|---|---|---|
| 1a | head-block | `- topic` / `- gap filled` / `- sources` (block-valued) / `- calibration` / `- couples` / `- source` / `- verified-at` / `- recheck` — 8 fields; no `- scope:` (not required) |
| 1b | five-field set | 5/5 present |
| 2 | source-pointer resolution | I-C12 7/7 resolve; I-C05: 8 unique paths, **0 unresolved**; 9 citations / 9 line numbers, **0 out-of-range** |
| 3 | couples resolution | 16 distinct tokens, **all resolve** (incl. `../synthesis/*` relative forms) |
| 4 | decision record | `## 7. Decision record` with `DR-IS-01..09`, all nine defined, none dangling |
| 5 | absence sweeps re-run | main term sweep `grep -rliE "index sweep\|counts footer\|totals line\|header drift\|ghost row\|orphan row\|duplicate row" corpus/knowledge/` → **0** ✓; `ghost` → **13** case-sensitive ✓ (reading unnamed — F3a); `topic mismatch` → **1**, at the cited `linguistics/register-strata-attestation.md:31` (a quoted sweep-output line) ✓ |
| 6 | digest pins | `corpus/README.md` sha256 `b80274bcd24b8b6e621f499fb20d4a07aa3b7b48dbb3508e0a9ac974f68e1d74` MATCH ✓; `reports/round-28/readme/sweep.py` sha256 `9b2ccac0046831fdaf48863ccd0ff6ca0fa390d044746c876e83a71c06f0cdd3`, 17 117 B, selftest **12/12** ✓; staged digest `eabb1d63ddc66b7c…` (19 745 B, stager shape) MATCH ✓; r27 leg claims verified in code (`:133` ok-gate has no footer term; `:314` selftest "9/9") ✓ |
| 7 | live replication (r28 instrument, read-only) | `parts 21/23/25/29/20/94`, `rows 212 files 212`, missing 0, topic_mismatch 0, orphan_rows 0, header_drift {}, totals 212 ok, footer ok vector `21/23/25/29/20/94`, README digest as pinned, **rc=0** ✓; independent duplicate-row parse → 212 rows, **0 duplicates** ✓ |
| 8 | fabrication spot-checks (16 needles) | `sweep.py:2,:15,:419`; `README.md:11,:43,:52,:97,:505,:510`; `x27-coverage-readme-vs-files.md:47,:132`; `verify.md:21`; `r27/sweep.py:19,:133,:314`; `two-reader-interop-agreement.md:13` — all as claimed |
| 9 | cross-domain bleed | 1 candidate (L89 "the disposition cites the re-run that cleared it"): ordinary sense, false positive (§4); canon boundary named ✓ |
| 10 | fence/staging | one 3-backtick ```markdown fence — stageable by the r35 stager regex ✓ |
| — | `to-verify` census | 1 ✓ |

## 3. C03 — `contact-strata-verification-gate.md`

**Verdict: PASS** (no entry-level defect; one wave-level process finding F1, §5).

| # | check | observed result |
|---|---|---|
| 1a | head-block | `- topic` / `- gap filled` / `- sources` (block) / `- calibration` / `- couples` / `- source` / `- verified-at` / `- recheck` / `- scope` — 9 fields |
| 1b | five-field set | 5/5 present |
| 2 | source-pointer resolution | I-C12 13/13 resolve; I-C05: 16 unique paths, **0 unresolved**; 72 citations / 72 line numbers, **0 out-of-range**; corrected binder 75/0 |
| 3 | couples resolution | 12 distinct tokens, **all resolve** — equals the fragment's own receipt (`couples_resolved: 12, couples_unresolved: []`) |
| 4 | decision record | `## 10. Decision record` with `DR-CS-01..10`, all ten defined, none dangling |
| 5 | absence sweeps re-run (exact commands of §2) | `grep -rli "loan strata\|contact strata" corpus/knowledge/` → **19** ✓; `grep -lic loanword corpus/knowledge/verification/*.md` → **4** ✓; gates sweep → **0** ✓; `strata\|stratum` in verification → **8** ✓; `contact` in verification → **11** ✓; `examples/culture-d3/` loan/borrow → **3 hits** ✓ |
| 6 | digest pins | **7/7 MATCH live**: `verification-method-overview.md` `f52708d9…`, `language-contact.md` `52385e3d…`, `historical-linguistics.md` `019f28f0…`, `loanword-material-dating.md` `5b1d75ab…`, `contact-scenario-builder.md` `fcc71a53…`, `multi-culture-creole-workshop.md` `62acbaae…`, `internal-consistency-audit.md` `c3118517…` |
| 7 | staged digest | block0 + `\n` = 33 526 B, sha256 `3fa037ae9f95de74…` ✓ = the fragment's pin = the F1 transient's recorded digest (§5) |
| 8 | fabrication spot-checks (13 needles + 2 files) | `language-contact.md:45,:53,:81`; `historical-linguistics.md:143,:145`; `loanword-material-dating.md:22`; `contact-scenario-builder.md:63,:153,:184,:198`; `calibration-registry.md:71`; `lexicon-coverage-audit.md:116`; `myth-consistency-gate.md:104`; `verification-method-overview.md:114`; `internal-consistency-audit.md:114`; `examples/culture-d3/handoff.md:111`; `examples/culture-d3/components/07-evidence.json:46` — all read as claimed |
| 9 | cross-domain bleed | 0 candidates, 0 unnegated `canon`; canon boundary named ✓; `https?://` count 0 ✓ |
| 10 | fence/staging | 4-backtick entry fence (stager-regex hazard, R01-10) + a 3-backtick receipt block in the same fragment — a naive regex could stage the receipt; integrator stages the entry by hand or with a fence-run parser |
| — | `to-verify` census | 4 ✓ |

## 4. C04 — `append-only-record-verification.md`

**Verdict: PASS-with-named-defects** (two S3: partial decision-record id coverage; §Self-audit pins the pre-reword size, §6 F4/F5).

| # | check | observed result |
|---|---|---|
| 1a | head-block | `- topic` / `- gap filled` / `- sources` (block, 13 entries) / `- calibration` / `- couples` / `- source` / `- verified-at` / `- recheck` / `- scope` — 9 fields |
| 1b | five-field set | 5/5 present |
| 2 | source-pointer resolution | I-C12 5/5 resolve; I-C05: 8 unique paths, **0 unresolved**; 4 attached citations / 9 line numbers, **0 out-of-range**; `AGENTS.md:32-39` (bare-name class, outside I-C12's regex) verified by hand: lines `:32` close-what-you-open, `:36` could-not-recover, `:38` SHA-256 at close ✓ |
| 3 | couples resolution | 19 distinct tokens, **all resolve** (incl. `AGENTS.md`, `LOG.md`, `corpus/README.md`, `reports/**`, `tools/replay-frozen.py` — file exists ✓) |
| 4 | decision record | `## 8. Decision record` with **8 numbered rules** (adopted/rejected/open) — heading+body passes the runbook's family-3 executable bar; **id coverage partial**: only `DR-AR-08` is ever used (twice, §5 and §Known-limits), and it is not defined in §8 (F4) |
| 5 | absence sweeps re-run | `grep -rn "closing snapshot" corpus/knowledge/ \| wc -l` → **0** ✓; `could-not-recover` → **0** ✓; close-digest variants → **0** ✓; `append-only` → **12** files ✓ |
| 6 | digest pins | none claimed in-entry (by design — pins belong to the snapshot that closes a record); the fragment's `§Self-audit` pins the pre-reword staged size 24 277 B while the filed block is 24 296 B (F5); C06's whole-fragment pin `94348f96…` MATCHES live bytes ✓ — chain intact |
| 7 | fabrication spot-checks (17 needles) | `AGENTS.md:32,:36,:38`; `provenance-audit-ledger-format.md:140,:155`; `verification-independence-anti-circularity.md:61,:144`; `header-conformance-readings.md:22`; `two-reader-interop-agreement.md:50`; `reports/round-39/telemetry/dispatch-declared.json:25` (`"closing_snapshot": "open-at-seat-close: owed once validation.json lands"` ✓); `reports/round-20/readme/gaps.md:18,:54`; `hold-set-contract-in-brief.md:77`; `generated-artifact-lifecycle.md:81`; `finding-disposition-workflow.md:60`; `gate-frozen-run-standard.md:15`; `corpus/README.md:43,:52,:511,:518`; `reports/round-37/calib/recount-ledger.json:68,:81,:94,:107` = the four `"disposition": "could-not-reproduce"` lines ✓ |
| 8 | cross-domain bleed | 0 candidates, 0 unnegated `canon`; canon boundary named ✓ |
| 9 | fence/staging | one 3-backtick ```markdown fence ✓ |
| — | `to-verify` census | 6 ✓ |

## 5. The transient corpus write (F1) — evidence timeline

Recorded by the **original C05 seat** during the wave; re-verified where possible by this seat.
All times UTC; the only writes by this seat are its out path and `.scratch/c05c/`.

| time | observation |
|---|---|
| 12:27Z | `corpus/knowledge/verification/C03-draft.md` (untracked, 33 526 B, sha256[:16] `3fa037ae9f95de74`) present in the corpus partition — bytes = C03's entry block + one trailing newline |
| 12:28:40Z | routine index sweep read red: `rows 212 files 213`, `missing_from_index 1 ['verification/C03-draft.md']`, `header_drift {'verification': 21 vs 20}`, totals/footer findings, **rc=1**; `git status` → `?? corpus/knowledge/verification/C03-draft.md` |
| ~12:30:05Z | `cov/C03-entry-3.md` lands (fragment `b753f1b3…`, later revised to `d476c8dc…`) |
| ~12:32:49Z | stray file gone; sweep re-run green (212/212, missing 0, verification 20, rc=0) |
| **this audit, 13:15Z** | **hash proof reproduces**: sha256(block0 ‖ `\n`) = `3fa037ae9f95de7449f4df937ed2ef0871bd85d75194c15f79c76053df3c841f`; file absent; `git status` → `?? reports/round-39/` only; sweep green (212/212, footer ok, rc=0) |

Reading: a seat wrote corpus bytes directly, violating `reports/round-39/targets.json`
`shared_rules[1]` (corpus changes are drafted as fenced blocks, integrator-applied); every index
surface read red for ~5 minutes mid-wave. The entry bytes themselves were never at risk. The stray's
bytes equal C03's entry bytes + newline (hash proof), so this is a **process** breach, not a content
defect. **Attribution is not determinable at completion time** (the file is removed and
`reports/round-39/` is untracked); C03's own sandbox receipt (`cov/C03-entry-3.md:224-251`) prints
the *sandbox-relative* path `corpus/knowledge/verification/C03-draft.md` for a file that lived under
`.scratch/c03/audit-root/` — a readability hazard, not evidence of authorship (F7). Owner:
**integrator** — record/close the transient; the at-close sweep is green.

**R01-14 reconciliation (carried):** R01 measured an unreproducible +2 inflation on five sweep
counts in one intermediate pass. The F1 transient explains **at most +1 per term** (one extra file);
the second +1 has no durable artifact. Filed against no seat (R01-14), and this seat could not
reproduce any extra-file state — recorded as `to-verify`, owner integrator.

## 6. Defects, severity-ranked

Tiers: **S1** blocker (structural contract), **S2** major, **S3** review/precision. **No S1.**

| # | sev | defect | evidence | owner |
|---|---|---|---|---|
| **F1** | **S2 (process; transient, closed on tree)** | a seat wrote corpus bytes directly (`corpus/knowledge/verification/C03-draft.md`, ~12:27–12:32Z), turning the index sweep red mid-wave; removed; tree clean at close | §5 timeline + reproducible hash proof | integrator (record/close) |
| **F2** | **S3** | **C01's "24/24 in-repo couples targets resolve" is not reproducible.** Measured: 19 backticked in-repo path tokens (+ plain-text `AGENTS.md`), all resolving; 20 backticked spans on the couples line (19 paths + `` `(to-verify)` ``); no counting of the couples field yields 24. The substantive leg (nothing dangling) holds. Fix: state the measured count or attach the script output. | §1 row 3; commands run 2026-10-19 at `dfb0719` | C01 / integrator (named-defects-allowed threshold) |
| **F3** | **S3** | **C02's `ghost` count carries an unnamed reading, and its descriptor is imprecise.** (a) `ghost` → **13** only case-sensitively (`-rli` 15, `-rlw` 9, `-rlwi` 11); the command is not quoted. (b) "13 folklore files" — the 13 files span four partitions (5 myth-symbol, 4 civilizations, 2 culture-material, 2 linguistics); the hits are ghost/ancestor folklore *mentions*, not folklore files. Same class as r35 `C13-audit-1-5.md` F1 and r36 `C01-audit.md` F2. | §2 row 5; the four commands run 2026-10-19 | C02 / integrator |
| **F4** | **S3** | **C04's decision-record id coverage is partial.** §8 carries 8 numbered rules (7 adopted/rejected + 1 open) but no `DR-AR-NN` ids; `DR-AR-08` is used twice in the body and is not defined in §8. P01 §1.3 phrases the contract as "a `## N. Decision record` section with `DR-<INIT>-NN` ids"; the executable bar (runbook family 3: heading + body, or a DR id) **passes**. Fix: id the eight rules, or state that §8 is the decision record without ids. | §4 row 4 | C04 / integrator |
| **F5** | **S3** | **C04's fragment `§Self-audit` pins the pre-reword staged size** (24 277 B) while the filed block is 24 296 B (24 297 B staged); the final bytes were audited `PASS/clean` but their size/digest is not carried in the fragment. Chain intact via C06's whole-fragment pin `94348f96…` = live. (Folds R01-9.) | §4 row 6; `cov/C04-entry-4.md` §Self-audit | C04 / integrator |
| **F6** | **S3 (instrument, carried + corrected)** | the carried I-C05 resolver binds a detached `` `:n` `` to the **last path on the line**, not the nearest preceding path as its docstring states (its selftest fixture passes only because the ref trails the last path). This seat re-ran a corrected nearest-preceding binder: 137 refs, **0 out-of-range** — no masked defect; the affected entry case (C03 `E19`/`E165`: `handoff.md` `` `:111` `` then `07-evidence.json` `` `:46` ``) hand-verified (handoff.md 286 lines, 07-evidence.json 134 lines, both refs in range). Also: the prior draft's "`-w` gives 11" is `-rlwi` 11 (`-rlw` is 9). | §0; `.scratch/c05c/` scripts | this seat (carried; corrected) |
| **F7** | **S3-note** | C03's receipt JSON prints the sandbox-relative path `corpus/knowledge/verification/C03-draft.md` (real location `.scratch/c03/audit-root/…`); the prose above it states the sandbox root, so it is a readability hazard, not a false claim. Related to F1's attribution ambiguity. | `cov/C03-entry-3.md:224-251` | C03 (one-clause clarity at landing) |

Carried notes (R01 folds, verified here): **R01-8** — C02's fragment self-audit says it "replicated
round-19 entry-audit regexes (`entry-audit.py:25-31`)" yet reports `header_fields: ['Boundary', …]`;
the filed `HEADER_RE` is `^- (topic|sources|couples|source|verified-at|recheck|status|gap):` (lowercase
fixed alternatives, verified at `reports/round-19/audit/entry-audit.py:25`), which cannot match the
staged entry's `- Boundary:` body bullet at line 28 — the inline replication was a looser variant; the
fragment itself flags `Boundary` as an over-match artifact, and its conclusions are unaffected.
**R01-10** — fence-shape heterogeneity (4-backtick C01/C03 vs ```markdown C02/C04): the r35 stager
regex silently skips C01/C03; the integrator must stage both shapes. **R01-11** — C01's missing
head-block `- calibration:` (executable bar unaffected). **R01-12/13** — K01's term counts are
verification-partition-scoped (re-measured here: loanword 4, euphemism 4, dialect 6, taboo 10,
"translation note" 0 — R01-12's numbers confirmed); K01's G2–G4 remain unclaimed gaps after this
round. **R01-14** — see §5.

## 7. Relation to R01 and to the superseded prior draft

- **R01 reproductions — agreed, cited:** R01 §2.1 (C01 sweeps exact; timekeeping digest
  `9805c0b854334ed3`; §10 demonstration line claims; literature `(to-verify)` shape) — reproduced
  here; R01 §2.2 (C02 staged digest `eabb1d63…` byte-exact; r28 instrument sha/selftest; README
  anchors; r27→r28 leg story) — reproduced; R01 §2.3 (C03 7/7 pins; five sweep counts; staged
  digest; cited lines) — reproduced; R01 §2.4 (C04 sweeps 0/0/0/12; anchors; ledger rows) —
  reproduced; R01 §2.5 (no slug collisions; fence heterogeneity) — reproduced. **Re-run where this
  seat disagreed:** R01's C01 couples reading ("12 distinct .md tokens") — measured here as 19
  backticked path tokens + plain-text `AGENTS.md`, all resolving; neither 12 nor 24 reproduces as a
  count of the couples field (F2).
- **R01-4 closure:** R01 recorded `cov/C05-audit.md` absent at its close and required the audit (or
  a recorded absence with owner+reason) before applying any entry. This file is that audit; its
  readings are §1–§4, and it must be read as C05's filed instrument run, not as R01's hunt.
- **Superseded prior draft:** a prior C05 draft (`91a4b4165fe4a96a…`, landed ~12:39Z, after R01's
  last poll) carried the same audit shape. This completion file re-measured every claim: the §1
  digests, §2 tables, §5 timeline and F1/F4 content are confirmed; two of its details are corrected
  — its C01 couples count ("12 distinct") and its `-w` ghost variant (11, which is `-rlwi`). Its
  instrument (`.scratch/c05/c05-audit.py`) is carried and its binding defect filed (F6).

## 8. Limits

- **Structural, not scholarly; a pass is not admission.** Nothing here judges whether the four
  topics are the right four, whether the scholarship is sound, or whether the entries should be
  promoted (`PROVINCE.md`; `corpus/QUALITY.md`).
- **No network.** Literature legs are carried `(to-verify)` (census §1–§4); this audit verified the
  flags' presence and form, fetched nothing.
- **One auditor.** Where the round wants a second independent read of the entries, that is another
  seat's leg. The F1 timeline is carried from the original seat's record and is not re-observable
  (the file was removed); its hash proof is reproducible and reproduced.
- **Freeze:** the audited digests are §0's. Any post-audit byte change to a fragment voids the
  corresponding reading and owes a re-run.

## Owed

- **F1's record** — the integrator records/closes the transient (or accepts §5 as the record) and
  keeps the at-close sweep green; C06's post-apply sweep is claim C's own reading.
- **F2/F3/F4/F5/F7 one-clause fixes** — owners C01/C02/C04/C03 respectively; integrator decides
  apply-as-is with named defects (claim C's threshold allows named defects) or pre-landing repairs.
- **Staging** — handle both fence shapes (4-backtick C01/C03); do not let a stager regex pick C03's
  receipt block.
- **`reports/round-39/run-validation.py`** — claim C's counting command (`reports/round-39/claims.json:23`);
  absent at filing (as every prior round's was until the integrator authored it), and per
  `shared_rules[4]` never executed in-tree by a seat.
- **K01's G2–G4** (taboo-euphemism, dialect-register, translation-fidelity) remain unclaimed gaps —
  X00/integrator records them as still-open; not this round's call.

## Citations

- `reports/round-39/targets.json` — `seats[id=C05].mission`; `shared_rules[0-4]`.
- `reports/round-39/claims.json:13-24` — claim C (thresholds "audit clean (named defects allowed);
  sweep green"; counting commands incl. the sweep).
- Audited drafts (§0 digests): `reports/round-39/cov/C01-entry-1.md`, `C02-entry-2.md`,
  `C03-entry-3.md`, `C04-entry-4.md`; staged copies under `.scratch/c05c/stage/`.
- Instruments: `reports/round-35/cov/C12-audit-runbook.md` §5 (digest `97361027…562d`, 663 lines);
  `.scratch/c05/c05-audit.py` (carried, sha `4326bb85…`); `reports/round-28/readme/sweep.py`
  (sha `9b2ccac0…`, 17 117 B; run read-only twice, selftest 12/12, live green).
- Contract: `reports/round-39/plan/P01-plan.md` §1.3; `reports/round-10/run-validation.py:81,362-370`;
  `reports/round-19/audit/entry-audit.py:25-27,106-133`.
- R01: `reports/round-39/review/R01-review.md` §2.1–2.5 (reproductions), R01-4, R01-8, R01-9,
  R01-10, R01-11, R01-12, R01-13, R01-14; prior-draft predecessor §5 timeline for F1.
- Cited corpus lines verified by needle (all quoted in §1–§4): `verification-method-overview.md:54,
  114,161,206`; `internal-consistency-audit.md:114,168`; `label-channel-routing-verification.md:82`;
  `gate-frozen-run-standard.md:15,144`; `verification-independence-anti-circularity.md:3,61,144`;
  `worked-example-mini-culture.md:2`; `historical-linguistics.md:55,143,145`;
  `timekeeping-instruments.md:111,112,134` (+ sha16 `9805c0b854334ed3`); `language-contact.md:45,53,81`;
  `loanword-material-dating.md:22`; `contact-scenario-builder.md:63,153,184,198`;
  `calibration-registry.md:71`; `lexicon-coverage-audit.md:116`; `myth-consistency-gate.md:104`;
  `provenance-audit-ledger-format.md:140,155`; `header-conformance-readings.md:22`;
  `two-reader-interop-agreement.md:13,50`; `pre-declared-hold-set-reconciliation.md:3,39`;
  `register-strata-attestation.md:31`; `AGENTS.md:32,36,38`; `corpus/README.md:11,43,52,97,505,510,511,518`;
  `examples/culture-d3/handoff.md:111`; `examples/culture-d3/components/07-evidence.json:46`;
  `reports/round-37/calib/recount-ledger.json:68,81,94,107`;
  `reports/round-39/telemetry/dispatch-declared.json:25`; `reports/round-20/readme/gaps.md:18,54`.
- Commands run (2026-10-19, lane root, `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`):
  `git rev-parse HEAD`; `git status --porcelain` (×3); C12 instrument install + sha256 + selftest;
  I-C05 selftest; fence extraction ×4 (+ C02 stager-regex and C03 block0+`\n` digest proofs);
  I-C12 over the staged set ×2; I-C05 over the staged set ×2; corrected-binding re-check (137 refs);
  `reports/round-28/readme/sweep.py` ×2 (selftest + live); every quoted sweep re-run verbatim
  (C01 8 commands, C02 3 + 4 variants, C03 6, C04 4); 65 needle reads; 4 sha256 batteries (C03 ×7,
  C01 ×1, C02 ×3, fragments ×4); README duplicate-row parse; K01 term re-count (5); to-verify
  census; ghost distribution. **Not run, deliberately**: any `reports/round-*/run-validation.py`;
  any network call; no write outside this fragment and `.scratch/c05c/`.
