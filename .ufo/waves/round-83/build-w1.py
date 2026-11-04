#!/usr/bin/env python3
"""Build the kotodama round-83 v1 wave spec (one wave, 14 seats). Prints the spec JSON."""
import json

LANE = "/home/vgpnk/Projects/shokunin/kotodama-shokunin"
FLEET = "/home/vgpnk/Projects/shokunin"
BASE = "3088bd7fe2a55a123214abba7008dcddf12b301c"
FREEZE = "21277b089e3c64c247bb4e0fcb033abfdfa1e668"
WAVE = LANE + "/.ufo/waves/round-83/w1"
ENTRY = "corpus/knowledge/myth-symbol/marriage-alliance-bridewealth.md"
TOOL_O = "tools/check-gate-registry.py"
TOOL_C = "tools/check-cited-records.py"
GODSPEED = """/skill:godspeed

You are a Godspeed-enabled subagent.

1. **Name the axes.**
2. **Iterate cheap, in parallel.**
3. **Keep moves that improve any axis and harm none.**
4. **Don't aim \u2014 let the frontier walk itself.**

"""

CONTEXT = f"""# Goal
Kotodama round 83 (hyaku run 15), ONE v1 wave of 14 seats: build and falsify the round's three claims together.
Lane repo {LANE} (jj-colocated; git is the backend). Fleet root {FLEET}.
Lane base revision {BASE}; frozen claims/counters commit {FREEZE}. Read any base byte with
`git -C {LANE} show {BASE}:<path>` and any frozen byte with `git -C {LANE} show {FREEZE}:<path>`.

# Claims (frozen before any data; do not renegotiate a target)
- **O (operability, capability acquisition).** `{TOOL_O}` lands and the 14 missing rows enter SKILL.md
  `## Gates and probes`: every committed `reports/round-*/accept-*.py` counter has a registry row, derived
  and checked from committed bytes. After-state: one `GATE-REGISTRY: 0 missing / <r> registered / <i>
  instruments / 0 dead` line, exit 0, i >= 61.
- **D (depth).** `{ENTRY}` lands as the 257th knowledge file: marriage as an alliance-and-transfer
  institution, with rows S909\u2013S912 opened this round.
- **C (calibration).** QUALITY criterion 31 lands, `{TOOL_C}` lands, and the round-82 routed record
  defects are repaired (the 0-byte `reports/round-82/counter-revisions.md`, the R82-M2 line erratum,
  S908's shape via a superseding row).

# Bounds (binding)
- Write ONLY the files your assignment names. Everything else in the lane, the fleet repo, sibling lanes,
  `.ufo/state/`, `MANIFEST.json` and `/home/vgpnk/Projects/shokunin/.scratch/` is read-only. Never edit
  `corpus/SOURCES.md` unless your assignment says so; never edit `considerthese/` (absent here) or another
  lane's rows.
- NEVER commit, push, or run a mutating git/jj command. The L1 lands every byte. Read-only git is fine.
- Use ABSOLUTE paths in every command and every `write`. Seat tools start at the fleet root: a relative
  path lands in the FLEET repo. Every `Report:` trailer path is relative to {LANE} \u2014 write it at
  {LANE}/<that path>.
- Git fixtures (only where an assignment asks for one): `D=$(mktemp -d) && git -C "$D" init -q`, every later
  git call names `-C "$D"` explicitly, and verify `git -C "$D" rev-parse --show-toplevel` equals `$D` before
  the first commit. Never commit with a throwaway identity anywhere else.
- Scratch: your dir is `/fast/scratch/hyaku/kotodama-r83/<YourSeatName>` (create it, `trap 'rm -rf -- "$S"' EXIT`,
  copy receipts into {WAVE}/ before exiting, and report if anything is left behind). `/tmp` is for files under
  50 MB only and a `/tmp` path is never citable evidence. Do not hardcode `/tmp` in anything committed.
- **No absolute scratch path may appear in any committed report/receipt you write this round**: cite
  repo-relative paths only (QUALITY criterion 31 binds from round 83; `{TOOL_C}` grades it).
- Tooling: you may install/upgrade tools that help the task (read `/home/vgpnk/.omp/agent/RULES.md` first:
  official channels, update-safety gate, record tool/version/channel/reason). **All pacman transactions are
  PAUSED host-wide** \u2014 use `uv tool`/`npx`/an official binary in `~/.local/bin`, never `pacman -S/-Sy/-Syu/-U/-R`.
- Sources: open them by ordinary means only \u2014 plain HTTP requests, public-domain editions, no browser
  challenge/captcha/login/paywall. Automation: none beyond plain fetches.
- Never message `agent://all`. Write your findings and files; the L1 integrates.
- Round-82 lesson R82-M3 binds: when two seats read the same source, say which reading is authoritative.
  This wave's rule: **`ScribeRows`' fetch receipts bind the registry rows; `ScoutSources`' reading is the
  independent second reading** \u2014 if they disagree on a byte count or a quote, report it, do not silently pick.

# Lane conventions you must obey
- `corpus/SOURCES.md` rows are exactly 11 cells, `| id | source | kind | tier | scope | anchor | teaches |
  status | opened | recheck | used-by |`, no literal or escaped `|` inside any cell, `opened` an ISO date,
  `status` one of queued/mined/rejected, append-only (only status/recheck/used-by change in place).
- Knowledge entries open with the header block (`- topic:`, `- gap filled:`, `- sources:`, `- couples:`,
  `- source:`, `- verified-at:`, `- recheck:`, `- scope:`) and carry `## 1. \u2026` \u2026 `## 6. \u2026`.
- A QUALITY criterion is numbered, states scope, a check (red-before), and its limits, and is grounded in a
  measured case.
"""

ITEMS = []


def it(name, role, axes, text):
    ITEMS.append({"name": name, "role": role, "axes": axes, "milestone": "r83-v1", "prompt": GODSPEED + text})


# ---------------------------------------------------------------- recon
it("ScoutGap", "scout", ["depth", "coverage"],
   f"RECON \u2014 claim-D absence census and partial-owner map. READ-ONLY; write only under {WAVE}/stage/ScoutGap/.\n"
   f"1) Prove or refute the before-state at `{BASE}`: filename sweep over `corpus/knowledge/**/*.md` for "
   "`marriage|bride|dowry|wedding|spouse|betroth` (expect 0 owning basenames), the institutional core "
   "`bridewealth|bride-price|bride price|dowry|betroth` (expect 9 files / 27 lines, all passing attributes), and "
   "`- gap filled:` claims naming the surface (expect 0). Use `git -C " + LANE + " ls-tree -r --name-only " + BASE + " corpus/knowledge`.\n"
   "2) Duplicate-document check by DOCUMENT, not URL: search the registry at base for Hammurabi,"
   " the EB11 'Marriage' article, the Rigveda (any RV 10.85 row), Leviticus, and for S904/S905 (already registered:\n"
   "   Homer Odyssey #1727, Tacitus Germania). Name for each candidate whether a row already registers the WORK.\n"
   "3) Partial-owner map: for at least these ten files quote the owning line and classify owns/mentions/hands-off:\n"
   "   linguistics/kinship-terminology.md, culture-material/sumptuary-law-rank-display.md, culture-material/ritual-garments.md,\n"
   "   culture-material/trade-economy-lexicon.md, culture-material/funerary-material-culture.md, linguistics/naming-systems.md,\n"
   "   myth-symbol/guest-right-hospitality-law.md, myth-symbol/purity-pollution-boundary-systems.md,\n"
   "   myth-symbol/binding-speech-complex.md, synthesis/contact-scenario-builder.md.\n"
   "4) Name the one-way couplings the entry must declare and any surface a sibling lane could claim (report, never absorb).\n"
   "Write {WAVE}/stage/ScoutGap/gap-census.md and {WAVE}/stage/ScoutGap/owners.md with commands and raw output.")

it("ScoutSources", "scout", ["depth", "freshness"],
   f"RECON \u2014 open the four claim-D candidate sources by ordinary means and produce the independent second reading.\n"
   f"Write only under {WAVE}/stage/ScoutSources/.\n"
   "Candidates, in the id order the rows will take:\n"
   "  S909 = the Code of Hammurabi (L. W. King translation, Yale Avalon Project,\n"
   "         https://avalon.law.yale.edu/ancient/hamframe.asp and its law pages).\n"
   "  S910 = 'Marriage', Encyclopaedia Britannica 11th edn, vol. 17 (Wikisource transcription,\n"
   "         https://en.wikisource.org/wiki/1911_Encyclop%C3%A6dia_Britannica/Marriage).\n"
   "  S911 = the Rigveda, RV 10.85 (the marriage hymn), public-domain translation \u2014 use\n"
   "         https://en.wikisource.org/wiki/The_Rig_Veda/Mandala_10/Hymn_85 (Griffith) or sacred-texts' Griffith page.\n"
   "  S912 = Leviticus 18 (KJV, Project Gutenberg #10 or #7999 \u2014 name the exact URL and byte count you used).\n"
   "For each: HTTP status, decoded bytes, sha256, access date (2026-11-04), user-agent used, and the located span you\n"
   "  propose with its word count (<= 25 words) plus a `raw <n> / folded <m>` count of the span (tags->separator,\n"
   "  U+00A0/U+2003->space; QUALITY 30). Where a page is template-rendered, also probe the same-page Wayback capture\n"
   "  and record its status, decoded bytes, paragraph count. Refuse (with reason and flip) any candidate whose prose\n"
   "  is a bare glossary stub for this scope. Name the tier each survives: A = primary/authoritative for the scope\n"
   "  (a legal code's own text, a scripture's own text), B = strong secondary (a 1911 overview), C = lead only.\n"
   "  Flag framework status explicitly: EB11's evolutionary stage-law vocabulary is calibration material, never\n"
   "  load-bearing doctrine.\n"
   "Report the cheapest usable quote per source, and for each a second passage a different entry section can cite.\n"
   "Write {WAVE}/stage/ScoutSources/sources.md plus one receipt per id (S909.txt..S912.txt) with raw counts and the\n"
   "  command that produced them. Do NOT write into corpus/.")

# ---------------------------------------------------------------- build
it("ExecRegistryCensus", "executor", ["operability", "calibration"],
   f"BUILD \u2014 the machine-readable registry census that the rows seat and the L1 both check against.\n"
   f"Write {LANE}/.ufo/waves/round-83/w1/stage/ExecRegistryCensus/registry-census.json and .md only.\n"
   "1) Enumerate at `" + FREEZE + "`: every `reports/round-*/accept-*.py` (the counter class; expect 61 at that revision).\n"
   "2) Parse the `## Gates and probes` table of SKILL.md at the same revision and compute the missing set\n"
   "   (a row covers a counter iff the counter's repo-relative path is inside the row's entry-command cell).\n"
   "3) For every missing counter emit the exact row cells it needs, derived from the script itself: name\n"
   "   (`accept-<x>-<nn>`), kind (`gate`), entry command (the script's real flags \u2014 read its argparse),\n"
   "   verdict map (its declared exit codes mapped onto clean/failed/could-not-evaluate), self-test (its real\n"
   "   spelling, or `\u2014` when it has none), pinned values (its fixture/pin paths, or `\u2014`), write scope\n"
   "   (`read-only; selftest scratch` or what the script actually writes), owner (`kotodama-shokunin`).\n"
   "4) Flag any counter whose script cannot be described from its own bytes (no main, no exits) as a defect\n"
   "   rather than inventing a cell.\n"
   "Output JSON: {{\"instruments\":[...],\"rows\":N,\"missing\":[...],\"proposed\":{{id: [8 cells]}} }}. Quote file:line for every\n"
   "  verdict-map claim. Delete your scratch dir on exit.")

it("ExecGateRegistryTool", "executor", ["operability"],
   f"BUILD \u2014 `{LANE}/{TOOL_O}`, the gate-registry coverage auditor. The L1 lands it; you write the file and prove it.\n"
   "Frozen contract (a counter grades exactly this; do not improvise):\n"
   "  CLI: `--root DIR` (default `.`), `--json`, `--selftest`, `-h`; optional `--registry PATH` (default `<root>/SKILL.md`).\n"
   "  Instrument set: sorted `reports/round-*/accept-*.py` under --root (repo-relative paths).\n"
   "  Registry rows: lines under the `## Gates and probes` heading that start with `|` after 0-3 leading spaces,\n"
   "    have >= 8 pipe-separated cells, and are not the header or the `---` separator.\n"
   "  Coverage: a row covers an instrument iff the instrument path is a substring of the row's 3rd cell\n"
   "    (entry command).\n"
   "  Dead row: each path token matching `(?:tools|reports)/[A-Za-z0-9_./-]+\\.py` in the entry-command cell that\n"
   "    does not exist under --root.\n"
   "  Output: exactly one summary line `GATE-REGISTRY: <missing> missing / <registered> registered / <instruments>\n"
   "    instruments / <dead> dead`, then optional `MISSING <path>`, `DEAD <row-name> <path>`, and exactly one\n"
   "    informational `GATE-REGISTRY-INFO: <n> tools without a row` line (count of `tools/*.py` with no row; never\n"
   "    affects the exit code).\n"
   "  Exit: 0 iff missing == 0 and dead == 0; 1 otherwise; 2 with `GATE-REGISTRY-ERROR <msg>` on could-not-evaluate\n"
   "    (no registry file, no heading, a row with < 8 cells, unreadable input). No traceback ever.\n"
   "  `--json`: one JSON object {{\"instruments\":[...],\"registered\":[...],\"missing\":[...],\"dead\":[...],\"rows\":N,\n"
   "    \"tools_without_rows\":[...]}}.\n"
   "  `--selftest`: >= 12 checks over fixtures in a `tempfile.mkdtemp()` that honours TMPDIR (never `/tmp`), asserting\n"
   "    exit codes and message text: clean registry; one missing; dead token; short row; absent registry; absent\n"
   "    heading; 0-3-space-indented rows accepted; a 4-space row ignored; `--json` shape; info line; no traceback on\n"
   "    malformed input. Prints `SELFTEST: PASS (<n> checks)` and exits 0; 1 on a failed check; 2 on could-not-evaluate.\n"
   "Prove it against real bytes: run it at `" + FREEZE + "` (expect the 11 missing counters named, exit 1) and against a\n"
   "  scratch registry that adds the 14 rows (expect 0 missing / 0 dead, exit 0). Paste both runs into\n"
   "  {WAVE}/stage/ExecGateRegistryTool/proof.md, plus your `--selftest` run. `py_compile` clean; python3 stdlib only. nothing may import counterlib.")

it("ScribeRegistryRows", "scribe", ["operability"],
   f"WRITE \u2014 the 14 missing rows of `{LANE}/SKILL.md` `## Gates and probes`. You own SKILL.md for this wave;\n"
   "  edit nothing else in it and invent no other section.\n"
   "Rows to add, in the table's exact 8-cell shape `| name | kind | entry command | verdict map | self-test |\n"
   "  pinned values | write scope | owner |`:\n"
   "  accept-c-76, accept-ca-76, accept-ca-79, accept-o-79, accept-d-80, accept-o-80, accept-c-81,\n"
   "  accept-d-81, accept-o-81, accept-d-82, accept-o-82 (the standing round-76..82 gap), and accept-o-83,\n"
   "  accept-d-83, accept-c-83 (this round's counters).\n"
   "Derive every cell from the script's own bytes (`git -C " + LANE + " show " + FREEZE + ":reports/round-NN/accept-*.py`):\n"
   "  the real flags in the entry command, the real exit codes in the verdict map, the real `--selftest` spelling\n"
   "  (or `\u2014`), and its pinned fixture paths. Do not copy a sibling row's text. `owner` is `kotodama-shokunin`.\n"
   "Place them after the existing `accept-ca-75` row and before the `accept-c-73 / accept-ca-73 correction` note row,\n"
   "  keeping the table contiguous. Every entry-command cell must contain the script's repo-relative path verbatim\n"
   "  (a counter checks that substring). Never touch the earlier rows' cells.\n"
   "Verify with `python3 -c` that every added line has exactly 8 cells and that no cell contains a literal pipe.\n"
   "Write your receipts to {WAVE}/stage/ScribeRegistryRows/rows.md (one row per line, plus the cells you rejected and why).")

it("ExecCitedRecords", "executor", ["calibration"],
   f"BUILD \u2014 `{LANE}/{TOOL_C}`, the cited-record checker for QUALITY criterion 31. The L1 lands it; you write the file and prove it.\n"
   "Frozen contract (a counter grades exactly this):\n"
   "  CLI: `--root DIR` (default `.`), `--from-round N` (default 83), `--bind-round N` (default 83), `--json`, `--selftest`.\n"
   f"  Documents for round k: `<root>/reports/round-<k>/**/*.md` for k >= --from-round; `<root>/corpus/lessons/round-<k>*.md`\n"
   "    for k >= --from-round.\n"
   "  EMPTY leg: every backticked token matching `(reports|corpus|tools|\\.ufo)/[A-Za-z0-9_./-]+\\.(md|txt|json|py|tsv|yml)`\n"
   "    cited in those documents that resolves under --root to a regular file of size 0 -> one `EMPTY <path> <doc>` line.\n"
   "    A token that does not resolve is NOT a finding (path lists are not citations).\n"
   "  SCRATCH leg: for k >= --bind-round, any absolute path matching `^/(tmp|var/tmp|fast/scratch)/` -> one\n"
   "    `SCRATCH <path> <doc>` line.\n"
   "  Output: exactly one `CITED-RECORDS: <empty> empty / <scratch> scratch` line; exit 0 iff both are 0; 1 otherwise;\n"
   "    2 with `CITED-RECORDS-ERROR <msg>` on could-not-evaluate. No traceback ever. `--json`:\n"
   "    {\"empty\":[...],\"scratch\":[...],\"documents\":N}.\n"
   "  `--selftest`: >= 10 checks over fixtures in a TMPDIR-honouring temp dir: clean tree green first, then an\n"
   "    empty cited record caught, a nonempty cited record accepted, a scratch path inside the bind window caught,\n"
   "    the same scratch path in an older round ignored, an unresolved token ignored, a 0-byte file that is not\n"
   "    cited not counted, `--json` shape, absent root exit 2, no traceback. Prints `SELFTEST: PASS (<n> checks)`.\n"
   "Prove it on real bytes: at `" + FREEZE + "` with `--bind-round 82 --from-round 82` it must catch round 82's\n"
   "  `reports/round-82/counter-revisions.md` (0 bytes, cited by `corpus/lessons/round-82.md`) and the two\n"
   "  `/fast/scratch/` receipts; at the default binding on the same tree it must report 0/0 over round-83 documents\n"
   "  (none exist yet: say so). Paste both runs into {WAVE}/stage/ExecCitedRecords/proof.md. stdlib only, py_compile clean. nothing may import counterlib.")

it("ScribeEntry", "scribe", ["depth"],
   f"WRITE \u2014 `{LANE}/{ENTRY}` (the round's depth claim). You own exactly that path.\n"
   "Shape (a counter grades the first three items mechanically, so use these exact strings):\n"
   "  - >= 12000 bytes; header block before `## 1.` carrying `- topic:`, `- gap filled:`, `- sources:`, `- couples:`,\n"
   "    `- source:`, `- verified-at:`, `- recheck:`, `- scope:` (lane convention; see\n"
   f"    `git -C {LANE} show {BASE}:corpus/knowledge/myth-symbol/guest-right-hospitality-law.md` for the shape and tone).\n"
   "  - >= 7 `## ` sections including EXACTLY `## 2. Six design decisions` (>= 6 table rows) and EXACTLY\n"
   "    `## 3. Attested anchors`.\n"
   "  - `## 3` carries >= 20 `- ` bullets, EACH with exactly one distinct S-id on the line (one source per anchor line;\n"
   "    never two ids on a line; no S-id inside any table row). Ids available: S909 (Hammurabi), S910 (EB11\n"
   "    'Marriage'), S911 (Rigveda 10.85), S912 (Leviticus 18), plus already-registered S904 (Homer Odyssey) and\n"
   "    S905 (Tacitus Germania ch. 18-19 on marriage and dowry) where the passage is apt. Cite >= 3 of the four new rows.\n"
   "  - Content: marriage as an alliance-and-transfer institution, not romance. Six decisions (the payment direction:\n"
   "    bridewealth vs dowry vs bride-service vs gift-exchange; prohibited degrees and exogamy/endogamy; the rite\n"
   "    sequence and who performs it; name and dress change; the dissolution and return rules; who guarantees the\n"
   "    union and what happens to the children). A `## 2.1 Lexicon interface` deriving the term set the institution\n"
   "    forces (payment, counter-payment, sponsor, prohibited kin, dissolution, return) with one worked NON-CANON\n"
   "    derivation. `## 4` craft checklist, `## 5` NON-CANON worked example, `## 6` lore handoff (canon belongs to\n"
   "    lore-shokunin). `## 1` partial owners with quoted lines \u2014 read {WAVE}/stage/ScoutGap/owners.md if it exists,\n"
   "    otherwise derive them yourself from base bytes.\n"
   "  - Calibration: EB11's evolutionary stage-law vocabulary (promiscuity/group-marriage stages) is framework\n"
   "    status \u2014 named as such, never load-bearing. Every factual sentence traces to an anchor row's located passage;\n"
   "    anything else is labelled craft, method or `(to-verify)`.\n"
   "  - Quotes: use the located passages from {WAVE}/stage/ScoutSources/sources.md and the binding receipts at\n"
   "    {WAVE}/stage/ScribeRows/ (the rows seat's reading binds; if the two disagree, use the rows seat's and say so\n"
   "    in your result). Do not invent a quote; a paraphrase belongs in your own words, not in guillemets.\n"
   "Run `python3 -B " + LANE + "/tools/check-cited-lines.py <your entry>` and paste the verdict into\n"
   "  {WAVE}/stage/ScribeEntry/lint.txt; it must print `CITED-LINES: 0 finding(s) in 1 file(s)`.")

it("ScribeRows", "scribe", ["depth", "freshness"],
   f"WRITE \u2014 the four new rows of `{LANE}/corpus/SOURCES.md` (S909, S910, S911, S912) and, if the entry cites\n"
   "  them, the `used-by` cell of S904 and S905. You own corpus/SOURCES.md for this wave; append-only: never\n"
   "  change any other cell of an existing row.\n"
   "1) Open all four sources yourself by ordinary means (plain HTTP, public domain) and record receipts under\n"
   "   {WAVE}/stage/ScribeRows/: S909.txt..S912.txt with URL, access date 2026-11-04, user-agent, HTTP status,\n"
   "   decoded bytes, sha256, the located span and its `raw <n> / folded <m>` counts. These receipts BIND.\n"
   "   Suggested pages: Code of Hammurabi (King, Avalon Project); EB11 'Marriage' vol. 17 (Wikisource);\n"
   "   Rigveda 10.85 (Wikisource Griffith or sacred-texts); Leviticus 18 (KJV, name the exact URL).\n"
   "2) Write four rows of exactly 11 cells in the registry's existing shape, `opened` = 2026-11-04, `status` = mined,\n"
   "   `recheck` = 365d for the fixed-text editions and on-release for any live wiki page, `used-by` = the entry path\n"
   "   `{ENTRY}` (write the repo-relative path, matching every other row's style). No literal or escaped pipe inside a\n"
   "   cell: if an anchor needs one, rewrite the locator in your own words. `tier`: A for a code/scripture's own text,\n"
   "   B for the 1911 overview; `anchor` carries `quote located: \u300c...\u300d (<n> words)` with <= 25 words.\n"
   "   `teaches` says what the source carries for the entry's scope (one clause, no framework claims).\n"
   "3) Update S904/S905 `used-by` old->new only if the entry cites them (append the entry path; keep the existing\n"
   "   entries), and log every such change old->new in your stage report.\n"
   "4) Verify: every row has exactly 11 cells; run\n"
   "   `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama`\n"
   "   and paste its exit code and tail into {WAVE}/stage/ScribeRows/census.md. Exit 0 required.\n"
   "5) Also draft (do NOT insert) the superseding S908 row as `{WAVE}/stage/ScribeRows/S913.row`: teaches starts\n"
   "   `supersedes S908 \u2014 ` and carries `REJECTED:` (contract spelling) with the reason, anchor names `chapter III`\n"
   "   (Frazer's stage law) and no quote; `used-by` `\u2014`. The L1 appends it under claim C.")

it("ScribeRecord", "scribe", ["calibration"],
   f"WRITE \u2014 the three record repairs of claim C. You own exactly these files:\n"
   f"  (a) `{LANE}/reports/round-82/counter-revisions.md` (currently 0 bytes while three documents cite it);\n"
   f"  (b) `{LANE}/reports/round-83/annotations/errata-r82.md` (new);\n"
   f"  (c) `{LANE}/corpus/QUALITY.md` \u2014 append criterion 31 after criterion 30, touching no earlier line.\n"
   "For (a): reconstruct the record from committed bytes only \u2014 read\n"
   f"  `git -C {LANE} show {BASE}:reports/round-82/telemetry/counter-r1-redbefore.txt`,\n"
   f"  `...:counter-r2-caught.txt`, `...:lands-o82-graded-r3.txt`, `...:selftest-o82-r3.txt`, and\n"
   f"  `git -C {LANE} show {BASE}:corpus/lessons/round-82.md` `## Mistakes` R82-M6. The file must be > 400 bytes,\n"
   "  name both revision hashes `696835ee5a8f8361031262f02d88299ea775ff1a` and `ea667212554f7062650ee6942d559bdd35736c05`,\n"
   "  say what each revision changed, cite the receipts repo-relative, and open with a line saying the bytes were\n"
   "  restored in round 83 from those committed receipts (the round-82 report's citation was honest; the file was\n"
   "  never written). Do not invent a receipt that does not exist.\n"
   "For (b): a short erratum naming R82-M2, the filed `RECHECK-ERROR line 7` vs the committed `line 5` in\n"
   "  `reports/round-82/telemetry/` and the round-82 lesson, and stating the filed bytes stand as history.\n"
   "For (c): criterion 31, one numbered entry in the file's existing style (scope, check with red-before, limits,\n"
   "  grounding). It must contain the words `nonempty`, `resolve` and `access date` (a counter greps for them) and\n"
   "  bind from round 83 with three clauses: (i) a record a round's report/lesson/scorecard cites as its evidence is\n"
   "  nonempty at the revision the report cites; (ii) from round 83 a committed receipt cites only repo-relative\n"
   "  paths that resolve at the cited revision \u2014 no `/tmp`, `/var/tmp` or `/fast/scratch` roots; (iii) a round\n"
   "  lesson's `## Gate` names, for every row the round opens, the URL and the access date. Ground it in the\n"
   "  round-82 routed defects and the measured red-before: `reports/round-82/counter-revisions.md` 0 bytes at\n"
   f"  {BASE}, and the two `/fast/scratch/` citations in round 82's receipts. State limits (the checker grades the\n"
   "  record, not the judgment; path lists are not citations; no earlier round is retro-fitted).\n"
   "Paste your red-before/green checks into {WAVE}/stage/ScribeRecord/checks.md.")

# ---------------------------------------------------------------- connector
it("ConnectorOverlap", "connector", ["adjacency", "coverage"],
   f"CROSS-AXIS OVERLAP SCAN (all three claims). READ-ONLY; write only {WAVE}/stage/ConnectorOverlap/overlap.md.\n"
   "1) For claim D: beside {WAVE}/stage/ScoutGap/owners.md if it exists, build your own table of every existing\n"
   "   knowledge file whose surface touches marriage/alliance/bride-price, classified owns/mentions/hands-off with\n"
   "   `path:line` and the quoted line. Check at minimum: linguistics/kinship-terminology.md,\n"
   "   culture-material/sumptuary-law-rank-display.md, culture-material/ritual-garments.md,\n"
   "   culture-material/trade-economy-lexicon.md, culture-material/funerary-material-culture.md,\n"
   "   linguistics/naming-systems.md, myth-symbol/guest-right-hospitality-law.md, synthesis/contact-scenario-builder.md.\n"
   "2) Name the one-way couplings the entry must declare and any sibling lane that could claim the surface (report, never absorb).\n"
   "3) For claims O and C: does any existing lane tool already read the gate registry or cited records?\n"
   "   `git -C " + LANE + " grep -ln 'Gates and probes' " + BASE + " -- tools/ reports/` and\n"
   "   `git -C " + LANE + " grep -ln 'counter-revisions' " + BASE + " -- tools/ reports/`. For each hit, say what it does\n"
   "   with the surface so the new tools neither duplicate nor contradict it. Name contradictions as defects.\n"
   "4) Check the 14 registry row names do not collide with any existing row name in SKILL.md, and say whether the\n"
   "   table's order convention (round order, notes at the end) admits them where planned.")

# ---------------------------------------------------------------- attack
it("CriticClaims", "critic", ["operability", "calibration"],
   f"FALSIFY the three frozen counters before data. READ-ONLY except {WAVE}/stage/CriticClaims/ and one scratch dir.\n"
   f"1) Read `{LANE}/reports/round-83/claims.json`, `counterlib.py`, `accept-o83.py`, `accept-d83.py`, `accept-c83.py`\n"
   "   (all at " + FREEZE + "). For each leg, name the cheapest artifact that passes it without doing the claimed work\n"
   "   (e.g. can a stub tool satisfy SELFTEST and REGISTRY? can a row be added with a wrong entry command and still\n"
   "   cover the instrument? can the D counter's SECTIONS/ANCHORS pass on a padded stub? can APPENDONLY be evaded by\n"
   "   deleting and re-adding a row with a new id? does SEPARABLE permit another claim's landing under a\n"
   "   reports/round-83/ path?). Give file:line for the code path that decides each.\n"
   "2) Build the cheapest control the frozen counters must refuse: in a scratch clone (`git clone --shared`, fixture\n"
   "   identity local to it, verify `rev-parse --show-toplevel`), commit a stub landing with the minimum bytes that\n"
   "   tries to pass claim O and claim D, then grade it with both counters. Paste the verdicts. Any PASS on the stub\n"
   "   is a vacuous claim \u2014 say so in those words.\n"
   "3) Check the do-nothing control and the refusal set: run each counter with `--lands " + BASE + "` and paste the\n"
   "   exact refusal line. Then name the ambiguities a seat could satisfy two ways (instrument glob edge, rows with\n"
   "   12 cells, an `--as-of`-like boundary) and which reading the counter enforces.\n"
   "4) Report a ranked list of the weakest legs with a one-line fix each \u2014 the L1 may re-freeze only before data.")

it("CriticDefects", "critic", ["calibration"],
   f"ATTACK the claim-C repairs and the round-82 routed-defect dispositions. READ-ONLY; write only\n"
   f"  {WAVE}/stage/CriticDefects/attack.md.\n"
   "1) Verify every claim-C before-state yourself at " + BASE + ": the r82 record's size, the three documents that\n"
   "   cite it, the absence of criterion 31, S908's teaches/anchor cells, and the two `/fast/scratch/` citations in\n"
   "   round 82's receipts. Quote bytes and line numbers.\n"
   "2) Check the erratum is honest: is the filed claim `line 7` or `line 5`, and which file actually says which?\n"
   "   `git -C " + LANE + " show " + BASE + ":corpus/lessons/round-82.md | grep -n 'line 5\\|line 7'` and the r82 report.\n"
   "3) Judge criterion 31's testability: state what it forbids precisely, name one sentence a seat could write that\n"
   "   satisfies the letter and violates the intent, and say whether the checker catches it. Name the scope\n"
   "   boundary (does it grade `reports/round-NN/**` only? what about `.ufo/waves/` receipts? say which reading the\n"
   "   frozen checker implements).\n"
   "4) Attack the S913 superseding row shape: does `supersedes S908 \u2014 ` plus `REJECTED:` plus a `chapter III`\n"
   "   anchor satisfy the census grammar and CORPUS rule 2, and does S908 remain valid as history? Name any cell\n"
   "   that would fail `sources-census.sh`.\n"
   "5) List differences between the routed defects (round-82 spot-check §6, items 1-7) and what this round is\n"
   "   landing; name any item left undispositioned.")

it("MutationTester", "mutation-tester", ["operability", "calibration"],
   f"MUTATION RUN against the round's instruments before data. Write only {WAVE}/stage/MutationTester/ and one scratch dir.\n"
   "1) Build five single-predicate mutants of the *tool contracts* (not of the counters) as standalone stub scripts in\n"
   "   a scratch clone of the lane, each committed as a stub landing so a counter grades it:\n"
   "   m1 `GATE-REGISTRY` summary printed from hardcoded zeros; m2 coverage matched on basename only (so a row\n"
   "   naming `accept-c.py` covers every round's `accept-c.py`); m3 dead-token check disabled; m4 `CITED-RECORDS`\n"
   "   EMPTY leg counting unresolved tokens as findings (over-broad); m5 SCRATCH leg ignoring `--bind-round`\n"
   "   (so round 82's history alone turns it red).\n"
   "   For each: run the frozen counters (`accept-o83.py` for m1-m3, `accept-c83.py` for m4-m5) at that stub commit\n"
   "   and report which leg caught it, pasting the leg line.\n"
   "2) Also mutate the counters themselves one line each (three mutants: REGISTRY accepts a mismatch in the\n"
   "   instruments set; ROWS accepts a row whose entry command lacks the path; APPENDONLY compares only row count)\n"
   "   and report whether any leg of the real artifacts would catch the mutation \u2014 if none exists, that is an\n"
   "   honest gap to name, not to fix.\n"
   "3) Report the mutation score (caught/5 contracts, 0/3 counters expected) and the weakest predicate.\n"
   "   Fixture repos: `D=$(mktemp -d) && git -C \"$D\" init -q`, verify toplevel, fixture identity only there.")

it("SentinelScope", "sentinel", ["adjacency", "calibration"],
   f"READ-ONLY ADVERSARIAL PROBE of scope and append-only discipline. Write only {WAVE}/stage/SentinelScope/probe.md.\n"
   "1) Enumerate at " + FREEZE + " every file this round plans to write (claims.json's own_paths per claim, plus the two\n"
   "   tools and the wave stage) and check each lies inside the lane repo and nowhere else. Name any path outside\n"
   "   {LANE}. Check the fleet repo is untouched: `git -C {FLEET} status --porcelain` and report any file one of this\n"
   "   round's seats wrote there (do not delete it; report it).\n"
   "2) Prove the registry is append-only across the planned changes: write a checker (in your scratch dir, not the\n"
   "   repo) that, given a hypothetical lands tree, would flag any existing row whose cells 0..6 moved. State exactly\n"
   "   which rows the round intends to modify in place (S904/S905 used-by) and confirm they are in the free columns.\n"
   "3) Check PROVINCE.md is byte-identical between base and freeze, and that no round-83 artifact touches\n"
   "   `MANIFEST.json`, `.ufo/state/`, `corpus/considerthese/` (absent) or a sibling repo.\n"
   "4) Look for credential material or absolute personal paths in the round's committed receipts at freeze\n"
   "   (`git -C " + LANE + " grep -nE '/home/[a-z]+/(\\.ssh|\\.config|\\.aws)' " + FREEZE + " -- reports/round-83`):\n"
   "   report findings or the clean result. nothing may import counterlib.")

SPEC = {
    "wave": "kotodama-r83-v1",
    "milestone": "Round 83 wave 1 (build + falsify, 14 seats; one v1 wave)",
    "reportDir": ".ufo/waves/round-83/w1",
    "axes": ["operability", "depth", "calibration", "coverage", "freshness", "adjacency"],
    "context": CONTEXT,
    "items": ITEMS,
}

if __name__ == "__main__":
    print(json.dumps(SPEC, indent=1, ensure_ascii=False))
