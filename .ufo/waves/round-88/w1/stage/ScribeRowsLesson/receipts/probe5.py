import json, pathlib, subprocess, importlib.util, hashlib
spec = importlib.util.spec_from_file_location('m88', '/home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-88/measure88.py')
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
m.ROOT = pathlib.Path('/home/vgpnk/Projects/shokunin/kotodama-shokunin')
work = pathlib.Path('/fast/scratch/hyaku/kotodama-r88/ScribeRowsLesson/probe')
raw = subprocess.run(['git','-C',str(m.ROOT),'show','4956282281dac1306cfbe59523e46dde99749d75:.ufo/waves/round-86/w1/stage/ExecCraftLedger/craft.json'],capture_output=True).stdout
packet_obj = json.loads(raw)
cases = json.loads(pathlib.Path('/home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-88/cases.json').read_text())
# Build the memorization table: sha256(packet bytes) -> expected verdict, for every case.
table = {}
for case in cases['cases']:
    if case['mutations'] and case['mutations'][0]['op'] == 'raw':
        payload = case['mutations'][0]['value'].encode()
    else:
        payload = json.dumps(m.build(packet_obj, case['mutations'])).encode()
    table[hashlib.sha256(payload).hexdigest()] = [case['rc'], case['ids'], case.get('records_count')]
body = '''import hashlib, json, pathlib, sys
TABLE = %s
p = pathlib.Path(sys.argv[sys.argv.index("--packet") + 1])
h = hashlib.sha256(p.read_bytes()).hexdigest()
entry = TABLE.get(h)
if entry is None:
    print(json.dumps({"records": 0, "findings": [{"id": "RECORD_ID", "record": "unknown"}]}))
    sys.exit(1)
rc, ids, records = entry
if rc == 2:
    sys.stderr.write("ATTESTATION_ERROR: unreadable packet\\n")
    print(json.dumps({"records": 0, "findings": [{"id": "ATTESTATION_ERROR", "record": ""}]}))
    sys.exit(2)
out = dict(findings=[dict(id=i, record="memo", detail="memorized") for i in ids])
if records is not None:
    out["records"] = records
print(json.dumps(out, sort_keys=True))
sys.exit(rc)
''' % repr(table)
t = work/'memo-oracle.py'; t.write_text(body)
rows = m.score(t, packet_obj, cases, work)
print(json.dumps(dict(passed=sum(r['passed'] for r in rows), total=len(rows),
                       failures=[r['case'] for r in rows if not r['passed']]), indent=1))
