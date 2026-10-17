# R10-C23 — auditor: linguistics + verification partition counts and index-vs-files diff

- seat: R10-C23 auditor. lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
  assignment: *linguistics+verification partition counts (command-carried) +
  index-vs-files diff*; deliverable `reports/round-10/coverage/audit-ling-verif.md`.
- date: 2026-10-17, local clock UTC−03:00 (= UTC−3); all times below in UTC unless
  marked local. T0 measurement window opens 21:27:00Z (first audit command) and
  closes 21:30:02Z (last T0 command). T1 post-landing window opens 21:41:20Z
  (first post-landing command) and closes 21:47:45Z (final stability command);
  the poll watch ran 21:28:20Z–21:47:37Z (`.scratch/poll-ling-verif.sh`, 60 s
  cadence, exit 0). T1 block in §5.
- role limits: this seat counts and diffs. Its only write is this file (plus
  scratch under `.scratch/`). It admits no claim, edits no corpus file, and
  absorbs no sibling fragment's evidence as its own. It does not judge new-entry
  quality (that is R10-C11..C20 reviewers) or index-row prose (R10-C21/C22).
- revision binding: `git rev-parse HEAD` = `e3a1ec9435787328ac9f828f96cb6390e4916b8f`
  ("round-10: availability attempt 3", 2026-10-17 18:24 local); declared round-10
  `baseline_revision` = `9dc18ec1339bffd6f81e74f1a5742464ef578749` ("round-9:
  admit F/O/D", 2026-10-17 18:17:00 −0300; `reports/round-10/claims.json`).
  `git diff --name-only 9dc18ec… -- corpus/knowledge/linguistics
  corpus/knowledge/verification` is empty at T0 (§2.1) — every count below
  grades bytes identical under both revisions.

## 1. Verdict

1. **linguistics and verification are unchanged from the round-9 close.** Live
   counts T0: linguistics **16**, verification **13** — identical to the declared
   baseline tree (`git ls-tree` at `9dc18ec…`, §2.1) and to the round-10 C-claim
   `before` statement ("linguistics 16 … verification 13", `reports/round-10/claims.json`).
2. **Index-vs-files is exact for both partitions, both directions.** On-disk
   files, `corpus/README.md` index rows, and section-header annotations agree
   16=16=16 and 13=13=13; zero files missing from the index, zero index rows
   without a file, zero duplicate rows (two independent parsers, §2.3).
3. **README count claims about the whole corpus hold.** Header annotations
   (6 sections) and the footer total line (`corpus/README.md:273` — "Total
   knowledge entries: 179.") match live counts 16/16/16/24/13/94 = 179 under
   three independent methods (§2.2).
4. **All 29 existing entries in the two partitions carry the five frontmatter
   fields** (`topic`, `sources`, `verified-at`, `recheck`, `couples`), so the
   round-8/9 header profile the round-10 authors must match is intact (§2.4).
   This is a field-presence sweep only; it does not judge field content.
5. **No new round-10 entry had landed in either partition at T0; at T1 all
   five had landed and the index matches.** At 21:30:02Z
   `git status --porcelain -- corpus/knowledge` was empty (new=0) — the
   C-claim's "≥2 new entries per thin partition" was **not yet satisfied at
   T0**, a scheduling fact, not a finding against any worker. T1 (§5):
   linguistics 19 = 16+3, verification 15 = 13+2, index-vs-files clean in both
   directions, README total 189 = 179+10, digests stable 21:41:20Z–21:47:45Z.

## 2. Commands and outputs (T0, 2026-10-17)

### 2.1 Baseline identity

```
$ git rev-parse HEAD
e3a1ec9435787328ac9f828f96cb6390e4916b8f
$ git show -s --format='%h %ci %s' 9dc18ec1339bffd6f81e74f1a5742464ef578749
9dc18ec 2026-10-17 18:17:00 -0300 round-9: admit F/O/D — escalated residuals, 7/7 gate baselines, D3 acceptance
$ git diff --name-only 9dc18ec1339bffd6f81e74f1a5742464ef578749 -- corpus/knowledge/linguistics corpus/knowledge/verification
(empty)
$ for p in linguistics verification; do
    printf "%s: " "$p"; git ls-tree -r --name-only 9dc18ec1339bffd6f81e74f1a5742464ef578749 -- corpus/knowledge/$p | grep -c '\.md$'; done
linguistics: 16
verification: 13
```

### 2.2 Independent counts (three methods)

Method A — `find` (files only, `.md`, non-recursive):

```
$ for p in linguistics verification; do
    printf "%-14s %s\n" "$p" "$(find corpus/knowledge/$p -maxdepth 1 -type f -name '*.md' | wc -l)"; done
linguistics    16
verification   13
$ for p in linguistics myth-symbol culture-material synthesis verification civilizations; do
    printf "%-18s %s\n" "$p" "$(find corpus/knowledge/$p -maxdepth 1 -type f -name '*.md' | wc -l)"; done
linguistics        16
myth-symbol        16
culture-material   16
synthesis          24
verification       13
civilizations      94
```

Method B — Python `os.listdir` + README section parser (`.scratch/audit-ling-verif.py`,
reproducible: parse `^## ([a-z-]+)/ \((\d+)\)` sections, collect `^- \`([^\`]+\.md)\``
rows, diff against `sorted(os.listdir('corpus/knowledge/<part>'))`):

```
$ python3 .scratch/audit-ling-verif.py
linguistics        actual= 16 index_rows= 16 header=16 files_not_indexed=[] rows_without_file=[]
verification       actual= 13 index_rows= 13 header=13 files_not_indexed=[] rows_without_file=[]
(myth-symbol 16/16/16, culture-material 16/16/16, synthesis 24/24/24, civilizations 94/94/94 likewise clean)
grand_total_actual=179 readme_total_line=179 matches=True
```

Method C — the lane's own inventory tool (the command the README footer cites,
`corpus/README.md:275-277`):

```
$ python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge
totals: files=179 files_with_any_mark=128 files_with_marker=118 lines=33021
        raw_lines=610 raw_occurrences=616 ci_occurrences=618 case_variant_occurrences=2
        marker_occurrences=584 bare_marker_occurrences=555 detailed_marker_occurrences=29
        marker_lines=581 unparenthesized_occurrences=34
per-directory (same JSON file list): civilizations 94, culture-material 16, linguistics 16,
        myth-symbol 16, synthesis 24, verification 13  → total 179
```

All three methods agree: linguistics 16, verification 13, corpus total 179.
The README footer's own claim ("total 179 files; directory totals remain
16/16/16/24/13/94", `corpus/README.md:277`) is therefore current at T0.

### 2.3 Index-vs-files diff (`corpus/README.md`)

Method 1 — `awk` section extraction + `comm` (both directions per partition):

```
$ for part in linguistics verification; do
    comm -23 <(find corpus/knowledge/$part -maxdepth 1 -type f -name '*.md' -printf '%f\n' | sort) \
             <(awk -v p="## $part/" '$0 ~ "^"p {insec=1; next} insec && /^## / {exit} \
                insec && /^- `[^`]+\.md`/ {match($0, /`[^`]+\.md`/); print substr($0, RSTART+1, RLENGTH-2)}' corpus/README.md | sort)
    comm -13 <(find corpus/knowledge/$part -maxdepth 1 -type f -name '*.md' -printf '%f\n' | sort) \
             <(awk -v p="## $part/" '$0 ~ "^"p {insec=1; next} insec && /^## / {exit} \
                insec && /^- `[^`]+\.md`/ {match($0, /`[^`]+\.md`/); print substr($0, RSTART+1, RLENGTH-2)}' corpus/README.md | sort)
  done
(files-not-in-index: empty; index-rows-without-file: empty — for both partitions)
```

Method 2 — Python parser (§2.2 Method B): `files_not_in_index=[]`,
`rows_without_file=[]`, `duplicate_rows=[]` for both partitions.

Section-header annotations vs live counts:

```
$ grep -n "^## " corpus/README.md
16:## linguistics/ (16)
35:## myth-symbol/ (16)
54:## culture-material/ (16)
73:## synthesis/ (24)
100:## verification/ (13)
116:## civilizations/ (94)
213:## Known gaps (frontier)
```

Header annotations 16 and 13 match live counts; every other section also
matches. `corpus/README.md:273` total line "Total knowledge entries: 179."
matches grand total 179. Index surface audited: `corpus/README.md` working-tree
bytes sha256 `e998910e898c6d96bfb60688108df5ddc768cde2dd3349089ed8511c3452c0c2`
at 21:28:39Z–21:30Z (the file was concurrently edited in its civilizations
section at 21:28:39Z — see §6; the linguistics/verification sections and the
count lines were byte-stable across the whole T0 window under both parsers).
SKILL.md does not enumerate partition files (`grep -n "linguistics/\|verification/"
SKILL.md` returns only directory-level mentions at :129 and :140 in the
committed/T0 copy — the drift-fixed working-tree copy shifts these to :131
and :142, still directory-level only), so no second file-level index exists
to diff for these partitions.

### 2.4 Frontmatter field-presence sweep (29 files)

```
$ for f in corpus/knowledge/linguistics/*.md corpus/knowledge/verification/*.md; do
    for field in topic sources verified-at recheck couples; do
      grep -q "^- $field:" "$f" || echo "MISSING:$field $f"; done; done
(empty)
```

All 16 linguistics + 13 verification entries carry all five fields. This does
not re-check the round-8 `source`/`verified-at`/`recheck` fleet-header
conformance question (a known gap for older historical entries, not these
partitions' current profile).

### 2.5 Stray-file and change-detector sweeps

```
$ find corpus/knowledge/linguistics corpus/knowledge/verification -mindepth 1 ! -name '*.md' -print
(empty)
$ git status --porcelain -- corpus/knowledge
(empty)
$ for p in linguistics verification; do
    printf "%s list: " "$p"; find corpus/knowledge/$p -maxdepth 1 -name '*.md' -type f -printf '%f\n' | sort | sha256sum
    printf "%s content: " "$p"; find corpus/knowledge/$p -maxdepth 1 -name '*.md' -type f -print0 | sort -z | xargs -0 sha256sum | sha256sum
  done
linguistics list: c5aab6a6039c023cdb0a328350ed82f0602fc7cd3b858fb71cef193969fe1509  -
linguistics content: 0f2b33b85a15aee3374bef5f53d33c40d644c7f68fbae5f56894cd1165e83995  -
verification list: 948bfc8324b04c2e0ebdcf99f5ed2c571e14398c776e9d19744b184aea61faff  -
verification content: cd98e74e48bdf4341a7f1efe427d94271dfeba41492c24d161e0802650311013  -
```

The content digests cover in-place edits as well as additions/removals: any
landed entry, edit, or index-relevant change in either partition moves at least
one digest or the `git status` line. Per-file sha256 for all 29 entries at T0
is appended in §7.

## 3. What this audit rules out at T0

- an entry added to or removed from linguistics or verification (counts and
  list digests move);
- an entry edited in place in either partition (content digests move);
- an index row added, dropped, renamed, or duplicated without a matching file,
  and a file without a row (two parsers, both directions, §2.3);
- a section-header or footer count claim that disagrees with live bytes
  (`corpus/README.md:16,100,273,277`);
- a stray non-`.md` file in either partition directory (§2.5);
- a missing frontmatter field among the 29 existing entries (§2.4).

## 4. What this audit does not cover

1. New-entry quality (provenance, calibration, coupling, no-filler,
   no-duplication) — R10-C11..C20 reviewer scope; this seat only counts.
2. Index-row prose correctness for entries that land after T0 — R10-C21/C22
   scope; §5 records whether rows matched at T1, nothing more.
3. `source`/`verified-at`/`recheck` fleet-header conformance of older
   historical entries (the README known-gaps item at `corpus/README.md:244-246`)
   — out of this seat's partition scope and left as filed.
4. The round-5/round-9 `validation.json` working-tree churn observed during
   the T0 window (§6) — reported to the parent, dispositioned by F/O seats.

## 5. T1 post-landing re-check

All ten C-claim entries landed (3 linguistics, 3 myth-symbol, 2
culture-material, 2 verification — the declared 3/3/2/2 split; earliest
`verification/header-conformance-readings.md` mtime 21:31:46Z, latest
`linguistics/language-shift-obsolescence-revival.md` 21:38:48Z per
`stat`, corroborated by the poll log), and the R10-C21/C22 index updaters
rewrote `corpus/README.md` at 21:39:51Z. This seat's partitions at T1:

New entries (+3 linguistics, +2 verification; the full `git status
--porcelain -- corpus/knowledge` untracked set is 10 rows, one per author):

- `corpus/knowledge/linguistics/language-shift-obsolescence-revival.md` — sha256 `89d2a225dd709a7947c4f9d967ffd6ce858f784bfef10f581b11a863dc6c8315`
- `corpus/knowledge/linguistics/numerals-and-measures.md` — sha256 `57fc76695c9fed38cf87ddccbaf7e5c5d322125f65b98aea154baf5046129340`
- `corpus/knowledge/linguistics/sound-symbolism.md` — sha256 `4f14b05a7df542ad5e3dca39c20cb02dc3f5745c70395418770da93794fddd5d`
- `corpus/knowledge/verification/header-conformance-readings.md` — sha256 `d627eba3b99f56933b6eae2ab1339013be57da30a5e5608b4d75ddb7f36feb90`
- `corpus/knowledge/verification/verification-independence-anti-circularity.md` — sha256 `743bce544c888a9159728af4b6f5dcecb98166adc3a77d30e7794b5d711d0cff`

Counts and index-vs-files diff (T1, 21:41:20Z–21:47:45Z, four measurements):

```
$ for p in linguistics verification; do printf "%-14s %s\n" "$p" "$(find corpus/knowledge/$p -maxdepth 1 -type f -name '*.md' | wc -l)"; done
linguistics    19
verification   15
$ python3 .scratch/audit-ling-verif.py
linguistics        actual= 19 index_rows= 19 header=19 files_not_indexed=[] rows_without_file=[]
myth-symbol        actual= 19 index_rows= 19 header=19 files_not_indexed=[] rows_without_file=[]
culture-material   actual= 18 index_rows= 18 header=18 files_not_indexed=[] rows_without_file=[]
synthesis          actual= 24 index_rows= 24 header=24 files_not_indexed=[] rows_without_file=[]
verification       actual= 15 index_rows= 15 header=15 files_not_indexed=[] rows_without_file=[]
civilizations       actual= 94 index_rows= 94 header=94 files_not_indexed=[] rows_without_file=[]
grand_total_actual=189 readme_total_line=189 matches=True
$ grep -n "^## .* (.*)" corpus/README.md
21:## linguistics/ (19)
43:## myth-symbol/ (19)
65:## culture-material/ (18)
86:## synthesis/ (24)
113:## verification/ (15)
131:## civilizations/ (94)
```

Footer total line (`corpus/README.md`, at T1): "Total knowledge entries:
189." — matching `grand_total_actual=189`. `corpus/README.md` working-tree
sha256 `9df4b7c579b89d6ff51ace4600cb0518b897d2e6d0819150e3fde6bbf5b8333c`
at 21:39:51Z, byte-stable through 21:47:45Z. The index updaters' §1 landing
table (`reports/round-10/coverage/index-update.md`) matches this seat's
independent count exactly (16→19, 16→19, 16→18, 13→15; synthesis 24,
civilizations 94 unchanged).

Independent re-check of the updaters' "two stale rows repaired" claim
(`index-update.md` §2/§4): both repaired rows now equal their entries'
joined `- topic:` head text exactly — `phonetics-phonology.md`
(`corpus/README.md:34`; the pre-round-10 row truncated at "— IPA") and
`africa-primary-sources.md` (`corpus/README.md:134`; paraphrase replaced).
Command (topic-extraction join vs row regex, the index-update.md §2
convention): 7/7 spot-checked rows matched — the 2 repaired rows plus all 5
new entries in this seat's partitions.

Digests (identical at 21:41:20Z and 21:47:45Z — no edit, addition, or
removal between the four T1 measurements):

```
linguistics list: d806bcc391baa80e9b8a818adb8897a96ca21358d4460af37378261ff25e7838  -
linguistics content: 46650a0f1bf58e650a3eeac1cc3316cb3110ce526b11e725031515cf9cd4e967  -
verification list: 84239de344f306b541724061a7508a0041045dc1bcd159355e541c6e8cbf7f9c  -
verification content: d2f7207006648ec21b28dee55131abb435ac13f790a39078b2a9ed07e2f40f23  -
```

T1 field-presence spot check on the five new entries: all carry `topic`,
`sources`, `verified-at`, `recheck`, `couples` and at least one headed
decision-record section (count-level fact only; the R10-C11..C20 reviewer
fragments own the quality verdicts, and all ten review files are present in
this directory).

Reconciliation: 179 + 10 = 189. `HEAD` unchanged (`e3a1ec9…`); no commit
was made by this seat or observed in the window. No further changes to
either partition were observed after 21:38:48Z (mtime sweep), so T1 is the
settled state at this seat's window close (21:47:45Z).

## 6. Out-of-scope observations (reported, not absorbed)

1. **`reports/round-9/validation.json` is modified in the working tree**
   (mtime 21:26:58Z; `git diff` removes 14 lines / adds 4: two `stdout_sha256`
   values changed and the `git_status`/`untracked_additions` blocks listing
   `?? tools/gates/expected/`, `?? tools/gates/frozen/handoff-packet-check/`,
   `?? tools/gates/frozen/lexicon-coverage-audit/`,
   `?? tools/gates/frozen/provenance-audit/` were dropped). `reports/round-9/run-validation.py:7`
   states the script "Writes ONLY reports/round-9/validation.json", and
   `reports/round-5/run-validation.py:194` likewise rewrites its own receipt —
   so any re-run of these historical acceptance runners mutates filed receipt
   bytes, which the round-10 targets forbid for fixers ("never rewrite filed
   report bytes — corrections are new entries"). `reports/round-5/validation.json`
   was modified at 21:27:32Z (361 lines diffed) and its mtime changed again at
   21:29:29Z, after which it matched HEAD again (restored or byte-identical
   rewrite). Both are outside this seat's partitions; recorded for the parent
   and the F/O seats.
2. **`corpus/README.md` was edited at 21:28:39Z** in the civilizations section
   (`africa-primary-sources.md` row description rewritten); linguistics and
   verification sections unchanged. Concurrent index edits are expected this
   round (R10-C21/C22) — noted so the T0 README digest in §2.3 is timestamped,
   not treated as stable.
3. **Sibling fragments observed landing during the window** (not consumed as
   evidence): `reports/round-10/coverage/review-C01..C10.md` (all ten present
   by window close), `reports/round-10/coverage/audit-unchanged.md` (R10-C25),
   `reports/round-10/drift/shard-07.md`, `reports/round-10/findings-tracker.json`.
4. **`reports/round-8/run-validation.py` is modified in the working tree**
   (T1-window observation, 21:47Z: 62 lines changed, `git diff --stat`).
   The diff rewires the frozen-replay pin resolution to search git history
   (`gate_blob_for_pin`, "Round 10 repair: the pinned revisions are resolved
   by matching each manifest gate_sha256 against git history — assuming HEAD
   still carried them read 0 of 7 rows reproduced after the round-8 admission
   commit revised the gates"). This is a live edit to a *historical* acceptance
   script, and `corpus/README.md`'s known-gaps paragraph states the lane's
   discipline for exactly this class: "do not edit old scripts or rewrite
   historical receipts to accommodate new paths" (pre-round-10 README lines
   266-269, carried into the current revision). Whether this repair was
   authorised under the round-10 F target ("fix it in place (cite evidence)")
   or violates that discipline is the parent's adjudication, not this seat's;
   recorded with the diff evidence, not absorbed.
5. **Final working-tree state of the receipts** (21:47Z, for the F/O seats):
   `M reports/round-9/validation.json` remains modified (same diff as item 1);
   `reports/round-5/validation.json` is no longer modified (restored to HEAD
   or byte-identical rewrite after its 21:29:29Z mtime); `M SKILL.md` (48
   lines) and `M corpus/README.md` are present as expected for drift fixers
   and index updaters. `HEAD` is unchanged (`e3a1ec9…`); no commit by any
   seat was observed in the window.

## 7. Appendix — per-file sha256 at T0 (21:27:00Z)

```
7ee9f7e45d8a63ac4362a95d71db923dde118d4a1f0a598fa0a0888e68105992  corpus/knowledge/linguistics/color-terminology.md
272329f70c1fe93e47f47d8c2618371902d1e5ccc78b6987abf437e101ac77ea  corpus/knowledge/linguistics/conlang-methodology.md
019f28f09ceac28a1bcb6685f756170b66944129a6b3dca17ca76d9663ab3caf  corpus/knowledge/linguistics/historical-linguistics.md
c51d3483a27b0943b257fa25287d0dec4dba3fe16f737b1893ce237ba92c07f8  corpus/knowledge/linguistics/kinship-terminology.md
52385e3d81f7d8f8eb1423d408a47bd12c968f1444fd9fc5d77a9c3e691cd409  corpus/knowledge/linguistics/language-contact.md
ffa38d0f2e89a774f373c9759978e8bd173e6e28b1f5cc1b1c87847fd5e54458  corpus/knowledge/linguistics/linguistic-anthropology.md
b423e811651aca4229e6621dd2a884df360a53809230778aa85bef6376dfeddb  corpus/knowledge/linguistics/morphological-typology.md
d972a1d65e7a8fba34f44e1cd57019c175a8ed24671ef95f3e0ea3d1ed9ffb3d  corpus/knowledge/linguistics/naming-systems.md
f827bbee6f305466a17a8b6e911539c38820e6865eb7755881e779ad143a6a95  corpus/knowledge/linguistics/orality-formulaic-language.md
b4f9b00384bc6840bdd1d7d7e7ae9bbb127a2fd1f5010c98d5b253df65d7776b  corpus/knowledge/linguistics/phonetics-phonology.md
a73c0b1fb8fd0052a46252e6262101220ca145e3c9a7f8b44c2151e45fc047e4  corpus/knowledge/linguistics/politeness-taboo-euphemism.md
80b5e2c89fc8a97be343d32be4071ec40cc2a0e2aedac4a8abf2311b7175f65d  corpus/knowledge/linguistics/semantic-fields-lexicon-building.md
9b9a3ff757fe3290a1435a75d08b96705645f68cdc9c200d27ed26cb8af6ae9b  corpus/knowledge/linguistics/semantics-pragmatics.md
95ea235f9e10e2efc6f1f917008fa3ac3cfc2e8cd5e21258a4615cd5e90abebd  corpus/knowledge/linguistics/sociolinguistics-registers.md
258accfd4e435628190c537e68ca84ab57f40e9b53aed0675bf98d92d7bbd090  corpus/knowledge/linguistics/syntax-typology.md
76263260dd8181bae0d969c2d4cd647892535a692eb0e41033d83ea8f005a98b  corpus/knowledge/linguistics/writing-systems.md
cf7cceee9008a9db768d074671f490e4e99feb59ed4e10fb21fa0b72a4e0454c  corpus/knowledge/verification/calibration-registry.md
6e27001de26ef30255b6dcd9ecdd3c91ca1095aebb8882f1b084abbd04c9d040  corpus/knowledge/verification/citation-format-and-source-registry.md
455ad8701a703031ca63e1d118a1af396f06aebf65c762ae9d53490d2cd7a80b  corpus/knowledge/verification/costume-era-consistency-gate.md
7eb2635bc72fb9a6ba19f0a565c15d7d03c0d6aaf62df46cc1413354b5626bb6  corpus/knowledge/verification/gate-frozen-run-standard.md
c3118517a8510e94b083ee061d0d18f867b479f3c60317cf1ccf7b4f6f2f3def  corpus/knowledge/verification/internal-consistency-audit.md
cbf4f7a0931270c49fdcf5d665bd2cc0823cb26e6278f4c5bf5e575a5f38f9b8  corpus/knowledge/verification/lexicon-coverage-audit.md
4523b7a2747973beeab00eb97b113e12a8cbfbba6a169ea7d56b3d037c995daf  corpus/knowledge/verification/myth-consistency-gate.md
ddaaee83a9ef8f16d179f49e24bb9b722617e32495b1def325ddc384b5f768e9  corpus/knowledge/verification/naming-collision-gate.md
de38547456a2b7e1fd774669da29c39957f1fe7df2d75a8d47b3d77ebd44e333  corpus/knowledge/verification/phonology-sanity-gate.md
dfa66d2af81b2789ad58b710cc577278f331a6cbda6d6c648d8bbf25613501f4  corpus/knowledge/verification/provenance-audit-ledger-format.md
dc66ed87559e533d026dd2e9a3efb1b999d39bd4e2f5f7e575f751a275e5858f  corpus/knowledge/verification/real-world-inspiration-boundaries.md
073a348b38c5d8b27cef8f109afed06ff592da00f2eb91252657ab857e32fb13  corpus/knowledge/verification/to-verify-triage-protocol.md
f52708d91f5829b44bbf081341d7073ba05e757764ce164ff21563c2f903f0c9  corpus/knowledge/verification/verification-method-overview.md
```
