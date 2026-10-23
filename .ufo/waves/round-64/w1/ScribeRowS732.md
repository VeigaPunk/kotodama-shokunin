# S732 — Heritage-language shift in immigrant-family childhood

## Behavior and evidence
The row records the bounded observation that bilingual children in immigrant households sometimes avoid the family's heritage language for the majority language. It supports a child language-use shift mechanism, not a claim that the cited children were directly measured to have lost previously acquired ability.

Source: Erika Hoff, “Bilingual Development in Children of Immigrant Families,” *Child Development Perspectives* 12(2) (2018), 80–86; open author manuscript in PubMed Central, PMCID PMC5966288. The body paragraph is under “Effects of Children’s Output on Bilingual Development.” The citation is Tier B: this is a peer-reviewed review synthesizing prior work, not an original study reporting this specific finding. The scoped claim is limited to majority-language preference/avoidance in immigrant-family child language use.

ROW: | S732 | Hoff, 2018 "Bilingual Development in Children of Immigrant Families", Child Development Perspectives, 12(2), 80–86 - https://pmc.ncbi.nlm.nih.gov/articles/PMC5966288/ ; capture https://web.archive.org/web/20261003105239id_/https://pmc.ncbi.nlm.nih.gov/articles/PMC5966288/ | paper | B | children's choice between the family heritage language and majority language in immigrant households | Effects of Children’s Output on Bilingual Development: "bilingual children in immigrant households sometimes avoid using the family’s heritage language in favor of the majority language" | Helps learners model how social prestige can shape children’s language choices and family conversation. | mined | 2026-10-23 | 180d | corpus/knowledge/linguistics/language-socialization-and-acquisition.md |

BULLET: - Children sometimes avoid heritage language and favor majority-language speech, shifting family conversation. (S732)

VERIFY: LOCATED https://pmc.ncbi.nlm.nih.gov/articles/PMC5966288/

## Gates and checks
- The lane locator was run twice; both runs returned `LOCATED https://pmc.ncbi.nlm.nih.gov/articles/PMC5966288/`.
- `awk -F'|' '/^ROW:/ { print "ROW fields=" NF }' row.txt` returned 13 fields (11 cells); the selected quote contains 18 whitespace-delimited words.
- No round acceptance or product test suite was run. This is one row artifact only; it does not establish that claim C's full predicate passes.
- No tools were installed or updated.

## Exact source-access and check commands
- `curl -sL --max-time 60 -o /home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRowS732/hoff.html -w 'HTTP %{http_code}\n' 'https://pmc.ncbi.nlm.nih.gov/articles/PMC5966288/'` → `HTTP 200` on 2026-10-23 (plain GET/curl).
- `curl -s --max-time 60 'https://archive.org/wayback/available?url=https%3A%2F%2Fpmc.ncbi.nlm.nih.gov%2Farticles%2FPMC5966288%2F'` → `{"url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC5966288/","archived_snapshots":{"closest":{"status":"200","available":true,"url":"http://web.archive.org/web/20261003105239/https://pmc.ncbi.nlm.nih.gov/articles/PMC5966288/","timestamp":"20261003105239"}}}`. Capture facts: timestamp `20261003105239`; original `https://pmc.ncbi.nlm.nih.gov/articles/PMC5966288/`.
- `cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && python3 -B reports/round-61/reopen-quote.py 'https://pmc.ncbi.nlm.nih.gov/articles/PMC5966288/' 'bilingual children in immigrant households sometimes avoid using the family’s heritage language in favor of the majority language'` → `LOCATED https://pmc.ncbi.nlm.nih.gov/articles/PMC5966288/` (run twice, same output).
- `awk -F'|' '/^ROW:/ { print "ROW fields=" NF }' /home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRowS732/row.txt` → `ROW fields=13`.
- `printf '%s\n' 'bilingual children in immigrant households sometimes avoid using the family’s heritage language in favor of the majority language' | wc -w` → `18`.

## Touched surfaces, exclusions, and limits
- Created scratch artifacts: `/home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRowS732/row.txt`, `hoff.html`, `source.html`, and `study.html`.
- Created this requested report at `.ufo/waves/round-64/w1/ScribeRowS732.md`. No product source, corpus entry, registry, judge, or lane state was edited by this seat.
- An alternate 2025 preschool study (PMC12085098) returned no Wayback snapshot in the availability API, so it was not used; the selected Hoff source had a same-page available capture.
- No conflict or canonical Rust judge output was encountered. The evidence does not show that heritage-language preference necessarily causes attrition, and does not generalize beyond the source's reviewed immigrant-family context.

## Artifact paths
- Row payload: `/home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRowS732/row.txt`
- Audit report: `.ufo/waves/round-64/w1/ScribeRowS732.md`
