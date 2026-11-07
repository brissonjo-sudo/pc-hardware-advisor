# Build playbook: requirement translation per use

Last checked: 2026-11-07. Values change: verify online before concluding.

Every priority, ratio and rule below is a **plugin heuristic** (a rule of thumb written for this plugin, not a measured or sourced fact) unless a shared reference is named. Label them as such in answers and replace them with real, dated prices and specs from the references and the web. Do not state percentages of budget as facts.

Shared references to open when a heuristic needs a fact: `${CLAUDE_PLUGIN_ROOT}/references/sockets-chipsets.md`, `memory.md`, `power-supplies-connectors.md`, `form-factors-cases.md`, `gpu-bandwidth-ai.md`.

## Gaming

- Questions: target resolution and refresh rate, monitor already owned or to buy, games played (esports titles versus demanding single-player), ray tracing wanted, streaming or recording while playing, upscaling acceptable.
- Matters most (plugin heuristic): GPU first, then CPU adequate for the target refresh rate, then enough RAM and a fast SSD. A strong CPU with a weak GPU wastes budget at high resolution; the reverse limits high refresh rates in CPU-bound titles.
- Typical choices to verify online: GPU VRAM against the target resolution and texture settings; PSU connectors for the chosen GPU (power-supplies-connectors.md); memory speed supported by the platform (memory.md).
- Constraints: GPU length and thickness against the case (form-factors-cases.md); airflow with a large GPU.
- Variant logic: cheaper = step the GPU down one tier or drop RAM/SSD capacity before touching the PSU quality or the case airflow; stronger = GPU tier up first, CPU second, only if the stated monitor can use it.

## Local AI

- Questions: models and sizes wanted, dense or MoE, quantization tolerance, context length, one user or several, chat versus coding versus agents versus fine-tuning, OS.
- First action: run the `size-local-ai` method; its memory sum and candidate hardware fix the floor. Do not re-derive it.
- Matters most (plugin heuristic): memory capacity of the accelerator, then its bandwidth, then the platform able to host it (slots, lanes, PSU, airflow); system RAM and CPU matter when models spill or for prefill-heavy use.
- Constraints: a second GPU needs slot spacing, lanes and PSU headroom (form-factors-cases.md, power-supplies-connectors.md); software support depends on vendor and OS (gpu-bandwidth-ai.md section 7 through `size-local-ai`).
- Variant logic: cheaper = smaller quantization or smaller model class that still meets the stated need; stronger = more accelerator memory or bandwidth, or a second card if the platform allows it. State that a second card adds capacity, not single-stream speed.
- Used datacenter cards are out of automatic configs (private-party); a professional refurbisher with invoice and warranty may qualify.

## Content creation (video, 3D, photo, audio)

- Questions: software used (each has its own CPU/GPU/RAM scaling), resolution and codecs, project size, render time tolerance, number of drives, colour-critical monitor.
- Matters most (plugin heuristic): software dependent. Typically CPU cores and RAM capacity for rendering and compiling; GPU for effects, encode and GPU renderers; fast scratch SSD and a separate larger storage drive. Check the software vendor's current requirements online.
- Constraints: ECC or high capacity memory needs board and CPU support (memory.md); multiple NVMe drives can share lanes (form-factors-cases.md section 6); quiet cooling for audio work.
- Variant logic: cheaper = reduce core count or GPU tier on the stage the user's software uses least; stronger = more RAM capacity, then cores, then GPU, following the user's bottleneck.

## Office and everyday

- Questions: applications, number of monitors and their resolution, video calls, longevity, noise, size, power draw.
- Matters most (plugin heuristic): a modern CPU with integrated graphics, enough RAM, a good SSD, quiet and efficient parts. A discrete GPU is rarely needed; skip it unless a monitor count or software demands it (verify the board and CPU outputs online).
- Constraints: small cases, silent operation, low idle power.
- Variant logic: cheaper = less RAM or storage capacity with open upgrade slots, never a no-name PSU; stronger = more cores or RAM only if the user names a heavy task.

## NAS and homelab

- Questions: drive count and capacity, redundancy level, OS or software stack, services run (media transcoding, virtual machines, containers), 24/7 operation, power cost, noise, ECC wanted, network speed.
- Matters most (plugin heuristic): drive bays and SATA/PCIe ports, reliability and idle power, network ports, then CPU (transcoding or VMs) and RAM capacity. Check ECC support on the exact CPU and board (memory.md, sockets-chipsets.md).
- Constraints: case drive bays and airflow; PSU efficiency at low load; SATA port count versus M.2 sharing (form-factors-cases.md); drive choices (recording technology, warranty) from manufacturer pages.
- Variant logic: cheaper = fewer bays populated now with room to grow; stronger = more capable CPU, ECC memory, extra network ports or an HBA if lanes allow.

## Mixed use

- Questions: rank the uses by importance and by hours per week; which use sets the performance floor; which can tolerate waiting.
- Method (plugin heuristic): size the build for the most demanding use, check the others are satisfied as a by-product, and do not pay for a second set of maximum requirements. Say which use was prioritized.

## Typical constraints (all uses)

- Small cases: GPU length, cooler height, PSU form factor, number of drives; read form-factors-cases.md section 4 and the case maker's page.
- Noise: larger fans at lower speed, adequate case airflow, PSU fan behaviour; reported noise levels come from manufacturer or tested sources, never guessed.
- Power draw and heat: GPU and CPU power limits from vendor pages; PSU headroom per power-supplies-connectors.md; electricity cost is the user's input, not an assumption.
- Owned parts: check them first; they can force the platform (socket, memory generation, PSU connectors).
- Banned or wanted brands: apply before shortlisting; say if the constraint removes the best option.
- Refurbished: only professional refurbishers with invoice and warranty; show warranty length and the seller type in the price row.

## Variant logic (general, plugin heuristic)

- Cheaper: reduce the part that the stated use stresses least; keep PSU quality, case airflow and upgrade path; state the capability lost.
- Stronger: improve the limiting part first (as ranked above), then the part next in line; do not upgrade a part that cannot be used (monitor, case, PSU limits).
- Always give each variant as a delta: parts that change, landed price difference, effect on the use, and the compatibility re-check.
- Memory and SSD: after the 2025-2026 price moves (used-market-checklist.md section 1), compare capacity options at current prices before fixing the default; the cheapest-per-GB assumption from older years may not hold.

## Not verified

- No benchmark data is included in this playbook; all rankings are plugin heuristics.
- Software-specific scaling (creation tools, virtualization) is not covered; check the software vendor's current requirements.
- Prices and availability are never stored here; use the `hunt-prices` method.
