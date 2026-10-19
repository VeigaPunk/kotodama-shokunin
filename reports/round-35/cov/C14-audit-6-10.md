- Seat: C14 | verifier | claim C | date 2026-10-19 | baseline 4a7aede

# C14 — second independent entry auditor: entries 6-10 (claim C)

Assignment (verbatim, `reports/round-35/targets.json` seat `C14`): "Audit entries
6-10 against the runbook; second independent auditor." Out: `cov/C14-audit-6-10.md`.

**Status: the audit itself is owed — its two inputs are unlanded.** At the time of
this fragment (single 64-seat wave, nothing else in `reports/round-35/` but
`claims.json`, `targets.json`, `telemetry/`) there are **no** entry drafts and no
runbook to audit them against:

- `reports/round-35/cov/C06-entry-6.md` … `C10-entry-10.md` (the ten drafts; entries
  6-10 are the five this seat audits) — absent.
- `reports/round-35/cov/C12-audit-runbook.md` (the runbook this seat audits
  *against*) — absent.

Per the missing-dependency rule this seat did every part that does not need those
bytes: it built and calibrated the audit instrument, pinned the audit contract to
filed lane conventions, established the false-positive baselines for both target
partitions, and pre-filled the audit slots so the integrator can complete the pass
with one command. Everything below is measured, cited, and re-runnable.

## 1. Findings for the runbook (each pinned to filed bytes)

### C14-F1 — `scope:` is declared in claim C but exists nowhere in the corpus

Claim C's `after_required` names the frontmatter vector as "(source / verified-at /
recheck / scope)". Measured: **0 of 201** corpus entries carry a `- scope:` field.

```
$ for k in topic sources couples verified-at recheck scope status; do printf "%-12s " "$k"; grep -l "^- $k:" corpus/knowledge/*/*.md | wc -l; done
topic        201
sources      201
couples      201
verified-at  201
recheck      201
scope        0
status       0
```

Only two files mention `scope:` at all, and both are prose examples of a *proposed*
header form, not fields:
`corpus/knowledge/verification/to-verify-triage-protocol.md:164` and
`corpus/knowledge/verification/header-conformance-readings.md:75`.

The lane's own last runner with entry legs reads the five-field vector and no
`scope`: `reports/round-10/run-validation.py:81`
`C_FRONTMATTER_FIELDS = ("topic", "sources", "verified-at", "recheck", "couples")`.
**Ask of the runbook (C12):** either drop `scope` from the audited vector, or define
it as a new requirement and state explicitly that it is a *new* class (it cannot be
the 3/4-class escape hatch — a 3/4 class presupposes a 4-field vector, and under the
literal four-field reading `source/verified-at/recheck/scope` **every one of the 201
existing entries fails**, since none has `scope`). This seat does not disposition it;
it is named so the audit is not silently run against two different contracts.

### C14-F2 — the strict legs are a *style generation*, not the partition status quo

The round-10 runner's entry legs (`reports/round-10/run-validation.py:363` gap field,
`:365` gap heading, `:368` decision-record heading, `:110-111` URL/repo-path
locators) read as follows on the 37 live entries of the two target partitions:

| leg | live reading | note |
|---|---|---|
| frontmatter (5-field, `source`\|`sources`) | 37/37 | clean |
| gap (r10 forms) | **5/37** | 32 entries name no gap in any r10-recognized form |
| decision record (r10 heading form) | **5/37** | |
| ≥1 resolving locator | **11/37** | bibliography-prose sources carry neither URL nor repo path |
| `couples:` targets resolve | 37/37 | 306 refs: 302 path-resolved + 4 basename shorthand, 0 unresolved |
| no-bleed (r34 predicate) | 37/37 | |

The five entries that clear all strict legs together are **exactly the five
round-10-era entries** (`git log -1` on each → `94ca098 round-10: admit C/F/O`):
`transport-mobility-lexicon.md`, `vessel-container-lexicon.md`,
`direction-symbolism.md`, `divination-omen-systems.md`, `plant-symbolism.md`. The
other 32 predate that style. Widest possible reading (`grep -ic gap` > 0) is 12/37 —
so even a generous prose reading does not make the strict legs describe the status
quo.

**Consequence for the audit of entries 6-10:** a draft that names its gap only in
prose will fail the round's own counting command, exactly as round-10's F1 caught
(`reports/round-10/coverage/audit-myth-culture.md` §5: two entries "fail the declared
counting command's per-entry legs" while stating their gaps in substance). The
runbook should therefore **mandate the r10-recognizable forms for all ten drafts** —
a `- gap:` field (the form the two repaired round-10 entries carry:
`corpus/knowledge/myth-symbol/plant-symbolism.md:3`,
`corpus/knowledge/culture-material/transport-mobility-lexicon.md:3`) and a
`## … Decision record` heading — so the audit, the runner, and the substance agree
instead of measuring three different things.

### C14-F3 — the round-19 audit instrument is miscalibrated for these partitions

The lane's only filed per-entry auditor (`reports/round-19/audit/entry-audit.py`,
sha256 `e7992c325a479aa7415c42722a034a95a9ea342a58367ead9cd2636a5a62830c`) reads
**2/37** on the two target partitions, and two of its legs are unusable there:

- its `source_locators()` only counts `  - ` sub-bullets under `- sources:`; 14 of the
  37 entries carry a single-line `- sources:` block → `src=0/0` (false failure);
- its `GAP_RE`/`DECISION_RE` vocabularies match neither partition's gap/decision
  prose (false failures on 32 and 32 of 37).

It also derives its repo root as `dirname(__file__)/../../..`, so it only reads
correctly from its filed location: a copy placed in `.scratch/` resolves the root to
`…/Projects/shokunin` and reports **every** `couples:` ref unresolved (1/37 pass,
observed this run at `.scratch/C14-entry-audit-r19.py`, before the copy was moved to
`.scratch/c14run/x/` to restore the depth and the same command then read 2/37). Both
numbers are recorded here so a later reader does not mistake either for a corpus
defect.

### C14-F4 — the v2 instrument reproduces two filed defects (independent validation)

Running the instrument below over all 201 entries (`--live` all six partitions):

- `couples:` 2174 refs → 2018 path-resolved, 148 basename-shorthand, **0 ambiguous,
  8 unresolved / 7 distinct names**, including `../linguistics/phonology-sanity.md`
  (×2). That is exactly finding **X26-1** of `reports/round-19/audit/x26-spotcheck-entries.md`
  §3 ("phantom `couples:` path `../linguistics/phonology-sanity.md` … **That file does
  not exist**"), independently re-derived here — and it is still unfixed in the live
  tree.
- frontmatter 198/201, the three failures being
  `verification/citation-format-and-source-registry.md`,
  `verification/myth-consistency-gate.md`,
  `verification/provenance-audit-ledger-format.md` — byte-for-byte the same
  "B-remainder" three files round-10's audit reported (`reports/round-10/coverage/audit-myth-culture.md`
  §2.4), i.e. the same pre-existing, documented open question and not new debt.
- no-bleed 198/201 (3 candidate lines; two are ordinary language — a `[V]` table
  marker in `synthesis/worked-example-mini-culture.md:61` and "canonical learning" in
  `civilizations/burma.md:40` — and one is a `- recheck:` sentence about promoting a
  *finding into a repair*, `verification/internal-consistency-audit.md:7`; none is a
  promotion/clearance claim). The two target partitions are **0 bleed hits**.

Because the instrument independently reproduces two filed findings, its legs are
calibrated against known ground truth rather than self-asserted.

## 2. Instrument (draft bytes for the integrator)

Target path: `reports/round-35/cov/audit-v2.py`. Read-only; writes nothing in-tree.
It audits **landed entries** and, crucially for this round, the **pre-landing fenced
draft blocks** in the C06–C10 fragments, so the ten entries can be checked *before*
the integrator writes them into `corpus/knowledge/`.

```python
#!/usr/bin/env python3
"""C14 — round-35 entry audit instrument v2 (read-only).

Audits corpus entries AND pre-landing draft blocks against the round-35 claim-C
contract: frontmatter completeness, resolving source pointers, decision record,
named gap, no cross-domain bleed. Reports the runner-compatible legs (round-10
`entry_checks` forms, the lane's last runner with entry legs) SEPARATELY from the
loose in-file forms, so a substance pass is never confused with a leg pass.

Usage:
    python3 audit-v2.py --live culture-material myth-symbol
    python3 audit-v2.py --drafts reports/round-35/cov/C06-entry-6.md ...
    python3 audit-v2.py --since <rev>
    python3 audit-v2.py --selftest
Exit: 0 all clear, 2 some entry fails the bar, 1 usage error.
"""
import argparse
import glob
import hashlib
import json
import os
import re
import subprocess
import sys

try:
    LANE = subprocess.run(["git", "rev-parse", "--show-toplevel"],
                          capture_output=True, text=True, check=True).stdout.strip()
except Exception:
    LANE = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                        "..", "..", ".."))
KNOWLEDGE = os.path.join(LANE, "corpus", "knowledge")

# --- lane conventions (round-10 run-validation.py:81, :363, :365, :368; round-34:283-288) ---
FM_FIELDS = ("topic", "sources", "verified-at", "recheck", "couples")
GAP_FIELD = re.compile(r"(?i)(?:^|[\s.;—–|-])gap(?:[\s-]+(?:filled|addressed|served))?\s*:\s*(\S[^\n]{0,300})")
GAP_HEADING = re.compile(r"(?mi)^#{2,4}[^\n]*\bgap\b[^\n]*\n(?:[^\n]*\n)*?[^\n\s][^\n]*$")
GAP_LOOSE = re.compile(r"(?i)(the gap this entry fills|gap filled|named gap|residual gap|"
                       r"absent from the partition|no entry (?:covers|states)|not covered by|"
                       r"fills? (?:that|this|the) gap)")
DEC_STRICT = re.compile(r"(?mi)^#{2,4}[^\n]*decision[- ]record[^\n]*\n+\s*(\S[^\n]*)")
DEC_LOOSE = re.compile(r"(?i)(decision record|decision table|DR-[A-Z]{2}-\d)")
SRC_PATH = re.compile(r"\b((?:corpus|tools|reports|examples)/[\w./-]+\.(?:md|json|py|yml|yaml|tsv|txt))\b")
URL = re.compile(r"https?://[^\s`)\]]+")
DIGEST = re.compile(r"\b[0-9a-f]{16,64}\b")
MDREF = re.compile(r"[A-Za-z0-9_./{},\-]+\.md")
LANG_TOKENS = re.compile(r"(?i)\b(promot\w*|canon\w*|clearance|closure|verified)\b")
LANG_ALLOW = re.compile(r"(?i)(no |none |not |never |remains? the operator|operator-owned|"
                        r"routed|owed|absorbed|without |non-|negation|not a)")
LANG_FRAME = re.compile(r"(?i)(is|are|was|were|being) (promoted|canonized|cleared|granted)\w*|"
                        r"promotion (is )?(granted|complete|approved)|boxes? (all )?(pass|satisf)|"
                        r"checklist (all )?pass|canon standing (is )?(granted|given|conferred)|"
                        r"closure (is )?(granted|complete|decided)|verdict:\s*(pass|admitted|promoted|granted)|"
                        r"\[(x|v)\]\s|verified by (the )?(lane|seat|self)\b|unconditional")
NEG = re.compile(r"(?i)\b(no|not|never|without|non-|outside|belongs? to|routed to|owned by)\b")

FIELD_RE = re.compile(r"^- ([a-z-]+):", re.M)


def read(path):
    with open(path, "rb") as fh:
        raw = fh.read()
    return raw, raw.decode("utf-8", "replace")


def frontmatter_block(text):
    """The opening key block: consecutive `- key:` lines with their continuations."""
    lines = text.splitlines()
    start = None
    end = len(lines)
    for i, line in enumerate(lines):
        if re.match(r"^- [a-z-]+:", line):
            if start is None:
                start = i
        elif start is not None and line.startswith("## "):
            end = i
            break
    if start is None:
        return ""
    return "\n".join(lines[start:end])


def fields_of(block):
    out = {}
    lines = block.splitlines()
    cur = None
    for line in lines:
        m = FIELD_RE.match(line)
        if m:
            cur = m.group(1)
            out[cur] = [line.split(":", 1)[1].strip()]
        elif cur and line.strip():
            out[cur].append(line.strip())
    return {k: "\n".join(v) for k, v in out.items()}


def expand_braces(s):
    m = re.search(r"\{([^{}]*)\}", s)
    if not m:
        return [s]
    out = []
    for part in m.group(1).split(","):
        out.extend(expand_braces(s[: m.start()] + part + s[m.end():]))
    return out


_BASENAME_INDEX = None


def basename_index():
    """basename -> [repo-relative paths] over corpus/knowledge (one walk, cached)."""
    global _BASENAME_INDEX
    if _BASENAME_INDEX is None:
        idx = {}
        for p in glob.glob(os.path.join(KNOWLEDGE, "*", "*.md")):
            idx.setdefault(os.path.basename(p), []).append(os.path.relpath(p, LANE))
        _BASENAME_INDEX = idx
    return _BASENAME_INDEX


def couples_refs(text, path):
    block = frontmatter_block(text)
    fm = fields_of(block)
    val = fm.get("couples", "")
    refs = set()
    for raw in MDREF.findall(val):
        for c in expand_braces(raw):
            refs.add(c.strip())
    resolved, shorthand, ambiguous, unresolved = [], [], [], []
    base = os.path.dirname(os.path.abspath(path)) if path else LANE
    idx = basename_index()
    for ref in sorted(refs):
        cands = [os.path.normpath(os.path.join(base, ref)),
                 os.path.normpath(os.path.join(LANE, ref)),
                 os.path.normpath(os.path.join(KNOWLEDGE, ref))]
        if any(os.path.isfile(c) for c in cands):
            resolved.append(ref)
            continue
        hits = idx.get(os.path.basename(ref), [])
        if len(hits) == 1:
            shorthand.append(f"{ref} -> {hits[0]}")
        elif len(hits) > 1:
            ambiguous.append(f"{ref} -> {len(hits)} candidates")
        else:
            unresolved.append(ref)
    return resolved, shorthand, ambiguous, unresolved


def source_locators(text):
    """Locator legs over the whole entry: repo paths that resolve, URLs, digests."""
    paths = [p for p in dict.fromkeys(SRC_PATH.findall(text))
             if os.path.exists(os.path.join(LANE, p))]
    dead = [p for p in dict.fromkeys(SRC_PATH.findall(text))
            if not os.path.exists(os.path.join(LANE, p))]
    urls = list(dict.fromkeys(URL.findall(text)))
    digs = list(dict.fromkeys(DIGEST.findall(text)))
    return {"repo_paths_resolving": paths, "repo_paths_dead": dead,
            "urls": urls, "digests": digs,
            "n_locators": len(paths) + len(urls) + len(digs)}


def bleed_hits(text):
    """The lane's operative no-bleed predicate (round-34 run-validation.py:305-306):
    token AND affirmative frame AND not negated/allowed."""
    hits = []
    for n, line in enumerate(text.splitlines(), 1):
        if LANG_TOKENS.search(line) and LANG_FRAME.search(line) and not LANG_ALLOW.search(line):
            hits.append((n, line.strip()[:160]))
    return hits


def audit_text(text, label, path=None):
    block = frontmatter_block(text)
    fm = fields_of(block)
    missing = [f for f in FM_FIELDS
               if f not in fm and not (f == "sources" and "source" in fm)]
    src = source_locators(text)
    resolved, shorthand, ambiguous, unresolved = couples_refs(text, path)
    rep = {
        "label": label,
        "sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(),
        "frontmatter_fields": sorted(fm),
        "frontmatter_missing": missing,
        "declared_scope_field": "scope" in fm,
        "gap_leg_r10": bool(GAP_FIELD.search(text) or GAP_HEADING.search(text)),
        "gap_in_file_loose": bool(GAP_FIELD.search(text) or GAP_HEADING.search(text)
                                  or GAP_LOOSE.search(text)),
        "decision_leg_r10": bool(DEC_STRICT.search(text)),
        "decision_in_file_loose": bool(DEC_LOOSE.search(text)),
        "couples_refs": len(resolved) + len(shorthand) + len(ambiguous) + len(unresolved),
        "couples_resolved": len(resolved),
        "couples_resolved_shorthand": shorthand,
        "couples_ambiguous": ambiguous,
        "couples_unresolved": unresolved,
        "locators": src,
        "bleed_hits": bleed_hits(text),
    }
    rep["bar_pass"] = (not missing and not unresolved
                       and rep["gap_leg_r10"] and rep["decision_leg_r10"]
                       and src["n_locators"] >= 1 and not rep["bleed_hits"])
    return rep


def live_paths(partitions):
    out = []
    for part in partitions:
        out.extend(sorted(glob.glob(os.path.join(KNOWLEDGE, part, "*.md"))))
    return out


def git_new_entries(rev):
    names = subprocess.run(["git", "diff", "--name-only", rev, "--", "corpus/knowledge"],
                           cwd=LANE, capture_output=True, text=True, check=True).stdout
    untracked = subprocess.run(["git", "ls-files", "--others", "--exclude-standard",
                                "--", "corpus/knowledge"],
                               cwd=LANE, capture_output=True, text=True, check=True).stdout
    files = {f for f in (names + "\n" + untracked).splitlines() if f.endswith(".md")}
    return [os.path.join(LANE, f) for f in sorted(files)
            if os.path.isfile(os.path.join(LANE, f))]


FENCE = re.compile(r"^(?P<fence>[`~]{3,})(?P<rest>[^\n]*)\n(?P<body>.*?)^(?P=fence)[ \t]*$",
                   re.M | re.S)


def draft_blocks(path):
    """Entry drafts carried as fenced blocks in a seat fragment."""
    _, text = read(path)
    blocks = []
    for m in FENCE.finditer(text):
        body = m.group("body")
        if not re.search(r"(?m)^- topic:", body):
            continue
        info = (m.group("rest") or "").strip()
        target = None
        tm = re.search(r"(corpus/knowledge/[\w./-]+\.md)", info)
        if tm:
            target = tm.group(1)
        else:
            tm = re.search(r"<!--\s*(?:target|file)\s*:\s*(corpus/knowledge/[\w./-]+\.md)\s*-->",
                           text[: m.start()])
            if tm:
                target = tm.group(1)
        title = re.search(r"(?m)^#\s+(.+)$", body)
        blocks.append({"fragment": os.path.relpath(path, LANE), "target": target,
                       "title": title.group(1).strip() if title else None,
                       "body": body})
    return blocks


def selftest():
    import tempfile
    ok = True

    def check(name, cond, detail=""):
        nonlocal ok
        if not cond:
            ok = False
        print(("PASS " if cond else "FAIL ") + name + (" " + detail if detail else ""))

    good = (
        "# Test Entry — a gap filler\n\n"
        "- gap: the register this partition lacks — this entry fills it\n"
        "- topic: the thing this entry covers — the gap this entry fills\n"
        "- sources:\n  - Author (2001), *Book*, Pub. https://e.org/x\n"
        "- couples: culture-material/era-periodization-models.md\n"
        "- verified-at: 2026-10-19 — checked\n- recheck: before printing\n\n"
        "## 1. Frame\n\n## 9. Decision record — the decisions this entry fixes\n\n"
        "1. pick a column.\n"
    )
    r = audit_text(good, "good")
    check("good entry clears the bar", r["bar_pass"] is True, json.dumps(r["couples_unresolved"]))
    check("good: fm complete", r["frontmatter_missing"] == [])
    check("good: gap leg r10", r["gap_leg_r10"] is True)
    check("good: decision leg r10", r["decision_leg_r10"] is True)
    check("good: locator resolves", r["locators"]["n_locators"] >= 1)
    check("good: couples resolve", r["couples_unresolved"] == [])

    bad = good.replace("- couples: culture-material/era-periodization-models.md",
                       "- couples: culture-material/phantom-file.md")
    r2 = audit_text(bad, "bad-couples")
    check("negative control: phantom couples caught", r2["bar_pass"] is False
          and r2["couples_unresolved"] == ["culture-material/phantom-file.md"], str(r2["couples_unresolved"]))

    r3 = audit_text(good.replace("## 9. Decision record — the decisions this entry fixes",
                                 "## 9. Notes"), "bad-decision")
    check("negative control: missing decision heading caught", r3["bar_pass"] is False
          and r3["decision_in_file_loose"] is False)

    r4 = audit_text(good.replace("- recheck: before printing", ""), "bad-fm")
    check("negative control: missing frontmatter field caught", r4["bar_pass"] is False
          and "recheck" in r4["frontmatter_missing"])

    r5 = audit_text(good + "\nthe promotion checklist passes\n", "bleed")
    check("negative control: affirmative bleed caught", r5["bar_pass"] is False
          and r5["bleed_hits"], str(r5["bleed_hits"]))
    r6 = audit_text(good + "\nno promotion decision is taken here\n", "negated")
    check("negation allowed", r6["bleed_hits"] == [])

    # multi-line couples block (the shape the r19 instrument mis-parsed)
    multi = good.replace("- couples: culture-material/era-periodization-models.md",
                         "- couples: culture-material/era-periodization-models.md;\n"
                         "  culture-material/costume-semiotics.md;\n"
                         "  corpus/knowledge/linguistics/color-terminology.md")
    r7 = audit_text(multi, "multi-couples")
    check("multi-line couples parsed", r7["couples_refs"] == 3 and r7["couples_unresolved"] == [],
          f"refs={r7['couples_refs']} un={r7['couples_unresolved']}")

    # draft-block extraction + target inference
    d = tempfile.mkdtemp()
    frag = os.path.join(d, "C99-entry.md")
    with open(frag, "w", encoding="utf-8") as fh:
        fh.write("<!-- target: corpus/knowledge/culture-material/zz-test.md -->\n"
                 "```markdown\n" + good + "```\n")
    blocks = draft_blocks(frag)
    check("draft block extracted", len(blocks) == 1 and blocks[0]["target"]
          == "corpus/knowledge/culture-material/zz-test.md", str(blocks[:1]))
    return ok


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", nargs="*", default=None)
    ap.add_argument("--drafts", nargs="*", default=None)
    ap.add_argument("--since")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args(argv)
    if args.selftest:
        return 0 if selftest() else 1
    reps = []
    if args.live is not None:
        parts = args.live or ["culture-material", "myth-symbol"]
        for p in live_paths(parts):
            _, text = read(p)
            reps.append(audit_text(text, os.path.relpath(p, LANE), p))
    if args.since:
        for p in git_new_entries(args.since):
            _, text = read(p)
            reps.append(audit_text(text, os.path.relpath(p, LANE), p))
    if args.drafts:
        for frag in args.drafts:
            if not os.path.isfile(os.path.join(LANE, frag)):
                print(f"OWED {frag} (draft fragment not landed)", file=sys.stderr)
                continue
            for b in draft_blocks(os.path.join(LANE, frag)):
                reps.append(audit_text(b["body"], f"{b['fragment']}::{b['target'] or 'target-unknown'}"))
    if not reps:
        print("nothing to audit", file=sys.stderr)
        return 1
    npass = sum(1 for r in reps if r["bar_pass"])
    if args.json:
        print(json.dumps({"schema": "kotodama-entry-audit-v2", "entries": reps,
                          "summary": {"total": len(reps), "pass": npass}}, indent=2))
    else:
        for r in reps:
            print(f"{'PASS' if r['bar_pass'] else 'FAIL'} {r['label']} "
                  f"fm_missing={r['frontmatter_missing']} gap_r10={r['gap_leg_r10']} "
                  f"gap_loose={r['gap_in_file_loose']} dec_r10={r['decision_leg_r10']} "
                  f"dec_loose={r['decision_in_file_loose']} "
                  f"couples={r['couples_resolved']}/{r['couples_refs']} "
                  f"unresolved={r['couples_unresolved']} "
                  f"locators={r['locators']['n_locators']} dead={r['locators']['repo_paths_dead']} "
                  f"bleed={len(r['bleed_hits'])}")
        print(f"TOTAL {npass}/{len(reps)} clear the bar")
    return 0 if npass == len(reps) else 2


if __name__ == "__main__":
    sys.exit(main())
```

Draft-block convention the instrument reads (so authors can make their drafts
auditable without a second format): either a fence info string naming the target
(```` ```markdown corpus/knowledge/culture-material/<slug>.md ````) or a
`<!-- target: corpus/knowledge/<partition>/<slug>.md -->` marker immediately above
the fence. Without one, the block is still audited but reports `target-unknown`
(so a cross-reference to a sibling draft cannot be resolved — see §4).

## 3. Calibration evidence (re-runnable)

```
$ export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
$ python3 -B reports/round-35/cov/audit-v2.py --selftest
PASS good entry clears the bar []
PASS good: fm complete
PASS good: gap leg r10
PASS good: decision leg r10
PASS good: locator resolves
PASS good: couples resolve
PASS negative control: phantom couples caught ['culture-material/phantom-file.md']
PASS negative control: missing decision heading caught
PASS negative control: missing frontmatter field caught
PASS negative control: affirmative bleed caught [(17, 'the promotion checklist passes')]
PASS negation allowed
PASS multi-line couples parsed refs=3 un=[]
PASS draft block extracted [{'fragment': '.../C99-entry.md', 'target': 'corpus/knowledge/culture-material/zz-test.md', ...}]
selftest_exit=0        # 13/13, four of them negative controls
```

Baseline readings on the delivered revision (baseline `4a7aede`, working tree
unchanged in `corpus/` — `git status --porcelain` at this seat's start showed only
`?? reports/round-35/`):

| surface | command | reading |
|---|---|---|
| census (claim C `before`) | `for p in linguistics myth-symbol culture-material synthesis verification civilizations; do ls corpus/knowledge/$p/*.md \| wc -l; done` | 21/19/18/29/20/94 = **201** — matches `reports/round-35/claims.json` C.before exactly |
| inventory (claim C counting cmd 2) | `python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge` | `totals.files 201`, `files_with_any_mark 147`, `lines 36395`, exit 0 |
| two target partitions | `audit-v2.py --live culture-material myth-symbol` | 5/37 clear the strict bar; fm 37/37; couples 306 refs → 0 unresolved; bleed 0; locators≥1 11/37 |
| whole corpus | `audit-v2.py --live linguistics myth-symbol culture-material synthesis verification civilizations` | 20/201 clear the strict bar; fm 198/201; couples 2174 refs → 8 unresolved (X26-1 phantom reproduced); bleed 198/201 |

Raw JSON for both live runs is reproduced by the two commands above (this seat's
copies were `.scratch/C14/live37.json`, `.scratch/C14/live201.json`; scratch is
disposable, the commands are the durable evidence).

## 4. The audit of entries 6-10 — slots ready, one command to complete

This seat's five audited entries are **6-10**, i.e. the drafts of seats C06–C10
(C06 = culture-material, C07–C10 = myth-symbol per `reports/round-35/targets.json`).
Completion command, once the drafts and the runbook land:

```
$ export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
$ python3 -B reports/round-35/cov/audit-v2.py --drafts \
    reports/round-35/cov/C06-entry-6.md reports/round-35/cov/C07-entry-7.md \
    reports/round-35/cov/C08-entry-8.md reports/round-35/cov/C09-entry-9.md \
    reports/round-35/cov/C10-entry-10.md --json
```

Observed **now** (owed-detection path exercised, so the integrator sees the failure
mode rather than a traceback):

```
OWED reports/round-35/cov/C06-entry-6.md (draft fragment not landed)
OWED reports/round-35/cov/C07-entry-7.md (draft fragment not landed)
OWED reports/round-35/cov/C08-entry-8.md (draft fragment not landed)
OWED reports/round-35/cov/C09-entry-9.md (draft fragment not landed)
OWED reports/round-35/cov/C10-entry-10.md (draft fragment not landed)
nothing to audit
exit=1
```

Audit slots (to be filled by whoever runs the completion command; the check list is
the runbook's substance, made mechanical):

| draft | target slug | fm 5/5 | gap r10 | dec r10 | couples resolve | locators≥1 | bleed 0 | bar |
|---|---|---|---|---|---|---|---|---|
| C06-entry-6 | (culture-material, from P01) | — | — | — | — | — | — | — |
| C07-entry-7 | (myth-symbol, from P01) | — | — | — | — | — | — | — |
| C08-entry-8 | (myth-symbol, from P01) | — | — | — | — | — | — | — |
| C09-entry-9 | (myth-symbol, from P01) | — | — | — | — | — | — | — |
| C10-entry-10 | (myth-symbol, from P01) | — | — | — | — | — | — | — |

Two checks the instrument cannot make from draft bytes alone, and which the auditor
must add by reading (recorded here so the integrator does not read their absence as
a pass):

1. **Cross-draft `couples:`** — a draft coupling a sibling draft that is not yet in
   `corpus/knowledge/` will report `couples_unresolved` even when the reference is
   legitimate. Read the unresolved list against the other nine drafts' target slugs
   before filing it as a defect (the X26-1 class — `../linguistics/phonology-sanity.md`
   — is the *other* case: a ref that names no draft and no file).
2. **Source-pointer resolution** — offline, a pointer "resolves" only as a repo path,
   URL string, or digest; the instrument cannot fetch a URL (no network this round).
   Any URL-only source leg is therefore `to-verify` at the audit, and the audit must
   say so rather than implying it was checked. The 201-entry baseline shows the scale
   of that class: 175/201 entries carry at least one locator, of which URL legs are
   unfetched here.

## Owed

- `reports/round-35/cov/C06-entry-6.md` — draft entry 6 (dependency; absent at write time)
- `reports/round-35/cov/C07-entry-7.md` — draft entry 7 (dependency; absent at write time)
- `reports/round-35/cov/C08-entry-8.md` — draft entry 8 (dependency; absent at write time)
- `reports/round-35/cov/C09-entry-9.md` — draft entry 9 (dependency; absent at write time)
- `reports/round-35/cov/C10-entry-10.md` — draft entry 10 (dependency; absent at write time)
- `reports/round-35/cov/C12-audit-runbook.md` — the runbook this audit is specified
  against (dependency; absent at write time). Without it, §4's check list is this
  seat's reconstruction from the filed round-10 legs and `corpus/QUALITY.md`, not the
  runbook's own list; the integrator should diff the two and record any divergence.
- `reports/round-35/cov/audit-v2.py` — the instrument draft in §2 (this seat may
  write only its own fragment; the integrator lands the bytes)
- the five per-entry verdict rows in §4 — owed with the drafts

This seat could not audit bytes that do not exist; it did not substitute the live
partition for the drafts, and it admits no claim, edits no corpus byte, and absorbs
no sibling fragment's evidence.

## Citations

- `reports/round-35/targets.json` — seat `C14` (role verifier, claim C, out `cov/C14-audit-6-10.md`); `shared_rules[]`; seats C06–C10, C12 missions
- `reports/round-35/claims.json` — claim C (`before` census 201; `after_required` frontmatter vector incl. `scope`; thresholds "10/10 new entries audited clean (two independent auditors)")
- `REGIMEN.md` — per-round contract; the axis set and the 1-3 claims rule
- `corpus/QUALITY.md` — the admission bar (provenance / calibration / coupling / usability / canon hygiene)
- `reports/round-10/run-validation.py:81` (`C_FRONTMATTER_FIELDS`), `:110-111` (`URL_RE`, `REPO_PATH_RE`), `:349` (`entry_checks`), `:363` (`gap_field`), `:365` (`gap_heading`), `:368` (decision-record heading)
- `reports/round-10/coverage/audit-myth-culture.md` §2.4 (A/B/C source-leg readings; B-remainder three files), §3.3 (provenance gate 37 files / 0 findings), §5 (F1: two entries fail the runner's per-entry legs while naming gaps in prose)
- `reports/round-19/audit/entry-audit.py` — sha256 `e7992c325a479aa7415c42722a034a95a9ea342a58367ead9cd2636a5a62830c`; §C14-F3 readings (2/37; mis-derived root at the wrong depth)
- `reports/round-19/audit/x26-spotcheck-entries.md` §3 — X26-1 phantom `couples:` path `../linguistics/phonology-sanity.md`
- `reports/round-34/run-validation.py:283-288` (`LANG_TOKENS`/`LANG_ALLOW`/`LANG_FRAME`), `:305-306` (operative no-bleed predicate), `:458-459` (its two language controls)
- `corpus/knowledge/myth-symbol/plant-symbolism.md:3` and `corpus/knowledge/culture-material/transport-mobility-lexicon.md:3` — the `- gap:` field form
- `corpus/knowledge/verification/to-verify-triage-protocol.md:164`, `corpus/knowledge/verification/header-conformance-readings.md:75` — the only two `scope:` mentions in the corpus
- `corpus/README.md` — revision 1.9 (counts 21/19/18/29/20/94, totals line 201)
- commands: `for p in linguistics myth-symbol culture-material synthesis verification civilizations; do ls corpus/knowledge/$p/*.md | wc -l; done`; `python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge`; `python3 -B .scratch/C14/audit-v2.py --selftest|--live|--drafts`; `grep -l "^- scope:" corpus/knowledge/*/*.md | wc -l`; `git log --oneline -1 -- corpus/knowledge/<entry>`
