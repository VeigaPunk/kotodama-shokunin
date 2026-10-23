# ReviewKongoB58 — round-58 re-check of carried kongo-kingdom.md sentence fixes

Seat: `KotodamaR58A2.ReviewKongoB58` (leaf reviewer; no subagents, no lane writes beyond this report).
Scope: `corpus/lessons/round-57-verifier-spotcheck.md` §5 item 6 — the carried (second round)
kongo-kingdom.md sentence fixes drafted in `.ufo/waves/round-57/build/ReviewCarried*.md`.
My lines (round-57 numbering): **93, 97, 110, 140, 141, 146**.

Method: `git diff 89b94b69 -- corpus/knowledge/civilizations/kongo-kingdom.md` is **empty** — the
worktree entry is byte-identical to the round-57 tip, so round-57 line numbers still apply.
Each finding was re-checked against the served text by ordinary means (plain `curl` GET, browser
UA only; every byte count matched its row's recorded size). Quotes were located with
`python3 -B reports/round-58/reopen-quote.py '<url>' '<quote>'` (output pasted below).
`xd://lsp` is not mounted ("Mounted devices: ast_edit, debug"), so all judgments rest on the
opened served text — recorded here as the text-grep fallback, not semantic LSP proof.

## Sources re-opened this session

- S384 `https://www.redalyc.org/jatsRepo/273/27353124003/27353124003.pdf` — HTTP 200, application/pdf,
  1,291,427 bytes (= row). Printed p. 12 = PDF leaf 3 (leaf footer "12"; article pp. 11–31).
- S385 `https://web.archive.org/web/20240327164523id_/https://journals.openedition.org/assr/pdf/2480`
  — HTTP 200, application/pdf, 303,987 bytes (= row note; the live OpenEdition URL was not retried
  since the row itself records the Anubis challenge). Printed p. 76 = PDF leaf 19 (footer "76").
- S397 `https://openaccess-api.clevelandart.org/api/artworks/159880` — HTTP 200, JSON, 8,764 bytes (= row).
- S359 `https://archive.org/download/monumentamissionariaafricana/MonumentaMission%C3%A1riaAfricana-01.001_djvu.txt`
  — HTTP 200, text/plain, 896,693 bytes (= row); leaf-level verification via
  `…-01.001_djvu.xml` (HTTP 200, 8,938,662 bytes, 641 PAGE objects) and footers.
- S383 `https://web.archive.org/web/20260203111247/https://www.cambridge.org/core/journals/journal-of-african-history/article/abs/development-of-an-african-catholic-church-in-the-kingdom-of-kongo-149117501/2FB5AD22282AF36704DE49E593623693`
  — HTTP 200, text/html, 1,158,760 bytes (~ the row's 1,158,762; capture re-templated 2 bytes differently).

## Registry context checked

`corpus/SOURCES.md` rows S481–S491 (round-57 records rows) are **filed**: S481 supersedes S359
(anchors now `doc. 142, p. 470` / `doc. 147, p. 490`), S483 supersedes S383, S484 supersedes S385
(anchors carry the curly-apostrophe p. 76 quote; **they do not carry the p. 61 note 5 or p. 63
note 8 quotes**). All are `status queued`, `opened 2026-10-22`, `recheck 365d`, `used-by —`.
Rows for S384 and S397 are unchanged (no superseding row).

## Verdicts and exact fixes (current line numbers; agree = on the served text)

### Line 93 — S385 "centre of palero practice" over-read — **AGREE with the finding**

Served (printed p. 76, verbatim, typographic apostrophes): `Les minkisi, qui ne représentaient
qu’une partie des objets rituels en pays kongo, sont devenus le centre de l’attention des paleros.`
and `Tous les rituels en rapport avec la fonction royale ont disparu.` — "attention", not "practice".
The rest of the sentence is carried by the same page: `Alors que le terme nganga désigne un
guérisseur traditionnel en Afrique, il désigne à Cuba le récipient où est « fixé » un esprit`
(printed p. 61, note 5 — leaf 4, footer "61") and `les ethnonymes utilisés dépendaient plus des
factoreries sur la côte africaine` (printed p. 59, leaf 2, footer "59").

- old: `In Cuba the minkisi became the centre of palero practice while every rite tied to the royal function disappeared (S385, p. 76)`
- new: `In Cuba the minkisi became the centre of the paleros' attention while every rite tied to the royal function disappeared (S385, p. 76)`

Keep the S385 id here: the p. 61 note 5 anchor exists only on the S385 row (S484's filed anchor
drops it), and the supersession convention keeps the superseded row cited.

### Line 97 — two clause fixes on one line — **AGREE with both findings**

(a) S384 "A Christian noble wore…" over-read. Served p. 12 describes the single "richly attired
leader" in Bernardino d'Asti's ca. 1740 watercolor (Figure 1): `He wears an mpu cap on the head,
an nkutu net over the shoulders. He carries a wooden staff in his left hand… a brilliant red coat
embroidered with the insignia of the Order of Christ hangs behind his back.` Recommended
verbatim-faithful fix (the page says the coat "hangs behind his back", not that he "wears" it):

- old: `A Christian noble wore an mpu, an nkutu net over the shoulders, a staff and a red coat with the order's insignia (S384, p. 12).`
- new: `In the watercolor, the richly attired leader wears an mpu cap and an nkutu net over his shoulders, carries a wooden staff, and a brilliant red coat embroidered with the Order of Christ insignia hangs behind his back (S384, p. 12).`
- (weaker alternative, the round-57 draft's own wording — also supported since the coat is part of his attire: `…and wears a red coat embroidered with the Order of Christ insignia (S384, p. 12).`)

(b) S397 date range narrowed. Served API fields: `creation_date: late 1800s–early 1900s`;
culture `Kongo-style maker, possibly Yombe subgroup`; Description carries `Zimpu (singular: mpu)`,
`this long cap (mpu ngola)`, `Known since at least 1607 in the former Loango Kingdom, as well as
the adjacent Kongo Kingdom`. Apply the original finding's minimal exact correction:

- old: `a late-1800s cap`
- new: `a late-1800s–early-1900s cap`

(optional strengthening, all served: `by a maker possibly Yombe` → `by a Kongo-style maker,
possibly Yombe subgroup`; the finding flagged only the date.)

### Line 110 — S359 doc-147 locator — **AGREE with the finding**

doc. 147 "CARTA DO REI DO CONGO A D. JOÃO III (18-10-1526)" opens on leaf 549. Both anchors
(`se sam catiuos, se forros`; `e as poderam leuar e embarquar`) sit on leaf 551, whose footer is
`49°` = printed p. 490 (neighbours: leaf 550 footer garbled, leaf 552 `49 1`, leaf 553 `49 -`,
leaf 548 `4 S 7`=487). p. 489 is the preceding page.

- old: `| 1506–1543 | Afonso I; letters of 1526 police who may be enslaved and exported, not abolition | S359 (doc. 147, p. 489) |`
- new: `| 1506–1543 | Afonso I; letters of 1526 police who may be enslaved and exported, not abolition | S359 (doc. 147, p. 490) |`
- id-swap variant: `S359` → `S481` here and in the other two locator fixes is cleaner — p. 470/490 exist only as S481 anchors — but keeping S359 matches both prior reviewers' drafts and the
  "superseded row stays cited, superseding row goes `mined` with the same used-by" convention.
  Decide once, apply across my lines and the sibling slices' (18, 65, 82, 84, 85, 89).

### Line 140 — S359 doc-142/147 locators — **AGREE with the finding**

doc. 142 "CARTA DO REI DO CONGO A D. JOÃO III (6-7-1526)" opens on leaf 529 (printed p. 469 on
leaf 530 footer `4 *9`). Both anchors and the will clause ("nossa vontade hé que nestes Reynos
nam aja [trato de esprauos…]", continuing onto leaf 532) sit on leaf 531, footer `* 7 °` = printed
p. 470 (sequence 467/469/470/`47-`=471/`473`).

- old: `His July 1526 letter states the wish that his kingdoms have no slave trade (S359, doc. 142, p. 469), but his October 1526 letter sends each sale to three court officials who judge captive or free and lets cleared captives be shipped (S359, doc. 147, p. 489)`
- new: `His July 1526 letter states the wish that his kingdoms have no slave trade (S359, doc. 142, p. 470), but his October 1526 letter sends each sale to three court officials who judge captive or free and lets cleared captives be shipped (S359, doc. 147, p. 490)`

### Line 141 — S383 "an African church accepted" over-read — **AGREE with the finding (partial agreement with the drafted replacement)**

Served Extract para. 1 (verbatim): `Scholarly opinion on the conversion of the Kingdom of Kongo
to Christianity has generally been that it was superficial, diplomatically oriented, impure,
dangerous to national sovereignty or rejected by the mass of the population. This article argues
that although Christianity in Kongo took a distinctly African form it was widely accepted both
in Kongo and in Europe as being the religion of the country.` So (i) the over-read stands —
"an African church" is not on the page; (ii) the round-57 draft's fuller replacement is itself
imprecise on two counts: its locator `paras. 1–2` is wrong (all cited content sits in para. 1 —
anchor 1 is para. 1, and the "scholarly opinion" sentence precedes it in the served Extract), and
`accepted as the country's religion` drops the page's hedged `as being` + `widely` + the Kongo-and-Europe scope. Recommended:

- old: `UNESCO says the kingdom adopted Christianity while retaining Kongo custom (S411, Criterion (iii), sentence 3); Thornton argues an African church accepted as the country's religion (S383, Extract, para. 1).`
- new: `UNESCO says the kingdom adopted Christianity while retaining Kongo custom (S411, Criterion (iii), sentence 3); Thornton names the older scholarly opinion that the conversion was 'superficial, diplomatically oriented, impure' and argues instead that Christianity in Kongo took a distinctly African form, widely accepted in Kongo and Europe as being the religion of the country (S383, Extract, para. 1).`
- minimal alternative (if the bullet should stay short): `…; Thornton argues that Christianity in Kongo took a distinctly African form, widely accepted in Kongo and Europe as being the religion of the country (S383, Extract, para. 1).`

The fuller new restores the older-opinion sentence the calibration bullet is supposed to weigh;
single quotes are used for the internal quote since the bullet already carries doubles.

### Line 146 — S359 doc-142 locator — **AGREE with the finding**

- old: `(S374, title page; S359, doc. 142, p. 469)`
- new: `(S374, title page; S359, doc. 142, p. 470)`

## Locator lines (pasted runs, `python3 -B reports/round-58/reopen-quote.py`)

```
$ … 'https://www.redalyc.org/jatsRepo/273/27353124003/27353124003.pdf' 'He wears an mpu cap on the head, an nkutu net over the shoulders'
LOCATED https://www.redalyc.org/jatsRepo/273/27353124003/27353124003.pdf
$ … 'https://www.redalyc.org/jatsRepo/273/27353124003/27353124003.pdf' 'a brilliant red coat embroidered with the insignia of the Order of Christ hangs behind his back'
LOCATED https://www.redalyc.org/jatsRepo/273/27353124003/27353124003.pdf
$ … 'https://web.archive.org/web/20240327164523id_/https://journals.openedition.org/assr/pdf/2480' 'Les minkisi, qui ne représentaient qu’une partie des objets rituels en pays kongo, sont devenus le centre de l’attention des paleros'
LOCATED https://web.archive.org/web/20240327164523id_/https://journals.openedition.org/assr/pdf/2480   (first attempt: NOT_LOCATED HTTPError — transient Wayback throttle; retry located)
$ … 'https://web.archive.org/web/20240327164523id_/https://journals.openedition.org/assr/pdf/2480' 'Tous les rituels en rapport avec la fonction royale ont disparu'
LOCATED https://web.archive.org/web/20240327164523id_/https://journals.openedition.org/assr/pdf/2480   (same transient-then-retry)
$ … 'https://archive.org/download/monumentamissionariaafricana/MonumentaMission%C3%A1riaAfricana-01.001_djvu.txt' 'os ditos mercadores leuam cada dia nossos naturaes, filhos da terra e filhos de nossos fidallgos e vassallos'
LOCATED https://archive.org/download/monumentamissionariaafricana/MonumentaMission%C3%A1riaAfricana-01.001_djvu.txt
$ … 'https://archive.org/download/monumentamissionariaafricana/MonumentaMission%C3%A1riaAfricana-01.001_djvu.txt' 'se sam catiuos, se forros e semdo per elles despachados ao diate nam terá nenhuüa duuyda nem embargo e as poderam leuar e embarquar'
LOCATED https://archive.org/download/monumentamissionariaafricana/MonumentaMission%C3%A1riaAfricana-01.001_djvu.txt   (the doc-147 anchors are 5–6 words each; this is one verbatim 22-word span covering both)
$ … 'https://web.archive.org/web/20260203111247/https://www.cambridge.org/core/journals/journal-of-african-history/article/abs/development-of-an-african-catholic-church-in-the-kingdom-of-kongo-149117501/2FB5AD22282AF36704DE49E593623693' 'was widely accepted both in Kongo and in Europe as being the religion of the country'
LOCATED https://web.archive.org/web/20260203111247/https://www.cambridge.org/core/journals/journal-of-african-history/article/abs/development-of-an-african-catholic-church-in-the-kingdom-of-kongo-149117501/2FB5AD22282AF36704DE49E593623693
$ … 'https://openaccess-api.clevelandart.org/api/artworks/159880' 'Prestige Cap (mpu ngola), late 1800s–early 1900s. Africa, Central Africa, Democratic Republic of Congo'
LOCATED https://openaccess-api.clevelandart.org/api/artworks/159880
```

## Residual risk and verification gaps

- **Status cells:** S481/S483/S484 are filed `queued`/`used-by —`. Under the round-58 memo rule a
  superseding row whose superseded row stays cited should be `mined` with the same used-by
  (kongo-kingdom.md); if the L1 instead adopts the S-id swap, `used-by` follows the new id.
  Either way the cells need touching at integration (status/recheck/used-by are in-place-editable).
- **Sibling-slice consistency:** my fixes reference only my six lines. The same S359 p.469→470 and
  S384/S385 wording fixes also sit at lines 18, 65, 82, 84, 85, 89 (other seats) — the S-id choice
  and the "hangs behind his back" wording should be uniform across all of them.
- **S385 entry cite kept as S385:** S484's filed anchor does not carry the p. 61 note 5 quote the
  sentence's second clause relies on (locator-undemonstrable under pypdf's extraction; it is
  verbatim on the served page — verified in pdftotext output). If the L1 wants S484 cited there,
  a further superseding row would need that quote anchored.
- **Wayback transport:** two S385 locator runs hit `NOT_LOCATED HTTPError` (throttle), both
  retried to `LOCATED`; the capture is byte-identical to the row's recorded 303,987 bytes.
- **Not re-opened:** rows the lines also cite but the fixes do not touch (S411 UNESCO; S389
  Clist et al.; S374 title page) — their carrying text was out of this seat's item.
- `rejected:` none — every opened source carried a fix.

## installs

None. Tools used: `curl`, `pdftotext` 26.08.0 (host-installed), Python 3 stdlib (xml/html/re/json),
`git` read-only (`diff`, none else). Scratch downloads under `/tmp/revkongo58/`; kill nothing —
no long-lived processes started.
