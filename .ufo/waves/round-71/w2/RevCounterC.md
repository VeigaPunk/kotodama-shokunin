# RevCounterC — round 71 wave 2 (claim-C counter, rows S861–S873, source re-open)

Seat: L1Kotodama71.RevCounterC · read-only on the lane · no installs/updates performed.

## Verdict

`ACCEPT-C-71: PASS` reproduces at lane HEAD in a fresh archive. All 13 rows S861–S873 are inside `## Registry`, status `mined`, and used by the entry. All re-opened quotes are verbatim. However, **four legs (CITED, ROWS, USEDBY-PATHS, SWEEP) can pass vacuously or under-enforce the docstring predicate**, as shown by mutation probes. Today's pass rests on the actual bytes, not on what the counter enforces.

## Fresh-clone runs (exact commands)

HEAD moved three times during the review. Each HEAD I saw was run fresh:

```
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
D=$(mktemp -d) && git archive HEAD | tar -x -C $D && cd $D && python3 -B reports/round-71/accept-c.py --root .; echo EXIT=$?
```

| HEAD | ENTRY | COUNTS | CITED | ROWS | USEDBY-PATHS | CITED-LINES | SWEEP | exit |
|---|---|---|---|---|---|---|---|---|
| 14c88d9 | PASS | PASS 36/243 | PASS 13 | PASS | PASS | PASS (0 findings) | PASS | 0 |
| ccadb59 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | 0 |
| edd7895 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | 0 |

Cross-check: `find corpus/knowledge/culture-material -type f | wc -l` → 36; `find corpus/knowledge -type f -name '*.md' | wc -l` → 243. `git diff 8c203bd HEAD -- corpus/` touches only the S860 row and lessons, so the receipt's measured revision `8c203bd` and HEAD agree on claim-C bytes.

## Rows S861–S873 — PASS

- `grep -n '^#' corpus/SOURCES.md`: `## Registry` at line 26, `## Paths` at 829. The 13 rows sit at lines 816–828, inside Registry.
- Header (line 28): `id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by`. This matches the counter's `cells[8]` (status) and `cells[11]` (used-by). All 13 rows split into 13 cells, with no stray `|`.
- All 13: status `mined`, opened `2026-10-25`, used-by exactly `corpus/knowledge/culture-material/dance-performance-movement-codes.md`.
- No duplicate ids anywhere in SOURCES.md (`uniq -d` empty). S861–S873 appear only on lines 816–828.
- Registry has 797 rows, all inside the section. The pre-round `assimilation/reg-ids` has 784 rows ending at S860, so the 13 ids are genuinely new.

## Source re-open — quotes PASS, anchors FAIL (inconsistent)

Wayback was intermittently unreachable (`curl: (7) Failed to connect to web.archive.org:443`); a retry with `--retry 3 --retry-all-errors` fetched both captures.

| row | fetched | Gate quote | result |
|---|---|---|---|
| S862 | live `ich.unesco.org/en/RL/mevlevi-sema-ceremony-00100` (200) + capture `20220323094705` (200) | "the whirlers begin to rotate on their left feet in short twists" | verbatim in both; entry's "using the right foot to drive their bodies around the left foot" also verbatim |
| S864 | live `…/carnival-of-oruro-00003` (200) + capture `20210227223454` (200) | "the dancers walk the four kilometres of the processional route" | verbatim in both; "repeat the journey for a full twenty hours without interruption" verbatim |
| S868 | live `abt.org/explore/learn/ballet-dictionary/` (200) | "the positions of the feet are standard in all methods" | verbatim, inside the "Positions of the arms" definition |

Extra (live pages): the S861, S863, S865, S866, S867 Gate quotes are all verbatim.

**Paragraph anchors.** `<p>` extraction gives each element's sequence as `Inscribed in YYYY…` line, then the narrative paragraphs:

| row | narrative paras | quote in narrative ¶ | anchor | counting the Inscribed line as ¶1 |
|---|---|---|---|---|
| S861 | 1 | 1 | ¶1 ✓ | 2 ✗ |
| S862 | 3 | 2 | ¶3 ✗ | 3 ✓ |
| S863 | 1 | 1 | ¶2 ✗ | 2 ✓ |
| S864 | 3 | 2 | ¶3 ✗ | 3 ✓ |
| S865 | 1 | 1 | ¶2 ✗ | 2 ✓ |
| S866 (live) | 1 | 1 | ¶1 ✓ | 2 ✗ |
| S867 | 3 | 1 | ¶2 ✗ | 2 ✓ |

The anchors read "inscription narrative, paragraph N", but no single convention reproduces them: 5/7 fail under narrative counting and 2/7 under Inscribed-line counting. This corroborates ScoutReopen's S861 finding and adds S866 on the live page, where there is no nomination-file block. **Severity: Low.** Quotes are verbatim; only the locators are non-reproducible. The fix is to declare one convention and correct the same cell in both SOURCES.md and the lesson Gate.

## Findings by severity

### Medium

**F1 — SWEEP leg can pass vacuously; the `danc` stem is dead.** `\b(danc)\b` cannot match "dance" (`echo '- topic: dance forms' | grep -ciE '\b(danc)\b'` → 0). The topic leg is `all(t.startswith(ENTRY+":") for t in topic_owners) and len(topic_owners) <= 1`, which is True on an empty list.
- Mutation M1 rewrites entry line 20 to `- topic: dance codes for invented cultures.`; result: SWEEP PASS, ACCEPT PASS.
- At HEAD, the entry is caught only by the token "performance".
- The pre-data correction (lesson line 46) traded a false positive ("avoidance") for a false negative.
- The claim itself survives a stem sweep: `grep -rniE '^- topic:.*\b(danc\w*|choreograph\w*|perform\w*)'` over culture-material finds only the entry and `ritual-garments.md:3` ("performative" vestments, not a register owner). Corroborates RevREADME R3.

**F2 — "NEW rows" is unenforced.** The docstring says ">=12 NEW SOURCES rows (S ids opened this round …)", but neither CITED nor ROWS checks `opened` or an id floor.
- M2 sets S861 opened to `2019-01-01`: PASS.
- M6 substitutes S873 with pre-existing S100 and rewrites S100's used-by to the entry: PASS.

**F3 — No leg binds an S-id to a body clause.** CITED counts any `S\d{3,}` token anywhere in the file.
- M4 strips every `(Sxxx)` from the body, leaving only the `- source:` header lines: PASS.
- At HEAD, **S873 is cited only in the header (line 15), never in the body.** Its row's "teaches" (definition/ephemerality debate) has no body content. The count would still be 12 ≥ 12 without it, so the leg outcome is unaffected, but the entry's line 21 implies all 13 support content.

### Low

**F4 — ROWS is not Registry-scoped, and duplicate rows resolve last-wins.** `ROW_RE` matches any table row in the file.
- M3 moves the S861 row below `## Leads (unopened)` (to line 925): PASS.
- M7 sets the Registry S862 row to `unopened` and appends a `mined` duplicate later in the file: PASS.

**F5 — USEDBY-PATHS is redundant by construction.** Once ENTRY and ROWS pass, used-by contains the existing ENTRY. The leg can only fail if used-by lists an additional, missing path. It adds no independent check for this claim.

**F6 — Exit-2 contract unimplemented.** The docstring promises "2 input error". M5 deletes the entry: legs ENTRY and COUNTS FAIL, then a `FileNotFoundError` traceback, exit 1. Also: `--lands` is parsed but unused, and the `corpus` variable (line 60) is dead.

**F7 — UNESCO paragraph anchors are inconsistent** (table above).

**F8 — The assimilation id-renumber map is stale against the landed rows.** `.ufo/waves/round-71/assimilation/id-renumber-map.json` was computed at `registry_count: 784` with `next_free: "S861"`.
- It maps staged S859→S861 … S871→S873, so its targets now land on the lane's own S861–S873.
- Staged ids S861–S873 (`staged-ids` lines 3–15) now also collide, yet `collisions` still lists only S859 and S860.
- Quarantine is CLOSED, so there is no live harm, but any adoption from this map would double-assign ids. Lesson line 73 cites the map as current. Route to RevQuarantine.

**F9 — The receipt's counter hash is stale at HEAD.**
- `measures-c.txt` records `counter sha256 (self): 1df995c2…`. That matches `accept-c.py` at 14c88d9 and ccadb59, but edd7895 changed the docstring, and HEAD's counter is `80b4ca09…`. Semantics are unchanged (docstring-only diff), but the hash no longer matches the file it describes.
- Earlier, the entry's `- recheck:` cited `reports/round-71/telemetry/measures-c.txt` as "commit receipts" while the file was untracked (absent from the 14c88d9 and ccadb59 archives). Commit c21213a fixed this; it is present at edd7895.

### Info

**F10 — `--root` resolves against the script's lane, not the cwd** (`root_abs` joins with `LANE`). Running `python3 -B /tmp/rc71c.Ig9l/reports/round-71/accept-c.py --root .` from `/tmp` graded `/tmp/rc71c.Ig9l/.`. A fresh-clone measurement is valid only if the clone's own copy is invoked, as done here.

## Mutation probe harness (reproducible)

Each probe copies the fresh tree to a throwaway dir, applies one `sed` edit, and runs the counter:

| probe | edit | result |
|---|---|---|
| M1 | entry line 20 → `- topic: dance codes for invented cultures.` | PASS (vacuous SWEEP) |
| M2 | S861 opened → 2019-01-01 | PASS |
| M3 | S861 row moved after `## Leads (unopened)` | PASS |
| M4 | strip ` (Sxxx)` from entry lines 22–EOF | PASS |
| M5 | `rm` entry | exit 1 with traceback (not 2) |
| M6 | S873 → S100 in entry; S100 used-by → entry | PASS |
| M7 | Registry S862 → `unopened`, `mined` duplicate appended | PASS |

## Residual risk / verification gaps

- Re-opened only the UNESCO/ABT rows. S869–S873 (RAD, ICKL, Wisdom Library ×2, SEP) were not re-fetched by this seat; ScoutReopen covers S871.
- The UNESCO live pages were fetched with a browser UA. ScoutReopen reported a CAPTCHA wall on the live pages, so the live content may vary by client.
- The paragraph convention is undeclared anywhere in the lane, so F7 cannot be resolved by evidence alone.
