import json
m = json.loads(open(r'C:\rje\dev\tarocchi\data\images\manifest.json', encoding='utf-8-sig').read())
c = m['marseille-conver-1761']
print("CONVER keys:", sorted(c.keys()))
print()
# RWS keys
r = m['rider-waite-smith']
print("RWS keys:", sorted(r.keys()))
print("RWS count:", len(r))
