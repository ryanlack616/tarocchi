# AGENTS.md — tarocchi

> Scaffolded from disk facts on 2026-11-15. UNVERIFIED means: written from the filesystem, not from understanding. Verify before trusting.

## Top level

```
.git .gitignore CNAME PLANS.md README.md __pycache__ _add_crowley.py _add_decks.py _add_deep.py _add_next_wave.py _add_wave3.py _add_wave4.py _build_decks_db.py _check_deploy.py _clean_manifest.py _deploy.py _deploy_images.py _dl_card_images.py _dl_conver_gaps.py _dl_missing_aces.py _dl_more_decks.py _dl_v3.log _dl_v3_targeted.py _find_aces.py _find_conver_gaps.py _fix_manifest.py _inspect.py _inspect_decks.py _probe_commons.py _probe_results.txt _validate.py data explorer.html index.html scripts
```

## Type (guessed from markers)

- UNVERIFIED: no build markers found; may be misclassified or not a software project.

## From README.md (verbatim head)

```
# tarocchi.help

Tarot reading and tarot history, built as a dependency-light static site.

> The cards help you think.

## What's Included

- A 78-card tarot reader with five spreads:
  - Daily Draw
  - Past / Present / Future
  - Horseshoe
  - Celtic Cross
  - Year Ahead
- Upright and reversed card readings
- Local deterministic synthesis with no API key or backend
- Share links and a local reading journal
- Dark and light themes
- Minimal inline SVG card art
- Historical explorer with timeline, genealogy, witnesses, people, cards, and lineage views
- Historical corpus covering 49 decks, 83 genealogy edges, and 237 card witnesses

## Run Locally

The pages use `fetch()` to load JSON, so serve the repository over HTTP rather than opening `index.html` directly.

```bash
python3 -m http.server 8000
```

Open:

- <http://localhost:8000/index.html>
- <http://localhost:8000/explorer.html>

## Validate

Validate the 78-card corpus:

```bash
python3 _validate.py
```

Rebuild the optional SQLite historical database:

```bash
python3 _build_decks_db.py
```

The project also uses browser smoke tests during development to verify the reader flows, image loading, and explorer tabs.

## Project
```

## Recent commits (git log, verbatim)

```
cc1b022 Add project README
c725603 Normalize maintenance and data tooling
41fc376 Expand deck corpus and harden static reader
1362460 Add CNAME + update data/html for GitHub Pages deploy
ef30c83 initial commit — tarocchi.help tarot reading SPA
```

## What agents should know

- **UNVERIFIED — verify by reading the code, not this file.**
- What this project is for: UNVERIFIED
- How to verify current state (tests/build): UNVERIFIED
- What NOT to touch: UNVERIFIED
- Working conventions (style, naming, tests): UNVERIFIED

## Red flags found on disk

- total size: 148M
- zero-byte files (excluding venv/node_modules): 1

Fill in the UNVERIFIED sections by reading the code. Do not treat this file as ground truth until they are gone.
