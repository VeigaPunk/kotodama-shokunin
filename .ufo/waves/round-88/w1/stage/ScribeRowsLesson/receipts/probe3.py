import json, pathlib, subprocess, importlib.util
spec = importlib.util.spec_from_file_location('m88', '/home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-88/measure88.py')
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
m.ROOT = pathlib.Path('/home/vgpnk/Projects/shokunin/kotodama-shokunin')
work = pathlib.Path('/fast/scratch/hyaku/kotodama-r88/ScribeRowsLesson/probe')
raw = subprocess.run(['git','-C',str(m.ROOT),'show','4956282281dac1306cfbe59523e46dde99749d75:.ufo/waves/round-86/w1/stage/ExecCraftLedger/craft.json'],capture_output=True).stdout
packet_obj = json.loads(raw)
cases = json.loads(pathlib.Path('/home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-88/cases.json').read_text())
# oracle v2: table keyed on the r88 case NAMES (not filenames) - shows the kill comes from opaque filenames
body = '''import json, pathlib, sys
TABLE = {
    "clean": (0, [], 6),
    "duplicate-id": (1, ["RECORD_ID"], 6),
    "missing-clock": (1, ["CLOCK_MISSING"], 6),
    "blank-reason": (1, ["CLOCK_REASON"], 6),
    "invalid-date": (1, ["CLOCK_DATE"], 6),
    "blank-sense": (1, ["RECORD_FIELD"], 6),
    "unresolved-selected": (1, ["SOLUTION_CONFLICT"], 6),
    "conjecture-promoted": (1, ["EDITORIAL_CONFLICT"], 6),
    "translation-backdated": (1, ["TRANSLATION_CLOCK"], 6),
    "unknown-explicit": (0, [], 6),
    "reordered": (0, [], 6),
    "double-anomaly": (1, ["RECORD_FIELD", "SOLUTION_CONFLICT"], 6),
    "invalid-json": (2, ["ATTESTATION_ERROR"], None),
}
p = pathlib.Path(sys.argv[sys.argv.index("--packet") + 1])
try:
    body_in = json.loads(p.read_text())
    name = body_in.get("__name__", "")
except Exception:
    name = ""
rc, ids, records = TABLE.get(name, (1, ["RECORD_ID"], 6))
if rc == 2:
    print("ATTESTATION_ERROR: unreadable packet", file=sys.stderr)
    sys.exit(2)
out = dict(findings=[dict(id=i, record="file", detail="from name") for i in ids])
if records is not None:
    out["records"] = records
print(json.dumps(out, sort_keys=True))
sys.exit(rc)
'''
t = work/'filename-oracle-v2.py'; t.write_text(body)
rows = m.score(t, packet_obj, cases, work)
print(json.dumps(dict(passed=sum(r['passed'] for r in rows), total=len(rows),
                       failures=[r['case'] for r in rows if not r['passed']]), indent=1))
