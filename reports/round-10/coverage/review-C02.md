# R10-C12 — Reviewer of worker C02's linguistics entry (author-side review)

- reviewer scope: `reports/round-10/coverage/review-C02.md` only. No corpus, ledger,
  bookkeeping, canon, or promotion edits. Author-side review evidence only; not an
  admission decision and not independent promotion verification.
- assignment: `reports/round-10/targets.json` → `R10-C11..C20` ("Ten reviewers: one
  per authored entry (poll for it, max 20 min): verify frontmatter completeness,
  source resolvability (re-run the cited command or open the cited path/URL), no
  filler, no duplication of an existing entry; verdict
  `reports/round-10/coverage/review-<id>.md`").
- C02 is the second linguistics-partition author (`R10-C01..C10` seat split:
  linguistics ×3 = C01–C03, myth-symbol ×3 = C04–C06, culture-material ×2 = C07–C08,
  verification ×2 = C09–C10). Expected outputs: fragment
  `reports/round-10/coverage/C02.md` naming one new
  `corpus/knowledge/linguistics/<slug>.md` entry.
- round-10 declared baseline revision `9dc18ec1339bffd6f81e74f1a5742464ef578749`
  (`reports/round-10/claims.json:5`); worktree HEAD during this review
  `e3a1ec9435787328ac9f828f96cb6390e4916b8f` (round-10 availability attempt 3).
- date: 2026-10-17, UTC (local clock UTC-03:00). Poll window opened 21:26Z (60 s
  cadence, 20-min cap → ≈21:46Z) on `reports/round-10/coverage/C02.md` **and** a
  17th-or-later `corpus/knowledge/linguistics/*.md` file, so a landed entry is
  caught even when its fragment is late. All times UTC unless marked -03.
- environment: `TMPDIR=$PWD/.scratch` exported for every scratch-writing command
  (`/tmp` inode-exhausted in this fleet); all scratch under `.scratch/`.

## 0. Review status and verdict

**Verdict: PASS for the four mandated checks — frontmatter complete, sources resolve
substantively, no filler, no duplication — with two low-severity findings (F1 fixed
in-revision, F2 open as a schema note) and one pin warning (F3).**

C02's fragment `reports/round-10/coverage/C02.md` had **not** landed when this
review opened at 21:26Z, so the entry was identified by elimination and content:
`numerals-and-measures.md` cites `reports/round-10/coverage/C03.md` as its receipts
file and `language-shift-obsolescence-revival.md` cites
`reports/round-10/coverage/C01.md` (`grep -l 'coverage/C0[123]\.md'
corpus/knowledge/linguistics/*.md` → those two files only), leaving the remaining
linguistics seat, and the entry's `- source:` line claims the
`phonetics-phonology.md` §8/§10 gap that `reports/round-10/coverage/C03.md:15`
records C03 as *deliberately not* choosing ("`phonetics-phonology.md:76-77,
279-280` names three *other* prospective siblings (`sound-change.md`,
`tone-prosody.md`, `sound-symbolism.md`), each of which overlaps existing entries
(historical-linguistics, phonetics-phonology) — deliberately not chosen.").

**The fragment landed at ≈21:39Z and confirms the attribution independently:**
`reports/round-10/coverage/C02.md` opens "coverage fragment:
`corpus/knowledge/linguistics/sound-symbolism.md`", states worker "C02 (linguistics
author, second entry)", and pins the same revision this review is pinned to
(`4f14b05a…ddd5d`, "28,980 / 155"). It also reproduces the corrected sweep, the
partition gate reading and the decision-record inventory recorded below.

**Revision pin (F3).** The entry was edited three times during the review window:

| observed (UTC) | bytes | sha256 (first 8) | note |
|---|---|---|---|
| 21:35:14 | 28,538 | `dbc8339e` | first inspectable revision — sweep receipt defective (F1) |
| 21:37:45 | 28,948 | `17670f81` | F1 corrected by the author; corrected sweep re-run and reproduced |
| 21:38:07 | 28,980 | `4f14b05a` | **the revision all checks below are pinned to** |

Any later edit invalidates the pin; §8 gives the re-run set. This is mid-wave churn,
not a defect — but a reviewer verdict must name its bytes.

## 1. Artifact under review

| item | value |
|---|---|
| entry path | `corpus/knowledge/linguistics/sound-symbolism.md` |
| title | *Sound Symbolism — Iconicity, Ideophones, and the Sound–Meaning Interface* |
| bytes / lines | 28,980 / 155 (`wc -lc`; the review harness prints 156 because it counts a final unterminated line) |
| sha256 (pin) | `4f14b05a7df542ad5e3dca39c20cb02dc3f5745c70395418770da93794fddd5d` |
| mtime | 2026-10-17 18:38:07 -03 |
| git status | untracked (`?? corpus/knowledge/linguistics/sound-symbolism.md`) — pre-admission, so an in-place fix by its author is still available |
| partition baseline | 179 entries at round-10 open (linguistics 16, myth-symbol 16, culture-material 16, verification 13, synthesis 24, civilizations 94); corpus tree sha256 `c5f81f68f88b295c726fd75231bde44169f601fa5ffe6c6c722140ab2a15e8e9` |

## 2. Frontmatter completeness — PASS

Criterion: the round-10 claim (`claims.json` C) requires "complete
`source`/`verified-at`/`recheck` frontmatter"; the house profile the 16 committed
linguistics entries carry is `topic`/`sources`/`verified-at`/`recheck`/`couples`
(`reports/round-9/metadata/v08-linguistics.md` §3: 16/16 `topic=1 sources=1
verified-at=1 recheck=1 couples=1`).

| field | line | present | content check |
|---|---|---|---|
| `topic` | 3 | yes | 832 chars; names the three-way map, the retrieved studies, and the deliverables |
| `source` | 4 | yes | gap statement + coverage sweep (see F2 for the field-semantics note) |
| `sources` | 5 | yes | multi-line block, 11 bullets; retrieval status recorded per item |
| `verified-at` | 17 | yes | 636 chars, dated `2026-10-17`, scope-bearing: names what was retrieved, what was not, and the HTTP statuses |
| `recheck` | 18 | yes | 246 chars; three named triggers |
| `couples` | 19 | yes | 1,354 chars; every referenced path resolves (§3) |

Order is `topic → source → sources → verified-at → recheck → couples`; the extra
`- source:` between `topic` and `sources` is the only ordering deviation from the
v08-measured house order (F2).

Unverifiable-claim hygiene: 11 `(to-verify)` marks, all inline at the dependent
claim, none load-bearing —
`python3 tools/gates/provenance-audit.py corpus/knowledge/linguistics/sound-symbolism.md`
→ `files=1 marks=11 mark-lines=11 findings=0 blocked=0` (exit 0, 21:38Z). Partition
regression check on all 19 current files (16 committed + C01/C02/C03 entries):
`files=19 marks=76 mark-lines=75 findings=0 blocked=0` (exit 0) against the
pre-landing 16-file reading `files=16 marks=29 mark-lines=29 findings=0 blocked=0`
(21:30Z) — no blocked file, no regression.

The round's own acceptance harness agrees with this section independently.
`reports/round-10/run-validation.py` `entry_checks('corpus/knowledge/linguistics/sound-symbolism.md')`
(imported read-only, `main()` not invoked, 21:41Z) returns
`missing_frontmatter: []`, `gap: True`, `decision_record: True`, 8 locators — the
three structural requirements of the C claim (complete frontmatter, named gap,
decision-record section) all read green by the harness that will score the claim,
not only by my own extraction.

Two round-level `C` failures in `reports/round-10/validation.json` concern this
entry's *packaging*, not its bytes, and belong to other seats: "README: no index row
for linguistics/sound-symbolism.md" is the C21/C22 index-update assignment, and
"coverage: 9 new entries < required 10" is the wave's aggregate shortfall. Neither
is a defect of this entry.

## 3. Source resolvability — PASS (with one method limit, F4)

### 3.1 Cited repo paths — 7/7 exist

All seven paths extracted from the entry resolve on disk: `corpus/QUALITY.md`,
`corpus/knowledge/linguistics/phonetics-phonology.md`,
`corpus/knowledge/synthesis/myth-to-language-derivation.md`,
`corpus/knowledge/verification/calibration-registry.md`,
`corpus/lessons/supplement-opencode-1/sources/phonetics.json`,
`reports/round-8/metadata/m08-linguistics.md`,
`reports/round-9/metadata/v08-linguistics.md`.

The three receipt claims that carry quoted content were opened, not merely resolved:

- `reports/round-9/metadata/v08-linguistics.md` — the entry's parenthetical
  `files=16 marks=29 findings=0` is a faithful elision of that file's line 164,
  `INFO scan: files=16 marks=29 mark-lines=29 findings=0 blocked=0   (exit 0)`; the
  same abbreviated form is used by v08 itself at line 167. **Verified, not
  misquoted.**
- `corpus/lessons/supplement-opencode-1/sources/phonetics.json` — 11 audits
  `PHON-A01 … PHON-A11` on `corpus/knowledge/linguistics/phonetics-phonology.md`,
  `checked_at_utc 2026-10-17T15:42:25Z`, and the claimed precedent is present
  verbatim: "The original Everett, Blasi & Roberts 2015 PNAS text was not retrieved
  (pnas.org HTTP 403)". **Verified.**
- `corpus/knowledge/verification/calibration-registry.md` — `CAL-03` exists (row at
  line 50, section at line 78) and covers exactly the relativity routing the entry
  cites. **Verified.**
- `corpus/knowledge/synthesis/myth-to-language-derivation.md` §6 = "Worked
  derivation B: candidate phonestheme sets, with controls", and it does carry the
  counting discipline the entry points to: "exclude productive prefix families and
  shared etymological families as independent evidence". **Verified.**

### 3.2 Cited URLs — 10/10 statuses reproduce exactly

Re-run 2026-10-17 21:31–21:33Z with `curl -sS -o /dev/null -w '%{http_code}' -L`:

| URL | entry claims | my re-run |
|---|---|---|
| `pmc.ncbi.nlm.nih.gov/articles/PMC5047153/` | 200 | **200** |
| `doi.org/10.1371/journal.pone.0092852` (PLOS) | 200 | **200** |
| `pure.mpg.de/…/file_1546262/content` (MPI PDF) | 200 | **200** |
| `doi.org/10.5334/gjgl.444` (Glossa) | 200 | **200** |
| `pubmed.ncbi.nlm.nih.gov/34775818/` | 203 | **203** |
| `pubmed.ncbi.nlm.nih.gov/23121711/` | 203 | **203** |
| `doi.org/10.1002/lnc3.361` (Wiley) | 403 | **403** |
| `doi.org/10.1353/lan.2004.0056` (MUSE) | 429 | **429** |
| `doi.org/10.1073/pnas.1605782113` (PNAS) | 403 precedent | **403** |
| `doi.org/10.1098/rstb.2020.0390` (Royal Society) | 403 | **403** |

No cited status is overstated: the blocked items are recorded as blocked in the
entry rather than presented as retrieved.

### 3.3 Substantive content verification — the numbers check out

Status codes alone prove nothing; the load-bearing numbers were checked against the
retrieved full texts.

**Blasi et al. 2016 (PMC5047153, full text fetched 21:32Z, 289,004 bytes).** All
seven signal rows in the entry's table match the published table exactly, including
lineage counts and areal ratios:

| entry claim | retrieved full text |
|---|---|
| small ↔ i, RR 1.58, 78 lineages, 3/5 | RR 1.58, 78, 3/5 |
| small ↔ C, RR 5.12, 61, 3/4 | RR 5.12, 61, 3/4 |
| round ↔ r, RR 2.48, 56, 4/5 | RR 2.48, 56, 4/5 |
| tongue ↔ l, RR 2.77, 280, 6/6 | RR 2.77, 280, 6/6 |
| nose ↔ n, RR 1.47, 334, 4/6 | RR 1.47, 334, 4/6 |
| full ↔ p, RR 2.11, 231, 5/6 | RR 2.11, 231, 5/6 |
| full ↔ b, RR 1.91, 213, 4/6 | RR 1.91, 213, 4/6 |

Also verified in the same text: 6,452 word lists; 28–40 lexical items with a
328-list subset up to 100 items; 62% of the world's languages and ≈85% of lineages;
six macroareas; the ≥10-lineages-in-each-of-≥3-macroareas screen; 74 detected
signals; "risk ratio" = RR; and the lower-bound framing ("should be regarded as
providing a lower-bound estimate"). The **negative** results the entry elevates are
also real: "big (nl = 73) and large (nl = 74) and o did not show any relevant
signature of association in our sample at the global level."

**Haynie et al. 2014 (PLOS full text fetched 21:37Z, 249,478 bytes).** "a sample of
120 languages" ✓; "Several sound-meaning relationships are only significant for
segments in prominent positions in the word" ✓; "the prevailing mapping between
vowel quality and magnitude meaning cannot be characterized by a simple link between
gradients of magnitude and vowel F2, contrary to the claims of previous studies" ✓ —
matching the entry's §2.2 and calibration row C4 verbatim in substance.

**Ćwiek et al. 2022 and Bremner et al. 2013 (abstracts via Europe PMC REST,
21:33Z).** Ćwiek: "speakers of 25 languages representing nine language families and
10 writing systems" ✓, effect "largely independent of orthography" ✓ — the entry's
"25 languages, nine language families, 10 writing systems" is exact. Bremner: Himba
of Northern Namibia show the shape–sound effect while differing on shape–taste ✓ —
so the entry's carried-forward **correction** of the neighbour entry's
"not universal (Bremner et al. 2013)" clause is the correct reading of the source,
and the entry's decision to record the correction without editing the committed
entry (D3) respects append-only discipline.

### 3.4 F4 — method limit, not an entry defect

PubMed returns 203 as the entry records, but to *this* lane's fetch it now serves a
cookie-required interstitial (`pubmed.ncbi.nlm.nih.gov/34775818/` → 5,590-byte
`cookies-required` page, no abstract text), so I could not reproduce the abstract
*retrieval* from PubMed. I verified the same abstracts through the Europe PMC REST
API instead. The entry's claim ("abstract retrieved 2026-10-17 from PubMed") is
consistent with the recorded status and with content that matches the papers; the
limit is on my re-verification route, not on the entry. Anyone re-checking should
expect the same wall.

## 4. Duplication — PASS

- **Slug:** `sound-symbolism.md` is not in the 179-entry baseline slug set
  (`.scratch/baseline-slugs.txt`) — no collision, so the `-b` suffix rule is not
  engaged.
- **Body reuse:** 8-gram shingle Jaccard against all 19 current linguistics entries
  — maximum **0.0028** (19 shared shingles, vs `phonetics-phonology.md`), next
  0.0016 (`color-terminology.md`). Calibration of the metric on the committed
  corpus: no pair among the 179 entries exceeds 0.05, so 0.0028 is far inside the
  no-reuse band.
- **Topic ownership:** the two nearest neighbours are handled by explicit
  demarcation rather than duplication — `phonetics-phonology.md` keeps inventory,
  allophony and §7 channels and defers §8 to this file (D1), and
  `synthesis/myth-to-language-derivation.md` keeps the operational pipeline while
  this file supplies the linguistics layer (D7). The entry states the boundary in
  both directions.

## 5. Filler check — PASS

The claim's bar is "NO filler — a new entry must name the gap it fills". The gap is
named, with a sweep, in `- source:` (line 4), and the sweep is the corrected form
(see F1): `grep -lic -e "sound symbol" -e "sound-symbol"
corpus/knowledge/linguistics/*.md` → `conlang-methodology.md` (one decision-table row
+ one recheck mention), `phonetics-phonology.md` (§8 summary + §10 pointer), this
file — "mentions only, no owning entry". I re-ran that command verbatim and it
reproduces file-for-file, and the per-file characterisation is right:
`conlang-methodology.md` has exactly 2 matches — line 6 `recheck:` and line 136
decision-table row — and `phonetics-phonology.md` has 6. The parent gap is also real:
`phonetics-phonology.md` §8 occupies 10 content lines (246–257) and §10 line 279
lists `sound-symbolism.md` among the prospective siblings.

Deliverable density (the usability bar in `corpus/QUALITY.md`): 10 `##` sections,
37 table rows, 49 bullet items, a 9-row calibration shelf (C1–C9) separating robust
/ culture-dependent / contested / discredited / hazard, and two step procedures
(phonestheme-bank protocol with nonmember and near-miss controls; ideophone register
design). §9 "Decision record (author)" carries D1–D7, each with a rationale and a
recheck trigger — satisfying the round's "at least one decision-record section"
requirement explicitly, and meeting the C01 reviewer's own criterion for that
section (a record of what was chosen, why, and the rejected alternative or limit).

## 6. Findings

**F1 — recorded negative sweep did not reproduce; fixed in-revision. (severity: low;
status: FIXED-WITH-CONTROL)**

At revision `dbc8339e` (21:35Z) the entry's `- source:` line recorded the sweep
`for f in corpus/knowledge/linguistics/*.md; do grep -l 'sound symbol' "$f"; done`
with the result "only `phonetics-phonology.md`". Re-running it printed **three**
files: `conlang-methodology.md`, `phonetics-phonology.md`, and the new entry itself.
`conlang-methodology.md` is committed and unmodified (`git status --short
corpus/knowledge/linguistics/` shows it clean; `git show
HEAD:corpus/knowledge/linguistics/conlang-methodology.md | grep -c 'sound symbol'`
→ 1), so the printed result was wrong at that revision — a receipt-accuracy defect
under the lane rule that negative claims carry their sweep.

*Control (the fix):* at `17670f81` the author replaced the sweep with the wider
`grep -lic -e "sound symbol" -e "sound-symbol" corpus/knowledge/linguistics/*.md`
and recorded all three files with per-file characterisation. I re-ran that exact
command at 21:38Z and it reproduces (3 files; `conlang-methodology.md` = 2 matches
matching "one decision-table row + one recheck mention"). The gap claim itself was
never at risk — a single table cell is not topic ownership — so this was a receipt
defect, not a gap failure, and it is closed in the pinned revision.

**F2 — `- source:` carries the gap statement, against the field's corpus-wide
semantics. (severity: low; status: OPEN — non-blocking, author's call)**

Of the 121 corpus files that carry a `- source:` field, 36 print the house formula
"the entry's own source apparatus — the `- sources:` field above …" and the rest
point at their source list ("the works listed above and …"). This entry is the
**only** one of the 121 where `- source:` carries a gap statement instead
(`grep -rh '^- source:' corpus/knowledge/ | grep -ci 'gap'` → 1). Provenance is not
lost — `- sources:` is present, multi-line and correct — and the round-10 claim's
"must name the gap it fills" is satisfied; but a reader or gate that parses
`- source:` for source-apparatus semantics will mis-read this file, and it makes
C02's frontmatter diverge from its own round's sibling: C03 placed the same content
in a body section (`numerals-and-measures.md` §0 "The gap this entry fills").

*Author's rationale, now on record:* the C02 fragment declares the field
deliberately — "`topic` + `source` (singular pointer, fleet-contract reading)" —
so this is a knowing divergence, not an oversight, and it is recorded here rather
than counted as a defect. The recommendation is therefore only that whoever next
touches the file decides it consciously: since the entry is still untracked, either
relocate the gap statement to a `## 0` section and restore the house `- source:`
pointer, or keep the fleet-contract reading and note it in the index update. No gate
currently fails on it — `provenance-audit.py` is green (exit 0, findings 0) and
`run-validation.py` `entry_checks` reports `missing_frontmatter: []`.

**F3 — mid-review churn. (severity: informational; status: DOCUMENTED)**

Three revisions in under three minutes (§0 pin table). Every check in this file was
re-run against `4f14b05a`; F1's fix is the only content change I could attribute
between revisions 1 and 3 by measurement. Any further edit invalidates the pin, so
this verdict should be read against the pinned sha, and re-checked with §8 if the
entry moves again.

## 7. Residual and limits of this review

- **Fragment timing:** `reports/round-10/coverage/C02.md` landed at ≈21:39Z, after
  this review's entry inspection but before this file was finalised; §0 records what
  it confirms (attribution, sha pin, sweep, gate reading). The review body was
  measured against the entry bytes, and the fragment did not change any of them.
- **Fragment's own count differs by one line:** C02.md says "28,980 / 155" and the
  review harness prints 156; `wc -lc` gives 155, so the harness counts a final
  unterminated line. No content difference — flagged only so a later reader is not
  confused by two "line counts" for one file.
- **Not an admission decision.** Per `AGENTS.md`, workers never claim independent
  promotion verification; this is author-side review evidence only.
- **Bibliographic items not re-retrieved.** The entry explicitly marks the
  Sapir/Köhler/Ohala/Ultan/Ramachandran block as riding on the in-corpus audited
  source block, and marks ideophone/acquisition page-level detail `(to-verify)`. I
  did not attempt retrieval for those, and did not need to: the entry makes no
  page-level claim on them.
- **PubMed content wall** (F4) limited one re-verification route; Europe PMC was
  used as the substitute route and agreed with the entry.
- **Concurrent workers.** The corpus and `reports/round-10/` were being written by
  sibling shards throughout; all counts above name their command and timestamp.

## 8. Reproduction

```sh
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
export TMPDIR=$PWD/.scratch

# identity + pin
sha256sum corpus/knowledge/linguistics/sound-symbolism.md
# 4f14b05a7df542ad5e3dca39c20cb02dc3f5745c70395418770da93794fddd5d

# frontmatter + citations + duplication (harness written for this review)
python3 .scratch/review-c02-check.py corpus/knowledge/linguistics/sound-symbolism.md

# gate, entry and partition
python3 tools/gates/provenance-audit.py corpus/knowledge/linguistics/sound-symbolism.md
python3 tools/gates/provenance-audit.py corpus/knowledge/linguistics/*.md

# the round's own acceptance harness, on this entry (read-only import; main() not invoked)
python3 -c "import importlib.util; spec=importlib.util.spec_from_file_location('rv','reports/round-10/run-validation.py'); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); print(m.entry_checks('corpus/knowledge/linguistics/sound-symbolism.md'))"
# -> missing_frontmatter: []  gap: True  decision_record: True  locators: 8

# the entry's own sweep, re-run verbatim
grep -lic -e "sound symbol" -e "sound-symbol" corpus/knowledge/linguistics/*.md

# the disputed (superseded) sweep from revision dbc8339e
for f in corpus/knowledge/linguistics/*.md; do grep -l 'sound symbol' "$f"; done

# source re-runs
curl -sS -o /dev/null -w '%{http_code}\n' -L \
  https://pmc.ncbi.nlm.nih.gov/articles/PMC5047153/          # 200
curl -sS -L https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0092852
curl -sS "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:%2210.1098/rstb.2020.0390%22&resultType=core&format=json"

# in-corpus receipts
grep -n 'files=16 marks=29' reports/round-9/metadata/v08-linguistics.md
grep -n 'PHON-A' corpus/lessons/supplement-opencode-1/sources/phonetics.json
grep -n 'CAL-03' corpus/knowledge/verification/calibration-registry.md
```

- reviewer run: 21:26Z–21:40Z UTC, 2026-10-17 (local UTC-03:00)
- entry pin at close: `4f14b05a7df542ad5e3dca39c20cb02dc3f5745c70395418770da93794fddd5d`
  (unchanged since 21:38:07Z; re-verified at 21:40:23Z)
- files written by this shard: this file only (`.scratch/` scratch aside)
