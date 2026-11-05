#!/usr/bin/env python3
"""Build the static HTML site from the markdown docs.

Reads every .md file in docs/ and writes a styled .html page into site/.
Uses only the Python standard library plus the `markdown` package.

Usage: python3 build.py
"""

import datetime
import re
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent
DOCS = ROOT / "docs"
SITE = ROOT / "site"

# (nav label, source file name) in reading order
PAGES = [
    ("Home", "index.md"),
    ("1. Search vs Chatbot", "01-when-search-beats-the-chatbot.md"),
    ("2. Craft Searches", "02-crafting-searches.md"),
    ("3. Sources & Verify", "03-ask-ai-for-sources-then-verify.md"),
    ("4. Reverse Image Search", "04-reverse-image-search.md"),
    ("5. Date Checks", "05-date-checks-on-stale-advice.md"),
    ("6. Reliability Rubric", "06-five-question-reliability-rubric.md"),
]

MD_EXTENSIONS = ["tables", "fenced_code", "sane_lists", "smarty"]

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — Searching Well with AI</title>
<meta name="description" content="A friendly manual on getting good answers from search engines and AI chatbots together — by Dylan Asdale (Asdale Dynamics, LLC).">
<link rel="stylesheet" href="styles.css">
</head>
<body>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="index.html">Searching Well with AI</a>
    <span class="tagline">a friendly manual · Dylan Asdale · Asdale Dynamics, LLC</span>
  </div>
  <nav class="wrap nav">
    {nav_links}
  </nav>
</header>
<main class="wrap">
<article>
{body}
</article>
<footer class="page-footer">
  <p><strong>Next:</strong> {next_label} · <strong>Series:</strong> The Massive AI Manual ·
  Companion guides: <em>Spot Fake Media Guide</em> · <em>Ask AI Better Questions</em></p>
  <p>Education only — never medical, legal, or financial advice. No affiliate links, no trackers.
  &copy; {year} Asdale Dynamics, LLC · <a href="https://dylanasdale.github.io/">dylanasdale.github.io</a></p>
  <p><a href="#top">Back to top</a></p>
</footer>
</main>
</body>
</html>
"""

STYLES = """/* Searching Well with AI — site styles */
:root {
  --ink: #1c2733;
  --paper: #fbfaf7;
  --accent: #14646e;
  --accent-soft: #e2eff1;
  --muted: #5c6b78;
}
* { box-sizing: border-box; }
body {
  margin: 0;
  font-family: Georgia, 'Times New Roman', serif;
  color: var(--ink);
  background: var(--paper);
  line-height: 1.65;
}
.wrap { max-width: 46rem; margin: 0 auto; padding: 0 1.25rem; }
a { color: var(--accent); }
a:hover { text-decoration-thickness: 2px; }
.site-header {
  background: #123f47;
  color: #fff;
  padding: 1rem 0 .6rem;
}
.brand {
  color: #fff; text-decoration: none;
  font-size: 1.35rem; font-weight: bold; letter-spacing: .5px;
}
.tagline { display: block; color: #bcd7da; font-size: .85rem; font-family: Verdana, sans-serif; margin-top: .2rem; }
.nav { font-family: Verdana, sans-serif; font-size: .8rem; margin-top: .8rem; }
.nav a { color: #dff0f2; text-decoration: none; margin-right: .35rem; padding: .2rem .5rem; border-radius: .35rem; }
.nav a:hover { background: rgba(255,255,255,.15); }
.nav a.kn { background: rgba(255,255,255,.22); }
main { padding: 2rem 0 1rem; }
article h1 { font-size: 2rem; line-height: 1.25; margin: 0 0 1rem; }
article h2 { font-size: 1.4rem; margin: 2.2rem 0 .6rem; color: #123f47; }
article h3 { font-size: 1.1rem; margin: 1.6rem 0 .5rem; }
article ul, article ol { padding-left: 1.4rem; }
article li { margin: .3rem 0; }
article blockquote {
  margin: 1.2rem 0; padding: .8rem 1.1rem;
  background: var(--accent-soft); border-left: 4px solid var(--accent);
  border-radius: .4rem;
}
article blockquote p { margin: .3rem 0; }
table { border-collapse: collapse; width: 100%; margin: 1.2rem 0; font-family: Verdana, sans-serif; font-size: .85rem; }
th, td { border: 1px solid #d8d5cd; padding: .5rem .65rem; text-align: left; vertical-align: top; }
th { background: var(--accent-soft); }
code {
  font-family: Consolas, Menlo, monospace; font-size: .9em;
  background: #efede6; padding: .1rem .35rem; border-radius: .25rem;
}
pre {
  background: #2b3a42; color: #e8eee9; padding: 1rem 1.2rem;
  border-radius: .5rem; overflow-x: auto;
}
pre code { background: none; color: inherit; padding: 0; }
.page-footer {
  margin: 3rem 0 2rem; padding: 1.2rem;
  background: #f1efe8; border-radius: .5rem;
  font-family: Verdana, sans-serif; font-size: .8rem; color: var(--muted);
}
.page-footer p { margin: .4rem 0; }
.page-footer a { color: var(--accent); }
home-note { display: block; }
@media print { .site-header, .page-footer, .nav { display: none; } }
"""


def slug_title(name: str) -> str:
    """First markdown H1 of a doc becomes the page title."""
    for line in name.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return md_inline(line[2:])
    return name.stem.replace("-", " ").title()


def md_inline(text: str) -> str:
    return markdown.markdown(text, extensions=MD_EXTENSIONS).replace("<p>", "").replace("</p>", "")


def build() -> int:
    if not DOCS.is_dir():
        raise SystemExit(f"docs/ not found next to build.py ({DOCS})")
    SITE.mkdir(exist_ok=True)
    for stale in SITE.glob("*.html"):
        stale.unlink()

    (SITE / "styles.css").write_text(STYLES, encoding="utf-8")

    count = 0
    for i, (label, src) in enumerate(PAGES):
        path = DOCS / src
        if not path.exists():
            raise SystemExit(f"missing doc: {path}")
        raw = path.read_text(encoding="utf-8")
        body = markdown.markdown(raw, extensions=MD_EXTENSIONS)
        title = slug_title(path)
        nav_links = " ".join(
            f'<a href="{Path(p).with_suffix(".html").name}" class="{"kn" if p == src else ""}">{l}</a>'
            for l, p in PAGES
        )
        next_label = PAGES[(i + 1) % len(PAGES)][0]
        html = TEMPLATE.format(
            title=title,
            nav_links=nav_links,
            body=body,
            next_label=next_label,
            year=datetime.date.today().year,
        )
        out = SITE / Path(src).with_suffix(".html").name
        out.write_text(html, encoding="utf-8")
        count += 1
    return count


if __name__ == "__main__":
    n = build()
    print(f"built {n} pages into {SITE}")
