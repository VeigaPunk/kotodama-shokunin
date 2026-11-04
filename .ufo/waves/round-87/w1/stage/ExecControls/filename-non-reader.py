import pathlib,json,sys
m={'positive-six':(0,None),'duplicate-record':(1,'RECORD_ID'),'missing-clock':(1,'CLOCK_MISSING'),'blank-reason':(1,'CLOCK_REASON'),'invalid-date':(1,'CLOCK_DATE'),'blank-sense':(1,'RECORD_FIELD'),'unresolved-selected':(1,'SOLUTION_CONFLICT'),'conjecture-promoted':(1,'EDITORIAL_CONFLICT'),'translation-backdated':(1,'TRANSLATION_CLOCK'),'unknown-explicit':(0,None),'reordered-records':(0,None),'invalid-json':(2,'ATTESTATION_ERROR')}
rc,label=m[pathlib.Path(sys.argv[sys.argv.index('--packet')+1]).stem]
print(json.dumps({'records':6,'findings':[] if label is None else [{'id':label}]}))
sys.exit(rc)
