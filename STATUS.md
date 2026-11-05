# STATUS.md — Searching Well with AI

Last updated: 2026-11-05

## What was built

A beginner-friendly manual on getting good answers from **search engines and AI
chatbots together**, by Dylan Asdale / **Asdale Dynamics, LLC** (part of
*The Massive AI Manual* series).

**Format:** `docs/` markdown (source of truth) + `site/` generated static HTML
(no JS, no trackers, no accounts, **no affiliate links**).

**Coverage — every goal item is present and tested:**

1. `docs/01-when-search-beats-the-chatbot.md` — when search engine beats a chatbot (and vice versa), plus the 3-step hybrid move.
2. `docs/02-crafting-searches.md` — crafting searches: quotes, `site:`, `-`, `filetype:`, `after:`, `OR`, plus reading results and when to stop.
3. `docs/03-ask-ai-for-sources-then-verify.md` — asking AI for sources (3 prompt strengths) and the two-minute verify routine, hallucination red flags.
4. `docs/04-reverse-image-search.md` — reverse image search via Google Lens, TinEye, Yandex, Bing; interpreting match ages and contexts.
5. `docs/05-date-checks-on-stale-advice.md` — date checks on stale advice: page dating, Wayback Machine, freshness tiers, the AI date-honesty prompt.
6. `docs/06-five-question-reliability-rubric.md` — the five-question rubric (Who · What · When · Why · Where else), with scoring.

**Companions referenced:** *Spot Fake Media Guide* (fake content) and
*Ask AI Better Questions* (prompt craft), linked from `docs/index.md`, the README,
and every site page footer.

**Tooling:**

- `build.py` — markdown → styled HTML with nav, current-page highlight, per-page footer; stdlib + `markdown` only. Deterministic (byte-identical on rebuild).
- `tests/test_searching_well.py` — 14 tests: build output, nav/links, determinism,
  topic coverage per chapter, exactly-5 rubric questions, no-affiliate-link patterns,
  no-secrets scanning, LICENSE/README integrity.

**Integrity guarantees (tested):** MIT LICENSE with exact line
`Copyright (c) 2026 Asdale Dynamics, LLC`; README credits Asdale Dynamics, LLC;
no affiliate links; no secrets or personal data.

## How to run it

```bash
python3 -m pip install markdown     # if needed
python3 build.py                    # rebuild site/ from docs/
python3 -m http.server 8000 --directory site   # preview at http://localhost:8000
                                    # (or just open site/index.html directly)
```

## How to test it

```bash
python3 -m unittest discover -s tests -v
```

## Verification results (this session)

- `python3 build.py` → **built 7 pages** (6 chapters + home) + `styles.css`. ✔
- `python3 -m unittest discover -s tests` → **Ran 14 tests … OK** (0 failures). ✔
- `python3 -m compileall build.py tests` → no syntax errors. ✔
- Affiliate-link patterns and secret patterns scanned across repo files — clean. ✔

## Known gaps

- Site styling is intentionally minimal CSS; no dark mode or search box.
- Chapters cite techniques as of 2026; search operators (e.g. `after:`) are
  Google-flavored and may differ slightly on other engines.
- Companion guides (Spot Fake Media Guide, Ask AI Better Questions) are separate
  projects — here they are referenced, not included.
- No screenshot illustrations yet (text-first release; images would need
  licensing-free assets or original captures).
- The hub link `https://dylanasdale.github.io/` points to the series hub.
