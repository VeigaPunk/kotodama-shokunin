# Kotodama round 63 — S701 source scribe

## Result
Partial evidence only; S701 is not ready to land. The live Britannica page and base locator support a social-use claim about adult Tuareg men's blue veil. The mandatory same-page Wayback capture was not obtained, so no valid registry row or Gate-ready source is produced. No product/source file was edited by this seat.

## Candidate artifacts

### Registry row
No admissible SOURCES.md row line was drafted because its required Wayback `id_` capture is unknown and unverified. Candidate row metadata is recorded in scratch `S701-row.md`: Britannica Editors, “Tuareg”, Encyclopaedia Britannica, last updated Oct. 15, 2026; live URL `https://www.britannica.com/topic/Tuareg`; kind `docs`, tier `B`; body-text quote below; mined, opened 2026-10-23, recheck 180d, used-by `corpus/knowledge/culture-material/headgear-head-covering-codes.md`. The exact live URL search in `corpus/SOURCES.md` returned no matches. Scope limit: this passage supports a Tuareg men's blue veil as social practice; it does not itself identify the garment as a tagelmust or document indigo dyeing.

### Entry bullet candidate (not landable until row admitted)
- Adult Tuareg men traditionally wore blue veils near women, strangers, and in-laws (S701)

The clause has at least five content words; “adult,” “traditionally,” “wore,” “blue,” “women,” “strangers,” and “in-laws” occur in quote order. The longest consecutive copied run is five words.

### Gate-line candidate (not Gate-ready; capture unverified)
- S701 | https://www.britannica.com/topic/Tuareg | 2026-10-23 | “Adult males traditionally wore a blue veil in the presence of women, strangers, and in-laws, but that practice began to be abandoned with urbanization.”

The quote is 24 normalized words and appears in the live article body paragraph, not a caption, alt text, or search snippet.

## Provenance and exact locator result

- Ordinary `read` of `https://www.britannica.com/topic/Tuareg` returned the page (method `native`); page metadata states last updated Oct. 15, 2026.
- Exact locator command:
  `cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && timeout 300 python3 -B reports/round-61/reopen-quote.py 'https://www.britannica.com/topic/Tuareg' 'Adult males traditionally wore a blue veil in the presence of women, strangers, and in-laws, but that practice began to be abandoned with urbanization.'`
  Full stdout: `LOCATED https://www.britannica.com/topic/Tuareg`; exit 0.
- The required CDX query through `read`, `https://web.archive.org/cdx/search/cdx?url=www.britannica.com%2Ftopic%2FTuareg&output=json&limit=-5&filter=statuscode%3A200`, failed with HTTP 429. `read` of `https://archive.org/wayback/available?url=www.britannica.com%2Ftopic%2FTuareg` also failed with HTTP 429.
- Ordinary urllib retry command:
  `python3 -c 'import urllib.request; u="https://web.archive.org/cdx/search/cdx?url=www.britannica.com%2Ftopic%2FTuareg&output=json&limit=-5&filter=statuscode%3A200"; r=urllib.request.urlopen(u, timeout=20); print("HTTP",r.status); print(r.read().decode())'`
  Outcome: `urllib.error.URLError: <urlopen error [Errno 111] Connection refused>` (underlying `ConnectionRefusedError: [Errno 111] Connection refused`); exit 1.
- No timestamp/capture ID was established; the capture locator was not run. No capture or capture quote verification is inferred.
- First-choice Smithsonian archival photo candidate, `https://www.si.edu/object/archives/components/sova-eepa-1973-001-ref28394`, failed ordinary `read` with HTTP 403. Its CDX `read` query failed HTTP 429. An ordinary curl attempt used:
  `curl -L -sS --max-time 30 -w '\nHTTP_STATUS=%{http_code}\n' 'https://web.archive.org/cdx/search/cdx?url=www.si.edu%2Fobject%2Farchives%2Fcomponents%2Fsova-eepa-1973-001-ref28394&output=json&limit=-5&filter=statuscode%3A200'`
  Full output: `curl: (7) Failed to connect to web.archive.org:443 after 178 ms: Could not connect to server` then `HTTP_STATUS=000`; exit 7. Search-result snippets were not treated as body-text evidence. With no accessible capture carrying a quote, this candidate was rejected.

## Gates, touched surfaces, and limits

- Live quote leg: met for Britannica (`LOCATED`, exit 0).
- Archive and valid-row legs: not met; no verified same-page `id_` URL or capture quote. S701 acceptance remains blocked. This row-scribe seat did not run `accept-c.py` or any counter.
- Lane files changed: only this requested report, `.ufo/waves/round-63/w1/ScribeRowS701.md`. No registry, entry, README, or product-code edits. Scratch evidence and all candidate artifacts are under `/fast/scratch/hyaku/kotodama-r63/kotodama-r63-w1-ScribeRowS701/`.
- Out of scope: O/reopen-row repair and review gate, lane integration, registry/entry/README edits, and counter scoring.
- Installs: none.

Scratch artifact paths:
- `/fast/scratch/hyaku/kotodama-r63/kotodama-r63-w1-ScribeRowS701/S701-row.md`
- `/fast/scratch/hyaku/kotodama-r63/kotodama-r63-w1-ScribeRowS701/S701-entry.md`
- `/fast/scratch/hyaku/kotodama-r63/kotodama-r63-w1-ScribeRowS701/S701-gate.md`
- `/fast/scratch/hyaku/kotodama-r63/kotodama-r63-w1-ScribeRowS701/locator-outputs.md`
- `/fast/scratch/hyaku/kotodama-r63/kotodama-r63-w1-ScribeRowS701/commands.txt`
- `/fast/scratch/hyaku/kotodama-r63/kotodama-r63-w1-ScribeRowS701/ScribeRowS701.md`
