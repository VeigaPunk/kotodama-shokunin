- Seat: C02 | executor | claim C | date 2026-10-19 | baseline ce103bf

# C02 — second independent audit of the r35 timekeeping spare + the `corpus/README.md` rev 2.1 delta

- Round 36, seat **C02**, role **executor**, claim **C** (coverage). Mission (verbatim,
  `reports/round-36/targets.json` → `seats[id=C02].mission`): *"Second independent audit + the
  README delta draft (rev 2.1: header 25, totals 212, footer vector 21/23/25/29/20/94, row in
  filename order)."* Out path `reports/round-36/cov/C02-audit-delta.md`.
- Lane root `/home/vgpnk/Projects/shokunin/kotodama-shokunin`; `git rev-parse HEAD` →
  `ce103bf5885af00023cdc4a174c17602476cdcf8`; `git status --porcelain corpus/` empty at the cut.
- **Canon: NON-CANON.** This seat audits bytes and drafts a delta; it admits no entry, certifies no
  round, promotes nothing, and is not promotion verification. A green reading below is a structural
  reading of bytes at a named digest — never a verdict on the scholarship, never canon
  (`PROVINCE.md:20-27`).
- **Writes**: this file only, plus gitignored scratch under `.scratch/c02/`. No `corpus/**` byte, no
  `tools/**` byte, no filed round-1..35 byte, no `.ufo/**`. No commit, no push, no install, no network.
- **F-C13-1 honoured**: no `reports/round-*/run-validation.py` was executed, in-tree or in any copy.
  No `--freeze` of `reports/round-34/handoff/declared-in-r7` was run. The only filed code executed is
  the read-only `reports/round-28/readme/sweep.py` (live mode, and imported read-only against a
  scratch tree).
- **Independence.** This seat did not read `reports/round-36/cov/C01-audit.md` until §2.5, after its
  own readings were taken; the two audits' agreements and disagreements are reported as such.

## 0. Verdict at a glance

| # | reading | class |
|---|---|---|
| 1 | the spare **is not landed**; `corpus/knowledge/culture-material/timekeeping-instruments.md` does not exist; `corpus/README.md` still rev 2.0 | measured |
| 2 | the spare's **26 quoted absence terms reproduce exactly at its pinned authoring HEAD `4a7aede`** (26/26 → 0 files) | measured |
| 3 | **exactly one term has drifted** since: `curfew` 0 → **1** file at `ce103bf`, and that file is a **round-35 landing** (`fire-fuel-light.md`) | measured |
| 4 | the spare's near-miss counts are **also authoring-pinned**: `clock` 6 culture-material files at `4a7aede` → **10** now; `bell` 81 → **87**; `hour` (word-bounded) 8 → 11 | measured |
| 5 | the spare's **structural contract passes**: 8/8 frontmatter fields, decision record, gap statement, canon boundary | measured |
| 6 | **49 raw backticked repo tokens → 30 distinct paths after `:line` stripping → 28 resolve**; the 2 unresolved are not pointers (a glob literal `corpus/knowledge/*/*.md` and an elided-form literal `corpus/knowledge/...`, both inside quoted commands); 8 attached `path:line` tokens, 0 out of range | measured |
| 7 | **two live defects in the FILED `corpus/README.md`** (rev 2.0): a stray blank line splitting the culture-material section, and three rows out of ASCII order | findings **F1**, **F2** |
| 8 | the lane's index instrument (`reports/round-28/readme/sweep.py`) **reads exit 0 over both defects** — an instrument blind spot, not a false reading | finding **F3** |
| 9 | the rev 2.1 delta **drafted below is measured, not asserted**: on a staged tree it reads `rows 212 files 212`, 0 missing, 0 ghosts, 0 topic mismatches, `header_drift {}`, `totals_line 212`, `footer_ok True`, exit 0 | §4 |
| 10 | the delta **also repairs F1 and F2**, and the repair is checked by an independent order/contiguity/duplication leg with a negative control that fires on the filed bytes | §4.4 |

## 1. The audited bytes, and their pins

| field | value |
|---|---|
| fragment | `reports/round-35/cov/C04-timekeeping-spare.md` |
| fragment sha256 | `258fb166e35f3b0f92854dcb7c5e08fcfc285c51a42aa828cb79f3f761f5bcd2` |
| fragment bytes / lines | 40 646 / 150 |
| fenced block | one, 3-backtick ``` ```markdown ``` open at `:9` / ``` ``` ``` close at `:150` |
| extracted entry bytes | **40 234** |
| extracted entry sha256 | `9805c0b854334ed396119476b6278cc4f58eb1014a0b06eb6bba561def05f0a6` |
| entry sha256[:16] | `9805c0b854334ed3` |
| staged by this seat at | `.scratch/c02/tree/knowledge/culture-material/timekeeping-instruments.md` |
| `corpus/README.md` at `ce103bf` | sha256 `51b966af20483328c3e221d2ab0f766aa5cf0f5a0b140650b95eb841d6bea6f0`, 125 229 bytes, 524 lines |
| index instrument | `reports/round-28/readme/sweep.py` sha256 `9b2ccac0046831fdaf48863ccd0ff6ca0fa390d044746c876e83a71c06f0cdd3` |

The extracted entry digest **matches C01's independent reading byte-for-byte** (`9805c0b854334ed3`,
40 234 bytes) — two seats, two extraction scripts, one digest. This is a consistency result between
instruments, not a correctness proof of the content.

## 2. The audit, leg by leg

### 2.1 Frontmatter — 8/8 present

Command: `python3 - <<'EOF'` over the extracted entry, `re.search(r'^- %s:' % f, body, re.M)` for
`f in [topic, gap filled, sources, source, couples, verified-at, recheck, scope]` → **all 8 present**.
The binding reading `R35-4F-1` (`reports/round-35/claims.json:24`) is satisfied with margin: its
source leg accepts `- sources:` **or** `- source:` (the spare carries both), and its scope leg accepts
`- scope:` **or** `- couples:` (the spare carries both).

### 2.2 Pointer resolution — 28/30 resolve, and the two misses are not pointers

Command: every backticked token matching `(corpus|tools|reports|examples)/….(md|json|py|yml|yaml|tsv|txt)`
was extracted, `path:line` suffixes stripped, and each path tested with `os.path.exists`.

Result: **49 raw tokens → 35 distinct → 30 distinct after suffix-stripping → 28 resolve**, 2 unresolved:
`corpus/knowledge/*/*.md` and `corpus/knowledge/...`.

That first one is the **operand of the spare's own absence sweep** (the `for kw in …; do grep -ril --
"$kw" corpus/knowledge/*/*.md | wc -l; done` loop), i.e. a glob literal inside a quoted command, not a
citation to a file. The second is the elided form the spare itself uses when introducing that sweep
("over `corpus/knowledge/*/*.md` (201 files at HEAD 4a7aede)") — an ellipsis, not a path. Both are
reported as **reading notes, not defects**. Independently, this seat re-ran that sweep over the real
tree (§2.3), which is the check that actually matters.

Attached `path:line` citations: **8 distinct tokens carry a line/range suffix**; every line number is
within its file's line count → **0 out of range**. This is a **lower bound** on the spare's citation
density: the corpus's dominant form (`` `path.md:13` ``) is counted here, and this seat's leg, like
C01's and like the round-35 interop findings (`reports/round-35/cov/C13-audit-1-5.md` F12), sees
fewer tokens than a full prose scan would. The count is reported as measured, not as "all citations
verified".

### 2.3 The absence sweep — reproduces exactly at the authoring pin, and one term has drifted

The spare's `- gap filled:` line quotes a 26-term loop. This seat parsed the loop out of the entry
bytes (parse: `re.search(r'for kw in (.*?); do', body, re.S)`, then
`[a or b for a, b in re.findall(r'"([^"]+)"|(\S+)', loop)]` → **26 terms**) and ran it against both
trees:

| tree | reading |
|---|---|
| `git grep -il -- "$kw" 4a7aede -- corpus/knowledge` (the spare's own pin) | **26/26 terms → 0 files** — the quoted sweep **reproduces exactly** |
| `grep -ril -- "$kw" corpus/knowledge/*/*.md` at `ce103bf` (the delivered tree) | **25/26 terms → 0 files; `curfew` → 1** |

The single drifted term, with its cause:

| term | @ `4a7aede` | @ `ce103bf` | first matching file | cause |
|---|---|---|---|---|
| `curfew` | 0 | **1** | `corpus/knowledge/culture-material/fire-fuel-light.md` | a **round-35 landing**; its `:3` gap line and `:82` section own the curfew as a fire ordinance that became a time ordinance |

`curfew` occurs in that file at `:3`, `:20`, `:27`, `:75`, `:82`, `:112`, `:131`, `:153` — the
landing postdates the spare's sweep, so this is **landing drift, not an authoring error**. The
inference the spare draws from the sweep ("no entry anywhere in the corpus covers the instrument") is
**weakened, not broken**: `fire-fuel-light.md` owns the *fire-risk institution* (watch, curfew,
firebreak, hearth tax) and explicitly hands the instrument itself onward — `fire-fuel-light.md:3`
lists the neighbouring owners and `:27`/`:75` treat the curfew as a lighting budget, not a
timekeeping device. The correct disposition is a **delta note on the spare**, not a rewrite of its
gap statement.

### 2.4 Near-miss counts — also authoring-pinned, and also drifted

| term | spare says | this seat @ `4a7aede` | @ `ce103bf` | verdict |
|---|---|---|---|---|
| `astrolabe` | 2 files | 2 | 2 | reproduces, stable |
| `"star clock"` | 2 | 2 | 2 | reproduces, stable |
| `chronometer` | 2 | 2 | **4** | drifted (two round-35 landings) |
| `obelisk` | 1 | 1 | 1 | reproduces, stable |
| `meridian` | 1 | 1 | 1 | reproduces, stable |
| `"time zone"` | 1 | 1 | 1 | reproduces, stable |
| `hour` | 8 files | 8 (`-w`) / 12 (plain) | 11 (`-w`) | reproduces under word boundaries |
| `bell` | 81 files | 81 | **87** | drifted |
| `clock` (culture-material) | 6 files | **6** | **10** | drifted |

The `clock` row is the load-bearing one and it **reproduces exactly at the pin**: `git grep -il --
clock 4a7aede -- corpus/knowledge/culture-material | wc -l` → **6**, the number the spare prints.
It is 10 at `ce103bf` because round 35 landed four more culture-material entries that use "clock"
as metaphor or calendar mechanics (`agrarian-field-system-lexicon.md`, `funerary-material-culture.md`,
`writing-media-surface-economy.md`, `fire-fuel-light.md`) — which is the *same class* the spare
already dispositions ("all of them metaphor or calendar mechanics"). So the spare's reading is
**true at its pin and correctly characterised**; only its currency is stale.

### 2.5 Against C01 (read after the above readings were taken)

C01's §0 rows 4–5 and its findings F3/F4/F5 agree with this seat's §2.3/§2.4 on the substance:
the sweep reproduces at the pin, the corpus has since moved, and no drift disclosure is carried. Two
differences, both recorded rather than smoothed:

- **C01 files the stale currency as a defect (F4, S3); this seat reports it as a reading with a named
  cause and a delta note.** Same measurement, different tier. The parent should pick one tier.
- **C01's §3.6 drafts the README delta as "arithmetic, not measured"** and does not carry the delta
  bytes. This seat's §4 **measures** the delta on a staged tree and carries the exact bytes; the two
  agree on every number (`(24)`→`(25)`, `211.`→`212.`, footer vector `21/23/24/…`→`21/23/25/…`).
- **Neither C01 nor the spare's landing arithmetic names F1/F2.** The README defects in §3 are new
  readings this seat contributes; they change the *shape* of the delta, not its numbers.

## 3. Defects in the FILED `corpus/README.md` (rev 2.0)

Both are live in the filed blob (`git show ce103bf:corpus/README.md` sha256
`51b966af20483328c3e221d2ab0f766aa5cf0f5a0b140650b95eb841d6bea6f0`), not artefacts of the working
tree: the working-tree file hashes identically.

| # | sev | finding | evidence |
|---|---|---|---|
| **F1** | **S2** | **A stray blank line splits `## culture-material/`.** Line 211 is empty, between `warrior-material-culture.md` (line 210) and `writing-media-surface-economy.md` (line 212). The section therefore reads as two runs, and the last row is visually orphaned from its section. Every other section is contiguous. | `awk 'NR>=209 && NR<=213' corpus/README.md` → rows at 209, 210, **211 blank**, 212; blank-line scan over all six sections: `linguistics [137,159] myth-symbol [161,185] culture-material [187,**211**] synthesis [214,244] verification [246,267] civilizations [269,364,366,491,493,506,510,514,519,524]` — only the trailing blank at `159`/`185`/`244`/`267` is normal |
| **F2** | **S2** | **Three culture-material rows are out of ASCII order.** Lines 198–200 read `furniture-interior-lexicon.md`, `funerary-material-culture.md`, `fire-fuel-light.md`; the section's own convention (and C11's §0/§3 rule, `reports/round-35/cov/C11-readme-delta.md:37-38,159-161`) is ASCII-ascending, which is `fire-fuel-light.md` < `funerary-material-culture.md` < `furniture-interior-lexicon.md`. | `python3` order leg over the filed bytes → `OUT OF ORDER culture-material [('furniture-interior-lexicon.md','fire-fuel-light.md'), ('fire-fuel-light.md','furniture-interior-lexicon.md')]`. The three names differ at the 3rd character (`r`/`u`/`u`) then the 4th (`e`/`n`/`r`), so the ASCII order is unambiguous |
| **F3** | **S3 (interop)** | **The lane's index instrument cannot see F1 or F2.** `reports/round-28/readme/sweep.py` checks rows/files, ghosts, missing, duplicate rows, topic equality, header drift, totals line and the counts footer — but never row *order* and never *contiguity*. It therefore reads `exit 0` over a section that is split and mis-ordered. | `python3 -B reports/round-28/readme/sweep.py` → `missing_from_index 0 []`, `topic_mismatch 0 []`, `orphan_rows 0 []`, `header_drift {}`, `totals_ok True`, `footer_ok True`, **exit 0** — on the same bytes the order leg calls `OUT OF ORDER` + `NON-CONTIGUOUS` |

**Provenance of F1/F2 — the rev-2.0 landing, not the working tree.** `git show 4a7aede:corpus/README.md`
(the pre-landing blob, 201 files) carries neither row set, so both defects entered with revision 2.0
(round 35). The round-35 delta's own claim (`reports/round-35/cov/C11-readme-delta.md:37-38`) that
"rows are filename-sorted (ASCII ascending) inside every section" is **falsified by the delivered
bytes** for these three rows.

**Why this matters for claim C.** The claim's `after_required` is *"CM 25 / total 212; README rev 2.1
sweep-green (212 rows == 212 files)"*. A delta that only adds a row and moves the counters lands rev
2.1 **sweep-green over a file that still carries F1 and F2** — a green reading that does not certify
the property the README's own revision notes assert. §4 therefore repairs both in the same delta, and
says so in the revision block.

## 4. The rev 2.1 delta (integrator-applied; this seat wrote no corpus byte)

Pre-state: `corpus/README.md` rev 2.0, sha256
`51b966af20483328c3e221d2ab0f766aa5cf0f5a0b140650b95eb841d6bea6f0`, 524 lines, `culture-material 24`,
total 211. Post-state: rev 2.1, sha256 **`fc2e6d070cd7d123b4248e63b42b34a5fba9012c26e96a1918c622b5d2115316`**,
533 lines, 127 680 bytes, `culture-material 25`, total 212. Seven edits, E1–E7.

**Precondition for the acceptance reading (§4.4):** the entry must be staged at
`corpus/knowledge/culture-material/timekeeping-instruments.md` with the §1 bytes (40 234 bytes,
sha256 `9805c0b854334ed3…`) **before** the sweep is run, and the sweep must be run from an isolated
`git archive` copy — never in-tree (F-C13-1).

### E1 — new revision block (insert after line 2)

before (lines 1–3):

```
# kotodama-shokunin corpus index

revision: 2.0 — Round-35 thin-partition expansion landing (2026-10-19): the ten
```

after (lines 1–12):

```
# kotodama-shokunin corpus index

revision: 2.1 — Round-36 timekeeping-instruments landing (2026-10-19): the routed
round-35 spare landed as `culture-material/timekeeping-instruments.md` (author fragment
`reports/round-35/cov/C04-timekeeping-spare.md`); `## culture-material/` moved 24 → **25**,
its row added in filename order with the entry's own `- topic:` text byte-equal; the totals
line and the counts footer moved 211 → **212** and the footer vector 21/23/24/29/20/94 →
**21/23/25/29/20/94**. This revision also repairs two rev-2.0 index defects (below).
Re-measured with `python3 reports/round-28/readme/sweep.py`: 212 rows vs 212 files, exit 0.
Non-canon examples and passing structural gates do not certify historical truth.

revision: 2.0 — Round-35 thin-partition expansion landing (2026-10-19): the ten
```

### E2 — culture-material header (line 186)

```
-## culture-material/ (24)
+## culture-material/ (25)
```

### E3 — F2 repair: re-sort lines 198–200

Delete all three rows and re-insert them ASCII-ascending at the position of the first (line 198).
Net line count unchanged. Byte-exact rows, copied from the filed blob:

```markdown
- `fire-fuel-light.md` — fire as the material system a culture is organized around — the hearth as an institution rather than a fixture (household unit, tax unit, cult center, the smoke it forces into architecture), the fuel ladder (wood → charcoal → peat → turf-dung → coal → oil → gas, each rung moving the fuel further from the household and closer to a trade that owns it), ignition (drill, saw, strike-a-light, fire piston, sulphur splint, phosphorus match) and the kept-embers economy, the light ladder (rushlight, tallow, beeswax, oil lamp, gas, kerosene) with light quality as a rank code, and the fire-risk apparatus — night watch and *vigiles*, curfew as a fire ordinance that became a time ordinance, firebreaks and building codes, the fire engine, the fire mark and the insurance brigade, the hearth tax that turned fireplaces into documents, the chimney sweep — plus the fire word-bank, the archaeological signature of fire (ash, charcoal, rubefaction, destruction layers), a build order, a decision record, and the calibration shelf; boundary stated in §1 (the ritual meaning of fire belongs to myth-symbol, the cookware to `vessel-container-lexicon.md`, the building's heating design to `architecture-settlement-lexicon.md`).
```
```markdown
- `funerary-material-culture.md` — how a culture disposes of its dead, and what that disposal does to everything else it makes — the master claim is that a mortuary system is four coupled machines, DISPOSAL (what the body becomes: earth, fire, air, water, bone, image), ASSEMBLAGE (what is deposited with it and who decides), MONUMENT (what the living build and must maintain), and WORD (the death register: avoidance terms, rite terms, office terms, monument terms), and that these four are wired in a fixed order — the disposal choice constrains the schedule, the schedule constrains the mourning duration, the duration constrains the mourning economy, and the economy generates the enforcement law; the second claim is that **the grave is the only artifact a culture makes for an audience it will never meet**, so it is written in the culture's most conservative register and is simultaneously the richest inference surface and the most trap-laden one; the third is that **grief has a budget** — a mortuary system is the largest per-capita expenditure in most pre-modern economies, which is why every culture that legislates anything legislates mourning duration, mourning dress, and funeral expense; load-bearing real cases: Hertz's double funeral and the secondary-burial interval (Hertz 1907, carried in-corpus at `corpus/knowledge/myth-symbol/ritual-liminality.md:24`); the Egyptian natron process and its 70-day clock (Herodotus *Histories* 2.86–88, (to-verify) fetch); Roman funerary sumptuary law in the Twelve Tables (Cicero *De Legibus* 2.58–2.59, (to-verify) fetch); the Chinese wǔfú 五服 five-grade mourning system enforced through the Tang Code (`corpus/knowledge/culture-material/ritual-garments.md:108`, citing Johnson 1979); the English Burial in Woollen Acts of 1666 and 1678 (`corpus/knowledge/culture-material/dress-through-eras.md:6`, `:95`, `:120`); the Zoroastrian exposure-and-ossuary system; the Tibetan *bya gtor*; the Merina *famadihana* (`corpus/knowledge/civilizations/malagasy-madagascar.md:98`, `:106`, citing Bloch 1971 at `:7`); and the Moche royal burials at Sipán (`corpus/knowledge/civilizations/moche.md:10`, `:29`, `:110`, `:117`, citing Alva & Donnan 1993); the word layer is a four-stratum register with attested etymology chains (*sarcophagus* < Greek *sarkophagos* "flesh-eating"; *coffin* < Old French *cofin* "little basket" < Latin *cophinus* < Greek *kophinos*; *mausoleum* < Mausolus of Caria; *mummy* < Arabic *mūmiyā* < Persian *mūm* "wax"; *dirge* < the Office of the Dead's *Dirige*; *epitaph* and *cenotaph* both built on Greek *taphos* "tomb"), each with a calibration flag where the literature disputes it — plus the disposal typology table, the assemblage-grammar rules, the monument maintenance clause, the mourning-economy law table, a ten-row inference-trap table, a design order of operations, and a decision record (DR-MMC-01..09).
```
```markdown
- `furniture-interior-lexicon.md` — furniture and the interior as a cultural system for fictional cultures — the gap this entry fills, since the partition owns buildings (`architecture-settlement-lexicon.md`) and dress (`dress-through-eras.md`) but no file owns what people sit on, sleep in, eat off, or keep things in; the master claim is that the **seating regime is chosen first** — floor, platform, or chair — and it silently decides table height, room proportions, garment cut, servant posture, and the grammar of rank, so it must be fixed before any furniture is named; the three-regime typology with real exemplars (Japanese tatami and seiza, Korean ondol, Indian āsana and the charpoy, the Islamic majlis cushion line, the Greek klismos/diphros/klinai, the Roman triclinium and late stibadium, the Chinese huchuang 胡床 folding stool and the Tang–Song turn to chair-and-table sitting); the chair's rank career (sella curulis and thronos/solium, kathédra → cathedral, the seat as office: chairman, the Chair, the bench, the electoral seat, the Japanese *za* 座, the Scottish stool of repentance); sleeping (the bed as rank object and semi-public stage — the state bed and the *ruelle*, the box-bed and Dutch *bedstede*, the folded futon, the kang 炕 platform, the Great Bed of Ware and the "second best bed with the furniture" as furniture in law); tables (boards and trestles, the table's institutional children — room and board, board of directors, the Lord's Table, the Covenanters' Tables, the Exchequer's checkered cloth cross-read from `trade-economy-lexicon.md`); storage furniture as document (the chest/coffer as archive and dowry record, cabinet and wardrobe as rooms that became departments of state and then pieces of furniture, the closet as privacy institution); screens, hangings and canopies as privacy technology; the un-sittable seat (the Asante Golden Stool, Luba caryatid stools) and the vacant seat as a holder for an absent guest; the calibration shelf of standing myths (crude-medieval furniture, chair = authority everywhere, the ancient fixed dining table, the private bed, furniture as trivia); a decision-record table; a build order and one non-canon worked micro-example. Reference and method only; canon decisions are lore-shokunin's.
```

The three rows' own digests, so the integrator can verify the copies rather than trust them:
`fire-fuel-light.md` row `a761585a354a1e11…` (1 261 bytes), `funerary-material-culture.md` row
`c757326c202b1837…` (2 914 bytes), `furniture-interior-lexicon.md` row `83c9c42125d2b4ab…`
(2 292 bytes), each including its trailing newline.

### E4 — the new row, in filename order (after `textile-technology.md`, line 206)

Insertion anchor: the line reading `` - `textile-technology.md` — … `` (line 206); the new row goes
**immediately after it** and **before** `` - `trade-economy-lexicon.md` — … `` (line 207). ASCII order
confirms the position: `textile-technology.md` < `timekeeping-instruments.md` < `trade-economy-lexicon.md`.

The row is generated from the entry's own `- topic:` head-block text, continuation lines space-joined
to one line — never retyped (`reports/round-28/readme/sweep.py:21-22,74-79,140`). Byte-exact:

```markdown
- `timekeeping-instruments.md` — the timekeeping instrument as a material-culture system for fictional cultures — the five instrument families that measure the day before and beside the clock (SHADOW: gnomon, obelisk, the sundial families Vitruvius catalogues, portable dials; FLOW: the clepsydra as legal timer and its constant-head fix; FIRE: calibrated candle, lamp and incense measures; SKY: decan star clocks, the astrolabe, the nocturnal; WHEEL: the escapement, tower clock, pendulum, chronometer, quartz) each with its resolution, failure mode and what it leaves in the ground; the variable-hour (temporal) regime against the equal-hour regime as the single biggest design decision, with Roman, monastic, Islamic, Edo Japanese and Italian-hour anchors; the unit ladder by which an instrument's resolution becomes the smallest unit a culture can *name* (hour → minute → second, sexagesimal inheritance) and what each rung enables; the institutions a time device generates (bell and tower, curfew, market bell, night watch, canonical hour, muwaqqit, timekeeper office, clockmakers' guild, standard time); the ownership question — temple, palace, city, state or employer — as the axis that decides whether time is public or private; the archaeology of timekeeping (what survives, what decays, what an in-world antiquarian can read); a calibration bank of legend-grade and contested items (Alfred's candles, the monks-invented-the-clock story, Salisbury's 1386 date, Chinese-to-European escapement diffusion, clock-as-cause-of-industrialism, sundial-time = clock-time); a twelve-row decision record; a build order with one NON-CANON worked example. Reference knowledge and method only; canon decisions belong to lore-shokunin.
```

Row digest: `49e67b35d3df34bd568d18ba82299c78d59861735c2c4a7cb3f3e7121c7c0982`, **1 741 bytes**
(1 706 topic bytes + the `` - `timekeeping-instruments.md` — `` prefix of 35 bytes), **one line**,
trailing newline included.

### E5 — F1 repair: delete the blank line (line 211)

```
 - `warrior-material-culture.md` — … the five armor-construction systems …
-
 - `writing-media-surface-economy.md` — … the surface economy of inscription …
```

Delete the empty line only. Net line count −1. After E3–E5 the culture-material section is
contiguous and ASCII-ascending.

### E6 — totals line (line 492)

```
-Total knowledge entries: 211.
+Total knowledge entries: 212.
```

### E7 — counts footer (line 496)

```
-(total 211 files; directory totals 21/23/24/29/20/94).
+(total 212 files; directory totals 21/23/25/29/20/94).
```

The footer's **date line (494) and command line (495) are already correct** and need no edit: they
read `Counts checked 2026-10-19 from the repo root:` and
`` `python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge` `` — this
revision moves only the numbers, not the date or the command. A stale **date** is a known blind spot
of the sweep (`reports/round-35/review/R03-c-review.md` §1.3), so it is called out explicitly here
rather than assumed.

### 4.1 The delta as a unified diff

```diff
--- a/corpus/README.md
+++ b/corpus/README.md
@@ -1,2 +1,11 @@
 # kotodama-shokunin corpus index
+
+revision: 2.1 — Round-36 timekeeping-instruments landing (2026-10-19): the routed
+round-35 spare landed as `culture-material/timekeeping-instruments.md` (author fragment
+`reports/round-35/cov/C04-timekeeping-spare.md`); `## culture-material/` moved 24 → **25**,
+its row added in filename order with the entry's own `- topic:` text byte-equal; the totals
+line and the counts footer moved 211 → **212** and the footer vector 21/23/24/29/20/94 →
+**21/23/25/29/20/94**. This revision also repairs two rev-2.0 index defects (below).
+Re-measured with `python3 reports/round-28/readme/sweep.py`: 212 rows vs 212 files, exit 0.
+Non-canon examples and passing structural gates do not certify historical truth.
 
@@ -185,3 +194,3 @@
 
-## culture-material/ (24)
+## culture-material/ (25)
 
@@ -197,5 +206,5 @@
 - `era-periodization-models.md` — The systems by which cultures divide their own history — the Sinosphere era-name family (Chinese nianhao, Japanese nengō, and the offshoots: Vietnamese niê …[+1158 bytes]
+- `fire-fuel-light.md` — fire as the material system a culture is organized around — the hearth as an institution rather than a fixture (household unit, tax unit, cult center, the smoke it  …[+1051 bytes]
+- `funerary-material-culture.md` — how a culture disposes of its dead, and what that disposal does to everything else it makes — the master claim is that a mortuary system is four coupled m …[+2701 bytes]
 - `furniture-interior-lexicon.md` — furniture and the interior as a cultural system for fictional cultures — the gap this entry fills, since the partition owns buildings (`architecture-sett …[+2077 bytes]
-- `funerary-material-culture.md` — how a culture disposes of its dead, and what that disposal does to everything else it makes — the master claim is that a mortuary system is four coupled m …[+2701 bytes]
-- `fire-fuel-light.md` — fire as the material system a culture is organized around — the hearth as an institution rather than a fixture (household unit, tax unit, cult center, the smoke it  …[+1051 bytes]
 - `garment-lexicon-crosslinguistic.md` — how real languages name garments — the shirt/skirt/sheath "cutting" kinship and doublet slot-division; ethnic vs descriptive naming politics (qipao/ …[+241 bytes]
@@ -206,2 +215,3 @@
 - `textile-technology.md` — the material substrate of dress for a fictional culture — fiber hierarchy (linen/wool/silk/cotton/hemp) and the prep labor each demands; dye chemistry, fastness  …[+334 bytes]
+- `timekeeping-instruments.md` — the timekeeping instrument as a material-culture system for fictional cultures — the five instrument families that measure the day before and beside the clo …[+1540 bytes]
 - `trade-economy-lexicon.md` — market language as a worldbuilding system — why measures come from body parts, grain, and casks (and why standardizing them is always a sacred-political act:  …[+638 bytes]
@@ -210,3 +220,2 @@
 - `warrior-material-culture.md` — the fighting body as legible text — the five armor-construction systems (lamellar, laminar, scale, mail, rigid plate, plus hybrid brigandine forms) with re …[+1026 bytes]
-
 - `writing-media-surface-economy.md` — What a culture writes on, priced — the surface economy of inscription as a worldbuilding system: the seven surface families (clay and wax; stone and m …[+1667 bytes]
@@ -491,3 +500,3 @@
 
-Total knowledge entries: 211.
+Total knowledge entries: 212.
 
@@ -495,3 +504,3 @@
 `python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge`
-(total 211 files; directory totals 21/23/24/29/20/94).
+(total 212 files; directory totals 21/23/25/29/20/94).
 The inventory counts markers, not verified facts.
```

Long row lines are elided with `…[+N bytes]` markers in the display above; the byte-exact rows are in
E3/E4. Hunk line numbers are for the pre-state (524 lines) → post-state (533 lines).

### 4.2 Line-number map, pre → post

| surface | pre (rev 2.0) | post (rev 2.1) |
|---|---|---|
| `revision: 2.1 …` block | — | `:3` |
| `revision: 2.0 …` block | `:3` | `:12` |
| `## linguistics/ (21)` | `:136` | `:145` |
| `## myth-symbol/ (23)` | `:160` | `:169` |
| `## culture-material/ (25)` | `:186` (`(24)`) | `:195` |
| first culture-material row (`adornment-body-codes.md`) | `:188` | `:197` |
| `fire-fuel-light.md` row | `:200` | **`:207`** |
| `funerary-material-culture.md` row | `:199` | **`:208`** |
| `furniture-interior-lexicon.md` row | `:198` | **`:209`** |
| `textile-technology.md` row | `:206` | `:215` |
| `timekeeping-instruments.md` row (new) | — | **`:216`** |
| `trade-economy-lexicon.md` row | `:207` | `:217` |
| `writing-media-surface-economy.md` row | `:212` | `:221` |
| `## synthesis/ (29)` | `:213` | `:222` |
| `## verification/ (20)` | `:245` | `:254` |
| `## civilizations/ (94)` | `:268` | `:277` |
| `Total knowledge entries: 212.` | `:492` (`211.`) | `:501` |
| `Counts checked 2026-10-19 …` | `:494` | `:503` |
| counts footer vector line | `:496` | `:505` |
| `Superseded reading, …` paragraph | `:498-505` | `:507-514` |
| **total lines** | **524** | **533** |

Every pair in this table was measured by a `find-prefix` pass over both files, not computed by adding
a constant; the three re-sorted rows and the new row are the only lines whose position changes
relative to their neighbours.

### 4.3 What the delta does NOT touch

No row text is rewritten except the three re-sorted lines (moved verbatim) and the one new row. No
revision-2.0 note is deleted. The `Superseded reading, preserved as the dated record it was:`
paragraph (`:498-505`, post `:507-514`) and the three dated `Index rows re-measured …` paragraphs are untouched — the
file's append-only revision convention. This seat writes none of these bytes.

### 4.4 The acceptance reading, measured

**Method.** A scratch tree (`.scratch/c02/tree/knowledge/`) was built as a copy of the live
`corpus/knowledge` **plus** the §1 entry at `culture-material/timekeeping-instruments.md` (25
culture-material files, 212 total). The filed instrument `reports/round-28/readme/sweep.py` was
imported read-only and pointed at that tree (`sw.KNOWLEDGE = …`), then run over the candidate README
`.scratch/c02/readme-2.1.md`. Nothing was written inside `corpus/**` or `tools/**`.

| leg | reading | status |
|---|---|---|
| rows vs files | `rows 212 files 212` | pass |
| missing from index | `[]` | pass |
| ghost rows | `[]` | pass |
| topic mismatch | `0` (the new row is byte-equal to the entry's `- topic:`) | pass |
| duplicate rows | none in any section | pass |
| header drift | `{}` | pass |
| totals line | `212` `totals_ok True` | pass |
| counts footer | `footer_findings []` `footer_ok True` | pass |
| **overall** | **`ok True`, exit 0** | **pass** |

**Pre-landing control (the sweep has teeth).** The same candidate README against the **live** tree
(entry not staged) reads `rows 212 files 211`, `orphan_rows ['culture-material/timekeeping-instruments.md']`,
`header_drift {'culture-material': {'declared': 25, 'files': 24}}`, `totals_line 212 totals_ok False`,
`footer_findings` = `FOOTER_TOTAL` + `FOOTER_DIR_TOTALS`, **exit 1**. The delta is therefore red until
the entry lands and green after — the acceptance leg is not always-green.

**Order/contiguity/duplication leg, with its negative control.** An independent leg (not the sweep)
checks ASCII order, row contiguity, duplicate rows and header-vs-row-count per section:

- on the **filed** README → `OUT OF ORDER culture-material [('furniture-interior-lexicon.md',
  'fire-fuel-light.md'), ('fire-fuel-light.md', 'furniture-interior-lexicon.md')]` and
  `NON-CONTIGUOUS culture-material between lines 210 and 212` — **the control fires on the real
  defect**, so the leg is not vacuous;
- on the **candidate** rev 2.1 → `order/contiguity/dup/header: CLEAN`.

Both defects F1/F2 are therefore repaired **and** the repair is independently verified.

## 5. What this seat did NOT do

- **No in-tree execution of any round runner** (F-C13-1). The only filed code run was the read-only
  `reports/round-28/readme/sweep.py`, in live mode and as a read-only import against a scratch tree.
- **No `--freeze`** of `reports/round-34/handoff/declared-in-r7`, and no touch of any pinned byte.
- **No corpus or tool byte written.** The delta is a draft; the integrator applies it.
- **No scholarship verdict.** Nothing here judges whether the spare's historical anchors, etymologies
  or `(to-verify)` marks are correct; §2 reads structure and counts only.
- **No external source resolved** — this run has no network. Every historical claim in the spare
  remains exactly as it was filed.
- **The candidate README was not committed**, and no `git add`/`commit`/`push` was run.

## Owed

- **`corpus/README.md` rev 2.1** — integrator-applied from §4 (E1–E7). Not owed as a missing
  dependency: the bytes are drafted here in full and measured.
- **`corpus/knowledge/culture-material/timekeeping-instruments.md`** — the entry itself, staged from
  the §1 bytes (sha256 `9805c0b854334ed3…`). This seat does not land it; landing is the integrator's
  call under claim C's `after_required`.
- **A delta note on the spare's `- gap filled:` sweep** — `curfew` now matches 1 file
  (`fire-fuel-light.md`, a round-35 landing). Filing it as a new dated line in the landed entry (not
  an edit of the filed fragment `reports/round-35/cov/C04-timekeeping-spare.md`, whose bytes are
  pinned) is owed to whoever lands the entry. Path owed:
  `corpus/knowledge/culture-material/timekeeping-instruments.md` (`- gap filled:` / `- verified-at:`).
- **F1/F2/F3 tiering** — C01 files the stale currency as a defect (F4/S3); this seat reports it as a
  reading with a cause. One tier should be chosen; that is the parent's call, not this seat's.
- **`reports/round-36/cov/C03-verify.md`** — independent verification of this audit and the delta
  numbers, owed to C03.

## Citations

- `reports/round-36/targets.json` → `seats[id=C02]` (mission, out path) and `shared_rules`.
- `reports/round-36/claims.json:19-27` — claim C, its `before` / `after_required` / `thresholds` /
  `counting_commands`.
- `reports/round-35/cov/C04-timekeeping-spare.md:1-9` (filing header), `:9`/`:150` (fence), `:10-150`
  (the entry) — fragment sha256 `258fb166e35f3b0f92854dcb7c5e08fcfc285c51a42aa828cb79f3f761f5bcd2`,
  40 646 bytes; extracted entry 40 234 bytes, sha256 `9805c0b854334ed3…`.
- `corpus/README.md:1-2` (header), `:3` (rev 2.0 block), `:186` (`## culture-material/ (24)`),
  `:198-200` (the mis-ordered rows), `:211` (the stray blank), `:206-207` (the insertion anchor),
  `:492` (totals line), `:494-496` (counts footer), `:498-505` (superseded paragraph) — sha256
  `51b966af20483328c3e221d2ab0f766aa5cf0f5a0b140650b95eb841d6bea6f0`.
- `reports/round-28/readme/sweep.py:21` (`ROW_RE`), `:22` (`TOPIC_RE`), `:74-79` (`topic_of`), `:140`
  (topic equality), `:398-401` (continuation-join control) — instrument sha256
  `9b2ccac0046831fdaf48863ccd0ff6ca0fa390d044746c876e83a71c06f0cdd3`.
- `reports/round-35/cov/C11-readme-delta.md:37-38,159-161` — the ASCII-ascending rule F2 falsifies.
- `reports/round-35/review/R03-c-review.md` §1.3 — the stale-footer-date blind spot.
- `reports/round-35/cov/C13-audit-1-5.md` F12 — the pointer-leg undercount this seat's §2.2 confirms.
- `reports/round-36/cov/C01-audit.md` §0 rows 4–8, §3.6, findings F3–F5 — the first independent audit
  (read after this seat's own readings; agreements and divergences recorded in §2.5).
- `corpus/knowledge/culture-material/fire-fuel-light.md:3,20,27,75,82,112,131,153` — the only
  `curfew` matches at `ce103bf`; the file is a round-35 landing.
- Command outputs, 2026-10-19 at HEAD `ce103bf5885af00023cdc4a174c17602476cdcf8`
  (`git rev-parse HEAD`), from the lane root with
  `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`:
  - the 26-term sweep at `4a7aede` (`git grep -il -- "$kw" 4a7aede -- corpus/knowledge | wc -l`) →
    26/26 zero; at `ce103bf` → `curfew` 1, the other 25 zero.
  - `git grep -il -- clock 4a7aede -- corpus/knowledge/culture-material | wc -l` → **6**;
    the same at `ce103bf` → **10**.
  - `git grep -il -- bell 4a7aede -- corpus/knowledge | wc -l` → 81; at `ce103bf` → 87.
  - `git grep -ilw -- hour 4a7aede -- corpus/knowledge | wc -l` → 8; plain substring → 12;
    at `ce103bf` word-bounded → 11.
  - near-misses at `ce103bf`: astrolabe 2, `star clock` 2, chronometer 4, obelisk 1, meridian 1,
    `time zone` 1.
  - `python3 -B reports/round-28/readme/sweep.py` (live) → `rows 211 files 211`, all legs clean,
    exit 0.
  - the order leg on the filed README → `OUT OF ORDER` + `NON-CONTIGUOUS`; the same leg on the
    candidate → `CLEAN`.
  - the sweep against the scratch tree with the candidate README → `rows 212 files 212`, `ok True`;
    against the live tree → `ok False`, `orphan_rows 1`, `FOOTER_TOTAL`+`FOOTER_DIR_TOTALS`, exit 1.
  - candidate README sha256 `fc2e6d070cd7d123b4248e63b42b34a5fba9012c26e96a1918c622b5d2115316`,
    127 680 bytes, 533 lines.
  - the §2.2 pointer leg → `49 raw / 35 distinct / 30 after strip / 28 resolve`; unresolved
    `['corpus/knowledge/*/*.md', 'corpus/knowledge/...']`; `8` anchored tokens; `0` out of range.
- Scratch (disposable, gitignored): `.scratch/c02/entry.md`, `.scratch/c02/row.txt`,
  `.scratch/c02/readme-2.1.md`, `.scratch/c02/tree/knowledge/`, `.scratch/c02/pointers.json`,
  `.scratch/c02/pieces/`.
- **Corroboration (read after this fragment was drafted).** `reports/round-36/cov/C03-verify.md`
  §F1/§F2 independently reports the same two README defects — "the `culture-material/` rows are not
  in filename order" and "a stray blank line splits the `culture-material/` section" — with the same
  mechanism (neither index sweep carries a row-order or contiguity leg). Two seats, two instruments,
  same reading. C03's F1 also confirms the pre-landing blob was clean, matching this seat's §3
  provenance check.
