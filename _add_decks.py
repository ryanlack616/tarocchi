#!/usr/bin/env python3
"""Add 3 new historical decks to historical_decks.json."""
import json, sys

DATA = "data/historical_decks.json"

NEW_DECKS = [
    {
        "id": "tarot-de-paris-c1600",
        "name": "Tarot de Paris",
        "name_local": "Tarot parisien",
        "region": "Paris, France",
        "culture": "French popular print culture",
        "date_earliest": 1590,
        "date_latest": 1620,
        "date_display": "c. 1600 (fragmentary)",
        "date_basis": "Style analysis and cardmaking technique place the surviving fragments in Paris c. 1590–1620. Held at the Bibliothèque nationale de France. Represents the Paris cardmaking tradition between Geoffroy (1557) and Noblet (c. 1650).",
        "date_confidence": "medium",
        "survival_status": "fragmentary",
        "cards_known": 16,
        "cards_original": 78,
        "missing_cards": [],
        "missing_cards_unidentified_count": 62,
        "missing_cards_notes": "Only 16 Major Arcana cards survive. All minor arcana are lost.",
        "structure": {
            "total_cards": 78,
            "suits": ["wands", "cups", "swords", "coins"],
            "ranks_per_suit": 14,
            "court_cards": ["king", "queen", "knight", "page"],
            "trump_cards": 22,
            "notes": "Marseille Type I iconography in Parisian manufacture. Shows the transfer of the Marseille tradition from Lyon to Paris in the late 16th century."
        },
        "material": ["paper"],
        "technique": ["woodblock_print"],
        "language_on_cards": ["French"],
        "holdings": [
            {
                "institution": "Bibliothèque nationale de France",
                "city": "Paris",
                "country": "France",
                "cards_held": 16,
                "accession": None,
                "digitized": True,
                "digitization_url": "https://gallica.bnf.fr"
            }
        ],
        "attributions": [
            {
                "role": "maker",
                "name": "Unknown Parisian cardmaker",
                "confidence": "low",
                "notes": "No maker's mark survives on these fragments. Attribution to Paris based on style and materials."
            }
        ],
        "patron": None,
        "commissioned_for": "Commercial sale",
        "primary_purpose": "gaming",
        "later_uses": [],
        "purpose": ["gaming"],
        "transmission_path": "Part of the 16th-century transfer of playing card production from Lyon (Geoffroy) to Paris. The Paris cardmaking guilds adapted the Marseille Type I iconography to northern manufacture, producing the idiom that Noblet would later standardize.",
        "iconography_notes": "Shows early Parisian interpretation of Marseille Type I trumps. Minor differences in figure proportions and costume details distinguish these from the Lyon Geoffroy and later Noblet traditions. The Fool appears without the usual dog — replaced by a figure biting his own leg.",
        "significance": "Bridges the gap between the Lyon Geoffroy (1557) and the Paris Noblet (c. 1650). Confirms that the Marseille iconographic tradition reached Paris by c. 1600, establishing the city as a cardmaking center a generation before Noblet's better-documented production.",
        "tags": ["marseille_type_i", "woodblock", "fragmentary", "french", "paris"],
        "sources": [
            "Kaplan, Stuart R. The Encyclopedia of Tarot. Vol. I. U.S. Games Systems, 1978.",
            "Depaulis, Thierry. 'Tarot, jeu et magie.' BnF exhibition catalogue, 1984."
        ]
    },
    {
        "id": "tarot-de-marseille-noblet",
        "name": "Tarot de Marseille (Noblet, c. 1650)",
        "name_local": "Tarot — Jean Noblet",
        "region": "Paris, France",
        "culture": "French popular print culture",
        "date_earliest": 1648,
        "date_latest": 1660,
        "date_display": "c. 1650",
        "date_basis": "Jean Noblet was registered as a master cardmaker in Paris from 1648. The deck style is consistent with mid-17th century Parisian production. No explicit date appears on the cards.",
        "date_confidence": "high",
        "survival_status": "fragmentary",
        "cards_known": 22,
        "cards_original": 78,
        "missing_cards": [],
        "missing_cards_unidentified_count": 56,
        "missing_cards_notes": "22 trump cards survive at the Bibliothèque nationale de France. All 56 minor arcana are lost. The surviving trumps are sufficiently complete to reconstruct the Marseille Type II iconography.",
        "structure": {
            "total_cards": 78,
            "suits": ["wands", "cups", "swords", "coins"],
            "ranks_per_suit": 14,
            "court_cards": ["king", "queen", "knight", "page"],
            "trump_cards": 22,
            "notes": "Marseille Type II — the later and more widely disseminated Marseille type, with Strength at XI and Justice at VIII. The Noblet is the earliest known exemplar of the Paris-pattern Marseille Type II, the tradition that Dodal and Conver would later standardize."
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
                "digitization_url": "https://gallica.bnf.fr"
            }
        ],
        "attributions": [
            {
                "role": "maker",
                "name": "Jean Noblet",
                "confidence": "high",
                "notes": "Noblet's name appears on the surviving cards. He was registered as master cardmaker in Paris from 1648. This is the only deck securely attributed to him."
            }
        ],
        "patron": None,
        "commissioned_for": "Commercial sale",
        "primary_purpose": "gaming",
        "later_uses": [
            {
                "use": "esoteric restoration reference",
                "date_earliest": 1990,
                "notes": "Jodorowsky and Camoin used the Noblet as one of their reference decks in restoring the 1761 Conver Marseille, comparing woodblock details across surviving exemplars."
            }
        ],
        "purpose": ["gaming"],
        "transmission_path": "Jean Noblet worked in the Parisian cardmaking tradition that adapted the Marseille iconography for northern French manufacture. His deck is the earliest extant Paris-pattern Marseille, establishing the template that Dodal (Marseille, c. 1701) and Conver (Marseille, 1761) would later adopt and refine.",
        "iconography_notes": "The Noblet establishes what will become canonical Marseille Type II: the Hanged Man's tree shows no roots (later Marseille standardized this detail), the Lovers shows three figures with Cupid overhead, and the Devil shows a distinctly hermaphroditic figure unlike Lévi's later Baphomet-influenced versions. The High Priestess (II) shows a papal tiara — later Marseille editions would soften this.",
        "significance": "Earliest known exemplar of the Paris-pattern Marseille Type II, the most widely reproduced tarot tradition. Establishes the iconographic vocabulary that Dodal, Conver, and all subsequent Marseille printers would follow. Critical reference point for understanding the evolution from Marseille Type I (Geoffroy 1557) to Type II. The Jodorowsky/Camoin restoration consulted it directly.",
        "tags": [
            "marseille_type_ii",
            "woodblock",
            "paris",
            "earliest_paris_pattern",
            "fragmentary",
            "french",
            "jodorowsky_reference"
        ],
        "sources": [
            "Kaplan, Stuart R. The Encyclopedia of Tarot. Vol. I. U.S. Games Systems, 1978.",
            "Dummett, Michael. The Game of Tarot. Duckworth, 1980.",
            "Jodorowsky, Alejandro and Camoin, Philippe. The Way of Tarot. Destiny Books, 2004.",
            "Depaulis, Thierry. 'Le Jeu de Tarot: histoire et pratique.' BnF, 1984."
        ]
    },
    {
        "id": "papus-tarot-1889",
        "name": "Tarot des Bohémiens (Papus, 1889)",
        "name_local": "Le Tarot des Bohémiens",
        "region": "Paris, France",
        "culture": "French occultism / Martinism",
        "date_earliest": 1889,
        "date_latest": 1889,
        "date_display": "1889",
        "date_basis": "Published as part of Gérard Encausse (Papus), 'Le Tarot des Bohémiens,' Paris, Carré, 1889. First edition with 22 Major Arcana plates drawn by Gabriel Goulinat.",
        "date_confidence": "exact",
        "survival_status": "extant",
        "cards_known": 22,
        "cards_original": 22,
        "missing_cards": [],
        "missing_cards_unidentified_count": 0,
        "missing_cards_notes": "The 1889 Papus publication contains 22 Major Arcana illustrations by Goulinat, adapted from Wirth's 1889 esoteric deck. A full 78-card deck was not produced; the Minor Arcana were treated theoretically rather than illustrated.",
        "structure": {
            "total_cards": 22,
            "suits": [],
            "ranks_per_suit": None,
            "court_cards": [],
            "trump_cards": 22,
            "notes": "Only 22 Major Arcana illustrated. Papus treated the Minor Arcana as a numerical/Kabbalistic system rather than providing card art. The theoretical framework for all 78 is described in text but only the 22 trumps exist as visual objects."
        },
        "material": ["paper"],
        "technique": ["engraving", "letterpress"],
        "language_on_cards": ["French"],
        "holdings": [
            {
                "institution": "Bibliothèque nationale de France",
                "city": "Paris",
                "country": "France",
                "cards_held": None,
                "accession": None,
                "digitized": True,
                "digitization_url": "https://gallica.bnf.fr"
            }
        ],
        "attributions": [
            {
                "role": "author",
                "name": "Gérard Encausse (Papus)",
                "confidence": "high",
                "notes": "Published under the pen name Papus. Encausse was the leading French occultist of his generation, founder of the Martinist Order, and prolific author on Kabbalah and esoteric tarot."
            },
            {
                "role": "artist",
                "name": "Gabriel Goulinat",
                "confidence": "high",
                "notes": "Illustrated the 22 Major Arcana plates for the 1889 edition, adapting Wirth's esoteric imagery with additional Martinist symbolism."
            }
        ],
        "patron": None,
        "commissioned_for": "Publication for the Martinist esoteric reading public",
        "primary_purpose": "esoteric",
        "later_uses": [],
        "purpose": ["esoteric", "divination"],
        "transmission_path": "Papus received Wirth's 1889 Major Arcana through his connections to the French Rosicrucian/Martinist milieu (Stanislas de Guaita commissioned both projects). He adapted and extended Wirth's visual symbolism in the context of his own Kabbalistic and astrological system, producing a parallel theoretical framework to the emerging Golden Dawn system in London.",
        "iconography_notes": "The Goulinat plates closely follow the Wirth 1889 imagery but add additional Martinist and Kabbalistic details. The Chariot shows astrological glyphs not present in Wirth. The Magician (called 'Le Bateleur') retains the lemniscate hat brim introduced by Wirth. The High Priestess (called 'La Papesse') shows a more explicit Kabbalistic duality motif. The deck is also notable for placing Hebrew letter attributions prominently on each card — anticipating the GD's Book T format.",
        "significance": "Represents the parallel French esoteric tarot tradition to the English Golden Dawn system — both produced in 1889, both drawing on Lévi's Kabbalistic correspondences, but developing distinct visual vocabularies. Papus's written system influenced French tarot practice for decades and introduced the idea of tarot as a complete esoteric encyclopedia to a wide popular audience. The 'Tarot des Bohémiens' framing — associating the cards with Romani culture as alleged transmitters of Egyptian wisdom — was already a well-established myth by 1889 but Papus systematized it most influentially.",
        "tags": [
            "major_arcana_only",
            "esoteric",
            "french",
            "martinism",
            "kabbalah",
            "levi_tradition",
            "1889",
            "goulinat"
        ],
        "sources": [
            "Encausse, Gérard (Papus). Le Tarot des Bohémiens. Carré, Paris, 1889.",
            "Decker, Ronald; Depaulis, Thierry; and Dummett, Michael. A Wicked Pack of Cards. St. Martin's Press, 1996.",
            "Farley, Helen. A Cultural History of Tarot. I.B. Tauris, 2009."
        ]
    }
]

NEW_EDGES = [
    {
        "from": "catelin-geoffroy-1557",
        "to": "tarot-de-paris-c1600",
        "relation": "ancestor",
        "notes": "The Geoffroy 1557 Lyon deck established the Marseille Type I iconographic blueprint that Parisian cardmakers adapted by c. 1600. The shift from Lyon to Paris as the northern French cardmaking center was underway in the late 16th century."
    },
    {
        "from": "tarot-de-paris-c1600",
        "to": "tarot-de-marseille-noblet",
        "relation": "ancestor",
        "notes": "The c. 1600 Parisian fragments belong to the same Parisian cardmaking tradition that Noblet would consolidate c. 1650 into the first well-documented Paris-pattern Marseille deck."
    },
    {
        "from": "tarot-de-marseille-noblet",
        "to": "tarot-de-marseille-dodal",
        "relation": "ancestor",
        "notes": "Dodal's Marseille printing (c. 1701–1715) refines and standardizes the Paris-pattern Marseille Type II iconography that Noblet's c. 1650 deck established. The Dodal is the first full extant exemplar of the Marseille tradition that would run through Conver."
    },
    {
        "from": "oswald-wirth-1889",
        "to": "papus-tarot-1889",
        "relation": "direct_iconographic_source",
        "notes": "Papus's Goulinat plates for 'Le Tarot des Bohémiens' adapt Wirth's 1889 Major Arcana directly. Both projects were commissioned within the same Rosicrucian/Martinist milieu (Stanislas de Guaita was the connecting figure). The lemniscate Magician, the Kabbalistic correspondences, and several compositional choices are shared."
    },
    {
        "from": "papus-tarot-1889",
        "to": "rider-waite-smith",
        "relation": "esoteric_source_material",
        "notes": "Waite was fluent in the French occultist tarot literature including Papus's work. While Waite explicitly distanced himself from the French Martinist system in his 'Pictorial Key to the Tarot' (1910), the underlying Lévi-derived Kabbalistic structure he shared with Papus is visible in both decks' Hebrew letter attributions and Major Arcana correspondences."
    }
]

def main():
    with open(DATA, "r", encoding="utf-8") as f:
        data = json.load(f)

    existing_ids = {d["id"] for d in data["decks"]}
    added = []
    for deck in NEW_DECKS:
        if deck["id"] in existing_ids:
            print(f"  SKIP (already exists): {deck['id']}")
        else:
            data["decks"].append(deck)
            added.append(deck["id"])
            print(f"  ADDED deck: {deck['name']}")

    # Sort decks by date_earliest
    data["decks"].sort(key=lambda d: d.get("date_earliest", 0))

    existing_edges = {(e["from"], e["to"]) for e in data["genealogy"]}
    for edge in NEW_EDGES:
        key = (edge["from"], edge["to"])
        if key in existing_edges:
            print(f"  SKIP edge (already exists): {key}")
        else:
            data["genealogy"].append(edge)
            print(f"  ADDED edge: {edge['from']} → {edge['to']} [{edge['relation']}]")

    n_decks = len(data["decks"])
    n_edges = len(data["genealogy"])
    print(f"\nResult: {n_decks} decks, {n_edges} genealogy edges")

    with open(DATA, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print("Saved historical_decks.json")

if __name__ == "__main__":
    main()
