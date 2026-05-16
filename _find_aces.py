"""Find Ace of Swords and Ace of Pentacles RWS images on Commons."""
import json, urllib.request, urllib.parse

API = 'https://commons.wikimedia.org/w/api.php'
HEADERS = {'User-Agent': 'tarocchi-dl/2.0 (tarocchi.help)'}

def api_get(params):
    url = API + '?' + urllib.parse.urlencode({'format': 'json', **params})
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=15) as r:
        return json.loads(r.read())

for term in ['Ace of Swords Rider-Waite', 'Ace of Pentacles Rider-Waite', 'Ace of Coins Rider-Waite']:
    data = api_get({'action': 'query', 'list': 'search', 'srnamespace': '6',
                    'srsearch': term, 'srlimit': '5'})
    print(f"\nSearch: {term}")
    for r in data['query']['search']:
        print(' ', r['title'])
