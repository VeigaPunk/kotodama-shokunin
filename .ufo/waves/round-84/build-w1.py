#!/usr/bin/env python3
"""Build the kotodama round-84 v1 wave spec (one wave, 12 seats). Prints the spec JSON."""
import json

LANE = "/home/vgpnk/Projects/shokunin/kotodama-shokunin"
FLEET = "/home/vgpnk/Projects/shokunin"
BASE = "81499ee45b5751d388fefc78583810878de01ecd"
FREEZE = "7e6ee2f8f7b54dbeecf42cfe96050e533a86a6e2"
WAVE = LANE + "/.ufo/waves/round-84/w1"
ENTRY = "corpus/knowledge/myth-symbol/witchcraft-sorcery-accusation-institution.md"
TOOL = "tools/apply-sound-laws.py"
EXDIR = "examples/sound-laws"
GODSPEED = """/skill:godspeed

You are a Godspeed-enabled subagent.

1. **Name the axes.**
2. **Iterate cheap, in parallel.**
3. **Keep moves that improve any axis and harm none.**
4. **Don't aim \u2014 let the frontier walk itself.**

"""

CONTEXT = f"""# Goal
Kotodama round 84 (hyaku run 15), ONE v1 wave of 12 seats: build and falsify the round's two claims together.
Lane repo {LANE} (jj-colocated; git is the backend). Fleet root {FLEET}.
Lane base revision {BASE}; frozen claims/counters commit {FREEZE}. Read any base byte with
`git -C {LANE} show {BASE}:<path>` and any frozen byte with `git -C {LANE} show {FREEZE}:<path>`.

# Claims (frozen before any data; do not renegotiate a target)
- **D (depth).** `{ENTRY}` lands as the 258th knowledge file: witchcraft and sorcery as an
  **accusation institution** (the vocabulary set, the accusation grammar, the proof technology, the
  confession, the slander law, the social functions), >= 16000 bytes, >= 7 `## ` sections, >= 6 data
  rows in `## 2. Six design decisions`, >= 20 anchors in `## 3. Attested anchors` each carrying exactly
  one distinct S-id across >= 4 ids, `tools/check-cited-lines.py` = 0 findings. Rows S914\u2013S917 are
  opened this round (2026-11-04), each `mined`, each `used-by` naming the entry; the entry cites at
  least three of them. SOURCES grows 837 -> >= 841.
- **O (operability, capability acquisition).** `{TOOL}` lands: a deterministic, dependency-free
  applier for ordered sound laws over a segment-tokenised proto-lexicon, one trace line per change,
  with `selftest` and `apply --rules --input --out [--trace]`. A committed example under `{EXDIR}/`
  (>= 12 words, >= 6 ordered rules) is reproduced byte-for-byte by the tool; the summary line is
  `SOUNDLAWS: <w> words / <r> rules / <c> changes` with w>=12, r>=6, c>=12; every rule fires in the
  trace; three malformed inputs exit 2 with a `SOUNDLAW_ERROR:` label and no traceback; the tool and
  both round-84 counters get `## Gates and probes` rows.

# Frozen tool contract (claim O; build exactly this)
CLI: `python3 {TOOL} --selftest` (alias `selftest`) and `python3 {TOOL} apply --rules PATH --input PATH --out PATH [--trace PATH]`.
Input TSV: `gloss<TAB>seg1 seg2 ...` (segments space-separated, `#` comment lines allowed, blank lines ignored).
Rules JSON: `{{"rules":[{{"name":str,"from":str,"to":str,"pre":[str],"post":[str]}}, ...]}}`; `pre`/`post` are
segment lists where `"#"` means the word start (pre) or word end (post); rules apply in file order, each
rule one left-to-right non-overlapping pass over the current word; `to` may be `""` (deletion).
Output TSV: `gloss<TAB>derived segments`, input order preserved. Trace TSV: one line per change,
`gloss<TAB>index<TAB>rule<TAB>before<TAB>after`.
On any input error print `SOUNDLAW_ERROR: <label>: <detail>` to stderr and exit 2, never a traceback.
`selftest` runs in-process checks and prints `SELFTEST: PASS (<n> checks)` on stdout, exit 0.

# Frozen row contract (claim D; build exactly this)
Eleven cells, no `|` inside any cell: id | source | kind | tier | scope | anchor | teaches | status |
opened | recheck | used-by. `opened` = `2026-11-04`, `status` = `mined`, `used-by` names {ENTRY}.
The row's `source` cell carries the URL(s) and the fetch facts (HTTP status, bytes, sha256, capture);
the `anchor` cell names the section/verse/page range of the located quote; `teaches` says what the
source teaches for that scope. A rejection is a row with `status=rejected`, its reason and its flip
condition in `teaches`.

# Bounds (binding)
- Write ONLY the files your assignment names. Everything else in the lane, the fleet repo, sibling lanes,
  `.ufo/state/`, `MANIFEST.json` and `{FLEET}/.scratch/` is read-only. Never edit `corpus/SOURCES.md`,
  `SKILL.md`, `corpus/QUALITY.md` or `considerthese/` (absent here) — the L1 lands every byte.
- NEVER commit, push, or run a mutating git/jj command. The L1 lands every byte. Read-only git is fine.
- Use ABSOLUTE paths in every command and every `write`. Seat tools start at the fleet root: a relative
  path lands in the FLEET repo. Every `Report:` trailer path is relative to {LANE} \u2014 write it at
  {LANE}/<that path>.
- Git fixtures (only where an assignment asks for one): `D=$(mktemp -d) && git -C "$D" init -q`, every later
  git call names `-C "$D"` explicitly, and verify `git -C "$D" rev-parse --show-toplevel` equals `$D` before
  the first commit. Never commit with a throwaway identity anywhere else.
- Scratch: your dir is `/fast/scratch/hyaku/kotodama-r84/<YourSeatName>` (create it, `trap 'rm -rf -- "$S"' EXIT`,
  copy receipts into {WAVE}/ before exiting, and report if anything is left behind). `/tmp` is for files under
  50 MB only and a `/tmp` path is never citable evidence. Do not hardcode `/tmp` in anything committed.
- **No absolute scratch path may appear in any committed report/receipt you write**: cite repo-relative
  paths only (QUALITY criterion 31 binds; `tools/check-cited-records.py` grades it).
- Sources: open by ordinary means only (plain HTTP GET; no challenge met or passed, no login, no paywall
  workaround), record URL, HTTP status, byte count, sha256 and access date 2026-11-04.
- Tooling: you may install/upgrade tools that help the task (read `/home/vgpnk/.omp/agent/RULES.md` first:
  official channels, update-safety gate, record tool/version/channel/reason). **All pacman transactions are
  PAUSED host-wide** \u2014 use `uv tool`/`npx`/an official binary in `~/.local/bin`, never `pacman -S/-Sy/-Syu/-U/-R`.
- Never message `agent://all`. Return findings; do not send progress updates.
"""

ITEMS = []


def it(name, role, axes, prompt):
    ITEMS.append({"name": name, "role": role, "axes": axes, "milestone": "r84-v1", "prompt": GODSPEED + prompt})


it("ScoutGapWitch", "scout", ["depth", "coverage"],
   f"RECON \u2014 claim-D absence census and partial-owner map. READ-ONLY; write only under {WAVE}/stage/ScoutGapWitch/.\n"
   "1) Prove or refute the before-state at " + BASE + ": filename sweep over `corpus/knowledge/**/*.md` for\n"
   "   pattern `witch|witches|witchcraft|sorcer|sorcery|malefic` (case-insensitive) — expect 0 owning\n"
   "   basenames; the matter-of-subject scan `grep -rlE '^- topic: .{0,160}\\b(witchcraft|sorcery|witch|sorcerer|malefic)'\n"
   "   corpus/knowledge` — expect 0 files; the word-boundary occurrence census `grep -rniE '\\b(witch|witches|witchcraft|sorcerer|sorcery|malefic)\\b'`\n"
   "   — expect ~19 lines in ~10 files, every one a passing attribute; and `- gap filled:` lines naming the surface = 0.\n"
   "   Paste every command and its raw output.\n"
   "2) Map the partial owners one-way: for each file that mentions the surface, name what that file owns and what it\n"
   "   does NOT answer (amulets, divination, binding speech, colour symbolism, funerary, purity). Cite line numbers.\n"
   "3) Extract the frontier rows from `corpus/README.md` `## Known gaps (frontier)` that bear on ritual institutions,\n"
   "   and say which frontier row this entry advances and which it leaves open.\n"
   "4) Write `gap-census.md` with a machine-readable summary table (file, owner, lines). Also write `gap-census.json`\n"
   "   with the exact counts. No recommendation about canon.")

it("ScoutSourcesWitch", "scout", ["depth", "freshness"],
   f"RECON \u2014 open the four claim-D candidate sources by ordinary means and produce the independent second reading.\n"
   f"Write only under {WAVE}/stage/ScoutSourcesWitch/.\n"
   "Candidates, in the id order the rows will take:\n"
   "  S914 = 'Witchcraft', Encyclopaedia Britannica 11th edn (Wikisource transcription),\n"
   "         https://en.wikisource.org/wiki/1911_Encyclop%C3%A6dia_Britannica/Witchcraft\n"
   "  S915 = 'Sorcery', Encyclopaedia Britannica 11th edn (Wikisource transcription),\n"
   "         https://en.wikisource.org/wiki/1911_Encyclop%C3%A6dia_Britannica/Sorcery\n"
   "  S916 = Malleus Maleficarum (Kramer & Sprenger; Summers translation), Wikisource,\n"
   "         https://en.wikisource.org/wiki/Malleus_Maleficarum\n"
   "  S917 = Charles W. Upham, Salem Witchcraft, Volumes I and II (1867), Project Gutenberg eBook #17845,\n"
   "         https://www.gutenberg.org/cache/epub/17845/pg17845.txt\n"
   "For each: plain HTTP GET on 2026-11-04, record HTTP status, byte count, sha256 of the served bytes, and\n"
   "the page's own revision/edition marker where the page carries one; locate TWO candidate quotes per source\n"
   "(one about the practice/institution, one about procedure/accusation) with the section/verse/page locator;\n"
   "record each quote's raw and folded occurrence counts and a <=25-word excerpt. Note every access limit\n"
   "(transclusion, template rendering, missing capture) explicitly. If a source cannot serve quotable prose,\n"
   "say so with the raw/folded counts and name a substitute candidate you did open.\n"
   "Write one receipt per row `S914.txt`..`S917.txt` plus `second-reading.md` summarising what each source\n"
   "does and does not teach. Never edit corpus/SOURCES.md.")

it("ExecSoundLaws", "executor", ["operability", "depth"],
   f"BUILD \u2014 `{TOOL}` and its committed example. The L1 lands them; you write and prove them.\n"
   f"Write only under {WAVE}/stage/ExecSoundLaws/: `apply-sound-laws.py`, `proto-lexicon.tsv`, `rules.json`,\n"
   "`expected.tsv`, `expected-trace.tsv`, `selftest.txt`, `demo.txt`, `negatives.txt`, `notes.md`.\n"
   "1) Implement exactly the frozen CLI contract in the wave context (python3 stdlib only, no third-party imports,\n"
   "   no network, no writes outside the paths the caller names). Refuse before writing on: missing rules file,\n"
   "   rules file that is not JSON, a rule missing/having an empty `from` or `name`, `pre`/`post` not lists,\n"
   "   duplicate rule names, input line without a TAB, and an output path that equals the rules or input file.\n"
   "   Every refusal prints `SOUNDLAW_ERROR: <label>: <detail>` to stderr and exits 2.\n"
   "2) `selftest` must be a real in-process battery with at least 24 cases: single-segment change, deletion,\n"
   "   insertion via `to` of a new segment, word-start `#` anchor, word-end `#` anchor, pre+post context both,\n"
   "   non-overlap within one pass (a a > ... must not cascade), rule ordering (two rules whose order changes the\n"
   "   output), no-match preservation, multi-segment input, empty word refusal, each negative case above, and a\n"
   "   trace-shape case. Print `SELFTEST: PASS (<n> checks)` and exit 0 only when every case passes.\n"
   "3) Build the example as a two-era derivation grounded in `corpus/knowledge/linguistics/historical-linguistics.md`\n"
   "   (read it at " + BASE + ", quote the section you follow in notes.md): 12\u201316 proto-words from a plausible\n"
   "   segment inventory, 6\u20137 ordered rules of different types (final vowel loss, intervocalic lenition or\n"
   "   voicing, cluster simplification, assimilation, umlaut/vowel harmony, word-initial change, a deletion).\n"
   "   Run the tool to produce `expected.tsv` and `expected-trace.tsv`; hand-check at least three words against\n"
   "   the rules and record the hand derivation in notes.md.\n"
   "4) Prove: run `--selftest` (save stdout/exit to selftest.txt), run `apply` on the example (save demo.txt with the\n"
   "   summary line and the trace fire counts), run three negatives (missing rules, bad JSON, empty-from) and save\n"
   "   negatives.txt with rc and stderr. Report the exact command lines.")

it("ExecBeforeState", "executor", ["calibration", "depth"],
   f"MEASURE \u2014 the red-before receipts for both claims at {BASE}. READ-ONLY; write only under {WAVE}/stage/ExecBeforeState/.\n"
   "1) Claim D before-state: knowledge file count under `corpus/knowledge` (expect 257); registry row count in\n"
   "   `corpus/SOURCES.md` under the census grammar (`^ {0,3}\\| *S[0-9]{3,}`) (expect 837); the four sweep commands\n"
   "   from ScoutGapWitch's brief, re-run independently with raw output; the entry path absent.\n"
   "2) Claim O before-state: `git ls-tree -r --name-only <base> tools examples | grep -ciE 'sound.?law|soundchange'`\n"
   "   (expect 0); `git grep -c SOUNDLAWS <base> -- tools examples reports` (expect 0 lines); `examples/sound-laws`\n"
   "   absent; `python3 -B tools/check-gate-registry.py --root .` at the lane tip (paste its two lines).\n"
   "3) Claim D source-side before-state: for each of the four candidate rows, `grep -c '| S91[4-7] |' corpus/SOURCES.md`\n"
   "   (expect 0).\n"
   "4) Write `before.json` (numbers) and `before.md` (commands, raw output, exit codes). Every command names the\n"
   "   revision it reads. Do not measure the working tree for a base-state claim: use `git show <base>:<path>`.")

it("ExecRegistryRows", "executor", ["operability", "calibration"],
   f"BUILD \u2014 the three `## Gates and probes` rows claim O needs. Write only under {WAVE}/stage/ExecRegistryRows/.\n"
   "1) Read `SKILL.md` `## Gates and probes` at " + BASE + " and re-derive, independently of tools/check-gate-registry.py:\n"
   "   the data-row count (expect 74), the header/separator shape (8 cells), the instrument set\n"
   "   (`reports/round-*/accept-*.py`, expect 61) and which instruments are unrowed (expect 0). Paste the commands.\n"
   "2) Draft exactly three rows in the table's 8-cell shape, matching the house prose of the last rows:\n"
   "   - name `apply-sound-laws`, kind `gate (capability)`, entry command\n"
   "     `python3 -B tools/apply-sound-laws.py --selftest && python3 -B tools/apply-sound-laws.py apply --rules examples/sound-laws/rules.json --input examples/sound-laws/proto-lexicon.tsv --out /dev/null`\n"
   "     (name a real read-only path, never `/dev/null` if the house does not; choose the safest read-only form and say why),\n"
   "     verdict map 0 pass / 1 findings / 2 could-not-evaluate, self-test `--selftest (>=24 checks)`, pinned values the\n"
   "     committed example, write scope `read-only`, owner kotodama-shokunin;\n"
   "   - name `accept-d-84`, entry command `python3 -B reports/round-84/accept-d84.py --root . --lands <rev> --freeze " + FREEZE + " --work <dir>`,\n"
   "     verdict `0 pass / 1 fail / 2 usage-env`;\n"
   "   - name `accept-o-84`, same shape for accept-o84.py.\n"
   "   No `|` inside a cell; no absolute scratch path; do not invent numbers you did not measure.\n"
   "3) Write `rows.md` (the exact three lines), `row-check.md` (11-cell/8-cell shape audit and the dead-token check\n"
   "   that each .py path resolves at " + BASE + " or is the new tool), and `registry-census.json`.\n"
   "4) State what `GATE-REGISTRY` and `GATE-REGISTRY-INFO` must print after the three rows land (missing 0,\n"
   "   registered >= 77, instruments >= 63, unrowed <= 25) and why.")

it("ScribeEntryWitch", "scribe", ["depth", "coverage"],
   f"WRITE \u2014 the claim-D knowledge entry draft. Write only {WAVE}/stage/ScribeEntryWitch/{ENTRY.split('/')[-1]} and `notes.md`.\n"
   "Shape (a frozen counter grades it): >= 16000 bytes; the eight header fields in the house order\n"
   "(`- topic:`, `- gap filled:`, `- sources:`, `- couples:`, `- source:`, `- verified-at:`, `- recheck:`, `- scope:`);\n"
   ">= 7 `## ` sections with `## 2. Six design decisions` carrying >= 6 data rows and `## 3. Attested anchors`\n"
   "carrying >= 20 bullets, each bullet naming EXACTLY ONE distinct S-id (S914\u2013S917 or an already registered\n"
   "row), across >= 4 distinct ids; no table row may carry an S-id (the lane's cited-lines lint flags it).\n"
   "Content: witchcraft and sorcery as an ACCUSATION INSTITUTION for a fictional culture \u2014 the vocabulary set\n"
   "(witch / sorcerer / healer / diviner / accuser and the translation traps), the accusation grammar (who may\n"
   "accuse whom, what counts as evidence, when an accusation is actionable), the proof technology (oracle,\n"
   "ordeal, divination, possession, confession, the counter-accusation), the confession and its extraction,\n"
   "the slander/defamation side (the accused who sues), witch-finding movements and their life cycle, and the\n"
   "social functions an accusation carries (levelling, scapegoating, boundary maintenance, inheritance and\n"
   "property). Give the designer a build order and a decision table with real thresholds; keep every factual\n"
   "anchor inside the cited row's scope and mark contested frameworks as contested. Cite the four new rows for\n"
   "their own material and the partial owners one-way by path. A worked NON-CANON derivation of one invented\n"
   "accusation case, and a lore handoff section. Real-world-inspiration boundaries\n"
   "(`corpus/knowledge/verification/real-world-inspiration-boundaries.md`) bind: published scholarship only,\n"
   "no claim about any living community, no accusation instructions.\n"
   "Open the sources yourself by ordinary means where an anchor needs a quote; record URL and access date\n"
   "2026-11-04 in notes.md. Do not write corpus/SOURCES.md.")

it("ScribeRowsWitch", "scribe", ["depth", "freshness"],
   f"WRITE \u2014 the four claim-D registry rows and their Gate bullets. Write only under {WAVE}/stage/ScribeRowsWitch/.\n"
   "1) Open each candidate source yourself by ordinary means on 2026-11-04 (URL in the wave context). For each row\n"
   "   write the 11 cells exactly as the row contract in the wave context says: id | source | kind | tier | scope |\n"
   "   anchor | teaches | status | opened | recheck | used-by. `source` carries URL(s) + HTTP status + bytes +\n"
   "   sha256 + capture state; `anchor` names the located section/verse/page; `teaches` is what the source teaches\n"
   "   for that scope, with its framework status and limits; `opened` = 2026-11-04; `status` = mined; `used-by` =\n"
   "   " + ENTRY + ". No `|` anywhere inside a cell; keep every cell under 1200 characters.\n"
   "2) Write the four lines to `rows.md` (one line each, nothing else in the file). Run\n"
   "   `python3 -B tools/check-row-fragments.py --selftest` and describe its contract, then build a scratch mirror\n"
   "   (under your scratch dir, never the lane) of `corpus/SOURCES.md` + your four rows and run\n"
   "   `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --file <mirror>/corpus/SOURCES.md`;\n"
   "   paste the exit code. If the mirror fails, fix the rows in the mirror before reporting (never the lane).\n"
   "3) Write `gate.md`: for each row, the URL, access date, locator and a <=25-word located quote (the lesson Gate\n"
   "   copies this verbatim). Also write `recheck.md` naming the cadence each row should take and why.\n"
   "4) If a candidate source cannot supply a quotable located span, do NOT invent one: report the failure with the\n"
   "   raw/folded counts and propose a substitute you did open, keeping the id order.")

it("ConnectorOverlap", "connector", ["adjacency", "coverage"],
   f"CONNECT \u2014 sibling-overlap scan for both claim surfaces. READ-ONLY; write only {WAVE}/stage/ConnectorOverlap/overlap.md.\n"
   "1) For claim D (witchcraft/sorcery accusation as an institution): scan sibling lane repos under\n"
   f"   {FLEET} for an owner of the surface (filenames and topic lines; do not read whole trees — use grep).\n"
   "   Name every lane you checked, each hit with path:line, and whether the material is a handoff target\n"
   "   (lore: canon), a neighbour (religion/ritual), or another lane's province (chousa research method,\n"
   "   mado security, kagi rights). Check lore-shokunin's world-bible contract one-way references.\n"
   "2) For claim O (ordered sound-law applier): search sibling lanes for an existing applier or gate that would\n"
   "   duplicate it, and for an in-corpus tool (`tools/check-craft-exercise.py`, `tools/gates/*`) whose contract\n"
   "   the new tool should mirror or explicitly differ from. Name the overlap and the difference.\n"
   "3) State the one-way handoff: what kotodama supplies to lore and what stays here. Report, never absorb.\n"
   "4) Return a short verdict: 'no sibling owner' or the owner+path, per surface.")

it("ReviewerEntry", "reviewer", ["depth", "calibration"],
   f"REVIEW \u2014 attack the claim-D entry draft against the lane's own bar. Write only {WAVE}/stage/ReviewerEntry/review.md.\n"
   "1) Read the draft at `{WAVE}/stage/ScribeEntryWitch/witchcraft-sorcery-accusation-institution.md` when it exists.\n"
   "   If it is not there yet, wait by re-reading once per ~60 s at most three times while you do the rest of this\n"
   "   brief; if it never appears, review the *contract* (claims.json claim D) and say so.\n"
   "2) Grade against QUALITY criteria 10, 11, 12, 18, 21, 24, 27, 30 and 31 (read `corpus/QUALITY.md` at " + BASE + "):\n"
   "   is every anchor inside its row's scope? Does any sentence overreach the cited source, restate a contested\n"
   "   framework as fact, or import a living-community claim? Is each anchor bullet single-id? Does any table row\n"
   "   carry an S-id (the lint would flag it)? Are the four new rows cited for material they actually teach?\n"
   "3) Check the real-world-inspiration boundary file and PROVINCE.md: does the entry hand canon to lore and stay\n"
   "   out of chousa/kagi ground?\n"
   "4) Return a numbered list of defects with exact locations and a required edit each, ordered by severity, plus\n"
   "   an explicit PASS/FAIL on the frozen shape (bytes, sections, decision rows, anchor count, single-id rule).")

it("CriticClaims", "critic", ["calibration", "operability"],
   f"FALSIFY \u2014 attack both claims before their artifacts land. READ-ONLY; write only {WAVE}/stage/CriticClaims/attack.md.\n"
   "1) Re-derive each before-state yourself at " + BASE + " and say whether the frozen before-text is true; name any\n"
   "   count that differs. Check the surface-absence claim for claim D (no topic-line owner, only passing mentions).\n"
   "2) Attack the counters' kill power: for each of the two counters read `reports/round-84/accept-*.py` at " + FREEZE + " and\n"
   "   name a landing that would satisfy the frozen after-state text but should NOT count as the claimed work\n"
   "   (a stub entry with 20 filler anchors, a tool that hardcodes the example output, a selftest that prints a\n"
   "   canned count). Say which leg catches each or, honestly, that none would.\n"
   "3) Attack the do-nothing control: run both counters at `--lands " + BASE + "` and paste the refusal lines; then\n"
   "   run both at `--lands " + FREEZE + "` and paste the leg tables (the red-before).\n"
   "4) Test the frozen tool contract for ambiguity: name any rule case where two correct implementations would\n"
   "   disagree (overlap, ordering, `#` anchoring, insertion), and state the reading the contract forces.\n"
   "5) List what would falsify each claim's after-state in one command.")

it("MutationTester", "mutation-tester", ["operability", "calibration"],
   f"MUTATION RUN against the round's instrument, before data. Write only under {WAVE}/stage/MutationTester/ and one scratch dir.\n"
   "1) Build five single-predicate mutants of the *claim artifacts*, as standalone stubs committed into a scratch\n"
   "   clone of the lane at " + FREEZE + " (fixture identity only in that clone; never the lane):\n"
   "   m1 entry whose anchor bullets each carry two S-ids (expect the LINT or ANCHORS leg);\n"
   "   m2 entry with 19 anchors against the frozen floor of 20 (expect ANCHORS);\n"
   "   m3 a new row with `status=queued` (expect ROWS);\n"
   "   m4 a tool that copies the committed expected.tsv to `--out` regardless of the rules (expect DEMO);\n"
   "   m5 a tool whose malformed-input path exits 0 and writes an empty out file (expect NEGATIVE).\n"
   "   For each, grade with the frozen counter at that stub commit and paste the leg line that fires. If a mutant\n"
   "   survives, that is an honest gap to name, not to fix.\n"
   "2) Also mutate the two counters one line each (three mutants total: D's ANCHORS accepts two ids; O's DEMO skips\n"
   "   the expected-bytes compare; O's REGISTRY ignores the unrowed-tool cap) and report whether any real artifact\n"
   "   would catch the mutation — name the gap if none exists.\n"
   "3) Report the mutation score and the weakest predicate. Fixture repos: `D=$(mktemp -d) && git -C \"$D\" init -q`,\n"
   "   verify toplevel, fixture identity only there.")

it("SentinelScope", "sentinel", ["adjacency", "calibration"],
   f"READ-ONLY ADVERSARIAL PROBE of scope, file-I/O and append-only discipline. Write only {WAVE}/stage/SentinelScope/probe.md.\n"
   "1) Enumerate at " + FREEZE + " every file this round plans to write (claims.json's own_paths per claim, the wave\n"
   "   stage) and check each lies inside the lane repo and nowhere else. Check the fleet repo is untouched:\n"
   f"   `git -C {FLEET} status --porcelain` and report any file this round's seats wrote there (do not delete it).\n"
   "2) Audit the planned tool's file I/O surface from the frozen contract: which paths can it read, which can it\n"
   "   write, can `--out`/`--trace` escape the caller's directory, can a rule or input line inject a path, and what\n"
   "   happens on a symlink or an existing directory. Name each risk and whether the contract forbids it.\n"
   "3) Prove the registry is append-only across the planned changes: write a checker in your scratch dir that flags\n"
   "   any existing row whose cells 0..6 move; state exactly which rows the round intends to modify in place.\n"
   "4) Check `PROVINCE.md` is byte-identical between base and freeze, and that no round-84 artifact touches\n"
   "   `MANIFEST.json`, `.ufo/state/` or a sibling repo. Look for credential material or absolute personal paths in\n"
   f"   the round's committed receipts (`git -C {LANE} grep -nE '/home/[a-z]+/(\\.ssh|\\.config|\\.aws)' " + FREEZE + " -- reports/round-84`).\n"
   "5) Report findings with severity; no fixes in the lane.")

SPEC = {
    "wave": "kotodama-r84-v1",
    "milestone": "Round 84 wave 1 (build + falsify, 12 seats; one v1 wave)",
    "reportDir": ".ufo/waves/round-84/w1",
    "axes": ["depth", "operability", "coverage", "calibration", "freshness", "adjacency"],
    "context": CONTEXT,
    "items": ITEMS,
}

if __name__ == "__main__":
    print(json.dumps(SPEC, indent=1, ensure_ascii=False))
