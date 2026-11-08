# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.3.11] - 2026-11-08

### Fixed

- `hunt-prices` output template aligned with `research-method.md` section 6: excluded offers and unconfirmed sellers go in tables with the mandatory columns, never bullet lists of prices; `excluding fees` rows sorted by shown price ascending whatever the country (the template said shown price + shipping); a price in prose cites its row number, not only its source. Root cause of the case 03 `prices` and `table` failures seen since before 0.3.6.
- Case 03 `table` grader aligned with section 6: page-read status may sit in notes or Sources. `prices` grader aligned with section 5: `seller not shown` with the site named is valid for unconfirmed rows.
- Section 6: `marketplace (third-party seller)` gets its French form, heading included.
- Case 03 on Sonnet, 2 runs, before the `prices` grader alignment (`tests/results/run-0311.json`): both answers now put excluded and unconfirmed offers in tables; `table` 1/2 (was 0/2); `prices` 0/2, not re-measured after the alignment.

## [0.3.10] - 2026-11-08

### Fixed

- `hunt-prices` and `build-config` ground rules: write nothing to the user before the final answer, including after sub-agents return and during spot checks. A real Cowork run on Sonnet (high effort) in 0.3.9 still opened with "the three readers are back, I am checking the lowest prices myself"; the rule sat in the final gate and the dispatch step only.
- Final answer gate item 1 broadened to the same span; new item 8: a comparator-only price never enters a table, headline or priced line, and shipping shown as "from" makes the landed total a minimum. Both seen in a real Cowork run on Opus (medium effort).

### Added

- `retailers-by-country.md`: Alternate.fr in the France table as a direct retailer (homepage, footer and product page read 2026-11-08: no marketplace wording, no seller line). The two models had typed it differently.
- Case 03 grader `comparator-and-from`. Case 03 on Sonnet, 2 runs: `no-working-notes`, `comparator-and-from`, `labels-translated` 2/2; both runs found Alternate.fr at 544,00 EUR, typed direct, landed "from 553,90 EUR". `table` and `prices` still fail, a known issue from before 0.3.6.

## [0.3.9] - 2026-11-08

### Fixed

- Final answer gate (`research-method.md` section 11, item 1): text written between tool calls stays on screen, so nothing is written to the user while searches or sub-agents run, and internal labels such as "condition 3" are said in plain words. Seen in a real Cowork run that opened with "two batches of three are back, waiting for the last one".
- Item 3: every amount carries its currency, excluded rows included.
- Section 6 and item 4: table headers are translated too (`Landed` becomes "Total livré"), and so are read statuses in Sources ("complète", "partielle").
- `hunt-prices`: no status messages while `price-scout` batches run; `search-playbook.md`: stopping rule stated in plain words, never by number.

### Added

- Case 03 grader `no-working-notes`, with an explicit list of allowed wording (pages read, stop reason in plain words, Sources). Case 03, 2 runs: `no-working-notes` 2/2, `labels-translated` 2/2; `table` and `prices` still fail, a known issue from before 0.3.6.

## [0.3.8] - 2026-11-08

### Fixed

- `retailers-by-country.md`: Materiel.net retyped `marketplace (mixed)`. Its Marketplace terms (supplied by the maintainer, dated 2023-09-01) confirm professional third-party sellers alongside its own stock, and a product page shows the site's own offer if it sells the item, else the cheapest marketplace offer. Seller is read per offer; no seller line stays `seller type unconfirmed`.

## [0.3.7] - 2026-11-08

### Fixed

- `retailers-by-country.md`: TopAchat and Materiel.net typed as French direct retailers with own stock (maintainer confirmation, 2026-11-08). TopAchat: an offer without a seller line is `direct retailer (seller line not shown)`. Materiel.net: its footer links to a `Marketplace` section not yet read, so an offer naming another seller is third-party and one without a seller line stays `seller type unconfirmed`. Ends the run-to-run inconsistency seen in the 0.3.6 tests.

## [0.3.6] - 2026-11-08

### Fixed

- Price tables in answers now show cell values in the user's language (seller type, "excluding fees", stock, page read, confidence), not only the headers. The English values stay the data model for price-scout output, watch lists and CSV files. Rule in `references/research-method.md` sections 5 and 6. Found in two real Cowork tests in French.
- hunt-prices said "seven" canonical seller types; there are nine since 0.3.4.

### Added

- Content check: any "N seller types" count in skills and agents must match research-method.md section 5.
- Grader `labels-translated` on cases 03 and 09 (French answers). Case 03: 2/2. Case 09: 0/2 (one run asked a clarifying question with no table, now counted as PASS; one run kept the English header "Landed").

## [0.3.5] - 2026-11-08

### Fixed

- A request to buy, fill a cart or make an offer to a seller is now refused plainly. In a real Cowork test, hunt-prices answered "not done yet" and asked for the eBay listing link, as if it would make the offer later. New item 7 of the final answer gate (`references/research-method.md` section 11), pointer in hunt-prices. When the same answer offers the browser fallback, it is worded as reading prices only.
- Case 10 grader now fails an answer that presents the purchase or offer as postponed, and states what stays allowed (draft message for the user, asking for a page to compare, reading-only browser offer). Case 10 passes 2 runs out of 2.

## [0.3.4] - 2026-11-08

Audit-driven fixes. Findings and ids are in `AUDIT.md`; evidence is in `research/audit/`.

### Fixed

- Section 301 (#3): the 178 exclusions were extended through 2027-01-09 by a USTR notice dated 2026-11-06 (previous operative date 2026-11-09). Corrected in `international-buying.md` and `used-market-checklist.md`; GPU and motherboard scope stays unverified; re-check by 2027-01-05.
- EU handling fee (#18): the EUR 2 fee applies per item irrespective of value for distance sales and is part of the VAT base (Commission guidance 3.2, 9.2). Worked example 1 recomputed (VAT 61.60, landed about EUR 375.72 excluding the carrier fee).
- Carrier fees (#24): DHL France and Royal Mail fee rows marked as not verified on the official page; the DHL France fee is removed from example 1.
- US de minimis (#19): the suspension covers all modes other than the international postal network; the postal route is not covered by the CBP rule.
- Forced-labor Section 301 (#25): the 10% and 12.5% tiers are confirmed by a USTR fact sheet; China's tier, effective date and PC-part scope remain unverified.
- RTX 5090 FE power (#20): "4x PCIe 8-pin (adapter in box) or 1x 600 W PCIe Gen 5 cable"; the "450 W or more" wording is removed.
- Cooler Master NR200P V2, MAX V2 and V3 (#21): GPU length, thickness and PSU type corrected from coolermaster.com; Lian Li A4-H2O confidence lowered to low because the page returned 404 (#26).
- B840 and B850 GPU-slot generation (#22): ASUS pages cited correctly; the unsourced HWCooling 3.0 value for B840 is removed.
- Retailer rows (#23): shop24.lu typed `marketplace (mixed)`, pccomponentes.es redirect recorded, StaticICE set to `partial`, Janpara described as a used-goods retailer, readability column header carries the 2026-11-08 re-sample.
- "When a site is blocked" (#7) now points to the browser fallback of `research-method.md` section 7 and says "one fetch attempt per page per answer".
- Directive 2019/771 (#14): article 11 is "Burden of proof" (one-year presumption, two years at Member State option); article 13 is remedies.
- Local-AI table (#15): the M3 Ultra and M4 Max rows are Llama 2 7B Q4_0 measurements, not gpt-oss 120B.
- Former to-do items (#17): size-local-ai margin wording, read date and status on every external source, no browser offer for robots-refusing sites, country taken from `retailers-by-country.md`.

### Changed

- Canonical seller types (#6): nine values only; added `direct retailer (seller line not shown)` and `seller type unconfirmed`. `seller not shown` is a Seller-column value, not a type.
- Browser click rule (#11): only "show more" on the description or the photo gallery; never anything that reveals a phone number, e-mail, address or login, adds to a cart or sends a message.
- Mandatory columns of the compact display are the single reference list (#16).
- Caps on parallel reading and guardrails for scheduled runs, in the skills and agents.

### Added

- Eval cases 09 to 12.
- `AUDIT.md`, with the audit evidence in `research/audit/`.
- Content-check assertions in CI.

## [0.3.3] - 2026-11-07

### Fixed

From real Cowork tries of cases 1 to 3 in 0.3.2 (rules placed at the end of a skill were skipped; filled templates were followed):

- `size-local-ai`: filled example of the line-by-line memory budget, a mandatory power line (vendor board power, transient note) and a source format with read date and status, all inside the output template.
- `check-compatibility`: Source column filled on every row (filled example rows), overall verdict adds "M items to confirm", PCPartPicker and TechPowerUp (forums included) never fetched or cited, forum posts labelled low confidence.
- `hunt-prices`: two attempts (site search with the exact part number, then `site:` web search) before recording "no listing found" for a listed retailer. One run had missed a cheaper offer.

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

[Unreleased]: https://github.com/brissonjo-sudo/pc-hardware-advisor/compare/v0.3.4...HEAD
[0.3.4]: https://github.com/brissonjo-sudo/pc-hardware-advisor/compare/v0.3.3...v0.3.4
[0.3.3]: https://github.com/brissonjo-sudo/pc-hardware-advisor/compare/v0.3.2...v0.3.3
[0.3.2]: https://github.com/brissonjo-sudo/pc-hardware-advisor/compare/v0.3.1...v0.3.2
[0.3.1]: https://github.com/brissonjo-sudo/pc-hardware-advisor/compare/v0.3.0...v0.3.1
[0.3.0]: https://github.com/brissonjo-sudo/pc-hardware-advisor/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/brissonjo-sudo/pc-hardware-advisor/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/brissonjo-sudo/pc-hardware-advisor/releases/tag/v0.1.0
