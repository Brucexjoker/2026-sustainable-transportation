# Source verification report

## Course structure (corrected)
First version used the official syllabus PDF (archive.nptel.ac.in/content/syllabus_pdf/105107210.pdf). That PDF is a generic EIA-style plan and does **not** match the real lectures. The NPTEL portal screenshots (Jul-Oct 2021 session, supplied by the user) show the actual 60 lectures, which match the original outline in the request. The app's 12 weeks now follow the real lecture titles:
1 Intro & sustainability · 2 Impacts of transportation · 3 EIA · 4 Global EIA practice & case studies (MAHSR) · 5 Land use, zoning, TOD · 6 TOD case studies & 4-step planning · 7 Contemporary planning, TSM & LCA · 8 MFA, circular economy, emission modelling · 9 Dispersion, noise models, policies (NCAP) · 10 Decarbonisation, fuels, EVs, Hyperloop, BRTS · 11 MRT, airports, water transport, NMT, openLCA · 12 openLCA, STAN, indicators, STAR.
Lecture titles come from the portal sidebar; the lecture *content* itself was not available, so notes are built from those titles, the assignment keys, and standard references.

## Official assignment questions (category A) - 233
**2021 session (125)**: transcribed by hand from NPTEL portal screenshots of Assignments 0-12 (`assignments/raw/`); answers are the portal's "Accepted Answers". A few keys look odd and are flagged in their explanations (A1-Q10 needs a graph; A8-Q4 was 0 points; A10-Q2 negatively worded).
**2026 session (120 questions; 108 new + 12 identical to 2021 questions, merged and shown as "2021 & 2026")**: transcribed from the 12 weekly assignment PDFs supplied by the user (`question banks/`, not published). The correct option is highlighted yellow in each PDF; answers were read from those highlights programmatically (119 of 120 found automatically; the remaining one, Week 1 Q3, confirmed by hand) and compared with my own independent answers: 118 agreed, 2 differed and the highlighted key was used (Week 2 Q4 -> 2307.69; Week 10 Q2 -> "Methanol from natural gas", whose wording looks inverted). Explanations are written by the assistant, not by NPTEL.
Graph question (Week 1 Q10) is included without the graph.
Not included: the 23-question live-session practice deck; final-exam PYQs (none available); 2022-2025 assignments (not supplied).

## Generated practice questions (category D) - 280
Newly written for this app, never labelled official (no year/URL). Not reviewed by a second person.

## Tests actually run
`python3 tests/check_data.py` PASS: 12 weeks complete, unique IDs and question texts, valid answer indices, no duplicate options, official questions carry year 2021 + "transcribed" label, generated ones carry no official metadata, 125 official, mocks reference valid IDs, 28 numerical answers recomputed independently.
Browser (scripted, localhost): all routes and 12 week pages render with no JS errors; all 125 official questions answered from their keys score 125/125; three 40-question timed mocks score 40/40 from the key; assignment filter returns 125, PYQ filter returns 0; earlier tests (multi-select grading, timer auto-submit, retry, bookmarks, flashcards, CSV export, 375px layout) were run on the previous build and not all repeated after the restructure.

## Not tested / not implemented
Backend, accounts, cross-device sync (not implemented). Offline/PWA files exist but offline use is untested. Real phones and screen readers untested. Official final-exam pattern unverified (mocks are unofficial).
