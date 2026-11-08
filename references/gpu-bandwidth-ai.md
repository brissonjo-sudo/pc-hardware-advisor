# GPU bandwidth and local AI sizing

Last checked: 2026-11-07. Values change: verify online before concluding.

Use this file to size hardware for local LLM inference. `[n]` points to `## Sources`. Confidence follows `${CLAUDE_PLUGIN_ROOT}/references/research-method.md`: high (solid), medium (plausible), low (to verify). "Read" = value read on the cited page (fetch-tool summary). "Derived" = arithmetic from bus width x memory speed, or taken from a secondary source; capped at medium, reason in the row. "Estimate" = inference, not a measurement.

## 1. Memory capacity and bandwidth (checked 2026-11-07)

Bandwidth is peak theoretical: a ceiling, never a delivered speed.

| Device | Memory | Bus / type | GB/s | NVLink | Status | Src | Confidence (why) |
|---|---|---|---|---|---|---|---|
| RTX 3060 12GB | 12 GB | 192-bit GDDR6 | 360 | not listed | used/new | [1][10] | medium (derived 192-bit x 15 Gbps; vendor page) |
| RTX 3090 | 24 GB | 384-bit GDDR6X | 936 | Yes, 2-way | used | [1][2][10] | high capacity/bus; medium bandwidth (secondary table) |
| RTX 3090 Ti | 24 GB | 384-bit GDDR6X | ~1008 | Yes | used | [1][2] | medium (derived 21 Gbps x 384/8) |
| RTX 4060 Ti 16GB | 16 GB | 128-bit GDDR6 | ~288 | No | new/used | [1] | medium (derived) |
| RTX 4070 Ti SUPER | 16 GB | 256-bit GDDR6X | ~672 | No | new/used | [1] | medium (derived) |
| RTX 4080 SUPER | 16 GB | 256-bit GDDR6X | ~736 | No | new/used | [1] | medium (derived) |
| RTX 4090 | 24 GB | 384-bit GDDR6X | ~1008 | No | used/new | [1][3] | medium (derived, not fetched) |
| RTX 5060 Ti 16GB | 16 GB | 128-bit GDDR7 | 448 | not listed | new | [1] | high |
| RTX 5070 Ti | 16 GB | 256-bit GDDR7 | 896 | not listed | new | [1] | high |
| RTX 5080 | 16 GB | 256-bit GDDR7 | 960 | not listed | new | [1] | high |
| RTX 5090 | 32 GB | 512-bit GDDR7 | 1792 | No | new | [1][4] | high |
| RTX PRO 6000 Blackwell | 96 GB GDDR7 ECC | 512-bit (estimate) | not stated by NVIDIA; ~1792 reported | not stated | new, pro (600/300/400-600 W) | [5] | medium capacity; low bandwidth (not on page) |
| RX 7900 XTX | 24 GB | 384-bit GDDR6 | 960 | none | new/used | [11] | medium (secondary; AMD page timed out) |
| RX 9070 XT | 16 GB | 256-bit GDDR6 | 640 | none | new | [11] | medium (secondary) |
| Radeon AI PRO R9700 | 32 GB | 256-bit GDDR6 | 640 (644.6 calc), 300 W | none | new, pro | [12] | medium (secondary) |
| Arc B580 | 12 GB | 192-bit GDDR6 | 456 | none | new | [6] | high |
| Arc Pro B60 | 24 GB | 192-bit GDDR6 | 456, 120-200 W | none | new, pro, via integrators | [7][13] | high (spec) |
| Tesla P40 | 24 GB GDDR5 | 384-bit (estimate) | ~346-347 | none | used/datacenter, passive, no video out | [14] | medium (secondary) |
| Tesla V100 32GB | 32 GB HBM2 | 4096-bit (estimate) | 900 (marketing; 897 third party) | SXM2 only, not PCIe | used/datacenter, passive | [14] | medium (secondary) |
| Instinct MI50 32GB | 32 GB HBM2 | 4096-bit | ~1024 | Infinity Fabric (not verified) | used/datacenter, 300 W, passive; ROCm unsupported | [15][16] | high |
| Ryzen AI Max+ 395 | up to 128 GB shared LPDDR5X-8000 | 256-bit (community README) | 256 theoretical; ~215-221 measured | n/a | new (mini PCs, laptops) | [17][18] | medium-high (AMD page timed out) |
| DGX Spark (GB10) | 128 GB LPDDR5X | 256-bit | 273 | n/a (ConnectX-7) | new | [8] | high |
| Apple M3 Ultra | up to 512 GB | unified | "over 800" Apple; 819 secondary | n/a | new (2025) | [20][19] | high 800+; medium 819 |
| Apple M4 Max | up to 128 GB | unified | 410 (32-GPU) / 546 (40-GPU) | n/a | new (2025) | [20][21] | high |
| Apple M5 Max | up to 128 GB | LPDDR5X-9600 (secondary) | 460 (32-GPU) / 614 (40-GPU) | n/a | new, MacBook Pro 2026-03-11; Mac Studio from 2026-09-22 (secondary) | [22][23][24] | high |
| Apple M5 Ultra | up to 512 GB | unified | 1228 (llama.cpp table); "1.2 TB/s" Apple | n/a | new, Mac Studio 2026; 512 GB config reported late Oct 2026 | [22][21][24] | medium-high |


## 2. Estimation method

Decode (batch 1) is memory-bound; prefill is compute-bound ("generating the first token is typically compute-bound", later tokens memory-bound [25], dated 2023-10-12). Choose by bandwidth for chat speed, by compute for long prompts and RAG. Evidence: M2/M3 Ultra prefill about 1,000-1,500 tok/s on a 7B versus 5,000-6,000 on an RTX 3090, with similar decode [21].

`decode tok/s <= MBU x B_peak / bytes_read_per_token`

- Bytes per token = weight file size (dense) + KV cache read at the current context [25].
- MoE: count active-expert bytes for bandwidth, keep all experts resident. Routing overhead suggests lower MBU (estimate).
- Published MBU: 60% on 2x H100-80GB, 55% on 4x A100-40GB, 50% in a 7B example, all batch 1; it falls as batch rises [25].

### Efficiency from measured data

Estimate = measured tg128 / (peak / file size). File: Llama 2 7B Q4_0, about 3.8 GB (3.56 GiB), recalled and not re-verified (see `## Not verified`): absolute level low confidence.

| Hardware (backend) | Peak GB/s | Ceiling | Measured tg128 | Efficiency | Src |
|---|---|---|---|---|---|
| RTX 3090 (CUDA) | 936 | ~244 | 151-178 | 62-73% | [26] |
| RTX 4090 (CUDA) | 1008 | ~263 | 186-189 | ~71% | [26] |
| RTX 5090 (CUDA) | 1792 | ~468 | 240-300 | 51-64% | [26] |
| RX 7900 XTX (Vulkan) | 960 | ~251 | 183-191 | 73-76% | [27] |
| RX 9070 XT (Vulkan) | 640 | ~167 | 137-142 | 82-85% | [27] |
| Arc B580 (Vulkan) | 456 | ~119 | 70-72 | 59-61% | [27] |
| Strix Halo (Vulkan) | 256 | ~67 | 52-54 | 77-81% (about 95% of measured 215-221) | [27][18] |
| M2/M3 Ultra | 800 | ~209 | 88-94 | 42-45% | [21] |
| M4 Max 40 GPU | 546 | ~143 | 83 | 58% | [21] |
| M5 Max 40 GPU | 614 | ~160 | 120 | 75% | [21] |

Reading (medium):
- Discrete NVIDIA/AMD GPUs reach 60-80% on small dense models; the 5090 drops to 50-65% (launch overhead); Apple 45-75%, older Ultra worst; APUs about 90% of measured bandwidth.
- **Planning factors: 0.6 conservative, 0.7 typical, never above 0.85.**
- Large dense models fill the pipeline better: 2x RTX 3090, Llama 3.3 70B Q4_K_M (42.5 GB), layer split, 19.5 tok/s versus ceiling 936/42.5 = 22, about 89% of one card's bandwidth [28].
- Context cost: DGX Spark gpt-oss-120b MXFP4 decode 60.6 tok/s at depth 0, 54.1 at 4k, 47.5 at 16k, 40.6 at 32k [29]. Plan a 15-35% loss at 16-32k (estimate, one data point).

## 3. Measured benchmarks

llama.cpp unless noted; pp512/tg128 unless noted; n/s = not stated. Scoreboard rows [26][27] are community-submitted with differing builds. Prefill and decode shown as "FA off / FA on" where two values appear.

| Hardware | Model, quant | Backend | Prefill | Decode | Src, date |
|---|---|---|---|---|---|
| RTX 3090 | Llama 2 7B Q4_0 | CUDA c76b420 | 5174 / 5560 | 158 / 162 | [26] 2025-08-01 |
| RTX 3090 | same | CUDA build 10809 | 5154 / 5974 | 169 / 178 | [26] 2026-09-07 |
| RTX 4090 | same | CUDA build 6098 | 11993 / 14771 | 186 / 189 | [26] 2025-08-06 |
| RTX 5090 | same | CUDA 600 W build 6060 | 14752 / 16042 | 240 / 249 | [26] 2025-08-02 |
| RTX 5090 | same | CUDA 8cf6b42 | 14073 / 14970 | 290 / 300 | [26] n/s |
| RX 7900 XTX | same | Vulkan | 3727 / 3890 | 183 / 191 | [27] undated |
| Arc B580 | same | Vulkan | 621 / 419 | 70 / 72 | [27] undated |
| Ryzen AI Max+ 395 | same | Vulkan | 1487 / 1704 | 52 / 54 | [27] undated |
| Ryzen AI Max+ 395 | Qwen3 30B-A3B MoE UD-Q4_K_XL | HIP rocWMMA FA / Vulkan | 669 | 58.5 / 78.0 | [18] ~2025 |
| Ryzen AI Max+ 395 | gpt-oss 120B MoE MXFP4 | Vulkan AMDVLK | 431 | 33.7 | [18] ~2025 |
| Ryzen AI Max+ 395 | Shisa V2 70B dense i1-Q4_K_M | HIP rocWMMA | 94.7 | 4.5 | [18] ~2025 |
| 2x RTX 3090 (PCIe 3.0 x16 each, no NVLink, 290 W cap) | Llama 3.3 70B Q4_K_M (42.5 GB) | CUDA layer split b11741 | 577 | 19.5 | [28] 2026-10-19 |
| 2x RTX 3090 (same) | same | CUDA tensor split (experimental) | 763 | 31.9 (29.9 at 8K, prefill 656) | [28] 2026-10-19 |
| 1 vs 2x RTX 3090 | Qwen3 32B Q4_K_M | CUDA, tensor split for 2 | 1198 vs 1578 | 35.3 vs 59.8 | [28] 2026-10-19 |
| 2x RTX 3090 | Llama 3.3 70B AWQ, 1 user | vLLM 0.31.0 TP=2 | TTFT 0.72 s | 31.25 (148.8 aggregate at 8 users) | [28] 2026-10-19 |
| DGX Spark | gpt-oss 120B MXFP4, pp2048/tg32, depth 0 | CUDA b6922 | 1956 | 60.6 | [29] ~Oct 2025 |
| M3 Ultra (80 GPU) | Llama 2 7B Q4_0 (not gpt-oss 120B) | Metal | 1471 | 92.1 | [21] commit 8e672ef |
| M4 Max (40 GPU) | Llama 2 7B Q4_0 (not gpt-oss 120B) | Metal | 886 | 83.1 | [21] commit 8e672ef |
| M5 Max (40 GPU) | Llama 2 7B Q4_0 / Q8_0 / F16 | Metal | 3220 / 3144 / 3158 | 119.9 / 72.4 / 37.1 | [21] c1d0e7a, 2026 |
| M5 Ultra (80 GPU) | same | Metal | 4945 / 4911 / 5207 | 179.1 / 119.0 / 73.6 | [21] c1d0e7a, 2026 |

Notes: [21] lists the M3 Ultra at 800 GB/s (Apple and secondary sources say 819). Dual-3090 rows come from one single-author blog (medium). No measured Apple Ultra 70B Q4 decode was found; secondary sites disagree (14 to 24 tok/s) and are not measurements; theory ceiling at 819 GB/s is about 19-20 tok/s, realistic 45-60% of that (estimate). No measured tok/s for 5070 Ti, 5080, 4060 Ti, 5060 Ti.

## 4. Memory sizing

Bits per weight, llama.cpp quantize README (Llama 3.1 8B) [30], high:

| Type | bpw | Bytes/weight | 8B size (GiB) |
|---|---|---|---|
| F16 | 16.00 | 2.000 | 14.96 |
| Q8_0 | 8.50 | 1.063 | 7.95 |
| Q6_K | 6.56 | 0.820 | 6.14 |
| Q5_K_M | 5.70 | 0.713 | 5.33 |
| Q4_K_M | 4.89 | 0.612 | 4.58 |
| Q4_K_S | 4.67 | 0.583 | 4.36 |
| IQ4_XS | 4.46 | 0.557 | 4.17 |
| Q3_K_M | 4.00 | 0.500 | 3.74 |
| Q2_K | 3.16 | 0.395 | 2.95 |
| IQ1_S | 2.00 | 0.250 | 1.87 |

Q4_K_M is about 4.9 bpw, not 4.0. Weight bytes = parameters x bpw / 8. For 70B: Q4_K_M about 42 GB (measured file 42.5 GB = 39.59 GiB, Llama 3.3 70B [28]), Q8_0 about 74 GB, F16 about 140 GB (arithmetic). MoE: all experts resident; only active experts count for bandwidth.

KV cache: `bytes = 2 x n_layers x n_kv_heads x head_dim x context_tokens x bytes_per_element` (F16 = 2; Q8_0 about 1.06; Q4_0 about 0.56). Read the three config values from the model's config. From unsloth mirrors of Meta configs [31][32] (high for the arithmetic):

| Model | Layers | KV heads | head_dim | Per token | 8k | 32k | 128k |
|---|---|---|---|---|---|---|---|
| Llama 3.1 8B | 32 | 8 (of 32) | 128 | 128 KiB | 1.0 GiB | 4.0 GiB | 16 GiB |
| Llama 3.1 70B | 80 | 8 (of 64) | 128 | 320 KiB | 2.5 GiB | 10 GiB | 40 GiB |

Without grouped-query attention (64 KV heads) the 70B cache would be 8x larger.

Overhead (estimate): reserve 1-2 GB per GPU for compute buffers and CUDA context, about 10% headroom, and 0.5-1 GB for the display on a Windows desktop GPU. Measured on 2x 24 GB, 70B Q4_K_M: 20.8 GiB per card at default context, 22.1 GiB at 8K filled [28].

Worked example, 70B Q4_K_M at 32k: weights 39.6 GiB + KV 10 GiB + overhead 1-2 GiB per GPU + 5-10% margin = about 55 GiB. Needs 2x 32 GB or 3x 24 GB. 2x 24 GB fits only at about 8k: 39.6 + 2.5 + overhead = about 44-46 GiB.

## 5. Multi-GPU

- llama.cpp `--split-mode` [33] (high): `layer` (default) is pipeline parallelism, tolerates a slow interconnect; capacity sums, single-stream speed does not (one GPU active at a time). `row` is deprecated. `tensor` is experimental: needs flash attention, KV cache f16/bf16/f32 only (no quantized KV), best on several NVIDIA GPUs with CUDA, interconnect-sensitive, NCCL recommended, not implemented for many MoE/SSM/hybrid models. Peer-to-peer (`GGML_CUDA_P2P`) is opt-in and usually limited to workstation and datacenter GPUs.
- Measured, 2x RTX 3090, PCIe 3.0 x16, no NVLink, 70B Q4_K_M: layer 19.5 tok/s, tensor 31.9 (1.64x). Qwen3 32B: 35.3 on one card versus 59.8 tensor on two (1.69x) [28] (blog, medium).
- vLLM [34]: tensor parallel needs fast links; without NVLink prefer pipeline parallel. vLLM is Linux only [35]. ExLlama tensor parallel: no primary source (gap).
- PCIe lanes: with the model fully in VRAM, single-GPU decode has no meaningful PCIe traffic (OCuLink about 1% utilised, forum anecdote [36]); layer split tolerates x1-x4 for decode (anecdotal). Tensor parallel cares: one report of 4x P100 limited at PCIe 3.0 x4, about 10% loss from x16 to x8 [37] (anecdote, low). Lanes mostly affect load time and prefill with offloading.
- NVLink: 3090/3090 Ti only; not 4090/5090 [1][2][4]. Consumer 4090/5090 often lack peer-to-peer across PCIe (estimate; [33]).

## 6. eGPU links

| Link | Raw | Usable PCIe | Src |
|---|---|---|---|
| OCuLink (PCIe 4.0 x4) | 16 GT/s x 4 | about 64 Gbps raw (7-7.8 GB/s) | [38] |
| Thunderbolt 3/4, USB4 40 Gbps | 40 Gbps | about 32 Gbps (PCIe 3.0 x4 equivalent); one article reports about 22 Gbps real-world, unverified | [38] |
| Thunderbolt 5 | 80 Gbps | PCIe Gen4 x4 = 64 Gbps tunnel | [38] |

Measured effects (secondary blogs, medium-low; no controlled llama.cpp study across links):
- Decode, model in VRAM: Llama 3.1 8B Q4_K_M, RTX 4090: 142 tok/s internal versus 138 over OCuLink (-3%). Another blog: OCuLink -1.8%, TB4 -5.4%, USB4 -5.9% (8B); -1.5% OCuLink, -4.9% TB4 (70B). RTX 3090 over TB3, offloaded 70B+: 2.33 versus 2.27 tok/s. Outlier: RTX 4090 over TB3, Mistral 7B, 62 versus 100 tok/s (-38%), not generalised by its author [36].
- Prompt processing, 2,048 tokens, TB3 versus internal on a 3090: 140 versus 304 tok/s (-54%). 70B load: internal 1.9 s, OCuLink 5.4 s, TB5 6.8 s, TB4 13.2 s, USB4 13.6 s.
- Conclusion (estimate, medium): one eGPU holding the whole model loses about 2-6% decode over OCuLink/TB4; load time rises several-fold; prefill suffers on TB3. Avoid eGPU when the model spills to RAM and for multi-eGPU tensor split.

## 7. Software stacks (checked 2026-11-07)

| Stack | Support status | Runs | OS | Src |
|---|---|---|---|---|
| NVIDIA CUDA | CUDA 13.0 removed offline compilation and library support for Maxwell, Pascal, Volta (cc below 7.5) [40][41]; they still run on CUDA 12.x (NVIDIA suggests 12.9 + driver branch 580, supported to about 2028 [41]). Ollama: cc 5.0+, driver 570+ for cc 5.0-6.2 [42]. vLLM: cc 7.5+ [35]. MLX CUDA: SM 7.5+, driver 550.54.14+ [43]. | llama.cpp, Ollama, LM Studio, vLLM, ExLlama, PyTorch training | Linux, Windows (vLLM Linux/WSL) | [35][40-43] |
| AMD ROCm | 7.14.0 production on Linux. Supported Radeon: RX 7900 XTX/XT, 7800 XT, 9070 XT, 9070, AI PRO R9700, PRO W7900. Ryzen AI Max+ 395 not on AMD's Linux list (works via TheRock nightlies/community; vLLM and Ollama list it). **MI50 unsupported** [16]. Linux: Ubuntu 24.04.4/22.04.5, RHEL 10.1/9.7. Windows: ROCm 7.2.1 + PyTorch 2.9, RX 7900 XTX, 9070 XT, 9070, 9060 XT, R9700, W7900, 7700; PyTorch only [44]. | PyTorch, llama.cpp HIP, Ollama, vLLM (Linux), LM Studio | Linux full, Windows limited | [16][35][42][44] |
| Vulkan (llama.cpp) | Vendor-neutral; competitive on AMD, good on Intel Arc, works on NVIDIA (3090 Llama 2 7B Q4_0: pp 4666 vs CUDA 5174, tg 164 vs 158). ROCm versus Vulkan not compared here. | llama.cpp, Ollama, LM Studio | Linux, Windows | [26][27][42] |
| Intel SYCL / oneAPI / OpenVINO | llama.cpp SYCL: Arc A770/A750, B580, Data Center Max, Flex 170, integrated Arc; oneAPI 2025.x-2026.1; Ubuntu 22.04/24.04, Windows 11; Arc Pro B60 only in a performance note [45]. **IPEX-LLM archived by Intel 2026-01-28**, no successor named [46]. vLLM XPU: Arc/Data Center, Python 3.12 [35]. OpenVINO not fetched. | llama.cpp SYCL/Vulkan, vLLM XPU | Linux best, Windows | [35][45][46] |
| Apple Metal / MLX | MLX: Apple silicon, macOS 14.0+, Python 3.10+ [43]. llama.cpp, Ollama, LM Studio use Metal [42]. MLX 4-bit 70B reported about 15% faster than llama.cpp (secondary, low). | llama.cpp, Ollama, LM Studio, MLX, PyTorch MPS | macOS | [42][43] |


## 8. Hardware status 2025-2026 (checked 2026-11-07)

- **RTX 50 Super**: not released as of this check. **Rumours:** reports (Jan-Feb 2026) say NVIDIA delayed the refresh indefinitely because of memory costs (rumoured 24 GB 5070 Ti Super/5080 Super); The Information via Tom's Hardware: no new gaming GPUs in 2026, RTX 60 not before 2028. NVIDIA has not confirmed. No source newer than Feb 2026 [47]. Medium that none launched: verify before advising to wait.
- **Pro and new entrants**: RTX PRO 6000 Blackwell 96 GB (Workstation 600 W, Max-Q 300 W, Server 400-600 W) [5]. Radeon AI PRO R9700 32 GB, about 1,299 USD at retail launch, ROCm Linux and Windows [12][16][44]. Arc Pro B60 24 GB, about 500 USD via integrators; Maxsun dual-B60 48 GB reported 1,200-3,000 USD, limited supply [7][13]. Prices low confidence: use the `hunt-prices` method.
- **Unified memory**: Ryzen AI Max+ 395 and DGX Spark suit MoE models (gpt-oss 120B 33.7 and about 60 tok/s decode); dense 70B is slow (4.5 tok/s on Strix Halo) [18][29].
- **Apple**: M5 Pro/Max MacBook Pro shipped 2026-03-11. M5 Max/M5 Ultra Mac Studio announced 2026-08-25 (Ultra 512 GB, about 1.2 TB/s, from 5,499 USD; M5 Max from 2,499 USD), shipping from 2026-09-22 (secondary [24]; spec page [22]). M5 Max prefill about 2.2x the M3 Ultra [21].

## Not verified

- AMD official pages (R9700, 7900 XTX, 9070 XT, Ryzen AI Max+ 395) timed out; secondary sources used. TechPowerUp returned HTTP 403 and was not bypassed [9]. Meta's Hugging Face repo returned 401; unsloth mirrors used.
- Bandwidth for 3090 Ti, 4060 Ti, 4070 Ti SUPER, 4080 SUPER, 4090 and RTX PRO 6000 is derived or recalled, not fetched; NVIDIA pages do not publish it.
- P40/V100 datasheets unreadable. Passive cooling, fan-shroud/EPS power needs and Windows WDDM limits are general knowledge, not source-verified.
- No source for ExLlamaV2/V3 tensor parallelism, OpenVINO, LM Studio runtime support or measured Apple 70B decode. No controlled x4 versus x16 PCIe benchmark. eGPU numbers come from blogs; the 22 Gbps Thunderbolt cap is unconfirmed.
- **The Llama 2 7B Q4_0 file size (3.56 GiB, about 3.8 GB) was recalled, not re-fetched; the section 2 efficiency ratios depend on it (low confidence on their absolute level).**
- No measured tok/s for 5070 Ti, 5080, 4060 Ti, 5060 Ti. The 15-35% context loss rests on one data point. MoE efficiency is an estimate.
- Strix Halo bus width not confirmed by AMD. Pricing, used availability, power and running costs out of scope.

## Sources

All checked 2026-11-07. Unless marked, fetched (tool summary). "sec." = secondary page; "snip." = search snippet only; "comm." = community post.

1. NVIDIA GeForce compare, https://www.nvidia.com/en-us/geforce/graphics-cards/compare/
2. NVIDIA RTX 3090/3090 Ti, https://www.nvidia.com/en-us/geforce/graphics-cards/30-series/rtx-3090-3090ti/
3. NVIDIA RTX 4090, https://www.nvidia.com/en-us/geforce/graphics-cards/40-series/rtx-4090/
4. NVIDIA RTX 5090, https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5090/
5. NVIDIA RTX PRO 6000 family, https://www.nvidia.com/en-us/products/workstations/professional-desktop-gpus/rtx-pro-6000-family/
6. Intel Arc B580, https://www.intel.com/content/www/us/en/products/sku/241598/intel-arc-b580-graphics/specifications.html
7. Intel Arc Pro B60, https://www.intel.com/content/www/us/en/products/sku/243916/intel-arc-pro-b60-graphics/specifications.html
8. NVIDIA DGX Spark, https://www.nvidia.com/en-us/products/workstations/dgx-spark/
9. TechPowerUp RTX 5090 page: blocked (HTTP 403), not read, no workaround.
10. Gigabyte 3060 spec / Techgage 3090 launch table (sec., snip.), https://www.gigabyte.com/id/Graphics-Card/GV-N3060EAGLE-12GD-rev-10/sp
11. Tom's Hardware RX 9070 XT review; gpu-monkey comparison (sec.), https://www.tomshardware.com/pc-components/gpus/amd-radeon-rx-9070-xt-review
12. Tom's Hardware / HotHardware, Radeon AI PRO R9700 (sec.), https://www.tomshardware.com/pc-components/gpus/amd-launches-radeon-ai-pro-r9700-to-challenge-nvidias-ai-market-dominance
13. TweakTown, Maxsun Arc Pro B60 Dual 48GB (sec.), https://www.tweaktown.com/news/107051/maxsuns-new-arc-pro-b60-dual-48gb-ships-next-week-intel-gpu-card-costs-1200/index.html
14. P40 vs V100 (sec.), https://hmc-tech.com/gpu/nvidia-tesla-p40-vs-nvidia-v100
15. AMD Instinct MI50 driver page, https://www.amd.com/en/support/downloads/drivers.html/accelerators/instinct/instinct-mi-series/instinct-mi50-32gb.html
16. ROCm Linux system requirements 7.14.0, https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html
17. Tom's Hardware / Notebookcheck, Strix Halo (sec.), https://www.notebookcheck.net/AMD-Ryzen-AI-Max-395-Processor-Benchmarks-and-Specs.942323.0.html
18. lhl strix-halo-testing llm-bench (comm.), https://github.com/lhl/strix-halo-testing/tree/main/llm-bench
19. Macworld, M3 Ultra 819 GB/s (sec., snip.), https://macworld.com/article/2973459/2026-mac-studio-m5-release-date-specs-price-rumors.html
20. Apple newsroom, Mac Studio 2025-03, https://www.apple.com/newsroom/2025/03/apple-unveils-new-mac-studio-the-most-powerful-mac-ever/
21. llama.cpp Apple Silicon performance (comm.), https://github.com/ggml-org/llama.cpp/discussions/4167
22. Apple Mac Studio specs, https://www.apple.com/mac-studio/specs/
23. Apple newsroom, MacBook Pro M5 Pro/Max 2026-03, https://www.apple.com/newsroom/2026/03/apple-introduces-macbook-pro-with-all-new-m5-pro-and-m5-max/
24. 9to5Mac / PetaPixel, M5 Mac Studio launch (sec.), https://9to5mac.com/2026/08/25/apple-unveils-next-generation-mac-studio-with-m5-max-and-m5-ultra/
25. Databricks, LLM inference performance engineering (2023-10-12), https://www.databricks.com/blog/llm-inference-performance-engineering-best-practices
26. llama.cpp CUDA scoreboard (comm.), https://github.com/ggml-org/llama.cpp/discussions/15013
27. llama.cpp Vulkan scoreboard (comm.), https://github.com/ggml-org/llama.cpp/discussions/10879
28. ComputingForGeeks, dual RTX 3090 build (tests 2026-10-19; single-author blog), https://computingforgeeks.com/build-dual-rtx-3090-llm/
29. llama.cpp DGX Spark thread (comm.), https://github.com/ggml-org/llama.cpp/discussions/16578
30. llama.cpp quantize README, https://github.com/ggml-org/llama.cpp/blob/master/tools/quantize/README.md
31. Llama 3.1 70B config (unsloth mirror), https://huggingface.co/unsloth/Meta-Llama-3.1-70B/raw/main/config.json
32. Llama 3.1 8B config (unsloth mirror), https://huggingface.co/unsloth/Meta-Llama-3.1-8B/raw/main/config.json
33. llama.cpp multi-GPU doc, https://github.com/ggml-org/llama.cpp/blob/master/docs/multi-gpu.md
34. vLLM parallelism and scaling, https://docs.vllm.ai/en/latest/serving/parallelism_scaling.html
35. vLLM GPU installation, https://docs.vllm.ai/en/latest/getting_started/installation/gpu.html
36. localaimaster eGPU benchmarks (sec., low-medium), https://localaimaster.com/blog/egpu-local-ai-benchmarks
37. Forum PCIe-lane anecdote (snip.), https://lr.us.psf.lt/r/LocalLLaMA/comments/1bhstjq/how_much_data_is_transferred_across_the_pcie_bus
38. Plugable / PCGH, Thunderbolt and OCuLink bandwidth (sec.), https://plugable.com/blogs/news/what-s-the-difference-between-thunderbolt-4-and-thunderbolt-5
39. Tom's Hardware, OCuLink RTX 4090 tests, https://www.tomshardware.com/pc-components/gpus/high-end-external-gpus-still-suffer-a-performance-hit-oculink-tests-show-up-to-a-23-drop-with-an-rtx-4090
40. CUDA Toolkit release notes, https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/index.html
41. NVIDIA blog, GPU architecture support, https://developer.nvidia.com/blog/navigating-gpu-architecture-support-a-guide-for-nvidia-cuda-developers
42. Ollama GPU docs, https://docs.ollama.com/gpu
43. MLX install, https://ml-explore.github.io/mlx/build/html/install.html
44. ROCm on Windows compatibility, https://rocm.docs.amd.com/projects/radeon-ryzen/en/latest/docs/compatibility/compatibilityrad/windows/windows_compatibility.html
45. llama.cpp SYCL doc, https://github.com/ggml-org/llama.cpp/blob/master/docs/backend/SYCL.md
46. intel/ipex-llm (archived 2026-01-28), https://github.com/intel/ipex-llm
47. Tom's Hardware / TweakTown, RTX 50 Super delay (sec., rumours), https://www.tomshardware.com/pc-components/gpus/report-claims-nvidia-will-not-be-releasing-any-new-rtx-gaming-gpus-in-2026-rtx-60-series-likely-debuting-in-2028
