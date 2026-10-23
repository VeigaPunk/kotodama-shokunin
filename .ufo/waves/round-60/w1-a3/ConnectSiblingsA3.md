# ConnectSiblingsA3 — sibling-lane scan for Claim D (amulets entry)

Seat: `KotodamaR60A3.ConnectSiblingsA3`. Axes judged: adjacency, depth.
Scope: read-only scan of every sibling lane `/home/vgpnk/Projects/shokunin/*-shokunin` except `kotodama-shokunin`, limited to `corpus/knowledge/`, `PROVINCE.md`, `SKILL.md` as instructed. No lane files edited; no subagents dispatched; no installs.

## 1. Scan method

Run from `/fast/scratch/hyaku/kotodama-r60a3/ConnectSiblingsA3/` with ripgrep (rg 15.1.0) over all 20 sibling lanes, all file types:

```
rg -i -l -e 'pazuzu|lamashtu|hematite|blood.?stone|concealed shoe|concealed deposit|ga'"'"'u|apotropaic|amulet|talism|evil eye|nazar|mezuz|omamori|ofuda|phylacter|witch mark' --glob '!kotodama-shokunin/**' /home/vgpnk/Projects/shokunin
```

Result: only `/home/vgpnk/Projects/shokunin/MANIFEST.json` (fleet dispatch digest, not a lane knowledge owner) contains "amulet", in a round-59 dispatch note. No sibling lane file contains any scanned term.

A second, path-scoped pass restricted to `corpus/knowledge/`, `PROVINCE.md`, `SKILL.md` per the seat instruction was also run; it returned zero hits. Per-lane PROVINCE titles were read to check conceptual neighbours (architecture/threshold marks, stone virtues, demons, building deposits); none of the 20 lanes owns a partial of the amulets chain.

## 2. Hits (path:line, one sentence each)

None. Across all 20 sibling lanes, no file under `corpus/knowledge/`, `PROVINCE.md`, or `SKILL.md` contains any of the scanned terms as a genuine topic reference.

No path:line hit to report.

## 3. Contested facts among siblings

None. No sibling lane states any of the four round-59 propositions or their S648–S651 repairs at all, so there is no sibling-side contested fact for the L1 to name. The four propositions remain contested only against their own cited pages (Heeßel/IDD on Pazuzu; the Met record on hematite; Shawcross/University of Hertfordshire on concealed shoes; the V&A record on ga'u), already captured in rows S602/S648, S616/S649, S623/S650, S643/S651.

## 4. One-way pointers the amulets entry could carry (report only; L1 decides)

- No new cross-lane pointer is warranted: no sibling lane owns a partial of the amulets chain (danger, carrier, material, surface, deposition, maker, life cycle) that the entry does not already own or point to in-lane.
- The existing pointer to `lore-shokunin` (couples line: "lore-shokunin receives canon (§13)") already covers the only sibling lane whose domain (fictional-world records) touches the entry's output. Keep it.
- Do not pre-add speculative §2 rows for sibling lanes that do not yet own the partial; add them only if a sibling lane later gains protective-object or apotropaic-mark content.

## 5. Proposed move (non-obvious)

No change to the entry, rows, lesson, or records from this seat. The scan closes the sibling-adjacency question for Claim D with a negative result: adjacency harm is nil because no sibling overlaps the topic, and depth is unaffected. The one non-obvious synthesis is to record the negative result as fleet-wide adjacency evidence rather than as a local absence: the entry's "gap filled" claim already states that no in-lane file under `corpus/knowledge` owns protective objects as a system; this scan extends that to all 20 sibling lanes, so the gap is fleet-wide, not merely lane-local. L1 may cite this report as the sibling-overlap check; no edit is required.

## 6. Risks

- A sibling lane could contain amulet/apotropaic content outside the scanned paths (e.g. in `.ufo/` build artifacts or lessons). The seat instruction limited the scan to `corpus/knowledge/`, `PROVINCE.md`, `SKILL.md`; those surfaces were fully covered. `.ufo/` artifacts were not exhaustively scanned and are out of scope for this seat.
- If a lane later adds content under a path not yet present, re-run this scan before the freeze.

## 7. Verification

- Lanes scanned: 20 (`audio`, `chousa`, `game-dev-2d`, `game-dev-3d`, `kagi`, `kaidoku`, `kake`, `kama`, `kasegi`, `kengaku`, `kotoba`, `kumitate`, `lore`, `mado`, `mori`, `revenger`, `souji`, `tabi`, `tameshi`, `tsukuroi`).
- Paths scanned per lane: `corpus/knowledge/` (when present), `PROVINCE.md`, `SKILL.md` (when present), plus an all-file-type sweep of sibling lanes.
- Genuine hits: 0. Out-of-scope textual hit inspected and dismissed: `MANIFEST.json` (fleet dispatch digest, not a lane knowledge owner).
- No git/jj write commands run; no files created outside this report and this seat's scratch dir.
- No installs.

Report: `.ufo/waves/round-60/w1-a3/ConnectSiblingsA3.md`
path: /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-60/w1-a3/ConnectSiblingsA3.md