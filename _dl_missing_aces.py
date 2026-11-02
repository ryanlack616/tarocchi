"""Download the 2 missing RWS aces and add to manifest."""
import json, urllib.request, urllib.parse, os

API = 'https://commons.wikimedia.org/w/api.php'
HEADERS = {'User-Agent': 'tarocchi-dl/2.0 (tarocchi.help)'}

def api_get(params):
    url = API + '?' + urllib.parse.urlencode({'format': 'json', **params})
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=15) as r:
        return json.loads(r.read())

def get_thumb_url(filename, width=300):
    data = api_get({'action': 'query', 'titles': f'File:{filename}',
                    'prop': 'imageinfo', 'iiprop': 'url',
                    'iiurlwidth': str(width)})
    pages = data['query']['pages']
    page = next(iter(pages.values()))
    return page['imageinfo'][0]['thumburl']

MISSING = [
    ('pents-01', 'RWS1909 - Pentacles 01.jpeg'),
    ('swords-01', 'RWS1909 - Swords 01.jpeg'),
]

OUT_DIR = r'C:\rje\dev\tarocchi\data\images\rider-waite-smith'
MANIFEST_PATH = r'C:\rje\dev\tarocchi\data\images\manifest.json'

m = json.loads(open(MANIFEST_PATH, encoding='utf-8-sig').read())
rws = m['rider-waite-smith']

for card_id, filename in MISSING:
    print(f"Fetching {filename}...")
    thumb_url = get_thumb_url(filename)
    print(f"  URL: {thumb_url}")
    out_path = os.path.join(OUT_DIR, f'{card_id}.jpg')
    req = urllib.request.Request(thumb_url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=30) as r:
        data = r.read()
    open(out_path, 'wb').write(data)
    rws[card_id] = f'data/images/rider-waite-smith/{card_id}.jpg'
    print(f"  Saved {out_path} ({len(data)} bytes)")

m['rider-waite-smith'] = rws
out = json.dumps(m, indent=2, ensure_ascii=False)
open(MANIFEST_PATH, 'w', encoding='utf-8').write(out)
print(f"\nManifest updated. RWS count now: {len(m['rider-waite-smith'])}")
