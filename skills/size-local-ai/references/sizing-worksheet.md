# Sizing worksheet

Last checked: 2026-11-07. Values change: verify online before concluding.

Read this file when the user wants a step-by-step calculation. Reference numbers come from `${CLAUDE_PLUGIN_ROOT}/references/gpu-bandwidth-ai.md` (cited "ref §n"; its sources are [n] there). Tag every number: `ref` (traced to the reference), `arith` (arithmetic from tagged numbers), `assumption` (state it), `user` (given by the user).

## Worksheet (fill in)

| # | Item | Formula | Value |
|---|---|---|---|
| 1 | Parameters P (billions) | user / model card | |
| 2 | Quant bpw | ref §4 table (Q4_K_M 4.89, Q8_0 8.50, Q6_K 6.56) | |
| 3 | Weights W (GB) | P x bpw / 8 (GiB = GB / 1.0737) | |
| 4 | KV per token (KiB) | 2 x layers x KV heads x head_dim x bytes / 1024; read the three numbers from the model config | |
| 5 | KV total (GiB) | row 4 x context / 1,048,576 | |
| 6 | Overhead (GiB) | 1-2 per GPU + 0.5-1 display (ref §4) | |
| 7 | Margin | about 10% of total memory (ref §4) | |
| 8 | Needed (GiB) | W + KV + overhead + margin | |
| 9 | Fits? | memory (one card, or sum over layer-split cards) versus row 8 | |
| 10 | Bytes per token (GB) | W (dense) or active-expert bytes (MoE) + KV read | |
| 11 | Ceiling tok/s | peak GB/s / row 10 | |
| 12 | Estimate range | efficiency 0.6 to 0.8 (never above 0.85) x row 11 | |
| 13 | Context correction | apply 15-35% loss at 16-32k, one data point (ref §2) | |
| 14 | Measured match | closest row in ref §3: hardware, model, quant, backend, date | |

Prefill is compute-bound: do not use rows 10-12 for it; use the measured prefill column in ref §3.

## Example A: 32B Q4_K_M at 16k context on one 24 GB card (RTX 3090)

Inputs: P = 32 (`user`); bpw 4.89 (`ref` §4); context 16,384 (`user`); card 24 GB, 936 GB/s peak (`ref` §1, 936 is medium confidence).

1. Weights: 32 x 4.89 / 8 = 19.56 GB = 18.2 GiB (`arith`).
2. KV per token: the reference holds no 32B config. Read layers, KV heads and head_dim from the model's config before concluding. For scale only: Llama 3.1 8B is 128 KiB/token and Llama 3.1 70B is 320 KiB/token (`ref` §4).
3. Memory left for KV. Conservative (Windows desktop, 2 GiB overhead, 1 GiB display, 10% margin = 2.4 GiB): 24 - 18.2 - 2 - 1 - 2.4 = 0.4 GiB (`arith`). Optimistic (headless Linux, 1 GiB overhead, 5% margin = 1.2 GiB): 24 - 18.2 - 1 - 1.2 = 3.6 GiB (`arith`). The 24 GB is treated as 24 GiB; check the actual usable amount.
4. KV budget per token over 16,384 tokens: 0.4 GiB gives about 24 KiB/token; 3.6 GiB gives about 229 KiB/token (`arith`).
5. Verdict: it fits only if the model's F16 KV is under that budget. With a placeholder of 128 KiB/token (`assumption`, the 8B figure), KV = 2.0 GiB at 16k: it fails the conservative case and fits the optimistic one. Quantized KV (Q8_0, about 1.06 bytes versus 2 for F16, `ref` §4) roughly halves the cache. Say "to verify with the real config".
6. Bytes per token: 19.56 GB + KV read 2.0 GiB (2.15 GB, with the placeholder) = 21.7 GB (`arith`).
7. Ceiling: 936 / 21.7 = 43.1 tok/s. Range at 0.6-0.8: 26-35 tok/s (`arith`). Label: estimate.
9. Measured match: Qwen3 32B Q4_K_M on one RTX 3090, 35.3 tok/s decode, llama.cpp CUDA, default test context (not 16k), tests 2026-10-19, single-author blog (`ref` §3, source [28]). That is 74% of the 47.9 ceiling (`arith`), inside the 0.6-0.8 range. Do not claim the measurement holds at 16k.

## Example B: 70B Q4_K_M on 2 x 24 GB, or on a 128 GB unified-memory APU

Inputs: Llama 3.3 70B Q4_K_M file 42.5 GB = 39.59 GiB (`ref` §3-4, [28]); KV 320 KiB/token, so 8k = 2.5 GiB and 32k = 10 GiB (`ref` §4).

**B1. Two 24 GB cards (RTX 3090, layer split)**

1. At 8k: 39.6 + 2.5 = 42.1 GiB, plus overhead 2 x (1-2) = 2-4 GiB, plus display 0.5-1 GiB = 44.6-47.1 GiB versus 48 GiB (`arith`). Fits with under 4 GiB spare; the 10% margin (4.8 GiB) is not met. Measured peak: 20.8 GiB per card at default context, 22.1 GiB per card at 8K filled (`ref` §4, [28]), so 44.2 GiB total.
2. At 32k: 39.6 + 10 + 1-2 per GPU = about 55 GiB (`ref` §4). It does not fit in 48 GiB. It needs 2 x 32 GB or 3 x 24 GB.
3. Ceiling: 936 / 42.5 = 22.0 tok/s (`arith`, one card's bandwidth because layer split uses one GPU at a time, `ref` §5). Measured: 19.5 tok/s layer split, 577 tok/s prefill, PCIe 3.0 x16 each, no NVLink, 290 W cap (`ref` §3, [28]). That is 89% of the ceiling.
4. Tensor split measured 31.9 tok/s (29.9 at 8K). It is experimental, needs flash attention and an unquantized KV cache (`ref` §5).

**B2. 128 GB unified-memory APU (Ryzen AI Max+ 395)**

1. Memory: 39.6 + 10 (32k) = 49.6 GiB before overhead, well inside 128 GB shared (`arith`). The share of 128 GB the GPU may use was not verified.
2. Ceiling: 256 GB/s theoretical gives 256 / 42.5 = 6.0 tok/s; measured bandwidth 215-221 gives about 5.1 tok/s (`arith`, `ref` §1).
3. Measured: Shisa V2 70B i1-Q4_K_M dense, 4.5 tok/s decode, 94.7 tok/s prefill, HIP rocWMMA, about 2025 (`ref` §3, [18]). A different file from Llama 3.3, so the match is approximate.
4. Will not do: comfortable dense 70B chat or fast long-prompt prefill. MoE models fit this hardware better (gpt-oss 120B MXFP4 measured 33.7 tok/s, `ref` §3).

**B3. Other options (estimates only)**

- Apple M3 Ultra class: theory ceiling about 19-20 tok/s; realistic 45-60% of it, so roughly 9-12 tok/s (`ref` §3 notes, estimate). No measured Ultra 70B number was found.

Prices: use the `hunt-prices` method; otherwise "price to check".
