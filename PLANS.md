# tarocchi.help — Project Plans

**Domain:** tarocchi.help (Porkbun static hosting)
**Concept:** A serious, AI-powered tarot reading tool. "The cards help you think."
**Stack:** Single-file HTML SPA, vanilla JS, CSS 3D, speed_layer AI interpretation
**Aesthetic:** Deep violet/candlelight gold, Cormorant Garamond serif + IBM Plex Mono, dark background
**Deck art:** Minimal symbolic SVG design (original, not Rider-Waite raster)

---

## Phase 1 — Corpus: `data/cards.json` ✓ COMPLETE

Full 78-card structured dataset. The UMF of tarot.

Schema per card:
```json
{
  "id": "major-00",
  "number": 0,
  "name": "The Fool",
  "name_it": "Il Matto",
  "arcana": "major",
  "suit": null,
  "element": "Air",
  "planet": null,
  "zodiac": "Uranus",
  "hebrew_letter": "Aleph",
  "keywords": ["beginnings", "spontaneity", "a leap of faith"],
  "shadow_keywords": ["recklessness", "naivety", "poor judgment"],
  "upright_meaning": "New beginnings, innocence, spontaneity, a free spirit",
  "reversed_meaning": "Holding back, recklessness, risk-taking",
  "archetype": "The Innocent",
  "numerology": "0 — unlimited potential, the void before creation",
  "visual_symbols": ["cliff", "white dog", "bindle", "sun", "flower"],
  "traditional_phrases": ["Le Mat", "The Unnumbered Card"]
}
```

Also includes `data/spreads.json` — 5 spread layouts:
- Daily Single (1 card)
- Past / Present / Future (3 cards)
- Celtic Cross (10 cards)
- Horseshoe (7 cards)
- Year Ahead (13 cards, one per month + synthesis)

Validation: `_build_cards.py` — checks all 78, required fields, no missing suits, completeness score.

---

## Phase 2 — Reader SPA: `index.html`

Single-file SPA. No dependencies except Google Fonts CDN.

### UI Flow
1. **Landing** — title "tarocchi.help", subtitle "the cards help you think", [Begin Reading] button
2. **Choose Spread** — 5 spread type cards with descriptions
3. **Shuffle** — animated card pile, click to shuffle (visual riffle)
4. **Draw** — click cards from facedown pile, fly to spread position
5. **Flip** — click each card to reveal, CSS 3D flip animation
6. **Reversed** — ~30% chance any card lands reversed, tracked in reading
7. **AI Brief** — per-card meaning tooltip on hover, full synthesis panel at bottom
8. **Share** — encode reading in URL hash (card IDs + orientations + spread), copy-link button
9. **Journal** — localStorage, last 10 readings, accessible from nav

### Card Art
- Original minimal SVGs generated inline — each Major Arcana has a unique symbol
- Minor Arcana: suit icon (wand/cup/sword/pentacle) + pip count + court figure for face cards
- Back design: geometric mandala pattern (CSS/SVG, no external images)

### AI Integration
- Uses `speed_layer` endpoint at `/ai` OR direct Anthropic API via fetch (configurable)
- Prompt pattern: position-aware, card + orientation + spread context
- Streams response into brief panel
- Graceful fallback: static meanings from cards.json if AI unavailable

### Color palette
```css
--bg: #0d0a14
--surface: #1a1428
--accent: #c9a84c      /* candlelight gold */
--accent2: #7b4fa6     /* deep violet */
--text: #e8e0f0
--muted: #7a6e8a
--card-back: #1e1632
```

### Typography
- Headings: Cormorant Garamond (Google Fonts)
- Body/UI: Inter
- AI output: IBM Plex Mono (monospace feel for "synthesis")

---

## Phase 3 — Deploy: tarocchi.help

Porkbun static hosting.
- FTP host: `pixie-ss1-ftp.porkbun.com`
- User: `tarocchi.help`
- Pass: (set after purchase)
- Files: `index.html` + `data/cards.json` + `data/spreads.json`

Same FTP upload pattern as minarealm.shop, atomus.space, pipecamp.homes.

---

## Phase 4 — Minarealm Bridge (future)

Embed lightweight version in minarealm.shop for Mara Divine / Mandy Kay pre-session readings.
- Client draws before booking, AI synthesizes brief
- CTA → book live session
- Iframe embed or separate subdomain: reader.minarealm.shop

---

## Phase 5 — Historical Decks Database ✓ SCHEMA COMPLETE

**Files:** `data/historical_decks.json` (source), `data/decks.db` (SQLite, built by `_build_decks_db.py`)

17 decks · 25 genealogy edges · 20 holdings · 27 attributions · 105 tags · 30 card witnesses

### Schema design decisions

**Dates as ranges, never a single year.** Every deck gets `date_earliest`, `date_latest`, `date_display` (human string), `date_basis` (evidence cited), `date_confidence` (exact/high/medium/low). The 1392 Charles VI court payment — often cited as "oldest tarot" — refers to plain playing cards, not tarot at all; the deck named "Charles VI Tarot" is actually c. 1440–1470. The date_basis field is where that gets recorded.

**Survival as first-class field.** `survival_status` ∈ {extant, fragmentary, documented, lost}. The Mamluk deck (15 of 52 cards) and Visconti-Sforza (74 of 78, split across 3 institutions) are both `fragmentary`. The `cards_known` vs `cards_original` pair quantifies the gap.

**Holdings are a join table.** The Visconti-Sforza is split 35/26/13 across Morgan Library (New York), Accademia Carrara (Bergamo), and Casa Colleoni. A single `location` column cannot represent this.

**Attributions carry roles and confidence.** Bonifacio Bembo gets `artist_primary` with confidence `high` for Visconti-Sforza (Sforza court association documented) but only `medium` for Visconti di Modrone (style-only attribution). Antonio Cicognara gets `low` for the replacement cards. Pamela Colman Smith gets `artist` / `high` for RWS — but note her name was omitted from the deck for decades.

**Genealogy is a typed edge list.** Not a tree — a directed graph. `sola-busca → rider-waite-smith` [direct_iconographic_source] captures that Smith lifted compositions directly. `tarot-de-marseille-dodal → rider-waite-smith` [reaction_against] captures Waite's deliberate departure.

**Structure is deck-relative.** Mamluk: 52 cards, 0 trumps, no human figures. Minchiate: 97 cards, 41 trumps, zodiac. Tarot: 78, 22 trumps. These are not deviations from a standard — they ARE the history.

### Current deck roster (oldest → newest)
| Deck | Date | Survival | Cards | Purpose |
|---|---|---|---|---|
| Tang Dynasty Leaf Game | c. 850–900 CE | documented | — | gaming |
| Mamluk Playing Cards | c. 1370–1400 | fragmentary | 15/52 | gaming |
| Spanish Naipes | c. 1371–1380 | documented | 0/52 | gaming |
| Charles VI Tarot | c. 1440–1470 | fragmentary | 17/78 | gaming |
| Visconti di Modrone | c. 1441–1447 | fragmentary | 67/78 | gaming |
| Visconti-Sforza | c. 1450–1480 | fragmentary | 74/78 | gaming |
| Sola-Busca | c. 1491–1500 | extant | 78/78 | unknown |
| Minchiate Fiorentine | c. 1500–1530 | extant | 97/97 | gaming |
| Tarot de Marseille (Geoffroy, 1557) | 1557 | fragmentary | 22/78 | gaming |
| Tarot de Besancon | c. 1650–1850 | extant | 78/78 | gaming |
| Tarot de Marseille (Dodal) | c. 1701–1715 | extant | 78/78 | gaming |
| Tarot de Marseille (Conver, 1761) | 1761 | extant | 78/78 | gaming |
| Grand Etteilla | 1789–1791 | extant | 78/78 | cartomancy |
| Golden Dawn corpus | 1888–1900 | documented | — | esoteric_system |
| Oswald Wirth (1889) | 1889 | extant | 22/22 | esoteric |
| Rider-Waite-Smith | December 1909 | extant | 78/78 | divination |
| Thoth Tarot | 1938–1943 | extant | 78/78 | divination |

### Current status (April 21, 2026)
**30 decks · 49 genealogy edges · 60 card witnesses** deployed to tarocchi.help/explorer.html.

Timeline now spans ~1000 years (Tang c.868 → B.O.T.A. 1929). The 1826–1888 theoretical gap (Lévi, Paul Christian) is closed. Bolognese (Mitelli), Swiss (1JJ), and American-esoteric (B.O.T.A.) branches now represented.

### Next wave — 9 decks to add (April 21, 2026)

Prioritized by structural necessity over completism. The 4 Tier A nodes close documented gaps in the 15th c. corpus. Tier B fills the Marseille lineage. Tier C establishes the 20th c. indie era.

**Tier A — Critical 15th c. structural nodes (4):**
- `rosenwald-sheet-c1500` — National Gallery of Art, Washington DC. Three uncut woodblock sheets (trumps, cups/coins, swords/batons). Companion to Cary Sheet; together they are the primary evidence for early printed Italian tarot.
- `steele-sermon-c1495` — *De ludo cum aliis* Franciscan sermon manuscript. Contains the earliest complete written list of the 22 trumps in canonical order. Not a deck but a document — the ur-source for the Milanese trump ordering that propagates through Marseille to RWS.
- `pierpont-morgan-bergamo-c1500` (PMB) — Third surviving Visconti-lineage deck, distinct from Visconti-Sforza. Split between Morgan Library (NY), Accademia Carrara, and Colleoni Collection. Workshop-attributed to Bembo circle.
- `ferrara-este-c1470` — Este court fragments (Yale Art Gallery + Museo Civico Ferrara). Third early regional center alongside Milan and Bologna; non-Visconti tradition.

**Tier B — Marseille lineage fills (2):**
- `madenie-1709` — Pierre Madenié, Dijon. Earliest definitive Tarot de Marseille Type II, the direct source Conver 1761 copied from. Sits between Noblet (Type I, Paris 1650) and Dodal/Conver.
- `grimaud-marteau-1930` — Paul Marteau's Grimaud recoloring. The standard 20th c. Marseille every reader used before Jodorowsky's 1997 restoration.

**Tier C — 20th c. indie / post-RWS (3):**
- `aquarian-palladini-1970` — David Palladini's Art Nouveau-influenced RWS variant. First major "mod" American deck; bridges the RWS-tradition and the indie era.
- `hermetic-dowson-1979` — Godfrey Dowson's Hermetic Tarot. Most precise visual transcription of Golden Dawn ritual symbolism ever made; companion to the Thoth.
- `motherpeace-1981` — Karen Vogel & Vicki Noble. First feminist circular deck; founding document of indie/reclaiming-era tarot; major pedagogical influence on 1980s–90s revival.

After this wave: **39 decks**, timeline extends to 1981, Marseille lineage complete from Noblet 1650 → Madenié 1709 → Dodal c.1710 → Conver 1761 → Grimaud 1930, and post-RWS indie era begins.

### Future waves (deferred)
- **Tarocco Piemontese (c.1830)** — Piedmontese regional Italian, still played
- **Crowley Book of Thoth text corpus (1944)** — textual companion to Thoth deck, mirror of Lévi 1855 pattern
- **Haindl Tarot (Hermann Haindl, 1988)** — first major ecumenical/cross-cultural deck
- **Wild Unknown (Kim Krans, 2012)** — indie minimalist pillar, influential on 2010s aesthetic
- **Spanish / Iberian Latin-suit regional variants** — Naipes Comuneros, Baraja Española; fills the Iberian gameplay branch

### Historical Explorer UI
`explorer.html` — standalone SPA that loads `data/historical_decks.json` + `data/card_witnesses.json` via fetch.
- **Timeline tab** — vertical chronological rail, click deck to expand detail panel (holdings, attributions, genealogy edges, significance)
- **Genealogy tab** — SVG force-directed graph of deck relationships; edge type color-coded; click node to highlight lineage
- **Witnesses tab** — filterable table of card borrowings across decks; filter by deck, card, confidence level
- **People tab** — key figures (Waite, Smith, Etteilla, Crowley, Harris, Bembo, Levi, Wirth, de Guaita, Jodorowsky) with dates, role, and decks affected

Same aesthetic as index.html (dark violet, Cormorant Garamond, IBM Plex Mono). Nav link from index.html.

---

## File Tree (target)
```
tarocchi/
  index.html          ← full SPA
  PLANS.md            ← this file
  data/
    cards.json        ← 78-card corpus
    spreads.json      ← 5 spread layouts
  _build_cards.py     ← validation + seed script
```

---

## Key Decisions
- No external image CDN — all art inline SVG/CSS
- No framework — vanilla JS only
- AI optional — works without it, better with it
- Public domain positioning: original art, original data schema
- `.help` TLD frames purpose: this tool helps you think, not predict

---

## Status
- [ ] Phase 1: corpus
- [ ] Phase 2: reader SPA
- [ ] Phase 3: deploy
- [ ] Phase 4: minarealm bridge
- [x] Phase 5: historical decks database (17 decks, 25 edges, 30 witnesses)
- [ ] Phase 5b: explorer.html UI
- [ ] Phase 6: minarealm bridge embed
