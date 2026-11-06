# ExecRegistry99 — registry rows and evidence, kotodama round 99 (w1)

- seat: ExecRegistry99 (leaf, sole writer of `corpus/SOURCES.md` and `reports/round-99/evidence/` this round)
- dependency: `ScoutSources99/DONE` present (sha256 of `candidates.json`); read `candidates.json` (14 candidates, 11 admitted)
- base: 527df3fee305b3454446946e6779ece45456307e; counter run with `--base-rev` that value
- scratch: `/fast/scratch/hyaku/kotodama-r99/ExecRegistry99/` (removed at the end)

## Appended rows (11, S1007–S1017)

Appended at the end of the `## Registry` table, after S1006 (line 963), in candidate-key order.
Every row: 11 cells, tier A or B, status `mined`, opened `2026-11-06`, recheck `180d`,
used-by exactly `corpus/knowledge/linguistics/praise-poetry-panegyric.md`.

| id | key | source | tier | kind | quote (verbatim, count 1) |
|---|---|---|---|---|---|
| S1007 | C1 | Finnegan, Oral Literature in Africa ch. 5 "Panegyric" (OBP 2012, CC BY), Internet Archive copy | B | book | In return the ruler acknowledges their praise by gifts or money which are often given publicly. |
| S1008 | C2 | Opland, Lord of the Singers, Oral Tradition 3/3 (1988) | A | paper | it is his duty to greet Lord with a royal praise name |
| S1009 | C3 | Barber, Text and Performance in Africa, Oral Tradition 20/2 (2005) | A | paper | Obscurity in praise poetry could be deployed for political reasons. |
| S1010 | C4 | Groenewald, I Control the Idioms, Oral Tradition 16/1 (2001) | A | paper | The praise poem for kings and chiefs has also been adapted to serve the trade union movement |
| S1011 | C5 | Kaschula, Mandela Comes Home, Oral Tradition 10/1 (1995) | A | paper | directed at the Chief, decrying what was unworthy, praising what was worthy |
| S1012 | C7 | Pindar, Extant Odes, trans. Myers, Gutenberg #10717 | A | book | Yet praise is overtaken of distaste, wherewith is no justice, but from covetous men it cometh |
| S1013 | C9 | Y Gododdin, trans. Williams 1852, Gutenberg #9842 | A | book | A more choice act of mine will be To celebrate thy praise in song |
| S1014 | C10 | Purananuru, English translation with introduction (archive.org copy) | B | book | The main themes found in Purananuuru are praise of the ruler, patronage, heroism in battles |
| S1015 | C11 | Kertzer, Trio Da Kali and the Mande Griot Tradition, World of Music | B | paper | the praise-singing function is by far the most obvious and audible manifestation |
| S1016 | C12 | Potts, Skaldic Poetry: A Short Introduction (Cambridge ASNC) | B | docs | There certainly was money in poetry for the skald; court poets would receive generous rewards |
| S1017 | C13 | Kavanagh, Signs and Wonders (Maynooth PhD thesis) | B | paper | a poet should not satirize or over-praise a subject, as the fili depended on the wealth of his patron |

Scope/teaches cells keep the boundary: `corpus/knowledge/linguistics/orality-formulaic-language.md`
section 3 owns praise-names as formula lexicon (Parry epithet sets, makura-kotoba); these rows teach the
institution (patronage and reward, the singer's office and audience reply, licensed criticism, the limits
of flattery, the bard circuit, griot role lists, skaldic reward) and never restate the epithet mechanism.

## Re-verification performed by this seat

- Re-fetch: plain `curl -L --max-time 30 -sS` with the default user agent, one attempt per URL unless
  transient. All 11 admitted URLs returned HTTP 200 on attempt 1 (rc=0). C6 returned HTTP 403 (Cloudflare
  shell, 5539 bytes, 1 attempt). C8 returned curl rc=28 (connect timeout, 0 bytes) on 4 attempts
  (1 + 3 retries at 20 s backoff).
- Fresh sha256 equals the shipped capture for every direct-file URL: C1 `73df25c2…` (1431723 B),
  C2 `82e20d08…` (122076 B), C3 `67933059…` (895589 B), C4 `c04fa91b…` (941966 B), C5 `680667fd…`
  (678241 B), C7 `d8823d13…` (320993 B), C9 html `1c058141…` (412673 B), C11 pdf `3ae6a081…`
  (121791 B), C12 pdf `9d5bc813…` (294812 B), C13 pdf `73809a35…` (1897884 B).
- C10's stream page returned 184993 bytes to this seat against the scout's 191267-byte capture (page
  changed between fetches); the quote counts 1 in the fresh bytes and 1 in the shipped capture, so the
  row stands and the byte difference is recorded in `rows.md`.
- Every scout capture was re-hashed against `candidates.json`: 20/20 match on bytes and sha256.
- Quote recount: `re.sub(r"\s+"," ")` collapse of each named `.txt`, `str.count` — every one is 1.
  Nothing was written that failed a check; the three non-written candidates are in `dropped.md`.

## Commands and numbers

| command | result | rc |
|---|---|---|
| `grep -cE '^ {0,3}\|[[:space:]]*S10(0[7-9]\|[1-9][0-9])' corpus/SOURCES.md` (before) | 0 | 1 |
| same grep (after appending) | 11 (my own rows only; no pre-existing S1007+) | 0 |
| `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` before / after | 930 / 941 | 0 |
| `bash scripts/sources-census.sh validate --file corpus/SOURCES.md` | no E lines, E-count 0 (30 pre-existing W04 warnings, none on my rows) | 0 |
| full-tree `predispatch.py --root <lane> --base-rev 527df3fe…` (entry present) | `PREDISPATCH-99: FAIL legs=14/16` (C9 only, ReviewerC99's file absent) | 0 |
| C-only `predispatch.py --root <fastroot> --base-registry <base SOURCES.md> --base-rev 527df3fe…` | C1–C8 PASS, C9 FAIL (ReviewerC99's file absent); `legs=8/16` because the O legs cannot run in that root by construction (no `tools/check-advance-evidence.py` there) | 0 |

The full-tree run was repeated after the scribe's `DONE`; it stalled in O6 (mutation99) under fleet load,
so the C legs were measured independently in a fast root that symlinks `corpus/`, `reports/round-99/evidence/`,
`.ufo/waves/round-99/w1/` and `tools/check-corpus-index.py`, with `--base-registry` holding the base bytes
(`git show 527df3fe:corpus/SOURCES.md`, rc=0, 1087015 B). Both runs read the same final entry bytes
(44922 B, mtime 2026-11-06 01:18:24 -0300, unchanged after ScribeEntry99 wrote `DONE`).

Counter lines (exact, C-only run):

```
LEG C2 PASS rows=941 highest=S1017 new=11 qualifying=11 (min rows 934, highest >= S1010, qualifying >= 4)
LEG C3 PASS added=11 removed=0 in-place-status/recheck/used-by=0 illegal=0 []
LEG C4 PASS census rc=0
LEG C5 PASS index rc=0 last: CORPUS-INDEX: OK files=271 rows=271 findings=0
LEG C6 PASS qualifying ids cited in entry: 11/11 uncited=[]
LEG C7 PASS qualifying ids bound: 11/11 captures-verified=20 failures=[]
LEG C8 PASS files scanned=271 other owners=0 []
LEG C9 FAIL reopen file missing: .ufo/waves/round-99/w1/stage/ReviewerC99/reopen.json
```

C9 is not this seat's leg: `ReviewerC99` writes `.ufo/waves/round-99/w1/stage/ReviewerC99/reopen.json`.
C1/C6/C4 depend on the entry written by ScribeEntry99 and were PASS at measurement time
(entry 44922 B, mtime 2026-11-06 01:18:24 -0300, all 11 ids cited).

## Evidence

`reports/round-99/evidence/` holds 20 captures plus `manifest.json` (JSON list, 11 entries):
`S1007.txt`; `S1008.pdf/.txt`; `S1009.pdf/.txt`; `S1010.pdf/.txt`; `S1011.pdf/.txt`; `S1012.txt`;
`S1013.html/.txt`; `S1014.html/.txt`; `S1015.pdf/.txt`; `S1016.pdf/.txt`; `S1017.pdf/.txt`.
Each manifest entry carries id, key, url, access, http, bytes, tier, status, used_by, quote,
quote_count, quote_capture, attempts (every attempt with http/rc/stderr) and captures
(file, url, bytes, sha256). The anchor cell of each row carries
`body text; reports/round-99/evidence/<id>.txt; exact locator: "<quote>"` with the quote
byte-identical to the manifest quote.

## Drops (detail in `dropped.md`)

- C6 Encyclopaedia Iranica, Courts and Courtiers x — HTTP 403 Cloudflare challenge; UNREACHABLE, no bypass.
- C8 Skaldic Project Óláfsdrápa introduction — 4 attempts, curl rc=28, 0 bytes; UNREACHABLE.
- C14 Gourlay, Long Trumpets of Northern Nigeria — HTTP 200 but REJECTED on anchor scope (trumpet article;
  praise-singer passage a six-line aside). Quote verified count 1; not written.

## Discipline

- No git/jj mutation; no commit. Read-only `git rev-parse/status/log` only.
- Wrote only `corpus/SOURCES.md`, `reports/round-99/evidence/` (20 captures + manifest.json), and this
  seat's stage dir (`rows.md`, `rows.json`, `rows.lines`, `dropped.md`, `census.txt`, `DONE`).
- Never edited `claims.json`, `predispatch.py`, `battery99.py`, `battery99.sha256`, any control receipt,
  or anything under `reports/round-99/controls/`.
- Tooling installed or upgraded: none. No pacman, no sysctl.
- Scratch `/fast/scratch/hyaku/kotodama-r99/ExecRegistry99/` removed before yield.
