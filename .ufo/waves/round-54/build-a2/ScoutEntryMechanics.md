# ScoutEntryMechanics — records and index mechanics for claim C (round 54, attempt 2)

- Seat: KotodamaR54a2.ScoutEntryMechanics (leaf; no delegation, no background jobs).
- Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, branch main, claim base `260c68d58c5d3c2b9a6463ca5c667b7e0fff5987` (worktree HEAD `260c68d` at every reading below).
- Read-only. Nothing in the lane was edited, staged or committed; no clone was made; `reports/round-49/run-validation.py` was not run. All commands are lane tools or plain reads; the one script written lives under `/fast/scratch/hyaku/kotodama-r54-a2/ScoutEntryMechanics/`.
- Axes judged: contract fidelity (C), index arithmetic (C), frontier and registry mechanics (C), acceptance-instrument fidelity (C).

## 0. Result

1. **Head contract is the r48/r49 eight-field head, and the live round-53 entry is the right model.** Exact key order `topic, gap filled, sources, couples, source, verified-at, recheck, scope`, each key at column 0 in the block before the first `## `; H1 line 1, blank line 2, keys from line 3, first H2 line 14 in the model.
2. **README work is five edits at exact lines** (312 header, insert before 330, 625 totals, 629 footer vector, new `revision: 2.11` block at line 3); the round-53 commit `47ec825` shows exactly this shape and no "Index rows re-measured" append.
3. **SOURCES rows append after the S238 row (line 267), before `## Paths` (line 269)**, 11 columns, no literal `|` inside cells; the seven census commands are clean at base and must stay clean.
4. **Decision-record prefix `DR-MSK` is unused** (0 word-bounded hits in `corpus` and `reports`; the near-string `DR-MS` belongs to `myth-symbol/mineral-stone-symbolism.md`).
5. **Two traps that would fail `accept-c.py` while looking correct**: (a) any S-id range notation anywhere in the entry, including the head — the gesture entry's own `rows S187–S238` style fails the RANGE leg; (b) the entry must not cite `corpus/lessons/round-54.md`.
6. **One live records defect found**: `SHONEN.md:6` carries the stale census tally `194 mined, 35 queued, 9 rejected`; the live census is `mined=194, queued=34, rejected=10` (the prerequisite's two status flips). `SHONEN.md` is a REC land, not a C land.

## 1. Entry contract (claim C entry)

### 1.1 Head: eight fields, exact order, before the first `## `

Models re-read this session: `corpus/knowledge/linguistics/gesture-co-speech-pointing.md` (round-53 landing, 223 lines, 14 H2, 0 H3 — the closest model in generation and date) and `corpus/knowledge/culture-material/ritual-garments.md` (head model only: 10 H2 and 3 H3, so **not** a heading precedent — round-50 contract §2.2 says so explicitly).

Observed positions in `gesture-co-speech-pointing.md`:

| line | content |
|---|---|
| 1 | `# Gesture in speech — co-speech gesture, pointing and quotable gestures …` (single H1, em dash U+2014 with one space each side) |
| 2 | blank |
| 3 | `- topic: …` |
| 4 | `- gap filled: …` |
| 5 | `- sources:` (nested `  - In-corpus anchors …` and `  - External shelf …` lines) |
| 8 | `- couples: …` |
| 9 | `- source: …` |
| 10 | `- verified-at: …` |
| 11 | `- recheck: …` |
| 12 | `- scope: …` |
| 13 | blank |
| 14 | `## 1. The register property: gesture is part of the utterance` |

Canonical key order, exact (`ReviewEntryContract.md` §2.3; checker §2.9-A `CANON`): `topic, gap filled, sources, couples, source, verified-at, recheck, scope`. The checker requires `keys != CANON` → FAIL, exactly one `- topic:` line, exactly one `- couples:` line. `ritual-garments.md` has the same 8 keys but out of order (`topic` 3, `sources` 5, `couples` 14, `recheck` 16) — do not copy its key spacing.

### 1.2 Heading and body rules (checker-enforced, §2.9-A)

- Length ≤ 250 lines (`wc -l`); the round-53 model is 223.
- Exactly one `# ` line, at line 1, containing ` — ` (em dash). Zero `###` or deeper lines. Every `## ` numbered `1. … N.` consecutively.
- Last H2 contains `Scope` (checker); a `Recheck` H2 exists (checker) and immediately precedes Scope (round-50 contract §2.2 prose, not a checker test); a `Calibration` H2 exists (checker); a line starting `**NON-CANON` exists (checker); at least one pipe-table separator row `|---|` exists (checker).
- Every `§N` reference ≤ the highest H2 number.
- Forbidden words: TODO, TBD, placeholder, scaffold, MVP (case-insensitive).
- Couples must be partition-labelled: `^- couples: (linguistics|myth-symbol|culture-material|civilizations|verification|synthesis) — `; every `*.md` token in the value must resolve (cross-partition as `../<partition>/<file>.md`, same directory as bare basename). The round-53 model is the style to follow; `ritual-garments.md`'s `myth-symbol/ritual-liminality (…)` style is the older one.
- `- sources:` is gate-checked (`tools/gates/provenance-audit.py:75-76`); `- topic:` text must be byte-equal to the README row topic (see §2).

### 1.3 Calibration codes (verbatim, `corpus/knowledge/verification/calibration-registry.md:35-39`)

| Code | Calibration status | Permitted use / stop rule |
|---|---|---|
| R | Rejected/discredited as the specified general inference | Do not use as evidence; may portray the theory as a dated ideology or choose a fictional premise explicitly |
| C | Contested empirical or historical interpretation | Preserve alternatives, scope, and discriminating evidence; do not report one reading as settled |
| B | Bounded, usable within a named domain | Carry population, genre, period, task, and exceptions; no extrapolation by resemblance |
| H | Heuristic or interpretive framework, not an established causal law | Generate with it; label the designer's choices instead of presenting a discovery |
| T | Unresolved provenance or claim check | Mark `(to-verify)` inline at the exact dependency; do not make it load-bearing |

The calibration bank is a `| Claim | Status | What to say instead |` table using these letters (round-50 contract §3: the models use R/C/B/H/T, not QUALITY's "mainstream/contested/discredited" words), followed by bold **Living-practice flag** and **Precision traps** paragraphs (both models have them).

### 1.4 Decision-record prefix

`DR-MSK` is free. Evidence: `grep -rnw 'DR-MSK' corpus reports` → 0; `grep -rn 'DR-MSK-' corpus reports` → 0. The string appears in this session only inside the round-54 wave spec JSON files under `.ufo/waves/round-54/` (the task text itself), never in `corpus/` or `reports/`. Prefixes in use across `corpus/knowledge` (counted, distinct files): DR-AG, DR-AR, DR-BB, DR-BS, DR-CM, DR-CS, DR-DC, DR-DE, DR-DIV, DR-FF, DR-FUR, DR-GES, DR-HF, DR-IS, DR-MMC, **DR-MS** (10, all in `myth-symbol/mineral-stone-symbolism.md:61,157,158`), DR-PP, DR-SGN, DR-SRG, DR-ST, DR-TF, DR-TK, DR-TR, DR-TS, DR-WE. `DR-MS` and `DR-MSK` are different strings; no collision. Table shape `| ID | Decision | Trigger | Failure if skipped |`, ids `DR-MSK-01…`.

## 2. README mechanics (`corpus/README.md`, 656 lines, sha256 `9c2d10d1…`)

### 2.1 The five edits, exact

| # | line at base | base text | change |
|---|---|---|---|
| 1 | 3 | `revision: 2.10 — Round-53 linguistics landing (2026-10-22): one linguistics entry` | insert a new `revision: 2.11 — Round-54 culture-material landing (2026-10-22): …` block **above** line 3 (label line plus continuation lines, then one blank line) |
| 2 | 312 | `## culture-material/ (28)` | `## culture-material/ (29)` |
| 3 | insert before 330 | line 329 is `- \`hunting-foraging-subsistence.md\` — …`, line 330 is `- \`material-culture-inference-method.md\` — …` | new single-line row `- \`masks-masquerade.md\` — <topic>` between them |
| 4 | 625 | `Total knowledge entries: 229.` | `Total knowledge entries: 230.` |
| 5 | 629 | `(total 229 files; directory totals 28/26/28/29/24/94).` | `(total 230 files; directory totals 28/26/29/29/24/94).` |

- **Insertion point is fixed by ASCII filename order**: `hunting-foraging-subsistence.md` < `masks-masquerade.md` < `material-culture-inference-method.md` (`mas` < `mat`). The section at base runs strictly in filename order (28 rows, lines 314–341). The sweep does **not** assert order (`sweep.py` checks missing/ghost/duplicate/topic/header-drift/footer only), so order is convention — but the round-53 revision text records it ("its row added in filename order between X and Y"), so keep it.
- **The row must be one line** (`ROW_RE = ^- \`([^\`]+\.md)\` — (.*)$`, no DOTALL) and its topic text must equal `topic_of(entry)` = the entry's `- topic:` head text with continuation lines space-joined (`sweep.py:74-82`). Neighbour row lengths at base: 1175 and 940 characters.
- **Footer vector order is** `[linguistics, myth-symbol, culture-material, synthesis, verification, civilizations]` (sweep `footer_live.order`, printed at base). Culture-material moves 28 → 29, so the vector becomes `28/26/29/29/24/94`. The date line (`Counts checked 2026-10-22 from the repo root:`) and the command line stay unchanged; the tool that produces it is `python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge`.
- **Revision block rules** (`tools/check-readme-revisions.py:99-148`): labels matched by `^revision: <label>`; labels unique; the line after a label must not be blank (`REVISION_STUB`); labels non-increasing top-to-bottom over numeric keys. New label `2.11` above `2.10` satisfies all three.
- **No "Index rows re-measured" append** is needed: the last such paragraph is dated 2026-10-19 (round 35, README:650-656), and the round-53 landing (`git show 47ec825 -- corpus/README.md`) touched only these four hunks — revision block, section header, row, totals line plus footer.

### 2.2 Checker outputs at base (run this session, read-only, exit codes as printed)

```
$ python3 -B tools/check-readme-revisions.py
readme /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/README.md
sha256 9c2d10d15b73d2c4c562f24939b0a3d08ca9504ff3344c09efd73eceb139e7ec
revision_lines [3, 13, 24, 35, 46, 67, 79, 91, 101, 110, 119, 146, 166, 178, 198, 224, 234]
labels ["2.10", "2.9", "2.8", "2.7", "2.6", "2.5", "2.4", "2.3", "2.2", "2.1", "2.0", "1.8", "1.7", "1.6", "1.5", "1.4", "1.3"]
findings 0
warnings 1
  REVISION-ORPHAN lines=[133, 144] unheaded paragraph inside revisions span (starts 'round-28 C entry landed (`linguistics/register-lexicon-ceili')
exit=0
$ python3 -B tools/check-readme-heading.py
readme /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/README.md
sha256 9c2d10d15b73d2c4c562f24939b0a3d08ca9504ff3344c09efd73eceb139e7ec
h1_lines [1]
headings {"1": 1, "2": 7}
findings 0
exit=0
```

Both must stay exit 0 after the landing; the one warning is pre-existing and is not a finding.

### 2.3 Sweep at base (the SWEEP leg's oracle)

```
$ python3 -B reports/round-28/readme/sweep.py
parts {"civilizations": 94, "culture-material": 28, "linguistics": 28, "myth-symbol": 26, "synthesis": 29, "verification": 24}
rows 229 files 229
missing_from_index 0 []
topic_mismatch 0 []
orphan_rows 0 []
header_drift {}
totals_line 229 totals_ok True
footer {"date": "2026-10-22", "command": "python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge", "total": 229, "dir_totals": [28, 26, 28, 29, 24, 94]}
footer_live {"total": 229, "dir_totals": [28, 26, 28, 29, 24, 94], "order": ["linguistics", "myth-symbol", "culture-material", "synthesis", "verification", "civilizations"]}
footer_findings [] footer_ok True
readme_sha256 9c2d10d15b73d2c4c562f24939b0a3d08ca9504ff3344c09efd73eceb139e7ec
exit=0
```

## 3. SOURCES mechanics (`corpus/SOURCES.md`)

### 3.1 Row format and append point

- Header row at **line 28**, exactly: `| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |`; separator at line 29. Eleven cells; a row line must split into exactly 13 `|`-separated fields (the census requires `NF==13`, so **no literal `|` inside any cell** — at base 0 malformed rows).
- Append point: the last registry row is **S238 at line 267**; insert new rows after it, before the blank line 268 and `## Paths` (line 269). Registry section spans lines 26–267 (`## Registry` at 26).
- Cell conventions as filed by round 53 (rows S187–S238 are the immediate precedent):
  - `source` = author, year, title, venue, stable id, then the URL actually read, with the route/status note in parentheses where relevant (for example S238: `… (HTTP 200, PMC open access, CC BY-NC 4.0, full text)`; S228: `(a plain curl request met an Anubis proof-of-work challenge, which was not passed; the quotes were checked against Wayback capture 20221018012522)`).
  - `kind` enum enforced by the census: `spec|docs|paper|code|tool|dataset|talk|book|community|own-work` (the round-50 contract lists only the seven kinds observed then; the census enum is authoritative).
  - `tier` ∈ {A, B, C}; tier A with kind `community` is flagged `tier-inflation`.
  - `status` ∈ {queued, mined, rejected}; **every row the entry cites must be `mined`** (accept-c STATUS leg).
  - `opened` = `2026-10-22`; `recheck` ∈ {90d, 180d, 365d, on-release} (round-50 contract §2.6); `used-by` = repo-relative entry path, comma- or semicolon-separated when several (`corpus/knowledge/culture-material/masks-masquerade.md`).
  - Append-only rule (`SOURCES.md:8-11`): only `status`, `recheck` and `used-by` change in place, each change logged old→new in a round lesson; a correction is a new row whose `teaches` opens `supersedes S0NN —`.
- No search-log paragraph was added to `SOURCES.md` for S187–S238; round 53 put its search-log paragraph in the **lesson** instead (`corpus/lessons/round-53.md`, `## Search log`). The registry's own search-log entries stop at rows S071–S124.

### 3.2 The seven census commands, run at base (read-only, this session)

Verbatim from `reports/round-49/run-validation.py:56-62`, run from the lane root:

```
rows:                238
malformed (NF!=13):  0
tiers:               A=138 B=92 C=8
statuses:            mined=194 queued=34 rejected=10
duplicate ids:       (none)
enum violations:     (none)
missing used-by:     (none)
```

Do **not** run `python3 reports/round-49/run-validation.py` in-tree (it rewrites its own filed receipts); run the seven commands directly or in a sandbox clone. After appending rows, these must stay clean (rows 238 → 238+N, mined 194 → 194+N, everything else unchanged).

### 3.3 Gate lines: how round 53 wrote them (`corpus/lessons/round-53.md`)

Lesson head fields, lines 3–6: `source:`, `verified-at:`, `recheck:`, `scope:`. Gate line format, one line per opened source (several lines per S-id allowed, one per seat):

```
- S187 — https://pages.ucsd.edu/~jhaviland/Publications/jlin.1993.3.1.3.Anchoring.pdf — accessed 2026-10-22 — p. 12: "If one is talking about going to the beach and the beach is east, one points east." Grounds: Guugu Yimithirr pointing keeps true bearings, so an absolute frame decides where the hands go. Seat: ScribeSec05SpaceTime.
```

Observed shape: `- S0NN — <URL actually read> — accessed 2026-10-22 — <locator>: "<quote ≤25 words>". Grounds: <one line>. Seat: <SeatName>.` Section headings used: `## Gate`, `### Prerequisite rows (opened 2026-10-22 by the L1, before the declaration; commit …)`, `### Rows opened for claim C (S187–S238)` with a lead-in paragraph explaining the draft-id → S-id mapping and merged rows. Challenges are recorded in the row's `source` cell and in the Gate lead-in as "met and not passed" with the ordinary route named (S186 pattern). A status/`used-by` change log follows as its own section, `## Status and used-by change log` (round-53.md:186-189), with lines such as "S187–S238 (52 rows) enter `mined`, `used-by` `…` (claim C, `47ec825`)."

## 4. Acceptance instrument: `reports/round-54/accept-c.py` (facts and traps)

Legs, in print order, from `accept-c.py:44-110`:

| leg | mechanical test |
|---|---|
| SET | every file under `corpus/knowledge` (any extension) is one of the 229 paths in `reports/round-54/base-knowledge-files.txt` or the entry; `len(live) == 230`, `added == [ENTRY]`, `removed == []` |
| SWEEP | `python3 -B reports/round-28/readme/sweep.py` run on its own: exit 0 and lines `rows 230 files 230` and `missing_from_index 0` |
| FLOOR | `len(set(re.findall(r"\bS\d{3}\b", entry))) >= 20` |
| RANGE | every cited id ≥ S239, exactly one `corpus/SOURCES.md` row, row splits into ≥13 fields, and **no range notation** anywhere: `\bS\d{3}\s*(?:[–—-]|to)\s*S?\d{3}\b` |
| STATUS | every cited row's status cell (`table[s][8]`) is exactly `mined` |
| USEDBY | every cited row's `used-by` cell (`table[s][11]`) contains `corpus/knowledge/culture-material/masks-masquerade.md` (substring test) |
| ACCESS | `python3 -B tools/check-source-access.py` exits 0 |

**Traps, with tested evidence:**

- **Range notation (RANGE).** The regex fires on `S239–S255`, `S239-S255`, `S239 to S255` — and on the gesture entry's own head style `rows S187–S238`. It does **not** fire on `the rows S239 upward`, `S239 and above`, `S239+ and up`, `rows S239–S2nn`, `S239 through S258`, `this round's rows from S239 on`. The masks entry's `- sources:`, `- source:` and `- recheck:` lines must use one of the safe wordings (or list ids) rather than copying the round-53 range style.
- **Floor (FLOOR).** ≥20 distinct S-ids must be cited, so the entry itself has to carry the citations, not only the head block.
- **`must_not_cite` (`claims.json`).** The entry must not cite `corpus/lessons/round-54.md`.
- **SET counts non-`.md` files too.** Any stray file under `corpus/knowledge` fails it; at base all 229 are `.md`.
- **SWEEP reads the sweep's own exit code** (no pipe), so a missing or misnamed README row fails the leg.

Pre-landing live state at base (this session; identical to the filed dry-run receipt `reports/round-54/telemetry/declaration-dry-run.txt`):

```
$ python3 -B reports/round-54/accept-c.py
SET FAIL count=229 required=230 added=[] removed=[]
SWEEP FAIL exit=0 rows 229 files 229 missing_from_index 0 []
FLOOR FAIL cited=0 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
exit=1
```

Also at base: `python3 -B reports/round-54/claims-agree.py` → `AGREE claims=['C']`, exit 0. `python3 -B tools/check-claim-separability.py reports/round-54/separability-manifest.json` → `SEPARABILITY_INPUT_ERROR unit C lands 'corpus/knowledge/culture-material/masks-masquerade.md', which is absent from the worktree …`, exit 2 — expected before landing (the checker stops at its first absent land). C's lands are the entry, `corpus/README.md` and `corpus/SOURCES.md`; C's export regex is `\bS(239|2[4-9][0-9]|[3-9][0-9][0-9])\b`, i.e. S239 upward only.

**ACCESS baseline:** `python3 -B tools/check-source-access.py` → `ACCESS: 2 flagged rows, 0 findings`, exit 0. The two flagged rows are the pre-existing **S094 and S132** (the Battison pair), both `rejected` and uncited, so no findings. New rows must not add bypass marker words to their `source`, `anchor` or `teaches` cells: the checker flags `headless`, `bypass(ed|ing)`, `solved a/the (bot )?(captcha|challenge)`, `got past/around/through <paywall|login|captcha|turnstile|geo-block|cloudflare/waf/browser challenge|access control>`, `playwright|puppeteer|selenium|chromedriver|cloudscraper|curl-impersonate`, `vpns`, `logged-in`, `subscription/paid/member account`, `session cookies`, `spoofed user-agent/ip`. The safe phrasing is the round-53 one: "the challenge was met and not passed", with the ordinary route (Wayback capture id) named.

## 5. Findings for the L1

- **F1 (records defect, REC land).** `SHONEN.md:6` asserts "238 rows after round 53 — 194 mined, 35 queued, 9 rejected — census exit 0 in `reports/round-53/telemetry/final-measures.txt`". The live census reads `mined=194 queued=34 rejected=10` (rejected ids: S028, S029, S030, S043, S047, S094, S132, S145, S178, S233). The delta is exactly the prerequisite's two flips (S145 mined→rejected, S185 queued→mined). The line needs the corrected tally and, after this round's rows land, the new count and the round-54 receipt pointer.
- **F2 (README).** The index row must be a single line whose topic text is byte-equal to the entry's `- topic:` text (continuations space-joined) — the sweep's `topic_mismatch` leg is the oracle.
- **F3 (entry).** No range notation anywhere in the entry, head fields included; the round-53 model's `rows S187–S238` wording is a trap here (§4).
- **F4 (entry).** Cite only `mined` rows with `used-by` naming the entry, ≥20 distinct ids, all ≥ S239.
- **F5 (expectation setting).** `accept-c.py` cannot pass before landing (SET, SWEEP, FLOOR fail by construction) and the separability check exits 2 until the entry exists; both are recorded as expected in the dry-run receipt.

## 6. Unrun checks and limits

- No entry, README edit, SOURCES row, lesson, clone or receipt was created; no gate that writes git was run; the lane's bytes are as found.
- No external source was opened; nothing in §3.1 about how seats should record access was tested against a real fetch this session (it is read from the round-53 rows and the checker's own regex).
- Post-landing numbers (rows 230, `mined=194+N`, footer vector `28/26/29/29/24/94`, revision label 2.11) are derived from the instruments and the base readings, not measured after a landing.
- `reports/round-54/criterion11-controls.py` and its receipt were read only as claims text; the twelve RED controls were not replayed by this seat.

## 7. Tooling record

- No installs or upgrades. Only the system `python3`, existing lane tools in read mode, and plain reads. One helper script written to `/fast/scratch/hyaku/kotodama-r54-a2/ScoutEntryMechanics/census.sh` (the seven census commands, verbatim) and one heredoc probe of the RANGE regex; no lane file was written except this report.
