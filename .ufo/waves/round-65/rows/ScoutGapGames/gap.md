# Claim-C gap at base: evidence

## Requested commands and outputs

1. Command (run at the frozen base):
```sh
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && git ls-tree -r --name-only 17c32302c6845c8f164b985a8cb312d3181c8788 -- corpus/knowledge | grep -ciE 'game|play|sport|contest|toy|mancala'
```
Output:
```text
2
```
This is **not** the expected 0. The two matching base paths are `corpus/knowledge/culture-material/sumptuary-law-rank-display.md` (`play` is a substring of `display`) and `corpus/knowledge/culture-material/transport-mobility-lexicon.md` (`sport` is a substring of `transport`). Thus the frozen filename counter has lexical false positives; it does not establish two topic owners, but its stated `0 filename owners` predicate is false as written.

2. Command (executed from the lane root against its current worktree):
```sh
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && grep -riE 'mancala|knucklebone|astragal|tug.of.war|senet|hnefatafl|patolli' corpus/knowledge/ | head -5
```
Output: *(no stdout)*

3. Command (run from `/home/vgpnk/Projects/shokunin`):
```sh
grep -rliE 'mancala|senet|hnefatafl|patolli' /home/vgpnk/Projects/shokunin/lore-shokunin /home/vgpnk/Projects/shokunin/chousa-shokunin 2>/dev/null | head -5
```
Output:
```text
/home/vgpnk/Projects/shokunin/chousa-shokunin/.ufo/waves/round-35/w2/ScoutManBash/bash.1
```
This is a copied GNU Bash man page, not an ownership entry: its line 13440 contains “Usenet”, which includes the searched substring `senet`.

## Base corroboration and limits

A base-pinned `git grep -n -iE 'mancala|knucklebone|astragal|tug.of.war|senet|hnefatafl|patolli' 17c32302c6845c8f164b985a8cb312d3181c8788 -- corpus/knowledge` returned no stdout (exit 1). The frozen `reports/round-65/telemetry/dry-run-c.txt` also records the base acceptance failing with the proposed entry unreadable, zero rows for S750-S775, all 26 IDs missing, and registry count unchanged at 675. The named-term scans support a gap in those specific game-name terms; they do not prove that no broader/partial topic coverage exists. In particular, the exact frozen filename count is not a valid zero-owner test because of the two substring matches above.

## Build order

1. Register map — map the entry’s coverage classes to the mined source rows.
2. Source-grounded bullets by class — board; ball; physical contest; children’s play; gambling/betting; ritual sport.
3. Cross-cultural patterns — compare attested patterns without flattening local contexts.
4. Design protocol; calibration — derive usable design choices and mark evidential limits.
5. One-way pointing to partial owners, without restating their scope; lore handoff.
