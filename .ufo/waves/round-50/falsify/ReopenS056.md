# ReopenS056 — falsify attack: SOURCES S056 (Khazanov 2019, Chungara)

Lane: kotodama-shokunin, `main`. Attacked artifact: landed commit
`1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0` (base `4ad2683`). Read-only seat; no lane
bytes edited, no clone created (landed bytes read with `git show`), no subagents, no
installs.

## Verdict: **HOLDS**

The row, its Gate bullet, the URL, the quote, the stated location, the tier/scope, and
all four S056 citations in the entry survive attack. Two non-blocking precision notes
are recorded below; neither contradicts a sentence the entry asserts on S056's authority.

## 1. Row and Gate as landed

Row (`corpus/SOURCES.md:85`):

```
| S056 | Khazanov 2019, Steppe Nomads in the Eurasian Trade, Chungara 51(1):85–93 — https://www.scielo.cl/pdf/chungara/v51n1/0717-7356-chungara-00302.pdf | paper | A | Khazanov's own thesis of nomadic non-autarky and trade under political pressure; B for the historical episodes it reports | Abstract p. 85; p. 87; p. 89 | nomads always needed external grain and crafts; sedentary states used trade as political pressure; tribute and gifts from dependent sedentary populations | mined | 2026-10-21 | 365d | corpus/knowledge/culture-material/pastoralism-animal-husbandry.md |
```

Gate bullet (`corpus/lessons/round-50.md:41`):

```
- S056 — https://www.scielo.cl/pdf/chungara/v51n1/0717-7356-chungara-00302.pdf — accessed 2026-10-21 — Abstract, p. 85: "always experienced a need for external agricultural and handicraft products". Seat: ScribeSec09Relations.
```

The Gate carries the three things the SOURCES header requires (URL, access date,
verbatim quote; `corpus/SOURCES.md:8-9`). Gate quote length: 10 words, under the
≤25-word convention used by the round's other bullets.

## 2. URL opened this session (2026-10-21)

```
$ curl -sS -L -o khazanov.pdf -w 'HTTP %{http_code} | %{content_type} | %{size_download} bytes | %{url_effective}\n' \
  'https://www.scielo.cl/pdf/chungara/v51n1/0717-7356-chungara-00302.pdf'
HTTP 200 | application/pdf | 1734103 bytes | https://www.scielo.cl/pdf/chungara/v51n1/0717-7356-chungara-00302.pdf
$ sha256sum khazanov.pdf
45e704afb6368a0b975d9e49d97bfd62c3cb33692cef9aaf3097a80afdaedf6d  khazanov.pdf
$ pdfinfo khazanov.pdf   # Pages: 10, PDF 1.4, created 2019-05-10
```

The PDF's title page confirms the identity: `Volumen 51, N° 1, 2019. Páginas 85-93`,
`Chungara Revista de Antropología Chilena`, "STEPPE NOMADS IN THE EURASIAN TRADE",
Anatoly M. Khazanov, DOI `10.4067/S0717-73562019005000302`, published online 1 March
2019. Title, author, journal, volume/issue and page range in the row all match.

Printed-page mapping was verified, not assumed: PDF p.1 carries the range header and
starts the article (printed 85 — first pages of SciELO articles carry no folio); PDF p.2
is printed 86, p.3 → 87, p.4 → 88, p.5 → 89, p.9 → 93, p.10 blank. Thus the row's
anchors p. 87 and p. 89 land where the row says they do.

Route note: the SciELO HTML landing route
`scielo.php?script=sci_arttext&pid=S0717-73562019000100302` returns **HTTP 403**
(Cloudflare "Just a moment..."), and DOI `10.4067/S0717-73562019005000302` redirects to
that 403 route. This is not a finding against the row: the row cites the PDF route,
which returns HTTP 200 and the exact article. It does mean the PDF is the only open
route on this host today.

## 3. Quote and location

`pdftotext -layout` p.85 (PDF p.1), English abstract:

> The specialized and non-autarchic character of their economy, provoked that the nomads
> **always experienced a need for external agricultural and handicraft products**.

The Gate quote is a verbatim contiguous substring of that abstract sentence, on the page
the row and bullet name (Abstract, p. 85). The article body repeats the same claim
without "external" on the same page:

> Because of a specialized and non-autarchic character of their economy the nomads always
> experienced a need for agricultural and handicraft products (Khazanov 1994).

So the A-anchor does not rest on the abstract alone; the body carries the non-autarky
thesis independently.

The row's other anchors verify at their stated pages:

- p. 87, §Regional and Interregional Trade: "In quite different historical periods,
  many sedentary states, especially China, but sometimes Central Asia states as well,
  considered the trade with nomads as a way of applying a political pressure on them."
  Same page: "its governments required that in order to trade nomads had to admit their
  political dependence on China, and nomads resorted to arms to acquire the right to
  trade"; and the Xiongnu treaties where "the latter always insisted that the Chinese
  government should pledge to open markets at its frontier centers."
- p. 89, §Long-distance Trade: "Successful nomadic states and polities always got much
  more goods, as gifts, tribute, revenues, and by other means, from dependent sedentary
  populations and states, than they could utilize themselves."
- p. 89, Scythian example: "The Scythian aristocracy recolected tribute such as grain, as
  well as slaves paid by the dependent cultivators on the Greek markets".

Every element of the row's `teaches` column is therefore present in the paper at the
stated anchors, with one paraphrase note in §6 below.

## 4. Tier and scope under QUALITY criterion 6

`corpus/QUALITY.md:29` (criterion 6): abstracts/publisher descriptions are tier B for
substantive claims *about a work*; tier A is reserved for sources primary or
authoritative for the exact scope. The row's tier cell scopes A narrowly to "Khazanov's
own thesis of nomadic non-autarky and trade under political pressure" and declares B for
"the historical episodes it reports".

That is honest:

- The 2019 article is an original, peer-reviewed paper ("This manuscript was evaluated by
  external reviewers", p.85 fn.1) by the thesis's author; SOURCES.md's own A definition
  explicitly includes "original paper" (`corpus/SOURCES.md:14-16`).
- The A scope is attribution ("Khazanov's own thesis"), not the truth of the thesis at
  large; the paper's body (p.85, quoted above) states it in the author's own voice, so
  the A-anchor is the paper, not a third-party abstract.
- The episode claims (Scythian tribute, Xiongnu silk rolls, etc.) are marked B in the same
  cell; that matches the paper, which reports them from other authorities (e.g. Kradin
  2002:189) and does not itself do the primary work.

No tier correction (superseding row) is warranted.

## 5. Every S056 citation in the entry

`git show 1c779e…:corpus/knowledge/culture-material/pastoralism-animal-husbandry.md`
contains five S056 hits (four citations plus the shelf list):

| line | text | support assessment |
|---|---|---|
| 7 | shelf list: "S056 Khazanov 2019 (non-autarky)" | correct bibliographic pointer; the row is opened and mined. |
| 122 | "A herding economy is non-autarkic by construction: steppe nomads \"always experienced a need for external agricultural and handicraft products\" (S056)." | quote verbatim from Abstract p.85; the quoted clause is correctly scoped to "steppe nomads". First clause is a method-level generalization (note 1). |
| 127 | "Trade under pressure \| the sedentary state licenses markets; nomads force them open (S056)" | supported by p.87 (states treat trade as political pressure; China requires political dependence; nomads resort to arms; treaties pledge open frontier markets). |
| 157 | build step 7 "Relations \| the sedentary neighbour, its power and the exchange form \| §9; S056" | pointer to §9; §9's S056 content is supported above. |
| 180 | calibration bank: "The 'pure nomad' lives on the herd alone \| R as description — S056: nomads always needed external grain and crafts" | R verdict follows from p.85 (external need) and p.89 (grain tribute); "grain" is a narrowing paraphrase (note 2). |

The seat's own source dossier (`.ufo/waves/round-50/build/ScribeSec09Relations.md:32-41`)
was also sampled: nine located quotes attributed to pp. 85, 87, 88, 89, 90, 91 were each
found verbatim in the PDF at the stated page (including "no unambiguous evidence of the
existence of indigenous professional traders in any nomadic society", p.88; "10,000 silk
rolls", p.89; "temporary shelter in tents", p.91; "pillaged by the Kazaks", p.87). No
fabricated or mispaged quote in the dossier. The seat's note that the silk-roll figures
are "to-verify" against Kradin 2002 is honest: the paper cites Kradin 2002:189 for the
number.

## 6. Precision notes (non-blocking)

1. **Generalizing clause at entry:122.** "A herding economy is non-autarkic by
   construction" is broader than S056's scope (nomads of the Eurasian steppes,
   semi-deserts and deserts). The sentence's cited evidence is explicitly "steppe
   nomads", and the entry's §1 dependence dial (S066: "Dependence varies … design a
   **dial**, not a type") already prevents reading it as a universal degree claim. The
   seat draft had a status sentence ("non-autarky is mainstream [K19][D87]",
   `ScribeSec09Relations.md:11`); the landed entry dropped it, so the entry is in fact
   *more* conservative than its draft — it never asserts consensus. If the author-lane
   wants belt-and-braces, add "Khazanov's steppe case" before the colon; nothing requires
   it.
2. **"grain" narrowing at row `teaches` and entry:180.** The paper's need claim is
   "agricultural … products"; grain appears only as Scythian tribute (p.89). "Grain and
   crafts" is a defensible précis (grain is the article's one named agricultural good and
   it flows to nomads), but it is not the abstract's word. Optional hardening in a future
   row: "external agricultural products and crafts". This is paraphrase precision, not a
   misquote: the quoted text in the row, Gate and entry is exact.

## 7. Tooling / cleanup

No tools installed or upgraded. Used preinstalled `curl 8.23.0` (HTTP open) and
`pdftotext 26.08.0` / poppler (text extraction). Working directory `/tmp/s056probe`
(PDF 1.7 MB + extracted text) deleted after the evidence was captured; the host
filesystem is at 96% and no clone was made.
