# STS Exam Prep (unofficial) - NPTEL 105107210

A dependency-free static web app (HTML/CSS/vanilla JS). No Node, database or server code is needed.
Folder to publish: `docs/`.

## What it is / is not
- Working prototype, tested locally in a browser (see VERIFICATION_REPORT.md).
- Progress is stored in the browser's localStorage only. **No accounts, no database, no cross-device sync.** Back up via Progress > Backup (JSON).
- Not yet deployed anywhere. Nothing here has been published or paid for.

## Run locally
```bash
cd docs && python3 -m http.server 8765   # then open http://localhost:8765
```

## Deploy (you do this; free tiers exist, accounts required)
Any static host works; upload/point to the `docs/` folder.
- **Netlify Drop**: drag the `docs/` folder onto https://app.netlify.com/drop (account needed to keep it).
- **GitHub Pages** (repo must be public on a free plan): Settings > Pages > Deploy from a branch > `main` / `docs`. Site URL: https://brucexjoker.github.io/2026-sustainable-transportation/
- **Cloudflare Pages / Vercel**: connect repo, build command none, output directory `docs`.
Custom domain: add it in the host's Domains settings and create the DNS record they show.
Service worker/offline caching works only over HTTPS (or localhost); test it after deploying.

## Update the question bank
Edit `content/questions.py`, `questions2.py`, `questions3.py` (concept questions), `content/official2021.py` (official assignments), `content/numericals.py` (numericals, answers computed in code), `content/weeks_real.py` (the real 12-week notes and flashcards; it merges older notes from `weeks_a.py`/`weeks_b.py`).
Then:
```bash
python3 content/build.py        # regenerates docs/data/data.js
python3 tests/check_data.py     # consistency tests
```
Official material (assignments/PYQs) must carry real `source` metadata (type, year, url); the tests reject anything generated that claims a year/URL.

## Adding cross-device sync later
Needs a backend (e.g. Supabase: auth + `attempts`, `bookmarks`, `progress` tables with row-level security; answer keys in a read-only table). Not implemented here.

## Adding official assignments for 2022-2025
Create `content/official2022.py` (or 2023/2024/2025) with `P = [...]` in the same tuple format as `content/official2026.py`:
`(week, q_no, text, [options], 'a'|'b'|'c'|'d'|'e', 'key', explanation)`, optionally `HOW = "where it came from"`. Then run `python3 content/build.py` and `python3 tests/check_data.py`. The build merges questions identical to an earlier year (listed under both years) and warns if the two years' keys disagree. The "Official assignments (by year)" page already has tabs for 2021-2026.

## Question categories
- **Official assignments** (green star): 2021 and 2026 so far, grouped by year on the Official page.
- **Self-made practice (reviewed)**: written for this app; answers re-checked in a second pass. Never labelled official.
- Official final-exam PYQs: none available.
