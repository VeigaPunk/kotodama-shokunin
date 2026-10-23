# ScoutPolishClanArms — Polish heraldic clans: one herb shared by many families, and the battle cry (zawołanie)

- seat: `KotodamaR57.ScoutPolishClanArms` (scout, claim C ground: heraldry/emblems/identity-marks entry — Polish heraldic clans)
- round: kotodama 57 (hyaku phase 4), 2026-10-22
- lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, claim base `0314aa981071220d206760b5263467faeea05b60`, declaration `13226c18aa352e3f3d1bfbe567f221acfb8b8344`
- assignment: 1–2 opened sources on Polish heraldry — the herb shared by many unrelated families (heraldic clans) and the zawołanie (battle/call cry) — as an open-access scholarly source or a public-domain armorial; every quote verified with the round locator `reports/round-57/reopen-quote.py`
- draft ids used below: `NEW-ScoutPolishClanArms-1` and `-2`; the L1 assigns the final `S` ids from the reserved block S413–S480 at integration

## Route summary

All reading 2026-10-22, plain ordinary requests (curl/urllib with a standard desktop User-Agent), no browser automation, no captcha bypass.

| source | URL | route | byte size |
|---|---|---|---|
| Gigoń 2012, *Znikające znaki*, Ogrody Nauk i Sztuk 2 (BazHum) | `https://bazhum.muzhp.pl/media/texts/ogrody-nauk-i-sztuk/2012-tom-2/ogrody_nauk_i_sztuk-r2012-t2-s253-262.pdf` | direct GET, HTTP 200, `application/pdf` | 1,104,463 |
| Wikipedia (polska), hasło „Zawołanie”, wersja 2026-09-30 | `https://pl.wikipedia.org/wiki/Zawo%C5%82anie` | direct GET, HTTP 200, `text/html` (Wayback capture 20260930233443 read this session; live URL also returns 200) | 127,104 (capture) |

Quotes below are all LOCATED by `python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-57/reopen-quote.py '<url>' '<quote>'`; each locator line is pasted under its quote. Both URLs are FRESH: `grep -c` on `corpus/SOURCES.md` prints 0 for `bazhum.muzhp.pl/media/texts/ogrody-nauk-i-sztuk/2012-tom-2` and for `pl.wikipedia.org/wiki/Zawo` (run this session; 0 matches, exit 1).

Polish is quoted as it stands in the served text (lower-case letters where the PDF text layer / HTML renders them; diacritics kept; HTML character references resolved by the reader).

---

### NEW-ScoutPolishClanArms-1

citation: Mateusz Gigoń, 2012. „Znikające znaki. Czy można prześledzić losy polskich herbów rycerskich w świetle źródeł średniowiecznych?”, *Ogrody Nauk i Sztuk* 2: 253–262. BazHum digital repository (Muzeum Historii Polski). ISSN 2353-7264.

url: https://bazhum.muzhp.pl/media/texts/ogrody-nauk-i-sztuk/2012-tom-2/ogrody_nauk_i_sztuk-r2012-t2-s253-262.pdf

route: direct GET (plain request), HTTP 200, `application/pdf`, 1,104,463 bytes, 11 pages; text layer extracted with pypdf (the round locator’s own PDF pipeline), read in full this session.

kind: paper

tier: A — the article’s own medievalist argument and examples (Bieniak’s characterisation quoted inside it is secondary, signalled below); authoritative for what the distinguishing dossier says about Polish knightly arms, not a primary charter source.

scope: how a medieval Polish coat-of-arms works as a clan sign — the shield device (herb) as a hereditary fixed mark, the vocal element (zawołanie / proclamatio) as a second essential part; arms as markers that bound one clan off from wider local/regional/state communities; the merging/merging problem of coats and rods; the concrete case of Piotr of Chechło using two cries (Glezyna and Larysza) in 1420–1453; modern heraldry’s goal of reconstructing social structure with genealogy.

quotes:
- §1 (znamię głosowe): "W średniowiecznej heraldyce polskiej dodatkowym istotnym elementem herbu jest znamię głosowe"
  - `LOCATED https://bazhum.muzhp.pl/media/texts/ogrody-nauk-i-sztuk/2012-tom-2/ogrody_nauk_i_sztuk-r2012-t2-s253-262.pdf`
- §1 (funkcja herbu): "herb wyodrębnia pewną grupę ród z szerszej społeczności lokalnej regionalnej państwowej nadaje jej granice"
  - `LOCATED https://bazhum.muzhp.pl/media/texts/ogrody-nauk-i-sztuk/2012-tom-2/ogrody_nauk_i_sztuk-r2012-t2-s253-262.pdf`
- §2 (ród rycerski, za Bieniakiem): "o rodach rycerskich jako realnych zwartych stosunkowo stronnictwach politycznych i solidarnych grupach społecznych"
  - `LOCATED https://bazhum.muzhp.pl/media/texts/ogrody-nauk-i-sztuk/2012-tom-2/ogrody_nauk_i_sztuk-r2012-t2-s253-262.pdf`
- §4 (Piotr z Chechła): "albowiem taż sama osoba piotr z chechła występuje raz z zawołaniem glezyn drugi raz z laryszą"
  - `LOCATED https://bazhum.muzhp.pl/media/texts/ogrody-nauk-i-sztuk/2012-tom-2/ogrody_nauk_i_sztuk-r2012-t2-s253-262.pdf`
- §3 (dziedziczność znaku): "herb dziedziczny ustalony znak kładziony w tarczy i nazwany danym mianem"
  - `LOCATED https://bazhum.muzhp.pl/media/texts/ogrody-nauk-i-sztuk/2012-tom-2/ogrody_nauk_i_sztuk-r2012-t2-s253-262.pdf`
- §1 (cel badań): "jednym z celów nowoczesnej heraldyki jest rekonstrukcja struktury społeczeństwa średniowiecznego wraz z genealogią"
  - `LOCATED https://bazhum.muzhp.pl/media/texts/ogrody-nauk-i-sztuk/2012-tom-2/ogrody_nauk_i_sztuk-r2012-t2-s253-262.pdf`

teaches: In medieval Polish knightly heraldry the vocal sign (zawołanie) stood beside the shield device and identified men who shared no single coat.

draft sentences:
- Give a heraldic clan a vocal sign beside its image: the article treats the zawołanie/proclamatio as a second, essential element of the medieval Polish coat, so a house can be announced by cry as well as by shield (NEW-ScoutPolishClanArms-1, §1 znamię głosowe).
- Design the clan as a solidarity group rather than a bloodline: the article, after Bieniak, describes knightly clans as real political factions and solidarity groups, which frees a shared coat from being read as proof of kinship (NEW-ScoutPolishClanArms-1, §2).
- Let one clan show overlapping or split coats: since the article records the same person using two different cries, and coats being identified, split or merged, a worldbuilder may draw several emblems for one family without changing its membership (NEW-ScoutPolishClanArms-1, §4).
- Make the shield mark hereditary and stable: the article defines the coat as an inherited fixed sign placed in the shield under a set name, so continuity of the badge is what marks the lineage (NEW-ScoutPolishClanArms-1, §3).
- Use heraldry as social cartography: the source frames modern heraldry as reconstructing medieval social structure alongside genealogy, so a faction’s arms are at least as telling as its family tree (NEW-ScoutPolishClanArms-1, §1 cel badań).

---

### NEW-ScoutPolishClanArms-2

citation: Wikipedia (polska), hasło „Zawołanie”, wersja z 30 września 2026 (Wayback capture 20260930233443, live URL also fetchable). Tekst encyklopedyczny; przytacza liczby Józefa Szymańskiego (116 zawołań najstarszych herbów; 189 łącznie do końca XV w.).

url: https://pl.wikipedia.org/wiki/Zawo%C5%82anie

route: direct GET, HTTP 200, `text/html` (127,104 bytes capture read this session; the live page was also fetched by the locator with HTTP 200 during quote verification).

kind: web

tier: C — tertiary encyclopedia entry; useful for the synoptic definition and the Szymański counts, not a primary or peer-reviewed source; L1 should lean on row 1 for medieval claim strength.

scope: definition of zawołanie as the verbal element of the Polish noble coat; its functional origin (identifying clan members, summoning them to war — wici); the Szymański statistics; the fact that coats created later by ennoblement (nobilitacja) or indygenat lack a cry; one coat able to carry several cries by branch.

quotes:
- Lead, zdanie definicyjne: "werbalny element polskiego herbu szlacheckiego, jedna z cech charakterystycznych polskiej heraldyki"
  - `LOCATED https://pl.wikipedia.org/wiki/Zawo%C5%82anie`
- Sekcja funkcji pierwotnych: "pierwotnie w Polsce zawołania posiadały funkcję co najmniej równorzędną ze znakami plastycznymi, czyli herbami"
  - `LOCATED https://pl.wikipedia.org/wiki/Zawo%C5%82anie`
- Sekcja funkcji pierwotnych: "stanowiło prawdopodobnie rodzaj hasła identyfikującego członków rodu, stosowanego w systemie mobilizacji oddziałów zbrojnych oraz w bitwie"
  - `LOCATED https://pl.wikipedia.org/wiki/Zawo%C5%82anie`
- Sekcja statystyczna (Szymański): "ustalone przez J. Szymańskiego 116 zawołań łączyć należy z najstarszymi herbami polskimi"
  - `LOCATED https://pl.wikipedia.org/wiki/Zawo%C5%82anie`
- Sekcja statystyczna: "Łącznie znane jest 189 zawołań pojawiających się w źródłach do końca XV wieku"
  - `LOCATED https://pl.wikipedia.org/wiki/Zawo%C5%82anie`
- Sekcja o gałęziach: "Niekiedy jeden herb posiadał kilka różnych zawołań, charakterystycznych dla odrębnych gałęzi rodu"
  - `LOCATED https://pl.wikipedia.org/wiki/Zawo%C5%82anie`

teaches: Zawołanie is the verbal element of the Polish noble coat: old arms carry it, new grants need not, and one coat can bear several cries.

draft sentences:
- Frame the Polish coat as a compound mark with a verbal part: the encyclopedia defines zawołanie as the verbal element of the noble coat and a distinctive feature of Polish heraldry, so a design system should treat cry and image as two channels (NEW-ScoutPolishClanArms-2, lead).
- Give the cry a function beyond ornament: originally the cries had a function at least equal to the plastic signs and served to identify clansmen and summon them to battle, which fits battle scenes and muster (NEW-ScoutPolishClanArms-2, funkcje pierwotne).
- Time your cries to the age of your arms: the 116 cries Szymański ties to the oldest Polish coats, and 189 known by 1500, suggest newer ennobled houses may legitimately lack a cry (NEW-ScoutPolishClanArms-2, statystyka).
- Differentiate branches by cry rather than by image: because one coat could carry several different cries characteristic of separate branches of the clan, keep one shield while varying the war-word per lineage (NEW-ScoutPolishClanArms-2, gałęzie).

---

## Findings, attacks and limits for the L1

1. **Two robust LOCATED rows.** Both URLs answered the round locator this session with `LOCATED` on every quote above, and both are FRESH (0 rows in SOURCES.md). BazHum serves the file as a direct, sizeable PDF (HTTP 200); Wikipedia serves plain HTML.
2. **The vocal element is the Polish differentiator.** Both sources agree the cry is a real structural part of the Polish coat, not an ornament; row 1 adds that it worked in the identification/merging of rods, row 2 adds the Szymański counts and the later-grant absence. Use them to say *ga* a Polish-style heraldic clan is a solidarity group, not a proven bloodline (row 1 quote 2, Bieniak), and that one herb can be shared by unrelated families precisely because the coat is a legal-political marker.
3. **Chechło example** (row 1, quote 4) is the strongest single design fact: one man, two cries (Glezyna/Larysza), 1420–1453 → cries are not one-to-one with coats or families.
4. **Locator PDF pipeline verified.** The locator extracts PDF text via `uv run --no-project --quiet --with pypdf==5.4.0`; verified working on this host (pypdf 5.4.0 fetched by uv into its ephemeral env; no system install). The `--with` resolution is part of the LOCATE leg and succeeded.
5. **Not opened / rejected:** Wroniszewski 2016 („Studya heraldyczne Antoniego Małeckiego…”, Studia z Dziejów Średniowiecza 20) — the journal’s full-text PDF at `https://ejournals.eu/en/journal_article_files/full_text/018ecedb-4235-71f4-94b4-b64274a57c0b/download` timed out twice (curl exit 28, 0 bytes) and has no Wayback capture; rejected as unserviceable this session. Niesiecki *Herbarz polski* (Bobrowicz ed. 1839–1846): archive.org items exist (`herbarzpolskika00bobrgoog`, `herbarzpolskipow05niesuoft`) but archive.org was unreachable from this environment (same as S052 note); the Radom digital library DjVu copy (`https://bc.radom.pl/dlibra/doccontent?id=44164`) has no OCR text layer (djvutxt output empty), so no served text to locate; Wielkopolska WBC DjVu (`https://www.wbc.poznan.pl/Content/1147/download/`) likewise empty text layer; pl.wikisource has no transcription of Długosz *Insignia seu clenodia* (API search: none). Any of these is a good candidate for a later round if a text-layer copy surfaces.
6. **Tooling record:** no persistent installs. Attempted `uv tool install pypdf` → fails (pypdf provides no executables; uv removes the tool entry); `python3 -m pip` absent on this image. Used `uv run --with pypdf==5.4.0` (ephemeral, official channel) for extraction, and plain `curl`/urllib for fetches; `pdftotext`, `ddjvu`, `djvutxt` already present. Nothing written anywhere but this report and /tmp scratch.
