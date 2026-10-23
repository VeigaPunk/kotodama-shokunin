# ReviewSupersedeD58 — superseding rows S568 (→ S452) and S569 (→ S453)

Round-57 residual Falsify findings under review (corpus/lessons/round-57.md:120-121, 133):
S452 anchor differs by an apostrophe and is Wayback-dependent; S453's scope/teaches implied
flag-protocol rules the served page does not carry. Both rows are cited by
corpus/knowledge/myth-symbol/heraldry-emblems-identity-marks.md (:113, :149), so both
superseding rows are `mined` with that used-by. The registry is append-only: nothing below
edits S452 or S453 in place.

## S452 → S568 — verdict: agree (with a nuance), fix = re-source to the live NAVA page

Re-opened by ordinary means, 2026-10-23.

- Wayback capture `http://web.archive.org/web/20010723223146if_/http://www.nava.org/gfbf/gfbf-3.htm`
  (GET redirects to capture 20010722170251; raw bytes fetched 2026-10-23, 3,544 bytes): the
  served sentence is `Never use writing of any kind or an organization\x92s seal\x85` — a
  cp1252 right single quote (’) in "organization’s" and a trailing ellipsis (…) that the
  anchor drops. Verbatim, the anchor `…an organization's seal` does differ by an apostrophe
  (and a dropped ellipsis). Agree.
- Nuance for calibration: under reports/round-58/reopen-quote.py's own match rule (NFKC,
  casefold, `\W+` → space) the curly apostrophe and the straight one both vanish, so the
  anchor DOES mechanically locate on this capture when the fetch succeeds — a live run today
  printed `LOCATED`. The defect is verbatim fidelity plus availability: the capture serves
  intermittently (urllib run ~20 s earlier returned `HTTPError`; the round-57 spot-check
  miss was the same Wayback HTTPError). The row should not stand on this capture.
- Live copy found: `https://nava.org/good-flag-bad-flag` (direct GET, HTTP 200, text/html,
  24,534 bytes) serves `Never use writing of any kind or an organization's seal.` with a
  STRAIGHT apostrophe — the anchor verbatim — in the ordered list "1. Keep It Simple …
  5. Be Distinctive or Be Related". The same content sits at
  `https://nava.org/content.aspx?page_id=22&club_id=622278&module_id=475721` (HTTP 200) and
  NAVA's PDF `https://nava.org/docs.ashx?id=804394` (HTTP 200, application/pdf via a signed
  S3 redirect, 2,591,832 bytes) prints `organization’s seal . . .` (curly). GET on the
  vanity URL is 200; HEAD returns 404 — use GET.
- Second defect, same class as S440: the S452 scope cell is truncated mid-phrase at
  `…the historical link from flags to |`. S568's scope below is written complete and covers
  only what the live page carries.

Registry row (append; teaches opens `supersedes S### — `):

| S568 | North American Vexillological Association / compiled by Ted Kaye, "Good Flag, Bad Flag" booklet page (booklet 2001; page undated) — https://nava.org/good-flag-bad-flag (direct, HTTP 200; also at https://nava.org/content.aspx?page_id=22&club_id=622278&module_id=475721, HTTP 200; PDF edition https://nava.org/docs.ashx?id=804394, HTTP 200, prints the same rule with a typographic apostrophe) | docs | A | The booklet's five basic principles of flag design with their one-line glosses as presented on the live page | served text: "Never use writing of any kind or an organization's seal" | supersedes S452 — re-source and scope only: the 2001 Wayback capture prints "organization’s seal…" (typographic apostrophe, trailing ellipsis) and serves intermittently, and S452's scope cell is truncated; the live page serves the anchor verbatim. Content as S452: the NAVA booklet's five principles give worldbuilders a working design grammar for flags, from simplicity to meaningful symbolism. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/myth-symbol/heraldry-emblems-identity-marks.md |

Gate line:

- S568 — https://nava.org/good-flag-bad-flag — accessed 2026-10-23 — served text: “Never use writing of any kind or an organization's seal”. Grounds: supersedes S452 — re-source and scope only: the 2001 Wayback capture prints "organization’s seal…" (typographic apostrophe, trailing ellipsis) and serves intermittently, and S452's scope cell is truncated; the live page serves the anchor verbatim. Content as S452: the NAVA booklet's five principles give worldbuilders a working design grammar for flags, from simplicity to meaningful symbolism. Seat: ReviewSupersedeD58.

Locator output (all runs this session, `python3 -B reports/round-58/reopen-quote.py '<url>' '<quote>'`):

```
LOCATED https://nava.org/good-flag-bad-flag
LOCATED https://nava.org/content.aspx?page_id=22&club_id=622278&module_id=475721
LOCATED https://web.archive.org/web/20010723223146if_/http://www.nava.org/gfbf/gfbf-3.htm
NOT_LOCATED http://web.archive.org/web/20010723223146if_/http://www.nava.org/gfbf/gfbf-3.htm HTTPError   (earlier run, ~20 s before; capture is intermittent)
```

## S453 → S569 — verdict: agree, fix = scope to the statutory design

Re-opened by ordinary means, 2026-10-23.

- `https://www.govinfo.gov/content/pkg/USCODE-2024-title4/html/USCODE-2024-title4-chap1-sec1.htm`
  (direct GET, HTTP 200): the page is 4 U.S.C. §1 and nothing more — the design statute
  ("thirteen horizontal stripes … forty-eight stars"), its 1947 credit, Statutory Notes
  (short-title amendments), and the Executive Documents notes including Ex. Ord. 10834's
  proportions/sizes table and agency procurement clauses. A full-text scan finds no
  protocol rules for handling the flag (no display, ceremony, salute, half-staff, carrying
  or respect rules; `hoist` and `respect` occur only inside the dimension table and
  procurement clauses). The S453 scope cell is truncated at `protocol rules for |` and the
  teaches cell claims "design and handling rules" — neither is on the page. Agree: the
  fix is to scope the row to the statutory design (plus the proportion notes the page does
  carry) and drop the handling-rules claim. The entry's offending protocol clause was
  already removed at round 57 (lesson: "clause removed, applied"); entry :113 now cites
  S453 only for the design statute.

Registry row (append):

| S569 | Office of the Law Revision Counsel / U.S. Government Publishing Office, 2024, United States Code Title 4 Chapter 1 §1 — https://www.govinfo.gov/content/pkg/USCODE-2024-title4/html/USCODE-2024-title4-chap1-sec1.htm (direct, HTTP 200) | docs | A | Statutory description of the national flag's design (stripes, union, stars), with the section's amendment and Ex. Ord. 10834 proportion notes; no flag-handling or protocol rules — those sit in 4 U.S.C. §§5-10 | served text: "The flag of the United States shall be thirteen horizontal stripes, alternate red and white; and the union of the flag shall be forty-eight stars, white in a blue field." | supersedes S453 — scope and teaches only: the served section fixes the statutory design and carries amendment plus Ex. Ord. 10834 proportion notes; it states no handling or protocol rules, and S453's scope cell is truncated. An official flag law fixes a flag's design, showing how a state codifies its identity mark. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/myth-symbol/heraldry-emblems-identity-marks.md |

Gate line:

- S569 — https://www.govinfo.gov/content/pkg/USCODE-2024-title4/html/USCODE-2024-title4-chap1-sec1.htm — accessed 2026-10-23 — served text: “The flag of the United States shall be thirteen horizontal stripes, alternate red and white; and the union of the flag shall be forty-eight stars, white in a blue field.”. Grounds: supersedes S453 — scope and teaches only: the served section fixes the statutory design and carries amendment plus Ex. Ord. 10834 proportion notes; it states no handling or protocol rules, and S453's scope cell is truncated. An official flag law fixes a flag's design, showing how a state codifies its identity mark. Seat: ReviewSupersedeD58.

Locator output:

```
LOCATED https://www.govinfo.gov/content/pkg/USCODE-2024-title4/html/USCODE-2024-title4-chap1-sec1.htm
```

## rejected:

- `http://web.archive.org/web/20010723223146if_/http://www.nava.org/gfbf/gfbf-3.htm` (and the
  `id_`/bare variants, each of which redirects to capture 20010722170251): intermittent —
  `NOT_LOCATED http://web.archive.org/web/20010723223146if_/http://www.nava.org/gfbf/gfbf-3.htm HTTPError`
  on one run, `LOCATED` on the next — and the served text prints `organization\x92s seal\x85`,
  not the anchor's straight-apostrophe wording. Not offered; superseded by the live NAVA page.
- `https://nava.org/docs.ashx?id=804394` (live NAVA PDF, HTTP 200 via signed S3 redirect):
  pypdf 5.4.0 extraction prints `Never use writing of any kind or an  \norganization’s seal . . .`
  — curly apostrophe and ellipsis, a different quote than the anchor. Kept as corroborating
  URL inside the S568 source cell, not as the anchor's carrier.
- `https://nava.org/content.aspx?page_id=22&club_id=622278&module_id=475721`: serves the
  anchor verbatim (LOCATED) and is named as the alternate URL in S568; the vanity URL is
  the cleaner primary.
- `https://nava.org/good-flag-bad-flag` HEAD returns 404 while GET returns 200 — noted for
  future re-openers; GET is what the locator tool and this seat used.

## Notes for the L1

- Records-row rules: TOPIC/RELEVANCE/8-30-word teaches limits are claim-C legs and do not
  apply here per the assignment; both rows keep the registry's records conventions
  (11 cells, `supersedes S### —` teaches, mined + used-by since the superseded rows are
  cited, opened 2026-10-23, recheck 2027-10-23).
- Residual: S452/S453 remain in the registry as mined (append-only); the entry's
  heraldry-emblems citations can keep S452/S453 or be repointed to S568/S569 at the
  integrator's option — the rows are mined with the same used-by either way.

installs: none (pypdf 5.4.0 run via `uv run --no-project --with pypdf==5.4.0`, ephemeral
environment, no system install).
