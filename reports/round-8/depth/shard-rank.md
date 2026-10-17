# Shard R8-D04 — rank-rule adapter (D2 rank rules → typed adapter)

- shard: R8-D04 (targets.json `depth`, "Rank-rule adapter shard")
- deliverable: this fragment; the code block below is the integration payload for **R8-D02** (owner of `tools/d2-typed-labels.py`)
- date: 2026-10-17
- status: **complete for D2**; runs standalone as tested; no file in `tools/` was written by this shard
- canon: NON-CANON design drill; D2 is a sample design, not a canon decision (lore-shokunin owns canon)
- write scope: this file only. No component, corpus, tool, packet or gate was edited.
- interface: aligned to `reports/round-8/depth/design-spec.md` §4 (normalized rule record, adapter rules A1–A8, worked example) as it stood at 17:18 today.

## 1. What the assignment asked

"Implement rank-rule adaptation logic as a code block … Ground in the D2 example's actual rank rules."

The D2 component carries **21 prose rules** and no executable rules, so the costume gate's R-checks never run against them. This shard turns those 21 prose rules into the spec's normalized record shape, adds a declared projection into the gate's schema, and ships negative controls.

## 2. Grounding receipts (every claim below is a read location)

| Fact | Location |
|---|---|
| 21 prose rules: `wear_rules` WR-01..WR-09 (9), `speech_rules` SR-01..SR-06 (6), `touch_rules` TR-01..TR-06 (6) | `examples/culture-d2/components/12-rank-rules.yml:198-468` |
| No executable `rank_rules` in the component; the gate's R-checks read that key only | `examples/culture-d2/reviews/12-rank-rules.md:110-116` (RF-01); `tools/gates/costume-era-consistency-gate.py:464-494` |
| The gate's executable schema: `{id, authority, jurisdiction, eras, rites, effect: prohibit\|permit\|require, property: {kind, value}, wearer_ranks, exempt_ranks}` | `tools/gates/costume-era-consistency-gate.py:65-69` |
| Modelled `property.kind` values (material/fiber/cloth/fabric/textile, dye, garment, trim/closure/fastening, badge, placement, colour); anything else returns `None` | `tools/gates/costume-era-consistency-gate.py:1085-1114` |
| R-check order and semantics (R-01 note / R-02 reject / R-04 hold / R-05 conflict / R-06 unresolved scope; `require` is skipped) | `tools/gates/costume-era-consistency-gate.py:883-958` |
| The assembly already declares this gap: "12 prose rank rules are not translated into executable rank_rules; R-checks are unevaluated" | `examples/culture-d2/packet.d2.yml:3341` (assembly `unresolved`) |
| Degree slots DEG-1..DEG-7 (rank identity) | `12-rank-rules.yml:156-197` |
| Wearer index WI-1..WI-7 with `institution` and `rule_ref` (the costume-side rank handle); WI-2's DEG slot and WI-3..WI-7's `lexicon_ref` are `(to-verify)` | `examples/culture-d2/components/11-costumes.yml:101-107` |
| Costume rows carry `rule_edges` binding them to rule ids (e.g. GAR-03 → WR-01, WR-03, WR-06, TR-02, TR-06, LO-01) | `examples/culture-d2/packet.d2.yml:1926-1936`, `:1968-1976`, `:1990-1997` |
| Exact material strings the projected values must equal: `felt`, `lowland plant-thread cloth`, `wool`, `silk`, `lowland cord` | `examples/culture-d2/packet.d2.yml:1858`, `:1919`, `:1949`, `:2038`, `:2077` |
| Costume rows carry no `trims`/`badge` key; trims live as `closures: [{material, form}]` | `examples/culture-d2/packet.d2.yml:1924-1928`, `:1980-1992` |
| Spec: normalized record shape, adapter rules A1–A8, worked WR-02/GAR-04 example | `reports/round-8/depth/design-spec.md:377-486` |
| Spec's worked example verdict: GAR-04 at the fairgrounds in E1 is `not-applies` (no finding) with `wearer_ranks=[registered herd-master]` | `reports/round-8/depth/design-spec.md:472-486` |
| Review findings to make executable: RR-01 (import entitlement collision), RR-02 (jurisdiction), RR-03 (sale touch), RR-04 (storm duration), RR-05 (felt-day assay), RR-06 (universal compliance language) | `examples/culture-d2/reviews/12-rank-rules.md:52-106` |

The 21/9/6/6 split is the review's own count (`reviews/12-rank-rules.md:7`).

## 3. Design

**Normalized records (spec §4.1 shape).** One record per rule with `jurisdiction: {raw, places, bands}`, `property: {kind, value, slot_ref}`, `eras` + `era_history_raw`, `enforcement: {mechanism, assay, reality, sanction}`, `adapt_status` ∈ `executable | partial | cannot-evaluate`, `unresolved[]`, and `source: {component, record_id, line}`. Property kinds come from the spec's declared `sign_axis` table (§4.3), not from prose inference (A3).

**Gate projection is declared, not assumed.** `project_to_gate()` maps normalized records into the gate's schema and returns `None` for kinds the gate does not model (`grade`, `rite-state`, `occasion-exemption`, `wearer-category`, `act`), recording them in `unresolved` instead. Values are mapped through a declared table to the packet's exact strings; a value with no declared mapping raises `Malformed` rather than inventing one.

**The `wearer_ranks` semantic collision (the shard's central finding).** In the spec's normalized record, `wearer_ranks` names the class the rule *licenses* — the worked example gives WR-02 `wearer_ranks=[registered herd-master]` and calls GAR-04 `not-applies` (`design-spec.md:393`, `:480-486`). In the gate, `wearer_ranks` names the class the rule is *scoped to* (it bites), with `exempt_ranks` as the carve-out (`costume-era-consistency-gate.py:923-941`). Copying the field across unchanged therefore **inverts the verdict**: the naive projection makes a registered herd-master at the E1 fair trip WR-02 (a false R-02 reject) where the spec's own example says no finding. The projection translates by effect — for a prohibition, spec `wearer_ranks` → gate `exempt_ranks`; for a permission, spec `wearer_ranks` → gate `wearer_ranks` — and the selftest ships the fail-before/pass-after control (`control.naive_projection_inverts`).

**Nothing is silently dropped.** `build_payload()` asserts that the 21 component rule ids are exactly partitioned across normalized records, the act channel, and residuals. The act channel holds the speech/touch rules the gate cannot evaluate; every act entry carries `adapt_status: cannot-evaluate`, so it can never be mistaken for an executable rule value (A3's discipline).

**Conflicts are triaged.** Every reported pair must carry a triage status (`genuine-priority-gap`, `abstraction-artifact`, `band-keyed-pair`); the selftest fails on `UNTRIAGED`.

**Quarantine (A8).** WI-2's missing DEG slot and WI-3..WI-7's `(to-verify)` lexicon refs are quarantined as `cannot-evaluate` in `QUARANTINE`, cited, never filled in.

## 4. Code block (integration payload for R8-D02)

Tested as pasted, standalone, stdlib-only, no PyYAML, no network, no file writes.

```python
import json, re, hashlib

class Malformed(ValueError):
    pass

def key(text):
    return str(text).strip().casefold()

C12 = "examples/culture-d2/components/12-rank-rules.yml:"

RANK_TOKENS = {
    "lineage-head":     {"deg": "DEG-1", "wi": "WI-1", "aliases": ["lineage head"]},
    "wind-speaker":     {"deg": "DEG-2", "wi": None,   "aliases": ["wind-speaker", "wind-speakers", "wind speaker"]},
    "herd-master":      {"deg": "DEG-3", "wi": "WI-3", "aliases": ["herd-master", "registered herd-master", "caravan-registered herd-master"]},
    "herder-household": {"deg": "DEG-4", "wi": None,   "aliases": ["herder household", "herder households"]},
    "shelter-kin":      {"deg": "DEG-5", "wi": None,   "aliases": ["shelter-kin", "attached client"]},
    "fair-stranger":    {"deg": "DEG-6", "wi": "WI-5", "aliases": ["fair-stranger", "treaty stranger", "fair stranger"]},
    "spouse":           {"deg": "DEG-7", "wi": None,   "aliases": ["spouse", "spouse-of-household"]},
    "vanguard-herder":  {"deg": None,    "wi": "WI-2", "aliases": ["vanguard herder"], "slot_unresolved": True},
    "mast-bearer":      {"deg": None,    "wi": "WI-4", "aliases": ["wind-standard bearer", "mast-sash bearer"]},
    "mourner":          {"deg": None,    "wi": "WI-6", "aliases": ["mourner", "household of the dead"]},
    "bale-keeper":      {"deg": None,    "wi": "WI-7", "aliases": ["bale keeper", "caravan hands", "caravan hand"]},
}
WI_MARK = re.compile(r"\bWI-(\d)\b")
DEG_MARK = re.compile(r"\bDEG-(\d+)\b")
RITE_TOKENS = {
    "mourning year": ["mourning year", "mourning"],
    "wedding day": ["wedding day", "day of her wedding"],
    "the crossing": ["crossing", "ascent and descent"],
    "the caravan fair": ["caravan fair", "treaty days"],
    "storm law": ["storm law"],
    "the bale audit": ["bale audit"],
}
GATE_PROPERTY_KINDS = frozenset((
    "material", "fiber", "cloth", "fabric", "textile", "dye", "dyestuff",
    "garment", "robe", "clothing", "trim", "closure", "fastening", "badge",
    "insignia", "placement", "hue", "color", "colour"))
NON_PROJECTABLE_KINDS = frozenset(("grade", "rite-state", "occasion-exemption", "wearer-category", "act"))
GATE_KIND_MAP = {"material": "material", "trim": "trim", "badge": "badge", "dye": "dye"}
GATE_VALUE_MAP = {
    ("material", "lowland-plant-cloth"): "lowland plant-thread cloth",
    ("material", "plant-thread"): "lowland plant-thread cloth",
    ("trim", "hem-cords"): "hem-cord",
    ("badge", "mast-sash"): "mast-sash",
}
GATE_EFFECT_MAP = {"prohibit": "prohibit", "permit": "permit", "obligate": "require", "exempt": None}

def wi_by_id(wid):
    return next((t for t, m in RANK_TOKENS.items() if m.get("wi") == wid), None)

def deg_by_id(did):
    return next((t for t, m in RANK_TOKENS.items() if m.get("deg") == did), None)

def rank_tokens(text):
    out, text = [], str(text or "")
    for m in WI_MARK.findall(text):
        tok = wi_by_id("WI-" + m)
        if tok and tok not in out:
            out.append(tok)
    for m in DEG_MARK.findall(text):
        tok = deg_by_id("DEG-" + m)
        if tok and tok not in out:
            out.append(tok)
    low = key(text)
    for tok, meta in RANK_TOKENS.items():
        if tok not in out and any(a in low for a in meta["aliases"]):
            out.append(tok)
    return sorted(out)

def normalize_rite(text):
    low = key(text)
    for tok, pats in RITE_TOKENS.items():
        if any(p in low for p in pats):
            return tok
    return None

RANK_RESOLUTIONS = {
    "GAR-01": {"primary": "lineage-head", "secondary": ["herder-household"],
               "reason": "WI-1 lineage head speaks the grade; the coat is 'any adult of a pasture-holding lineage'",
               "cite": "examples/culture-d2/packet.d2.yml:1852"},
    "GAR-06": {"primary": "fair-stranger", "secondary": ["herd-master"],
               "reason": "WI-5 is the index marker; herd-master is the gift reading ('by gift, a registered herd-master may wear one')",
               "cite": "examples/culture-d2/packet.d2.yml:2007"},
    "GAR-08": {"primary": "bale-keeper", "secondary": ["herder-household"],
               "reason": "WI-7 bale keeper; the coil is worn by the man who counts bales",
               "cite": "examples/culture-d2/packet.d2.yml:2056"},
}

def resolve_costume_rank(cos):
    cid = cos.get("id") or "?"
    toks = rank_tokens(cos.get("wearer_rank"))
    if cid in RANK_RESOLUTIONS:
        return RANK_RESOLUTIONS[cid]["primary"], "resolved-by-declaration", RANK_RESOLUTIONS[cid]
    if len(toks) == 1:
        return toks[0], "resolved", None
    if not toks:
        return None, "unresolved", None
    return None, "ambiguous", {"candidates": toks}

def N(rid, effect, kind, value, slot_ref, eras, era_history_raw, wearer_ranks, exempt_ranks,
      authority, jurisdiction_raw, places, bands, rites, garment_refs, enforcement,
      adapt_status, unresolved, line, **extra):
    rec = {"id": rid, "authority": authority,
           "jurisdiction": {"raw": jurisdiction_raw, "places": list(places), "bands": list(bands)},
           "effect": effect, "property": {"kind": kind, "value": value, "slot_ref": slot_ref},
           "wearer_ranks": list(wearer_ranks), "exempt_ranks": list(exempt_ranks),
           "eras": list(eras), "era_history_raw": era_history_raw, "rites": list(rites),
           "garment_refs": list(garment_refs), "enforcement": enforcement,
           "adapt_status": adapt_status, "unresolved": list(unresolved),
           "source": {"component": "12-rank-rules.yml", "record_id": rid, "line": line}}
    rec.update(extra)
    return rec

def ENF(mechanism, assay, reality, sanction):
    return {"mechanism": mechanism, "assay": assay, "reality": reality, "sanction": sanction}

NORMALIZED = [
 N("WR-01", "prohibit", "grade", "G1-G3 felt-day ladder", "MAT-02", ["E0", "E1", "E2"],
   "E0 (knot only) -> E1 (renewed in script) -> E2 (grade floors frozen, prices left to the fair)",
   ["herd-master", "lineage-head"], [], "Valley Moot statute; oldest cord in the archive",
   "all circuits and all altitude bands", [], [], [], ["GAR-01", "GAR-02", "GAR-03"],
   ENF("winter moot cord check", "felt-days stamped at the bale seal-knot",
       "obeyed in the valley where the cord check runs; above the snow-line a household wears one grade up all summer and is not prosecuted",
       "knot cut, the coat's hem to the informing household, salt fine"),
   "partial", ["prose-only span: no felt-day-to-grade thresholds exist (RR-05)"], 199),
 N("WR-02", "prohibit", "material", "lowland-plant-cloth", "CMAT-06", ["E1", "E2"],
   "E1 onward (the treaty is the script's first D2 use)",
   ["herd-master"], [], "caravan treaty ratified at the winter moot",
   "valley fairgrounds and valley road; void at transit and high pasture",
   ["fairgrounds", "valley-road"], [], ["the caravan fair"], ["GAR-04", "GAR-06"],
   ENF("fair court register", "the fair court reads the caravan register against the coat",
       "the fair court prosecutes strangers and the visibly overdressed, and almost never a registered herd-master's spouse",
       "forfeiture of the coat at the fair gate, half the coat's hem-value to whoever sues"),
   "partial", ["the sell-line is undefined, so the upland scope is undecidable (RR-02)"], 212),
 N("WR-03", "prohibit", "trim", "hem-cords", "GAR-03", ["E0", "E1", "E2"], "E0 to E2",
   [], [], "Valley Moot statute", "all bands; the check itself happens only in the winter valley",
   [], [], ["the crossing"], ["GAR-03"],
   ENF("moot cord check", "count of cords against the cord archive",
       "over-fringed coats at the fair, cord-twist forgeries, a summer trade in second-hand fringes",
       "the over-count cords are cut at the moot in public; a forger's twist cord pays a bale"),
   "partial", ["cord count versus recorded ascents is not expressible",
               "costume rows carry hem-cords in prose, not in closures/trims"], 225),
 N("WR-04", "prohibit", "badge", "mast-sash", "GAR-05", ["E0", "E1", "E2"], "E0 to E2",
   ["mast-bearer"], [], "lineage head with moot confirmation",
   "all bands, because the mast travels with the herds", [], [], [], ["GAR-05"],
   ENF("moot issuance and recall", "weights tied into the end-cords, counted against the archive",
       "a forged sash is the only D2 dress crime that can end a family",
       "sash forfeited and burned; moot voice lost for a year"),
   "partial", ["the annual issuance/revocation interval is not expressible",
               "GAR-05 declares no badge field, so the gate's R-03 cannot fire"], 238),
 N("WR-05", "prohibit", "rite-state", "mourning finish", "GAR-07", ["E0", "E1", "E2"], "E0 to E2",
   ["mourner"], [], "Valley Moot statute with the wind-speakers' recitation",
   "all bands; suspended during storm law's first day (see TR-05)", [], [], ["mourning year"], ["GAR-07", "GAR-04"],
   ENF("moot comment by the dead-roll reciter", "the shaggy finish is visible; cut-back cords checked at the next moot",
       "observed hard - mourning is the one rule that is self-enforcing",
       "none needed; the sanction is social"),
   "cannot-evaluate", ["rite-state is not a gate-modelled property kind",
                       "the suspension interval (storm law's first day) disagrees with TR-05 (while storm law holds)"], 251),
 N("WR-06", "exempt", "occasion-exemption", "wedding day", None, ["E0", "E1", "E2"], "E0 to E2",
   ["spouse"], [], "Valley Moot statute", "any band, the day only", [], [], ["wedding day"], ["GAR-01", "GAR-03"],
   ENF("moot single-day entry", "the exemption is recorded by the moot as a single-day entry",
       "kept and even traded - families time weddings to the muster",
       "for the second wearing - salt fine and the cords returned"),
   "cannot-evaluate", ["the single-day duration and the borrowed household grade are not expressible"], 264),
 N("WR-07", "obligate", "wearer-category", "treaty stranger", "GAR-06", ["E1", "E2"], "E1 onward",
   ["fair-stranger"], [], "caravan treaty; enforced by the fair court",
   "fairgrounds and valley road only", ["fairgrounds", "valley-road"], [], ["the caravan fair"], ["GAR-06", "GAR-02"],
   ENF("fair court", "at corridor distance a good imitation passes; the court's real test is speech",
       "the fair court convicts on speech, not cloth",
       "coat forfeited; the trader's seal withdrawn for a season"),
   "cannot-evaluate", ["wearer-category is not a gate-modelled property kind",
                       "the G1 ceiling on strangers' felt is a grade predicate"], 277),
 N("WR-08", "prohibit", "material", "plant-thread", "CMAT-06", ["E0", "E1", "E2"],
   "E0 (when the thread was rare) to E2 (when everyone wears it)",
   [], [], "an archaic cord in the archive; renewed twice in living memory", "all bands, unenforced",
   [], [], [], ["GAR-08", "GAR-01", "GAR-04"],
   ENF("none that works", "none that works - the repair patch is the loophole written into the statute",
       "dead letter; old herders still refuse the patch publicly and wear it under the placket",
       "on paper, a salt fine; in practice, moot laughter"),
   "partial", ["the exception channel (bale-tying cord; patches smaller than a hand) is a form/size exemption the gate cannot express"], 290),
 N("WR-09", "permit", "material", "lowland-plant-cloth", "CMAT-06", ["E2"], "E2",
   [], [], "Valley Moot, after the storm-famine", "valley fairgrounds", ["fairgrounds"], [], ["the caravan fair"],
   ["GAR-02", "GAR-04", "GAR-08"],
   ENF("fair register", "the register keeps the seller's name, not the buyer's",
       "the reform passes and the fair booms",
       "none (permissive statute)"),
   "partial", ["the supersession list (which clauses this reform overrides) is not stated (RR-01)"], 303),
]

ACT_RULES = [
 {"id": "SR-01#a", "source_rule": "SR-01", "channel": "speech", "object": "storm-name", "effect": "prohibit",
  "wearer_ranks": [], "exempt_ranks": ["wind-speaker"], "eras": ["E0", "E1", "E2"],
  "jurisdiction": "below the snow-line", "adapt_status": "cannot-evaluate",
  "unresolved": ["speech is not a gate-modelled channel; raw sign_axis: sacred speech - the storm-name"], "cite": C12 + "318-329"},
 {"id": "SR-01#b", "source_rule": "SR-01", "channel": "speech", "object": "storm-name", "effect": "permit",
  "wearer_ranks": ["wind-speaker"], "exempt_ranks": [], "eras": ["E0", "E1", "E2"],
  "jurisdiction": "above the snow-line", "adapt_status": "cannot-evaluate",
  "unresolved": ["speech is not a gate-modelled channel"], "cite": C12 + "318-329"},
 {"id": "SR-02#a", "source_rule": "SR-02", "channel": "speech", "object": "summit greeting", "effect": "prohibit",
  "wearer_ranks": [], "exempt_ranks": [], "eras": ["E0", "E1", "E2"], "jurisdiction": "below the snow-line",
  "adapt_status": "cannot-evaluate", "unresolved": ["speech is not a gate-modelled channel"], "cite": C12 + "330-341"},
 {"id": "SR-03#a", "source_rule": "SR-03", "channel": "speech", "object": "another lineage's dead-name",
  "effect": "prohibit", "wearer_ranks": [], "exempt_ranks": [], "eras": ["E0", "E1", "E2"],
  "jurisdiction": "valley moot only", "adapt_status": "cannot-evaluate",
  "unresolved": ["speech is not a gate-modelled channel"], "cite": C12 + "342-353"},
 {"id": "SR-04#a", "source_rule": "SR-04", "channel": "speech", "object": "oath-form", "effect": "prohibit",
  "wearer_ranks": [], "exempt_ranks": [], "eras": ["E0", "E1", "E2"],
  "jurisdiction": "valley and camps (lineage oath); fairgrounds (trade oath)", "adapt_status": "cannot-evaluate",
  "unresolved": ["speech is not a gate-modelled channel"], "cite": C12 + "354-365"},
 {"id": "SR-05#a", "source_rule": "SR-05", "channel": "speech", "object": "statute-recitation", "effect": "obligate",
  "wearer_ranks": ["wind-speaker"], "exempt_ranks": [], "eras": ["E1", "E2"],
  "jurisdiction": "everywhere the moot's law runs", "adapt_status": "cannot-evaluate",
  "unresolved": ["speech is not a gate-modelled channel"], "cite": C12 + "366-377"},
 {"id": "SR-06#a", "source_rule": "SR-06", "channel": "speech", "object": "storm-law recitation", "effect": "prohibit",
  "wearer_ranks": [], "exempt_ranks": [], "eras": ["E0", "E1", "E2"],
  "jurisdiction": "valley, any season except the storm; camps, never", "adapt_status": "cannot-evaluate",
  "unresolved": ["speech is not a gate-modelled channel",
                 "the jurisdiction field excludes the settings where the prohibition appears to operate (RR-02)"], "cite": C12 + "378-389"},
 {"id": "TR-01#a", "source_rule": "TR-01", "channel": "touch", "object": "archive cord", "effect": "prohibit",
  "wearer_ranks": ["lineage-head"], "exempt_ranks": [], "eras": ["E0", "E1", "E2"],
  "jurisdiction": "the winter valley archive", "adapt_status": "cannot-evaluate",
  "unresolved": ["touch is not a gate-modelled channel; the touch right is limited to the lineage's own cord in the keeper's presence"], "cite": C12 + "392-404"},
 {"id": "TR-02#a", "source_rule": "TR-02", "channel": "touch", "object": "wind-standard hem", "effect": "prohibit",
  "wearer_ranks": [], "exempt_ranks": [], "eras": ["E0", "E1", "E2"], "jurisdiction": "the moot only",
  "adapt_status": "cannot-evaluate", "unresolved": ["touch is not a gate-modelled channel; the act kind is named by the spec's table but not modelled by the gate"], "cite": C12 + "405-417"},
 {"id": "TR-03#a", "source_rule": "TR-03", "channel": "touch", "object": "bale seal-knot", "effect": "permit",
  "wearer_ranks": [], "exempt_ranks": [], "eras": ["E1", "E2"],
  "jurisdiction": "fairgrounds; the custom travels with the bales", "adapt_status": "cannot-evaluate",
  "unresolved": ["touch is not a gate-modelled channel"], "cite": C12 + "418-430"},
 {"id": "TR-04#a", "source_rule": "TR-04", "channel": "touch", "object": "salt-measure", "effect": "prohibit",
  "wearer_ranks": [], "exempt_ranks": ["fair-stranger"], "eras": ["E0", "E1", "E2"],
  "jurisdiction": "fairgrounds and valley stores", "adapt_status": "cannot-evaluate",
  "unresolved": ["touch is not a gate-modelled channel"], "cite": C12 + "431-442"},
 {"id": "TR-05#a", "source_rule": "TR-05", "channel": "touch", "object": "mast rope", "effect": "permit",
  "wearer_ranks": [], "exempt_ranks": [], "eras": ["E0", "E1", "E2"],
  "jurisdiction": "above the snow-line, during storm law only", "adapt_status": "cannot-evaluate",
  "unresolved": ["touch is not a gate-modelled channel; the necessity clause's interval (while storm law holds) disagrees with WR-05"], "cite": C12 + "443-455"},
 {"id": "TR-06#a", "source_rule": "TR-06", "channel": "touch", "object": "salt-measure", "effect": "obligate",
  "wearer_ranks": [], "exempt_ranks": [], "eras": ["E1", "E2"], "jurisdiction": "fairgrounds",
  "adapt_status": "cannot-evaluate", "unresolved": ["touch is not a gate-modelled channel"], "cite": C12 + "456-468"},
]
RESIDUALS = [
 {"id": "WR-06#b", "source_rule": "WR-06", "reason": "the household-grade lock is a grade predicate; recorded as a loss, not a record", "cite": C12 + "264-276"},
]
CALIBRATION_FLAGS = [
 {"rule": "WR-05", "text": "observed hard - mourning is the one rule that is self-enforcing", "cite": C12 + "259"},
 {"rule": "SR-06", "text": "kept strictly", "cite": C12 + "386"},
 {"rule": "TR-05", "text": "the one rule no one evades", "cite": C12 + "451"},
]
ENTITLEMENT_EDGES = [
 {"rank": "fair-stranger", "rights": "may wear their own lowland cloth and fair coat", "cite": C12 + "189", "against": ["WR-02"]},
 {"rank": "herd-master", "rights": "may wear lowland cloth inside the fairgrounds", "cite": C12 + "171", "against": []},
]
QUARANTINE = [
 {"handle": "WI-2", "issue": "no DEG slot: rule_ref is '(to-verify) DEG slot'", "adapt_status": "cannot-evaluate",
  "cite": "examples/culture-d2/components/11-costumes.yml:102"},
 {"handle": "WI-3..WI-7", "issue": "lexicon_ref is '(to-verify)' for each", "adapt_status": "cannot-evaluate",
  "cite": "examples/culture-d2/components/11-costumes.yml:103-107"},
 {"handle": "GAR-06", "issue": "one wearer_rank field names two ranks; the primary is declared in RANK_RESOLUTIONS, the gift reading stays secondary",
  "adapt_status": "cannot-evaluate", "cite": "examples/culture-d2/packet.d2.yml:2007"},
]
CONFLICT_TRIAGE = {
 "WR-02|WR-09": {"status": "genuine-priority-gap", "why": "RR-01: the E2 reform's supersession of the E1 monopoly is unstated", "cite": C12 + "212-224,303-315"},
 "WR-05|WR-09": {"status": "genuine-priority-gap", "reachable": False,
                 "why": "RR-01 recheck: an ordinary household's lowland cloth at the E2 winter fair against the mourning-body ban; not emitted as a conflict because WR-05's rite-state kind is not gate-modelled", "cite": C12 + "251-263,303-315"},
 "WR-08|WR-09": {"status": "genuine-priority-gap", "why": "RR-01: the fossil ban is a dead letter in practice but is not repealed on paper", "cite": C12 + "290-302,303-315"},
 "WR-03|WR-06": {"status": "abstraction-artifact", "reachable": False,
                 "why": "both carry {trim, hem-cord}, but WR-06 is an occasion exemption (exempt path, A6) and is not projected, so the pair cannot fire; retained because a future projection change would resurrect it", "cite": C12 + "225-237,264-276"},
 "SR-01#a|SR-01#b": {"status": "band-keyed-pair", "why": "below-line prohibition and above-line permission of the same rule; jurisdictions are disjoint by construction", "cite": C12 + "318-329"},
 "TR-04#a|TR-06#a": {"status": "genuine-priority-gap", "why": "RR-03: the sale's mandatory touch of the buyer's measure collides with the prohibition on touching the measure rather than the salt", "cite": C12 + "431-442,456-468"},
}
JURISDICTION_GAPS = [
 {"rule": "WR-02", "gap": "the sell-line is undefined, so upland wearing is either illegal-but-unpoliced or outside the ban", "cite": C12 + "212-224"},
 {"rule": "SR-06", "gap": "the jurisdiction field excludes the settings where the prohibition appears to operate", "cite": C12 + "378-389"},
 {"rule": "JU-3", "gap": "officer coverage disagrees with EN-2's circuit-wide reach", "cite": C12 + "514-520,528-533"},
]
ASSAY_GAPS = [
 {"rule": "WR-01", "gap": "no felt-day-to-grade thresholds, ascent/bale-to-entitlement rule, or coat-to-bale link exists", "cite": C12 + "199-211"},
 {"rule": "WR-03", "gap": "the cord count has no machine-readable field on the costume rows", "cite": C12 + "225-237"},
]
COMPONENT_RULE_IDS = ["WR-0%d" % i for i in range(1, 10)] + ["SR-0%d" % i for i in range(1, 7)] + ["TR-0%d" % i for i in range(1, 7)]

def project_to_gate(rec):
    """Normalized record -> gate schema, or None when the gate cannot evaluate it."""
    kind = key(rec["property"]["kind"])
    if rec["adapt_status"] == "cannot-evaluate" or kind in NON_PROJECTABLE_KINDS:
        return None
    if kind not in GATE_KIND_MAP:
        raise Malformed("%s: no declared gate kind mapping for %r" % (rec["id"], kind))
    value = GATE_VALUE_MAP.get((kind, rec["property"]["value"]))
    if value is None:
        raise Malformed("%s: no declared gate value mapping for (%s, %s) - refusing to invent one"
                        % (rec["id"], kind, rec["property"]["value"]))
    gate_effect = GATE_EFFECT_MAP[rec["effect"]]
    if gate_effect is None:
        return None
    if rec["effect"] == "prohibit":
        wearer_ranks, exempt_ranks = [], list(rec["wearer_ranks"]) + list(rec["exempt_ranks"])
    else:
        wearer_ranks, exempt_ranks = list(rec["wearer_ranks"]), list(rec["exempt_ranks"])
    return {"id": rec["id"] + "#g", "source_rule": rec["id"], "authority": rec["authority"],
            "jurisdiction": rec["jurisdiction"]["raw"], "eras": list(rec["eras"]),
            "rites": list(rec["rites"]) or None, "effect": gate_effect,
            "property": {"kind": GATE_KIND_MAP[kind], "value": value},
            "wearer_ranks": wearer_ranks, "exempt_ranks": exempt_ranks,
            "adapt_status": rec["adapt_status"], "cite": rec["source"]["component"] + ":" + str(rec["source"]["line"]),
            "semantics_note": ("spec wearer_ranks names the licensed class for a prohibition; the gate scopes "
                               "wearer_ranks to the class the rule bites, so the licensed class moves to exempt_ranks")}

def naive_projection(rec):
    """The un-translated copy that inverts prohibition verdicts; shipped only as a negative control."""
    out = project_to_gate(rec)
    if out is None:
        return None
    out = dict(out)
    out["wearer_ranks"], out["exempt_ranks"] = list(rec["wearer_ranks"]), list(rec["exempt_ranks"])
    return out

def build_payload():
    src = sorted({r["id"] for r in NORMALIZED} | {r["source_rule"] for r in ACT_RULES} | {r["source_rule"] for r in RESIDUALS})
    if src != sorted(COMPONENT_RULE_IDS):
        raise Malformed("coverage: component rules %r not partitioned exactly" % sorted(set(COMPONENT_RULE_IDS) ^ set(src)))
    for rec in NORMALIZED:
        if not rec["eras"]:
            raise Malformed("%s: no effective interval (EAR-04 class)" % rec["id"])
        if rec["adapt_status"] not in ("executable", "partial", "cannot-evaluate"):
            raise Malformed("%s: unknown adapt_status %r" % (rec["id"], rec["adapt_status"]))
    gate = [g for g in (project_to_gate(r) for r in NORMALIZED) if g is not None]
    unresolved = sorted([{"rule": r["id"], "item": u} for r in NORMALIZED for u in r["unresolved"]],
                        key=lambda d: (d["rule"], d["item"]))
    return {"normalized_rules": sorted(NORMALIZED, key=lambda r: r["id"]),
            "gate_rank_rules": sorted(gate, key=lambda r: r["id"]),
            "act_rules": sorted(ACT_RULES, key=lambda r: r["id"]),
            "residuals": sorted(RESIDUALS, key=lambda r: r["id"]),
            "unresolved": unresolved,
            "quarantine": sorted(QUARANTINE, key=lambda r: r["handle"]),
            "calibration_flags": sorted(CALIBRATION_FLAGS, key=lambda r: r["rule"]),
            "entitlement_edges": sorted(ENTITLEMENT_EDGES, key=lambda r: r["rank"]),
            "jurisdiction_gaps": sorted(JURISDICTION_GAPS, key=lambda r: r["rule"]),
            "assay_gaps": sorted(ASSAY_GAPS, key=lambda r: r["rule"]),
            "coverage": {"component_rules": len(COMPONENT_RULE_IDS), "normalized": len(NORMALIZED),
                         "gate_projected": len(gate), "partitioned": True}}

def scope_of(rule):
    return {r for r in (rule.get("wearer_ranks") or sorted(RANK_TOKENS)) if r not in set(rule.get("exempt_ranks") or [])}

def eras_overlap(a, b):
    return bool({key(x) for x in a} & {key(x) for x in b})

def conflicts(records):
    out = []
    for i, a in enumerate(records):
        for b in records[i + 1:]:
            if key(a["property"]["kind"]) != key(b["property"]["kind"]) or key(a["property"]["value"]) != key(b["property"]["value"]):
                continue
            if {key(a["effect"]), key(b["effect"])} != {"prohibit", "permit"}:
                continue
            if not eras_overlap(a["eras"], b["eras"]):
                continue
            shared = scope_of(a) & scope_of(b)
            if shared:
                pid = "%s|%s" % (a["source_rule"], b["source_rule"])
                out.append({"class": "R-05-class", "pair": [a["id"], b["id"]], "rank_in_scope": sorted(shared)[0],
                            "triage": CONFLICT_TRIAGE.get(pid, {"status": "UNTRIAGED"})})
    return out

def act_conflicts(rules):
    out = []
    for i, a in enumerate(rules):
        for b in rules[i + 1:]:
            if a["channel"] != b["channel"] or key(a["object"]) != key(b["object"]):
                continue
            if not eras_overlap(a["eras"], b["eras"]):
                continue
            effs = {key(a["effect"]), key(b["effect"])}
            if effs & {"prohibit"} and effs & {"permit", "obligate"}:
                pid = "%s|%s" % (a["id"], b["id"])
                out.append({"class": "act-collision", "pair": [a["id"], b["id"]], "object": a["object"],
                            "triage": CONFLICT_TRIAGE.get(pid, {"status": "UNTRIAGED"})})
    return out

def verdict_for(rule, row):
    """Three-valued verdict in the spec's vocabulary, mirroring the gate's applicability order."""
    if not any(key(e) == key(row.get("era")) for e in rule["eras"]):
        return "not-applies"
    kind = key(rule["property"]["kind"])
    if kind not in GATE_PROPERTY_KINDS:
        raise Malformed("property kind %r is outside the gate's modelled set" % kind)
    value = key(rule["property"]["value"])
    if kind in ("material", "fiber", "cloth", "fabric", "textile"):
        target = key(row.get("material") or "")
        if not target or target != value:
            return "not-applies"
    elif kind in ("garment", "robe", "clothing"):
        target = key(row.get("garment") or "")
        if not target or not (target == value or (len(value) >= 4 and value in target)):
            return "not-applies"
    elif kind in ("badge", "insignia"):
        target = key(row.get("badge_office") or row.get("badge") or "")
        if not target or target != value:
            return "not-applies"
    elif kind in ("trim", "closure", "fastening"):
        return "cannot-evaluate"
    else:
        return "not-applies"
    if rule.get("effect") not in ("prohibit", "permit"):
        return "cannot-evaluate"
    wearer, status, _ = resolve_costume_rank(row)
    wearer_ranks = rule.get("wearer_ranks")
    if wearer_ranks:
        if status != "resolved":
            return "cannot-evaluate"
        if not any(key(wearer) == key(w) for w in wearer_ranks):
            return "not-applies"
    elif status in ("unresolved", "ambiguous"):
        return "cannot-evaluate"
    if any(key(wearer) == key(x) for x in (rule.get("exempt_ranks") or [])):
        return "not-applies"
    return "applies"

def entitlement_conflicts(records):
    by_rule = {r["source_rule"]: r for r in records}
    out = []
    for edge in ENTITLEMENT_EDGES:
        for rid in edge["against"]:
            rec = by_rule[rid]
            if key(rec["effect"]) == "prohibit" and edge["rank"] in scope_of(rec):
                out.append({"class": "entitlement-conflict", "rank": edge["rank"], "rule": rid, "cite": edge["cite"],
                            "note": "declared degree entitlement meets a projected prohibition with no exemption"})
    return out

def fixtures():
    gate = {r["source_rule"]: r for r in (g for g in (project_to_gate(r) for r in NORMALIZED) if g is not None)}
    stranger = {"id": "FIX-STRANGER", "material": "lowland plant-thread cloth", "era": "E2",
                "wearer_rank": "treaty stranger (WI-5)", "rite": "the caravan fair (treaty days)"}
    master = {"id": "FIX-MASTER", "material": "lowland plant-thread cloth", "era": "E1",
              "wearer_rank": "registered herd-master only (WI-3)", "rite": "the caravan fair (treaty days)"}
    mourner = {"id": "FIX-MOURNER", "material": "lowland plant-thread cloth", "era": "E1",
               "wearer_rank": "mourner, household of the dead (WI-6)", "rite": "the mourning year (time-locked)"}
    return [
      {"name": "RR-01 treaty stranger in their own lowland cloth at the E2 fair", "row": stranger,
       "verdicts": {rid: verdict_for(gate[rid], stranger) for rid in ("WR-02", "WR-09")}},
      {"name": "spec worked example: registered herd-master at the E1 fair", "row": master,
       "verdicts": {rid: verdict_for(gate[rid], master) for rid in ("WR-02", "WR-09")}},
      {"name": "RR-04 mourner on the second day of storm law", "row": mourner,
       "verdicts": {"WR-05": "cannot-evaluate (rite-state is not gate-modelled)"},
       "act_interval": {"WR-05": "storm law's first day only", "TR-05#a": "while storm law holds"},
       "interval_mismatch": True},
      {"name": "RR-05 shelter-kin coat of unrecorded felt grade",
       "verdicts": {"WR-01": "cannot-evaluate (grade kind; no felt-day-to-grade thresholds exist)"}},
    ]

def selftest():
    checks, payload = [], build_payload()
    def ck(name, cond, detail=""):
        checks.append({"check": name, "ok": bool(cond), "detail": detail})
    ck("coverage.partition", payload["coverage"]["partitioned"] and payload["coverage"]["component_rules"] == 21)
    ck("coverage.normalized_nine", payload["coverage"]["normalized"] == 9)
    ck("coverage.gate_projected_five", payload["coverage"]["gate_projected"] == 5
       and "WR-04" in [g["source_rule"] for g in payload["gate_rank_rules"]],
       str([g["source_rule"] for g in payload["gate_rank_rules"]]))
    ck("triage.unreachable_marked", all(("reachable" in t) == (t.get("reachable") is False)
       for t in CONFLICT_TRIAGE.values()))
    ck("record.spec_shape", all({"id", "authority", "jurisdiction", "effect", "property", "wearer_ranks",
        "exempt_ranks", "eras", "era_history_raw", "rites", "garment_refs", "enforcement", "adapt_status",
        "unresolved", "source"} <= set(r) for r in payload["normalized_rules"]))
    ck("record.source_mapping", all(r["source"]["component"] == "12-rank-rules.yml" and r["source"]["line"]
        and r["source"]["record_id"] == r["id"] for r in payload["normalized_rules"]))
    ck("record.adapt_status_vocabulary", all(r["adapt_status"] in ("executable", "partial", "cannot-evaluate")
        for r in payload["normalized_rules"]))
    ck("identity.herd_master", resolve_costume_rank({"id": "GAR-04", "wearer_rank": "registered herd-master only (WI-3)"})[0] == "herd-master")
    ck("identity.ambiguous_never_silent", resolve_costume_rank({"id": "X", "wearer_rank": "treaty stranger and a lineage head"})[1] == "ambiguous")
    ck("identity.unresolved_never_silent", resolve_costume_rank({"id": "X", "wearer_rank": "no rank named"})[1] == "unresolved")
    ck("quarantine.A8_present", {q["handle"] for q in payload["quarantine"]} >= {"WI-2", "WI-3..WI-7", "GAR-06"})
    conf = conflicts(payload["gate_rank_rules"])
    pairs = sorted(tuple(c["pair"]) for c in conf)
    ck("conflict.WR02_vs_WR09", ("WR-02#g", "WR-09#g") in pairs, str(pairs))
    ck("conflict.all_triaged", all(c["triage"]["status"] != "UNTRIAGED" for c in conf))
    actp = act_conflicts(payload["act_rules"])
    ck("actconflict.TR04_vs_TR06", ("TR-04#a", "TR-06#a") in sorted(tuple(c["pair"]) for c in actp))
    ck("actconflict.all_triaged", all(c["triage"]["status"] != "UNTRIAGED" for c in actp))
    gate = {r["source_rule"]: r for r in payload["gate_rank_rules"]}
    master = {"id": "FIX-MASTER", "material": "lowland plant-thread cloth", "era": "E1",
              "wearer_rank": "registered herd-master only (WI-3)"}
    ck("spec.worked_example_not_applies", verdict_for(gate["WR-02"], master) == "not-applies",
       verdict_for(gate["WR-02"], master))
    naive = {r["source_rule"]: r for r in (naive_projection(r) for r in NORMALIZED) if r is not None}
    ck("control.naive_projection_inverts", verdict_for(naive["WR-02"], master) == "applies",
       "naive=%s declared=%s" % (verdict_for(naive["WR-02"], master), verdict_for(gate["WR-02"], master)))
    stranger = {"id": "FIX-STRANGER", "material": "lowland plant-thread cloth", "era": "E2",
                "wearer_rank": "treaty stranger (WI-5)"}
    ck("control.declared_projection_still_catches_stranger", verdict_for(gate["WR-02"], stranger) == "applies")
    ent = entitlement_conflicts(payload["gate_rank_rules"])
    ck("entitlement.fair_stranger", any(e["rank"] == "fair-stranger" for e in ent))
    fx = fixtures()
    ck("fixture.RR01_conflict_visible", fx[0]["verdicts"] == {"WR-02": "applies", "WR-09": "applies"}, str(fx[0]["verdicts"]))
    ck("fixture.RR04_interval_mismatch", fx[2]["interval_mismatch"] is True)
    ck("fixture.RR05_cannot_evaluate", "cannot-evaluate" in fx[3]["verdicts"]["WR-01"])
    ck("gaps.RR02_present", {g["rule"] for g in payload["jurisdiction_gaps"]} >= {"WR-02", "SR-06", "JU-3"})
    ck("gaps.RR05_present", {g["rule"] for g in payload["assay_gaps"]} >= {"WR-01", "WR-03"})
    ck("calibration.flags_present", len(payload["calibration_flags"]) == 3)
    ck("unresolved.not_empty", len(payload["unresolved"]) >= 6, str(len(payload["unresolved"])))
    d1 = hashlib.sha256(json.dumps(payload, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode()).hexdigest()
    d2 = hashlib.sha256(json.dumps(build_payload(), sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode()).hexdigest()
    ck("determinism.double_build", d1 == d2, d1)
    try:
        project_to_gate({"id": "X", "effect": "prohibit", "adapt_status": "executable",
                         "property": {"kind": "material", "value": "invented-cloth"}, "wearer_ranks": [],
                         "exempt_ranks": [], "eras": ["E0"], "rites": [], "authority": "?", "jurisdiction": {"raw": "?"},
                         "source": {"component": "12-rank-rules.yml", "record_id": "X", "line": 1}})
        ck("neg.undeclared_value_refused", False, "no rejection")
    except Malformed as exc:
        ck("neg.undeclared_value_refused", True, str(exc))
    ck("neg.unknown_rank_cannot_evaluate", verdict_for({"eras": ["E0"], "effect": "prohibit",
        "property": {"kind": "material", "value": "felt"}, "wearer_ranks": [], "exempt_ranks": []},
        {"id": "X", "material": "felt", "era": "E0", "wearer_rank": "unlisted rank"}) == "cannot-evaluate")
    ck("neg.trim_cannot_evaluate", verdict_for({"eras": ["E0"], "effect": "prohibit",
        "property": {"kind": "trim", "value": "hem-cord"}, "wearer_ranks": [], "exempt_ranks": []},
        {"id": "GAR-03", "material": "felt", "era": "E0", "wearer_rank": "herder household"}) == "cannot-evaluate")
    failed = [c for c in checks if not c["ok"]]
    print("passed=%d failed=%d digest=%s" % (len(checks) - len(failed), len(failed), d1))
    for c in failed:
        print("FAIL", c["check"], c["detail"])
    print("conflicts:", json.dumps([(c["pair"], c["triage"]["status"]) for c in conf]))
    print("act:", json.dumps([(c["pair"], c["triage"]["status"]) for c in actp]))
    return 0 if not failed else 1

import sys
sys.exit(selftest())
```

## 5. Verification receipt

Run at 2026-10-17 from the lane root: the code block was extracted from this file and piped to `python3 -` (no scratch file, no write), so the delivered bytes are what ran.

```
$ cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
$ python3 - <<'PY'   # extracts the ```python block from reports/round-8/depth/shard-rank.md and pipes it to python3 -
$ echo $?
```

Actual observed output of that extraction run (2026-10-17):

```
python blocks: 1 chars: 35925
exit: 0
passed=30 failed=0 digest=1fe3901da6ea311e1dd0040640afb313e58e7f94da3d6dc1faaa6d3ddce3f702
conflicts: [[["WR-02#g", "WR-09#g"], "genuine-priority-gap"], [["WR-08#g", "WR-09#g"], "genuine-priority-gap"]]
act: [[["SR-01#a", "SR-01#b"], "band-keyed-pair"], [["TR-04#a", "TR-06#a"], "genuine-priority-gap"]]
```

`digest` is `sha256(json.dumps(payload, sort_keys=True, ensure_ascii=False, separators=(",", ":")))`, recomputed twice in the same run and asserted equal (`determinism.double_build`). D02 should freeze this value when the code lands in `tools/d2-typed-labels.py`; any later ledger edit must then show up as explicit digest drift.

## 6. What the adapter found in the actual D2 rules (findings for D02/integrators)

Machine verdicts, not new prose claims; each traces to the triage/gap/quarantine tables above.

1. **The `wearer_ranks` inversion (highest priority).** The spec's normalized record uses `wearer_ranks` for the *licensed* class (`design-spec.md:393`, `:480-486`); the gate uses it for the *scoped* class (`costume-era-consistency-gate.py:923-941`). A verbatim copy makes GAR-04 (registered herd-master, E1 fair) trip WR-02 — a false R-02 reject where the spec's own worked example says `not-applies`. `project_to_gate()` translates by effect and the selftest asserts both sides: naive = `applies`, declared = `not-applies`, while the treaty stranger still yields `applies`. This is the same identity-collision family as the round-7 parent-check defect the O-shards are repairing.
2. **RR-01 reproduced.** `WR-02#g` (prohibit, E1+) and `WR-09#g` (permit, E2, fairgrounds) collide on the same row at the E2 fair; `entitlement_conflicts()` adds the DEG-6 edge (`12-rank-rules.yml:189`). The component states no supersession list, so the gap stands.
3. **RR-03 reproduced.** `TR-04#a` (prohibit touching the measure) vs `TR-06#a` (obligate the seller's touch of the buyer's measure) collide on `salt-measure` at the fair from E1.
4. **RR-04 reproduced.** `WR-05` suspends on storm law's *first day*, `TR-05#a` runs *while storm law holds*; the fixture records the mismatch rather than resolving it.
5. **RR-05 stays `cannot-evaluate` by construction.** `WR-01` is a `grade` kind with no felt-day thresholds; the adapter never yields a grade verdict.
6. **Only 5 of 9 wear rules project to the gate.** `WR-02`, `WR-03`, `WR-04`, `WR-08`, `WR-09` project (`gate_projected_five`); `WR-01` (grade), `WR-05` (rite-state), `WR-06` (occasion exemption), `WR-07` (wearer-category) do not. Two of the five are hollow in practice: `WR-04`'s projection cannot fire because GAR-05 declares no `badge` field (`packet.d2.yml:1980-1992`), and `WR-03`'s every costume-side row returns `cannot-evaluate` because hem-cords are prose only. So the working gate coverage today is 3 rules, not 9.
7. **Identity defects found live:** WI-2 has no DEG slot; GAR-06 names two ranks in one field. Both quarantined, neither guessed.
8. **Rite tokens collide the same way as rank tokens:** the packet's rite strings carry parentheticals, so the gate's exact `key()` comparison under-applies rite-scoped rules; `normalize_rite()` supplies the token layer.

## 7. Integration contract for R8-D02

- Lift the code block into `tools/d2-typed-labels.py` as-is (stdlib only); it does not depend on this markdown file.
- `--selftest` should call `selftest()` and exit 0/1 (targets.json `depth` counting command: `python3 tools/d2-typed-labels.py --selftest`).
- Use `project_to_gate()`, never `naive_projection()`. The naive function exists only as the shipped negative control.
- Keep `adapt_status` and `unresolved[]` in the emitted artifact: they are the mechanism that stops a `cannot-evaluate` rule from being read as a pass (A4).
- `conflicts()` results triaged `genuine-priority-gap` are findings for the owner of component 12, not repairs. Do not add exemptions to clear them: RR-01's candidate repair is an owner decision (`reviews/12-rank-rules.md:59`) and canon belongs to lore-shokunin.
- Projected records match the D3 executable precedent's shape (`examples/culture-d3/components/06-material.json` `rank_rules`), with extra provenance keys (`source_rule`, `cite`, `adapt_status`, `semantics_note`) that the gate ignores.

## 8. Limits

- The ledger is authored from component 12 as read today; if the component changes, the `source.line` values and the frozen digest must be re-derived together.
- Conflict detection runs on the *projected abstraction* (kind+value, era overlap, rank scope). Two triage entries are marked `reachable: false` because their rules are not projected at all (`WR-05|WR-09`, `WR-03|WR-06`); they are retained, not deleted, so a future projection change cannot resurrect an untriaged pair. Untriaged pairs fail the selftest.
- Speech/touch rules are structured only as a `cannot-evaluate` act channel for conflict checking; a full speech-channel evaluation is out of this shard's scope.
- No external source was retrieved for this shard: it is grounded entirely in lane files, and every count and quote names its `file:line`.
- D02's `tools/d2-typed-labels.py` was red at 17:20 today (4 controls: `malformed: unreadable maps_to refused`, `malformed: unknown institution id refused`, `parser: malformed '(translated label)' refused`, `parser: malformed 'label (analyst label)' refused`); D02 repaired it, and at 17:22:53 the tool reports `selftest: 32/32 checks passed` with exit 0. As of 17:24 the tool contains **none** of this shard's adapter symbols (`grep -c "project_to_gate\|naive_projection\|semantics_note\|RANK_TOKENS\|shard-rank" tools/d2-typed-labels.py` = 0), so the rank-rule adapter is delivered here and still needs D02's integration. Neither run is evidence for the other: this shard's green run covers this file's code block only.
