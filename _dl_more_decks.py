"""
_dl_more_decks.py — Grab what we can from Wikimedia Commons for decks
not yet imaged. Public-domain only (pre-1930 where possible).

Target decks (by priority / feasibility):
  1.  sola-busca                   — Commons category, full 78-card extant deck
  2.  visconti-di-modrone          — Cary-Yale Beinecke, category
  3.  charles-vi                   — BnF "Charles VI" tarot, category
  4.  cary-sheet-c1500             — Cary Sheet Beinecke
  5.  rosenwald-sheet-c1500        — Rosenwald NGA sheets
  6.  tarot-de-marseille-noblet    — Noblet 1650
  7.  jacques-vieville-c1650       — Vieville 1650
  8.  tarocchino-mitelli-1664      — Mitelli engravings
  9.  minchiate-fiorentine         — 18th c. Minchiate
  10. tarot-de-besancon            — Besançon
  11. tarot-de-marseille-dodal     — Dodal
  12. 1jj-swiss-c1831              — 1JJ Swiss
  13. etteilla-grand-etteilla-1789 — Etteilla I
  14. madenie-1709                 — Madenié Dijon
  15. papus-tarot-1889             — Papus engravings

Strategy: for each deck, try (category) + (search query). Download everything
that's a real image file. Use major-NN card_id when we can parse a number or
a canonical trump name from the filename; otherwise card-NNN sequential.

Idempotent — skips files already downloaded; preserves existing manifest entries.
"""
import json, re, time, urllib.request, urllib.parse, urllib.error
from pathlib import Path

OUT   = Path("data/images")
MAN   = OUT / "manifest.json"
W     = 300
DELAY = 2.0   # base delay between every Commons request
BACKOFF_WAITS = [90, 180, 300]  # seconds to wait on 429, then give up

API = "https://commons.wikimedia.org/w/api.php"
UA  = "tarocchi-dl/3.0 (tarocchi.help research bot; contact ryan at tarocchi.help)"
IMG_EXTS = {".jpg", ".jpeg", ".png", ".tif", ".tiff", ".webp"}

# ─── API helpers ──────────────────────────────────────────────────────────────

def _fetch_with_backoff(url, timeout=25):
    """urlopen wrapper with 429 exponential backoff."""
    last_err = None
    for wait in [0] + BACKOFF_WAITS:
        if wait:
            print(f"      [429] sleeping {wait}s …", flush=True)
            time.sleep(wait)
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            last_err = e
            if e.code != 429:
                raise
        except Exception as e:
            last_err = e
            raise
    raise last_err

def api_get(params):
    url = API + "?" + urllib.parse.urlencode({"format": "json", **params})
    return json.loads(_fetch_with_backoff(url))

def thumb_url(filename, width=W):
    try:
        data = api_get({
            "action": "query",
            "titles": f"File:{filename}",
            "prop": "imageinfo",
            "iiprop": "url",
            "iiurlwidth": width,
        })
        for page in data["query"]["pages"].values():
            ii = page.get("imageinfo", [])
            if ii:
                return ii[0].get("thumburl") or ii[0].get("url")
    except Exception as e:
        print(f"      (thumb err) {e}")
    return None

def category_files(cat, recurse=False):
    """All filenames from a Commons category. recurse=True adds subcategories (one level)."""
    try:
        files, cont = [], {}
        while True:
            params = {
                "action": "query",
                "list": "categorymembers",
                "cmtitle": f"Category:{cat}",
                "cmtype": "file",
                "cmlimit": "100",
                **cont,
            }
            data = api_get(params)
            files += [m["title"][5:] for m in data["query"]["categorymembers"]]
            time.sleep(DELAY)
            if "continue" not in data:
                break
            cont = data["continue"]
        if recurse:
            # find subcats
            subcats, cont = [], {}
            while True:
                params = {
                    "action": "query",
                    "list": "categorymembers",
                    "cmtitle": f"Category:{cat}",
                    "cmtype": "subcat",
                    "cmlimit": "50",
                    **cont,
                }
                data = api_get(params)
                subcats += [m["title"][9:] for m in data["query"]["categorymembers"]]  # strip "Category:"
                if "continue" not in data:
                    break
                cont = data["continue"]
            for sub in subcats:
                try:
                    files += category_files(sub, recurse=False)
                except Exception as e:
                    print(f"    subcat err {sub}: {e}")
        return list(dict.fromkeys(files))
    except Exception as e:
        print(f"    category err {cat}: {e}")
        return []

def search_files(query, limit=100):
    try:
        files, cont = [], {}
        while True:
            params = {
                "action": "query",
                "list": "search",
                "srsearch": query,
                "srnamespace": "6",
                "srlimit": min(limit, 50),
                **cont,
            }
            data = api_get(params)
            batch = data["query"]["search"]
            files += [r["title"][5:] for r in batch]
            if len(files) >= limit or "continue" not in data or not batch:
                break
            cont = data["continue"]
            time.sleep(DELAY)
        return files[:limit]
    except Exception as e:
        print(f"    search err '{query}': {e}")
        return []

def download(url, dest):
    dest.write_bytes(_fetch_with_backoff(url, timeout=60))

def dl_one(fn, card_id, deck_dir, deck_id):
    # Pick extension from source to preserve it
    src_ext = Path(fn).suffix.lower()
    # Commons thumburl delivers jpg for most images; keep .jpg consistently
    ext = ".jpg" if src_ext in {".tif", ".tiff", ".webp"} else (src_ext or ".jpg")
    if ext not in {".jpg", ".jpeg", ".png"}:
        ext = ".jpg"
    dest = deck_dir / f"{card_id}{ext}"
    if dest.exists():
        return card_id, f"data/images/{deck_id}/{dest.name}"
    url = thumb_url(fn)
    if not url:
        time.sleep(DELAY)
        return None
    try:
        download(url, dest)
    except Exception as e:
        print(f"      DL err: {e}")
        time.sleep(DELAY)
        return None
    time.sleep(DELAY)
    return card_id, f"data/images/{deck_id}/{dest.name}"

# ─── Name-matching helpers ─────────────────────────────────────────────────────

# Canonical trump names (many languages) → major-NN
TRUMP_MATCHERS = [
    # (regex, major-NN)
    (r"\b(fool|matto|mat|der\s*narr|le\s*fou)\b", "major-00"),
    (r"\b(bagatto|bagatella|bateleur|magician|juggler|mago)\b", "major-01"),
    (r"\b(popess|papess|papesse|high\s*priestess|papessa|priestess)\b", "major-02"),
    (r"\b(empress|imp[eé]ratrice|imperatrice)\b", "major-03"),
    (r"\b(emperor|empereur|imperatore)\b", "major-04"),
    (r"\b(pope|papa|hierophant|papus|pape\b)\b", "major-05"),
    (r"\b(lovers|amoureux|amanti|innamorati)\b", "major-06"),
    (r"\b(chariot|char\b|carro)\b", "major-07"),
    (r"\b(justice|giustizia)\b", "major-08"),
    (r"\b(hermit|ermite|eremita)\b", "major-09"),
    (r"(wheel\s*of\s*fortune|roue\s*de\s*fortune|ruota\s*di\s*fortuna|fortuna)", "major-10"),
    (r"\b(strength|force|la\s*forza|forza\b|fortitude|fortezza)\b", "major-11"),
    (r"(hanged\s*man|pendu|appeso|impiccato)", "major-12"),
    (r"\b(death|la\s*mort|mort\b|morte)\b", "major-13"),
    (r"\b(temperance|temp[eé]rance|temperanza)\b", "major-14"),
    (r"\b(devil|diable|diavolo)\b", "major-15"),
    (r"(tower|maison\s*dieu|tour|torre|casa\s*de\s*dio)", "major-16"),
    (r"\b(star|[eé]toile|stella)\b", "major-17"),
    (r"\b(moon|lune|luna)\b", "major-18"),
    (r"\b(sun|soleil|sole)\b", "major-19"),
    (r"\b(judgement|judgment|jugement|giudizio|angel)\b", "major-20"),
    (r"\b(world|monde|mondo)\b", "major-21"),
]

ROMAN_MAP = {
    "XXI":21,"XX":20,"XIX":19,"XVIII":18,"XVII":17,"XVI":16,"XV":15,"XIV":14,
    "XIII":13,"XII":12,"XI":11,"X":10,"IX":9,"VIII":8,"VII":7,"VI":6,"V":5,
    "IV":4,"III":3,"II":2,"I":1,"VIIII":9,"XIIII":14,"XVIIII":19,
}

def parse_card_id(fn):
    """Return major-NN if we can detect a trump, else None."""
    stem = Path(fn).stem
    s = " " + stem + " "
    # Leading 2-digit number like "05 CardName"
    m = re.match(r"^\s*(\d{1,2})\b", stem)
    if m:
        n = int(m.group(1))
        if 0 <= n <= 21:
            return f"major-{n:02d}"
    # Roman numerals as standalone token
    up = stem.upper()
    for rom, n in sorted(ROMAN_MAP.items(), key=lambda x: -len(x[0])):
        if re.search(r"(^|[^A-Z])" + re.escape(rom) + r"([^A-Z]|$)", up):
            if 0 <= n <= 21:
                return f"major-{n:02d}"
    # Trump name regex
    low = stem.lower()
    for pat, cid in TRUMP_MATCHERS:
        if re.search(pat, low):
            return cid
    return None

# ─── Per-deck config ──────────────────────────────────────────────────────────
# Each entry: (deck_id, [categories], [search queries], options)
# options: recurse_subcats=True to descend one level of subcats

DECKS = [
    ("sola-busca",
        ["Sola-Busca_tarocchi"],
        ["Sola Busca tarot", "Sola-Busca tarocchi"],
        {"recurse": True}),
    ("visconti-di-modrone",
        ["Cary-Yale_Visconti_tarot_deck", "Visconti_di_Modrone_tarot_deck"],
        ["Cary-Yale Visconti tarot", "Visconti di Modrone tarot"],
        {"recurse": True}),
    ("charles-vi",
        ["Charles_VI_tarot_deck", "Gringonneur_tarot"],
        ["Charles VI tarot", "Gringonneur tarot"],
        {"recurse": True}),
    ("tarot-de-marseille-noblet",
        ["Jean_Noblet_tarot_deck", "Noblet_Tarot"],
        ["Jean Noblet tarot 1650"],
        {"recurse": True}),
    ("jacques-vieville-c1650",
        ["Jacques_Vi[eé]ville_tarot_deck"],
        ["Jacques Vieville tarot", "Jacques Viéville tarot"],
        {"recurse": True}),
    ("tarocchino-mitelli-1664",
        ["Giuseppe_Maria_Mitelli_tarocchino", "Tarocchino_Mitelli"],
        ["Mitelli tarocchino", "Giuseppe Maria Mitelli tarocchino"],
        {"recurse": True}),
    ("minchiate-fiorentine",
        ["Minchiate"],
        ["Minchiate fiorentine tarot", "Minchiate Etruria"],
        {"recurse": True}),
    ("tarot-de-besancon",
        ["Tarot_de_Besan[çc]on"],
        ["Tarot de Besançon", "Tarot de Besancon"],
        {"recurse": True}),
    ("tarot-de-marseille-dodal",
        ["Jean_Dodal_tarot_deck"],
        ["Jean Dodal tarot 1701", "Dodal tarot de Marseille"],
        {"recurse": True}),
    ("1jj-swiss-c1831",
        ["1JJ_Swiss_tarot", "AGM%C3%BCller_tarot"],
        ["1JJ Swiss tarot", "AGMüller tarot", "Müller Schaffhausen tarot"],
        {"recurse": True}),
    ("etteilla-grand-etteilla-1789",
        ["Etteilla_tarot"],
        ["Etteilla tarot 1789", "Grand Etteilla tarot"],
        {"recurse": True}),
    ("madenie-1709",
        ["Pierre_Maden[ié]e_tarot"],
        ["Pierre Madenié tarot Dijon", "Madenié 1709"],
        {"recurse": True}),
    ("papus-tarot-1889",
        ["Papus_tarot", "G%C3%A9rard_Encausse_tarot"],
        ["Papus Tarot des Bohémiens", "Encausse tarot 1889"],
        {"recurse": True}),
    ("rosenwald-sheet-c1500",
        [],
        ["Rosenwald tarot sheet", "Rosenwald playing cards Italian"],
        {"recurse": False}),
    ("cary-sheet-c1500",
        [],
        ["Cary sheet tarot", "Cary-Yale tarot uncut sheet"],
        {"recurse": False}),
]

# ─── Download loop ────────────────────────────────────────────────────────────

def do_deck(deck_id, cats, queries, opts, full_manifest):
    deck_dir = OUT / deck_id
    deck_dir.mkdir(parents=True, exist_ok=True)
    existing = full_manifest.get(deck_id, {})
    manifest = dict(existing)

    all_files = []
    for cat in cats:
        cat_clean = urllib.parse.unquote(cat)
        print(f"  CAT: {cat_clean}")
        got = category_files(cat_clean, recurse=opts.get("recurse", False))
        print(f"    +{len(got)} files")
        all_files += got
    for q in queries:
        print(f"  SEARCH: {q}")
        got = search_files(q, limit=100)
        print(f"    +{len(got)} files")
        all_files += got
    # Dedup, keep only images
    all_files = [f for f in dict.fromkeys(all_files) if Path(f).suffix.lower() in IMG_EXTS]
    # Filter out category/icon junk
    all_files = [f for f in all_files if not re.search(r"\b(commons[-_ ]logo|wikimedia|icon|flag)\b", f, re.I)]
    print(f"  TOTAL unique image files: {len(all_files)}")

    card_counter = 1
    used_majors = {v for k, v in manifest.items() if k.startswith("major-")}
    for fn in all_files:
        cid = parse_card_id(fn)
        if cid and cid in manifest:
            # Already have this major — skip
            continue
        if not cid:
            # Find next free card-NNN
            while f"card-{card_counter:03d}" in manifest:
                card_counter += 1
            cid = f"card-{card_counter:03d}"
            card_counter += 1
        print(f"    {cid} ← {fn[:70]}")
        r = dl_one(fn, cid, deck_dir, deck_id)
        if r:
            manifest[r[0]] = r[1]
        # cap per deck to keep things sane
        if len(manifest) >= 120:
            print(f"    (cap reached at 120)")
            break

    full_manifest[deck_id] = manifest
    return manifest

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    if MAN.exists():
        full_manifest = json.loads(MAN.read_text(encoding="utf-8"))
    else:
        full_manifest = {}

    summary = {}
    for deck_id, cats, queries, opts in DECKS:
        print(f"\n══ {deck_id} ══")
        before = len(full_manifest.get(deck_id, {}))
        try:
            m = do_deck(deck_id, cats, queries, opts, full_manifest)
        except Exception as e:
            print(f"  DECK ERR: {e}")
            m = full_manifest.get(deck_id, {})
        after = len(m)
        summary[deck_id] = (before, after)
        # Write manifest after every deck (crash-safe)
        MAN.write_text(json.dumps(full_manifest, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"  {deck_id}: {before} → {after}")

    print("\n══ SUMMARY ══")
    for d, (b, a) in summary.items():
        delta = a - b
        print(f"  {d:35s} {b:3d} → {a:3d}  (+{delta})")
    print(f"\nManifest at {MAN}")

if __name__ == "__main__":
    main()
