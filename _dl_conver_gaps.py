"""Download missing Conver major-14 and major-16 and update manifest."""
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
                    'prop': 'imageinfo', 'iiprop': 'url', 'iiurlwidth': str(width)})
    pages = data['query']['pages']
    page = next(iter(pages.values()))
    return page['imageinfo'][0]['thumburl']

MISSING = [
    ('major-14', '13 XIII Nicolas Conver Tarot 1760.jpg'),
    ('major-16', 'XVI LA MAISON DE DIEU Nicolas Conver Tarot 1760.jpg'),
]

OUT_DIR = r'C:\rje\dev\tarocchi\data\images\marseille-conver-1761'
MANIFEST_PATH = r'C:\rje\dev\tarocchi\data\images\manifest.json'

m = json.loads(open(MANIFEST_PATH, encoding='utf-8-sig').read())
deck = m['marseille-conver-1761']

for card_id, filename in MISSING:
    print(f"Fetching {filename}...")
    thumb_url = get_thumb_url(filename)
    print(f"  URL: {thumb_url}")
    out_path = os.path.join(OUT_DIR, f'{card_id}.jpg')
    req = urllib.request.Request(thumb_url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=30) as r:
        data_bytes = r.read()
    open(out_path, 'wb').write(data_bytes)
    deck[card_id] = f'data/images/marseille-conver-1761/{card_id}.jpg'
    print(f"  Saved {out_path} ({len(data_bytes)} bytes)")

m['marseille-conver-1761'] = deck
out = json.dumps(m, indent=2, ensure_ascii=False)
open(MANIFEST_PATH, 'w', encoding='utf-8').write(out)
print(f"\nManifest updated. Conver count now: {len(m['marseille-conver-1761'])}")
print("Keys:", sorted(m['marseille-conver-1761'].keys()))
