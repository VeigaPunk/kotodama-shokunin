# ScoutSurface96 — round 96, coverage surface + adjacency for claim C

Seat: ScoutSurface96 (scout; axes coverage, adjacency). Milestone r96-v1.
Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`. Base `0539276c0e329743200b60e98bf289c540f78864`.
Deliverable: `.ufo/waves/round-96/w1/stage/ScoutSurface96/surface.md` (27146 B,
sha256 `14cffabecc777cc6633fbdb7c19a69ab3fec2fc12f13d181dce30f9e8c529399`).
Read-only seat: nothing in the lane repo was created or edited except this seat's own stage and
this report. Scratch mirror deleted at yield.

## Zero-owner evidence (claim C "before" holds)

| Command (from lane root) | rc | Result |
|---|---|---|
| `ls corpus/knowledge/*/ \| grep -i -E 'oath\|curse\|bless\|malediction\|imprecat\|vow\|swear\|sanction\|witness'` | 1 | no output |
| `find corpus/knowledge -type f \( -iname '*oath*' -o -iname '*curse*' -o -iname '*bless*' -o -iname '*maledict*' -o -iname '*imprecat*' -o -iname '*vow*' -o -iname '*swear*' -o -iname '*sanction*' -o -iname '*witness*' \) -print` | 0 | no output |
| `git ls-tree -r --name-only 0539276c… corpus/knowledge \| grep -i -E 'oath\|curse\|bless\|malediction\|imprecat\|vow\|swear\|sanction\|witness'` | 1 | no output (base tree) |
| `find corpus/knowledge -name '*.md' \| wc -l` | 0 | 267 (== base tree 267) |

Coverage map `corpus/README.md`, per-term `grep -n -i -E '<term>'`: oath 6 (rc=0, lines 408/431/624/873/875/876),
curse 2 (rc=0, 408/449), blessing 2 (rc=0, 408/536), imprecation 1 (rc=0, 408), vow 3 (rc=0, 385/460/970),
malediction 0 (rc=1), swearing 0 (rc=1). The `## Known gaps (frontier)` block (lines 638–817) has
0 hits for the vocabulary (rc=1). Registry `teaches` cells: 6 non-owning hits (S839, S840, S901,
S902, S945, S950) out of 898 parsed rows.

## Adjacency (full table in surface.md §3)

Nine files carry the vocabulary in their `- topic:` line; **none owns the formula-grammar surface**.
Closest owner is `myth-symbol/binding-speech-complex.md` (touch ranges: oath 99–139, curse 140–167,
blessing 168–179, name-power 180–195, enforcement ledger 196–219, release 220–235, master table 85–98,
boundary 39–59, canon 301–305) — it owns the *myth-side machinery and executor doctrine*, not the
linguistic formula grammar. Boundary: the new entry owns formula grammar; that entry owns who
executes and what happens; defer, do not restate.
Other owners and boundaries: `register-strata-attestation.md` (register law, 58/68–69/88/134–136/195/204/230–236/265/373);
`sacred-registers-liturgical-language.md` (§1 26–40, §7 113/115); `politeness-taboo-euphemism.md`
(75/78/102/106/115); `naming-systems.md` (§4 73–79, §6 87–108, 105); `semantics-pragmatics.md` (94);
`taboo-strata-lifecycle.md` (14); `ritual-liminality.md` (33/112); `creation-myths-taxonomy.md` (104);
`guest-right-hospitality-law.md` (16/34–35/101/119); `ordeal-judicial-proof-rituals.md` (3/6/7/14/25–26/70–71/148);
`witchcraft-sorcery-accusation-institution.md` (3/6/17/34/70–71/148); `sacred-kingship-mythic-charter.md` (topic);
`scythian-saka.md` (topic); `hair-grooming-codes.md` (topic, 22); `religion-language-co-evolution.md` (36).
Zero-touch (no boundary needed): `kinship-terminology.md` (grep -c → 0, rc=1) and
`sumptuary-law-rank-display.md` (grep -c → 0, rc=1). False positives ruled out:
`craft-artisan-lexicon.md` ("build-curses"), `verification-independence-anti-circularity.md`
("bless-the-tamper"). **No contested scope.**

## Skeleton (surface.md §4)

Ten h2: 1 Scope/ownership+deferral · 2 The oath formula · 3 The blessing formula ·
4 The curse formula · 5 The witness invocation · 6 The sanction clause · 7 Registers
(sacred/legal/everyday) · 8 Master grammar table (6 data rows × 5 cols) · 9 Error patterns ·
10 Design procedure and checklist. Each of the six frozen phrases lands in its own numbered h2
with ≥ 2 content tokens (grader `_content_toks`, v6 NUM1/RM1/NUM2), and three repeat in table cells,
so the counter's C1 and the grader's `min_anchor_span` rule both clear.

## Planner data-walk (partition counts)

`find corpus/knowledge -name '*.md' | awk -F/ '{print $3}' | sort | uniq -c` (rc=0):
95 civilizations · 43 culture-material · **40 linguistics** · 36 myth-symbol · 29 synthesis · 24 verification (total 267).
New entry → **linguistics** (40 → 41): the frozen path is `corpus/knowledge/linguistics/oath-blessing-curse-formulae.md`;
the frozen topic is a formula grammar, and the four sibling formula entries live in this partition
(`find corpus/knowledge -name '*formula*'` → 5 linguistics files); `myth-symbol/` already holds the
enforcement-side owner.

## Verified recipe for the index leg (C5)

`corpus/README.md` needs four edits, each verified on a scratch mirror of the base tree:
before → `CORPUS-INDEX: FINDINGS files=268 rows=267 findings=5 ids=FOOTER_DIR_TOTALS,FOOTER_TOTAL,HEADER_DRIFT,MISSING_ROW,TOTALS_DRIFT` (rc=1);
after → `CORPUS-INDEX: OK files=268 rows=268 findings=0` (rc=0), and the frozen counter then prints
`LEG C1 PASS bytes=51952 h2=7 table=6x3 phrases=6/6 topic-line=equal` and `LEG C5 PASS index rc=0`.
Edits: (a) index row inside `## linguistics/` with the topic text verbatim after `— ` (the checker
compares README row to the file's topic field, `TOPIC_MISMATCH`); (b) header `(40)` → `(41)`;
(c) `Total knowledge entries: 267.` → `268.`; (d) last footer line → `(total 268 files; directory totals 41/36/43/29/24/95).`
plus a dated `## Round 96 …` footer block (`FOOTER_RE` takes the last "Counts checked" block).
Topic line must be one line: `- topic: ` + frozen text = 354 B (multi-line breaks the byte compare).

## Routing gap for the L1

**No round-96 seat is told to write `corpus/README.md`.** `ExecRegistry96` owns only
`corpus/SOURCES.md` and `reports/round-96/evidence/`; `ScribeEntry96` owns only the entry file.
Round 95's `ExecRegistry95` did own the README (its item step 5 built `stage/ExecRegistry95/README.new.md`
+ `README.diff`), and the L1 landed it in commit `feb94bc3`. Leg **C5** cannot pass without the
README bytes; the L1 is the only committer, so the bytes must be produced by a seat. The exact
recipe is in surface.md §5. Not written by this seat.

## Tooling

None installed or upgraded (no pacman — host-paused by orchestrator ruling; no uv/cargo/npm).
Only pre-existing tools used: grep, find, awk, sed, python3 stdlib, git read-only
(ls-tree/log/show/status), `tools/check-corpus-index.py`, `reports/round-96/predispatch.py`,
`tools/check-cited-lines.py` (rc=0, 0 findings on two reference entries), `scripts/sources-census.sh`
(lane file rc=0), `scripts/hyaku/disk-guard.sh status` (rc=0). No host sysctl touched.
