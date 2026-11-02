"""Probe Wikimedia Commons for missing RWS Aces and clean Conver manifest."""
import json, urllib.request, urllib.parse, os

API = 'https://commons.wikimedia.org/w/api.php'
HEADERS = {'User-Agent': 'tarocchi-dl/2.0 (tarocchi.help)'}

def api_get(params):
    url = API + '?' + urllib.parse.urlencode({'format': 'json', **params})
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=15) as r:
        return json.loads(r.read())

# ── Probe Geldard category for Ace of Swords / Ace of Pentacles ──
print("Scanning Geldard category for Aces...")
data = api_get({'action': 'query', 'list': 'categorymembers',
                'cmtitle': 'Category:Rider-Waite-Smith_tarot_deck_(Geldard)',
                'cmtype': 'file', 'cmlimit': '500'})
files = [m['title'].replace('File:', '') for m in data['query']['categorymembers']]

for f in sorted(files):
    if 'Ace' in f or 'ace' in f:
        print(' ', f)

# ── Clean Conver manifest ──────────────────────────────────────────
print("\nCleaning Conver manifest...")
manifest_path = r'C:\rje\dev\tarocchi\data\images\manifest.json'
m = json.loads(open(manifest_path, encoding='utf-8-sig').read())

conver = m['marseille-conver-1761']
keep_keys = {k for k in conver if k.startswith('major-') or k in ('card-001','card-002','card-005','card-023')}
noise_keys = {k for k in conver if k not in keep_keys}

print(f"Keeping {len(keep_keys)} entries, removing {len(noise_keys)} noise entries")
m['marseille-conver-1761'] = {k: v for k, v in conver.items() if k in keep_keys}

out = json.dumps(m, indent=2, ensure_ascii=False)
open(manifest_path, 'w', encoding='utf-8').write(out)
print("Manifest saved.")
print("Conver keys now:", sorted(m['marseille-conver-1761'].keys()))
