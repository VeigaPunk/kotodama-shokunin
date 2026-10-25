# RevEntry — round-71 dance entry QUALITY falsify seat (wave 2)

- Seat: `L1Kotodama71.RevEntry` (leaf reviewer, read-only on the lane; this file is the only write)
- Date: 2026-10-25 · lane HEAD `edd7895` (`git rev-parse HEAD`)
- Object: `corpus/knowledge/culture-material/dance-performance-movement-codes.md`, blob `49a80ad9362215540a2ecbae082c73de12768b61`, sha256 `d811cd8291eafe64c550c72638ca80ff6eacaadf6508361bcd2f93df78e07f0c` (identical at `14c88d9`, `cb77200`, `edd7895` — `git rev-parse <rev>:<path>` on all three; `git diff --stat cb77200 edd7895 -- <path>` empty)
- Base for the gap claim: `b94a543c70f40dba7e49fff96d05bfb8bbd8c678` (declared `base_revision`, `reports/round-71/claims.json`), materialized with `git archive | tar -x -C /tmp/r71decl`
- Assigned criteria: (1) trio opens the file, (2) exactly one S-id per cited line, (3) no table row cites an S-id, (4) scope refuses canon, (5) topic is one line, (6) gap-filled names the word-bounded sweep.

## Verdict summary

| criterion | measured | verdict |
|---|---|---|
| 1. trio opens file | `source:` ×13 at `:3-15`, `verified-at:` `:16`, `recheck:` `:17`; first `## ` at `:26` | **PASS** on shape; the `verified-at` leg is a bare date (finding F1, MEDIUM) |
| 2. exactly one S-id per cited line | 36 cited lines, each exactly 1 distinct id; `check-cited-lines.py` exit 0 | **PASS** (leg exercised on 36 real lines; mutation proves it can fail) |
| 3. no table row cites an S-id | 0 lines start with `|` (the file has no tables); the only `|` is the regex alternation in `:19` | **PASS**, but the TABLE-ID leg is unexercised on this file (finding F7); mutation proves the leg is real |
| 4. scope refuses canon | `:23` "it decides no world's canon"; `:24` refuses canon/historical truth; `:109-110`, `:119-124` restate the handoff | **PASS** |
| 5. topic is one line | single `- topic:` at `:20`, one physical line, no continuation | **PASS** |
| 6. gap-filled names the word-bounded sweep | both commands reproduce at base (0 hits, exit 1); unbound variant = 1 hit ("avoidance") | **PASS** on the gap claim; one parenthetical count is false (finding F3, LOW) |

No criterion FAILs. Three defects sit inside criteria 1 and 6 at review-only depth (F1, F3), and one cross-file defect is routed from the entry's own 13-row source list (F2).

## Commands and observed output

1. `python3 -B tools/check-cited-lines.py corpus/knowledge/culture-material/dance-performance-movement-codes.md` → `CITED-LINES: 0 finding(s) in 1 file(s)`, exit 0.
2. Independent count (not the tool): per-line `\bS\d{3,4}\b` scan over all 125 lines → 36 lines carry ids, each exactly one: header `3-15` (S861-S873), section claims `31,34,37,45,48,58,61,69,75,82,86,93`, build steps `98-108`. Distinct ids = 13; **S873 appears only at `:15`** (finding F2).
3. Mutation proof of the lint (temp copies in `/tmp/linttest`, lane untouched): clean copy exit 0; copy with `(S871, S872)` on `:31` and an added table row `| kabuki | (S867) |` prints `MULTI-ID /tmp/linttest/b.md:31 S871,S872`, `TABLE-ID /tmp/linttest/b.md:93 S867`, exit 1. `--selftest` → `selftest 26/26`, exit 0.
4. Table-row sweep: `python3 -c` scan for `l.lstrip().startswith('|')` → `[]`; pipes anywhere → `[19]` only.
5. Trio sweep: `re.match(r'^- [a-z][a-z -]*:', l)` → `- source` ×13 (`:3-15`), `- verified-at` (`:16`), `- recheck` (`:17`), then `- gap filled/topic/sources/couples/scope/refuses` (`:19-24`). First `## ` heading `:26`. `python3 -B tools/gates/provenance-audit.py <entry>` → `findings=0 blocked=0`, exit 0 (the gate reads `topic|sources|couples` and is blind to the trio by construction, `corpus/knowledge/verification/header-conformance-readings.md:29`).
6. Gap sweeps at base `b94a543` (in `/tmp/r71decl`):
   - `find corpus/knowledge/culture-material -maxdepth 1 -type f -name '*danc*'` → no output, `count=0`
   - `grep -rniE '^- topic:.*\b(danc|choreograph|movement culture|performance)\b' corpus/knowledge/culture-material/*.md` → no output, exit 1
   - unbound variant `grep -rniE '^- topic:.*(danc|choreograph|movement culture|performance)' …` → 1 line, `funerary-material-culture.md:4` ("…WORD (the death register: avoidance terms, rite terms…")
   - `find corpus/knowledge/culture-material -maxdepth 1 -type f | wc -l` → 35; `find corpus/knowledge -type f -name '*.md' | wc -l` → 242
7. Post-landing: `python3 -B reports/round-71/accept-c.py --root .` at `edd7895` → all 7 legs PASS (`culture-material=36 corpus=243`, `distinct S-ids cited=13`, `check-cited-lines exit=0`), `ACCEPT-C-71: PASS`, exit 0. Its SWEEP leg shows the only filename owner and the only topic-line owner are the entry itself.
   - Precision note on `:19`: the topic-line sweep is word-bounded (`\b…\b`); the filename sweep is a substring glob (`-name '*danc*'`, which also matches "avoidance"/"dancing"). The line calls both "word-bounded". This is not a false claim — a substring sweep returning 0 is strictly stronger than a word-bounded one, and it returns 0 at base — but the modifier is accurate only for the second command.
8. Quote re-location (12 of the 13 rows re-opened by plain `curl`, ordinary user-agent; page text stripped of tags):
   - S861 tango, S862 Mevlevi, S863 Chhau, S864 Oruro, S865 flamenco, S866 Talchum, S867 kabuki, S868 ABT, S870 ICKL, S871 Nāṭyaśāstra, S872 Abhinaya-darpana, S873 SEP → HTTP 200, each claim's quoted span found (details in F4-F6 where a span is exceeded).
   - S869 RAD live URL → HTTP 403 to a plain request; the row's capture `20260907171642` → HTTP 200 and contains "Benesh Movement Notation (BMN) is a system for documenting human movement. It is mainly used in the documentation and reconstruction of dance pieces."; the capture's embedded original normalizes to the live URL.
   - S871 "Two Karaṇas will make one Mātṛkā, and two, three, or four Mātṛkās will make up one Aṅgahāra" confirms the entry's karaṇa→mātṛkā→aṅgahāra hierarchy.
   - S868 "Although the positions of the feet are standard in all methods, the positions of the arms are not, each method having its own set of arm positions" confirms the entry's school-relative claim.

## Findings by severity

### F1 — MEDIUM: the trio is present but its `verified-at` leg is a bare date (boilerplate verification)

- `:16` is exactly `- verified-at: 2026-10-25`. It names no check and no instrument, so a reader cannot re-derive what the pass verified.
- The lane's standing decision forbids this shape: `corpus/knowledge/verification/header-conformance-readings.md:140` DR-4 — "entries gain the trio only with a check they performed and can cite", grounded in `reports/supplement-opencode-1/28-corpus-contract.md:162` ("Do not add empty or boilerplate `verified-at:` … a placeholder date is a fabricated verification").
- Every sibling entry landed in rounds 65-70 that carries the trio carries a statement instead: `games-play-sport-contests.md:5` ("26 cited claims inserted from the registry rows opened this round … L1 preflight on the frozen counter passes"), `medicine-healing-codes.md:5`, `scent-perfume-aromatics-codes.md:5`, `footwear-codes-terminology.md:8` ("written against the lane worktree on the round-61 instruments `78ad4b17`; pre-entry knowledge files 235, post-entry 236, measured by …").
- Prevalence, measured corpus-wide: `grep -rlE '^- verified-at: *[0-9]{4}-[0-9]{2}-[0-9]{2} *$' corpus/knowledge --include=*.md` returns exactly 2 files — this entry and `civilizations/mali-songhai.md:7` (round-9 A-remainder, `9dc18ec`, 2026-10-17). The dance entry is the only entry landed after round 9 with a bare-date `verified-at`, and the only one in round 71.
- No automated leg catches it: the lane gate reads `topic|sources|couples` (`tools/gates/provenance-audit.py` FIELD_NAMES; my run exits 0 on this file), `grep -rln verified-at tools/gates/*.py` returns nothing, and `reports/round-71/accept-c.py` never reads `verified-at` (its legs are ENTRY/COUNTS/CITED/ROWS/USEDBY-PATHS/CITED-LINES/SWEEP). The only `tools/` match is `tools/harness/couples-reference-extractor.py:220,228,235`, which **emits** a bare `- verified-at: 2026-10-19` template line — the boilerplate shape has a generator and no checker.
- Smallest fix (owning lane, not this seat): state the check, e.g. "`verified-at: 2026-10-25 — 13 rows opened this round, each quote located in the live page or its capture; entry shape at `check-cited-lines.py` exit 0; 12 claims re-located by RevEntry`". Do not template it into other files.

### F2 — MEDIUM: S873 is registered, `mined`, and `used-by` the entry, but no claim in the entry cites it

- `:15` registers S873 (SEP, *The Philosophy of Dance*); `:116` says "SEP's entry is tier B" but carries no id; the body cites S861-S872 only (12 ids over 12 section claims + 11 build steps).
- `corpus/SOURCES.md:828` S873 cell 11 is `corpus/knowledge/culture-material/dance-performance-movement-codes.md`, and the Gate row (`corpus/lessons/round-71.md:31`) records the quote "This is a vexed methodological question" — I confirmed that string locates on `https://plato.stanford.edu/entries/dance/` ("What counts as 'philosophy' of dance? This is a vexed methodological question."). The quote is real and the row is opened; it simply anchors nothing in the entry.
- Consequence for claim C: `accept-c.py` leg 3 builds `cited = set(TOKEN_RE.findall(entry_text))`, which counts the header `- source:` lines, so it prints `distinct S-ids cited=13` and passes `>=12`. The leg cannot distinguish 12 claim-citing rows from 13 header-listed rows; a row can be registered and never used and the declared leg still passes.
- Either fix is lane work: add the one claim the SEP row was registered for (the entry's own topic names "the social/role codes of performance"; SEP section 1 frames the definition/ephemerality debate the entry's `Limits and handoff` leans on), or correct S873's `used-by`. Silence leaves a mined row with a false `used-by` assertion.

### F3 — LOW: the gap-filled parenthetical "the single 'choreograph' token" is false

- `:19` says "Partial one-way owners remain … `dress-through-eras.md` (the single "choreograph" token)".
- Measured: `grep -niE "choreograph\w*" corpus/knowledge/culture-material/dress-through-eras.md` → one line (`:13`) containing the exact word **three** times ("draped cultures choreograph movement; tailored cultures choreograph posture; layered cultures choreograph *opacity*"); `grep -oiE "\bchoreograph\b" … | wc -l` → 3.
- The stem also appears in 8 other knowledge files the parenthetical does not name: `linguistics/numerals-and-measures.md`, `linguistics/sign-languages-manual-modality.md`, `civilizations/{taino,germanic-norse,maori,hopi,korea-joseon}.md` (`grep -rliE choreograph corpus/knowledge --include=*.md`).
- The central gap claim is unaffected (see criterion 6). Fix: "one line, three tokens" or drop the count.

### F4 — LOW: `:45` "governed by the ICKL" exceeds the S870 homepage text

- Entry: "Kinetography Laban/Labanotation is governed by the ICKL, whose practitioners practice the system originated by Rudolf Laban (S870)."
- `http://ickl.org/` (fetched, 200, body text 2 766 chars): "The International Council of Kinetography Laban was founded in England in 1959. It currently has nearly a hundred members and fellows from across the continents. Its members practice the system of movement and dance notation originated by Rudolf Laban, known as Kinetography Laban or Labanotation."
- The page has **no** occurrence of `authorit` or `govern` (case-insensitive scan). "Governed by" is an inference from the organisation's name, and build step 4 (`:101`) repeats it as "bind it to the notation authority (S870)". The registry's `teaches` cell (`corpus/SOURCES.md:825`) makes the same leap ("the international authority for that notation system"), so the fix may belong to the row's scope as well as the entry clause.
- Note the clause shape: one line, two clauses under one id — permitted by QUALITY 15's shape rule, review-only at clause scope (criterion 15 names exactly this).

### F5 — LOW: `:59-61` mangled S861 paraphrase ("an embodied identity that both embodies")

- Entry: "Tango is defined by UNESCO as the music, dance and poetry of tango together — an embodied identity that both embodies and encourages diversity and cultural dialogue (S861)."
- Source: "As one of the most recognizable embodiments of that identity, the music, dance and poetry of tango both embodies and encourages diversity and cultural dialogue."
- The source's subject is the music/dance/poetry; the entry makes "an embodied identity" the subject and then has it "embody" itself. Substance survives, wording is self-referential. Fix: "…the music, dance and poetry of tango together embody and encourage diversity and cultural dialogue".

### F6 — LOW: `:46-48` drops the "mainly" qualifier from S869

- Entry: "…a system for documenting human movement, used in documentation and reconstruction of dance pieces (S869)."
- Capture text: "It is **mainly** used in the documentation and reconstruction of dance pieces."
- Typical-use hedge → blanket use. Fix: "mainly used in".

### F7 — INFO: the TABLE-ID leg is vacuous on this file, and `:34` is a cited line with no claim on it

- The file contains no table at all, so criterion 3 passes with zero instances. I proved the leg is not dead by mutation (`TABLE-ID …:93 S867`, exit 1), but nothing about this entry exercises it.
- `:34` is the line `(S872).` alone (a wrapped paragraph): it carries the id but no claim text, the inverse of the shape the criterion guards against. Same pattern at `:31` (id ends a wrapped line). Passes the lint; a packet row shows a bare id.
- Also on usability (QUALITY 4, not in my assigned set): the entry is prose sections plus an 11-step build order, with no decision/typology table, where `footwear-codes-terminology.md:26-33` and `games-play-sport-contests.md` carry tables and bullet anchors. Not a criterion failure, but it is the one QUALITY axis where this entry is thinner than its round-61-70 siblings.

## Residual risk and verification gaps

- **Out-of-slice observation (routed, not claimed):** the CITED leg's header-line counting (F2) is the one place where claim C's `>=12` predicate is satisfied by registration rather than use. RevCounterC owns that leg; this report only supplies the entry-side evidence.
- **Receipt provenance (checked, no defect):** `reports/round-71/telemetry/measures-c.txt` is in HEAD's tree and is internally consistent at its stamped revision `8c203bd`: `git show 8c203bd:reports/round-71/accept-c.py | sha256sum` = `1df995c2…` (the receipt's `# counter sha256 (self)`), `git rev-parse 8c203bd^{tree}` = `ffb5c549…` (the receipt's `# tree`). HEAD's `accept-c.py` is `80b4ca09…` after `edd7895`'s one-line docstring edit, so a re-run is not byte-identical to the receipted counter — the verdict reproduces (all 7 legs PASS at `edd7895`).
- **Not run by this seat:** `tools/check-gate-quotes.py corpus/lessons/round-71.md` (RevGate's slice; its wave-2 report records the Gate table-shape blind spot). I verified quote location by fetching, not by the checker, and only for the 13 quotes the entry's `- sources:` line names.
- **Fetch surface:** 14 ordinary `curl` requests (13 rows, RAD via its capture); no archive substitution except S869's declared capture; no challenge bypassed. Page text was tag-stripped, so a span "found" here is body text, not an attribute or caption.
- **Not verified:** the entry's `- couples:` semantics (13 paths, all exist — `os.path.exists` on each), the README row text, and the lesson's 13 Gate rows as a table (RevREADME/RevGate/RevRows).
- Entry bytes are frozen at blob `49a80ad` across `14c88d9`→`edd7895`, so these findings hold for every wave-2 revision that has landed so far.
