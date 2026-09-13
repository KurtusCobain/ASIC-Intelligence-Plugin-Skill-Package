from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class VisualPersonalityContractTests(unittest.TestCase):
    def _read(self, rel):
        path = ROOT / rel
        self.assertTrue(path.is_file(), f"missing file: {rel}")
        return path.read_text(encoding="utf-8")

    def test_hero_has_mining_infrastructure_atmosphere(self):
        html = self._read("docs/index.html")
        hero = html.split('<section class="hero"', 1)[1].split('</section>', 1)[0]
        self.assertIn('hero-atmosphere', hero)
        self.assertIn('topology-line', hero)
        self.assertIn('signal-node', hero)

    def test_demo_is_presented_as_feature_stage(self):
        html = self._read("docs/index.html")
        demo = html.split('id="demo"', 1)[1].split('</section>', 1)[0]
        self.assertIn('demo-stage', demo)
        self.assertIn('LIVE WORKFLOW', demo)
        self.assertIn('Attach evidence', demo)
        self.assertIn('Find the pattern', demo)
        self.assertIn('Get the next safe check', demo)

    def test_diagnostic_example_is_signature_centerpiece(self):
        html = self._read("docs/index.html")
        diagnosis = html.split('id="diagnosis"', 1)[1].split('</section>', 1)[0]
        self.assertIn('signature-diagnostic', diagnosis)
        self.assertIn('diagnostic-cues', diagnosis)
        for cue in ["Observed evidence", "Reasoned conclusion", "Safe next step"]:
            self.assertIn(cue, diagnosis)

    def test_trust_section_uses_compact_principles_not_repeated_cards(self):
        html = self._read("docs/index.html")
        trust = html.split('id="trust"', 1)[1].split('</section>', 1)[0]
        self.assertIn('trust-principles', trust)
        self.assertNotIn('<article class="card', trust)
        self.assertEqual(trust.count('class="trust-principle"'), 3)

    def test_founder_section_has_operator_quote_treatment(self):
        html = self._read("docs/index.html")
        founder = html.split('id="founder"', 1)[1].split('</section>', 1)[0]
        self.assertIn('operator-story', founder)
        self.assertIn('operator-quote', founder)
        self.assertIn('About the developer', founder)

    def test_validation_is_an_operations_status_board(self):
        html = self._read("docs/index.html")
        validation = html.split('id="validation"', 1)[1].split('</section>', 1)[0]
        self.assertIn('status-board', validation)
        self.assertIn('status-board-header', validation)
        self.assertIn('status-row', validation)

    def test_lower_support_content_is_visually_grouped(self):
        html = self._read("docs/index.html")
        self.assertIn('support-zone', html)
        support = html.split('class="support-zone"', 1)[1]
        self.assertIn('id="desktop"', support)
        self.assertIn('id="funding"', support)

    def test_css_defines_visual_motifs_and_non_card_variation(self):
        css = self._read("docs/styles.css")
        for selector in [
            '.hero-atmosphere',
            '.topology-line',
            '.signal-node',
            '.demo-stage',
            '.signature-diagnostic',
            '.trust-principles',
            '.operator-story',
            '.status-board',
            '.support-zone',
        ]:
            self.assertIn(selector, css)
        self.assertIn('linear-gradient', css)
        self.assertIn('radial-gradient', css)

    def test_motion_polish_respects_reduced_motion(self):
        css = self._read("docs/styles.css")
        self.assertIn('@media(prefers-reduced-motion:reduce)', css)
        self.assertIn('animation:none!important', css)


if __name__ == "__main__":
    unittest.main()
