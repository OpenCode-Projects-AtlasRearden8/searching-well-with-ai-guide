# Searching Well with AI

*A friendly manual on getting good answers from search engines and AI chatbots together —
so the answer you use is the answer that's true.*

Part of **The Massive AI Manual** series by Dylan Asdale, published by **Asdale Dynamics, LLC**.

## What this is

Two tools sit next to each other on every homework, work task, and health question:
the **search engine** and the **AI chatbot**. Most of us use whichever is closest and
hope for the best. This short manual teaches the partnership — seven short chapters,
about an hour total, no jargon:

| # | Chapter | Skill |
|---|---------|-------|
| — | [Home](docs/index.md) | how to read the manual |
| 1 | [When Search Beats the Chatbot](docs/01-when-search-beats-the-chatbot.md) | picking the right tool first |
| 2 | [Crafting Searches](docs/02-crafting-searches.md) | quotes, `site:`, `filetype:`, date filters |
| 3 | [Ask AI for Sources, Then Verify](docs/03-ask-ai-for-sources-then-verify.md) | catching invented citations in under two minutes |
| 4 | [Reverse Image Search](docs/04-reverse-image-search.md) | finding where a photo really came from |
| 5 | [Date Checks on Stale Advice](docs/05-date-checks-on-stale-advice.md) | the 30-second habit against outdated answers |
| 6 | [Five-Question Reliability Rubric](docs/06-five-question-reliability-rubric.md) | Who · What · When · Why · Where else |

**Companion guides** (the same style, different skills):

- *Spot Fake Media Guide* — catching fake images, video, and audio. This guide covers finding good sources; that one covers spotting fakes.
- *Ask AI Better Questions* — prompt craft. This guide covers verifying answers; that one covers asking better.
- Hub: [dylanasdale.github.io](https://dylanasdale.github.io/)

## How to run it

Requirements: Python 3.10+ with the `markdown` package (`pip install markdown`).

```bash
# build the static HTML site from docs/
python3 build.py

# preview the site locally (no server needed to read files:
# just open site/index.html in a browser — or serve it if you prefer)
python3 -m http.server 8000 --directory site
# then visit http://localhost:8000
```

Everything is static, local-first, and tracker-free: no accounts, no analytics,
no JavaScript required, no affiliate links.

## How to test it

```bash
python3 -m unittest discover -s tests -v
```

The test suite (stdlib `unittest`, no extra dependencies) verifies:

- the build runs and emits every expected page + stylesheet
- navigation, current-page highlighting, and internal links all resolve
- the build is deterministic (same output every time)
- each promised topic actually appears in its chapter (search-vs-chatbot logic,
  operators, source verification, reverse image search, date checks, the 5-question rubric)
- the rubric really has exactly five questions (not six, not four)
- **no affiliate links** anywhere in docs, site, README, or templates — tested
- **no secrets or personal data** — keys/credential patterns are scanned and tested against
- MIT LICENSE with the exact line `Copyright (c) 2026 Asdale Dynamics, LLC`

## Project layout

```
docs/    the manual, in markdown (source of truth)
site/    generated static HTML site (run python3 build.py after editing docs/)
tests/   unittest suite for build, content, and integrity checks
build.py docs → site build script
```

## Who made this

Made by **Asdale Dynamics, LLC** (Dylan Asdale — registered nurse turned AI author,
explained "like a friend would": plain English, step by step, never condescending).

Education only — nothing here is medical, legal, or financial advice.
Licensed MIT. No trackers, no secrets, no affiliate links, ever.
