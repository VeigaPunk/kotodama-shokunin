# ConnectSiblings — round 62 wave 1

## Evidence
- Sibling scan (read-only, excluding `.git` and `.ufo`; terms `web.archive.org/web`, `Retry-After`, `figcaption`, `CAPTION_ONLY`, `reopen`, `locate(`, `talaria`, `footwear`): the only sibling with a source-row re-open tool is `chousa-shokunin/tools/quote-reopen.py`.
- `chousa-shokunin/tools/quote-reopen.py` fetches registry URLs with one retry, URL safety checks, and normalised quote matching; it treats `figcaption` as ordinary block text and has no archived-copy fallback or body-vs-caption verdict.
- `chousa-shokunin/corpus/knowledge/quote-reopen-r29.md` and `quote-reopen-r30.md` document that lane's quote-reopen rule.
- Exact-term searches for `talaria` and `footwear` across sibling lanes returned no matches; no sibling lane owns footwear or classical-myth costume (talaria) terms.
- Kotodama's own prior tool is `kotodama-shokunin/reports/round-61/reopen-quote.py`, not a sibling.

## Affected axes
- Adjacency: unchanged-to-improved by explicit naming; no harm to depth, operability, freshness, calibration.

## Proposed move
- Name `chousa-shokunin` in the round-62 adjacency notes as the nearest prior art for row/quote re-opening.
- State that claim O (`tools/reopen-row.py`) is not a duplicate of chousa's `quote-reopen.py`: chousa covers live fetch/retry/normalisation, while kotodama's tool adds bounded multi-pass retry, archived-copy fallback, and a body-vs-caption verdict.
- State that no sibling lane owns footwear/talaria terms, so no cross-lane ownership or citation conflict exists for the new talaria row.

## Risks
- Conflating chousa's live-only quote reopen with kotodama's row reopen could make future adjacency claims overstate reuse.
- If a later round imports chousa's fetcher, preserve the caption classification and archived-copy fallback as kotodama-owned behaviour.

## Verification
- `grep -RIn --exclude-dir=.git --exclude-dir=.ufo -l 'talaria' /home/vgpnk/Projects/shokunin/*-shokunin` → no sibling matches.
- `grep -RIn --exclude-dir=.git --exclude-dir=.ufo -l 'footwear' /home/vgpnk/Projects/shokunin/*-shokunin` → no sibling matches.
- `sed -n '1,40p' /home/vgpnk/Projects/shokunin/chousa-shokunin/tools/quote-reopen.py` confirms no caption/body verdict or archived-copy fallback.