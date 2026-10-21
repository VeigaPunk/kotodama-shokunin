# SrcUnescoGer — frontier source for claim C: UNESCO ICH Mongol Ger (element 00872)

Seat: ChousaR27R2.SrcUnescoGer-4, source seat, 2026-10-21. Assigned: open the UNESCO ICH
element page for *Traditional craftsmanship of the Mongol Ger and its associated customs*
(2013), quote the located description of mobile dwelling and herding life, return a SOURCES
candidate (URL, access date, kind, tier + reason, scope, <=25-word verbatim quote with
location, what it teaches the entry, recheck cadence). Author-lane advice, never admission.

## Result

**Candidate row: S048** (next free id; `grep -rn 'S048' corpus tools reports` → no hits,
2026-10-21). Row below is paste-ready in `corpus/SOURCES.md` registry format; `status: mined`
and `used-by` are correct only once claim C's entry text actually cites it — otherwise file
`queued` with empty `used-by`.

| S048 | UNESCO ICH, Traditional craftsmanship of the Mongol Ger and its associated customs (element 00872), Mongolia — https://ich.unesco.org/en/RL/traditional-craftsmanship-of-the-mongol-ger-and-its-associated-customs-00872 | docs | A | the element's inscription record and UNESCO's own description of the ger as a portable nomadic dwelling and household craft — not pastoral ecology, herd management or transhumance | element page, description paragraph following the line "Inscribed in 2013 (8.COM) on the Representative List"; live page bot-checked on 2026-10-21, text read in Wayback captures 20241219152138 and 20260103060250 of the exact URL | a walls-and-poles round structure, canvas-and-felt covered and rope-tightened, light enough for nomads to carry and foldable for dismantling; sheep's-wool felt, animal-hair rope and hand-sewn felt carpets are household-communal products, craft taught by senior mentoring — cite as one official worked case of a mobile dwelling, never as comparative evidence about herding | mined | 2026-10-21 | 365d | corpus/knowledge/culture-material/pastoralism-animal-husbandry.md |

### Quote (22 words, verbatim, both captures)

> It is light enough for nomads to carry; flexible enough to fold and pack; and sturdy enough to be dismantled and reassembled.

Location: element page, **Description paragraph, third sentence** (the paragraph that opens
"Craftsmanship of the Mongol Ger is a traditional enterprise involving the labour of a
household or group…", immediately after the inscription line "Inscribed in 2013 (8.COM) on
the Representative List of the Intangible Cultural Heritage of Humanity").

### Access route and why the row says so

- Live `https://ich.unesco.org/en/RL/traditional-craftsmanship-of-the-mongol-ger-and-its-associated-customs-00872`
  returned the site's CAPTCHA interstitial ("This question is for testing whether you are a
  human visitor…", support ID 5619449045260540837) on 2026-10-21. The short form
  `https://ich.unesco.org/en/RL/00872` returned the same interstitial (support ID
  5619449045255127460). No live text was obtained.
- `https://web.archive.org/web/20241219152138/https://ich.unesco.org/en/RL/traditional-craftsmanship-of-the-mongol-ger-and-its-associated-customs-00872`
  opened in full; description text read and quoted.
- `https://web.archive.org/web/20260103060250/https://ich.unesco.org/en/RL/traditional-craftsmanship-of-the-mongol-ger-and-its-associated-customs-00872`
  opened in full 13 months later; the description paragraph is **byte-identical** in the two
  captures, which controls for capture corruption. Both captures carry 111 total captures for
  the URL (2017-05-10 → 2026-10-10).
- Remaining unknown: whether the live page differs today. Nothing suggests it; the element
  was inscribed in 2013 and both captures agree.

### Tier reasoning (QUALITY criterion 6)

Tier **A scoped to** "the element's inscription record and UNESCO's own description". The
publisher is the Convention secretariat, and the page is the authoritative record of its own
inscription (2013, 8.COM, Representative List) and of its own description text. This is not
the round-49 publisher-blurb pattern (S034/S038/S039 → S044–S046): those rows described a
third-party work through a publisher abstract; here the scope *is* UNESCO's own record, for
which UNESCO is primary. The narrow scope does the calibration work: the row is **not**
authority for pastoral ecology, herd composition, grazing, or transhumance — those claims
need specialist rows or `(to-verify)`. If a reviewer reads the scope as substantive
ethnography of Mongolian pastoralism, the criterion-6 fix is a superseding tier-B row, never
an in-place tier edit.

### What it teaches claim C's entry, by section

1. **Mobile dwelling / camp section.** The ger is the official worked case that a pastoral
   dwelling is designed by move frequency: light enough to carry, foldable, dismantle-and-
   reassemble. Feeds a decision-table row "dwelling form vs. moves per year" — portability as
   a derived requirement of the round, not a stylistic choice.
2. **Herd products → household processing.** Located on the same page (not part of the row's
   single anchor quote): covers "made of white felt and canvas, ropes of animal hair, flooring
   and carpets of hand-sewn felt"; "Cutting and preparing sheep's wool, making felt, stitching
   canvas and preparing woodwork are usually communal endeavours." This is the herd-output-to-
   craft link the entry needs (wool → felt; hair → rope), with labour organized by household
   or group and a stated gendered division ("men carving the wood and both women and men
   engaged in painting, sewing and stitching, and felt-making").
3. **Transmission / labour reproduction.** "Traditional craftsmanship is taught to the younger
   generations, principally through mentoring by a senior craftsperson"; dismantling and
   reassembly are "always family operations". Feeds the entry's apprenticeship/mentoring row
   for pastoral households.
4. **Boundary confirmation (page metadata, not evidence about the world).** The page's own
   concept tags include "Nomads" (44) and "Mobile homes" (2), and its biome tag is
   "Grasslands, savannahs" (93). Useful to show the register is externally catalogued on the
   mobile-herding axis; the numerals are UNESCO list tallies, never frequency evidence.

**Cannot support (mark `(to-verify)` or cite elsewhere if used):** herd composition, species
mix, herd size, grazing rotation, pasture tenure, transhumance distance or seasonality,
livestock wealth/bridewealth, dairy/meat economy. The page mentions animals only as materials
(sheep's wool, animal hair, a "Leather" concept tag); it contains no herd-management content.
It is also one State-Party-supplied element summary, not comparative ethnography.

### Boundary inputs observed this session (for the entry's one-owner table)

- `corpus/knowledge/civilizations/mongol.md:40` — mobile pastoralism coexists with urban
  production and documentary administration (anti-ladder caveat); `:131` — "Fur, wool/felt,
  silk | Different production chains and unequal access". Cite both; do not restate the
  Mongol file's script/Heaven/authority/deel/yam ownership.
- `corpus/knowledge/culture-material/agrarian-field-system-lexicon.md:62` — the agropastoral
  row already owns "fields + pasture + transhumance routes"; mixed systems stay there.
- `corpus/knowledge/culture-material/fire-fuel-light.md:37` — dried dung as fuel and the
  manure trade-off; the entry cites it, does not re-own fuel.
- `corpus/knowledge/linguistics/semantic-fields-lexicon-building.md:70` — pastoral wealth
  vocabulary (herd-age/colour/condition) indexes property systems; `:105` — "steppe pastoral"
  culture-type bundle. The entry owns production facts, the field owns the lexicon.
- Census observed 2026-10-21 in the lane worktree: `find corpus/knowledge -name '*.md' | wc -l`
  → 225; `ls corpus/knowledge/culture-material/*.md | wc -l` → 27; pastoral/herd/husbandry
  filename sweep → 0. Consistent with `reports/round-50/claims.json` before-state (225/27).

### Confidence and unresolved

- Quote text and location: **high** (two independent captures, verbatim agreement).
- S048 free + 0 pastoral filenames: **high** (direct probes this session).
- Boundary anchors: **high** (lines read this session).
- Tier call: **medium-high** — scope-dependent; argument stated above so L1 can overrule
  with a superseding row rather than an edit.
- Not opened: the 2013 nomination file and decision 8.COM/8.a (would strengthen inscription
  facts; a lead, not needed for this row); the live page beyond the two bot-checked fetches.

### Unrun checks

Lane validators (`reports/round-28/readme/sweep.py`, `reports/round-49/run-validation.py`)
were not run — source seat, no production edits. No tools installed. No files outside this
report were written.
