# Connectors

## How tool references work

Plugin files use `~~category` as a placeholder for whatever tool the user has in that category. The plugin is tool-agnostic: skills describe workflows in terms of categories, never a mandatory product. Claude uses whichever tool of the category is available in the session; if none is, the skill says so and falls back to asking the user (for example for a screenshot or pasted page text).

Nothing in this plugin requires an account, an API key or a paid service. Optional connectors that need the user's own key are listed separately below.

## Categories used by this plugin

| Category | Placeholder | What it is used for | Examples of tools (any one is enough) |
|---|---|---|---|
| Web search | `~~web search` | Find manufacturer pages, retailer listings, sold listings, official rules | Built-in web search, a search connector |
| Web fetch | `~~web fetch` | Read one public page as text (retailer, comparator, official page) | Built-in web fetch, a page-reader connector |
| Price comparator | `~~price comparator` | Discover which merchants list an item; never quoted as a final price | Country comparators listed in `references/retailers-by-country.md`, or a comparator connector |
| Classifieds site | `~~classifieds site` | Recent sold or asking prices for used parts | Country classifieds listed in `references/retailers-by-country.md` |
| Scheduler | `~~scheduler` | Run `track-price` checks on a schedule | Session scheduler, desktop-app scheduled tasks, cloud scheduled routines |
| Notifications | `~~notifications` | Deliver a price alert | The scheduler's own run notice, a chat or e-mail connector |

## Rules that apply whatever the tool

- **No circumvention.** A page that refuses automated reading (403, captcha, login wall, robots rules, JavaScript-only content) is recorded as blocked. No alternate user agents, caches, mirrors, archive copies or browser automation are used to get around it. Claude asks the user for a screenshot or pasted text instead.
- **Read-only.** No tool is ever used to buy, create an account, submit a form or contact a seller.
- **Dated data.** Every value read through a connector carries its source and read date.

## Optional data sources (user's own access)

Checked 2026-11-07 (see `references/research-method.md` and `references/international-buying.md`). Terms change: verify before relying on them.

| Need | Keyless public sources | Sources needing the user's own key or approval |
|---|---|---|
| Exchange rates (indicative, mid-market) | ECB euro reference rates (daily XML), Frankfurter API, open.er-api.com (attribution required) | Commercial FX APIs |
| Tax and tariff lookups | EU TARIC consultation, EU Taxes in Europe Database, UK Trade Tariff, US HTS (USITC), CBSA tariff files | none required |
| Price data | none | eBay Browse API (approval required), Keepa (paid, Amazon price history), Yahoo! Shopping Japan and Rakuten APIs, Best Buy API (Best Buy data only; its terms bar cross-retailer analysis) |

Not listed on purpose: services whose terms or robots rules forbid automated access, retired APIs, and merchant-only APIs (details and dates in the research notes of the source repository).

Converted prices are always labelled indicative: card issuers apply their own rate and fees.
