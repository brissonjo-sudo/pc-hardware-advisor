# Audit A6a: factual accuracy, European retailer list

- Date: 2026-11-08
- Model: Haiku 5.5 (claude-haiku-5-5)
- Tool calls: 43 (2 Read, 1 ToolSearch, 39 WebFetch, 1 Write). Web fetches: 39 of the 40 cap.
- Files read: `research/audit/_brief.md`, `references/retailers-by-country.md` (Legend lines 15-25; France 27-40; Belgium 42-54; Netherlands 56-68; Luxembourg 70-79; Germany 81-97; Spain 99-110; Italy 112-125; United Kingdom 127-140).
- Scope: the 8 sections named in the brief (France, Belgium, Netherlands, Luxembourg, Germany, Spain, Italy, United Kingdom). 73 rows in those sections.
- Sampling: the first 3 rows of each section (24 rows) plus 15 high-use rows (LDLC, Rue du Commerce, GrosBill, Back Market FR, Hardware.info, Back Market BE, bol.com, Coolblue NL, Alternate.de, Notebooksbilliger, Amazon.de, Amazon.es, Amazon.it, Amazon UK, eBay UK). 39 rows sampled, 34 not sampled.
- Method: one fetch per sampled row (homepage). Fetch failures are recorded as blocked and were not retried. No cache, mirror or alternate user agent. One 301 redirect (pccomponentes.es) was followed once to read its stated target.
- Readability column: the header still reads "Auto-readable (2026-11-07)" (line 20) and line 3 reads "Last checked: 2026-11-07". Both dates are still stated as the check date. No 2026-11-08 date appears anywhere in the file.

## Findings

| id | axis | severity | evidence | failure_case | minimal_fix | effort |
|---|---|---|---|---|---|---|
| shop24-lu-listed-direct-but-hosts-third-party-sellers | A | major | https://www.shop24.lu/ (checked 2026-11-08): homepage lists "Vendeurs" (e.g. "Musthave Global") and invites sellers with "Commencez à vendre". No statement that it sells its own stock. File line 76 types it `direct retailer`. | A buyer reads Shop24 offers as first-party stock, merges them with direct-retailer prices, and does not learn that a third-party seller supplies the item (warranty and returns may differ). | Change line 76 seller type to `marketplace (mixed)` until the seller of each offer is read. Move the row to the marketplace list. | S |
| pccomponentes-es-url-redirects-to-com | A | minor | https://www.pccomponentes.es/ (checked 2026-11-08): 301 to http://www.pccomponentes.com/. The .com page does not state Spain (only Spanish text and EUR prices). | The URL on line 105 leads to a different domain. The file note "target not fetched" is now out of date. | Record the redirect in the row, and check the country on the target before keeping the .es URL. | S |
| materiel-net-footer-marketplace-link-not-noted | A | info | https://www.materiel.net/ (checked 2026-11-08): footer "Marketplace" link; catalogue described as chosen by staff ("sélectionnent avec soin les références de notre catalogue"). No "vendu par" wording on the homepage. | Line 33 says "direct retailer" and "Own stock vs marketplace not confirmed". The footer shows a marketplace exists, so the row should say so. | Add "footer shows a Marketplace link; per-offer seller not checked" to Notes. | S |
| back-market-typed-as-refurbisher-but-platform-calls-itself-marketplace | A | info | https://www.backmarket.fr/ (checked 2026-11-08): structured data says "marketplace internationale" and "parmi + de 250 reconditionneurs". https://www.backmarket.be/ (checked 2026-11-08): FAQ says "tous les vendeurs". | The Legend types sellers per offer. A platform-wide `professional refurbisher` label hides that offers come from many refurbishers with different warranties and ratings. | Keep the type, and add "platform is a marketplace of refurbishers; type and warranty per offer" to Notes in all Back Market rows (FR, BE, NL, DE, ES, IT, US). | S |
| geizhals-de-readability-blocked-now-readable | A | info | https://geizhals.de/ (checked 2026-11-08): product names, prices and "371.565 aktive Händler" visible, no error notice. | Line 85 says "blocked (HTTP 403)" as of 2026-11-07. A reader who trusts the file skips a comparator that now returns data. | Update the cell on a full re-check. Keep freshness and seller mixing as unverified. | S |
| not-tested-rows-now-readable | A | info | Fetched 2026-11-08: https://www.alternate.be/ (yes, session-expired notice); https://www.vandenborre.be/ (yes); https://www.backmarket.fr/ (yes); https://www.backmarket.be/ (yes); https://www.obiwan.lu/ (yes); https://www.shop24.lu/ (yes); https://letzshop.lu/en/vendors/linsys (partial: truncated, no product listings). | The file says "not tested" for these rows. The status is out of date. | Update the cells with the 2026-11-08 date and the result. | S |
| not-tested-rows-now-blocked | A | info | Fetched 2026-11-08: https://www.coolblue.be/ (HTTP 403); https://www.hardware.info/ (fetch error); https://www.bol.com/nl/nl/ (HTTP 403); https://www.amazon.es/ (HTTP 503); https://www.amazon.it/ (HTTP 503); https://www.amazon.co.uk/ (HTTP 503); https://www.ebay.co.uk/ (HTTP 403); https://www.kelkoo.es/ (HTTP 403). | Rows say "not tested" (rate limit or not fetched). The true status is blocked, so a buyer may plan a price read that fails. | Change these cells to `blocked (HTTP code or error)` dated 2026-11-08. | S |
| amazon-de-503-on-homepage-too | A | info | https://www.amazon.de/ (checked 2026-11-08): HTTP 503 on the homepage, not only the search URL. | Line 94 says the 503 "may be transient" (search URL only). The homepage also fails today. | Keep `blocked`. Remove "may be transient" or re-test in a later session. | S |
| rue-du-commerce-and-ldlc-error-banner | A | info | https://www.rueducommerce.fr/ (checked 2026-11-08): product names and prices visible, plus "Une erreur est survenue". https://www.ldlc.com/ (checked 2026-11-08): same error text, names visible, no prices. | Line 38 says readable `yes`. The page shows an error banner, so a reader may trust partial content. | Note the error banner in the Notes cell, or re-check and keep the status as `partial`. | S |
| auto-readable-column-date-still-2026-11-07 | A | info | references/retailers-by-country.md:20 (column header "Auto-readable (2026-11-07)") and line 3 ("Last checked: 2026-11-07"). | The date is correct for the file's own tests. However, about 15 statuses changed on 2026-11-08 and the header does not show it. | Add a 2026-11-08 recheck date to the header or to each changed cell. | S |

## Claim table

| claim_id | file:line | stated_value | official_source_url | checked_on | result | note |
|---|---|---|---|---|---|---|
| fr-ledenicheur | 31 | price comparator; readable yes | https://www.ledenicheur.fr/ | 2026-11-08 | confirmed | Comparator, FR footer, merchant names and prices visible ("chez Amazon.fr", "+16 marchands"). Status unchanged. |
| fr-idealo | 32 | price comparator; blocked (fetch error) | https://www.idealo.fr/ | 2026-11-08 | blocked | Tool fetch error, cause unknown. Same as 2026-11-07. Not retried. |
| fr-materiel | 33 | direct retailer; yes | https://www.materiel.net/ | 2026-11-08 | confirmed | Staff-selected catalogue wording, FR, EUR, prices visible. Footer "Marketplace" link, see finding materiel-net-footer-marketplace-link-not-noted. |
| fr-ldlc | 34 | direct retailer (plus marketplace); partial | https://www.ldlc.com/ | 2026-11-08 | confirmed | Footer "Vendez sur LDLC" and "Marketplace"; "catalogue de plus de 25 000 références" matches. Error banner, no prices. Status partial, unchanged. |
| fr-topachat | 35 | direct retailer; partial | - | - | not-checked | not-checked (sampled). |
| fr-cybertek | 36 | direct retailer; yes | - | - | not-checked | not-checked (sampled). |
| fr-grosbill | 37 | direct retailer; yes | https://www.grosbill.com/ | 2026-11-08 | confirmed | "Vous voyez le stock de GrosBill", SAV en France, prices visible. Status unchanged. |
| fr-rue-du-commerce | 38 | direct retailer (plus marketplace); yes | https://www.rueducommerce.fr/ | 2026-11-08 | confirmed | "vendus et expédiés par Rue du Commerce"; footer "Vendez sur RDC". Error banner shown, see finding. |
| fr-back-market | 39 | professional refurbisher; not tested | https://www.backmarket.fr/ | 2026-11-08 | confirmed | "plus de 250 reconditionneurs", fr-fr locale, EUR. Readable yes (was not tested). |
| fr-leboncoin | 40 | private party; not tested | - | - | not-checked | not-checked (sampled). |
| be-alternate | 46 | direct retailer; not tested | https://www.alternate.be/ | 2026-11-08 | confirmed | "Ruim assortiment op voorraad", Belgian shipping, EUR. No marketplace wording. Readable yes, was not tested. |
| be-vandenborre | 47 | direct retailer; not tested | https://www.vandenborre.be/ | 2026-11-08 | confirmed | "onze eigen specialisten", 71 shops in Belgium. Readable yes, was not tested. |
| be-coolblue | 48 | direct retailer; not tested | https://www.coolblue.be/ | 2026-11-08 | blocked | HTTP 403. Seller type not verifiable today. |
| be-informatique | 49 | direct retailer; not tested | - | - | not-checked | not-checked (sampled). |
| be-hardware-info | 50 | price comparator; not tested | https://www.hardware.info/ | 2026-11-08 | blocked | Tool fetch error. Not in the first 3 rows (extra row). |
| be-beslist | 51 | price comparator; not tested | - | - | not-checked | not-checked (sampled). |
| be-bstore | 52 | price comparator; not tested | - | - | not-checked | not-checked (sampled). |
| be-2dehands | 53 | private party; not tested | - | - | not-checked | not-checked (sampled). |
| be-back-market | 54 | professional refurbisher; not tested | https://www.backmarket.be/ | 2026-11-08 | confirmed | FAQ "tous les vendeurs"; prices in EUR (fr-be); company address in Paris. Readable yes. |
| nl-tweakers | 60 | price comparator; blocked (fetch error) | https://tweakers.net/pricewatch/ | 2026-11-08 | blocked | Tool fetch error, unchanged. |
| nl-kieskeurig | 61 | price comparator; yes | https://www.kieskeurig.nl/ | 2026-11-08 | confirmed | "616 aangesloten webshops", "v.a." prices and shop counts visible, Dutch. Unchanged. |
| nl-alternate | 62 | direct retailer; not tested | https://www.alternate.nl/ | 2026-11-08 | confirmed | No marketplace wording, but no own-stock statement either (plausible, not proven). Readable yes, was not tested. |
| nl-azerty | 63 | direct retailer; not tested | - | - | not-checked | not-checked (sampled). |
| nl-megekko | 64 | direct retailer; not tested | - | - | not-checked | not-checked (sampled). |
| nl-coolblue | 65 | direct retailer; blocked (HTTP 403) | https://www.coolblue.nl/ | 2026-11-08 | blocked | HTTP 403, unchanged. |
| nl-bol | 66 | marketplace (mixed); not tested | https://www.bol.com/nl/nl/ | 2026-11-08 | blocked | HTTP 403 (was not tested). Seller mix not verifiable today. |
| nl-back-market | 67 | professional refurbisher; not tested | - | - | not-checked | not-checked (sampled). |
| nl-marktplaats | 68 | private party; not tested | - | - | not-checked | not-checked (sampled). |
| lu-shop24 | 76 | direct retailer; not tested | https://www.shop24.lu/ | 2026-11-08 | changed | New value: `marketplace (mixed)` until per-offer seller is read. Homepage lists "Vendeurs" and "Commencez à vendre". Readable yes (prices visible). Major finding. |
| lu-linsys | 77 | marketplace (third-party seller); not tested | https://letzshop.lu/en/vendors/linsys | 2026-11-08 | confirmed | Letzshop vendor page, Luxembourg company (Ehlerange). No product listings visible: readability partial (truncated). |
| lu-obiwan | 78 | direct retailer (physical); not tested | https://obiwan.lu/ | 2026-11-08 | confirmed | "nous nous concentrons sur la vente d'ordinateurs", Rue de Beggen, prices visible. Readable yes, was not tested. |
| lu-electronic-shop | 79 | direct retailer; not tested | - | - | not-checked | not-checked (sampled). |
| de-geizhals | 85 | price comparator; blocked (HTTP 403) | https://geizhals.de/ | 2026-11-08 | confirmed | Comparator ("unabhängiges Preis- und Produktvergleichs-Portal"), 371.565 active merchants. Readability changed from blocked to yes, see finding. |
| de-idealo | 86 | price comparator; blocked (fetch error) | https://www.idealo.de/ | 2026-11-08 | blocked | Tool fetch error, unchanged. |
| de-billiger | 87 | price comparator; blocked (HTTP 403) | https://www.billiger.de/ | 2026-11-08 | blocked | HTTP 403, unchanged. |
| de-alternate | 88 | direct retailer; partial | https://www.alternate.de/ | 2026-11-08 | confirmed | No marketplace or own-stock wording found. Product names and prices visible, session-expired notice. Partial, unchanged. |
| de-mindfactory | 89 | direct retailer; blocked (HTTP 403) | - | - | not-checked | not-checked (sampled). |
| de-caseking | 90 | direct retailer; blocked (HTTP 403) | - | - | not-checked | not-checked (sampled). |
| de-cyberport | 91 | direct retailer; blocked (fetch error) | - | - | not-checked | not-checked (sampled). |
| de-notebooksbilliger | 92 | direct retailer; blocked (HTTP 403) | https://www.notebooksbilliger.de/ | 2026-11-08 | blocked | HTTP 403, unchanged. Extra row. |
| de-computeruniverse | 93 | direct retailer; blocked (fetch error) | - | - | not-checked | not-checked (sampled). |
| de-amazon | 94 | marketplace (mixed); blocked (HTTP 503) | https://www.amazon.de/ | 2026-11-08 | blocked | HTTP 503 on the homepage too (file recorded it on the search URL only). Extra row. |
| de-back-market | 95 | professional refurbisher; not tested | - | - | not-checked | not-checked (sampled). |
| de-refurbed | 96 | professional refurbisher (mixed); partial | - | - | not-checked | not-checked (sampled). |
| de-kleinanzeigen | 97 | private party; yes | - | - | not-checked | not-checked (sampled). |
| es-idealo | 103 | price comparator; blocked (fetch error) | https://www.idealo.es/ | 2026-11-08 | blocked | Tool fetch error, unchanged. |
| es-kelkoo | 104 | price comparator; not tested | https://www.kelkoo.es/ | 2026-11-08 | blocked | HTTP 403 (was not tested, rate limit). Extra note: now blocked. |
| es-pccomponentes | 105 | direct retailer (marketplace share unchecked); partial | http://www.pccomponentes.com/ | 2026-11-08 | changed | .es URL returns 301 to pccomponentes.com. Target: "más de 100.000 artículos", footer "Vender en Marketplace" (marketplace exists, share unchecked). Spain not stated on the page. |
| es-coolmod | 106 | direct retailer; blocked (too many redirects) | - | - | not-checked | not-checked (sampled). |
| es-ldlc | 107 | direct retailer; partial | - | - | not-checked | not-checked (sampled). |
| es-amazon | 108 | marketplace (mixed); not tested | https://www.amazon.es/ | 2026-11-08 | blocked | HTTP 503 (was not tested). Extra row. |
| es-back-market | 109 | professional refurbisher; not tested | - | - | not-checked | not-checked (sampled). |
| es-wallapop | 110 | private party; partial | - | - | not-checked | not-checked (sampled). |
| it-trovaprezzi | 116 | price comparator; blocked (HTTP 403) | https://www.trovaprezzi.it/ | 2026-11-08 | blocked | HTTP 403, unchanged. |
| it-idealo | 117 | price comparator; blocked (fetch error) | https://www.idealo.it/ | 2026-11-08 | blocked | Tool fetch error, unchanged. |
| it-drako | 118 | direct retailer; yes | https://www.drako.it/ | 2026-11-08 | confirmed | Footer operator "Drako Legacy S.R.L.", "Rivenditore autorizzato", prices visible, Italian, EUR. No marketplace wording. |
| it-eprice | 119 | direct retailer; yes | - | - | not-checked | not-checked (sampled). |
| it-yeppon | 120 | direct retailer (unverified); not tested | - | - | not-checked | not-checked (sampled). |
| it-amazon | 121 | marketplace (mixed); not tested | https://www.amazon.it/ | 2026-11-08 | blocked | HTTP 503 (was not tested). Extra row. |
| it-back-market | 122 | professional refurbisher; not tested | - | - | not-checked | not-checked (sampled). |
| it-messoanuovo | 123 | professional refurbisher; not tested | - | - | not-checked | not-checked (sampled). |
| it-pccomponentes | 124 | direct retailer (refurbished tiers); not tested | - | - | not-checked | not-checked (sampled). |
| it-subito | 125 | private party; not tested | - | - | not-checked | not-checked (sampled). |
| uk-pricespy | 131 | price comparator; yes (homepage) | https://pricespy.co.uk/ | 2026-11-08 | confirmed | UK, GBP. Merchants include Amazon.co.uk, eBay, Currys, OnBuy, Very, Temu, Scan, ao.com, Boots, Notino. Temu is a marketplace not listed in the row. |
| uk-pcpartpicker | 132 | price comparator; blocked (HTTP 403) | https://uk.pcpartpicker.com/ | 2026-11-08 | not-checked | Sampled but not fetched: file (line 132 and Not verified) says robots.txt disallows Claude user agents and forbids fetching. Not re-checked. |
| uk-google-shopping | 133 | price comparator; blocked (browser notice) | https://www.google.com/shopping | 2026-11-08 | blocked | Only a browser-update notice. No listings or merchant names, unchanged. |
| uk-scan | 134 | direct retailer; blocked (HTTP 403) | - | - | not-checked | not-checked (sampled). |
| uk-overclockers | 135 | direct retailer; yes | - | - | not-checked | not-checked (sampled). |
| uk-ccl-online | 136 | direct retailer; blocked (HTTP 403) | - | - | not-checked | not-checked (sampled). |
| uk-ebuyer | 137 | direct retailer; not tested | - | - | not-checked | not-checked (sampled). |
| uk-amazon | 138 | marketplace (mixed); not tested | https://www.amazon.co.uk/ | 2026-11-08 | blocked | HTTP 503 (was not tested). Extra row. |
| uk-ebay | 139 | marketplace (third-party seller); not tested | https://www.ebay.co.uk/ | 2026-11-08 | blocked | HTTP 403 (was not tested). Extra row. |
| uk-gumtree | 140 | private party; not tested | - | - | not-checked | not-checked (sampled). |

Rows 35, 36, 40, 49, 51, 52, 53, 63, 64, 67, 68, 79, 89, 90, 91, 93, 95, 96, 97, 106, 107, 109, 110, 119, 120, 122, 123, 124, 125, 134, 135, 136, 137, 140 are not sampled: result `not-checked` (sampled).

## Counts per result

| result | count |
|---|---|
| confirmed | 17 |
| changed | 2 |
| could-not-verify | 0 |
| blocked | 19 |
| not-checked | 35 (34 not sampled, 1 sampled but not fetched: uk-pcpartpicker) |
| total rows | 73 |

Findings by severity: blocker 0, major 1, minor 1, info 9.

## Not checked

- **34 rows not sampled** (sampling cap of 40 fetches; 15 extra rows chosen by usage). Listed in the claim table as `not-checked (sampled)`.
- **PCPartPicker UK (line 132):** not fetched. The file says robots.txt disallows Claude user agents, and the brief and file both say not to fetch it.
- **Fetch errors without HTTP code** (idealo FR, DE, ES, IT; Tweakers; Hardware.info): the tool returned "unable to fetch" with no cause. Recorded as blocked (fetch error). Not retried.
- **Seller types on homepages only:** no category or offer page was read, so per-offer seller type on any marketplace is unverified. Materiel.net and Alternate NL "direct retailer" stays plausible, not proven.
- **Amazon (DE, ES, IT, UK):** HTTP 503 on the homepage. No alternate attempt, per the brief.
- **Redirect:** the pccomponentes.es 301 target was read once. Its country was not stated on the page.
- **Readability column date:** still stated as 2026-11-07 (header line 20 and line 3). Not updated in the file by this audit (read-only).
- **Not done:** no prices checked, no robots or terms of service read, no Azerty.nl fetch (dropped to stay within cap; one fetch left unused).
