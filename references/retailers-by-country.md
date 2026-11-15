# Retailers by country

Last checked: 2026-11-07 (access tiers: 2026-11-15). Values change: verify online before concluding.

## How to use this file

1. Pick the buyer's country. Read its section, then the sections of neighbouring countries that ship to it (see Cross-border).
2. Check direct retailers and professional refurbishers first. Read each offer's seller: a marketplace listing is typed per seller, never per site.
3. Treat price comparators as pointers to merchants, not as prices. Open the merchant page and fill the canonical price row from it.
4. Keep marketplaces in their own list in the answer. Never merge them with direct-retailer prices without the seller type.
5. Use classifieds sites (seller type `private party`) only for a used-market review with `used-market-checklist.md`. Never feed them into an automatic build.
6. Every row below is a lead, not a verified price source. Confidence is low for most rows: read the page yourself before relying on it.
7. For landed cost, duty and warranty abroad, read `${CLAUDE_PLUGIN_ROOT}/references/international-buying.md`. For tool categories, see `CONNECTORS.md`.

## Legend

| Column | Values |
|---|---|
| Seller type | `direct retailer`, `marketplace (first-party)`, `marketplace (third-party seller)`, `marketplace (mixed)` (first and third party on one site), `professional refurbisher`, `manufacturer store`, `private party`, `proxy-buying service`, `price comparator` (not a seller) |
| Access | `A`, `B`, `C` or `browser`, the check date, then the finding: tiers and rules in `source-access-policy.md` (robots.txt read raw on 2026-11-15; terms of use read for the French retailers). After it, `Fetch test 2026-11-07:` keeps the earlier result: `yes` = prices and names in the fetched HTML text, `partial (what was missing)`, `blocked (HTTP code or error)`, `not tested (reason)`. |
| API/feed | What research found. `none found` means no public buyer-side API found, not proof of absence. Merchant-side or affiliate-only access is not usable by a casual buyer. |
| Confidence | `high`, `medium`, `low`, as in research. |
| Source | Numbers in `## Sources`. |

**`not tested` is NOT `blocked`.** A rate limit was a tool-side limit, not a site decision. Try the page once in the current session and record the result (`full`, `partial`, `blocked`). Do not assume it works or fails. Do not loop on retries.

## France

| Name | URL | Seller type | Role | Access (tier and check date: `source-access-policy.md`; earlier fetch test 2026-11-07) | API/feed | Notes | Confidence | Source |
|---|---|---|---|---|---|---|---|---|
| Amazon.fr | https://www.amazon.fr/ | marketplace (mixed) | Marketplace | browser (2026-11-15): robots.txt disallows Claude-User; browser fallback only, on the user's yes. Fetch test 2026-11-07: no automated reading: browser fallback only, on the user's yes (`research-method.md` section 7) | See Amazon note | Read "Expédié par" and "Vendu par" per offer; delivery dates can run months out, record them. | low | [141] |
| Joybuy.fr | https://www.joybuy.fr/ | not shown | Retail | A (2026-11-15): root allowed for `*`, no Anthropic agent named; product path not checked. Fetch test 2026-11-07: no: "Joybuy Risk Control" page to automated reading, image captcha in the browser (2026-11-15) | none found | Captcha in the browser: stop (`research-method.md` section 7). Seller entity, VAT status and warranty not shown on the product pages read; legal notice and terms not read. | low | [157] |
| PcComponentes.fr | https://www.pccomponentes.fr/ | marketplace (mixed) | Retailer and marketplace | A (2026-11-15): root allowed for `*`, no Anthropic agent named; product path not checked. Fetch test 2026-11-07: yes (product pages, maintainer tests 2026-11-11) | none found | French storefront of a Spanish company. Read "Vendu et expédié par" per offer: PcComponentes itself (`marketplace (first-party)`) or a third-party seller with its rating (`marketplace (third-party seller)`). Free shipping shown on some offers. | medium | [156] |
| leDénicheur | https://www.ledenicheur.fr/ | price comparator | Comparator | A (2026-11-15): root allowed for `*`, no Anthropic agent named; product path not checked. Fetch test 2026-11-07: not used (terms art. 4.3 d) | none found | Merchant name per offer (Amazon.fr, Cdiscount, Rue du Commerce, eBay, Carrefour). Mixes marketplace sellers. No price date. Terms of use art. 4.3 d forbid robots and any means of retrieving its content without prior express authorisation (read 2026-11-11): discovery from search results only, never fetch its pages. | medium (homepage only) | [1] |
| idealo.fr | https://www.idealo.fr/ | price comparator | Comparator | B (2026-11-15): robots.txt unreadable (HTTP 403). Fetch test 2026-11-07: blocked (fetch error, cause unknown) | Merchant feed/import (CSV/TXT/XML), third-party sources only; not a buyer-read API | Site unread. Verify feed on idealo's business pages. | low | [3], [4], [147] |
| Materiel.net | https://www.materiel.net/ | marketplace (mixed) | Retail | A (2026-11-15): product pages `/produit/` allowed (`*/produits/`, plural, does not match them); `/recherche/`, `/product-listing/`, deals and refurbished sections disallowed. Fetch test 2026-11-07: yes | none found | Sells its own stock (maintainer, 2026-11-08) and hosts a Marketplace of professional third-party sellers (new, refurbished, used), per the Marketplace terms supplied by the maintainer (dated 2023-09-01, not fetched by research). Default offer on a product page: the site's own if it sells the item, else the cheapest marketplace offer, so a page read without a seller line can be a third-party offer; other offers are in a separate panel. Read the seller per offer: "vendu par" another seller is `marketplace (third-party seller)`, no seller line is `seller type unconfirmed`. DDR5 search showed EUR prices and "Occasion" (used) items. | medium | [5], [154] |
| LDLC | https://www.ldlc.com/ | direct retailer (plus marketplace) | Retail | A (2026-11-15): product pages `/fiche/` allowed; `/recherche/`, `/coin-des-affaires/`, `/stock-price/`, `/en/cat/` disallowed for `*`. Fetch test 2026-11-07: partial (homepage yes; search URL error page) | none found | 25,000+ references; footer links "Vendez sur LDLC" and "Marketplace". Its search pages are disallowed by robots.txt: reach products by web search. | medium | [6] |
| TopAchat | https://www.topachat.com/ | direct retailer | Retail | B (2026-11-15): robots.txt allows product pages, but the terms of use forbid any automated or manual extraction of data, prices included, without written authorisation (https://www.topachat.com/p/cgu, read 2026-11-15). Fetch test 2026-11-07: partial (search URL returned a promotional page) | none found | French direct retailer, own stock, no marketplace known (maintainer, 2026-11-08): an offer without a seller line is `direct retailer (seller line not shown)`. Use homepage or category URLs. | low | [7] |
| Alternate.fr | https://www.alternate.fr/ | direct retailer | Retail | A (2026-11-15): root allowed for `*`, no Anthropic agent named; product path not checked. Fetch test 2026-11-07: yes (2026-11-08) | none found | Alternate's storefront for France (country selector also lists Germany, see Alternate.de). No marketplace or third-party seller wording on the homepage, footer or a product page (2026-11-08). Seller line absent, so an offer is `direct retailer (seller line not shown)`. Prices incl. VAT; shipping shown "à partir de 9,90 €", so the landed total is a minimum. Seller entity and shipping origin not stated on the pages read. | medium | [155] |
| Cybertek | https://www.cybertek.fr/ | direct retailer | Retail | A (2026-11-15): product pages allowed for `*`; `/recherche`, `/api/`, configurators, PC category pages and sort or filter URLs disallowed; Crawl-delay 2 for ClaudeBot only. Fetch test 2026-11-07: yes | none found | Shows own stock; shops in Paris, Lyon, Marseille, Bordeaux; no marketplace language. | high | [8] |
| GrosBill | https://www.grosbill.com/ | direct retailer | Retail | A (2026-11-15): product pages allowed for `*`; `/recherche`, `/api/` and sort, stock, promo, price and store filter URLs disallowed; Crawl-delay 2 for ClaudeBot only. Fetch test 2026-11-07: yes | none found | Shows own stock; 10 shops; no third-party seller mention. | high | [9] |
| Rue du Commerce | https://www.rueducommerce.fr/ | direct retailer (plus marketplace) | Retail | A (2026-11-15): root allowed for `*`, no Anthropic agent named; product path not checked. Fetch test 2026-11-07: yes | none found | Footer links "Vendez sur RDC" and marketplace terms. Free shipping applies to items "vendus et expédiés par Rue du Commerce". Check seller per offer. | high (marketplace role), medium (split) | [10] |
| Back Market (FR) | https://www.backmarket.fr/ | professional refurbisher (marketplace of refurbishers) | Refurbisher | B (2026-11-15): terms of use (art. 4.5) bar scripts, robots and data extraction (read on backmarket.fr 2026-11-15). Fetch test 2026-11-07: not tested (not fetched) | none found | Sellers are professional refurbishers. Public seller ratings. Warranty and returns claims are marketing: check on page. Same platform in BE, NL, IT, US. | medium (search only) | [11] |
| Leboncoin (components) | https://www.leboncoin.fr/ck/ordinateurs/composant-informatique/p-2 | private party | Classifieds | B (2026-11-15): robots.txt disallows ad pages `/ad/` for Claude-User and states that automated access is forbidden without permission. Fetch test 2026-11-07: not tested (not fetched) | none found | 717 used listings at indexing. State condition and fraud risk. Used review only. | medium | [12] |

## Belgium

| Name | URL | Seller type | Role | Access (tier and check date: `source-access-policy.md`; earlier fetch test 2026-11-07) | API/feed | Notes | Confidence | Source |
|---|---|---|---|---|---|---|---|---|
| Alternate (BE) | https://www.alternate.be/ | direct retailer | Retail | A (2026-11-15): root allowed for `*`, no Anthropic agent named; product path not checked. Fetch test 2026-11-07: not tested (rate limit) | none found | Old forum threads only. | low | [13] |
| Vandenborre | https://www.vandenborre.be/ | direct retailer | Retail | A (2026-11-15): root allowed for `*`, no Anthropic agent named; product path not checked. Fetch test 2026-11-07: not tested (not fetched) | none found | One 2010 blog; too old to rely on. | low | [14] |
| Coolblue (BE) | https://www.coolblue.be/ | direct retailer | Retail | B (2026-11-15): robots.txt unreadable (HTTP 403). Fetch test 2026-11-07: not tested (not fetched; NL site was blocked) | none found | Selective partner programme, not an open marketplace. | low | [15] |
| Informatique.be | https://www.informatique.be/ | direct retailer | Retail | B (2026-11-15): robots.txt unreadable (no answer). Fetch test 2026-11-07: not tested (rate limit) | none found | Candidate only. | low | — |
| Hardware.info | https://www.hardware.info/ | price comparator | Comparator | B (2026-11-15): robots.txt unreadable (HTTP 400). Fetch test 2026-11-07: not tested (not fetched) | none found | Marketing source calls it a leading Belgian hardware comparison. | low | [16] |
| Beslist.be | https://www.beslist.be/ | price comparator | Comparator | A (2026-11-15): root allowed for `*`, no Anthropic agent named; product path not checked. Fetch test 2026-11-07: not tested (not fetched) | none found | Described as a Belgian shopping and comparison platform. | low | [17] |
| Bstore.be | https://bstore.be/ | price comparator | Comparator | A (2026-11-15): root allowed for `*`, no Anthropic agent named; product path not checked. Fetch test 2026-11-07: not tested (not fetched) | none found | Compares across Amazon, Bol, Coolblue, Krëfel, Vanden Borre. | low | [18] |
| 2dehands.be | https://www.2dehands.be/ | private party | Classifieds | A (2026-11-15): root allowed for `*`, no Anthropic agent named; product path not checked. Fetch test 2026-11-07: not tested (not fetched) | none found. Third-party scrapers exist: do not use. | Belgian sister of Marktplaats. PC-parts section not confirmed. | medium | [19], [20] |
| Back Market (BE) | https://www.backmarket.be/ | professional refurbisher (marketplace of refurbishers) | Refurbisher | B (2026-11-15): terms of use (art. 4.5) bar scripts, robots and data extraction (read on backmarket.fr 2026-11-15). Fetch test 2026-11-07: not tested (not fetched) | none found | Same platform as FR; sold in 16 countries (search). | medium | [11] |

## Netherlands

| Name | URL | Seller type | Role | Access (tier and check date: `source-access-policy.md`; earlier fetch test 2026-11-07) | API/feed | Notes | Confidence | Source |
|---|---|---|---|---|---|---|---|---|
| Tweakers Pricewatch | https://tweakers.net/pricewatch/ | price comparator | Comparator | A (2026-11-15): root allowed for `*`, no Anthropic agent named; product path not checked. Fetch test 2026-11-07: blocked (fetch error, cause unknown) | No official public API. Merchant feed by arrangement. An unofficial endpoint exists: do not use. | Shows shop per price (search only). Refresh four times an hour (vendor claim). | low | [21], [22] |
| Kieskeurig | https://www.kieskeurig.nl/ | price comparator | Comparator | A (2026-11-15): root allowed for `*`, no Anthropic agent named; product path not checked. Fetch test 2026-11-07: yes (server vs JS rendering unknown) | none found | "From" price plus "+X andere aanbieders"; 616 affiliated webshops. No price date. | high (shape), medium (price HTML) | [23] |
| Alternate (NL) | https://www.alternate.nl/ | direct retailer | Retail | A (2026-11-15): root allowed for `*`, no Anthropic agent named; product path not checked. Fetch test 2026-11-07: not tested (not fetched) | none found | Trustpilot 4.1 from 24,754 reviews (via automated scan site, unverified). | low | [24] |
| Azerty.nl | https://www.azerty.nl/ | direct retailer | Retail | B (2026-11-15): robots.txt unreadable (HTTP 403). Fetch test 2026-11-07: not tested (rate limit) | none found | Trustpilot 3.5 from about 8,000 reviews (search). Recent stock and service complaints. Custom PC assembly. | low | [25] |
| Megekko | https://www.megekko.nl/ | direct retailer | Retail | B (2026-11-15): robots.txt unreadable (HTML page instead). Fetch test 2026-11-07: not tested (rate limit) | none found | No meaningful review data; an automated trust score is not evidence. | low | [26] |
| Coolblue (NL) | https://www.coolblue.nl/ | direct retailer | Retail | B (2026-11-15): robots.txt unreadable (HTTP 403). Fetch test 2026-11-07: blocked (HTTP 403) | none found | Selective partner programme, not an open marketplace. | low | [15] |
| bol.com | https://www.bol.com/nl/nl/ | marketplace (mixed) | Marketplace | A (2026-11-15): root allowed for `*`, no Anthropic agent named; product path not checked. Fetch test 2026-11-07: not tested (rate limit) | Partner platform (partnerplatform.bol.com), seller-side | Third-party sellers since 2016, curated. Seller counts vary by source (about 20,000 to 52,000+). Check seller per offer. | medium | [27] |
| Back Market (NL) | https://www.backmarket.nl/ | professional refurbisher (marketplace of refurbishers) | Refurbisher | B (2026-11-15): terms of use (art. 4.5) bar scripts, robots and data extraction (read on backmarket.fr 2026-11-15). Fetch test 2026-11-07: not tested (not fetched) | none found | Same platform as FR. | medium | [11] |
| Marktplaats | https://www.marktplaats.nl/ | private party | Classifieds | A (2026-11-15): root allowed for `*`, no Anthropic agent named; product path not checked. Fetch test 2026-11-07: not tested (not fetched) | none found | Mostly private ads; scam-prone (search source). Non-binding listings. | medium | [28] |

## Luxembourg

Coverage is weak: no comparator and no classifieds site verified. Neighbouring countries (BE, FR, DE) are the working option; confirm they ship to Luxembourg.

| Name | URL | Seller type | Role | Access (tier and check date: `source-access-policy.md`; earlier fetch test 2026-11-07) | API/feed | Notes | Confidence | Source |
|---|---|---|---|---|---|---|---|---|
| Shop24.lu (eConcept Sàrl-S) | https://shop24.lu/ | marketplace (mixed) | Marketplace | A (2026-11-15): root allowed for `*`, search and cart paths disallowed (read with the fetch tool). Fetch test 2026-11-07: yes (prices visible, 2026-11-08) | none found | Wormeldange; TERRA distributor; only online shop with a clear range in search. Homepage lists "Vendeurs" and "Commencez a vendre" (read 2026-11-08): read the seller of each offer. | low | [29] |
| Linsys (on Letzshop) | https://letzshop.lu/en/vendors/linsys | marketplace (third-party seller) | Retail | A (2026-11-15): root allowed for `*`, no Anthropic agent named; product path not checked. Fetch test 2026-11-07: not tested (not fetched) | none found | Vendor on the Letzshop marketplace; PCs, laptops, components; claims immediate stock. | low | [30] |
| Obiwan Computers | https://obiwan.lu/ | direct retailer | Retail (physical) | A (2026-11-15): root allowed for `*`, no Anthropic agent named; product path not checked. Fetch test 2026-11-07: not tested (not fetched) | none found | Rue de Beggen. Only review is from 2018, negative on service: may be outdated. | low | [31] |

## Germany

| Name | URL | Seller type | Role | Access (tier and check date: `source-access-policy.md`; earlier fetch test 2026-11-07) | API/feed | Notes | Confidence | Source |
|---|---|---|---|---|---|---|---|---|
| Geizhals.de | https://geizhals.de/ | price comparator | Comparator | A (2026-11-15): root allowed for `*`, no Anthropic agent named; product path not checked. Fetch test 2026-11-07: blocked (HTTP 403) | No official API. Third-party scrapers and feed apps exist: do not use. | Freshness and seller mixing unverified. | low | [33], [60], [61], [148] |
| idealo.de | https://www.idealo.de/ | price comparator | Comparator | B (2026-11-15): robots.txt unreadable (HTTP 403). Fetch test 2026-11-07: blocked (fetch error) | Partner Web Service 2.0 is merchant-side (secondary sources); feed CSV/TXT/XML about every 30 minutes | Seller display and marketplace mix unverified. | low | [34], [63], [147] |
| Billiger.de | https://www.billiger.de/ | price comparator | Comparator | A (2026-11-15): root allowed for `*`, no Anthropic agent named; product path not checked. Fetch test 2026-11-07: blocked (HTTP 403) | none found | Nothing else verified. | low | [35] |
| Alternate.de | https://www.alternate.de/ | direct retailer | Retail | A (2026-11-15): root allowed for `*`, no Anthropic agent named; product path not checked. Fetch test 2026-11-07: partial (prices readable; filters JS-loaded; "session timed out" notice; 24 of 684 results) | none found | Appears first-party (no third-party labels). | medium | [37] |
| Mindfactory | https://www.mindfactory.de/ | direct retailer | Retail | A (2026-11-15): root allowed for `*`, no Anthropic agent named; product path not checked. Fetch test 2026-11-07: blocked (HTTP 403) | none found | Direct vs marketplace unverified. | low | [36] |
| Caseking | https://www.caseking.de/ | direct retailer | Retail | A (2026-11-15): root allowed for `*`, no Anthropic agent named; product path not checked. Fetch test 2026-11-07: blocked (HTTP 403) | none found | Homepage not read. | low | [38] |
| Cyberport | https://www.cyberport.de/ | direct retailer | Retail | B (2026-11-15): robots.txt unreadable (HTTP 403). Fetch test 2026-11-07: blocked (fetch error) | none found | Unverified. | low | [39] |
| Notebooksbilliger | https://www.notebooksbilliger.de/ | direct retailer | Retail | B (2026-11-15): robots.txt unreadable (HTTP 403). Fetch test 2026-11-07: blocked (HTTP 403) | none found | Unverified. | low | [40] |
| Computeruniverse | https://www.computeruniverse.net/ | direct retailer | Retail | B (2026-11-15): robots.txt unreadable (HTTP 403). Fetch test 2026-11-07: blocked (fetch error) | none found | Unverified. | low | [41] |
| Amazon.de | https://www.amazon.de/ | marketplace (mixed) | Marketplace | browser (2026-11-15): robots.txt disallows Claude-User; browser fallback only, on the user's yes. Fetch test 2026-11-07: blocked (HTTP 503 on search URL, may be transient) | Retired/gated, see Amazon note below | Read seller per offer. | low | [42] |
| Back Market (DE) | https://www.backmarket.de/ | professional refurbisher (marketplace of refurbishers) | Refurbisher | B (2026-11-15): terms of use (art. 4.5) bar scripts, robots and data extraction (read on backmarket.fr 2026-11-15). Fetch test 2026-11-07: not tested (rate limit) | none found | Not verified. | low | [59] |
| refurbed.de | https://www.refurbed.de/ | professional refurbisher (mixed first and third party) | Refurbisher | A (2026-11-15): root allowed for `*`, no Anthropic agent named; product path not checked. Fetch test 2026-11-07: partial (text only; no listings; "not loading") | none found | No CPU/GPU/RAM seen; desktops and accessories only. Discount claims inconsistent (40% vs 70%). | medium | [44] |
| Kleinanzeigen.de | https://www.kleinanzeigen.de/ | private party | Classifieds | B (2026-11-15): terms of use (section 5) require express written consent for bots, crawlers and scrapers (read 2026-11-15). Fetch test 2026-11-07: yes (title, price, location, date, no login) | none found | 345 results: 335 private, 10 commercial (filter counts). Terms and robots status not read. Used review only. | medium | [43] |

## Spain

| Name | URL | Seller type | Role | Access (tier and check date: `source-access-policy.md`; earlier fetch test 2026-11-07) | API/feed | Notes | Confidence | Source |
|---|---|---|---|---|---|---|---|---|
| idealo.es | https://www.idealo.es/ | price comparator | Comparator | B (2026-11-15): robots.txt unreadable (HTTP 403). Fetch test 2026-11-07: blocked (fetch error) | As idealo.de | Unverified. | low | [51] |
| Kelkoo.es | https://www.kelkoo.es/ | price comparator | Comparator | A (2026-11-15): root allowed for `*`, no Anthropic agent named; query strings disallowed (read with the fetch tool). Fetch test 2026-11-07: not tested (rate limit, two attempts) | Publisher-side token, eligibility unknown | Freshness and seller mix unverified. | low | [48], [149] |
| PcComponentes | https://www.pccomponentes.es/ (redirects 301 to https://www.pccomponentes.com/, read 2026-11-08) | direct retailer (marketplace share unchecked) | Retail | B (2026-11-15): robots.txt unreadable (HTTP 403). Fetch test 2026-11-07: partial (redirect to pccomponentes.com; footer shows "Vender en Marketplace"; Spain not stated on the page, 2026-11-08) | none found | Sells refurbished tiers (snippet only). | low | [46] |
| Coolmod | https://www.coolmod.com/ | direct retailer | Retail | A (2026-11-15): root allowed for `*`, no Anthropic agent named; product path not checked. Fetch test 2026-11-07: blocked (too many redirects) | none found | Unverified. | low | [47] |
| LDLC España | https://www.ldlc.com/es-es/ | direct retailer | Retail | A (2026-11-15): product pages `/fiche/` allowed; `/recherche/`, `/coin-des-affaires/`, `/stock-price/`, `/en/cat/` disallowed for `*`. Fetch test 2026-11-07: partial (categories and links; no prices; error banner) | none found | First-party; no marketplace seen. | medium | [45] |
| Amazon.es | https://www.amazon.es/ | marketplace (mixed) | Marketplace | browser (2026-11-15): robots.txt disallows Claude-User; browser fallback only, on the user's yes. Fetch test 2026-11-07: not tested (result not reliably attributed) | See Amazon note | Read seller per offer. | low | [49] |
| Back Market (ES) | https://www.backmarket.es/ | professional refurbisher (marketplace of refurbishers) | Refurbisher | B (2026-11-15): terms of use (art. 4.5) bar scripts, robots and data extraction (read on backmarket.fr 2026-11-15). Fetch test 2026-11-07: not tested (rate limit) | none found | Not verified. | low | [59] |
| Wallapop | https://es.wallapop.com/ | private party (plus Wallapop Pro businesses) | Classifieds | A (2026-11-15): root allowed for `*`, no Anthropic agent named; product path not checked. Fetch test 2026-11-07: partial (homepage; no listings; "Cargando...") | none found | Login need unclear. Used review only. | low | [50] |

## Italy

| Name | URL | Seller type | Role | Access (tier and check date: `source-access-policy.md`; earlier fetch test 2026-11-07) | API/feed | Notes | Confidence | Source |
|---|---|---|---|---|---|---|---|---|
| Trovaprezzi | https://www.trovaprezzi.it/ | price comparator | Comparator | A (2026-11-15): root allowed for `*`, no Anthropic agent named; product path not checked. Fetch test 2026-11-07: blocked (HTTP 403) | none found | Unverified. | low | [52] |
| idealo.it | https://www.idealo.it/ | price comparator | Comparator | B (2026-11-15): robots.txt unreadable (HTTP 403). Fetch test 2026-11-07: blocked (fetch error) | As idealo.de | Unverified. | low | [53] |
| Drako.it | https://www.drako.it/ | direct retailer | Retail | A (2026-11-15): root allowed for Claude-User; product path not checked. Fetch test 2026-11-07: yes | none found | Single operator (Drako Legacy S.R.L.), two stores, authorised reseller. Narrower range. Example: DDR5 Corsair Vengeance 5200 16GB at 324.90 EUR, reduced to 309.90 EUR. | medium | [58] |
| ePrice.it | https://www.eprice.it/ | direct retailer | Retail | B (2026-11-15): robots.txt unreadable (HTTP 403). Fetch test 2026-11-07: yes (attribution inferred from page content) | none found | Operator B2VIBE S.r.l. in footer. Informatica > Componenti. | medium | [54] |
| Yeppon | https://www.yeppon.it/ | direct retailer (unverified) | Retail | A (2026-11-15): Claude-User and Claude-SearchBot allowed `/` (read with the fetch tool). Fetch test 2026-11-07: not tested (503 or 403, ambiguous) | none found | Retry. | low | [55] |
| Amazon.it | https://www.amazon.it/ | marketplace (mixed) | Marketplace | browser (2026-11-15): robots.txt disallows Claude-User; browser fallback only, on the user's yes. Fetch test 2026-11-07: not tested (result not reliably attributed) | See Amazon note | Read seller per offer. | low | [56] |
| Back Market (IT) | https://www.backmarket.it/ | professional refurbisher (marketplace of refurbishers) | Refurbisher | B (2026-11-15): terms of use (art. 4.5) bar scripts, robots and data extraction (read on backmarket.fr 2026-11-15). Fetch test 2026-11-07: not tested (rate limit) | none found | Not verified. | low | [59] |
| Messoanuovo | https://www.messoanuovo.it/ | professional refurbisher | Refurbisher | A (2026-11-15): root allowed for `*`, no Anthropic agent named; product path not checked. Fetch test 2026-11-07: not tested (search snippet only) | none found | Refurbished computers. | low | [62] |
| PcComponentes (IT) | https://www.pccomponentes.it/pages/ricondizionati | direct retailer (refurbished tiers) | Refurbisher tiers | A (2026-11-15): root allowed for `*`, no Anthropic agent named; product path not checked. Fetch test 2026-11-07: not tested (snippet only) | none found | Grades and warranties (as new 3 years, almost new 2, functional 1) from a secondary article, not the retailer. | low | [62] |
| Subito.it | https://www.subito.it/annunci-italia/vendita/informatica/ | private party | Classifieds | A (2026-11-15): root allowed for `*`, no Anthropic agent named; product path not checked. Fetch test 2026-11-07: not tested (rate limit, two attempts) | none found | Used review only. | low | [57] |

## United Kingdom

| Name | URL | Seller type | Role | Access (tier and check date: `source-access-policy.md`; earlier fetch test 2026-11-07) | API/feed | Notes | Confidence | Source |
|---|---|---|---|---|---|---|---|---|
| PriceSpy UK | https://pricespy.co.uk/ | price comparator | Comparator | A (2026-11-15): root allowed for `*`, no Anthropic agent named; product path not checked. Fetch test 2026-11-07: yes (homepage only) | none found | Names sellers (Amazon.co.uk, eBay, OnBuy, Very, ao.com); mixes "Amazon Marketplace" and eBay. "From" price and "+N shops". No freshness stamp. PC-parts coverage unverified. | medium | [67] |
| PCPartPicker UK | https://uk.pcpartpicker.com/ | price comparator | Comparator | B (2026-11-15): robots.txt disallows Claude-User. Fetch test 2026-11-07: blocked (HTTP 403) | No official API | robots.txt disallows Claude user agents; terms exclude collecting prices. Do not fetch. Global site same (also /api/ 403). | low | [65], [145], [146] |
| Google Shopping | https://www.google.com/shopping | price comparator | Comparator | A (2026-11-15): root allowed for `*`, no Anthropic agent named; product path not checked. Fetch test 2026-11-07: blocked (browser-update notice, no content) | none found | Seller display and freshness unconfirmed. | low | [69] |
| Scan Computers | https://www.scan.co.uk/ | direct retailer (type from prior knowledge) | Retail | B (2026-11-15): robots.txt unreadable (HTTP 403). Fetch test 2026-11-07: blocked (HTTP 403) | Affiliate via Awin (base commission 1%); feed unconfirmed | Ask the retailer or Awin before any feed design. | medium (type), low (readability) | [72], [98] |
| Overclockers UK | https://www.overclockers.co.uk/ | direct retailer | Retail | A (2026-11-15): root allowed for `*`, no Anthropic agent named; product path not checked. Fetch test 2026-11-07: yes (first 100k of 224k chars) | No public API; Awin affiliate, no feed seen | Own categories; no marketplace structure visible. | high (type), medium (feed) | [73], [99] |
| CCL Online | https://www.cclonline.com/ | direct retailer (prior knowledge) | Retail | A (2026-11-15): root allowed for `*`, no Anthropic agent named; product path not checked. Fetch test 2026-11-07: blocked (HTTP 403) | none found | Unverified. | low | [74] |
| Ebuyer | https://www.ebuyer.com/ | direct retailer (prior knowledge) | Retail | A (2026-11-15): root allowed for `*`, no Anthropic agent named; product path not checked. Fetch test 2026-11-07: not tested (rate limit) | unknown | Unverified. | low | [90] |
| Amazon UK | https://www.amazon.co.uk/ | marketplace (mixed) | Marketplace | browser (2026-11-15): robots.txt disallows Claude-User; browser fallback only, on the user's yes. Fetch test 2026-11-07: not tested (rate limit) | See Amazon note | Third-party sellers mixed in (prior knowledge). | low | [83], [96] |
| eBay UK | https://www.ebay.co.uk/ | marketplace (third-party seller; private and professional) | Marketplace | B (2026-11-15): terms of use bar bots and scrapers (eBay user agreement section 3, read on ebay.fr 2026-11-15). Fetch test 2026-11-07: not tested (ebay.com returned 403) | Browse API, see eBay note | Mixed private and pro sellers. Used review only for private sellers. | medium (API), low (readability) | [82], [93] |
| Gumtree UK | https://www.gumtree.com/ | private party | Classifieds | A (2026-11-15): root allowed for `*`, no Anthropic agent named; product path not checked. Fetch test 2026-11-07: not tested (rate limit) | unknown | Used review only. | low | [87] |

## United States

| Name | URL | Seller type | Role | Access (tier and check date: `source-access-policy.md`; earlier fetch test 2026-11-07) | API/feed | Notes | Confidence | Source |
|---|---|---|---|---|---|---|---|---|
| Newegg | https://www.newegg.com/ | marketplace (mixed) | Marketplace | A (2026-11-15): root allowed for `*`, no Anthropic agent named; product path not checked. Fetch test 2026-11-07: blocked (HTTP 403) | Seller-side only (Elite Seller required); no buyer feed | Check seller per listing. | medium | [75], [94], [152] |
| Newegg Refreshed | https://www.newegg.com/ | professional refurbisher (Newegg plus partners) | Refurbisher | A (2026-11-15): root allowed for `*`, no Anthropic agent named; product path not checked. Fetch test 2026-11-07: blocked (no page fetched) | unknown | 2024 launch: 90-day refund or replacement. Re-check current terms. | medium (existence), low (terms) | [97] |
| Best Buy | https://www.bestbuy.com/ | direct retailer | Retail | B (2026-11-15): robots.txt unreadable (no answer). Fetch test 2026-11-07: partial (country landing only) | Products API, free key, 50,000 calls/day, 5/s; cache max 72 h; no use by third parties to analyse Best Buy pricing | Fits only apps offering Best Buy products; cross-retailer comparison is outside terms. PC-parts coverage unverified. | high (API), low (catalogue) | [78], [92], [144] |
| B&H Photo | https://www.bhphotovideo.com/ | direct retailer | Retail | A (2026-11-15): root allowed for `*`, no Anthropic agent named; product path not checked. Fetch test 2026-11-07: blocked (HTTP 403) | none found | Unverified. | low | [76] |
| Micro Center | https://www.microcenter.com/ | direct retailer | Retail | B (2026-11-15): robots.txt unreadable (HTTP 403). Fetch test 2026-11-07: blocked (HTTP 403) | none found | Store-only stock signals unverified. | low | [77] |
| Amazon US | https://www.amazon.com/ | marketplace (mixed) | Marketplace | browser (2026-11-15): robots.txt disallows Claude-User; browser fallback only, on the user's yes. Fetch test 2026-11-07: not tested (not fetched) | See Amazon note | Read seller per offer. | low | [96] |
| eBay US | https://www.ebay.com/ | marketplace (third-party seller; private and professional) | Marketplace | B (2026-11-15): terms of use bar bots and scrapers (eBay user agreement section 3, read on ebay.fr 2026-11-15). Fetch test 2026-11-07: blocked (HTTP 403) | Browse API, see eBay note | Existence from docs search, not live site. | medium (API), low (site) | [82], [93] |
| Back Market (US) | https://www.backmarket.com/en-us | professional refurbisher (marketplace of refurbishers) | Refurbisher | B (2026-11-15): terms of use (art. 4.5) bar scripts, robots and data extraction (read on backmarket.fr 2026-11-15). Fetch test 2026-11-07: not tested (rate limit) | none found | 12-month seller warranty per help center (search). Back Market Pro says it does not refurbish itself. PC-component coverage unverified. | medium | [84], [100] |
| Dell Outlet | https://www.dell.com/en-us/shop/outlet | manufacturer store | Outlet | A (2026-11-15): root allowed for `*`, no Anthropic agent named; product path not checked. Fetch test 2026-11-07: not tested (rate limit) | none found | Unverified. | low | [85] |
| Reddit r/hardwareswap | https://www.reddit.com/r/hardwareswap/ | private party | Classifieds | B (2026-11-15): robots.txt disallows `/` for `*`. Fetch test 2026-11-07: not tested (rate limit) | Reddit API exists (not checked) | Used review only. | low | [88] |
| Facebook Marketplace | https://www.facebook.com/marketplace/ | private party (mixed with businesses) | Classifieds | B (2026-11-15): robots.txt disallows claudebot and does not name Claude-User. Fetch test 2026-11-07: not tested (rate limit) | Not checked; likely unavailable to unauthenticated tools | Used review only. | low | [89] |

## Canada

| Name | URL | Seller type | Role | Access (tier and check date: `source-access-policy.md`; earlier fetch test 2026-11-07) | API/feed | Notes | Confidence | Source |
|---|---|---|---|---|---|---|---|---|
| Canada Computers & Electronics | https://www.canadacomputers.com/ | direct retailer | Retail | A (2026-11-15): root allowed for `*`, no Anthropic agent named; product path not checked. Fetch test 2026-11-07: yes (first 100k of 164k chars) | none found | CPUs, motherboards, GPUs; member-only prices; PC Builder tool; no marketplace mentioned. | high (type), medium (readability) | [80] |
| Memory Express | https://www.memoryexpress.com/ | direct retailer | Retail | B (2026-11-15): robots.txt disallows claudebot and does not name Claude-User. Fetch test 2026-11-07: blocked (HTTP 403) | none found | Unverified. | low | [79] |
| Newegg Canada | https://www.newegg.ca/ | marketplace (mixed) | Marketplace | A (2026-11-15): root allowed for `*`, no Anthropic agent named; product path not checked. Fetch test 2026-11-07: not tested (not fetched) | Seller API base URL exists (seller-side) | Unverified. | low | [94] |
| Amazon.ca | https://www.amazon.ca/ | marketplace (mixed) | Marketplace | browser (2026-11-15): robots.txt disallows Claude-User; browser fallback only, on the user's yes. Fetch test 2026-11-07: not tested (not fetched) | See Amazon note | Unverified. | low | [96] |
| Kijiji | https://www.kijiji.ca/ | private party (mixed with professionals) | Classifieds | B (2026-11-15): robots.txt unreadable (HTTP 403). Fetch test 2026-11-07: not tested (rate limit) | unknown | Used review only. | low | [86] |

## Australia

| Name | URL | Seller type | Role | Access (tier and check date: `source-access-policy.md`; earlier fetch test 2026-11-07) | API/feed | Notes | Confidence | Source |
|---|---|---|---|---|---|---|---|---|
| StaticICE | https://www.staticice.com.au/ | price comparator | Comparator | A (2026-11-15): root allowed for `*`, no Anthropic agent named; product path not checked. Fetch test 2026-11-07: partial (no product or price text on the homepage, 2026-11-08) | none found | Tracks "199 Australian stores" without naming them. No freshness indicator. Sister sites NZ, UK, US. | medium | [68] |
| PC Case Gear | https://www.pccasegear.com/ | direct retailer (prior knowledge) | Retail | B (2026-11-15): robots.txt unreadable (HTTP 403). Fetch test 2026-11-07: blocked (HTTP 403) | none found | Unverified. | low | [81] |
| Mwave | https://www.mwave.com.au/ | direct retailer (prior knowledge) | Retail | A (2026-11-15): root allowed for `*`, no Anthropic agent named; product path not checked. Fetch test 2026-11-07: not tested (rate limit) | unknown | Unverified. | low | — |
| Scorptec | https://www.scorptec.com.au/ | direct retailer (prior knowledge) | Retail | A (2026-11-15): root allowed for `*`, no Anthropic agent named; product path not checked. Fetch test 2026-11-07: not tested (rate limit) | unknown | Unverified. | low | — |
| Umart | https://www.umart.com.au/ | direct retailer (prior knowledge) | Retail | A (2026-11-15): root allowed for `*`, no Anthropic agent named; product path not checked. Fetch test 2026-11-07: not tested (rate limit) | unknown | Unverified. | low | — |
| Centre Com | https://www.centrecom.com.au/ | direct retailer (prior knowledge) | Retail | B (2026-11-15): robots.txt unreadable (HTTP 403). Fetch test 2026-11-07: not tested (rate limit) | unknown | Unverified. | low | — |
| Amazon AU | https://www.amazon.com.au/ | marketplace (mixed) | Marketplace | browser (2026-11-15): robots.txt disallows Claude-User; browser fallback only, on the user's yes. Fetch test 2026-11-07: not tested (not fetched) | See Amazon note | Unverified. | low | [96] |
| Gumtree AU | https://www.gumtree.com.au/ | private party | Classifieds | A (2026-11-15): root allowed for `*`, no Anthropic agent named; product path not checked. Fetch test 2026-11-07: not tested (not fetched) | unknown | Used review only. | low | — |

## Japan

Japanese retailer pages read show domestic delivery only or say nothing about overseas shipping: confirm on each retailer's 特定商取引法 page (not fetched) or use a proxy-buying service (see Cross-border).

| Name | URL | Seller type | Role | Access (tier and check date: `source-access-policy.md`; earlier fetch test 2026-11-07) | API/feed | Notes | Confidence | Source |
|---|---|---|---|---|---|---|---|---|
| Kakaku.com | https://kakaku.com/ | price comparator | Comparator | A (2026-11-15): root allowed for `*`, no Anthropic agent named; product path not checked. Fetch test 2026-11-07: yes (Japanese text garbled, structure readable) | RSS (news) only; 2006 product API, current status unknown | No merchant API found. Third-party scrapers exist (terms not reviewed). | high (site), low (API) | [105], [135] |
| Dospara | https://www.dospara.co.jp/ | direct retailer (also used sales and buyback) | Retail | A (2026-11-15): root allowed for `*`, no Anthropic agent named; product path not checked. Fetch test 2026-11-07: yes | none found | BTO PCs and parts; 中古販売 and 中古買取. Domestic only per page evidence. | high | [107] |
| PC工房 (Pc-koubou) | https://www.pc-koubou.jp/ | direct retailer | Retail | A (2026-11-15): root allowed for `*`, no Anthropic agent named; product path not checked. Fetch test 2026-11-07: yes | none found | Operated by Unitcom. 1-year standard warranty; 3/4-year optional. Overseas not mentioned. | high | [108] |
| Tsukumo | https://www.tsukumo.co.jp/ | direct retailer | Retail | B (2026-11-15): robots.txt unreadable (no answer). Fetch test 2026-11-07: blocked (socket hang up, 2 attempts) | none found | Retry later. | low | [106] |
| Ark | https://www.ark-pc.co.jp/ | direct retailer | Retail | B (2026-11-15): robots.txt unreadable (HTTP 403). Fetch test 2026-11-07: blocked (HTTP 403) | none found | Unverified. | low | [109] |
| Yodobashi | https://www.yodobashi.com/ | direct retailer | Retail | B (2026-11-15): robots.txt unreadable (no answer). Fetch test 2026-11-07: blocked (timeout, 2 attempts) | none found | Not read. | low | [110] |
| Bic Camera | https://www.biccamera.com/ | direct retailer | Retail | B (2026-11-15): robots.txt unreadable (no answer). Fetch test 2026-11-07: blocked (timeout, 2 attempts) | none found | Not read. | low | [111] |
| Sofmap | https://www.sofmap.com/ | direct retailer (plus used, Recole) | Retail | A (2026-11-15): root allowed for `*`, no Anthropic agent named; product path not checked. Fetch test 2026-11-07: yes | none found | PC-parts category; used goods and trade-in. Overseas not mentioned. | high | [112] |
| Janpara | https://www.janpara.co.jp/ | direct retailer | Retail | A (2026-11-15): root allowed for `*`, no Anthropic agent named; product path not checked. Fetch test 2026-11-07: yes (first 100k of 184k chars) | none found | Used-goods retailer (sales and buyback seen on the homepage, 2026-11-08), not confirmed as a refurbisher; grades A to D not seen. Shipping page linked, not read. | low | [116] |
| Amazon.co.jp | https://www.amazon.co.jp/ | marketplace (mixed) | Marketplace | browser (2026-11-15): robots.txt disallows Claude-User; browser fallback only, on the user's yes. Fetch test 2026-11-07: blocked (HTTP 403 then 503) | PA-API not checked; see Amazon note | Read seller per offer. | low | [113] |
| Mercari | https://jp.mercari.com/ | private party (plus Mercari Shops businesses) | Classifieds | A (2026-11-15): root allowed for `*`, no Anthropic agent named; product path not checked. Fetch test 2026-11-07: yes | none found (not searched) | Buyers abroad usually reach it via proxies. Used review only. | medium | [114] |
| Yahoo! Auctions | https://auctions.yahoo.co.jp/ | private party | Classifieds | B (2026-11-15): robots.txt unreadable (HTTP 403). Fetch test 2026-11-07: blocked (HTTP 403) | See Yahoo! Shopping API row (different service) | Not read. | low | [115] |
| Yahoo! Shopping Item Search v3 | https://developer.yahoo.co.jp/webapi/shopping/v3/itemsearch.html | API, not a shop | API | C (2026-11-15): official API with the user's own application ID; documentation page unreadable (HTTP 403). Fetch test 2026-11-07: blocked (HTTP 403; content from search snippet) | Free Client ID (Yahoo! JAPAN ID); keyword, JAN, genre, brand, store ID; JSON; about 1 query/s (snippet); credit notice required (third party) | v1 discontinued 2020-06-30. Guidelines must be accepted. | medium (existence), low (limits) | [129], [132], [151] |

## China (official brand stores, for buyers abroad)

Only official brand sites and brand-linked stores. Foreign-buyer warranty is not confirmed for any entry. Do not assume EU, US or UK shipping: no brand site read states shipping terms.

| Name | URL | Seller type | Role | Access (tier and check date: `source-access-policy.md`; earlier fetch test 2026-11-07) | API/feed | Notes | Confidence | Source |
|---|---|---|---|---|---|---|---|---|
| AliExpress (platform) | https://www.aliexpress.com/ | marketplace (third-party seller) | Marketplace | browser (2026-11-15): robots.txt disallows ClaudeBot; browser fallback only, on the user's yes. Fetch test 2026-11-07: no automated reading (robots.txt: `User-agent: ClaudeBot`, `Disallow: /`, read 2026-11-10): browser fallback only, on the user's yes; rules in `retailer-criteria.md` section 6 | Affiliate API: separate enrolment, signed calls, about 500 requests/day for new apps (third-party guides) | Not a brand store. Choice program and IOSS: see Not verified. | low | [102], [136], [153] |
| AliExpress Lian Li store | https://www.aliexpress.com/store/1101594887 | manufacturer store (linked from brand site) | Official store | browser (2026-11-15): robots.txt disallows ClaudeBot; browser fallback only, on the user's yes. Fetch test 2026-11-07: partial (empty body) | none found | Linked from the lian-li.com Support menu, so the brand declares it. Badge not seen. | medium (link), low (badge) | [103], [123] |
| Thermalright | https://www.thermalright.com/ | manufacturer store | Brand site | A (2026-11-15): root allowed for `*`, no Anthropic agent named; product path not checked. Fetch test 2026-11-07: yes | none found | 5-year warranty on some models; sales through "Find Distributors"; no AliExpress, Amazon or JD link. Newegg "Thermalright Authorized Store" seen in search only. | high (site), low (China store) | [119], [131] |
| Lexar | https://www.lexar.com/ | manufacturer store | Brand site | A (2026-11-15): no robots.txt (HTTP 404). Fetch test 2026-11-07: yes (FR locale served) | none found | Store link "Où acheter"; no AliExpress or JD link. Warranty page linked, not read. China store not fetched. | medium (brand), low (China store) | [120] |
| Asgard (阿斯加特) | https://www.asgard.com.cn/ | manufacturer store | Brand site | A (2026-11-15): root allowed for `*`, no Anthropic agent named; product path not checked. Fetch test 2026-11-07: yes | none found | RAM and SSDs; no e-commerce link; English site asgardoc.com linked. Warranty and foreign-buyer terms absent. | high (site), low (store) | [126] |
| Montech | https://www.montech.com/ | manufacturer store | Brand site (Swiss AG) | A (2026-11-15): root allowed for `*`, no Anthropic agent named; product path not checked. Fetch test 2026-11-07: yes | none found | Official shop montech.com/ch (Switzerland); regional /us/en. China store unverified. montechworld.com: DNS error. | medium | [121], [122] |
| Fanxiang | https://www.fanxiang.com/ | manufacturer store (claimed) | Brand site | B (2026-11-15): robots.txt unreadable (HTML page instead). Fetch test 2026-11-07: partial (minimal text) | none found | Official status not confirmed. | low | [124] |
| SAMA | https://www.sama.com.cn/ | manufacturer store (unverified) | Brand site | B (2026-11-15): robots.txt unreadable (no answer). Fetch test 2026-11-07: blocked (TLS certificate mismatch) | none found | Not bypassed. | low | [125] |
| MSI | https://www.msi.com/ | manufacturer store | Brand site | B (2026-11-15): robots.txt unreadable (HTTP 403). Fetch test 2026-11-07: blocked (HTTP 403) | none found | msi.com.cn not tested. | low | [127] |
| ASUS China | https://www.asus.com.cn/ | manufacturer store | Brand site | A (2026-11-15): no robots.txt (HTTP 404). Fetch test 2026-11-07: partial (title only) | none found | Title: 华硕电脑官方直营平台; China only per title; links unconfirmed. | low | [128] |
| JD Worldwide | https://global.jd.com/ | marketplace (third-party seller) | Cross-border marketplace | B (2026-11-15): robots.txt unreadable (HTML page instead). Fetch test 2026-11-07: yes | none found | Title 京东全球版; mainland operator in footer. No official-store badge text; shipping countries not stated. | medium (identity), low (shipping) | [117] |
| Tmall Global | https://global.tmall.com/ | marketplace (third-party seller) | Cross-border marketplace | A (2026-11-15): no robots.txt (HTTP 404). Fetch test 2026-11-07: blocked (HTTP 404) | none found | Unverified. | low | [118] |

## Cross-border

Zones in this table are the only ones research supports. For any other pair, read the seller's own shipping page and record it; do not infer.

| Zone / pair | What research supports | Confidence | Source |
|---|---|---|---|
| Belgium and Netherlands | bol.com has a partner platform for NL and BE sellers. Coolblue runs .nl and .be sites. Back Market runs .be and .nl on the same platform as FR. | medium | [11], [15], [27] |
| France, Spain | LDLC has a Spanish storefront (ldlc.com/es-es). | medium | [45] |
| Back Market | One platform sold in 16 countries (search). Seller ratings and warranty differ per refurbisher: read per offer. | medium | [11] |
| Montech | Official shop is Swiss (montech.com/ch). Shipping to other countries not stated. | medium | [122] |
| Japan retailers | Pages read show domestic delivery or no overseas mention. | high | [107], [108], [112] |
| Australia, NZ, UK, US | StaticICE lists sister sites for NZ, UK and US. No shipping claim. | low | [68] |
| Other pairs (e.g. Luxembourg, Germany, Spain, Italy, Canada) | Not established by research. | n/a | n/a |

**Proxy-buying services (Japan).** Seller type `proxy-buying service`, distinct from the retailer behind it. Add their fee and international forwarding to the landed price. Fees below are from blogs and conflict: record them as `low`.

| Name | URL | Fees claimed | Confidence | Source |
|---|---|---|---|---|
| Buyee | https://japanlanded.pages.dev/articles/buyee-vs-zenmarket/ | 500 JPY per order (one source, per order from April 2026) vs 300-500 JPY plus 5-10% (another); official Mercari partner per one blog | low | [137] |
| ZenMarket | same page | 800 JPY per item on Mercari and Yahoo! Auctions (one source) | low | [137] |
| OneMall | https://blog.onemall.jp/?p=2107 | 3% of winning bid on Yahoo! Auctions, min 200 JPY, max 300 JPY (blog claim) | low | [137] |

**Marketplace listings are typed per seller.** On Amazon, eBay, Newegg, bol.com, Rue du Commerce, LDLC, AliExpress, JD Worldwide and refurbished marketplaces, read the seller of each offer and fill `marketplace (first-party)` or `marketplace (third-party seller)` or `professional refurbisher`. A site-level label is not enough.

**eBay note.** Browse API: free tier 5,000 calls/day, OAuth application token, one category ID per request; production Buy API access is gated; eBay content display rules apply; confidence medium [93], [138]-[140]. Marketplace Insights (sold data) is limited release, not self-serve [139].

**Amazon note.** Pages are read only through the browser fallback, on the user's yes (`research-method.md` section 7, maintainer exception). PA-API 5.0 is deprecated (calls return HTTP 403). Its successor, the Creators API, needs Amazon Associates enrolment and 10 or more qualifying sales in 30 days [141], [142]. A secondary source gives 3 sales instead of 10 [96]. Do not assume access. Keepa has a paid API with a token bucket; plan prices are unverified [143].

## When a site is blocked

1. Record the page as `blocked (<reason>)` in the price row, with the HTTP code or error seen.
2. Do not circumvent: no alternate user agents, no caches, mirrors or archive copies used to dodge a block. Do not use unofficial endpoints or third-party scrapers.
3. Do not fetch sites whose robots.txt disallows Claude user agents (PCPartPicker, TechPowerUp) [145].
4. Do not loop. One fetch attempt per page per answer; a browser read on the user's yes is a separate step. A rate-limited page is `not tested`: try it once, then record the result.
5. Offer the browser fallback in one line, as defined in `research-method.md` section 7 (interactive answers only, read-only, stop at any bot check, never for sites whose robots rules or terms exclude automated collection, Amazon and AliExpress excepted). If the user says yes, read the page there and record `Page read: browser (user session)`.
6. Otherwise ask the user for a screenshot or pasted text of the page. Record `Page read: user screenshot`, `Confidence: medium` at best.
7. Prefer another retailer in the same country that is `yes` or `partial`, and say which retailers could not be read.

## Not verified

- Electronic-Shop Sarl (direct retailer): no URL recorded, so no access tier. Niederanven; directories only, no catalogue seen. Source [32].
- PayPay Flea Market (private party): no URL recorded, so no access tier. Listed in the brief only. Source —.
- Rakuten Ichiba Item Search (API, not a shop): no URL recorded, so no access tier. Rate and result caps conflict across sources. Source [133], [150].
- Peerless Assassin (Thermalright line) (manufacturer store): no URL recorded, so no access tier. Search found only third-party sellers. Official AliExpress store NOT confirmed. Source [131].
- Kingbank (manufacturer store (claimed on AliExpress)): no URL recorded, so no access tier. A review cites the "KingBank official AliExpress store"; one anecdote of warranty problems. Store page not located. Source [130].
- **Comparators blocked or unread:** idealo (FR, DE, ES, IT), Tweakers Pricewatch, Geizhals, Billiger, Trovaprezzi, PCPartPicker (global and UK), Google Shopping. Freshness, seller display and marketplace mixing unknown. Kelkoo.es not tested.
- **Retailers blocked or unreadable:** Mindfactory, Caseking, Cyberport, Notebooksbilliger, Computeruniverse, Coolmod, Coolblue (NL), Scan, CCL Online, Newegg, B&H, Micro Center, Memory Express, PC Case Gear, Ark, Tsukumo, Yodobashi, Bic Camera, Amazon (DE, JP), Yahoo! Auctions, eBay (US), MSI, SAMA, Tmall Global.
- **Not tested (rate limit):** alternate.be, megekko.nl, azerty.nl, informatique.be, bol.com, pricespy.fr, Ebuyer, Amazon UK, Back Market (DE, ES, IT, US), Dell Outlet, Kijiji, Gumtree, Reddit, Facebook Marketplace, Subito, Mwave, Scorptec, Umart, Centre Com. Rows for Australian and several UK/US retailers rest on prior knowledge.
- **Search-only, no page read:** Back Market (FR, BE, NL), Leboncoin, Marktplaats, 2dehands.be, Hardware.info, Beslist.be, Bstore.be, Alternate NL/BE, Shop24.lu, Linsys, Obiwan, Messoanuovo, PcComponentes refurbished tiers. Not searched: PCPartPicker CA and AU, Back Market UK seller pages, eBay UK and AU Browse coverage, Tweakers.be (dropped, no URL or source).
- **Luxembourg:** no comparator, no classifieds, no verified catalogue. Marktplaats and 2dehands are not verified for Luxembourg.
- **Official-store badges:** none confirmed live (AliExpress store pages returned empty bodies). Peerless Assassin, Kingbank, Fanxiang and Asgard store status unconfirmed. JD Worldwide badges and shipping countries unconfirmed.
- **Foreign-buyer warranty:** unconfirmed for every China brand and every Japanese retailer. Japanese overseas shipping policy not read.
- **Conflicting secondary sources:** EU duty changes for 1 July 2026 (end of the 150 EUR exemption, 3 EUR per-item duty) and AliExpress Choice and IOSS handling disagree on who collects duty. Do not rely on this file: read `${CLAUDE_PLUGIN_ROOT}/references/international-buying.md` and check EU Commission customs pages.
- **Other conflicts:** Amazon Creators API sales threshold (3 vs 10); Rakuten limits and access key; proxy fees; Keepa token costs.
- **Freshness:** no page showed a price date. Prices seen on 2026-11-07 are "as seen" only.
- **Terms of service:** none reviewed for automated access, except PCPartPicker, Best Buy and eBay terms in the rows above. Check terms and robots.txt before any systematic reading.
- **Operator and trust data:** Trustpilot scores and seller counts come from secondary aggregators and are low confidence.

## Sources

All accessed 2026-11-07. Fetched pages are the entry URL unless noted; "search" means a search-result snippet; "(403)" and similar are fetch results.

France and Benelux
1. ledenicheur.fr (fetched)
2. ledenicheur.fr (merchant listing text; merged into 1)
3. idealo.fr (fetch error)
4. mergado.com/tag/idealo ; pricefy.io/feed-channels/idealo (search)
5. materiel.net/recherche/DDR5%206000%2032GB
6. ldlc.com ; ldlc.com/recherche/DDR5+6000+32GB/ (error page)
7. topachat.com/pages/recherche.php?ssearch=DDR5+6000+32GB
8. cybertek.fr
9. grosbill.com
10. rueducommerce.fr
11. backmarket.co.uk/en-gb/s/smartselling/a07d1294-a0ea-4c55-a46c-8b1436a01e08 ; backmarket.co.uk/en-gb/r/s/les-reconditionnes/1fa7b9b0-a90c-46e7-af7b-d21c51541de5 (search)
12. leboncoin.fr/ck/ordinateurs/composant-informatique/p-2 (search)
13. beyondgaming.be/archive/bs-hardware.195/i5-4460-gtx750ti-z97k-mx259h.1078795 (search)
14. cheeseweb.eu/2010/03/computer-shopping-belgium (search, 2010)
15. coolblue.be/en/computers-tablets/experience-in-the-store-in-brussels/coolblues-choice (search) ; coolblue.nl (403)
16. hardware.info (search, not fetched)
17. beslist.be (search, not fetched)
18. bstore.be/amazon/computer/ (search)
19. ebayinc.com/stories/news/ebay-inc-acquires-leading-belgian-online-classifieds-sites-2dehandsbe-and/ (search, undated)
20. apify.com/studio-amba/2dehands-scraper (search; scraper vendor, not used)
21. github.com/tychobrouwer/tweakers-pricewatch (search; unofficial, not used)
22. pricetweakers.net/product-feed-requirements/ ; koongo.com/tweakers.html (search)
23. kieskeurig.nl
24. nl.trustpilot.com/review/azerty.nl ; gridinsoft.com/online-virus-scanner/url/alternate-nl (search)
25. nl.trustpilot.com/review/azerty.nl (search)
26. gridinsoft.com/online-virus-scanner/url/megekko-nl (search; automated scan)
27. partnerplatform.bol.com/en/cdp/selling-via-bol-as-nlbe-partner ; emerce.nl/nieuws/bolcom-populairste-marktplaats-amazon-duurste (search)
28. cowcotland.com/topic8702.html ; zunapro.com/netherlands/en/blog/dutch-marketplaces-best-platforms-selling-online (search)
29. shop24.lu/en/?p=265463 (search)
30. letzshop.lu/en/vendors/linsys (search)
31. vymaps.com/LU/Obiwan-Computers-Shop-78286/ (search; 2018 review)
32. europeanjobdays.eu/en/node/81975 (search)

Germany, Spain, Italy
33. geizhals.de/?fs=DDR5+6000+32GB (403)
34. idealo.de/preisvergleich/MainSearchProductCategory.html?q=DDR5+6000+32GB (fetch error)
35. billiger.de (403)
36. mindfactory.de/search_result.php?search=DDR5+6000+32GB (403)
37. alternate.de/html/search.html?query=DDR5+6000+32GB (partial)
38. caseking.de (403)
39. cyberport.de (fetch error)
40. notebooksbilliger.de/produkte/suche?q=DDR5+6000+32GB (403)
41. computeruniverse.net/de/search?q=DDR5+6000+32GB (fetch error)
42. amazon.de/s?k=DDR5+6000+32GB (503)
43. kleinanzeigen.de/s-pc-komponenten/k0
44. refurbed.de (partial)
45. ldlc.com/es-es/ (partial)
46. pccomponentes.es/buscar/?query=DDR5+6000+32GB (301 to pccomponentes.com, not followed)
47. coolmod.com/buscar?q=DDR5+6000+32GB (too many redirects)
48. kelkoo.es (rate limit)
49. amazon.es/s?k=DDR5+6000+32GB (unverified)
50. es.wallapop.com (partial)
51. idealo.es (fetch error)
52. trovaprezzi.it (403)
53. idealo.it (fetch error)
54. eprice.it
55. yeppon.it (unverified)
56. amazon.it/s?k=DDR5+6000+32GB (unverified)
57. subito.it/annunci-italia/vendita/informatica/ (rate limit)
58. drako.it
59. backmarket.it ; backmarket.de ; backmarket.es (rate limit)
60. readme.priceapi.com/reference/geizhals-1 ; xcrawl.com/de/solutions/geizhalsde-price-comparison-scraper-api (search; third-party scrapers)
61. apps.shopify.com/geizhals-sync?locale=de (search; third-party feed app)
62. refurb.me/it/refurbishers ; roxmir.it/guide/computer-ricondizionati-guida-completa-2025/ (search snippets; secondary)
63. help.productsup.com/en/29544-30186-add-idealo-partner-api-v2-0-export.html ; mergado.com/integration/idealo-csv.md (search; verify on import.idealo.com)

UK, US, Canada, Australia
64. pcpartpicker.com (403)
65. uk.pcpartpicker.com (403)
66. pcpartpicker.com/api/ (403)
67. pricespy.co.uk
68. staticice.com.au
69. google.com/shopping (browser notice)
70. camelcamelcamel.com (403)
71. keepa.com (title only)
72. scan.co.uk (403)
73. overclockers.co.uk
74. cclonline.com (403)
75. newegg.com (403)
76. bhphotovideo.com (403)
77. microcenter.com (403)
78. bestbuy.com (country page)
79. memoryexpress.com (403)
80. canadacomputers.com
81. pccasegear.com (403)
82. ebay.com (403)
83. amazon.co.uk (rate limit)
84. backmarket.com/en-us (rate limit)
85. dell.com/en-us/shop/outlet (rate limit)
86. kijiji.ca (rate limit)
87. gumtree.com (rate limit)
88. reddit.com/r/hardwareswap/ (rate limit)
89. facebook.com/marketplace/ (rate limit)
90. ebuyer.com (rate limit)
91. github.com/cyruscuenca/PCPartPicker-API/blob/master/README.rst (search; unofficial)
92. developer.bestbuy.com/apis ; bestbuyapis.github.io/api-documentation/#products-api (search)
93. developer.ebay.com/api-docs/buy/browse/resources/item_summary/methods/search (search)
94. developer.newegg.com/?p=3794 ; feedonomics.com/supported-channels/newegg-feed-specs/ (search)
95. keepa.com/api-docs/ (search)
96. webservices.amazon.com/paapi5/documentation/register-for-pa-api.html ; affiliate-program.amazon.co.uk/help/node/topic/GVJ2BJP35457CLML (search) ; keywordrush.com/blog/amazon-pa-api-associatenoteligible-error-is-there-a-new-10-sales-rule (secondary)
97. businesswire.com/news/home/20240125666246/en/Newegg-Debuts-Newegg-Refreshed-Program-to-Offer-Quality-Resale-Products-at-Low-Prices (search)
98. ui.awin.com/merchant-profile/15473 ; scan.co.uk/affiliate-program (search)
99. overclockers.co.uk/affiliate-program ; ui.awin.com/merchant-profile/28821 (search)
100. help.backmarket.com/hc/en-gb/articles/360021395800-Refurbished-in-the-UK-resold-in-the-UK ; backmarket-business.gorgias.help/en-US/does-back-market-pro-refurbish-products-4642374 (search)
101. apify.com/parseforge/pcpartpicker-component-scraper (search; third-party scraper, not used)

Japan and China
102. aliexpress.com (empty body)
103. aliexpress.com/store/1101594887 (empty body)
104. aliexpress.com/help/help_center.html (302 to maintenance page, not followed)
105. kakaku.com
106. tsukumo.co.jp (socket hang up x2)
107. dospara.co.jp
108. pc-koubou.jp
109. ark-pc.co.jp (403)
110. yodobashi.com (timeout x2)
111. biccamera.com (timeout x2)
112. sofmap.com
113. amazon.co.jp (403, 503)
114. jp.mercari.com
115. auctions.yahoo.co.jp (403)
116. janpara.co.jp (partial)
117. global.jd.com
118. global.tmall.com (404)
119. thermalright.com
120. lexar.com (FR locale)
121. montechworld.com (DNS error)
122. montech.com
123. lian-li.com
124. fanxiang.com (minimal)
125. sama.com.cn (TLS mismatch)
126. asgard.com.cn
127. msi.com (403)
128. asus.com.cn (title only)
129. developer.yahoo.co.jp/webapi/shopping/v3/itemsearch.html (403; snippet)
130. search "Kingbank official store AliExpress" (incl. newegg.com/kingbank-32gb-ddr5-6400-cas-latency-cl32-memory-white/p/0RN-012W-00028)
131. search "Peerless Assassin official store AliExpress Thermalright" (incl. newegg.com/global/il-en/Seller-Store/Thermalright-Authorized-Store ; buywisely.com.au)
132. search "Yahoo! Shopping API developer" (developer.yahoo.co.jp/webapi/shopping/v3/)
133. search "Rakuten Web Service API ichiba" (rubydoc.info/gems/rakuten_web_service/1.4.0 ; apify.com/fruitful_quintessence/rakuten-japan-mcp; third-party)
134. search "AliExpress Affiliate API" (rapidevelopers.com/replit-integration/aliexpress-api; vendor guide)
135. search "kakaku.com API" (webtan.impress.co.jp/node/267 ; metacpan.org/pod/WebService::KakakuCom)
136. search "AliExpress Choice IOSS VAT EU 2026" (yakkyofy.com/aliexpress-import-tax-what-to-do/ ; easproject.com/ioss-registration-1-july-3-euro-duty/)
137. search "Japan proxy buying service fees" (japanlanded.pages.dev/articles/buyee-vs-zenmarket/ ; blog.onemall.jp/?p=2107)

APIs and constraints (research note r2)
138. developer.ebay.com/api-docs/buy/browse/overview.html (403)
139. developer.ebay.com/api-docs/buy/marketplace-insights/overview.html ; edp.ebay.com/api-docs/buy/marketplace-insights/static/overview.html
140. developer.ebay.com/develop/apis/api-license-agreement (search)
141. affiliate-program.amazon.com/creatorsapi/docs/en-us/paapiv5-deprecation
142. affiliate-program.amazon.com/creatorsapi/docs/en-us/introduction
143. keepa.com/api-docs/plans-tokens.html
144. developer.bestbuy.com/legal
145. pcpartpicker.com/robots.txt ; techpowerup.com/robots.txt
146. be.pcpartpicker.com/tos (search)
147. idealo.github.io/partner-web-service/docs/v2 (search)
148. ce-docs.keywordrush.com/modules/affiliate/geizhalsde-module (third party)
149. docs.kelkoogroup.com/for-publishers
150. webservice.rakuten.co.jp/en/ (blocked; search only)
151. developer.yahoo.co.jp/webapi/shopping/v3/itemsearch.html (search)
152. developer.newegg.com/newegg_marketplace_api (search)
153. developers.aliexpress.com (via third-party guides, e.g. zuplo.com/learning-center/aliexpress-api-guide.md)
154. Materiel.net Marketplace terms (CGU) and referencing criteria, PDFs supplied by the maintainer, dated 2023-09-01, from the footer "Marketplace" section; not fetched by research
155. alternate.fr homepage and product page 100063948 (Patriot PVV532G600C30K), read 2026-11-08: no marketplace wording, no seller line, "frais d'expédition en sus à partir de 9,90 €"
156. pccomponentes.fr product pages read in the maintainer's Cowork tests, 2026-11-11 (Ryzen 7 9800X3D sold and shipped by PcComponentes; AORUS RTX 5080 sold by the third-party seller Leasi-fr)
157. joybuy.fr product pages 101833183, 101811052 and 10353554 (RTX 5080), maintainer's Cowork test 2026-11-15: Risk Control page to automated reading, image captcha in the browser
