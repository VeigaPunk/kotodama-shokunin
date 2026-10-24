# ScoutReopenB — blind re-open (claim C), S758–S765

## Method / evidence
Read the frozen claim and `reports/round-65/accept-c.py` contract. The row-opening task records fragment format and seat ownership in `.ufo/waves/round-65/taskcall-v2.json`: `.ufo/waves/round-65/rows/<SEAT>/row-<SID>.txt`. The `rows/` directory listing was empty, and direct reads of all eight expected fragment paths returned `Path ... not found`. Therefore no live URL or quote was available to supply to curl; no curl attempt is claimed. These are missing-fragment dependencies, not findings that a source URL is dead.

## Per-row findings

- **S758 — NOT-LOCATED:fragment absent.** Dependency: `.ufo/waves/round-65/rows/ScoutRow05/row-S758.txt`. Direct read: path not found; URL unavailable, so no independent curl reopen.
- **S759 — NOT-LOCATED:fragment absent.** Dependency: `.ufo/waves/round-65/rows/ScoutRow05/row-S759.txt`. Direct read: path not found; URL unavailable, so no independent curl reopen.
- **S760 — NOT-LOCATED:fragment absent.** Dependency: `.ufo/waves/round-65/rows/ScoutRow06/row-S760.txt`. Direct read: path not found; URL unavailable, so no independent curl reopen.
- **S761 — NOT-LOCATED:fragment absent.** Dependency: `.ufo/waves/round-65/rows/ScoutRow06/row-S761.txt`. Direct read: path not found; URL unavailable, so no independent curl reopen.
- **S762 — NOT-LOCATED:fragment absent.** Dependency: `.ufo/waves/round-65/rows/ScoutRow07/row-S762.txt`. Direct read: path not found; URL unavailable, so no independent curl reopen.
- **S763 — NOT-LOCATED:fragment absent.** Dependency: `.ufo/waves/round-65/rows/ScoutRow07/row-S763.txt`. Direct read: path not found; URL unavailable, so no independent curl reopen.
- **S764 — NOT-LOCATED:fragment absent.** Dependency: `.ufo/waves/round-65/rows/ScoutRow08/row-S764.txt`. Direct read: path not found; URL unavailable, so no independent curl reopen.
- **S765 — NOT-LOCATED:fragment absent.** Dependency: `.ufo/waves/round-65/rows/ScoutRow08/row-S765.txt`. Direct read: path not found; URL unavailable, so no independent curl reopen.

No source-body, quote-length, capture-path, or HTTP-status conclusion is possible until the corresponding fragment lands.
