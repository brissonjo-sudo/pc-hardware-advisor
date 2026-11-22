# Pair-check matrix

Last checked: 2026-11-07. Values change: verify online before concluding.

Use this file to run the pair checks of `check-compatibility` in order. "Shared" means a file in `${CLAUDE_PLUGIN_ROOT}/references/`. "Official page" means the manufacturer spec page, manual, QVL or CPU support list for the exact model.

## Verdict vocabulary

| Verdict | Definition |
|---|---|
| Compatible | Every value is sourced and inside the limit, no open action. |
| Compatible with conditions | Works if one named action is done or one named limit is accepted (BIOS version, manual setting, adapter, lower speed, manual page to check). The action is exact and testable. |
| Incompatible | A hard blocker: no action short of replacing a part fixes it. Name the blocker. |
| Not verified | A value could not be sourced (blocked page, missing model, no data in references). Never counts as compatible. Say what would settle it. |

Overall verdict = the worst pair. Confidence: high (official page or high reference row), medium (secondary, snippet, older), low (forum, retailer, unconfirmed).

## Matrix

| # | Pair | What to compare | Value comes from | Typical blockers | Typical conditions |
|---|---|---|---|---|---|
| 1 | CPU - board | Socket, chipset family, CPU generation, minimum BIOS | Shared `sockets-chipsets.md`; official board CPU support list | Different socket; generation not supported by the chipset (for example 13th/14th Gen on 500-series) | BIOS update needed (version from the support list); flash method (no-CPU feature or older CPU) |
| 2 | RAM - board - CPU | DDR4 vs DDR5 (board and CPU), speed against CPU spec, module count, capacity, profile (XMP/EXPO), controller ratio | Shared `memory.md`; official CPU spec page; board memory QVL | Wrong DDR type; capacity above platform maximum | Runs below the rated speed; 1 module runs in single channel (use 2); 4 modules lower the speed; profile must be enabled or set manually; check the QVL |
| 3 | GPU - board | x16 slot, PCIe generation, lanes | Shared `form-factors-cases.md`; board manual | Rare: no x16 slot | Slot or lane count lower than the card's (works, with less bandwidth) |
| 4 | M.2 / SATA sharing | Which sockets disable SATA ports or drop the x16 slot to x8 | Board manual lane-sharing table (see `form-factors-cases.md`) | Not usually a blocker | A SATA port is disabled when an NVMe drive uses a socket; x16 falls to x8 |
| 5 | Board - case | Form factor listed by the case | Shared `form-factors-cases.md`; official case page | Form factor not listed by the case | E-ATX varies by model: check both pages |
| 6 | GPU - case | Length (with plug), thickness, height, cable bend space | Shared `form-factors-cases.md`; official GPU and case pages | Length or thickness over the case limit | Case version or orientation changes the limit; 16-pin cable needs straight space (attribute the 35 mm and 36 mm figures) |
| 7 | Cooler - case, cooler - RAM | Cooler height, radiator and fan thickness, clearance over RAM | Official cooler and case pages | Cooler taller than the case limit | GPU thickness lowers the cooler limit in small cases; check both |
| 8 | Cooler - CPU | Socket mounting kit, rated TDP against CPU max turbo or PPT | Official cooler page; shared `power-supplies-connectors.md` (CPU power) | Kit lacks the socket | Cooler rating at or under the CPU's turbo power: expect throttling (state as a condition, not a blocker) |
| 9 | PSU - case | PSU type (ATX, SFX, SFX-L) and length | Shared `form-factors-cases.md`; official case and PSU pages | Type not listed by the case | SFX-L needs the 130 mm clearance listed by the case |
| 10 | PSU - GPU | Connector type and count, adapter, ATX 3.1, vendor-recommended wattage | Shared `power-supplies-connectors.md`; official GPU page | Missing connector with no documented adapter; wattage below the vendor figure | Adapter needed (state the plug count); PSU equals the vendor figure; ATX 3.0 or older with a 300 W+ card |
| 11 | Total power | GPU board power + CPU max turbo or PPT + rest of system; EPS connectors | Shared `power-supplies-connectors.md` (sizing method) | PSU under the requirement; missing EPS connector the board needs | At the edge of the requirement; margin is a plugin heuristic, not sourced |
| 12 | Fans and lighting - board | Fan and lighting header count; rated current or power of each fan, hub or controller on a header, summed, against the per-header limit; lighting voltage and pins (5 V 3-pin, 12 V 4-pin) | Exact board manual (header table); official fan, hub and controller pages | Lighting plug whose voltage or pin count matches no free header, with no documented adapter | Group over the header limit: power it from a PSU-fed hub or controller (SATA, Molex); too few headers: splitter or hub within the limit; limit read only in another board's manual: not verified |

If a value is not in the shared file and no official page was read, the cell result is "not verified".

## Worked examples

Values come from the shared references; anything else is marked illustrative.

### Example 1. XMP-only DDR5-7200 kit on AM5 (RAM - board - CPU)

- Check: AM5 is DDR5-only. AMD lists DDR5-5600 with 2 modules and DDR5-3600 with 4 modules for a Ryzen 9 9950X; the memory controller runs 1:1 up to DDR5-6000 and 2:1 above.
- The kit has an XMP profile and no EXPO profile.
- Verdict: **Compatible with conditions**. The kit works, but expect about DDR5-6000 for the 1:1 ratio; enable the profile manually (ASUS labels XMP support D.O.C.P.), settings may need manual tuning, and 7200 is not guaranteed. Check the board QVL.
- Source: `memory.md` (AM5 section, XMP on AM5). Confidence: medium (press, no AMD primary page).

### Example 2. RTX 5090 Founders Edition in a Fractal Terra (GPU - case, PSU - GPU)

- Case: 322 mm long, 72 mm thick, 2 expansion slots, cooler height 48 mm, SFX / SFX-L (max PSU length 130 mm), Mini-ITX only.
- Card: 304 mm long. The NVIDIA page says 2-slot in the table and 61 mm in the text (inconsistent): use up to 61 mm.
- Length: 322 - 304 = 18 mm remaining. Thickness: 72 - 61 = 11 mm remaining.
- Power: NVIDIA lists 1000 W in the spec table (the page also says a minimum of 850 W), 575 W board power, and 4x 8-pin adapter or 1x 600 W 12V-2x6 cable.
- Verdict GPU - case: **Compatible with conditions**: dimensions fit; count the 16-pin cable space (cable makers advise 35 mm straight, NVIDIA says plan about 36 mm); the cooler limit of 48 mm applies with this card (check the case page).
- Verdict PSU - GPU: **Not verified** until the user gives the SFX/SFX-L PSU model, its wattage and connectors (whether it offers a 12V-2x6 port or four 8-pin plugs for the adapter).
- Sources: `form-factors-cases.md` (GPU dimensions, small-case limits), `power-supplies-connectors.md` (GPU power). Confidence: high (vendor pages).

### Example 3. Core i7-14700K on a 700-series board (CPU - board, total power)

- Socket: LGA1700, supported by 600 and 700-series boards. Intel states that these boards need a BIOS update to boot 13th/14th Gen CPUs (page reviewed 2026-02-05).
- Verdict CPU - board: **Compatible with conditions**: BIOS version from the board's CPU support list (illustrative: "X or later"); if the board has a flash-without-CPU feature, use it; otherwise an older supported CPU is needed. Then use a BIOS with microcode 0x12F or later and Intel Default Settings (Intel instability guidance).
- Power: CPU max turbo 253 W; with an RTX 4080 FE at 320 W board power, NVIDIA recommends 750 W and the card needs 3x 8-pin adapter or a 450 W+ 12V-2x6 cable. Intel's example budget (300 W card + 300 W CPU + 150 W rest = 750 W) is a test budget, not a buying rule.
- Verdict PSU - GPU: **Compatible** only when the user's PSU is at least 750 W and has the connectors above; otherwise conditions. State which step set the requirement.
- Sources: `sockets-chipsets.md` (LGA1700, BIOS), `power-supplies-connectors.md` (CPU power, GPU power, sizing). Confidence: high (Intel and NVIDIA pages).
