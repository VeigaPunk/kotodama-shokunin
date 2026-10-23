# ReviewCarry151to159 — round-56 carry rows S151, S159 (superseding rows S573, S574)

Seat: `KotodamaR58A2.ReviewCarry151to159` (reviewer, leaf, no delegation). Session 2026-10-22 -03 / 2026-10-23 UTC. Sources re-opened by ordinary means this session: plain `curl` (deposit page, live UNESCO URL, Wayback capture), `soffice --headless` for the .doc, the frozen locator `reports/round-58/reopen-quote.py`. Downloads: `/fast/scratch/hyaku/kotodama-r58/ReviewCarry151to159/` (`s151.html` 29,629 B; `s159.doc` 236,544 B; `s159.txt` 57,808 B converted). No challenge, captcha or paywall met. Drafts re-verified from `.ufo/waves/round-55/build/ReviewCells135to159.md` (rows NEW-ReviewCells135to159-4, -5) against the live sources and the current entry. Recommendation only — I wrote no file but this report.

## Verdicts

### S151 — AGREE with the round-53 finding (teaches over-read)

Served page (HTTP 200, text/html): Details → Description reads verbatim "David Yetman and Mark Sicoli elicit spoken and whistled Chinantec from children in San Pedro Sochiápam" (HTML lines 217, 238, 280); Persistent Identifier `https://hdl.handle.net/1839/00-0000-0000-0016-B509-0` on the page (line 233); item "CAM20459" in collection "Sicoli" (line 314). Zero hits on the page for "of the village", "transmit", "learn", "young", "Oaxaca": the taught claims "made with children of the village — the register is transmitted young" (`SOURCES.md:180`) are not on the page. Locator line:

```
LOCATED https://archive.mpi.nl/tla/islandora/object/lat:1839_00_0000_0000_0016_B509_0
```

(run: `timeout 300 python3 -B reports/round-58/reopen-quote.py 'https://archive.mpi.nl/tla/islandora/object/lat:1839_00_0000_0000_0016_B509_0' 'David Yetman and Mark Sicoli elicit spoken and whistled Chinantec from children in San Pedro Sochiápam'`, exit 0). **Fix:** superseding row S573 below; drop "of the village" and "transmitted young"; keep the entry's "(to-verify)" hedge on learning age.

### S159 — AGREE with the round-55 finding (anchor names a heading the file lacks), plus one correction the draft could not see

Served form (HTTP 200, application/msword, 17 pp., 8,824 words): the file has **no** "Brief textual description of the nominated element" heading (0 hits); its lettered fields are A–F with §D "D. Geographical location and range of the element" (`s159.txt:32`); §C "Name of the communities, groups or, if applicable, individuals concerned" (`:27`, with "nearly 10.000 people … able to speak and/or understand whistled language", `:30`); §1 "Identification and definition of the element" (`:77`; terrain and remote houses `:93`; "warning and SOS or calling for help, such as "There is a forest fire!"" `:94`); shepherd remainder "limited to a few words spoken by shepherds" in §D (`:44`); §2 "Need for urgent safeguarding" (`:101`) with "One of the most important threats to this element is the increase in the use of mobile phones. … Today, however, it is about to lose its communication function." (`:107`). The draft's section map is exact; the old anchor's §D name is not.

**New today:** the live URL now serves the nomination form itself — HTTP 200, application/msword, 236,544 B, sha256 `85b777c910a2c003d892b330ca9d41084e799105ed5cefef6a1d1a694c59b2d7`, byte-identical to Wayback capture 20221007161757 (both files hash equal). The route note "live URL serves an unrelated page" (true in rounds 52–55) is stale as of 2026-10-23, so S574 cites the live URL directly instead of the draft's Wayback routing — a strict improvement; the anchor-heading defect stands regardless. Locator line (live URL):

```
LOCATED https://ich.unesco.org/doc/src/36234-EN.doc
```

(run: `timeout 300 python3 -B reports/round-58/reopen-quote.py 'https://ich.unesco.org/doc/src/36234-EN.doc' 'The steep mountains and rugged topography of the region have resulted in houses being built that are remote and inaccessible from one another'`, exit 0; the sentence is verbatim at `s159.txt:93`.) For the record, the same quote through the Wayback capture under the instrument: `NOT_LOCATED https://web.archive.org/web/20221007161757/https://ich.unesco.org/doc/src/36234-EN.doc HTTPError` (urllib fetch error; `curl -sSL` fetched the same capture fine) — moot with the live URL locating.

**Fix:** superseding row S574 below.

## Final rows (append to `corpus/SOURCES.md`; both superseded rows are cited in the entry, so status `mined` with the same used-by)

```
| S573 | The Language Archive, Max Planck Institute for Psycholinguistics — deposit CAM20459, "David Yetman and Mark Sicoli elicit spoken and whistled Chinantec from children in San Pedro Sochiápam" — https://archive.mpi.nl/tla/islandora/object/lat:1839_00_0000_0000_0016_B509_0 | dataset | A | the existence and content of a Chinantec whistled-speech deposit from San Pedro Sochiápam, recorded in spoken and whistled Chinantec elicited from children there; not a linguistic analysis, and no acquisition-age statement | deposit title and Details Description: "David Yetman and Mark Sicoli elicit spoken and whistled Chinantec from children in San Pedro Sochiápam"; persistent identifier https://hdl.handle.net/1839/00-0000-0000-0016-B509-0 | supersedes S151 — scope and teaches only: S151's "children of the village" and "the register is transmitted young" are not on the page, which says "from children in San Pedro Sochiápam" and carries no acquisition or transmission-age claim; a Chinantec whistled-speech deposit from San Pedro Sochiápam exists, recorded in spoken and whistled Chinantec elicited from children there | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md |
```

```
| S574 | UNESCO nomination form 00658, "Whistled language" (Türkiye) (English), https://ich.unesco.org/doc/src/36234-EN.doc (live URL serves the form itself, re-opened 2026-10-23, sha256 85b777c9…, byte-identical to Wayback capture 20221007161757; rounds 52–55 read the capture because the live URL then served an unrelated page) | docs | A | Primary State Party nomination document for element 00658: terrain and settlement pattern, use cases, bearers, decline factors | §1 terrain paragraph: "The steep mountains and rugged topography of the region have resulted in houses being built that are remote and inaccessible from one another"; §1 warning and SOS calls ("There is a forest fire!"); §C "Name of the communities, groups or, if applicable, individuals concerned" (nearly 10.000 people able to speak and/or understand); §D "Geographical location and range of the element" (shepherd remainder); §2 "Need for urgent safeguarding" (mobile phones, loss of function) | supersedes S159 — anchor and route note only: S159's anchor names a "§D Brief textual description of the nominated element" heading the file does not have; the file's sections are §1 "Identification and definition of the element" (terrain, remote houses, warning and SOS calls), §C community box (nearly 10.000 people able to speak and/or understand), §D "Geographical location and range of the element" (use reduced to "a few words spoken by shepherds") and §2 "Need for urgent safeguarding" (mobile phones one of the most important threats, the language about to lose its communication function); the live URL serves the form again, so the read no longer needs the Wayback route | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md |
```

Registry is append-only; ids S573/S574 verified unused (`grep 'S57[0-9]' corpus/SOURCES.md` → no matches). Precedent cells mirrored from S185→S145 (`SOURCES.md:214,174`). Re-pointing S151→S573 and S159→S574 re-uses URLs across rows by design; the census's W04 duplicate-URL warnings may fire as they did for S482/S483/S485/S490 — expected.

## Exact citation re-points (`corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md`, all six sites, grep-verified)

1. `:79` `San Pedro Sochiápam, Oaxaca (S151; S155)` -> `San Pedro Sochiápam, Oaxaca (S573; S155)`
2. `:79` `an archive deposit records spoken and whistled Chinantec elicited from children in San Pedro Sochiápam (S151)` -> `an archive deposit records spoken and whistled Chinantec elicited from children in San Pedro Sochiápam (S573)`
3. `:105` `whose houses are "remote and inaccessible from one another" (S159)` -> `whose houses are "remote and inaccessible from one another" (S574)`
4. `:106` `Turkish whistling now survives in "a few words spoken by shepherds" (S159)` -> `Turkish whistling now survives in "a few words spoken by shepherds" (S574)`
5. `:109` `for example "There is a forest fire!" (S159)` -> `for example "There is a forest fire!" (S574)`
6. `:113` `is "about to lose its communication function" (S159)` -> `is "about to lose its communication function" (S574)`

Every entry sentence these lines carry was re-checked against the served texts and is supported (see Verdicts; `s159.txt:30,32,44,93,94,107`; `s151.html:238`); line 79's "the age at which the register is learned is (to-verify)" stays and is now honest under S573.

## Landing edits on the superseded rows (L1, one line each — append-only cells touched: teaches, status, used-by)

- `SOURCES.md:180` S151 — append to teaches: ` Superseded 2026-10-23 (round 58): retired in favour of S573, which drops the unsupported "of the village" and "transmitted young"; the entry now cites S573.`; status `mined` -> `rejected`; used-by -> `—`.
- `SOURCES.md:188` S159 — append to teaches: ` Superseded 2026-10-23 (round 58): retired in favour of S574, which names the file's real sections and the live-URL route; the entry now cites S574.`; status `mined` -> `rejected`; used-by -> `—`.

## Residual risk and verification gaps

- The S159 anchor's first quoted span locates through the instrument only because the tool's plain-text path happens to surface the .doc's ASCII runs; a future instrument change to `to_text` could unlocate it. Mitigation already in the row: the live URL is the ordinary copy, and the quote is verbatim in the soffice-converted text (`s159.txt:93`).
- The round-55 draft's S574 locator named "§1 'Identification and definition of the element'" as its first quoted span (5 words, below the instrument's 8-word floor); my final row re-orders the anchor so the first quoted span is the 23-word verbatim sentence. No content change otherwise.
- No LSP server applies (markdown corpus, no code symbols); caller checks were text greps on the entry and registry, per the draft's stated method.
- Entry :106's "working their farms" stays with S162 (fixed in round 53); not re-adjudicated here. Old-row retirement cells and the entry re-points are L1 landings; I ran none of them.
- No installs this run (tooling directive: prefer none). Used: curl, file, sha256sum, soffice, python3 — all already present.
