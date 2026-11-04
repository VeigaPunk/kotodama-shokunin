import pathlib,json,sys
n=pathlib.Path(sys.argv[sys.argv.index('--packet')+1]).stem
print(json.dumps({'records':5,'findings':[]}))
