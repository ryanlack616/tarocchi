"""
Append next-wave 9 decks to historical_decks.json and card_witnesses.json.
Tier A (4): rosenwald-sheet, steele-sermon, pierpont-morgan-bergamo, ferrara-este
Tier B (2): madenie-1709, grimaud-marteau-1930
Tier C (3): aquarian-palladini-1970, hermetic-dowson-1979, motherpeace-1981
"""
import json
from pathlib import Path

ROOT = Path(r"C:\rje\dev\tarocchi\data")
DECKS_FILE = ROOT / "historical_decks.json"
WIT_FILE = ROOT / "card_witnesses.json"

# ---------------------------------------------------------------------------
# 9 NEW DECKS
# ---------------------------------------------------------------------------
NEW_DECKS = [
    # ---------------- TIER A: 15th c. structural nodes ----------------
    {
        "id": "rosenwald-sheet-c1500",
        "name": "Rosenwald Sheet",
        "name_local": "Rosenwald Playing-Card Sheets (Italian, c.1500)",
        "date_earliest": 1490,
        "date_latest": 1510,
        "date_display": "c. 1490–1510",
        "date_basis": "Stylistic dating by Kaplan and others places the three uncut woodblock sheets in the decade around 1500. Acquired by Lessing J. Rosenwald and donated with his print collection to the National Gallery of Art, Washington DC in 1943.",
        "date_confidence": "medium",
        "survival_status": "extant",
        "cards_known": 60,
        "cards_original": 78,
        "missing_cards": [],
        "missing_cards_unidentified_count": 18,
        "missing_cards_notes": "Three uncut woodblock sheets survive: one trump sheet (incomplete — appears to show ~19 of 22 trumps), one sheet with cups and coins, one sheet with swords and batons. Together they form most but not all of a 78-card tarot deck; no court-rank information is fully reconstructible.",
        "structure": {
            "total_cards": 78,
            "suits": ["batons", "cups", "swords", "coins"],
            "ranks_per_suit": 10,
            "court_cards": 16,
            "trump_cards": 22,
            "notes": "Three-sheet layout suggests the intended deck was a complete 78-card Italian tarot, though the preserved sheets are incomplete. Card order on the trump sheet is significant evidence for the canonical Milanese trump sequence."
        },
        "material": "Woodblock-printed uncut sheets on rag paper",
        "technique": "Woodblock printing (xylography), uncolored",
        "language_on_cards": "None (iconographic only)",
        "holdings": [
            {
                "institution": "National Gallery of Art",
                "city": "Washington, DC",
                "country": "USA",
                "cards_held": 60,
                "accession": "Rosenwald Collection 1943.3.878–880",
                "digitized": True,
                "digitization_url": "https://www.nga.gov/collection/"
            }
        ],
        "attributions": [
            {"role": "workshop", "name": "Unknown Italian (Florentine or Emilian) printshop", "confidence": "medium", "notes": "Attribution to Florence is commonly proposed on iconographic grounds; some scholars argue for Bologna or Ferrara based on figure conventions."}
        ],
        "patron": None,
        "commissioned_for": "Mass-market card production",
        "primary_purpose": "gaming",
        "later_uses": ["scholarly-reference"],
        "purpose": ["gaming", "commercial-production"],
        "transmission_path": "Italian woodblock printing tradition (c. 1450–1500) → Rosenwald workshop sheets → commercial distribution (cards cut from sheets and played) → preservation of master sheet by collector → Rosenwald → NGA.",
        "iconography_notes": "The trump sheet preserves a trump order closely matching the Steele Sermon canonical list, confirming the Milanese trump sequence was stable by c.1500. The pip cards show the Italian-suited conventions (batons, cups, swords, coins) with rank-specific ornamental patterns.",
        "significance": "The Rosenwald and Cary sheets are the two primary witnesses to mass-produced 15th c. Italian tarot. Together they document that by c.1500 tarot had transitioned from luxury hand-painted decks (Visconti-Sforza, PMB) to commercial woodblock production, and they preserve the canonical Milanese trump order in printed form.",
        "tags": ["uncut-sheet", "woodblock", "italian", "15th-century", "rosenwald-collection", "printed-tarot-origins"],
        "sources": [
            "Kaplan, Stuart R. Encyclopedia of Tarot. Vol. I. U.S. Games Systems, 1978.",
            "Dummett, Michael. The Game of Tarot. Duckworth, 1980.",
            "National Gallery of Art, Washington DC — Rosenwald Collection records."
        ],
        "region": "Northern Italy (Florence or Emilia-Romagna)",
        "culture": "Italian Early Renaissance"
    },
    {
        "id": "steele-sermon-c1495",
        "name": "Steele Sermon (De ludo cum aliis)",
        "name_local": "Sermones de ludo cum aliis — anonymous Franciscan manuscript",
        "date_earliest": 1470,
        "date_latest": 1500,
        "date_display": "c. 1470–1500",
        "date_basis": "Paleographic dating of the manuscript to late 15th c.; Robert Steele published the transcription in 1900. The sermon is catalogued as BL Additional MS 5197 / also preserved in a Würzburg manuscript.",
        "date_confidence": "medium",
        "survival_status": "extant",
        "cards_known": 0,
        "cards_original": 0,
        "missing_cards": [],
        "missing_cards_unidentified_count": 0,
        "missing_cards_notes": "This is a manuscript document, not a deck. It is included in the corpus because it is the earliest complete written record of the 22 trump cards in canonical order, and therefore constitutes primary evidence for the structure of the trump sequence that all later decks inherit.",
        "structure": {
            "total_cards": 22,
            "suits": [],
            "ranks_per_suit": 0,
            "court_cards": 0,
            "trump_cards": 22,
            "notes": "Records only the 22 trumps in a specific order: Bagatella, Empress, Emperor, Popess, Pope, Temperance, Love, Chariot, Fortitude, Wheel, Hunchback/Hermit, Hanged Man, Death, Devil, Tower, Star, Moon, Sun, Angel/Judgment, Justice, World, Fool. The ordering differs from later Tarot de Marseille convention."
        },
        "material": "Manuscript (parchment/paper, Latin text)",
        "technique": "Hand-written Latin sermon",
        "language_on_cards": "N/A (Latin document describing cards)",
        "holdings": [
            {"institution": "British Library", "city": "London", "country": "UK", "cards_held": None, "accession": "Add MS 5197", "digitized": False, "digitization_url": None},
            {"institution": "Universitätsbibliothek Würzburg", "city": "Würzburg", "country": "Germany", "cards_held": None, "accession": None, "digitized": False, "digitization_url": None}
        ],
        "attributions": [
            {"role": "author", "name": "Anonymous Franciscan preacher", "confidence": "medium", "notes": "Sermon style and moralizing tone suggest a Franciscan friar in Northern Italy, preaching against gambling and the use of cards. Identity unrecovered."}
        ],
        "patron": None,
        "commissioned_for": "Religious moral instruction",
        "primary_purpose": "theological-critique",
        "later_uses": ["scholarly-reference"],
        "purpose": ["theological-critique", "historical-evidence"],
        "transmission_path": "Late 15th c. Italian religious manuscript culture → preserved in monastery/institutional libraries → 19th c. British Library and Würzburg holdings → Steele 1900 transcription → central citation in all modern tarot historiography.",
        "iconography_notes": "The manuscript describes no images but lists the 22 trumps by name in a specific sequence, which is the earliest surviving structural evidence for a canonical trump order. The sequence is designated 'Order A' by Dummett and represents the Milanese/Bolognese ordering tradition.",
        "significance": "The Steele Sermon is the single most important textual witness to the structure of tarot before 1500. Without it, we would not know the canonical trump order existed this early or what form it took. Every later Marseille, RWS, and Thoth ordering can be traced back to the Order A sequence this manuscript preserves.",
        "tags": ["manuscript-evidence", "trump-order", "15th-century", "theological-source", "structural-evidence", "order-a"],
        "sources": [
            "Steele, Robert. 'A Notice of the Ludus Triumphorum and Some Early Italian Card Games.' Archaeologia 57 (1900): 185–200.",
            "Dummett, Michael. The Game of Tarot. Duckworth, 1980.",
            "Depaulis, Thierry. 'Early Italian Lists of Tarot Trumps.' The Playing-Card 36 (2007)."
        ],
        "region": "Northern Italy",
        "culture": "Italian Late-Medieval / Franciscan"
    },
    {
        "id": "pierpont-morgan-bergamo-c1500",
        "name": "Pierpont-Morgan Bergamo Tarot (PMB)",
        "name_local": "Tarocchi detti 'Colleoni-Baglioni' / Pierpont-Morgan-Bergamo",
        "date_earliest": 1480,
        "date_latest": 1510,
        "date_display": "c. 1480–1510 (third Visconti-lineage deck)",
        "date_basis": "Distinct from the main Visconti-Sforza deck (c.1450–1480) on stylistic and heraldic grounds. Six cards are 17th c. replacements. Main surviving set dated on iconographic comparison with late Bembo workshop and post-Bembo Milanese painting.",
        "date_confidence": "medium",
        "survival_status": "fragmentary",
        "cards_known": 74,
        "cards_original": 78,
        "missing_cards": ["major-15", "major-16", "knight-of-coins", "page-of-swords"],
        "missing_cards_unidentified_count": 0,
        "missing_cards_notes": "PMB preserves 74 of 78 cards across three institutions. Six of the 74 (the Devil, Tower, Fortitude, Star, Moon, Sun — contested) are generally considered later 17th c. replacements painted to fill gaps. Historical literature sometimes conflates PMB with Visconti-Sforza; Dummett and Kaplan treat them as a distinct deck.",
        "structure": {
            "total_cards": 78,
            "suits": ["batons", "cups", "swords", "coins"],
            "ranks_per_suit": 10,
            "court_cards": 16,
            "trump_cards": 22,
            "notes": "Full 78-card Italian tarot structure. Trump ordering and iconography follow the Milanese tradition, with Bembo-workshop stylistic conventions distinguishable from the slightly earlier Visconti-Sforza deck."
        },
        "material": "Hand-painted on heavy cardstock with gold leaf and silver leaf backgrounds",
        "technique": "Tempera and gold leaf on paper/cardstock (luxury commission)",
        "language_on_cards": "None",
        "holdings": [
            {"institution": "Morgan Library & Museum", "city": "New York", "country": "USA", "cards_held": 35, "accession": "MS M.630", "digitized": True, "digitization_url": "https://www.themorgan.org/collection/tarot-cards"},
            {"institution": "Accademia Carrara", "city": "Bergamo", "country": "Italy", "cards_held": 26, "accession": None, "digitized": False, "digitization_url": None},
            {"institution": "Casa Colleoni", "city": "Bergamo", "country": "Italy", "cards_held": 13, "accession": None, "digitized": False, "digitization_url": None}
        ],
        "attributions": [
            {"role": "workshop", "name": "Bembo workshop circle (post-Bonifacio Bembo)", "confidence": "medium", "notes": "Style is consistent with the extended Bembo workshop tradition in Cremona and Milan, slightly later than the master-period Visconti-Sforza cards."},
            {"role": "replacement_artist", "name": "Unknown 17th c. painter", "confidence": "medium", "notes": "Six cards considered later replacements, painted in a recognizably post-Renaissance style to complete the deck after original cards were lost."}
        ],
        "patron": "Sforza or Colleoni family (unresolved)",
        "commissioned_for": "Milanese aristocratic court use",
        "primary_purpose": "gaming",
        "later_uses": ["dynastic-heirloom", "scholarly-reference"],
        "purpose": ["gaming", "aristocratic-display"],
        "transmission_path": "Bembo workshop (Cremona/Milan, c.1480–1510) → Sforza or Colleoni family inheritance → Colleoni palace Bergamo → 19th c. dispersal (sale of 35 cards eventually to Pierpont Morgan, New York; 26 to Accademia Carrara; 13 retained at Casa Colleoni).",
        "iconography_notes": "Iconographically similar to Visconti-Sforza but distinct in painterly execution: figures are slightly more elongated, drapery conventions later, backgrounds more consistently gold-leafed. The replacement cards show unmistakable 17th c. academic painting conventions.",
        "significance": "PMB is the third surviving luxury Visconti-era tarot (with Visconti di Modrone and Visconti-Sforza). Together these three decks document that hand-painted tarocchi production in Milan continued at the highest level for at least 60 years (c.1441–1510) across three distinct commissions, establishing tarot's court-art status before the transition to woodblock mass production.",
        "tags": ["luxury-tarot", "milanese", "bembo-workshop", "sforza-era", "hand-painted", "gold-leaf", "15th-century", "morgan-library"],
        "sources": [
            "Kaplan, Stuart R. Encyclopedia of Tarot. Vol. I. U.S. Games Systems, 1978.",
            "Dummett, Michael. The Game of Tarot. Duckworth, 1980.",
            "Morgan Library & Museum catalogue MS M.630."
        ],
        "region": "Milan / Cremona, Lombardy",
        "culture": "Italian High Renaissance court"
    },
    {
        "id": "ferrara-este-c1470",
        "name": "Ferrara / Este Court Tarocchi",
        "name_local": "Tarocchi della corte estense di Ferrara",
        "date_earliest": 1460,
        "date_latest": 1480,
        "date_display": "c. 1460–1480",
        "date_basis": "Este court account books at Modena document payments for 'carte da trionfi' to Ferrara cardmakers in the 1450s–1470s. Surviving fragments attributed to the Este court on stylistic and heraldic grounds.",
        "date_confidence": "medium",
        "survival_status": "fragmentary",
        "cards_known": 16,
        "cards_original": 78,
        "missing_cards": [],
        "missing_cards_unidentified_count": 62,
        "missing_cards_notes": "Only a small number of Este-attributed cards survive, split between Yale University Art Gallery (Cary Collection) and Museo Civico in Ferrara. No complete deck from the Este commissions survives.",
        "structure": {
            "total_cards": 78,
            "suits": ["batons", "cups", "swords", "coins"],
            "ranks_per_suit": 10,
            "court_cards": 16,
            "trump_cards": 22,
            "notes": "Reconstructed as a standard 78-card Italian tarot. Surviving fragments suggest the Ferrarese iconographic tradition differed in detail from Milanese (different figure treatments, distinctive Este heraldry on court cards)."
        },
        "material": "Hand-painted on cardstock with gold and silver ground",
        "technique": "Tempera on paper with metal leaf (luxury)",
        "language_on_cards": "None",
        "holdings": [
            {"institution": "Yale University Art Gallery (Cary Collection)", "city": "New Haven, CT", "country": "USA", "cards_held": 9, "accession": None, "digitized": True, "digitization_url": "https://artgallery.yale.edu"},
            {"institution": "Museo Civico Schifanoia / Palazzo Schifanoia", "city": "Ferrara", "country": "Italy", "cards_held": 7, "accession": None, "digitized": False, "digitization_url": None}
        ],
        "attributions": [
            {"role": "workshop", "name": "Ferrara court painters (Cosmè Tura circle, tentative)", "confidence": "low", "notes": "Some cards have been tentatively associated with the Tura/Del Cossa painterly environment that produced the Schifanoia frescoes, though no firm documentary link exists."}
        ],
        "patron": "Este court (Borso d'Este and/or Ercole I d'Este)",
        "commissioned_for": "Ferrarese court card-playing and display",
        "primary_purpose": "gaming",
        "later_uses": ["dynastic-heirloom"],
        "purpose": ["gaming", "aristocratic-display"],
        "transmission_path": "Este court commissions (Ferrara, c.1460–1480) → court dispersal through Este succession → fragmentation across Italian noble collections → 19th–20th c. acquisition by Yale Cary Collection (New Haven) and Museo Civico (Ferrara).",
        "iconography_notes": "Ferrarese tarocchi stand as a third regional tradition alongside Milan (Visconti/PMB) and Bologna (later Mitelli lineage). The surviving fragments show distinctive Este heraldic elements and painterly conventions linked to the Schifanoia fresco cycle, pointing to a Ferrara-based court workshop separate from the Milanese Bembo tradition.",
        "significance": "Establishes Ferrara as a third major 15th c. tarot production center alongside Milan and Bologna. The Este court commissions prove that tarot was not a monolithic Milanese phenomenon but a cross-regional aristocratic craft with distinct local iconographic traditions — a fact obscured when only the more fully surviving Visconti material is considered.",
        "tags": ["luxury-tarot", "ferrarese", "este-court", "15th-century", "fragmentary", "yale-cary", "regional-diversity"],
        "sources": [
            "Kaplan, Stuart R. Encyclopedia of Tarot. Vol. I. U.S. Games Systems, 1978.",
            "Dummett, Michael. The Game of Tarot. Duckworth, 1980.",
            "Bellosi, Luciano. 'Per la storia delle carte da gioco ferraresi.' Prospettiva, various numbers."
        ],
        "region": "Ferrara, Emilia-Romagna",
        "culture": "Italian Early Renaissance (Este court)"
    },
    # ---------------- TIER B: Marseille lineage fills ----------------
    {
        "id": "madenie-1709",
        "name": "Tarot de Marseille (Pierre Madenié, Dijon, 1709)",
        "name_local": "Tarot de Marseille — Pierre Madenié, Dijon 1709",
        "date_earliest": 1709,
        "date_latest": 1709,
        "date_display": "1709 (dated edition)",
        "date_basis": "The deck bears a printed 1709 date on the Deux de Coupe and is signed 'Pierre Madenié à Dijon.' Among the earliest dated complete Tarot de Marseille Type II decks.",
        "date_confidence": "exact",
        "survival_status": "extant",
        "cards_known": 78,
        "cards_original": 78,
        "missing_cards": [],
        "missing_cards_unidentified_count": 0,
        "missing_cards_notes": "Several near-complete exemplars survive in Swiss and French collections. Restored for modern publication by Yves Reynaud.",
        "structure": {
            "total_cards": 78,
            "suits": ["batons", "cups", "swords", "coins"],
            "ranks_per_suit": 10,
            "court_cards": 16,
            "trump_cards": 22,
            "notes": "Canonical Tarot de Marseille Type II structure: 22 trumps with Justice at VIII and Strength at XI, Papesse at II and Pape at V, French titles on trumps, Italian-style pip suits. The direct typographic ancestor of Dodal and Conver."
        },
        "material": "Woodblock-printed cards, hand-stenciled color on cardstock",
        "technique": "Woodblock printing with pochoir (stencil) coloring",
        "language_on_cards": "French",
        "holdings": [
            {"institution": "Bibliothèque nationale de France", "city": "Paris", "country": "France", "cards_held": None, "accession": None, "digitized": True, "digitization_url": "https://gallica.bnf.fr"},
            {"institution": "Swiss Museum of Playing Cards (Schweizerisches Spielkartenmuseum)", "city": "Schaffhausen", "country": "Switzerland", "cards_held": None, "accession": None, "digitized": False, "digitization_url": None}
        ],
        "attributions": [
            {"role": "cardmaker", "name": "Pierre Madenié", "confidence": "high", "notes": "Dijon master cardmaker, active early 18th c. His deck is signed and dated, giving it unusual dating certainty among Marseille-tradition decks."}
        ],
        "patron": None,
        "commissioned_for": "Commercial gaming market",
        "primary_purpose": "gaming",
        "later_uses": ["cartomancy", "esoteric", "facsimile-reprint"],
        "purpose": ["gaming", "commercial"],
        "transmission_path": "Paris-region Marseille tradition (Noblet 1650) → Dijon adaptation (Madenié 1709) → direct typographic influence on Marseille/Dodal (c.1701–1715) and Conver (1761) → modern Marseille restoration (Camoin-Jodorowsky 1997) → contemporary facsimile tradition (Reynaud, Flornoy).",
        "iconography_notes": "The Madenié 1709 is the earliest clearly dated survivor of the Type II Tarot de Marseille iconographic canon. It standardizes the imagery that Dodal and Conver would propagate: the specific mountain-and-sun pattern on the Moon, the double cords on the Hanged Man, the specific crayfish on the Moon, the two dogs, and dozens of other micro-details that distinguish Type II from Noblet's Type I.",
        "significance": "Madenié 1709 is the single most important dated node for the Tarot de Marseille canon. It proves the Type II iconography was fully stabilized by 1709, decades earlier than often assumed, and provides the documentary anchor for the Marseille tradition that Conver 1761 then propagates into global recognition. Without Madenié, the Noblet → Conver jump has no dated middle term.",
        "tags": ["marseille-type-ii", "dated-exemplar", "dijon", "early-18th-century", "typographic-ancestor-conver"],
        "sources": [
            "Depaulis, Thierry. Tarot, jeu et magie. BnF, 1984.",
            "Reynaud, Yves. Tarot de Marseille de Pierre Madenié (Dijon 1709) — restoration edition.",
            "Dummett, Michael and Ronald Decker. A History of the Occult Tarot 1870–1970. Duckworth, 2002."
        ],
        "region": "Dijon, Burgundy, France",
        "culture": "French 18th-century cardmaking trade"
    },
    {
        "id": "grimaud-marteau-1930",
        "name": "Ancien Tarot de Marseille (Grimaud / Paul Marteau, 1930)",
        "name_local": "Ancien Tarot de Marseille — Grimaud (Paul Marteau recoloration)",
        "date_earliest": 1930,
        "date_latest": 1930,
        "date_display": "1930 (Marteau recoloration; Grimaud publication)",
        "date_basis": "Paul Marteau's recolored Tarot de Marseille was published by B.P. Grimaud in 1930. The line drawings are adapted from the 18th c. Marseille tradition (particularly the Conver 1761 and Dijon-lineage decks).",
        "date_confidence": "exact",
        "survival_status": "extant",
        "cards_known": 78,
        "cards_original": 78,
        "missing_cards": [],
        "missing_cards_unidentified_count": 0,
        "missing_cards_notes": "Continuously in print since 1930; probably the most-printed tarot deck of the 20th century prior to the rise of RWS-tradition decks in the English-speaking world.",
        "structure": {
            "total_cards": 78,
            "suits": ["batons", "cups", "swords", "coins"],
            "ranks_per_suit": 10,
            "court_cards": 16,
            "trump_cards": 22,
            "notes": "Standard Tarot de Marseille Type II structure (Justice VIII, Strength XI, Papesse II, Pape V). Distinctive Marteau color palette: strong primaries, large blocks of flat color, characteristic Grimaud 'orange' pip backgrounds."
        },
        "material": "Commercial printed cards on cardstock with Grimaud back pattern",
        "technique": "Offset printing with stabilized color palette",
        "language_on_cards": "French",
        "holdings": [
            {"institution": "Continuously in print (Cartamundi/France Cartes)", "city": "Various", "country": "France", "cards_held": None, "accession": None, "digitized": True, "digitization_url": None}
        ],
        "attributions": [
            {"role": "colorist_adapter", "name": "Paul Marteau", "confidence": "high", "notes": "French occultist and Grimaud editor (1885–1966). His 1930 recoloration stabilized the Marseille palette for the 20th c. commercial market. His 1949 book 'Le Tarot de Marseille' became the standard French-language Marseille reference."},
            {"role": "publisher", "name": "B.P. Grimaud", "confidence": "high", "notes": "Major French card publisher (Paris). The Grimaud Marseille became the de facto standard Marseille deck from 1930 until Jodorowsky's Camoin restoration in 1997."}
        ],
        "patron": None,
        "commissioned_for": "20th-century French commercial market",
        "primary_purpose": "cartomancy",
        "later_uses": ["gaming", "esoteric", "pedagogical"],
        "purpose": ["cartomancy", "gaming", "commercial"],
        "transmission_path": "Conver 1761 and Dijon-lineage Marseille woodblock tradition → Paul Marteau's 1930 recoloration for Grimaud → continuous French commercial print run → 20th c. occult and cartomantic use in Europe → superseded in connoisseur/restoration use by Camoin-Jodorowsky 1997.",
        "iconography_notes": "Line drawings follow 18th c. Conver-lineage closely but color palette is Marteau's 20th c. recalibration: stronger reds and yellows, consistent flat blue backgrounds, simplified blocks of color. The orange pip-card background is a Grimaud signature. Aesthetically the Grimaud differs noticeably from the 18th c. pochoir decks; this aesthetic shaped 20th c. expectations of 'what a Marseille looks like' in France.",
        "significance": "The Grimaud-Marteau Marseille is the deck of 20th c. French cartomancy. Every mid-century French reader (Kardec-era spiritualists, surrealists in their divination moods, 1970s esotericists) used this deck. Marteau's 1949 'Le Tarot de Marseille' book paired with it became the dominant French tarot reference until Jodorowsky. The deck established the commercial-Marseille aesthetic that persisted until the Camoin-Jodorowsky restoration challenged its color choices in 1997.",
        "tags": ["marseille", "20th-century", "grimaud", "marteau", "french-cartomancy", "commercial-standard"],
        "sources": [
            "Marteau, Paul. Le Tarot de Marseille. Arts et Métiers Graphiques, 1949.",
            "Depaulis, Thierry. Tarot, jeu et magie. BnF, 1984.",
            "Jodorowsky, Alejandro and Philippe Camoin. The Way of Tarot. Destiny Books, 2009."
        ],
        "region": "Paris, France",
        "culture": "French 20th-century cartomantic tradition"
    },
    # ---------------- TIER C: 20th c. post-RWS indie / esoteric ----------------
    {
        "id": "aquarian-palladini-1970",
        "name": "Aquarian Tarot (David Palladini, 1970)",
        "name_local": "The Aquarian Tarot — David Palladini",
        "date_earliest": 1970,
        "date_latest": 1970,
        "date_display": "1970 (first edition, Morgan Press)",
        "date_basis": "Published by Morgan Press (with U.S. Games Systems distribution) in 1970, becoming one of the defining American tarot decks of the 1970s.",
        "date_confidence": "exact",
        "survival_status": "extant",
        "cards_known": 78,
        "cards_original": 78,
        "missing_cards": [],
        "missing_cards_unidentified_count": 0,
        "missing_cards_notes": "Continuously in print since 1970.",
        "structure": {
            "total_cards": 78,
            "suits": ["wands", "cups", "swords", "pentacles"],
            "ranks_per_suit": 10,
            "court_cards": 16,
            "trump_cards": 22,
            "notes": "Standard RWS-tradition 78-card structure (Strength VIII, Justice XI; English suit names). Scenic pips follow the RWS convention (Smith's scenic minor arcana preserved in composition)."
        },
        "material": "Commercial printed cards with Art Deco / Art Nouveau aesthetic",
        "technique": "Ink-and-color commercial illustration, offset printing",
        "language_on_cards": "English",
        "holdings": [
            {"institution": "Continuously in print (U.S. Games Systems)", "city": "Stamford, CT", "country": "USA", "cards_held": None, "accession": None, "digitized": True, "digitization_url": None}
        ],
        "attributions": [
            {"role": "artist_designer", "name": "David Palladini", "confidence": "high", "notes": "American illustrator (1946–2020) in Art Nouveau and Art Deco idioms. Later also designed the Neo-Classical Tarot and The Linweave Tarot. His Aquarian was his first and most influential deck."}
        ],
        "patron": None,
        "commissioned_for": "1970s American commercial market (post-hippie esoteric revival)",
        "primary_purpose": "divination",
        "later_uses": ["collectible", "pedagogical"],
        "purpose": ["divination", "aesthetic-display"],
        "transmission_path": "RWS iconographic tradition (1909) → American 1960s–70s occult revival → Palladini's stylized Art Nouveau/Deco recomposition (1970) → dominant 'mod' tarot aesthetic in 1970s U.S. → influence on post-RWS indie deck designers.",
        "iconography_notes": "Strict RWS compositional fidelity for the Minor Arcana (Smith's scenes preserved) but with Palladini's Art Nouveau linework and Deco stylization. The trumps show more invention: the figures are more stylized and less narrative than Smith's, with a characteristic flat-color-block aesthetic that became widely imitated. This deck is often the first tarot deck 1970s and 80s Americans encountered outside the classic RWS.",
        "significance": "The Aquarian Tarot marks the beginning of the 'post-RWS art deck' era: a deck that is recognizably a RWS descendant but with a distinct artist's vision and aesthetic, not a pedagogical or esoteric retool. Every indie illustrated deck of the 1980s–2020s descends from this precedent of treating the tarot as a vehicle for a personal artistic idiom.",
        "tags": ["20th-century", "rws-derivative", "art-nouveau", "art-deco", "post-rws-era", "american-commercial", "palladini"],
        "sources": [
            "Kaplan, Stuart R. Encyclopedia of Tarot. Vol. II. U.S. Games Systems, 1986.",
            "Palladini, David. The Aquarian Tarot deck and booklet. Morgan Press / U.S. Games Systems, 1970.",
            "Wolfe, Rachel. The Rider-Waite Tarot: A Handbook for Smith's Minor Arcana. 2013."
        ],
        "region": "New York / USA",
        "culture": "American 20th-century Commercial Tarot"
    },
    {
        "id": "hermetic-dowson-1979",
        "name": "Hermetic Tarot (Godfrey Dowson, 1979)",
        "name_local": "The Hermetic Tarot — Godfrey Dowson",
        "date_earliest": 1979,
        "date_latest": 1979,
        "date_display": "1979 (first edition)",
        "date_basis": "Published by U.S. Games Systems in 1979. Based on Dowson's extensive study of the original Golden Dawn ritual papers and the Crowley-Harris correspondence.",
        "date_confidence": "exact",
        "survival_status": "extant",
        "cards_known": 78,
        "cards_original": 78,
        "missing_cards": [],
        "missing_cards_unidentified_count": 0,
        "missing_cards_notes": "In print continuously since 1979; standard reference edition printed in high-contrast black-and-white with occasional colored accents.",
        "structure": {
            "total_cards": 78,
            "suits": ["wands", "cups", "swords", "disks"],
            "ranks_per_suit": 10,
            "court_cards": 16,
            "trump_cards": 22,
            "notes": "Golden Dawn structure: Strength (Fortitude) and Justice in Crowley-equivalent positions; Princess/Prince/Queen/Knight court ranks following the GD system rather than the RWS King/Queen/Knight/Page. Hebrew letters and zodiacal/planetary attributions printed on each trump."
        },
        "material": "High-contrast black-and-white line illustration on cardstock",
        "technique": "Pen-and-ink illustration (Rapidograph / technical pen), densely symbolic",
        "language_on_cards": "English (with Hebrew letters and astrological glyphs)",
        "holdings": [
            {"institution": "Continuously in print (U.S. Games Systems)", "city": "Stamford, CT", "country": "USA", "cards_held": None, "accession": None, "digitized": True, "digitization_url": None}
        ],
        "attributions": [
            {"role": "artist_designer", "name": "Godfrey Dowson", "confidence": "high", "notes": "British occultist-artist (1923–2005), long-time student of the Golden Dawn material. His Hermetic Tarot is the product of decades of study of GD ritual documents and the Waite-era Golden Dawn literature."}
        ],
        "patron": None,
        "commissioned_for": "Advanced Golden Dawn practitioners and esotericists",
        "primary_purpose": "esoteric_study",
        "later_uses": ["meditation-tool", "pedagogical"],
        "purpose": ["esoteric-study", "golden-dawn-transmission"],
        "transmission_path": "Golden Dawn ritual papers (c.1888–1900) → Waite/Crowley 20th c. commentaries → Regardie's publication of the Golden Dawn corpus (1937–1940) → Dowson's synthetic reconstruction of the ritual imagery into a complete deck (1979) → adoption by post-Regardie GD-tradition study groups.",
        "iconography_notes": "The Hermetic is the single most informationally dense tarot ever produced: each card bears Hebrew letters, zodiacal and planetary sigils, Sephiroth attributions, elemental attributions, decan associations, and densely worked symbolic imagery drawn from the Golden Dawn ritual papers. It makes no concession to visual approachability; it is a ritual document in card form.",
        "significance": "The Hermetic Tarot is the most faithful surviving visual transcription of the Golden Dawn ritual symbolic system. Where RWS (Waite) and Thoth (Crowley) each made editorial decisions that departed from the GD originals in different directions, Dowson attempts a pure synthesis: 'what would the Golden Dawn cards have looked like if the system itself drew them?' It is the scholarly-reference companion to the Thoth and the RWS for the Golden Dawn tradition.",
        "tags": ["golden-dawn", "esoteric", "hermetic", "20th-century", "black-and-white", "dense-symbolism", "ritual-document"],
        "sources": [
            "Dowson, Godfrey. The Hermetic Tarot (booklet). U.S. Games Systems, 1979.",
            "Regardie, Israel. The Golden Dawn. Llewellyn, 1937–1940 (4 vols).",
            "Kaplan, Stuart R. Encyclopedia of Tarot. Vol. II. U.S. Games Systems, 1986."
        ],
        "region": "UK / international",
        "culture": "20th-century Golden Dawn revival"
    },
    {
        "id": "motherpeace-1981",
        "name": "Motherpeace Tarot (Karen Vogel & Vicki Noble, 1981)",
        "name_local": "The Motherpeace Round Tarot — Karen Vogel and Vicki Noble",
        "date_earliest": 1981,
        "date_latest": 1983,
        "date_display": "1981 (designed); 1983 (first commercial edition, U.S. Games Systems)",
        "date_basis": "Designed 1978–1981 by Vogel and Noble as part of their collaborative feminist spirituality research in Berkeley, CA. Published as a commercial deck by U.S. Games Systems in 1983.",
        "date_confidence": "exact",
        "survival_status": "extant",
        "cards_known": 78,
        "cards_original": 78,
        "missing_cards": [],
        "missing_cards_unidentified_count": 0,
        "missing_cards_notes": "Continuously in print; the defining circular-format tarot deck. Accompanied by Noble's 'Motherpeace: A Way to the Goddess Through Myth, Art, and Tarot' (1983).",
        "structure": {
            "total_cards": 78,
            "suits": ["wands", "cups", "swords", "discs"],
            "ranks_per_suit": 10,
            "court_cards": 16,
            "trump_cards": 22,
            "notes": "78-card structure but circular cards (not rectangular). Court cards renamed: Daughter/Son/Priestess/Shaman replacing Page/Knight/Queen/King. Orientation on circular cards is continuous, allowing subtler gradations of 'reversal' than binary upright/reversed."
        },
        "material": "Circular commercial printed cards, color illustration",
        "technique": "Mixed media collage-style illustration (gouache, colored pencil, reference imagery)",
        "language_on_cards": "English",
        "holdings": [
            {"institution": "Continuously in print (U.S. Games Systems)", "city": "Stamford, CT", "country": "USA", "cards_held": None, "accession": None, "digitized": True, "digitization_url": None}
        ],
        "attributions": [
            {"role": "artist_designer", "name": "Karen Vogel", "confidence": "high", "notes": "American artist and feminist spirituality researcher; primary illustrator of the Motherpeace deck."},
            {"role": "designer_writer", "name": "Vicki Noble", "confidence": "high", "notes": "American feminist spirituality writer and teacher; co-designer of the deck and author of the accompanying Motherpeace book (1983)."}
        ],
        "patron": None,
        "commissioned_for": "Feminist spirituality movement of the 1970s–80s",
        "primary_purpose": "divination",
        "later_uses": ["feminist-ritual", "pedagogical", "goddess-tradition"],
        "purpose": ["divination", "feminist-spirituality", "goddess-tradition"],
        "transmission_path": "Second-wave feminist spirituality movement (1970s) → archaeological goddess-civilization research (Gimbutas, Stone) → Vogel-Noble Berkeley collaboration (1978–1981) → commercial publication by U.S. Games Systems (1983) → defining artifact of 1980s–90s feminist tarot tradition → major influence on 2000s–2020s indie-deck wave.",
        "iconography_notes": "Circular cards with no fixed orientation — a structural departure from every prior tarot. Imagery draws on reconstructed pre-patriarchal goddess iconography (Minoan, Catalhöyük, Old European), Native American and African religious imagery, and reimagined tarot archetypes centered on female figures and matriarchal reference points. Court cards rebuilt around priestess/shaman/daughter/son axes rather than king-queen-knight hierarchy.",
        "significance": "Motherpeace is the founding document of feminist tarot and arguably of the entire post-RWS indie-deck era. It proves that the tarot structure (78 cards, 22 trumps, 4 suits) can carry a symbolic system radically different from the medieval-Christian-patriarchal framework it grew up in. Every indie deck that reframes tarot through a new cultural or political lens (queer, Afrofuturist, decolonial, ecological) is working in the Motherpeace lineage.",
        "tags": ["feminist-tarot", "goddess-tradition", "circular", "indie-era-origin", "20th-century", "reframed-structure", "post-rws"],
        "sources": [
            "Noble, Vicki. Motherpeace: A Way to the Goddess Through Myth, Art, and Tarot. Harper & Row, 1983.",
            "Vogel, Karen and Vicki Noble. Motherpeace Tarot (booklet). U.S. Games Systems, 1983.",
            "Graf, Susan Johnston. Women and Tarot. Ithaca Press, 2015."
        ],
        "region": "Berkeley, CA / USA",
        "culture": "Second-wave feminist spirituality, American 20th c."
    },
]

# ---------------------------------------------------------------------------
# NEW GENEALOGY EDGES
# ---------------------------------------------------------------------------
NEW_EDGES = [
    # --- Tier A: 15th c. structural ---
    {"from": "visconti-sforza", "to": "pierpont-morgan-bergamo-c1500", "relation": "parallel_workshop_tradition",
     "notes": "PMB is a third Bembo-circle Milanese deck, distinct from but stylistically continuous with Visconti-Sforza. Both descend from the same Cremona/Milan Bembo-workshop environment."},
    {"from": "pierpont-morgan-bergamo-c1500", "to": "cary-sheet-c1500", "relation": "same_iconographic_period",
     "notes": "PMB (luxury hand-painted) and Cary Sheet (mass-produced woodblock) are near-contemporary witnesses to the stabilization of Milanese tarot iconography c.1500."},
    {"from": "cary-sheet-c1500", "to": "rosenwald-sheet-c1500", "relation": "parallel_printed_tradition",
     "notes": "Cary and Rosenwald sheets together are the two primary witnesses to early printed Italian tarot; both date to c.1500 and preserve the canonical Milanese/Order-A trump sequence."},
    {"from": "steele-sermon-c1495", "to": "cary-sheet-c1500", "relation": "canonical_order_evidence",
     "notes": "Steele Sermon records the trump order in writing c.1495; Cary and Rosenwald sheets instantiate that order in printed imagery c.1500."},
    {"from": "steele-sermon-c1495", "to": "rosenwald-sheet-c1500", "relation": "canonical_order_evidence",
     "notes": "Rosenwald trump sheet ordering matches the Steele Sermon's 'Order A' Milanese sequence, providing image-plus-text confirmation of the canonical pre-Marseille trump sequence."},
    {"from": "visconti-di-modrone", "to": "ferrara-este-c1470", "relation": "parallel_regional_tradition",
     "notes": "Ferrarese Este commissions represent a third major 15th c. tarot production center alongside the Milanese Visconti-lineage decks, proving early tarot was cross-regional."},
    {"from": "ferrara-este-c1470", "to": "sola-busca", "relation": "regional_iconographic_continuity",
     "notes": "The Ferrara-Este and Sola-Busca (also Ferrarese attribution) decks together establish a distinct Emilian iconographic lineage parallel to the Milanese Visconti tradition."},
    {"from": "steele-sermon-c1495", "to": "visconti-sforza", "relation": "canonical_order_evidence",
     "notes": "Steele Sermon's trump order matches the implied ordering of the Visconti-Sforza trumps (where extant), establishing that the canonical Milanese/Order-A sequence was shared between luxury and documentary traditions."},

    # --- Tier B: Marseille lineage fills ---
    {"from": "tarot-de-marseille-noblet", "to": "madenie-1709", "relation": "ancestor",
     "notes": "Noblet's Paris Type I Marseille (c.1650) informs but does not directly copy the Dijon Type II tradition Madenié represents (1709). Both derive from the broader 17th c. French tarot workshop environment."},
    {"from": "madenie-1709", "to": "tarot-de-marseille-dodal", "relation": "typographic_sibling",
     "notes": "Madenié (Dijon, 1709) and Dodal (Lyon, c.1701–1715) are near-contemporary Type II Marseille exemplars sharing the canonical iconographic program that Conver 1761 later propagates."},
    {"from": "madenie-1709", "to": "marseille-conver-1761", "relation": "direct_typographic_source",
     "notes": "Conver's 1761 Marseille is typographically and iconographically closest to the Madenié 1709 line, confirming Madenié as the definitive early 18th c. anchor for the Type II Marseille canon Conver then propagates globally."},
    {"from": "marseille-conver-1761", "to": "grimaud-marteau-1930", "relation": "direct_descendant",
     "notes": "Paul Marteau's 1930 Grimaud Marseille is a direct line-drawing and palette adaptation of the Conver-lineage Marseille tradition, produced for 20th c. French commercial distribution."},

    # --- Tier C: 20th c. post-RWS / esoteric ---
    {"from": "rider-waite-smith", "to": "aquarian-palladini-1970", "relation": "direct_derivative",
     "notes": "Palladini's Aquarian preserves Smith's scenic pip compositions and reworks the trumps in Art Nouveau/Deco idiom, establishing the post-RWS 'illustrated art deck' template."},
    {"from": "golden-dawn-corpus", "to": "hermetic-dowson-1979", "relation": "direct_intellectual_source",
     "notes": "Dowson's Hermetic Tarot is a synthetic reconstruction of the Golden Dawn ritual-paper imagery, the most faithful GD-tradition deck after the Thoth."},
    {"from": "thoth-tarot", "to": "hermetic-dowson-1979", "relation": "iconographic_reference",
     "notes": "The Hermetic borrows some Crowley-Harris decisions (e.g., the GD court rank structure Princess/Prince/Queen/Knight) while departing from Harris's Deco abstraction in favor of dense GD-ritualist linework."},
    {"from": "rider-waite-smith", "to": "motherpeace-1981", "relation": "reframed_derivative",
     "notes": "Motherpeace retains the 78-card / 22-trump / 4-suit RWS structural skeleton while replacing nearly every iconographic and symbolic choice with reconstructed pre-patriarchal goddess imagery — the founding precedent for the post-RWS structural-reframe tradition."},
]

# ---------------------------------------------------------------------------
# NEW CARD WITNESSES
# ---------------------------------------------------------------------------
NEW_WITNESSES = [
    {"_comment": "═══ Rosenwald Sheet ═══"},
    {"deck_id": "rosenwald-sheet-c1500", "card_id": "major-21", "present": True, "borrowing_source": None, "confidence": "confirmed",
     "notes": "The World on the Rosenwald trump sheet shows the characteristic mandorla composition with the dancing figure inside, corroborating the iconographic stabilization of this trump by c.1500."},
    {"deck_id": "rosenwald-sheet-c1500", "card_id": "major-13", "present": True, "borrowing_source": None, "confidence": "confirmed",
     "notes": "Death card present on Rosenwald sheet with the skeleton-with-scythe iconography that persists through the Marseille tradition."},
    {"deck_id": "rosenwald-sheet-c1500", "card_id": "major-00", "present": True, "borrowing_source": None, "confidence": "high",
     "notes": "Fool figure present; with the Rosenwald Fool we can see the un-numbered wanderer form stabilized as early as c.1500 in mass-produced Italian tarot."},

    {"_comment": "═══ Steele Sermon (document, not images) ═══"},
    {"deck_id": "steele-sermon-c1495", "card_id": "major-01", "present": True, "borrowing_source": None, "confidence": "confirmed",
     "notes": "Steele lists 'Bagatella' (the Magician/Juggler) as the first trump, establishing the canonical position of card I in the pre-Marseille Milanese order."},
    {"deck_id": "steele-sermon-c1495", "card_id": "major-00", "present": True, "borrowing_source": None, "confidence": "confirmed",
     "notes": "Steele's sermon lists 'el matto' (the Fool) at the end of the trump sequence, establishing the canonical Fool-outside-the-sequence status by c.1495."},
    {"deck_id": "steele-sermon-c1495", "card_id": "major-21", "present": True, "borrowing_source": None, "confidence": "confirmed",
     "notes": "Steele lists 'el mondo' (the World) second-to-last before the Fool, establishing the canonical World-as-culmination position that persists through RWS."},

    {"_comment": "═══ Pierpont-Morgan Bergamo (PMB) ═══"},
    {"deck_id": "pierpont-morgan-bergamo-c1500", "card_id": "major-15", "present": False, "borrowing_source": None, "confidence": "confirmed",
     "notes": "The Devil is definitively absent from the surviving PMB set; the card now in some reconstructions is a later 17th c. replacement, not original Bembo-circle work."},
    {"deck_id": "pierpont-morgan-bergamo-c1500", "card_id": "major-16", "present": False, "borrowing_source": None, "confidence": "confirmed",
     "notes": "The Tower also missing from original PMB holdings; a 17th c. replacement exists in the deck's reconstruction but is not original to the Bembo-circle commission."},
    {"deck_id": "pierpont-morgan-bergamo-c1500", "card_id": "major-02", "present": True, "borrowing_source": "visconti-sforza", "confidence": "high",
     "notes": "Popess (Papesse) present and iconographically continuous with Visconti-Sforza, consistent with Bembo-circle stylistic inheritance."},

    {"_comment": "═══ Ferrara / Este Tarocchi ═══"},
    {"deck_id": "ferrara-este-c1470", "card_id": "major-07", "present": True, "borrowing_source": None, "confidence": "high",
     "notes": "Chariot fragment attributed to Ferrara Este commission shows the Ferrarese court-workshop style with Este heraldic references, distinct from Milanese Chariot iconography."},
    {"deck_id": "ferrara-este-c1470", "card_id": "major-10", "present": True, "borrowing_source": None, "confidence": "medium",
     "notes": "Wheel of Fortune fragment preserved in the Yale Cary collection Ferrara attribution, showing the early Ferrarese treatment of the wheel motif."},

    {"_comment": "═══ Madenié 1709 ═══"},
    {"deck_id": "madenie-1709", "card_id": "major-18", "present": True, "borrowing_source": "tarot-de-marseille-noblet", "confidence": "confirmed",
     "notes": "The Moon on Madenié 1709 shows the canonical Marseille Type II iconography (two dogs, crayfish, two towers) in its earliest dated form, anchoring the tradition Conver 1761 later propagates."},
    {"deck_id": "madenie-1709", "card_id": "major-12", "present": True, "borrowing_source": None, "confidence": "confirmed",
     "notes": "The Hanged Man on Madenié shows the distinctive double-cord binding and T-frame gallows that become the Type II Marseille standard."},
    {"deck_id": "madenie-1709", "card_id": "major-08", "present": True, "borrowing_source": None, "confidence": "confirmed",
     "notes": "Justice at position VIII (not XI as in RWS) and Strength at XI confirms the Marseille Type II ordering was stable by 1709 — the canonical pre-Golden-Dawn Marseille sequence."},

    {"_comment": "═══ Grimaud-Marteau 1930 ═══"},
    {"deck_id": "grimaud-marteau-1930", "card_id": "major-02", "present": True, "borrowing_source": "marseille-conver-1761", "confidence": "confirmed",
     "notes": "The Papesse is preserved in the Grimaud tradition (unlike the Besançon/1JJ Swiss tradition which replaced her with Juno), following the Conver-lineage Marseille canon directly."},
    {"deck_id": "grimaud-marteau-1930", "card_id": "major-13", "present": True, "borrowing_source": "marseille-conver-1761", "confidence": "confirmed",
     "notes": "Death is unnumbered on the Grimaud-Marteau (as on Conver), preserving the traditional unnumbered Arcanum XIII convention of the Marseille Type II tradition."},

    {"_comment": "═══ Aquarian (Palladini) 1970 ═══"},
    {"deck_id": "aquarian-palladini-1970", "card_id": "major-01", "present": True, "borrowing_source": "rider-waite-smith", "confidence": "confirmed",
     "notes": "The Magician on Palladini preserves the RWS altar-and-tools composition (wand, cup, sword, pentacle on table) but stylizes the figure in Art Nouveau linework — the template for post-RWS 'art deck' composition."},
    {"deck_id": "aquarian-palladini-1970", "card_id": "cups-03", "present": True, "borrowing_source": "rider-waite-smith", "confidence": "confirmed",
     "notes": "Three of Cups preserves Smith's three-figures-toasting composition in Palladini's Deco idiom, typical of the Aquarian's faithful-to-Smith Minor Arcana treatment."},

    {"_comment": "═══ Hermetic (Dowson) 1979 ═══"},
    {"deck_id": "hermetic-dowson-1979", "card_id": "major-00", "present": True, "borrowing_source": "golden-dawn-corpus", "confidence": "confirmed",
     "notes": "The Fool on Dowson's Hermetic bears the Hebrew letter Aleph prominently and the Golden Dawn ritual attributions — an informationally maximal card reflecting the deck's function as a ritual document."},
    {"deck_id": "hermetic-dowson-1979", "card_id": "major-15", "present": True, "borrowing_source": "thoth-tarot", "confidence": "high",
     "notes": "The Devil (Ayin / Capricorn) shows clear continuity with Harris-Crowley Thoth symbolism in its densely allegorical treatment, confirming the Thoth as intermediary between original GD papers and Dowson."},

    {"_comment": "═══ Motherpeace 1981 ═══"},
    {"deck_id": "motherpeace-1981", "card_id": "major-02", "present": True, "borrowing_source": None, "confidence": "confirmed",
     "notes": "The Priestess on Motherpeace is reimagined as a pre-patriarchal Mediterranean goddess-figure (Minoan snake-goddess lineage), the defining Motherpeace move of keeping the structural position while replacing the Western-Christian-patriarchal content."},
    {"deck_id": "motherpeace-1981", "card_id": "major-03", "present": True, "borrowing_source": None, "confidence": "confirmed",
     "notes": "The Empress is recast as an earth-mother / goddess-of-abundance figure drawing on reconstructed Paleolithic Venus iconography, showing Motherpeace's use of archaeological goddess-civilization research as source material."},
    {"deck_id": "motherpeace-1981", "card_id": "court-page-of-pentacles", "present": True, "borrowing_source": None, "confidence": "confirmed",
     "notes": "Court rank is 'Daughter of Discs' rather than 'Page of Pentacles', one of the Motherpeace structural renames (Daughter/Son/Priestess/Shaman) that reframe the hierarchical RWS court-card system."},
]

# ---------------------------------------------------------------------------
# RUN
# ---------------------------------------------------------------------------
def main():
    # Load
    decks_data = json.loads(DECKS_FILE.read_text(encoding="utf-8"))
    wit_data = json.loads(WIT_FILE.read_text(encoding="utf-8"))

    # Dedup-safety: check IDs not already present
    existing_ids = {d["id"] for d in decks_data["decks"]}
    to_add_decks = [d for d in NEW_DECKS if d["id"] not in existing_ids]
    skipped = [d["id"] for d in NEW_DECKS if d["id"] in existing_ids]
    if skipped:
        print(f"Skipping already-present decks: {skipped}")

    decks_data["decks"].extend(to_add_decks)
    decks_data["genealogy"].extend(NEW_EDGES)
    wit_data["witnesses"].extend(NEW_WITNESSES)

    DECKS_FILE.write_text(json.dumps(decks_data, indent=2, ensure_ascii=False), encoding="utf-8")
    WIT_FILE.write_text(json.dumps(wit_data, indent=2, ensure_ascii=False), encoding="utf-8")

    # Report
    real_witnesses = [w for w in wit_data["witnesses"] if "_comment" not in w]
    print(f"OK")
    print(f"  decks:     {len(decks_data['decks'])} (+{len(to_add_decks)})")
    print(f"  edges:     {len(decks_data['genealogy'])} (+{len(NEW_EDGES)})")
    print(f"  witnesses: {len(real_witnesses)} (+{sum(1 for w in NEW_WITNESSES if '_comment' not in w)})")


if __name__ == "__main__":
    main()
