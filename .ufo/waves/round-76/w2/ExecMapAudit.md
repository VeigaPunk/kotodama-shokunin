# ExecMapAudit — round 76, WAVE 2 falsification (seat: ExecMapAudit)

Scope: read-only audit of `.ufo/waves/round-76/assimilation/id-renumber-map.json` and the staged/base id
lists, plus the by-document mapping S908/S935→S894, S932/S938→S895, S937→S896 and the URL-representation
mismatch behind it. No source file, lane file, claim, counter or report was modified. No build/test/lint was
run (the counter was not executed; its committed receipts and source were read instead).

Revisions audited (all read via `git show`, never the mutable worktree):

| role | revision |
|---|---|
| base (claim base) | `98c486bdb4650ba5b8e651d332910e8ee60ad121` |
| frozen C/Ca configuration | `df0f0309d61e5485bb17035d3f8791b1e6a11d40` |
| Ca landing | `a43ed807ea38b5fc5a7875a839d576cea73aba7c` |
| C landing | `722e69ff6361aadf148cb46acbf6ac8fd147f59a` |

---

## VERDICT (short)

1. **The mapping is exactly as claimed, in the frozen bytes.** The frozen map carries
   `S908→S894, S935→S894, S932→S895, S938→S895, S937→S896` (plus the two reused rows `S919→S892`,
   `S921→S885`), and the landed registry at `722e69f` carries rows S894/S895/S896 whose source cells name
   those three documents. The map's bytes are identical at the freeze, at the Ca landing and at the C
   landing (sha256 `a9f530e2…`, equal to the frozen `claims.json → map.sha256`), so nothing was edited
   between freeze and landing.
2. **The staged/base id lists are sound and re-derivable.** reg-ids 817 = the base registry's id set;
   staged-ids 132 = the package's id set; collisions 35 = their `comm -12`. S894/S895/S896 are free at base
   and absent from the collision set.
3. **There is exactly one URL-representation mismatch, and it is on the `S938→S895` edge.** It is a
   pre-data fact, not a landing regression: the same mismatch is already red in the frozen no-data control.
   `S938` is folded into lane row `S895` on a **measured HTTP 302 redirect**, while the map's own declared
   join key is a **normalized document URL** — under that key `showGb` and `newGbInfo` are two different
   documents. The landed row names the alias in prose only (no scheme/host), so the frozen counter's
   URL-identity check cannot match it, and the `COLLCHECK` leg is red at both the freeze and the landing.
4. Two smaller map defects are recorded below (§4): a staged row that names the S895 document but has no
   map record (`S859`), and a `cited_by_file` / `entry_substitutions` section computed against a **different
   file** than the one that landed.

---

## 1. The map file: identity, integrity, content

Frozen artifact: `.ufo/waves/round-76/assimilation/id-renumber-map.json`
(committed at `b4965d5` "round-76: freeze claims, counters, source controls and wave-1 evidence"; unchanged
afterwards on the first-parent chain `98c486b → 722e69f`).

* sha256 at `df0f030` = `a9f530e26cbbd607d156a2fc32cc4ed241f9c37b79e17dc17cc5335f184f4092`
* sha256 at `a43ed80` = same; sha256 at `722e69f` = same; worktree copy = same.
* `reports/round-76/claims.json` (frozen at `df0f030`) → claim C `map.sha256` = the same value, and
  `map.path` = `.ufo/waves/round-76/assimilation/id-renumber-map.json`. The map the counter grades is the
  frozen blob, and it is the blob I audited.

Map content (line numbers of the frozen file):

| map lines | record | lane id | `document_normalized` |
|---|---|---|---|
| 541–560 | `S908` | S894 | `digital.archives.go.jp/search` |
| 561–580 | `S935` | S894 | `digital.archives.go.jp/search` |
| 582–602 | `S932` | S895 | `openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=E107EA4DE9725EDF819F33C60A44B296` |
| 603–621 | `S938` | S895 | `openstd.samr.gov.cn/bzgk/std/showGb?type=online&hcno=E107EA4DE9725EDF819F33C60A44B296` |
| 622–640 | `S937` | S896 | `news.gmw.cn/2017-05/23/content_24559485.htm` |
| 641–674 | `S919` | S892 (reused) | `iris.unipa.it/…/2014 marrone age dor---2.pdf` |
| 675–712 | `S921` | S885 (reused) | `persee.fr/doc/comm_0588-8018_1966_num_8_1_1113` |

`assignments` (lines 713–761) repeat the same seven pairs. The frozen `claims.json` `row_set` (lines
103–119) names exactly the three adopted rows with the same staged groupings: `"S908/S935"`, `"S932/S938"`,
`"S937"`; `reused_rows` is `[]` (claims.json:120). The map and the frozen claim agree; the map is not the
thing that diverged.

## 2. The id lists re-derived (not trusted)

I re-derived all three lists from committed bytes with the map's own extractor (`^ {0,3}\|\s*(S\d{3,})\s*\|`):

* base registry at `98c486b` → **817** ids, `S001`…`S893`; equals `assimilation/reg-ids` (817 lines) — **equal**.
* package `merge/kotodama/SOURCES.append.md` → **132** ids, `S859`…`S990`; equals `assimilation/staged-ids` — **equal**.
* `reg-ids ∩ staged-ids` = **35** (`S859`…`S893`); equals `assimilation/collisions` — **equal**.
* sha256 of the three files equals the values recorded in the map's `inputs` block and in
  `corpus/lessons/round-76.md:69`:
  `reg-ids 97eef07a…`, `staged-ids bab11d7d…`, `collisions be203dd8…`; base `corpus/SOURCES.md`
  `c1f9f1e0…`; package append `7fb4f488…`.
* `S894`, `S895`, `S896` are **not** in reg-ids and **not** in collisions → the adopted numbers were free
  at base. (The *staged* ids `S894/S895/S896` exist in the package but name unrelated documents —
  Sowers-Wills, 王昕玥, 韓国 中國文化硏究會 — exactly the overlap the map records at lines 380–409.)
* Guard proof: the planted 1–3-space id is `S897` (`guard-proof/planted-1space-registry.md`, 2-space indent),
  detected by the whitespace-tolerant extractor; the 4-space control is not detected
  (`planted-4space-proof.txt`, exit 1). `S897` is a staged id absent from the base registry, so the plant
  satisfies the counter's R6 requirement.
* Base ground: `git grep -l -E 'GB/T 33661' 98c486b -- corpus/knowledge` → exit 1 (nothing); the base
  registry contains **0** rows naming `digital.archives.go.jp`, `openstd.samr.gov.cn` or `news.gmw.cn`
  (so the map's `lane_holds_any_document_of_the_map_except_S885_S892: []` holds), and `knowledge` holds
  **252** `.md` at base vs **253** at the C landing.

## 3. The URL-representation mismatch (the assigned question)

### 3.1 Where the representations diverge

Three different "same document" rules are in play, and they disagree on one pair:

| rule | where | outcome for showGb vs newGbInfo |
|---|---|---|
| **map join key** — "normalized document URL (round-75 norm_url): host lowercased without www., path percent-decoded, persee … -> /doc/<slug>, web.archive.org wrapper stripped" | map file line 10; implementation `build-map.py:17-32` (`norm_url`) | **different documents** (`/bzgk/std/showGb?type=online&hcno=…` vs `/bzgk/std/newGbInfo?hcno=…`) |
| **map assignment fact** — the two routes are one document because `showGb` 302-redirects to `newGbInfo` | map line 620 (`"note": "showGb route redirects by 302 to the same newGbInfo record; alias only, no second row"`), asserted at `build-map.py:63` | same document |
| **counter's leg rule** — "every such record's url must name a document the landed row's source cell names (document identity via urls_compatible …)" | `reports/round-76/accept-c.py:3394-3399` (leg text R7), implemented at 3620–3631 with `urls_compatible` (471–483) | **different** — path containment fails |

The map is internally honest about this: `S938`'s own `by_document_join.staged_rows_naming_this_document`
is `["S938"]` (map lines 613–615) and its `document_normalized` differs from `S932`'s (607 vs 586). The map
never claims URL identity between them; it merges them on a measured redirect. The counter, however,
grades the *map record's URL* against the *landed row's source-cell URLs* by string/containment identity.

### 3.2 Why the landed row does not satisfy that check

Landed row `S895` source cell (`corpus/SOURCES.md:850` at `722e69f`):

```
live https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=E107EA4DE9725EDF819F33C60A44B296 ;
showGb?type=online redirects here by HTTP 302 ;
same record captured 2026-04-24 at https://web.archive.org/web/20260424031027id_/https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=…
```

The alias appears **as prose, without scheme and host**. The counter extracts URL tokens with
`URL_RE = re.compile(r"https?://[^\s|<>()（）「」『』]+")` (`accept-c.py:262`, used by `urls_in`, 457) and
then compares each map-record URL with the row's URLs via `urls_compatible`, which folds host+path only
(the query string is dropped by `norm_url`, 299–303) and accepts equality or one path contained in the
other. Re-running that exact comparison on the committed bytes (my own re-implementation of the two
functions from `accept-c.py:299-303` and `471-483`, applied to the map's `staged_url_cell_urls` and to
`SOURCES.md:850`):

```
map S908 -> S894  url https://www.digital.archives.go.jp/search                              compat [True, True]
map S935 -> S894  url https://web.archive.org/web/20260422145052id_/…/digital.archives.go.jp/search  compat [True, True]
map S932 -> S895  url https://web.archive.org/web/20260424031027id_/…/newGbInfo?hcno=…       compat [True, True]
map S938 -> S895  url https://openstd.samr.gov.cn/bzgk/std/showGb?type=online&hcno=…          compat [False, False]   <-- mismatch
map S937 -> S896  url https://news.gmw.cn/2017-05/23/content_24559485.htm                    compat [True, True]
```

`/bzgk/std/showGb` is neither equal to nor contained in `/bzgk/std/newGbInfo` (and the query, which the
counter discards, could not have helped). Hence the committed red leg, verbatim:

* `reports/round-76/telemetry/measures-c.txt:38-39` (C landing `722e69f`):
  `LEG FAIL COLLCHECK — map record S938 -> S895 names a document the row does not: https://openstd.samr.gov.cn/bzgk/std/showGb?type=online&hcno; ids=817 staged=132 collisions=35 guard=ok/ok map=7`
  and `measures-c.txt:45` → `ACCEPT-C-76: FAIL legs=11/13` (exit 1).
* `reports/round-76/telemetry/controls-c.txt:48-49` (no-data control at the freeze `df0f030`): the **same**
  message, already red before any data landed.

So the mismatch is **frozen-in**, not introduced by the landing: at `lands == freeze` it is present too.
It is the one edge of the mapping that the frozen counter's URL-identity rule cannot accept.

### 3.3 The redirect fact itself is well measured (so the fold is justified; only its representation is not)

The 302 alias is corroborated by committed wave-1 receipts:

* `.ufo/waves/round-76/w1/stage/ScribeEntryB/gate-notes.md:14-18` — F1/F2: `showGb?type=online` and
  `?type=download` both answer `302 Location: …/bzgk/std/newGbInfo?hcno=…&refer=outter`; F3/F4/F5: the
  followed target is 24,144 B, sha256 `80b4c781…`, byte-identical across repeats and under
  `Accept-Language: zh-CN`.
* `.ufo/waves/round-76/w1/stage/ScribeLesson-7/fetch-receipts.md` — the `showGb` route followed through
  302 → 200 with stored bytes identical to the `newGbInfo` capture; the `/bzgk/gb/*` spellings resolve to
  the same bytes.
* `corpus/lessons/round-76.md:17` records the alias as a 302 with the same-document measurement.

Note the alias identity is **header-conditional** and the lane recorded that carefully in wave 1: with a
catalogue `Referer`, `showGb?type=online` answers 200 with 89,039 B / 89,002 B and is *not* byte-stable
(`ScribeEntryB/gate-notes.md:19-23`, F6–F10), and `showGb?type=download` serves a 7,606 B captcha modal, not
a file. So "showGb is the same document as newGbInfo" holds for the referer-less request the lane actually
made; the row's prose "redirects here by HTTP 302" is a fair statement of that measurement.

### 3.4 Minimal representation repair (for round 77; not applied here)

The mismatch is fixed by making the alias a **URL token** in row S895's source cell rather than prose —
e.g. writing the full `https://openstd.samr.gov.cn/bzgk/std/showGb?type=online&hcno=E107…` beside the
newGbInfo URL. With that token present, `urls_compatible(showGb-URL, showGb-URL)` is exact equality and
the leg goes green; nothing about the redirect fact, the row count, the used-by or the frozen claim
constants changes. (Adding the alias as prose, or as a bare route without scheme, does not help: `URL_RE`
requires `https?://`, and `norm_url` drops the query.) Alternatively the map record for `S938` would have to
carry the `newGbInfo` URL — but the map is frozen by sha256 and its `S938` key is deliberately the alias,
so the row is the cheaper side to repair. Note the collateral: `claims.json` freezes `row_set` with
`"staged": "S932/S938"`, so the `S938` staged row must keep pointing at lane row `S895`; the repair keeps
that.

### 3.5 The other red leg, for completeness (not a map defect)

`LEG FAIL ROWS` (`measures-c.txt:33-34`) is caused by two **prose** lines the landing added inside
`corpus/SOURCES.md` outside the registry table: the `## Paths` bullet at line 854
(`- calendar-standard design — S896 → S895 → S894: start with …`) and the `## Search log` paragraph at
line 902 (`**State-standard calendar compilation (round 76).** Question: …`). The ROWS leg diffs the whole
file line multiset and treats any added non-blank non-row line as a row addition outside the frozen
row_set (`accept-c.py:1584-1607`). Both lines were committed in `cab5247`, i.e. **before** the freeze
commit `df0f030` (ancestor of it) — which is also why the no-data control already shows this red. The
lane routed this as `R76-M3` (`corpus/lessons/round-76.md:85`, "none (routed)").

## 4. Two further map defects (recorded, not repaired)

**(a) A staged row that names the S895 document has no map record.** `S932`'s `by_document_join`
lists `staged_rows_naming_this_document: ["S859","S932"]` (map lines 593–596), and the package row `S859`
(`merge/kotodama/SOURCES.append.md:7`) indeed carries the same `newGbInfo` URL. But the map's `map` block
has **no** `S859` record and `assignments` has **no** `S859` entry (the builder's own `PKGMAP` at
`build-map.py:99` does contain `"S859":"S895"`, but that constant is never emitted into the map). So a
reader following the map "by document" finds a staged row naming the S895 document with no mapping. It
caused no leg failure (the frozen `row_set` names only `S932/S938` for S895, and the admitted entry cites
the `newGbInfo` capture, i.e. S932), but the map's coverage is incomplete against its own by-document index.

**(b) `cited_by_file` and `entry_substitutions` describe a file that did not land.** The map's
`entry_substitutions` (lines 780–935, 19 records, line numbers up to 95) and `cited_by_file` (lines
936–951) were computed against the **package** file
`merge/kotodama/knowledge/corpus/knowledge/culture-material/calendar-festival-systems.amend-2026-10-24.md`
(98 lines). The landed file `corpus/knowledge/culture-material/calendar-festival-systems.amend-2026-10-24.md`
at `722e69f` is 109 lines and its only S-tokens are `S894` (×10), `S895` (×9), `S896` (×13). The map
asserts `S892` and `S885` are cited by that file; the landed file cites neither (it declines the
Barthes/Marrone passage at lines 14 and 66). Correspondingly the reused rows' `used_by` cells are
**unchanged from base** (`S892`: `…/narrative-structure-frameworks.amend-2026-10-23b.md`; `S885`: the three
narrative-structure files) — the map's planned "add the calendar entry to used-by in place" for
`S919→S892` / `S921→S885` (map lines 668–673, 706–711) was not executed, consistently with the entry
dropping that material. This is why the map is marked `"scratch_only": true` (line 958) — but a reader
who treats `cited_by_file` as fact would mis-read the landed tree. The `REPOINTED` leg passed regardless,
because the landed entry cites only adopted lane ids.

## 5. Cross-check against the landed tree (C landing `722e69f`)

* `corpus/SOURCES.md` at `722e69f`: 820 rows; base 817 + exactly `S894` (line 849), `S895` (850),
  `S896` (851); **no** pre-existing row removed or altered (`S892`/`S885` `used_by` byte-identical to base).
* The three landed rows carry 11 cells each, `mined`, opened `2026-10-27`, recheck `180d`, and `used_by`
  = exactly `corpus/knowledge/culture-material/calendar-festival-systems.amend-2026-10-24.md`.
* The three landed source cells name exactly the mapped documents: S894 → live + 2026-04-22 Wayback
  capture of `digital.archives.go.jp/search`; S895 → live `newGbInfo?hcno=E107…` + 2026-04-24 capture of
  the same page (+ the prose alias, §3.2); S896 → `news.gmw.cn/2017-05/23/content_24559485.htm` + its
  2017-05-23 capture.
* Committed Gate evidence windows exist for all three rows
  (`reports/round-76/evidence/S894.txt|S895.txt|S896.txt`, each with `quote-found: yes`,
  `quote-found-verbatim: yes`, `challenge: none`).
* End census `reports/round-76/telemetry/census-end.txt`: `kotodama ok …` exit 0, no E-code.
* Frozen-claim outcome: **C fails as declared** — `ACCEPT-C-76: FAIL legs=11/13` with ROWS and COLLCHECK
  red (`measures-c.txt:33-45`); the lane routed it (`corpus/lessons/round-76.md:89`: "C failed as declared
  at `722e69ff…`: `ACCEPT-C-76: FAIL legs=11/13`, with only ROWS and COLLCHECK red … COLLCHECK rejects
  frozen map record S938→S895 because the map URL is the `showGb` alias and the appended S895 source cell
  only names its `newGbInfo` target"). Ca likewise fails as declared at `a43ed807`
  (`ACCEPT-CA-76: FAIL legs=5/12`). My audit confirms the lane's own diagnosis of the COLLCHECK cause and
  identifies the minimal representation repair it did not perform.

## 6. Files read (all committed bytes; nothing modified)

* `.ufo/waves/round-76/assimilation/id-renumber-map.json` @ `df0f030` / `a43ed80` / `722e69f`
* `.ufo/waves/round-76/assimilation/build-map.py`, `reg-ids`, `staged-ids`, `collisions`,
  `guard-proof/*`, `validate-receipt.txt`
* `reports/round-76/claims.json` @ `df0f030` / `722e69f`; `reports/round-76/accept-c.py` (read only)
* `reports/round-76/telemetry/{controls-c,measures-c,census-end}.txt`; `reports/round-76/evidence/S89{4,5,6}.txt`
* `corpus/SOURCES.md` @ `98c486b` / `722e69f`; `corpus/lessons/round-76.md` @ `722e69f`;
  `corpus/knowledge/culture-material/calendar-festival-systems.amend-2026-10-24.md` @ `722e69f`
* `merge/kotodama/SOURCES.append.md` and `merge/kotodama/knowledge/corpus/knowledge/culture-material/calendar-festival-systems.amend-2026-10-24.md`
  (read-only source repo `/home/vgpnk/Projects/shokuknow`)
* `.ufo/waves/round-76/w1/stage/ScribeEntryB/gate-notes.md`,
  `.ufo/waves/round-76/w1/stage/ScribeLesson-7/fetch-receipts.md`,
  `.ufo/waves/round-76/w1/ScoutDocS897.md` @ `722e69f`

## 7. Tooling

No tool was installed or upgraded. `/home/vgpnk/.omp/agent/RULES.md` was read first (it authorizes installs
with full privilege, but this seat expected none); pacman was **not** invoked and no system package was
touched. Everything used was already present: `git`, `python3` (stdlib only), `grep`/`awk`/`sed`/`cut`/
`sha256sum`. No build, test, linter or formatter was run; the frozen counter `accept-c.py` was **not**
executed (its committed receipts and source were read, and its two URL functions were re-implemented
independently in scratch to reproduce the recorded COLLCHECK verdict). Scratch
`/fast/scratch/hyaku/kotodama-r76/ExecMapAudit/` was removed before yielding.

## 8. Answers to the assigned questions, in one line each

* **Is S908/S935→S894 correct?** Yes — one document (`digital.archives.go.jp/search`), live form and
  same-page Wayback capture; the landed row S894 names both URLs; map lines 541–580; counter-compatible.
* **Is S932/S938→S895 correct?** Yes as a document fact (the `showGb` route 302-redirects to the
  `newGbInfo` record, byte-identical body, measured in wave 1), and the landed row S895 names the
  `newGbInfo` live + capture URLs — **but** the map records `S938` under its own alias URL
  (`showGb?type=online&hcno=…`, map line 607) and the row records the alias as prose only, so the frozen
  counter's URL-identity rule red-lights this one edge (COLLCHECK, at the freeze and at the landing).
* **Is S937→S896 correct?** Yes — one document (`news.gmw.cn/2017-05/23/content_24559485.htm`); landed
  row S896 names it; counter-compatible.
* **URL representation mismatch:** the map joins by *document* (measured 302) but records the alias URL;
  the counter joins by *URL string/path identity*; the landed row states the alias without scheme/host, so
  the two never meet. Fix by making the alias a full URL in row S895's source cell (§3.4).
