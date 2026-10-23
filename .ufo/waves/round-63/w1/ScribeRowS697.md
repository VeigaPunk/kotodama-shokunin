# Round 63 S697 source finding

**Axis:** coverage (claim C), S697 only. **Status:** candidate artifacts drafted; archive-locator gate did not pass, so this source is **not cleared for admission**.

## Draft artifacts

Candidate registry row (not yet admissible):

| S697 | Phrygian cap, Encyclopaedia Britannica (Britannica Editors), updated September 7, 2026 - https://www.britannica.com/art/Phrygian-cap ; capture https://web.archive.org/web/20261017073405id_/https://www.britannica.com/art/Phrygian-cap | docs | B | Britannica Editors' account of the Phrygian cap's material, shape, Anatolian origin, and ancient Greek representation; not universal headwear evidence | Opening body paragraph: "soft felt or wool conical headdress fitting closely around the head and characterized by a pointed crown that curls forward" | describes a close-fitting felt-or-wool headdress with a forward-curling point and places the form in ancient Anatolia and Greek art | mined | 2026-10-23 | 180d | corpus/knowledge/culture-material/headgear-head-covering-codes.md |

Entry bullet draft:

- Phrygian caps use felt or wool and a pointed crown that curls forward, echoing their Anatolian origin and Greek artistic representation. (S697)

Gate line draft:

- S697 | https://www.britannica.com/art/Phrygian-cap | 2026-10-23 | "soft felt or wool conical headdress fitting closely around the head and characterized by a pointed crown that curls forward"

The entry clause has more than five content words and shares quote terms in order (felt, wool, pointed, crown, curls, forward); the longest verbatim run is five words. The anchor quote is 20 normalized words.

## Provenance and gate evidence

- Opened the source through ordinary `read`: `https://www.britannica.com/topic/Phrygian-cap`, canonicalized to `https://www.britannica.com/art/Phrygian-cap`. The page names Britannica Editors and says it was last updated Sep. 7, 2026. The selected quote is in the opening **body paragraph**, not a caption, alt text, or title.
- Registry reuse check: `functions.grep` against `corpus/SOURCES.md`, pattern `britannica\.com/art/Phrygian-cap|britannica\.com/topic/Phrygian-cap` → `No matches found`.
- CDX query used: `http://web.archive.org/cdx/search/cdx?url=https%3A%2F%2Fwww.britannica.com%2Fart%2FPhrygian-cap&output=json&limit=-5&filter=statuscode%3A200&fl=timestamp%2Coriginal%2Cstatuscode`. It returned five status-200 captures with the exact original `https://www.britannica.com/art/Phrygian-cap`: 20250921083038, 20251006054354, 20251016150700, 20260327023549, and 20261017073405. The selected id_ capture is `https://web.archive.org/web/20261017073405id_/https://www.britannica.com/art/Phrygian-cap`.
- Ordinary `read` of the selected id_ capture returned the same quote in its opening body paragraph. However, the required base locator could not fetch the archive URL, so archive confirmation by the required locator remains unmet.

Base locator runs (executed with `functions.bash` cwd `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, equivalent to the assignment's lane-root `cd`):

1. Command: `timeout 300 python3 -B reports/round-61/reopen-quote.py 'https://www.britannica.com/art/Phrygian-cap' 'soft felt or wool conical headdress fitting closely around the head and characterized by a pointed crown that curls forward'`
   - stdout: `LOCATED https://www.britannica.com/art/Phrygian-cap`
   - exit: 0
2. Command with selected archive id_ URL and the same quote:
   - stdout: `NOT_LOCATED https://web.archive.org/web/20261017073405id_/https://www.britannica.com/art/Phrygian-cap URLError`
   - exit: 1
3. Alternate exact-original archive capture `https://web.archive.org/web/20260327023549id_/https://www.britannica.com/art/Phrygian-cap`, same locator and quote:
   - stdout: `NOT_LOCATED https://web.archive.org/web/20260327023549id_/https://www.britannica.com/art/Phrygian-cap URLError`
   - exit: 1
4. HTTP transport variant of the selected capture, same locator and quote:
   - stdout: `NOT_LOCATED http://web.archive.org/web/20261017073405id_/https://www.britannica.com/art/Phrygian-cap HTTPError`
   - exit: 1

The failed locator outputs are fetch errors, not evidence that the quote is absent; nevertheless, the assignment requires `LOCATED` on both URLs, and that condition was not met. The candidate row is therefore not a complete/pass artifact. HTTPS CDX/timemap reads returned HTTP 429; a plain curl CDX attempt returned `curl: (7) Failed to connect to web.archive.org:443 after 177 ms: Could not connect to server`, `HTTP 000`, exit 7. The ordinary HTTP CDX query above succeeded and identified the exact HTTPS original URL.

## Surfaces and bounds

- Written surfaces: this report and five scratch artifacts only. No product source, registry, entry, counter, or other lane file was modified. No counter or held `tools/reopen-row.py` was run. No installs/updates were made.
- Out of scope: claim O, remaining C rows, entry assembly, counter execution, independent review, and broader headgear claims beyond the material/form/origin/representation stated by this page.

## Artifact paths

Scratch directory: `/fast/scratch/hyaku/kotodama-r63/kotodama-r63-w1-ScribeRowS697/`

- `S697.registry-row.md`
- `S697.entry-line.md`
- `S697.gate-line.md`
- `S697.locator-evidence.md`
- `S697.status.md`

Lane report: `.ufo/waves/round-63/w1/ScribeRowS697.md`
