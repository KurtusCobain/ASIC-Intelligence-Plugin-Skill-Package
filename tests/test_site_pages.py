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
    "privacy.html": "Privacy Policy",
    "terms.html": "Terms of Service",
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

    def test_policy_pages_disclose_plugin_and_site_boundaries(self):
        privacy = self._read_page("privacy.html")
        for phrase in [
            "Google Analytics",
            "no ASIC Intelligence backend",
            "intentionally provide",
            "host AI environment",
        ]:
            self.assertIn(phrase, privacy)

        terms = self._read_page("terms.html")
        for phrase in [
            "PolyForm Shield License 1.0.0",
            "read-only diagnostic guidance",
            "no warranty",
            "does not authorize",
        ]:
            self.assertIn(phrase, terms)

    def test_policy_pages_are_listed_in_sitemap(self):
        sitemap = (DOCS / "sitemap.xml").read_text(encoding="utf-8")
        self.assertIn("/privacy.html", sitemap)
        self.assertIn("/terms.html", sitemap)

    def _read_page(self, filename):
        path = DOCS / filename
        self.assertTrue(path.is_file(), f"missing visitor-facing page: {filename}")
        return path.read_text(encoding="utf-8")

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

    def test_all_public_html_pages_load_shared_site_script(self):
        pages = sorted(DOCS.glob("*.html"))
        self.assertTrue(pages, "no public HTML pages found")
        for path in pages:
            with self.subTest(page=path.name):
                html = path.read_text(encoding="utf-8")
                self.assertEqual(
                    html.count('src="app.js"'),
                    1,
                    f"{path.name} must load the shared site script exactly once",
                )

    def test_shared_site_script_initializes_ga4_once(self):
        javascript = (DOCS / "app.js").read_text(encoding="utf-8")
        loader = f"https://www.googletagmanager.com/gtag/js?id={GA4_MEASUREMENT_ID}"
        self.assertEqual(javascript.count(GA4_MEASUREMENT_ID), 2)
        self.assertEqual(javascript.count(loader), 1)
        self.assertIn("window.dataLayer = window.dataLayer || [];", javascript)
        self.assertIn("gtag('js', new Date());", javascript)
        self.assertIn(f"gtag('config', GA4_MEASUREMENT_ID);", javascript)


if __name__ == "__main__":
    unittest.main()
