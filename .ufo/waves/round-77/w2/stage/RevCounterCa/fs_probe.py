"""RevCounterCa falsifier probe: is a frozen fixed_surfaces entry without
line/sha256/required an unbound whole-file APPENDONLY exemption?

Arm A (control): no fixed_surfaces; rewrite a SKILL.md prose line at lands
                 -> APPENDONLY must FAIL (changed line outside repair set).
Arm B (mutant) : claims Ca fixed_surfaces = [{"path": "SKILL.md"}]
                 (no line, no sha256, no required); same rewrite
                 -> observe whether the counter still PASSes 12/12.
Prior run (SHONEN.md prose rewrite, control, no exemption at all) PASSED
12/12: the protected-path `continue` skips the changed-line whitelist and the
"mark lines" scope only grades mark-line removals.
"""
import importlib.util
import json
import os
import tempfile

os.environ["HYAKU_SCRATCH"] = "/fast/scratch/hyaku/kotodama-r77/RevCounterCa/work"

ACA = ("/home/vgpnk/Projects/shokunin/kotodama-shokunin"
       "/.ufo/waves/round-77/w1/stage/ExecAdaptCa/accept-ca.py")
WORK = "/fast/scratch/hyaku/kotodama-r77/RevCounterCa/fsdemo"

spec = importlib.util.spec_from_file_location("aca", ACA)
aca = importlib.util.module_from_spec(spec)
spec.loader.exec_module(aca)

os.makedirs(WORK, exist_ok=True)


def run_arm(tag, claims_mutate):
    td = tempfile.mkdtemp(prefix=tag + "-", dir=WORK)
    lane, fleet, base, freeze, clean, combined0 = aca._build(
        td, tag, claims_mutate=claims_mutate)
    # a fresh Ca landing on the freeze, with one SHONEN.md prose line rewritten
    aca._fork(lane, "arm", freeze)
    aca._at(lane, freeze)
    pairs = aca._pairs(aca._g(lane, "rev-parse", "base").stdout.strip(), lane)
    with open(os.path.join(lane, "SCORECARD.md"), "a", encoding="utf-8") as fh:
        fh.write(aca._corrections(pairs))
    aca._write(lane, "corpus/README.md",
               "# corpus\n\n%s\n\n%s\n"
               % (aca.README_BASE_LINE, aca.README_TOTAL_AFTER))
    skill = open(os.path.join(lane, "SKILL.md"), encoding="utf-8").read()
    rewritten = skill.replace(
        "- a mutable skill line",
        "- a mutable skill line REWRITTEN-BY-NO-ONE", 1)
    assert rewritten != skill, "SKILL rewrite did not apply"
    aca._write(lane, "SKILL.md", rewritten)
    lands = aca._commit(lane, "Ca landing (SKILL prose line rewritten)")
    aca._set_branch(lane, "arm", lands)
    # claim C landing on top so COMBINED has both landings
    aca._write(lane, aca.CLAIM_C_ENTRY, "# naming systems\n\nbody\n")
    aca._write(lane, "corpus/README.md",
               "# corpus\n\n%s\n\n%s\n"
               % (aca.README_AFTER_LINE, aca.README_TOTAL_AFTER))
    aca._write(lane, "corpus/SOURCES.md",
               aca.FIXTURE_FILES["corpus/SOURCES.md"].rstrip("\n")
               + "\n| S897 | naming systems — https://example.org/ns | article"
                 " | B | naming | abstract | naming | mined | 2026-10-27 |"
                 " 180d | %s |" % aca.CLAIM_C_ENTRY
               + "\n| S898 | naming inventory — https://example.org/nv |"
                 " article | B | inventory | abstract | naming | mined |"
                 " 2026-10-27 | 180d | %s |\n" % aca.CLAIM_C_ENTRY)
    combined = aca._commit(lane, "claim C landing")
    aca._set_branch(lane, "main", combined)
    aca._at(lane, combined)
    code, states, text = aca._run_check(lane, lands, freeze, fleet, "arm",
                                        combined=combined)
    print("=== arm %s: exit=%d states=%s" % (tag, code, states))
    for line in text.splitlines():
        if line.startswith("LEG ") or line.startswith("ACCEPT-CA-77"):
            print(line)
    print()
    return code, states


print("SKILL.md base bytes (fixture):")
print(aca.FIXTURE_FILES["SKILL.md"])
print("claims Ca fixed_surfaces guard check in load_frozen: none (paths only)")

code_a, states_a = run_arm("ctrl", None)
mutate = None


def claims_mutate(claims):
    ca = [c for c in claims["claims"] if c["id"] == "Ca"][0]
    ca["fixed_surfaces"] = [{"path": "SKILL.md"}]
    print("injected fixed_surfaces:",
          json.dumps(ca["fixed_surfaces"]))


code_b, states_b = run_arm("mut", claims_mutate)

print("=== summary")
print("control  APPENDONLY:", states_a.get("APPENDONLY"), "exit:", code_a)
print("mutant   APPENDONLY:", states_b.get("APPENDONLY"), "exit:", code_b)
print("mutant   overall    :", states_b)
