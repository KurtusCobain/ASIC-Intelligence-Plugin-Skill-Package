from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
GA4_MEASUREMENT_ID = "G-EGDNX281X0"

VISITOR_PAGES = {
    "funding.html": "Fund ASIC Intelligence",
    "partners.html": "Partner with ASIC Intelligence",
    "safety.html": "Safety & Scope",
    "benchmarks.html": "Validation & Benchmarks",
    "install-codex.html": "Install for Codex",
    "install-claude.html": "Install for Claude",
    "install-agent-skill.html": "Install the Agent Skill",
}


class VisitorFacingSitePagesTests(unittest.TestCase):
    def test_visitor_pages_exist_and_use_shared_brand_shell(self):
        for filename, heading in VISITOR_PAGES.items():
            with self.subTest(page=filename):
                path = DOCS / filename
                self.assertTrue(path.is_file(), f"missing visitor-facing page: {filename}")
                html = path.read_text(encoding="utf-8")
                self.assertIn(heading, html)
                self.assertIn('href="styles.css"', html)
                self.assertIn('href="index.html"', html)
                self.assertIn('ASIC Intelligence', html)
                self.assertIn('austin@wnclogiclab.com', html)

    def test_visitor_pages_keep_mobile_navigation_available(self):
        for filename in VISITOR_PAGES:
            with self.subTest(page=filename):
                html = (DOCS / filename).read_text(encoding="utf-8")
                self.assertIn('<script defer src="app.js"></script>', html)
                self.assertIn('class="menu-button"', html)
                self.assertIn('aria-controls="site-nav"', html)
                self.assertIn('id="site-nav"', html)

    def test_homepage_routes_visitors_to_html_not_markdown(self):
        html = (DOCS / "index.html").read_text(encoding="utf-8")
        expected = [
            "funding.html",
            "partners.html",
            "safety.html",
            "benchmarks.html",
            "install-codex.html",
            "install-claude.html",
            "install-agent-skill.html",
        ]
        for route in expected:
            self.assertIn(f'href="{route}"', html)

        visitor_markdown_links = re.findall(
            r'href="(?:INSTALL-(?:CODEX|CLAUDE|AGENT-SKILL)|SAFETY|FUNDING|PARTNERS|BENCHMARKS)\.md"',
            html,
        )
        self.assertEqual(visitor_markdown_links, [], f"visitor-facing markdown links remain: {visitor_markdown_links}")

    def test_technical_markdown_sources_remain_available(self):
        expected_sources = [
            "INSTALL-CODEX.md",
            "INSTALL-CLAUDE.md",
            "INSTALL-AGENT-SKILL.md",
            "SAFETY.md",
            "FUNDING.md",
            "PARTNERS.md",
            "BENCHMARKS.md",
        ]
        missing = [name for name in expected_sources if not (DOCS / name).is_file()]
        self.assertEqual(missing, [], f"technical markdown source docs were removed: {missing}")

    def test_all_public_html_pages_include_ga4_measurement(self):
        pages = sorted(DOCS.glob("*.html"))
        self.assertTrue(pages, "no public HTML pages found")

        loader = f"https://www.googletagmanager.com/gtag/js?id={GA4_MEASUREMENT_ID}"
        config = f"gtag('config', '{GA4_MEASUREMENT_ID}');"

        for path in pages:
            with self.subTest(page=path.name):
                html = path.read_text(encoding="utf-8")
                self.assertEqual(html.count(loader), 1, f"{path.name} must load GA4 exactly once")
                self.assertEqual(html.count(config), 1, f"{path.name} must configure GA4 exactly once")


if __name__ == "__main__":
    unittest.main()
