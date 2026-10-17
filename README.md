# STS Exam Prep (unofficial) - NPTEL 105107210

A dependency-free static web app (HTML/CSS/vanilla JS). No Node, database or server code is needed.
Folder to publish: `app/`.

## What it is / is not
- Working prototype, tested locally in a browser (see VERIFICATION_REPORT.md).
- Progress is stored in the browser's localStorage only. **No accounts, no database, no cross-device sync.** Back up via Progress > Backup (JSON).
- Not yet deployed anywhere. Nothing here has been published or paid for.

## Run locally
```bash
cd app && python3 -m http.server 8765   # then open http://localhost:8765
```

## Deploy (you do this; free tiers exist, accounts required)
Any static host works; upload/point to the `app/` folder.
- **Netlify Drop**: drag the `app/` folder onto https://app.netlify.com/drop (account needed to keep it).
- **GitHub Pages**: push `app/` contents to a repo, Settings > Pages > deploy from branch.
- **Cloudflare Pages / Vercel**: connect repo, build command none, output directory `app`.
Custom domain: add it in the host's Domains settings and create the DNS record they show.
Service worker/offline caching works only over HTTPS (or localhost); test it after deploying.

## Update the question bank
Edit `content/questions.py`, `questions2.py`, `questions3.py` (concept questions), `content/official2021.py` (official assignments), `content/numericals.py` (numericals, answers computed in code), `content/weeks_real.py` (the real 12-week notes and flashcards; it merges older notes from `weeks_a.py`/`weeks_b.py`).
Then:
```bash
python3 content/build.py        # regenerates app/data/data.js
python3 tests/check_data.py     # consistency tests
```
Official material (assignments/PYQs) must carry real `source` metadata (type, year, url); the tests reject anything generated that claims a year/URL.

## Adding cross-device sync later
Needs a backend (e.g. Supabase: auth + `attempts`, `bookmarks`, `progress` tables with row-level security; answer keys in a read-only table). Not implemented here.
