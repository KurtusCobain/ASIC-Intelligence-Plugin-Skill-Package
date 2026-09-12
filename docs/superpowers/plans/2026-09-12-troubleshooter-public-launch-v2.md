# Bitcoin Mining Troubleshooter Public Launch v2 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rebuild the public Bitcoin Mining Troubleshooter site around the official ChatGPT plugin, the YouTube demo, evidence-grounded diagnostics, measurable downloads, clear product separation from ASIC Intelligence Desktop, and honest v1.1/v1.2 release boundaries.

**Architecture:** Keep the site static HTML/CSS/JavaScript under `docs/`, reuse the existing visual system and GA4 installation, add behavior through small shared JavaScript helpers, and enforce public-release/product-boundary rules with Python tests. Keep v1.1.0 as the only public release while staging v1.2 language behind release gates.

**Tech Stack:** Static HTML5, CSS, vanilla JavaScript, Python `unittest`, GitHub Pages, GA4.

**Spec:** `docs/superpowers/specs/2026-09-12-troubleshooter-public-launch-v2-design.md`

## Global Constraints

- Public release remains `v1.1.0` during this branch.
- `v1.2.0` must not become a public download or current-release claim.
- Claude marketplace status must remain `pending approval` until approval is confirmed.
- Bitcoin Mining Troubleshooter and ASIC Intelligence Desktop are separate products.
- The primary CTA is the official ChatGPT plugin URL.
- Existing read-only safety boundaries remain intact.
- Existing GA4 property `G-EGDNX281X0` remains the analytics property.
- No merge to `main` without explicit human approval.

---

### Task 1: Add launch-contract tests

**Files:**
- Modify: `tests/test_site_pages.py`

**Produces:** Assertions for product hierarchy, ChatGPT CTA, YouTube demo, v1.1 release guard, Claude pending status, release asset links, structured data, landing pages, sitemap entries, and analytics event names.

- [ ] Add failing tests for the new launch contract.
- [ ] Run the site test suite and confirm failures correspond to missing launch-v2 behavior.
- [ ] Commit the red tests.

### Task 2: Rebuild homepage hierarchy and conversion path

**Files:**
- Modify: `docs/index.html`
- Modify: `docs/styles.css`

**Produces:** ChatGPT-first hero, supported-evidence cards, video section, simplified diagnostic example, trust section, distributions, safety, founder/operator context, separate Desktop note, secondary partnership section.

- [ ] Implement only the HTML/CSS needed to satisfy homepage contract tests.
- [ ] Keep all v1.2-only claims out of current-release copy.
- [ ] Run tests until homepage contract is green.
- [ ] Commit.

### Task 3: Add conversion analytics

**Files:**
- Modify: `docs/app.js`

**Produces:** A defensive click-event helper that sends GA4 events when `gtag` is available and never blocks navigation when analytics is unavailable.

- [ ] Add failing analytics-event assertions.
- [ ] Implement tracking for `chatgpt_plugin_click`, `youtube_demo_click`, `package_download`, `demo_file_open`, `github_repo_click`, `desktop_interest_click`, `partner_contact_click`, and `founder_profile_click`.
- [ ] Run tests and commit.

### Task 4: Route downloads through GitHub Releases

**Files:**
- Modify: `docs/index.html`
- Modify: relevant install HTML pages if they currently point at raw ZIPs.

**Produces:** v1.1.0 package CTAs using GitHub Release asset URLs so GitHub download counts become meaningful.

- [ ] Add failing assertions that raw `distributions/...zip` links are absent from customer-facing download CTAs.
- [ ] Replace with v1.1.0 release asset URLs.
- [ ] Run tests and commit.

### Task 5: Add structured data and search metadata

**Files:**
- Modify: `docs/index.html`

**Produces:** JSON-LD for `SoftwareApplication`, `SoftwareSourceCode`, `VideoObject`, and `FAQPage`, with v1.1.0 and truthful availability/status claims.

- [ ] Add failing structured-data assertions.
- [ ] Add JSON-LD and refreshed title/meta/OG copy.
- [ ] Run tests and commit.

### Task 6: Add four problem-intent landing pages

**Files:**
- Create: `docs/asic-miner-troubleshooting.html`
- Create: `docs/antminer-log-analysis.html`
- Create: `docs/multiple-miners-offline.html`
- Create: `docs/asic-repair-history-analysis.html`
- Modify: `docs/sitemap.xml`

**Produces:** Useful, non-thin educational pages with evidence collection guidance, common diagnostic mistakes, synthetic examples, explicit boundaries, and ChatGPT CTA.

- [ ] Add failing existence/sitemap/shell tests.
- [ ] Create pages using the existing shared shell and script.
- [ ] Add sitemap entries.
- [ ] Run tests and commit.

### Task 7: Align README and public documentation

**Files:**
- Modify: `README.md`
- Modify: public install/status documentation only where required for product hierarchy or release-link correctness.

**Produces:** `Bitcoin Mining Troubleshooter — Powered by ASIC Intelligence` as the primary public identity, with explicit statement that Desktop is separate.

- [ ] Add/adjust release-boundary tests if needed.
- [ ] Update README and status language without changing package internals.
- [ ] Run full tests and commit.

### Task 8: Final verification and draft PR

**Files:**
- No production files unless verification identifies a defect.

- [ ] Run the full Python test suite.
- [ ] Verify critical external URLs and internal routes.
- [ ] Verify no public v1.2 download/current-release claim exists.
- [ ] Verify Claude is still labeled pending approval.
- [ ] Compare branch against baseline and inspect changed files.
- [ ] Open a draft PR `launch/troubleshooter-public-v2` → `main` with validation notes.
- [ ] Stop before merge.
