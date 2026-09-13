from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
PUBLIC_VERSION = "v1.1.0"
UNRELEASED_VERSION = "v1.2.0"


class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hrefs = []
        self.ids = set()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.add(attrs["id"])
        if tag == "a" and attrs.get("href"):
            self.hrefs.append(attrs["href"])


class ProductionHardeningTests(unittest.TestCase):
    def test_gitignore_blocks_common_local_junk_and_secrets(self):
        text = (ROOT / ".gitignore").read_text(encoding="utf-8")
        for entry in [
            ".env",
            ".env.*",
            ".venv/",
            "venv/",
            ".pytest_cache/",
            ".mypy_cache/",
            ".ruff_cache/",
            ".coverage",
            "htmlcov/",
            "*.log",
            "*.orig",
            "*.rej",
        ]:
            self.assertIn(entry, text)
        self.assertNotIn("*.zip", text, "release ZIPs are intentionally versioned")

    def test_security_policy_has_private_reporting_route(self):
        text = (ROOT / "SECURITY.md").read_text(encoding="utf-8")
        self.assertIn("austin@wnclogiclab.com", text)
        self.assertIn("[SECURITY]", text)
        self.assertIn("Do not open a public GitHub issue", text)

    def test_public_release_surfaces_do_not_publish_v12(self):
        surfaces = [ROOT / "README.md", ROOT / "SHA256SUMS"] + sorted(DOCS.glob("*.html"))
        for path in surfaces:
            with self.subTest(path=path.relative_to(ROOT)):
                self.assertNotIn(UNRELEASED_VERSION, path.read_text(encoding="utf-8", errors="ignore"))
        distribution_names = [p.name for p in (ROOT / "distributions").rglob("*") if p.is_file()]
        self.assertFalse(any(UNRELEASED_VERSION in name for name in distribution_names))
        self.assertIn(PUBLIC_VERSION, (ROOT / "README.md").read_text(encoding="utf-8"))

    def test_no_stale_install_anchor_remains(self):
        for path in sorted(DOCS.glob("*.html")):
            with self.subTest(page=path.name):
                html = path.read_text(encoding="utf-8")
                self.assertNotIn("index.html#install", html)

    def test_internal_links_and_fragments_resolve(self):
        page_parsers = {}
        for page in sorted(DOCS.glob("*.html")):
            parser = LinkParser()
            parser.feed(page.read_text(encoding="utf-8"))
            page_parsers[page.name] = parser

        for page_name, parser in page_parsers.items():
            for href in parser.hrefs:
                with self.subTest(page=page_name, href=href):
                    parsed = urlsplit(href)
                    if parsed.scheme or parsed.netloc or href.startswith(("mailto:", "tel:", "javascript:")):
                        continue
                    target_name = parsed.path or page_name
                    target = DOCS / target_name
                    if target_name.endswith("/"):
                        target = target / "index.html"
                    self.assertTrue(target.exists(), f"broken local link from {page_name}: {href}")
                    if parsed.fragment and target.suffix.lower() == ".html":
                        target_parser = page_parsers.get(target.name)
                        if target_parser is None:
                            target_parser = LinkParser()
                            target_parser.feed(target.read_text(encoding="utf-8"))
                        self.assertIn(parsed.fragment, target_parser.ids, f"missing fragment target for {href}")

    def test_workflows_pin_actions_and_bound_execution(self):
        verify = (ROOT / ".github/workflows/verify.yml").read_text(encoding="utf-8")
        pages = (ROOT / ".github/workflows/pages.yml").read_text(encoding="utf-8")
        for workflow in (verify, pages):
            self.assertIn("timeout-minutes:", workflow)
            self.assertIn("persist-credentials: false", workflow)
            for match in re.findall(r"uses:\s+([^\s#]+)", workflow):
                if match.startswith("actions/"):
                    self.assertRegex(match, r"@[0-9a-f]{40}$", f"action is not SHA pinned: {match}")

    def test_public_verifier_defines_hygiene_and_secret_guards(self):
        verifier = (ROOT / "tools/verify_public_repo.py").read_text(encoding="utf-8")
        for marker in [
            "JUNK_PATH_PARTS",
            "SECRET_PATTERNS",
            "LOCAL_PATH_PATTERNS",
            "unreleased-version",
            "forbidden-junk-path",
            "secret-pattern",
            "local-absolute-path",
        ]:
            self.assertIn(marker, verifier)


if __name__ == "__main__":
    unittest.main()
