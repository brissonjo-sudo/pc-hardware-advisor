# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.8.5] - 2026-11-16

### Fixed

- `find-deals`: the same-day reference is never another deal of the same list, nor a site whose seller type is `not shown` (Joybuy, Galaxus). A live test called an RTX 5080 deal dearer than elsewhere (+5.3 %) against another deal with an unconfirmed seller.
- `find-deals`: a same-chip reference not drawn from at least 3 chip listings gives `not verified (chip listings not read)`. The same test gave good-price verdicts while stating the chip listings were not read.

### Added

- Test case 24: graders `reference-not-a-deal` and `chip-listings-gate`.

## [0.8.4] - 2026-11-16

### Fixed

- `find-deals`: a same-chip reference is the cheapest in-stock offer of the chip found on the retailers' chip listings, never another deal's exact-model reference reused; deals sharing a chip share one read of each listing. A live test reused a 2,269.95 EUR exact-model reference for two other RTX 5080 deals and showed a 20.7 % gap.
- `find-deals`: a `not verified` deal is never called a good price, "on paper" or otherwise, in its verdict line; a deal price not read on its own product page gets no gap and no comparison wording. A live test computed a 16.3 % gap from the price the user typed.

### Added

- `retailers-by-country.md`: Galaxus.fr row, tier B (home page HTTP 403 to automated reading, terms unread; browser fallback on the user's yes).
- Test case 24 (`deal-list-shared-chip`).

## [0.8.3] - 2026-11-16

### Fixed

- `find-deals`: a cheaper in-stock offer seen on a listing is opened on its product page before the reference is chosen. A live test dropped a 1,898.99 EUR in-stock card seen on a listing and called a deal a good price at 13 % below a 2,074.99 EUR reference, instead of about 5 %.
- `find-deals`: a deal's price comes from its own product page; a "recommended" block on another page counts as a listing.

## [0.8.2] - 2026-11-16

### Fixed

- `find-deals`: a reference price read only on a listing gives `not verified (reference read on a listing)`, never a price verdict; the self-check asks whether the reference was read on its product page. A live test called a deal a good price at 5.2 % below a reference read on the retailer's listing.

## [0.8.1] - 2026-11-16

### Fixed

- `find-deals`: a deal older than 7 days is named with its date only, never with its price, in prose or in a table. A live test listed four ended graphics-card deals with their claimed prices.
- `find-deals` self-check: exactly one next action, the browser offer being that action when made. Three live tests ended with two or three next actions.

## [0.8.0] - 2026-11-15

### Added

- `references/source-access-policy.md`: selection criteria, tiers (A read one product page at a time, B link only, C the user's own API key, `browser` for Amazon and AliExpress), usage rules (one host per agent, best-effort 2-second spacing, stop at the first block, `stale` after 24 hours, error-price and deal-alert sites never a reference), non-retail sources and APIs.
- `retailers-by-country.md`: an `Access` column (tier, check date, finding) replaces `Auto-readable` on every row, from raw robots.txt files read on 2026-11-15 and the French retailers' terms of use.
- `check_content.py`: fails when a retailer row or a non-retail source has no tier, date or https URL.

### Changed

- `hunt-prices`, `find-deals`, `review-used-listing`, `track-price` read the policy before any site access; the `price-scout` brief excludes tier B sites and gives each host to one brief.
- `find-deals`: the chip listing is a plain category page allowed by robots.txt, never a search, sort or filter URL.
- TopAchat, eBay, Back Market, Leboncoin and Kleinanzeigen move to tier B (terms of use or robots.txt); Materiel.net stays readable (its robots.txt rule `*/produits/` does not match its `/produit/` pages).
- README and its translations: eleven shared references and a line on access tiers.
- Maintainer decisions: a block on `ClaudeBot` alone does not refuse `Claude-User` (the `*` rules apply; browser fallback on the user's yes); filter pages are read where robots.txt allows them (never a site search or sort URL); manufacturer spec pages stay read as before; the Amazon and AliExpress browser exception stays.

## [0.7.7] - 2026-11-15

### Fixed

- `build-config` now takes "one part to match parts the user already owns" (for example a motherboard for an owned CPU): one grouped question when the use is unknown, otherwise written defaults, and a table limited to that part. On 0.7.6 no skill fired for this request (2 runs of 2) and the answer gave prices from memory.
- `hunt-prices` description sends a part named only by its category to `build-config`.

## [0.7.6] - 2026-11-15

### Fixed

- `find-deals`: the same-chip reference is found from each retailer's chip listing (sorted by price), then the product page of the cheapest in-stock offer. A live test took a 2,099 EUR reference while 1,898.99 EUR was in stock at another retailer read, turning a 5 % gap into 14 %. "In stock" means the page says so in words; an offer with stock not shown is not the reference while an in-stock offer of the same chip exists.
- `research-method.md`: Sources cite a plugin reference file only for a data point taken from it (spec, retailer or bandwidth row); the plugin's method and rules are never sources.

## [0.7.5] - 2026-11-15

### Fixed

- `find-deals`: when no other direct retailer has the exact model in stock, the reference is the cheapest in-stock model of the same chip; an out-of-stock offer is never the reference. A live test left three RTX 5080 deals without reference while the chip sold well below them.
- `find-deals`: a `not verified` verdict ends with the missing check as next action, never a purchase.
- `research-method.md`: the delivery address or postal code of the user's browser session is never written.
- `retailers-by-country.md`: Joybuy.fr row (bot check and captcha, seller details not shown).

## [0.7.4] - 2026-11-14

### Fixed

- `find-deals`: an affiliate link that points straight at the retailer (Amazon `tag=`) is never clicked from a deal list; the clean product URL is opened instead (Amazon `/dp/<ASIN>`). A live test opened Amazon through a deal site's link.
- `find-deals`: the Compared label is written in the user's language.

## [0.7.3] - 2026-11-14

### Fixed

- Run ledger in `build-config`, `hunt-prices` and `find-deals`: the ledger is created with the first batch of reads, and each append goes in the same message as the next batch, so it costs no extra turn. In a test of case 12, one run ran out of turns before its answer with the ledger written in turns of its own.
- Case 12 checks that the ledger is written (`ledger-written` grader).

## [0.7.2] - 2026-11-14

### Fixed

- `find-deals`: the same-day reference is chosen among at least 3 other direct retailers when that many sell the item, shown in a Compared line per deal (retailers read with prices, others with the reason). A live test rested three verdicts on one retailer.
- `find-deals`: a deal list's update date only from the list read in the answer; volatile Monsieur PC figures removed from its source note. A live test quoted them as current without opening the page.

## [0.7.1] - 2026-11-14

### Changed

- `memory.md`: one module runs in single channel; plugin rule of two matched modules, with sourced figures (VC-Gaming 270K Plus, NoobFeed 9700X) and no general percentage. New verdict rule 9 (one module: compatible with conditions).
- `memory.md`: sourced note on Core Ultra memory-speed sensitivity (5600 versus 7800: about -11 % at 1080p with an RTX 5090, one reviewer).
- `sockets-chipsets.md`: LGA1851 future: no further CPU announced by Intel; new socket for the next generation reported by press, not by Intel.
- `build-config` lever 1 keeps two modules; `check-compatibility` flags a single module.

## [0.7.0] - 2026-11-14

### Added

- `find-deals` finds the current deals of a category when the user has none in hand ("SSD deals right now"): reads only deal lists marked `web fetch`, keeps at most 5 dated within 7 days (plugin heuristic), finds each item on the retailer's own site without following affiliate links, then runs the usual reference, safety filter and verdict.
- Hardware & Co bons plans added to "Deal lists" as `web fetch` (robots.txt and terms allow it, CC BY-ND, affiliate links declared).
- Monsieur PC bons plans added first in "Deal lists", read through the browser fallback on the user's yes (its deals load from data inside the page): retailer URL taken from Awin links without opening them, AliExpress short links never opened, prices with promo codes treated as claims.

## [0.6.2] - 2026-11-14

### Changed

- `memory.md`: the EXPO or XMP label is not a price criterion (compare speed, CL, capacity, ranks; XMP-only on AM5 with conditions; EXPO on Intel only if the kit lists an XMP profile). Sourced note on X3D memory-speed sensitivity (NoobFeed, AMD slides, PCGH), with no general percentage.
- `build-config` budget lever 1: for GPU-bound gaming or an X3D processor, the cheapest kit at the platform's official speed before any GPU step down; price gap from prices read that day.
- Origin: a creator's short on DDR5 prices, fact-checked on 2026-11-14 (the advice holds; the 50 to 100 EUR gap is about 200 EUR today, and the performance figures are only partly supported).

## [0.6.1] - 2026-11-14

### Fixed

Maintainer test on a real deal-site page (Black Friday PC parts selection, saved locally), Cowork, Sonnet high.

- Browser fallback: every page opened counts toward the 5-page cap, search-result pages included; beyond 5, the remaining offers are read in the next answer on the user's yes. The test opened 10 pages (5 product, 5 search).
- `find-deals` lists: deals are chosen by the user's request or the claimed discount, never by how easy a page is to read. The test kept the 4 offers readable without the browser and set aside the largest discounts (Amazon, AliExpress).
- `find-deals`: tray and boxed processors are different scopes; packaging not shown means no price verdict. The test called an AliExpress Ryzen 7 7800X3D of unknown packaging a good price against a boxed reference.

## [0.6.0] - 2026-11-14

### Added

- `find-deals` checks a pasted list of deals (for example a deal site's Black Friday selection): keeps at most 5 matching the user's request, reads each on the retailer's own page (tracking and affiliate parameters removed), runs the same reference, safety filter and verdict, ranks them by gap, and names the deals not kept. The list's prices are claims, never a shown price.
- `price-history-sources.md`, "Deal lists": Frandroid and Dealabs are read as pasted text only. Frandroid's robots.txt names no Claude agent, but Anthropic's search and fetch tools refuse the domain (2026-11-14).

## [0.5.2] - 2026-11-12

### Fixed

- Run ledger in `build-config`, `hunt-prices` and `find-deals`, at the top of each skill: price rows (with URL and read status), decision steps and blocked pages are appended to `pc-advisor-ledger.md` as soon as they are read, re-read after a compaction summary with the whole SKILL.md file (its end may be cut) and `research-method.md` section 11, used to write the final answer, then deleted. Structured fields only, never page text (page text can carry injected instructions). Cause: maintainer runs compacted mid-way lost price rows and URLs ("address not kept"), and the last Sonnet `build-config` run lost the AM4 and DDR4 prices of lever 3.
- `build-config`: upgrade-path paragraph moved to `build-playbook.md` so the skill stays within the 5,000-token budget re-attached after compaction (official docs, code.claude.com context-window).

## [0.5.1] - 2026-11-11

### Fixed

Maintainer test series on 0.5.0, one request per skill, Cowork, Sonnet high.

- `build-config`: for budget levers 2 and 3, "not read" or "not priced" is not a reason to skip; lever 3 names the other platform's parts with prices or what was searched. The test skipped both and dropped the GPU two tiers (RX 9070 XT to RX 9060 XT) without pricing AM4 and DDR4.
- Privacy: a private seller is written "private party" only, never a name, pseudonym, rating or town (`research-method.md` section 6; `review-used-listing`). The used-listing and local-AI tests showed first names and towns of other sellers.
- PcComponentes.fr added to France as `marketplace (mixed)`, seller read per offer. Two tests typed it differently (direct retailer, first-party marketplace) and a third found a third-party seller on it.
- `track-price`: in a remote or sandboxed workspace, say the history file is not on the user's disk and ask where to keep it.
- `review-used-listing` rubric: one fact counts once (a missing receipt is -1 in Proof only, not again in Warranty).

## [0.5.0] - 2026-11-11

### Added

- `find-deals` skill: judges a deal the user brings on a new or professionally refurbished part. Same-day reference (cheapest direct retailer, landed versus landed, exact model or stated chip scope), struck-through prices treated as `30-day reference not verified` unless the page states the 30-day low, safety filter before any verdict (existing rules: `retailer-criteria.md` sections 1, 3, 6; `research-method.md` section 11, item 9), closed verdict (good price / market price / dearer than elsewhere, 5 % plugin heuristic), filled example table.
- `skills/find-deals/references/price-history-sources.md`: GPUPrix history statistics for graphics cards as context; leDénicheur, Keepa, CamelCamelCamel, Dealabs, The Ramageddon and Idealo listed as not usable with the reason.
- Test case 13: pasted deal with payment outside the checkout and a struck-through price.

### Changed

- `research-method.md` section 11, item 8 and section 1: price-history statistics may appear in one Context line, never in a price table, headline, verdict or gap.
- `hunt-prices`, `review-used-listing` and `track-price` point to `find-deals` for deals; leDénicheur row notes its terms of use (art. 4.3 d).

## [0.4.1] - 2026-11-10

### Changed

- Amazon storefronts may be read through the browser fallback, on the user's yes, product and offer pages only, within the 5-page cap; never with web fetch, in sub-agents or in scheduled runs. Amazon.fr added to the France retailers. Same exception for AliExpress (its robots.txt blocks ClaudeBot), with a new `retailer-criteria.md` section 6: seller per offer, red flags, AMD tray warranty from the seller only, price-versus-risk comparison with the buyer's country, buyer protection advice. Maintainer decision after a test on a DDR5 kit: the plugin read 7 French retailers (best 553.90 EUR minimum landed), while another assistant read Amazon.fr in the browser and found 524.99 EUR delivered.

## [0.4.0] - 2026-11-10

### Added

- OpenAI Codex marketplace, experimental and not tested yet: `.codex-plugin/plugin.json` (Codex manifest with skills and display metadata) and `.agents/plugins/marketplace.json` (repository marketplace, plugin at the repository root). Install with `codex plugin marketplace add brissonjo-sudo/pc-hardware-advisor`. Format from developers.openai.com/codex/plugins/build, read 2026-11-10.

### Changed

- Each skill says that `${CLAUDE_PLUGIN_ROOT}` paths start at the plugin root, two folders above `SKILL.md`, for hosts that leave the variable unexpanded (Codex documents it for hooks only).
- `build_plugin.py` leaves the Codex files out of the Claude package; `check_content.py` checks that the Codex manifest version matches.

## [0.3.23] - 2026-11-10

### Fixed

- `check-compatibility`: the output template (verdict table and Sources) is required from the top of the skill, even for a quick question; a claim about a whole product line is labelled as an assumption. Cowork test (Sonnet high): right blocker (DDR4 on AM5) but no table, no sources and no official page read; the same prompt with Opus high followed the template.
- `review-used-listing`: filled example of the market comparison table, low confidence said below 10 items, one seller question per red flag. Cowork test (Sonnet high): a price range instead of the table, one seller question for two red flags.
- `size-local-ai`: the Recommended line says when no price row fits the budget; model config read from the publisher's repository. Cowork test (Sonnet high): RTX 3090 called the choice for a 1,000 EUR budget with a 1,150 EUR median, config read from third-party re-uploads.

## [0.3.22] - 2026-11-09

### Fixed

- `build-config` Compared lines: for the GPU and memory, each retailer's cheapest in-stock card or kit of the chip or spec, from its list sorted by price, any brand, with the exact model named. Cowork test on 0.3.21 (Opus high): the GPU line compared one board partner's model; the cheapest RX 9070 found was 907.00 EUR, against 794.95 EUR for another model at Cybertek in a test the same day, and the gap forced 16 GB of memory.

## [0.3.21] - 2026-11-09

### Fixed

- `build-config` Budget fit line: lever 2 names the cheaper model searched, with price and source, or what was searched and found nothing. "Already the cheapest I read" no longer counts. Cowork test on 0.3.20 (Opus high): budget met with the RX 9070 kept, but lever 2 on AM5 stopped at the pages already read and no A620 board was tried.
- `build-config` Compared lines point to another table only for a row it contains (the 0.3.20 test sent the reader to a table without that row).
- `build-config`: prices outside the main table go in one table per seller group, sorted by landed price, without repeating main-table rows.

## [0.3.20] - 2026-11-09

### Changed

- `build-config`: step 4.7 details (Compared and Budget fit exceptions) and step 4.8 (import routes) move to `skills/build-config/references/pricing-rules.md`, read at that step. The core price-row rule, the output template and the self-check stay in `SKILL.md`.
- `build-config`: the import route examples and the empty-slot rationale cut in 0.3.19 are restored.
- `check_content.py`: the 3 000-word cap on each `SKILL.md` becomes the official 500-line guidance plus a 4 000-word cap.

## [0.3.19] - 2026-11-09

### Fixed

- `build-config` step 5: budget levers add up. After a platform change, memory goes back to the use's minimum and the cheapest CPU and board are searched on the new platform before the GPU is lowered; each further GPU tier is one more Budget fit step. Cowork test on 0.3.18 (Opus high): memory went from 16 GB back to 32 GB DDR4 on AM4 and the GPU dropped two tiers.
- `build-config` self-check: memory and CPU checked before each GPU step down; owned parts take their specs from the manufacturer page or say why not.

### Changed

- `build-config`: three redundant phrases removed (a rationale sentence, "even a short summary table", the import route examples) to stay under the 3 000-word limit of `check_content.py`.

## [0.3.18] - 2026-11-09

### Fixed

- `build-config` step 5: budget levers in order with a new one, another platform that still meets the use (for example DDR4), and a cheaper model searched for rather than picked among pages already read. Stop at the first config that fits. Cowork tests on 0.3.17: Opus high kept 32 GB and ended 7.90 EUR over budget; Sonnet high said the CPU read was already the cheapest and never tried DDR4.
- `build-config` template: one visible Budget fit line listing each lever tried with its total, or "not needed".
- `build-config` step 4: a mixed site (LDLC, Materiel.net) counts as a direct retailer for an offer it sells itself. Sonnet high excluded both as marketplaces.
- README and translations: high effort recommended for skills that research prices.

## [0.3.17] - 2026-11-09

### Fixed

- `build-config` template: one Compared line per GPU, memory, CPU and motherboard, with each retailer read, its shown price and source, under one sentence giving their common date, seller type and country (step 4 rule 7 names this as its only exception). Cowork tests on 0.3.16 (Opus medium, Sonnet high) both fitted the budget but showed no comparison; Opus paid 184.99 EUR for a CPU listed at 118.90 EUR the same day at another retailer.
- `build-config` template: headers and values follow section 6 in the user's language ("Total livré", ISO dates, full seller types, listed read statuses). Sonnet run kept "Landed", wrote 09/11/2026 and abbreviated seller types.
- `build-config` step 2: owned-part specs come from the manufacturer page first. Sonnet run took the PSU specs from a spec database.

## [0.3.16] - 2026-11-09

### Fixed

- `build-config` step 5: before declaring an overrun, fit the budget with the playbook's cheaper levers (memory capacity, CPU or board on the same platform, GPU one tier down); "cannot be met" only when the cheapest config that meets the use is still over, shown with its total. Cowork test (Opus medium) concluded 1 986.81 EUR minimum for a 1 500 EUR budget, while a Sonnet run the same day built a full config at 1 441.50 EUR.
- `build-config` step 4: GPU, memory, CPU and motherboard read at 3 direct retailers when that many sell them; cheapest in stock kept unless a reason is stated. Same Opus run took one retailer per part.
- `build-config` template: main table gains Shown price, Stock and Source; every number in the compatibility summary cites its source; a page without a kept URL is not a source. Sonnet run had no Stock column, uncited dimensions and wattage, and a source "addresses not kept".

## [0.3.15] - 2026-11-08

### Fixed

- For a spec that several products match, retailer listings are read sorted by price ascending when the site offers that sort, and the cheapest matching product pages (up to 3 per retailer) are opened first, never only the first match (`search-playbook.md` section 2, `hunt-prices` step 5, `price-scout`). Cowork test on 0.3.14 (Sonnet high) headlined 605 EUR at Alternate.fr while three runs the same day had found a 544 EUR kit at the same retailer. Cause of the miss not established; fix plausible, not measured.

## [0.3.14] - 2026-11-08

### Fixed

- The host-forced line rule covers lines between tool calls too: no price, figure, count, progress tally or estimate (`hunt-prices`, `build-config`, gate item 1). Cowork test on 0.3.13 (Sonnet high) showed "one page read out of nine" mid-run; the opening line was compliant.
- Gate item 3: a price difference compares shown with shown or landed with landed, and says which. Same test subtracted a landed minimum from a shown price.
- Gate item 4 and the `hunt-prices` Sources template: each entry carries its own read status; a global "partial unless noted" does not count.

## [0.3.13] - 2026-11-08

### Fixed

- A line the host forces before the first tool call names only what is searched: no price, figure, count or estimate (`hunt-prices` and `build-config` ground rules, final answer gate item 1). Cowork test on 0.3.12 (Sonnet high) opened with "around 540 EUR the kit, answer in a few minutes"; the eval harness does not reproduce it.
- Gate item 9 and the `hunt-prices` landed-price step apply to storefronts, not company seats: a storefront listed for the buyer's country delivers there even when the company is abroad. Same test typed Alternate.fr as Germany, which item 9 read literally would have demoted.
- Section 6 fill rules: Country is the storefront's country for direct retailers and manufacturer stores (company seat in a note), the seller's country for third-party sellers; Seller with no name on the page is `not shown (<site>)`.
- Gate item 8: a comparator lead carries no figure and no comparison with a listed price.

## [0.3.12] - 2026-11-08

### Fixed

- A foreign offer counts as delivered to the buyer only when its page or the seller's shipping page names the buyer's country with a cost; otherwise `excluding fees` with "delivery to <country> not confirmed", never the headline (final answer gate item 9, `hunt-prices` landed-price step and summary line). Seen in a 0.3.11 run that headlined Alternate.de as best delivered to France with delivery unconfirmed.
- `hunt-prices` template: an approximate price in prose ("about 530 EUR") also cites its row, and the excluded table keeps Landed and Confidence. Both gaps seen in the 0.3.12 test run.
- Case 03: new `headline-delivery` grader.
- Case 03 on Sonnet, 2 runs, before the template line above (`tests/results/run-0312.json`): `headline-delivery` 2/2 (a cheaper Alternate.de offer is shown as a lead, never as best delivered); `prices` 0/2, `table` 0/2, `direct-only` 1/2. Judge reasons are not stored; the two gaps above are the visible rule breaks.

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
