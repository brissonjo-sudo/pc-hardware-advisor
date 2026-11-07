# R1 Retailers: France and Benelux
Collected: 2026-11-07 · Model: haiku · Method: WebFetch on homepages and search URLs where allowed; WebSearch for APIs, feeds, marketplaces and gaps. Several domains were rate-limited or blocked (see Not verified). Every row is either a fetch on 2026-11-07 or a search-result claim, and the Confidence column says which.

Legend. Auto-readable: yes = prices/names in HTML text in the fetch; partial = page returned an error or wrong page, or content was incomplete; blocked = HTTP 403 or fetch error; not tested = WebFetch rate-limited, no fetch made. Type: DR = direct retailer, MP = marketplace, REF = professional refurbisher, CLS = private-party classifieds, CMP = price comparator, MFR = manufacturer store.

## France

| Name | URL | Type | Role | Auto-readable | API/feed | Notes (reputation, shows seller, freshness) | Confidence | Source |
|---|---|---|---|---|---|---|---|---|
| leDénicheur | https://www.ledenicheur.fr/ | CMP | Price comparator | yes | none found | Shows merchant name per offer (Amazon.fr, Cdiscount, Rue du Commerce, eBay, Carrefour among others) and a "Dès" price in EUR. Mixes marketplace sellers in. Price freshness not stated on the page. | medium (fetched homepage only; product page not read) | [1], [2] |
| idealo.fr | https://www.idealo.fr/ | CMP | Price comparator (candidate) | blocked (fetch error "unable to fetch", cause not stated by tool) | merchant feed/import API exists for idealo Business (CSV/TXT/XML; import.idealo.com/docs per third-party source). Affiliate feed for FR not confirmed. | Could not read the site. Feed info from third-party sources only. Verify on idealo's own business pages. | low | [3], [4] |
| Materiel.net | https://www.materiel.net/recherche/DDR5%206000%2032GB | DR | Direct retailer | yes (prices in HTML) | none found | Search returned 5 DDR5 6000 32GB products with prices in EUR, including two "Occasion" (used) items, so it sells used parts too. Own stock vs marketplace not confirmed. | medium | [5] |
| LDLC | https://www.ldlc.com/ | DR + MP | Direct retailer, with marketplace | partial (homepage yes; search URL returned an error page "Une erreur est survenue" with 0 results) | none found | Homepage states a catalogue of 25,000+ references from major brands, and footer links "Vendez sur LDLC" and "Marketplace". Categories CPU/GPU/RAM visible. Retry search later. | medium | [6] |
| TopAchat | https://www.topachat.com/ | DR | Direct retailer | partial (search URL returned a promotional PC-builds page, 4 products with prices; not a search result list) | none found | Use the homepage/category URLs instead of the search URL. Own stock vs marketplace not checked. | low | [7] |
| Cybertek | https://www.cybertek.fr/ | DR | Direct retailer (own assembly) | yes (text read) | none found | States "Vous voyez le stock de Cybertek", shop locations (Paris, Lyon, Marseille, Bordeaux), CPU/GPU/RAM/SSD categories and a configurator. No marketplace language found. | high (primary page read) | [8] |
| GrosBill | https://www.grosbill.com/ | DR | Direct retailer | yes (text read) | none found | States "Vous voyez le stock de GrosBill", 10 shops in France, component categories (processors, GPUs, RAM, motherboards, PSUs, SSD) visible. No third-party seller mention. | high (primary page read) | [9] |
| Rue du Commerce | https://www.rueducommerce.fr/ | DR + MP | Retailer and marketplace | yes (text read) | none found | Footer links "Vendez sur RDC" and "CGU Marketplace". Free shipping applies to products "vendus et expédiés par Rue du Commerce", implying third-party items. Marketplace role inferred from terms and links, not explicit in listings. | high for the marketplace role (links and terms read); medium for the split | [10] |
| Back Market (FR) | https://www.backmarket.fr/ | REF (aggregator MP) | Marketplace of professional refurbishers | not tested (search only) | none found | Paris-based marketplace for refurbished electronics. Sellers are professional refurbishers, not private individuals. Public seller ratings exist (one seller page: 4/5 from 756 reviews). Marketing claims (1-year warranty, 30-day returns) to be checked on the site. | medium (search results; no direct page read) | [11] |
| Leboncoin (computer components) | https://www.leboncoin.fr/ck/ordinateurs/composant-informatique/p-2 | CLS | Private-party classifieds | not tested (URL seen in search results only) | none found | Components section listed with 717 used listings at indexing time. Private-to-private; condition and fraud risk to be stated in the plugin. | medium (search result listing; freshness unknown) | [12] |

## Belgium

| Name | URL | Type | Role | Auto-readable | API/feed | Notes (reputation, shows seller, freshness) | Confidence | Source |
|---|---|---|---|---|---|---|---|---|
| Alternate (BE) | https://www.alternate.be/ | DR | Direct retailer (candidate) | not tested (rate-limited) | none found | Forum threads describe it as popular in Belgium, but these threads are old. Own stock vs marketplace not checked. | low | [13] |
| Vandenborre | https://www.vandenborre.be/ | DR | Direct retailer (candidate) | not tested | none found | Mentioned in a 2010 blog as good for brand names and service. Too old to rely on. | low | [14] |
| Coolblue (BE) | https://www.coolblue.be/ | DR | Direct retailer (candidate) | not tested | none found | The NL site returned 403, so the BE site is not verified. Coolblue runs a selective partner programme (search result), not an open marketplace. | low | [15] |
| Informatique.be | https://www.informatique.be/ | DR | Direct retailer (candidate) | not tested (rate-limited) | none found | Listed as candidate only; not verified. | low | — |
| Hardware.info | https://www.hardware.info/ | CMP | Price comparator (candidate) | not tested | none found | Described by a marketing source as a leading Belgian hardware comparison channel. Not fetched. | low | [16] |
| Beslist.be | https://www.beslist.be/ | CMP | Price comparator (candidate) | not tested | none found | Described as a Belgian shopping and comparison platform. Not fetched. | low | [17] |
| Bstore.be | https://bstore.be/ | CMP | Price comparator (candidate) | not tested | none found | Compares computer prices across Amazon, Bol, Coolblue, Krëfel and Vanden Borre. Not fetched. | low | [18] |
| 2dehands.be | https://www.2dehands.be/ | CLS | Private-party classifieds | not tested (search only) | none found by search; third-party scrapers exist on Apify (not used) | Belgian sister site of Marktplaats, acquired by eBay. PC-parts section not confirmed. Announcement undated. | medium (search results) | [19], [20] |
| Back Market (BE) | https://www.backmarket.be/ | REF (aggregator MP) | Marketplace of professional refurbishers | not tested | none found | Same platform as FR/NL; sold in 16 countries (search). | medium (search only) | [11] |
| Tweakers.be | — | CMP | Price comparator (candidate) | not verified | — | Not verified in this research. | low | — |

## Netherlands

| Name | URL | Type | Role | Auto-readable | API/feed | Notes (reputation, shows seller, freshness) | Confidence | Source |
|---|---|---|---|---|---|---|---|---|
| Tweakers Pricewatch | https://tweakers.net/pricewatch/ | CMP | Price comparator | blocked (fetch error "unable to fetch", cause not stated by tool) | No official public API found. Merchant feed via a Pricewatch merchant arrangement (search). An unofficial, undocumented price-history endpoint exists on GitHub; do not use it. Scraping may breach terms. | Could not read the site. Shows shop per price (from search only). Pricewatch refresh cycle reported as four times an hour (vendor claim). | low (secondary sources only) | [21], [22] |
| Kieskeurig | https://www.kieskeurig.nl/ | CMP | Price comparator | yes (text read; server-side vs JS rendering unknown) | none found | Lists shops per product ("from" price plus "+X andere aanbieders"). Says it tracks 616 affiliated webshops. Not a marketplace. Date of prices not shown. | high for listing shape; medium for price HTML | [23] |
| Alternate (NL) | https://www.alternate.nl/ | DR | Direct retailer | not tested | none found | Trustpilot 4.1 from 24,754 reviews (automated scan site; not verified on Trustpilot). Older forum threads recommend it. | low | [24] |
| Azerty.nl | https://www.azerty.nl/ | DR | Direct retailer | not tested (rate-limited) | none found | Trustpilot TrustScore 3.5 from about 8,000 reviews (search result). Recent complaints about stock status and service. Also does custom PC assembly. | low | [25] |
| Megekko | https://www.megekko.nl/ | DR | Direct retailer | not tested (rate-limited) | none found | No meaningful customer review data found. Only an automated scan result (trust 100/100 from an automated checker, which is not evidence of service quality). | low | [26] |
| Coolblue (NL) | https://www.coolblue.nl/ | DR | Direct retailer | blocked (HTTP 403) | none found | Not retried. Runs a selective partner programme, not an open marketplace (search). | low | [15] |
| bol.com | https://www.bol.com/nl/nl/ | MP (plus DR) | Retailer and marketplace | not tested (rate-limited) | Bol partner platform (search: partnerplatform.bol.com) | Opened to third-party sellers in 2016. Curated assortment; not every category is open to new partners. Seller counts vary by source (about 20,000 older, 52,000+ newer). | medium (search results on the marketplace role) | [27] |
| Back Market (NL) | https://www.backmarket.nl/ | REF (aggregator MP) | Marketplace of professional refurbishers | not tested | none found | Same platform as FR/BE. | medium (search only) | [11] |
| Marktplaats | https://www.marktplaats.nl/ | CLS | Private-party classifieds | not tested (search only) | none found | Most ads are placed by private individuals. Scam-prone (per a search source). Non-binding classified listings. | medium (search results) | [28] |

## Luxembourg

| Name | URL | Type | Role | Auto-readable | API/feed | Notes (reputation, shows seller, freshness) | Confidence | Source |
|---|---|---|---|---|---|---|---|---|
| Shop24.lu (eConcept Sàrl-S) | https://shop24.lu/ | DR | Direct retailer (Wormeldange; TERRA distributor) | not tested | none found | Only direct online shop with a clear product range in the search results. Not verified. | low | [29] |
| Linsys (letzshop.lu) | https://letzshop.lu/en/vendors/linsys | DR (on a marketplace) | Vendor on the Letzshop marketplace | not tested | none found | Lists PCs, laptops, spare parts and components; claims immediate stock. Letzshop is itself a marketplace. | low | [30] |
| Obiwan Computers | https://obiwan.lu/ | DR (physical) | Local electronics shop, Rue de Beggen | not tested | none found | Website mentioned in directory. Only review found is from 2018 and negative about service, so may be outdated. | low | [31] |
| Electronic-Shop Sarl | — | DR | E-commerce electronics trading (Niederanven) | not tested | none found | Found in directories only; no catalogue seen. | low | [32] |

## Not verified / gaps

- **Blocked (3):** idealo.fr (fetch error on WebFetch; cause unknown), tweakers.net (fetch error), coolblue.nl (HTTP 403). Not retried or bypassed.
- **Not tested because of the domain rate-limit (6):** alternate.be, megekko.nl, azerty.nl, informatique.be, bol.com, pricespy.fr. Retry in a later session. Do not loop. Pricespy FR coverage is unknown; no claim made.
- **Search-only (no page read):** Back Market (all three countries), Leboncoin, Marktplaats, 2dehands.be, Hardware.info, Beslist.be, Bstore.be, Alternate NL/BE, Azerty.nl review score, Shop24.lu, Linsys, Obiwan.
- **Freshness:** no page showed a price date. Prices seen on 2026-11-07 are "as seen" only. The plugin needs a per-row price timestamp strategy.
- **Luxembourg:** no PC comparator or classifieds found. Marktplaats/2dehands are not verified for Luxembourg.
- **Tweakers.be:** not verified.
- **API/feeds:** no public API found for any retailer. Only confirmed route is an idealo Business merchant feed (third-party source, medium at best). Tweakers Pricewatch needs a merchant arrangement with Tweakers. The undocumented Tweakers endpoint must not be used. PriceTweakers (pricetweakers.net) is a separate company; not evaluated.
- **Rate-limit note:** WebFetch returned rate-limit errors for six domains after about 20 calls on this network.
- **Search-result claims** on Trustpilot scores and seller counts come from secondary aggregators. Treat as low confidence.

## Sources

1. https://www.ledenicheur.fr/ (fetched 2026-11-07)
2. https://www.ledenicheur.fr/ (same page, merchant listing text)
3. https://www.idealo.fr/ (fetch error 2026-11-07)
4. https://www.mergado.com/tag/idealo ; https://www.pricefy.io/feed-channels/idealo (search 2026-11-07)
5. https://www.materiel.net/recherche/DDR5%206000%2032GB (fetched 2026-11-07)
6. https://www.ldlc.com/ (fetched 2026-11-07); https://www.ldlc.com/recherche/DDR5+6000+32GB/ (error page, 2026-11-07)
7. https://www.topachat.com/pages/recherche.php?ssearch=DDR5+6000+32GB (fetched 2026-11-07; promotional page returned)
8. https://www.cybertek.fr/ (fetched 2026-11-07)
9. https://www.grosbill.com/ (fetched 2026-11-07)
10. https://www.rueducommerce.fr/ (fetched 2026-11-07)
11. https://www.backmarket.co.uk/en-gb/s/smartselling/a07d1294-a0ea-4c55-a46c-8b1436a01e08 ; https://www.backmarket.co.uk/en-gb/r/s/les-reconditionnes/1fa7b9b0-a90c-46e7-af7b-d21c51541de5 (search 2026-11-07; claims from search snippets)
12. https://www.leboncoin.fr/ck/ordinateurs/composant-informatique/p-2 (search result 2026-11-07)
13. https://www.beyondgaming.be/archive/bs-hardware.195/i5-4460-gtx750ti-z97k-mx259h.1078795 (search 2026-11-07; forum thread referenced Alternate)
14. https://cheeseweb.eu/2010/03/computer-shopping-belgium (search 2026-11-07; 2010, old)
15. https://www.coolblue.be/en/computers-tablets/experience-in-the-store-in-brussels/coolblues-choice (search 2026-11-07); https://www.coolblue.nl/ (403 on 2026-11-07)
16. https://www.hardware.info/ (named in search results 2026-11-07, not fetched)
17. https://www.beslist.be/ (named in search results 2026-11-07, not fetched)
18. https://bstore.be/amazon/computer/ (search 2026-11-07)
19. https://www.ebayinc.com/stories/news/ebay-inc-acquires-leading-belgian-online-classifieds-sites-2dehandsbe-and/ (search 2026-11-07; undated)
20. https://apify.com/studio-amba/2dehands-scraper (search 2026-11-07; scraper vendor, not used)
21. https://github.com/tychobrouwer/tweakers-pricewatch (search 2026-11-07; unofficial, not used)
22. https://pricetweakers.net/product-feed-requirements/ ; https://www.koongo.com/tweakers.html (search 2026-11-07)
23. https://www.kieskeurig.nl/ (fetched 2026-11-07)
24. https://nl.trustpilot.com/review/azerty.nl ; https://gridinsoft.com/online-virus-scanner/url/alternate-nl (search 2026-11-07)
25. https://nl.trustpilot.com/review/azerty.nl (search 2026-11-07)
26. https://gridinsoft.com/online-virus-scanner/url/megekko-nl (search 2026-11-07; automated scan, not evidence of service quality)
27. https://partnerplatform.bol.com/en/cdp/selling-via-bol-as-nlbe-partner ; https://www.emerce.nl/nieuws/bolcom-populairste-marktplaats-amazon-duurste (search 2026-11-07)
28. https://www.cowcotland.com/topic8702.html ; https://www.zunapro.com/netherlands/en/blog/dutch-marketplaces-best-platforms-selling-online (search 2026-11-07)
29. https://shop24.lu/en/?p=265463 (search 2026-11-07)
30. https://letzshop.lu/en/vendors/linsys (search 2026-11-07)
31. https://vymaps.com/LU/Obiwan-Computers-Shop-78286/ (search 2026-11-07; 2018 review)
32. https://europeanjobdays.eu/en/node/81975 (search 2026-11-07)
