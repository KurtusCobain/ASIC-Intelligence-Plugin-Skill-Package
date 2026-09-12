# Bitcoin Mining Troubleshooter Public Launch v2 Design

## Product hierarchy

Bitcoin Mining Troubleshooter is the standalone public diagnostic product. It is powered by ASIC Intelligence, but it is not ASIC Intelligence Desktop and does not require the Desktop product.

ASIC Intelligence Desktop is a separate product in development. Desktop capabilities must not be represented as Troubleshooter capabilities.

## Public release boundary

The current public package release remains v1.1.0. The v1.2.0 review bundle remains unreleased until live runtime validation, package verification, safety regression checks, and human acceptance are complete.

## Primary conversion path

The website makes the official ChatGPT plugin the easiest path to value. The hero primary CTA points to the live ChatGPT plugin. The YouTube Short is the secondary demonstration path. Package downloads remain available for Codex, Claude, and portable Agent Skill users but are secondary.

## Homepage structure

1. Hero: Bitcoin Mining Troubleshooter, powered by ASIC Intelligence.
2. Availability strip for ChatGPT, Claude pending approval, Codex, and Agent Skill.
3. Supported evidence cards.
4. Embedded YouTube demonstration.
5. Evidence-grounded diagnostic example.
6. Trust model: provenance, freshness, conflicts, unknowns, common-cause reasoning, confidence, next safe check.
7. Synthetic fleet-scale demos.
8. Distribution/install options.
9. Read-only safety boundary.
10. Founder/operator credibility.
11. Separate ASIC Intelligence Desktop note.
12. Partnerships/funding secondary to product use.
13. Validation status and FAQ.

## Measurement

Continue using the existing GA4 property. Track ChatGPT plugin clicks, YouTube demo clicks, package downloads, demo-file opens, GitHub repository clicks, Desktop-interest clicks, partner-contact clicks, and founder-profile clicks. No mining evidence, filenames, credentials, or user-provided diagnostic content may be sent to analytics.

## SEO

Keep existing canonical, sitemap, robots, and Open Graph support. Add JSON-LD for SoftwareApplication, SoftwareSourceCode, VideoObject, and FAQPage. Create four substantial problem-intent pages: ASIC miner troubleshooting, Antminer log analysis, multiple miners offline, and ASIC repair-history analysis.

## Release safety

The launch branch must not publish v1.2.0, overwrite v1.1.0 packages, claim Claude marketplace approval before approval exists, or conflate the Troubleshooter with ASIC Intelligence Desktop.

## Review and merge

All work occurs on `launch/troubleshooter-public-v2`. A draft pull request will be opened for review. No merge to `main` occurs without explicit user approval.
