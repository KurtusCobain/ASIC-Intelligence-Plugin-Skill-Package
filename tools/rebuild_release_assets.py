#!/usr/bin/env python3
"""Rebuild public release assets after a release-hardening audit.

This intentionally operates only on the public Claude distribution and public
website assets. It does not depend on or inspect any private ASIC Intelligence
source tree.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import shutil
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parents[1]
CLAUDE_ZIP = ROOT / "distributions/claude/bitcoin-mining-troubleshooter-claude-v1.1.0.zip"
REPO_URL = "https://github.com/KurtusCobain/ASIC-Intelligence-Plugin-Skill-Package"
SITE_URL = "https://kurtuscobain.github.io/ASIC-Intelligence-Plugin-Skill-Package/"


def patch_claude_archive() -> None:
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        with zipfile.ZipFile(CLAUDE_ZIP) as zf:
            zf.extractall(tmp)

        manifests = list(tmp.rglob(".claude-plugin/plugin.json"))
        if len(manifests) != 1:
            raise RuntimeError(f"expected one Claude manifest, found {len(manifests)}")
        manifest_path = manifests[0]
        plugin_root = manifest_path.parent.parent

        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        manifest["repository"] = REPO_URL
        manifest["license"] = "PolyForm-Shield-1.0.0"
        manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

        readme = plugin_root / "README.md"
        text = readme.read_text(encoding="utf-8")
        old = "invoke the skill manually with `/bitcoin-mining-troubleshooter`; Claude Code may display the fully namespaced form in its skill list."
        new = "invoke the skill manually with `/bitcoin-mining-troubleshooter:diagnose`. Plugin skills are namespaced by the plugin name in Claude Code."
        if old not in text and "/bitcoin-mining-troubleshooter:diagnose" not in text:
            raise RuntimeError("Claude README invocation text was not recognized")
        text = text.replace(old, new)
        readme.write_text(text, encoding="utf-8")

        skill = plugin_root / "skills" / "diagnose" / "SKILL.md"
        skill_text = skill.read_text(encoding="utf-8")
        if "ChatGPT/Codex" not in skill_text and "Claude Code" not in skill_text:
            raise RuntimeError("Claude SKILL platform wording was not recognized")
        skill_text = skill_text.replace("ChatGPT/Codex", "Claude Code")
        skill.write_text(skill_text, encoding="utf-8")

        rebuilt = CLAUDE_ZIP.with_suffix(".zip.tmp")
        with zipfile.ZipFile(rebuilt, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
            for path in sorted(p for p in tmp.rglob("*") if p.is_file()):
                zf.write(path, path.relative_to(tmp).as_posix())
        rebuilt.replace(CLAUDE_ZIP)


def patch_public_docs() -> None:
    docs = ROOT / "docs"
    pending = "STATIC VALIDATION · CLI CHECK PENDING"
    replacement = "CLAUDE CLI VALIDATED"

    for path in list(docs.glob("*.html")) + list(docs.glob("*.md")) + [ROOT / "README.md"]:
        text = path.read_text(encoding="utf-8")
        text = text.replace(pending, replacement)
        if path.suffix == ".html" and 'href="favicon.ico"' not in text:
            marker = '<link rel="icon" href="assets/icon.svg" type="image/svg+xml">'
            if marker in text:
                text = text.replace(marker, marker + '<link rel="alternate icon" href="favicon.ico">')
        path.write_text(text, encoding="utf-8")

    install_md = docs / "INSTALL-CLAUDE.md"
    text = install_md.read_text(encoding="utf-8")
    validation_note = (
        "\nValidation status: the final v1.1.0 archive passes both "
        "`claude plugin validate` and `claude plugin validate --strict`. "
        "Claude Code plugin skills use the namespaced form "
        "`/bitcoin-mining-troubleshooter:diagnose`.\n"
    )
    if "Validation status: the final v1.1.0 archive passes" not in text:
        anchor = "For stricter validation:\n\n```bash\nclaude plugin validate --strict ./bitcoin-mining-troubleshooter\n```\n"
        if anchor not in text:
            raise RuntimeError("INSTALL-CLAUDE validation section was not recognized")
        text = text.replace(anchor, anchor + validation_note)
    install_md.write_text(text, encoding="utf-8")

    install_html = docs / "install-claude.html"
    text = install_html.read_text(encoding="utf-8")
    old = "The public release is currently labeled static validation with CLI validation pending until that check is completed against the final package."
    new = "The final v1.1.0 archive passes Claude Code's standard and strict plugin validators. Its diagnostic skill is exposed under the namespaced command <code>/bitcoin-mining-troubleshooter:diagnose</code>."
    text = text.replace(old, new)
    install_html.write_text(text, encoding="utf-8")

    robots = docs / "robots.txt"
    robots.write_text(
        "User-agent: *\nAllow: /\nSitemap: " + SITE_URL + "sitemap.xml\n",
        encoding="utf-8",
    )

    pages = [
        "",
        "funding.html",
        "partners.html",
        "safety.html",
        "benchmarks.html",
        "install-codex.html",
        "install-claude.html",
        "install-agent-skill.html",
    ]
    sitemap = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    sitemap.extend(f"  <url><loc>{SITE_URL}{page}</loc></url>" for page in pages)
    sitemap.append("</urlset>")
    (docs / "sitemap.xml").write_text("\n".join(sitemap) + "\n", encoding="utf-8")


def _font(path: str, size: int):
    from PIL import ImageFont

    candidate = Path(path)
    if candidate.is_file():
        return ImageFont.truetype(str(candidate), size=size)
    return ImageFont.load_default()


def rebuild_social_and_favicon() -> None:
    from PIL import Image, ImageDraw

    docs = ROOT / "docs"
    bg = "#090C0B"
    surface = "#111614"
    green = "#7CFF6B"
    text = "#F2F6F3"
    muted = "#9DA9A1"

    card = Image.new("RGB", (1200, 630), bg)
    draw = ImageDraw.Draw(card)
    draw.rounded_rectangle((48, 48, 1152, 582), radius=28, fill=surface, outline="#26312C", width=2)
    draw.rounded_rectangle((84, 84, 220, 220), radius=22, fill=bg, outline=green, width=4)

    brand = _font("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 42)
    product = _font("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 25)
    hero = _font("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 48)
    meta = _font("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 22)
    icon_font = _font("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 84)

    draw.text((123, 102), "A", font=icon_font, fill=green)
    draw.text((258, 92), "ASIC INTELLIGENCE", font=brand, fill=text)
    draw.text((260, 150), "Bitcoin Mining Troubleshooter", font=product, fill=muted)

    draw.text((84, 286), "Turn mining evidence into", font=hero, fill=text)
    draw.text((84, 346), "the next diagnostic step.", font=hero, fill=green)

    # ASCII pipes are deliberate: they avoid the missing-glyph/tofu issue found
    # in the pre-release audit while remaining legible in every unfurl renderer.
    draw.text((84, 505), "READ-ONLY | EVIDENCE-FIRST | 21,470 DEMO RECORDS", font=meta, fill=muted)
    card.save(docs / "assets" / "social-card.png", format="PNG", optimize=True)

    icon = Image.new("RGBA", (64, 64), bg)
    idraw = ImageDraw.Draw(icon)
    idraw.rounded_rectangle((3, 3, 61, 61), radius=12, fill=surface, outline=green, width=3)
    small = _font("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 42)
    bbox = idraw.textbbox((0, 0), "A", font=small)
    x = (64 - (bbox[2] - bbox[0])) // 2
    y = (64 - (bbox[3] - bbox[1])) // 2 - bbox[1]
    idraw.text((x, y), "A", font=small, fill=green)
    icon.save(docs / "favicon.ico", format="ICO", sizes=[(16, 16), (32, 32), (48, 48), (64, 64)])


def refresh_checksums() -> None:
    archives = [
        ROOT / "distributions/codex/bitcoin-mining-troubleshooter-codex-v1.1.0.zip",
        CLAUDE_ZIP,
        ROOT / "distributions/agent-skill/bitcoin-mining-troubleshooter-agent-skill-v1.1.0.zip",
    ]
    lines = []
    for archive in archives:
        digest = hashlib.sha256(archive.read_bytes()).hexdigest()
        lines.append(f"{digest}  {archive.relative_to(ROOT).as_posix()}")
    (ROOT / "SHA256SUMS").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    patch_claude_archive()
    patch_public_docs()
    rebuild_social_and_favicon()
    refresh_checksums()
    print("Release hardening assets rebuilt.")


if __name__ == "__main__":
    main()
