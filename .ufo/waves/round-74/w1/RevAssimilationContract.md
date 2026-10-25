# RevAssimilationContract — round 74 wave 1 (claim C plan vs prompt §6 item 10 and the package adopt checklist)

Seat: reviewer (leaf). Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin` at base
`f7104cbce186bc2e1522abf0cfd619cc834628bb`. Date 2026-10-25.
Target of review: `reports/round-74/claims.json` claim **C** (DRAFT, not frozen) against
`/home/vgpnk/Projects/shokunin/.ufo/prompts/kotodama-round-74.md` §6 item 10 (lines 440-548),
fleet `CORPUS.md` (rules 1-4, census clause), and the staged package's own adopt checklist
(`/home/vgpnk/Projects/shokuknow/merge/kotodama/MERGE-REPORT.md` §"Adopt checklist", lines 103-112).

Read-only throughout: no write to the fleet root, `shokuknow`, sibling lanes, the lane git state,
or `claims.json`. No delegation, no background jobs, no `task` spawns. Nothing installed.
Downloads: none (this seat fetched nothing; the page evidence below is read from wave-1 seat
reports and from the receipts already on disk).

## 0. What I exercised, and what I only read

Ran myself (read-only text checks): registry row count and `before`-state re-derivation; the
prompt's quarantine-slice `awk` (21 rows); staged-row field counts with `awk -F'|'`; `claims.json`
content greps for S895/S816/S817; `git status` and file mtimes of lane and `shokuknow`; word counts
of the wave-1 drafts and of every base knowledge entry (`git show <base>:...`); targeted greps of
the untracked counter draft `.ufo/waves/round-74/counters/accept-c.py` (as of 21:43 today) and of
`assimilation/`.

Read only, **not re-run**: every fetch and every census/counter run. `census-start.txt`
(804 rows, `exit=0`) was read, not produced by me. `assimilation/validate-receipt-draft.txt`
and `guard-proof/out/` were read, not produced by me.

## 1. Obligation walk — item 10 against the plan

Legend: **PASS** = plan clause covers it and wave-1 evidence exists; **GAP** = no plan clause;
**CONTRADICTION** = plan clause (or its drafted counter) states something that cannot hold at a
correct lands.

| # | Obligation (prompt §6 item 10) | Plan element in `claims.json` | Verdict |
|---|---|---|---|
| 1 | Source repo read-only; never run campaign tools there (l.449-453) | no clause; this round's scans and fetches were read-only | PASS on evidence, GAP in plan (F22) |
| 2 | ONE theme, 1-3 knowledge entries (l.454-456) | one theme (`worldbuilding-setting-practice`), two entries: base + `.amend-2026-10-23` | PASS |
| 3 | Re-ground **every cited source** in-round; own date + quote in the Gate (l.456-460) | GATE/EVIDENCE legs cover the four adopted rows only; S877 is cited by the base entry and is outside both legs | **CONTRADICTION** with the claim's own kill rule (F1) |
| 4 | Append only rows an admitted entry cites; no bulk append (l.460-462) | `row_set` = 4 rows, each cited; S882 not appended (document = S877); folded S895 neither appended nor rejected | PASS on rows; GAP on S895 (F7) |
| 5 | Id collision check, 0-3-space extractor, planted-collision proof, map by document (l.470-493) | COLLCHECK leg; `assimilation/guard-proof/README.md` (2sp/3sp caught, 4sp ignored, column-zero false-green reproduced); map 22 collisions, 0 adopted | PASS (F5, F20 are hardening, not conformance) |
| 6 | Scratch transformation + `validate --file` exit 0 **before** the append (l.494-513) | SCRATCHMIRROR leg; `validate-notes.md` (mirror 808 rows, exit 0, E01/E03/E04/E09/E11/E12 mutant controls); receipt must precede the append commit | PASS on shape; receipt is not bound to final bytes (F6) |
| 7 | Quarantine slice hand-check, per-row verdict (l.514-528) | REJECTS names the earlier-refused S899/S900 quotes and the re-quote; no slice re-derivation or register-id verdict in any leg | GAP (F3, F11, F12) |
| 8 | Refused entries keep reason + flip; stay refused until the reason clears (l.462-463) | the round-72 refused entry is the entry now admitted; no clearing record | **GAP/CONTRADICTION** — see §3 (F3) |
| 9 | ≥1 admit and ≥1 reject from the assimilation set in the lesson Gate (l.467-469) | GATE leg (>=1 admit, >=1 reject, URL+reason+flip per reject row) | PASS as a rule; unsatisfiable for unprobed family rejects as worded (F14) |
| 10 | Amendment files APPENDED not replaced | not triggered: both targets are new files | GAP in declaration only (F8) |
| 11 | Folded duplicate-target entries; "the earlier round's rows stay cited" (MERGE-REPORT:17) | both entries listed; the fold's round-3 block (S895) is dropped by the draft | **GAP** (F7) |
| 12 | Package checklist 1-8 (MERGE-REPORT:103-112) | items 1/2/3/4 covered (re-ground all rows, append only cited rows, copy both entries); item 5 not triggered; item 6 violated by the trim; item 7 half-covered (SCORECARD/LOG yes, QUALITY.md no); item 8 see §3 | GAP (F7, F8, F25) |

Wave-4 quarantine-first (l.529-539) does **not** bar this round: round 72 recorded
"Adoption OPEN this round (wave-4 quarantine-first completed by rounds 68-71: 21/21 register rows
verdicted)" (`corpus/lessons/round-72.md:55-59`), and I re-derived the slice myself with the
prompt's `awk` — 21 data rows, 18 `payload-absent` + 3 prose-class (S807/S812/S835) — matching
`reports/round-71/telemetry/quarantine-verdicts.md:9-31`. The two rows this theme touches are
S816 (chinawriter 2025/0605) and S817 (chinawriter 2022/1207), both REFUSED (`:25-26`).

## 2. Findings by severity

### HIGH

**F1 — The reused row S877 is cited but has no Gate record or evidence window; the claim's
kill rule demands both.**
`claims.json:89` fails the claim if "any cited source lacks a round-74 Gate record and a committed
evidence window containing the Gate quote". The base entry cites S877 in its `source:` line and
quotes it repeatedly (draft `.ufo/waves/round-74/drafts/worldbuilding-setting-practice.md`: its
first `source:` line, draft line 3, and §2). Item 10 (l.456-460) says "re-open **every cited source** yourself; your Gate block
carries YOUR access date and ≤25-word located quote". But GATE (`claims.json:79`) and EVIDENCE
(`:80`) are worded "per adopted row", and the drafted counter iterates only the four frozen ids
(`.ufo/waves/round-74/counters/accept-c.py:999` in `leg_gate`, `:1061` in `leg_evidence`).
So the predicate and the kill rule disagree, and the clause would pass while item 10 is unmet.
Fix before freeze: add S877 as a Gate verification row (access date 2026-10-25, one located
≤25-word quote with page, locator) plus `reports/round-74/evidence/S877.txt`; or — if the round
decides S877 is "reused, already gated in round 73" — say so and narrow the kill rule, but that
does not satisfy item 10's "every cited source".

**F2 — The ROWS wording deletes an existing used-by pointer at a correct lands.**
`claims.json:77`: "used-by exactly the admitted entries whose source: lines cite it; the only
in-place registry change is S877's used-by cell". S877's cell at base is exactly
`corpus/knowledge/linguistics/conlang-scholarship.md` (`corpus/SOURCES.md:832`; awk field 12, the
11th column). The
correct in-place change (and the one the wave-1 mirror made — `assimilation/validate-notes.md`
§2 "old used-by ... new used-by: ...conlang-scholarship.md, ...worldbuilding-setting-practice.md")
keeps the old path and adds the base entry. The literal leg would require used-by = {base entry},
dropping a true pointer from a `mined` row. The drafted counter implements the literal text
(`counters/accept-c.py:833-836`: `want_used = cited.get(sid, set())`; `used != want_used`) and its
clean fixture bakes the deletion in (fixture S877 used-by old `corpus/knowledge/old/old-entry.md`
→ both admitted entries, `:1700`, `:1819`, `:2054-2057`). Consequence: the frozen predicate fails
at a correct lands, and fixing it after data would be a rule change (item 9). CORPUS rule 2
(`CORPUS.md:116-118`) permits the used-by edit in place, but it does not sanction removing a
pointer that is still true. Fix before freeze: "the four appended rows' used-by is exactly the
citing admitted entries; S877's used-by is its base value plus the base entry, logged old→new".

**F3 — The round-72 refused entry is re-admitted with no recorded clearing; register ids absent.**
`claims.json` contains zero occurrences of `S895`, `S816`, `S817` (I grepped the file). Its only
framing of the refused documents is `rejects.forced_new_quotes: ["S899","S900"]`
(`claims.json:49-52`), which presents them as re-quoted, not as refused. The record that must be
answered:
`corpus/lessons/round-72.md:32` — entry rejected, reason "both cited rows quarantine-REFUSED
(round-68 and round-71: quoted spans absent)", flip "the same, per row";
`reports/round-71/telemetry/quarantine-verdicts.md:25-26` — S816 REFUSED, S817 REFUSED;
register lines 129-130 (`/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md`)
— the two refused spans.
Item 10 (l.462-463): "Refused entries keep reason + flip condition in the Gate block and stay
refused until the reason clears." The plan has no clause that names the refused entry, its reason,
its flip, or the clearing. The wave-1 records already contain the needed facts
(`.ufo/waves/round-74/w1/ScoutQuarantine816817.md` §2-§4; `ScribeEntryAmend.md:11,81`), but the
frozen predicate (GATE/REJECTS legs, `claims.json:79,81`) would pass without them: the drafted
REJECTS leg only needs S899/S900 named on a line containing a re-quote/mispairing marker
(`counters/accept-c.py:1141`), and "reason"/"flip" anywhere in the lesson (`:1152`).
Fix pre-freeze, in the plan and in the lesson Gate: refused register ids + verdicts, this round's
re-confirmed absence of those spans, the located replacement spans, and the sentence that the
refused **rows** stay refused while the **document** is re-opened as a new row. See §3.

### MEDIUM-HIGH

**F4 — FROZENCFG says the map is never read from the graded tree; the map only exists in the
graded tree.**
`claims.json:87`: "row set, entry paths, fragments, map and every constant the counter uses are
read from claims.json AT the <freeze> commit ..., never from the graded tree". `claims.json`'s
`row_set` entries carry `{id, staged}` only (`:16-33`) — no URL — so the counter must read URLs
from `assimilation/id-renumber-map.json` **at lands** (`counters/accept-c.py:808`, `:1439`
`_map_records(mat)`), and a lands can rewrite the map URL. The selftest's
`config_edited_in_lands` control covers `claims.json`, not the map. Fix: freeze the four
`staged→lane→URL` triples in `claims.json` (so FROZENCFG's sentence is true), or read the map via
`git show <freeze>:...` and add a map-edited-in-lands junk landing.

**F5 — COLLCHECK trusts graded-tree evidence files instead of re-deriving them.**
`claims.json:86` asks that "reg-ids/collisions hold no adopted id" and that the guard proof shows
the plant behaviour. The drafted counter reads `reg-ids`, `staged-ids`, `collisions` and every file
under the assimilation tree from the **lands** tree (`counters/accept-c.py:1355-1360` reads
`reg-ids`/`staged-ids`/`collisions` from the materialized tree; `_guard_files(mat)` at `:1385`), and checks a
compiled-in regex result rather than rerunning the
extractor over `git show <lands>:corpus/SOURCES.md`. A lands that ships a doctored `collisions`
file or a self-authored "detected" line passes. This is round 73's routed defect 4 class
("config read from graded tree") under a new name. Fix: re-derive `reg-ids` from the lands
registry with the exact 0-3-space pattern, freeze the staged id list (or its sha256) in
`claims.json`, and keep `guard-proof` as the one-time guard proof whose planted ids are frozen.

**F6 — SCRATCHMIRROR reads strings, not bytes: a rehearsal receipt on placeholder anchors passes,
and the real receipt's `exit code: 0` does not even match the leg's regex.**
Two observations on the receipt on disk (`assimilation/validate-receipt-draft.txt`): it already
carries `--file`, all four ids and both entry basenames (I grepped it) while its own notes say the
anchor cells are "rehearsal-only" staged locators (`validate-notes.md` §4) and its §7 says the quote
cells are staged-derived; and its exit line reads `exit code: 0`, which the drafted leg's regex
`(?:exit|rc)\s*[=:]?\s*0` does **not** match (I ran the regex against every receipt line: the only
`exit` line is false) — round 73's artifact-vs-leg shape class again (`counters/accept-c.py:1288`).
The receipt does record the mirror registry sha256 (its line 7), so the binding data exists and the
leg does not use it. Fix: specify the receipt's exit-line grammar once, and bind the receipt to the
final bytes — accept the receipt only when its registry sha256 equals sha256(base registry + the
exact append block) and its recorded entry sha256s equal the entries at lands — and regenerate it
after the seven quotes are re-located (the four Japanese/Chinese rows plus the S877/§2 quotes).

**F7 — The folded round-3 passage is dropped without operator authorisation or a declared reject.**
`MERGE-REPORT.md:57-58` marks the worldbuilding amendment as **new-file** (round4) plus
**folded-into-canonical** (round3); `:17` says "The earlier round's rows stay cited, so they remain
mined. The operator may trim the folded passage if the later entry supersedes it outright."
The staged file carries the round-3 block with `source: S895 —
https://www.chinawriter.com.cn/n1/2025/1030/c404027-40592897.html` (staged file lines 38-44), which
is a different document from the build-order/delivery text and is not superseded by it. The draft
drops it (`ScribeEntryAmend.md:11`), and claim C makes carrying it impossible: `row_set` is
S881..S884 and ROWS requires "exactly S881..S884 (contiguous)" (`claims.json:77`), and the kill
rule fails an entry citing an id outside the five rows (`:89`). Neither `S895` nor "Folded" appears
in `claims.json` (0 hits). So the plan, as frozen, commits a trim that the package reserves to the
operator. Fix (choose one, pre-freeze): (a) adopt staged S895 → lane **S885** with a this-round
located quote, evidence window, Gate row and map record, and change `row_set`/ROWS to S881..S885;
or (b) declare the trim in `rejects` with reason + flip and record operator approval in the round
report. Option (a) is the one the package's own words support.

**F8 — The own-new-file disposition is not declared.**
`MERGE-REPORT.md:48` (base, new-file) and `:57` (amendment, new-file; the `amendments/` directory
holds only calendar, era, conlang-methodology and naming-systems — I listed it). Therefore
checklist item 5 ("For every file under `amendments/`, append ... Do not replace the file",
`:109`) is not triggered and the round creates two new files; checklist item 6's fold is the
package's internal one. The plan's entries list mirrors this, but nothing states it, so a closure
reader can read the round as "append or replace" and disagree. Fix: one sentence in the claim's
`after` or the lesson, plus the report.

### MEDIUM

**F9 — Item 10's per-entry gates are not in the predicate.**
l.465-469 requires a `PROVINCE.md` scope check and a `QUALITY.md` bar per entry. The 12 legs
(`claims.json:76-87`) contain neither. PROVINCE does allow it — the lane owns the generative craft
in `culture-material` (`PROVINCE.md:9-18`), and the draft's `couples:` line routes canon to lore
via `synthesis/worldbible-integration-contract.md`. Add the two verdicts to the GATE leg (or a
P/G leg) so the lesson's Gate cannot omit them.

**F10 — S877 is used outside its recorded scope, and the scout's condition is not enforced.**
S877's `scope` is the book's framing — classification, vocabulary, Tolkien/Klingon/D'ni status,
literature survey (`corpus/SOURCES.md:832`, scope cell). The base draft's §2 also derives "a world is
built around a premise" from PDF p.36 and "язык — главный инструмент" from p.7. The wave-1 scout
already conditions this use: "S877's `scope` ... is classification of artificial languages, not
setting-note practice ... the entry's wording must stay inside the scope, so rewrite claims #4,
#5, #6 first" (`.ufo/waves/round-74/w1/ScoutSidorovaWorldview.md:63`; also `:19`, `:64`). CORPUS
rule 2 forbids widening `scope` in place (`CORPUS.md:116-118`), so the options are: confine §2 to
the scoped claims, or take a superseding row "supersedes S877 —" (which changes the declared row
set). No leg checks a citation against its row's scope.

**F11 — No `## Quarantine` obligation.**
The plan has no leg requiring the lesson to re-derive the 21-row slice with the prompt's `awk`,
carry the standing verdict table, and re-check S816/S817 this round. The drafted REJECTS leg only
looks for the word "quarantine" anywhere (`counters/accept-c.py:1150`). Round 72's lesson carried
the section (`round-72.md:55-71`); round 74 should carry it or reference the standing table.

**F12 — The slice's three prose-class rows print a stray backtick.**
The prompt's `awk` yields `S807\``, `S812\``, `S835\`` because those register rows shift columns
(I re-derived the 21-line slice; the scout recorded the same, `ScoutQuarantine816817.md` §1). Any
closure re-derivation must not treat that as a missing S-id. Put the note in the lesson so the
non-author spot-check reads the same 21 rows.

**F13 — The ≤25-word cap is vacuous for CJK quotes.**
Item 10 and the seat rule require the character count for CJK ("CJK counts per whitespace token —
also give the character count"). GATE's check is `len(s.split()) <= 25` (`counters/accept-c.py:1018`),
and a CJK quote is one token, so a 500-character quote passes. The wave-1 quotes are short
(32/22/19/27 chars, `ScoutQuarantine816817.md` §4), so this is a predicate defect, not a content
one. Require a character count per CJK Gate quote and a bound (or at least its recording).

**F14 — "Every reject row carries its probed URL" is unsatisfiable for family rejects.**
`claims.json:79` and `counters/accept-c.py:1040` require a URL in every reject row, but
`rejects.refused_files` (`claims.json:53-61`) is 7 family entries, most with no probe (naming,
calendar, era, verification, conlang amendments). An honest family row carries no probed URL;
carrying one to satisfy the leg is a junk landing. Split the predicate: probed rejects
(URL + reason + flip) vs not-adopted staged families (family/file name + reason + flip +
refusing round where one exists).

**F15 — QUALITY 23's freeze-commit run is not declared.**
`corpus/QUALITY.md:77` requires the counter be run "at the FREEZE commit (receipts present,
landing absent) so artifact-vs-leg shape mismatches show before data", and names round 73's
GROUND/SCRATCHMIRROR/COLLCHECK as the class. Claim C's `do_nothing_control` (`claims.json:90`)
declares lands==base plus four junk landings only; neither C nor Ca declares the freeze-commit run
or its receipt. This matters more than usual here: F6 shows the receipt on disk would pass every string
check but the exit-line grammar while its anchors are placeholder locators — the shape class
QUALITY 23 exists to catch before data.

**F16 — Control coverage is under-declared relative to the drafted selftest.**
The do-nothing control names four junk landings; the drafted selftest names ~40 mutations
across all legs (`EXPECTED_FAIL` at `counters/accept-c.py:2236`). The claim should name at least one control per
leg (notably REPOINTED campaign-id, GATE no-requote, SCRATCHMIRROR receipt-in-append, COLLCHECK
map/guard, REJECTS) or cite the selftest verdict line, otherwise routed defect 4's closure is not
observable from the claim text.

### LOW

**F17 — Rejects family counts omit the three base-path staged amendments.**
The counting convention is "`.amend-*` files only": naming-systems ×11, calendar ×3, era ×2
(`claims.json:55-57`) exclude the staged amendments that target existing lane paths
(`naming-systems.md`, `calendar-festival-systems.md`, `era-periodization-models.md`,
`MERGE-REPORT.md:39,41,44`). Those three are still unadopted and unnamed. State the convention
and list the three, or say the family label covers them.

**F18 — `after` is not one concrete value.**
"PASS legs=<n>/<n> (n fixed at freeze)" (`claims.json:15`); the draft selftest expects 12/12
(`counters/accept-c.py:2307`). Round 73 wrote "PASS legs=11/11". Concretize at freeze (and note
that the count changes if F1/F9/F11 add legs).

**F19 — "none removed" is literally false for S877's line.**
`claims.json:77` pairs "adds exactly S881..S884 ..., none removed" with "the only in-place registry
change is S877's used-by cell". A line-level diff removes and re-adds S877's line (the drafted
counter handles exactly that, `counters/accept-c.py:748-800`). Write the predicate as "the only
changed line is S877's row and the only changed cell is its used-by", so plan, counter and receipt
are the same sentence (item 9).

**F20 — Map source-of-truth duplication and an ambiguous staged-id list.**
`after` (`claims.json:15`) points at a committed `id-renumber-map.json`; FROZENCFG points at
`claims.json` at freeze. One source must win (see F4). REPOINTED's "no staged-namespace id
(S882..S884 of the campaign, S899, S900)" (`:78`) is ambiguous after adoption, because lane
S882..S884 then exist; state the URL-identity test, not a token list.

**F21 — `before` (b)'s README assertion has no command.**
CORPUS "a negative claim carries its sweep". I re-derived it: 17 `worldbuilding` hits in
`corpus/README.md`, 13 as "...worldbuilding method/tool/system/evidence", 4 as lane-domain
descriptors (`:395,:396,:496,:524`), 0 `setting-practice` rows. Add the command.

**F22 — Source-repo read-only has no evidence obligation.**
I verified the round wrote nothing there: `find merge/kotodama -newermt "2026-10-25 00:00"`
returns nothing (the files I opened carry mtimes of 2026-10-24 23:33; `git status` there shows
uncommitted upstream campaign modifications that predate this round). Record that check in the round report; keep every seat's downloads under
`/tmp/<seat>/`.

**F23 — The stripped recheck prose is required in the lesson, not just in scratch.**
Item 10 (l.494-500) requires the stripped prose "(re-verify conditions, Gate pointers) recorded in
the round lesson's Gate block". It is currently only in `assimilation/validate-notes.md` §3 (the
four `curl ... \| grep -c ...` commands). Add it to the GATE leg.

**F24 — "no placeholder values" is header-scoped, and the body carries two `(to-verify)` leads.**
The drafted check scans header fields only (`counters/accept-c.py:697-699`), which matches the
intent; the base draft body has `(to-verify)` at
`drafts/worldbuilding-setting-practice.md:24,251`. Scope the leg wording to the header and have
the lesson classify those two as leads (not admitted claims).

**F25 — Package checklist item 7 has no QUALITY.md obligation, and Ca does not guard the file.**
`MERGE-REPORT.md:111` asks to "Update `corpus/QUALITY.md` and the lane's `SCORECARD`/`LOG` per the
lane's own protocol". Claim Ca covers SCORECARD (`ANNOTATE`, `APPENDONLY`) and LOG, but
`QUALITY.md` is in neither the APPENDONLY set (`claims.json:106`) nor any leg, while
`frontier_step.quality_candidate` promises "QUALITY 25 — a counter reads its constants from the
frozen commit and ships junk-landing controls" (`claims.json:124`). So a new criterion can be added
or an existing one removed with no leg reading the diff. Fix: name the QUALITY.md criterion (and
its ground) in one claim's after-state, and either add QUALITY.md to the APPENDONLY set or state
that its edit is append-only by protocol and checked by a diff line count.

Data note (not a finding, but closure-relevant): the staged rows for this theme are **NF=14**
against the fleet's NF=13 (I measured all six with `awk -F'|'`: S882/S883/S884/S895/S899/S900).
The extra field is the escaped `\|` inside the recheck command. The scratch transformation
(`validate-notes.md` §2-§3) merges it and strips the prose, which is exactly item 10's rule; no
staged row may land as-is, and the drafted counter also rejects an escaped pipe
(`counters/accept-c.py:817`).

## 3. The refused-rows question, decided on the exact words

**Question.** Is "two entries from ONE theme where one rests on previously REFUSED rows" allowed by
the contract's "Refused entries keep reason + flip condition in the Gate block and stay refused
until the reason clears" (prompt l.462-463) — and does a fresh row with a re-located quote clear
the reason?

**Decision.** Allowed, but only as a re-write on new rows, and only with the clearing recorded. The
reason the round-72 refusal states is a proposition about **spans**, and re-quoting does not make
it false:

1. The cap is not the obstacle. Item 10 allows one theme and 1-3 entries (l.454-456); the plan
   takes one theme and two entries. Nothing in the refusal sentence limits entries or themes.
2. The refused unit is the **row/quote**, and the entry-level refusal inherited it:
   `round-72.md:32` — "both cited rows quarantine-REFUSED (round-68 and round-71: quoted spans
   absent)", flip "the same, per row"; the register's own class definition is quote-level —
   "`payload-absent` | every relevant source fetched cleanly and the quote is in none of them", and
   its reader action is "**the fabrication class**: verify by hand, then correct the quote or
   refuse the row" (register lines 11-15; `payload-absent` at line 13).
3. The refused spans are still absent, and a new span cannot clear their absence:
   `ScoutQuarantine816817.md` §3 (observed, not re-run by me) found S816's span
   `这个我肯定考虑过。我自己就是资深读者` **0 hits on the 2025 page** and 1 hit on the 2022 page,
   and S817's `Sowers-Wills ...` span 0 hits on either chinawriter page (it belongs to lane S880's
   document). So "the reason" — the quoted span is not on the cited page — has **not** cleared for
   either refused row, and cannot unless the pages change.
4. What round 74 does is the register's second remedy, "correct the quote", and item 10's own
   quarantine sentence — "present → adopt with the anchor you located" (l.521-524): a **fresh row**
   on the same URL whose quote was located this round. That is a new evidence object with its own
   gate. It does **not** execute the round-72 flip ("a re-opened source carrying the quoted span,
   written as a new row", `round-72.md:31-32`) — the re-opened sources do not carry the refused
   spans — and the round must not say it does.
5. Therefore "does a fresh row with a re-located quote clear the reason?" — **yes, at the level the
   reason is stated, and under four conditions**, none of which `claims.json` meets today:
   (a) the refused register ids (S816, S817) and their standing REFUSED verdicts are in the lesson
   Gate with their reason and flip; (b) this round re-confirms the refused spans are absent (so
   the flip is recorded as *not* executed, not as passed); (c) the replacement span is located this
   round, with its own access date, evidence window and located quote, and is not inherited from
   the staged cell; (d) the Gate says the refused **rows stay refused** while the **document is
   re-opened as a new row**, and the admitted bytes are a round-74 entry, not the refused staged
   entry adopted. Missing (a)-(d), the round is admitting a refused entry without a clearing —
   the exact thing the sentence forbids.

**Consequence for this plan.** Because the plan keeps the refused entry's filename
(`worldbuilding-setting-practice.amend-2026-10-23.md`) and describes the two documents only as
"forced_new_quotes" (`claims.json:49-52`), the burden is entirely on a record that does not exist
(F3). This is the one item that must change before freeze; the content is already correct in
`ScoutQuarantine816817.md` §4 ("a fresh lane row opened this round ... is honest provided that ...")
and `ScribeEntryAmend.md:11`, so it is a recording fix, not new research.

## 4. Residual risk

- The re-quote rests on wave-1 fetches under the browser-shaped UA whose bytes were already stable
  across rounds 68/71/74 (scout's byte-identity comparison, `ScoutQuarantine816817.md` §2). I did
  not re-fetch; if the pages change between now and lands, EVIDENCE's stored window (which is
  checked, not a flag) is the guard, and it is the right guard.
- The base entry's S877 use (F10) is the one place where admitted prose can be broader than the row
  that supports it. A closure reader applying CORPUS rule 1's "quote ... grounding `teaches`" is
  entitled to fail §2; the draft already carries the scout's rewrite list.
- The id map is sound as declared (22 numeric collisions S859..S880, all unrelated documents; the
  four theme ids are outside the collision set; single-pass substitution documented in
  `assimilation/id-renumber-map.json`), but its URL half lives in the graded tree (F4).
- Two counters are in flight as untracked drafts (`counters/accept-c.py`, `accept-ca.py`, 21:42-21:43).
  Every counter defect above is reproduced from those drafts at that time; the freeze must not
  inherit them, and a leg/condition changed after any seat scores is not the claim's rule (item 9).

## 5. Verification gaps (what this seat did not exercise)

- No fetch, no CDX probe, no census run, no counter run, no `--selftest` run: every fetch/census/
  counter statement above is a read of another seat's artifact, and I label it as such.
- The receipt/ordering claims of SCRATCHMIRROR were not executed (the receipt's commit position is
  a later wave's job). I checked which of the leg's string checks the rehearsal receipt satisfies
  (ids, entry basenames, `--file`) and that its exit line does **not** match the leg's regex (F6).
- I did not verify the four located quotes against page bytes; that is ScoutChinawriter2025/2022,
  ScoutLitmemo, ScoutTuduku and ScoutQuarantine816817's ground, and the EVIDENCE window is the
  counter's guard.
- The `guard-proof/out/*.summary.txt` numbers are read from the wave-1 receipt, not regenerated.
- Tool installs: none. Downloads: none.
