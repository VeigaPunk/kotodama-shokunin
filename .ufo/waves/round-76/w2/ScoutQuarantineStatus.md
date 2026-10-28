# Round 76 W2 — quarantine document overlap check

**Verdict: overlap found, not none.** Compared the 21-row kotodama slice with the complete current `corpus/SOURCES.md` at C landing `722e69ff6361aadf148cb46acbf6ac8fd147f59a` by document URL (the frozen map's join key is normalized document URL, not numeric ID). The current registry has five slice-document matches:

| Current lane row | Slice register row | Document identity | Standing verdict | Status in round 76 |
|---|---|---|---|---|
| S883 | S816 | `chinawriter.com.cn/n1/2025/0605/c404024-40494534.html` | REFUSED | Pre-existing round-75 bridge |
| S884 | S817 | `chinawriter.com.cn/n1/2022/1207/c404024-32582252.html` | REFUSED | Pre-existing round-75 bridge |
| S893 | S787 | `chinawriter.com.cn/n1/2023/0922/c404024-40083104.html` | REFUSED | Pre-existing round-75 bridge |
| **S894** | **S825** | `digital.archives.go.jp/search` | PRESENT | **New round-76 admitted row** |
| **S895** | **S776** | `openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=E107EA4DE9725EDF819F33C60A44B296` | PRESENT | **New round-76 admitted row** |

The two new overlaps are exact live-URL matches; each lane row also includes an archive capture of that same document. Slice source evidence: `shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md:118` identifies S776 and the openstd URL; `:134` identifies S825 and the National Archives URL. Standing verdict evidence: `reports/round-71/telemetry/quarantine-verdicts.md:14` (S776 PRESENT) and `:30` (S825 PRESENT). Current lane rows at the C landing are `corpus/SOURCES.md:849-850` (S894-S895). The admitted amendment cites S895 and S894 at `corpus/knowledge/culture-material/calendar-festival-systems.amend-2026-10-24.md:4-5`.

The other three matches are not round-76 additions: the round-75 lesson already explicitly records register S787 ↔ lane S893, S816 ↔ S883, and S817 ↔ S884 (`corpus/lessons/round-75.md`, `## Quarantine`, lines 137-140 and bridging paragraph). Their standing REFUSED verdicts remain unchanged. Round 76 adds the two PRESENT-document overlaps above; the quarantine verdicts themselves remain unchanged.

**Falsified round-76 statement:** the C-landing lesson says “No current candidate or new lane row is a slice document” (`corpus/lessons/round-76.md:39`) and lists S776/S825 as carried/not touched (`:43`, `:59`). The admitted rows S895/S894 are respectively those exact slice documents. The entry's Gate table and source headers establish they were admitted (`corpus/lessons/round-76.md:11-12`). This is a document-level overlap despite the distinct lane/register IDs; the W1 scout's ID-based conclusion does not establish document disjointness.

**Evidence basis and limits:** the W1 slice artifact records 21 IDs and the 10/7/4 standing histogram (`.ufo/waves/round-76/w1/ScoutQuarantine.md:7-14`); the round-71 verdict ledger supplies per-row verdicts. Compared all 820 S-rows in the committed C-landing registry against the slice's source URLs, normalizing away www and Wayback wrappers. Exact matches are the five shown; no additional slice-document match was found. The 21-row slice includes three unreachable entries whose IDs have a trailing-backtick artifact in the source register; they did not produce additional matches. No fetch, build, test, lint, formatter, install, or source edit was performed. Scratch was removed.
