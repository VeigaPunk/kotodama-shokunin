import pathlib,json,sys
n=pathlib.Path(sys.argv[sys.argv.index('--packet')+1]).stem
if n=='invalid-json':
 print('not JSON: NOT_ATTESTATION_ERROR_SUFFIX',file=sys.stderr)
 sys.exit(2)
labels=['RECORD_ID','CLOCK_MISSING','CLOCK_REASON','CLOCK_DATE','RECORD_FIELD','SOLUTION_CONFLICT','EDITORIAL_CONFLICT','TRANSLATION_CLOCK']
pos=n in ['positive-six','unknown-explicit','reordered-records']
print(json.dumps({'records':6 if pos else -999,'findings':[] if pos else [{'id':x,'record':'NONEXISTENT','detail':'fabricated'} for x in labels]}))
sys.exit(0 if pos else 1)
