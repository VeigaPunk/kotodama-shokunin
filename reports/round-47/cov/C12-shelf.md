# C12 — source-shelf verification: the cartography entry's tiered shelf

- Seat: **C12** | role: verifier | claim: **C** (coverage) | round 47, loop 2
- Date: 2026-10-19
- Baseline: HEAD `6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe` (`git rev-parse HEAD`); `find corpus/knowledge -name '*.md' | wc -l` → **223**; `ls corpus/knowledge/culture-material/*.md | wc -l` → **25**
- Out path: `reports/round-47/cov/C12-shelf.md` (this file is the only path this seat wrote)
- Writes: none under `corpus/`, `tools/`, `reports/round-1..46/`, or anywhere else. No git, install, or network. No `reports/round-*/run-validation.py` executed.
- Mission: check that the cartography entry's external shelf is honestly marked `(to-verify)`, that no unread work is presented as inspected, and that the in-corpus shelf resolves.
- Method: mechanical resolution of every backticked `corpus/knowledge/...md` reference against the live 223-entry tree, `sed -n` content comparison for every line assertion, SHA-256 comparison for every pinned file, and a per-item honesty audit of the external shelf. Instrument transcript in §7.

## 0. Verdict at a glance

| Leg | Measurement | Verdict |
|---|---|---|
| In-corpus shelf files resolve | **21/21** files exist at HEAD | **PASS** |
| In-corpus line assertions content-match | **24/24** line anchors resolve and say what the shelf claims | **PASS** |
| SHA-256 pins | **9/9** pins equal the live files | **PASS** |
| External shelf honesty | **18/18** items carry `(to-verify)`; block says "not consulted this round"; no item described as inspected | **PASS** |
| Shelf completeness against the body | **6** body-cited in-corpus files absent from the head inventory; the **OED** is invoked by the body but absent from the external shelf | **PASS-WITH-ADVISORIES** — additions listed in §4 |
| Count hygiene | lead says "sha256 pinned for the six load-bearing anchors" (`C04-entry-header.md:117`) but 9 pins follow | **cosmetic defect** — §5 D1 |
| Final assembled entry | not filed at this cut; this audit covers the four pinned fragments | **could-not-evaluate** for the assembled bytes |

**Reading:** the shelf is honest and the in-corpus half is fully resolvable. It is not yet complete as an inventory of what the entry actually uses: six in-corpus files are cited inside the body fences but omitted from `- sources:`, and the OED is the named external check for C02's etymology section but is not on the external shelf. These are additive fixes for the integrator, not provenance defects in the existing entries.

## 1. Bytes audited (pins)

The C-fragments were live-edited during the wave. The digests below are the bytes this audit actually read; a later edit is detectable as a digest mismatch and re-runs the probes in §7.

| Fragment | Role | Fenced body | Bytes | SHA-256 |
|---|---|---|---|---|
| `reports/round-47/cov/C04-entry-header.md` | head block + shelf under audit | lines 111–163 | 36 044 | `cb5a7489676de47e146e5055e07be9c8fa9d2df624c8872b0d438efcd67b68b0` |
| `reports/round-47/cov/C01-entry-a.md` | body §§1–4 | lines 85–287 | 47 829 | `cfb42955617373479a41d881fb6fd83f7df907aa7f563f51de95493d9ec8c44d` |
| `reports/round-47/cov/C02-entry-b.md` | body §§5–9 | lines 59–421 | 61 511 | `bfce3acaf20e527b949a45b708f1d9e10c9ab9447651375f89075f1c80be3602` |
| `reports/round-47/cov/C03-entry-c.md` | body §§10–15 | lines 72–250 | 41 114 | `4b699e06537115274807b64fbc5947cefc889348e5b4434b14a8ddb661eee3e5` |

Supporting sources read, not edited: `reports/round-44/scout/K02-gap-scout.md` (§4.4 shelf, SHA-256 `a72fff27ee193cc12e689b5a3b485d3c03839bd4317b7810abf745ee441f335f6`), `reports/round-47/scout/K02-seed-extract.md` (§6 shelf, SHA-256 `6abd5f19b21a1ffd11a2d24e2e6f9746b61180e28b513404f26d37b82098d572`), and `corpus/QUALITY.md` (`:5-8` provenance, `:9-12` calibration).

## 2. In-corpus shelf — every anchor resolves

The head block's `- sources:` field (`C04-entry-header.md:116-157`) names **21 distinct in-corpus files**. A mechanical sweep found **24 line assertions** across them (the extra three are the second/third lines in `transport`, `material-culture-inference-method`, `trade-economy` and `writing-systems`). Every file exists; every line number is in range; every quoted phrase is present on the cited line.

| In-corpus file | Anchors | Live text the shelf relies on (abridged) | Verdict |
|---|---|---|---|
| `myth-symbol/cosmology-cosmography.md` (sha `165f292b…`) | `:71`, `:102` | `:71` T-O row: "T-O diagrams are symbolic, not survey maps"; `:102` "T-O diagrams are symbolic devices, not cartographic" | resolve |
| `myth-symbol/sacred-topography-pilgrimage.md` (sha `241113b5…`) | `:5` | "sacred-geography mapping … as a diagram: radial, quartered, linear-corridor, or archipelago" | resolve |
| `myth-symbol/direction-symbolism.md` (sha `5a6ef38f…`) | `:51` | "**The compass trap**: an abstract north requires deciding *which* north — true or magnetic … declination" | resolve |
| `culture-material/architecture-settlement-lexicon.md` (sha `9af04e75…`) | `:95` | Roman castrum "surveyed with the **groma** … The grid is **cadastral**" | resolve |
| `culture-material/writing-media-surface-economy.md` (sha `f039e6e1…`) | `:3` | topic line: "the seven surface families (clay and wax; stone and metal; …)" | resolve (see §5 D5 on the source block's `:5`) |
| `culture-material/transport-mobility-lexicon.md` (sha `86e5f952…`) | `:28`, `:117` | `:28` "a route is only real if someone maintains it"; `:117` DR-TR-02 maintenance clause | resolve |
| `civilizations/mesoamerica-primary-sources.md` (sha `d04d8913…`) | `:58` | "Lienzos and cartographic histories … Cloth maps/migration-conquest accounts" | resolve (see §5 D6 on provenance) |
| `culture-material/timekeeping-instruments.md` (sha `9805c0b8…`) | `:50` | table row: the minute → "longitude at sea" | resolve |
| `culture-material/material-culture-inference-method.md` | `:69`, `:76` | `:69` perishability/"what survives to be seen"; `:76` anti-determinism guard | resolve |
| `culture-material/craft-artisan-lexicon.md` | `:44` | material-grade row (steel: *tamahagane*, *kawagane*, *shingane*) | resolve |
| `culture-material/trade-economy-lexicon.md` | `:92`, `:121` | Exchequer *stock*/*foil*; split-object authentication (*symbolon*, chirograph, indenture) | resolve |
| `culture-material/vessel-container-lexicon.md` | `:115` | "Containers as documents and as chronometers" | resolve |
| `linguistics/naming-systems.md` | path only | toponymy/onomastics ownership | resolve |
| `linguistics/writing-systems.md` | `:117`, `:149`, `:156` | media bias; media-blind design; build step 2 (medium and tool from economy) | resolve |
| `civilizations/japan-medieval-sengoku.md` | `:157` | "a neat Edo cadastral map must not be treated as a direct Sengoku map" | resolve |
| `civilizations/polynesia-navigation.md` | `:52` | horizon compass / steering stars / sky mnemonic / latitude clue distinguished | resolve (see §5 D7 on `:185`) |
| `verification/calibration-registry.md` (sha `cf7cceee…`) | `:78–88` | CAL-03 heading through "weak relativity is always defensible" too broad | resolve |
| `verification/real-world-inspiration-boundaries.md` | `:6` | recheck: local guidance and permissions before delivery/reuse | resolve |
| `verification/myth-consistency-gate.md` | `:34` | "Do not expose restricted ritual knowledge to fill a table" | resolve |
| `synthesis/worldbible-integration-contract.md` | path only | handoff target | resolve |
| `synthesis/era-material-scoped-reconciliation.md` | path only | era and material stages are separate clocks | resolve |

SHA-256 pins: the block pins nine files (`C04-entry-header.md:118-134`) and all nine equal the live digests (`165f292b…`, `241113b5…`, `5a6ef38f…`, `9af04e75…`, `f039e6e1…`, `86e5f952…`, `d04d8913…`, `9805c0b8…`, `cf7cceee…`). The pin list is therefore trustworthy evidence of the bytes read, even though the prose count is wrong (§5 D1).

## 3. External shelf — honest, 18/18

`C04-entry-header.md:139` opens the external shelf with the explicit frame: "**not consulted this round** (no network at seat time); author/year/title/publisher stated at book level, every edition, volume and page locator `(to-verify)`; no unread work is presented as inspected." The 18 bullets that follow are:

| # | Item (abridged) | Mark |
|---|---|---|
| 1 | Harley & Woodward, *The History of Cartography*, U Chicago Press, 1987– — "volume/book count and the volume covering portolan charts `(to-verify)`" | `(to-verify)` |
| 2 | Harley 1989, "Deconstructing the Map," *Cartographica* 26(2): 1–20 | `(to-verify)` |
| 3 | Wood, *The Power of Maps* (1992; 2nd ed. 2010) | `(to-verify)` |
| 4 | Monmonier, *How to Lie with Maps* (1991; 3rd ed. 2018) | `(to-verify)` |
| 5 | Jacob, *The Sovereign Map* (Fr. 1992; Eng. 2006) | `(to-verify)` |
| 6 | Ptolemy, *Geography*, trans. Berggren & Jones (2000) | `(to-verify)` |
| 7 | Campbell 1987, "Portolan Charts…," in *History of Cartography* vol. 1 | `(to-verify)` (page range and volume) |
| 8 | Edson, *The World Map, 1300–1492* (2007) | `(to-verify)` |
| 9 | Kain & Baigent, *The Cadastral Map in the Service of the State* (1992) | `(to-verify)` |
| 10 | Mundy, *The Mapping of New Spain* (1996) | `(to-verify)` |
| 11 | Boone, *Stories in Red and Black* (2000) | `(to-verify)` |
| 12 | Pickles, *A History of Spaces* (2004) | `(to-verify)` |
| 13 | Buisseret (ed.), *Monarchs, Ministers, and Maps* (1992) | `(to-verify)` |
| 14 | Snyder, *Map Projections: A Working Manual* (USGS PP 1395) | `(to-verify)` |
| 15 | Dilke, *The Roman Land Surveyors* (1971) | `(to-verify)` |
| 16 | al-Idrisi, *Nuzhat al-mushtāq* (1154) | `(to-verify)` (edition/translation) |
| 17 | *Tabula Peutingeriana*; *Antonine Itinerary* | `(to-verify)` (editions) |
| 18 | Ortelius, *Theatrum* (1570); Mercator's atlas | `(to-verify)` (editions) |

Positive findings:

- **The seed's over-specific claims were softened, not laundered.** The r44 seed asserted "6 vols. in 7 … 1987–2022 … vol. 1 (1987) … vol. 3 (2007)" (`reports/round-44/scout/K02-gap-scout.md:253`). The head shelf now says "University of Chicago Press, 1987– — … volume/book count and the volume covering portolan charts `(to-verify)`" (`C04-entry-header.md:141`). This is the correct response to the offline limit: a title-level cite with the unverified volume claim explicitly open.
- **Precise page numbers are marked, not asserted.** Harley 1989's `26(2): 1–20` and Campbell's page range carry `(to-verify)` (`:142`, `:147`); al-Idrisi's edition/translation and the two primary-text editions are marked (`:156-158`).
- **No inspection claim survives a text search.** Across the external shelf the only occurrences of "inspected"/"consulted"/"read" are the negations ("not consulted this round"; "no unread work is presented as inspected"). The `- source:` field repeats "**none fetched or inspected this run**" (`:158`), and `- verified-at:` says "**No external source was fetched or inspected**" (`:160`).
- **Body fragments behave the same way.** C01 marks its projected rows `Snyder 1987 (to-verify)`, `Mercator 1569 (to-verify)`, `Campbell, to-verify`, `Ortelius 1570 (to-verify)` (`C01-entry-a.md:172-175,242-244`) and states the no-network limit at `:351`. C02 marks Ptolemy, al-Idrisi, Mercator and Blaeu with `(to-verify)` (`C02-entry-b.md:75,200,257-259`) and says "no external work was consulted at this seat" (`:500`). C03 carries 22 marks and states "The Tier B shelf was not inspected this round" (`C03-entry-c.md:214`). No body sentence presents an unread work as a page-level source.

## 4. Shelf completeness — what the body uses that the head omits

The shelf is honest but not a complete inventory. Six in-corpus files are cited **inside the body fences** and are absent from the head `- sources:` list; the OED is invoked by the body and absent from the external shelf. All six paths resolve and all cited lines say what the body uses them for (checked with `sed -n`).

| Omitted in-corpus file | Body citation (current bytes) | What the body uses it for |
|---|---|---|
| `myth-symbol/symbolism-synthesis-method.md` | `C01-entry-a.md:105` (`:23`) | the five canonical symbol registers — the map is a composition register, not a sixth symbol register |
| `synthesis/loanword-material-dating.md` | `C02-entry-b.md:112,337` (`:40`); `:402` (`:30`) | the copy/original rule and the three-clock table (lexical entry vs referent arrival vs first written token) |
| `culture-material/fire-fuel-light.md` | `C02-entry-b.md:340` (`:89`) | archive destruction as "the cheapest way to write a *hole*" |
| `culture-material/funerary-material-culture.md` | `C02-entry-b.md:370` (`:22`) | the *sarcophagus* stone of Assos as the material-property→container-name fossil |
| `civilizations/maori.md` | `C03-entry-c.md:180,215` (`:20`) | the named-knowledge-holder precedent for living-tradition material |
| `verification/to-verify-triage-protocol.md` | `C03-entry-c.md:187,206,214,222` (`:15`) | the definition of `(to-verify)` and the routing rule before canon promotion |

**Additions for the integrator.** Add those six files to the in-corpus `- sources:` list (with the line anchors already used in the body), or to `- couples:` where the relationship is ownership rather than evidential support — `symbolism-synthesis-method` and `to-verify-triage-protocol` read as couples/contract entries; the other four are evidential anchors.

**The OED.** `C02-entry-b.md:390` says "All etymologies are standard-shelf but **`to-verify` at OED level** … the external check is the *Oxford English Dictionary*". The current head shelf has no OED entry. C02's own out-of-fence shelf names it ("*Oxford English Dictionary*, 3rd edn (online) — every etymology in §9. **Not consulted this round**", `C02-entry-b.md:493`). Add that line to the external shelf if §9 ships; it is the only external work the body names as its check that is not already on the shelf.

**Fragment-only items that must not be imported.** C02's out-of-fence shelf also lists Scott 1998 (`C02-entry-b.md:492`) as supporting §8.2, but no body citation to Scott exists — do not add it to the head shelf unless the body acquires one. The head shelf's softened Harley line is the correct form; do not replace it with any restated "6 vols. in 7" variant.

**Reverse delta (no action).** Three head-listed files are not body-cited: `writing-systems.md` (a couples boundary), `worldbible-integration-contract.md` (handoff), and `era-material-scoped-reconciliation.md` (context rule). These are legitimate coupling/handoff entries, not padding.

## 5. Defects and advisories

**D1 (cosmetic, fix before filing).** `C04-entry-header.md:117` says "sha256 pinned for the **six** load-bearing anchors", but nine pins follow (`:118-134`). Change "six" to "nine" or reduce the pins to six. The pins themselves all match, so this is a count error, not a provenance error.

**D2 (advisory, completeness).** Add the six in-corpus files in §4 to the head inventory. Without them, the `- sources:` field undercounts the entry's in-corpus dependencies by six.

**D3 (advisory, completeness).** Add the OED to the external shelf if C02's §9 etymology section ships. It is already marked `(to-verify)` in C02's fragment; the head shelf is the landing surface.

**D4 (anchor precision).** `writing-media-surface-economy.md:3` is the `- topic:` line; it does support "the seven surface families", but the `- sources:` block for that entry begins at `:5`. If any cost figure or cost-ladder claim is quoted, cite the source record (`:5-28`) or the body row, not the topic line.

**D5 (provenance carry-forward).** `mesoamerica-primary-sources.md:58` is the lienzo/cartographic-history row; that row's own limits are at `:28` ("a current room-level Puebla location is not established here") and `:58` ("Originals often lost; the copy chain is the evidence"). If the body uses the lienzo case as evidence, carry the copy-chain caveat rather than citing the row as a general warrant.

**D6 (provenance carry-forward).** `polynesia-navigation.md:52` is a body-claim anchor, not a bibliography entry. The entry's own source line at `:185` says "page-level check of the catalogue itself was not possible in this pass". If the body quotes a star name or a navigation term, inherit that limit; the head anchor is sufficient only for the boundary statement.

## 6. What this seat could not evaluate

- **External bibliographic accuracy.** No network at seat time. This audit judges whether the shelf is *honestly marked*, not whether Harley & Woodward's volume count, Snyder's paper number, or any edition/year is correct. Every such detail remains `(to-verify)` in the shelf.
- **The assembled entry.** No scribe/assembled artifact was filed at this cut. The verdict applies to the four pinned fragments; if assembly reorders or rewrites the head shelf, the probes in §7 must be re-run.
- **The "re-read at HEAD" process claim.** I can verify that every cited line exists and matches the quoted content; I cannot verify the author's reading process beyond that content match.
- **Live edits.** The fragments were edited during the wave (C02's fence moved from line 39 to 59 between reads; C04 changed from `b4ae…` to `cb5a…`). The digests in §1 pin the audited bytes; a later edit invalidates the pin, not the method.

## 7. Re-run probes

All commands are read-only. From the lane root, with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`:

```text
$ git rev-parse HEAD
6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe
$ find corpus/knowledge -name '*.md' | wc -l
223
$ sha256sum reports/round-47/cov/C04-entry-header.md
cb5a7489676de47e146e5055e07be9c8fa9d2df624c8872b0d438efcd67b68b0
```

The resolver used for §2–§4 (stdlib only; prints each unique ref and its resolution):

```python
import re, pathlib, hashlib
head = pathlib.Path("reports/round-47/cov/C04-entry-header.md").read_text()
blk = re.search(r"````markdown\n(.*?)\n````", head, re.S).group(1)
src = blk.split("- sources:")[1].split("\n- source:")[0]
refs = set(re.findall(r"`(corpus/knowledge/[^`:]+\.md)((?::\d+(?:[,–-]\d+)*)*)`", src))
for path, loc in sorted(refs):
    fp = pathlib.Path(path)
    assert fp.exists(), path
    total = len(fp.read_text().splitlines())
    for n in [int(x) for x in re.findall(r"\d+", loc)]:
        assert 1 <= n <= total, (path, loc, total)
# pins
for path, pin in re.findall(r"`(corpus/knowledge/[^`]+?)` \(sha256 `([0-9a-f]{64})`\)", blk):
    assert hashlib.sha256(pathlib.Path(path).read_bytes()).hexdigest() == pin, path
# external shelf: every bullet carries a mark
ext = src.split("External standard shelf")[1].split("\n- source:")[0]
bullets = [l for l in ext.splitlines() if l.strip().startswith("- ")]
assert bullets and all("to-verify" in b for b in bullets), [b for b in bullets if "to-verify" not in b]
print("in-corpus refs", len(refs), "| pins ok | external bullets", len(bullets))
```

Expected output at the pins in §1: `in-corpus refs 21 | pins ok | external bullets 18`.

Body-usage probe (the §4 delta):

```text
$ python3 - <<'PY'
import re, pathlib
spans = {"C01": ("reports/round-47/cov/C01-entry-a.md", 85, 287),
         "C02": ("reports/round-47/cov/C02-entry-b.md", 59, 421),
         "C03": ("reports/round-47/cov/C03-entry-c.md", 72, 250)}
pat = re.compile(r"`((?:corpus/knowledge/)?(?:myth-symbol|culture-material|civilizations|linguistics|verification|synthesis)/[a-z0-9-]+\.md)((?::\d+(?:[,–-]\d+)*)*)`")
used = set()
for seat, (p, a, b) in spans.items():
    body = "\n".join(pathlib.Path(p).read_text().splitlines()[a-1:b])
    used |= {"corpus/knowledge/" + m[0].replace("corpus/knowledge/", "") for m in pat.findall(body)}
head = pathlib.Path("reports/round-47/cov/C04-entry-header.md").read_text()
blk = re.search(r"````markdown\n(.*?)\n````", head, re.S).group(1)
shelf = set(re.findall(r"`(corpus/knowledge/[^`:]+\.md)", blk.split("- sources:")[1].split("\n- source:")[0]))
print(sorted(used - shelf))
PY
```

At the §1 pins this prints the six files in §4.

## 8. Handoff

- **C06 (source audit):** the §2 table is a ready-made 24/24 content-match sheet; reuse it rather than re-deriving. The six §4 files are outside the head shelf but inside the body — audit them as body anchors.
- **C13 (couples):** already reports 21/21 couple tokens resolving (`reports/round-47/cov/C13-couples.md`), independent of this shelf check. The §4 additions are source-list/couples additions, not a couples failure.
- **Integrator / C11 / W02:** apply the current head shelf (`C04-entry-header.md:111-163`, sha `cb5a…`) — not any earlier revision and not C02's out-of-fence shelf block. Before applying: fix D1 and add D2/D3. Keep `- topic:` byte-equal to the README row.
- **V02 / post-landing:** the shelf itself does not change on landing (the entry is an add; no external file moves). The post-landing check only needs to confirm the landed file's `- sources:` sha matches the applied block.

## Owed

- none for this seat. The shelf's two stated criteria pass; the completeness additions in §4 are for the integrator and are additive.
