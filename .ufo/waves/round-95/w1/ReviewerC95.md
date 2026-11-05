# ReviewerC95 — seat report (stage trailer)

Stage dir: `.ufo/waves/round-95/w1/stage/ReviewerC95/`
Scratch: `/fast/scratch/hyaku/kotodama-r95/ReviewerC95/` (removed before yield, trap
`rm -rf -- "$S"` semantics; nothing under /tmp was citable; disk guard checked twice,
both clean).

Verdict: `REVIEWER-C-95: PASS legs=5/5`

## What was measured (every count with its command and rc)

Dependencies (bounded wait, ran to completion, no BLOCKED):
```
for i in $(seq 1 45); do all=1; for d in ExecRegistry95 ScribeEntry95 ScribeLesson95; do
  [ -f <stage>/$d/DONE ] || all=0; done; [ $all = 1 ] && break; sleep 60; done
  -> wall 2640 s, rc 0, all three DONE present
```

Leg 1 — captures (both files per row, `sha256sum`, rc 0):
```
S970.txt dc7394e9862003b0b26e7631520e3dcb19832d25b19ddd4e6898cda06c371316
S970.pdf e8fb753b6b3adf3fe45075604e36e6c20034c5432748d19dd26aeb36465d3a8e
S971.txt 656c45388dbfcab8f9de8a233eada5d8f8571647a1f04955605bff71cbc4a26a
S971.pdf 85b821c7233c85bf1d3907b5db5ce98d368d19f6a06cdacc029a7df628345fbe
S972.txt d3ff0209b9d80418bcc9345535f5fd440a3fc8a2433da6982c42a65d777293ce
S972.pdf 1e0b0f8d8b529aae60ff2138d591aeb40465e778d11702b88b176d68334b30c8
S973.txt e017b3958dac14b32ff08a11f1750638e997c5df43ec9674a91413f5c42cac76
S973.pdf 8750510347c20a3ef8a12112435cc917c2737a42a4ffeadab3f85b557720a5d9
S974.txt 251b4d3f420164baa4bdc6508e54736cb0d00a42bc66940363203c264060159d
S974.pdf f1e4be9fd0868713bf363ea18b368a501dd48d87dc7bd3039e801f4954ad2672
```
All ten match the Gate table in `ScribeLesson95/round-95.md` byte-for-byte.

Quotes (Python `.count()` on the raw capture bytes; `len(q.split())` word counts):
| row | table quote | occurrence count in own .txt | words declared/measured |
|---|---|---|---|
| S970 | `the antiphonal way of performing Seto songs` | 1 | 7 / 7 |
| S971 | `The antiphonal nature of voceru performance` | 1 | 6 / 6 |
| S972 | `Professional keeners took over.` | 1 | 4 / 4 |
| S973 | `was important in the role of the female professional mourner` | 1 | 10 / 10 |
| S974 | `ends with a refrain exclamation` | 1 | 5 / 5 |
Bullet-line longer spans: 14/15/8/12/11 words, each count 1 in own .txt, rc 0.

Spot-reopen (plain `curl -L --max-time 30`, default UA, rc 0):
```
url=https://sciendo.com/pdf/10.2478/jef-2025-0006 http=200 bytes=950971
type=binary/octet-stream
sha256 = e8fb753b6b3adf3fe45075604e36e6c20034c5432748d19dd26aeb36465d3a8e
```
Byte-identical to the committed `S970.pdf` capture → re-opened quote still present.

Leg 2 — entry:
```
wc -c <entry>                        -> 50148
grep -c '^## ' <entry>               -> 12
python reimplement of predispatch C1 -> bytes=50148 h2=12 table=11x5 phrases=6/6
                                       topic-line=equal   rc 0
python3 -B tools/check-cited-lines.py <entry>
                                     -> CITED-LINES: 0 finding(s) in 1 file(s)  rc 0
```
Grader v5 entry-mode (`tools/check-advance-evidence.py entry --entry … --lesson …
--capture-dir captures --base-registry base --lands-registry my-mirror --manifest
<scratch> --as-of 2026-11-05`, claim `frozen_topic` via --topic):
`ENTRY-EVIDENCE: PASS legs=8/8`.
Strongest run, grader v6 bytes (`ExecGraderV6/v6-candidate.py`) + `--base-lesson`
(the frozen base-tree round-94 lesson bytes, out of the archive):
`ENTRY-EVIDENCE: PASS legs=9/9` (all nine legs at the claimed floors).
All five filename stems (`funerary`, `lament`, `dirge`, `formulae`, plus the compound
stems) appear as words in the entry prose.
Cited ids S970–S974: 5/5 present in `ExecRegistry95/SOURCES.append.md`, rc 0.

Leg 3 — registry and index (over my own rebuilt mirror, hanging off the live tree's
cold start, not the sibling's scratch):
```
git show 19aa4dd…:corpus/SOURCES.md > base            -> rc 0
append ExecRegistry95/SOURCES.append.md before ## Paths -> 893+5 = 898 rows
bash …/sources-census.sh validate --file <mirror>/corpus/SOURCES.md
    -> ok (E-codes: 0 ; W-codes: 35 = the same 35 pre-existing base warnings)  rc 0
python3 -B tools/check-corpus-index.py --root <mirror>
    -> CORPUS-INDEX: OK files=267 rows=267 findings=0                        rc 0
diff -u README.md README.new.md
    -> +24/-1: 8 header-block lines, 1 entry-row, `## linguistics/ (40)` swap,
       +14 trailing-lines  (only the declared lines)
```
Tier A 5/5, status mined 5/5, opened 2026-11-05 5/5, used-by = the entry path 5/5.

Leg 4 — lesson gate:
```
python3 -B tools/check-gate-quotes.py <round-95.md>   -> GATE_QUOTES: 0 findings, rc 0
python byte-== anchor quote vs Gate quote (5 rows)    -> True/True/True/True/True, rc 0
awk '/^## Gate/{g=1;next} /^## /{g=0} g' lesson | grep -E '^- ' | grep -vE '^- S[0-9]+ admit'
                                                     -> 29 bullets
… | grep -viE 'reason|because|off-topic|...|scope|population'
                                                     -> 0
```
(as calibration, the same 0-finding sweep on the committed round-94 lesson).

Leg 5 — verdict + files:
`REVIEWER-C-95: PASS legs=5/5`; `stage/ReviewerC95/review.md` (short twin) and
`reports/round-95/w1/ReviewerC95.md` (the graded trailer, this file at its
relative path) written; `DONE` written last = `sha256(review.md)`.

## What I could not measure, and why

1. The three prose-count arithmetic identities inside the round-95 lesson Gate
   (27 = 25+2; 265 = 263+2; 265 = 253+12) are stated, not re-derived — verifying
   them would require the raw API JSON captures, which no seat staged inside a
   stage-visible dir (they are recorded only in the lesson prose itself). UNMEASURED,
   routed in review.md `## Leg 4` — not a claim-C leg.
2. `reports/round-95/evidence/manifest.json` is not staged by any seat (R95-M5,
   already routed to the L1): to drive the **frozen** grader entry-mode probe over
   the same five artifacts I had to stage a reviewer-side manifest (`manifest95.json`)
   built byte-for-byte from the lesson Gate table; both v5 (8/8) and strongest v6
   (9/9) runs against it are recorded above and the manifest lives only in my
   scratch, never under `reports/`.

## Tooling authorization / uninstall

None used beyond what was already present (`curl`, `sha256sum`, `gawk`, `python3`,
`git read-only`, plain file tools). Nothing installed, nothing updated, no pacman
transaction, no sysctl write. Scratch removed before yield (review repro scripts
`review_c.py`, `build_manifest.py`, and the mirror live only in the deleted
`/fast/scratch/hyaku/kotodama-r95/ReviewerC95/`; their final full outputs are in
`review.md` and here).

## Residual risk (as a reviewer, for the record)

- S975–S981 remain scout-only captures (12 staged − 5 landed = 7 not landed;
  R95-M6 routes the reason-recording to the L1). The five landed rows jointly
  cover all six frozen sub-topic phrases (S970+S971 antiphonal, S972 professional
  keeners, S974 lament refrain + praise of the dead, S973 female professional
  mourner/gendered rules, plus the entry's own design-procedure facet) — nothing
  in the frozen legs is weakened, it is a numerator question, not a defect.
- Grader v5-vs-v6 stability of the entry legs: entry runs were re-run with
  `--base-lesson`, `--as-of` and the claim topic (`--topic`) against both the
  frozen v5 bytes and the staged v6 bytes; no leg flips between the two
  (`PASS 8/8` v5, `PASS 9/9` v6). No O-side artifact was relied on except the
  v6 candidate's byte-identity receipt from ExecGraderV6 (informational only).
