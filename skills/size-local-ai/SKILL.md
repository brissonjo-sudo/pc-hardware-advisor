---
name: size-local-ai
description: This skill should be used when the user wants to size a PC, GPU, APU, mini-PC or Mac for running local LLMs, and asks things like "how much VRAM do I need to run", "what GPU for local LLM", "how many tokens per second will I get", "can I run a 70B model on", "is an eGPU good for local AI", "will two 3090s run a 70B model", or "which quantization fits in 24 GB". Covers model size, quantization, KV cache, memory bandwidth, tok/s estimates, multi-GPU, eGPU, unified memory and software stacks (CUDA, ROCm, Vulkan, SYCL, Metal). The user may write in any language. Not for gaming GPU choice, price hunting (use hunt-prices), part compatibility, or cloud/API inference.
---

# Size a machine for local AI inference

Answer in the user's language. Keep model names, quant names and units as-is. Open with the verdict (recommended card or machine), then the numbers, then limits.

## Rules that always apply

- Treat specs, prices and software support from memory as hypotheses. Take them from `${CLAUDE_PLUGIN_ROOT}/references/gpu-bandwidth-ai.md` (dated 2026-11-07). If a value matters and the reference is older than a month, or the product is newer than the reference, re-check with `~~web search` / `~~web fetch` and cite the page with its date.
- Never present an estimate as a measurement. Label every tok/s figure `estimate` and show the method. When a measured benchmark in the reference matches the hardware, model and quant, cite it first, with its conditions (backend, context, date, source).
- Prices: do not invent any. If the user gave a budget, compare against it. For current prices, apply the `hunt-prices` method (canonical price rows with date, seller type, landed price). With no row, write "price to check".
- Unread, blocked or JavaScript-only pages: record them as `blocked (<reason>)` in the answer. Never circumvent (no alternate user agents, caches, mirrors or archive copies, no browser automation to dodge a block). Ask the user for a screenshot or pasted text and continue with other sources.
- Never buy, create accounts, submit forms or contact sellers. Use no personal data.
- Scope: desktop PCs, mini-PCs and APU systems, Macs as inference machines, eGPU, used parts. Laptops as products, phones, consoles and cloud rentals are out of scope: say so politely and suggest what the user can check.

## Step 0: collect inputs

Ask only for what is missing, in one short message. Needed:

1. Models wanted, with parameter count and architecture type (dense or MoE).
2. Quantization tolerance (Q8, Q4_K_M, lower) and quality expectations.
3. Context length needed (4k, 16k, 32k, 128k).
4. Concurrency (one user, or several simultaneous users).
5. Use: chat, coding, agents, RAG with long prompts, fine-tuning or training.
6. OS preference (Windows, Linux, macOS).
7. Existing hardware (GPU, PCIe slots, PSU, case, RAM).
8. Budget and country (for price rows).

If the model is unnamed, ask one clarifying question. Do not guess a model size.

## Step 1: memory needed (compute it explicitly)

`needed = weights + KV cache + overhead + margin`

1. Weights = parameters x bits per weight / 8. Read the bpw table in section 4 of the reference. Q4_K_M is about 4.9 bpw, not 4.0. If the user names a real file, use its size.
2. KV cache = 2 x layers x KV heads x head_dim x context x bytes per element. Read layers, KV heads and head_dim from the model's config (`~~web fetch` of the model card or config). If the config was not read, say so and give the Llama 3.1 8B / 70B figures from the reference as orders of magnitude only. Quantized KV halves the cache roughly but is unavailable in tensor split mode.
3. Overhead = 1-2 GB per GPU plus about 0.5-1 GB for the display on a desktop GPU.
4. Margin = about 10%.
5. MoE: all experts must be resident (or offloaded to RAM, which is slow); bandwidth counts only active experts.
6. Show the sum line by line. Mark each line `arithmetic`, `reference [n]` or `assumption`. Fine-tuning needs far more than inference (gradients and optimizer state): the reference has no figures for it, so say "not verified" and keep the advice qualitative.

Read `${CLAUDE_PLUGIN_ROOT}/skills/size-local-ai/references/sizing-worksheet.md` when the user wants a step-by-step calculation or when you need a template and worked examples.

## Step 2: candidate hardware by capacity

1. Open the capacity/bandwidth table in section 1 of the reference. Keep only devices whose memory fits `needed` (alone, or summed over GPUs with layer split).
2. Note status: new, used, datacenter. Note the confidence of each bandwidth value (derived or secondary values are medium).
3. Check physical fit with the other references when relevant: `${CLAUDE_PLUGIN_ROOT}/references/power-supplies-connectors.md` (PSU, connectors) and `${CLAUDE_PLUGIN_ROOT}/references/form-factors-cases.md` (card size, slots, PCIe lanes). Quote them; do not guess.

## Step 3: decode speed estimate

Decode (token generation) is memory-bandwidth-bound:

`tok/s = efficiency x peak bandwidth / bytes read per token`

- Bytes read per token = weight bytes (dense) or active-expert bytes (MoE), plus the KV cache read at the working context.
- Efficiency range from the reference (section 2): 0.6 conservative, 0.7 typical, never above 0.85. Show the result as a range, for example "estimate 29-38 tok/s", not one number. Mention that the fastest cards and older Apple Ultra chips sit lower (50-65%, 42-45% on a 7B) and APUs with measured bandwidth sit near 90% of the measured figure.
- Long context lowers the figure. The reference has one data point (15-35% loss at 16-32k); apply it as a range and label it.
- Prefill (prompt processing) is compute-bound, not bandwidth-bound. For long prompts, RAG or agents with big contexts, compare compute and measured prefill rates (reference section 3), not bandwidth. Apple chips decode acceptably but prefill several times slower than a recent NVIDIA card.
- Concurrency: single-stream numbers do not scale to several users. The reference has one vLLM data point (aggregate 148.8 tok/s at 8 users versus 31.25 for one). Cite it as a measurement on that setup only.
- When a measured row matches (same hardware, model, quant), cite it and give its conditions; otherwise give the estimate and say which measured row was used to pick the efficiency.
- Where the reference lacks a measurement for the hardware (for example RTX 5070 Ti, 5080, 4060 Ti, 5060 Ti, Apple Ultra 70B), say "no measurement found" and keep the range wide.

## Step 4: multi-GPU and eGPU rules

Read sections 5 and 6 of the reference before advising.

- Capacity adds, single-stream speed does not. Layer split (llama.cpp default) uses one GPU at a time: speed is about that of one card's bandwidth over the whole model.
- Tensor split can raise speed on NVIDIA CUDA but is experimental in llama.cpp, needs flash attention and unquantized KV cache, and is interconnect-sensitive. Cite the measured dual-3090 rows with their conditions (PCIe 3.0 x16, no NVLink, single-author blog).
- NVLink exists only on GeForce RTX 3090 and 3090 Ti (2-way bridge). Not on 4090 or 5090.
- Cards need slots, lanes, PSU and airflow: check the other references. Do not promise x16/x16 on a consumer board; check the board manual.
- eGPU: OCuLink and Thunderbolt/USB4 lose little on decode when the whole model sits in VRAM (reported 2-6%), but load time rises several-fold and prefill suffers on Thunderbolt 3. Avoid eGPU when the model spills to system RAM, and for multi-eGPU tensor split. These numbers are secondary (blogs): say medium-low confidence.
- A laptop appears only as an eGPU host.

## Step 5: software stack fit per OS

Read section 7 of the reference. Check the user's OS and card against it.

- NVIDIA CUDA runs everything (llama.cpp, Ollama, LM Studio, vLLM on Linux/WSL, ExLlama, training). CUDA 13 dropped Maxwell, Pascal and Volta: those cards stay on CUDA 12.x, and vLLM needs compute capability 7.5 or higher. Tell the user this limit applies to P40 and V100.
- AMD: ROCm supported list is narrow; the MI50 is unsupported; Ryzen AI Max+ 395 is not on AMD's Linux list yet works through community or nightly builds; Windows ROCm is PyTorch only. Vulkan in llama.cpp is a vendor-neutral fallback and was competitive in the measured rows.
- Intel Arc: llama.cpp via SYCL or Vulkan; IPEX-LLM was archived on 2026-01-28; OpenVINO not verified.
- Apple: Metal and MLX on macOS; best memory per currency unit, weakest prefill.
- Software support changes fast. Re-check the exact card against the vendor's current support list before recommending a used or unusual card.

## Step 6: used and datacenter card caveats

When recommending used or datacenter cards (3090, P40, V100, MI50, others), state:

- Cooling: datacenter PCIe cards are passive and need forced airflow; no video output on some. Treat this as general knowledge, not source-verified.
- Driver and software support: CUDA 13 dropped Pascal and Volta; ROCm does not support the MI50. A card can be cheap and already end-of-life.
- Condition risks, test checklists and fair-price method: point to `${CLAUDE_PLUGIN_ROOT}/references/used-market-checklist.md`; seller trust to `${CLAUDE_PLUGIN_ROOT}/references/retailer-criteria.md`. Prices follow the `hunt-prices` method. Never present a used price range as a final price.
- Bandwidth for P40 and V100 is medium confidence (secondary sources).

## Step 7: present the recommendation

Use this structure, conclusion first:

1. **Recommended**: one card or machine, with capacity, bandwidth (value and confidence), and why it fits `needed`.
2. **Memory budget**: the line-by-line sum from Step 1.
3. **Speed**: decode range labelled `estimate`, the formula with the efficiency used, prefill note, and the matching measured benchmark if any (conditions and source).
4. **Alternatives** (one or two): for example a cheaper smaller-quant option, a unified-memory option, or two cards. Each with the trade-off.
5. **What it will NOT do**: for example models that do not fit at the wanted context, slow dense 70B on an APU, training limits, missing software support, prefill on Apple, speed not scaling with a second GPU.
6. **Budget**: compare with the user's budget using canonical price rows from the `hunt-prices` method; otherwise write "price to check". Never invent a price.
7. **Not verified**: list every unchecked item (config not read, bandwidth derived, no matching benchmark, software support to re-check).
8. **Next action**: one concrete step, for example "run the `hunt-prices` method for this card in your country", or "send me the model's config link".

Typical shape of the trade-off to explain (from the reference, not a recommendation to repeat blindly): small and mid dense models favour high-bandwidth discrete GPUs; large MoE models favour large unified memory (APU, DGX Spark, Mac) because only active experts are read per token; dense 70B at Q4 needs about 40+ GB plus KV and runs slowly on 256 GB/s class memory.

## Source hierarchy reminder

Official vendor pages and software docs first; independent benchmarks and community scoreboards second; forum anecdotes last, labelled. Community benchmark rows carry build and hardware differences: cite them as such. Quote at most the numbers, not long text.

## Self-check before answering

1. Is the conclusion first, with one named recommendation?
2. Is the memory sum shown, with weights, KV cache, overhead and margin?
3. Is every tok/s figure labelled estimate or measurement, with method or conditions?
4. Is the efficiency shown as a range, never above 0.85?
5. Is multi-GPU speed treated honestly (capacity adds, speed does not)?
6. Is the software stack checked for the user's OS and card, including end-of-support limits?
7. Is anything price-related either a canonical row or "price to check"?
8. Are blocked pages recorded, gaps listed under "Not verified", and one next action given?
