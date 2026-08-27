from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]


class PublicRepoShapeTests(unittest.TestCase):
    def test_required_surface_exists(self):
        required = [
            'README.md', 'LICENSE', 'CHANGELOG.md', 'SECURITY.md', 'CONTRIBUTING.md', 'CODE_OF_CONDUCT.md',
            '.github/FUNDING.yml', '.github/workflows/verify.yml', '.github/workflows/pages.yml',
            'docs/index.html', 'docs/styles.css', 'docs/app.js', 'docs/assets/icon.svg',
            'docs/INSTALL-CODEX.md', 'docs/INSTALL-CLAUDE.md', 'docs/INSTALL-AGENT-SKILL.md',
            'docs/SAFETY.md', 'docs/FAQ.md', 'docs/FUNDING.md', 'docs/PARTNERS.md', 'docs/BENCHMARKS.md',
            'tools/verify_public_repo.py',
        ]
        missing = [p for p in required if not (ROOT / p).is_file()]
        self.assertEqual(missing, [], f'missing required public files: {missing}')

    def test_release_artifacts_exist(self):
        required = [
            'distributions/codex/bitcoin-mining-troubleshooter-codex-v1.1.0.zip',
            'distributions/claude/bitcoin-mining-troubleshooter-claude-v1.1.0.zip',
            'distributions/agent-skill/bitcoin-mining-troubleshooter-agent-skill-v1.1.0.zip',
            'demos/01-fleet-restart-recovery.csv',
            'demos/02-network-segment-incident.xlsx',
            'demos/03-power-thermal-operations.xlsx',
            'demos/04-repair-history.jsonl',
            'demos/05-miner-log-corpus.ndjson',
            'demos/README.md', 'demos/DEMO-SCRIPT.md',
        ]
        missing = [p for p in required if not (ROOT / p).is_file()]
        self.assertEqual(missing, [], f'missing release artifacts: {missing}')

    def test_private_material_is_not_present(self):
        forbidden = ('evaluator', 'answer-key', 'expected-findings', 'source-v1.1.0', 'private-build-notes', 'recovery-bundle')
        hits = []
        for p in ROOT.rglob('*'):
            rel = str(p.relative_to(ROOT)).lower()
            if any(fragment in rel for fragment in forbidden):
                hits.append(rel)
        self.assertEqual(hits, [], f'private material leaked into public tree: {hits}')


class PublicRepoContentTests(unittest.TestCase):
    def _read(self, rel):
        path = ROOT / rel
        self.assertTrue(path.is_file(), f'required file missing: {rel}')
        return path.read_text(encoding='utf-8')

    def test_readme_uses_public_product_identity(self):
        text = self._read('README.md')
        for phrase in [
            'ASIC Intelligence Plugin/Skill Package',
            'Bitcoin Mining Troubleshooter',
            'Powered by ASIC Intelligence',
            'Read-only',
            'Install for Codex',
            'Install for Claude',
            'Use it. Integrate it. Fund it.',
        ]:
            self.assertIn(phrase, text)

    def test_funding_separates_open_support_from_private_partnerships(self):
        text = self._read('docs/FUNDING.md')
        self.assertIn('Public project sponsorship', text)
        self.assertIn('ASIC Intelligence development partnerships', text)
        self.assertIn('Integration Sponsor', text)
        self.assertIn('Founding Design Partner', text)
        self.assertIn('does not purchase', text)

    def test_site_contains_core_routes(self):
        html = self._read('docs/index.html')
        for phrase in [
            'ASIC Intelligence Plugin/Skill Package',
            'Bitcoin Mining Troubleshooter',
            'Try a fleet-scale demo',
            'Install for Codex',
            'Install for Claude',
            'Use it. Integrate it. Fund it.',
            'Founding Design Partner',
        ]:
            self.assertIn(phrase, html)

    def test_site_uses_approved_brand_palette(self):
        css = self._read('docs/styles.css').upper()
        for color in ['#090C0B', '#111614', '#7CFF6B', '#F2F6F3']:
            self.assertIn(color, css)

    def test_workflows_verify_and_deploy_docs(self):
        verify = self._read('.github/workflows/verify.yml')
        pages = self._read('.github/workflows/pages.yml')
        self.assertIn('python -m unittest -v tests.test_public_repo', verify)
        self.assertIn('python tools/verify_public_repo.py .', verify)
        self.assertIn('path: docs', pages)
        self.assertIn('pages: write', pages)
        self.assertIn('id-token: write', pages)

    def test_demo_scale_is_derived_from_release_files(self):
        import importlib.util
        verifier = ROOT / 'tools' / 'verify_public_repo.py'
        spec = importlib.util.spec_from_file_location('verify_public_repo', verifier)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        counts = module.demo_counts(ROOT)
        self.assertEqual(counts, {
            'fleet_restart': 5250,
            'network_incident': 4800,
            'power_thermal': 4920,
            'repair_miners': 3500,
            'miner_logs': 3000,
        })
        self.assertEqual(sum(counts.values()), 21470)


    def test_site_uses_pages_safe_repo_links_and_private_contact(self):
        html = self._read('docs/index.html')
        self.assertNotIn('href="../demos/', html)
        self.assertNotIn('href="../distributions/', html)
        self.assertIn('https://github.com/KurtusCobain/ASIC-Intelligence-Plugin-Skill-Package/raw/main/demos/', html)
        self.assertIn('https://github.com/KurtusCobain/ASIC-Intelligence-Plugin-Skill-Package/raw/main/distributions/', html)
        self.assertIn('mailto:austin@wnclogiclab.com', html)

    def test_site_has_unambiguous_validation_status_and_social_metadata(self):
        html = self._read('docs/index.html')
        self.assertIn('Illustrative diagnostic example', html)
        self.assertIn('21,470', html)
        self.assertIn('NOT PART OF v1.1.0', html)
        for phrase in ['og:title', 'og:description', 'og:image', 'canonical']:
            self.assertIn(phrase, html)

    def test_distribution_packages_use_asic_intelligence_identity(self):
        import zipfile
        checks = {
            'distributions/codex/bitcoin-mining-troubleshooter-codex-v1.1.0.zip': '.codex-plugin/plugin.json',
            'distributions/claude/bitcoin-mining-troubleshooter-claude-v1.1.0.zip': '.claude-plugin/plugin.json',
            'distributions/agent-skill/bitcoin-mining-troubleshooter-agent-skill-v1.1.0.zip': 'SKILL.md',
        }
        for rel, suffix in checks.items():
            with zipfile.ZipFile(ROOT / rel) as zf:
                member = next(n for n in zf.namelist() if n.endswith(suffix))
                text = zf.read(member).decode('utf-8')
                self.assertIn('ASIC Intelligence', text, rel)
                self.assertNotIn('wnclogiclab.com/products/bitcoin-mining-troubleshooter', text, rel)

    def test_release_has_checksums(self):
        sums = self._read('SHA256SUMS')
        for name in [
            'bitcoin-mining-troubleshooter-codex-v1.1.0.zip',
            'bitcoin-mining-troubleshooter-claude-v1.1.0.zip',
            'bitcoin-mining-troubleshooter-agent-skill-v1.1.0.zip',
        ]:
            self.assertIn(name, sums)

    def test_public_verifier_passes(self):
        verifier = ROOT / 'tools' / 'verify_public_repo.py'
        self.assertTrue(verifier.is_file(), 'public verifier missing')
        result = subprocess.run([sys.executable, str(verifier), str(ROOT)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn('PUBLIC REPO: PASS', result.stdout)


if __name__ == '__main__':
    unittest.main()
