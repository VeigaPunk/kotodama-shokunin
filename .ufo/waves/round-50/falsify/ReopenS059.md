# Reopen S059 — Sametinget Renmärken

Seat: `KotodamaR50-2.ReopenS059-21` (leaf, read-only). Round 50 falsify wave.
Landed target: `1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0` (base `4ad26836552462d28a946ca3b067cab0b5ce3532`).
All lane bytes read with `git show <sha>:<path>`; the URL was opened live this session. No clone,
no lane edits, no installs.

## Verdict: **PARTIAL**

Row S059 and its Gate bullet **hold** on every checked field: the URL answers 200 on the stated
route, the Gate quote is verbatim in the ingress directly under the H1, the footer date is exact,
and tier A is honest for the row's explicitly Sweden-scoped, agency-statement scope. The defect is
downstream in the entry: the two propositions that cite S059 write a **generic Sámi** earmark from a
**Swedish-only** source (the row itself says "not Norwegian law"), and one of them states "personal"
without the sameby-owner class the same page lists. Fix is two words plus one parenthetical; no row
change is needed.

Split verdict: **row HOLDS; C's entry citations PARTIAL.**

## 1. Row and Gate as landed

Row — `corpus/SOURCES.md:88` (11 fields, matching the header at `corpus/SOURCES.md:28`):

```
| S059 | Swedish Sámi Parliament (Sametinget), Renmärken — https://sametinget.se/renmarken | docs | A | the Swedish earmark institution as stated by the agency that keeps the register; not Norwegian law, not a court holding | page Renmärken (H1), opening paragraph; footer Senast uppdaterad 13 december 2024 | an earmark is a combination of cuts in both ears that names the owner; personal, usually inherited, registered for one sameby; unmarked reindeer are the sameby's collective property | mined | 2026-10-21 | 365d | corpus/knowledge/culture-material/pastoralism-animal-husbandry.md |
```

Gate bullet — `corpus/lessons/round-50.md:44`:

```
- S059 — https://sametinget.se/renmarken — accessed 2026-10-21 — opening paragraph under the H1: "Ett renmärke är kombinationen av snitt på både höger och vänster öra. Renmärket talar om vem som äger renen." Seat: SrcSamiReindeer.
```

Registry hygiene: `S059` occurs once in `corpus/SOURCES.md`; `git grep -n 'S059' 1c779e4 -- ':!corpus/SOURCES.md' ':!corpus/lessons/round-50.md'`
returns only `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md:7,64,77,116,189`;
`corpus/README.md` has 0 hits; the lesson has 1. `status=mined` with `used-by` naming that entry is
consistent, so no in-place change was owed under the append-only rule (`corpus/SOURCES.md:9-13`).
The row's field count (`awk -F'|' '/^\| S059 /{print NF-2}'` → `11`) matches the 11-column header.

## 2. URL re-opened this session

```
$ curl -sS -L --max-time 45 -o /tmp/s059.html -w 'HTTP %{http_code} url=%{url_effective} bytes=%{size_download}\n' https://sametinget.se/renmarken
HTTP 200 url=https://sametinget.se/renmarken bytes=32908

$ curl -sS -I -L --max-time 30 https://sametinget.se/renmarken
HTTP/2 200
content-type: text/html;charset=UTF-8
date: Wed, 21 Oct 2026 16:34:47 GMT
```

No redirect (`url_effective` identical to the row URL), no login/paywall, no bot wall on this route.
A second independent fetch (`/tmp/s059b.html`) returned the same text (raw byte hashes differ only in
per-session tokens); both fetches carried the quote and footer below verbatim. Deleted after the checks.

## 3. Quote verbatim and located

Raw HTML around the anchor:

```
<h1 id="upperContentH">Renmärken</h1>
<div class="ingress"><p>Ett renmärke är kombinationen av snitt på både höger och vänster öra. Renmärket talar om vem som äger renen. I Sverige finns det inga vilda renar. Alla renar ägs av någon privatperson, det kan vara ett barn eller en vuxen. En omärkt ren tillhör samebyn i området.</p></div>
```

Substring tests on the served bytes: both Gate sentences `True`; the quote is the first two sentences
of the H1 ingress, before the first subheading "Vem kan äga ett renmärke?" — exactly the row's
`page Renmärken (H1), opening paragraph`. Footer:

```
<div id="articleFooter">
    Senast uppdaterad: 13 december 2024  av Marie Enoksson.<!--updated-->
```

The row's `footer Senast uppdaterad 13 december 2024` is exact (punctuation/author omitted, immaterial).
Tier support sentence also verbatim: "Det är Sametingets ansvar att registrera och avregistrera
renmärken." (section "Renmärkesregister").

## 4. Tier and scope under QUALITY criterion 6

`corpus/QUALITY.md:29`: "publisher descriptions and abstracts are tier B for substantive claims about
a work, even when accurate; reserve tier A for sources primary or authoritative for the exact scope."

- The row claims **A** for "the Swedish earmark institution **as stated by the agency that keeps the
  register**; not Norwegian law, not a court holding." The page is Sametinget's own statement of its
  own register duty and its own institution, so the agency is primary for that narrow scope. This is
  not the round-49 publisher-blurb pattern (a page describing a third party's book): here the
  publisher is the institution the claim is about. The disclaimers are honest — it is an agency page,
  not statute and not case law, and it is Sweden-specific ("I Sverige finns det inga vilda renar";
  `sameby`).
- The landed build seat's own tier reasoning agrees (`.ufo/waves/round-50/build/SrcSamiReindeer.md`,
  "Tier reasoning", rows 1–8): A for the register/administration statement, not for statute or
  practice; corroboration only, not authority for this report.
- `teaches` is supported by the page: cuts in both ears and naming the owner (first sentence);
  personal and usually inherited, registered for use in one sameby, unmarked reindeer as the sameby's
  collective property (first body paragraph).

**Row passes criterion 6.**

## 5. Citation-by-citation audit of the entry

`git show 1c779e4:corpus/knowledge/culture-material/pastoralism-animal-husbandry.md | grep -n 'S059'`
→ lines 7, 64, 77, 116, 189.

| line | sentence | supported by what was read? |
|---|---|---|
| 7 | shelf list: `S059 Sametinget *Renmärken* (earmarks)` | **Yes.** Page is Sametinget's *Renmärken* page. No country qualifier here, but it is a list entry, not a rule. |
| 64 | `migration with the herd; earmark institutions (S059)` | **Yes as placed.** The citation follows the semicolon, so it attaches to "earmark institutions"; the page states the earmark institution. It says nothing about migration, but the migration clause is not cited to S059. Minor placement ambiguity only (N1). |
| 77 | `a Sámi earmark is a combination of cuts in both ears and names the owner (S059)` | **PARTIAL.** The mechanics are verbatim for Sweden, but the subject "a Sámi earmark" is wider than the source and the row's scope; no country qualifier anywhere in the entry (F1). |
| 116 | `a Sámi earmark is personal, usually inherited and registered for use in one herding community; unmarked reindeer are that community's collective property (S059)` | **PARTIAL.** "usually inherited", "registered for use in one sameby" and "unmarked = sameby's collective property" are verbatim-supported for Sweden; F1 applies, and "personal" omits the page's own sameby-owner class (F2). The status column's `B — one legal system` signals single-system calibration but does not name the country. |
| 189 | living-practice flag: `Mongolian, Sámi, Maasai, Bedu, WoDaaBe and Tibetan herding are living practice (S058, S059, S063)` | **Yes, minimally.** A 2024-updated official page about an operating register supports "the institution is current"; the substantive living-practice warrant rests on S058/S063. Not a defect. |

No other entry sentence repeats an S059 claim. The entry contains no `Sweden`/`Swedish`/`Norway`/
`Norwegian`/`reindrift`/`Lovdata` token:
`git show 1c779e4:<entry> | grep -n -i 'sweden\|swedish\|norway\|norwegian\|reindrift\|lovdata'` → no
hits (exit 1).

## 6. Findings and smallest fixes

**F1 — scope transfer, Swedish source used for a generic Sámi rule.** The row's scope is explicit:
"the **Swedish** earmark institution … **not Norwegian law**" (`SOURCES.md:88`). The page is
Sweden-specific (it says "I Sverige finns det inga vilda renar" and uses `sameby`, a Swedish
administrative form), and no Norwegian/Finnish row landed in S048–S069 (`SOURCES.md:77-98` lists no
such row) and the entry cites none. The entry's two propositions therefore assert more than the
opened source establishes for the non-Swedish Sámi. This is not a claim that the generic rule is
false — I did not open a Norwegian/Finnish source — only that S059 cannot carry it under QUALITY 1/6.
*Smallest fix:* add the qualifier at `:77` and `:116` — "a **Swedish** Sámi earmark …" (or "in
Sweden, a Sámi earmark …"). Two words, no row change.

**F2 — holder class: "personal" omits sameby ownership.** The same page, under
"Vem kan äga ett renmärke?", says verbatim: "Ett renmärke kan ägas av en sameby, en person som är
medlem i den sameby där märket skall användas eller en person som får ha skötesrenar i den sameby där
märket ska användas." The entry's unqualified "is personal" and the row's `teaches` ("personal,
usually inherited") compress the page's "mycket personligt" but drop the corporate-owner alternative.
*Smallest fix:* at `:116` — "a Sámi earmark is usually personal (a sameby may hold one), usually
inherited …". The row's `teaches` could take the same parenthetical; not required for the row to hold.

**N1 — `:64` citation placement (non-blocking).** `migration with the herd; earmark institutions
(S059)` puts the id after the second item; S059 does not support migration. Read as attached to
"earmark institutions" it is correct. If a reviewer reads cell-trailing ids as covering the whole
cell, cite the migration clause separately or move the id directly after "institutions" (it already
is).

**N2 — anchor is narrower than `teaches` (non-blocking; requested by ReviewSec08).** The Gate quote
and the row's anchor are the H1 ingress paragraph only. The inheritance / registration /
collective-property sentences are **not** in that paragraph; they are in the immediately following
first body paragraph (`<div class="text"><p>`), before `<h3>Vem kan äga ett renmärke?</h3>`:
"Omärkta renar är samebyns kollektiva egendom. Ett renmärke är mycket personligt och går vanligtvis i
arv inom släkten. Ett renmärke är registrerat för användning inom viss sameby. Ingen får samtidigt ha
mer än ett renmärke registrerat." Every taught fact is on the page, so §8's proposition is backed;
but the anchor names only the quote paragraph. `corpus/SOURCES.md` requires each Gate bullet to hold
the URL, access date and a verbatim quote, so one quote per row conforms. If the lane wants the anchor
coextensive with `teaches`, widen to "H1 ingress + first body paragraph, before 'Vem kan äga ett
renmärke?'". No fix required for admission.

## 7. What remains unresolved

- No Norwegian, Finnish or Russian Sámi source was opened, so the generic Sámi form of the earmark
  rule is **unsupported, not disproven**, outside Sweden. The row's own "not Norwegian law" makes
  that a scope defect in the entry rather than a truth claim.
- The underlying statute (SFS 1971:437) was not read; the row does not claim it, and the page's
  register-duty sentence is the agency's own statement.
- Nothing else in the row was left unverified.

## 8. Bounds and tooling honoured

Read-only; no lane file edited, no git index/jj state touched, no mutating git/jj command, no clone,
no background jobs, no delegation. Tool installs: none (pacman paused; nothing needed). Temp artifacts
`/tmp/s059.html` and `/tmp/s059b.html` were deleted after the checks.
