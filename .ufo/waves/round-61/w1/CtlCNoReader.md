# CtlCNoReader — claim C quote-only writing shortcut

## Result and axes

**CONTROL-MET**, using `mutant-entry.md` with the permitted FLOOR-only probe. The no-reader writing mutant **SURVIVED**: pristine, mutated and byte-restored entries all passed the same `FLOOR = 3` detector. All three failed the frozen detector only at FLOOR (3 < 20), so the frozen runs are **INCONCLUSIVE as mutation kills**, not successful rejection of the writing defect. No frozen 20-row PASS is claimed.

Axes: coverage discrimination (source acquisition versus sentence writing), honest live provenance, reproducibility, and exact restoration. One deterministic mutant was tried; no output wording was hand-repaired or selected through repeated generation.

Revision: `78ad4b176695e9fcd490ab607cb8218e2ce62738`.
Scratch root: `/fast/scratch/hyaku/kotodama-r61/CtlCNoReader/`.
Isolated clone: `/fast/scratch/hyaku/kotodama-r61/CtlCNoReader/clone`.

## Mutant and expected detector

The single defect is replacing three human-written restatement bullets with six quote words sampled/shuffled deterministically from each row's id and quote. Only the three cited entry lines changed between pristine and mutant fixtures. The rows, URLs, index, metadata and locator stayed identical.

Expected detector: the clone's `reports/round-61/accept-c.py`, run on pristine, mutated and restored entry bytes with the identical bounded command:

```sh
timeout 900 python3 -B reports/round-61/accept-c.py; echo exit=$?
```

Each invocation used the clone as its working directory. The frozen instrument should fail the three-row fixture at FLOOR. The probe changes only FLOOR to 3; a discriminator for authored restatements would reject the shuffled word lists, but the frozen mechanics have no semantic-support leg. LINES checks bullet/id shape, LINK shared words, and COPY consecutive copying. Thus survival under the allowed probe is the relevant finding, not a changed contract.

### Honest sources acquired by this seat

I opened the selected public V&A HTML pages by ordinary read requests and selected these verbatim body quotes. The quote-only generator does not open pages, infer meaning, consult the baseline wording, or use a prose model. “No reader” describes **entry-line production**, not source acquisition: I did read the source pages to obtain honest anchors.

- S652, [V&A Pair of chopines, O74599](https://collections.vam.ac.uk/item/O74599/pair-of-chopines-unknown/), Summary, first sentence: “Shoes of this type are called chopines or pantobles in England.” (12 words.)
- S653, [V&A Chopines and Geta](https://www.vam.ac.uk/museumofsavagebeauty/rel/chopines-and-geta/), first body paragraph, final sentence: “The chopine denoted wealth and privilege, but also had sexual allure.” (12 words.)
- S654, [V&A Pair of geta (shoes), O1302324](https://collections.vam.ac.uk/item/O1302324/pair-of-geta/), Gallery label, Cover for Winter, first full sentence: “Traditionally, Japanese men and women wore thonged wooden clogs, or geta.” (12 words.)

A registry search for `O74599|museumofsavagebeauty|O1302324` in the frozen clone's `corpus/SOURCES.md` returned `No matches found`; FRESH also passed every behavioral run. The three fixture rows are mined, opened 2026-10-23 and used-by the requested entry path. They are preserved in `source-rows.md`.

Each selected anchor was checked with an individual `timeout 300 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-61/reopen-quote.py URL QUOTE` invocation. Actual stdout:

```text
LOCATED https://collections.vam.ac.uk/item/O74599/pair-of-chopines-unknown/
LOCATED https://www.vam.ac.uk/museumofsavagebeauty/rel/chopines-and-geta/
LOCATED https://collections.vam.ac.uk/item/O1302324/pair-of-geta/
```

The counter independently reopened all three rows in each run below. No browser, challenge solver, login, archive detour or PDF extraction was used for the selected sources. An unused Met candidate returned HTTP 429; it was not used or bypassed. An unused V&A blog read returned a comments feed; none of its text entered this fixture.

### Program

Saved as `/fast/scratch/hyaku/kotodama-r61/CtlCNoReader/generate-lines.py` (SHA-256 `d3caf3eceb2c93f322a6118026c9c4548dddc5f49513b24bf05f6dc1477a16fb`):

```python
#!/usr/bin/env python3
"""Emit cited bullets from row id plus anchor quote; no URLs, reading, or prose model."""
import json
import random
import re
import sys
import unicodedata

for row in json.load(open(sys.argv[1], encoding="utf-8")):
    words = re.findall(r"[^\W\d_]+", unicodedata.normalize("NFKC", row["quote"]).casefold())
    words = list(dict.fromkeys(word for word in words if len(word) >= 4))
    random.Random(row["id"]).shuffle(words)
    print(f"- {' '.join(words[:6])}. ({row['id']})")
```

Input: `rows.json` (SHA-256 `bbd11eae446262dc69537251a38f71e9696cd0254b7f02d4afd337535f4893fa`). Its URL/title/baseline fields are fixture documentation; the generator accesses only `id` and `quote`.

Actual command:

```sh
timeout 30 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCNoReader/generate-lines.py /fast/scratch/hyaku/kotodama-r61/CtlCNoReader/rows.json
```

Actual stdout, used verbatim as the mutant's cited lines:

```text
- called shoes england this pantobles chopines. (S652)
- also wealth privilege allure chopine sexual. (S653)
- geta traditionally japanese clogs wooden thonged. (S654)
```

These are token lists, not three authored, source-supported clauses. Nevertheless, all LINES, LINK and COPY legs passed. The baseline comparator used these hand-written sentences:

```text
- In England, these shoes bear the names chopines or pantobles. (S652)
- Wealth and privilege were denoted by the chopine. (S653)
- Japanese men and women traditionally wore wooden thonged clogs called geta. (S654)
```

### Probe diff

No TOTAL, base-list, locator, lexicon or other counter change was made. The same temporary constant edit was used for all three phases, then reverted.

```diff
--- frozen/reports/round-61/accept-c.py
+++ probe/reports/round-61/accept-c.py
@@ -57 +57 @@
-FLOOR = 20
+FLOOR = 3
```

Frozen counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`.
Probe counter SHA-256: `71f91748f4e69664038d0dfbf9f80c77875c1cf652a498fea2bf8d3cf7402749`.

## Full behavioral outputs, chronological

### 1. Pristine entry, frozen counter

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=3 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=3 bad=[]
TOPIC PASS rows=3 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=3 cited=3 need=3 at=2026-10-23T09:44Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### 2. Pristine entry, FLOOR probe

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=3 floor=3
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=3 bad=[]
TOPIC PASS rows=3 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=3 cited=3 need=3 at=2026-10-23T09:44Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
```

### 3. No-reader mutant, FLOOR probe

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=3 floor=3
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=3 bad=[]
TOPIC PASS rows=3 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=3 cited=3 need=3 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
```

### 4. No-reader mutant, frozen counter

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=3 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=3 bad=[]
TOPIC PASS rows=3 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=3 cited=3 need=3 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### 5. Byte-restored pristine entry, frozen counter

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=3 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=3 bad=[]
TOPIC PASS rows=3 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=3 cited=3 need=3 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### 6. Byte-restored pristine entry, FLOOR probe

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=3 floor=3
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=3 bad=[]
TOPIC PASS rows=3 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=3 cited=3 need=3 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
```

## Required receipts and scoped verdict

The `counter-sha256` field names the frozen run; every paired probe used SHA-256 `71f91748f4e69664038d0dfbf9f80c77875c1cf652a498fea2bf8d3cf7402749` and exited 0. `stopped-by` lists frozen failures; no probe leg failed.

```text
RECEIPT CtlCNoReader/pristine counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=PASS stopped-by=FLOOR
RECEIPT CtlCNoReader/no-reader counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=PASS stopped-by=FLOOR
RECEIPT CtlCNoReader/restored counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=PASS stopped-by=FLOOR
CONTROL-MET CtlCNoReader/no-reader fixture=/fast/scratch/hyaku/kotodama-r61/CtlCNoReader/mutant-entry.md via=FLOOR-only-probe
```

What the control still did: discover three real on-topic sources, open them, select actual body quotes, check URL freshness, locate every quote live, create properly shaped source rows, and index the new entry. It does **not** demonstrate skipping research or provenance work.

What it skipped: writing three supported restatement clauses, understanding the sampled words' relation, and building usable explanatory prose. The program blindly reused quote vocabulary and ids; none of its three output bullets is a normal authored clause. The hand-written baseline was only the comparator, not an input to generation.

Because line wording beyond shared tokens is explicitly review-only (`claims.json` and the counter docstring), this shortcut reaches the declared FLOOR probe while omitting sentence-writing work. [INFERENCE] With 20 otherwise-valid honest rows, the same strategy can satisfy the unchanged count while continuing to skip semantic writing: the observed wording checks do not measure it. That 20-row outcome was **not exercised**, and a future source/URL/fetch failure could still stop it. This is a coverage-discrimination finding for the writing dimension, not a claim that all sourced-coverage work can be bypassed, not a lane acceptance judgment, and not permission to alter the frozen predicate.

## Hashes and exact restoration

Entry SHA-256 sequence (measured):

```text
pristine da398bc61aaf66651b69ce8a5e22ca2977e39ba336632d67e7b3d56a319128eb
mutated  b28ab8a93ab55edbe64b4fd46632af4d27c890d9b9b88d63bacadbc0f199c1d8
restored da398bc61aaf66651b69ce8a5e22ca2977e39ba336632d67e7b3d56a319128eb
```

During the mutation, unchanged fixture supporting bytes measured:

```text
5ca87e5f8648f7d6ca1cd39a25157dc23153a8faef973778c8efe72e9929394d  corpus/README.md
4fb737f8d042a72e781db7ffd4319015f091e80174b23a9b306155df1d8f4551  corpus/SOURCES.md
```

After the restored-phase detector runs, all fixture additions were removed from the clone and all touched existing files restored. Initial and final clone hashes matched exactly:

```text
0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10  reports/round-61/accept-c.py
cdf71cb38155712fe3fdaeefae828622761837a7ba2a12d0d00dd931ad98f53d  reports/round-61/reopen-quote.py
a7fc403cf0f2908581926515d70c5b358afb504ac132bde3e1a0987e5870352c  corpus/README.md
641115af3777359d9b42cce28a249f7ce6807df601e543b4f5a867c74d7af485  corpus/SOURCES.md
entry_absent_exit=0
```

The absence check was `timeout 30 test ! -e corpus/knowledge/culture-material/footwear-codes-terminology.md; echo entry_absent_exit=$?`. The frozen tree had no such file; the clone again has none.

Preserved reconstruction artifacts, all under the scratch root: `rows.json`, `generate-lines.py`, `pristine-entry.md`, `mutant-entry.md`, `source-rows.md`, `fixture.patch`, and `probe.diff`. The entry snapshots' hashes matched the measured pristine/mutated clone bytes. The patch records index changes and original row insertion location.

No installs or updates. No delegation, background jobs or services were started; all bounded commands returned. No git/jj writes occurred in the lane or fleet repository. This report is the only lane file written by this seat. Probe complete.
