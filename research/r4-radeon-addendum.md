# R4 Addendum: Radeon GPU power, connectors, size
Collected: 2026-11-07 · Model: haiku

Scope: RX 9070 XT, RX 9070, RX 9060 XT (16 GB), RX 7900 XTX, RX 7800 XT, Radeon AI PRO R9700.
Method: one fetch attempt per AMD page; Sapphire official spec pages read in full (spec section fetched at offset 100000); other sources as noted. No caches, mirrors or archive copies used.

## Reference specs

| GPU | TBP W | AMD recommended PSU | Memory / bus / GB/s | Source | Confidence |
|---|---|---|---|---|---|
| RX 9070 XT | **Not verified** (AMD page blocked: timeout; TPU blocked: 403) | **Not verified** | 16 GB GDDR6 / 256-bit / 20 Gbps (vendor). GB/s 640 = inference (20 Gbps x 256 / 8) | [3] Sapphire PULSE spec page | Memory: high (vendor). Reference power/PSU: missing |
| RX 9070 | **Not verified** | **Not verified** | 16 GB GDDR6 / 256-bit / 20 Gbps (vendor). GB/s 640 = inference | [5] Sapphire PULSE 9070 spec page | Memory: high (vendor). Reference power/PSU: missing |
| RX 9060 XT 16 GB | **Not verified** | **Not verified** | 16 GB GDDR6 / 128-bit / 20 Gbps (vendor). GB/s 320 = inference (20 x 128 / 8) | [6] Sapphire PULSE 9060 XT spec page | Memory: high (vendor). Reference power/PSU: missing |
| RX 7900 XTX | **Not verified** | **Not verified** | 24 GB GDDR6 / 384-bit (vendor). GB/s not stated on page | [7] Sapphire PULSE 7900 XTX spec page | Memory size/bus: high. Reference power/PSU: missing |
| RX 7800 XT | **Not verified** | **Not verified** | 16 GB GDDR6 / 256-bit / 19.5 Gbps (vendor). GB/s 624 = inference (19.5 x 256 / 8) | [8] Sapphire PULSE 7800 XT spec page | Memory: high (vendor). Reference power/PSU: missing |
| Radeon AI PRO R9700 | 300 W (search snippet only, citing Tom's Hardware; article body not readable) | 750 W minimum (snippet only, PowerColor page not reachable) | 32 GB GDDR6 / 256-bit / 640 GB/s (search snippets; HotHardware snippet says 644.6) | [10], [11], [12] | Low (snippets only) |

Note: the only official power figures obtained are partner-model figures (see below). No AMD reference TBP or AMD recommended PSU is verified for any GPU in this list.

## Partner models

| Model | Board power | Recommended PSU | Connectors | Length x height mm | Slots | Source | Confidence |
|---|---|---|---|---|---|---|---|
| Sapphire PULSE RX 9070 XT (11348-03-20G) | 304 W typical | Minimum 750 W | 2 x 8-pin | 320 (L) x 120.25 (W) x 61.6 (H) | 3 (ATX) | [3] | High (vendor spec page) |
| Sapphire NITRO+ RX 9070 XT | 330 W typical | Minimum 850 W | 12V-2x6 (H++); 3x 8-pin adapter included | 330.8 (L) x 128.5 (W) x 65.68 (H) | 3.2 (ATX) | [4] | High (vendor spec page) |
| Sapphire PULSE RX 9070 (11349-03-20G) | 220 W typical | Minimum 650 W | 2 x 8-pin | 280 (L) x 120.25 (W) x 51.5 (H) | 2.5 (ATX) | [5] | High (vendor spec page) |
| Sapphire PULSE RX 9060 XT 16G | 170 W typical | Minimum 450 W | 1 x 8-pin | 240 (L) x 111.25 (W) x 46.08 (H) | 2.3 (ATX) | [6] | High (vendor spec page) |
| Sapphire PULSE RX 7900 XTX 24G (11322-02-20G) | 370 W total | Minimum 800 W | 3 x 8-pin | 313 (L) x 133.75 (W) x 52.67 (H) | 2.7 (ATX) | [7] | High (vendor spec page) |
| Sapphire PULSE RX 7800 XT (11330-02-20G) | 266 W total | Minimum 700 W | 2 x 8-pin | 280 (L) x 128.75 (W) x 52.57 (H) | 2.5 (ATX) | [8] | High (vendor spec page) |
| Sapphire / PowerColor / XFX / ASRock / ASUS / Gigabyte other models | Not checked | Not checked | Not checked | Not checked | Not checked | n/a | Gap |

Notes on the partner rows:
- "Minimum PSU" is the vendor's own wording on its spec page. It is not AMD's recommendation and is recorded as the vendor value.
- Factory-OC models (NITRO+ 9070 XT: 330 W vs PULSE 304 W) confirm that board power is per model. Both Sapphire 9070 XT models are listed separately.
- A third-party snippet claimed 220 W for the PULSE 9070 XT (with 8-pin + 6-pin). This conflicts with the Sapphire official page (304 W, 2 x 8-pin) and is rejected.
- A Sapphire listing for model 21322-01 (7900 XTX, 346 W, 2 x 8-pin, 287 x 123.2 x 51.25 mm, 2.5 slot) was seen in a search snippet. It is not the PULSE board, was not fetched, and is not used.

## Not verified / gaps

1. **AMD reference TBP and AMD recommended PSU: missing for all six GPUs.** The amd.com 9070 XT product page timed out once (60 s). Not retried, per the one-attempt rule.
2. **TechPowerUp review pages: blocked** (HTTP 403, PULSE 9070 XT review). Not bypassed. No medium-confidence review values were obtained.
3. **Memory bandwidth in GB/s: not stated by any official page read.** The values in the reference table are inference from the stated effective data rate and bus width. Confidence: plausible, to verify.
4. **Sapphire NITRO+ 7900 XTX URL: 404.** Not replaced by a guessed URL.
5. **Sapphire US site (sapphire-usa.com) product URL: 404.**
6. **PowerColor R9700 page (powercolor.com/product-detail255.htm): TLS error "unable to verify the first certificate".** Not bypassed. R9700 PSU/connector (single 16-pin, 750 W) comes only from a search snippet: unverified.
7. **Tom's Hardware R9700 article: page returned headline only.** The 300 W figure is from a search snippet: low confidence.
8. **R9700 partner dimensions and PSU: not verified.**
9. **XFX, PowerColor, ASRock, ASUS, Gigabyte 9070 XT / 9060 XT / 7900 XTX / 7800 XT models: not checked** (budget limit reached).
10. **Dates:** Sapphire spec pages carry no publication date (only a "2026" banner). Dates recorded are the access date, 2026-11-07. The search index noted that the PULSE 9070 XT page was last indexed about 617 days ago, so the live page may differ from the indexed copy; the page content was read live this session.

## Sources (numbered)

1. AMD product page, RX 9070 XT: https://www.amd.com/en/products/graphics/desktops/radeon/9000-series/amd-radeon-rx-9070xt.html. Status: **blocked, timeout (60 s)**. Checked 2026-11-07.
2. TechPowerUp review, Sapphire PULSE RX 9070 XT: https://www.techpowerup.com/review/sapphire-radeon-rx-9070-xt-pulse. Status: **blocked, HTTP 403**. Checked 2026-11-07.
3. Sapphire PULSE RX 9070 XT (11348-03-20G): https://www.sapphiretech.com/en/consumer/pulse-radeon-rx-9070-xt-16g-gddr6. Read 2026-11-07, spec section at offset 100000. Confidence: high (vendor).
4. Sapphire NITRO+ RX 9070 XT: https://www.sapphiretech.com/en/consumer/nitro-radeon-rx-9070-xt-16g-gddr6. Read 2026-11-07, spec section at offset 100000. Confidence: high (vendor).
5. Sapphire PULSE RX 9070 (11349-03-20G): https://www.sapphiretech.com/en/consumer/pulse-radeon-rx-9070-16g-gddr6. Read 2026-11-07, spec section at offset 100000. Confidence: high (vendor).
6. Sapphire PULSE RX 9060 XT 16G: https://www.sapphiretech.com/en/consumer/pulse-radeon-rx-9060-xt-16g-gddr6. Read 2026-11-07, spec section at offset 100000. Confidence: high (vendor).
7. Sapphire PULSE RX 7900 XTX 24G (11322-02-20G): https://www.sapphiretech.com/en/consumer/pulse-radeon-rx-7900-xtx-24g-gddr6. Read 2026-11-07, spec section at offset 100000. Confidence: high (vendor).
8. Sapphire PULSE RX 7800 XT (11330-02-20G): https://www.sapphiretech.com/en/consumer/pulse-radeon-rx-7800-xt-16g-gddr6. Read 2026-11-07, spec section at offset 100000. Confidence: high (vendor).
9. Sapphire NITRO+ RX 7900 XTX (guessed URL): https://www.sapphiretech.com/en/consumer/nitro-radeon-rx-7900-xtx-24g-gddr6. Status: **404**. Not used.
10. Tom's Hardware, AMD Radeon AI PRO R9700 launch: https://www.tomshardware.com/pc-components/gpus/amd-launches-radeon-ai-pro-r9700-to-challenge-nvidias-ai-market-dominance. Status: headline only when fetched; 300 W from search snippet. Confidence: low.
11. PowerColor Radeon AI PRO R9700: https://powercolor.com/product-detail255.htm. Status: **TLS certificate error**. 750 W / 16-pin from search snippet. Confidence: low.
12. HotHardware, Radeon AI PRO R9700: https://hothardware.com/news/radeon-ai-pro-r9700-arrives-32gb-vram-machine-learning. Search snippet only (644.6 GB/s). Confidence: low.
