# Source access policy

Last checked: 2026-11-15. Read this file before any access to a website. Each retailer's tier and check date are in the `Access` column of `retailers-by-country.md`; non-retail sources and APIs are in sections 5 and 6 below. Rules marked "project rule" are plugin policy, not external facts. The notes on terms of use are a record of what the texts read say, not legal advice.

## 1. Which agent the rules apply to

Pages a user asks Claude to read are fetched as `Claude-User`; `ClaudeBot` is Anthropic's training crawler and `Claude-SearchBot` its search indexer [1]. Apply the robots.txt group that names `Claude-User`; if none does, the `*` group. A block on `ClaudeBot`, `anthropic-ai` or `Claude-Web` alone does not apply to `Claude-User` (maintainer decision, 2026-11-15); the browser fallback of `research-method.md` section 7 stays open there on the user's yes.

## 2. Selection criteria

A source is read automatically (tier A) only if all of these hold:

1. robots.txt does not disallow the product page path for the agent of section 1.
2. robots.txt does not block `Claude-User` (section 1). A block naming other price or AI bots only is recorded in the row's notes, not counted as a refusal (project rule).
3. Price (with VAT shown or stated), stock and shipping are readable in the fetched page; structured data preferred.
4. The seller is identifiable (company name, registration number, legal notice) and the warranty is stated.
5. The terms of use read do not forbid automated reading or reuse of prices.
6. The site ships to the buyer's country.

A source failing 1, 2 or 5 is tier B. A source whose robots.txt or terms could not be read is tier B too, with the reason ("robots.txt unreadable (HTTP 403)"). Failing 3, 4 or 6 alone does not change the tier: it lowers the row's confidence or excludes the offer, as `research-method.md` and `retailer-criteria.md` already say.

## 3. Tiers

| Tier | Behaviour |
|---|---|
| `A` | Read product pages automatically, one page at a time. A category or filter page (for example the chip's filter) only where robots.txt allows its path. Never the site's own search, a sort URL or a promotion or deals section. |
| `B` | Link only: give the URL and ask the user to open it, paste the text or send a screenshot (`research-method.md` section 7, step 5). The browser fallback of section 7 step 4 does not apply to a site refused by robots or terms. |
| `C` | Official API with the user's own key (section 6). The plugin never ships, asks to paste into a file, or stores a key; it only documents where the user plugs one in. |
| `browser` | Amazon and AliExpress only: never `~~web fetch`, product, offer and store pages through the user's browser on their yes, within the 5-page cap (`research-method.md` section 7, step 4; maintainer decision of 2026-11-10). |

## 4. Usage rules

1. Access starts from a user request on a named part, a deal or a pasted list, never from a background crawl. A `track-price` schedule the user set for named items counts as such a request.
2. One page at a time per host. When `price-scout` agents run in parallel, each host goes to one agent only.
3. Wait about 2 seconds between two requests to the same host. Best effort: the fetch tool has no delay setting, so this is a rule of conduct, not a guarantee.
4. Stop reading a host at the first error or block (robots refusal, HTTP 403 or 429, captcha, bot page, login wall): record it, give the link, move on. Never a cache, mirror, archive copy, proxy, changed user agent or captcha workaround (`research-method.md` section 7).
5. Every price shown carries its source URL and its read date. A price read more than 24 hours before the answer is labelled `stale` and is never a same-day reference (`find-deals`, `hunt-prices`). Earlier readings kept by `track-price` and dated reference snapshots (`used-market-checklist.md`) stay usable as history, with their date.
6. Error-price and deal-alert sites are never a reference price: they are delayed, often expired and often cancelled. A deal list may start a `find-deals` check; the reference always comes from retailer pages.
7. Check the exact domain and the legal notice before trusting a price: look-alike domains exist.

## 5. Non-retail sources

Specification, used-market and benchmark sources, checked 2026-11-15.

Retailers, classifieds and refurbishers (eBay UK and US, Leboncoin, Kleinanzeigen, Back Market) are typed in `retailers-by-country.md`. Terms of use below were read through the fetch tool, which returns summaries: re-read the page before quoting it.

| Source | URL | Type | Access | Notes | Source |
|---|---|---|---|---|---|
| eBay France | https://www.ebay.fr/ | used | B (2026-11-15): terms bar bots and scrapers (ClaudeBot and anthropic-ai disallowed `/`, Claude-User under `*`) | Sold listings (`/sch/`) disallowed for `*`. Ask the user for the listing text or a screenshot. | [2][5] |
| eBay Germany | https://www.ebay.de/ | used | B (2026-11-15): same eBay user agreement as eBay France (terms bar bots and scrapers); ClaudeBot and anthropic-ai disallowed `/`, Claude-User under `*` | Terms read in part (first 100,000 of 135,000 characters): no clause found there. | [2][6] |
| TechPowerUp | https://www.techpowerup.com/ | specs | B (2026-11-15): robots.txt disallows `/` for Claude-User and anthropic-ai | Do not fetch or cite, as `research-method.md` section 7 says. | [2] |
| NVIDIA | https://www.nvidia.com/ | specs | A (2026-11-15): robots.txt allows product pages for `*`; the legal terms (section 3.2(f)) bar robots, spiders, scrapers and data-mining tools | Maintainer decision (2026-11-15): manufacturer pages stay read as before, one page at a time on a user's request, as rank 1 for specs. Spec pages readable in a test (RTX 5090 page). | [2][7] |
| ASUS | https://www.asus.com/ | specs | A (2026-11-15): robots.txt allows `*`; the terms (clause 1.8.4, in the "Website Events" part) bar "data mining, robots, or similar data gathering and/ or extraction tools" | Maintainer decision (2026-11-15): read as before, one page at a time on a user's request. | [2][8] |
| Intel ARK | https://ark.intel.com/ | specs | A (2026-11-15): terms (section 4.1.14 to 4.1.17) bar automated searches, bots, scraping and data mining; robots.txt redirected to an HTML page | Maintainer decision (2026-11-15): read as before, one page at a time on a user's request. | [9] |
| AMD | https://www.amd.com/ | specs | A (2026-11-15): robots.txt and terms unreadable (timeout) | Maintainer decision (2026-11-15): read as before when reachable, one page at a time; record a block as `blocked`. | [2] |
| GitHub (llama.cpp benchmarks) | https://github.com/ggml-org/llama.cpp/discussions | benchmark | A (2026-11-15): Claude-User named with path rules only, Crawl-delay 1; terms read have no robots clause | Benchmark numbers readable in the discussion pages. | [2][10] |
| LocalScore | https://www.localscore.ai/ | benchmark | A (2026-11-15): no robots.txt (HTTP 404); no terms found | Leaderboard readable. | [11] |

## 6. APIs (tier C)

| API | Access | Status (2026-11-15) | Source |
|---|---|---|---|
| Keepa API (Amazon price history) | C (2026-11-15) | Unresolved: keepa.com shows its plans only through JavaScript, so no plan, price or token figure was read. Secondary sources claim no free tier and about 49 EUR a month for 20 tokens a minute; their tier ladders disagree. The user supplies their own key. | [3] |
| Amazon Creators API | C (2026-11-15) | Replaces the Product Advertising API 5.0, which Amazon states "has been deprecated"; the official page read gives no retirement date (secondary sources say 15 May 2026). For Amazon Associates; the user plugs in their own credentials, never the author's. | [4] |

## 7. How to update

For each new or changed source: read the raw robots.txt, read the terms of use, test one product page, then set the `Access` value with the date. Move a source to tier B as soon as a rule refuses it. `scripts/check_content.py` fails when a retailer row has no `Access` tier and date or no URL.

## Not verified

- Terms of use of most retailers outside France, and of LDLC (its sales terms page returned no text on 2026-11-15) and Materiel.net (sales terms PDF unreadable). Absence of a clause in a text read does not mean automated reading is allowed.
- Product path of most tier A rows: robots.txt was read for the root and the named agents, not for each site's product URLs (checked for LDLC, GrosBill, Cybertek, Materiel.net and TopAchat).
- Rows outside France where robots.txt allows reading but product pages answered HTTP 403, 429 or timed out on 2026-11-15: Mindfactory, Caseking, Notebooksbilliger, Coolmod, ePrice, Yeppon, CCL Online, Ebuyer, B&H. Treat as `blocked` when it happens again (`research-method.md` section 7).
- Leboncoin terms: page returned HTTP 403; its robots.txt header states that automated access is forbidden without permission.
- Amazon and AliExpress terms: not read (HTTP 503; redirect to a 404 page).

## Sources

1. Anthropic, "Does Anthropic crawl data from the web, and how can site owners block the crawler?", https://support.claude.com/en/articles/8896518-bots-and-crawlers, read 2026-11-15, full
2. Raw robots.txt files fetched 2026-11-15 from each retailer's `/robots.txt` (URL in the row of `retailers-by-country.md`)
3. keepa.com, https://keepa.com/#!api, read 2026-11-15, unreadable (JavaScript only)
4. Amazon Associates, PA-API 5 deprecation, https://affiliate-program.amazon.com/creatorsapi/docs/en-us/paapiv5-deprecation, read 2026-11-15, full
5. eBay France, user agreement, https://www.ebay.fr/help/policies/member-behaviour/user-agreement?id=4259, read 2026-11-15, summary through the fetch tool
6. eBay Germany, user agreement, https://www.ebay.de/help/policies/member-behaviour/user-agreement?id=4259, read 2026-11-15, partial
7. NVIDIA, legal information, https://www.nvidia.com/en-us/about-nvidia/legal-info/, read 2026-11-15, summary through the fetch tool
8. ASUS, terms of use notice, https://www.asus.com/terms_of_use_notice_privacy_policy/official-site/, read 2026-11-15, summary through the fetch tool
9. Intel, terms of use, https://www.intel.com/content/www/us/en/legal/terms-of-use.html, read 2026-11-15, summary through the fetch tool
10. GitHub, terms of service, https://docs.github.com/en/site-policy/github-terms/github-terms-of-service, read 2026-11-15, summary through the fetch tool
11. LocalScore, https://www.localscore.ai/ and https://www.localscore.ai/robots.txt (HTTP 404), read 2026-11-15
