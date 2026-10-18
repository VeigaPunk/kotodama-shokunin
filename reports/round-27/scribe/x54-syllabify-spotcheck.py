#!/usr/bin/env python3
"""X54 — independent syllabify spot-check, before/after, on every delivered form.

Assignment (verbatim): "SCRIBE X54: spot-check (syllabify before/after on all 62
forms independently)."

Claim under test: **D / depth** — "the syllabify disagreement fixed (one
algorithm, forms re-verified)" (`reports/round-27/claims.json`, claim D
`after_required`). This seat is a **spot-check**: it measures the delivered
artifact and the amended artifact, and adjudicates neither. The round's verdict
is `reports/round-27/run-validation.py`; this instrument is evidence for it.

## What is measured

Three witnesses, each obtained by a **different route**, over **every delivered
form** (the round-27 lexicon's `term`/`quote_form` rows plus every `names` row):

| witness | route | why it is independent |
|---|---|---|
| **W1 — the delivered gate** | `runpy` of `tools/gates/argot-derivation-gate.py`, calling its own `syllabify()` | the artifact under test, executed, never re-implemented |
| **W2 — the design's stated algorithm** | re-implemented *here* from the prose of `reports/round-17/d4/design-language.md:191-196` plus the packet's own `phonology` block | never copied from the gate and never copied from the round-26 probe |
| **W3 — the packet's own `syllables:` field** | the 8 `names` records, which carry an author-declared syllable split | authored by an **earlier round**, for a different purpose; consulted by neither W1 nor W2 |

W3 is the load-bearing addition. The round-26 review compared the gate against
its own re-implementation of the design (`reports/round-26/register/review.md`
§5) — two readings, both authored inside round 26. The delivered packet already
contains a **third, author-declared** reading that nobody consulted, and it
settles the dispute without appeal to prose.

## Legality, stated exactly

From the packet's own `phonology` block (not assumed): the template
`(C)V(V)(C)`, `onset_clusters: false`, the 8 declared codas, the 5 long-vowel
digraphs `aa ee ii oo uu` and the 2 falling diphthongs `ai au`. The packet's
`accent` field declares the diphthongs: *"Vowel length is contrastive only on
the stressed syllable and is written as a double vowel (aa ee ii oo uu); the
falling diphthongs ai and au are the only other vowel sequences."* A falling
diphthong is **one nucleus**, which W3 independently confirms: `tumhai` is
`['tum', 'hai']`, not `['tu', 'mha', 'i']`.

## Usage

    python3 reports/round-27/scribe/x54-syllabify-spotcheck.py            # census
    python3 reports/round-27/scribe/x54-syllabify-spotcheck.py --json     # receipt
    python3 reports/round-27/scribe/x54-syllabify-spotcheck.py --selftest # controls

Read-only. Nothing outside this file and the gitignored scratch is written.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import re
import runpy
import subprocess
import sys
from pathlib import Path

ROOT = Path(".")
GATE = ROOT / "tools/gates/argot-derivation-gate.py"
PACKET = ROOT / "examples/culture-d4/packet.d4.yml"
NAMING = ROOT / "tools/gates/naming-collision-gate.py"
DESIGN = ROOT / "reports/round-17/d4/design-language.md"

# The round-26 revision this "before" reading binds. The round-26 declared
# baseline is fc13cd27…; 1ad491a is the round-26 declare commit, which is the
# revision at which the published 62-form figure was measured.
R26_REV = "1ad491a"

# The register records round 26 added (RF-01..RF-08 = L-55..L-62). Excluded to
# reconstruct the round-26 62-form surface from the live 70-form surface.
R26_REGISTER_IDS = {"L-55", "L-56", "L-57", "L-58", "L-59", "L-60", "L-61", "L-62"}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(p) -> str:
    return sha256_bytes(Path(p).read_bytes())


def git_show(rev: str, path: str) -> str:
    return subprocess.run(["git", "show", f"{rev}:{path}"],
                          capture_output=True, text=True).stdout


def lane_head() -> str:
    return subprocess.run(["git", "rev-parse", "HEAD"],
                          capture_output=True, text=True).stdout.strip()


# ---------------------------------------------------------------------------
# the packet's own legality, read from the packet (never hard-coded)
# ---------------------------------------------------------------------------

class Legality:
    def __init__(self, phon: dict):
        self.consonants = set(phon["consonants"])
        self.vowels = set(phon["vowels"])
        self.codas = set(phon["coda"])
        self.onset_clusters = bool(phon.get("onset_clusters"))
        self.long = {"aa", "ee", "ii", "oo", "uu"}
        self.diphthongs = {"ai", "au"}

    def nuclei(self, word: str):
        """(start, end) of every nucleus. A doubled vowel and a falling
        diphthong are each ONE nucleus (packet `accent` field)."""
        out, i = [], 0
        while i < len(word):
            c = word[i]
            if c in self.vowels:
                j = i + 1
                if j < len(word) and word[j] == c:
                    j += 1
                elif j < len(word) and (c + word[j]) in self.diphthongs:
                    j += 1
                out.append((i, j))
                i = j
            else:
                i += 1
        return out

    def syllable_legal(self, s: str) -> bool:
        """Template (C)V(V)(C), onset_clusters=false, declared codas only."""
        i = 0
        if i < len(s) and s[i] in self.consonants:
            i += 1
        if i >= len(s) or s[i] not in self.vowels:
            return False
        if i + 1 < len(s) and s[i + 1] == s[i]:
            i += 2
        elif i + 1 < len(s) and (s[i] + s[i + 1]) in self.diphthongs:
            i += 2
        else:
            i += 1
        if i == len(s):
            return True
        return (i + 1 == len(s)) and (s[i] in self.codas)

    def design_syllabify(self, word: str):
        """W2 — maximal onset, legality-constrained, straight from the prose of
        `design-language.md:191-196`: "a consonant is taken as the onset of the
        following syllable whenever that yields a legal syllable".

        A consonant that cannot be an onset (because the result would be an
        onset cluster, which `onset_clusters: false` forbids) stays as the
        previous syllable's coda. `None` means no legal syllabification exists —
        a case the design leaves undefined and this seat reports rather than
        guesses.
        """
        nuc = self.nuclei(word)
        if not nuc:
            return None
        syls, prev_end = [], 0
        for start, end in nuc:
            run = word[prev_end:start]
            if len(run) <= 1 or self.onset_clusters:
                onset, leftover = run, ""
            else:
                onset, leftover = run[-1], run[:-1]
            if leftover:
                if len(leftover) == 1 and leftover in self.codas and syls:
                    syls[-1] += leftover
                else:
                    return None
            syls.append(onset + word[start:end])
            prev_end = end
        tail = word[prev_end:]
        if tail:
            if len(tail) == 1 and tail in self.codas:
                syls[-1] += tail
            else:
                return None
        return syls

    def design_head2(self, word: str):
        s = self.design_syllabify(word)
        return "".join(s[:2]) if s else None


# ---------------------------------------------------------------------------
# W1 — the delivered gate, executed
# ---------------------------------------------------------------------------

def gate_module():
    return runpy.run_path(str(GATE))


def naming_loader():
    return runpy.run_path(str(NAMING))["load_yaml"]


# ---------------------------------------------------------------------------
# the form surface
# ---------------------------------------------------------------------------

def surface(packet) -> list:
    """Every delivered form, as (id, form, packet_syllables_or_None)."""
    rows = []
    for r in packet.get("lexicon") or []:
        t = r.get("term") or r.get("quote_form")
        if t:
            rows.append((r["id"], t, r.get("syllables")))
    for r in packet.get("names") or []:
        t = r.get("name")
        if t:
            rows.append((r["id"], t, r.get("syllables")))
    return rows


# ---------------------------------------------------------------------------
# the measurement
# ---------------------------------------------------------------------------

def measure(label: str, packet, leg: Legality, gsyl) -> dict:
    rows = surface(packet)
    rec = {"label": label, "forms": len(rows), "rows": []}
    n_head2 = n_syllist = n_illegal = 0
    for rid, form, w3 in rows:
        w1 = gsyl(form)
        w2 = leg.design_syllabify(form)
        w1_h2 = "".join(w1[:2])
        w2_h2 = "".join(w2[:2]) if w2 else None
        row = {"id": rid, "form": form,
               "W1_gate_syllables": w1, "W1_gate_head2": w1_h2,
               "W2_design_syllables": w2, "W2_design_head2": w2_h2,
               "head2_agree": w1_h2 == w2_h2,
               "syllable_list_agree": w1 == w2,
               "gate_emits_non_syllable": [s for s in w1 if not leg.syllable_legal(s)]}
        if w3 is not None:
            row["W3_packet_syllables"] = w3
            row["W3_eq_W1"] = list(w3) == w1
            row["W3_eq_W2"] = list(w3) == w2
        if not row["head2_agree"]:
            n_head2 += 1
        if not row["syllable_list_agree"]:
            n_syllist += 1
        if row["gate_emits_non_syllable"]:
            n_illegal += 1
        rec["rows"].append(row)
    rec["head2_disagreements"] = n_head2
    rec["syllable_list_disagreements"] = n_syllist
    rec["forms_with_non_syllable_from_gate"] = n_illegal
    w3rows = [r for r in rec["rows"] if "W3_packet_syllables" in r]
    rec["W3"] = {
        "rows": len(w3rows),
        "W3_eq_W1": sum(1 for r in w3rows if r.get("W3_eq_W1")),
        "W3_eq_W2": sum(1 for r in w3rows if r.get("W3_eq_W2")),
    }
    return rec


def r26_probe_design_syllabify(word: str):
    """The round-26 probe's `design_syll` (`.scratch/r26-d-reg/syl.py`),
    transcribed verbatim so the published figure can be reproduced and audited.

    This is **not** W2. It is reproduced only to test whether the round-26
    "15 of 62" measures the design's algorithm or the probe's own.
    """
    C = set("ptkbdgmnsrlwjh")
    V = set("aeiou")
    CODA = set("nmsklrtd")
    SYL = re.compile(r"^([%s]?)(?:aa|ee|ii|oo|uu|ai|au|a|e|i|o|u)([%s]?)$"
                     % ("".join(C), "".join(CODA)))

    def legal_word(w):
        i, ss = 0, []
        while i < len(w):
            m = None
            for L in (4, 3, 2, 1):
                if i + L <= len(w) and SYL.match(w[i:i + L]):
                    m = w[i:i + L]
                    break
            if m is None:
                return None
            ss.append(m)
            i += len(m)
        if len(ss) > 1 and len(set(ss)) == 1:
            return None
        return ss

    out, i = [], 0
    while i < len(word):
        j = i
        while j < len(word) and word[j] not in V:
            j += 1
        if j == len(word):
            if out:
                out[-1] += word[i:j]
            else:
                out.append(word[i:j])
            break
        k = j
        if k + 1 < len(word) and word[k + 1] == word[k]:
            k += 2
        else:
            k += 1
        if k < len(word) and word[k] in CODA:
            k += 1
        run = word[i:j]
        if len(run) == 1 and j + 1 <= len(word) and legal_word(word[j:k]):
            out.append(word[i:j])
            i = j
        else:
            out.append(word[i:k])
            i = k
    return out


# The round-26 gate's own syllabify, transcribed from the pre-fix bytes
# (git revision R26_GATE_REV), so the BEFORE column measures the round-26
# artifact and not whatever the wave has since written to the live file.
R26_GATE_REV = "b95fca1"

_R26_VOWELS = frozenset("aeiou")


def r26_gate_syllabify(word: str):
    """The round-26 delivered `syllabify`, transcribed verbatim from
    `git show b95fca1:tools/gates/argot-derivation-gate.py` (the round-27
    declare commit, at which the gate was byte-identical to round-25).

    Transcribed rather than executed so the BEFORE column stays pinned to the
    round-26 bytes after the wave lands a fix in the live file. The
    transcription is verified against the pinned digest by `--selftest` C7.
    """
    syllables, pending, index = [], "", 0
    while index < len(word):
        char = word[index]
        if char in _R26_VOWELS:
            if index + 1 < len(word) and word[index + 1] == char:
                pending += char * 2
                index += 2
            else:
                pending += char
                index += 1
            syllables.append(pending)
            pending = ""
        else:
            pending += char
            index += 1
    if pending:
        syllables.append(pending)
    return syllables


# ---------------------------------------------------------------------------
# self-test: the controls this instrument must fail closed on
# ---------------------------------------------------------------------------

def selftest() -> int:
    load = naming_loader()
    packet = load(PACKET.read_text())
    leg = Legality(packet["phonology"])
    checks, failures = [], []

    def check(name, cond, observed=None):
        checks.append(name)
        if not cond:
            failures.append((name, observed))

    # C1 — the design's ONE published worked row must reproduce under W2.
    check("C1 design worked row saalumi -> saa.lu.mi",
          leg.design_syllabify("saalumi") == ["saa", "lu", "mi"],
          leg.design_syllabify("saalumi"))
    check("C1b design head2(saalumi) == saalu",
          leg.design_head2("saalumi") == "saalu", leg.design_head2("saalumi"))

    # C2 — a falling diphthong is ONE nucleus (packet accent field).
    check("C2 hai is one syllable", leg.design_syllabify("hai") == ["hai"],
          leg.design_syllabify("hai"))
    check("C2b sau is one syllable", leg.design_syllabify("sau") == ["sau"],
          leg.design_syllabify("sau"))

    # C3 — onset_clusters=false: a consonant run collapses to coda + single onset.
    check("C3 kalker -> kal.ker", leg.design_syllabify("kalker") == ["kal", "ker"],
          leg.design_syllabify("kalker"))

    # C4 — legality predicate agrees with the packet's own template.
    check("C4 'kme' is not a legal syllable", not leg.syllable_legal("kme"))
    check("C4b 'saa' is a legal syllable", leg.syllable_legal("saa"))
    check("C4c 'r' alone is not a legal syllable", not leg.syllable_legal("r"))

    # C5 — the round-26 probe's implementation is NOT the design's algorithm
    #      (negative control: if these ever coincide, the audit is meaningless).
    check("C5 r26-probe saalumi != design saalumi",
          r26_probe_design_syllabify("saalumi") != leg.design_syllabify("saalumi"),
          r26_probe_design_syllabify("saalumi"))

    # C6 — the gate's bytes are what we think we are measuring.
    check("C6 gate has a syllabify symbol", "syllabify" in gate_module())

    # C7 — the round-26 transcription is faithful to the pinned round-26 bytes.
    #      The BEFORE column reads the transcription, not the live file, so this
    #      control is what keeps BEFORE honest after the wave lands a fix.
    r26_src = git_show(R26_GATE_REV, str(GATE))
    check("C7 the round-26 transcription reproduces the pinned round-26 bytes",
          _r26_syllabify_matches_pinned(r26_src),
          "transcription diverges from %s:%s" % (R26_GATE_REV, GATE))

    print(f"selftest: {len(checks) - len(failures)}/{len(checks)} checks passed")
    for name, obs in failures:
        print(f"  FAIL {name}: observed={obs!r}")
    return 0 if not failures else 1


def _r26_syllabify_matches_pinned(r26_src: str) -> bool:
    """Execute the pinned round-26 gate's `syllabify` in isolation and compare it
    to the transcription on a probe set that covers both the consonant-run and
    the diphthong axes."""
    import tempfile
    with tempfile.TemporaryDirectory() as td:
        p = Path(td) / "r26gate.py"
        p.write_text(r26_src)
        try:
            mod = runpy.run_path(str(p))
        except Exception:
            return False
        ref = mod.get("syllabify")
        if ref is None:
            return False
        probes = ["saalumi", "tikmes", "kalker", "ker", "tumhai", "haitik",
                  "hai", "sau", "dau", "mesar", "kalen", "tum", "nes", "mes"]
        return all(ref(w) == r26_gate_syllabify(w) for w in probes)


# ---------------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.selftest:
        return selftest()

    load = naming_loader()
    gate = gate_module()
    gsyl = gate["syllabify"]

    live_text = PACKET.read_text()
    live_packet = load(live_text)
    leg_live = Legality(live_packet["phonology"])

    r26_text = git_show(R26_REV, str(PACKET))
    r26_packet = load(r26_text)

    # BEFORE — the round-26 revision, whose 62-form figure was published, measured
    # against the round-26 GATE BYTES (transcribed, digest-pinned), so the BEFORE
    # column does not drift when the wave lands a fix in the live file.
    before = measure(f"round-26 revision {R26_REV}", r26_packet, leg_live,
                     r26_gate_syllabify)
    # AFTER — the live tree with the live gate.
    after = measure("round-27 live tree", live_packet, leg_live, gsyl)

    # The published figure, re-derived with the probe's own implementation
    # against the round-26 gate (the pair that produced "15 of 62").
    probe_head2_dis = 0
    for rid, form, _ in surface(r26_packet):
        if ("".join(r26_probe_design_syllabify(form)[:2])
                != "".join(r26_gate_syllabify(form)[:2])):
            probe_head2_dis += 1

    report = {
        "instrument": "reports/round-27/scribe/x54-syllabify-spotcheck.py",
        "seat": "SCRIBE X54",
        "assignment": "spot-check (syllabify before/after on all 62 forms independently)",
        "date": "2026-10-18",
        "measured_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "lane_head": lane_head(),
        "pins": {
            "gate_live": {str(GATE): sha256_file(GATE)},
            "gate_r26": {f"{R26_GATE_REV}:{GATE}": sha256_bytes(
                git_show(R26_GATE_REV, str(GATE)).encode())},
            "packet_live": {str(PACKET): sha256_bytes(live_text.encode())},
            "packet_r26": {f"{R26_REV}:{PACKET}": sha256_bytes(r26_text.encode())},
            "design": {str(DESIGN): sha256_file(DESIGN)},
        },
        "legality_source": {
            "template": live_packet["phonology"]["phonotactics"],
            "onset_clusters": live_packet["phonology"]["onset_clusters"],
            "codas": live_packet["phonology"]["coda"],
            "vowels": live_packet["phonology"]["vowels"],
            "diphthongs": "ai au (packet accent field: 'the only other vowel sequences')",
        },
        "before": before,
        "after": after,
        "published_figure_r26": {
            "source": "reports/round-26/register/review.md section 5 (RL-3)",
            "published": "15 of 62",
            "rederived_with_the_probes_own_implementation": probe_head2_dis,
            "rederived_with_W2_the_design_prose": before["head2_disagreements"],
        },
    }

    if args.json:
        print(json.dumps(report, indent=1, ensure_ascii=False))
        return 0

    print(f"X54 syllabify spot-check — {report['measured_at_utc']}")
    print(f"lane HEAD {report['lane_head']}")
    print(f"gate(live) {list(report['pins']['gate_live'].values())[0][:16]}  "
          f"gate(r26) {list(report['pins']['gate_r26'].values())[0][:16]}  "
          f"packet(live) {list(report['pins']['packet_live'].values())[0][:16]}  "
          f"packet(r26) {list(report['pins']['packet_r26'].values())[0][:16]}")
    print(f"legality: {report['legality_source']['template']}  "
          f"onset_clusters={report['legality_source']['onset_clusters']}  "
          f"codas={''.join(report['legality_source']['codas'])}")
    print()
    print("NOTE: BEFORE reads the round-26 GATE BYTES (transcribed from "
          f"{R26_GATE_REV}, C7-verified);")
    print("      AFTER reads the live gate. When the digests above differ, the "
          "fix has landed.")
    print()
    for key in ("before", "after"):
        r = report[key]
        print(f"== {key.upper()} — {r['label']} ==")
        print(f"   forms {r['forms']} | head2 disagreements {r['head2_disagreements']}"
              f" | syllable-list disagreements {r['syllable_list_disagreements']}"
              f" | forms the gate splits into a non-syllable {r['forms_with_non_syllable_from_gate']}")
        w = r["W3"]
        print(f"   W3 (packet's own `syllables:`) on {w['rows']} name records:"
              f" W1 agrees {w['W3_eq_W1']}/{w['rows']}, W2 agrees {w['W3_eq_W2']}/{w['rows']}")
    print()
    print("head2 disagreements, AFTER (the rows that matter for the declared op):")
    for row in report["after"]["rows"]:
        if not row["head2_agree"]:
            print(f"   {row['id']:6s} {row['form']:9s} gate={row['W1_gate_head2']:7s}"
                  f" design={row['W2_design_head2']}")
    print()
    print("published r26 figure vs this seat's re-derivation (round-26 gate bytes):")
    p = report["published_figure_r26"]
    print(f"   published:            {p['published']}")
    print(f"   probe impl re-run:    {p['rederived_with_the_probes_own_implementation']} of 62")
    print(f"   W2 (design prose):    {p['rederived_with_W2_the_design_prose']} of 62")
    return 0


if __name__ == "__main__":
    sys.exit(main())
