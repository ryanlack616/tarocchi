"""
_patch_decks2.py — adds Conver 1761, Tarot de Besancon, Oswald Wirth 1889
to historical_decks.json and wires their genealogy edges.
Run once: C:\Python314\python.exe -X utf8 _patch_decks2.py
"""
import json
from pathlib import Path

src = Path("data/historical_decks.json")
d = json.loads(src.read_text(encoding="utf-8"))

# ── New decks ─────────────────────────────────────────────────────────────────

NEW_DECKS = [
    {
        "id": "marseille-conver-1761",
        "name": "Tarot de Marseille (Conver, 1761)",
        "name_it": "Tarot de Marseille — Type II (Conver)",
        "origin_location": "Marseille, France",
        "origin_country": "France",
        "date_earliest": 1761,
        "date_latest": 1761,
        "date_display": "1761 (dated impression)",
        "date_basis": (
            "Date appears printed on the ace of coins face: "
            "'N. Conver M.re Cartier a Marseille 1761.' "
            "One of the few exactly dated Marseille impressions."
        ),
        "date_confidence": "exact",
        "survival_status": "extant",
        "cards_known": 78,
        "cards_original": 78,
        "missing_cards": [],
        "missing_cards_unidentified_count": 0,
        "missing_cards_notes": None,
        "structure": {
            "total_cards": 78,
            "suits": ["cups", "coins", "swords", "batons"],
            "ranks_per_suit": 14,
            "court_cards": ["Valet", "Cavalier", "Reine", "Roi"],
            "trump_cards": 22,
            "notes": (
                "Type II Marseille. Strength at XI, Justice at VIII "
                "(standard Marseille ordering). The Papesse (II) and Pope (V) "
                "are present, distinguishing it from the Besancon variant."
            ),
        },
        "material": ["woodblock", "hand-coloring"],
        "technique": ["relief printing"],
        "language_on_cards": ["French"],
        "patron": None,
        "commissioned_for": None,
        "primary_purpose": "gaming",
        "later_uses": [
            {
                "use": "divination",
                "date_earliest": 1870,
                "notes": (
                    "Adopted by French cartomancers in the 19th century. "
                    "Became the standard reference for Marseille occultists."
                ),
            },
            {
                "use": "restoration_source",
                "date_earliest": 1997,
                "notes": (
                    "Used by Alejandro Jodorowsky and Philippe Camoin as the "
                    "primary source for their 1997 restored Tarot de Marseille "
                    "— the most influential modern Marseille restoration."
                ),
            },
        ],
        "attributions": [
            {
                "role": "publisher_cardmaker",
                "name": "Nicolas Conver",
                "confidence": "confirmed",
                "notes": (
                    "Named on the ace of coins. One of the rare directly "
                    "attributed Marseille productions. Conver was a master "
                    "cardmaker (maitre cartier) of Marseille."
                ),
            }
        ],
        "holdings": [
            {
                "institution": "Bibliotheque nationale de France",
                "city": "Paris",
                "country": "France",
                "cards_held": 78,
                "accession": "Kh-35 (4)",
                "digitized": True,
                "digitization_url": "https://gallica.bnf.fr/",
            }
        ],
        "tags": [
            "Marseille", "woodblock", "Type-II", "complete", "Conver",
            "French", "cartomancy", "gaming", "restoration-source",
        ],
        "transmission_path": (
            "Conver 1761 → 19th-century French cartomancers → "
            "Jodorowsky/Camoin restoration (1997) → contemporary Marseille revival"
        ),
        "iconography_notes": (
            "Type II is distinguished from Type I by subtle but consistent "
            "iconographic refinements: cleaner linework, more standardized "
            "figure proportions, revised color conventions. "
            "The Conver is the definitive Type II exemplar."
        ),
        "significance": (
            "The single most influential surviving Marseille impression. "
            "Jodorowsky and Camoin's 1997 restoration — the most widely used "
            "Marseille deck in contemporary practice — was based directly on "
            "the Conver 1761. Any student of the Marseille tradition is "
            "effectively studying Conver's hand, 263 years later."
        ),
        "sources": [
            "Kaplan, Stuart R. The Encyclopedia of Tarot. Vol. 1. 1978.",
            "Jodorowsky, Alejandro and Camoin, Philippe. The Way of Tarot. 2004.",
            "Decker, Depaulis, Dummett. A Wicked Pack of Cards. 1996.",
        ],
    },
    {
        "id": "tarot-de-besancon",
        "name": "Tarot de Besancon",
        "name_it": "Tarot de Besancon (variante svizzera)",
        "origin_location": "Besancon, France / Switzerland",
        "origin_country": "France",
        "date_earliest": 1650,
        "date_latest": 1850,
        "date_display": "c. 1650–1850 (production span)",
        "date_basis": (
            "First documented Besancon-type impressions from the mid-17th century; "
            "production continued into the 19th century. A regional tradition "
            "with many cardmakers, not a single originating impression."
        ),
        "date_confidence": "medium",
        "survival_status": "extant",
        "cards_known": 78,
        "cards_original": 78,
        "missing_cards": [],
        "missing_cards_unidentified_count": 0,
        "missing_cards_notes": None,
        "structure": {
            "total_cards": 78,
            "suits": ["cups", "coins", "swords", "batons"],
            "ranks_per_suit": 14,
            "court_cards": ["Valet", "Cavalier", "Reine", "Roi"],
            "trump_cards": 22,
            "notes": (
                "The defining feature: trump II (La Papesse) replaced by Juno, "
                "trump V (Le Pape) replaced by Jupiter. All other cards follow "
                "the Marseille woodblock tradition. Substitution avoids "
                "Catholic clergy imagery for Protestant Swiss/German markets."
            ),
        },
        "material": ["woodblock", "hand-coloring"],
        "technique": ["relief printing"],
        "language_on_cards": ["French"],
        "patron": None,
        "commissioned_for": None,
        "primary_purpose": "gaming",
        "later_uses": [],
        "attributions": [
            {
                "role": "regional_tradition",
                "name": "Besancon cardmakers (multiple)",
                "confidence": "confirmed",
                "notes": (
                    "A tradition of production, not a single maker. "
                    "Known cardmakers include Joseph Jerger and others "
                    "in the Besancon and Swiss tradition."
                ),
            }
        ],
        "holdings": [
            {
                "institution": "Bibliotheque nationale de France",
                "city": "Paris",
                "country": "France",
                "cards_held": 78,
                "accession": None,
                "digitized": False,
                "digitization_url": None,
            }
        ],
        "tags": [
            "Marseille-variant", "Swiss", "Besancon", "Juno-Jupiter",
            "Protestant-market", "woodblock", "gaming",
        ],
        "transmission_path": (
            "Marseille woodblock tradition → Swiss/Alsatian cardmakers → "
            "Besancon production → gaming in Swiss, German, and Alsatian markets"
        ),
        "iconography_notes": (
            "The Juno/Jupiter substitution for Papesse/Pope is the sole "
            "structural departure from the Marseille model. Juno typically "
            "holds a scepter and peacock; Jupiter holds a thunderbolt. "
            "Reflects the pragmatics of selling into Protestant markets."
        ),
        "significance": (
            "The most geographically widespread Marseille variant. "
            "Documents how the tarot traveled and adapted to local religious "
            "and political contexts. The Juno/Jupiter substitution is the "
            "earliest documented intentional modification of trump iconography "
            "for market reasons — a precursor to modern 'themed' decks."
        ),
        "sources": [
            "Kaplan, Stuart R. The Encyclopedia of Tarot. Vol. 1. 1978.",
            "Decker, Depaulis, Dummett. A Wicked Pack of Cards. 1996.",
            "Depaulis, Thierry. Tarot, Jeu et Magie. BnF exhibition catalogue. 1984.",
        ],
    },
    {
        "id": "oswald-wirth-1889",
        "name": "Oswald Wirth Tarot (1889)",
        "name_it": "Tarocchi di Oswald Wirth",
        "origin_location": "Paris, France",
        "origin_country": "France",
        "date_earliest": 1889,
        "date_latest": 1889,
        "date_display": "1889",
        "date_basis": (
            "Published 1889 by Oswald Wirth with the support of Stanislas de Guaita. "
            "Limited edition of 350 copies. Major Arcana only; "
            "full 78-card Wirth not published until 1926."
        ),
        "date_confidence": "exact",
        "survival_status": "extant",
        "cards_known": 22,
        "cards_original": 22,
        "missing_cards": [],
        "missing_cards_unidentified_count": 0,
        "missing_cards_notes": (
            "The 1889 publication was 22 Major Arcana only. "
            "Wirth designed the full 78-card deck but published it in 1926 "
            "(Le Tarot des imagiers du Moyen Age). This entry covers the 1889 edition."
        ),
        "structure": {
            "total_cards": 22,
            "suits": [],
            "ranks_per_suit": 0,
            "court_cards": [],
            "trump_cards": 22,
            "notes": (
                "Major Arcana only. Based on the Marseille trump sequence "
                "but overlaid with Kabbalistic, astrological, and Hebrew-letter "
                "attributions per Eliphas Levi's system. The Fool is unnumbered (0), "
                "positioned before The Magician (I)."
            ),
        },
        "material": ["engraving", "hand-coloring"],
        "technique": ["intaglio"],
        "language_on_cards": ["French"],
        "patron": "Stanislas de Guaita",
        "commissioned_for": "Ordre Kabbalistique de la Rose-Croix",
        "primary_purpose": "esoteric",
        "later_uses": [
            {
                "use": "divination",
                "date_earliest": 1920,
                "notes": "Widely adopted by French occultists and cartomancers in the early 20th century.",
            }
        ],
        "attributions": [
            {
                "role": "artist_designer",
                "name": "Oswald Wirth",
                "confidence": "confirmed",
                "notes": (
                    "Swiss-French occultist, freemason, and artist. "
                    "Designed the deck as a visual compendium of Levi's "
                    "tarot-Kabbala synthesis."
                ),
            },
            {
                "role": "esoteric_advisor",
                "name": "Stanislas de Guaita",
                "confidence": "confirmed",
                "notes": (
                    "French Rosicrucian occultist who sponsored and guided the project. "
                    "De Guaita provided the Kabbalistic framework."
                ),
            },
        ],
        "holdings": [
            {
                "institution": "Bibliotheque nationale de France",
                "city": "Paris",
                "country": "France",
                "cards_held": 22,
                "accession": None,
                "digitized": False,
                "digitization_url": None,
            },
            {
                "institution": "Various private collections",
                "city": None,
                "country": None,
                "cards_held": 22,
                "accession": None,
                "digitized": False,
                "digitization_url": None,
            },
        ],
        "tags": [
            "Major-Arcana-only", "esoteric", "Kabbalistic", "Rosicrucian",
            "Marseille-derived", "Golden-Age-occultism", "Wirth", "French",
        ],
        "transmission_path": (
            "Marseille iconography + Levi Kabbalistic system → "
            "Wirth 1889 Major Arcana → French occultist tradition → "
            "partial influence on Rider-Waite-Smith → Wirth 1926 full deck"
        ),
        "iconography_notes": (
            "Wirth retained the Marseille compositions as structural foundation "
            "but inscribed each card with Hebrew letters, astrological glyphs, "
            "and Kabbalistic correspondences. The Fool is explicitly card 0. "
            "First deck where esoteric attributions are visually integrated "
            "rather than added in a companion text."
        ),
        "significance": (
            "The bridge between the French occultist Marseille reinterpretation "
            "(Levi, de Guaita) and the English Golden Dawn tradition (Waite, Crowley). "
            "Wirth's visual language — Marseille structure with integrated Kabbalistic "
            "notation — was a direct precursor to the RWS approach. "
            "Waite knew Wirth's work; the Fool-as-zero treatment is the clearest shared marker."
        ),
        "sources": [
            "Wirth, Oswald. Le Tarot des imagiers du Moyen Age. 1926.",
            "Decker, Depaulis, Dummett. A Wicked Pack of Cards. 1996.",
        ],
    },
]

# ── New genealogy edges ───────────────────────────────────────────────────────

NEW_EDGES = [
    {
        "from": "catelin-geoffroy-1557",
        "to": "marseille-conver-1761",
        "relation": "ancestor_via_woodblock_tradition",
        "notes": (
            "Conver 1761 is the Type II culmination of the Marseille woodblock tradition "
            "that begins with the Geoffroy 1557 (Type I). "
            "204 years of continuous cardmaking in the Lyonnaise/Marseillaise tradition."
        ),
    },
    {
        "from": "tarot-de-marseille-dodal",
        "to": "marseille-conver-1761",
        "relation": "parallel_workshop_tradition",
        "notes": (
            "Both are Marseille productions from the same woodblock tradition. "
            "Dodal (c. 1701) is Type I; Conver (1761) is Type II. "
            "Type II refines Type I iconography without structural change."
        ),
    },
    {
        "from": "marseille-conver-1761",
        "to": "rider-waite-smith",
        "relation": "reaction_against",
        "notes": (
            "Waite explicitly rejected the Marseille unillustrated pip tradition. "
            "The Conver 1761 — the definitive Type II Marseille — "
            "is among the specific decks he was reacting against."
        ),
    },
    {
        "from": "tarot-de-marseille-dodal",
        "to": "tarot-de-besancon",
        "relation": "ancestor_via_woodblock_tradition",
        "notes": (
            "The Besancon variant descends directly from the Marseille woodblock tradition. "
            "The Juno/Jupiter substitution is the only structural departure; "
            "all other iconography follows the Marseille program."
        ),
    },
    {
        "from": "marseille-conver-1761",
        "to": "tarot-de-besancon",
        "relation": "parallel_regional_variant",
        "notes": (
            "Contemporary productions from the same Marseille woodblock tradition. "
            "Conver is Type II (Papesse/Pope present); "
            "Besancon replaces them with Juno/Jupiter for Protestant markets."
        ),
    },
    {
        "from": "tarot-de-marseille-dodal",
        "to": "oswald-wirth-1889",
        "relation": "iconographic_source",
        "notes": (
            "Wirth took the Marseille trump sequence and iconographic program "
            "as his structural foundation, then overlaid Levi's Kabbalistic attributions."
        ),
    },
    {
        "from": "oswald-wirth-1889",
        "to": "golden-dawn-corpus",
        "relation": "parallel_esoteric_tradition",
        "notes": (
            "Wirth (Paris, 1889) and the Golden Dawn (London, 1888-1900) represent "
            "parallel contemporaneous esoterization of the tarot. "
            "Both worked from Levi; both used Kabbalistic attributions."
        ),
    },
    {
        "from": "oswald-wirth-1889",
        "to": "rider-waite-smith",
        "relation": "ancestor",
        "notes": (
            "Waite was aware of Wirth's work. Wirth established the model of a tarot "
            "where esoteric attributions are visually integrated into the card designs "
            "— the approach Waite and Smith then extended to the Minor Arcana."
        ),
    },
]

# ── Apply ─────────────────────────────────────────────────────────────────────

existing_ids = {deck["id"] for deck in d["decks"]}
for deck in NEW_DECKS:
    if deck["id"] not in existing_ids:
        d["decks"].append(deck)
        print(f"  Added deck: {deck['id']}")
    else:
        print(f"  Skip (exists): {deck['id']}")

existing_edges = {(e["from"], e["to"]) for e in d["genealogy"]}
for edge in NEW_EDGES:
    k = (edge["from"], edge["to"])
    if k not in existing_edges:
        d["genealogy"].append(edge)
        print(f"  Added edge: {k[0]} → {k[1]}")
    else:
        print(f"  Skip edge (exists): {k[0]} → {k[1]}")

src.write_text(json.dumps(d, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"\nWrote {len(d['decks'])} decks, {len(d['genealogy'])} edges → historical_decks.json")
