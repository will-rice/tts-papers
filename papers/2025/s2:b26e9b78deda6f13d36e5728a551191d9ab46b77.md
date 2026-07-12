---
arxiv_id: s2:b26e9b78deda6f13d36e5728a551191d9ab46b77
title: Fast Inference End-to-End Speech Synthesis with Style Diffusion
authors:
  - Hui Sun
  - Jiyeoun Song
  - Yi Jiang
submitted: "2025-07-15"
categories: []
arxiv_url: https://www.semanticscholar.org/paper/b26e9b78deda6f13d36e5728a551191d9ab46b77
source: metadata-only
converter: none
llm_remediated: false
citations_resolved: 0/0
citations_resolved_at: "2026-07-07T15:58:26+00:00"
references_parsed: 0
arxiv_version: ""
---

## Abstract

In recent years, deep learning-based end-to-end Text-To-Speech (TTS) models have made significant progress in enhancing speech naturalness and fluency. However, existing Variational Inference Text-to-Speech (VITS) models still face challenges such as insufficient pitch modeling, inadequate contextual dependency capture, and low inference efficiency in the decoder. To address these issues, this paper proposes an improved TTS framework named Q-VITS. Q-VITS incorporates Rotary Position Embedding (RoPE) into the text encoder to enhance long-sequence modeling, adopts a frame-level prior modeling strategy to optimize one-to-many mappings, and designs a style extractor based on a diffusion model for controllable style rendering. Additionally, the proposed decoder ConfoGAN integrates explicit F0 modeling, Pseudo-Quadrature Mirror Filter (PQMF) multi-band synthesis and Conformer structure. The experimental results demonstrate that Q-VITS outperforms the VITS in terms of speech quality, pitch accuracy, and inference efficiency in both subjective Mean Opinion Score (MOS) and objective Mel-Cepstral Distortion (MCD) and Root Mean Square Error (RMSE) evaluations on a single-speaker dataset, achieving performance close to ground-truth audio. These improvements provide an effective solution for efficient and controllable speech synthesis.
