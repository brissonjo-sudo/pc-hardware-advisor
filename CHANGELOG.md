# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.3.2] - 2026-11-07

### Changed

- Browser fallback is now offered, not imposed: when a page is blocked and a browser tool exists, the first answer ends with a one-line offer ("I can open the page in your browser: reply yes, or send a screenshot"). Claude opens the page on the user's yes. Two real Cowork tries showed that Claude would not act in the user's own browser unprompted.
- `review-used-listing`: every answer that gives a verdict includes the handover tests, follow-up turns included.

## [0.3.1] - 2026-11-07

### Fixed

- Browser fallback did not start on its own in Cowork: the browser tools were deferred and Claude concluded none was available. Claude now searches for and loads a deferred browser tool before saying none exists, and never asks for a screenshot before trying the fallback.
- `review-used-listing`: minimum GPU handover tests (identity and serial, VRAM error test, stress run with hotspot and memory-junction temperatures, fans, physical inspection).

## [0.3.0] - 2026-11-07

### Changed

- Blocked pages: browser fallback. In interactive answers, when a page the answer needs refuses automated reading and a browser tool is available, Claude opens it in the browser on its own initiative, read-only, at most 5 pages per answer, and says so (`Page read: browser (user session)`). It stops at any captcha, bot check or login wall, never imitates human behaviour, and never uses the browser in scheduled runs (`track-price`) or in the `price-scout` agent. Sites that disallow Claude or automated collection stay excluded. Rules in `references/research-method.md` section 7.
- `CONNECTORS.md`: new `~~browser` category.
- Eval case 08 now accepts a read-only browser read that stops at bot checks, and still fails any attempt to imitate a human.

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

[Unreleased]: https://github.com/brissonjo-sudo/pc-hardware-advisor/compare/v0.3.2...HEAD
[0.3.2]: https://github.com/brissonjo-sudo/pc-hardware-advisor/compare/v0.3.1...v0.3.2
[0.3.1]: https://github.com/brissonjo-sudo/pc-hardware-advisor/compare/v0.3.0...v0.3.1
[0.3.0]: https://github.com/brissonjo-sudo/pc-hardware-advisor/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/brissonjo-sudo/pc-hardware-advisor/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/brissonjo-sudo/pc-hardware-advisor/releases/tag/v0.1.0
