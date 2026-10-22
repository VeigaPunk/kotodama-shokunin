# Round 54, attempt 2 — seat ExecDryRunCensus

**Seat:** KotodamaR54a2.ExecDryRunCensus (executor, leaf)
**Assignment:** re-verify the inherited declaration's before-state; run each declared command in a sandbox clone at the declaration commit and give a verdict per command; report lane drift against the declaration commit.
**Declaration commit:** `7fa37fbb6f0a0c39b3d6cfd3d371f5bb3a65050c`
**Lane:** `/home/vgpnk/Projects/shokunin/kotodama-shokunin`
**Scratch:** `/fast/scratch/hyaku/kotodama-r54-a2/ExecDryRunCensus/`
**Date:** 2026-10-22

## Verdict summary

**The inherited declaration's before-state is confirmed intact. Every declared command produced exactly the declared output and exit code: 12 of 12 checks MATCH THE DECLARATION.**

Nothing in the declaration needed correcting for the before-state. The work below is in the *landing* path: the declaration's `after_required` text understates what the seven legs actually require of the three files claim C lands, and several concrete traps would let a landing pass `accept-c.py` while failing the fleet census, or pass silently. Those findings are for the L1, who writes the entry and the registry rows.

Section 4A adds the same findings re-tested against the L1's live landing, which began while this seat was finishing: the README obligations were still open in the live tree, and the landed entry cites 47 draft ids, so the registry needs 47 rows rather than the FLOOR's 20.

No lane file was created, edited or deleted by this seat. The only writes are under this seat's scratch directory and this report file.

---

## 1. Sandbox setup

```
$ git clone -q /home/vgpnk/Projects/shokunin/kotodama-shokunin /fast/scratch/hyaku/kotodama-r54-a2/ExecDryRunCensus/lane
$ git -C /fast/scratch/hyaku/kotodama-r54-a2/ExecDryRunCensus/lane checkout -q 7fa37fbb6f0a0c39b3d6cfd3d371f5bb3a65050c
$ git -C /fast/scratch/hyaku/kotodama-r54-a2/ExecDryRunCensus/lane log --oneline -3
7fa37fb round-54: declaration revised before dispatch — claim C statement, clause list and controls receipt (13/13), dry run
260c68d round-54: claim C instruments revised before dispatch (SET walks every file; RANGE fails duplicate rows and range notation; five more red controls) after the pre-dispatch critic findings
1ec84db round-54: declaration — claim C (masks and masquerade entry), clause list, criterion-11 controls receipt, dry run
```

`git status --porcelain` in the clone after checkout: empty (clean tree at the declaration commit).

---

## 2. Command-by-command results

Every command below was run in the sandbox clone at `7fa37fb`, except the census, which the assignment specifies reads the real lane (it writes nothing).

### 2.1 `python3 -B reports/round-54/accept-c.py`

```
$ python3 -B reports/round-54/accept-c.py
SET FAIL count=229 required=230 added=[] removed=[]
SWEEP FAIL exit=0 rows 229 files 229 missing_from_index 0 []
FLOOR FAIL cited=0 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
exit 1
```

**Verdict: MATCHES DECLARATION.** The declared `expected_pre_landing_counting` reads "exit 1: SET FAIL (count=229 added=[] removed=[]), SWEEP FAIL (exit 0 but rows 229 files 229), FLOOR FAIL (cited=0); RANGE, STATUS, USEDBY PASS vacuously; ACCESS PASS". Every leg verdict and every detail string matches, leg by leg, including the vacuous passes.

The same output was produced by running the command against the real lane worktree (read-only), so the sandbox and the live lane agree.

### 2.2 `python3 -B reports/round-54/dry-run.py` and its check mode

The script's docstring names the two modes: `run [--label TEXT]` prints a receipt block to stdout; `check RECEIPT` does a two-way check of a receipt file.

```
$ python3 -B reports/round-54/dry-run.py run --label "ExecDryRunCensus declaration dry run"
# ExecDryRunCensus declaration dry run 2026-10-22T18:34:46Z
$ python3 -B reports/round-54/accept-c.py
SET FAIL count=229 required=230 added=[] removed=[]
SWEEP FAIL exit=0 rows 229 files 229 missing_from_index 0 []
FLOOR FAIL cited=0 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
exit 1
# role: C counting; expected pre-landing: exit 1: SET FAIL (count=229 added=[] removed=[]), SWEEP FAIL (exit 0 but rows 229 files 229), FLOOR FAIL (cited=0); RANGE, STATUS, USEDBY PASS vacuously; ACCESS PASS
$ python3 -B reports/round-54/accept-c.py
SET FAIL count=229 required=230 added=[] removed=[]
SWEEP FAIL exit=0 rows 229 files 229 missing_from_index 0 []
FLOOR FAIL cited=0 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
exit 1
# role: C acceptance; expected pre-landing: fails before landing (exit 1), printing the before value; passes at all seven legs PASS (exit 0): count 230, added [masks-masquerade.md], removed [], rows 230 files 230, missing_from_index 0, cited >= 20, no bad S-id
$ python3 -B tools/check-claim-separability.py reports/round-54/separability-manifest.json
SEPARABILITY_INPUT_ERROR unit C lands 'corpus/knowledge/culture-material/masks-masquerade.md', which is absent from the worktree under '/fast/scratch/hyaku/kotodama-r54-a2/ExecDryRunCensus/lane'
exit 2
# role: separability; expected pre-landing: exit 2 before landing: SEPARABILITY_INPUT_ERROR naming the absent C land; checker stops at its first absent land, so later legs are unevaluated
$ python3 -B reports/round-54/claims-agree.py
AGREE claims=['C']
exit 0
# role: agreement; expected pre-landing: AGREE, exit 0
exit 0
```

**Verdict: MATCHES DECLARATION.** All four declared commands ran, each produced its declared exit code, and the role-expectation lines the script prints are the declaration's own strings.

Check mode, against the committed receipt `reports/round-54/telemetry/declaration-dry-run.txt`:

```
$ python3 -B reports/round-54/dry-run.py check reports/round-54/telemetry/declaration-dry-run.txt
MISSING_FROM_RECEIPT []
UNDECLARED_IN_RECEIPT []
exit 0
```

**Verdict: MATCHES DECLARATION.** Both lists empty, exit 0.

A fresh `run` reproduces the committed receipt byte for byte once the label line and the lane path are normalised:

```
$ python3 -B reports/round-54/dry-run.py run --label X > /tmp/dryrun-out.txt
$ diff <(sed -e '1d' -e 's#/fast/scratch/.../lane#LANE#g' -e 's#/home/vgpnk/Projects/shokunin/kotodama-shokunin#LANE#g' /tmp/dryrun-out.txt) \
       <(sed -e '1d' -e 's#/home/vgpnk/Projects/shokunin/kotodama-shokunin#LANE#g' reports/round-54/telemetry/declaration-dry-run.txt)
diff exit 0
```

### 2.3 `python3 -B tools/check-claim-separability.py reports/round-54/separability-manifest.json`

```
$ python3 -B tools/check-claim-separability.py reports/round-54/separability-manifest.json
SEPARABILITY_INPUT_ERROR unit C lands 'corpus/knowledge/culture-material/masks-masquerade.md', which is absent from the worktree under '/fast/scratch/hyaku/kotodama-r54-a2/ExecDryRunCensus/lane'
exit 2
```

**Verdict: MATCHES DECLARATION.** The declaration's separability role expects exactly "exit 2 before landing: SEPARABILITY_INPUT_ERROR naming the absent C land".

### 2.4 `python3 -B reports/round-54/claims-agree.py`

```
$ python3 -B reports/round-54/claims-agree.py
AGREE claims=['C']
exit 0
```

**Verdict: MATCHES DECLARATION.** The declaration expects "AGREE, exit 0".

### 2.5 `python3 -B tools/check-source-access.py`

```
$ python3 -B tools/check-source-access.py
ACCESS: 2 flagged rows, 0 findings
exit 0
```

**Verdict: MATCHES DECLARATION.** The declaration's `before` field expects "ACCESS PASS (check-source-access exit 0)". The two flagged rows are `S094` and `S132`, both with status `rejected`; a rejected row raises no finding, so the leg passes.

### 2.6 `python3 -B reports/round-28/readme/sweep.py`

```
$ python3 -B reports/round-28/readme/sweep.py
parts {"civilizations": 94, "culture-material": 28, "linguistics": 28, "myth-symbol": 26, "synthesis": 29, "verification": 24}
rows 229 files 229
missing_from_index 0 []
topic_mismatch 0 []
orphan_rows 0 []
header_drift {}
totals_line 229 totals_ok True
footer {"date": "2026-10-22", "command": "python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge", "total": 229, "dir_totals": [28, 26, 28, 29, 24, 94]}
footer_live {"total": 229, "dir_totals": [28, 26, 28, 29, 24, 94], "order": ["linguistics", "myth-symbol", "culture-material", "synthesis", "verification", "civilizations"]}
footer_findings [] footer_ok True
readme_sha256 9c2d10d15b73d2c4c562f24939b0a3d08ca9504ff3344c09efd73eceb139e7ec
exit 0
```

**Verdict: MATCHES DECLARATION.** The declared expectation is "SWEEP FAIL (exit 0 but rows 229 files 229)" — the sweep itself exits 0, and the accept-c SWEEP leg reads it as FAIL because the row count is not 230. The `rows 229 files 229` and `missing_from_index 0` strings match exactly.

### 2.7 `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama`

```
$ /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama
kotodama	W04	S127 duplicate url voices.uchicago.edu/goldinmeadowlab/people/susan-goldin-meadow/research-statement across scopes
kotodama	W04	S128 duplicate url pure.uvt.nl/ws/portalfiles/portal/100130712/Zeshan_deVos_Eds._2012.pdf across scopes
kotodama	W04	S129 duplicate url pmc.ncbi.nlm.nih.gov/articles/PMC10622114 across scopes
kotodama	W04	S130 duplicate url pmc.ncbi.nlm.nih.gov/articles/PMC6818964 across scopes
kotodama	W04	S131 duplicate url link.springer.com/article/10.1186/1477-7517-9-16 across scopes
kotodama	W04	S132 duplicate url ida.gallaudet.edu/cgi/viewcontent.cgi?article=1004&context=sls across scopes
kotodama	W04	S133 duplicate url www.cslds.org/apsl-consortium/sign-linguistics/module-7-sign-phonetics-and-phonology-symmetry-and-dominance-condition across scopes
kotodama	W04	S185 duplicate url www.internationalphoneticassociation.org/icphs-proceedings/ICPhS2003/papers/p15_2131.pdf across scopes
kotodama	W04	S186 duplicate url ich.unesco.org/en/RL/whistled-language-of-the-island-of-la-gomera-canary-islands-the-silbo-gomero-00172 across scopes
kotodama	ok	/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md
exit 0
```

**Verdict: MATCHES DECLARATION.** Output is identical to the attempt-2 start census at `reports/round-54/telemetry/census-start-a2.txt` (same nine W04 warnings, same `ok` line, same exit 0). W04 is a warning code and does not change the exit status.

### 2.8 Instrument integrity

The criterion-11 receipt `reports/round-54/telemetry/criterion11-controls.txt` lists sha256 lines for five instruments. All five match the files at the declaration commit:

```
$ sha256sum reports/round-54/accept-c.py reports/round-54/base-knowledge-files.txt reports/round-28/readme/sweep.py tools/check-source-access.py reports/round-54/criterion11-controls.py
ceadf2c68313bc82c4299e11f356aeb148a07531e7600f9453e60f9f0f466160  reports/round-54/accept-c.py
ce217cb7b24ed382ce8ed06ccaf14d593fadfeea454c1b4d755c04e5de2c9f37  reports/round-54/base-knowledge-files.txt
9b2ccac0046831fdaf48863ccd0ff6ca0fa390d044746c876e83a71c06f0cdd3  reports/round-28/readme/sweep.py
fb915386a781b332ae4d73e6d81b2e441ad0d9cd264d8c10421b0c01cd973bd5  tools/check-source-access.py
d4223b4fbc6f98a066806c46b3fd97d6b77be2d81f7481770ec52a5687697a7d  reports/round-54/criterion11-controls.py
```

**Verdict: MATCHES DECLARATION.** The receipt is valid for the tree under test.

The controls themselves replay cleanly at the declaration commit:

```
$ python3 -B reports/round-54/criterion11-controls.py <clone> 7fa37fbb6f0a0c39b3d6cfd3d371f5bb3a65050c
...
## RED-USEDBY: exit 1 (expected 1); failing legs ['USEDBY']; AS EXPECTED
...
## RED-ACCESS: exit 1 (expected 1); failing legs ['ACCESS']; AS EXPECTED
...
CONTROLS 13/13 as expected
exit 0
```

**Verdict: MATCHES DECLARATION.** 13/13, matching the receipt's own "CONTROLS 13/13 as expected".

### 2.9 Gap evidence at base

The declaration's `gap_evidence_at_base` was recounted from the tree, not taken on trust:

```
find corpus/knowledge -iname '*mask*'                                   -> 0 files
grep -rlE '^- topic:.*(mask|masquerad)' corpus/knowledge                 -> 1 file: civilizations/siam-thai.md
grep -rliE '\bmask(s|ed|ing)?\b|masquerade' corpus/knowledge             -> 41 files
```

**Verdict: MATCHES DECLARATION.** 0 filename owners, 1 topic-line owner, 41 files with passing mentions. The three named partial owners exist on disk: `myth-symbol/ritual-liminality.md`, `culture-material/funerary-material-culture.md`, `culture-material/costume-semiotics.md`.

---

## 3. Lane state versus the declaration commit

```
$ git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin diff --stat 7fa37fbb6f0a0c39b3d6cfd3d371f5bb3a65050c
 .ufo/waves/round-54/build-a2-dispatch.json     | 687 +++++++++++++++++++++++++
 .ufo/waves/round-54/build-a2-sent-payload.json | 215 ++++++++
 .ufo/waves/round-54/build-a2-spec.json         | 362 +++++++++++++
 .ufo/waves/round-54/build-dispatch.json        | 591 +++++++++++++++++++++++++
 .ufo/waves/round-54/build-sent-payload.json    | 221 ++++++++
 .ufo/waves/round-54/build-spec.json            | 308 +++++++++++++
 .ufo/waves/round-54/build/swarm-registry.json  | 377 ++++++++++++++++
 .ufo/waves/round-54/gen-build-spec.py          | 121 +++++
 reports/round-54/telemetry/census-start-a2.txt |  13 +
 9 files changed, 2895 insertions(+)

$ git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin status --porcelain
?? .ufo/waves/round-54/build-a2/
```

**Paths differing from the declaration commit, and what they are.** The nine tracked paths are all wave records and telemetry added by the single commit after the declaration, `5757c45118771d8baac238b52aa5e95fc18cbd54` ("attempt-1 dead build-wave dispatch records ... committed as evidence; attempt-2 build-a2 spec ..., generator, dispatch and sent payload; census at attempt-2 start"). The one untracked path is the wave's own report directory, `.ufo/waves/round-54/build-a2/`, which holds this report and the other build-a2 seat reports.

**None of them is claim-relevant.** Filtering the diff to the claim's land set (`corpus/knowledge/culture-material/masks-masquerade.md`, `corpus/README.md`, `corpus/SOURCES.md`) and to every instrument path (`accept-c.py`, `base-knowledge-files.txt`, `sweep.py`, `check-source-access.py`, `criterion11-controls.py`, `claims.json`, `separability-manifest.json`, `claims-agree.py`, `dry-run.py`) returns an empty list. No claim-relevant path has changed since the declaration.

One consequence worth naming: because `reports/round-54/telemetry/census-start-a2.txt` was added *after* the declaration, the declaration commit's own census state is the attempt-1 one. The attempt-2 census (`census-start-a2.txt`, lane tip `7fa37fb`) and this seat's re-run agree exactly, so the census baseline is stable across the attempt change.

---

## 4. Landing-path findings for the L1

These are beyond the before-state re-verification, and each one is a case where a landing would have passed `accept-c.py` while the lane was actually in a worse state, or where the declaration's `after_required` text is silent about a requirement the seven legs enforce. The L1 writes the entry and the registry rows, so these are the actionable items.

### 4.1 The README counts footer must be updated, or the SWEEP leg fails

The declaration's `after_required` says the landing yields "rows 230 files 230, missing_from_index 0". It does not mention the counts footer. But `sweep.py` exits non-zero on a footer drift, and accept-c's SWEEP leg reads the sweep's exit status directly, so the footer is inside the claim.

Rehearsed on a scratch tree (`rehearse_landing.py`, `rehearse_landing2.py` in this seat's scratch):

```
=== README footer NOT updated ===
sweep.py exit 1
totals_line 229 totals_ok False
footer_findings [{"class": "FOOTER_TOTAL", "declared": 229, "live": 230, ...},
                 {"class": "FOOTER_DIR_TOTALS", "declared": [28, 26, 28, 29, 24, 94], "live": [28, 26, 29, 29, 24, 94], ...}] footer_ok False
accept-c.py: SWEEP FAIL exit=1 rows 230 files 230 missing_from_index 0 []
```

```
=== README footer updated to 230 ===
sweep.py exit 1 -> 0
totals_line 230 totals_ok True
footer_findings [] footer_ok True
accept-c.py exit 0, all seven legs PASS
```

The footer is prose in `corpus/README.md`, in two places, not JSON:

- `Total knowledge entries: 229.` becomes `Total knowledge entries: 230.`
- `(total 229 files; directory totals 28/26/28/29/24/94).` becomes `(total 230 files; directory totals 28/26/29/29/24/94).`

The six numbers are in the sweep's section order — linguistics, myth-symbol, culture-material, synthesis, verification, civilizations — so culture-material moves 28 to 29 and the other five stay. The section header `## culture-material/ (28)` becomes `(29)`.

### 4.2 The README index row's topic text must equal the entry's `- topic:` line verbatim

The sweep's topic-equality leg compares the index row's text with the entry's own `- topic:` head-block text, space-joined across continuation lines. A paraphrase is caught:

```
=== README topic text paraphrased, footer updated ===
topic_mismatch 1 ['culture-material/masks-masquerade.md']
sweep.py exit 1
```

The index row must carry the entry's topic string exactly, not a shortened version of it.

### 4.3 New registry rows must go inside the `## Registry` table

This is the trap with the largest consequence: **appending the new rows at the end of `corpus/SOURCES.md` passes `accept-c.py` and fails the fleet census.**

The `## Registry` section runs from line 26 to line 267 (the S238 row); `## Paths` starts at line 269. The census reports E12 for a row-shaped line that sits outside the Registry section.

```
=== new rows INSIDE the ## Registry table ===
accept-c.py exit 0, all seven legs PASS
sources-census.sh validate exit 0
ok_rows	ok	.../corpus/SOURCES.md

=== new rows appended AFTER the ## Registry table ===
accept-c.py exit 0, all seven legs PASS        <- accept-c does not care
sources-census.sh validate exit 1
bad_rows	E12	S239 row outside Registry section
bad_rows	E12	S240 row outside Registry section
... (E12 for each of the 20 new rows)
```

`accept-c.py` reads the registry with a bare `^\| S\d{3} ` line match, so it is blind to the section structure. The census is the only checker that sees the difference. Insert the new rows immediately after the S238 row, inside the table.

### 4.4 A cited S-id spelled with fewer than three digits escapes every leg

The RANGE leg extracts cited ids with `\bS\d{3}\b`. Two spellings slip past it:

```
=== entry cites 3-digit S095 (the Grand Council medicine-mask row) ===
RANGE FAIL bad=['S095'] range_notation=[]
accept-c.py exit 1

=== entry cites 2-digit S95 (same row, two-digit spelling) ===
RANGE PASS bad=[] range_notation=[]
FLOOR PASS cited=20 floor=20
accept-c.py exit 0        <- a pre-S239 citation that no leg sees
```

The registry stores every id in three-digit form (`S001` through `S238`; there are no two-digit ids in the registry, and 238 rows all of three digits). The two-digit spelling is a shape the registry never uses, so writing it in the entry both escapes the RANGE leg and points the reader at an id that does not exist. The corpus has 28 distinct two-digit `S`-tokens in prose today (`S1`, `S6`, `S95`, `S98` and so on), so the mistake is one this lane's style invites.

A four-digit id escapes the same way. `S1234` is not matched by `\bS\d{3}\b` at all: FLOOR stays at 20, RANGE passes, and the leg set exits 0.

**Recommendation for the L1:** write every cited id in the registry's own three-digit form, and prefer the file-path form of a citation over a bare id when pointing at a partial owner.

### 4.5 A negative access statement in a registry row still trips the ACCESS leg

The access checker scans each row's source, anchor and teaches cells for marker words, and the denial forms are matched too. Rehearsed against the real `tools/check-source-access.py`:

```
explicit denial: 'no headless browser was used'          -> exit 1  ACCESS FAIL
denial: 'not opened via a headless browser'              -> exit 1  ACCESS FAIL
denial: 'never used a captcha solver'                    -> exit 1  ACCESS FAIL
denial: 'no paywall was bypassed'                        -> exit 1  ACCESS FAIL
denial: 'no VPN was used'                                -> exit 1  ACCESS FAIL
ordinary access note: 'captcha met, not passed'          -> exit 0  ACCESS PASS
plain wording: 'opened by ordinary means'                -> exit 0  ACCESS PASS
UNESCO ICH page, plain request                          -> exit 0  ACCESS PASS
UNESCO page read via Wayback after a challenge          -> exit 0  ACCESS PASS
museum collection record                                 -> exit 0  ACCESS PASS
```

The regular expression carries a negative lookbehind (`(?<!\bnot\ )(?<!\bno\ )(?<!\bnever\ )`) only on the "bypassed/solved/passed" branch; the `\bheadless\b`, `\bvpns?\b` and `\bcaptcha\b` branches have no such guard. A row that says "no headless browser was used" is therefore flagged.

**Recommendation for the L1 and the source seats:** write the access route positively — "opened by ordinary means", "HTTP 200, plain request", or "challenge met, not passed; read via a Wayback capture" — and never repeat a marker word in order to deny it. All three passing forms above are already in use in the lane's existing rows.

### 4.6 Two more registry-row shapes the census catches but accept-c does not

```
=== a registry row written with 10 cells (one cell missing) ===
accept-c.py: RANGE PASS (the row is not cited), ACCESS FAIL exit=2
census: malformed_row	E01	S238 fields=10     exit 1

=== a cited registry row written with 10 cells ===
accept-c.py: RANGE FAIL bad=['S239'], ACCESS FAIL exit=2     exit 1

=== a used-by cell naming a path that is not on disk ===
census: E03 duplicate id (when the row is added twice)
census: E11 missing used-by corpus/knowledge/culture-material/nonexistent.md     exit 1
```

A row needs all 11 cells. The used-by cell must name paths that exist on disk, so `corpus/knowledge/culture-material/masks-masquerade.md` can only be written once the entry itself is in the tree.

### 4.7 The registry currently ends at S238, and the claim needs 20 new ids

```
existing registry ids: 238
highest id: S238
ids >= S239 available: 0
```

The FLOOR leg requires 20 distinct cited ids, and RANGE requires each to be S239 or above with exactly one registry row. So the landing needs 20 new rows, S239 upward, each mined, each naming the entry in its used-by cell. The 26 build-a2 scout seats each report one opened source under a draft id `NEW-<SeatName>-<n>`; the L1 assigns the final S-numbers at integration. The topic ground is clean: `grep -ic` over `corpus/SOURCES.md` finds zero rows for mask, masquerade, carnival, Gelede, Egungun, Talchum, Noh, Commedia, Malagan, Mummer, Parachicos, Kwakwakawakw, Haudenosaunee, Venice, Kolam or Sri Lanka, so the new ids will not collide with existing rows. There are already 9 `ich.unesco.org` rows (S062, S063, S069, S157, S159, S163, S183, S184, S186); a UNESCO source already in the registry must be cited by its existing id or not cited at all, since a duplicate id is census E03.

### 4.8 A landed tree does satisfy the separability checker

With the entry landed and the REC record lands present, the separability checker returns a verdict rather than an input error:

```
$ python3 -B tools/check-claim-separability.py reports/round-54/separability-manifest.json
SEPARABILITY: 0 findings
SEPARABILITY_NOTE units=2 ordered_pairs=2 acceptance_runs=1
exit 0
```

### 4.9 Two operational notes on the instruments

- `dry-run.py` resolves `claims["separability_manifest"]` relative to the current working directory, not to the script's own directory. Running it from anywhere other than the lane root raises `FileNotFoundError` and exits 1 (run mode) or prints `CHECK_INPUT_ERROR` and exits 2 (check mode). Run it from the lane root, as the declaration does.
- `dry-run.py run` writes nothing: it prints to stdout. The receipt file `reports/round-54/telemetry/declaration-dry-run.txt` was produced by redirecting stdout, and re-running with the same redirect reproduces it byte for byte (shown in 2.2). The declaration's `dry_run_rule` wording ("writes reports/round-54/telemetry/declaration-dry-run.txt") describes the intended pipeline rather than what the script does on its own.

---

## 4A. Addendum: the same findings against the L1's live landing

After the before-state work above was finished, the L1 began landing claim C in the live lane while this seat was still writing. This seat did not write any of it. `corpus/knowledge/culture-material/masks-masquerade.md` appeared as an untracked file (23,643 bytes, 15:42) with no S-ids in it yet, and `corpus/README.md` had no index row for it.

That intermediate state is a live confirmation of finding 4.1 and 4.2. `accept-c.py` and `sweep.py` on the live lane at that moment:

```
$ python3 -B reports/round-54/accept-c.py
SET PASS count=230 required=230 added=['corpus/knowledge/culture-material/masks-masquerade.md'] removed=[]
SWEEP FAIL exit=1 rows 229 files 230 missing_from_index 1 ['culture-material/masks-masquerade.md']
FLOOR FAIL cited=0 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
exit 1

$ python3 -B reports/round-28/readme/sweep.py
parts {"civilizations": 94, "culture-material": 29, "linguistics": 28, "myth-symbol": 26, "synthesis": 29, "verification": 24}
rows 229 files 230
missing_from_index 1 ['culture-material/masks-masquerade.md']
topic_mismatch 0 []
orphan_rows 0 []
header_drift {'culture-material': {'declared': 28, 'files': 29}}
totals_line 229 totals_ok False
footer_findings [{"class": "FOOTER_TOTAL", "declared": 229, "live": 230, ...},
                 {"class": "FOOTER_DIR_TOTALS", "declared": [28, 26, 28, 29, 24, 94], "live": [28, 26, 29, 29, 24, 94], ...}] footer_ok False
exit 1
```

Three separate README obligations were still open at that point: the index row (`missing_from_index 1`), the section header (`header_drift {'culture-material': {'declared': 28, 'files': 29}}`) and the counts footer (`FOOTER_TOTAL`, `FOOTER_DIR_TOTALS`).

Applying the fix this seat had already derived, on a copy of the live tree, clears every one of them:

```
rows 230 files 230
missing_from_index 0 []
topic_mismatch 0 []
orphan_rows 0 []
header_drift {}
totals_line 230 totals_ok True
footer_findings [] footer_ok True
exit 0
```

The index row's topic text must be the entry's own `- topic:` line, taken from the file itself (the landed entry's topic block is a single 474-character line). Copying the declared TOPIC string from `criterion11-controls.py` instead of the entry's actual topic would produce a topic mismatch, because the L1 wrote a longer, more specific topic than the controls' stand-in.

### 4A.1 The entry currently cites 47 draft ids, so the landing needs 47 registry rows, not 20

The landed entry cites draft ids, not S-ids:

```
distinct draft ids: 47
CARNIVAL1 CARNIVAL2 CARNIVAL3 COMMEDIA1 COMMEDIA2 DEATH1 DEATH2 GELEDE1 GELEDE2
KOLAM1 KOLAM2 KOLAM3 KOLAM4 KWAK1 KWAK2 MALAGAN1 MALAGAN2 MALAGAN3 MALAGAN4
MALAGAN5 MASKTHEORY1 MASKTHEORY2 NUO1 NUO2 NUO3 NUO4 NUO5 NUO6 PERSONA1 PERSONA2
PERSONA3 PERSONA4 ROMAN1 ROMAN2 ROMAN3 ROMAN4 ROMAN5 SACRED2 SACRED3 SOWEI1 SOWEI2
SOWEI3 VENICE1 VENICE2 VOICE1 VOICE2 VOICE3
```

FLOOR's floor is 20, but RANGE requires a row for **every** id the entry cites, not just 20 of them. Rehearsing the L1's entry with its draft ids replaced by S239 upward:

```
=== entry citing 47 S-ids, but only 20 registry rows ===
FLOOR PASS cited=47 floor=20
RANGE FAIL bad=['S259', 'S260', ..., 'S285'] range_notation=[]
accept-c.py exit 1

=== all 47 cited ids have their own registry row ===
SET PASS ... SWEEP PASS ... FLOOR PASS cited=47 floor=20 ... RANGE PASS bad=[] ...
accept-c.py exit 0
sources-census.sh validate exit 0
```

So the number of registry rows the landing needs is set by the number of distinct ids the entry cites (47 at this moment), not by the FLOOR floor of 20. If the L1 assigns S-numbers to only 20 of the draft ids and leaves the rest as draft names, the entry would cite ids that RANGE cannot see and the claim would still pass — but the entry's citations would then point at names the registry does not define. The clean form is one row per cited id, S239 upward, each `mined`, each naming the entry in its used-by cell.

This also updates finding 4.7: the registry will need 47 new rows on the current text, not 20.

### 4A.2 The drift detector now fires, correctly

The verifier was re-run after the L1's landing appeared. The eleven command and leg checks still read the sandbox clone at the declaration commit, so they still match. The twelfth, lane-drift, now reports:

```
$ git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin status --porcelain
?? .ufo/waves/round-54/build-a2/
?? corpus/knowledge/culture-material/masks-masquerade.md

paths differing from the declaration commit (untracked): [".ufo/waves/round-54/build-a2/", "corpus/knowledge/culture-material/masks-masquerade.md"]
claim-relevant paths among them: ["corpus/knowledge/culture-material/masks-masquerade.md"]
VERDICT lane-drift: DIFFERS (claim-relevant paths changed: corpus/knowledge/culture-material/masks-masquerade.md)
```

This is the detector working as intended: the claim's own land path has appeared since the declaration, so the lane is no longer at the declared before-state. The before-state verdict in section 2 stands on the sandbox clone at `7fa37fb`; this later DIFFERS records that the live lane has moved on, which is the expected consequence of the landing, not a defect in the declaration.

---

## 5. Code and fixtures written by this seat

All under `/fast/scratch/hyaku/kotodama-r54-a2/ExecDryRunCensus/`. Python 3 standard library only. No installs were needed and none were made.

| Path | What it is |
|---|---|
| `verify_before_state.py` | The verifier: clones the lane at the declaration commit, runs every declared command, and prints one verdict per command. |
| `fixtures/expected_before_state.json` | The expected values, each tagged with the declaration field or receipt line it comes from. |
| `rehearse_landing.py` | First landing rehearsal (found the footer and topic-equality obligations). |
| `rehearse_landing2.py` | Corrected rehearsal (found the Registry-section requirement). |
| `probe_traps.py` | The trap probes for the pre-S239 citation and the census on a landed tree. |
| `verify/`, `rehearse/`, `rehearse2/`, `probes/`, `traps2/`, `traps3/` | Scratch clones and captured outputs. |

### 5.1 `verify_before_state.py` (final source, 344 lines)

```python
#!/usr/bin/env python3
"""Re-verify the inherited round-54 declaration's before-state.

Seat: KotodamaR54a2.ExecDryRunCensus. Scope: read-only verification only. The
script creates its own sandbox clone, runs the declared commands there, and
prints one verdict per command. It writes nothing outside its own scratch
directory.

Usage (from anywhere):

  python3 -B verify_before_state.py --lane /path/to/kotodama-shokunin \
      --work /fast/scratch/hyaku/kotodama-r54-a2/ExecDryRunCensus/verify \
      --fixture fixtures/expected_before_state.json

Verdicts per command: MATCHES DECLARATION or DIFFERS (with the difference).
Stdlib only.
"""
import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
FIXTURE_DEFAULT = os.path.join(HERE, "fixtures", "expected_before_state.json")


# --------------------------------------------------------------------- utils

def run(argv, cwd):
    """(rc, stdout+stderr) for ARGV in CWD."""
    proc = subprocess.run(argv, cwd=cwd, capture_output=True, text=True)
    return proc.returncode, (proc.stdout + proc.stderr).rstrip("\n")


def sha256_of(path):
    with open(path, "rb") as handle:
        return hashlib.sha256(handle.read()).hexdigest()


def git(lane, *args):
    proc = subprocess.run(["git", "-C", lane] + list(args),
                          capture_output=True, text=True)
    return proc.returncode, proc.stdout.rstrip("\n"), proc.stderr.rstrip("\n")


def sandbox_clone(src, work, commit):
    """A fresh clone of SRC checked out at COMMIT; returns the clone path."""
    if os.path.exists(work):
        shutil.rmtree(work)
    os.makedirs(os.path.dirname(work) or ".", exist_ok=True)
    rc, out, err = git(src, "clone", "-q", src, work)
    if rc != 0:
        raise SystemExit("clone failed: %s" % err)
    rc, out, err = git(work, "checkout", "-q", commit)
    if rc != 0:
        raise SystemExit("checkout failed: %s" % err)
    return work


# --------------------------------------------------- declared-text comparison

LEG_RE = re.compile(r"^(\w+) (PASS|FAIL) (.*)$", re.M)
EXPECTED_LEG_RE = re.compile(r"\b(SET|SWEEP|FLOOR|RANGE|STATUS|USEDBY|ACCESS)\b")


def _item_verdict(item):
    """'PASS'/'FAIL' stated in ITEM, or None when ITEM names legs but no verdict."""
    for word in ("FAIL", "PASS"):
        if re.search(r"\b%s\b" % word, item):
            return word
    return None


def parse_expected_legs(expected_text):
    """Leg -> 'PASS'/'FAIL' implied by the declaration's expected_pre_landing text.

    The declaration writes "SET FAIL (count=229 added=[] removed=[]), SWEEP FAIL
    (exit 0 but rows 229 files 229), FLOOR FAIL (cited=0); RANGE, STATUS, USEDBY
    PASS vacuously; ACCESS PASS". A comma-separated item that names legs but
    states no verdict of its own takes the verdict of the item that follows it
    ("RANGE, STATUS, USEDBY PASS" gives all three PASS), so the parse is
    per-leg, not per-item.
    """
    legs = {}
    for group in expected_text.split(";"):
        items = group.split(",")
        verdicts = [_item_verdict(item) for item in items]
        for index, item in enumerate(items):
            names = EXPECTED_LEG_RE.findall(item)
            if not names:
                continue
            verdict = verdicts[index]
            if verdict is None:
                # Inherit forward, then backward.
                for later in range(index + 1, len(items)):
                    if verdicts[later] is not None:
                        verdict = verdicts[later]
                        break
                else:
                    for earlier in range(index - 1, -1, -1):
                        if verdicts[earlier] is not None:
                            verdict = verdicts[earlier]
                            break
            if verdict is None:
                continue
            for name in names:
                legs[name] = verdict
    return legs


def compare_legs(expected_text, actual_text):
    """(differences list, expected leg map, actual leg map)."""
    want = parse_expected_legs(expected_text)
    got = {}
    for name, verdict, detail in LEG_RE.findall(actual_text):
        got[name] = verdict
    diffs = []
    for name in sorted(set(want) | set(got)):
        w, g = want.get(name), got.get(name)
        if w != g:
            diffs.append("%s expected %s, got %s" % (name, w, g))
    return diffs, want, got


# --------------------------------------------------------------- the commands

def verify_commands(fixture, roots, out_lines):
    """Run every declared command; return (verdicts list, all_match bool)."""
    verdicts = []
    for spec in fixture["commands"]:
        cwd = roots[spec["cwd"]]
        rc, text = run(spec["argv"], cwd)
        out_lines.append("$ " + " ".join(spec["argv"]) + "   [cwd=%s]" % spec["cwd"])
        for line in text.splitlines():
            out_lines.append(line)
        out_lines.append("exit %d" % rc)

        diffs = []
        if rc != spec["expect_rc"]:
            diffs.append("exit expected %d, got %d" % (spec["expect_rc"], rc))
        for marker in spec.get("markers", []):
            if marker not in text:
                diffs.append("missing marker %r" % marker)
        for token in spec.get("forbid", []):
            if token in text:
                diffs.append("forbidden token present %r" % token)
        verdict = "MATCHES DECLARATION" if not diffs else "DIFFERS"
        if diffs:
            verdict += " (" + "; ".join(diffs) + ")"
        verdicts.append((spec["name"], verdict, rc, text))
        out_lines.append("VERDICT %s: %s" % (spec["name"], verdict))
        out_lines.append("")
    return verdicts


def verify_accept_c_legs(fixture, roots, out_lines):
    """Compare accept-c's per-leg verdicts with claims.json's declared text."""
    claims_path = os.path.join(roots["lane"], "reports", "round-54", "claims.json")
    with open(claims_path, encoding="utf-8") as handle:
        claims = json.load(handle)
    declared = claims["claims"][0]["expected_pre_landing_counting"]
    rc, text = run(["python3", "-B", "reports/round-54/accept-c.py"], roots["lane"])
    diffs, want, got = compare_legs(declared, text)
    out_lines.append("declared expected_pre_landing_counting: %s" % declared)
    out_lines.append("declared legs: %s" % json.dumps(want, sort_keys=True))
    out_lines.append("observed legs: %s" % json.dumps(got, sort_keys=True))
    verdict = "MATCHES DECLARATION" if not diffs else "DIFFERS (" + "; ".join(diffs) + ")"
    out_lines.append("VERDICT accept-c-legs: %s" % verdict)
    out_lines.append("")
    return verdict, rc, text


def verify_instrument_hashes(fixture, roots, out_lines):
    """Compare the five instrument hashes with the criterion-11 receipt."""
    expected = fixture["instrument_hashes"]["expected"]
    diffs = []
    for rel, want in sorted(expected.items()):
        path = os.path.join(roots["lane"], rel)
        got = sha256_of(path) if os.path.isfile(path) else "MISSING"
        out_lines.append("sha256 %s  %s" % (got, rel))
        if got != want:
            diffs.append("%s expected %s got %s" % (rel, want, got))
    verdict = "MATCHES DECLARATION" if not diffs else "DIFFERS (" + "; ".join(diffs) + ")"
    out_lines.append("VERDICT instrument-hashes: %s" % verdict)
    out_lines.append("")
    return verdict


def verify_gap_evidence(fixture, roots, out_lines):
    """Recount the declared gap evidence at base."""
    knowledge = os.path.join(roots["lane"], "corpus", "knowledge")
    counts = {}
    names = []
    for dirpath, _dirs, files in os.walk(knowledge):
        for name in files:
            names.append(os.path.join(dirpath, name))
    counts["filename owners (*mask* under corpus/knowledge)"] = sum(
        1 for p in names if "mask" in os.path.basename(p).lower())
    topic, mention = [], []
    for path in sorted(names):
        try:
            with open(path, encoding="utf-8", errors="replace") as handle:
                text = handle.read()
        except OSError:
            continue
        if re.search(r"^- topic:.*(mask|masquerad)", text, re.M):
            topic.append(os.path.relpath(path, knowledge))
        if re.search(r"\bmask(s|ed|ing)?\b|masquerade", text, re.I):
            mention.append(os.path.relpath(path, knowledge))
    counts["topic-line owners (^- topic:.*(mask|masquerad))"] = len(topic)
    counts["files with passing mentions (\\bmask(s|ed|ing)?\\b|masquerade)"] = len(mention)
    diffs = []
    for spec in fixture["gap_evidence_at_base"]["expectations"]:
        got = counts.get(spec["label"])
        out_lines.append("gap count %-72s expect %s got %s"
                         % (spec["label"], spec["expect"], got))
        if got != spec["expect"]:
            diffs.append("%s expected %s got %s" % (spec["label"], spec["expect"], got))
    out_lines.append("topic-line owners are: %s" % ", ".join(topic))
    verdict = "MATCHES DECLARATION" if not diffs else "DIFFERS (" + "; ".join(diffs) + ")"
    out_lines.append("VERDICT gap-evidence: %s" % verdict)
    out_lines.append("")
    return verdict


def verify_lane_drift(fixture, lane, out_lines):
    """Which paths differ from the declaration commit, and are they claim-relevant?"""
    commit = fixture["declaration_commit"]
    rc, stat, err = git(lane, "diff", "--stat", commit)
    out_lines.append("$ git -C %s diff --stat %s" % (lane, commit))
    for line in stat.splitlines():
        out_lines.append(line)
    out_lines.append("exit %d" % rc)
    rc, status, err = git(lane, "status", "--porcelain")
    out_lines.append("$ git -C %s status --porcelain" % lane)
    for line in status.splitlines():
        out_lines.append(line)
    out_lines.append("exit %d" % rc)

    rc, names, err = git(lane, "diff", "--name-only", commit)
    changed = [n for n in names.splitlines() if n]
    untracked = []
    for line in status.splitlines():
        if line.startswith("??"):
            untracked.append(line[3:].strip())
    watch = set(fixture["claim_land_set"]) | set(fixture["instrument_paths"])
    relevant = sorted(n for n in changed + untracked if n in watch)
    out_lines.append("paths differing from the declaration commit (tracked): %s"
                     % json.dumps(changed))
    out_lines.append("paths differing from the declaration commit (untracked): %s"
                     % json.dumps(untracked))
    out_lines.append("claim-relevant paths among them: %s" % json.dumps(relevant))
    verdict = ("MATCHES DECLARATION" if not relevant
               else "DIFFERS (claim-relevant paths changed: %s)" % ", ".join(relevant))
    out_lines.append("VERDICT lane-drift: %s" % verdict)
    out_lines.append("")
    return verdict, changed, untracked, relevant


# ------------------------------------------------------------------- selftest

def selftest():
    """The leg parser is this seat's own code; check it on hand-written cases."""
    cases = [
        ("exit 1: SET FAIL (count=229 added=[] removed=[]), SWEEP FAIL (exit 0 but rows 229 files 229), FLOOR FAIL (cited=0); RANGE, STATUS, USEDBY PASS vacuously; ACCESS PASS",
         {"SET": "FAIL", "SWEEP": "FAIL", "FLOOR": "FAIL", "RANGE": "PASS",
          "STATUS": "PASS", "USEDBY": "PASS", "ACCESS": "PASS"}),
        ("all seven legs PASS (exit 0): count 230, added [masks-masquerade.md], removed [], rows 230 files 230, missing_from_index 0, cited >= 20, no bad S-id",
         {}),
        ("SET FAIL, ACCESS PASS", {"SET": "FAIL", "ACCESS": "PASS"}),
        ("RANGE FAIL, STATUS PASS", {"RANGE": "FAIL", "STATUS": "PASS"}),
        ("SET, SWEEP PASS", {"SET": "PASS", "SWEEP": "PASS"}),
    ]
    failures = 0
    for text, want in cases:
        got = parse_expected_legs(text)
        ok = got == want
        failures += not ok
        print("%s parse %r -> %s" % ("PASS" if ok else "FAIL", text[:48], json.dumps(got, sort_keys=True)))
    print("SELFTEST: %d/%d pass" % (len(cases) - failures, len(cases)))
    return 1 if failures else 0


# ------------------------------------------------------------------- the main

def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--lane", help="the lane repo to verify")
    ap.add_argument("--work", help="scratch dir for the sandbox clone")
    ap.add_argument("--fixture", default=FIXTURE_DEFAULT)
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args(argv)

    if args.selftest:
        return selftest()
    if not args.lane or not args.work:
        ap.error("--lane and --work are required unless --selftest")

    with open(args.fixture, encoding="utf-8") as handle:
        fixture = json.load(handle)

    lane = os.path.abspath(args.lane)
    clone = sandbox_clone(lane, os.path.join(args.work, "clone"), fixture["declaration_commit"])
    roots = {"lane": clone, "real-lane": lane}

    out_lines = ["# round-54 before-state re-verification, seat ExecDryRunCensus",
                 "# declaration commit %s" % fixture["declaration_commit"],
                 "# sandbox clone %s" % clone,
                 ""]

    accept_verdict, accept_rc, accept_text = verify_accept_c_legs(fixture, roots, out_lines)
    verdicts = verify_commands(fixture, roots, out_lines)
    hash_verdict = verify_instrument_hashes(fixture, roots, out_lines)
    gap_verdict = verify_gap_evidence(fixture, roots, out_lines)
    drift_verdict, changed, untracked, relevant = verify_lane_drift(fixture, lane, out_lines)

    summary = [accept_verdict] + [v for _n, v, _rc, _t in verdicts] + [
        hash_verdict, gap_verdict, drift_verdict]
    all_match = all(v.startswith("MATCHES") for v in summary)
    out_lines.append("SUMMARY %d checks, %s"
                     % (len(summary), "ALL MATCH THE DECLARATION" if all_match
                        else "DIFFERENCES FOUND"))
    for name, verdict, rc, _t in verdicts:
        out_lines.append("  %-24s exit %d  %s" % (name, rc, verdict))
    out_lines.append("  %-24s        %s" % ("accept-c-legs", accept_verdict))
    out_lines.append("  %-24s        %s" % ("instrument-hashes", hash_verdict))
    out_lines.append("  %-24s        %s" % ("gap-evidence", gap_verdict))
    out_lines.append("  %-24s        %s" % ("lane-drift", drift_verdict))

    text = "\n".join(out_lines) + "\n"
    sys.stdout.write(text)
    out_path = os.path.join(args.work, "before-state-report.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as handle:
        handle.write(text)
    return 0 if all_match else 1


if __name__ == "__main__":
    sys.exit(main())
```

### 5.2 The fixture, `fixtures/expected_before_state.json`

Every expected value carries the declaration field or receipt line it comes from, so no target was invented:

```json
{
  "schema": "kotodama-r54-before-state-fixture-v1",
  "note": "Expected values for the inherited round-54 declaration (commit 7fa37fbb6f0a0c39b3d6cfd3d371f5bb3a65050c). Every entry records where the expectation comes from, so the verifier never invents a target.",
  "declaration_commit": "7fa37fbb6f0a0c39b3d6cfd3d371f5bb3a65050c",
  "claim_id": "C",
  "commands": [
    {
      "name": "accept-c",
      "argv": ["python3", "-B", "reports/round-54/accept-c.py"],
      "cwd": "lane",
      "expect_rc": 1,
      "declared_by": "reports/round-54/claims.json -> claims[0].expected_pre_landing_counting",
      "markers": [
        "SET FAIL count=229 required=230 added=[] removed=[]",
        "SWEEP FAIL exit=0 rows 229 files 229 missing_from_index 0 []",
        "FLOOR FAIL cited=0 floor=20",
        "RANGE PASS bad=[] range_notation=[]",
        "STATUS PASS bad=[]",
        "USEDBY PASS bad=[]",
        "ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings"
      ]
    },
    {
      "name": "dry-run-run",
      "argv": ["python3", "-B", "reports/round-54/dry-run.py", "run", "--label", "ExecDryRunCensus before-state re-verification"],
      "cwd": "lane",
      "expect_rc": 0,
      "declared_by": "reports/round-54/claims.json -> dry_run_rule (QUALITY criterion 9); role expectations are the declared strings",
      "markers": [
        "$ python3 -B reports/round-54/accept-c.py",
        "$ python3 -B tools/check-claim-separability.py reports/round-54/separability-manifest.json",
        "$ python3 -B reports/round-54/claims-agree.py",
        "SEPARABILITY_INPUT_ERROR unit C lands 'corpus/knowledge/culture-material/masks-masquerade.md'",
        "AGREE claims=['C']"
      ],
      "forbid": ["MISSING_FROM_RECEIPT", "UNDECLARED_IN_RECEIPT"]
    },
    {
      "name": "dry-run-check",
      "argv": ["python3", "-B", "reports/round-54/dry-run.py", "check", "reports/round-54/telemetry/declaration-dry-run.txt"],
      "cwd": "lane",
      "expect_rc": 0,
      "declared_by": "reports/round-54/dry-run.py check mode: two-way receipt check, exit 0 only when both lists are empty",
      "markers": ["MISSING_FROM_RECEIPT []", "UNDECLARED_IN_RECEIPT []"]
    },
    {
      "name": "separability",
      "argv": ["python3", "-B", "tools/check-claim-separability.py", "reports/round-54/separability-manifest.json"],
      "cwd": "lane",
      "expect_rc": 2,
      "declared_by": "reports/round-54/claims.json -> dry-run.py separability role: exit 2 before landing, SEPARABILITY_INPUT_ERROR naming the absent C land",
      "markers": [
        "SEPARABILITY_INPUT_ERROR unit C lands 'corpus/knowledge/culture-material/masks-masquerade.md', which is absent from the worktree"
      ]
    },
    {
      "name": "claims-agree",
      "argv": ["python3", "-B", "reports/round-54/claims-agree.py"],
      "cwd": "lane",
      "expect_rc": 0,
      "declared_by": "reports/round-54/claims.json -> dry-run.py agreement role: AGREE, exit 0",
      "markers": ["AGREE claims=['C']"]
    },
    {
      "name": "check-source-access",
      "argv": ["python3", "-B", "tools/check-source-access.py"],
      "cwd": "lane",
      "expect_rc": 0,
      "declared_by": "reports/round-54/claims.json -> claims[0].before: ACCESS PASS (check-source-access exit 0)",
      "markers": ["ACCESS: 2 flagged rows, 0 findings"]
    },
    {
      "name": "readme-sweep",
      "argv": ["python3", "-B", "reports/round-28/readme/sweep.py"],
      "cwd": "lane",
      "expect_rc": 0,
      "declared_by": "reports/round-54/claims.json -> claims[0].expected_pre_landing_counting: SWEEP FAIL (exit 0 but rows 229 files 229)",
      "markers": ["rows 229 files 229", "missing_from_index 0 []", "totals_line 229 totals_ok True"]
    },
    {
      "name": "sources-census-validate",
      "argv": ["/home/vgpnk/Projects/shokunin/scripts/sources-census.sh", "validate", "--root", "/home/vgpnk/Projects/shokunin", "kotodama"],
      "cwd": "real-lane",
      "expect_rc": 0,
      "declared_by": "reports/round-54/telemetry/census-start-a2.txt (the attempt-2 start census of the same command on the same lane tip)",
      "markers": ["kotodama\tok\t"]
    }
  ],
  "instrument_hashes": {
    "source": "reports/round-54/telemetry/criterion11-controls.txt (sha256 lines)",
    "expected": {
      "reports/round-54/accept-c.py": "ceadf2c68313bc82c4299e11f356aeb148a07531e7600f9453e60f9f0f466160",
      "reports/round-54/base-knowledge-files.txt": "ce217cb7b24ed382ce8ed06ccaf14d593fadfeea454c1b4d755c04e5de2c9f37",
      "reports/round-28/readme/sweep.py": "9b2ccac0046831fdaf48863ccd0ff6ca0fa390d044746c876e83a71c06f0cdd3",
      "tools/check-source-access.py": "fb915386a781b332ae4d73e6d81b2e441ad0d9cd264d8c10421b0c01cd973bd5",
      "reports/round-54/criterion11-controls.py": "d4223b4fbc6f98a066806c46b3fd97d6b77be2d81f7481770ec52a5687697a7d"
    }
  },
  "gap_evidence_at_base": {
    "source": "reports/round-54/claims.json -> claims[0].gap_evidence_at_base",
    "expectations": [
      {"label": "filename owners (*mask* under corpus/knowledge)", "expect": 0},
      {"label": "topic-line owners (^- topic:.*(mask|masquerad))", "expect": 1},
      {"label": "files with passing mentions (\\bmask(s|ed|ing)?\\b|masquerade)", "expect": 41}
    ]
  },
  "claim_land_set": [
    "corpus/knowledge/culture-material/masks-masquerade.md",
    "corpus/README.md",
    "corpus/SOURCES.md"
  ],
  "instrument_paths": [
    "reports/round-54/accept-c.py",
    "reports/round-54/base-knowledge-files.txt",
    "reports/round-28/readme/sweep.py",
    "tools/check-source-access.py",
    "reports/round-54/criterion11-controls.py",
    "reports/round-54/claims.json",
    "reports/round-54/separability-manifest.json",
    "reports/round-54/claims-agree.py",
    "reports/round-54/dry-run.py"
  ]
}
```

---

## 6. Runs of this seat's own scripts

### 6.1 Parser selftest

```
$ python3 -B verify_before_state.py --selftest
PASS parse 'exit 1: SET FAIL (count=229 added=[] removed=[])' -> {"ACCESS": "PASS", "FLOOR": "FAIL", "RANGE": "PASS", "SET": "FAIL", "STATUS": "PASS", "SWEEP": "FAIL", "USEDBY": "PASS"}
PASS parse 'all seven legs PASS (exit 0): count 230, added [' -> {}
PASS parse 'SET FAIL, ACCESS PASS' -> {"ACCESS": "PASS", "SET": "FAIL"}
PASS parse 'RANGE FAIL, STATUS PASS' -> {"RANGE": "FAIL", "STATUS": "PASS"}
PASS parse 'SET, SWEEP PASS' -> {"SET": "PASS", "SWEEP": "PASS"}
SELFTEST: 5/5 pass
exit 0
```

The first draft of the parser assigned no verdict to the legs named before the shared "PASS vacuously" word and reported a false DIFFERS on RANGE and STATUS. The parser was corrected to inherit a shared verdict forward, and the selftest now covers that case explicitly.

### 6.2 The verifier, final run

```
$ python3 -B verify_before_state.py --lane /home/vgpnk/Projects/shokunin/kotodama-shokunin \
      --work /fast/scratch/hyaku/kotodama-r54-a2/ExecDryRunCensus/verify \
      --fixture fixtures/expected_before_state.json
```

Full output is reproduced in section 2 above, command by command. Its summary block:

```
SUMMARY 12 checks, ALL MATCH THE DECLARATION
  accept-c                 exit 1  MATCHES DECLARATION
  dry-run-run              exit 0  MATCHES DECLARATION
  dry-run-check            exit 0  MATCHES DECLARATION
  separability             exit 2  MATCHES DECLARATION
  claims-agree             exit 0  MATCHES DECLARATION
  check-source-access      exit 0  MATCHES DECLARATION
  readme-sweep             exit 0  MATCHES DECLARATION
  sources-census-validate  exit 0  MATCHES DECLARATION
  accept-c-legs                   MATCHES DECLARATION
  instrument-hashes               MATCHES DECLARATION
  gap-evidence                    MATCHES DECLARATION
  lane-drift                      MATCHES DECLARATION
exit 0
```

The script exits 0 when every check matches the declaration and 1 otherwise.

### 6.3 The rehearsal scripts

```
$ python3 -B rehearse_landing.py --lane ... --work .../rehearse --commit 7fa37fb     exit 0
$ python3 -B rehearse_landing2.py --work .../rehearse2                              exit 0
$ python3 -B probe_traps.py --work .../probes                                        exit 0
```

Outputs are quoted in section 4.

---

## 7. Risks, blockers and scope notes

**No blocker.** The assignment is complete: every declared command was run in a sandbox clone at the declaration commit, every output and exit code is pasted above, and every command carries a MATCHES DECLARATION verdict.

**No tool was installed or upgraded.** Every command in this seat ran with the Python 3 standard library and with tools already on the host. Nothing to record under the tooling directive.

**No lane file was written by this seat.** The seat wrote only its report file and files under its scratch directory. `git status --porcelain` on the lane shows the untracked wave report directory (which also holds the other build-a2 seat reports) and, since the L1 began integrating concurrently, the untracked `corpus/knowledge/culture-material/masks-masquerade.md` — the L1's work, not this seat's. The L1's README and SOURCES.md edits were not present at the time this seat finished its checks. No jj command was run at the fleet root; only read-only `git` in the lane and in scratch clones.

**What this seat did not do, by design.** It did not write the entry, the registry rows or the README index row — the L1 owns those, and the L1's integration is where the findings in section 4 apply. It did not run any build, lint, test or formatter against the lane: the parent owns the post-integration gate.

**Residual risk on the findings themselves.** Section 4's landing-path results come from a stand-in landing (a synthetic entry and synthetic registry rows) in a scratch clone, not from the real entry. The behaviours measured are properties of the instruments — the regex in `accept-c.py`, the footer and topic checks in `sweep.py`, the section scan in `sources-census.sh`, the marker patterns in `check-source-access.py` — and those instruments are byte-identical to the ones the claim will be measured with, as the sha256 lines in section 2.8 confirm. The rehearsal's stand-in content is not a claim about what the real entry will say.

**One judgement left to the L1.** The declaration's `after_required` describes the landing outcome but not the README obligations, the registry-section placement, the id spelling or the access-phrasing rules that the seven legs and the fleet census actually enforce. Sections 4.1 to 4.6 are the L1's to act on; this seat did not amend the declaration, since the claim instrument is the L1's to change and the before-state it certifies is correct as it stands.
