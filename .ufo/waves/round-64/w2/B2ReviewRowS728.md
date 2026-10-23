# B2ReviewRowS728 — falsification review of inherited draft S728

Draft under review: `/home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRowS728/row.txt` (wave-1 inheritance, unverified).
Counter: `reports/round-64/accept-c.py` legs ROWS (shape) and RESTATE (entry-line support); LIVE leg also covers S728.

## HTTP results (verbatim)

- Live URL: `curl -sL --max-time 90 -o body.pdf -w ... 'https://press-files.anu.edu.au/downloads/press/n9994/pdf/ch08.pdf'`
  → `HTTP 200 https://press-files.anu.edu.au/downloads/press/n9994/pdf/ch08.pdf size=129796` — `PDF document, version 1.7`. Plain GET, 2026-10-23.
- Capture: `curl -sL ... 'https://web.archive.org/web/20250505204752id_/https://press-files.anu.edu.au/downloads/press/n9994/pdf/ch08.pdf'`
  → `HTTP 200 https://web.archive.org/web/20250505204752id_/https://press-files.anu.edu.au/downloads/press/n9994/pdf/ch08.pdf size=129796` — identical byte count; same-page capture confirmed.
- Lane locator re-run (this seat): `python3 -B reports/round-61/reopen-quote.py '<URL>' '<quote>'` →
  `LOCATED https://press-files.anu.edu.au/downloads/press/n9994/pdf/ch08.pdf` (exit 0). Matches draft's `VERIFY:` line.

## Anchor quote search

Method: `uv run --with pypdf==5.4.0` (same extractor the locator uses) → 10 pages; normaliser = NFKC + casefold + `[\W_]+`→space, identical to `reopen-quote.py`/`accept-c.py`.

- Normalised quote (14 words, in the 8–25 window): `kaluli mothers use elema say it like this to prompt the children to correct`
- FOUND at normalised offset 1456. Context (±200 chars):
  `…there is not much research for non weird languages nevertheless the existing research suggests that there is variation between language communities schieffelin 1990 for example reports that kaluli mothers use elema say it like this to prompt the children to correct their non target like utterances a much more explicit strategy…`
- Location check: verbatim, contiguous, in running body text — first paragraph of § 8.1 "Previous research on corrective input" (p. 139), immediately after the heading. Not a caption/alt/navigation element; the PDF has no such markup anyway. Locator claim `§ 8.1 … paragraph 1` verified.

## Verdict table

| field | draft value | verified? | evidence (verbatim) | required fix |
|---|---|---|---|---|
| Row shape | 11 cells, `\| S### \|` row | yes | cell count 11; no `\|` inside cells; ends `corpus/knowledge/linguistics/language-socialization-and-acquisition.md` | none |
| Citation | Henrike Frye, 2022 "Corrective input", Child-directed Speech in Qaqet: A Language of East New Britain, Papua New Guinea | yes | PDF tail: `This text is taken from Child-directed Speech in Qaqet: A Language of East New Britain, Papua New Guinea, by Henrike Frye, published 2022, The Australian National University, Canberra, Australia. doi.org/10.22459/CDSQ.2022.08`; page 1 heading `8 Corrective input` | none |
| kind | `book` | yes | chapter PDF of a published monograph (ANU Press n9994) | none |
| tier | `B` for scope "Frye's secondary account of Schieffelin's report on Kaluli maternal elema prompting" | yes | scope self-declares secondary; PDF body: `Schieffelin (1990), for example, reports that Kaluli mothers use elema…` — the row is correctly scoped to what this page is authoritative for (the secondary report), not to Kaluli primary data (which would be Schieffelin 1990, tier A). B = "strong secondary" fits | none |
| anchor quote | `"Kaluli mothers use elema 'say it like this' to prompt the children to correct"` | yes | verbatim contiguous hit at offset 1456; 14 normalised words (8–25 ✓); body text, not heading/caption | none |
| live URL | `press-files.anu.edu.au/.../ch08.pdf` | yes | HTTP 200, real PDF; not a placeholder/search/echo host | none |
| capture | `web.archive.org/web/20250505204752id_/...` | yes | HTTP 200, size 129796 identical to live fetch → same-page capture | none |
| teaches | "Helps worldbuilders represent children learning explicit utterance correction from caregivers." | yes | consistent with quoted passage (mothers prompting children to correct utterances) | none |
| status/date/recheck/used-by | `mined` \| 2026-10-23 \| 180d \| entry path | yes | matches ROWS leg requirements | none |
| BULLET | `- Kaluli caregivers teach children to correct non-target-like speech with explicit prompts (S728)` | yes | RESTATE simulation: content words {kaluli,caregivers,teach,children,correct,target,like,speech,explicit,prompts} = 10 ≥ 5; in-order quote hits = 3 (kaluli→children→correct, minimum met); longest verbatim copied run = 3 ("children to correct") ≤ 12; novel words {caregivers,teach,target,speech,explicit,prompts} present. Support: quote states mothers "prompt the children to correct their non-target-like utterances" — bullet's "explicit prompts" tracks "elema 'say it like this'… a much more explicit strategy"; "teach…with prompts" is a fair paraphrase, no invented quantity or overreach | none |

## Residual risk

- In-order hits sit exactly at the minimum (3). Any entry-line rewrite that drops `kaluli` or reorders `children`/`correct` before it would fail RESTATE; the L1 should keep the clause's first three content words in this order.
- Anchor quotes a secondary report; if the entry needed a primary claim about Kaluli practice, Schieffelin (1990) itself would be required — but the row's scope and tier are internally consistent, so no fix required.

## Tooling

No installs. Used `uv run --with pypdf==5.4.0` (already-present uv; ephemeral env, same pypdf pin as the lane locator).

VERDICT: CLEAN — quote located verbatim in §8.1 body text (locator prints LOCATED), citation/tier/scope accurate, bullet passes RESTATE with in_order=3.
