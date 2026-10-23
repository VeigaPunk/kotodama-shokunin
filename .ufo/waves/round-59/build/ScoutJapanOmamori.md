# ScoutJapanOmamori — claim C source item (S624, S625)

Scope: Japanese omamori / ofuda as protective objects — shrine and temple issue, materials,
inscriptions, household placement, what they answer, and the yearly return-and-renew cycle.
Two rows offered, both checked with the round-59 instrument. All fetches with the acceptance
User-Agent (`Mozilla/5.0 (X11; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0`), ordinary
GETs only, no browser, no challenge solving.

## Rows

| S624 | Okada Yoshiyuki, Encyclopedia of Shinto (Kokugakuin University), n.d., Shinsatsu, Mamorifuda — https://d-museum.kokugakuin.ac.jp/eos/detail/?id=9633 (direct, HTTP 200, 17563 bytes); capture https://web.archive.org/web/20260415164210id_/https://d-museum.kokugakuin.ac.jp/eos/detail/?id=9633 | docs | B | shrine-issued shinsatsu as a symbolic talisman of a spiritual being's supranormal power, with its materials, placement and mamorifuda counterpart | Text: "Shinsatsu are a type of thaumaturgic talisman (also known as gofu) distributed at shrines and symbolic of a spiritual being or its supranormal power" | A shrine-issued talisman called shinsatsu is understood as a symbolic token of a spiritual being and its power. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md |
| S625 | Japan Tourism Agency (MLIT), n.d., Koshinpu Nosatsusho, Box to Return Old Amulets, JTA Sightseeing Database — https://www.mlit.go.jp/tagengo-db/en/H30-00525.html (direct, HTTP 200, 17999 bytes) | docs | B | yearly return of used omamori and household ofuda to a shrine box and their burning | Text: "Omamori, the lucky charms available at shrines, are usually returned once they have served their purpose, or if they are more than a year old" | A shrine omamori is normally returned once its purpose is served or after roughly a year, instead of being kept. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md |

## Gate lines

- S624 — https://d-museum.kokugakuin.ac.jp/eos/detail/?id=9633 — accessed 2026-10-23 — Text: “Shinsatsu are a type of thaumaturgic talisman (also known as gofu) distributed at shrines and symbolic of a spiritual being or its supranormal power”. Grounds: A shrine-issued talisman called shinsatsu is understood as a symbolic token of a spiritual being and its power. Seat: ScoutJapanOmamori.
- S625 — https://www.mlit.go.jp/tagengo-db/en/H30-00525.html — accessed 2026-10-23 — Text: “Omamori, the lucky charms available at shrines, are usually returned once they have served their purpose, or if they are more than a year old”. Grounds: A shrine omamori is normally returned once its purpose is served or after roughly a year, instead of being kept. Seat: ScoutJapanOmamori.

## rowcheck output (verbatim)

```
$ cd /fast/scratch/hyaku/kotodama-r59/ScoutJapanOmamori && timeout 900 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-59/rowcheck.py --draft /fast/scratch/hyaku/kotodama-r59/ScoutJapanOmamori/rows_final.md --entry /fast/scratch/hyaku/kotodama-r59/ScoutJapanOmamori/stub4.md
# rows_final.md is the two `| S6…` lines copied verbatim out of this report; stub4.md is the
# "Draft sentences" block below.
S624 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://d-museum.kokugakuin.ac.jp/eos/detail/?id=9633 | BOILER: root-clear https://d-museum.kokugakuin.ac.jp/; not a title, h1 or meta label | RELEVANCE: shared=['power', 'shins', 'shrin', 'spiri', 'symbo', 'talis'] | TOPIC: quote_hits=2 function_words=8 page_hits=12 page_terms=11 need=1/2/3/2
S625 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://www.mlit.go.jp/tagengo-db/en/H30-00525.html | BOILER: root-clear https://www.mlit.go.jp/; not a title, h1 or meta label | RELEVANCE: shared=['omamo', 'purpo', 'retur', 'serve', 'shrin', 'year'] | TOPIC: quote_hits=2 function_words=6 page_hits=11 page_terms=11 need=1/2/3/2
```

## Draft sentences

A shinsatsu is a shrine-distributed talisman that stands for a spiritual being and its supranormal power (S624).
Shinsatsu may be made of wood, paper or metal and carry a written or printed inscription (S624).
Large shinsatsu are enshrined in a household kamidana or affixed above gates, doors, pillars or ceilings (S624).
The smaller mamorifuda is a talisman carried on the person in a brocade bag, used against illness, misfortune and traffic danger (S624).
An omamori is normally returned to the shrine once its purpose has been served, or after about a year (S625).
Because omamori are sacred items, throwing them away with ordinary rubbish is discouraged (S625).
Shrines provide return boxes for used omamori, household ofuda and decorative arrows, and the returned items are burned in a sacred fire (S625).

Every sentence above is either the anchor quote itself or verbatim body text of the same opened page
(e.g. "Shinsatsu may be made of wood, paper, or metal and bear a written or printed inscription";
"charms against illness and misfortune ... traffic safety"; "As omamori are considered sacred items,
disposing of them in the trash is discouraged"; "Returned items are then burned in a sacred fire").

## Rejected (opened, not offered)

1. Claudia Marra, 2019, "Omamori — Shintō and Buddhist Lucky Charms", Journal of Nagasaki University of
   Foreign Studies 23 — https://nufs.repo.nii.ac.jp/record/773/files/3.%E3%82%AF%E3%83%A9%E3%82%A6%E3%83%87%E3%82%A3%E3%82%A2%E3%80%80%E3%83%9E%E3%83%A9.pdf
   The richest text found (issue by shrines/temples, yearly renewal, return and Setsubun burning, brocade
   cover hiding written words, printed function labels). It is unreachable to the acceptance fetch: the host
   answers 406 to the tool's User-Agent (it answers 200 to other UA strings), and there is no Wayback capture.
   Verbatim, rowcheck: `S625 LOCATE FAIL BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: https://nufs.repo.nii.ac.jp/record/773/files/3.%E3%82%AF%E3%83%A9%E3%82%A6%E3%83%87%E3%82%A3%E3%82%A2%E3%80%80%E3%83%9E%E3%83%A9.pdf HTTPError`
   Verbatim, urllib probe with the tool UA: `HTTPError 406 Not Acceptable text/html` (nginx).
   Note for the L1: this article is the best single source on omamori renewal; it would pass every leg if
   the host accepted the frozen UA. It does not, so it cannot be offered.
2. Encyclopedia of Shinto, "Kamidana" (id=9666) — https://d-museum.kokugakuin.ac.jp/eos/detail/?id=9666
   A vetted alternate that passes the instrument; not offered only because the two S-ids are spent and the
   MLIT row covers a different axis. Verbatim: `S625 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://d-museum.kokugakuin.ac.jp/eos/detail/?id=9666 | BOILER: root-clear https://d-museum.kokugakuin.ac.jp/; not a title, h1 or meta label | RELEVANCE: shared=['altar', 'amule', 'enshr', 'grand', 'shrin'] | TOPIC: quote_hits=2 function_words=5 page_hits=3 page_terms=3 need=1/2/3/2`
   Its quote: "it became customary throughout the country to construct special Ise altars (Daijingūdana) to
   enshrine an amulet (taima or ofuda) from the Grand Shrines (Jingū)"; capture
   https://web.archive.org/web/20260908163012id_/https://d-museum.kokugakuin.ac.jp/eos/detail/?id=9666.
3. Japan Tourism Agency (MLIT), "Ofuda and Omamori Talismans" R1-00454 —
   https://www.mlit.go.jp/tagengo-db/en/R1-00454.html (HTTP 200, 17506 bytes). Body is a short tourism sign;
   the one usable sentence has no CHARM-GUARD window. Verbatim:
   `S625 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC FAIL | LOCATE: ... TOPIC: quote_hits=0 function_words=6 page_hits=17 page_terms=18 need=1/2/3/2`
4. Kyoto Mikane Shrine, English FAQ — https://mikane-jinja.or.jp/en/faq-english/ (HTTP 200, 22251 bytes).
   Has the renewal sentence, but no CHARM-GUARD window in it. Verbatim:
   `S625 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC FAIL | LOCATE: https://mikane-jinja.or.jp/en/faq-english/ | BOILER: root-clear https://mikane-jinja.or.jp/; not a title, h1 or meta label | RELEVANCE: shared=['charm', 'divin', 'gener', 'ofuda', 'pract', 'prote'] | TOPIC: quote_hits=0 function_words=7 page_hits=6 page_terms=24 need=1/2/3/2`
   The companion page https://mikane-jinja.or.jp/en/omamori-omikuji/ (HTTP 200, 34133 bytes) carries an
   ofuda-protection sentence ("An ofuda slip, imbued with the power of the deities, is believed to ward off
   evil spirits") that also scores quote_hits=0 under the instrument's window arithmetic.
5. Nanzan Institute (JJRS) article page https://nirc.nanzan-u.ac.jp/journal/6/issue/197/article/1488 —
   `HTTP 503`, body: "The Nanzan Institute for Religion and Culture website is temporarily offline for
   essential system patches and security updates." Whole host returning 503 today.
6. British Museum object record https://www.britishmuseum.org/collection/object/A_1952-0407-1 — `403` (curl,
   browser UA), and the collection search — `403`. Smithsonian NMAA search https://asia.si.edu/search/?q=omamori
   — `403`. Art Institute of Chicago API — Cloudflare "Just a moment..." challenge (not passed).
7. Met Collection API v1.1 `q=omamori` — `{"total":0,"objectIDs":null}` (no omamori records). Cleveland
   open-access API `q=omamori` and `q=ofuda` — `{"info": {"total": 0, ...,}, "data": []}`.
8. V&A records O1755607 and O486960 (`api.vam.ac.uk/v2/objects/search?q=omamori`, record_count 4) — the
   omamori appears only in a Shichi-Go-San ensemble's brief description; no curatorial text about protection.
9. Ise Jingu English site (https://www.isejingu.or.jp/en/, and /en/pray/, /en/ritual/, /en/about/) and Meiji
   Jingu English site (https://www.meijijingu.or.jp/en/qa/, /en/visit/, /en/feelshinto/, /en/whattosee/) —
   opened, none carries a sentence about omamori/ofuda protection; only an "amulet office" mention.
10. E3S conference PDF (omamori, ICENIS 2020) — `403` to the tool UA. APJJF search — `403`. Hilltop Review
    landing page (https://scholarworks.wmich.edu/hilltopreview/vol7/iss2/19/) — HTTP 200 but its abstract is
    duplicated in `<meta name="description">`, so a quote from it is a page label for BOILER.

## Notes and remaining unknowns

- Hosts: d-museum.kokugakuin.ac.jp and www.mlit.go.jp; neither is in corpus/SOURCES.md
  (`grep -F` for both returned nothing) and neither is on the round's reserved list.
- S625 has no Wayback capture (`archive.org/wayback/available` returned `{"archived_snapshots": {}}`), so it
  is offered live only. The S624 capture was confirmed by the availability API and the CDX index
  (20260415164210, status 200) but web.archive.org was intermittently refusing connections at the end of the
  session; the live page answers 200, and LOCATE tries it first.
- The two rows are both "docs" (a university encyclopedia and a government heritage-interpretation database)
  and both concern Japanese practice; they were chosen for axis spread (object type and symbolism; yearly
  return and disposal) over a second Kokugakuin entry.
- Not covered by these two rows: commodification/souvenir trade, and the writing itself (what an inscription
  says). The EOS shinsatsu entry only states that inscriptions are written or printed.
- Installations: none (pypdf 5.4.0 ran ephemerally under `uv run --with`, as the instrument itself does).
