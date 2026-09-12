from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
CHATGPT_PLUGIN_URL = "https://chatgpt.com/plugins/plugins_6a90d9a9a63c81919cf452b0c4dcb665"


class UiOptimizationContractTests(unittest.TestCase):
    def _read(self, rel):
        path = ROOT / rel
        self.assertTrue(path.is_file(), f"missing file: {rel}")
        return path.read_text(encoding="utf-8")

    def test_hero_has_two_conversion_buttons_and_no_github_button(self):
        html = self._read("docs/index.html")
        hero = html.split('<section class="hero"', 1)[1].split('</section>', 1)[0]
        self.assertIn(CHATGPT_PLUGIN_URL, hero)
        self.assertIn("Watch the demo", hero)
        self.assertNotIn("View on GitHub", hero)
        self.assertIn("Read-only", hero)
        self.assertIn("Free to try", hero)
        self.assertNotIn("Current public package release", hero)

    def test_demo_precedes_evidence_section(self):
        html = self._read("docs/index.html")
        self.assertLess(html.index('id="demo"'), html.index('id="evidence"'))

    def test_homepage_has_four_step_how_it_works_flow(self):
        html = self._read("docs/index.html")
        for phrase in ["Bring evidence", "Correlate it", "Get the diagnosis", "Check safely"]:
            self.assertIn(phrase, html)

    def test_evidence_is_consolidated_into_three_groups(self):
        html = self._read("docs/index.html")
        evidence = html.split('id="evidence"', 1)[1].split('</section>', 1)[0]
        for heading in ["Miner evidence", "Fleet &amp; infrastructure", "Historical evidence"]:
            self.assertIn(heading, evidence)
        self.assertEqual(evidence.count('<article class="card'), 3)

    def test_diagnostic_example_uses_result_emphasis(self):
        html = self._read("docs/index.html")
        self.assertIn("What a diagnosis looks like", html)
        for label in ["LIKELY CAUSE", "CONFIDENCE", "NEXT SAFE CHECK"]:
            self.assertIn(label, html)
        self.assertIn("result-key", html)

    def test_trust_model_is_consolidated_into_three_cards(self):
        html = self._read("docs/index.html")
        trust = html.split('id="trust"', 1)[1].split('</section>', 1)[0]
        for heading in ["Evidence integrity", "No invented certainty", "Operational reasoning"]:
            self.assertIn(heading, trust)
        self.assertEqual(trust.count('<article class="card'), 3)

    def test_demo_trials_include_guided_prompt_and_copy_action(self):
        html = self._read("docs/index.html")
        self.assertIn("Copy test prompt", html)
        self.assertIn('data-track="demo_prompt_copy"', html)
        self.assertIn("What most likely happened, and what should I check next?", html)
        js = self._read("docs/app.js")
        self.assertIn("demo_prompt_copy", js)
        self.assertIn("navigator.clipboard", js)

    def test_availability_separates_chatgpt_from_developer_options(self):
        html = self._read("docs/index.html")
        availability = html.split('id="availability"', 1)[1].split('</section>', 1)[0]
        self.assertIn("Try it now", availability)
        self.assertIn("Developer &amp; local options", availability)
        self.assertLess(availability.index("Try it now"), availability.index("Developer &amp; local options"))

    def test_proof_strip_uses_read_only_instead_of_package_count(self):
        html = self._read("docs/index.html")
        stats = html.split('<section class="stats">', 1)[1].split('</section>', 1)[0]
        self.assertIn("READ-ONLY", stats)
        self.assertNotIn("downloadable package formats", stats)

    def test_desktop_note_is_compact_and_after_faq(self):
        html = self._read("docs/index.html")
        self.assertIn("Also from ASIC Intelligence", html)
        self.assertLess(html.index('id="faq"'), html.index('id="desktop"'))

    def test_funding_comes_after_faq_and_desktop(self):
        html = self._read("docs/index.html")
        self.assertLess(html.index('id="faq"'), html.index('id="funding"'))
        self.assertLess(html.index('id="desktop"'), html.index('id="funding"'))

    def test_css_has_focus_visible_and_tablet_nav_breakpoint(self):
        css = self._read("docs/styles.css")
        self.assertIn(":focus-visible", css)
        self.assertRegex(css, r"@media\(max-width:(?:9[0-9]{2})px\)")
        self.assertIn(".menu-button{display:block", css)

    def test_mobile_primary_actions_stack_full_width(self):
        css = self._read("docs/styles.css")
        self.assertIn(".hero-actions .button", css)
        self.assertIn("width:100%", css)

    def test_navigation_supports_escape_outside_click_and_resize_cleanup(self):
        js = self._read("docs/app.js")
        self.assertIn("Escape", js)
        self.assertIn("document.addEventListener('click'", js)
        self.assertIn("window.addEventListener('resize'", js)

    def test_demo_grid_uses_adaptive_minmax_layout(self):
        css = self._read("docs/styles.css")
        self.assertRegex(css, r"\.demo-grid\{[^}]*repeat\(auto-fit,minmax\(")


if __name__ == "__main__":
    unittest.main()
