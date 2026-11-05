#!/usr/bin/env python3
"""Tests for the Searching Well with AI guide.

Run:  python3 -m unittest discover -s tests -v
(or)  python3 tests/run_tests.py
"""

import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
SITE = ROOT / "site"
sys.path.insert(0, str(ROOT))

import build  # noqa: E402

EXPECTED_PAGES = [
    "index.html",
    "01-when-search-beats-the-chatbot.html",
    "02-crafting-searches.html",
    "03-ask-ai-for-sources-then-verify.html",
    "04-reverse-image-search.html",
    "05-date-checks-on-stale-advice.html",
    "06-five-question-reliability-rubric.html",
]

DOCS_COVERAGE = {
    "01-when-search-beats-the-chatbot.md": ["chatbot", "search", "hybrid"],
    "02-crafting-searches.md": ["site:", "filetype:", "operator"],
    "03-ask-ai-for-sources-then-verify.md": ["source", "verify", "hallucination"],
    "04-reverse-image-search.md": ["reverse", "TinEye", "Google Lens", "oldest"],
    "05-date-checks-on-stale-advice.md": ["archive", "wayback", "date", "2026"],
    "06-five-question-reliability-rubric.md": ["WHO", "WHAT", "WHEN", "WHY", "WHERE"],
}

AFFILIATE_PATTERNS = [  # URL/link shapes, not the English word
    r"\?(tag|ref|aff|affid|sid)=[\w-]", r"\b(?:t\.|amzn)\.to/",
    r"amazon\.[a-z.]+/[^\s]*&?(tag|ref)=", r"/affiliate",
    r"shareasale|clickbank|rstyle\.me|impact\.com/.*/offer",
]

MUST_PROMISE_NO_AFFILIATES = ["index.md"]

SECRET_PATTERNS = [
    r"sk-[A-Za-z0-9]{20,}",           # openai-style key
    r"ghp_[A-Za-z0-9]{20,}",          # github PAT
    r"AKIA[0-9A-Z]{16}",              # aws access key
    r"xox[bpars]-[A-Za-z0-9-]{10,}",  # slack token
    r"-----BEGIN [A-Z ]*PRIVATE KEY-----",
]


class TestBuild(unittest.TestCase):
    def setUp(self):
        self.pages_built = build.build()

    def test_build_produces_all_pages(self):
        self.assertEqual(self.pages_built, len(EXPECTED_PAGES))
        for page in EXPECTED_PAGES:
            self.assertTrue((SITE / page).is_file(), f"missing {page}")
        self.assertTrue((SITE / "styles.css").is_file())

    def test_pages_have_structure(self):
        for page in EXPECTED_PAGES:
            html = (SITE / page).read_text(encoding="utf-8")
            with self.subTest(page=page):
                self.assertIn("<!DOCTYPE html>", html)
                self.assertIn("<nav", html)
                self.assertIn("Asdale Dynamics, LLC", html)
                self.assertIn("</html>", html)

    def test_nav_highlights_current_page(self):
        for page in EXPECTED_PAGES:
            html = (SITE / page).read_text(encoding="utf-8")
            with self.subTest(page=page):
                self.assertIn(f'href="{page}" class="kn"', html)

    def test_internal_links_resolve(self):
        for page in EXPECTED_PAGES:
            html = (SITE / page).read_text(encoding="utf-8")
            links = re.findall(r'href="([^"#]+\.html)"', html)
            for link in links:
                with self.subTest(page=page, link=link):
                    self.assertTrue(
                        (SITE / link).exists(),
                        f"{page} links to missing {link}",
                    )

    def test_rebuild_is_deterministic(self):
        before = {p.name: p.read_bytes() for p in SITE.glob("*")}
        build.build()
        after = {p.name: p.read_bytes() for p in SITE.glob("*")}
        self.assertEqual(before, after)


class TestDocs(unittest.TestCase):
    def test_every_doc_starts_with_h1(self):
        for md in DOCS.glob("*.md"):
            text = md.read_text(encoding="utf-8")
            with self.subTest(doc=md.name):
                self.assertTrue(
                    text.lstrip().startswith("# "),
                    f"{md.name} does not start with an H1",
                )

    def test_docs_cover_the_manuals_promised_topics(self):
        for filename, keywords in DOCS_COVERAGE.items():
            text = (DOCS / filename).read_text(encoding="utf-8").lower()
            for kw in keywords:
                with self.subTest(doc=filename, keyword=kw):
                    self.assertIn(kw.lower(), text)

    def test_rubric_has_exactly_five_questions(self):
        text = (DOCS / "06-five-question-reliability-rubric.md").read_text(encoding="utf-8")
        for i in range(1, 6):
            self.assertRegex(text, rf"\*\*{i}\. ")
        self.assertNotRegex(text, r"\*\*6\. ")

    def test_no_affiliate_links(self):
        haystacks = [p.read_text(encoding="utf-8", errors="ignore")
                     for p in list(ROOT.glob("*.md")) + list(DOCS.glob("*.md")) + list(SITE.glob("*")) if p.is_file()]
        haystacks.append(build.STYLES)
        haystacks.append(build.TEMPLATE)
        for hay in haystacks:
            for pattern in AFFILIATE_PATTERNS:
                with self.subTest(pattern=pattern):
                    self.assertIsNone(re.search(pattern, hay, re.IGNORECASE))

    def test_no_affiliate_promise_is_made(self):
        for name in MUST_PROMISE_NO_AFFILIATES:
            with self.subTest(doc=name):
                self.assertRegex(
                    (DOCS / name).read_text(encoding="utf-8"),
                    r"[Nn]o affiliate links",
                )
        self.assertRegex(build.TEMPLATE, r"[Nn]o affiliate links")

    def test_no_secrets(self):
        files = [p for p in ROOT.rglob("*")
                 if p.is_file() and p.suffix in {".md", ".py", ".css", ".html", ".txt"}]
        for path in files:
            text = path.read_text(encoding="utf-8", errors="ignore")
            for pattern in SECRET_PATTERNS:
                with self.subTest(file=path.name, pattern=pattern):
                    self.assertIsNone(re.search(pattern, text))


class TestRepoIntegrity(unittest.TestCase):
    def test_license_is_mit_with_exact_copyright(self):
        license_text = (ROOT / "LICENSE").read_text(encoding="utf-8")
        self.assertIn("MIT License", license_text)
        self.assertIn("Copyright (c) 2026 Asdale Dynamics, LLC", license_text)

    def test_readme_credits_and_explains(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("Asdale Dynamics, LLC", readme)
        self.assertIn("site", readme.lower())
        self.assertIn("test", readme.lower())
        for topic in ["when search beats", "crafting searches", "source", "reverse image",
                      "date check", "rubric"]:
            self.assertIn(topic, readme.lower())

    def test_companion_guides_are_referenced(self):
        index = (DOCS / "index.md").read_text(encoding="utf-8")
        self.assertIn("Spot Fake Media Guide", index)
        self.assertIn("Ask AI Better Questions", index)


if __name__ == "__main__":
    unittest.main(verbosity=2)
