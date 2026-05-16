"""Find missing Conver major-14 (Death) and major-16 (Tower) on Commons."""
import json, urllib.request, urllib.parse, os

API = 'https://commons.wikimedia.org/w/api.php'
HEADERS = {'User-Agent': 'tarocchi-dl/2.0 (tarocchi.help)'}

def api_get(params):
    url = API + '?' + urllib.parse.urlencode({'format': 'json', **params})
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=15) as r:
        return json.loads(r.read())

for term in [
    'Nicolas Conver Tarot Death 1760',
    'Nicolas Conver Tarot Tower 1760',
    'Tarot de Marseille Death Conver',
    'Tarot de Marseille Tower Conver',
    'Conver 1760 XIII',
    'Conver 1760 XVI',
    'Conver 1760 la mort',
    'Conver 1760 maison dieu',
]:
    data = api_get({'action': 'query', 'list': 'search', 'srnamespace': '6',
                    'srsearch': term, 'srlimit': '5'})
    results = [r['title'] for r in data['query']['search']]
    if results:
        print(f"\n{term}:")
        for r in results:
            print(' ', r)
