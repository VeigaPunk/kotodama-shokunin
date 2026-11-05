# ScribeEntry — round 93 coverage draft

Seat: ScribeEntry (leaf, no dispatch). Lane: kotodama-shokunin. Lane wiki: `.ufo/waves/round-93/w1/ScribeEntry.md`. Milestone: r93-v1.

## Draft path

`/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-93/w1/stage/ScribeEntry/greeting-leave-taking-formulae.md`

The L1 copies this file to `corpus/knowledge/linguistics/greeting-leave-taking-formulae.md` after checks. I wrote nothing outside my stage dir and this report file.

## Numbers measured (2026-11-05)

| measure | command | value | floor |
|---|---|---|---|
| byte count | `wc -c greeting-leave-taking-formulae.md` | 21036 | 14000 (seat) / 12000 (claim C) |
| h2 headings | `grep -c '^## ' greeting-leave-taking-formulae.md` | 8 | 8 (seat) / 6 (claim C) |
| table data rows × cols | parsed pipe rows (8 pipe lines, header + separator excluded) | 6 × 5 | 5 × 3 |
| data rows containing "greeting" or "politeness" | same parse | 6 of 6 | — |
| prose/topic content-word overlap | `check-advance-evidence.py` `overlap()` on non-heading non-table lines vs the frozen topic | 15 | 10 |
| sub-topic phrase anchors | `check-advance-evidence.py` TOPIC logic (greeting, leave-taking, formulae, politeness) | 4/4 phrases, spanning 5 heading/table surfaces | 4 phrases, span 3 |
| filename stem words present in text | `greeting`, `leave`, `taking`, `formulae` | 4 of 4 hit | ≥1 |
| worst repeated prose sentence | `check-advance-evidence.py` `sentences()` + count | 1 | ≤2 |
| duplicate prose lines | line-exact duplicate scan | 0 | — |
| cited-lines findings | `python3 -B tools/check-cited-lines.py <draft>` | `CITED-LINES: 0 finding(s) in 1 file(s)`, rc 0 | 0 |

## Commands run, with rc

- `python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/tools/check-cited-lines.py <draft>` — rc **0**, output `CITED-LINES: 0 finding(s) in 1 file(s)`. Findings: zero, nothing to explain. No line carries two distinct S-ids; no table row carries an S-id.
- `wc -c <draft>` — rc 0, 21036 bytes.
- `grep -c '^## ' <draft>` — rc 0, 8.
- `curl -sS -o /dev/null -w '%{http_code}' -L --max-time 40 <url>` for each of the four source URLs — rc 0 overall; all four returned **200** (ordinary HTTP, default user agent, no TLS bypass, no login, no browser):
  - `https://bop.unibe.ch/linguistik-online/article/view/1426` → 200 (S961)
  - `https://pressto.amu.edu.pl/index.php/srp/article/view/21548` → 200 (S962)
  - `https://bop.unibe.ch/linguistik-online/article/view/3847` → 200 (S963)
  - `https://oaj.fupress.net/index.php/ss/article/view/17732` → 200 (S964)
- Python (stdlib only, reading the committed captures) — rc 0: each of the four manifest quotes is an exact substring of the captured text; each quoted span used in the draft is an exact substring of the corresponding capture; quoted spans map 1:1 to S961/S962/S963/S964 with no cross-source reuse.
- Python re-using the frozen `tools/check-advance-evidence.py` `overlap()`, `table_shape()`, `sentences()`, `words()` helpers — rc 0, for the numbers tabulated above. No production file was modified; the tool was imported read-only.

## What the draft contains

- Header block exactly as specified: `# Greeting and leave-taking formulae`, blank line, the frozen `- topic:` line verbatim, `- sources:` with one id per line (`S961 Rash 2004`, `S962 Zieliński 2019`, `S963 Mapunda and Sommer 2017`, `S964 Trubnikova 2025`), `- verified-at: 2026-11-05`, `- recheck: 180d`.
- Eight h2 sections in the required order: scope and the four sourced cases; greeting and leave-taking as one speech-act family; form and meaning in the kissing-hands pair; politeness and access rituals under contact; leave-taking formulae elicited as a pool; formulae in a register design; the sourced cases at a glance (the table); limits and open questions.
- One markdown table, 6 data rows × 5 columns, each data row naming either a greeting or a politeness property, with each row bound to its own source on a separate cited line below the table.
- Every prose line either carries exactly one S-id or carries the literal `(design, not sourced)` label and no S-id. Verified by scan: zero uncited-and-unlabelled prose lines, zero multi-id lines, zero S-ids in table rows.
- The entry is non-canon: §1 states it asserts nothing about canon, lore acceptance, real-world rights or cultural permission, and the closing limit repeats that standing condition.

## Source discipline

Each S-id was used only inside what its own abstract and quoted span support: S961 for German-speaking Switzerland (greeting and leave-taking as one politeness type, the grüssen verb, retention of politeness rituals, cohesion/respect/affection motive, formulae especially important); S962 for Spanish (two kissing-hands formulae from one atelic predicate, opposite socio-pragmatic values, epistolary texts to the beginnings of the 20th century, three analytic questions); S963 for Tanzanian Ngoni (access rituals verbal and visual, three methods, brevity and code-switching under pervasive contact with Swahili, generational split over respect); S964 for the Russian pilot study (situationally bound questionnaire, pool of farewell items for acquaintances and strangers, context-sensitive partings, familiarity / elapsed time / anticipated separation). One short quote per source, each an exact substring of the corresponding capture.

## Out of scope (not done here, and why)

- Registry rows for S961–S964 in `corpus/SOURCES.md` (with `used-by` naming the entry) and the `corpus/lessons/round-93.md` gate/disposition lines are production files, read-only for this seat; the L1 integrates them. At base there is no `S961`–`S964` row in `corpus/SOURCES.md` (grep count 0), so the NEWIDS leg depends on the L1's landing, not on this draft.
- The unreachable candidate (`reports/round-93/evidence/unreachable-mdpi-403.raw`, HTTP 403 Access Denied from the publisher's edge) is named in §8 as not evidence. It is not quoted, not counted, and carries no S-id.
- No canon, lore, rights or permission claim appears anywhere in the draft.
- No tool was installed or upgraded for this seat; no pacman, sysctl or PATH-directory write was performed.

## Findings and limits I could not resolve

1. The four sources are abstracts and landing pages, not full texts; every sourced claim is confined to what the captured abstracts state. Each of the four cases carries an explicit confinement line in §8. This is the main evidential limit of the draft.
2. S964 is a pilot study by its own abstract, and S962 is a historical case from epistolary texts up to the beginnings of the twentieth century, so neither supports a synchronic claim; both limits are stated in §8 with their own S-ids.
3. The four-source base is narrow for a topic spanning two speech acts, several politeness traditions and a contact situation; §8 says so explicitly and refuses a typology reading.
4. Unreachable candidates are not evidence; the 403 response is reported by what it was (an HTTP 403 Access Denied page from the publisher's edge) and no inference is drawn from it.
5. I did not verify the SHAPE/NEWIDS/BASEROWS/GATE/CAPTURE legs of claim C end to end, because those legs measure the L1's landed tree (registry rows, lesson, index and census), which does not exist yet. The entry-mode metrics that depend only on the draft (bytes, h2 count, header keys, table shape, repetition, topic overlap, phrase anchors, stem words) were measured directly and are tabulated above.

## Artifact paths

- Draft: `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-93/w1/stage/ScribeEntry/greeting-leave-taking-formulae.md`
- This report: `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-93/w1/ScribeEntry.md`
- Evidence read (not written): `/home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-93/evidence/{S961,S962,S963,S964}.html`, `manifest.json`, `unreachable-mdpi-403.raw`
