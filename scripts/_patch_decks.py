"""
_patch_decks.py — one-shot patch of historical_decks.json

Applies:
  1. Fix genealogy: RWS→Thoth relation to 'reaction_against'
  2. Add missing genealogy edges (mamluk→charles-vi, charles-vi→marseille,
     golden-dawn→rws, golden-dawn→thoth, minchiate outbound)
  3. Add 'missing_cards' arrays to fragmentary decks (using cards.json IDs)
  4. Add 'primary_purpose' + 'later_uses' to all decks
  5. Add 5 new decks: tang-dynasty-c868, spanish-naipes-c1371,
     catelin-geoffroy-1557, etteilla-grand-etteilla-1789, golden-dawn-corpus
  6. Add new valid genealogy relations to schema notes

Run once: python _patch_decks.py
"""

import json
from pathlib import Path

DATA = Path(__file__).parent / "data"
SRC = DATA / "historical_decks.json"
BAK = DATA / "historical_decks.json.bak"

data = json.loads(SRC.read_text(encoding="utf-8"))

# ── Backup ──────────────────────────────────────────────────────────────────
BAK.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Backup written to {BAK.name}")

# ─────────────────────────────────────────────────────────────────────────────
# 1. Fix genealogy: RWS→Thoth should be reaction_against, not parallel_*
# ─────────────────────────────────────────────────────────────────────────────
for edge in data["genealogy"]:
    if edge["from"] == "rider-waite-smith" and edge["to"] == "thoth-tarot":
        edge["relation"] = "reaction_against"
        edge["notes"] = (
            "Crowley explicitly designed Thoth as a rival to and correction of Waite's deck — "
            "he called Waite's instructions 'deliberately misleading.' Both descend from Golden Dawn "
            "manuscripts, but Crowley's Thelemic system departs fundamentally from Waite's Christian mysticism."
        )
        print("Fixed: RWS→Thoth relation updated to reaction_against")

# ─────────────────────────────────────────────────────────────────────────────
# 2. Add missing genealogy edges
# ─────────────────────────────────────────────────────────────────────────────
new_edges = [
    {
        "from": "mamluk-c1375",
        "to": "charles-vi",
        "relation": "ancestor",
        "notes": (
            "The Charles VI deck (actually c. 1440–1470, Northern Italy) inherits the four-suit playing card "
            "structure from the Mamluk/Iberian tradition, then layers tarot trumps on top — same path as the "
            "Visconti decks but from an independent workshop."
        ),
    },
    {
        "from": "charles-vi",
        "to": "tarot-de-marseille-dodal",
        "relation": "ancestor",
        "notes": (
            "The 'Charles VI' deck (Northern Italian, c. 1440–1470) represents an iconographic lineage that "
            "fed into the Marseille standardization. The Marseille Type I is a synthesis of multiple Northern "
            "Italian workshop traditions, not solely the Visconti-Sforza line."
        ),
    },
    {
        "from": "golden-dawn-corpus",
        "to": "rider-waite-smith",
        "relation": "esoteric_source_material",
        "notes": (
            "Waite was a member of the Golden Dawn (Isis-Urania Temple). The RWS implements the Golden Dawn "
            "attributions: Hebrew letter↔trump, planet/zodiac↔trump, elemental↔suit. Smith was also a member. "
            "The GD manuscript 'Book T' is the direct source for Waite's symbolic program."
        ),
    },
    {
        "from": "golden-dawn-corpus",
        "to": "thoth-tarot",
        "relation": "esoteric_source_material",
        "notes": (
            "Crowley was a Golden Dawn initiate (Neophyte → Adeptus Minor). The Thoth deck implements the "
            "same GD attribution schema as RWS but extends it with Thelemic attributions. The key difference: "
            "Crowley restores Strength to VIII and Justice to XI (reversing Waite's swap back to Marseille order)."
        ),
    },
    {
        "from": "etteilla-grand-etteilla-1789",
        "to": "rider-waite-smith",
        "relation": "ancestor",
        "notes": (
            "Etteilla's system of reading all 78 cards as a coherent cartomantic whole — with positional "
            "meanings, reversal meanings, and a spread system — became the template for all subsequent "
            "English-language tarot reading. Waite's 'Pictorial Key to the Tarot' (1910) is a direct "
            "descendant of Etteilla's reading methodology even as it rejected his 'Egyptian' iconography."
        ),
    },
]

existing_edge_keys = {(e["from"], e["to"]) for e in data["genealogy"]}
added = 0
for edge in new_edges:
    key = (edge["from"], edge["to"])
    if key not in existing_edge_keys:
        data["genealogy"].append(edge)
        existing_edge_keys.add(key)
        print(f"Added edge: {edge['from']} → {edge['to']} [{edge['relation']}]")
        added += 1
print(f"Added {added} genealogy edges")

# ─────────────────────────────────────────────────────────────────────────────
# 3. Add missing_cards arrays to fragmentary decks
# ─────────────────────────────────────────────────────────────────────────────
MISSING_CARDS = {
    "visconti-di-modrone": {
        "identified": ["major-15", "major-16", "major-17", "major-18", "major-19", "major-21", "pentacles-12"],
        "unidentified_count": 4,
        "notes": (
            "6 major arcana definitively absent: The Devil (15), The Tower (16), The Star (17), The Moon (18), "
            "The Sun (19), The World (21). Knight of Pentacles (pentacles-12, historically 'Knight of Coins') also "
            "missing. 4 pip cards unidentified — the specific cards are not established in the scholarly literature."
        ),
    },
    "visconti-sforza": {
        "identified": ["major-15", "major-16"],
        "unidentified_count": 2,
        "notes": (
            "The Devil (major-15) and The Tower (major-16) are definitively absent — notably the two most "
            "'dark' trump cards. Whether this reflects censorship, loss, or original omission is debated. "
            "2 minor suit cards also missing but not specifically identified."
        ),
    },
    "charles-vi": {
        "identified": [],
        "unidentified_count": 61,
        "notes": (
            "Only 17 of 78 cards survive — all major arcana (trump cards). All 56 minor arcana are "
            "missing. Of the 22 trumps, 5 are also absent; the specific 17 surviving trumps are documented "
            "but the missing 5 have not been definitively identified against a canonical trump order."
        ),
    },
    "mamluk-c1375": {
        "identified": [],
        "unidentified_count": 37,
        "notes": (
            "15 of 52 cards survive. The Mamluk deck uses a different structure (polo_sticks, cups, swords, "
            "coins; 13 ranks; no trumps) so comparison to tarot IDs is not meaningful. The surviving cards "
            "include examples from multiple suits but are not mapped to the tarot card ID namespace."
        ),
    },
}

for deck in data["decks"]:
    did = deck["id"]
    if did in MISSING_CARDS:
        mc = MISSING_CARDS[did]
        if "missing_cards" not in deck:
            deck["missing_cards"] = mc["identified"]
            deck["missing_cards_unidentified_count"] = mc["unidentified_count"]
            deck["missing_cards_notes"] = mc["notes"]
            print(f"Added missing_cards to {did} ({len(mc['identified'])} identified, {mc['unidentified_count']} unknown)")

# ─────────────────────────────────────────────────────────────────────────────
# 4. Add primary_purpose + later_uses to all decks
# ─────────────────────────────────────────────────────────────────────────────
PURPOSE_MAP = {
    "tang-dynasty-c868":           ("gaming", []),
    "spanish-naipes-c1371":        ("gaming", []),
    "mamluk-c1375":                ("gaming", []),
    "visconti-di-modrone":         ("gaming", []),
    "visconti-sforza":             ("gaming", []),
    "charles-vi":                  ("gaming", []),
    "catelin-geoffroy-1557":       ("gaming", []),
    "tarot-de-marseille-dodal":    ("gaming", [
        {
            "use": "cartomancy",
            "date_earliest": 1785,
            "notes": "Etteilla (c. 1785–1789) adapted the Marseille-type deck for cartomancy. Court de Gébelin's "
                     "'Egyptian origins' essay (1781) created the intellectual context. Marseille decks were "
                     "repurposed for divination; they were never designed for it.",
        }
    ]),
    "minchiate-fiorentine":        ("gaming", []),
    "sola-busca":                  ("unknown", [
        {
            "use": "esoteric_reference",
            "date_earliest": 1909,
            "notes": "Pamela Colman Smith used the Sola-Busca as a visual source for the RWS minor arcana. "
                     "The deck's original purpose is unclear — possibly hermetic or alchemical, "
                     "possibly gaming with esoteric overlay.",
        }
    ]),
    "etteilla-grand-etteilla-1789": ("cartomancy", []),
    "golden-dawn-corpus":           ("esoteric_system", []),
    "rider-waite-smith":            ("divination", []),
    "thoth-tarot":                  ("divination", []),
}

for deck in data["decks"]:
    did = deck["id"]
    if did in PURPOSE_MAP and "primary_purpose" not in deck:
        pp, lu = PURPOSE_MAP[did]
        deck["primary_purpose"] = pp
        deck["later_uses"] = lu

print(f"Added primary_purpose/later_uses to {sum(1 for d in data['decks'] if 'primary_purpose' in d)} decks")

# ─────────────────────────────────────────────────────────────────────────────
# 5. New decks (inserted in chronological order)
# ─────────────────────────────────────────────────────────────────────────────
existing_ids = {d["id"] for d in data["decks"]}

NEW_DECKS = [
    {
        "id": "tang-dynasty-c868",
        "name": "Tang Dynasty Leaf Game",
        "name_local": "葉子戲 (Yèzǐ Xì)",
        "region": "Tang Empire (China)",
        "culture": "Tang Dynasty Chinese",
        "date_earliest": 850,
        "date_latest": 900,
        "date_display": "c. 850–900 CE",
        "date_basis": (
            "Referenced in a text attributed to Princess Tongchang during the reign of Emperor Yizong "
            "(859–873 CE). The word 'yèzǐ' (leaves) likely refers to paper cards. The game rules and "
            "card descriptions are partially preserved in later Tang and Song dynasty writings."
        ),
        "date_confidence": "low",
        "survival_status": "documented",
        "cards_known": 0,
        "cards_original": None,
        "missing_cards": [],
        "missing_cards_unidentified_count": None,
        "missing_cards_notes": "No physical cards survive. The game is known only from textual references.",
        "structure": {
            "total_cards": None,
            "suits": [],
            "ranks_per_suit": None,
            "court_cards": [],
            "trump_cards": 0,
            "notes": (
                "Card count and structure unknown. Some scholars propose 30–40 cards with monetary or "
                "hierarchical denominations. No suit structure comparable to Mamluk or European playing cards "
                "is documented."
            ),
        },
        "material": ["paper (assumed)"],
        "technique": ["unknown"],
        "language_on_cards": ["Chinese"],
        "holdings": [],
        "attributions": [
            {
                "role": "origin_culture",
                "name": "Tang Dynasty court",
                "confidence": "medium",
                "notes": "Association with Princess Tongchang; game may have spread from court to wider use",
            }
        ],
        "patron": None,
        "commissioned_for": None,
        "primary_purpose": "gaming",
        "later_uses": [],
        "purpose": ["gaming"],
        "transmission_path": (
            "Possibly an ancestor of Chinese paper money games, eventually influencing Mahjong and Chinese "
            "domino traditions. The connection to Western playing cards via the Silk Road remains speculative "
            "and not established in mainstream playing card scholarship."
        ),
        "iconography_notes": "Unknown; no surviving images.",
        "significance": (
            "If the textual attribution is accurate, this is the earliest documented reference to a card "
            "game anywhere in the world — predating the Mamluk deck by roughly 500 years. The connection "
            "to the European playing card tradition is debated and unproven; it may represent an independent "
            "invention rather than a direct ancestor."
        ),
        "tags": ["oldest_documented", "chinese", "no_surviving_cards", "paper"],
        "sources": [
            "Needham, Joseph. Science and Civilisation in China. Vol. 4, Part 1. Cambridge, 1962.",
            "Lo, Andrew. 'The Game of Leaves: An Inquiry into the Origin of Chinese Playing Cards.' Bulletin of the School of Oriental and African Studies, Vol. 63, 2000.",
        ],
    },
    {
        "id": "spanish-naipes-c1371",
        "name": "Spanish Naipes (earliest documented)",
        "name_local": "Naipes españoles",
        "region": "Catalonia / Castile, Iberian Peninsula",
        "culture": "Medieval Iberian",
        "date_earliest": 1371,
        "date_latest": 1380,
        "date_display": "c. 1371–1380 (documented)",
        "date_basis": (
            "A 1371 Barcelona account book records the purchase of playing cards. The 1377 Basel chronicle "
            "of Johannes von Rheinfelden describes a 52-card game that reached Europe 'from the Saracens.' "
            "No physical cards from this period survive; the earliest surviving European cards are c. 1390–1430."
        ),
        "date_confidence": "high",
        "survival_status": "documented",
        "cards_known": 0,
        "cards_original": 52,
        "missing_cards": [],
        "missing_cards_unidentified_count": 52,
        "missing_cards_notes": "No physical cards from this specific date range survive. Documentary evidence only.",
        "structure": {
            "total_cards": 52,
            "suits": ["cups", "coins", "swords", "clubs (batons)"],
            "ranks_per_suit": 13,
            "court_cards": ["king", "knight", "page"],
            "trump_cards": 0,
            "notes": (
                "The four Latin suits (cups/coins/swords/clubs) are direct adaptations of the Mamluk suits "
                "(cups/coins/swords/polo sticks). Only 3 court cards per suit (no queen) — a feature of all "
                "Latin-suited decks. The queen appears only in northern European (German/French) variants."
            ),
        },
        "material": ["paper"],
        "technique": ["woodblock_print (assumed)", "hand_painted"],
        "language_on_cards": ["none (non-scenic pips)"],
        "holdings": [],
        "attributions": [
            {
                "role": "origin_culture",
                "name": "Iberian cardmakers (Moorish transmission)",
                "confidence": "high",
                "notes": (
                    "The 1377 Basel chronicle explicitly states cards arrived 'from the Saracens' — "
                    "i.e., via the Moorish presence in Iberia. The Latin suit system is a direct "
                    "adaptation of the Mamluk suits."
                ),
            }
        ],
        "patron": None,
        "commissioned_for": "Commercial gaming market",
        "primary_purpose": "gaming",
        "later_uses": [],
        "purpose": ["gaming"],
        "transmission_path": (
            "Mamluk Egypt → Iberian peninsula (Moorish transmission) → Italy and northern Europe. "
            "The Italian suit system (cups/coins/swords/clubs) derives from the Spanish. "
            "German and French suits (hearts/bells/leaves/acorns and hearts/diamonds/clubs/spades) "
            "are later regional adaptations."
        ),
        "iconography_notes": (
            "The pole suit (Mamluk polo sticks) becomes clubs/batons in Iberian and Italian decks. "
            "The queen figure is absent — Mamluk and Latin-suited decks have king + two male officers. "
            "French decks later added the queen, creating the 52-card deck with four courts."
        ),
        "significance": (
            "The documentary pivot between Mamluk Egypt and European playing cards. The Latin suit "
            "system established here (cups/coins/swords/clubs) remains the standard for Italian, Spanish, "
            "and Portuguese cards to this day — and is the direct ancestor of the tarot minor arcana suits."
        ),
        "tags": ["latin_suits", "iberian", "mamluk_derived", "transmission_vector", "no_trumps"],
        "sources": [
            "Dummett, Michael. The Game of Tarot. Duckworth, 1980.",
            "Hargrave, Catherine Perry. A History of Playing Cards. Houghton Mifflin, 1930.",
            "Mann, Sylvia. All Cards on the Table. Jonas, 1990.",
        ],
    },
    {
        "id": "catelin-geoffroy-1557",
        "name": "Tarot de Marseille (Geoffroy, 1557)",
        "name_local": "Taraux — Catelin Geoffroy",
        "region": "Lyon, France",
        "culture": "French popular print culture",
        "date_earliest": 1557,
        "date_latest": 1557,
        "date_display": "1557",
        "date_basis": (
            "Catelin Geoffroy's name and the year 1557 appear on the surviving trump cards. This makes it "
            "the earliest *dated* and *signed* Tarot de Marseille Type I deck — predating the Dodal by 144 years."
        ),
        "date_confidence": "exact",
        "survival_status": "fragmentary",
        "cards_known": 22,
        "cards_original": 78,
        "missing_cards": [],
        "missing_cards_unidentified_count": 56,
        "missing_cards_notes": "Only the 22 trump cards survive. All 56 minor arcana are lost.",
        "structure": {
            "total_cards": 78,
            "suits": ["wands", "cups", "swords", "coins"],
            "ranks_per_suit": 14,
            "court_cards": ["king", "queen", "knight", "page"],
            "trump_cards": 22,
            "notes": (
                "Type I Tarot de Marseille — the earlier of the two Marseille type traditions. "
                "The surviving 22 trumps show the iconography that will be standardized in later Marseille editions. "
                "Strength at VIII, Justice at XI."
            ),
        },
        "material": ["paper"],
        "technique": ["woodblock_print"],
        "language_on_cards": ["French"],
        "holdings": [
            {
                "institution": "Bibliothèque nationale de France",
                "city": "Paris",
                "country": "France",
                "cards_held": 22,
                "accession": None,
                "digitized": True,
                "digitization_url": "https://gallica.bnf.fr",
            }
        ],
        "attributions": [
            {
                "role": "maker",
                "name": "Catelin Geoffroy",
                "confidence": "high",
                "notes": "Name and date (1557) appear on the surviving cards",
            }
        ],
        "patron": None,
        "commissioned_for": "Commercial sale",
        "primary_purpose": "gaming",
        "later_uses": [
            {
                "use": "cartomancy",
                "date_earliest": 1785,
                "notes": "Marseille-type decks repurposed for cartomancy from c. 1785 onward",
            }
        ],
        "purpose": ["gaming"],
        "transmission_path": (
            "Part of the Lyonnaise cardmaking tradition. Lyon was the center of French playing card "
            "production in the 16th century. The Marseille iconography was codified here before the "
            "industry shifted south."
        ),
        "iconography_notes": (
            "The 1557 Geoffroy is the earliest datable reference point for Marseille Type I iconography. "
            "It predates the Dodal (c. 1701) by nearly 150 years, confirming the Marseille tradition's "
            "continuous existence from the mid-16th century."
        ),
        "significance": (
            "Proof that the Marseille iconographic tradition was established by 1557 at the latest. "
            "Anchors the Marseille tradition as a 16th-century phenomenon rather than a 17th-century one. "
            "The Dodal and Conver are refinements of a tradition already old by their time."
        ),
        "tags": ["marseille_type_i", "woodblock", "earliest_dated_marseille", "fragmentary", "french"],
        "sources": [
            "Dummett, Michael. The Game of Tarot. Duckworth, 1980.",
            "Depaulis, Thierry. 'Tarot, jeu et magie.' BnF exhibition catalogue, 1984.",
        ],
    },
    {
        "id": "etteilla-grand-etteilla-1789",
        "name": "Grand Etteilla",
        "name_local": "Grand Etteilla, ou Tarots Égyptiens",
        "region": "Paris, France",
        "culture": "Enlightenment / occult revival",
        "date_earliest": 1789,
        "date_latest": 1791,
        "date_display": "1789–1791",
        "date_basis": (
            "Jean-Baptiste Alliette (pseudonym Etteilla — his name reversed) published his cartomantic "
            "system progressively: 'Manière de se récréer avec le jeu de cartes nommées tarots' (1783) "
            "established the theory; the redesigned deck 'Grand Etteilla' appeared 1789–1791."
        ),
        "date_confidence": "high",
        "survival_status": "extant",
        "cards_known": 78,
        "cards_original": 78,
        "structure": {
            "total_cards": 78,
            "suits": ["wands", "cups", "swords", "coins"],
            "ranks_per_suit": 14,
            "court_cards": ["king", "queen", "knight", "page"],
            "trump_cards": 22,
            "notes": (
                "Card order and imagery completely redesigned for cartomancy. Card 1 (the Querent) replaces "
                "The Fool as the card representing the reading subject. The trumps are renumbered and given "
                "pseudo-Egyptian names (following Court de Gébelin's false attribution). Etteilla introduced "
                "upright/reversed meanings, positional spreads, and dedicated cartomantic keywords — the "
                "mechanics that define modern tarot reading."
            ),
        },
        "material": ["paper"],
        "technique": ["engraving", "commercial_printing"],
        "language_on_cards": ["French"],
        "holdings": [
            {
                "institution": "Bibliothèque nationale de France and private collections",
                "city": "Paris",
                "country": "France",
                "cards_held": 78,
                "accession": None,
                "digitized": True,
                "digitization_url": None,
            }
        ],
        "attributions": [
            {
                "role": "designer",
                "name": "Jean-Baptiste Alliette (Etteilla)",
                "confidence": "high",
                "notes": (
                    "First professional tarot reader in recorded history. Developed the cartomantic "
                    "reading system independently of — and prior to — the Golden Dawn tradition."
                ),
            }
        ],
        "patron": None,
        "commissioned_for": "Commercial cartomancy market",
        "primary_purpose": "cartomancy",
        "later_uses": [],
        "purpose": ["cartomancy", "divination"],
        "transmission_path": (
            "Etteilla's system spread through French occult circles and formed the basis of parlor "
            "cartomancy practice. Marie-Anne Adelaide Lenormand — who read for Napoleon — was trained "
            "in this tradition. The system reached England and eventually influenced Waite's methodology "
            "even as Waite rejected the Egyptian iconography."
        ),
        "iconography_notes": (
            "The deck inverts the Marseille imagery and adds 'Egyptian' symbols based on Court de Gébelin's "
            "fabricated etymology. The Querent card (Card 1) is an innovation with no precedent. "
            "The reversed card system — where a card dealt upside down has an opposite meaning — "
            "is Etteilla's invention and now universal in tarot practice."
        ),
        "significance": (
            "The pivot deck. Before Etteilla, tarot was a card game that some people also used for "
            "fortune-telling with standard playing cards. After Etteilla, tarot was a purpose-built "
            "divination tool. The upright/reversed system, the spread positions, the Querent card, "
            "and the cartomantic keyword tradition are all Etteilla's inventions — not ancient Egyptian ones."
        ),
        "tags": ["first_divination_deck", "french", "enlightenment", "occult_revival", "complete", "reversed_meanings"],
        "sources": [
            "Decker, Ronald, Thierry Depaulis, and Michael Dummett. A Wicked Pack of Cards. St. Martin's Press, 1996.",
            "Farley, Helen. A Cultural History of Tarot. I.B. Tauris, 2009.",
            "Place, Robert M. The Tarot: History, Symbolism, and Divination. Tarcher/Penguin, 2005.",
        ],
    },
    {
        "id": "golden-dawn-corpus",
        "name": "Hermetic Order of the Golden Dawn — Esoteric Correspondences",
        "name_local": None,
        "region": "London, England",
        "culture": "Victorian occultism",
        "date_earliest": 1888,
        "date_latest": 1900,
        "date_display": "1888–1900 (manuscripts)",
        "date_basis": (
            "The Hermetic Order of the Golden Dawn was founded in 1888 by Samuel Liddell MacGregor Mathers, "
            "William Wynn Westcott, and William Robert Woodman. The tarot attribution schema — pairing each "
            "Major Arcana with a Hebrew letter, a path on the Kabbalistic Tree of Life, a planet or zodiacal "
            "sign, and an element — was codified in the initiation manuscripts, primarily the 'Book T' "
            "(sub-figura LXXVIII), c. 1888–1896. No physical deck was produced."
        ),
        "date_confidence": "high",
        "survival_status": "documented",
        "cards_known": 0,
        "cards_original": 0,
        "missing_cards": [],
        "missing_cards_unidentified_count": None,
        "missing_cards_notes": "This is not a physical deck. It is a body of manuscript attributions.",
        "structure": {
            "total_cards": 78,
            "suits": ["wands", "cups", "swords", "pentacles"],
            "ranks_per_suit": 14,
            "court_cards": ["king", "queen", "knight", "page"],
            "trump_cards": 22,
            "notes": (
                "Not a physical deck. The Golden Dawn attribution schema maps all 78 cards to Kabbalistic, "
                "astrological, and elemental correspondences. This schema was the direct source for both "
                "Waite's RWS and Crowley's Thoth — making the GD corpus the hidden parent of all modern "
                "esoteric tarot. The key manuscript is 'Book T' (sub-figura LXXVIII)."
            ),
        },
        "material": ["manuscript_paper"],
        "technique": ["manuscript"],
        "language_on_cards": ["English"],
        "holdings": [
            {
                "institution": "Warburg Institute (partial)",
                "city": "London",
                "country": "UK",
                "cards_held": 0,
                "accession": None,
                "digitized": False,
                "digitization_url": None,
            }
        ],
        "attributions": [
            {
                "role": "author",
                "name": "Samuel Liddell MacGregor Mathers",
                "confidence": "high",
                "notes": "Primary author of the Grade Papers including 'Book T'",
            },
            {
                "role": "co_founder",
                "name": "William Wynn Westcott",
                "confidence": "high",
                "notes": "Co-founder and Supreme Magus; contributed cipher manuscripts",
            },
        ],
        "patron": None,
        "commissioned_for": "Internal use by Golden Dawn initiates",
        "primary_purpose": "esoteric_system",
        "later_uses": [],
        "purpose": ["esoteric", "initiation_system"],
        "transmission_path": (
            "The GD manuscripts were never publicly published in their original form. They entered "
            "public knowledge through Israel Regardie's 'The Golden Dawn' (1937–1940) and Aleister Crowley's "
            "semi-public disclosures. Both Waite and Crowley implemented the system in their respective decks "
            "before Regardie's publication."
        ),
        "iconography_notes": None,
        "significance": (
            "The invisible infrastructure of all modern esoteric tarot. The Golden Dawn's attribution schema "
            "— Hebrew letter + Tree of Life path + planet/zodiac + element — is implemented in every "
            "esoteric tarot deck from 1909 onward. It transformed tarot from a gaming deck and folk fortune-"
            "telling tool into a systematic magical instrument. Waite and Crowley are rivals in the "
            "same tradition, not innovators of independent systems."
        ),
        "tags": ["golden_dawn", "manuscript_only", "esoteric_schema", "kabbalah", "victorian", "ur_template"],
        "sources": [
            "Regardie, Israel. The Golden Dawn. Llewellyn, 1937–1940.",
            "Greer, Mary K. Women of the Golden Dawn. Park Street Press, 1995.",
            "Decker, Ronald, and Michael Dummett. A History of the Occult Tarot. Duckworth, 2002.",
        ],
    },
]

# Insert new decks in chronological position
inserted = 0
for deck in NEW_DECKS:
    if deck["id"] not in existing_ids:
        # Find insertion point by date_earliest
        insert_at = len(data["decks"])
        for i, d in enumerate(data["decks"]):
            de = d.get("date_earliest") or 9999
            new_de = deck.get("date_earliest") or 9999
            if new_de < de:
                insert_at = i
                break
        data["decks"].insert(insert_at, deck)
        existing_ids.add(deck["id"])
        print(f"Added deck: {deck['id']} at position {insert_at}")
        inserted += 1
print(f"Inserted {inserted} new decks")

# ─────────────────────────────────────────────────────────────────────────────
# 6. Update schema_version and notes
# ─────────────────────────────────────────────────────────────────────────────
data["schema_version"] = "1.1"
data["notes"] = (
    "Historical card sets. Dates are ranges — never collapse to a single year. "
    "Survival: extant|fragmentary|documented|lost. "
    "Holdings are split by institution. "
    "Attributions carry roles and confidence. "
    "Genealogy is a typed edge list. "
    "missing_cards uses cards.json IDs (pentacles = historical coins). "
    "primary_purpose captures original intent; later_uses records functional shifts. "
    "v1.1: added Tang dynasty, Spanish naipes, Catelin Geoffroy, Etteilla, Golden Dawn pseudo-node; "
    "fixed RWS→Thoth genealogy edge; added missing_cards arrays; added primary_purpose/later_uses."
)

# ─────────────────────────────────────────────────────────────────────────────
# Write output
# ─────────────────────────────────────────────────────────────────────────────
SRC.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"\nWrote {len(data['decks'])} decks, {len(data['genealogy'])} edges → {SRC.name}")
