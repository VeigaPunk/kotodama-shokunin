# ReviewEntryContractC — claim C entry contract, round 51 attempt 3

- Seat: KotodamaR51a3.ReviewEntryContractC (leaf; no delegation, no background jobs).
- Lane: /home/vgpnk/Projects/shokunin/kotodama-shokunin. Read-only except this report.
- Basis: contract `.ufo/waves/round-50/build/ReviewEntryContract.md` §2; models `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md` (204 lines) and `culture-material/hunting-foraging-subsistence.md` (205 lines); claims `reports/round-51/claims.json` (base `bff83ba65bf9559af4d7567e81703059667a0005`). Corpus bytes equal base; every `path:line` below was re-read at the worktree this session (2026-10-22).
- Result: **no blocker to writing the entry.** Path free; DR-SGN unused in corpus and reports; README/SOURCES insertion points pinned; no linguistics entry uses the eight-field head, so the two culture-material models govern.

## 0. Partition census (read this session)

Head keys of all 25 `corpus/knowledge/linguistics/*.md` (census run this session): **0 of 25 use the exact eight-field canon order.**

| nearest precedents | head keys observed | lesson |
|---|---|---|
| `taboo-strata-lifecycle.md` (134), `sacred-registers-liturgical-language.md` (160), `dialect-register-consistency.md` (129) | 9 keys, extra `calibration:` inserted (after `sources:` / between `sources` and `couples` / after `sources`) | the extra `- calibration:` head key FAILS the §2.9-A checker (`head keys != CANON`); do not copy it |
| `register-lexicon-ceilings.md` (317), `register-strata-attestation.md` (436) | 7 keys, no `scope` | fail the head checker too |
| `translation-protocol-fidelity.md` (199) | 9 keys with `scope` before `source` | out of canon order |
| `sound-symbolism.md` (155) | 6 keys incl. singular `source` | not the canon order |

`historical-linguistics.md` is 252 lines and `phonetics-phonology.md` 325 — the 250-line cap is claim-scoped, not a partition norm. Copy the culture-material models for head and body shape; adapt content to the linguistics partition.

## 1. The checklist (apply in order)

### 1.1 Path and length

- File: `corpus/knowledge/linguistics/sign-languages-manual-modality.md`. `test ! -e` first — verified free this session. Never overwrite an existing entry.
- `wc -l` ≤ 250 (claim C; build brief repeats it).

### 1.2 Head: eight fields, exact order, column 0

Required key sequence, exact: `topic`, `gap filled`, `sources`, `couples`, `source`, `verified-at`, `recheck`, `scope` (models `pastoralism-animal-husbandry.md:3-12`, `hunting-foraging-subsistence.md:3+`; no other key, no `calibration:` key, each exactly once).

1. `- topic:` single line preferred (TOPIC_RE `sweep.py:61` runs to the next `- \w` line; `topic_of` `sweep.py:74-82` space-joins continuations). Must contain the register words as whole words so future freshness probes hit it: sign language(s), signing, deaf/Deaf, manual, homesign, fingerspelling, kinesic, gesture. No canonical trailing-period rule — the enforced rule is byte-equality with the README row (§1.8.3).
2. `- gap filled:` re-run both base sweeps at the worktree and print measured `→ **0**` results, dated 2026-10-22 at base `bff83ba`: `find corpus/knowledge -iname '*sign-lang*' -o -iname '*gestur*' -o -iname '*kinesic*' -o -iname '*nonverbal*' | wc -l` and `grep -rliP '^- topic:.*\b(gestur|sign language|kinesic|nonverbal|non-verbal|body language|proxemic)' corpus/knowledge | wc -l` (word-bounded; the un-bounded form false-positives — round-50 defect D2 pattern). Name the partial owners cited one-way in §2 with live anchors: `culture-material/adornment-body-codes.md` §7, `linguistics/syntax-typology.md:99`, `linguistics/numerals-and-measures.md:107`, plus any the scribes found.
3. `- sources:` (plural) — nested two-space bullets exactly as the models (`pastoralism-animal-husbandry.md:5-7`): in-corpus anchors `path:line` re-read at base on 2026-10-22; then `External shelf — opened this round (2026-10-22), registered in corpus/SOURCES.md rows S071–S0nn`, each with URL, tier scope and locator. The S-id range is L1-assigned placeholder text until integration (§1.8.2).
4. `- couples:` exactly one line, starting `linguistics — ` (partition label + em dash; checker regex accepts only the six partition labels). Same-directory siblings by bare basename (`syntax-typology.md`); cross-partition by `../<partition>/<file>.md` (`../culture-material/adornment-body-codes.md`). Ends with a period. Every `*.md` token must resolve (acceptance: basename-couples-resolver). Models end the line with a non-path `lore-shokunin (canon: …)` group — copy that pattern for the handoff.
5. `- source:` (singular) — required by the 8-field head (round-50 contract §3); names the anchor list and the S-ids with URL + locator; ends with one design-method sentence.
6. `- verified-at: 2026-10-22 —` written at base `bff83ba…`; pre-counts 226 total / 25 linguistics, post 227 / 26; `Measured with …` commands → **value**; must name checks actually run (no template date — DR-4 precedent).
7. `- recheck:` trigger first ("before any in-world sign system becomes load-bearing"); re-open every cited URL before quoting a number; re-read the live anchors.
8. `- scope:` reference method and lane policy for the linguistics partition; this entry owns sign languages and other manual communication systems as conlang/worldbuilding method; it does not own clinical audiology, deaf-education policy or rights/legal rulings (PROVINCE.md:9-11 owns the six partitions; PROVINCE.md:17-18,31 out-of-province → report, never absorb; build brief repeats "no clinical, education-policy or legal rulings").

### 1.3 Headings

- Line 1: `# <Title> — <subtitle>`, exactly one H1, em dash U+2014 with one space each side; line 2 blank.
- H2s `## 1. …` through `## 15. …`, consecutive, all numbered; zero `###`/`####`.
- Last H2 = `Scope`; `Recheck` immediately precedes it (14, then 15).
- Every `§N` reference ≤ 15.

### 1.4 Section plan and line budget (sums ≤ 250)

Budgets are the build brief's (`.ufo/waves/round-51/gen-build-spec.py:54-66`), counted per section including the H2 line and internal blank lines.

| block | budget |
|---|---|
| opening block (H1 + blank + 8 fields, `sources` = key + 2 nested bullets; models are 12 lines, `pastoralism-animal-husbandry.md:1-12`) | 12 |
| 1 register property (master claim, 4 load-bearing choices, `| Test | Pass when | Fails as (owner) |` gesture/manual-code/writing-system separation) | 16 |
| 2 one-owner boundary (lead sentence + `| Neighbour (anchor) | What it owns | This entry's boundary |`, 12–15 rows, one distinct neighbour each, backticked `file.md:N` anchor re-read and supporting the ownership cell) | 20 |
| 3 typology of manual systems (deaf-community / shared-village / emerging / alternate / homesign / manual codes / gesture boundary) | 18 |
| 4 community ecology and transmission | 15 |
| 5 sublexical structure (parameters) | 15 |
| 6 grammar in space | 15 |
| 7 iconicity and arbitrariness | 13 |
| 8 emergence, families, diachrony | 15 |
| 9 alternate sign languages | 15 |
| 10 contact, codes, writing | 15 |
| 11 decision table + build order + decision record | 24 |
| 12 NON-CANON worked micro-example | 8 |
| 13 calibration bank + Living-practice flag + Precision traps | 20 |
| 14 Recheck | 3 |
| 15 Scope (with `Handoff: lore-shokunin owns …`) | 3 |
| **total** | **227** |

Worst case with 14 inter-section separator blanks on top: 241 ≤ 250; slack 9. Keep §11 within 24 — it is the only section that can blow the cap.

### 1.5 Tables

- Every pipe table has a `|---|` separator row and a blank line before and after (checker regex `^\|[\s:\-|]+\|\s*$`).
- §11 decision table `| If your culture… | then the sign system needs… | and check |`, 5–7 rows; build order numbered, each step ending `*Artifact: …*`; decision record `| ID | Decision | Trigger | Failure if skipped |`, 4–6 rows.
- §13 `| Claim | Status | What to say instead |`, at least: one universal sign language (R); sign is pantomime/gesture (R); sign language = spoken language on the hands (R); sign languages lack grammar (R); shared-signing village idyll (C); critical period (C or B, carefully scoped); number of sign languages (B, with the counting source); Deaf-culture terminology. Then bold **Living-practice flag** and **Precision traps** paragraphs (both models carry them).

### 1.6 Calibration codes and sourcing

- Status codes are exactly `R`, `C`, `B`, `H`, `T` per `corpus/knowledge/verification/calibration-registry.md:35-39` (table verified: header `:33`, separator `:34`, R–T `:35-39`); cite that anchor in §13. Not QUALITY's mainstream/contested/discredited words.
- `(to-verify)` inline for any claim without an opened source (QUALITY.md:5-8); never load-bearing (code T stop rule).
- Tiers per QUALITY criterion 6 (QUALITY.md:29): publisher description/abstract = B for substantive claims about a work; A only primary/authoritative for the exact scope; community never A; C a lead, never sole support. Tier corrections via a superseding SOURCES row, never an in-place edit.
- Every factual claim cites `path:line`, an S-id, or carries `(to-verify)`.

### 1.7 Decision-record prefix

- IDs `DR-SGN-01` upward, consecutive. Prefix verified unused: `grep DR-SGN` over `corpus/` → 0 hits and over `reports/` → 0 hits (grep tool, this session; the only lane hits are the round-51 wave build files themselves, which are assignment text, not precedent).

### 1.8 C-land index edits (README + SOURCES) with exact current lines

**`corpus/README.md` (verified lines this session):**

1. Insert `revision: 2.8 — Round-51 linguistics landing (2026-10-22): …` directly above line 3 (`revision: 2.7 — Round-50 culture-material landing (2026-10-21): one`). Rules (`tools/check-readme-revisions.py`): label unique (REVISION-DUP `:125`); the label line must be followed by a non-blank body (REVISION-STUB `:138-140`); labels non-increasing top-to-bottom, so 2.8 above 2.7 is required (REVISION-ORDER `:151-154`); REVISION-GAP (skipped minor) is advisory `:457-460`, and 2.8 has no gap. Docstring states the three hard rules at `:20-31`.
2. Line 220 `## linguistics/ (25)` → `(26)` (SECTION_RE `sweep.py:59`; drift check `declared == len(files)`).
3. Insert the new row between line 239 (`- \`semantics-pragmatics.md\` — …`) and line 240 (`- \`sociolinguistics-registers.md\` — …`): `- \`sign-languages-manual-modality.md\` — <topic>` where `<topic>` is **byte-equal to `topic_of()` of the entry** (sweep.py:74-82 — the `- topic:` value, continuations space-joined). Row regex `^- \`file.md\` — text` (ROW_RE `sweep.py:60`). Alphabetical order is a convention, not sweep-enforced; 239/240 is the correct sorted position (se < si < so). The 25 current rows are lines 221–245.
4. Line 590: `Total knowledge entries: 226.` → `227.` (TOTALS_RE `sweep.py:62`; must equal the live file count).
5. Footer, lines 592–594: new live reading `Counts checked 2026-10-22 from the repo root:` / command line unchanged (`python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge`) / `(total 227 files; directory totals 26/26/28/29/24/94).` Directory order is section order (linguistics, myth-symbol, culture-material, synthesis, verification, civilizations; FOOTER_RE `sweep.py:66-69`, FOOTER_TOTAL `:173`, FOOTER_DIR_TOTALS `:184`). Preserve line 595 and the superseded-reading history from line 596 (move the outgoing 226/25/26/28/29/24/94 reading into the preserved record per the file's own convention; never delete earlier readings).
6. Optional (convention, not checked): append an `Index rows re-measured 2026-10-22 at HEAD …` paragraph at the end; last existing one is the round-35 paragraph at lines 617–621; no round-48/49/50 paragraph exists.
7. Do not change line 1 (the only H1), any other section header/row (`## myth-symbol/ (26)` :248, culture-material :277, synthesis :307, verification :339, civilizations :366), or Known gaps (:463+).

**`corpus/SOURCES.md`:**

- Append new rows immediately after the last row `S070` (line 99), before the blank at line 100 and `## Paths` at line 101. Column order exact: `| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |` (line 28).
- ids `S071` upward, assigned by the L1 at integration; `opened` = `2026-10-22`; `status` = `mined` once the entry cites the row; `recheck` ∈ 90d/180d/365d/on-release; `used-by` = `corpus/knowledge/linguistics/sign-languages-manual-modality.md` (repo-relative, as in S001–S070). Only URLs actually opened this round, each with a ≤25-word verbatim located quote; that quote and its Gate line live in the round lesson (L1/REC land), while the row itself is C's land.
- The entry's `- sources:`/`- source:` S-id placeholders (`S071–S0nn`) must be reconciled to the real ids at integration — the falsifier "any cited S-id missing from SOURCES or lacking the entry path in used-by" runs on final bytes.

### 1.9 Claim-wide constraints (C's landed bytes = entry + README added lines + SOURCES added rows)

- Must NOT contain the strings `corpus/lessons/round-51.md` or `reports/round-51/boundary-count.py` (claims.json C.must_not_cite). Separability (tools/check-claim-separability.py:32-38) flags C naming `reports/round-51/boundary-count.py` outright: it is D's land and absent at base. The lesson is REC's land (claim→record dependencies are permitted by the checker, docstring line "Records are never scanned as dependers") but the claim forbids it anyway. Referring to "the round lesson's ## Gate" without the path string is precedented (`pastoralism-animal-husbandry.md:9`) and safe.
- The same rule binds the new README `revision: 2.8` body text: it must not name `reports/round-51/boundary-count.py` (would read as a C→D dependency from README's added lines). Naming `pastoralism-animal-husbandry.md` in prose is separability-safe (the path exists at base, checker rule "a path that already resolves at base is not a dependency"), but the revision text has no need of it — keep it linguistics-only.
- C's own export regex `\bS(07[1-9]|0[89]\d|[1-9]\d\d)\b` must match no base line of C's lands: satisfied today (max base id S070, SOURCES.md:99). Corollary: D's bytes must not cite S071+ — that is D's seat's constraint, flagged here only as the shared boundary.
- If the entry cites the pastoralism entry (not required; it is not a §2 neighbour), prefer section references: D's landing grows its §2 table by 4 rows and shifts every later line number.
- Anchor discipline in §2: every `file.md:N` re-read at the worktree with the ownership cell actually supported by the anchored line(s) — the round-50-verifier-spotcheck routed defect pattern.

### 1.10 Forbidden content

No `TODO|TBD|placeholder|scaffold|MVP` (checker, case-insensitive); no emoji; no H3+; no canon decisions (handoff in Scope, QUALITY.md:18-20); respectful terminology per the build brief (deaf/Deaf community, signers, sign languages; never 'deaf-mute', 'dumb', 'hearing-impaired' as labels; no deficit framing); the NON-CANON paragraph begins `**NON-CANON.**` and states culture, place, signs and numbers are invented.

## 2. Acceptance (integrator clone; all read-only; never run-validation.py in-tree)

| check | command | expected |
|---|---|---|
| counts | `find corpus/knowledge -name '*.md' \| wc -l`; `ls corpus/knowledge/linguistics/*.md \| wc -l` | 227; 26 (base: 226 declared README.md:590; 25 counted this session) |
| length | `wc -l corpus/knowledge/linguistics/sign-languages-manual-modality.md` | ≤ 250 |
| sweep | `python3 -B reports/round-28/readme/sweep.py` | exit 0; render lines `rows 227 files 227`, `topic_mismatch 0 []`, `footer_ok True` (`sweep.py:230-231`). Bare command — it takes no positional args (round-50 defect D1) |
| heading | `python3 -B tools/check-readme-heading.py` | exit 0 |
| revisions | `python3 -B tools/check-readme-revisions.py` | exit 0; top label 2.8; pre-existing REVISION-ORPHAN warning is advisory |
| provenance | `python3 -B tools/gates/provenance-audit.py corpus/knowledge/linguistics/sign-languages-manual-modality.md` | exit 0, findings=0 |
| couples | `python3 -B tools/harness/basename-couples-resolver.py <entry>` | zero unresolved, zero ambiguous |
| S-ids | §3 Part B | empty list and ≥ 1 id cited (C's acceptance exits 1 on `not ids`) |
| separability | `python3 -B tools/check-claim-separability.py reports/round-51/separability-manifest.json` | exit 0 (declared required exit) |
| freshness | `python3 -B tools/harness/claims-freshness.py --claims reports/round-51/claims.json --root . --no-exec` | C clauses FRESH (git-bound; clone only) |

## 3. Mechanical checker (adapted from round-50 contract §2.9; run from lane root, in memory)

Part A — head order, headings, README topic equality: the round-50 §2.9-A script verbatim, with two substitutions:
`entry = pathlib.Path('corpus/knowledge/linguistics/sign-languages-manual-modality.md')` and
`row = re.search(r'^- \`sign-languages-manual-modality\.md\` — (.*)$', readme, re.M)`.
Expected `PASS` (it enforces: 250-line cap; single line-1 H1 with em dash; no H3+; head keys == CANON in order; one topic line; one couples line; H2s numbered 1..N; last H2 Scope; Recheck and Calibration present; NON-CANON paragraph; pipe-table separator; README topic byte-equal; partition-labelled couples; §N ≤ H2 count; no placeholder words).

Part B — S-id resolution and used-by (the same script with `REL = 'corpus/knowledge/linguistics/sign-languages-manual-modality.md'`); additionally assert `cited` is non-empty.

## 4. Unrun checks and limits

- I ran no gate (sweep/revisions/provenance/freshness/separability) — no landing tree exists yet; every expected output above is derived from the checked source, not executed post-landing. The two base sweeps in §1.2.2 were not re-run by this seat (the scribe brief requires the entry author to re-run them; claims.json gap_evidence_at_base records 0/0 at base).
- No external source opened; no registry row drafted (S-ids are L1-assigned).
- 226 total files taken from README.md:590 declaration and claims.json `before`, not re-counted; the 25 linguistics files were counted directly.
- No entry, README, SOURCES, lesson or clone byte was written; only this report.

## 5. Tooling record

No installs or updates. Read-only commands only: lane `python3` census one-liner over `corpus/knowledge/linguistics/*.md` (head keys + line counts) and the `test ! -e` path probe; all other evidence from `read`/`grep` tools at the worktree.
