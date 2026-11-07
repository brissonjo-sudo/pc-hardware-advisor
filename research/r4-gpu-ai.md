# R4 GPU, APU and local AI sizing data
Collected: 2026-11-07 · Model: sonnet

All "checked" dates are 2026-11-07. Conventions: **[V]** = read on the cited page by this session's fetch tool (the tool summarises pages; treat quotes as paraphrase); **[D]** = derived by arithmetic from verified bus width x memory speed or from a secondary source; **[E]** = estimate/inference, not a measurement. Confidence: high / medium / low.

## Memory capacity and bandwidth

| Device | Memory | Bus/type | Bandwidth GB/s | NVLink | Status | Source | Confidence |
|---|---|---|---|---|---|---|---|
| RTX 3060 12GB | 12 GB | 192-bit GDDR6 [V bus/type] | 360 [D: 192-bit x 15 Gbps; Gigabyte spec pages list 360, S10] | not listed | used/new (old) | S1, S10 | medium |
| RTX 3090 | 24 GB | 384-bit GDDR6X [V] | 936 [D, S10 Techgage launch table] | Yes (NVLink bridge, 2-way) [V] | used | S1, S2, S10 | high (cap/bus), medium (bw) |
| RTX 3090 Ti | 24 GB | 384-bit GDDR6X [V] | ~1008 [D: 21 Gbps x 384/8, not fetched] | Yes [V] | used | S1, S2 | medium |
| RTX 4060 Ti 16GB | 16 GB | 128-bit GDDR6 [V] | ~288 [D, not fetched] | No | new/used | S1 | medium |
| RTX 4070 Ti SUPER | 16 GB | 256-bit GDDR6X [V] | ~672 [D, not fetched] | No | new/used | S1 | medium |
| RTX 4080 SUPER | 16 GB | 256-bit GDDR6X [V] | ~736 [D, not fetched] | No | new/used | S1 | medium |
| RTX 4090 | 24 GB | 384-bit GDDR6X [V] | ~1008 [D, not fetched] | No [V] | used/new | S1, S3 | medium |
| RTX 5060 Ti 16GB | 16 GB | 128-bit GDDR7 [V] | 448 [V] | not listed | new | S1 | high |
| RTX 5070 Ti | 16 GB | 256-bit GDDR7 [V] | 896 [V] | not listed | new | S1 | high |
| RTX 5080 | 16 GB | 256-bit GDDR7 [V] | 960 [V] | not listed | new | S1 | high |
| RTX 5090 | 32 GB | 512-bit GDDR7 [V] | 1792 [V] | No [V] | new | S1, S4 | high |
| RTX PRO 6000 Blackwell (Workstation / Max-Q / Server) | 96 GB GDDR7 ECC | 512-bit [E: same GB202 class, not on page] | not stated on NVIDIA page (blocked from stating); 1792 widely reported, unverified | not stated | new, pro (600 W / 300 W / 400-600 W) | S5 | medium (cap), low (bw) |
| RX 7900 XTX | 24 GB | 384-bit GDDR6 | 960 [secondary S11; AMD page timed out] | none | new/used | S11 | medium |
| RX 9070 XT | 16 GB | 256-bit GDDR6 20 Gbps | 640 [secondary S11; AMD page timed out] | none | new | S11 | medium |
| Radeon AI PRO R9700 | 32 GB | 256-bit GDDR6 20 Gbps | 640 (AMD spec; 644.6 exact calc) [secondary S12; AMD page timed out]; 300 W; ~$1,299 | none | new, pro | S12 | medium |
| Arc B580 | 12 GB | 192-bit GDDR6 [V] | 456 [V] | none | new | S6 | high |
| Arc Pro B60 | 24 GB | 192-bit GDDR6 [V] | 456 [V], 120-200 W, launch Q2'25 | none | new (pro, mostly via integrators); Maxsun dual-B60 48 GB reported $1,200 to $3,000 | S7, S13 | high (spec), low (price) |
| Tesla P40 | 24 GB GDDR5 | 384-bit [E] | ~346-347 (secondary S14) | none | used/datacenter; passive heatsink (needs forced airflow, not verified from page); no video out | S14 | medium |
| Tesla V100 32GB | 32 GB HBM2 | 4096-bit [E] | 900 NVIDIA marketing (897 per third party); NVLink 300 GB/s only on SXM2 variant, not PCIe | SXM2 only | used/datacenter; PCIe card passive cooling; SXM2 needs adapter board | S14 | medium |
| Instinct MI50 32GB | 32 GB HBM2 | 4096-bit [V] | ~1024 ("1 TB/s" on AMD driver page) [V] | Infinity Fabric link (not verified) | used/datacenter, 300 W, passive; **ROCm: unsupported in current release** [V S16] | S15, S16 | high (spec), high (unsupported) |
| Ryzen AI Max+ 395 (Strix Halo) | up to 128 GB shared LPDDR5X-8000 | 256-bit [source: lhl README "256 GB/s theoretical (256-bit 8000 MT/s)"] | 256 theoretical; ~215-221 measured GPU memory bandwidth (memtest_vulkan) | n/a | new (mini PCs, laptops) | S17, S18 | medium-high (AMD page timed out; bus width from community measurement) |
| NVIDIA DGX Spark (GB10) | 128 GB (64 GB via OEM) LPDDR5X | 256-bit | 273 [V] | n/a (ConnectX-7 200 Gbps, up to 4 systems) | new | S8 | high |
| Apple M3 Ultra | up to 512 GB | unified | "over 800" per Apple release; 819 per secondary S19 | n/a | new (Mac Studio 2025) | S20, S19 | high (800+), medium (819) |
| Apple M4 Max | up to 128 GB | unified | "over half a TB/s" per Apple; 410 (32-GPU) / 546 (40-GPU) per llama.cpp #4167 table | n/a | new (2025) | S20, S21 | high |
| Apple M5 Max | up to 128 GB (36/48/64/128 options) | LPDDR5X-9600 [secondary] | 614 (40-GPU) / 460 (32-GPU) [V Apple Mac Studio specs; MacBook Pro newsroom 614] | n/a | new, MacBook Pro 11 Mar 2026; Mac Studio announced 25 Aug 2026, shipping from 22 Sep 2026 (secondary) | S22, S23, S24 | high |
| Apple M5 Ultra | up to 512 GB | unified | 1228 per llama.cpp table; "1.2 TB/s" per Apple spec page [V] | n/a | new, Mac Studio 2026 (from $5,499 at 96 GB, secondary); 512 GB config reported late Oct 2026 | S22, S21, S24 | medium-high |

NVLink summary: among GeForce, NVIDIA's own comparison page lists NVLink "Yes" only for RTX 3090 and 3090 Ti (2-way bridge). RTX 4090, 4080 SUPER, 4070 Ti SUPER, 4060 Ti and 5090 show "No". Blackwell 50 series: no NVLink row (RTX 5090 page says "No"). Confidence high [S1, S2, S4]. The 3060 NVLink status was "not listed".

## Estimation method and efficiency factors

Formula (decode, batch 1): `tok/s <= B_eff / bytes_read_per_token`, with `B_eff = MBU x B_peak`. Bytes per token ~ weight file size (dense) + KV cache read for the current context (Databricks: achieved bandwidth = (parameter size + KV cache size) / time per output token). For MoE, use active-expert bytes (routing adds overhead: expect a lower MBU than dense) [E].
- Prefill (prompt processing) is compute-bound; decode is memory-bound. Databricks: "generating the first token is typically compute-bound", subsequent decode memory-bound [V, S25, dated 2023-10-12]. Practical consequence: pick GPUs by bandwidth for chat/decode speed, by TFLOPS for long prompts/RAG. Evidence in S21: M2/M3 Ultra prefill is ~1,000-1,500 tok/s for a 7B vs 5,000-6,000 on an RTX 3090 despite similar decode.
- Published MBU: 60% on 2x H100-80GB and 55% on 4x A100-40GB at batch 1; 50% in the 7B worked example [V S25]. These are datacenter/vLLM figures; MBU falls as batch rises.
- My ratios below are [E]: measured tg128 divided by (peak bandwidth / model file size). Model file used: Llama 2 7B Q4_0 ~3.8 GB (3.56 GiB; recalled from llama-bench output, not re-verified this session, so +/-3%). Calculated using peak bandwidth in the table above.

| Hardware | Peak GB/s | Ceiling tok/s (7B Q4_0) | Measured tg128 (S26/S27/S21) | Efficiency [E] |
|---|---|---|---|---|
| RTX 3090 (CUDA) | 936 | ~244 | 151-178 | 62-73% |
| RTX 4090 (CUDA) | 1008 | ~263 | 186-189 | ~71% |
| RTX 5090 (CUDA) | 1792 | ~468 | 240-300 | 51-64% |
| RX 7900 XTX (Vulkan) | 960 | ~251 | 183-191 | 73-76% |
| RX 9070 XT (Vulkan) | 640 | ~167 | 137-142 | 82-85% |
| Arc B580 (Vulkan) | 456 | ~119 | 70-72 | 59-61% |
| Strix Halo (Vulkan) | 256 | ~67 | 52-54 | 77-81% of 256 (about 95% of the measured 215-221) |
| M2/M3 Ultra | 800 | ~209 | 88-94 | 42-45% (Apple Ultra decode scales poorly with bandwidth) |
| M4 Max (40 GPU) | 546 | ~143 | 83 | 58% |
| M5 Max (40 GPU) | 614 | ~160 | 120 | 75% |

Rule of thumb supported by data: discrete NVIDIA/AMD GPUs reach 60-80% of peak on small dense models; the very fast cards (5090) drop to 50-65% (kernel/launch overhead dominates small models); Apple chips range 45-75% (older Ultra worst); APUs with measured bandwidth reach ~90% of the measured figure. For sizing use 0.6 as a conservative planning factor, 0.7 typical, never above 0.85. Confidence medium.
- Large dense models fill the memory pipeline better: dual RTX 3090, Llama 3.3 70B Q4_K_M (42.5 GB file), layer split measured 19.5 tok/s versus a ceiling of 936/42.5 = 22 tok/s, so ~89% of a single card's bandwidth (S28). Only one GPU is active at a time in layer split.
- Context cost: decode slows with depth. DGX Spark gpt-oss-120b MXFP4: tg 60.6 tok/s at depth 0, 54.1 at 4k, 47.5 at 16k, 40.6 at 32k (S29). Plan for 15-35% loss at 16-32k context [E, from this one data point].

## Measured benchmarks

All are llama.cpp unless noted. Prefill = pp512 unless noted. "n/s" = not stated.

| Hardware | Model | Quant | Context | Backend | Prefill tok/s | Decode tok/s | Source | Date |
|---|---|---|---|---|---|---|---|---|
| RTX 3090 | Llama 2 7B | Q4_0 | pp512/tg128, FA off / on | CUDA | 5174 / 5560 (c76b420) | 158 / 162 | S26 | 2025-08-01 |
| RTX 3090 | Llama 2 7B | Q4_0 | same | CUDA (build 10809) | 5154 / 5974 | 169 / 178 | S26 | 2026-09-07 |
| RTX 4090 | Llama 2 7B | Q4_0 | same | CUDA (build 6098) | 11993 / 14771 | 186 / 189 | S26 | 2025-08-06 |
| RTX 5090 | Llama 2 7B | Q4_0 | same | CUDA (600 W, build 6060) | 14752 / 16042 | 240 / 249 | S26 | 2025-08-02 |
| RTX 5090 | Llama 2 7B | Q4_0 | same | CUDA (8cf6b42) | 14073 / 14970 | 290 / 300 | S26 | n/s (scoreboard) |
| RX 7900 XTX | Llama 2 7B | Q4_0 | same | Vulkan | 3727 / 3890 | 183 / 191 | S27 | thread started 2024-12-18; entry undated |
| RX 9070 XT | Llama 2 7B | Q4_0 | same | Vulkan | 5202 / 5604 | 137 / 142 | S27 | undated |
| Arc B580 | Llama 2 7B | Q4_0 | same | Vulkan | 621 / 419 | 70 / 72 | S27 | undated |
| Arc Pro B60 | Llama 2 7B | Q4_0 | same | Vulkan | 730 / 727 | 65 / 68 | S27 | undated |
| Ryzen AI Max+ 395 | Llama 2 7B | Q4_0 | same | Vulkan | 1487 / 1704 | 52 / 54 | S27 | undated |
| Ryzen AI Max+ 395 | Llama 2 7B | Q4_0 | pp512/tg128 | Vulkan AMDVLK, FA | 1294 | 47.7 | S18 | b5863, ~2025-07 |
| Ryzen AI Max+ 395 | gpt-oss 20B | MXFP4 | pp512/tg128 | HIP + hipBLASLt | 1196 | 46.9 | S18 | ~2025-07/08 |
| Ryzen AI Max+ 395 | Qwen3 30B-A3B (MoE) | UD-Q4_K_XL | pp512/tg128 | HIP rocWMMA FA / Vulkan b=256 | 669 | 58.5 / 78.0 | S18 | ~2025-07/08 |
| Ryzen AI Max+ 395 | gpt-oss 120B (MoE) | MXFP4 | pp512/tg128 | Vulkan AMDVLK | 431 | 33.7 | S18 | ~2025 |
| Ryzen AI Max+ 395 | Shisa V2 70B (dense) | i1-Q4_K_M | pp512/tg128 | HIP rocWMMA | 94.7 | 4.5 | S18 | ~2025 |
| 2x RTX 3090 (PCIe 3.0 x16 each, no NVLink, 290 W cap) | Llama 3.3 70B | Q4_K_M (42.5 GB) | default test; 8K filled variant | CUDA, layer split | 577 | 19.5 | S28 | tests 2026-10-19, build b11741 |
| 2x RTX 3090 (same) | Llama 3.3 70B | Q4_K_M | default test | CUDA, tensor split (experimental) | 763 | 31.9 (29.9 at 8K ctx, prefill 656) | S28 | 2026-10-19 |
| 1 vs 2x RTX 3090 | Qwen3 32B | Q4_K_M | default | CUDA | 1198 vs 1578 (tensor) | 35.3 vs 59.8 | S28 | 2026-10-19 |
| 2x RTX 3090 | Llama 3.3 70B | AWQ (vLLM 0.31.0, TP=2) | 1 user | vLLM | TTFT 0.72 s | 31.25 (148.8 aggregate at 8 users) | S28 | 2026-10-19 |
| NVIDIA DGX Spark GB10 | gpt-oss 120B | MXFP4 | pp2048 / tg32, depth 0 | CUDA b6922 (kernel 6.17.1) | 1956 | 60.6 | S29 | b6922, ~Oct 2025 |
| M2 Ultra (76 GPU, 800 GB/s) | Llama 2 7B | Q4_0 | pp512/tg128 | Metal | 1238 | 94.3 | S21 | 2023-11-21 |
| M3 Ultra (80 GPU) | Llama 2 7B | Q4_0 | same | Metal | 1471 | 92.1 | S21 | commit 8e672ef |
| M4 Max (40 GPU, 546 GB/s) | Llama 2 7B | Q4_0 | same | Metal | 886 | 83.1 | S21 | commit 8e672ef |
| M5 Max (40 GPU, 614 GB/s) | Llama 2 7B | Q4_0 / Q8_0 / F16 | same | Metal | 3220 / 3144 / 3158 | 119.9 / 72.4 / 37.1 | S21 | commit c1d0e7a, 2026 |
| M5 Ultra (80 GPU, 1228 GB/s) | Llama 2 7B | Q4_0 / Q8_0 / F16 | same | Metal | 4945 / 4911 / 5207 | 179.1 / 119.0 / 73.6 | S21 | commit c1d0e7a, 2026 |

Notes: (1) S26 and S27 results are community-submitted; hardware states and builds differ per row. (2) The M3 Ultra was entered at 800 GB/s in S21 although Apple/secondaries say 819. (3) A single-card Llama 8B Q4_K_M number was not obtained in a verifiable form. The Llama 2 7B Q4_0 (about 3.8 GB) is the standard stand-in; an 8B Q4_K_M (4.58 GiB per S30) should run ~20% slower on the same card [E]. (4) No measured M-series Ultra 70B Q4 number was found; secondary estimate sites (willitrunai, specpicks) disagree (14 to 24 tok/s) and are not measurements. Theory ceiling for 70B Q4_K_M (~40-42 GB) at 819 GB/s is ~19-20 tok/s, realistic 45-60% of that [E].

## Memory sizing

Bits per weight and sizes from llama.cpp `tools/quantize/README.md` (Llama 3.1 8B; S30, fetched 2026-11-07, high confidence):

| Type | bpw | Size, 8B (GiB) | Bytes/weight |
|---|---|---|---|
| F16 | 16.00 | 14.96 | 2.000 |
| Q8_0 | 8.50 | 7.95 | 1.063 |
| Q6_K | 6.56 | 6.14 | 0.820 |
| Q5_K_M | 5.70 | 5.33 | 0.713 |
| Q4_K_M | 4.89 | 4.58 | 0.612 |
| Q4_K_S | 4.67 | 4.36 | 0.583 |
| IQ4_XS | 4.46 | 4.17 | 0.557 |
| Q3_K_M | 4.00 | 3.74 | 0.500 |
| IQ3_M / IQ3_S | 3.76 / 3.66 | 3.52 / 3.42 | 0.47 / 0.46 |
| Q2_K | 3.16 | 2.95 | 0.395 |
| IQ2_XS | 2.59 | 2.42 | 0.324 |
| IQ1_S | 2.00 | 1.87 | 0.250 |

Q4_K_M is ~4.9 bpw (not 4.0). Bytes = params x bpw / 8. Examples [computed from the table]: 70B at Q4_K_M ~42 GB (measured file 42.5 GB, 39.59 GiB for Llama 3.3 70B in S28); at Q8_0 ~74 GB; at F16 ~140 GB. Note for MoE: all expert weights must be resident (or offloaded), only active experts count for bandwidth.

KV cache formula: `bytes = 2 (K and V) x n_layers x n_kv_heads x head_dim x context_tokens x bytes_per_element` (F16 = 2 bytes; Q8_0 KV ~1.06; Q4_0 ~0.56). Inputs from HF configs [V, S31, S32]:
- Llama 3.1 8B: 32 layers, 8 KV heads (of 32 attention heads), head_dim 128 -> 2x32x8x128x2 = 131,072 B = 128 KiB/token -> 8k ctx = 1.0 GiB; 32k = 4.0 GiB; 128k = 16 GiB.
- Llama 3.1 70B: 80 layers, 8 KV heads (of 64), head_dim 128 -> 2x80x8x128x2 = 327,680 B = 320 KiB/token -> 8k = 2.5 GiB; 32k = 10 GiB; 128k = 40 GiB.
- Without GQA (64 KV heads) the 70B figure would be 8x larger (so GQA is essential). Confidence: high for arithmetic; layer/head numbers from unsloth mirrors of Meta configs.

Worked sizing, 70B Q4_K_M at 32k context: weights 39.6 GiB + KV 10 GiB + compute buffers/CUDA context ~1-2 GiB/GPU + 5-10% safety margin ~= 55 GiB total -> needs 2x 32 GB (e.g., 2x RTX 5090) or 3x 24 GB; 2x 24 GB (48 GB) fits only with ~8k context (39.6 + 2.5 + overhead ~ 44-46 GiB). Measured: S28 reported 20.8 GiB/card peak for 70B Q4_K_M at default context and 22.1 GiB/card at 8K filled on 2x 24 GB. Overhead rule [E]: reserve 1-2 GB per GPU plus ~10% headroom; Windows desktop GPUs also lose ~0.5-1 GB to the display.

## Multi-GPU

- llama.cpp `--split-mode` (S33, docs/multi-gpu.md): `layer` (default) = pipeline parallelism; each GPU holds a contiguous block of layers; tolerates slow interconnect; capacity sums, speed does not (single stream: one GPU active at a time). `row` = deprecated, avoid. `tensor` = experimental; splits weights and KV cache; needs flash attention; KV cache must be f16/bf16/f32 (no quantized KV); best on multiple NVIDIA GPUs on CUDA; heavily interconnect-sensitive; NCCL recommended; not implemented for many MoE/SSM/hybrid architectures. Peer-to-peer (`GGML_CUDA_P2P`) is opt-in and usually limited to workstation/datacenter GPUs. [V, high]
- Measured: 2x RTX 3090 on PCIe 3.0 x16, no NVLink, 70B Q4_K_M: layer split 19.5 tok/s, tensor split 31.9 tok/s (1.64x), 32B: 1 card 35.3 vs 2 cards tensor 59.8 (1.69x) [S28, blog, medium confidence; it states the tensor mode as experimental].
- vLLM (S34): tensor parallel needs fast intra-node links; on nodes without NVLink (L40S example) prefer pipeline parallel. Linux only [S35]. ExLlama-based tensor parallel: no primary source fetched (gap).
- PCIe lane impact: single GPU with model fully in VRAM, decode generates no meaningful PCIe traffic (Reddit-derived report that OCuLink was ~1% utilised during generation, S36); layer-split llama.cpp also tolerates x1-x4 for decode (anecdotal; no controlled benchmark found). Tensor parallel does care: one report of 4x P100 TP bottlenecked at PCIe 3.0 x4, advice x8 or better, ~10% loss from x16 to x8 (anecdote, S37, low confidence). Lane width mostly affects model load time and prefill with offloading.
- NVLink: GeForce 3090/3090 Ti only (2-way bridge); not on 4090/5090. Consumer cards 4090/5090 across PCIe lack P2P in many setups [E; llama.cpp doc says P2P usually limited to workstation/datacenter].

## eGPU links

| Link | Raw | Usable PCIe | Source |
|---|---|---|---|
| OCuLink (PCIe 4.0 x4) | 16 GT/s x 4 | ~64 Gbps raw (~7-7.8 GB/s) | S38 (secondary) |
| Thunderbolt 3/4, USB4 40 Gbps | 40 Gbps | ~32 Gbps PCIe 3.0 x4-equivalent ceiling (one article reports a lower real-world ~22 Gbps cap, not verified) | S38 |
| Thunderbolt 5 | 80 Gbps (120 Gbps boost for display) | PCIe Gen4 x4 = 64 Gbps tunnel | S38 |

Measured effect (all secondary blogs/forums, medium-low confidence; no controlled llama.cpp study across links found):
- Decode with model fully in VRAM: Llama 3.1 8B Q4_K_M on RTX 4090: 142 tok/s internal PCIe 5.0 x16 vs 138 over OCuLink (-3%); another blog gives OCuLink -1.8%, TB4 -5.4%, USB4 -5.9% for 8B, and -1.5% (OCuLink) / -4.9% (TB4) for 70B. llama.cpp internal vs TB3 RTX 3090: generation 2.33 vs 2.27 tok/s (a 70B+ offloaded run). Outlier: one Jan test, RTX 4090 over TB3: 62 vs 100 tok/s for Mistral 7B (-38%), which the author does not generalise (S36 aggregator).
- Prompt processing: 140 vs 304 tok/s on a 2,048-token prompt for TB3 vs internal on 3090 (-54%).
- Model load (70B, RAM cache to VRAM): internal 1.9 s, OCuLink 5.4 s, TB5 6.8 s, TB4 13.2 s, USB4 13.6 s (blog).
- Gaming comparison for context: Tom's Hardware reports up to -23% on RTX 4090 over OCuLink; OCuLink beats TB5 by ~13-20% on average despite equal PCIe rate (S39, S38).
- Conclusion [E, supported by the above]: for a single eGPU holding the whole model, decode loses 2-6% (OCuLink/TB4), load time rises several-fold, prefill suffers on TB3. Avoid eGPUs for models that spill into system RAM or for multi-eGPU tensor split. Confidence medium.

## Software stacks

| Stack | HW requirement (checked) | Runs | OS | Source |
|---|---|---|---|---|
| CUDA / NVIDIA | CUDA 13.0 removed offline compilation/library support for Maxwell, Pascal, Volta (cc < 7.5) [V S40, S41]; cuFFT 13.0 note says same. Pascal/Volta/Maxwell cards still run on CUDA 12.x (NVIDIA recommends staying on 12.9 + driver branch 580, supported to ~2028 per S41). Ollama minimum cc 5.0 with driver 570+ for cc 5.0-6.2 [S42]. vLLM: cc >= 7.5 [S35]. MLX CUDA: SM 7.5+, driver 550.54.14+ [S43]. | llama.cpp, Ollama, LM Studio, vLLM, ExLlama, PyTorch training | Linux, Windows (vLLM Linux/WSL only) | S35, S40-S43 |
| ROCm / AMD | ROCm 7.14.0 production on Linux. Officially supported Radeon: RX 7900 XTX/XT, 7800 XT, 9070 XT, 9070, AI PRO R9700, PRO W7900; **Ryzen AI Max+ 395 not on AMD's Linux list** (works via TheRock nightlies/community; vLLM and Ollama list it, S35, S42); MI50 unsupported [V S16]. Linux OS: Ubuntu 24.04.4/22.04.5, RHEL 10.1/9.7. Windows: ROCm 7.2.1 + PyTorch 2.9 on Windows 11, RX 7900 XTX/9070 XT/9070/9060 XT/AI PRO R9700/W7900/7700, PyTorch only ("not the entire ROCm stack") [V S44]. Ollama: Windows RX 7600-7900 XTX, W7500-W7900. | PyTorch, llama.cpp HIP, Ollama, vLLM (Linux), LM Studio (ROCm llama.cpp) | Linux (full), Windows (limited) | S16, S44, S42 |
| Vulkan backend (llama.cpp) | Vendor-neutral; competitive on AMD (7900 XTX tg 183-191 vs ROCm not compared here), good on Intel Arc, works on NVIDIA with coopmat2 (3090 pp 4666 vs CUDA 5174, tg 164 vs 158 on Llama 2 7B Q4_0) [S26, S27]. Ollama and LM Studio enable Vulkan where needed [S42]. | llama.cpp, Ollama, LM Studio | Linux, Windows | S27, S42 |
| Intel (SYCL / oneAPI / OpenVINO) | llama.cpp SYCL supports Arc A-series (A770/A750), B580, Data Center Max, Flex 170, integrated Arc; oneAPI 2025.x-2026.1; Linux (Ubuntu 22.04/24.04) and Windows 11; Arc Pro B60 is mentioned only in a performance note [V S45]. **IPEX-LLM repository archived by Intel on 2026-01-28**, no successor named [V S46]. vLLM XPU backend supports Intel Arc/Data Center GPUs, Python 3.12 [S35]. OpenVINO: not fetched this session (gap). | llama.cpp SYCL/Vulkan, vLLM XPU | Linux (best), Windows | S45, S46, S35 |
| Apple Metal / MLX | MLX: Apple silicon, macOS >= 14.0, Python >= 3.10 [V S43]; llama.cpp Metal; Ollama and LM Studio use Metal. MLX 4-bit on 70B reported ~15% faster than llama.cpp (secondary, low confidence). | llama.cpp, Ollama, LM Studio, MLX/mlx-lm, PyTorch MPS (inference/light training) | macOS | S43, S42 |
| NVIDIA DGX Spark / GB10 | CUDA on Arm, llama.cpp CUDA works (S29); software is DGX OS (not verified). | llama.cpp, vLLM, PyTorch | Linux (Arm) | S8, S29 |

Recommendation guidance [E]: NVIDIA/CUDA is the only stack that runs everything (vLLM, training, ExLlama). AMD RDNA3/4 is fine for llama.cpp/Ollama inference, training on Linux with caveats. Intel Arc runs llama.cpp via SYCL/Vulkan but lost IPEX-LLM. Apple has the most memory per euro but the lowest prefill speed and bandwidth efficiency.

## 2025-2026 hardware status

- **RTX 50 Super**: not released as of this check. Reports (Jan-Feb 2026) say NVIDIA delayed the Super refresh "indefinitely" due to memory costs, with rumoured 24 GB 5070 Ti Super / 5080 Super; The Information via Tom's Hardware: no new gaming GPUs in 2026, RTX 60 not before 2028. Rumours only, NVIDIA unconfirmed. No sources newer than Feb 2026 found (S47). Confidence: medium that none launched; verify before advising to wait.
- **RTX PRO 6000 Blackwell**: 96 GB GDDR7 ECC; Workstation 600 W, Max-Q 300 W, Server 400-600 W, PCIe Gen5 x16 (S5). Bandwidth not stated on NVIDIA page.
- **Radeon AI PRO R9700**: 32 GB GDDR6, 640 GB/s, 300 W, ~$1,299 at retail launch; ROCm Linux and Windows supported (S12, S16, S44).
- **Intel Arc Pro B60**: 24 GB, 456 GB/s, 120-200 W, ~$500 single card via integrators; Maxsun dual-B60 48 GB reported at $1,200 (early) up to $3,000 listings, limited supply (S7, S13; low confidence on price).
- **Ryzen AI Max+ 395**: up to 128 GB LPDDR5X-8000, 256-bit (~256 GB/s theoretical, ~215-221 measured), Radeon 8060S 40 CU. Sustained dense 70B Q4 ~4.5 tok/s; MoE models (gpt-oss 120B 33.7 tok/s, Qwen3 30B-A3B 58-78) are the sweet spot (S17, S18).
- **DGX Spark / GB10**: 128 GB LPDDR5X 273 GB/s; gpt-oss-120b ~60 tok/s decode, ~1,950 pp2048 (S8, S29). Bandwidth is the limiter for dense models.
- **Apple**: M3 Ultra / M4 Max Mac Studio (5 Mar 2025). M5 Pro/Max MacBook Pro shipped 11 Mar 2026 (Max: 128 GB, 614 GB/s). M5 Max and M5 Ultra Mac Studio announced 25 Aug 2026 (Ultra: 512 GB, ~1.2 TB/s, from $5,499; M5 Max from $2,499), shipping from 22 Sep 2026 (secondary S24; Apple spec page S22 lists M5 Max 460/614 GB/s and M5 Ultra 1.2 TB/s). M5 Max decode on 7B Q4_0: 120 tok/s; prefill 3,220, about 2.2x the M3 Ultra (S21).
- Memory price pressure (DRAM crisis) is cited by multiple secondary sources as the cause of GPU Super delays; used-market prices for 3090/MI50/P40 not collected.

## Not verified / gaps

- AMD official spec pages (R9700, 7900 XTX, 9070 XT, Ryzen AI Max+ 395) timed out; values taken from secondary sources. TechPowerUp blocked (HTTP 403, not bypassed). Hugging Face official Meta repo returned 401; unsloth mirrors used.
- NVIDIA pages do not publish bandwidth for 30/40 series or RTX PRO 6000; bandwidth for 3090 Ti, 4060 Ti, 4070 Ti SUPER, 4080 SUPER, 4090, RTX PRO 6000 are derived or recalled, not fetched.
- P40/V100 official datasheets unreadable (P40 PDF compressed, V100 page lacks). Passive cooling, driver caveats (P40 needs a 3D-printed fan shroud, 8-pin EPS power, no Windows WDDM in some cases) are general knowledge, not source-verified.
- No fetched source for ExLlamaV2/V3 tensor parallelism, OpenVINO, LM Studio runtime support, or Apple 70B measured decode. No controlled x4 vs x16 PCIe llama.cpp benchmark. eGPU numbers are from low-to-medium quality blogs; the "22 Gbps" Thunderbolt PCIe cap is unconfirmed.
- Llama 2 7B Q4_0 file size (3.56 GiB) used in the efficiency table was not re-fetched.
- The Oct 2026 dual-3090 article (S28) is a single-author blog; llama.cpp build b11741 and vLLM 0.31.0 are as cited by that page.
- No 5070 Ti / 5080 / 4060 Ti / 5060 Ti measured tok/s collected.
- Strix Halo official AMD memory bus width not confirmed from AMD; derived from community README.
- Pricing, used-market availability and power/cost figures were out of scope.

## Sources

All checked 2026-11-07.

1. NVIDIA GeForce compare specs, https://www.nvidia.com/en-us/geforce/graphics-cards/compare/
2. NVIDIA RTX 3090/3090 Ti, https://www.nvidia.com/en-us/geforce/graphics-cards/30-series/rtx-3090-3090ti/
3. NVIDIA RTX 4090, https://www.nvidia.com/en-us/geforce/graphics-cards/40-series/rtx-4090/
4. NVIDIA RTX 5090, https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5090/
5. NVIDIA RTX PRO 6000 family, https://www.nvidia.com/en-us/products/workstations/professional-desktop-gpus/rtx-pro-6000-family/
6. Intel Arc B580 specs, https://www.intel.com/content/www/us/en/products/sku/241598/intel-arc-b580-graphics/specifications.html
7. Intel Arc Pro B60 specs, https://www.intel.com/content/www/us/en/products/sku/243916/intel-arc-pro-b60-graphics/specifications.html
8. NVIDIA DGX Spark, https://www.nvidia.com/en-us/products/workstations/dgx-spark/
9. (blocked) TechPowerUp RTX 5090 page, HTTP 403.
10. RTX 3060/3090 bandwidth secondary: Gigabyte 3060 pages and Techgage launch table via search, https://www.gigabyte.com/id/Graphics-Card/GV-N3060EAGLE-12GD-rev-10/sp
11. RX 9070 XT / 7900 XTX secondary: https://www.tomshardware.com/pc-components/gpus/amd-radeon-rx-9070-xt-review and https://www.gpu-monkey.com/en/compare_gpu-amd_radeon_rx_9070_xt-vs-amd_radeon_rx_7900_xtx
12. Radeon AI PRO R9700: https://www.tomshardware.com/pc-components/gpus/amd-launches-radeon-ai-pro-r9700-to-challenge-nvidias-ai-market-dominance and https://hothardware.com/news/amd-confirms-radeon-ai-pro-r9700-gpu-pricing-release-date
13. Maxsun Arc Pro B60 Dual 48GB: https://www.tweaktown.com/news/107051/maxsuns-new-arc-pro-b60-dual-48gb-ships-next-week-intel-gpu-card-costs-1200/index.html and https://www.tweaktown.com/news/107258/maxsuns-new-intel-arc-pro-b60-dual-48gb-turbo-dual-gpu-card-has-been-listed-in-us-for-3000/index.html
14. P40/V100 secondary: https://hmc-tech.com/gpu/nvidia-tesla-p40-vs-nvidia-v100 and https://lifeinformatica.com/tienda/cisco-nvidia-tesla-v100-32gb-hbm2-cloud-data-center-tarjeta-grafica-profesional
15. AMD Instinct MI50 32GB driver page, https://www.amd.com/en/support/downloads/drivers.html/accelerators/instinct/instinct-mi-series/instinct-mi50-32gb.html
16. ROCm Linux system requirements (7.14.0), https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html
17. Ryzen AI Max+ 395 secondary specs, https://www.tomshardware.com/pc-components/cpus/amds-beastly-strix-halo-ryzen-ai-max-debuts-with-radical-new-memory-tech-to-feed-rdna-3-5-graphics-and-zen-5-cpu-cores and https://www.notebookcheck.net/AMD-Ryzen-AI-Max-395-Processor-Benchmarks-and-Specs.942323.0.html
18. lhl strix-halo-testing llm-bench, https://github.com/lhl/strix-halo-testing/tree/main/llm-bench
19. Apple M3 Ultra 819 GB/s via secondary: https://macworld.com/article/2973459/2026-mac-studio-m5-release-date-specs-price-rumors.html (and search result text)
20. Apple newsroom Mac Studio Mar 2025, https://www.apple.com/newsroom/2025/03/apple-unveils-new-mac-studio-the-most-powerful-mac-ever/
21. llama.cpp Apple Silicon performance, https://github.com/ggml-org/llama.cpp/discussions/4167
22. Apple Mac Studio specs, https://www.apple.com/mac-studio/specs/
23. Apple newsroom MacBook Pro M5 Pro/Max (Mar 2026), https://www.apple.com/newsroom/2026/03/apple-introduces-macbook-pro-with-all-new-m5-pro-and-m5-max/
24. M5 Mac Studio launch coverage, https://9to5mac.com/2026/08/25/apple-unveils-next-generation-mac-studio-with-m5-max-and-m5-ultra/ and https://petapixel.com/2026/08/25/apples-new-mac-studio-supports-up-to-512gb-of-unified-memory/
25. Databricks LLM inference performance engineering (2023-10-12), https://www.databricks.com/blog/llm-inference-performance-engineering-best-practices
26. llama.cpp CUDA scoreboard, https://github.com/ggml-org/llama.cpp/discussions/15013
27. llama.cpp Vulkan scoreboard, https://github.com/ggml-org/llama.cpp/discussions/10879
28. ComputingForGeeks dual RTX 3090 LLM build (tests 2026-10-19), https://computingforgeeks.com/build-dual-rtx-3090-llm/
29. llama.cpp DGX Spark thread, https://github.com/ggml-org/llama.cpp/discussions/16578
30. llama.cpp quantize README, https://github.com/ggml-org/llama.cpp/blob/master/tools/quantize/README.md
31. Llama 3.1 70B config (unsloth mirror), https://huggingface.co/unsloth/Meta-Llama-3.1-70B/raw/main/config.json
32. Llama 3.1 8B config (unsloth mirror), https://huggingface.co/unsloth/Meta-Llama-3.1-8B/raw/main/config.json
33. llama.cpp multi-GPU doc, https://github.com/ggml-org/llama.cpp/blob/master/docs/multi-gpu.md
34. vLLM parallelism and scaling, https://docs.vllm.ai/en/latest/serving/parallelism_scaling.html
35. vLLM GPU installation, https://docs.vllm.ai/en/latest/getting_started/installation/gpu.html
36. eGPU benchmark aggregators (secondary, low-medium): https://localaimaster.com/blog/egpu-local-ai-benchmarks and https://localaimaster.com/blog/thunderbolt-vs-oculink-ai
37. Reddit/forum PCIe-lane anecdotes via search, https://lr.us.psf.lt/r/LocalLLaMA/comments/1bhstjq/how_much_data_is_transferred_across_the_pcie_bus
38. Thunderbolt/OCuLink bandwidth coverage, https://plugable.com/blogs/news/what-s-the-difference-between-thunderbolt-4-and-thunderbolt-5 and https://www.pcgameshardware.de/Grafikkarten-Grafikkarte-97980/News/eGPU-Vergleich-Thunderbolt-5-Oculink-bleibt-zurueck-identischer-Datenrate-1483548/
39. Tom's Hardware OCuLink RTX 4090 tests, https://www.tomshardware.com/pc-components/gpus/high-end-external-gpus-still-suffer-a-performance-hit-oculink-tests-show-up-to-a-23-drop-with-an-rtx-4090
40. CUDA Toolkit release notes, https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/index.html
41. NVIDIA blog on GPU architecture support, https://developer.nvidia.com/blog/navigating-gpu-architecture-support-a-guide-for-nvidia-cuda-developers
42. Ollama GPU docs, https://docs.ollama.com/gpu
43. MLX install, https://ml-explore.github.io/mlx/build/html/install.html
44. ROCm on Windows compatibility, https://rocm.docs.amd.com/projects/radeon-ryzen/en/latest/docs/compatibility/compatibilityrad/windows/windows_compatibility.html
45. llama.cpp SYCL backend doc, https://github.com/ggml-org/llama.cpp/blob/master/docs/backend/SYCL.md
46. intel/ipex-llm (archived 2026-01-28), https://github.com/intel/ipex-llm
47. RTX 50 Super delay coverage, https://www.tomshardware.com/pc-components/gpus/report-claims-nvidia-will-not-be-releasing-any-new-rtx-gaming-gpus-in-2026-rtx-60-series-likely-debuting-in-2028 and https://www.tweaktown.com/news/109694/geforce-rtx-50-super-series-delayed-indefinitely-as-nvidia-informs-its-partners/

