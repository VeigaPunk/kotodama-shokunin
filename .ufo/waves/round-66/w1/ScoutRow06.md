# ScoutRow06 — ROW-OPENING S787 & S788 (claim C, r66-v2)

## Deliverables
- `.ufo/waves/round-66/rows/ScoutRow06/row-S787.txt` — OPENED
- `.ufo/waves/round-66/rows/ScoutRow06/row-S788.txt` — OPENED
- `.ufo/waves/round-66/rows/ScoutRow06/rejects.txt` — 2 rejects with flips

## S787 — Vedic/Hindu puja fragrance (sandalwood, ghee lamps)
**Source**: Chihiro Koiso, "Fragrance in Hindu Culture," Kanazawa Seiryo University Humanities Research 2(1), pp. 49–59 (2017), university-journal PDF — tier B.
- Live: `https://www.seiryo-u.ac.jp/u/research/gakkai/ronbunlib/humanities_ronsyu_pdf/No2/04_koiso.pdf` → curl -L HTTP 200, `application/pdf`, 701,396 B, 2026-10-24.
- Anchor (English abstract, verbatim via pdftotext): "sandalwood paste, incense, pastille, camphor, lamps of burning oil or ghī, and fragranced flowers to the deity" — covers sandalwood + ghee lamps + incense in one quote.
- Capture: fresh `/save/` redirect → `web/20261024113504`; prior capture 20240624185409 replays **byte-identical** to live (verified `cmp`). Uniqueness: zero `seiryo-u.ac.jp` hits in corpus/SOURCES.md.
- Caveat recorded in ACCESS: paper body is Japanese; the quote comes from the English abstract.

## S788 — Anthropology of smell (class/gender codes, Classen)
**Source**: Howes, Synnott & Classen, "Anthropology of Odor (1990–1994)" — research report by Concordia U / Harvard CSWR anthropologists, author-hosted on david-howes.com — tier B (survey by the field's central authors, named in the brief).
- Live: `https://david-howes.com/senses/Consert-Odor.htm` → HTTP 200, 22,050 B; www and non-www hosts serve byte-identical copies (verified `cmp`).
- Anchor (body, Suyá section, verbatim): "Men are socialized through initiation and lose their strong-smelling odor. Women, on the other hand, by their very sexuality are strong smelling." — gender/life-stage odor coding; the page's six-fold olfactory-classification scheme covers group/class typing.
- Capture: CDX latest 200 = **20260827025307** (same page, non-www host). Uniqueness: zero `david-howes` hits in corpus/SOURCES.md.

## Rejects
- `pluralism.org/lamp-offerings-hindu-worship` — ideal content for S787 but live curl 403 (default + Chrome UA); flip = 200 + locatable quote.
- `moodle4.cs.huji.ac.il/...view.php?id=117579` — Moodle copy of Classen's "Odor of the Other" (canonical is paywalled on AnthroSource/JSTOR); flip = stable OA repository.

## Gaps / risks for L1
- Fresh `/save/` for S788: archive.org went unreachable mid-run (curl exit 7, ~11:37 UTC) after the first save round; the 20260827 capture is a real prior 200 capture of the identical page, so the row carries a capture either way. If accept-c requires a strictly fresh ts, retry `/save/` when archive.org recovers.
- S788 live URL uses non-www host to match the capture; www host serves identical bytes, recorded in ACCESS.
- No tools installed; no repo mutation (writes confined to `.ufo/waves/round-66/`).

Report: .ufo/waves/round-66/w1/ScoutRow06.md
