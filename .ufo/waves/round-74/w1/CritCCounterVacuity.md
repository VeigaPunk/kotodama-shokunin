# CritCCounterVacuity — round 74 w1 — claim C predicate vacuity

Seat: CritCCounterVacuity (leaf; no delegation, no background jobs, no fetches).
Target: the twelve legs of claim C in `reports/round-74/claims.json` (status DRAFT,
`frozen: null`, base `f7104cbce186bc2e1522abf0cfd619cc834628bb`).
Reference implementation: `reports/round-73/accept-c.py` (sha256
`95aee88166023f4b0dc78cda5f0f3a769e94de476f5558bd6e33650922fea416` per
`.ufo/waves/round-73/w2/MutPredicateC.md`), and the round-73 wave-2 falsification
receipts `MutPredicateC.md` / `MutLandedC.md`. `reports/round-74/accept-c.py` does
not exist yet (only `claims.json` and `telemetry/` are present), so every verdict
below is against the *wording* of the draft legs, read through the r73 code paths
the r74 counter will inherit.

## Verdict

**Claim C as drafted is satisfiable end-to-end by a seat that never opens any of the
four pages.** The twelve legs bind the landing to itself: the URLs come from a map
the landing may rewrite, the quotes are checked against windows the landing authors,
and the digest is checked only for being 64 hex characters. Round-73 already
demonstrated each link of this chain against the r73 counter — P1 (filler entries),
P2 (staged rows laundered), P4 (invented quotes + forged captures), P6b (fabricated
reject row), P7a (rows cited by nobody), M10/M11/M17 (reject side, reason/flip word
presence, guard-proof debris), all `PASS legs=11/11`. The r74 draft adds wording that
kills the *literal* controls it names (a header-only stub fails the word floor; a
flag-only evidence file fails the window check), but the next-cheapest landing passes.
Three legs are genuinely load-bearing and none of them touches a source page: GROUND
(base-pinned, re-derived — I re-verified the four `before` numbers below), the ROWS
registry-diff shape, and FROZENCFG (if implemented as worded).

Two of the draft legs are also wrong in the opposite direction: as worded, ROWS and
REPOINTED **reject the honest landing** (C2 and C3 below). A predicate that both
admits junk and rejects the real artifact is not yet a predicate.

## Method and evidence base

- Read (read-only): `reports/round-74/claims.json` (claim C in full), the complete
  `reports/round-73/accept-c.py` (all 11 legs, `load_config`, `_map_url`,
  `leg_*`, `main`), `.ufo/waves/round-73/w2/MutPredicateC.md`,
  `.ufo/waves/round-73/w2/MutLandedC.md`, `.ufo/waves/round-74/w1/ScoutMapIds.md`,
  `.ufo/waves/round-74/w1/id-map-draft.json`, the two drafted entries under
  `.ufo/waves/round-74/drafts/`, `tools/check-cited-lines.py` (header contract), the
  staged rows in `/home/vgpnk/Projects/shokuknow/merge/kotodama/SOURCES.append.md`
  (read-only, no campaign tool run).
- Re-derived by execution against a materialized base tree
  (`git archive f7104cb | tar -x -C /tmp/ccv-base`): the claim's `before` block is
  **true** — `find corpus/knowledge -iname '*worldbuilding-setting*'` = 0;
  registry rows = **804**; rows naming `litmemo.com|tuduku.space|chinawriter.com.cn`
  = **0**; files containing `設定ノート|世界観|世界观` = **0**; the smallest knowledge
  entry at base is **478 words**
  (`corpus/knowledge/culture-material/heritage-taxonomy-models.amend-2026-10-24-r13.md`).
- No live fetch was made by this seat; no network. Everything about the pages comes
  from the seats' own records, which is exactly the weakness attacked below.

## The null-seat landing, leg by leg

One landing, composed as cheaply as the wording allows: two entries = nine-field
header + 479 words of neutral prose; four rows = staged bytes renumbered, dated
2026-10-25, recheck `180d`, escaped pipe stripped, anchor cell carrying a quote the
seat invents; a `## Gate` table with the same invented quote; four evidence files
carrying that quote plus a window containing it plus an arbitrary 64-hex digest; the
lesson naming the right frozen ids and files. Nothing is fetched.

| # | leg | cheapest junk that passes it | as worded, rejected? | mutant that survives | r73 reference |
|---|---|---|---|---|---|
| 1 | ENTRIES | nine-field header + 479-word filler body, zero quoted spans, zero CJK | **no** (the header-only stub is rejected — floor 478 — but filler is not) | filler body, or a body whose only "content" is a restatement of the header | P1 `PASS 11/11` |
| 2 | ROWS | staged rows renumbered + normalized; anchor cell holds an invented quote; used-by = the stub entries; source cell holds the frozen URL | **no** — every check is self-consistent shape | (a) a row cited by nobody with `used-by: —`; (b) **no** in-place change at all (S877 untouched) — "the only in-place change is X" is true of the empty set | P2, P7a, M06 |
| 3 | REPOINTED | `source:` lines cite S881..S884 with URLs copied from the map; inline ids omitted | **no** | (a) map rewritten at lands → ids name `example.org` documents; (b) inline `(S883)` on a litmemo sentence "resolves" to lane S883 = chinawriter, an unrelated document (C1) | P5b, M12/P7a class |
| 4 | GATE | four admit rows with invented quotes + locators + frozen URLs + date; one invented reject row naming S882 with a "probed" URL | **no** — nothing compares a Gate quote with a page | (a) quote not on the page (item control c); (b) fabricated reject row replacing the real ones | P4, P6b, M10 |
| 5 | EVIDENCE | flag + window + invented quote + arbitrary `sha256`; `quote-found-verbatim: yes` | **partly** — a file carrying *only* a flag fails (quote/window required); flag + forged window passes | (a) digest of a different body; (b) window that is a whitespace-normalized match rather than committed bytes; (c) quote nowhere on the page | P4 `PASS 11/11`, P3 |
| 6 | REJECTS | lesson prose names S882, S899, S900, every refused family, and the words "reason"/"flip"; per-row cells emptied | **no** as worded ("with reason and flip" — word presence, not per-row content) | reason+flip cells `—`; `x11` count copied from the staged package without re-derivation | M11, M10 |
| 7 | GROUND | — | **yes, rejects** | none found: the counter re-derives from the base tree; I confirmed 0/804/0/0. Only a landing that omits or miscounts the receipt fails | none |
| 8 | CITEDLINES | entries with `source:` lines only and zero inline ids → `CITED-LINES: 0 finding(s) in 2 file(s)` | **no** (vacuous 0 findings) | (a) zero-citation body; (b) replace `tools/check-cited-lines.py` at lands — line 903 reads the tool from the graded tree | r73 "Observations" |
| 9 | CENSUS | any structurally valid registry | **no** (passes junk by design) | a URL swap between rows (M03: census stayed green) | M03 |
| 10 | SCRATCHMIRROR | forged receipt text (`validate --file`, `exit 0`, four ids) in a commit before the append; mirror never validated | **no** as worded ("shows … exit 0 on the mirrored corpus") | receipt-only; mirror corpus ≠ the graded corpus | r73 `leg_scratch_mirror` (text grep only) |
| 11 | COLLCHECK | empty `reg-ids`/`collisions` + any file under `guard-proof/` holding an indented planted row and the word "collision" (fixture debris) | **no** | (a) delete `guard-proof.txt`, keep a mirror (M17); (b) no leg requires the counter to check the 4-space *not-found* side, only the prose does | M17 `PASS 11/11` |
| 12 | FROZENCFG | — (this is the anti-junk leg) | **yes for the literal control** (config edited in the graded tree) | (a) caller passes a friendlier `<freeze>` whose claims.json narrows `row_set`; (b) the **map** is not in claims.json, so it is still read from the graded tree; (c) the **tool** executed (`check-cited-lines.py`) is not pinned | P7b, F1 |

Composed landing: legs 1,2,3,4,5',6,8,9,10,11 green; only 7 (GROUND) and 12
(FROZENCFG) red — and neither can see whether a page was read.

## Structural counterexamples

### C1 — the lane/staged id namespaces collide numerically *after* adoption, so "no staged id cited as a lane row" has no operational meaning

`id-map-draft.json` records it: after adoption, lane S881 = litmemo = staged **S883**;
lane S882 = tuduku = staged **S884**; lane S883 = chinawriter 2025 = staged **S899**;
lane S884 = chinawriter 2022 = staged **S900**; and staged S882 = the Sidorova PDF =
lane S877. The drafted amend entry already cites `(S883)`/`(S884)` for chinawriter —
and those same tokens are campaign ids for litmemo/tuduku.

- REPOINTED's clause "no staged-namespace id (S882..S884 of the campaign, S899, S900)
  is cited as if it were a lane row" is therefore **either unsatisfiable** (the honest
  entry must cite lane S883/S884) **or vacuous** (S882/S883/S884 *are* registry rows,
  so the check cannot fire). Deleting the honest citation to satisfy it destroys the
  claim; keeping it means the check never runs on exactly the three ids it names.
- The identity defect it was meant to catch survives: a sentence about litmemo citing
  `(S883)` passes "every inline S-id resolves to one of those five rows" while naming
  chinawriter — an unrelated document under the same number.
- The `kill_rule` has the same defect: "any admitted entry cites a refused/unknown
  staged id" fires on the *honest* entry's `(S882)` (tuduku), because S882 is also the
  refused staged id of the Sidorova row. Read literally, the kill rule rejects the
  landing the claim describes.

### C2 — ROWS as worded rejects the honest landing on S877

Base row S877 carries `used-by = corpus/knowledge/linguistics/conlang-scholarship.md`
(verified: that file has `- source: S877` and 25 inline `S877` mentions). The draft
base entry also cites S877, and the claim's `after` says S877's used-by is "changed in
place old->new". Honest new value = `conlang-scholarship.md, worldbuilding-setting-practice.md`.
ROWS as worded requires "used-by exactly the admitted entries whose source: lines cite
it" = `{worldbuilding-setting-practice.md}` — dropping the pre-existing user, i.e. the
leg demands a **false registry cell**. Round-73's implementation adds a
`used-by union == both entries` check on top (`accept-c.py:658-659`), which widens the
same error. Meanwhile the empty case is unguarded: a landing that never cites S877
makes zero in-place changes and "the only in-place change is S877's used-by" is
vacuously true.

### C3 — the map and the tool are read from the graded tree

`_map_url` reads `RENUMBER_MAP` out of the materialized **lands** tree
(`accept-c.py:666-677`), and ROWS uses it to require "the map URL verbatim in the
source cell". A landing that rewrites the map's `url` fields and writes the same URL
into its rows and entries passes ROWS and REPOINTED with documents of its own choosing
— the exact "REPOINTED satisfied by ids that name unrelated documents" channel. FROZENCFG
says the "map" is read from claims.json at `<freeze>`, but **claims.json has no map
object**: `row_set` carries only `{id, staged}`, and the URLs exist only in the
`after` prose string. As worded the leg is unimplementable, and the natural
implementation falls back to the lands-tree map. The same hole exists for the executed
verdict tool: `leg_citedlines` runs `os.path.join(mat, "tools/check-cited-lines.py")`
(`accept-c.py:903`), so a landing can ship a tool that prints the required line.
(Code-read, not run — `reports/round-74/accept-c.py` does not exist yet.)

### C4 — `<freeze>` is a caller-chosen argument

FROZENCFG requires "read from claims.json AT the `<freeze>` commit" and "`<freeze>`
must be a strict ancestor of `<lands>`". Nothing binds `<freeze>` to the commit that
actually published claims.json, so a seat self-reporting PASS can pass a freeze whose
`row_set` is narrower, and the claim text's "adds exactly S881..S884" is then checked
against the narrower config (the class P7b exploited in r73, now moved from the
graded tree to the CLI). The draft also never says the map's digest, the counter's own
digest, or the leg count `n` are frozen — the r73 receipt prints a self-sha256 that
nothing compares (`print_receipt`, `accept-c.py:1135-1137`).

### C5 — the quote triangle has no external anchor

ENTRIES ↔ ROWS anchor ↔ GATE ↔ EVIDENCE all draw from files the landing authors.
EVIDENCE's new clause ("the counter checks the Gate quote occurs inside that stored
window") closes the flag-only file, not forgery: the forger writes the window, so it
contains whatever quote the forger chose. r73 P4 proved exactly this
(`PASS 11/11` with five invented quotes and forged captures). No offline counter can
prove a live page said a sentence; the honest fix is to make the commitment
**byte-level and re-derivable** (committed window text + digest recomputed from those
bytes) and to state in the claim that the offline counter proves capture-internal
consistency, live re-verification being a separately declared step. Requiring an
archive copy unconditionally would make the claim unprovable: `ScoutLitmemo.md:114`
records CDX has **no capture** of the litmemo slug (positive controls returned rows),
so a dual-capture requirement must be conditional on the row naming an archive URL.

## Ranked tightenings (8), exact wording

Ordered by surviving-landing cheapness × blast radius on the verdict: T1–T3 close
channels that make every other leg's PASS meaningless (frozen inputs, identity, the
quote-to-page bridge); T4–T6 close the specific junk controls the claim names; T7–T8
close receipt forgery and guard-proof debris.

Each is a drop-in replacement for the named draft leg. "Provable" notes what in the
honest landing already satisfies it.

### T1 — FROZENCFG (closes C3, C4, P7b, the config-edit control)

> FROZENCFG: `<freeze>` is derived, not passed — the counter requires exactly one
> commit reachable from `<lands>` that introduced `reports/round-74/claims.json`
> (`git log --diff-filter=A`), requires it to be a strict ancestor of `<lands>`,
> requires that commit's name-status to add `claims.json`, `ledger.json`,
> `accept-c.py`, `accept-ca.py` and `telemetry/controls-c{,a}.txt`, requires
> `status: FROZEN` (not DRAFT), requires claims.json byte-identical at `<freeze>` and
> `<lands>`, and reads from `<freeze>` only: `counter_sha256` (the running counter's
> self-digest must equal it), `legs_n`, `row_set[].url`, `reused_rows[].id`,
> `map.path`/`map.sha256` (the map is read with `git show <freeze>:<map.path>`, its
> digest equal at `<lands>`), and the pinned digest of every program the counter
> executes. A caller-supplied `--freeze` is a usage error.

Provable: the freeze commit is created by the integrator and adds exactly those
paths by the claim's own freeze rule; `row_set` URLs are pre-data knowledge
(`id-map-draft.json` already holds them); the counter's digest is computed after the
counter is frozen.

### T2 — REPOINTED (closes C1, C3; kills P5b, the unrelated-document channel)

> REPOINTED: every `source:` line carries exactly one id whose `url` in the frozen
> `row_set` equals the line's URL (scheme/host/path after neutralization); every
> inline `S\d{3,}` occurrence resolves to one of the five lane rows; in every
> blank-line-delimited paragraph that carries both an inline id and a quoted span,
> each quoted span occurs (whitespace-normalized) in the evidence window of at least
> one id cited in that paragraph; a campaign id may appear only inside a
> `staged:`-prefixed span (`staged:S899`), so a bare `S899`/`S900` fails, and a bare
> `S882`/`S883`/`S884` is judged by the frozen row URL — a staged id used as a lane
> id fails **by document**, not by number; a token matching `(?i)\bs\d{3,}\b` in any
> non-canonical case is a failure.

Provable: both drafts already pair quotes with ids in the same bullet
(e.g. `「我先做的是世界观…」 (loc: ¶67) (S883)`), and every cited row has a frozen URL.

### T3 — EVIDENCE (closes C5, P4, the flag-only control)

> EVIDENCE: per adopted row, `reports/round-74/evidence/<id>.txt` records
> `access-date: 2026-10-25`, `http-status: 200`, the browser-shaped UA, `body-bytes`,
> `body-sha256`, `text-sha256`, `window-offset` and `quote`; the bytes the quote is
> located in are committed as `evidence/<id>.text` (raw body, or the extraction with
> its extractor command and the raw digest recorded); the counter recomputes
> `text-sha256` over the committed file, requires `quote` to be an exact byte
> substring of it starting at `window-offset`, and requires the Gate admit row's
> quoted span and the row's anchor span to equal `quote` (whitespace-normalized);
> where the row's source cell names a `web.archive.org/…id_/…` capture,
> `evidence/<id>.archive.text` is also committed and must contain `quote`.
> `quote-found-verbatim` is never read as evidence.

Provable: the scouts already hold the bytes and digests (`ScoutLitmemo.md:21-31`:
101,615 bytes, `sha256 441fc9…`, visible-text `sha256 82454e6c…`); committing a text
window is cheap; the archive clause is conditional precisely because no capture exists
for the litmemo slug (`ScoutLitmemo.md:114`). The claim should also state that the
offline counter proves capture-internal consistency, not live-page truth.

### T4 — GATE and REJECTS (kills P6b, M10, M11; item control c)

> GATE: the `## Gate` table holds exactly one admit row per adopted row and no other
> admit row; each admit row carries the frozen row URL, `2026-10-25`, a non-empty
> locator and one quoted span equal to that row's evidence `quote`; the S883 and S884
> rows each carry a cell naming the staged id (`S899`, `S900`), the mispairing reason,
> and the located replacement span equal to the evidence quote.
> REJECTS: exactly one refuse row per item in `rejects.refused_staged_not_appended ∪
> rejects.refused_files`, each naming the item verbatim with a probed URL and
> non-empty reason and flip cells (not `—`, not placeholder); each `refused_files`
> count (`x3`, `x11`, …) equals the number of files that family matches in
> `corpus/knowledge` at `<lands>`; no `not adopted` filename appears outside that set.

Provable: the frozen lists already fix the item names; the counts are re-derivable
with `ls`/`glob`; the honest Gate already has per-row URL + locator + quote.

### T5 — ROWS (closes C2; kills P2, P7a, M06, the empty in-place set)

> ROWS: base..`<lands>` adds exactly S881..S884 contiguously and removes none; each
> row is status `mined`, opened `2026-10-25`, a cadence-only recheck cell, carries no
> literal or escaped pipe in any cell, carries the frozen row URL verbatim in the
> source cell and the evidence `quote` as a quoted span (QUOTE_RE) in the anchor cell,
> and a used-by cell equal to the set of admitted entries whose `source:` line cites
> it — non-empty for every S881..S884, and for S877 equal to its **base cell ∪** the
> entries citing it; no cell carries a date other than 2026-10-25; and base..`<lands>`
> makes exactly one in-place registry change — S877's used-by — whose old value is the
> base cell and whose old→new pair appears verbatim in the lesson.

Provable: the base cell is `corpus/knowledge/linguistics/conlang-scholarship.md` and
the claim itself says old→new; the drafted entries quote each source.

### T6 — ENTRIES (kills P1, the filler/stub control)

> ENTRIES: both files exist at `<lands>`, absent at base, with the nine-field header
> first and no placeholder value; each body carries at least as many words **outside
> quoted spans** as the smallest knowledge entry at base (478 at base `f7104cb`), at
> least one quoted span per cited row that occurs in that row's evidence window, and
> at least one inline id per cited row outside the header.

Provable: the drafts measure 3,495 and 1,304 non-quote words with 24 and 37 quoted
spans (measured: `python3` QUOTE_RE over the draft bodies), and each cited row already
appears in a quoting bullet.

### T7 — SCRATCHMIRROR (receipt text is never the verdict)

> SCRATCHMIRROR: the counter materializes the tree at the receipt's introductory
> commit, runs the census `validate --file` on
> `.ufo/waves/round-74/assimilation/validate/corpus/SOURCES.md` itself and requires
> exit 0, no E-codes and S881..S884 present; the mirror's two entry files are the same
> blobs as at `<lands>`; the receipt commit is a strict ancestor of the commit that
> first adds S881 to `corpus/SOURCES.md`; receipt text is not read as a verdict.

Provable: `validate/` already holds a mirrored corpus and the receipt draft; the
ordering relation is already computed by git.

### T8 — COLLCHECK (kills M17; keeps the guard proof from being satisfied by debris)

> COLLCHECK: `guard-proof/guard-proof.txt` carries the three lines `2sp found=1`,
> `3sp found=1`, `4sp found=0`; the counter re-derives each by applying the census row
> regex to the committed `guard-proof/mirror-{2sp,3sp,4sp}/corpus/SOURCES.md` bytes
> (indent 1–3 detected, indent 4 not) and requires the values to match; `reg-ids`
> lists no adopted id and `collisions` none; the map read at `<freeze>` holds exactly
> one `old -> new` per adopted id, no target that is also an old id (single-pass
> substitution), and a `url` for each adopted target equal to the frozen
> `row_set[].url`.

Provable: the three mirror dirs and `run-guard.sh` already exist; the map draft
already carries URLs; the "no target that is also an old id" rule is the draft map's
own `substitution_rule`.

## What I could NOT check

- The round-74 counter does not exist yet, so no junk landing could be graded against
  the r74 wording. Every "as worded" verdict is a reading of the leg text through the
  r73 code paths it must inherit; where I claim a code behavior I cite the r73 line.
- No live fetch, no Wayback probe: whether the r74 quotes are on the pages is not
  this seat's ground (w1 scouts hold it). C5 attacks the *proof structure*, not the
  facts.
- The r73 selftest's 24 mutants were not re-run, and I did not enumerate which of them
  survive the r74 wording.
- Claim Ca, the ledger and `accept-ca.py` are outside this item.
- I did not test whether census emits a new E-code for any r74 row shape; only the
  r73 M03/M05 observations are cited.

## Bounds and tooling

- Writes: this report file, and `/tmp/ccv-base/` (a materialized base tree used
  read-only for the `before` counts). Nothing else was written: no lane tracked file,
  no index/jj state, no fleet repo, no shokuknow, no `scripts/`/`templates/`, no
  `.ufo/state`, no `LOG.md`/`SCORECARD.md`/`SKILL.md`, no `corpus/SOURCES.md`, no
  claims.json.
- Lane git was read only (`git show`, `git archive`, `git ls-tree`, `git status`);
  the six uncommitted round-73 w2 seat files and the untracked round-74 scaffolding
  were left untouched.
- Nothing installed; pacman not run; no network and no downloads; no subagents, no
  background jobs, no peer messages.
- `/home/vgpnk/Projects/shokuknow/merge/kotodama/SOURCES.append.md` was read only; no
  campaign tool was run there.
