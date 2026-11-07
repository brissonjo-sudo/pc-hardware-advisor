# Search playbook for hunt-prices

Last checked: 2026-11-07. Values change: verify online before concluding.

Read this file at step 3 of `hunt-prices`. It is project method (policy), not external fact. Site behaviour changes: verify on the page.

## 1. Query patterns

Search with `~~web search`. Start narrow, widen only if needed.

1. Exact manufacturer part number or SKU in quotes, plus the country word or the retailer's name: `"<MPN>" <retailer>`.
2. EAN / GTIN when known (from the manufacturer page or a retailer page): search the bare number. EAN matches are the strongest sign of the same product.
3. Full model name + capacity + speed: `<brand> <model> <capacity> <speed>`.
4. Language of the buyer's country for the word "price" or "buy" only when the site is local; keep the SKU unchanged.
5. Site-restricted queries (`site:<domain> <SKU>`) to reach one retailer's page when its own search page is JavaScript-only.

Do not trust a search snippet for a price. A snippet supports `medium` confidence at most and the row is `Page read: snippet only`.

## 2. Comparator listings vs retailer pages

- A `~~price comparator` lists merchants and prices that may be stale, may include shipping or not, and may be sponsored. Use it only to discover merchants and compare the item name.
- Never quote a comparator price as final. Open the merchant page and fill the row from that page.
- Check that the comparator's product match really is your SKU: compare MPN/EAN, capacity, speed, box vs OEM.
- Skip comparators that disallow automated access. Record them as unreadable.
- A retailer's own search or category page is also discovery only: it rarely shows the seller line, shipping or exact stock. Open the PRODUCT page of each candidate and fill the row from it. Use a listing price only when the product page is unreadable, with `Page read: partial (listing only)` and confidence `medium` at most.

## 3. Reading a retailer page

Capture, from the page text, in this order:

1. Item name, SKU/MPN, capacity, speed (exact, as shown).
2. Price, currency, VAT status (`incl. VAT`, `excl. VAT`, `unknown`).
3. Seller line (sold by / shipped by).
4. Stock and delay wording.
5. Shipping cost to the buyer country, if the page or cart estimator shows it without creating an account.
6. Warranty or returns wording, if shown.

If the price is rendered by JavaScript and absent from the text, mark `partial (price missing)` or `blocked (JavaScript only)`. Do not work around it.

## 4. Detecting "sold by third party"

1. Read "sold by" and "shipped by" / "fulfilled by". A seller name different from the marketplace name means `marketplace (third-party seller)`, even when the marketplace ships it.
2. Look for words such as "marketplace", "partner seller", "other sellers", "offers from", "new from".
3. Open the seller profile or imprint when reachable: legal name, address, trader statement.
4. If the product page has no seller line, check the site in `${CLAUDE_PLUGIN_ROOT}/references/retailers-by-country.md`:
   - listed as a direct retailer with no marketplace: Seller = site name, Seller type = `direct retailer (site type; seller line not shown)`, confidence `medium` at most;
   - known to run a marketplace, or not listed: Seller = `seller not shown`, Seller type = `unconfirmed (site may host third-party sellers)`, Page read = `partial (seller line missing)`. Keep these rows in a separate "Seller unconfirmed" group, never in the direct-retailer ranking.
5. Never type a seller from the domain name alone, without the reference or the page.

## 5. Stock and delay wording

Record the page's own words; map to the canonical Stock values.

| Wording seen | Stock cell |
|---|---|
| "in stock", "available", "ships today" | `in stock (shown)` |
| "ships in 3 to 5 days", "back-order", "delivery in 2 weeks" | `delay (shown: <wording>)` |
| "pre-order", "coming soon" | `delay (shown: pre-order, <date if shown>)` |
| "out of stock", "sold out" | `delay (shown: out of stock)`, and exclude the row from the ranking |
| nothing | `not shown` |

"Last units" and countdown timers are not stock evidence. Ignore urgency wording.

## 6. Deduplication

- Same seller, same item, same URL: keep one row, the freshest read.
- Same product reached through several comparators: keep the merchant page only.
- Same marketplace item listed by several third-party sellers: one row per seller.
- Same item, different variant (OEM vs boxed, different kit layout): different rows, labelled in Item.

## 7. When to stop searching

A source counts as read only when a product page for the item (or its closest match) was read. A homepage, a search page or an error page does not count: try the next source instead.

Stop when any of these is true:

1. At least 5 product pages from distinct direct retailers in the buyer's country were read, plus at least 3 per additional country or zone the user asked for, and further sources are not cheaper by shown price + shipping.
2. Two consecutive batches add no row cheaper than the current best.
3. All sources in the buyer-country section and the accepted import countries were tried once.
4. The user's delay or country limits leave nothing more to try.

Say in the answer which stopping rule applied. Do not claim the result is the global minimum: it is the minimum of what was read.

## 8. Prices shown excluding VAT (B2B sites)

1. Record `excl. VAT` in Shown price. Do not silently add or remove VAT.
2. A consumer can usually not buy at the excl.-VAT price: check whether the site sells to consumers and shows incl.-VAT prices at checkout or after setting the country. If it needs a business account or a VAT number, write the row as `not available to consumers (<reason>)` and exclude it from the ranking; never create an account.
3. If it sells to consumers, add the destination VAT only with a rate verified for that country. Otherwise leave Landed as `excluding fees` and list the missing rate under "Not verified".
4. Non-EU sites may show prices that exclude sales tax by design. Treat as `excl. VAT` unless the page says otherwise.

## 9. Briefing price-scout

Send one brief per batch of about 3 to 6 sources. Fill every field; do not add opinions or hints about expected prices. Template:

```
Item: <brand, exact model, SKU/MPN, EAN if known, capacity, speed, box/OEM>
Acceptable equivalents: <none | list of exact SKUs>
Buyer country: <country>   Buyer currency: <code>
Condition: <new | new or refurbished>
Today: <ISO date and time>
Sources (read each once):
1. <site> | <URL or search query>
2. <site> | <URL or search query>
...
Return: only the canonical price rows table and an "Unreadable" list.
Do not compute taxes. Leave Landed as `excluding fees` unless shipping to the buyer country is shown.
Never bypass blocks; never log in; never create accounts.
```

After the reply: check the column count (14), check that no cell contains a guess, and re-open the cheapest rows yourself.
