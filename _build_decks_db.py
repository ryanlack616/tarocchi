"""
_build_decks_db.py — build tarocchi/data/decks.db from historical_decks.json + card_witnesses.json

Tables:
  decks          — one row per card set
  holdings       — institution locations for each deck
  attributions   — roles/names/confidence per deck
  genealogy      — typed edge list (deck → deck)
  deck_tags      — flat tag index

Run: python _build_decks_db.py
Validates on the way in; prints a summary on success.
"""

import json
import sqlite3
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"
SOURCE = DATA_DIR / "historical_decks.json"
WITNESSES_SRC = DATA_DIR / "card_witnesses.json"
DB = DATA_DIR / "decks.db"

REQUIRED_DECK_FIELDS = [
    "id", "name", "region", "culture",
    "date_earliest", "date_latest", "date_display", "date_basis", "date_confidence",
    "survival_status", "cards_known", "cards_original",
    "structure", "holdings", "attributions", "significance",
]

VALID_SURVIVAL = {"extant", "fragmentary", "documented", "lost"}
VALID_DATE_CONF = {"exact", "high", "medium", "low"}
VALID_GENEALOGY_RELATIONS = {
    "ancestor", "same_workshop_tradition", "parallel_workshop",
    "ancestor_via_woodblock_tradition", "reaction_against",
    "direct_iconographic_source", "parallel_golden_dawn_tradition",
    "parallel_regional_variant", "copy_of", "influenced_by", "derives_from",
    "esoteric_source_material",
    # Extended — added as corpus grew:
    "parallel_paris_tradition", "direct_reference_source",
    "direct_intellectual_source", "piracy_continuation",
    "iconographic_reference", "direct_derivative",
    "canonical_order_evidence", "parallel_regional_tradition",
    "regional_iconographic_continuity", "parallel_printed_tradition",
    "same_iconographic_period", "parallel_workshop_tradition",
    "typographic_sibling", "direct_typographic_source",
    "direct_descendant", "reframed_derivative", "companion_text",
}

VALID_PRIMARY_PURPOSE = {
    "gaming", "cartomancy", "divination", "esoteric", "esoteric_system",
    "unknown", "aristocratic_display",
    # Extended:
    "esoteric_theory", "esoteric_study", "intellectual_system",
    "theological-critique",
}

VALID_TAGS = set()  # Open vocabulary — tags are not enumerated


def validate(data):
    errors = []
    ids = set()
    for d in data["decks"]:
        did = d.get("id", "<missing_id>")
        if did in ids:
            errors.append(f"Duplicate deck id: {did}")
        ids.add(did)
        for f in REQUIRED_DECK_FIELDS:
            if f not in d:
                errors.append(f"{did}: missing required field '{f}'")
        if d.get("survival_status") not in VALID_SURVIVAL:
            errors.append(f"{did}: survival_status must be one of {VALID_SURVIVAL}")
        if d.get("date_confidence") not in VALID_DATE_CONF:
            errors.append(f"{did}: date_confidence must be one of {VALID_DATE_CONF}")
        if d.get("date_earliest") and d.get("date_latest"):
            if d["date_earliest"] > d["date_latest"]:
                errors.append(f"{did}: date_earliest > date_latest")
        for h in d.get("holdings", []):
            if not h.get("institution"):
                errors.append(f"{did}: holding missing institution")
        for a in d.get("attributions", []):
            if not a.get("role") or not a.get("name"):
                errors.append(f"{did}: attribution missing role or name")

    for edge in data.get("genealogy", []):
        if edge.get("relation") not in VALID_GENEALOGY_RELATIONS:
            errors.append(f"Genealogy edge {edge.get('from')}→{edge.get('to')}: unknown relation '{edge.get('relation')}'")
        if edge.get("from") not in ids:
            errors.append(f"Genealogy edge: unknown source id '{edge.get('from')}'")
        if edge.get("to") not in ids:
            errors.append(f"Genealogy edge: unknown target id '{edge.get('to')}'")

    # Holdings integrity: sum(cards_held) should equal cards_known for fragmentary
    # survivors (single artifact split across institutions).  For extant/documented
    # decks, multiple institutions may each hold complete independent copies, so the
    # sum legitimately exceeds cards_known.  Only enforce for fragmentary decks.
    for d in data["decks"]:
        did = d.get("id", "?")
        known = d.get("cards_known")
        if known is not None and known > 0 and d.get("survival_status") == "fragmentary":
            held_total = sum(h.get("cards_held") or 0 for h in d.get("holdings", []))
            if held_total > 0 and held_total != known:
                errors.append(
                    f"{did}: holdings sum {held_total} ≠ cards_known {known} "
                    f"(unlocated cards or data error)"
                )

    # Orphan nodes: decks with no genealogy edges at all
    # (skip decks marked genealogy_isolated — intentional independent lineages)
    edge_participants = set()
    for edge in data.get("genealogy", []):
        edge_participants.add(edge.get("from"))
        edge_participants.add(edge.get("to"))
    for d in data["decks"]:
        if d["id"] not in edge_participants and not d.get("genealogy_isolated"):
            errors.append(f"{d['id']}: orphan — no genealogy edges (in or out)")

    # Circular genealogy (simple pair check — not full cycle detection)
    edge_set = {(e["from"], e["to"]) for e in data.get("genealogy", [])}
    for (a, b) in edge_set:
        if (b, a) in edge_set:
            errors.append(f"Circular genealogy pair: {a} ↔ {b}")

    # primary_purpose vocabulary (warn only — not all decks may have it yet)
    for d in data["decks"]:
        pp = d.get("primary_purpose")
        if pp and pp not in VALID_PRIMARY_PURPOSE:
            errors.append(f"{d['id']}: unknown primary_purpose '{pp}'")

    return errors


def build(data, db_path):
    if db_path.exists():
        db_path.unlink()

    con = sqlite3.connect(db_path)
    cur = con.cursor()

    cur.executescript("""
        CREATE TABLE decks (
            id                TEXT PRIMARY KEY,
            name              TEXT NOT NULL,
            name_local        TEXT,
            region            TEXT,
            culture           TEXT,
            date_earliest     INTEGER,
            date_latest       INTEGER,
            date_display      TEXT,
            date_basis        TEXT,
            date_confidence   TEXT CHECK(date_confidence IN ('exact','high','medium','low')),
            survival_status   TEXT CHECK(survival_status IN ('extant','fragmentary','documented','lost')),
            cards_known       INTEGER,
            cards_original    INTEGER,

            -- structure fields (flattened)
            struct_total      INTEGER,
            struct_suits      TEXT,           -- JSON array
            struct_ranks_per_suit INTEGER,
            struct_court_cards TEXT,          -- JSON array
            struct_trump_cards INTEGER,
            struct_notes      TEXT,

            material          TEXT,           -- JSON array
            technique         TEXT,           -- JSON array
            language_on_cards TEXT,           -- JSON array
            patron            TEXT,
            commissioned_for  TEXT,
            primary_purpose   TEXT,
            later_uses        TEXT,           -- JSON array of {use, date_earliest, notes}
            purpose           TEXT,           -- JSON array (legacy)
            transmission_path TEXT,
            iconography_notes TEXT,
            significance      TEXT,
            sources           TEXT,           -- JSON array
            raw_json          TEXT            -- full original object for any fields not promoted
        );

        CREATE TABLE missing_cards (
            id           INTEGER PRIMARY KEY AUTOINCREMENT,
            deck_id      TEXT NOT NULL REFERENCES decks(id),
            card_id      TEXT,               -- NULL = unidentified
            identified   INTEGER NOT NULL CHECK(identified IN (0,1)),
            notes        TEXT
        );

        CREATE TABLE card_witnesses (
            id           INTEGER PRIMARY KEY AUTOINCREMENT,
            deck_id      TEXT NOT NULL REFERENCES decks(id),
            card_id      TEXT NOT NULL,
            present      INTEGER NOT NULL CHECK(present IN (0,1)),
            borrowing_source TEXT,           -- deck_id this card was borrowed FROM
            confidence   TEXT,               -- open vocab: confirmed/probable/possible/disputed/high/medium
            notes        TEXT
        );

        CREATE TABLE holdings (
            id           INTEGER PRIMARY KEY AUTOINCREMENT,
            deck_id      TEXT NOT NULL REFERENCES decks(id),
            institution  TEXT NOT NULL,
            city         TEXT,
            country      TEXT,
            cards_held   INTEGER,
            accession    TEXT,
            digitized    INTEGER CHECK(digitized IN (0,1)),
            digitization_url TEXT
        );

        CREATE TABLE attributions (
            id           INTEGER PRIMARY KEY AUTOINCREMENT,
            deck_id      TEXT NOT NULL REFERENCES decks(id),
            role         TEXT NOT NULL,
            name         TEXT NOT NULL,
            confidence   TEXT CHECK(confidence IN ('high','medium','low')),
            notes        TEXT
        );

        CREATE TABLE genealogy (
            id       INTEGER PRIMARY KEY AUTOINCREMENT,
            from_id  TEXT NOT NULL REFERENCES decks(id),
            to_id    TEXT NOT NULL REFERENCES decks(id),
            relation TEXT NOT NULL,
            notes    TEXT
        );

        CREATE TABLE deck_tags (
            deck_id TEXT NOT NULL REFERENCES decks(id),
            tag     TEXT NOT NULL,
            PRIMARY KEY (deck_id, tag)
        );

        CREATE INDEX idx_holdings_deck      ON holdings(deck_id);
        CREATE INDEX idx_attrib_deck        ON attributions(deck_id);
        CREATE INDEX idx_genealogy_from     ON genealogy(from_id);
        CREATE INDEX idx_genealogy_to       ON genealogy(to_id);
        CREATE INDEX idx_tags_tag           ON deck_tags(tag);
        CREATE INDEX idx_missing_deck       ON missing_cards(deck_id);
        CREATE INDEX idx_witnesses_deck     ON card_witnesses(deck_id);
        CREATE INDEX idx_witnesses_card     ON card_witnesses(card_id);
    """)

    for d in data["decks"]:
        s = d.get("structure", {})
        cur.execute("""
            INSERT INTO decks VALUES (
                ?,?,?,?,?,?,?,?,?,?,?,?,?,
                ?,?,?,?,?,?,
                ?,?,?,?,?,?,?,?,?,?,?,?,?
            )
        """, (
            d["id"],
            d["name"],
            d.get("name_local"),
            d.get("region"),
            d.get("culture"),
            d.get("date_earliest"),
            d.get("date_latest"),
            d.get("date_display"),
            d.get("date_basis"),
            d.get("date_confidence"),
            d.get("survival_status"),
            d.get("cards_known"),
            d.get("cards_original"),
            s.get("total_cards"),
            json.dumps(s.get("suits", [])),
            s.get("ranks_per_suit"),
            json.dumps(s.get("court_cards", [])),
            s.get("trump_cards"),
            s.get("notes"),
            json.dumps(d.get("material", [])),
            json.dumps(d.get("technique", [])),
            json.dumps(d.get("language_on_cards", [])),
            d.get("patron"),
            d.get("commissioned_for"),
            d.get("primary_purpose"),
            json.dumps(d.get("later_uses", [])),
            json.dumps(d.get("purpose", [])),
            d.get("transmission_path"),
            d.get("iconography_notes"),
            d.get("significance"),
            json.dumps(d.get("sources", [])),
            json.dumps(d),
        ))

        # missing_cards
        mc_identified = d.get("missing_cards", [])
        mc_notes = d.get("missing_cards_notes")
        for cid in mc_identified:
            cur.execute(
                "INSERT INTO missing_cards (deck_id, card_id, identified, notes) VALUES (?,?,1,?)",
                (d["id"], cid, mc_notes),
            )
        unid_count = d.get("missing_cards_unidentified_count") or 0
        if unid_count > 0:
            for _ in range(unid_count):
                cur.execute(
                    "INSERT INTO missing_cards (deck_id, card_id, identified, notes) VALUES (?,NULL,0,?)",
                    (d["id"], mc_notes),
                )

        for h in d.get("holdings", []):
            cur.execute("""
                INSERT INTO holdings (deck_id, institution, city, country, cards_held, accession, digitized, digitization_url)
                VALUES (?,?,?,?,?,?,?,?)
            """, (
                d["id"],
                h["institution"],
                h.get("city"),
                h.get("country"),
                h.get("cards_held"),
                h.get("accession"),
                1 if h.get("digitized") else 0,
                h.get("digitization_url"),
            ))

        for a in d.get("attributions", []):
            cur.execute("""
                INSERT INTO attributions (deck_id, role, name, confidence, notes)
                VALUES (?,?,?,?,?)
            """, (
                d["id"],
                a["role"],
                a["name"],
                a.get("confidence"),
                a.get("notes"),
            ))

        for tag in d.get("tags", []):
            cur.execute("INSERT INTO deck_tags VALUES (?,?)", (d["id"], tag))

    for edge in data.get("genealogy", []):
        cur.execute("""
            INSERT INTO genealogy (from_id, to_id, relation, notes)
            VALUES (?,?,?,?)
        """, (edge["from"], edge["to"], edge["relation"], edge.get("notes")))

    # card_witnesses (loaded from separate file)
    if WITNESSES_SRC.exists():
        wdata = json.loads(WITNESSES_SRC.read_text(encoding="utf-8"))
        for w in wdata.get("witnesses", []):
            if "_comment" in w:
                continue
            cur.execute("""
                INSERT INTO card_witnesses (deck_id, card_id, present, borrowing_source, confidence, notes)
                VALUES (?,?,?,?,?,?)
            """, (
                w["deck_id"],
                w["card_id"],
                1 if w.get("present") else 0,
                w.get("borrowing_source"),
                w.get("confidence"),
                w.get("notes"),
            ))

    con.commit()
    con.close()


def summary(db_path):
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    decks = cur.execute("SELECT COUNT(*) FROM decks").fetchone()[0]
    holdings = cur.execute("SELECT COUNT(*) FROM holdings").fetchone()[0]
    attribs = cur.execute("SELECT COUNT(*) FROM attributions").fetchone()[0]
    edges = cur.execute("SELECT COUNT(*) FROM genealogy").fetchone()[0]
    tags = cur.execute("SELECT COUNT(*) FROM deck_tags").fetchone()[0]
    missing = cur.execute("SELECT COUNT(*) FROM missing_cards WHERE card_id IS NOT NULL").fetchone()[0]
    witnesses = cur.execute("SELECT COUNT(*) FROM card_witnesses").fetchone()[0]

    print(f"\n  decks.db built — {db_path}")
    print(f"  decks:        {decks}")
    print(f"  holdings:     {holdings}")
    print(f"  attributions: {attribs}")
    print(f"  genealogy:    {edges} edges")
    print(f"  tags:         {tags}")
    print(f"  missing cards:{missing} identified")
    print(f"  witnesses:    {witnesses}")

    print("\n  Deck list (oldest → newest):")
    rows = cur.execute(
        "SELECT id, name, date_display, survival_status, cards_known, cards_original, primary_purpose FROM decks ORDER BY date_earliest"
    ).fetchall()
    for r in rows:
        ck, co = r[4], r[5]
        if ck is None:
            frac = "docs only"
        elif ck == co:
            frac = "complete"
        else:
            frac = f"{ck}/{co}"
        pp = r[6] or ""
        print(f"    {r[1][:38]:<38}  {r[2]:<32}  {r[3]:<12}  {frac:<12}  {pp}")

    print("\n  Genealogy edges:")
    edges_rows = cur.execute(
        "SELECT from_id, to_id, relation FROM genealogy ORDER BY from_id"
    ).fetchall()
    for r in edges_rows:
        print(f"    {r[0]} → {r[1]}  [{r[2]}]")

    con.close()


if __name__ == "__main__":
    print(f"Loading {SOURCE}...")
    data = json.loads(SOURCE.read_text(encoding="utf-8"))

    errors = validate(data)
    if errors:
        print(f"\n  {len(errors)} validation error(s):")
        for e in errors:
            print(f"    ! {e}")
        raise SystemExit(1)

    print(f"  {len(data['decks'])} decks, {len(data.get('genealogy', []))} genealogy edges — valid.")
    build(data, DB)
    summary(DB)
    print("\nDone.\n")
