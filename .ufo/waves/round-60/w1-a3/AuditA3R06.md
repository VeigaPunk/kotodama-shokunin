NONE-MET
(w1-a3 wording audit, ids S618/S619/S620 only. No counter fixture was run through my hands and no fixture reached `ACCEPT-D-60: PASS` via me; this report is pre-freeze entry wording evidence, not a control receipt. No tools installed. Sandbox: /fast/scratch/hyaku/kotodama-r60a3/AuditA3R06/. Lane untouched; lane bytes touched only by read/grep and a read-only import of reports/round-60/reopen-quote.py with PYTHONDONTWRITEBYTECODE=1.)

# AuditA3R06 — pre-data-freeze wording audit: S618, S619, S620

Method: for each id, grep of /fast/scratch/hyaku/kotodama-r60a3/L1/candidate-entry.md (all citing lines) and of the lane SOURCES.md row; live re-open of the row's first URL by plain curl (no browser, no challenge bypass; final URLs recorded); the row quote located in the fetched bytes with the lane's own locator `reports/round-60/reopen-quote.py` (`locate_in` incl. its OCR de-hyphenation pass); teaches-cell and every entry-line clause checked against the page text. No line citing my ids cites a second id (all five citing lines are single-id), so the two-id rule never engaged. No S648-S651 rows fall in my scope, so the round-59 mapping check is n/a for me.

Fetch evidence (live, HTTP 200, byte counts exactly equal to the sizes pinned in the rows — no drift detected):

| id | URL | status | bytes | final URL |
|---|---|---|---|---|
| S618 | https://www.cam.ac.uk/research/news/medieval-birthing-girdle-parchment-was-worn-during-labour-study-suggests | 200 | 142,514 (pinned 142,514) | same URL |
| S619 | https://archive.org/download/anglosaxoncharms00gren/anglosaxoncharms00gren_djvu.txt | 200 | 394,072 (pinned 394,072) | https://dn790001.ca.archive.org/0/items/anglosaxoncharms00gren/anglosaxoncharms00gren_djvu.txt (archive.org's own download node for the same item) |
| S620 | https://www.agecrofthall.org/single-post/apotropaic-mark | 200 | 160,412 (pinned 160,412) | same URL |

Locator results on the fetched bytes: S618 located=True, S619 located=True, S620 located=True.

## AUDIT S618 OK
- Row: S618, docs, tier B, quote locates. Entry lines citing it: candidate-entry.md 119, 129, 138.
- Quote is body prose: hits once, inside a body `<p>` (raw tag-before = p-tag), the paragraph beginning "Made from materials such as silk, paper and parchment". Not heading, caption, nav, cookie or promo.
- Page sentence carrying every clause: "Made from materials such as silk, paper and parchment, and inscribed with prayers and invocations for safe delivery, birthing girdles were one of the most common spiritual charms loaned out by monasteries to their parishioners."
  - L119 "birthing girdles inscribed with prayers and invocations for safe delivery were among the most common spiritual charms loaned out by monasteries to parishioners": "prayers and invocations for safe delivery" verbatim; "one of the most common spiritual charms" (page) carries "among the most common"; "loaned out by monasteries to their parishioners" verbatim (entry drops only "their"). Carried.
  - L129 "monasteries loaned out birthing girdles inscribed with prayers for safe delivery to their parishioners": strictly narrower than the page clause (drops "and invocations"); carried.
  - L138 "birthing girdles were among the spiritual charms monasteries loaned out to their parishioners": narrower still; carried.
- Teaches cell carried: made — "Made from materials such as silk, paper and parchment"; lent out — the loan sentence above; suppressed as a class of protective text — "Talismanic items such as girdles, designed to secure assistance from divine and supernatural forces, were targeted for destruction during the Dissolution of the Monasteries, which began in 1536 under King Henry VIII." plus "Despite a ban on girdles by bishops in the wake of the Reformation, women were known to have used them surreptitiously up until the early 17th century"; English — "offered to anxious pregnant women by the Pre-Reformation English Church". The class-level claims are the study's own statements about the class, not a universal drawn from the single Wellcome scroll.
- No rewrite. Note (not a defect): the word "suppress" itself is absent; the teaches verb is carried by "targeted for destruction" + "a ban on girdles by bishops".

## AUDIT S619 OK
- Row: S619, book, tier B, quote locates. Entry line citing it: candidate-entry.md 114 only.
- Quote is body prose in section D (Amulet Charms) of the OCR text: "In five of the printed D charms, the amulet consists of a writing con- taining mysterious words, letters, and other symbols." — OCR line-break hyphen "con- taining", which `locate_in` de-hyphenates (located=True). Row locator "section D (Amulet Charms), second paragraph, p. 135 of the scan" matches the OCR flow (page marker "135" adjacent). Not a heading, caption or nav.
- Entry line 114: `- Writing as the amulet: in five of the printed Anglo-Saxon D charms the amulet consists of a writing of mysterious words, letters and other symbols (S619). **B**`
  - "five of the printed D charms": verbatim. The added "Anglo-Saxon" is carried by the page: "Anglo-Saxon charms may be divided into five groups, as follows : — A. ... D. Amulet charms. E. Charm remedies." and "D. Amulet Charms. — The fourth group of charms...".
  - "the amulet consists of a writing of mysterious words, letters and other symbols": page says "a writing containing mysterious words, letters, and other symbols" — carried ("of" narrows "containing"; no over-reach). The page itself quantifies over five charms, so no universal-from-one-object.
- Teaches cell carried: writing — the quote (material named: "parchment and wax are respectively named" in D 10 / DD 14); herb — "These plants are all recommended as amulets: lupine and garlic in D i, lupine also in DD 2 ... clover, which hung around the neck, insures the wearer against dimness of eyesight"; stone — "Like herbs, stones were held in great veneration ... and were employed as periapts. They are so used in charms D 4, D 5, and D 11."; where each was placed — "clover, which hung around the neck", "D 11 recommends the farmer to place a meal-stone in the middle of a field", "carried about by the sick man".
- No rewrite.

## AUDIT S620 OK
- Row: S620, docs, tier B, quote locates. Entry line citing it: candidate-entry.md 101 only.
- Quote is body prose: verbatim inside a body `<p>` (raw tag-before = p-tag): "Frequently small, faint, and hard to see, apotropaic marks are usually found where there is an opening through which evil could easily enter—doors, windows, and fireplaces." Between the Daemonologie paragraph and "A mantle, whether stone or wood...". Not heading, caption, nav, cookie or promo.
- Entry line 101: `- Openings of the building: apotropaic marks are usually found where there is an opening through which evil could easily enter, at doors, windows and fireplaces (S620). **B**` — identical clause set (entry renders the em dash as ", at" and drops the serial comma; no claim change, "usually" kept). Carried.
- Teaches cell carried: a museum's own reading of one house's mark — "Dr. Ian Tyers, a dedrochronologist from England, was here in 2016 ... located in our Great Parlor ... you will see a lightly inscribed daisy wheel (above), an apotropaic mark."; why such marks gather at openings — the quote sentence plus "Fireplaces were a known weak spot in home defense because 'it was thought that...the chimney, open to the sky, was vulnerable—particularly for incursions of evil.'"; the general placement statement is the museum's synthesis of the secondary literature it cites, not fieldwork — the post carries a five-item reference list ([1] Binding & Wilson, "Ritual Protection Marks in Wookey Hole and Long Hole, Somerset," 2010; [2][3] Reeve, "Here be witchcraft," Lassco; [4] Kennedy, The Guardian, 4 Nov 2014; [5] "Guarding the Lintels," winslowhouse.org) and footnotes its general statements to them, while the one-house mark is its own observation.
- No rewrite. Notes (not defects): page spells "Great Parlor" (the SOURCES row's bibliographic parenthetical says "Great Parlour"); page typo "dedrochronologist"; page shows "Oct 13" with no year, matching the row's "undated". None of these enters quote, teaches or entry line.

## Residual risk
- All verdicts rest on live bytes fetched 2026-10-23; I did not diff against the rows' listed Wayback captures. Byte-count equality with the pinned sizes makes undetected drift unlikely but is not proof; a support seat fetching later could meet a changed page (the rows' Wayback captures remain the fallback and a page unreachable by both is a NOT-SUPPORTED under FETCH-60).
- S619's verbatim verdict passes through the locator's de-hyphenation of OCR line breaks; a support seat that demands literal contiguous (non-normalised) matching would not find the quote verbatim — the lane instrument's `locate_in` is the frozen arbiter and it locates.
- Entry/row freeze, sha256 and the 47-id blind re-judgement belong to later seats and are outside this audit.

## Verification gaps
- None actionable in scope: every entry clause and teaches cell for my three ids is carried by the live page, quotes locate mechanically, no quoting-of-heading/caption/nav/cookie/promo case found, and no id of mine shares a line with another id.
