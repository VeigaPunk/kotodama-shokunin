# RevRows — round-71 wave 2, registry rows S861–S873

Seat: `L1Kotodama71.RevRows` · reviewer (falsify) · leaf, no spawns · 2026-10-25
Scope: `corpus/SOURCES.md` rows S861–S873 (lines 816–828), their anchor cells, and
their `used-by` target. Read-only on the lane; the only file written is this one.
No tool installed, no pacman transaction, no mutation of lane bytes.

Method: re-derived every count from the landed bytes with an independent parser,
re-ran the seven frozen census commands and the two read-only checkers, and
re-opened **all 13** source rows (7 UNESCO captures, RAD capture, 5 live pages),
not the 3 the dispatch asked for.

---

## 1. Assignment checklist (PASS/FAIL, exact commands)

| # | item | result | command / evidence |
|---|---|---|---|
| 1 | valid 11 columns | **PASS** | `awk -F'\|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ && NF!=13 {n++} END{print n+0}' corpus/SOURCES.md` → `0` (all 797 rows NF=13; the header row names exactly the 11 columns `id source kind tier scope anchor teaches status opened recheck used-by`) |
| 2 | no pipe inside cells | **PASS** | same NF!=13 = 0; a fixed-string grep for the escape sequence returns `0` with exit 1 (no match), so no cell smuggles a pipe past the split — command in the block below |
| 3 | tier A/B, no community-A | **PASS** | 12×A + 1×B across S861–S873; census tier leg `A=486 B=299 C=12`; kind leg `spec\|docs\|paper\|code\|tool\|dataset\|talk\|book\|community\|own-work` prints nothing; community rows are B=10 / C=7, no A |
| 4 | opened 2026-10-25 | **PASS** | 13/13 `opened=2026-10-25` (field 9); matches the lesson Gate access dates, `corpus/lessons/round-71.md:19-31` |
| 5 | status mined | **PASS** | 13/13 `status=mined`; census `mined=702 queued=58 rejected=37`; each is cited by its `used-by` path (item 6) |
| 6 | used-by exactly the entry path | **PASS** | 13/13 cell == `corpus/knowledge/culture-material/dance-performance-movement-codes.md`, no second path, no trailing separator; census used-by leg (each mined row's paths piped through an existence test) prints nothing |
| 7 | anchors point to real sections | **PARTIAL** | all 13 pages re-fetched and all 13 Gate quotes located verbatim (≤25 words) in the named page's body; but 2 locators mis-name their target (S872, S873) and 2 paragraph indices use a different base from the other 5 UNESCO rows (S861, S866) — §2 |

Supporting count re-derivations (independent of the round's counters):

```
grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md            → 797
grep -cF '\|' corpus/SOURCES.md                                                 → 0 (exit 1, no match)
python3 (own parser): rows 797, first S001, last S873, unique 797, dups [], sorted True
awk duplicate-id leg (census cmd5)                                              → (empty)
ids S861..S873 contiguous immediately after S860, all inside `## Registry` (26–828)
find corpus/knowledge/culture-material -maxdepth 1 -type f | wc -l              → 36
find corpus/knowledge -type f -name '*.md' | wc -l                              → 243
grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md                    → 797
```

Claim-C counter legs reproduce (`reports/round-71/telemetry/measures-c.txt`:
`registry=797`, `distinct S-ids cited=13`, `entries-cited: 13`, `usedby-paths: all exist`).

Read-only checkers, both exit 0:

```
python3 -B tools/check-source-access.py --root .            → ACCESS: 3 flagged rows, 0 findings (exit 0)
python3 -B tools/check-cited-lines.py corpus/knowledge/culture-material/dance-performance-movement-codes.md
                                                            → CITED-LINES: 0 finding(s) in 1 file(s) (exit 0)
```

Seven frozen census commands (`CENSUS` of `reports/round-49/run-validation.py`,
executed as strings, never via the runner — the runner rewrites its own
`validation.json`, round-71 lesson "landing" mistake): all exit 0, outputs
`797` / `0` / `A=486 B=299 C=12` / `mined=702 queued=58 rejected=37` /
empty / empty / empty.

Gate quotes: all 13 parsed out of `corpus/lessons/round-71.md:19-31` and matched
verbatim against the re-fetched page text — `S861 15w, S862 12w, S863 8w, S864 10w,
S865 8w, S866 10w, S867 7w, S868 10w, S869 11w, S870 6w, S871 10w, S872 8w,
S873 6w`, 13/13 verbatim, 13/13 ≤25 words.

---

## 2. Findings

### HIGH-1 — `id-renumber-map.json` targets 13 ids the round has now occupied

`/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-71/assimilation/id-renumber-map.json`
is frozen pre-landing: `registry_count: 784`, `next_free: "S861"`, `map` = every
staged id shifted +2 (`S859→S861 … S990→S992`). The round then landed S861–S873,
so `sorted(set(map.values()) & {S861..S873})` is exactly those 13 ids — applying
the map today renumbers a staged document onto a live registry row (UNESCO Tango
etc.). Post-landing the correct base is `next_free: "S874"` and a +15 shift, not +2.

The lesson states the artifact as current — `corpus/lessons/round-71.md:73`
"id-renumber-map.json S861→S992 by document" — with no note that its target
space is now the lane's own rows, and `reg-ids`/`staged-ids` (784 / 132) are
likewise pre-landing. Adoption is CLOSED and the lesson records "No shokuknow
bytes adopted, appended or renumbered", so no id is corrupted today; the defect
is that the only adoption gate on disk would corrupt 13 ids if used. Fix: re-emit
the map at the post-landing base (next_free S874, registry_count 797) and say so
in the lesson, or stamp the file `pre-landing, superseded by S861–S873`.

### MEDIUM-1 — S861 and S866 number their paragraph from a different base than the other five UNESCO rows

Counting the element record's own block sequence (`<p style="font-size:1.5em">Inscribed in …</p>`
= ¶1), which is the base that fits 5 of 7 rows:

| row | line | quote paragraph | row anchor | |
|---|---|---|---|---|
| S861 | 816 | ¶2 (¶1 = "Inscribed in 2009 (4.COM)…") | ¶1 | **off by one** |
| S862 | 817 | ¶3 | ¶3 | ok |
| S863 | 818 | ¶2 | ¶2 | ok |
| S864 | 819 | ¶3 | ¶3 | ok |
| S865 | 820 | ¶2 | ¶2 | ok |
| S866 | 821 | ¶2 (¶1 = "Inscribed in 2022 (17.COM)…") | ¶1 | **off by one** |
| S867 | 822 | ¶2 | ¶2 | ok |

Under the other reading (narrative prose only, status line not counted) the split
inverts: S861/S866 are right and S862/S863/S864/S865/S867 are off by one. There is
no documented base anywhere — the wave-1 scout report states no paragraph at all
(`.ufo/waves/round-71/w1/ScoutOpenSourcesC.md`), so the column is internally
inconsistent whichever base a re-opener picks. The same index is propagated into
`corpus/knowledge/culture-material/dance-performance-movement-codes.md:3-9` and
into the lesson Gate grounds (`corpus/lessons/round-71.md:19-25`), so a fix has
three call sites. Evidence (capture HTML, block extraction):

```
S861 https://web.archive.org/web/20260925201518/https://ich.unesco.org/en/RL/tango-00258
  p1 "Inscribed in 2009 ( 4.COM ) on the Representative List …"
  p2 "The Argentinian and Uruguayan tradition of the Tango …"   <== quote
S866 https://web.archive.org/web/20241111072724/https://ich.unesco.org/en/RL/talchum-…-01742
  p1 "Inscribed in 2022 ( 17.COM ) on the Representative List …"
  p2 "Talchum is a performing art that encompasses dance, music and theatre …"  <== quote
```

### MEDIUM-2 — S873's anchor names section 1, the quote is in the unnumbered preamble

`corpus/SOURCES.md:828` anchor: "entry “The Philosophy of Dance”, section 1
(methodological questions)". On `https://plato.stanford.edu/entries/dance/` the
quoted sentence — "What counts as “philosophy” of dance? This is a vexed
methodological question." — is in the **preamble**, before any numbered section.
Section 1 is headed "1. Analytic Approaches to Dance as Art" and is about the
definitional/ontological/identity questions, not about the methodological
question. QUALITY 18 requires the anchor quote findable in the named anchor's
body: it is findable in the entry, but not in the section the cell names. The
mis-locator is propagated to the entry source line
(`dance-performance-movement-codes.md:15` "section 1, methodological questions").
Fix: "entry preamble (methodological question); §1–§1.2 for the
definition/ephemerality debates".

### MEDIUM-3 — S872's anchor calls a Wisdom Library site Summary the "edition preamble"

`corpus/SOURCES.md:827` anchor: "mirror-of-gesture edition preamble
(Coomaraswamy translation)"; teaches: "the manual's own description frames it as
an encyclopedic gesture lexicon". The quote "an encyclopedic manual of the art of
gesticulation" is Wisdom Library's own `*Summary*` blurb on the book landing page
(`https://www.wisdomlib.org/hinduism/book/the-mirror-of-gesture`), repeated
verbatim as the `meta-description` and on every page of the book (checked
`/hinduism/book/the-mirror-of-gesture/d/doc143254.html`, where the same Summary
block sits above the Introduction heading; Coomaraswamy's Introduction body
begins "Mr. Gordon Craig, who understands so well the noble artificiality of
Indian dramatic technique…" and does not contain the phrase). So the locator
names a text that does not hold the quote, and the teaches attributes an
aggregator blurb to the manual itself. Under QUALITY 6 ("publisher descriptions
and abstracts are tier B for substantive claims about a work") the quote cannot
carry the "primary" framing of the row; the row's tier-A rests on the source
being a primary treatise, not on this anchor. Fix: re-anchor to a located span in
the Coomaraswamy text (e.g. the Chapter 4 gesture chapter, `doc143261.html`) or
restate teaches as "Wisdom Library's summary describes the manual as …".

### MEDIUM-4 — 5 of 13 rows name no same-page Wayback capture

QUALITY 18: "A registry row's source cell names one live URL plus a wayback
capture of that same page". Rows S868 (823), S870 (825), S871 (826), S872 (827),
S873 (828) carry a single live URL. The other 8 (S861–S867, S869) carry live +
capture and all 8 pass the embedded-original leg (extracted original == live URL,
query-aware: `MATCH` 8/8). All five live pages did serve the quote to my re-open
today (ABT dictionary, ickl.org, wisdomlib doc209696, wisdomlib mirror-of-gesture,
plato.stanford.edu), so the rows are re-openable now but not durable; QUALITY 18
sends a row with no capture *and* an unservable live URL to `rejected`. Note the
round's own shape review does not cover this leg —
`grep -n 'wayback\|archive.org\|capture' .ufo/waves/round-71/w1/RevSOURCESRowShape.md .ufo/waves/round-71/w1/ExecSOURCESRowTemplate.md`
is empty — and 512/797 registry rows are live-only (40 in S700+), so this is a
lane-wide backlog the round inherited rather than invented. Report it as a shape
deviation to be declared, not a false citation.

### LOW-1 — S866 teaches claims improvisation the inscription does not state

`corpus/SOURCES.md:821` teaches: "documents masked dance-drama as a compound form
with social-critical improvisation". In the capture the string `improv` occurs
only inside the thesaurus `Concepts` list ("Improvisation (77)"); the inscription
narrative has dance+music+theatre, social criticism, audience cheers/jeers and
"any empty space can become a venue", but no improvisation. Drop the word or cite
the tag list explicitly.

### LOW-2 — S870 calls the homepage about-text a "charter"

`corpus/SOURCES.md:825` teaches: "the ICKL's own charter names Labanotation and
its practitioner base". The located text is the homepage "You are here: Home"
about paragraph ("The International Council of Kinetography Laban was founded in
England in 1959 … Its members practice the system … known as Kinetography Laban
or Labanotation"); the site's `Statutes` is a separate nav item that was not read.
Scope ("provenance and scope") is supported; only the word "charter" overstates.

### LOW-3 — S868 tier A for a cross-school divergence claim

`corpus/SOURCES.md:823` scope: "ballet movement vocabulary as a named term
register; school-dependent arm positions show code divergence". ABT's dictionary
is authoritative for ABT's own usage and for its statement about its own
positions, but it is a secondary witness to the Cecchetti, French and Vaganova
arm positions it summarises. QUALITY 6 reserves A for a source "primary or
authoritative for the exact scope"; the entry's use
(`dance-performance-movement-codes.md:36-37`) is the divergence claim. A judgment
call, not a mechanical fail — flag for the tier reviewer, do not edit in place
(QUALITY 6: correct a filed tier with a superseding row).

### LOW-4 — 4 opened candidates vanished between the scout report and the registry, unreasoned

`.ufo/waves/round-71/w1/ScoutOpenSourcesC.md` opens 17 candidates; 13 landed.
Candidates 13–16 (Britannica "dance" B, Hanna *To Dance Is Human* B, Royce
*The Anthropology of Dance* B, Sachs *World History of the Dance* B) are not
named in the lesson's reject sweep (`corpus/lessons/round-71.md:33-40`, which
claims to be "the explicit reject-sweep statement (V70-5)"). They were never
rows, so no registry rule is broken, but the round's accounting for opened
candidates is incomplete: 17 opened ≠ 13 rows + 8 refused.

---

## 3. Anchor spot-check — all 13 re-opened

| row | named locator | fetched | quote located in named anchor | note |
|---|---|---|---|---|
| S861 | element record 00258, inscription narrative ¶1 | capture 20260925201518 | yes (narrative ¶2 by the 5/7 base) | MEDIUM-1 |
| S862 | 00100, narrative ¶3 | capture 20220323094705 | yes (¶3) | — |
| S863 | 00337, narrative ¶2 | capture 20210514035531 | yes (¶2) | — |
| S864 | 00003, narrative ¶3 | capture 20210227223454 | yes (¶3) | — |
| S865 | 00363, narrative ¶2 | capture 20210302140159 | yes (¶2) | — |
| S866 | 01742, narrative ¶1 | capture 20241111072724 | yes (narrative ¶2) | MEDIUM-1 |
| S867 | 00163, narrative ¶2 | capture 20200330004935 | yes (¶2) | — |
| S868 | Ballet Dictionary, "Positions of the arms" paragraph | live abt.org | yes — the `bras, positions des` entry, body "Positions of the arms. Although the positions of the feet are standard in all methods…" | locator is entry body text, not a heading; acceptable |
| S869 | Benesh International page, opening ¶ | capture 20260907171642 | yes — "Benesh Movement Notation (BMN) is a system for documenting human movement." | — |
| S870 | ICKL homepage, opening ¶ | live ickl.org | yes — "…originated by Rudolf Laban, known as Kinetography Laban or Labanotation." | LOW-2 |
| S871 | chapter IV (karaṇa), aṅgahāra section | live wisdomlib doc209696 | yes — "Chapter IV – Description of the Class Dance (tāṇḍava)", §*Aṅgahāras*, "Thus the Aṅgahāras consist of six, seven, eight or nine Karaṇas." | — |
| S872 | mirror-of-gesture edition preamble | live wisdomlib book root | quote on page, but as the site Summary, not the edition preamble | MEDIUM-3 |
| S873 | entry §1 (methodological questions) | live plato.stanford.edu | quote in the unnumbered preamble; §1 is "Analytic Approaches to Dance as Art" | MEDIUM-2 |

Additional scope-vs-text checks that came back clean: S864's "dancer/musician
counts" are in the narrative ("More than 28,000 dancers and 10,000 musicians
organized in about 50 groups"); S865's "gender-differentiated movement technique"
is in the narrative ("differing depending on whether the performer is male
(heavier use of the feet) or female (gentler, more sensual movements)") and
"transmission through dynasties" is verbatim; S867's onnagata/mie/stage devices
are all in the narrative.

---

## 4. Residual risk

- **Anchor prose is review-only.** Criterion 18's mechanical leg (quote findable
  in a named anchor) passes 13/13; the *precision* of a locator (which paragraph,
  which section, which text of a page) has no checker, so MEDIUM-1/2/3 are
  reachable only by a seat that re-fetches. The round's wave-1 shape review
  checked grammar, not locators.
- **Durability of 5 rows** depends on live pages only (ABT, ICKL, wisdomlib ×2,
  SEP). All five served the quote today, but the same fetch class walled the
  wave-1 scout elsewhere (RAD live 403, ROH live 500, Princeton Noh 403, DNB
  unreachable) — the RAD row survives only because it carries a capture. A future
  403 on any of the five leaves the row with no same-page fallback.
- **The census is green and says nothing about anchors.** 797 / NF=13=0 / enums /
  used-by-exists all pass while 2 rows carry a wrong paragraph base and 2 a wrong
  section name: the counters cannot see this class, so a PASS from RevCounterC
  and a PARTIAL from this seat are both correct.

## 5. Verification gaps

- I read the 13 pages as rendered/parsed text (Wayback capture HTML and live
  HTML), not as a browser session; the paragraph indices are derived from the
  `<p>` block sequence of each capture, which is the only mechanical reading
  available. If the lane intends "paragraph" to mean something else (e.g.
  rendered visual paragraphs after CSS), MEDIUM-1's base must be restated — but
  the inconsistency between S861/S866 and the other five holds under either base.
- UNESCO live pages are CAPTCHA-walled (wave-1 scout); I did not attempt them,
  only the named captures. The captures are 2020–2026 and each served its quote.
- `ickl.org` is http-only; I fetched it over http as the row states, no TLS
  verification question arises.
- I did not run `reports/round-71/accept-c.py` (RevCounterC owns it) and did not
  run `reports/round-49/run-validation.py` in the lane (it rewrites its filed
  `validation.json`); its `CENSUS` strings were executed individually instead.
- The renumber-map finding (HIGH-1) is adjacent to my slice (same id space); I did
  not audit the quarantine verdict table or the receipt re-stamps.
