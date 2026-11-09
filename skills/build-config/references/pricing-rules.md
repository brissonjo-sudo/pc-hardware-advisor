# Pricing rules for build-config

Read by `build-config` step 4. Section 1 before writing any price outside the main table; section 2 when the user accepts importing.

## 1. Price fields on every row

Every price shown anywhere in the answer (main table, routes compared, variants) carries on its own row: date read, seller, seller type, country, and landed price or `excluding fees` (compact display, `research-method.md` section 6). Never drop these columns to shorten a table; write `not shown` when a value is unknown. A date in the table title does not replace the per-row date. In prose, cite prices only with their row. Only exception: the Compared lines of the output template, which list shown prices of direct retailers of the buyer's country with their `[n]`, under one sentence giving their common read date, seller type and country; any other seller type or country there gets its own row. The Budget fit line gives totals of rows shown elsewhere in the answer; a price that appears only there needs its own row.

## 2. Import routes

Import: when the user accepts importing (or asks for "worldwide", "anywhere"), price at least one import route from OUTSIDE the buyer's customs zone (intra-EU purchases are not imports), for example a US retailer or a manufacturer store in China or Japan that ships to the buyer, for the most expensive component (sources in `retailers-by-country.md`), compute its landed price with `international-buying.md` (VAT, duty, handling fee, shipping, dated FX), and compare it with the domestic row. Whenever you have read a foreign price, compute its landed estimate (label it `estimate`, name each rate and its source); never leave it as "not comparable". Only a rate you cannot establish may stay open, and you name it. If no import page could be read, say so explicitly AND still state, with their sources from `international-buying.md`, the costs an import would add for this buyer (import VAT rate, duty or flat duty, handling fee, carrier fees), so the user can apply them to any foreign price they find.
