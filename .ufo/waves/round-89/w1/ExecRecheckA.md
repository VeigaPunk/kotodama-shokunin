# ExecRecheckA — round 89, claim F slice (S009 S012 S020 S021 S031 S032 S033 S084)

Access date 2026-11-04 (-03:00). Stage: `.ufo/waves/round-89/w1/stage/ExecRecheckA/` with `{id}.txt` captures (8), `manifest-part.json`, `rows.md`.

## Counts
LOCATED 8 / NOT-LOCATED 0.

## Per row
- S009 LOCATED — https://cals.info/statistics/ 200. Quick numbers still read 1323 conlangs, 127 natlangs, 145 features, 97.9% from WALS.
- S012 LOCATED — https://arxiv.org/abs/2508.06094 200. The abstract is now v4 (revised 17 Apr 2026). The method text in the teaches cell is unchanged.
- S020 LOCATED — https://arxiv.org/abs/2603.19283 200. The abstract still gives 2,670 / 200 / 58,450 and Llama3 0.85 F1.
- S021 LOCATED — https://arxiv.org/abs/2606.17350 200. The abstract is now v2 (revised 2 Sep 2026). It still states the homogeneity finding, the frontier convergence and the failed mitigations.
- S031 LOCATED — PLOS article 200. Results still read "50 (79%)" of 63, and 36 (87%) of 41.
- S032 LOCATED, with caveats (see Defects) — https://doi.org/10.1016/j.evolhumbehav.2024.04.014.
- S033 LOCATED — PLOS correction 200. It still contains the reliability/replicability concern, plus the "Definition of forager" and "Selection criteria" sections.
- S084 LOCATED — https://www.signwriting.org/ 200. The banner "Sign Languages are written languages!" is still there.

I checked every quote with `measure89.contains` on the stage capture: all True, all ≤25 words and ≥20 normalised characters. Every sha256 matches its stage file.

## Teaches cells that look wrong
None. Two small drifts, neither a contradiction:
- S012's anchor cell says "arXiv v1", but the live abstract is v4.
- S021's abstract is now v2.

I only flag these; nothing was edited.

## Defects / risks (unresolved, for L1)
1. **S032 capture method.** A plain GET of the DOI returns HTTP 200, but the body is an Elsevier linkinghub meta-refresh/JS redirect stub. Its only non-script text is "Redirecting". The other attempts:
   - ScienceDirect: 403.
   - Wayback `web/2026/<doi>`: resolves to the 20261019045840 ScienceDirect 403 block page.
   - CDX: lists no 2xx body capture of the article page.

   The capture I used comes from the **same DOI URL** fetched with `Accept: application/vnd.citationstyles.csl+json`. That redirected to api.crossref.org and returned 200 CSL-JSON, which I kept as-is. The JSON has the title, issued 2024-07 and 54 references, which matches the row's Crossref anchor.

   The risk: a re-fetch with the bare prescribed curl command gets the stub, not this JSON. The manifest `url` is the DOI exactly as fetched, and the header is recorded in `attempts`. If L1 rejects header-negotiated fetches, change S032 to NOT-LOCATED (reason: live body is a redirect stub and the article is 403/archived-403).
2. **S009 capture is short (689 chars).** The Quick numbers are split across lines ("97\n.9%"). The quote matches only after measure89 normalisation, not as a raw substring.
3. The counter's known hole: a fabricated capture would also pass. These captures are real fetches; their raw_sha256 values are in the manifest for an independent re-fetch.

## Commands (rc)
- curl live ×8 (rc 0, all 200).
- curl ScienceDirect (rc 0, 403).
- curl Wayback 2026 DOI (rc 0, 403).
- Wayback CDX ×3 (rc 0).
- curl DOI with CSL Accept header (rc 0, 200).
- measure89.contains / sha re-check (rc 0).

No installs (pdftotext was already present and not needed). No production, git or pacman actions. Scratch `/fast/scratch/hyaku/kotodama-r89/ExecRecheckA` removed.
