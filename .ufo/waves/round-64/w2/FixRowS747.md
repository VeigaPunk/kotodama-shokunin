# FixRowS747 — scoped findings

## Axes
Coverage, operability, calibration.

## Change
Edited only `.ufo/waves/round-64/rows/ScribeRejS747/row.txt`.

- Old anchor: `wording tested: “Britannica’s Mortarboard page as evidence for mortarboard use in academic dress”`
- New anchor: `Britannica Mortarboard entry, article lead (intended locator); live fetch 403 (Cloudflare challenge) on 2026-10-23; wording not locatable`

The anchor now names the intended locator and records the failed fetch without presenting invented wording as a quote. The `rejected` status, `REJECTED:` ground, flip condition, and `used-by —` remain unchanged.

## Retained evidence and check
The existing `.ufo/waves/round-64/w1/ScribeRejS747.md` retest records the exact output `403 https://www.britannica.com/topic/mortarboard` and says the ordinary request did not serve an article; the quote locator was not run (`TEST2: not applicable`). `.ufo/waves/round-64/w1/ReviewSupportC.md` independently records a 403 Cloudflare challenge for S747.

Ran the required row self-check:

```text
python3 -B .ufo/waves/round-64/check-rows.py --rows-dir .ufo/waves/round-64/rows
CHECK-ROWS: 32/32 clean
```

## Risks and blockers
The article wording remains unlocatable while the live URL returns 403; the repaired anchor is an intended locator and access record, not a source quotation. No blocker. No tools installed or updated.
