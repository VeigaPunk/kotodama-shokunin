# ResVerifyRows — final staged-row audit after the five RF repairs

Seat: `kotodama-r64.ResVerifyRows` (leaf; no subagent dispatch). Lane repo
`/home/vgpnk/Projects/shokunin/kotodama-shokunin`. This report is the lane's only write from this
seat. No row, counter, registry, entry, jj state, or git index was edited; no commit; no acceptance
counter or Rust judge was run. No tools installed or updated; pacman untouched.

Local times below are UTC-3 (2026-10-23 23:54 through 2026-10-24 00:00 local = 2026-10-24
02:54–03:00 UTC).

## What was audited, and against which bytes

Canonical command (the assignment's gate), run on the final bytes:

```
python3 -B .ufo/waves/round-64/check-rows.py --rows-dir .ufo/waves/round-64/rows
CHECK-ROWS: 32/32 clean        (exit 0; transcript: scratch/check-final.txt, mtime 23:59:21)
```

Custody (SHA-256 of the bytes actually read):

| Artifact | SHA-256 | Note |
|---|---|---|
| `check-rows.py` | `922c41c18251aa3ec1903bdc408e67f5587a37207f63c2b3473c4fe77680f8ee` | stable since 20:05 |
| `corpus/SOURCES.md` (770 lines) | `7a77cabcf633bc4868ac72807d88192092d21ed2db477f26aeee151d03009434` | identical to the critic's registry snapshot; unchanged across this audit |
| `reports/round-64/accept-c.py` | `979050ce21fa01758c075745b08bf3ecf7d6e73baad543a1df83f666ecc5de2b` | read, not run; file was edited at 23:56:55, citations below are to these bytes |
| `integrate-w2.py` | `3ea312cdfb7f322945d339c25ddda42616935ec56b4cbe4d63ba6916c6837b50` | read for row-ingestion contract |

Three snapshots were taken of all 32 `row.txt` files: v1 23:56:55, v2 23:57:44, v3 23:59:15.
`v3 == v2` byte for byte, and a post-checker re-hash of all 32 rows matched the certified set with
**0 mismatches**, so the certified state is stable from 23:57:44 through 23:59:21 and the checker
read exactly the hashes recorded here.

**Concurrency at my start:** the five repair seats had not landed their corrections when I began
(23:54–23:56). S721/S726/S737 were still tier `A`; S723's teaches cell was still 44 whitespace
words; S740's was still 43. They landed **during** the audit — S723 at 23:56:54, the other four in
the window (23:56:55, 23:57:44]. I waited zero, audited what existed, and certify the resolved v2/v3
bytes. Post-repair hashes in the five seats' receipts (`ResFixS721.md:85`, `ResFixS726.md:47`,
`ResFixS737.md:65`, `ResFixS723.md:49`, `ResFixS740.md:82`) match my measured file-byte hashes
exactly.

## Final per-row verdict

| ID | tier | status | kind | teaches (ws / norm) | quote words |
|---|---|---|---|---|---|
| S718 | A | mined | paper | 15 / 16 | 9 |
| S719 | B | mined | paper | 18 / 20 | 24 |
| S720 | A | mined | paper | 18 / 20 | 24 |
| S721 | **B** | mined | paper | 12 / 13 | 18 |
| S722 | B | mined | paper | 16 / 17 | 17 |
| S723 | B | mined | docs | **15** / 15 | 13 |
| S724 | B | mined | book | 14 / 16 | 16 |
| S725 | B | mined | paper | 14 / 16 | 19 |
| S726 | **B** | mined | paper | 13 / 13 | 19 |
| S727 | B | mined | paper | 15 / 15 | 16 |
| S728 | B | mined | book | 10 / 10 | 14 |
| S729 | A | mined | paper | 20 / 23 | 20 |
| S730 | B | mined | book | 16 / 18 | 24 |
| S731 | A | mined | paper | 15 / 17 | 23 |
| S732 | B | mined | paper | 14 / 15 | 19 |
| S733 | A | mined | paper | 14 / 14 | 15 |
| S734 | A | mined | paper | 16 / 17 | 16 |
| S735 | A | mined | paper | 18 / 18 | 17 |
| S736 | A | mined | paper | 14 / 15 | 10 |
| S737 | **B** | mined | paper | 16 / 16 | 25 |
| S738 | A | mined | book | 13 / 13 | 20 |
| S739 | A | mined | paper | 12 / 12 | 20 |
| S740 | A | mined | paper | **14** / 15 | 22 |
| S741 | A | mined | paper | 13 / 13 | 12 |
| S742 | A | mined | paper | 18 / 18 | 23 |
| S743 | A | mined | paper | 16 / 18 | 10 |
| S744 | B | rejected | docs | 50 / 53 | 14 |
| S745 | A | rejected | docs | 31 / 32 | 11 |
| S746 | B | queued | docs | 43 / 45 | 17 |
| S747 | B | rejected | docs | 27 / 32 | 0 |
| S748 | B | queued | book | 42 / 45 | 11 |
| S749 | C | queued | community | 23 / 25 | 21 |

`teaches (ws / norm)` = whitespace split / the checker's own `norm_words` (NFKC, casefold, Unicode
nonword split). Mined rows: teaches **10–20** ws (bound 25), quote **9–25** normalized words
(bound 8–25). Disposition rows' cell 7 is the `REJECTED:`/`QUEUED-CANDIDATE: … ; flip:` verdict,
not a learner benefit — see LOW-3.

## The five corrections, verified on final bytes

Cell-level diffs pre-repair → final. In every row **only the allowed cells changed**; the source
cell, locator, anchor quote, BULLET, VERIFY/CAPTURE/ACCESS lines, status, dates and used-by are
byte-identical to the pre-repair row.

| Row | RF | pre | final | cells changed | final SHA-256 (file bytes) |
|---|---|---|---|---|---|
| S721 | RF1 | `A`; scope “infant vocal turn-taking and protoconversation…” | `B`; definition scope | 3 (tier), 4 (scope) | `6c4e32d8a6e0df0f4cd2c8571f8b4db23a07684498b35a2477ae9c8503b69f58` |
| S726 | RF2 | `A`; unqualified paradigm scope | `B`; abstract-reported scope | 3, 4 | `cda347814c7c2cc440f6ae3bc361090427defc13de02745f8f14dc4555d5f9c7` |
| S737 | RF3 | `A`; unqualified operational-definition scope | `B`; abstract-reported scope | 3, 4 | `3b4ba7f776153326ec77efbfab679d7565d8e30bf55446550c267d47e61fd5bd` |
| S723 | RF4 | teaches 44 ws / 44 norm | teaches **15 ws / 15 norm** | 6 (teaches) only | `2a76a8b04a7dde68a1c80a5b08e04cbda26df6faa7832bc5c73398a90517bcf9` |
| S740 | RF5 | teaches 43 ws / 45 norm | teaches **14 ws / 15 norm** | 6 (teaches) only | `e50673c41c119b070a1b98f4dd332537d2e629a9d39fad9b6d860c08dc7f54aa` |

The three tier corrections are the critic's smallest safe correction ("mark B with a scope
explicitly describing the evidence actually opened") and nothing more:

- **S721** — scope now: `the review's secondary literature-background definition of infant
  proto-conversation (citations to Hsu & Fogel 2003, Hsu et al. 2001, Kaye 1977), not its own
  synthesis result`. Honest: I fetched the recorded capture
  (`web.archive.org/web/20250212173742id_/…PMC9271548/`, HTTP 200, 313,768 B) and the quoted
  sentence is immediately followed by `(Hsu & Fogel, 2003; Hsu et al., 2001; Kaye, 1977)` inside
  the review's background section — so the row is B for a definition it reports from upstream
  work, not A for the review's own synthesis.
- **S726** — scope now: `ERIC abstract-reported claim of Ochs and Schieffelin's foundational
  language acquisition/socialization paradigm`. Capture opened (HTTP 200, 11,729 B): the quoted
  sentence is present and the record closes with the ERIC abstract marker `(MSE)`. Abstract-only
  evidence for a substantive claim ⇒ B under `corpus/QUALITY.md:29` criterion 6, matching the
  registry precedent S102 (`corpus/SOURCES.md:131`).
- **S737** — scope now: `ERIC abstract-reported operational definition of verbal play in Schwartz's
  study of young children's metalinguistic awareness`. Capture opened (HTTP 200, 11,124 B): quote
  present, record closes with `(BD)`; the row keeps its honest `ACCESS` line recording the linked
  full-text PDF `HTTP 404`. B is the criterion-6 answer; no full-text claim is made.
- **S723** — teaches now: `Worldbuilders can depict overextension as a child using one simple word
  for many different things.` (15 ws words; the critic's example verbatim). Grounded in the
  unchanged 13-word quote (`In overextension, children use a simple word to refer to many
  different things.`, verified present in the capture, HTTP 200, 9,543 B). Tier stays B.
- **S740** — teaches now: `Worldbuilders can model Japanese noun-title overgeneralizations as
  suggesting rule learning rather than input memorization.` (14 ws words; the critic's example
  verbatim, hedge retained). Grounded in the unchanged 22-word quote, verified present in the
  capture (HTTP 200, 243,294 B). Tier stays A per the critic's explicit non-finding (the paper's
  own corpus observations); nothing downgraded it by reflex.

Anchor re-verification used only the recorded archive captures with a plain curl
(`Mozilla/5.0 (research; row-audit)`); all five answered HTTP 200 and all five quoted sentences
were found verbatim. The live S740 host still returns the Cloudflare interstitial recorded in its
`ACCESS` cell, which is why the capture is the read path.

## Histogram (final, staged)

- New rows S718–S743: **A 14 / B 12**, all `mined`; kinds paper 21, book 4, docs 1.
- Disposition rows S744–S749: **rejected 3** (S744 B, S745 A, S747 B), **queued 3** (S746 B,
  S748 B, S749 C); kinds docs 4, book 1, community 1.
- All 32 staged rows: **A 15 / B 16 / C 1**; **mined 26 / queued 3 / rejected 3**.
- Delta from pre-repair: new rows were A 17 / B 9 (critic snapshot); post-repair A 14 / B 12.
  The only tier movement is the three A→B corrections; no other row changed tier.

## Uniqueness

- 32/32 rows carry exactly one live URL in the source cell, each with a same-page `id_` capture.
- Literal live-URL collisions across staged rows: **0**. Strict normalized collisions (NFKC,
  casefold, scheme removed, `www.` removed, trailing slash removed, **query retained**): **0**
  across 32 distinct normalized URLs.
- Live URLs found in `corpus/SOURCES.md`: **0** (strict). Any URL in any row cell, including the
  capture URLs, found in the registry: **0**.
- Query-insensitive (host+path only) hits are query-differentiated and therefore different
  records, not duplicates: S726 and S737 against registry S102 (`?id=EJ124326` vs
  `?id=ED252065`/`?id=ED149852`), and S729 against registry PLOS rows (`e0326569` vs `0283218`,
  `0287101`).
- Work identity beyond URLs: no staged title pair reaches Jaccard ≥ 0.5 on content tokens; only
  two rows carry DOIs and they do not overlap; no shared rare-token signature. The critic's
  S718/S729 same-work pair is **resolved** — S729 now cites Neer et al. 2025, PLOS ONE
  `e0326569`, a different work from S718's Farran et al. 2016 `e0151518`. S728 remains the only
  Kaluli/elema row.

## Findings

### MEDIUM-1 — the teaches ≤25 bound has no mechanical gate; the 32/32 line does not cover it

`check-rows.py:97–157` validates cells, tier, status, dates, used-by, quote length, capture
identity, BULLET shape and BULLET↔quote overlap; it never measures the teaches cell.
`accept-c.py:187–229` (ROWS leg) and `:249–251` (REJECTS leg) likewise measure no teaches length
(the only length check is `accept-c.py:213`, the 8–25 quote bound).

Direct evidence that the green line cannot carry this claim: my **first** checker run in this
audit, before the 23:56:54/23:57:44 edits, printed `CHECK-ROWS: 32/32 clean` while S723's teaches
cell was 44 words and S740's was 43. The post-repair 32/32 is not the evidence for RF4/RF5 — this
seat's independent whitespace count (15 and 14) is. No row edit and no counter edit from me: the
fix belongs to the counter owner if round 65 wants the bound mechanized.

### MEDIUM-2 — checker URL identity is literal for duplicates and query-blind for captures

- Duplicate detection keys on the **raw** first URL string
  (`check-rows.py:117`, group check at `:160`), while `norm_url` (`:49–66`) is used only for the
  capture comparison. Two spellings of one live URL (`http://www.example.org/x/` vs
  `https://example.org/x`) would therefore not collide.
- `norm_url` drops the query string. Running the checker's own function: both
  `https://eric.ed.gov/?id=ED252065` and `https://eric.ed.gov/?id=ED149852` normalize to
  `https://eric.ed.gov/`, so `capture_mismatch` cannot detect a capture that points at a different
  ERIC record on the same path. `accept-c.py`'s HOSTS and LINK legs (`:338–362`) are literal too.

Current staged bytes are clean under the stricter scan above (0 collisions, 0 registry hits), so
this is a gate-contract gap, not a defect in any row. It matters because the critic's stated axis
("normalized URL identity") is stronger than what the gate actually enforces.

### LOW-3 — disposition rows exceed 25 words in cell 7 by design

S744 50, S745 31, S746 43, S747 27, S748 42 (S749 23) whitespace words. The ≤25 rule is the
mined-row learner-benefit rule (`gen-w2.py:72`); these cells are the `REJECTED:` /
`QUEUED-CANDIDATE: … ; flip:` verdicts required by the REJECTS leg. Not a violation; recorded so
this column is not misread as six failures.

### LOW-4 — the used-by target is a string, not a file, at audit time

`corpus/knowledge/linguistics/language-socialization-and-acquisition.md` does not exist in the
lane yet. Both gates check containment only (`check-rows.py` usedby branch;
`accept-c.py:209`), so 32/32 does not prove the entry exists — `accept-c.py`'s FILE leg (`:161`)
is the leg that will. Expected pre-integration; recorded as a dependency, not a defect.

### LOW-5 — SHA custody conventions differ between seats

The critic's row-snapshot hashes are of the row text with the trailing newline stripped (verified:
S721 pre-repair text is 1 byte shorter than my file read; S726 matches because its file has no
trailing newline). A naive `sha256sum` of the file therefore disagrees with the critic's table by
construction. `ResFixS740.md:80–83` now records both conventions explicitly; future receipts
should name the convention whenever they publish a digest. The five post-repair hashes quoted
above are file bytes and match all five repair receipts.

### INFO-6 — S721's scope no longer names the coverage topic verbatim

The scope cell now describes the anchored definition rather than the topic phrase
("infant vocal turn-taking and protoconversation in early development"). No mechanical consumer
reads the scope cell (checker, `accept-c.py`, and `integrate-w2.py:95–124` validate cells, status,
used-by and the row shape, not scope), so nothing breaks; a final coverage census should read
S721's scope as the definition scope it now honestly claims, and the entry's §3 turn-taking
mapping is unaffected.

### INFO-7 — concluded no-action observations

- S747's `quote_words=0` is the intentional honest unreachable-record anchor; the bound applies to
  new rows only, so it is not a defect.
- All disposition rows carry used-by `—`, matching `integrate-w2.py:113`.
- ROW hygiene on all 32: 12 pipes / 11 cells, no double spaces, no untrimmed cells, no CR, no BOM;
  BULLET shape valid for all 26 mined rows.

## Residual risk and verification gaps

- I ran the pre-integration checker only. `accept-c.py` was read, not run: it judges the integrated
  state (rows in `corpus/SOURCES.md`, the entry file), and at audit time the registry holds no
  S718+ row and `corpus/knowledge/linguistics/language-socialization-and-acquisition.md` does not
  exist. Claim admission remains with the canonical judge.
- Network evidence is point-in-time archive reads; I did not re-run the live-URL access for every
  row. The five repaired rows' captures were opened during this audit; the S740 live host remains
  Cloudflare-gated as its `ACCESS` cell already records.
- Concurrency: other seats edited rows before my v1 snapshot (S719/S722/S728/S729/S735/S739/S742/
  S747 mtimes 23:50–23:54) and the five repairs landed in the v1→v2 window; the certified state is
  v3. Any receipt quoting the critic's pre-repair S723/S740/S721/S726/S737 hashes is stale by
  construction, not wrong at its time.
- Scratch custody: `/home/vgpnk/.cache/hyaku/kotodama-r64-res/ResVerifyRows/` —
  `snapshot.json` (v1), `snapshot-v2.json`, `snapshot-v3.json`, `final-shas.json` (all 32),
  `check-final.txt` (full checker transcript), `rows/` (byte copies of all 32 rows as audited).
