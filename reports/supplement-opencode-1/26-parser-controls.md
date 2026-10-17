# 26 — Parser controls: malformed / duplicate / ambiguous culture packets against the gate loaders

- **Wave:** supplement-opencode-1 (not a numbered GLM round)
- **Baseline revision:** `fe34faaafbe0add59ff68827a0df6c5782a72404`
- **Role:** reviewer. No parser, fixture, or expected-output file was modified.
- **Scope tested:** the five culture-packet (YAML/JSON) gate loaders:
  `phonology-sanity-gate.py`, `naming-collision-gate.py`, `myth-consistency-gate.py`,
  `costume-era-consistency-gate.py`, `lexicon-coverage-audit.py`.
  `handoff-packet-check.py` and `provenance-audit.py` consume markdown entries, not packets — out of scope.

Baseline identity of every file reviewed (blob = `git rev-parse fe34faa:<path>`,
sha256 = the bytes actually executed; all five were `unchanged vs fe34faa` at test time):

| gate | baseline blob | sha256 |
|---|---|---|
| phonology-sanity-gate.py | `441f1c5dada40cf6a35691f648dc7a3ec6c4d874` | `fb05c644cafb0855481beb5d8bc3f619ae688d8b12787e530f01543f85372655` |
| naming-collision-gate.py | `a32267a718760d4cc0c515bd48bdc32a37853e57` | `8c5afb0a5abc8b00a659120e3795586ddce688bd962ccc68f7308f7bf19aa526` |
| myth-consistency-gate.py | `21a5e3b5c88f8a4e65a64770da2c78d93b80b534` | `26d246e9936db4375c31c6eb260545bf55051d11ec00bb1e757458399b1b55c5` |
| costume-era-consistency-gate.py | `700747e287af740b87b1672dd6233e68a1125348` | `29a9361c7b96a354c41a3994e3459a951ce0a43425b3984d6506b3e5b3a43f03` |
| lexicon-coverage-audit.py | `2e7662bd9a12580b60efb2d688d061057f1735c1` | `63ee4ec6b15188fefa3e997766971d66fe4d7d7bf9eed65cdcdd55f548fe8a80` |

Method: payloads generated **in memory**, written to an auto-cleaned
`tempfile.TemporaryDirectory()` (no repo scratch used), each gate invoked as a subprocess
(`python3 <gate> <packet.yml>`), return code + first stdout/stderr lines recorded. No
payload was written under the repo; `git status` for `tools/gates/` stayed clean.

---

## 1. What is correct (verified, not assumed)

1. **No code execution path.** A scan of `tools/**/*.py` for
   `import yaml|from yaml|yaml.load|yaml.safe|eval(|exec(|__import__|pickle|marshal.loads|os.system`
   produced only two substring false positives, both read and dismissed: `assemble-d2.py:79,86`
   (`yield from yaml_lines(...)` — a local renderer, not a library) and the untracked
   `replay-frozen.py:403` (`subprocess.run([... str(snapshot) ...])` — "snapshot" contains "sh").
   No loader imports a YAML library or calls a dynamic-execution primitive, and `_parse_scalar` in
   every loader can only construct `str/int/float/bool/None/list/dict`.
   The PyYAML RCE payload `!!python/object/apply:os.system ["touch <marker>"]` was placed in
   `name:` (and in a DERIV `output:` field) in all five gates: **no marker file was created in any
   run**, and no gate errored differently because of the tag. Alias expansion is absent, so a
   "billion laughs" anchor bomb is structurally impossible.
2. **CLI exit handling for I/O and usage.** All five gates return **2** for: no argument,
   wrong argument count, missing path, and a directory path — each with an explicit
   `FINDING G-DATA …` / `ERROR: …` message (lexicon prints its reason to stderr, which its
   docstring lines 20–26 declares).
3. **Explicit not-evaluable for whole-packet failures.** Empty file, non-mapping root, and
   missing required section all produce an explicit could-not-evaluate diagnostic in every gate:
   `G-DATA` exit 2 (phonology/costume/lexicon; myth for parse failures), `PHON-PROFILE`/`CROSS-HOLD`
   HOLD exit 1 (naming), `MC-P00`-family exit 1 (myth). No gate silently passes such a packet.
4. **One gate is strict where it should be.** `myth-consistency-gate.py:267-268` rejects duplicate
   **block-mapping** keys: `name: a` / `name: b` → `FINDING G-DATA: duplicate key 'name'`, exit 2.
   `lexicon-coverage-audit.py:1490` has a selftest case for `name: [unclosed` (its parser rejects it).

## 2. Divergence matrix (identical bytes, five gates)

`rc` = process exit code; `IDs` = finding ids printed.

| payload | phonology | naming | myth | costume | lexicon |
|---|---|---|---|---|---|
| `consonants: [p, t, k` (unterminated flow) | **rc=1** M-CLASS,T-C · *evaluated* | rc=2 G-DATA | rc=2 G-DATA | rc=2 G-DATA | rc=2 ERROR |
| duplicate `phonology:` block key | **rc=1** I-UNKNOWN,A-NEUTRAL,M-EJECT · *last wins* | rc=1 (silent) | rc=2 G-DATA `duplicate key` | rc=2 | rc=2 |
| `name: &tag …` / `name: *tag` | rc=1 | rc=1 PHON-INVENTORY `/*/` | rc=1 | rc=2 | rc=2 |
| tab indentation (complete packet) | **rc=0 silent** (tab→2 spaces) | rc=2 G-DATA | rc=2 `unparsed YAML content` | rc=1 (same finding as spaces; tab→4 spaces) | rc=2 ERROR |
| `---` multi-document | rc=2 | **rc=1** (documents merged, not rejected) | rc=2 | rc=2 | rc=2 |
| `!!python/object/apply:os.system …` | rc=1, no exec | rc=1, no exec | rc=1, no exec | rc=2, no exec | rc=2, no exec |
| empty / non-mapping root | rc=2 explicit | rc=2 explicit | rc=2 explicit | rc=2 explicit | rc=2 explicit |

## 3. Defect register (counterexamples)

Severity: **high** = silent wrong verdict on plausible authoring input;
**medium** = silent guess or documented-contract violation needing crafted input;
**low** = hardening. Nothing here was fixed — reviewer role.

### D1 (medium) Unterminated flow sequence is silently closed — `phonology-sanity-gate.py:323-330`
`_parse_scalar` uses `body = s[1:-1] if s.endswith("]") else s[1:]`, so a truncated
`[p, t, k` becomes the list `['p', 't', 'k']`.
Evidence: direct in-memory call `_parse_scalar("[p, t, k")` → `['p', 't', 'k']`; CLI on the
truncated packet → `rc=1`, `FINDING T-C: REVIEW — 3 distinct consonants …` (the gate audited a
document that is not valid YAML). All four siblings return exit 2 on the same bytes.
Documented contract: the module docstring says exit 2 for an "unparseable packet" (lines 11-15).

### D2 (high) Duplicate mapping keys silently last-win in 4 of 5 loaders — no diagnostic
Overwrite sites: `phonology-sanity-gate.py:416`, `naming-collision-gate.py:430`,
`costume-era-consistency-gate.py:274`, `lexicon-coverage-audit.py:465`;
`myth-consistency-gate.py:249` (flow mappings only — its block check at 267 misses flow form:
direct call `parse_packet("phonology: {consonants: [p], consonants: [k]}")` →
`{'phonology': {'consonants': ['k']}}`, no error).
JSON paths are also silent (`json.loads`: costume `:325-332`, lexicon `:498-503`).
Counterexample that **flips a verdict**: a naming packet carrying

```yaml
orthography: {case: contrastive}
orthography: {case: display-only}
```
emits `NAME-REUSE …` (last wins) with no duplicate-key finding, while the same packet with only
`contrastive` emits `NAME-CASE,PHON-INVENTORY`. Same class in phonology: two `phonology:` blocks
give `I-UNKNOWN,A-NEUTRAL,M-EJECT` (last wins) where the first block alone would be clean.
An author's stale key silently changes the audit outcome — this is exactly the "ambiguous packet"
class this review was asked to test, and no gate reports it.

### D3 (medium) Anchors and tags are guessed, not rejected — contradicted by the naming gate's own policy
`naming-collision-gate.py:57-60` states: "No anchors, tags, multi-document streams, or tab
indentation; input outside the subset exits 2 instead of being guessed."
Observed: `name: &tag anchor-probe` keeps the literal, and `name: *tag` is audited as the form
`*tag` → `FINDING PHON-INVENTORY: FAIL — name N1 '*tag': symbol /*/ at position 1 is not in the
declared inventory`. The gate invented a phoneme-level defect from syntax it promised to reject.
phonology/myth/costume/lexicon also parse tags and anchors as literal text (no rejection).

### D4 (medium) YAML 1.1 boolean coercion re-renders authored forms — `naming-collision-gate.py:199-203`, `:450-457`
`_parse_scalar` maps `yes|no|true|false` (any case) to `bool`; `_s()` renders booleans back as
`"true"`/`"false"`. Counterexample: a packet whose name is `no` with inventory
`consonants: [p, t, n]`, `vowels: [a, o]` yields

```
FINDING PHON-INVENTORY: FAIL — name N1 'false': symbol /f/ at position 1 is not in the declared inventory …
```
— a FAIL finding about a name that appears nowhere in the packet, while the authored `no`
would have parsed cleanly. `yes` → `'true'`; `on`/`off` stay strings here but become booleans in
`myth-consistency-gate.py:219-225` (`on|yes|true`, `off|no|false`); `phonology-sanity-gate.py:343-344`
coerces only `true|false`, so the same authored token is typed differently per gate.
(PyYAML compatible for these tokens — but an audit tool must not silently audit a different form.)

### D5 (medium) Tab indentation has four different outcomes
- `phonology-sanity-gate.py:289`: `raw.replace("\t", "  ")` → a fully tab-indented valid packet returned **rc=0, no output**.
- `costume-era-consistency-gate.py:334`: `text.replace("\t", "    ")` → tab-indented packet produced the
  same finding as its space-indented twin (silently accepted, 4-space assumption).
- `naming-collision-gate.py:154-157` and `lexicon-coverage-audit.py:399-400`: exit 2, explicit message.
- `myth-consistency-gate.py:321-325`: the guard tests only the *space* prefix
  (`indent_text`), so a line beginning with a tab is collapsed to indent 0 and the tab is stripped;
  a tab-indented child block either evaluates (rc=1 with unrelated MC-* findings, tab payload v1) or
  dies with the misleading `FINDING G-DATA: unparsed YAML content at token 7` (v2). The documented
  tab rejection does not fire for leading tabs.
- Multi-document input is the same class of promise: `naming-collision-gate.py` converts
  `---`-separated files by merging the documents into one packet (probe: doc 1 supplying
  `phonology`+`names`, doc 2 supplying `name` → the union evaluated, rc=1, only `CROSS-HOLD`),
  not by rejecting the stream as its docstring declares.

### D6 (medium) Uncaught `RecursionError` → traceback and exit 1 on deep flow nesting
3000 nested `[`…`]` inside `phonology.consonants` (balanced, valid-ish input):
`phonology` and `naming` both print a Python traceback ending
`RecursionError: maximum recursion depth exceeded`, return **rc=1** in ~0.2 s, and print no finding.
Exit 1 is the gates' "findings" code, so a caller cannot distinguish a crash from a FAIL, and the
documented "2 = could-not-evaluate" contract is violated. Recursive sites:
`phonology-sanity-gate.py:327`, `naming-collision-gate.py:324-345`.

### D7 (medium) Non-UTF-8 packet file → traceback, exit 1, in 2 of 5 gates
File `name: caf\xe9-probe` encoded Latin-1: `phonology` and `myth` raise uncaught
`UnicodeDecodeError` (traceback, rc=1) because their `main` catches only `OSError`
(`phonology-sanity-gate.py:1279-1284`, `myth-consistency-gate.py:833-837`).
`naming` (`:1710-1712`), `costume` (`:1150-1151`) and `lexicon` (`:978-980`) return exit 2 with a message.

### D8 (medium) Packet-controlled regex can hang the naming gate — `naming-collision-gate.py:1279-1288`
`formation.pattern` is compiled with `re.fullmatch` and only `re.error` is caught.
Payload: rule `pattern: "^(?P<stem>(a+)+)$"`, `stem: aaaa…b` (40 `a` + `b`) — the subprocess was
still running at a 15 s wall bound and was killed (`rc=TIMEOUT`). Unbounded CPU from a packet a
collaborator or another lane can author; no timeout or complexity screen exists.

### D9 (low, hardening) `formation.output` is a packet-controlled `str.format` template that reaches into objects — `:1300-1324`
`output.format(**match.groupdict())` with `output: "{stem.__class__}"` produced
`… yields "<class 'str'>" …` in the finding text. No code execution is possible
(`str.format` has no call syntax), but interpreter internals are reachable from packet text and are
echoed into the report; `{stem.__class__.__mro__}`-style templates are accepted packets.

### D10 (note, not a defect) Coverage gap in the registered battery
The divergences above are invisible to the selftests that the wave's operability claim runs:
`phonology-sanity-gate.py:1161-1217` (CONTROL_CASES) has **no** unterminated-flow, duplicate-key,
anchor/tag, or boolean-coercion case (only the indent case at `:1255`);
`naming-collision-gate.py:1610-1615` covers unterminated flow and tabs **for itself only**;
`myth-consistency-gate.py` has no selftest case for its duplicate-key check;
no gate has a cross-gate conformance fixture. Green battery ⇒ parser controls untested.

## 4. Reproduce

```bash
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
python3 - <<'PY'
import os, subprocess, sys, tempfile
REPO=os.getcwd()
G={"phonology":"tools/gates/phonology-sanity-gate.py","naming":"tools/gates/naming-collision-gate.py",
   "myth":"tools/gates/myth-consistency-gate.py","costume":"tools/gates/costume-era-consistency-gate.py",
   "lexicon":"tools/gates/lexicon-coverage-audit.py"}
def run(gate, text, timeout=20):
    with tempfile.TemporaryDirectory() as d:            # auto-cleaned, nothing under the repo
        p=os.path.join(d,"p.yml"); open(p,"w",encoding="utf-8").write(text)
        try:
            r=subprocess.run([sys.executable,os.path.join(REPO,G[gate]),p],
                             capture_output=True,text=True,timeout=timeout)
            return r.returncode,(r.stdout or r.stderr).strip().splitlines()[:2]
        except subprocess.TimeoutExpired: return "TIMEOUT",[]
UNTERM="name: t\nphonology:\n  consonants: [p, t, k\n  vowels: [a, e, i]\n  phonotactics: (C)V\n  tones: 0\n"
DUP=("name: t\nphonology:\n  consonants: [p, t, k, m, n, s, l]\n  vowels: [a, e, i, o, u]\n"
     "  phonotactics: (C)V(C)\n  tones: 0\nphonology:\n  consonants: [p, t, k, m, n, s, l, q\u02bc]\n"
     "  vowels: [a, e, i, o, u]\n  phonotactics: (C)V(C)\n  tones: 0\n")
TAB="name: t\nphonology:\n\tconsonants: [p, t, k, m, n, s, l]\n\tvowels: [a, e, i, o, u]\n\tphonotactics: (C)V(C)\n\ttones: 0\n\tnotable_rules:\n\t  - \"t \u2192 ts / _i\"\n"
for label,payload in (("unterminated-flow",UNTERM),("duplicate-key",DUP),("tab-indent",TAB)):
    for g in G: print("%-17s %-9s rc=%-3s %s" % (label,g,*run(g,payload)))
deep="name: d\nphonology:\n  consonants: ["+"["*3000+"]"*3000+"\n  vowels: [a]\n  phonotactics: (C)V\n  tones: 0\n"
for g in ("phonology","naming"): print("deep-nesting",g,run(g,deep)[0])
print("redos naming", run("naming","name: R\nphonology: {consonants: [p, t, k, m, n, s, l], vowels: [a, e, i, o, u], phonotactics: \"(C)V(C)\", tones: 0}\nmorphology:\n  derivation_rules:\n    - {id: R1, kind: suffix, affix: -x, pattern: \"^(?P<stem>(a+)+)$\", output: \"{stem}x\"}\nnames:\n  - {name: x, id: N1, type: person, formation: {stem: "+"a"*40+"b, rule: R1}}\n", timeout=10)[0])
PY
```
Expected: the `rc` column matches §2 for phonology / naming / myth / lexicon (the first printed
finding differs from the §2 cells because the snippet's payloads are minimal; costume returns 2 here
only because this minimal packet declares no `costumes` — its §2 cell used a complete costume packet);
`deep-nesting` rc=1 after a `RecursionError` traceback; `redos naming` `TIMEOUT` (the 10 s bound kills
the child).

## 5. Limits

- Only the five packet gates were probed; `handoff-packet-check.py` / `provenance-audit.py`
  (markdown inputs) and stdin (`-`) paths were not.
- The ReDoS result is a 15 s wall-bound observation, not a complexity proof; other patterns may be worse.
- No source texts or external claims are involved in this review; every statement above is tied to a
  command result or a line-cited local file.
- I did not re-run any `--selftest`: `phonology-sanity-gate.py --selftest` and
  `lexicon-coverage-audit.py --selftest` rewrite fixture files, which is outside this role's write scope.
- Concurrent workers modified `tools/assemble-d2.py`, `corpus/`, and `examples/` during my run;
  the five gate scripts were confirmed byte-identical to `fe34faa` at test time and their hashes are
  pinned in §0 above.

## 6. Recommended moves (for the parent to route; not applied here)

1. `phonology-sanity-gate.py:325-330` — reject unbalanced flow starts (mirror `naming:335-339`); one-line change.
2. All loaders — reject duplicate keys uniformly in block and flow mappings, and on the JSON path
   (`object_pairs_hook`); this is the highest-value single control.
3. Reject `&`, `*`, `!` at scalar start with exit 2, honoring the naming gate's declared subset policy.
4. Catch `RecursionError` and `UnicodeDecodeError` at the CLI boundary in phonology and myth → exit 2 `G-DATA`
   (add a depth cap for flow nesting).
5. Preserve raw authored text for form-bearing fields (`names[].name`, `lexicon[].term`, inventory tokens)
   so booleans/numbers are never re-rendered as forms.
6. Screen or time-bound `formation.pattern` matching in `_gate_c`.
7. Add one shared conformance fixture (these payloads) executed against all five gates, so the
   operability claim covers a cross-gate input contract instead of per-gate selftests only.
