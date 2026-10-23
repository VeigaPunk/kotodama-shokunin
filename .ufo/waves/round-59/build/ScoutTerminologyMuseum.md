# ScoutTerminologyMuseum — round 59 build, claim C source item

Subtopic: the vocabulary itself — how a museum or reference work defines amulet, talisman, charm
and the protective object, and where the terms separate. Design decisions aimed at: what the object
is made of and how it is mounted, what danger it answers, who makes or charges it, and what the word
on the label commits the worldbuilder to.

Ids assigned: **S644, S645**. Two rows offered; both print `LOCATE PASS BOILER PASS RELEVANCE PASS
TOPIC PASS` against `reports/round-59/rowcheck.py` with the entry stub. One further row (S645-spare,
Catholic Encyclopedia) is fully verified by the same four legs but withheld under the two-row cap
(§ Spare, below) so the L1 can lift it if an id frees up.

Discovery note (what I was looking for): a museum page that quotes a dictionary/OED definition of
*amulet* and then widens *charm*; and a museum page that separates *amulet* from *talisman* by the
origin of the power. Both were found as ordinary public pages; no challenge, paywall or login was
touched.

## Rowcheck (verbatim, `EXIT=0`)

```
S644 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://prm.web.ox.ac.uk/files/amuletspdf | BOILER: root-clear https://prm.web.ox.ac.uk/; not a title, h1 or meta label | RELEVANCE: shared=['amule', 'charm', 'dicti', 'disea', 'evil', 'misch'] | TOPIC: quote_hits=2 function_words=6 page_hits=80 page_terms=113 need=1/2/3/2
S645 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://www.aub.edu.lb/museum_archeo/Pages/Amulets-&-Talismans.aspx | BOILER: root-clear https://www.aub.edu.lb/; not a title, h1 or meta label | RELEVANCE: shared=['amule', 'charg', 'creat', 'natur', 'objec', 'power'] | TOPIC: quote_hits=3 function_words=7 page_hits=25 page_terms=22 need=1/2/3/2
EXIT=0
```

Command run:
`cd /fast/scratch/hyaku/kotodama-r59/ScoutTerminologyMuseum && timeout 900 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-59/rowcheck.py --draft /fast/scratch/hyaku/kotodama-r59/ScoutTerminologyMuseum/rows.md --entry /fast/scratch/hyaku/kotodama-r59/ScoutTerminologyMuseum/stub.md`

## Rows (exactly 11 cells each)

| S644 | Pitt Rivers Museum, University of Oxford, *Discover... Amulets and charms* (introductory guide leaflet, undated) — https://prm.web.ox.ac.uk/files/amuletspdf (direct, HTTP 200, 449625 bytes); capture https://web.archive.org/web/20250808020412id_/https://prm.web.ox.ac.uk/files/amuletspdf | docs | B | the museum's own working definition of amulet and charm, quoted from the Oxford English Dictionary, and its caveat that not every ritual object is one | leaflet introduction: "An amulet is defined by the Oxford English Dictionary as: ‘Anything worn about the person as a charm preventative against evil, mischief, disease, witchcraft, etc.’" | A museum leaflet adopts the dictionary sense of amulet as a worn charm against evil, mischief, disease and witchcraft, and adds that a charm may also be a spoken spell. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md |
| S645 | American University of Beirut Archaeological Museum, *Amulets & Talismans at the AUB Museum* (museum web page, undated) — https://www.aub.edu.lb/museum_archeo/Pages/Amulets-&-Talismans.aspx (direct, HTTP 200, 86605 bytes); capture https://web.archive.org/web/20240917194011id_/https://www.aub.edu.lb/museum_archeo/Pages/Amulets-&-Talismans.aspx | docs | B | how a university museum splits amulet from talisman by the origin of the power, and what that split does to who may make the object | page text, second paragraph: "The amulet is an object with natural magical properties, whereas a talisman must be charged with magical powers by a creator" | A university museum separates the pair by the source of power: an amulet's potency is natural to the object, while a talisman must be charged by its creator. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md |

Cell facts: S644 quote is 25 whitespace words (the top of the 10–25 band), S645 quote is 21; each
locator cell holds exactly one straight-double-quoted span and no other URL; each source cell holds
exactly two URLs, the live page first and a capture of that same page second (both captures were
re-opened this session and located the same quote).

## Gate lines

- S644 — https://prm.web.ox.ac.uk/files/amuletspdf — accessed 2026-10-23 — leaflet introduction: “An amulet is defined by the Oxford English Dictionary as: ‘Anything worn about the person as a charm preventative against evil, mischief, disease, witchcraft, etc.’”. Grounds: A museum leaflet adopts the dictionary sense of amulet as a worn charm against evil, mischief, disease and witchcraft, and adds that a charm may also be a spoken spell. Seat: KotodamaR59.ScoutTerminologyMuseum.
- S645 — https://www.aub.edu.lb/museum_archeo/Pages/Amulets-&-Talismans.aspx — accessed 2026-10-23 — page text, second paragraph: “The amulet is an object with natural magical properties, whereas a talisman must be charged with magical powers by a creator”. Grounds: A university museum separates the pair by the source of power: an amulet's potency is natural to the object, while a talisman must be charged by its creator. Seat: KotodamaR59.ScoutTerminologyMuseum.

## Draft entry sentences

S644:

The Pitt Rivers leaflet defines an amulet only as something worn about the person against evil, mischief, disease and witchcraft, so a museum label using the word is asserting a worn object, not a rite (S644).

It quotes the same dictionary for charm and then widens charm to cover a spoken spell or incantation, which is the one place the two words part company in museum usage (S644).

The leaflet also concedes that some objects on display are technically neither amulet nor charm but ritual objects given a supernatural power, so the boundary drawn on the label is curatorial rather than native (S644).

S645:

A university museum draws the line at where the power comes from: an amulet is protective by nature, while a talisman becomes protective only once its maker charges it (S645).

That charging is described as an act of consecration and as purpose-built, so a talisman answers one stated reason while an amulet may serve general luck or protection (S645).

The same page labels each object with a material and a suspension, faience or limestone or bronze hanging from a ring or a lateral piercing, so the vocabulary choice arrives with a mounting choice (S645).

## What I opened (all ordinary GETs, this session)

| URL | status | bytes | read |
|---|---|---|---|
| https://prm.web.ox.ac.uk/files/amuletspdf | 200 | 449,625 (application/pdf) | full 4,165-word leaflet text, extracted with the instrument's own pypdf path; definitions, the "sympathetic magic" passage, the technical-caveat passage, per-region object notes |
| https://web.archive.org/web/20250808020412id_/https://prm.web.ox.ac.uk/files/amuletspdf | 200 | captures the same PDF | quote located; listed as the row's second URL |
| https://prm.web.ox.ac.uk/ (BOILER root) | 200 | 190,511 | quote absent (root-clear) |
| https://www.aub.edu.lb/museum_archeo/Pages/Amulets-&-Talismans.aspx | 200 | 86,605 | full 1,261-word page: the amulet/talisman definition, the "form, material and color" sentence, five object entries (Nefertum, wedjat eye, monkey, Medusa, hand) |
| https://web.archive.org/web/20240917194011id_/https://www.aub.edu.lb/museum_archeo/Pages/Amulets-&-Talismans.aspx | 200 | same page | quote located; listed as the row's second URL |
| https://www.aub.edu.lb/ (BOILER root) | 200 | 96,924 | quote absent (root-clear) |
| https://www.newadvent.org/cathen/01443a.htm | 200 | 19,357 | Catholic Encyclopedia, *Amulet* (1913): Greek *phylakterion*, Latin *amuleta*, the Church's emblem substitution, the Laodicea canon, the "dispensing of amulets was a regular profession" passage — spare row, below |
| https://www.newadvent.org/ (BOILER root for the spare) | 200 | 41,886 | quote absent (root-clear) |

Wayback discovery calls (not sources): `https://archive.org/wayback/available?url=…` for both offered
live URLs, and the CDX API for `newadvent.org/cathen/01443a.htm`.

## Rejected / not offered (with the tool output that decided it)

- **https://www.metmuseum.org/essays/egyptian-amulets** — probe: `HTTPError: HTTP Error 429: Too Many Requests`. The best-fitting page for the talisman gloss (the Met essay that calls a talisman "any object that is imbued with protective powers") is on that host; it refused every plain GET I made, so no row.
- **https://www.metmuseum.org/essays/amulets-and-talismans-from-the-islamic-world** — `HTTPError: HTTP Error 429: Too Many Requests`. Same host, same refusal.
- **https://www.britannica.com/topic/amulet** — `HTTPError: HTTP Error 403: Forbidden`.
- **https://iranicaonline.org/articles/amulet** — `HTTPError: HTTP Error 404: Not Found` (no such entry path; I did not guess a second path).
- **https://www.jewishencyclopedia.com/articles/1447-amulet** — HTTP 200, 89,125 bytes, but the served page is `AMUSEMENTS - JewishEncyclopedia.com` (786 words, zero occurrences of "amulet"): the id in the path does not address the Amulet article, so the page cannot vouch for anything.
- **https://www.fitzmuseum.cam.ac.uk/** — `HTTPError: HTTP Error 503: Service Unavailable` (root only; no candidate page reached).
- **https://museum.birzeit.edu/tawfiq-canaan-amulets-and-talismans-collection** — `URLError <urlopen error timed out>` after 123 s; the Tawfiq Canaan amulet collection page would have been a strong Palestinian maker/script row but the host did not answer.
- **https://web.archive.org/web/20260711151602id_/https://www.newadvent.org/cathen/01443a.htm** — `NOT_LOCATED … quote-absent`: the capture replays gzip bytes that the instrument decodes as text (4,988 chars of binary, `amulet` count 0), so no capture of that host is listed on any row. Second capture (20250126183436) behaves identically.
- **Catholic Encyclopedia row** — verified, not offered: see § Spare.

## Spare (verified PASS, not offered under the two-row cap)

If an id frees up, this row already passes all four legs against the same stub; it carries the
religious-reform and phylactery-naming axis rather than the pure vocabulary split.

| S645 | Catholic Encyclopedia (1913), "Amulet", New Advent online edition — https://www.newadvent.org/cathen/01443a.htm (direct, HTTP 200, 19357 bytes) | book | B | how a religious authority reclassifies amulets as emblems, and the Greek and Latin names the entry gives for the object | opening paragraph: "the Church, while forbidding amulets, permitted the use of emblems which would remind the bearers of some doctrine of Christianity" | A church that forbids amulets can still license emblems carrying doctrine, so reform renames the worn protective object rather than ending the habit. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md |

Verbatim legs for that row when it was run with the stub (before the AUB row replaced it):

```
S645 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://www.newadvent.org/cathen/01443a.htm | BOILER: root-clear https://www.newadvent.org/; not a title, h1 or meta label | RELEVANCE: shared=['amule', 'churc', 'doctr', 'emble', 'forbi'] | TOPIC: quote_hits=1 function_words=3 page_hits=27 page_terms=26 need=1/2/3/2
```

## Notes for the L1

1. **The AUB URL contains a literal `&`** (`…/Pages/Amulets-&-Talismans.aspx`). Copy it byte for byte; percent-encoding it to `%26` addresses a different request. Rowcheck's URL regex keeps `&`, and the live fetch, the capture replay and the root check all succeeded on this exact string.
2. **Host distinctness.** S644's host `prm.web.ox.ac.uk` is not the `web.prm.ox.ac.uk` that other build rows use (six URLs in the sibling reports), so the two Pitt Rivers rows do not collapse into one DISTINCT host. S645 sits on `www.aub.edu.lb`, which no row in `corpus/SOURCES.md` or in the sibling build reports uses.
3. **Where the entry's vocabulary section can lean.** S644 gives the worn-object sense and the charm-as-spell widening; S645 gives the natural-versus-charged split and names the maker as the one who charges. Together they answer "what is the difference between amulet, talisman and charm" with two museums' own words, not with an editor's synthesis. Neither row defines *apotropaic* as a term, and no row here gives the etymology; if the entry states either, source it elsewhere.
4. **No installs** and no updates were made for this item; the only tools used were `python3`, `curl` and the round-59 instruments. Nothing was left running; all scratch files are under `/fast/scratch/hyaku/kotodama-r59/ScoutTerminologyMuseum/` (`rows.md`, `stub.md`, `probe.py`, `prm-amulets.pdf`, `prm-amulets.txt`, `aub.txt`, `ce-amulet.txt`).
5. **Remaining unknown.** A museum page that defines *talisman* primarily as an inscribed object (the Met's Islamic-world essay) stayed behind a 429; the AUB row splits the pair by charging, not by inscription. If the entry wants "the words on it are what make it work" as a *definitional* claim, that needs another seat's row.

Seat: KotodamaR59.ScoutTerminologyMuseum. Report written 2026-10-23.
