# B2ExecEntry — claim C integration proof

## Files and behavior

- Added `/home/vgpnk/.cache/hyaku/kotodama-r64/w2/B2ExecEntry/assemble_entry.py`.
- CLI: `python3 assemble_entry.py --root <lane-copy> [--bullets <json>]`. `--bullets` defaults to `/home/vgpnk/.cache/hyaku/kotodama-r64/w2/bullets.json`.
- The assembler requires all 26 mapped S-IDs, fills each skeleton marker in numeric ID order (section 9 is empty), writes the entry, inserts the README row after the final linguistics index row, bumps the linguistics count and total, and recomputes the counts-footer values from the copy's six indexed directories.
- Added `synthetic-bullets.json` in the executor scratch directory and assembled into `/home/vgpnk/.cache/hyaku/kotodama-r64/w2/B2ExecEntry/lane/` only. The original lane was not modified by the copy-based proof; this requested report is the only file written in it.

Assembly command:

```text
python3 /home/vgpnk/.cache/hyaku/kotodama-r64/w2/B2ExecEntry/assemble_entry.py --root /home/vgpnk/.cache/hyaku/kotodama-r64/w2/B2ExecEntry/lane --bullets /home/vgpnk/.cache/hyaku/kotodama-r64/w2/B2ExecEntry/synthetic-bullets.json
```

Output:

```text
assembled /home/vgpnk/.cache/hyaku/kotodama-r64/w2/B2ExecEntry/lane/corpus/knowledge/linguistics/language-socialization-and-acquisition.md
```

## Retained evidence

`python3 -B reports/round-28/readme/sweep.py` from the copied lane (exit 0):

```text
parts {"civilizations": 95, "culture-material": 31, "linguistics": 30, "myth-symbol": 29, "synthesis": 29, "verification": 24}
rows 238 files 238
missing_from_index 0 []
topic_mismatch 0 []
orphan_rows 0 []
header_drift {}
totals_line 238 totals_ok True
footer {"date": "2026-10-23", "command": "python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge", "total": 238, "dir_totals": [30, 29, 31, 29, 24, 95]}
footer_live {"total": 238, "dir_totals": [30, 29, 31, 29, 24, 95], "order": ["linguistics", "myth-symbol", "culture-material", "synthesis", "verification", "civilizations"]}
footer_findings [] footer_ok True
readme_sha256 5044b7a64c47eb588e7f038fe8684517a4214b15bc254be029993ce8f864f693
```

`python3 -B tools/check-cited-lines.py corpus/knowledge/linguistics/language-socialization-and-acquisition.md` from the copied lane (exit 1):

```text
MULTI-ID corpus/knowledge/linguistics/language-socialization-and-acquisition.md:4 S718,S743
CITED-LINES: 1 finding(s) in 1 file(s)
```

The single finding is the skeleton's metadata range `S718–S743` on line 4; synthetic claim bullets each contain one ID. The entry has **81 lines**, **H1=1**, **H2=10**, **H3=0**.

## Risks / blockers

No build blocker. The cited-lines finding is retained rather than changing the supplied skeleton's source-range metadata; the fixture bullets are invented solely for the requested assembly proof and are not source-validated content. No tools were installed or updated.
