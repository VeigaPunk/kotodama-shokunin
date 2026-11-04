import pathlib,json,sys
n=pathlib.Path(sys.argv[sys.argv.index('--packet')+1]).stem
m={'duplicate-record':'RECORD_ID','missing-clock':'CLOCK_MISSING','blank-reason':'CLOCK_REASON','invalid-date':'CLOCK_DATE','blank-sense':'RECORD_FIELD','unresolved-selected':'SOLUTION_CONFLICT','conjecture-promoted':'EDITORIAL_CONFLICT','translation-backdated':'TRANSLATION_CLOCK','invalid-json':'ATTESTATION_ERROR'}
label=m.get(n)
print(json.dumps({'records':6,'findings':[] if label is None else [{'id':label}]}))
sys.exit(2 if n=='invalid-json' else 1 if label else 0)
