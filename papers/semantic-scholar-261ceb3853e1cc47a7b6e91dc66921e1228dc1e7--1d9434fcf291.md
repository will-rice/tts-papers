---
arxiv_id: s2:261ceb3853e1cc47a7b6e91dc66921e1228dc1e7
title:
  Efficient and Natural Tibetan Speech Synthesis via Gaussian Noise-Improved
  Monotonic Alignment Search and Lightweight iSTFT Multiband Decoder
authors:
  - Shiqi Wu
  - Yue Zhao
  - Jing Yu
  - Xiaona Xu
  - Haizhou Li
submitted: "2025-09-01"
categories: []
arxiv_url: https://www.semanticscholar.org/paper/261ceb3853e1cc47a7b6e91dc66921e1228dc1e7
source: metadata-only
converter: none
llm_remediated: false
citations_resolved: 0/0
citations_resolved_at: "2026-07-07T15:56:15+00:00"
references_parsed: 0
arxiv_version: ""
---

## Abstract

Although end-to-end speech synthesis technology has made significant progress in general domains, Tibetan speech synthesis still faces issues such as inaccurate alignment and unnatural synthesis due to its unique linguistic features and low-resource data sparsity. To address these challenges, this paper proposes the EnhancedTTS model, which incorporates a random duration predictor based on generative adversarial networks, a Gaussian noise-enhanced monotonic alignment search algorithm, and a Transformer block with residual connections to significantly improve the modeling accuracy of complex Tibetan syllable boundaries. Additionally, the model uses iSTFT and multi-band parallel strategies in the decoder to enhance inference speed. Furthermore, Tibetan character components are used as modeling units, providing a more accurate representation of Tibetan’s unique phonetic and structural features. To validate the e ff ectiveness of the proposed model, experiments were conducted using a Tibetan Amdo dialect dataset, and comparisons were made with the VITS and FastSpeech2 models. The results show significant breakthroughs in both speech quality and e ffi ciency. The MOS score reached 4.69, improving by 3.1% and 1.5% over VITS and FastSpeech2. Objective tests showed significant optimizations in RMSE and MCD, with inference speed increasing by 2-5 times. Ablation experiments further confirmed the e ff ectiveness of the key modules.
