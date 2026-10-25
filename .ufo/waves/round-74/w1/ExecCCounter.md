# ExecCCounter — claim-C acceptance counter (kotodama round 74, wave 1)

Seat: `ExecCCounter` (leaf executor). Assigned write paths used: this report and
`.ufo/waves/round-74/counters/accept-c.py`. Nothing else in the lane, the fleet root, the
jj/git state or `/home/vgpnk/Projects/shokuknow` was written. No network fetch was made (so
there is no User-Agent to record); no tool was installed (python3 3.14.8 + stdlib only).

## 1. What landed

| path | sha256 | size |
|---|---|---|
| `.ufo/waves/round-74/counters/accept-c.py` | `64e4c19090d51bfe8066a25aca474f12fd1bacbc255a86b3a1b1eed27693dbe1` | 102353 B, 2439 lines |

Adapted from `reports/round-73/accept-c.py` (read whole, 1687 lines). Kept: the leg/`leg()`
protocol, the materialize-then-read grading model, the r73 receipt-header grammar, the
fixture-per-mutant selftest shape. Changed: `git archive` → `git clone` + `checkout --detach`
inside the mktemp dir; config source → `git show <freeze>:…`; the r73 `--base`/`--census-sh`
flags are gone (`--base` now comes from the frozen claims.json); the r73 `SCRATCHMIRROR`
`git log -S` heuristic is replaced by an explicit base..lands rev-list walk; 12 legs.

## 2. CLI and receipt

```
python3 -B accept-c.py --root <lane> --lands <40hex> --freeze <40hex> [--fleet-root <fleet>] [--selftest]
```

Exit 0 = all legs pass, 1 = a leg failed, 2 = input error or **refusal**.
The receipt header is the `tools/check-receipt-seq.py` grammar (`# counter sha256 (self)`,
`# stamped revision`, `# evaluated revision`, `# measured revision (lane main)`, `# tree`)
plus `# base revision`, `# freeze revision`, `# config sha256 (frozen claims.json)`,
`# config source: git show <freeze>:reports/round-74/claims.json (never the graded tree)`,
`# materialized: git clone of … checkout --detach …`, `# lane worktree HEAD (disclosure only)`.
`measured` is the revision the clone was checked out at (= lands), so stamped == evaluated ==
measured == lands, as the Ca STAMP leg requires; the lane worktree HEAD is printed only as a
disclosure and is never graded.

## 3. The 12 legs (each frozen in claims.json `legs[]`)

| leg | reads at `<lands>` | fails when |
|---|---|---|
| ENTRIES | both entry files | missing; present at base; header field missing/placeholder; no `## ` section; body < the smallest base knowledge entry in words |
| ROWS | `corpus/SOURCES.md` base vs lands | any added line that is not an adopted row; any removed line that is not a reused row's old line; a reused-row pair differing outside the used-by cell; non-contiguous or below-base ids; cells ≠ 11; `\|`; status ≠ mined; opened ≠ access date; recheck not a cadence; source cell lacking the map URL verbatim; anchor cell lacking the evidence quote; used-by ≠ exactly the citing entries; used-by union ≠ the entries; reused used-by change not logged old→new |
| REPOINTED | both entries + registry | a `source:` line with ≠1 id; an id outside the five adopted/reused rows; a cited URL not registered on that row; any inline id outside the five; a staged-namespace id (S899/S900) cited as a lane row |
| GATE | `corpus/lessons/round-74.md` `## Gate` | admit header lacks quote/date/locator columns; a row without its URL, the access date, a recomputed ≤25-token quoted span or a non-dash locator; no admit or no reject row; a reject row without a probed URL, reason or flip; a re-quoted row (staged id in `forced_new_quotes`) not stating re-quote + absent/refused/mispairing |
| EVIDENCE | `reports/round-74/evidence/<id>.txt` | missing file; http-status ≠ 200; access-date ≠ access date; sha256 not 64-hex; UA not `Mozilla/5.0…`; fetch line not naming the row URL; no stored window; **the Gate quote absent from the window after NFKC+whitespace folding** |
| REJECTS | the lesson | a refused staged id not named (or not tied to its existing lane row); a `forced_new_quotes` id not named with its refusal/re-quote; a `refused_files` name absent; no reason+flip record |
| GROUND | `reports/round-74/telemetry/gap-sweep.txt` + base tree | receipt missing; receipt's N-row figure ≠ the base row count; no `0` per fragment / per CJK term; the base registry already naming a fragment; a base knowledge file already carrying a CJK term; a base knowledge file already carrying an entry stem |
| CITEDLINES | `tools/check-cited-lines.py` in the clone | tool exit ≠ 0, or the summary is not `CITED-LINES: 0 finding(s) in N file(s)` |
| CENSUS | real `scripts/sources-census.sh` via a temp fleet root | exit ≠ 0, any `E`-code, or no `kotodama\tok` line |
| SCRATCHMIRROR | `.ufo/waves/round-74/assimilation/validate-receipt.txt` | no `--file`, no exit 0, a missing row id or entry basename, or the receipt's introducing commit not strictly before the registry-append commit (found by walking `rev-list base..lands` and reading each registry blob) |
| COLLCHECK | `assimilation/{reg-ids,staged-ids,collisions}`, `assimilation/guard-proof/`, `assimilation/id-renumber-map.json` | an adopted id in reg-ids/collisions; a staged id missing; no 1-3-space planted row with a positive detection marker; no 4-space plant with a not-found marker; the map missing old→new for an adopted id, mapped to the wrong staged id, or carrying a URL the row does not name |
| FROZENCFG | `git show <freeze>:claims.json` + lands claims blob | freeze not a strict ancestor; base not an ancestor of lands; **claims.json at lands ≠ the frozen bytes**; non-contiguous frozen row_set; empty entries/ground lists |

## 4. Hardenings (each named in the docstring, each with a mutant)

- **H1 FROZENCFG** — every constant (row_set incl. staged ids, reused_rows, entries,
  ground.fragments, ground.cjk_terms, the rejects lists, the claim base, the access date) is
  read with `git show <freeze>:reports/round-74/claims.json`. `load_frozen_config()` has no
  other source; the graded tree's claims.json is read only to prove it is byte-identical.
  `<freeze>` not a strict ancestor ⇒ `REFUSED` (exit 2) before any byte is graded. Mutant
  `config_edited_in_lands` fails FROZENCFG; the refusal cases are scenarios 5–7.
- **H2 EVIDENCE** — the Gate quote is searched inside the stored `--- window ---` body after
  `NFKC` + whitespace folding. `quote-found:` / `quote-found-verbatim:` / `quote-words:` are
  never read. Mutant `evidence_quote_absent` writes `quote-found: yes` over a window with no
  matching sentence and fails EVIDENCE.
- **H3 GATE** — the quoted span is re-tokenised from the row itself and must be ≤25 whitespace
  tokens. Mutant `gate_quote_words` (30 tokens) fails GATE with `recomputed: [30]`.
- **H4 ROWS** — registry diff base..lands as a line multiset: added lines must be the adopted
  rows; removed lines must be a reused row's old line; that pair may differ in the used-by
  cell alone. Prose edits, in-place edits elsewhere, extra rows, removed rows and gaps all
  fail (mutants `registry_prose`, `inplace_other`, `extra_row`, `remove_row`, `row_gap`).
  A blank line is tolerated — it adds no row and hides no row (narrower than the r73 hunk
  rule, not wider than the frozen sentence).
- **H5 junk landings** — stub entry → ENTRIES; staged rows with used-by at stub paths → ROWS;
  entry citing an id whose row URL differs → REPOINTED; config edited in the graded tree →
  FROZENCFG.

## 5. Selftest — exercised, not asserted

```
$ python3 -B .ufo/waves/round-74/counters/accept-c.py --selftest
SELFTEST: 52/52 scenarios          (exit 0, ~9 s)
```

52 scenarios = 11 controls + 41 mutants; **every one of the 12 legs has at
least one mutant that fails that named leg** (`set(EXPECTED_FAIL.values()) == set(leg names)`).

Controls: `clean` (PASS 12/12 + stamped/evaluated/measured + frozen-config disclosure),
`lands-eq-base` (FAIL), `missing-lands` (exit 2), `missing-freeze` (exit 2), `freeze-eq-lands`
(refused), `freeze-descendant` (refused), `freeze-no-claims` (refused), `config-narrow-drives-
rows` (FAIL ROWS — the frozen row_set really drives the leg), `config-extra-row` (FAIL ROWS),
`guard-r73-shape` (PASS — the COLLCHECK guard leg is not over-fitted to my fixture prose),
`do-nothing-no-data` (FAIL, with ENTRIES and ROWS failing and FROZENCFG still passing).

Mutants by leg (41): ENTRIES 4 (`drop_entry`, `stub_entry`, `placeholder_header`,
`entry_at_base`); ROWS 10 (`staged_as_is`, `usedby_stub`, `row_gap`, `extra_row`,
`remove_row`, `inplace_other`, `registry_prose`, `anchor_no_quote`, `map_url_absent`,
`reused_unlogged`); REPOINTED 3 (`repoint_url`, `campaign_id`, `inline_unrelated`);
GATE 5 (`gate_quote_words`, `gate_reject_no_url`, `gate_no_admit`, `gate_reject_no_flip`,
`gate_no_requote`); EVIDENCE 4 (`evidence_missing`, `evidence_quote_absent`,
`evidence_bad_ua`, `evidence_bad_sha`); REJECTS 2; GROUND 3; CITEDLINES 1; CENSUS 1;
SCRATCHMIRROR 3; COLLCHECK 4; FROZENCFG 1.

Every mutant was also probed for *why* it fails (not just that it fails) — e.g.
`staged_as_is → "S881 row carries an escaped pipe (staged text appended as-is)"`,
`map_url_absent → "S882 source cell lacks the map URL verbatim: …"`,
`reused_unlogged → "S877 used-by change not logged old->new in corpus/lessons/round-74.md"`,
`config_edited_in_lands → "reports/round-74/claims.json at lands differs from the frozen bytes"`.

Clean-fixture receipt (captured, `/tmp/ExecCCounter/clean-run.txt`):

```
# counter sha256 (self): 64e4c190…
# stamped revision: 1c5d8c31…   # evaluated revision: 1c5d8c31…
# measured revision (lane main): 1c5d8c31…   # tree: 289d775e…
# base revision: 8ce7254e…   # freeze revision: 44192a6a…
# config source: git show 44192a6a…:reports/round-74/claims.json (never the graded tree)
LEG PASS × 12 ;  ACCEPT-C-74: PASS legs=12/12 ;  exit=0
```

## 6. Read-only checks against the real lane (evidence, not a claim grade)

The counter cannot be graded yet (no freeze/lands commit exists) — by design it refuses. What I
did verify, read-only:

1. **Base re-derivation of the claim's before-state** (materialized `f7104cb` into /tmp and ran
   the counter's own GROUND helpers): `base rows: 804`, last id `S880`; fragment occurrences in
   the base registry `{litmemo.com: 0, tuduku.space: 0, chinawriter.com.cn: 0}`; 247 knowledge
   `.md` files with **0** CJK hits for 設定ノート / 世界観 / 世界观; 0 `worldbuilding-setting`
   stems. This matches `before` (a)(b)(c) exactly.
2. **ENTRIES body floor at base = 478 words** (the smallest `corpus/knowledge` entry). Both
   entries must therefore carry ≥478 words *after* the provenance header. (The two wave-1
   drafts are 4194 and 1989 words and cite only S877/S881/S882/S883/S884 — already inside the
   allowed set.)
3. **CENSUS invocation shape against the real script** (temp fleet root + symlink to the lane,
   read-only): `sources-census.sh validate --root <tmp> --today 2026-10-25 kotodama` → 28 W04
   lines and `kotodama\tok\t…/corpus/SOURCES.md`, exit 0. The leg's argv is accepted by the
   real parser, not only by the selftest stub.
4. **Refusals on the real lane**: `--freeze == --lands` → `REFUSED … must be a strict ancestor`
   + `ACCEPT-C-74: FAIL legs=0/12 (refused: …)`, exit 2; `--freeze` = an ancestor without
   `reports/round-74/claims.json` → refused, exit 2; missing/abbreviated hashes → exit 2.
5. **Lane state untouched**: `git rev-parse --short HEAD` = `f7104cb`; the worktree still shows
   only the six inherited round-73 w2 files plus the untracked `reports/round-74/` and
   `.ufo/waves/round-74/`; `.git/index` mtime predates this session (20:48, session started
   21:37), so no index write happened. All fixtures and clones were in `mktemp` dirs under
   `/tmp` (plus `/tmp/ExecCCounter/` for my probes).

## 7. Artifact-shape contract the landing must meet

These are the exact shapes the legs read; a miss is a FAIL, never a skip. Documented in the
counter docstring (§"Artifact shapes the legs read") so the scribes can hit them:

1. **Row**: 11 cells, `| S881 | <source, carrying the map URL verbatim> | … | <anchor, carrying
   the evidence quote> | mined | 2026-10-25 | 180d | <used-by = exactly the citing entry
   paths> |`; no `\|`.
2. **Gate admit table**: header carrying `quote`, an access-date and a `locator`/`grounds`/
   `anchor` column; one row per adopted row; the S883/S884 rows (staged S899/S900) must say
   `re-quote` **and** one of `absent`/`refus…`/`mispair…`.
3. **Gate reject table**: header carrying `reason` and `flip`; every reject row carries its
   probed URL and a non-dash reason and flip.
4. **Evidence file**: the grammar `counters/capture-evidence.py` writes — `url:`/`fetch:`,
   `user-agent: Mozilla/5.0 …`, `http-status: 200`, 64-hex `sha256:`, `access-date:
   2026-10-25`, then `--- window ---` … `--- quote ---`. The Gate quote must appear inside the
   window after NFKC + whitespace folding.
5. **Renumber map**: `.ufo/waves/round-74/assimilation/id-renumber-map.json` with
   `assignments[]` (staged_id / new_target / **url**) and/or a `map` object; the `url` must be
   the exact string that appears in the registry row's source cell.
6. **Guard proof**: one file with a literal 1-3-space-indented planted row (an id that is no
   real row) plus a positive detection marker, and a 4-space control with a not-found marker
   (a literal 4-space row, or the round-73 shape that describes it).
7. **Mirror receipt**: `validate-receipt.txt` showing `--file`, exit 0, the four ids and both
   entry basenames, committed **before** the registry-append commit.
8. **S877**: used-by must equal exactly the entries whose `source:` lines cite it, changed in
   the used-by cell alone, and logged old→new in the lesson.

## 8. Schema — no change needed

The counter reads the draft schema unchanged: `row_set[{id,staged}]`, `reused_rows[{id,staged}]`,
`entries[]`, `ground.fragments[]`, `ground.cjk_terms[]`,
`rejects.{refused_staged_not_appended,forced_new_quotes,refused_files}`, top-level `base`.
The **only optional addition** is `claims[id=C].access_date` (or top-level `access_date`);
absent, it defaults to `2026-10-25`. No existing key changed meaning. `rejects.refused_files`
entries are matched by their leading name token (e.g. `naming-systems` from `naming-systems
x11`), so their prose may change freely.

## 9. Risks / decisions for the L1 (all pre-data)

1. **`lands == base` is a refusal, not a graded FAIL.** With the round's topology the freeze
   commit is always a descendant of base, so `--freeze` can never be a strict ancestor of base
   and H1 forbids grading there. The counter prints
   `ACCEPT-C-74: FAIL legs=0/12 (refused: …)` and exits 2, so a grep-based control still sees
   FAIL (selftest scenario `lands-eq-base` asserts exactly that). Two honest options for the
   L1: keep the claims wording as it stands (the FAIL line is printed), or land `controls-c.txt`
   at a **no-data commit after the freeze** (tree = base + claims.json), which fails every data
   leg for the graded reason. Both shapes are exercised: `lands-eq-base` (refusal → FAIL line)
   and `do-nothing-no-data` (ENTRIES + ROWS fail, FROZENCFG still passes). The claims wording is
   the L1's to adjust.
2. **`legs=12` is fixed in the counter** and equals the 12 entries of the frozen `legs[]`; if
   the frozen claims.json changes the leg list, the counter must be regenerated (not silently
   diverge).
3. **CJK quote token counts are weak by construction.** `claims` says "≤25 words (CJK counts
   per whitespace token)"; a 60-character Chinese sentence can be 1 token. I implemented
   exactly the frozen rule and did **not** add a character cap (that would be wider than
   frozen). If the L1 wants a character guard for the two chinawriter quotes, it is a pre-data
   claims change plus a one-line leg change.
4. **The map URL must be verbatim in the source cell** (frozen: "the map URL verbatim in the
   source cell"). If the map writes `chinawriter.com.cn/…` without `www.` the row will not
   match; the map and the rows must be written from the same string.
5. **The two entries' bodies must reach 478 words each** after the header (real base floor).
6. The six uncommitted round-73 w2 seat files are never read by this counter (it grades a clone
   of the committed lands tree); the Ca counter is the one that must track them.

## 10. Blockers

None. The counter is complete, installed-ready (`reports/round-74/accept-c.py` is the path the
claim's `counter` command names) and its selftest is green. It has **not** been run against real
landed data: no freeze commit and no lands commit exist yet, and running it before the freeze
would be exactly the "score landed data before the rule is frozen" failure the round forbids.

## Post-wave update — final 13-leg claim (2026-10-25, L1 amendment applied)

This section supersedes the 12-leg description in §§1–3 and the 52-scenario selftest in §5.
The claim is now FINAL at 13 legs (`reports/round-74/claims.json` `legs[]`), with `INDEX`
and the `LEGCOUNT` refusal added, and with the EVIDENCE `window-scope` amendment.

### Counter

| path | sha256 | size |
|---|---|---|
| `.ufo/waves/round-74/counters/accept-c.py` | `8d30487fa4692261edfee549d2ba07517fc8b3c9fc4f5af5f0562a504ca5433a` | 127,965 B, 3017 lines |

Read-only git for metadata only; the graded bytes are a `git clone` + `checkout --detach <lands>`
(with a `git archive` fallback if the clone refuses an unreachable revision) and a
`git archive <base>` tree. Every constant comes from `git show <freeze>:reports/round-74/claims.json`.

### What changed (the L1 list, item by item)

1. **INDEX** (new leg, last in the table). `corpus/README.md` at lands must carry exactly one row
   per adopted entry *inside the `## culture-material/ (N)` section*, shaped
   ``- `name.md` — <the entry's own `- topic:` text>`` byte-for-byte; the last
   `Counts checked` footer's `(total N files; directory totals V)` must equal the landed
   `.md` count and the vector of the six partition sections (linguistics, myth-symbol,
   culture-material, synthesis, verification, civilizations — derived from the README's own
   headings); every older `Counts checked` paragraph must appear byte-identically from base.
2. **Leg count 13 + LEGCOUNT.** `LEGS` has 13 entries in the frozen order; the receipt prints
   `# frozen legs: 13 (...)` and `ACCEPT-C-74: ... legs=13/13`; a frozen `legs[]` whose length or
   ordered names differ makes the counter REFUSE (exit 2) with `LEGCOUNT: ...` and a FAIL line.
3. **ENTRIES** now rejects any header value in `{TODO, TBD, FIXME, XXX, n/a, ?, —}` (plus the
   empty value) and any value matching `<[^>]+>`; keeps the base-derived word floor (481 in the
   fixture, 478 at the real base) and the `## ` requirement.
4. **ROWS**: the four new rows keep the full row rule (11 cells, no `\|`, mined, opened =
   access date, cadence-only recheck, map URL verbatim in the source cell, evidence quote inside
   the anchor cell, used-by exactly the citing entries). The reused row S877 is now checked by
   its own rule — parsed from both revisions, it may differ **only** in the used-by cell, and
   that cell must equal `base used-by ∪ {entries[0]}` exactly (the base-entry path only).
5. **GATE**: loops over `rows + reused` (S877, S881..S884); a quote must be ≤25 whitespace
   tokens **and** ≤80 characters, recomputed from the quoted span itself.
6. **EVIDENCE**: loops over `rows + reused`; parses `window-scope: excerpt|whole-document`,
   `visible-chars:`, recomputes `window-sha256:` (and `window-bytes:` when present) from the
   stored window line, extracted exactly as `capture-evidence.py`'s `stored_window()` does;
   `excerpt` requires ≥4096 characters, `whole-document` is allowed only when the window is
   <4096 characters and equals `visible-chars:`; the Gate quote must occur in the window after
   NFKC + whitespace folding. `quote-found*` flags are still never read.
7. **REJECTS**: additionally requires the lesson to state the frozen counts in order
   (2 adopted / 4 path-present / 34 refused of 40, paragraph-scoped so a wrapped line is fine),
   to name the folded-dropped staged row (S895) as folded/dropped, and to carry a
   `## Quarantine` section naming S816 and S817 as refused with the phrases `stay refused` and
   `re-opened as new rows`; the frozen `path_present_bytes_differ` length must equal
   `counts.path_present`.
8. **CENSUS**: passes iff `sources-census.sh validate` exits 0 against a temp fleet root whose
   `kotodama-shokunin` is the materialized lands tree **and** no TSV line matches
   `^E[0-9][0-9]` (the `kotodama\tok` line is disclosure, not a condition).
9. **FROZENCFG**: `map.path` and `map.sha256` are read from the frozen claims; the sha256 of
   `git show <freeze>:<map.path>` must equal `map.sha256`; the freeze must be on `<lands>`'
   first-parent chain (`git rev-list --first-parent <lands>`), the claim base an ancestor of
   lands, and `reports/round-74/claims.json` at lands byte-identical to the freeze blob.
10. **COLLCHECK** reads the by-document map from the freeze commit (`git show <freeze>:<path>`),
    not from the graded tree; the real map's `new_lane_id` key is accepted alongside
    `new_target`/`map`.
11. **Controls**: `lands == the frozen base` is a REFUSAL (exit 2) that still prints
    `ACCEPT-C-74: FAIL`; `lands == <freeze>` is **not** a refusal — it is a graded FAIL with
    ENTRIES/ROWS/GATE/EVIDENCE/REJECTS/INDEX red and FROZENCFG green; a freeze after lands is a
    graded FAIL with FROZENCFG red; a freeze without claims.json is still a refusal.
12. **Selftest** keeps every earlier scenario and adds the required mutants.

### Selftest — exercised

```
$ python3 -B .ufo/waves/round-74/counters/accept-c.py --selftest
SELFTEST: 69/69 scenarios
```

(exit 0, ~28 s, every fixture is `mktemp -d` + `git -C "$D" init -q`, fixtures removed at exit.)

69 scenarios = 12 controls + 57 mutants. Controls: `clean` (PASS 13/13 + stamped lands +
freeze revision + frozen-config source + `# frozen legs: 13`), `lands-eq-base` (refusal, FAIL
line), `missing-lands`, `missing-freeze`, `legcount-mismatch` (refusal naming LEGCOUNT),
`freeze-eq-lands` (FAIL exit 1 with the six data legs red and FROZENCFG green),
`freeze-descendant` (FAIL FROZENCFG), `freeze-no-claims` (refusal), `config-narrow-drives-rows`
(FAIL ROWS + receipt follows the frozen set), `config-extra-row` (FAIL ROWS), `guard-r73-shape`
(PASS 13/13 — the four-space control is not over-fitted), `do-nothing-no-data` (FAIL with
ENTRIES/ROWS red and FROZENCFG green).

Coverage is asserted set-wise: `set(EXPECTED_FAIL.values()) == {13 leg names}`; each leg has at
least one mutant that fails it, and every mutant was inspected for *why*:

- ENTRIES — `drop_entry`, `stub_entry`, `stub_entry_400` (401-word body vs the 481 floor),
  `placeholder_header`, `entry_at_base`;
- ROWS — `staged_as_is`, `usedby_stub`, `row_gap`, `extra_row`, `remove_row`, `inplace_other`,
  `registry_prose`, `anchor_no_quote`, `map_url_absent`, `reused_unlogged`,
  `reused_usedby_wrong` (`S877 used-by=... (want its base value plus exactly ...)`);
- REPOINTED — `repoint_url`, `campaign_id`, `inline_unrelated`;
- GATE — `gate_quote_words` (30 tokens), `gate_quote_chars` (4 tokens / 103 chars),
  `gate_reject_no_url`, `gate_no_admit`, `gate_reject_no_flip`, `gate_no_requote`;
- EVIDENCE — `evidence_missing`, `evidence_quote_absent`, `evidence_bad_ua`, `evidence_bad_sha`,
  `window_sha_tamper`, `window_short` (33 chars), `window_scope_whole_4096`,
  `window_scope_visible_mismatch`, `window_scope_unknown`;
- REJECTS — `no_refused_staged`, `refused_file_missing`, `rejects_counts_missing`,
  `quarantine_missing`;
- GROUND — `ground_zero_missing`, `ground_cjk_missing`, `ground_rows_wrong`;
- CITEDLINES — `multi_id_line`; CENSUS — `census_fail`;
- SCRATCHMIRROR — `receipt_no_exit`, `receipt_in_append`, `receipt_missing_ids`;
- COLLCHECK — `collisions_adopted`, `guard_missing`, `guard_fourspace_missing`;
- FROZENCFG — `map_missing`, `map_sha_mismatch`, `config_edited_in_lands`;
- INDEX — `index_missing_row`, `index_topic_mismatch`, `index_footer_total`,
  `index_footer_vector`, `index_older_footer_edited`.

### Real evidence files — read-only audit (no lands commit exists)

`_evidence_core()` (the leg's per-file half) run against `reports/round-74/evidence/*.txt`,
with row URL keys from the base registry (S877) and from the intended map URLs (S881..S884):

| id | window-scope | visible-chars | window chars | window-sha256 recomputed | Gate quote in window |
|---|---|---|---|---|---|
| S877 | excerpt | 492810 | 4098 | yes | yes |
| S881 | excerpt | 9855 | 4098 | yes | yes |
| S882 | **whole-document** | 2953 | 2953 | yes | yes |
| S883 | excerpt | 8162 | 4104 | yes | yes |
| S884 | excerpt | 12270 | 4103 | yes | yes |

All five produce **0 findings**. S882 is the only whole-document capture and its window equals
`visible-chars` exactly (2953 < 4096), as the amended rule allows. The amended S877 Gate quote
«Язык – главный инструмент построения вымышленных миров» is 54 characters / 7 tokens
(`quote_ok` true) and occurs in the S877 window after NFKC + whitespace folding.

What could **not** be exercised: the Gate↔window coupling, because `corpus/lessons/round-74.md`
does not exist yet (the `EVIDENCE` leg needs its `## Gate` table). That coupling is covered by
the selftest (`evidence_quote_absent` fails, clean passes) and will run for real at lands. The
leg function itself, run read-only on the current worktree, reports exactly that:

```
$ python3 -B -c "… leg_evidence(ctx with mat=<lane worktree>) …"
LEG FAIL EVIDENCE
     corpus/lessons/round-74.md
```


### Real frozen-config probe (temporary clone, read-only on the lane)

A temp clone in `/tmp` with the worktree `claims.json` + `id-renumber-map.json` committed (then
deleted) was fed to `load_frozen_config()`: the loader accepts the FINAL claims — base
`f7104cb…`, rows S881..S884 (staged S883/S884/S899/S900), reused S877 (staged S882), both entry
paths, 3 fragments, 3 CJK terms, refused S882, forced S899/S900, folded S895, 7 refused
files, 4 path-present paths, counts 2/4/34/40, `map.path` set, and a 13-name `legs[]` whose
ordered names equal `LEGS` (LEGCOUNT would pass).

**One freeze-time action is required:** `claims[id=C].map.sha256` is still the placeholder
`FILLED-AT-FREEZE`. The map blob at the probe freeze hashes to
`d3573f7d3cf23afa7296c281d201225eed643aef2b406b3a403c2a67aeb24afa`, so FROZENCFG is red at
lands until the freeze fills that field (or the map changes and the freeze records the new
hash). This is an L1/freeze action, not a counter change.

Pre-freeze refusals on the real lane (exercised): `--lands f7104cb… --freeze f7104cb…` →
`REFUSED: cannot read reports/round-74/claims.json at freeze f7104cbce186 …` +
`ACCEPT-C-74: FAIL legs=0/13 (refused: …)`, exit 2 — correct while no freeze commit exists.

### Deviations and readings worth an attack

1. `lands == <freeze>` is a graded FAIL (exit 1), not a refusal — exactly the L1 control. The
   earlier draft refused it; the scenario and `main()` were changed accordingly.
2. A freeze *after* lands is a graded FAIL with FROZENCFG red (was a refusal in the draft).
3. INDEX is strict about the section: rows must sit under the `## culture-material/ (N)` heading.
   The scribe's draft inserts at `:444`/`:445` inside that section, so it satisfies the rule; a
   future landing that appends rows in a separate `## Round N additions` block would fail INDEX.
4. INDEX compares the footer vector against counts derived from the README's own six section
   names, not against a hard-coded order; a README with a seventh `## <name>/ (N)` section fails
   INDEX with both the vector and the "six partition sections" finding.
5. CENSUS no longer requires a `kotodama\tok` line (the frozen sentence is "exit 0 and no
   `^E[0-9][0-9]` line"); a silent stub that exits 0 would pass this leg. The selftest's stub
   prints `kotodama\tok\tstub`, so the legacy shape still works.
6. EVIDENCE requires `visible-chars` for both scopes and recomputes `window-bytes` when present;
   the frozen sentence only names `window-sha256`, so a file with `window-scope` but no
   `visible-chars` fails — the five real files carry both.
7. The map parser accepts the real map's `new_lane_id` key (the draft only accepted
   `new_target`/`map`), so the real map's URLs reach ROWS and COLLCHECK.
8. The GROUND row-count pin is derived from the materialized base (804 for the real base,
   4 in the fixture), never hard-coded to 799.
9. No new tool was installed; no network fetch was made by this seat; the five evidence files
   were read, never written. Lane state untouched: `git status --short` still shows only the
   inherited round-73 w1/w2 modifications plus the untracked `reports/round-74/` and
   `.ufo/waves/round-74/` trees.
