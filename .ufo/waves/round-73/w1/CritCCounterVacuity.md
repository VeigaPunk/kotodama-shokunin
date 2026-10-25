# CritCCounterVacuity — does claim C's predicate reject anything? (round 73, w1)

- Seat: CritCCounterVacuity (leaf critic; no delegation, no background jobs, no repo mutation).
- Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin` (read-only for this seat).
- Target: `reports/round-73/claims.json` claim C (`legs` at lines 17–26, `kill_rule` at 28, `do_nothing_control` at 29) — DRAFT-v0, not edited.
- Reference implementation: `reports/round-72/accept-c.py` (803 lines, sha256 `355e67f1bdb15d52368ad454d68d8391fd72d1de59622570689c4822d21da3c1`). `reports/round-73/accept-c.py` **does not exist at base** (`ls` → No such file); the round-73 counter is built in wave 2 from the round-72 one, so the round-72 leg functions *are* the predicate's executable meaning today.
- Date: 2026-10-25. Tools: none installed (python3 3.14.8, git 2.56.0, curl 8.23.0 already present; PACMAN untouched).

## 0. Verdict

**Claim C's predicate is currently satisfiable without opening a single page.** I built a landing that no honest seat would file — two 50-word header-only stub entries, five rows copied out of the staged package, invented Gate quotes, two handwritten receipts, a fabricated `staged-ids` file, an inline campaign id `S728` — and a minimally re-parameterised port of the round-72 counter prints:

```
LEG PASS ENTRIES / ROWS / REPOINTED / GATE / REJECTS / GROUND / CITEDLINES / CENSUS / SCRATCHMIRROR / COLLCHECK
ACCEPT-C-73MUT: PASS legs=10/10
```

The real `scripts/sources-census.sh validate --file` also exits **0** on the census-clean form of that landing (`file ok …`, two W03 warnings only) — the form E09 forces by rejecting the staged recheck cell. So CENSUS does not close it either.

**Eight of ten legs are vacuous against junk**: ENTRIES, ROWS, REPOINTED, GATE, REJECTS, GROUND, SCRATCHMIRROR, COLLCHECK all survive variants that differ only in which fabrication they use (§3). **CENSUS is partial** — it enforces field count, status enum, recheck grammar and used-by existence, but reads the worktree rather than `<lands>` bytes. **CITEDLINES is narrow** — it prints `0 finding(s)` on a citation-free entry. Only the **base-only** do-nothing control genuinely rejects (nine legs fail).

The claim is not unprovable — every tightening in §5 is decidable from committed bytes plus the read-only staged package. But as worded, "PASS legs=10/10" would certify a fabricated landing.

**Impacted axes.** *Coverage* (primary): C is the coverage claim, and a predicate that passes a fabricated landing lets the coverage axis move on unopened sources. *Calibration* (secondary): the unbound-receipt class is exactly round-72's R2 (a verdict filed against bytes that do not say it), and the worktree-vs-lands substitution is a new instance of the same class; Ca's `STAMP` leg is stronger, but any counter ported from `accept-c.py` inherits the CENSUS hole.

**Smallest safe correction.** Two predicate edits do most of the work — T2 (ENTRIES non-placeholder + body citation) and T5's capture binding (GATE quote must occur in a committed capture) — because they are what makes the cheapest junk landing (stub entries, invented quotes) fail. T1 (committed selftest controls) is the smallest *enforcement* that keeps T2–T8 from silently weakening later.

## 1. Method

I attacked each leg by constructing the cheapest landing that satisfies its *letter*, then ran the reference counter on it. The counter is a **port**, not the round-73 file: I copied `reports/round-72/accept-c.py` to `/tmp/CritCCounterVacuity/accept-c-73mut.py` and changed only:

| # | patch | why forced |
|---|---|---|
| 1 | `LESSON`/`ASSIM`/`RECEIPT`/`GROUND_RECEIPT` → round-73 paths | paths are hardcoded |
| 2 | `ENTRIES` → `corpus/knowledge/linguistics/conlang-scholarship.md`, `…amend-2026-10-23.md` | hardcoded |
| 3 | `NEW_IDS` → `S876..S880` | hardcoded |
| 4 | `registry_sweep` → the five domain fragments | `ihchina`/`bunka` are now *live* rows at base (S874/S875), so the unpatched sweep returns 1/1 and GROUND fails a correct landing |
| 5 | GROUND receipt token `797`→`799`, tokens → five domains, base sweep → all-zero | same |
| 6 | REPOINTED floor `874`→`876` | claim floor |
| 7 | REJECTS tokens → `S869`, `S894`, `S910`, `naming-systems`, `calendar`, `era`, `verification` | round-73 refusal set |
| 8 | SCRATCHMIRROR `-S S874`→`-S S876`, receipt must carry all five ids; banner `ACCEPT-C-73MUT` | round-73 ids |

No other logic changed. `--selftest` was not run (its fixtures are round-72 hardcoded). The census leg accepts `--census-sh`, so for the variant matrix I used a stub; for the decisive fixture I *also* ran the real script (§2.3, §8).

Fixtures: one `mktemp -d` repo per variant under `/tmp/CritCCounterVacuity/`, `git -C <D>` on every call, fixture-only identity `-c user.name=fixture -c user.email=fixture@local`. Nothing was written to the fleet root, the lane, or shokuknow.

## 2. The counterexample

### 2.1 Composition of the junk landing (`/tmp/CritCCounterVacuity/junk-84jKiv`, lands `a55cd5f0`)

- **ENTRIES** — two files, 15 lines each, 50 and 52 words (`wc -w`). The pre-`##` block is the nine labels with `—` values; the body is one sentence. Entry 1 cites `S876` and carries `(S728)` inline; entry 2 cites `S877`.
- **ROWS** — the five staged rows from `SOURCES.append.md:29,30,40,41,49` (`S881/S882/S892/S893/S901`), with: the id cell rewritten to `S876..S880`; the escaped pipe `\|` replaced by `;`; the `recheck` cell reduced to `180d`; `used-by` set to *both* entries on every row. Every other cell — `scope`, `anchor`, `teaches` — is the staged text **verbatim**, and `opened` is the staged `2026-10-23`.
- **GATE** — five table rows with access date `2026-10-25` and the invented quote *"constructed languages replace natural-language data in every linguistics curriculum"* (9 words). Per-row URLs are absent; the five URLs sit in a footnote paragraph. Two reject rows carry the literal cells `reason: held` / `flip: reopen`.
- **REJECTS** — prose naming `S869`, `S894/S910`, `naming-systems`, `calendar`, `era`, `verification`, and the word "refused". No per-entry reason/flip row.
- **GROUND** — `reports/round-73/telemetry/gap-sweep.txt`, handwritten: `at the 799-row registry:` + five `… rows: 0` lines. The fixture's base registry has **4 rows**.
- **SCRATCHMIRROR** — `.ufo/waves/round-73/assimilation/validate-receipt.txt`, handwritten: `census validate --file …`, `exit 0`, `rows present in mirror: S876 S877 S878 S879 S880`. No mirror exists.
- **COLLCHECK** — `collisions` empty; `staged-ids` **fabricated** to contain `S881 S882 S892 S893 S901` *and* `S876..S880`; no planted-collision proof; no regenerated map; `.ufo/waves/round-71/assimilation/id-renumber-map.json` written once at base and never touched.

### 2.2 The quote really is not on the page

I fetched the S876 document's landing page once, browser-shaped UA (QUALITY 21/22):

```
curl -sS -o fetch/ojs7099.html -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36' \
  'https://ojs.unito.it/index.php/ricognizioni/article/view/7099'
HTTP_STATUS=200 BYTES=30289 CT=text/html; charset=utf-8   sha256 e7260b49…9369c
```

The abstract is on that page (`marginalize` ×2, the abstract paragraph extracts cleanly). Against the extracted text:

- invented Gate quote — **0 occurrences**;
- a real abstract sentence ("the construction of languages by students allows them to better grasp the reality of linguistic analysis", 16 words `wc -w`) — **1 occurrence**.

So the Gate records a 9-word "quote" that is provably absent from the page it attributes it to, and the counter passes it. No leg compares a quote to any capture; `leg_gate` only counts `len(span.split()) <= 25`.

### 2.3 The real census also passes it

`junk_census_clean` (same landing, `recheck` = `180d`, `opened` still the staged `2026-10-23`):

```
cd <fixture> && /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --file corpus/SOURCES.md --today 2026-10-25
file	W03	S001 mined but unused
file	W03	S728 mined but unused
file	ok	<fixture>/corpus/SOURCES.md
CENSUS_EXIT=0
ACCEPT-C-73MUT: PASS legs=10/10
```

Note the interaction: census **E09** rejects the staged recheck cell (`180d — `curl … | grep -c …` -> 2 (ran 2026-10-23)`), so the cheapest way to make a staged-copied row census-clean is to **delete the staged recheck command** — the provenance the row is supposed to carry. E01 rejects the escaped pipe (verified: appending a raw staged row gives `E01 S881 fields=12` plus `E11 … missing used-by grep -c 'marginalize'` -> 2 (ran 2026-10-23)`). Those two rules are the only teeth against "appended as-is".

## 3. Leg-by-leg: cheapest junk landing, and what a mutant survives

Legend: **PASSES** = the leg as worded is satisfied by junk; **PARTIAL** = only a mechanical sliver is enforced.

### ENTRIES (claims.json:17) — **PASSES**
Cheapest: two header-only files whose nine labels carry `—`.
Mutant (`leg_entries`): `header_field_names` over lines before the first `##`; no value check, no body check, no "added by this round" check.
Survives: placeholder values (fixture PASS); entries present at base (`entries_at_base` variant → **PASS 10/10**); a 50-word file whose body is one sentence. The leg says "exist at `<lands>`", so a file committed in an earlier round also satisfies it.

### ROWS (claims.json:18) — **PASSES** (four independent ways)
Mutant (`leg_rows`): `added == set(NEW_IDS)`; `removed` empty; `cells[8] == "mined"`; `used_by ⊆ ENTRIES`; `union == ENTRIES`.
Survives:
1. **used-by ≠ the citing entry** — rows S878/S879/S880 are used-by both entries while *nobody* cites them (only S876/S877 are cited); `union == ENTRIES` holds, `⊆` holds → PASS. "each used-by naming exactly the admitted entries that cite it" is not implemented.
2. **in-place mutation of an unrelated base row** — `row_mutation` rewrites S001's `teaches` cell in the lands commit → **PASS**; the id sets are identical, so "no other registry row added or removed" does not cover modification (which the registry contract allows only for `status`/`recheck`/`used-by`, logged old→new).
3. **duplicate-id shadow row** — `shadow_row` appends `| S001 | SHADOW junk … |` at the table end; `parse_rows` is a dict, so the duplicate collapses and the *last* line wins → **PASS**. A shadow row silently replaces what every other leg sees for that id.
4. **staged rows kept in substance** — `opened` stays `2026-10-23`, `scope`/`anchor`/`teaches` stay staged bytes → PASS. "no row is the staged text appended as-is" is enforced nowhere; census only forces the `recheck` command out (E09).
Also: `rows_only` (rows, no entries at all) **passes ROWS** — used-by paths need not exist; only census E11 notices, and only if the real script runs.
Also: "row set fixed at freeze" is not derivable from the frozen bytes — the claim names `S876` as a floor but never enumerates the set, so a counter must hardcode it, and "one per source the two entries cite" is **circular** (the entries define the source set).

### REPOINTED (claims.json:19) — **PASSES** (two ways)
Mutant (`leg_repointed`): only `source:` lines in the header block; exactly one id per line; `num >= 876`; id present in the registry; cited URL normalises equal to one of `row_cells(...)[2]`'s URLs.
Survives:
1. **inline campaign ids** — the fixture entry carries `(S728)` on a body line and passes; no leg scans body ids. `S769`/`S806` would pass identically.
2. **ids naming unrelated documents** — `unrelated_doc` binds entry and row to `https://junk.example/not-the-enguehard-article` (both sides rewritten) → **PASS 10/10**. URL equality is the *only* join; nothing ties a lane row to the staged document the scout verdict approved. The staged→lane map is not in the predicate at all, so `S881→S877` (wrong document) would pass as long as entry and row agree.

### GATE (claims.json:20) — **PASSES**
Mutant (`leg_gate`): per-id Gate row exists; `2026-10-25` in that row; ≥1 quoted span ≤25 words (`split()`); the row's URL appears *somewhere* in the Gate section; ≥1 row whose last cell contains `admitted`, ≥1 with `rejected`; the words `reason` and `flip` appear anywhere in the section.
Survives: a quote absent from the page (§2.2); no locator at all; URL only in a footnote; `gate_noreason` (reject cells `—`/`—`, with "reason"/"flip" elsewhere) → **PASS**; the QUALITY-21 "probed URL" requirement is never checked. `--selftest`'s gate mutants cover only an over-25-word quote and a deleted reject table — not an absent quote, an off-row URL, or empty reason/flip cells.

### REJECTS (claims.json:21) — **PASSES**
Mutant (ported): token presence for `S869`/`S894`/`S910`/`naming-systems`/`calendar`/`era`/`verification` + one of `refused|rejected|quarantine` anywhere in the lesson.
Survives: prose-only naming with no reason/flip; the S894/S910 clause is **conditional** ("if their payload stays unreachable by ordinary means"), so a landing that files no probe verdict leaves it vacuously satisfied; no set equality against the staged theme's entry list, so a theme entry that is neither admitted nor refused is invisible.

### GROUND (claims.json:22) — **PASSES**
Mutant (`leg_ground`): receipt contains `799` and a `0` on each domain-token line; the base registry re-sweeps to 0 for the tokens.
Survives: a **handwritten** receipt (no binding to any run); the receipt committed in the **same** commit as the data (`ground_same_commit` → **PASS**; only SCRATCHMIRROR has an ordering check); the "799-row" claim with a 4-row base (the counter never counts rows). The one real check — base sweep 0 — is genuine and worth keeping.

### CITEDLINES (claims.json:23) — **PASSES** (vacuously)
Mutant: runs `tools/check-cited-lines.py` and requires `0 finding(s)`.
Survives: entries with **no citations at all** — the fixture's two stubs print `CITED-LINES: 0 finding(s) in 2 file(s)`, exit 0. A single inline `S728` is not a finding (the tool flags only ≥2 ids per line and ids in table rows). So the leg certifies "no multi-id line", not "cites its sources".

### CENSUS (claims.json:24) — **PARTIAL**
Mutant (`leg_census`): runs the census script in the **worktree** and requires exit 0 and `HEAD == lands`.
Survives: **dirty worktree**. I committed a clean lands, appended a `JUNK-MARKER` line to the worktree registry only (`git status --porcelain` → ` M corpus/SOURCES.md`; `git show <lands>:corpus/SOURCES.md | grep -c JUNK-MARKER` → 0), and ran with a census stub that requires the marker: `LEG PASS CENSUS … exit=0 head=f4d2f92…` → **PASS 10/10**. The leg validates bytes that are not `<lands>`'s bytes, while every other leg reads `git show <lands>:`. A landing could commit clean rows and leave junk (or the reverse) and still pass.
What it *does* enforce (real script): E01 field count, E07 status enum, E09 recheck grammar, E11 used-by existence, E02/E03 ids. That is real but structural.

### SCRATCHMIRROR (claims.json:25) — **PASSES**
Mutant: receipt text contains `--file`, `exit 0`, the new ids; the receipt's introducing commit is an ancestor of the commit that introduces `S876` and is not that commit.
Survives: a handwritten receipt naming a mirror that never existed and a census that never ran. The ordering half is genuine and should be kept; the content half proves nothing.

### COLLCHECK (claims.json:26) — **PASSES**, and the naive port is itself defective
Mutant (round-72 `leg_collcheck`): `collisions` has no id tokens; adopted ids absent from `reg-ids`; **`NEW_IDS ⊆ staged-ids`**.
Survives: empty collisions file with no planted-collision proof, no regenerated map, the round-71 map untouched. Worse, the ported check *requires the lane ids to appear in `staged-ids`* — which is false provenance for round 73 (staged namespace `S881..S901` vs lane `S876..S880`; the three namespaces join by URL only). The cheapest way to satisfy it is exactly what the fixture does: fabricate `staged-ids` with both namespaces. A faithful port therefore either **fails an honest landing** or **passes a fabricated id file**. The claim's own `staged S881/S882/…` text contradicts the check.

## 4. The do-nothing controls are under-powered

| control | result | comment |
|---|---|---|
| lands == base (`base_only`) | **FAIL** (9 legs; CENSUS passes) | works, but CENSUS cannot distinguish base from lands — expected |
| rows only, no entries (`rows_only`) | **FAIL** (ENTRIES, REPOINTED, CITEDLINES) | **ROWS passes** — the "junk-row control" is not caught by the row leg; it fails on legs that never look at rows |
| **stub-entry landing** (missing control) | **PASS 10/10** | the landing a rushed seat would file |
| **unrelated-document landing** (missing) | **PASS 10/10** | entry and row agree on a URL nobody opened |
| **dirty-worktree landing** (missing) | **PASS 10/10** | CENSUS reads non-lands bytes |
| **same-commit GROUND receipt** (missing) | **PASS 10/10** | "receipt committed before data" unchecked for GROUND |

"receipts committed before dispatch of wave 2" is itself unchecked: no leg reads a dispatch timestamp, and no receipt records one.

### kill_rule audit (claims.json:28)

The rule names four artifacts: a quarantine-REFUSED staged row cited, a campaign id naming an unrelated lane document, a Gate record missing (access date 2026-10-25 + located quote), and "any staged row appended as-is (un-normalized recheck cell, escaped pipe, used-by not exactly the admitted entries)".

| named artifact | enforced by | verdict |
|---|---|---|
| campaign id (`S728`/`S769`/`S806`) in an entry | **nothing** — only `source:` header lines are scanned; the fixture's inline `(S728)` passes | hole |
| Gate record missing a located quote | `leg_gate` counts words only; "located" is not parsed; a quote absent from the page passes | hole |
| un-normalized recheck cell | census **E09** (real script) | enforced |
| escaped pipe | census **E01** (real script) — and E09 also fires on the shifted cell | enforced |
| used-by not exactly the admitted entries | `leg_rows` checks `⊆` and union, **not** "the entries that cite it"; rows S878–S880 cite nobody and pass | hole |

So two of the five artifacts in the kill rule have no check at all, and one ("used-by not exactly the admitted entries") is only half-checked.

## 5. Ranked tightenings (exact wording)

Ordered by survivors closed per unit of new machinery. Each is decidable from committed bytes at `<lands>` plus the read-only staged package; none requires a live fetch at judgement time.

**T1 — CONTROLS (closes the whole class at once).**
> `CONTROLS: reports/round-73/accept-c.py --selftest builds four throwaway repositories (base-only, rows-only, stub-entry, unrelated-document) and prints SELFTEST: 4/4, where stub-entry fails ENTRIES, ROWS, REPOINTED and GATE by name, rows-only fails ENTRIES and REPOINTED, unrelated-document fails REPOINTED, and base-only fails every leg but CENSUS; a fixture that passes a leg it is declared to fail makes that leg fail.`

The machinery already exists in the round-72 selftest; I built all four fixtures by hand and know the expected verdicts. This is the only tightening that keeps the others honest.

**T2 — ENTRIES substance (closes header-only stubs, entries-at-base).**
> `ENTRIES: both files are absent at base and added by the diff base..<lands>; each carries the nine header fields with a non-placeholder value (not empty, "—", "TODO", "n/a"); each has a body (lines after the first "##") of at least the word count of the smallest corpus/knowledge entry at base (478 at 8841ad3, recomputed by the counter); and every id named on a source: line appears at least once in the body on a line carrying no other S-id.`

**T3 — ROWS exactness (closes staged-copy, used-by mismatch, shadow rows, in-place mutation, circular row set).**
> `ROWS: the added ids equal exactly the target set of the map committed before data at .ufo/waves/round-73/assimilation/id-renumber-map.json (per staged row: staged id, staged URL, lane id, sha256 of the staged teaches cell); every added row carries the staged row's URL verbatim in its source cell (archive captures may be added), opened = 2026-10-25, a recheck cell that is a cadence token only, an anchor cell containing that id's Gate located quote, and a teaches cell whose sha256 differs from the map's staged teaches sha256; its used-by set equals exactly the admitted entries whose body cites that id; git diff --word-diff base..<lands> -- corpus/SOURCES.md changes no line of the base table and no id occurs twice in the registry.`

**T4 — REPOINTED whole-entry + COLLCHECK namespace integrity (closes inline campaign ids, unrelated documents, fabricated staged-ids, unproved guard, stale map).**
> `REPOINTED: every S-id token in both entries, header and body, is a lane id in the map's target set, present in the registry at <lands>, and outside the campaign-id blacklist {S728, S769, S806}; each source: line carries exactly one id and at least one URL, and every URL it carries is one of that row's URLs. COLLCHECK: the map records old→new for every adopted id; .ufo/waves/round-71/assimilation/id-renumber-map.json is byte-identical base..<lands>; the collisions receipt shows a planted collision at 3-space indent (found) and at 4-space indent (not found) before the empty real list, and carries zero adopted-id tokens; staged-ids lists the staged namespace (S881/S882/S892/S893/S901) and is never required to contain a lane id.`

**T5 — GATE capture-bound quote (closes invented quotes, missing locator, off-row URL, prose reason/flip).**
> `GATE: each new row's Gate table row carries, in that same row, the row's URL, access date 2026-10-25, a locator naming a heading/page/line, and a quoted span of at most 25 words (wc -w); the span occurs verbatim in a committed capture at reports/round-73/evidence/<id>.txt whose sha256 and fetch line (URL + exact User-Agent) are recorded in the row; the section records at least one admit and one reject from the assimilation set, each with a non-empty reason cell, a non-empty flip cell and the probed URL(s) in that same row.`

**T6 — REJECTS set equality and probe verdicts (closes prose-only refusals and the vacuously-true S894/S910 clause).**
> `REJECTS: the lesson's reject table carries exactly one row per staged entry of the conlang theme (the file list whose sources: cite a staged conlang id), with that filename, its staged ids, the probed URL(s), a non-empty reason cell, a non-empty flip cell and a verdict in {refused, not-adopted-this-round}; the row set equals the staged theme's entry set. For every staged id the theme cites, the lesson carries a probe verdict REACHABLE or UNREACHABLE with the probed URL, so no refusal condition is vacuously true.`

**T7 — GROUND + SCRATCHMIRROR bound to a recomputation (closes handwritten receipts, same-commit receipts, the uncounted 799).**
> `GROUND: the receipt's introducing commit is a strict ancestor of the commit that introduces the first adopted row; the counter recomputes at base that corpus/SOURCES.md has exactly 799 rows and 0 matches for each of the five domain tokens and that the receipt's numbers equal the recomputation. SCRATCHMIRROR: the receipt records the sha256 of the mirrored registry and the exact census stdout; the counter rebuilds the mirror from git show <base>:corpus/SOURCES.md plus the added rows, recomputes both sha256 values, and requires equality.`

**T8 — CENSUS at lands bytes (closes the dirty-worktree substitution).**
> `CENSUS: the counter materialises git show <lands>:corpus/SOURCES.md and every path its used-by cells name into a temporary tree, runs sources-census.sh validate --file on that mirror, requires exit 0 with no E-codes, and requires git -C <root> status --porcelain to be empty at <lands>.`

### Pre-freeze claim-text fix (not a leg, but the predicate depends on it)
`claims.json` never enumerates the adopted ids or the staged→lane map; `ROWS` says "row set fixed at freeze from the wave-1 scout verdicts" and `REPOINTED` says "re-pointed by document", neither of which is derivable from the frozen bytes. Before freeze, `before`/`after` must carry the five pairs (`S881→S876`, `S882→S877`, `S892→S878`, `S893→S879`, `S901→S880`) with their staged URLs, or T3/T4 have no referent. (The tentative map is consistent with `ScoutMapIds.md` §3; I did not re-derive it — not my seat.)

## 6. Residual risk after all eight

- A **forged capture** still passes T5: committing `evidence/<id>.txt` with a plausible UA line and a sha256 proves consistency, not that the fetch happened. The defence is auditability, not truth; a critic seat should spot-check one capture per round against the live page (as I did for S876's landing page).
- **Semantic relevance** of a row to the theme is not decidable mechanically; T3's URL equality to the staged row is the strongest local proxy.
- T3's `opened = 2026-10-25` is a *policy* choice (the claim's Gate leg already requires that access date); it makes a staged-copied `2026-10-23` fail, which is the point.

## 7. Honesty notes

- `reports/round-73/accept-c.py` does not exist; every "PASS/FAIL" in §3 is from my port (`sha256 4eebfe64…f55b28`). A wave-2 counter that differs from the port could behave differently; the port's patches are listed in §1 so they can be diffed.
- For the variant matrix the census leg ran a stub (`--census-sh`), a flag the **reference counter** itself provides; the decisive `junk_census_clean` result in §2.3 was re-run with the **real** `sources-census.sh` (exit 0). Where I say "census catches E01/E09/E11" I ran the real script.
- I did not run `--selftest` (round-72 fixtures are hardcoded to S874/S875 and would fail for the wrong reason).
- Nothing was fetched plain-curl: the single fetch used the browser-shaped UA recorded in §2.2 and succeeded on the first attempt.
- No repo bytes outside `/tmp/CritCCounterVacuity/` and this report were written; no tool was installed or upgraded.

## 8. Evidence index

| artifact | path | sha256 / id |
|---|---|---|
| ported counter | `/tmp/CritCCounterVacuity/accept-c-73mut.py` | `4eebfe64fd6ffbbeffb6d86a6c9fe714aa2fd2ace4dcc6ddcfe9b31182f55b28` |
| fixture builder | `/tmp/CritCCounterVacuity/build.py` | `9dd1262b2a89b4bf97fd70db5377a5ddb9c3d29cd653ae41ef5815a0e042ec39` |
| census stub (ok) | `/tmp/CritCCounterVacuity/census-ok.sh` | `e1931566ea84815b9dffc6f41e97e8fc4aaa3fd4b56f0b6bed4420bf047f4b13` |
| census stub (marker) | `/tmp/CritCCounterVacuity/census-marker.sh` | `231f80fd88addc7e9cb5d0d3741646a16f6440ac0338ff584c3f758ed125217e` |
| fetched page | `/tmp/CritCCounterVacuity/fetch/ojs7099.html` | `e7260b49370e9a1e715d92b2102eabf8c2c8846f00a94caf3d80138dd019369c` |
| junk fixture | `/tmp/CritCCounterVacuity/junk-84jKiv` | base `999498b6`, lands `a55cd5f0` |
| census-clean junk | `/tmp/CritCCounterVacuity/clean-89rqka` | base `0a730d1d`, lands `2778d5b2` |

Variant matrix (`--census-sh census-ok.sh`, except the dirty-worktree run):

```
junk               PASS 10/10
base_only          FAIL (ENTRIES ROWS REPOINTED GATE REJECTS GROUND CITEDLINES SCRATCHMIRROR COLLCHECK)
rows_only          FAIL (ENTRIES REPOINTED CITEDLINES)   <- ROWS PASSES
shadow_row         PASS 10/10
row_mutation       PASS 10/10
entries_at_base    PASS 10/10
ground_same_commit PASS 10/10
gate_noreason      PASS 10/10
unrelated_doc      PASS 10/10
junk_census_clean  PASS 10/10   (real census --file: exit 0)
dirty worktree     PASS 10/10   (CENSUS reads a marker absent from lands bytes)
```

Real census runs:

```
validate --file junk-84jKiv/corpus/SOURCES.md   -> E09 x5 (staged recheck command), exit 1
validate --file asis.md (raw staged row)        -> E01 S881 fields=12, E11 dangling, exit 1
validate --file clean-89rqka/corpus/SOURCES.md  -> ok (W03 x2), exit 0
```

Stub-entry facts: `wc -w` 50 and 52; `check-cited-lines.py` → `CITED-LINES: 0 finding(s) in 2 file(s)`, exit 0; body cites only `S876`/`S877`; inline `S728` at line 15 of entry 1.
