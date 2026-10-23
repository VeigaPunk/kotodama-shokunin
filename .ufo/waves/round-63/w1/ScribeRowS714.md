# ScribeRowS714 — S714 source report

## Outcome
Prepared candidate artifacts for S714 from an Imperial War Museums object record. The archived page extraction contains an appropriate body-text quote, and the page is a primary institutional catalog record for one object. However, the required base locator did not confirm the quote on either live or capture URL; the live URL returned an HTTP error and the capture URL returned a URL error on two attempts. Only one status-200 Wayback capture was observed, not several. **S714 is therefore a candidate, not a locator-cleared row.** Do not report the C LIVE leg or ACCEPT-C-63 as passed from this work.

The ordinary live page failure plus archived text is recorded as met-not-passed evidence per the prompt's access rule, but the mandated locator results remain unresolved. The capture's extracted text is not a substitute for successful locator confirmation.

## Candidate artifacts

### Registry row (candidate; not cleared)
| S714 | Ushanka, Imperial War Museums (page date not shown; catalogue no. UNI 16402) - https://www.iwm.org.uk/collections/item/object/30155099 ; capture https://web.archive.org/web/20260819072847id_/https://www.iwm.org.uk/collections/item/object/30155099 | docs | A | physical description of one IWM-catalogued Soviet warrant officers' ushanka, not universal construction or civilian use | Physical description, "padded grey woollen crown with blue-dyed (synthetic?) fur ear flaps tied up to the crown" | IWM's record describes the padded crown and tied fur ear flaps of this one Soviet military specimen; its material note is explicitly uncertain and it is not a universal definition. | mined | 2026-10-23 | 180d | corpus/knowledge/culture-material/headgear-head-covering-codes.md |

Tier A is narrowly scoped to the museum's own catalogue record for its own collection object. The IWM page does not show a publication date; the archived record lists catalogue number UNI 16402. The exact live URL was not found in SOURCES.md.

### Entry bullet (candidate)
- An IWM specimen has a padded crown and fur ear flaps tied up. (S714)

The clause has five qualifying content words (`specimen`, `padded`, `crown`, `flaps`, `tied`); `padded`, `crown`, `flaps`, and `tied` appear in the quote in order. The longest consecutive copied run is five words (`fur ear flaps tied up`), within the 12-word maximum.

### Gate line (candidate)
- S714 | https://www.iwm.org.uk/collections/item/object/30155099 | 2026-10-23 | "padded grey woollen crown with blue-dyed (synthetic?) fur ear flaps tied up to the crown"

## Provenance and locator evidence

The direct `read` of `https://www.iwm.org.uk/collections/item/object/30155099` failed to fetch the page (HTTP 403). A `read` of `https://web.archive.org/web/20260819072847id_/https://www.iwm.org.uk/collections/item/object/30155099` returned extracted page text. Under `## Description` / `### Physical description`, the archived page states: `Ushanka headwear comprising a padded grey woollen crown with blue-dyed (synthetic?) fur ear flaps tied up to the crown and front flap, complete with metal Soviet cap badge on front flap, the headwear is stamped on the inside with a diamond and labelling in cyrrilic and date '89' and a large number 56 alongside.` The proposed anchor is contiguous body text in that paragraph, not a caption, alt text, title, or search result.

CDX request `https://web.archive.org/cdx/search/cdx?url=https%3A%2F%2Fwww.iwm.org.uk%2Fcollections%2Fitem%2Fobject%2F30155099&output=json&limit=-5&filter=statuscode%3A200` returned one status-200 capture, timestamp `20260819072847`, with original URL exactly `https://www.iwm.org.uk/collections/item/object/30155099`. A second CDX request without `limit=-5` failed HTTP 429. Only one capture was observed, fewer than the requested several.

Exact locator command and result for live URL:

```text
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && timeout 300 python3 -B reports/round-61/reopen-quote.py 'https://www.iwm.org.uk/collections/item/object/30155099' 'padded grey woollen crown with blue-dyed (synthetic?) fur ear flaps tied up to the crown'
stdout: NOT_LOCATED https://www.iwm.org.uk/collections/item/object/30155099 HTTPError
exit=1
```

Exact locator command and result for capture URL:

```text
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && timeout 300 python3 -B reports/round-61/reopen-quote.py 'https://web.archive.org/web/20260819072847id_/https://www.iwm.org.uk/collections/item/object/30155099' 'padded grey woollen crown with blue-dyed (synthetic?) fur ear flaps tied up to the crown'
stdout: NOT_LOCATED https://web.archive.org/web/20260819072847id_/https://www.iwm.org.uk/collections/item/object/30155099 URLError
exit=1
```

An exact retry of the capture locator command produced the same stdout and exit 1. No result claims the quote was absent; the locator could not retrieve the URLs.

Rejected source checks: `read` of `https://www.britannica.com/topic/ushanka` failed HTTP 404; `read` of `https://www.merriam-webster.com/dictionary/ushanka` failed HTTP 404. Neither is used. Exact URL search for the proposed IWM live URL in `/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md` returned no matches.

## Gates and limits

Read the frozen claims and both counter docstrings. Claim C has frozen legs FILE, ROWS, ONEID, RESTATE, LINK, APPEND, NOHARM, SWEEP, LIVE; its frozen LIVE subset includes S714. No counter was run, and the other C legs cannot be judged from this isolated candidate. Claim O's operability repair and review gate were not this seat's scope. No source row, entry, README, counter, or product file was changed; the L1 remains responsible for integration and the decision to replace or retry this candidate.

## Touched surfaces and artifacts

- Lane change: this report only: `.ufo/waves/round-63/w1/ScribeRowS714.md`.
- Scratch research artifact (candidate row, entry bullet, Gate line, source text and locator outputs): `/fast/scratch/hyaku/kotodama-r63/kotodama-r63-w1-ScribeRowS714/S714.md`.
- No install/update was performed. No git/jj write command, counter run, or browser was used.
