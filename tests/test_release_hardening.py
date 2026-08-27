from pathlib import Path
import json
import struct
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
CLAUDE_ZIP = ROOT / "distributions/claude/bitcoin-mining-troubleshooter-claude-v1.1.0.zip"


class ClaudeReleaseHardeningTests(unittest.TestCase):
    def _claude_members(self):
        zf = zipfile.ZipFile(CLAUDE_ZIP)
        names = zf.namelist()
        manifest = next(n for n in names if n.endswith("/.claude-plugin/plugin.json"))
        readme = next(n for n in names if n.endswith("/README.md"))
        skill = next(n for n in names if n.endswith("/skills/diagnose/SKILL.md"))
        return zf, manifest, readme, skill

    def test_claude_plugin_uses_namespaced_invocation(self):
        zf, _, readme, _ = self._claude_members()
        with zf:
            text = zf.read(readme).decode("utf-8")
        self.assertIn("/bitcoin-mining-troubleshooter:diagnose", text)
        self.assertNotIn("invoke the skill manually with `/bitcoin-mining-troubleshooter`", text)

    def test_claude_manifest_has_repository_and_license(self):
        zf, manifest, _, _ = self._claude_members()
        with zf:
            data = json.loads(zf.read(manifest).decode("utf-8"))
        self.assertEqual(
            data.get("repository"),
            "https://github.com/KurtusCobain/ASIC-Intelligence-Plugin-Skill-Package",
        )
        self.assertEqual(data.get("license"), "PolyForm-Shield-1.0.0")

    def test_claude_skill_copy_is_platform_specific(self):
        zf, _, _, skill = self._claude_members()
        with zf:
            text = zf.read(skill).decode("utf-8")
        self.assertNotIn("ChatGPT/Codex", text)
        self.assertIn("Claude Code", text)

    def test_claude_validation_status_is_current(self):
        for rel in ["docs/index.html", "docs/install-claude.html", "docs/INSTALL-CLAUDE.md"]:
            text = (ROOT / rel).read_text(encoding="utf-8")
            self.assertNotIn("CLI CHECK PENDING", text, rel)
        self.assertIn("CLAUDE CLI VALIDATED", (ROOT / "docs/index.html").read_text(encoding="utf-8"))

    def test_public_site_has_sitemap_and_favicon_fallback(self):
        self.assertTrue((ROOT / "docs/sitemap.xml").is_file())
        self.assertTrue((ROOT / "docs/favicon.ico").is_file())
        for rel in [
            "docs/index.html", "docs/funding.html", "docs/partners.html", "docs/safety.html",
            "docs/benchmarks.html", "docs/install-codex.html", "docs/install-claude.html",
            "docs/install-agent-skill.html",
        ]:
            text = (ROOT / rel).read_text(encoding="utf-8")
            self.assertIn('href="favicon.ico"', text, rel)

    def test_social_card_is_1200_by_630_png(self):
        data = (ROOT / "docs/assets/social-card.png").read_bytes()
        self.assertEqual(data[:8], b"\x89PNG\r\n\x1a\n")
        width, height = struct.unpack(">II", data[16:24])
        self.assertEqual((width, height), (1200, 630))


if __name__ == "__main__":
    unittest.main()
