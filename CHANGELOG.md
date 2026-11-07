# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.2.0] - 2026-11-07

### Added

- Language switcher at the top of the README and of every translation.
- Eval case 08: the user asks to get around a site's bot protection (suite now has eight cases).

### Changed

- Final answer gate shared by all skills (`references/research-method.md` section 11): no working notes in answers, full output templates, every number traced to a dated source, struck-through "was" prices checked against the EU 30-day rule, cheap marketplace or unconfirmed sellers checked for red flags.
- Blocked sites stay blocked even when the user asks for a workaround: no browser automation, no logged-in browser session, no human-like mouse or timing. The plugin asks for a screenshot or the pasted text instead.
- `track-price`: always runs a first price check and starts the history file, then asks one explicit confirmation before creating a persistent scheduled task (cloud routine, desktop or system task). Its description now states that it takes precedence over generic scheduling skills for PC-hardware price watches.
- `check-compatibility`: verdict table always used, manufacturer pages preferred over retailer pages for specs, minimum-BIOS check states whether the board's CPU list was read or blocked.
- `size-local-ai`: line-by-line memory budget for every model called a fit; power figures sourced, with a note that transient peaks can be higher.
- `review-used-listing`: handover tests included in the first answer; market ranges carry source, date, basis and sample size.

### Fixed

- Frontmatter of `hunt-prices`, `track-price` and the `price-scout` agent is now strictly valid YAML (descriptions quoted). It could fail to parse on claude.ai or Cowork.

### Known issues

- In Claude Code, a request phrased mainly as a schedule may still be routed to the built-in scheduling skill. If so, name the skill: "use track-price".
- Price hunts that depend on import sources outside the EU are limited where those retailers block automated reading.

## [0.1.0] - 2026-11-07

### Added

- Six skills: `hunt-prices`, `check-compatibility`, `build-config`, `size-local-ai`, `review-used-listing`, `track-price`.
- `price-scout` agent, used by `hunt-prices` to read retailer pages in parallel.
- Ten shared references, dated 2026-11-07 and sourced.
- `CONNECTORS.md`: tool categories used by the plugin (`~~` placeholders), optional data sources and no-circumvention rules.
- PolyForm Noncommercial License 1.0.0 (SPDX: PolyForm-Noncommercial-1.0.0).
- `CONTRIBUTING.md` with contribution terms.
- Machine translations of the README (French, Spanish, Simplified Chinese, Hindi, Portuguese, Arabic, German, Japanese), not reviewed.
- Eval suite of seven cases.

[Unreleased]: https://github.com/brissonjo-sudo/pc-hardware-advisor/compare/v0.2.0...HEAD
[0.2.0]: https://github.com/brissonjo-sudo/pc-hardware-advisor/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/brissonjo-sudo/pc-hardware-advisor/releases/tag/v0.1.0
