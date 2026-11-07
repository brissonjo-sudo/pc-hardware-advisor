# Common brief for writers (orchestrator, 2026-11-07)

Shared by every writing sub-agent so that references, skills and the price-scout agent agree.

## Canonical price row (used everywhere)

| Checked | Item | Seller | Seller type | Country | Shown price | Shipping to buyer | Tax/duty est. | Landed (buyer currency) | Stock | Warranty from buyer country | Page read | Confidence | URL |

- Checked: ISO date (and time if known) the page was read.
- Item: exact model / SKU / capacity / speed as shown on the page.
- Seller type, one of: `direct retailer`, `marketplace (first-party)`, `marketplace (third-party seller)`, `professional refurbisher`, `manufacturer store`, `private party`, `proxy-buying service`.
- Shown price: amount + currency + `incl. VAT` / `excl. VAT` / `unknown`.
- Landed: shown price + shipping + import VAT/duty/handling fees, converted to the buyer's currency with the rate date; or `excluding fees` when not computable.
- Stock: `in stock (shown)`, `delay (shown: …)`, `not shown`.
- Page read: `full`, `partial (<what was missing>)`, `snippet only`, `blocked (<reason>)`, `user screenshot`.
- Confidence: `high` (full page read, price + stock + seller visible, today), `medium` (partial page or snippet, or older than 24 h), `low` (unconfirmed single mention).

## Rules for every writer

- English, imperative, written as instructions for Claude.
- Every reference file opens with: `Last checked: 2026-11-07. Values change: verify online before concluding.`
- Every table carries a date (column or caption). Every factual claim cites a source: inline `[n]` and a numbered `## Sources` list. Keep confidence levels from research. Do not add any value that is not in `research/` (or that you verified yourself with a cited official source today); gaps stay gaps, listed under `## Not verified`.
- Never name a tool as mandatory (no "use Keepa", "use Slack"): refer to tool categories (web search, web fetch, price comparator, classifieds site, scheduler, file storage, browser automation) and point to `CONNECTORS.md`. Naming retailers and sites as data is fine.
- Blocked or JavaScript-only pages: never circumvent (no alternate user agents, caches, mirrors, archive copies used to dodge a block). Record the page as blocked, then ask the user for a screenshot or pasted text.
- No personal data. No em-dash-free constraint for English files.
- Shared references live at `${CLAUDE_PLUGIN_ROOT}/references/<file>.md`; refer to them by that path from skills.
- Shared reference names (fixed): sockets-chipsets.md, memory.md, power-supplies-connectors.md, form-factors-cases.md, gpu-bandwidth-ai.md, retailers-by-country.md, retailer-criteria.md, international-buying.md, research-method.md, used-market-checklist.md.
