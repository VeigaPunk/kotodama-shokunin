# Round-66 entry spec — `scent-perfume-aromatics-codes.md` (claim C)

Status: pre-data design. Written by ScribeEntrySpec before any row exists. Every number below is
either quoted from `reports/round-66/accept-c.py` (the frozen counter) or measured in this seat
(temp tree, read-only over the lane). Nothing here asserts that a source or capture exists.

Non-shippable: this file is the skeleton. Every `SLOT` marker must be gone before the draft leaves
`.ufo/waves/round-66/stage/`. Gate: `grep -c SLOT <entry>` prints 0.

---

## 0. Frozen constraints (measured, not paraphrased)

`accept-c.py` at `reports/round-66/accept-c.py`, sha256 `0726b4bc99eefe05a81c92cb6fd1bb3819a041b68679466aa6278350c19dda86`
(counter self-sha, from `telemetry/dry-run-c.txt`). Constants: `ENTRY =
corpus/knowledge/culture-material/scent-perfume-aromatics-codes.md`, `NEW_IDS = S777..S800`,
`BASE = 94209e8f80969dbac48d56c5d0e2e623635b8616`.

| Leg | Exact code condition |
|---|---|
| FILE | file readable; `h1 == 1`, `h3 == 0`, `h2 <= 16`, `len(text.splitlines()) <= 250`, some line `.startswith("- topic:")` |
| SET | each of S777–S800 matches `^\|\s*(S\d+)\s*\|` exactly once in `corpus/SOURCES.md` |
| ROWS | `len(cells) == 11`; `c[2] in KINDS`; `c[3] in {"A","B"}`; `c[7] == "mined"`; `c[8] == "2026-10-24"`; `ENTRY in c[10]` |
| ONEID | `len(re.findall(r"\((S777)\)", text)) == 1` for every id, over the **whole file** |
| RESTATE | see §6 — 3 conditions per id, computed on the single bullet line |
| HOSTS | `>= 10` distinct lowercase netlocs among new rows' **first non-archive** URLs |
| LINK | `norm_url(first non-archive URL)` unique vs all 701 base rows and vs other new rows |
| APPEND | no base row line may change (`set` equality of rstripped row lines); additions only |
| NOHARM | `git diff --name-only BASE main -- corpus/knowledge` ⊆ {new entry, `games-play-sport-contests.md`} |
| SWEEP | `reports/round-28/readme/sweep.py` exit 0, `totals_ok True`, no `topic_mismatch` other than `0` |
| CAPTURE | per new row, `web\.archive\.org/web/\d{14}(id_\|if_\|im_)?/\S+` **or** the literal `no-capture`/`nocapture` (casefolded) inside `c[1]` |
| TOPIC | the entry's `- topic:` text (first such line, stripped) is a **substring of the first README line containing `scent-perfume-aromatics-codes.md`** |

---

## 1. Trap #1 — TOPIC is a *first-match* leg, not a "row exists" leg

`TOPIC` in the counter does:

```python
row = next((l for l in rtext.splitlines() if ENTRY.split("/")[-1] in l), "")
topic_ok = bool(tline) and tline[len("- topic:"):].strip() in row
```

The revision block sits above the index sections (`corpus/README.md` line 3 onward; index rows start
at line 308, `## culture-material/` at 373). If the new revision note names the entry **with** its
`.md` suffix, `next()` returns the revision line and the topic text is not in it → `TOPIC FAIL`,
while `SWEEP` still passes (the sweep never reads the revision block).

Measured on the existing round-65 entry as the control:

```
first line containing games filename -> culture-material entry landed (`games-play-sport-contests.md`, games, play,
TOPIC leg would be: False
after removing .md token from revision note, first match -> - `games-play-sport-contests.md` — games, play, sport and contests as material a
TOPIC leg would be: True
```

**Rule: the revision note must refer to the entry as `` `scent-perfume-aromatics-codes` `` — no `.md`.**
The index row and any later `## Known gaps` note (line 564+, i.e. after the index) may use the full
filename. This is the only place in README where the suffix must be dropped.

---

## 2. Entry skeleton (copy-ready; fill slots, do not renumber)

Head block — modelled on `games-play-sport-contests.md` lines 1–7. Four head lines, one H1, no H3.

```markdown
# Scent, perfume and aromatics — how a culture captures, compounds, and reads smell

- topic: scent, perfume and aromatics as a material-culture register — how a culture names and classifies smells, sources aromatic materials, extracts and compounds them, burns them as incense, wears them as unguents and oils, reads them as medicine, and moves them along trade routes — a sourced design reference for fictional scent practice, not a universal history of smell
- source: the round-66 registry rows in `corpus/SOURCES.md` are the evidence anchors; each inserted claim stays within its cited row.
- verified-at: 2026-10-24 — 24 cited claims inserted from the registry rows opened this round, one row per bullet; L1 preflight on the frozen counter passes; independent closure spot-check pending.
- recheck: 180 days, per row (`corpus/SOURCES.md` recheck cells).
```

- `- topic:` must be **one physical line**, no backticks, no `- ` at line start inside it. It is the
  exact string that must appear verbatim in the README row (§7) and it is what `sweep.topic_of()`
  compares for equality (continuations are space-joined, so a wrapped line would compare fine but
  `accept-c`'s `tline` would only take the first line — keep it single-line and both legs agree).
- `- verified-at:` may be rewritten by the executor only to state what was actually run; it never
  claims a closure review that did not happen.

H2 map — 13 sections (three spare under the `h2 <= 16` ceiling), zero H3, no tables outside §9:

```
## 1. What a smell term names: the olfactory register
## 2. Aromatic raw materials: resins, gums, barks and flowers
## 3. Animal fixatives: musk, civet, ambergris
## 4. Extraction: expression, maceration, distillation, solvent
## 5. Incense, fumigation and offering smoke
## 6. Oils, unguents and the perfumed body
## 7. Miasma, medicine and therapeutic smell
## 8. Provenance, trade and the price of aromatics
## 9. Design prompts
## 10. Cross-cultural patterns
## 11. Limits and evidence
## 12. Adjacent topics
## 13. Handoff to the world bible
```

That is 13 H2 (measured; three spare if a class needs splitting). Body sections 1–8 carry the
24 bullets, three per section. Sections 9–13 carry **no ids at all** (ONEID and RESTATE both count
every `(Snnn)` in the file).

Section pattern (games entry §2 is the model): one editorial paragraph of 2–3 sentences stating what
to compare and what not to conflate, then the bullets, one bullet per line, each ending ` (Snnn)`.

Body section text to use (edit only where a row forces it):

```markdown
## 1. What a smell term names: the olfactory register

Separate the three jobs a smell word can do: name a material ("frankincense"), name a sensation
("sweet", "burnt"), or name a practice ("incense"). A register that conflates them cannot say
whether a culture classifies smells by source, by effect, or by use.
- SLOT S777
- SLOT S778
- SLOT S779

## 2. Aromatic raw materials: resins, gums, barks and flowers

Name the material before the perfume: resin, wood, root, seed, flower, or the dried exudate of a
particular tree. Distribution is a claim about where the plant grows, not about where the perfume is
made.
- SLOT S780
- SLOT S781
- SLOT S782

## 3. Animal fixatives: musk, civet, ambergris

Animal fixatives carry a provenance problem: the animal, the region, and the trade that moved the
substance are three separate records. A scent that depends on one of them inherits its supply risk.
- SLOT S783
- SLOT S784
- SLOT S785

## 4. Extraction: expression, maceration, distillation, solvent

The technique fixes what the product is: an expressed oil, an infused fat, a distillate, or a
tincture. Equipment, fuel and labour are part of the evidence, not background.
- SLOT S786
- SLOT S787
- SLOT S788

## 5. Incense, fumigation and offering smoke

Keep the burned substance, the brazier or censer, and the occasion as three separate variables.
Smoke read as petition, as purification, and as medicine can be the same material in different
hands.
- SLOT S789
- SLOT S790
- SLOT S791

## 6. Oils, unguents and the perfumed body

Distinguish a scented oil applied to skin, a fat-based unguent, and a bath or laundry additive. Each
implies a different container, a different shelf life, and a different person who applies it.
- SLOT S792
- SLOT S793
- SLOT S794

## 7. Miasma, medicine and therapeutic smell

Therapeutic smell is a theory of causation before it is a recipe: bad air, corrupted matter, or an
offended power each imply a different remedy and a different practitioner.
- SLOT S795
- SLOT S796
- SLOT S797

## 8. Provenance, trade and the price of aromatics

Track the substance from habitat to market. Distance, monopoly, adulteration and substitution are
recurring features of the aromatics trade and each one is visible in a different kind of record.
- SLOT S798
- SLOT S799
- SLOT S800

## 9. Design prompts

Use the rows as conditional design prompts, not prescriptions. Select an option, combine
alternatives, or specify exceptions for a named setting.

| Worldbuilder choice | Possible consequence for scent scenes | Possible consequence for social structure |
|---|---|---|
| A smell is classified by its source | Show the plant, animal or mineral named in the scene's vocabulary. | Decide who may name, grow, or harvest the source. |
| A scent is classified by its effect | Give the sensation word and who is entitled to apply it. | Decide whether expertise in smell is an office or a trade. |
| A fixative must be imported | Show the sealed container, the merchant, and the substitute. | Decide what a supply interruption does to rank display. |
| Extraction requires fuel and labour | Show the still, the fire, and the hours someone watches it. | Decide whether the craft is guilded, household, or temple-bound. |
| Incense marks an occasion | Fix the censer, the route of the smoke, and who stands in it. | Decide who supplies, who officiates, and who is excluded. |
| A scent is worn on the body | Specify the carrier (oil, fat, powder) and its staying power. | Decide whether scent marks status, occupation, or availability. |
| Smell is medical evidence | State the theory of causation the practitioner holds. | Decide whether the healer, the priest, or the household reads the smell. |
| Aromatic goods travel far | Mark the route, the middlemen, and the adulterant. | Decide who profits, who certifies, and who is blamed for a fake. |

## 10. Cross-cultural patterns

These are cross-row readings of the bullets above, not new source claims; no citation is added here.

- WRITE 6–9 bullets, each a comparison across at least two rows; no citation ids in this section.

## 11. Limits and evidence

Evidence limits: no single source gives a universal history of smell. Recipes survive better than
practice, museum objects survive better than their contents, and a chemical identification of a
residue does not by itself name a use. This register samples particular regions and periods, so
absence here is not evidence that a scent practice is absent from a culture. Treat each bullet as
scoped to its cited source; the registry's source, scope and quote cells carry the evidence boundary.

## 12. Adjacent topics

This entry points to the following entries for adjacent scope. The pointing is one-way: they own
their topic, and this entry does not restate or extend them.

- `corpus/knowledge/culture-material/bathing-and-body-hygiene.md` owns the bath and hygiene
  institution; a scented oil applied after washing is cited here as scent evidence only.
- `corpus/knowledge/culture-material/cuisine-food-lexicon.md` owns food and spice as cuisine;
  aromatics are cited here as materials, not as flavour.
- `corpus/knowledge/culture-material/sumptuary-law-rank-display.md` owns legal rank display;
  a scent restriction is noted here as a constraint on supply, not modelled as law.
- `corpus/knowledge/culture-material/trade-economy-lexicon.md` owns exchange vocabulary; the
  movement of aromatics is noted here, not modelled.
- `corpus/knowledge/culture-material/funerary-material-culture.md` owns grave assemblage; a resin
  found in a tomb is cited here as scent material, not as mortuary practice.
- `corpus/knowledge/culture-material/ritual-garments.md` owns vesture; a perfumed garment is not
  described here.
- `corpus/knowledge/culture-material/material-culture-inference-method.md` owns the inference
  ladder from residue to practice; scent inference follows it rather than restating it.
- `corpus/knowledge/culture-material/music-instrument-lexicon.md` owns performance sound; the
  sensory staging of a rite is not scored here.

## 13. Handoff to the world bible

This entry supplies sourced anchors and conditional design questions; it makes no canon decision.
Lore-shokunin owns the world bible and its consistency verification under
`corpus/knowledge/synthesis/worldbible-integration-contract.md`; contested scope goes to the
integrator.

Decisions this entry deliberately does not make: whether a given culture's incense is sacred or
therapeutic, which scent is authoritative for a rank, and how a fictional perfume is compounded.
Those are canon choices for lore-shokunin, recorded and verified in the world bible, not here.
Drafts and contested readings route to the integrator.
```

Line budget, assembled from the skeleton above and counted: 137 lines with all 24 slots present
(measured on the assembled head + body texts). Well inside the 250 ceiling, with room for longer
bullets. Do not add H3s (`h3 == 0`); if a section needs sub-structure, use a bold lead-in on a bullet
instead.

---

## 3. Slot table — one row per id, grouped by scent class

Each slot fixes *what kind of evidence* the row must be, so the 24 rows do not collapse into one
source type. Host families are candidates to open and verify — none is asserted to exist or to
support a claim.

| Slot | Class / section | Evidence target | kind (suggested) | Host family (verify by opening) |
|---|---|---|---|---|
| S777 | §1 register | a scholarly or institutional account of how a language or culture sorts odours | paper / docs | university press, museum essay, journal |
| S778 | §1 register | a lexical or terminological treatment of smell words (a thesaurus, a standard vocabulary) | spec / book | standards body, lexicon project |
| S779 | §1 register | a sensory-history or anthropology argument that smell classification is learned | paper | journal, university repository |
| S780 | §2 materials | a resin or gum whose harvest and grade are documented (frankincense, myrrh, labdanum…) | docs / paper | botanical garden, museum, herbarium |
| S781 | §2 materials | a flower or wood material with a documented production region | docs / dataset | botanical database, trade body |
| S782 | §2 materials | a material-preparation record: cleaning, grading, or adulteration of a raw aromatic | paper / book | conservation institute, historical source |
| S783 | §3 fixatives | museum or conservation record for a musk-bearing object or the substance itself | docs | museum collection |
| S784 | §3 fixatives | ambergris: a natural-history or trade account, including its origin | paper / docs | natural history museum, archive |
| S785 | §3 fixatives | a welfare, legal or substitution record for an animal fixative | spec / docs | regulatory body, conservation NGO |
| S786 | §4 extraction | a distillation account with apparatus and product named | book / paper | digitized book, university repository |
| S787 | §4 extraction | maceration/enfleurage or solvent extraction described as a technique | docs / paper | museum, craft/history source |
| S788 | §4 extraction | an archaeological-chemistry residue study naming a compound and its context | paper | journal (PMC/PLOS/Elsevier) |
| S789 | §5 incense | a ritual-use record naming substance, censer and occasion | docs / paper | museum, heritage body |
| S790 | §5 incense | an inscribed or archival inventory listing incense by quantity | book / docs | digitized archive, museum |
| S791 | §5 incense | a heritage-inscription or living-practice record of incense/attar | docs | UNESCO ICH/WHC, national heritage |
| S792 | §6 body | a recipe collection with a scented oil or unguent formula | book / docs | manuscript library (Gallica, Wellcome) |
| S793 | §6 body | a cosmetic/unguent object record with contents analysed | docs / paper | museum, conservation science |
| S794 | §6 body | a hygiene, bath or laundry practice that consumes aromatics | book / paper | digitized book, journal |
| S795 | §7 medicine | a miasma or airs-and-places doctrine text | book / docs | medical library, digitized book |
| S796 | §7 medicine | a materia medica entry for an aromatic drug with indication | book / reference | digitized reference, botanical-medical DB |
| S797 | §7 medicine | an archaeological or experimental study of therapeutic burning/fumigation | paper | journal |
| S798 | §8 trade | a route or caravan/port record for aromatics | book / docs | archive, museum, historical geography |
| S799 | §8 trade | trade statistics or a market/price record for an aromatic commodity | dataset | statistics agency, FAO/UN, customs record |
| S800 | §8 trade | adulteration, substitution or monopoly in the aromatics trade | paper / docs | journal, regulatory/standards body |

Tier: A or B only (`community` is never A per `corpus/SOURCES.md`). Spread: aim ≥8 A and ≥8 B across
the 24; do not let one institution supply more than 3 rows.

Host plan — the `HOSTS` leg needs ≥10 distinct netlocs. Target 12–16 distinct hosts across the 24
rows, and check `LINK` before writing: no new normalized URL may equal any of the 701 base rows'
live URLs (host reuse is legal; identical host+path+query is not). Known heavy base hosts to differ
from by path: `metmuseum.org`, `vam.ac.uk`, `ich.unesco.org`, `collections.vam.ac.uk`,
`repository.si.edu`, `penn.museum`, `archive.org`.

---

## 4. Registry row shape (11 cells — one miscount fails ROWS)

Append point: `corpus/SOURCES.md` line 731 is `| S775 | …`, line 732 is blank, line 733 is
`## Paths`. New rows go between them, in id order: S776 (claim Ca's seat) first, then S777–S800.

```
| S777 | Author/Institution, "Title" - https://live.example/path ; https://web.archive.org/web/20261024HHMMSSid_/https://live.example/path . | paper | B | the scope this row may speak for | locator → "the verbatim quote, in double quotes" | what the source teaches, in the row author's words | mined | 2026-10-24 | 180d | corpus/knowledge/culture-material/scent-perfume-aromatics-codes.md |
```

Cell rules measured against the counter:

1. Exactly 11 cells — the table row must start `| ` and end ` |`; a `|` inside a cell splits it.
2. `c[1]` source: **live URL first**, then ` ; ` then the capture. `row_urls()` takes the first
   non-`web.archive.org` URL as the row's live URL; a capture-first cell leaves the row with no live
   URL and silently drops it from `HOSTS` and `LINK`.
3. `c[1]` capture: `https://web.archive.org/web/<14 digits>[id_|if_|im_]/<the same page>` — exactly 14
   digits immediately after `/web/`; `/web/2026/…` does not match. If no capture is possible, put the
   literal `no-capture: <reason>` in the **source cell** (the check is `"no-capture" in c[1].casefold()`;
   `no capture` with a space fails).
4. `c[4]` scope: the row's own limit, not the entry's.
5. `c[5]` anchor: `locator → "quote"`. `anchor_quote()` takes the **first** double-quoted (or
   curly-quoted) span in the cell, so put the real quote in straight double quotes and do not use
   double quotes in the locator prefix.
6. `c[6]` teaches: the full teaching, in the row author's words — this is the cell the RESTATE
   coverage leg measures against, so it should be *more* detailed than the bullet, not equal to it.
7. `c[7]` exactly `mined`; `c[8]` exactly `2026-10-24`; `c[10]` contains the entry path verbatim.
8. `c[9]` recheck: `180d` (entry head line says 180 days).

APPEND consequence, measured: the leg compares **sets of complete row lines**. Any in-place edit of an
existing row — including a `used-by` addition — makes that line "missing_old" and fails the leg. So the
24 rows are additions only, and the round-65 rows (S750–S775) must stay byte-identical.

---

## 5. `corpus/README.md` edit recipe (validated)

Five replacements, nothing else. Verified end-to-end in a throwaway tree by running
`sweep.sweep(modified_readme, root_override=tempknowledge)`: `ok True`, `total_files 240`,
`total_rows 240`, `topic_mismatch []`, `missing_from_index []`, `orphan_rows []`, `header_drift {}`,
`totals_line 240`, `totals_ok True`, `footer_findings []`, `footer_ok True`.

**R1 — new revision block above `revision: 2.17`, with the filename written without `.md`** (§1):

```
revision: 2.18 — Round-66 culture-material landing (2026-10-24): one
culture-material entry landed (`scent-perfume-aromatics-codes`, the scent, perfume
and aromatics register), its row added in filename order between `ritual-garments.md`
and `sumptuary-law-rank-display.md` with the entry's `- topic:` text verbatim;
`## culture-material/` moved 32 → **33**; the totals and footer moved 239 → **240**.
```

**R2 — section header**: `## culture-material/ (32)` → `## culture-material/ (33)`
(single occurrence, line 373).

**R3 — index row**, inserted between the `ritual-garments.md` row (line 398) and the
`sumptuary-law-rank-display.md` row (line 399), filename order, topic text byte-identical to the
entry's `- topic:` line:

```
- `scent-perfume-aromatics-codes.md` — <the entry's - topic: text, verbatim, one line>
```

`ROW_RE` requires the shape `` - `name.md` — text`` (backticks, U+2014, one space each side) — the
same em dash the neighbouring rows use.

**R4 — totals line** (line 693): `Total knowledge entries: 239.` → `Total knowledge entries: 240.`

**R5 — counts footer** (line 697), re-run its own command first and confirm 240:

```
`python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge`
(total 240 files; directory totals 30/29/33/29/24/95).
```

Footer arithmetic (live tree today): linguistics 30, myth-symbol 29, culture-material 32 → 33,
synthesis 29, verification 24, civilizations 95; total 239 → 240. `FOOTER_RE` is
`^Counts checked (\d{4}-\d{2}-\d{2}) from the repo root:\n` + the backticked command + `\n(total N
files; directory totals a/b/c/d/e/f).` — keep the date line, the command line and the totals line as
three consecutive lines with the command backticked and the totals sentence ending `).`.

Optional, not counter-checked, and **after** the index row: a one-line round note in `## Known gaps`
(line 564+), following the round-65 note at line 691. It may use the full filename because the index
row precedes it.

---

## 6. RESTATE — exact arithmetic, worked examples, pre-insertion check

For each id the counter takes the **one** line containing `(Snnn)`, and computes, with
`norm = NFKC → casefold → [\W_]+ → " "`:

```python
content_words(t) = [w for w in norm(t).split() if len(w) >= 4 and w not in STOPWORDS and w.isalpha()]
quote   = first quoted span in c[5]
inq     = sum(1 for w in content_words(quote) if w in content_words(bullet))     # >= 3
cov     = in_order_coverage(content_words(c[6]), content_words(bullet))           # < 0.8
novel   = [w for w in content_words(bullet) if w not in content_words(c[6])]      # >= 1
```

Three corrections to the shorthand in circulation — the frozen code, not the shorthand, decides:

- The quote leg is **membership, not order**: a bullet passes with ≥3 distinct quote content words in
  any order. (It counts *occurrences* in the quote list, so a quote repeating one word three times
  could reach 3 with fewer than three distinct words — do not rely on that; it is a loophole, not a
  target.)
- The teaches leg **is** in-order: `in_order_coverage` walks the teaches words through the bullet and
  returns hits/len(teaches). It must stay **below** 0.80 — pasting the teaches cell scores 1.00.
- `content_words` drops anything under 4 characters, any stopword, and anything containing a digit or
  punctuation (`"1200s".isalpha()` is False; `"s730".isalpha()` is False — the id itself contributes
  nothing). Words are compared **exactly**, so `resin` ≠ `resins`, `smoke` ≠ `smoking`.

Measured, using the counter's own functions on a synthetic row (frankincense/myrrh, teaches = a
two-clause sentence):

```
good : Frankincense, myrrh and other resins burned in temple braziers; a scene can price the resin and name who carries it. (S790)
       quote_words=6 teaches_cov=0.38 novel=5  -> PASS
paste: <the teaches sentence, verbatim> (S790)
       quote_words=6 teaches_cov=1.00 novel=0  -> FAIL (cov, novel)
short: Resin burns. (S790)
       quote_words=0 teaches_cov=0.00 novel=2  -> FAIL (quote)
```

Bullet recipe that satisfies all three without gaming them:

1. **Name the material and the object** using at least three of the quote's own ≥4-letter words —
   material names and proper nouns are usually the quote's longest words, so lift them, not the
   verbs.
2. **Add one consequence the teaches cell does not state** — a design consequence, a limit, or a
   contrast. This is the `novel` word and it is also what makes the bullet worth reading.
3. **Never reuse the teaches syntax.** Two clauses in the teaches' order is enough to cross 0.8.
4. One physical line per bullet, ending ` (S777)`. A wrapped bullet counts only its first line.
5. No `(Snnn)` anywhere else — not in section prose, not in §10, not in §12, not twice in one bullet.

Pre-insertion check (reuses the frozen functions, adds no second implementation):

```bash
python3 - <<'PY'
import importlib.util, re, sys
spec = importlib.util.spec_from_file_location("ac", "reports/round-66/accept-c.py")
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
ent = open("corpus/knowledge/culture-material/scent-perfume-aromatics-codes.md").read().splitlines()
reg = {re.match(r"^\|\s*(S\d+)\s*\|", l).group(1): l for l in open("corpus/SOURCES.md") if re.match(r"^\|\s*(S\d+)\s*\|", l)}
for sid in [f"S{n}" for n in range(777, 801)]:
    hits = [l for l in ent if f"({sid})" in l]
    if len(hits) != 1: print(sid, "bullets", len(hits)); continue
    c = m.cells(reg[sid]); q, t, b = m.anchor_quote(c[5]) or "", c[6], hits[0]
    bw, qw, tw = m.content_words(b), m.content_words(q), m.content_words(t)
    inq, cov = sum(1 for w in qw if w in bw), m.in_order_coverage(tw, bw)
    novel = [w for w in bw if w not in tw]
    bad = inq < 3 or cov >= 0.8 or not novel
    print(sid, "quote", inq, "cov", round(cov, 2), "novel", len(novel), "FAIL" if bad else "ok")
PY
```

---

## 7. Verification sequence (who runs what, when)

1. Draft leaves stage with `grep -c SLOT` = 0, 24 bullets, 13 H2, 0 H3, ≤250 lines.
2. Row draft passes §6's checker for all 24 ids, plus a manual `cells()` count of 11 for each row.
3. `python3 -B reports/round-28/readme/sweep.py` after the README edit → exit 0, `totals_ok True`,
   `topic_mismatch 0`, `footer_ok True`.
4. `python3 -B reports/round-66/accept-c.py --root .` after integration → all legs PASS. The dry-run
   at base (`telemetry/dry-run-c.txt`) is the pre-data control and already fails, as required:
   `FILE/SET/ONEID/RESTATE/HOSTS/CAPTURE/TOPIC FAIL`, `ROWS/LINK/APPEND/NOHARM/SWEEP PASS`.

## 8. Findings carried forward (for the L1 integrator, not action here)

1. **TOPIC first-match** (§1) — the README revision note must not contain `.md` for the new entry.
   Unfixed precedent: the round-65 block at README line 4 names `games-play-sport-contests.md`, so the
   same leg would fail if the games entry were the `ENTRY`; harmless for C because `ENTRY` is the scent file.
2. **APPEND is set-strict** — the leg's description speaks of "allowed status/used-by flips logged in
   the lesson", but the code tolerates none. Consequence: S753's `used-by` cell will keep naming the
   games entry after the claim-Ca re-point to S776; the counter cannot see the staleness and the file
   may not be corrected in place. Record the flip in `corpus/lessons/round-66.md` instead.
3. **CAPTURE has an escape hatch** — the literal `no-capture` passes the leg. It is a reason string,
   not evidence; the 24 rows should carry real captures wherever the page is reachable, and every
   escape should be justified in the row's scope cell. Review-only, but the counter will not catch an
   over-used escape.
4. **HOSTS counts netlocs only** — 24 rows from 10 hosts satisfy the leg even if one institution
   supplies 8 of them. §3's ≤3-rows-per-institution rule is a review-time constraint, not a leg.
5. **LINK normalizes away the fragment and the trailing slash** — two rows differing only by `#anchor`
   or a trailing `/` collide. Compare `norm_url` results before writing, not the raw strings.
